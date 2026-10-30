# `ULServiceMO`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 8 properties, 1 instance methods, 2 class methods

## Properties

```
@property (T@"NSString",&,D,N) clientId;
@property (Td,D,N) lastActiveTimestamp;
@property (Tq,D,N) locationTypes;
@property (Ti,D,N) serviceType;
@property (T@"NSString",&,D,N) serviceUUID;
@property (T@"NSSet",&,D,N) customLOIs;
@property (T@"NSSet",&,D,N) labels;
@property (T@"NSSet",&,D,N) models;
```

## Class methods

```
+[ULServiceMO fetchRequest];
+[ULServiceMO createFromDO:inManagedObjectContext:];
```

## Instance methods

```
-[ULServiceMO convertToDO];
```
