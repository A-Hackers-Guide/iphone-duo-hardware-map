# `MTL3On4ComputeCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MTL3On4.framework/MTL3On4`](../userland/System__Library__PrivateFrameworks__MTL3On4.framework__MTL3On4.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL3On4CommandEncoder`
- Protocols: `MTLComputeCommandEncoderSPI`
- 3 instance variables, 7 properties, 60 instance methods, 0 class methods

## Instance variables

```
@"<MTL4ArgumentTable>" _argumentTable;
[31@"<MTLBuffer>"] _bufferBindings;
Q _dispatchType;
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
-[MTL3On4ComputeCommandEncoder waitForFence:];
-[MTL3On4ComputeCommandEncoder useResources:count:usage:];
-[MTL3On4ComputeCommandEncoder setBuffers:offsets:withRange:];
-[MTL3On4ComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:];
-[MTL3On4ComputeCommandEncoder useResource:usage:];
-[MTL3On4ComputeCommandEncoder setVisibleFunctionTables:withBufferRange:];
-[MTL3On4ComputeCommandEncoder setBuffer:offset:atIndex:];
-[MTL3On4ComputeCommandEncoder updateFence:];
-[MTL3On4ComputeCommandEncoder setAccelerationStructure:atBufferIndex:];
-[MTL3On4ComputeCommandEncoder executeCommandsInBuffer:withRange:];
-[MTL3On4ComputeCommandEncoder useHeap:];
-[MTL3On4ComputeCommandEncoder useHeaps:count:];
-[MTL3On4ComputeCommandEncoder sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[MTL3On4ComputeCommandEncoder setIntersectionFunctionTable:atBufferIndex:];
-[MTL3On4ComputeCommandEncoder setVisibleFunctionTable:atBufferIndex:];
-[MTL3On4ComputeCommandEncoder memoryBarrierWithScope:];
-[MTL3On4ComputeCommandEncoder useResidencySet:];
-[MTL3On4ComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:];
-[MTL3On4ComputeCommandEncoder useResidencySets:count:];
-[MTL3On4ComputeCommandEncoder setTexture:atIndex:];
-[MTL3On4ComputeCommandEncoder setSamplerState:atIndex:];
-[MTL3On4ComputeCommandEncoder setSamplerStates:lodMinClamps:lodMaxClamps:withRange:];
-[MTL3On4ComputeCommandEncoder setBytes:length:atIndex:];
-[MTL3On4ComputeCommandEncoder dealloc];
-[MTL3On4ComputeCommandEncoder setThreadgroupMemoryLength:atIndex:];
-[MTL3On4ComputeCommandEncoder setStageInRegion:];
-[MTL3On4ComputeCommandEncoder setSamplerState:lodMinClamp:lodMaxClamp:atIndex:];
-[MTL3On4ComputeCommandEncoder setStageInRegionWithIndirectBuffer:indirectBufferOffset:];
-[MTL3On4ComputeCommandEncoder setBufferOffset:atIndex:];
-[MTL3On4ComputeCommandEncoder setBuffer:offset:attributeStride:atIndex:];
-[MTL3On4ComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:];
-[MTL3On4ComputeCommandEncoder dispatchType];
-[MTL3On4ComputeCommandEncoder setSamplerStates:withRange:];
-[MTL3On4ComputeCommandEncoder setComputePipelineState:];
-[MTL3On4ComputeCommandEncoder setBuffers:offsets:attributeStrides:withRange:];
-[MTL3On4ComputeCommandEncoder setImageblockWidth:height:];
-[MTL3On4ComputeCommandEncoder setBufferOffset:attributeStride:atIndex:];
-[MTL3On4ComputeCommandEncoder setTextures:withRange:];
-[MTL3On4ComputeCommandEncoder setBytes:length:attributeStride:atIndex:];
-[MTL3On4ComputeCommandEncoder memoryBarrierWithResources:count:];
-[MTL3On4ComputeCommandEncoder setIntersectionFunctionTables:withBufferRange:];
-[MTL3On4ComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:];
-[MTL3On4ComputeCommandEncoder encodeStartElse];
-[MTL3On4ComputeCommandEncoder setThreadgroupDistributionMode:];
-[MTL3On4ComputeCommandEncoder encodeEndDoWhile:offset:comparison:referenceValue:];
-[MTL3On4ComputeCommandEncoder encodeEndIf];
-[MTL3On4ComputeCommandEncoder encodeEndWhile];
-[MTL3On4ComputeCommandEncoder encodeStartDoWhile];
-[MTL3On4ComputeCommandEncoder encodeStartIf:offset:comparison:referenceValue:];
-[MTL3On4ComputeCommandEncoder encodeStartWhile:offset:comparison:referenceValue:];
-[MTL3On4ComputeCommandEncoder setThreadgroupDistributionModeWithClusterGroupIndex:];
-[MTL3On4ComputeCommandEncoder setThreadgroupPackingDisabled:];
-[MTL3On4ComputeCommandEncoder setToolsDispatchBufferSPI:atIndex:];
-[MTL3On4ComputeCommandEncoder initWithMTL3On4CommandBuffer:commandEncoder:];
-[MTL3On4ComputeCommandEncoder newKernelDebugInfo];
-[MTL3On4ComputeCommandEncoder initWithMTL3On4CommandBuffer:commandEncoder:argumentTable:residencySet:];
-[MTL3On4ComputeCommandEncoder initWithMTL3On4CommandBuffer:commandEncoder:argumentTable:residencySet:descriptor:];
-[MTL3On4ComputeCommandEncoder initWithMTL3On4CommandBuffer:commandEncoder:argumentTable:residencySet:dispatchType:];
-[MTL3On4ComputeCommandEncoder sampleCountersInBuffer:atIndex:allowOverlap:];
-[MTL3On4ComputeCommandEncoder setTensor:atBufferIndex:];
```
