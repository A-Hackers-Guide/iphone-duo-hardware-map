# `_ANEProgramForEvaluation`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 6 properties, 21 instance methods, 3 class methods

## Instance variables

```
{unordered_map<unsigned long long, MutableWeightsEntry, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, MutableWeightsEntry>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long long, MutableWeightsEntry>, std::__unordered_map_hasher<unsigned long long, std::pair<const unsigned long long, MutableWeightsEntry>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::pair<const unsigned long long, MutableWeightsEntry>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::pair<const unsigned long long, MutableWeightsEntry>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, MutableWeightsEntry>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, MutableWeightsEntry>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, MutableWeightsEntry>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, MutableWeightsEntry>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _mutableWeightsMap;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _mutableWeightsMapLock;
c _queueDepth;
@"_ANEDeviceController" _controller;
Q _programHandle;
Q _intermediateBufferHandle;
@"NSObject<OS_dispatch_semaphore>" _requestsInFlight;
q _currentAsyncRequestsInFlight;
```

## Properties

```
@property (T@"_ANEDeviceController",R,N,V_controller) controller;
@property (TQ,N,V_programHandle) programHandle;
@property (TQ,N,V_intermediateBufferHandle) intermediateBufferHandle;
@property (Tc,R,N,V_queueDepth) queueDepth;
@property (T@"NSObject<OS_dispatch_semaphore>",R,N,V_requestsInFlight) requestsInFlight;
@property (Tq,V_currentAsyncRequestsInFlight) currentAsyncRequestsInFlight;
```

## Class methods

```
+[_ANEProgramForEvaluation new];
+[_ANEProgramForEvaluation programWithController:intermediateBufferHandle:queueDepth:];
+[_ANEProgramForEvaluation programWithHandle:intermediateBufferHandle:queueDepth:];
```

## Instance methods

```
-[_ANEProgramForEvaluation programInferenceOtherErrorForMessage:model:methodName:];
-[_ANEProgramForEvaluation controller];
-[_ANEProgramForEvaluation deviceController];
-[_ANEProgramForEvaluation init];
-[_ANEProgramForEvaluation intermediateBufferHandle];
-[_ANEProgramForEvaluation dealloc];
-[_ANEProgramForEvaluation processOutputSet:model:options:error:];
-[_ANEProgramForEvaluation mapMutableWeightsBufferDirectForProcedure:bufferID:buffer:size:error:];
-[_ANEProgramForEvaluation processInputBuffers:model:options:error:];
-[_ANEProgramForEvaluation processRequest:model:qos:qIndex:modelStringID:options:returnValue:error:];
-[_ANEProgramForEvaluation setCurrentAsyncRequestsInFlight:];
-[_ANEProgramForEvaluation description];
-[_ANEProgramForEvaluation initWithController:intermediateBufferHandle:queueDepth:];
-[_ANEProgramForEvaluation queueDepth];
-[_ANEProgramForEvaluation requestsInFlight];
-[_ANEProgramForEvaluation setProgramHandle:];
-[_ANEProgramForEvaluation currentAsyncRequestsInFlight];
-[_ANEProgramForEvaluation programHandle];
-[_ANEProgramForEvaluation setIntermediateBufferHandle:];
-[_ANEProgramForEvaluation processSessionHint:options:report:error:];
-[_ANEProgramForEvaluation unmapMutableWeightsBufferDirectForProcedure:bufferID:];
```
