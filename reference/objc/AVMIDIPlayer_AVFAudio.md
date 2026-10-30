# `AVMIDIPlayer`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 4 properties, 18 instance methods, 0 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (Td,R,N) duration;
@property (TB,R,N,GisPlaying) playing;
@property (Tf,N) rate;
@property (Td,N) currentPosition;
```

## Instance methods

```
-[AVMIDIPlayer finalize];
-[AVMIDIPlayer rate];
-[AVMIDIPlayer play:];
-[AVMIDIPlayer stop];
-[AVMIDIPlayer dealloc];
-[AVMIDIPlayer isPlaying];
-[AVMIDIPlayer setRate:];
-[AVMIDIPlayer duration];
-[AVMIDIPlayer currentPosition];
-[AVMIDIPlayer prepareToPlay];
-[AVMIDIPlayer initBase];
-[AVMIDIPlayer beatsForHostTime:];
-[AVMIDIPlayer destroyBase];
-[AVMIDIPlayer hostTimeForBeats:];
-[AVMIDIPlayer implGuard];
-[AVMIDIPlayer initWithContentsOfURL:soundBankURL:error:];
-[AVMIDIPlayer initWithData:soundBankURL:error:];
-[AVMIDIPlayer setCurrentPosition:];
```
