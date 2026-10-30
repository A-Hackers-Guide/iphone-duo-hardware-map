# `NWConcrete_nw_masque_listener_pair`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_masque_listener_pair`
- 23 instance variables, 4 properties, 1 instance methods, 0 class methods

## Instance variables

```
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} mlp_lock;
@"NWConcrete_nw_masque_connection" mlp_parent;
@"NSObject<OS_nw_connection_group>" mlp_outer_connection_group;
@? mlp_state_changed_handler;
@"NSObject<OS_nw_dictionary>" mlp_client_demux_options;
@"NWConcrete_nw_connection" mlp_inner_direct_send_connection;
@"NSObject<OS_nw_array>" mlp_inner_direct_receive_connections;
[17c] mlp_key;
B mlp_sent_response;
B mlp_closed;
B mlp_exclude_proxy_status;
B mlp_uses_capsules;
@"NSObject<OS_nw_endpoint>" mlp_client_endpoint;
@"NSObject<OS_dispatch_group>" mlp_close_group;
I mlp_traffic_class;
i mlp_require_interface;
B mlp_prohibit_constrained;
B mlp_prohibit_expensive;
B mlp_prohibit_wifi;
B mlp_prohibit_cellular;
B mlp_prohibit_wired;
@"NSString" mlp_src_bundle_id;
@"NSString" mlp_listener_association;
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
-[NWConcrete_nw_masque_listener_pair dealloc];
```
