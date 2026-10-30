# `MTL3On4CommandQueue`

- Image: [`/System/Library/PrivateFrameworks/MTL3On4.framework/MTL3On4`](../userland/System__Library__PrivateFrameworks__MTL3On4.framework__MTL3On4.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTLCommandQueueSPI`
- 10 instance variables, 23 properties, 61 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
@"<MTL4CommandQueue>" _commandQueue;
@"MTL3On4Context" _context;
@? _perfSampleHandlerBlock;
B _statEnabled;
Q _statOptions;
Q _statLocations;
B _profilingEnabled;
i _backgroundTrackingPID;
Q _maxCommandBufferCount;
```

## Properties

```
@property (T@"<MTL4CommandQueue>",R,N,V_commandQueue) commandQueue;
@property (T@"MTL3On4Context",R,N,V_context) context;
@property (Ti,V_backgroundTrackingPID) backgroundTrackingPID;
@property (TQ,R,V_maxCommandBufferCount) maxCommandBufferCount;
@property (TQ,R) qosLevel;
@property (T@"NSObject<OS_dispatch_queue>",R) commitQueue;
@property (TB,R) commitSynchronously;
@property (T@"NSObject<OS_dispatch_queue>",R) completionQueue;
@property (TB,R) disableCrossQueueHazardTracking;
@property (TB) skipRender;
@property (TB) executionEnabled;
@property (TB,R) isOpenGLQueue;
@property (TB,R) commitsWithQoS;
@property (TB,GisProfilingEnabled,V_profilingEnabled) profilingEnabled;
@property (TB,?,N,GisStatEnabled,V_statEnabled) StatEnabled;
@property (TQ,?,N,GgetStatOptions,V_statOptions) StatOptions;
@property (TQ,?,N,GgetStatLocations,V_statLocations) StatLocations;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R,V_device) device;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTL3On4CommandQueue requestCounters:];
-[MTL3On4CommandQueue removeInternalResidencySets:count:];
-[MTL3On4CommandQueue dispatchAvailableCompletionNotifications];
-[MTL3On4CommandQueue removeResidencySet:];
-[MTL3On4CommandQueue qosLevel];
-[MTL3On4CommandQueue setGPUPriority:];
-[MTL3On4CommandQueue setSubmissionQueue:];
-[MTL3On4CommandQueue initWithDevice:];
-[MTL3On4CommandQueue insertDebugCaptureBoundary];
-[MTL3On4CommandQueue executionEnabled];
-[MTL3On4CommandQueue requestCounters:withIndex:];
-[MTL3On4CommandQueue removeInternalResidencySet:];
-[MTL3On4CommandQueue isProfilingEnabled];
-[MTL3On4CommandQueue setStatLocations:];
-[MTL3On4CommandQueue addInternalResidencySet:];
-[MTL3On4CommandQueue addInternalResidencySets:count:];
-[MTL3On4CommandQueue setProfilingEnabled:];
-[MTL3On4CommandQueue setStatOptions:];
-[MTL3On4CommandQueue isOpenGLQueue];
-[MTL3On4CommandQueue addResidencySets:count:];
-[MTL3On4CommandQueue commitSynchronously];
-[MTL3On4CommandQueue removeResidencySets:count:];
-[MTL3On4CommandQueue completionQueue];
-[MTL3On4CommandQueue commitsWithQoS];
-[MTL3On4CommandQueue getStatOptions];
-[MTL3On4CommandQueue device];
-[MTL3On4CommandQueue getStatLocations];
-[MTL3On4CommandQueue isStatEnabled];
-[MTL3On4CommandQueue finish];
-[MTL3On4CommandQueue commandBufferWithDescriptor:];
-[MTL3On4CommandQueue disableCrossQueueHazardTracking];
-[MTL3On4CommandQueue skipRender];
-[MTL3On4CommandQueue backgroundTrackingPID];
-[MTL3On4CommandQueue addPerfSampleHandler:];
-[MTL3On4CommandQueue addResidencySet:];
-[MTL3On4CommandQueue initWithCommandQueue:];
-[MTL3On4CommandQueue setBackgroundGPUPriority:offset:];
-[MTL3On4CommandQueue setExecutionEnabled:];
-[MTL3On4CommandQueue setSkipRender:];
-[MTL3On4CommandQueue availableCounters];
-[MTL3On4CommandQueue commitQueue];
-[MTL3On4CommandQueue dealloc];
-[MTL3On4CommandQueue setStatEnabled:];
-[MTL3On4CommandQueue maxCommandBufferCount];
-[MTL3On4CommandQueue getBackgroundGPUPriority];
-[MTL3On4CommandQueue setGPUPriority:offset:];
-[MTL3On4CommandQueue commandQueue];
-[MTL3On4CommandQueue getGPUPriority];
-[MTL3On4CommandQueue commandBuffer];
-[MTL3On4CommandQueue setCompletionQueue:];
-[MTL3On4CommandQueue commandBufferWithUnretainedReferences];
-[MTL3On4CommandQueue setBackgroundGPUPriority:];
-[MTL3On4CommandQueue setBackgroundTrackingPID:];
-[MTL3On4CommandQueue context];
-[MTL3On4CommandQueue counterInfo];
-[MTL3On4CommandQueue availableCountersAndDict];
-[MTL3On4CommandQueue getRequestedCounters];
-[MTL3On4CommandQueue getSPIStats];
-[MTL3On4CommandQueue subdivideCounterList:];
-[MTL3On4CommandQueue initDummyQueueWithDevice:];
-[MTL3On4CommandQueue perfSampleHandlerBlock];
```
