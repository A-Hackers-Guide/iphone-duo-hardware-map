# `CMSensorRecorder`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 23 instance methods, 6 class methods

## Class methods

```
+[CMSensorRecorder authorizationStatus];
+[CMSensorRecorder isAccelerometerRecordingAvailable];
+[CMSensorRecorder isAuthorizedForRecording];
+[CMSensorRecorder isGyroRecordingAvailable];
+[CMSensorRecorder isPressureRecordingAvailable];
+[CMSensorRecorder isRecordingAvailableForType:];
```

## Instance methods

```
-[CMSensorRecorder recordAccelerometerForDuration:];
-[CMSensorRecorder accelerometerDataFrom:to:];
-[CMSensorRecorder accelerometerDataFromDate:toDate:];
-[CMSensorRecorder accelerometerDataSince:];
-[CMSensorRecorder accelerometerDataSinceId:];
-[CMSensorRecorder gyroDataFromDate:toDate:];
-[CMSensorRecorder gyroDataSinceId:];
-[CMSensorRecorder pressureDataFromDate:toDate:];
-[CMSensorRecorder pressureDataSinceId:];
-[CMSensorRecorder recordAccelerometerFor:];
-[CMSensorRecorder recordDataType:forDuration:];
-[CMSensorRecorder recordGyroForDuration:];
-[CMSensorRecorder recordPressureForDuration:];
-[CMSensorRecorder sendAccelDataToUrl:fromDate:toDate:];
-[CMSensorRecorder sendGyroDataToUrl:fromDate:toDate:];
-[CMSensorRecorder sendPressureDataToUrl:fromDate:toDate:];
-[CMSensorRecorder sendSensorDataToUrl:fromDate:toDate:forType:];
-[CMSensorRecorder sensorDataFromDate:toDate:forType:];
-[CMSensorRecorder setAccelSampleRate:];
-[CMSensorRecorder setGyroSampleRate:];
-[CMSensorRecorder setPressureSampleRate:];
-[CMSensorRecorder setSensorSampleRate:forType:];
-[CMSensorRecorder validateTimesFromDate:toDate:];
```
