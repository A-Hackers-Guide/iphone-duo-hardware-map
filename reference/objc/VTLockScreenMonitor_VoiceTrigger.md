# `VTLockScreenMonitor`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTEventMonitor`
- 2 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
i _notifyToken;
C _lockScreenState;
```

## Class methods

```
+[VTLockScreenMonitor sharedInstance];
```

## Instance methods

```
-[VTLockScreenMonitor init];
-[VTLockScreenMonitor _stopMonitoring];
-[VTLockScreenMonitor _startMonitoringWithQueue:];
-[VTLockScreenMonitor lockScreenState];
-[VTLockScreenMonitor _checkLockScreenState];
-[VTLockScreenMonitor _didReceiveLockScreenStateChanged:];
-[VTLockScreenMonitor _didReceiveLockScreenStateChangedInQueue:];
-[VTLockScreenMonitor _notifyObserver:withLockScreenState:];
-[VTLockScreenMonitor lockScreenStateDescription:];
```
