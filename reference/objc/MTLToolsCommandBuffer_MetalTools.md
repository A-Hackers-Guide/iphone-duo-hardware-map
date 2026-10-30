# `MTLToolsCommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLCommandBufferSPI`, `MTLToolsRetainingContainer`
- 13 instance variables, 27 properties, 109 instance methods, 1 class methods

## Instance variables

```
{?="hasCommit"b1"addedCompletedHandler"b1"addedScheduledHandler"b1"padding"b29} _flags;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _retainedObjectsLock;
B _useRetainedObjectsLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _handlerLock;
{vector<void (^)(id<MTLCommandBuffer>), std::allocator<void (^)(id<MTLCommandBuffer>)>>="__begin_"^@?"__end_"^@?""{?="__cap_"^@?}} _scheduledHandlers;
{vector<void (^)(id<MTLCommandBuffer>), std::allocator<void (^)(id<MTLCommandBuffer>)>>="__begin_"^@?"__end_"^@?""{?="__cap_"^@?}} _completedHandlers;
B _didInvokeHandlers;
@? _perfSampleHandlerBlock;
B _StatEnabled;
@"MTLToolsDeadlineProfile" _deadlineProfile;
@"NSMutableSet" _usedResidencySets;
@"NSMutableSet" _usedInternalResidencySets;
@"NSMutableSet" _retainedObjects;
```

## Properties

```
@property (TB,V_useRetainedObjectsLock) useRetainedObjectsLock;
@property (T@"NSMutableSet",R,N,V_retainedObjects) retainedObjects;
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
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MTLToolsCommandBuffer unwrapMTLComputePassDescriptorInternal:];
```

## Instance methods

```
-[MTLToolsCommandBuffer presentDrawable:options:];
-[MTLToolsCommandBuffer commitWithDeadline:];
-[MTLToolsCommandBuffer encodeSignalEvent:value:agentMask:];
-[MTLToolsCommandBuffer commitAndHold];
-[MTLToolsCommandBuffer useInternalResidencySet:];
-[MTLToolsCommandBuffer addSynchronizationNotification:];
-[MTLToolsCommandBuffer GPUEndTime];
-[MTLToolsCommandBuffer presentDrawable:afterMinimumDuration:];
-[MTLToolsCommandBuffer encodeDashboardFinalizeForResourceGroup:dashboard:values:indices:count:];
-[MTLToolsCommandBuffer addCompletedHandler:];
-[MTLToolsCommandBuffer encodeDashboardTagForResourceGroup:];
-[MTLToolsCommandBuffer setProtectionOptions:];
-[MTLToolsCommandBuffer debugBufferContentsWithLength:];
-[MTLToolsCommandBuffer waitUntilScheduled];
-[MTLToolsCommandBuffer errorOptions];
-[MTLToolsCommandBuffer deadlineProfile];
-[MTLToolsCommandBuffer blitCommandEncoderWithDescriptor:];
-[MTLToolsCommandBuffer executeSynchronizationNotifications:scope:resources:count:];
-[MTLToolsCommandBuffer waitUntilCompleted];
-[MTLToolsCommandBuffer pushDebugGroup:];
-[MTLToolsCommandBuffer sampledAccelerationStructureCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLToolsCommandBuffer setLogs:];
-[MTLToolsCommandBuffer encodeDashboardFinalizeForResourceGroup:dashboard:value:forIndex:];
-[MTLToolsCommandBuffer sampledRenderCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLToolsCommandBuffer __waitUntilCompletedAsync:];
-[MTLToolsCommandBuffer useResidencySet:];
-[MTLToolsCommandBuffer addScheduledHandler:];
-[MTLToolsCommandBuffer computeCommandEncoderWithDispatchType:];
-[MTLToolsCommandBuffer resourceStateCommandEncoderWithDescriptor:];
-[MTLToolsCommandBuffer sampledComputeCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLToolsCommandBuffer setResponsibleTaskIDs:count:];
-[MTLToolsCommandBuffer enqueue];
-[MTLToolsCommandBuffer kernelStartTime];
-[MTLToolsCommandBuffer commit];
-[MTLToolsCommandBuffer presentDrawable:];
-[MTLToolsCommandBuffer retainedReferences];
-[MTLToolsCommandBuffer commitAndWaitUntilSubmittedWithDeadline:];
-[MTLToolsCommandBuffer __waitUntilScheduledAsync:];
-[MTLToolsCommandBuffer computeCommandEncoderWithDescriptor:];
-[MTLToolsCommandBuffer useResidencySets:count:];
-[MTLToolsCommandBuffer isProfilingEnabled];
-[MTLToolsCommandBuffer logs];
-[MTLToolsCommandBuffer sampledBlitCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLToolsCommandBuffer userDictionary];
-[MTLToolsCommandBuffer sampledBlitCommandEncoder:capacity:];
-[MTLToolsCommandBuffer sampledComputeCommandEncoderWithProgramInfoBuffer:capacity:];
-[MTLToolsCommandBuffer executeSynchronizationNotifications:];
-[MTLToolsCommandBuffer sampledAccelerationStructureCommandEncoder:capacity:];
-[MTLToolsCommandBuffer sampledComputeCommandEncoderWithDispatchType:programInfoBuffer:capacity:];
-[MTLToolsCommandBuffer presentDrawable:atTime:];
-[MTLToolsCommandBuffer popDebugGroup];
-[MTLToolsCommandBuffer commitAndWaitUntilSubmitted];
-[MTLToolsCommandBuffer GPUStartTime];
-[MTLToolsCommandBuffer profilingResults];
-[MTLToolsCommandBuffer accelerationStructureCommandEncoderWithDescriptor:];
-[MTLToolsCommandBuffer setProfilingEnabled:];
-[MTLToolsCommandBuffer kernelEndTime];
-[MTLToolsCommandBuffer accelerationStructureCommandEncoder];
-[MTLToolsCommandBuffer encodeConditionalAbortEvent:];
-[MTLToolsCommandBuffer encodeSignalEvent:value:];
-[MTLToolsCommandBuffer useInternalResidencySets:count:];
-[MTLToolsCommandBuffer protectionOptions];
-[MTLToolsCommandBuffer computeCommandEncoder];
-[MTLToolsCommandBuffer label];
-[MTLToolsCommandBuffer setLabel:];
-[MTLToolsCommandBuffer getListIndex];
-[MTLToolsCommandBuffer globalTraceObjectID];
-[MTLToolsCommandBuffer dealloc];
-[MTLToolsCommandBuffer status];
-[MTLToolsCommandBuffer error];
-[MTLToolsCommandBuffer commandQueue];
-[MTLToolsCommandBuffer addPurgedResource:];
-[MTLToolsCommandBuffer encodeWaitForEvent:value:];
-[MTLToolsCommandBuffer encodeWaitForEvent:value:timeout:];
-[MTLToolsCommandBuffer addPurgedHeap:];
-[MTLToolsCommandBuffer respondsToSelector:];
-[MTLToolsCommandBuffer encodeSignalEventScheduled:value:];
-[MTLToolsCommandBuffer blitCommandEncoder];
-[MTLToolsCommandBuffer encodeCacheHintFinalize:resourceGroups:count:];
-[MTLToolsCommandBuffer encodeCacheHintTag:resourceGroups:count:];
-[MTLToolsCommandBuffer renderCommandEncoderWithDescriptor:];
-[MTLToolsCommandBuffer parallelRenderCommandEncoderWithDescriptor:];
-[MTLToolsCommandBuffer resourceStateCommandEncoder];
-[MTLToolsCommandBuffer initWithBaseObject:parent:];
-[MTLToolsCommandBuffer debugCommandEncoder];
-[MTLToolsCommandBuffer dropResourceGroups:count:];
-[MTLToolsCommandBuffer setResourceGroups:count:];
-[MTLToolsCommandBuffer retainedObjects];
-[MTLToolsCommandBuffer unwrapMTLComputePassDescriptor:];
-[MTLToolsCommandBuffer addRetainedObject:];
-[MTLToolsCommandBuffer clearRetainedObjects];
-[MTLToolsCommandBuffer initWithCommandBuffer:parent:descriptor:];
-[MTLToolsCommandBuffer invokeCompletedHandlers];
-[MTLToolsCommandBuffer invokeScheduledHandlers];
-[MTLToolsCommandBuffer postCompletionHandlers];
-[MTLToolsCommandBuffer postScheduledHandlers];
-[MTLToolsCommandBuffer preCommit];
-[MTLToolsCommandBuffer preCompletionHandlers];
-[MTLToolsCommandBuffer preScheduledHandlers];
-[MTLToolsCommandBuffer retainObjectsFromRenderPassDescriptor:];
-[MTLToolsCommandBuffer setUseRetainedObjectsLock:];
-[MTLToolsCommandBuffer unwrapMTLAccelerationStructurePassDescriptor:];
-[MTLToolsCommandBuffer unwrapMTLBlitPassDescriptor:];
-[MTLToolsCommandBuffer unwrapMTLRenderPassDescriptor:];
-[MTLToolsCommandBuffer unwrapMTLResourceStatePassDescriptor:];
-[MTLToolsCommandBuffer useRetainedObjectsLock];
-[MTLToolsCommandBuffer usedInternalResidencySets];
-[MTLToolsCommandBuffer usedResidencySets];
-[MTLToolsCommandBuffer willEncodeSignalEvent:value:writeableResources:];
```
