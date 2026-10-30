# `STSController`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 0 properties, 12 instance methods, 2 class methods

## Instance variables

```
^{OpaqueFigSTS=} _sts;
{unordered_map<std::string, STSPerLabelControllerState, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, STSPerLabelControllerState>>>="__table_"{__hash_table<std::__hash_value_type<std::string, STSPerLabelControllerState>, std::__unordered_map_hasher<std::string, std::pair<const std::string, STSPerLabelControllerState>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, STSPerLabelControllerState>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, STSPerLabelControllerState>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _perLabelState;
{stack<unsigned long, std::deque<unsigned long>>="c"{deque<unsigned long, std::allocator<unsigned long>>="__map_"{__split_buffer<unsigned long *, std::allocator<unsigned long *>>="__first_"^^Q"__begin_"^^Q"__end_"^^Q""{?="__cap_"^^Q}}"__start_"Q""{?="__size_"Q}}} _availableIndicesWithinSharedStorage;
{STSActiveIndices="m_activeLabels"Q} _activeIndices;
{STSGlobalState="hostTime"Q"listenerTransform"{?="columns"[4]}} _globalState;
Q _globalGeneration;
^v _sharedStorage;
{semaphore="mMachSem"I"mOwned"B} _controlSemaphore;
Q _shmemSize;
B _allowAutomaticHeadTracking;
```

## Class methods

```
+[STSController maxLabelLength];
+[STSController maxNumberOfPerLabelStates];
```

## Instance methods

```
-[STSController dealloc];
-[STSController _updateGlobalState:didChange:error:];
-[STSController cleanupAllLabels];
-[STSController cleanupLabel:];
-[STSController ensureResourcesAllocatedForLabel:error:];
-[STSController initWithSTSObject:error:];
-[STSController signalChangeWithError:];
-[STSController updateGlobalState:didChange:error:];
-[STSController updateGlobalState:labelStates:additionalLabelInfo:error:];
-[STSController updateGlobalState:labelStates:error:];
-[STSController updateLabel:state:didChange:additionalInfo:error:];
-[STSController updateLabel:state:didChange:error:];
```
