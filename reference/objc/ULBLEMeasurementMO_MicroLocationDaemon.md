# `ULBLEMeasurementMO`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 6 properties, 1 instance methods, 2 class methods

## Properties

```
@property (Ts,D,N) bleChannel;
@property (Ts,D,N) deviceModel;
@property (Ti,D,N) rssi;
@property (T@"NSString",&,D,N) sourceIdsUUID;
@property (Td,D,N) timestamp;
@property (T@"ULScanningEventMO",&,D,N) scanningEvent;
```

## Class methods

```
+[ULBLEMeasurementMO fetchRequest];
+[ULBLEMeasurementMO createFromDO:withScanningEventMO:inManagedObjectContext:];
```

## Instance methods

```
-[ULBLEMeasurementMO convertToDO];
```
