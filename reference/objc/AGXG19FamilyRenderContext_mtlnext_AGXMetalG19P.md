# `AGXG19FamilyRenderContext_mtlnext`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetal4RenderCommandEncoder`
- Protocols: `MTL4RenderCommandEncoderGGDSPI`
- 10 instance variables, 10 properties, 61 instance methods, 1 class methods

## Instance variables

```
Q _options;
@"AGXG19FamilyCommandAllocator_mtlnext" _allocator;
@"AGXG19FamilyCommandBuffer_mtlnext" _command_buffer;
^v _impl;
^v _framebuffer;
{unique_ptr<AGX::HAL400::RenderContextB, std::function<void (AGX::HAL400::RenderContextB *)>>=""{?="__ptr_"^{RenderContextB}"__deleter_"{function<void (AGX::HAL400::RenderContextB *)>="__f_"{__value_func<void (AGX::HAL400::RenderContextB *)>="__buf_"(type="__data"[24C])"__f_"^v}}}} _impl_wrapper;
{unique_ptr<AGX::HAL400::Framebuffer, std::function<void (AGX::HAL400::Framebuffer *)>>=""{?="__ptr_"^{Framebuffer}"__deleter_"{function<void (AGX::HAL400::Framebuffer *)>="__f_"{__value_func<void (AGX::HAL400::Framebuffer *)>="__buf_"(type="__data"[24C])"__f_"^v}}}} _framebuffer_wrapper;
B _mergeable;
@"AGXG19FamilyDevice" _device;
I _user_draw_token_offset;
```

## Properties

```
@property (TQ,R) tileWidth;
@property (TQ,R) tileHeight;
@property (T@"NSString",C) label;
@property (T@"<MTL4CommandBuffer>",R,N) commandBuffer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) globalTraceObjectID;
@property (T@"<MTL4CommandAllocator>",R,N) commandAllocator;
```

## Class methods

```
+[AGXG19FamilyRenderContext_mtlnext mergeRenderEncoders:count:options:commitFeedback:queue:error:];
```

## Instance methods

```
-[AGXG19FamilyRenderContext_mtlnext executeCommandsInBuffer:withRange:];
-[AGXG19FamilyRenderContext_mtlnext isMergeable];
-[AGXG19FamilyRenderContext_mtlnext drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:];
-[AGXG19FamilyRenderContext_mtlnext setLineWidth:];
-[AGXG19FamilyRenderContext_mtlnext setFrontFacingWinding:];
-[AGXG19FamilyRenderContext_mtlnext setBlendColorRed:green:blue:alpha:];
-[AGXG19FamilyRenderContext_mtlnext setColorStoreAction:atIndex:];
-[AGXG19FamilyRenderContext_mtlnext setCullMode:];
-[AGXG19FamilyRenderContext_mtlnext setVisibilityResultMode:offset:];
-[AGXG19FamilyRenderContext_mtlnext endEncoding];
-[AGXG19FamilyRenderContext_mtlnext setRenderPipelineState:];
-[AGXG19FamilyRenderContext_mtlnext dealloc];
-[AGXG19FamilyRenderContext_mtlnext setTriangleFillMode:];
-[AGXG19FamilyRenderContext_mtlnext setStencilReferenceValue:];
-[AGXG19FamilyRenderContext_mtlnext tileHeight];
-[AGXG19FamilyRenderContext_mtlnext setViewports:count:];
-[AGXG19FamilyRenderContext_mtlnext drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[AGXG19FamilyRenderContext_mtlnext setStencilStoreAction:];
-[AGXG19FamilyRenderContext_mtlnext tileWidth];
-[AGXG19FamilyRenderContext_mtlnext setThreadgroupMemoryLength:offset:atIndex:];
-[AGXG19FamilyRenderContext_mtlnext setViewport:];
-[AGXG19FamilyRenderContext_mtlnext setScissorRects:count:];
-[AGXG19FamilyRenderContext_mtlnext setVertexAmplificationCount:viewMappings:];
-[AGXG19FamilyRenderContext_mtlnext setDepthStencilState:];
-[AGXG19FamilyRenderContext_mtlnext setDepthStoreAction:];
-[AGXG19FamilyRenderContext_mtlnext drawPrimitives:vertexStart:vertexCount:];
-[AGXG19FamilyRenderContext_mtlnext drawPrimitives:vertexStart:vertexCount:instanceCount:];
-[AGXG19FamilyRenderContext_mtlnext setObjectThreadgroupMemoryLength:atIndex:];
-[AGXG19FamilyRenderContext_mtlnext setDepthClipMode:];
-[AGXG19FamilyRenderContext_mtlnext setDepthBias:slopeScale:clamp:];
-[AGXG19FamilyRenderContext_mtlnext setScissorRect:];
-[AGXG19FamilyRenderContext_mtlnext setDepthTestMinBound:maxBound:];
-[AGXG19FamilyRenderContext_mtlnext dispatchThreadsPerTile:];
-[AGXG19FamilyRenderContext_mtlnext setStencilFrontReferenceValue:backReferenceValue:];
-[AGXG19FamilyRenderContext_mtlnext drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[AGXG19FamilyRenderContext_mtlnext isMemorylessRender];
-[AGXG19FamilyRenderContext_mtlnext dispatchThreadsPerTile:inRegion:];
-[AGXG19FamilyRenderContext_mtlnext updateFence:afterEncoderStages:];
-[AGXG19FamilyRenderContext_mtlnext barrierAfterEncoderStages:beforeEncoderStages:options:];
-[AGXG19FamilyRenderContext_mtlnext barrierAfterQueueStages:beforeStages:options:];
-[AGXG19FamilyRenderContext_mtlnext barrierAfterStages:beforeQueueStages:options:];
-[AGXG19FamilyRenderContext_mtlnext commandBatchIdOffset];
-[AGXG19FamilyRenderContext_mtlnext commandBatchIdRangeMin:max:];
-[AGXG19FamilyRenderContext_mtlnext dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:];
-[AGXG19FamilyRenderContext_mtlnext drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:];
-[AGXG19FamilyRenderContext_mtlnext drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:];
-[AGXG19FamilyRenderContext_mtlnext drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:baseVertex:baseInstance:];
-[AGXG19FamilyRenderContext_mtlnext drawIndexedPrimitives:indexType:indexBuffer:indexBufferLength:indirectBuffer:];
-[AGXG19FamilyRenderContext_mtlnext drawMeshThreadgroupsWithIndirectBuffer:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[AGXG19FamilyRenderContext_mtlnext drawPrimitives:indirectBuffer:];
-[AGXG19FamilyRenderContext_mtlnext executeCommandsInBuffer:indirectBuffer:];
-[AGXG19FamilyRenderContext_mtlnext filterCounterRangeWithFirstBatch:lastBatch:filterIndex:];
-[AGXG19FamilyRenderContext_mtlnext setArgumentTable:atStages:];
-[AGXG19FamilyRenderContext_mtlnext setColorAttachmentMap:];
-[AGXG19FamilyRenderContext_mtlnext setCommandDataCorruptModeSPI:];
-[AGXG19FamilyRenderContext_mtlnext setToolsDispatchBufferSPI:atIndex:stages:];
-[AGXG19FamilyRenderContext_mtlnext setVertexAmplificationMode:value:];
-[AGXG19FamilyRenderContext_mtlnext waitForFence:beforeEncoderStages:];
-[AGXG19FamilyRenderContext_mtlnext writeTimestampWithGranularity:afterStage:intoHeap:atIndex:];
-[AGXG19FamilyRenderContext_mtlnext destroyImpl];
-[AGXG19FamilyRenderContext_mtlnext initWithCommandBuffer:allocator:descriptor:options:captureProgramAddressTable:];
```
