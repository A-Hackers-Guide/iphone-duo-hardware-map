# `/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`

iOS 27.2 dyld shared cache image. Version `293.200.0.0.0`. **[DSC]**

## Linked libraries (11)

- `/System/Library/PrivateFrameworks/caulk.framework/caulk`
- `/System/Library/Frameworks/Security.framework/Security`
- `/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`
- `/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`
- `/usr/lib/libAudioStatistics.dylib`
- `/usr/lib/libMobileGestalt.dylib`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 26 classes, 12 protocols, 717 methods, 201 properties

### Class pages

Every class and protocol, with its methods: [`AVHapticClient`](../objc/AVHapticClient_CoreHaptics.md), [`AVHapticParameterCurveValue`](../objc/AVHapticParameterCurveValue_CoreHaptics.md), [`AVHapticPlayer`](../objc/AVHapticPlayer_CoreHaptics.md), [`AVHapticPlayerChannel`](../objc/AVHapticPlayerChannel_CoreHaptics.md), [`AVHapticSequence`](../objc/AVHapticSequence_CoreHaptics.md), [`AVHapticSequenceEntry`](../objc/AVHapticSequenceEntry_CoreHaptics.md), [`AdvancedPatternPlayer`](../objc/AdvancedPatternPlayer_CoreHaptics.md), [`CHDefaultHapticDeviceCapability`](../objc/CHDefaultHapticDeviceCapability_CoreHaptics.md), [`CHEmbeddedAudioResourceInfo`](../objc/CHEmbeddedAudioResourceInfo_CoreHaptics.md), [`CHHapticAdvancedPatternPlayer`](../objc/CHHapticAdvancedPatternPlayer_CoreHaptics.protocol.md), [`CHHapticAdvancedPatternPlayerExtended`](../objc/CHHapticAdvancedPatternPlayerExtended_CoreHaptics.protocol.md), [`CHHapticClientInterface`](../objc/CHHapticClientInterface_CoreHaptics.protocol.md), [`CHHapticDeviceCapability`](../objc/CHHapticDeviceCapability_CoreHaptics.protocol.md), [`CHHapticDynamicParameter`](../objc/CHHapticDynamicParameter_CoreHaptics.md), [`CHHapticEngine`](../objc/CHHapticEngine_CoreHaptics.md), [`CHHapticEvent`](../objc/CHHapticEvent_CoreHaptics.md), [`CHHapticEventParameter`](../objc/CHHapticEventParameter_CoreHaptics.md), [`CHHapticParameterAttributes`](../objc/CHHapticParameterAttributes_CoreHaptics.protocol.md), [`CHHapticParameterAttributesImpl`](../objc/CHHapticParameterAttributesImpl_CoreHaptics.md), [`CHHapticParameterCurve`](../objc/CHHapticParameterCurve_CoreHaptics.md), [`CHHapticParameterCurveControlPoint`](../objc/CHHapticParameterCurveControlPoint_CoreHaptics.md), [`CHHapticPattern`](../objc/CHHapticPattern_CoreHaptics.md), [`CHHapticPatternPlayer`](../objc/CHHapticPatternPlayer_CoreHaptics.protocol.md), [`CHHapticPatternPlayerExtended`](../objc/CHHapticPatternPlayerExtended_CoreHaptics.protocol.md), [`CHHapticPlayable`](../objc/CHHapticPlayable_CoreHaptics.protocol.md), [`CHHapticServerInterface`](../objc/CHHapticServerInterface_CoreHaptics.protocol.md), [`CHMetrics`](../objc/CHMetrics_CoreHaptics.md), [`EventToDictionaryConverter`](../objc/EventToDictionaryConverter_CoreHaptics.md), [`HapticCommandConverter`](../objc/HapticCommandConverter_CoreHaptics.md), [`HapticDictionaryReader`](../objc/HapticDictionaryReader_CoreHaptics.md), [`HapticDictionaryWriter`](../objc/HapticDictionaryWriter_CoreHaptics.md), [`HapticServerConfig`](../objc/HapticServerConfig_CoreHaptics.md), [`NSObject`](../objc/NSObject_CoreHaptics.protocol.md), [`NSXPCListenerDelegate`](../objc/NSXPCListenerDelegate_CoreHaptics.protocol.md), [`PatternPlayer`](../objc/PatternPlayer_CoreHaptics.md), [`PatternPlayerBase`](../objc/PatternPlayerBase_CoreHaptics.md), [`PatternPlayerDetails`](../objc/PatternPlayerDetails_CoreHaptics.protocol.md), [`PlaybackAction`](../objc/PlaybackAction_CoreHaptics.md)

### Classes

`AVHapticClient`, `AVHapticParameterCurveValue`, `AVHapticPlayer`, `AVHapticPlayerChannel`, `AVHapticSequence`, `AVHapticSequenceEntry`, `AdvancedPatternPlayer`, `CHDefaultHapticDeviceCapability`, `CHEmbeddedAudioResourceInfo`, `CHHapticDynamicParameter`, `CHHapticEngine`, `CHHapticEvent`, `CHHapticEventParameter`, `CHHapticParameterAttributesImpl`, `CHHapticParameterCurve`, `CHHapticParameterCurveControlPoint`, `CHHapticPattern`, `CHMetrics`, `EventToDictionaryConverter`, `HapticCommandConverter`, `HapticDictionaryReader`, `HapticDictionaryWriter`, `HapticServerConfig`, `PatternPlayer`, `PatternPlayerBase`, `PlaybackAction`

### Protocols

`CHHapticAdvancedPatternPlayer`, `CHHapticAdvancedPatternPlayerExtended`, `CHHapticClientInterface`, `CHHapticDeviceCapability`, `CHHapticParameterAttributes`, `CHHapticPatternPlayer`, `CHHapticPatternPlayerExtended`, `CHHapticPlayable`, `CHHapticServerInterface`, `NSObject`, `NSXPCListenerDelegate`, `PatternPlayerDetails`

### Properties

```
@property (TB) loopEnabled;
@property (Td) loopEnd;
@property (Tf) playbackRate;
@property (TB) isMuted;
@property (T@?,C) completionHandler;
@property (Tf) volume;
@property (TB,R) supportsHaptics;
@property (TB,R) supportsAudio;
@property (Tf,R) minValue;
@property (Tf,R) maxValue;
@property (Tf,R) defaultValue;
@property (TB) isMuted;
@property (T@"NSArray",R) events;
@property (T@"NSArray",R) parameters;
@property (T@"NSArray",R) parameterCurves;
@property (T@"NSString",R) patternID;
@property (Td,R) duration;
@property (T@"NSString",R) locality;
@property (T@"NSString",R) priority;
@property (T@"NSString",R) hapticPowerUsage;
@property (T@"NSString",R) audioPowerUsage;
@property (T@"NSString",R) usageCategory;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,R) patternDuration;
@property (TB,V_connected) connected;
@property (TQ,R,V_clientID) clientID;
@property (T@"NSArray",R,V_channelKeys) channelKeys;
@property (TB,R,V_prewarmed) prewarmed;
@property (TB,R) running;
@property (Ti,R) state;
@property (Ti,V_serverProcessID) serverProcessID;
@property (Td,R) hapticLatency;
@property (T@?,C,V_asyncStopCallback) asyncStopCallback;
@property (T@?,C,V_completionCallback) completionCallback;
@property (T@?,C,V_connectionCallback) connectionCallback;
@property (TB,R,V_disconnecting) disconnecting;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,V_time) time;
@property (Tf,V_value) value;
@property (T@"AVHapticClient",R,V_client) client;
@property (TB,R,V_resourcesAllocated) resourcesAllocated;
@property (T@?,C,V_stopRunningHandler) stopRunningHandler;
@property (TQ,N,V_behavior) behavior;
@property (T@"NSArray",R,N) channels;
@property (Td,R) currentMediaTime;
@property (Td,R) hapticLatency;
@property (T@?,C) connectionErrorHandler;
@property (TQ,V_chanID) chanID;
@property (T@"AVHapticClient",W,V_client) client;
@property (TQ) eventBehavior;
@property (TB,R) invalidated;
@property (T@"AVHapticPlayer",W,V_player) player;
@property (TQ,V_seqID) seqID;
@property (Td,V_duration) duration;
@property (Td,V_lastStartTime) lastStartTime;
@property (TQ,V_activeChannel) activeChannel;
@property (TQ) eventBehavior;
@property (TB) loopingEnabled;
@property (TB,V_isMuted) isMuted;
@property (Tf) playbackRate;
@property (TQ,R,V_channelCount) channelCount;
@property (T@?,C) completionHandler;
@property (TB,R) invalidated;
@property (T@?,C,V_handler) handler;
@property (TB,V_running) running;
@property (TB,V_detached) detached;
@property (Td) seekOffset;
@property (TB,R) running;
@property (TB,R) paused;
@property (Tf) volume;
@property (TB) loopEnabled;
@property (Td) loopEnd;
@property (Tf) playbackRate;
@property (TB) isMuted;
@property (T@?,C) completionHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) maximumNumberOfHapticChannels;
@property (TQ,R) maximumNumberOfAudioChannels;
@property (TB,R) supportsHaptics;
@property (TB,R) supportsAudio;
@property (T@"NSURL",R,V_url) url;
@property (T@"NSDictionary",R,V_options) options;
@property (T@"NSString",R,V_param) parameterID;
@property (Tf,V_value) value;
@property (Td,V_time) relativeTime;
@property (T@"AVHapticPlayer",R) player;
@property (TB) running;
@property (T@"CHMetrics",R) metrics;
@property (TB,N) activateAudioSessionOnStart;
@property (T@"AVHapticPlayer",&,V_player) player;
@property (T@"HapticServerConfig",&,V_serverConfig) writableServerConfig;
@property (T@"AVAudioSession",R,V_avAudioSession) avAudioSession;
@property (TI,R,V_audioSessionID) audioSessionID;
@property (TB,R,V_sessionIsShared) sessionIsShared;
@property (T@?,C,V_clientFinishedHandler) clientFinishedHandler;
@property (T@"NSObject<OS_dispatch_source>",&,V_timer) timer;
@property (TQ,V_currentPlayerBehavior) currentPlayerBehavior;
@property (TB,R) needsAudioPowerBudget;
@property (T@"HapticServerConfig",R) serverConfig;
@property (TB,N) muteHapticsWhileRecordingAudio;
@property (TB,N) followAudioRoute;
@property (TB,N) highPriority;
@property (T@"NSArray",R) availableLocalities;
@property (T@"NSString",R) locality;
@property (T@"NSString",R,V_priority) priority;
@property (T@"NSString",R,V_hapticPowerUsage) hapticPowerUsage;
@property (T@"NSString",R,V_audioPowerUsage) audioPowerUsage;
@property (T@"NSString",R,V_usageCategory) usageCategory;
@property (Td) autoShutdownTimeout;
@property (Td,R) currentTime;
@property (T@?,C,V_stoppedHandler) stoppedHandler;
@property (T@?,C,V_resetHandler) resetHandler;
@property (TB,N) playsHapticsOnly;
@property (TB,N) playsAudioOnly;
@property (TB,N) isMutedForAudio;
@property (TB,N) isMutedForHaptics;
@property (TB,N,GisAutoShutdownEnabled) autoShutdownEnabled;
@property (T@"CASpatialAudioExperience",C,V_intendedSpatialExperience) intendedSpatialExperience;
@property (TQ,R) audioResID;
@property (Td,R) fullDuration;
@property (T@"NSString",R,V_type) type;
@property (T@"NSArray",R,V_eventParams) eventParameters;
@property (Td,V_time) relativeTime;
@property (Td,V_duration) duration;
@property (T@"NSArray",R) events;
@property (T@"NSArray",R) parameters;
@property (T@"NSArray",R) parameterCurves;
@property (T@"NSString",R) patternID;
@property (T@"NSString",R) locality;
@property (T@"NSString",R) priority;
@property (T@"NSString",R) hapticPowerUsage;
@property (T@"NSString",R) audioPowerUsage;
@property (T@"NSString",R) usageCategory;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,V_param) parameterID;
@property (Tf,V_value) value;
@property (Tf,R,V_minValue) minValue;
@property (Tf,R,V_maxValue) maxValue;
@property (Tf,R,V_defaultValue) defaultValue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,V_param) parameterID;
@property (Td,V_time) relativeTime;
@property (T@"NSArray",R) controlPoints;
@property (Td,V_time) relativeTime;
@property (Tf,V_value) value;
@property (Tf,R) version;
@property (T@"NSDictionary",R,N,V_configurationDictionary) configurationDictionary;
@property (Td,R,N) duration;
@property (T@"NSArray",R) events;
@property (T@"NSArray",R) parameters;
@property (T@"NSArray",R) parameterCurves;
@property (T@"NSString",R) patternID;
@property (T@"NSString",R) locality;
@property (T@"NSString",R) priority;
@property (T@"NSString",R) hapticPowerUsage;
@property (T@"NSString",R) audioPowerUsage;
@property (T@"NSString",R) usageCategory;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"HapticServerConfig",R,V_serverConfig) serverConfig;
@property (TB,R,V_usingInternalHaptics) usingInternalHaptics;
@property (TB,R,V_supportsAudioPlayback) supportsAudioPlayback;
@property (TB,R,V_supportsHapticPlayback) supportsHapticPlayback;
@property (TB,R,V_supportsAdvancedPatternPlayers) supportsAdvancedPatternPlayers;
@property (Tf,R,V_hapticContinuousTimeLimit) hapticContinuousTimeLimit;
@property (T@"NSString",R,V_currentLocality) currentLocality;
@property (Tf,R,V_defaultHapticTransientEventSharpness) defaultHapticTransientEventSharpness;
@property (Tf,R,V_defaultHapticContinuousEventSharpness) defaultHapticContinuousEventSharpness;
@property (Tf,R,V_defaultHapticTransientEventIntensity) defaultHapticTransientEventIntensity;
@property (Tf,R,V_defaultHapticContinuousEventIntensity) defaultHapticContinuousEventIntensity;
@property (T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{?=^Q}},R,V_hapticTransientIDs) hapticTransientIDs;
@property (T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{?=^Q}},R,V_hapticContinuousSustainedIDs) hapticContinuousSustainedIDs;
@property (T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{?=^Q}},R,V_hapticContinuousNonsustainedIDs) hapticContinuousNonsustainedIDs;
@property (T@"NSDictionary",R,V_builtInAudioEventIDs) builtInAudioEventIDs;
@property (TB) isMuted;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"CHHapticEngine",W,V_engine) engine;
@property (T@"NSString",R,V_patternID) patternID;
@property (Td,R,V_patternDuration) patternDuration;
@property (Tq,N,Vaction) action;
@property (Tf,N,Vtime) time;
```

## Strings (1,341)

```
UseVolumeEnvelope
CHHapticEngine.mm
-[HapticDictionaryReader parseParam:]
com.apple.coreaudio
-[CHHapticEngine playPatternFromURL:error:]
hcln
HapticMiniTap4
-[CHMetrics stopReporter]
-[CHHapticEngine createPlayerWithPattern:error:]
-[AVHapticPlayerChannel clearEvents:error:]
com.apple.CoreHaptics
com.apple.corehaptics
readAndAllocateRawBuffer
IntensityBin1
DecayTime
-[CHHapticEngine stopWithCompletionHandler:]
kAudioQueueErr_CannotStart
UIStatesFeedbackGeneratorSwipeActionConfirmOut
HighestPriority
-[AVHapticSequence initWithData:player:error:]_block_invoke
RequestedLocality
HapticMicroTap8
HapticMiniTap9
-[CHHapticEngine(EngineUsageCategory) setupEngineWithCategory:session:needsAudioPowerBudget:error:]
isAdvanced
-[AVHapticClient prepareHapticSequence:error:]
-[CHHapticEngine beginIdleTimer]_block_invoke_2
AVAudioSessionMediaServicesWereResetNotification
AP
ShakeToUndo
UIClickFeedbackGeneratorDown
NanoFindMyNearby
AudioPanControl
-[CHHapticEngine doStopEngineAndWait:]
verifyAudioFile
FullTap3
AudioClick
BypassAudioSession
-[CHHapticEngine doStopWithCompletionHandler:]_block_invoke
plist
-[AVHapticSequence initWithData:player:error:]
Event parameter has invalid or missing parameter value
%p
-[CHMetrics prepareData:events:]
-[AVHapticPlayer finishWithCompletionHandler:]
decrementAllocatedBytes
Carrier
-[AVHapticClient doScheduleParamCurveWithMemoryReserve:atTime:channel:memoryReserve:paramCurve:error:]
UISelectionFeedbackGeneratorStrong
-[CHHapticEngine reconfigureAudioSession]
-[CHHapticEngine unregisterAudioResource:error:]
-[HapticCommandConverter eventForAudioEventType:time:eventParams:duration:]
basic_string
-[AVHapticClient loadAndPrepareHapticSequenceFromData:reply:]_block_invoke_2
NameDropConnectedSecondaryDevice
CameraShutterTouchDown
KeyboardDeletion
[self.client sendEvents:events withImmediateParameters:immediateParameters atTime:time channel:self.chanID outToken:nil error:outError]
SPI
com.apple.audio.virtualaudio
KeypadEvent
-[CHHapticEngine stopAndWait]_block_invoke
-[CHMetrics getLoopsForAdvancedPlayer:endTime:]
%c%d%c
-[AVHapticClient getSyncDelegateForMethod:errorHandler:]_block_invoke
UIClickPresentationFeedbackGeneratorPresentationPreview
/Library/Caches/com.apple.xbs/5A437E4E-E2C7-407A-AFFA-30EFD690A69B/TemporaryDirectory.EsNIKG/Sources/CoreHaptics/Source/AVHapticPlayer.mm
HapticMicroTap2
HapticAttackTime
iOSKeyboard
-[AVHapticClient handleServerConnectionInterruption]
UIStatesFeedbackGeneratorHapticTouchCommit
-[CHHapticEngine createAdvancedPlayerWithPattern:error:]
-[CHHapticEngine hasPublicAudioResourceID:]
hmet
CAException
HapticDictionaryWriter.mm
FullTap9
EngineOff
UIClickPresentationFeedbackGeneratorPresentationDragged
-[CHHapticEngine doPlayPattern:error:]
-[AVHapticSequence setParameter:value:channel:atTime:error:]
-[AdvancedPatternPlayer setCompletionHandler:]_block_invoke
HapticMicroTap6
HapticTransposition
i
AudioPitchControl
-[CHHapticEngine(CHHapticEngineInternal) releaseChannel:]
RequestedPriority
RequestedUsageCategory
_sequence != nil
-[CHMetrics sendDetailedMetricsForPlayerID:endTime:]
Failed to set up audio session whose session ID is 0
-[CHHapticEngine notifyWhenPlayersFinished:]_block_invoke
AudioSineTransient
Cannot export AudioCustom events
time
MiniTap4
kAudioHardwareUnknownPropertyError
Locality
-[AVHapticPlayer doInitWithOptions:error:]_block_invoke
HapticMicroTap4
HapticMiniTap8
-[HapticDictionaryReader parseEvent:withBaseURL:]
CoreHapticsMissingEventTypeException
SupportsIrisCapture
-[AVHapticClient loadAndPrepareHapticSequenceFromData:reply:]
UIFluidSliderFeedbackGeneratorMinEdge
_seqID != kInvalidSequenceID
HapticReleaseTime
kAudioHardwareBadStreamError
DeviceSupportsStereoAudioRecording
HapticReleaseTimeControl
-[CHHapticEngine finishInit:]
-[CHHapticEngine notifyWhenPlayersFinished:]_block_invoke_2
AVAudioSessionCategorySystemSoundsAndHaptics
-[AVHapticSequence stopAtTime:error:]
-[PatternPlayer dealloc]
-[AdvancedPatternPlayer doSetMute:]
HapticFullTap2
Time
UIFluidSliderFeedbackGeneratorTick
audio_decoders_out_of_process
AudioSessionID
SystemSound
HapticContinuousDefaultIntensity
HapticSine
HapticMicroTap9
-[AVHapticClient createCustomAudioEvent:format:frames:options:reply:]
UIDragFeedbackGeneratorTargetUpdated
-[CHHapticEngine stopAndWait]
XPC_ProcessTaskToken
%s: %s
-[AdvancedPatternPlayer initWithPattern:engine:privileged:error:]
-[AdvancedPatternPlayer pauseAtTime:error:]
MiniTap7
CHHapticErrorCodeMemoryError
-[AVHapticClient sequenceFinished:error:]
AssistiveTouch3DTouchActionDown
-[CHHapticEngine removePublicAudioResourceID:]
MicrophoneCount
-[AVHapticClient startRunning:]
ButtonEvent
ClientProcessTaskToken
-[CHHapticEngine(CHHapticEngineInternal) doReferenceAudioResourceByID:]
-[AVHapticSequence seekToTime:error:]
UsingInternalHaptics
Unknown event param type
FullTap4
KeyboardInputText
KeyboardOther
SliderDecremented
-[CHHapticEngine doStartEngineAndWait:]
[self.client clearEventsFromTime:fromTime channel:self.chanID]
HapticDecayTime
IntensityBin3
EnableTelephonyMonitor
-[AVHapticClient finish:]_block_invoke
-[CHHapticEngine cancelIdleTimer]
-[AVHapticPlayer doInitWithOptions:error:]
HapticTransientDefaultSharpness
Invalid audio resource
EnableEANCTelephonyMonitor
%lf
UIButtonFeedbackGeneratorDefaultEnded
ToggledOff
-[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:error:]
HapticTransientEventIDs
MicroTap4
MiniTap3
HapticFullnessSelect
/System/Library/Frameworks/AVFoundation.framework/AVFoundation
-[AVHapticSequence initWithEvents:player:error:]
v24@?0@\"NSDictionary\"8@\"NSError\"16
HapticMicroTap3
with constant
EngineOn
kAudioHardwareIllegalOperationError
-[AVHapticClient createCustomAudioEvent:format:frames:options:reply:]_block_invoke_2
found
-[AVHapticSequence resetAtTime:error:]
Missing event type
NanoFindMyRanging
+[CHHapticPattern patternForKey:error:]
-[AVHapticPlayer createCustomAudioEvent:format:frames:options:reply:]
HapticServerConfig.mm
com.apple.private.allow-background-haptics
HapticContinuousSustainedEventIDs
-[AdvancedPatternPlayer seekToOffset:error:]
HapticSineTransient
HapticMicroTap7
KBDown
-[CHMetrics logMetric:value:]
hapticpower_verbose
playback
HostApplicationDisplayID
-[AVHapticClient finish:]
UIStatesFeedbackGeneratorHapticTouchPreview
json
self.client.clientID != kInvalidClientID
-[HapticDictionaryReader parseParamCurveControlPoints:]
SharpnessSlot%lu
kAudioHardwareNotRunningError
UIImpactFeedbackGeneratorLight
-[CHHapticEngine handleMediaServerRecovery:]_block_invoke
CHHapticEngineUsageCategory.mm
edgeCase
VibratorCapability
-[AVHapticClient prewarm:]_block_invoke_2
CoreAudioServices
HapticSharpness
-[CHHapticEngine playPatternFromData:error:]
AVAudioSessionMediaServicesWereLostNotification
EnableVADTelephonyMonitor
com.apple.coreaudio.LoadDecodersInProcess
-[AVHapticPlayerChannel sendEvents:withImmediateParameters:atTime:error:]
-[AVHapticPlayer addChannel:]
-[AVHapticPlayer startRunningWithCompletionHandler:]
-[AVHapticSequence prepareToPlayAndReturnError:]
+[EventToDictionaryConverter convertEvents:]
UIFeedback
UIButtonFeedbackGeneratorProminentEnded
UISelectionFeedbackGeneratorLight
AVAudioFormat
-[AdvancedPatternPlayer dealloc]
ignore_custom_audio_limit
-[AVHapticClient stopRunning]_block_invoke
-[AVHapticClient doSendEvents:withImmediateParameters:atTime:channel:sorted:outToken:error:]
UINotificationFeedbackGeneratorWarning
v40@?0@\"NSMutableArray\"8@\"NSMutableArray\"16@\"NSMutableArray\"24@\"NSError\"32
-[CHHapticEngine initWithAudioSession:error:]
SystemSoundHapticsParser
q
-[AVHapticClient releaseCustomAudioEvent:reply:]
SwipeEvent
-[CHHapticEngine doStartWithCompletionHandler:]_block_invoke
-[CHHapticEngine initWithAudioSession:sessionIsShared:options:error:]
resource->verifyAudioFile(false)
-[AVHapticPlayer removeChannel:error:]
MonarchLowEndHardware
-[AVHapticPlayer loadAndPrepareHapticSequenceFromEvents:reply:]
-[AVHapticPlayer prewarmWithCompletionHandler:]
-[AdvancedPatternPlayer sendParameters:atTime:error:]
HapticSineMid
MiniTap2
-[AVHapticClient stopRunning:]
q24@?0@\"AVHapticPlayerParameterCurveControlPoint\"8@\"AVHapticPlayerParameterCurveControlPoint\"16
-[CHHapticEngine stopWithCompletionHandler:]_block_invoke
-[CHHapticEngine(CHHapticEngineInternal) notifyPlayerStarted:atTime:]_block_invoke_2
AudioReleaseTime
Illegal or missing event duration
Unknown privileged event type
EnableHALTelephonyMonitor
Retarget
HighPriority
HapticMiniTap2
HapticFullTap5
Invalid or missing audio resource
AID
-[AVHapticClient loadHapticEvent:reply:]
CameraControlFocusLock
CHHapticEngineDispatchQueue
-[CHHapticEngine createAdvancedPlayerWithRingtoneData:error:]
Value
-[HapticDictionaryReader scanForEmbeddedResources:]_block_invoke
-[AVHapticClient scheduleParameterCurve:curve:atTime:channel:error:]
-[AVHapticClient setupConnectionWithOptions:error:]
-[AVHapticClient requestAssignedChannels:error:]
UIImpactFeedbackGeneratorSoft
ahap
-[CHHapticEngine createAdvancedPlayerWithVibePatternDictionary:error:]
HapticSineLow
HapticSineLowMid
Param
Illegal event duration
DeviceSupportsHaptics
AVHapticClient.mm
UINotificationFeedbackGeneratorError
-[CHHapticEngine initWithAudioSessionID:options:error:]
AudioDecayTime
CoreHapticInvalidEventDurationException
Wrist
AudioAttackTimeControl
-[AVHapticPlayerChannel scheduleParameterCurve:curve:atTime:error:]
-[AVHapticPlayer loadAndPrepareHapticSequenceFromData:reply:]
-[CHMetrics getMetricsForPlayer:]
-[CHHapticEngine doStartWithCompletionHandler:]
-[AVHapticPlayerChannel setEventBehavior:]
initPatternPlayer
kAudioDevicePermissionsError
-[AVHapticClient allocateResources:]_block_invoke
NameDropConnectedPrimaryDevice
UIImpactFeedbackGeneratorMedium
EventParameters
AudioCustom
HapticSharpnessControl
-[AVHapticClient referenceCustomAudioEvent:reply:]_block_invoke_2
-[CHHapticEngine(EngineUsageCategory) setupUnsharedAudioSession:isConstantVolume:needsAudioPowerBudget:error:]
ParameterTime
BuiltInAudioEventIDs
HapticMiniTap6
continuousData
-[AVHapticClient setupConnectionWithOptions:error:]_block_invoke_2
KeyboardInputSeparator
HapticContinuousNonsustainedEventIDs
%d
Event
-[AVHapticClient loadAndPrepareHapticSequenceFromEvents:reply:]_block_invoke_2
UIButtonFeedbackGeneratorDefaultStarted
AVHapticPlayer.mm
[self.client resetChannel:self.chanID atTime:time]
-[AVHapticPlayer dealloc]
Pattern
-[AVHapticClient allocateResources:]
details
Cannot mix Fullness with unprivileged Sharpness parameter
-[CHMetrics getLoopsForPlayer:endTime:]
-[AVHapticClient hapticLatency]_block_invoke
-[AVHapticPlayer startRunningWithCompletionHandler:]_block_invoke
-[AVHapticSequence cancelAndReturnError:]
AudioVolume
InternalBuild
-[AVHapticClient stopPrewarm]
-[AVHapticPlayer referenceCustomAudioEvent:reply:]
-[CHMetrics startReporter]
UIImpactFeedbackGeneratorRigid
SliderLimitMax
-[AVHapticPlayer enableSequenceLooping:enable:error:]
-[AdvancedPatternPlayer activateChannelByIndex:atTime:error:]
HapticFullTap8
kAudioHardwareBadPropertySizeError
dev
-[AVHapticClient clientCompletedWithError:]_block_invoke
AVAudioSessionModeHapticsConstantVolume
-[HapticServerConfig initWithHapticPlayer:withOptions:error:]_block_invoke
HapticMicroTap5
Invalid dynamic parameter for curve
-[AVHapticPlayer copyCustomAudioEvent:options:reply:]
-[AVHapticPlayer setSequencePlaybackRate:rate:error:]
-[AVHapticSequence dealloc]
CoreHapticsInvalidEventDurationException
-[CHHapticEngine createPrivilegedPlayerWithPlayable:error:]
self.client != nil
-[AVHapticPlayer prepareHapticSequence:error:]
CoreHapticInvalidParamException
-[CHHapticEngine startIdleTimerWithHandler:]
-[AVHapticPlayer stopPrewarm]
playbackLastAction
UIClickFeedbackGeneratorUp
UIDragFeedbackGeneratorSnapped
[self.client sendEvents:events withImmediateParameters:nil atTime:time channel:self.chanID outToken:nil error:outError]
-[AVHapticPlayer deallocateRenderResources]
-[HapticCommandConverter eventForTransientHapticAtTime:params:duration:]
-[HapticCommandConverter eventForDynamicParameterEntry:]
Unknown dynamic parameter
Parameter has invalid or missing time or type key
-[HapticDictionaryReader parseParamCurve:]
MedusaPIPCapability
DeviceUnsilenced
HardwareButtonGenericToggle
notice
minutiae
DeviceSupportsTelephonyOverUSB
DeviceSupportsUSBTypeC
UIDragFeedbackGeneratorStarted
NanoFindMyFar
CHHapticErrorCodeServerInitFailedException
-[CHHapticEngine beginIdleTimer]_block_invoke
HapticSineHigh
-[CHHapticEngine(EngineUsageCategory) setupSystemSoundAudioSession:needsAudioPowerBudget:error:]
initPatternPlayer_SPI
-[CHMetrics markAdvancedPlaybackAction:action:time:]
CHHapticErrorCodeInsufficientPower
IsUIBuild
-[AVHapticClient loadHapticEvent:reply:]_block_invoke_2
-[AVHapticClient removeAssignedChannelID:error:]
hpwr
-[PatternPlayer cancelAndReturnError:]
Invalid audio resource path
CoreHapticsBadParameterEntryException
CameraCaptureBurst
CameraShutterLatchUp
CameraSliderDetent
DeviceSilenced
HapticContinuousTimeLimit
-[CHHapticEngine(EngineUsageCategory) updateAudioConfigurations:session:]
EventType
NSXPCConnectionInvalid
-[AVHapticClient handleServerConnectionInterruption]_block_invoke
KeyboardInputCandidate
-[CHHapticEngine getSessionIDFromAVAudioSession:]
-[CHHapticEngine finishInit:]_block_invoke
v16@?0@\"NSError\"8
note
CoreHapticInvalidAudioResourceException
FullTap6
-[AVHapticClient prewarm:]
-[AVHapticClient clientDisconnectingForReason:error:]
CameraShutterUnlatchDown
MagSafeChargeAttach
SupportsAdvancedPatternPlayers
EventTime
initParameterCurve_SPI
-[CHHapticPattern initWithContentsOfURL:error:]
AttackTime
-[CHHapticEngine prewarmWithCompletionHandler:]
AVAudioSession
-[AVHapticSequence setEventBehavior:]
UIImpactFeedbackGeneratorHeavy
self.client.running
v8@?0
B32@?0@\"CHHapticEventParameter\"8Q16^B24
ap
true
HapticTransient
AudioBrightnessControl
+[CHHapticEngine clearResourceMap]
-[CHHapticEngine handleMediaServerDeath:]
Missing or invalid audio resource path
patternID
FullTap2
-[CHMetrics sendPatternLibraryMetrics]
-[CHMetrics preparePlaybackData:events:]
-[AVHapticClient queryServerCapabilities:reply:]_block_invoke
-[CHHapticEngine notifyWhenPlayersFinished:]
-[CHHapticEngine registerAudioResource:options:error:]
-[AdvancedPatternPlayer cancelAndReturnError:]
HapticFullTap4
ParameterCurve has invalid or missing time or type key
FullTap5
CameraShutterGesture
UIEdgeFeedbackGeneratorSliderEdge
AudioReleaseTimeControl
-[AVHapticPlayer releaseCustomAudioEvent:reply:]
AudioSine
HapticPowerUsage
-[CHHapticEngine(CHHapticEngineInternal) getAvailableChannel:]
-[CHHapticEngine(CHHapticEngineInternal) doUnregisterAudioResource:fromPattern:error:]
but sequence was muted
channelIndex < self.channelCount
-[AVHapticSequence activateChannelByIndex:atTime:error:]
un
Description
DeviceSupportsSiriBargeIn
-[AVHapticClient copyCustomAudioEvent:options:reply:]
EmptyAppSwitcher
UINotificationFeedbackGeneratorSuccess
status
pattern-loaded
DeviceSupportsClosedLoopHaptics
-[AVHapticClient setSequenceEventBehavior:behavior:channel:]
-[CHHapticPattern resolveExternalResources:error:]
hcst
HapticTransientDefaultIntensity
EventCount
AudioContinuous
AudioPan
-[AVHapticPlayer setSequenceLoopLength:length:error:]
-[CHDefaultHapticDeviceCapability attributesForDynamicParameter:error:]
Default
AudioAttackTime
-[CHMetrics setReporter]
-[CHHapticEngine doUnregisterAllAudioResources]
-[AVHapticSequence initWithDictionary:player:error:]
-[PatternPlayer processImmediateParameters:]_block_invoke
-[CHMetrics dealloc]
MagSafeWalletDetach
SpeakOnTouchFingerOver
Failed to set up audio session
AudioResourceIndex
/Library/Caches/com.apple.xbs/5A437E4E-E2C7-407A-AFFA-30EFD690A69B/TemporaryDirectory.EsNIKG/Sources/CoreHaptics/Source/CHHapticPatternPlayer.mm
Unknown event parameter type
MiniTap6
kAudioHardwareBadObjectError
u
AssistiveTouch3DTouchActionUp
UIDragFeedbackGeneratorEnded
DragBegan
HapticUtils.h
DeviceSupportsBrook
-[AVHapticClient prepareHapticSequence:error:]_block_invoke_2
-[AVHapticClient getAsyncDelegateForMethod:errorHandler:]_block_invoke
UIStatesFeedbackGeneratorHapticTouchCancel
Configuration
AudioPowerUsage
EventWaveformUseVolumeEnvelope
hapi
CHDeviceCapability.mm
CHHapticLocalityEngineDefault
-[CHHapticEngine setAutoShutdownTimeout:]
-[CHHapticEngine updateEngineBehaviorWithError:]
-[CHHapticEngine doInit:sessionIsShared:options:bypassAudioSession:error:]
-[CHHapticEngine doPlayPattern:error:]_block_invoke
HapticFullTap3
Type
transientData
HasBaseband
v24@?0d8@\"NSError\"16
-[AVHapticClient stopRunning]
v24@?0@\"NSArray\"8@\"NSError\"16
CameraShutterTouchUp
AcousticID
MagSafeAttach
UIFluidSliderFeedbackGeneratorDetent
SliderIncremented
ExclusivePriority
-[CHHapticEngine initAndReturnError:]
-[CHHapticEngine doStartWithCompletionHandler:]_block_invoke_2
-[AVHapticPlayerChannel setParameter:value:atTime:error:]
time >= 0.0
HapticSineMidHigh
-[HapticDictionaryReader parseEventsAndParameters:withBaseURL:reply:]
type
MicroTap2
MicroTap8
-[CHMetrics markPlaybackAction:action:time:]
strongSelf && (strongSelf.player != nil)
error
KBKey
com.apple.haptics.metrics.shared
yes
-[CHHapticEngine stopPrewarm]
-[CHHapticEngine doStopWithCompletionHandler:]
-[CHHapticEngine createAdvancedPlayerWithRingtonePattern:error:]
clientID invalid
SupportsAudioPlayback
spew
-[AVHapticClient clientCompletedWithError:]
-[CHHapticEngine setAutoShutdownEnabled:]_block_invoke
Failed to recreate HapticServerConfig
!
-[AVHapticPlayer queryServerCapabilities:reply:]
MiniTap8
v28@?0@\"NSObject<OS_xpc_object>\"8I16@\"NSError\"20
HapticContinuous
-[CHHapticEngine(CHHapticEngineInternal) notifyPlayerStopped:atTime:]
-[AVHapticPlayer loadAndPrepareHapticSequenceFromVibePattern:reply:]
-[AdvancedPatternPlayer scheduleParameterCurve:atTime:error:]
HapticCommandConverter.mm
-[HapticCommandConverter limitDynamicParameter:value:parameter:]
v32@?0@8@16^B24
v40@?0Q8d16Q24@\"NSError\"32
-[AVHapticClient releaseResources]
MachServiceName
-[AVHapticClient handleServerConnectionInvalidation]
-[HapticCommandConverter eventForContinuousHapticEventType:time:params:duration:]
-[PatternPlayer startAtTime:withImmediateParameters:error:]
RequestedPowerUsage
startHapticEngine
advancedPlayback
v16@?0Q8
Parameter
Failed to connect to server
-[PatternPlayer startAtTime:error:]
/Library/Caches/com.apple.xbs/5A437E4E-E2C7-407A-AFFA-30EFD690A69B/TemporaryDirectory.EsNIKG/Sources/CoreHaptics/Source/CHHapticAdvancedPatternPlayer.mm
-[AdvancedPatternPlayer stopAtTime:error:]
-[HapticCommandConverter limitEventParameter:value:parameter:eventType:]
MicroTap9
ParameterID
ParameterValue
-[CHHapticEngine startWithCompletionHandler:]_block_invoke
HapticVolume
DEV
UISelectionFeedbackGeneratorPageControl
UIStatesFeedbackGeneratorSwipeActionConfirmIn
KeypadModifierEvent
LowPriority
-[AVHapticPlayerChannel sendEvents:atTime:error:]
-[AVHapticPlayer initWithSessionID:error:]
Cannot mix privileged and unprivileged Sharpness parameters
Unsupported event param type
Unknown event type
no
NameDropHintingPrimaryDevice
Version
-[CHHapticEngine createProcessTaskToken]
self.running
OSStatus
-[AdvancedPatternPlayer setVolume:]
pausedDuration
MicroTap6
-[CHMetrics logPatternLibraryMetric:]
-[CHMetrics retainData:forTestingPlayer:]
UISelectionFeedbackGeneratorDefault
ParameterCurveControlPoints
-[HapticDictionaryReader readAndVerifyVersion:error:]
-[HapticDictionaryReader parseEventParams:]
ErrorCode
CHHapticPattern.mm
EventDuration
-[CHHapticEngine setAutoShutdownEnabled:]
/Library/Caches/com.apple.xbs/5A437E4E-E2C7-407A-AFFA-30EFD690A69B/TemporaryDirectory.EsNIKG/Sources/CoreHaptics/Source/CHHapticEngine.mm
-[AVHapticSequence initWithDictionary:player:error:]_block_invoke
vector
-[HapticCommandConverter eventForSPIEventType:time:eventParams:duration:]
DefaultWithConstantVolume
Intensity
-[AVHapticClient setState:]
-[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:error:]_block_invoke
-[AVHapticPlayer queryServerCapabilities:reply:]_block_invoke
self.player.resourcesAllocated
HapticContinuousDefaultSharpness
Duration
playbackDuration
-[AVHapticClient callSequenceFinishedHandlersWithError:]
KeyboardDeletionRapid
NanoFindMyAhead
HapticSharpnessSelect
-[AVHapticSequence pauseAtTime:error:]
-[CHDefaultHapticDeviceCapability attributesForEventParameter:eventType:error:]
AudioTransposition
-[HapticDictionaryWriter eventToDictionary:embeddedResourceInfo:]
HapticDictionaryReader.mm
SharpnessIndex%lu
-[AVHapticClient initWithOptions:error:]
-[CHHapticEngine doStartEngineAndWait:]_block_invoke
-[CHHapticEngine isResourceLoopEnabled:]
-[AVHapticClient setPlayerBehavior:error:]_block_invoke_2
EventWaveformPath
HapticIntensityControl
did not find
-[AVHapticPlayerChannel resetAtTime:error:]
-[AVHapticPlayer stopRunningWithCompletionHandler:]
self.player.client.running
CoreHapticsInvalidAudioResourceException
WirelessChargingCapability
-[AVHapticClient copyCustomAudioEvent:options:reply:]_block_invoke_2
-[AVHapticClient stopPrewarm]_block_invoke
CameraModeDialDetent
-[CHHapticEngine doStopEngineAndWait:]_block_invoke
-[CHHapticEngine(CHHapticEngineInternal) checkEngineStateOnStart:]
[self.client setParameter:type atTime:time value:value channel:self.chanID]
CoreHapticsBadEventEntryException
CHHapticErrorCodeEngineStartTimeout
-[AVHapticClient loadAndPrepareHapticSequenceFromEvents:reply:]
CameraControlHalfPressUp
AudioVolumeControl
-[AVHapticSequence playAtTime:offset:error:]
-[AVHapticSequence resumeAtTime:error:]
-[PatternPlayer stopAtTime:error:]
CHHapticAdvancedPatternPlayer.mm
KeyboardSwitchMode
FullGamut
-[AdvancedPatternPlayer earlyUnduckAudioAtTime:error:]
HapticFullTap7
patternDuration
firstStartTime
MiniTap5
WoT
-[CHMetrics setMetricsTestModeEnabled]
ReleaseType
hapticclient_verbose
AllowBackgroundHaptics
StarkCapability
ToggledOn
-[CHHapticPattern doInitWithDictionary:error:]
UsageCategory
Touch
Sustained
HapticMiniTap7
v16@?0@\"NSNotification\"8
CameraShutterUnlatchUp
DeviceUnlock
UIEdgeFeedbackGeneratorZoomLimit
HapticAttackTimeControl
-[CHHapticEngine doInitWithOptions:error:]
DeviceSupportsAOP
shared
-[AdvancedPatternPlayer resumeAtTime:error:]
-[AdvancedPatternPlayer setCompletionHandler:]
HapticMiniTap3
MicroTap5
EngineState
Completion
SliderLimitMin
-[CHHapticEngine startIdleTimerWithHandler:]_block_invoke
open
HapticFullTap9
-[CHMetrics removePlaybackData:]
false
CameraCaptureNightMode
CameraControlHalfPressDown
-[CHHapticEngine prewarmWithCompletionHandler:]_block_invoke
-[CHHapticEngine addPublicAudioResourceID:withURL:options:]
CHHapticPatternPlayer.mm
-[AdvancedPatternPlayer setCompletionHandler:]_block_invoke_2
-[HapticCommandConverter eventForEventEntry:engine:privileged:]
-[CHMetrics logPowerLogMetric:]
HapticDecayTimeControl
self.player.client.clientID != kInvalidClientID
index < self.channelCount
CameraControlSliderDetent
-[CHHapticEngine(CHHapticEngineInternal) checkEngineRunning:]
DeviceIsMuseCapable
AudioBrightness
self.player != nil
-[CHMetrics isEnabled]
-[AVHapticClient allocateResources:]_block_invoke_2
DefaultWithFullStrength
-[CHHapticEngine handleFinish:]_block_invoke
-[CHHapticEngine updateEngineBehavior]
-[CHHapticEngine startWithCompletionHandler:]
public-loaded
-[AVHapticPlayer allocateRenderResourcesWithCompletionHandler:]
v32@?0@\"NSString\"8@16^B24
following ringer
MicroTap7
kAudioHardwareUnspecifiedError
NameDropHintingSecondaryDevice
NanoFindMyAheadOff
AudioSessionIsShared
hapticapi_verbose
-[HapticCommandConverter CHtoAVParameterCurve:]
FullTap7
+[CHMetrics doHandleErrorCode:description:]
-[AVHapticClient dealloc]
v24@?0Q8@\"NSError\"16
-[AVHapticClient detachHapticSequence:]
-[AVHapticClient setPlayerBehavior:error:]
-[AdvancedPatternPlayer startAtTime:error:]
-[AdvancedPatternPlayer setVolume:atTime:error:]
-[CHMetrics handleFinishedForPlayersAtTime:]
-[AVHapticClient setChannelEventBehavior:channel:]
UISelectionFeedbackGeneratorPicker
HighPower
-[AVHapticPlayer setNumberOfChannels:error:]
-[AVHapticClient loadAndPrepareHapticSequenceFromVibePattern:reply:]_block_invoke_2
hapticclient_state_verbose
incrementAllocatedBytes
warning
info
startHapticEngine_SPI
-[CHMetrics initWithEngine:audioSessionID:sessionIsShared:isSPI:]
MiniTap9
HapticMiniTap5
IntensityBin2
kAudioHardwareUnsupportedOperationError
kAudioDeviceUnsupportedFormatError
-[AVHapticClient disconnect]
CameraShutterLatchDown
CameraZoomDialDetent
CardZoomOutDismiss
CHMetrics.mm
PTQ+ABwag03BwO/CKvIK/A
EnableVPTelephonyMonitor
-[AVHapticClient clientStoppedForReason:error:]
KeyboardDeletionRepeat
HapticIntensity
[self.client scheduleParameterCurve:type curve:parameterCurve atTime:time channel:self.chanID error:outError]
-[AVHapticPlayer stopRunning]
CoreHapticInvalidEventTimeException
Count
MicroTap3
FullTap8
DeviceClassNumber
assistant
UIFluidSliderFeedbackGeneratorMaxEdge
DragEnded
-[AdvancedPatternPlayer finishInit]
initParameterCurve
AppSwitcher
-[AVHapticSequence earlyUnduckAudioAtTime:error:]
-[AdvancedPatternPlayer finishInit]_block_invoke
-[HapticCommandConverter eventForLegacyTransientHapticAtTime:params:duration:]
Event parameter has invalid or missing parameter ID
-[AVHapticClient setSequenceEventBehavior:behavior:channel:]_block_invoke_2
EdgeProtect
-[AVHapticSequence initWithEvents:player:error:]_block_invoke
Looped custom audio event missing duration
CoreHapticsInvalidEventTimeException
KBModifier
%@%@
unordered_map::at: key not found
CameraControlSwipe
Generic
v16@?0q8
SupportsHapticPlayback
Illegal or missing event time
-[AVHapticClient setChannelEventBehavior:channel:]_block_invoke_2
Priority
-[CHHapticEngine createHapticPlayerWithOptions:]
-[CHHapticEngine dealloc]
-[CHHapticEngine initWithAudioSessionID:error:]
Public
CHMetricsDispatchQueue
kAudioHardwareBadDeviceError
-[AVHapticClient releaseCustomAudioEvent:reply:]_block_invoke_2
applyImmediateParameters
LowPower
-[AVHapticPlayer setBehavior:error:]
-[AVHapticSequence setVolume:atTime:error:]
Unknown
-[AVHapticSequence setLoopingEnabled:error:]
AudioResource.mm
hapticmetrics_client_disabled
-[CHMetrics prepareAdvancedPlaybackData:events:]
EventWaveformLoopEnabled
-[CHHapticEngine getDurationForResource:]
_Haptic_Check
HapticFullTap6
UserAssignedDeviceName
m
-[AVHapticClient requestAssignedChannels:error:]_block_invoke_2
q24@?0@\"AVHapticEvent\"8@\"AVHapticEvent\"16
operator()
UIButtonFeedbackGeneratorProminentStarted
-[PatternPlayer scheduleParameterCurve:atTime:error:]
-[PatternPlayer sendParameters:atTime:error:]
Error 
-[HapticServerConfig initWithHapticPlayer:withOptions:error:]
CoreHapticInvalidEventTypeException
-[AVHapticClient referenceCustomAudioEvent:reply:]
NanoFindMyPulse
/Library/Audio/Tunings/%@/Haptics/Library/hapticpatternlibrary.plist
-[PatternPlayer initWithPlayable:engine:privileged:error:]
Illegal time value
kAudioHardwareNotReadyError
ReleaseTime
-[CHHapticEngine handleFinish:]
AVAudioSessionCategoryPlayback
-[AVHapticPlayer initWithOptions:error:]
com.apple.audio.hapticd
AudioPitch
LoopEnabled
-[CHHapticEngine startAndReturnError:]
-[CHHapticEngine doUnregisterAllPublicAudioResources]
-[AVHapticPlayer loadHapticEvent:reply:]
CoreHapticsOperationNotPermittedException
CHHapticErrorCodeServerInitFailed
FullURLPathFromURL
-[CHHapticEngine(CHHapticEngineInternal) notifyPlayerStarted:atTime:]_block_invoke
hapticmetrics_verbose
EventToDictionaryConverter.mm
Client completion queue
ParameterCurve
AudioDecayTimeControl
unshared
AudioLPFilterCutoff
-[AVHapticClient loadAndPrepareHapticSequenceFromVibePattern:reply:]
WheelsOfTime
%25s:%-5d %s: Starting simple player %p at time %.3f
%25s:%-5d %s: updating haptics reporter with audio session reporter id %lld
%25s:%-5d %s: ERROR: Memory write failed
%25s:%-5d %s: auto-shutdown being disabled
%25s:%-5d %s: Calling start completion handler on internal queue
%25s:%-5d %s: ERROR: Lower-level player stop failed: %@
%25s:%-5d %s: Stopping simple player %p at time %.3f
%25s:%-5d %s: flushing all player data for engine %@
%25s:%-5d %s: Setting behavior to not follow audio route
%25s:%-5d %s: Requested not to stop-on-finish
%25s:%-5d %s: sending reset event: clientID: 0x%lx time: %.3f
%25s:%-5d %s: ERROR: Failed to get property for audio resource %@
%25s:%-5d %s: ImmediateParameter for ID %u is not supported
%25s:%-5d %s: We were waiting for a completion callback, so call it now
PatternPlayer_cancelAndReturnError
%25s:%-5d %s: Querying server for capabilities with HapticPowerUsage '%@'
%25s:%-5d %s: ERROR: Cannot export AudioCustom events
%25s:%-5d %s: EventParameter %@ does not support ImmediateParameter modulation. Ignore
%25s:%-5d %s: Starting player %p at time %.3f
%25s:%-5d %s: ERROR: Invalid dynamic parameter ID
%25s:%-5d %s: ERROR: Unknown privileged event type: %@
%25s:%-5d %s: done preparing
%25s:%-5d %s: [xpc] done handling disconnect for client ID 0x%x
%25s:%-5d %s: Adding new AVHapticPlayerChannel %p to end of array with channel ID %u
%25s:%-5d %s: ERROR: Event parameter has invalid or missing parameter value
%25s:%-5d %s: Got error during transaction: %p
%25s:%-5d %s: done releasing
%25s:%-5d %s: %@
%25s:%-5d %s: Client 0x%x detaching sequenceID %u
%25s:%-5d ASSERTION FAILURE [(result != std::end(_publicAudioResources)) != 0 is false]: 
%25s:%-5d %s: sending metrics for engine %@ player %@ - %lu transient, %lu continuous
%25s:%-5d %s: edge case - no case found
%25s:%-5d %s: Calling configureWithOptions:reply on server with dictionary: '%@'
%25s:%-5d %s: Incoming URL not a valid file path
%25s:%-5d %s: External haptic server initialization options do not specify a valid address, aborting
%25s:%-5d %s: Total channels was %u, now %u
HapticEngine_initWithAudioSession
%25s:%-5d %s: clientID: 0x%lx numberOfChannels: %u
%25s:%-5d %s: Querying server for capabilities with '%@' Locality
%25s:%-5d %s: ERROR: Failed to open audio resource %@: %u
%25s:%-5d %s: done copying event
%25s:%-5d %s: ERROR: Unable to stop prewarm: %@
%25s:%-5d %s: done setting behavior
%25s:%-5d %s: Waiting to reconnect
%25s:%-5d %s: Shared audio session cannot be nil
%25s:%-5d %s: Resources already allocated -- just call completion handler
%25s:%-5d %s: ERROR: Failed to set property on audio resource %@
%25s:%-5d %s: AHAP dictionary is corrupt: %@
%25s:%-5d %s: Done with reconnect for engine %p
%25s:%-5d %s: Calling prewarm completion handler
%25s:%-5d %s: clientID: 0x%lx
%25s:%-5d %s: initWithData: reply block for hapticPlayer loadAndPrepareHapticSequenceFromData: replyID: %u, replyChannelCount: %u, replyError: %@
%25s:%-5d %s: stopping reporter for engine %@
%25s:%-5d %s: dealloc of HapticClient exited
%25s:%-5d %s: Directly calling stop completionHandler on internal queue
%25s:%-5d %s: ERROR: audio resource ID %u not registered on this CHHapticEngine
%25s:%-5d %s: logging Error metrics : %@
%25s:%-5d %s: ERROR: Failed setting options / retrieving client ID from server
%25s:%-5d %s: Engine had external passed-in auxiliary session. Caller should reconfigure session
%25s:%-5d %s: Engine %p removing resID %u from public resource list
%25s:%-5d %s: loading and preparing haptic sequence from NSArray: clientID: 0x%lx
%25s:%-5d %s: ERROR: Unknown event type: %@
%25s:%-5d %s: releasing resources
%25s:%-5d %s: Calling server with request for %u channels
%25s:%-5d %s: Creating advanced player from vibe pattern dictionary
%25s:%-5d %s: Failed to set duck level
%25s:%-5d %s: Cannot set audio buffer frame size to %u. Error: %@
%25s:%-5d %s: ERROR: Server timeout
%25s:%-5d %s: Client-supplied stopped handler called on destroyed player - calling captured block %p on global queue
%25s:%-5d %s: initWithOptions entered
%25s:%-5d %s: Starting simple player extended %p at time %.3f
%25s:%-5d %s: Received %u haptic continuous sustained IDs
%25s:%-5d %s: Server returned: supports audio: %d adv players: %d internal: %d cont time limit: %us
%25s:%-5d %s: ERROR: Custom event is missing its audio resource path
%25s:%-5d %s: client side metrics DISABLED (defaults write com.apple.corehaptics hapticmetrics_client_disabled == true)
%25s:%-5d %s: done loading sequence
HapticEngine_prewarmWithCompletionHandler
%25s:%-5d %s: Engine %p %s resID %u
%25s:%-5d %s: Synchronously stopping underlying Haptic Player
%25s:%-5d %s: AutoShutdown on and engine stopped - auto start
%25s:%-5d %s: Returning ID %u for copied resource '%@'
%25s:%-5d %s: player %p, clientID: 0x%lx channel %p (ID %u)
%25s:%-5d %s: Client-side (async) stop callback for client 0x%x, reason %d
%25s:%-5d %s: Underlying player %p not running
%25s:%-5d %s: Cannot set audio buffer frame size to %u. Using default buffer size
%25s:%-5d %s: ERROR: Invalid audio session ID: %u
%25s:%-5d %s: In underlying AVHapticPlayer's completion handler block
AdvancedPatternPlayer_sendParameters
%25s:%-5d %s: ERROR: Parameter curve control point has invalid or missing time
%25s:%-5d %s: done removing channel
%25s:%-5d %s: Pattern version > %.1f - looking for config dictionary
%25s:%-5d %s: Cannot find resource referenced by ID %u. Returning 0.0
%25s:%-5d %s: clientID: 0x%lx: call failed
%25s:%-5d %s: ERROR: Unknown param type: %u
%25s:%-5d %s: ERROR: Illegal duration value: %f
HapticEngine_unregisterAudioResource
%25s:%-5d %s: Returning ID 0 due to error
%25s:%-5d %s: loading haptic event: clientID: 0x%lx
%25s:%-5d %s: set sequence playback rate: entered
%25s:%-5d %s: Failed to set mode %@ on audio session. Continue
%25s:%-5d %s: removing playback data for engine %@ player %@
%25s:%-5d ASSERTION FAILURE [(sharedBufferSize > 0) != 0 is false]: 
%25s:%-5d %s: finishWithCompletionHandler callback returned error: %@
HapticEngine_handleMediaServerRecovery
HapticEngine_registerAudioResource
%25s:%-5d %s: Resource ID %u not previously registered!
%25s:%-5d %s: ERROR: Server query returned error '%@'
%25s:%-5d %s: Associated player is not running - action delayed until sequence start
%25s:%-5d %s: Destroying advanced player %p
%25s:%-5d %s: Adding %llu bytes to our existing %llu
%25s:%-5d %s: In underlying AVHapticPlayer's completion handler block for doStopWithCompletionHandler
%25s:%-5d %s: Using passed-in auxiliary audio session with no UsageCategory
%25s:%-5d %s: Failed to disable audio session notifications
%25s:%-5d %s: Pattern library path: %@
%25s:%-5d %s: Calling engine-reset handler on default queue
%25s:%-5d %s: Received %u haptic transient IDs
%25s:%-5d %s: Setting for System Sound, disabling notifications and NowPlaying for this audio session
%25s:%-5d %s: initializing metrics for engine %@
%25s:%-5d %s: ERROR: unable to release server-side audio resource with ID %u: %@
%25s:%-5d %s: Querying server for capabilities with Priority '%@'
%25s:%-5d %s: Client 0x%x, behavior %u
HapticEngine_stopWithCompletionHandler
HapticEngine_playPatternFromData
%25s:%-5d %s: Player %p client-supplied completion handler called - calling captured block %p on internal queue
%25s:%-5d %s: ERROR: Continuous haptic event has a missing or zero-length duration
%25s:%-5d %s: Client 0x%x finishing
%25s:%-5d %s: Client thinks it is not running.  Did we just get a call to stop?
%25s:%-5d %s: Invalid shutdown timeout (%f) being ignored
%25s:%-5d %s: Client-side call for client 0x%x with disconnect reason %d
HapticEngine_initAndReturnError
%25s:%-5d %s: Starting underlying Haptic Player
%25s:%-5d %s: Attempting to remove %s ID %u
%25s:%-5d %s: ERROR: Player was not running - bailing with error %@ for client 0x%x
%25s:%-5d %s: Allocating resources...
%25s:%-5d %s: set volume on seq: clientID: 0x%lx time: %.3f volume: %.3f
%25s:%-5d %s: Incoming fileURL cannot be nil
%25s:%-5d %s: calculated pattern duration: %@
%25s:%-5d %s: set sequence loop length: entered
%25s:%-5d %s: Error setting player %p audio and haptics volume to %.3f: %@
%25s:%-5d %s: Client 0x%x starting
%25s:%-5d %s: Searching for resource in '%@'
%25s:%-5d %s: Failed to load pattern library: %@
%25s:%-5d %s: Synchronously stopping the underlying player %p
%25s:%-5d %s: Omitting audio session creation for usage category: %@
%25s:%-5d %s: resume seq: clientID: 0x%lx time: %.3f
PatternPlayer_startAtTime
%25s:%-5d %s: %s: %s error %d
%25s:%-5d %s: ERROR: async stop after timeout failed with error %@
%25s:%-5d %s: [xpc] Server connection: %@, PID: %d
%25s:%-5d %s: ERROR: could not find audio resource with ID %u
%25s:%-5d %s: ERROR: Unable to set up client: %@
%25s:%-5d %s: Cannot reconfigure audio session for system sound
%25s:%-5d %s: setting param: clientID: 0x%lx type: %u value: %.2f atTime: %.3f
%25s:%-5d %s: Failed to set category on audio session
%25s:%-5d %s: Failed to set not to be ducked by others
%25s:%-5d %s: ERROR: Missing event type
%25s:%-5d %s: Creating pattern for key '%@'
%25s:%-5d %s: Default behavior is to follow audio route
%25s:%-5d %s: skipping metrics - first start time > end time
%25s:%-5d %s: We were running, so call async stopped callback
%25s:%-5d %s: auto-shutdown being enabled while running - wait for any existing players
HapticEngine_stopPrewarm
AdvancedPatternPlayer_initWithPattern
%25s:%-5d %s: done allocating
%25s:%-5d %s: options: '%@'
%25s:%-5d %s: Cannot find resource referenced by ID %u. Returning FALSE
%25s:%-5d %s: initWithSessionID exited
%25s:%-5d %s: ERROR: Failed to read from audio resource %@: %u
%25s:%-5d %s: Cannot configure audio session %u
%25s:%-5d %s: Engine already running
%25s:%-5d %s: In underlying AVHapticPlayer's completion handler block for doStopEngineAndWait
%25s:%-5d %s: ERROR: Unable to stop running: %@
%25s:%-5d %s: Stopping underlying Haptic Player
%25s:%-5d %s: enable sequence looping: entered
%25s:%-5d %s: starting init with event array
%25s:%-5d %s: Got error from server: %p
%25s:%-5d %s: Client-side sequence finish callback for client 0x%x, seq %u
%25s:%-5d ASSERTION FAILURE [(!in_dispatch_sync) != 0 is false]: 
%25s:%-5d %s: ERROR: ID %@ is not supported by parameter curves
%25s:%-5d %s: ERROR: Event parameter has invalid or missing parameter ID
%25s:%-5d %s: adding test player data for player %@
%25s:%-5d %s: done loading event
%25s:%-5d %s: Finished initializing
%25s:%-5d %s: Setting SS&H category %@ volume, disabling notifications and NowPlaying for this audio session
%25s:%-5d %s: ERROR: Illegal event duration
%25s:%-5d %s: ERROR: Attempt to write FinalEvent failed - bailing by calling completionCallback with error %@ for client 0x%x
%25s:%-5d %s: Exited
%25s:%-5d %s: Waiting for startup...
%25s:%-5d %s: In parameter %@ is not a valid CHHapticDynamicParameter
%25s:%-5d %s: Init exited
%25s:%-5d ASSERTION FAILURE [(result) != 0 is false]: 
%25s:%-5d %s: [xpc] Connecting...
%25s:%-5d %s: Done handling finish
%25s:%-5d %s: synchronously stopping and destroying engine %p
%25s:%-5d ASSERTION FAILURE [(resourceEntries.emplace(copiedResourceID, resource, resource->url(), options, refCountKey) == true) != 0 is false]: 
%25s:%-5d %s: <Top of doStopWithCompletionHandler block>
%25s:%-5d %s: Calling stop completion handler on internal queue
%25s:%-5d %s: Returning channel %p (ID %u)
%25s:%-5d %s: deallocating metrics for engine %@
%25s:%-5d %s: Client 0x%x stopping prewarm
%25s:%-5d %s: Called on engine %p with error %@
%25s:%-5d %s: Directly calling start completionHandler on internal queue
%25s:%-5d %s: ERROR: Illegal power usage: %@
%25s:%-5d %s: Caching player %p offset %.2f for later start/resume
%25s:%-5d %s: Adding embedded audio resource path '%@', options '%@'
%25s:%-5d %s: logging metrics data for HapticContinuous : %@
%25s:%-5d %s: Client 0x%x loading sequence from event array
%25s:%-5d %s: In parameter %@ is not a valid CHHapticEventParameter
%25s:%-5d %s: Resuming player %p at time %.3f
%25s:%-5d %s: loading and preparing haptic pattern: clientID: 0x%lx
%25s:%-5d %s: Cancelling events on simple player %p immediately
%25s:%-5d %s: Memory limit reached on custom audio resources - unregister others to make space
%25s:%-5d %s: sending %lu pattern library metrics
%25s:%-5d %s: Attempting to reconnect engine %p to server
%25s:%-5d %s: Called on engine %p with finishedHandler %p
%25s:%-5d %s: Incoming NSData cannot be nil
%25s:%-5d %s: stop running: clientID: 0x%lx
 enableTelemetry=YES 
%25s:%-5d %s: paused duration: %g = %g - %g
%25s:%-5d %s: No audio session used. Returning 0
%25s:%-5d %s: ERROR: Startup timeout
%25s:%-5d %s: Stopping player %p at time %.3f
%25s:%-5d %s: marking action %ld for engine %@ player %p
%25s:%-5d %s: Done waiting for underlying player stop
%25s:%-5d %s: clientID: 0x%lx seqID: %u behavior: %u
%25s:%-5d %s: Player %p default completion handler called
%25s:%-5d %s: Setting player %p audio and haptics volume to %.3f. Server will clamp volume argument to [0, 1]
%25s:%-5d %s: completionCallback set to %p
%25s:%-5d %s: ERROR: Server failure: %@
%25s:%-5d %s: Removing %llu bytes from our existing %llu
%25s:%-5d %s: ERROR: Resource allocation failure: %@
%25s:%-5d %s: Releasing lock
%25s:%-5d %s: ERROR: pattern contains no playable events
%25s:%-5d %s: Creating advanced player %p
%25s:%-5d %s: Calling server with player behavior %u
%25s:%-5d %s: ERROR: unable to reference server-side audio resource with ID %u: %@
%25s:%-5d %s: loading haptic sequence from NSData: clientID: 0x%lx
%25s:%-5d %s: Querying server for UsageCategory of '%@'
%25s:%-5d %s: ERROR: Unrecognized dynamic parameter: %@
%25s:%-5d %s: Client 0x%x preparing sequenceID: %u
%25s:%-5d %s: [xpc] Entered (due to connection invalidation) for client ID 0x%x
%25s:%-5d %s: starting init with dictionary
%25s:%-5d %s: Cancelling commands for player %p immediately
%25s:%-5d %s: ERROR: Audio resource with ID %u has looping enabled but the event does not specify a duration
%25s:%-5d %s: Got error during transaction: %@
%25s:%-5d %s: Client ID: 0x%lx
%25s:%-5d %s: strongSelf.completionCallback is nil
%25s:%-5d %s: Initial XPC call to server timed out. Invalidating connection to prevent hang
%25s:%-5d %s: Attempt #%d...
%25s:%-5d %s: sessionID: %u, isShared: %u options: '%@'
%25s:%-5d %s: Seeking on player %p to offset %.2f
%25s:%-5d %s: Cannot set audio buffer frame size to %u
%25s:%-5d %s: ERROR: Empty pattern
%25s:%-5d %s: ERROR: Client 0x%x: doScheduleParamCurve failed!
%25s:%-5d %s: Calling completionCallback %p and then setting to nil
%25s:%-5d %s: <Bottom of AV finishWithCompletionHandler block>
%25s:%-5d %s: ERROR: Player start failed: %@
%25s:%-5d %s: Creating privileged player from Playable
%25s:%-5d %s: done releasing event
%25s:%-5d %s: Client 0x%x loading sequence: %p
%25s:%-5d %s: [xpc] Invalidating...
PatternPlayer_initWithPlayable
%25s:%-5d %s: ERROR: Illegal priority: %@
%25s:%-5d %s: Creating engine %p with legacy initializer
%25s:%-5d %s: ERROR: Unable to add an additional player channel
%25s:%-5d %s: Creating haptic pattern from JSON or AHAP...
%25s:%-5d %s: pause seq: clientID: 0x%lx time: %.3f
%25s:%-5d %s: WARNING: Missing or malformed version key - assuming v1.0
%25s:%-5d %s: Client-side (async) finish completion callback for client 0x%x called from server
%25s:%-5d ASSERTION FAILURE [(resourceEntries.emplace(resourceID, resource, resource->url(), options, refCountKey) == true) != 0 is false]: 
%25s:%-5d %s: ERROR: Pattern dictionary is missing '%@' key
%25s:%-5d %s: [xpc] Entered (due to client disconnect) for client ID 0x%x
%25s:%-5d %s: Starting idle timer (on async dispatch)
%25s:%-5d %s: ERROR: Server failed to create custom audio event: %@
%25s:%-5d %s: Engine not configured with a Locality - querying using '%@'
%25s:%-5d %s: AVHapticClient 'strongSelf' is nil
%25s:%-5d %s: ERROR creating identify token with error %d. Resource memory usage will be billed to server
%25s:%-5d %s: prepare to play seq: clientID: 0x%lx
%25s:%-5d %s: request pushed out to pending play request at time %.3f
%25s:%-5d %s: Creating advanced player from ringtone pattern
PatternPlayer_startAtTime_withImmediateParameters
AdvancedPatternPlayer_stopAtTime
%25s:%-5d %s: logging PowerLog metrics for \"%@\"
%25s:%-5d %s: done referencing event
%25s:%-5d %s: ERROR: Sync XPC call for '%@' (client ID 0x%x) failed: %@
%25s:%-5d %s: In player's stopRunningHandler block.  Stopped reason: %d
%25s:%-5d %s: sending event array: clientID: 0x%lx atTime: %.3f
%25s:%-5d %s: Received %u haptic continuous nonsustained IDs
%25s:%-5d %s: Found it at '%@'
%25s:%-5d %s: FATAL ERROR: Unable to reconnect to server
%25s:%-5d %s: Calling engine-stopped handler on internal queue
%25s:%-5d %s:    found it - reference count now %u
%25s:%-5d %s: Waiting for server...
%25s:%-5d ASSERTION FAILURE [(self.paused) != 0 is false]: 
%25s:%-5d %s: WARNING: Parameter curve has no control points, skipping
%25s:%-5d %s: logging metrics for \"%@\"
%25s:%-5d %s: stop seq: clientID: 0x%lx time: %.3f
PatternPlayer_scheduleParameterCurve
%25s:%-5d %s: ERROR: Unknown event parameter type: %@
%25s:%-5d %s: Prewarming the underlying Haptic Player
%25s:%-5d %s: Adding reference to audio resource ID %u from pattern
%25s:%-5d %s: Connection error
%25s:%-5d %s: Wrapping client's completion handler block %p in our block and setting on underlying AVHapticSequence
%25s:%-5d %s: seek seq: clientID: 0x%lx time: NOW
%25s:%-5d %s: ERROR: Unknown event param type: %@
%25s:%-5d %s: Client 0x%x EngineState -> %d
%25s:%-5d %s: Cannot set session %u prefering no ducking. Continue
%25s:%-5d %s: Init calling disconnect on self
%25s:%-5d %s: Creating underlying Haptic Player
%25s:%-5d %s: Waiting for player stop...
%25s:%-5d %s: ERROR: Server failed to copy custom audio event: %@
%25s:%-5d %s: clientID: 0x%lx behavior: %u
%25s:%-5d %s: Async dispatch: preparing to call completionCallback for client 0x%x
%25s:%-5d %s: Creating engine %p with audio session %p
%25s:%-5d %s: initWithSessionID entered
%25s:%-5d %s: dealloc seq %p, clientID: 0x%lx
%25s:%-5d %s: Pausing player %p at time %.3f
 Unhandled case in switch
%25s:%-5d %s: Client 0x%x loading pattern: %p
%25s:%-5d %s: <Top of AV finishWithCompletionHandler block>
%25s:%-5d %s: <Bottom of doStopWithCompletionHandler block>
%25s:%-5d %s: Resource not already registered - creating new entry
PatternPlayer_sendParameters
%25s:%-5d ASSERTION FAILURE [(_sTotalAllocatedBytes >= bytes) != 0 is false]: 
%25s:%-5d %s: releasing resource ID %u from engine dealloc
%25s:%-5d %s: Registering %s audio resource '%@'
%25s:%-5d %s:    found it and decrementing refcount
%25s:%-5d %s: ERROR: Player stop failed: %@
%25s:%-5d %s: ERROR: Caught exception during dictionary parse
%25s:%-5d %s: Starting CHHapticEngine...
%25s:%-5d %s: Adding new ID %u for %s resource '%@'
%25s:%-5d %s: early unduck audio on seq: clientID: 0x%lx time: %.3f
%25s:%-5d %s: start running: clientID: 0x%lx
%25s:%-5d %s: Server returned shared buffer of size %u
%25s:%-5d %s: Creating engine %p with %s audio session %p
%25s:%-5d %s: ERROR: Event is none of haptic/audio event, parameter, or parameter curve. returning
%25s:%-5d %s: Calling engine-stopped handler with reason %d
%25s:%-5d %s: destroying player %p
%25s:%-5d %s: Received %u built-in audio event IDs
%25s:%-5d %s: ERROR: Illegal time value: %f
%25s:%-5d %s: marking advanced action %ld for engine %@ player %@
%25s:%-5d %s: [xpc] done connecting
%25s:%-5d %s: Calling server with request to remove channelID %u
%25s:%-5d %s: finish with comp handler: clientID: 0x%lx
%25s:%-5d %s: creating player %p
%25s:%-5d %s: Warning: engine start timed out but server side may be running, triggering async stop
%25s:%-5d %s: deallocating resources: clientID: 0x%lx
%25s:%-5d %s: activating seqID %u track index: clientID: 0x%lx time: %.3f index: %u muted: %d
%25s:%-5d %s: initWithEvents: reply block for hapticPlayer loadAndPrepareHapticSequenceFromEvents: replyID: %u, replyChannelCount: %u, replyError: %@
%25s:%-5d %s: logging metrics data for HapticTransient : %@
%25s:%-5d %s: WARNING: Skipping Custom Audio event - server does not support audio
%25s:%-5d %s: Cannot start haptic engine: error %@
%25s:%-5d %s: Can't set channel count while player is running
%25s:%-5d %s: ERROR: Unsupported version number: %.1f
%25s:%-5d %s: Client 0x%x, seqID %u, behavior %u
%25s:%-5d %s: Calling completion handlers on any active sequences
%25s:%-5d %s: Engine %p was notified of server death
HapticEngine_initWithOptions
%25s:%-5d %s: Starting Pattern Player...
AdvancedPatternPlayer_initWithVibePatternDictionary
%25s:%-5d %s: Using default usage category
%25s:%-5d %s: initializing with options
%25s:%-5d %s: ERROR: This channel was not registered
%25s:%-5d %s: creating custom audio event: clientID: 0x%lx, frameCount: %lu
%25s:%-5d %s: retrieving metrics for engine %@ player %@
%25s:%-5d %s: Server called client-side prewarm completionCallback
%25s:%-5d %s: clearing events: clientID: 0x%lx fromTime: %.3f
HapticEngine_playPatternFromURL
%25s:%-5d %s: Client 0x%lx asynchronously stopped for reason %d
%25s:%-5d %s: ERROR: Invalid event parameter ID.
%25s:%-5d %s: Called on engine %p
%25s:%-5d %s: Client finishedHandler is nil
HapticEngine_startWithCompletionHandler
%25s:%-5d ASSERTION FAILURE [([self doFindPublicAudioResourceID:resourceID] == std::end(_publicAudioResources)) != 0 is false]: 
%25s:%-5d %s: exited with nil
%25s:%-5d ASSERTION FAILURE [(newChannelCount == oldChannelCount + 1) != 0 is false]: 
%25s:%-5d %s: ERROR: Continuous audio event has a missing or zero-length duration
%25s:%-5d %s: Deallocating HapticClient 0x%x
%25s:%-5d %s: Client 0x%x allocating
%25s:%-5d %s: ERROR: Async XPC call for '%@' (client ID 0x%x) failed: %@
%25s:%-5d %s: Clearing resource map
%25s:%-5d %s: Calling client's finishedHandler on internal queue
%25s:%-5d %s: edge case: unknown case
%25s:%-5d %s: [xpc] done handling crash for client ID 0x%x
%25s:%-5d %s: File type is not supported
%25s:%-5d %s: Creating Pattern Player
%25s:%-5d %s: referencing custom audio event: clientID: 0x%lx
%25s:%-5d %s: ERROR: Unsupported event param type: %@
%25s:%-5d %s: Client 0x%x done with finish
%25s:%-5d %s: Failed to read pattern library data: %@
%25s:%-5d %s: Stopping engine in response to timeout
%25s:%-5d %s: Creating engine %p with internal audio session
%25s:%-5d %s: Engine %p adding resID %u to public resource list
%25s:%-5d %s: Incoming NSData is invalid
%25s:%-5d %s: reset parameters on seq: clientID: 0x%lx time: %.3f 
%25s:%-5d %s: ERROR: Illegal or missing event time
%25s:%-5d %s: Got error from server: %@
%25s:%-5d %s: Notifying caller via completion callback
%25s:%-5d %s: sequence %u already prepared for clientID: 0x%lx - NOOP
%25s:%-5d %s: ERROR: Cannot mix Fullness with unprivileged Sharpness parameter
%25s:%-5d %s: done loading pattern
%25s:%-5d %s: player %p notified engine it will be stopping at time %.3f
%25s:%-5d %s: Creating engine %p with shared audio session ID %u
%25s:%-5d %s: play seq %u: clientID: 0x%lx time: %.3f offsetTime: %.3f playback rate: %.1f muted: %d
AdvancedPatternPlayer_initWithRingtoneData
%25s:%-5d %s: ERROR: Parameter curve control point has invalid or missing value
%25s:%-5d %s: Setting player's behavior to 0x%x
HapticEngine_startAndReturnError
PatternPlayer_stopAtTime
%25s:%-5d %s: Advanced player %p: Sending %smute params
%25s:%-5d %s: unable to set reporter for engine %@: error %d
%25s:%-5d %s: preparing playback data for engine %@ player %@
%25s:%-5d %s: [xpc] Entered (due to connection interruption) for client ID 0x%x
%25s:%-5d %s: Haptic pattern with key '%@' not found
%25s:%-5d %s: ERROR: Custom event's audio resource path cannot be resolved
%25s:%-5d %s: ERROR: Cannot mix privileged and unprivileged Sharpness parameters
%25s:%-5d %s: skipping metrics - no playback actions recorded
%25s:%-5d %s: Client 0x%x stopping
%25s:%-5d %s: Channel not found on player
%25s:%-5d %s: Failed to disable audio session now-playing policy
%25s:%-5d %s: Setting up shared memory on client
%25s:%-5d %s: cancel seq: clientID: 0x%lx
%25s:%-5d %s: Client 0x%x starting prewarm
%25s:%-5d %s: soloing sequence ID: %u track %u %s
%25s:%-5d %s: Clearing public audio resources
%25s:%-5d %s: Creating player from pattern
%25s:%-5d %s: initWithOptions exited
%25s:%-5d %s: Client-supplied completion handler called on destroyed player - calling captured block %p on global queue
%25s:%-5d %s: [xpc] Got error during transaction: %@
%25s:%-5d %s: Setting behavior to not activate audio session (if haptics-only)
%25s:%-5d %s: Illegal event behavior: %u
%25s:%-5d %s: Setting default completion handler on underlying AVHapticSequence
%25s:%-5d %s: [xpc] done disconnecting
%25s:%-5d %s: Server returned count of %u
%25s:%-5d %s: Read pattern library data
%25s:%-5d %s: Cancelling idle timer
%25s:%-5d %s: Creating advanced player from pattern
%25s:%-5d %s: Resource already registered but request uses options - copy existing ID (%u) as new ID
%25s:%-5d %s: prewarm: clientID: 0x%lx
%25s:%-5d %s: ERROR: Unknown event param type: %u
%25s:%-5d %s: edge case: action time out of order %g < %g
%25s:%-5d %s: ERROR: Unable to get server capabilities: %@
%25s:%-5d %s: '%@' path: %@
%25s:%-5d %s: Engine already destroyed - noop
%25s:%-5d %s: Stopping prewarm on the underlying Haptic Player
%25s:%-5d %s: allocating resources: clientID: 0x%lx
%25s:%-5d %s: starting init with data %p, player %p
%25s:%-5d %s: done creating event
%25s:%-5d %s: Creating idle timer for %.3f seconds
%25s:%-5d %s: Engine not running
%25s:%-5d %s: Calling client's engine-stopped handler on internal queue
%25s:%-5d %s:    found it and refcount is at zero - erasing and releasing on server
%25s:%-5d %s: dealloc exited
%25s:%-5d %s: edge case: did not see startAtTime as first call
%25s:%-5d %s: preparing advanced playback data for engine %@ player %@
%25s:%-5d %s: dealloc entered for player %p
%25s:%-5d %s: ERROR: Param is missing a %s
%25s:%-5d %s: logging metrics for pattern library \"%@\"
%25s:%-5d %s: edge case - no loop multiplier, log once
%25s:%-5d %s: ERROR: Unable to get latency: %@
%25s:%-5d %s: Loaded pattern library dict:\n%@
%25s:%-5d %s: Startup complete
%25s:%-5d %s: Creating internal unshared audio session
%25s:%-5d %s: Resource already registered and request uses matching options - referencing existing ID (%u)
%25s:%-5d %s: clientID: 0x%lx channelID: %u behavior: %u
%25s:%-5d %s: copying custom audio event: clientID: 0x%lx, eventID: %u
%25s:%-5d %s: Client was not running - calling completion handler immediately
%25s:%-5d %s: set param on seq: clientID: 0x%lx type: %u value: %.2f channelIndex: %u atTime: %.3f
%25s:%-5d %s: Client requested engine stop-on-finish
%25s:%-5d %s: WARNING: timed out waiting for underlying player to stop
%25s:%-5d %s: Creating advanced player from ringtone data
%25s:%-5d %s: Cannot start without allocating resources
HapticEngine_initWithAudioSessionID
HapticEngine_initWithAudioSessionID_options
%25s:%-5d %s: releasing custom audio event: clientID: 0x%lx
%25s:%-5d %s: stop prewarm: clientID: 0x%lx
AdvancedPatternPlayer_startAtTime
%25s:%-5d %s: test mode ENABLED
%25s:%-5d %s: Creating haptic pattern from plist...
%25s:%-5d %s: ERROR: Parameter curves are not yet supported on CHHapticAdvancedPlayers
%25s:%-5d %s: Client 0x%x loading dictionary: %p
%25s:%-5d %s: done destroying engine %p
%25s:%-5d %s: -- Entry list has '%@' with ID %u
%25s:%-5d %s: player %p, clientID: 0x%lx
%25s:%-5d %s: Resources already deallocated -- noop
%25s:%-5d %s: initWithDictionary: reply block for hapticPlayer loadAndPrepareHapticSequenceFromVibePattern: replyID: %u, replyError: %@
%25s:%-5d %s: Calling idle timeout handler on internal queue
%25s:%-5d %s: Attempting to remove all remaining public audio resources for this engine
%25s:%-5d %s: Destroying a sequence that is still looping!  Disabling loop.
%25s:%-5d %s: Setting player %p to early unduck audio at time %.3f
%25s:%-5d %s: ERROR: Invalid or missing audio resource with ID %u
%25s:%-5d %s: starting reporter for engine %@
%25s:%-5d %s: ERROR: Unable to access shared memory
%25s:%-5d %s: [xpc] ERROR: Failed retrieving client ID
%25s:%-5d %s: done requesting channels
%25s:%-5d %s: ERROR: Player prewarm failed: %@
%25s:%-5d %s: Cannot set audio session with session flags. Continue
%25s:%-5d %s: Failed to set audio session NeedsPowerBudgeting
%25s:%-5d %s: skipping metrics - no advanced playback actions recorded
%25s:%-5d %s: ERROR: Server connection broke with error '%@'
%25s:%-5d %s: Using passed-in shared audio session
```
