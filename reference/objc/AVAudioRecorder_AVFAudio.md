# `AVAudioRecorder`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAudioSessionParticipant`
- 1 instance variables, 12 properties, 45 instance methods, 0 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (Ti,N) processToTap;
@property (TB,N) instantaneousMetering;
@property (TB,R,GisRecording) recording;
@property (T@"NSURL",R) url;
@property (T@"NSDictionary",R) settings;
@property (T@"AVAudioFormat",R) format;
@property (T@"<AVAudioRecorderDelegate>",W) delegate;
@property (Td,R) currentTime;
@property (Td,R) deviceCurrentTime;
@property (TB,GisMeteringEnabled) meteringEnabled;
@property (T@"NSArray",C,N) channelAssignments;
@property (T@"AVAudioSession",&) audioSession;
```

## Instance methods

```
-[AVAudioRecorder finalize];
-[AVAudioRecorder impl];
-[AVAudioRecorder pause];
-[AVAudioRecorder isRecording];
-[AVAudioRecorder audioSession];
-[AVAudioRecorder init];
-[AVAudioRecorder stop];
-[AVAudioRecorder updateMeters];
-[AVAudioRecorder settings];
-[AVAudioRecorder baseInit];
-[AVAudioRecorder dealloc];
-[AVAudioRecorder currentTime];
-[AVAudioRecorder averagePowerForChannel:];
-[AVAudioRecorder setDelegate:];
-[AVAudioRecorder setMeteringEnabled:];
-[AVAudioRecorder setAudioSession:];
-[AVAudioRecorder delegate];
-[AVAudioRecorder record];
-[AVAudioRecorder peakPowerForChannel:];
-[AVAudioRecorder format];
-[AVAudioRecorder url];
-[AVAudioRecorder channelAssignments];
-[AVAudioRecorder setChannelAssignments:];
-[AVAudioRecorder deviceCurrentTime];
-[AVAudioRecorder handleInterruption:];
-[AVAudioRecorder endInterruption];
-[AVAudioRecorder beginInterruption];
-[AVAudioRecorder endInterruptionWithFlags:];
-[AVAudioRecorder deleteRecording];
-[AVAudioRecorder prepareToRecord];
-[AVAudioRecorder autoreleaseDelegate];
-[AVAudioRecorder finishedRecording:];
-[AVAudioRecorder initWithURL:format:error:];
-[AVAudioRecorder initWithURL:settings:error:];
-[AVAudioRecorder instantaneousMetering];
-[AVAudioRecorder isMeteringEnabled];
-[AVAudioRecorder privCommonCleanup];
-[AVAudioRecorder privRemoveSessionPropertyListeners];
-[AVAudioRecorder privSetDelegate:];
-[AVAudioRecorder processToTap];
-[AVAudioRecorder recordAtTime:];
-[AVAudioRecorder recordAtTime:forDuration:];
-[AVAudioRecorder recordForDuration:];
-[AVAudioRecorder setInstantaneousMetering:];
-[AVAudioRecorder setProcessToTap:];
```
