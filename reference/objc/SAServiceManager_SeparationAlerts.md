# `SAServiceManager`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAServiceServiceProtocol`, `SAServiceClientProtocol`
- 15 instance variables, 16 properties, 56 instance methods, 2 class methods

## Instance variables

```
@"SPBeaconManager" _beaconManager;
@"SPOwnerSession" _ownerSession;
@"NSObject<SPSeparationMonitoringProtocol>" _separationMonitoringSession;
B _beaconGroupComplete;
B _beaconGroupSafeLocationsMatch;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSHashTable" _clients;
@"SAService" _service;
@"SATrialManager" _trialManager;
@"SAAnalytics" _analytics;
@"SAAudioAccessory" _audioAcccessory;
@"NSDate" _nextAnalyticsSubmission;
@"RTRoutineManager" _routineManager;
@"TADefaults" _defaults;
@? _scheduledMetricSubmissionBlock;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSHashTable",&,N,V_clients) clients;
@property (T@"SAService",&,N,V_service) service;
@property (T@"SATrialManager",&,N,V_trialManager) trialManager;
@property (T@"SAAnalytics",&,N,V_analytics) analytics;
@property (T@"SAAudioAccessory",&,N,V_audioAcccessory) audioAcccessory;
@property (T@"NSDate",&,N,V_nextAnalyticsSubmission) nextAnalyticsSubmission;
@property (T@"RTRoutineManager",&,N,V_routineManager) routineManager;
@property (T@"TADefaults",&,N,V_defaults) defaults;
@property (TB,N,V_beaconGroupComplete) beaconGroupComplete;
@property (TB,N,V_beaconGroupSafeLocationsMatch) beaconGroupSafeLocationsMatch;
@property (T@?,C,N,V_scheduledMetricSubmissionBlock) scheduledMetricSubmissionBlock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SAServiceManager convertBeaconToDeviceType:];
+[SAServiceManager convertCLReferenceFrameToSAReferenceFrame:];
```

## Instance methods

```
-[SAServiceManager setDefaults:];
-[SAServiceManager clients];
-[SAServiceManager _fetchAndIngestLastVisit];
-[SAServiceManager analytics];
-[SAServiceManager defaults];
-[SAServiceManager routineManager];
-[SAServiceManager setTrialManager:];
-[SAServiceManager ingestTAEvent:];
-[SAServiceManager separationAlertsService:requestStateForRegion:];
-[SAServiceManager initWithQueue:];
-[SAServiceManager setAnalytics:];
-[SAServiceManager setRoutineManager:];
-[SAServiceManager removeClient:];
-[SAServiceManager separationAlertsService:addGeofence:];
-[SAServiceManager nextAnalyticsSubmission];
-[SAServiceManager separationAlertsService:enableMonitoringForSeparations:];
-[SAServiceManager setService:];
-[SAServiceManager scheduleBeaconGroupMetricSubmission];
-[SAServiceManager setClients:];
-[SAServiceManager trialManager];
-[SAServiceManager _startMonitoringAndIngestingPredictedContexts];
-[SAServiceManager separationAlertsServiceFetchHomeLocation:];
-[SAServiceManager dealloc];
-[SAServiceManager audioAcccessory];
-[SAServiceManager queue];
-[SAServiceManager _stopMonitoringPredictedContexts];
-[SAServiceManager didFetchAllDevices:];
-[SAServiceManager addClient:];
-[SAServiceManager setNextAnalyticsSubmission:];
-[SAServiceManager _ingestVisit:];
-[SAServiceManager scheduledMetricSubmissionBlock];
-[SAServiceManager separationAlertsService:notifySeparationsForDevices:withLocation:withContext:];
-[SAServiceManager separationAlertsService:requestLocationForType:];
-[SAServiceManager separationAlertsServiceStopBackgroundScanning:];
-[SAServiceManager _fetchAndIngestHomeLocation];
-[SAServiceManager service];
-[SAServiceManager setBeaconGroupSafeLocationsMatch:];
-[SAServiceManager separationAlertsServiceFetchLastVisit:];
-[SAServiceManager separationAlertsService:removeGeofence:];
-[SAServiceManager setScheduledMetricSubmissionBlock:];
-[SAServiceManager beaconGroupComplete];
-[SAServiceManager separationAlertsService:requestFamiliarityIndexForDateInterval:lookbackInterval:location:distance:];
-[SAServiceManager separationAlertsServiceStartBackgroundScanning:];
-[SAServiceManager beaconGroupSafeLocationsMatch];
-[SAServiceManager handleTrialConfigurationUpdate:forNamespace:];
-[SAServiceManager setupTrialManager];
-[SAServiceManager setAudioAcccessory:];
-[SAServiceManager initWithQueue:defaults:];
-[SAServiceManager setBeaconGroupComplete:];
-[SAServiceManager separationAlertsService:cancelSATimeEventForAlarm:];
-[SAServiceManager separationAlertsServiceStopLongAggressiveScan:];
-[SAServiceManager _ingestPredictedContexts:];
-[SAServiceManager didFetchAllSafeLocations:];
-[SAServiceManager setQueue:];
-[SAServiceManager separationAlertsService:requestBluetoothScanForTypes:];
-[SAServiceManager separationAlertsService:scheduleSATimeEvent:forAlarm:];
```
