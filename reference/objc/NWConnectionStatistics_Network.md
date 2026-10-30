# `NWConnectionStatistics`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 58 properties, 77 instance methods, 1 class methods

## Instance variables

```
C _metricType;
@"NSString" _clientIdentifier;
@"NSString" _sourceIdentifier;
@"NSUUID" _externallyVisibleConnectionUUID;
@"NSUUID" _externallyVisibleParentUUID;
@"NSArray" _activities;
@"NSArray" _externallyVisibleActivityUUIDs;
@"NSDictionary" _layer2Report;
@"NSDictionary" _deviceReport;
@"NSMutableDictionary" _dictionaryReport;
{netcore_stats_tcp_report="u"(?="legacy"{?="statistics_report"{netcore_stats_tcp_statistics_report="bytes_in"Q"bytes_out"Q"bytes_duplicate"Q"bytes_ooo"Q"bytes_retransmitted"Q"packets_in"Q"packets_out"Q"packets_duplicate"Q"packets_ooo"Q"packets_retransmitted"Q"multipath_bytes_in_cell"Q"multipath_bytes_out_cell"Q"multipath_bytes_in_wifi"Q"multipath_bytes_out_wifi"Q"multipath_bytes_in_initial"Q"multipath_bytes_out_initial"Q"time_to_dns_resolved_msecs"I"time_to_dns_start_msecs"I"dns_resolved_time_msecs"I"time_to_connection_start_msecs"I"time_to_connection_establishment_msecs"I"connection_establishment_time_msecs"I"flow_duration_msecs"I"traffic_class"I"current_rtt_msecs"I"smoothed_rtt_msecs"I"best_rtt_msecs"I"rtt_variance"I"syn_retransmission_count"I"better_route_event_count"I"connection_reuse_count"I"app_reporting_data_stall_count"I"app_data_stall_timer_msecs"I"interface_type"i"connected_interface_type"i"multipath_service_type"i"dns_answers_cached"b1"connected"b1"cellular_fallback"b1"cellular_rrc_connected"b1"prefer_fallback"b1"kernel_reported_stalls"b1"kernel_reporting_connection_stalled"b1"kernel_reporting_read_stalled"b1"kernel_reporting_write_stalled"b1"tcp_fast_open"b1"first_party"b1"tls13_configured"b1"__pad_bits"b4"__pad"[6C]}"fallback_report"{netcore_stats_tcp_cell_fallback_report="network_events"[20{netcore_stats_network_event="network_event_type"i"time_to_network_event_msecs"I}]"data_usage_snapshots_at_network_events"[20{netcore_stats_data_usage_snapshot="bytes_in"Q"bytes_out"Q"multipath_bytes_in_cell"Q"multipath_bytes_out_cell"Q"multipath_bytes_in_wifi"Q"multipath_bytes_out_wifi"Q"multipath_bytes_in_initial"Q"multipath_bytes_out_initial"Q}]"deny_reason"i"network_event_count"I"data_usage_snapshots_at_network_events_count"I"fallback_timer_msecs"I"fellback"B"__pad"[7C]}"connection_attempts"[8{netcore_stats_tcp_statistics_report="bytes_in"Q"bytes_out"Q"bytes_duplicate"Q"bytes_ooo"Q"bytes_retransmitted"Q"packets_in"Q"packets_out"Q"packets_duplicate"Q"packets_ooo"Q"packets_retransmitted"Q"multipath_bytes_in_cell"Q"multipath_bytes_out_cell"Q"multipath_bytes_in_wifi"Q"multipath_bytes_out_wifi"Q"multipath_bytes_in_initial"Q"multipath_bytes_out_initial"Q"time_to_dns_resolved_msecs"I"time_to_dns_start_msecs"I"dns_resolved_time_msecs"I"time_to_connection_start_msecs"I"time_to_connection_establishment_msecs"I"connection_establishment_time_msecs"I"flow_duration_msecs"I"traffic_class"I"current_rtt_msecs"I"smoothed_rtt_msecs"I"best_rtt_msecs"I"rtt_variance"I"syn_retransmission_count"I"better_route_event_count"I"connection_reuse_count"I"app_reporting_data_stall_count"I"app_data_stall_timer_msecs"I"interface_type"i"connected_interface_type"i"multipath_service_type"i"dns_answers_cached"b1"connected"b1"cellular_fallback"b1"cellular_rrc_connected"b1"prefer_fallback"b1"kernel_reported_stalls"b1"kernel_reporting_connection_stalled"b1"kernel_reporting_read_stalled"b1"kernel_reporting_write_stalled"b1"tcp_fast_open"b1"first_party"b1"tls13_configured"b1"__pad_bits"b4"__pad"[6C]}]"report_reason"i"ip_address_attempt_count"I}"nw_connection_report"{nw_connection_report_s="bytes_in"Q"bytes_out"Q"bytes_duplicate"Q"bytes_ooo"Q"bytes_retransmitted"Q"ecn_capable_packets_sent"Q"ecn_capable_packets_acked"Q"ecn_capable_packets_marked"Q"ecn_capable_packets_lost"Q"packets_in"Q"ect1_packets_in"Q"ect0_packets_in"Q"ce_packets_in"Q"packets_out"Q"multipath_bytes_in_cell"Q"multipath_bytes_out_cell"Q"multipath_bytes_in_wifi"Q"multipath_bytes_out_wifi"Q"multipath_bytes_in_initial"Q"multipath_bytes_out_initial"Q"estimated_upload_throughput"Q"estimated_download_throughput"Q"transform_last_timeout_msecs"Q"attempt_delay_msecs"Q"attempt_establishment_msecs"Q"network_resolution_a_milliseconds"Q"network_resolution_aaaa_milliseconds"Q"network_resolution_svcb_milliseconds"Q"current_rtt_msecs"I"smoothed_rtt_msecs"I"best_rtt_msecs"I"rtt_variance"I"syn_retransmission_count"I"used_proxy_type"I"traffic_class"I"path_trigger_milliseconds"I"resolution_milliseconds"I"proxy_milliseconds"I"flow_connect_milliseconds"I"tls_milliseconds"I"flow_duration_milliseconds"I"ipv4_address_count"I"ipv6_address_count"I"connected_address_index"I"connection_reuse_count"I"data_stall_count"I"ipv4_dns_server_count"I"ipv6_dns_server_count"I"seconds_since_interface_change"I"transport_protocol"I"dns_protocol"I"connection_report_reason"I"transform_first_protocol"I"transform_connected_protocol"I"transform_connected_protocol_index"I"last_error_domain"i"last_error_code"i"tls_pake_negotiated"I"failure_reason"i"connected_interface_type"i"connected_interface_subtype"i"multipath_service_type"i"connection_mode"i"apple_host"i"apple_app"i"dns_provider"i"tls_version"i"stack_level"i"mptcp_version"C"first_address_family"C"connected_address_family"C"connection_uuid"[16C]"parent_uuid"[16C]"activities"[50[16C]]"bundle_id"[256c]"effective_bundle_id"[256c]"tls_library"[32c]"privacy_stance"C"client_accurate_ecn_state"i"server_accurate_ecn_state"i"proxy_result"C"privacy_proxy_client"C"is_known_tracker"b1"is_third_party_web_content"b1"triggered_path"b1"system_proxy_configured"b1"custom_proxy_configured"b1"fallback_eligible"b1"weak_fallback"b1"prefer_fallback"b1"used_fallback"b1"started_fallback"b1"resolution_required"b1"tls_configured"b1"tls13_configured"b1"tfo_configured"b1"multipath_configured"b1"connected"b1"tls_succeeded"b1"synthesized_ipv6_address"b1"synthesized_extra_ipv6_address"b1"ipv4_available"b1"ipv6_available"b1"used_tfo"b1"tls_version_timeout"b1"first_party"b1"is_daemon"b1"tls_handshake_timed_out"b1"is_path_expensive"b1"is_path_constrained"b1"prohibits_expensive"b1"prohibits_constrained"b1"svcb_requested"b1"svcb_received"b1"svcb_dohuri"b1"is_probe"b1"quic_experiment_enabled"b1"quic_deferred"b1"quic_application_deferred"b1"quic_denied"b1"quic_alternative_present"b1"quic_updated_alternative"b1"quic_speculative_attempt"b1"tls_ech_enabled"b1"is_web_search_content"b1"l4s_enabled"b1"used_pqtls"b1"pqtls_enabled"b1"quic_migration_enabled"b1"quic_migration_supported"b1"quic_stateless_reset_received"b1"quic_stateless_reset_during_path_probe"b1"ulpn"b1"tls_pake_offered"b1"tls_epsk_offered"b1"tls_epsk_negotiated"b1"tls_raw_epsks_enabled"b1"is_direct"b1"__pad_bits"b24"protocol_establishment_reports"[10{nw_connection_protocol_establishment_report_s="protocol_name"[32c]"handshake_milliseconds"Q"handshake_rtt_milliseconds"Q"protocol_index"i"__pad"[4C]}]"proxy_hops"[2{nw_connection_proxy_hop_s="proxy_name"[64c]"__pad"[0C]}]"migration_reports"[5{nw_connection_migration_report_s="event_index"I"connection_lifetime_milliseconds"I"migration_time_milliseconds"I"source_rtt_milliseconds"I"destination_rtt_milliseconds"I"source_interface_type"i"destination_interface_type"i"source_link_quality"C"destination_link_quality"C"result"C"from_fallback"b1"from_priority"b1"from_primary"b1"from_loss"b1"valid"b1"repeat_count"b3"__pad"[0C]}]"migration_delayed_by_rtt_count"I"migration_delayed_by_lqm_count"I"__pad"[0C]})"delegated"B"legacy"B"__pad"[6C]} _report;
```

## Properties

```
@property (T@"NSString",&,N,V_clientIdentifier) clientIdentifier;
@property (T{netcore_stats_tcp_report=(?={?={netcore_stats_tcp_statistics_report=QQQQQQQQQQQQQQQQIIIIIIIIIIIIIIIIIiiib1b1b1b1b1b1b1b1b1b1b1b1b4[6C]}{netcore_stats_tcp_cell_fallback_report=[20{netcore_stats_network_event=iI}][20{netcore_stats_data_usage_snapshot=QQQQQQQQ}]iIIIB[7C]}[8{netcore_stats_tcp_statistics_report=QQQQQQQQQQQQQQQQIIIIIIIIIIIIIIIIIiiib1b1b1b1b1b1b1b1b1b1b1b1b4[6C]}]iI}{nw_connection_report_s=QQQQQQQQQQQQQQQQQQQQQQQQQQQQIIIIIIIIIIIIIIIIIIIIIIIIIIIiiIiiiiiiiiiiCCC[16C][16C][50[16C]][256c][256c][32c]CiiCCb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b24[10{nw_connection_protocol_establishment_report_s=[32c]QQi[4C]}][2{nw_connection_proxy_hop_s=[64c][0C]}][5{nw_connection_migration_report_s=IIIIIiiCCCb1b1b1b1b1b3[0C]}]II[0C]})BB[6C]},N,V_report) report;
@property (T@"NSMutableDictionary",&,N,V_dictionaryReport) dictionaryReport;
@property (TC,N,V_metricType) metricType;
@property (T@"NSArray",&,N,V_activities) activities;
@property (T@"NSString",&,N,V_sourceIdentifier) sourceIdentifier;
@property (TB,R,N) delegated;
@property (Ti,R,N) interfaceType;
@property (TI,R,N) timeToDnsResolvedMsecs;
@property (TI,R,N) timeToDnsStartMsecs;
@property (TI,R,N) dnsResolvedTimeMsecs;
@property (TB,R,N) dnsAnswersCached;
@property (TI,R,N) timeToConnectionStartMsecs;
@property (TI,R,N) timeToConnectionEstablishmentMsecs;
@property (TI,R,N) connectionEstablishmentTimeMsecs;
@property (TI,R,N) flowDurationMsecs;
@property (Ti,R,N) connectedInterfaceType;
@property (TB,R,N) connected;
@property (TI,R,N) trafficClass;
@property (TB,R,N) fallbackEligible;
@property (TB,R,N) cellularFallback;
@property (TB,R,N) cellularRrcConnected;
@property (TB,R,N) tls13Configured;
@property (TB,R,N) tlsSucceeded;
@property (TB,R,N) kernelReportedStalls;
@property (TB,R,N) kernelReportingConnectionStalled;
@property (TB,R,N) kernelReportingReadStalled;
@property (TB,R,N) kernelReportingWriteStalled;
@property (TQ,R,N) bytesIn;
@property (TQ,R,N) bytesOut;
@property (TQ,R,N) bytesDuplicate;
@property (TQ,R,N) bytesOOO;
@property (TQ,R,N) bytesRetransmitted;
@property (TQ,R,N) packetsIn;
@property (TQ,R,N) packetsOut;
@property (TQ,R,N) packetsDuplicate;
@property (TQ,R,N) packetsOOO;
@property (TQ,R,N) packetsRetransmitted;
@property (TI,R,N) tcpRTTCurrentMsecs;
@property (TI,R,N) tcpRTTSmoothedMsecs;
@property (TI,R,N) tcpRTTBestMsecs;
@property (TI,R,N) tcpRTTVariance;
@property (TI,R,N) tcpSynRetransmissionCount;
@property (TB,R,N) tcpFastOpen;
@property (TI,R,N) tcpBetterRouteEventCount;
@property (TI,R,N) tcpConnectionReuseCount;
@property (TI,R,N) tcpAppReportingDataStallCount;
@property (TI,R,N) tcpAppDataStallTimerMsecs;
@property (TI,R,N) connectionReportReason;
@property (T@"NSUUID",R,N) connectionUUID;
@property (T@"NSUUID",&,N,V_externallyVisibleConnectionUUID) externallyVisibleConnectionUUID;
@property (T@"NSUUID",R,N) parentUUID;
@property (T@"NSUUID",&,N,V_externallyVisibleParentUUID) externallyVisibleParentUUID;
@property (T@"NSArray",&,N,V_externallyVisibleActivityUUIDs) externallyVisibleActivityUUIDs;
@property (T@"NSDictionary",&,N,V_layer2Report) layer2Report;
@property (T@"NSDictionary",&,N,V_deviceReport) deviceReport;
@property (T@"NSString",&,N) bundleID;
@property (T@"NSString",&,N) effectiveBundleID;
```

## Class methods

```
+[NWConnectionStatistics protocolToTransportProtocolString:];
```

## Instance methods

```
-[NWConnectionStatistics setReport:];
-[NWConnectionStatistics connected];
-[NWConnectionStatistics setDeviceReport:];
-[NWConnectionStatistics layer2Report];
-[NWConnectionStatistics trafficClass];
-[NWConnectionStatistics activities];
-[NWConnectionStatistics fallbackEligible];
-[NWConnectionStatistics setMetricType:];
-[NWConnectionStatistics metricType];
-[NWConnectionStatistics clientIdentifier];
-[NWConnectionStatistics setEffectiveBundleID:];
-[NWConnectionStatistics externallyVisibleActivityUUIDs];
-[NWConnectionStatistics interfaceType];
-[NWConnectionStatistics bytesOOO];
-[NWConnectionStatistics packetsOOO];
-[NWConnectionStatistics packetsRetransmitted];
-[NWConnectionStatistics timeToDnsStartMsecs];
-[NWConnectionStatistics tcpAppDataStallTimerMsecs];
-[NWConnectionStatistics setBundleID:];
-[NWConnectionStatistics externallyVisibleConnectionUUID];
-[NWConnectionStatistics kernelReportedStalls];
-[NWConnectionStatistics setExternallyVisibleParentUUID:];
-[NWConnectionStatistics tcpConnectionReuseCount];
-[NWConnectionStatistics timeToConnectionEstablishmentMsecs];
-[NWConnectionStatistics bytesOut];
-[NWConnectionStatistics cellularRrcConnected];
-[NWConnectionStatistics tls13Configured];
-[NWConnectionStatistics bytesIn];
-[NWConnectionStatistics packetsOut];
-[NWConnectionStatistics kernelReportingReadStalled];
-[NWConnectionStatistics timeToConnectionStartMsecs];
-[NWConnectionStatistics initWithJSONData:];
-[NWConnectionStatistics setLayer2Report:];
-[NWConnectionStatistics tlsHandshakeTimedOut];
-[NWConnectionStatistics sourceIdentifier];
-[NWConnectionStatistics connectedInterfaceType];
-[NWConnectionStatistics setClientIdentifier:];
-[NWConnectionStatistics packetsIn];
-[NWConnectionStatistics bytesRetransmitted];
-[NWConnectionStatistics setSourceIdentifier:];
-[NWConnectionStatistics connectionEstablishmentTimeMsecs];
-[NWConnectionStatistics tcpSynRetransmissionCount];
-[NWConnectionStatistics kernelReportingWriteStalled];
-[NWConnectionStatistics _createFallbackReportDictionaryFromStruct:];
-[NWConnectionStatistics effectiveBundleID];
-[NWConnectionStatistics timeToDnsResolvedMsecs];
-[NWConnectionStatistics dnsAnswersCached];
-[NWConnectionStatistics tcpAppReportingDataStallCount];
-[NWConnectionStatistics parentUUID];
-[NWConnectionStatistics dictionaryReport];
-[NWConnectionStatistics setActivities:];
-[NWConnectionStatistics packetsDuplicate];
-[NWConnectionStatistics bundleID];
-[NWConnectionStatistics connectionReportReason];
-[NWConnectionStatistics tcpFastOpen];
-[NWConnectionStatistics delegated];
-[NWConnectionStatistics tcpRTTBestMsecs];
-[NWConnectionStatistics setDictionaryReport:];
-[NWConnectionStatistics connectionUUID];
-[NWConnectionStatistics tcpRTTSmoothedMsecs];
-[NWConnectionStatistics externallyVisibleParentUUID];
-[NWConnectionStatistics tcpRTTVariance];
-[NWConnectionStatistics tcpRTTCurrentMsecs];
-[NWConnectionStatistics flowDurationMsecs];
-[NWConnectionStatistics setExternallyVisibleConnectionUUID:];
-[NWConnectionStatistics kernelReportingConnectionStalled];
-[NWConnectionStatistics cellularFallback];
-[NWConnectionStatistics _createDataUsageSnapshotDictionaryFromStruct:];
-[NWConnectionStatistics tlsSucceeded];
-[NWConnectionStatistics report];
-[NWConnectionStatistics initWithTCPReport:length:clientIdentifier:sourceIdentifier:];
-[NWConnectionStatistics dnsResolvedTimeMsecs];
-[NWConnectionStatistics setExternallyVisibleActivityUUIDs:];
-[NWConnectionStatistics bytesDuplicate];
-[NWConnectionStatistics _createStatisticsReportDictionaryFromStruct:];
-[NWConnectionStatistics deviceReport];
-[NWConnectionStatistics tcpBetterRouteEventCount];
```
