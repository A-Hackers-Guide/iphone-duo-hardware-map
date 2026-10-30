# `MTLToolsComputeCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsCommandEncoder`
- Protocols: `MTLComputeCommandEncoderSPI`
- 0 instance variables, 7 properties, 65 instance methods, 0 class methods

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
-[MTLToolsComputeCommandEncoder waitForFence:];
-[MTLToolsComputeCommandEncoder useResources:count:usage:];
-[MTLToolsComputeCommandEncoder setBuffers:offsets:withRange:];
-[MTLToolsComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:];
-[MTLToolsComputeCommandEncoder useResource:usage:];
-[MTLToolsComputeCommandEncoder setVisibleFunctionTables:withBufferRange:];
-[MTLToolsComputeCommandEncoder setBuffer:offset:atIndex:];
-[MTLToolsComputeCommandEncoder updateFence:];
-[MTLToolsComputeCommandEncoder setAccelerationStructure:atBufferIndex:];
-[MTLToolsComputeCommandEncoder executeCommandsInBuffer:withRange:];
-[MTLToolsComputeCommandEncoder useHeap:];
-[MTLToolsComputeCommandEncoder useHeaps:count:];
-[MTLToolsComputeCommandEncoder sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[MTLToolsComputeCommandEncoder setIntersectionFunctionTable:atBufferIndex:];
-[MTLToolsComputeCommandEncoder setVisibleFunctionTable:atBufferIndex:];
-[MTLToolsComputeCommandEncoder memoryBarrierWithScope:];
-[MTLToolsComputeCommandEncoder useResidencySet:];
-[MTLToolsComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:];
-[MTLToolsComputeCommandEncoder useResidencySets:count:];
-[MTLToolsComputeCommandEncoder setTexture:atIndex:];
-[MTLToolsComputeCommandEncoder setSamplerState:atIndex:];
-[MTLToolsComputeCommandEncoder setSamplerStates:lodMinClamps:lodMaxClamps:withRange:];
-[MTLToolsComputeCommandEncoder setBytes:length:atIndex:];
-[MTLToolsComputeCommandEncoder setThreadgroupMemoryLength:atIndex:];
-[MTLToolsComputeCommandEncoder setStageInRegion:];
-[MTLToolsComputeCommandEncoder setSamplerState:lodMinClamp:lodMaxClamp:atIndex:];
-[MTLToolsComputeCommandEncoder setStageInRegionWithIndirectBuffer:indirectBufferOffset:];
-[MTLToolsComputeCommandEncoder setBufferOffset:atIndex:];
-[MTLToolsComputeCommandEncoder setBuffer:offset:attributeStride:atIndex:];
-[MTLToolsComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:];
-[MTLToolsComputeCommandEncoder dispatchType];
-[MTLToolsComputeCommandEncoder setSamplerStates:withRange:];
-[MTLToolsComputeCommandEncoder setComputePipelineState:];
-[MTLToolsComputeCommandEncoder setBuffers:offsets:attributeStrides:withRange:];
-[MTLToolsComputeCommandEncoder setImageblockWidth:height:];
-[MTLToolsComputeCommandEncoder setBufferOffset:attributeStride:atIndex:];
-[MTLToolsComputeCommandEncoder setTextures:withRange:];
-[MTLToolsComputeCommandEncoder setBytes:length:attributeStride:atIndex:];
-[MTLToolsComputeCommandEncoder memoryBarrierWithResources:count:];
-[MTLToolsComputeCommandEncoder setIntersectionFunctionTables:withBufferRange:];
-[MTLToolsComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:];
-[MTLToolsComputeCommandEncoder encodeStartElse];
-[MTLToolsComputeCommandEncoder setThreadgroupDistributionMode:];
-[MTLToolsComputeCommandEncoder signalProgress:];
-[MTLToolsComputeCommandEncoder enableNullBufferBinds:];
-[MTLToolsComputeCommandEncoder encodeEndDoWhile:offset:comparison:referenceValue:];
-[MTLToolsComputeCommandEncoder encodeEndIf];
-[MTLToolsComputeCommandEncoder encodeEndWhile];
-[MTLToolsComputeCommandEncoder encodeStartDoWhile];
-[MTLToolsComputeCommandEncoder encodeStartIf:offset:comparison:referenceValue:];
-[MTLToolsComputeCommandEncoder encodeStartWhile:offset:comparison:referenceValue:];
-[MTLToolsComputeCommandEncoder endEncodingAndRetrieveProgramAddressTable];
-[MTLToolsComputeCommandEncoder initWithBaseObject:parent:];
-[MTLToolsComputeCommandEncoder insertCompressedTextureReinterpretationFlush];
-[MTLToolsComputeCommandEncoder setSubstream:];
-[MTLToolsComputeCommandEncoder setThreadgroupDistributionModeWithClusterGroupIndex:];
-[MTLToolsComputeCommandEncoder setThreadgroupPackingDisabled:];
-[MTLToolsComputeCommandEncoder setToolsDispatchBufferSPI:atIndex:];
-[MTLToolsComputeCommandEncoder waitForProgress:];
-[MTLToolsComputeCommandEncoder dispatchThreadsWithIndirectBuffer:indirectBufferOffset:];
-[MTLToolsComputeCommandEncoder insertUncompressedToCompressedFlush];
-[MTLToolsComputeCommandEncoder newKernelDebugInfo];
-[MTLToolsComputeCommandEncoder setImageBlockWidth:height:];
-[MTLToolsComputeCommandEncoder useResourceGroup:usage:];
-[MTLToolsComputeCommandEncoder initWithComputeCommandEncoder:parent:descriptor:];
```
