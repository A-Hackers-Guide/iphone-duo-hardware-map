# `SBDynamicFlashlightSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- Protocols: `SBDynamicFlashlightOptionsProvider`
- 15 instance variables, 20 properties, 33 instance methods, 1 class methods

## Instance variables

```
B _suppressOnContinuity;
d _minimumIntensity;
d _minimumHWIntensity;
d _gestureXScaling;
d _gestureYScaling;
d _gestureClampFactor;
d _tapMoveThreshold;
d _tapTimeThreshold;
@"SBFFluidBehaviorSettings" _springAnimationSettings;
d _inertiaFactor;
d _overshootClampFactor;
d _heightStretchFactor;
d _widthStretchFactor;
d _persistenceDelay;
d _autoDismissalDelay;
```

## Properties

```
@property (Td,N,V_minimumIntensity) minimumIntensity;
@property (Td,N,V_minimumHWIntensity) minimumHWIntensity;
@property (Td,N,V_gestureXScaling) gestureXScaling;
@property (Td,N,V_gestureYScaling) gestureYScaling;
@property (Td,N,V_gestureClampFactor) gestureClampFactor;
@property (Td,N,V_tapMoveThreshold) tapMoveThreshold;
@property (Td,N,V_tapTimeThreshold) tapTimeThreshold;
@property (T@"SBFFluidBehaviorSettings",&,N,V_springAnimationSettings) springAnimationSettings;
@property (Td,N,V_inertiaFactor) inertiaFactor;
@property (Td,N,V_overshootClampFactor) overshootClampFactor;
@property (Td,N,V_heightStretchFactor) heightStretchFactor;
@property (Td,N,V_widthStretchFactor) widthStretchFactor;
@property (Td,N,V_persistenceDelay) persistenceDelay;
@property (Td,N,V_autoDismissalDelay) autoDismissalDelay;
@property (TB,N,V_suppressOnContinuity) suppressOnContinuity;
@property (T{CGPoint=dd},R,N) gestureScaling;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBDynamicFlashlightSettings settingsControllerModule];
```

## Instance methods

```
-[SBDynamicFlashlightSettings setDefaultValues];
-[SBDynamicFlashlightSettings setAutoDismissalDelay:];
-[SBDynamicFlashlightSettings autoDismissalDelay];
-[SBDynamicFlashlightSettings gestureYScaling];
-[SBDynamicFlashlightSettings gestureXScaling];
-[SBDynamicFlashlightSettings gestureClampFactor];
-[SBDynamicFlashlightSettings gestureScaling];
-[SBDynamicFlashlightSettings heightStretchFactor];
-[SBDynamicFlashlightSettings inertiaFactor];
-[SBDynamicFlashlightSettings minimumHWIntensity];
-[SBDynamicFlashlightSettings minimumIntensity];
-[SBDynamicFlashlightSettings overshootClampFactor];
-[SBDynamicFlashlightSettings persistenceDelay];
-[SBDynamicFlashlightSettings setGestureClampFactor:];
-[SBDynamicFlashlightSettings setGestureScaling:];
-[SBDynamicFlashlightSettings setGestureXScaling:];
-[SBDynamicFlashlightSettings setGestureYScaling:];
-[SBDynamicFlashlightSettings setHeightStretchFactor:];
-[SBDynamicFlashlightSettings setInertiaFactor:];
-[SBDynamicFlashlightSettings setMinimumHWIntensity:];
-[SBDynamicFlashlightSettings setMinimumIntensity:];
-[SBDynamicFlashlightSettings setOvershootClampFactor:];
-[SBDynamicFlashlightSettings setPersistenceDelay:];
-[SBDynamicFlashlightSettings setSpringAnimationSettings:];
-[SBDynamicFlashlightSettings setSuppressOnContinuity:];
-[SBDynamicFlashlightSettings setTapMoveThreshold:];
-[SBDynamicFlashlightSettings setTapTimeThreshold:];
-[SBDynamicFlashlightSettings setWidthStretchFactor:];
-[SBDynamicFlashlightSettings springAnimationSettings];
-[SBDynamicFlashlightSettings suppressOnContinuity];
-[SBDynamicFlashlightSettings tapMoveThreshold];
-[SBDynamicFlashlightSettings tapTimeThreshold];
-[SBDynamicFlashlightSettings widthStretchFactor];
```
