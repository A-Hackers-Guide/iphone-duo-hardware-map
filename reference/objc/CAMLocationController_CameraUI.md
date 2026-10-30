# `CAMLocationController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CLLocationManagerDelegate`
- 12 instance variables, 16 properties, 36 instance methods, 3 class methods

## Instance variables

```
B _enabled;
B _headingEnabled;
B _supportsIntelligenceLocationPrompt;
B __monitoringLocation;
B __didRequestLocation;
i _lastKnownAuthorizationStatus;
@"CLLocation" _currentLocation;
@"CLHeading" _currentHeading;
@"CLLocationManager" __locationManager;
@"NSMutableArray" __enqueuedAssetsWaitingForLocation;
@"NSHashTable" __listenersWaitingForLocation;
@"NSObject<OS_dispatch_queue>" __listenersQueue;
```

## Properties

```
@property (T@"CLLocation",&,N,S_setCurrentLocation:,V_currentLocation) currentLocation;
@property (T@"CLHeading",&,N,S_setCurrentHeading:,V_currentHeading) currentHeading;
@property (Ti,N,S_setLastKnownAuthorizationStatus:,V_lastKnownAuthorizationStatus) lastKnownAuthorizationStatus;
@property (TB,R,N,G_isMonitoringLocation,V__monitoringLocation) _monitoringLocation;
@property (T@"CLLocationManager",R,N,V__locationManager) _locationManager;
@property (T@"NSMutableArray",R,N,V__enqueuedAssetsWaitingForLocation) _enqueuedAssetsWaitingForLocation;
@property (T@"NSHashTable",R,N,V__listenersWaitingForLocation) _listenersWaitingForLocation;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__listenersQueue) _listenersQueue;
@property (TB,N,S_setDidRequestLocation:,V__didRequestLocation) _didRequestLocation;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TB,N,GisHeadingEnabled,V_headingEnabled) headingEnabled;
@property (TB,N,V_supportsIntelligenceLocationPrompt) supportsIntelligenceLocationPrompt;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMLocationController _sharedGPSDatestampFormatter];
+[CAMLocationController _sharedGPSTimestampFormatter];
+[CAMLocationController locationMetadataForLocation:heading:device:];
```

## Instance methods

```
-[CAMLocationController _notifyListenersForAuthorizationStatusUpdate:];
-[CAMLocationController locationManager:didUpdateLocations:];
-[CAMLocationController _setLastKnownAuthorizationStatus:];
-[CAMLocationController _isMonitoringLocation];
-[CAMLocationController _performBlock:andLogIfExecutionExceeds:logPrefix:];
-[CAMLocationController supportsIntelligenceLocationPrompt];
-[CAMLocationController init];
-[CAMLocationController _didRequestLocation];
-[CAMLocationController addListenerForLocationUpdates:];
-[CAMLocationController currentLocation];
-[CAMLocationController _enqueuedAssetsWaitingForLocation];
-[CAMLocationController _setCurrentHeading:];
-[CAMLocationController dealloc];
-[CAMLocationController _notifyListenersWaitingOnHeading:];
-[CAMLocationController _listenersQueue];
-[CAMLocationController _startMonitoringLocationUpdates];
-[CAMLocationController _authorizeOrStartLocationManager];
-[CAMLocationController _locationManager];
-[CAMLocationController _setCurrentLocation:];
-[CAMLocationController _listenersWaitingForLocation];
-[CAMLocationController isEnabled];
-[CAMLocationController setEnabled:];
-[CAMLocationController _updateLocationMonitoring];
-[CAMLocationController removeListenerForLocationUpdates:];
-[CAMLocationController lastKnownAuthorizationStatus];
-[CAMLocationController headingForOrientation:];
-[CAMLocationController _notifyListenersWaitingOnLocation:];
-[CAMLocationController currentHeading];
-[CAMLocationController isHeadingEnabled];
-[CAMLocationController locationManager:didUpdateHeading:];
-[CAMLocationController _setDidRequestLocation:];
-[CAMLocationController locationManagerDidChangeAuthorization:];
-[CAMLocationController setHeadingEnabled:];
-[CAMLocationController _resetDidRequestLocation];
-[CAMLocationController _stopMonitoringLocationUpdates];
-[CAMLocationController setSupportsIntelligenceLocationPrompt:];
```
