# `CAMLibrarySelectionSignalResult`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 10 properties, 18 instance methods, 3 class methods

## Instance variables

```
i _locationAuthorizationStatus;
@"NSArray" _identitiesInProximity;
@"CLLocation" _currentLocation;
@"NSArray" _homeLocations;
@"NSArray" _frequentAndHomeLocations;
@"NSNumber" _suggestsSharingValue;
```

## Properties

```
@property (T@"NSArray",&,N,V_identitiesInProximity) identitiesInProximity;
@property (T@"CLLocation",&,N,V_currentLocation) currentLocation;
@property (T@"NSArray",R,N,V_homeLocations) homeLocations;
@property (T@"NSArray",R,N,V_frequentAndHomeLocations) frequentAndHomeLocations;
@property (T@"NSNumber",&,N,V_suggestsSharingValue) suggestsSharingValue;
@property (Ti,R,N,V_locationAuthorizationStatus) locationAuthorizationStatus;
@property (TB,R,N) cameraHasAccessToLocation;
@property (TB,R,N) isOnTrip;
@property (TB,R,N) currentLocationCloseToHome;
@property (TB,R,N) suggestsSharing;
```

## Class methods

```
+[CAMLibrarySelectionSignalResult currentLocation:isContainedInCircularRegions:];
+[CAMLibrarySelectionSignalResult distanceBetweenLocation:andCircularRegion:atDate:];
+[CAMLibrarySelectionSignalResult librarySelectionSignalResultWithIdentitiesInProximity:currentLocation:locationAuthorizationStatus:homeLocations:frequentLocations:];
```

## Instance methods

```
-[CAMLibrarySelectionSignalResult locationAuthorizationStatus];
-[CAMLibrarySelectionSignalResult setCurrentLocation:];
-[CAMLibrarySelectionSignalResult currentLocation];
-[CAMLibrarySelectionSignalResult description];
-[CAMLibrarySelectionSignalResult homeLocations];
-[CAMLibrarySelectionSignalResult suggestsSharing];
-[CAMLibrarySelectionSignalResult _diagnosticsForRegions:];
-[CAMLibrarySelectionSignalResult cameraHasAccessToLocation];
-[CAMLibrarySelectionSignalResult currentLocationCloseToHome];
-[CAMLibrarySelectionSignalResult frequentAndHomeLocations];
-[CAMLibrarySelectionSignalResult frequentLocationRegionContainingLocation:];
-[CAMLibrarySelectionSignalResult identitiesInProximity];
-[CAMLibrarySelectionSignalResult initWithIdentitiesInProximity:currentLocation:locationAuthorizationStatus:homeLocations:frequentLocations:];
-[CAMLibrarySelectionSignalResult isOnTrip];
-[CAMLibrarySelectionSignalResult resultDiagnostics];
-[CAMLibrarySelectionSignalResult setIdentitiesInProximity:];
-[CAMLibrarySelectionSignalResult setSuggestsSharingValue:];
-[CAMLibrarySelectionSignalResult suggestsSharingValue];
```
