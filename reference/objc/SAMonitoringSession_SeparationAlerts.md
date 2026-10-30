# `SAMonitoringSession`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 24 instance variables, 24 properties, 56 instance methods, 1 class methods

## Instance variables

```
B _earlyVehicularTrigger;
B _earlyAirplaneTrigger;
B _foundAtLocation;
B _previouslySuppressedDueToPLC;
B _foundAtLocationBeforePLCSuppression;
B _scanRetryInProgress;
B _wasBootstrapped;
B _hasTransitionedSinceBootstrap;
@"NSUUID" _deviceUUID;
@"CLCircularRegion" _geofence;
Q _state;
Q _scenario;
@"NSDate" _trackedTravelingStartDate;
@"NSDate" _travelingGeofenceExitDate;
@"NSDate" _earlyVehicularStateChangeDate;
@"TALocationLite" _trackedTravelingStartLocation;
@"TALocationLite" _firstNotWithYouLocation;
@"SAScenarioClassifier" _scenarioClassifier;
@"NSDate" _lastAlertDateInCurrentTravelingSession;
q _btHintCountDuringTravel;
q _scanRetryCount;
d _cumulativeScanRxTime;
@"NSDate" _caLastStateTransition;
@"CLLocation" _caSeparationLocation;
```

## Properties

```
@property (T@"NSUUID",&,N,V_deviceUUID) deviceUUID;
@property (T@"CLCircularRegion",&,N,V_geofence) geofence;
@property (TQ,N,V_state) state;
@property (TQ,N,V_scenario) scenario;
@property (T@"NSDate",&,N,V_trackedTravelingStartDate) trackedTravelingStartDate;
@property (T@"NSDate",&,N,V_travelingGeofenceExitDate) travelingGeofenceExitDate;
@property (T@"NSDate",&,N,V_earlyVehicularStateChangeDate) earlyVehicularStateChangeDate;
@property (T@"TALocationLite",&,N,V_trackedTravelingStartLocation) trackedTravelingStartLocation;
@property (T@"TALocationLite",&,N,V_firstNotWithYouLocation) firstNotWithYouLocation;
@property (T@"SAScenarioClassifier",&,N,V_scenarioClassifier) scenarioClassifier;
@property (TB,N,V_earlyVehicularTrigger) earlyVehicularTrigger;
@property (TB,N,V_earlyAirplaneTrigger) earlyAirplaneTrigger;
@property (T@"NSDate",&,N,V_lastAlertDateInCurrentTravelingSession) lastAlertDateInCurrentTravelingSession;
@property (TB,N,V_foundAtLocation) foundAtLocation;
@property (TB,N,V_previouslySuppressedDueToPLC) previouslySuppressedDueToPLC;
@property (TB,N,V_foundAtLocationBeforePLCSuppression) foundAtLocationBeforePLCSuppression;
@property (Tq,N,V_btHintCountDuringTravel) btHintCountDuringTravel;
@property (Tq,N,V_scanRetryCount) scanRetryCount;
@property (TB,N,V_scanRetryInProgress) scanRetryInProgress;
@property (Td,N,V_cumulativeScanRxTime) cumulativeScanRxTime;
@property (T@"NSDate",&,N,V_caLastStateTransition) caLastStateTransition;
@property (T@"CLLocation",&,N,V_caSeparationLocation) caSeparationLocation;
@property (TB,N,V_wasBootstrapped) wasBootstrapped;
@property (TB,N,V_hasTransitionedSinceBootstrap) hasTransitionedSinceBootstrap;
```

## Class methods

```
+[SAMonitoringSession supportsSecureCoding];
```

## Instance methods

```
-[SAMonitoringSession deviceUUID];
-[SAMonitoringSession setState:];
-[SAMonitoringSession setDeviceUUID:];
-[SAMonitoringSession descriptionDictionary];
-[SAMonitoringSession encodeWithCoder:];
-[SAMonitoringSession description];
-[SAMonitoringSession initWithCoder:];
-[SAMonitoringSession copyWithZone:];
-[SAMonitoringSession isEqual:];
-[SAMonitoringSession state];
-[SAMonitoringSession scenario];
-[SAMonitoringSession setScenario:];
-[SAMonitoringSession foundAtLocation];
-[SAMonitoringSession wasBootstrapped];
-[SAMonitoringSession btHintCountDuringTravel];
-[SAMonitoringSession caLastStateTransition];
-[SAMonitoringSession caSeparationLocation];
-[SAMonitoringSession clearScanRetryState];
-[SAMonitoringSession cumulativeScanRxTime];
-[SAMonitoringSession earlyAirplaneTrigger];
-[SAMonitoringSession earlyVehicularStateChangeDate];
-[SAMonitoringSession earlyVehicularTrigger];
-[SAMonitoringSession firstNotWithYouLocation];
-[SAMonitoringSession foundAtLocationBeforePLCSuppression];
-[SAMonitoringSession geofence];
-[SAMonitoringSession hasTransitionedSinceBootstrap];
-[SAMonitoringSession initWithDeviceUUID:state:geofence:scenario:trackedTravelingStartDate:];
-[SAMonitoringSession lastAlertDateInCurrentTravelingSession];
-[SAMonitoringSession previouslySuppressedDueToPLC];
-[SAMonitoringSession scanRetryCount];
-[SAMonitoringSession scanRetryInProgress];
-[SAMonitoringSession scenarioClassifier];
-[SAMonitoringSession setBtHintCountDuringTravel:];
-[SAMonitoringSession setCaLastStateTransition:];
-[SAMonitoringSession setCaSeparationLocation:];
-[SAMonitoringSession setCumulativeScanRxTime:];
-[SAMonitoringSession setEarlyAirplaneTrigger:];
-[SAMonitoringSession setEarlyVehicularStateChangeDate:];
-[SAMonitoringSession setEarlyVehicularTrigger:];
-[SAMonitoringSession setFirstNotWithYouLocation:];
-[SAMonitoringSession setFoundAtLocation:];
-[SAMonitoringSession setFoundAtLocationBeforePLCSuppression:];
-[SAMonitoringSession setGeofence:];
-[SAMonitoringSession setHasTransitionedSinceBootstrap:];
-[SAMonitoringSession setLastAlertDateInCurrentTravelingSession:];
-[SAMonitoringSession setPreviouslySuppressedDueToPLC:];
-[SAMonitoringSession setScanRetryCount:];
-[SAMonitoringSession setScanRetryInProgress:];
-[SAMonitoringSession setScenarioClassifier:];
-[SAMonitoringSession setTrackedTravelingStartDate:];
-[SAMonitoringSession setTrackedTravelingStartLocation:];
-[SAMonitoringSession setTravelingGeofenceExitDate:];
-[SAMonitoringSession setWasBootstrapped:];
-[SAMonitoringSession trackedTravelingStartDate];
-[SAMonitoringSession trackedTravelingStartLocation];
-[SAMonitoringSession travelingGeofenceExitDate];
```
