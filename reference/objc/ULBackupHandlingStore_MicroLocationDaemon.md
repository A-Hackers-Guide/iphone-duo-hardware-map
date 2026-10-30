# `ULBackupHandlingStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- 5 instance variables, 5 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"ULStore" _targetStore;
@"NSArray" _distinctHomeloiGroupIds;
@"NSDictionary" _loiUUIDToObjectIDMap;
@"NSDictionary" _scanEventUUIDToObjectIDMap;
{function<bool ()>="__f_"{__value_func<bool ()>="__buf_"(type="__data"[24C])"__f_"^v}} _shouldCancel;
```

## Properties

```
@property (T@"ULStore",&,N,V_targetStore) targetStore;
@property (T@"NSArray",&,N,V_distinctHomeloiGroupIds) distinctHomeloiGroupIds;
@property (T@"NSDictionary",&,N,V_loiUUIDToObjectIDMap) loiUUIDToObjectIDMap;
@property (T@"NSDictionary",&,N,V_scanEventUUIDToObjectIDMap) scanEventUUIDToObjectIDMap;
@property (T{function<bool ()>={__value_func<bool ()>=(type=[24C])^v}},N,V_shouldCancel) shouldCancel;
```

## Instance methods

```
-[ULBackupHandlingStore importData];
-[ULBackupHandlingStore exportData];
-[ULBackupHandlingStore setShouldCancel:];
-[ULBackupHandlingStore shouldCancel];
-[ULBackupHandlingStore setTargetStore:];
-[ULBackupHandlingStore _commitBatchToStore:forEntityName:stop:];
-[ULBackupHandlingStore _getDistinctHomeLoiGroupIds];
-[ULBackupHandlingStore _getUUIDToObjectIDMapForEntityName:uuidAttribute:sortAttribute:atStore:];
-[ULBackupHandlingStore _transferDataUsingGroupIdsFilter:];
-[ULBackupHandlingStore _transferLOIsInBatch:toStore:];
-[ULBackupHandlingStore _transferLOIsUsingGroupIdsFilter:];
-[ULBackupHandlingStore _transferRecordsForEntityName:relation:relationUUID:uuidMap:sortAttribute:limit:fetchBatchSize:];
-[ULBackupHandlingStore _transferRecordsInBatch:forEntityName:relation:relationUUID:uuidMap:toStore:];
-[ULBackupHandlingStore distinctHomeloiGroupIds];
-[ULBackupHandlingStore initWithSourceDatabase:targetDatabase:andCancelFunc:];
-[ULBackupHandlingStore logTransferResult:isExport:];
-[ULBackupHandlingStore loiUUIDToObjectIDMap];
-[ULBackupHandlingStore scanEventUUIDToObjectIDMap];
-[ULBackupHandlingStore setDistinctHomeloiGroupIds:];
-[ULBackupHandlingStore setLoiUUIDToObjectIDMap:];
-[ULBackupHandlingStore setScanEventUUIDToObjectIDMap:];
-[ULBackupHandlingStore targetStore];
```
