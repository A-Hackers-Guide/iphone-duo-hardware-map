# `AVScheduledVolumeRamp`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVScheduledFloatValueRamp`
- 1 instance variables, 3 properties, 9 instance methods, 2 class methods

## Instance variables

```
q _rampMode;
```

## Properties

```
@property (Tf,R) startVolume;
@property (Tf,R) endVolume;
@property (Tq,R) rampMode;
```

## Class methods

```
+[AVScheduledVolumeRamp _defaultAdditionalFigRepresentationObjects];
+[AVScheduledVolumeRamp volumeRampWithStartVolume:endVolume:timeRange:rampMode:];
```

## Instance methods

```
-[AVScheduledVolumeRamp initWithPropertyList:];
-[AVScheduledVolumeRamp propertyList];
-[AVScheduledVolumeRamp _additionalFigRepresentationObjects];
-[AVScheduledVolumeRamp _makeRampWithTruncatedTimeRange:endValue:];
-[AVScheduledVolumeRamp _parameterRampMode];
-[AVScheduledVolumeRamp endVolume];
-[AVScheduledVolumeRamp initWithStartVolume:endVolume:timeRange:rampMode:];
-[AVScheduledVolumeRamp rampMode];
-[AVScheduledVolumeRamp startVolume];
```
