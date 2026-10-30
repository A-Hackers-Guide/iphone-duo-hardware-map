# `SBSecureAppManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBLayoutStateTransitionObserver`
- 6 instance variables, 12 properties, 33 instance methods, 1 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"NSMutableDictionary" _secureAppActions;
@"NSMutableArray" _remoteAlertActions;
@"NSHashTable" _observers;
@"NSHashTable" _wakeDestinationProviders;
@"NSMapTable" _transitionCoordinatorsByWindowScene;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_secureAppActions) secureAppActions;
@property (T@"NSMutableArray",&,N,V_remoteAlertActions) remoteAlertActions;
@property (T@"NSHashTable",&,N,V_observers) observers;
@property (T@"NSHashTable",&,N,V_wakeDestinationProviders) wakeDestinationProviders;
@property (T@"NSMapTable",&,N,V_transitionCoordinatorsByWindowScene) transitionCoordinatorsByWindowScene;
@property (TB,R,N) hasSecureApp;
@property (TB,R,N) hasWakeDestination;
@property (T@"SBWakeDestination",R,N) wakeDestination;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSecureAppManager sharedInstance];
```

## Instance methods

```
-[SBSecureAppManager removeObserver:];
-[SBSecureAppManager initWithApplicationController:];
-[SBSecureAppManager addObserver:];
-[SBSecureAppManager layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBSecureAppManager setObservers:];
-[SBSecureAppManager observers];
-[SBSecureAppManager secureAppAction];
-[SBSecureAppManager wakeDestination];
-[SBSecureAppManager _addRemoteAlertLockScreenContentAction:];
-[SBSecureAppManager _addSecureAppAction:];
-[SBSecureAppManager _applicationForAction:];
-[SBSecureAppManager _applicationSceneEntityForAction:windowScene:];
-[SBSecureAppManager _enumerateSecureAppActionsByPriorityUsingBlock:];
-[SBSecureAppManager _enumerateSecureAppActionsOfType:usingBlock:];
-[SBSecureAppManager _transitionCoordinatorCanReportSecureAppUserDismissal:];
-[SBSecureAppManager addLockScreenContentAction:];
-[SBSecureAppManager addWakeDestinationProvider:];
-[SBSecureAppManager hasSecureApp];
-[SBSecureAppManager hasSecureAppOfType:];
-[SBSecureAppManager hasWakeDestination];
-[SBSecureAppManager newApplicationSceneEntityForCurrentSecureAppOnWindowScene:];
-[SBSecureAppManager newHostableEntityForCurrentSecureApp];
-[SBSecureAppManager remoteAlertActions];
-[SBSecureAppManager removeWakeDestinationProvider:];
-[SBSecureAppManager secureAppActions];
-[SBSecureAppManager secureAppTransitionCoordinatorForWindowScene:];
-[SBSecureAppManager setRemoteAlertActions:];
-[SBSecureAppManager setSecureAppActions:];
-[SBSecureAppManager setSecureAppTransitionCoordinator:forWindowScene:];
-[SBSecureAppManager setTransitionCoordinatorsByWindowScene:];
-[SBSecureAppManager setWakeDestinationProviders:];
-[SBSecureAppManager transitionCoordinatorsByWindowScene];
-[SBSecureAppManager wakeDestinationProviders];
```
