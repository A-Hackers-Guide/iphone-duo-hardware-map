# `/usr/lib/system/libxpc.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 737,696 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 40 (Size: 4528)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (21)

- `/usr/lib/system/libxpc.dylib (compatibility version 1.0.0, current version 3298.52.1)`
- `/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libcompiler_rt.dylib (compatibility version 1.0.0, current version 103.4.0)`
- `/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.2)`
- `/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/usr/lib/system/libsystem_pthread.dylib (compatibility version 1.0.0, current version 553.40.2)`
- `/usr/lib/system/libunwind.dylib (compatibility version 1.0.0, current version 2200.5.0)`
- `/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0)`
- `/usr/lib/system/libdispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/system/libsystem_sandbox.dylib (compatibility version 1.0.0, current version 3051.40.81)`
- `/usr/lib/system/libmacho.dylib (compatibility version 1.0.0, current version 1040.0.0)`
- `/usr/lib/system/libsystem_asl.dylib (compatibility version 1.0.0, current version 409.40.3, upward)`
- `/usr/lib/system/libsystem_collections.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/usr/lib/system/libsystem_darwin.dylib (compatibility version 1.0.0, current version 1.0.0, upward)`
- `/usr/lib/system/libsystem_featureflags.dylib (compatibility version 1.0.0, current version 111.0.0, upward)`
- `/usr/lib/system/libsystem_trace.dylib (compatibility version 1.0.0, current version 1966.40.15, upward)`
- `/usr/lib/system/libsystem_info.dylib (compatibility version 1.0.0, current version 1.0.0, upward)`
- `/usr/lib/system/libsystem_notify.dylib (compatibility version 1.0.0, current version 368.40.2, upward)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0, upward)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (36 classes, 31 protocols)

Classes: `OS_os_transaction`, `OS_xpc_activity`, `OS_xpc_array`, `OS_xpc_bool`, `OS_xpc_bundle`, `OS_xpc_connection`, `OS_xpc_data`, `OS_xpc_date`, `OS_xpc_dictionary`, `OS_xpc_double`, `OS_xpc_endpoint`, `OS_xpc_error`, `OS_xpc_event_publisher`, `OS_xpc_fd`, `OS_xpc_file_transfer`, `OS_xpc_int64`, `OS_xpc_listener`, `OS_xpc_mach_recv`, `OS_xpc_mach_send`, `OS_xpc_mach_send_once`, `OS_xpc_null`, `OS_xpc_object`, `OS_xpc_payload`, `OS_xpc_peer_requirement`, `OS_xpc_pipe`, `OS_xpc_pointer`, `OS_xpc_rich_error`, `OS_xpc_serializer`, `OS_xpc_service`, `OS_xpc_service_instance`, `OS_xpc_session`, `OS_xpc_shmem`, `OS_xpc_string`, `OS_xpc_string_cache`, `OS_xpc_uint64`, `OS_xpc_uuid`

Protocols: `NSObject`, `OS_xpc_activity`, `OS_xpc_array`, `OS_xpc_bool`, `OS_xpc_bundle`, `OS_xpc_connection`, `OS_xpc_data`, `OS_xpc_date`, `OS_xpc_dictionary`, `OS_xpc_double`, `OS_xpc_endpoint`, `OS_xpc_error`, `OS_xpc_fd`, `OS_xpc_file_transfer`, `OS_xpc_int64`, `OS_xpc_mach_recv`, `OS_xpc_mach_send`, `OS_xpc_mach_send_once`, `OS_xpc_null`, `OS_xpc_object`, `OS_xpc_pipe`, `OS_xpc_pointer`, `OS_xpc_rich_error`, `OS_xpc_serializer`, `OS_xpc_service`, `OS_xpc_service_instance`, `OS_xpc_shmem`, `OS_xpc_string`, `OS_xpc_string_cache`, `OS_xpc_uint64`, `OS_xpc_uuid`

## Strings (1,385)

```
Attempt to set non-bundled on a live connection.
<%s: %p>: %lli
_asan
/Contents
Attempting to create peer requirement with invalid type: %s
InvolvedProcesses
der_decode_numeric_string
Client returned invalid action for dictionary container end event
invalid tag or length
No Constraint provided
XPC_EXIT_REASON_EXTENSION_CHECK_IN_TIMEOUT
Client returned invalid action for array container end event
MIG demux failed. This message ID is invalid: 0x%x
Service name already exists
Configuration error: Service does not have NSString.
Sandbox restriction
base
%d: [
Could not get asid for stream/token: %s/%llu: %d: %s
Attempt to send non-message dictionary as reply
_AdditionalSubServices
Data corruption: Invalid out-of-line descriptor specified.
com.apple.launchd.service-stats-default
%s%c
uuids
xpc_pipe_create_with_user_session_uid() cannot be used with the privileged flag.
security.mac.amfi.developer_mode_status
XPC_EXIT_REASON_ABANDONED
[<count = %u>]
Could not signal service %s: %d: %s
unsupported type: %s
Attempt to set binpref on a connection without instance uuid.
Constraint too large
B24@?0^v8Q16
NSRunLoop
Request for stale data
DASData
Session manually canceled
YES
Attempt to get connection property before it was populated.
Resources
lt
com.apple.libxpc.launchd
RequireSignificantUserInactivity
(not running)
Permission denied
Unknown service name
NSString
configurable
...
uuid
Versions/Current/Library/LoginItems
endpoint
<%s: %p> { name = %s }
RequireNetworkConnectivity
dictionary keys are not sorted or not unique
init-done
XPCExtensionBundleIdentifier
Given object not of required type. Given: %s, required: %s
This SPI may not be called on non-configurable services.
Attempt to change the non-launching property on a live connection.
Configuration error: Service specifies unknown RunLoopType.
XPC_DEBUG_SERVICES
, value = %p
/MacOS
linked xpc services
<%s> { id = %lld, state = %d, transaction = %s }
number too large
libdispatch bug: Unexpected send result.
XPCErrorDescription
Service stub created
Could not get service identifier for token: %llu: %d: %s
Attempt to populate an unknown bundle type.
/
invalid arguments passed in
Connection init failed at lookup with error %d - %s
%a %b %d %T %Y %Z
Out-of-line descriptor count is out-of-sync. Actual/expected: %lu/%lu
der_vm_execute_select_key
cid
Tried to serialize an object containing a cycle
failed to serialized value for key: %s
Path had bad ownership/permissions
Bad context on connection port: notify: 0x%x self: %p pctx: %p recvp: 0x%x
Service is disabled
der_vm_execute_select_longest_matching_key
key contains an embedded NUL
unknown number encoding
%d.%d
Only peer connections have a filter policy
XPCServiceEndpointName
]]>
apos
Calling -init
Service cannot load in current boot environment
XPCExtensionPath
Attempt to set the bs_checkin_info on a peer connection.
ingsk
Reply format must specify a dictionary!
bundle %s tainted with reason \"%s\"
Over-resume of a connection.
!ready_only
Configuration error: Bundle Info.plist has no XPCService dictionary.
team-identifier-for-current-process
%s (backtrace follows)
Could not set XPC event for stream/key: %s/%s: %d: %s
pid domain
Connections cannot be directly embedded in messages. You must create an endpoint from the connection.
xpc_user_sessions_get_foreground_uid() failed with error: %d - %s
boolean should be exactly 1 byte
descriptor
Cannot set NONE when specifying checkin info.
flags
bootstrap_lookup_children
XPCServiceEndpointNeedsActivation
path
Requestor lacks required entitlement
xpc-fault
uid
file
bundle
RequiresClassC
unable to decode value tag for key-value pair
Configuration error: Bundle XPCService dictionary does not declare specified subservice.
<%s: %p> { name = %u, right = %s, urefs = %u }
The specified path is not a bundle
Unexpected type to match against
Setting the target UID for a connection is not supported on embedded platforms.
<no channel>
%f
com.apple.xpc.transaction
attrs
Configuration error: Service does not have NSAutoreleasePool.
/usr/lib
Bogus domain object.
RequireHDDSpinning
UserRequestedBackupTask
Not eligible for acceleration
bootstrap port must lead to PID 1 [actual pid = %d]
Routine not yet implemented
key / value decoding failure
/System/Library/Frameworks/UIKit.framework/UIKit
Exclusive
RunOnAppForeground
%Y-%m-%dT%H:%M:%SZ
libdispatch bug: _sendp is still valid
_AdditionalServices
-->
root path = \"%s\",\n
Could not find specified service
DuetAttributeValue
true
Configuration error: Nonexistent bundle layout was resolved.
data element not allowed
der_decode_utc_time
<%s: %p> { count = %u, capacity = %u, contents =\n
Bug in libxpc: Message larger than reliable size.
Bug in libxpc: No port given.
'\"`~\\
Bad response from server
connection must be a listener.
__XPC_
%s.%s
NetworkParameters
Data corruption: CoreEntitlements has aborted due to an unrecoverable error
, buff = (unmapped), len = %lu
null
__libxpcunittest
service
der_validate_array
cryptex
Data corruption: Out-of-bounds descriptor append attempt.
Null required format arg!
%lu: 
()
subsetport
block device
full graph sz = %zu, remaining = %zu, needed = %zu
Unknown numeric string encoding
, str = %s, len = %zu, string cache = %p
%s => 
mach send right
event
\t\"%s\" => %zu\n
Service cannot be launched because of BTM policy
launchd
Contents/Library/LaunchAgents
DataBudgeting
Connection init failed with readying error with error %d - %s
peer
%svoucher = %p, 
MayRebootDevice
dictionary key is not a valid string
Service does not support the specified action
Attempt to reset attach handler.
der_vm_string_from_context
Canceling event publisher for %s because of error: %d - %s
Message:\n%s
Session must be inactive to extract the connection, not %s
BUG IN CLIENT OF libxpc: attempt to create file transfer from unusual file type
XPC_EXIT_REASON_FAST_LOGOUT
Can't set event channel on peer connection
Invalid payload transport for dictionary creation
CFFIXED_USER_HOME
}
(not registered)
request originated from a different PID
Failed to enable path: code = %d: %s, %s
Attempting to activate an already active session
, list follows
NetworkTransferSize
_UIApplicationClass
<%s: %p>: %p
PowerNap
ExpectedDuration
der_validate_dictionary
Attempt to clear sent descriptors on a serializer created from the wire.
B24@?0r*8^v16
Underflow of transaction count.
signing-identifier
Attempt to set target session UID on a privileged connection.
Data corruption: Reply handler block scheduled with NULL reply.
XPC_CONTROL_USER_SESSIONS_INFO failed with error %d - %s
Invalid disposition
Action not allowed on singleton service
The specified service path was not in the service cache
com.apple.system.notification_center
der_decode_boolean
%x
reqport
]
Bug in libxpc: invalid state passed to _xpc_session_message_error_during_cancelation()
PostInstall
send_message_with_reply_sync is not allowed with a non-launching Mach service
Service is already active
XPCService
, %s
com.apple.xpc.activity.unmanaged
BUG IN (CLIENT OF?) LIBXPC: invalid disconnect oldsendp 0x%x, conn %s
, fileport = 0x%x
0x0
data
This API is functionally useless.
XPCEventStreamName
reload-error
Unknown UTC Time encoding
no value for key: %s
linked info.plist
Cycling
com.apple.logd
der_vm_execute_string_value_allowed
voucher = %p, 
signal
XPCExtensionPID
Attempting to send message using a canceled session
RequiresClassA
token.pid
Check-in is too big : %zu
gt
Array mutated during iteration
Could not get attrs using %s for pid %d: %d: %s
noop
Attempt to set instance binpref on a listening connection.
<%s: %p> %s
entitlements blob does not have CCDER_ENTITLEMENTS coding
bool decode failure
euid of PID 1 must be 0
A complete hack
cputypes
%s[%p]%s: { refcnt = %x, xrefcnt = %x
subscriber-pid
Reconnect failed at listener activation with error %d - %s
Bug in libxpc: _xpc_objc_uimain() is not supposed to return
CEValidateWithOptions
%p
<%s: %p> { id = %lld, state = %d, transaction = %s }
DiskIntensive
Could not copy XPC event for stream/token/subscriber: %s/%llu/%d: %d: %s
Requestor is not a platform binary
XPC_EXIT_REASON_UNKNOWN_IPC
ds
while trying to exit cleanly
false
DuetRelatedApplications
<%s>
Attempt to fetch the bs_checkin_info on a live connection.
Peer connection was rejected by the listener (%s)
bootstrap
Attempting to activate an already active listener
Unable to allocate reply port, possible port leak
Attempt to fetch the bs_checkin_info on a listener connection.
, name = %s, count = %zu
populated = %d,\n
Configuration error: Specified service name is disabled.
Invalid rest suffix for 'uint{64}' format specifier!
/Contents/MacOS
der_decode_entitlements
Termination imminent
int64
NSAutoreleasePool
directory
Invalid rest suffix for 'int{64}' format specifier!
LWCR invalid: %s
der_vm_execute_match_string
rich error
Attempt to set the bs_checkin_info on a live connection.
, 
v20@?0^{dispatch_data_s=}8i16
MotionState
resume is not allowed on this connection.
Extracted
Attempting to activate a listener in an unknown state
suspended
Unknown boolean encoding
Subscribed to event %s using token %llu
_xpc_connection_init
%s\n
<%s: %p> { count = %u, transaction: %d, 
Session must be canceled before it's disposed
, port = 0x%x
monitor_id
type
monitor
enabled
Attempting to select an integer value from a non-integer DER object
[%s]: %s\n
lookup-handle
Cannot set specific when not from endpoint.
in
set target user session UID
<%s: %p> { name = 0x%x, right = %s }
/System/Cryptexes/OS/
Peer image changed
user/foreground/ specifier is not supported on this platform
Download
Data corruption: Teardown of an uninitialized connection.
xpc_user_sessions_get_session_uid() must not be called if xpc_user_sessions_enabled() is false
The executable did not ship in the bundle
Extension objects cannot be serialized.
[%zu] -> %p
, value = %f
dispatch_main
This function, long deprecated, is no longer supported. Please stop using launch_data (or at least switch to launch_data_new_integer).
_profile
Path not searched for services
Could not find a bundle of the given identifier through LaunchServices
Run
CoreEntitlements: Couldn't iterate over DER entitlements\n
Attempting to send reply dictionary without valid reply port. Did you call xpc_dictionary_create_reply() or XPCDictionary.createReply()?
Debug
dictionary value verification failure
Attempt to set instance on a listening connection.
Peer forbidden (code signing)
Client
Data corruption: Invalid disposition in payload.
suspend is not allowed on this connection.
i24@?0r^v8r^v16
Versions/Current
send once
anonymous
Attempting to activate a canceling session
Service name is reserved or invalid
System service is not in system service allow list
Walking
dictionary key / value decoding failure
Publisher %s is removed by launchd
Reply messages must not be sent as notifications; use xpc_dictionary_send_reply()
Attempt to set the bs_checkin_info on a non-bs_type connection.
xpc_connection_set_peer_* family must be called no more than once
Kernel bug: The kernel cannot allocate memory needed for the pseudo-receive.
com.apple.xpc.anonymous.%p
Unreasonably large name
_UIApplicationDelegateClass
Client returned invalid action for dictionary container start event
stream
Client is gone
bundle %s missing from disk and dyld shared cache
<CHECK-IN>
B16@?0^{?={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}{der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}II^v}8
Attempting to select a data value from a non-data DER object
der_vm_execute_string_prefix_value_allowed
disable
Attempt to send a message expecting a reply to the wrong connection.
checked-allocations
com.apple.xpc.activity.control
/System/Library/CoreServices/SystemVersion.plist
wait
B40@?0^{dispatch_data_s=}8Q16r^v24Q32
Could not create subscription for stream/event/subscriber: %s/%s/%d: %d: %s
Connection init failed at listener activation with error %d - %s
Data corruption: clock_gettime_nsec_np failed or is unreasonably far in the future
!-_;./?
%s. Reason: %s
v12@?0i8
request
event publisher must be cancelled to be disposed
contents =\n
XPCServices
<%s: %s %s>
Unknown string encoding
Configuration error: unreasonably large PID or execcnt
Attempt to set privileged bit on a connection targetting a specific user.
XPC Dictionary is not a message
Contents
Operation only supported on development builds
com.apple.xpc.activity.%s
recursion limit reached
unidomain
Could not get entitlements for stream/token: %s/%llu: %d: %s
connection must be internal lifecycle.
XPCExtensionBundleVersion
Attempting to send a message using a session that is neither active or canceled.
XPC_FLAGS
B24@?0Q8^v16
all
Publisher %s was unable talk to launchd
Connection init failed at no-senders registration with error %d - %s
overlay
Listener
Attempting to select a string value from a non-string DER object
numeric string element not allowed
Client returned invalid action for simple element event
Not yet implemented
service-name
Attempt to set privileged bit on a live connection.
AMFI
Attempt to set instance on a live connection.
/usr/local/lib
Attempting to set privileged flag on connection to XPC Service.
Could not set event state: %s: %d: %s
job-handle
xml-looking blob was passed in
cwd
Attach handler is already NULL.
invalid dictionary element
Invalid Arguments
Attempt to enable termination-imminent event on a live connection.
, port = 0x%x, len = %llu (%llu pages)
XPCExtensionHostBundleIdentifier
Unsupported service stats version %d
_objectForActiveContext
Attempt to access an out-of-bounds index.
(anonymous)
%s.peer[%d]
__launchctl
v12@?0c8
*+
Underlying connection was invalidated
CFBundleExecutable
Unable to generate a fault: %d - %s
Could not get event name for stream/token: %s/%llu: %d: %s
XPCExtensionHostPID
bundle-id
bootstrap-error
jetsam-memlimit
Interval
Priority
additional-properties
com.apple.diagnosticd
Unreasonably large string
The evaluator doesn't do anything. Pass NULL.
r*12@?0c8
AllowBattery
Command
, transport = %d, dest port = 0x%x, dest msg id = 0x%llx, transaction = %d, voucher = %p
_UIApplicationMain
_manufacturingCallback
integer_allowed_iterate
Event stream listener got an error: %s
connection
_SequenceNumber
Flags
libdispatch bug: _recvp is still valid
%lli
origin
Cannot use xpc_mach_send_get_right and _xpc_mach_send_extract_right at the same time
Attempting to cancel an inactive session
Attempt to resolve populated bundle.
der_vm_integer_from_context
String contains an embedded NUL
Could not copy XPC event for stream/key: %s/%s: %d: %s
Attempt to change the sim-to-host mode on a live connection.
Query cannot be satisfied
xpc_telemetry
ondemand
validation-category
Verification failed
<%s: %p>: %llu
%s<%s>
DuetPowerBudgeting
RequiresClassB
checked in
%2.2x
set
__launchd
Configuration error: Invalid bootstrap port.
Reconnect failed at receive right creation with error %d - %s
Notification types other than dictionaries are not supported.
The specified service did not ship with the operating system
<%s: %p>: %s
activate is not allowed on this connection.
Kernel bug: mach_ports_lookup() failed.
XPC API Misuse: %s
Invalid property list
Request type is no longer supported
Result
<%s: %p> { name = %s, listener = %s, pid = %d, euid = %u, egid = %u, asid = %u }
Bug in libxpc: Could not create pipe to bootstrap server!
Data corruption: Out-of-line descriptor count is out-of-sync.
Contents/XPCServices
Unable to consume send-once notification, error = %d, msgh_id = %x
der_vm_data_from_context
recursivelyValidateEntitlements
Could not get bufsize for getpwnam_r(): %s
Configuration error: Invalid XPCService dictionary.
/private/preboot/Cryptexes/OS/
.xpc
binpref
Attempting to set entitlement matching value with unsupported value type: %s
DYLD_IMAGE_SUFFIX
Refusing to execute/trust quarantined program/file
foreground
unable to decode value size for key-value pair
must be called before _xpc_start_listeners
Attempting to send message using a session that's canceling
kill
Could not attach to service: %d: %s
Entitlements element not allowed
<%s: %p> { name = %s, mutgen = %llu, count = %zu, peak_count = %zu, 
Canceling
Canceled
Reconnect failed with error %d - %s
Unknown
token
readying
__TEXT
port
mach port
version
security.mac.amfi.developer_mode_resolved
This is not what you want to do.
Activation of a connection without an event handler.
PATH
/System/Library/Frameworks/
(dummy)
Cannot serialize an xpc_mach_send object and use _xpc_mach_send_extract_right at the same time
Listener must be inactive to %s, but listener is %s
(none)
Could not get uid for token: %llu: %d: %s
instances
handle
entitlements blob does not have CCDER_ENTITLEMENTS_DICT as the second element
der_decode_next
response
fifo
Bug in libxpc: Could not get bootstrap port.
Inactive
info plist = 
shmem
RandomInitialDelay
ShouldWakeDevice
libdispatch bug: Unexpected async reply reason.
set peer requirement
Resources/Info.plist
ActivityGroupName
set incoming session handler
Unable to convert LWCR dictionary to LWCR data
Out of order requests
array decoding failure
loaded
Could not set XPC event for stream/token/subscriber: %s/%llu/%d: %d: %s
, value = %lli
Domain is tearing down
com.apple.xpc
invalid populated entry
unthrottle
Automotive
, path = 
socket
/System/Library/PrivateFrameworks/
An XPC Service cannot be run directly.\n
v24@?0^v8r*16
Contents/Library/LoginItems
pre-exec
com.apple.system.logger
Normal message received by listener connection. Ignoring.
libdispatch bug: Multiple cancellation events delivered.
self
Attempt to set target session UID on a non-MachService connection.
outgsk
file transfer
An extension with the same bundle ID already exists with a different path
<%s: %p> { pid = %d }
ProductVersion
Configuration error: Bundle XPCService dictionary does not declare additional services.
ccat
XPC_EXIT_REASON_UNMANAGED
Attempt to create an endpoint out of an unsupported connection type.
Tried to create an XPC data with NULL bytes and %zu length
/usr/lib/system/libsystem_notify.dylib
Versions/Current/Resources
Messages must be dictionaries.
sanitizers
mount-point
Connection init failed with error %d - %s)
XPCServiceEndpointActive
Shared memory length exceeded size supported by a single memory entry (actual/supported): %llu/%llu
labels
com.apple.xpc.activity
_NSApplicationMain
UIApplicationMain
, name = %s
receive
Malformed bundle
Attempt to configure a service after it has been run.
Could not attach service: %d: %s
OK
<%s: %p> %s (approx)
leader-pid
0x%llx
Bug in libxpc: xpc_listener_t configured without session handler
resolved origin path = \"%s\",\n
NO
Domain creation with that UID is not allowed anymore
Repeating
RunLoopType
Configuration error: Service specifies NSApplicationMain() for run loop but AppKit is not available on this platform.
extension
Underlying connection interrupted
os_transaction: [%p] '%s', created %llu sec ago\n
Unknown error
Unexpected type to match against during iteration
Attempt to do a per-user lookup, but user sessions are not enabled.
Process is not managed
count
hostpid
(is running)
run
encountered invalid element in an array
could not decode tag for next DER sub-sequence
%s%s
Service cannot presently execute
jetsam-priority
Reconnect failed at lookup with error %d - %s
yesno
com.apple.xpc.bundle
<none>
_xpc_start_listeners may only be called once
Service cannot be loaded on this hardware
Session
API Misuse
dead-name
Unknown DER entitlements encoding
Message types other than dictionaries are not supported.
UTC Time element not allowed
<
$in
Security policy issue
Reconnect failed at no-senders registration with error %d - %s
Invalid format specifier!
get
double
Cannot force the listener to be both a MachService and a XPCService
List
<unknown>
Data corruption: Found unexpected non-XPC tagged pointer object
Attempting to activate a canceled session
The service was superseded by a later version
!(ready_only && (self->_type == XC_TYPE_PEER))
%d %s
Given object not of required type.
targetpid
v24@?0^{_xpc_connection_s=}8^v16
Data corruption: Malformed Mach message or kernel bug.
canceled
mach receive right
Kernel bug: Unexpected error from service attach port mach_port_construct()
dictionary decoding failure
xpc_connection_bs_seal_listener
Could not get uid for user %s: %s
Connection was released
Could not get attrs using %s for connection %s, pid %d: %d: %s
com.apple.session.queue
RequireScreenSleep
 }
.dylib
Multiple attempts to serialize a receive right.
events
Too many lookups were requested in one request
pointer
services = 
Invalid path
system
Attempt to set instance binpref on a MachService connection.
XPC_EXIT_REASON_SANDBOX_FILTERED_IPC
rec_execcnt
\t
asid
Reconnect failed at send right creation with error %d - %s
session_uid
Configuration error: UIKit does not exist.
%s(%s)
Contents/Resources
Out of memory
Configuration error: Specified subservice is disabled.
Attempt to append to a serializer created from the wire.
after SIGTERM
iterable decoding failure
libdispatch bug: Disconnect with invalid receive port
vers
eligible
Could not kickstart service: %d: %s
<%s: %p>
parent
bundle_identifier
Bug in libxpc: Unexpected platform
Active
Info.plist
This platform does not support bundles in other platforms' formats.
entitlements
Connection invalid
XPC_SERVICES_UNAVAILABLE
Could not attach to service: %d: %s:\n%s
Upload
CoreEntitlements: not a sequence
Kernel bug: MACH_SEND_NO_BUFFER returned for reliable message size.
XPCEventName
Cached XPC strings are immutable
Unable to activate listener: %s
Versions
CoreEntitlements: unknown DER type
\"
Out-of-bounds array insertion attempt.
event stream %s is already monitored
Finalizing BS connection
cmd
XPC_SERVICE_NAME
HOME
Couldn't retrieve XPCService dictionary from service bundle. Cause: %s
[<capacity = %u>\n
Invalid rest suffix for 'double' format specifier!
com.apple.listener.queue
xpc_pipe_create_with_user_session_uid() can only be used if xpc_user_sessions_enabled() returns true.
?>
RequireBatteryLevel
activity
v16@?0^v8
identifier
Cannot set TBD when from endpoint or anon.
/usr/lib/system/libsystem_info.dylib
(n/a)
Unknown data encoding
bootout-error
Bug in libxpc: Invalid audit token in bootstrap dictionary
Session must be inactive to set the cancel handler, not %s
Over-release of a transaction object.
com.apple.xpc.file_transfer.incoming
<transaction
Attempt to pass a malloc(3)ed region to xpc_shmem_create().
Could not signal service: %d: %s
<%s: %p>: null-object
Configuration error: Couldn't retrieve XPCService identifier from service bundle.
Running
der_vm_execute_match_string_prefix
der_decode_key_value
Can Retry: %d. Description:\"
Send once port already consumed
send_message_with_reply is not allowed with a non-launching Mach service
AutomotiveStationary
dictionary
validate_V0
Attempting to merge reply with non-received dictionary
Connection interrupted
, value = %llu
linked executable
archpref
XPC_EXIT_REASON_SIGTERM_TIMEOUT
xpc_connection_get_peer_instance() must be called on a peer connection.
%llu
pid
Out-of-bounds launch array insertion attempt.
Success
Disposing non-empty string cache
$query
Identifier
unhandled opcode
encountered invalid tag
__CF_USER_TEXT_ENCODING
Kernel bug: Could not obtain task bootstrap port.
serializer
Attempt to change the bs_type property on a live connection.
DoItLater
A memory allocation has failed
fd
CommunicatesWithPairedDevice
could not decode size for next DER sub-sequence
Attempt to set instance binpref on a live connection.
com.apple.xpc.telemetry
initial-load-completed
init-recv
Contents/Info.plist
Connection init failed at send right creation with error %d - %s
%s.%p
Unimplemented routine: %s
serverport
, (null)
TMPDIR
r*8@?0
B16@?0r*8
CLASSIC
Invalid rest suffix for 'fd' format specifier!
(consumed)
origin path = \"%s\",\n
[%s]: entitlements blob has unexpected version %lld\n
[\"%s\"] -> %p
, name = %s, type = %s, state = %s, cancelation = (%u, %s), mach = %s, privileged = %s, bssend = 0x%x, recv = 0x%x, send = 0x%x, pid = %d, euid = %u, egid = %u, asid = %u, channel: %s
%s: %d: %s
__xpcproxy
_debug
Data corruption: Attempted to deserialize an unknown type of object (the caller should have skipped it with _xpc_wire_length_from_wire_id
Release of last reference on a suspended connection.
bssendp
Attempt to set target session UID, but user sessions are not enabled.
_test
[]
service instance
xpc_connection_cancel()
Session must be inactive to set the message handler, not %s
Could not find specified domain
<%s: %p>: %f
Contents/Library/LaunchDaemons
cancel is not allowed on this connection.
An XPC service cannot be launched directly
string
Attempting to select a boolean value from a non-boolean DER object
kern.osproductversion
foreground_uid
XPCServiceEndpointEvent
(invalid path)
<%s: %p>: %llu bytes (%llu page%s)
loginwindow
activating
send
lwcr
LWCR requirement doesn't match: %s (%d)
Maintenance
<%s: %p> {\n
The specified service did not ship in the requestor's bundle
der_vm_execute_integer_value_allowed
non-launching
Attempt to modify a global dictionary.
Data corruption: Destructor set on inline object graph.
Remaining %d os_transaction + %d xpc_transaction_begin\n
Operation not permitted while System Integrity Protection is engaged
der_vm_execute_nocopy
com.apple.logd.events
instance
Bug in libxpc: _xpc_objc_main() is not supposed to return
Attempt to populate a non-inert bundle.
AutomotiveMoving
state
date
How does one look up a service owned by nobody?
Kernel bug: Unexpected error from pipe mach_port_construct()
array
check-in
name
string_prefix_allowed_iterate
<%s: %p>: { length = %lu bytes, contents = 
Peer Forbidden
Listener must be canceled before it's disposed
Domain is in on-demand-only mode
Could not configure service: %d: %s
init-term
Bug in libxpc: mach_port_construct() failed
userreboot_purpose
connection.c
Invalid rest suffix in dictionary element format specifier!
%s%s%s
The specified group does not exist
GracePeriod
Attempt to set the bs_checkin_info on a listener connection.
NetworkDownloadSize
request originated from a different execcnt
<%s: %p> { type = 
Failed to extend PID domain: %d: %s
error = %d,\n
Object is not an XPC object
dropped-count
exception
Attempt to get connection property with no connection and no target PID.
Completely unexpected error
NetworkEndpoint
Kernel bug: Misfired notification: port-deleted.
Configuration error: Bundle Info.plist has no CFBundleIdentifier.
Library/LoginItems
Cannot call _xpc_mach_send_extract_right twice
Incoming message to %s is dropped because incoming message handler isn't set
Contents/MacOS
pipe
Attempt to configure non-configurable service instance.
pid-version
init-send
Configuration error: Service specifies NSRunLoop for run loop but does not have class.
Bad subsystem destination for request
validate_VNext
character device
Configuration error: Bundle XPCService dictionary does not declare additional subservices.
origin type = %d,\n
s
Service cannot load in requested session
iteration over a non-iterable type
string_value_allowed_iterate
out-entitlements
XPCServiceEndpoints
DuetAttributeName
der_vm_execute_match_bool
Client returned invalid action for array container start event
Failed to check-in, peer may have been unloaded: mach_error=%x
dummy
Data corruption: Message buffer was shorter than mach_msg_header
>
amp
NetworkTransferDirection
Failed to disable path: code = %d: %s, %s
Attempt to grow an array to a smaller size.
bool
(bogus)
Configuration error: Service specifies UIApplicationMain() for run loop but does not have symbol.
NSExecutable
Release of a suspended connection.
Requested entry was cached
Endpoint is hidden
\" }
/Versions
completion_status
enable
Data corruption: Too many objects
rootport
Cannot create endpoint from invalid mach port.
DuetAttributeCost
Configuration error: XPCService is not a dictionary.
session
Attempt to extract a receive right multiple times from the same object. This is unsafe.
Codesigning issue
creator
out
invalid flags value %llu
mach send once right
LANG
quot
executable path = \"%s\",\n
AppRefresh
Attempt to fetch the bs_checkin_info on a non-peer connection.
req_pid
, count = %u
Reconnect failed with readying error with error %d - %s
service-ctl-reply-port
named
Configuration error: Bundle has no Info.plist
com.apple.xpc.transaction.sigterm
Attempt to set target session UID on a live connection.
XPC_EXIT_REASON_RESERVED
Encountered XPC object loop: %s
\"%s\" => 
Swap operation not supported: %d
Could not get bootstrap port: %d
Invalid rest suffix for 'bool' format specifier!
Bug in libxpc: unhandled error in session
(invalid descriptor)
environment
fds
NetworkUploadSize
der_vm_bool_from_context
key length is invalid
new
_xpc_get_service_instance failed
program
der_decode_string
_xpc_connection_set_event_handler_f called after connection activation
_xpc_connection_activate_if_needed
 (from wire)
Configuration error: Already have a main service listener.
Stationary
activated
Data corruption: looking up type for a bogus id
init-note
xpcservice-dict
listener
Configuration error: failed to fetch our own audit token
%s%s%s%s%s
reply must be from PID 1 [actual pid = %d]
service-port
(null)
, value = %s
Service cannot be loaded on current os variant
user
Bidirectional
_ReplyEndpoint
key-value pair contains extra elements
/usr/lib/system/libsystem_trace.dylib
%d.%d.%d
Dictionary mutated during iteration
Bogus event received by listener connection:\n%s
errors
Missing required format arg!
resolved = %d,\n
entitlements blob does not have CCDER_CONSTRUCTED_SET coding
libdispatch bug: Non-check-in message without context.
!(consume_suspend_cnt && ready_only)
uint64
, uuid = %s
encountered invalid element in an iterable
reqs
PreventsDeviceSleep
v8@?0
_TargetLocalDomain
string cache
, subtype = %d, count = %u
0
Invalid rest suffix for 'date' format specifier!
XPCExtensionXPCBundle
paths
der_vm_iterate_b
The system encountered a condition where behavior was undefined
Service cannot be loaded with current boot-args
Reentrancy avoided
RequiresBuddyComplete
der_vm_execute_select_index
XPC_EXIT_REASON_FAULT
Bogus check-in attempt. Ignoring.
libdispatch bug: Invalid reply-received event delivered.
set instance
Domain does not support specified action
init-ready
Kernel bug: Unexpected error from connection mach_port_construct()
jetsam-flags
MemoryIntensive
comp
<%s: %s>
der_vm_execute_match_integer
Can Retry: %d. Description:\"%s\"
, interval = %lli
Peer rejected with reason: %s
The specified username does not exist
XPC_NULL_BOOTSTRAP
Attempt to clear sent descriptors on an unpacked serializer.
missing root
Invalid or missing service identifier
error
Delay
CPUIntensive
Connection init failed at receive right creation with error %d - %s
Sealing is only possible for listeners.
%s
Multiple errors were returned; see stderr
ActivityGroupConcurrencyLimit
Kernel bug: Misfired notification: dead-name.
, hdr = %p, hdr size = %lu, graph = %p, graph sz = %lu, out-of-line = %s
Session must be inactive to %s, but session is %s
com.apple.xpc.file_transfer.outgoing
string decode failure
extra data at the end of element
xpc_user_sessions_get_foreground_uid() must not be called if xpc_user_sessions_enabled() is false
\n
dict
names
No Connection
resource-usage-blob
Data corruption: mach_port_destroy() called on send right referenced by an XPC object.
Invalid or missing Program/ProgramArguments
com.apple.xpc.service-instance
Utility
der_decode_data
mdns
(is registered)
Attempted to serialize xpc_data that is too large for what the wire protocol currently supports. Length was %zu and max supported is %u
Underlying connection extracted
(invalid)
taint = %s,\n
sub-sequence size is larger than sequence size
telemetry
, buff = %p, len = %lu
Configuration error: Bundle XPCService dictionary does not declare specified service name.
Attempting to activate a session in an unknown state
on activation of exit_when_clean
capacity
<%s: %p> { string cache = %p, length = %zu, contents = \"
RequireInexpensiveNetworkConnectivity
der_decode_number
[%p] Session created with Endpoint.
[%p] Connection invalidation received
[%p] Termination imminent. No more messages will be received on this session.
_xpc_activity_set_state: %{public}s (%p), %ld
assertion failure: \"_xpc_mach_port_close_recv(port, 0, ((void*)0))\" -> %llu
assertion failure: \"i < self->xb_count\" -> %llu
[%p] %{public}s connection: name=%{public}s publishToken=%{public}llu
xpc_activity_register: %{public}s, criteria: %{public}s
assertion failure: \"platform < _XPC_PLATFORM_COUNT\" -> %llu
assertion failure: \"(*__error())\" -> %llu
assertion failure: \"posix_spawnattr_setarchpref_np(psattr, self->xb_count, self->xb_cpu_types, self->xb_cpu_subtypes, ((void*)0))\" -> %llu
assertion failure: \"self->_state == XC_STATE_CANCELED\" -> %llu
[%p] failed to do a bootstrap look-up: xpc_error=%{errno}d
[%p] listener failed to create a send right: mach_error=%{mach.errno}x
assertion failure: \"error != ((void*)0)\" -> %llu
[%p] Session activated
assertion failure: \"(((port) != 0) && ((port) != ((mach_port_name_t) ~0)))\" -> %llu
assertion failure: \"_xpc_message_request_expects_reply(xmrq)\" -> %llu
assertion failure: \"__builtin___strlcpy_chk (new_buffer, sb->buffer, new, __builtin_object_size (new_buffer, 2 > 1 ? 1 : 0)) < new\" -> %llu
xpc_activity_set_criteria: %{public}s (%p), %{public}s
_xpc_activity_register: %{public}s (%p), %llu
_xpc_activity_dispatch: created connection %p for activity name %{public}s (%p), seqno %llu
_xpc_activity_begin_running: %{public}s (%p) seqno: %llu.
assertion failure: \"!xgd->_key_string_cache\" -> %llu
assertion failure: \"serializer->_graph_destructor == &_xpc_serializer_free\" -> %llu
assertion failure: \"idx < self->count\" -> %llu
assertion failure: \"((((struct _xpc_base_s *)(self))->_xo_flags & (((xpc_flags_t)(1U << 0)))) != 0)\" -> %llu
_xpc_activity_dispatch: %{public}s (%p): ignoring an activity with matching seqno because of reply connection mismatch %llu
_xpc_activity_dispatch: %{public}s (%{public}p): no references remain after unregistering old activity.
assertion failure: \"format[foi] == delimiter\" -> %llu
assertion failure: \"m_block\" -> %llu
[%p] Session created with XPC Service: %s
assertion failure: \"xhandle != ((void*)0)\" -> %llu
assertion failure: \"(*__error()) != 0\" -> %llu
assertion failure: \"self->state == XPC_FILE_TRANSFER_STATE_INIT\" -> %llu
assertion failure: \"self->state != XPC_FILE_TRANSFER_STATE_IN_PROGRESS\" -> %llu
assertion failure: \"change_fdguard_np(fd, ((void*)0), 0, &guard, guard_flags, &fd_flags)\" -> %{errno}d
assertion failure: \"self->_cancelation.reason\" -> %llu
assertion failure: \"self->_state == XL_STATE_CANCELED\" -> %llu
[%p] Peer session explicitly activated
xpc_activity_set_criteria: %{public}s (%p), there is a pending event, which contained seqno %llu. If next state is CHECK_IN, it will be dispatched. If next state is WAIT, it will be dropped.
_xpc_activity_dispatch: %{public}s (%{public}p): found an activity with seqno %llu older than the event's seqno %llu. Unregistering it.
_xpc_activity_dispatch: %{public}s (%p): An event was delivered before the process has checked in. Stashing pending_seqno %llu, transaction, endpoint
_xpc_activity_unregister: %{public}s %llu, last registration: %{bool}d
assertion failure: \"token != 0\" -> %llu
[%p] Connection returned listener port: 0x%x
assertion failure: \"!globals->remote_hooks\" -> %llu
assertion failure: \"packed == _xpc_spawnattr_binprefs_size(binprefs)\" -> %llu
assertion failure: \"!unmanaged\" -> %llu
_xpc_activity_set_state_from_cts: %{public}s (%p), set activity state to %ld
[%p] bs_checkin_info failed to decode
[%p] Listener created with name: %s
assertion failure: \"matched == (match_result.error_code == AICMR_MATCH)\" -> %llu
assertion failure: \"xpc_dictionary_get_count(self->properties)\" -> %llu
assertion failure: \"stats_out != ((void*)0)\" -> %llu
assertion failure: \"xp->_subtype == XPLD_TRANSPORT_MACH\" -> %llu
assertion failure: \"entry->num_inflight_msg >= count\" -> %llu
assertion failure: \"self->_wants_sigterm != 0\" -> %llu
[%p] Session created with Mach Service: %s
[%p] Listener canceled.
assertion failure: \"prefix_len > 0\" -> %llu
_xpc_activity_set_criteria: xpc_set_event %{public}s, %llu
_xpc_activity_dispatch: %{public}s (%p): found a activity with seqno %llu NEWER THAN than the event's seqno %llu. Doing nothing.
assertion failure: \"pthread_key_create(&_mig_tsd, ((void*)0))\" -> %llu
assertion failure: \"hooks->send_reply\" -> %llu
assertion failure: \"self->state == XPC_FILE_TRANSFER_STATE_IN_PROGRESS\" -> %llu
_xpc_activity_dispatch: lower half, activity name %{public}s (%p), seqno from top half was %llu
__XPC_ACTIVITY_CALLING_HANDLER__ returned from handler: %{public}s (%p), current state %ld, pending state %ld
assertion failure: \"self->xep_state == XPC_EVENT_PUBLISHER_CANCELLED\" -> %llu
[%p] Dropping check-in message due to code signing requirement: %s
assertion failure: \"self->_xo_xrefcnt == 1\" -> %llu
[%p] Anonymous listener created
[%p] Received object of unsupported type: %s
assertion failure: \"rc\" -> %{errno}d
assertion failure: \"cb != ((void*)0)\" -> %llu
Service Lookup
assertion failure: \"hooks->extension.cls\" -> %llu
assertion failure: \"error\" -> %llu
_xpc_activity_dispatch: xpc_connection_set_event_handler: %{public}s (%p): found an activity with matching seqno %llu
assertion failure: \"hooks->msg_dispose\" -> %llu
assertion failure: \"payload\" -> %llu
assertion failure: \"self->_dmsg != 0\" -> %llu
assertion failure: \"initial_state == XL_STATE_NEW\" -> %llu
[%p] Falling back to bootstrap_look_up() = %d, lp: 0x%x
assertion failure: \"self->_sent != 0\" -> %llu
assertion failure: \"reply\" -> %llu
[%p] Peer session rejected
xpc_activity_set_criteria: %{public}s (%p), setting state now to %ld
[%p] failed to register a no-senders notification: mach_error=%{mach.errno}x
[%p] invalidated after a failed reconnect
_xpc_activity_dispatch: %{public}s (%p): state is checking and criteria is checking. Calling _xpc_activity_set_criteria(...CHECK_IN)
[%p] invalidated because the client process (pid %d) either cancelled the connection or exited
[%p] Sealing failed to make send right.
assertion failure: \"checkin->recvp.disposition == 16\" -> %llu
assertion failure: \"self->_graph_destructor == 0\" -> %llu
[%p] Session canceled.
[%p] Disposing of listener
[%p] Error creating session for incoming peer: %s
assertion failure: \"(bool)strchr(\"])\", format[foi])\" -> %llu
[%p] Error activating session: %s
_xpc_activity_dispatch: beginning dispatch, activity name %{public}s, seqno %llu
__XPC_ACTIVITY_CALLING_HANDLER__: %{public}s (%p), current state %ld, pending state %ld
assertion failure: \"platform != _XPC_PLATFORM_DATA\" -> %llu
assertion failure: \"kr\" -> %llu
[%p] Disposing of session
[%p] Session created.
assertion failure: \"serializer->_ool_serialize_callback != ((void*)0)\" -> %llu
xpc_activity_set_criteria, lower half: %{public}s (%p), %{public}s
xpc_activity_set_criteria: %{public}s (%p): registration->pending_seqno %llu >= registration->seqno %llu; creating a pending event
xpc_activity_set_criteria: %{public}s (%p): clearing pending seqno %llu, endpoint, transaction
assertion failure: \"count_is_odd == 0\" -> %llu
[%p] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
[%p] Failed to verify check-in connection port was derived from the listener connection port (kr=%d, sandbox_message_filter_id=#%llx)
[%p] %{public}s connection: mach=%{bool}d listener=%{bool}d peer=%{bool}d name=%{public}s
[%p] '%s': Transaction created
os_transaction: '%{public}s', created %llu sec ago
assertion failure: \"io\" -> %llu
assertion failure: \"unmanaged\" -> %llu
assertion failure: \"!xgd->_ool_callback\" -> %llu
[%p] Sealing failed to init recv right.
[%p] Peer did not meet the code signing requirement. Cancelling the connection.
assertion failure: \"self->_sync != 0\" -> %llu
assertion failure: \"xpc_data_get_bytes_ptr_and_length(lwcr_data, &lwcr_bytes, &lwcr_size)\" -> %llu
_xpc_activity_dispose: %{public}s (%p) seqno: %llu, %{public}s
_xpc_activity_set_criteria: %{public}s (%p), %{public}s
assertion failure: \"(*__error()) != 9\" -> %llu
assertion failure: \"got_data\" -> %llu
assertion failure: \"self->count < self->max_capacity\" -> %llu
[%p] listener failed to activate: xpc_error=%{errno}d
[%p] Failed to derive connection port; error %#x
[%p] invalidated after a failed init
assertion failure: \"dbuff\" -> %llu
[%p] Received event on inactive Listener
assertion failure: \"olddepth <= xgd->_depth\" -> %llu
%s
assertion failure: \"entry != ((void*)0)\" -> %llu
[%p] Received message forbidden due to code signing requirement: %s
[%p] Failed listener activation: %s
assertion failure: \"self->file_transfer_id != 0\" -> %llu
assertion failure: \"guarded_close_np(fd, &guard)\" -> %{errno}d
assertion failure: \"self->_len > 0\" -> %llu
assertion failure: \"self->xep_state == XPC_EVENT_PUBLISHER_INACTIVE\" -> %llu
assertion failure: \"speclen > 0\" -> %llu
[%p] Session created from connection [%p]
[%p] Peer session extracted
Remaining transactions %s: %d (%d os_transaction + %d xpc_transaction_begin)%s
assertion failure: \"new >= sb->size * 2\" -> %llu
xpc_activity_set_criteria: %{public}s (%p): early return
assertion failure: \"((void*)0) == reply\" -> %llu
[%p] invalidated after the last release of the connection object
[%p] invalidated after a failed send of the check-in message: mach_error=%{mach.errno}x
assertion failure: \"needed\" -> %llu
assertion failure: \"sb->length < sb->size\" -> %llu
assertion failure: \"msgid_lo & (~0x00ffffffu)\" -> %llu
assertion failure: \"q != ((void*)0)\" -> %llu
assertion failure: \"connection == activity->reply_connection\" -> %llu
[%p] Re-initialization successful; calling out to event handler with XPC_ERROR_CONNECTION_INTERRUPTED
assertion failure: \"_xpc_message_request_get_transport(xmrq) == XMSG_TRANSPORT_REMOTE\" -> %llu
[%p] Received event on inactive Session
assertion failure: \"self->transport_start_writing == ((void*)0)\" -> %llu
assertion failure: \"event\" -> %llu
_xpc_activity_set_state: send new state to CTS: %{public}s (%p), %ld
assertion failure: \"existing == self\" -> %llu
assertion failure: \"xpc_get_type(subs) == (&_xpc_type_array)\" -> %llu
assertion failure: \"flat != ((void*)0) || dispatch_data_get_size(self->_ddata) == 0\" -> %llu
assertion failure: \"xmrq\" -> %llu
assertion failure: \"!_xpc_activity_is_unmanaged()\" -> %llu
assertion failure: \"dictionary\" -> %llu
assertion failure: \"hard_limit > 2\" -> %llu
assertion failure: \"ret == 0 && own_path_len != 0\" -> %llu
assertion failure: \"format[foi] == '}'\" -> %llu
[%p] '%s': Transaction released
assertion failure: \"variant != XPC_BUNDLE_VARIANT_NONE\" -> %llu
assertion failure: \"self->xep_token_cache\" -> %llu
[%p] A message is received from other than initial peer.
[%p] anonymous connection failed to decode send port
[%p] invalid checkin_info length : %zu
assertion failure: \"hooks->size == sizeof(*hooks)\" -> %llu
assertion failure: \"success\" -> %llu
assertion failure: \"((&activity->eligibility_changed_handlers)->lh_first == ((void*)0))\" -> %llu
_xpc_activity_end_running: %{public}s (%p) seqno: %llu.
assertion failure: \"xmrq->_transport == XMSG_TRANSPORT_REMOTE\" -> %llu
assertion failure: \"src->_depth == 0\" -> %llu
[%p] Channel returned listener port: 0x%x
[%p] bs_checkin_info failed to encode : %s
assertion failure: \"c_block\" -> %llu
[%p] Incoming message to %s from PID %d is dropped because incoming message handler isn't set
[%p] Listener activated
assertion failure: \"i <= os_transaction_count\" -> %llu
assertion failure: \"xmrq->_transport == XMSG_TRANSPORT_MACH\" -> %llu
[%p] Connection interruption received
[%p] Unable to generate a fault: %d - %s
[%p] Unexpected peer session state: %s
assertion failure: \"xpc_get_type(xdata) == (&_xpc_type_data)\" -> %llu
assertion failure: \"self->transport_cancel_writing == ((void*)0)\" -> %llu
__xpc_activity_unregister: %{public}s (%p) seqno: %llu, %{public}s
assertion failure: \"!xgd->_value_string_cache\" -> %llu
assertion failure: \"object\" -> %llu
assertion failure: \"binprefs\" -> %llu
assertion failure: \"self->_state == XS_STATE_NEW\" -> %llu
assertion failure: \"self->transaction != ((void*)0)\" -> %llu
assertion failure: \"error == 0 && (((reply_port) != 0) && ((reply_port) != ((mach_port_name_t) ~0)))\" -> %llu
_xpc_activity_dispatch: %{public}s (%p): found an activity with matching seqno %llu
[%p] bs_checkin_info is too big : %s
assertion failure: \"hooks->extension.xet\" -> %llu
assertion failure: \"self->_subtype == XPC_DICTIONARY_SUBTYPE_RECEIVED\" -> %llu
assertion failure: \"self->_state == XS_STATE_CANCELED\" -> %llu
NSObject
OS_xpc_shmem
OS_xpc_endpoint
OS_xpc_serializer
OS_xpc_mach_send_once
OS_xpc_string_cache
OS_xpc_service
OS_xpc_mach_send
OS_xpc_date
OS_xpc_data
OS_xpc_fd
OS_xpc_service_instance
OS_xpc_double
OS_xpc_string
OS_xpc_pipe
OS_xpc_activity
OS_xpc_listener
OS_xpc_uuid
OS_xpc_rich_error
OS_os_transaction
OS_xpc_session
OS_xpc_null
OS_xpc_bool
OS_xpc_file_transfer
OS_xpc_object
OS_xpc_connection
OS_xpc_dictionary
OS_xpc_mach_recv
OS_xpc_uint64
OS_xpc_payload
OS_xpc_event_publisher
OS_xpc_peer_requirement
OS_xpc_pointer
OS_xpc_array
OS_xpc_error
OS_xpc_bundle
OS_xpc_int64
run
isMemberOfClass:
retain
conformsToProtocol:
T#,R
isProxy
T@\"NSString\",R,C
UTF8String
allowsWeakReference
init
TQ,R
class
description
hash
isEqual:
performSelector:
performSelector:withObject:
performSelector:withObject:withObject:
retainCount
self
T@\"NSString\",?,R,C
autorelease
debugDescription
dealloc
superclass
drain
stringWithFormat:
stringWithUTF8String:
zone
respondsToSelector:
release
_xref_dispose
currentRunLoop
initWithUTF8String:
isKindOfClass:
retainWeakReference
^{_NSZone=}16@0:8
v16@0:8
@24@0:8:16
@32@0:8:16@24
@40@0:8:16@24@32
#16@0:8
B24@0:8:16
Vv16@0:8
B24@0:8@\"Protocol\"16
@\"NSString\"16@0:8
B24@0:8@16
B16@0:8
Q16@0:8
@16@0:8
B24@0:8#16
```
