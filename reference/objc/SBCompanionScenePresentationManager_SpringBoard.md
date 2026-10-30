# `SBCompanionScenePresentationManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBCompanionScenePresenterObserving`, `BSDescriptionStreaming`
- 7 instance variables, 11 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"SBCompanionSceneRestrictionCoordinator" _restrictionCoordinator;
@"SBThermalController" _thermalController;
@"<SBFSensorActivityDataProvider>" _sensorActivityDataProvider;
@"NSMutableSet" _hostScenes;
@"NSMutableSet" _presenters;
@"<BSInvalidatable>" _thermallyBlockedPresentationRestriction;
@"<BSInvalidatable>" _lowPowerModePresentationRestriction;
```

## Properties

```
@property (T@"SBCompanionSceneRestrictionCoordinator",R,N,V_restrictionCoordinator) restrictionCoordinator;
@property (T@"SBThermalController",R,N,V_thermalController) thermalController;
@property (T@"<SBFSensorActivityDataProvider>",R,N,V_sensorActivityDataProvider) sensorActivityDataProvider;
@property (T@"NSMutableSet",R,N,V_hostScenes) hostScenes;
@property (T@"NSMutableSet",R,N,V_presenters) presenters;
@property (T@"<BSInvalidatable>",R,N,V_thermallyBlockedPresentationRestriction) thermallyBlockedPresentationRestriction;
@property (T@"<BSInvalidatable>",R,N,V_lowPowerModePresentationRestriction) lowPowerModePresentationRestriction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCompanionScenePresentationManager sensorActivityDataProvider];
-[SBCompanionScenePresentationManager _lowPowerModeChanged:];
-[SBCompanionScenePresentationManager presenters];
-[SBCompanionScenePresentationManager description];
-[SBCompanionScenePresentationManager appendDescriptionToStream:];
-[SBCompanionScenePresentationManager _addPresenter:];
-[SBCompanionScenePresentationManager _removePresenter:];
-[SBCompanionScenePresentationManager _thermalLevelChanged:];
-[SBCompanionScenePresentationManager acquireCompanionScenePresenterForWindowScene:];
-[SBCompanionScenePresentationManager companionScenePresenterDidInvalidate:];
-[SBCompanionScenePresentationManager hostScenes];
-[SBCompanionScenePresentationManager initWithRestrictionCoordinator:thermalController:sensorActivityDataProvider:];
-[SBCompanionScenePresentationManager lowPowerModePresentationRestriction];
-[SBCompanionScenePresentationManager registerHostScene:forPresentationModes:];
-[SBCompanionScenePresentationManager registeredHostScenes];
-[SBCompanionScenePresentationManager restrictionCoordinator];
-[SBCompanionScenePresentationManager thermalController];
-[SBCompanionScenePresentationManager thermallyBlockedPresentationRestriction];
-[SBCompanionScenePresentationManager unregisterHostScene:];
```
