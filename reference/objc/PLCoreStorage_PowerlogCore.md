# `PLCoreStorage`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UMUserSwitchStakeholder`
- 24 instance variables, 28 properties, 127 instance methods, 5 class methods

## Instance variables

```
B _storageLocked;
B _storageReady;
@"PLSQLiteConnection" _connection;
@"NSString" _uuid;
@"PLKQueue" _profileDefaultsKQueue;
@"PLTimer" _dailyTaskTimer;
@"PLTimer" _flushCachesTimer;
@"PLNSNotificationOperatorComposition" _dailyTaskNotification;
@"PLCFNotificationOperatorComposition" _flushCachesCFNotification;
@"PLCFNotificationOperatorComposition" _blockingFlushCachesCFNotification;
@"PLCFNotificationOperatorComposition" _keybagFirstUnlockNotification;
@"PLCFNotificationOperatorComposition" _keybagLockStatusNotification;
@"PLXPCResponderOperatorComposition" _safeFileResponder;
@"PLXPCResponderOperatorComposition" _XPCFlushCacheResponder;
@"PLXPCResponderOperatorComposition" _blPathResponder;
@"PLXPCResponderOperatorComposition" _archivesResponder;
@"PLXPCResponderOperatorComposition" _quarantineResponder;
@"PLXPCResponderOperatorComposition" _quarantineCopyResponder;
@"PLXPCResponderOperatorComposition" _batteryUIPlistsResponder;
@"PLXPCResponderOperatorComposition" _upgradeLogsResponder;
@"PLStorageOperator" _storageOperator;
@"NSMutableSet" _safeCopyInProgress;
@"NSObject<OS_dispatch_queue>" _backgroundQueue;
@"NSObject<OS_dispatch_queue>" _utilityQueue;
```

## Properties

```
@property (TB,N,V_storageLocked) storageLocked;
@property (T@"PLKQueue",&,V_profileDefaultsKQueue) profileDefaultsKQueue;
@property (T@"PLTimer",&,V_dailyTaskTimer) dailyTaskTimer;
@property (T@"PLTimer",&,V_flushCachesTimer) flushCachesTimer;
@property (T@"PLNSNotificationOperatorComposition",&,V_dailyTaskNotification) dailyTaskNotification;
@property (T@"PLCFNotificationOperatorComposition",&,V_flushCachesCFNotification) flushCachesCFNotification;
@property (T@"PLCFNotificationOperatorComposition",&,V_blockingFlushCachesCFNotification) blockingFlushCachesCFNotification;
@property (T@"PLCFNotificationOperatorComposition",&,V_keybagFirstUnlockNotification) keybagFirstUnlockNotification;
@property (T@"PLCFNotificationOperatorComposition",&,V_keybagLockStatusNotification) keybagLockStatusNotification;
@property (T@"PLXPCResponderOperatorComposition",&,V_safeFileResponder) safeFileResponder;
@property (T@"PLXPCResponderOperatorComposition",&,V_XPCFlushCacheResponder) XPCFlushCacheResponder;
@property (T@"PLXPCResponderOperatorComposition",&,V_blPathResponder) blPathResponder;
@property (T@"PLXPCResponderOperatorComposition",&,V_archivesResponder) archivesResponder;
@property (T@"PLXPCResponderOperatorComposition",&,V_quarantineResponder) quarantineResponder;
@property (T@"PLXPCResponderOperatorComposition",&,V_quarantineCopyResponder) quarantineCopyResponder;
@property (T@"PLXPCResponderOperatorComposition",&,V_batteryUIPlistsResponder) batteryUIPlistsResponder;
@property (T@"PLXPCResponderOperatorComposition",&,V_upgradeLogsResponder) upgradeLogsResponder;
@property (T@"PLStorageOperator",&,V_storageOperator) storageOperator;
@property (T@"NSMutableSet",&,V_safeCopyInProgress) safeCopyInProgress;
@property (T@"NSObject<OS_dispatch_queue>",&,V_backgroundQueue) backgroundQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,V_utilityQueue) utilityQueue;
@property (T@"PLSQLiteConnection",&,V_connection) connection;
@property (TB,V_storageReady) storageReady;
@property (T@"NSString",&,V_uuid) uuid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PLCoreStorage logMessage:fromFile:fromFunction:fromLineNumber:];
+[PLCoreStorage additionalTables];
+[PLCoreStorage allOperatorTablesToTrimConditionsForTrimDate:];
+[PLCoreStorage storageQueueNameForClass:];
+[PLCoreStorage storageQueueNameForEntryKey:];
```

## Instance methods

```
-[PLCoreStorage registerDailyTasks];
-[PLCoreStorage dailyTaskTimer];
-[PLCoreStorage loadDynamicValuesIntoEntry:];
-[PLCoreStorage upgradeLogsResponder];
-[PLCoreStorage dailyTasks];
-[PLCoreStorage setAllNullValuesForEntryKey:forKey:toValue:withFilters:];
-[PLCoreStorage setKeybagFirstUnlockNotification:];
-[PLCoreStorage setBlPathResponder:];
-[PLCoreStorage blockingUpdateEntry:withBlock:];
-[PLCoreStorage setFlushCachesTimer:];
-[PLCoreStorage countOfEntriesForKey:];
-[PLCoreStorage profileDefaultsKQueue];
-[PLCoreStorage checkCacheSizeForFlush];
-[PLCoreStorage storageLocked];
-[PLCoreStorage backgroundQueue];
-[PLCoreStorage uuid];
-[PLCoreStorage init];
-[PLCoreStorage setBlockingFlushCachesCFNotification:];
-[PLCoreStorage setupStorageForOperatorName:];
-[PLCoreStorage setProfileDefaultsKQueue:];
-[PLCoreStorage startStorage];
-[PLCoreStorage processIDEntryForPid:];
-[PLCoreStorage setupArrayForTableName:forColumnNamed:withValueType:withShouldIndexFKID:];
-[PLCoreStorage aggregateEntriesForKey:withBucketLength:inTimeIntervalRange:];
-[PLCoreStorage setBatteryUIPlistsResponder:];
-[PLCoreStorage setupStorageForOperatorClass:];
-[PLCoreStorage dealloc];
-[PLCoreStorage setUuid:];
-[PLCoreStorage entriesForKey:inTimeRange:withFilters:];
-[PLCoreStorage initOperatorDependancies];
-[PLCoreStorage setXPCFlushCacheResponder:];
-[PLCoreStorage blockingFlushCachesWithReason:];
-[PLCoreStorage writeEntries:withCompletionBlock:];
-[PLCoreStorage configureCacheFlush];
-[PLCoreStorage lastEntryForKey:withFilters:];
-[PLCoreStorage flushCachesTimer];
-[PLCoreStorage removeErroneousQualificationEntries];
-[PLCoreStorage blPathResponder];
-[PLCoreStorage blockingFlushCachesWithReason:timeout:];
-[PLCoreStorage setStorageLocked:];
-[PLCoreStorage deleteEntry:];
-[PLCoreStorage entriesForKey:withComparisons:];
-[PLCoreStorage setupTableName:withEntryKeyConfig:withKeyOrder:isDynamic:withShouldIndexFKID:];
-[PLCoreStorage setUpgradeLogsResponder:];
-[PLCoreStorage dispatchSyncForEntryKey:withBlock:];
-[PLCoreStorage deleteAllEntriesForKey:withFilters:];
-[PLCoreStorage logPreUnlockState:];
-[PLCoreStorage setupCompositeIndexOnTable:withColumns:];
-[PLCoreStorage setDailyTaskTimer:];
-[PLCoreStorage setBackgroundQueue:];
-[PLCoreStorage _updateEntry:withBlock:];
-[PLCoreStorage generalEntryCacheSizeLimit];
-[PLCoreStorage willSwitchUser];
-[PLCoreStorage setupStorageForOperator:];
-[PLCoreStorage blockingWriteEntry:withCompletionBlock:];
-[PLCoreStorage safeCopyInProgress];
-[PLCoreStorage setStorageReady:];
-[PLCoreStorage entriesForKey:before:timeInterval:count:withFilters:];
-[PLCoreStorage lastEntryForKey:];
-[PLCoreStorage reportPerfStats];
-[PLCoreStorage storageReady];
-[PLCoreStorage handleSchemaMismatchForTable:expectedVersion:schemaMatch:];
-[PLCoreStorage copyUpgradePowerlogsAtPath:toPath:];
-[PLCoreStorage flushCachesWithReason:];
-[PLCoreStorage XPCFlushCacheResponder];
-[PLCoreStorage connection];
-[PLCoreStorage quarantineResponder];
-[PLCoreStorage deleteEntryForKey:WithRowID:];
-[PLCoreStorage flushCachesIfRequiredForEntryKey:];
-[PLCoreStorage deleteAllEntriesForKey:beforeTimestamp:];
-[PLCoreStorage registerDailyTasks_XPCActivity];
-[PLCoreStorage setArchivesResponder:];
-[PLCoreStorage deleteAllEntriesForKey:];
-[PLCoreStorage lastEntryForKey:withSubEntryKey:];
-[PLCoreStorage removeOldPowerlogFiles];
-[PLCoreStorage quarantineCopyResponder];
-[PLCoreStorage setDailyTaskNotification:];
-[PLCoreStorage setConnection:];
-[PLCoreStorage deleteAllEntriesForKey:beforeTimestamp:withFilters:];
-[PLCoreStorage batteryUIPlistsResponder];
-[PLCoreStorage applyContainerPOSIXPermissions];
-[PLCoreStorage setStorageOperator:];
-[PLCoreStorage utilityQueue];
-[PLCoreStorage writeEntry:];
-[PLCoreStorage archivesResponder];
-[PLCoreStorage stopStorage];
-[PLCoreStorage cleanupQuarantine];
-[PLCoreStorage setupStorageForEntryKey:];
-[PLCoreStorage lastEntryForKey:withComparisons:isSingleton:];
-[PLCoreStorage entriesForKey:withProperties:];
-[PLCoreStorage blockingFlushCachesCFNotification];
-[PLCoreStorage setupStorageVersions];
-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:];
-[PLCoreStorage entriesForKey:withQuery:];
-[PLCoreStorage entryForKey:withID:];
-[PLCoreStorage firstEntryForKey:];
-[PLCoreStorage removeStorageForEntryKey:];
-[PLCoreStorage entriesForKey:inTimeRange:withCountOfEntriesBefore:withCountOfEntriesAfter:withFilters:];
-[PLCoreStorage dispatchAsyncForEntryKey:withBlock:];
-[PLCoreStorage storageOperator];
-[PLCoreStorage entriesForKey:];
-[PLCoreStorage setFileProtectionForPath:withLevel:];
-[PLCoreStorage lastEntriesForKey:count:withFilters:];
-[PLCoreStorage updateEntry:withBlock:];
-[PLCoreStorage logMessage:fromFile:fromFunction:fromLineNumber:];
-[PLCoreStorage setKeybagLockStatusNotification:];
-[PLCoreStorage writeAggregateEntry:];
-[PLCoreStorage blockingFlushQueues:withTimeout:];
-[PLCoreStorage keybagLockStatusNotification];
-[PLCoreStorage cleanupTmp];
-[PLCoreStorage addAggdModeKeys];
-[PLCoreStorage setFlushCachesCFNotification:];
-[PLCoreStorage writeEntry:withCompletionBlock:];
-[PLCoreStorage setUtilityQueue:];
-[PLCoreStorage safeFileResponder];
-[PLCoreStorage setSafeCopyInProgress:];
-[PLCoreStorage keybagFirstUnlockNotification];
-[PLCoreStorage attemptToSendTaskingStartNotification];
-[PLCoreStorage dailyTaskNotification];
-[PLCoreStorage setQuarantineResponder:];
-[PLCoreStorage flushCachesCFNotification];
-[PLCoreStorage setSafeFileResponder:];
-[PLCoreStorage verifySchemaVersionOfTable:matchesExpectedVersion:];
-[PLCoreStorage entriesForKey:startingFromRowID:count:withFilters:];
-[PLCoreStorage setQuarantineCopyResponder:];
-[PLCoreStorage lastEntryForKey:withIDLessThan:];
-[PLCoreStorage processEntriesForKey:withProperties:withBlock:];
```
