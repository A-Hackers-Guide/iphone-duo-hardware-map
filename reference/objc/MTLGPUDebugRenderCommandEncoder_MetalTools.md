# `MTLGPUDebugRenderCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsRenderCommandEncoder`
- Protocols: `MTLGPUDebugCommandEncoder`
- 28 instance variables, 6 properties, 113 instance methods, 0 class methods

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
@"MTLGPUDebugCommandBuffer" _commandBuffer;
{MTLGPUDebugTileThreadgroup="entries"[32{GPUDebugThreadgroupTableEntry="offset"I"length"I}]"needsFlush"B} _tileThreadgroup;
{MTLGPUDebugThreadgroupLengths="threadgroupSizes"[31I]"entries"[32{GPUDebugThreadgroupTableEntry="offset"I"length"I}]"needsFlush"B} _meshThreadgroup;
{MTLGPUDebugThreadgroupLengths="threadgroupSizes"[31I]"entries"[32{GPUDebugThreadgroupTableEntry="offset"I"length"I}]"needsFlush"B} _objectThreadgroup;
^{Options=IiiiI{?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}} _options;
{GPUDebugEventUUIDPacket="crc"Q"pipelineStateID"Q"entryPointImageID"Q"encoderID"I"commandInfo"I} _drawID;
Q _encoderType;
@"MTLGPUDebugRenderPipelineState" _currentPipeline;
@"MTLToolsDepthStencilState" _currentDepthStencil;
[31{GPUDebugEncoderBoundBuffers="resource"@"<MTLResource>""offset"Q"stride"Q"type"Q}] _vertexEncoderBoundBuffers;
[31{GPUDebugEncoderBoundBuffers="resource"@"<MTLResource>""offset"Q"stride"Q"type"Q}] _fragmentEncoderBoundBuffers;
[31{GPUDebugEncoderBoundBuffers="resource"@"<MTLResource>""offset"Q"stride"Q"type"Q}] _meshEncoderBoundBuffers;
[31{GPUDebugEncoderBoundBuffers="resource"@"<MTLResource>""offset"Q"stride"Q"type"Q}] _objectEncoderBoundBuffers;
{?="count"C"mappingsValid"B"mappings"[2{?="viewportArrayIndexOffset"I"renderTargetArrayIndexOffset"I}]} _vertexAmpState;
[4^{ResourceUsageTable}] _bufferUsageTable;
[4^{ResourceUsageTable}] _textureUsageTable;
[4^{ResourceUsageTable}] _bvhUsageTable;
[4^{ResourceUsageTable}] _tensorResidencyTable;
[4@"<MTLBuffer>"] _textureTypeTable;
[5@"<MTLBuffer>"] _internalBindingTables;
```

## Properties

```
@property (T@"MTLGPUDebugCommandBuffer",R,D) commandBuffer;
@property (TI,R) encoderID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLGPUDebugRenderCommandEncoder useResources:count:usage:];
-[MTLGPUDebugRenderCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:];
-[MTLGPUDebugRenderCommandEncoder useResource:usage:];
-[MTLGPUDebugRenderCommandEncoder executeCommandsInBuffer:withRange:];
-[MTLGPUDebugRenderCommandEncoder useHeap:];
-[MTLGPUDebugRenderCommandEncoder useHeaps:count:];
-[MTLGPUDebugRenderCommandEncoder setFragmentBuffers:offsets:withRange:];
-[MTLGPUDebugRenderCommandEncoder setMeshIntersectionFunctionTables:withBufferRange:];
-[MTLGPUDebugRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:];
-[MTLGPUDebugRenderCommandEncoder setObjectAccelerationStructure:atBufferIndex:];
-[MTLGPUDebugRenderCommandEncoder drawPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:instanceCount:baseInstance:];
-[MTLGPUDebugRenderCommandEncoder setVertexBuffers:offsets:withRange:];
-[MTLGPUDebugRenderCommandEncoder useResidencySet:];
-[MTLGPUDebugRenderCommandEncoder useResidencySets:count:];
-[MTLGPUDebugRenderCommandEncoder drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:];
-[MTLGPUDebugRenderCommandEncoder setFragmentIntersectionFunctionTable:atBufferIndex:];
-[MTLGPUDebugRenderCommandEncoder setTileVisibleFunctionTable:atBufferIndex:];
-[MTLGPUDebugRenderCommandEncoder setObjectIntersectionFunctionTables:withBufferRange:];
-[MTLGPUDebugRenderCommandEncoder drawPrimitives:indirectBuffer:indirectBufferOffset:];
-[MTLGPUDebugRenderCommandEncoder setVertexBuffer:offset:attributeStride:atIndex:];
-[MTLGPUDebugRenderCommandEncoder setTileAccelerationStructure:atBufferIndex:];
-[MTLGPUDebugRenderCommandEncoder setFragmentBuffer:offset:atIndex:];
-[MTLGPUDebugRenderCommandEncoder endEncoding];
-[MTLGPUDebugRenderCommandEncoder setRenderPipelineState:];
-[MTLGPUDebugRenderCommandEncoder drawMeshThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTLGPUDebugRenderCommandEncoder setVertexBytes:length:attributeStride:atIndex:];
-[MTLGPUDebugRenderCommandEncoder setTileTextures:withRange:];
-[MTLGPUDebugRenderCommandEncoder setVertexVisibleFunctionTables:withBufferRange:];
-[MTLGPUDebugRenderCommandEncoder drawPatches:patchIndexBuffer:patchIndexBufferOffset:indirectBuffer:indirectBufferOffset:];
-[MTLGPUDebugRenderCommandEncoder setFragmentTexture:atIndex:];
-[MTLGPUDebugRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:];
-[MTLGPUDebugRenderCommandEncoder setVertexBuffers:offsets:attributeStrides:withRange:];
-[MTLGPUDebugRenderCommandEncoder setVertexBytes:length:atIndex:];
-[MTLGPUDebugRenderCommandEncoder setTileBuffer:offset:atIndex:];
-[MTLGPUDebugRenderCommandEncoder setObjectBuffer:offset:atIndex:];
-[MTLGPUDebugRenderCommandEncoder setTileBuffers:offsets:withRange:];
-[MTLGPUDebugRenderCommandEncoder setMeshBuffer:offset:atIndex:];
-[MTLGPUDebugRenderCommandEncoder setObjectBuffers:offsets:withRange:];
-[MTLGPUDebugRenderCommandEncoder setTileVisibleFunctionTables:withBufferRange:];
-[MTLGPUDebugRenderCommandEncoder setVertexIntersectionFunctionTable:atBufferIndex:];
-[MTLGPUDebugRenderCommandEncoder setObjectIntersectionFunctionTable:atBufferIndex:];
-[MTLGPUDebugRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:];
-[MTLGPUDebugRenderCommandEncoder setVertexAccelerationStructure:atBufferIndex:];
-[MTLGPUDebugRenderCommandEncoder setFragmentVisibleFunctionTable:atBufferIndex:];
-[MTLGPUDebugRenderCommandEncoder setMeshAccelerationStructure:atBufferIndex:];
-[MTLGPUDebugRenderCommandEncoder useResource:usage:stages:];
-[MTLGPUDebugRenderCommandEncoder drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTLGPUDebugRenderCommandEncoder setFragmentVisibleFunctionTables:withBufferRange:];
-[MTLGPUDebugRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:];
-[MTLGPUDebugRenderCommandEncoder setVertexIntersectionFunctionTables:withBufferRange:];
-[MTLGPUDebugRenderCommandEncoder useHeaps:count:stages:];
-[MTLGPUDebugRenderCommandEncoder setThreadgroupMemoryLength:offset:atIndex:];
-[MTLGPUDebugRenderCommandEncoder setTessellationFactorBuffer:offset:instanceStride:];
-[MTLGPUDebugRenderCommandEncoder setTileBytes:length:atIndex:];
-[MTLGPUDebugRenderCommandEncoder setVertexAmplificationCount:viewMappings:];
-[MTLGPUDebugRenderCommandEncoder setVertexVisibleFunctionTable:atBufferIndex:];
-[MTLGPUDebugRenderCommandEncoder setDepthStencilState:];
-[MTLGPUDebugRenderCommandEncoder setVertexTexture:atIndex:];
-[MTLGPUDebugRenderCommandEncoder setMeshTextures:withRange:];
-[MTLGPUDebugRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:];
-[MTLGPUDebugRenderCommandEncoder setMeshBuffers:offsets:withRange:];
-[MTLGPUDebugRenderCommandEncoder useHeap:stages:];
-[MTLGPUDebugRenderCommandEncoder setObjectTexture:atIndex:];
-[MTLGPUDebugRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:];
-[MTLGPUDebugRenderCommandEncoder setTileIntersectionFunctionTables:withBufferRange:];
-[MTLGPUDebugRenderCommandEncoder setFragmentTextures:withRange:];
-[MTLGPUDebugRenderCommandEncoder useResources:count:usage:stages:];
-[MTLGPUDebugRenderCommandEncoder drawIndexedPatches:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:indirectBuffer:indirectBufferOffset:];
-[MTLGPUDebugRenderCommandEncoder setObjectThreadgroupMemoryLength:atIndex:];
-[MTLGPUDebugRenderCommandEncoder setObjectTextures:withRange:];
-[MTLGPUDebugRenderCommandEncoder setFragmentIntersectionFunctionTables:withBufferRange:];
-[MTLGPUDebugRenderCommandEncoder drawIndexedPrimitives:indexType:indexBuffer:indexBufferOffset:indirectBuffer:indirectBufferOffset:];
-[MTLGPUDebugRenderCommandEncoder setObjectBytes:length:atIndex:];
-[MTLGPUDebugRenderCommandEncoder setVertexBufferOffset:atIndex:];
-[MTLGPUDebugRenderCommandEncoder setMeshTexture:atIndex:];
-[MTLGPUDebugRenderCommandEncoder setVertexBuffer:offset:atIndex:];
-[MTLGPUDebugRenderCommandEncoder setVertexTextures:withRange:];
-[MTLGPUDebugRenderCommandEncoder dispatchThreadsPerTile:];
-[MTLGPUDebugRenderCommandEncoder setTileTexture:atIndex:];
-[MTLGPUDebugRenderCommandEncoder setTileIntersectionFunctionTable:atBufferIndex:];
-[MTLGPUDebugRenderCommandEncoder setMeshIntersectionFunctionTable:atBufferIndex:];
-[MTLGPUDebugRenderCommandEncoder drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTLGPUDebugRenderCommandEncoder setFragmentBytes:length:atIndex:];
-[MTLGPUDebugRenderCommandEncoder setFragmentAccelerationStructure:atBufferIndex:];
-[MTLGPUDebugRenderCommandEncoder setMeshBytes:length:atIndex:];
-[MTLGPUDebugRenderCommandEncoder dispatchThreadsPerTile:inRegion:];
-[MTLGPUDebugRenderCommandEncoder dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:];
-[MTLGPUDebugRenderCommandEncoder setMeshVisibleFunctionTable:atBufferIndex:];
-[MTLGPUDebugRenderCommandEncoder setMeshVisibleFunctionTables:withBufferRange:];
-[MTLGPUDebugRenderCommandEncoder setObjectVisibleFunctionTable:atBufferIndex:];
-[MTLGPUDebugRenderCommandEncoder setObjectVisibleFunctionTables:withBufferRange:];
-[MTLGPUDebugRenderCommandEncoder dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:withCondition:];
-[MTLGPUDebugRenderCommandEncoder dispatchThreadsPerTile:withCondition:];
-[MTLGPUDebugRenderCommandEncoder resetTileCondition];
-[MTLGPUDebugRenderCommandEncoder prepareExecuteIndirect:variant:];
-[MTLGPUDebugRenderCommandEncoder _internalBindingTableForStage:];
-[MTLGPUDebugRenderCommandEncoder _setBufferForStage:atIndex:stage:];
-[MTLGPUDebugRenderCommandEncoder _setInternalBindingTableForStage:stage:];
-[MTLGPUDebugRenderCommandEncoder _useResourceCommon:usage:stages:];
-[MTLGPUDebugRenderCommandEncoder bindInternalBufferForStage:index:stage:];
-[MTLGPUDebugRenderCommandEncoder bindInternalBufferForStage:index:stage:offset:];
-[MTLGPUDebugRenderCommandEncoder bindInternalValueForStage:index:stage:];
-[MTLGPUDebugRenderCommandEncoder encoderID];
-[MTLGPUDebugRenderCommandEncoder flushBindings];
-[MTLGPUDebugRenderCommandEncoder initWithRenderCommandEncoder:commandBuffer:descriptor:encoderID:];
-[MTLGPUDebugRenderCommandEncoder initWithRenderCommandEncoder:parallelEncoder:encoderID:];
-[MTLGPUDebugRenderCommandEncoder restoreInternalState:];
-[MTLGPUDebugRenderCommandEncoder setBufferUsageTable:textureUsageTable:tensorResidencyTable:bvhUsageTable:textureTypeTable:textureWriteUsageTable:forStage:];
-[MTLGPUDebugRenderCommandEncoder setInternalBytesForStage:length:atIndex:stage:];
-[MTLGPUDebugRenderCommandEncoder setRenderPipelineStateBuffers:];
-[MTLGPUDebugRenderCommandEncoder temporaryBufferWithBytes:length:];
-[MTLGPUDebugRenderCommandEncoder temporaryBufferWithLength:];
-[MTLGPUDebugRenderCommandEncoder useResourceInternal:usage:stages:];
```
