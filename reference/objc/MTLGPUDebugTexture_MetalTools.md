# `MTLGPUDebugTexture`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsTexture`
- Protocols: `MTLGPUDebugResource`, `MTLGPUDebugViewable`
- 3 instance variables, 23 properties, 25 instance methods, 0 class methods

## Instance variables

```
Q _identifier;
{unordered_set<unsigned long long, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<unsigned long long>>="__table_"{__hash_table<unsigned long long, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<unsigned long long>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<unsigned long long, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _activeViews;
@"<MTLGPUDebugViewable>" _parentViewable;
```

## Properties

```
@property (T@"<MTLTextureSPI>",&,D,N) baseObject;
@property (TQ,R,N) gpuIdentifier;
@property (T@"<MTLGPUDebugViewable>",&,N,V_parentViewable) parentViewable;
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
-[MTLGPUDebugTexture setLabel:];
-[MTLGPUDebugTexture dealloc];
-[MTLGPUDebugTexture length];
-[MTLGPUDebugTexture addView:];
-[MTLGPUDebugTexture newTextureViewWithPixelFormat:textureType:levels:slices:resourceIndex:];
-[MTLGPUDebugTexture newTextureViewWithPixelFormat:resourceIndex:];
-[MTLGPUDebugTexture newTextureViewWithDescriptor:];
-[MTLGPUDebugTexture newCompressedTextureViewWithPixelFormat:textureType:level:slice:];
-[MTLGPUDebugTexture newTextureViewWithPixelFormat:textureType:levels:slices:];
-[MTLGPUDebugTexture newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:resourceIndex:];
-[MTLGPUDebugTexture newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:];
-[MTLGPUDebugTexture removeView:];
-[MTLGPUDebugTexture newTextureViewWithPixelFormat:];
-[MTLGPUDebugTexture baseObject];
-[MTLGPUDebugTexture getActiveViews];
-[MTLGPUDebugTexture gpuIdentifier];
-[MTLGPUDebugTexture handleForOffset:];
-[MTLGPUDebugTexture initWithTexture:heap:device:];
-[MTLGPUDebugTexture initWithTextureView:parentBuffer:heap:device:];
-[MTLGPUDebugTexture initWithTextureView:parentTexture:heap:device:];
-[MTLGPUDebugTexture parentViewable];
-[MTLGPUDebugTexture setParentViewable:];
-[MTLGPUDebugTexture underlyingGPUAddress];
-[MTLGPUDebugTexture useWithComputeEncoder:usage:];
-[MTLGPUDebugTexture useWithRenderEncoder:usage:stages:];
```
