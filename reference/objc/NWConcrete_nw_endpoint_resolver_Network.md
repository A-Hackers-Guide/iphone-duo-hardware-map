# `NWConcrete_nw_endpoint_resolver`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_endpoint_resolver`
- 26 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_resolver>" resolver;
i last_resolver_status;
I next_child_endpoint_index;
b1 transport_finished;
b1 failed_to_start_next_child;
b1 started_desperate_ivan;
b1 waiting_for_desperate_ivan;
b1 resolver_complete_on_connect;
b1 cancel_removed_endpoints;
b1 had_resolved_endpoints;
b1 reported_children_stall;
b2 child_failure_threshold;
b1 started_child_with_path_evaluator;
@"NWConcrete_nw_endpoint_handler" connected_child;
@"NSObject<OS_nw_array>" child_endpoint_handlers;
@"NSObject<OS_nw_array>" failed_child_endpoint_handlers;
^v child_timer;
^v trigger_agent_timer;
^v desperate_ivan_timer;
^v dns_stall_timer;
@"NSObject<OS_nw_dictionary>" resolve_flow_registrations;
@"NSObject<OS_nw_array>" path_resolved_endpoints;
@"NSObject<OS_nw_array>" resolver_resolved_endpoints;
@"NSObject<OS_nw_endpoint>" modified_endpoint;
@"NSObject<OS_xpc_object>" asserted_agent_uuids;
@"NSObject<OS_xpc_object>" resolver_complete_on_connect_agent_uuids;
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
-[NWConcrete_nw_endpoint_resolver init];
-[NWConcrete_nw_endpoint_resolver dealloc];
-[NWConcrete_nw_endpoint_resolver cancelWithHandler:forced:];
-[NWConcrete_nw_endpoint_resolver updatePathWithHandler:];
-[NWConcrete_nw_endpoint_resolver startWithHandler:];
-[NWConcrete_nw_endpoint_resolver applyWithHandler:toChildren:];
```
