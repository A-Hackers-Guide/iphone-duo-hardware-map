# `IOGPUMetalRenderCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalCommandEncoder`
- 0 instance variables, 0 properties, 53 instance methods, 0 class methods

## Instance methods

```
-[IOGPUMetalRenderCommandEncoder useResources:count:usage:];
-[IOGPUMetalRenderCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:];
-[IOGPUMetalRenderCommandEncoder useResource:usage:];
-[IOGPUMetalRenderCommandEncoder executeCommandsInBuffer:withRange:];
-[IOGPUMetalRenderCommandEncoder useHeap:];
-[IOGPUMetalRenderCommandEncoder useHeaps:count:];
-[IOGPUMetalRenderCommandEncoder sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[IOGPUMetalRenderCommandEncoder setMeshIntersectionFunctionTables:withBufferRange:];
-[IOGPUMetalRenderCommandEncoder setObjectAccelerationStructure:atBufferIndex:];
-[IOGPUMetalRenderCommandEncoder setStencilCleared];
-[IOGPUMetalRenderCommandEncoder setColorStoreAction:atIndex:];
-[IOGPUMetalRenderCommandEncoder initWithCommandBuffer:descriptor:];
-[IOGPUMetalRenderCommandEncoder setFragmentIntersectionFunctionTable:atBufferIndex:];
-[IOGPUMetalRenderCommandEncoder setTileVisibleFunctionTable:atBufferIndex:];
-[IOGPUMetalRenderCommandEncoder setObjectIntersectionFunctionTables:withBufferRange:];
-[IOGPUMetalRenderCommandEncoder setTileAccelerationStructure:atBufferIndex:];
-[IOGPUMetalRenderCommandEncoder setVertexVisibleFunctionTables:withBufferRange:];
-[IOGPUMetalRenderCommandEncoder setStencilStoreActionOptions:];
-[IOGPUMetalRenderCommandEncoder getFragmentBufferContentsAtIndex:];
-[IOGPUMetalRenderCommandEncoder getType];
-[IOGPUMetalRenderCommandEncoder setTileVisibleFunctionTables:withBufferRange:];
-[IOGPUMetalRenderCommandEncoder setVertexIntersectionFunctionTable:atBufferIndex:];
-[IOGPUMetalRenderCommandEncoder setObjectIntersectionFunctionTable:atBufferIndex:];
-[IOGPUMetalRenderCommandEncoder setVertexAccelerationStructure:atBufferIndex:];
-[IOGPUMetalRenderCommandEncoder setFragmentVisibleFunctionTable:atBufferIndex:];
-[IOGPUMetalRenderCommandEncoder setMeshAccelerationStructure:atBufferIndex:];
-[IOGPUMetalRenderCommandEncoder getVertexBufferContentsAtIndex:];
-[IOGPUMetalRenderCommandEncoder useResource:usage:stages:];
-[IOGPUMetalRenderCommandEncoder setFragmentVisibleFunctionTables:withBufferRange:];
-[IOGPUMetalRenderCommandEncoder setStencilStoreAction:];
-[IOGPUMetalRenderCommandEncoder setVertexIntersectionFunctionTables:withBufferRange:];
-[IOGPUMetalRenderCommandEncoder useHeaps:count:stages:];
-[IOGPUMetalRenderCommandEncoder getRenderPipelineState];
-[IOGPUMetalRenderCommandEncoder setVertexAmplificationCount:viewMappings:];
-[IOGPUMetalRenderCommandEncoder setVertexVisibleFunctionTable:atBufferIndex:];
-[IOGPUMetalRenderCommandEncoder setDepthStoreAction:];
-[IOGPUMetalRenderCommandEncoder setDepthCleared];
-[IOGPUMetalRenderCommandEncoder useHeap:stages:];
-[IOGPUMetalRenderCommandEncoder setTileIntersectionFunctionTables:withBufferRange:];
-[IOGPUMetalRenderCommandEncoder useResources:count:usage:stages:];
-[IOGPUMetalRenderCommandEncoder updateFence:afterStages:];
-[IOGPUMetalRenderCommandEncoder setDepthStoreActionOptions:];
-[IOGPUMetalRenderCommandEncoder setFragmentIntersectionFunctionTables:withBufferRange:];
-[IOGPUMetalRenderCommandEncoder setDepthClipModeSPI:];
-[IOGPUMetalRenderCommandEncoder setColorStoreActionOptions:atIndex:];
-[IOGPUMetalRenderCommandEncoder memoryBarrierWithResources:count:afterStages:beforeStages:];
-[IOGPUMetalRenderCommandEncoder waitForFence:beforeStages:];
-[IOGPUMetalRenderCommandEncoder memoryBarrierWithScope:afterStages:beforeStages:];
-[IOGPUMetalRenderCommandEncoder textureBarrier];
-[IOGPUMetalRenderCommandEncoder setTileIntersectionFunctionTable:atBufferIndex:];
-[IOGPUMetalRenderCommandEncoder setMeshIntersectionFunctionTable:atBufferIndex:];
-[IOGPUMetalRenderCommandEncoder isMemorylessRender];
-[IOGPUMetalRenderCommandEncoder setFragmentAccelerationStructure:atBufferIndex:];
```
