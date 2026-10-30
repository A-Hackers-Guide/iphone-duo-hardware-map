# `MTLDebugVisibleFunctionTable`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsVisibleFunctionTable`
- Protocols: `MTLDebugResourcePurgeable`
- 5 instance variables, 2 properties, 14 instance methods, 0 class methods

## Instance variables

```
{atomic<int>="__a_"{__cxx_atomic_impl<int, std::__cxx_atomic_base_impl<int>>="__a_value"Ai}} _purgeableStateToken;
B _purgeableStateHasBeenSet;
Q _functionCount;
@"MTLToolsObject" _pipelineState;
Q _stage;
```

## Properties

```
@property (TQ,R,V_functionCount) functionCount;
@property (TQ,R,V_stage) stage;
```

## Instance methods

```
-[MTLDebugVisibleFunctionTable functionCount];
-[MTLDebugVisibleFunctionTable formattedDescription:];
-[MTLDebugVisibleFunctionTable stage];
-[MTLDebugVisibleFunctionTable dealloc];
-[MTLDebugVisibleFunctionTable setFunction:atIndex:];
-[MTLDebugVisibleFunctionTable setPurgeableState:];
-[MTLDebugVisibleFunctionTable setFunctions:withRange:];
-[MTLDebugVisibleFunctionTable description];
-[MTLDebugVisibleFunctionTable initWithBaseObject:parent:];
-[MTLDebugVisibleFunctionTable purgeableStateValidForRendering];
-[MTLDebugVisibleFunctionTable initWithVisibleFunctionTable:parent:descriptor:pipelineState:stage:];
-[MTLDebugVisibleFunctionTable initWithVisibleFunctionTable:parent:descriptor:stage:];
-[MTLDebugVisibleFunctionTable lockPurgeableState];
-[MTLDebugVisibleFunctionTable unlockPurgeableState];
```
