# `MTLGPUDebugIndirectComputeCommand`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsIndirectComputeCommand`
- 1 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance variables

```
Q _commandIndex;
```

## Instance methods

```
-[MTLGPUDebugIndirectComputeCommand dealloc];
-[MTLGPUDebugIndirectComputeCommand setThreadgroupMemoryLength:atIndex:];
-[MTLGPUDebugIndirectComputeCommand reset];
-[MTLGPUDebugIndirectComputeCommand setStageInRegion:];
-[MTLGPUDebugIndirectComputeCommand setComputePipelineState:];
-[MTLGPUDebugIndirectComputeCommand setKernelBuffer:offset:atIndex:];
-[MTLGPUDebugIndirectComputeCommand clearBarrier];
-[MTLGPUDebugIndirectComputeCommand concurrentDispatchThreadgroups:threadsPerThreadgroup:];
-[MTLGPUDebugIndirectComputeCommand concurrentDispatchThreads:threadsPerThreadgroup:];
-[MTLGPUDebugIndirectComputeCommand setBarrier];
-[MTLGPUDebugIndirectComputeCommand setKernelBuffer:offset:attributeStride:atIndex:];
-[MTLGPUDebugIndirectComputeCommand setToolsDispatchBufferSPI:atIndex:];
-[MTLGPUDebugIndirectComputeCommand initWithIndirectComputeCommand:commandIndex:indirectCommandBuffer:];
```
