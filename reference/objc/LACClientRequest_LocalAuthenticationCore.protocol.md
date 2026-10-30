# `LACClientRequest` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `LACRequest`
- 0 instance variables, 4 properties, 4 instance methods, 0 class methods

## Properties

```
@property (T@"<LACXPCClient>",R,N) client;
@property (T@"LACClientInfo",R,N) clientInfo;
@property (T@"NSUUID",R,N) contextID;
@property (TQ,R,N) originatorId;
```

## Instance methods

```
-[LACClientRequest clientInfo];
-[LACClientRequest contextID];
-[LACClientRequest originatorId];
-[LACClientRequest client];
```
