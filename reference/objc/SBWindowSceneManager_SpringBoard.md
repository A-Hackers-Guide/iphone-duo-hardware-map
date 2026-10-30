# `SBWindowSceneManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDisplayContentModeTransitionObserver`, `SBLastInteractedSceneObserver`, `SBMultiDisplayUserInteractionCoordinatorDelegate`, `SBLastInteractedSceneProviding`
- 5 instance variables, 14 properties, 37 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _mutableConnectedWindowScenes;
@"SBMultiDisplayUserInteractionCoordinator" _userInteractionCoordinator;
@"SBDisplayContentModeCoordinator" _displayContentModeCoordinator;
@"SBSceneManager" _sceneManager;
@"NSHashTable" _lastInteractedSceneObservers;
```

## Properties

```
@property (T@"NSMutableSet",R,N,V_mutableConnectedWindowScenes) mutableConnectedWindowScenes;
@property (T@"SBMultiDisplayUserInteractionCoordinator",&,N,V_userInteractionCoordinator) userInteractionCoordinator;
@property (T@"SBDisplayContentModeCoordinator",&,N,V_displayContentModeCoordinator) displayContentModeCoordinator;
@property (T@"SBSceneManager",&,N,V_sceneManager) sceneManager;
@property (T@"NSHashTable",&,N,V_lastInteractedSceneObservers) lastInteractedSceneObservers;
@property (T@"NSSet",R,C,N) connectedWindowScenes;
@property (T@"SBWindowScene",R,N) activeDisplayWindowScene;
@property (T@"NSArray",R,N) restartSnapshotDisplays;
@property (T@"CADisplay",R,N) activeRestartSnapshotDisplay;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"FBScene",R,N) lastInteractedScene;
```

## Instance methods

```
-[SBWindowSceneManager sceneManager];
-[SBWindowSceneManager initWithSceneManager:userInteractionCoordinator:displayContentModeCoordinator:];
-[SBWindowSceneManager removeLastInteractedSceneObserver:];
-[SBWindowSceneManager restartSnapshotDisplays];
-[SBWindowSceneManager displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBWindowSceneManager _integratedDisplayForWindowScene:];
-[SBWindowSceneManager _validateSuggestedActiveWindowScene:];
-[SBWindowSceneManager displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBWindowSceneManager windowSceneForPersistentIdentifier:];
-[SBWindowSceneManager _extendedDisplayWindowScene];
-[SBWindowSceneManager setLastInteractedSceneObservers:];
-[SBWindowSceneManager addLastInteractedSceneObserver:];
-[SBWindowSceneManager windowSceneForKeyboardFocus];
-[SBWindowSceneManager mutableConnectedWindowScenes];
-[SBWindowSceneManager connectedWindowScenes];
-[SBWindowSceneManager _continuityDisplayWindowScene];
-[SBWindowSceneManager setUserInteractionCoordinator:];
-[SBWindowSceneManager windowSceneForSceneHandle:];
-[SBWindowSceneManager _bringupDisplayWindowScene];
-[SBWindowSceneManager windowSceneForSceneIdentifier:];
-[SBWindowSceneManager windowSceneForAlertItems];
-[SBWindowSceneManager setDisplayContentModeCoordinator:];
-[SBWindowSceneManager lastInteractedSceneObservers];
-[SBWindowSceneManager activeDisplayWindowScene];
-[SBWindowSceneManager _sceneWillConnect:];
-[SBWindowSceneManager windowSceneForHardwareIdentifier:];
-[SBWindowSceneManager embeddedDisplayWindowScene];
-[SBWindowSceneManager windowSceneForDisplayConfigurationForClassicApps];
-[SBWindowSceneManager _sceneDidDisconnect:];
-[SBWindowSceneManager lastInteractedScene];
-[SBWindowSceneManager setSceneManager:];
-[SBWindowSceneManager activeRestartSnapshotDisplay];
-[SBWindowSceneManager lastInteractedSceneProvider:didUpdateLastInteractedScene:];
-[SBWindowSceneManager userInteractionCoordinator];
-[SBWindowSceneManager displayContentModeCoordinator];
-[SBWindowSceneManager windowSceneForDisplayIdentity:];
-[SBWindowSceneManager _embeddedDisplayWindowScene];
```
