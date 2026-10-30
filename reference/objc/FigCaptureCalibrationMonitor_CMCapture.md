# `FigCaptureCalibrationMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 0 properties, 6 instance methods, 3 class methods

## Instance variables

```
@"NSMutableArray" _streamCalibrationInformation;
@"NSObject<OS_dispatch_queue>" _calibrationRunQueue;
^{OpaqueFigSimpleMutex=} _calibrationPipelineMutex;
B _calibrationShouldAbort;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _calibrationLock;
{?="x"d"y"d"z"d} _coreMotionMagneticField;
d _coreMotionMagneticFieldMagnitude;
i _magneticFieldAttempt;
i _magneticFieldAccuracyAttemptCount;
[1{?="attemptCount"i"threshold"d}] _magneticFieldMagnitudeTiers;
@"FigCaptureAutoFocusPositionSensorCalibrationContext" _autoFocusPositionSensorCalibrationContext;
@"FigCaptureAutoFocusCalibrationContext" _autoFocusCalibrationContext;
@"FigCaptureAPSSphereInteractionCalibrationContext" _apsSphereInteractionCalibrationContext;
@"FigCaptureSphereCalibrationContext" _sphereCalibrationContext;
@"FigCaptureSphereEndStopCalibrationContext" _sphereEndStopCalibrationContext;
```

## Class methods

```
+[FigCaptureCalibrationMonitor sharedInstance];
+[FigCaptureCalibrationMonitor initialize];
+[FigCaptureCalibrationMonitor initializeSharedInstanceWithCaptureSourceBackings:];
```

## Instance methods

```
-[FigCaptureCalibrationMonitor apsSphereInteractionCalibrationData];
-[FigCaptureCalibrationMonitor autoFocusCalibrationData];
-[FigCaptureCalibrationMonitor autoFocusPositionSensorCalibrationData];
-[FigCaptureCalibrationMonitor runAutoFocusPositionSensorCalibrationAndGetResultsForDeviceType:devicePosition:];
-[FigCaptureCalibrationMonitor sphereCalibrationData];
-[FigCaptureCalibrationMonitor sphereEndStopCalibrationData];
```
