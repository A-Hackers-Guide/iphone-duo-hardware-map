# `SBSoftLockoutController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSExternalLockProviding`, `CSCoverSheetViewControllerObserver`
- 4 instance variables, 10 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"SBLockScreenManager" _lockScreenManager;
Q _desiredBiometricLockoutState;
@"<BSInvalidatable>" _passcodeRequiredAssertion;
@"<SBSoftLockoutControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBSoftLockoutControllerDelegate>",W,N,V_delegate) delegate;
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
-[SBSoftLockoutController unlockFromSource:];
-[SBSoftLockoutController isLocked];
-[SBSoftLockoutController init];
-[SBSoftLockoutController dealloc];
-[SBSoftLockoutController reload];
-[SBSoftLockoutController initWithBiometricLockoutState:lockScreenManager:];
-[SBSoftLockoutController setDelegate:];
-[SBSoftLockoutController coverSheetViewControllerDidDismissPasscodeLockView:];
-[SBSoftLockoutController delegate];
-[SBSoftLockoutController presentsAlert];
-[SBSoftLockoutController coverSheetIdentifier];
-[SBSoftLockoutController showPasscode];
-[SBSoftLockoutController _createPasscodeRequiredAssertion];
-[SBSoftLockoutController participantState];
-[SBSoftLockoutController _clearPasscodeRequiredAssertion];
```
