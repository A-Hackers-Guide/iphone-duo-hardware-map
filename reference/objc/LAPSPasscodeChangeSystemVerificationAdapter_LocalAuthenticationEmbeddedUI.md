# `LAPSPasscodeChangeSystemVerificationAdapter`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LAPSPasscodeChangeSystem`
- 2 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"LAPSCurrentPasscodeService" _currentPasscodeService;
@"LAPSPasscodeVerificationSystemOptions" _options;
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
-[LAPSPasscodeChangeSystemVerificationAdapter hasPasscode];
-[LAPSPasscodeChangeSystemVerificationAdapter initWithPersistence:];
-[LAPSPasscodeChangeSystemVerificationAdapter canChangePasscodeWithError:];
-[LAPSPasscodeChangeSystemVerificationAdapter changePasscode:to:completion:];
-[LAPSPasscodeChangeSystemVerificationAdapter initWithPersistence:options:];
-[LAPSPasscodeChangeSystemVerificationAdapter lastPasscodeChange];
-[LAPSPasscodeChangeSystemVerificationAdapter newPasscodeRequest];
-[LAPSPasscodeChangeSystemVerificationAdapter oldPasscodeRequest];
-[LAPSPasscodeChangeSystemVerificationAdapter verifyNewPasscode:completion:];
-[LAPSPasscodeChangeSystemVerificationAdapter verifyPasscode:completion:];
-[LAPSPasscodeChangeSystemVerificationAdapter verifyPasscode:contextRef:completion:];
```
