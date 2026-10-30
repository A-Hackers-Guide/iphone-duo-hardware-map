# `SBSingleSceneController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneObserver`, `SBSceneSettingsUpdaterObserver`, `SBSceneViewControllerBuilding`, `BSInvalidatable`, `BSDescriptionProviding`
- 28 instance variables, 28 properties, 67 instance methods, 0 class methods

## Instance variables

```
@"RBSProcessIdentity" _clientIdentity;
@"<BSInvalidatable>" _settingsUpdaterObserverInvalidatable;
@"SBSceneSettingsUpdater" _sceneSettingsUpdater;
@"<UIScenePresenter>" _uiScenePresenter;
@"SBTraitsSceneParticipantDelegate" _lastSceneTraitsParticipantDelegate;
@"SBTraitsOrientedContentViewController" _orientedSceneViewController;
@"SBTraitsOrientedResizableContentViewController" _resizableOrientedSceneViewController;
B _visible;
B _shouldForegroundForDisplayConfiguration;
B _shouldActivateForDisplayConfiguration;
B _shouldActivateUponClientConnection;
B _shouldBeKeptActiveWhileForeground;
B _shouldAlwaysBeKeptActive;
B _shouldPresentAnyContentState;
B _hidden;
B _sceneContentVisible;
B _enhancedWindowingModeEnabled;
@"SBFSceneWorkspaceController" _sceneWorkspaceController;
@"UISceneRequestOptions" _sceneOptions;
@"NSString" _traitsRole;
@"FBScene" _scene;
@"<SBScenePresenting>" _presenter;
@"SBUIKitResizableSceneHostComponent" _hostComponent;
q _orientationModeOverride;
Q _initialSupportedInterfaceOrientations;
Q _supportedInterfaceOrientationsOverride;
@"FBSDisplayConfiguration" _targetDisplayConfiguration;
@"BSCornerRadiusConfiguration" _cornerRadiusConfiguration;
```

## Properties

```
@property (TB,N,V_visible) visible;
@property (T@"SBUIKitResizableSceneHostComponent",&,N,V_hostComponent) hostComponent;
@property (TB,N,V_shouldForegroundForDisplayConfiguration) shouldForegroundForDisplayConfiguration;
@property (TB,N,V_shouldActivateForDisplayConfiguration) shouldActivateForDisplayConfiguration;
@property (TB,N,V_shouldActivateUponClientConnection) shouldActivateUponClientConnection;
@property (TB,N,V_shouldBeKeptActiveWhileForeground) shouldBeKeptActiveWhileForeground;
@property (TB,N,V_shouldAlwaysBeKeptActive) shouldAlwaysBeKeptActive;
@property (TB,N,V_shouldPresentAnyContentState) shouldPresentAnyContentState;
@property (Tq,N,V_orientationModeOverride) orientationModeOverride;
@property (TQ,N,V_initialSupportedInterfaceOrientations) initialSupportedInterfaceOrientations;
@property (TQ,N,V_supportedInterfaceOrientationsOverride) supportedInterfaceOrientationsOverride;
@property (TB,N,GisHidden,V_hidden) hidden;
@property (TB,N,GisSceneActive) sceneActive;
@property (TB,N,GisSceneForeground) sceneForeground;
@property (TB,N,GisSceneContentVisible,V_sceneContentVisible) sceneContentVisible;
@property (T@"FBSDisplayConfiguration",&,N,V_targetDisplayConfiguration) targetDisplayConfiguration;
@property (T@"BSCornerRadiusConfiguration",&,N,V_cornerRadiusConfiguration) cornerRadiusConfiguration;
@property (TB,N,GisEnhancedWindowingModeEnabled,V_enhancedWindowingModeEnabled) enhancedWindowingModeEnabled;
@property (T@"SBFSceneWorkspaceController",R,N,V_sceneWorkspaceController) sceneWorkspaceController;
@property (T@"UISceneRequestOptions",R,N,V_sceneOptions) sceneOptions;
@property (T@"NSString",R,N) scenePersistentIdentifier;
@property (T@"NSString",R,N,V_traitsRole) traitsRole;
@property (T@"FBScene",R,N,V_scene) scene;
@property (T@"<SBScenePresenting>",&,N,V_presenter) presenter;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSingleSceneController isSceneActive];
-[SBSingleSceneController setTraitsParticipantNeedsPreferencesUpdateWithReason:];
-[SBSingleSceneController visible];
-[SBSingleSceneController setSceneContentVisible:];
-[SBSingleSceneController presenter];
-[SBSingleSceneController cornerRadiusConfiguration];
-[SBSingleSceneController sceneDidInvalidate:withContext:];
-[SBSingleSceneController traitsOrientedResizableViewController];
-[SBSingleSceneController setVisible:];
-[SBSingleSceneController debugDescription];
-[SBSingleSceneController setShouldBeKeptActiveWhileForeground:];
-[SBSingleSceneController setHidden:];
-[SBSingleSceneController succinctDescriptionBuilder];
-[SBSingleSceneController setPresenter:];
-[SBSingleSceneController setShouldForegroundForDisplayConfiguration:];
-[SBSingleSceneController initialSupportedInterfaceOrientations];
-[SBSingleSceneController scene:didUpdateSettings:];
-[SBSingleSceneController _evaluateSceneForegroundState];
-[SBSingleSceneController _evaluateVisibility];
-[SBSingleSceneController setInitialSupportedInterfaceOrientations:];
-[SBSingleSceneController isSceneContentVisible];
-[SBSingleSceneController setCornerRadiusConfiguration:];
-[SBSingleSceneController shouldActivateUponClientConnection];
-[SBSingleSceneController sceneOptions];
-[SBSingleSceneController _isClientProcessRunning];
-[SBSingleSceneController orientationModeOverride];
-[SBSingleSceneController setEnhancedWindowingModeEnabled:];
-[SBSingleSceneController setOrientationModeOverride:];
-[SBSingleSceneController sceneWorkspaceController];
-[SBSingleSceneController dealloc];
-[SBSingleSceneController setShouldPresentAnyContentState:];
-[SBSingleSceneController sceneContentStateDidChange:];
-[SBSingleSceneController scenePersistentIdentifier];
-[SBSingleSceneController isSceneForeground];
-[SBSingleSceneController setHostComponent:];
-[SBSingleSceneController shouldAlwaysBeKeptActive];
-[SBSingleSceneController traitsRole];
-[SBSingleSceneController descriptionWithMultilinePrefix:];
-[SBSingleSceneController isEnhancedWindowingModeEnabled];
-[SBSingleSceneController initWithSceneWorkspaceController:sceneRequestOptions:clientIdentity:traitsRole:level:];
-[SBSingleSceneController setTargetDisplayConfiguration:];
-[SBSingleSceneController supportedInterfaceOrientationsOverride];
-[SBSingleSceneController succinctDescription];
-[SBSingleSceneController _newActivationContext];
-[SBSingleSceneController invalidate];
-[SBSingleSceneController shouldForegroundForDisplayConfiguration];
-[SBSingleSceneController _dismissScene];
-[SBSingleSceneController _presentScene];
-[SBSingleSceneController isHidden];
-[SBSingleSceneController shouldBeKeptActiveWhileForeground];
-[SBSingleSceneController setSupportedInterfaceOrientationsOverride:];
-[SBSingleSceneController scene];
-[SBSingleSceneController setShouldAlwaysBeKeptActive:];
-[SBSingleSceneController setSceneActive:];
-[SBSingleSceneController setSceneForeground:];
-[SBSingleSceneController description];
-[SBSingleSceneController didUpdateSceneTraitsDelegate:];
-[SBSingleSceneController shouldActivateForDisplayConfiguration];
-[SBSingleSceneController hostComponent];
-[SBSingleSceneController _evaluateSceneActivationState];
-[SBSingleSceneController _setVisible:];
-[SBSingleSceneController traitsOrientedViewController];
-[SBSingleSceneController setShouldActivateUponClientConnection:];
-[SBSingleSceneController setShouldActivateForDisplayConfiguration:];
-[SBSingleSceneController targetDisplayConfiguration];
-[SBSingleSceneController descriptionBuilderWithMultilinePrefix:];
-[SBSingleSceneController shouldPresentAnyContentState];
```
