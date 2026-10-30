# `MTL4ToolsCompilerTask`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTL4CompilerTaskGGDSPI`
- 1 instance variables, 6 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"<MTL4Compiler>" compiler;
```

## Properties

```
@property (T@"<MTL4Compiler>",R,Vcompiler) compiler;
@property (Tq,R) status;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTL4ToolsCompilerTask compiler];
-[MTL4ToolsCompilerTask waitUntilCompleted];
-[MTL4ToolsCompilerTask tryCancel];
-[MTL4ToolsCompilerTask status];
-[MTL4ToolsCompilerTask initWithBaseObject:parent:];
-[MTL4ToolsCompilerTask initWithCompiler:];
```
