# `ULLabelStore`

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
+[ULLabelStore MOClass];
+[ULLabelStore defaultSortProperty];
+[ULLabelStore maxEntriesInTable];
```

## Instance methods

```
-[ULLabelStore fetchAllRecordsWithLimit:];
-[ULLabelStore clearAllLabelsForContextLayer:];
-[ULLabelStore countAnchorsForLoiGroupId:contextLayer:deviceClass:fromTimestamp:];
-[ULLabelStore countHomeKitAnchorsForLoiGroupId:entityType:fromTimestamp:];
-[ULLabelStore countLabelsForContextLayer:];
-[ULLabelStore countLabelsForLoiGroupId:deviceClass:];
-[ULLabelStore deleteOrphanRecords];
-[ULLabelStore deleteSimilarityListAnchorsOlderThan:orNewerThan:];
-[ULLabelStore fetchAllAnchorsAndObjectIDsASCWithLOIGroupUUID:];
-[ULLabelStore fetchAllAnchorsAndObjectIDsASCWithLOIGroupUUID:deviceClass:];
-[ULLabelStore fetchAnchorAndObjectIDWithUUID:deviceClass:];
-[ULLabelStore fetchAnchorsASCWithLOIGroupUUID:deviceClass:startDate:endDate:];
-[ULLabelStore fetchAnchorsWithLOIGroupUUID:andContextLayers:limit:ascending:];
-[ULLabelStore fetchDistinctContextLayers];
-[ULLabelStore insertDataObjectAndReturnObjectID:atLoiUUID:];
-[ULLabelStore insertDataObjectAndReturnObjectID:forScanningEventUUID:andServiceUUID:];
-[ULLabelStore insertDataObjects:atLoiUUID:];
-[ULLabelStore insertDataObjects:forScanningEventUUID:andServiceUUID:];
-[ULLabelStore oldestHomeKitAnchorTimestampForLoiGroupId:];
-[ULLabelStore updateAnchorsWithScanEvent:scanEventUUID:maxTimeDifference:];
-[ULLabelStore updateDataOfAnchor:];
```
