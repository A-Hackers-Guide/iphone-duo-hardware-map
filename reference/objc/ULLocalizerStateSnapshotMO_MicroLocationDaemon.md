# `ULLocalizerStateSnapshotMO`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 4 properties, 1 instance methods, 2 class methods

## Properties

```
@property (T@"NSString",&,D,N) snapshotUUID;
@property (Td,D,N) generationTimestamp;
@property (T@"NSData",&,D,N) snapshotData;
@property (T@"ULModelMO",&,D,N) model;
```

## Class methods

```
+[ULLocalizerStateSnapshotMO fetchRequest];
+[ULLocalizerStateSnapshotMO createFromDO:withModelMO:inManagedObjectContext:];
```

## Instance methods

```
-[ULLocalizerStateSnapshotMO convertToDO];
```
