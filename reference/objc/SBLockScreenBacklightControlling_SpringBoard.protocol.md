# `SBLockScreenBacklightControlling` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 10 instance methods, 0 class methods

## Properties

```
@property (Tq,R,N) backlightLuminance;
@property (Td,N) backlightLevel;
```

## Instance methods

```
-[SBLockScreenBacklightControlling setBacklightLevel:];
-[SBLockScreenBacklightControlling backlightLevel];
-[SBLockScreenBacklightControlling setInScreenOffMode:forAutoUnlock:fromUnlockSource:];
-[SBLockScreenBacklightControlling setInScreenOffMode:];
-[SBLockScreenBacklightControlling isInScreenOffMode];
-[SBLockScreenBacklightControlling screenSleepCompletedForSource:];
-[SBLockScreenBacklightControlling setInScreenOffMode:preservingCoverSheetPresentationState:];
-[SBLockScreenBacklightControlling shouldDisableALS];
-[SBLockScreenBacklightControlling startLockScreenFadeInAnimationForSource:];
-[SBLockScreenBacklightControlling backlightLuminance];
```
