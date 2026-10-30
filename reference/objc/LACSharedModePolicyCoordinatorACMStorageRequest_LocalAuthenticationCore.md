# `LACSharedModePolicyCoordinatorACMStorageRequest`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACStorageRequest`
- 7 instance variables, 13 properties, 16 instance methods, 0 class methods

## Instance variables

```
I _identifier;
@"NSData" _value;
q _key;
@"<LACXPCClient>" _client;
@"NSUUID" _contextID;
q _domain;
@"NSDictionary" _options;
```

## Properties

```
@property (TI,N,V_identifier) identifier;
@property (Tq,N,V_key) key;
@property (T@"<LACXPCClient>",&,N,V_client) client;
@property (T@"NSUUID",&,N,V_contextID) contextID;
@property (Tq,N,V_domain) domain;
@property (T@"NSData",&,N,V_value) value;
@property (T@"NSDictionary",&,N,V_options) options;
@property (T@"LACClientInfo",R,N) clientInfo;
@property (TQ,R,N) originatorId;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACSharedModePolicyCoordinatorACMStorageRequest setDomain:];
-[LACSharedModePolicyCoordinatorACMStorageRequest domain];
-[LACSharedModePolicyCoordinatorACMStorageRequest setOptions:];
-[LACSharedModePolicyCoordinatorACMStorageRequest identifier];
-[LACSharedModePolicyCoordinatorACMStorageRequest setContextID:];
-[LACSharedModePolicyCoordinatorACMStorageRequest value];
-[LACSharedModePolicyCoordinatorACMStorageRequest setClient:];
-[LACSharedModePolicyCoordinatorACMStorageRequest setKey:];
-[LACSharedModePolicyCoordinatorACMStorageRequest setIdentifier:];
-[LACSharedModePolicyCoordinatorACMStorageRequest setValue:];
-[LACSharedModePolicyCoordinatorACMStorageRequest options];
-[LACSharedModePolicyCoordinatorACMStorageRequest contextID];
-[LACSharedModePolicyCoordinatorACMStorageRequest isEqual:];
-[LACSharedModePolicyCoordinatorACMStorageRequest client];
-[LACSharedModePolicyCoordinatorACMStorageRequest key];
-[LACSharedModePolicyCoordinatorACMStorageRequest initWithKey:boolValue:];
```
