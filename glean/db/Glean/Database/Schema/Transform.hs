{-
  Copyright (c) Meta Platforms, Inc. and affiliates.
  All rights reserved.

  This source code is licensed under the BSD-style license found in the
  LICENSE file in the root directory of this source tree.
-}

module Glean.Database.Schema.Transform
  ( mkPredicateTransformation
  , transformPat
  , transitiveDeps
  ) where

import Data.List (elemIndex)
import Data.Bifoldable
import qualified Data.Map.Strict as Map
import Data.Map.Strict (Map)
import Data.Maybe (fromMaybe, listToMaybe)
import Data.Text (Text)
import qualified Data.Set as Set
import Data.Word (Word64)

import Glean.Angle.Types (FieldDef_(..))
import qualified Glean.Angle.Types as Type
import Glean.Query.Codegen
import Glean.Database.Schema.Types
import qualified Glean.RTS as RTS
import Glean.RTS.Types
import Glean.RTS.Term (Value, Term(..))
import Glean.Schema.Util (lowerMaybe, lowerBool, lowerEnum)
import qualified Glean.Types as Thrift

mkPredicateTransformation
  :: (Pid -> PredicateDetails)
  -> Pid
  -> Pid
  -> Maybe PredicateTransformation
mkPredicateTransformation detailsFor fromPid toPid
  | fromPid == toPid = Nothing
  | otherwise = Just PredicateTransformation
    { tRequested = from
    , tAvailable = to
    , tTransformKey = transform
        (predicateKeyType from)
        (predicateKeyType to)
    , tTransformValue = transform
        (predicateValueType from)
        (predicateValueType to)
    , tTransformFactBack = fromMaybe id $
        mkFactTransformation to from
    }
  where
      to = detailsFor toPid
      from = detailsFor fromPid
      transform from to pat = transformPat overUnit overVar from to pat
      overUnit _ _ () = ()
      overVar _ _ var = var

transitiveDeps :: (Pid -> PredicateDetails) -> Pid -> [Pid]
transitiveDeps = transitive . predicateDeps
  where
    -- All predicates mentioned in a predicate's type.
    -- Does not include predicates from the derivation query.
    predicateDeps :: (Pid -> PredicateDetails) -> Pid -> [Pid]
    predicateDeps detailsFor pred =
      typeDeps (predicateKeyType details) <>
        typeDeps (predicateValueType details)
      where
        details = detailsFor pred
        typeDeps = bifoldMap overPidRef overExpanded
        overExpanded (ExpandedType _ ty) = typeDeps ty
        overPidRef (PidRef pid _) = [pid]

    transitive :: Ord a => (a -> [a]) -> a -> [a]
    transitive next root = Set.elems $ go (next root) mempty
      where
        go [] visited = visited
        go (x:xs) visited
          | x `Set.member`visited = go xs visited
          | otherwise = go xs $ go (next x) $ Set.insert x visited

transformPat :: (Show a, Show b)
  => (Type -> Type -> a -> c)
  -> (Type -> Type -> b -> d)
  -> Type
  -> Type
  -> Term (Match a b)
  -> Term (Match c d)
transformPat innerL innerR from@(Type.NamedType _) to pat =
  transformPat innerL innerR (derefType from) to pat
transformPat innerL innerR from to@(Type.NamedType _) pat =
  transformPat innerL innerR from (derefType to) pat
transformPat innerL innerR from to pat = case pat of
  Byte x -> Byte x
  Nat x -> Nat x
  ByteArray x -> ByteArray x
  String x -> String x
  Ref match -> Ref $ case match of
    -- we can keep variable bindings as they are given any value of type T
    -- assigned to a variable will have been changed to type transformed(T).
    MatchBind var -> MatchBind $ innerR from to var
    MatchVar var -> MatchVar $ innerR from to var
    MatchWild _ -> MatchWild to
    MatchNever _ -> MatchNever to
    MatchFid fid -> MatchFid fid
    MatchAnd a b -> MatchAnd
      (transform from to a)
      (transform from to b)
    MatchPrefix prefix rest -> MatchPrefix prefix $ transform from to rest
    MatchExt extra -> MatchExt $ innerL from to extra
  Alt fromIx term
    | Type.Boolean <- from
    , Type.Boolean <- to ->
        transform lowerBool lowerBool pat
    | Type.Maybe fromTy <- from
    , Type.Maybe toTy <- to ->
        transform (lowerMaybe fromTy) (lowerMaybe toTy) pat
    | Type.Enumerated fromAlts <- from
    , Type.Enumerated toAlts <- to ->
        transform
          (lowerEnum fromAlts)
          (lowerEnum toAlts)
          pat
    | Type.Sum fromAlts <- from
    , Type.Sum toAlts <- to
    -- alternatives could change order
    , Just fromAlt <- fromAlts `maybeAt` fromIntegral fromIx
    , Just toIx <-
        elemIndex (fieldDefName fromAlt) (fieldDefName <$> toAlts)
    , Just toAlt <- toAlts `maybeAt` toIx ->
        Alt (fromIntegral toIx) $ transform
          (fieldDefType fromAlt)
          (fieldDefType toAlt)
          term
  Array terms
    | Type.Array fromTy <- from
    , Type.Array toTy <- to ->
      Array $ transform fromTy toTy <$> terms
  Tuple terms
    | Type.Record fromFields <- from
    , Type.Record toFields <- to
    ->  let termsMap = Map.fromList
              [ (name, (fromTy, term))
              | (FieldDef name fromTy, term) <- zip fromFields terms ]
            termForField  (FieldDef name toTy) =
              case Map.lookup name termsMap of
                Just (fromTy, term) -> transform fromTy toTy term
                Nothing -> Ref (MatchWild toTy)
        in
        Tuple $ fmap termForField toFields
  _ -> error "unexpected"
  where
    maybeAt list ix = listToMaybe (drop ix list)
    transform = transformPat innerL innerR

mkFactTransformation
  :: PredicateDetails
  -> PredicateDetails
  -> Maybe (Thrift.Fact -> Thrift.Fact)
mkFactTransformation from to
  | Nothing <- mTransformKey
  , Nothing <- mTransformValue = Nothing
  | otherwise = Just $ \(Thrift.Fact _ key value) ->
     Thrift.Fact
       (fromPid $ predicatePid to)
       (RTS.fromValue $ overKey $ RTS.toValue keyRep key)
       (RTS.fromValue $ overValue $ RTS.toValue valueRep value)
  where
    overKey = fromMaybe id mTransformKey
    overValue = fromMaybe id mTransformValue
    keyRep = repType $ predicateKeyType from
    valueRep = repType $ predicateValueType from
    mTransformKey = mkValueTransformation
      (predicateKeyType from)
      (predicateKeyType to)
    mTransformValue = mkValueTransformation
      (predicateValueType from)
      (predicateValueType to)

-- | Create a transformation from a term into another term of a compatible
-- type.  Returns Nothing if no change is needed.
mkValueTransformation :: Type -> Type -> Maybe (Value -> Value)
mkValueTransformation from to = go from to
  where
    names = map fieldDefName

    -- if an option's definition and index didn't change it
    -- will not have an entry in this map.
    transformationsFor
      :: [FieldDef]
      -> [FieldDef]
      -> Map Text (Word64, Value -> Value)
    transformationsFor from to = Map.fromList
      [ (name, (ixTo, f))
      | (FieldDef name defFrom, ixFrom) <- zip from [0..]
      , Just (ixTo, f) <- return $ do
          case Map.lookup name toFields of
            Nothing -> Just unknown
            Just (ixTo, defTo) ->
              case go defFrom defTo of
                Nothing | ixTo == ixFrom -> Nothing
                Nothing -> Just (ixTo, id)
                Just f -> Just (ixTo, f)
      ]
      where
        unknown = (fromIntegral (length to), const (Tuple []))

        toFields :: Map Text (Word64, Type)
        toFields = Map.fromList $ flip map (zip to [0..])
          $ \(FieldDef name def, ix) -> (name, (ix, def))

    go :: Type -> Type -> Maybe (Value -> Value)
    go from@(Type.NamedType _) to = go (derefType from) to
    go from to@(Type.NamedType _) = go from (derefType to)
    go Type.Byte Type.Byte = Nothing
    go Type.Nat Type.Nat = Nothing
    go Type.String Type.String = Nothing
    go Type.Boolean Type.Boolean = Nothing
    go (Type.Maybe from) (Type.Maybe to) = go (lowerMaybe from) (lowerMaybe to)
    go (Type.Predicate _) (Type.Predicate _) = Nothing
    go (Type.Enumerated from) (Type.Enumerated to) =
      go (lowerEnum from) (lowerEnum to)
    go (Type.Array from) (Type.Array to) = do
      f <- go from to
      return $ \term -> case term of
        Array vs -> Array (map f vs)
        _ -> error $ "expected Array, got " <> show term

    go (Type.Record from) (Type.Record to) =
      let transformationsMap = transformationsFor from to
          transformations =
            [ (field, transform)
            | field <- names to
            , transform <- [maybe id snd $ Map.lookup field transformationsMap]
            ]
          noChange = null transformationsMap
      in
      if noChange
      then Nothing
      else Just $ \term -> case term of
        Tuple contents -> Tuple
          [ transform content
          | (field, transform) <- transformations
          , Just content <- [lookup field withNames]
          ]
          where withNames = zip (names from) contents
        _ -> error $ "expected Tuple, got " <> show term

    go (Type.Sum from) (Type.Sum to) =
      let transformations = transformationsFor from to
          noChange = Map.null transformations
          altMap = Map.fromList
              [ (ixFrom, (ixTo, change))
              | (name, ixFrom) <- zip (names from) [0..]
              , Just (ixTo, change) <- [Map.lookup name transformations]
              ]
      in
      if noChange
        then Nothing
        else Just $ \term -> case term of
          Alt n content -> case Map.lookup n altMap of
            Nothing -> Alt n content
            Just (n', change) -> Alt n' (change content)
          _ -> error $ "expected Alt, got " <> show term
    go from to =
      error $ "invalid type conversion: "
        <> show from <> " to " <> show to
