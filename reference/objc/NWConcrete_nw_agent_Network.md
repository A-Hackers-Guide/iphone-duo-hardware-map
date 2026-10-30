# `NWConcrete_nw_agent`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_agent`
- 52 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
I logging_id;
AI last_client_id;
[32c] domain;
[32c] type;
[128c] description;
@"NSObject<OS_dispatch_queue>" queue;
@"NSObject<OS_dispatch_data>" data;
i state;
i options;
@"NSObject<OS_nw_context>" context;
@"NSObject<OS_nw_nexus>" nexus;
i flow_protocol_level;
i flow_endpoint_type;
Q tx_slots;
Q rx_slots;
Q slot_size;
[15i] flow_request_types;
C flow_request_type_count;
[15{nw_agent_resolve_handlers="resolve_from_type"i"resolve_to_type"i"start_resolve_handler"@?"stop_resolve_handler"@?}] resolve_handlers;
C resolve_handler_count;
I token_low_water;
[16C] uuid;
@"NSObject<OS_nw_dictionary>" clients;
@"NSObject<OS_nw_dictionary>" channels;
@"NSObject<OS_nw_dictionary>" contexts;
@? activate_handler;
@? assert_handler;
@? unassert_handler;
@? start_flow_handler;
@? start_flow_handler_extended;
@? start_flow_handler_with_result;
@? stop_flow_handler;
@? start_browse_handler;
@? start_filterable_browse_handler;
@? stop_browse_handler;
@? add_members_handler;
@? remove_members_handler;
@? tokens_needed_handler;
@? error_handler;
@"NSObject<OS_nw_fd_wrapper>" fd_wrapper;
@"NSObject<OS_dispatch_source>" event_source;
i resolve_flags;
b1 registered;
b1 supports_listen;
b1 require_assert;
b1 nexus_agent;
b1 browse_agent;
b1 resolve_agent;
b1 group_agent;
b1 do_not_coalesce_flow;
b1 open_flow_on_behalf_of_client;
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
-[NWConcrete_nw_agent init];
-[NWConcrete_nw_agent dealloc];
```
