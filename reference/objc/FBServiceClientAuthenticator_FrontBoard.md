# `FBServiceClientAuthenticator`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 2 instance variables, 6 properties, 15 instance methods, 6 class methods

## Instance variables

```
@"NSString" _entitlement;
Q _credentials;
```

## Properties

```
@property (T@"NSString",R,C,N,V_entitlement) entitlement;
@property (TQ,R,N,V_credentials) credentials;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBServiceClientAuthenticator sharedSystemClientAuthenticator];
+[FBServiceClientAuthenticator _authenticateAuditToken:entitlement:credentials:error:];
+[FBServiceClientAuthenticator _errorForCode:process:failedEntitlement:];
+[FBServiceClientAuthenticator authenticateAuditToken:forEntitlement:error:];
+[FBServiceClientAuthenticator sharedForegroundUIAppClientAuthenticator];
+[FBServiceClientAuthenticator sharedUIAppClientAuthenticator];
```

## Instance methods

```
-[FBServiceClientAuthenticator entitlement];
-[FBServiceClientAuthenticator succinctDescriptionBuilder];
-[FBServiceClientAuthenticator init];
-[FBServiceClientAuthenticator descriptionWithMultilinePrefix:];
-[FBServiceClientAuthenticator succinctDescription];
-[FBServiceClientAuthenticator descriptionBuilderWithMultilinePrefix:];
-[FBServiceClientAuthenticator credentials];
-[FBServiceClientAuthenticator initWithCredentials:];
-[FBServiceClientAuthenticator initWithEntitlement:];
-[FBServiceClientAuthenticator authenticateAuditToken:];
-[FBServiceClientAuthenticator authenticateAuditToken:error:];
-[FBServiceClientAuthenticator authenticateAuditToken:forEntitlement:error:];
-[FBServiceClientAuthenticator authenticateClient:];
-[FBServiceClientAuthenticator authenticateClient:error:];
-[FBServiceClientAuthenticator initWithEntitlement:additionalCredentials:];
```
