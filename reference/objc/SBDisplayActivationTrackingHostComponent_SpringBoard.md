# `SBDisplayActivationTrackingHostComponent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `BLSHBacklightHostObserving`, `FBSceneObserver`, `FBSSceneObserver`, `SBDisplayContentModeTransitionObserver`
- 6 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _isSpringBoardScene;
B _isInTransition;
@"FBSScene" _fbsScene;
q _backlightState;
@"FBSDisplayIdentity" _latestDisplayIdentity;
@"SBWindowScene" _trackedWindowScene;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDisplayActivationTrackingHostComponent sceneWillActivate:];
-[SBDisplayActivationTrackingHostComponent scene:didUpdateSettings:];
-[SBDisplayActivationTrackingHostComponent displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBDisplayActivationTrackingHostComponent setScene:];
-[SBDisplayActivationTrackingHostComponent displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBDisplayActivationTrackingHostComponent backlight:didCompleteUpdateToState:forEvent:];
-[SBDisplayActivationTrackingHostComponent backlightHost:willTransitionToState:forEvent:];
-[SBDisplayActivationTrackingHostComponent _evaluate];
-[SBDisplayActivationTrackingHostComponent _apply:];
```
