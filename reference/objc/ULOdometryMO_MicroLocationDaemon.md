# `ULOdometryMO`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 9 properties, 1 instance methods, 2 class methods

## Properties

```
@property (Ts,D,N) deltaPositionX;
@property (Ts,D,N) deltaPositionY;
@property (Ts,D,N) deltaPositionZ;
@property (T@"NSNumber",&,D,N) alignmentAngleRad;
@property (T@"NSNumber",&,D,N) alignmentAngleErrorEstimateRad;
@property (Td,D,N) timestamp;
@property (T@"NSUUID",&,D,N) trajectoryUUID;
@property (T@"ULLoiMO",&,D,N) loi;
@property (Ts,D,N) odometrySourceType;
```

## Class methods

```
+[ULOdometryMO fetchRequest];
+[ULOdometryMO createFromDO:loiMO:inManagedObjectContext:];
```

## Instance methods

```
-[ULOdometryMO convertToDO];
```
