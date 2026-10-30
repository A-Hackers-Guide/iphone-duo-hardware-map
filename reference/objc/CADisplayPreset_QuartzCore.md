# `CADisplayPreset`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 7 properties, 12 instance methods, 0 class methods

## Instance variables

```
f _autoLuminanceBoost;
B _allowTrueTone;
B _allowNightShift;
B _allowAutoBrightness;
B _isReference;
d _minSliderBrightness;
d _maxSliderBrightness;
@"CAUserAdjustment" _userAdjustment;
```

## Properties

```
@property (TB,R,V_allowTrueTone) allowTrueTone;
@property (TB,R,V_allowNightShift) allowNightShift;
@property (TB,R,V_allowAutoBrightness) allowAutoBrightness;
@property (Td,R,V_minSliderBrightness) minSliderBrightness;
@property (Td,R,V_maxSliderBrightness) maxSliderBrightness;
@property (TB,R,V_isReference) isReference;
@property (T@"CAUserAdjustment",R,V_userAdjustment) userAdjustment;
```

## Instance methods

```
-[CADisplayPreset isReference];
-[CADisplayPreset dealloc];
-[CADisplayPreset allowNightShift];
-[CADisplayPreset allowAutoBrightness];
-[CADisplayPreset allowTrueTone];
-[CADisplayPreset applyUserAdjustmentCommand:];
-[CADisplayPreset initWithIsReference:userAdjustment:];
-[CADisplayPreset initWithIsReference:userAdjustment:autoLuminanceBoost:];
-[CADisplayPreset maxSliderBrightness];
-[CADisplayPreset minSliderBrightness];
-[CADisplayPreset userAdjustment];
-[CADisplayPreset userAdjustmentCommand];
```
