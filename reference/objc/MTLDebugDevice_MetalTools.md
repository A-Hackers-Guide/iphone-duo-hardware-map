# `MTLDebugDevice`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsDevice`
- 8 instance variables, 3 properties, 164 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _argumentBufferSamplersLock;
{MTLSamplerDescriptorHashMap="_map"{unordered_map<std::array<unsigned long long, 3>, unsigned int, MTLSamplerDescriptorHashMap::hash_t, MTLSamplerDescriptorHashMap::equal_t, std::allocator<std::pair<const std::array<unsigned long long, 3>, unsigned int>>>="__table_"{__hash_table<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, std::__unordered_map_hasher<std::array<unsigned long long, 3>, std::pair<const std::array<unsigned long long, 3>, unsigned int>, MTLSamplerDescriptorHashMap::hash_t, MTLSamplerDescriptorHashMap::equal_t>, std::__unordered_map_equal<std::array<unsigned long long, 3>, std::pair<const std::array<unsigned long long, 3>, unsigned int>, MTLSamplerDescriptorHashMap::equal_t, MTLSamplerDescriptorHashMap::hash_t>, std::allocator<std::pair<const std::array<unsigned long long, 3>, unsigned int>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::array<unsigned long long, 3>, unsigned int>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}}"_limit"I} _argumentBufferSamplers;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _referenceTrackingCommandBufferLock;
{unordered_set<MTLDebugCommandBuffer *, std::hash<MTLDebugCommandBuffer *>, std::equal_to<MTLDebugCommandBuffer *>, std::allocator<MTLDebugCommandBuffer *>>="__table_"{__hash_table<MTLDebugCommandBuffer *, std::hash<MTLDebugCommandBuffer *>, std::equal_to<MTLDebugCommandBuffer *>, std::allocator<MTLDebugCommandBuffer *>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<MTLDebugCommandBuffer *, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<MTLDebugCommandBuffer *, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<MTLDebugCommandBuffer *, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<MTLDebugCommandBuffer *, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _referenceTrackingCommandBuffers;
{CheckerboardRenderTargetPipelineCache="_cacheLock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"_library"@"<MTLLibrary>""_vertexFunction"@"<MTLFunction>""_depthStencilState"[2@"<MTLDepthStencilState>"]"_fConstants"@"MTLFunctionConstantValues""_cache"{unordered_map<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>, MTLDebugCheckerboardFillHashKey::Hash, std::equal_to<MTLDebugCheckerboardFillHashKey>, std::allocator<std::pair<const MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>>>="__table_"{__hash_table<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, std::__unordered_map_hasher<MTLDebugCheckerboardFillHashKey, std::pair<const MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, MTLDebugCheckerboardFillHashKey::Hash, std::equal_to<MTLDebugCheckerboardFillHashKey>>, std::__unordered_map_equal<MTLDebugCheckerboardFillHashKey, std::pair<const MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, std::equal_to<MTLDebugCheckerboardFillHashKey>, MTLDebugCheckerboardFillHashKey::Hash>, std::allocator<std::pair<const MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLDebugCheckerboardFillHashKey, id<MTLRenderPipelineState>>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}}} _checkerboardRTPipelineCache;
B _storeValidationEnabled;
B _relaxedTextureArrayBindingsEnabled;
B _loadValidationEnabled;
```

## Properties

```
@property (TB,R,V_loadValidationEnabled) loadValidationEnabled;
@property (TB,R,V_storeValidationEnabled) storeValidationEnabled;
@property (TB,R,V_relaxedTextureArrayBindingsEnabled) relaxedTextureArrayBindingsEnabled;
```

## Class methods

```
+[MTLDebugDevice complainAboutSloppyTextureUsage];
```

## Instance methods

```
-[MTLDebugDevice newUncachedIOFileHandleWithURL:compressionMethod:error:];
-[MTLDebugDevice loadDynamicLibrariesForComputeDescriptor:options:error:];
-[MTLDebugDevice newDynamicLibrary:computeDescriptor:error:];
-[MTLDebugDevice newArgumentEncoderWithLayout:];
-[MTLDebugDevice newRenderPipelineStateWithTileDescriptor:options:completionHandler:];
-[MTLDebugDevice newMTL4CommandQueue];
-[MTLDebugDevice newLibraryWithFile:error:];
-[MTLDebugDevice deserializeInstanceAccelerationStructure:fromBytes:primitiveAccelerationStructures:withDescriptor:];
-[MTLDebugDevice setWritableHeapsEnabled:];
-[MTLDebugDevice newDynamicLibraryFromURL:error:];
-[MTLDebugDevice functionHandleWithFunction:resourceIndex:];
-[MTLDebugDevice newCounterSampleBufferWithDescriptor:error:];
-[MTLDebugDevice heapAccelerationStructureSizeAndAlignWithSize:];
-[MTLDebugDevice sizeOfCounterHeapEntry:];
-[MTLDebugDevice newSharedTextureWithHandle:withResourceIndex:];
-[MTLDebugDevice newUncachedIOHandleWithURL:error:];
-[MTLDebugDevice newLateEvalEvent];
-[MTLDebugDevice targetDeviceInfo];
-[MTLDebugDevice functionHandleWithFunction:];
-[MTLDebugDevice newComputePipelineStateWithFunction:completionHandler:];
-[MTLDebugDevice newRenderPipelineStateWithDescriptor:options:completionHandler:];
-[MTLDebugDevice newCommandAllocator];
-[MTLDebugDevice newLibraryWithDescriptor:completionHandler:];
-[MTLDebugDevice newRenderPipelineStateWithMeshDescriptor:options:reflection:error:];
-[MTLDebugDevice newIOFileHandleWithURL:compressionMethod:error:];
-[MTLDebugDevice newIOFileHandleWithURL:error:];
-[MTLDebugDevice newCommandQueueWithDescriptor:];
-[MTLDebugDevice newIOHandleWithURL:error:];
-[MTLDebugDevice newLibraryWithStitchedDescriptor:error:];
-[MTLDebugDevice newSharedEventWithHandle:];
-[MTLDebugDevice newComputePipelineStateWithFunction:options:completionHandler:];
-[MTLDebugDevice newRenderPipelineStateWithMeshDescriptor:completionHandler:];
-[MTLDebugDevice newLibraryWithSource:options:completionHandler:];
-[MTLDebugDevice newRenderPipelineStateWithDescriptor:completionHandler:];
-[MTLDebugDevice newLibraryWithURL:error:];
-[MTLDebugDevice newDynamicLibrary:error:];
-[MTLDebugDevice newDefaultLibraryWithBundle:error:];
-[MTLDebugDevice validateDynamicLibraryURL:error:];
-[MTLDebugDevice newRasterizationRateMapWithDescriptor:];
-[MTLDebugDevice areWritableHeapsEnabled];
-[MTLDebugDevice minimumLinearTextureAlignmentForPixelFormat:];
-[MTLDebugDevice newUncachedIOFileHandleWithURL:error:];
-[MTLDebugDevice newBufferWithLength:options:placementSparsePageSize:];
-[MTLDebugDevice newComputePipelineStateWithImageFilterFunctionsSPI:imageFilterFunctionInfo:error:];
-[MTLDebugDevice newCommandAllocatorWithDescriptor:error:];
-[MTLDebugDevice newTensorWithDescriptor:attachments:error:];
-[MTLDebugDevice tensorSizeAndAlignWithDescriptor:];
-[MTLDebugDevice newLibraryWithStitchedDescriptorSPI:error:];
-[MTLDebugDevice newIOHandleWithURL:compressionType:error:];
-[MTLDebugDevice newTextureWithDescriptor:iosurface:plane:slice:];
-[MTLDebugDevice functionHandleWithBinaryFunction:];
-[MTLDebugDevice newDagStringWithGraphs:];
-[MTLDebugDevice newProfileWithExecutionSize:];
-[MTLDebugDevice newComputePipelineStateWithDescriptor:completionHandler:];
-[MTLDebugDevice newUncachedIOHandleWithURL:compressionType:error:];
-[MTLDebugDevice validateDynamicLibrary:state:error:];
-[MTLDebugDevice newComputePipelineStateWithDescriptor:options:completionHandler:];
-[MTLDebugDevice loadDynamicLibrariesForFunction:insertLibraries:options:error:];
-[MTLDebugDevice newLibraryWithData:error:];
-[MTLDebugDevice newComputePipelineStateWithDescriptor:error:];
-[MTLDebugDevice newComputePipelineStateWithFunction:options:reflection:error:];
-[MTLDebugDevice newAccelerationStructureWithSize:withDescriptor:];
-[MTLDebugDevice newResidencySetWithDescriptor:error:];
-[MTLDebugDevice newLibraryWithStitchedDescriptor:completionHandler:];
-[MTLDebugDevice newTensorWithDescriptor:error:];
-[MTLDebugDevice newRenderPipelineStateWithMeshDescriptor:options:completionHandler:];
-[MTLDebugDevice newMTL4CommandQueueWithDescriptor:error:];
-[MTLDebugDevice newCompilerWithDescriptor:error:];
-[MTLDebugDevice newSharedEvent];
-[MTLDebugDevice newCounterHeapWithDescriptor:error:];
-[MTLDebugDevice newSharedTextureWithDescriptor:];
-[MTLDebugDevice newBinaryArchiveWithDescriptor:error:];
-[MTLDebugDevice newEvent];
-[MTLDebugDevice newArchiveWithURL:error:];
-[MTLDebugDevice newBinaryLibraryWithOptions:url:error:];
-[MTLDebugDevice newCommandQueueWithMaxCommandBufferCount:];
-[MTLDebugDevice newLibraryWithDAG:functions:error:];
-[MTLDebugDevice minLinearTextureAlignmentForPixelFormat:];
-[MTLDebugDevice newLibraryWithImageFilterFunctionsSPI:imageFilterFunctionInfo:error:];
-[MTLDebugDevice newLibraryWithDescriptor:error:];
-[MTLDebugDevice newSharedEventWithMachPort:];
-[MTLDebugDevice newCommandBuffer];
-[MTLDebugDevice newDefaultLibrary];
-[MTLDebugDevice newAccelerationStructureWithBuffer:offset:];
-[MTLDebugDevice newIOHandleWithURL:compressionMethod:error:];
-[MTLDebugDevice newLibraryWithSource:options:error:];
-[MTLDebugDevice newAccelerationStructureWithBuffer:offset:resourceIndex:];
-[MTLDebugDevice newDynamicLibraryWithURL:options:error:];
-[MTLDebugDevice newTextureViewPoolWithDescriptor:error:];
-[MTLDebugDevice newArgumentEncoderWithArguments:];
-[MTLDebugDevice queryTimestampFrequency];
-[MTLDebugDevice deserializePrimitiveAccelerationStructureFromBytes:withDescriptor:];
-[MTLDebugDevice newDynamicLibraryWithURL:error:];
-[MTLDebugDevice newArgumentEncoderWithBufferBinding:];
-[MTLDebugDevice deserializePrimitiveAccelerationStructure:fromBytes:withDescriptor:];
-[MTLDebugDevice newIOCommandQueueWithDescriptor:error:];
-[MTLDebugDevice newSharedTextureWithHandle:];
-[MTLDebugDevice newArgumentTableWithDescriptor:error:];
-[MTLDebugDevice newRenderPipelineStateWithDescriptor:options:reflection:error:];
-[MTLDebugDevice newRenderPipelineStateWithDescriptor:error:];
-[MTLDebugDevice newLibraryWithDescriptorSPI:error:];
-[MTLDebugDevice newComputePipelineStateWithFunction:error:];
-[MTLDebugDevice heapAccelerationStructureSizeAndAlignWithDescriptor:];
-[MTLDebugDevice newComputePipelineStateWithDescriptor:options:reflection:error:];
-[MTLDebugDevice newRenderPipelineStateWithMeshDescriptor:error:];
-[MTLDebugDevice newPipelineLibraryWithFilePath:error:];
-[MTLDebugDevice newCommandQueue];
-[MTLDebugDevice newAccelerationStructureWithSize:];
-[MTLDebugDevice newBufferWithDescriptor:];
-[MTLDebugDevice newAccelerationStructureWithDescriptor:];
-[MTLDebugDevice newIndirectCommandBufferWithDescriptor:maxCommandCount:options:];
-[MTLDebugDevice newAccelerationStructureWithSize:resourceIndex:];
-[MTLDebugDevice newTextureWithDescriptor:];
-[MTLDebugDevice newFence];
-[MTLDebugDevice accelerationStructureSizesWithDescriptor:];
-[MTLDebugDevice newIntersectionFunctionTableWithDescriptor:];
-[MTLDebugDevice newRenderPipelineStateWithTileDescriptor:options:reflection:error:];
-[MTLDebugDevice deserializeInstanceAccelerationStructureFromBytes:primitiveAccelerationStructures:withDescriptor:];
-[MTLDebugDevice newBufferWithBytesNoCopy:length:options:deallocator:];
-[MTLDebugDevice newBufferWithLength:options:];
-[MTLDebugDevice newDepthStencilStateWithDescriptor:];
-[MTLDebugDevice newHeapWithDescriptor:];
-[MTLDebugDevice newSamplerStateWithDescriptor:];
-[MTLDebugDevice newTextureLayoutWithDescriptor:isHeapOrBufferBacked:];
-[MTLDebugDevice newTextureWithBytesNoCopy:length:descriptor:deallocator:];
-[MTLDebugDevice newTextureWithDescriptor:iosurface:plane:];
-[MTLDebugDevice heapBufferSizeAndAlignWithLength:options:];
-[MTLDebugDevice heapTextureSizeAndAlignWithDescriptor:];
-[MTLDebugDevice newBufferWithBytes:length:options:];
-[MTLDebugDevice newVisibleFunctionTableWithDescriptor:];
-[MTLDebugDevice newBufferWithIOSurface:];
-[MTLDebugDevice newRenderPipelineStateWithTileDescriptor:completionHandler:];
-[MTLDebugDevice newRenderPipelineStateWithTileDescriptor:error:];
-[MTLDebugDevice initWithBaseObject:parent:];
-[MTLDebugDevice _newComputePipelineStateWithFunction:options:completionHandler:];
-[MTLDebugDevice _newRenderPipelineStateWithDescriptor:options:reflection:error:];
-[MTLDebugDevice getDynamicLibraryForBaseObject:];
-[MTLDebugDevice _newComputePipelineStateWithDescriptor:options:completionHandler:];
-[MTLDebugDevice _newComputePipelineStateWithDescriptor:options:reflection:error:];
-[MTLDebugDevice _newComputePipelineStateWithFunction:options:reflection:error:];
-[MTLDebugDevice _newRenderPipelineStateWithDescriptor:options:completionHandler:];
-[MTLDebugDevice _newRenderPipelineStateWithMeshDescriptor:options:completionHandler:];
-[MTLDebugDevice _newRenderPipelineStateWithMeshDescriptor:options:reflection:error:];
-[MTLDebugDevice _newRenderPipelineStateWithTileDescriptor:options:completionHandler:];
-[MTLDebugDevice _newRenderPipelineStateWithTileDescriptor:options:reflection:error:];
-[MTLDebugDevice addReferenceTrackingCommandBuffer:];
-[MTLDebugDevice clearRenderEncoder:writeMask:withCheckerboard:];
-[MTLDebugDevice getDepthStencilStateForBaseObject:descriptor:];
-[MTLDebugDevice getFunctionForBaseObject:library:];
-[MTLDebugDevice getFunctionForBaseObject:library:onInit:];
-[MTLDebugDevice getSamplerStateForBaseObject:descriptor:];
-[MTLDebugDevice loadValidationEnabled];
-[MTLDebugDevice notifyExternalReferencesNonZeroOnDealloc:];
-[MTLDebugDevice notifySamplerStateDeallocated:];
-[MTLDebugDevice relaxedTextureArrayBindingsEnabled];
-[MTLDebugDevice removeReferenceTrackingCommandBuffer:];
-[MTLDebugDevice storeValidationEnabled];
-[MTLDebugDevice validateAddressRanges:expectedTotalSize:context:];
-[MTLDebugDevice validateImageblockTypes:reflection:context:];
-[MTLDebugDevice validateLinkedFunctions:context:];
-[MTLDebugDevice validateMemorylessResource:context:];
-[MTLDebugDevice validateNewBufferArgs:options:context:];
-[MTLDebugDevice validateRaytracing];
-[MTLDebugDevice validateResourceOptions:isTexture:isIOSurface:context:];
```
