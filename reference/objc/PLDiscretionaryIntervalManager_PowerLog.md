# `PLDiscretionaryIntervalManager`

- Image: [`/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`](../userland/System__Library__PrivateFrameworks__PowerLog.framework__PowerLog.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _quickEnergyEnabled;
@"NSMutableDictionary" _identifierToDiscretionaryIntervals;
@"NSMutableDictionary" _activityNameToInvolvedIdentifiers;
@"NSObject<OS_dispatch_source>" _openIntervalTimer;
@"NSObject<OS_dispatch_source>" _powerlogReportTimer;
@"PLDiscretionaryEnergyMonitor" _discretionaryEnergyMonitor;
@"NSMutableDictionary" _mockData;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_identifierToDiscretionaryIntervals) identifierToDiscretionaryIntervals;
@property (T@"NSMutableDictionary",&,V_activityNameToInvolvedIdentifiers) activityNameToInvolvedIdentifiers;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_openIntervalTimer) openIntervalTimer;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_powerlogReportTimer) powerlogReportTimer;
@property (T@"PLDiscretionaryEnergyMonitor",W,N,V_discretionaryEnergyMonitor) discretionaryEnergyMonitor;
@property (TB,N,V_quickEnergyEnabled) quickEnergyEnabled;
@property (T@"NSMutableDictionary",&,V_mockData) mockData;
```

## Instance methods

```
-[PLDiscretionaryIntervalManager mockData];
-[PLDiscretionaryIntervalManager setMockData:];
-[PLDiscretionaryIntervalManager activityNameToInvolvedIdentifiers];
-[PLDiscretionaryIntervalManager coalesceIntervals:];
-[PLDiscretionaryIntervalManager createOpenIntervalTimer];
-[PLDiscretionaryIntervalManager createPowerlogReportTimer];
-[PLDiscretionaryIntervalManager disableQuickEnergy];
-[PLDiscretionaryIntervalManager discretionaryEnergyMonitor];
-[PLDiscretionaryIntervalManager enableQuickEnergy];
-[PLDiscretionaryIntervalManager handleOpenIntervalTimer];
-[PLDiscretionaryIntervalManager handlePowerlogReportTimer];
-[PLDiscretionaryIntervalManager handleStartEvent:withInfo:];
-[PLDiscretionaryIntervalManager handleStopEvent:withInfo:];
-[PLDiscretionaryIntervalManager identifierToDiscretionaryIntervals];
-[PLDiscretionaryIntervalManager initWithEnergyMonitor:andMockData:];
-[PLDiscretionaryIntervalManager logActivityNameToInvolvedIdentifiers];
-[PLDiscretionaryIntervalManager logDiscretionaryIntervals];
-[PLDiscretionaryIntervalManager openIntervalTimer];
-[PLDiscretionaryIntervalManager powerlogReportTimer];
-[PLDiscretionaryIntervalManager quickEnergyEnabled];
-[PLDiscretionaryIntervalManager reportIntervalsToPowerlog];
-[PLDiscretionaryIntervalManager reportQuickEnergyForInterval:withIdentifier:andAdjustSnapshotToNow:];
-[PLDiscretionaryIntervalManager setActivityNameToInvolvedIdentifiers:];
-[PLDiscretionaryIntervalManager setDiscretionaryEnergyMonitor:];
-[PLDiscretionaryIntervalManager setIdentifierToDiscretionaryIntervals:];
-[PLDiscretionaryIntervalManager setOpenIntervalTimer:];
-[PLDiscretionaryIntervalManager setPowerlogReportTimer:];
-[PLDiscretionaryIntervalManager setQuickEnergyEnabled:];
```
