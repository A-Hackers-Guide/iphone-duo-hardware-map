# `ULBatteryModeMonitor`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULEventMonitor`
- 3 instance variables, 3 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _unlimitedPower;
B _lowPowerMode;
@"ULDarwinNotificationHelper" _notificationHelper;
```

## Properties

```
@property (T@"ULDarwinNotificationHelper",&,N,V_notificationHelper) notificationHelper;
@property (TB,N,V_unlimitedPower) unlimitedPower;
@property (TB,N,V_lowPowerMode) lowPowerMode;
```

## Instance methods

```
-[ULBatteryModeMonitor notificationHelper];
-[ULBatteryModeMonitor stopMonitoring:];
-[ULBatteryModeMonitor setNotificationHelper:];
-[ULBatteryModeMonitor init];
-[ULBatteryModeMonitor latestEventAfterAddingObserverForEventName:];
-[ULBatteryModeMonitor setLowPowerMode:];
-[ULBatteryModeMonitor startMonitoring:];
-[ULBatteryModeMonitor lowPowerMode];
-[ULBatteryModeMonitor _startMonitoringForLowPowerMode];
-[ULBatteryModeMonitor _checkLowPowerMode];
-[ULBatteryModeMonitor _checkUnlimitedPower];
-[ULBatteryModeMonitor _handleIOPSNotifyAdapterChangeNotification];
-[ULBatteryModeMonitor _handleNSProcessInfoPowerStateDidChangeNotification:];
-[ULBatteryModeMonitor _startMonitoringForUnlimitedPower];
-[ULBatteryModeMonitor _stopMonitoringForLowPowerMode];
-[ULBatteryModeMonitor _stopMonitoringForUnlimitedPower];
-[ULBatteryModeMonitor initWithNotificationHelper:];
-[ULBatteryModeMonitor setUnlimitedPower:];
-[ULBatteryModeMonitor unlimitedPower];
```
