# `WiFiLocationManager`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CLLocationManagerDelegate`
- 13 instance variables, 17 properties, 53 instance methods, 8 class methods

## Instance variables

```
C _shouldMonitorVisits;
C _isAuthorized;
i _locationManagerState;
@"<WiFiLocationManagerDelegate>" _delegate;
@"CLLocation" _latestLocation;
@"CLLocationManager" _clLocationManager;
@"NSMutableArray" _clientsDataArray;
@"NSMutableArray" _visitClientsDataArray;
@"NSObject<OS_dispatch_queue>" _queue;
@"WiFiAirplaneLandingDetector" _airplaneLandingDetector;
@"CLLocation" _lastKnownAirportLocation;
@"CLLocation" _lastAirportQueryLocation;
@"NSDate" _firstTimeExceededAirportRadius;
```

## Properties

```
@property (T@"CLLocationManager",&,N,V_clLocationManager) clLocationManager;
@property (T@"NSMutableArray",&,N,V_clientsDataArray) clientsDataArray;
@property (T@"NSMutableArray",&,N,V_visitClientsDataArray) visitClientsDataArray;
@property (Ti,V_locationManagerState) locationManagerState;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"WiFiAirplaneLandingDetector",&,N,V_airplaneLandingDetector) airplaneLandingDetector;
@property (T@"CLLocation",&,N,V_lastKnownAirportLocation) lastKnownAirportLocation;
@property (T@"CLLocation",&,N,V_lastAirportQueryLocation) lastAirportQueryLocation;
@property (T@"NSDate",&,N,V_firstTimeExceededAirportRadius) firstTimeExceededAirportRadius;
@property (T@"CLLocation",&,V_latestLocation) latestLocation;
@property (TC,V_isAuthorized) isAuthorized;
@property (T@"<WiFiLocationManagerDelegate>",W,N,V_delegate) delegate;
@property (TC,N,V_shouldMonitorVisits) shouldMonitorVisits;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[WiFiLocationManager isLocationAnAirport:completion:];
+[WiFiLocationManager airportQuerySampleRate];
+[WiFiLocationManager getStringOfCallbackType:];
+[WiFiLocationManager getStringOfState:];
+[WiFiLocationManager isLocationValid:uptoSeconds:isHighAccuracy:];
+[WiFiLocationManager isLocationValid:uptoSeconds:requiredAccuracy:];
+[WiFiLocationManager logLocation:addPrefixString:];
+[WiFiLocationManager sharedWiFiLocationManager];
```

## Instance methods

```
-[WiFiLocationManager setClLocationManager:];
-[WiFiLocationManager registerCallbackFunctionPtr:withContext:];
-[WiFiLocationManager manageAirplaneWiFiDetector:];
-[WiFiLocationManager locationManager:didVisit:];
-[WiFiLocationManager locationManager:didUpdateLocations:];
-[WiFiLocationManager stopQueryingLocation];
-[WiFiLocationManager locationManager:didFailWithError:];
-[WiFiLocationManager init];
-[WiFiLocationManager setShouldMonitorVisits:];
-[WiFiLocationManager lastKnownAirportLocation];
-[WiFiLocationManager requestLowAccuracyLocationUpdate];
-[WiFiLocationManager setFirstTimeExceededAirportRadius:];
-[WiFiLocationManager dealloc];
-[WiFiLocationManager locationManagerState];
-[WiFiLocationManager handleAirplaneLandingDetectorResult:];
-[WiFiLocationManager queue];
-[WiFiLocationManager visitClientsDataArray];
-[WiFiLocationManager setLastKnownAirportLocation:];
-[WiFiLocationManager setLocationManagerState:];
-[WiFiLocationManager latestLocation];
-[WiFiLocationManager setLastAirportQueryLocation:];
-[WiFiLocationManager setIsAuthorized:];
-[WiFiLocationManager setVisitClientsDataArray:];
-[WiFiLocationManager locationRequestDidTimeOut];
-[WiFiLocationManager airplaneLandingDetector];
-[WiFiLocationManager setDelegate:];
-[WiFiLocationManager setClientsDataArray:];
-[WiFiLocationManager destroyCoreLocationObjects];
-[WiFiLocationManager registerVisitCallbackFunctionPtr:withContext:];
-[WiFiLocationManager createAirplaneWiFiDetectorWithStartReason:];
-[WiFiLocationManager cancelLocationRequestTimeOut];
-[WiFiLocationManager clLocationManager];
-[WiFiLocationManager locationManager:didChangeAuthorizationStatus:];
-[WiFiLocationManager shouldMonitorVisits];
-[WiFiLocationManager delegate];
-[WiFiLocationManager clientsDataArray];
-[WiFiLocationManager invokeClientsCallbackType:withLocation:withError:];
-[WiFiLocationManager lastAirportQueryLocation];
-[WiFiLocationManager setLatestLocation:];
-[WiFiLocationManager networkDidJoinWithDetails:];
-[WiFiLocationManager createCoreLocationObjects];
-[WiFiLocationManager createAirplaneWiFiDetector];
-[WiFiLocationManager requestHighAccuracyLocationUpdate];
-[WiFiLocationManager gatherLandingDetectedLogs:];
-[WiFiLocationManager isLocationAnAirport:completion:];
-[WiFiLocationManager networkDidDisconnect];
-[WiFiLocationManager setCLLocationUpdateParams:];
-[WiFiLocationManager airplaneModeDidChange:];
-[WiFiLocationManager setAirplaneLandingDetector:];
-[WiFiLocationManager firstTimeExceededAirportRadius];
-[WiFiLocationManager isAuthorized];
-[WiFiLocationManager requestLeechedAccuracyLocationUpdate];
-[WiFiLocationManager setQueue:];
```
