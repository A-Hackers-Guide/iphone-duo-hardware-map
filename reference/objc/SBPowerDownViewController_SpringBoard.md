# `SBPowerDownViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransientOverlayViewController`
- Protocols: `SBPowerDownViewDelegate`, `SBPasscodeEntryTransientOverlayViewControllerDelegate`
- 10 instance variables, 12 properties, 48 instance methods, 0 class methods

## Instance variables

```
@"SBPowerDownView" _powerDownView;
@"<BSInvalidatable>" _powerDownCaptureButtonSuppressionAssertion;
B _userWantsFindMySuppressed;
@"<SBPowerDownViewControllerDelegate>" _delegate;
@"SPBeaconManager" _beaconManager;
@"SBWindowSceneManager" _windowSceneManager;
@"SBPasscodeEntryTransientOverlayViewController" _passcodeEntryTransientOverlayViewController;
@"NSMutableArray" _externalDisplayDimmingWindows;
@"SBFUserAuthenticationController" _userAuthController;
@"<SBFLockOutStatusProvider>" _lockOutController;
```

## Properties

```
@property (T@"SPBeaconManager",&,N,V_beaconManager) beaconManager;
@property (T@"SBWindowSceneManager",&,N,V_windowSceneManager) windowSceneManager;
@property (T@"SBPasscodeEntryTransientOverlayViewController",&,N,V_passcodeEntryTransientOverlayViewController) passcodeEntryTransientOverlayViewController;
@property (T@"NSMutableArray",&,N,V_externalDisplayDimmingWindows) externalDisplayDimmingWindows;
@property (T@"SBFUserAuthenticationController",&,N,V_userAuthController) userAuthController;
@property (TB,N,V_userWantsFindMySuppressed) userWantsFindMySuppressed;
@property (T@"<SBFLockOutStatusProvider>",&,N,V_lockOutController) lockOutController;
@property (T@"<SBPowerDownViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBPowerDownViewController shouldPendAlertItems];
-[SBPowerDownViewController passcodeEntryTransientOverlayViewController:authenticatePasscode:];
-[SBPowerDownViewController passcodeEntryTransientOverlayViewControllerStatusSubtitleText];
-[SBPowerDownViewController newTransientOverlayPresentationTransitionCoordinator];
-[SBPowerDownViewController shouldDisableBanners];
-[SBPowerDownViewController viewWillDisappear:];
-[SBPowerDownViewController newTransientOverlayDismissalTransitionCoordinator];
-[SBPowerDownViewController viewDidLoad];
-[SBPowerDownViewController setLockOutController:];
-[SBPowerDownViewController handleLockButtonPress];
-[SBPowerDownViewController viewDidLayoutSubviews];
-[SBPowerDownViewController beaconManager];
-[SBPowerDownViewController _preferredStatusBarVisibility];
-[SBPowerDownViewController shouldDisableSiri];
-[SBPowerDownViewController viewWillAppear:];
-[SBPowerDownViewController lockOutController];
-[SBPowerDownViewController shouldDisableControlCenter];
-[SBPowerDownViewController windowSceneManager];
-[SBPowerDownViewController _canShowWhileLocked];
-[SBPowerDownViewController setDelegate:];
-[SBPowerDownViewController passcodeEntryTransientOverlayViewControllerRequestsDismissal:];
-[SBPowerDownViewController delegate];
-[SBPowerDownViewController setWindowSceneManager:];
-[SBPowerDownViewController setBeaconManager:];
-[SBPowerDownViewController passcodeEntryTransientOverlayViewControllerStatusText];
-[SBPowerDownViewController viewDidDisappear:];
-[SBPowerDownViewController idleTimerMode];
-[SBPowerDownViewController allowsStackingOverlayContentAbove];
-[SBPowerDownViewController prefersEmbeddedDisplayPresentation];
-[SBPowerDownViewController powerDownViewAnimateOutCompleted:];
-[SBPowerDownViewController powerDownViewRequestCancel:];
-[SBPowerDownViewController powerDownViewRequestPowerDown:];
-[SBPowerDownViewController powerDownViewWillAnimateIn:];
-[SBPowerDownViewController powerDownViewWillAnimateOut:];
-[SBPowerDownViewController showPowerDownFindMyAlert];
-[SBPowerDownViewController showPowerDownFindMyAlertWithProceed:cancelCompletion:];
-[SBPowerDownViewController _setPasscodeVisible:animated:];
-[SBPowerDownViewController didTapTemporarilyDisableFindMy];
-[SBPowerDownViewController externalDisplayDimmingWindows];
-[SBPowerDownViewController initWithWindowSceneManager:];
-[SBPowerDownViewController passcodeEntryTransientOverlayViewController];
-[SBPowerDownViewController setExternalDisplayDimmingWindows:];
-[SBPowerDownViewController setPasscodeEntryTransientOverlayViewController:];
-[SBPowerDownViewController setUserAuthController:];
-[SBPowerDownViewController setUserWantsFindMySuppressed:];
-[SBPowerDownViewController userAcknowledgedFindMyInfo];
-[SBPowerDownViewController userAuthController];
-[SBPowerDownViewController userWantsFindMySuppressed];
```
