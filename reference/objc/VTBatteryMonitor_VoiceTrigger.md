# `VTBatteryMonitor`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTEventMonitor`
- 2 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
i _notifyToken;
C _batteryState;
```

## Class methods

```
+[VTBatteryMonitor sharedInstance];
```

## Instance methods

```
-[VTBatteryMonitor init];
-[VTBatteryMonitor _stopMonitoring];
-[VTBatteryMonitor _startMonitoringWithQueue:];
-[VTBatteryMonitor batteryState];
-[VTBatteryMonitor _checkBatteryState];
-[VTBatteryMonitor _didReceiveBatteryStatusChanged:];
-[VTBatteryMonitor _didReceiveBatteryStatusChangedInQueue:];
-[VTBatteryMonitor _notifyObserver:withBatteryState:];
```
