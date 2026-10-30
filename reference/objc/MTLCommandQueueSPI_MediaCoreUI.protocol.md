# `MTLCommandQueueSPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI`](../userland/System__Library__PrivateFrameworks__MediaCoreUI.framework__MediaCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLCommandQueue`
- 0 instance variables, 15 properties, 41 instance methods, 0 class methods

## Properties

```
@property (Ti) backgroundTrackingPID;
@property (TQ,R) maxCommandBufferCount;
@property (TQ,R) qosLevel;
@property (T@"OS_dispatch_queue",R) commitQueue;
@property (TB,R) commitSynchronously;
@property (T@"OS_dispatch_queue",R) completionQueue;
@property (TB,R) disableCrossQueueHazardTracking;
@property (TB) skipRender;
@property (TB) executionEnabled;
@property (TB,R) isOpenGLQueue;
@property (TB,R) commitsWithQoS;
@property (TB,GisProfilingEnabled) profilingEnabled;
@property (TB,?,N,GisStatEnabled) StatEnabled;
@property (TQ,?,N,GgetStatOptions) StatOptions;
@property (TQ,?,N,GgetStatLocations) StatLocations;
```

## Instance methods

```
-[MTLCommandQueueSPI qosLevel];
-[MTLCommandQueueSPI setGPUPriority:];
-[MTLCommandQueueSPI setSubmissionQueue:];
-[MTLCommandQueueSPI executionEnabled];
-[MTLCommandQueueSPI isProfilingEnabled];
-[MTLCommandQueueSPI setProfilingEnabled:];
-[MTLCommandQueueSPI isOpenGLQueue];
-[MTLCommandQueueSPI commitSynchronously];
-[MTLCommandQueueSPI completionQueue];
-[MTLCommandQueueSPI commitsWithQoS];
-[MTLCommandQueueSPI finish];
-[MTLCommandQueueSPI disableCrossQueueHazardTracking];
-[MTLCommandQueueSPI skipRender];
-[MTLCommandQueueSPI backgroundTrackingPID];
-[MTLCommandQueueSPI setBackgroundGPUPriority:offset:];
-[MTLCommandQueueSPI setExecutionEnabled:];
-[MTLCommandQueueSPI setSkipRender:];
-[MTLCommandQueueSPI commitQueue];
-[MTLCommandQueueSPI maxCommandBufferCount];
-[MTLCommandQueueSPI getBackgroundGPUPriority];
-[MTLCommandQueueSPI setGPUPriority:offset:];
-[MTLCommandQueueSPI getGPUPriority];
-[MTLCommandQueueSPI setCompletionQueue:];
-[MTLCommandQueueSPI setBackgroundGPUPriority:];
-[MTLCommandQueueSPI setBackgroundTrackingPID:];
-[MTLCommandQueueSPI requestCounters:];
-[MTLCommandQueueSPI dispatchAvailableCompletionNotifications];
-[MTLCommandQueueSPI requestCounters:withIndex:];
-[MTLCommandQueueSPI setStatLocations:];
-[MTLCommandQueueSPI setStatOptions:];
-[MTLCommandQueueSPI getStatOptions];
-[MTLCommandQueueSPI getStatLocations];
-[MTLCommandQueueSPI isStatEnabled];
-[MTLCommandQueueSPI addPerfSampleHandler:];
-[MTLCommandQueueSPI availableCounters];
-[MTLCommandQueueSPI setStatEnabled:];
-[MTLCommandQueueSPI counterInfo];
-[MTLCommandQueueSPI availableCountersAndDict];
-[MTLCommandQueueSPI getRequestedCounters];
-[MTLCommandQueueSPI getSPIStats];
-[MTLCommandQueueSPI subdivideCounterList:];
```
