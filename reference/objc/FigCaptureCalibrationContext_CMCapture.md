# `FigCaptureCalibrationContext`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 8 properties, 17 instance methods, 6 class methods

## Instance variables

```
@"NSMutableDictionary" _lastSuccessfulCalibrationData;
d _lastSuccessfulCalibrationTimeStamp;
{?="x"d"y"d"z"d} _lastSuccessfulCalibrationMagneticField;
@"NSString" _activityName;
@"NSString" _preferenceString;
@"NSString" _propertyName;
Q _expectedDataSize;
i _interval;
i _minimumBatteryLevelToRun;
@"NSString" _internalLogName;
@"NSArray" _supportedDevices;
```

## Properties

```
@property (T@"NSDictionary",&,N) lastSuccessfulCalibrationData;
@property (Td,N,V_lastSuccessfulCalibrationTimeStamp) lastSuccessfulCalibrationTimeStamp;
@property (T{?=ddd},N,V_lastSuccessfulCalibrationMagneticField) lastSuccessfulCalibrationMagneticField;
@property (T@"NSString",R,N,V_activityName) activityName;
@property (T@"NSString",R,N,V_propertyName) propertyName;
@property (TQ,R,N,V_expectedDataSize) expectedDataSize;
@property (Ti,R,N,V_interval) interval;
@property (Ti,R,N,V_minimumBatteryLevelToRun) minimumBatteryLevelToRun;
```

## Class methods

```
+[FigCaptureCalibrationContext initialize];
+[FigCaptureCalibrationContext calibrationDataStringForInternalLogging:];
+[FigCaptureCalibrationContext calibrationStatusFromRawStreamCalibrationData:];
+[FigCaptureCalibrationContext createRawStreamCalibrationDataWithFailureReasons:];
+[FigCaptureCalibrationContext printDebugInfoForRawStreamCalibrationData:];
+[FigCaptureCalibrationContext setStatusForCalibrationData:status:];
```

## Instance methods

```
-[FigCaptureCalibrationContext interval];
-[FigCaptureCalibrationContext propertyName];
-[FigCaptureCalibrationContext activityName];
-[FigCaptureCalibrationContext calibrationDataHistory];
-[FigCaptureCalibrationContext expectedDataSize];
-[FigCaptureCalibrationContext initWithPreferenceString:withActivityName:withPropertyName:withExpectedDataSize:withInterval:withMinimumBatteryLevel:withInternalLogName:supportedDeviceNames:];
-[FigCaptureCalibrationContext initWithSupportedDeviceNames:];
-[FigCaptureCalibrationContext lastSuccessfulCalibrationData];
-[FigCaptureCalibrationContext lastSuccessfulCalibrationMagneticField];
-[FigCaptureCalibrationContext lastSuccessfulCalibrationTimeStamp];
-[FigCaptureCalibrationContext minimumBatteryLevelToRun];
-[FigCaptureCalibrationContext pushCalibrationDataToHistory:isRejected:];
-[FigCaptureCalibrationContext reportLoggingWithCalibrationData:isValid:magneticFieldMagnitude:];
-[FigCaptureCalibrationContext setLastSuccessfulCalibrationData:];
-[FigCaptureCalibrationContext setLastSuccessfulCalibrationMagneticField:];
-[FigCaptureCalibrationContext setLastSuccessfulCalibrationTimeStamp:];
-[FigCaptureCalibrationContext updateWithNewCalibrationData:orExternalErrors:magneticFieldAttempts:magneticField:isCalibrationValid:calibrationStatus:];
```
