# `SBDynamicFlashlightOptionsProvider` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 14 properties, 14 instance methods, 0 class methods

## Properties

```
@property (Td,R,N) minimumIntensity;
@property (Td,R,N) minimumHWIntensity;
@property (T{CGPoint=dd},R,N) gestureScaling;
@property (Td,R,N) gestureClampFactor;
@property (Td,R,N) tapMoveThreshold;
@property (Td,R,N) tapTimeThreshold;
@property (T@"SBFFluidBehaviorSettings",R,N) springAnimationSettings;
@property (Td,R,N) inertiaFactor;
@property (Td,R,N) overshootClampFactor;
@property (Td,R,N) heightStretchFactor;
@property (Td,R,N) widthStretchFactor;
@property (Td,R,N) persistenceDelay;
@property (Td,R,N) autoDismissalDelay;
@property (TB,R,N) suppressOnContinuity;
```

## Instance methods

```
-[SBDynamicFlashlightOptionsProvider autoDismissalDelay];
-[SBDynamicFlashlightOptionsProvider gestureClampFactor];
-[SBDynamicFlashlightOptionsProvider gestureScaling];
-[SBDynamicFlashlightOptionsProvider heightStretchFactor];
-[SBDynamicFlashlightOptionsProvider inertiaFactor];
-[SBDynamicFlashlightOptionsProvider minimumHWIntensity];
-[SBDynamicFlashlightOptionsProvider minimumIntensity];
-[SBDynamicFlashlightOptionsProvider overshootClampFactor];
-[SBDynamicFlashlightOptionsProvider persistenceDelay];
-[SBDynamicFlashlightOptionsProvider springAnimationSettings];
-[SBDynamicFlashlightOptionsProvider suppressOnContinuity];
-[SBDynamicFlashlightOptionsProvider tapMoveThreshold];
-[SBDynamicFlashlightOptionsProvider tapTimeThreshold];
-[SBDynamicFlashlightOptionsProvider widthStretchFactor];
```
