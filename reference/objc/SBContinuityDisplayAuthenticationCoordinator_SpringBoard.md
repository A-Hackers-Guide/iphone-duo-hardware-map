# `SBContinuityDisplayAuthenticationCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`, `SBFMobileKeyBagObserver`
- 9 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"BSCompoundAssertion" _continuityDisplaySessionAssertions;
@"BSContinuousMachTimer" _heartbeatTimer;
@"SBLockScreenCoordinator" _lockScreenCoordinator;
@"SBFMobileKeyBag" _mobileKeyBag;
@"NSHashTable" _observers;
B _invalidated;
Q _previousLockState;
B _sessionActive;
d _heartbeatInterval;
```

## Properties

```
@property (TB,N,G_isSessionActive,S_setSessionActive:,V_sessionActive) sessionActive;
@property (Td,N,V_heartbeatInterval) heartbeatInterval;
@property (TQ,R,N) lockState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBContinuityDisplayAuthenticationCoordinator lockState];
-[SBContinuityDisplayAuthenticationCoordinator removeObserver:];
-[SBContinuityDisplayAuthenticationCoordinator dealloc];
-[SBContinuityDisplayAuthenticationCoordinator addObserver:];
-[SBContinuityDisplayAuthenticationCoordinator invalidate];
-[SBContinuityDisplayAuthenticationCoordinator keybag:extendedStateDidChange:];
-[SBContinuityDisplayAuthenticationCoordinator _handleAuthenticationHeartbeatTimer];
-[SBContinuityDisplayAuthenticationCoordinator _handleKeyBagStateChange];
-[SBContinuityDisplayAuthenticationCoordinator _isSessionActive];
-[SBContinuityDisplayAuthenticationCoordinator _setSessionActive:];
-[SBContinuityDisplayAuthenticationCoordinator _updateSessionState];
-[SBContinuityDisplayAuthenticationCoordinator acquireContinuityDisplayActiveAssertionForReason:];
-[SBContinuityDisplayAuthenticationCoordinator heartbeatInterval];
-[SBContinuityDisplayAuthenticationCoordinator initWithLockScreenCoordinator:mobileKeyBag:];
-[SBContinuityDisplayAuthenticationCoordinator setHeartbeatInterval:];
```
