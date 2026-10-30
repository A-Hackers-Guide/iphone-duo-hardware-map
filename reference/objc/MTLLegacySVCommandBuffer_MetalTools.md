# `MTLLegacySVCommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsCommandBuffer`
- Protocols: `MTLLegacySVBufferEncoder`
- 26 instance variables, 1 properties, 45 instance methods, 0 class methods

## Instance variables

```
B _initialized;
^{Options=IiiiI{?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}} _options;
^{LegacySVDeviceOptions=b1b1b1b1} _deviceOptions;
@"<MTLArgumentEncoder>" _stageArgumentEncoder;
@"<MTLBuffer>" _vertexComputeReportBuffer;
Q _vertexComputeReportOffset;
@"<MTLBuffer>" _fragmentReportBuffer;
Q _fragmentReportOffset;
{vector<LegacySVMetalBuffer, std::allocator<LegacySVMetalBuffer>>="__begin_"^{LegacySVMetalBuffer}"__end_"^{LegacySVMetalBuffer}""{?="__cap_"^{LegacySVMetalBuffer}}} _usedBuffers;
{LegacySVMetalBuffer="heap"^{LegacySVMetalBufferHeap}"index"I} _currentPooledBuffer;
Q _currentPooledBufferOffset;
I _currentEncoderID;
I _currentReportID;
{vector<id<MTLBuffer>, std::allocator<id<MTLBuffer>>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _reportBufferList;
{vector<(anonymous namespace)::ReportBufferEntry, std::allocator<(anonymous namespace)::ReportBufferEntry>>="__begin_"^{ReportBufferEntry}"__end_"^{ReportBufferEntry}""{?="__cap_"^{ReportBufferEntry}}} _reportEntryList;
{vector<NSString *, std::allocator<NSString *>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _encoderLabels;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _allocationLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _tempBufLock;
B _supportsTileStage;
B _supportsMeshStage;
B _hasDeferredBindingObjectAndMeshReportBuffers;
[4{BufferUsageTable="_backingMemory"@"<MTLBuffer>"}] _bufferUsageTables;
[4{TextureUsageTable="_backingMemory"@"<MTLBuffer>"}] _textureUsageTables;
{HeapUsageTable="_heapUsage"Q"_heapEntries"{vector<(anonymous namespace)::(anonymous namespace)::HeapUsageTable::HeapUsageTableEntry, std::allocator<(anonymous namespace)::(anonymous namespace)::HeapUsageTable::HeapUsageTableEntry>>="__begin_"^{HeapUsageTableEntry}"__end_"^{HeapUsageTableEntry}""{?="__cap_"^{HeapUsageTableEntry}}}} _heapUsageTable;
{unordered_map<unsigned long, MTLLegacySVResidencySet *, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, MTLLegacySVResidencySet *>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, std::__unordered_map_hasher<unsigned long, std::pair<const unsigned long, MTLLegacySVResidencySet *>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::pair<const unsigned long, MTLLegacySVResidencySet *>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::pair<const unsigned long, MTLLegacySVResidencySet *>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, MTLLegacySVResidencySet *>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _residencySets;
{unordered_map<unsigned long, (anonymous namespace)::EncoderResourceUsage, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, (anonymous namespace)::EncoderResourceUsage>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, std::__unordered_map_hasher<unsigned long, std::pair<const unsigned long, (anonymous namespace)::EncoderResourceUsage>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::pair<const unsigned long, (anonymous namespace)::EncoderResourceUsage>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::pair<const unsigned long, (anonymous namespace)::EncoderResourceUsage>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, (anonymous namespace)::EncoderResourceUsage>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _encodersResourceUsage;
```

## Properties

```
@property (T@"MTLLegacySVDevice",R,D) device;
```

## Instance methods

```
-[MTLLegacySVCommandBuffer blitCommandEncoderWithDescriptor:];
-[MTLLegacySVCommandBuffer sampledAccelerationStructureCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLLegacySVCommandBuffer sampledRenderCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLLegacySVCommandBuffer useResidencySet:];
-[MTLLegacySVCommandBuffer computeCommandEncoderWithDispatchType:];
-[MTLLegacySVCommandBuffer sampledComputeCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLLegacySVCommandBuffer computeCommandEncoderWithDescriptor:];
-[MTLLegacySVCommandBuffer useResidencySets:count:];
-[MTLLegacySVCommandBuffer sampledBlitCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLLegacySVCommandBuffer sampledBlitCommandEncoder:capacity:];
-[MTLLegacySVCommandBuffer sampledComputeCommandEncoderWithProgramInfoBuffer:capacity:];
-[MTLLegacySVCommandBuffer sampledAccelerationStructureCommandEncoder:capacity:];
-[MTLLegacySVCommandBuffer sampledComputeCommandEncoderWithDispatchType:programInfoBuffer:capacity:];
-[MTLLegacySVCommandBuffer accelerationStructureCommandEncoderWithDescriptor:];
-[MTLLegacySVCommandBuffer accelerationStructureCommandEncoder];
-[MTLLegacySVCommandBuffer computeCommandEncoder];
-[MTLLegacySVCommandBuffer dealloc];
-[MTLLegacySVCommandBuffer blitCommandEncoder];
-[MTLLegacySVCommandBuffer renderCommandEncoderWithDescriptor:];
-[MTLLegacySVCommandBuffer parallelRenderCommandEncoderWithDescriptor:];
-[MTLLegacySVCommandBuffer beginUseOfMeshShadersInEncoder:];
-[MTLLegacySVCommandBuffer _allocReportEntryStorageForType:];
-[MTLLegacySVCommandBuffer _checkReportBuffers];
-[MTLLegacySVCommandBuffer _encodeReportBuffer:type:];
-[MTLLegacySVCommandBuffer _lateInit];
-[MTLLegacySVCommandBuffer _newReportBuffer];
-[MTLLegacySVCommandBuffer _temporaryBufferWithLength:];
-[MTLLegacySVCommandBuffer addResidencySetGPUDebug:fromEncoder:];
-[MTLLegacySVCommandBuffer beginingEncoder:type:];
-[MTLLegacySVCommandBuffer encodeBuffers:offsets:withRange:resultOffset:];
-[MTLLegacySVCommandBuffer encodeResourceTableBuffers:type:];
-[MTLLegacySVCommandBuffer encoderIdentifierForEncoderIndex:];
-[MTLLegacySVCommandBuffer endingEncoder:type:];
-[MTLLegacySVCommandBuffer initWithCommandBuffer:commandQueue:descriptor:];
-[MTLLegacySVCommandBuffer markAccelerationStructure:usage:stages:];
-[MTLLegacySVCommandBuffer markBuffer:usage:stages:];
-[MTLLegacySVCommandBuffer markHeap:stages:];
-[MTLLegacySVCommandBuffer markHeap:usage:stages:];
-[MTLLegacySVCommandBuffer markTexture:usage:stages:];
-[MTLLegacySVCommandBuffer preCommit];
-[MTLLegacySVCommandBuffer preCompletionHandlers];
-[MTLLegacySVCommandBuffer resourceUsageForBuffer:stage:];
-[MTLLegacySVCommandBuffer resourceUsageForTexture:stage:];
-[MTLLegacySVCommandBuffer temporaryBufferWithBytes:length:];
-[MTLLegacySVCommandBuffer temporaryBufferWithLength:];
```
