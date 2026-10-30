# `CAMCustomExposureCommand`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCaptureCommand`
- 4 instance variables, 4 properties, 7 instance methods, 6 class methods

## Instance variables

```
f __ISO;
f __lensAperture;
@? __completionHandler;
{?="value"q"timescale"i"flags"I"epoch"q} __duration;
```

## Properties

```
@property (T{?=qiIq},R,N,V__duration) _duration;
@property (Tf,R,N,V__ISO) _ISO;
@property (Tf,R,N,V__lensAperture) _lensAperture;
@property (T@?,R,C,N,V__completionHandler) _completionHandler;
```

## Class methods

```
+[CAMCustomExposureCommand durationCurrent];
+[CAMCustomExposureCommand ISOAuto];
+[CAMCustomExposureCommand ISOCurrent];
+[CAMCustomExposureCommand durationAuto];
+[CAMCustomExposureCommand lensApertureAuto];
+[CAMCustomExposureCommand lensApertureCurrent];
```

## Instance methods

```
-[CAMCustomExposureCommand _duration];
-[CAMCustomExposureCommand executeWithContext:];
-[CAMCustomExposureCommand copyWithZone:];
-[CAMCustomExposureCommand _completionHandler];
-[CAMCustomExposureCommand _ISO];
-[CAMCustomExposureCommand _lensAperture];
-[CAMCustomExposureCommand initWithDuration:ISO:lensAperture:completionHandler:];
```
