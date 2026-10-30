# `AURemoteHost`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AUAudioUnitXPCProtocol`
- 19 instance variables, 6 properties, 63 instance methods, 1 class methods

## Instance variables

```
@"AUAudioUnit" _audioUnit;
@"NSXPCConnection" _remoteHostXPCConnection;
{optional<AUOOPRenderingServerUser>=""(?="__null_state_"c"__val_"{AUOOPRenderingServerUser="_vptr$Root"^^?"mToken"I"mAUAudioUnit"@"AUAudioUnit""mRetainedRenderBlock"@?"mRenderBlock"@?"mCanProcessInPlace"B"mIsV2AudioUnit"B"mMIDIOutBaseSampleTime"q"mEventSchedule"^{AUEventSchedule}"mSharedBuffers"^{AUOOPSharedMemory}"mRenderThreadId"{optional<std::__thread_id>=""(?="__null_state_"c"__val_"{__thread_id="__id_"^{_opaque_pthread_t}})"__engaged_"B}})"__engaged_"B} _renderServerUser;
@"NSObject<OS_voucher>" _initializationVoucher;
@"AUParameterTree" _cachedParameterTree;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _parameterTreeMutex;
{reply_watchdog_factory="mDebugging"B"mDefaultTimeoutMS"i"mTimeoutHandler"{function<void ()>="__f_"{__value_func<void ()>="__buf_"(type="__data"[24C])"__f_"^v}}} _replyWatchdogFactory;
@"NSObject<OS_dispatch_queue>" _presetMonitoringQueue;
@"NSObject<OS_dispatch_source>" _presetFolderWatcher;
@"NSMutableArray" _userPresets;
@"NSUUID" _audioUnitUUID;
{shared_ptr<auoop::WorkgroupMirror>="__ptr_"^{WorkgroupMirror}"__cntrl_"^{__shared_weak_count}} _workgroupMirror;
{KVOAggregator="mRecords"{vector<KVOAggregator::Record, std::allocator<KVOAggregator::Record>>="__begin_"^{Record}"__end_"^{Record}""{?="__cap_"^{Record}}}} _kvoAggregator;
{vector<AURemoteMessageChannel *, std::allocator<AURemoteMessageChannel *>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _remoteMessageChannels;
{unique_ptr<XOSTransactor, std::default_delete<XOSTransactor>>=""{?="__ptr_"^{XOSTransactor}}} _transactorIO;
B _localCachingDisabled;
i _deferPropertyChangeNotifications;
@"NSObject<OS_dispatch_queue>" _propertyObserverQueue;
@"NSMutableArray" _pendingChangedProperties;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_propertyObserverQueue) propertyObserverQueue;
@property (Ti,N,V_deferPropertyChangeNotifications) deferPropertyChangeNotifications;
@property (T@"NSMutableArray",R,N,V_pendingChangedProperties) pendingChangedProperties;
@property (T{?=[8I]},R,N) hostAuditToken;
@property (T@"NSUUID",R,N,V_audioUnitUUID) audioUnitUUID;
@property (TB,N,V_localCachingDisabled) localCachingDisabled;
```

## Class methods

```
+[AURemoteHost _staticInit];
```

## Instance methods

```
-[AURemoteHost reset:];
-[AURemoteHost close:];
-[AURemoteHost observeValueForKeyPath:ofObject:change:context:];
-[AURemoteHost dealloc];
-[AURemoteHost hostAuditToken];
-[AURemoteHost initialize:reply:];
-[AURemoteHost openImpl:reply:];
-[AURemoteHost startUserPresetFolderMonitoring];
-[AURemoteHost _fetchAndClearPendingChangedProperties];
-[AURemoteHost _getBus:scope:error:];
-[AURemoteHost _getSpeechSynthesisProviderAudioUnit];
-[AURemoteHost _identifyBus:scope:element:];
-[AURemoteHost addPropertyObserver:context:reply:];
-[AURemoteHost audioUnit];
-[AURemoteHost audioUnitUUID];
-[AURemoteHost cancelSpeechRequest:];
-[AURemoteHost createRenderPipe:formats:maxFrames:midiOutSizeHint:resources:reply:];
-[AURemoteHost currentParameterTree];
-[AURemoteHost deferPropertyChangeNotifications];
-[AURemoteHost deleteUserPreset:reply:];
-[AURemoteHost destroyRenderPipe:reply:];
-[AURemoteHost disableProfile:cable:onChannel:reply:];
-[AURemoteHost enableProfile:cable:onChannel:reply:];
-[AURemoteHost getBusses:reply:];
-[AURemoteHost getCustomMessageChannelFor:reply:];
-[AURemoteHost getParameter:sequenceNumber:reply:];
-[AURemoteHost getParameterTree:];
-[AURemoteHost getSpeechVoices:];
-[AURemoteHost initWithConnection:config:];
-[AURemoteHost initWithConnection:config:timeOutHandler:];
-[AURemoteHost loadUserPresets:];
-[AURemoteHost localCachingDisabled];
-[AURemoteHost localCachingDisabled:newValue:reply:];
-[AURemoteHost open:instanceUUID:reply:];
-[AURemoteHost parameterNode:displayNameWithLength:reply:];
-[AURemoteHost parameterStringFromValue:currentValue:address:reply:];
-[AURemoteHost parameterValueFromString:address:reply:];
-[AURemoteHost parametersForOverviewWithCount:reply:];
-[AURemoteHost pendingChangedProperties];
-[AURemoteHost presetStateFor:reply:];
-[AURemoteHost profileStateForCable:channel:reply:];
-[AURemoteHost propertyObserverQueue];
-[AURemoteHost readHostEntitlement:];
-[AURemoteHost removePropertyObserver:context:reply:];
-[AURemoteHost retrieveInstanceUUID:];
-[AURemoteHost saveUserPreset:state:reply:];
-[AURemoteHost selectViewConfiguration:reply:];
-[AURemoteHost setBlocks];
-[AURemoteHost setBusCount:scope:reply:];
-[AURemoteHost setBusFormat:scope:format:reply:];
-[AURemoteHost setBusName:scope:name:reply:];
-[AURemoteHost setDeferPropertyChangeNotifications:];
-[AURemoteHost setLocalCachingDisabled:];
-[AURemoteHost setValue:forKey:reply:];
-[AURemoteHost setValue:forProperty:propagateError:reply:];
-[AURemoteHost supportedViewConfigurations:reply:];
-[AURemoteHost syncParameter:value:extOriginator:hostTime:eventType:];
-[AURemoteHost synthesizeSpeechRequest:reply:];
-[AURemoteHost uninitialize:];
-[AURemoteHost updateHostCallbacks:reply:];
-[AURemoteHost updateWorkgroupMirror:reply:];
-[AURemoteHost valueForKey:reply:];
-[AURemoteHost valueForProperty:propagateError:reply:];
```
