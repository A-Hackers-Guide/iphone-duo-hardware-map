# `SBFUserAuthenticationController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFMobileKeyBagObserver`, `SBFUserAuthenticationModelDelegate`, `SBFAuthenticationAssertionProviding`, `SBFAuthenticationStatusProvider`, `SBFPasscodeFieldChangeObserver`, `SBFSecureDisplayStateProviding`
- 16 instance variables, 9 properties, 80 instance methods, 0 class methods

## Instance variables

```
@"SBFMobileKeyBag" _keybag;
@"NSMutableArray" _responders;
@"NSHashTable" _observers;
@"<SBFUserAuthenticationModel>" _model;
q _authenticationState;
@"NSDate" _lastRevokedAuthenticationDate;
@"SBFAuthenticationAssertionManager" _assertionManager;
@"<SBFAuthenticationPolicy>" _policy;
@"NSString" _lastIncorrectPasscodeAttempt;
@"SBFAuthenticationAssertion" _transientAuthCheckingAssertion;
^{__CFRunLoopObserver=} _runLoopObserver;
@"PCPersistentTimer" _unblockTimer;
q _cachedAuthFlag;
@"SBFSecureDisplayCoordinator" _secureDisplayCoordinator;
@"SBFMobileKeyBagState" _cachedExtendedState;
@"BSCompoundAssertion" _secureDisplayDeferralAssertions;
```

## Properties

```
@property (T@"SBFSecureDisplayCoordinator",R,N,V_secureDisplayCoordinator) secureDisplayCoordinator;
@property (T@"<SBFAuthenticationPolicy>",&,N,G_policy,S_setPolicy:,V_policy) policy;
@property (T@"NSDate",R,N,V_lastRevokedAuthenticationDate) lastRevokedAuthenticationDate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) supportsSecureDisplayMode;
@property (TB,R,N,GisInSecureDisplayMode) inSecureDisplayMode;
```

## Instance methods

```
-[SBFUserAuthenticationController isAuthenticated];
-[SBFUserAuthenticationController _addAuthenticationAssertion:];
-[SBFUserAuthenticationController _handleSuccessfulAuthentication:responder:];
-[SBFUserAuthenticationController _cachedLockStateExtended];
-[SBFUserAuthenticationController _setModel:];
-[SBFUserAuthenticationController _setup_runLoopObserverIfNecessary];
-[SBFUserAuthenticationController _addAsFirstResponder:];
-[SBFUserAuthenticationController _isAssertionValid:];
-[SBFUserAuthenticationController publicDescription];
-[SBFUserAuthenticationController _setupPolicy:];
-[SBFUserAuthenticationController processAuthenticationRequest:];
-[SBFUserAuthenticationController secureDisplayCoordinator];
-[SBFUserAuthenticationController _isTemporarilyBlocked];
-[SBFUserAuthenticationController deviceLockStateMayHaveChangedForModel:];
-[SBFUserAuthenticationController revokeAuthenticationIfNecessaryForPublicReason:];
-[SBFUserAuthenticationController _isPermanentlyBlocked];
-[SBFUserAuthenticationController succinctDescriptionBuilder];
-[SBFUserAuthenticationController _revokeAuthenticationImmediately:forPublicReason:];
-[SBFUserAuthenticationController createGracePeriodAssertionWithReason:];
-[SBFUserAuthenticationController _isInBioUnlockState];
-[SBFUserAuthenticationController createSecureDisplayDeferralAssertionWithReason:];
-[SBFUserAuthenticationController _shouldRevokeAuthenticationNow];
-[SBFUserAuthenticationController _evaluateAuthenticationAttempt:outError:];
-[SBFUserAuthenticationController _evaluateBiometricAttempt:];
-[SBFUserAuthenticationController _isUserRequestedEraseEnabled];
-[SBFUserAuthenticationController _policy];
-[SBFUserAuthenticationController dealloc];
-[SBFUserAuthenticationController initWithAssertionManager:policy:keybag:model:];
-[SBFUserAuthenticationController _performNilPasscodeCheck];
-[SBFUserAuthenticationController _updateAuthenticationStateImmediately:forPublicReason:];
-[SBFUserAuthenticationController notePasscodeEntryBegan];
-[SBFUserAuthenticationController _removeAuthResponder:];
-[SBFUserAuthenticationController _setAuthState:];
-[SBFUserAuthenticationController revokeAuthenticationImmediatelyIfNecessaryForPublicReason:];
-[SBFUserAuthenticationController removeResponder:];
-[SBFUserAuthenticationController hasAuthenticatedAtLeastOnceSinceBoot];
-[SBFUserAuthenticationController descriptionWithMultilinePrefix:];
-[SBFUserAuthenticationController _handleFailedAuthentication:error:responder:];
-[SBFUserAuthenticationController _isInGracePeriodState];
-[SBFUserAuthenticationController _processAuthenticationRequest:responder:];
-[SBFUserAuthenticationController _timeUntilUnblockedSinceReferenceDate];
-[SBFUserAuthenticationController _removePrivateAuthenticationObserver:];
-[SBFUserAuthenticationController processAuthenticationRequest:responder:];
-[SBFUserAuthenticationController _scheduleUnblockTimer];
-[SBFUserAuthenticationController _updateAuthenticationStateAndDateForLockState:];
-[SBFUserAuthenticationController succinctDescription];
-[SBFUserAuthenticationController _authenticateIfInGracePeriod];
-[SBFUserAuthenticationController createKeybagUnlockAssertionWithReason:];
-[SBFUserAuthenticationController _updateSecureModeIfNecessaryForNewAuthState];
-[SBFUserAuthenticationController _noteDeviceLockStateMayHaveChangedForExternalReasons];
-[SBFUserAuthenticationController _boolForAuthenticationResult:];
-[SBFUserAuthenticationController hasPasscodeSet];
-[SBFUserAuthenticationController revokeAuthenticationImmediatelyForPublicReason:];
-[SBFUserAuthenticationController _evaluatePasscodeAttempt:outError:];
-[SBFUserAuthenticationController authenticationStatusProviderTreatingContinuityUnlockedAsUnlocked:];
-[SBFUserAuthenticationController isInSecureDisplayMode];
-[SBFUserAuthenticationController keybag:extendedStateDidChange:];
-[SBFUserAuthenticationController notePasscodeEntryCancelled];
-[SBFUserAuthenticationController _refreshModelCacheIfNeeded];
-[SBFUserAuthenticationController _clearBlockedState];
-[SBFUserAuthenticationController _notifyClientsOfAuthenticationResult:forRequest:error:withResponder:];
-[SBFUserAuthenticationController addAsFirstResponder:];
-[SBFUserAuthenticationController _setPolicy:];
-[SBFUserAuthenticationController _addPrivateAuthenticationObserver:];
-[SBFUserAuthenticationController lastRevokedAuthenticationDate];
-[SBFUserAuthenticationController _updateAuthenticationStateForPublicReason:];
-[SBFUserAuthenticationController _invalidateCachedPasscodeLockState];
-[SBFUserAuthenticationController _clearUnblockTimer];
-[SBFUserAuthenticationController deviceLockModelRequestsDeviceWipe:];
-[SBFUserAuthenticationController description];
-[SBFUserAuthenticationController _handleInvalidAuthentication:responder:];
-[SBFUserAuthenticationController _unblockTimerFired];
-[SBFUserAuthenticationController _notifyAboutTemporaryBlockStatusChanged];
-[SBFUserAuthenticationController supportsSecureDisplayMode];
-[SBFUserAuthenticationController _removeAuthenticationAssertion:];
-[SBFUserAuthenticationController _isUserAuthenticated];
-[SBFUserAuthenticationController _uncachePasscodeIfNecessary];
-[SBFUserAuthenticationController isAuthenticatedCached];
-[SBFUserAuthenticationController keybagDidUnlockForTheFirstTime:];
-[SBFUserAuthenticationController descriptionBuilderWithMultilinePrefix:];
```
