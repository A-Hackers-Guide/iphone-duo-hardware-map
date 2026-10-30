# `CWFJITTDImpactEstimator`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 20 instance variables, 20 properties, 63 instance methods, 1 class methods

## Instance variables

```
B __legacyAccountingComplete;
@? _scanForNetworkHandler;
@? _gatherCellularDataStats;
q __rssi;
q __activity;
@"CWFScanResult" __tdNetwork;
@"NSDate" __startTime;
@"NSObject<OS_dispatch_queue>" __timerQueue;
@"NSObject<OS_dispatch_queue>" __serviceQueue;
q __boundaryTime;
@"NSObject<OS_dispatch_source>" __boundaryTimer;
@"NSObject<OS_dispatch_source>" __periodicTimer;
@"NSNumber" __totalCellularInBytes;
@"NSNumber" __totalCellularOutBytes;
@"NSNumber" __totalCellularInPackets;
@"NSNumber" __totalCellularOutPackets;
@"NSDate" __lastSubmissionTimePreAJ;
@"NSDate" __lastSubmissionTimePostTD;
@"NSDictionary" __previousCellularDataUsageInPostTD;
@"NSDictionary" __cellularDataUsageInLegacyBoundary;
```

## Properties

```
@property (Tq,N,V__rssi) _rssi;
@property (Tq,N,V__activity) _activity;
@property (T@"CWFScanResult",&,N,V__tdNetwork) _tdNetwork;
@property (T@"NSDate",&,N,V__startTime) _startTime;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V__timerQueue) _timerQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V__serviceQueue) _serviceQueue;
@property (Tq,N,V__boundaryTime) _boundaryTime;
@property (T@"NSObject<OS_dispatch_source>",&,N,V__boundaryTimer) _boundaryTimer;
@property (T@"NSObject<OS_dispatch_source>",&,N,V__periodicTimer) _periodicTimer;
@property (T@"NSNumber",&,N,V__totalCellularInBytes) _totalCellularInBytes;
@property (T@"NSNumber",&,N,V__totalCellularOutBytes) _totalCellularOutBytes;
@property (T@"NSNumber",&,N,V__totalCellularInPackets) _totalCellularInPackets;
@property (T@"NSNumber",&,N,V__totalCellularOutPackets) _totalCellularOutPackets;
@property (T@"NSDate",&,N,V__lastSubmissionTimePreAJ) _lastSubmissionTimePreAJ;
@property (TB,N,V__legacyAccountingComplete) _legacyAccountingComplete;
@property (T@"NSDate",&,N,V__lastSubmissionTimePostTD) _lastSubmissionTimePostTD;
@property (T@"NSDictionary",&,N,V__previousCellularDataUsageInPostTD) _previousCellularDataUsageInPostTD;
@property (T@"NSDictionary",&,N,V__cellularDataUsageInLegacyBoundary) _cellularDataUsageInLegacyBoundary;
@property (T@?,C,V_scanForNetworkHandler) scanForNetworkHandler;
@property (T@?,C,V_gatherCellularDataStats) gatherCellularDataStats;
```

## Class methods

```
+[CWFJITTDImpactEstimator initJITTDImpactEstimator];
```

## Instance methods

```
-[CWFJITTDImpactEstimator _startTime];
-[CWFJITTDImpactEstimator cancelBoundaryTimer];
-[CWFJITTDImpactEstimator _cellularDataUsageInLegacyBoundary];
-[CWFJITTDImpactEstimator set_activity:];
-[CWFJITTDImpactEstimator init];
-[CWFJITTDImpactEstimator set_cellularDataUsageInLegacyBoundary:];
-[CWFJITTDImpactEstimator set_lastSubmissionTimePostTD:];
-[CWFJITTDImpactEstimator set_previousCellularDataUsageInPostTD:];
-[CWFJITTDImpactEstimator _lastSubmissionTimePreAJ];
-[CWFJITTDImpactEstimator _lastSubmissionTimePostTD];
-[CWFJITTDImpactEstimator set_totalCellularInBytes:];
-[CWFJITTDImpactEstimator _totalCellularOutPackets];
-[CWFJITTDImpactEstimator setScanForNetworkHandler:];
-[CWFJITTDImpactEstimator _timerQueue];
-[CWFJITTDImpactEstimator set_startTime:];
-[CWFJITTDImpactEstimator _tdNetwork];
-[CWFJITTDImpactEstimator set_totalCellularInPackets:];
-[CWFJITTDImpactEstimator invalidate];
-[CWFJITTDImpactEstimator set_periodicTimer:];
-[CWFJITTDImpactEstimator __stopCellularDataUsageAccountingPostTD];
-[CWFJITTDImpactEstimator notifyScanResult:withError:];
-[CWFJITTDImpactEstimator _activity];
-[CWFJITTDImpactEstimator set_boundaryTime:];
-[CWFJITTDImpactEstimator computeDataUsageInCurrentSession:];
-[CWFJITTDImpactEstimator _totalCellularOutBytes];
-[CWFJITTDImpactEstimator _previousCellularDataUsageInPostTD];
-[CWFJITTDImpactEstimator notifyAJDelayedOnlyDueToJITTD];
-[CWFJITTDImpactEstimator _boundaryTimer];
-[CWFJITTDImpactEstimator postCellularDataUsageAccountingPreAJ:];
-[CWFJITTDImpactEstimator _periodicTimer];
-[CWFJITTDImpactEstimator cancelPeriodicTimer];
-[CWFJITTDImpactEstimator setGatherCellularDataStats:];
-[CWFJITTDImpactEstimator set_legacyAccountingComplete:];
-[CWFJITTDImpactEstimator storeCellularDataUsage:];
-[CWFJITTDImpactEstimator startCellularDataUsageAccountingDelayedAJ:withMaxRSSI:forNetwork:];
-[CWFJITTDImpactEstimator issueFullBandScan];
-[CWFJITTDImpactEstimator twoSigFig:];
-[CWFJITTDImpactEstimator gatherCellularDataStats];
-[CWFJITTDImpactEstimator set_tdNetwork:];
-[CWFJITTDImpactEstimator resetStores];
-[CWFJITTDImpactEstimator scanForNetworkHandler];
-[CWFJITTDImpactEstimator _totalCellularInBytes];
-[CWFJITTDImpactEstimator set_totalCellularOutPackets:];
-[CWFJITTDImpactEstimator set_rssi:];
-[CWFJITTDImpactEstimator stopAccounting];
-[CWFJITTDImpactEstimator _legacyAccountingComplete];
-[CWFJITTDImpactEstimator gatherCellularDataUsageSoFar:];
-[CWFJITTDImpactEstimator _serviceQueue];
-[CWFJITTDImpactEstimator set_serviceQueue:];
-[CWFJITTDImpactEstimator _totalCellularInPackets];
-[CWFJITTDImpactEstimator stopCellularDataUsageAccountingPostTD];
-[CWFJITTDImpactEstimator set_boundaryTimer:];
-[CWFJITTDImpactEstimator stopCellularDataUsageAccountingDelayedAJ];
-[CWFJITTDImpactEstimator postCellularDataUsageAccoutingPostTD:];
-[CWFJITTDImpactEstimator set_timerQueue:];
-[CWFJITTDImpactEstimator canSubmitToCA:];
-[CWFJITTDImpactEstimator _boundaryTime];
-[CWFJITTDImpactEstimator setupPeriodicTimerForScan];
-[CWFJITTDImpactEstimator set_totalCellularOutBytes:];
-[CWFJITTDImpactEstimator startCellularDataUsageAccountingPostTD:withMinRSSI:];
-[CWFJITTDImpactEstimator checkCellularDataSanity:];
-[CWFJITTDImpactEstimator _rssi];
-[CWFJITTDImpactEstimator set_lastSubmissionTimePreAJ:];
```
