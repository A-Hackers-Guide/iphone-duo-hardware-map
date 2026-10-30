# `NWConcrete_nw_protocol_instance`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_protocol_instance`
- 87 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NWConcrete_nw_protocol_definition" parent_definition;
{nw_protocol_stub_s=} protocol;
^v internal_reference;
^{nw_listen_protocol=^{nw_listen_protocol_callbacks}^{nw_protocol}^v^v} listen_handler;
^v destroy_timer;
@"NSObject<OS_nw_endpoint>" endpoint;
@"NSObject<OS_nw_parameters>" parameters;
@"NSObject<OS_nw_protocol_options>" options;
@"NSObject<OS_nw_association>" association;
@"NSObject<OS_xpc_object>" paths_to_establish;
Q flow_sequence_number;
Q reserve_header_size;
Q reserve_footer_size;
Q maximum_content_size;
I protocol_outbound_data_limit;
^v handle;
@"NSObject<OS_nw_context>" context;
{nw_frame_array_s="tqh_first"^{nw_frame}"tqh_last"^^{nw_frame}} inbound_frames;
{nw_frame_array_s="tqh_first"^{nw_frame}"tqh_last"^^{nw_frame}} outbound_frames;
I empty_frame_pool_count;
{nw_frame_array_s="tqh_first"^{nw_frame}"tqh_last"^^{nw_frame}} empty_frame_pool;
{nw_frame_array_s="tqh_first"^{nw_frame}"tqh_last"^^{nw_frame}} pending_inbound_frames;
I pending_inbound_frame_count;
I pending_inbound_frame_bytes;
{nw_frame_array_s="tqh_first"^{nw_frame}"tqh_last"^^{nw_frame}} pending_outbound_frames;
@"NSObject<OS_nw_array>" outbound_data_requests;
[16C] asserted_agent;
^{nw_hash_table=} flows_table;
^{nw_hash_table=} custom_flow_mapping_table;
Q last_accepted_flow;
@"NSObject<OS_nw_protocol_metadata>" new_flow_metadata;
I pending_new_flow_count;
@? wakeup;
@? wakeup_block;
@"NSObject<OS_nw_path_flow_registration>" flow_registration;
@"NSObject<OS_nw_path>" current_path;
^{nw_hash_table=} paths_table;
Q default_path;
Q primary_path;
Q current_setup_path;
@"NSObject<OS_nw_endpoint>" current_setup_path_endpoint;
@"NSObject<OS_nw_endpoint>" current_setup_path_local_endpoint;
@"NSObject<OS_nw_parameters>" current_setup_path_parameters;
@"NSObject<OS_nw_endpoint>" derived_ipv4_endpoint;
@"NSObject<OS_nw_endpoint>" preferred_ipv4_address;
@"NSObject<OS_nw_endpoint>" preferred_ipv6_address;
i level;
^{nw_hash_node=} connecting_node;
Q flow_in_connected;
@"NSObject<OS_nw_protocol_instance_registrar>" registrar;
S paths_log_id_num;
b1 last_probe_connectivity;
b1 initialized;
b1 started;
b1 ready;
b1 connection_used;
b1 output_connected;
b1 limit_outbound_data;
b1 datagram;
b1 reported_send_error;
b1 supports_external_data;
b1 link_flow_controlled;
b1 waiting_for_link_flow_control;
b1 processing_input;
b1 processing_output;
b1 pending_input_finished;
b1 should_signal_outbound_not_pending;
b1 waiting_for_listener_accept;
b1 new_flow_is_control;
b1 prohibit_joining;
b1 should_destroy;
b1 timer_enabled;
b1 input_acknowledged;
b1 reads_suspended;
b1 failed_to_get_output;
b1 needs_output_available;
b1 needs_finalize_output;
b1 wait_for_early_data;
b1 handling_early_data_rejection;
b1 previous_should_fallback;
b1 previous_fallback_is_weak;
b1 previous_fallback_is_preferred;
b1 reporting_all_done;
b1 suppress_logging;
b1 tearing_down;
b1 flushing;
[84c] log_str;
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
-[NWConcrete_nw_protocol_instance init];
-[NWConcrete_nw_protocol_instance destroy];
-[NWConcrete_nw_protocol_instance getProtocolStructure];
```
