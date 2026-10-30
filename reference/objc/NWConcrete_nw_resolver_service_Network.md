# `NWConcrete_nw_resolver_service`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_resolver_service`
- 11 instance variables, 4 properties, 1 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_endpoint>" service_host;
@"NSObject<OS_nw_endpoint>" alternative_origin;
@"NSObject<OS_dnssd_getaddrinfo>" gai;
S priority;
S weight;
S port;
S flags;
@"NSObject<OS_dispatch_data>" ech_config;
b1 sensitive_redacted;
b1 host_matches_origin;
b1 port_matches_origin;
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
-[NWConcrete_nw_resolver_service description];
```
