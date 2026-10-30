# `MTLLegacySVDevice`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsDevice`
- 22 instance variables, 10 properties, 135 instance methods, 0 class methods

## Instance variables

```
{LegacySVMetalBufferHeap="_mutex"{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}}"_buffers"{vector<id<MTLBuffer>, std::allocator<id<MTLBuffer>>>="__begin_"^@"__end_"^@""{?="__cap_"^@}}"_freeList"{vector<unsigned int, std::allocator<unsigned int>>="__begin_"^I"__end_"^I""{?="__cap_"^I}}"_currentFreeIndex"i"_totalMemoryAllocated"Q"_totalMemoryInUse"Q"_bufferLength"Q"_device"@"MTLLegacySVDevice"} bufferHeap;
{Options="version"I"mode"i"accessTypes"i"failMode"i"maxTrackedResourcesMultiplier"I""{?="enableForPerPSO"b1"enableReporting"b1"packPointerAddresses"b1"unpackPointerAddress"b1"forceInline"b1"enableBacktracking"b1"optimizeConstantDeref"b1"skipVertexFetchLoads"b1"enableGEPOptimization"b1"enableRuntimeStacktrace"b1"enableBoundsChecking"b1"runStandardOptimizations"b1"backtrackFailuresAssumeSafe"b1"pageDataIs32bitLength"b1"forceUnrollLoops"b1"mergeAccessChecks"b1"convertToAB"b1"arraysOfBuffersAB"b1"noInlineTrivialFunctions"b1"unrollMemCpyWA"b1"checkGlobalConstants"b1"enableTextureChecks"b1"demoteGlobalConstantsToArg"b1"argumentPointerIndirection"b1"enableThreadgroupMemoryChecks"b1"mergeThreadgroupGlobals"b1"mergeThreadgroupArguments"b1"tagThreadgroupPointers"b1"enableJumpThreading"b1"enableICBSupport"b1"enableGlobalRelocations"b1"enableTrapReporting"b1"enableRaytracing"b1"enableResourceUsageValidation"b1"enableStackOverflow"b1"enableDumpToStderr"b1"enableAccelerationStructureChecks"b1"enableAddressSpaceValidation"b1"enableRelaxedTextureArrayBindings"b1"enableNumericsChecks"b1"enableDeepResidencyCheck"b1"enableTensorValidation"b1"enableTextureOffsetValidation"b1"enableBVHResidencyCheck"b1"enableYieldChecks"b1"enableTagPreservation"b1}} boundsCheckOptions;
{LegacySVDeviceOptions="retainReflection"b1"retainPSOFunctions"b1"abortOnFault"b1"enableDumpToStderr"b1} deviceOptions;
{LegacySVBufferDescriptorHeap="s"{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}}"_freeIndexList"{vector<unsigned int, std::allocator<unsigned int>>="__begin_"^I"__end_"^I""{?="__cap_"^I}}"_bufferList"{vector<MTLLegacySVBuffer *, std::allocator<MTLLegacySVBuffer *>>="__begin_"^@"__end_"^@""{?="__cap_"^@}}"_freeIndex"Q"_argumentEncoder"@"<MTLArgumentEncoder>""_descriptorHeap"@"<MTLBuffer>"} globalBufferHeap;
{LegacySVConstantBufferCache="_totalUsedMemory"Q"_accessMutex"{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}}"_cache"{unordered_map<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value, LegacySVConstantBufferCache::Key::Hash, std::equal_to<LegacySVConstantBufferCache::Key>, std::allocator<std::pair<const LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>>>="__table_"{__hash_table<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, std::__unordered_map_hasher<LegacySVConstantBufferCache::Key, std::pair<const LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, LegacySVConstantBufferCache::Key::Hash, std::equal_to<LegacySVConstantBufferCache::Key>>, std::__unordered_map_equal<LegacySVConstantBufferCache::Key, std::pair<const LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, std::equal_to<LegacySVConstantBufferCache::Key>, LegacySVConstantBufferCache::Key::Hash>, std::allocator<std::pair<const LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<LegacySVConstantBufferCache::Key, LegacySVConstantBufferCache::Value>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}}"_device"@"MTLLegacySVDevice"} constantBufferCache;
{LegacySVGlobalResidentBufferList="_iteration"I"_accessMutex"{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}}"_bufferList"{list<id<MTLBuffer>, std::allocator<id<MTLBuffer>>>="__end_"{__list_node_base<id<MTLBuffer>, void *>="__prev_"^v"__next_"^v}""{?="__size_"Q}}} globalICBBufferResidentList;
@"<MTLBuffer>" uncheckedBuffer;
@"NSSet" psoEnableChecksList;
@"NSSet" psoDisableChecksList;
@"NSData" _boundsCheckOptionsData;
@"NSMutableArray" _argumentDescriptors;
{once_flag="__state_"Q} _deviceInitFlag;
{once_flag="__state_"Q} _icbPipelineInit;
@"<MTLRenderPipelineState>" _icbInheritVertexPipelineState;
@"<MTLRenderPipelineState>" _icbInheritNoneVertexPipelineState;
@"<MTLRenderPipelineState>" _icbInheritBuffersVertexPipelineState;
@"<MTLDepthStencilState>" _icbDepthStencilState;
@"<MTLComputePipelineState>" _icbInheritComputePipelineState;
@"<MTLComputePipelineState>" _icbInheritNoneComputePipelineState;
@"<MTLComputePipelineState>" _icbInheritBuffersComputePipelineState;
@"<MTLComputePipelineState>" _icbInheritBothComputePipelineState;
@"<MTLComputePipelineState>" _accelerationStructureComputePipelineState;
```

## Properties

```
@property (T@"<MTLRenderPipelineState>",R,N) ICB_Inherit_PSO_VertexPipelineState;
@property (T@"<MTLRenderPipelineState>",R,N) ICB_Inherit_None_VertexPipelineState;
@property (T@"<MTLRenderPipelineState>",R,N) ICB_Inherit_Buffers_VertexPipelineState;
@property (T@"<MTLDepthStencilState>",R,N) ICB_DepthStencilState;
@property (T@"<MTLComputePipelineState>",R,N) ICB_Inherit_PSO_ComputePipelineState;
@property (T@"<MTLComputePipelineState>",R,N) ICB_Inherit_None_ComputePipelineState;
@property (T@"<MTLComputePipelineState>",R,N) ICB_Inherit_Buffers_ComputePipelineState;
@property (T@"<MTLComputePipelineState>",R,N) ICB_Inherit_Both_ComputePipelineState;
@property (T@"<MTLComputePipelineState>",R,N,V_accelerationStructureComputePipelineState) accelerationStructureComputePipelineState;
@property (TB,R,N) supportsResourceUsageValidation;
```

## Instance methods

```
-[MTLLegacySVDevice loadDynamicLibrariesForComputeDescriptor:options:error:];
-[MTLLegacySVDevice supportsGFXIndirectCommandBuffers];
-[MTLLegacySVDevice loadDynamicLibrariesForComputeDescriptor:error:];
-[MTLLegacySVDevice newDynamicLibrary:computeDescriptor:error:];
-[MTLLegacySVDevice supportsSharedFunctionTables];
-[MTLLegacySVDevice supportsFunctionPointersFromRender];
-[MTLLegacySVDevice newArgumentEncoderWithLayout:];
-[MTLLegacySVDevice newRenderPipelineStateWithTileDescriptor:options:completionHandler:];
-[MTLLegacySVDevice supportsForkJoin];
-[MTLLegacySVDevice newLibraryWithFile:error:];
-[MTLLegacySVDevice setWritableHeapsEnabled:];
-[MTLLegacySVDevice newDynamicLibraryFromURL:error:];
-[MTLLegacySVDevice loadDynamicLibrariesForFunction:insertLibraries:error:];
-[MTLLegacySVDevice supportsBinaryArchives];
-[MTLLegacySVDevice newComputePipelineStateWithFunction:completionHandler:];
-[MTLLegacySVDevice supportsGlobalVariableBindings];
-[MTLLegacySVDevice newRenderPipelineStateWithDescriptor:options:completionHandler:];
-[MTLLegacySVDevice newLibraryWithDescriptor:completionHandler:];
-[MTLLegacySVDevice newRenderPipelineStateWithMeshDescriptor:options:reflection:error:];
-[MTLLegacySVDevice newCommandQueueWithDescriptor:];
-[MTLLegacySVDevice newLibraryWithStitchedDescriptor:error:];
-[MTLLegacySVDevice supportsRenderDynamicLibraries];
-[MTLLegacySVDevice newComputePipelineStateWithFunction:options:completionHandler:];
-[MTLLegacySVDevice newRenderPipelineStateWithMeshDescriptor:completionHandler:];
-[MTLLegacySVDevice newLibraryWithSource:options:completionHandler:];
-[MTLLegacySVDevice newRenderPipelineStateWithDescriptor:completionHandler:];
-[MTLLegacySVDevice newLibraryWithURL:error:];
-[MTLLegacySVDevice newDynamicLibrary:error:];
-[MTLLegacySVDevice newDefaultLibraryWithBundle:error:];
-[MTLLegacySVDevice areWritableHeapsEnabled];
-[MTLLegacySVDevice newLibraryWithStitchedDescriptorSPI:error:];
-[MTLLegacySVDevice newTextureWithDescriptor:iosurface:plane:slice:];
-[MTLLegacySVDevice newDagStringWithGraphs:];
-[MTLLegacySVDevice newComputePipelineStateWithDescriptor:completionHandler:];
-[MTLLegacySVDevice newComputePipelineStateWithDescriptor:options:completionHandler:];
-[MTLLegacySVDevice loadDynamicLibrariesForFunction:insertLibraries:options:error:];
-[MTLLegacySVDevice newLibraryWithData:error:];
-[MTLLegacySVDevice newComputePipelineStateWithDescriptor:error:];
-[MTLLegacySVDevice newComputePipelineStateWithFunction:options:reflection:error:];
-[MTLLegacySVDevice newAccelerationStructureWithSize:withDescriptor:];
-[MTLLegacySVDevice newResidencySetWithDescriptor:error:];
-[MTLLegacySVDevice newLibraryWithStitchedDescriptor:completionHandler:];
-[MTLLegacySVDevice newRenderPipelineStateWithMeshDescriptor:options:completionHandler:];
-[MTLLegacySVDevice supportsArgumentBuffersTier2];
-[MTLLegacySVDevice newSharedTextureWithDescriptor:];
-[MTLLegacySVDevice newBinaryArchiveWithDescriptor:error:];
-[MTLLegacySVDevice supportsStackOverflowErrorCode];
-[MTLLegacySVDevice newBinaryLibraryWithOptions:url:error:];
-[MTLLegacySVDevice supportsRaytracingFromRender];
-[MTLLegacySVDevice newCommandQueueWithMaxCommandBufferCount:];
-[MTLLegacySVDevice newLibraryWithDAG:functions:error:];
-[MTLLegacySVDevice newLibraryWithImageFilterFunctionsSPI:imageFilterFunctionInfo:error:];
-[MTLLegacySVDevice newArgumentEncoderWithArguments:structType:];
-[MTLLegacySVDevice supportsRaytracing];
-[MTLLegacySVDevice newLibraryWithDescriptor:error:];
-[MTLLegacySVDevice newDefaultLibrary];
-[MTLLegacySVDevice newAccelerationStructureWithBuffer:offset:];
-[MTLLegacySVDevice newLibraryWithSource:options:error:];
-[MTLLegacySVDevice newAccelerationStructureWithBuffer:offset:resourceIndex:];
-[MTLLegacySVDevice newDynamicLibraryWithURL:options:error:];
-[MTLLegacySVDevice newArgumentEncoderWithArguments:];
-[MTLLegacySVDevice supportsCMPIndirectCommandBuffers];
-[MTLLegacySVDevice supportsPipelineLibraries];
-[MTLLegacySVDevice deserializePrimitiveAccelerationStructureFromBytes:withDescriptor:];
-[MTLLegacySVDevice newDynamicLibraryWithURL:error:];
-[MTLLegacySVDevice newArgumentEncoderWithBufferBinding:];
-[MTLLegacySVDevice newSharedTextureWithHandle:];
-[MTLLegacySVDevice newRenderPipelineStateWithDescriptor:options:reflection:error:];
-[MTLLegacySVDevice supportsRayTracingPerPrimitiveData];
-[MTLLegacySVDevice newRenderPipelineStateWithDescriptor:error:];
-[MTLLegacySVDevice newLibraryWithDescriptorSPI:error:];
-[MTLLegacySVDevice newComputePipelineStateWithFunction:error:];
-[MTLLegacySVDevice newComputePipelineStateWithDescriptor:options:reflection:error:];
-[MTLLegacySVDevice newRenderPipelineStateWithMeshDescriptor:error:];
-[MTLLegacySVDevice newCommandQueue];
-[MTLLegacySVDevice newAccelerationStructureWithSize:];
-[MTLLegacySVDevice newBufferWithDescriptor:];
-[MTLLegacySVDevice newAccelerationStructureWithDescriptor:];
-[MTLLegacySVDevice newIndirectCommandBufferWithDescriptor:maxCommandCount:options:];
-[MTLLegacySVDevice newAccelerationStructureWithSize:resourceIndex:];
-[MTLLegacySVDevice dealloc];
-[MTLLegacySVDevice newTextureWithDescriptor:];
-[MTLLegacySVDevice accelerationStructureSizesWithDescriptor:];
-[MTLLegacySVDevice newIntersectionFunctionTableWithDescriptor:];
-[MTLLegacySVDevice newRenderPipelineStateWithTileDescriptor:options:reflection:error:];
-[MTLLegacySVDevice deserializeInstanceAccelerationStructureFromBytes:primitiveAccelerationStructures:withDescriptor:];
-[MTLLegacySVDevice newLibraryWithCIFilters:imageFilterFunctionInfo:error:];
-[MTLLegacySVDevice newBufferWithBytesNoCopy:length:options:deallocator:];
-[MTLLegacySVDevice newBufferWithLength:options:];
-[MTLLegacySVDevice newHeapWithDescriptor:];
-[MTLLegacySVDevice newTextureWithBytesNoCopy:length:descriptor:deallocator:];
-[MTLLegacySVDevice newTextureWithDescriptor:iosurface:plane:];
-[MTLLegacySVDevice newBufferWithBytes:length:options:];
-[MTLLegacySVDevice newVisibleFunctionTableWithDescriptor:];
-[MTLLegacySVDevice newBufferWithIOSurface:];
-[MTLLegacySVDevice newBufferWithBytesNoCopy:length:options:gpuAddress:deallocator:];
-[MTLLegacySVDevice newBufferWithBytes:length:options:gpuAddress:];
-[MTLLegacySVDevice newBufferWithLength:options:gpuAddress:];
-[MTLLegacySVDevice newLibraryWithCIFiltersForComputePipeline:imageFilterFunctionInfo:error:];
-[MTLLegacySVDevice newRenderPipelineStateWithTileDescriptor:completionHandler:];
-[MTLLegacySVDevice newRenderPipelineStateWithTileDescriptor:error:];
-[MTLLegacySVDevice initWithBaseObject:parent:];
-[MTLLegacySVDevice ICB_DepthStencilState];
-[MTLLegacySVDevice ICB_Inherit_Buffers_ComputePipelineState];
-[MTLLegacySVDevice ICB_Inherit_Buffers_VertexPipelineState];
-[MTLLegacySVDevice ICB_Inherit_PSO_ComputePipelineState];
-[MTLLegacySVDevice ICB_Inherit_PSO_VertexPipelineState];
-[MTLLegacySVDevice ICB_Inherit_Both_ComputePipelineState];
-[MTLLegacySVDevice ICB_Inherit_None_ComputePipelineState];
-[MTLLegacySVDevice ICB_Inherit_None_VertexPipelineState];
-[MTLLegacySVDevice getDynamicLibraryForBaseObject:];
-[MTLLegacySVDevice supportsResourceUsageValidation];
-[MTLLegacySVDevice _modifyCompileOptions:];
-[MTLLegacySVDevice _modifyComputePipelineDescriptor:options:];
-[MTLLegacySVDevice _modifyMeshRenderPipelineDescriptor:options:];
-[MTLLegacySVDevice _modifyRenderPipelineDescriptor:options:];
-[MTLLegacySVDevice _modifyTilePipelineDescriptor:options:];
-[MTLLegacySVDevice _prepareBinaryLinkedFunctions:];
-[MTLLegacySVDevice _prepareInsertLibraries:];
-[MTLLegacySVDevice accelerationStructureComputePipelineState];
-[MTLLegacySVDevice getFunctionForBaseObject:library:];
-[MTLLegacySVDevice modifyFunctionDescriptor:];
-[MTLLegacySVDevice newInternalBufferWithLength:options:];
-[MTLLegacySVDevice newModifyPluginData:];
-[MTLLegacySVDevice newStageArgumentBuffer];
-[MTLLegacySVDevice newStageBufferArgumentEncoder];
-[MTLLegacySVDevice onComputePipelineCreated:];
-[MTLLegacySVDevice onRenderPipelineCreated:];
-[MTLLegacySVDevice setGpuCompilerSPIOptionShaderValidation:options:];
-[MTLLegacySVDevice unwrapAndModifyComputePipelineDescriptor:options:];
-[MTLLegacySVDevice unwrapAndModifyMeshRenderPipelineDescriptor:options:];
-[MTLLegacySVDevice unwrapAndModifyRenderPipelineDescriptor:options:];
-[MTLLegacySVDevice unwrapAndModifyTileRenderPipelineDescriptor:options:];
-[MTLLegacySVDevice unwrapStitchedLibraryDescriptor:];
-[MTLLegacySVDevice validateRaytracing];
```
