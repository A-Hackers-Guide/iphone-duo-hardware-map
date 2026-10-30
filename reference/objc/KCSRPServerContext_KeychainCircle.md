# `KCSRPServerContext`

- Image: [`/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`](../userland/System__Library__PrivateFrameworks__KeychainCircle.framework__KeychainCircle.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `KCSRPContext`
- 2 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSData" _salt;
@"NSData" _verifier;
```

## Properties

```
@property (T@"NSData",&,V_verifier) verifier;
@property (T@"NSData",R,V_salt) salt;
```

## Instance methods

```
-[KCSRPServerContext verifier];
-[KCSRPServerContext salt];
-[KCSRPServerContext setVerifier:];
-[KCSRPServerContext copyChallengeFor:error:];
-[KCSRPServerContext copyConfirmationFor:error:];
-[KCSRPServerContext initWithUser:password:digestInfo:group:randomSource:];
-[KCSRPServerContext initWithUser:salt:verifier:digestInfo:group:randomSource:];
-[KCSRPServerContext resetWithPassword:error:];
```
