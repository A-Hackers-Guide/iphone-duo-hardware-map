# `BWStillImageCameraCalibrationDataNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 8 instance variables, 0 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _sensorConfigurationsByPortType;
B _propagatesDetectedObjects;
@"NSDictionary" _baseZoomFactorsByPortType;
@"NSSet" _expectedPortTypes;
@"BWStillImageCaptureSettings" _captureSettings;
i _processingMode;
@"NSMutableDictionary" _inputSbufsByPortType;
@"FigCalibration" _calibrationProcessor;
```

## Class methods

```
+[BWStillImageCameraCalibrationDataNode initialize];
```

## Instance methods

```
-[BWStillImageCameraCalibrationDataNode prepareForCurrentConfigurationToBecomeLive];
-[BWStillImageCameraCalibrationDataNode setBaseZoomFactorsByPortType:];
-[BWStillImageCameraCalibrationDataNode renderSampleBuffer:forInput:];
-[BWStillImageCameraCalibrationDataNode dealloc];
-[BWStillImageCameraCalibrationDataNode nodeSubType];
-[BWStillImageCameraCalibrationDataNode baseZoomFactorsByPortType];
-[BWStillImageCameraCalibrationDataNode didSelectFormat:forInput:];
-[BWStillImageCameraCalibrationDataNode handleNodeError:forInput:];
-[BWStillImageCameraCalibrationDataNode nodeType];
-[BWStillImageCameraCalibrationDataNode initWithSensorConfigurationsByPortType:];
-[BWStillImageCameraCalibrationDataNode propagatesDetectedObjects];
-[BWStillImageCameraCalibrationDataNode setPropagatesDetectedObjects:];
```
