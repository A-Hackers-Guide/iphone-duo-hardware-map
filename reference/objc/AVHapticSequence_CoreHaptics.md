# `AVHapticSequence`

- Image: [`/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`](../userland/System__Library__Frameworks__CoreHaptics.framework__CoreHaptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 12 properties, 42 instance methods, 0 class methods

## Instance variables

```
@"AVHapticPlayer" _player;
Q _seqID;
d _lastStartTime;
Q _eventBehavior;
B _loopIsEnabled;
B _isMuted;
f _loopLength;
f _playbackRate;
d _duration;
Q _channelCount;
Q _activeChannel;
```

## Properties

```
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
```

## Instance methods

```
-[AVHapticSequence setEventBehavior:];
-[AVHapticSequence resumeAtTime:error:];
-[AVHapticSequence setVolume:atTime:error:];
-[AVHapticSequence isMuted];
-[AVHapticSequence channelCount];
-[AVHapticSequence earlyUnduckAudioAtTime:error:];
-[AVHapticSequence activateChannelByIndex:atTime:error:];
-[AVHapticSequence setPlaybackRate:];
-[AVHapticSequence player];
-[AVHapticSequence stopAtTime:error:];
-[AVHapticSequence pauseAtTime:error:];
-[AVHapticSequence playbackRate];
-[AVHapticSequence setLoopingEnabled:];
-[AVHapticSequence cancelAndReturnError:];
-[AVHapticSequence setCompletionHandler:];
-[AVHapticSequence completionHandler];
-[AVHapticSequence setIsMuted:];
-[AVHapticSequence getChannelCount];
-[AVHapticSequence setLoopLength:error:];
-[AVHapticSequence seekToTime:error:];
-[AVHapticSequence invalidated];
-[AVHapticSequence lastStartTime];
-[AVHapticSequence initWithEvents:player:error:];
-[AVHapticSequence init];
-[AVHapticSequence dealloc];
-[AVHapticSequence eventBehavior];
-[AVHapticSequence setLoopingEnabled:error:];
-[AVHapticSequence setSeqID:];
-[AVHapticSequence setPlayer:];
-[AVHapticSequence duration];
-[AVHapticSequence setParameter:value:channel:atTime:error:];
-[AVHapticSequence initWithData:player:error:];
-[AVHapticSequence resetAtTime:error:];
-[AVHapticSequence loopingEnabled];
-[AVHapticSequence initWithDictionary:player:error:];
-[AVHapticSequence seqID];
-[AVHapticSequence setDuration:];
-[AVHapticSequence playAtTime:offset:error:];
-[AVHapticSequence prepareToPlayAndReturnError:];
-[AVHapticSequence activeChannel];
-[AVHapticSequence setLastStartTime:];
-[AVHapticSequence setActiveChannel:];
```
