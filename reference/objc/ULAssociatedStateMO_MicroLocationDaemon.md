# `ULAssociatedStateMO`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 7 properties, 1 instance methods, 2 class methods

## Properties

```
@property (Ti,D,N) band;
@property (Ti,D,N) channel;
@property (TB,D,N) isAssociated;
@property (T@"ULLoiMO",&,D,N) loi;
@property (T@"NSString",&,D,N) macAddress;
@property (Td,D,N) timestamp;
@property (T@"NSString",&,D,N) loiId_deprecated;
```

## Class methods

```
+[ULAssociatedStateMO fetchRequest];
+[ULAssociatedStateMO createFromDO:withLoiMO:inManagedObjectContext:];
```

## Instance methods

```
-[ULAssociatedStateMO convertToDO];
```
