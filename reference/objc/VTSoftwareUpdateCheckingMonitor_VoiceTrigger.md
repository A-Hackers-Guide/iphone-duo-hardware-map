# `VTSoftwareUpdateCheckingMonitor`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTEventMonitor`
- 2 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
i _notifyToken;
B _isSoftwareUpdateCheckingRunning;
```

## Class methods

```
+[VTSoftwareUpdateCheckingMonitor sharedInstance];
```

## Instance methods

```
-[VTSoftwareUpdateCheckingMonitor init];
-[VTSoftwareUpdateCheckingMonitor _stopMonitoring];
-[VTSoftwareUpdateCheckingMonitor _startMonitoringWithQueue:];
-[VTSoftwareUpdateCheckingMonitor isSoftwareUpdateCheckingRunning];
-[VTSoftwareUpdateCheckingMonitor _checkSoftwareUpdateCheckingState];
-[VTSoftwareUpdateCheckingMonitor _didReceiveSoftwareUpdateCheckingStateChanged:];
-[VTSoftwareUpdateCheckingMonitor _didReceiveSoftwareUpdateCheckingStateChangedInQueue:];
-[VTSoftwareUpdateCheckingMonitor _notifyObserver:withSoftwareUpdateCheckingRunning:];
-[VTSoftwareUpdateCheckingMonitor _softwareUpdateCheckingState];
```
