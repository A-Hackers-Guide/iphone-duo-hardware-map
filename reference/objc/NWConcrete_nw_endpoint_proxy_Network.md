# `NWConcrete_nw_endpoint_proxy`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_endpoint_proxy`
- 33 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_array>" child_endpoint_handlers;
@"NSObject<OS_nw_array>" failed_child_endpoint_handlers;
I next_child_endpoint_index;
@"NWConcrete_nw_endpoint_handler" connected_child;
@"NSObject<OS_nw_array>" custom_proxy_configs;
@"NSObject<OS_nw_array>" path_proxy_configs;
@"NSObject<OS_nw_array>" parsed_proxy_configs;
^{__CFURL=} url;
@"NSObject<OS_nw_array>" pac_resolvers;
@"NSObject<OS_nw_error>" child_error;
^v child_timer;
b1 has_privacy_proxy;
b1 privacy_proxy_fail_closed;
b1 privacy_proxy_strict_fail_closed;
b1 privacy_proxy_fail_closed_for_unreachable_hosts;
b1 allow_non_privacy_proxy_children;
b1 privacy_proxy_detected_unreachable_host;
b1 direct_prohibited;
b1 synthesized_url;
b1 pac_failed_missing_url;
b1 overrode_to_https;
b1 has_pac;
b1 transport_finished;
b1 proxy_flow_finished;
b1 is_known_tracker;
b1 is_custom_proxy;
b1 is_pac_connection;
b1 is_http_scheme;
b1 is_https_scheme;
C stats_result;
b1 proxy_race_timeout;
b1 proxy_failed;
b1 proxy_finished_transport;
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
-[NWConcrete_nw_endpoint_proxy init];
-[NWConcrete_nw_endpoint_proxy dealloc];
-[NWConcrete_nw_endpoint_proxy cancelWithHandler:forced:];
-[NWConcrete_nw_endpoint_proxy updatePathWithHandler:];
-[NWConcrete_nw_endpoint_proxy startWithHandler:];
-[NWConcrete_nw_endpoint_proxy applyWithHandler:toChildren:];
```
