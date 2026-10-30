# `MTLCountersComputeCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsComputeCommandEncoder`
- 2 instance variables, 0 properties, 38 instance methods, 0 class methods

## Instance variables

```
B _APITimingEnabled;
@"MTLCountersTraceComputeCommandEncoder" _traceEncoder;
```

## Instance methods

```
-[MTLCountersComputeCommandEncoder waitForFence:];
-[MTLCountersComputeCommandEncoder useResources:count:usage:];
-[MTLCountersComputeCommandEncoder setBuffers:offsets:withRange:];
-[MTLCountersComputeCommandEncoder useResource:usage:];
-[MTLCountersComputeCommandEncoder setVisibleFunctionTables:withBufferRange:];
-[MTLCountersComputeCommandEncoder insertDebugSignpost:];
-[MTLCountersComputeCommandEncoder setBuffer:offset:atIndex:];
-[MTLCountersComputeCommandEncoder updateFence:];
-[MTLCountersComputeCommandEncoder useHeap:];
-[MTLCountersComputeCommandEncoder useHeaps:count:];
-[MTLCountersComputeCommandEncoder setIntersectionFunctionTable:atBufferIndex:];
-[MTLCountersComputeCommandEncoder setVisibleFunctionTable:atBufferIndex:];
-[MTLCountersComputeCommandEncoder memoryBarrierWithScope:];
-[MTLCountersComputeCommandEncoder pushDebugGroup:];
-[MTLCountersComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:];
-[MTLCountersComputeCommandEncoder popDebugGroup];
-[MTLCountersComputeCommandEncoder setTexture:atIndex:];
-[MTLCountersComputeCommandEncoder setSamplerState:atIndex:];
-[MTLCountersComputeCommandEncoder setSamplerStates:lodMinClamps:lodMaxClamps:withRange:];
-[MTLCountersComputeCommandEncoder setBytes:length:atIndex:];
-[MTLCountersComputeCommandEncoder setLabel:];
-[MTLCountersComputeCommandEncoder endEncoding];
-[MTLCountersComputeCommandEncoder dealloc];
-[MTLCountersComputeCommandEncoder setThreadgroupMemoryLength:atIndex:];
-[MTLCountersComputeCommandEncoder setStageInRegion:];
-[MTLCountersComputeCommandEncoder setSamplerState:lodMinClamp:lodMaxClamp:atIndex:];
-[MTLCountersComputeCommandEncoder setStageInRegionWithIndirectBuffer:indirectBufferOffset:];
-[MTLCountersComputeCommandEncoder setBufferOffset:atIndex:];
-[MTLCountersComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:];
-[MTLCountersComputeCommandEncoder setSamplerStates:withRange:];
-[MTLCountersComputeCommandEncoder setComputePipelineState:];
-[MTLCountersComputeCommandEncoder setTextures:withRange:];
-[MTLCountersComputeCommandEncoder memoryBarrierWithResources:count:];
-[MTLCountersComputeCommandEncoder setIntersectionFunctionTables:withBufferRange:];
-[MTLCountersComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:];
-[MTLCountersComputeCommandEncoder dispatchThreadsWithIndirectBuffer:indirectBufferOffset:];
-[MTLCountersComputeCommandEncoder setImageBlockWidth:height:];
-[MTLCountersComputeCommandEncoder initWithComputeCommandEncoder:commandBuffer:descriptor:];
```
