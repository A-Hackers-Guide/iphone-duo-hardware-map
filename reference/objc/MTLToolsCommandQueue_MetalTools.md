# `MTLToolsCommandQueue`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLCommandQueueSPI`
- 6 instance variables, 21 properties, 61 instance methods, 0 class methods

## Instance variables

```
@"MTLToolsPerfCounterMailbox" _perfSampleMailbox;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _perfHandlerLock;
@? _perfSampleHandlerBlock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _residencySetsLock;
@"NSCountedSet" _residencySets;
@"NSCountedSet" _internalResidencySets;
```

## Properties

```
@property (Ti) backgroundTrackingPID;
@property (TQ,R) maxCommandBufferCount;
@property (TQ,R) qosLevel;
@property (T@"NSObject<OS_dispatch_queue>",R) commitQueue;
@property (TB,R) commitSynchronously;
@property (T@"NSObject<OS_dispatch_queue>",R) completionQueue;
@property (TB,R) disableCrossQueueHazardTracking;
@property (TB) skipRender;
@property (TB) executionEnabled;
@property (TB,R) isOpenGLQueue;
@property (TB,R) commitsWithQoS;
@property (TB,GisProfilingEnabled) profilingEnabled;
@property (TB,?,N,GisStatEnabled) StatEnabled;
@property (TQ,?,N,GgetStatOptions) StatOptions;
@property (TQ,?,N,GgetStatLocations) StatLocations;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsCommandQueue requestCounters:];
-[MTLToolsCommandQueue removeInternalResidencySets:count:];
-[MTLToolsCommandQueue dispatchAvailableCompletionNotifications];
-[MTLToolsCommandQueue removeResidencySet:];
-[MTLToolsCommandQueue qosLevel];
-[MTLToolsCommandQueue setGPUPriority:];
-[MTLToolsCommandQueue setSubmissionQueue:];
-[MTLToolsCommandQueue insertDebugCaptureBoundary];
-[MTLToolsCommandQueue executionEnabled];
-[MTLToolsCommandQueue requestCounters:withIndex:];
-[MTLToolsCommandQueue removeInternalResidencySet:];
-[MTLToolsCommandQueue isProfilingEnabled];
-[MTLToolsCommandQueue setStatLocations:];
-[MTLToolsCommandQueue addInternalResidencySet:];
-[MTLToolsCommandQueue addInternalResidencySets:count:];
-[MTLToolsCommandQueue setProfilingEnabled:];
-[MTLToolsCommandQueue setStatOptions:];
-[MTLToolsCommandQueue isOpenGLQueue];
-[MTLToolsCommandQueue addResidencySets:count:];
-[MTLToolsCommandQueue commitSynchronously];
-[MTLToolsCommandQueue removeResidencySets:count:];
-[MTLToolsCommandQueue completionQueue];
-[MTLToolsCommandQueue commitsWithQoS];
-[MTLToolsCommandQueue getStatOptions];
-[MTLToolsCommandQueue getStatLocations];
-[MTLToolsCommandQueue isStatEnabled];
-[MTLToolsCommandQueue finish];
-[MTLToolsCommandQueue label];
-[MTLToolsCommandQueue commandBufferWithDescriptor:];
-[MTLToolsCommandQueue disableCrossQueueHazardTracking];
-[MTLToolsCommandQueue skipRender];
-[MTLToolsCommandQueue backgroundTrackingPID];
-[MTLToolsCommandQueue setLabel:];
-[MTLToolsCommandQueue addPerfSampleHandler:];
-[MTLToolsCommandQueue addResidencySet:];
-[MTLToolsCommandQueue setBackgroundGPUPriority:offset:];
-[MTLToolsCommandQueue setExecutionEnabled:];
-[MTLToolsCommandQueue setSkipRender:];
-[MTLToolsCommandQueue availableCounters];
-[MTLToolsCommandQueue commitQueue];
-[MTLToolsCommandQueue dealloc];
-[MTLToolsCommandQueue setStatEnabled:];
-[MTLToolsCommandQueue maxCommandBufferCount];
-[MTLToolsCommandQueue getBackgroundGPUPriority];
-[MTLToolsCommandQueue setGPUPriority:offset:];
-[MTLToolsCommandQueue getGPUPriority];
-[MTLToolsCommandQueue commandBuffer];
-[MTLToolsCommandQueue setCompletionQueue:];
-[MTLToolsCommandQueue commandBufferWithUnretainedReferences];
-[MTLToolsCommandQueue setBackgroundGPUPriority:];
-[MTLToolsCommandQueue setBackgroundTrackingPID:];
-[MTLToolsCommandQueue initWithBaseObject:parent:];
-[MTLToolsCommandQueue counterInfo];
-[MTLToolsCommandQueue getRequestedCounters];
-[MTLToolsCommandQueue getSPIStats];
-[MTLToolsCommandQueue subdivideCounterList:];
-[MTLToolsCommandQueue internalResidencySets];
-[MTLToolsCommandQueue residencySets];
-[MTLToolsCommandQueue residencySetsArray];
-[MTLToolsCommandQueue residencySetsLock];
-[MTLToolsCommandQueue snapshotPerfSampleHandlerAndStatEnabled:forCommandBuffer:];
```
