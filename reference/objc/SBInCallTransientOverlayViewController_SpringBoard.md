# `SBInCallTransientOverlayViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransientOverlayViewController`
- Protocols: `SBDeviceApplicationSceneHandleObserver`, `SBDeviceApplicationSceneStatusBarStateObserver`, `SBIdleTimerCoordinating`, `BSInvalidatable`
- 11 instance variables, 8 properties, 69 instance methods, 0 class methods

## Instance variables

```
@"UIView<SBApplicationSceneBackgroundView>" _existingSceneBackgroundView;
@"SBIdleTimerCoordinatorHelper" _idleTimerCoordinatorHelper;
@"SBSUIInCallSceneClientSettingsDiffInspector" _inCallSceneClientSettingsDiffInspector;
@"_SBInCallProxySceneBackgroundView" _proxySceneBackgroundView;
@"SBDeviceApplicationSceneViewController" _sceneViewController;
@"SBInCallSettings" _settings;
B _preferContinuityDisplay;
B _shouldIgnoreHomeIndicatorAutoHiddenClientSettings;
B _shouldAlwaysPreventHomeGestureDismissal;
@"SBDeviceApplicationSceneHandle" _sceneHandle;
@"<SBInCallTransientOverlayViewControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"SBDeviceApplicationSceneHandle",R,N,V_sceneHandle) sceneHandle;
@property (T@"<SBInCallTransientOverlayViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_shouldIgnoreHomeIndicatorAutoHiddenClientSettings) shouldIgnoreHomeIndicatorAutoHiddenClientSettings;
@property (TB,N,V_shouldAlwaysPreventHomeGestureDismissal) shouldAlwaysPreventHomeGestureDismissal;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBInCallTransientOverlayViewController sceneHandle:didUpdateClientSettings:];
-[SBInCallTransientOverlayViewController sceneWithIdentifier:didChangeBackgroundActivitiesToSuppressTo:];
-[SBInCallTransientOverlayViewController preferredUnlockedGestureDismissalStyle];
-[SBInCallTransientOverlayViewController supportsAlwaysOnDisplay];
-[SBInCallTransientOverlayViewController idleTimerProvider:didProposeBehavior:forReason:];
-[SBInCallTransientOverlayViewController sceneWithIdentifier:didChangeStatusBarAlphaTo:];
-[SBInCallTransientOverlayViewController handleVolumeDownButtonPress];
-[SBInCallTransientOverlayViewController sceneWithIdentifier:didChangeStatusBarStyleTo:];
-[SBInCallTransientOverlayViewController handleGestureDismissal];
-[SBInCallTransientOverlayViewController sceneHandle];
-[SBInCallTransientOverlayViewController newTransientOverlayPresentationTransitionCoordinator];
-[SBInCallTransientOverlayViewController shouldDisableBanners];
-[SBInCallTransientOverlayViewController succinctDescriptionBuilder];
-[SBInCallTransientOverlayViewController preferredDisplayLayoutElementIdentifier];
-[SBInCallTransientOverlayViewController setContainerOrientation:];
-[SBInCallTransientOverlayViewController setShouldIgnoreHomeIndicatorAutoHiddenClientSettings:];
-[SBInCallTransientOverlayViewController viewWillDisappear:];
-[SBInCallTransientOverlayViewController associatedSceneIdentifiersToSuppressInSystemAperture];
-[SBInCallTransientOverlayViewController supportedInterfaceOrientations];
-[SBInCallTransientOverlayViewController shouldIgnoreHomeIndicatorAutoHiddenClientSettings];
-[SBInCallTransientOverlayViewController dealloc];
-[SBInCallTransientOverlayViewController newTransientOverlayDismissalTransitionCoordinator];
-[SBInCallTransientOverlayViewController handleHeadsetButtonPress:];
-[SBInCallTransientOverlayViewController noteDidMoveToWindowScene:];
-[SBInCallTransientOverlayViewController viewDidLoad];
-[SBInCallTransientOverlayViewController setIdleTimerCoordinator:];
-[SBInCallTransientOverlayViewController movesAutomaticallyToPrimaryWindowScene];
-[SBInCallTransientOverlayViewController handleLockButtonPress];
-[SBInCallTransientOverlayViewController prefersHomeIndicatorAutoHidden];
-[SBInCallTransientOverlayViewController hostedSceneIdentityTokens];
-[SBInCallTransientOverlayViewController viewDidLayoutSubviews];
-[SBInCallTransientOverlayViewController handleVolumeUpButtonPress];
-[SBInCallTransientOverlayViewController preferredWhitePointAdaptivityStyle];
-[SBInCallTransientOverlayViewController keyboardFocusTarget];
-[SBInCallTransientOverlayViewController shouldUseSceneBasedKeyboardFocus];
-[SBInCallTransientOverlayViewController _preferredStatusBarAxis];
-[SBInCallTransientOverlayViewController isPresentedFromSceneWithIdentityTokenString:];
-[SBInCallTransientOverlayViewController associatedBundleIdentifiersToSuppressInSystemAperture];
-[SBInCallTransientOverlayViewController viewWillAppear:];
-[SBInCallTransientOverlayViewController preferredBackgroundActivitiesToSuppress];
-[SBInCallTransientOverlayViewController invalidate];
-[SBInCallTransientOverlayViewController _canShowWhileLocked];
-[SBInCallTransientOverlayViewController setDelegate:];
-[SBInCallTransientOverlayViewController viewDidAppear:];
-[SBInCallTransientOverlayViewController canResignFirstResponder];
-[SBInCallTransientOverlayViewController isContentOpaque];
-[SBInCallTransientOverlayViewController preferredLockedGestureDismissalStyle];
-[SBInCallTransientOverlayViewController serviceProcessIdentifier];
-[SBInCallTransientOverlayViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBInCallTransientOverlayViewController delegate];
-[SBInCallTransientOverlayViewController hasIdleTimerBehaviors];
-[SBInCallTransientOverlayViewController viewDidDisappear:];
-[SBInCallTransientOverlayViewController _inCallSceneClientSettingsDiffInspector];
-[SBInCallTransientOverlayViewController allowsStackingOverlayContentAbove];
-[SBInCallTransientOverlayViewController preferredStatusBarStyle];
-[SBInCallTransientOverlayViewController prefersStatusBarHidden];
-[SBInCallTransientOverlayViewController sceneWithIdentifier:didChangeStatusBarHiddenTo:withAnimation:];
-[SBInCallTransientOverlayViewController canBecomeFirstResponder];
-[SBInCallTransientOverlayViewController prefersEmbeddedDisplayPresentation];
-[SBInCallTransientOverlayViewController handleHomeButtonPress];
-[SBInCallTransientOverlayViewController coordinatorRequestedIdleTimerBehavior:];
-[SBInCallTransientOverlayViewController _registerForAmbientPresentationTraitChange];
-[SBInCallTransientOverlayViewController initWithSceneHandle:shouldPreferContinuityDisplay:];
-[SBInCallTransientOverlayViewController prefersContinuityDisplayPresentation];
-[SBInCallTransientOverlayViewController preventsSystemApertureSuppressionFromBelow];
-[SBInCallTransientOverlayViewController sceneDeactivationPredicate];
-[SBInCallTransientOverlayViewController sceneWithIdentifier:didChangeStatusBarAxisTo:withAnimationParameters:];
-[SBInCallTransientOverlayViewController setShouldAlwaysPreventHomeGestureDismissal:];
-[SBInCallTransientOverlayViewController shouldAlwaysPreventHomeGestureDismissal];
```
