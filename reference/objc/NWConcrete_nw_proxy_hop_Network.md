# `NWConcrete_nw_proxy_hop`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_proxy_hop`
- 26 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
[16C] resumable_session_agent;
@"NSObject<OS_nw_endpoint>" endpoint;
@"NSObject<OS_nw_endpoint>" fallback_endpoint;
@"NSObject<OS_nw_protocol_options>" options;
@"NSObject<OS_nw_protocol_options>" tls_options;
^{__CFArray=} raw_public_keys;
^{__CFData=} client_identity_persistent_reference;
^{__CFArray=} client_certificates;
I idle_timeout_ms;
b1 supports_raw_ip;
b1 supports_resumption;
b1 supports_l4s;
b1 enable_multipath;
b1 trust_certs;
b1 fallback_only;
b1 supports_udp_listen;
b1 use_x25519;
b1 enable_demux;
b1 supports_udp_proxying_over_http2;
b1 client_identity_is_raw_public_key;
b1 use_pqtls;
b1 allow_redirects;
b1 disable_idle_timeout;
b1 disable_keepalives;
b1 ignore_path_errors;
b1 migration_for_non_transport;
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
-[NWConcrete_nw_proxy_hop init];
-[NWConcrete_nw_proxy_hop dealloc];
```
