# `SBDashBoardLockScreenEnvironment`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBApplicationHosting`, `SBAutoUnlockRule`, `SBBiometricUnlockBehavior`, `SBBiometricUnlockBehaviorDelegate`, `SBButtonEventsHandler`, `CSCoverSheetViewControllerObserver`, `SBLockScreenBacklightControlling`, `SBLockScreenBehaviorSuppressing`, `SBLockScreenBlockedStateObserving`, `SBLockScreenButtonObserving`, `SBLockScreenContentStateProviding`, `SBLockScreenCustomActionStoring`, `SBLockScreenLockingAndUnlocking`, `SBLockScreenMediaControlsPresenting`, `SBLockScreenPasscodeViewPresenting`, `SBLockScreenProximityBehaviorProviding`, `SBLockScreenStatusBarTransitioning`, `SBLockScreenSpotlightPresenting`, `SBDashBoardCameraPageViewControllerDelegate`, `SBDashBoardCaptureLaunchPolicyObserver`, `SBLockScreenEnvironment`
- 21 instance variables, 39 properties, 112 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
@"SBApplicationController" _applicationController;
@"CSCoverSheetViewController" _coverSheetViewController;
@"SBDashBoardAnalyticsEmitter" _analyticsEmitter;
@"SBDashBoardApplicationLauncher" _applicationLauncher;
@"SBDashBoardBiometricUnlockController" _biometricUnlockController;
@"<SBDashBoardCaptureLaunchPolicy>" _captureLaunchPolicy;
@"SBDashBoardCameraPageViewController" _cameraPageViewController;
@"SBLockScreenActionManager" _lockScreenActionManager;
@"SBDashBoardEmergencyDialerController" _emergencyDialerController;
@"SBDashBoardIdleTimerController" _idleTimerController;
@"SBDashBoardPluginController" _pluginController;
@"SBDashBoardPolicyBasedBehaviorProvider" _policyBasedBehaviorProvider;
@"SBDashBoardSetupController" _setupController;
@"SBDashBoardWidgetURLHandler" _widgetURLHandler;
@"SBCoverSheetSpotlightPresenter" _coverSheetSpotlightPresenter;
@"SBBacklightSignificantUserInteractionMonitor" _significantUserInteractionMonitor;
@"SBSearchGesture" _searchGesture;
B _expectsFaceContact;
B _isHandlingUnlockAttempt;
@"<SBBiometricUnlockBehaviorDelegate>" _biometricUnlockBehaviorDelegate;
```

## Properties

```
@property (T@"CSCoverSheetViewController",R,N,V_coverSheetViewController) coverSheetViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBBiometricUnlockBehaviorDelegate>",W,N,V_biometricUnlockBehaviorDelegate) biometricUnlockBehaviorDelegate;
@property (Tq,R,N) backlightLuminance;
@property (Td,N) backlightLevel;
@property (T@"SBFLockScreenActionContext",&,N,G_customLockScreenActionContext) customLockScreenActionContext;
@property (TB,N,GisAuthenticated) authenticated;
@property (TB,N,GisShowingMediaControls) showingMediaControls;
@property (TB,R,N,V_expectsFaceContact) expectsFaceContact;
@property (TB,R,N) shouldShowLockStatusBarTime;
@property (T@"UIViewController",R,N) rootViewController;
@property (T@"<SBAutoUnlockRule>",R,N) autoUnlockRule;
@property (T@"<SBBiometricUnlockBehavior>",R,N) biometricUnlockBehavior;
@property (T@"<SBButtonEventsHandler>",R,N) buttonEventsHandler;
@property (T@"<SBApplicationHosting>",R,N) applicationHoster;
@property (T@"<SBFScreenWakeAnimationTarget>",R,N) screenWakeAnimationTarget;
@property (T@"<SBControlCenterPresenting>",R,N) controlCenterPresenter;
@property (T@"<SBLockScreenApplicationLaunching>",R,N) applicationLauncher;
@property (T@"<SBLockScreenBacklightControlling>",R,N) backlightController;
@property (T@"<SBLockScreenBehaviorSuppressing>",R,N) behaviorSuppressor;
@property (T@"<SBLockScreenBlockedStateObserving>",R,N) blockedStateObserver;
@property (T@"<SBLockScreenButtonObserving>",R,N) buttonObserver;
@property (T@"<SBLockScreenCallHandling>",R,N) callController;
@property (T@"<SBLockScreenContentStateProviding>",R,N) contentStateProvider;
@property (T@"<SBLockScreenCustomActionStoring>",R,N) customActionStore;
@property (T@"<SBLockScreenIdleTimerControlling>",R,N) idleTimerController;
@property (T@"<SBLockScreenLockingAndUnlocking>",R,N) lockController;
@property (T@"<SBLockScreenMediaControlsPresenting>",R,N) mediaControlsPresenter;
@property (T@"<SBLockScreenPasscodeViewPresenting>",R,N) passcodeViewPresenter;
@property (T@"<SBLockScreenPluginPresenting>",R,N) pluginPresenter;
@property (T@"<SBLockScreenProximityBehaviorProviding>",R,N) proximityBehaviorProvider;
@property (T@"<SBLockScreenStatusBarTransitioning>",R,N) statusBarTransitionController;
@property (T@"<SBSWidgetMetricsProviding>",R,N) widgetMetricsProvider;
@property (T@"<SBLockScreenSpotlightPresenting>",R,N) spotlightPresenter;
@property (T@"<CSCoverSheetSpotlightPresenting>",R,N,V_coverSheetSpotlightPresenter) coverSheetSpotlightPresenter;
@property (T@"<SBLockScreenSetupControlling>",R,N,V_setupController) setupController;
```

## Instance methods

```
-[SBDashBoardLockScreenEnvironment coverSheetViewController];
-[SBDashBoardLockScreenEnvironment _assistantIslandEnablementDidChange:];
-[SBDashBoardLockScreenEnvironment isAuthenticated];
-[SBDashBoardLockScreenEnvironment jiggleLockIcon];
-[SBDashBoardLockScreenEnvironment setAuthenticated:];
-[SBDashBoardLockScreenEnvironment isShowingMediaControls];
-[SBDashBoardLockScreenEnvironment createHomeButtonSuppressAfterUnlockRecognizerForUnlockSource:];
-[SBDashBoardLockScreenEnvironment customActionStore];
-[SBDashBoardLockScreenEnvironment backlightController];
-[SBDashBoardLockScreenEnvironment rootViewController];
-[SBDashBoardLockScreenEnvironment performDeferredInitialization];
-[SBDashBoardLockScreenEnvironment applicationHoster];
-[SBDashBoardLockScreenEnvironment setupController];
-[SBDashBoardLockScreenEnvironment setBacklightLevel:];
-[SBDashBoardLockScreenEnvironment widgetMetricsProvider];
-[SBDashBoardLockScreenEnvironment handleVolumeDownButtonPress];
-[SBDashBoardLockScreenEnvironment autoUnlockRule];
-[SBDashBoardLockScreenEnvironment coverSheetSpotlightPresenter];
-[SBDashBoardLockScreenEnvironment coverSheetViewController:didChangeActiveBehavior:];
-[SBDashBoardLockScreenEnvironment spotlightPresenter];
-[SBDashBoardLockScreenEnvironment prepareForUIUnlock];
-[SBDashBoardLockScreenEnvironment lockController];
-[SBDashBoardLockScreenEnvironment backlightLevel];
-[SBDashBoardLockScreenEnvironment handleHomeButtonLongPress];
-[SBDashBoardLockScreenEnvironment succinctDescriptionBuilder];
-[SBDashBoardLockScreenEnvironment proximityBehaviorProvider];
-[SBDashBoardLockScreenEnvironment suppressesScreenshots];
-[SBDashBoardLockScreenEnvironment screenWakeAnimationTarget];
-[SBDashBoardLockScreenEnvironment initWithWindowScene:applicationController:lockScreenManager:];
-[SBDashBoardLockScreenEnvironment suppressesBanners];
-[SBDashBoardLockScreenEnvironment noteResetRestoreStateUpdated];
-[SBDashBoardLockScreenEnvironment idleTimerController];
-[SBDashBoardLockScreenEnvironment handleVoiceCommandButtonPress];
-[SBDashBoardLockScreenEnvironment dealloc];
-[SBDashBoardLockScreenEnvironment shouldUnlockUIOnKeyDownEvent];
-[SBDashBoardLockScreenEnvironment setInScreenOffMode:forAutoUnlock:fromUnlockSource:];
-[SBDashBoardLockScreenEnvironment applicationLauncher];
-[SBDashBoardLockScreenEnvironment captureLaunchPolicyDidUpdatePolicy:];
-[SBDashBoardLockScreenEnvironment noteLockButtonUp];
-[SBDashBoardLockScreenEnvironment handleHeadsetButtonPress:];
-[SBDashBoardLockScreenEnvironment handlesRotationIndependentOfCoverSheet];
-[SBDashBoardLockScreenEnvironment setInScreenOffMode:];
-[SBDashBoardLockScreenEnvironment _handleCoverSheetTranslationForPasscodeLockVisible:blockingForOtherReasons:ignoringPreflightRequirementsForPresentation:];
-[SBDashBoardLockScreenEnvironment handleLockButtonPress];
-[SBDashBoardLockScreenEnvironment isPasscodeLockVisible];
-[SBDashBoardLockScreenEnvironment hostedAppWillRotateToInterfaceOrientation:];
-[SBDashBoardLockScreenEnvironment descriptionWithMultilinePrefix:];
-[SBDashBoardLockScreenEnvironment noteDeviceBlockedStatusUpdated];
-[SBDashBoardLockScreenEnvironment handleVolumeUpButtonPress];
-[SBDashBoardLockScreenEnvironment biometricUnlockBehavior:requestsFeedback:];
-[SBDashBoardLockScreenEnvironment updateStatusBarForLockScreenComeback];
-[SBDashBoardLockScreenEnvironment biometricUnlockBehavior];
-[SBDashBoardLockScreenEnvironment pluginPresenter];
-[SBDashBoardLockScreenEnvironment willUIUnlockFromSource:isLockScreenDisabledForAssertion:];
-[SBDashBoardLockScreenEnvironment isProcessingUnlockAttempt];
-[SBDashBoardLockScreenEnvironment _updateActiveCoverSheetSearchAffordance];
-[SBDashBoardLockScreenEnvironment isInScreenOffMode];
-[SBDashBoardLockScreenEnvironment createHomeButtonShowPasscodeRecognizerForHomeButtonPress];
-[SBDashBoardLockScreenEnvironment succinctDescription];
-[SBDashBoardLockScreenEnvironment shouldPresentOrDismissCoverSheetSpotlight];
-[SBDashBoardLockScreenEnvironment isMainPageVisible];
-[SBDashBoardLockScreenEnvironment handleHomeButtonDoublePress];
-[SBDashBoardLockScreenEnvironment conformsToSBApplicationHosting];
-[SBDashBoardLockScreenEnvironment screenSleepCompletedForSource:];
-[SBDashBoardLockScreenEnvironment passcodeViewPresenter];
-[SBDashBoardLockScreenEnvironment setInScreenOffMode:preservingCoverSheetPresentationState:];
-[SBDashBoardLockScreenEnvironment setInScreenOffMode:forAutoUnlock:fromUnlockSource:preservingCoverSheetPresentationState:];
-[SBDashBoardLockScreenEnvironment hostedAppSceneHandle];
-[SBDashBoardLockScreenEnvironment isUnlockDisabled];
-[SBDashBoardLockScreenEnvironment contentStateProvider];
-[SBDashBoardLockScreenEnvironment canHostAnApp];
-[SBDashBoardLockScreenEnvironment mediaControlsPresenter];
-[SBDashBoardLockScreenEnvironment finishUIUnlockFromSource:];
-[SBDashBoardLockScreenEnvironment presentOrDismissCoverSheetSpotlightAnimated:];
-[SBDashBoardLockScreenEnvironment canBeDeactivatedForUIUnlockFromSource:];
-[SBDashBoardLockScreenEnvironment callController];
-[SBDashBoardLockScreenEnvironment fingerPresenceDidChange:];
-[SBDashBoardLockScreenEnvironment controlCenterPresenter];
-[SBDashBoardLockScreenEnvironment blockedStateObserver];
-[SBDashBoardLockScreenEnvironment shouldDisableALS];
-[SBDashBoardLockScreenEnvironment updateStatusBarForLockScreenTeardown];
-[SBDashBoardLockScreenEnvironment _customLockScreenActionContext];
-[SBDashBoardLockScreenEnvironment shouldAutoUnlockForSource:];
-[SBDashBoardLockScreenEnvironment hostedAppSceneHandles];
-[SBDashBoardLockScreenEnvironment biometricUnlockBehaviorDelegate];
-[SBDashBoardLockScreenEnvironment defaultHostableEntityForActivationOfCamera:];
-[SBDashBoardLockScreenEnvironment buttonEventsHandler];
-[SBDashBoardLockScreenEnvironment description];
-[SBDashBoardLockScreenEnvironment handleBiometricEvent:];
-[SBDashBoardLockScreenEnvironment noteMenuButtonUp];
-[SBDashBoardLockScreenEnvironment prepareForUILock];
-[SBDashBoardLockScreenEnvironment setPasscodeLockVisible:intent:ignoringPreflightRequirementsForPresentation:animated:completion:];
-[SBDashBoardLockScreenEnvironment _setExpectsFaceContact:];
-[SBDashBoardLockScreenEnvironment updateScaleViewWithScale:withDuration:];
-[SBDashBoardLockScreenEnvironment buttonObserver];
-[SBDashBoardLockScreenEnvironment setCustomLockScreenActionContext:];
-[SBDashBoardLockScreenEnvironment suppressesControlCenter];
-[SBDashBoardLockScreenEnvironment startLockScreenFadeInAnimationForSource:];
-[SBDashBoardLockScreenEnvironment biometricUnlockBehavior:requestsUnlock:withFeedback:];
-[SBDashBoardLockScreenEnvironment statusBarTransitionController];
-[SBDashBoardLockScreenEnvironment setBiometricUnlockBehaviorDelegate:];
-[SBDashBoardLockScreenEnvironment behaviorSuppressor];
-[SBDashBoardLockScreenEnvironment noteMenuButtonDown];
-[SBDashBoardLockScreenEnvironment backlightLuminance];
-[SBDashBoardLockScreenEnvironment setPasscodeLockVisible:animated:completion:];
-[SBDashBoardLockScreenEnvironment isHostingAnApp];
-[SBDashBoardLockScreenEnvironment expectsFaceContact];
-[SBDashBoardLockScreenEnvironment setShowingMediaControls:];
-[SBDashBoardLockScreenEnvironment setPasscodeLockVisible:animated:];
-[SBDashBoardLockScreenEnvironment handleHomeButtonPress];
-[SBDashBoardLockScreenEnvironment shouldShowLockStatusBarTime];
-[SBDashBoardLockScreenEnvironment descriptionBuilderWithMultilinePrefix:];
```
