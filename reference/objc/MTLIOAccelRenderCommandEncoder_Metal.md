# `MTLIOAccelRenderCommandEncoder`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLIOAccelCommandEncoder`
- 0 instance variables, 0 properties, 59 instance methods, 0 class methods

## Instance methods

```
-[MTLIOAccelRenderCommandEncoder useResources:count:usage:];
-[MTLIOAccelRenderCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:];
-[MTLIOAccelRenderCommandEncoder useResource:usage:];
-[MTLIOAccelRenderCommandEncoder executeCommandsInBuffer:withRange:];
-[MTLIOAccelRenderCommandEncoder useHeap:];
-[MTLIOAccelRenderCommandEncoder useHeaps:count:];
-[MTLIOAccelRenderCommandEncoder sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[MTLIOAccelRenderCommandEncoder setMeshIntersectionFunctionTables:withBufferRange:];
-[MTLIOAccelRenderCommandEncoder setObjectAccelerationStructure:atBufferIndex:];
-[MTLIOAccelRenderCommandEncoder setStencilCleared];
-[MTLIOAccelRenderCommandEncoder setColorStoreAction:atIndex:];
-[MTLIOAccelRenderCommandEncoder initWithCommandBuffer:descriptor:];
-[MTLIOAccelRenderCommandEncoder setFragmentIntersectionFunctionTable:atBufferIndex:];
-[MTLIOAccelRenderCommandEncoder setTileVisibleFunctionTable:atBufferIndex:];
-[MTLIOAccelRenderCommandEncoder setObjectIntersectionFunctionTables:withBufferRange:];
-[MTLIOAccelRenderCommandEncoder setVertexVisibleFunctionTables:withBufferRange:];
-[MTLIOAccelRenderCommandEncoder setStencilStoreActionOptions:];
-[MTLIOAccelRenderCommandEncoder getFragmentBufferContentsAtIndex:];
-[MTLIOAccelRenderCommandEncoder getType];
-[MTLIOAccelRenderCommandEncoder setTileVisibleFunctionTables:withBufferRange:];
-[MTLIOAccelRenderCommandEncoder setVertexIntersectionFunctionTable:atBufferIndex:];
-[MTLIOAccelRenderCommandEncoder setObjectIntersectionFunctionTable:atBufferIndex:];
-[MTLIOAccelRenderCommandEncoder setFragmentVisibleFunctionTable:atBufferIndex:];
-[MTLIOAccelRenderCommandEncoder setMeshAccelerationStructure:atBufferIndex:];
-[MTLIOAccelRenderCommandEncoder getVertexBufferContentsAtIndex:];
-[MTLIOAccelRenderCommandEncoder useResource:usage:stages:];
-[MTLIOAccelRenderCommandEncoder setFragmentVisibleFunctionTables:withBufferRange:];
-[MTLIOAccelRenderCommandEncoder setStencilStoreAction:];
-[MTLIOAccelRenderCommandEncoder setVertexIntersectionFunctionTables:withBufferRange:];
-[MTLIOAccelRenderCommandEncoder useHeaps:count:stages:];
-[MTLIOAccelRenderCommandEncoder getRenderPipelineState];
-[MTLIOAccelRenderCommandEncoder setVertexAmplificationCount:viewMappings:];
-[MTLIOAccelRenderCommandEncoder setVertexVisibleFunctionTable:atBufferIndex:];
-[MTLIOAccelRenderCommandEncoder setDepthStoreAction:];
-[MTLIOAccelRenderCommandEncoder setDepthCleared];
-[MTLIOAccelRenderCommandEncoder setFragmentTexture:atTextureIndex:samplerState:atSamplerIndex:];
-[MTLIOAccelRenderCommandEncoder useHeap:stages:];
-[MTLIOAccelRenderCommandEncoder setTileIntersectionFunctionTables:withBufferRange:];
-[MTLIOAccelRenderCommandEncoder useResources:count:usage:stages:];
-[MTLIOAccelRenderCommandEncoder updateFence:afterStages:];
-[MTLIOAccelRenderCommandEncoder setDepthStoreActionOptions:];
-[MTLIOAccelRenderCommandEncoder setFragmentIntersectionFunctionTables:withBufferRange:];
-[MTLIOAccelRenderCommandEncoder setDepthClipModeSPI:];
-[MTLIOAccelRenderCommandEncoder setColorStoreActionOptions:atIndex:];
-[MTLIOAccelRenderCommandEncoder memoryBarrierWithResources:count:afterStages:beforeStages:];
-[MTLIOAccelRenderCommandEncoder waitForFence:beforeStages:];
-[MTLIOAccelRenderCommandEncoder memoryBarrierWithScope:afterStages:beforeStages:];
-[MTLIOAccelRenderCommandEncoder textureBarrier];
-[MTLIOAccelRenderCommandEncoder setTileIntersectionFunctionTable:atBufferIndex:];
-[MTLIOAccelRenderCommandEncoder setMeshIntersectionFunctionTable:atBufferIndex:];
-[MTLIOAccelRenderCommandEncoder isMemorylessRender];
-[MTLIOAccelRenderCommandEncoder bindEmulationArguments];
-[MTLIOAccelRenderCommandEncoder setEmulationFragmentBuffers:offsets:withRange:];
-[MTLIOAccelRenderCommandEncoder setEmulationFragmentSamplerStates:withRange:];
-[MTLIOAccelRenderCommandEncoder setEmulationFragmentTextures:withRange:];
-[MTLIOAccelRenderCommandEncoder setEmulationVertexBuffers:offsets:withRange:];
-[MTLIOAccelRenderCommandEncoder setEmulationVertexSamplerStates:withRange:];
-[MTLIOAccelRenderCommandEncoder setEmulationVertexTextures:withRange:];
-[MTLIOAccelRenderCommandEncoder setToolsDispatchBufferSPI:atIndex:stages:];
```
