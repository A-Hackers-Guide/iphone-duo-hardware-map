# `CBBrightnessBoost`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
f boostScaler;
f boostStart;
f boostFull;
f boostFullEnd;
f boostEnd;
floatProperties;
```

## Properties

```
@property (Tf,N,VboostScaler) boostScaler;
@property (Tf,N,VboostStart) boostStart;
@property (Tf,N,VboostFull) boostFull;
@property (Tf,N,VboostFullEnd) boostFullEnd;
@property (Tf,N,VboostEnd) boostEnd;
```

## Instance methods

```
-[CBBrightnessBoost init];
-[CBBrightnessBoost initWithConfiguration:];
-[CBBrightnessBoost setFloatValue:forKey:];
-[CBBrightnessBoost setBoostScaler:];
-[CBBrightnessBoost boostEnd];
-[CBBrightnessBoost boostFull];
-[CBBrightnessBoost boostFullEnd];
-[CBBrightnessBoost boostScaler];
-[CBBrightnessBoost boostStart];
-[CBBrightnessBoost copyProperty:];
-[CBBrightnessBoost scalerForLux:];
-[CBBrightnessBoost setBoostEnd:];
-[CBBrightnessBoost setBoostFull:];
-[CBBrightnessBoost setBoostFullEnd:];
-[CBBrightnessBoost setBoostStart:];
```
