# `ULRecordingEventStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- Protocols: `ULStoreProtocol`
- 0 instance variables, 4 properties, 23 instance methods, 3 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULRecordingEventStore MOClass];
+[ULRecordingEventStore defaultSortProperty];
+[ULRecordingEventStore maxEntriesInTable];
```

## Instance methods

```
-[ULRecordingEventStore fetchAllRecordsWithLimit:];
-[ULRecordingEventStore insertDataObjects:];
-[ULRecordingEventStore _fetchRecordingEventTriggers:atLoiGroupId:fromTime:toTime:withLimit:];
-[ULRecordingEventStore _fetchRecordingEventsByAndPredicates:sortDescriptors:andLimit:];
-[ULRecordingEventStore batchTransferRecordingEventsForRecordingUUIDs:withEventTypes:batchSize:andLimit:intoTargetStore:];
-[ULRecordingEventStore batchTransferRecordsUsingBatchSize:andLimit:intoTargetStore:];
-[ULRecordingEventStore countRecordingEventsForLoiGroupId:];
-[ULRecordingEventStore countRecordingEventsFromTime:toTime:atLoiGroupId:];
-[ULRecordingEventStore deleteRecordingEventsFromRecordingUUIDs:];
-[ULRecordingEventStore fetchDistinctRecordingEventsFromTime:toTime:atLoiGroupId:withLimit:];
-[ULRecordingEventStore fetchMostRecentRecordingForLoiGroupId:];
-[ULRecordingEventStore fetchRecordingEventTriggersForLearningMeasurements:];
-[ULRecordingEventStore fetchRecordingEventTriggersForLearningMeasurements:atLoiGroupId:];
-[ULRecordingEventStore fetchRecordingEventsForRecordingUUIDs:];
-[ULRecordingEventStore fetchRecordingEventsFromTriggerUUIDs:];
-[ULRecordingEventStore fetchRecordingEventsWithScanMeasurements:fromTime:toTime:withLimit:];
-[ULRecordingEventStore getDistinctRecordingUUIDsWithLimit:];
-[ULRecordingEventStore getOldestRecordingTimestamp];
-[ULRecordingEventStore getRecordingUUIDsForLocalizationActionsFromTime:toTime:];
-[ULRecordingEventStore getRecordingUUIDsForRecordingEventActionsAtLoiGroupId:fromTime:toTime:withLimit:];
-[ULRecordingEventStore getRecordingUUIDsOlderThan:orNewerThan:];
-[ULRecordingEventStore getTriggerUUIDsForLoiGroupId:];
-[ULRecordingEventStore selectAllRecordingLOITypesFromTime:andLimit:];
```
