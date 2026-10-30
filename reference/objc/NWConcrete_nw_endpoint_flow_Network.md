# `NWConcrete_nw_endpoint_flow`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_endpoint_flow`
- 94 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_path>" connected_path;
@"NSObject<OS_nw_path>" flow_path;
@"NWConcrete_nw_endpoint_flow" internally_retained_object;
b1 is_root_flow_handler;
b1 is_leaf_flow_handler;
b1 is_empty_root;
b1 initialized_protocol_callbacks;
b1 started;
b1 rebuild_stack;
b1 setup_protocols;
b1 started_protocols;
b1 did_join_protocols;
b1 is_viable;
b1 is_connected;
b1 has_connected;
b1 initial_payload_sent;
b1 assigned_initial_writes;
b1 is_channel;
b1 is_multipath;
b1 multipath_nat64_query_outstanding;
b1 custom_protocols_only;
b1 is_flow_divert;
b1 multilayer_packet_logging;
b1 has_progress_target;
b1 path_is_direct;
b1 should_ignore_path_result;
b1 reported_do_not_reuse;
b1 in_setup_protocols;
b1 connected_child_handles_requests;
b1 connected_child_failed;
b1 should_start_child;
b1 delay_start_child;
b1 did_add_proxy;
b1 guard_fd;
b1 defer_fail;
b1 path_changed_since_last_error;
b1 failing;
b1 reported_stall;
@"NWConcrete_nw_endpoint_flow" clone_from_flow;
{nw_protocol_identifier="name"[32c]"level"i"mapping"i} protocol_identifier;
{nw_protocol_callbacks="add_input_handler"^?"remove_input_handler"^?"replace_input_handler"^?"connect"^?"disconnect"^?"connected"^?"disconnected"^?"error"^?"input_available"^?"output_available"^?"get_input_frames"^?"get_output_frames"^?"finalize_output_frames"^?"link_state"^?"get_parameters"^?"get_path"^?"get_local_endpoint"^?"get_remote_endpoint"^?"register_notification"^?"unregister_notification"^?"notify"^?"updated_path"^?"supports_external_data"^?"input_finished"^?"output_finished"^?"get_output_local_endpoint"^?"get_output_interface"^?"waiting_for_output"^?"copy_info"^?"add_listen_handler"^?"remove_listen_handler"^?"get_message_properties"^?"reset"^?"input_flush"^?"log_send_state"^?} protocol_callbacks;
{nw_listen_protocol_callbacks="new_flow"^?"disconnected"^?} listen_callbacks;
^{nw_flow_protocol={additional=[16C]^{nw_protocol_identifier}^{nw_protocol_callbacks}^{nw_protocol}^v^{nw_protocol}^v^{nw_protocol_ref_counted}^{additional}}{nw_listen_protocol=^{nw_listen_protocol_callbacks}^{nw_protocol}^v^v}@@@@@@@@@@@@QQ@@{nw_frame_array_s=^{nw_frame}^^{nw_frame}}^{nw_hash_table}{nw_frame_array_s=^{nw_frame}^^{nw_frame}}@@@Ib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b7[1C]} shared_protocol;
@"NSObject<OS_nw_read_request>" new_flow_read_requests;
{retained_ptr<nw_protocol *>="m_obj"^{nw_protocol}"m_should_release"b1"__pad_bits"b7"__pad_bytes"[7C]} transport_protocol;
{retained_ptr<nw_protocol *>="m_obj"^{nw_protocol}"m_should_release"b1"__pad_bits"b7"__pad_bytes"[7C]} joined_protocol;
{retained_ptr<nw_protocol *>="m_obj"^{nw_protocol}"m_should_release"b1"__pad_bits"b7"__pad_bytes"[7C]} proxy_protocol;
{retained_ptr<nw_protocol *>="m_obj"^{nw_protocol}"m_should_release"b1"__pad_bits"b7"__pad_bytes"[7C]} bottom_protocol;
^{nw_protocol_identifier=[32c]ii} ip_protocol_identifier;
@"NSObject<OS_nw_protocol_definition>" multiplexed_message_definition;
{retained_ptr<nw_protocol *>="m_obj"^{nw_protocol}"m_should_release"b1"__pad_bits"b7"__pad_bytes"[7C]} multiplexed_message_protocol;
^{tcp_info=CCCCIIIIIIIIIIIIIIiIQQQQQQQQQCCSQQQQQQQQQQQQ{tcp_conn_status=(?={?=b1b1b1b1}I)}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1IIIIIIIIIQIIIQQQQQQQQQQQQQQQ} tcp_info;
^{tcp_connection_info=CCCCIIIIIIIIIIIIb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b17QQQQQQQ} tcp_connection_info;
^{nw_data_transfer_snapshot=QQQQQQQQQQQQQQQQQQQQQQQIIb1b1b62[5{nw_data_transfer_migration_event=IIIIIiiCCCb1b1b1b1b1b3[0C]}]} data_transfer_snapshot;
Q snapshot_length;
I snapshot_count;
@"NSObject<OS_nw_path_flow_registration>" flow_registration;
@"NSObject<OS_dispatch_queue>" client_queue;
@? read_close_handler;
@? write_close_handler;
^{nw_hash_table=} multiplexed_flow_table;
@"NSObject<OS_nw_error>" last_error;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} lock;
@"NSObject<OS_nw_fd_wrapper>" connected_fd_wrapper;
I pending_write_bytes;
i pre_connected_fd;
@"NSObject<OS_nw_channel>" channel;
{retained_ptr<nw_protocol *>="m_obj"^{nw_protocol}"m_should_release"b1"__pad_bits"b7"__pad_bytes"[7C]} socket_protocol;
^{_DNSServiceRef_t=} sleep_proxy_ref;
@"NWConcrete_nw_endpoint_handler" child_endpoint_handler;
@"NWConcrete_nw_endpoint_handler" connected_endpoint_handler;
@"NSObject<OS_nw_array>" candidate_endpoint_handlers;
@"NSObject<OS_xpc_object>" flow_divert_token;
@"NSObject<OS_nw_endpoint>" flow_divert_endpoint;
@"NSObject<OS_nw_endpoint>" saved_original_endpoint;
S protocol_log_id_num;
b1 keepalive_event_enabled;
Q first_keepalive_time;
I keepalive_count;
I configured_keepalive_count;
I configured_keepalive_interval;
I restart_count;
I adaptive_read_count;
I adaptive_write_count;
@? adaptive_read_event_handler;
@? adaptive_write_event_handler;
@? keepalive_event_handler;
@? metadata_changed_event_handler;
@"NSObject<OS_nw_array>" connected_metadata;
@"NSObject<OS_nw_array>" connection_wide_metadata;
Q sent_application_byte_count;
Q received_application_byte_count;
[16C] connection_uuid;
^v connect_stall_timer;
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
-[NWConcrete_nw_endpoint_flow init];
-[NWConcrete_nw_endpoint_flow dealloc];
-[NWConcrete_nw_endpoint_flow cancelWithHandler:forced:];
-[NWConcrete_nw_endpoint_flow updatePathWithHandler:];
-[NWConcrete_nw_endpoint_flow startWithHandler:];
-[NWConcrete_nw_endpoint_flow applyWithHandler:toChildren:];
```
