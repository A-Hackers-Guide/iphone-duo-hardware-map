# `SBPasscodeEntryTransientOverlayViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransientOverlayViewController`
- Protocols: `CSBiometricSuppressionObserver`, `PTSettingsKeyObserver`, `SBFAuthenticationResponder`, `SBUIPasscodeLockViewDelegate`
- 16 instance variables, 12 properties, 56 instance methods, 0 class methods

## Instance variables

```
B _attemptingUnlock;
@"SBFUserAuthenticationController" _authenticationController;
@"<SBUIPasscodeLockView>" _passcodeRequester;
@"SBUIPasscodeViewWithLockScreenStyle" _passcodeView;
@"CSLockScreenPearlSettings" _pearlSettings;
@"CSPoseidonViewController" _poseidonViewController;
B _keyboardVisible;
@"<BSInvalidatable>" _poseidonBiometricInaccessibleAssertion;
B _dismissesSiriForPresentation;
B _showEmergencyCallButton;
B _useBiometricPresentation;
i _intent;
@"<SBPasscodeEntryTransientOverlayViewControllerDelegate>" _delegate;
@"NSString" _unlockDestination;
q _overridePresentationOrientation;
@"<CSBiometricSuppressionProviding>" _biometricSuppressionProvider;
```

## Properties

```
@property (T@"<SBPasscodeEntryTransientOverlayViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_showEmergencyCallButton) showEmergencyCallButton;
@property (TB,N,V_useBiometricPresentation) useBiometricPresentation;
@property (T@"NSString",C,N,V_unlockDestination) unlockDestination;
@property (Ti,N,V_intent) intent;
@property (Tq,N,V_overridePresentationOrientation) overridePresentationOrientation;
@property (TB,N,V_dismissesSiriForPresentation) dismissesSiriForPresentation;
@property (T@"<CSBiometricSuppressionProviding>",&,N,V_biometricSuppressionProvider) biometricSuppressionProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBPasscodeEntryTransientOverlayViewController biometricSuppressionProvider];
-[SBPasscodeEntryTransientOverlayViewController preferredInterfaceOrientationForPresentation];
-[SBPasscodeEntryTransientOverlayViewController newTransientOverlayPresentationTransitionCoordinator];
-[SBPasscodeEntryTransientOverlayViewController setIntent:];
-[SBPasscodeEntryTransientOverlayViewController preferredDisplayLayoutElementIdentifier];
-[SBPasscodeEntryTransientOverlayViewController initWithAuthenticationController:];
-[SBPasscodeEntryTransientOverlayViewController supportedInterfaceOrientations];
-[SBPasscodeEntryTransientOverlayViewController intent];
-[SBPasscodeEntryTransientOverlayViewController unlockDestination];
-[SBPasscodeEntryTransientOverlayViewController idleTimerDuration];
-[SBPasscodeEntryTransientOverlayViewController newTransientOverlayDismissalTransitionCoordinator];
-[SBPasscodeEntryTransientOverlayViewController biometricSuppressionProvider:didUpdateSuppressedBiometricModalities:];
-[SBPasscodeEntryTransientOverlayViewController viewDidLoad];
-[SBPasscodeEntryTransientOverlayViewController viewDidLayoutSubviews];
-[SBPasscodeEntryTransientOverlayViewController shouldAutorotate];
-[SBPasscodeEntryTransientOverlayViewController _preferredStatusBarVisibility];
-[SBPasscodeEntryTransientOverlayViewController settings:changedValueForKey:];
-[SBPasscodeEntryTransientOverlayViewController viewWillAppear:];
-[SBPasscodeEntryTransientOverlayViewController _canShowWhileLocked];
-[SBPasscodeEntryTransientOverlayViewController setDelegate:];
-[SBPasscodeEntryTransientOverlayViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[SBPasscodeEntryTransientOverlayViewController isContentOpaque];
-[SBPasscodeEntryTransientOverlayViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBPasscodeEntryTransientOverlayViewController delegate];
-[SBPasscodeEntryTransientOverlayViewController viewDidDisappear:];
-[SBPasscodeEntryTransientOverlayViewController setUnlockDestination:];
-[SBPasscodeEntryTransientOverlayViewController idleTimerMode];
-[SBPasscodeEntryTransientOverlayViewController preferredStatusBarStyle];
-[SBPasscodeEntryTransientOverlayViewController prefersEmbeddedDisplayPresentation];
-[SBPasscodeEntryTransientOverlayViewController idleWarnMode];
-[SBPasscodeEntryTransientOverlayViewController passcodeLockViewCancelButtonPressed:];
-[SBPasscodeEntryTransientOverlayViewController passcodeLockViewEmergencyCallButtonPressed:];
-[SBPasscodeEntryTransientOverlayViewController passcodeLockViewPasscodeDidChange:];
-[SBPasscodeEntryTransientOverlayViewController passcodeLockViewPasscodeEntered:];
-[SBPasscodeEntryTransientOverlayViewController passcodeLockViewPasscodeEnteredViaMesa:];
-[SBPasscodeEntryTransientOverlayViewController handleFailedAuthenticationRequest:error:];
-[SBPasscodeEntryTransientOverlayViewController handleInvalidAuthenticationRequest:];
-[SBPasscodeEntryTransientOverlayViewController handleSuccessfulAuthenticationRequest:];
-[SBPasscodeEntryTransientOverlayViewController _passcodeLockViewPasscodeEntered:authenticationType:];
-[SBPasscodeEntryTransientOverlayViewController setUseBiometricPresentation:];
-[SBPasscodeEntryTransientOverlayViewController useBiometricPresentation];
-[SBPasscodeEntryTransientOverlayViewController _applyBiometricSuppressionState];
-[SBPasscodeEntryTransientOverlayViewController overridePresentationOrientation];
-[SBPasscodeEntryTransientOverlayViewController _attemptUnlock:passcode:];
-[SBPasscodeEntryTransientOverlayViewController _deviceSupportsAutorotation];
-[SBPasscodeEntryTransientOverlayViewController _isBiometricAuthenticationAvailable];
-[SBPasscodeEntryTransientOverlayViewController _updatePrototypeSettings];
-[SBPasscodeEntryTransientOverlayViewController _updateStatusAndSubtitle];
-[SBPasscodeEntryTransientOverlayViewController canBecomeLocalFirstResponder];
-[SBPasscodeEntryTransientOverlayViewController dismissesSiriForPresentation];
-[SBPasscodeEntryTransientOverlayViewController handleWillShowKeyboard:];
-[SBPasscodeEntryTransientOverlayViewController setBiometricSuppressionProvider:];
-[SBPasscodeEntryTransientOverlayViewController setDismissesSiriForPresentation:];
-[SBPasscodeEntryTransientOverlayViewController setOverridePresentationOrientation:];
-[SBPasscodeEntryTransientOverlayViewController setShowEmergencyCallButton:];
-[SBPasscodeEntryTransientOverlayViewController showEmergencyCallButton];
```
