# `NWConcrete_nw_protocol_establishment_report`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_protocol_establishment_report`
- 7 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
Q handshake_milliseconds;
Q handshake_rtt_milliseconds;
i client_accurate_ecn_state;
i server_accurate_ecn_state;
@"NSObject<OS_nw_protocol_definition>" protocol;
b1 l4s_enabled;
b1 quic_migration_supported;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NWConcrete_nw_protocol_establishment_report init];
-[NWConcrete_nw_protocol_establishment_report dealloc];
```
