# `PLDiscretionaryEnergyMonitor`

- Image: [`/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`](../userland/System__Library__PrivateFrameworks__PowerLog.framework__PowerLog.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 20 instance variables, 20 properties, 61 instance methods, 1 class methods

## Instance variables

```
B _isCharging;
B _debugMode;
@"PLDiscretionaryIntervalManager" _intervalManager;
@? _completionBlock;
d _lastReportedTotalEnergy;
d _lastReportedCPUEnergy;
d _lastReportedNetworkEnergy;
@"NSDictionary" _lastPowerlogResponse;
@"NSMutableArray" _quickEnergySnapshots;
@"NSObject<OS_dispatch_source>" _powerlogQueryTimer;
@"NSObject<OS_dispatch_source>" _quickEnergyAccumulatorTimer;
@"NSObject<OS_dispatch_queue>" _workQueue;
d _accumulatedCPUEnergy;
d _accumulatedNetworkEnergy;
d _powerlogEnergyDiff;
@"NSDate" _powerlogTimestampPrevious;
@"NSDate" _powerlogTimestampLast;
d _powerlogEnergyPrevious;
d _powerlogEnergyLast;
@"NSMutableDictionary" _mockData;
```

## Properties

```
@property (T@"PLDiscretionaryIntervalManager",&,V_intervalManager) intervalManager;
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (Td,N,V_lastReportedTotalEnergy) lastReportedTotalEnergy;
@property (Td,N,V_lastReportedCPUEnergy) lastReportedCPUEnergy;
@property (Td,N,V_lastReportedNetworkEnergy) lastReportedNetworkEnergy;
@property (T@"NSDictionary",&,N,V_lastPowerlogResponse) lastPowerlogResponse;
@property (T@"NSMutableArray",&,N,V_quickEnergySnapshots) quickEnergySnapshots;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_powerlogQueryTimer) powerlogQueryTimer;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_quickEnergyAccumulatorTimer) quickEnergyAccumulatorTimer;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (Td,V_accumulatedCPUEnergy) accumulatedCPUEnergy;
@property (Td,V_accumulatedNetworkEnergy) accumulatedNetworkEnergy;
@property (Td,V_powerlogEnergyDiff) powerlogEnergyDiff;
@property (T@"NSDate",&,V_powerlogTimestampPrevious) powerlogTimestampPrevious;
@property (T@"NSDate",&,V_powerlogTimestampLast) powerlogTimestampLast;
@property (Td,V_powerlogEnergyPrevious) powerlogEnergyPrevious;
@property (Td,V_powerlogEnergyLast) powerlogEnergyLast;
@property (TB,V_isCharging) isCharging;
@property (TB,V_debugMode) debugMode;
@property (T@"NSMutableDictionary",&,V_mockData) mockData;
```

## Class methods

```
+[PLDiscretionaryEnergyMonitor getDiscretionaryEnergyBudget];
```

## Instance methods

```
-[PLDiscretionaryEnergyMonitor isCharging];
-[PLDiscretionaryEnergyMonitor setWorkQueue:];
-[PLDiscretionaryEnergyMonitor setDebugMode:];
-[PLDiscretionaryEnergyMonitor debugMode];
-[PLDiscretionaryEnergyMonitor powerlogEnergyPrevious];
-[PLDiscretionaryEnergyMonitor runCompletionBlockWithEnergyResponse:];
-[PLDiscretionaryEnergyMonitor updateMockData:];
-[PLDiscretionaryEnergyMonitor setPowerlogTimestampLast:];
-[PLDiscretionaryEnergyMonitor setCompletionBlock:];
-[PLDiscretionaryEnergyMonitor completionBlock];
-[PLDiscretionaryEnergyMonitor setIsCharging:];
-[PLDiscretionaryEnergyMonitor lastReportedNetworkEnergy];
-[PLDiscretionaryEnergyMonitor setPowerlogTimestampPrevious:];
-[PLDiscretionaryEnergyMonitor setIntervalManager:];
-[PLDiscretionaryEnergyMonitor setStateForNotification:withState:];
-[PLDiscretionaryEnergyMonitor quickEnergyAccumulatorTimer];
-[PLDiscretionaryEnergyMonitor setPowerlogQueryTimer:];
-[PLDiscretionaryEnergyMonitor workQueue];
-[PLDiscretionaryEnergyMonitor initWithDebugMode:andMockData:andCompletionBlock:];
-[PLDiscretionaryEnergyMonitor reportChargingStatus:];
-[PLDiscretionaryEnergyMonitor setLastReportedNetworkEnergy:];
-[PLDiscretionaryEnergyMonitor generateEnergyReport];
-[PLDiscretionaryEnergyMonitor getPowerlogEnergySum:];
-[PLDiscretionaryEnergyMonitor createPowerlogQueryTimer];
-[PLDiscretionaryEnergyMonitor logPowerlogResponse:];
-[PLDiscretionaryEnergyMonitor powerlogTimestampPrevious];
-[PLDiscretionaryEnergyMonitor testHighVolumeStartStopReporting:withInfo:withNumIterations:];
-[PLDiscretionaryEnergyMonitor powerlogTimestampLast];
-[PLDiscretionaryEnergyMonitor setQuickEnergySnapshots:];
-[PLDiscretionaryEnergyMonitor lastReportedTotalEnergy];
-[PLDiscretionaryEnergyMonitor setupNotificationListeners];
-[PLDiscretionaryEnergyMonitor incrementCPUEnergy:];
-[PLDiscretionaryEnergyMonitor createQuickEnergyAccumulatorTimer];
-[PLDiscretionaryEnergyMonitor accumulatedNetworkEnergy];
-[PLDiscretionaryEnergyMonitor powerlogEnergyLast];
-[PLDiscretionaryEnergyMonitor setLastReportedCPUEnergy:];
-[PLDiscretionaryEnergyMonitor setAccumulatedNetworkEnergy:];
-[PLDiscretionaryEnergyMonitor setPowerlogEnergyPrevious:];
-[PLDiscretionaryEnergyMonitor accumulatedCPUEnergy];
-[PLDiscretionaryEnergyMonitor reportStartEvent:withInfo:];
-[PLDiscretionaryEnergyMonitor reportStopEvent:withInfo:];
-[PLDiscretionaryEnergyMonitor initWithCompletionBlock:];
-[PLDiscretionaryEnergyMonitor mockData];
-[PLDiscretionaryEnergyMonitor setAccumulatedCPUEnergy:];
-[PLDiscretionaryEnergyMonitor setPowerlogEnergyLast:];
-[PLDiscretionaryEnergyMonitor powerlogQueryTimer];
-[PLDiscretionaryEnergyMonitor lastReportedCPUEnergy];
-[PLDiscretionaryEnergyMonitor logEnergyReport:];
-[PLDiscretionaryEnergyMonitor setLastPowerlogResponse:];
-[PLDiscretionaryEnergyMonitor quickEnergySnapshots];
-[PLDiscretionaryEnergyMonitor queryPowerlogForDiscretionaryEnergy];
-[PLDiscretionaryEnergyMonitor logQuickEnergySnapshots];
-[PLDiscretionaryEnergyMonitor setQuickEnergyAccumulatorTimer:];
-[PLDiscretionaryEnergyMonitor lastPowerlogResponse];
-[PLDiscretionaryEnergyMonitor incrementNetworkEnergy:];
-[PLDiscretionaryEnergyMonitor accumulateQuickEnergy];
-[PLDiscretionaryEnergyMonitor powerlogEnergyDiff];
-[PLDiscretionaryEnergyMonitor setLastReportedTotalEnergy:];
-[PLDiscretionaryEnergyMonitor setMockData:];
-[PLDiscretionaryEnergyMonitor setPowerlogEnergyDiff:];
-[PLDiscretionaryEnergyMonitor intervalManager];
```
