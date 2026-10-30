# `MTLGPUDebugComputeCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsComputeCommandEncoder`
- Protocols: `MTLGPUDebugCommandEncoder`
- 14 instance variables, 6 properties, 54 instance methods, 0 class methods

## Instance variables

```
I useResourceIteration;
B _enableUseResourceValidation;
I _commandBufferJumpNestingLevel;
^{Options=IiiiI{?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}} _options;
{MTLGPUDebugThreadgroupLengths="threadgroupSizes"[31I]"entries"[32{GPUDebugThreadgroupTableEntry="offset"I"length"I}]"needsFlush"B} _threadgroup;
{GPUDebugEventUUIDPacket="crc"Q"pipelineStateID"Q"entryPointImageID"Q"encoderID"I"commandInfo"I} _dispatchID;
@"MTLGPUDebugComputePipelineState" _currentPipeline;
[31{GPUDebugEncoderBoundBuffers="resource"@"<MTLResource>""offset"Q"stride"Q"type"Q}] _computeEncoderBoundBuffers;
^{ResourceUsageTable=^{MTLGPUDebugStorageManager}@@I{shared_mutex={__shared_mutex_base={mutex={_opaque_pthread_mutex_t=q[56c]}}{condition_variable={_opaque_pthread_cond_t=q[40c]}}{condition_variable={_opaque_pthread_cond_t=q[40c]}}I}}} _bufferUsageTable;
^{ResourceUsageTable=^{MTLGPUDebugStorageManager}@@I{shared_mutex={__shared_mutex_base={mutex={_opaque_pthread_mutex_t=q[56c]}}{condition_variable={_opaque_pthread_cond_t=q[40c]}}{condition_variable={_opaque_pthread_cond_t=q[40c]}}I}}} _textureUsageTable;
^{ResourceUsageTable=^{MTLGPUDebugStorageManager}@@I{shared_mutex={__shared_mutex_base={mutex={_opaque_pthread_mutex_t=q[56c]}}{condition_variable={_opaque_pthread_cond_t=q[40c]}}{condition_variable={_opaque_pthread_cond_t=q[40c]}}I}}} _tensorResidencyTable;
@"<MTLBuffer>" _internalBindingTable;
^{ResourceUsageTable=^{MTLGPUDebugStorageManager}@@I{shared_mutex={__shared_mutex_base={mutex={_opaque_pthread_mutex_t=q[56c]}}{condition_variable={_opaque_pthread_cond_t=q[40c]}}{condition_variable={_opaque_pthread_cond_t=q[40c]}}I}}} _bvhUsageTable;
@"<MTLBuffer>" _textureTypeTable;
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
-[MTLGPUDebugComputeCommandEncoder useResources:count:usage:];
-[MTLGPUDebugComputeCommandEncoder setBuffers:offsets:withRange:];
-[MTLGPUDebugComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:];
-[MTLGPUDebugComputeCommandEncoder useResource:usage:];
-[MTLGPUDebugComputeCommandEncoder setVisibleFunctionTables:withBufferRange:];
-[MTLGPUDebugComputeCommandEncoder setBuffer:offset:atIndex:];
-[MTLGPUDebugComputeCommandEncoder setAccelerationStructure:atBufferIndex:];
-[MTLGPUDebugComputeCommandEncoder executeCommandsInBuffer:withRange:];
-[MTLGPUDebugComputeCommandEncoder useHeap:];
-[MTLGPUDebugComputeCommandEncoder useHeaps:count:];
-[MTLGPUDebugComputeCommandEncoder setIntersectionFunctionTable:atBufferIndex:];
-[MTLGPUDebugComputeCommandEncoder setVisibleFunctionTable:atBufferIndex:];
-[MTLGPUDebugComputeCommandEncoder useResidencySet:];
-[MTLGPUDebugComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:];
-[MTLGPUDebugComputeCommandEncoder useResidencySets:count:];
-[MTLGPUDebugComputeCommandEncoder setTexture:atIndex:];
-[MTLGPUDebugComputeCommandEncoder setBytes:length:atIndex:];
-[MTLGPUDebugComputeCommandEncoder endEncoding];
-[MTLGPUDebugComputeCommandEncoder setThreadgroupMemoryLength:atIndex:];
-[MTLGPUDebugComputeCommandEncoder setBufferOffset:atIndex:];
-[MTLGPUDebugComputeCommandEncoder setBuffer:offset:attributeStride:atIndex:];
-[MTLGPUDebugComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:];
-[MTLGPUDebugComputeCommandEncoder setComputePipelineState:];
-[MTLGPUDebugComputeCommandEncoder setBuffers:offsets:attributeStrides:withRange:];
-[MTLGPUDebugComputeCommandEncoder setTextures:withRange:];
-[MTLGPUDebugComputeCommandEncoder setBytes:length:attributeStride:atIndex:];
-[MTLGPUDebugComputeCommandEncoder setIntersectionFunctionTables:withBufferRange:];
-[MTLGPUDebugComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:];
-[MTLGPUDebugComputeCommandEncoder beginVirtualSubstream];
-[MTLGPUDebugComputeCommandEncoder encodeEndDoWhile:offset:comparison:referenceValue:];
-[MTLGPUDebugComputeCommandEncoder encodeEndIf];
-[MTLGPUDebugComputeCommandEncoder encodeEndWhile];
-[MTLGPUDebugComputeCommandEncoder encodeStartDoWhile];
-[MTLGPUDebugComputeCommandEncoder encodeStartIf:offset:comparison:referenceValue:];
-[MTLGPUDebugComputeCommandEncoder encodeStartWhile:offset:comparison:referenceValue:];
-[MTLGPUDebugComputeCommandEncoder endVirtualSubstream];
-[MTLGPUDebugComputeCommandEncoder nextVirtualSubstream];
-[MTLGPUDebugComputeCommandEncoder waitForVirtualSubstream:];
-[MTLGPUDebugComputeCommandEncoder dispatchThreadsWithIndirectBuffer:indirectBufferOffset:];
-[MTLGPUDebugComputeCommandEncoder setComputePipelineStateBuffers:];
-[MTLGPUDebugComputeCommandEncoder bindInternalBuffer:index:];
-[MTLGPUDebugComputeCommandEncoder bindInternalBufferWithOffset:offset:index:];
-[MTLGPUDebugComputeCommandEncoder bindInternalValue:index:];
-[MTLGPUDebugComputeCommandEncoder encoderID];
-[MTLGPUDebugComputeCommandEncoder flushBindings];
-[MTLGPUDebugComputeCommandEncoder initWithComputeCommandEncoder:commandBuffer:descriptor:encoderID:];
-[MTLGPUDebugComputeCommandEncoder initWithComputeCommandEncoder:parent:encoderID:];
-[MTLGPUDebugComputeCommandEncoder setAccelerationStructures:withBufferRange:];
-[MTLGPUDebugComputeCommandEncoder setBufferUsageTable:textureUsageTable:tensorResidencyTable:bvhUsageTable:textureTypeTable:textureWriteUsageTable:];
-[MTLGPUDebugComputeCommandEncoder setInternalBindingTable:];
-[MTLGPUDebugComputeCommandEncoder setInternalBytes:length:atIndex:];
-[MTLGPUDebugComputeCommandEncoder temporaryBufferWithBytes:length:];
-[MTLGPUDebugComputeCommandEncoder temporaryBufferWithLength:];
-[MTLGPUDebugComputeCommandEncoder useResourceInternal:usage:];
```
