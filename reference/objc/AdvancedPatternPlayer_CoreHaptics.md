# `AdvancedPatternPlayer`

- Image: [`/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`](../userland/System__Library__Frameworks__CoreHaptics.framework__CoreHaptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PatternPlayerBase`
- Protocols: `CHHapticAdvancedPatternPlayerExtended`
- 6 instance variables, 13 properties, 43 instance methods, 0 class methods

## Instance variables

```
@"AVHapticSequence" _sequence;
d _loopEnd;
i _state;
{optional<double>=""(?="__null_state_"c"__val_"d)"__engaged_"B} _seekOffset;
@? _completionHandler;
f _volume;
```

## Properties

```
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
```

## Instance methods

```
-[AdvancedPatternPlayer resetState];
-[AdvancedPatternPlayer resumeAtTime:error:];
-[AdvancedPatternPlayer setVolume:atTime:error:];
-[AdvancedPatternPlayer isMuted];
-[AdvancedPatternPlayer doSetMute:];
-[AdvancedPatternPlayer sendParameters:atTime:error:];
-[AdvancedPatternPlayer earlyUnduckAudioAtTime:error:];
-[AdvancedPatternPlayer loopEnd];
-[AdvancedPatternPlayer activateChannelByIndex:atTime:error:];
-[AdvancedPatternPlayer clearExternalResources:];
-[AdvancedPatternPlayer setPlaybackRate:];
-[AdvancedPatternPlayer stopAtTime:error:];
-[AdvancedPatternPlayer pauseAtTime:error:];
-[AdvancedPatternPlayer setPaused];
-[AdvancedPatternPlayer playbackRate];
-[AdvancedPatternPlayer patternDuration];
-[AdvancedPatternPlayer startAtTime:error:];
-[AdvancedPatternPlayer cancelAndReturnError:];
-[AdvancedPatternPlayer seekToOffset:error:];
-[AdvancedPatternPlayer seekOffset];
-[AdvancedPatternPlayer setCompletionHandler:];
-[AdvancedPatternPlayer setLoopEnd:];
-[AdvancedPatternPlayer completionHandler];
-[AdvancedPatternPlayer setIsMuted:];
-[AdvancedPatternPlayer volume];
-[AdvancedPatternPlayer doStartFromPausedAtTime:error:];
-[AdvancedPatternPlayer paused];
-[AdvancedPatternPlayer init];
-[AdvancedPatternPlayer dealloc];
-[AdvancedPatternPlayer setVolume:];
-[AdvancedPatternPlayer scheduleParameterCurve:atTime:error:];
-[AdvancedPatternPlayer loopEnabled];
-[AdvancedPatternPlayer setLoopEnabled:];
-[AdvancedPatternPlayer running];
-[AdvancedPatternPlayer initWithPattern:engine:privileged:error:];
-[AdvancedPatternPlayer setRunning];
-[AdvancedPatternPlayer setSeekOffset:];
-[AdvancedPatternPlayer doStartFromStoppedAtTime:error:];
-[AdvancedPatternPlayer doResumeAtTime:error:];
-[AdvancedPatternPlayer clearSeekOffset];
-[AdvancedPatternPlayer initWithRingtoneData:engine:error:];
-[AdvancedPatternPlayer finishInit];
-[AdvancedPatternPlayer initWithVibePatternDictionary:engine:error:];
```
