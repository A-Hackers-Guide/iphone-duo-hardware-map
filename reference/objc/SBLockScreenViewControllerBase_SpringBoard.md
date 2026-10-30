# `SBLockScreenViewControllerBase`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBApplicationHosting`, `SBAutoUnlockRule`, `SBBiometricUnlockBehavior`, `SBButtonEventsHandler`, `SBCoverSheetSlidingViewControllerContentViewController`, `SBLockScreenBacklightControlling`, `SBLockScreenBehaviorSuppressing`, `SBLockScreenBlockedStateObserving`, `SBLockScreenButtonObserving`, `SBLockScreenCallHandling`, `SBLockScreenContentStateProviding`, `SBLockScreenCustomActionStoring`, `SBLockScreenIdleTimerControlling`, `SBLockScreenLockingAndUnlocking`, `SBLockScreenMediaControlsPresenting`, `SBLockScreenPasscodeViewPresenting`, `SBLockScreenPluginPresenting`, `SBLockScreenProximityBehaviorProviding`, `SBLockScreenStatusBarTransitioning`, `SBLockScreenSpotlightPresenting`
- 9 instance variables, 17 properties, 87 instance methods, 0 class methods

## Instance variables

```
@"SBFLockScreenActionContext" _customLockScreenActionContext;
B _authenticated;
B _expectsFaceContact;
@"SBBacklightController" _backlightController;
d _backlightLevel;
@"<SBBiometricUnlockBehaviorDelegate>" _biometricUnlockBehaviorDelegate;
@"SBWallpaperController" _wallpaperController;
@"UIVisualEffectView" _wakeEffectView;
@"SBFLegacyWallpaperWakeAnimator" _legacyWallpaperWakeAnimator;
```

## Properties

```
@property (T@"UIVisualEffectView",W,N,V_wakeEffectView) wakeEffectView;
@property (T@"SBFLegacyWallpaperWakeAnimator",R,N,V_legacyWallpaperWakeAnimator) legacyWallpaperWakeAnimator;
@property (T@"SBWallpaperController",R,N,V_wallpaperController) wallpaperController;
@property (T@"SBBacklightController",R,N,V_backlightController) backlightController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBBiometricUnlockBehaviorDelegate>",W,N,V_biometricUnlockBehaviorDelegate) biometricUnlockBehaviorDelegate;
@property (TB,R,N) contentOccludesBackground;
@property (Tq,R,N) backlightLuminance;
@property (Td,N,V_backlightLevel) backlightLevel;
@property (T@"SBFLockScreenActionContext",&,N,G_customLockScreenActionContext) customLockScreenActionContext;
@property (TB,N,GisAuthenticated,V_authenticated) authenticated;
@property (TB,N,GisShowingMediaControls) showingMediaControls;
@property (TB,R,N,V_expectsFaceContact) expectsFaceContact;
@property (TB,R,N) shouldShowLockStatusBarTime;
```

## Instance methods

```
-[SBLockScreenViewControllerBase isAuthenticated];
-[SBLockScreenViewControllerBase jiggleLockIcon];
-[SBLockScreenViewControllerBase setAuthenticated:];
-[SBLockScreenViewControllerBase isShowingMediaControls];
-[SBLockScreenViewControllerBase createHomeButtonSuppressAfterUnlockRecognizerForUnlockSource:];
-[SBLockScreenViewControllerBase backlightController];
-[SBLockScreenViewControllerBase wallpaperController];
-[SBLockScreenViewControllerBase setBacklightLevel:];
-[SBLockScreenViewControllerBase handleVolumeDownButtonPress];
-[SBLockScreenViewControllerBase prepareForUIUnlock];
-[SBLockScreenViewControllerBase setWakeEffectView:];
-[SBLockScreenViewControllerBase backlightLevel];
-[SBLockScreenViewControllerBase handleHomeButtonLongPress];
-[SBLockScreenViewControllerBase succinctDescriptionBuilder];
-[SBLockScreenViewControllerBase suppressesScreenshots];
-[SBLockScreenViewControllerBase suppressesBanners];
-[SBLockScreenViewControllerBase noteResetRestoreStateUpdated];
-[SBLockScreenViewControllerBase handleVoiceCommandButtonPress];
-[SBLockScreenViewControllerBase shouldUnlockUIOnKeyDownEvent];
-[SBLockScreenViewControllerBase setInScreenOffMode:forAutoUnlock:fromUnlockSource:];
-[SBLockScreenViewControllerBase noteLockButtonUp];
-[SBLockScreenViewControllerBase handleHeadsetButtonPress:];
-[SBLockScreenViewControllerBase viewDidLoad];
-[SBLockScreenViewControllerBase handlesRotationIndependentOfCoverSheet];
-[SBLockScreenViewControllerBase setInScreenOffMode:];
-[SBLockScreenViewControllerBase handleLockButtonPress];
-[SBLockScreenViewControllerBase isPasscodeLockVisible];
-[SBLockScreenViewControllerBase hostedAppWillRotateToInterfaceOrientation:];
-[SBLockScreenViewControllerBase descriptionWithMultilinePrefix:];
-[SBLockScreenViewControllerBase noteDeviceBlockedStatusUpdated];
-[SBLockScreenViewControllerBase handleVolumeUpButtonPress];
-[SBLockScreenViewControllerBase updateStatusBarForLockScreenComeback];
-[SBLockScreenViewControllerBase willUIUnlockFromSource:isLockScreenDisabledForAssertion:];
-[SBLockScreenViewControllerBase isProcessingUnlockAttempt];
-[SBLockScreenViewControllerBase isInScreenOffMode];
-[SBLockScreenViewControllerBase createHomeButtonShowPasscodeRecognizerForHomeButtonPress];
-[SBLockScreenViewControllerBase succinctDescription];
-[SBLockScreenViewControllerBase shouldPresentOrDismissCoverSheetSpotlight];
-[SBLockScreenViewControllerBase isMainPageVisible];
-[SBLockScreenViewControllerBase handleHomeButtonDoublePress];
-[SBLockScreenViewControllerBase conformsToSBApplicationHosting];
-[SBLockScreenViewControllerBase screenSleepCompletedForSource:];
-[SBLockScreenViewControllerBase setInScreenOffMode:preservingCoverSheetPresentationState:];
-[SBLockScreenViewControllerBase hostedAppSceneHandle];
-[SBLockScreenViewControllerBase wakeEffectView];
-[SBLockScreenViewControllerBase isUnlockDisabled];
-[SBLockScreenViewControllerBase canHostAnApp];
-[SBLockScreenViewControllerBase finishUIUnlockFromSource:];
-[SBLockScreenViewControllerBase presentOrDismissCoverSheetSpotlightAnimated:];
-[SBLockScreenViewControllerBase canBeDeactivatedForUIUnlockFromSource:];
-[SBLockScreenViewControllerBase viewWillTransitionToSize:withTransitionCoordinator:];
-[SBLockScreenViewControllerBase disableLockScreenPluginWithContext:];
-[SBLockScreenViewControllerBase shouldDisableALS];
-[SBLockScreenViewControllerBase updateStatusBarForLockScreenTeardown];
-[SBLockScreenViewControllerBase enableLockScreenPluginWithContext:];
-[SBLockScreenViewControllerBase _customLockScreenActionContext];
-[SBLockScreenViewControllerBase shouldAutoUnlockForSource:];
-[SBLockScreenViewControllerBase hostedAppSceneHandles];
-[SBLockScreenViewControllerBase biometricUnlockBehaviorDelegate];
-[SBLockScreenViewControllerBase handleBiometricEvent:];
-[SBLockScreenViewControllerBase noteMenuButtonUp];
-[SBLockScreenViewControllerBase prepareForUILock];
-[SBLockScreenViewControllerBase setPasscodeLockVisible:intent:ignoringPreflightRequirementsForPresentation:animated:completion:];
-[SBLockScreenViewControllerBase updateScaleViewWithScale:withDuration:];
-[SBLockScreenViewControllerBase setCustomLockScreenActionContext:];
-[SBLockScreenViewControllerBase suppressesControlCenter];
-[SBLockScreenViewControllerBase startLockScreenFadeInAnimationForSource:];
-[SBLockScreenViewControllerBase setBiometricUnlockBehaviorDelegate:];
-[SBLockScreenViewControllerBase noteMenuButtonDown];
-[SBLockScreenViewControllerBase backlightLuminance];
-[SBLockScreenViewControllerBase setPasscodeLockVisible:animated:completion:];
-[SBLockScreenViewControllerBase isHostingAnApp];
-[SBLockScreenViewControllerBase expectsFaceContact];
-[SBLockScreenViewControllerBase setShowingMediaControls:];
-[SBLockScreenViewControllerBase setPasscodeLockVisible:animated:];
-[SBLockScreenViewControllerBase handleHomeButtonPress];
-[SBLockScreenViewControllerBase shouldShowLockStatusBarTime];
-[SBLockScreenViewControllerBase descriptionBuilderWithMultilinePrefix:];
-[SBLockScreenViewControllerBase isMakingEmergencyCall];
-[SBLockScreenViewControllerBase contentOccludesBackground];
-[SBLockScreenViewControllerBase launchEmergencyDialer];
-[SBLockScreenViewControllerBase legacyWallpaperWakeAnimator];
-[SBLockScreenViewControllerBase emergencyDialerExitedWithError:];
-[SBLockScreenViewControllerBase conformsToSBCoverSheetSlidingViewControllerContentViewController];
-[SBLockScreenViewControllerBase exitEmergencyDialerAnimated:];
-[SBLockScreenViewControllerBase initWithWallpaperController:backlightController:];
-[SBLockScreenViewControllerBase launchEmergencyDialerAnimated:];
```
