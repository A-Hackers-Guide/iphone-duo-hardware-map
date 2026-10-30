# `_MTL4ComputeCommandEncoder`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTL4CommandEncoder`
- Protocols: `MTL4ComputeCommandEncoderGGDSPI`
- 0 instance variables, 9 properties, 80 instance methods, 0 class methods

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
-[_MTL4ComputeCommandEncoder executeCommandsInBuffer:withRange:];
-[_MTL4ComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:];
-[_MTL4ComputeCommandEncoder copyFromTexture:toTexture:];
-[_MTL4ComputeCommandEncoder setThreadgroupMemoryLength:atIndex:];
-[_MTL4ComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:];
-[_MTL4ComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:];
-[_MTL4ComputeCommandEncoder optimizeContentsForCPUAccess:slice:level:];
-[_MTL4ComputeCommandEncoder optimizeIndirectCommandBuffer:withRange:];
-[_MTL4ComputeCommandEncoder setComputePipelineState:];
-[_MTL4ComputeCommandEncoder fillTexture:level:slice:region:color:];
-[_MTL4ComputeCommandEncoder setImageblockWidth:height:];
-[_MTL4ComputeCommandEncoder optimizeContentsForGPUAccess:];
-[_MTL4ComputeCommandEncoder fillBuffer:range:pattern4:];
-[_MTL4ComputeCommandEncoder fillTexture:level:slice:region:bytes:length:];
-[_MTL4ComputeCommandEncoder fillTexture:level:slice:region:color:pixelFormat:];
-[_MTL4ComputeCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:];
-[_MTL4ComputeCommandEncoder resetCommandsInBuffer:withRange:];
-[_MTL4ComputeCommandEncoder optimizeContentsForCPUAccess:];
-[_MTL4ComputeCommandEncoder optimizeContentsForGPUAccess:slice:level:];
-[_MTL4ComputeCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:];
-[_MTL4ComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[_MTL4ComputeCommandEncoder generateMipmapsForTexture:];
-[_MTL4ComputeCommandEncoder stages];
-[_MTL4ComputeCommandEncoder setArgumentTable:];
-[_MTL4ComputeCommandEncoder encodeStartElse];
-[_MTL4ComputeCommandEncoder setThreadgroupDistributionMode:];
-[_MTL4ComputeCommandEncoder signalProgress:];
-[_MTL4ComputeCommandEncoder beginVirtualSubstream];
-[_MTL4ComputeCommandEncoder buildAccelerationStructure:descriptor:scratchBuffer:];
-[_MTL4ComputeCommandEncoder copyAccelerationStructure:toAccelerationStructure:];
-[_MTL4ComputeCommandEncoder copyAndCompactAccelerationStructure:toAccelerationStructure:];
-[_MTL4ComputeCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[_MTL4ComputeCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[_MTL4ComputeCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:sourcePlane:toTensor:destinationOrigin:destinationDimensions:destinationPlane:];
-[_MTL4ComputeCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:];
-[_MTL4ComputeCommandEncoder copyFromTensor:sourceSlice:toTensor:destinationSlice:];
-[_MTL4ComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:];
-[_MTL4ComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:];
-[_MTL4ComputeCommandEncoder currentArgumentTable];
-[_MTL4ComputeCommandEncoder deserializeInstanceAccelerationStructure:referencedAccelerationStructures:fromBuffer:];
-[_MTL4ComputeCommandEncoder deserializePrimitiveAccelerationStructure:fromBuffer:];
-[_MTL4ComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:threadsPerThreadgroup:];
-[_MTL4ComputeCommandEncoder dispatchThreadsWithIndirectBuffer:];
-[_MTL4ComputeCommandEncoder enableNullBufferBinds:];
-[_MTL4ComputeCommandEncoder encodeEndDoWhile:comparison:referenceValue:];
-[_MTL4ComputeCommandEncoder encodeEndDoWhile:offset:comparison:referenceValue:];
-[_MTL4ComputeCommandEncoder encodeEndIf];
-[_MTL4ComputeCommandEncoder encodeEndWhile];
-[_MTL4ComputeCommandEncoder encodeStartDoWhile];
-[_MTL4ComputeCommandEncoder encodeStartIf:comparison:referenceValue:];
-[_MTL4ComputeCommandEncoder encodeStartIf:offset:comparison:referenceValue:];
-[_MTL4ComputeCommandEncoder encodeStartWhile:comparison:referenceValue:];
-[_MTL4ComputeCommandEncoder encodeStartWhile:offset:comparison:referenceValue:];
-[_MTL4ComputeCommandEncoder endVirtualSubstream];
-[_MTL4ComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:];
-[_MTL4ComputeCommandEncoder fillBuffer:range:value:];
-[_MTL4ComputeCommandEncoder flushCompressionMetadata];
-[_MTL4ComputeCommandEncoder initWithCommandAllocator:];
-[_MTL4ComputeCommandEncoder insertCompressedTextureReinterpretationFlush];
-[_MTL4ComputeCommandEncoder invalidateCompressedTexture:];
-[_MTL4ComputeCommandEncoder invalidateCompressedTexture:slice:level:];
-[_MTL4ComputeCommandEncoder nextVirtualSubstream];
-[_MTL4ComputeCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:];
-[_MTL4ComputeCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:options:];
-[_MTL4ComputeCommandEncoder serializeInstanceAccelerationStructure:referencedAccelerationStructures:toBuffer:];
-[_MTL4ComputeCommandEncoder serializePrimitiveAccelerationStructure:toBuffer:];
-[_MTL4ComputeCommandEncoder setSubstream:];
-[_MTL4ComputeCommandEncoder setThreadgroupDistributionModeWithClusterGroupIndex:];
-[_MTL4ComputeCommandEncoder setToolsDispatchBufferSPI:atIndex:];
-[_MTL4ComputeCommandEncoder waitForProgress:];
-[_MTL4ComputeCommandEncoder waitForVirtualSubstream:];
-[_MTL4ComputeCommandEncoder writeAccelerationStructureSerializationData:toBuffer:];
-[_MTL4ComputeCommandEncoder writeAccelerationStructureTraversalDepth:toBuffer:];
-[_MTL4ComputeCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:];
-[_MTL4ComputeCommandEncoder writeDeserializedAccelerationStructureSize:toBuffer:];
-[_MTL4ComputeCommandEncoder writeGenericBVHStructureOfAccelerationStructure:into:];
-[_MTL4ComputeCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:into:];
-[_MTL4ComputeCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:];
-[_MTL4ComputeCommandEncoder writeSerializedAccelerationStructureSize:toBuffer:];
-[_MTL4ComputeCommandEncoder writeTimestampWithGranularity:intoHeap:atIndex:];
```
