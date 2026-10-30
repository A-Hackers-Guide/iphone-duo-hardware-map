# `MTL3On4GlobalCommandBufferManager`

- Image: [`/System/Library/PrivateFrameworks/MTL3On4.framework/MTL3On4`](../userland/System__Library__PrivateFrameworks__MTL3On4.framework__MTL3On4.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
{unordered_map<MTL3On4CommandBufferMapKey, MTL3On4CommandBuffer *, MTL3On4CommandBufferMapKeyHasher, std::equal_to<MTL3On4CommandBufferMapKey>, std::allocator<std::pair<const MTL3On4CommandBufferMapKey, MTL3On4CommandBuffer *>>>="__table_"{__hash_table<std::__hash_value_type<MTL3On4CommandBufferMapKey, MTL3On4CommandBuffer *>, std::__unordered_map_hasher<MTL3On4CommandBufferMapKey, std::pair<const MTL3On4CommandBufferMapKey, MTL3On4CommandBuffer *>, MTL3On4CommandBufferMapKeyHasher, std::equal_to<MTL3On4CommandBufferMapKey>>, std::__unordered_map_equal<MTL3On4CommandBufferMapKey, std::pair<const MTL3On4CommandBufferMapKey, MTL3On4CommandBuffer *>, std::equal_to<MTL3On4CommandBufferMapKey>, MTL3On4CommandBufferMapKeyHasher>, std::allocator<std::pair<const MTL3On4CommandBufferMapKey, MTL3On4CommandBuffer *>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTL3On4CommandBufferMapKey, MTL3On4CommandBuffer *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTL3On4CommandBufferMapKey, MTL3On4CommandBuffer *>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTL3On4CommandBufferMapKey, MTL3On4CommandBuffer *>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTL3On4CommandBufferMapKey, MTL3On4CommandBuffer *>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _commandBufferMap;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _commandBufferMapLock;
```

## Class methods

```
+[MTL3On4GlobalCommandBufferManager sharedInstance];
```

## Instance methods

```
-[MTL3On4GlobalCommandBufferManager init];
-[MTL3On4GlobalCommandBufferManager wrapCommandBuffer:];
-[MTL3On4GlobalCommandBufferManager releaseCommandBufferWrapperForKey:];
```
