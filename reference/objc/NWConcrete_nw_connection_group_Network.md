# `NWConcrete_nw_connection_group`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_connection_group`
- 34 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" client_queue;
I client_qos_class;
@"NWConcrete_nw_connection_group" internally_retained_object;
@? state_changed_handler;
i state;
@"NSObject<OS_nw_error>" last_error;
@"NSObject<OS_nw_parameters>" parameters;
@"NSObject<OS_nw_group_descriptor>" group_descriptor;
@"NSObject<OS_nw_path_evaluator>" group_evaluator;
@? membership_change_handler;
@? has_completed_any_connection_handler;
@"NSObject<OS_nw_listener>" listener;
@"NSObject<OS_nw_listener>" unicast_listener;
@"NSObject<OS_nw_array>" connections;
@"NSObject<OS_nw_array>" send_requests;
[16C] group_uuid;
@? receive_handler;
@? new_connection_handler;
* description;
* redacted_description;
I log_id;
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
I maximum_message_size;
I connection_limit;
I new_connection_limit;
S initial_port;
b1 started;
b1 reject_oversized_messages;
b1 is_server;
b1 has_listener_started;
b1 is_listener_ready;
b1 is_unicast_listener_ready;
b1 is_first_connection_ready;
b1 has_user_cancelled;
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
-[NWConcrete_nw_connection_group dealloc];
-[NWConcrete_nw_connection_group redactedDescription];
-[NWConcrete_nw_connection_group description];
```
