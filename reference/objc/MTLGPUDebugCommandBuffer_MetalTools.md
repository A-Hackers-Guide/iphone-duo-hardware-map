# `MTLGPUDebugCommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsCommandBuffer`
- Protocols: `MTLGPUDebugBufferEncoder`
- 26 instance variables, 2 properties, 46 instance methods, 0 class methods

## Instance variables

```
B _initialized;
^{Options=IiiiI{?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}} _options;
^{GPUDebugDeviceOptions=b1b1b1b1b1b1} _deviceOptions;
@"<MTLArgumentEncoder>" _stageArgumentEncoder;
{vector<MetalBuffer, std::allocator<MetalBuffer>>="__begin_"^{MetalBuffer}"__end_"^{MetalBuffer}""{?="__cap_"^{MetalBuffer}}} _usedBuffers;
{MetalBuffer="heap"^{MetalBufferHeap}"index"I} _currentPooledBuffer;
Q _currentPooledBufferOffset;
{vector<MTLGPUDebugBuffer *, std::allocator<MTLGPUDebugBuffer *>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _usedBytesBuffers;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _usedBytesBuffersLock;
I _currentEncoderID;
I _numDispatches;
{unordered_map<unsigned int, NSString *, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, NSString *>>>="__table_"{__hash_table<std::__hash_value_type<unsigned int, NSString *>, std::__unordered_map_hasher<unsigned int, std::pair<const unsigned int, NSString *>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::pair<const unsigned int, NSString *>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::pair<const unsigned int, NSString *>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, NSString *>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _encoderLabels;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _allocationLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _tempBufLock;
B _supportsTileStage;
B _supportsMeshStage;
[5@"<MTLBuffer>"] _internalBindingTables;
[4{ResourceUsageTable="_allocator"^{MTLGPUDebugStorageManager}"_backingMemory"@"<MTLBuffer>""_residencySet"@"<MTLResidencySet>""maxBitsinValue"I"_mutex"{shared_mutex="__base_"{__shared_mutex_base="__mut_"{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}}"__gate1_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__gate2_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__state_"I}}}] _bufferUsageTables;
[4{ResourceUsageTable="_allocator"^{MTLGPUDebugStorageManager}"_backingMemory"@"<MTLBuffer>""_residencySet"@"<MTLResidencySet>""maxBitsinValue"I"_mutex"{shared_mutex="__base_"{__shared_mutex_base="__mut_"{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}}"__gate1_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__gate2_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__state_"I}}}] _textureUsageTables;
[4{ResourceUsageTable="_allocator"^{MTLGPUDebugStorageManager}"_backingMemory"@"<MTLBuffer>""_residencySet"@"<MTLResidencySet>""maxBitsinValue"I"_mutex"{shared_mutex="__base_"{__shared_mutex_base="__mut_"{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}}"__gate1_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__gate2_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__state_"I}}}] _tensorResidencyTables;
[4{ResourceUsageTable="_allocator"^{MTLGPUDebugStorageManager}"_backingMemory"@"<MTLBuffer>""_residencySet"@"<MTLResidencySet>""maxBitsinValue"I"_mutex"{shared_mutex="__base_"{__shared_mutex_base="__mut_"{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}}"__gate1_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__gate2_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__state_"I}}}] _bvhUsageTables;
{HeapUsageTable="_heapUsage"Q"_heapEntries"{vector<HeapUsageTable::HeapUsageTableEntry, std::allocator<HeapUsageTable::HeapUsageTableEntry>>="__begin_"^{HeapUsageTableEntry}"__end_"^{HeapUsageTableEntry}""{?="__cap_"^{HeapUsageTableEntry}}}} _heapUsageTable;
{unordered_map<unsigned long, MTLGPUDebugResidencySet *, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, MTLGPUDebugResidencySet *>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, std::__unordered_map_hasher<unsigned long, std::pair<const unsigned long, MTLGPUDebugResidencySet *>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::pair<const unsigned long, MTLGPUDebugResidencySet *>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::pair<const unsigned long, MTLGPUDebugResidencySet *>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLGPUDebugResidencySet *>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _residencySets;
{unordered_map<unsigned long, (anonymous namespace)::EncoderResourceUsage, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, (anonymous namespace)::EncoderResourceUsage>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, std::__unordered_map_hasher<unsigned long, std::pair<const unsigned long, (anonymous namespace)::EncoderResourceUsage>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::pair<const unsigned long, (anonymous namespace)::EncoderResourceUsage>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::pair<const unsigned long, (anonymous namespace)::EncoderResourceUsage>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _encodersResourceUsage;
@"<MTLLogState>" _reportLogState;
@"MTLGPUDebugCommandQueue" _commandQueue;
```

## Properties

```
@property (TI,V_numDispatches) numDispatches;
@property (T@"MTLGPUDebugDevice",R,D) device;
```

## Instance methods

```
-[MTLGPUDebugCommandBuffer blitCommandEncoderWithDescriptor:];
-[MTLGPUDebugCommandBuffer sampledAccelerationStructureCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLGPUDebugCommandBuffer sampledRenderCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLGPUDebugCommandBuffer useResidencySet:];
-[MTLGPUDebugCommandBuffer computeCommandEncoderWithDispatchType:];
-[MTLGPUDebugCommandBuffer sampledComputeCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLGPUDebugCommandBuffer computeCommandEncoderWithDescriptor:];
-[MTLGPUDebugCommandBuffer useResidencySets:count:];
-[MTLGPUDebugCommandBuffer sampledBlitCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLGPUDebugCommandBuffer sampledBlitCommandEncoder:capacity:];
-[MTLGPUDebugCommandBuffer sampledComputeCommandEncoderWithProgramInfoBuffer:capacity:];
-[MTLGPUDebugCommandBuffer sampledAccelerationStructureCommandEncoder:capacity:];
-[MTLGPUDebugCommandBuffer sampledComputeCommandEncoderWithDispatchType:programInfoBuffer:capacity:];
-[MTLGPUDebugCommandBuffer accelerationStructureCommandEncoderWithDescriptor:];
-[MTLGPUDebugCommandBuffer accelerationStructureCommandEncoder];
-[MTLGPUDebugCommandBuffer computeCommandEncoder];
-[MTLGPUDebugCommandBuffer dealloc];
-[MTLGPUDebugCommandBuffer blitCommandEncoder];
-[MTLGPUDebugCommandBuffer renderCommandEncoderWithDescriptor:];
-[MTLGPUDebugCommandBuffer parallelRenderCommandEncoderWithDescriptor:];
-[MTLGPUDebugCommandBuffer _addUsedBuffer:];
-[MTLGPUDebugCommandBuffer _setInternalBindingTables:type:];
-[MTLGPUDebugCommandBuffer _checkReportBuffers];
-[MTLGPUDebugCommandBuffer _decodeReportLogState:];
-[MTLGPUDebugCommandBuffer _internalBindingTableForStage:];
-[MTLGPUDebugCommandBuffer _lateInit];
-[MTLGPUDebugCommandBuffer _temporaryBufferWithLength:];
-[MTLGPUDebugCommandBuffer addResidencySetGPUDebug:fromEncoder:];
-[MTLGPUDebugCommandBuffer beginingEncoder:type:];
-[MTLGPUDebugCommandBuffer encodeResourceTableBuffers:type:];
-[MTLGPUDebugCommandBuffer endingEncoder:type:];
-[MTLGPUDebugCommandBuffer initWithCommandBuffer:commandQueue:descriptor:];
-[MTLGPUDebugCommandBuffer markBVH:usage:stages:];
-[MTLGPUDebugCommandBuffer markBuffer:usage:stages:];
-[MTLGPUDebugCommandBuffer markBufferHandle:stages:];
-[MTLGPUDebugCommandBuffer markHeap:stages:];
-[MTLGPUDebugCommandBuffer markHeap:usage:stages:];
-[MTLGPUDebugCommandBuffer markTensor:stages:];
-[MTLGPUDebugCommandBuffer markTexture:usage:stages:];
-[MTLGPUDebugCommandBuffer numDispatches];
-[MTLGPUDebugCommandBuffer preCommit];
-[MTLGPUDebugCommandBuffer preCompletionHandlers];
-[MTLGPUDebugCommandBuffer resourceUsageForTexture:stage:];
-[MTLGPUDebugCommandBuffer setNumDispatches:];
-[MTLGPUDebugCommandBuffer temporaryBufferWithBytes:length:];
-[MTLGPUDebugCommandBuffer temporaryBufferWithLength:];
```
