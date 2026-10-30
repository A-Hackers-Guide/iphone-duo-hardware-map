# `SBUnavailableProximityBacklightPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBProximityBacklightPolicy`
- 3 instance variables, 7 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SBSystemGestureManager" _systemGestureManager;
@"SBIdleTimerGlobalCoordinator" _idleTimerGlobalCoordinator;
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
-[SBUnavailableProximityBacklightPolicy setSystemGestureManager:];
-[SBUnavailableProximityBacklightPolicy setWindowScene:];
-[SBUnavailableProximityBacklightPolicy windowSceneDidDisconnect:];
-[SBUnavailableProximityBacklightPolicy systemGestureManager];
-[SBUnavailableProximityBacklightPolicy windowSceneDidConnect:];
-[SBUnavailableProximityBacklightPolicy windowScene];
-[SBUnavailableProximityBacklightPolicy idleTimerGlobalCoordinator];
-[SBUnavailableProximityBacklightPolicy setIdleTimerGlobalCoordinator:];
```
