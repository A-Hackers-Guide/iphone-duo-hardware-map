# `SBAppResizingCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBLastInteractedSceneObserver`
- 10 instance variables, 8 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"SBAppResizingService" _resizingService;
@"SBSceneManager" _sceneManager;
@"SBWindowSceneManager" _windowSceneManager;
@"NSHashTable" _observedWindowScenes;
@"NSHashTable" _observers;
@"SBDeviceApplicationSceneHandle" _lastInteractedResizableSceneHandle;
B _resizingPossible;
B _lastNotifiedResizingPossible;
@"LSApplicationIdentity" _lastNotifiedResizableApplication;
@"SBAppResizingSession" _currentSession;
```

## Properties

```
@property (T@"SBAppResizingSession",R,N,V_currentSession) currentSession;
@property (TB,R,N,GisResizingPossible) resizingPossible;
@property (T@"LSApplicationIdentity",R,N) resizableApplication;
@property (T{CGSize=dd},R,N) preferredSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAppResizingCoordinator removeObserver:];
-[SBAppResizingCoordinator windowSceneDidDisconnect:];
-[SBAppResizingCoordinator dealloc];
-[SBAppResizingCoordinator addObserver:];
-[SBAppResizingCoordinator currentSession];
-[SBAppResizingCoordinator windowSceneDidConnect:];
-[SBAppResizingCoordinator lastInteractedSceneProvider:didUpdateLastInteractedScene:];
-[SBAppResizingCoordinator preferredSize];
-[SBAppResizingCoordinator isResizingPossible];
-[SBAppResizingCoordinator resizableApplication];
-[SBAppResizingCoordinator resizingService];
-[SBAppResizingCoordinator _notifyResizingChangedIfNeeded];
-[SBAppResizingCoordinator _setLastInteractedResizableSceneHandle:];
-[SBAppResizingCoordinator acquireSessionForDisplay:monitoredWindowScene:resizingCornerRadius:];
-[SBAppResizingCoordinator initWithSceneManager:displayProfileManager:windowSceneManager:startupInterfaceOrientation:];
-[SBAppResizingCoordinator resizingSessionDidActivate:];
-[SBAppResizingCoordinator resizingSessionDidInvalidate:];
```
