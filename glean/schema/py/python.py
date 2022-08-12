# @generated
# To regenerate this file run fbcode//glean/schema/gen/sync
from typing import Union
import json
from glean.schema.py.glean_schema_predicate import GleanSchemaPredicate


class GSPythonNameLowerCase(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.NameLowerCase.1 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonNameLowerCase":
    raise Exception("this function can only be called from @angle_query")

class GSPythonLocalName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.LocalName.3 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonLocalName":
    raise Exception("this function can only be called from @angle_query")

class GSPythonIsTopLevelDefinition(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.IsTopLevelDefinition.3 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonIsTopLevelDefinition":
    raise Exception("this function can only be called from @angle_query")

class GSPythonClassDefinition(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.ClassDefinition.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonClassDefinition":
    raise Exception("this function can only be called from @angle_query")

class GSPythonNonImportDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.NonImportDeclaration.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonNonImportDeclaration":
    raise Exception("this function can only be called from @angle_query")

class GSPythonDeclarationReference(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.DeclarationReference.3 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonDeclarationReference":
    raise Exception("this function can only be called from @angle_query")

class GSPythonDefinitionsByFile(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.DefinitionsByFile.3 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonDefinitionsByFile":
    raise Exception("this function can only be called from @angle_query")

class GSPythonModule(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.Module.1 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonModule":
    raise Exception("this function can only be called from @angle_query")

class GSPythonDefinitionLocation(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.DefinitionLocation.3 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonDefinitionLocation":
    raise Exception("this function can only be called from @angle_query")

class GSPythonClassBySName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.ClassBySName.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonClassBySName":
    raise Exception("this function can only be called from @angle_query")

class GSPythonDeclarationUses(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.DeclarationUses.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonDeclarationUses":
    raise Exception("this function can only be called from @angle_query")

class GSPythonImportStatement(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.ImportStatement.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonImportStatement":
    raise Exception("this function can only be called from @angle_query")

class GSPythonModuleDefinition(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.ModuleDefinition.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonModuleDefinition":
    raise Exception("this function can only be called from @angle_query")

class GSPythonDeclarationBySName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.DeclarationBySName.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonDeclarationBySName":
    raise Exception("this function can only be called from @angle_query")

class GSPythonDeclarationWithSName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.DeclarationWithSName.3 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonDeclarationWithSName":
    raise Exception("this function can only be called from @angle_query")

class GSPythonModuleBySName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.ModuleBySName.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonModuleBySName":
    raise Exception("this function can only be called from @angle_query")

class GSPythonImportStarStatement(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.ImportStarStatement.3 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonImportStarStatement":
    raise Exception("this function can only be called from @angle_query")

class GSPythonDeclarationLocation(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.DeclarationLocation.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonDeclarationLocation":
    raise Exception("this function can only be called from @angle_query")

class GSPythonClassDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.ClassDeclaration.1 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonClassDeclaration":
    raise Exception("this function can only be called from @angle_query")

class GSPythonDeclarationToName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.DeclarationToName.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonDeclarationToName":
    raise Exception("this function can only be called from @angle_query")

class GSPythonDeclarationDefinition(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.DeclarationDefinition.3 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonDeclarationDefinition":
    raise Exception("this function can only be called from @angle_query")

class GSPythonDeclarationByName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.DeclarationByName.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonDeclarationByName":
    raise Exception("this function can only be called from @angle_query")

class GSPythonName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.Name.1 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonName":
    raise Exception("this function can only be called from @angle_query")

class GSPythonImportStatementByName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.ImportStatementByName.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonImportStatementByName":
    raise Exception("this function can only be called from @angle_query")

class GSPythonDocstringContent(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.DocstringContent.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonDocstringContent":
    raise Exception("this function can only be called from @angle_query")

class GSPythonVariableDefinition(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.VariableDefinition.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonVariableDefinition":
    raise Exception("this function can only be called from @angle_query")

class GSPythonType(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.Type.1 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonType":
    raise Exception("this function can only be called from @angle_query")

class GSPythonDirectXRefsByFile(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.DirectXRefsByFile.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonDirectXRefsByFile":
    raise Exception("this function can only be called from @angle_query")

class GSPythonVariableBySName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.VariableBySName.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonVariableBySName":
    raise Exception("this function can only be called from @angle_query")

class GSPythonDeclarationWithLocalName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.DeclarationWithLocalName.3 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonDeclarationWithLocalName":
    raise Exception("this function can only be called from @angle_query")

class GSPythonFileDirectXRefs(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.FileDirectXRefs.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonFileDirectXRefs":
    raise Exception("this function can only be called from @angle_query")

class GSPythonFunctionDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.FunctionDeclaration.1 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonFunctionDeclaration":
    raise Exception("this function can only be called from @angle_query")

class GSPythonSNameToName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.SNameToName.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonSNameToName":
    raise Exception("this function can only be called from @angle_query")

class GSPythonNameToSName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.NameToSName.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonNameToSName":
    raise Exception("this function can only be called from @angle_query")

class GSPythonImportStatementByAsName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.ImportStatementByAsName.3 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonImportStatementByAsName":
    raise Exception("this function can only be called from @angle_query")

class GSPythonFunctionDefinition(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.FunctionDefinition.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonFunctionDefinition":
    raise Exception("this function can only be called from @angle_query")

class GSPythonImportStarsByFile(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.ImportStarsByFile.3 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonImportStarsByFile":
    raise Exception("this function can only be called from @angle_query")

class GSPythonIsTopLevelDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.IsTopLevelDeclaration.3 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonIsTopLevelDeclaration":
    raise Exception("this function can only be called from @angle_query")

class GSPythonSearchByLocalName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.SearchByLocalName.3 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonSearchByLocalName":
    raise Exception("this function can only be called from @angle_query")

class GSPythonDeclarationsByFile(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.DeclarationsByFile.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonDeclarationsByFile":
    raise Exception("this function can only be called from @angle_query")

class GSPythonXRefsViaNameByFile(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.XRefsViaNameByFile.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonXRefsViaNameByFile":
    raise Exception("this function can only be called from @angle_query")

class GSPythonDeclarationWithName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.DeclarationWithName.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonDeclarationWithName":
    raise Exception("this function can only be called from @angle_query")

class GSPythonVariableDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.VariableDeclaration.1 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonVariableDeclaration":
    raise Exception("this function can only be called from @angle_query")

class GSPythonFunctionBySName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.FunctionBySName.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonFunctionBySName":
    raise Exception("this function can only be called from @angle_query")

class GSPythonImportStarLocation(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.ImportStarLocation.3 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonImportStarLocation":
    raise Exception("this function can only be called from @angle_query")

class GSPythonImportStatementByAsSName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.ImportStatementByAsSName.3 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonImportStatementByAsSName":
    raise Exception("this function can only be called from @angle_query")

class GSPythonDefinitionDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.DefinitionDeclaration.3 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonDefinitionDeclaration":
    raise Exception("this function can only be called from @angle_query")

class GSPythonContainingTopLevelDeclaration(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.ContainingTopLevelDeclaration.3 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonContainingTopLevelDeclaration":
    raise Exception("this function can only be called from @angle_query")

class GSPythonSName(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.SName.2 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonSName":
    raise Exception("this function can only be called from @angle_query")

class GSPythonLocalNameLowerCase(GleanSchemaPredicate):
  @staticmethod
  def build_angle(key: Union[str, int]) -> str:
    return f"python.LocalNameLowerCase.3 { json.dumps(key) }"

  @staticmethod
  def angle_query(*, name: str) -> "GSPythonLocalNameLowerCase":
    raise Exception("this function can only be called from @angle_query")

