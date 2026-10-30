# `AVAudioMixSweepFilterEffectParameters`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAudioMixEffect`
- 1 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"AVAudioMixSweepFilterEffectParametersInternal" _sweepFilterAudioEffect;
```

## Properties

```
@property (Ti,R,N) minimumCutOffFrequency;
@property (Ti,R,N) maximumCutOffFrequency;
@property (Tf,R,N) bypassThreshold;
@property (Tf,R,N) sweepValue;
```

## Class methods

```
+[AVAudioMixSweepFilterEffectParameters sweepFilterEffectParametersWithMinimumCutOffFrequency:maximumCutOffFrequency:bypassThreshold:sweepValue:];
```

## Instance methods

```
-[AVAudioMixSweepFilterEffectParameters init];
-[AVAudioMixSweepFilterEffectParameters dealloc];
-[AVAudioMixSweepFilterEffectParameters hash];
-[AVAudioMixSweepFilterEffectParameters isEqual:];
-[AVAudioMixSweepFilterEffectParameters bypassThreshold];
-[AVAudioMixSweepFilterEffectParameters initWithMinimumCutOffFrequency:maximumCutOffFrequency:bypassThreshold:sweepValue:];
-[AVAudioMixSweepFilterEffectParameters maximumCutOffFrequency];
-[AVAudioMixSweepFilterEffectParameters minimumCutOffFrequency];
-[AVAudioMixSweepFilterEffectParameters sweepFilterEffectWithSweepValue:];
-[AVAudioMixSweepFilterEffectParameters sweepValue];
```
