# `LAPSRecoveryPasscodeService`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"<LAPSPasscodePersistence>" _persistence;
```

## Properties

```
@property (T@"<LAPSPasscodePersistence>",R,N,V_persistence) persistence;
```

## Instance methods

```
-[LAPSRecoveryPasscodeService persistence];
-[LAPSRecoveryPasscodeService isPasscodeRecoveryRestricted];
-[LAPSRecoveryPasscodeService isPasscodeRecoverySupported];
-[LAPSRecoveryPasscodeService initWithPersistence:];
-[LAPSRecoveryPasscodeService passcodeType];
-[LAPSRecoveryPasscodeService _failedPasscodeRecoveryAttempts];
-[LAPSRecoveryPasscodeService _clearRecoveryPasscode];
-[LAPSRecoveryPasscodeService _failedPasscodeAttempts];
-[LAPSRecoveryPasscodeService _hasAttemptedPasscodeEnoughTimes];
-[LAPSRecoveryPasscodeService _hasPasscodeRecoveryAttemptsLeft];
-[LAPSRecoveryPasscodeService _maxPasscodeRecoveryAttempts];
-[LAPSRecoveryPasscodeService _minRequiredPasscodeFailures];
-[LAPSRecoveryPasscodeService _reportPasscodeChangedTo:];
-[LAPSRecoveryPasscodeService _setPasscodeRecoveryEnabled:];
-[LAPSRecoveryPasscodeService changePasscode:to:enableRecovery:completion:];
-[LAPSRecoveryPasscodeService failedPasscodeAttempts];
-[LAPSRecoveryPasscodeService isPasscodeRecoveryAvailableWithError:];
-[LAPSRecoveryPasscodeService isPasscodeRecoveryEnabled];
-[LAPSRecoveryPasscodeService verifyPasscode:completion:];
```
