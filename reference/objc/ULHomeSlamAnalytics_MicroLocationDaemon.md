# `ULHomeSlamAnalytics`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 31 instance methods, 1 class methods

## Instance variables

```
B _dependenciesSet;
@"NSMutableArray" _sleepWakeEventsQueue;
^{ULDatabaseStoreInterface=^^?} _dbStore;
@"ULEnvironment" _environment;
```

## Properties

```
@property (T^{ULDatabaseStoreInterface=^^?},N,V_dbStore) dbStore;
@property (T@"ULEnvironment",&,N,V_environment) environment;
@property (TB,N,V_dependenciesSet) dependenciesSet;
@property (T@"NSMutableArray",&,N,V_sleepWakeEventsQueue) sleepWakeEventsQueue;
```

## Class methods

```
+[ULHomeSlamAnalytics shared];
```

## Instance methods

```
-[ULHomeSlamAnalytics setEnvironment:];
-[ULHomeSlamAnalytics init];
-[ULHomeSlamAnalytics dealloc];
-[ULHomeSlamAnalytics environment];
-[ULHomeSlamAnalytics dbStore];
-[ULHomeSlamAnalytics logSleepStateEvent:atTimestamp:];
-[ULHomeSlamAnalytics dependenciesSet];
-[ULHomeSlamAnalytics logEventExitHomeLOIAtTimestamp:];
-[ULHomeSlamAnalytics _createBGTRequest];
-[ULHomeSlamAnalytics _logEventType:atTimestamp:];
-[ULHomeSlamAnalytics _registerForBackgroundTask];
-[ULHomeSlamAnalytics _runStopDetectionAnalyticsTask];
-[ULHomeSlamAnalytics _unregisterForBackgroundTask];
-[ULHomeSlamAnalytics handleSleepWakeMonitorEvent:];
-[ULHomeSlamAnalytics logEventAcceleratedTriggerChanged:AtTimestamp:];
-[ULHomeSlamAnalytics logEventDaemonStartedAtTimestamp:];
-[ULHomeSlamAnalytics logEventEnterHomeLOIAtTimestamp:];
-[ULHomeSlamAnalytics logEventMiLoEnabled:AtTimestamp:];
-[ULHomeSlamAnalytics logEventRequireIsLowLatencyChanged:AtTimestamp:];
-[ULHomeSlamAnalytics logEventScanConfigurationModeDisabledAtTimestamp:];
-[ULHomeSlamAnalytics logEventScanConfigurationModeEnabled:AtTimestamp:];
-[ULHomeSlamAnalytics logEventScanEventGeneratedAfterDisplayOnAtTimeStamp:];
-[ULHomeSlamAnalytics logEventScreenOffAtTimestamp:];
-[ULHomeSlamAnalytics logEventScreenOnAtTimestamp:];
-[ULHomeSlamAnalytics logEventSleepStateRegisterAtTimestamp:];
-[ULHomeSlamAnalytics resetDependencies];
-[ULHomeSlamAnalytics setDbStore:];
-[ULHomeSlamAnalytics setDependenciesAndRegisterToBackgroundTaskWithDB:environment:];
-[ULHomeSlamAnalytics setDependenciesSet:];
-[ULHomeSlamAnalytics setSleepWakeEventsQueue:];
-[ULHomeSlamAnalytics sleepWakeEventsQueue];
```
