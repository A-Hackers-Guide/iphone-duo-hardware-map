# `HIDRemoteDeviceAACPServer`

- Image: [`/System/Library/PrivateFrameworks/RemoteHID.framework/RemoteHID`](../userland/System__Library__PrivateFrameworks__RemoteHID.framework__RemoteHID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `HIDRemoteDeviceServer`
- 8 instance variables, 1 properties, 24 instance methods, 0 class methods

## Instance variables

```
^{MobileBluetoothInterface=^^?} _mb;
^{BTSessionImpl=} _session;
^{BTAccessoryManagerImpl=} _manager;
@"NSMutableData" _decodeBuff;
Q _stateHandler;
Q _tsID;
@"HIDRemoteDeviceAACPServer" _me;
@"NSObject<OS_dispatch_queue>" _btQueue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,V_btQueue) btQueue;
```

## Instance methods

```
-[HIDRemoteDeviceAACPServer initWithQueue:];
-[HIDRemoteDeviceAACPServer dealloc];
-[HIDRemoteDeviceAACPServer activate];
-[HIDRemoteDeviceAACPServer description];
-[HIDRemoteDeviceAACPServer cancel];
-[HIDRemoteDeviceAACPServer btSessionEventHandler:event:result:];
-[HIDRemoteDeviceAACPServer btSessionCreate];
-[HIDRemoteDeviceAACPServer removeBTDevice:];
-[HIDRemoteDeviceAACPServer btQueue];
-[HIDRemoteDeviceAACPServer addBTDevice:];
-[HIDRemoteDeviceAACPServer btAccessoryEventHandler:event:state:];
-[HIDRemoteDeviceAACPServer btDeviceMessageHandler:type:data:size:];
-[HIDRemoteDeviceAACPServer btServiceEventHandler:services:eventType:event:result:];
-[HIDRemoteDeviceAACPServer btSessionInit:];
-[HIDRemoteDeviceAACPServer createRemoteDevice:deviceID:property:];
-[HIDRemoteDeviceAACPServer remoteDeviceGetReport:type:reportID:report:];
-[HIDRemoteDeviceAACPServer remoteDeviceRefresh:deviceID:transportVersion:side:];
-[HIDRemoteDeviceAACPServer remoteDeviceSetReport:type:reportID:report:];
-[HIDRemoteDeviceAACPServer removeAllBTDevices];
-[HIDRemoteDeviceAACPServer sendMessageBTDevice:data:size:transportVersion:side:];
-[HIDRemoteDeviceAACPServer setBtQueue:];
-[HIDRemoteDeviceAACPServer setMobileBluetoothInterface:];
-[HIDRemoteDeviceAACPServer stateHandler:];
-[HIDRemoteDeviceAACPServer timeSyncEnable:forEndpointID:];
```
