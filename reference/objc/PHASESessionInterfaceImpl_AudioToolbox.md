# `PHASESessionInterfaceImpl`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PHASESessionInterface`
- 7 instance variables, 5 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"ATPhasePlatform" _phasePlatform;
{recursive_mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _callbackMutex;
@? _muteSessionInputBlock;
@? _fadeSessionOutputBlock;
@? _activateSessionBlock;
@ _sessionVolumeImpl;
{unordered_map<unsigned int, std::unordered_set<void *>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, std::unordered_set<void *>>>>="__table_"{__hash_table<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, std::__unordered_map_hasher<unsigned int, std::pair<const unsigned int, std::unordered_set<void *>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::pair<const unsigned int, std::unordered_set<void *>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::pair<const unsigned int, std::unordered_set<void *>>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} audioSessionInputClients;
```

## Properties

```
@property (T@"<PHASESessionVolumeInterface>",?,R,N) sessionVolumeInterface;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PHASESessionInterfaceImpl init];
-[PHASESessionInterfaceImpl dealloc];
-[PHASESessionInterfaceImpl muteSessionInput:mute:fadeTime:];
-[PHASESessionInterfaceImpl setClientStateOnSession:clientToken:modes:state:outDuckingInfo:];
-[PHASESessionInterfaceImpl activateSession:activate:];
-[PHASESessionInterfaceImpl fadeClientsInSession:activating:fadeLevel:fadeTime:];
-[PHASESessionInterfaceImpl getInputMuteStateForSession:fromCallback:];
-[PHASESessionInterfaceImpl initWithPhasePlatform:];
-[PHASESessionInterfaceImpl lazyInitSessionVolumeInterface];
-[PHASESessionInterfaceImpl refreshInputMuteOnAllSessions:];
-[PHASESessionInterfaceImpl registerActivateAudioSessionBlock:];
-[PHASESessionInterfaceImpl registerFadeClientsInAudioSessionBlock:];
-[PHASESessionInterfaceImpl registerMuteInputClientsInAudioSessionBlock:];
-[PHASESessionInterfaceImpl removeInputClientToken:fromSessionID:];
-[PHASESessionInterfaceImpl sessionVolumeInterface];
-[PHASESessionInterfaceImpl setClientStateFromCallbackOnSession:clientToken:modes:state:outDuckingInfo:];
-[PHASESessionInterfaceImpl setInputMuteStateFromCallbackOnSession:clientToken:isMuted:];
-[PHASESessionInterfaceImpl setInputMuteStateOnSession:clientToken:isMuted:];
```
