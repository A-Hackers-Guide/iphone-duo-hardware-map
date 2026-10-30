# `ULBackupAndRestore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 20 instance methods, 0 class methods

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
-[ULBackupAndRestore _getFileSize:];
-[ULBackupAndRestore dbStore];
-[ULBackupAndRestore _clearTempBackupDirectory:];
-[ULBackupAndRestore _createBackupDbPathWithAttributes:];
-[ULBackupAndRestore _createTempBackupDirectoryIfNotExists:];
-[ULBackupAndRestore _deleteTempDb:];
-[ULBackupAndRestore _didReceiveCancel:];
-[ULBackupAndRestore _exportiCloudBackupTransactionWithCancelFunc:];
-[ULBackupAndRestore _getTempBackupDatabaseDirectoryClearCurrent:createNew:];
-[ULBackupAndRestore _importiCloudBackupTransaction];
-[ULBackupAndRestore _setClassBAttributeToFile:];
-[ULBackupAndRestore _setExcludeFromBackupAttribute:withValue:];
-[ULBackupAndRestore dbManagement];
-[ULBackupAndRestore deleteBackupFiles];
-[ULBackupAndRestore exportiCloudBackupWithCancelFunc:];
-[ULBackupAndRestore getBackupDatabasePath];
-[ULBackupAndRestore importiCloudBackup];
-[ULBackupAndRestore initWithDbStore:andDbManagement:];
-[ULBackupAndRestore setDbManagement:];
-[ULBackupAndRestore setDbStore:];
```
