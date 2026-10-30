# `NWConcrete_nw_masque_server`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_masque_server`
- 25 instance variables, 4 properties, 1 instance methods, 0 class methods

## Instance variables

```
Q ms_id;
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} ms_lock;
@"NSObject<OS_dispatch_queue>" ms_queue;
@"NSObject<OS_nw_parameters>" ms_parameters;
@"NSObject<OS_dispatch_queue>" ms_client_queue;
@? ms_state_handler;
@? ms_error;
@"NSObject<OS_nw_listener>" ms_listener;
@"NSObject<OS_nw_array>" ms_groups;
@"NSObject<OS_nw_protocol_options>" ms_options;
@? ms_proxy_client_connection_event_handler;
@? ms_outer_connection_handler;
@"NSObject<OS_nw_array>" ms_connections;
@"NSObject<OS_nw_interface>" ms_outbound_interface;
@"NSObject<OS_xpc_object>" ms_listener_associations_dictionary;
@"NSObject<OS_sec_protocol_options>" ms_sec_options;
@"NSObject<OS_sec_identity>" ms_reverse_proxy_identity;
B ms_exclude_proxy_status;
B ms_sent_secondary_certificate;
B ms_cancelled;
Q ms_assertion_toggle_mach_time;
@"NSObject<OS_dispatch_source>" ms_assertion_timer;
I ms_assertion;
I ms_busy_count;
b1 ms_assertion_timer_running;
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
-[NWConcrete_nw_masque_server description];
```
