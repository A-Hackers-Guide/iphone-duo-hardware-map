# `CAContentStream`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 0 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"CAContentStreamOptions" _options;
{unordered_map<unsigned int, unsigned int, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, unsigned int>>>="__table_"{__hash_table<std::__hash_value_type<unsigned int, unsigned int>, std::__unordered_map_hasher<unsigned int, std::pair<const unsigned int, unsigned int>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::pair<const unsigned int, unsigned int>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::pair<const unsigned int, unsigned int>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _includedContexts;
{unordered_map<unsigned int, unsigned int, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, unsigned int>>>="__table_"{__hash_table<std::__hash_value_type<unsigned int, unsigned int>, std::__unordered_map_hasher<unsigned int, std::pair<const unsigned int, unsigned int>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::pair<const unsigned int, unsigned int>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::pair<const unsigned int, unsigned int>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _excludedContexts;
{small_vector<ContentStreamClientFrame, 8UL>="_begin"^{ContentStreamClientFrame}"_end"^{ContentStreamClientFrame}"_fixedStorage"^{ContentStreamClientFrame}"_capacity"Q""(?="storage"[8(type="__data"[16C])]"flat_storage"[0{ContentStreamClientFrame="iosurface"^{__IOSurface}"id"I"port"I}])} _seen_surfaces;
I _serverPort;
{ClientIPC="_port"I"_queue"@"NSObject<OS_dispatch_queue>""_source"@"NSObject<OS_dispatch_source>"} _clientIPC;
B _started;
B _warmed_up;
{SpinLock="_l"{?="x"i}} _callback_lock;
@"NSObject<OS_dispatch_queue>" _queue;
@? _handler;
```

## Class methods

```
+[CAContentStream contentStreamWithOptions:queue:handler:error:];
```

## Instance methods

```
-[CAContentStream start:];
-[CAContentStream streamId];
-[CAContentStream updateOptions:error:];
-[CAContentStream dealloc];
-[CAContentStream stop:];
-[CAContentStream clearSeenSurfaces];
-[CAContentStream copyOptions];
-[CAContentStream produceSurface:withFrameInfo:];
-[CAContentStream releaseSurface:error:];
-[CAContentStream releaseSurfaceWithId:error:];
-[CAContentStream setExcludedContexts:error:];
-[CAContentStream setIncludedContexts:error:];
```
