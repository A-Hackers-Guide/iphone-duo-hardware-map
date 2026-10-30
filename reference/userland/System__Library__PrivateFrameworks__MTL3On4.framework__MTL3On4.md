# `/System/Library/PrivateFrameworks/MTL3On4.framework/MTL3On4`

iOS 27.2 dyld shared cache image. Version `383.1.2.0.0`. **[DSC]**

## Linked libraries (9)

- `/System/Library/Frameworks/IOSurface.framework/IOSurface`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/Frameworks/Metal.framework/Metal`
- `/usr/lib/libcompression.dylib`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/usr/lib/libobjc.A.dylib`

## Objective-C: 7 classes, 11 protocols, 562 methods, 117 properties

### Class pages

Every class and protocol, with its methods: [`MTL3On4BlitCommandEncoder`](../objc/MTL3On4BlitCommandEncoder_MTL3On4.md), [`MTL3On4CommandBuffer`](../objc/MTL3On4CommandBuffer_MTL3On4.md), [`MTL3On4CommandEncoder`](../objc/MTL3On4CommandEncoder_MTL3On4.md), [`MTL3On4CommandQueue`](../objc/MTL3On4CommandQueue_MTL3On4.md), [`MTL3On4ComputeCommandEncoder`](../objc/MTL3On4ComputeCommandEncoder_MTL3On4.md), [`MTL3On4Context`](../objc/MTL3On4Context_MTL3On4.md), [`MTL3On4GlobalCommandBufferManager`](../objc/MTL3On4GlobalCommandBufferManager_MTL3On4.md), [`MTLBlitCommandEncoder`](../objc/MTLBlitCommandEncoder_MTL3On4.protocol.md), [`MTLBlitCommandEncoderSPI`](../objc/MTLBlitCommandEncoderSPI_MTL3On4.protocol.md), [`MTLCommandBuffer`](../objc/MTLCommandBuffer_MTL3On4.protocol.md), [`MTLCommandBufferSPI`](../objc/MTLCommandBufferSPI_MTL3On4.protocol.md), [`MTLCommandEncoder`](../objc/MTLCommandEncoder_MTL3On4.protocol.md), [`MTLCommandEncoderSPI`](../objc/MTLCommandEncoderSPI_MTL3On4.protocol.md), [`MTLCommandQueue`](../objc/MTLCommandQueue_MTL3On4.protocol.md), [`MTLCommandQueueSPI`](../objc/MTLCommandQueueSPI_MTL3On4.protocol.md), [`MTLComputeCommandEncoder`](../objc/MTLComputeCommandEncoder_MTL3On4.protocol.md), [`MTLComputeCommandEncoderSPI`](../objc/MTLComputeCommandEncoderSPI_MTL3On4.protocol.md), [`NSObject`](../objc/NSObject_MTL3On4.protocol.md)

### Classes

`MTL3On4BlitCommandEncoder`, `MTL3On4CommandBuffer`, `MTL3On4CommandEncoder`, `MTL3On4CommandQueue`, `MTL3On4ComputeCommandEncoder`, `MTL3On4Context`, `MTL3On4GlobalCommandBufferManager`

### Protocols

`MTLBlitCommandEncoder`, `MTLBlitCommandEncoderSPI`, `MTLCommandBuffer`, `MTLCommandBufferSPI`, `MTLCommandEncoder`, `MTLCommandEncoderSPI`, `MTLCommandQueue`, `MTLCommandQueueSPI`, `MTLComputeCommandEncoder`, `MTLComputeCommandEncoderSPI`, `NSObject`

### Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"<MTLCommandQueue>",R) commandQueue;
@property (TB,R) retainedReferences;
@property (TQ,R) errorOptions;
@property (T@"NSString",C) label;
@property (Td,R) kernelStartTime;
@property (Td,R) kernelEndTime;
@property (T@"<MTLLogContainer>",R) logs;
@property (Td,R) GPUStartTime;
@property (Td,R) GPUEndTime;
@property (TQ,R) status;
@property (T@"NSError",R) error;
@property (TQ,?,R,N,GgetListIndex) listIndex;
@property (TB,GisProfilingEnabled) profilingEnabled;
@property (T@"NSDictionary",R) profilingResults;
@property (T@"NSMutableDictionary",R,N) userDictionary;
@property (TQ,?,R) globalTraceObjectID;
@property (T@"<MTLBuffer>",?,&,N) privateData;
@property (TQ,?,N) privateDataOffset;
@property (T@"<MTLBuffer>",?,N) privateLoggingBuffer;
@property (T@"<MTLDeadlineProfile>",R,&) deadlineProfile;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
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
@property (TQ,R) dispatchType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<MTLLogContainer>",&,N,V_logs) logs;
@property (T@"MTL3On4Context",R,N,V_context) context;
@property (T@"<MTLResidencySet>",R,N,V_residencySet) residencySet;
@property (T@"<MTL4ArgumentTable>",R,N,V_computeArgumentTable) computeArgumentTable;
@property (TB,N,GisStatEnabled,V_statEnabled) StatEnabled;
@property (TQ,?,R,N,GgetListIndex) listIndex;
@property (TB,GisProfilingEnabled,V_profilingEnabled) profilingEnabled;
@property (T@"NSDictionary",R) profilingResults;
@property (T@"NSMutableDictionary",R,N,V_userDictionary) userDictionary;
@property (TQ,?,R) globalTraceObjectID;
@property (T@"<MTLBuffer>",?,&,N) privateData;
@property (TQ,?,N) privateDataOffset;
@property (T@"<MTLBuffer>",?,N) privateLoggingBuffer;
@property (T@"<MTLDeadlineProfile>",R,&) deadlineProfile;
@property (T@"<MTLDevice>",R,V_device) device;
@property (T@"<MTLCommandQueue>",R) commandQueue;
@property (TB,R,V_retainedReferences) retainedReferences;
@property (TQ,R,V_errorOptions) errorOptions;
@property (T@"NSString",C) label;
@property (Td,R,V_kernelStartTime) kernelStartTime;
@property (Td,R,V_kernelEndTime) kernelEndTime;
@property (Td,R,V_GPUStartTime) GPUStartTime;
@property (Td,R,V_GPUEndTime) GPUEndTime;
@property (TQ,R,V_status) status;
@property (T@"NSError",R,V_error) error;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"MTL3On4CommandBuffer",R,N,V_commandBuffer) commandBuffer;
@property (T@"<MTLDevice>",R,V_device) device;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
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
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) dispatchType;
```

## Strings (14)

```
MTLCommandBufferSubmitToKernelTime
MTLCommandBufferCompletionInterruptTime
MTLCommandBufferCompletionHandlerEnqueueTime
v16@?0@\"<MTL4CommitFeedback>\"8
vector
v8@?0
MTLCommandBufferEnqueueTime
MTLCommandBufferKernelScheduledTime
MTLCommandBufferSubmitToHWTime
MTLCommandBufferKernelCompleteTime
MTLCommandBufferCompletionHandlerExecutionTime
v16@?0@\"<MTLCommandBuffer>\"8
MTLCommandBufferCreationTime
MTLCommandBufferCommitTime
```
