# `MTL4DebugComputeCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4ToolsComputeCommandEncoder`
- 11 instance variables, 0 properties, 94 instance methods, 0 class methods

## Instance variables

```
@"MTL4DebugCommandEncoder" _debugCommandEncoder;
{MTL4DebugComputeCommandEncoderState="canSetComputePipelineState"b1"hasSetComputePipelineState"b1"hasEncodedCommandBufferJump"b1"isEncodingVirtualSubstream"b1"isEncodingCommandBufferJump"b1} _encoderState;
Q _numSubstreams;
B _allowsNullBufferBindings;
[31{MTLDebugFunctionArgument="isValid"B"hasBeenUsed"B"type"Q"object"@"baseLevel"Q"bufferLength"Q"bufferOffset"Q"bufferAttributeStride"Q"threadgroupMemoryLength"Q"threadgroupMemoryOffset"Q"hasLodClamp"B"lodMinClamp"f"lodMaxClamp"f}] _currentThreadgroupMemoryLengths;
{?="width"Q"height"Q"depth"Q} _currentImageBlockSize;
@"<MTLComputePipelineState>" _currentComputePipelineState;
{set<unsigned int, std::less<unsigned int>, std::allocator<unsigned int>>="__tree_"{__tree<unsigned int, std::less<unsigned int>, std::allocator<unsigned int>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _currentSubstreamProgressLabels;
Q _currentVirtualSubstreamIndex;
B _currentVirtualSubstreamHasEncodedDispatch;
{stack<MTL4DebugCommandBufferJumpScope, std::deque<MTL4DebugCommandBufferJumpScope>>="c"{deque<MTL4DebugCommandBufferJumpScope, std::allocator<MTL4DebugCommandBufferJumpScope>>="__map_"{__split_buffer<MTL4DebugCommandBufferJumpScope *, std::allocator<MTL4DebugCommandBufferJumpScope *>>="__first_"^^i"__begin_"^^i"__end_"^^i""{?="__cap_"^^i}}"__start_"Q""{?="__size_"Q}}} _commandBufferJumpScopes;
```

## Instance methods

```
-[MTL4DebugComputeCommandEncoder executeCommandsInBuffer:withRange:];
-[MTL4DebugComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:];
-[MTL4DebugComputeCommandEncoder endEncoding];
-[MTL4DebugComputeCommandEncoder copyFromTexture:toTexture:];
-[MTL4DebugComputeCommandEncoder dealloc];
-[MTL4DebugComputeCommandEncoder setThreadgroupMemoryLength:atIndex:];
-[MTL4DebugComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:];
-[MTL4DebugComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:];
-[MTL4DebugComputeCommandEncoder optimizeContentsForCPUAccess:slice:level:];
-[MTL4DebugComputeCommandEncoder optimizeIndirectCommandBuffer:withRange:];
-[MTL4DebugComputeCommandEncoder setComputePipelineState:];
-[MTL4DebugComputeCommandEncoder fillTexture:level:slice:region:color:];
-[MTL4DebugComputeCommandEncoder setImageblockWidth:height:];
-[MTL4DebugComputeCommandEncoder optimizeContentsForGPUAccess:];
-[MTL4DebugComputeCommandEncoder fillBuffer:range:pattern4:];
-[MTL4DebugComputeCommandEncoder commandBuffer];
-[MTL4DebugComputeCommandEncoder fillTexture:level:slice:region:bytes:length:];
-[MTL4DebugComputeCommandEncoder fillTexture:level:slice:region:color:pixelFormat:];
-[MTL4DebugComputeCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:];
-[MTL4DebugComputeCommandEncoder resetCommandsInBuffer:withRange:];
-[MTL4DebugComputeCommandEncoder optimizeContentsForCPUAccess:];
-[MTL4DebugComputeCommandEncoder optimizeContentsForGPUAccess:slice:level:];
-[MTL4DebugComputeCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:];
-[MTL4DebugComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTL4DebugComputeCommandEncoder generateMipmapsForTexture:];
-[MTL4DebugComputeCommandEncoder setArgumentTable:];
-[MTL4DebugComputeCommandEncoder updateFence:afterEncoderStages:];
-[MTL4DebugComputeCommandEncoder encodeStartElse];
-[MTL4DebugComputeCommandEncoder setThreadgroupDistributionMode:];
-[MTL4DebugComputeCommandEncoder signalProgress:];
-[MTL4DebugComputeCommandEncoder barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:];
-[MTL4DebugComputeCommandEncoder barrierAfterQueueStages:beforeStages:visibilityOptions:];
-[MTL4DebugComputeCommandEncoder barrierAfterStages:beforeQueueStages:visibilityOptions:];
-[MTL4DebugComputeCommandEncoder beginVirtualSubstream];
-[MTL4DebugComputeCommandEncoder buildAccelerationStructure:descriptor:scratchBuffer:];
-[MTL4DebugComputeCommandEncoder copyAccelerationStructure:toAccelerationStructure:];
-[MTL4DebugComputeCommandEncoder copyAndCompactAccelerationStructure:toAccelerationStructure:];
-[MTL4DebugComputeCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTL4DebugComputeCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[MTL4DebugComputeCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:sourcePlane:toTensor:destinationOrigin:destinationDimensions:destinationPlane:];
-[MTL4DebugComputeCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:];
-[MTL4DebugComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:];
-[MTL4DebugComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:];
-[MTL4DebugComputeCommandEncoder deserializeInstanceAccelerationStructure:referencedAccelerationStructures:fromBuffer:];
-[MTL4DebugComputeCommandEncoder deserializePrimitiveAccelerationStructure:fromBuffer:];
-[MTL4DebugComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:threadsPerThreadgroup:];
-[MTL4DebugComputeCommandEncoder dispatchThreadsWithIndirectBuffer:];
-[MTL4DebugComputeCommandEncoder enableNullBufferBinds:];
-[MTL4DebugComputeCommandEncoder encodeEndDoWhile:comparison:referenceValue:];
-[MTL4DebugComputeCommandEncoder encodeEndDoWhile:offset:comparison:referenceValue:];
-[MTL4DebugComputeCommandEncoder encodeEndIf];
-[MTL4DebugComputeCommandEncoder encodeEndWhile];
-[MTL4DebugComputeCommandEncoder encodeStartDoWhile];
-[MTL4DebugComputeCommandEncoder encodeStartIf:comparison:referenceValue:];
-[MTL4DebugComputeCommandEncoder encodeStartIf:offset:comparison:referenceValue:];
-[MTL4DebugComputeCommandEncoder encodeStartWhile:comparison:referenceValue:];
-[MTL4DebugComputeCommandEncoder encodeStartWhile:offset:comparison:referenceValue:];
-[MTL4DebugComputeCommandEncoder endVirtualSubstream];
-[MTL4DebugComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:];
-[MTL4DebugComputeCommandEncoder fillBuffer:range:value:];
-[MTL4DebugComputeCommandEncoder insertCompressedTextureReinterpretationFlush];
-[MTL4DebugComputeCommandEncoder invalidateCompressedTexture:];
-[MTL4DebugComputeCommandEncoder invalidateCompressedTexture:slice:level:];
-[MTL4DebugComputeCommandEncoder nextVirtualSubstream];
-[MTL4DebugComputeCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:];
-[MTL4DebugComputeCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:options:];
-[MTL4DebugComputeCommandEncoder serializeInstanceAccelerationStructure:referencedAccelerationStructures:toBuffer:];
-[MTL4DebugComputeCommandEncoder serializePrimitiveAccelerationStructure:toBuffer:];
-[MTL4DebugComputeCommandEncoder setSubstream:];
-[MTL4DebugComputeCommandEncoder setThreadgroupDistributionModeWithClusterGroupIndex:];
-[MTL4DebugComputeCommandEncoder waitForFence:beforeEncoderStages:];
-[MTL4DebugComputeCommandEncoder waitForProgress:];
-[MTL4DebugComputeCommandEncoder waitForVirtualSubstream:];
-[MTL4DebugComputeCommandEncoder writeAccelerationStructureSerializationData:toBuffer:];
-[MTL4DebugComputeCommandEncoder writeAccelerationStructureTraversalDepth:toBuffer:];
-[MTL4DebugComputeCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:];
-[MTL4DebugComputeCommandEncoder writeDeserializedAccelerationStructureSize:toBuffer:];
-[MTL4DebugComputeCommandEncoder writeGenericBVHStructureOfAccelerationStructure:into:];
-[MTL4DebugComputeCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:into:];
-[MTL4DebugComputeCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:];
-[MTL4DebugComputeCommandEncoder writeSerializedAccelerationStructureSize:toBuffer:];
-[MTL4DebugComputeCommandEncoder writeTimestampWithGranularity:intoHeap:atIndex:];
-[MTL4DebugComputeCommandEncoder _resetEncoder];
-[MTL4DebugComputeCommandEncoder _updateEncoderStateAfterDispatch];
-[MTL4DebugComputeCommandEncoder _validateComputeFunctionArguments:];
-[MTL4DebugComputeCommandEncoder _validateComputeFunctionBuiltinArguments:threadsPerThreadgroup:threadgroupsPerGrid:];
-[MTL4DebugComputeCommandEncoder _validateCopyFromBufferToTextureCommon:sourceBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:destinationTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[MTL4DebugComputeCommandEncoder _validateCopyFromTextureToBufferCommon:sourceTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:destinationBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:];
-[MTL4DebugComputeCommandEncoder _validateCopyFromTextureToTextureCommon:sourceTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:destinationTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTL4DebugComputeCommandEncoder _validateFillTextureCommon:texture:level:slice:region:];
-[MTL4DebugComputeCommandEncoder _validateThreadsPerThreadgroupCommon:threadsPerThreadgroup:];
-[MTL4DebugComputeCommandEncoder initWithComputeCommandEncoder:commandBuffer:];
-[MTL4DebugComputeCommandEncoder initWithComputeCommandEncoder:commandBuffer:numSubstreams:];
-[MTL4DebugComputeCommandEncoder validateRefit:descriptor:destination:scratchBuffer:options:];
```
