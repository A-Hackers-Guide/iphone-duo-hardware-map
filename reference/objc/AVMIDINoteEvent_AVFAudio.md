# `AVMIDINoteEvent`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMusicEvent`
- 1 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
{MIDINoteMessage="channel"C"note"C"velocity"C"releaseVelocity"C"duration"f} _msg;
```

## Properties

```
@property (T^{MIDINoteMessage=CCCCf},R) message;
@property (TI) channel;
@property (TI) key;
@property (TI) velocity;
@property (Td) duration;
```

## Instance methods

```
-[AVMIDINoteEvent setChannel:];
-[AVMIDINoteEvent channel];
-[AVMIDINoteEvent initWithMessage:];
-[AVMIDINoteEvent message];
-[AVMIDINoteEvent velocity];
-[AVMIDINoteEvent setKey:];
-[AVMIDINoteEvent duration];
-[AVMIDINoteEvent isEqualTo:];
-[AVMIDINoteEvent setDuration:];
-[AVMIDINoteEvent setVelocity:];
-[AVMIDINoteEvent key];
-[AVMIDINoteEvent initWithChannel:key:velocity:duration:];
```
