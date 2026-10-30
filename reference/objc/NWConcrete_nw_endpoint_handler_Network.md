# `NWConcrete_nw_endpoint_handler`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NWDeallocOnQueueObject`
- Protocols: `OS_nw_endpoint_handler`
- 33 instance variables, 0 properties, 2 instance methods, 1 class methods

## Instance variables

```
^? report_callback;
@"NSObject<OS_nw_object>" callback_context;
@"NSObject<OS_nw_endpoint>" endpoint;
@"NSObject<OS_nw_parameters>" parameters;
@"NSObject<OS_nw_context>" context;
@? migration_callback;
@"NSObject<OS_nw_association>" association;
@"NSObject<OS_nw_path>" current_path;
@"NWConcrete_nw_endpoint_handler" parent_handler;
{nw_endpoint_handler_event_s="domain"S"event"S} event;
@"NSObject<OS_xpc_object>" inactive_agent_uuids;
@"NSObject<OS_nw_path>" inactive_agent_path;
@"NSObject<OS_xpc_object>" triggered_agent_uuids;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} lock;
i mode;
i state;
Q start_time;
^v fallback_timer;
I top_id;
[16C] connection_uuid;
{atomic<unsigned int>="__a_"{__cxx_atomic_impl<unsigned int, std::__cxx_atomic_base_impl<unsigned int>>="__a_value"AI}} last_child_id;
[16C] id_chain;
[75c] id_str;
@"NSObject<NWConcrete_nw_endpoint_mode_handler>" mode_handler;
@"NSObject<OS_nw_path_evaluator>" override_evaluator;
i privacy_stance;
b1 dry_run;
b1 triggering_voluntary_agents;
b1 reuse_association;
b1 has_better_path;
b1 has_finished_transport;
b1 minimize_logging;
b1 logging_disabled;
```

## Class methods

```
+[NWConcrete_nw_endpoint_handler initialize];
```

## Instance methods

```
-[NWConcrete_nw_endpoint_handler dealloc];
-[NWConcrete_nw_endpoint_handler copyContext];
```
