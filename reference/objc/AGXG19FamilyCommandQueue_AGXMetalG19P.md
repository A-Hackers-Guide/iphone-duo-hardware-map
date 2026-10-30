# `AGXG19FamilyCommandQueue`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalCommandQueue`
- Protocols: `MTLCommandQueueSPI`
- 4 instance variables, 21 properties, 15 instance methods, 0 class methods

## Instance variables

```
I _telemetryInternalClientMask;
{?="numFrames"i"callstack"[64^v]} _commandQueueBTInfo;
B _hasLoggedBacktraceTelemetry;
i _currentPriority;
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
-[AGXG19FamilyCommandQueue requestCounters:];
-[AGXG19FamilyCommandQueue setGPUPriority:];
-[AGXG19FamilyCommandQueue initWithDevice:descriptor:];
-[AGXG19FamilyCommandQueue commandBufferWithDescriptor:];
-[AGXG19FamilyCommandQueue setLabel:];
-[AGXG19FamilyCommandQueue availableCounters];
-[AGXG19FamilyCommandQueue dealloc];
-[AGXG19FamilyCommandQueue setStatEnabled:];
-[AGXG19FamilyCommandQueue setGPUPriority:offset:];
-[AGXG19FamilyCommandQueue commandBuffer];
-[AGXG19FamilyCommandQueue commandBufferWithUnretainedReferences];
-[AGXG19FamilyCommandQueue counterInfo];
-[AGXG19FamilyCommandQueue getRequestedCounters];
-[AGXG19FamilyCommandQueue subdivideCounterList:];
-[AGXG19FamilyCommandQueue resolveAndUpdateQueuePriority:];
```
