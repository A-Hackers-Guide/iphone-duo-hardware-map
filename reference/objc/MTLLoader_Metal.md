# `MTLLoader`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 2 instance methods, 5 class methods

## Instance variables

```
^v _global;
@"NSObject<OS_dispatch_queue>" _claimQueue;
{unordered_map<MTLLoadedFile *, id, std::hash<MTLLoadedFile *>, std::equal_to<MTLLoadedFile *>, std::allocator<std::pair<MTLLoadedFile *const, id>>>="__table_"{__hash_table<std::__hash_value_type<MTLLoadedFile *, id>, std::__unordered_map_hasher<MTLLoadedFile *, std::pair<MTLLoadedFile *const, id>, std::hash<MTLLoadedFile *>, std::equal_to<MTLLoadedFile *>>, std::__unordered_map_equal<MTLLoadedFile *, std::pair<MTLLoadedFile *const, id>, std::equal_to<MTLLoadedFile *>, std::hash<MTLLoadedFile *>>, std::allocator<std::pair<MTLLoadedFile *const, id>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLLoadedFile *, id>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLLoadedFile *, id>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<MTLLoadedFile *, id>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<MTLLoadedFile *, id>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _claims;
```

## Class methods

```
+[MTLLoader deserializeHashesFromAIRNTHeaderAtOffset:headerSize:singleHeaderExpected:reader:errorHandler:handler:];
+[MTLLoader isAIRHeaderExtLoadCommand:headerOffset:headerSize:headerSection:];
+[MTLLoader deserializeObjectFromAIRNTHeaderAtSection:reader:errorHandler:handler:];
+[MTLLoader deserializePipelinesFromAIRNTAtSection:reader:errorHandler:handler:];
+[MTLLoader ReadHashTable:begin:end:hashList:reader:errorHandler:handler:];
```

## Instance methods

```
-[MTLLoader init];
-[MTLLoader dealloc];
```
