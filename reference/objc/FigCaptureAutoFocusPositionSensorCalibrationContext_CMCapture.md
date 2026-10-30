# `FigCaptureAutoFocusPositionSensorCalibrationContext`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureCalibrationContext`
- 10 instance variables, 1 properties, 17 instance methods, 6 class methods

## Instance variables

```
B _shouldDeleteOldVersion;
@"NSMutableDictionary" _iStopZEstimateDeltaHistory;
d _previousAngleDelta;
d _currentAngleDelta;
@"NSMutableArray" _calibrationDataHistoryQueue;
i _maxHistoryBuffer;
B _lastSuccessfulCalibrationWasDiscarded;
B _disableHistoryChecking;
i _maxIStopZEstimateDifference;
i _minCompassHeadingChange;
```

## Properties

```
@property (TB,N,V_disableHistoryChecking) disableHistoryChecking;
```

## Class methods

```
+[FigCaptureAutoFocusPositionSensorCalibrationContext initialize];
+[FigCaptureAutoFocusPositionSensorCalibrationContext calibrationDataStringForInternalLogging:];
+[FigCaptureAutoFocusPositionSensorCalibrationContext calibrationStatusFromRawStreamCalibrationData:];
+[FigCaptureAutoFocusPositionSensorCalibrationContext createRawStreamCalibrationDataWithFailureReasons:];
+[FigCaptureAutoFocusPositionSensorCalibrationContext printDebugInfoForRawStreamCalibrationData:];
+[FigCaptureAutoFocusPositionSensorCalibrationContext setStatusForCalibrationData:status:];
```

## Instance methods

```
-[FigCaptureAutoFocusPositionSensorCalibrationContext _pushToCalibrationHistoryQueue:];
-[FigCaptureAutoFocusPositionSensorCalibrationContext _calibrationDataCompassHeadingHasMovedPastMinimum:basedOnCalibrationHistory:];
-[FigCaptureAutoFocusPositionSensorCalibrationContext _calibrationDataIsWithinIStopZEstimateLimits:basedOnCalibrationHistory:];
-[FigCaptureAutoFocusPositionSensorCalibrationContext _initForUnitTests];
-[FigCaptureAutoFocusPositionSensorCalibrationContext _shouldRejectCalibrationData:];
-[FigCaptureAutoFocusPositionSensorCalibrationContext calibrationDataHistory];
-[FigCaptureAutoFocusPositionSensorCalibrationContext currentAngleDelta];
-[FigCaptureAutoFocusPositionSensorCalibrationContext currentIStopZEstimateDeltaForPosition:];
-[FigCaptureAutoFocusPositionSensorCalibrationContext disableHistoryChecking];
-[FigCaptureAutoFocusPositionSensorCalibrationContext initWithSupportedDeviceNames:];
-[FigCaptureAutoFocusPositionSensorCalibrationContext passingIStopZEstimateDeltaForPosition:];
-[FigCaptureAutoFocusPositionSensorCalibrationContext previousAngleDelta];
-[FigCaptureAutoFocusPositionSensorCalibrationContext previousIStopZEstimateDeltaForPosition:];
-[FigCaptureAutoFocusPositionSensorCalibrationContext pushCalibrationDataToHistory:isRejected:];
-[FigCaptureAutoFocusPositionSensorCalibrationContext reportLoggingWithCalibrationData:isValid:magneticFieldMagnitude:];
-[FigCaptureAutoFocusPositionSensorCalibrationContext setDisableHistoryChecking:];
-[FigCaptureAutoFocusPositionSensorCalibrationContext setLastSuccessfulCalibrationData:];
```
