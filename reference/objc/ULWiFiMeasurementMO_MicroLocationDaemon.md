# `ULWiFiMeasurementMO`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 7 properties, 1 instance methods, 2 class methods

## Properties

```
@property (Ts,D,N) channel;
@property (Ti,D,N) flags;
@property (Ti,D,N) rssi;
@property (Tq,D,N) sourceBSSID;
@property (Td,D,N) timestamp;
@property (Ts,D,N) band;
@property (T@"ULScanningEventMO",&,D,N) scanningEvent;
```

## Class methods

```
+[ULWiFiMeasurementMO fetchRequest];
+[ULWiFiMeasurementMO createFromDO:withScanningEventMO:inManagedObjectContext:];
```

## Instance methods

```
-[ULWiFiMeasurementMO convertToDO];
```
