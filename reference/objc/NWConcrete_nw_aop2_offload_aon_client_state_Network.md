# `NWConcrete_nw_aop2_offload_aon_client_state`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_aop2_offload_aon_client_state`
- 5 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
{nw_aop2_offload_aon_net_client="tb_client_name"[128c]"tb_server_name"[128c]"shm_tx_name"[128c]"shm_rx_name"[128c]"config_key"[512c]"client"^{aon_net_client}"service_callback"{?="connected"@?"disconnected"@?"rx_buffers_available"@?"tx_buffers_available"@?"connected_with_metadata"@?"disconnected_with_error"@?"notify"@?"rx_buffers_available_with_wake"@?"transport_connected"@?}"tx_buffer_size"Q"rx_buffer_size"Q"ring_id_bitmap"Q"__pad"[0C]} aon_client;
^{nw_hash_table=} contexts;
^v cleanup_timer;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} lock;
B detaching;
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
-[NWConcrete_nw_aop2_offload_aon_client_state init];
-[NWConcrete_nw_aop2_offload_aon_client_state dealloc];
```
