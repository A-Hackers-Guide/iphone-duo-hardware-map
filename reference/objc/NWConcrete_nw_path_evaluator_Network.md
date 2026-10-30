# `NWConcrete_nw_path_evaluator`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_path_evaluator`
- 21 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_parameters>" parameters;
@"NSObject<OS_nw_endpoint>" endpoint;
@"NSObject<OS_nw_group_descriptor>" group_descriptor;
@"NSObject<OS_nw_browse_descriptor>" browse_descriptor;
@"NSObject<OS_nw_advertise_descriptor>" advertise_descriptor;
@"NWConcrete_nw_path" path;
@"NSObject<OS_dispatch_queue>" client_queue;
@? update_block;
@? cancel_handler;
[16C] client_id;
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
I flow_count;
S custom_ethertype;
C custom_ip_protocol;
b1 is_default;
b1 is_listener;
b1 is_interpose;
b1 is_custom_ether;
b1 started;
b1 cancelled;
b1 logging;
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
-[NWConcrete_nw_path_evaluator init];
-[NWConcrete_nw_path_evaluator dealloc];
-[NWConcrete_nw_path_evaluator redactedDescription];
-[NWConcrete_nw_path_evaluator description];
```
