# `MTL4RenderCommandEncoder` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTL4CommandEncoder`
- 0 instance variables, 2 properties, 41 instance methods, 0 class methods

## Properties

```
@property (TQ,R) tileWidth;
@property (TQ,R) tileHeight;
```

## Instance methods

```
-[MTL4RenderCommandEncoder executeCommandsInBuffer:withRange:];
-[MTL4RenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:];
-[MTL4RenderCommandEncoder setFrontFacingWinding:];
-[MTL4RenderCommandEncoder setBlendColorRed:green:blue:alpha:];
-[MTL4RenderCommandEncoder setColorStoreAction:atIndex:];
-[MTL4RenderCommandEncoder setCullMode:];
-[MTL4RenderCommandEncoder setVisibilityResultMode:offset:];
-[MTL4RenderCommandEncoder setRenderPipelineState:];
-[MTL4RenderCommandEncoder setTriangleFillMode:];
-[MTL4RenderCommandEncoder setStencilReferenceValue:];
-[MTL4RenderCommandEncoder tileHeight];
-[MTL4RenderCommandEncoder setViewports:count:];
-[MTL4RenderCommandEncoder drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTL4RenderCommandEncoder setStencilStoreAction:];
-[MTL4RenderCommandEncoder tileWidth];
-[MTL4RenderCommandEncoder setThreadgroupMemoryLength:offset:atIndex:];
-[MTL4RenderCommandEncoder setViewport:];
-[MTL4RenderCommandEncoder setScissorRects:count:];
-[MTL4RenderCommandEncoder setVertexAmplificationCount:viewMappings:];
-[MTL4RenderCommandEncoder setDepthStencilState:];
-[MTL4RenderCommandEncoder setDepthStoreAction:];
-[MTL4RenderCommandEncoder drawPrimitives:vertexStart:vertexCount:];
-[MTL4RenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:];
-[MTL4RenderCommandEncoder setObjectThreadgroupMemoryLength:atIndex:];
-[MTL4RenderCommandEncoder setDepthClipMode:];
-[MTL4RenderCommandEncoder setDepthBias:slopeScale:clamp:];
-[MTL4RenderCommandEncoder setScissorRect:];
-[MTL4RenderCommandEncoder setDepthTestMinBound:maxBound:];
-[MTL4RenderCommandEncoder dispatchThreadsPerTile:];
-[MTL4RenderCommandEncoder setStencilFrontReferenceValue:backReferenceValue:];
-[MTL4RenderCommandEncoder drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTL4RenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:];
-[MTL4RenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:];
-[MTL4RenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:baseVertex:baseInstance:];
-[MTL4RenderCommandEncoder drawIndexedPrimitives:indexType:indexBuffer:indexBufferLength:indirectBuffer:];
-[MTL4RenderCommandEncoder drawMeshThreadgroupsWithIndirectBuffer:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTL4RenderCommandEncoder drawPrimitives:indirectBuffer:];
-[MTL4RenderCommandEncoder executeCommandsInBuffer:indirectBuffer:];
-[MTL4RenderCommandEncoder setArgumentTable:atStages:];
-[MTL4RenderCommandEncoder setColorAttachmentMap:];
-[MTL4RenderCommandEncoder writeTimestampWithGranularity:afterStage:intoHeap:atIndex:];
```
