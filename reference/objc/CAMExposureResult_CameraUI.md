# `CAMExposureResult`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _adjustingExposure;
B _exposureDidStart;
B _exposureDidEnd;
B _deviceSupportsFocus;
f _exposureTargetBias;
q _exposureMode;
{CGPoint="x"d"y"d} _pointOfInterest;
```

## Properties

```
@property (TB,R,N,GisAdjustingExposure,V_adjustingExposure) adjustingExposure;
@property (T{CGPoint=dd},R,N,V_pointOfInterest) pointOfInterest;
@property (Tq,R,N,V_exposureMode) exposureMode;
@property (Tf,R,N,V_exposureTargetBias) exposureTargetBias;
@property (TB,R,N,V_exposureDidStart) exposureDidStart;
@property (TB,R,N,V_exposureDidEnd) exposureDidEnd;
@property (TB,R,N,V_deviceSupportsFocus) deviceSupportsFocus;
```

## Instance methods

```
-[CAMExposureResult exposureMode];
-[CAMExposureResult exposureTargetBias];
-[CAMExposureResult isAdjustingExposure];
-[CAMExposureResult description];
-[CAMExposureResult pointOfInterest];
-[CAMExposureResult deviceSupportsFocus];
-[CAMExposureResult exposureDidEnd];
-[CAMExposureResult exposureDidStart];
-[CAMExposureResult initWithMode:pointOfInterest:exposureTargetBias:adjusting:exposureDidStart:exposureDidEnd:deviceSupportsFocus:];
```
