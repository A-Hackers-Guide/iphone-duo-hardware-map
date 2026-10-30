# `PLPowerAssertionAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 30 instance variables, 31 properties, 82 instance methods, 13 class methods

## Instance variables

```
B _assertionBufferFullNotificationActive;
B _firstBufferDrain;
B _lastActivityOverflow;
B _optimizesSubSecondAssertions;
B _gameMode;
B _displayOn;
B _pluggedIn;
@"PLCFNotificationOperatorComposition" _assertionNotification;
@"PLCFNotificationOperatorComposition" _assertionBufferFullNotification;
@"PLTimer" _assertionBufferFullNotificationRearmTimer;
@"NSMutableArray" _assertionBufferNotificationTracking;
@"PLEntryNotificationOperatorComposition" _batteryLevelNotificiations;
@"PLEntryNotificationOperatorComposition" _wakeNotification;
@"PLEntryNotificationOperatorComposition" _canSleepNotification;
@"PLNSNotificationOperatorComposition" _dailyTaskNotification;
@"PLCFNotificationOperatorComposition" _flushAssertionBufferCFNotification;
@"PLTimer" _runQueryTimer;
@"PLTimer" _assertionSnapShotTimer;
q _aggregateMaxPIDCount;
q _aggregteZeroDeltaCount;
@"NSMutableDictionary" _assertionAggregatedLastSamplePLDataStructure;
@"NSMutableDictionary" _assertionAggregatedLastSample;
@"NSDictionary" _startEndActionsToEnum;
@"NSDictionary" _assertTypeToEnum;
@"NSSet" _logAssertNameForActions;
@"NSMutableDictionary" _assertionUUIDCache;
@"NSMutableDictionary" _UUIDStartEntryCache;
@"NSMutableDictionary" _subSecondUUIDStartEntryCache;
@"PLNSNotificationOperatorComposition" _consoleModeListener;
@"PLStateTrackingComposition" _stateTracker;
```

## Properties

```
@property (T@"PLCFNotificationOperatorComposition",&,V_assertionNotification) assertionNotification;
@property (T@"PLCFNotificationOperatorComposition",&,V_assertionBufferFullNotification) assertionBufferFullNotification;
@property (T@"PLTimer",&,V_assertionBufferFullNotificationRearmTimer) assertionBufferFullNotificationRearmTimer;
@property (TB,N,V_assertionBufferFullNotificationActive) assertionBufferFullNotificationActive;
@property (T@"NSMutableArray",&,V_assertionBufferNotificationTracking) assertionBufferNotificationTracking;
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryLevelNotificiations) batteryLevelNotificiations;
@property (T@"PLEntryNotificationOperatorComposition",&,V_wakeNotification) wakeNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_canSleepNotification) canSleepNotification;
@property (T@"PLNSNotificationOperatorComposition",&,V_dailyTaskNotification) dailyTaskNotification;
@property (T@"PLCFNotificationOperatorComposition",&,V_flushAssertionBufferCFNotification) flushAssertionBufferCFNotification;
@property (T@"PLTimer",&,V_runQueryTimer) runQueryTimer;
@property (T@"PLTimer",&,V_assertionSnapShotTimer) assertionSnapShotTimer;
@property (TB,N) assertionSnapshotTimerActive;
@property (TB,V_firstBufferDrain) firstBufferDrain;
@property (Tq,V_aggregateMaxPIDCount) aggregateMaxPIDCount;
@property (Tq,V_aggregteZeroDeltaCount) aggregteZeroDeltaCount;
@property (T@"NSMutableDictionary",&,V_assertionAggregatedLastSamplePLDataStructure) assertionAggregatedLastSamplePLDataStructure;
@property (T@"NSMutableDictionary",&,N,V_assertionAggregatedLastSample) assertionAggregatedLastSample;
@property (T@"NSDictionary",R,V_startEndActionsToEnum) startEndActionsToEnum;
@property (T@"NSDictionary",R,V_assertTypeToEnum) assertTypeToEnum;
@property (T@"NSSet",R,V_logAssertNameForActions) logAssertNameForActions;
@property (TB,N,V_lastActivityOverflow) lastActivityOverflow;
@property (T@"NSMutableDictionary",&,V_assertionUUIDCache) assertionUUIDCache;
@property (T@"NSMutableDictionary",&,V_UUIDStartEntryCache) UUIDStartEntryCache;
@property (T@"NSMutableDictionary",&,V_subSecondUUIDStartEntryCache) subSecondUUIDStartEntryCache;
@property (TB,V_optimizesSubSecondAssertions) optimizesSubSecondAssertions;
@property (T@"PLNSNotificationOperatorComposition",&,V_consoleModeListener) consoleModeListener;
@property (TB,V_gameMode) gameMode;
@property (TB,V_displayOn) displayOn;
@property (TB,V_pluggedIn) pluggedIn;
@property (T@"PLStateTrackingComposition",&,V_stateTracker) stateTracker;
```

## Class methods

```
+[PLPowerAssertionAgent entryEventIntervalDefinitions];
+[PLPowerAssertionAgent entryEventPointDefinitions];
+[PLPowerAssertionAgent entryEventForwardDefinitions];
+[PLPowerAssertionAgent entryEventBackwardDefinitions];
+[PLPowerAssertionAgent entryEventNoneDefinitions];
+[PLPowerAssertionAgent load];
+[PLPowerAssertionAgent defaults];
+[PLPowerAssertionAgent entryEventPointDefinitionSnapshotReason];
+[PLPowerAssertionAgent entryEventPointDefinitionAggregateReset];
+[PLPowerAssertionAgent entryEventPointDefinitionBufferStatus];
+[PLPowerAssertionAgent shouldOptimizeSmallAssertions];
+[PLPowerAssertionAgent entryEventPointDefinitionTimedOutProcesses];
+[PLPowerAssertionAgent entryEventForwardDefinitionAssertion];
```

## Instance methods

```
-[PLPowerAssertionAgent setPluggedIn:];
-[PLPowerAssertionAgent setDisplayOn:];
-[PLPowerAssertionAgent handleStateChange];
-[PLPowerAssertionAgent aggregateMaxPIDCount];
-[PLPowerAssertionAgent displayOn];
-[PLPowerAssertionAgent setAggregteZeroDeltaCount:];
-[PLPowerAssertionAgent setConsoleModeListener:];
-[PLPowerAssertionAgent setAggregateMaxPIDCount:];
-[PLPowerAssertionAgent setAssertionNotification:];
-[PLPowerAssertionAgent updatePluggedInState];
-[PLPowerAssertionAgent logAssertNameForActions];
-[PLPowerAssertionAgent checkAssertionBufferFullNotificationRate];
-[PLPowerAssertionAgent init];
-[PLPowerAssertionAgent gameMode];
-[PLPowerAssertionAgent canSleepNotification];
-[PLPowerAssertionAgent stateTracker];
-[PLPowerAssertionAgent setAssertionSnapshotTimerActive:];
-[PLPowerAssertionAgent bundleIDForAssertionProcessPID:];
-[PLPowerAssertionAgent setAssertionBufferFullNotificationActive:];
-[PLPowerAssertionAgent initOperatorDependancies];
-[PLPowerAssertionAgent optimizesSubSecondAssertions];
-[PLPowerAssertionAgent batteryLevelNotificiations];
-[PLPowerAssertionAgent setAssertionBufferFullNotificationActive:withReason:];
-[PLPowerAssertionAgent setRunQueryTimer:];
-[PLPowerAssertionAgent firstBufferDrain];
-[PLPowerAssertionAgent logAggregatedAssertionActivityPLDataStructure];
-[PLPowerAssertionAgent assertionAggregatedLastSample];
-[PLPowerAssertionAgent logEventForwardAssertion];
-[PLPowerAssertionAgent setAssertionAggregatedLastSample:];
-[PLPowerAssertionAgent runQueryTimer];
-[PLPowerAssertionAgent pluggedIn];
-[PLPowerAssertionAgent logSnapshotAtMidnight:];
-[PLPowerAssertionAgent assertTypeToEnum];
-[PLPowerAssertionAgent assertionSnapshotTimerActive];
-[PLPowerAssertionAgent resetIOPMSetAssertionActivityAggregateWithReason:withPidCount:];
-[PLPowerAssertionAgent assertionUUIDCache];
-[PLPowerAssertionAgent logEventPointAggregateResetWithReason:withPidCount:];
-[PLPowerAssertionAgent setOptimizesSubSecondAssertions:];
-[PLPowerAssertionAgent setAssertionSnapShotTimer:];
-[PLPowerAssertionAgent assertionBufferFullNotificationActive];
-[PLPowerAssertionAgent assertionBufferFullNotification];
-[PLPowerAssertionAgent setAssertionBufferNotificationTracking:];
-[PLPowerAssertionAgent updateDisplayState];
-[PLPowerAssertionAgent setFirstBufferDrain:];
-[PLPowerAssertionAgent assertTypeToEnumMapping];
-[PLPowerAssertionAgent sanitizeAssertionNameForEntry:];
-[PLPowerAssertionAgent setSubSecondUUIDStartEntryCache:];
-[PLPowerAssertionAgent startEndActionsToEnumMapping];
-[PLPowerAssertionAgent UUIDStartEntryCache];
-[PLPowerAssertionAgent setWakeNotification:];
-[PLPowerAssertionAgent lastActivityOverflow];
-[PLPowerAssertionAgent startEndActionsToEnum];
-[PLPowerAssertionAgent setCanSleepNotification:];
-[PLPowerAssertionAgent setStateTracker:];
-[PLPowerAssertionAgent updateOptimizeSubSecondAssertions];
-[PLPowerAssertionAgent subSecondUUIDStartEntryCache];
-[PLPowerAssertionAgent setDailyTaskNotification:];
-[PLPowerAssertionAgent assertionBufferFullNotificationRearmTimer];
-[PLPowerAssertionAgent setGameMode:];
-[PLPowerAssertionAgent assertionNotification];
-[PLPowerAssertionAgent logSnapshot:];
-[PLPowerAssertionAgent wakeNotification];
-[PLPowerAssertionAgent flushAssertionBufferCFNotification];
-[PLPowerAssertionAgent log];
-[PLPowerAssertionAgent consoleModeListener];
-[PLPowerAssertionAgent setFlushAssertionBufferCFNotification:];
-[PLPowerAssertionAgent setAssertionAggregatedLastSamplePLDataStructure:];
-[PLPowerAssertionAgent logEventForwardAssertionWithReason:asSnapshot:];
-[PLPowerAssertionAgent resetIOPMSetAssertionActivityAggregatePLDataStructureWithReason:withPidCount:];
-[PLPowerAssertionAgent setAssertionBufferFullNotification:];
-[PLPowerAssertionAgent assertionBufferNotificationTracking];
-[PLPowerAssertionAgent setUUIDStartEntryCache:];
-[PLPowerAssertionAgent assertionAggregatedLastSamplePLDataStructure];
-[PLPowerAssertionAgent dailyTaskNotification];
-[PLPowerAssertionAgent setAssertionBufferFullNotificationRearmTimer:];
-[PLPowerAssertionAgent logAggregatedAssertionActivity];
-[PLPowerAssertionAgent aggregteZeroDeltaCount];
-[PLPowerAssertionAgent setAssertionUUIDCache:];
-[PLPowerAssertionAgent setLastActivityOverflow:];
-[PLPowerAssertionAgent setBatteryLevelNotificiations:];
-[PLPowerAssertionAgent assertionSnapShotTimer];
-[PLPowerAssertionAgent logInterval:];
```
