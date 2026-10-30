# `SBDisplayYoinkingCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDisplayContentModeTransitionObserver`, `SBSensorActivityObserver`, `PTSettingsKeyPathObserver`, `SBDisplayYoinkingControllerObserver`, `SBCompanionScenePresenterObserving`
- 12 instance variables, 5 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"SBDisplayContentModeCoordinator" _displayContentModeCoordinator;
@"SBSensorActivityDataProvider" _sensorActivityDataProvider;
@"CMFlipManager" _flipManager;
@"NSHashTable" _observers;
@"NSHashTable" _controllersWithYoinkingSliderInteractionInProgress;
@"NSHashTable" _controllersWithSlidePastTouchBlockingThreshold;
@"NSHashTable" _companionScenePresenters;
B _cameraSessionActive;
B _listeningToFlip;
B _flipActive;
B _displayToolFlipOverridden;
B _persistentFlipOverride;
```

## Properties

```
@property (TB,N,GisDisplayToolFlipOverridden) displayToolFlipOverridden;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDisplayYoinkingCoordinator activityDidChangeForSensorActivityDataProvider:];
-[SBDisplayYoinkingCoordinator removeObserver:];
-[SBDisplayYoinkingCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBDisplayYoinkingCoordinator dealloc];
-[SBDisplayYoinkingCoordinator displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBDisplayYoinkingCoordinator addObserver:];
-[SBDisplayYoinkingCoordinator companionScenePresenter:hostingDidChange:];
-[SBDisplayYoinkingCoordinator settings:changedValueForKeyPath:];
-[SBDisplayYoinkingCoordinator _setFlipActive:];
-[SBDisplayYoinkingCoordinator _anyCameraSessionCurrentlyActive];
-[SBDisplayYoinkingCoordinator _controllers:containControllerOtherThan:];
-[SBDisplayYoinkingCoordinator _setListeningToFlip:];
-[SBDisplayYoinkingCoordinator _startFlipUpdates];
-[SBDisplayYoinkingCoordinator _stopFlipUpdates];
-[SBDisplayYoinkingCoordinator _updateListeningToFlip];
-[SBDisplayYoinkingCoordinator companionScenePresenterDidInvalidate:];
-[SBDisplayYoinkingCoordinator displayYoinkingController:didChangeSlidePastTouchBlockingThreshold:];
-[SBDisplayYoinkingCoordinator displayYoinkingController:didChangeYoinkingSliderInteractionInProgress:];
-[SBDisplayYoinkingCoordinator initWithDisplayContentModeCoordinator:sensorActivityDataProvider:];
-[SBDisplayYoinkingCoordinator isDisplayToolFlipOverridden];
-[SBDisplayYoinkingCoordinator newDisplayYoinkingControllerForWindowScene:companionScenePresenter:delegate:];
-[SBDisplayYoinkingCoordinator setDisplayToolFlipOverridden:];
```
