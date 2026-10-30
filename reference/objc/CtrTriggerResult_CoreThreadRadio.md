# `CtrTriggerResult`

- Image: [`/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`](../userland/System__Library__PrivateFrameworks__CoreThreadRadio.framework__CoreThreadRadio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 29 instance variables, 29 properties, 32 instance methods, 1 class methods

## Instance variables

```
B _is_leader_thirdparty;
B _is_partition_id_change_detected;
B _is_parent_change_detected;
B _is_threaddaemon_crash_detected;
B _is_threadfw_crash_detected;
B _is_role_detach_disable_detected;
B _is_border_router_advertised;
q _num_apple_BRs;
q _num_thirdparty_BRs;
q _num_thread_networks;
q _max_simultaneous_prefix_detected;
q _tx_total;
q _tx_total_success;
q _tx_success_perc;
q _rx_total;
q _rx_total_success;
q _rx_success_perc;
q _tx_delayavg;
q _tx_delaymin;
q _tx_delaymax;
q _coex_tx_denied_requests_percentage;
q _coex_rx_denied_requests_percentage;
@"NSString" _last_known_device_role;
@"NSString" _leader_name;
@"NSString" _num_routers;
@"NSString" _thread_mesh_size;
q _num_border_routers_advertised;
@"NSMutableArray" _accessory_result;
q _duration;
```

## Properties

```
@property (Tq,R,N,V_num_apple_BRs) num_apple_BRs;
@property (Tq,R,N,V_num_thirdparty_BRs) num_thirdparty_BRs;
@property (Tq,R,N,V_num_thread_networks) num_thread_networks;
@property (Tq,R,N,V_max_simultaneous_prefix_detected) max_simultaneous_prefix_detected;
@property (Tq,R,N,V_tx_total) tx_total;
@property (Tq,R,N,V_tx_total_success) tx_total_success;
@property (Tq,R,N,V_tx_success_perc) tx_success_perc;
@property (Tq,R,N,V_rx_total) rx_total;
@property (Tq,R,N,V_rx_total_success) rx_total_success;
@property (Tq,R,N,V_rx_success_perc) rx_success_perc;
@property (Tq,R,N,V_tx_delayavg) tx_delayavg;
@property (Tq,R,N,V_tx_delaymin) tx_delaymin;
@property (Tq,R,N,V_tx_delaymax) tx_delaymax;
@property (Tq,R,N,V_coex_tx_denied_requests_percentage) coex_tx_denied_requests_percentage;
@property (Tq,R,N,V_coex_rx_denied_requests_percentage) coex_rx_denied_requests_percentage;
@property (TB,R,N,V_is_leader_thirdparty) is_leader_thirdparty;
@property (T@"NSString",R,N,V_last_known_device_role) last_known_device_role;
@property (TB,R,N,V_is_partition_id_change_detected) is_partition_id_change_detected;
@property (T@"NSString",R,N,V_leader_name) leader_name;
@property (T@"NSString",R,N,V_num_routers) num_routers;
@property (T@"NSString",R,N,V_thread_mesh_size) thread_mesh_size;
@property (TB,R,N,V_is_parent_change_detected) is_parent_change_detected;
@property (TB,R,N,V_is_threaddaemon_crash_detected) is_threaddaemon_crash_detected;
@property (TB,R,N,V_is_threadfw_crash_detected) is_threadfw_crash_detected;
@property (TB,R,N,V_is_role_detach_disable_detected) is_role_detach_disable_detected;
@property (TB,R,N,V_is_border_router_advertised) is_border_router_advertised;
@property (Tq,R,N,V_num_border_routers_advertised) num_border_routers_advertised;
@property (T@"NSMutableArray",R,N,V_accessory_result) accessory_result;
@property (Tq,R,N,V_duration) duration;
```

## Class methods

```
+[CtrTriggerResult supportsSecureCoding];
```

## Instance methods

```
-[CtrTriggerResult duration];
-[CtrTriggerResult encodeWithCoder:];
-[CtrTriggerResult initWithCoder:];
-[CtrTriggerResult max_simultaneous_prefix_detected];
-[CtrTriggerResult num_apple_BRs];
-[CtrTriggerResult num_border_routers_advertised];
-[CtrTriggerResult num_thirdparty_BRs];
-[CtrTriggerResult num_thread_networks];
-[CtrTriggerResult rx_total];
-[CtrTriggerResult rx_total_success];
-[CtrTriggerResult tx_delayavg];
-[CtrTriggerResult tx_total];
-[CtrTriggerResult tx_total_success];
-[CtrTriggerResult is_partition_id_change_detected];
-[CtrTriggerResult tx_success_perc];
-[CtrTriggerResult is_role_detach_disable_detected];
-[CtrTriggerResult rx_success_perc];
-[CtrTriggerResult accessory_result];
-[CtrTriggerResult coex_rx_denied_requests_percentage];
-[CtrTriggerResult coex_tx_denied_requests_percentage];
-[CtrTriggerResult initWithData:num_thirdparty_BRs:num_thread_networks:max_simultaneous_prefixes:tx_total:tx_total_success:tx_success_perc:rx_total:rx_total_success:rx_success_perc:tx_delayavg:tx_delaymin:tx_delaymax:coex_tx_denied_reqs_perc:coex_rx_denied_reqs_perc:thirdparty_leader:last_known_device_role:is_partition_id_change_detected:leader_name:num_routers:thread_mesh_size:is_parent_change_detected:is_threaddaemon_crash_detected:is_threadfw_crash_detected:is_role_detach_disable_detected:is_border_router_advertised:num_border_routers_advertised:duration:];
-[CtrTriggerResult is_border_router_advertised];
-[CtrTriggerResult is_leader_thirdparty];
-[CtrTriggerResult is_parent_change_detected];
-[CtrTriggerResult is_threaddaemon_crash_detected];
-[CtrTriggerResult is_threadfw_crash_detected];
-[CtrTriggerResult last_known_device_role];
-[CtrTriggerResult leader_name];
-[CtrTriggerResult num_routers];
-[CtrTriggerResult thread_mesh_size];
-[CtrTriggerResult tx_delaymax];
-[CtrTriggerResult tx_delaymin];
```
