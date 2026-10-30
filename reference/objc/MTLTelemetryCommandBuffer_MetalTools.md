# `MTLTelemetryCommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsCommandBuffer`
- 22 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
^{MTLTelemetryEncoderCountRec=IIII} encoderCount;
^{MTLTelemetryStatisticUIRec=IIQI} attachmentCount;
^{MTLTelemetryStatisticUIRec=IIQI} textureBindCount;
^{MTLTelemetryStatisticUIRec=IIQI} parallellRenderEncoderDistribution;
^{MTLTelemetryStatisticUIRec=IIQI} renderTargetArrayLengthDistribution;
^{MTLTelemetryViewportDistributionRec={MTLTelemetryStatisticUIRec=IIQI}{MTLTelemetryStatisticFRec=fffI}{MTLTelemetryStatisticFRec=fffI}{MTLTelemetryStatisticFRec=fffI}{MTLTelemetryStatisticFRec=fffI}} viewportDistribution;
^{MTLTelemetryScissorRectDistributionRec={MTLTelemetryStatisticUIRec=IIQI}{MTLTelemetryStatisticFRec=fffI}{MTLTelemetryStatisticFRec=fffI}} scissorRectDistribution;
^{MTLTelemetryDrawDistributionRec=[5[3[3{MTLTelemetryDrawStatRec=I{MTLTelemetryStatisticUIRec=IIQI}{MTLTelemetryStatisticUIRec=IIQI}}]]]} drawDistribution;
^{MTLTelemetryDispatchDistributionRec=I{MTLTelemetryStatisticUIRec=IIQI}{MTLTelemetryStatisticUIRec=IIQI}{MTLTelemetryStatisticUIRec=IIQI}{MTLTelemetryStatisticUIRec=IIQI}{MTLTelemetryStatisticUIRec=IIQI}{MTLTelemetryStatisticUIRec=IIQI}{MTLTelemetryStatisticUIRec=IIQI}{MTLTelemetryStatisticUIRec=IIQI}{MTLTelemetryStatisticUIRec=IIQI}{MTLTelemetryStatisticUIRec=IIQI}} dispatchDistribution;
I cbDraws;
I cbDispatches;
I cbBlits;
I cbMemoryBarriers;
^{MTLTelemetryStatisticUIRec=IIQI} renderEncoderDrawCallDistribution;
^{MTLTelemetryStatisticUIRec=IIQI} computeEncoderDispatchDistribution;
^{MTLTelemetryStatisticUIRec=IIQI} blitEncoderBlitDistribution;
{unordered_map<MTLPixelFormat, MTLTelemetryRenderTargetDistribution, std::hash<unsigned long long>, std::equal_to<MTLPixelFormat>, std::allocator<std::pair<const MTLPixelFormat, MTLTelemetryRenderTargetDistribution>>>="__table_"{__hash_table<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, std::__unordered_map_hasher<MTLPixelFormat, std::pair<const MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, std::hash<unsigned long long>, std::equal_to<MTLPixelFormat>>, std::__unordered_map_equal<MTLPixelFormat, std::pair<const MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, std::equal_to<MTLPixelFormat>, std::hash<unsigned long long>>, std::allocator<std::pair<const MTLPixelFormat, MTLTelemetryRenderTargetDistribution>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryRenderTargetDistribution>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} renderTargetMap;
{unordered_map<MTLPixelFormat, MTLTelemetryBlitDistribution, std::hash<unsigned long long>, std::equal_to<MTLPixelFormat>, std::allocator<std::pair<const MTLPixelFormat, MTLTelemetryBlitDistribution>>>="__table_"{__hash_table<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, std::__unordered_map_hasher<MTLPixelFormat, std::pair<const MTLPixelFormat, MTLTelemetryBlitDistribution>, std::hash<unsigned long long>, std::equal_to<MTLPixelFormat>>, std::__unordered_map_equal<MTLPixelFormat, std::pair<const MTLPixelFormat, MTLTelemetryBlitDistribution>, std::equal_to<MTLPixelFormat>, std::hash<unsigned long long>>, std::allocator<std::pair<const MTLPixelFormat, MTLTelemetryBlitDistribution>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLPixelFormat, MTLTelemetryBlitDistribution>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} blitMap;
^{MTLTelemetryAnisoClippedCountsRec=[4I]} anisoClippedCounts;
I depthClipModeClampCount;
@"MTLTelemetryDevice" _telemetryDevice;
{MTLTelemetryKernelStateRec="pbAlloc"i"spmRenderCount"i"tiledSceneBytes"i"renderCount"i} _initKernelState;
```

## Instance methods

```
-[MTLTelemetryCommandBuffer blitCommandEncoderWithDescriptor:];
-[MTLTelemetryCommandBuffer computeCommandEncoderWithDescriptor:];
-[MTLTelemetryCommandBuffer computeCommandEncoder];
-[MTLTelemetryCommandBuffer dealloc];
-[MTLTelemetryCommandBuffer blitCommandEncoder];
-[MTLTelemetryCommandBuffer renderCommandEncoderWithDescriptor:];
-[MTLTelemetryCommandBuffer parallelRenderCommandEncoderWithDescriptor:];
-[MTLTelemetryCommandBuffer initDistributions];
-[MTLTelemetryCommandBuffer initWithCommandBuffer:commandQueue:descriptor:];
-[MTLTelemetryCommandBuffer mergeDistributions];
-[MTLTelemetryCommandBuffer postCompletionHandlers];
```
