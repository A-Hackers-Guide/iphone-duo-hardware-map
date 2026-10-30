# `CAMExposureCommand`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCaptureCommand`
- 3 instance variables, 3 properties, 9 instance methods, 0 class methods

## Instance variables

```
B __configureSecondaryDevice;
q __exposureMode;
{CGPoint="x"d"y"d} __exposurePointOfInterest;
```

## Properties

```
@property (Tq,R,N,V__exposureMode) _exposureMode;
@property (T{CGPoint=dd},R,N,V__exposurePointOfInterest) _exposurePointOfInterest;
@property (TB,R,N,V__configureSecondaryDevice) _configureSecondaryDevice;
```

## Instance methods

```
-[CAMExposureCommand initWithExposureMode:];
-[CAMExposureCommand _configureSecondaryDevice];
-[CAMExposureCommand initWithExposureMode:atPointOfInterest:configureSecondaryDevice:];
-[CAMExposureCommand _descriptionForExposureMode:];
-[CAMExposureCommand initWithExposureMode:atPointOfInterest:];
-[CAMExposureCommand executeWithContext:];
-[CAMExposureCommand _exposurePointOfInterest];
-[CAMExposureCommand copyWithZone:];
-[CAMExposureCommand _exposureMode];
```
