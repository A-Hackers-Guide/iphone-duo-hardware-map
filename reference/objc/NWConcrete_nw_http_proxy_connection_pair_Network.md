# `NWConcrete_nw_http_proxy_connection_pair`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_http_proxy_connection_pair`
- 8 instance variables, 4 properties, 1 instance methods, 0 class methods

## Instance variables

```
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
@"NSObject<OS_dispatch_queue>" queue;
@"NSObject<OS_dispatch_queue>" client_queue;
@"NSObject<OS_nw_connection>" inbound_connection;
@"NSObject<OS_nw_connection>" outbound_connection;
@? state_changed_handler;
@? outbound_connection_handler;
B setup;
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
-[NWConcrete_nw_http_proxy_connection_pair dealloc];
```
