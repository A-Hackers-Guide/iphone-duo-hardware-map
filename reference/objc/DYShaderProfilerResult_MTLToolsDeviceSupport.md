# `DYShaderProfilerResult`

- Image: [`/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport`](../userland/System__Library__PrivateFrameworks__MTLToolsDeviceSupport.framework__MTLToolsDeviceSupport.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 34 instance variables, 27 properties, 52 instance methods, 0 class methods

## Instance variables

```
{DYShaderProfilerTiming="_cycle"{Statistics="average"d"min"d"max"d}"_time"{Statistics="average"d"min"d"max"d}} _vertexTiming;
{DYShaderProfilerTiming="_cycle"{Statistics="average"d"min"d"max"d}"_time"{Statistics="average"d"min"d"max"d}} _fragmentTiming;
{DYShaderProfilerTiming="_cycle"{Statistics="average"d"min"d"max"d}"_time"{Statistics="average"d"min"d"max"d}} _computeTiming;
{DYShaderProfilerTiming="_cycle"{Statistics="average"d"min"d"max"d}"_time"{Statistics="average"d"min"d"max"d}} _timing;
{unordered_map<unsigned long long, unsigned int, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, unsigned int>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long long, unsigned int>, std::__unordered_map_hasher<unsigned long long, std::pair<const unsigned long long, unsigned int>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::pair<const unsigned long long, unsigned int>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::pair<const unsigned long long, unsigned int>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _drawCallInfoIndexMap;
@"NSMutableDictionary" _vertexShaderBinaryInfo;
@"NSMutableDictionary" _fragmentShaderBinaryInfo;
@"NSMutableDictionary" _computeKernelBinaryInfo;
@"NSMutableDictionary" _allShaderBinaryInfo;
{unordered_map<unsigned long long, unsigned int, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, unsigned int>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long long, unsigned int>, std::__unordered_map_hasher<unsigned long long, std::pair<const unsigned long long, unsigned int>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::pair<const unsigned long long, unsigned int>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::pair<const unsigned long long, unsigned int>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, unsigned int>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _perContextDrawCallCounterDY;
{unordered_map<unsigned long long, std::unordered_map<int, unsigned int>, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, std::unordered_map<int, unsigned int>>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long long, std::unordered_map<int, unsigned int>>, std::__unordered_map_hasher<unsigned long long, std::pair<const unsigned long long, std::unordered_map<int, unsigned int>>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::pair<const unsigned long long, std::unordered_map<int, unsigned int>>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::pair<const unsigned long long, std::unordered_map<int, unsigned int>>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::unordered_map<int, unsigned int>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::unordered_map<int, unsigned int>>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::unordered_map<int, unsigned int>>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, std::unordered_map<int, unsigned int>>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _functionIndexToDrawCallIndexMap;
I _commandBufferCount;
I _deviceUtilization;
I _encoderCount;
@"NSMutableArray" _drawCallInfoList;
@"NSMutableArray" _encoderInfoList;
@"NSMutableArray" _encoderFunctionIndexList;
@"NSMutableArray" _programInfoList;
@"NSMutableArray" _programPipelineInfoList;
@"NSMutableDictionary" _encoderFunctionIndexToEncoderIndexMap;
@"NSMutableArray" _effectiveKickTimes;
@"NSMutableArray" _effectivePerEncoderDrawKickTimes;
@"NSMutableArray" _averagePerDrawKickDurations;
@"NSMutableArray" _loadActionTimes;
@"NSMutableArray" _storeActionTimes;
@"NSMutableArray" _perCommandBufferEncoderCount;
@"NSDictionary" _encoderIndexToLabelMap;
@"NSDictionary" _derivedCountersData;
Q _frameTime;
d _gpuTime;
@"NSArray" _blitTimeData;
@"NSMutableDictionary" _blitEncoderTimeInfo;
@"NSMutableArray" _shaderProfilingFrameTimes;
d _shaderProfilingTime;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_drawCallInfoList) drawCallInfoList;
@property (T@"NSMutableArray",&,N,V_programPipelineInfoList) programPipelineInfoList;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},N,V_vertexTiming) vertexTiming;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},N,V_fragmentTiming) fragmentTiming;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},N,V_computeTiming) computeTiming;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},N,V_timing) timing;
@property (TQ,N,V_frameTime) frameTime;
@property (TI,N,V_deviceUtilization) deviceUtilization;
@property (TI,N,V_encoderCount) encoderCount;
@property (Td,N,V_gpuTime) gpuTime;
@property (T@"NSArray",&,N,V_blitTimeData) blitTimeData;
@property (T@"NSMutableDictionary",&,N,V_blitEncoderTimeInfo) blitEncoderTimeInfo;
@property (T@"NSMutableArray",&,N,V_shaderProfilingFrameTimes) shaderProfilingFrameTimes;
@property (Td,N,V_shaderProfilingTime) shaderProfilingTime;
@property (T@"NSDictionary",&,N,V_derivedCountersData) derivedCountersData;
@property (T@"NSMutableArray",R,N,V_encoderInfoList) encoderInfoList;
@property (T@"NSMutableArray",R,N,V_encoderFunctionIndexList) encoderFunctionIndexList;
@property (T@"NSMutableArray",R,N,V_programInfoList) programInfoList;
@property (T@"NSMutableDictionary",R,N,V_encoderFunctionIndexToEncoderIndexMap) encoderFunctionIndexToEncoderIndexMap;
@property (T@"NSMutableArray",&,N,V_effectiveKickTimes) effectiveKickTimes;
@property (T@"NSMutableArray",&,N,V_effectivePerEncoderDrawKickTimes) effectivePerEncoderDrawKickTimes;
@property (T@"NSMutableArray",&,N,V_averagePerDrawKickDurations) averagePerDrawKickDurations;
@property (T@"NSMutableArray",&,N,V_loadActionTimes) loadActionTimes;
@property (T@"NSMutableArray",&,N,V_storeActionTimes) storeActionTimes;
@property (TI,N,V_commandBufferCount) commandBufferCount;
@property (T@"NSMutableArray",&,N,V_perCommandBufferEncoderCount) perCommandBufferEncoderCount;
@property (T@"NSDictionary",&,N,V_encoderIndexToLabelMap) encoderIndexToLabelMap;
```

## Instance methods

```
-[DYShaderProfilerResult setCommandBufferCount:];
-[DYShaderProfilerResult init];
-[DYShaderProfilerResult timing];
-[DYShaderProfilerResult setTiming:];
-[DYShaderProfilerResult frameTime];
-[DYShaderProfilerResult setFrameTime:];
-[DYShaderProfilerResult gpuTime];
-[DYShaderProfilerResult commandBufferCount];
-[DYShaderProfilerResult setGpuTime:];
-[DYShaderProfilerResult loadActionTimes];
-[DYShaderProfilerResult setAveragePerDrawKickDurations:];
-[DYShaderProfilerResult encoderInfoList];
-[DYShaderProfilerResult programInfoList];
-[DYShaderProfilerResult averagePerDrawKickDurations];
-[DYShaderProfilerResult blitEncoderTimeInfo];
-[DYShaderProfilerResult blitTimeData];
-[DYShaderProfilerResult buildDrawCallIndexMap];
-[DYShaderProfilerResult computeTiming];
-[DYShaderProfilerResult derivedCountersData];
-[DYShaderProfilerResult deviceUtilization];
-[DYShaderProfilerResult drawCallInfoList];
-[DYShaderProfilerResult effectiveKickTimes];
-[DYShaderProfilerResult effectivePerEncoderDrawKickTimes];
-[DYShaderProfilerResult encoderCount];
-[DYShaderProfilerResult encoderFunctionIndexList];
-[DYShaderProfilerResult encoderFunctionIndexToEncoderIndexMap];
-[DYShaderProfilerResult encoderIndexToLabelMap];
-[DYShaderProfilerResult fragmentTiming];
-[DYShaderProfilerResult perCommandBufferEncoderCount];
-[DYShaderProfilerResult programPipelineInfoList];
-[DYShaderProfilerResult setBlitEncoderTimeInfo:];
-[DYShaderProfilerResult setBlitTimeData:];
-[DYShaderProfilerResult setComputeTiming:];
-[DYShaderProfilerResult setDerivedCountersData:];
-[DYShaderProfilerResult setDeviceUtilization:];
-[DYShaderProfilerResult setDrawCallInfoList:];
-[DYShaderProfilerResult setEffectiveKickTimes:];
-[DYShaderProfilerResult setEffectivePerEncoderDrawKickTimes:];
-[DYShaderProfilerResult setEncoderCount:];
-[DYShaderProfilerResult setEncoderIndexToLabelMap:];
-[DYShaderProfilerResult setFragmentTiming:];
-[DYShaderProfilerResult setLoadActionTimes:];
-[DYShaderProfilerResult setPerCommandBufferEncoderCount:];
-[DYShaderProfilerResult setProgramPipelineInfoList:];
-[DYShaderProfilerResult setShaderProfilingFrameTimes:];
-[DYShaderProfilerResult setShaderProfilingTime:];
-[DYShaderProfilerResult setStoreActionTimes:];
-[DYShaderProfilerResult setVertexTiming:];
-[DYShaderProfilerResult shaderProfilingFrameTimes];
-[DYShaderProfilerResult shaderProfilingTime];
-[DYShaderProfilerResult storeActionTimes];
-[DYShaderProfilerResult vertexTiming];
```
