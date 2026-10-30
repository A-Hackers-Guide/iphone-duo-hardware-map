# `MTLCountersRenderCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsRenderCommandEncoder`
- 2 instance variables, 0 properties, 97 instance methods, 0 class methods

## Instance variables

```
B _APITimingEnabled;
@"MTLCountersTraceRenderCommandEncoder" _traceEncoder;
```

## Instance methods

```
-[MTLCountersRenderCommandEncoder useResources:count:usage:];
-[MTLCountersRenderCommandEncoder useResource:usage:];
-[MTLCountersRenderCommandEncoder insertDebugSignpost:];
-[MTLCountersRenderCommandEncoder useHeap:];
-[MTLCountersRenderCommandEncoder useHeaps:count:];
-[MTLCountersRenderCommandEncoder setFragmentBuffers:offsets:withRange:];
-[MTLCountersRenderCommandEncoder setVertexBufferOffset:attributeStride:atIndex:];
-[MTLCountersRenderCommandEncoder pushDebugGroup:];
-[MTLCountersRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:];
-[MTLCountersRenderCommandEncoder setLineWidth:];
-[MTLCountersRenderCommandEncoder drawPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:instanceCount:baseInstance:];
-[MTLCountersRenderCommandEncoder setVertexBuffers:offsets:withRange:];
-[MTLCountersRenderCommandEncoder setFrontFacingWinding:];
-[MTLCountersRenderCommandEncoder setBlendColorRed:green:blue:alpha:];
-[MTLCountersRenderCommandEncoder setColorStoreAction:atIndex:];
-[MTLCountersRenderCommandEncoder setFragmentSamplerState:atIndex:];
-[MTLCountersRenderCommandEncoder popDebugGroup];
-[MTLCountersRenderCommandEncoder drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:];
-[MTLCountersRenderCommandEncoder setCullMode:];
-[MTLCountersRenderCommandEncoder setVisibilityResultMode:offset:];
-[MTLCountersRenderCommandEncoder setTileSamplerState:atIndex:];
-[MTLCountersRenderCommandEncoder drawPrimitives:indirectBuffer:indirectBufferOffset:];
-[MTLCountersRenderCommandEncoder setVertexBuffer:offset:attributeStride:atIndex:];
-[MTLCountersRenderCommandEncoder setVertexSamplerState:lodMinClamp:lodMaxClamp:atIndex:];
-[MTLCountersRenderCommandEncoder setLabel:];
-[MTLCountersRenderCommandEncoder setFragmentBuffer:offset:atIndex:];
-[MTLCountersRenderCommandEncoder endEncoding];
-[MTLCountersRenderCommandEncoder setRenderPipelineState:];
-[MTLCountersRenderCommandEncoder setVertexSamplerStates:lodMinClamps:lodMaxClamps:withRange:];
-[MTLCountersRenderCommandEncoder setVertexBytes:length:attributeStride:atIndex:];
-[MTLCountersRenderCommandEncoder setTileTextures:withRange:];
-[MTLCountersRenderCommandEncoder dealloc];
-[MTLCountersRenderCommandEncoder setFragmentBufferOffset:atIndex:];
-[MTLCountersRenderCommandEncoder setTileSamplerStates:withRange:];
-[MTLCountersRenderCommandEncoder drawPatches:patchIndexBuffer:patchIndexBufferOffset:indirectBuffer:indirectBufferOffset:];
-[MTLCountersRenderCommandEncoder setFragmentTexture:atIndex:];
-[MTLCountersRenderCommandEncoder setTriangleFillMode:];
-[MTLCountersRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:];
-[MTLCountersRenderCommandEncoder setVertexBuffers:offsets:attributeStrides:withRange:];
-[MTLCountersRenderCommandEncoder setVertexBytes:length:atIndex:];
-[MTLCountersRenderCommandEncoder setTileBuffer:offset:atIndex:];
-[MTLCountersRenderCommandEncoder setTileBuffers:offsets:withRange:];
-[MTLCountersRenderCommandEncoder setStencilReferenceValue:];
-[MTLCountersRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:];
-[MTLCountersRenderCommandEncoder setViewports:count:];
-[MTLCountersRenderCommandEncoder setVertexSamplerState:atIndex:];
-[MTLCountersRenderCommandEncoder useResource:usage:stages:];
-[MTLCountersRenderCommandEncoder setFragmentSamplerState:lodMinClamp:lodMaxClamp:atIndex:];
-[MTLCountersRenderCommandEncoder setVertexSamplerStates:withRange:];
-[MTLCountersRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:];
-[MTLCountersRenderCommandEncoder setStencilStoreAction:];
-[MTLCountersRenderCommandEncoder setFragmentSamplerStates:withRange:];
-[MTLCountersRenderCommandEncoder setTileSamplerStates:lodMinClamps:lodMaxClamps:withRange:];
-[MTLCountersRenderCommandEncoder setThreadgroupMemoryLength:offset:atIndex:];
-[MTLCountersRenderCommandEncoder setTessellationFactorBuffer:offset:instanceStride:];
-[MTLCountersRenderCommandEncoder setViewport:];
-[MTLCountersRenderCommandEncoder setTileBytes:length:atIndex:];
-[MTLCountersRenderCommandEncoder setScissorRects:count:];
-[MTLCountersRenderCommandEncoder setVertexAmplificationCount:viewMappings:];
-[MTLCountersRenderCommandEncoder setDepthStencilState:];
-[MTLCountersRenderCommandEncoder setVertexTexture:atIndex:];
-[MTLCountersRenderCommandEncoder setDepthStoreAction:];
-[MTLCountersRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:];
-[MTLCountersRenderCommandEncoder setFragmentTexture:atTextureIndex:samplerState:atSamplerIndex:];
-[MTLCountersRenderCommandEncoder setTessellationFactorScale:];
-[MTLCountersRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:];
-[MTLCountersRenderCommandEncoder setFragmentTextures:withRange:];
-[MTLCountersRenderCommandEncoder useResources:count:usage:stages:];
-[MTLCountersRenderCommandEncoder updateFence:afterStages:];
-[MTLCountersRenderCommandEncoder drawIndexedPatches:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:indirectBuffer:indirectBufferOffset:];
-[MTLCountersRenderCommandEncoder setFragmentSamplerStates:lodMinClamps:lodMaxClamps:withRange:];
-[MTLCountersRenderCommandEncoder drawIndexedPrimitives:indexType:indexBuffer:indexBufferOffset:indirectBuffer:indirectBufferOffset:];
-[MTLCountersRenderCommandEncoder setTileSamplerState:lodMinClamp:lodMaxClamp:atIndex:];
-[MTLCountersRenderCommandEncoder setDepthClipMode:];
-[MTLCountersRenderCommandEncoder setDepthBias:slopeScale:clamp:];
-[MTLCountersRenderCommandEncoder memoryBarrierWithResources:count:afterStages:beforeStages:];
-[MTLCountersRenderCommandEncoder setScissorRect:];
-[MTLCountersRenderCommandEncoder setVertexBufferOffset:atIndex:];
-[MTLCountersRenderCommandEncoder setVertexBuffer:offset:atIndex:];
-[MTLCountersRenderCommandEncoder setVertexTextures:withRange:];
-[MTLCountersRenderCommandEncoder dispatchThreadsPerTile:];
-[MTLCountersRenderCommandEncoder waitForFence:beforeStages:];
-[MTLCountersRenderCommandEncoder memoryBarrierWithScope:afterStages:beforeStages:];
-[MTLCountersRenderCommandEncoder setTileTexture:atIndex:];
-[MTLCountersRenderCommandEncoder setStencilFrontReferenceValue:backReferenceValue:];
-[MTLCountersRenderCommandEncoder setTileBufferOffset:atIndex:];
-[MTLCountersRenderCommandEncoder setFragmentBytes:length:atIndex:];
-[MTLCountersRenderCommandEncoder setVertexAmplificationMode:value:];
-[MTLCountersRenderCommandEncoder setColorResolveTexture:slice:depthPlane:level:atIndex:];
-[MTLCountersRenderCommandEncoder setColorResolveTexture:slice:depthPlane:level:yInvert:atIndex:];
-[MTLCountersRenderCommandEncoder setDepthResolveTexture:slice:depthPlane:level:];
-[MTLCountersRenderCommandEncoder setDepthResolveTexture:slice:depthPlane:level:yInvert:];
-[MTLCountersRenderCommandEncoder setStencilResolveTexture:slice:depthPlane:level:];
-[MTLCountersRenderCommandEncoder setStencilResolveTexture:slice:depthPlane:level:yInvert:];
-[MTLCountersRenderCommandEncoder _initWithCommandBuffer:];
-[MTLCountersRenderCommandEncoder initWithRenderCommandEncoder:parent:];
-[MTLCountersRenderCommandEncoder initWithRenderCommandEncoder:parent:descriptor:];
```
