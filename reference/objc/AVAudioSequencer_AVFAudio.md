# `AVAudioSequencer`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 7 properties, 37 instance methods, 0 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (Td,N) currentPositionInSeconds;
@property (Td,N) currentPositionInBeats;
@property (TB,R,N,GisPlaying) playing;
@property (Tf,N) rate;
@property (T@"NSArray",R,N) tracks;
@property (T@"AVMusicTrack",R,N) tempoTrack;
@property (T@"NSDictionary",R,N) userInfo;
```

## Instance methods

```
-[AVAudioSequencer rate];
-[AVAudioSequencer initWithImpl:];
-[AVAudioSequencer init];
-[AVAudioSequencer stop];
-[AVAudioSequencer userInfo];
-[AVAudioSequencer dealloc];
-[AVAudioSequencer isPlaying];
-[AVAudioSequencer setRate:];
-[AVAudioSequencer removeTrack:];
-[AVAudioSequencer startAndReturnError:];
-[AVAudioSequencer tracks];
-[AVAudioSequencer prepareToPlay];
-[AVAudioSequencer setupTrackArray];
-[AVAudioSequencer beatsForHostTime:error:];
-[AVAudioSequencer beatsForSeconds:];
-[AVAudioSequencer cleanTracks];
-[AVAudioSequencer createAndAppendTrack];
-[AVAudioSequencer currentPositionInBeats];
-[AVAudioSequencer currentPositionInSeconds];
-[AVAudioSequencer dataWithSMPTEResolution:error:];
-[AVAudioSequencer getTempoTrack];
-[AVAudioSequencer hostTimeForBeats:error:];
-[AVAudioSequencer initWithAudioEngine:];
-[AVAudioSequencer loadFromData:options:error:];
-[AVAudioSequencer loadFromURL:options:error:];
-[AVAudioSequencer numberOfTracks];
-[AVAudioSequencer reverseEvents];
-[AVAudioSequencer secondsForBeats:];
-[AVAudioSequencer setCurrentPositionInBeats:];
-[AVAudioSequencer setCurrentPositionInSeconds:];
-[AVAudioSequencer setTempoTrack:];
-[AVAudioSequencer setTrackArray:];
-[AVAudioSequencer setUserCallback:];
-[AVAudioSequencer setupTracks];
-[AVAudioSequencer tempoTrack];
-[AVAudioSequencer trackArray];
-[AVAudioSequencer writeToURL:SMPTEResolution:replaceExisting:error:];
```
