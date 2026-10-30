# `MTLCommandBufferSPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLCommandBuffer`
- 0 instance variables, 9 properties, 51 instance methods, 0 class methods

## Properties

```
@property (TQ,?,R,N,GgetListIndex) listIndex;
@property (TB,GisProfilingEnabled) profilingEnabled;
@property (T@"NSDictionary",R) profilingResults;
@property (T@"NSMutableDictionary",R,N) userDictionary;
@property (TQ,?,R) globalTraceObjectID;
@property (T@"<MTLBuffer>",?,&,N) privateData;
@property (TQ,?,N) privateDataOffset;
@property (T@"<MTLBuffer>",?,N) privateLoggingBuffer;
@property (T@"<MTLDeadlineProfile>",R,&) deadlineProfile;
```

## Instance methods

```
-[MTLCommandBufferSPI presentDrawable:options:];
-[MTLCommandBufferSPI commitWithDeadline:];
-[MTLCommandBufferSPI encodeSignalEvent:value:agentMask:];
-[MTLCommandBufferSPI useInternalResidencySet:];
-[MTLCommandBufferSPI encodeDashboardFinalizeForResourceGroup:dashboard:values:indices:count:];
-[MTLCommandBufferSPI encodeDashboardTagForResourceGroup:];
-[MTLCommandBufferSPI deadlineProfile];
-[MTLCommandBufferSPI setLogs:];
-[MTLCommandBufferSPI encodeDashboardFinalizeForResourceGroup:dashboard:value:forIndex:];
-[MTLCommandBufferSPI __waitUntilCompletedAsync:];
-[MTLCommandBufferSPI setResponsibleTaskIDs:count:];
-[MTLCommandBufferSPI commitAndWaitUntilSubmittedWithDeadline:];
-[MTLCommandBufferSPI __waitUntilScheduledAsync:];
-[MTLCommandBufferSPI isProfilingEnabled];
-[MTLCommandBufferSPI userDictionary];
-[MTLCommandBufferSPI profilingResults];
-[MTLCommandBufferSPI setProfilingEnabled:];
-[MTLCommandBufferSPI encodeConditionalAbortEvent:];
-[MTLCommandBufferSPI useInternalResidencySets:count:];
-[MTLCommandBufferSPI addPurgedResource:];
-[MTLCommandBufferSPI addPurgedHeap:];
-[MTLCommandBufferSPI commitAndHold];
-[MTLCommandBufferSPI setPrivateDataOffset:];
-[MTLCommandBufferSPI privateLoggingBuffer];
-[MTLCommandBufferSPI setProtectionOptions:];
-[MTLCommandBufferSPI debugBufferContentsWithLength:];
-[MTLCommandBufferSPI configWithCommandBufferDescriptor:];
-[MTLCommandBufferSPI sampledAccelerationStructureCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLCommandBufferSPI sampledRenderCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLCommandBufferSPI setPrivateData:];
-[MTLCommandBufferSPI privateData];
-[MTLCommandBufferSPI sampledComputeCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLCommandBufferSPI privateDataOffset];
-[MTLCommandBufferSPI sampledBlitCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLCommandBufferSPI sampledBlitCommandEncoder:capacity:];
-[MTLCommandBufferSPI sampledComputeCommandEncoderWithProgramInfoBuffer:capacity:];
-[MTLCommandBufferSPI sampledAccelerationStructureCommandEncoder:capacity:];
-[MTLCommandBufferSPI sampledComputeCommandEncoderWithDispatchType:programInfoBuffer:capacity:];
-[MTLCommandBufferSPI commitAndWaitUntilSubmitted];
-[MTLCommandBufferSPI setPrivateLoggingBuffer:];
-[MTLCommandBufferSPI protectionOptions];
-[MTLCommandBufferSPI getListIndex];
-[MTLCommandBufferSPI globalTraceObjectID];
-[MTLCommandBufferSPI encodeWaitForEvent:value:timeout:];
-[MTLCommandBufferSPI encodeSignalEventScheduled:value:];
-[MTLCommandBufferSPI encodeCacheHintFinalize:resourceGroups:count:];
-[MTLCommandBufferSPI encodeCacheHintTag:resourceGroups:count:];
-[MTLCommandBufferSPI debugCommandEncoder];
-[MTLCommandBufferSPI computeCommandEncoderWithDispatchType:substreamCount:];
-[MTLCommandBufferSPI dropResourceGroups:count:];
-[MTLCommandBufferSPI setResourceGroups:count:];
```
