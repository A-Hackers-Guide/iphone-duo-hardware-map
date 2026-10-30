# `MTLDebugTexture`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsTexture`
- Protocols: `MTLDebugResourcePurgeable`
- 14 instance variables, 7 properties, 43 instance methods, 0 class methods

## Instance variables

```
{MTLPixelFormatInfo="name"*"flags"I"castClass"Q"type"(?="normal"{MTLNormalPixelFormatInfo="pixelBytes"Q"componentCount"C"alignment"C"pixelBytesRender"Q"pixelBytesRenderMSAA"Q}"compressed"{MTLCompressedPixelFormatInfo="blockBytes"Q"blockWidth"Q"blockHeight"Q"blockDepth"Q})} _pixelFormatInfo;
@"MTLDebugDevice" _debugDevice;
Q _usageRequired;
{atomic<int>="__a_"{__cxx_atomic_impl<int, std::__cxx_atomic_base_impl<int>>="__a_value"Ai}} _purgeableStateToken;
B _purgeableStateHasBeenSet;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _subViewUseLock;
{unordered_map<SubView, unsigned long, SubView::hash_t, SubView::equal_t, std::allocator<std::pair<const SubView, unsigned long>>>="__table_"{__hash_table<std::__hash_value_type<SubView, unsigned long>, std::__unordered_map_hasher<SubView, std::pair<const SubView, unsigned long>, SubView::hash_t, SubView::equal_t>, std::__unordered_map_equal<SubView, std::pair<const SubView, unsigned long>, SubView::equal_t, SubView::hash_t>, std::allocator<std::pair<const SubView, unsigned long>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SubView, unsigned long>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SubView, unsigned long>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<SubView, unsigned long>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<SubView, unsigned long>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _activeSubViews;
B _isLinearTexture;
@"MTLDebugResource" _common;
Q _offset;
Q _bytesPerRow;
Q _bytesPerImage;
Q _plane;
q _placementSparsePageSize;
```

## Properties

```
@property (T@"MTLDebugResource",R,N,V_common) common;
@property (TQ,R,N,V_offset) offset;
@property (TQ,R,N,V_bytesPerRow) bytesPerRow;
@property (TQ,R,N,V_bytesPerImage) bytesPerImage;
@property (TQ,R,N,V_plane) plane;
@property (TB,R,N,V_isLinearTexture) isLinearTexture;
@property (Tq,R,N,V_placementSparsePageSize) placementSparsePageSize;
```

## Instance methods

```
-[MTLDebugTexture placementSparsePageSize];
-[MTLDebugTexture bytesPerRow];
-[MTLDebugTexture dealloc];
-[MTLDebugTexture replaceRegion:mipmapLevel:withBytes:bytesPerRow:];
-[MTLDebugTexture getBytes:bytesPerRow:bytesPerImage:fromRegion:mipmapLevel:slice:];
-[MTLDebugTexture replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:];
-[MTLDebugTexture newTextureViewWithPixelFormat:textureType:levels:slices:resourceIndex:];
-[MTLDebugTexture newTextureViewWithPixelFormat:resourceIndex:];
-[MTLDebugTexture setPurgeableState:];
-[MTLDebugTexture newTextureViewWithDescriptor:];
-[MTLDebugTexture newCompressedTextureViewWithPixelFormat:textureType:level:slice:];
-[MTLDebugTexture description];
-[MTLDebugTexture newTextureViewWithPixelFormat:textureType:levels:slices:];
-[MTLDebugTexture newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:resourceIndex:];
-[MTLDebugTexture getBytes:bytesPerRow:fromRegion:mipmapLevel:];
-[MTLDebugTexture common];
-[MTLDebugTexture makeAliasable];
-[MTLDebugTexture newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:];
-[MTLDebugTexture bytesPerImage];
-[MTLDebugTexture offset];
-[MTLDebugTexture newTextureViewWithPixelFormat:];
-[MTLDebugTexture doesAliasAllResources:count:];
-[MTLDebugTexture doesAliasAnyResources:count:];
-[MTLDebugTexture doesAliasResource:];
-[MTLDebugTexture plane];
-[MTLDebugTexture isLinearTexture];
-[MTLDebugTexture purgeableStateValidForRendering];
-[MTLDebugTexture addUsedRenderTarget:slices:];
-[MTLDebugTexture evaluateSloppyUsage:];
-[MTLDebugTexture evaluateUsage:];
-[MTLDebugTexture initWithBaseTexture:device:];
-[MTLDebugTexture initWithBaseTexture:device:buffer:offset:bytesPerRow:bytesPerImage:descriptor:];
-[MTLDebugTexture initWithBaseTexture:device:buffer:offset:bytesPerRow:descriptor:];
-[MTLDebugTexture initWithBaseTexture:device:placementSparsePageSize:];
-[MTLDebugTexture initWithBaseTexture:device:plane:];
-[MTLDebugTexture initWithBaseTexture:device:texture:];
-[MTLDebugTexture initWithBaseTexture:device:texture:pixelFormat:];
-[MTLDebugTexture initWithBaseTexture:device:texture:pixelFormat:textureType:levels:slices:];
-[MTLDebugTexture initWithBaseTexture:heap:device:];
-[MTLDebugTexture lockPurgeableState];
-[MTLDebugTexture removeUsedRenderTarget:slices:];
-[MTLDebugTexture requireUsage:];
-[MTLDebugTexture unlockPurgeableState];
```
