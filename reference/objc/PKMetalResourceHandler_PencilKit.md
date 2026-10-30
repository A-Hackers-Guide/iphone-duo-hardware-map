# `PKMetalResourceHandler`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 40 instance variables, 0 properties, 1 instance methods, 1 class methods

## Instance variables

```
@"<MTLComputePipelineState>" _particleShaderKernelPipelineState;
@"<MTLComputePipelineState>" _particleShaderKernelPipelineStateWithVariableSpacing;
@"<MTLComputePipelineState>" _paintShaderKernelPipelineState;
@"<MTLComputePipelineState>" _sdfPenShaderKernelPipelineState;
@"<MTLTexture>" _sdfPenMaxHeightLookupTexture;
@"<MTLTexture>" _sdfPenEllipseLookupTexture;
@"<MTLComputePipelineState>" _paintShaderKernelPipelineStateWithLiveStrokeMode;
@"<MTLComputePipelineState>" _paintShaderKernelPipelineStateWithLiveStrokeParticles;
@"<MTLBuffer>" _cachedQuadVertexBuffer;
@"<MTLBuffer>" _cachedQuadTexCoordBuffer;
@"NSMutableDictionary" _inkTextures;
{unordered_map<(anonymous namespace)::PKMetalShaderKey, PKMetalShader *, (anonymous namespace)::PKMetalResourceHandlerHashFunctions, std::equal_to<(anonymous namespace)::PKMetalShaderKey>, std::allocator<std::pair<const (anonymous namespace)::PKMetalShaderKey, PKMetalShader *>>>="__table_"{__hash_table<std::__hash_value_type<(anonymous namespace)::PKMetalShaderKey, PKMetalShader *>, std::__unordered_map_hasher<(anonymous namespace)::PKMetalShaderKey, std::pair<const (anonymous namespace)::PKMetalShaderKey, PKMetalShader *>, (anonymous namespace)::PKMetalResourceHandlerHashFunctions, std::equal_to<(anonymous namespace)::PKMetalShaderKey>>, std::__unordered_map_equal<(anonymous namespace)::PKMetalShaderKey, std::pair<const (anonymous namespace)::PKMetalShaderKey, PKMetalShader *>, std::equal_to<(anonymous namespace)::PKMetalShaderKey>, (anonymous namespace)::PKMetalResourceHandlerHashFunctions>, std::allocator<std::pair<const (anonymous namespace)::PKMetalShaderKey, PKMetalShader *>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<(anonymous namespace)::PKMetalShaderKey, PKMetalShader *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<(anonymous namespace)::PKMetalShaderKey, PKMetalShader *>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<(anonymous namespace)::PKMetalShaderKey, PKMetalShader *>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<(anonymous namespace)::PKMetalShaderKey, PKMetalShader *>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _uberShaders;
{unordered_map<(anonymous namespace)::PKSixChannelShaderKey, PKMetalShader *, (anonymous namespace)::PKMetalResourceHandlerHashFunctions, std::equal_to<(anonymous namespace)::PKSixChannelShaderKey>, std::allocator<std::pair<const (anonymous namespace)::PKSixChannelShaderKey, PKMetalShader *>>>="__table_"{__hash_table<std::__hash_value_type<(anonymous namespace)::PKSixChannelShaderKey, PKMetalShader *>, std::__unordered_map_hasher<(anonymous namespace)::PKSixChannelShaderKey, std::pair<const (anonymous namespace)::PKSixChannelShaderKey, PKMetalShader *>, (anonymous namespace)::PKMetalResourceHandlerHashFunctions, std::equal_to<(anonymous namespace)::PKSixChannelShaderKey>>, std::__unordered_map_equal<(anonymous namespace)::PKSixChannelShaderKey, std::pair<const (anonymous namespace)::PKSixChannelShaderKey, PKMetalShader *>, std::equal_to<(anonymous namespace)::PKSixChannelShaderKey>, (anonymous namespace)::PKMetalResourceHandlerHashFunctions>, std::allocator<std::pair<const (anonymous namespace)::PKSixChannelShaderKey, PKMetalShader *>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<(anonymous namespace)::PKSixChannelShaderKey, PKMetalShader *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<(anonymous namespace)::PKSixChannelShaderKey, PKMetalShader *>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<(anonymous namespace)::PKSixChannelShaderKey, PKMetalShader *>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<(anonymous namespace)::PKSixChannelShaderKey, PKMetalShader *>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _sixChannelShaders;
{unordered_map<PKNamedShaderKey, PKMetalShader *, (anonymous namespace)::PKMetalResourceHandlerHashFunctions, std::equal_to<PKNamedShaderKey>, std::allocator<std::pair<const PKNamedShaderKey, PKMetalShader *>>>="__table_"{__hash_table<std::__hash_value_type<PKNamedShaderKey, PKMetalShader *>, std::__unordered_map_hasher<PKNamedShaderKey, std::pair<const PKNamedShaderKey, PKMetalShader *>, (anonymous namespace)::PKMetalResourceHandlerHashFunctions, std::equal_to<PKNamedShaderKey>>, std::__unordered_map_equal<PKNamedShaderKey, std::pair<const PKNamedShaderKey, PKMetalShader *>, std::equal_to<PKNamedShaderKey>, (anonymous namespace)::PKMetalResourceHandlerHashFunctions>, std::allocator<std::pair<const PKNamedShaderKey, PKMetalShader *>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<PKNamedShaderKey, PKMetalShader *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<PKNamedShaderKey, PKMetalShader *>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<PKNamedShaderKey, PKMetalShader *>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<PKNamedShaderKey, PKMetalShader *>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _namedShaders;
{unordered_map<PKShaderPipelineConfig, MTLRenderPipelineDescriptor *, (anonymous namespace)::PKMetalResourceHandlerHashFunctions, std::equal_to<PKShaderPipelineConfig>, std::allocator<std::pair<const PKShaderPipelineConfig, MTLRenderPipelineDescriptor *>>>="__table_"{__hash_table<std::__hash_value_type<PKShaderPipelineConfig, MTLRenderPipelineDescriptor *>, std::__unordered_map_hasher<PKShaderPipelineConfig, std::pair<const PKShaderPipelineConfig, MTLRenderPipelineDescriptor *>, (anonymous namespace)::PKMetalResourceHandlerHashFunctions, std::equal_to<PKShaderPipelineConfig>>, std::__unordered_map_equal<PKShaderPipelineConfig, std::pair<const PKShaderPipelineConfig, MTLRenderPipelineDescriptor *>, std::equal_to<PKShaderPipelineConfig>, (anonymous namespace)::PKMetalResourceHandlerHashFunctions>, std::allocator<std::pair<const PKShaderPipelineConfig, MTLRenderPipelineDescriptor *>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<PKShaderPipelineConfig, MTLRenderPipelineDescriptor *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<PKShaderPipelineConfig, MTLRenderPipelineDescriptor *>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<PKShaderPipelineConfig, MTLRenderPipelineDescriptor *>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<PKShaderPipelineConfig, MTLRenderPipelineDescriptor *>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _pipelineDescriptors;
{unordered_map<(anonymous namespace)::PKMetalKernelKey, id<MTLComputePipelineState>, (anonymous namespace)::PKMetalResourceHandlerHashFunctions, std::equal_to<(anonymous namespace)::PKMetalKernelKey>, std::allocator<std::pair<const (anonymous namespace)::PKMetalKernelKey, id<MTLComputePipelineState>>>>="__table_"{__hash_table<std::__hash_value_type<(anonymous namespace)::PKMetalKernelKey, id<MTLComputePipelineState>>, std::__unordered_map_hasher<(anonymous namespace)::PKMetalKernelKey, std::pair<const (anonymous namespace)::PKMetalKernelKey, id<MTLComputePipelineState>>, (anonymous namespace)::PKMetalResourceHandlerHashFunctions, std::equal_to<(anonymous namespace)::PKMetalKernelKey>>, std::__unordered_map_equal<(anonymous namespace)::PKMetalKernelKey, std::pair<const (anonymous namespace)::PKMetalKernelKey, id<MTLComputePipelineState>>, std::equal_to<(anonymous namespace)::PKMetalKernelKey>, (anonymous namespace)::PKMetalResourceHandlerHashFunctions>, std::allocator<std::pair<const (anonymous namespace)::PKMetalKernelKey, id<MTLComputePipelineState>>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<(anonymous namespace)::PKMetalKernelKey, id<MTLComputePipelineState>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<(anonymous namespace)::PKMetalKernelKey, id<MTLComputePipelineState>>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<(anonymous namespace)::PKMetalKernelKey, id<MTLComputePipelineState>>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<(anonymous namespace)::PKMetalKernelKey, id<MTLComputePipelineState>>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _kernelPipelines;
@"<MTLLibrary>" _defaultLibrary;
@"<MTLTexture>" _paperTexture;
{CGSize="width"d"height"d} _paperTextureSize;
@"PKLRUCache" _strokeRenderCache;
@"<MTLBuffer>" _uint16IndexBuffer;
@"<MTLBuffer>" _uint32IndexBuffer;
Q _uint32IndexBufferNumVertices;
@"<MTLBuffer>" _randomNumberBuffer;
@"NSObject<OS_dispatch_queue>" _accessQueue;
Q _signpost_id;
@"PKMetalResourceHandlerBuffer" _purgeableResourceBuffer;
@"PKMetalResourceHandlerBuffer" _resourceBuffer;
@"<MTLPipelineLibrarySPI>" _pipelineLibrary;
B _generatePipelineDescriptors;
B _generateForScribble;
B _deviceSupportsAppleFamily;
B _deviceSupportsMacFamily;
B _deviceSupportsFramebufferFetch;
B _sixChannelUsesWideGamutForNonEDR;
@"<MTLDevice>" _device;
Q _sixChannelOriginalBackPixelFormatNonEDR;
Q _sixChannelMetalLayerPixelFormatNonEDR;
Q _extendedDynamicRangePixelFormat;
@"MTLPipelineBufferDescriptor" _sharedPipelineDescriptor;
```

## Class methods

```
+[PKMetalResourceHandler generatePipelineDescriptorsForDevice:];
```

## Instance methods

```
-[PKMetalResourceHandler init];
```
