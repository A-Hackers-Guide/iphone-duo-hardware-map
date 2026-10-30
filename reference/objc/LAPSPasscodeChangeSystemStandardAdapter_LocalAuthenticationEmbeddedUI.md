# `LAPSPasscodeChangeSystemStandardAdapter`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LAPSPasscodeChangeSystem`
- 4 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"LAPSPasscodeChangeSystemOptions" _options;
@"LAPSCurrentPasscodeService" _currentPasscodeService;
@"LAPSNewPasscodeService" _newPasscodeService;
@"LAPSRecoveryPasscodeService" _recoveryPasscodeService;
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
-[LAPSPasscodeChangeSystemStandardAdapter hasPasscode];
-[LAPSPasscodeChangeSystemStandardAdapter initWithPersistence:];
-[LAPSPasscodeChangeSystemStandardAdapter canChangePasscodeWithError:];
-[LAPSPasscodeChangeSystemStandardAdapter changePasscode:to:completion:];
-[LAPSPasscodeChangeSystemStandardAdapter initWithPersistence:options:];
-[LAPSPasscodeChangeSystemStandardAdapter lastPasscodeChange];
-[LAPSPasscodeChangeSystemStandardAdapter newPasscodeRequest];
-[LAPSPasscodeChangeSystemStandardAdapter oldPasscodeRequest];
-[LAPSPasscodeChangeSystemStandardAdapter verifyNewPasscode:completion:];
-[LAPSPasscodeChangeSystemStandardAdapter verifyPasscode:completion:];
-[LAPSPasscodeChangeSystemStandardAdapter verifyPasscode:contextRef:completion:];
```
