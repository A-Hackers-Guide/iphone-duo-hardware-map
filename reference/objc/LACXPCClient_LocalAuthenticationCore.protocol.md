# `LACXPCClient` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 7 instance methods, 0 class methods

## Properties

```
@property (TI,R,N) userId;
@property (Ti,R,N) processId;
@property (Ti,R,N) auditSessionId;
@property (T{?=[8I]},R,N) auditToken;
@property (T@"NSString",R,N) signingID;
@property (TB,R,N) isFirstPartyClient;
```

## Instance methods

```
-[LACXPCClient processId];
-[LACXPCClient checkEntitlement:];
-[LACXPCClient auditSessionId];
-[LACXPCClient auditToken];
-[LACXPCClient isFirstPartyClient];
-[LACXPCClient userId];
-[LACXPCClient signingID];
```
