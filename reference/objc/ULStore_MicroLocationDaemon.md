# `ULStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 34 instance methods, 4 class methods

## Instance variables

```
@"NSManagedObjectContext" _managedObjectContext;
^{ULDatabaseStoreInterface=^^?} _dbStore;
```

## Properties

```
@property (T^{ULDatabaseStoreInterface=^^?},N,V_dbStore) dbStore;
@property (T@"NSManagedObjectContext",&,N,V_managedObjectContext) managedObjectContext;
```

## Class methods

```
+[ULStore bufferMaxSize];
+[ULStore MOClass];
+[ULStore defaultSortProperty];
+[ULStore maxEntriesInTable];
```

## Instance methods

```
-[ULStore managedObjectContext];
-[ULStore setManagedObjectContext:];
-[ULStore dealloc];
-[ULStore count];
-[ULStore batchDeleteObjectsWithEntityName:byAndPredicates:sortDescriptors:andLimit:];
-[ULStore batchUpdateObjectsWithEntityName:predicate:propertiesToUpdate:];
-[ULStore commitChangesToStore];
-[ULStore fetchManagedObjectsWithEntityName:byAndPredicates:sortDescriptors:andLimit:];
-[ULStore dbStore];
-[ULStore deleteOldestRecordsForEntityName:sortProperty:maxRecordsToKeep:];
-[ULStore _batchFetchManagedObjectsWithEntityName:byAndPredicates:sortDescriptors:batchSize:limit:error:];
-[ULStore _efficientlyEnumerateManagedObjectsInFetchRequest:usingManagedObjectContext:andApplyBlock:];
-[ULStore _handleDatabaseError:];
-[ULStore _insertFetchedBatchedObjects:usingBatchSize:];
-[ULStore batchTransferManagedObjectsWithEntityName:byAndPredicates:sortDescriptors:batchSize:limit:intoTargetStore:];
-[ULStore countAllRecordsForEntityName:];
-[ULStore countManagedObjectsWithEntityName:byAndPredicates:sortDescriptors:andLimit:];
-[ULStore deleteAllRecords];
-[ULStore deleteAllRecordsForEntityName:];
-[ULStore deleteOldestRecordsIfFull];
-[ULStore deleteRecordsForEntityName:sortProperty:olderThan:orNewerThan:];
-[ULStore deleteRecordsOlderThan:orNewerThan:];
-[ULStore efficientlyFetchManagedObjectsWithEntityName:byAndPredicates:sortDescriptors:andLimit:fetchBatchSize:andApplyBlock:];
-[ULStore fetchManagedObjectsForEntityName:propertiesToFetch:propertiesToGroupBy:byAndPredicates:sortDescriptors:andLimit:];
-[ULStore fetchManagedObjectsWithEntityName:byAndPredicates:sortDescriptors:andLimit:returnObjectsAsFaults:withManagedObjectContext:];
-[ULStore fetchManagedObjectsWithEntityName:byAndPredicates:sortDescriptors:andLimit:withManagedObjectContext:];
-[ULStore fetchPropertiesForEntityName:propertiesToFetch:propertiesToGroupBy:distinctResults:byAndPredicates:sortDescriptors:andLimit:resetContext:];
-[ULStore fetchPropertyForEntityName:propertyToFetch:distinctResults:byAndPredicates:sortDescriptors:andLimit:];
-[ULStore flushStoreBuffer];
-[ULStore initWithDbStore:];
-[ULStore insertDataObjectsBuffered:atLoiUUID:];
-[ULStore isBufferingEnabled];
-[ULStore resetMOC];
-[ULStore setDbStore:];
```
