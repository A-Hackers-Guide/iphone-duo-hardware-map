# `nw_ip_channel_inbox`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `nw_listener_inbox`
- 10 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_nw_path>" _path;
@"NSObject<OS_nw_path_flow>" _flow;
@"NSObject<OS_nw_channel>" _channel;
{?="slh_first"^{nw_ip_channel_recent_flow}} _recent_flows;
^v _recent_flow_reaper;
r^(sockaddr_in_4_6={sockaddr=CC[14c]}{__sockaddr_header=CC}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}) _local;
I _scopeid;
S _local_port;
C _ip_proto;
b1 _bound_local_address;
```

## Class methods

```
+[nw_ip_channel_inbox alloc];
```

## Instance methods

```
-[nw_ip_channel_inbox destroy];
-[nw_ip_channel_inbox description];
-[nw_ip_channel_inbox cancel];
```
