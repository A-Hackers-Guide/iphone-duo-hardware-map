# `SBSecurityDefaults`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAbstractSpringBoardDefaultDomain`
- 0 instance variables, 11 properties, 3 instance methods, 0 class methods

## Properties

```
@property (TB,D,N,GisBlockedForThermal) blockedForThermal;
@property (T@"NSNumber",&,D,N,GisPendingDeviceWipe) pendingDeviceWipe;
@property (T@"NSNumber",&,D,N,GisBlockedForPasscode) blockedForPasscode;
@property (T@"NSNumber",&,D,N) numberOfFailedPasscodeAttempts;
@property (T@"NSNumber",&,D,N) unblockTimeFromReferenceDate;
@property (T@"NSNumber",&,D,N) blockStateGeneration;
@property (TB,R,D,N,GisDeviceWipeEnabled) deviceWipeEnabled;
@property (TB,R,D,N) dontLockEver;
@property (TB,R,D,N) allowLockAndUnlockWithCase;
@property (TB,R,D,N) enableLayerBasedViewSecurity;
@property (TB,R,D,N) reportSecureDrawViolations;
```

## Instance methods

```
-[SBSecurityDefaults _bindAndRegisterDefaults];
-[SBSecurityDefaults deviceLockDefaultForKey:];
-[SBSecurityDefaults setDeviceLockDefault:forKey:];
```
