# `NWConcrete_nw_masque_connection_pair`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_masque_connection_pair`
- 54 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} mcp_lock;
@"NWConcrete_nw_masque_connection" mcp_parent;
@"NWConcrete_nw_connection" mcp_inner_server_cid_connection;
@"NWConcrete_nw_connection" mcp_inner_direct_send_connection;
@"NSObject<OS_nw_array>" mcp_inner_direct_receive_connections;
@"NWConcrete_nw_connection" mcp_outer_connection;
@"NSObject<OS_nw_content_context>" mcp_inner_response_context;
@? mcp_state_changed_handler;
S mcp_client_cid_length;
[20C] mcp_client_cid;
S mcp_virtual_client_cid_length;
[20C] mcp_virtual_client_cid;
[20c] mcp_client_cid_header;
S mcp_server_cid_length;
[20C] mcp_server_cid;
[20c] mcp_server_cid_header;
[8c] mcp_datagram_flow_id;
@"NSObject<OS_nw_protocol_options>" mcp_client_demux_options;
[17c] mcp_key;
B mcp_sent_response;
B mcp_closed;
B mcp_is_datagram;
B mcp_exclude_proxy_status;
B mcp_uses_capsules;
@"NSObject<OS_nw_endpoint>" mcp_client_endpoint;
@"NSObject<OS_dispatch_group>" mcp_close_group;
@"NSObject<OS_sec_identity>" mcp_reverse_proxy_identity;
B mcp_reverse_proxying;
I mcp_traffic_class;
i mcp_require_interface;
i mcp_multipath_service;
S mcp_multipath_alt_port;
B mcp_prohibit_constrained;
B mcp_prohibit_expensive;
B mcp_prohibit_wifi;
B mcp_prohibit_cellular;
B mcp_prohibit_wired;
B mcp_out_connection_failed_or_sent_write_close;
B mcp_ready;
B mcp_cancelled;
@"NSString" mcp_src_bundle_id;
S mcp_local_port;
@"NSObject<OS_dispatch_source>" mcp_waiting_timer_source;
@"NSObject<OS_dispatch_source>" mcp_teardown_timer_source;
Q mcp_total_received_inner_bytes;
Q mcp_total_sent_inner_bytes;
Q mcp_total_received_direct_inner_bytes;
Q mcp_total_sent_direct_inner_bytes;
Q mcp_total_received_outer_bytes;
Q mcp_total_sent_outer_bytes;
Q mcp_busy_counter;
Q mcp_busy_start_time_nanos;
Q mcp_total_busy_time_nanos;
B mcp_decremented_for_connecting;
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
-[NWConcrete_nw_masque_connection_pair dealloc];
-[NWConcrete_nw_masque_connection_pair description];
```
