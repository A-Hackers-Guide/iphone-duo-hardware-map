# `LACXPCClient`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACXPCClient`
- 6 instance variables, 13 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _bypassEntitlement;
i _auditSessionId;
i _processId;
I _userId;
@"LACAuditToken" _token;
@"NSXPCConnection" _connection;
```

## Properties

```
@property (TB,N,V_bypassEntitlement) bypassEntitlement;
@property (Ti,N,V_auditSessionId) auditSessionId;
@property (T@"LACAuditToken",&,N,V_token) token;
@property (Ti,N,V_processId) processId;
@property (TI,N,V_userId) userId;
@property (T@"NSXPCConnection",W,N,V_connection) connection;
@property (T{?=[8I]},R,N) auditToken;
@property (T@"NSString",R,N) signingID;
@property (TB,R,N) isFirstPartyClient;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACXPCClient setProcessId:];
-[LACXPCClient processId];
-[LACXPCClient setBypassEntitlement:];
-[LACXPCClient initWithConnection:];
-[LACXPCClient checkEntitlement:];
-[LACXPCClient bypassEntitlement];
-[LACXPCClient auditSessionId];
-[LACXPCClient connection];
-[LACXPCClient setConnection:];
-[LACXPCClient description];
-[LACXPCClient auditToken];
-[LACXPCClient token];
-[LACXPCClient setUserId:];
-[LACXPCClient setToken:];
-[LACXPCClient setAuditSessionId:];
-[LACXPCClient isFirstPartyClient];
-[LACXPCClient userId];
-[LACXPCClient signingID];
```
