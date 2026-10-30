# `AVHapticServerInstance`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`, `CHHapticServerInterface`
- 17 instance variables, 16 properties, 64 instance methods, 0 class methods

## Instance variables

```
@"AVHapticServer" _server;
@"NSXPCConnection" _connection;
Q _clientID;
{shared_ptr<HapticSession>="__ptr_"^{HapticSession}"__cntrl_"^{__shared_weak_count}} _hapticSession;
{shared_ptr<opaqueCMSession>="__ptr_"^{opaqueCMSession}"__cntrl_"^{__shared_weak_count}} _clientSession;
{AQMESession="mProcessID"i"mSessionID"I"mSourceSessionID"{optional<unsigned int>=""(?="__null_state_"c"__val_"I)"__engaged_"B}"mSubsessionRef"{ObjectRef<const void *>="mCFObject"^v}"mSubsessionID"Q"mDescription"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}"mOneWordID"i"mBundleID"{optional<applesauce::CF::StringRef>=""(?="__null_state_"c"__val_"{StringRef="mObject"{ObjectRef<const __CFString *>="mCFObject"^{__CFString}}})"__engaged_"B}} _aqmeSession;
@"AVServerWrapper" _listenerWrapper;
B _clientSuspended;
B _wasPrewarmedAndSuspended;
B _wasRunningAndSuspended;
B _clientInterrupted;
B _runningInBackground;
B _prewarmIncludesAudio;
B _runIncludesHaptics;
B _runIncludesAudio;
@"NSString" _currentRoute;
B _prewarmIncludesHaptics;
```

## Properties

```
@property (T@"AVHapticServer",R,V_server) server;
@property (TQ,R,V_clientID) clientID;
@property (T{shared_ptr<HapticSession>=^{HapticSession}^{__shared_weak_count}},R,V_hapticSession) hapticSession;
@property (TB,V_clientSuspended) clientSuspended;
@property (TB,V_wasPrewarmedAndSuspended) wasPrewarmedAndSuspended;
@property (TB,V_clientInterrupted) clientInterrupted;
@property (TB,V_wasRunningAndSuspended) wasRunningAndSuspended;
@property (TB,V_runningInBackground) runningInBackground;
@property (TB,V_prewarmIncludesHaptics) prewarmIncludesHaptics;
@property (TB,V_prewarmIncludesAudio) prewarmIncludesAudio;
@property (TB,V_runIncludesHaptics) runIncludesHaptics;
@property (TB,V_runIncludesAudio) runIncludesAudio;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVHapticServerInstance stopRunning];
-[AVHapticServerInstance loadHapticEvent:reply:];
-[AVHapticServerInstance referenceCustomAudioEvent:reply:];
-[AVHapticServerInstance allocateClientResources:];
-[AVHapticServerInstance releaseCustomAudioEvent:reply:];
-[AVHapticServerInstance stopPrewarm];
-[AVHapticServerInstance createCustomAudioEvent:format:frames:options:reply:];
-[AVHapticServerInstance releaseChannels];
-[AVHapticServerInstance setChannelEventBehavior:behavior:reply:];
-[AVHapticServerInstance clientID];
-[AVHapticServerInstance requestChannels:reply:];
-[AVHapticServerInstance handleClientApplicationStateChange:];
-[AVHapticServerInstance server];
-[AVHapticServerInstance removeChannel:reply:];
-[AVHapticServerInstance getSyncDelegateForMethod:errorHandler:];
-[AVHapticServerInstance setWasRunningAndSuspended:];
-[AVHapticServerInstance handleInterruptionForSession:command:dictionary:];
-[AVHapticServerInstance copyCustomAudioEvent:options:reply:];
-[AVHapticServerInstance setClientSuspended:];
-[AVHapticServerInstance handleClientApplicationStateChangeUsingAppState:];
-[AVHapticServerInstance clientInterrupted];
-[AVHapticServerInstance runIncludesHaptics];
-[AVHapticServerInstance runIncludesAudio];
-[AVHapticServerInstance getAsyncDelegateForMethod:errorHandler:];
-[AVHapticServerInstance handleConnectionError];
-[AVHapticServerInstance loadHapticSequenceFromEvents:reply:];
-[AVHapticServerInstance dealloc];
-[AVHapticServerInstance muteClientForRingerSwitch:];
-[AVHapticServerInstance setPrewarmIncludesHaptics:];
-[AVHapticServerInstance releaseClientResources];
-[AVHapticServerInstance fadeClientForSessionInterruption:affectHaptics:fadeTime:fadeLevel:stopAfterFade:];
-[AVHapticServerInstance setWasPrewarmedAndSuspended:];
-[AVHapticServerInstance configureWithOptions:reply:];
-[AVHapticServerInstance notifyClientOnStopWithReason:error:];
-[AVHapticServerInstance loadVibePattern:reply:];
-[AVHapticServerInstance hapticSession];
-[AVHapticServerInstance prepareHapticSequence:reply:];
-[AVHapticServerInstance prewarm:];
-[AVHapticServerInstance getHapticLatency:];
-[AVHapticServerInstance clientSuspended];
-[AVHapticServerInstance setPrewarmIncludesAudio:];
-[AVHapticServerInstance debugExpectNotifyOnFinishAfter:reply:];
-[AVHapticServerInstance wasRunningAndSuspended];
-[AVHapticServerInstance stopRunning:];
-[AVHapticServerInstance queryCapabilities:reply:];
-[AVHapticServerInstance handleClientRouteChange:];
-[AVHapticServerInstance setClientInterrupted:];
-[AVHapticServerInstance prewarmIncludesAudio];
-[AVHapticServerInstance setRunIncludesHaptics:];
-[AVHapticServerInstance initWithServer:id:connection:outError:];
-[AVHapticServerInstance runningInBackground];
-[AVHapticServerInstance setupAudioSessionFromID:isShared:error:];
-[AVHapticServerInstance detachSequence:];
-[AVHapticServerInstance prewarmIncludesHaptics];
-[AVHapticServerInstance setRunIncludesAudio:];
-[AVHapticServerInstance wasPrewarmedAndSuspended];
-[AVHapticServerInstance unmuteClientAfterSessionInterruption:];
-[AVHapticServerInstance loadHapticSequenceFromData:reply:];
-[AVHapticServerInstance setPlayerBehavior:reply:];
-[AVHapticServerInstance handleSynthOutputNotificationDeviceStoppedFromBelow:];
-[AVHapticServerInstance setRunningInBackground:];
-[AVHapticServerInstance setSequenceEventBehavior:behavior:channelIndex:reply:];
-[AVHapticServerInstance removeSessionListeners];
-[AVHapticServerInstance startRunning:];
```
