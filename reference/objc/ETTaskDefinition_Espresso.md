# `ETTaskDefinition`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ETTaskContext`
- 22 instance variables, 6 properties, 36 instance methods, 0 class methods

## Instance variables

```
{unordered_map<std::string, unsigned long, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, unsigned long>>>="__table_"{__hash_table<std::__hash_value_type<std::string, unsigned long>, std::__unordered_map_hasher<std::string, std::pair<const std::string, unsigned long>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, unsigned long>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, unsigned long>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned long>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned long>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned long>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, unsigned long>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} inference_layer_index;
@"ETVariablesDefinition" varsDef;
Q runtimePlatform;
i precision;
Q batchSize;
{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}} training_control_name;
{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}} gradient_control_name;
{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}} optimizer_control_name;
@"NSArray" infInputNames;
@"NSArray" infOutputNames;
@"NSArray" trainInputNames;
@"NSArray" trainOutputNames;
{unordered_map<std::string, Espresso::layer_shape, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, Espresso::layer_shape>>>="__table_"{__hash_table<std::__hash_value_type<std::string, Espresso::layer_shape>, std::__unordered_map_hasher<std::string, std::pair<const std::string, Espresso::layer_shape>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, Espresso::layer_shape>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, Espresso::layer_shape>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} infInputBlobShapes;
{unordered_map<std::string, Espresso::layer_shape, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, Espresso::layer_shape>>>="__table_"{__hash_table<std::__hash_value_type<std::string, Espresso::layer_shape>, std::__unordered_map_hasher<std::string, std::pair<const std::string, Espresso::layer_shape>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, Espresso::layer_shape>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, Espresso::layer_shape>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} trainInputBlobShapes;
{unordered_map<std::string, Espresso::layer_shape, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, Espresso::layer_shape>>>="__table_"{__hash_table<std::__hash_value_type<std::string, Espresso::layer_shape>, std::__unordered_map_hasher<std::string, std::pair<const std::string, Espresso::layer_shape>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, Espresso::layer_shape>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, Espresso::layer_shape>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} infOutputBlobShapes;
{unordered_map<std::string, Espresso::layer_shape, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, Espresso::layer_shape>>>="__table_"{__hash_table<std::__hash_value_type<std::string, Espresso::layer_shape>, std::__unordered_map_hasher<std::string, std::pair<const std::string, Espresso::layer_shape>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, Espresso::layer_shape>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, Espresso::layer_shape>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, Espresso::layer_shape>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} trainOutputBlobShapes;
@"ETModelDefinition" _inferenceModel;
@"ETOptimizerDefinition" _optimizer;
Q _platform;
@"ETTaskState" _taskState;
{shared_ptr<Espresso::net>="__ptr_"^{net}"__cntrl_"^{__shared_weak_count}} _inferenceGraphNetPtr;
{shared_ptr<Espresso::net>="__ptr_"^{net}"__cntrl_"^{__shared_weak_count}} _trainingGraphNetPtr;
```

## Properties

```
@property (T{shared_ptr<Espresso::net>=^{net}^{__shared_weak_count}},V_inferenceGraphNetPtr) inferenceGraphNetPtr;
@property (T{shared_ptr<Espresso::net>=^{net}^{__shared_weak_count}},V_trainingGraphNetPtr) trainingGraphNetPtr;
@property (T@"ETModelDefinition",&,N,V_inferenceModel) inferenceModel;
@property (T@"ETOptimizerDefinition",&,N,V_optimizer) optimizer;
@property (TQ,N,V_platform) platform;
@property (T@"ETTaskState",&,N,V_taskState) taskState;
```

## Instance methods

```
-[ETTaskDefinition setTaskState:];
-[ETTaskDefinition taskState];
-[ETTaskDefinition platform];
-[ETTaskDefinition setPlatform:];
-[ETTaskDefinition description];
-[ETTaskDefinition getTensorNamed:];
-[ETTaskDefinition setTensorNamed:withValue:error:];
-[ETTaskDefinition setupShapes:forBlobs:withError:];
-[ETTaskDefinition checkShapes:withSample:withError:];
-[ETTaskDefinition context_for_runtime_platform:];
-[ETTaskDefinition dataTypeForParameterOfType:fromLayerNamed:];
-[ETTaskDefinition doInferenceOnData:error:];
-[ETTaskDefinition doTrainingOnData:forNumberOfEpochs:withCallback:error:];
-[ETTaskDefinition getParameterOfType:forLayerNamed:error:];
-[ETTaskDefinition getTensorNamed:directBind:];
-[ETTaskDefinition inferenceGraphNetPtr];
-[ETTaskDefinition inferenceModel];
-[ETTaskDefinition initWithModelDefinition:lossDefinition:variablesDefinition:optimizerDefinition:forPlatform:error:];
-[ETTaskDefinition initWithTrainingModelDefinition:forPlatform:error:];
-[ETTaskDefinition namesVectorToFoundationArray:];
-[ETTaskDefinition optimizer];
-[ETTaskDefinition platformForLayerNamed:error:];
-[ETTaskDefinition privateDoTrainingOnData:forNumberOfEpochs:withCallback:error:];
-[ETTaskDefinition reloadOnRuntimePlatform:];
-[ETTaskDefinition saveNetwork:inplace:error:];
-[ETTaskDefinition saveTrainingNetwork:checkpoint:error:];
-[ETTaskDefinition setInferenceGraphNetPtr:];
-[ETTaskDefinition setInferenceModel:];
-[ETTaskDefinition setInferenceNetworkWeights:error:];
-[ETTaskDefinition setOptimizer:];
-[ETTaskDefinition setParameterOfType:forLayerNamed:withValue:error:];
-[ETTaskDefinition setTrainingGraphNetPtr:];
-[ETTaskDefinition setWeightsOfInferenceNetworkLoadedFrom:AndSaveTo:error:];
-[ETTaskDefinition setupInputOutputShapes:];
-[ETTaskDefinition shareWeights];
-[ETTaskDefinition trainingGraphNetPtr];
```
