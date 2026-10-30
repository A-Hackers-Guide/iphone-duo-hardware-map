# `ULAssociatedStateStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- Protocols: `ULStoreProtocol`
- 0 instance variables, 4 properties, 6 instance methods, 3 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULAssociatedStateStore MOClass];
+[ULAssociatedStateStore defaultSortProperty];
+[ULAssociatedStateStore maxEntriesInTable];
```

## Instance methods

```
-[ULAssociatedStateStore fetchAllRecordsWithLimit:];
-[ULAssociatedStateStore _fetchAssociatedStatesByAndPredicates:sortDescriptors:andLimit:];
-[ULAssociatedStateStore deleteOrphanRecords];
-[ULAssociatedStateStore fetchAllAssociatedStateBetweenTimes:toTime:atLoiGroupId:];
-[ULAssociatedStateStore getAllDistinctAssociatedStateLoiIds];
-[ULAssociatedStateStore insertDataObjects:atLoiUUID:];
```
