# `ULScanningEventMO`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 17 properties, 1 instance methods, 2 class methods

## Properties

```
@property (TB,D,N) bleSuspended;
@property (Ts,D,N) motionState;
@property (T@"NSString",&,D,N) scanEventUUID;
@property (Ts,D,N) scanResult;
@property (Ts,D,N) scanType;
@property (Td,D,N) timestamp;
@property (TB,D,N) uwbSuspended;
@property (TB,D,N) wifiDisabled;
@property (T@"NSNumber",&,D,N) wifiAssociationBSSID;
@property (T@"NSNumber",&,D,N) wifiAssociationRSSI;
@property (T@"NSSet",&,D,N) bleMeasurements;
@property (T@"NSSet",&,D,N) labels;
@property (T@"ULLoiMO",&,D,N) loi;
@property (T@"NSSet",&,D,N) uwbMeasurements;
@property (T@"NSSet",&,D,N) wifiMeasurements;
@property (T@"NSSet",&,D,N) photoFeatures;
@property (T@"ULMagnetometerMO",&,D,N) magnetometer;
```

## Class methods

```
+[ULScanningEventMO fetchRequest];
+[ULScanningEventMO createFromDO:withLoiMO:inManagedObjectContext:];
```

## Instance methods

```
-[ULScanningEventMO convertToDO];
```
