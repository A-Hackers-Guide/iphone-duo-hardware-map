# `AUAudioUnit`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 43 instance variables, 52 properties, 123 instance methods, 14 class methods

## Instance variables

```
{weak_ptr<APComponent>="__ptr_"^{APComponent}"__cntrl_"^{__shared_weak_count}} _component;
@"NSString" _componentName;
I _componentVersion;
@"UIViewController" _cachedViewController;
I _maximumFramesToRender;
q _MIDIOutputBufferSizeHint;
{RealtimeState="mMultipleRenderMutex"{pooled_semaphore_mutex="mCountAndSema"{atomic<caulk::pooled_semaphore_mutex::CountAndSema>="__a_"{__cxx_atomic_impl<caulk::pooled_semaphore_mutex::CountAndSema, std::__cxx_atomic_base_impl<caulk::pooled_semaphore_mutex::CountAndSema>>="__a_value"A{CountAndSema}}}}"mResetVsRenderMutex"{pooled_semaphore_mutex="mCountAndSema"{atomic<caulk::pooled_semaphore_mutex::CountAndSema>="__a_"{__cxx_atomic_impl<caulk::pooled_semaphore_mutex::CountAndSema, std::__cxx_atomic_base_impl<caulk::pooled_semaphore_mutex::CountAndSema>>="__a_value"A{CountAndSema}}}}"renderObserverList"{RenderObserverList="mObservers"{TThreadSafeList<RenderObserver>="mActiveList"{NodeStack="mHead"^{Node}}"mPendingList"{NodeStack="mHead"^{Node}}"mFreeList"{NodeStack="mHead"^{Node}}}"mTouched"B}"eventSchedule"{AUEventSchedule="mAUv2GetParameterSynchronizer"^{AUv2GetParameterSynchronizer}"mAllocator"^{AURenderEventAllocator}"mScheduledParameterRefresher"^{AUScheduledParameterRefresher2}"mAddedEventQueue"{lf_mpsc_queue<AURenderEventNode, caulk::concurrent::intrusive_single_link_member<AURenderEventNode, &AURenderEventNode::next>, true>="mEnqueueHead"{atomic<AURenderEventNode *>="__a_"{__cxx_atomic_impl<AURenderEventNode *, std::__cxx_atomic_base_impl<AURenderEventNode *>>="__a_value"A^{AURenderEventNode}}}"mDequeueHead"{prepadded_t<AURenderEventNode *, 248UL>="padding"[248C]"value"^{AURenderEventNode}}}"mHavePendingSetParameter"{atomic<bool>="__a_"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>="__a_value"AB}}"mScheduleHead"^(AURenderEvent)"mOwningAU"^v"mRenderBlock"@?"mPreviousRenderTime"{PreviousRenderTime="mSampleRate"d"mLastRender"{atomic<PreviousRenderTime::Snapshot>="__a_"{__cxx_atomic_impl<PreviousRenderTime::Snapshot, std::__cxx_atomic_base_impl<PreviousRenderTime::Snapshot>>="__a_value"A{Snapshot}}}}}"auv2GetParameterSynchronizer"{AUv2GetParameterSynchronizer="mSeqNums"{atomic<AUv2GetParameterSynchronizer::SeqNumPair>="__a_"{__cxx_atomic_impl<AUv2GetParameterSynchronizer::SeqNumPair, std::__cxx_atomic_base_impl<AUv2GetParameterSynchronizer::SeqNumPair>>="__a_value"A{SeqNumPair}}}"mSyncGetParamSema"{semaphore="mImpl"{semaphore="mMachSem"I"mOwned"B}"mCounter"{atomic<int>="__a_"{__cxx_atomic_impl<int, std::__cxx_atomic_base_impl<int>>="__a_value"Ai}}"mOriginalCounter"i}}"contextChangeGenerator"{optional<RenderContextChangeGenerator>=""(?="__null_state_"c"__val_"{RenderContextChangeGenerator="mLastWorkgroup"^v"mObserver"@?})"__engaged_"B}"renderBlockType"i"cachedMIDIProtocol"i} _realtimeState;
@"AUParameterTree" _parameterTree;
@"NSMutableArray" _userPresets;
B _isLoadedInProcess;
@"NSObject<OS_dispatch_queue>" _presetMonitoringQueue;
@"NSObject<OS_dispatch_source>" _presetFolderWatcher;
@? _MIDIOutputEventBlock;
@? _MIDIOutputEventListBlock;
@? _MIDIOutputEventHostBlock;
@? _MIDIOutputEventListHostBlock;
B _shouldUseMIDI2;
B _localCachingDisabled;
B _renderResourcesAllocated;
B _allParameterValues;
B _shouldBypassEffect;
B _canProcessInPlace;
B _renderingOffline;
B _supportsMPE;
B _requestViewControllerSynchronously;
i _AudioUnitMIDIProtocol;
i _hostMIDIProtocol;
@"NSString" _audioUnitShortName;
q _virtualMIDICableCount;
@"NSArray" _factoryPresets;
@"AUAudioUnitPreset" _currentPreset;
d _latency;
d _tailTime;
q _renderQuality;
@? _musicalContextBlock;
@? _transportStateBlock;
@"NSString" _contextName;
@"NSArray" _migrateFromPlugin;
@"NSArray" _channelMap;
@? _profileChangedBlock;
@"NSURL" _iconURL;
@"AUv3HostIdentifier" _hostIdentifier;
{AudioComponentDescription="componentType"I"componentSubType"I"componentManufacturer"I"componentFlags"I"componentFlagsMask"I} _componentDescription;
```

## Properties

```
@property (T@?,R,N) internalRenderBlock;
@property (T@?,R,N) renderContextObserver;
@property (Tq,N) MIDIOutputBufferSizeHint;
@property (T@"NSURL",R,N,V_iconURL) iconURL;
@property (T@"AUv3HostIdentifier",&,N,V_hostIdentifier) hostIdentifier;
@property (TB,N,V_requestViewControllerSynchronously) requestViewControllerSynchronously;
@property (T{AudioComponentDescription=IIIII},R,N,V_componentDescription) componentDescription;
@property (T^{OpaqueAudioComponent=},R,N) component;
@property (T@"NSString",R,C,N) componentName;
@property (T@"NSString",R,C,N) audioUnitName;
@property (T@"NSString",R,C,N) manufacturerName;
@property (T@"NSString",R,C,N,V_audioUnitShortName) audioUnitShortName;
@property (TI,R,N) componentVersion;
@property (TB,R,N,V_renderResourcesAllocated) renderResourcesAllocated;
@property (T@"AUAudioUnitBusArray",R,N) inputBusses;
@property (T@"AUAudioUnitBusArray",R,N) outputBusses;
@property (T@?,R,N) renderBlock;
@property (T@?,R,N) scheduleParameterBlock;
@property (TI,N) maximumFramesToRender;
@property (T@"AUParameterTree",&,N) parameterTree;
@property (TB,R,N,V_allParameterValues) allParameterValues;
@property (TB,R,N,GisMusicDeviceOrEffect) musicDeviceOrEffect;
@property (Tq,R,N,V_virtualMIDICableCount) virtualMIDICableCount;
@property (T@?,R,N) scheduleMIDIEventBlock;
@property (T@?,R,N) scheduleMIDIEventListBlock;
@property (T@"NSArray",R,C,N) MIDIOutputNames;
@property (TB,R,N) providesUserInterface;
@property (T@?,C,N) MIDIOutputEventBlock;
@property (T@?,C,N) MIDIOutputEventListBlock;
@property (Ti,R,N,V_AudioUnitMIDIProtocol) AudioUnitMIDIProtocol;
@property (Ti,N,V_hostMIDIProtocol) hostMIDIProtocol;
@property (T@"NSDictionary",C,N) fullState;
@property (T@"NSDictionary",C,N) fullStateForDocument;
@property (T@"NSArray",R,C,N,V_factoryPresets) factoryPresets;
@property (T@"NSArray",R,C,N) userPresets;
@property (TB,R,N) supportsUserPresets;
@property (TB,R,N) isLoadedInProcess;
@property (T@"AUAudioUnitPreset",&,N,V_currentPreset) currentPreset;
@property (Td,R,N,V_latency) latency;
@property (Td,R,N,V_tailTime) tailTime;
@property (Tq,N,V_renderQuality) renderQuality;
@property (TB,N,V_shouldBypassEffect) shouldBypassEffect;
@property (TB,R,N,V_canProcessInPlace) canProcessInPlace;
@property (TB,N,GisRenderingOffline,V_renderingOffline) renderingOffline;
@property (T@"NSArray",R,C,N) channelCapabilities;
@property (T@?,C,N,V_musicalContextBlock) musicalContextBlock;
@property (T@?,C,N,V_transportStateBlock) transportStateBlock;
@property (T@"NSString",C,N,V_contextName) contextName;
@property (T@"NSArray",R,N,V_migrateFromPlugin) migrateFromPlugin;
@property (TB,R,N,V_supportsMPE) supportsMPE;
@property (T@"NSArray",C,N,V_channelMap) channelMap;
@property (T@?,C,N,V_profileChangedBlock) profileChangedBlock;
```

## Class methods

```
+[AUAudioUnit __presetFromPath:];
+[AUAudioUnit __sanitizeFileName:];
+[AUAudioUnit __sanitizePresetNumber:];
+[AUAudioUnit __userPresetPath:error:];
+[AUAudioUnit _deleteUserPreset:error:];
+[AUAudioUnit _loadUserPresets:error:];
+[AUAudioUnit _monitorUserPresets:callback:];
+[AUAudioUnit _presetStateFor:error:];
+[AUAudioUnit _saveUserPreset:state:error:];
+[AUAudioUnit auAudioUnitForAudioUnit:];
+[AUAudioUnit instantiateWithComponentDescription:options:completionHandler:];
+[AUAudioUnit instantiateWithComponentDescription:options:connectionProvider:completionHandler:];
+[AUAudioUnit keyPathsForValuesAffectingAllParameterValues];
+[AUAudioUnit registerSubclass:asComponentDescription:name:version:];
```

## Instance methods

```
-[AUAudioUnit setHostIdentifier:];
-[AUAudioUnit hostIdentifier];
-[AUAudioUnit latency];
-[AUAudioUnit requestViewControllerWithCompletionHandler:];
-[AUAudioUnit valueForUndefinedKey:];
-[AUAudioUnit init];
-[AUAudioUnit currentPreset];
-[AUAudioUnit setCurrentPreset:];
-[AUAudioUnit initWithComponentDescription:options:error:];
-[AUAudioUnit dealloc];
-[AUAudioUnit componentName];
-[AUAudioUnit reset];
-[AUAudioUnit component];
-[AUAudioUnit tokenByAddingRenderObserver:];
-[AUAudioUnit addRenderObserver:userData:];
-[AUAudioUnit deallocateRenderResources];
-[AUAudioUnit manufacturerName];
-[AUAudioUnit contextName];
-[AUAudioUnit iconURL];
-[AUAudioUnit setValue:forUndefinedKey:];
-[AUAudioUnit removeRenderObserver:userData:];
-[AUAudioUnit removeRenderObserver:];
-[AUAudioUnit componentVersion];
-[AUAudioUnit MIDIOutputNames];
-[AUAudioUnit MIDIOutputBufferSizeHint];
-[AUAudioUnit MIDIOutputEventListBlock];
-[AUAudioUnit parametersForOverviewWithCount:];
-[AUAudioUnit setContextName:];
-[AUAudioUnit AudioUnitMIDIProtocol];
-[AUAudioUnit MIDIOutputEventBlock];
-[AUAudioUnit startUserPresetFolderMonitoring];
-[AUAudioUnit _setValue:forKey:error:];
-[AUAudioUnit _valueForProperty:error:];
-[AUAudioUnit allParameterValues];
-[AUAudioUnit allocateRenderResourcesAndReturnError:];
-[AUAudioUnit audioUnit];
-[AUAudioUnit audioUnitName];
-[AUAudioUnit audioUnitShortName];
-[AUAudioUnit auv2GetParameterSynchronizer];
-[AUAudioUnit cachedViewController];
-[AUAudioUnit canProcessInPlace];
-[AUAudioUnit channelCapabilities];
-[AUAudioUnit channelMap];
-[AUAudioUnit componentDescription];
-[AUAudioUnit deleteUserPreset:error:];
-[AUAudioUnit deliverV2Parameters:];
-[AUAudioUnit disableProfile:cable:onChannel:error:];
-[AUAudioUnit enableProfile:cable:onChannel:error:];
-[AUAudioUnit eventSchedule];
-[AUAudioUnit factoryPresets];
-[AUAudioUnit flushEventSchedule];
-[AUAudioUnit fullState];
-[AUAudioUnit fullStateForDocument];
-[AUAudioUnit getV2Parameter:sequenceNumber:];
-[AUAudioUnit hostMIDIProtocol];
-[AUAudioUnit initWithComponentDescription:error:];
-[AUAudioUnit inputBusses];
-[AUAudioUnit internalDeallocateRenderResources];
-[AUAudioUnit internalRenderBlock];
-[AUAudioUnit invalidateAudioUnit];
-[AUAudioUnit isHeadTrackingBinauralRenderer];
-[AUAudioUnit isLoadedInProcess];
-[AUAudioUnit isLocalCachingDisabled];
-[AUAudioUnit isMusicDeviceOrEffect];
-[AUAudioUnit isRenderingOffline];
-[AUAudioUnit isSpeechSynthesisProvider];
-[AUAudioUnit maximumFramesToRender];
-[AUAudioUnit messageChannelFor:];
-[AUAudioUnit migrateFromPlugin];
-[AUAudioUnit musicalContextBlock];
-[AUAudioUnit osWorkgroup];
-[AUAudioUnit outputBusses];
-[AUAudioUnit parameterTree];
-[AUAudioUnit presetStateFor:error:];
-[AUAudioUnit profileChangedBlock];
-[AUAudioUnit profileStateForCable:channel:];
-[AUAudioUnit providesUserInterface];
-[AUAudioUnit remoteProcessAuditToken];
-[AUAudioUnit remoteProcessIdentifier];
-[AUAudioUnit renderBlock];
-[AUAudioUnit renderContextObserver];
-[AUAudioUnit renderQuality];
-[AUAudioUnit renderResourcesAllocated];
-[AUAudioUnit requestViewControllerSynchronously];
-[AUAudioUnit resolveComponent];
-[AUAudioUnit saveUserPreset:error:];
-[AUAudioUnit scheduleMIDIEventBlock];
-[AUAudioUnit scheduleMIDIEventListBlock];
-[AUAudioUnit scheduleParameterBlock];
-[AUAudioUnit scheduledParameterRefresher];
-[AUAudioUnit selectViewConfiguration:];
-[AUAudioUnit setCachedViewController:];
-[AUAudioUnit setChannelMap:];
-[AUAudioUnit setFullState:];
-[AUAudioUnit setFullStateForDocument:];
-[AUAudioUnit setHostMIDIProtocol:];
-[AUAudioUnit setLoadedOutOfProcess];
-[AUAudioUnit setLocalCachingDisabled:];
-[AUAudioUnit setMIDIOutputBufferSizeHint:];
-[AUAudioUnit setMIDIOutputEventBlock:];
-[AUAudioUnit setMIDIOutputEventListBlock:];
-[AUAudioUnit setMaximumFramesToRender:];
-[AUAudioUnit setMusicalContextBlock:];
-[AUAudioUnit setParameterTree:];
-[AUAudioUnit setProfileChangedBlock:];
-[AUAudioUnit setRenderQuality:];
-[AUAudioUnit setRenderResourcesAllocated:];
-[AUAudioUnit setRenderingOffline:];
-[AUAudioUnit setRequestViewControllerSynchronously:];
-[AUAudioUnit setShouldBypassEffect:];
-[AUAudioUnit setTransportStateBlock:];
-[AUAudioUnit setV2Parameter:value:bufferOffset:sequenceNumber:];
-[AUAudioUnit setupMIDIConversion];
-[AUAudioUnit shouldBypassEffect];
-[AUAudioUnit shouldChangeToFormat:forBus:];
-[AUAudioUnit supportedViewConfigurations:];
-[AUAudioUnit supportsMPE];
-[AUAudioUnit supportsUserPresets];
-[AUAudioUnit tailTime];
-[AUAudioUnit tearDownExtension];
-[AUAudioUnit transportStateBlock];
-[AUAudioUnit userPresets];
-[AUAudioUnit virtualMIDICableCount];
```
