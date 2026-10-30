# `CHHapticServerInterface` (protocol)

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 0 properties, 28 instance methods, 0 class methods

## Instance methods

```
-[CHHapticServerInterface stopRunning];
-[CHHapticServerInterface loadHapticEvent:reply:];
-[CHHapticServerInterface referenceCustomAudioEvent:reply:];
-[CHHapticServerInterface allocateClientResources:];
-[CHHapticServerInterface releaseCustomAudioEvent:reply:];
-[CHHapticServerInterface stopPrewarm];
-[CHHapticServerInterface createCustomAudioEvent:format:frames:options:reply:];
-[CHHapticServerInterface releaseChannels];
-[CHHapticServerInterface setChannelEventBehavior:behavior:reply:];
-[CHHapticServerInterface requestChannels:reply:];
-[CHHapticServerInterface removeChannel:reply:];
-[CHHapticServerInterface copyCustomAudioEvent:options:reply:];
-[CHHapticServerInterface loadHapticSequenceFromEvents:reply:];
-[CHHapticServerInterface releaseClientResources];
-[CHHapticServerInterface configureWithOptions:reply:];
-[CHHapticServerInterface loadVibePattern:reply:];
-[CHHapticServerInterface prepareHapticSequence:reply:];
-[CHHapticServerInterface prewarm:];
-[CHHapticServerInterface getHapticLatency:];
-[CHHapticServerInterface debugExpectNotifyOnFinishAfter:reply:];
-[CHHapticServerInterface stopRunning:];
-[CHHapticServerInterface queryCapabilities:reply:];
-[CHHapticServerInterface detachSequence:];
-[CHHapticServerInterface loadHapticSequenceFromData:reply:];
-[CHHapticServerInterface setPlayerBehavior:reply:];
-[CHHapticServerInterface setSequenceEventBehavior:behavior:channelIndex:reply:];
-[CHHapticServerInterface startRunning:];
-[CHHapticServerInterface setIntendedSpatialExperience:reply:];
```
