# `AVCaptureManualExposureBracketedStillImageSettings`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureBracketedStillImageSettings`
- 2 instance variables, 2 properties, 5 instance methods, 2 class methods

## Instance variables

```
{?="value"q"timescale"i"flags"I"epoch"q} _exposureDuration;
f _ISO;
```

## Properties

```
@property (T{?=qiIq},R,V_exposureDuration) exposureDuration;
@property (Tf,R,V_ISO) ISO;
```

## Class methods

```
+[AVCaptureManualExposureBracketedStillImageSettings initialize];
+[AVCaptureManualExposureBracketedStillImageSettings manualExposureSettingsWithExposureDuration:ISO:];
```

## Instance methods

```
-[AVCaptureManualExposureBracketedStillImageSettings exposureDuration];
-[AVCaptureManualExposureBracketedStillImageSettings ISO];
-[AVCaptureManualExposureBracketedStillImageSettings debugDescription];
-[AVCaptureManualExposureBracketedStillImageSettings description];
-[AVCaptureManualExposureBracketedStillImageSettings _initManualExposureSettingsWithExposureDuration:ISO:];
```
