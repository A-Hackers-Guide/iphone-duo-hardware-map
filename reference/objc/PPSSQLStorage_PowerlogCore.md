# `PPSSQLStorage`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PPSStorage`
- 3 instance variables, 3 properties, 35 instance methods, 7 class methods

## Instance variables

```
B _storageStarted;
@"NSDictionary" _connectionByStorage;
@"NSMutableSet" _entryKeysToSetup;
```

## Properties

```
@property (TB,V_storageStarted) storageStarted;
@property (T@"NSDictionary",&,V_connectionByStorage) connectionByStorage;
@property (T@"NSMutableSet",&,V_entryKeysToSetup) entryKeysToSetup;
```

## Class methods

```
+[PPSSQLStorage trimConditionsForBGSQLWithTrimDate:];
+[PPSSQLStorage trimConditionsForCESQLWithTrimDate:];
+[PPSSQLStorage trimConditionsForEPSQLWithTrimDate:];
+[PPSSQLStorage trimConditionsForEntryKey:trimDate:currDate:];
+[PPSSQLStorage trimConditionsForPLSQLWithTrimDate:];
+[PPSSQLStorage trimConditionsForStorage:trimDate:];
+[PPSSQLStorage trimConditionsForXCSQLWithTrimDate:];
```

## Instance methods

```
-[PPSSQLStorage setupDBConnections];
-[PPSSQLStorage connectionForKey:];
-[PPSSQLStorage persistMetadata];
-[PPSSQLStorage connectionByStorage];
-[PPSSQLStorage init];
-[PPSSQLStorage startStorage];
-[PPSSQLStorage updateMetadata:updateMetrics:addMetrics:];
-[PPSSQLStorage setEntryKeysToSetup:];
-[PPSSQLStorage entryKeysToSetup];
-[PPSSQLStorage closeAllConnections];
-[PPSSQLStorage deleteOldMetadataStore];
-[PPSSQLStorage storageForConnection:];
-[PPSSQLStorage CESQLConnection];
-[PPSSQLStorage handleMetadataVersionChange];
-[PPSSQLStorage XCSQLConnection];
-[PPSSQLStorage BGSQLConnection];
-[PPSSQLStorage storageStarted];
-[PPSSQLStorage setupFolders];
-[PPSSQLStorage setupDBConnectionAtPath:];
-[PPSSQLStorage PreUnlockEPSQLConnection];
-[PPSSQLStorage handleSchemaMismatchForTable:];
-[PPSSQLStorage createMetadataTable];
-[PPSSQLStorage setupStorageForEntryKey:];
-[PPSSQLStorage setupDynamicTableForEntryKey:withName:withConnection:];
-[PPSSQLStorage setupTableForEntryKey:];
-[PPSSQLStorage setupArrayTableForEntryKey:withName:withConnection:];
-[PPSSQLStorage PLSQLConnection];
-[PPSSQLStorage setConnectionByStorage:];
-[PPSSQLStorage setupMetadataStorage];
-[PPSSQLStorage metricsToAddForStorage:processedMetrics:];
-[PPSSQLStorage updateTable:transferDataForKeys:];
-[PPSSQLStorage setupTableForEntryKey:withName:];
-[PPSSQLStorage setStorageStarted:];
-[PPSSQLStorage metricsToUpdateForStorage:processedMetrics:];
-[PPSSQLStorage EPSQLConnection];
```
