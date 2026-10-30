# `MTLDebugIntersectionFunctionTable`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsIntersectionFunctionTable`
- Protocols: `MTLDebugResourcePurgeable`
- 5 instance variables, 2 properties, 18 instance methods, 0 class methods

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
-[MTLDebugIntersectionFunctionTable functionCount];
-[MTLDebugIntersectionFunctionTable formattedDescription:];
-[MTLDebugIntersectionFunctionTable stage];
-[MTLDebugIntersectionFunctionTable dealloc];
-[MTLDebugIntersectionFunctionTable setFunction:atIndex:];
-[MTLDebugIntersectionFunctionTable setPurgeableState:];
-[MTLDebugIntersectionFunctionTable setFunctions:withRange:];
-[MTLDebugIntersectionFunctionTable description];
-[MTLDebugIntersectionFunctionTable initWithBaseObject:parent:];
-[MTLDebugIntersectionFunctionTable setOpaqueCurveIntersectionFunctionWithSignature:atIndex:];
-[MTLDebugIntersectionFunctionTable setOpaqueCurveIntersectionFunctionWithSignature:withRange:];
-[MTLDebugIntersectionFunctionTable setOpaqueTriangleIntersectionFunctionWithSignature:atIndex:];
-[MTLDebugIntersectionFunctionTable setOpaqueTriangleIntersectionFunctionWithSignature:withRange:];
-[MTLDebugIntersectionFunctionTable purgeableStateValidForRendering];
-[MTLDebugIntersectionFunctionTable initWithIntersectionFunctionTable:parent:descriptor:pipelineState:stage:];
-[MTLDebugIntersectionFunctionTable initWithIntersectionFunctionTable:parent:descriptor:stage:];
-[MTLDebugIntersectionFunctionTable lockPurgeableState];
-[MTLDebugIntersectionFunctionTable unlockPurgeableState];
```
