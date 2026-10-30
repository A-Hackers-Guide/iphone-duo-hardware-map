# `SBLockScreenLockingAndUnlocking` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 1 properties, 11 instance methods, 0 class methods

## Properties

```
@property (TB,N,GisAuthenticated) authenticated;
```

## Instance methods

```
-[SBLockScreenLockingAndUnlocking isAuthenticated];
-[SBLockScreenLockingAndUnlocking jiggleLockIcon];
-[SBLockScreenLockingAndUnlocking setAuthenticated:];
-[SBLockScreenLockingAndUnlocking prepareForUIUnlock];
-[SBLockScreenLockingAndUnlocking shouldUnlockUIOnKeyDownEvent];
-[SBLockScreenLockingAndUnlocking willUIUnlockFromSource:isLockScreenDisabledForAssertion:];
-[SBLockScreenLockingAndUnlocking isProcessingUnlockAttempt];
-[SBLockScreenLockingAndUnlocking isUnlockDisabled];
-[SBLockScreenLockingAndUnlocking finishUIUnlockFromSource:];
-[SBLockScreenLockingAndUnlocking canBeDeactivatedForUIUnlockFromSource:];
-[SBLockScreenLockingAndUnlocking prepareForUILock];
```
