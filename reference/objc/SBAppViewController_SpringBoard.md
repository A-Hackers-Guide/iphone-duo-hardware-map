# `SBAppViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBDeviceApplicationSceneHandleObserver`, `SBWorkspaceApplicationSceneTransitionContextDelegate`, `SBDeviceApplicationSceneViewControllerDelegate`, `SBApplicationSceneUpdateTransactionDelegate`, `SBApplicationHosting`, `SBApplicationSceneViewControlling`, `BSInvalidatable`
- 18 instance variables, 24 properties, 88 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
@"SBDeviceApplicationSceneHandle" _sceneHandle;
@"SBDeviceApplicationSceneViewController" _deviceAppViewController;
@"SBActivationSettings" _activationSettings;
@"<SBScenePlaceholderContentContext>" _placeholderContentContext;
@"NSMutableSet" _activeTransitions;
@"NSSet" _actionsToDeliver;
q _requestedMode;
q _currentMode;
B _sceneContentIsReady;
B _ignoresOcclusions;
B _invalidated;
B _automatesLifecycle;
B _placeholderContentEnabled;
B _wantsSecureRendering;
@"<SBApplicationSceneViewControllingStatusBarDelegate>" applicationSceneStatusBarDelegate;
@"<SBAppViewControllerDelegate>" _delegate;
@"SBActivationSettings" _supplementalActivationSettings;
```

## Properties

```
@property (T@"<SBAppViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_automatesLifecycle) automatesLifecycle;
@property (Tq,N,V_requestedMode) requestedMode;
@property (Tq,R,N,V_currentMode) currentMode;
@property (T@"SBApplicationSceneView",R,N) appView;
@property (TB,N,V_ignoresOcclusions) ignoresOcclusions;
@property (T@"NSSet",&,N,V_actionsToDeliver) actionsToDeliver;
@property (TB,N,V_wantsSecureRendering) wantsSecureRendering;
@property (TB,N,V_placeholderContentEnabled) placeholderContentEnabled;
@property (T@"SBActivationSettings",&,N,V_supplementalActivationSettings) supplementalActivationSettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SBApplicationSceneHandle",R,N,V_sceneHandle) sceneHandle;
@property (Td,R,N) statusBarAlpha;
@property (Tq,R,N) overrideStatusBarStyle;
@property (T@"<SBApplicationSceneViewControllingStatusBarDelegate>",W,N,VapplicationSceneStatusBarDelegate) applicationSceneStatusBarDelegate;
@property (Tq,R,N) displayMode;
@property (T@"<SBScenePlaceholderContentContext>",&,N,V_placeholderContentContext) placeholderContentContext;
@property (T@"UIView",&,N) customContentView;
@property (T{CGSize=dd},R,N) contentReferenceSize;
@property (Tq,R,N) contentOrientation;
@property (Tq,R,N) containerOrientation;
```

## Instance methods

```
-[SBAppViewController sceneHandle:didDestroyScene:];
-[SBAppViewController sceneHandle:didCreateScene:];
-[SBAppViewController customContentView];
-[SBAppViewController setCustomContentView:];
-[SBAppViewController statusBarAlpha];
-[SBAppViewController containerOrientation];
-[SBAppViewController sceneHandle:didUpdateContentState:];
-[SBAppViewController requestedMode];
-[SBAppViewController currentMode];
-[SBAppViewController supplementalActivationSettings];
-[SBAppViewController sceneHandle];
-[SBAppViewController _sendActions:];
-[SBAppViewController actionsToDeliver];
-[SBAppViewController viewIsAppearing:];
-[SBAppViewController viewWillDisappear:];
-[SBAppViewController ignoresOcclusions];
-[SBAppViewController setApplicationSceneStatusBarDelegate:];
-[SBAppViewController setRequestedMode:];
-[SBAppViewController setPlaceholderContentContext:];
-[SBAppViewController sceneHandle:didUpdateSettingsWithDiff:previousSettings:];
-[SBAppViewController beginInteractiveDisplayModeTransitionToMode:];
-[SBAppViewController _primeParentSceneForChildScene:];
-[SBAppViewController contentOrientation];
-[SBAppViewController dealloc];
-[SBAppViewController applicationSceneViewController:didRequestWindowControlsAdaptiveStyle:adaptive:];
-[SBAppViewController displayMode];
-[SBAppViewController containerContentWrapperInterfaceOrientationChangedTo:];
-[SBAppViewController applicationTransitionContext:frameForApplicationSceneEntity:];
-[SBAppViewController initWithIdentifier:andApplicationSceneEntity:];
-[SBAppViewController willMoveToParentViewController:];
-[SBAppViewController setWantsSecureRendering:];
-[SBAppViewController wantsSecureRendering];
-[SBAppViewController setPlaceholderContentEnabled:];
-[SBAppViewController _transformHostedAppViewForRotationToOrientation:];
-[SBAppViewController handlesRotationIndependentOfCoverSheet];
-[SBAppViewController _activateApp];
-[SBAppViewController setSupplementalActivationSettings:];
-[SBAppViewController layoutStateForApplicationTransitionContext:];
-[SBAppViewController appView];
-[SBAppViewController _createSceneViewController];
-[SBAppViewController viewDidLayoutSubviews];
-[SBAppViewController hostedAppWillRotateToInterfaceOrientation:];
-[SBAppViewController applicationSceneViewController:statusBarTapped:tapActionType:];
-[SBAppViewController beginApplicationSceneUpdateTransaction];
-[SBAppViewController _windowSceneFromSceneHandle];
-[SBAppViewController applicationSceneStatusBarDelegate];
-[SBAppViewController applicationSceneViewController:didChangePreferredStatusBarAxis:withAnimationParameters:];
-[SBAppViewController setContentReferenceSize:withContentOrientation:andContainerOrientation:];
-[SBAppViewController viewWillAppear:];
-[SBAppViewController conformsToSBApplicationHosting];
-[SBAppViewController invalidate];
-[SBAppViewController applicationSceneViewController:statusBarDoubleTapped:];
-[SBAppViewController _canShowWhileLocked];
-[SBAppViewController setIgnoresOcclusions:];
-[SBAppViewController setDelegate:];
-[SBAppViewController setActionsToDeliver:];
-[SBAppViewController previousLayoutStateForApplicationTransitionContext:];
-[SBAppViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[SBAppViewController viewDidAppear:];
-[SBAppViewController _deactivateHostedApp];
-[SBAppViewController hostedAppSceneHandle];
-[SBAppViewController canHostAnApp];
-[SBAppViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBAppViewController _destroySceneViewController];
-[SBAppViewController _updateForAppearanceState:];
-[SBAppViewController sceneUpdateTransaction:finishedApplyingUpdate:];
-[SBAppViewController setAutomatesLifecycle:];
-[SBAppViewController _configureApplicationSceneEntity:deliveringActions:];
-[SBAppViewController applicationSceneViewControllerDidUpdateHomeAffordanceSupportedOrientations:];
-[SBAppViewController hostedAppSceneHandles];
-[SBAppViewController delegate];
-[SBAppViewController windowControlsLayoutForApplicationSceneViewController:];
-[SBAppViewController endInteractiveDisplayModeTransitionAtMode:];
-[SBAppViewController automatesLifecycle];
-[SBAppViewController viewDidDisappear:];
-[SBAppViewController overrideStatusBarStyle];
-[SBAppViewController _setCurrentMode:];
-[SBAppViewController _installedAppsDidChange:];
-[SBAppViewController containerDidUpdateTraitsParticipant:];
-[SBAppViewController applicationSceneViewController:didUpdateStatusBarHidden:withAnimation:];
-[SBAppViewController setDisplayMode:animationFactory:completion:];
-[SBAppViewController _createSceneUpdateTransactionForApplicationSceneEntity:deliveringActions:];
-[SBAppViewController contentReferenceSize];
-[SBAppViewController isHostingAnApp];
-[SBAppViewController placeholderContentEnabled];
-[SBAppViewController placeholderContentContext];
-[SBAppViewController applicationSceneViewControllerIsInNonrotatingWindow:];
-[SBAppViewController updateInteractiveDisplayModeTransitionProgress:];
```
