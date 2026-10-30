# `MTLDebugFunctionHandle`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsFunctionHandle`
- Protocols: `MTLFunctionHandleSPI`
- 1 instance variables, 10 properties, 6 instance methods, 0 class methods

## Instance variables

```
Q _stage;
```

## Properties

```
@property (TQ,R,V_stage) stage;
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
-[MTLDebugFunctionHandle resourceIndex];
-[MTLDebugFunctionHandle stage];
-[MTLDebugFunctionHandle gpuResourceID];
-[MTLDebugFunctionHandle initWithBaseObject:parent:binaryFunction:stage:];
-[MTLDebugFunctionHandle initWithBaseObject:parent:function:stage:];
-[MTLDebugFunctionHandle initWithBaseObject:parent:stage:];
```
