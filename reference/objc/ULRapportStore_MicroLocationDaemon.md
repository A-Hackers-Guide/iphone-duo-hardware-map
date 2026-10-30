# `ULRapportStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- Protocols: `ULStoreProtocol`
- 0 instance variables, 4 properties, 5 instance methods, 3 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULRapportStore MOClass];
+[ULRapportStore defaultSortProperty];
+[ULRapportStore maxEntriesInTable];
```

## Instance methods

```
-[ULRapportStore fetchAllRecordsWithLimit:];
-[ULRapportStore _fetchRapportsByAndPredicates:sortDescriptors:andLimit:];
-[ULRapportStore deleteOrphanRecords];
-[ULRapportStore fetchRapportEntriesAtLoiFromTime:toTime:loiGroupId:];
-[ULRapportStore insertDataObjects:atLoiUUID:];
```
