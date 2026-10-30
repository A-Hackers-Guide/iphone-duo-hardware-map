# `CAMCustomExposureValues`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 10 properties, 12 instance methods, 6 class methods

## Instance variables

```
f _ISO;
f _lensAperture;
{?="value"q"timescale"i"flags"I"epoch"q} _duration;
```

## Properties

```
@property (TB,R,N) isAutoDuration;
@property (TB,R,N) isAutoISO;
@property (TB,R,N) isAutoLensAperture;
@property (TB,R,N) isCurrentDuration;
@property (TB,R,N) isCurrentISO;
@property (TB,R,N) isCurrentLensAperture;
@property (TB,R,N) isAuto;
@property (T{?=qiIq},R,N,V_duration) duration;
@property (Tf,R,N,V_ISO) ISO;
@property (Tf,R,N,V_lensAperture) lensAperture;
```

## Class methods

```
+[CAMCustomExposureValues durationCurrent];
+[CAMCustomExposureValues ISOAuto];
+[CAMCustomExposureValues ISOCurrent];
+[CAMCustomExposureValues durationAuto];
+[CAMCustomExposureValues lensApertureAuto];
+[CAMCustomExposureValues lensApertureCurrent];
```

## Instance methods

```
-[CAMCustomExposureValues ISO];
-[CAMCustomExposureValues lensAperture];
-[CAMCustomExposureValues duration];
-[CAMCustomExposureValues isAuto];
-[CAMCustomExposureValues initWithAuto];
-[CAMCustomExposureValues initWithDuration:ISO:lensAperture:];
-[CAMCustomExposureValues isAutoDuration];
-[CAMCustomExposureValues isAutoISO];
-[CAMCustomExposureValues isAutoLensAperture];
-[CAMCustomExposureValues isCurrentDuration];
-[CAMCustomExposureValues isCurrentISO];
-[CAMCustomExposureValues isCurrentLensAperture];
```
