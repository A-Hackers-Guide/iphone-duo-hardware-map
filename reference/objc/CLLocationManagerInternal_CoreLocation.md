# `CLLocationManagerInternal`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 23 instance variables, 6 properties, 23 instance methods, 0 class methods

## Instance variables

```
^{__CLClient=} fClient;
@"<CLLocationManagerDelegate>" fDelegate;
@"CLLocationManager" fManager;
@"CLLocationManagerStateTracker" fState;
{?="suitability"i"coordinate"{?="latitude"d"longitude"d}"horizontalAccuracy"d"altitude"d"verticalAccuracy"d"speed"d"speedAccuracy"d"course"d"courseAccuracy"d"timestamp"d"confidence"i"lifespan"d"type"i"rawCoordinate"{?="latitude"d"longitude"d}"rawCourse"d"floor"i"integrity"I"referenceFrame"i"rawReferenceFrame"i"signalEnvironmentType"i"ellipsoidalAltitude"d"fromSimulationController"B} fLocation;
@"NSString" fLocationEventType;
@"CLTimer" fLocationRequestTimer;
d fLocationRequestTimeout;
i fHeadingOrientation;
@"<CLBodyIdentifiable>" fHeadingBody;
@"CLBodyToken" fHeadingBodyToken;
d fInterfaceAngle;
@"NSMutableSet" fRangedRegions;
@"NSMutableSet" fRangedConstraints;
@? fPlaceInferenceHandler;
Q fFidelityPolicy;
@"CLTimer" fPlaceInferenceTimer;
B fIsMasquerading;
@"NSMutableSet" fIdentifiableClients;
@"CLSilo" fSilo;
@"CLBufferedLocationFlushMonitor" fBufferedLocationFlushMonitor;
@"NSString" _clientKeyForIdentityValidation;
@"NSData" _monitorLedgerAccessKey;
```

## Properties

```
@property (T@"NSString",&,V_clientKeyForIdentityValidation) clientKeyForIdentityValidation;
@property (T@"NSData",&,V_monitorLedgerAccessKey) monitorLedgerAccessKey;
@property (T@"NSMutableSet",R,N,VfRangedRegions) rangedRegions;
@property (T@"NSMutableSet",R,N,VfRangedConstraints) rangedConstraints;
@property (T@"<CLLocationManagerDelegate>",W,N,VfDelegate) delegate;
@property (T@"CLLocationManager",W,N,VfManager) manager;
```

## Instance methods

```
-[CLLocationManagerInternal rangedRegions];
-[CLLocationManagerInternal monitorLedgerAccessKey];
-[CLLocationManagerInternal setManager:];
-[CLLocationManagerInternal dealloc];
-[CLLocationManagerInternal setClientKeyForIdentityValidation:];
-[CLLocationManagerInternal setAllowsBackgroundLocationUpdates:];
-[CLLocationManagerInternal initWithInfo:bundleIdentifier:bundlePath:websiteIdentifier:delegate:silo:];
-[CLLocationManagerInternal showsBackgroundLocationIndicator];
-[CLLocationManagerInternal manager];
-[CLLocationManagerInternal PausesLocationUpdatesAutomatically];
-[CLLocationManagerInternal stopUpdatingLocationAutoPaused];
-[CLLocationManagerInternal setPausesLocationUpdatesAutomatically:];
-[CLLocationManagerInternal invalidate];
-[CLLocationManagerInternal cancelLocationRequest];
-[CLLocationManagerInternal setDelegate:];
-[CLLocationManagerInternal setMonitorLedgerAccessKey:];
-[CLLocationManagerInternal clientKeyForIdentityValidation];
-[CLLocationManagerInternal delegate];
-[CLLocationManagerInternal performCourtesyPromptIfNeeded];
-[CLLocationManagerInternal allowsBackgroundLocationUpdates];
-[CLLocationManagerInternal tearDownBufferedFlushMonitorWithCode:reason:];
-[CLLocationManagerInternal rangedConstraints];
-[CLLocationManagerInternal setShowsBackgroundLocationIndicator:];
```
