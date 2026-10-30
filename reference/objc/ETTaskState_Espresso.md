# `ETTaskState`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
{shared_ptr<Espresso::net>="__ptr_"^{net}"__cntrl_"^{__shared_weak_count}} _networkPointer;
{unordered_map<std::string, std::shared_ptr<Espresso::blob<float, 4>>, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::shared_ptr<Espresso::blob<float, 4>>>>>="__table_"{__hash_table<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 4>>>, std::__unordered_map_hasher<std::string, std::pair<const std::string, std::shared_ptr<Espresso::blob<float, 4>>>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, std::shared_ptr<Espresso::blob<float, 4>>>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, std::shared_ptr<Espresso::blob<float, 4>>>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 4>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 4>>>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 4>>>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 4>>>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _blobs;
```

## Properties

```
@property (T{unordered_map<std::string, std::shared_ptr<Espresso::blob<float, 4>>, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::shared_ptr<Espresso::blob<float, 4>>>>>={__hash_table<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 4>>>, std::__unordered_map_hasher<std::string, std::pair<const std::string, std::shared_ptr<Espresso::blob<float, 4>>>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, std::shared_ptr<Espresso::blob<float, 4>>>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, std::shared_ptr<Espresso::blob<float, 4>>>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 4>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 4>>>, void *> *> *>>>={?=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 4>>>, void *> *> *>>={?=Q}}}}{?={__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 4>>>, void *> *>=^v}}{?=Q}{?=f}}},V_blobs) blobs;
@property (T{shared_ptr<Espresso::net>=^{net}^{__shared_weak_count}},V_networkPointer) networkPointer;
```

## Instance methods

```
-[ETTaskState initWithNetwork:];
-[ETTaskState blobs];
-[ETTaskState initWithBlobMap:];
-[ETTaskState networkPointer];
-[ETTaskState setBlobs:];
-[ETTaskState setNetworkPointer:];
```
