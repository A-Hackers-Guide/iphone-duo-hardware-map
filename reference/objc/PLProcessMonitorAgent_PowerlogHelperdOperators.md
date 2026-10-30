# `PLProcessMonitorAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 21 instance variables, 21 properties, 86 instance methods, 26 class methods

## Instance variables

```
B _firstBoot;
B _launchServiceStatsEnabled;
@"NSDate" _currentCachedDate;
@"NSDate" _previousCacheDate;
d _currentCachedTotalCPUTime;
@"PLMonotonicTimer" _logTimer;
@"PLEntryNotificationOperatorComposition" _batteryLevelChanged;
@"PLNSNotificationOperatorComposition" _asertionNotifications;
@"NSMutableSet" _processes;
@"NSDictionary" _lastCPUTimeDict;
@"NSDictionary" _lastThreadIdToKTMonitorEntryDict;
@"NSDate" _lastEntryDate;
q _processExitSummaryCount;
@"NSDictionary" _lastFreezerProcs;
@"NSDictionary" _diffFreezerProcs;
@"PLXPCListenerOperatorComposition" _appResumePredictionsListener;
@"PLXPCListenerOperatorComposition" _appResumeInferredCarryListener;
@"PLXPCListenerOperatorComposition" _appNotFrozenListener;
@"PLXPCResponderOperatorComposition" _memoryKillsResponder;
@"PLXPCResponderOperatorComposition" _hudKillsResponder;
@"PLThreadStats" _threadStats;
```

## Properties

```
@property (T@"NSDate",&,V_currentCachedDate) currentCachedDate;
@property (T@"NSDate",&,V_previousCacheDate) previousCacheDate;
@property (Td,V_currentCachedTotalCPUTime) currentCachedTotalCPUTime;
@property (TB,V_firstBoot) firstBoot;
@property (T@"PLMonotonicTimer",&,V_logTimer) logTimer;
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryLevelChanged) batteryLevelChanged;
@property (T@"PLNSNotificationOperatorComposition",&,V_asertionNotifications) asertionNotifications;
@property (T@"NSMutableSet",&,V_processes) processes;
@property (T@"NSDictionary",&,V_lastCPUTimeDict) lastCPUTimeDict;
@property (T@"NSDictionary",&,V_lastThreadIdToKTMonitorEntryDict) lastThreadIdToKTMonitorEntryDict;
@property (T@"NSDate",&,V_lastEntryDate) lastEntryDate;
@property (TB,V_launchServiceStatsEnabled) launchServiceStatsEnabled;
@property (Tq,V_processExitSummaryCount) processExitSummaryCount;
@property (T@"NSDictionary",&,V_lastFreezerProcs) lastFreezerProcs;
@property (T@"NSDictionary",&,V_diffFreezerProcs) diffFreezerProcs;
@property (T@"PLXPCListenerOperatorComposition",&,V_appResumePredictionsListener) appResumePredictionsListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_appResumeInferredCarryListener) appResumeInferredCarryListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_appNotFrozenListener) appNotFrozenListener;
@property (T@"PLXPCResponderOperatorComposition",&,V_memoryKillsResponder) memoryKillsResponder;
@property (T@"PLXPCResponderOperatorComposition",&,V_hudKillsResponder) hudKillsResponder;
@property (T@"PLThreadStats",&,V_threadStats) threadStats;
```

## Class methods

```
+[PLProcessMonitorAgent entryEventIntervalDefinitions];
+[PLProcessMonitorAgent entryEventPointDefinitions];
+[PLProcessMonitorAgent entryEventForwardDefinitions];
+[PLProcessMonitorAgent entryEventBackwardDefinitions];
+[PLProcessMonitorAgent entryEventNoneDefinitions];
+[PLProcessMonitorAgent load];
+[PLProcessMonitorAgent defaults];
+[PLProcessMonitorAgent PIDToCoalitionID:];
+[PLProcessMonitorAgent enableThreadStatsLogging];
+[PLProcessMonitorAgent entryEventBackwardAppLaunchTimeSeries];
+[PLProcessMonitorAgent entryEventBackwardDefinitionThreadStats];
+[PLProcessMonitorAgent entryEventBackwardProcessExitHistogram];
+[PLProcessMonitorAgent entryEventForwardAppResumeInferredCarry];
+[PLProcessMonitorAgent entryEventForwardProcessID];
+[PLProcessMonitorAgent entryEventIntervalDefinitionKernelTaskMonitor];
+[PLProcessMonitorAgent entryEventIntervalDefinitionProcessMonitorDiff];
+[PLProcessMonitorAgent entryEventPointAppNapEnabled];
+[PLProcessMonitorAgent entryEventPointAppNotFrozen];
+[PLProcessMonitorAgent entryEventPointAppResumePredictions];
+[PLProcessMonitorAgent entryEventPointFreezerDemotion];
+[PLProcessMonitorAgent entryEventPointFreezerStats];
+[PLProcessMonitorAgent entryEventPointMemoryTracking];
+[PLProcessMonitorAgent entryEventPointProcessExit];
+[PLProcessMonitorAgent entryEventPointProcessSnapshot];
+[PLProcessMonitorAgent entryEventPointSharedCacheReslid];
+[PLProcessMonitorAgent entryEventPointSystemFreezerStats];
```

## Instance methods

```
-[PLProcessMonitorAgent processes];
-[PLProcessMonitorAgent init];
-[PLProcessMonitorAgent initOperatorDependancies];
-[PLProcessMonitorAgent lastEntryDate];
-[PLProcessMonitorAgent initTaskOperatorDependancies];
-[PLProcessMonitorAgent setBatteryLevelChanged:];
-[PLProcessMonitorAgent log];
-[PLProcessMonitorAgent setProcesses:];
-[PLProcessMonitorAgent batteryLevelChanged];
-[PLProcessMonitorAgent setLastEntryDate:];
-[PLProcessMonitorAgent logEventPointSharedCacheReslid:];
-[PLProcessMonitorAgent setThreadStats:];
-[PLProcessMonitorAgent getProcessName:];
-[PLProcessMonitorAgent lastCPUTimeDict];
-[PLProcessMonitorAgent logEventPointSystemFreezerStats];
-[PLProcessMonitorAgent appNotFrozenListener];
-[PLProcessMonitorAgent appResumeInferredCarryListener];
-[PLProcessMonitorAgent appResumePredictionsListener];
-[PLProcessMonitorAgent asertionNotifications];
-[PLProcessMonitorAgent currentCachedDate];
-[PLProcessMonitorAgent currentCachedTotalCPUTime];
-[PLProcessMonitorAgent diffFreezerProcs];
-[PLProcessMonitorAgent disableProcessExitLogging];
-[PLProcessMonitorAgent enableProcessExitLogging];
-[PLProcessMonitorAgent eventForwardProcessIDForPID:];
-[PLProcessMonitorAgent fetchSnapshotWithFlags:];
-[PLProcessMonitorAgent firstBoot];
-[PLProcessMonitorAgent getAllProcessExitsInLastHour];
-[PLProcessMonitorAgent getCpuUsageAndMemoryForPid:withBuffer:withNewProcessArray:withTotalCpu:withActiveProcesses:];
-[PLProcessMonitorAgent getFrozenProcesses];
-[PLProcessMonitorAgent getFrozenToSwapLedgerIndex:];
-[PLProcessMonitorAgent getJSEIdleTime];
-[PLProcessMonitorAgent getJetsamSnapshotEntries:];
-[PLProcessMonitorAgent getLedgerIndex:forKey:];
-[PLProcessMonitorAgent getProcDirtyTimeLedgerIndex:];
-[PLProcessMonitorAgent getProcessExits:];
-[PLProcessMonitorAgent getProcessesNotInFreezer:withCurrentProcesses:];
-[PLProcessMonitorAgent get_kthread_list:];
-[PLProcessMonitorAgent hudKillsResponder];
-[PLProcessMonitorAgent initializeThreadStatsLogging];
-[PLProcessMonitorAgent lastFreezerProcs];
-[PLProcessMonitorAgent lastThreadIdToKTMonitorEntryDict];
-[PLProcessMonitorAgent launchServiceStatsEnabled];
-[PLProcessMonitorAgent ledgerDataAtIndex:forPid:];
-[PLProcessMonitorAgent logEventBackwardAppLaunchTimeSeries:];
-[PLProcessMonitorAgent logEventBackwardProcessExitHistogram:withStats:withDate:];
-[PLProcessMonitorAgent logEventForwardAppResumeInferredCarry:];
-[PLProcessMonitorAgent logEventIntervalKernelTaskMonitor];
-[PLProcessMonitorAgent logEventIntervalProcessMonitorIntervalUsingCache];
-[PLProcessMonitorAgent logEventPointAppNapEnabled];
-[PLProcessMonitorAgent logEventPointAppNotFrozen:];
-[PLProcessMonitorAgent logEventPointAppResumePredictions:];
-[PLProcessMonitorAgent logEventPointFreezerDemotion];
-[PLProcessMonitorAgent logEventPointFreezerStats];
-[PLProcessMonitorAgent logEventPointMemoryTracking];
-[PLProcessMonitorAgent logEventPointProcessExit:excludeProcesses:withStats:withDate:withNowInSec:];
-[PLProcessMonitorAgent logEventPointProcessSnapshot];
-[PLProcessMonitorAgent logProcDirtyStats];
-[PLProcessMonitorAgent logProcessExit];
-[PLProcessMonitorAgent logThreadStats];
-[PLProcessMonitorAgent logTimer];
-[PLProcessMonitorAgent memoryKillsResponder];
-[PLProcessMonitorAgent previousCacheDate];
-[PLProcessMonitorAgent processExitSummaryCount];
-[PLProcessMonitorAgent processMonitorMultiKeyFromProcessID:];
-[PLProcessMonitorAgent processesOfInterest:];
-[PLProcessMonitorAgent setAppNotFrozenListener:];
-[PLProcessMonitorAgent setAppResumeInferredCarryListener:];
-[PLProcessMonitorAgent setAppResumePredictionsListener:];
-[PLProcessMonitorAgent setAsertionNotifications:];
-[PLProcessMonitorAgent setCurrentCachedDate:];
-[PLProcessMonitorAgent setCurrentCachedTotalCPUTime:];
-[PLProcessMonitorAgent setDiffFreezerProcs:];
-[PLProcessMonitorAgent setFirstBoot:];
-[PLProcessMonitorAgent setHudKillsResponder:];
-[PLProcessMonitorAgent setLastCPUTimeDict:];
-[PLProcessMonitorAgent setLastFreezerProcs:];
-[PLProcessMonitorAgent setLastThreadIdToKTMonitorEntryDict:];
-[PLProcessMonitorAgent setLaunchServiceStatsEnabled:];
-[PLProcessMonitorAgent setLogTimer:];
-[PLProcessMonitorAgent setMemoryKillsResponder:];
-[PLProcessMonitorAgent setPreviousCacheDate:];
-[PLProcessMonitorAgent setProcessExitSummaryCount:];
-[PLProcessMonitorAgent threadStats];
-[PLProcessMonitorAgent updateProcessExitSummary];
-[PLProcessMonitorAgent updateProcessMonitorCache];
```
