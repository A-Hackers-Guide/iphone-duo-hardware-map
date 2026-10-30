# `AVHapticClient`

- Image: [`/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`](../userland/System__Library__Frameworks__CoreHaptics.framework__CoreHaptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`, `CHHapticClientInterface`
- 17 instance variables, 16 properties, 85 instance methods, 0 class methods

## Instance variables

```
@"NSXPCConnection" _connection;
^v _commandWriter;
Q _uniqueID;
@? _completionCallback;
@? _connectionCallback;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _mapMutex;
{map<unsigned long, AVHapticSequenceEntry *, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, AVHapticSequenceEntry *>>>="__tree_"{__tree<std::__value_type<unsigned long, AVHapticSequenceEntry *>, std::__map_value_compare<unsigned long, std::pair<const unsigned long, AVHapticSequenceEntry *>, std::less<unsigned long>>, std::allocator<std::pair<const unsigned long, AVHapticSequenceEntry *>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _sequenceEntryMap;
@"NSObject<OS_dispatch_queue>" _completionQueue;
i _state;
B _disconnecting;
{reply_watchdog_factory="mDebugging"B"mDefaultTimeoutMS"i"mTimeoutHandler"{function<void ()>="__f_"{__value_func<void ()>="__buf_"(type="__data"[24C])"__f_"^v}}} _configurationReplyWatchdogFactory;
B _prewarmed;
B _connected;
i _serverProcessID;
Q _clientID;
@"NSArray" _channelKeys;
@? _asyncStopCallback;
```

## Properties

```
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
```

## Instance methods

```
-[AVHapticClient connected];
-[AVHapticClient releaseResources];
-[AVHapticClient stopRunning];
-[AVHapticClient expectNotifyAfter:];
-[AVHapticClient setConnected:];
-[AVHapticClient loadHapticEvent:reply:];
-[AVHapticClient prepareHapticSequence:error:];
-[AVHapticClient referenceCustomAudioEvent:reply:];
-[AVHapticClient clearSequenceEvents:atTime:];
-[AVHapticClient enableSequenceLooping:enable:error:];
-[AVHapticClient releaseCustomAudioEvent:reply:];
-[AVHapticClient stopPrewarm];
-[AVHapticClient sendUnduckAudioCommand:atTime:];
-[AVHapticClient createCustomAudioEvent:format:frames:options:reply:];
-[AVHapticClient resetHapticSequence:atTime:];
-[AVHapticClient clientID];
-[AVHapticClient detachHapticSequence:];
-[AVHapticClient setState:];
-[AVHapticClient seekHapticSequence:toTime:];
-[AVHapticClient getSyncDelegateForMethod:errorHandler:];
-[AVHapticClient sendEvents:withImmediateParameters:atTime:channel:outToken:error:];
-[AVHapticClient copyCustomAudioEvent:options:reply:];
-[AVHapticClient doSendEvents:withImmediateParameters:atTime:channel:sorted:outToken:error:];
-[AVHapticClient allocateResources:];
-[AVHapticClient hapticLatency];
-[AVHapticClient scheduleParameterCurve:curve:atTime:channel:error:];
-[AVHapticClient destroySharedMemory];
-[AVHapticClient doScheduleParamCurveWithMemoryReserve:atTime:channel:memoryReserve:paramCurve:error:];
-[AVHapticClient getAsyncDelegateForMethod:errorHandler:];
-[AVHapticClient dealloc];
-[AVHapticClient setAsyncStopCallback:];
-[AVHapticClient setCompletionCallback:];
-[AVHapticClient setSequencePlaybackRate:rate:error:];
-[AVHapticClient initWithOptions:error:];
-[AVHapticClient handleServerConnectionInvalidation];
-[AVHapticClient finish:];
-[AVHapticClient clearAssignedChannels];
-[AVHapticClient completionCallback];
-[AVHapticClient setupConnectionWithOptions:error:];
-[AVHapticClient asyncStopCallback];
-[AVHapticClient setServerProcessID:];
-[AVHapticClient removeAssignedChannelID:error:];
-[AVHapticClient resumeHapticSequence:atTime:];
-[AVHapticClient serverProcessID];
-[AVHapticClient setConnectionCallback:];
-[AVHapticClient setSequenceChannelParameter:atTime:value:sequenceID:channel:];
-[AVHapticClient loadAndPrepareHapticSequenceFromData:reply:];
-[AVHapticClient setChannelKeys:];
-[AVHapticClient clientStoppedForReason:error:];
-[AVHapticClient sequenceFinished:error:];
-[AVHapticClient disconnect];
-[AVHapticClient setRunStateForSequenceEntryWithID:running:];
-[AVHapticClient setChannelEventBehavior:channel:];
-[AVHapticClient doInit];
-[AVHapticClient running];
-[AVHapticClient prewarm:];
-[AVHapticClient doScheduleParamCurve:atTime:channel:paramCurve:error:];
-[AVHapticClient setSequenceEventBehavior:behavior:channel:];
-[AVHapticClient clearEventsFromTime:channel:];
-[AVHapticClient prewarmed];
-[AVHapticClient stopHapticSequence:atTime:];
-[AVHapticClient requestAssignedChannels:error:];
-[AVHapticClient setParameter:atTime:value:channel:];
-[AVHapticClient queryServerCapabilities:reply:];
-[AVHapticClient handleServerConnectionInterruption];
-[AVHapticClient calculateHapticCommandParamCurveMemorySize:];
-[AVHapticClient setPlayerBehavior:error:];
-[AVHapticClient clientDisconnectingForReason:error:];
-[AVHapticClient stopRunning:];
-[AVHapticClient connectionCallback];
-[AVHapticClient disconnecting];
-[AVHapticClient getSequenceFinishedHandlerForID:];
-[AVHapticClient startHapticSequence:atTime:withOffset:];
-[AVHapticClient callSequenceFinishedHandlersWithError:];
-[AVHapticClient channelKeys];
-[AVHapticClient loadAndPrepareHapticSequenceFromVibePattern:reply:];
-[AVHapticClient pauseHapticSequence:atTime:];
-[AVHapticClient resetChannel:atTime:];
-[AVHapticClient clientCompletedWithError:];
-[AVHapticClient detachSequenceEntryforID:];
-[AVHapticClient setSequenceFinishedHandlerForID:finishedHandler:];
-[AVHapticClient loadAndPrepareHapticSequenceFromEvents:reply:];
-[AVHapticClient state];
-[AVHapticClient setSequenceLoopLength:length:error:];
-[AVHapticClient startRunning:];
```
