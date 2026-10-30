# `CLConditionLedger`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSData" _encryptionKey;
@"NSMutableDictionary" _recordTable;
B _readSucceeded;
@"NSString" _ledgerName;
@"NSNumber" _ledgerVersionNumber;
@"NSURL" _ledgerFile;
```

## Properties

```
@property (T@"NSFileManager",R,GdefaultFileManager) fileManager;
@property (T@"NSString",R,N,V_ledgerName) ledgerName;
@property (T@"NSNumber",R,N,V_ledgerVersionNumber) ledgerVersionNumber;
@property (T@"NSURL",R,N,V_ledgerFile) ledgerFile;
@property (T@"NSDictionary",R,GallMonitoringRecordsByIdentifier) monitoredRecordsByIdentifier;
@property (T@"NSArray",R,GallMonitoringIdentifiers) monitoredIdentifiers;
```

## Instance methods

```
-[CLConditionLedger dealloc];
-[CLConditionLedger writeToFile];
-[CLConditionLedger performMigration];
-[CLConditionLedger directoryExists:];
-[CLConditionLedger addRecordForMonitoring:identifier:persist:];
-[CLConditionLedger allMonitoringIdentifiers];
-[CLConditionLedger allMonitoringRecordsByIdentifier];
-[CLConditionLedger defaultFileManager];
-[CLConditionLedger deleteLedgerFile];
-[CLConditionLedger initWithStoreType:domain:monitorConfiguration:];
-[CLConditionLedger ledgerFile];
-[CLConditionLedger ledgerName];
-[CLConditionLedger ledgerVersionNumber];
-[CLConditionLedger monitoringRecordForIdentifier:];
-[CLConditionLedger persistentFileReadSucceeded];
-[CLConditionLedger readConditionsFromFile];
-[CLConditionLedger removeRecordFromMonitoringWithIdentifier:];
-[CLConditionLedger setLedgerForType:domain:monitor:client:path:];
-[CLConditionLedger setLedgerVersionNumber:];
-[CLConditionLedger shouldMigrate];
-[CLConditionLedger updateEvent:forIdentifier:];
-[CLConditionLedger updateRecord:identifier:];
```
