# `SBSystemUISceneController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBProcessManagerObserver`, `FBProcessObserver`, `SBBacklightControllerObserver`, `SBFDevicePoseProviderObserver`, `SBDisplayContentModeTransitionObserver`, `SBScenePresentingDelegate`, `SBWindowSceneAttachmentObserving`, `SBFSceneWorkspaceControlling`, `SBButtonEventsHandler`, `BSDescriptionProviding`
- 15 instance variables, 12 properties, 76 instance methods, 1 class methods

## Instance variables

```
@"FBProcess" _clientProcess;
@"RBSProcessHandle" _clientProcessHandle;
Q _sceneIDGeneration;
@"<BSInvalidatable>" _stateCaptureInvalidatable;
@"NSMutableArray" _sceneControllers;
@"NSPointerArray" _presenters;
@"NSMapTable" _sceneControllersByDisplayIdentity;
@"RBSProcessIdentity" _clientProcessIdentity;
q _sceneVendingPolicy;
@"NSString" _traitsRole;
@"NSString" _jobLabel;
d _level;
@"SBFSceneWorkspaceDefaultDelegate" _sceneWorkspaceControllerDelegate;
@"SBFSceneWorkspaceController" _sceneWorkspaceController;
@"SBSystemUISceneDefaultPresenter" _defaultPresenter;
```

## Properties

```
@property (T@"SBFSceneWorkspaceDefaultDelegate",&,N,V_sceneWorkspaceControllerDelegate) sceneWorkspaceControllerDelegate;
@property (T@"SBFSceneWorkspaceController",R,N,V_sceneWorkspaceController) sceneWorkspaceController;
@property (T@"SBSystemUISceneDefaultPresenter",&,N,V_defaultPresenter) defaultPresenter;
@property (T@"RBSProcessIdentity",R,N,V_clientProcessIdentity) clientProcessIdentity;
@property (Tq,R,N,V_sceneVendingPolicy) sceneVendingPolicy;
@property (T@"NSString",R,C,N,V_traitsRole) traitsRole;
@property (T@"NSString",R,C,N,V_jobLabel) jobLabel;
@property (Td,R,N,V_level) level;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSystemUISceneController _setupInfo];
```

## Instance methods

```
-[SBSystemUISceneController enumerateScenesWithBlock:];
-[SBSystemUISceneController backlightController:didTransitionToBacklightState:source:];
-[SBSystemUISceneController addPresenter:];
-[SBSystemUISceneController destroyScenesWithPersistentIdentifiers:processIdentity:completion:];
-[SBSystemUISceneController handleVolumeDownButtonPress];
-[SBSystemUISceneController initWithSceneWorkspaceIdentifier:clientProcessIdentity:sceneVendingPolicy:traitsRole:jobLabel:level:];
-[SBSystemUISceneController willEnableSecureRendering:];
-[SBSystemUISceneController debugDescription];
-[SBSystemUISceneController _shouldUpdateEnhancedWindowingModeForScenes];
-[SBSystemUISceneController handleHomeButtonLongPress];
-[SBSystemUISceneController succinctDescriptionBuilder];
-[SBSystemUISceneController _evaluateSceneForegroundState];
-[SBSystemUISceneController windowSceneDidDisconnect:];
-[SBSystemUISceneController processManager:didAddProcess:];
-[SBSystemUISceneController displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBSystemUISceneController handleVoiceCommandButtonPress];
-[SBSystemUISceneController sceneWorkspaceController];
-[SBSystemUISceneController dealloc];
-[SBSystemUISceneController displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBSystemUISceneController activateSceneForProcessIdentity:withHandle:options:completion:];
-[SBSystemUISceneController _evaluateAvailablePresenters:forSceneControllers:];
-[SBSystemUISceneController handleHeadsetButtonPress:];
-[SBSystemUISceneController jobLabel];
-[SBSystemUISceneController level];
-[SBSystemUISceneController scenePresenter:willDismissScene:];
-[SBSystemUISceneController handleLockButtonPress];
-[SBSystemUISceneController traitsRole];
-[SBSystemUISceneController descriptionWithMultilinePrefix:];
-[SBSystemUISceneController handleVolumeUpButtonPress];
-[SBSystemUISceneController _isAllowedToRecreateSceneOnConnectingWindowScene:];
-[SBSystemUISceneController _invalidateSceneControllersForWindowScene:];
-[SBSystemUISceneController succinctDescription];
-[SBSystemUISceneController handleHomeButtonDoublePress];
-[SBSystemUISceneController poseProvider:didUpdateFromPose:toPose:];
-[SBSystemUISceneController _canShowWhileLocked];
-[SBSystemUISceneController processDidExit:];
-[SBSystemUISceneController scenePresenter:didPresentScene:];
-[SBSystemUISceneController sceneFromIdentityToken:];
-[SBSystemUISceneController processManager:didRemoveProcess:];
-[SBSystemUISceneController _shouldHideForInvalidClientProcess];
-[SBSystemUISceneController _requiresKeyboard];
-[SBSystemUISceneController _isDefaultPresenterDelegate];
-[SBSystemUISceneController description];
-[SBSystemUISceneController _invalidateAllSceneControllers];
-[SBSystemUISceneController _newSceneControllerForWindowScene:sceneRequestOptions:traitsRole:level:];
-[SBSystemUISceneController windowSceneDidConnect:];
-[SBSystemUISceneController didDisableSecureRendering:];
-[SBSystemUISceneController sceneWorkspaceControllerForProcessIdentity:];
-[SBSystemUISceneController sceneFromIdentityTokenStringRepresentation:];
-[SBSystemUISceneController handleHomeButtonPress];
-[SBSystemUISceneController descriptionBuilderWithMultilinePrefix:];
-[SBSystemUISceneController _newAppSceneRequestOptionsForWindowScene:withBlueprintOptions:];
-[SBSystemUISceneController defaultPresenter];
-[SBSystemUISceneController _presenterArray];
-[SBSystemUISceneController __newSceneIdentifierForWindowScene:sessionRole:];
-[SBSystemUISceneController _cornerRadiusConfigurationForWindowScene:];
-[SBSystemUISceneController _evaluateSceneVisibility];
-[SBSystemUISceneController _moveSceneController:toWindowScene:];
-[SBSystemUISceneController _newSceneControllerForWindowScene:withSceneRequestOptions:];
-[SBSystemUISceneController _removeSceneController:];
-[SBSystemUISceneController _sceneControllerWithScene:];
-[SBSystemUISceneController _secureDisplayModeDidChangeForSceneControllersOnWindowScene:];
-[SBSystemUISceneController _setNeedsPresentersEvaluation];
-[SBSystemUISceneController _shouldUpdateDisplayConfigurationForScenes];
-[SBSystemUISceneController _updateClientProcess:];
-[SBSystemUISceneController _updateDisplayConfiguration:forSceneControllerWithScene:];
-[SBSystemUISceneController _updateEnhancedWindowingModeEnabled:forSceneControllerWithScene:];
-[SBSystemUISceneController clientProcessIdentity];
-[SBSystemUISceneController scenePresenter:updateDisplayConfiguration:forScene:];
-[SBSystemUISceneController scenePresenter:updateEnhancedWindowingModeEnabled:forScene:];
-[SBSystemUISceneController scenePresenter:updateHomeAffordance:forScene:];
-[SBSystemUISceneController scenePresenterVisibilityDidChange:];
-[SBSystemUISceneController sceneVendingPolicy];
-[SBSystemUISceneController sceneWorkspaceControllerDelegate];
-[SBSystemUISceneController setDefaultPresenter:];
-[SBSystemUISceneController setSceneWorkspaceControllerDelegate:];
```
