# `SBAssistantController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SASActivationSourceEligibilityDelegate`, `SBFIdleTimerBehaviorProviding`, `PTSettingsKeyObserver`, `SBFAuthenticationResponder`, `SiriPresentationSpringBoardMainScreenViewControllerDelegate`, `SBAssistantSessionDelegate`, `SBWindowLevelAssertionManagerDelegate`, `SBAlertItemsControllerObserver`, `SBBannerManagerTransitionObserver`, `FBSceneObserver`, `SBDisplayContentModeTransitionObserver`, `SBIdleTimerProviding`, `SBWindowLevelAssertionProviding`
- 30 instance variables, 24 properties, 141 instance methods, 6 class methods

## Instance variables

```
@"FBScene" _fbScene;
@"<BSInvalidatable>" _deferringRule;
@"BSEventQueue" _operationQueue;
B _unlockedDevice;
@"SBFAuthenticationAssertion" _disableAssertion;
@"NSHashTable" _observers;
@"SiriPresentationSpringBoardMainScreenViewController" _mainScreenSiriPresentation;
B _systemAssistantExperienceAvailable;
B _systemAssistantExperienceEnabled;
B _systemAssistantExperiencePersistentSiriEnabled;
B _linwoodDismissalEnabled;
@"SASActivationSourceEligibility" _activationSourceEligibility;
B _homeAffordanceDoubleTapGestureEnabled;
@"SBAssistantGestureConfiguration" _gestureConfiguration;
@"NSSet" _audioCategoriesDisablingVolumeHUD;
@"SBSystemAnimationSettings" _settings;
@"<SBIdleTimer>" _idleTimer;
@"SBWindowLevelAssertionManager" _windowLevelAssertionManager;
B _screenShotServicesIsRunning;
B _visible;
B _dismissing;
B _visualIntelligenceControlEnabled;
@"<SBWindowSceneTracking>" _uiSceneTracker;
@"NSArray" _systemApertureFrames;
@"NSMutableSet" _presentedDodgingBanners;
B _visualSearchEnabled;
B _shouldDismissForWorkspaceTransitions;
@"<SBIdleTimerCoordinating>" _idleTimerCoordinator;
@"<SAInvalidatable>" _systemApertureAssertion;
@"SBAssistantSession" _currentSession;
```

## Properties

```
@property (TB,R,N,V_unlockedDevice) unlockedDevice;
@property (T@"<SAInvalidatable>",&,N,V_systemApertureAssertion) systemApertureAssertion;
@property (TB,N,GisSystemAssistantExperienceEnabled,V_systemAssistantExperienceEnabled) systemAssistantExperienceEnabled;
@property (TB,N,GisSystemAssistantExperiencePersistentSiriEnabled,V_systemAssistantExperiencePersistentSiriEnabled) systemAssistantExperiencePersistentSiriEnabled;
@property (TB,N,GisLinwoodDismissalEnabled,V_linwoodDismissalEnabled) linwoodDismissalEnabled;
@property (TB,N,GisHomeAffordanceDoubleTapGestureEnabled,V_homeAffordanceDoubleTapGestureEnabled) homeAffordanceDoubleTapGestureEnabled;
@property (TB,N,V_shouldDismissForWorkspaceTransitions) shouldDismissForWorkspaceTransitions;
@property (TB,R,N,GisEnabled) enabled;
@property (T@"<SBIdleTimerCoordinating>",W,N,G_idleTimerCoordinator,S_setIdleTimerCoordinator:,V_idleTimerCoordinator) idleTimerCoordinator;
@property (T@"SBAssistantSession",&,N,V_currentSession) currentSession;
@property (TB,R,N,GisSystemAssistantExperienceAvailable,V_systemAssistantExperienceAvailable) systemAssistantExperienceAvailable;
@property (TB,R,N,GisVisualSearchEnabled,V_visualSearchEnabled) visualSearchEnabled;
@property (TB,R,N,GisVisible,V_visible) visible;
@property (TB,R,N) contentObscuresEmbeddedDisplayScreen;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,R,N) idleTimerDuration;
@property (Tq,R,N) idleTimerMode;
@property (Tq,R,N) idleWarnMode;
@property (Td,?,R,N) customIdleExpirationTimeout;
@property (Td,?,R,N) customIdleWarningTimeout;
@property (TB,R,N) hasIdleTimerBehaviors;
```

## Class methods

```
+[SBAssistantController sharedInstance];
+[SBAssistantController sharedInstanceIfExists];
+[SBAssistantController _activationSettingsWithPunchoutStyle:];
+[SBAssistantController bootstrapServices];
+[SBAssistantController defaultActivationSettings];
+[SBAssistantController shouldDismissSiriForGestureTranslation:velocity:];
```

## Instance methods

```
-[SBAssistantController rootViewController];
-[SBAssistantController acquireWindowLevelAssertionWithPriority:windowLevel:windowScene:reason:];
-[SBAssistantController bannerManager:presentable:willTransitionToSize:withTransitionCoordinator:];
-[SBAssistantController windowLevelAssertionManager:didUpdateAssertionsForWindowScene:];
-[SBAssistantController alertItemsController:willActivateAlertItem:];
-[SBAssistantController alertItemsController:didActivateAlertItem:];
-[SBAssistantController _updateWindowLevelForScene:];
-[SBAssistantController _idleTimerCoordinator];
-[SBAssistantController isLinwoodDismissalEnabled];
-[SBAssistantController removeObserver:];
-[SBAssistantController init];
-[SBAssistantController isSystemAssistantExperiencePersistentSiriEnabled];
-[SBAssistantController isSystemAssistantExperienceEnabled];
-[SBAssistantController displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBAssistantController setCurrentSession:];
-[SBAssistantController dealloc];
-[SBAssistantController displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBAssistantController idleTimerDuration];
-[SBAssistantController sceneContentStateDidChange:];
-[SBAssistantController isVisible];
-[SBAssistantController window];
-[SBAssistantController settings:changedValueForKey:];
-[SBAssistantController sceneDidInvalidate:];
-[SBAssistantController _idleTimerBehavior];
-[SBAssistantController isEnabled];
-[SBAssistantController addObserver:];
-[SBAssistantController alertItemsController:didDeactivateAlertItem:forReason:];
-[SBAssistantController isHomeAffordanceDoubleTapGestureEnabled];
-[SBAssistantController restrictSystemApertureToDefaultLayoutWithReason:];
-[SBAssistantController shouldDismissForWorkspaceTransitions];
-[SBAssistantController hasIdleTimerBehaviors];
-[SBAssistantController requestPasscodeUnlockWithCompletion:];
-[SBAssistantController currentSession];
-[SBAssistantController isSystemAssistantExperienceAvailable];
-[SBAssistantController idleTimerMode];
-[SBAssistantController _setVisible:];
-[SBAssistantController bannerManager:willDismissPresentable:withTransitionCoordinator:userInfo:];
-[SBAssistantController bannerManager:willPresentPresentable:withTransitionCoordinator:userInfo:];
-[SBAssistantController idleWarnMode];
-[SBAssistantController setShouldDismissForWorkspaceTransitions:];
-[SBAssistantController isVisualSearchEnabled];
-[SBAssistantController _setIdleTimerCoordinator:];
-[SBAssistantController coordinatorRequestedIdleTimerBehavior:];
-[SBAssistantController bannerManager:containerWillTransitionToSize:withTransitionCoordinator:];
-[SBAssistantController handleFailedAuthenticationRequest:error:];
-[SBAssistantController handleInvalidAuthenticationRequest:];
-[SBAssistantController handleSuccessfulAuthenticationRequest:];
-[SBAssistantController activationEligibilityDidChange];
-[SBAssistantController requestTamaleLaunchAnimationLayerProviderWithCompletion:];
-[SBAssistantController siriPresentation:willChangeKeyboardVisibility:];
-[SBAssistantController siriPresentation:didUpdateShouldDismissForSwipesOutsideContent:];
-[SBAssistantController isAmbientActive];
-[SBAssistantController siriPresentation:didUpdateShouldDismissForWorkspaceTransitions:];
-[SBAssistantController invalidateSystemApertureAssertionWithReason:];
-[SBAssistantController screenWakeIdleTimerResetRequested];
-[SBAssistantController screenWakeRequested];
-[SBAssistantController siriPresentation:acquireElevatedEffectsViewControllerAssertionWithReason:handler:];
-[SBAssistantController siriPresentation:didCreateSiriScene:];
-[SBAssistantController siriPresentation:didUpdateAudioCategoriesDisablingVolumeHUD:];
-[SBAssistantController siriPresentation:didUpdateHomeGestureSharing:];
-[SBAssistantController siriPresentation:didUpdateInputType:];
-[SBAssistantController siriPresentation:didUpdatePresentationOptions:];
-[SBAssistantController siriPresentation:didUpdateShouldDismissForTapsOutsideContent:];
-[SBAssistantController siriPresentation:didUpdateShouldPassTouchesThroughToSpringBoard:];
-[SBAssistantController siriPresentation:isEnabledDidChange:];
-[SBAssistantController siriPresentation:requestsDeemphasizedBackdrop:];
-[SBAssistantController siriPresentation:requestsDeviceUnlockWithPassword:];
-[SBAssistantController siriPresentation:requestsDismissalOfEffectsViewControllerWithHandler:];
-[SBAssistantController siriPresentation:requestsDismissalWithOptions:withHandler:];
-[SBAssistantController siriPresentation:requestsPresentationOfEffectsViewController:withHandler:];
-[SBAssistantController siriPresentation:requestsPresentationWithOptions:withHandler:];
-[SBAssistantController siriPresentation:requestsPunchout:withHandler:];
-[SBAssistantController siriPresentation:setHomeAffordanceSuppression:];
-[SBAssistantController siriPresentation:setShowsHomeAffordance:];
-[SBAssistantController siriPresentation:willStartHostingSceneWithIdentifier:bundleIdentifier:];
-[SBAssistantController siriPresentation:willStopHostingSceneWithIdentifier:bundleIdentifier:];
-[SBAssistantController siriRequestDidReactivateForSiriPresentation:];
-[SBAssistantController _dismissAssistantViewIfNecessaryWithAnimation:factory:dismissalOptions:completion:];
-[SBAssistantController _deviceBlocked:];
-[SBAssistantController _uiSceneTracker];
-[SBAssistantController _updateControlWidgetEligibility];
-[SBAssistantController commandeerCaptureDropletPreludeForVisionInvocation:windowScene:];
-[SBAssistantController shouldDismissSiriForRemoteTransientOverlayFromBundleIdentifier:];
-[SBAssistantController _bioAuthenticated:];
-[SBAssistantController _currentSessionCreatingIfNeededWithFailureExplanation:];
-[SBAssistantController _dismissAssistantViewIfNecessaryWithAnimation:factory:dismissalOptions:windowScene:completion:];
-[SBAssistantController _isLocationTCCAlert:];
-[SBAssistantController _noteDeviceLockedOrBlocked];
-[SBAssistantController _notifyAssistantOfDisplayTransition:];
-[SBAssistantController _prototypeSettingsChanged];
-[SBAssistantController _remoteLocked:];
-[SBAssistantController _setUnlockedDevice:];
-[SBAssistantController _siriPreferencesDidChange];
-[SBAssistantController _systemApertureFrameDidChange:];
-[SBAssistantController _systemAssistantExperienceAvailabilityDidChange];
-[SBAssistantController _systemAssistantExperienceAvailabilityNotificationReceived];
-[SBAssistantController _turnScreenOffWithCompletion:];
-[SBAssistantController _uiLocked:];
-[SBAssistantController _updateDeferringRules];
-[SBAssistantController _updateHomeAffordanceDoubleTapGestureEnabled];
-[SBAssistantController _updateLinwoodDismissalEnabled];
-[SBAssistantController _updateSystemAssistantExperienceEnabled];
-[SBAssistantController _updateSystemAssistantExperiencePersistentSiriEnabled];
-[SBAssistantController _updateVisualIntelligenceControlEnabled];
-[SBAssistantController _updateVisualSearchEnabled];
-[SBAssistantController alwaysOnLiveRenderingAssertionRequested];
-[SBAssistantController applicationProcessDidChangeState:];
-[SBAssistantController assistantSession:didChangePresentationInWindowScene:];
-[SBAssistantController assistantSession:requestsDismissalWithDismissalOptions:];
-[SBAssistantController assistantSession:viewDidAppearInWindowScene:];
-[SBAssistantController assistantSession:viewDidDisappearInWindowScene:];
-[SBAssistantController assistantSession:viewWillAppearInWindowScene:];
-[SBAssistantController assistantSession:viewWillDisappearInWindowScene:];
-[SBAssistantController contentObscuresEmbeddedDisplayScreen];
-[SBAssistantController deviceUnlockRequestedWithPassword:];
-[SBAssistantController dismissAssistantViewIfNecessaryForGestureTranslation:velocity:windowScene:];
-[SBAssistantController dismissAssistantViewIfNecessaryInWindowScene:];
-[SBAssistantController dismissAssistantViewIfNecessaryWithAnimation:windowScene:];
-[SBAssistantController dismissAssistantViewIfNecessaryWithAnimation:windowScene:completion:];
-[SBAssistantController dismissAssistantViewInEverySceneIfNecessary];
-[SBAssistantController dismissAssistantViewInEverySceneIfNecessaryForGestureTranslation:velocity:];
-[SBAssistantController dismissAssistantViewInEverySceneIfNecessaryWithAnimation:];
-[SBAssistantController dismissAssistantViewInEverySceneIfNecessaryWithAnimation:completion:];
-[SBAssistantController dismissAssistantViewInEverySceneIfNecessaryWithAnimation:factory:completion:];
-[SBAssistantController isVisibleInWindowScene:];
-[SBAssistantController notifyAssistantOfApplicationTransition];
-[SBAssistantController sessionForWindowScene:];
-[SBAssistantController setHomeAffordanceDoubleTapGestureEnabled:];
-[SBAssistantController setLinwoodDismissalEnabled:];
-[SBAssistantController setSystemApertureAssertion:];
-[SBAssistantController setSystemAssistantExperienceEnabled:];
-[SBAssistantController setSystemAssistantExperiencePersistentSiriEnabled:];
-[SBAssistantController setUISceneTracker:];
-[SBAssistantController setVisualIntelligenceControlEnabled:];
-[SBAssistantController setVisualSearchEnabled:];
-[SBAssistantController shouldBreadcrumbLaunchedApplicationWithBundleIdentifier:];
-[SBAssistantController shouldShowSystemVolumeHUDForCategory:];
-[SBAssistantController statusBarActionGestureRecognizerDidChange:];
-[SBAssistantController systemApertureAssertion];
-[SBAssistantController systemApertureFramesIncludingBanners];
-[SBAssistantController unlockedDevice];
```
