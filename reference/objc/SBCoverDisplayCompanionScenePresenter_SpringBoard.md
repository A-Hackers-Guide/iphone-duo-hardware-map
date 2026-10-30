# `SBCoverDisplayCompanionScenePresenter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBCompanionScenePresenter`
- Protocols: `SBFSensorActivityObserver`, `SBCompanionSceneRestrictionCoordinatorObserver`
- 4 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"<SBFSensorActivityDataProvider>" _sensorActivityDataProvider;
@"<SBFSensorActivityAttribution>" _activeCameraActivityAttribution;
@"<BSInvalidatable>" _noCameraSessionActiveRestriction;
B _ignoresOrientationLock;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBCoverDisplayCompanionScenePresenter defaultSupportedOrientations];
```

## Instance methods

```
-[SBCoverDisplayCompanionScenePresenter activityDidChangeForSensorActivityDataProvider:];
-[SBCoverDisplayCompanionScenePresenter invalidate];
-[SBCoverDisplayCompanionScenePresenter _activeCameraActivityAttributionFromDataProvider:];
-[SBCoverDisplayCompanionScenePresenter _activeCameraProcessIdentityForAttribution:];
-[SBCoverDisplayCompanionScenePresenter _lifecycleConstraintsWithCameraSessionProcessIdentity:];
-[SBCoverDisplayCompanionScenePresenter _updateAvailableCompanionModesForActive:];
-[SBCoverDisplayCompanionScenePresenter companionSceneRestrictionCoordinator:didBeginRestrictingPresentationMode:];
-[SBCoverDisplayCompanionScenePresenter companionSceneRestrictionCoordinator:didEndRestrictingPresentationMode:];
-[SBCoverDisplayCompanionScenePresenter ignoresOrientationLock];
-[SBCoverDisplayCompanionScenePresenter initWithWindowScene:restrictionCoordinator:sensorActivityDataProvider:];
-[SBCoverDisplayCompanionScenePresenter supportedOrientationsForClientHandle:];
```
