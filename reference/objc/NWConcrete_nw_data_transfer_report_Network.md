# `NWConcrete_nw_data_transfer_report`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_data_transfer_report`
- 13 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
Q start_time;
Q duration_milliseconds;
@"NWConcrete_nw_connection" connection;
@"NSObject<OS_nw_interface>" currently_collecting_interface;
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
I path_count;
I allocated_path_count;
i state;
{nw_data_transfer_path_report="total"{nw_data_transfer_path_report_value="received_ip_packet_count"Q"received_ip_ect1_packet_count"Q"received_ip_ect0_packet_count"Q"received_ip_ce_packet_count"Q"sent_ip_packet_count"Q"received_transport_byte_count"Q"received_transport_duplicate_byte_count"Q"received_transport_out_of_order_byte_count"Q"sent_transport_byte_count"Q"sent_transport_retransmitted_byte_count"Q"sent_transport_ecn_capable_packet_count"Q"sent_transport_ecn_capable_acked_packet_count"Q"sent_transport_ecn_capable_marked_packet_count"Q"sent_transport_ecn_capable_lost_packet_count"Q"transport_smoothed_rtt_milliseconds"Q"transport_minimum_rtt_milliseconds"Q"transport_current_rtt_milliseconds"Q"transport_rtt_variance"Q"transport_congestion_window"Q"transport_slow_start_threshold"Q"received_application_byte_count"Q"sent_application_byte_count"Q"__pad"[0C]}"incremental"{nw_data_transfer_path_report_value="received_ip_packet_count"Q"received_ip_ect1_packet_count"Q"received_ip_ect0_packet_count"Q"received_ip_ce_packet_count"Q"sent_ip_packet_count"Q"received_transport_byte_count"Q"received_transport_duplicate_byte_count"Q"received_transport_out_of_order_byte_count"Q"sent_transport_byte_count"Q"sent_transport_retransmitted_byte_count"Q"sent_transport_ecn_capable_packet_count"Q"sent_transport_ecn_capable_acked_packet_count"Q"sent_transport_ecn_capable_marked_packet_count"Q"sent_transport_ecn_capable_lost_packet_count"Q"transport_smoothed_rtt_milliseconds"Q"transport_minimum_rtt_milliseconds"Q"transport_current_rtt_milliseconds"Q"transport_rtt_variance"Q"transport_congestion_window"Q"transport_slow_start_threshold"Q"received_application_byte_count"Q"sent_application_byte_count"Q"__pad"[0C]}"interface"@"NSObject<OS_nw_interface>""__pad"[0C]} primary_path;
^{nw_data_transfer_path_report={nw_data_transfer_path_report_value=QQQQQQQQQQQQQQQQQQQQQQ[0C]}{nw_data_transfer_path_report_value=QQQQQQQQQQQQQQQQQQQQQQ[0C]}@[0C]} secondary_paths;
b1 collection_in_progress;
b1 collection_incremental;
b6 __pad_bits;
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
-[NWConcrete_nw_data_transfer_report init];
-[NWConcrete_nw_data_transfer_report dealloc];
-[NWConcrete_nw_data_transfer_report description];
```
