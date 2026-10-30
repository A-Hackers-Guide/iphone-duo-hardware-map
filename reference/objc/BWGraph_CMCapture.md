# `BWGraph`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigCaptureOSStateDataProvider`
- 50 instance variables, 18 properties, 78 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _nodes;
@"NSMutableArray" _sourceNodes;
@"NSMutableArray" _sinkNodes;
@"NSMutableArray" _connections;
@"NSMutableArray" _outputsWithSharedPools;
@"NSMutableArray" _nodesToBypassUntilPrepared;
@"NSMutableDictionary" _outputsWithSharedPoolsForAttachedMedia;
@"NSMutableArray" _nodesToPrepareConcurrently;
@"NSArray" _nodesToPrepareAfterGraphStart;
@"NSMutableArray" _deferredPreparePrioritySinks;
B _deferredNodePrepareSupported;
B _deferredNodePrepareCancelled;
B _resumesConnectionsAsNodesArePrepared;
@"NSMutableArray" _deferredStartSourceNodes;
@"NSMutableArray" _deferredStartSourceNodesThatMustStartAfterNonDeferred;
B _haveStartedOrCancelledDeferredSourceNodes;
Ai _deferredPrepareState;
AQ _asyncPrepareActiveNode;
B _running;
B _beingConfigured;
@"BWGraphLiveExtension" _activeLiveExtension;
q _inflightConfigurationID;
@"NSObject<OS_dispatch_group>" _sourceNodesStartGroup;
@"NSObject<OS_dispatch_group>" _nonDeferredSourceNodesStartGroup;
@"NSObject<OS_dispatch_queue>" _sourceStartQueue;
@"NSObject<OS_dispatch_group>" _startGroup;
@"NSObject<OS_dispatch_group>" _commitGroup;
@"NSObject<OS_dispatch_group>" _sinkNodesIdleGroupForParallelGraphRebuild;
B _supportsLiveReconfiguration;
@"NSObject<OS_dispatch_queue>" _liveReconfigNodeConnectionsResumeQueue;
@"NSObject<OS_dispatch_queue>" _liveReconfigPrepareQueue;
i _errorStatus;
@"<BWGraphStatusDelegate>" _statusDelegate;
@"NSObject<OS_dispatch_group>" _statusDelegateDidFinishStartingGroup;
B _classicRetainedBufferCount;
@"BWMemoryPool" _memoryPool;
@"NSString" _clientApplicationID;
i _clientPID;
@"NSString" _userFriendlyClientName;
@"NSString" _modeDescription;
@"NSString" _sourceDescription;
i _graphStateTransitionTimeoutSeconds;
I _configurationQueuePriority;
@"BWMemoryPoolFlushAssertion" _flushAssertion;
B _memoryAnalyticsReportingEnabled;
@"BWMemoryAnalyticsPayload" _memoryAnalyticsPayload;
@"NSObject<OS_os_transaction>" _graphOSTransaction;
B _runningForContinuityCapture;
B _clientExpectsCameraMountedInLandscapeOrientation;
@"<FigCaptureInterruptionDelegate>" _interruptionDelegate;
```

## Properties

```
@property (Ti,V_errorStatus) errorStatus;
@property (TB,N,V_deferredNodePrepareSupported) deferredNodePrepareSupported;
@property (TB,R,N) deferredNodePrepareEnabled;
@property (T@"NSArray",R,N,V_deferredPreparePrioritySinks) deferredPreparePrioritySinks;
@property (TB,N,V_resumesConnectionsAsNodesArePrepared) resumesConnectionsAsNodesArePrepared;
@property (TB,R,N) supportsLiveReconfiguration;
@property (T@"<BWGraphStatusDelegate>",N,V_statusDelegate) statusDelegate;
@property (T@"<FigCaptureInterruptionDelegate>",N,V_interruptionDelegate) interruptionDelegate;
@property (T@"BWMemoryPool",&,N,V_memoryPool) memoryPool;
@property (TB,R,N,GisRunningForContinuityCapture,V_runningForContinuityCapture) runningForContinuityCapture;
@property (TB,N,V_memoryAnalyticsReportingEnabled) memoryAnalyticsReportingEnabled;
@property (T@"BWMemoryAnalyticsPayload",R,N,V_memoryAnalyticsPayload) memoryAnalyticsPayload;
@property (TB,N,V_clientExpectsCameraMountedInLandscapeOrientation) clientExpectsCameraMountedInLandscapeOrientation;
@property (Ti,N,V_graphStateTransitionTimeoutSeconds) graphStateTransitionTimeoutSeconds;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWGraph initialize];
```

## Instance methods

```
-[BWGraph start:];
-[BWGraph osStatePropertyList];
-[BWGraph modeDescription];
-[BWGraph cancelDeferredNodePrepare];
-[BWGraph setSourceDescription:];
-[BWGraph enableDeferredStartForSourceNode:mustStartAfterNonDeferred:];
-[BWGraph setErrorStatus:];
-[BWGraph memoryAnalyticsReportingEnabled];
-[BWGraph deferredPreparePrioritySinks];
-[BWGraph waitForStartOrCommitToComplete];
-[BWGraph setMemoryPool:];
-[BWGraph cancelDeferredSourceNodeStart];
-[BWGraph graphStateTransitionTimeoutSeconds];
-[BWGraph init];
-[BWGraph registerEmitSampleBufferSemaphoreFromNode:toNode:];
-[BWGraph setResumesConnectionsAsNodesArePrepared:];
-[BWGraph clientExpectsCameraMountedInLandscapeOrientation];
-[BWGraph _reverseBreadthFirstEnumerator];
-[BWGraph dotString];
-[BWGraph supportsLiveReconfiguration];
-[BWGraph addNode:error:];
-[BWGraph dealloc];
-[BWGraph nodesUnsupportedForLiveReconfiguration];
-[BWGraph removeNode:];
-[BWGraph startDeferredSourceNodesIfNeeded];
-[BWGraph _resolveFormats:];
-[BWGraph _reverseDepthFirstEnumeratorWithVertexOrdering:];
-[BWGraph _sourceNodes];
-[BWGraph setMemoryAnalyticsReportingEnabled:];
-[BWGraph deferredNodePrepareEnabled];
-[BWGraph startLiveExtensionSourceNodes:];
-[BWGraph resumesConnectionsAsNodesArePrepared];
-[BWGraph setClientApplicationID:];
-[BWGraph setGraphStateTransitionTimeoutSeconds:];
-[BWGraph setInterruptionDelegate:];
-[BWGraph memoryAnalyticsPayload];
-[BWGraph createAndBeginLiveExtension];
-[BWGraph setModeDescription:];
-[BWGraph deferredNodePrepareSupported];
-[BWGraph nodePrepareCancelled];
-[BWGraph setClientPID:];
-[BWGraph clientPID];
-[BWGraph safelyConnectOutput:toInput:pipelineStage:deferredAttach:];
-[BWGraph _depthFirstEnumeratorWithVertexOrdering:];
-[BWGraph waitForStartOrCommitToCompleteWithWillBeStoppedImmediately:];
-[BWGraph isRunningForContinuityCapture];
-[BWGraph enableBypassUntilPreparedForNode:deferredPreparePriority:];
-[BWGraph prepareLiveExtensionToBecomeLive:];
-[BWGraph enableConcurrentPrepareForNode:];
-[BWGraph initWithConfigurationQueuePriority:];
-[BWGraph _sinkNodes];
-[BWGraph cancelLiveExtension:];
-[BWGraph _breadthFirstEnumerator];
-[BWGraph sourceDescription];
-[BWGraph commitConfigurationWithID:error:];
-[BWGraph stop:];
-[BWGraph setStatusDelegate:];
-[BWGraph setDeferredNodePrepareSupported:];
-[BWGraph beginConfiguration];
-[BWGraph waitForNonDeferredSourceNodesToStart];
-[BWGraph errorStatus];
-[BWGraph notifyWhenNonDeferredSourceNodesHaveStarted:];
-[BWGraph commitLiveExtension:withError:];
-[BWGraph memoryPool];
-[BWGraph _connections];
-[BWGraph stopSources:];
-[BWGraph enableDeferredPrepareForNodesNotInPathOfSinkNode:];
-[BWGraph statusDelegate];
-[BWGraph setClientExpectsCameraMountedInLandscapeOrientation:];
-[BWGraph stopLiveExtensionSourceNodes:];
-[BWGraph startDeferredNodePrepareIfNeededWithDidPrepareCriticalPriorityNodesHandler:completionHandler:];
-[BWGraph connectOutput:toInput:pipelineStage:];
-[BWGraph userFriendlyClientName];
-[BWGraph setUserFriendlyClientName:];
-[BWGraph interruptionDelegate];
-[BWGraph safelyConnectOutput:toInput:pipelineStage:];
-[BWGraph clientApplicationID];
-[BWGraph connectOutput:toInput:pipelineStage:deferredAttach:];
```
