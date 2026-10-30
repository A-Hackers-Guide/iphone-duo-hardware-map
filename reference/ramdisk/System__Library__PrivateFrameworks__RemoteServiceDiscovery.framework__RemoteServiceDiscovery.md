# `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery`

From the upgrade restore ramdisk (141-29011-104.dmg). 271,680 bytes.

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
TQ,N,V_device_id
disconnected_callback
_callback
connected_callback
dq
setCanceling:
setConnected_callback:
T@\"NSObject<OS_dispatch_queue>\",&,N,V_disconnected_callback_queue
T@\"OS_remote_device\",&,N,V_connected_callback_self_retain
T*,N,V_uuid
T@\"NSObject<OS_xpc_object>\",&,N,V_properties
_connected_callback
_queue
copyProperty:allowSensitive:
lastObject
setCallback:
setDisconnected_callback_self_retain:
TI,R,N
queue
setState:
shouldEncryptSocketData
canceling
connected_callback_queue
setCbq:
Ti,R,N,V_clientSock
device
event
T@\"NSObject<OS_dispatch_queue>\",&,N,V_dq
TQ,N,V_messaging_protocol_version
keepalive_time
setDisconnected_callback:
setUuid:
_connection
T*,R,N
_properties
setDevice_id:
connect_timeout
peer
uuid
TB,N,V_remotexpc_tls_enabled
_device_type
_onCancel
initWithSocket:device:queue:server:
setConnection:
TI,N,V_state
_disconnected_callback_queue
_serverSock
sha256
T@?,C,N,V_disconnected_callback
onCancel
setOnCancel:
T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue
TI,N,V_type
bytes
keepinterval
_dq
cbq
activate
connected_callback_self_retain
setAvailableService:
connection
next
setProperties:
_canceling
T@?,C,N,V_callback
TB,N,V_canceled
T@\"OS_xpc_remote_connection\",R,N,V_peer
setDq:
_connected_callback_queue
_connected_callback_self_retain
Tr*,N,V_name
addObject:
init
setType:
T@?,C,N,V_connected_callback
Tr*,N,V_availableService
_canceled
length
TI,N,V_device_type
_device_id
_remotexpc_tls_enabled
proxySocketOverRemoteXPC:
removeObject:
availableService
setConnected_callback_queue:
T@\"NSObject<OS_dispatch_queue>\",&,N,V_connected_callback_queue
callback
cancel
disconnected_callback_self_retain
mutableBytes
name
wildcard
dealloc
_disconnected_callback_self_retain
_messaging_protocol_version
_name
_type
serverSock
setName:
proxies
_cbq
copy
device_id
hasServiceWithName:peerMessage:
T@?,C,N,V_onCancel
matches:forMessage:log:
properties
setConnected_callback_self_retain:
Tr*,N,V_uuid
_clientSock
setDisconnected_callback_queue:
TB,N,V_canceling
canceled
data
T@\"OS_remote_device\",&,N,V_disconnected_callback_self_retain
_availableService
device_type
dictionaryWithObjects:forKeys:count:
stringWithFormat:
takeOwnershipOfClientSocket
type
Tr*,R,N
accept_block
clientSock
device_alias
device_name
messaging_protocol_version
_disconnected_callback
countByEnumeratingWithState:objects:count:
remotexpc_tls_enabled
service_name
setCanceled:
sortUsingComparator:
Ti,R,N,V_serverSock
_state
setRemotexpc_tls_enabled:
.cxx_destruct
_peer
_uuid
description
initWithBytes:length:
keepcount
setMessaging_protocol_version:
state
disconnected_callback_queue
keepalive
T@\"NSObject<OS_dispatch_queue>\",&,N,V_cbq
setDevice_type:
dataWithLength:
T@\"NSObject<OS_xpc_object>\",&,N,V_connection
v24@0:8r*16
Q16@0:8
B16@0:8
@\"NSObject<OS_dispatch_queue>\"
B32@0:8r*16@24
B32@0:8r*16@\"NSObject<OS_xpc_object>\"24
*
v24@0:8@?16
@\"OS_remote_listening_service\"
@\"OS_remote_pending_event\"
@28@0:8*16B24
@\"NSObject<OS_xpc_object>\"28@0:8*16B24
i16@0:8
@16@0:8
I16@0:8
v24@0:8@16
v24@0:8Q16
v20@0:8B16
@?16@0:8
@\"OS_xpc_remote_connection\"
I
@\"NSObject<OS_xpc_object>\"
@40@0:8i16@20@28B36
@\"OS_remote_device\"
v16@0:8
v20@0:8I16
r*16@0:8
i20@0:8i16
@?
i
r*
v24@0:8*16
*16@0:8
B
Q
@\"NSMutableArray\"
B40@0:8@16@24@32
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL uuid_out argument
host
remote_device_t
RemoteXPCVersionFlags
cmd
remote_device_copy_local_service_names was invoked on a device which is not connected yet. Doing so is either race-prone or inefficient due to polling. Please refer to the headerdocs for guidance.
enable_network_peer
is_tls_required
loopback
bridge
v16@?0@\"NSObject<OS_xpc_object>\"8
identity
DeviceType
INTERRUPTED
remote device browse
munmap
net.c
any
Major
v16@?0i8i12
remote_device_copy_service_names was invoked on a device which is not connected yet. Doing so is either race-prone or inefficient due to polling. Please refer to the headerdocs for guidance.
get_local_device_description
create_local_device_identity
bridge-external
ncm-device
LocationID
remote_device_check_service was invoked on a device which is not connected yet. Doing so is either race-prone or inefficient due to polling. Please refer to the headerdocs for guidance.
com.apple.remoted.service
resume_loopback
reset_loopback
host-external
remote client heartbeat
open
BUG IN CLIENT OF RemoteServiceDiscovery: remote_device_type_is_trusted() called with undefined type
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL complete argument
list_local_services
service
enable_bonjour_loopback
listen_cancel
compute-controller
connected
detach_loopback
v32@?0@\"NSObject<OS_sec_protocol_metadata>\"8@\"NSObject<OS_sec_trust>\"16@?<v@?B>24
compute-node
%u
UniqueDeviceID
BridgeBuildGroup
identity_cert
identity_key
connect
device_id
BuildVersion
API misuse: Invalid type value passed to remote_device_copy_unique_of_type
com.apple.RemoteServiceDiscovery.listener-demux
address
display-device
coredevice-host
keepcount
device_state
UUID
get_device
v16@?0@\"OS_remote_pending_event\"8
AppleInternal
authenticate_device
t1.seconds
device
list_local_device_services
BootSessionUUID
connect_loopback
com.apple.remoted.compute-platform
coredevice-device
properties
endpoint
helo_device
device_tls_enabled
SEPEpoch
DeviceName
disable_network_peer
 not
com.apple.remoted
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL matching_dict argument
arg
override
BridgeVersion
B24@?0Q8@\"NSObject<OS_xpc_object>\"16
TimesyncPayload
network-peer
v12@?0B8
Invalid forward transition from DISCONNECTED
SocketRemoteXpcProxy
mmap
SerialNumber
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL device argument
result
interface_name
q24@?0@\"OS_remote_device\"8@\"OS_remote_device\"16
socket
addresses
remote_device_copy_service was invoked on a device which is not connected yet. Doing so is either race-prone or inefficient due to polling. Please refer to the headerdocs for guidance.
get_local_device_identity
keepalive_time
ftruncate
(name~='%s', type='%s', uuid='%s', '%s' in services)
/System/Library/CoreServices/BridgeVersion.plist
error_code
disable_bonjour
browse_cancel
display-host
virtualmachine
ERROR
check_service
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL service argument
B7
EncryptSocketData
attached
v12@?0i8
write
get_connectable
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL service_name argument
trust_level
RemoteServiceDiscovery
Features
legacy_timesync
DeviceUUID
AvailableService
Browse handle must be canceled before releasing it
remove_device
listen
bonjour-peer
get_latest_connect_error
t1.subsecs
attach_loopback
disconnect_loopback
v16@?0@\"OS_remote_device\"8
sntp_server_exchange
<unknown>
OSVersion
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL alias argument
device_type
ServiceProperties
suspend_loopback
require_tls
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL interface name argument
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL address argument
eos
present_only
close
remote_device_authenticate was invoked on a device which is not connected yet. Doing so is either race-prone or inefficient due to polling. Please refer to the headerdocs for guidance.
reset
delete_local_device_identity
trusted
browse
ncm-host
get_service
ProductType
BUG IN CLIENT OF RemoteServiceDiscovery: unrecognized bridge_version_comparison_style
UsesRemoteXPC
Minor
add_device
is_tls_required_cmd
found_device
sntp_client_unicast
device_name
v20@?0@\"OS_remote_device\"8i16
connect_loopback_with_override
HWModel
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL trust argument
set_alias
com.apple.RemoteServiceDiscovery
keepalive
name
get_unique_device
v20@?0@\"OS_remote_device\"8B16
%u.%u.%u.%u.%u,%u
v8@?0
clockfunc
services
heartbeat_stats
fd
remote client queue
keepinterval
device_messaging_protocol_version
com.apple.remoted.control
list_services
heartbeat
get_heartbeat_stats
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL browser argument
connect_network_peer
virtualmachine-host
%u.%u.%u.%u.%u
BUG IN CLIENT OF RemoteServiceDiscovery: API called with NULL callback argument
disconnect_device
device_alias
untrusted
enable_bonjour
disconnected
connect_timeout
ServiceVersion
%{public}s> browsing_matching: Found a candidate
%{public}s> browsing_matching: Device didn't match
Received error sending CHECK SERVICE command
No cert data in reply.
remote_compute_controller_browse: %{darwin.errno}d
Event fired on deallocated device
assertion failure: \"reply != ((void *)0)\" -> %llu
Attempted to listen for service '%{public}s' twice
Unexpected mesage on compute platfrom channel
CONNECT command failed with INTERRUPTED
Got unexpected RemoteXPC message
assertion failure: \"self.device_id == (unsigned int)xpc_dictionary_get_uint64(desc, \"device_id\")\" -> %llu
RemoteXPC proxy's client socket is invalid
Received error sending GET LATEST CONNECT ERROR command
%{public}s> Received error sending RESET DEVICE command
%{public}s> Received error sending DISCONNECT DEVICE command
Creating service from: %{public}s
assertion failure: \"uuid_parse(value_str, uuid) == 0\" -> %llu
poll(2) failed while connecting to a service: %{errno}d
%{public}s> remote_device_timesync: This is no longer supported!
Failed to create key ACL: %{public}@
assertion failure: \"local_device_service_names != ((void*)0)\" -> %llu
device is not of type compute-controller
Updating device from: %s
%{public}s> browsing_matching: Found a match
Bogus response: result doesn't have mandatory key: %{public}s
connectx(2): %{errno}d
assertion failure: \"_uuid != ((void*)0)\" -> %llu
Failed to create key from data: %{public}@
Failed to create identity.
remote_compute_platform_tls_required: missing key %s
%{public}s> RemoteXPC is%s encrypted
Started browsing.
RemoteXPC is unavailable.
assertion failure: \"sema\" -> %llu
Sending CONNECT command
assertion failure: \"name\" -> %llu
connect(2) completed
No key data in reply.
BUG IN CLIENT OF RemoteServiceDiscovery: Tried to listen for unknown service '%{public}s'.
assertion failure: \"self.type != 0\" -> %llu
assertion failure: \"device_name != ((void*)0)\" -> %llu
assertion failure: \"d1 == ((void*)0)\" -> %llu
Received error sending ADD DEVICE command
Received error sending REQUIRE TLS command
asynchronously waiting for connect(2) to complete
fcntl(2): %{errno}d
Invalid or missing remote device connection version flags
%{public}s> remote_device_set_alias: client lacks privilege
Received error sending GET UNIQUE DEVICE command
Key '%{public}s' has invalid type
Starting browsing: %s
assertion failure: \"fd != -1\" -> %llu
accept(2): %{errno}d
%{public}s> : Device isn't connected
Received error sending LIST SERVICES command
Failed to initialize certificate data.
Creating device from: %{public}s
socket(2): %{errno}d
bind(2): %{errno}d
invalid sntp response payload
Failed to proxy socket over RemoteXPC
assertion failure: \"services != ((void*)0)\" -> %llu
Cannot set target user session for remoted connection because we failed to get the foreground user's uid: %{darwin.errno}d
RemoteXPC error: %{public}@
poll(2) timed out; events: 0x%x
getsockname(2): %{errno}d
Received error sending BROWSE command
socket connection failed, heartbeat remote device and try again
assertion failure: \"self->connection != ((void*)0)\" -> %llu
assertion failure: \"device_desc != ((void*)0)\" -> %llu
remote_device_copy_device_matching: device not found
Browsing stopped by client
remote_compute_node_listen_cancel: %{darwin.errno}d
connect socket failed
Got new device
Received error sending REMOVE DEVICE command
CONNECT command finished with an XPC error
assertion failure: \"self.device_id != 0\" -> %llu
Bogus response: operation failed without error code
assertion failure: \"message != ((void *)0)\" -> %llu
local_device_copy_service_names: failed
CONNECT command failed with unrecoverable error
assertion failure: \"xpc_get_type(msg) == (&_xpc_type_dictionary)\" -> %llu
assertion failure: \"new_state == REMOTE_DEVICE_STATE_CONNECTED || new_state == REMOTE_DEVICE_STATE_DISCONNECTED\" -> %llu
remote_socket_poll_connect_async: EBADF
listen(2): %{errno}d
assertion failure: \"self->device != ((void*)0)\" -> %llu
Received error sending CREATE LOCAL DEVICE IDENTITY command: %{public}@
remote_compute_platform_tls_required: %{darwin.errno}d
Error on service connection
Unable to start browsing: %s
Received xpc error sending AUTHENTICATE command
No identity in reply.
assertion failure: \"endpoint != ((void*)0)\" -> %llu
assertion failure: \"self->device_name != ((void*)0)\" -> %llu
Unexpected mesage on control channel
%{public}s> Updated device
Received error sending GET LOCAL DEVICE IDENTITY command: %{public}@
remote_device_copy_device_with_uuid_and_trust_level: device not found
Unexpected message from remoted
assertion failure: \"device != ((void*)0)\" -> %llu
poll(2) was interrupted while connecting to a service
%{public}s> remote_device_reset: client lacks privilege
local_device_create_identity: failed
Received error sending GET DEVICE command
assertion failure: \"new_state == REMOTE_DEVICE_STATE_DISCONNECTED\" -> %llu
%{public}s> remote_device_authenticate failed
Failed to get cert chain's leaf certificate.
local_device_copy_description: failed
local_device_copy_identity: failed
Received error sending DELETE LOCAL DEVICE IDENTITY command: %{public}@
Unexpected mesage on compute platform channel
connect(2) failed with error: %{errno}d
assertion failure: \"clock_gettime(_CLOCK_REALTIME, &ts)\" -> %llu
assertion failure: \"local_device_desc != ((void*)0)\" -> %llu
Received error sending LIST LOCAL DEVICE SERVICES command
remote_device_copy_unique_of_type: device not found
assertion failure: \"srv_conn != ((void*)0)\" -> %llu
write socket to RemoteXPC ended: %{darwin.errno}d
assertion failure: \"connect_errno == 0\" -> %llu
CONNECT command failed - bogus reply
%{public}s> Error on device connection: %s
Connection invalidated
assertion failure: \"connect_errno != 0\" -> %llu
Received error sending GET CONNECTABLE command
Failed to create certificate from data.
remote_compute_node_listen: %{darwin.errno}d
device advancing from %d to %d
F_SETNOSIGPIPE failed: %{darwin.errno}d
assertion failure: \"heartbeat_queue\" -> %llu
connect socket has succceeded - fd %d
creating socket pair failed: %s
Received error sending LIST LOCAL SERVICES command
Received error sending LISTEN command
Received error sending LISTEN CANCEL command
Received error sending GET SERVICE command
Received error sending GET LOCAL DEVICE DESCRIPTION command
duping server socket failed: %{darwin.errno}d
getsockname(2) did not populate sin6_port
assertion failure: \"getsockopt(fd, 0xffff, 0x1007, connect_errno_out, &error_length)\" -> %{errno}d
Failed to copy certificate chain.
remote_socket_poll_connect_async: NULL reply_queue
assertion failure: \"service_desc != ((void*)0)\" -> %llu
remote_device_check_service: service %{public}s found
%{public}s> browsing_matching: Device isn't connected
remote_compute_controller_add_node: %{darwin.errno}d
Received error sending BROWSE CANCEL command
remote_compute_controller_browse_cancel: %{darwin.errno}d
local_device_compute_platform_require_tls: %{darwin.errno}d
%{public}s> Device connection received unexpected command \"%s\"
%{public}s> remote_device_disconnect: %{errno}d
remote_device_copy_service: service not found
assertion failure: \"self.type == (unsigned int)xpc_dictionary_get_uint64(desc, \"device_type\")\" -> %llu
Not delivering the device because client is canceling the browser
write RemoteXPC to socket ended: %{darwin.errno}d
Failed to initialize key data.
local_device_delete_identity: failed
remote_compute_controller_remove_node: %{darwin.errno}d
CONNECT command failed with unknown result: %s
Error received on client connection:
OS_remote_service
OS_remote_device
RemoteDeviceCommon
OS_remote_device_browser
SocketRemoteXpcProxy
RemoteDeviceQuery
sha256
OS_remote_listening_service
OS_remote_pending_event
```
