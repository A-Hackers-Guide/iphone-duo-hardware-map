# `PasscodeDetectionDSPHost`

- Image: [`/System/Library/PrivateFrameworks/CoreAudioOrchestration.framework/CoreAudioOrchestration`](../userland/System__Library__PrivateFrameworks__CoreAudioOrchestration.framework__CoreAudioOrchestration.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OrchestratedDSPObject`
- 9 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
@ mADMFactory;
{PasscodeDetectorDSPHostContext="dspHost"@"PasscodeDetectionDSPHost"} mBoxedSelf;
B mReadyCallbackFired;
^? mReadyForStartCallback;
^v mRecruiterData;
{HALToOrchestrationDSPHostCallbacks="doIO"^?"start"^?"stop"^?"refCon"^v} mOrchestrationCallbacks;
{optional<OrchestrationDSPHostToHALCallbacks>=""(?="__null_state_"c"__val_"{OrchestrationDSPHostToHALCallbacks="toUCID"^?"refCon"^v})"__engaged_"B} mHALCallbacks;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} mDeviceContextMutex;
{unordered_map<std::string, DeviceContext, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, DeviceContext>>>="__table_"{__hash_table<std::__hash_value_type<std::string, DeviceContext>, std::__unordered_map_hasher<std::string, std::pair<const std::string, DeviceContext>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::pair<const std::string, DeviceContext>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::pair<const std::string, DeviceContext>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, DeviceContext>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, DeviceContext>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, DeviceContext>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, DeviceContext>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} mDeviceContexts;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PasscodeDetectionDSPHost deviceUIDs];
```

## Instance methods

```
-[PasscodeDetectionDSPHost dealloc];
-[PasscodeDetectionDSPHost SetupDeviceListener:];
-[PasscodeDetectionDSPHost GetCallbacksFromPlugin:];
-[PasscodeDetectionDSPHost InjectCallbacksToPlugin:];
-[PasscodeDetectionDSPHost RecruitDevice:pluginID:fireRecruitCallback:];
-[PasscodeDetectionDSPHost stopDSP];
-[PasscodeDetectionDSPHost TranslateAudioObjectIDToUCIDViaHAL:];
-[PasscodeDetectionDSPHost initWithCallback:inRecruiterData:inADMFactory:outStatus:];
-[PasscodeDetectionDSPHost processDSPWithNow:inInputData:inInputTime:inOutputData:inOutputTime:];
-[PasscodeDetectionDSPHost startDSP];
```
