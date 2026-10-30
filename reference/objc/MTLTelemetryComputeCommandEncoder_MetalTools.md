# `MTLTelemetryComputeCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsComputeCommandEncoder`
- 3 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"MTLTelemetryDevice" _telemetryDevice;
@"MTLTelemetryCommandBuffer" _telemetryCommandBuffer;
I _ceDispatches;
```

## Instance methods

```
-[MTLTelemetryComputeCommandEncoder memoryBarrierWithScope:];
-[MTLTelemetryComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:];
-[MTLTelemetryComputeCommandEncoder setTexture:atIndex:];
-[MTLTelemetryComputeCommandEncoder endEncoding];
-[MTLTelemetryComputeCommandEncoder setThreadgroupMemoryLength:atIndex:];
-[MTLTelemetryComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:];
-[MTLTelemetryComputeCommandEncoder setComputePipelineState:];
-[MTLTelemetryComputeCommandEncoder setTextures:withRange:];
-[MTLTelemetryComputeCommandEncoder memoryBarrierWithResources:count:];
-[MTLTelemetryComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:];
-[MTLTelemetryComputeCommandEncoder dispatchThreadsWithIndirectBuffer:indirectBufferOffset:];
-[MTLTelemetryComputeCommandEncoder accumDispatchDistribution:threadgroupsPerGrid:threadsPerThreadgroup:threadsPerGrid:];
-[MTLTelemetryComputeCommandEncoder initWithComputeCommandEncoder:commandBuffer:descriptor:];
```
