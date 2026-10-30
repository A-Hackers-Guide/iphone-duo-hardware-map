# `FigCaptureStillImageProcessingSettings`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 15 instance methods, 1 class methods

## Instance variables

```
f _uiZoomFactor;
I _sensorRawPixelFormat;
{?="width"i"height"i} _sensorRawDimensions;
{?="width"i"height"i} _ultraHighResSensorRawDimensions;
@"NSDictionary" _cameraInfoByPortType;
@"NSDictionary" _moduleCalibrationByPortType;
```

## Properties

```
@property (Tf,N,V_uiZoomFactor) uiZoomFactor;
@property (TI,N,V_sensorRawPixelFormat) sensorRawPixelFormat;
@property (T{?=ii},N,V_sensorRawDimensions) sensorRawDimensions;
@property (T{?=ii},N,V_ultraHighResSensorRawDimensions) ultraHighResSensorRawDimensions;
@property (T@"NSDictionary",C,N,V_cameraInfoByPortType) cameraInfoByPortType;
@property (T@"NSDictionary",C,N,V_moduleCalibrationByPortType) moduleCalibrationByPortType;
```

## Class methods

```
+[FigCaptureStillImageProcessingSettings supportsSecureCoding];
```

## Instance methods

```
-[FigCaptureStillImageProcessingSettings sensorRawPixelFormat];
-[FigCaptureStillImageProcessingSettings moduleCalibrationByPortType];
-[FigCaptureStillImageProcessingSettings sensorRawDimensions];
-[FigCaptureStillImageProcessingSettings setCameraInfoByPortType:];
-[FigCaptureStillImageProcessingSettings cameraInfoByPortType];
-[FigCaptureStillImageProcessingSettings setUiZoomFactor:];
-[FigCaptureStillImageProcessingSettings setModuleCalibrationByPortType:];
-[FigCaptureStillImageProcessingSettings dealloc];
-[FigCaptureStillImageProcessingSettings encodeWithCoder:];
-[FigCaptureStillImageProcessingSettings setSensorRawPixelFormat:];
-[FigCaptureStillImageProcessingSettings initWithCoder:];
-[FigCaptureStillImageProcessingSettings uiZoomFactor];
-[FigCaptureStillImageProcessingSettings ultraHighResSensorRawDimensions];
-[FigCaptureStillImageProcessingSettings setSensorRawDimensions:];
-[FigCaptureStillImageProcessingSettings setUltraHighResSensorRawDimensions:];
```
