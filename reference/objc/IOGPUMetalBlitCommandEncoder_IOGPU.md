# `IOGPUMetalBlitCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalCommandEncoder`
- 0 instance variables, 0 properties, 20 instance methods, 0 class methods

## Instance methods

```
-[IOGPUMetalBlitCommandEncoder waitForFence:];
-[IOGPUMetalBlitCommandEncoder updateFence:];
-[IOGPUMetalBlitCommandEncoder sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[IOGPUMetalBlitCommandEncoder synchronizeResource:];
-[IOGPUMetalBlitCommandEncoder copyFromTexture:toTexture:];
-[IOGPUMetalBlitCommandEncoder synchronizeTexture:slice:level:];
-[IOGPUMetalBlitCommandEncoder getType];
-[IOGPUMetalBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:];
-[IOGPUMetalBlitCommandEncoder optimizeContentsForCPUAccess:slice:level:];
-[IOGPUMetalBlitCommandEncoder optimizeIndirectCommandBuffer:withRange:];
-[IOGPUMetalBlitCommandEncoder fillTexture:level:slice:region:color:];
-[IOGPUMetalBlitCommandEncoder optimizeContentsForGPUAccess:];
-[IOGPUMetalBlitCommandEncoder fillBuffer:range:pattern4:];
-[IOGPUMetalBlitCommandEncoder fillTexture:level:slice:region:bytes:length:];
-[IOGPUMetalBlitCommandEncoder resolveCounters:inRange:destinationBuffer:destinationOffset:];
-[IOGPUMetalBlitCommandEncoder fillTexture:level:slice:region:color:pixelFormat:];
-[IOGPUMetalBlitCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:];
-[IOGPUMetalBlitCommandEncoder resetCommandsInBuffer:withRange:];
-[IOGPUMetalBlitCommandEncoder optimizeContentsForCPUAccess:];
-[IOGPUMetalBlitCommandEncoder optimizeContentsForGPUAccess:slice:level:];
```
