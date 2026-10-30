# `SBLockScreenBiometricAuthenticationCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `SBUIBiometricResourceObserver`, `SBBiometricUnlockBehaviorDelegate`, `SBWalletPrearmRecognizerDelegate`, `PKPassLibraryDelegate`, `SBUIPasscodeBiometricMatchingAssertionFactory`
- 27 instance variables, 19 properties, 73 instance methods, 0 class methods

## Instance variables

```
@"SBUIBiometricResource" _biometricResource;
@"<BSInvalidatable>" _fingerDetectEnabledAssertion;
@"<SBLockScreenBiometricAuthenticationCoordinatorDelegate>" _delegate;
@"<SBBiometricUnlockBehavior>" _autoUnlockBehavior;
@"SBWalletPreArmController" _walletPreArmController;
@"SBWalletPrearmRecognizer" _walletPrearmRecognizer;
B _presentingWalletInterface;
B _didMatchBeforeWalletPrearmRecognizerTimeout;
@"<BSInvalidatable>" _walletPresentationDisableUnlockAssertion;
@"PKPassLibrary" _passLibrary;
@"NFWalletPresentation" _walletPresentation;
Q _state;
B _isAuthenticated;
@"<BSInvalidatable>" _matchingWantedAssertion;
Q _matchingWantedAssertionMode;
@"NSTimer" _matchingAssertionInvalidationTimer;
B _matchedWithResult;
B _bioAuthenticatedWhileMenuButtonDown;
@"_SBPendingMesaUnlockBehaviorUnlockRequest" _pendingUnlockRequest;
@"NSMutableOrderedSet" _activePasscodeMatchAssertions;
@"NSHashTable" _disabledAssertions;
@"NSHashTable" _disabledUnlockAssertions;
@"NSHashTable" _disabledAutoUnlockAssertions;
@"NSHashTable" _strictTouchCoverageAssertions;
@"SBBiometricFailureStrictMatchingSettings" _failureStrictMatchingSettings;
q _consecutiveMatchFailures;
@"<BSInvalidatable>" _repeatedFailureStrictCoverageAssertion;
```

## Properties

```
@property (T@"SBWalletPrearmRecognizer",R,N,G_walletPrearmRecognizer,V_walletPrearmRecognizer) walletPrearmRecognizer;
@property (TQ,R,N,G_state,V_state) state;
@property (Tq,R,N,G_consecutiveMatchFailures,V_consecutiveMatchFailures) consecutiveMatchFailures;
@property (T@"SBBiometricFailureStrictMatchingSettings",&,N,G_failureStrictMatchingSettings,S_setFailureStrictMatchingSettings:,V_failureStrictMatchingSettings) failureStrictMatchingSettings;
@property (T@"PKPassLibrary",&,N,G_getPassLibrary,S_setPassLibrary:,V_passLibrary) passLibrary;
@property (T@"NFWalletPresentation",&,N,G_getWalletPresentation,S_setWalletPresentation:,V_walletPresentation) walletPresentation;
@property (T@"<SBBiometricUnlockBehavior>",&,N,G_setAutoUnlockBehavior,S_setAutoUnlockBehavior:,V_autoUnlockBehavior) autoUnlockBehavior;
@property (T@"<SBLockScreenBiometricAuthenticationCoordinatorDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_bioAuthenticatedWhileMenuButtonDown) bioAuthenticatedWhileMenuButtonDown;
@property (TB,N,GisAuthenticated,V_isAuthenticated) authenticated;
@property (TB,R,N,GisEnabled) enabled;
@property (TB,R,N,GisWalletPreArmDisabled) walletPreArmDisabled;
@property (TB,R,N,GisUnlockingDisabled) isUnlockingDisabled;
@property (TB,R,N,GisAutoUnlockingDisabled) autoUnlockingDisabled;
@property (TB,R,N,GisStrictTouchCoverageRequired) strictTouchCoverageRequired;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLockScreenBiometricAuthenticationCoordinator isAuthenticated];
-[SBLockScreenBiometricAuthenticationCoordinator _state];
-[SBLockScreenBiometricAuthenticationCoordinator setAuthenticated:];
-[SBLockScreenBiometricAuthenticationCoordinator succinctDescriptionBuilder];
-[SBLockScreenBiometricAuthenticationCoordinator descriptionWithMultilinePrefix:];
-[SBLockScreenBiometricAuthenticationCoordinator biometricUnlockBehavior:requestsFeedback:];
-[SBLockScreenBiometricAuthenticationCoordinator contactlessInterfaceDidDismissFromSource:];
-[SBLockScreenBiometricAuthenticationCoordinator isEnabled];
-[SBLockScreenBiometricAuthenticationCoordinator succinctDescription];
-[SBLockScreenBiometricAuthenticationCoordinator setDelegate:];
-[SBLockScreenBiometricAuthenticationCoordinator acquireMatchingAssertionWithMode:reason:];
-[SBLockScreenBiometricAuthenticationCoordinator isStrictTouchCoverageRequired];
-[SBLockScreenBiometricAuthenticationCoordinator acquireStrictTouchCoverageAssertionForReason:];
-[SBLockScreenBiometricAuthenticationCoordinator delegate];
-[SBLockScreenBiometricAuthenticationCoordinator description];
-[SBLockScreenBiometricAuthenticationCoordinator biometricUnlockBehavior:requestsUnlock:withFeedback:];
-[SBLockScreenBiometricAuthenticationCoordinator descriptionBuilderWithMultilinePrefix:];
-[SBLockScreenBiometricAuthenticationCoordinator passLibraryReceivedInterruption];
-[SBLockScreenBiometricAuthenticationCoordinator biometricResource:observeEvent:];
-[SBLockScreenBiometricAuthenticationCoordinator biometricResource:fingerPresenceDidChange:];
-[SBLockScreenBiometricAuthenticationCoordinator biometricResource:matchingAllowedDidChange:];
-[SBLockScreenBiometricAuthenticationCoordinator _getPassLibrary];
-[SBLockScreenBiometricAuthenticationCoordinator _walletPreArmDisabledDidChange:];
-[SBLockScreenBiometricAuthenticationCoordinator _addPasscodeMatchingAssertion:];
-[SBLockScreenBiometricAuthenticationCoordinator _clearFingerDetectAssertion];
-[SBLockScreenBiometricAuthenticationCoordinator _clearPendingUnlockRequest];
-[SBLockScreenBiometricAuthenticationCoordinator _consecutiveMatchFailures];
-[SBLockScreenBiometricAuthenticationCoordinator _createFingerDetectAssertion];
-[SBLockScreenBiometricAuthenticationCoordinator _evaluateRepeatedFailureStrictCoverage];
-[SBLockScreenBiometricAuthenticationCoordinator _failureStrictMatchingSettings];
-[SBLockScreenBiometricAuthenticationCoordinator _getWalletPresentation];
-[SBLockScreenBiometricAuthenticationCoordinator _handleIdentityMatchSuccess:];
-[SBLockScreenBiometricAuthenticationCoordinator _handlePassKitDismissalIfNecessaryWithReason:];
-[SBLockScreenBiometricAuthenticationCoordinator _hasActivePasscodeViews];
-[SBLockScreenBiometricAuthenticationCoordinator _invalidateWalletPreArmRecognizer];
-[SBLockScreenBiometricAuthenticationCoordinator _isMatchingEffectivelyDisabled];
-[SBLockScreenBiometricAuthenticationCoordinator _isWalletPreArmAllowed];
-[SBLockScreenBiometricAuthenticationCoordinator _noteLockButtonDoublePress];
-[SBLockScreenBiometricAuthenticationCoordinator _noteLockButtonSinglePress];
-[SBLockScreenBiometricAuthenticationCoordinator _noteMatchAttemptDidSucceed:];
-[SBLockScreenBiometricAuthenticationCoordinator _noteMenuButtonDoublePress];
-[SBLockScreenBiometricAuthenticationCoordinator _noteMenuButtonSinglePress];
-[SBLockScreenBiometricAuthenticationCoordinator _noteScreenIsOn:];
-[SBLockScreenBiometricAuthenticationCoordinator _pendUnlockRequest:];
-[SBLockScreenBiometricAuthenticationCoordinator _releaseWalletPresentationDisableUnlockAssertion];
-[SBLockScreenBiometricAuthenticationCoordinator _removePasscodeMatchingAssertion:];
-[SBLockScreenBiometricAuthenticationCoordinator _resetConsecutiveMatchFailuresForReason:];
-[SBLockScreenBiometricAuthenticationCoordinator _resetStateForReason:];
-[SBLockScreenBiometricAuthenticationCoordinator _setAutoUnlockBehavior];
-[SBLockScreenBiometricAuthenticationCoordinator _setAutoUnlockBehavior:];
-[SBLockScreenBiometricAuthenticationCoordinator _setFailureStrictMatchingSettings:];
-[SBLockScreenBiometricAuthenticationCoordinator _setPassLibrary:];
-[SBLockScreenBiometricAuthenticationCoordinator _setState:forReason:];
-[SBLockScreenBiometricAuthenticationCoordinator _setWalletPresentation:];
-[SBLockScreenBiometricAuthenticationCoordinator _setupPreArmRecognizerIfPossibleForReason:];
-[SBLockScreenBiometricAuthenticationCoordinator _stateChangedFrom:to:];
-[SBLockScreenBiometricAuthenticationCoordinator _stateWantsMatching:outMatchMode:];
-[SBLockScreenBiometricAuthenticationCoordinator _toggleAutoUnlockBehaviorEnabled:];
-[SBLockScreenBiometricAuthenticationCoordinator _updateMatchingForState:forReason:];
-[SBLockScreenBiometricAuthenticationCoordinator _updateStrictCoverageOnBiometricInterface];
-[SBLockScreenBiometricAuthenticationCoordinator _walletPrearmRecognizer];
-[SBLockScreenBiometricAuthenticationCoordinator acquireDisableAutoUnlockAssertionForReason:];
-[SBLockScreenBiometricAuthenticationCoordinator acquireDisableCoordinatorAssertionForReason:];
-[SBLockScreenBiometricAuthenticationCoordinator acquireDisableUnlockAssertionForReason:];
-[SBLockScreenBiometricAuthenticationCoordinator acquireDisableWalletPreArmAssertionForReason:];
-[SBLockScreenBiometricAuthenticationCoordinator bioAuthenticatedWhileMenuButtonDown];
-[SBLockScreenBiometricAuthenticationCoordinator initWithBiometricResource:walletPreArmController:];
-[SBLockScreenBiometricAuthenticationCoordinator isAutoUnlockingDisabled];
-[SBLockScreenBiometricAuthenticationCoordinator isUnlockingDisabled];
-[SBLockScreenBiometricAuthenticationCoordinator isWalletPreArmDisabled];
-[SBLockScreenBiometricAuthenticationCoordinator setBioAuthenticatedWhileMenuButtonDown:];
-[SBLockScreenBiometricAuthenticationCoordinator walletPrearmRecognizer:didFailToRecognizeForReason:];
-[SBLockScreenBiometricAuthenticationCoordinator walletPrearmRecognizerDidRecognize:];
```
