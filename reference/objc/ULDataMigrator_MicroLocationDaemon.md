# `ULDataMigrator`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
^{ULDatabaseStoreInterface=^^?} _dbStore;
^{ULDatabaseManagementInterface=^^?} _dbManagement;
```

## Properties

```
@property (T^{ULDatabaseStoreInterface=^^?},N,V_dbStore) dbStore;
@property (T^{ULDatabaseManagementInterface=^^?},N,V_dbManagement) dbManagement;
```

## Instance methods

```
-[ULDataMigrator dbStore];
-[ULDataMigrator migrateMiloData];
-[ULDataMigrator _getCAMigrationErrorTypeForLastMigrationStateAfterMaxFailures:];
-[ULDataMigrator _initializeMigrationStatusMetricsDict:forType:];
-[ULDataMigrator _migrateMiloDataTransaction];
-[ULDataMigrator _sendCoreAnalyticsEventForMigrationIfNecessary:];
-[ULDataMigrator dbManagement];
-[ULDataMigrator initWithDbStore:andDbManagement:];
-[ULDataMigrator setDbManagement:];
-[ULDataMigrator setDbStore:];
```
