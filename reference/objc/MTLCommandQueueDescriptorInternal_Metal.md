# `MTLCommandQueueDescriptorInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLCommandQueueDescriptor`
- 15 instance variables, 13 properties, 35 instance methods, 0 class methods

## Instance variables

```
Q _maxCommandBufferCount;
Q _qosLevel;
@"NSObject<OS_dispatch_queue>" _commitQueue;
B _commitSynchronously;
@"NSObject<OS_dispatch_queue>" _completionQueue;
B _disableCrossQueueHazardTracking;
B _disableAsyncCompletionDispatch;
B _openGLQueue;
Q _devicePartition;
B _disableIOFencing;
B _enableLowLatencySignalSharedEvent;
B _enableLowLatencyWaitSharedEvent;
B _lockParameterBufferSizeToMax;
@"<MTLLogState>" _logState;
B _commitsWithQoS;
```

## Properties

```
@property (TQ,N,V_qosLevel) qosLevel;
@property (T@"NSObject<OS_dispatch_queue>",N,V_commitQueue) commitQueue;
@property (TB,N,V_commitSynchronously) commitSynchronously;
@property (T@"NSObject<OS_dispatch_queue>",N,V_completionQueue) completionQueue;
@property (TB,N,V_disableCrossQueueHazardTracking) disableCrossQueueHazardTracking;
@property (TB,N,V_disableAsyncCompletionDispatch) disableAsyncCompletionDispatch;
@property (TQ,N,V_devicePartition) devicePartition;
@property (TB,V_openGLQueue) isOpenGLQueue;
@property (TB,N,V_disableIOFencing) disableIOFencing;
@property (TB,N,V_enableLowLatencySignalSharedEvent) enableLowLatencySignalSharedEvent;
@property (TB,N,V_enableLowLatencyWaitSharedEvent) enableLowLatencyWaitSharedEvent;
@property (TB,N,V_lockParameterBufferSizeToMax) lockParameterBufferSizeToMax;
@property (TB,N,V_commitsWithQoS) commitsWithQoS;
```

## Instance methods

```
-[MTLCommandQueueDescriptorInternal qosLevel];
-[MTLCommandQueueDescriptorInternal setEnableLowLatencySignalSharedEvent:];
-[MTLCommandQueueDescriptorInternal isOpenGLQueue];
-[MTLCommandQueueDescriptorInternal commitSynchronously];
-[MTLCommandQueueDescriptorInternal formattedDescription:];
-[MTLCommandQueueDescriptorInternal completionQueue];
-[MTLCommandQueueDescriptorInternal commitsWithQoS];
-[MTLCommandQueueDescriptorInternal init];
-[MTLCommandQueueDescriptorInternal disableCrossQueueHazardTracking];
-[MTLCommandQueueDescriptorInternal setDisableAsyncCompletionDispatch:];
-[MTLCommandQueueDescriptorInternal commitQueue];
-[MTLCommandQueueDescriptorInternal dealloc];
-[MTLCommandQueueDescriptorInternal maxCommandBufferCount];
-[MTLCommandQueueDescriptorInternal lockParameterBufferSizeToMax];
-[MTLCommandQueueDescriptorInternal setCommitQueue:];
-[MTLCommandQueueDescriptorInternal setLockParameterBufferSizeToMax:];
-[MTLCommandQueueDescriptorInternal enableLowLatencySignalSharedEvent];
-[MTLCommandQueueDescriptorInternal devicePartition];
-[MTLCommandQueueDescriptorInternal setEnableLowLatencyWaitSharedEvent:];
-[MTLCommandQueueDescriptorInternal setMaxCommandBufferCount:];
-[MTLCommandQueueDescriptorInternal disableAsyncCompletionDispatch];
-[MTLCommandQueueDescriptorInternal setCompletionQueue:];
-[MTLCommandQueueDescriptorInternal description];
-[MTLCommandQueueDescriptorInternal setCommitSynchronously:];
-[MTLCommandQueueDescriptorInternal setQosLevel:];
-[MTLCommandQueueDescriptorInternal disableIOFencing];
-[MTLCommandQueueDescriptorInternal setDisableIOFencing:];
-[MTLCommandQueueDescriptorInternal enableLowLatencyWaitSharedEvent];
-[MTLCommandQueueDescriptorInternal setIsOpenGLQueue:];
-[MTLCommandQueueDescriptorInternal setDevicePartition:];
-[MTLCommandQueueDescriptorInternal setDisableCrossQueueHazardTracking:];
-[MTLCommandQueueDescriptorInternal copyWithZone:];
-[MTLCommandQueueDescriptorInternal setLogState:];
-[MTLCommandQueueDescriptorInternal setCommitsWithQoS:];
-[MTLCommandQueueDescriptorInternal logState];
```
