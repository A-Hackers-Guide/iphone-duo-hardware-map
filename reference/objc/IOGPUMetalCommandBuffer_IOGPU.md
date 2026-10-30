# `IOGPUMetalCommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLCommandBuffer`
- 9 instance variables, 5 properties, 57 instance methods, 0 class methods

## Instance variables

```
@"IOGPUMetalDevice<MTLDevice>" _device;
^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}Q^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B} _storage;
^Q _submitToHardwareTimeStampPointer;
Q _protectionOptions;
^v _scheduledCallbackBlockPtr;
^v _completedCallbackBlockPtr;
@"NSObject<OS_dispatch_semaphore>" _commitAndResetSem;
@"NSMutableSet" _purgedResources;
Q _gpuFaultAddress;
```

## Properties

```
@property (T^{IOGPUMetalCommandBufferResourceInfo=Q^I^I^I@{IOGPUResourceInfo=^{__IOSurface}b56b8I}},R) commandBufferResourceInfo;
@property (T^{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v},R) ioGPUResourceList;
@property (T@"<MTLDevice>",R,V_device) device;
@property (T^{IOGPUMetalCommandBufferStorage=@^{IOGPUMetalCommandBufferStoragePool}{?=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}@***{IOGPUMetalCommandBufferSidebandBuffer=@***}@**^{IOGPUSegmentListHeader}^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{IOGPUMetalCommandBufferResourceInfo}Q^@IQ^{IOGPUSegmentListShmemHeader}^{IOGPUSegmentKernelCommmandListHeader}IIiiI^{IOGPUSegmentResourceListHeader}^{IOGPUSegmentResourceDescriptorGroup}@**^{sIOGPUKernelCommandSetResourceGroupsArgs}[2@]B},R,V_storage) commandBufferStorage;
@property (TQ,R,V_gpuFaultAddress) gpuFaultAddress;
```

## Instance methods

```
-[IOGPUMetalCommandBuffer validate];
-[IOGPUMetalCommandBuffer encodeSignalEvent:value:agentMask:];
-[IOGPUMetalCommandBuffer useInternalResidencySet:];
-[IOGPUMetalCommandBuffer setProtectionOptions:];
-[IOGPUMetalCommandBuffer setCurrentCommandEncoder:];
-[IOGPUMetalCommandBuffer initWithQueue:retainedReferences:];
-[IOGPUMetalCommandBuffer pushDebugGroup:];
-[IOGPUMetalCommandBuffer fillCommandBufferArgs:commandQueue:];
-[IOGPUMetalCommandBuffer useResidencySet:];
-[IOGPUMetalCommandBuffer setResponsibleTaskIDs:count:];
-[IOGPUMetalCommandBuffer commit];
-[IOGPUMetalCommandBuffer useResidencySets:count:];
-[IOGPUMetalCommandBuffer getSegmentListHeader];
-[IOGPUMetalCommandBuffer commitAndReset];
-[IOGPUMetalCommandBuffer popDebugGroup];
-[IOGPUMetalCommandBuffer didCompleteWithStartTime:endTime:error:];
-[IOGPUMetalCommandBuffer encodeConditionalAbortEvent:];
-[IOGPUMetalCommandBuffer initWithQueue:retainedReferences:synchronousDebugMode:];
-[IOGPUMetalCommandBuffer encodeSignalEvent:value:];
-[IOGPUMetalCommandBuffer useInternalResidencySets:count:];
-[IOGPUMetalCommandBuffer getDebugBufferPointerStart:end:];
-[IOGPUMetalCommandBuffer protectionOptions];
-[IOGPUMetalCommandBuffer device];
-[IOGPUMetalCommandBuffer setLabel:];
-[IOGPUMetalCommandBuffer getSegmentListPointerStart:current:end:];
-[IOGPUMetalCommandBuffer commandBufferStorage];
-[IOGPUMetalCommandBuffer getCurrentKernelCommandBufferPointer:end:];
-[IOGPUMetalCommandBuffer dealloc];
-[IOGPUMetalCommandBuffer commandBufferResourceInfo];
-[IOGPUMetalCommandBuffer beginSegment:];
-[IOGPUMetalCommandBuffer ioGPUResourceList];
-[IOGPUMetalCommandBuffer _encodePurgedResources];
-[IOGPUMetalCommandBuffer growSidebandBuffer:];
-[IOGPUMetalCommandBuffer kernelCommandCollectTimeStamp];
-[IOGPUMetalCommandBuffer commitEncoder];
-[IOGPUMetalCommandBuffer growKernelCommandBuffer:];
-[IOGPUMetalCommandBuffer addPurgedResource:];
-[IOGPUMetalCommandBuffer endCurrentSegment];
-[IOGPUMetalCommandBuffer akResourceList];
-[IOGPUMetalCommandBuffer allocCommandBufferResourceAtIndex:];
-[IOGPUMetalCommandBuffer encodeWaitForEvent:value:];
-[IOGPUMetalCommandBuffer setCurrentKernelCommandBufferPointer:];
-[IOGPUMetalCommandBuffer _reserveKernelCommandBufferSpace:];
-[IOGPUMetalCommandBuffer encodeWaitForEvent:value:timeout:];
-[IOGPUMetalCommandBuffer kprintfBytes:length:];
-[IOGPUMetalCommandBuffer gpuFaultAddress];
-[IOGPUMetalCommandBuffer addPurgedHeap:];
-[IOGPUMetalCommandBuffer getCurrentKernelCommandBufferStart:current:end:];
-[IOGPUMetalCommandBuffer akPrivateResourceList];
-[IOGPUMetalCommandBuffer allocDebugBuffer];
-[IOGPUMetalCommandBuffer allocateSidebandBuffer:];
-[IOGPUMetalCommandBuffer growDebugBuffer:];
-[IOGPUMetalCommandBuffer encodeSubmitSleepMS:];
-[IOGPUMetalCommandBuffer _debugBytes:length:output_type:];
-[IOGPUMetalCommandBuffer encodeSignalEventScheduled:value:];
-[IOGPUMetalCommandBuffer setCurrentSegmentListPointer:];
-[IOGPUMetalCommandBuffer growSegmentList];
```
