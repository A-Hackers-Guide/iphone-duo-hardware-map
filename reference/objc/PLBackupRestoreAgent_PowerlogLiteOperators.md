# `PLBackupRestoreAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 5 instance variables, 5 properties, 17 instance methods, 9 class methods

## Instance variables

```
B _backupState;
B _restoreState;
@"MBManager" _backupRestoreManager;
@"PLCFNotificationOperatorComposition" _backupRestoreNotification;
@"PLEntryNotificationOperatorComposition" _fastPassCallback;
```

## Properties

```
@property (T@"MBManager",R,V_backupRestoreManager) backupRestoreManager;
@property (TB,N,V_backupState) backupState;
@property (TB,N,V_restoreState) restoreState;
@property (T@"PLCFNotificationOperatorComposition",&,V_backupRestoreNotification) backupRestoreNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_fastPassCallback) fastPassCallback;
```

## Class methods

```
+[PLBackupRestoreAgent entryEventIntervalDefinitions];
+[PLBackupRestoreAgent entryEventPointDefinitions];
+[PLBackupRestoreAgent entryEventForwardDefinitions];
+[PLBackupRestoreAgent entryEventBackwardDefinitions];
+[PLBackupRestoreAgent entryEventNoneDefinitions];
+[PLBackupRestoreAgent load];
+[PLBackupRestoreAgent defaults];
+[PLBackupRestoreAgent isEnabled];
+[PLBackupRestoreAgent entryAggregateDefinitions];
```

## Instance methods

```
-[PLBackupRestoreAgent restoreState];
-[PLBackupRestoreAgent init];
-[PLBackupRestoreAgent backupState];
-[PLBackupRestoreAgent initOperatorDependancies];
-[PLBackupRestoreAgent setBackupState:];
-[PLBackupRestoreAgent log];
-[PLBackupRestoreAgent updateRestoreState];
-[PLBackupRestoreAgent backupRestoreManager];
-[PLBackupRestoreAgent backupRestoreNotification];
-[PLBackupRestoreAgent didChangeEvent:toState:];
-[PLBackupRestoreAgent fastPassCallback];
-[PLBackupRestoreAgent handleFastPassCallback:];
-[PLBackupRestoreAgent logEventForwardBackupRestore];
-[PLBackupRestoreAgent setBackupRestoreNotification:];
-[PLBackupRestoreAgent setFastPassCallback:];
-[PLBackupRestoreAgent setRestoreState:];
-[PLBackupRestoreAgent updateBackupState];
```
