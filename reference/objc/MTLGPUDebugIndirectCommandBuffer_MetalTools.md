# `MTLGPUDebugIndirectCommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsIndirectCommandBuffer`
- Protocols: `MTLGPUDebugResource`
- 26 instance variables, 43 properties, 49 instance methods, 0 class methods

## Instance variables

```
B _hasRender;
B _hasOnlyRender;
B _hasCompute;
B _inheritsBuffers;
B _inheritsPipelineState;
@"<MTLBuffer>" _argumentStorage;
@"<MTLBuffer>" _vertexKernelDrawOrDispatchIDBuffer;
@"<MTLBuffer>" _fragmentDrawIDBuffer;
@"<MTLBuffer>" _meshDrawIDBuffer;
@"<MTLBuffer>" _objectDrawIDBuffer;
@"<MTLBuffer>" _SVBindingTableMeshBuffer;
@"<MTLBuffer>" _SVBindingTableObjectBuffer;
@"<MTLBuffer>" _SVBindingTableVertexKernelBuffer;
@"<MTLBuffer>" _SVBindingTableFragmentBuffer;
Q _maxCommands;
Q _maxThreadgroupBindings;
{unordered_map<unsigned long, id, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, id>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long, id>, std::__unordered_map_hasher<unsigned long, std::pair<const unsigned long, id>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::pair<const unsigned long, id>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::pair<const unsigned long, id>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, id>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, id>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, id>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, id>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _pipelineForCommand;
B _mayContainDrawMeshes;
Q _commandByteStride;
Q _originalResourceOptions;
B _initializedTables;
Q _maxVertexBindings;
Q _maxFragmentBindings;
Q _maxKernelBindings;
Q _maxObjectBindings;
Q _maxMeshBindings;
```

## Properties

```
@property (T@"<MTLBuffer>",R,N) internalICBBuffer;
@property (T@"<MTLBuffer>",R,N) internalDispatchIDBuffer;
@property (T@"<MTLBuffer>",R,N) internalVertexDrawIDBuffer;
@property (T@"<MTLBuffer>",R,N) internalFragmentDrawIDBuffer;
@property (T@"<MTLBuffer>",R,N) internalMeshDrawIDBuffer;
@property (T@"<MTLBuffer>",R,N) internalObjectDrawIDBuffer;
@property (TQ,R,N) maxCommands;
@property (TQ,R,N,V_maxVertexBindings) maxVertexBindings;
@property (TQ,R,N,V_maxFragmentBindings) maxFragmentBindings;
@property (TQ,R,N,V_maxKernelBindings) maxKernelBindings;
@property (TQ,R,N,V_maxObjectBindings) maxObjectBindings;
@property (TQ,R,N,V_maxMeshBindings) maxMeshBindings;
@property (TB,R,N) mayContainDrawMeshes;
@property (TB,R,N) hasOnlyRender;
@property (TQ,R,N) commandByteStride;
@property (TB,R,N) inheritsPipelineState;
@property (TB,R,N) inheritsBuffers;
@property (T@"<MTLBuffer>",N,V_SVBindingTableVertexKernelBuffer) SVBindingTableVertexKernelBuffer;
@property (T@"<MTLBuffer>",N,V_SVBindingTableFragmentBuffer) SVBindingTableFragmentBuffer;
@property (T@"<MTLBuffer>",N,V_SVBindingTableMeshBuffer) SVBindingTableMeshBuffer;
@property (T@"<MTLBuffer>",N,V_SVBindingTableObjectBuffer) SVBindingTableObjectBuffer;
@property (TB,N,V_initializedTables) initializedTables;
@property (T@"<MTLIndirectCommandBufferSPI>",&,D,N) baseObject;
@property (TQ,R,N) length;
@property (TQ,R,N) gpuAddress;
@property (TQ,R,N) underlyingGPUAddress;
@property (Ti) responsibleProcess;
@property (TQ,R) allocationID;
@property (TQ,R) protectionOptions;
@property (TQ,R) unfilteredResourceOptions;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) cpuCacheMode;
@property (TQ,R) storageMode;
@property (TQ,R) hazardTrackingMode;
@property (TQ,R) resourceOptions;
@property (T@"<MTLHeap>",R) heap;
@property (TQ,R) heapOffset;
@property (TQ,R) allocatedSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLGPUDebugIndirectCommandBuffer resourceOptions];
-[MTLGPUDebugIndirectCommandBuffer hazardTrackingMode];
-[MTLGPUDebugIndirectCommandBuffer cpuCacheMode];
-[MTLGPUDebugIndirectCommandBuffer storageMode];
-[MTLGPUDebugIndirectCommandBuffer dealloc];
-[MTLGPUDebugIndirectCommandBuffer gpuAddress];
-[MTLGPUDebugIndirectCommandBuffer length];
-[MTLGPUDebugIndirectCommandBuffer gpuResourceID];
-[MTLGPUDebugIndirectCommandBuffer indirectComputeCommandAtIndex:];
-[MTLGPUDebugIndirectCommandBuffer indirectRenderCommandAtIndex:];
-[MTLGPUDebugIndirectCommandBuffer SVBindingTableFragmentBuffer];
-[MTLGPUDebugIndirectCommandBuffer SVBindingTableObjectBuffer];
-[MTLGPUDebugIndirectCommandBuffer inheritsBuffers];
-[MTLGPUDebugIndirectCommandBuffer maxMeshBindings];
-[MTLGPUDebugIndirectCommandBuffer SVBindingTableMeshBuffer];
-[MTLGPUDebugIndirectCommandBuffer SVBindingTableVertexKernelBuffer];
-[MTLGPUDebugIndirectCommandBuffer commandByteStride];
-[MTLGPUDebugIndirectCommandBuffer handleForOffset:];
-[MTLGPUDebugIndirectCommandBuffer hasOnlyRender];
-[MTLGPUDebugIndirectCommandBuffer inheritsPipelineState];
-[MTLGPUDebugIndirectCommandBuffer initWithIndirectCommandBuffer:descriptor:maxCommandCount:resourceOptions:device:];
-[MTLGPUDebugIndirectCommandBuffer initializedTables];
-[MTLGPUDebugIndirectCommandBuffer internalDispatchIDBuffer];
-[MTLGPUDebugIndirectCommandBuffer internalFragmentDrawIDBuffer];
-[MTLGPUDebugIndirectCommandBuffer internalICBBuffer];
-[MTLGPUDebugIndirectCommandBuffer internalMeshDrawIDBuffer];
-[MTLGPUDebugIndirectCommandBuffer internalObjectDrawIDBuffer];
-[MTLGPUDebugIndirectCommandBuffer internalVertexDrawIDBuffer];
-[MTLGPUDebugIndirectCommandBuffer maxCommands];
-[MTLGPUDebugIndirectCommandBuffer maxFragmentBindings];
-[MTLGPUDebugIndirectCommandBuffer maxKernelBindings];
-[MTLGPUDebugIndirectCommandBuffer maxObjectBindings];
-[MTLGPUDebugIndirectCommandBuffer maxVertexBindings];
-[MTLGPUDebugIndirectCommandBuffer mayContainDrawMeshes];
-[MTLGPUDebugIndirectCommandBuffer onExecuteWithComputeEncoder:];
-[MTLGPUDebugIndirectCommandBuffer onExecuteWithRenderEncoder:];
-[MTLGPUDebugIndirectCommandBuffer pipelineForCommandAtIndex:];
-[MTLGPUDebugIndirectCommandBuffer resetAtIndex:];
-[MTLGPUDebugIndirectCommandBuffer setComputePipelineStateBuffers:commandIndex:];
-[MTLGPUDebugIndirectCommandBuffer setInitializedTables:];
-[MTLGPUDebugIndirectCommandBuffer setRenderPipelineStateBuffers:commandIndex:];
-[MTLGPUDebugIndirectCommandBuffer setSVBindingTableFragmentBuffer:];
-[MTLGPUDebugIndirectCommandBuffer setSVBindingTableMeshBuffer:];
-[MTLGPUDebugIndirectCommandBuffer setSVBindingTableObjectBuffer:];
-[MTLGPUDebugIndirectCommandBuffer setSVBindingTableVertexKernelBuffer:];
-[MTLGPUDebugIndirectCommandBuffer setThreadgroupMemoryLength:atIndex:commandIndex:];
-[MTLGPUDebugIndirectCommandBuffer underlyingGPUAddress];
-[MTLGPUDebugIndirectCommandBuffer useWithComputeEncoder:usage:];
-[MTLGPUDebugIndirectCommandBuffer useWithRenderEncoder:usage:stages:];
```
