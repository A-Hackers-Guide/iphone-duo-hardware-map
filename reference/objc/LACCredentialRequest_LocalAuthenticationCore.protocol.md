# `LACCredentialRequest` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `LACRequest`
- 0 instance variables, 4 properties, 4 instance methods, 0 class methods

## Properties

```
@property (Tq,R,N) credential;
@property (T@"NSData",R,N) externalizedContext;
@property (TI,R,N) userID;
@property (T{?=[8I]},R,N) auditToken;
```

## Instance methods

```
-[LACCredentialRequest credential];
-[LACCredentialRequest userID];
-[LACCredentialRequest externalizedContext];
-[LACCredentialRequest auditToken];
```
