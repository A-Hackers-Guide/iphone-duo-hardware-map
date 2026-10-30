# `MTL3On4CommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/MTL3On4.framework/MTL3On4`](../userland/System__Library__PrivateFrameworks__MTL3On4.framework__MTL3On4.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTLCommandBufferSPI`
- 34 instance variables, 29 properties, 101 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
@"MTL3On4Context" _context;
@"MTL3On4CommandQueue" _commandQueue;
@"<MTL4CommandBuffer>" _commandBuffer;
@"<MTL4CommandAllocator>" _commandAllocator;
B _isPooledCommandAllocator;
@"<MTL4ArgumentTable>" _computeArgumentTable;
@"<MTLResidencySet>" _residencySet;
{vector<void (^)(id<MTLCommandBuffer>), std::allocator<void (^)(id<MTLCommandBuffer>)>>="__begin_"^@?"__end_"^@?""{?="__cap_"^@?}} _scheduledHandlers;
{vector<void (^)(id<MTLCommandBuffer>), std::allocator<void (^)(id<MTLCommandBuffer>)>>="__begin_"^@?"__end_"^@?""{?="__cap_"^@?}} _completedHandlers;
{unordered_map<id<MTLAllocation>, MTL3On4ResourceFences, std::hash<id<MTLAllocation>>, std::equal_to<id<MTLAllocation>>, std::allocator<std::pair<const id<MTLAllocation>, MTL3On4ResourceFences>>>="__table_"{__hash_table<std::__hash_value_type<id<MTLAllocation>, MTL3On4ResourceFences>, std::__unordered_map_hasher<id<MTLAllocation>, std::pair<const id<MTLAllocation>, MTL3On4ResourceFences>, std::hash<id<MTLAllocation>>, std::equal_to<id<MTLAllocation>>>, std::__unordered_map_equal<id<MTLAllocation>, std::pair<const id<MTLAllocation>, MTL3On4ResourceFences>, std::equal_to<id<MTLAllocation>>, std::hash<id<MTLAllocation>>>, std::allocator<std::pair<const id<MTLAllocation>, MTL3On4ResourceFences>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<id<MTLAllocation>, MTL3On4ResourceFences>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<id<MTLAllocation>, MTL3On4ResourceFences>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<id<MTLAllocation>, MTL3On4ResourceFences>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<id<MTLAllocation>, MTL3On4ResourceFences>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _fenceCache;
@"<MTLBuffer>" _currentTransientBuffer;
Q _currentTransientBufferUsedSize;
{vector<id<MTLBuffer>, std::allocator<id<MTLBuffer>>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _allTransientBuffers;
@"<MTLLogContainer>" _logs;
@"NSError" _error;
@"NSMutableDictionary" _userDictionary;
Q _protectionOptions;
@? _perfSampleHandlerBlock;
{MTL3On4CommandBufferStatistics="creationTime"Q"enqueueTime"Q"commitTime"Q"submitToKernelTime"Q"kernelEndTime"Q"submitToHardwareTime"Q"completionInterruptTime"Q"gpuEndTime"Q"completionHandlerEnqueueTime"Q"completionHandlerExecutionTime"Q} _profilingStatistics;
B _statEnabled;
B _retainedReferences;
{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}} _hasPendingCompletionHandlerConditionVariable;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _hasPendingCompletionHandlerMutex;
B _hasPendingCompletionHandler;
@"NSMutableArray" _retainedObjects;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _commitAndCompletionLock;
B _profilingEnabled;
Q _status;
Q _errorOptions;
d _GPUStartTime;
d _GPUEndTime;
d _kernelStartTime;
d _kernelEndTime;
```

## Properties

```
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
```

## Instance methods

```
-[MTL3On4CommandBuffer presentDrawable:options:];
-[MTL3On4CommandBuffer commitWithDeadline:];
-[MTL3On4CommandBuffer encodeSignalEvent:value:agentMask:];
-[MTL3On4CommandBuffer setPrivateDataOffset:];
-[MTL3On4CommandBuffer useInternalResidencySet:];
-[MTL3On4CommandBuffer GPUEndTime];
-[MTL3On4CommandBuffer privateLoggingBuffer];
-[MTL3On4CommandBuffer presentDrawable:afterMinimumDuration:];
-[MTL3On4CommandBuffer encodeDashboardFinalizeForResourceGroup:dashboard:values:indices:count:];
-[MTL3On4CommandBuffer addCompletedHandler:];
-[MTL3On4CommandBuffer encodeDashboardTagForResourceGroup:];
-[MTL3On4CommandBuffer setProtectionOptions:];
-[MTL3On4CommandBuffer debugBufferContentsWithLength:];
-[MTL3On4CommandBuffer waitUntilScheduled];
-[MTL3On4CommandBuffer errorOptions];
-[MTL3On4CommandBuffer deadlineProfile];
-[MTL3On4CommandBuffer blitCommandEncoderWithDescriptor:];
-[MTL3On4CommandBuffer waitUntilCompleted];
-[MTL3On4CommandBuffer pushDebugGroup:];
-[MTL3On4CommandBuffer configWithCommandBufferDescriptor:];
-[MTL3On4CommandBuffer setLogs:];
-[MTL3On4CommandBuffer encodeDashboardFinalizeForResourceGroup:dashboard:value:forIndex:];
-[MTL3On4CommandBuffer sampledRenderCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTL3On4CommandBuffer setPrivateData:];
-[MTL3On4CommandBuffer __waitUntilCompletedAsync:];
-[MTL3On4CommandBuffer useResidencySet:];
-[MTL3On4CommandBuffer addScheduledHandler:];
-[MTL3On4CommandBuffer privateData];
-[MTL3On4CommandBuffer computeCommandEncoderWithDispatchType:];
-[MTL3On4CommandBuffer resourceStateCommandEncoderWithDescriptor:];
-[MTL3On4CommandBuffer sampledComputeCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTL3On4CommandBuffer setResponsibleTaskIDs:count:];
-[MTL3On4CommandBuffer enqueue];
-[MTL3On4CommandBuffer kernelStartTime];
-[MTL3On4CommandBuffer commit];
-[MTL3On4CommandBuffer presentDrawable:];
-[MTL3On4CommandBuffer retainedReferences];
-[MTL3On4CommandBuffer commitAndWaitUntilSubmittedWithDeadline:];
-[MTL3On4CommandBuffer __waitUntilScheduledAsync:];
-[MTL3On4CommandBuffer computeCommandEncoderWithDescriptor:];
-[MTL3On4CommandBuffer privateDataOffset];
-[MTL3On4CommandBuffer useResidencySets:count:];
-[MTL3On4CommandBuffer isProfilingEnabled];
-[MTL3On4CommandBuffer logs];
-[MTL3On4CommandBuffer isCommitted];
-[MTL3On4CommandBuffer userDictionary];
-[MTL3On4CommandBuffer sampledComputeCommandEncoderWithProgramInfoBuffer:capacity:];
-[MTL3On4CommandBuffer sampledComputeCommandEncoderWithDispatchType:programInfoBuffer:capacity:];
-[MTL3On4CommandBuffer presentDrawable:atTime:];
-[MTL3On4CommandBuffer popDebugGroup];
-[MTL3On4CommandBuffer GPUStartTime];
-[MTL3On4CommandBuffer profilingResults];
-[MTL3On4CommandBuffer accelerationStructureCommandEncoderWithDescriptor:];
-[MTL3On4CommandBuffer setProfilingEnabled:];
-[MTL3On4CommandBuffer kernelEndTime];
-[MTL3On4CommandBuffer setPrivateLoggingBuffer:];
-[MTL3On4CommandBuffer accelerationStructureCommandEncoder];
-[MTL3On4CommandBuffer encodeConditionalAbortEvent:];
-[MTL3On4CommandBuffer encodeSignalEvent:value:];
-[MTL3On4CommandBuffer useInternalResidencySets:count:];
-[MTL3On4CommandBuffer protectionOptions];
-[MTL3On4CommandBuffer device];
-[MTL3On4CommandBuffer computeCommandEncoder];
-[MTL3On4CommandBuffer isStatEnabled];
-[MTL3On4CommandBuffer getListIndex];
-[MTL3On4CommandBuffer globalTraceObjectID];
-[MTL3On4CommandBuffer dealloc];
-[MTL3On4CommandBuffer setStatEnabled:];
-[MTL3On4CommandBuffer status];
-[MTL3On4CommandBuffer error];
-[MTL3On4CommandBuffer commandQueue];
-[MTL3On4CommandBuffer addPurgedResource:];
-[MTL3On4CommandBuffer encodeWaitForEvent:value:];
-[MTL3On4CommandBuffer encodeWaitForEvent:value:timeout:];
-[MTL3On4CommandBuffer addPurgedHeap:];
-[MTL3On4CommandBuffer context];
-[MTL3On4CommandBuffer encodeSignalEventScheduled:value:];
-[MTL3On4CommandBuffer blitCommandEncoder];
-[MTL3On4CommandBuffer encodeCacheHintFinalize:resourceGroups:count:];
-[MTL3On4CommandBuffer encodeCacheHintTag:resourceGroups:count:];
-[MTL3On4CommandBuffer renderCommandEncoderWithDescriptor:];
-[MTL3On4CommandBuffer residencySet];
-[MTL3On4CommandBuffer parallelRenderCommandEncoderWithDescriptor:];
-[MTL3On4CommandBuffer resourceStateCommandEncoder];
-[MTL3On4CommandBuffer computeCommandEncoderWithDispatchType:substreamCount:];
-[MTL3On4CommandBuffer dropResourceGroups:count:];
-[MTL3On4CommandBuffer setResourceGroups:count:];
-[MTL3On4CommandBuffer prepareForDeferredCommit];
-[MTL3On4CommandBuffer _commandBufferDidCompleteWithCommitFeedback:];
-[MTL3On4CommandBuffer _prepareForCommit];
-[MTL3On4CommandBuffer allocateTransientBytes:];
-[MTL3On4CommandBuffer allocateTransientBytes:alignment:];
-[MTL3On4CommandBuffer cachedFencesForAllocation:];
-[MTL3On4CommandBuffer commitToCommandQueue:];
-[MTL3On4CommandBuffer computeArgumentTable];
-[MTL3On4CommandBuffer initWithMTL3On4CommandQueue:];
-[MTL3On4CommandBuffer initWithMTL3On4CommandQueue:descriptor:];
-[MTL3On4CommandBuffer initWithMTL3On4CommandQueue:descriptor:context:commandBuffer:device:retainedReferences:];
-[MTL3On4CommandBuffer initWithMTL3On4CommandQueue:retainedReferences:];
-[MTL3On4CommandBuffer initWithMTL3On4Context:commandBuffer:];
-[MTL3On4CommandBuffer retainObject:];
```
