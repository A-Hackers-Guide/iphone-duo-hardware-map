# `AVCaptureSynchronizedCameraCalibrationData`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureSynchronizedData`
- 3 instance variables, 3 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"AVCameraCalibrationData" _cameraCalibrationData;
B _cameraCalibrationDataWasDropped;
q _droppedReason;
```

## Properties

```
@property (T@"AVCameraCalibrationData",R) cameraCalibrationData;
@property (TB,R) cameraCalibrationDataWasDropped;
@property (Tq,R) droppedReason;
```

## Instance methods

```
-[AVCaptureSynchronizedCameraCalibrationData dealloc];
-[AVCaptureSynchronizedCameraCalibrationData cameraCalibrationData];
-[AVCaptureSynchronizedCameraCalibrationData cameraCalibrationDataWasDropped];
-[AVCaptureSynchronizedCameraCalibrationData _initWithCameraCalibrationData:timestamp:cameraCalibrationDataWasDropped:droppedReason:];
-[AVCaptureSynchronizedCameraCalibrationData droppedReason];
```
