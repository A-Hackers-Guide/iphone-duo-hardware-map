# `NWConcrete_tcp_connection`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_tcp_connection`
- 41 instance variables, 4 properties, 1 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_xpc_object>" tc_context;
@"NSObject<OS_nw_connection>" tc_nwconn;
@"NSObject<OS_nw_error>" tc_last_nw_error;
@"NSObject<OS_nw_path>" tc_nw_current_path;
@"NSObject<OS_nw_endpoint>" tc_network_endpoint;
@"NSObject<OS_nw_parameters>" tc_network_parameters;
@"NSObject<OS_dispatch_queue>" tc_client_queue;
@? tc_event;
@? tc_cancel_handler;
@"NSObject<OS_dispatch_source>" tc_connection_attempt_timer;
@"NWConcrete_tcp_connection" tc_internally_retained_object;
Q tc_id;
Q tc_attempt_timeout_nanos;
i tc_error;
i tc_dup_fd;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} tc_lock;
i tc_usage_model;
q tc_quality;
I tc_keepalive_count;
I tc_keepalive_interval;
I tc_adaptive_read_count;
I tc_adaptive_write_count;
I tc_minimum_throughput;
C tc_state;
C tc_by;
b1 tc_event_read_close_delivered;
b1 tc_event_write_close_delivered;
b1 tc_event_connected_delivered;
b1 tc_event_disconnected_delivered;
b1 tc_better_route;
b1 tc_not_viable;
b1 tc_attempt_timeout_should_generate_event;
b1 tc_allow_socket_access;
b1 tc_sent_connected;
b1 tc_sent_tls_finished;
b1 tc_state_has_been_preparing;
b1 tc_client_owns_dup_fd;
b1 tc_started;
b1 tc_keepalive_events;
b1 tc_adaptive_read_events;
b1 tc_adaptive_write_events;
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
-[NWConcrete_tcp_connection dealloc];
```
