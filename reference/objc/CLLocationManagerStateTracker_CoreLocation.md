# `CLLocationManagerStateTracker`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CLStateTracker`
- 3 instance variables, 27 properties, 62 instance methods, 2 class methods

## Instance variables

```
{_CLLocationManagerStateTrackerState="distanceFilter"d"desiredAccuracy"d"updatingLocation"B"requestingLocation"B"updatingHeading"B"headingFilter"d"allowsLocationPrompts"B"allowsAlteredAccessoryLocations"B"dynamicAccuracyReductionEnabled"B"previousAuthorizationStatusValid"B"previousAuthorizationStatus"i"limitsPrecision"B"activityType"q"pausesLocationUpdatesAutomatically"i"paused"B"allowsBackgroundLocationUpdates"B"showsBackgroundLocationIndicator"B"allowsMapCorrection"B"batchingLocation"B"updatingVehicleSpeed"B"updatingVehicleHeading"B"matchInfoEnabled"B"groundAltitudeEnabled"B"fusionInfoEnabled"B"courtesyPromptNeeded"B"isAuthorizedForWidgetUpdates"B"trackRunInfoEnabled"B} _state;
^v _identifier;
B _inTransaction;
```

## Properties

```
@property (Td,N) distanceFilter;
@property (Td,N) desiredAccuracy;
@property (TB,N) updatingLocation;
@property (TB,N) requestingLocation;
@property (TB,N) updatingHeading;
@property (Td,N) headingFilter;
@property (TB,N) allowsLocationPrompts;
@property (TB,N) allowsAlteredAccessoryLocations;
@property (TB,N) dynamicAccuracyReductionEnabled;
@property (TB,N) previousAuthorizationStatusValid;
@property (Ti,N) previousAuthorizationStatus;
@property (TB,N) limitsPrecision;
@property (Tq,N) activityType;
@property (Ti) pausesLocationUpdatesAutomatically;
@property (TB,N) paused;
@property (TB,N) allowsBackgroundLocationUpdates;
@property (TB,N) showsBackgroundLocationIndicator;
@property (TB,N) allowsMapCorrection;
@property (TB,N) batchingLocation;
@property (TB,N) updatingVehicleSpeed;
@property (TB,N) updatingVehicleHeading;
@property (TB,N) matchInfoEnabled;
@property (TB,N) groundAltitudeEnabled;
@property (TB,N) fusionInfoEnabled;
@property (TB,N) courtesyPromptNeeded;
@property (TB,N) isAuthorizedForWidgetUpdates;
@property (TB,N) trackRunInfoEnabled;
```

## Class methods

```
+[CLLocationManagerStateTracker trackerStateSize];
+[CLLocationManagerStateTracker trackerStateTypeName];
```

## Instance methods

```
-[CLLocationManagerStateTracker setUpdatingVehicleSpeed:];
-[CLLocationManagerStateTracker pausesLocationUpdatesAutomatically];
-[CLLocationManagerStateTracker setUpdatingHeading:];
-[CLLocationManagerStateTracker setActivityType:];
-[CLLocationManagerStateTracker setCourtesyPromptNeeded:];
-[CLLocationManagerStateTracker isAuthorizedForWidgetUpdates];
-[CLLocationManagerStateTracker identifier];
-[CLLocationManagerStateTracker updatingVehicleHeading];
-[CLLocationManagerStateTracker setUpdatingVehicleHeading:];
-[CLLocationManagerStateTracker setUpdatingLocation:];
-[CLLocationManagerStateTracker paused];
-[CLLocationManagerStateTracker setMatchInfoEnabled:];
-[CLLocationManagerStateTracker dealloc];
-[CLLocationManagerStateTracker setAllowsBackgroundLocationUpdates:];
-[CLLocationManagerStateTracker showsBackgroundLocationIndicator];
-[CLLocationManagerStateTracker setTrackRunInfoEnabled:];
-[CLLocationManagerStateTracker distanceFilter];
-[CLLocationManagerStateTracker activityType];
-[CLLocationManagerStateTracker setPreviousAuthorizationStatus:];
-[CLLocationManagerStateTracker allowsLocationPrompts];
-[CLLocationManagerStateTracker groundAltitudeEnabled];
-[CLLocationManagerStateTracker setBatchingLocation:];
-[CLLocationManagerStateTracker batchingLocation];
-[CLLocationManagerStateTracker setIsAuthorizedForWidgetUpdates:];
-[CLLocationManagerStateTracker updatingHeading];
-[CLLocationManagerStateTracker dynamicAccuracyReductionEnabled];
-[CLLocationManagerStateTracker setPreviousAuthorizationStatusValid:];
-[CLLocationManagerStateTracker setPausesLocationUpdatesAutomatically:];
-[CLLocationManagerStateTracker initWithQueue:identifier:state:];
-[CLLocationManagerStateTracker trackRunInfoEnabled];
-[CLLocationManagerStateTracker setPaused:];
-[CLLocationManagerStateTracker allowsAlteredAccessoryLocations];
-[CLLocationManagerStateTracker previousAuthorizationStatusValid];
-[CLLocationManagerStateTracker setDistanceFilter:];
-[CLLocationManagerStateTracker previousAuthorizationStatus];
-[CLLocationManagerStateTracker setAllowsAlteredAccessoryLocations:];
-[CLLocationManagerStateTracker dumpState:withSize:hints:];
-[CLLocationManagerStateTracker initInSilo:withIdentifier:];
-[CLLocationManagerStateTracker setRequestingLocation:];
-[CLLocationManagerStateTracker allowsBackgroundLocationUpdates];
-[CLLocationManagerStateTracker setLimitsPrecision:];
-[CLLocationManagerStateTracker setGroundAltitudeEnabled:];
-[CLLocationManagerStateTracker setAllowsMapCorrection:];
-[CLLocationManagerStateTracker courtesyPromptNeeded];
-[CLLocationManagerStateTracker updateState:];
-[CLLocationManagerStateTracker updatingVehicleSpeed];
-[CLLocationManagerStateTracker desiredAccuracy];
-[CLLocationManagerStateTracker setFusionInfoEnabled:];
-[CLLocationManagerStateTracker requestingLocation];
-[CLLocationManagerStateTracker headingFilter];
-[CLLocationManagerStateTracker setDynamicAccuracyReductionEnabled:];
-[CLLocationManagerStateTracker updatingLocation];
-[CLLocationManagerStateTracker limitsPrecision];
-[CLLocationManagerStateTracker setHeadingFilter:];
-[CLLocationManagerStateTracker initInSilo:withIdentifier:state:];
-[CLLocationManagerStateTracker allowsMapCorrection];
-[CLLocationManagerStateTracker fusionInfoEnabled];
-[CLLocationManagerStateTracker matchInfoEnabled];
-[CLLocationManagerStateTracker initWithQueue:identifier:];
-[CLLocationManagerStateTracker setDesiredAccuracy:];
-[CLLocationManagerStateTracker setShowsBackgroundLocationIndicator:];
-[CLLocationManagerStateTracker setAllowsLocationPrompts:];
```
