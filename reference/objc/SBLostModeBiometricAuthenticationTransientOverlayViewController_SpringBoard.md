# `SBLostModeBiometricAuthenticationTransientOverlayViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransientOverlayViewController`
- Protocols: `CSExternalLockProviding`
- 13 instance variables, 10 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"SBLockScreenManager" _lockScreenManager;
@"SBUIBiometricResource" _biometricResource;
@"CSPasscodeBackgroundView" _backgroundView;
@"UILabel" _titleLabel;
@"UILabel" _subtitleLabel;
@"UILayoutGuide" _layoutGuide;
@"UIStackView" _labelsStackView;
@"UIButton" _biometricAuthButton;
@"UIButton" _cancelButton;
@"UIButton" _emergencyButton;
@"LAContext" _authContext;
B _didAuthenticate;
@"<SBLostModeBiometricAuthenticationTransientOverlayViewControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBLostModeBiometricAuthenticationTransientOverlayViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisLocked) locked;
@property (TB,R,N) showPasscode;
@property (TB,R,N) presentsAlert;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) coverSheetIdentifier;
@property (Tq,R,N) participantState;
```

## Instance methods

```
-[SBLostModeBiometricAuthenticationTransientOverlayViewController unlockFromSource:];
-[SBLostModeBiometricAuthenticationTransientOverlayViewController isLocked];
-[SBLostModeBiometricAuthenticationTransientOverlayViewController viewWillDisappear:];
-[SBLostModeBiometricAuthenticationTransientOverlayViewController dealloc];
-[SBLostModeBiometricAuthenticationTransientOverlayViewController viewDidLoad];
-[SBLostModeBiometricAuthenticationTransientOverlayViewController setDelegate:];
-[SBLostModeBiometricAuthenticationTransientOverlayViewController _hasTelephonyCapability];
-[SBLostModeBiometricAuthenticationTransientOverlayViewController delegate];
-[SBLostModeBiometricAuthenticationTransientOverlayViewController presentsAlert];
-[SBLostModeBiometricAuthenticationTransientOverlayViewController coverSheetIdentifier];
-[SBLostModeBiometricAuthenticationTransientOverlayViewController allowsStackingOverlayContentAbove];
-[SBLostModeBiometricAuthenticationTransientOverlayViewController showPasscode];
-[SBLostModeBiometricAuthenticationTransientOverlayViewController participantState];
-[SBLostModeBiometricAuthenticationTransientOverlayViewController _buttonsBottomSpacing];
-[SBLostModeBiometricAuthenticationTransientOverlayViewController _handleCancelButtonAction];
-[SBLostModeBiometricAuthenticationTransientOverlayViewController _handleEmergencyButtonAction];
-[SBLostModeBiometricAuthenticationTransientOverlayViewController _biometricAuthenticationButtonAction];
-[SBLostModeBiometricAuthenticationTransientOverlayViewController _biometricCapabilityText];
-[SBLostModeBiometricAuthenticationTransientOverlayViewController _runLocalAuthenticationEvaluation];
-[SBLostModeBiometricAuthenticationTransientOverlayViewController initWithLockScreenManager:biometricResource:];
```
