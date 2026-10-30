# `MTLToolsIndirectComputeCommand`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLIndirectComputeCommandSPI`
- 0 instance variables, 4 properties, 23 instance methods, 0 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsIndirectComputeCommand setThreadgroupMemoryLength:atIndex:];
-[MTLToolsIndirectComputeCommand reset];
-[MTLToolsIndirectComputeCommand setStageInRegion:];
-[MTLToolsIndirectComputeCommand setComputePipelineState:];
-[MTLToolsIndirectComputeCommand setImageblockWidth:height:];
-[MTLToolsIndirectComputeCommand setKernelBuffer:offset:atIndex:];
-[MTLToolsIndirectComputeCommand clearBarrier];
-[MTLToolsIndirectComputeCommand concurrentDispatchThreadgroups:threadsPerThreadgroup:];
-[MTLToolsIndirectComputeCommand concurrentDispatchThreads:threadsPerThreadgroup:];
-[MTLToolsIndirectComputeCommand dispatchThreadgroupsArguments];
-[MTLToolsIndirectComputeCommand dispatchThreadsArguments];
-[MTLToolsIndirectComputeCommand getCommandType];
-[MTLToolsIndirectComputeCommand getImageBlockSize];
-[MTLToolsIndirectComputeCommand getKernelAttributeStrideAtIndex:];
-[MTLToolsIndirectComputeCommand getKernelBufferAddressAtIndex:];
-[MTLToolsIndirectComputeCommand getKernelBufferAtIndex:];
-[MTLToolsIndirectComputeCommand getOptimizedStatus];
-[MTLToolsIndirectComputeCommand getPipelineStateUniqueIdentifier];
-[MTLToolsIndirectComputeCommand getStageInRegion];
-[MTLToolsIndirectComputeCommand getThreadgroupMemoryLengthAtIndex:];
-[MTLToolsIndirectComputeCommand hasBarrier];
-[MTLToolsIndirectComputeCommand setBarrier];
-[MTLToolsIndirectComputeCommand setKernelBuffer:offset:attributeStride:atIndex:];
```
