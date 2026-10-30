# `MTLDebugIndirectCommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsIndirectCommandBuffer`
- Protocols: `MTLDebugResourcePurgeable`
- 7 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _optimizedRangeList;
@"MTLIndirectCommandBufferDescriptor" _desc;
Q _maxCommandCount;
@"<MTLIndirectCommandBuffer>" _iCB;
B _isRender;
{atomic<int>="__a_"{__cxx_atomic_impl<int, std::__cxx_atomic_base_impl<int>>="__a_value"Ai}} _purgeableStateToken;
B _purgeableStateHasBeenSet;
```

## Properties

```
@property (T@"NSMutableArray",R) optimizedRangeList;
@property (T@"MTLIndirectCommandBufferDescriptor",R) descriptor;
```

## Instance methods

```
-[MTLDebugIndirectCommandBuffer descriptor];
-[MTLDebugIndirectCommandBuffer dealloc];
-[MTLDebugIndirectCommandBuffer setPurgeableState:];
-[MTLDebugIndirectCommandBuffer resetWithRange:];
-[MTLDebugIndirectCommandBuffer indirectComputeCommandAtIndex:];
-[MTLDebugIndirectCommandBuffer indirectRenderCommandAtIndex:];
-[MTLDebugIndirectCommandBuffer purgeableStateValidForRendering];
-[MTLDebugIndirectCommandBuffer initWithIndirectCommandBuffer:device:descriptor:maxCommandCount:options:];
-[MTLDebugIndirectCommandBuffer lockPurgeableState];
-[MTLDebugIndirectCommandBuffer optimizedRangeList];
-[MTLDebugIndirectCommandBuffer unlockPurgeableState];
```
