# `BWAutoFocusPositionSensorMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 2 instance methods, 6 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _apsMonitorQueue;
@"FigCaptureDisplayLayoutMonitor" _displayLayoutMonitor;
```

## Class methods

```
+[BWAutoFocusPositionSensorMonitor sharedInstance];
+[BWAutoFocusPositionSensorMonitor initialize];
+[BWAutoFocusPositionSensorMonitor logVideoRecordingAPSStatistics:];
+[BWAutoFocusPositionSensorMonitor clientHasBeenBackgrounded];
+[BWAutoFocusPositionSensorMonitor logStillImageAPSStatistics:];
+[BWAutoFocusPositionSensorMonitor processAPSOffsetEstimatorInfo:portType:];
```

## Instance methods

```
-[BWAutoFocusPositionSensorMonitor init];
-[BWAutoFocusPositionSensorMonitor dealloc];
```
