# `HIDRemoteDeviceServer`

- Image: [`/System/Library/PrivateFrameworks/RemoteHID.framework/RemoteHID`](../userland/System__Library__PrivateFrameworks__RemoteHID.framework__RemoteHID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _asyncQueue;
@"NSMutableDictionary" _refreshCounts;
@"NSMutableDictionary" _endpoints;
{os_unfair_recursive_lock_s="ourl_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"ourl_count"I} _lock;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,V_queue) queue;
```

## Instance methods

```
-[HIDRemoteDeviceServer initWithQueue:];
-[HIDRemoteDeviceServer endpoints];
-[HIDRemoteDeviceServer queue];
-[HIDRemoteDeviceServer disconnectAll];
-[HIDRemoteDeviceServer activate];
-[HIDRemoteDeviceServer description];
-[HIDRemoteDeviceServer cancel];
-[HIDRemoteDeviceServer getEndpoint:];
-[HIDRemoteDeviceServer remoteDeviceConfirmConnectHandler:packet:transportVersion:side:];
-[HIDRemoteDeviceServer _disconnectEndpointID:];
-[HIDRemoteDeviceServer connectEndpoint:];
-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:];
-[HIDRemoteDeviceServer disconnectEndpointID:];
-[HIDRemoteDeviceServer endpointMessageHandler:data:size:];
-[HIDRemoteDeviceServer endpointPacketHandler:packet:transportVersion:side:];
-[HIDRemoteDeviceServer getRefreshCountForEndpoint:deviceID:];
-[HIDRemoteDeviceServer remoteDeviceConnectHandler:packet:transportVersion:side:];
-[HIDRemoteDeviceServer remoteDeviceGetReport:type:reportID:report:];
-[HIDRemoteDeviceServer remoteDeviceGetReportHandler:packet:];
-[HIDRemoteDeviceServer remoteDeviceRefresh:deviceID:transportVersion:side:];
-[HIDRemoteDeviceServer remoteDeviceReportHandler:header:];
-[HIDRemoteDeviceServer remoteDeviceReportHandler:packet:];
-[HIDRemoteDeviceServer remoteDeviceSetReport:type:reportID:report:];
-[HIDRemoteDeviceServer remoteDeviceSetReportHandler:packet:];
-[HIDRemoteDeviceServer setRefreshCountForEndpoint:deviceID:count:];
```
