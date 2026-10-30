# `ULScanningEventStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- Protocols: `ULStoreProtocol`
- 0 instance variables, 4 properties, 21 instance methods, 3 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULScanningEventStore MOClass];
+[ULScanningEventStore defaultSortProperty];
+[ULScanningEventStore maxEntriesInTable];
```

## Instance methods

```
-[ULScanningEventStore fetchAllRecordsWithLimit:];
-[ULScanningEventStore getOldestScanTimeForLoiGroupId:];
-[ULScanningEventStore _fetchScanningEventsByAndPredicates:sortDescriptors:andLimit:];
-[ULScanningEventStore addPhotoFeatures:forScanningEvent:];
-[ULScanningEventStore countScanningEventsForLoiGroupId:];
-[ULScanningEventStore countScanningEventsFromTime:toTime:atLoiGroupId:];
-[ULScanningEventStore deleteOldestScanEventsIfBLEMeasurementsExceedLimit];
-[ULScanningEventStore deleteOrphanRecords];
-[ULScanningEventStore fetchDistinctScanningEventsUUIDsFromTime:toTime:atLoiGroupId:withLimit:];
-[ULScanningEventStore fetchDistinctScanningEventsUUIDsFromTime:toTime:withScanType:Limit:];
-[ULScanningEventStore fetchScanningEventManagedObjectWithUUID:withManagedObjectContext:];
-[ULScanningEventStore fetchScanningEventUUIDsWithLOIGroupUUID:scanType:motionState:scansWithPhotoFeatures:startDate:endDate:scanResult:onlyScansWithAnchors:fetchLimit:newest:ascending:];
-[ULScanningEventStore fetchScanningEventsForUUIDs:];
-[ULScanningEventStore fetchScanningEventsWithLOIGroupUUID:scanType:startDate:endDate:fetchLimit:ascending:];
-[ULScanningEventStore fetchScanningEventsWithLabelObjectIDsForUUIDs:];
-[ULScanningEventStore getMostRecentScanTimeForLoiGroupId:];
-[ULScanningEventStore getOldestScanTimestamp];
-[ULScanningEventStore getScanningEventUUIDsAtLoiGroupId:withScanType:startDate:endDate:onlyScansWithAnchors:Limit:];
-[ULScanningEventStore insertDataObjects:atLoiUUID:];
-[ULScanningEventStore oneByOneFetchScanningEventsWithLOIGroupUUID:scanType:motionState:scansWithPhotoFeatures:startDate:endDate:scanResult:onlyScansWithAnchors:fetchLimit:newest:ascending:];
-[ULScanningEventStore selectAllScanningLOITypesFromTime:withLimit:];
```
