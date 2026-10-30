# `_UIFocusAnimationConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 11 instance variables, 11 properties, 28 instance methods, 1 class methods

## Instance variables

```
d _focusingBaseDuration;
d _unfocusingBaseDuration;
Q _animationOptions;
d _focusingDurationScaleFactorLowerBound;
d _focusingDurationScaleFactorUpperBound;
d _unfocusingDurationScaleFactorLowerBound;
d _unfocusingDurationScaleFactorUpperBound;
d _minimumFocusDuration;
d _unfocusingRepositionBaseDuration;
d _unfocusingBackgroundFadeDurationPercentage;
d _focusingDelay;
```

## Properties

```
@property (TQ,N,V_animationOptions) animationOptions;
@property (Td,N,V_focusingDurationScaleFactorLowerBound) focusingDurationScaleFactorLowerBound;
@property (Td,N,V_focusingDurationScaleFactorUpperBound) focusingDurationScaleFactorUpperBound;
@property (Td,N,V_unfocusingDurationScaleFactorLowerBound) unfocusingDurationScaleFactorLowerBound;
@property (Td,N,V_unfocusingDurationScaleFactorUpperBound) unfocusingDurationScaleFactorUpperBound;
@property (Td,N,V_minimumFocusDuration) minimumFocusDuration;
@property (Td,N,V_unfocusingRepositionBaseDuration) unfocusingRepositionBaseDuration;
@property (Td,N,V_unfocusingBackgroundFadeDurationPercentage) unfocusingBackgroundFadeDurationPercentage;
@property (Td,N,V_focusingDelay) focusingDelay;
@property (Td,N,V_focusingBaseDuration) focusingBaseDuration;
@property (Td,N,V_unfocusingBaseDuration) unfocusingBaseDuration;
```

## Class methods

```
+[_UIFocusAnimationConfiguration configurationWithStyle:];
```

## Instance methods

```
-[_UIFocusAnimationConfiguration animationOptions];
-[_UIFocusAnimationConfiguration setAnimationOptions:];
-[_UIFocusAnimationConfiguration focusingBaseDuration];
-[_UIFocusAnimationConfiguration init];
-[_UIFocusAnimationConfiguration unfocusingRepositionBaseDuration];
-[_UIFocusAnimationConfiguration unfocusingBackgroundFadeDurationPercentage];
-[_UIFocusAnimationConfiguration setUnfocusingBackgroundFadeDurationPercentage:];
-[_UIFocusAnimationConfiguration unfocusingDurationScaleFactorLowerBound];
-[_UIFocusAnimationConfiguration setFocusingBaseDuration:];
-[_UIFocusAnimationConfiguration _focusingVelocityBasedDurationScaleFactorForAnimationInContext:];
-[_UIFocusAnimationConfiguration focusingDelay];
-[_UIFocusAnimationConfiguration minimumFocusDuration];
-[_UIFocusAnimationConfiguration setUnfocusingRepositionBaseDuration:];
-[_UIFocusAnimationConfiguration focusingDurationScaleFactorLowerBound];
-[_UIFocusAnimationConfiguration _unfocusingVelocityBasedDurationScaleFactorForAnimationInContext:];
-[_UIFocusAnimationConfiguration unfocusingBaseDuration];
-[_UIFocusAnimationConfiguration setUnfocusingDurationScaleFactorLowerBound:];
-[_UIFocusAnimationConfiguration _defaultVelocityBasedDurationScaleFactorForAnimationInContext:];
-[_UIFocusAnimationConfiguration setUnfocusingDurationScaleFactorUpperBound:];
-[_UIFocusAnimationConfiguration setFocusingDurationScaleFactorLowerBound:];
-[_UIFocusAnimationConfiguration setUnfocusingBaseDuration:];
-[_UIFocusAnimationConfiguration _unfocusingRepositionVelocityBasedDurationScaleFactorForAnimationInContext:];
-[_UIFocusAnimationConfiguration unfocusingDurationScaleFactorUpperBound];
-[_UIFocusAnimationConfiguration setMinimumFocusDuration:];
-[_UIFocusAnimationConfiguration setFocusingDurationScaleFactorUpperBound:];
-[_UIFocusAnimationConfiguration copyWithZone:];
-[_UIFocusAnimationConfiguration focusingDurationScaleFactorUpperBound];
-[_UIFocusAnimationConfiguration setFocusingDelay:];
```
