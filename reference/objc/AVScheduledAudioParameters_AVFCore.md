# `AVScheduledAudioParameters`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 1 instance variables, 1 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"AVScheduledAudioParametersInternal" _scheduledParametersInternal;
```

## Properties

```
@property (T@"NSMutableDictionary",C,N,G_ramps,S_setRamps:) ramps;
```

## Instance methods

```
-[AVScheduledAudioParameters initWithPropertyList:];
-[AVScheduledAudioParameters mutableCopyWithZone:];
-[AVScheduledAudioParameters propertyList];
-[AVScheduledAudioParameters init];
-[AVScheduledAudioParameters dealloc];
-[AVScheduledAudioParameters hash];
-[AVScheduledAudioParameters description];
-[AVScheduledAudioParameters copyWithZone:];
-[AVScheduledAudioParameters isEqual:];
-[AVScheduledAudioParameters _figAudioCurves];
-[AVScheduledAudioParameters _audioCurveOfClass:];
-[AVScheduledAudioParameters _audioVolumeCurve];
-[AVScheduledAudioParameters _getRampOfClass:forTime:timeRange:];
-[AVScheduledAudioParameters _isScheduledRampClass:];
-[AVScheduledAudioParameters _ramps];
-[AVScheduledAudioParameters _rampsOfClass:];
-[AVScheduledAudioParameters _setRamp:];
-[AVScheduledAudioParameters _setRamps:];
-[AVScheduledAudioParameters _volumeCurveAsString];
-[AVScheduledAudioParameters _volumeCurveKeysForScheduledRampClassNames];
-[AVScheduledAudioParameters getVolumeRampForTime:startVolume:endVolume:timeRange:];
-[AVScheduledAudioParameters getVolumeRampForTime:startVolume:endVolume:timeRange:rampMode:];
```
