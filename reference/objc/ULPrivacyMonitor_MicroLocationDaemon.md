# `ULPrivacyMonitor`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULEventMonitor`
- Protocols: `CLLocationManagerDelegate`
- 3 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _locationServicesEnabled;
@"CLLocationManager" _locationManager;
@"ULDarwinNotificationHelper" _notificationHelper;
```

## Properties

```
@property (T@"CLLocationManager",&,N,V_locationManager) locationManager;
@property (T@"ULDarwinNotificationHelper",&,N,V_notificationHelper) notificationHelper;
@property (TB,N,V_locationServicesEnabled) locationServicesEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ULPrivacyMonitor notificationHelper];
-[ULPrivacyMonitor setLocationManager:];
-[ULPrivacyMonitor stopMonitoring:];
-[ULPrivacyMonitor setNotificationHelper:];
-[ULPrivacyMonitor locationManager];
-[ULPrivacyMonitor locationManager:didFailWithError:];
-[ULPrivacyMonitor init];
-[ULPrivacyMonitor setLocationServicesEnabled:];
-[ULPrivacyMonitor latestEventAfterAddingObserverForEventName:];
-[ULPrivacyMonitor startMonitoring:];
-[ULPrivacyMonitor locationManagerDidChangeAuthorization:];
-[ULPrivacyMonitor locationServicesEnabled];
-[ULPrivacyMonitor _checkLocationServicesEnabledForAuthorizationStatus:];
-[ULPrivacyMonitor _locationAuthorizationStatusToString:];
-[ULPrivacyMonitor initWithNotificationHelper:];
```
