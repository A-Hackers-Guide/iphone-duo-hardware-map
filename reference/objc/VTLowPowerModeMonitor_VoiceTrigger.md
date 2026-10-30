# `VTLowPowerModeMonitor`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTEventMonitor`
- 1 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
C _powerMode;
```

## Class methods

```
+[VTLowPowerModeMonitor sharedInstance];
```

## Instance methods

```
-[VTLowPowerModeMonitor init];
-[VTLowPowerModeMonitor _stopMonitoring];
-[VTLowPowerModeMonitor _startMonitoringWithQueue:];
-[VTLowPowerModeMonitor powerMode];
-[VTLowPowerModeMonitor _checkPowerMode];
-[VTLowPowerModeMonitor _didReceiveLowPowerModeChanged];
-[VTLowPowerModeMonitor _didReceiveLowPowerModeChangedInQueue:];
-[VTLowPowerModeMonitor _notifyObserver:withPowerMode:];
-[VTLowPowerModeMonitor isLowPowerMode];
```
