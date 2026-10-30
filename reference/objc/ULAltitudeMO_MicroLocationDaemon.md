# `ULAltitudeMO`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 5 properties, 1 instance methods, 2 class methods

## Properties

```
@property (Tf,D,N) altitudeMeters;
@property (Td,D,N) timestamp;
@property (T@"NSUUID",&,D,N) altitudeSessionUUID;
@property (Ts,D,N) altitudeStatusInfo;
@property (T@"ULLoiMO",&,D,N) loi;
```

## Class methods

```
+[ULAltitudeMO fetchRequest];
+[ULAltitudeMO createFromDO:loiMO:inManagedObjectContext:];
```

## Instance methods

```
-[ULAltitudeMO convertToDO];
```
