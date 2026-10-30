# `CAMLevelViewModel`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMObservable`
- 8 instance variables, 8 properties, 26 instance methods, 0 class methods

## Instance variables

```
q _currentIndicatorMode;
d _currentIndicatorAlpha;
d _currentIndicatorRotationAngle;
d _desiredUpdateInterval;
q __desiredIndicatorMode;
d __desiredModeBeganTime;
d __lastNonZeroAngleTime;
{UIOffset="horizontal"d"vertical"d} __currentIndicatorOffset;
```

## Properties

```
@property (Tq,N,S_setCurrentIndicatorMode:,V_currentIndicatorMode) currentIndicatorMode;
@property (T{UIOffset=dd},N,S_setCurrentIndicatorOffset:,V__currentIndicatorOffset) _currentIndicatorOffset;
@property (Td,N,S_setCurrentIndicatorRotationAngle:,V_currentIndicatorRotationAngle) currentIndicatorRotationAngle;
@property (Td,N,S_setCurrentIndicatorAlpha:,V_currentIndicatorAlpha) currentIndicatorAlpha;
@property (Td,N,S_setDesiredUpdateInterval:,V_desiredUpdateInterval) desiredUpdateInterval;
@property (Tq,N,S_setDesiredIndicatorMode:,V__desiredIndicatorMode) _desiredIndicatorMode;
@property (Td,N,S_setDesiredModeBeganTime:,V__desiredModeBeganTime) _desiredModeBeganTime;
@property (Td,N,S_setLastNonZeroAngleTime:,V__lastNonZeroAngleTime) _lastNonZeroAngleTime;
```

## Instance methods

```
-[CAMLevelViewModel reset];
-[CAMLevelViewModel mutableChangeObject];
-[CAMLevelViewModel _updateModeNone];
-[CAMLevelViewModel _currentIndicatorOffset];
-[CAMLevelViewModel _desiredIndicatorMode];
-[CAMLevelViewModel _desiredModeBeganTime];
-[CAMLevelViewModel _deviceAngleForGravity:captureOrientation:relativeRoll:relativePitch:];
-[CAMLevelViewModel _hysteresisAlphaForDesiredAlpha:fromCurrentAlpha:];
-[CAMLevelViewModel _hysteresisModeForDesiredMode:];
-[CAMLevelViewModel _lastNonZeroAngleTime];
-[CAMLevelViewModel _setCurrentIndicatorAlpha:];
-[CAMLevelViewModel _setCurrentIndicatorMode:];
-[CAMLevelViewModel _setCurrentIndicatorOffset:];
-[CAMLevelViewModel _setCurrentIndicatorRotationAngle:];
-[CAMLevelViewModel _setDesiredIndicatorMode:];
-[CAMLevelViewModel _setDesiredModeBeganTime:];
-[CAMLevelViewModel _setDesiredUpdateInterval:];
-[CAMLevelViewModel _setLastNonZeroAngleTime:];
-[CAMLevelViewModel _updateFlatModeWithRoll:pitch:magnitude:];
-[CAMLevelViewModel _updateStraightModeWithMode:roll:pitch:];
-[CAMLevelViewModel applyDeviceMotion:captureOrientation:];
-[CAMLevelViewModel currentIndicatorAlpha];
-[CAMLevelViewModel currentIndicatorMode];
-[CAMLevelViewModel currentIndicatorOffsetWithScale:];
-[CAMLevelViewModel currentIndicatorRotationAngle];
-[CAMLevelViewModel desiredUpdateInterval];
```
