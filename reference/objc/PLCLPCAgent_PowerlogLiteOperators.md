# `PLCLPCAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 11 instance variables, 11 properties, 47 instance methods, 12 class methods

## Instance variables

```
@"NSDate" _lastEntryDate;
@"NSDate" _lastCPUClusterEntryDate;
@"PLTimer" _tenMinuteTimer;
@"<CLPCReportingAccess>" _provider;
@"CLPCReportingStatSelection" _selection;
@"CLPCReportingReadResult" _readResults;
@"<CLPCReportingAccess>" _CPUClusterProvider;
@"CLPCReportingStatSelection" _CPUClusterSelection;
@"CLPCReportingReadResult" _CPUClusterReadResults;
@"PLNSNotificationOperatorComposition" _thermalMonitorListener;
@"PLStateTrackingComposition" _stateTracker;
```

## Properties

```
@property (T@"NSDate",&,V_lastEntryDate) lastEntryDate;
@property (T@"NSDate",&,V_lastCPUClusterEntryDate) lastCPUClusterEntryDate;
@property (T@"PLTimer",&,V_tenMinuteTimer) tenMinuteTimer;
@property (T@"<CLPCReportingAccess>",&,V_provider) provider;
@property (T@"CLPCReportingStatSelection",&,V_selection) selection;
@property (T@"CLPCReportingReadResult",&,V_readResults) readResults;
@property (T@"<CLPCReportingAccess>",&,V_CPUClusterProvider) CPUClusterProvider;
@property (T@"CLPCReportingStatSelection",&,V_CPUClusterSelection) CPUClusterSelection;
@property (T@"CLPCReportingReadResult",&,V_CPUClusterReadResults) CPUClusterReadResults;
@property (T@"PLNSNotificationOperatorComposition",&,V_thermalMonitorListener) thermalMonitorListener;
@property (T@"PLStateTrackingComposition",&,V_stateTracker) stateTracker;
```

## Class methods

```
+[PLCLPCAgent entryEventIntervalDefinitions];
+[PLCLPCAgent entryEventNoneDefinitions];
+[PLCLPCAgent load];
+[PLCLPCAgent entryEventNoneLostPerformanceLookup];
+[PLCLPCAgent entryEventIntervalDefinitionLostPerformance];
+[PLCLPCAgent entryEventIntervalDefinitionTGCPUClusterAccumulators];
+[PLCLPCAgent entryEventIntervalDefinitionTGInfo];
+[PLCLPCAgent entryEventNoneAccumulatorsLookup];
+[PLCLPCAgent entryEventIntervalDefinitionAccumulators];
+[PLCLPCAgent entryEventIntervalDefinitionCPUClusterAccumulators];
+[PLCLPCAgent entryEventNoneCPUClusterAccumulatorsLookup];
+[PLCLPCAgent entryEventIntervalDefinitionTGAccumulators];
```

## Instance methods

```
-[PLCLPCAgent selection];
-[PLCLPCAgent setSelection:];
-[PLCLPCAgent CPUClusterReadResults];
-[PLCLPCAgent constructCache:forEntryKey:];
-[PLCLPCAgent logLookupTable:withEntryKey:];
-[PLCLPCAgent CPUClusterSelection];
-[PLCLPCAgent configureAccumulators];
-[PLCLPCAgent createLookupMaps];
-[PLCLPCAgent init];
-[PLCLPCAgent stateTracker];
-[PLCLPCAgent setReadResults:];
-[PLCLPCAgent setCPUClusterProvider:];
-[PLCLPCAgent configureTGAccumulators];
-[PLCLPCAgent configureTGCPUClusterAccumulators];
-[PLCLPCAgent initOperatorDependancies];
-[PLCLPCAgent logCLPCTGInfo:];
-[PLCLPCAgent setLastCPUClusterEntryDate:];
-[PLCLPCAgent provider];
-[PLCLPCAgent createLookupCache:];
-[PLCLPCAgent readResults];
-[PLCLPCAgent configureLostPerformance];
-[PLCLPCAgent configureCPUClusterAccumulators];
-[PLCLPCAgent logCLPCTGAccumulators:];
-[PLCLPCAgent setThermalMonitorListener:];
-[PLCLPCAgent setTenMinuteTimer:];
-[PLCLPCAgent tenMinuteTimer];
-[PLCLPCAgent lastEntryDate];
-[PLCLPCAgent logCLPCCPUClusterAccumulators:];
-[PLCLPCAgent setEntryKeys];
-[PLCLPCAgent setStateTracker:];
-[PLCLPCAgent configureTGInfo];
-[PLCLPCAgent setupStatsForCPUCluster];
-[PLCLPCAgent logCLPCStatsAccumulators:];
-[PLCLPCAgent setupStats];
-[PLCLPCAgent setupTimer];
-[PLCLPCAgent logCLPCLostPerformance:];
-[PLCLPCAgent addToLookupTableAndCache:forEntryKey:andLookupMap:];
-[PLCLPCAgent logCLPCTGCPUClusterAccumulators:];
-[PLCLPCAgent CPUClusterProvider];
-[PLCLPCAgent trimConditionsForEntryKey:forTrimDate:];
-[PLCLPCAgent setProvider:];
-[PLCLPCAgent setCPUClusterSelection:];
-[PLCLPCAgent thermalMonitorListener];
-[PLCLPCAgent setUpDisplayStateChangeNotification];
-[PLCLPCAgent setLastEntryDate:];
-[PLCLPCAgent setCPUClusterReadResults:];
-[PLCLPCAgent lastCPUClusterEntryDate];
```
