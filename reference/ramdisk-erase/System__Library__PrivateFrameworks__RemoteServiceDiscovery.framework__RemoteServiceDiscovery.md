# `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 271,680 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 25 (Size: 3736)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (8)

- `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery (compatibility version 1.0.0, current version 245.40.9)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC (compatibility version 1.0.0, current version 3298.52.1, weak)`
- `/usr/lib/libFDR.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (8 classes, 1 protocols)

Classes: `NSData`, `OS_remote_device`, `OS_remote_device_browser`, `OS_remote_listening_service`, `OS_remote_pending_event`, `OS_remote_service`, `RemoteDeviceQuery`, `SocketRemoteXpcProxy`

Protocols: `RemoteDeviceCommon`

## Strings (555)

```
B
@?
v20@0:8I16
*
@\"NSObject<OS_xpc_object>\"
@\"NSMutableArray\"
Q
B32@0:8r*16@24
B32@0:8r*16@\"NSObject<OS_xpc_object>\"24
@28@0:8*16B24
B40@0:8@16@24@32
r*
i20@0:8i16
@\"OS_remote_device\"
@\"OS_remote_pending_event\"
@40@0:8i16@20@28B36
I16@0:8
v24@0:8@?16
i16@0:8
@?16@0:8
@\"OS_xpc_remote_connection\"
*16@0:8
@\"NSObject<OS_xpc_object>\"28@0:8*16B24
@\"NSObject<OS_dispatch_queue>\"
@16@0:8
r*16@0:8
v24@0:8*16
v24@0:8Q16
i
v16@0:8
I
v24@0:8@16
B16@0:8
v20@0:8B16
@\"OS_remote_listening_service\"
v24@0:8r*16
Q16@0:8
host
display-device
v12@?0i8
Minor
device_type
add_device
bonjour-peer
ncm-host
ftruncate
UniqueDeviceID
remote_device_t
cmd
enable_bonjour
remote device browse
net.c
Features
heartbeat
com.apple.remoted.service
com.apple.remoted.compute-platform
 not
v16@?0i8i12
(name~='%s', type='%s', uuid='%s', '%s' in services)
Major
t1.subsecs
connect_loopback
connect_loopback_with_override
keepalive
SocketRemoteXpcProxy
LocationID
get_service
device_name
EncryptSocketData
listen_cancel
coredevice-host
clockfunc
ServiceVersion
set_alias
Browse handle must be canceled before releasing it
SerialNumber
BUG IN CLIENT OF RemoteServiceDiscovery: remote_device_type_is_trusted() called with undefined type
service
get_unique_device
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL interface name argument
close
keepinterval
socket
write
munmap
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL complete argument
identity
reset_loopback
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL trust argument
remote_device_authenticate was invoked on a device which is not connected yet. Doing so is either race-prone or inefficient due to polling. Please refer to the headerdocs for guidance.
reset
get_device
disable_network_peer
virtualmachine-host
ERROR
endpoint
remote_device_copy_local_service_names was invoked on a device which is not connected yet. Doing so is either race-prone or inefficient due to polling. Please refer to the headerdocs for guidance.
get_heartbeat_stats
device_alias
get_local_device_identity
interface_name
connect_timeout
device_messaging_protocol_version
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL matching_dict argument
BridgeVersion
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL alias argument
remove_device
loopback
sntp_server_exchange
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL device argument
identity_key
v20@?0@\"OS_remote_device\"8B16
bridge
keepcount
remote client heartbeat
com.apple.remoted
helo_device
fd
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL address argument
UsesRemoteXPC
com.apple.remoted.control
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL service argument
error_code
address
require_tls
host-external
SEPEpoch
/System/Library/CoreServices/BridgeVersion.plist
check_service
t1.seconds
disconnect_device
enable_bonjour_loopback
is_tls_required_cmd
compute-node
untrusted
connected
com.apple.RemoteServiceDiscovery
found_device
open
mmap
any
BridgeBuildGroup
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL uuid_out argument
get_local_device_description
v20@?0@\"OS_remote_device\"8i16
browse_cancel
bridge-external
addresses
OSVersion
v16@?0@\"NSObject<OS_xpc_object>\"8
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL callback argument
disconnect_loopback
identity_cert
list_local_services
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL service_name argument
DeviceUUID
compute-controller
remote client queue
v12@?0B8
arg
UUID
disconnected
override
AppleInternal
remote_device_copy_service_names was invoked on a device which is not connected yet. Doing so is either race-prone or inefficient due to polling. Please refer to the headerdocs for guidance.
TimesyncPayload
DeviceType
detach_loopback
browse
is_tls_required
device_state
resume_loopback
ProductType
list_local_device_services
AvailableService
trusted
keepalive_time
v16@?0@\"OS_remote_device\"8
BUG IN CLIENT OF RemoteServiceDiscovery: unrecognized bridge_version_comparison_style
B7
get_latest_connect_error
authenticate_device
legacy_timesync
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL browser argument
v16@?0@\"OS_remote_pending_event\"8
v32@?0@\"NSObject<OS_sec_protocol_metadata>\"8@\"NSObject<OS_sec_trust>\"16@?<v@?B>24
%u.%u.%u.%u.%u,%u
BuildVersion
services
create_local_device_identity
disable_bonjour
coredevice-device
Invalid forward transition from DISCONNECTED
q24@?0@\"OS_remote_device\"8@\"OS_remote_device\"16
%u.%u.%u.%u.%u
v8@?0
heartbeat_stats
eos
virtualmachine
sntp_client_unicast
BootSessionUUID
trust_level
RemoteServiceDiscovery
device_tls_enabled
<unknown>
result
com.apple.RemoteServiceDiscovery.listener-demux
ServiceProperties
suspend_loopback
network-peer
attached
properties
get_connectable
list_services
device
delete_local_device_identity
API misuse: Invalid type value passed to remote_device_copy_unique_of_type
DeviceName
ncm-device
device_id
B24@?0Q8@\"NSObject<OS_xpc_object>\"16
attach_loopback
connect_network_peer
connect
INTERRUPTED
RemoteXPCVersionFlags
remote_device_check_service was invoked on a device which is not connected yet. Doing so is either race-prone or inefficient due to polling. Please refer to the headerdocs for guidance.
listen
display-host
present_only
%u
HWModel
remote_device_copy_service was invoked on a device which is not connected yet. Doing so is either race-prone or inefficient due to polling. Please refer to the headerdocs for guidance.
name
enable_network_peer
accept(2): %{errno}d
remote_device_copy_service: service not found
%{public}s> remote_device_disconnect: %{errno}d
%{public}s> remote_device_set_alias: client lacks privilege
BUG IN CLIENT OF RemoteServiceDiscovery: Tried to listen for unknown service '%{public}s'.
CONNECT command finished with an XPC error
assertion failure: \"self->device != ((void*)0)\" -> %llu
Invalid or missing remote device connection version flags
Received error sending CHECK SERVICE command
No key data in reply.
Received error sending DELETE LOCAL DEVICE IDENTITY command: %{public}@
local_device_delete_identity: failed
Received error sending LIST LOCAL DEVICE SERVICES command
assertion failure: \"name\" -> %llu
Received error sending GET UNIQUE DEVICE command
remote_compute_node_listen: %{darwin.errno}d
assertion failure: \"sema\" -> %llu
assertion failure: \"self->device_name != ((void*)0)\" -> %llu
Bogus response: result doesn't have mandatory key: %{public}s
remote_socket_poll_connect_async: NULL reply_queue
getsockname(2): %{errno}d
Received error sending ADD DEVICE command
remote_compute_platform_tls_required: %{darwin.errno}d
%{public}s> browsing_matching: Found a match
assertion failure: \"_uuid != ((void*)0)\" -> %llu
Received error sending LIST LOCAL SERVICES command
connect socket failed
Got unexpected RemoteXPC message
Received error sending GET LATEST CONNECT ERROR command
Failed to create key from data: %{public}@
remote_compute_platform_tls_required: missing key %s
assertion failure: \"xpc_get_type(msg) == (&_xpc_type_dictionary)\" -> %llu
getsockname(2) did not populate sin6_port
remote_compute_controller_add_node: %{darwin.errno}d
Received error sending LISTEN command
assertion failure: \"endpoint != ((void*)0)\" -> %llu
Started browsing.
duping server socket failed: %{darwin.errno}d
Failed to copy certificate chain.
Failed to get cert chain's leaf certificate.
%{public}s> remote_device_authenticate failed
Received error sending GET LOCAL DEVICE IDENTITY command: %{public}@
Event fired on deallocated device
Received error sending REQUIRE TLS command
assertion failure: \"fd != -1\" -> %llu
Bogus response: operation failed without error code
RemoteXPC error: %{public}@
connectx(2): %{errno}d
assertion failure: \"self->connection != ((void*)0)\" -> %llu
%{public}s> : Device isn't connected
Received xpc error sending AUTHENTICATE command
remote_compute_controller_browse_cancel: %{darwin.errno}d
assertion failure: \"self.device_id != 0\" -> %llu
Updating device from: %s
Received error sending GET LOCAL DEVICE DESCRIPTION command
Failed to initialize key data.
assertion failure: \"heartbeat_queue\" -> %llu
RemoteXPC is unavailable.
invalid sntp response payload
Received error sending CREATE LOCAL DEVICE IDENTITY command: %{public}@
Attempted to listen for service '%{public}s' twice
%{public}s> RemoteXPC is%s encrypted
CONNECT command failed with INTERRUPTED
assertion failure: \"self.type != 0\" -> %llu
assertion failure: \"new_state == REMOTE_DEVICE_STATE_DISCONNECTED\" -> %llu
bind(2): %{errno}d
Failed to create key ACL: %{public}@
local_device_compute_platform_require_tls: %{darwin.errno}d
creating socket pair failed: %s
assertion failure: \"reply != ((void *)0)\" -> %llu
No cert data in reply.
%{public}s> browsing_matching: Device isn't connected
Error received on client connection:
assertion failure: \"self.type == (unsigned int)xpc_dictionary_get_uint64(desc, \"device_type\")\" -> %llu
socket(2): %{errno}d
connect(2) failed with error: %{errno}d
%{public}s> Received error sending DISCONNECT DEVICE command
device is not of type compute-controller
device advancing from %d to %d
remote_compute_controller_browse: %{darwin.errno}d
CONNECT command failed - bogus reply
Not delivering the device because client is canceling the browser
listen(2): %{errno}d
assertion failure: \"service_desc != ((void*)0)\" -> %llu
Failed to initialize certificate data.
CONNECT command failed with unrecoverable error
F_SETNOSIGPIPE failed: %{darwin.errno}d
poll(2) failed while connecting to a service: %{errno}d
Received error sending GET CONNECTABLE command
assertion failure: \"device_desc != ((void*)0)\" -> %llu
%{public}s> Error on device connection: %s
remote_socket_poll_connect_async: EBADF
remote_device_copy_device_matching: device not found
RemoteXPC proxy's client socket is invalid
%{public}s> browsing_matching: Found a candidate
assertion failure: \"getsockopt(fd, 0xffff, 0x1007, connect_errno_out, &error_length)\" -> %{errno}d
Failed to create identity.
assertion failure: \"local_device_service_names != ((void*)0)\" -> %llu
Unexpected mesage on compute platfrom channel
assertion failure: \"d1 == ((void*)0)\" -> %llu
assertion failure: \"connect_errno == 0\" -> %llu
poll(2) timed out; events: 0x%x
assertion failure: \"message != ((void *)0)\" -> %llu
write socket to RemoteXPC ended: %{darwin.errno}d
remote_device_check_service: service %{public}s found
Failed to create certificate from data.
remote_device_copy_device_with_uuid_and_trust_level: device not found
%{public}s> browsing_matching: Device didn't match
local_device_create_identity: failed
Browsing stopped by client
Creating service from: %{public}s
Creating device from: %{public}s
assertion failure: \"new_state == REMOTE_DEVICE_STATE_CONNECTED || new_state == REMOTE_DEVICE_STATE_DISCONNECTED\" -> %llu
assertion failure: \"device != ((void*)0)\" -> %llu
Got new device
fcntl(2): %{errno}d
connect socket has succceeded - fd %d
Starting browsing: %s
poll(2) was interrupted while connecting to a service
connect(2) completed
assertion failure: \"clock_gettime(_CLOCK_REALTIME, &ts)\" -> %llu
No identity in reply.
remote_device_copy_unique_of_type: device not found
Received error sending BROWSE CANCEL command
Unexpected mesage on compute platform channel
Error on service connection
Unable to start browsing: %s
%{public}s> Received error sending RESET DEVICE command
%{public}s> remote_device_reset: client lacks privilege
%{public}s> Updated device
Unexpected mesage on control channel
Received error sending LISTEN CANCEL command
Cannot set target user session for remoted connection because we failed to get the foreground user's uid: %{darwin.errno}d
Failed to proxy socket over RemoteXPC
Received error sending LIST SERVICES command
Received error sending GET SERVICE command
Key '%{public}s' has invalid type
remote_compute_controller_remove_node: %{darwin.errno}d
socket connection failed, heartbeat remote device and try again
Unexpected message from remoted
assertion failure: \"connect_errno != 0\" -> %llu
local_device_copy_description: failed
Received error sending BROWSE command
assertion failure: \"uuid_parse(value_str, uuid) == 0\" -> %llu
asynchronously waiting for connect(2) to complete
local_device_copy_identity: failed
local_device_copy_service_names: failed
assertion failure: \"device_name != ((void*)0)\" -> %llu
assertion failure: \"services != ((void*)0)\" -> %llu
Received error sending GET DEVICE command
Received error sending REMOVE DEVICE command
remote_compute_node_listen_cancel: %{darwin.errno}d
Sending CONNECT command
CONNECT command failed with unknown result: %s
assertion failure: \"srv_conn != ((void*)0)\" -> %llu
assertion failure: \"self.device_id == (unsigned int)xpc_dictionary_get_uint64(desc, \"device_id\")\" -> %llu
%{public}s> remote_device_timesync: This is no longer supported!
assertion failure: \"local_device_desc != ((void*)0)\" -> %llu
%{public}s> Device connection received unexpected command \"%s\"
Connection invalidated
write RemoteXPC to socket ended: %{darwin.errno}d
RemoteDeviceCommon
OS_remote_device_browser
OS_remote_listening_service
sha256
OS_remote_pending_event
SocketRemoteXpcProxy
RemoteDeviceQuery
OS_remote_service
OS_remote_device
T@?,C,N,V_disconnected_callback
length
setConnected_callback_queue:
Tr*,R,N
T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue
setCbq:
connected_callback
setOnCancel:
_device_id
canceled
clientSock
keepinterval
serverSock
setCanceling:
initWithBytes:length:
service_name
setConnection:
T@\"OS_remote_device\",&,N,V_connected_callback_self_retain
T@\"OS_xpc_remote_connection\",R,N,V_peer
_type
activate
onCancel
bytes
peer
setProperties:
T@?,C,N,V_onCancel
_connected_callback
canceling
device
setDq:
Tr*,N,V_uuid
disconnected_callback_self_retain
_serverSock
disconnected_callback
removeObject:
setCallback:
device_id
name
setType:
setUuid:
device_alias
messaging_protocol_version
TB,N,V_remotexpc_tls_enabled
TI,N,V_device_type
properties
setConnected_callback:
_dq
T@\"NSObject<OS_xpc_object>\",&,N,V_properties
T@\"NSObject<OS_xpc_object>\",&,N,V_connection
Tr*,N,V_availableService
availableService
setName:
sha256
state
_messaging_protocol_version
_onCancel
connected_callback_queue
type
copyProperty:allowSensitive:
T@\"OS_remote_device\",&,N,V_disconnected_callback_self_retain
TI,N,V_type
_name
_peer
proxies
hasServiceWithName:peerMessage:
setDisconnected_callback_queue:
_disconnected_callback_self_retain
connection
keepalive
connect_timeout
T@?,C,N,V_connected_callback
device_type
T@\"NSObject<OS_dispatch_queue>\",&,N,V_cbq
T*,R,N
cbq
Ti,R,N,V_serverSock
_clientSock
accept_block
cancel
copy
T*,N,V_uuid
TB,N,V_canceled
dataWithLength:
_remotexpc_tls_enabled
data
matches:forMessage:log:
sortUsingComparator:
wildcard
T@\"NSObject<OS_dispatch_queue>\",&,N,V_dq
TI,N,V_state
_device_type
_properties
description
disconnected_callback_queue
keepcount
setRemotexpc_tls_enabled:
_canceling
_cbq
addObject:
proxySocketOverRemoteXPC:
stringWithFormat:
_disconnected_callback
dictionaryWithObjects:forKeys:count:
mutableBytes
setMessaging_protocol_version:
TB,N,V_canceling
_availableService
queue
uuid
setAvailableService:
setCanceled:
setDisconnected_callback_self_retain:
T@\"NSObject<OS_dispatch_queue>\",&,N,V_disconnected_callback_queue
_state
_uuid
callback
event
keepalive_time
T@?,C,N,V_callback
.cxx_destruct
Ti,R,N,V_clientSock
Tr*,N,V_name
_connection
_queue
setDisconnected_callback:
dealloc
_canceled
_disconnected_callback_queue
init
initWithSocket:device:queue:server:
_connected_callback_self_retain
_callback
dq
remotexpc_tls_enabled
setConnected_callback_self_retain:
setState:
lastObject
next
TI,R,N
TQ,N,V_device_id
_connected_callback_queue
connected_callback_self_retain
setDevice_id:
shouldEncryptSocketData
setDevice_type:
T@\"NSObject<OS_dispatch_queue>\",&,N,V_connected_callback_queue
TQ,N,V_messaging_protocol_version
countByEnumeratingWithState:objects:count:
device_name
takeOwnershipOfClientSocket
```
