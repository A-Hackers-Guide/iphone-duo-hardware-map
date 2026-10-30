# `ULPeripheralOdometryMO`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 10 properties, 1 instance methods, 2 class methods

## Properties

```
@property (Td,D,N) timestamp;
@property (Tf,D,N) deltaPositionX;
@property (Tf,D,N) deltaPositionY;
@property (Tf,D,N) deltaPositionZ;
@property (Tf,D,N) attitudeQuaternionX;
@property (Tf,D,N) attitudeQuaternionY;
@property (Tf,D,N) attitudeQuaternionZ;
@property (Tf,D,N) attitudeQuaternionW;
@property (TI,D,N) sensorID;
@property (T@"ULLoiMO",&,D,N) loi;
```

## Class methods

```
+[ULPeripheralOdometryMO fetchRequest];
+[ULPeripheralOdometryMO createFromDO:loiMO:inManagedObjectContext:];
```

## Instance methods

```
-[ULPeripheralOdometryMO convertToDO];
```
