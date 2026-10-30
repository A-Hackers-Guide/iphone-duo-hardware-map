# `NWConcrete_nw_endpoint_transform`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_endpoint_transform`
- 18 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_array>" child_endpoint_handlers;
@"NSObject<OS_nw_array>" failed_child_endpoint_handlers;
@"NSObject<OS_xpc_object>" fallback_modes;
@"NSObject<OS_nw_array>" blocked_protocols;
I next_child_endpoint_index;
@"NWConcrete_nw_endpoint_handler" connected_child;
@"NSObject<OS_nw_endpoint>" primary_endpoint;
^v child_timer;
Q last_timeout_ms;
I first_protocol;
I connected_protocol;
I connected_protocol_index;
B quic_deferred;
B quic_application_deferred;
B quic_denied;
B quic_alternative_present;
B quic_updated_alternative;
B quic_speculative_attempt;
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
-[NWConcrete_nw_endpoint_transform init];
-[NWConcrete_nw_endpoint_transform dealloc];
-[NWConcrete_nw_endpoint_transform cancelWithHandler:forced:];
-[NWConcrete_nw_endpoint_transform updatePathWithHandler:];
-[NWConcrete_nw_endpoint_transform startWithHandler:];
-[NWConcrete_nw_endpoint_transform applyWithHandler:toChildren:];
```
