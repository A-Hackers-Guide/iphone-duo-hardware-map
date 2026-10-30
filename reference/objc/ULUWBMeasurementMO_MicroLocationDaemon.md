# `ULUWBMeasurementMO`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 5 properties, 1 instance methods, 2 class methods

## Properties

```
@property (Ts,D,N) deviceModel;
@property (Tf,D,N) range;
@property (T@"NSString",&,D,N) sourceIdsUUID;
@property (Td,D,N) timestamp;
@property (T@"ULScanningEventMO",&,D,N) scanningEvent;
```

## Class methods

```
+[ULUWBMeasurementMO fetchRequest];
+[ULUWBMeasurementMO createFromDO:withScanningEventMO:inManagedObjectContext:];
```

## Instance methods

```
-[ULUWBMeasurementMO convertToDO];
```
