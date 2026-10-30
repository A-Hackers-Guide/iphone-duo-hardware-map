# `_MTLCommandBuffer`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- 65 instance variables, 25 properties, 106 instance methods, 1 class methods

## Instance variables

```
@"<MTLCommandEncoder>" _currentCommandEncoder;
@"_MTLCommandQueue<MTLCommandQueue>" _queue;
^{MTLDispatch=^{MTLDispatch}@?} _scheduledDispatchList;
^{MTLDispatch=^{MTLDispatch}@?} _scheduledDispatchListTail;
^{MTLDispatch=^{MTLDispatch}@?} _completedDispatchList;
^{MTLDispatch=^{MTLDispatch}@?} _completedDispatchListTail;
^{MTLSyncDispatch=^{MTLSyncDispatch}@?} _syncDispatchList;
^{MTLSyncDispatch=^{MTLSyncDispatch}@?} _syncDispatchListTail;
{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]} _mutex;
{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]} _completedCond;
{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]} _scheduledCond;
Q _creationTime;
Q _enqueueTime;
Q _commitTime;
Q _submitToKernelTime;
Q _submitToHardwareTime;
Q _completionInterruptTime;
Q _completionHandlerEnqueueTime;
Q _completionHandlerExecutionTime;
Q _status;
@"NSError" _error;
B _skipRender;
B _profilingEnabled;
B _scheduledCallbacksDone;
B _completedCallbacksDone;
B _strongObjectReferences;
@"NSDictionary" _profilingResults;
B _retainedReferences;
B _synchronousDebugMode;
@"NSMutableDictionary" _userDictionary;
Q _kernelStartTime;
Q _kernelEndTime;
Q _gpuStartTime;
Q _gpuEndTime;
Q _numEncoders;
Q _numThisCommandBuffer;
Q _listIndex;
B _ownedByParallelEncoder;
B _wakeOnCommit;
@"NSMutableArray" _retainedObjects;
B _needsCommandBufferSemaphoreSignal;
Q _globalTraceObjectID;
@"<MTLBuffer>" _privateData;
Q _privateDataOffset;
@"<MTLBuffer>" _privateLoggingBuffer;
@"<MTLLogState>" _logState;
Q _labelTraceID;
B _StatEnabled;
@? _perfSampleHandlerBlock;
B _hasPresent;
@"<MTLBuffer>" _progressBuffer;
I _progressOffset;
B _creatingProgressEncoder;
B _needsFrameworkAssistedErrorTracking;
@"NSMutableArray" _encoderInfos;
@"<MTLDeadlineProfile>" _deadlineProfile;
@"NSArray" _logs;
Q _numPresentWaits;
B _requiresBindingLogState;
B _didComplete;
^{MTLDispatch=^{MTLDispatch}@?} _swiftConcurrencyScheduledWaiters;
^{MTLDispatch=^{MTLDispatch}@?} _swiftConcurrencyScheduledWaitersTail;
^{MTLDispatch=^{MTLDispatch}@?} _swiftConcurrencyCompletedWaiters;
^{MTLDispatch=^{MTLDispatch}@?} _swiftConcurrencyCompletedWaitersTail;
Q _errorOptions;
```

## Properties

```
@property (TB,R,V_retainedReferences) retainedReferences;
@property (TB,R,V_synchronousDebugMode) synchronousDebugMode;
@property (T@"<MTLCommandQueue>",R,V_queue) commandQueue;
@property (TQ,R,V_status) status;
@property (T@"NSString",C,D) label;
@property (T@"NSError",R) error;
@property (TB,GisProfilingEnabled) profilingEnabled;
@property (T@"NSDictionary",R) profilingResults;
@property (TQ,R,V_globalTraceObjectID) globalTraceObjectID;
@property (T@"<MTLBuffer>",&,N,V_privateData) privateData;
@property (TQ,N,V_privateDataOffset) privateDataOffset;
@property (T@"<MTLBuffer>",N,V_privateLoggingBuffer) privateLoggingBuffer;
@property (T@"NSArray",&,N) logs;
@property (Td,R,N) kernelStartTime;
@property (Td,R,N) kernelEndTime;
@property (Td,R,N) GPUStartTime;
@property (Td,R,N) GPUEndTime;
@property (T@"NSMutableDictionary",R,N) userDictionary;
@property (TB,N,GisStatEnabled,V_StatEnabled) StatEnabled;
@property (TQ,N,V_numThisCommandBuffer) numThisCommandBuffer;
@property (TQ,N,V_numEncoders) numEncoders;
@property (TQ,R,N,GgetListIndex,V_listIndex) listIndex;
@property (TB,N,V_ownedByParallelEncoder) ownedByParallelEncoder;
@property (T@"<MTLDeadlineProfile>",R,&,V_deadlineProfile) deadlineProfile;
@property (TQ,N,V_errorOptions) errorOptions;
```

## Class methods

```
+[_MTLCommandBuffer initialize];
```

## Instance methods

```
-[_MTLCommandBuffer presentDrawable:options:];
-[_MTLCommandBuffer commitWithDeadline:];
-[_MTLCommandBuffer encodeSignalEvent:value:agentMask:];
-[_MTLCommandBuffer commitAndHold];
-[_MTLCommandBuffer numThisCommandBuffer];
-[_MTLCommandBuffer setErrorOptions:];
-[_MTLCommandBuffer setPrivateDataOffset:];
-[_MTLCommandBuffer didScheduleWithStartTime:endTime:error:];
-[_MTLCommandBuffer ownedByParallelEncoder];
-[_MTLCommandBuffer useInternalResidencySet:];
-[_MTLCommandBuffer processEncoderInfos];
-[_MTLCommandBuffer addSynchronizationNotification:];
-[_MTLCommandBuffer setOwnedByParallelEncoder:];
-[_MTLCommandBuffer GPUEndTime];
-[_MTLCommandBuffer privateLoggingBuffer];
-[_MTLCommandBuffer presentDrawable:afterMinimumDuration:];
-[_MTLCommandBuffer encodeDashboardFinalizeForResourceGroup:dashboard:values:indices:count:];
-[_MTLCommandBuffer runPerfCounterCallbackWithBlock:];
-[_MTLCommandBuffer addCompletedHandler:];
-[_MTLCommandBuffer encodeDashboardTagForResourceGroup:];
-[_MTLCommandBuffer debugBufferContentsWithLength:];
-[_MTLCommandBuffer waitUntilScheduled];
-[_MTLCommandBuffer errorOptions];
-[_MTLCommandBuffer setCurrentCommandEncoder:];
-[_MTLCommandBuffer initWithQueue:retainedReferences:];
-[_MTLCommandBuffer deadlineProfile];
-[_MTLCommandBuffer blitCommandEncoderWithDescriptor:];
-[_MTLCommandBuffer executeSynchronizationNotifications:scope:resources:count:];
-[_MTLCommandBuffer waitUntilCompleted];
-[_MTLCommandBuffer pushDebugGroup:];
-[_MTLCommandBuffer progressTrackingRenderCommandEncoder];
-[_MTLCommandBuffer setNumEncoders:];
-[_MTLCommandBuffer kernelSubmitTime];
-[_MTLCommandBuffer configWithCommandBufferDescriptor:];
-[_MTLCommandBuffer sampledAccelerationStructureCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[_MTLCommandBuffer bindLogState];
-[_MTLCommandBuffer setLogs:];
-[_MTLCommandBuffer getDriverEncoderInfoData:];
-[_MTLCommandBuffer progressTrackingComputeCommandEncoder];
-[_MTLCommandBuffer encodeDashboardFinalizeForResourceGroup:dashboard:value:forIndex:];
-[_MTLCommandBuffer sampledRenderCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[_MTLCommandBuffer setPrivateData:];
-[_MTLCommandBuffer setCommitted:];
-[_MTLCommandBuffer __waitUntilCompletedAsync:];
-[_MTLCommandBuffer useResidencySet:];
-[_MTLCommandBuffer getAndIncrementNumEncoders];
-[_MTLCommandBuffer addScheduledHandler:];
-[_MTLCommandBuffer privateData];
-[_MTLCommandBuffer computeCommandEncoderWithDispatchType:];
-[_MTLCommandBuffer _addRetainedObject:];
-[_MTLCommandBuffer resourceStateCommandEncoderWithDescriptor:];
-[_MTLCommandBuffer setNumThisCommandBuffer:];
-[_MTLCommandBuffer sampledComputeCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[_MTLCommandBuffer setResponsibleTaskIDs:count:];
-[_MTLCommandBuffer enqueue];
-[_MTLCommandBuffer kernelStartTime];
-[_MTLCommandBuffer commit];
-[_MTLCommandBuffer presentDrawable:];
-[_MTLCommandBuffer retainedReferences];
-[_MTLCommandBuffer commitAndWaitUntilSubmittedWithDeadline:];
-[_MTLCommandBuffer __waitUntilScheduledAsync:];
-[_MTLCommandBuffer computeCommandEncoderWithDescriptor:];
-[_MTLCommandBuffer privateDataOffset];
-[_MTLCommandBuffer synchronousDebugMode];
-[_MTLCommandBuffer useResidencySets:count:];
-[_MTLCommandBuffer initProgressTracking];
-[_MTLCommandBuffer isProfilingEnabled];
-[_MTLCommandBuffer commitAndReset];
-[_MTLCommandBuffer logs];
-[_MTLCommandBuffer sampledBlitCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[_MTLCommandBuffer signalCommandBufferAvailable];
-[_MTLCommandBuffer isCommitted];
-[_MTLCommandBuffer userDictionary];
-[_MTLCommandBuffer sampledBlitCommandEncoder:capacity:];
-[_MTLCommandBuffer sampledComputeCommandEncoderWithProgramInfoBuffer:capacity:];
-[_MTLCommandBuffer executeSynchronizationNotifications:];
-[_MTLCommandBuffer sampledAccelerationStructureCommandEncoder:capacity:];
-[_MTLCommandBuffer sampledComputeCommandEncoderWithDispatchType:programInfoBuffer:capacity:];
-[_MTLCommandBuffer presentDrawable:atTime:];
-[_MTLCommandBuffer popDebugGroup];
-[_MTLCommandBuffer commitAndWaitUntilSubmitted];
-[_MTLCommandBuffer GPUStartTime];
-[_MTLCommandBuffer profilingResults];
-[_MTLCommandBuffer accelerationStructureCommandEncoderWithDescriptor:];
-[_MTLCommandBuffer setProfilingEnabled:];
-[_MTLCommandBuffer numEncoders];
-[_MTLCommandBuffer kernelEndTime];
-[_MTLCommandBuffer setPrivateLoggingBuffer:];
-[_MTLCommandBuffer didCompleteWithStartTime:endTime:error:];
-[_MTLCommandBuffer didSchedule:error:];
-[_MTLCommandBuffer accelerationStructureCommandEncoder];
-[_MTLCommandBuffer progressTrackingBlitCommandEncoder];
-[_MTLCommandBuffer encodeConditionalAbortEvent:];
-[_MTLCommandBuffer initWithQueue:retainedReferences:synchronousDebugMode:];
-[_MTLCommandBuffer useInternalResidencySets:count:];
-[_MTLCommandBuffer formattedDescription:];
-[_MTLCommandBuffer isStatEnabled];
-[_MTLCommandBuffer skipRender];
-[_MTLCommandBuffer getListIndex];
-[_MTLCommandBuffer globalTraceObjectID];
-[_MTLCommandBuffer dealloc];
-[_MTLCommandBuffer setStatEnabled:];
-[_MTLCommandBuffer status];
-[_MTLCommandBuffer error];
-[_MTLCommandBuffer commandQueue];
-[_MTLCommandBuffer description];
```
