# `ULVersionMigrationStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- 1 instance variables, 1 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _handledRecordingUUIDs;
```

## Properties

```
@property (T@"NSMutableSet",&,N,V_handledRecordingUUIDs) handledRecordingUUIDs;
```

## Instance methods

```
-[ULVersionMigrationStore _commitBatchForEntityName:migratingAttribute:stop:];
-[ULVersionMigrationStore _connectLabelsInBatch:withTriggerUUIDMap:andScanEventsUUIDMap:];
-[ULVersionMigrationStore _connectLabelsToScanningEvents];
-[ULVersionMigrationStore _createAnchorAppearanceMapMOFromConfigurationMO:withLOIObjectID:];
-[ULVersionMigrationStore _createBLEMeasurementFromDeprecatedMeasurement:withMeasurementProto:andRelatedScanningEventObjectID:];
-[ULVersionMigrationStore _createMeasurementFromDeprecatedMeasurement:withRelatedScanningEventObjectID:];
-[ULVersionMigrationStore _createScanningEventFromRecordingEvent:withRelatedLOIObjectID:];
-[ULVersionMigrationStore _createUWBMeasurementFromDeprecatedMeasurement:withMeasurementProto:andRelatedScanningEventObjectID:];
-[ULVersionMigrationStore _createWiFiHistogramMOFromConfigurationMO:withLOIObjectID:];
-[ULVersionMigrationStore _createWiFiMeasurementFromDeprecatedMeasurement:withMeasurementProto:andRelatedScanningEventObjectID:];
-[ULVersionMigrationStore _getConfigProtoFromConfigurationMO:];
-[ULVersionMigrationStore _getTriggerToRecordingUUIDMap];
-[ULVersionMigrationStore _getUUIDToObjectIDMapForRelatedEntityName:relatedAttribute:relatedSortAttribute:filterUUIDs:];
-[ULVersionMigrationStore _migrateAttributeToRelationshipForEntityName:deprecatedAttribute:sortAttribute:relationship:relatedEntityName:relatedAttribute:relatedSortAttribute:fetchBatchSize:];
-[ULVersionMigrationStore _migrateAttributesToRelationships];
-[ULVersionMigrationStore _migrateBatch:forDeprecatedAttribute:relationship:withRelationUUIDMap:];
-[ULVersionMigrationStore _migrateConfigurationInBatch:withLOIMap:];
-[ULVersionMigrationStore _migrateConfigurations];
-[ULVersionMigrationStore _migrateMeasurements];
-[ULVersionMigrationStore _migrateMeasurementsInBatch:withRelationUUIDMap:];
-[ULVersionMigrationStore _migrateRecordingEvents];
-[ULVersionMigrationStore _migrateRecordingEventsInBatch:withRelationUUIDMap:];
-[ULVersionMigrationStore _updateContextLayersForLabelsInBatch:];
-[ULVersionMigrationStore _updateLabelsContextLayers];
-[ULVersionMigrationStore handledRecordingUUIDs];
-[ULVersionMigrationStore initWithDbStore:];
-[ULVersionMigrationStore performVersionMigrationForModelVersion:];
-[ULVersionMigrationStore setHandledRecordingUUIDs:];
```
