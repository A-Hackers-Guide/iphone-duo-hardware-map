# `MTL4GPUDebugCommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4ToolsCommandBuffer`
- 22 instance variables, 3 properties, 41 instance methods, 0 class methods

## Instance variables

```
{ResourceUsageTable="_allocator"^{MTLGPUDebugStorageManager}"_backingMemory"@"<MTLBuffer>""_residencySet"@"<MTLResidencySet>""maxBitsinValue"I"_mutex"{shared_mutex="__base_"{__shared_mutex_base="__mut_"{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}}"__gate1_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__gate2_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__state_"I}}} tensorResidencyTable;
B _initialized;
^{Options=IiiiI{?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}} _options;
^{GPUDebugDeviceOptions=b1b1b1b1b1b1} _deviceOptions;
{MetalBuffer="heap"^{MetalBufferHeap}"index"I} _currentPooledBuffer;
Q _currentPooledBufferOffset;
I _numDispatches;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _allocationLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _tempBufLock;
B _supportsTileStage;
B _supportsMeshStage;
[6{unordered_map<unsigned long long, InCommandResourceInfo, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, InCommandResourceInfo>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long long, InCommandResourceInfo>, std::__unordered_map_hasher<unsigned long long, std::pair<const unsigned long long, InCommandResourceInfo>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::pair<const unsigned long long, InCommandResourceInfo>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::pair<const unsigned long long, InCommandResourceInfo>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, InCommandResourceInfo>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, InCommandResourceInfo>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, InCommandResourceInfo>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, InCommandResourceInfo>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}}] _inCommandResources;
{ResourceUsageTable="_allocator"^{MTLGPUDebugStorageManager}"_backingMemory"@"<MTLBuffer>""_residencySet"@"<MTLResidencySet>""maxBitsinValue"I"_mutex"{shared_mutex="__base_"{__shared_mutex_base="__mut_"{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}}"__gate1_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__gate2_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__state_"I}}} _bufferUsageTable;
{ResourceUsageTable="_allocator"^{MTLGPUDebugStorageManager}"_backingMemory"@"<MTLBuffer>""_residencySet"@"<MTLResidencySet>""maxBitsinValue"I"_mutex"{shared_mutex="__base_"{__shared_mutex_base="__mut_"{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}}"__gate1_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__gate2_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__state_"I}}} _textureUsageTable;
{ResourceUsageTable="_allocator"^{MTLGPUDebugStorageManager}"_backingMemory"@"<MTLBuffer>""_residencySet"@"<MTLResidencySet>""maxBitsinValue"I"_mutex"{shared_mutex="__base_"{__shared_mutex_base="__mut_"{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}}"__gate1_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__gate2_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__state_"I}}} _bvhUsageTable;
{HeapUsageTable="_heapUsage"Q"_heapEntries"{vector<HeapUsageTable::HeapUsageTableEntry, std::allocator<HeapUsageTable::HeapUsageTableEntry>>="__begin_"^{HeapUsageTableEntry}"__end_"^{HeapUsageTableEntry}""{?="__cap_"^{HeapUsageTableEntry}}}} _heapUsageTable;
{unordered_map<unsigned long, MTLGPUDebugResidencySet *, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, MTLGPUDebugResidencySet *>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, std::__unordered_map_hasher<unsigned long, std::pair<const unsigned long, MTLGPUDebugResidencySet *>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::pair<const unsigned long, MTLGPUDebugResidencySet *>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::pair<const unsigned long, MTLGPUDebugResidencySet *>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _residencySets;
{unordered_map<unsigned long, (anonymous namespace)::EncoderResourceUsage, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, (anonymous namespace)::EncoderResourceUsage>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, std::__unordered_map_hasher<unsigned long, std::pair<const unsigned long, (anonymous namespace)::EncoderResourceUsage>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::pair<const unsigned long, (anonymous namespace)::EncoderResourceUsage>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::pair<const unsigned long, (anonymous namespace)::EncoderResourceUsage>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _encodersResourceUsage;
@"<MTL4CommandAllocator>" _allocator;
@"<MTLLogState>" _reportLogState;
@"GPUDebugRetainedReportingData" _retainedData;
^B _deallocated;
```

## Properties

```
@property (TI,V_numDispatches) numDispatches;
@property (T@"MTLGPUDebugDevice",R,D) device;
@property (T@"GPUDebugRetainedReportingData",R,N) retainedData;
```

## Instance methods

```
-[MTL4GPUDebugCommandBuffer useResidencySet:];
-[MTL4GPUDebugCommandBuffer useResidencySets:count:];
-[MTL4GPUDebugCommandBuffer computeCommandEncoder];
-[MTL4GPUDebugCommandBuffer dealloc];
-[MTL4GPUDebugCommandBuffer renderCommandEncoderWithDescriptor:];
-[MTL4GPUDebugCommandBuffer beginCommandBufferWithAllocator:];
-[MTL4GPUDebugCommandBuffer beginCommandBufferWithAllocator:options:];
-[MTL4GPUDebugCommandBuffer endCommandBuffer];
-[MTL4GPUDebugCommandBuffer renderCommandEncoderWithDescriptor:options:];
-[MTL4GPUDebugCommandBuffer computeCommandEncoderWithSubstreamCount:];
-[MTL4GPUDebugCommandBuffer _Init];
-[MTL4GPUDebugCommandBuffer _lateInit];
-[MTL4GPUDebugCommandBuffer _temporaryBufferWithLength:];
-[MTL4GPUDebugCommandBuffer addInCommandResource:resourceType:encoderInfo:commandInfo:];
-[MTL4GPUDebugCommandBuffer addInCommandResourceAddress:resourceType:encoderInfo:commandInfo:];
-[MTL4GPUDebugCommandBuffer addResidencySetGPUDebug:fromEncoder:];
-[MTL4GPUDebugCommandBuffer addUsedPipelineState:];
-[MTL4GPUDebugCommandBuffer applyResidencySets:];
-[MTL4GPUDebugCommandBuffer beginningEncoder:type:];
-[MTL4GPUDebugCommandBuffer checkResidencyForResourceType:];
-[MTL4GPUDebugCommandBuffer encodeResourceTableBuffers:type:];
-[MTL4GPUDebugCommandBuffer endingEncoder:type:];
-[MTL4GPUDebugCommandBuffer getTableForResourceType:];
-[MTL4GPUDebugCommandBuffer initReportBufferInPrivateData:];
-[MTL4GPUDebugCommandBuffer initRetainedData];
-[MTL4GPUDebugCommandBuffer initWithCommandBuffer:device:];
-[MTL4GPUDebugCommandBuffer markBVH:];
-[MTL4GPUDebugCommandBuffer markBuffer:usage:];
-[MTL4GPUDebugCommandBuffer markBufferHandle:];
-[MTL4GPUDebugCommandBuffer markHeap:stages:];
-[MTL4GPUDebugCommandBuffer markHeap:usage:stages:];
-[MTL4GPUDebugCommandBuffer markTensor:];
-[MTL4GPUDebugCommandBuffer markTexture:usage:];
-[MTL4GPUDebugCommandBuffer numDispatches];
-[MTL4GPUDebugCommandBuffer preCommit:];
-[MTL4GPUDebugCommandBuffer retainedData];
-[MTL4GPUDebugCommandBuffer setNumDispatches:];
-[MTL4GPUDebugCommandBuffer setResidencyForBufferRange:];
-[MTL4GPUDebugCommandBuffer setResidencyForResource:];
-[MTL4GPUDebugCommandBuffer temporaryBufferWithBytes:length:];
-[MTL4GPUDebugCommandBuffer temporaryBufferWithLength:];
```
