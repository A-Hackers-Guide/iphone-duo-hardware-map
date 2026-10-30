# `NWConcrete_nw_masque_connection`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_masque_connection`
- 17 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
Q mc_id;
Q mc_group_id;
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} mc_lock;
@"NSObject<OS_dispatch_queue>" mc_queue;
@"NSObject<OS_nw_masque_server>" mc_parent;
@"NWConcrete_nw_connection" mc_in_connection;
@"NSObject<OS_nw_dictionary>" mc_connection_pairs;
@"NSObject<OS_nw_dictionary>" mc_listener_pairs;
@"NSObject<OS_sec_identity>" mc_reverse_proxy_identity;
@"NSObject<OS_nw_interface>" mc_outbound_interface;
@? mc_outer_connection_handler;
B mc_drop_requests;
B mc_sent_secondary_certificate;
B mc_in_connection_failed_or_sent_write_close;
@? mc_cancel;
C mc_state;
@"NSObject<OS_nw_error>" mc_error;
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
-[NWConcrete_nw_masque_connection dealloc];
-[NWConcrete_nw_masque_connection description];
```
