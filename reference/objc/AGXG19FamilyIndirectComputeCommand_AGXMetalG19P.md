# `AGXG19FamilyIndirectComputeCommand`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalIndirectComputeCommand`
- Protocols: `MTLIndirectComputeCommandSPI`
- 2 instance variables, 4 properties, 24 instance methods, 0 class methods

## Instance variables

```
^v _encoder;
I _index;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AGXG19FamilyIndirectComputeCommand setThreadgroupMemoryLength:atIndex:];
-[AGXG19FamilyIndirectComputeCommand reset];
-[AGXG19FamilyIndirectComputeCommand setStageInRegion:];
-[AGXG19FamilyIndirectComputeCommand setComputePipelineState:];
-[AGXG19FamilyIndirectComputeCommand setImageblockWidth:height:];
-[AGXG19FamilyIndirectComputeCommand setKernelBuffer:offset:atIndex:];
-[AGXG19FamilyIndirectComputeCommand clearBarrier];
-[AGXG19FamilyIndirectComputeCommand concurrentDispatchThreadgroups:threadsPerThreadgroup:];
-[AGXG19FamilyIndirectComputeCommand concurrentDispatchThreads:threadsPerThreadgroup:];
-[AGXG19FamilyIndirectComputeCommand dispatchThreadgroupsArguments];
-[AGXG19FamilyIndirectComputeCommand dispatchThreadsArguments];
-[AGXG19FamilyIndirectComputeCommand getCommandType];
-[AGXG19FamilyIndirectComputeCommand getImageBlockSize];
-[AGXG19FamilyIndirectComputeCommand getKernelAttributeStrideAtIndex:];
-[AGXG19FamilyIndirectComputeCommand getKernelBufferAddressAtIndex:];
-[AGXG19FamilyIndirectComputeCommand getKernelBufferAtIndex:];
-[AGXG19FamilyIndirectComputeCommand getPipelineStateUniqueIdentifier];
-[AGXG19FamilyIndirectComputeCommand getStageInRegion];
-[AGXG19FamilyIndirectComputeCommand getThreadgroupMemoryLengthAtIndex:];
-[AGXG19FamilyIndirectComputeCommand hasBarrier];
-[AGXG19FamilyIndirectComputeCommand setBarrier];
-[AGXG19FamilyIndirectComputeCommand setKernelBuffer:offset:attributeStride:atIndex:];
-[AGXG19FamilyIndirectComputeCommand setToolsDispatchBufferSPI:atIndex:];
-[AGXG19FamilyIndirectComputeCommand initWithEncoder:withIndex:];
```
