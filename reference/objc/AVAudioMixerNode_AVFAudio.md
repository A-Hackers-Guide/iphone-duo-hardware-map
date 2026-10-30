# `AVAudioMixerNode`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAudioNode`
- Protocols: `AVAudioMixing`
- 0 instance variables, 7 properties, 8 instance methods, 0 class methods

## Properties

```
@property (Tf,N) outputVolume;
@property (TQ,R,N) nextAvailableInputBus;
@property (Tf,D,N) volume;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVAudioMixerNode init];
-[AVAudioMixerNode outputVolume];
-[AVAudioMixerNode setOutputVolume:];
-[AVAudioMixerNode inputConnected:];
-[AVAudioMixerNode didAttachToEngine:];
-[AVAudioMixerNode nextAvailableInputBus];
-[AVAudioMixerNode setInputPan:bus:];
-[AVAudioMixerNode setInputVolume:bus:];
```
