# `IOGPUMetal4CommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTL4CommandBuffer`
- 3 instance variables, 0 properties, 43 instance methods, 0 class methods

## Instance variables

```
^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}Q^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B} _storage;
Q _protectionOptions;
I _allocatorGeneration;
```

## Instance methods

```
-[IOGPUMetal4CommandBuffer useInternalResidencySet:];
-[IOGPUMetal4CommandBuffer setProtectionOptions:];
-[IOGPUMetal4CommandBuffer initWithDevice:];
-[IOGPUMetal4CommandBuffer useResidencySet:];
-[IOGPUMetal4CommandBuffer useResidencySets:count:];
-[IOGPUMetal4CommandBuffer encodeSignalEvent:value:];
-[IOGPUMetal4CommandBuffer useInternalResidencySets:count:];
-[IOGPUMetal4CommandBuffer getDebugBufferPointerStart:end:];
-[IOGPUMetal4CommandBuffer protectionOptions];
-[IOGPUMetal4CommandBuffer setLabel:];
-[IOGPUMetal4CommandBuffer getSegmentListPointerStart:current:end:];
-[IOGPUMetal4CommandBuffer commandBufferStorage];
-[IOGPUMetal4CommandBuffer getCurrentKernelCommandBufferPointer:end:];
-[IOGPUMetal4CommandBuffer dealloc];
-[IOGPUMetal4CommandBuffer beginSegment:];
-[IOGPUMetal4CommandBuffer ioGPUResourceList];
-[IOGPUMetal4CommandBuffer growSidebandBuffer:];
-[IOGPUMetal4CommandBuffer commitEncoder];
-[IOGPUMetal4CommandBuffer growKernelCommandBuffer:];
-[IOGPUMetal4CommandBuffer endCurrentSegment];
-[IOGPUMetal4CommandBuffer akResourceList];
-[IOGPUMetal4CommandBuffer allocCommandBufferResourceAtIndex:];
-[IOGPUMetal4CommandBuffer encodeWaitForEvent:value:];
-[IOGPUMetal4CommandBuffer setCurrentKernelCommandBufferPointer:];
-[IOGPUMetal4CommandBuffer _reserveKernelCommandBufferSpace:];
-[IOGPUMetal4CommandBuffer encodeWaitForEvent:value:timeout:];
-[IOGPUMetal4CommandBuffer getCurrentKernelCommandBufferStart:current:end:];
-[IOGPUMetal4CommandBuffer akPrivateResourceList];
-[IOGPUMetal4CommandBuffer allocDebugBuffer];
-[IOGPUMetal4CommandBuffer allocateSidebandBuffer:];
-[IOGPUMetal4CommandBuffer growDebugBuffer:];
-[IOGPUMetal4CommandBuffer setCurrentSegmentListPointer:];
-[IOGPUMetal4CommandBuffer growSegmentList];
-[IOGPUMetal4CommandBuffer beginCommandBufferWithAllocator:];
-[IOGPUMetal4CommandBuffer beginCommandBufferWithAllocator:options:];
-[IOGPUMetal4CommandBuffer copyBufferMappingsFromBuffer:toBuffer:operations:count:];
-[IOGPUMetal4CommandBuffer endCommandBuffer];
-[IOGPUMetal4CommandBuffer updateBufferMappings:heap:operations:count:];
-[IOGPUMetal4CommandBuffer resetCommandBuffer];
-[IOGPUMetal4CommandBuffer allocatorGeneration];
-[IOGPUMetal4CommandBuffer beginIOGPUCommandBufferWithAllocator:options:];
-[IOGPUMetal4CommandBuffer encodePostMappingWaitEvent:postMappingValue:timeout:];
-[IOGPUMetal4CommandBuffer fillCommandBufferArgs:];
```
