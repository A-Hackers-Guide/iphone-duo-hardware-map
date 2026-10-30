# `ULEnvironment`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 21 properties, 43 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"ULDataProtectionMonitor" _dataProtectionMonitor;
@"ULAirplaneModeMonitor" _airplaneModeMonitor;
@"ULBatteryModeMonitor" _batteryModeMonitor;
@"ULBluetoothMonitor" _bluetoothMonitor;
@"ULRapportMonitor" _rapportMonitor;
@"ULDisplayMonitor" _displayMonitor;
@"ULDisplayMonitor_OSX" _displayMonitor_OSX;
@"ULInternalNotifyMonitor" _internalNotifyMonitor;
@"ULBGSystemTaskManager" _backgroundSystemTaskManager;
@"ULDiagnostics" _diagnostics;
@"ULPrivacyMonitor" _privacyMonitor;
@"ULBuddyMonitor" _buddyMonitor;
@"ULOdometryMonitor" _odometryMonitor;
@"ULAltitudeMonitor" _altitudeMonitor;
@"ULPeripheralOdometryMonitor" _peripheralOdometryMonitor;
@"ULElevationRoutineBridgeInterface" _elevationRoutineBridge;
@"_TtC19MicroLocationDaemon34ULBiomeEventStreamCarPlayConnected" _biomeEventStreamCarPlayConnected;
@"_TtC19MicroLocationDaemon34ULBiomeEventStreamLocationSemantic" _biomeEventStreamLocationSemantic;
@"ULSleepWakeMonitor" _sleepWakeMonitor;
@"ULDarwinNotificationHelper" _notificationHelper;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"ULDataProtectionMonitor",&,N,V_dataProtectionMonitor) dataProtectionMonitor;
@property (T@"ULAirplaneModeMonitor",&,N,V_airplaneModeMonitor) airplaneModeMonitor;
@property (T@"ULBatteryModeMonitor",&,N,V_batteryModeMonitor) batteryModeMonitor;
@property (T@"ULBluetoothMonitor",&,N,V_bluetoothMonitor) bluetoothMonitor;
@property (T@"ULRapportMonitor",&,N,V_rapportMonitor) rapportMonitor;
@property (T@"ULDisplayMonitor",&,N,V_displayMonitor) displayMonitor;
@property (T@"ULDisplayMonitor_OSX",&,N,V_displayMonitor_OSX) displayMonitor_OSX;
@property (T@"ULInternalNotifyMonitor",&,N,V_internalNotifyMonitor) internalNotifyMonitor;
@property (T@"ULBGSystemTaskManager",&,N,V_backgroundSystemTaskManager) backgroundSystemTaskManager;
@property (T@"ULDiagnostics",&,N,V_diagnostics) diagnostics;
@property (T@"ULPrivacyMonitor",&,N,V_privacyMonitor) privacyMonitor;
@property (T@"ULBuddyMonitor",&,N,V_buddyMonitor) buddyMonitor;
@property (T@"ULOdometryMonitor",&,N,V_odometryMonitor) odometryMonitor;
@property (T@"ULPeripheralOdometryMonitor",&,N,V_peripheralOdometryMonitor) peripheralOdometryMonitor;
@property (T@"ULElevationRoutineBridgeInterface",&,N,V_elevationRoutineBridge) elevationRoutineBridge;
@property (T@"ULAltitudeMonitor",&,N,V_altitudeMonitor) altitudeMonitor;
@property (T@"_TtC19MicroLocationDaemon34ULBiomeEventStreamCarPlayConnected",&,N,V_biomeEventStreamCarPlayConnected) biomeEventStreamCarPlayConnected;
@property (T@"_TtC19MicroLocationDaemon34ULBiomeEventStreamLocationSemantic",&,N,V_biomeEventStreamLocationSemantic) biomeEventStreamLocationSemantic;
@property (T@"ULSleepWakeMonitor",&,N,V_sleepWakeMonitor) sleepWakeMonitor;
@property (T@"ULDarwinNotificationHelper",&,N,V_notificationHelper) notificationHelper;
```

## Class methods

```
+[ULEnvironment standardEnvironment];
```

## Instance methods

```
-[ULEnvironment notificationHelper];
-[ULEnvironment setDiagnostics:];
-[ULEnvironment setNotificationHelper:];
-[ULEnvironment setPrivacyMonitor:];
-[ULEnvironment setBiomeEventStreamCarPlayConnected:];
-[ULEnvironment setBiomeEventStreamLocationSemantic:];
-[ULEnvironment dataProtectionMonitor];
-[ULEnvironment diagnostics];
-[ULEnvironment setBuddyMonitor:];
-[ULEnvironment setInternalNotifyMonitor:];
-[ULEnvironment setSleepWakeMonitor:];
-[ULEnvironment init];
-[ULEnvironment setDataProtectionMonitor:];
-[ULEnvironment setRapportMonitor:];
-[ULEnvironment elevationRoutineBridge];
-[ULEnvironment setOdometryMonitor:];
-[ULEnvironment setElevationRoutineBridge:];
-[ULEnvironment queue];
-[ULEnvironment privacyMonitor];
-[ULEnvironment sleepWakeMonitor];
-[ULEnvironment internalNotifyMonitor];
-[ULEnvironment buddyMonitor];
-[ULEnvironment backgroundSystemTaskManager];
-[ULEnvironment bluetoothMonitor];
-[ULEnvironment peripheralOdometryMonitor];
-[ULEnvironment setDisplayMonitor:];
-[ULEnvironment setAirplaneModeMonitor:];
-[ULEnvironment setAltitudeMonitor:];
-[ULEnvironment airplaneModeMonitor];
-[ULEnvironment biomeEventStreamLocationSemantic];
-[ULEnvironment altitudeMonitor];
-[ULEnvironment displayMonitor];
-[ULEnvironment batteryModeMonitor];
-[ULEnvironment setBatteryModeMonitor:];
-[ULEnvironment displayMonitor_OSX];
-[ULEnvironment setBluetoothMonitor:];
-[ULEnvironment setBackgroundSystemTaskManager:];
-[ULEnvironment biomeEventStreamCarPlayConnected];
-[ULEnvironment setPeripheralOdometryMonitor:];
-[ULEnvironment setDisplayMonitor_OSX:];
-[ULEnvironment rapportMonitor];
-[ULEnvironment setQueue:];
-[ULEnvironment odometryMonitor];
```
