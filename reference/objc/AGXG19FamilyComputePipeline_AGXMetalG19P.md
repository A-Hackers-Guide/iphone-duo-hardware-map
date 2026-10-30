# `AGXG19FamilyComputePipeline`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLComputePipelineState`
- Protocols: `MTLComputePipelineStateSPI`
- 5 instance variables, 26 properties, 30 instance methods, 0 class methods

## Instance variables

```
{ComputePipeline="scs_per_shader_config_table"{unique_ptr<AGX::HeapBuffer, std::default_delete<AGX::HeapBuffer>>=""{?="__ptr_"^{HeapBuffer}}}"dora_state_buffer"@"AGXG19FamilyBuffer""owns_variants"B"compute_variant"^{ComputeProgramVariant}"supports_indirect_command_buffers"B"requires_binary_linking_bindings"B"descendent_pipeline"B"max_call_stack_depth"I"optimize_for_persistent_kernel"B"sfe_state"{ForwardProgressPipelineState="overrideForwardProgressUsageMode"{optional<_AGCForwardProgressMode>=""(?="__null_state_"c"__val_"i)"__engaged_"B}"persistentKernelMode"B}"ei_state"{ExecuteIndirectPipelineState="pipeline_state_gpu_address"Q"allocation"{Allocation="buffer_"{BufferView<unsigned char>="address"{AddressView<unsigned char>="gpu"Q"cpu"*}"size"Q}"resource_"^{_Resource}"heap_"^v"element_"{tuple<>=}}}"resource_indirection_heap_allocation"{Allocation="index"I"size"I"pool"^v"directly_assigned"B}"loader_runtime_state"{RuntimeState="got"{shared_ptr<AGX::HeapBuffer>="__ptr_"^{HeapBuffer}"__cntrl_"^{__shared_weak_count}}"global_constructors"{shared_ptr<AGX::HeapBuffer>="__ptr_"^{HeapBuffer}"__cntrl_"^{__shared_weak_count}}"max_temporary_register_count"I"mxu_operand_gpr_bytes"I"mxu_accumulator_gpr_bytes"I"total_spill_buffer_bytes"I"base_spill_buffer_bytes"I"entry_function_group_non_main_spill_buffer_bytes"I"total_ipr_buffer_bytes"I"base_ipr_buffer_bytes"I"max_call_stack_depth"I"max_spill_per_function_bytes"I"max_spill_per_stateless_pso_function_bytes"I"max_ipr_per_function_bytes"I"tls_alloc_size"I"total_tls_size"I"global_constructor_count"I"ray_payload_size_align"{RayPayloadSizeAlignImpl<AGX::HAL400::Classes>="user_payload_align"I"max_traversal_depth"I"cached_scs_layout"{CachedScsLayout="scs_layout"{ScsLayoutGen3="traversal_depth"b16"max_instance_levels"b8"num_cliques"b8"per_ray_user_payload_size"b16"per_ray_driver_payload_size"b16}"scs_section_offsets"{array<unsigned int, 12UL>="__elems_"[12I]}"scs_section_sizes"{array<unsigned int, 12UL>="__elems_"[12I]}"leaf_ptrs_scs_stride"I"total_scs_size"I}}"ray_ifb_payload_variants"I"has_side_effects"B"uses_dpg"B"reads_tgsrs"B"requires_builtin_state"B"has_texture_stores"B"got_size"Q"max_lm_spill_size"I"max_sgpr_lm_size"I"entry_spill_buffer_bytes"I"entry_ipr_bytes"I"max_tptg_from_dylibs"I"allocate_from_ei_heap"B"forward_progress_usage_is_forced"B"inferred_forward_progress_usage"i"global_binding_table_layout"{GlobalBindingTableLayout="sampler_state_registers_count"I"global_binding_buffers"{ArgumentMask<64UL>="mask"Q}"global_binding_textures"{ArgumentMask<128UL>="mask"[2Q]}"global_binding_samplers"{ArgumentMask<64UL>="mask"Q}"global_binding_tgbuffers"{ArgumentMask<64UL>="mask"Q}}}"dylib_resources"{PipelineDylibResources<AGX::HAL400::ObjClasses, AGX::HAL400::Classes, AGX::ICBType::Compute>="dylibs"{vector<std::shared_ptr<AGX::HAL400::DynamicLibrary>, std::allocator<std::shared_ptr<AGX::HAL400::DynamicLibrary>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}}}"max_wg_size"I"function_handle_map"{unordered_map<id<MTLFunction>, RetainedObjCPointer<AGXG19FamilyFunctionHandle *>, std::hash<id<MTLFunction>>, std::equal_to<id<MTLFunction>>, std::allocator<std::pair<const id<MTLFunction>, RetainedObjCPointer<AGXG19FamilyFunctionHandle *>>>>="__table_"{__hash_table<std::__hash_value_type<id<MTLFunction>, RetainedObjCPointer<AGXG19FamilyFunctionHandle *>>, std::__unordered_map_hasher<id<MTLFunction>, std::pair<const id<MTLFunction>, RetainedObjCPointer<AGXG19FamilyFunctionHandle *>>, std::hash<id<MTLFunction>>, std::equal_to<id<MTLFunction>>>, std::__unordered_map_equal<id<MTLFunction>, std::pair<const id<MTLFunction>, RetainedObjCPointer<AGXG19FamilyFunctionHandle *>>, std::equal_to<id<MTLFunction>>, std::hash<id<MTLFunction>>>, std::allocator<std::pair<const id<MTLFunction>, RetainedObjCPointer<AGXG19FamilyFunctionHandle *>>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<id<MTLFunction>, RetainedObjCPointer<AGXG19FamilyFunctionHandle *>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<id<MTLFunction>, RetainedObjCPointer<AGXG19FamilyFunctionHandle *>>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<id<MTLFunction>, RetainedObjCPointer<AGXG19FamilyFunctionHandle *>>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<id<MTLFunction>, RetainedObjCPointer<AGXG19FamilyFunctionHandle *>>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}}"name_to_function_map"{unordered_map<std::string, id<MTLFunction>, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, id<MTLFunction>>>>="__table_"{__hash_table<std::__hash_value_type<std::string, id<MTLFunction>>, std::__unordered_map_hasher<std::string, std::pair<const std::string, id<MTLFunction>>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, id<MTLFunction>>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, id<MTLFunction>>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, id<MTLFunction>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, id<MTLFunction>>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, id<MTLFunction>>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, id<MTLFunction>>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}}"vft_set"{shared_ptr<AGX::FunctionTableSet<AGXG19FamilyVisibleFunctionTable>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}}"clone_visible_function_table_heap"^{VisibleFunctionTableHeap}"ift_set"{shared_ptr<AGX::FunctionTableSet<AGXG19FamilyUserIntersectionFunctionTable>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}}"intersection_pipeline_sets"{vector<std::shared_ptr<AGX::HAL400::IntersectionPipelineSet>, std::allocator<std::shared_ptr<AGX::HAL400::IntersectionPipelineSet>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}}"ift_spill_info"{shared_ptr<AGX::HAL400::SpillInfo>="__ptr_"^{SpillInfo}"__cntrl_"^{__shared_weak_count}}} _impl;
@"AGXG19FamilyComputeProgram" _cp;
@"AGXG19FamilyComputePipeline" _basePipeline;
@"MTLComputePipelineReflection" _reflection;
@"NSObject<OS_dispatch_data>" _reflectionData;
```

## Properties

```
@property (TQ,R) maxTotalThreadsPerThreadgroup;
@property (TQ,R) threadExecutionWidth;
@property (TQ,R) staticThreadgroupMemoryLength;
@property (TQ,R) allocatedSize;
@property (T@"MTLComputePipelineReflection",&,V_reflection) reflection;
@property (T@"NSObject<OS_dispatch_data>",&,V_reflectionData) reflectionData;
@property (TQ,R) globalConstantsBase;
@property (TQ,R) globalConstantsSize;
@property (Tq,R) textureWriteRoundingMode;
@property (TQ,?,R,N) resourceIndex;
@property (TQ,?,R,N) gpuAddress;
@property (TQ,R) uniqueIdentifier;
@property (T@"MTLDebugInstrumentationData",R,&,N) debugInstrumentationData;
@property (TQ,R) gpuHandle;
@property (Tq,R,N) shaderValidationState;
@property (T@"NSString",R) label;
@property (T@"<MTLDevice>",R) device;
@property (TB,R) supportIndirectCommandBuffers;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (Tq,R,N) shaderValidation;
@property (T{?=QQQ},R) requiredThreadsPerThreadgroup;
@property (Tq,R) forwardProgressUsage;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AGXG19FamilyComputePipeline functionHandleWithFunction:];
-[AGXG19FamilyComputePipeline resourceIndex];
-[AGXG19FamilyComputePipeline functionHandleWithBinaryFunction:];
-[AGXG19FamilyComputePipeline initWithDevice:pipelineStateDescriptor:];
-[AGXG19FamilyComputePipeline allocatedSize];
-[AGXG19FamilyComputePipeline dealloc];
-[AGXG19FamilyComputePipeline uniqueIdentifier];
-[AGXG19FamilyComputePipeline imageblockMemoryLengthForDimensions:];
-[AGXG19FamilyComputePipeline newIntersectionFunctionTableWithDescriptor:];
-[AGXG19FamilyComputePipeline maxTotalThreadsPerThreadgroup];
-[AGXG19FamilyComputePipeline pipelineBinaries];
-[AGXG19FamilyComputePipeline initWithParent:];
-[AGXG19FamilyComputePipeline reflectionData];
-[AGXG19FamilyComputePipeline forwardProgressUsage];
-[AGXG19FamilyComputePipeline reflection];
-[AGXG19FamilyComputePipeline threadExecutionWidth];
-[AGXG19FamilyComputePipeline functionHandleWithName:];
-[AGXG19FamilyComputePipeline newComputePipelineStateWithAdditionalBinaryFunctions:error:];
-[AGXG19FamilyComputePipeline newComputePipelineStateWithBinaryFunctions:error:];
-[AGXG19FamilyComputePipeline newVisibleFunctionTableWithDescriptor:];
-[AGXG19FamilyComputePipeline recommendedPersistentThreadgroupsPerGridForThreadsPerThreadgroup:];
-[AGXG19FamilyComputePipeline staticThreadgroupMemoryLength];
-[AGXG19FamilyComputePipeline functionReflectionWithFunctionDescriptor:];
-[AGXG19FamilyComputePipeline getComputeKernelTelemetryID];
-[AGXG19FamilyComputePipeline globalConstantsBase];
-[AGXG19FamilyComputePipeline globalConstantsSize];
-[AGXG19FamilyComputePipeline newComputePipelineStateWithAdditionalBinaryFunctions:resourceIndices:error:];
-[AGXG19FamilyComputePipeline setReflection:];
-[AGXG19FamilyComputePipeline imageBlockMemoryLengthForDimensions:];
-[AGXG19FamilyComputePipeline setReflectionData:];
```
