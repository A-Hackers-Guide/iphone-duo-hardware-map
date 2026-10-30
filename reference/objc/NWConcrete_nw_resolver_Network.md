# `NWConcrete_nw_resolver`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_resolver`
- 64 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
i status;
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
@"NSObject<OS_nw_parameters>" parameters;
@"NSObject<OS_nw_endpoint>" endpoint;
@"NSObject<OS_nw_context>" context;
@"NSObject<OS_dispatch_group>" cancel_group;
@"NSObject<OS_dnssd_getaddrinfo>" gai;
I dns_service_id;
^{_DNSServiceRef_t=} dns_service;
^{_DNSServiceRef_t=} dns_service_secondary_pointer;
I forced_protocol;
i dns_error;
S flags;
@? update_block;
@? cancel_handler;
@"NSObject<OS_dispatch_queue>" client_queue;
@"NSObject<OS_nw_browser>" awdl_trigger_browser;
@"NSObject<OS_nw_path_evaluator>" evaluator;
@"NSObject<OS_nw_path>" host_path;
@"NSObject<OS_nw_array>" flow_array;
^v query_timer;
^v delayed_reporting_timer;
@"NSObject<OS_nw_array>" endpoint_array;
@"NSObject<OS_nw_array>" non_preferred_endpoint_array;
^v non_preferred_timer;
@? alternative_handler;
@"NSObject<OS_nw_array>" services;
@"NSObject<OS_nw_array>" alternative_endpoints;
@"NSObject<OS_nw_array>" alternative_protocols;
@"NSObject<OS_nw_path>" path;
@"NSObject<OS_nw_interface>" path_required_interface;
@"NWConcrete_nw_resolver" internally_retained_object;
* extended_dns_error_extra_text;
[16C] selected_resolver_config;
i result_protocol;
i result_provider;
[84c] log_str;
I unique_id;
Q network_resolution_start_time;
Q network_resolution_a_end_time;
Q network_resolution_aaaa_end_time;
Q network_resolution_svcb_end_time;
S extended_dns_error_code;
b1 is_custom_resolver;
b1 used_local_cache;
b1 ipv4_used_resolver_cache;
b1 ipv6_used_resolver_cache;
b1 local_only;
b1 suppress_logging;
b1 has_ipv4;
b1 has_ipv6;
b1 has_nat64_prefixes;
b1 svcb_requested;
b1 svcb_received;
b1 svcb_dohuri;
b1 ech_received;
b1 is_standalone;
b1 has_oblivious_config;
b1 allow_encrypted_dns_name_resolution_failover;
b1 config_allows_failover;
b1 config_fell_back;
b1 has_completed_preferred_weighting;
b1 use_persistent_cache;
b1 use_agent_resolver;
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
-[NWConcrete_nw_resolver dealloc];
-[NWConcrete_nw_resolver redactedDescription];
-[NWConcrete_nw_resolver description];
```
