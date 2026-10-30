# `FigCaptureDeferredProcessingEngine`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWGraphStatusDelegate`
- 20 instance variables, 7 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _workQueue;
^{OpaqueFigSimpleMutex=} _reservationLock;
i _reservedClientPID;
@"NSString" _currentPortType;
@"BWDeferredPipelineParameters" _currentPipelineParameters;
B _currentDemosaicedRawEnabled;
B _currentDepthDataDeliveryEnabled;
@"BWStillImageSettings" _currentSettings;
@"BWGraph" _graph;
B _graphRunning;
@"BWDeferredProcessingSourceNode" _sourceNode;
@"FigCaptureDeferredProcessingJob" _job;
@"BWDeferredProcessingContainer" _prewarmedContainer;
@"NSSet" _allSensorIDStrings;
@"NSDictionary" _defaultSensorIDsByPortType;
@"BWMemoryPool" _memoryPool;
@"BWMemoryPoolFlushAssertion" _flushAssertion;
B _lastJobReusedGraph;
I _lastJobQoS;
@"NSObject<OS_dispatch_source>" _activeJobDurationTimer;
```

## Properties

```
@property (T@"FigCaptureDeferredProcessingJob",R,N) currentJob;
@property (T@"BWDeferredProcessingContainer",R,N) currentContainer;
@property (TB,R,V_lastJobReusedGraph) lastJobReusedGraph;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigCaptureDeferredProcessingEngine initialize];
+[FigCaptureDeferredProcessingEngine sharedProcessingEngine];
```

## Instance methods

```
-[FigCaptureDeferredProcessingEngine graph:didStartSourceNode:error:];
-[FigCaptureDeferredProcessingEngine init];
-[FigCaptureDeferredProcessingEngine dealloc];
-[FigCaptureDeferredProcessingEngine graphDidPrepareNodes:];
-[FigCaptureDeferredProcessingEngine graph:didFinishStartingWithError:];
-[FigCaptureDeferredProcessingEngine lastJobReusedGraph];
-[FigCaptureDeferredProcessingEngine currentContainer];
-[FigCaptureDeferredProcessingEngine currentJob];
-[FigCaptureDeferredProcessingEngine ensurePrewarmedGraphForSettings:processingSettings:applicationID:];
-[FigCaptureDeferredProcessingEngine executeJob:];
-[FigCaptureDeferredProcessingEngine immediateTermination];
-[FigCaptureDeferredProcessingEngine releasePrewarmingResources];
-[FigCaptureDeferredProcessingEngine releaseResourcesForClientPID:isPrewarmCancellation:];
```
