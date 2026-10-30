# `_MTL4RenderCommandEncoder`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTL4CommandEncoder`
- Protocols: `MTL4RenderCommandEncoderGGDSPI`
- 2 instance variables, 10 properties, 52 instance methods, 0 class methods

## Instance variables

```
Q _tileWidth;
Q _tileHeight;
```

## Properties

```
@property (TQ,V_tileWidth) tileWidth;
@property (TQ,V_tileHeight) tileHeight;
@property (T@"NSString",C) label;
@property (T@"<MTL4CommandBuffer>",R,N) commandBuffer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) globalTraceObjectID;
@property (T@"<MTL4CommandAllocator>",R,N) commandAllocator;
```

## Instance methods

```
-[_MTL4RenderCommandEncoder executeCommandsInBuffer:withRange:];
-[_MTL4RenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:];
-[_MTL4RenderCommandEncoder setLineWidth:];
-[_MTL4RenderCommandEncoder setFrontFacingWinding:];
-[_MTL4RenderCommandEncoder setBlendColorRed:green:blue:alpha:];
-[_MTL4RenderCommandEncoder setColorStoreAction:atIndex:];
-[_MTL4RenderCommandEncoder setCullMode:];
-[_MTL4RenderCommandEncoder setVisibilityResultMode:offset:];
-[_MTL4RenderCommandEncoder setRenderPipelineState:];
-[_MTL4RenderCommandEncoder setTriangleFillMode:];
-[_MTL4RenderCommandEncoder setStencilReferenceValue:];
-[_MTL4RenderCommandEncoder setTileWidth:];
-[_MTL4RenderCommandEncoder tileHeight];
-[_MTL4RenderCommandEncoder setViewports:count:];
-[_MTL4RenderCommandEncoder drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[_MTL4RenderCommandEncoder setStencilStoreAction:];
-[_MTL4RenderCommandEncoder tileWidth];
-[_MTL4RenderCommandEncoder setThreadgroupMemoryLength:offset:atIndex:];
-[_MTL4RenderCommandEncoder setViewport:];
-[_MTL4RenderCommandEncoder setScissorRects:count:];
-[_MTL4RenderCommandEncoder setVertexAmplificationCount:viewMappings:];
-[_MTL4RenderCommandEncoder setDepthStencilState:];
-[_MTL4RenderCommandEncoder setDepthStoreAction:];
-[_MTL4RenderCommandEncoder drawPrimitives:vertexStart:vertexCount:];
-[_MTL4RenderCommandEncoder setTileHeight:];
-[_MTL4RenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:];
-[_MTL4RenderCommandEncoder setObjectThreadgroupMemoryLength:atIndex:];
-[_MTL4RenderCommandEncoder setDepthClipMode:];
-[_MTL4RenderCommandEncoder setDepthBias:slopeScale:clamp:];
-[_MTL4RenderCommandEncoder setDepthClipModeSPI:];
-[_MTL4RenderCommandEncoder setScissorRect:];
-[_MTL4RenderCommandEncoder setDepthTestMinBound:maxBound:];
-[_MTL4RenderCommandEncoder dispatchThreadsPerTile:];
-[_MTL4RenderCommandEncoder setStencilFrontReferenceValue:backReferenceValue:];
-[_MTL4RenderCommandEncoder drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[_MTL4RenderCommandEncoder isMemorylessRender];
-[_MTL4RenderCommandEncoder dispatchThreadsPerTile:inRegion:];
-[_MTL4RenderCommandEncoder dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:];
-[_MTL4RenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:];
-[_MTL4RenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:];
-[_MTL4RenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:baseVertex:baseInstance:];
-[_MTL4RenderCommandEncoder drawIndexedPrimitives:indexType:indexBuffer:indexBufferLength:indirectBuffer:];
-[_MTL4RenderCommandEncoder drawMeshThreadgroupsWithIndirectBuffer:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[_MTL4RenderCommandEncoder drawPrimitives:indirectBuffer:];
-[_MTL4RenderCommandEncoder executeCommandsInBuffer:indirectBuffer:];
-[_MTL4RenderCommandEncoder initWithCommandAllocator:];
-[_MTL4RenderCommandEncoder setArgumentTable:atStages:];
-[_MTL4RenderCommandEncoder setColorAttachmentMap:];
-[_MTL4RenderCommandEncoder setCommandDataCorruptModeSPI:];
-[_MTL4RenderCommandEncoder setToolsDispatchBufferSPI:atIndex:stages:];
-[_MTL4RenderCommandEncoder setVertexAmplificationMode:value:];
-[_MTL4RenderCommandEncoder writeTimestampWithGranularity:afterStage:intoHeap:atIndex:];
```
