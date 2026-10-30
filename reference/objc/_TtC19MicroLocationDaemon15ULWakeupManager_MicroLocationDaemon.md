# `_TtC19MicroLocationDaemon15ULWakeupManager`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_TtP19MicroLocationDaemon16ULWakeupManaging_`
- 12 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
MicroLocationDaemon.ULWakeupManager.WakeupState wakeupState;
DispatchQueue queue;
_$sSo18ULSleepWakeMonitorC sleepWakeMonitor;
_$sSo17ULOdometryMonitorC mainDeviceOdometryMonitor;
_$sSo27ULPeripheralOdometryMonitorC peripheralOdometryMonitor;
MicroLocationDaemon.ULWakeupManager.WakeupSensorReadiness mainDeviceReadiness;
MicroLocationDaemon.ULWakeupManager.WakeupSensorReadiness peripheralReadiness;
Swift.Bool isMonitoringMainDeviceOdometry;
Swift.Bool isMonitoringPeripheralOdometry;
(objc_protocol 0x29481c098) timerFactory;
_$sSo7ULTimerCSg catchingUpTimer;
(objc_protocol 0x29481c0a0) ? delegate;
```

## Properties

```
@property (Tq,N,R) currentState;
```

## Class methods

```
+[_TtC19MicroLocationDaemon15ULWakeupManager createWakeupManagerWithEnvironment:queue:delegate:];
```

## Instance methods

```
-[_TtC19MicroLocationDaemon15ULWakeupManager init];
-[_TtC19MicroLocationDaemon15ULWakeupManager dealloc];
-[_TtC19MicroLocationDaemon15ULWakeupManager currentState];
-[_TtC19MicroLocationDaemon15ULWakeupManager updateMainDeviceOdometryStatus:];
-[_TtC19MicroLocationDaemon15ULWakeupManager updatePeripheralStatus:];
```
