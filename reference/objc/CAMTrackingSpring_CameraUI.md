# `CAMTrackingSpring`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMSpring`
- 3 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"CAMSpring" __settleProgressSpring;
d __convergenceStartValue;
{?="value"d"strength"d} __secondaryTarget;
```

## Properties

```
@property (T@"CAMSpring",&,N,S_setSettlingSpring:,V__settleProgressSpring) _settleProgressSpring;
@property (T{?=dd},N,S_setSecondaryTarget:,V__secondaryTarget) _secondaryTarget;
@property (Td,N,S_convergenceStartValue:,V__convergenceStartValue) _convergenceStartValue;
@property (Td,R,N) convergenceProgress;
@property (TB,R,N) hasSecondaryTarget;
```

## Instance methods

```
-[CAMTrackingSpring updateForTimestamp:];
-[CAMTrackingSpring initWithTension:friction:epsilon:];
-[CAMTrackingSpring resetToValue:];
-[CAMTrackingSpring isConverged];
-[CAMTrackingSpring removeSecondaryTargetAnimated:];
-[CAMTrackingSpring setSecondaryTarget:withStrength:animated:];
-[CAMTrackingSpring setTarget:animated:];
-[CAMTrackingSpring convergenceProgress];
-[CAMTrackingSpring hasSecondaryTarget];
-[CAMTrackingSpring _convergenceStartValue];
-[CAMTrackingSpring _setSettlingSpring:];
-[CAMTrackingSpring _settleProgressSpring];
-[CAMTrackingSpring _setSecondaryTarget:];
-[CAMTrackingSpring _secondaryTarget];
-[CAMTrackingSpring resetToValue:animated:];
-[CAMTrackingSpring _beginConverging];
-[CAMTrackingSpring _convergenceStartValue:];
```
