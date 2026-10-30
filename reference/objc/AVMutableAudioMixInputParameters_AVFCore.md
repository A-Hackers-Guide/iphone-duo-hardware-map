# `AVMutableAudioMixInputParameters`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAudioMixInputParameters`
- 1 instance variables, 3 properties, 15 instance methods, 4 class methods

## Instance variables

```
@"AVMutableAudioMixInputParametersInternal" _mutableInputParameters;
```

## Properties

```
@property (Ti,N) trackID;
@property (T@"NSString",C,N) audioTimePitchAlgorithm;
@property (T^{opaqueMTAudioProcessingTap=},&,N) audioTapProcessor;
```

## Class methods

```
+[AVMutableAudioMixInputParameters audioMixInputParameters];
+[AVMutableAudioMixInputParameters audioMixInputParametersWithAssetTrack:introFadeDuration:fadeOutStart:fadeOutDuration:];
+[AVMutableAudioMixInputParameters audioMixInputParametersWithTrack:];
+[AVMutableAudioMixInputParameters audioMixInputParametersWithTrack:scheduledAudioParameters:];
```

## Instance methods

```
-[AVMutableAudioMixInputParameters addEffect:];
-[AVMutableAudioMixInputParameters trackID];
-[AVMutableAudioMixInputParameters removeAllEffects];
-[AVMutableAudioMixInputParameters audioTimePitchAlgorithm];
-[AVMutableAudioMixInputParameters setAudioTimePitchAlgorithm:];
-[AVMutableAudioMixInputParameters audioTapProcessor];
-[AVMutableAudioMixInputParameters removeEffectParameters:];
-[AVMutableAudioMixInputParameters setAmbienceLevel:atTime:];
-[AVMutableAudioMixInputParameters setAudioTapProcessor:];
-[AVMutableAudioMixInputParameters setDialogLevel:atTime:];
-[AVMutableAudioMixInputParameters setDialogMixBias:atTime:];
-[AVMutableAudioMixInputParameters setTrackID:];
-[AVMutableAudioMixInputParameters setVolume:atTime:];
-[AVMutableAudioMixInputParameters setVolumeRampFromStartVolume:toEndVolume:timeRange:];
-[AVMutableAudioMixInputParameters setVolumeRampFromStartVolume:toEndVolume:timeRange:rampMode:];
```
