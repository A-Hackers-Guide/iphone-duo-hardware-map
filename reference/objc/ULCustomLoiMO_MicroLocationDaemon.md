# `ULCustomLoiMO`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 5 properties, 1 instance methods, 2 class methods

## Properties

```
@property (Td,D,N) lastSeenTimeStamp;
@property (T@"ULLoiMO",&,D,N) loi;
@property (T@"ULServiceMO",&,D,N) service;
@property (T@"NSString",&,D,N) loiId_deprecated;
@property (T@"NSString",&,D,N) serviceId_deprecated;
```

## Class methods

```
+[ULCustomLoiMO fetchRequest];
+[ULCustomLoiMO createFromDO:withServiceMO:loiMO:inManagedObjectContext:];
```

## Instance methods

```
-[ULCustomLoiMO convertToDO];
```
