# `ULDataProtectionMonitor`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULEventMonitor`
- 2 instance variables, 2 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _dataAvailable;
@"ULDarwinNotificationHelper" _notificationHelper;
```

## Properties

```
@property (T@"ULDarwinNotificationHelper",&,N,V_notificationHelper) notificationHelper;
@property (TB,N,V_dataAvailable) dataAvailable;
```

## Instance methods

```
-[ULDataProtectionMonitor notificationHelper];
-[ULDataProtectionMonitor stopMonitoring:];
-[ULDataProtectionMonitor setNotificationHelper:];
-[ULDataProtectionMonitor init];
-[ULDataProtectionMonitor latestEventAfterAddingObserverForEventName:];
-[ULDataProtectionMonitor isDataAvailable];
-[ULDataProtectionMonitor startMonitoring:];
-[ULDataProtectionMonitor dataAvailable];
-[ULDataProtectionMonitor _checkDataAvailable];
-[ULDataProtectionMonitor _checkHasContentProtection];
-[ULDataProtectionMonitor _handleKeyBagLockStatusChangeNotification];
-[ULDataProtectionMonitor initWithNotificationHelper:];
-[ULDataProtectionMonitor setDataAvailable:];
```
