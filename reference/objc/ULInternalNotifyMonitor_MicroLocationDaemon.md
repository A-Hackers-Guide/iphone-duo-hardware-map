# `ULInternalNotifyMonitor`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULEventMonitor`
- 1 instance variables, 1 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"ULDarwinNotificationHelper" _notificationHelper;
```

## Properties

```
@property (T@"ULDarwinNotificationHelper",&,N,V_notificationHelper) notificationHelper;
```

## Instance methods

```
-[ULInternalNotifyMonitor notificationHelper];
-[ULInternalNotifyMonitor stopMonitoring:];
-[ULInternalNotifyMonitor setNotificationHelper:];
-[ULInternalNotifyMonitor init];
-[ULInternalNotifyMonitor startMonitoring:];
-[ULInternalNotifyMonitor _handleNotificationForEventName:];
-[ULInternalNotifyMonitor _identifierFromEventName:];
-[ULInternalNotifyMonitor _startMonitoringForEventName:identifier:];
-[ULInternalNotifyMonitor _stopMonitoringForEventName:identifier:];
-[ULInternalNotifyMonitor initWithNotificationHelper:];
```
