# `CAMFocusCommand`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCaptureCommand`
- 6 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
B __shouldUseSmoothFocus;
B __enableContinuousAutoFocusTracking;
B __configureSecondaryDevice;
q __focusMode;
q __rectSize;
{CGPoint="x"d"y"d} __focusPointOfInterest;
```

## Properties

```
@property (Tq,R,N,V__focusMode) _focusMode;
@property (Tq,R,N,V__rectSize) _rectSize;
@property (T{CGPoint=dd},R,N,V__focusPointOfInterest) _focusPointOfInterest;
@property (TB,R,N,V__shouldUseSmoothFocus) _shouldUseSmoothFocus;
@property (TB,R,N,V__enableContinuousAutoFocusTracking) _enableContinuousAutoFocusTracking;
@property (TB,R,N,V__configureSecondaryDevice) _configureSecondaryDevice;
```

## Instance methods

```
-[CAMFocusCommand _focusMode];
-[CAMFocusCommand initWithFocusMode:atPointOfInterest:rectSize:smooth:];
-[CAMFocusCommand _configureSecondaryDevice];
-[CAMFocusCommand _rectSize];
-[CAMFocusCommand _shouldUseSmoothFocus];
-[CAMFocusCommand _descriptionForFocusMode:];
-[CAMFocusCommand _enableContinuousAutoFocusTracking];
-[CAMFocusCommand initWithFocusMode:atPointOfInterest:rectSize:smooth:configureSecondaryDevice:enableContinuousAutoFocusTracking:];
-[CAMFocusCommand initWithFocusMode:];
-[CAMFocusCommand executeWithContext:];
-[CAMFocusCommand initWithFocusMode:atPointOfInterest:];
-[CAMFocusCommand initWithFocusMode:smooth:];
-[CAMFocusCommand _focusPointOfInterest];
-[CAMFocusCommand copyWithZone:];
```
