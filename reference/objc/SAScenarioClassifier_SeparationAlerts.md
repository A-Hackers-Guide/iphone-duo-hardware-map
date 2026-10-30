# `SAScenarioClassifier`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAScenarioClassifierServiceProtocol`, `SAFenceManagerClientProtocol`
- 11 instance variables, 15 properties, 41 instance methods, 1 class methods

## Instance variables

```
@"CLRegion" _currentUnsafeLocation;
@"CLRegion" _lastUnsafeLocation;
@"NSUUID" _deviceUuid;
Q _scenarioClassification;
@"NSDate" _scenarioChangeDate;
@"<SAFenceManagerRequestProtocol>" _delegate;
@"<SATimeServiceProtocol>" _timeDelegate;
@"NSHashTable" _clients;
@"NSMutableSet" _safeLocations;
@"NSMutableDictionary" _statesBySafeLocation;
@"CLCircularRegion" _currentVisit;
```

## Properties

```
@property (TQ,N,V_scenarioClassification) scenarioClassification;
@property (T@"NSUUID",C,N,V_deviceUuid) deviceUuid;
@property (T@"NSHashTable",&,N,V_clients) clients;
@property (T@"CLRegion",C,N,V_currentUnsafeLocation) currentUnsafeLocation;
@property (T@"CLRegion",C,N,V_lastUnsafeLocation) lastUnsafeLocation;
@property (T@"NSMutableSet",&,N,V_safeLocations) safeLocations;
@property (T@"NSMutableDictionary",&,N,V_statesBySafeLocation) statesBySafeLocation;
@property (T@"CLCircularRegion",C,N,V_currentVisit) currentVisit;
@property (T@"NSDate",R,C,N,V_scenarioChangeDate) scenarioChangeDate;
@property (T@"<SAFenceManagerRequestProtocol>",&,N,V_delegate) delegate;
@property (T@"<SATimeServiceProtocol>",&,N,V_timeDelegate) timeDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SAScenarioClassifier convertSAScenarioClassToString:];
```

## Instance methods

```
-[SAScenarioClassifier clients];
-[SAScenarioClassifier ingestTAEvent:];
-[SAScenarioClassifier removeClient:];
-[SAScenarioClassifier setClients:];
-[SAScenarioClassifier dealloc];
-[SAScenarioClassifier currentVisit];
-[SAScenarioClassifier addClient:];
-[SAScenarioClassifier setDelegate:];
-[SAScenarioClassifier setSafeLocations:];
-[SAScenarioClassifier delegate];
-[SAScenarioClassifier setCurrentVisit:];
-[SAScenarioClassifier safeLocations];
-[SAScenarioClassifier removeGeofence:];
-[SAScenarioClassifier _addSafeLocation:];
-[SAScenarioClassifier _addUnsafeLocation:];
-[SAScenarioClassifier _findSafeLocationWithUUID:];
-[SAScenarioClassifier _hasAllSafeLocationStatesKnown];
-[SAScenarioClassifier _isInsideAnySafeLocation];
-[SAScenarioClassifier _notifyAllClientsOfScenarioChangeFrom:to:];
-[SAScenarioClassifier _removeSafeLocation:];
-[SAScenarioClassifier _removeUnsafeLocation:];
-[SAScenarioClassifier _setNewScenarioClass:];
-[SAScenarioClassifier addGeofence:];
-[SAScenarioClassifier currentUnsafeLocation];
-[SAScenarioClassifier deviceUuid];
-[SAScenarioClassifier didDetermineState:forSafeLocation:forDevice:];
-[SAScenarioClassifier didDetermineState:forUnsafeLocation:forDevice:];
-[SAScenarioClassifier getCurrentTime];
-[SAScenarioClassifier initWithDeviceUuid:];
-[SAScenarioClassifier initWithDeviceUuid:scenarioClass:unsafeLocation:];
-[SAScenarioClassifier lastUnsafeLocation];
-[SAScenarioClassifier scenarioChangeDate];
-[SAScenarioClassifier scenarioClassification];
-[SAScenarioClassifier setCurrentUnsafeLocation:];
-[SAScenarioClassifier setDeviceUuid:];
-[SAScenarioClassifier setLastUnsafeLocation:];
-[SAScenarioClassifier setScenarioClassification:];
-[SAScenarioClassifier setStatesBySafeLocation:];
-[SAScenarioClassifier setTimeDelegate:];
-[SAScenarioClassifier statesBySafeLocation];
-[SAScenarioClassifier timeDelegate];
```
