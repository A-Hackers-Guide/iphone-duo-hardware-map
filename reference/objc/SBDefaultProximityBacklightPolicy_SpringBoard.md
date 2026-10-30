# `SBDefaultProximityBacklightPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBProximityBacklightPolicy`
- 7 instance variables, 7 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"SBBacklightController" _backlightController;
@"<BSInvalidatable>" _idleTimerDisableAssertion;
@"<BSInvalidatable>" _captureButtonSuppressionAssertion;
B _scheduled;
@"SBIdleTimerGlobalCoordinator" _idleTimerGlobalCoordinator;
@"SBSystemGestureManager" _systemGestureManager;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBSystemGestureManager",&,N,V_systemGestureManager) systemGestureManager;
@property (T@"SBIdleTimerGlobalCoordinator",&,N,V_idleTimerGlobalCoordinator) idleTimerGlobalCoordinator;
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDefaultProximityBacklightPolicy setSystemGestureManager:];
-[SBDefaultProximityBacklightPolicy setWindowScene:];
-[SBDefaultProximityBacklightPolicy windowSceneDidDisconnect:];
-[SBDefaultProximityBacklightPolicy dealloc];
-[SBDefaultProximityBacklightPolicy initWithConfiguration:];
-[SBDefaultProximityBacklightPolicy systemGestureManager];
-[SBDefaultProximityBacklightPolicy windowSceneDidConnect:];
-[SBDefaultProximityBacklightPolicy windowScene];
-[SBDefaultProximityBacklightPolicy idleTimerGlobalCoordinator];
-[SBDefaultProximityBacklightPolicy _backlightWillUndim:];
-[SBDefaultProximityBacklightPolicy _cancelScheduledBacklightFactorToZero];
-[SBDefaultProximityBacklightPolicy _restoreBacklightFactor];
-[SBDefaultProximityBacklightPolicy _scheduleBacklightFactorToZeroAfterDebounceDuration:];
-[SBDefaultProximityBacklightPolicy _scheduleBacklightFactorToZeroAfterDefaultDuration];
-[SBDefaultProximityBacklightPolicy _turnBacklightOff];
-[SBDefaultProximityBacklightPolicy proximitySensorManager:objectWithinProximityDidChange:];
-[SBDefaultProximityBacklightPolicy setIdleTimerGlobalCoordinator:];
```
