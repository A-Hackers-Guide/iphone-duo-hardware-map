# `NWConcrete_nw_connection`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NWDeallocOnQueueObject`
- Protocols: `OS_nw_connection`
- 86 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_nw_endpoint>" endpoint;
@"NSObject<OS_nw_parameters>" parameters;
@"NSObject<OS_nw_context>" context;
@"NSObject<OS_dispatch_queue>" request_queue;
@"NSObject<OS_dispatch_workloop>" workloop;
@"NWConcrete_nw_connection" _internal_reference;
@"NSObject<OS_nw_candidate_manager>" candidate_manager;
@"NSObject<OS_nw_array>" ids_info;
Q start_time;
Q last_attempt_start_time;
I connection_attempt_count;
i state;
@"NSObject<OS_dispatch_data>" start_trace;
^{netcore_stats_tcp_report=(?={?={netcore_stats_tcp_statistics_report=QQQQQQQQQQQQQQQQIIIIIIIIIIIIIIIIIiiib1b1b1b1b1b1b1b1b1b1b1b1b4[6C]}{netcore_stats_tcp_cell_fallback_report=[20{netcore_stats_network_event=iI}][20{netcore_stats_data_usage_snapshot=QQQQQQQQ}]iIIIB[7C]}[8{netcore_stats_tcp_statistics_report=QQQQQQQQQQQQQQQQIIIIIIIIIIIIIIIIIiiib1b1b1b1b1b1b1b1b1b1b1b1b4[6C]}]iI}{nw_connection_report_s=QQQQQQQQQQQQQQQQQQQQQQQQQQQQIIIIIIIIIIIIIIIIIIIIIIIIIIIiiIiiiiiiiiiiCCC[16C][16C][50[16C]][256c][256c][32c]CiiCCb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b24[10{nw_connection_protocol_establishment_report_s=[32c]QQi[4C]}][2{nw_connection_proxy_hop_s=[64c][0C]}][5{nw_connection_migration_report_s=IIIIIiiCCCb1b1b1b1b1b3[0C]}]II[0C]})BB[6C]} stats_report;
i stats_reason;
b1 should_report_stats;
b1 stats_reported;
b1 should_report_generic_stats;
b1 generic_stats_reported;
b1 hit_max_timestamps;
b1 companion_bt_classic_upgrade_symptom_reported;
b1 should_report_activities;
b1 should_report_probe_parent_stats;
b1 should_report_probe_stats;
b1 attempted_probe;
b1 should_report_proxy_race_stats;
b1 should_report_fallback_eligible_stats;
b1 created_from_protocol;
b1 cancelled;
b1 prohibit_set_queue;
b1 batching;
b1 endpoint_handler_connected;
b1 has_called_update_block;
b1 blocked_tracker;
b1 unlisted_tracker;
b1 xcode_issue_raised;
@"NSObject<OS_nw_write_request>" batched_sends;
@"NSObject<OS_nw_read_request>" batched_receives;
i reported_viable;
i alternate_path_state;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} lock;
@"NSObject<OS_nw_endpoint_handler>" parent_endpoint_handler;
@"NSObject<OS_nw_endpoint_handler>" transport_endpoint_handler;
@"NSObject<OS_nw_endpoint_handler>" dry_run_endpoint_handler;
@"NSObject<OS_nw_endpoint_handler>" ready_dry_run_endpoint_handler;
I client_qos_class;
@"NSObject<OS_dispatch_queue>" client_queue;
@? client_handler;
@? cancel_handler;
^v viability_changed_timer;
@? viability_changed_handler;
@? better_path_available_handler;
@? alternate_path_state_handler;
@? path_changed_handler;
@? progress_handler;
@"NSObject<OS_nw_connection_progress_report>" last_progress_report;
C phases_delivered_bitmap;
i stall_reason;
{metadata_changed_registration_list_s="tqh_first"^{nw_connection_metadata_changed_registration}"tqh_last"^^{nw_connection_metadata_changed_registration}} metadata_changed_registration_list;
I interface_time_delta;
I connected_fallback_generation;
Q pending_expected_progress_target;
Q estimated_bytes_download;
Q estimated_bytes_upload;
^{nw_connection_timestamp_s=Q{nw_endpoint_handler_event_s=SS}(?={?=SCC}{?=S})[0C]} timestamps;
S num_timestamps;
S used_timestamps;
@"NSObject<OS_nw_array>" attempted_endpoints;
{nw_connection_throughput_monitor_s="current_bytes"Q"current_time"Q"last_bytes"Q"last_time"Q"timer"^v"minimum"I"__pad"[4C]} throughput_monitor;
@? low_throughput_handler;
@"NSObject<OS_nw_array>" activities;
@"NSObject<OS_nw_array>" probes;
@"NSObject<OS_dispatch_group>" cancel_group;
@"NSObject<OS_nw_establishment_report>" establishment_report;
@"NSObject<OS_nw_array>" data_transfer_reports;
@"NSObject<OS_nw_resolution_report>" failed_resolution_report;
@"NSObject<OS_nw_array>" errors;
I top_id;
[16C] top_uuid;
[16C] parent_uuid;
[16C] group_uuid;
C logging_sequence_number;
i privacy_stance;
@? interface_use_update_block;
@"NSObject<OS_nw_interface>" current_interface;
* parameters_description;
```

## Class methods

```
+[NWConcrete_nw_connection initialize];
```

## Instance methods

```
-[NWConcrete_nw_connection dealloc];
-[NWConcrete_nw_connection redactedDescription];
-[NWConcrete_nw_connection copyContext];
-[NWConcrete_nw_connection description];
```
