# `LAPSPasscodeChangeController`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LAPSPasscodeChangeUIDelegate`, `LAPSPasscodeChangeController`
- 5 instance variables, 4 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"<LAPSPasscodeChangeSystem>" _system;
@"<LAPSPasscodeChangeUI>" _ui;
@"<LACPSAuthorizer>" _authorizer;
@"LAPSPasscodeChangeControllerOptions" _options;
@? _handler;
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
-[LAPSPasscodeChangeController cancel];
-[LAPSPasscodeChangeController startWithCompletion:];
-[LAPSPasscodeChangeController _presentErrorIfNeed:completion:];
-[LAPSPasscodeChangeController _checkCanChangePasscodeWithCompletion:];
-[LAPSPasscodeChangeController _extractCSPasscode:completion:];
-[LAPSPasscodeChangeController _extractPasscode:completion:];
-[LAPSPasscodeChangeController _fetchNewPasscode:completion:];
-[LAPSPasscodeChangeController _fetchOldPasscode:completion:];
-[LAPSPasscodeChangeController _injectNewPasscodeWithCompletion:];
-[LAPSPasscodeChangeController _injectOldPasscodeWithCompletion:];
-[LAPSPasscodeChangeController _notifyCompletionWithPasscode:error:];
-[LAPSPasscodeChangeController _runWithCompletion:];
-[LAPSPasscodeChangeController _shouldInjectNewPasscode];
-[LAPSPasscodeChangeController _shouldInjectOldPasscode];
-[LAPSPasscodeChangeController initWithSystem:authorizer:ui:];
-[LAPSPasscodeChangeController initWithSystem:authorizer:ui:options:];
-[LAPSPasscodeChangeController passcodeChangeUI:verifyNewPasscode:completion:];
-[LAPSPasscodeChangeController passcodeChangeUI:verifyPasscode:completion:];
-[LAPSPasscodeChangeController passcodeChangeUIDidDisappear:];
-[LAPSPasscodeChangeController verifyPasscode:completion:];
```
