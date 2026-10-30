# `SBFTodayGestureSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 13 instance variables, 13 properties, 27 instance methods, 1 class methods

## Instance variables

```
B _scaleAnimationSettingsWithGestureVelocity;
d _sideSpringTension;
d _sideSpringFriction;
d _interactiveSideSpringTension;
d _interactiveSideSpringFriction;
@"SBFFluidBehaviorSettings" _overlayPositionSettings;
@"SBFFluidBehaviorSettings" _overlayBackdropSettings;
d _minimumVelocity;
d _maximumVelocity;
d _dampingRatioAtMinimumVelocity;
d _dampingRatioAtMaximumVelocity;
d _responseAtMinimumVelocity;
d _responseAtMaximumVelocity;
```

## Properties

```
@property (Td,N,V_sideSpringTension) sideSpringTension;
@property (Td,N,V_sideSpringFriction) sideSpringFriction;
@property (Td,N,V_interactiveSideSpringTension) interactiveSideSpringTension;
@property (Td,N,V_interactiveSideSpringFriction) interactiveSideSpringFriction;
@property (T@"SBFFluidBehaviorSettings",C,N,V_overlayPositionSettings) overlayPositionSettings;
@property (T@"SBFFluidBehaviorSettings",C,N,V_overlayBackdropSettings) overlayBackdropSettings;
@property (TB,N,V_scaleAnimationSettingsWithGestureVelocity) scaleAnimationSettingsWithGestureVelocity;
@property (Td,N,V_minimumVelocity) minimumVelocity;
@property (Td,N,V_maximumVelocity) maximumVelocity;
@property (Td,N,V_dampingRatioAtMinimumVelocity) dampingRatioAtMinimumVelocity;
@property (Td,N,V_dampingRatioAtMaximumVelocity) dampingRatioAtMaximumVelocity;
@property (Td,N,V_responseAtMinimumVelocity) responseAtMinimumVelocity;
@property (Td,N,V_responseAtMaximumVelocity) responseAtMaximumVelocity;
```

## Class methods

```
+[SBFTodayGestureSettings settingsControllerModule];
```

## Instance methods

```
-[SBFTodayGestureSettings setDefaultValues];
-[SBFTodayGestureSettings maximumVelocity];
-[SBFTodayGestureSettings setMaximumVelocity:];
-[SBFTodayGestureSettings minimumVelocity];
-[SBFTodayGestureSettings dampingRatioAtMaximumVelocity];
-[SBFTodayGestureSettings dampingRatioAtMinimumVelocity];
-[SBFTodayGestureSettings interactiveSideSpringFriction];
-[SBFTodayGestureSettings interactiveSideSpringTension];
-[SBFTodayGestureSettings overlayBackdropSettings];
-[SBFTodayGestureSettings overlayPositionSettings];
-[SBFTodayGestureSettings responseAtMaximumVelocity];
-[SBFTodayGestureSettings responseAtMinimumVelocity];
-[SBFTodayGestureSettings scaleAnimationSettingsWithGestureVelocity];
-[SBFTodayGestureSettings setDampingRatioAtMaximumVelocity:];
-[SBFTodayGestureSettings setDampingRatioAtMinimumVelocity:];
-[SBFTodayGestureSettings setInteractiveSideSpringFriction:];
-[SBFTodayGestureSettings setInteractiveSideSpringTension:];
-[SBFTodayGestureSettings setMinimumVelocity:];
-[SBFTodayGestureSettings setOverlayBackdropSettings:];
-[SBFTodayGestureSettings setOverlayPositionSettings:];
-[SBFTodayGestureSettings setResponseAtMaximumVelocity:];
-[SBFTodayGestureSettings setResponseAtMinimumVelocity:];
-[SBFTodayGestureSettings setScaleAnimationSettingsWithGestureVelocity:];
-[SBFTodayGestureSettings setSideSpringFriction:];
-[SBFTodayGestureSettings setSideSpringTension:];
-[SBFTodayGestureSettings sideSpringFriction];
-[SBFTodayGestureSettings sideSpringTension];
```
