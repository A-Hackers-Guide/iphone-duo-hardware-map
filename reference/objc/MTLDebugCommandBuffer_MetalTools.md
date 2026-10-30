# `MTLDebugCommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsCommandBuffer`
- 13 instance variables, 0 properties, 54 instance methods, 0 class methods

## Instance variables

```
@"_MTLCommandEncoder" _currentEncoder;
{unordered_multiset<AttachmentDescriptorSimple, AttachmentDescriptorSimple::hash_t, AttachmentDescriptorSimple::equal_t, std::allocator<AttachmentDescriptorSimple>>="__table_"{__hash_table<AttachmentDescriptorSimple, AttachmentDescriptorSimple::hash_t, AttachmentDescriptorSimple::equal_t, std::allocator<AttachmentDescriptorSimple>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _attachmentSet;
{array<AttachmentDescriptorSimple, 8UL>="__elems_"[8{AttachmentDescriptorSimple="texture"^v"level"Q"sliceRange"{_NSRange="location"Q"length"Q}"depthPlaneRange"{_NSRange="location"Q"length"Q}"storeAction"Q}]} _prevAttachments;
{array<AttachmentDescriptorSimple, 8UL>="__elems_"[8{AttachmentDescriptorSimple="texture"^v"level"Q"sliceRange"{_NSRange="location"Q"length"Q}"depthPlaneRange"{_NSRange="location"Q"length"Q}"storeAction"Q}]} _currAttachments;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _purgeableObjectsLock;
{unordered_set<id<MTLDebugResourcePurgeable>, std::hash<id<MTLDebugResourcePurgeable>>, std::equal_to<id<MTLDebugResourcePurgeable>>, std::allocator<id<MTLDebugResourcePurgeable>>>="__table_"{__hash_table<id<MTLDebugResourcePurgeable>, std::hash<id<MTLDebugResourcePurgeable>>, std::equal_to<id<MTLDebugResourcePurgeable>>, std::allocator<id<MTLDebugResourcePurgeable>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<id<MTLDebugResourcePurgeable>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<id<MTLDebugResourcePurgeable>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<id<MTLDebugResourcePurgeable>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<id<MTLDebugResourcePurgeable>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _referencedPurgeableObjects;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _retainedObjectsLock;
{unordered_set<MTLToolsObject *, std::hash<MTLToolsObject *>, std::equal_to<MTLToolsObject *>, std::allocator<MTLToolsObject *>>="__table_"{__hash_table<MTLToolsObject *, std::hash<MTLToolsObject *>, std::equal_to<MTLToolsObject *>, std::allocator<MTLToolsObject *>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _externallyRetainedObjects;
{unordered_set<MTLToolsObject *, std::hash<MTLToolsObject *>, std::equal_to<MTLToolsObject *>, std::allocator<MTLToolsObject *>>="__table_"{__hash_table<MTLToolsObject *, std::hash<MTLToolsObject *>, std::equal_to<MTLToolsObject *>, std::allocator<MTLToolsObject *>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<MTLToolsObject *, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _internallyRetainedObjects;
@"MTLToolsObject" _referencedDeadObject;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _renderTargetAttachmentLock;
B _didAddRenderTargetAttachments;
@"NSMutableSet" _renderTargetAttachments;
```

## Instance methods

```
-[MTLDebugCommandBuffer commitWithDeadline:];
-[MTLDebugCommandBuffer useInternalResidencySet:];
-[MTLDebugCommandBuffer addSynchronizationNotification:];
-[MTLDebugCommandBuffer encodeDashboardFinalizeForResourceGroup:dashboard:values:indices:count:];
-[MTLDebugCommandBuffer addCompletedHandler:];
-[MTLDebugCommandBuffer encodeDashboardTagForResourceGroup:];
-[MTLDebugCommandBuffer debugBufferContentsWithLength:];
-[MTLDebugCommandBuffer waitUntilScheduled];
-[MTLDebugCommandBuffer blitCommandEncoderWithDescriptor:];
-[MTLDebugCommandBuffer executeSynchronizationNotifications:scope:resources:count:];
-[MTLDebugCommandBuffer waitUntilCompleted];
-[MTLDebugCommandBuffer sampledAccelerationStructureCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLDebugCommandBuffer encodeDashboardFinalizeForResourceGroup:dashboard:value:forIndex:];
-[MTLDebugCommandBuffer sampledRenderCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLDebugCommandBuffer useResidencySet:];
-[MTLDebugCommandBuffer addScheduledHandler:];
-[MTLDebugCommandBuffer computeCommandEncoderWithDispatchType:];
-[MTLDebugCommandBuffer resourceStateCommandEncoderWithDescriptor:];
-[MTLDebugCommandBuffer sampledComputeCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLDebugCommandBuffer computeCommandEncoderWithDescriptor:];
-[MTLDebugCommandBuffer useResidencySets:count:];
-[MTLDebugCommandBuffer sampledBlitCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLDebugCommandBuffer sampledBlitCommandEncoder:capacity:];
-[MTLDebugCommandBuffer sampledComputeCommandEncoderWithProgramInfoBuffer:capacity:];
-[MTLDebugCommandBuffer executeSynchronizationNotifications:];
-[MTLDebugCommandBuffer sampledAccelerationStructureCommandEncoder:capacity:];
-[MTLDebugCommandBuffer sampledComputeCommandEncoderWithDispatchType:programInfoBuffer:capacity:];
-[MTLDebugCommandBuffer accelerationStructureCommandEncoderWithDescriptor:];
-[MTLDebugCommandBuffer accelerationStructureCommandEncoder];
-[MTLDebugCommandBuffer encodeSignalEvent:value:];
-[MTLDebugCommandBuffer useInternalResidencySets:count:];
-[MTLDebugCommandBuffer computeCommandEncoder];
-[MTLDebugCommandBuffer dealloc];
-[MTLDebugCommandBuffer encodeWaitForEvent:value:];
-[MTLDebugCommandBuffer encodeWaitForEvent:value:timeout:];
-[MTLDebugCommandBuffer blitCommandEncoder];
-[MTLDebugCommandBuffer renderCommandEncoderWithDescriptor:];
-[MTLDebugCommandBuffer parallelRenderCommandEncoderWithDescriptor:];
-[MTLDebugCommandBuffer resourceStateCommandEncoder];
-[MTLDebugCommandBuffer _removeUsedRenderTargetsExcept:];
-[MTLDebugCommandBuffer addActiveRenderTargets:];
-[MTLDebugCommandBuffer addObject:retained:purgeable:];
-[MTLDebugCommandBuffer addPurgeableObject:];
-[MTLDebugCommandBuffer addReferencedObject:internallyRetained:];
-[MTLDebugCommandBuffer initWithCommandBuffer:commandQueue:descriptor:];
-[MTLDebugCommandBuffer lockPurgeableObjects];
-[MTLDebugCommandBuffer postCompletionHandlers];
-[MTLDebugCommandBuffer preCommit];
-[MTLDebugCommandBuffer preCompletionHandlers];
-[MTLDebugCommandBuffer removeAllReferencedObjects:];
-[MTLDebugCommandBuffer testObjectReferenced:wasInternallyRetained:];
-[MTLDebugCommandBuffer unlockPurgeableObjects];
-[MTLDebugCommandBuffer unwrapMTLRenderPassDescriptor:];
-[MTLDebugCommandBuffer validateStoreLoadTransition:atIndex:renderTargetArrayLength:];
```
