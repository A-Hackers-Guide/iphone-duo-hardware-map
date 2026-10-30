# `LAPSPasscodePersistenceAdapter`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LAPSPasscodePersistence`
- 5 instance variables, 4 properties, 36 instance methods, 0 class methods

## Instance variables

```
@"LAPSPasscodePersistenceLAAdapter" _laAdapter;
@"LAPSPasscodePersistenceMCAdapter" _mcAdapter;
@"LAPSPasscodePersistenceCDPAdapter" _cdpAdapter;
@"LAPSPasscodePersistenceMKBAdapter" _mkbAdapter;
@"LAPSPasscodePersistenceSecAdapter" _secAdapter;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LAPSPasscodePersistenceAdapter init];
-[LAPSPasscodePersistenceAdapter hasPasscode];
-[LAPSPasscodePersistenceAdapter isPasscodeRecoveryRestricted];
-[LAPSPasscodePersistenceAdapter clearRecoveryPasscode];
-[LAPSPasscodePersistenceAdapter passcodeCreationDate];
-[LAPSPasscodePersistenceAdapter isPasscodeRecoverySupported];
-[LAPSPasscodePersistenceAdapter passcodeType];
-[LAPSPasscodePersistenceAdapter verifyPasscode:];
-[LAPSPasscodePersistenceAdapter backoffTimeout];
-[LAPSPasscodePersistenceAdapter backoffTimeoutForUserId:];
-[LAPSPasscodePersistenceAdapter canChangePasscode];
-[LAPSPasscodePersistenceAdapter canRemovePasscode:];
-[LAPSPasscodePersistenceAdapter changePasscode:to:enableRecovery:error:];
-[LAPSPasscodePersistenceAdapter defaultNewPasscodeType];
-[LAPSPasscodePersistenceAdapter failedPasscodeAttempts];
-[LAPSPasscodePersistenceAdapter failedPasscodeAttemptsForUserId:];
-[LAPSPasscodePersistenceAdapter failedPasscodeRecoveryAttempts];
-[LAPSPasscodePersistenceAdapter failedPasscodeRecoveryAttemptsForUserId:];
-[LAPSPasscodePersistenceAdapter isPasscodeLockedOut];
-[LAPSPasscodePersistenceAdapter isPasscodeLockedOutForUserId:];
-[LAPSPasscodePersistenceAdapter isPasscodeRecoveryAvailable];
-[LAPSPasscodePersistenceAdapter isPasscodeRecoveryEnabled];
-[LAPSPasscodePersistenceAdapter localizedPasscodeRequirements];
-[LAPSPasscodePersistenceAdapter maxPasscodeRecoveryAttempts];
-[LAPSPasscodePersistenceAdapter maxPasscodeRecoveryAttemptsForUserId:];
-[LAPSPasscodePersistenceAdapter performRecovery:newPasscode:enableRecovery:error:];
-[LAPSPasscodePersistenceAdapter recoveryPasscodeType];
-[LAPSPasscodePersistenceAdapter reportPasscodeDidChangeTo:completion:];
-[LAPSPasscodePersistenceAdapter setPasscodeRecoveryEnabled:];
-[LAPSPasscodePersistenceAdapter simplestAllowedNewPasscodeType];
-[LAPSPasscodePersistenceAdapter verifyFixedLengthNumericPasscodeIsStrong:];
-[LAPSPasscodePersistenceAdapter verifyNewPasscodeMeetsPlatformRequirements:error:];
-[LAPSPasscodePersistenceAdapter verifyPasscode:contextRef:];
-[LAPSPasscodePersistenceAdapter verifyPasscode:userId:contextRef:];
-[LAPSPasscodePersistenceAdapter verifyRecoveryPasscode:];
-[LAPSPasscodePersistenceAdapter verifyVariableLengthAlphanumericPasscodeIsStrong:];
```
