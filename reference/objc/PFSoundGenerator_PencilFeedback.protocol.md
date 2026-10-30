# `PFSoundGenerator` (protocol)

- Image: [`/System/Library/PrivateFrameworks/PencilFeedback.framework/PencilFeedback`](../userland/System__Library__PrivateFrameworks__PencilFeedback.framework__PencilFeedback.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 10 properties, 24 instance methods, 0 class methods

## Properties

```
@property (Tq,N) currentVolumeState;
@property (Tf,N) outputVolume;
@property (TI,R,N) channelCount;
@property (Tf,N) strokeVolume;
@property (Tf,N) bandpassFrequency;
@property (Tf,N) bandwidth;
@property (Tf,N) highPassFrequency;
@property (Tf,N) lowPassFrequency;
@property (Tf,R,N) panHorizontal;
@property (Tf,R,N) panVertical;
```

## Instance methods

```
-[PFSoundGenerator channelCount];
-[PFSoundGenerator pause];
-[PFSoundGenerator stop];
-[PFSoundGenerator setBandwidth:];
-[PFSoundGenerator bandwidth];
-[PFSoundGenerator resume];
-[PFSoundGenerator outputVolume];
-[PFSoundGenerator setOutputVolume:];
-[PFSoundGenerator stopSound];
-[PFSoundGenerator debugAudioGraph];
-[PFSoundGenerator bandpassFrequency];
-[PFSoundGenerator currentVolumeState];
-[PFSoundGenerator highPassFrequency];
-[PFSoundGenerator lowPassFrequency];
-[PFSoundGenerator panHorizontal];
-[PFSoundGenerator panVertical];
-[PFSoundGenerator setBandpassFrequency:];
-[PFSoundGenerator setCurrentVolumeState:];
-[PFSoundGenerator setHighPassFrequency:];
-[PFSoundGenerator setLowPassFrequency:];
-[PFSoundGenerator setStrokeVolume:];
-[PFSoundGenerator startSound];
-[PFSoundGenerator strokeVolume];
-[PFSoundGenerator updateWithParameters:];
```
