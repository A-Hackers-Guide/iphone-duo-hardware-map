# `_ETBufferDataSource`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ETDataProvider`
- 5 instance variables, 9 properties, 14 instance methods, 0 class methods

## Instance variables

```
Q _number_of_data_points;
Q _batchSize;
{vector<std::string, std::allocator<std::string>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} _nonBatchBlobNames;
{unordered_map<std::string, std::shared_ptr<Espresso::blob<float, 1>>, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::shared_ptr<Espresso::blob<float, 1>>>>>="__table_"{__hash_table<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 1>>>, std::__unordered_map_hasher<std::string, std::pair<const std::string, std::shared_ptr<Espresso::blob<float, 1>>>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, std::shared_ptr<Espresso::blob<float, 1>>>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, std::shared_ptr<Espresso::blob<float, 1>>>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 1>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 1>>>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 1>>>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 1>>>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _dataStorage;
{unordered_map<std::string, Espresso::layer_shape, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, Espresso::layer_shape>>>="__table_"{__hash_table<std::__hash_value_type<std::string, Espresso::layer_shape>, std::__unordered_map_hasher<std::string, std::pair<const std::string, Espresso::layer_shape>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, Espresso::layer_shape>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, Espresso::layer_shape>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _blobShapes;
```

## Properties

```
@property (T{unordered_map<std::string, std::shared_ptr<Espresso::blob<float, 1>>, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::shared_ptr<Espresso::blob<float, 1>>>>>={__hash_table<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 1>>>, std::__unordered_map_hasher<std::string, std::pair<const std::string, std::shared_ptr<Espresso::blob<float, 1>>>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, std::shared_ptr<Espresso::blob<float, 1>>>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, std::shared_ptr<Espresso::blob<float, 1>>>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 1>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 1>>>, void *> *> *>>>={?=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 1>>>, void *> *> *>>={?=Q}}}}{?={__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::shared_ptr<Espresso::blob<float, 1>>>, void *> *>=^v}}{?=Q}{?=f}}},V_dataStorage) dataStorage;
@property (T{unordered_map<std::string, Espresso::layer_shape, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, Espresso::layer_shape>>>={__hash_table<std::__hash_value_type<std::string, Espresso::layer_shape>, std::__unordered_map_hasher<std::string, std::pair<const std::string, Espresso::layer_shape>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, Espresso::layer_shape>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, Espresso::layer_shape>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *> *>>>={?=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *> *>>={?=Q}}}}{?={__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *>=^v}}{?=Q}{?=f}}},V_blobShapes) blobShapes;
@property (TQ,V_number_of_data_points) number_of_data_points;
@property (TQ,V_batchSize) batchSize;
@property (T{vector<std::string, std::allocator<std::string>>=^v^v{?=^v}},V_nonBatchBlobNames) nonBatchBlobNames;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_ETBufferDataSource batchSize];
-[_ETBufferDataSource setBatchSize:];
-[_ETBufferDataSource numberOfDataPoints];
-[_ETBufferDataSource setDataStorage:];
-[_ETBufferDataSource blobShapes];
-[_ETBufferDataSource dataAtIndex:key:];
-[_ETBufferDataSource dataPointAtIndex:error:];
-[_ETBufferDataSource dataStorage];
-[_ETBufferDataSource initWithBlobShapes:numberOfDataPoints:batchSize:error:];
-[_ETBufferDataSource nonBatchBlobNames];
-[_ETBufferDataSource number_of_data_points];
-[_ETBufferDataSource setBlobShapes:];
-[_ETBufferDataSource setNonBatchBlobNames:];
-[_ETBufferDataSource setNumber_of_data_points:];
```
