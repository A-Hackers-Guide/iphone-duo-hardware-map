# `LACDTOMutableKVStoreWriteRequest`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOKVStoreWriteRequest`
- 5 instance variables, 9 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _bypassEntitlements;
q _key;
@"LACDTOKVStoreValue" _value;
@"NSXPCConnection" _connection;
@"NSUUID" _contextUUID;
```

## Properties

```
@property (Tq,N,V_key) key;
@property (T@"LACDTOKVStoreValue",&,N,V_value) value;
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (T@"NSUUID",&,N,V_contextUUID) contextUUID;
@property (TB,N,V_bypassEntitlements) bypassEntitlements;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACDTOMutableKVStoreWriteRequest value];
-[LACDTOMutableKVStoreWriteRequest setKey:];
-[LACDTOMutableKVStoreWriteRequest setValue:];
-[LACDTOMutableKVStoreWriteRequest connection];
-[LACDTOMutableKVStoreWriteRequest setConnection:];
-[LACDTOMutableKVStoreWriteRequest description];
-[LACDTOMutableKVStoreWriteRequest isEqual:];
-[LACDTOMutableKVStoreWriteRequest key];
-[LACDTOMutableKVStoreWriteRequest initWithKey:value:];
-[LACDTOMutableKVStoreWriteRequest contextUUID];
-[LACDTOMutableKVStoreWriteRequest setContextUUID:];
-[LACDTOMutableKVStoreWriteRequest bypassEntitlements];
-[LACDTOMutableKVStoreWriteRequest setBypassEntitlements:];
```
