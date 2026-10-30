# `AGXG19FamilyComputeContext_mtlnext`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetal4ComputeCommandEncoder`
- Protocols: `MTL4ComputeCommandEncoderGGDSPI`
- 12 instance variables, 9 properties, 86 instance methods, 0 class methods

## Instance variables

```
@"AGXG19FamilyCommandBuffer_mtlnext" _command_buffer;
^v _impl;
^v _blit_context;
^v _legacy_blit_context;
^v _bvh_builder;
@"AGXG19FamilyCommandAllocator_mtlnext" _allocator;
@"AGXG19FamilyDevice" _device;
Q _bvhBarrierBeforeStages;
B _bvhFlushNeedsReasourceAliasCFI;
B _bvhFlushOnSplit;
B _useFramework;
B _hasFrameworkBvhWork;
```

## Properties

```
@property (T@"<MTL4ArgumentTable>",R,N) currentArgumentTable;
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
-[AGXG19FamilyComputeContext_mtlnext useResources:count:usage:];
-[AGXG19FamilyComputeContext_mtlnext executeCommandsInBuffer:withRange:];
-[AGXG19FamilyComputeContext_mtlnext dispatchThreadgroups:threadsPerThreadgroup:];
-[AGXG19FamilyComputeContext_mtlnext endEncoding];
-[AGXG19FamilyComputeContext_mtlnext copyFromTexture:toTexture:];
-[AGXG19FamilyComputeContext_mtlnext dealloc];
-[AGXG19FamilyComputeContext_mtlnext setThreadgroupMemoryLength:atIndex:];
-[AGXG19FamilyComputeContext_mtlnext copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:];
-[AGXG19FamilyComputeContext_mtlnext dispatchThreads:threadsPerThreadgroup:];
-[AGXG19FamilyComputeContext_mtlnext optimizeContentsForCPUAccess:slice:level:];
-[AGXG19FamilyComputeContext_mtlnext optimizeIndirectCommandBuffer:withRange:];
-[AGXG19FamilyComputeContext_mtlnext setComputePipelineState:];
-[AGXG19FamilyComputeContext_mtlnext fillTexture:level:slice:region:color:];
-[AGXG19FamilyComputeContext_mtlnext setImageblockWidth:height:];
-[AGXG19FamilyComputeContext_mtlnext optimizeContentsForGPUAccess:];
-[AGXG19FamilyComputeContext_mtlnext fillBuffer:range:pattern4:];
-[AGXG19FamilyComputeContext_mtlnext fillTexture:level:slice:region:bytes:length:];
-[AGXG19FamilyComputeContext_mtlnext fillTexture:level:slice:region:color:pixelFormat:];
-[AGXG19FamilyComputeContext_mtlnext copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:];
-[AGXG19FamilyComputeContext_mtlnext resetCommandsInBuffer:withRange:];
-[AGXG19FamilyComputeContext_mtlnext optimizeContentsForCPUAccess:];
-[AGXG19FamilyComputeContext_mtlnext optimizeContentsForGPUAccess:slice:level:];
-[AGXG19FamilyComputeContext_mtlnext copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:];
-[AGXG19FamilyComputeContext_mtlnext copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[AGXG19FamilyComputeContext_mtlnext generateMipmapsForTexture:];
-[AGXG19FamilyComputeContext_mtlnext stages];
-[AGXG19FamilyComputeContext_mtlnext copyTextureMappingsFromTexture:toTexture:operations:count:];
-[AGXG19FamilyComputeContext_mtlnext setArgumentTable:];
-[AGXG19FamilyComputeContext_mtlnext updateTextureMappings:heap:operations:count:];
-[AGXG19FamilyComputeContext_mtlnext updateFence:afterEncoderStages:];
-[AGXG19FamilyComputeContext_mtlnext encodeStartElse];
-[AGXG19FamilyComputeContext_mtlnext barrierAfterEncoderStages:beforeEncoderStages:options:];
-[AGXG19FamilyComputeContext_mtlnext barrierAfterQueueStages:beforeStages:options:];
-[AGXG19FamilyComputeContext_mtlnext barrierAfterStages:beforeQueueStages:options:];
-[AGXG19FamilyComputeContext_mtlnext buildAccelerationStructure:descriptor:scratchBuffer:];
-[AGXG19FamilyComputeContext_mtlnext commandBatchIdOffset];
-[AGXG19FamilyComputeContext_mtlnext commandBatchIdRangeMin:max:];
-[AGXG19FamilyComputeContext_mtlnext copyAccelerationStructure:toAccelerationStructure:];
-[AGXG19FamilyComputeContext_mtlnext copyAndCompactAccelerationStructure:toAccelerationStructure:];
-[AGXG19FamilyComputeContext_mtlnext copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[AGXG19FamilyComputeContext_mtlnext copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[AGXG19FamilyComputeContext_mtlnext copyFromTensor:sourceOrigin:sourceDimensions:sourcePlane:toTensor:destinationOrigin:destinationDimensions:destinationPlane:];
-[AGXG19FamilyComputeContext_mtlnext copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:];
-[AGXG19FamilyComputeContext_mtlnext copyFromTensor:sourceSlice:toTensor:destinationSlice:];
-[AGXG19FamilyComputeContext_mtlnext copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:];
-[AGXG19FamilyComputeContext_mtlnext copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:];
-[AGXG19FamilyComputeContext_mtlnext currentArgumentTable];
-[AGXG19FamilyComputeContext_mtlnext deserializeInstanceAccelerationStructure:referencedAccelerationStructures:fromBuffer:];
-[AGXG19FamilyComputeContext_mtlnext deserializePrimitiveAccelerationStructure:fromBuffer:];
-[AGXG19FamilyComputeContext_mtlnext dispatchThreadgroupsWithIndirectBuffer:threadsPerThreadgroup:];
-[AGXG19FamilyComputeContext_mtlnext dispatchThreadsWithIndirectBuffer:];
-[AGXG19FamilyComputeContext_mtlnext encodeEndDoWhile:offset:comparison:referenceValue:];
-[AGXG19FamilyComputeContext_mtlnext encodeEndIf];
-[AGXG19FamilyComputeContext_mtlnext encodeEndWhile];
-[AGXG19FamilyComputeContext_mtlnext encodeStartDoWhile];
-[AGXG19FamilyComputeContext_mtlnext encodeStartIf:offset:comparison:referenceValue:];
-[AGXG19FamilyComputeContext_mtlnext encodeStartWhile:offset:comparison:referenceValue:];
-[AGXG19FamilyComputeContext_mtlnext executeCommandsInBuffer:indirectBuffer:];
-[AGXG19FamilyComputeContext_mtlnext fillBuffer:range:value:];
-[AGXG19FamilyComputeContext_mtlnext filterCounterRangeWithFirstBatch:lastBatch:filterIndex:];
-[AGXG19FamilyComputeContext_mtlnext flushCompressionMetadata];
-[AGXG19FamilyComputeContext_mtlnext refitAccelerationStructure:descriptor:destination:scratchBuffer:];
-[AGXG19FamilyComputeContext_mtlnext refitAccelerationStructure:descriptor:destination:scratchBuffer:options:];
-[AGXG19FamilyComputeContext_mtlnext serializeInstanceAccelerationStructure:referencedAccelerationStructures:toBuffer:];
-[AGXG19FamilyComputeContext_mtlnext serializePrimitiveAccelerationStructure:toBuffer:];
-[AGXG19FamilyComputeContext_mtlnext setToolsDispatchBufferSPI:atIndex:];
-[AGXG19FamilyComputeContext_mtlnext waitForFence:beforeEncoderStages:];
-[AGXG19FamilyComputeContext_mtlnext writeAccelerationStructureSerializationData:toBuffer:];
-[AGXG19FamilyComputeContext_mtlnext writeAccelerationStructureTraversalDepth:toBuffer:];
-[AGXG19FamilyComputeContext_mtlnext writeCompactedAccelerationStructureSize:toBuffer:];
-[AGXG19FamilyComputeContext_mtlnext writeDeserializedAccelerationStructureSize:toBuffer:];
-[AGXG19FamilyComputeContext_mtlnext writeGenericBVHStructureOfAccelerationStructure:into:];
-[AGXG19FamilyComputeContext_mtlnext writeGenericBVHStructureSizesOfAccelerationStructure:into:];
-[AGXG19FamilyComputeContext_mtlnext writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:];
-[AGXG19FamilyComputeContext_mtlnext writeSerializedAccelerationStructureSize:toBuffer:];
-[AGXG19FamilyComputeContext_mtlnext writeTimestampWithGranularity:intoHeap:atIndex:];
-[AGXG19FamilyComputeContext_mtlnext copyTextureMappingsFromTexture:sourceSlices:sourceLevels:sourceOrigins:sourceSizes:numSizes:toTexture:destinationSlices:destinationLevels:destinationOrigins:];
-[AGXG19FamilyComputeContext_mtlnext destroyImpl];
-[AGXG19FamilyComputeContext_mtlnext encodeSSTTFlushInvalidate];
-[AGXG19FamilyComputeContext_mtlnext encodeSyncComputeWithBackFacingBarrierSrcMask:BackFacingBarrierDstMask:FrontFacingBarrierSrcMask:FrontFacingBarrierDstMask:];
-[AGXG19FamilyComputeContext_mtlnext initWithCommandBuffer:allocator:captureProgramAddressTable:];
-[AGXG19FamilyComputeContext_mtlnext initWithCommandBufferForQueueSparseOperation:allocator:];
-[AGXG19FamilyComputeContext_mtlnext internalResolveCounterHeap:offset:size:destAddress:destResource:];
-[AGXG19FamilyComputeContext_mtlnext needsSSTTFlushInvalidate];
-[AGXG19FamilyComputeContext_mtlnext performEndEncoding];
-[AGXG19FamilyComputeContext_mtlnext updateTextureMappings:numRegions:regions:levels:slices:heap:rangeModes:rangeOffsets:];
```
