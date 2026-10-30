# `AVHapticServer`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`
- 19 instance variables, 6 properties, 46 instance methods, 0 class methods

## Instance variables

```
@"NSXPCListener" _listener;
{map<unsigned int, NSMutableArray<AVServerWrapper *> *, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, NSMutableArray<AVServerWrapper *> *>>>="__tree_"{__tree<std::__value_type<unsigned int, NSMutableArray<AVServerWrapper *> *>, std::__map_value_compare<unsigned int, std::pair<const unsigned int, NSMutableArray<AVServerWrapper *> *>, std::less<unsigned int>>, std::allocator<std::pair<const unsigned int, NSMutableArray<AVServerWrapper *> *>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _instanceMap;
{recursive_mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _instanceMutex;
@"NSXPCInterface" _cachedClientInterface;
@"NSXPCInterface" _cachedServerInterface;
^v _manager;
{map<int, std::bitset<255>, std::less<int>, std::allocator<std::pair<const int, std::bitset<255>>>>="__tree_"{__tree<std::__value_type<int, std::bitset<255>>, std::__map_value_compare<int, std::pair<const int, std::bitset<255>>, std::less<int>>, std::allocator<std::pair<const int, std::bitset<255>>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _processIndexMap;
{recursive_mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _processIndexMutex;
Q _initCount;
Q _audioPrewarmCount;
Q _hapticsPrewarmCount;
Q _audioRunningCount;
Q _hapticsRunningCount;
Q _runningChannelIDCount;
Q _SSSClientID;
@"NSError" _savedError;
^{PowerTimer=@@B} _powerTimer;
{shared_ptr<HapticMetrics>="__ptr_"^{HapticMetrics}"__cntrl_"^{__shared_weak_count}} _hapticMetrics;
{shared_ptr<HapticAudioMetrics>="__ptr_"^{HapticAudioMetrics}"__cntrl_"^{__shared_weak_count}} _hapticAudioMetrics;
```

## Properties

```
@property (TQ,R,V_initCount) initCount;
@property (T^v,R,V_manager) manager;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVHapticServer cleanup];
-[AVHapticServer getChannelID];
-[AVHapticServer stopPrewarm];
-[AVHapticServer incrementPrewarmCountForAudio:haptics:entry:];
-[AVHapticServer incrementChannelID];
-[AVHapticServer getPrewarmedClientEntries];
-[AVHapticServer doPrewarm:];
-[AVHapticServer startPrewarm];
-[AVHapticServer listener:shouldAcceptNewConnection:];
-[AVHapticServer doStopRunningForInterrupt:audio:haptics:];
-[AVHapticServer init];
-[AVHapticServer playVibePattern:gain:synchronizer:flags:atTime:completionHandler:];
-[AVHapticServer dealloc];
-[AVHapticServer displayRunningProcessEntriesWithOnTime:];
-[AVHapticServer buildActiveProcessesForPowerLogForAudio:haptics:];
-[AVHapticServer reportRunningCountToPowerLogForAudio:haptics:entry:];
-[AVHapticServer removeProcessEntry:];
-[AVHapticServer manager];
-[AVHapticServer doStopPrewarm:audio:haptics:];
-[AVHapticServer dumpProcessEntries:];
-[AVHapticServer forceStopIdleDaemonClients];
-[AVHapticServer incrementInit:];
-[AVHapticServer getRunningClientEntries];
-[AVHapticServer forceStopIdleBackgroundRunningClients];
-[AVHapticServer forceUnprewarmEligibleClients];
-[AVHapticServer decrementPrewarmCountAndStopAudio:stopHaptics:entry:];
-[AVHapticServer displayPrewarmedProcessEntriesWithPrewarmTime:];
-[AVHapticServer incrementRunningCountForAudio:haptics:entry:];
-[AVHapticServer initCount];
-[AVHapticServer buildClientsStringFromEntries:returningLastEntry:];
-[AVHapticServer clientTypeForEntry:withClientID:];
-[AVHapticServer setupSSSClient];
-[AVHapticServer addProcessEntry:];
-[AVHapticServer loadSynthPreset];
-[AVHapticServer checkRunningCountAndStopSynth];
-[AVHapticServer decrementInit];
-[AVHapticServer removeListener:withAudioSessionID:];
-[AVHapticServer HandleInterruptionForSession:command:dictionary:];
-[AVHapticServer decrementRunningCountAndStopAudio:stopHaptics:entry:];
-[AVHapticServer doStartRunning:completedBlock:];
-[AVHapticServer entryWithID:];
-[AVHapticServer cancelPatternWithOptions:];
-[AVHapticServer doReleaseClientResources:];
-[AVHapticServer doStopRunning:audio:haptics:];
-[AVHapticServer performAction:forClientsMatchingPredicate:];
-[AVHapticServer addListener:forAudioSessionID:];
```
