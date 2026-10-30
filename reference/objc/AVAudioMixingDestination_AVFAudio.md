# `AVAudioMixingDestination`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAudioMixing`
- 1 instance variables, 6 properties, 26 instance methods, 0 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (T@"AVAudioConnectionPoint",R,N) connectionPoint;
@property (Tf,N) volume;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVAudioMixingDestination pan];
-[AVAudioMixingDestination rate];
-[AVAudioMixingDestination initWithImpl:];
-[AVAudioMixingDestination position];
-[AVAudioMixingDestination volume];
-[AVAudioMixingDestination init];
-[AVAudioMixingDestination dealloc];
-[AVAudioMixingDestination setVolume:];
-[AVAudioMixingDestination setRate:];
-[AVAudioMixingDestination implementation];
-[AVAudioMixingDestination setPosition:];
-[AVAudioMixingDestination setPan:];
-[AVAudioMixingDestination setSourceMode:];
-[AVAudioMixingDestination sourceMode];
-[AVAudioMixingDestination occlusion];
-[AVAudioMixingDestination setObstruction:];
-[AVAudioMixingDestination setReverbBlend:];
-[AVAudioMixingDestination obstruction];
-[AVAudioMixingDestination pointSourceInHeadMode];
-[AVAudioMixingDestination renderingAlgorithm];
-[AVAudioMixingDestination reverbBlend];
-[AVAudioMixingDestination setOcclusion:];
-[AVAudioMixingDestination setPointSourceInHeadMode:];
-[AVAudioMixingDestination setRenderingAlgorithm:];
-[AVAudioMixingDestination connectionPoint];
-[AVAudioMixingDestination destinationForMixer:bus:];
```
