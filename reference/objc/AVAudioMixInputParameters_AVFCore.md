# `AVAudioMixInputParameters`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 1 instance variables, 3 properties, 48 instance methods, 0 class methods

## Instance variables

```
@"AVAudioMixInputParametersInternal" _inputParameters;
```

## Properties

```
@property (Ti,R,N) trackID;
@property (T@"NSString",R,C,N) audioTimePitchAlgorithm;
@property (T^{opaqueMTAudioProcessingTap=},R,&,N) audioTapProcessor;
```

## Instance methods

```
-[AVAudioMixInputParameters addEffect:];
-[AVAudioMixInputParameters mutableCopyWithZone:];
-[AVAudioMixInputParameters effects];
-[AVAudioMixInputParameters init];
-[AVAudioMixInputParameters trackID];
-[AVAudioMixInputParameters dealloc];
-[AVAudioMixInputParameters audioTimePitchAlgorithm];
-[AVAudioMixInputParameters removeEffect:];
-[AVAudioMixInputParameters hash];
-[AVAudioMixInputParameters description];
-[AVAudioMixInputParameters copyWithZone:];
-[AVAudioMixInputParameters setAudioTimePitchAlgorithm:];
-[AVAudioMixInputParameters isEqual:];
-[AVAudioMixInputParameters _figAudioCurves];
-[AVAudioMixInputParameters _audioVolumeCurve];
-[AVAudioMixInputParameters _figProcessingEffectsScheduledParameters];
-[AVAudioMixInputParameters _scheduledAudioParameters];
-[AVAudioMixInputParameters _setScheduledAudioParameters:];
-[AVAudioMixInputParameters _setVolume:atTime:];
-[AVAudioMixInputParameters _setVolumeRampFromStartVolume:toEndVolume:timeRange:rampMode:];
-[AVAudioMixInputParameters _volumeCurveAsString];
-[AVAudioMixInputParameters audioTapProcessor];
-[AVAudioMixInputParameters checkEffectPrecondition:];
-[AVAudioMixInputParameters checkEffectsPrecondition:];
-[AVAudioMixInputParameters effectParameters];
-[AVAudioMixInputParameters getAmbienceLevelRampForTime:startValue:endValue:timeRange:];
-[AVAudioMixInputParameters getAmbienceLoudnessRampForTime:startValue:endValue:timeRange:];
-[AVAudioMixInputParameters getDialogLevelRampForTime:startValue:endValue:timeRange:];
-[AVAudioMixInputParameters getDialogLoudnessRampForTime:startValue:endValue:timeRange:];
-[AVAudioMixInputParameters getDialogMixBiasRampForTime:startValue:endValue:timeRange:];
-[AVAudioMixInputParameters getRecordingLoudnessRampForTime:startValue:endValue:timeRange:];
-[AVAudioMixInputParameters getRenderingStyleRampForTime:startValue:endValue:timeRange:];
-[AVAudioMixInputParameters getVolumeRampForTime:startVolume:endVolume:timeRange:];
-[AVAudioMixInputParameters getVolumeRampForTime:startVolume:endVolume:timeRange:rampMode:];
-[AVAudioMixInputParameters removeAllEffectParameters];
-[AVAudioMixInputParameters setAmbienceLevel:atTime:];
-[AVAudioMixInputParameters setAmbienceLoudness:atTime:];
-[AVAudioMixInputParameters setAudioTapProcessor:];
-[AVAudioMixInputParameters setDialogLevel:atTime:];
-[AVAudioMixInputParameters setDialogLoudness:atTime:];
-[AVAudioMixInputParameters setDialogMixBias:atTime:];
-[AVAudioMixInputParameters setEffectParameters:];
-[AVAudioMixInputParameters setRecordingLoudness:atTime:];
-[AVAudioMixInputParameters setRenderingStyle:atTime:];
-[AVAudioMixInputParameters setTrackID:];
-[AVAudioMixInputParameters setVolume:atTime:];
-[AVAudioMixInputParameters setVolumeRampFromStartVolume:toEndVolume:timeRange:];
-[AVAudioMixInputParameters setVolumeRampFromStartVolume:toEndVolume:timeRange:rampMode:];
```
