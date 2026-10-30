# `MTL4GPUDebugRenderCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4ToolsRenderCommandEncoder`
- Protocols: `MTLGPUDebugCommandEncoder`
- 19 instance variables, 5 properties, 41 instance methods, 0 class methods

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
{MTLGPUDebugTileThreadgroup="entries"[32{GPUDebugThreadgroupTableEntry="offset"I"length"I}]"needsFlush"B} _tileThreadgroup;
{MTLGPUDebugThreadgroupLengths="threadgroupSizes"[31I]"entries"[32{GPUDebugThreadgroupTableEntry="offset"I"length"I}]"needsFlush"B} _meshThreadgroup;
{MTLGPUDebugThreadgroupLengths="threadgroupSizes"[31I]"entries"[32{GPUDebugThreadgroupTableEntry="offset"I"length"I}]"needsFlush"B} _objectThreadgroup;
^{Options=IiiiI{?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}} _options;
{GPUDebugEventUUIDPacket="crc"Q"pipelineStateID"Q"entryPointImageID"Q"encoderID"I"commandInfo"I} _drawID;
q _encoderType;
@"MTLGPUDebugRenderPipelineState" _currentPipeline;
@"MTLToolsDepthStencilState" _currentDepthStencil;
[5@"<MTL4ArgumentTable>"] currentArgumentTables;
{?="count"C"mappingsValid"B"mappings"[2{?="viewportArrayIndexOffset"I"renderTargetArrayIndexOffset"I}]} _vertexAmpState;
[5[40Q]] _internalBindingTables;
```

## Properties

```
@property (TI,R) encoderID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTL4GPUDebugRenderCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:];
-[MTL4GPUDebugRenderCommandEncoder executeCommandsInBuffer:withRange:];
-[MTL4GPUDebugRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:];
-[MTL4GPUDebugRenderCommandEncoder endEncoding];
-[MTL4GPUDebugRenderCommandEncoder setRenderPipelineState:];
-[MTL4GPUDebugRenderCommandEncoder drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTL4GPUDebugRenderCommandEncoder setThreadgroupMemoryLength:offset:atIndex:];
-[MTL4GPUDebugRenderCommandEncoder setVertexAmplificationCount:viewMappings:];
-[MTL4GPUDebugRenderCommandEncoder setDepthStencilState:];
-[MTL4GPUDebugRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:];
-[MTL4GPUDebugRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:];
-[MTL4GPUDebugRenderCommandEncoder setObjectThreadgroupMemoryLength:atIndex:];
-[MTL4GPUDebugRenderCommandEncoder dispatchThreadsPerTile:];
-[MTL4GPUDebugRenderCommandEncoder drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTL4GPUDebugRenderCommandEncoder dispatchThreadsPerTile:inRegion:];
-[MTL4GPUDebugRenderCommandEncoder dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:];
-[MTL4GPUDebugRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:];
-[MTL4GPUDebugRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:];
-[MTL4GPUDebugRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:baseVertex:baseInstance:];
-[MTL4GPUDebugRenderCommandEncoder drawIndexedPrimitives:indexType:indexBuffer:indexBufferLength:indirectBuffer:];
-[MTL4GPUDebugRenderCommandEncoder drawMeshThreadgroupsWithIndirectBuffer:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTL4GPUDebugRenderCommandEncoder drawPrimitives:indirectBuffer:];
-[MTL4GPUDebugRenderCommandEncoder setArgumentTable:atStages:];
-[MTL4GPUDebugRenderCommandEncoder commandInfo];
-[MTL4GPUDebugRenderCommandEncoder getInternalValueForStage:stage:];
-[MTL4GPUDebugRenderCommandEncoder prepareExecuteIndirect:variant:];
-[MTL4GPUDebugRenderCommandEncoder _internalBindingTableForStage:];
-[MTL4GPUDebugRenderCommandEncoder bindInternalBufferForStage:index:stage:];
-[MTL4GPUDebugRenderCommandEncoder bindInternalBufferForStage:index:stage:offset:];
-[MTL4GPUDebugRenderCommandEncoder bindInternalValueForStage:index:stage:];
-[MTL4GPUDebugRenderCommandEncoder encoderID];
-[MTL4GPUDebugRenderCommandEncoder flushBindings];
-[MTL4GPUDebugRenderCommandEncoder initWithRenderCommandEncoder:commandBuffer:descriptor:encoderID:];
-[MTL4GPUDebugRenderCommandEncoder processAttachmentDescriptor:encoderInfo:commandInfo:];
-[MTL4GPUDebugRenderCommandEncoder restoreInternalState:];
-[MTL4GPUDebugRenderCommandEncoder setBufferUsageTable:textureUsageTable:tensorResidencyTable:bvhUsageTable:textureTypeTable:];
-[MTL4GPUDebugRenderCommandEncoder setInternalBytesForStage:length:atIndex:stage:];
-[MTL4GPUDebugRenderCommandEncoder setRenderPipelineStateBuffers:];
-[MTL4GPUDebugRenderCommandEncoder temporaryBufferWithBytes:length:];
-[MTL4GPUDebugRenderCommandEncoder temporaryBufferWithLength:];
-[MTL4GPUDebugRenderCommandEncoder validateAttachmentResourcesFromDescriptor:encoderInfo:];
```
