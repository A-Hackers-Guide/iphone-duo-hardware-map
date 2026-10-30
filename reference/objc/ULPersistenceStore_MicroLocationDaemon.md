# `ULPersistenceStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _isMigrationToLatestModelRequired;
@"NSPersistentStoreDescription" _storeDescription;
@"NSNumber" _storeModelVersionBeforeMigration;
```

## Properties

```
@property (T@"NSPersistentStoreDescription",&,N,V_storeDescription) storeDescription;
@property (TB,N,V_isMigrationToLatestModelRequired) isMigrationToLatestModelRequired;
@property (T@"NSNumber",&,N,V_storeModelVersionBeforeMigration) storeModelVersionBeforeMigration;
```

## Instance methods

```
-[ULPersistenceStore persistentStoreDescription];
-[ULPersistenceStore storeDescription];
-[ULPersistenceStore _getLoadedModelVersionNumber:];
-[ULPersistenceStore _getStoreMetaData:];
-[ULPersistenceStore _getStoreModelVersionNumber];
-[ULPersistenceStore _getVersionNumberFromModelVersion:];
-[ULPersistenceStore _isMigrationRequired:];
-[ULPersistenceStore initWithURL:useWal:];
-[ULPersistenceStore isMigrationToLatestModelRequired];
-[ULPersistenceStore loadWithCoordinator:error:];
-[ULPersistenceStore setIsMigrationToLatestModelRequired:];
-[ULPersistenceStore setMigrationComplete];
-[ULPersistenceStore setStoreDescription:];
-[ULPersistenceStore setStoreModelVersionBeforeMigration:];
-[ULPersistenceStore storeModelVersionBeforeMigration];
```
