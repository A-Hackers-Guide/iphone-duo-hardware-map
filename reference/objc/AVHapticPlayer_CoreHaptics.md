# `AVHapticPlayer`

- Image: [`/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`](../userland/System__Library__Frameworks__CoreHaptics.framework__CoreHaptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 8 properties, 55 instance methods, 3 class methods

## Instance variables

```
@"AVHapticClient" _client;
B _resourcesAllocated;
Q _behavior;
@"NSMutableArray" _channelArray;
@? _connectionErrorHandler;
@? _stopRunningHandler;
```

## Properties

```
@property (T@"AVHapticClient",R,V_client) client;
@property (TB,R,V_resourcesAllocated) resourcesAllocated;
@property (T@?,C,V_stopRunningHandler) stopRunningHandler;
@property (TQ,N,V_behavior) behavior;
@property (T@"NSArray",R,N) channels;
@property (Td,R) currentMediaTime;
@property (Td,R) hapticLatency;
@property (T@?,C) connectionErrorHandler;
```

## Class methods

```
+[AVHapticPlayer supportsAudio];
+[AVHapticPlayer isSupported];
+[AVHapticPlayer supportsHaptics];
```

## Instance methods

```
-[AVHapticPlayer stopRunning];
-[AVHapticPlayer expectNotifyAfter:];
-[AVHapticPlayer channels];
-[AVHapticPlayer loadHapticEvent:reply:];
-[AVHapticPlayer prepareHapticSequence:error:];
-[AVHapticPlayer referenceCustomAudioEvent:reply:];
-[AVHapticPlayer clearSequenceEvents:atTime:];
-[AVHapticPlayer enableSequenceLooping:enable:error:];
-[AVHapticPlayer currentMediaTime];
-[AVHapticPlayer doInitWithOptions:error:];
-[AVHapticPlayer releaseCustomAudioEvent:reply:];
-[AVHapticPlayer stopPrewarm];
-[AVHapticPlayer connectionErrorHandler];
-[AVHapticPlayer sendUnduckAudioCommand:atTime:];
-[AVHapticPlayer createCustomAudioEvent:format:frames:options:reply:];
-[AVHapticPlayer resetHapticSequence:atTime:];
-[AVHapticPlayer releaseChannels];
-[AVHapticPlayer detachHapticSequence:];
-[AVHapticPlayer prewarmWithCompletionHandler:];
-[AVHapticPlayer setStopRunningHandler:];
-[AVHapticPlayer setSequenceChannelParam:atTime:channel:param:value:error:];
-[AVHapticPlayer seekHapticSequence:toTime:];
-[AVHapticPlayer stopRunningHandler];
-[AVHapticPlayer copyCustomAudioEvent:options:reply:];
-[AVHapticPlayer removeChannel:error:];
-[AVHapticPlayer getBehavior];
-[AVHapticPlayer initWithSessionID:error:];
-[AVHapticPlayer hapticLatency];
-[AVHapticPlayer dealloc];
-[AVHapticPlayer setNumberOfChannels:error:];
-[AVHapticPlayer setSequencePlaybackRate:rate:error:];
-[AVHapticPlayer initWithOptions:error:];
-[AVHapticPlayer addChannel:];
-[AVHapticPlayer resumeHapticSequence:atTime:];
-[AVHapticPlayer loadAndPrepareHapticSequenceFromData:reply:];
-[AVHapticPlayer setConnectionErrorHandler:];
-[AVHapticPlayer invalidateChannels];
-[AVHapticPlayer setBehavior:];
-[AVHapticPlayer behavior];
-[AVHapticPlayer setBehavior:error:];
-[AVHapticPlayer stopRunningWithCompletionHandler:];
-[AVHapticPlayer createOptionsFromAudioSessionID:shared:bypassAudioSession:];
-[AVHapticPlayer playHapticSequence:atTime:offset:];
-[AVHapticPlayer stopHapticSequence:atTime:];
-[AVHapticPlayer deallocateRenderResources];
-[AVHapticPlayer queryServerCapabilities:reply:];
-[AVHapticPlayer resourcesAllocated];
-[AVHapticPlayer allocateRenderResourcesWithCompletionHandler:];
-[AVHapticPlayer loadAndPrepareHapticSequenceFromVibePattern:reply:];
-[AVHapticPlayer pauseHapticSequence:atTime:];
-[AVHapticPlayer client];
-[AVHapticPlayer loadAndPrepareHapticSequenceFromEvents:reply:];
-[AVHapticPlayer startRunningWithCompletionHandler:];
-[AVHapticPlayer setSequenceLoopLength:length:error:];
-[AVHapticPlayer finishWithCompletionHandler:];
```
