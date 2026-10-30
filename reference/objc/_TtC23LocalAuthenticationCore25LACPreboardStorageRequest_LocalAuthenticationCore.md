# `_TtC23LocalAuthenticationCore25LACPreboardStorageRequest`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACStorageRequest`
- 8 instance variables, 8 properties, 10 instance methods, 0 class methods

## Instance variables

```
Swift.UInt32 identifier;
_$sSi originatorId;
(objc_protocol 0x20683d538) ? client;
_$sSo13LACClientInfoCSg clientInfo;
Foundation.UUID ? contextID;
__C.LACStorageDomain domain;
__C.LACStorageKey key;
_$sSD -> Swift.AnyHashable _$sypGSg options;
```

## Properties

```
@property (TI,N,R,Videntifier) identifier;
@property (Tq,N,R,VoriginatorId) originatorId;
@property (T@"<LACXPCClient>",N,R,Vclient) client;
@property (T@"LACClientInfo",N,&,VclientInfo) clientInfo;
@property (T@"NSUUID",N,R) contextID;
@property (Tq,N,R,Vdomain) domain;
@property (Tq,N,R,Vkey) key;
@property (T@"NSDictionary",N,R) options;
```

## Instance methods

```
-[_TtC23LocalAuthenticationCore25LACPreboardStorageRequest setClientInfo:];
-[_TtC23LocalAuthenticationCore25LACPreboardStorageRequest domain];
-[_TtC23LocalAuthenticationCore25LACPreboardStorageRequest clientInfo];
-[_TtC23LocalAuthenticationCore25LACPreboardStorageRequest identifier];
-[_TtC23LocalAuthenticationCore25LACPreboardStorageRequest init];
-[_TtC23LocalAuthenticationCore25LACPreboardStorageRequest options];
-[_TtC23LocalAuthenticationCore25LACPreboardStorageRequest contextID];
-[_TtC23LocalAuthenticationCore25LACPreboardStorageRequest originatorId];
-[_TtC23LocalAuthenticationCore25LACPreboardStorageRequest client];
-[_TtC23LocalAuthenticationCore25LACPreboardStorageRequest key];
```
