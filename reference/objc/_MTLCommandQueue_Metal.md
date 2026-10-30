# `_MTLCommandQueue`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- 34 instance variables, 19 properties, 61 instance methods, 0 class methods

## Instance variables

```
@"_MTLDevice" _dev;
@"NSMutableArray" _pendingQueue;
@"NSMutableArray" _submittedQueue;
{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]} _pendingQueueLock;
{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]} _submittedQueueLock;
@"NSObject<OS_dispatch_group>" _submittedGroup;
@"NSObject<OS_dispatch_queue>" _commandQueueDispatch;
@"NSObject<OS_dispatch_queue>" _completionQueueDispatch;
@"NSObject<OS_dispatch_source>" _commandQueueEventSource;
@"NSObject<OS_dispatch_semaphore>" _commandBufferSemaphore;
i _backgroundTrackingPID;
Q _globalTraceObjectID;
Q _labelTraceID;
B _profilingEnabled;
@"<MTLLogState>" _logState;
B _StatEnabled;
Q _StatOptions;
Q _StatLocations;
Ai _numCommandBuffers;
@? _perfSampleHandlerBlock;
Q _listIndex;
Q _maxCommandBufferCount;
Q _qosLevel;
@"NSObject<OS_dispatch_queue>" _commitQueue;
B _commitSynchronously;
@"NSObject<OS_dispatch_queue>" _completionQueue;
B _disableCrossQueueHazardTracking;
B _executionEnabled;
B _skipRender;
B _openGLQueue;
@"NSObject<OS_dispatch_semaphore>" _presentScheduledSemaphore;
B _forceImmediateSubmissionOnCommitThread;
@"MTLPrivateDataTable" _privateDataTable;
B _commitsWithQoS;
```

## Properties

```
@property (TQ,R,V_maxCommandBufferCount) maxCommandBufferCount;
@property (TQ,R,V_qosLevel) qosLevel;
@property (T@"NSObject<OS_dispatch_queue>",R,V_commitQueue) commitQueue;
@property (TB,R,V_commitSynchronously) commitSynchronously;
@property (T@"NSObject<OS_dispatch_queue>",R,V_completionQueue) completionQueue;
@property (TB,R,V_disableCrossQueueHazardTracking) disableCrossQueueHazardTracking;
@property (TB,R,V_openGLQueue) isOpenGLQueue;
@property (TB,R,V_commitsWithQoS) commitsWithQoS;
@property (Ti,V_backgroundTrackingPID) backgroundTrackingPID;
@property (TQ,R,V_globalTraceObjectID) globalTraceObjectID;
@property (TB,V_skipRender) skipRender;
@property (TB,V_executionEnabled) executionEnabled;
@property (T@"NSString",C,D) label;
@property (TB,GisProfilingEnabled,V_profilingEnabled) profilingEnabled;
@property (TB,N,GisStatEnabled,V_StatEnabled) StatEnabled;
@property (TQ,N,GgetStatOptions,V_StatOptions) StatOptions;
@property (TQ,N,GgetStatLocations,V_StatLocations) StatLocations;
@property (TQ,D,N) numCommandBuffers;
@property (TQ,N,GgetListIndex,V_listIndex) listIndex;
```

## Instance methods

```
-[_MTLCommandQueue releasePrivateData:privateDataOffset:];
-[_MTLCommandQueue requestCounters:];
-[_MTLCommandQueue removeInternalResidencySets:count:];
-[_MTLCommandQueue dispatchAvailableCompletionNotifications];
-[_MTLCommandQueue removeResidencySet:];
-[_MTLCommandQueue qosLevel];
-[_MTLCommandQueue completeCommandBuffers:count:];
-[_MTLCommandQueue enqueueCommandBuffer:];
-[_MTLCommandQueue _submitAvailableCommandBuffers];
-[_MTLCommandQueue setSubmissionQueue:];
-[_MTLCommandQueue submitCommandBuffer:];
-[_MTLCommandQueue initWithDevice:];
-[_MTLCommandQueue insertDebugCaptureBoundary];
-[_MTLCommandQueue executionEnabled];
-[_MTLCommandQueue initWithDevice:descriptor:];
-[_MTLCommandQueue setPrivateData:privateDataOffset:logState:];
-[_MTLCommandQueue commandBufferDidComplete:startTime:completionTime:error:];
-[_MTLCommandQueue requestCounters:withIndex:];
-[_MTLCommandQueue removeInternalResidencySet:];
-[_MTLCommandQueue isProfilingEnabled];
-[_MTLCommandQueue setStatLocations:];
-[_MTLCommandQueue addInternalResidencySet:];
-[_MTLCommandQueue addInternalResidencySets:count:];
-[_MTLCommandQueue getAndIncrementNumCommandBuffers];
-[_MTLCommandQueue setProfilingEnabled:];
-[_MTLCommandQueue setStatOptions:];
-[_MTLCommandQueue isOpenGLQueue];
-[_MTLCommandQueue addResidencySets:count:];
-[_MTLCommandQueue commitSynchronously];
-[_MTLCommandQueue removeResidencySets:count:];
-[_MTLCommandQueue getPrivateDataAndOffset:privateDataOffset:];
-[_MTLCommandQueue formattedDescription:];
-[_MTLCommandQueue completionQueue];
-[_MTLCommandQueue commitsWithQoS];
-[_MTLCommandQueue initWithDevice:maxCommandBufferCount:];
-[_MTLCommandQueue getStatOptions];
-[_MTLCommandQueue getStatLocations];
-[_MTLCommandQueue isStatEnabled];
-[_MTLCommandQueue finish];
-[_MTLCommandQueue numCommandBuffers];
-[_MTLCommandQueue commandBufferWithDescriptor:];
-[_MTLCommandQueue disableCrossQueueHazardTracking];
-[_MTLCommandQueue commitCommandBuffer:wake:];
-[_MTLCommandQueue skipRender];
-[_MTLCommandQueue backgroundTrackingPID];
-[_MTLCommandQueue setLabel:];
-[_MTLCommandQueue getListIndex];
-[_MTLCommandQueue addPerfSampleHandler:];
-[_MTLCommandQueue addResidencySet:];
-[_MTLCommandQueue globalTraceObjectID];
-[_MTLCommandQueue setExecutionEnabled:];
-[_MTLCommandQueue setSkipRender:];
-[_MTLCommandQueue availableCounters];
-[_MTLCommandQueue setListIndex:];
-[_MTLCommandQueue commitQueue];
-[_MTLCommandQueue dealloc];
-[_MTLCommandQueue submitCommandBuffers:count:];
-[_MTLCommandQueue setStatEnabled:];
-[_MTLCommandQueue maxCommandBufferCount];
-[_MTLCommandQueue description];
-[_MTLCommandQueue setBackgroundTrackingPID:];
```
