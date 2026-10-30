# `LAPasscodeVerificationServiceOptions`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _dismissUIAfterCompletion;
@"NSString" _title;
@"NSString" _passcodePrompt;
@"NSString" _passcodeSubPrompt;
@"NSNumber" _userId;
q _passcodeType;
@"LACSExtractablePassword" _passcode;
```

## Properties

```
@property (T@"LACSExtractablePassword",&,N,V_passcode) passcode;
@property (T@"NSString",&,N,V_title) title;
@property (T@"NSString",&,N,V_passcodePrompt) passcodePrompt;
@property (T@"NSString",&,N,V_passcodeSubPrompt) passcodeSubPrompt;
@property (TB,N,V_dismissUIAfterCompletion) dismissUIAfterCompletion;
@property (T@"NSNumber",C,N,V_userId) userId;
@property (Tq,N,V_passcodeType) passcodeType;
```

## Instance methods

```
-[LAPasscodeVerificationServiceOptions passcode];
-[LAPasscodeVerificationServiceOptions title];
-[LAPasscodeVerificationServiceOptions description];
-[LAPasscodeVerificationServiceOptions setTitle:];
-[LAPasscodeVerificationServiceOptions setUserId:];
-[LAPasscodeVerificationServiceOptions setPasscodeType:];
-[LAPasscodeVerificationServiceOptions userId];
-[LAPasscodeVerificationServiceOptions passcodeType];
-[LAPasscodeVerificationServiceOptions setPasscode:];
-[LAPasscodeVerificationServiceOptions setPasscodePrompt:];
-[LAPasscodeVerificationServiceOptions dismissUIAfterCompletion];
-[LAPasscodeVerificationServiceOptions passcodePrompt];
-[LAPasscodeVerificationServiceOptions passcodeSubPrompt];
-[LAPasscodeVerificationServiceOptions setDismissUIAfterCompletion:];
-[LAPasscodeVerificationServiceOptions setPasscodeSubPrompt:];
```
