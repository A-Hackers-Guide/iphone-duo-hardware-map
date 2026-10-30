# `HIDRemoteEndpoint`

- Image: [`/System/Library/PrivateFrameworks/RemoteHID.framework/RemoteHID`](../userland/System__Library__PrivateFrameworks__RemoteHID.framework__RemoteHID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 2 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _devices;
@"NSMutableArray" _prevDeviceLog;
{os_unfair_recursive_lock_s="ourl_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"ourl_count"I} _lock;
C _primarySide;
Q _endpointID;
```

## Properties

```
@property (TQ,V_endpointID) endpointID;
@property (TC,V_primarySide) primarySide;
```

## Instance methods

```
-[HIDRemoteEndpoint devices];
-[HIDRemoteEndpoint addDevice:];
-[HIDRemoteEndpoint endpointID];
-[HIDRemoteEndpoint setEndpointID:];
-[HIDRemoteEndpoint initWithID:];
-[HIDRemoteEndpoint removeAllDevices];
-[HIDRemoteEndpoint removeDeviceID:];
-[HIDRemoteEndpoint setPrimarySide:];
-[HIDRemoteEndpoint _removeDeviceID:];
-[HIDRemoteEndpoint copyState];
-[HIDRemoteEndpoint getDevice:];
-[HIDRemoteEndpoint logRemovedDevice:];
-[HIDRemoteEndpoint primarySide];
```
