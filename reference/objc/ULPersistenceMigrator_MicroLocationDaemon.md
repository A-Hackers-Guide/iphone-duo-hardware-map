# `ULPersistenceMigrator`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CLLocationManagerDelegate`
- 2 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
^{ULDatabaseStoreInterface=^^?} _dbStore;
^{ULDatabaseManagementInterface=^^?} _dbManagement;
```

## Properties

```
@property (T^{ULDatabaseStoreInterface=^^?},N,V_dbStore) dbStore;
@property (T^{ULDatabaseManagementInterface=^^?},N,V_dbManagement) dbManagement;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ULPersistenceMigrator dbStore];
-[ULPersistenceMigrator _databaseMigrationTransaction];
-[ULPersistenceMigrator dbManagement];
-[ULPersistenceMigrator initWithDbStore:andDbManagement:];
-[ULPersistenceMigrator migrateToLatestVersion];
-[ULPersistenceMigrator setDbManagement:];
-[ULPersistenceMigrator setDbStore:];
```
