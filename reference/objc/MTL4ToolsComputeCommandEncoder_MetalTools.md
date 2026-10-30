# `MTL4ToolsComputeCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4ToolsCommandEncoder`
- Protocols: `MTL4ComputeCommandEncoderGGDSPI`
- 1 instance variables, 9 properties, 83 instance methods, 0 class methods

## Instance variables

```
@"<MTL4ArgumentTable>" _currentArgumentTable;
```

## Properties

```
@property (T@"<MTL4ArgumentTable>",R,N,V_currentArgumentTable) currentArgumentTable;
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
-[MTL4ToolsComputeCommandEncoder executeCommandsInBuffer:withRange:];
-[MTL4ToolsComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:];
-[MTL4ToolsComputeCommandEncoder endEncoding];
-[MTL4ToolsComputeCommandEncoder copyFromTexture:toTexture:];
-[MTL4ToolsComputeCommandEncoder dealloc];
-[MTL4ToolsComputeCommandEncoder setThreadgroupMemoryLength:atIndex:];
-[MTL4ToolsComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:];
-[MTL4ToolsComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:];
-[MTL4ToolsComputeCommandEncoder optimizeContentsForCPUAccess:slice:level:];
-[MTL4ToolsComputeCommandEncoder optimizeIndirectCommandBuffer:withRange:];
-[MTL4ToolsComputeCommandEncoder setComputePipelineState:];
-[MTL4ToolsComputeCommandEncoder fillTexture:level:slice:region:color:];
-[MTL4ToolsComputeCommandEncoder setImageblockWidth:height:];
-[MTL4ToolsComputeCommandEncoder optimizeContentsForGPUAccess:];
-[MTL4ToolsComputeCommandEncoder fillBuffer:range:pattern4:];
-[MTL4ToolsComputeCommandEncoder fillTexture:level:slice:region:bytes:length:];
-[MTL4ToolsComputeCommandEncoder fillTexture:level:slice:region:color:pixelFormat:];
-[MTL4ToolsComputeCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:];
-[MTL4ToolsComputeCommandEncoder resetCommandsInBuffer:withRange:];
-[MTL4ToolsComputeCommandEncoder optimizeContentsForCPUAccess:];
-[MTL4ToolsComputeCommandEncoder optimizeContentsForGPUAccess:slice:level:];
-[MTL4ToolsComputeCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:];
-[MTL4ToolsComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTL4ToolsComputeCommandEncoder generateMipmapsForTexture:];
-[MTL4ToolsComputeCommandEncoder stages];
-[MTL4ToolsComputeCommandEncoder setArgumentTable:];
-[MTL4ToolsComputeCommandEncoder encodeStartElse];
-[MTL4ToolsComputeCommandEncoder setThreadgroupDistributionMode:];
-[MTL4ToolsComputeCommandEncoder signalProgress:];
-[MTL4ToolsComputeCommandEncoder beginVirtualSubstream];
-[MTL4ToolsComputeCommandEncoder buildAccelerationStructure:descriptor:scratchBuffer:];
-[MTL4ToolsComputeCommandEncoder copyAccelerationStructure:toAccelerationStructure:];
-[MTL4ToolsComputeCommandEncoder copyAndCompactAccelerationStructure:toAccelerationStructure:];
-[MTL4ToolsComputeCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTL4ToolsComputeCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[MTL4ToolsComputeCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:sourcePlane:toTensor:destinationOrigin:destinationDimensions:destinationPlane:];
-[MTL4ToolsComputeCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:];
-[MTL4ToolsComputeCommandEncoder copyFromTensor:sourceSlice:toTensor:destinationSlice:];
-[MTL4ToolsComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:];
-[MTL4ToolsComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:];
-[MTL4ToolsComputeCommandEncoder currentArgumentTable];
-[MTL4ToolsComputeCommandEncoder deserializeInstanceAccelerationStructure:referencedAccelerationStructures:fromBuffer:];
-[MTL4ToolsComputeCommandEncoder deserializePrimitiveAccelerationStructure:fromBuffer:];
-[MTL4ToolsComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:threadsPerThreadgroup:];
-[MTL4ToolsComputeCommandEncoder dispatchThreadsWithIndirectBuffer:];
-[MTL4ToolsComputeCommandEncoder enableNullBufferBinds:];
-[MTL4ToolsComputeCommandEncoder encodeEndDoWhile:comparison:referenceValue:];
-[MTL4ToolsComputeCommandEncoder encodeEndDoWhile:offset:comparison:referenceValue:];
-[MTL4ToolsComputeCommandEncoder encodeEndIf];
-[MTL4ToolsComputeCommandEncoder encodeEndWhile];
-[MTL4ToolsComputeCommandEncoder encodeStartDoWhile];
-[MTL4ToolsComputeCommandEncoder encodeStartIf:comparison:referenceValue:];
-[MTL4ToolsComputeCommandEncoder encodeStartIf:offset:comparison:referenceValue:];
-[MTL4ToolsComputeCommandEncoder encodeStartWhile:comparison:referenceValue:];
-[MTL4ToolsComputeCommandEncoder encodeStartWhile:offset:comparison:referenceValue:];
-[MTL4ToolsComputeCommandEncoder endVirtualSubstream];
-[MTL4ToolsComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:];
-[MTL4ToolsComputeCommandEncoder fillBuffer:range:value:];
-[MTL4ToolsComputeCommandEncoder flushCompressionMetadata];
-[MTL4ToolsComputeCommandEncoder initWithBaseObject:parent:];
-[MTL4ToolsComputeCommandEncoder insertCompressedTextureReinterpretationFlush];
-[MTL4ToolsComputeCommandEncoder invalidateCompressedTexture:];
-[MTL4ToolsComputeCommandEncoder invalidateCompressedTexture:slice:level:];
-[MTL4ToolsComputeCommandEncoder nextVirtualSubstream];
-[MTL4ToolsComputeCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:];
-[MTL4ToolsComputeCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:options:];
-[MTL4ToolsComputeCommandEncoder serializeInstanceAccelerationStructure:referencedAccelerationStructures:toBuffer:];
-[MTL4ToolsComputeCommandEncoder serializePrimitiveAccelerationStructure:toBuffer:];
-[MTL4ToolsComputeCommandEncoder setSubstream:];
-[MTL4ToolsComputeCommandEncoder setThreadgroupDistributionModeWithClusterGroupIndex:];
-[MTL4ToolsComputeCommandEncoder setToolsDispatchBufferSPI:atIndex:];
-[MTL4ToolsComputeCommandEncoder waitForProgress:];
-[MTL4ToolsComputeCommandEncoder waitForVirtualSubstream:];
-[MTL4ToolsComputeCommandEncoder writeAccelerationStructureSerializationData:toBuffer:];
-[MTL4ToolsComputeCommandEncoder writeAccelerationStructureTraversalDepth:toBuffer:];
-[MTL4ToolsComputeCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:];
-[MTL4ToolsComputeCommandEncoder writeDeserializedAccelerationStructureSize:toBuffer:];
-[MTL4ToolsComputeCommandEncoder writeGenericBVHStructureOfAccelerationStructure:into:];
-[MTL4ToolsComputeCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:into:];
-[MTL4ToolsComputeCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:];
-[MTL4ToolsComputeCommandEncoder writeSerializedAccelerationStructureSize:toBuffer:];
-[MTL4ToolsComputeCommandEncoder writeTimestampWithGranularity:intoHeap:atIndex:];
-[MTL4ToolsComputeCommandEncoder releaseArgumentTable];
```
