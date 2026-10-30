# `CHHapticEngine`

- Image: [`/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`](../userland/System__Library__Frameworks__CoreHaptics.framework__CoreHaptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 24 instance variables, 33 properties, 134 instance methods, 9 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@"AVAudioSession" _avAudioSession;
I _audioSessionID;
I _processTaskToken;
{dict="fObj"{object="fObj"@"NSObject<OS_xpc_object>"}} _processTaskTokenDict;
B _sessionIsShared;
{map<unsigned long, std::pair<NSURL *, NSDictionary *>, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, std::pair<NSURL *, NSDictionary *>>>>="__tree_"{__tree<std::__value_type<unsigned long, std::pair<NSURL *, NSDictionary *>>, std::__map_value_compare<unsigned long, std::pair<const unsigned long, std::pair<NSURL *, NSDictionary *>>, std::less<unsigned long>>, std::allocator<std::pair<const unsigned long, std::pair<NSURL *, NSDictionary *>>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _publicAudioResources;
@"AVHapticPlayer" _player;
@"NSObject<OS_dispatch_source>" _timer;
@? _stoppedHandler;
@? _resetHandler;
B _autoShutdownEnabled;
@? _clientFinishedHandler;
B _running;
Q _currentPlayerBehavior;
@"HapticServerConfig" _serverConfig;
@"NSString" _priority;
@"NSString" _hapticPowerUsage;
@"NSString" _audioPowerUsage;
@"NSString" _usageCategory;
d _runTimeout;
@"CHMetrics" _metrics;
@"NSDictionary" _storedOptions;
@"CASpatialAudioExperience" _intendedSpatialExperience;
```

## Properties

```
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
```

## Class methods

```
+[CHHapticEngine GetMetricsSelectedErrorsMap];
+[CHHapticEngine initialize];
+[CHHapticEngine resourceIsRegistered:];
+[CHHapticEngine GetMediaServicesWereLostNotification];
+[CHHapticEngine capabilitiesForHardware];
+[CHHapticEngine dispatchOnGlobal:];
+[CHHapticEngine clearResourceMap];
+[CHHapticEngine supportsHapticServer];
+[CHHapticEngine supports1stPartyHaptics];
```

## Instance methods

```
-[CHHapticEngine audioPowerUsage];
-[CHHapticEngine setPlaysAudioOnly:];
-[CHHapticEngine doInitWithOptions:error:];
-[CHHapticEngine priority];
-[CHHapticEngine stopPrewarm];
-[CHHapticEngine createAdvancedPlayerWithPattern:error:];
-[CHHapticEngine muteHapticsWhileRecordingAudio];
-[CHHapticEngine player];
-[CHHapticEngine clientFinishedHandler];
-[CHHapticEngine getUsageCategory:];
-[CHHapticEngine followAudioRoute];
-[CHHapticEngine prewarmWithCompletionHandler:];
-[CHHapticEngine doReferenceAudioResourceByID:];
-[CHHapticEngine idForPublicAudioResourceURL:withOptions:];
-[CHHapticEngine setClientFinishedHandler:];
-[CHHapticEngine setHighPriority:];
-[CHHapticEngine handleFinish:];
-[CHHapticEngine audioSessionID];
-[CHHapticEngine setWritableServerConfig:];
-[CHHapticEngine createHapticPlayerWithOptions:];
-[CHHapticEngine needsAudioPowerBudget];
-[CHHapticEngine setResetHandler:];
-[CHHapticEngine setCurrentPlayerBehavior:];
-[CHHapticEngine setupEngineWithCategory:session:needsAudioPowerBudget:error:];
-[CHHapticEngine setIntendedSpatialExperience:];
-[CHHapticEngine setTimer:];
-[CHHapticEngine dispatchSyncOnLocal:];
-[CHHapticEngine intendedSpatialExperience];
-[CHHapticEngine highPriority];
-[CHHapticEngine doInit:sessionIsShared:options:bypassAudioSession:error:];
-[CHHapticEngine setAutoShutdownTimeout:];
-[CHHapticEngine stopAndWait];
-[CHHapticEngine setupSystemSoundAudioSession:needsAudioPowerBudget:error:];
-[CHHapticEngine finishInit:];
-[CHHapticEngine getAvailableChannel:];
-[CHHapticEngine setStoppedHandler:];
-[CHHapticEngine resourceIsRegistered:];
-[CHHapticEngine updateEngineBehaviorWithError:];
-[CHHapticEngine initWithAudioSession:sessionIsShared:error:];
-[CHHapticEngine init];
-[CHHapticEngine serverConfig];
-[CHHapticEngine startIdleTimerWithHandler:];
-[CHHapticEngine doStopEngineAndWait:];
-[CHHapticEngine timer];
-[CHHapticEngine activateAudioSessionOnStart];
-[CHHapticEngine setupUnsharedAudioSession:isConstantVolume:needsAudioPowerBudget:error:];
-[CHHapticEngine initWithAudioSessionID:options:error:];
-[CHHapticEngine connectAudioSession:];
-[CHHapticEngine notifyPlayerStarted:atTime:];
-[CHHapticEngine handleConnectionError];
-[CHHapticEngine initAndReturnError:];
-[CHHapticEngine dealloc];
-[CHHapticEngine doUnregisterAllPublicAudioResources];
-[CHHapticEngine playsAudioOnly];
-[CHHapticEngine unregisterAudioResource:error:];
-[CHHapticEngine resetHandler];
-[CHHapticEngine currentTime];
-[CHHapticEngine stopWithCompletionHandler:];
-[CHHapticEngine cancelIdleTimer];
-[CHHapticEngine initWithOptions:error:];
-[CHHapticEngine reconfigureAudioSession];
-[CHHapticEngine setFollowAudioRoute:];
-[CHHapticEngine playPatternFromURL:error:];
-[CHHapticEngine removePublicAudioResourceID:];
-[CHHapticEngine updateAudioConfigurations:session:];
-[CHHapticEngine isResourceLoopEnabled:];
-[CHHapticEngine disconnectAudioSession:];
-[CHHapticEngine toggleBehavior:set:];
-[CHHapticEngine doRegisterAudioResource:options:fromPattern:error:];
-[CHHapticEngine deallocateProcessTaskToken];
-[CHHapticEngine setPlayer:];
-[CHHapticEngine setRunning:];
-[CHHapticEngine avAudioSession];
-[CHHapticEngine startAndReturnError:];
-[CHHapticEngine hapticPowerUsage];
-[CHHapticEngine getSessionIDFromAVAudioSession:];
-[CHHapticEngine isMutedForHaptics];
-[CHHapticEngine running];
-[CHHapticEngine stoppedHandler];
-[CHHapticEngine currentPlayerBehavior];
-[CHHapticEngine setMuteHapticsWhileRecordingAudio:];
-[CHHapticEngine doFindPublicAudioResourceID:];
-[CHHapticEngine setMetricsTestModeEnabled];
-[CHHapticEngine initWithAudioSessionID:error:];
-[CHHapticEngine createOptionsFromAudioSessionID:shared:bypassAudioSession:];
-[CHHapticEngine handleMediaServerDeath:];
-[CHHapticEngine isMutedForAudio];
-[CHHapticEngine initWithAudioSession:sessionIsShared:options:error:];
-[CHHapticEngine setPlaysHapticsOnly:];
-[CHHapticEngine registerAudioResource:options:error:];
-[CHHapticEngine releaseChannel:];
-[CHHapticEngine getMetricsForPlayer:];
-[CHHapticEngine isAutoShutdownEnabled];
-[CHHapticEngine notifyWhenPlayersFinished:];
-[CHHapticEngine getDurationForResource:];
-[CHHapticEngine locality];
-[CHHapticEngine autoShutdownTimeout];
-[CHHapticEngine sessionIsShared];
-[CHHapticEngine availableLocalities];
-[CHHapticEngine doStartEngineAndWait:];
-[CHHapticEngine notifyPlayerStopped:atTime:];
-[CHHapticEngine checkEngineStateOnStart:];
-[CHHapticEngine createPrivilegedPlayerWithPlayable:error:];
-[CHHapticEngine playPatternFromData:error:];
-[CHHapticEngine doUnregisterAllAudioResources];
-[CHHapticEngine createPlayerWithPattern:error:];
-[CHHapticEngine initWithAudioSession:error:];
-[CHHapticEngine isBehaviorSet:];
-[CHHapticEngine createAdvancedPlayerWithRingtonePattern:error:];
-[CHHapticEngine doPlayPattern:error:];
-[CHHapticEngine setIsMutedForHaptics:];
-[CHHapticEngine hasPublicAudioResourceID:];
-[CHHapticEngine setAutoShutdownEnabled:];
-[CHHapticEngine updateEngineBehavior];
-[CHHapticEngine setActivateAudioSessionOnStart:];
-[CHHapticEngine metrics];
-[CHHapticEngine beginIdleTimer];
-[CHHapticEngine addPublicAudioResourceID:withURL:options:];
-[CHHapticEngine createAdvancedPlayerWithRingtoneData:error:];
-[CHHapticEngine usageCategory];
-[CHHapticEngine doStopWithCompletionHandler:];
-[CHHapticEngine startWithCompletionHandler:];
-[CHHapticEngine createAdvancedPlayerWithVibePatternDictionary:error:];
-[CHHapticEngine handleMediaServerRecovery:];
-[CHHapticEngine doUnregisterAudioResource:fromPattern:error:];
-[CHHapticEngine dispatchOnLocal:];
-[CHHapticEngine doStartWithCompletionHandler:];
-[CHHapticEngine writableServerConfig];
-[CHHapticEngine createProcessTaskToken];
-[CHHapticEngine playsHapticsOnly];
-[CHHapticEngine getReporterIDFromAVAudioSession:];
-[CHHapticEngine setIsMutedForAudio:];
-[CHHapticEngine checkEngineRunning:];
-[CHHapticEngine storeOptions:];
```
