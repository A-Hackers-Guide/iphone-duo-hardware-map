# `LACPasscodeVerificationRequest` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 11 properties, 11 instance methods, 0 class methods

## Properties

```
@property (T@"LACSUnmanagedExtractablePassword",R,N) passcode;
@property (T@"NSData",R,N) acmContext;
@property (T@"LACAuditToken",R,N) auditToken;
@property (T@"NSNumber",R,N) userId;
@property (Tq,R,N) policy;
@property (T@"NSDictionary",R,N) options;
@property (TB,R,N) bioLockoutRecovery;
@property (T@"NSString",R,N) pamService;
@property (T@"NSString",R,N) pamUser;
@property (T@"NSData",R,N) pamToken;
@property (Tq,R,N) authenticator;
```

## Instance methods

```
-[LACPasscodeVerificationRequest passcode];
-[LACPasscodeVerificationRequest auditToken];
-[LACPasscodeVerificationRequest options];
-[LACPasscodeVerificationRequest userId];
-[LACPasscodeVerificationRequest policy];
-[LACPasscodeVerificationRequest authenticator];
-[LACPasscodeVerificationRequest pamUser];
-[LACPasscodeVerificationRequest acmContext];
-[LACPasscodeVerificationRequest bioLockoutRecovery];
-[LACPasscodeVerificationRequest pamService];
-[LACPasscodeVerificationRequest pamToken];
```
