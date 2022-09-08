"use strict";(self.webpackChunkwebsite=self.webpackChunkwebsite||[]).push([[23],{3905:function(e,n,t){t.r(n),t.d(n,{MDXContext:function(){return d},MDXProvider:function(){return u},mdx:function(){return h},useMDXComponents:function(){return p},withMDXComponents:function(){return s}});var r=t(67294);function i(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function a(){return a=Object.assign||function(e){for(var n=1;n<arguments.length;n++){var t=arguments[n];for(var r in t)Object.prototype.hasOwnProperty.call(t,r)&&(e[r]=t[r])}return e},a.apply(this,arguments)}function o(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function l(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?o(Object(t),!0).forEach((function(n){i(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):o(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function c(e,n){if(null==e)return{};var t,r,i=function(e,n){if(null==e)return{};var t,r,i={},a=Object.keys(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||(i[t]=e[t]);return i}(e,n);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(i[t]=e[t])}return i}var d=r.createContext({}),s=function(e){return function(n){var t=p(n.components);return r.createElement(e,a({},n,{components:t}))}},p=function(e){var n=r.useContext(d),t=n;return e&&(t="function"==typeof e?e(n):l(l({},n),e)),t},u=function(e){var n=p(e.components);return r.createElement(d.Provider,{value:n},e.children)},m={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},f=r.forwardRef((function(e,n){var t=e.components,i=e.mdxType,a=e.originalType,o=e.parentName,d=c(e,["components","mdxType","originalType","parentName"]),s=p(t),u=i,f=s["".concat(o,".").concat(u)]||s[u]||m[u]||a;return t?r.createElement(f,l(l({ref:n},d),{},{components:t})):r.createElement(f,l({ref:n},d))}));function h(e,n){var t=arguments,i=n&&n.mdxType;if("string"==typeof e||i){var a=t.length,o=new Array(a);o[0]=f;var l={};for(var c in n)hasOwnProperty.call(n,c)&&(l[c]=n[c]);l.originalType=e,l.mdxType="string"==typeof e?e:i,o[1]=l;for(var d=2;d<a;d++)o[d]=t[d];return r.createElement.apply(null,o)}return r.createElement.apply(null,t)}f.displayName="MDXCreateElement"},95673:function(e,n,t){t.r(n),t.d(n,{assets:function(){return p},contentTitle:function(){return d},default:function(){return h},frontMatter:function(){return c},metadata:function(){return s},toc:function(){return u}});var r,i=t(83117),a=t(80102),o=(t(67294),t(3905)),l=["components"],c={id:"haskell",title:"Haskell",sidebar_label:"Haskell"},d=void 0,s={unversionedId:"indexer/haskell",id:"indexer/haskell",title:"Haskell",description:"To index Haskell Glean consumes .hie files produced by the GHC compiler (>=8.8) with the flag -fwrite-ide-info.",source:"@site/docs/indexer/haskell.md",sourceDirName:"indexer",slug:"/indexer/haskell",permalink:"/docs/indexer/haskell",draft:!1,editUrl:"https://github.com/facebookincubator/Glean/tree/main/glean/website/docs/indexer/haskell.md",tags:[],version:"current",frontMatter:{id:"haskell",title:"Haskell",sidebar_label:"Haskell"},sidebar:"someSidebar",previous:{title:"Hack",permalink:"/docs/indexer/hack"},next:{title:"TypeScript",permalink:"/docs/indexer/lsif-typescript"}},p={},u=[{value:"Schema",id:"schema",level:2}],m=(r="SrcFile",function(e){return console.warn("Component "+r+" was not imported, exported, or provided by MDXProvider as global scope"),(0,o.mdx)("div",e)}),f={toc:u};function h(e){var n=e.components,t=(0,a.Z)(e,l);return(0,o.mdx)("wrapper",(0,i.Z)({},f,t,{components:n,mdxType:"MDXLayout"}),(0,o.mdx)("p",null,"To index ",(0,o.mdx)("a",{parentName:"p",href:"https://haskell.org"},"Haskell")," Glean consumes ",(0,o.mdx)("inlineCode",{parentName:"p"},".hie")," files produced by the GHC compiler (>=8.8) with the flag ",(0,o.mdx)("inlineCode",{parentName:"p"},"-fwrite-ide-info"),"."),(0,o.mdx)("h1",{id:"run-the-indexer"},"Run the indexer"),(0,o.mdx)("p",null,"The indexer is run via the main ",(0,o.mdx)("inlineCode",{parentName:"p"},"glean")," CLI tool."),(0,o.mdx)("pre",null,(0,o.mdx)("code",{parentName:"pre"},"BUILD --ghc-options=-fwrite-ide-info\nglean --db-root DBDIR index haskell ROOT --repo name/hash\n")),(0,o.mdx)("p",null,"where"),(0,o.mdx)("ul",null,(0,o.mdx)("li",{parentName:"ul"},(0,o.mdx)("inlineCode",{parentName:"li"},"BUILD")," is a build command such that GHC is called with ",(0,o.mdx)("inlineCode",{parentName:"li"},"-fwrite-ide-info")),(0,o.mdx)("li",{parentName:"ul"},(0,o.mdx)("inlineCode",{parentName:"li"},"DBDIR")," is the directory where the Glean db will be created"),(0,o.mdx)("li",{parentName:"ul"},(0,o.mdx)("inlineCode",{parentName:"li"},"ROOT")," is the root directory containing the build artifacts generated with the ",(0,o.mdx)("inlineCode",{parentName:"li"},"fwrite-ide-info")," flag (e.g. ",(0,o.mdx)("inlineCode",{parentName:"li"},"dist")," if a Cabal project)"),(0,o.mdx)("li",{parentName:"ul"},(0,o.mdx)("inlineCode",{parentName:"li"},"name/hash")," is the name of the repository to create")),(0,o.mdx)("h2",{id:"schema"},"Schema"),(0,o.mdx)("p",null,"The schema is in ",(0,o.mdx)(m,{file:"glean/schema/source/hs.angle",mdxType:"SrcFile"})))}h.isMDXComponent=!0}}]);