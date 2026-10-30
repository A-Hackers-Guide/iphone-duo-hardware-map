# `MTLLegacySVComputeCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsComputeCommandEncoder`
- Protocols: `MTLLegacySVCommandEncoder`
- 11 instance variables, 6 properties, 48 instance methods, 0 class methods

## Instance variables

```
I useResourceIteration;
B _enableUseResourceValidation;
I _commandBufferJumpNestingLevel;
^{Options=IiiiI{?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}} _options;
{MTLLegacySVStageBufferHandles="handles"[31Q]"resources"[31@"<MTLLegacySVResource>"]"offsets"[31Q]"strides"[31Q]"lengths"[31I]"gpu_address"[31[2Q]]"needsFlush"B} _handles;
{MTLLegacySVThreadgroupLengths="threadgroupSizes"[31I]"entries"[32{GPUDebugThreadgroupTableEntry="offset"I"length"I}]"needsFlush"B} _threadgroup;
{LegacyEventUUIDPacket="pipelineStateID"Q"entryPointImageID"Q"encoderID"I"eventID"I} _dispatchID;
@"MTLLegacySVComputePipelineState" _currentPipeline;
{MTLLegacySVBufferSubAlloc="buffer"@"<MTLBuffer>""offset"Q} _reportBuffer;
@"<MTLBuffer>" _bufferUsageTable;
@"<MTLBuffer>" _textureUsageTable;
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
-[MTLLegacySVComputeCommandEncoder useResources:count:usage:];
-[MTLLegacySVComputeCommandEncoder setBuffers:offsets:withRange:];
-[MTLLegacySVComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:];
-[MTLLegacySVComputeCommandEncoder useResource:usage:];
-[MTLLegacySVComputeCommandEncoder setVisibleFunctionTables:withBufferRange:];
-[MTLLegacySVComputeCommandEncoder setBuffer:offset:atIndex:];
-[MTLLegacySVComputeCommandEncoder setAccelerationStructure:atBufferIndex:];
-[MTLLegacySVComputeCommandEncoder executeCommandsInBuffer:withRange:];
-[MTLLegacySVComputeCommandEncoder useHeap:];
-[MTLLegacySVComputeCommandEncoder useHeaps:count:];
-[MTLLegacySVComputeCommandEncoder setIntersectionFunctionTable:atBufferIndex:];
-[MTLLegacySVComputeCommandEncoder setVisibleFunctionTable:atBufferIndex:];
-[MTLLegacySVComputeCommandEncoder useResidencySet:];
-[MTLLegacySVComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:];
-[MTLLegacySVComputeCommandEncoder useResidencySets:count:];
-[MTLLegacySVComputeCommandEncoder setTexture:atIndex:];
-[MTLLegacySVComputeCommandEncoder setBytes:length:atIndex:];
-[MTLLegacySVComputeCommandEncoder endEncoding];
-[MTLLegacySVComputeCommandEncoder setThreadgroupMemoryLength:atIndex:];
-[MTLLegacySVComputeCommandEncoder setBufferOffset:atIndex:];
-[MTLLegacySVComputeCommandEncoder setBuffer:offset:attributeStride:atIndex:];
-[MTLLegacySVComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:];
-[MTLLegacySVComputeCommandEncoder setComputePipelineState:];
-[MTLLegacySVComputeCommandEncoder setBuffers:offsets:attributeStrides:withRange:];
-[MTLLegacySVComputeCommandEncoder setBufferOffset:attributeStride:atIndex:];
-[MTLLegacySVComputeCommandEncoder setTextures:withRange:];
-[MTLLegacySVComputeCommandEncoder setBytes:length:attributeStride:atIndex:];
-[MTLLegacySVComputeCommandEncoder setIntersectionFunctionTables:withBufferRange:];
-[MTLLegacySVComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:];
-[MTLLegacySVComputeCommandEncoder encodeEndDoWhile:offset:comparison:referenceValue:];
-[MTLLegacySVComputeCommandEncoder encodeEndIf];
-[MTLLegacySVComputeCommandEncoder encodeEndWhile];
-[MTLLegacySVComputeCommandEncoder encodeStartDoWhile];
-[MTLLegacySVComputeCommandEncoder encodeStartIf:offset:comparison:referenceValue:];
-[MTLLegacySVComputeCommandEncoder encodeStartWhile:offset:comparison:referenceValue:];
-[MTLLegacySVComputeCommandEncoder dispatchThreadsWithIndirectBuffer:indirectBufferOffset:];
-[MTLLegacySVComputeCommandEncoder setComputePipelineStateBuffers:];
-[MTLLegacySVComputeCommandEncoder _initBufferArgumentData:];
-[MTLLegacySVComputeCommandEncoder encoderID];
-[MTLLegacySVComputeCommandEncoder flushBindings];
-[MTLLegacySVComputeCommandEncoder initWithComputeCommandEncoder:commandBuffer:descriptor:encoderID:];
-[MTLLegacySVComputeCommandEncoder initWithComputeCommandEncoder:parent:encoderID:];
-[MTLLegacySVComputeCommandEncoder setAccelerationStructures:withBufferRange:];
-[MTLLegacySVComputeCommandEncoder setBufferUsageTable:textureUsageTable:];
-[MTLLegacySVComputeCommandEncoder setKernelReportBuffer:offset:];
-[MTLLegacySVComputeCommandEncoder temporaryBufferWithBytes:length:];
-[MTLLegacySVComputeCommandEncoder temporaryBufferWithLength:];
-[MTLLegacySVComputeCommandEncoder useResourceInternal:usage:];
```
