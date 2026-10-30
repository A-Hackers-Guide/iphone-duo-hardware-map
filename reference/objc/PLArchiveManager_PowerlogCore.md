# `PLArchiveManager`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLArchiveJobManager`
- 15 instance variables, 20 properties, 57 instance methods, 10 class methods

## Instance variables

```
B _enabled;
B _interrupted;
B _monotonicResetOccurred;
d _interval;
d _mustRunInterval;
d _archiveRetention;
d _PLSQLDBDuration;
d _CESQLDBDuration;
d _EPSQLDBDuration;
d _EPSQLVacuumInterval;
d _XCSQLDBDuration;
d _BGSQLDBDuration;
@"NSMutableArray" _archiveJobs;
@"NSMutableArray" _notificationBlocks;
@"PLCFNotificationOperatorComposition" _fireArchiveListener;
```

## Properties

```
@property (Td,V_interval) interval;
@property (Td,V_mustRunInterval) mustRunInterval;
@property (Td,V_archiveRetention) archiveRetention;
@property (Td,V_PLSQLDBDuration) PLSQLDBDuration;
@property (Td,V_CESQLDBDuration) CESQLDBDuration;
@property (Td,V_EPSQLDBDuration) EPSQLDBDuration;
@property (Td,V_EPSQLVacuumInterval) EPSQLVacuumInterval;
@property (T@"NSDate",&) lastEPSQLVacuumDate;
@property (Td,V_XCSQLDBDuration) XCSQLDBDuration;
@property (Td,V_BGSQLDBDuration) BGSQLDBDuration;
@property (T@"NSMutableArray",&,V_archiveJobs) archiveJobs;
@property (TB,N,V_interrupted) interrupted;
@property (T@"NSMutableArray",&,V_notificationBlocks) notificationBlocks;
@property (TB,V_monotonicResetOccurred) monotonicResetOccurred;
@property (T@"PLCFNotificationOperatorComposition",&,V_fireArchiveListener) fireArchiveListener;
@property (TB,N,V_enabled) enabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PLArchiveManager sharedInstance];
+[PLArchiveManager storageQueue];
+[PLArchiveManager workQueue];
+[PLArchiveManager allArchivePaths];
+[PLArchiveManager archiveForDate:];
+[PLArchiveManager lastArchivePath];
+[PLArchiveManager archiveEntriesFinished];
+[PLArchiveManager archiveEntriesUnfinished];
+[PLArchiveManager archiveEntriesWithComparisons:];
+[PLArchiveManager systemTimeChangedByOffset:];
```

## Instance methods

```
-[PLArchiveManager enable];
-[PLArchiveManager migrate];
-[PLArchiveManager cleanup];
-[PLArchiveManager isInterrupted];
-[PLArchiveManager interrupted];
-[PLArchiveManager setInterval:];
-[PLArchiveManager enabled];
-[PLArchiveManager interval];
-[PLArchiveManager init];
-[PLArchiveManager dealloc];
-[PLArchiveManager disable];
-[PLArchiveManager setEnabled:];
-[PLArchiveManager setInterrupted:];
-[PLArchiveManager recover];
-[PLArchiveManager EPSQLVacuumInterval];
-[PLArchiveManager EPSQLDBDuration];
-[PLArchiveManager PLSQLDBDuration];
-[PLArchiveManager deprecateTables];
-[PLArchiveManager setArchiveJobs:];
-[PLArchiveManager BGSQLDBDuration];
-[PLArchiveManager CESQLDBDuration];
-[PLArchiveManager XCSQLDBDuration];
-[PLArchiveManager migrateArchive:];
-[PLArchiveManager mustRunInterval];
-[PLArchiveManager archiveJobs];
-[PLArchiveManager archiveRetention];
-[PLArchiveManager deprecateTablesBGSQL];
-[PLArchiveManager deprecateTablesEPSQL];
-[PLArchiveManager deprecateTablesXCSQL];
-[PLArchiveManager eliglibleToVacuumEPSQLForDate:];
-[PLArchiveManager fireArchiveListener];
-[PLArchiveManager getArchivingCriteria];
-[PLArchiveManager handleFailure:forArchiveEntry:];
-[PLArchiveManager lastEPSQLVacuumDate];
-[PLArchiveManager monotonicResetOccurred];
-[PLArchiveManager notificationBlocks];
-[PLArchiveManager registerForArchivingNotificationUsingBlock:];
-[PLArchiveManager runActivityWithLastCompletedDate:];
-[PLArchiveManager runArchiveJobs];
-[PLArchiveManager runInitialActivity];
-[PLArchiveManager scheduleArchiveJobs];
-[PLArchiveManager setArchiveRetention:];
-[PLArchiveManager setBGSQLDBDuration:];
-[PLArchiveManager setCESQLDBDuration:];
-[PLArchiveManager setEPSQLDBDuration:];
-[PLArchiveManager setEPSQLVacuumInterval:];
-[PLArchiveManager setFireArchiveListener:];
-[PLArchiveManager setLastEPSQLVacuumDate:];
-[PLArchiveManager setMonotonicResetOccurred:];
-[PLArchiveManager setMustRunInterval:];
-[PLArchiveManager setNotificationBlocks:];
-[PLArchiveManager setPLSQLDBDuration:];
-[PLArchiveManager setXCSQLDBDuration:];
-[PLArchiveManager trimBackgroundProcessingLog];
-[PLArchiveManager trimCleanEnergyLog];
-[PLArchiveManager trimExtendedPersistenceLog];
-[PLArchiveManager trimXcodeOrganizerLog];
```
