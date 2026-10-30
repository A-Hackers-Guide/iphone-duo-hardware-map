# `AGXG19FamilyComputeContext`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalComputeCommandEncoder`
- Protocols: `MTLComputeCommandEncoderSPI`
- 2 instance variables, 7 properties, 87 instance methods, 0 class methods

## Instance variables

```
^v _impl;
Q _markerID;
```

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) dispatchType;
```

## Instance methods

```
-[AGXG19FamilyComputeContext waitForFence:];
-[AGXG19FamilyComputeContext useResources:count:usage:];
-[AGXG19FamilyComputeContext setBuffers:offsets:withRange:];
-[AGXG19FamilyComputeContext executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:];
-[AGXG19FamilyComputeContext useResource:usage:];
-[AGXG19FamilyComputeContext setVisibleFunctionTables:withBufferRange:];
-[AGXG19FamilyComputeContext setBuffer:offset:atIndex:];
-[AGXG19FamilyComputeContext updateFence:];
-[AGXG19FamilyComputeContext setAccelerationStructure:atBufferIndex:];
-[AGXG19FamilyComputeContext executeCommandsInBuffer:withRange:];
-[AGXG19FamilyComputeContext useHeap:];
-[AGXG19FamilyComputeContext useHeaps:count:];
-[AGXG19FamilyComputeContext sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[AGXG19FamilyComputeContext setIntersectionFunctionTable:atBufferIndex:];
-[AGXG19FamilyComputeContext setVisibleFunctionTable:atBufferIndex:];
-[AGXG19FamilyComputeContext memoryBarrierWithScope:];
-[AGXG19FamilyComputeContext useResidencySet:];
-[AGXG19FamilyComputeContext dispatchThreadgroups:threadsPerThreadgroup:];
-[AGXG19FamilyComputeContext useResidencySets:count:];
-[AGXG19FamilyComputeContext setFunctionTable:atIndex:];
-[AGXG19FamilyComputeContext setTexture:atIndex:];
-[AGXG19FamilyComputeContext setSamplerState:atIndex:];
-[AGXG19FamilyComputeContext setSamplerStates:lodMinClamps:lodMaxClamps:withRange:];
-[AGXG19FamilyComputeContext setBytes:length:atIndex:];
-[AGXG19FamilyComputeContext endEncoding];
-[AGXG19FamilyComputeContext dealloc];
-[AGXG19FamilyComputeContext setThreadgroupMemoryLength:atIndex:];
-[AGXG19FamilyComputeContext setStageInRegion:];
-[AGXG19FamilyComputeContext setFunctionTables:withRange:];
-[AGXG19FamilyComputeContext setSamplerState:lodMinClamp:lodMaxClamp:atIndex:];
-[AGXG19FamilyComputeContext setStageInRegionWithIndirectBuffer:indirectBufferOffset:];
-[AGXG19FamilyComputeContext setBufferOffset:atIndex:];
-[AGXG19FamilyComputeContext setBuffer:offset:attributeStride:atIndex:];
-[AGXG19FamilyComputeContext dispatchThreads:threadsPerThreadgroup:];
-[AGXG19FamilyComputeContext dispatchType];
-[AGXG19FamilyComputeContext setSamplerStates:withRange:];
-[AGXG19FamilyComputeContext setComputePipelineState:];
-[AGXG19FamilyComputeContext setBuffers:offsets:attributeStrides:withRange:];
-[AGXG19FamilyComputeContext setImageblockWidth:height:];
-[AGXG19FamilyComputeContext setBufferOffset:attributeStride:atIndex:];
-[AGXG19FamilyComputeContext setTextures:withRange:];
-[AGXG19FamilyComputeContext setBytes:length:attributeStride:atIndex:];
-[AGXG19FamilyComputeContext memoryBarrierWithResources:count:];
-[AGXG19FamilyComputeContext setIntersectionFunctionTables:withBufferRange:];
-[AGXG19FamilyComputeContext dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:];
-[AGXG19FamilyComputeContext encodeStartElse];
-[AGXG19FamilyComputeContext setThreadgroupDistributionMode:];
-[AGXG19FamilyComputeContext signalProgress:];
-[AGXG19FamilyComputeContext barrierAfterQueueStages:beforeStages:];
-[AGXG19FamilyComputeContext beginVirtualSubstream];
-[AGXG19FamilyComputeContext commandBatchIdOffset];
-[AGXG19FamilyComputeContext commandBatchIdRangeMin:max:];
-[AGXG19FamilyComputeContext enableNullBufferBinds:];
-[AGXG19FamilyComputeContext encodeEndDoWhile:offset:comparison:referenceValue:];
-[AGXG19FamilyComputeContext encodeEndIf];
-[AGXG19FamilyComputeContext encodeEndWhile];
-[AGXG19FamilyComputeContext encodeStartDoWhile];
-[AGXG19FamilyComputeContext encodeStartIf:offset:comparison:referenceValue:];
-[AGXG19FamilyComputeContext encodeStartWhile:offset:comparison:referenceValue:];
-[AGXG19FamilyComputeContext endVirtualSubstream];
-[AGXG19FamilyComputeContext filterCounterRangeWithFirstBatch:lastBatch:filterIndex:];
-[AGXG19FamilyComputeContext flushCompressionMetadata];
-[AGXG19FamilyComputeContext getDriverUniqueID];
-[AGXG19FamilyComputeContext insertCompressedTextureReinterpretationFlush];
-[AGXG19FamilyComputeContext insertSplit];
-[AGXG19FamilyComputeContext nextVirtualSubstream];
-[AGXG19FamilyComputeContext setSubstream:];
-[AGXG19FamilyComputeContext setThreadgroupDistributionModeWithClusterGroupIndex:];
-[AGXG19FamilyComputeContext setToolsDispatchBufferSPI:atIndex:];
-[AGXG19FamilyComputeContext waitForProgress:];
-[AGXG19FamilyComputeContext waitForVirtualSubstream:];
-[AGXG19FamilyComputeContext addProtectedContentBarrier];
-[AGXG19FamilyComputeContext deferredEndEncoding];
-[AGXG19FamilyComputeContext destroyImpl];
-[AGXG19FamilyComputeContext dispatchFenceOnly];
-[AGXG19FamilyComputeContext dispatchFlushInvalidate];
-[AGXG19FamilyComputeContext dispatchFlushOnly];
-[AGXG19FamilyComputeContext dispatchInvalidateOnly];
-[AGXG19FamilyComputeContext dispatchThreadsWithIndirectBuffer:indirectBufferOffset:];
-[AGXG19FamilyComputeContext dispatchWaitFlush];
-[AGXG19FamilyComputeContext initWithCommandBuffer:config:];
-[AGXG19FamilyComputeContext newKernelDebugInfo];
-[AGXG19FamilyComputeContext parallelExecution];
-[AGXG19FamilyComputeContext reInitWithCommandBuffer:];
-[AGXG19FamilyComputeContext setImageBlockWidth:height:];
-[AGXG19FamilyComputeContext setMTLCounterSampleLocationWithBuffer:startIndex:endIndex:];
-[AGXG19FamilyComputeContext setParallelExecution:];
```
