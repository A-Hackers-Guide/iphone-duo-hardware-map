# `ULMapLabelStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- Protocols: `ULStoreProtocol`
- 0 instance variables, 4 properties, 19 instance methods, 3 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULMapLabelStore MOClass];
+[ULMapLabelStore defaultSortProperty];
+[ULMapLabelStore maxEntriesInTable];
```

## Instance methods

```
-[ULMapLabelStore fetchAllRecordsWithLimit:];
-[ULMapLabelStore _createLabelMOFromDO:forScanningEventUUID:andServiceUUID:];
-[ULMapLabelStore _createMapLabelMOFromDO:withLabelMO:modelMO:];
-[ULMapLabelStore _fetchLabelMOWithObjectID:withManagedObjectContext:];
-[ULMapLabelStore _fetchMapLabelByAndPredicates:sortDescriptors:andLimit:];
-[ULMapLabelStore _fetchRelatedModelMOWithUUID:];
-[ULMapLabelStore _insertMapLabelMOFromDO:withLabelMO:];
-[ULMapLabelStore deleteMapLabelsForModel:withTimestampAfter:];
-[ULMapLabelStore deleteOrphanRecords];
-[ULMapLabelStore fetchInternalMapLabelsForModel:limit:ascending:];
-[ULMapLabelStore fetchMapLabelsForModel:andContextLayers:limit:ascending:];
-[ULMapLabelStore fetchMapLabelsForModel:forService:limit:ascending:];
-[ULMapLabelStore fetchMapLabelsForModel:limit:ascending:];
-[ULMapLabelStore insertDataObjects:forLabelObjectID:andModelUUID:];
-[ULMapLabelStore insertLabelDOAndMapLabelDO:forScanningEventUUID:];
-[ULMapLabelStore insertMapLabelDO:atLoiUUID:];
-[ULMapLabelStore insertMapLabelsWithRelatedLabelsObjectIDs:];
-[ULMapLabelStore removeLabelsUpToTimestamp:forContextLayer:loiGroupUUID:];
-[ULMapLabelStore removeLabelsWithUUIDStrings:];
```
