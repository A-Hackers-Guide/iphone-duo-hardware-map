# `SAService`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAMonitoringSessionManagerClientProtocol`, `SAFenceManagerClientProtocol`, `SAPowerLogClientProtocol`, `SAServiceServiceProtocol`, `SAGeoFenceRequestProtocol`, `SABluetoothScanRequestProtocol`, `SALocationRequestProtocol`, `SATimeEventRequestProtocol`, `SAFamiliarityIndexRequestProtocol`
- 12 instance variables, 16 properties, 44 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _clients;
@"SATime" _clock;
@"SADeviceRecord" _deviceRecord;
@"SAWithYouDetector" _withYouDetector;
@"SAMonitoringSessionManager" _monitoringSessionManager;
@"SAFenceManager" _fenceManager;
@"SATravelTypeClassifier" _travelTypeClassifier;
@"SAPowerLog" _powerLogger;
@"SAPersistenceManager" _persistenceManager;
@"SAFamiliarityManager" _familiarityManager;
@"SASuppressionManager" _suppressionManager;
@"SAAlertFeedbackManager" _alertFeedbackManager;
```

## Properties

```
@property (T@"NSHashTable",&,N,V_clients) clients;
@property (T@"SATime",&,N,V_clock) clock;
@property (T@"SADeviceRecord",&,N,V_deviceRecord) deviceRecord;
@property (T@"SAWithYouDetector",&,N,V_withYouDetector) withYouDetector;
@property (T@"SAMonitoringSessionManager",&,N,V_monitoringSessionManager) monitoringSessionManager;
@property (T@"SAFenceManager",&,N,V_fenceManager) fenceManager;
@property (T@"SATravelTypeClassifier",&,N,V_travelTypeClassifier) travelTypeClassifier;
@property (T@"SAPowerLog",&,N,V_powerLogger) powerLogger;
@property (T@"SAPersistenceManager",&,N,V_persistenceManager) persistenceManager;
@property (T@"SAFamiliarityManager",&,N,V_familiarityManager) familiarityManager;
@property (T@"SASuppressionManager",&,N,V_suppressionManager) suppressionManager;
@property (T@"SAAlertFeedbackManager",&,N,V_alertFeedbackManager) alertFeedbackManager;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SAService clients];
-[SAService clock];
-[SAService persistenceManager];
-[SAService setClock:];
-[SAService deviceRecord];
-[SAService ingestTAEvent:];
-[SAService setPersistenceManager:];
-[SAService removeClient:];
-[SAService withYouDetector];
-[SAService requestStateForRegion:];
-[SAService setAlertFeedbackManager:];
-[SAService setDeviceRecord:];
-[SAService setClients:];
-[SAService suppressionManager];
-[SAService travelTypeClassifier];
-[SAService addClient:];
-[SAService alertFeedbackManager];
-[SAService setWithYouDetector:];
-[SAService setSuppressionManager:];
-[SAService fenceManager];
-[SAService setTravelTypeClassifier:];
-[SAService setFenceManager:];
-[SAService powerLogger];
-[SAService enableMonitoringForSeparations:];
-[SAService setPowerLogger:];
-[SAService removeGeofence:];
-[SAService addGeofence:];
-[SAService cancelSATimeEventForAlarm:];
-[SAService familiarityManager];
-[SAService fetchHomeLocation];
-[SAService fetchLastVisit];
-[SAService initWithAnalytics:isReplay:audioAccessoryManager:defaults:];
-[SAService monitoringSessionManager];
-[SAService notifySeparationsForDevices:withLocation:withContext:];
-[SAService requestBluetoothScanForTypes:];
-[SAService requestFamiliarityIndexForDateInterval:lookbackInterval:location:distance:];
-[SAService requestLocationForType:];
-[SAService scheduleSATimeEvent:forAlarm:];
-[SAService setFamiliarityManager:];
-[SAService setMonitoringSessionManager:];
-[SAService startBackgroundScanning];
-[SAService stopBackgroundScanning];
-[SAService stopLongAggressiveScan];
-[SAService updatedMonitoringState:forDeviceUUID:];
```
