# `LAPSPasscodeChangeAuthorizerDTOAdapter`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACPSAuthorizer`
- 1 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"LAPSPasscodeChangeAuthorizationOptions" _options;
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
-[LAPSPasscodeChangeAuthorizerDTOAdapter initWithOptions:];
-[LAPSPasscodeChangeAuthorizerDTOAdapter authorizeWithCompletion:];
-[LAPSPasscodeChangeAuthorizerDTOAdapter _authorizeOperationWithIdentifier:options:completion:];
-[LAPSPasscodeChangeAuthorizerDTOAdapter _authorizePasscodeChangeWithCompletion:];
-[LAPSPasscodeChangeAuthorizerDTOAdapter _authorizePasscodeRecoveryWithCompletion:];
-[LAPSPasscodeChangeAuthorizerDTOAdapter _authorizePasscodeRemovalWithCompletion:];
-[LAPSPasscodeChangeAuthorizerDTOAdapter _authorizePasscodeVerificationWithCompletion:];
```
