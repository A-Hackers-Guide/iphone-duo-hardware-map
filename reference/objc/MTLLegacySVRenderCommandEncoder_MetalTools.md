# `MTLLegacySVRenderCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsRenderCommandEncoder`
- Protocols: `MTLLegacySVCommandEncoder`
- 35 instance variables, 6 properties, 116 instance methods, 0 class methods

## Instance variables

```
I useResourceIteration;
B _tileStageActive;
B _tileStageUsed;
B _fragmentStageActive;
B _vertexStageActive;
B _objectStageActive;
B _meshStageActive;
B _enableUseResourceValidation;
@"MTLLegacySVCommandBuffer" _commandBuffer;
{MTLLegacySVStageBufferHandles="handles"[31Q]"resources"[31@"<MTLLegacySVResource>"]"offsets"[31Q]"strides"[31Q]"lengths"[31I]"gpu_address"[31[2Q]]"needsFlush"B} _vertexHandles;
{MTLLegacySVStageBufferHandles="handles"[31Q]"resources"[31@"<MTLLegacySVResource>"]"offsets"[31Q]"strides"[31Q]"lengths"[31I]"gpu_address"[31[2Q]]"needsFlush"B} _fragmentHandles;
{MTLLegacySVStageBufferHandles="handles"[31Q]"resources"[31@"<MTLLegacySVResource>"]"offsets"[31Q]"strides"[31Q]"lengths"[31I]"gpu_address"[31[2Q]]"needsFlush"B} _tileHandles;
{MTLLegacySVTileThreadgroup="entries"[32{GPUDebugThreadgroupTableEntry="offset"I"length"I}]"needsFlush"B} _tileThreadgroup;
{MTLLegacySVStageBufferHandles="handles"[31Q]"resources"[31@"<MTLLegacySVResource>"]"offsets"[31Q]"strides"[31Q]"lengths"[31I]"gpu_address"[31[2Q]]"needsFlush"B} _objectHandles;
{MTLLegacySVStageBufferHandles="handles"[31Q]"resources"[31@"<MTLLegacySVResource>"]"offsets"[31Q]"strides"[31Q]"lengths"[31I]"gpu_address"[31[2Q]]"needsFlush"B} _meshHandles;
{MTLLegacySVThreadgroupLengths="threadgroupSizes"[31I]"entries"[32{GPUDebugThreadgroupTableEntry="offset"I"length"I}]"needsFlush"B} _meshThreadgroup;
^{Options=IiiiI{?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}} _options;
{LegacyEventUUIDPacket="pipelineStateID"Q"entryPointImageID"Q"encoderID"I"eventID"I} _drawID;
Q _encoderType;
@"MTLLegacySVRenderPipelineState" _currentPipeline;
@"MTLToolsDepthStencilState" _currentDepthStencil;
{MTLLegacySVBufferSubAlloc="buffer"@"<MTLBuffer>""offset"Q} _vertexReportBuffer;
{MTLLegacySVBufferSubAlloc="buffer"@"<MTLBuffer>""offset"Q} _fragmentReportBuffer;
{MTLLegacySVBufferSubAlloc="buffer"@"<MTLBuffer>""offset"Q} _tileReportBuffer;
{MTLLegacySVBufferSubAlloc="buffer"@"<MTLBuffer>""offset"Q} _objectReportBuffer;
{MTLLegacySVBufferSubAlloc="buffer"@"<MTLBuffer>""offset"Q} _meshReportBuffer;
{?="count"C"mappingsValid"B"mappings"[2{?="viewportArrayIndexOffset"I"renderTargetArrayIndexOffset"I}]} _vertexAmpState;
@"<MTLBuffer>" _vertexBufferUsageTable;
@"<MTLBuffer>" _vertexTextureUsageTable;
@"<MTLBuffer>" _fragmentBufferUsageTable;
@"<MTLBuffer>" _fragmentTextureUsageTable;
@"<MTLBuffer>" _objectBufferUsageTable;
@"<MTLBuffer>" _objectTextureUsageTable;
@"<MTLBuffer>" _meshBufferUsageTable;
@"<MTLBuffer>" _meshTextureUsageTable;
```

## Properties

```
@property (T@"MTLLegacySVCommandBuffer",R,D) commandBuffer;
@property (TI,R) encoderID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLLegacySVRenderCommandEncoder useResources:count:usage:];
-[MTLLegacySVRenderCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:];
-[MTLLegacySVRenderCommandEncoder useResource:usage:];
-[MTLLegacySVRenderCommandEncoder executeCommandsInBuffer:withRange:];
-[MTLLegacySVRenderCommandEncoder useHeap:];
-[MTLLegacySVRenderCommandEncoder useHeaps:count:];
-[MTLLegacySVRenderCommandEncoder setFragmentBuffers:offsets:withRange:];
-[MTLLegacySVRenderCommandEncoder setMeshIntersectionFunctionTables:withBufferRange:];
-[MTLLegacySVRenderCommandEncoder setVertexBufferOffset:attributeStride:atIndex:];
-[MTLLegacySVRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:];
-[MTLLegacySVRenderCommandEncoder setObjectAccelerationStructure:atBufferIndex:];
-[MTLLegacySVRenderCommandEncoder drawPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:instanceCount:baseInstance:];
-[MTLLegacySVRenderCommandEncoder setVertexBuffers:offsets:withRange:];
-[MTLLegacySVRenderCommandEncoder useResidencySet:];
-[MTLLegacySVRenderCommandEncoder setObjectBufferOffset:atIndex:];
-[MTLLegacySVRenderCommandEncoder useResidencySets:count:];
-[MTLLegacySVRenderCommandEncoder drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:];
-[MTLLegacySVRenderCommandEncoder setFragmentIntersectionFunctionTable:atBufferIndex:];
-[MTLLegacySVRenderCommandEncoder setTileVisibleFunctionTable:atBufferIndex:];
-[MTLLegacySVRenderCommandEncoder setObjectIntersectionFunctionTables:withBufferRange:];
-[MTLLegacySVRenderCommandEncoder drawPrimitives:indirectBuffer:indirectBufferOffset:];
-[MTLLegacySVRenderCommandEncoder setVertexBuffer:offset:attributeStride:atIndex:];
-[MTLLegacySVRenderCommandEncoder setTileAccelerationStructure:atBufferIndex:];
-[MTLLegacySVRenderCommandEncoder setFragmentBuffer:offset:atIndex:];
-[MTLLegacySVRenderCommandEncoder endEncoding];
-[MTLLegacySVRenderCommandEncoder setRenderPipelineState:];
-[MTLLegacySVRenderCommandEncoder drawMeshThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTLLegacySVRenderCommandEncoder setVertexBytes:length:attributeStride:atIndex:];
-[MTLLegacySVRenderCommandEncoder setTileTextures:withRange:];
-[MTLLegacySVRenderCommandEncoder setVertexVisibleFunctionTables:withBufferRange:];
-[MTLLegacySVRenderCommandEncoder setFragmentBufferOffset:atIndex:];
-[MTLLegacySVRenderCommandEncoder drawPatches:patchIndexBuffer:patchIndexBufferOffset:indirectBuffer:indirectBufferOffset:];
-[MTLLegacySVRenderCommandEncoder setFragmentTexture:atIndex:];
-[MTLLegacySVRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:];
-[MTLLegacySVRenderCommandEncoder setVertexBuffers:offsets:attributeStrides:withRange:];
-[MTLLegacySVRenderCommandEncoder setVertexBytes:length:atIndex:];
-[MTLLegacySVRenderCommandEncoder setTileBuffer:offset:atIndex:];
-[MTLLegacySVRenderCommandEncoder setObjectBuffer:offset:atIndex:];
-[MTLLegacySVRenderCommandEncoder setTileBuffers:offsets:withRange:];
-[MTLLegacySVRenderCommandEncoder setMeshBuffer:offset:atIndex:];
-[MTLLegacySVRenderCommandEncoder setObjectBuffers:offsets:withRange:];
-[MTLLegacySVRenderCommandEncoder setTileVisibleFunctionTables:withBufferRange:];
-[MTLLegacySVRenderCommandEncoder setVertexIntersectionFunctionTable:atBufferIndex:];
-[MTLLegacySVRenderCommandEncoder setObjectIntersectionFunctionTable:atBufferIndex:];
-[MTLLegacySVRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:];
-[MTLLegacySVRenderCommandEncoder setVertexAccelerationStructure:atBufferIndex:];
-[MTLLegacySVRenderCommandEncoder setFragmentVisibleFunctionTable:atBufferIndex:];
-[MTLLegacySVRenderCommandEncoder setMeshAccelerationStructure:atBufferIndex:];
-[MTLLegacySVRenderCommandEncoder useResource:usage:stages:];
-[MTLLegacySVRenderCommandEncoder drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTLLegacySVRenderCommandEncoder setFragmentVisibleFunctionTables:withBufferRange:];
-[MTLLegacySVRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:];
-[MTLLegacySVRenderCommandEncoder setVertexIntersectionFunctionTables:withBufferRange:];
-[MTLLegacySVRenderCommandEncoder useHeaps:count:stages:];
-[MTLLegacySVRenderCommandEncoder setThreadgroupMemoryLength:offset:atIndex:];
-[MTLLegacySVRenderCommandEncoder setTileBytes:length:atIndex:];
-[MTLLegacySVRenderCommandEncoder setVertexAmplificationCount:viewMappings:];
-[MTLLegacySVRenderCommandEncoder setVertexVisibleFunctionTable:atBufferIndex:];
-[MTLLegacySVRenderCommandEncoder setDepthStencilState:];
-[MTLLegacySVRenderCommandEncoder setVertexTexture:atIndex:];
-[MTLLegacySVRenderCommandEncoder setMeshBufferOffset:atIndex:];
-[MTLLegacySVRenderCommandEncoder setMeshTextures:withRange:];
-[MTLLegacySVRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:];
-[MTLLegacySVRenderCommandEncoder setMeshBuffers:offsets:withRange:];
-[MTLLegacySVRenderCommandEncoder useHeap:stages:];
-[MTLLegacySVRenderCommandEncoder setObjectTexture:atIndex:];
-[MTLLegacySVRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:];
-[MTLLegacySVRenderCommandEncoder setTileIntersectionFunctionTables:withBufferRange:];
-[MTLLegacySVRenderCommandEncoder setFragmentTextures:withRange:];
-[MTLLegacySVRenderCommandEncoder useResources:count:usage:stages:];
-[MTLLegacySVRenderCommandEncoder drawIndexedPatches:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:indirectBuffer:indirectBufferOffset:];
-[MTLLegacySVRenderCommandEncoder setObjectTextures:withRange:];
-[MTLLegacySVRenderCommandEncoder setFragmentIntersectionFunctionTables:withBufferRange:];
-[MTLLegacySVRenderCommandEncoder drawIndexedPrimitives:indexType:indexBuffer:indexBufferOffset:indirectBuffer:indirectBufferOffset:];
-[MTLLegacySVRenderCommandEncoder setObjectBytes:length:atIndex:];
-[MTLLegacySVRenderCommandEncoder setVertexBufferOffset:atIndex:];
-[MTLLegacySVRenderCommandEncoder setMeshTexture:atIndex:];
-[MTLLegacySVRenderCommandEncoder setVertexBuffer:offset:atIndex:];
-[MTLLegacySVRenderCommandEncoder setVertexTextures:withRange:];
-[MTLLegacySVRenderCommandEncoder dispatchThreadsPerTile:];
-[MTLLegacySVRenderCommandEncoder setTileTexture:atIndex:];
-[MTLLegacySVRenderCommandEncoder setTileIntersectionFunctionTable:atBufferIndex:];
-[MTLLegacySVRenderCommandEncoder setMeshIntersectionFunctionTable:atBufferIndex:];
-[MTLLegacySVRenderCommandEncoder drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTLLegacySVRenderCommandEncoder setTileBufferOffset:atIndex:];
-[MTLLegacySVRenderCommandEncoder setFragmentBytes:length:atIndex:];
-[MTLLegacySVRenderCommandEncoder setFragmentAccelerationStructure:atBufferIndex:];
-[MTLLegacySVRenderCommandEncoder setMeshBytes:length:atIndex:];
-[MTLLegacySVRenderCommandEncoder dispatchThreadsPerTile:inRegion:];
-[MTLLegacySVRenderCommandEncoder dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:];
-[MTLLegacySVRenderCommandEncoder setMeshVisibleFunctionTable:atBufferIndex:];
-[MTLLegacySVRenderCommandEncoder setMeshVisibleFunctionTables:withBufferRange:];
-[MTLLegacySVRenderCommandEncoder setObjectVisibleFunctionTable:atBufferIndex:];
-[MTLLegacySVRenderCommandEncoder setObjectVisibleFunctionTables:withBufferRange:];
-[MTLLegacySVRenderCommandEncoder dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:withCondition:];
-[MTLLegacySVRenderCommandEncoder dispatchThreadsPerTile:withCondition:];
-[MTLLegacySVRenderCommandEncoder resetTileCondition];
-[MTLLegacySVRenderCommandEncoder prepareExecuteIndirect:variant:];
-[MTLLegacySVRenderCommandEncoder setFragmentReportBuffer:offset:];
-[MTLLegacySVRenderCommandEncoder _initBufferArgumentData:];
-[MTLLegacySVRenderCommandEncoder _useResourceCommon:usage:stages:];
-[MTLLegacySVRenderCommandEncoder encoderID];
-[MTLLegacySVRenderCommandEncoder flushBindings];
-[MTLLegacySVRenderCommandEncoder initWithRenderCommandEncoder:commandBuffer:descriptor:encoderID:];
-[MTLLegacySVRenderCommandEncoder initWithRenderCommandEncoder:parallelEncoder:encoderID:];
-[MTLLegacySVRenderCommandEncoder restoreInternalState:];
-[MTLLegacySVRenderCommandEncoder setBufferUsageTable:textureUsageTable:forStage:];
-[MTLLegacySVRenderCommandEncoder setMeshReportBuffer:offset:];
-[MTLLegacySVRenderCommandEncoder setObjectReportBuffer:offset:];
-[MTLLegacySVRenderCommandEncoder setRenderPipelineStateBuffers:];
-[MTLLegacySVRenderCommandEncoder setTessellationControlPointIndexBuffer:offset:];
-[MTLLegacySVRenderCommandEncoder setTileReportBuffer:offset:];
-[MTLLegacySVRenderCommandEncoder setVertexReportBuffer:offset:];
-[MTLLegacySVRenderCommandEncoder temporaryBufferWithBytes:length:];
-[MTLLegacySVRenderCommandEncoder temporaryBufferWithLength:];
-[MTLLegacySVRenderCommandEncoder useResourceInternal:usage:stages:];
```
