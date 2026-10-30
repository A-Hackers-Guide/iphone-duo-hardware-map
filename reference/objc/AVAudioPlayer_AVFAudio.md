# `AVAudioPlayer`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 19 properties, 64 instance methods, 0 class methods

## Instance variables

```
@ _impl;
@"NSString" _currentDevice;
@"CASpatialAudioExperience" _intendedSpatialExperience;
```

## Properties

```
@property (TB,R,GisPlaying) playing;
@property (TQ,R) numberOfChannels;
@property (Td,R) duration;
@property (T@"NSString",C,V_currentDevice) currentDevice;
@property (T@"<AVAudioPlayerDelegate>",W) delegate;
@property (T@"NSURL",R) url;
@property (T@"NSData",R) data;
@property (Tf) pan;
@property (Tf) volume;
@property (TB) enableRate;
@property (Tf) rate;
@property (Td) currentTime;
@property (Td,R) deviceCurrentTime;
@property (Tq) numberOfLoops;
@property (T@"NSDictionary",R) settings;
@property (T@"AVAudioFormat",R) format;
@property (TB,GisMeteringEnabled) meteringEnabled;
@property (T@"NSArray",C,N) channelAssignments;
@property (T@"CASpatialAudioExperience",C,V_intendedSpatialExperience) intendedSpatialExperience;
```

## Instance methods

```
-[AVAudioPlayer pan];
-[AVAudioPlayer finalize];
-[AVAudioPlayer setCurrentTime:];
-[AVAudioPlayer impl];
-[AVAudioPlayer pause];
-[AVAudioPlayer rate];
-[AVAudioPlayer play];
-[AVAudioPlayer audioSession];
-[AVAudioPlayer setIntendedSpatialExperience:];
-[AVAudioPlayer intendedSpatialExperience];
-[AVAudioPlayer volume];
-[AVAudioPlayer init];
-[AVAudioPlayer stop];
-[AVAudioPlayer updateMeters];
-[AVAudioPlayer settings];
-[AVAudioPlayer data];
-[AVAudioPlayer dealloc];
-[AVAudioPlayer isPlaying];
-[AVAudioPlayer currentTime];
-[AVAudioPlayer averagePowerForChannel:];
-[AVAudioPlayer currentDevice];
-[AVAudioPlayer setVolume:];
-[AVAudioPlayer initWithData:error:];
-[AVAudioPlayer setRate:];
-[AVAudioPlayer duration];
-[AVAudioPlayer initWithContentsOfURL:error:];
-[AVAudioPlayer setDelegate:];
-[AVAudioPlayer setSTSLabel:];
-[AVAudioPlayer setMeteringEnabled:];
-[AVAudioPlayer setAudioSession:];
-[AVAudioPlayer delegate];
-[AVAudioPlayer peakPowerForChannel:];
-[AVAudioPlayer setPan:];
-[AVAudioPlayer setCurrentDevice:];
-[AVAudioPlayer format];
-[AVAudioPlayer url];
-[AVAudioPlayer channelAssignments];
-[AVAudioPlayer numberOfChannels];
-[AVAudioPlayer prepareToPlay];
-[AVAudioPlayer setChannelAssignments:];
-[AVAudioPlayer setNumberOfLoops:];
-[AVAudioPlayer deviceCurrentTime];
-[AVAudioPlayer enableRate];
-[AVAudioPlayer playAtTime:];
-[AVAudioPlayer setEnableRate:];
-[AVAudioPlayer STSLabel];
-[AVAudioPlayer numberOfLoops];
-[AVAudioPlayer handleInterruption:];
-[AVAudioPlayer endInterruption];
-[AVAudioPlayer beginInterruption];
-[AVAudioPlayer endInterruptionWithFlags:];
-[AVAudioPlayer initBase];
-[AVAudioPlayer setMixToUplink:];
-[AVAudioPlayer autoreleaseDelegate];
-[AVAudioPlayer decodeError:];
-[AVAudioPlayer finishedPlaying:];
-[AVAudioPlayer initWithContentsOfURL:fileTypeHint:error:];
-[AVAudioPlayer initWithData:fileTypeHint:error:];
-[AVAudioPlayer isMeteringEnabled];
-[AVAudioPlayer mixToUplink];
-[AVAudioPlayer privRemoveSessionListener];
-[AVAudioPlayer setUseInjectionDevice:];
-[AVAudioPlayer setVolume:fadeDuration:];
-[AVAudioPlayer useInjectionDevice];
```
