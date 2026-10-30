# `CAMSystemPressureState`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"AVCaptureSystemPressureState" __underlyingSystemPressureState;
```

## Properties

```
@property (T@"AVCaptureSystemPressureState",R,N,V__underlyingSystemPressureState) _underlyingSystemPressureState;
@property (TB,R,N,GisCameraTooHot) cameraTooHot;
@property (TB,R,N) hasBatteryStress;
@property (TB,R,N) shouldDisablePIPMotionBlur;
@property (TB,R,N) shouldDisableOptionalUIEffects;
@property (T@"AVCaptureSystemPressureState",R,N) underlyingSystemPressureState;
```

## Instance methods

```
-[CAMSystemPressureState description];
-[CAMSystemPressureState isEqual:];
-[CAMSystemPressureState _underlyingSystemPressureState];
-[CAMSystemPressureState hasBatteryStress];
-[CAMSystemPressureState initWithCaptureSystemPressureState:];
-[CAMSystemPressureState isCameraTooHot];
-[CAMSystemPressureState isEqualToSystemPressureState:];
-[CAMSystemPressureState shouldDisableOptionalUIEffects];
-[CAMSystemPressureState shouldDisablePIPMotionBlur];
-[CAMSystemPressureState underlyingSystemPressureState];
```
