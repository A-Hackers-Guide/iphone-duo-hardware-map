# `SAWithYouDetector`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAWithYouDetectorServiceProtocol`, `SATimeClientProtocol`, `SATravelTypeClassifierClientProtocol`
- 29 instance variables, 29 properties, 97 instance methods, 2 class methods

## Instance variables

```
B _longScanIsOngoing;
B _requestedShortScan;
B _isNotifyWhileTravelingEnabled;
B _isPeriodicScansNeeded;
B _isInVehicularTravel;
B _isFindingRelevantDevices;
@"<SATimeServiceProtocol>" _clock;
@"<SABluetoothScanRequestProtocol>" _bluetoothScanner;
@"<SALocationRequestProtocol>" _locationRequester;
@"<SAAnalyticsServiceProtocol>" _analytics;
@"NSHashTable" _clients;
@"SADeviceRecord" _deviceRecord;
@"NSDate" _lastLongScanRequest;
@"NSDate" _lastStartOfScan;
@"NSDate" _lastEndOfScan;
d _lastScanRxTime;
@"NSDate" _nextOpportunisticScanDate;
@"NSUUID" _nextScheduledAlarm;
@"NSDate" _previousBufferEmptyTime;
@"NSDate" _initializationTime;
@"NSMutableSet" _relevantDevicesToFindDuringLongScan;
@"NSMutableDictionary" _foundDevicesDuringCurrentScan;
@"SAScanSessionTracker" _scanTracker;
@"NSDate" _lastRelevantDeviceFoundTime;
Q _lastLongScanContext;
Q _extraFoundHELECount;
Q _extraFoundNonHELECount;
@"NSDate" _lastExtraHELEFoundTime;
@"NSDate" _lastExtraNonHELEFoundTime;
```

## Properties

```
@property (T@"<SATimeServiceProtocol>",&,N,V_clock) clock;
@property (T@"<SABluetoothScanRequestProtocol>",W,N,V_bluetoothScanner) bluetoothScanner;
@property (T@"<SALocationRequestProtocol>",W,N,V_locationRequester) locationRequester;
@property (T@"<SAAnalyticsServiceProtocol>",&,N,V_analytics) analytics;
@property (T@"NSHashTable",&,N,V_clients) clients;
@property (T@"SADeviceRecord",&,N,V_deviceRecord) deviceRecord;
@property (TB,N,V_longScanIsOngoing) longScanIsOngoing;
@property (TB,N,V_requestedShortScan) requestedShortScan;
@property (T@"NSDate",&,N,V_lastLongScanRequest) lastLongScanRequest;
@property (T@"NSDate",&,N,V_lastStartOfScan) lastStartOfScan;
@property (T@"NSDate",&,N,V_lastEndOfScan) lastEndOfScan;
@property (Td,N,V_lastScanRxTime) lastScanRxTime;
@property (TB,N,V_isNotifyWhileTravelingEnabled) isNotifyWhileTravelingEnabled;
@property (TB,N,V_isPeriodicScansNeeded) isPeriodicScansNeeded;
@property (TB,N,V_isInVehicularTravel) isInVehicularTravel;
@property (T@"NSDate",&,N,V_nextOpportunisticScanDate) nextOpportunisticScanDate;
@property (T@"NSUUID",&,N,V_nextScheduledAlarm) nextScheduledAlarm;
@property (T@"NSDate",&,N,V_previousBufferEmptyTime) previousBufferEmptyTime;
@property (T@"NSDate",&,N,V_initializationTime) initializationTime;
@property (T@"NSMutableSet",&,N,V_relevantDevicesToFindDuringLongScan) relevantDevicesToFindDuringLongScan;
@property (T@"NSMutableDictionary",&,N,V_foundDevicesDuringCurrentScan) foundDevicesDuringCurrentScan;
@property (T@"SAScanSessionTracker",&,N,V_scanTracker) scanTracker;
@property (TB,N,V_isFindingRelevantDevices) isFindingRelevantDevices;
@property (T@"NSDate",&,N,V_lastRelevantDeviceFoundTime) lastRelevantDeviceFoundTime;
@property (TQ,N,V_lastLongScanContext) lastLongScanContext;
@property (TQ,N,V_extraFoundHELECount) extraFoundHELECount;
@property (TQ,N,V_extraFoundNonHELECount) extraFoundNonHELECount;
@property (T@"NSDate",&,N,V_lastExtraHELEFoundTime) lastExtraHELEFoundTime;
@property (T@"NSDate",&,N,V_lastExtraNonHELEFoundTime) lastExtraNonHELEFoundTime;
```

## Class methods

```
+[SAWithYouDetector convertSAWithYouStatusToString:];
+[SAWithYouDetector convertSAWithYouLongScanContextToString:];
```

## Instance methods

```
-[SAWithYouDetector clients];
-[SAWithYouDetector clock];
-[SAWithYouDetector analytics];
-[SAWithYouDetector setIsPeriodicScansNeeded:];
-[SAWithYouDetector setClock:];
-[SAWithYouDetector nextOpportunisticScanDate];
-[SAWithYouDetector setLastRelevantDeviceFoundTime:];
-[SAWithYouDetector deviceRecord];
-[SAWithYouDetector _finalizeToBeVerifiedStatus:];
-[SAWithYouDetector _shouldSkipScan];
-[SAWithYouDetector ingestTAEvent:];
-[SAWithYouDetector setAnalytics:];
-[SAWithYouDetector forceUpdateWithYouStatusToFindDevices:withContext:];
-[SAWithYouDetector previousBufferEmptyTime];
-[SAWithYouDetector setLastExtraNonHELEFoundTime:];
-[SAWithYouDetector requestedShortScan];
-[SAWithYouDetector removeClient:];
-[SAWithYouDetector isNotifyWhileTravelingEnabled];
-[SAWithYouDetector setLocationRequester:];
-[SAWithYouDetector initWithBluetoothScanner:locationRequester:deviceRecord:clock:analytics:];
-[SAWithYouDetector setDeviceRecord:];
-[SAWithYouDetector setRelevantDevicesToFindDuringLongScan:];
-[SAWithYouDetector _scheduleNextAlarmForScanAfterDate:];
-[SAWithYouDetector setClients:];
-[SAWithYouDetector updateExtraDeviceInformation:];
-[SAWithYouDetector requestScanIfNeeded];
-[SAWithYouDetector lastLongScanContext];
-[SAWithYouDetector setRequestedShortScan:];
-[SAWithYouDetector isPeriodicScansAllowed];
-[SAWithYouDetector initializationTime];
-[SAWithYouDetector _isStatusBitSetForRelatedDeviceWithShiftIndex:fromAdvertisement:];
-[SAWithYouDetector isInVehicularTravel];
-[SAWithYouDetector statusForDeviceWithUUID:];
-[SAWithYouDetector forceUpdateWithYouStatusWithShortScan:];
-[SAWithYouDetector setInitializationTime:];
-[SAWithYouDetector setExtraFoundNonHELECount:];
-[SAWithYouDetector setIsNotifyWhileTravelingEnabled:];
-[SAWithYouDetector setLastLongScanContext:];
-[SAWithYouDetector isFindingRelevantDevices];
-[SAWithYouDetector setScanTracker:];
-[SAWithYouDetector pausePeriodicScan];
-[SAWithYouDetector locationRequester];
-[SAWithYouDetector addClient:];
-[SAWithYouDetector allSAEnabledDevicesAreFound];
-[SAWithYouDetector lastEndOfScan];
-[SAWithYouDetector setLastEndOfScan:];
-[SAWithYouDetector setNextOpportunisticScanDate:];
-[SAWithYouDetector forceUpdateWithYouStatus];
-[SAWithYouDetector setFoundDevicesDuringCurrentScan:];
-[SAWithYouDetector sendScanContextToCoreAnalytics:isPartOfLongScan:scanDuration:scanRxTime:relevantOnlyScanDuration:foundExtraHELECount:extraHELEScanDuration:foundExtraNonHELECount:extraNonHELEScanDuration:longScanContext:allDevicesFound:];
-[SAWithYouDetector _wasDeviceConnectedDuringSession:];
-[SAWithYouDetector resumePeriodicScan];
-[SAWithYouDetector setLastScanRxTime:];
-[SAWithYouDetector _updateLastWithYouDateAndLocation:forCurrentDate:];
-[SAWithYouDetector foundDevicesDuringCurrentScan];
-[SAWithYouDetector lastExtraNonHELEFoundTime];
-[SAWithYouDetector lastExtraHELEFoundTime];
-[SAWithYouDetector setBluetoothScanner:];
-[SAWithYouDetector isPeriodicScansNeeded];
-[SAWithYouDetector extraFoundNonHELECount];
-[SAWithYouDetector _updateAllWithYouStatusOnScanEndedEvent:];
-[SAWithYouDetector resetAllWithYouStatusAndScanStates];
-[SAWithYouDetector setLastLongScanRequest:];
-[SAWithYouDetector lastRelevantDeviceFoundTime];
-[SAWithYouDetector setIsFindingRelevantDevices:];
-[SAWithYouDetector _deviceWithUUID:isWithYouDuringLongScanOnAdvertisement:];
-[SAWithYouDetector longScanIsOngoing];
-[SAWithYouDetector scanTracker];
-[SAWithYouDetector nextScheduledAlarm];
-[SAWithYouDetector setLongScanIsOngoing:];
-[SAWithYouDetector _isValidPartID:];
-[SAWithYouDetector _updateWithYouStatusOnAdvBufferEmptyEvent:];
-[SAWithYouDetector setNextScheduledAlarm:];
-[SAWithYouDetector setPreviousBufferEmptyTime:];
-[SAWithYouDetector _enoughTimeHasPassedSinceInitializationToMarkNotWithYouForDeviceUUID:];
-[SAWithYouDetector _updateWithYouStatusIfNecessaryOnConnectionEvent:];
-[SAWithYouDetector _notifyAllClientsOfWithYouStatusUpdate:forDeviceWithUUID:];
-[SAWithYouDetector lastLongScanRequest];
-[SAWithYouDetector bluetoothScanner];
-[SAWithYouDetector setExtraFoundHELECount:];
-[SAWithYouDetector setIsInVehicularTravel:];
-[SAWithYouDetector isExtraDeviceFound:onDate:];
-[SAWithYouDetector lastStartOfScan];
-[SAWithYouDetector getCurrentlyConnectedDevices];
-[SAWithYouDetector _updateWithYouStatusIfNecessaryOnAdvertisement:];
-[SAWithYouDetector _deviceIsWatch:];
-[SAWithYouDetector lastScanRxTime];
-[SAWithYouDetector _isRecentEnoughAdvertisementDate:forDeviceUUID:currentDate:];
-[SAWithYouDetector _updateWithYouStatusOfRelatedDevices:];
-[SAWithYouDetector allRelevantDevicesToFindAreFound];
-[SAWithYouDetector alarmFiredForUUID:];
-[SAWithYouDetector relevantDevicesToFindDuringLongScan];
-[SAWithYouDetector setLastStartOfScan:];
-[SAWithYouDetector didChangeTravelTypeFrom:to:];
-[SAWithYouDetector extraFoundHELECount];
-[SAWithYouDetector _maxAgeOfWithYouAdvertisementForDeviceUUID:];
-[SAWithYouDetector setLastExtraHELEFoundTime:];
```
