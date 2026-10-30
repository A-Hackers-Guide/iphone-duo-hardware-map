# `CAMLibrarySelectionController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMLocationControllerListener`, `CAMPeopleProximityDelegate`
- 15 instance variables, 22 properties, 62 instance methods, 0 class methods

## Instance variables

```
B _peopleProximityDetectionSupported;
i __resultQueue_authorizationStatus;
@"CAMLibrarySelectionSignalResult" _acquiredSignalResults;
@"NSObject<OS_dispatch_queue>" _resultQueue;
@"NSMutableSet" __resultQueue_identitiesInProximity;
@"CLLocation" __resultQueue_currentLocation;
@"PHCameraSmartSharingMetadata" __resultQueue_smartSharingMetadata;
@"NSNumber" __resultQueue_needsLocationShifting;
@"GEOLocationShifter" __resultQueue_locationShifter;
@"<CAMLibrarySelectionLocationProvider>" _locationProvider;
@? _ppt_changeHandler;
@"<CAMPeopleProximityControllerProtocol>" _proximityController;
# _smartSharingMetadataProvider;
@"CAMLibrarySelectionSession" _session;
@"NSArray" _identitiesToScan;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_resultQueue) resultQueue;
@property (T@"NSMutableSet",&,N,V__resultQueue_identitiesInProximity) _resultQueue_identitiesInProximity;
@property (T@"CLLocation",&,N,V__resultQueue_currentLocation) _resultQueue_currentLocation;
@property (Ti,N,V__resultQueue_authorizationStatus) _resultQueue_authorizationStatus;
@property (T@"PHCameraSmartSharingMetadata",&,N,V__resultQueue_smartSharingMetadata) _resultQueue_smartSharingMetadata;
@property (T@"NSNumber",&,N,V__resultQueue_needsLocationShifting) _resultQueue_needsLocationShifting;
@property (T@"GEOLocationShifter",&,N,V__resultQueue_locationShifter) _resultQueue_locationShifter;
@property (T@"<CAMLibrarySelectionLocationProvider>",&,N,V_locationProvider) locationProvider;
@property (T@"CAMLibrarySelectionSignalResult",&,N,V_acquiredSignalResults) acquiredSignalResults;
@property (TB,N,V_peopleProximityDetectionSupported) peopleProximityDetectionSupported;
@property (T@?,C,N,V_ppt_changeHandler) ppt_changeHandler;
@property (T@"<CAMPeopleProximityControllerProtocol>",&,N,V_proximityController) proximityController;
@property (T#,&,N,V_smartSharingMetadataProvider) smartSharingMetadataProvider;
@property (T@"CAMLibrarySelectionSession",&,N,V_session) session;
@property (T@"NSArray",C,N,V_identitiesToScan) identitiesToScan;
@property (Tq,R,N) sharedLibraryMode;
@property (Tq,R,N) sharedLibraryInitialMode;
@property (Tq,R,N) userInteractionsCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMLibrarySelectionController peopleProximityDetectionSupported];
-[CAMLibrarySelectionController sharedLibraryMode];
-[CAMLibrarySelectionController setLocationProvider:];
-[CAMLibrarySelectionController setResultQueue:];
-[CAMLibrarySelectionController setSession:];
-[CAMLibrarySelectionController setDelegate:];
-[CAMLibrarySelectionController session];
-[CAMLibrarySelectionController locationProvider];
-[CAMLibrarySelectionController resultQueue];
-[CAMLibrarySelectionController startNewSession];
-[CAMLibrarySelectionController _diagnosticsForLocation:currentLocation:];
-[CAMLibrarySelectionController _ensureProximityController];
-[CAMLibrarySelectionController _newSessionWithDelegate:];
-[CAMLibrarySelectionController _ppt_callChangeHandler];
-[CAMLibrarySelectionController _resultQueue_authorizationStatus];
-[CAMLibrarySelectionController _resultQueue_clearAcquiredSignals];
-[CAMLibrarySelectionController _resultQueue_currentLocation];
-[CAMLibrarySelectionController _resultQueue_currentLocationUpdatedAndShiftedIfNeeded:];
-[CAMLibrarySelectionController _resultQueue_identitiesInProximity];
-[CAMLibrarySelectionController _resultQueue_locationShifter];
-[CAMLibrarySelectionController _resultQueue_needsLocationShifting];
-[CAMLibrarySelectionController _resultQueue_needsLocationShiftingForLocation:];
-[CAMLibrarySelectionController _resultQueue_shiftCoordinatesForLocation:];
-[CAMLibrarySelectionController _resultQueue_smartSharingMetadata];
-[CAMLibrarySelectionController _resultQueue_startDiscovery];
-[CAMLibrarySelectionController _resultQueue_stopDiscovery];
-[CAMLibrarySelectionController _resultQueue_updateAcquiredSignalResults];
-[CAMLibrarySelectionController _retrieveMetadata];
-[CAMLibrarySelectionController _stopAcquiringSignalsAndClear:];
-[CAMLibrarySelectionController acquiredSignalResults];
-[CAMLibrarySelectionController authorizationStatusUpdated:];
-[CAMLibrarySelectionController currentHeadingUpdated:];
-[CAMLibrarySelectionController currentLocationUpdated:];
-[CAMLibrarySelectionController didDiscoverIdentity:];
-[CAMLibrarySelectionController didLoseIdentity:];
-[CAMLibrarySelectionController identitiesToScan];
-[CAMLibrarySelectionController initWithLocationProvider:];
-[CAMLibrarySelectionController librarySelectionDiagnostics];
-[CAMLibrarySelectionController listeningQueue];
-[CAMLibrarySelectionController ppt_changeHandler];
-[CAMLibrarySelectionController ppt_installChangeHandler:];
-[CAMLibrarySelectionController proximityController];
-[CAMLibrarySelectionController setAcquiredSignalResults:];
-[CAMLibrarySelectionController setIdentitiesToScan:];
-[CAMLibrarySelectionController setPeopleProximityDetectionSupported:];
-[CAMLibrarySelectionController setPpt_changeHandler:];
-[CAMLibrarySelectionController setProximityController:];
-[CAMLibrarySelectionController setSmartSharingMetadataProvider:];
-[CAMLibrarySelectionController set_resultQueue_authorizationStatus:];
-[CAMLibrarySelectionController set_resultQueue_currentLocation:];
-[CAMLibrarySelectionController set_resultQueue_identitiesInProximity:];
-[CAMLibrarySelectionController set_resultQueue_locationShifter:];
-[CAMLibrarySelectionController set_resultQueue_needsLocationShifting:];
-[CAMLibrarySelectionController set_resultQueue_smartSharingMetadata:];
-[CAMLibrarySelectionController sharedLibraryInitialMode];
-[CAMLibrarySelectionController smartSharingMetadataProvider];
-[CAMLibrarySelectionController startAcquiringSignals];
-[CAMLibrarySelectionController stopAcquiringSignals];
-[CAMLibrarySelectionController stopAndClearAcquiredSignals];
-[CAMLibrarySelectionController tapToRadarAlertController];
-[CAMLibrarySelectionController userDidPickSharedLibraryMode:];
-[CAMLibrarySelectionController userInteractionsCount];
```
