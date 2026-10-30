# `PFSoundGeneratorAVAE`

- Image: [`/System/Library/PrivateFrameworks/PencilFeedback.framework/PencilFeedback`](../userland/System__Library__PrivateFrameworks__PencilFeedback.framework__PencilFeedback.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PFSoundGeneratorBase`
- 10 instance variables, 10 properties, 38 instance methods, 0 class methods

## Instance variables

```
B _isAudioActive;
@"AVAudioEngine" _engine;
@"AVAudioSourceNode" _noiseSourceNode;
^{NoiseGenerator=} _noiseGenerator;
@"AVAudioUnit" _highPassFilter;
@"AVAudioUnit" _bandPassFilter;
@"AVAudioUnit" _lowPassFilter;
@"AVAudioUnit" _crossoverLowPassFilter;
@"AVAudioFormat" _monoFormat;
@"PFSoundXYPanner" _panner;
```

## Properties

```
@property (T@"AVAudioEngine",&,N,V_engine) engine;
@property (TB,N,V_isAudioActive) isAudioActive;
@property (T@"AVAudioSourceNode",&,N,V_noiseSourceNode) noiseSourceNode;
@property (T^{NoiseGenerator=},N,V_noiseGenerator) noiseGenerator;
@property (T@"AVAudioUnit",&,N,V_highPassFilter) highPassFilter;
@property (T@"AVAudioUnit",&,N,V_bandPassFilter) bandPassFilter;
@property (T@"AVAudioUnit",&,N,V_lowPassFilter) lowPassFilter;
@property (T@"AVAudioUnit",&,N,V_crossoverLowPassFilter) crossoverLowPassFilter;
@property (T@"AVAudioFormat",&,N,V_monoFormat) monoFormat;
@property (T@"PFSoundXYPanner",&,N,V_panner) panner;
```

## Instance methods

```
-[PFSoundGeneratorAVAE setEngine:];
-[PFSoundGeneratorAVAE pause];
-[PFSoundGeneratorAVAE engine];
-[PFSoundGeneratorAVAE stop];
-[PFSoundGeneratorAVAE dealloc];
-[PFSoundGeneratorAVAE isAudioActive];
-[PFSoundGeneratorAVAE resume];
-[PFSoundGeneratorAVAE stopSound];
-[PFSoundGeneratorAVAE applyBandwidth:];
-[PFSoundGeneratorAVAE debugAudioGraph];
-[PFSoundGeneratorAVAE noiseSourceNode];
-[PFSoundGeneratorAVAE applyPanH:panV:];
-[PFSoundGeneratorAVAE applyBandpassFrequency:];
-[PFSoundGeneratorAVAE applyCrossoverFrequency:];
-[PFSoundGeneratorAVAE applyHighPassFrequency:];
-[PFSoundGeneratorAVAE applyLowPassFrequency:];
-[PFSoundGeneratorAVAE applyNormalizedGain:];
-[PFSoundGeneratorAVAE bandPassFilter];
-[PFSoundGeneratorAVAE createAudioUnitWithType:subType:];
-[PFSoundGeneratorAVAE createNoiseSourceNode];
-[PFSoundGeneratorAVAE crossoverLowPassFilter];
-[PFSoundGeneratorAVAE highPassFilter];
-[PFSoundGeneratorAVAE lowPassFilter];
-[PFSoundGeneratorAVAE monoFormat];
-[PFSoundGeneratorAVAE noiseGenerator];
-[PFSoundGeneratorAVAE panner];
-[PFSoundGeneratorAVAE setBandPassFilter:];
-[PFSoundGeneratorAVAE setCrossoverLowPassFilter:];
-[PFSoundGeneratorAVAE setHighPassFilter:];
-[PFSoundGeneratorAVAE setIsAudioActive:];
-[PFSoundGeneratorAVAE setLowPassFilter:];
-[PFSoundGeneratorAVAE setMonoFormat:];
-[PFSoundGeneratorAVAE setNoiseGenerator:];
-[PFSoundGeneratorAVAE setNoiseSourceNode:];
-[PFSoundGeneratorAVAE setPanner:];
-[PFSoundGeneratorAVAE setupAudioEngine];
-[PFSoundGeneratorAVAE startSound];
-[PFSoundGeneratorAVAE strokeVolumeDidChange];
```
