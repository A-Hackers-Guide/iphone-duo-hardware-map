# `SBFMutableMobileKeyBagState`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFMobileKeyBagState`
- 0 instance variables, 9 properties, 13 instance methods, 0 class methods

## Properties

```
@property (Tq,D,N) lockState;
@property (Td,D,N) backOffTime;
@property (TQ,D,N) failedAttemptCount;
@property (TB,D,N) permanentlyBlocked;
@property (TB,D,N) shouldWipe;
@property (TB,D,N) recoveryEnabled;
@property (TB,D,N) recoveryRequired;
@property (TB,D,N) recoveryPossible;
@property (Tq,D,N) escrowCount;
```

## Instance methods

```
-[SBFMutableMobileKeyBagState setLockState:];
-[SBFMutableMobileKeyBagState setEscrowCount:];
-[SBFMutableMobileKeyBagState setRecoveryRequired:];
-[SBFMutableMobileKeyBagState setBackOffTime:];
-[SBFMutableMobileKeyBagState init];
-[SBFMutableMobileKeyBagState setPermanentlyBlocked:];
-[SBFMutableMobileKeyBagState initWithKeyBagInfo:extended:];
-[SBFMutableMobileKeyBagState setFailedAttemptCount:];
-[SBFMutableMobileKeyBagState setShouldWipe:];
-[SBFMutableMobileKeyBagState _mutableState];
-[SBFMutableMobileKeyBagState setRecoveryPossible:];
-[SBFMutableMobileKeyBagState copyWithZone:];
-[SBFMutableMobileKeyBagState setRecoveryEnabled:];
```
