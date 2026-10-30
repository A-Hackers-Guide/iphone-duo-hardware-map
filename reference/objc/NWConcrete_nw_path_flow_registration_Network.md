# `NWConcrete_nw_path_flow_registration`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_path_flow_registration`
- 26 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NWConcrete_nw_path_evaluator" parent_evaluator;
@"NSObject<OS_nw_array>" subflow_registrations;
@"NSObject<OS_nw_array>" override_extra_interface_options;
[16C] registration_id;
[16C] nexus_agent;
^{necp_all_stats=(?={necp_tcp_stats={necp_stats_hdr=IIQ}{necp_stat_counts=QQQQIIIIIIIII}{necp_basic_metadata=II}{necp_extra_tcp_metadata={necp_connection_probe_status=b1b1b1b1}IIIIIIIIII}}{necp_udp_stats={necp_stats_hdr=IIQ}{necp_stat_counts=QQQQIIIIIIIII}{necp_basic_metadata=II}}{necp_quic_stats={necp_udp_stats={necp_stats_hdr=IIQ}{necp_stat_counts=QQQQIIIIIIIII}{necp_basic_metadata=II}}{necp_extra_quic_metadata=IIIIIIIIb1b1b30[16C]{necp_connection_probe_status=b1b1b1b1}[16C]}})} flow_stats_area;
^{ifnet_stats_per_flow=QQQIIIIIIIIIIIIIIIIIIb1b1b1b1b1b1b1b1b1b1b6SIQQQQ} flow_interface_stats;
r^{sk_nexusadv=} advisory;
^{nw_protocol_identifier=[32c]ii} upper_transport_stats_protocol;
^{nw_protocol_identifier=[32c]ii} transport_stats_protocol;
^{nw_protocol_identifier=[32c]ii} internet_stats_protocol;
^v upper_transport_stats_region;
^v transport_stats_region;
^v internet_stats_region;
@"NWConcrete_nw_path_evaluator" override_evaluator;
I override_traffic_class;
b1 registered;
b1 partial_checksum_offload;
b1 uses_nexus;
b1 has_override_traffic_class;
b1 override_is_expensive;
b1 override_is_constrained;
b1 override_uses_wifi;
b1 override_uses_cellular;
b1 override_reason;
b1 specific_use_only;
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
-[NWConcrete_nw_path_flow_registration init];
-[NWConcrete_nw_path_flow_registration dealloc];
-[NWConcrete_nw_path_flow_registration description];
```
