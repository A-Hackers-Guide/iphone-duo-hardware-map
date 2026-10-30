# `SBSensorActivityDataProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CCUISensorActivityDataProvider`, `SBFSensorActivityDataProvider`
- 11 instance variables, 26 properties, 39 instance methods, 0 class methods

## Instance variables

```
B _hasProcessedDomainData;
@"NSSet" _activeSensorActivityAttributions;
@"NSSet" _recentSensorActivityAttributions;
@"NSSet" _activeAccessSensorActivityAttributions;
@"NSSet" _microphoneAttributionsAwaitingMinimumOnTime;
@"NSSet" _cameraAttributionsAwaitingMinimumOnTime;
@"STDataAccessStatusDomain" _dataAccessDomain;
@"NSHashTable" _observers;
@"SBSecureIndicatorMinimumOnTimeCoordinator" _minimumOnTimeCoordinator;
@"<SBSecureIndicatorMinimumOnTimeCoordinatedBlockRegistration>" _microphoneMinimumOnTimeRegistration;
@"<SBSecureIndicatorMinimumOnTimeCoordinatedBlockRegistration>" _cameraMinimumOnTimeRegistration;
```

## Properties

```
@property (T@"NSSet",R,N) activeSensorActivityData;
@property (T@"CCUISensorActivityData",R,C,N) inactiveSensorActivityDataEligibleForMicModeSelection;
@property (T@"CCUISensorActivityData",R,C,N) mostRecentSensorActivityData;
@property (T@"NSSet",?,R,N) mutedMicrophoneSensorActivityData;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSSet",C,N,V_activeSensorActivityAttributions) activeSensorActivityAttributions;
@property (T@"NSSet",C,N,V_recentSensorActivityAttributions) recentSensorActivityAttributions;
@property (T@"NSSet",C,N,V_activeAccessSensorActivityAttributions) activeAccessSensorActivityAttributions;
@property (T@"NSSet",C,N,V_microphoneAttributionsAwaitingMinimumOnTime) microphoneAttributionsAwaitingMinimumOnTime;
@property (T@"NSSet",C,N,V_cameraAttributionsAwaitingMinimumOnTime) cameraAttributionsAwaitingMinimumOnTime;
@property (T@"STDataAccessStatusDomain",R,N,V_dataAccessDomain) dataAccessDomain;
@property (T@"NSHashTable",R,C,N,V_observers) observers;
@property (TB,N,V_hasProcessedDomainData) hasProcessedDomainData;
@property (T@"SBSecureIndicatorMinimumOnTimeCoordinator",R,N,V_minimumOnTimeCoordinator) minimumOnTimeCoordinator;
@property (T@"<SBSecureIndicatorMinimumOnTimeCoordinatedBlockRegistration>",&,N,V_microphoneMinimumOnTimeRegistration) microphoneMinimumOnTimeRegistration;
@property (T@"<SBSecureIndicatorMinimumOnTimeCoordinatedBlockRegistration>",&,N,V_cameraMinimumOnTimeRegistration) cameraMinimumOnTimeRegistration;
@property (T@"NSSet",R,C,N) activeCameraAndMicrophoneActivityAttributions;
@property (T@"SBSensorActivityAttribution",R,C,N) mostRecentCameraAndMicrophoneSensorActivityAttribution;
@property (T@"NSSet",R,C,N) activeAndRecentSensorActivityAttributions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSensorActivityDataProvider minimumOnTimeCoordinator];
-[SBSensorActivityDataProvider setActiveAccessSensorActivityAttributions:];
-[SBSensorActivityDataProvider inactiveSensorActivityDataEligibleForMicModeSelection];
-[SBSensorActivityDataProvider microphoneAttributionsAwaitingMinimumOnTime];
-[SBSensorActivityDataProvider activeAndRecentSensorActivityAttributions];
-[SBSensorActivityDataProvider mostRecentCameraAndMicrophoneSensorActivityAttribution];
-[SBSensorActivityDataProvider removeObserver:];
-[SBSensorActivityDataProvider init];
-[SBSensorActivityDataProvider _recentCameraAndMicrophoneActivityAttributions];
-[SBSensorActivityDataProvider activeCameraAndMicrophoneActivityAttributions];
-[SBSensorActivityDataProvider dealloc];
-[SBSensorActivityDataProvider setRecentSensorActivityAttributions:];
-[SBSensorActivityDataProvider setCameraAttributionsAwaitingMinimumOnTime:];
-[SBSensorActivityDataProvider activeSensorActivityData];
-[SBSensorActivityDataProvider cameraMinimumOnTimeRegistration];
-[SBSensorActivityDataProvider _applicationEligibleForInactiveMicModeSelection];
-[SBSensorActivityDataProvider _sensorActivityDataFromSensorActivityAttribution:];
-[SBSensorActivityDataProvider activeSensorActivityAttributions];
-[SBSensorActivityDataProvider _updateActiveSensorActivityAttributions];
-[SBSensorActivityDataProvider setActiveSensorActivityAttributions:];
-[SBSensorActivityDataProvider mostRecentSensorActivityData];
-[SBSensorActivityDataProvider addObserver:];
-[SBSensorActivityDataProvider recentSensorActivityAttributions];
-[SBSensorActivityDataProvider initWithSystemStatusServer:devicePoseProvider:];
-[SBSensorActivityDataProvider hasProcessedDomainData];
-[SBSensorActivityDataProvider setMicrophoneMinimumOnTimeRegistration:];
-[SBSensorActivityDataProvider _inactiveMicModeSelectionSensorActivityDataFromApplication:];
-[SBSensorActivityDataProvider activeAccessSensorActivityAttributions];
-[SBSensorActivityDataProvider microphoneMinimumOnTimeRegistration];
-[SBSensorActivityDataProvider observers];
-[SBSensorActivityDataProvider _attributionsWithSensorType:fromAttributions:];
-[SBSensorActivityDataProvider setCameraMinimumOnTimeRegistration:];
-[SBSensorActivityDataProvider setHasProcessedDomainData:];
-[SBSensorActivityDataProvider dataAccessDomain];
-[SBSensorActivityDataProvider _notifyObserversOfActivityChange];
-[SBSensorActivityDataProvider setMicrophoneAttributionsAwaitingMinimumOnTime:];
-[SBSensorActivityDataProvider mutedMicrophoneSensorActivityData];
-[SBSensorActivityDataProvider _handleNewDomainData:];
-[SBSensorActivityDataProvider cameraAttributionsAwaitingMinimumOnTime];
```
