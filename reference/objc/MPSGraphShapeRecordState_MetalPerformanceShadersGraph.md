# `MPSGraphShapeRecordState`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<GPU::AsyncShapeShiftingPatternTracker, std::default_delete<GPU::AsyncShapeShiftingPatternTracker>>=""{?="__ptr_"^{AsyncShapeShiftingPatternTracker}}} _tracker;
Q _historySize;
Q _minSamplesForPattern;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _resultMutex;
{PredictionResult="detectedIncrement"q"hasPattern"B"isStable"B"predictedInputShapes"{vector<std::vector<long long>, std::allocator<std::vector<long long>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}}"shapeResults"{unordered_map<std::string, std::vector<long long>, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::vector<long long>>>>="__table_"{__hash_table<std::__hash_value_type<std::string, std::vector<long long>>, std::__unordered_map_hasher<std::string, std::pair<const std::string, std::vector<long long>>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, std::vector<long long>>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, std::vector<long long>>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::vector<long long>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::vector<long long>>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::vector<long long>>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::vector<long long>>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}}"foldedResults"{unordered_map<std::string, std::vector<std::vector<long long>>, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::vector<std::vector<long long>>>>>="__table_"{__hash_table<std::__hash_value_type<std::string, std::vector<std::vector<long long>>>, std::__unordered_map_hasher<std::string, std::pair<const std::string, std::vector<std::vector<long long>>>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, std::vector<std::vector<long long>>>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, std::vector<std::vector<long long>>>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::vector<std::vector<long long>>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::vector<std::vector<long long>>>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::vector<std::vector<long long>>>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::vector<std::vector<long long>>>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}}"memrefViewResults"{unordered_map<std::string, std::vector<long long>, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::vector<long long>>>>="__table_"{__hash_table<std::__hash_value_type<std::string, std::vector<long long>>, std::__unordered_map_hasher<std::string, std::pair<const std::string, std::vector<long long>>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, std::vector<long long>>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, std::vector<long long>>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::vector<long long>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::vector<long long>>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::vector<long long>>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::vector<long long>>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}}"memrefAllocResults"{unordered_map<std::string, std::vector<long long>, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::vector<long long>>>>="__table_"{__hash_table<std::__hash_value_type<std::string, std::vector<long long>>, std::__unordered_map_hasher<std::string, std::pair<const std::string, std::vector<long long>>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, std::vector<long long>>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, std::vector<long long>>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::vector<long long>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::vector<long long>>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::vector<long long>>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::vector<long long>>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}}"hasComputedResults"B} _latestResult;
```

## Properties

```
@property (TB,R,N) hasDetectedPattern;
@property (TB,R,N) isPatternStable;
@property (Tq,R,N) detectedIncrement;
@property (TQ,R,N) executionCount;
@property (TQ,R,N) uniqueShapeCount;
```

## Instance methods

```
-[MPSGraphShapeRecordState reset];
-[MPSGraphShapeRecordState executionCount];
-[MPSGraphShapeRecordState _publishResult:];
-[MPSGraphShapeRecordState isPatternStable];
-[MPSGraphShapeRecordState _getTracker];
-[MPSGraphShapeRecordState _predictFutureShapesWithDepth:];
-[MPSGraphShapeRecordState _recordExecutionWithShapes:];
-[MPSGraphShapeRecordState detectedIncrement];
-[MPSGraphShapeRecordState hasDetectedPattern];
-[MPSGraphShapeRecordState initWithHistorySize:minSamplesForPattern:];
-[MPSGraphShapeRecordState uniqueShapeCount];
```
