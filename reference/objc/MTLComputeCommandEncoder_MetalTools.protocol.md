# `MTLComputeCommandEncoder` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLCommandEncoder`
- 0 instance variables, 1 properties, 39 instance methods, 0 class methods

## Properties

```
@property (TQ,R) dispatchType;
```

## Instance methods

```
-[MTLComputeCommandEncoder waitForFence:];
-[MTLComputeCommandEncoder useResources:count:usage:];
-[MTLComputeCommandEncoder setBuffers:offsets:withRange:];
-[MTLComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:];
-[MTLComputeCommandEncoder useResource:usage:];
-[MTLComputeCommandEncoder setVisibleFunctionTables:withBufferRange:];
-[MTLComputeCommandEncoder setBuffer:offset:atIndex:];
-[MTLComputeCommandEncoder updateFence:];
-[MTLComputeCommandEncoder setAccelerationStructure:atBufferIndex:];
-[MTLComputeCommandEncoder executeCommandsInBuffer:withRange:];
-[MTLComputeCommandEncoder useHeap:];
-[MTLComputeCommandEncoder useHeaps:count:];
-[MTLComputeCommandEncoder sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[MTLComputeCommandEncoder setIntersectionFunctionTable:atBufferIndex:];
-[MTLComputeCommandEncoder setVisibleFunctionTable:atBufferIndex:];
-[MTLComputeCommandEncoder memoryBarrierWithScope:];
-[MTLComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:];
-[MTLComputeCommandEncoder setTexture:atIndex:];
-[MTLComputeCommandEncoder setSamplerState:atIndex:];
-[MTLComputeCommandEncoder setSamplerStates:lodMinClamps:lodMaxClamps:withRange:];
-[MTLComputeCommandEncoder setBytes:length:atIndex:];
-[MTLComputeCommandEncoder setThreadgroupMemoryLength:atIndex:];
-[MTLComputeCommandEncoder setStageInRegion:];
-[MTLComputeCommandEncoder setSamplerState:lodMinClamp:lodMaxClamp:atIndex:];
-[MTLComputeCommandEncoder setStageInRegionWithIndirectBuffer:indirectBufferOffset:];
-[MTLComputeCommandEncoder setBufferOffset:atIndex:];
-[MTLComputeCommandEncoder setBuffer:offset:attributeStride:atIndex:];
-[MTLComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:];
-[MTLComputeCommandEncoder dispatchType];
-[MTLComputeCommandEncoder setSamplerStates:withRange:];
-[MTLComputeCommandEncoder setComputePipelineState:];
-[MTLComputeCommandEncoder setBuffers:offsets:attributeStrides:withRange:];
-[MTLComputeCommandEncoder setImageblockWidth:height:];
-[MTLComputeCommandEncoder setBufferOffset:attributeStride:atIndex:];
-[MTLComputeCommandEncoder setTextures:withRange:];
-[MTLComputeCommandEncoder setBytes:length:attributeStride:atIndex:];
-[MTLComputeCommandEncoder memoryBarrierWithResources:count:];
-[MTLComputeCommandEncoder setIntersectionFunctionTables:withBufferRange:];
-[MTLComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:];
```
