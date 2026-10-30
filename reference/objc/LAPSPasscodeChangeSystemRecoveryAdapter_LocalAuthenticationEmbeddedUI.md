# `LAPSPasscodeChangeSystemRecoveryAdapter`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LAPSPasscodeChangeSystem`
- 3 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"LAPSCurrentPasscodeService" _currentPasscodeService;
@"LAPSRecoveryPasscodeService" _passcodeRecoveryService;
@"LAPSNewPasscodeService" _newPasscodeService;
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
-[LAPSPasscodeChangeSystemRecoveryAdapter hasPasscode];
-[LAPSPasscodeChangeSystemRecoveryAdapter initWithPersistence:];
-[LAPSPasscodeChangeSystemRecoveryAdapter canChangePasscodeWithError:];
-[LAPSPasscodeChangeSystemRecoveryAdapter changePasscode:to:completion:];
-[LAPSPasscodeChangeSystemRecoveryAdapter lastPasscodeChange];
-[LAPSPasscodeChangeSystemRecoveryAdapter newPasscodeRequest];
-[LAPSPasscodeChangeSystemRecoveryAdapter oldPasscodeRequest];
-[LAPSPasscodeChangeSystemRecoveryAdapter verifyNewPasscode:completion:];
-[LAPSPasscodeChangeSystemRecoveryAdapter verifyPasscode:completion:];
-[LAPSPasscodeChangeSystemRecoveryAdapter verifyPasscode:contextRef:completion:];
```
