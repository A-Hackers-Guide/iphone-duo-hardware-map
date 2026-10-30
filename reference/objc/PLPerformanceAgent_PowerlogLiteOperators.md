# `PLPerformanceAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 8 instance variables, 8 properties, 37 instance methods, 14 class methods

## Instance variables

```
i _randomSample;
i _sampleCounter;
@"PLEntryNotificationOperatorComposition" _batteryLevelChanged;
@"PLEntryNotificationOperatorComposition" _batteryEntryLogged;
@"PLNSNotificationOperatorComposition" _dailyTaskNotification;
@"PLCFNotificationOperatorComposition" _llmOverheadNotification;
@"PLCFNotificationOperatorComposition" _vmTuningNotification;
@"NSSet" _systemMemoryProcessNames;
```

## Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryLevelChanged) batteryLevelChanged;
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryEntryLogged) batteryEntryLogged;
@property (T@"PLNSNotificationOperatorComposition",&,V_dailyTaskNotification) dailyTaskNotification;
@property (T@"PLCFNotificationOperatorComposition",&,V_llmOverheadNotification) llmOverheadNotification;
@property (T@"PLCFNotificationOperatorComposition",&,V_vmTuningNotification) vmTuningNotification;
@property (Ti,V_randomSample) randomSample;
@property (Ti,V_sampleCounter) sampleCounter;
@property (T@"NSSet",R,V_systemMemoryProcessNames) systemMemoryProcessNames;
```

## Class methods

```
+[PLPerformanceAgent entryEventIntervalDefinitions];
+[PLPerformanceAgent entryEventPointDefinitions];
+[PLPerformanceAgent load];
+[PLPerformanceAgent entryEventPointDefinitionDiskUsage];
+[PLPerformanceAgent entryEventPointDefinitionAPFSFragmentation];
+[PLPerformanceAgent entryEventPointDefinitionJetsamPriority];
+[PLPerformanceAgent entryEventIntervalDefinitionExperiment];
+[PLPerformanceAgent entryEventPointDefinitionVMTunables];
+[PLPerformanceAgent entryEventPointDefinitionDiskFragmentation];
+[PLPerformanceAgent shouldCreateJetsamPriorityTable];
+[PLPerformanceAgent entryEventPointDefinitionSystemMemory];
+[PLPerformanceAgent entryEventPointDefinitionRollout];
+[PLPerformanceAgent entryEventPointDefinitionIdleReaper];
+[PLPerformanceAgent entryEventPointDefinitionCodePrewarming];
```

## Instance methods

```
-[PLPerformanceAgent setRandomSample:];
-[PLPerformanceAgent sampleCounter];
-[PLPerformanceAgent countMachPort:];
-[PLPerformanceAgent init];
-[PLPerformanceAgent logEventPointJetsamPrority];
-[PLPerformanceAgent logEventPointAPFSFragmentation];
-[PLPerformanceAgent vmTuningNotification];
-[PLPerformanceAgent initOperatorDependancies];
-[PLPerformanceAgent setVmTuningNotification:];
-[PLPerformanceAgent countFD:];
-[PLPerformanceAgent descriptionForMemoryPressure:];
-[PLPerformanceAgent logEventPointDiskFragmentation];
-[PLPerformanceAgent setBatteryEntryLogged:];
-[PLPerformanceAgent llmOverheadNotification];
-[PLPerformanceAgent logEventPointDiskUsage];
-[PLPerformanceAgent logEventPointVMStats];
-[PLPerformanceAgent logEventPointSystemMemory:];
-[PLPerformanceAgent convertCodePrewarmingSysctl:];
-[PLPerformanceAgent logEventPointSystemMemoryPerProcess:];
-[PLPerformanceAgent setSampleCounter:];
-[PLPerformanceAgent logEventIntervalExperiment];
-[PLPerformanceAgent logSharedCacheStatisticsToCA:];
-[PLPerformanceAgent logEventPointRollout];
-[PLPerformanceAgent setDailyTaskNotification:];
-[PLPerformanceAgent systemMemoryProcessNames];
-[PLPerformanceAgent logEventPointCodePrewarming];
-[PLPerformanceAgent logEventPointVMTunables];
-[PLPerformanceAgent logSystemMemoryToCA:];
-[PLPerformanceAgent setBatteryLevelChanged:];
-[PLPerformanceAgent setLlmOverheadNotification:];
-[PLPerformanceAgent batteryEntryLogged];
-[PLPerformanceAgent randomSample];
-[PLPerformanceAgent log];
-[PLPerformanceAgent logEventPointIdleReaper];
-[PLPerformanceAgent logEventPointAPFSFragmentationWithContainer:];
-[PLPerformanceAgent dailyTaskNotification];
-[PLPerformanceAgent batteryLevelChanged];
```
