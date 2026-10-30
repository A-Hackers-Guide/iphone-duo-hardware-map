# `ULModelMO`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 10 properties, 1 instance methods, 2 class methods

## Properties

```
@property (T@"NSString",&,D,N) modelUUID;
@property (Td,D,N) generationTimestamp;
@property (T@"NSData",&,D,N) model;
@property (Ti,D,N) modelType;
@property (T@"NSData",&,D,N) rawModelData;
@property (T@"ULLoiMO",&,D,N) loi;
@property (T@"ULServiceMO",&,D,N) service;
@property (T@"NSSet",&,D,N) mapLabels;
@property (T@"NSString",&,D,N) loiId_deprecated;
@property (T@"NSString",&,D,N) serviceUUID_deprecated;
```

## Class methods

```
+[ULModelMO fetchRequest];
+[ULModelMO createFromDO:withServiceMO:loiMO:inManagedObjectContext:];
```

## Instance methods

```
-[ULModelMO convertToDO];
```
