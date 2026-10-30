# `LAPSPasscodePersistence` (protocol)

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 35 instance methods, 0 class methods

## Instance methods

```
-[LAPSPasscodePersistence hasPasscode];
-[LAPSPasscodePersistence isPasscodeRecoveryRestricted];
-[LAPSPasscodePersistence clearRecoveryPasscode];
-[LAPSPasscodePersistence passcodeCreationDate];
-[LAPSPasscodePersistence isPasscodeRecoverySupported];
-[LAPSPasscodePersistence passcodeType];
-[LAPSPasscodePersistence verifyPasscode:];
-[LAPSPasscodePersistence backoffTimeout];
-[LAPSPasscodePersistence backoffTimeoutForUserId:];
-[LAPSPasscodePersistence canChangePasscode];
-[LAPSPasscodePersistence canRemovePasscode:];
-[LAPSPasscodePersistence changePasscode:to:enableRecovery:error:];
-[LAPSPasscodePersistence defaultNewPasscodeType];
-[LAPSPasscodePersistence failedPasscodeAttempts];
-[LAPSPasscodePersistence failedPasscodeAttemptsForUserId:];
-[LAPSPasscodePersistence failedPasscodeRecoveryAttempts];
-[LAPSPasscodePersistence failedPasscodeRecoveryAttemptsForUserId:];
-[LAPSPasscodePersistence isPasscodeLockedOut];
-[LAPSPasscodePersistence isPasscodeLockedOutForUserId:];
-[LAPSPasscodePersistence isPasscodeRecoveryAvailable];
-[LAPSPasscodePersistence isPasscodeRecoveryEnabled];
-[LAPSPasscodePersistence localizedPasscodeRequirements];
-[LAPSPasscodePersistence maxPasscodeRecoveryAttempts];
-[LAPSPasscodePersistence maxPasscodeRecoveryAttemptsForUserId:];
-[LAPSPasscodePersistence performRecovery:newPasscode:enableRecovery:error:];
-[LAPSPasscodePersistence recoveryPasscodeType];
-[LAPSPasscodePersistence reportPasscodeDidChangeTo:completion:];
-[LAPSPasscodePersistence setPasscodeRecoveryEnabled:];
-[LAPSPasscodePersistence simplestAllowedNewPasscodeType];
-[LAPSPasscodePersistence verifyFixedLengthNumericPasscodeIsStrong:];
-[LAPSPasscodePersistence verifyNewPasscodeMeetsPlatformRequirements:error:];
-[LAPSPasscodePersistence verifyPasscode:contextRef:];
-[LAPSPasscodePersistence verifyPasscode:userId:contextRef:];
-[LAPSPasscodePersistence verifyRecoveryPasscode:];
-[LAPSPasscodePersistence verifyVariableLengthAlphanumericPasscodeIsStrong:];
```
