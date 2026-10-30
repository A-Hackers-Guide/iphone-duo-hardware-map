# `ULCLDatabaseMigrator`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _migrateAllData;
^{ULDatabaseStoreInterface=^^?} _dbStore;
```

## Properties

```
@property (T^{ULDatabaseStoreInterface=^^?},N,V_dbStore) dbStore;
@property (TB,N,V_migrateAllData) migrateAllData;
```

## Instance methods

```
-[ULCLDatabaseMigrator dbStore];
-[ULCLDatabaseMigrator _connectToLocationdDatabase:];
-[ULCLDatabaseMigrator _logStatsForExportedDatabase:];
-[ULCLDatabaseMigrator _logStatsForLocalDatabase];
-[ULCLDatabaseMigrator _migrateTableUsingPaging:tableName:migrationLimit:pageSize:copyPageBlock:];
-[ULCLDatabaseMigrator initWithDbStore:];
-[ULCLDatabaseMigrator migrateAllData];
-[ULCLDatabaseMigrator setDbStore:];
-[ULCLDatabaseMigrator setMigrateAllData:];
```
