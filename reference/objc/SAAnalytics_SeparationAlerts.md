# `SAAnalytics`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAAnalyticsServiceProtocol`
- 33 instance variables, 37 properties, 93 instance methods, 0 class methods

## Instance variables

```
@"SAAnalyticsSettings" _settings;
B _isAllUsingSameSafe;
Q _numAlerts;
Q _numAlertsLeftBehind;
Q _numAlertsTraveling;
Q _numEnabled;
@"NSMutableDictionary" _numEnabledPerType;
Q _numSafe;
Q _numSafeInUse;
Q _numBTRequests;
Q _numBTLeftBehindRequests;
Q _numBTTravelingRequests;
Q _numBTRetryRequests;
Q _numGpsRequests;
Q _numWifiRequests;
Q _numTimers;
Q _numDevicesAtSafeExit;
Q _numUnsafe;
Q _numUnsafeWithLOI;
Q _numUnsafeWithoutLOI;
Q _aggActiveDuration;
Q _aggInSafeDuration;
Q _aggInUnsafeDuration;
Q _aggInTravelDuration;
d _aggScanDuration;
d _aggScanDurationForFindingRelevantItemsOnly;
Q _numBootstrapEvents;
Q _numBootstrappedSessionsValid;
Q _numBootstrappedSessionsInvalid;
@"NSDate" _lastActivated;
@"NSDate" _lastSafeEntry;
@"NSDate" _lastUnsafeEntry;
@"NSDate" _lastTravelStart;
```

## Properties

```
@property (TQ,N,V_numAlerts) numAlerts;
@property (TQ,N,V_numAlertsLeftBehind) numAlertsLeftBehind;
@property (TQ,N,V_numAlertsTraveling) numAlertsTraveling;
@property (TQ,N,V_numEnabled) numEnabled;
@property (T@"NSMutableDictionary",&,N,V_numEnabledPerType) numEnabledPerType;
@property (TQ,N,V_numSafe) numSafe;
@property (TQ,N,V_numSafeInUse) numSafeInUse;
@property (TB,N,V_isAllUsingSameSafe) isAllUsingSameSafe;
@property (TQ,N,V_numBTRequests) numBTRequests;
@property (TQ,N,V_numBTLeftBehindRequests) numBTLeftBehindRequests;
@property (TQ,N,V_numBTTravelingRequests) numBTTravelingRequests;
@property (TQ,N,V_numBTRetryRequests) numBTRetryRequests;
@property (TQ,N,V_numGpsRequests) numGpsRequests;
@property (TQ,N,V_numWifiRequests) numWifiRequests;
@property (TQ,N,V_numTimers) numTimers;
@property (TQ,N,V_numDevicesAtSafeExit) numDevicesAtSafeExit;
@property (TQ,N,V_numUnsafe) numUnsafe;
@property (TQ,N,V_numUnsafeWithLOI) numUnsafeWithLOI;
@property (TQ,N,V_numUnsafeWithoutLOI) numUnsafeWithoutLOI;
@property (TQ,N,V_aggActiveDuration) aggActiveDuration;
@property (TQ,N,V_aggInSafeDuration) aggInSafeDuration;
@property (TQ,N,V_aggInUnsafeDuration) aggInUnsafeDuration;
@property (TQ,N,V_aggInTravelDuration) aggInTravelDuration;
@property (Td,N,V_aggScanDuration) aggScanDuration;
@property (Td,N,V_aggScanDurationForFindingRelevantItemsOnly) aggScanDurationForFindingRelevantItemsOnly;
@property (TQ,N,V_numBootstrapEvents) numBootstrapEvents;
@property (TQ,N,V_numBootstrappedSessionsValid) numBootstrappedSessionsValid;
@property (TQ,N,V_numBootstrappedSessionsInvalid) numBootstrappedSessionsInvalid;
@property (T@"NSDate",&,N,V_lastActivated) lastActivated;
@property (T@"NSDate",&,N,V_lastSafeEntry) lastSafeEntry;
@property (T@"NSDate",&,N,V_lastUnsafeEntry) lastUnsafeEntry;
@property (T@"NSDate",&,N,V_lastTravelStart) lastTravelStart;
@property (Td,R,N) publishingInterval;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SAAnalytics numUnsafe];
-[SAAnalytics numDevicesAtSafeExit];
-[SAAnalytics submitAlertRateEvent:alertType:];
-[SAAnalytics numEnabledPerType];
-[SAAnalytics addWakeTimerRequest];
-[SAAnalytics setNumAlerts:];
-[SAAnalytics setLastUnsafeEntry:];
-[SAAnalytics setNumBTTravelingRequests:];
-[SAAnalytics submitEvent:content:];
-[SAAnalytics numUnsafeWithLOI];
-[SAAnalytics addBootstrapResult:invalidCount:];
-[SAAnalytics setInTravelState:];
-[SAAnalytics setAggScanDurationForFindingRelevantItemsOnly:];
-[SAAnalytics init];
-[SAAnalytics setNumBootstrappedSessionsValid:];
-[SAAnalytics numAlerts];
-[SAAnalytics setInUnsafeLocationState:];
-[SAAnalytics lastTravelStart];
-[SAAnalytics setAggScanDuration:];
-[SAAnalytics setNumBootstrapEvents:];
-[SAAnalytics submitDefaultAlertRateEvent];
-[SAAnalytics numBootstrappedSessionsInvalid];
-[SAAnalytics setNumAlertsLeftBehind:];
-[SAAnalytics setAggInUnsafeDuration:];
-[SAAnalytics addAggressiveScanRetryRequest];
-[SAAnalytics setNumBTRequests:];
-[SAAnalytics isAllUsingSameSafe];
-[SAAnalytics addVisit:withRadius:];
-[SAAnalytics numGpsRequests];
-[SAAnalytics resetAggregation];
-[SAAnalytics numEnabled];
-[SAAnalytics numAlertsTraveling];
-[SAAnalytics aggInUnsafeDuration];
-[SAAnalytics addScanDuration:];
-[SAAnalytics setNumEnabledPerType:];
-[SAAnalytics numSafe];
-[SAAnalytics numBTLeftBehindRequests];
-[SAAnalytics numUnsafeWithoutLOI];
-[SAAnalytics setLastTravelStart:];
-[SAAnalytics setNumEnabled:];
-[SAAnalytics setNumUnsafeWithLOI:];
-[SAAnalytics setLastActivated:];
-[SAAnalytics numWifiRequests];
-[SAAnalytics addPreArrivalAlertTime:didRejoinPriorExit:];
-[SAAnalytics submitBeaconMonitoringEvent:safeLocationsMatch:];
-[SAAnalytics numTimers];
-[SAAnalytics setNumBootstrappedSessionsInvalid:];
-[SAAnalytics addAggressiveScanRequest:];
-[SAAnalytics addSafeLocationFetchResultCount:];
-[SAAnalytics setNumDevicesAtSafeExit:];
-[SAAnalytics setNumSafeInUse:];
-[SAAnalytics aggInSafeDuration];
-[SAAnalytics setNumUnsafeWithoutLOI:];
-[SAAnalytics setInSafeLocationState:];
-[SAAnalytics setNumSafe:];
-[SAAnalytics setNumWifiRequests:];
-[SAAnalytics setNumBTRetryRequests:];
-[SAAnalytics aggActiveDuration];
-[SAAnalytics setNumBTLeftBehindRequests:];
-[SAAnalytics addDidSeparateWhileInVisit:didRejoinPriorExit:];
-[SAAnalytics numSafeInUse];
-[SAAnalytics setNumUnsafe:];
-[SAAnalytics addDeviceFetchResultCount:type1count:type2count:type3count:type4count:type5count:type6count:type7count:type8count:safeCount:usingSameSafe:];
-[SAAnalytics setLastSafeEntry:];
-[SAAnalytics setAggInSafeDuration:];
-[SAAnalytics publishAndResetAggregation];
-[SAAnalytics publishingInterval];
-[SAAnalytics addNumDevicesWithYou:];
-[SAAnalytics aggScanDurationForFindingRelevantItemsOnly];
-[SAAnalytics setAggInTravelDuration:];
-[SAAnalytics numBTTravelingRequests];
-[SAAnalytics addAlertWithContext:];
-[SAAnalytics aggScanDuration];
-[SAAnalytics numBootstrappedSessionsValid];
-[SAAnalytics setNumAlertsTraveling:];
-[SAAnalytics setAggActiveDuration:];
-[SAAnalytics setActiveState:];
-[SAAnalytics setIsAllUsingSameSafe:];
-[SAAnalytics logAnalyticsEvent:content:isSubmissionEnabled:];
-[SAAnalytics addWifiLocationRequest:];
-[SAAnalytics numBTRequests];
-[SAAnalytics addGpsLocationRequest:];
-[SAAnalytics addScanDurationForFindingRelevantItemsOnly:];
-[SAAnalytics numBTRetryRequests];
-[SAAnalytics setNumTimers:];
-[SAAnalytics lastSafeEntry];
-[SAAnalytics aggInTravelDuration];
-[SAAnalytics numBootstrapEvents];
-[SAAnalytics lastUnsafeEntry];
-[SAAnalytics numAlertsLeftBehind];
-[SAAnalytics initWithSettings:];
-[SAAnalytics setNumGpsRequests:];
-[SAAnalytics lastActivated];
```
