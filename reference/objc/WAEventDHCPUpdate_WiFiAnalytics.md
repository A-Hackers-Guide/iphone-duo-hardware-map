# `WAEventDHCPUpdate`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WAEvent`
- 4 instance variables, 4 properties, 11 instance methods, 2 class methods

## Instance variables

```
{?="band"s"channel"s"channelWidth"s"motionState"s"reason"i"rssi"s"status"i"subreason"i"dhcpLatencyMilliSecs"i"networkAuthFlags"s"dhcpLeaseMins"i"interfaceIPv4Addr"{in_addr="s_addr"I}"ipv4routerAddr"{in_addr="s_addr"I}} _data;
@"NSString" _ssid;
@"NSString" _routerMACAddr;
@"WADeviceAnalytics_DHCPServerInfo" _dhcpServerInfo;
```

## Properties

```
@property (T@"NSString",&,N,V_ssid) ssid;
@property (T@"WADeviceAnalytics_DHCPServerInfo",&,N,V_dhcpServerInfo) dhcpServerInfo;
@property (T@"NSString",&,N,V_routerMACAddr) routerMACAddr;
@property (T@"NSString",R,D,N) bssid;
```

## Class methods

```
+[WAEventDHCPUpdate propertiesToPrefetch];
+[WAEventDHCPUpdate logChangesForBSS:withLAN:];
```

## Instance methods

```
-[WAEventDHCPUpdate processEventOnPersistentContainer:andRunPostprocessing:withError:];
-[WAEventDHCPUpdate ssid];
-[WAEventDHCPUpdate setSsid:];
-[WAEventDHCPUpdate updateRecord:];
-[WAEventDHCPUpdate data];
-[WAEventDHCPUpdate setRouterMACAddr:];
-[WAEventDHCPUpdate description];
-[WAEventDHCPUpdate initWithBssid:ssid:serverInfo:routerMacAddr:at:data:withError:];
-[WAEventDHCPUpdate routerMACAddr];
-[WAEventDHCPUpdate setDhcpServerInfo:];
-[WAEventDHCPUpdate dhcpServerInfo];
```
