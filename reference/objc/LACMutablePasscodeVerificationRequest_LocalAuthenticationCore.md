# `LACMutablePasscodeVerificationRequest`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACPasscodeVerificationRequest`
- 11 instance variables, 12 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"LACSUnmanagedExtractablePassword" passcode;
? acmContext;
@"LACAuditToken" auditToken;
q authenticator;
@"NSNumber" userId;
q policy;
? options;
B bioLockoutRecovery;
? pamService;
? pamUser;
? pamToken;
```

## Properties

```
@property (T@"LACSUnmanagedExtractablePassword",N,R,Vpasscode) passcode;
@property (T@"NSData",N,R) acmContext;
@property (T@"LACAuditToken",N,R,VauditToken) auditToken;
@property (Tq,N,Vauthenticator) authenticator;
@property (T@"NSNumber",N,&,VuserId) userId;
@property (Tq,N,Vpolicy) policy;
@property (T@"NSDictionary",N,C) options;
@property (TB,N,VbioLockoutRecovery) bioLockoutRecovery;
@property (T@"NSString",N,C) pamService;
@property (T@"NSString",N,C) pamUser;
@property (T@"NSData",N,C) pamToken;
@property (T@"NSString",N,R) description;
```

## Instance methods

```
-[LACMutablePasscodeVerificationRequest passcode];
-[LACMutablePasscodeVerificationRequest setOptions:];
-[LACMutablePasscodeVerificationRequest init];
-[LACMutablePasscodeVerificationRequest initWithRequest:];
-[LACMutablePasscodeVerificationRequest description];
-[LACMutablePasscodeVerificationRequest auditToken];
-[LACMutablePasscodeVerificationRequest setUserId:];
-[LACMutablePasscodeVerificationRequest options];
-[LACMutablePasscodeVerificationRequest userId];
-[LACMutablePasscodeVerificationRequest setPolicy:];
-[LACMutablePasscodeVerificationRequest policy];
-[LACMutablePasscodeVerificationRequest authenticator];
-[LACMutablePasscodeVerificationRequest setAuthenticator:];
-[LACMutablePasscodeVerificationRequest pamUser];
-[LACMutablePasscodeVerificationRequest acmContext];
-[LACMutablePasscodeVerificationRequest bioLockoutRecovery];
-[LACMutablePasscodeVerificationRequest initWithPasscode:acmContext:auditToken:];
-[LACMutablePasscodeVerificationRequest initWithPasscode:acmContext:auditToken:pamService:pamUser:pamToken:];
-[LACMutablePasscodeVerificationRequest initWithPasscode:acmContext:rawAuditToken:];
-[LACMutablePasscodeVerificationRequest pamService];
-[LACMutablePasscodeVerificationRequest pamToken];
-[LACMutablePasscodeVerificationRequest setBioLockoutRecovery:];
-[LACMutablePasscodeVerificationRequest setPamService:];
-[LACMutablePasscodeVerificationRequest setPamToken:];
-[LACMutablePasscodeVerificationRequest setPamUser:];
```
