# `SBSceneManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSSceneDelegateWithActionHandlers`, `FBSceneManagerDelegate`, `FBSceneDelegate`, `FBSceneWorkspaceDelegate`, `BSDescriptionProviding`
- 16 instance variables, 5 properties, 46 instance methods, 0 class methods

## Instance variables

```
@"FBSceneManager" _fbSceneManager;
@"NSMapTable" _persistentMapSceneIdentityToSceneHandle;
@"NSMapTable" _transientMapSceneIdentityToSceneHandle;
@"BSCopyingCacheSet" _allScenes;
@"BSCopyingCacheSet" _daemonScenes;
@"BSCopyingCacheSet" _workspaceScenes;
@"BSCopyingCacheSet" _externalApplicationSceneHandles;
@"BSCopyingCacheSet" _externalForegroundApplicationSceneHandles;
@"BSCopyingCacheSet" _reportedExternalForegroundApplicationSceneHandles;
@"NSCountedSet" _assertedBackgroundScenes;
@"UIApplicationSceneDeactivationManager" _sceneDeactivationManager;
@"NSHashTable" _observers;
@"NSMutableSet" _workspaceIdentifiersToIgnore;
@"NSMapTable" _blsActionHandlersForScenes;
@"<BSInvalidatable>" _stateCaptureInvalidatable;
@"SBApplicationController" _applicationController;
```

## Properties

```
@property (T@"UIApplicationSceneDeactivationManager",R,N,V_sceneDeactivationManager) sceneDeactivationManager;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSceneManager sceneDidDeactivate:withContext:];
-[SBSceneManager scene:clientDidConnect:];
-[SBSceneManager sceneWillDeactivate:withContext:];
-[SBSceneManager sceneDidInvalidate:withContext:];
-[SBSceneManager debugDescription];
-[SBSceneManager succinctDescriptionBuilder];
-[SBSceneManager removeObserver:];
-[SBSceneManager scene:didUpdateSettings:];
-[SBSceneManager scene:handleActions:];
-[SBSceneManager sceneDidActivate:];
-[SBSceneManager initWithApplicationController:];
-[SBSceneManager dealloc];
-[SBSceneManager descriptionWithMultilinePrefix:];
-[SBSceneManager scene:willUpdateSettings:];
-[SBSceneManager succinctDescription];
-[SBSceneManager addObserver:];
-[SBSceneManager description];
-[SBSceneManager sceneManager:clientDidConnectWithHandshake:];
-[SBSceneManager workspace:didReceiveActions:];
-[SBSceneManager scene:didUpdateClientSettings:];
-[SBSceneManager sceneManager:didAddScene:];
-[SBSceneManager descriptionBuilderWithMultilinePrefix:];
-[SBSceneManager _addScene:];
-[SBSceneManager allScenes];
-[SBSceneManager sceneManager:didReceiveSceneRequestWithOptions:fromProcess:completion:];
-[SBSceneManager externalApplicationSceneHandles];
-[SBSceneManager _addInitialSceneExtensionsToScene:];
-[SBSceneManager _addReportedForegroundExternalApplicationSceneHandle:];
-[SBSceneManager _addSceneExtensionsToConnectedScene:];
-[SBSceneManager _createSceneForApplication:withOptions:completion:];
-[SBSceneManager _reconnectSceneRemnant:forProcess:sceneManager:];
-[SBSceneManager _removeReportedForegroundExternalApplicationSceneHandle:];
-[SBSceneManager _updateStateForScene:withSettings:];
-[SBSceneManager addActionHandler:forScene:];
-[SBSceneManager assertBackgroundedStatusForScenes:];
-[SBSceneManager daemonScenes];
-[SBSceneManager existingSceneHandleForPersistenceIdentifier:];
-[SBSceneManager existingSceneHandleForScene:];
-[SBSceneManager existingSceneHandleForSceneIdentity:];
-[SBSceneManager externalApplicationSceneHandlesForBundleIdentifiers:];
-[SBSceneManager externalForegroundApplicationSceneHandles];
-[SBSceneManager fetchOrCreateApplicationSceneHandleForRequest:];
-[SBSceneManager fetchOrCreateApplicationSceneHandleForScene:application:];
-[SBSceneManager removeActionHandler:forScene:];
-[SBSceneManager sceneDeactivationManager];
-[SBSceneManager transientApplicationSceneHandlesForApplication:];
```
