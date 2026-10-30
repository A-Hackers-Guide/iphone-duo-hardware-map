# `WiFiAirplaneLandingDetector`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 17 properties, 64 instance methods, 5 class methods

## Instance variables

```
B _waitingForFirstSampleAfterReboot;
B _isCurrentlyAssociated;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@"NSObject<OS_dispatch_source>" _samplingTimer;
@? _landingCallback;
@"<WiFiLocationProtocol>" _locationManager;
@"NSMutableArray" _verticalSpeedSamples;
d _lastAltitude;
@"NSDate" _lastSampleDate;
d _maxAltitude;
d _currentSamplingInterval;
@"NSDate" _layoverModeStartDate;
@"NSDate" _firstTimeExceededAirportRadius;
@"WiFiSoftError" _softError;
@"WiFiAirplaneLandingDetectorAnalytics" _analytics;
@"WiFiUsageNetworkDetails" _currentNetworkDetails;
{?="activeFlightInterval"d"layoverInterval"d"inactiveInterval"d"maxSamples"Q"minSamplesAboveThreshold"Q"minVerticalSpeed"d"minMaxAltitude"d"takeoffAltitudeIncrease"d"layoverTimeout"d"sustainedInactivityOutsideAirportTimeout"d} _config;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_samplingTimer) samplingTimer;
@property (T@?,C,N,V_landingCallback) landingCallback;
@property (T@"<WiFiLocationProtocol>",&,N,V_locationManager) locationManager;
@property (T{?=dddQQddddd},N,V_config) config;
@property (T@"NSMutableArray",&,N,V_verticalSpeedSamples) verticalSpeedSamples;
@property (Td,N,V_lastAltitude) lastAltitude;
@property (T@"NSDate",&,N,V_lastSampleDate) lastSampleDate;
@property (TB,N,V_waitingForFirstSampleAfterReboot) waitingForFirstSampleAfterReboot;
@property (Td,N,V_maxAltitude) maxAltitude;
@property (Td,N,V_currentSamplingInterval) currentSamplingInterval;
@property (T@"NSDate",&,N,V_layoverModeStartDate) layoverModeStartDate;
@property (T@"NSDate",&,N,V_firstTimeExceededAirportRadius) firstTimeExceededAirportRadius;
@property (T@"WiFiSoftError",&,N,V_softError) softError;
@property (T@"WiFiAirplaneLandingDetectorAnalytics",&,N,V_analytics) analytics;
@property (T@"WiFiUsageNetworkDetails",&,N,V_currentNetworkDetails) currentNetworkDetails;
@property (TB,N,V_isCurrentlyAssociated) isCurrentlyAssociated;
```

## Class methods

```
+[WiFiAirplaneLandingDetector defaultConfig];
+[WiFiAirplaneLandingDetector defaultLocationManager];
+[WiFiAirplaneLandingDetector clearPersistedState];
+[WiFiAirplaneLandingDetector describeTime:];
+[WiFiAirplaneLandingDetector isDetectorActive];
```

## Instance methods

```
-[WiFiAirplaneLandingDetector setLocationManager:];
-[WiFiAirplaneLandingDetector analytics];
-[WiFiAirplaneLandingDetector notifyStateChange:];
-[WiFiAirplaneLandingDetector locationManager];
-[WiFiAirplaneLandingDetector dispatchQueue];
-[WiFiAirplaneLandingDetector setAnalytics:];
-[WiFiAirplaneLandingDetector config];
-[WiFiAirplaneLandingDetector setConfig:];
-[WiFiAirplaneLandingDetector setCurrentNetworkDetails:];
-[WiFiAirplaneLandingDetector setFirstTimeExceededAirportRadius:];
-[WiFiAirplaneLandingDetector dealloc];
-[WiFiAirplaneLandingDetector initWithCompletion:];
-[WiFiAirplaneLandingDetector setDispatchQueue:];
-[WiFiAirplaneLandingDetector persistState];
-[WiFiAirplaneLandingDetector description];
-[WiFiAirplaneLandingDetector networkDidJoinWithDetails:];
-[WiFiAirplaneLandingDetector gatherLandingDetectedLogs:];
-[WiFiAirplaneLandingDetector currentNetworkDetails];
-[WiFiAirplaneLandingDetector networkDidDisconnect];
-[WiFiAirplaneLandingDetector lastSampleDate];
-[WiFiAirplaneLandingDetector airplaneModeDidChange:];
-[WiFiAirplaneLandingDetector firstTimeExceededAirportRadius];
-[WiFiAirplaneLandingDetector setLastSampleDate:];
-[WiFiAirplaneLandingDetector updateConfig:];
-[WiFiAirplaneLandingDetector processSample:];
-[WiFiAirplaneLandingDetector currentModeName];
-[WiFiAirplaneLandingDetector initWithCompletion:startReason:];
-[WiFiAirplaneLandingDetector landingCallback];
-[WiFiAirplaneLandingDetector setMaxAltitude:];
-[WiFiAirplaneLandingDetector currentModeEnum];
-[WiFiAirplaneLandingDetector checkDetectionCriteria:];
-[WiFiAirplaneLandingDetector createSamplingTimer];
-[WiFiAirplaneLandingDetector currentSamplingInterval];
-[WiFiAirplaneLandingDetector enterActiveFlightMode];
-[WiFiAirplaneLandingDetector enterInactiveMode];
-[WiFiAirplaneLandingDetector enterLayoverMode:];
-[WiFiAirplaneLandingDetector getAltitudeSample];
-[WiFiAirplaneLandingDetector inInactiveMode];
-[WiFiAirplaneLandingDetector inLayoverMode];
-[WiFiAirplaneLandingDetector initWithCompletion:startReason:config:locationManager:];
-[WiFiAirplaneLandingDetector isCurrentlyAssociated];
-[WiFiAirplaneLandingDetector lastAltitude];
-[WiFiAirplaneLandingDetector layoverModeStartDate];
-[WiFiAirplaneLandingDetector maxAltitude];
-[WiFiAirplaneLandingDetector notifyExceededAirportRadius];
-[WiFiAirplaneLandingDetector resetExceededAirportRadius];
-[WiFiAirplaneLandingDetector retrieveAndClearState];
-[WiFiAirplaneLandingDetector samplingDescription];
-[WiFiAirplaneLandingDetector samplingTimer];
-[WiFiAirplaneLandingDetector setCurrentSamplingInterval:];
-[WiFiAirplaneLandingDetector setIsCurrentlyAssociated:];
-[WiFiAirplaneLandingDetector setLandingCallback:];
-[WiFiAirplaneLandingDetector setLastAltitude:];
-[WiFiAirplaneLandingDetector setLayoverModeStartDate:];
-[WiFiAirplaneLandingDetector setSamplingTimer:];
-[WiFiAirplaneLandingDetector setSoftError:];
-[WiFiAirplaneLandingDetector setVerticalSpeedSamples:];
-[WiFiAirplaneLandingDetector setWaitingForFirstSampleAfterReboot:];
-[WiFiAirplaneLandingDetector softError];
-[WiFiAirplaneLandingDetector ttr:];
-[WiFiAirplaneLandingDetector updateSpeedSamples:];
-[WiFiAirplaneLandingDetector updateTimerInterval:];
-[WiFiAirplaneLandingDetector verticalSpeedSamples];
-[WiFiAirplaneLandingDetector waitingForFirstSampleAfterReboot];
```
