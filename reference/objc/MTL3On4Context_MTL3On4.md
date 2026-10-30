# `MTL3On4Context`

- Image: [`/System/Library/PrivateFrameworks/MTL3On4.framework/MTL3On4`](../userland/System__Library__PrivateFrameworks__MTL3On4.framework__MTL3On4.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _transientBufferPoolLock;
{vector<id<MTLBuffer>, std::allocator<id<MTLBuffer>>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _transientBufferPool;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _commandAllocatorPoolLock;
{vector<id<MTL4CommandAllocator>, std::allocator<id<MTL4CommandAllocator>>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _commandAllocatorPool;
{MTL3On4ResourceHazardMap="m_ResourceHazardMapShards"[16{MTL3On4ResourceHazardMapShard="hazardTrackedAllocations"{unordered_map<id<MTLAllocation>, MTL3On4ResourceHazardMap::MTL3On4HazardTrackedAllocationEntry, std::hash<id<MTLAllocation>>, std::equal_to<id<MTLAllocation>>, std::allocator<std::pair<const id<MTLAllocation>, MTL3On4ResourceHazardMap::MTL3On4HazardTrackedAllocationEntry>>>="__table_"{__hash_table<std::__hash_value_type<id<MTLAllocation>, MTL3On4ResourceHazardMap::MTL3On4HazardTrackedAllocationEntry>, std::__unordered_map_hasher<id<MTLAllocation>, std::pair<const id<MTLAllocation>, MTL3On4ResourceHazardMap::MTL3On4HazardTrackedAllocationEntry>, std::hash<id<MTLAllocation>>, std::equal_to<id<MTLAllocation>>>, std::__unordered_map_equal<id<MTLAllocation>, std::pair<const id<MTLAllocation>, MTL3On4ResourceHazardMap::MTL3On4HazardTrackedAllocationEntry>, std::equal_to<id<MTLAllocation>>, std::hash<id<MTLAllocation>>>, std::allocator<std::pair<const id<MTLAllocation>, MTL3On4ResourceHazardMap::MTL3On4HazardTrackedAllocationEntry>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<id<MTLAllocation>, MTL3On4ResourceHazardMap::MTL3On4HazardTrackedAllocationEntry>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<id<MTLAllocation>, MTL3On4ResourceHazardMap::MTL3On4HazardTrackedAllocationEntry>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<id<MTLAllocation>, MTL3On4ResourceHazardMap::MTL3On4HazardTrackedAllocationEntry>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<id<MTLAllocation>, MTL3On4ResourceHazardMap::MTL3On4HazardTrackedAllocationEntry>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}}"fencePool"{MTL3On4ResourceFencePool="m_Device"@"<MTLDevice>""m_ResourceFences"{vector<MTL3On4ResourceFences, std::allocator<MTL3On4ResourceFences>>="__begin_"^{?}"__end_"^{?}""{?="__cap_"^{?}}}"m_ReferenceCounts"{vector<unsigned int, std::allocator<unsigned int>>="__begin_"^I"__end_"^I""{?="__cap_"^I}}"m_FreeList"{vector<unsigned int, std::allocator<unsigned int>>="__begin_"^I"__end_"^I""{?="__cap_"^I}}"m_Capacity"I"m_Size"I"m_OverflowCounter"I}"lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}}]} _resourceHazardMap;
```

## Instance methods

```
-[MTL3On4Context initWithDevice:];
-[MTL3On4Context dealloc];
-[MTL3On4Context allocateTransientBufferFromPool];
-[MTL3On4Context allocateCommandAllocatorFromPool];
-[MTL3On4Context fencesForAllocation:incrementReferenceCount:];
-[MTL3On4Context notifyAllocationComplete:];
-[MTL3On4Context releasePooledCommandAllocator:];
-[MTL3On4Context releasePooledTransientBuffer:];
```
