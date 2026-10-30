# `VTSpringboardStartMonitor`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTEventMonitor`
- 2 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
i _notifyToken;
B _isSpringBoardStarted;
```

## Class methods

```
+[VTSpringboardStartMonitor sharedInstance];
```

## Instance methods

```
-[VTSpringboardStartMonitor init];
-[VTSpringboardStartMonitor _stopMonitoring];
-[VTSpringboardStartMonitor _startMonitoringWithQueue:];
-[VTSpringboardStartMonitor _checkSpringBoardStarted];
-[VTSpringboardStartMonitor isSpringboardStarted];
-[VTSpringboardStartMonitor _didReceiveSpringboardStarted:];
-[VTSpringboardStartMonitor _didReceiveSpringboardStartedInQueue:];
-[VTSpringboardStartMonitor _notifyObserver:withStarted:];
```
