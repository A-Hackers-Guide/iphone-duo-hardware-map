# `PLSQLiteConnection`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 14 properties, 117 instance methods, 10 class methods

## Instance variables

```
B _metadataStmtCreated;
i _transactionInProgress;
i _entryCacheStorageSize;
@"NSString" _filePath;
^{sqlite3=} _dbConnection;
@"NSObject<OS_dispatch_semaphore>" _dbSem;
@"NSMutableDictionary" _preparedStatements;
@"NSMutableDictionary" _preparedUpdateStatements;
@"NSMutableDictionary" _preparedDynamicStatements;
@"NSString" _transactionLock;
@"NSString" _cachedClassName;
q _cacheSize;
@"PLSQLStatement" _metadataStmt;
```

## Properties

```
@property (T^{sqlite3=},V_dbConnection) dbConnection;
@property (T@"NSObject<OS_dispatch_semaphore>",&,V_dbSem) dbSem;
@property (T@"NSMutableDictionary",&,V_preparedStatements) preparedStatements;
@property (T@"NSMutableDictionary",&,V_preparedUpdateStatements) preparedUpdateStatements;
@property (T@"NSMutableDictionary",&,V_preparedDynamicStatements) preparedDynamicStatements;
@property (Ti,V_transactionInProgress) transactionInProgress;
@property (T@"NSString",&,V_transactionLock) transactionLock;
@property (T@"NSString",&,V_cachedClassName) cachedClassName;
@property (Ti,V_entryCacheStorageSize) entryCacheStorageSize;
@property (Tq,V_cacheSize) cacheSize;
@property (TB,V_metadataStmtCreated) metadataStmtCreated;
@property (T@"PLSQLStatement",&,V_metadataStmt) metadataStmt;
@property (T@"NSObject<OS_dispatch_queue>",R) workQueue;
@property (T@"NSString",C,N,V_filePath) filePath;
```

## Class methods

```
+[PLSQLiteConnection masterTableForTable:andType:];
+[PLSQLiteConnection periodicIntegrityCheckInterval];
+[PLSQLiteConnection removeAdditionalFiles:];
+[PLSQLiteConnection removeDBAtFilePath:];
+[PLSQLiteConnection sharedSQLiteConnection];
+[PLSQLiteConnection tableColumnPresenceCache];
+[PLSQLiteConnection tableColumnPresenceCacheSem];
+[PLSQLiteConnection tableHasTimestampColumn];
+[PLSQLiteConnection tableHasTimestampColumnSem];
+[PLSQLiteConnection versionForTable:];
```

## Instance methods

```
-[PLSQLiteConnection endTransaction];
-[PLSQLiteConnection setMetadataStmt:];
-[PLSQLiteConnection beginTransaction];
-[PLSQLiteConnection scheduleIntegrityCheck];
-[PLSQLiteConnection openCurrentFileWithCacheSize:];
-[PLSQLiteConnection loadDynamicValuesIntoEntry:];
-[PLSQLiteConnection displaySchema:];
-[PLSQLiteConnection performQuery:];
-[PLSQLiteConnection mergeDataFromOtherDBFile:];
-[PLSQLiteConnection schemaVersionForTable:];
-[PLSQLiteConnection setAllNullValuesForEntryKey:forKey:toValue:withFilters:];
-[PLSQLiteConnection writeDynamicEntries:];
-[PLSQLiteConnection transactionLock];
-[PLSQLiteConnection dropTables:];
-[PLSQLiteConnection deleteEntryForKey:withRowID:];
-[PLSQLiteConnection copyTable:fromDBName:withProperties:];
-[PLSQLiteConnection trimAllTablesFromDate:toDate:withTableFilters:];
-[PLSQLiteConnection preparedUpdateStatements];
-[PLSQLiteConnection setEntryCacheStorageSize:];
-[PLSQLiteConnection sqlFormatedColumnNamesForTableSelect:withSystemOffset:];
-[PLSQLiteConnection enumerateAllTablesWithBlock:];
-[PLSQLiteConnection init];
-[PLSQLiteConnection initWithFilePath:];
-[PLSQLiteConnection setPreparedDynamicStatements:];
-[PLSQLiteConnection cacheSize];
-[PLSQLiteConnection vacuum];
-[PLSQLiteConnection getCacheSpillValue];
-[PLSQLiteConnection initWithFilePath:withFlags:];
-[PLSQLiteConnection isIncrementalVacuumEnabled];
-[PLSQLiteConnection workQueue];
-[PLSQLiteConnection dealloc];
-[PLSQLiteConnection initWithFilePath:withCacheSize:];
-[PLSQLiteConnection enumerateTablesWithBlock:];
-[PLSQLiteConnection attachDB:withName:];
-[PLSQLiteConnection rowCountForTable:];
-[PLSQLiteConnection sqlPropertiesAsString:];
-[PLSQLiteConnection preparedStatements];
-[PLSQLiteConnection setDbSem:];
-[PLSQLiteConnection truncateDB];
-[PLSQLiteConnection loadArrayValuesIntoEntry:];
-[PLSQLiteConnection removeEmptyOldTables];
-[PLSQLiteConnection isTransactionInProgress];
-[PLSQLiteConnection trimTable:fromDate:withFilter:withTrimLimit:];
-[PLSQLiteConnection copyDatabase:];
-[PLSQLiteConnection setTransactionLock:];
-[PLSQLiteConnection deleteAllEntriesForKey:withFilters:];
-[PLSQLiteConnection setTransactionInProgress:];
-[PLSQLiteConnection clearTableHasTimestampColumnCache];
-[PLSQLiteConnection setCachedClassName:];
-[PLSQLiteConnection tableExistsForTableName:];
-[PLSQLiteConnection fullVacuum];
-[PLSQLiteConnection copyDatabaseToPath:fromDate:toDate:];
-[PLSQLiteConnection dbSem];
-[PLSQLiteConnection removeIDIndexes];
-[PLSQLiteConnection createTableName:withColumns:];
-[PLSQLiteConnection performStatement:];
-[PLSQLiteConnection dropTable:];
-[PLSQLiteConnection writeArrayEntries:];
-[PLSQLiteConnection freeMetadataState];
-[PLSQLiteConnection sortedSqlFormatedColumnNamesForTableInsert:];
-[PLSQLiteConnection clearTableColumnPresenceCache];
-[PLSQLiteConnection setJournalMode:];
-[PLSQLiteConnection writeDynamicEntriesToPPS:];
-[PLSQLiteConnection versionHashForTable:];
-[PLSQLiteConnection performQuery:returnValue:returnResult:];
-[PLSQLiteConnection copyDatabaseToPath:];
-[PLSQLiteConnection setPreparedUpdateStatements:];
-[PLSQLiteConnection cachedClassName];
-[PLSQLiteConnection writeMetadata:forFKID:build:name:version:];
-[PLSQLiteConnection bindEntry:toPreparedStatement:atBindPosition:];
-[PLSQLiteConnection setDbConnection:];
-[PLSQLiteConnection copyDatabaseToPath:fromDate:toDate:withTableFilters:vacuumDB:withCacheSize:];
-[PLSQLiteConnection transactionInProgress];
-[PLSQLiteConnection cachedStatementForMetadataInsert];
-[PLSQLiteConnection copyTable:fromConnection:withDBName:withProperties:andAttach:];
-[PLSQLiteConnection rowCountForTableName:];
-[PLSQLiteConnection tableInfo:];
-[PLSQLiteConnection buildColumnInsert:andValueInsert:forEntry:];
-[PLSQLiteConnection trimAllTablesFromDate:toDate:];
-[PLSQLiteConnection dbConnection];
-[PLSQLiteConnection closeConnection];
-[PLSQLiteConnection getIntegrityCheckCriteria];
-[PLSQLiteConnection deleteDynamicEntriesForKey:withRowID:];
-[PLSQLiteConnection setMetadataStmtCreated:];
-[PLSQLiteConnection detachDB:];
-[PLSQLiteConnection setCacheSize:];
-[PLSQLiteConnection removeTableNameFromMergeDB:];
-[PLSQLiteConnection writeEntry:];
-[PLSQLiteConnection filePath];
-[PLSQLiteConnection createIndexOnTable:forColumn:];
-[PLSQLiteConnection entriesForKey:withProperties:];
-[PLSQLiteConnection entriesForKey:withQuery:];
-[PLSQLiteConnection setVersionHash:forTableName:];
-[PLSQLiteConnection hashEntryKeyKeys:];
-[PLSQLiteConnection initWithFilePath:withCacheSize:withFlags:];
-[PLSQLiteConnection setSchemaVersion:forTableName:];
-[PLSQLiteConnection tableHasColumn:inTable:];
-[PLSQLiteConnection metadataStmt];
-[PLSQLiteConnection openCurrentFileWithCacheSize:withFlags:];
-[PLSQLiteConnection printDBStatusString];
-[PLSQLiteConnection setFilePath:];
-[PLSQLiteConnection createCompositeIndexOnTable:forColumns:];
-[PLSQLiteConnection openCurrentFile];
-[PLSQLiteConnection checkEmptyMasterTable:];
-[PLSQLiteConnection tableHasTimestampColumn:];
-[PLSQLiteConnection moveDatabaseToPath:];
-[PLSQLiteConnection deleteArrayEntriesForKey:withRowID:];
-[PLSQLiteConnection passesIntegrityCheck];
-[PLSQLiteConnection entryCacheStorageSize];
-[PLSQLiteConnection updateEntry:];
-[PLSQLiteConnection preparedDynamicStatements];
-[PLSQLiteConnection commonInitProcessWithFilePath:withCacheSize:];
-[PLSQLiteConnection runTrimQuery:];
-[PLSQLiteConnection sqlFormatedColumnNamesForTableInsert:];
-[PLSQLiteConnection copyDatabaseToPath:fromDate:toDate:withTableFilters:vacuumDB:];
-[PLSQLiteConnection setPreparedStatements:];
-[PLSQLiteConnection metadataStmtCreated];
```
