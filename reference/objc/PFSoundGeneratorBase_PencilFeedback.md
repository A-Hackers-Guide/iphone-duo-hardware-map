# `PFSoundGeneratorBase`

- Image: [`/System/Library/PrivateFrameworks/PencilFeedback.framework/PencilFeedback`](../userland/System__Library__PrivateFrameworks__PencilFeedback.framework__PencilFeedback.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PFSoundGenerator`
- 13 instance variables, 17 properties, 47 instance methods, 0 class methods

## Instance variables

```
f _outputVolume;
I _channelCount;
f _strokeVolume;
f _bandpassFrequency;
f _bandwidth;
f _highPassFrequency;
f _lowPassFrequency;
f _panHorizontal;
f _panVertical;
f _gainNormalizationDivisor;
f _crossoverFrequency;
q _currentVolumeState;
@"AVAudioSession" _auxiliarySession;
```

## Properties

```
@property (Tf,N,V_gainNormalizationDivisor) gainNormalizationDivisor;
@property (Tf,N,V_crossoverFrequency) crossoverFrequency;
@property (T@"AVAudioSession",&,N,V_auxiliarySession) auxiliarySession;
@property (Tq,N,V_currentVolumeState) currentVolumeState;
@property (Tf,N,V_outputVolume) outputVolume;
@property (TI,R,N,V_channelCount) channelCount;
@property (Tf,N,V_strokeVolume) strokeVolume;
@property (Tf,N,V_bandpassFrequency) bandpassFrequency;
@property (Tf,N,V_bandwidth) bandwidth;
@property (Tf,N,V_highPassFrequency) highPassFrequency;
@property (Tf,N,V_lowPassFrequency) lowPassFrequency;
@property (Tf,R,N,V_panHorizontal) panHorizontal;
@property (Tf,R,N,V_panVertical) panVertical;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PFSoundGeneratorBase channelCount];
-[PFSoundGeneratorBase pause];
-[PFSoundGeneratorBase init];
-[PFSoundGeneratorBase stop];
-[PFSoundGeneratorBase setBandwidth:];
-[PFSoundGeneratorBase auxiliarySession];
-[PFSoundGeneratorBase bandwidth];
-[PFSoundGeneratorBase resume];
-[PFSoundGeneratorBase outputVolume];
-[PFSoundGeneratorBase setOutputVolume:];
-[PFSoundGeneratorBase setAuxiliarySession:];
-[PFSoundGeneratorBase setupAudioSession];
-[PFSoundGeneratorBase stopSound];
-[PFSoundGeneratorBase applyBandwidth:];
-[PFSoundGeneratorBase debugAudioGraph];
-[PFSoundGeneratorBase updateFinalGain];
-[PFSoundGeneratorBase applyPanH:panV:];
-[PFSoundGeneratorBase applyBandpassFrequency:];
-[PFSoundGeneratorBase applyCrossoverFrequency:];
-[PFSoundGeneratorBase applyHighPassFrequency:];
-[PFSoundGeneratorBase applyLowPassFrequency:];
-[PFSoundGeneratorBase applyNormalizedGain:];
-[PFSoundGeneratorBase bandpassFrequency];
-[PFSoundGeneratorBase crossoverFrequency];
-[PFSoundGeneratorBase currentVolumeState];
-[PFSoundGeneratorBase didUpdateAllParameters];
-[PFSoundGeneratorBase gainNormalizationDivisor];
-[PFSoundGeneratorBase highPassFrequency];
-[PFSoundGeneratorBase lowPassFrequency];
-[PFSoundGeneratorBase panHorizontal];
-[PFSoundGeneratorBase panVertical];
-[PFSoundGeneratorBase reloadCrossoverFrequency];
-[PFSoundGeneratorBase reloadGainNormalizationDivisor];
-[PFSoundGeneratorBase reloadGlobalParameters];
-[PFSoundGeneratorBase setBandpassFrequency:];
-[PFSoundGeneratorBase setCrossoverFrequency:];
-[PFSoundGeneratorBase setCurrentVolumeState:];
-[PFSoundGeneratorBase setGainNormalizationDivisor:];
-[PFSoundGeneratorBase setHighPassFrequency:];
-[PFSoundGeneratorBase setLowPassFrequency:];
-[PFSoundGeneratorBase setPanPositionX:Y:];
-[PFSoundGeneratorBase setStrokeVolume:];
-[PFSoundGeneratorBase setupAudioEngine];
-[PFSoundGeneratorBase startSound];
-[PFSoundGeneratorBase strokeVolume];
-[PFSoundGeneratorBase strokeVolumeDidChange];
-[PFSoundGeneratorBase updateWithParameters:];
```
