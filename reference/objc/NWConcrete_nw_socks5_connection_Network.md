# `NWConcrete_nw_socks5_connection`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_socks5_connection`
- 38 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
Q sc_id;
@"NWConcrete_nw_socks5_connection" sc_internally_retained_object;
@"NSObject<OS_nw_socks5_server>" sc_parent;
@"NWConcrete_nw_connection" sc_in_connection;
@"NSObject<OS_dispatch_queue>" sc_queue;
@? sc_cancel;
C sc_state;
C sc_out_address_type;
@"NSObject<OS_nw_path_evaluator>" sc_prefer_wifi_path_evaluator;
i sc_prefer_wifi_previous_path_status;
^v sc_udp_associate_verification_source;
I sc_udp_associate_verification_count;
(?="byte_pointer"*"ipv4_addr"^{in_addr}"ipv6_addr"^{in6_addr}"domain"*) sc_out_address;
S sc_shoes_request_length_hbo;
C sc_out_address_domain_length;
Q sc_busy_counter;
Q sc_busy_start_time_nanos;
Q sc_total_busy_time_nanos;
Q sc_start_time_nanos;
@"NWConcrete_nw_connection" sc_out_connection;
@"NSObject<OS_nw_error>" sc_error;
b1 sc_out_connection_failed_or_sent_write_close;
b1 sc_in_connection_failed_or_sent_write_close;
b1 sc_out_disable_proxy;
b1 sc_sent_reply;
b1 sc_has_read_from_in_connection;
b1 sc_out_udp;
b1 sc_should_prefer_wifi;
b1 sc_is_udp_associate;
b1 sc_processed_udp_associate_request;
b1 sc_in_connection_send_connected_endpoint;
b1 sc_in_connection_send_resolved_endpoint;
@"NWConcrete_nw_connection" sc_in_udp_associated_tcp_connection;
@"NSObject<OS_nw_establishment_report>" sc_out_establishment_report;
Q sc_out_connection_bytes_read;
Q sc_out_connection_bytes_written;
Q sc_in_connection_bytes_read;
Q sc_in_connection_bytes_written;
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
-[NWConcrete_nw_socks5_connection dealloc];
-[NWConcrete_nw_socks5_connection description];
```
