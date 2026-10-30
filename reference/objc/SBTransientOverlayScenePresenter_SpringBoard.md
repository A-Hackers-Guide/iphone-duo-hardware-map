# `SBTransientOverlayScenePresenter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFZStackParticipantDelegate`, `SBHomeGrabberPointerClickDelegate`, `SBIdleTimerCoordinating`, `SBTransientOverlayViewControllerDelegate`, `SBHomeGrabberViewObserver`, `SBTransientOverlayPresenting`, `SBIdleTimerProviding`
- 32 instance variables, 32 properties, 114 instance methods, 0 class methods

## Instance variables

```
@"SBAlertItemsController" _alertItemsController;
@"SBBannerManager" _bannerManager;
@"SBInCallPresentationManager" _inCallPresentationManager;
@"<BSInvalidatable>" _bannerSuppressionAssertion;
@"<BSInvalidatable>" _inCallNonModalSuppressionAssertion;
@"NSMutableArray" _contentStatusBarHiddenAssertions;
@"<CSExternalBehaviorProviding>" _coverSheetExternalBehaviorProvider;
@"<BSInvalidatable>" _deviceOrientationUpdateDeferralAssertion;
@"NSMutableArray" _entities;
@"NSMapTable" _entityToSceneDeactivationAssertion;
@"SBFZStackParticipant" _zStackParticipant;
@"SBPhysicalButtonZStackPolicyAssistant" _zStackPhysicalButtonPolicyAssistant;
@"SBIdleTimerCoordinatorHelper" _idleTimerCoordinatorHelper;
@"UIWindow" _initialPresentationKeyWindow;
@"<BSInvalidatable>" _interactiveScreenshotGestureDisabledAssertion;
@"<BSInvalidatable>" _preventVideoCallPIPFromAppearingBelowControlCenterAssertion;
B _isInitiatingEntityPresentation;
Q _nextEntityPresentationSequence;
B _isPendingAlertItems;
B _isReachabilityTemporarilyDisabled;
B _homeAffordanceUpdatesShouldBeAnimated;
@"SBLockStateAggregator" _lockStateAggregator;
@"SBReachabilityController" _reachabilityController;
@"SBWindowSceneStatusBarSettingsAssertion" _globalStatusBarAssertion;
@"SBInAppStatusBarHiddenAssertion" _appStatusBarAssertion;
@"NSHashTable" _observers;
B _windowSceneDisconnected;
@"SBWindowScene" _windowScene;
@"NSNumber" _preferredWhitePointAdaptivityStyleValue;
q _topmostViewControllerInterfaceOrientation;
@"<SBTransientOverlayScenePresenterDelegate>" _delegate;
@"SBCoverSheetPresentationManager" _coverSheetPresentationManager;
```

## Properties

```
@property (T@"SBCoverSheetPresentationManager",&,N,V_coverSheetPresentationManager) coverSheetPresentationManager;
@property (T@"<SBTransientOverlayScenePresenterDelegate>",W,N,V_delegate) delegate;
@property (T@"SBBannerManager",R,N,V_bannerManager) bannerManager;
@property (T@"SBInCallPresentationManager",R,N,V_inCallPresentationManager) inCallPresentationManager;
@property (T@"<SBIdleTimerCoordinating>",W,N) idleTimerCoordinator;
@property (T@"NSArray",R,N) presentedViewControllerContexts;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (TB,R,N) hasActivePresentation;
@property (TB,R,N) canActivePresentationBecomeLocalFirstResponder;
@property (Tq,R,N) presentedViewControllerCount;
@property (TB,R,N) shouldUseSceneBasedKeyboardFocusForActivePresentation;
@property (TB,R,N) canHandleButtonEvents;
@property (T@"UIStatusBarStyleRequest",R,C,N) currentStatusBarStyleRequest;
@property (TB,R,N) hasVisibleStatusBar;
@property (TB,R,N) prefersStatusBarActivityItemVisible;
@property (T@"NSNumber",R,N,V_preferredWhitePointAdaptivityStyleValue) preferredWhitePointAdaptivityStyleValue;
@property (T@"SBTransientOverlayViewController",R,N) topmostPresentedViewController;
@property (Tq,R,N,V_topmostViewControllerInterfaceOrientation) topmostViewControllerInterfaceOrientation;
@property (Td,R,N) topmostWindowLevel;
@property (T@"NSArray",R,N) presentedViewControllers;
@property (TB,R,N) ownsHomeGesture;
@property (Tq,R,N) preferredGestureDismissalStyle;
@property (T@"SBTransientOverlayViewController",R,N) viewControllerForGestureDismissal;
@property (TB,R,N) shouldDisableControlCenter;
@property (TB,R,N) shouldDisableCoverSheetGesture;
@property (TB,R,N) shouldDisableSiri;
@property (TB,R,N) activePresentationPreventsDragAndDrop;
@property (TB,R,N) hasIdleTimerBehaviors;
```

## Instance methods

```
-[SBTransientOverlayScenePresenter isTopmostPresentedViewController:];
-[SBTransientOverlayScenePresenter isPresentingViewController:];
-[SBTransientOverlayScenePresenter hasActivePresentationFromBundleIdentifier:];
-[SBTransientOverlayScenePresenter topmostPresentedViewController];
-[SBTransientOverlayScenePresenter transientOverlayViewController:requestZStackParticipantPreferencesUpdateWithReason:];
-[SBTransientOverlayScenePresenter hasActivePresentation];
-[SBTransientOverlayScenePresenter coverSheetPresentationManager];
-[SBTransientOverlayScenePresenter _dismissEntity:animated:completion:];
-[SBTransientOverlayScenePresenter shouldUseSceneBasedKeyboardFocusForActivePresentation];
-[SBTransientOverlayScenePresenter canActivePresentationBecomeLocalFirstResponder];
-[SBTransientOverlayScenePresenter shouldDisableCoverSheetGesture];
-[SBTransientOverlayScenePresenter idleTimerProvider:didProposeBehavior:forReason:];
-[SBTransientOverlayScenePresenter performPresentationRequest:];
-[SBTransientOverlayScenePresenter presentedViewControllerCount];
-[SBTransientOverlayScenePresenter hasActiveSpotlightPresentation];
-[SBTransientOverlayScenePresenter handleVolumeDownButtonPress];
-[SBTransientOverlayScenePresenter isTopmostPresentationFromSceneWithIdentityTokenString:];
-[SBTransientOverlayScenePresenter keyboardFocusTargetForTopmostPresentingScene];
-[SBTransientOverlayScenePresenter ownsHomeGesture];
-[SBTransientOverlayScenePresenter hasActivePresentationFromProcess:];
-[SBTransientOverlayScenePresenter bannerManager];
-[SBTransientOverlayScenePresenter prefersStatusBarActivityItemVisible];
-[SBTransientOverlayScenePresenter _isPresentationStatusBarHiddenForVisibility:currentExternalStatusBarSettings:];
-[SBTransientOverlayScenePresenter homeGrabberViewDidReceiveClick:];
-[SBTransientOverlayScenePresenter hasPresentationAboveWindowLevel:];
-[SBTransientOverlayScenePresenter inCallPresentationManager];
-[SBTransientOverlayScenePresenter activePresentationPreventsDragAndDrop];
-[SBTransientOverlayScenePresenter setCoverSheetPresentationManager:];
-[SBTransientOverlayScenePresenter zStackParticipant:updatePreferences:];
-[SBTransientOverlayScenePresenter handleHomeButtonLongPress];
-[SBTransientOverlayScenePresenter newContentStatusBarHiddenAssertionWithReason:];
-[SBTransientOverlayScenePresenter _backgroundWindowLevelForEntity:];
-[SBTransientOverlayScenePresenter removeObserver:];
-[SBTransientOverlayScenePresenter _topmostPresentedEntity];
-[SBTransientOverlayScenePresenter windowSceneDidDisconnect:];
-[SBTransientOverlayScenePresenter transientOverlayViewControllerNeedsProximityDetectionUpdate:];
-[SBTransientOverlayScenePresenter _preferredStatusBarVisibilityForEntity:];
-[SBTransientOverlayScenePresenter _currentExternalStatusBarSettings];
-[SBTransientOverlayScenePresenter handleDoubleHeightStatusBarTap];
-[SBTransientOverlayScenePresenter _updatePreferredWhitePointAdaptivityStyle];
-[SBTransientOverlayScenePresenter presentedViewControllers];
-[SBTransientOverlayScenePresenter handleVoiceCommandButtonPress];
-[SBTransientOverlayScenePresenter dealloc];
-[SBTransientOverlayScenePresenter _restoreInputViewsForEntityIfNeeded:];
-[SBTransientOverlayScenePresenter _getContentScale:translation:fromRect:entity:];
-[SBTransientOverlayScenePresenter hasVisibleStatusBar];
-[SBTransientOverlayScenePresenter _contentCornerRadiiForEntity:];
-[SBTransientOverlayScenePresenter handleHeadsetButtonPress:];
-[SBTransientOverlayScenePresenter setIdleTimerCoordinator:];
-[SBTransientOverlayScenePresenter _applyWallpaperAnimationSuspensionAssertionForEntity:];
-[SBTransientOverlayScenePresenter transientOverlayViewControllerDidUpdateHIDEventDeferringDisabled:];
-[SBTransientOverlayScenePresenter handleLockButtonPress];
-[SBTransientOverlayScenePresenter zStackParticipantDidChange:];
-[SBTransientOverlayScenePresenter defaultPreferredInterfaceOrientationForPresentationForTransientOverlayViewController:];
-[SBTransientOverlayScenePresenter _invalidateAssertionsForEntity:];
-[SBTransientOverlayScenePresenter handleVolumeUpButtonPress];
-[SBTransientOverlayScenePresenter _updateContentStatusBarPresentation];
-[SBTransientOverlayScenePresenter isKeyboardVisibleForSpringBoardForTransientOverlayViewController:];
-[SBTransientOverlayScenePresenter _updateCurrentEntityHomeGrabberAnimated:];
-[SBTransientOverlayScenePresenter shouldDisableSiri];
-[SBTransientOverlayScenePresenter _windowedAccessoryDidAttachOrDetach:];
-[SBTransientOverlayScenePresenter topmostViewControllerInterfaceOrientation];
-[SBTransientOverlayScenePresenter _newKeyboardFocusAssertionForEntity:];
-[SBTransientOverlayScenePresenter transientOverlayViewControllerNeedsContentOpaqueUpdate:];
-[SBTransientOverlayScenePresenter homeGrabberViewDidUpdateHidden:];
-[SBTransientOverlayScenePresenter transientOverlayViewControllerNeedsGestureDismissalStyleUpdate:];
-[SBTransientOverlayScenePresenter transientOverlayViewControllerNeedsSceneDeactivationUpdate:];
-[SBTransientOverlayScenePresenter handleHomeButtonDoublePress];
-[SBTransientOverlayScenePresenter _handleCoverSheetWillPresent:];
-[SBTransientOverlayScenePresenter addObserver:];
-[SBTransientOverlayScenePresenter _preserveInputViewsForEntityIfNeeded:];
-[SBTransientOverlayScenePresenter shouldDisableControlCenter];
-[SBTransientOverlayScenePresenter _applyProximityDetectionModeForEntity:];
-[SBTransientOverlayScenePresenter _baseWindowLevelForViewController:];
-[SBTransientOverlayScenePresenter viewControllerForGestureDismissal];
-[SBTransientOverlayScenePresenter setDelegate:];
-[SBTransientOverlayScenePresenter initWithWindowScene:alertItemsController:lockStateAggregator:zStackResolver:bannerManager:inCallPresentationManager:];
-[SBTransientOverlayScenePresenter _newSceneDeactivationAssertionWithReason:];
-[SBTransientOverlayScenePresenter idleTimerCoordinator];
-[SBTransientOverlayScenePresenter preferredWhitePointAdaptivityStyleValue];
-[SBTransientOverlayScenePresenter performDismissalRequest:outerCompletionHandler:];
-[SBTransientOverlayScenePresenter presentedViewControllerContexts];
-[SBTransientOverlayScenePresenter _updateBackgroundWindowForEntity:];
-[SBTransientOverlayScenePresenter transientOverlayDidUpdateSupportedInterfaceOrientations:];
-[SBTransientOverlayScenePresenter preferredGestureDismissalStyle];
-[SBTransientOverlayScenePresenter currentStatusBarStyleRequest];
-[SBTransientOverlayScenePresenter _updateDeactivationAssertions];
-[SBTransientOverlayScenePresenter canHandleButtonEvents];
-[SBTransientOverlayScenePresenter transientOverlayViewControllerDidEndRotation:];
-[SBTransientOverlayScenePresenter transientOverlayViewControllerWillBeginRotation:toInterfaceOrientation:];
-[SBTransientOverlayScenePresenter topmostWindowLevel];
-[SBTransientOverlayScenePresenter transientOverlayViewControllerNeedsWindowHitTestingUpdate:];
-[SBTransientOverlayScenePresenter delegate];
-[SBTransientOverlayScenePresenter _buttonEventHandlingViewController];
-[SBTransientOverlayScenePresenter _updateStatusBarWithCurrentExternalStatusBarSettings:animated:];
-[SBTransientOverlayScenePresenter transientOverlayViewControllerIsForegroundActive:];
-[SBTransientOverlayScenePresenter hasIdleTimerBehaviors];
-[SBTransientOverlayScenePresenter _updateZStackStateWithAnimationBehavior:reason:];
-[SBTransientOverlayScenePresenter transientOverlayViewControllerNeedsStatusBarAppearanceUpdate:];
-[SBTransientOverlayScenePresenter _updateWindowHitTestingForEntity:];
-[SBTransientOverlayScenePresenter defaultShouldAutorotateForTransientOverlayViewController:];
-[SBTransientOverlayScenePresenter setFluidDismissalState:forViewController:];
-[SBTransientOverlayScenePresenter transientOverlayViewControllerNeedsFeaturePolicyUpdate:];
-[SBTransientOverlayScenePresenter windowScene];
-[SBTransientOverlayScenePresenter transientOverlayViewControllerDidUpdatePresentationPrefersStatusBarHidden:];
-[SBTransientOverlayScenePresenter _windowLevelForEntity:];
-[SBTransientOverlayScenePresenter systemModalAlertVisibilityDidChange];
-[SBTransientOverlayScenePresenter _updateFeaturePolicies];
-[SBTransientOverlayScenePresenter defaultSupportedInterfaceOrientationsForTransientOverlayViewController:];
-[SBTransientOverlayScenePresenter transientOverlayViewControllerNeedsWhitePointAdaptivityStyleUpdate:];
-[SBTransientOverlayScenePresenter handleHomeButtonPress];
-[SBTransientOverlayScenePresenter transientOverlayViewControllerNeedsOrientationUpdatesDisabledUpdate:];
-[SBTransientOverlayScenePresenter coordinatorRequestedIdleTimerBehavior:];
-[SBTransientOverlayScenePresenter _statusBarEntity];
```
