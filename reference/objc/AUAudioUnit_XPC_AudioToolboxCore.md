# `AUAudioUnit_XPC`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AUAudioUnit`
- 21 instance variables, 1 properties, 59 instance methods, 1 class methods

## Instance variables

```
@"NSXPCConnection" _xpcConnection;
{recursive_mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _propListenerMutex;
B _crashNotificationSent;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _mCrashNotificationMutex;
^{OpaqueAudioComponentInstance=} _componentInstance;
i _remotePID;
{mach_timebase_info="numer"I"denom"I} _remoteMachTimebaseInfo;
B _canRender;
B _canProcess;
B _removingObserverWithContext;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _parameterTreeMutex;
@"AUAudioUnitBusArray_XPC" _inputBusses;
@"AUAudioUnitBusArray_XPC" _outputBusses;
{unique_ptr<AUProcAndUserData, std::default_delete<AUProcAndUserData>>=""{?="__ptr_"^{AUProcAndUserData}}} _elementCountListenerToken;
{vector<AUAudioUnit_XPC_PropListener, std::allocator<AUAudioUnit_XPC_PropListener>>="__begin_"^{AUAudioUnit_XPC_PropListener}"__end_"^{AUAudioUnit_XPC_PropListener}""{?="__cap_"^{AUAudioUnit_XPC_PropListener}}} _propListeners;
{shared_ptr<caulk::synchronized<auoop::RenderPipePool, std::recursive_mutex>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} _renderPipePool;
{optional<auoop::RenderPipeUser>=""(?="__null_state_"c"__val_"{RenderPipeUser="mPipeSubPool"^{PipeSubPool}"mRenderClientUser"{AUOOPRenderClientUser="au"@"AUAudioUnit_XPC""xpcConnection"@"NSXPCConnection""musicalContextBlock"@?"transportStateBlock"@?"MIDIOutputEventBlock"@?"MIDIOutputEventListBlock"@?"serviceProcessAUInstanceToken"I"isOffline"B"isMIDIProcessor"B}"mInvalidated"{atomic<bool>="__a_"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>="__a_value"AB}}})"__engaged_"B} _renderPipeUser;
@"AUParameterTree" _cachedParameterTree;
@"NSArray" _userPresets;
{optional<bool>=""(?="__null_state_"c"__val_"B)"__engaged_"B} _localCachingDisabled;
@"NSUUID" _auInstanceUUID;
```

## Properties

```
@property (T@"NSUUID",R,N,V_auInstanceUUID) auInstanceUUID;
```

## Class methods

```
+[AUAudioUnit_XPC automaticallyNotifiesObserversForKey:];
```

## Instance methods

```
-[AUAudioUnit_XPC addObserver:forKeyPath:options:context:];
-[AUAudioUnit_XPC removeObserver:forKeyPath:];
-[AUAudioUnit_XPC valueForUndefinedKey:];
-[AUAudioUnit_XPC setCurrentPreset:];
-[AUAudioUnit_XPC dealloc];
-[AUAudioUnit_XPC reset];
-[AUAudioUnit_XPC didInvalidate];
-[AUAudioUnit_XPC setValue:forUndefinedKey:];
-[AUAudioUnit_XPC removeObserver:forKeyPath:context:];
-[AUAudioUnit_XPC XPCListenerEndpoint];
-[AUAudioUnit_XPC parametersForOverviewWithCount:];
-[AUAudioUnit_XPC _refreshBusses:];
-[AUAudioUnit_XPC _doOpen:completion:];
-[AUAudioUnit_XPC _getBus:scope:error:];
-[AUAudioUnit_XPC _getInvalidationNotificationInfo];
-[AUAudioUnit_XPC _getValueForKey:];
-[AUAudioUnit_XPC _getValueForProperty:error:];
-[AUAudioUnit_XPC _invalidatePipePoolAndUser];
-[AUAudioUnit_XPC _parameterTreeChanged];
-[AUAudioUnit_XPC _setBusCount:scope:error:];
-[AUAudioUnit_XPC _setComponentInstance:];
-[AUAudioUnit_XPC _setState:forKey:error:];
-[AUAudioUnit_XPC _setValue:forProperty:error:];
-[AUAudioUnit_XPC allocateRenderResourcesAndReturnError:];
-[AUAudioUnit_XPC auInstanceUUID];
-[AUAudioUnit_XPC audioUnitInstanceUUID];
-[AUAudioUnit_XPC cancelSpeechRequest];
-[AUAudioUnit_XPC deleteUserPreset:error:];
-[AUAudioUnit_XPC didCrash:];
-[AUAudioUnit_XPC disableProfile:cable:onChannel:error:];
-[AUAudioUnit_XPC enableProfile:cable:onChannel:error:];
-[AUAudioUnit_XPC getV2Parameter:sequenceNumber:];
-[AUAudioUnit_XPC inputBusses];
-[AUAudioUnit_XPC internalDeallocateRenderResources];
-[AUAudioUnit_XPC internalRenderBlock];
-[AUAudioUnit_XPC invalidateAllParameters];
-[AUAudioUnit_XPC isLoadedInProcess];
-[AUAudioUnit_XPC isLocalCachingDisabled];
-[AUAudioUnit_XPC messageChannelFor:];
-[AUAudioUnit_XPC outputBusses];
-[AUAudioUnit_XPC parameterTree];
-[AUAudioUnit_XPC presetStateFor:error:];
-[AUAudioUnit_XPC profileStateForCable:channel:];
-[AUAudioUnit_XPC propertiesChanged:];
-[AUAudioUnit_XPC providesUserInterface];
-[AUAudioUnit_XPC remoteProcessAuditToken];
-[AUAudioUnit_XPC remoteProcessIdentifier];
-[AUAudioUnit_XPC remoteReset];
-[AUAudioUnit_XPC saveUserPreset:error:];
-[AUAudioUnit_XPC selectViewConfiguration:];
-[AUAudioUnit_XPC setFullState:];
-[AUAudioUnit_XPC setFullStateForDocument:];
-[AUAudioUnit_XPC setLocalCachingDisabled:];
-[AUAudioUnit_XPC setMusicalContextBlock:];
-[AUAudioUnit_XPC setTransportStateBlock:];
-[AUAudioUnit_XPC speechVoices];
-[AUAudioUnit_XPC supportedViewConfigurations:];
-[AUAudioUnit_XPC synthesizeSpeechRequest:];
-[AUAudioUnit_XPC userPresets];
```
