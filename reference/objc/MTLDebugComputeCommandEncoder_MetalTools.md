# `MTLDebugComputeCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsComputeCommandEncoder`
- 23 instance variables, 1 properties, 69 instance methods, 0 class methods

## Instance variables

```
[31{MTLDebugFunctionArgument="isValid"B"hasBeenUsed"B"type"Q"object"@"baseLevel"Q"bufferLength"Q"bufferOffset"Q"bufferAttributeStride"Q"threadgroupMemoryLength"Q"threadgroupMemoryOffset"Q"hasLodClamp"B"lodMinClamp"f"lodMaxClamp"f}] _buffers;
[128{MTLDebugFunctionArgument="isValid"B"hasBeenUsed"B"type"Q"object"@"baseLevel"Q"bufferLength"Q"bufferOffset"Q"bufferAttributeStride"Q"threadgroupMemoryLength"Q"threadgroupMemoryOffset"Q"hasLodClamp"B"lodMinClamp"f"lodMaxClamp"f}] _textures;
[16{MTLDebugFunctionArgument="isValid"B"hasBeenUsed"B"type"Q"object"@"baseLevel"Q"bufferLength"Q"bufferOffset"Q"bufferAttributeStride"Q"threadgroupMemoryLength"Q"threadgroupMemoryOffset"Q"hasLodClamp"B"lodMinClamp"f"lodMaxClamp"f}] _samplers;
[31{MTLDebugFunctionArgument="isValid"B"hasBeenUsed"B"type"Q"object"@"baseLevel"Q"bufferLength"Q"bufferOffset"Q"bufferAttributeStride"Q"threadgroupMemoryLength"Q"threadgroupMemoryOffset"Q"hasLodClamp"B"lodMinClamp"f"lodMaxClamp"f}] _threadgroupMemoryLengths;
{?="width"Q"height"Q"depth"Q} _imageBlockSize;
@"MTLDebugCommandBuffer" _commandBuffer;
B canDealloc;
B canEndEncoding;
B canSetComputePipelineState;
B hasEndEncoding;
B hasSetComputePipelineState;
B hasSetStageInRegion;
{?="origin"{?="x"Q"y"Q"z"Q}"size"{?="width"Q"height"Q"depth"Q}} stageInRegion;
B hasIndirectSetStageInRegion;
B allowsNullBufferBinds;
{deque<id, std::allocator<id>>="__map_"{__split_buffer<id *, std::allocator<id *>>="__first_"^^@"__begin_"^^@"__end_"^^@""{?="__cap_"^^@}}"__start_"Q""{?="__size_"Q}} updatedFences;
I _activeSubstream;
I _numSubstreams;
{set<unsigned int, std::less<unsigned int>, std::allocator<unsigned int>>="__tree_"{__tree<unsigned int, std::less<unsigned int>, std::allocator<unsigned int>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _progressLabels;
B _encodingVirtualSubstream;
i _currentVirtualSubstreamIndex;
B _encodedVirtualSubstreamDispatch;
@"<MTLComputePipelineState>" _computePipelineState;
```

## Properties

```
@property (T@"<MTLComputePipelineState>",R,N,V_computePipelineState) computePipelineState;
```

## Instance methods

```
-[MTLDebugComputeCommandEncoder waitForFence:];
-[MTLDebugComputeCommandEncoder useResources:count:usage:];
-[MTLDebugComputeCommandEncoder setBuffers:offsets:withRange:];
-[MTLDebugComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:];
-[MTLDebugComputeCommandEncoder useResource:usage:];
-[MTLDebugComputeCommandEncoder setVisibleFunctionTables:withBufferRange:];
-[MTLDebugComputeCommandEncoder setBuffer:offset:atIndex:];
-[MTLDebugComputeCommandEncoder updateFence:];
-[MTLDebugComputeCommandEncoder setAccelerationStructure:atBufferIndex:];
-[MTLDebugComputeCommandEncoder executeCommandsInBuffer:withRange:];
-[MTLDebugComputeCommandEncoder useHeap:];
-[MTLDebugComputeCommandEncoder useHeaps:count:];
-[MTLDebugComputeCommandEncoder sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[MTLDebugComputeCommandEncoder setIntersectionFunctionTable:atBufferIndex:];
-[MTLDebugComputeCommandEncoder setVisibleFunctionTable:atBufferIndex:];
-[MTLDebugComputeCommandEncoder memoryBarrierWithScope:];
-[MTLDebugComputeCommandEncoder useResidencySet:];
-[MTLDebugComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:];
-[MTLDebugComputeCommandEncoder useResidencySets:count:];
-[MTLDebugComputeCommandEncoder formattedDescription:];
-[MTLDebugComputeCommandEncoder setTexture:atIndex:];
-[MTLDebugComputeCommandEncoder setSamplerState:atIndex:];
-[MTLDebugComputeCommandEncoder setSamplerStates:lodMinClamps:lodMaxClamps:withRange:];
-[MTLDebugComputeCommandEncoder setBytes:length:atIndex:];
-[MTLDebugComputeCommandEncoder endEncoding];
-[MTLDebugComputeCommandEncoder dealloc];
-[MTLDebugComputeCommandEncoder setThreadgroupMemoryLength:atIndex:];
-[MTLDebugComputeCommandEncoder setStageInRegion:];
-[MTLDebugComputeCommandEncoder setSamplerState:lodMinClamp:lodMaxClamp:atIndex:];
-[MTLDebugComputeCommandEncoder setStageInRegionWithIndirectBuffer:indirectBufferOffset:];
-[MTLDebugComputeCommandEncoder setBufferOffset:atIndex:];
-[MTLDebugComputeCommandEncoder setBuffer:offset:attributeStride:atIndex:];
-[MTLDebugComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:];
-[MTLDebugComputeCommandEncoder setSamplerStates:withRange:];
-[MTLDebugComputeCommandEncoder setComputePipelineState:];
-[MTLDebugComputeCommandEncoder setBuffers:offsets:attributeStrides:withRange:];
-[MTLDebugComputeCommandEncoder setImageblockWidth:height:];
-[MTLDebugComputeCommandEncoder setBufferOffset:attributeStride:atIndex:];
-[MTLDebugComputeCommandEncoder description];
-[MTLDebugComputeCommandEncoder setTextures:withRange:];
-[MTLDebugComputeCommandEncoder setBytes:length:attributeStride:atIndex:];
-[MTLDebugComputeCommandEncoder memoryBarrierWithResources:count:];
-[MTLDebugComputeCommandEncoder setIntersectionFunctionTables:withBufferRange:];
-[MTLDebugComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:];
-[MTLDebugComputeCommandEncoder signalProgress:];
-[MTLDebugComputeCommandEncoder barrierAfterQueueStages:beforeStages:];
-[MTLDebugComputeCommandEncoder beginVirtualSubstream];
-[MTLDebugComputeCommandEncoder enableNullBufferBinds:];
-[MTLDebugComputeCommandEncoder endEncodingAndRetrieveProgramAddressTable];
-[MTLDebugComputeCommandEncoder endVirtualSubstream];
-[MTLDebugComputeCommandEncoder filterCounterRangeWithFirstBatch:lastBatch:filterIndex:];
-[MTLDebugComputeCommandEncoder nextVirtualSubstream];
-[MTLDebugComputeCommandEncoder setSubstream:];
-[MTLDebugComputeCommandEncoder waitForProgress:];
-[MTLDebugComputeCommandEncoder waitForVirtualSubstream:];
-[MTLDebugComputeCommandEncoder _setDefaults];
-[MTLDebugComputeCommandEncoder dispatchThreadsWithIndirectBuffer:indirectBufferOffset:];
-[MTLDebugComputeCommandEncoder computePipelineState];
-[MTLDebugComputeCommandEncoder enumerateBuffersUsingBlock:];
-[MTLDebugComputeCommandEncoder enumerateSamplersUsingBlock:];
-[MTLDebugComputeCommandEncoder enumerateTexturesUsingBlock:];
-[MTLDebugComputeCommandEncoder _validateThreadsPerThreadgroup:];
-[MTLDebugComputeCommandEncoder _validateAllFunctionArguments];
-[MTLDebugComputeCommandEncoder endEncoding_private];
-[MTLDebugComputeCommandEncoder enumerateThreadgroupMemoryLengthsUsingBlock:];
-[MTLDebugComputeCommandEncoder initWithComputeCommandEncoder:commandBuffer:descriptor:];
-[MTLDebugComputeCommandEncoder validateComputeFunctionArgumentsCommon];
-[MTLDebugComputeCommandEncoder validateFunctionTableUseResource:selectorName:];
-[MTLDebugComputeCommandEncoder validateStageInRegion:];
```
