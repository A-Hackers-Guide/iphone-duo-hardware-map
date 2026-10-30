# `SBFShamMobileKeyBag`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 0 properties, 12 instance methods, 2 class methods

## Instance variables

```
f _timeScaleFactor;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSData" _queue_correctPasscode;
@"SBFMutableMobileKeyBagState" _queue_state;
Q _queue_escrowState;
f _queue_escrowCountTotal;
f _queue_escrowCountDelta;
@"NSData" _queue_trialPasscode;
```

## Class methods

```
+[SBFShamMobileKeyBag shamKeyBagWithRecoveryRequired:correctPasscode:];
+[SBFShamMobileKeyBag shamKeyBagWithRecoveryRequired:recoveryPossible:timeScaleFactor:correctPasscode:];
```

## Instance methods

```
-[SBFShamMobileKeyBag lock];
-[SBFShamMobileKeyBag state];
-[SBFShamMobileKeyBag extendedState];
-[SBFShamMobileKeyBag _queue_initializeSecretChangeMachine:];
-[SBFShamMobileKeyBag _queue_stepSecretChangeMachine];
-[SBFShamMobileKeyBag _simplifiedLockStateForLockState:];
-[SBFShamMobileKeyBag beginRecovery:error:];
-[SBFShamMobileKeyBag createStashBag:skipSEKeepUserDataOperation:completion:];
-[SBFShamMobileKeyBag createStashBag:skipSEKeepUserDataOperation:completion:completionQueue:];
-[SBFShamMobileKeyBag initWithRecoveryRequired:correctPasscode:];
-[SBFShamMobileKeyBag initWithRecoveryRequired:recoveryPossible:timeScaleFactor:correctPasscode:];
-[SBFShamMobileKeyBag waitForUnlockWithTimeout:];
```
