# `ULPersistenceManager`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 40 instance methods, 2 class methods

## Instance variables

```
B _useWal;
@"NSURL" _modelsDirectory;
@"NSURL" _storesDirectory;
@"NSManagedObjectModel" _managedObjectModel;
@"NSPersistentStoreCoordinator" _persistentStoreCoordinator;
@"ULPersistenceStore" _persistenceStore;
@"ULDataContainer" _dataContainer;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"NSPersistentStoreCoordinator",&,N,V_persistentStoreCoordinator) persistentStoreCoordinator;
@property (T@"ULPersistenceStore",&,N,V_persistenceStore) persistenceStore;
@property (T@"NSManagedObjectModel",&,N,V_managedObjectModel) managedObjectModel;
@property (T@"ULDataContainer",&,N,V_dataContainer) dataContainer;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSURL",&,N,V_modelsDirectory) modelsDirectory;
@property (T@"NSURL",&,N,V_storesDirectory) storesDirectory;
@property (TB,N,V_useWal) useWal;
```

## Class methods

```
+[ULPersistenceManager defaultModelsDirectory];
+[ULPersistenceManager defaultLocalStoreFilename];
```

## Instance methods

```
-[ULPersistenceManager init];
-[ULPersistenceManager setManagedObjectModel:];
-[ULPersistenceManager createManagedObjectContext];
-[ULPersistenceManager queue];
-[ULPersistenceManager useWal];
-[ULPersistenceManager persistentStoreCoordinator];
-[ULPersistenceManager managedObjectModel];
-[ULPersistenceManager setQueue:];
-[ULPersistenceManager setPersistentStoreCoordinator:];
-[ULPersistenceManager handleDatabaseError:];
-[ULPersistenceManager _enableConcurrencyDebug];
-[ULPersistenceManager _getDefaultStoresDirectory];
-[ULPersistenceManager _isStoreConnected];
-[ULPersistenceManager connectToStore];
-[ULPersistenceManager disconnectFromStore];
-[ULPersistenceManager getLocalStoreURL];
-[ULPersistenceManager persistenceStore];
-[ULPersistenceManager setPersistenceStore:];
-[ULPersistenceManager storesDirectory];
-[ULPersistenceManager modelsDirectory];
-[ULPersistenceManager _isMainDatabase];
-[ULPersistenceManager _deleteDatabaseFilesAtPath:];
-[ULPersistenceManager _destroyStore];
-[ULPersistenceManager _disconnectFromStore];
-[ULPersistenceManager _excludeDirectoryFromTimeMachineBackup:];
-[ULPersistenceManager _exitProcessWithFailureCode];
-[ULPersistenceManager _getDefaultStoresDirectoryPathForCurrentPlatform];
-[ULPersistenceManager _getLocalStoreURL];
-[ULPersistenceManager _handleCorruptedDatabase:];
-[ULPersistenceManager _handleDatabaseError:];
-[ULPersistenceManager dataContainer];
-[ULPersistenceManager destroyStore];
-[ULPersistenceManager initWithModelsDirectory:storesDirectory:managedObjectModel:useWal:];
-[ULPersistenceManager initWithModelsDirectory:storesDirectory:useWal:];
-[ULPersistenceManager isMainDatabase];
-[ULPersistenceManager isStoreConnected];
-[ULPersistenceManager setDataContainer:];
-[ULPersistenceManager setModelsDirectory:];
-[ULPersistenceManager setStoresDirectory:];
-[ULPersistenceManager setUseWal:];
```
