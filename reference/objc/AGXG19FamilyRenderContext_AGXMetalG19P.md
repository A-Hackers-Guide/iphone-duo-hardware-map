# `AGXG19FamilyRenderContext`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalRenderCommandEncoder`
- Protocols: `MTLRenderCommandEncoderSPI`
- 4 instance variables, 8 properties, 184 instance methods, 0 class methods

## Instance variables

```
^v _impl;
^v _framebuffer;
I _user_draw_token_offset;
B parallelSubContext;
```

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) tileWidth;
@property (TQ,R) tileHeight;
```

## Instance methods

```
-[AGXG19FamilyRenderContext useResources:count:usage:];
-[AGXG19FamilyRenderContext executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:];
-[AGXG19FamilyRenderContext useResource:usage:];
-[AGXG19FamilyRenderContext executeCommandsInBuffer:withRange:];
-[AGXG19FamilyRenderContext useHeap:];
-[AGXG19FamilyRenderContext useHeaps:count:];
-[AGXG19FamilyRenderContext sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[AGXG19FamilyRenderContext setFragmentBuffers:offsets:withRange:];
-[AGXG19FamilyRenderContext setMeshIntersectionFunctionTables:withBufferRange:];
-[AGXG19FamilyRenderContext setVertexBufferOffset:attributeStride:atIndex:];
-[AGXG19FamilyRenderContext drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:];
-[AGXG19FamilyRenderContext setObjectAccelerationStructure:atBufferIndex:];
-[AGXG19FamilyRenderContext setLineWidth:];
-[AGXG19FamilyRenderContext drawPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:instanceCount:baseInstance:];
-[AGXG19FamilyRenderContext setVertexBuffers:offsets:withRange:];
-[AGXG19FamilyRenderContext setFrontFacingWinding:];
-[AGXG19FamilyRenderContext setMeshSamplerStates:lodMinClamps:lodMaxClamps:withRange:];
-[AGXG19FamilyRenderContext useResidencySet:];
-[AGXG19FamilyRenderContext setObjectBufferOffset:atIndex:];
-[AGXG19FamilyRenderContext setBlendColorRed:green:blue:alpha:];
-[AGXG19FamilyRenderContext useResidencySets:count:];
-[AGXG19FamilyRenderContext setStencilCleared];
-[AGXG19FamilyRenderContext setColorStoreAction:atIndex:];
-[AGXG19FamilyRenderContext setFragmentSamplerState:atIndex:];
-[AGXG19FamilyRenderContext drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:];
-[AGXG19FamilyRenderContext setCullMode:];
-[AGXG19FamilyRenderContext setVisibilityResultMode:offset:];
-[AGXG19FamilyRenderContext initWithCommandBuffer:descriptor:];
-[AGXG19FamilyRenderContext setPointSize:];
-[AGXG19FamilyRenderContext setFragmentIntersectionFunctionTable:atBufferIndex:];
-[AGXG19FamilyRenderContext setTileVisibleFunctionTable:atBufferIndex:];
-[AGXG19FamilyRenderContext setTileSamplerState:atIndex:];
-[AGXG19FamilyRenderContext setObjectIntersectionFunctionTables:withBufferRange:];
-[AGXG19FamilyRenderContext drawPrimitives:indirectBuffer:indirectBufferOffset:];
-[AGXG19FamilyRenderContext setVertexBuffer:offset:attributeStride:atIndex:];
-[AGXG19FamilyRenderContext setVertexSamplerState:lodMinClamp:lodMaxClamp:atIndex:];
-[AGXG19FamilyRenderContext setTileAccelerationStructure:atBufferIndex:];
-[AGXG19FamilyRenderContext setFragmentBuffer:offset:atIndex:];
-[AGXG19FamilyRenderContext endEncoding];
-[AGXG19FamilyRenderContext setRenderPipelineState:];
-[AGXG19FamilyRenderContext setVertexSamplerStates:lodMinClamps:lodMaxClamps:withRange:];
-[AGXG19FamilyRenderContext drawMeshThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[AGXG19FamilyRenderContext setVertexBytes:length:attributeStride:atIndex:];
-[AGXG19FamilyRenderContext setTileTextures:withRange:];
-[AGXG19FamilyRenderContext dealloc];
-[AGXG19FamilyRenderContext setVertexVisibleFunctionTables:withBufferRange:];
-[AGXG19FamilyRenderContext setFragmentBufferOffset:atIndex:];
-[AGXG19FamilyRenderContext setObjectSamplerState:atIndex:];
-[AGXG19FamilyRenderContext setTileSamplerStates:withRange:];
-[AGXG19FamilyRenderContext drawPatches:patchIndexBuffer:patchIndexBufferOffset:indirectBuffer:indirectBufferOffset:];
-[AGXG19FamilyRenderContext setFragmentTexture:atIndex:];
-[AGXG19FamilyRenderContext setTriangleFillMode:];
-[AGXG19FamilyRenderContext drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:];
-[AGXG19FamilyRenderContext setVertexBuffers:offsets:attributeStrides:withRange:];
-[AGXG19FamilyRenderContext setVertexBytes:length:atIndex:];
-[AGXG19FamilyRenderContext setTileBuffer:offset:atIndex:];
-[AGXG19FamilyRenderContext setObjectBuffer:offset:atIndex:];
-[AGXG19FamilyRenderContext setTileBuffers:offsets:withRange:];
-[AGXG19FamilyRenderContext setStencilReferenceValue:];
-[AGXG19FamilyRenderContext setMeshBuffer:offset:atIndex:];
-[AGXG19FamilyRenderContext setObjectBuffers:offsets:withRange:];
-[AGXG19FamilyRenderContext setTileVisibleFunctionTables:withBufferRange:];
-[AGXG19FamilyRenderContext setVertexIntersectionFunctionTable:atBufferIndex:];
-[AGXG19FamilyRenderContext setMeshSamplerState:atIndex:];
-[AGXG19FamilyRenderContext setObjectIntersectionFunctionTable:atBufferIndex:];
-[AGXG19FamilyRenderContext drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:];
-[AGXG19FamilyRenderContext tileHeight];
-[AGXG19FamilyRenderContext setVertexAccelerationStructure:atBufferIndex:];
-[AGXG19FamilyRenderContext setViewports:count:];
-[AGXG19FamilyRenderContext setFragmentVisibleFunctionTable:atBufferIndex:];
-[AGXG19FamilyRenderContext setVertexSamplerState:atIndex:];
-[AGXG19FamilyRenderContext setMeshAccelerationStructure:atBufferIndex:];
-[AGXG19FamilyRenderContext useResource:usage:stages:];
-[AGXG19FamilyRenderContext drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[AGXG19FamilyRenderContext setFragmentSamplerState:lodMinClamp:lodMaxClamp:atIndex:];
-[AGXG19FamilyRenderContext setFragmentVisibleFunctionTables:withBufferRange:];
-[AGXG19FamilyRenderContext setVertexSamplerStates:withRange:];
-[AGXG19FamilyRenderContext drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:];
-[AGXG19FamilyRenderContext setStencilStoreAction:];
-[AGXG19FamilyRenderContext setFragmentSamplerStates:withRange:];
-[AGXG19FamilyRenderContext tileWidth];
-[AGXG19FamilyRenderContext setTileSamplerStates:lodMinClamps:lodMaxClamps:withRange:];
-[AGXG19FamilyRenderContext setVertexIntersectionFunctionTables:withBufferRange:];
-[AGXG19FamilyRenderContext useHeaps:count:stages:];
-[AGXG19FamilyRenderContext setThreadgroupMemoryLength:offset:atIndex:];
-[AGXG19FamilyRenderContext setTessellationFactorBuffer:offset:instanceStride:];
-[AGXG19FamilyRenderContext setViewport:];
-[AGXG19FamilyRenderContext setTileBytes:length:atIndex:];
-[AGXG19FamilyRenderContext setScissorRects:count:];
-[AGXG19FamilyRenderContext setObjectSamplerStates:withRange:];
-[AGXG19FamilyRenderContext setVertexAmplificationCount:viewMappings:];
-[AGXG19FamilyRenderContext setVertexVisibleFunctionTable:atBufferIndex:];
-[AGXG19FamilyRenderContext setDepthStencilState:];
-[AGXG19FamilyRenderContext setVertexTexture:atIndex:];
-[AGXG19FamilyRenderContext setMeshBufferOffset:atIndex:];
-[AGXG19FamilyRenderContext setObjectSamplerState:lodMinClamp:lodMaxClamp:atIndex:];
-[AGXG19FamilyRenderContext setDepthStoreAction:];
-[AGXG19FamilyRenderContext setMeshTextures:withRange:];
-[AGXG19FamilyRenderContext drawPrimitives:vertexStart:vertexCount:];
-[AGXG19FamilyRenderContext setMeshBuffers:offsets:withRange:];
-[AGXG19FamilyRenderContext setDepthCleared];
-[AGXG19FamilyRenderContext setFragmentTexture:atTextureIndex:samplerState:atSamplerIndex:];
-[AGXG19FamilyRenderContext useHeap:stages:];
-[AGXG19FamilyRenderContext setTessellationFactorScale:];
-[AGXG19FamilyRenderContext setObjectTexture:atIndex:];
-[AGXG19FamilyRenderContext drawPrimitives:vertexStart:vertexCount:instanceCount:];
-[AGXG19FamilyRenderContext setTileIntersectionFunctionTables:withBufferRange:];
-[AGXG19FamilyRenderContext setFragmentTextures:withRange:];
-[AGXG19FamilyRenderContext useResources:count:usage:stages:];
-[AGXG19FamilyRenderContext updateFence:afterStages:];
-[AGXG19FamilyRenderContext drawIndexedPatches:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:indirectBuffer:indirectBufferOffset:];
-[AGXG19FamilyRenderContext setObjectThreadgroupMemoryLength:atIndex:];
-[AGXG19FamilyRenderContext setObjectTextures:withRange:];
-[AGXG19FamilyRenderContext setFragmentSamplerStates:lodMinClamps:lodMaxClamps:withRange:];
-[AGXG19FamilyRenderContext setFragmentIntersectionFunctionTables:withBufferRange:];
-[AGXG19FamilyRenderContext drawIndexedPrimitives:indexType:indexBuffer:indexBufferOffset:indirectBuffer:indirectBufferOffset:];
-[AGXG19FamilyRenderContext setTileSamplerState:lodMinClamp:lodMaxClamp:atIndex:];
-[AGXG19FamilyRenderContext setDepthClipMode:];
-[AGXG19FamilyRenderContext setDepthBias:slopeScale:clamp:];
-[AGXG19FamilyRenderContext setMeshSamplerStates:withRange:];
-[AGXG19FamilyRenderContext memoryBarrierWithResources:count:afterStages:beforeStages:];
-[AGXG19FamilyRenderContext setObjectBytes:length:atIndex:];
-[AGXG19FamilyRenderContext setScissorRect:];
-[AGXG19FamilyRenderContext setDepthTestMinBound:maxBound:];
-[AGXG19FamilyRenderContext setVertexBufferOffset:atIndex:];
-[AGXG19FamilyRenderContext setMeshTexture:atIndex:];
-[AGXG19FamilyRenderContext setVertexBuffer:offset:atIndex:];
-[AGXG19FamilyRenderContext setVertexTextures:withRange:];
-[AGXG19FamilyRenderContext dispatchThreadsPerTile:];
-[AGXG19FamilyRenderContext waitForFence:beforeStages:];
-[AGXG19FamilyRenderContext memoryBarrierWithScope:afterStages:beforeStages:];
-[AGXG19FamilyRenderContext setTileTexture:atIndex:];
-[AGXG19FamilyRenderContext setStencilFrontReferenceValue:backReferenceValue:];
-[AGXG19FamilyRenderContext setTileIntersectionFunctionTable:atBufferIndex:];
-[AGXG19FamilyRenderContext setMeshIntersectionFunctionTable:atBufferIndex:];
-[AGXG19FamilyRenderContext setObjectSamplerStates:lodMinClamps:lodMaxClamps:withRange:];
-[AGXG19FamilyRenderContext drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[AGXG19FamilyRenderContext setTileBufferOffset:atIndex:];
-[AGXG19FamilyRenderContext setFragmentBytes:length:atIndex:];
-[AGXG19FamilyRenderContext isMemorylessRender];
-[AGXG19FamilyRenderContext setMeshSamplerState:lodMinClamp:lodMaxClamp:atIndex:];
-[AGXG19FamilyRenderContext setFragmentAccelerationStructure:atBufferIndex:];
-[AGXG19FamilyRenderContext setMeshBytes:length:atIndex:];
-[AGXG19FamilyRenderContext dispatchThreadsPerTile:inRegion:];
-[AGXG19FamilyRenderContext barrierAfterQueueStages:beforeStages:];
-[AGXG19FamilyRenderContext commandBatchIdOffset];
-[AGXG19FamilyRenderContext commandBatchIdRangeMin:max:];
-[AGXG19FamilyRenderContext dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:];
-[AGXG19FamilyRenderContext filterCounterRangeWithFirstBatch:lastBatch:filterIndex:];
-[AGXG19FamilyRenderContext insertSplit];
-[AGXG19FamilyRenderContext setColorAttachmentMap:];
-[AGXG19FamilyRenderContext setCommandDataCorruptModeSPI:];
-[AGXG19FamilyRenderContext setMeshVisibleFunctionTable:atBufferIndex:];
-[AGXG19FamilyRenderContext setMeshVisibleFunctionTables:withBufferRange:];
-[AGXG19FamilyRenderContext setObjectVisibleFunctionTable:atBufferIndex:];
-[AGXG19FamilyRenderContext setObjectVisibleFunctionTables:withBufferRange:];
-[AGXG19FamilyRenderContext setToolsDispatchBufferSPI:atIndex:stages:];
-[AGXG19FamilyRenderContext setVertexAmplificationMode:value:];
-[AGXG19FamilyRenderContext addSplitHandler:];
-[AGXG19FamilyRenderContext dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:withCondition:];
-[AGXG19FamilyRenderContext dispatchThreadsPerTile:withCondition:];
-[AGXG19FamilyRenderContext resetTileCondition];
-[AGXG19FamilyRenderContext setAlphaTestReferenceValue:];
-[AGXG19FamilyRenderContext setColorResolveTexture:slice:depthPlane:level:atIndex:];
-[AGXG19FamilyRenderContext setColorResolveTexture:slice:depthPlane:level:yInvert:atIndex:];
-[AGXG19FamilyRenderContext setDepthResolveTexture:slice:depthPlane:level:];
-[AGXG19FamilyRenderContext setDepthResolveTexture:slice:depthPlane:level:yInvert:];
-[AGXG19FamilyRenderContext setPrimitiveRestartEnabled:];
-[AGXG19FamilyRenderContext setPrimitiveRestartEnabled:index:];
-[AGXG19FamilyRenderContext setProvokingVertexMode:];
-[AGXG19FamilyRenderContext setStencilResolveTexture:slice:depthPlane:level:];
-[AGXG19FamilyRenderContext setStencilResolveTexture:slice:depthPlane:level:yInvert:];
-[AGXG19FamilyRenderContext setViewportTransformEnabled:];
-[AGXG19FamilyRenderContext getImpl];
-[AGXG19FamilyRenderContext useComputePipelineStates:count:];
-[AGXG19FamilyRenderContext addProtectedContentBarrier];
-[AGXG19FamilyRenderContext deferredEndEncoding:];
-[AGXG19FamilyRenderContext destroyImpl];
-[AGXG19FamilyRenderContext drawMeshThreadgroups:];
-[AGXG19FamilyRenderContext initWithCommandBuffer:descriptor:subEncoderIndex:framebuffer:];
-[AGXG19FamilyRenderContext initWithCommandBuffer:dummyDescriptor:];
-[AGXG19FamilyRenderContext setMTLCounterSampleLocationWithBuffer:startIndex:endIndex:dm:];
-[AGXG19FamilyRenderContext setMTLCounterSampleLocationWithBuffer:vertexStartIndex:vertexEndIndex:fragmentStartIndex:fragmentEndIndex:];
-[AGXG19FamilyRenderContext useComputePipelineState:];
```
