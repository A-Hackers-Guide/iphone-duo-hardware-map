# `SBProximityBacklightPolicy` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `SBProximitySensorManagerObserver`, `SBWindowSceneAttachmentObserving`
- 0 instance variables, 3 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"SBSystemGestureManager",&,N) systemGestureManager;
@property (T@"SBIdleTimerGlobalCoordinator",&,N) idleTimerGlobalCoordinator;
@property (T@"SBWindowScene",W,N) windowScene;
```

## Instance methods

```
-[SBProximityBacklightPolicy setSystemGestureManager:];
-[SBProximityBacklightPolicy setWindowScene:];
-[SBProximityBacklightPolicy systemGestureManager];
-[SBProximityBacklightPolicy windowScene];
-[SBProximityBacklightPolicy idleTimerGlobalCoordinator];
-[SBProximityBacklightPolicy setIdleTimerGlobalCoordinator:];
```
