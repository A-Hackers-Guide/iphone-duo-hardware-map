# `ULModelStore`

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
+[ULModelStore MOClass];
+[ULModelStore defaultSortProperty];
+[ULModelStore maxEntriesInTable];
```

## Instance methods

```
-[ULModelStore fetchAllRecordsWithLimit:];
-[ULModelStore countModelsOfType:atLoiGroupId:];
-[ULModelStore _fetchModelsByAndPredicates:sortDescriptors:andLimit:];
-[ULModelStore deleteAllModelsOfType:atLoiGroupId:];
-[ULModelStore deleteModelsForService:];
-[ULModelStore deleteOldestModelsOfType:atLoiGroupId:limit:];
-[ULModelStore deleteOrphanRecords];
-[ULModelStore deleteOutdatedModelsOfType:forServiceUUID:atLoiGroupId:modelsToKeep:];
-[ULModelStore fetchDistinctServiceUUIDsForModelType:atLoiGroupId:];
-[ULModelStore fetchModelManagedObjectWithUUID:withManagedObjectContext:];
-[ULModelStore fetchModelsAtLoiGroupId:andLimit:];
-[ULModelStore fetchMostRecentMagicalMomentsModelAtLoiGroupId:];
-[ULModelStore fetchMostRecentModelForServiceUuid:atLoiGroupId:];
-[ULModelStore fetchMostRecentModelOfModelType:ForClient:atLoiGroupId:];
-[ULModelStore fetchMostRecentModelOfModelType:ForService:atLoiGroupId:];
-[ULModelStore fetchMostRecentModelOfModelType:atLoiGroupId:];
-[ULModelStore fetchMostRecentModels];
-[ULModelStore hasVisualMappingKitModel];
-[ULModelStore insertDataObjects:forServiceUUID:atLoiUUID:];
```
