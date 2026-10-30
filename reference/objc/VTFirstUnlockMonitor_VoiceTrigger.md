# `VTFirstUnlockMonitor`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTEventMonitor`
- 2 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
i _notifyToken;
B _firstUnlocked;
```

## Class methods

```
+[VTFirstUnlockMonitor sharedInstance];
```

## Instance methods

```
-[VTFirstUnlockMonitor init];
-[VTFirstUnlockMonitor _stopMonitoring];
-[VTFirstUnlockMonitor _startMonitoringWithQueue:];
-[VTFirstUnlockMonitor isFirstUnlocked];
-[VTFirstUnlockMonitor _checkFirstUnlocked];
-[VTFirstUnlockMonitor _didReceiveFirstUnlock:];
-[VTFirstUnlockMonitor _didReceiveFirstUnlockInQueue:];
-[VTFirstUnlockMonitor _notifyObserver:withUnlocked:];
```
