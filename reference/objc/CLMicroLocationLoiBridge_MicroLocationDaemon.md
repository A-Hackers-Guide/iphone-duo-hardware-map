# `CLMicroLocationLoiBridge`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CLLocationManagerDelegate`, `CLMicroLocationLoiBridgeProtocol`
- 7 instance variables, 10 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"CLLocationManager" _clLocationManager;
@"RTRoutineManager" _routineManager;
@"NSObject<OS_dispatch_queue>" _queue;
@"ULTimer" _fetchPlaceInferenceTimer;
^{CLMicroLocationLoiDelegate=^^?} _microLocationLoiDelegate;
@"CLMonitorConfiguration" _regionMonitorConfiguration;
@"CLMonitor" _regionMonitor;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"CLLocationManager",&,N,V_clLocationManager) clLocationManager;
@property (T@"RTRoutineManager",&,N,V_routineManager) routineManager;
@property (T@"CLMonitor",&,N,V_regionMonitor) regionMonitor;
@property (T@"CLMonitorConfiguration",&,N,V_regionMonitorConfiguration) regionMonitorConfiguration;
@property (T@"ULTimer",&,N,V_fetchPlaceInferenceTimer) fetchPlaceInferenceTimer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CLMicroLocationLoiBridge regionMonitor];
-[CLMicroLocationLoiBridge routineManager];
-[CLMicroLocationLoiBridge initWithQueue:];
-[CLMicroLocationLoiBridge setClLocationManager:];
-[CLMicroLocationLoiBridge setupFetchPlaceInferenceTimer];
-[CLMicroLocationLoiBridge setRoutineManager:];
-[CLMicroLocationLoiBridge locationManager:didVisit:];
-[CLMicroLocationLoiBridge locationManager:didUpdateLocations:];
-[CLMicroLocationLoiBridge setRegionMonitor:];
-[CLMicroLocationLoiBridge locationManager:didFailWithError:];
-[CLMicroLocationLoiBridge removeGeofencesNearLocationWithLatitude:andLongitude:];
-[CLMicroLocationLoiBridge startLeechingLocationUpdates];
-[CLMicroLocationLoiBridge getAllActiveGeofences];
-[CLMicroLocationLoiBridge setMicroLocationLoiDelegate:];
-[CLMicroLocationLoiBridge setFetchPlaceInferenceTimer:];
-[CLMicroLocationLoiBridge dealloc];
-[CLMicroLocationLoiBridge queue];
-[CLMicroLocationLoiBridge generateGeofenceUpdateToClient:];
-[CLMicroLocationLoiBridge setupRegionMonitoring];
-[CLMicroLocationLoiBridge regionMonitor:didGenerateEvent:];
-[CLMicroLocationLoiBridge stopLeechingLocationUpdates];
-[CLMicroLocationLoiBridge clLocationManager];
-[CLMicroLocationLoiBridge invalidateFetchPlaceInferenceTimer];
-[CLMicroLocationLoiBridge convertMonitoringEventToGeofenceState:];
-[CLMicroLocationLoiBridge fetchLocationOfInterestAtLocation:];
-[CLMicroLocationLoiBridge generateLocationManagerNotAvailableError];
-[CLMicroLocationLoiBridge requestBootstrapWithLastGeofenceStates];
-[CLMicroLocationLoiBridge regionMonitorConfiguration];
-[CLMicroLocationLoiBridge startVisitMonitoring];
-[CLMicroLocationLoiBridge fetchRelatedLoisForLoi:];
-[CLMicroLocationLoiBridge setRegionMonitorConfiguration:];
-[CLMicroLocationLoiBridge microLocationLoiDelegate];
-[CLMicroLocationLoiBridge fetchPlaceInferenceAtCurrentLocationWithPolicy:];
-[CLMicroLocationLoiBridge fetchPlaceInferenceTimer];
-[CLMicroLocationLoiBridge getCurrentLocation];
-[CLMicroLocationLoiBridge removeGeofenceWithRegionId:];
-[CLMicroLocationLoiBridge setGeofenceAtLocation:];
-[CLMicroLocationLoiBridge generateRegionMonitorNotAvailableError];
-[CLMicroLocationLoiBridge retrieveAllActiveGeofences];
-[CLMicroLocationLoiBridge setQueue:];
```
