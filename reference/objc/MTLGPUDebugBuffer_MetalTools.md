# `MTLGPUDebugBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsBuffer`
- Protocols: `MTLGPUDebugResource`, `MTLGPUDebugViewable`
- 6 instance variables, 25 properties, 26 instance methods, 0 class methods

## Instance variables

```
Q _bufferIndex;
Q _offset;
Q _length;
Q _bufferEndAddress;
^v _descriptorHeap;
{unordered_set<unsigned long long, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<unsigned long long>>="__table_"{__hash_table<unsigned long long, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<unsigned long long>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<unsigned long long, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<unsigned long long, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _activeViews;
```

## Properties

```
@property (TQ,R,N) offset;
@property (TQ,R,N) gpuAddress;
@property (TQ,N,V_bufferEndAddress) bufferEndAddress;
@property (T@"<MTLBuffer>",&,D,N) baseObject;
@property (TQ,N) bufferIndex;
@property (TB,R,N) isTracked;
@property (TQ,R,N) length;
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
-[MTLGPUDebugBuffer newLinearTextureWithDescriptor:offset:bytesPerRow:bytesPerImage:];
-[MTLGPUDebugBuffer setBufferIndex:];
-[MTLGPUDebugBuffer contents];
-[MTLGPUDebugBuffer bufferIndex];
-[MTLGPUDebugBuffer setLabel:];
-[MTLGPUDebugBuffer dealloc];
-[MTLGPUDebugBuffer gpuAddress];
-[MTLGPUDebugBuffer length];
-[MTLGPUDebugBuffer addView:];
-[MTLGPUDebugBuffer removeView:];
-[MTLGPUDebugBuffer offset];
-[MTLGPUDebugBuffer newTensorWithDescriptor:offset:error:];
-[MTLGPUDebugBuffer newTextureWithDescriptor:offset:bytesPerRow:];
-[MTLGPUDebugBuffer isTracked];
-[MTLGPUDebugBuffer bufferEndAddress];
-[MTLGPUDebugBuffer getActiveViews];
-[MTLGPUDebugBuffer handleForOffset:];
-[MTLGPUDebugBuffer initWithBuffer:device:];
-[MTLGPUDebugBuffer initWithBuffer:device:offset:length:];
-[MTLGPUDebugBuffer initWithBuffer:device:offset:length:track:];
-[MTLGPUDebugBuffer initWithBuffer:heap:device:];
-[MTLGPUDebugBuffer initWithBuffer:heap:device:offset:length:track:];
-[MTLGPUDebugBuffer setBufferEndAddress:];
-[MTLGPUDebugBuffer underlyingGPUAddress];
-[MTLGPUDebugBuffer useWithComputeEncoder:usage:];
-[MTLGPUDebugBuffer useWithRenderEncoder:usage:stages:];
```
