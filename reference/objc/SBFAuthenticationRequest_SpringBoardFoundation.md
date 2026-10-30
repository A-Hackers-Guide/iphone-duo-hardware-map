# `SBFAuthenticationRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 19 instance methods, 0 class methods

## Instance variables

```
Q _type;
q _source;
@? _handler;
B _skipSEKeepUserDataOperation;
B _verifyOnly;
@"NSString" _passcode;
```

## Properties

```
@property (TQ,R,N,V_type) type;
@property (Tq,R,N,V_source) source;
@property (T@"NSString",R,C,N,V_passcode) passcode;
@property (T@?,R,C,N,V_handler) handler;
@property (TB,R,N,V_skipSEKeepUserDataOperation) skipSEKeepUserDataOperation;
@property (TB,R,N,V_verifyOnly) verifyOnly;
```

## Instance methods

```
-[SBFAuthenticationRequest publicDescription];
-[SBFAuthenticationRequest passcode];
-[SBFAuthenticationRequest succinctDescriptionBuilder];
-[SBFAuthenticationRequest descriptionWithMultilinePrefix:];
-[SBFAuthenticationRequest succinctDescription];
-[SBFAuthenticationRequest type];
-[SBFAuthenticationRequest handler];
-[SBFAuthenticationRequest description];
-[SBFAuthenticationRequest source];
-[SBFAuthenticationRequest descriptionBuilderWithMultilinePrefix:];
-[SBFAuthenticationRequest initForPasscode:source:handler:];
-[SBFAuthenticationRequest _initWithType:source:passcode:skipSEKeepUserDataOperation:verifyOnly:handler:];
-[SBFAuthenticationRequest initForBiometricAuthenticationWithSource:];
-[SBFAuthenticationRequest initForBiometricAuthenticationWithSource:handler:];
-[SBFAuthenticationRequest initForPasscode:source:];
-[SBFAuthenticationRequest initForPasscode:source:skipSEKeepUserDataOperation:handler:];
-[SBFAuthenticationRequest initForPasscode:source:skipSEKeepUserDataOperation:verifyOnly:handler:];
-[SBFAuthenticationRequest skipSEKeepUserDataOperation];
-[SBFAuthenticationRequest verifyOnly];
```
