# `NWConcrete_nw_proxy_config`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_proxy_config`
- 39 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_dictionary>" stacks;
@"NSObject<OS_xpc_object>" proxied_transports;
@"NSObject<OS_xpc_object>" required_protocols;
@"NSObject<OS_xpc_object>" remove_protocols;
@"NSObject<OS_nw_endpoint>" endpoint;
@"NSObject<OS_nw_array>" resolved_endpoints;
[16C] identifier;
[16C] fallback_agent_uuid;
@"NWConcrete_nw_proxy_config" fallback_config;
@"NSObject<OS_nw_agent>" agent;
@"NSObject<OS_nw_authentication_credential>" credential;
@"NSObject<OS_xpc_object>" pac_script;
@"NSObject<OS_xpc_object>" match_domains;
@"NSObject<OS_xpc_object>" excluded_domains;
@"NSObject<OS_xpc_object>" preferred_domains;
@"NSObject<OS_xpc_object>" alternate_agents;
i mode;
i type;
i multipath_service;
I generation;
S config_epoch;
b1 is_privacy_proxy;
b1 privacy_proxy_fail_open;
b1 ignore_privacy_stance;
b1 prohibit_direct;
b1 supports_bonjour;
b1 match_address_family;
b1 prohibit_unsatisfied_paths;
b1 exclude_simple_hostnames;
b1 force_tfo;
b1 force_multipath;
b1 apply_tfo;
b1 disable_tfo_cookie;
b1 override_opaque_https;
b1 is_fallback;
b1 use_fast_fallback;
b1 use_over_privacy_proxy;
b1 require_domain_match;
b1 is_companion_proxy;
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
-[NWConcrete_nw_proxy_config init];
-[NWConcrete_nw_proxy_config dealloc];
-[NWConcrete_nw_proxy_config description];
```
