# `NWConcrete_nw_endpoint_fallback`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_endpoint_fallback`
- 25 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
Q fallback_usage_cap;
Q fallback_cap_interval;
Q fallback_timeout_nanos;
@"NWConcrete_nw_endpoint_handler" primary_child;
@"NWConcrete_nw_endpoint_handler" fallback_child;
i result;
@"NSObject<OS_nw_interface>" primary_interface;
@"NSObject<OS_nw_interface>" fallback_interface;
^v fallback_timer;
^v post_transport_timer;
^v usage_cap_timer;
Q fallback_timer_start;
I fallback_disposition;
b1 received_primary_cancelled_error;
b1 weak_fallback;
b1 no_fallback_timer;
b1 fallback_is_forced;
b1 fallback_is_preferred;
b1 fallback_based_on_interface_type;
b1 started_fallback;
b1 primary_child_in_progress;
b1 fallback_child_in_progress;
b1 primary_child_indefinite_failed;
b1 fallback_child_indefinite_failed;
b1 fallback_is_cellular;
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
-[NWConcrete_nw_endpoint_fallback init];
-[NWConcrete_nw_endpoint_fallback dealloc];
-[NWConcrete_nw_endpoint_fallback cancelWithHandler:forced:];
-[NWConcrete_nw_endpoint_fallback updatePathWithHandler:];
-[NWConcrete_nw_endpoint_fallback startWithHandler:];
-[NWConcrete_nw_endpoint_fallback applyWithHandler:toChildren:];
```
