# `NWConcrete_nw_socks5_server`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_socks5_server`
- 20 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
Q ss_id;
@"NWConcrete_nw_socks5_server" ss_internally_retained_object;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} ss_lock;
@"NSObject<OS_dispatch_queue>" ss_queue;
@"NSObject<OS_nw_parameters>" ss_parameters;
@"NSObject<OS_dispatch_queue>" ss_client_queue;
@? ss_state_handler;
@? ss_error;
@"NSObject<OS_nw_listener>" ss_listener;
@"NSObject<OS_nw_array>" ss_socks5_connections;
@"NSObject<OS_nw_dictionary>" ss_socks5_udp_associate_connections;
@? outer_connection_handler;
{nw_shoes_statistics="ss_max_simultaneous_connections"I"ss_total_connections"I} ss_stats;
Q ss_assertion_toggle_mach_time;
@"NSObject<OS_dispatch_source>" ss_assertion_timer;
I ss_assertion;
I ss_busy_count;
b1 ss_shoes;
b1 ss_assertion_timer_running;
b1 ss_cancelled;
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
-[NWConcrete_nw_socks5_server dealloc];
-[NWConcrete_nw_socks5_server description];
```
