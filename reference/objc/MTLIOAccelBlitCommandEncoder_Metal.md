# `MTLIOAccelBlitCommandEncoder`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLIOAccelCommandEncoder`
- 0 instance variables, 0 properties, 20 instance methods, 0 class methods

## Instance methods

```
-[MTLIOAccelBlitCommandEncoder waitForFence:];
-[MTLIOAccelBlitCommandEncoder updateFence:];
-[MTLIOAccelBlitCommandEncoder sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[MTLIOAccelBlitCommandEncoder synchronizeResource:];
-[MTLIOAccelBlitCommandEncoder copyFromTexture:toTexture:];
-[MTLIOAccelBlitCommandEncoder synchronizeTexture:slice:level:];
-[MTLIOAccelBlitCommandEncoder getType];
-[MTLIOAccelBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:];
-[MTLIOAccelBlitCommandEncoder optimizeContentsForCPUAccess:slice:level:];
-[MTLIOAccelBlitCommandEncoder optimizeIndirectCommandBuffer:withRange:];
-[MTLIOAccelBlitCommandEncoder fillTexture:level:slice:region:color:];
-[MTLIOAccelBlitCommandEncoder optimizeContentsForGPUAccess:];
-[MTLIOAccelBlitCommandEncoder fillBuffer:range:pattern4:];
-[MTLIOAccelBlitCommandEncoder fillTexture:level:slice:region:bytes:length:];
-[MTLIOAccelBlitCommandEncoder resolveCounters:inRange:destinationBuffer:destinationOffset:];
-[MTLIOAccelBlitCommandEncoder fillTexture:level:slice:region:color:pixelFormat:];
-[MTLIOAccelBlitCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:];
-[MTLIOAccelBlitCommandEncoder resetCommandsInBuffer:withRange:];
-[MTLIOAccelBlitCommandEncoder optimizeContentsForCPUAccess:];
-[MTLIOAccelBlitCommandEncoder optimizeContentsForGPUAccess:slice:level:];
```
