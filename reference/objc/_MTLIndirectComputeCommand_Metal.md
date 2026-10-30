# `_MTLIndirectComputeCommand`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLIndirectComputeCommandSPI`
- 0 instance variables, 4 properties, 25 instance methods, 0 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLIndirectComputeCommand setThreadgroupMemoryLength:atIndex:];
-[_MTLIndirectComputeCommand reset];
-[_MTLIndirectComputeCommand setStageInRegion:];
-[_MTLIndirectComputeCommand setComputePipelineState:];
-[_MTLIndirectComputeCommand setImageblockWidth:height:];
-[_MTLIndirectComputeCommand setKernelBuffer:offset:atIndex:];
-[_MTLIndirectComputeCommand clearBarrier];
-[_MTLIndirectComputeCommand concurrentDispatchThreadgroups:threadsPerThreadgroup:];
-[_MTLIndirectComputeCommand concurrentDispatchThreads:threadsPerThreadgroup:];
-[_MTLIndirectComputeCommand dispatchThreadgroupsArguments];
-[_MTLIndirectComputeCommand dispatchThreadsArguments];
-[_MTLIndirectComputeCommand getCommandType];
-[_MTLIndirectComputeCommand getImageBlockSize];
-[_MTLIndirectComputeCommand getKernelAttributeStrideAtIndex:];
-[_MTLIndirectComputeCommand getKernelBufferAddressAtIndex:];
-[_MTLIndirectComputeCommand getKernelBufferAtIndex:];
-[_MTLIndirectComputeCommand getOptimizedStatus];
-[_MTLIndirectComputeCommand getPipelineStateUniqueIdentifier];
-[_MTLIndirectComputeCommand getStageInRegion];
-[_MTLIndirectComputeCommand getThreadgroupMemoryLengthAtIndex:];
-[_MTLIndirectComputeCommand hasBarrier];
-[_MTLIndirectComputeCommand setBarrier];
-[_MTLIndirectComputeCommand setKernelArgument:offset:atIndex:];
-[_MTLIndirectComputeCommand setKernelBuffer:offset:attributeStride:atIndex:];
-[_MTLIndirectComputeCommand setToolsDispatchBufferSPI:atIndex:];
```
