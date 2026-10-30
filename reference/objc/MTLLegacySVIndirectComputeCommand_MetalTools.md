# `MTLLegacySVIndirectComputeCommand`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsIndirectComputeCommand`
- 1 instance variables, 0 properties, 12 instance methods, 0 class methods

## Instance variables

```
Q _commandIndex;
```

## Instance methods

```
-[MTLLegacySVIndirectComputeCommand dealloc];
-[MTLLegacySVIndirectComputeCommand setThreadgroupMemoryLength:atIndex:];
-[MTLLegacySVIndirectComputeCommand reset];
-[MTLLegacySVIndirectComputeCommand setStageInRegion:];
-[MTLLegacySVIndirectComputeCommand setComputePipelineState:];
-[MTLLegacySVIndirectComputeCommand setKernelBuffer:offset:atIndex:];
-[MTLLegacySVIndirectComputeCommand clearBarrier];
-[MTLLegacySVIndirectComputeCommand concurrentDispatchThreadgroups:threadsPerThreadgroup:];
-[MTLLegacySVIndirectComputeCommand concurrentDispatchThreads:threadsPerThreadgroup:];
-[MTLLegacySVIndirectComputeCommand setBarrier];
-[MTLLegacySVIndirectComputeCommand setKernelBuffer:offset:attributeStride:atIndex:];
-[MTLLegacySVIndirectComputeCommand initWithIndirectComputeCommand:commandIndex:indirectCommandBuffer:];
```
