# `/System/Library/PrivateFrameworks/RemoteHID.framework/RemoteHID`

iOS 27.2 dyld shared cache image. Version `224.40.2.0.0`. **[DSC]**

## Linked libraries (9)

- `/System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth`
- `/System/Library/PrivateFrameworks/TimeSync.framework/TimeSync`
- `/System/Library/PrivateFrameworks/HID.framework/HID`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libc++.1.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 5 classes, 0 protocols, 104 methods, 20 properties

### Class pages

Every class and protocol, with its methods: [`HIDAACPRemoteEndpoint`](../objc/HIDAACPRemoteEndpoint_RemoteHID.md), [`HIDRemoteDevice`](../objc/HIDRemoteDevice_RemoteHID.md), [`HIDRemoteDeviceAACPServer`](../objc/HIDRemoteDeviceAACPServer_RemoteHID.md), [`HIDRemoteDeviceServer`](../objc/HIDRemoteDeviceServer_RemoteHID.md), [`HIDRemoteEndpoint`](../objc/HIDRemoteEndpoint_RemoteHID.md)

### Classes

`HIDAACPRemoteEndpoint`, `HIDRemoteDevice`, `HIDRemoteDeviceAACPServer`, `HIDRemoteDeviceServer`, `HIDRemoteEndpoint`

### Properties

```
@property (T@"HIDRemoteDeviceAACPServer",&,V_server) server;
@property (TB,V_cancelled) cancelled;
@property (T@"NSObject<OS_dispatch_semaphore>",&,V_semaphore) semaphore;
@property (T@"NSData",&,V_lastGetReport) lastGetReport;
@property (Ti,V_lastSetReportStatus) lastSetReportStatus;
@property (TB,V_waitForReport) waitForReport;
@property (TI,V_handleReportCount) handleReportCount;
@property (TI,V_handleReportError) handleReportError;
@property (TQ,V_endpointID) endpointID;
@property (TQ,V_deviceID) deviceID;
@property (TC,V_transportVersion) transportVersion;
@property (TC,V_side) side;
@property (T^{IONotificationPort=},V_propertyPort) propertyPort;
@property (TI,V_propertyNotify) propertyNotify;
@property (TB,V_enableTS) enableTS;
@property (T@"HIDRemoteEndpoint",&,V_endpoint) endpoint;
@property (T@"NSObject<OS_dispatch_queue>",&,V_btQueue) btQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,V_queue) queue;
@property (TQ,V_endpointID) endpointID;
@property (TC,V_primarySide) primarySide;
```

## Strings (144)

```
i40@?0q8q16^v24^q32
invalid data_size
c
<HIDRemoteHIDUserDevice:%p id:%lld service:%llx handleReportCount:%u handleReportError:%u device:%@>
ReportInterval
bytes size exceeded
failed to set defaults
bytes overflow
-[HIDAACPRemoteEndpoint registerPropertyNotification:]
HIDTimeSyncProperties
Q
EndpointID
SerialNumber
size too large
wrong wire type
Transport
VendorID
RemoteDevices
end-of-stream
no malloc support
RequestTimeout
i
unterminated string
Active
TimeSyncEnabled
com.apple.hidrc.bluetooth
ProductID
1\"
packets
callback error
wrong size for fixed count field
TSClockID
<HIDRemoteDeviceAACPServer timeSyncID:%llu %@>
^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8
BT-AACP
BT_ADDR
<HIDRemoteDeviceServer state:%@ %@>
submsg size changed
missing required field
zero-length string
invalid field descriptor
invalid wire_type
integer too large
v32@?0@\"HIDRemoteDevice\"8Q16^B24
HIDRemoteDeviceAACPServer.mm
HIDRemoteAACPServer
v32@?0@\"NSNumber\"8@\"HIDRemoteDevice\"16^B24
i40@?0q8q16r^v24q32
incorrect fixed length bytes size
IOGeneralInterest
v8@?0
v32@?0@\"HIDRemoteEndpoint\"8Q16^B24
com.apple.hid.RemoteHID
Side
, retrying
Unrecognized data format
invalid field type
zero tag
com.apple.RemoteHID
default
stream full
io error
RemoteHID State
HIDTimeSyncProtocol
parent stream too short
Unserialized data is not a dictionary
invalid extension
string overflow
0 == status
VersionNumber
(none)
varint overflow
callback failed
PreviousRemoteDevices
array max size exceeded
array overflow
Couldn't set %u timesync for device:%p status:%d
BTAccessoryManagerRegisterCustomMessageClient 1:%d
Plist Serialization error %@
Create device:%@ with id:%llu for endpoint:%@ property:%@
Invalid message - length:%zu data:%@
decode fail
[%p] encoded packet - timestamp:%lld packet:%{RemoteHID:encodedpacket}.*P
Unsupported packet type:%u
HID AACP device:%p
Expected response
Invalid header - length:%zu data:%@
BTLocalDeviceGetConnectedDevices:%d
[device:%d] getReport type:%ld reportID:%ld
[device:%d] remoteDeviceGetReport:0x%x
[device:%d] remoteDeviceSetReport:0x%x%s
[device:%d] remoteDeviceSetReport:0x%x
addDevice device:%p result:%d
encodedData alloc fail
HIDUserDevice failed, property:%@
[device:%d] remoteDeviceSetReport:0x%x, bailing
HIDPacketDevice config data:%@
BTAccessoryManagerGetFeatureCapability:%d (FEATURE_SENSOR_DATA:%d)
remoteDeviceRefresh id:%llu result:%d
BTAccessoryManagerSendCustomMessage fail - device:%p result:%d
[%p] receive packet - type:0x%x timestamp:%lld packet:%{RemoteHID:packet}.*P
BTAccessoryManagerGetTimeSyncId device:%p tsID:0x%llx
TIMESYNC_NOT_AVAILABLE device:%p
GetReport device:%p status:%d
Set %u timesync for device:%p
Removing all devices for endpoint:%llu
BTAccessoryManagerRegisterCustomMessageClient 2:%d
HID AACP device remove:0x%llx
btAccessoryEventHandler device:%p event:%d state:%d
BTAccessoryManagerGetTimeSyncId failed result:%d
[device:%d] remoteDeviceGetReport timeout
endpointPacketHandler deviceid:%u type:%d size:%u
btServiceEventHandler services:0x%x eventType:%d event:%d result:%d
[device:%d] setReport type:%ld reportID:%ld report:%@
HID Device for deviceID:%d does not exist
encode size fail
Remove device:%@ with id:%llu for endpoint:%llu
Remaining devices:%@
DisconnectAll
handleReport:%@
received confirm connect for missing device id:%d, retry limit exceeded
decodeHeader fail
HIDAccesoryServiceEventCallback eventType:%d event:%d result:%d data:%p
Invalid report size:%d
HIDPacketDevice de-serialization error:%@
[device:%d] invalid report :%@
[%p] send packet:%{RemoteHID:packet}.*P
encodeHeader size fail
encode fail
Unknown device:%p
remoteDeviceSetReport deviceID:0x%llx type:%ld report:%@
received confirm connect for missing device id:%d, refreshing
BTSessionAttachWithQueue:%d
BTAccessoryManagerAddCallbacks:%d
BTServiceAddCallbacks:%d
btSessionEventHandler session:%p event:%d result:%d
SetReport device:%p status:%d
BTLocalDeviceGetDefault:%d
BTAccessoryManagerRegisterCustomMessageClient 3:%d
HIDAccesorySessionEventCallback event:%d result:%d
HID AACP device:%p already connected
BTAccessoryManagerGetDefault:%d
encodeHeader fail
TIMESYNC_AVAILABLE device:%p
```
