# `FigCaptureAutoFocusPositionSensorCalibrationIStopZEstimateDeltaHistory`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
i _lastPassingIStopZEstimateDelta;
i _previousIStopZEstimateDelta;
i _currentIStopZEstimateDelta;
i _previousIStopZEstimate;
i _currentIStopZEstimate;
```

## Properties

```
@property (Ti,N,V_lastPassingIStopZEstimateDelta) lastPassingIStopZEstimateDelta;
@property (Ti,N,V_previousIStopZEstimate) previousIStopZEstimateDelta;
@property (Ti,N,V_currentIStopZEstimate) currentIStopZEstimateDelta;
```

## Instance methods

```
-[FigCaptureAutoFocusPositionSensorCalibrationIStopZEstimateDeltaHistory setPreviousIStopZEstimateDelta:];
-[FigCaptureAutoFocusPositionSensorCalibrationIStopZEstimateDeltaHistory currentIStopZEstimateDelta];
-[FigCaptureAutoFocusPositionSensorCalibrationIStopZEstimateDeltaHistory lastPassingIStopZEstimateDelta];
-[FigCaptureAutoFocusPositionSensorCalibrationIStopZEstimateDeltaHistory previousIStopZEstimateDelta];
-[FigCaptureAutoFocusPositionSensorCalibrationIStopZEstimateDeltaHistory setCurrentIStopZEstimateDelta:];
-[FigCaptureAutoFocusPositionSensorCalibrationIStopZEstimateDeltaHistory setLastPassingIStopZEstimateDelta:];
```
