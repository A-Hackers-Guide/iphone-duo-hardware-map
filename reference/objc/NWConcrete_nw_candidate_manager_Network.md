# `NWConcrete_nw_candidate_manager`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_candidate_manager`
- 26 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
Q log_id;
@"NSObject<OS_nw_endpoint>" ids_endpoint;
@"NSObject<OS_nw_dictionary>" ids_resolve_registrations;
@"NSMutableDictionary" ids_candidates;
@"NSObject<OS_nw_endpoint>" service;
@"NSObject<OS_nw_resolver>" service_resolver;
@"NSObject<OS_nw_resolver>" awdl_service_resolver;
@"NSObject<OS_nw_endpoint>" awdl_endpoint;
@"NSObject<OS_nw_listener>" listener;
@"NSObject<OS_nw_parameters>" parameters;
@"NSMutableDictionary" hostname_resolvers;
^v lost_path_timer;
@"NSObject<OS_nw_endpoint>" original_remote_endpoint;
@? add_eligible_details;
@? remove_eligible_details;
@? modify_ids_parameters;
@"NWConcrete_nw_connection" connection;
@"NWConcrete_nw_connection" monitored_connection;
@"NSObject<OS_nw_array>" candidates;
i state;
@? state_handler;
@? new_connection_handler;
@"NSObject<OS_nw_path_evaluator>" ids_path_evaluator;
b1 currently_using_awdl;
b1 should_connect;
b1 monitor_started;
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
-[NWConcrete_nw_candidate_manager init:];
-[NWConcrete_nw_candidate_manager description];
```
