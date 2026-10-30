# `CBGammaContrastPreservationPolicy`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBChromaticCorrectionPolicy`, `CBLuxRampPolicy`
- 1 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"CBGammaContrastPreservationParams" _params;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tf,R) rampUpDuration;
@property (Tf,R) rampDownDuration;
```

## Instance methods

```
-[CBGammaContrastPreservationPolicy dealloc];
-[CBGammaContrastPreservationPolicy initWithParams:];
-[CBGammaContrastPreservationPolicy name];
-[CBGammaContrastPreservationPolicy rampUpDuration];
-[CBGammaContrastPreservationPolicy rampIdentifier];
-[CBGammaContrastPreservationPolicy cappedRampStartLux:];
-[CBGammaContrastPreservationPolicy cappedRampTargetLux:];
-[CBGammaContrastPreservationPolicy isEnabledPropertyKey];
-[CBGammaContrastPreservationPolicy luxIsInActiveRange:];
-[CBGammaContrastPreservationPolicy nitsAreInActiveRange:];
-[CBGammaContrastPreservationPolicy rampDownDuration];
-[CBGammaContrastPreservationPolicy rampDownLuxDeltaThresholdFor:];
-[CBGammaContrastPreservationPolicy rampTargetLuxCap];
-[CBGammaContrastPreservationPolicy rampUpLuxDeltaThresholdFor:];
-[CBGammaContrastPreservationPolicy strengthForNits:andLux:];
-[CBGammaContrastPreservationPolicy strengthNotification];
```
