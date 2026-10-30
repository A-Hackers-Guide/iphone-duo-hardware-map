# `LAPSFetchOldPasscodeRequest`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"LACPasscode" _passcodeType;
q _failedAttempts;
q _backoffTimeout;
```

## Properties

```
@property (T@"LACPasscode",&,N,V_passcodeType) passcodeType;
@property (Tq,N,V_failedAttempts) failedAttempts;
@property (Tq,N,V_backoffTimeout) backoffTimeout;
```

## Instance methods

```
-[LAPSFetchOldPasscodeRequest init];
-[LAPSFetchOldPasscodeRequest setPasscodeType:];
-[LAPSFetchOldPasscodeRequest passcodeType];
-[LAPSFetchOldPasscodeRequest failedAttempts];
-[LAPSFetchOldPasscodeRequest setFailedAttempts:];
-[LAPSFetchOldPasscodeRequest backoffTimeout];
-[LAPSFetchOldPasscodeRequest setBackoffTimeout:];
```
