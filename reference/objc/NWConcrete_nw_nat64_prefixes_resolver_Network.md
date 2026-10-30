# `NWConcrete_nw_nat64_prefixes_resolver`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_nat64_prefixes_resolver`
- 14 instance variables, 4 properties, 1 instance methods, 0 class methods

## Instance variables

```
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
I ifindex;
@"NSObject<OS_nw_parameters>" parameters;
@"NSObject<OS_nw_context>" context;
@"NWConcrete_nw_nat64_prefixes_resolver" internally_retained_object;
I dns_service_id;
^{_DNSServiceRef_t=} dns_service;
i dns_error;
@? update_handler;
@? cancel_handler;
@"NSObject<OS_dispatch_queue>" client_queue;
^{in6_addr=(?=[16C][8S][4I])} ipv6_addrs;
@"NSObject<OS_nw_path_evaluator>" evaluator;
i address_count;
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
-[NWConcrete_nw_nat64_prefixes_resolver dealloc];
```
