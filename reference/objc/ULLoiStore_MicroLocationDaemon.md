# `ULLoiStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- Protocols: `ULStoreProtocol`
- 0 instance variables, 4 properties, 20 instance methods, 3 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULLoiStore MOClass];
+[ULLoiStore defaultSortProperty];
+[ULLoiStore maxEntriesInTable];
```

## Instance methods

```
-[ULLoiStore fetchAllRecordsWithLimit:];
-[ULLoiStore insertDataObjects:];
-[ULLoiStore clear:];
-[ULLoiStore updateCategory:isSpareCategory:];
-[ULLoiStore _fetchLoisByAndPredicates:sortDescriptors:andLimit:];
-[ULLoiStore batchTransferRecordsUsingBatchSize:andLimit:intoTargetStore:];
-[ULLoiStore countDistinctLoiGroups];
-[ULLoiStore countDistinctLoiTypes:];
-[ULLoiStore fetchAllDistinctLoiGroups];
-[ULLoiStore fetchLoiIdEntriesInLoiGroupId:];
-[ULLoiStore fetchLoiIdEntriesforLoiGroupIds:withLimit:];
-[ULLoiStore fetchLoiManagedObjectWithUUID:withManagedObjectContext:];
-[ULLoiStore getDistinctHomeLoiGroupIdsWithLimit:];
-[ULLoiStore getLoiGroupIdForLoi:];
-[ULLoiStore getLoiGroupIdToCategoryMap];
-[ULLoiStore getLoiGroupIdsForLois:];
-[ULLoiStore getLoiIdsInLoiGroupId:];
-[ULLoiStore getLoiTypeForLoi:];
-[ULLoiStore setCategoryForLoiGroupId:category:isSpareCategory:];
-[ULLoiStore updateLoiIds:withLoiGroupId:andLoiType:];
```
