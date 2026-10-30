# `MTLIOAccelCommandBuffer`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLCommandBuffer`
- 8 instance variables, 4 properties, 44 instance methods, 0 class methods

## Instance variables

```
@"MTLIOAccelDevice<MTLDevice>" _device;
^{MTLIOAccelCommandBufferStorage=@^{MTLIOAccelCommandBufferStoragePool}{?=^{MTLIOAccelCommandBufferStorage}^^{MTLIOAccelCommandBufferStorage}}@***@**^{IOAccelSegmentListHeader}^{IOAccelSegmentResourceListHeader}^{IOAccelSegmentResourceDescriptorGroup}{IOAccelResourceList=[256S]^{IOAccelSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{MTLIOAccelCommandBufferResourceInfo}@^@IQ^{IOAccelSegmentListShmemHeader}^{IOAccelSegmentKernelCommmandListHeader}IIiiI^{IOAccelSegmentResourceListHeader}^{IOAccelSegmentResourceDescriptorGroup}} _storage;
^Q _submitToHardwareTimeStampPointer;
Q _protectionOptions;
^v _scheduledCallbackBlockPtr;
^v _completedCallbackBlockPtr;
@"NSObject<OS_dispatch_semaphore>" _commitAndResetSem;
@"NSMutableSet" _purgedResources;
```

## Properties

```
@property (T^{MTLIOAccelCommandBufferResourceInfo=Q^I^I^I@{IOAccelResourceInfo=^{__IOSurface}b56b8I}},R) commandBufferResourceInfo;
@property (T^{IOAccelResourceList=[256S]^{IOAccelSegmentResourceDescriptorGroup}QQIIIIIII^?^v},R) ioAccelResourceList;
@property (T@"<MTLDevice>",R,V_device) device;
@property (T^{MTLIOAccelCommandBufferStorage=@^{MTLIOAccelCommandBufferStoragePool}{?=^{MTLIOAccelCommandBufferStorage}^^{MTLIOAccelCommandBufferStorage}}@***@**^{IOAccelSegmentListHeader}^{IOAccelSegmentResourceListHeader}^{IOAccelSegmentResourceDescriptorGroup}{IOAccelResourceList=[256S]^{IOAccelSegmentResourceDescriptorGroup}QQIIIIIII^?^v}@@QQ^@^{MTLIOAccelCommandBufferResourceInfo}@^@IQ^{IOAccelSegmentListShmemHeader}^{IOAccelSegmentKernelCommmandListHeader}IIiiI^{IOAccelSegmentResourceListHeader}^{IOAccelSegmentResourceDescriptorGroup}},R,V_storage) commandBufferStorage;
```

## Instance methods

```
-[MTLIOAccelCommandBuffer validate];
-[MTLIOAccelCommandBuffer setProtectionOptions:];
-[MTLIOAccelCommandBuffer setCurrentCommandEncoder:];
-[MTLIOAccelCommandBuffer initWithQueue:retainedReferences:];
-[MTLIOAccelCommandBuffer pushDebugGroup:];
-[MTLIOAccelCommandBuffer setResponsibleTaskIDs:count:];
-[MTLIOAccelCommandBuffer commit];
-[MTLIOAccelCommandBuffer getSegmentListHeader];
-[MTLIOAccelCommandBuffer commitAndReset];
-[MTLIOAccelCommandBuffer popDebugGroup];
-[MTLIOAccelCommandBuffer didCompleteWithStartTime:endTime:error:];
-[MTLIOAccelCommandBuffer encodeConditionalAbortEvent:];
-[MTLIOAccelCommandBuffer initWithQueue:retainedReferences:synchronousDebugMode:];
-[MTLIOAccelCommandBuffer encodeSignalEvent:value:];
-[MTLIOAccelCommandBuffer protectionOptions];
-[MTLIOAccelCommandBuffer device];
-[MTLIOAccelCommandBuffer ioAccelResourceList];
-[MTLIOAccelCommandBuffer setLabel:];
-[MTLIOAccelCommandBuffer getSegmentListPointerStart:current:end:];
-[MTLIOAccelCommandBuffer commandBufferStorage];
-[MTLIOAccelCommandBuffer getCurrentKernelCommandBufferPointer:end:];
-[MTLIOAccelCommandBuffer dealloc];
-[MTLIOAccelCommandBuffer commandBufferResourceInfo];
-[MTLIOAccelCommandBuffer beginSegment:];
-[MTLIOAccelCommandBuffer _encodePurgedResources];
-[MTLIOAccelCommandBuffer kernelCommandCollectTimeStamp];
-[MTLIOAccelCommandBuffer commitEncoder];
-[MTLIOAccelCommandBuffer growKernelCommandBuffer:];
-[MTLIOAccelCommandBuffer addPurgedResource:];
-[MTLIOAccelCommandBuffer endCurrentSegment];
-[MTLIOAccelCommandBuffer akResourceList];
-[MTLIOAccelCommandBuffer allocCommandBufferResourceAtIndex:];
-[MTLIOAccelCommandBuffer encodeWaitForEvent:value:];
-[MTLIOAccelCommandBuffer setCurrentKernelCommandBufferPointer:];
-[MTLIOAccelCommandBuffer _reserveKernelCommandBufferSpace:];
-[MTLIOAccelCommandBuffer encodeWaitForEvent:value:timeout:];
-[MTLIOAccelCommandBuffer kprintfBytes:length:];
-[MTLIOAccelCommandBuffer addPurgedHeap:];
-[MTLIOAccelCommandBuffer getCurrentKernelCommandBufferStart:current:end:];
-[MTLIOAccelCommandBuffer akPrivateResourceList];
-[MTLIOAccelCommandBuffer encodeSubmitSleepMS:];
-[MTLIOAccelCommandBuffer _debugBytes:length:output_type:];
-[MTLIOAccelCommandBuffer setCurrentSegmentListPointer:];
-[MTLIOAccelCommandBuffer growSegmentList];
```
