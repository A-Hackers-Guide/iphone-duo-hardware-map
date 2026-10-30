# `MTLToolsFunctionHandle`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLFunctionHandleSPI`
- 2 instance variables, 11 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"MTLToolsFunction" _function;
@"MTL4ToolsBinaryFunction" _binaryFunction;
```

## Properties

```
@property (T@"MTLToolsFunction",R,V_function) function;
@property (T@"MTL4ToolsBinaryFunction",R,V_binaryFunction) binaryFunction;
@property (TQ,R) resourceIndex;
@property (TQ,R) functionType;
@property (T@"NSString",R) name;
@property (T@"<MTLDevice>",R) device;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsFunctionHandle resourceIndex];
-[MTLToolsFunctionHandle functionType];
-[MTLToolsFunctionHandle function];
-[MTLToolsFunctionHandle dealloc];
-[MTLToolsFunctionHandle gpuResourceID];
-[MTLToolsFunctionHandle name];
-[MTLToolsFunctionHandle binaryFunction];
-[MTLToolsFunctionHandle initWithBaseObject:parent:binaryFunction:];
-[MTLToolsFunctionHandle initWithBaseObject:parent:function:];
```
