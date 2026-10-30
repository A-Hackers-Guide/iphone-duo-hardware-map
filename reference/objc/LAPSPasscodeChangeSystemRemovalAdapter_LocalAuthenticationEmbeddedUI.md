# `LAPSPasscodeChangeSystemRemovalAdapter`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LAPSPasscodeChangeSystem`
- 2 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"LAPSCurrentPasscodeService" _currentPasscodeService;
@"<LAPSPasscodeChangeSystem>" _changeSystem;
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
-[LAPSPasscodeChangeSystemRemovalAdapter hasPasscode];
-[LAPSPasscodeChangeSystemRemovalAdapter initWithPersistence:];
-[LAPSPasscodeChangeSystemRemovalAdapter canChangePasscodeWithError:];
-[LAPSPasscodeChangeSystemRemovalAdapter changePasscode:to:completion:];
-[LAPSPasscodeChangeSystemRemovalAdapter lastPasscodeChange];
-[LAPSPasscodeChangeSystemRemovalAdapter newPasscodeRequest];
-[LAPSPasscodeChangeSystemRemovalAdapter oldPasscodeRequest];
-[LAPSPasscodeChangeSystemRemovalAdapter verifyNewPasscode:completion:];
-[LAPSPasscodeChangeSystemRemovalAdapter verifyPasscode:completion:];
-[LAPSPasscodeChangeSystemRemovalAdapter verifyPasscode:contextRef:completion:];
```
