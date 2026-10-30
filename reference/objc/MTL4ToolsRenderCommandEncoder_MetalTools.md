# `MTL4ToolsRenderCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4ToolsCommandEncoder`
- Protocols: `MTL4RenderCommandEncoderGGDSPI`
- 5 instance variables, 15 properties, 57 instance methods, 0 class methods

## Instance variables

```
@"<MTL4ArgumentTable>" _currentVertexArgumentTable;
@"<MTL4ArgumentTable>" _currentFragmentArgumentTable;
@"<MTL4ArgumentTable>" _currentTileArgumentTable;
@"<MTL4ArgumentTable>" _currentObjectArgumentTable;
@"<MTL4ArgumentTable>" _currentMeshArgumentTable;
```

## Properties

```
@property (TQ,R) tileWidth;
@property (TQ,R) tileHeight;
@property (T@"<MTL4ArgumentTable>",R,N,V_currentVertexArgumentTable) currentVertexArgumentTable;
@property (T@"<MTL4ArgumentTable>",R,N,V_currentFragmentArgumentTable) currentFragmentArgumentTable;
@property (T@"<MTL4ArgumentTable>",R,N,V_currentTileArgumentTable) currentTileArgumentTable;
@property (T@"<MTL4ArgumentTable>",R,N,V_currentObjectArgumentTable) currentObjectArgumentTable;
@property (T@"<MTL4ArgumentTable>",R,N,V_currentMeshArgumentTable) currentMeshArgumentTable;
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
-[MTL4ToolsRenderCommandEncoder executeCommandsInBuffer:withRange:];
-[MTL4ToolsRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:];
-[MTL4ToolsRenderCommandEncoder setLineWidth:];
-[MTL4ToolsRenderCommandEncoder setFrontFacingWinding:];
-[MTL4ToolsRenderCommandEncoder setBlendColorRed:green:blue:alpha:];
-[MTL4ToolsRenderCommandEncoder setColorStoreAction:atIndex:];
-[MTL4ToolsRenderCommandEncoder setCullMode:];
-[MTL4ToolsRenderCommandEncoder setVisibilityResultMode:offset:];
-[MTL4ToolsRenderCommandEncoder endEncoding];
-[MTL4ToolsRenderCommandEncoder setRenderPipelineState:];
-[MTL4ToolsRenderCommandEncoder dealloc];
-[MTL4ToolsRenderCommandEncoder setTriangleFillMode:];
-[MTL4ToolsRenderCommandEncoder setStencilReferenceValue:];
-[MTL4ToolsRenderCommandEncoder tileHeight];
-[MTL4ToolsRenderCommandEncoder setViewports:count:];
-[MTL4ToolsRenderCommandEncoder drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTL4ToolsRenderCommandEncoder setStencilStoreAction:];
-[MTL4ToolsRenderCommandEncoder tileWidth];
-[MTL4ToolsRenderCommandEncoder setThreadgroupMemoryLength:offset:atIndex:];
-[MTL4ToolsRenderCommandEncoder setViewport:];
-[MTL4ToolsRenderCommandEncoder setScissorRects:count:];
-[MTL4ToolsRenderCommandEncoder setVertexAmplificationCount:viewMappings:];
-[MTL4ToolsRenderCommandEncoder setDepthStencilState:];
-[MTL4ToolsRenderCommandEncoder setDepthStoreAction:];
-[MTL4ToolsRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:];
-[MTL4ToolsRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:];
-[MTL4ToolsRenderCommandEncoder setObjectThreadgroupMemoryLength:atIndex:];
-[MTL4ToolsRenderCommandEncoder setDepthClipMode:];
-[MTL4ToolsRenderCommandEncoder setDepthBias:slopeScale:clamp:];
-[MTL4ToolsRenderCommandEncoder setDepthClipModeSPI:];
-[MTL4ToolsRenderCommandEncoder setScissorRect:];
-[MTL4ToolsRenderCommandEncoder setDepthTestMinBound:maxBound:];
-[MTL4ToolsRenderCommandEncoder dispatchThreadsPerTile:];
-[MTL4ToolsRenderCommandEncoder setStencilFrontReferenceValue:backReferenceValue:];
-[MTL4ToolsRenderCommandEncoder drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTL4ToolsRenderCommandEncoder isMemorylessRender];
-[MTL4ToolsRenderCommandEncoder dispatchThreadsPerTile:inRegion:];
-[MTL4ToolsRenderCommandEncoder dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:];
-[MTL4ToolsRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:];
-[MTL4ToolsRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:];
-[MTL4ToolsRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:baseVertex:baseInstance:];
-[MTL4ToolsRenderCommandEncoder drawIndexedPrimitives:indexType:indexBuffer:indexBufferLength:indirectBuffer:];
-[MTL4ToolsRenderCommandEncoder drawMeshThreadgroupsWithIndirectBuffer:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTL4ToolsRenderCommandEncoder drawPrimitives:indirectBuffer:];
-[MTL4ToolsRenderCommandEncoder executeCommandsInBuffer:indirectBuffer:];
-[MTL4ToolsRenderCommandEncoder setArgumentTable:atStages:];
-[MTL4ToolsRenderCommandEncoder setColorAttachmentMap:];
-[MTL4ToolsRenderCommandEncoder setCommandDataCorruptModeSPI:];
-[MTL4ToolsRenderCommandEncoder setToolsDispatchBufferSPI:atIndex:stages:];
-[MTL4ToolsRenderCommandEncoder setVertexAmplificationMode:value:];
-[MTL4ToolsRenderCommandEncoder writeTimestampWithGranularity:afterStage:intoHeap:atIndex:];
-[MTL4ToolsRenderCommandEncoder currentFragmentArgumentTable];
-[MTL4ToolsRenderCommandEncoder currentMeshArgumentTable];
-[MTL4ToolsRenderCommandEncoder currentObjectArgumentTable];
-[MTL4ToolsRenderCommandEncoder currentTileArgumentTable];
-[MTL4ToolsRenderCommandEncoder currentVertexArgumentTable];
-[MTL4ToolsRenderCommandEncoder releaseArgumentTables];
```
