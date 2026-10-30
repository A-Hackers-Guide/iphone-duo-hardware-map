# `CtrAccessorySpecificTriggerResult`

- Image: [`/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`](../userland/System__Library__PrivateFrameworks__CoreThreadRadio.framework__CoreThreadRadio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 19 instance variables, 19 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _is_current_node_parent;
B _is_link_loss_detected;
B _is_neighbor_table_removal_detected;
B _is_direct_link;
@"NSString" _ip_addr;
@"NSString" _name;
q _tx_total;
q _tx_total_success;
q _rx_total;
q _rx_total_success;
q _tx_icmp_total;
q _rx_icmp_total;
@"NSString" _last_known_role;
q _avg_rssi;
q _tx_success_perc;
q _rx_success_perc;
q _tx_delayavg;
q _tx_delaymin;
q _tx_delaymax;
```

## Properties

```
@property (T@"NSString",R,N,V_ip_addr) ip_addr;
@property (T@"NSString",R,N,V_name) name;
@property (Tq,R,N,V_tx_total) tx_total;
@property (Tq,R,N,V_tx_total_success) tx_total_success;
@property (Tq,R,N,V_rx_total) rx_total;
@property (Tq,R,N,V_rx_total_success) rx_total_success;
@property (Tq,R,N,V_tx_icmp_total) tx_icmp_total;
@property (Tq,R,N,V_rx_icmp_total) rx_icmp_total;
@property (T@"NSString",R,N,V_last_known_role) last_known_role;
@property (TB,R,N,V_is_current_node_parent) is_current_node_parent;
@property (TB,R,N,V_is_link_loss_detected) is_link_loss_detected;
@property (TB,R,N,V_is_neighbor_table_removal_detected) is_neighbor_table_removal_detected;
@property (TB,R,N,V_is_direct_link) is_direct_link;
@property (Tq,R,N,V_avg_rssi) avg_rssi;
@property (Tq,R,N,V_tx_success_perc) tx_success_perc;
@property (Tq,R,N,V_rx_success_perc) rx_success_perc;
@property (Tq,R,N,V_tx_delayavg) tx_delayavg;
@property (Tq,R,N,V_tx_delaymin) tx_delaymin;
@property (Tq,R,N,V_tx_delaymax) tx_delaymax;
```

## Instance methods

```
-[CtrAccessorySpecificTriggerResult name];
-[CtrAccessorySpecificTriggerResult rx_total];
-[CtrAccessorySpecificTriggerResult rx_total_success];
-[CtrAccessorySpecificTriggerResult tx_delayavg];
-[CtrAccessorySpecificTriggerResult tx_total];
-[CtrAccessorySpecificTriggerResult tx_total_success];
-[CtrAccessorySpecificTriggerResult ip_addr];
-[CtrAccessorySpecificTriggerResult tx_success_perc];
-[CtrAccessorySpecificTriggerResult last_known_role];
-[CtrAccessorySpecificTriggerResult rx_success_perc];
-[CtrAccessorySpecificTriggerResult avg_rssi];
-[CtrAccessorySpecificTriggerResult initWithAccessoryData:ip_addr:tx_total:tx_total_success:rx_total:rx_total_success:tx_icmp_total:rx_icmp_total:last_known_role:is_current_node_parent:is_link_loss_detected:is_neighbor_table_removal_detected:is_direct_link:avg_rssi:tx_success_perc:rx_success_perc:tx_delayavg:tx_delaymin:tx_delaymax:];
-[CtrAccessorySpecificTriggerResult is_current_node_parent];
-[CtrAccessorySpecificTriggerResult is_direct_link];
-[CtrAccessorySpecificTriggerResult is_link_loss_detected];
-[CtrAccessorySpecificTriggerResult is_neighbor_table_removal_detected];
-[CtrAccessorySpecificTriggerResult rx_icmp_total];
-[CtrAccessorySpecificTriggerResult tx_delaymax];
-[CtrAccessorySpecificTriggerResult tx_delaymin];
-[CtrAccessorySpecificTriggerResult tx_icmp_total];
```
