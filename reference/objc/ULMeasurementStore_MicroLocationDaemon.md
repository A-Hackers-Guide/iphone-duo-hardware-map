# `ULMeasurementStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- Protocols: `ULStoreProtocol`
- 0 instance variables, 4 properties, 11 instance methods, 3 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULMeasurementStore MOClass];
+[ULMeasurementStore defaultSortProperty];
+[ULMeasurementStore maxEntriesInTable];
```

## Instance methods

```
-[ULMeasurementStore fetchAllRecordsWithLimit:];
-[ULMeasurementStore insertDataObjects:];
-[ULMeasurementStore _fetchMeasurementEntriesByAndPredicates:sortDescriptors:andLimit:];
-[ULMeasurementStore batchTransferRecordsUsingBatchSize:andLimit:usingDistinctRecords:intoTargetStore:];
-[ULMeasurementStore deleteMeasurementsFromRecordingUUIDs:];
-[ULMeasurementStore deleteRecordsOlderThan:orNewerThan:];
-[ULMeasurementStore fetchAllLocalizingMeasurementsWithLimit:];
-[ULMeasurementStore fetchLearningMeasurementsAtLoiGroupId:fromTime:toTime:];
-[ULMeasurementStore fetchMeasurementsForRecordingUUIDs:];
-[ULMeasurementStore numLocalizationScansFromTime:toTime:];
-[ULMeasurementStore numRecordingScansFromTime:toTime:];
```
