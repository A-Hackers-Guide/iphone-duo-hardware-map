# `PFSoundGeneratorPHASE`

- Image: [`/System/Library/PrivateFrameworks/PencilFeedback.framework/PencilFeedback`](../userland/System__Library__PrivateFrameworks__PencilFeedback.framework__PencilFeedback.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PFSoundGeneratorBase`
- 4 instance variables, 4 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _isAudioActive;
@"PHASEEngine" _engine;
@"PHASEDataBundleAsset" _dataBundleAsset;
@"PHASESoundEvent" _soundEvent;
```

## Properties

```
@property (T@"PHASEEngine",&,N,V_engine) engine;
@property (T@"PHASEDataBundleAsset",&,N,V_dataBundleAsset) dataBundleAsset;
@property (T@"PHASESoundEvent",&,N,V_soundEvent) soundEvent;
@property (TB,N,V_isAudioActive) isAudioActive;
```

## Instance methods

```
-[PFSoundGeneratorPHASE setEngine:];
-[PFSoundGeneratorPHASE pause];
-[PFSoundGeneratorPHASE engine];
-[PFSoundGeneratorPHASE stop];
-[PFSoundGeneratorPHASE dealloc];
-[PFSoundGeneratorPHASE isAudioActive];
-[PFSoundGeneratorPHASE resume];
-[PFSoundGeneratorPHASE initializeParameters];
-[PFSoundGeneratorPHASE soundEvent];
-[PFSoundGeneratorPHASE stopSound];
-[PFSoundGeneratorPHASE applyBandwidth:];
-[PFSoundGeneratorPHASE dataBundleAsset];
-[PFSoundGeneratorPHASE debugAudioGraph];
-[PFSoundGeneratorPHASE applyPanH:panV:];
-[PFSoundGeneratorPHASE applyBandpassFrequency:];
-[PFSoundGeneratorPHASE applyCrossoverFrequency:];
-[PFSoundGeneratorPHASE applyHighPassFrequency:];
-[PFSoundGeneratorPHASE applyLowPassFrequency:];
-[PFSoundGeneratorPHASE applyNormalizedGain:];
-[PFSoundGeneratorPHASE didUpdateAllParameters];
-[PFSoundGeneratorPHASE setDataBundleAsset:];
-[PFSoundGeneratorPHASE setIsAudioActive:];
-[PFSoundGeneratorPHASE setSoundEvent:];
-[PFSoundGeneratorPHASE setupAudioEngine];
-[PFSoundGeneratorPHASE startSound];
```
