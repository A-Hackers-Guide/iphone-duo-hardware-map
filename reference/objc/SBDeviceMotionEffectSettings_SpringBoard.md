# `SBDeviceMotionEffectSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 6 instance variables, 6 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _optimizingBacklightChangeSource;
B _optimizingLowPower;
B _optimizingReducedMotion;
B _optimizingSignificantMotion;
B _optimizingUserPresence;
B _optimizingWallpaperObscured;
```

## Properties

```
@property (TB,N,V_optimizingBacklightChangeSource) optimizingBacklightChangeSource;
@property (TB,N,V_optimizingLowPower) optimizingLowPower;
@property (TB,N,V_optimizingReducedMotion) optimizingReducedMotion;
@property (TB,N,V_optimizingSignificantMotion) optimizingSignificantMotion;
@property (TB,N,V_optimizingUserPresence) optimizingUserPresence;
@property (TB,N,V_optimizingWallpaperObscured) optimizingWallpaperObscured;
```

## Class methods

```
+[SBDeviceMotionEffectSettings settingsControllerModule];
```

## Instance methods

```
-[SBDeviceMotionEffectSettings setDefaultValues];
-[SBDeviceMotionEffectSettings setOptimizingSignificantMotion:];
-[SBDeviceMotionEffectSettings optimizingBacklightChangeSource];
-[SBDeviceMotionEffectSettings setOptimizingWallpaperObscured:];
-[SBDeviceMotionEffectSettings optimizingLowPower];
-[SBDeviceMotionEffectSettings optimizingReducedMotion];
-[SBDeviceMotionEffectSettings optimizingSignificantMotion];
-[SBDeviceMotionEffectSettings optimizingUserPresence];
-[SBDeviceMotionEffectSettings optimizingWallpaperObscured];
-[SBDeviceMotionEffectSettings setOptimizingBacklightChangeSource:];
-[SBDeviceMotionEffectSettings setOptimizingLowPower:];
-[SBDeviceMotionEffectSettings setOptimizingReducedMotion:];
-[SBDeviceMotionEffectSettings setOptimizingUserPresence:];
```
