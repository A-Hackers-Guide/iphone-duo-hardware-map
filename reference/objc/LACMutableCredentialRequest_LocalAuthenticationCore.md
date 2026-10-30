# `LACMutableCredentialRequest`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACCredentialRequest`
- 5 instance variables, 9 properties, 13 instance methods, 0 class methods

## Instance variables

```
I _identifier;
I _userID;
q _credential;
@"NSData" _externalizedContext;
{?="val"[8I]} _auditToken;
```

## Properties

```
@property (TI,N,V_identifier) identifier;
@property (Tq,N,V_credential) credential;
@property (T@"NSData",&,N,V_externalizedContext) externalizedContext;
@property (TI,N,V_userID) userID;
@property (T{?=[8I]},N,V_auditToken) auditToken;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACMutableCredentialRequest credential];
-[LACMutableCredentialRequest userID];
-[LACMutableCredentialRequest setUserID:];
-[LACMutableCredentialRequest identifier];
-[LACMutableCredentialRequest init];
-[LACMutableCredentialRequest externalizedContext];
-[LACMutableCredentialRequest setIdentifier:];
-[LACMutableCredentialRequest setAuditToken:];
-[LACMutableCredentialRequest setExternalizedContext:];
-[LACMutableCredentialRequest description];
-[LACMutableCredentialRequest auditToken];
-[LACMutableCredentialRequest isEqual:];
-[LACMutableCredentialRequest setCredential:];
```
