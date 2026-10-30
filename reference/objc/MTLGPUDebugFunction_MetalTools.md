# `MTLGPUDebugFunction`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsFunction`
- 3 instance variables, 0 properties, 12 instance methods, 3 class methods

## Instance variables

```
@"MTLGPUDebugImageData" data;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _argumentLayoutsMutex;
{unordered_map<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>>>="__table_"{__hash_table<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, std::__unordered_map_hasher<unsigned int, std::pair<const unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::pair<const unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::pair<const unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unique_ptr<GPUDebugArgumentEncoderLayout>>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _argumentLayouts;
```

## Class methods

```
+[MTLGPUDebugFunction convertUserType:];
+[MTLGPUDebugFunction internalArrayTypeFromUserArrayType:];
+[MTLGPUDebugFunction internalStructTypeFromUserStructType:];
```

## Instance methods

```
-[MTLGPUDebugFunction dealloc];
-[MTLGPUDebugFunction newArgumentEncoderWithBufferIndex:reflection:pipelineLibrary:];
-[MTLGPUDebugFunction newArgumentEncoderWithBufferIndex:];
-[MTLGPUDebugFunction newArgumentEncoderWithBufferIndex:reflection:];
-[MTLGPUDebugFunction newArgumentEncoderWithBufferIndex:reflection:binaryArchives:];
-[MTLGPUDebugFunction newArgumentEncoderWithBufferIndex:pipelineLibrary:];
-[MTLGPUDebugFunction _initImageData];
-[MTLGPUDebugFunction initWithFunction:library:];
-[MTLGPUDebugFunction newArgumentEncoderWithBufferIndex:reflection:pipelineLibrary:binaryArchives:];
-[MTLGPUDebugFunction prepareForBinaryFunctionUsage];
-[MTLGPUDebugFunction prepareForComputePipelineUsage];
-[MTLGPUDebugFunction prepareForRenderPipelineUsage];
```
