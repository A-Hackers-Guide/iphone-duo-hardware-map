# `CBPreset`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 11 properties, 12 instance methods, 1 class methods

## Instance variables

```
B _trueToneDisabled;
B _nightShiftDisabled;
B _autoBrighnessDisabled;
B _brightnessDisabled;
B _referenceMode;
B _alwaysRequestMaxHeadroom;
I _luminanceThrottlePolicy;
@"NSNumber" _luminanceThrottleLimit;
@"NSNumber" _maxPotentialEDRHeadroom;
```

## Properties

```
@property (TB,R,V_trueToneDisabled) trueToneDisabled;
@property (TB,R,V_nightShiftDisabled) nightShiftDisabled;
@property (TB,R,V_autoBrighnessDisabled) autoBrighnessDisabled;
@property (TB,R,V_brightnessDisabled) brightnessDisabled;
@property (TB,R,V_referenceMode) referenceMode;
@property (Tf,R) maxSDRLuminance;
@property (T@"NSNumber",R) maxAutobrightnessSDRLuminance;
@property (TI,R,V_luminanceThrottlePolicy) luminanceThrottlePolicy;
@property (T@"NSNumber",R,V_luminanceThrottleLimit) luminanceThrottleLimit;
@property (T@"NSNumber",R,V_maxPotentialEDRHeadroom) maxPotentialEDRHeadroom;
@property (TB,R,V_alwaysRequestMaxHeadroom) alwaysRequestMaxHeadroom;
```

## Class methods

```
+[CBPreset newActive:];
```

## Instance methods

```
-[CBPreset maxSDRLuminance];
-[CBPreset alwaysRequestMaxHeadroom];
-[CBPreset autoBrighnessDisabled];
-[CBPreset brightnessDisabled];
-[CBPreset initWithCAPreset:];
-[CBPreset luminanceThrottleLimit];
-[CBPreset luminanceThrottlePolicy];
-[CBPreset maxAutobrightnessSDRLuminance];
-[CBPreset maxPotentialEDRHeadroom];
-[CBPreset nightShiftDisabled];
-[CBPreset referenceMode];
-[CBPreset trueToneDisabled];
```
