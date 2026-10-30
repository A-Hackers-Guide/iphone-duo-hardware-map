# `PLCoalitionAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 13 instance variables, 13 properties, 61 instance methods, 8 class methods

## Instance variables

```
@"PLEntryNotificationOperatorComposition" _batteryLevelChanged;
@"PLEntryNotificationOperatorComposition" _batteryEntryLogged;
@"NSMutableDictionary" _lastCoalitionObjectDictionary;
@"NSDate" _lastDate;
@"NSDate" _currentDate;
@"NSString" _driveCapacity;
@"PLNSNotificationOperatorComposition" _thermalMonitorListener;
@"PLXPCResponderOperatorComposition" _logicalWritesResponder;
@"NSDate" _reportMemoryStatsAfterTime;
@"NSDate" _reportHighFrequencyMemoryStatsAfterTime;
@"PLStateTrackingComposition" _stateTracker;
@"PLTimer" _osMetricMonitorTimer;
d _osMetricMonitorCadence;
```

## Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryLevelChanged) batteryLevelChanged;
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryEntryLogged) batteryEntryLogged;
@property (T@"NSMutableDictionary",&,V_lastCoalitionObjectDictionary) lastCoalitionObjectDictionary;
@property (T@"NSDate",&,V_lastDate) lastDate;
@property (T@"NSDate",&,V_currentDate) currentDate;
@property (T@"NSString",&,V_driveCapacity) driveCapacity;
@property (T@"PLNSNotificationOperatorComposition",&,V_thermalMonitorListener) thermalMonitorListener;
@property (T@"PLXPCResponderOperatorComposition",&,V_logicalWritesResponder) logicalWritesResponder;
@property (T@"NSDate",&,V_reportMemoryStatsAfterTime) reportMemoryStatsAfterTime;
@property (T@"NSDate",&,V_reportHighFrequencyMemoryStatsAfterTime) reportHighFrequencyMemoryStatsAfterTime;
@property (T@"PLStateTrackingComposition",&,V_stateTracker) stateTracker;
@property (T@"PLTimer",&,V_osMetricMonitorTimer) osMetricMonitorTimer;
@property (Td,V_osMetricMonitorCadence) osMetricMonitorCadence;
```

## Class methods

```
+[PLCoalitionAgent entryEventIntervalDefinitions];
+[PLCoalitionAgent entryEventPointDefinitions];
+[PLCoalitionAgent load];
+[PLCoalitionAgent entryAggregateDefinitions];
+[PLCoalitionAgent entryAggregateDefinitionNANDStats];
+[PLCoalitionAgent entryEventIntervalDefinitionCoalitionUsage];
+[PLCoalitionAgent entryEventPointDefinitionCoalitionDrop];
+[PLCoalitionAgent entryEventPointDefinitionCoalitionMemory];
```

## Instance methods

```
-[PLCoalitionAgent currentDate];
-[PLCoalitionAgent init];
-[PLCoalitionAgent stateTracker];
-[PLCoalitionAgent initOperatorDependancies];
-[PLCoalitionAgent setThermalMonitorListener:];
-[PLCoalitionAgent setBatteryEntryLogged:];
-[PLCoalitionAgent setStateTracker:];
-[PLCoalitionAgent setBatteryLevelChanged:];
-[PLCoalitionAgent batteryEntryLogged];
-[PLCoalitionAgent log];
-[PLCoalitionAgent thermalMonitorListener];
-[PLCoalitionAgent batteryLevelChanged];
-[PLCoalitionAgent setCurrentDate:];
-[PLCoalitionAgent lastDate];
-[PLCoalitionAgent setLastDate:];
-[PLCoalitionAgent osMetricEnabled];
-[PLCoalitionAgent addAccountingEventsFromCoalitions:];
-[PLCoalitionAgent buildPLCoalitionDataObject:withBundleId:withLaunchdName:withDate:withCoalitionId:withMetrics:isApp:];
-[PLCoalitionAgent buildPLEntryDiffForObject:withNewUsage:hasPrevSample:withStartDate:withEndDate:];
-[PLCoalitionAgent driveCapacity];
-[PLCoalitionAgent getANEEnergyFromEntry:];
-[PLCoalitionAgent getCPUEnergyFromEntry:];
-[PLCoalitionAgent getCPUVoucherTimeFromEntry:];
-[PLCoalitionAgent getCPUWeightFromEntry:];
-[PLCoalitionAgent getCoalitionInfoWithHFLFlag:];
-[PLCoalitionAgent getGPUEnergyFromEntry:];
-[PLCoalitionAgent getGPUTimeFromEntry:];
-[PLCoalitionAgent getGPUWeightFromEntry:];
-[PLCoalitionAgent getStorageCapacity];
-[PLCoalitionAgent handleStateChangeForCoalitions];
-[PLCoalitionAgent lastCoalitionObjectDictionary];
-[PLCoalitionAgent logAggregateNANDStatsWithInfo:];
-[PLCoalitionAgent logCoalitionObjectMemory:];
-[PLCoalitionAgent logCoalitionObjectMemory:withOSMetrics:];
-[PLCoalitionAgent logEventIntervalCoalitionIntervalWithHFLFlag:];
-[PLCoalitionAgent logEventIntervalCoalitionIntervalWithoutHighFreqLogging];
-[PLCoalitionAgent logOSMetrics:withNewUsage:hasPrevSample:];
-[PLCoalitionAgent logOsMetricsMemory:withData:];
-[PLCoalitionAgent logToAggd:];
-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:];
-[PLCoalitionAgent logicalWritesResponder];
-[PLCoalitionAgent metricCount:withStart:withEnd:];
-[PLCoalitionAgent metricCount:withStartTime:withEndTime:];
-[PLCoalitionAgent metricCount:withTime:];
-[PLCoalitionAgent metricCount:withValue:];
-[PLCoalitionAgent osMetricMonitorCadence];
-[PLCoalitionAgent osMetricMonitorTimer];
-[PLCoalitionAgent processMemoryUsageWithPid:withLaunchdName:withRusage:withJetsamInfo:withLimitInfo:];
-[PLCoalitionAgent processPerAppLogicalWritesWithInfo:];
-[PLCoalitionAgent readPropertyFromRegistry:];
-[PLCoalitionAgent reportHighFrequencyMemoryStatsAfterTime];
-[PLCoalitionAgent reportMemoryStatsAfterTime];
-[PLCoalitionAgent setDriveCapacity:];
-[PLCoalitionAgent setLastCoalitionObjectDictionary:];
-[PLCoalitionAgent setLogicalWritesResponder:];
-[PLCoalitionAgent setOsMetricMonitorCadence:];
-[PLCoalitionAgent setOsMetricMonitorTimer:];
-[PLCoalitionAgent setReportHighFrequencyMemoryStatsAfterTime:];
-[PLCoalitionAgent setReportMemoryStatsAfterTime:];
-[PLCoalitionAgent shouldLogCoalitionObject:withNewUsage:hasPrevSample:];
-[PLCoalitionAgent shouldProcessCoalitionID:seenCoalitionIDs:];
```
