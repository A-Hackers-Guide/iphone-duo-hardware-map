# `/usr/lib/system/libxpc.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 737,696 bytes.

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
assertion failure: \"self->_graph_destructor == 0\" -> %llu
assertion failure: \"speclen > 0\" -> %llu
assertion failure: \"(bool)strchr(\"])\", format[foi])\" -> %llu
[%p] Session created.
assertion failure: \"matched == (match_result.error_code == AICMR_MATCH)\" -> %llu
[%p] bs_checkin_info is too big : %s
[%p] listener failed to activate: xpc_error=%{errno}d
assertion failure: \"xmrq\" -> %llu
assertion failure: \"c_block\" -> %llu
assertion failure: \"reply\" -> %llu
assertion failure: \"variant != XPC_BUNDLE_VARIANT_NONE\" -> %llu
_xpc_activity_dispatch: %{public}s (%p): An event was delivered before the process has checked in. Stashing pending_seqno %llu, transaction, endpoint
assertion failure: \"entry != ((void*)0)\" -> %llu
[%p] Failed to derive connection port; error %#x
assertion failure: \"_xpc_message_request_get_transport(xmrq) == XMSG_TRANSPORT_REMOTE\" -> %llu
assertion failure: \"needed\" -> %llu
assertion failure: \"src->_depth == 0\" -> %llu
assertion failure: \"xpc_get_type(subs) == (&_xpc_type_array)\" -> %llu
[%p] Sealing failed to init recv right.
[%p] Dropping check-in message due to code signing requirement: %s
assertion failure: \"flat != ((void*)0) || dispatch_data_get_size(self->_ddata) == 0\" -> %llu
assertion failure: \"serializer->_ool_serialize_callback != ((void*)0)\" -> %llu
xpc_activity_register: %{public}s, criteria: %{public}s
assertion failure: \"error\" -> %llu
assertion failure: \"msgid_lo & (~0x00ffffffu)\" -> %llu
assertion failure: \"change_fdguard_np(fd, ((void*)0), 0, &guard, guard_flags, &fd_flags)\" -> %{errno}d
xpc_activity_set_criteria: %{public}s (%p), there is a pending event, which contained seqno %llu. If next state is CHECK_IN, it will be dispatched. If next state is WAIT, it will be dropped.
assertion failure: \"self->xep_state == XPC_EVENT_PUBLISHER_INACTIVE\" -> %llu
[%p] invalid checkin_info length : %zu
assertion failure: \"error != ((void*)0)\" -> %llu
assertion failure: \"((void*)0) == reply\" -> %llu
assertion failure: \"(*__error()) != 9\" -> %llu
[%p] invalidated after a failed init
assertion failure: \"self->transaction != ((void*)0)\" -> %llu
assertion failure: \"io\" -> %llu
_xpc_activity_begin_running: %{public}s (%p) seqno: %llu.
[%p] Received message forbidden due to code signing requirement: %s
assertion failure: \"posix_spawnattr_setarchpref_np(psattr, self->xb_count, self->xb_cpu_types, self->xb_cpu_subtypes, ((void*)0))\" -> %llu
%s
assertion failure: \"hooks->extension.xet\" -> %llu
[%p] Connection invalidation received
assertion failure: \"xpc_get_type(xdata) == (&_xpc_type_data)\" -> %llu
assertion failure: \"guarded_close_np(fd, &guard)\" -> %{errno}d
_xpc_activity_dispatch: %{public}s (%p): found an activity with matching seqno %llu
Service Lookup
assertion failure: \"self->_xo_xrefcnt == 1\" -> %llu
[%p] Disposing of session
[%p] Session created with Endpoint.
[%p] Session created from connection [%p]
[%p] Error activating session: %s
_xpc_activity_dispatch: %{public}s (%p): ignoring an activity with matching seqno because of reply connection mismatch %llu
__xpc_activity_unregister: %{public}s (%p) seqno: %llu, %{public}s
assertion failure: \"platform != _XPC_PLATFORM_DATA\" -> %llu
assertion failure: \"self->count < self->max_capacity\" -> %llu
[%p] invalidated because the client process (pid %d) either cancelled the connection or exited
[%p] %{public}s connection: mach=%{bool}d listener=%{bool}d peer=%{bool}d name=%{public}s
[%p] Peer did not meet the code signing requirement. Cancelling the connection.
[%p] '%s': Transaction created
assertion failure: \"existing == self\" -> %llu
assertion failure: \"(((port) != 0) && ((port) != ((mach_port_name_t) ~0)))\" -> %llu
assertion failure: \"self->_wants_sigterm != 0\" -> %llu
[%p] Received event on inactive Session
[%p] Listener canceled.
assertion failure: \"xpc_data_get_bytes_ptr_and_length(lwcr_data, &lwcr_bytes, &lwcr_size)\" -> %llu
_xpc_activity_register: %{public}s (%p), %llu
assertion failure: \"object\" -> %llu
[%p] Sealing failed to make send right.
assertion failure: \"self->_sent != 0\" -> %llu
[%p] Session created with Mach Service: %s
assertion failure: \"prefix_len > 0\" -> %llu
assertion failure: \"binprefs\" -> %llu
assertion failure: \"serializer->_graph_destructor == &_xpc_serializer_free\" -> %llu
assertion failure: \"pthread_key_create(&_mig_tsd, ((void*)0))\" -> %llu
assertion failure: \"dbuff\" -> %llu
assertion failure: \"_xpc_message_request_expects_reply(xmrq)\" -> %llu
assertion failure: \"self->state == XPC_FILE_TRANSFER_STATE_IN_PROGRESS\" -> %llu
assertion failure: \"xpc_dictionary_get_count(self->properties)\" -> %llu
xpc_activity_set_criteria: %{public}s (%p): registration->pending_seqno %llu >= registration->seqno %llu; creating a pending event
assertion failure: \"(*__error())\" -> %llu
assertion failure: \"count_is_odd == 0\" -> %llu
[%p] invalidated after the last release of the connection object
assertion failure: \"payload\" -> %llu
assertion failure: \"m_block\" -> %llu
[%p] Connection interruption received
[%p] Unable to generate a fault: %d - %s
assertion failure: \"connection == activity->reply_connection\" -> %llu
assertion failure: \"checkin->recvp.disposition == 16\" -> %llu
assertion failure: \"!globals->remote_hooks\" -> %llu
assertion failure: \"format[foi] == '}'\" -> %llu
[%p] Incoming message to %s from PID %d is dropped because incoming message handler isn't set
[%p] Error creating session for incoming peer: %s
assertion failure: \"rc\" -> %{errno}d
_xpc_activity_dispose: %{public}s (%p) seqno: %llu, %{public}s
_xpc_activity_dispatch: %{public}s (%p): found a activity with seqno %llu NEWER THAN than the event's seqno %llu. Doing nothing.
assertion failure: \"ret == 0 && own_path_len != 0\" -> %llu
assertion failure: \"hard_limit > 2\" -> %llu
assertion failure: \"i < self->xb_count\" -> %llu
[%p] bs_checkin_info failed to decode
[%p] failed to register a no-senders notification: mach_error=%{mach.errno}x
assertion failure: \"hooks->msg_dispose\" -> %llu
assertion failure: \"hooks->extension.cls\" -> %llu
assertion failure: \"self->file_transfer_id != 0\" -> %llu
[%p] Falling back to bootstrap_look_up() = %d, lp: 0x%x
[%p] Received object of unsupported type: %s
assertion failure: \"(*__error()) != 0\" -> %llu
assertion failure: \"!unmanaged\" -> %llu
_xpc_activity_dispatch: created connection %p for activity name %{public}s (%p), seqno %llu
assertion failure: \"!_xpc_activity_is_unmanaged()\" -> %llu
_xpc_activity_set_state: %{public}s (%p), %ld
assertion failure: \"self->_len > 0\" -> %llu
[%p] bs_checkin_info failed to encode : %s
os_transaction: '%{public}s', created %llu sec ago
assertion failure: \"self->_sync != 0\" -> %llu
assertion failure: \"self->transport_start_writing == ((void*)0)\" -> %llu
assertion failure: \"success\" -> %llu
assertion failure: \"unmanaged\" -> %llu
assertion failure: \"event\" -> %llu
assertion failure: \"!xgd->_ool_callback\" -> %llu
assertion failure: \"idx < self->count\" -> %llu
assertion failure: \"((((struct _xpc_base_s *)(self))->_xo_flags & (((xpc_flags_t)(1U << 0)))) != 0)\" -> %llu
[%p] Session created with XPC Service: %s
[%p] Listener created with name: %s
[%p] '%s': Transaction released
assertion failure: \"self->state != XPC_FILE_TRANSFER_STATE_IN_PROGRESS\" -> %llu
assertion failure: \"stats_out != ((void*)0)\" -> %llu
assertion failure: \"got_data\" -> %llu
assertion failure: \"self->xep_token_cache\" -> %llu
assertion failure: \"self->_state == XS_STATE_NEW\" -> %llu
[%p] Session activated
[%p] Anonymous listener created
[%p] Peer session rejected
[%p] Unexpected peer session state: %s
assertion failure: \"i <= os_transaction_count\" -> %llu
assertion failure: \"xp->_subtype == XPLD_TRANSPORT_MACH\" -> %llu
assertion failure: \"self->transport_cancel_writing == ((void*)0)\" -> %llu
xpc_activity_set_criteria: %{public}s (%p): early return
xpc_activity_set_criteria: %{public}s (%p), setting state now to %ld
_xpc_activity_dispatch: lower half, activity name %{public}s (%p), seqno from top half was %llu
_xpc_activity_set_state: send new state to CTS: %{public}s (%p), %ld
assertion failure: \"xmrq->_transport == XMSG_TRANSPORT_REMOTE\" -> %llu
assertion failure: \"olddepth <= xgd->_depth\" -> %llu
assertion failure: \"dictionary\" -> %llu
[%p] A message is received from other than initial peer.
assertion failure: \"hooks->size == sizeof(*hooks)\" -> %llu
assertion failure: \"((&activity->eligibility_changed_handlers)->lh_first == ((void*)0))\" -> %llu
_xpc_activity_dispatch: %{public}s (%{public}p): no references remain after unregistering old activity.
__XPC_ACTIVITY_CALLING_HANDLER__: %{public}s (%p), current state %ld, pending state %ld
assertion failure: \"token != 0\" -> %llu
[%p] Connection returned listener port: 0x%x
[%p] failed to do a bootstrap look-up: xpc_error=%{errno}d
[%p] listener failed to create a send right: mach_error=%{mach.errno}x
[%p] %{public}s connection: name=%{public}s publishToken=%{public}llu
assertion failure: \"hooks->send_reply\" -> %llu
assertion failure: \"q != ((void*)0)\" -> %llu
assertion failure: \"error == 0 && (((reply_port) != 0) && ((reply_port) != ((mach_port_name_t) ~0)))\" -> %llu
assertion failure: \"platform < _XPC_PLATFORM_COUNT\" -> %llu
[%p] Failed to verify check-in connection port was derived from the listener connection port (kr=%d, sandbox_message_filter_id=#%llx)
Remaining transactions %s: %d (%d os_transaction + %d xpc_transaction_begin)%s
assertion failure: \"self->state == XPC_FILE_TRANSFER_STATE_INIT\" -> %llu
_xpc_activity_end_running: %{public}s (%p) seqno: %llu.
_xpc_activity_dispatch: beginning dispatch, activity name %{public}s, seqno %llu
_xpc_activity_dispatch: %{public}s (%{public}p): found an activity with seqno %llu older than the event's seqno %llu. Unregistering it.
_xpc_activity_set_state_from_cts: %{public}s (%p), set activity state to %ld
[%p] Peer session explicitly activated
assertion failure: \"sb->length < sb->size\" -> %llu
xpc_activity_set_criteria, lower half: %{public}s (%p), %{public}s
_xpc_activity_dispatch: %{public}s (%p): state is checking and criteria is checking. Calling _xpc_activity_set_criteria(...CHECK_IN)
_xpc_activity_unregister: %{public}s %llu, last registration: %{bool}d
assertion failure: \"self->xep_state == XPC_EVENT_PUBLISHER_CANCELLED\" -> %llu
[%p] Re-initialization successful; calling out to event handler with XPC_ERROR_CONNECTION_INTERRUPTED
assertion failure: \"initial_state == XL_STATE_NEW\" -> %llu
assertion failure: \"cb != ((void*)0)\" -> %llu
_xpc_activity_dispatch: xpc_connection_set_event_handler: %{public}s (%p): found an activity with matching seqno %llu
assertion failure: \"!xgd->_key_string_cache\" -> %llu
[%p] anonymous connection failed to decode send port
assertion failure: \"self->_dmsg != 0\" -> %llu
assertion failure: \"self->_state == XS_STATE_CANCELED\" -> %llu
[%p] Received event on inactive Listener
assertion failure: \"new >= sb->size * 2\" -> %llu
xpc_activity_set_criteria: %{public}s (%p): clearing pending seqno %llu, endpoint, transaction
_xpc_activity_set_criteria: %{public}s (%p), %{public}s
[%p] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
[%p] invalidated after a failed reconnect
[%p] invalidated after a failed send of the check-in message: mach_error=%{mach.errno}x
assertion failure: \"self->_subtype == XPC_DICTIONARY_SUBTYPE_RECEIVED\" -> %llu
[%p] Session canceled.
xpc_activity_set_criteria: %{public}s (%p), %{public}s
assertion failure: \"!xgd->_value_string_cache\" -> %llu
assertion failure: \"entry->num_inflight_msg >= count\" -> %llu
assertion failure: \"packed == _xpc_spawnattr_binprefs_size(binprefs)\" -> %llu
assertion failure: \"self->_state == XC_STATE_CANCELED\" -> %llu
[%p] Termination imminent. No more messages will be received on this session.
assertion failure: \"self->_state == XL_STATE_CANCELED\" -> %llu
_xpc_activity_set_criteria: xpc_set_event %{public}s, %llu
__XPC_ACTIVITY_CALLING_HANDLER__ returned from handler: %{public}s (%p), current state %ld, pending state %ld
[%p] Channel returned listener port: 0x%x
assertion failure: \"format[foi] == delimiter\" -> %llu
assertion failure: \"xhandle != ((void*)0)\" -> %llu
[%p] Peer session extracted
assertion failure: \"__builtin___strlcpy_chk (new_buffer, sb->buffer, new, __builtin_object_size (new_buffer, 2 > 1 ? 1 : 0)) < new\" -> %llu
assertion failure: \"kr\" -> %llu
assertion failure: \"xmrq->_transport == XMSG_TRANSPORT_MACH\" -> %llu
assertion failure: \"_xpc_mach_port_close_recv(port, 0, ((void*)0))\" -> %llu
[%p] Disposing of listener
[%p] Failed listener activation: %s
[%p] Listener activated
assertion failure: \"self->_cancelation.reason\" -> %llu
OS_xpc_shmem
OS_xpc_pipe
OS_xpc_payload
OS_xpc_object
OS_xpc_pointer
OS_xpc_serializer
OS_xpc_event_publisher
OS_xpc_connection
OS_xpc_service
OS_xpc_double
OS_xpc_fd
OS_xpc_mach_send
OS_xpc_endpoint
OS_xpc_error
OS_xpc_activity
NSObject
OS_xpc_service_instance
OS_xpc_file_transfer
OS_xpc_mach_send_once
OS_xpc_rich_error
OS_xpc_int64
OS_os_transaction
OS_xpc_session
OS_xpc_null
OS_xpc_date
OS_xpc_uuid
OS_xpc_mach_recv
OS_xpc_string_cache
OS_xpc_uint64
OS_xpc_peer_requirement
OS_xpc_string
OS_xpc_array
OS_xpc_dictionary
OS_xpc_bool
OS_xpc_data
OS_xpc_bundle
OS_xpc_listener
conformsToProtocol:
currentRunLoop
debugDescription
drain
retain
self
stringWithFormat:
dealloc
isMemberOfClass:
stringWithUTF8String:
superclass
T#,R
release
run
allowsWeakReference
respondsToSelector:
UTF8String
class
initWithUTF8String:
performSelector:
retainCount
T@\"NSString\",?,R,C
TQ,R
T@\"NSString\",R,C
autorelease
isKindOfClass:
performSelector:withObject:
isProxy
_xref_dispose
description
hash
isEqual:
retainWeakReference
init
performSelector:withObject:withObject:
zone
B24@0:8#16
Vv16@0:8
B24@0:8@\"Protocol\"16
#16@0:8
B16@0:8
Q16@0:8
^{_NSZone=}16@0:8
v16@0:8
B24@0:8@16
@16@0:8
@24@0:8:16
@32@0:8:16@24
@40@0:8:16@24@32
B24@0:8:16
@\"NSString\"16@0:8
send
Service is disabled
v8@?0
Unknown data encoding
subscriber-pid
bssendp
user
CEValidateWithOptions
Canceling event publisher for %s because of error: %d - %s
Attempt to enable termination-imminent event on a live connection.
Attempting to create peer requirement with invalid type: %s
The specified path is not a bundle
Kernel bug: Unexpected error from connection mach_port_construct()
get
could not decode size for next DER sub-sequence
Out-of-bounds array insertion attempt.
readying
The executable did not ship in the bundle
der_vm_integer_from_context
rec_execcnt
xpc_user_sessions_get_foreground_uid() must not be called if xpc_user_sessions_enabled() is false
contents =\n
, path = 
Cannot force the listener to be both a MachService and a XPCService
DuetAttributeValue
der_validate_dictionary
Data corruption: Invalid out-of-line descriptor specified.
activity
base
XPC_EXIT_REASON_UNMANAGED
xpc_pipe_create_with_user_session_uid() cannot be used with the privileged flag.
YES
bool
Reconnect failed at send right creation with error %d - %s
Attempt to set non-bundled on a live connection.
new
session
Contents
Reentrancy avoided
Array mutated during iteration
parent
Connection was released
<%s: %p>: { length = %lu bytes, contents = 
outgsk
Configuration error: Specified subservice is disabled.
Session manually canceled
Configuration error: Nonexistent bundle layout was resolved.
Send once port already consumed
<%s: %p>: %llu
xpc_pipe_create_with_user_session_uid() can only be used if xpc_user_sessions_enabled() returns true.
system
Could not get uid for user %s: %s
init-recv
__CF_USER_TEXT_ENCODING
%lu: 
Configuration error: Couldn't retrieve XPCService identifier from service bundle.
B16@?0^{?={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}{der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}II^v}8
mach port
, 
_profile
com.apple.system.notification_center
XPCExtensionPath
foreground
Debug
der_vm_iterate_b
encountered invalid element in an array
Attempt to set the bs_checkin_info on a non-bs_type connection.
_UIApplicationDelegateClass
subsetport
__launchd
.dylib
Cannot call _xpc_mach_send_extract_right twice
-->
(null)
DataBudgeting
recursion limit reached
\"%s\" => 
double
int64
set peer requirement
Configuration error: failed to fetch our own audit token
team-identifier-for-current-process
Service cannot presently execute
der_decode_numeric_string
Failed to disable path: code = %d: %s, %s
Attempt to pass a malloc(3)ed region to xpc_shmem_create().
version
Info.plist
DuetRelatedApplications
recursivelyValidateEntitlements
UTC Time element not allowed
Could not get entitlements for stream/token: %s/%llu: %d: %s
Bug in libxpc: Unexpected platform
Extracted
Attempt to populate an unknown bundle type.
Client returned invalid action for array container end event
activated
/usr/lib/system/libsystem_info.dylib
, port = 0x%x, len = %llu (%llu pages)
Configuration error: Bundle XPCService dictionary does not declare specified subservice.
Client returned invalid action for array container start event
_xpc_connection_init
B24@?0r*8^v16
The service was superseded by a later version
ProductVersion
B40@?0^{dispatch_data_s=}8Q16r^v24Q32
endpoint
<%s: %s>
xpc_telemetry
uuids
canceled
, name = %s, count = %zu
!-_;./?
NSString
invalid tag or length
%d.%d.%d
Service cannot be loaded with current boot-args
unthrottle
Unexpected type to match against during iteration
response
Reconnect failed at listener activation with error %d - %s
must be called before _xpc_start_listeners
string_value_allowed_iterate
connection must be a listener.
%s: %d: %s
rootport
HOME
Invalid rest suffix for 'date' format specifier!
Priority
bootstrap port must lead to PID 1 [actual pid = %d]
Could not get event name for stream/token: %s/%llu: %d: %s
, subtype = %d, count = %u
Bug in libxpc: No port given.
A complete hack
RunOnAppForeground
der_vm_execute_select_index
com.apple.logd.events
Client returned invalid action for simple element event
activating
CFFIXED_USER_HOME
serializer
security.mac.amfi.developer_mode_resolved
loginwindow
Configuration error: Service specifies UIApplicationMain() for run loop but does not have symbol.
XPCExtensionHostBundleIdentifier
Requested entry was cached
attrs
libdispatch bug: _recvp is still valid
Configuration error: Bundle XPCService dictionary does not declare additional services.
Kernel bug: mach_ports_lookup() failed.
labels
\"
Connection init failed at listener activation with error %d - %s
Too many lookups were requested in one request
dead-name
%s%s%s
origin type = %d,\n
Sandbox restriction
RequireHDDSpinning
Reconnect failed at lookup with error %d - %s
Attempt to set privileged bit on a connection targetting a specific user.
reqs
The specified service did not ship with the operating system
The specified service path was not in the service cache
der_vm_execute_match_string_prefix
Client returned invalid action for dictionary container end event
Connection interrupted
%s.%s
euid of PID 1 must be 0
data
Kernel bug: Unexpected error from service attach port mach_port_construct()
Attempt to send a message expecting a reply to the wrong connection.
, value = %p
%s(%s)
listener
LWCR invalid: %s
Attempting to set entitlement matching value with unsupported value type: %s
The specified group does not exist
program
...
ds
uid
Success
bundle %s missing from disk and dyld shared cache
ShouldWakeDevice
Unexpected type to match against
security.mac.amfi.developer_mode_status
Could not copy XPC event for stream/key: %s/%s: %d: %s
dummy
ActivityGroupName
der_decode_next
Constraint too large
Client returned invalid action for dictionary container start event
Service is already active
_UIApplicationClass
linked info.plist
, buff = (unmapped), len = %lu
date
CoreEntitlements: unknown DER type
der_vm_string_from_context
while trying to exit cleanly
Refusing to execute/trust quarantined program/file
configurable
Release of last reference on a suspended connection.
Messages must be dictionaries.
Could not create subscription for stream/event/subscriber: %s/%s/%d: %d: %s
xpc_connection_get_peer_instance() must be called on a peer connection.
Finalizing BS connection
Attempt to change the bs_type property on a live connection.
resume is not allowed on this connection.
peer
serverport
Invalid disposition
Invalid format specifier!
error
Attempt to get connection property with no connection and no target PID.
identifier
Invalid rest suffix for 'int{64}' format specifier!
Canceling
AMFI
Data corruption: Reply handler block scheduled with NULL reply.
NSAutoreleasePool
/usr/local/lib
Unsupported service stats version %d
unidomain
mount-point
.xpc
DuetAttributeName
Over-resume of a connection.
Attempt to get connection property before it was populated.
cancel is not allowed on this connection.
%s. Reason: %s
Domain is in on-demand-only mode
der_vm_execute_integer_value_allowed
request originated from a different execcnt
v24@?0^{_xpc_connection_s=}8^v16
MIG demux failed. This message ID is invalid: 0x%x
XPCServiceEndpointName
, fileport = 0x%x
DYLD_IMAGE_SUFFIX
Cannot serialize an xpc_mach_send object and use _xpc_mach_send_extract_right at the same time
overlay
iterable decoding failure
Reconnect failed at no-senders registration with error %d - %s
%s\n
bundle-id
Failed to extend PID domain: %d: %s
<%s: %p> {\n
executable path = \"%s\",\n
libdispatch bug: Multiple cancellation events delivered.
XPC_FLAGS
, hdr = %p, hdr size = %lu, graph = %p, graph sz = %lu, out-of-line = %s
failed to serialized value for key: %s
linked xpc services
ActivityGroupConcurrencyLimit
Unknown boolean encoding
<%s: %p> { count = %u, transaction: %d, 
resource-usage-blob
xpcservice-dict
Contents/Library/LaunchDaemons
/Versions
Service cannot load in requested session
v16@?0^v8
<%s: %p> { count = %u, capacity = %u, contents =\n
event stream %s is already monitored
Cannot set NONE when specifying checkin info.
%s.%p
/usr/lib
()
Peer image changed
Configuration error: Bundle Info.plist has no XPCService dictionary.
(n/a)
Completely unexpected error
_NSApplicationMain
Attempt to populate a non-inert bundle.
Connections cannot be directly embedded in messages. You must create an endpoint from the connection.
_xpc_start_listeners may only be called once
<%s: %p>: %p
sanitizers
ExpectedDuration
entitlements blob does not have CCDER_ENTITLEMENTS_DICT as the second element
array decoding failure
com.apple.logd
<%s>
named
%lli
Could not configure service: %d: %s
This platform does not support bundles in other platforms' formats.
service
xpc_user_sessions_get_foreground_uid() failed with error: %d - %s
number too large
_TargetLocalDomain
Attempt to create an endpoint out of an unsupported connection type.
gt
NetworkUploadSize
wait
Connection init failed at lookup with error %d - %s
xpc_connection_set_peer_* family must be called no more than once
directory
NO
The specified service did not ship in the requestor's bundle
Kernel bug: Could not obtain task bootstrap port.
v12@?0i8
(is registered)
_xpc_get_service_instance failed
Attempt to send non-message dictionary as reply
Bug in libxpc: _xpc_objc_main() is not supposed to return
<%s: %p> { name = %u, right = %s, urefs = %u }
Unable to generate a fault: %d - %s
NSRunLoop
_AdditionalServices
r*8@?0
Reply format must specify a dictionary!
pipe
/
pid-version
(bogus)
, name = %s, type = %s, state = %s, cancelation = (%u, %s), mach = %s, privileged = %s, bssend = 0x%x, recv = 0x%x, send = 0x%x, pid = %d, euid = %u, egid = %u, asid = %u, channel: %s
__launchctl
, list follows
bundle %s tainted with reason \"%s\"
Could not attach to service: %d: %s
completion_status
Extension objects cannot be serialized.
%llu
CoreEntitlements: Couldn't iterate over DER entitlements\n
dictionary key is not a valid string
Domain does not support specified action
XPC_EXIT_REASON_FAULT
Out-of-bounds launch array insertion attempt.
Could not get bufsize for getpwnam_r(): %s
Publisher %s was unable talk to launchd
DiskIntensive
Message:\n%s
Missing required format arg!
Incoming message to %s is dropped because incoming message handler isn't set
binpref
No Constraint provided
enable
Session
Attempt to extract a receive right multiple times from the same object. This is unsafe.
Bogus check-in attempt. Ignoring.
Termination imminent
XPC_SERVICES_UNAVAILABLE
Configuration error: Bundle XPCService dictionary does not declare additional subservices.
Invalid Arguments
Setting the target UID for a connection is not supported on embedded platforms.
Peer connection was rejected by the listener (%s)
set instance
reply must be from PID 1 [actual pid = %d]
[<capacity = %u>\n
, value = %s
Client is gone
, interval = %lli
This function, long deprecated, is no longer supported. Please stop using launch_data (or at least switch to launch_data_new_integer).
pointer
taint = %s,\n
Bad response from server
%a %b %d %T %Y %Z
validation-category
Bidirectional
der_vm_execute_match_integer
Data corruption: Teardown of an uninitialized connection.
Peer forbidden (code signing)
NetworkTransferDirection
der_vm_data_from_context
rich error
An XPC service cannot be launched directly
XPCService
info plist = 
Action not allowed on singleton service
fds
UserRequestedBackupTask
<CHECK-IN>
Bug in libxpc: Message larger than reliable size.
<%s: %p>
Reply messages must not be sent as notifications; use xpc_dictionary_send_reply()
Bug in libxpc: Invalid audit token in bootstrap dictionary
Unable to convert LWCR dictionary to LWCR data
Request for stale data
in
__xpcproxy
Over-release of a transaction object.
<%s: %p>: %lli
leader-pid
B24@?0Q8^v16
System service is not in system service allow list
(not registered)
Bad subsystem destination for request
Service cannot be loaded on current os variant
Remaining %d os_transaction + %d xpc_transaction_begin\n
origin path = \"%s\",\n
RequireSignificantUserInactivity
MayRebootDevice
NetworkEndpoint
der_decode_data
Out of memory
Session must be inactive to set the message handler, not %s
Bug in libxpc: mach_port_construct() failed
NSExecutable
(not running)
errors
monitor
Kernel bug: Misfired notification: dead-name.
Attempt to set privileged bit on a live connection.
, uuid = %s
com.apple.xpc.activity.control
Attempt to resolve populated bundle.
com.apple.xpc.anonymous.%p
Attempt to set instance binpref on a live connection.
activate is not allowed on this connection.
%2.2x
Permission denied
DoItLater
integer_allowed_iterate
<transaction
No Connection
Attempt to configure a service after it has been run.
send_message_with_reply is not allowed with a non-launching Mach service
An XPC Service cannot be run directly.\n
lt
missing root
jetsam-memlimit
kill
_SequenceNumber
<%s: %p>: %s
Data corruption: Attempted to deserialize an unknown type of object (the caller should have skipped it with _xpc_wire_length_from_wire_id
stream
Could not get attrs using %s for connection %s, pid %d: %d: %s
XPCExtensionBundleIdentifier
numeric string element not allowed
Unknown UTC Time encoding
Attempt to set target session UID on a privileged connection.
socket
receive
Unable to activate listener: %s
Contents/XPCServices
com.apple.xpc.transaction.sigterm
quot
\n
dictionary value verification failure
xpc_connection_bs_seal_listener
Tried to serialize an object containing a cycle
jetsam-flags
\t
Attempt to set instance binpref on a MachService connection.
Can't set event channel on peer connection
Path had bad ownership/permissions
Unreasonably large string
Configuration error: Service specifies NSRunLoop for run loop but does not have class.
PATH
v24@?0^v8r*16
<unknown>
Could not set XPC event for stream/key: %s/%s: %d: %s
Attempt to set the bs_checkin_info on a listener connection.
Invalid or missing Program/ProgramArguments
user/foreground/ specifier is not supported on this platform
port
Cached XPC strings are immutable
TMPDIR
'\"`~\\
Notification types other than dictionaries are not supported.
Shared memory length exceeded size supported by a single memory entry (actual/supported): %llu/%llu
com.apple.listener.queue
services = 
Domain is tearing down
Service cannot load in current boot environment
Attempting to select a boolean value from a non-boolean DER object
set target user session UID
RequiresClassC
Reconnect failed with readying error with error %d - %s
Path not searched for services
cwd
mdns
Upload
Identifier
launchd
targetpid
XPCServiceEndpointNeedsActivation
com.apple.xpc.file_transfer.incoming
Multiple errors were returned; see stderr
Data corruption: clock_gettime_nsec_np failed or is unreasonably far in the future
%s => 
Attempted to serialize xpc_data that is too large for what the wire protocol currently supports. Length was %zu and max supported is %u
Contents/Library/LoginItems
_ReplyEndpoint
req_pid
Event stream listener got an error: %s
capacity
Automotive
data element not allowed
libdispatch bug: Unexpected async reply reason.
Configuration error: Already have a main service listener.
Process is not managed
count
request
init-ready
XPC_CONTROL_USER_SESSIONS_INFO failed with error %d - %s
instances
der_vm_bool_from_context
Cannot set TBD when from endpoint or anon.
!ready_only
ingsk
/System/Library/Frameworks/
after SIGTERM
populated = %d,\n
Calling -init
Could not find specified service
XPCEventName
Unreasonably large name
com.apple.session.queue
Bogus domain object.
com.apple.launchd.service-stats-default
connection
signal
$query
suspend is not allowed on this connection.
, name = %s
Query cannot be satisfied
Attempt to set binpref on a connection without instance uuid.
, value = %llu
(invalid path)
Could not attach to service: %d: %s:\n%s
Interval
der_decode_key_value
disable
Reconnect failed with error %d - %s
, buff = %p, len = %lu
UIApplicationMain
on activation of exit_when_clean
run
set
, (null)
full graph sz = %zu, remaining = %zu, needed = %zu
CoreEntitlements: not a sequence
ccat
InvolvedProcesses
Tried to create an XPC data with NULL bytes and %zu length
, str = %s, len = %zu, string cache = %p
Bug in libxpc: Could not get bootstrap port.
XPC Dictionary is not a message
Configuration error: Bundle has no Info.plist
Unknown error
Service stub created
com.apple.libxpc.launchd
_test
Invalid rest suffix for 'fd' format specifier!
Session must be inactive to %s, but session is %s
reload-error
service-name
session_uid
bootstrap_lookup_children
cid
<%s: %p> { pid = %d }
Encountered XPC object loop: %s
XPCServiceEndpointEvent
Attempting to send message using a session that's canceling
AutomotiveStationary
cputypes
Could not set XPC event for stream/token/subscriber: %s/%llu/%d: %d: %s
Attempt to change the non-launching property on a live connection.
/usr/lib/system/libsystem_notify.dylib
The evaluator doesn't do anything. Pass NULL.
dict
unable to decode value size for key-value pair
token
Dictionary mutated during iteration
r*12@?0c8
Session must be inactive to extract the connection, not %s
unsupported type: %s
LWCR requirement doesn't match: %s (%d)
com.apple.xpc.activity.unmanaged
%s.peer[%d]
pid
RequireNetworkConnectivity
validate_V0
Configuration error: Service specifies NSApplicationMain() for run loop but AppKit is not available on this platform.
How does one look up a service owned by nobody?
Cannot set specific when not from endpoint.
XPC_EXIT_REASON_SIGTERM_TIMEOUT
This API is functionally useless.
Resources/Info.plist
iteration over a non-iterable type
Attempting to select a data value from a non-data DER object
dictionary key / value decoding failure
Versions/Current/Library/LoginItems
fd
Attempt to change the sim-to-host mode on a live connection.
com.apple.xpc.telemetry
creator
Running
AutomotiveMoving
Could not get asid for stream/token: %s/%llu: %d: %s
\t\"%s\" => %zu\n
<%s: %p>: %llu bytes (%llu page%s)
Command
Configuration error: Service specifies unknown RunLoopType.
yesno
Contents/Library/LaunchAgents
Failed to enable path: code = %d: %s, %s
invalid arguments passed in
<%s: %p>: null-object
_asan
Attempt to reset attach handler.
<no channel>
/System/Library/Frameworks/UIKit.framework/UIKit
_AdditionalSubServices
Cannot use xpc_mach_send_get_right and _xpc_mach_send_extract_right at the same time
>
monitor_id
Could not attach service: %d: %s
Data corruption: looking up type for a bogus id
<%s: %p> { name = 0x%x, right = %s }
_manufacturingCallback
Could not get attrs using %s for pid %d: %d: %s
Attempt to fetch the bs_checkin_info on a listener connection.
init-done
Invalid rest suffix for 'uint{64}' format specifier!
entitlements blob does not have CCDER_ENTITLEMENTS coding
XPC_EXIT_REASON_RESERVED
%s[%p]%s: { refcnt = %x, xrefcnt = %x
reqport
Operation only supported on development builds
Can Retry: %d. Description:\"
cryptex
B24@?0^v8Q16
Configuration error: Service does not have NSAutoreleasePool.
resolved origin path = \"%s\",\n
Not eligible for acceleration
Contents/Info.plist
Delay
[<count = %u>]
, count = %u
XPC_SERVICE_NAME
Attempt to append to a serializer created from the wire.
Inactive
Connection init failed with readying error with error %d - %s
Attempt to set target session UID on a live connection.
connection.c
Configuration error: Specified service name is disabled.
Check-in is too big : %zu
root path = \"%s\",\n
environment
/System/Library/PrivateFrameworks/
Could not get bootstrap port: %d
Attempting to activate a listener in an unknown state
Active
PreventsDeviceSleep
Peer Forbidden
Invalid rest suffix for 'bool' format specifier!
Versions/Current/Resources
linked executable
dropped-count
GracePeriod
der_decode_utc_time
Release of a suspended connection.
Attempt to modify a global dictionary.
ondemand
Listener must be inactive to %s, but listener is %s
Underflow of transaction count.
telemetry
Connection init failed with error %d - %s)
init-send
mach send right
vers
com.apple.system.logger
flags
Data corruption: Found unexpected non-XPC tagged pointer object
(is running)
der_decode_boolean
non-launching
Attempt to access an out-of-bounds index.
Session must be inactive to set the cancel handler, not %s
Can Retry: %d. Description:\"%s\"
Connection init failed at receive right creation with error %d - %s
uuid
__TEXT
(invalid)
AllowBattery
validate_VNext
lookup-handle
path
Unknown
]]>
der_decode_string
Attempt to set the bs_checkin_info on a peer connection.
<%s: %p> { type = 
Multiple attempts to serialize a receive right.
request originated from a different PID
origin
com.apple.xpc.transaction
Exclusive
NetworkParameters
/System/Library/CoreServices/SystemVersion.plist
file
Could not find a bundle of the given identifier through LaunchServices
Versions
error = %d,\n
_objectForActiveContext
(anonymous)
0
PostInstall
com.apple.xpc.activity
Subscribed to event %s using token %llu
Invalid rest suffix for 'double' format specifier!
Canceled
unable to decode value tag for key-value pair
Could not get uid for token: %llu: %d: %s
string cache
Null required format arg!
Underlying connection interrupted
Attempting to select an integer value from a non-integer DER object
xml-looking blob was passed in
[%s]: entitlements blob has unexpected version %lld\n
Verification failed
XPCErrorDescription
Attempting to activate a session in an unknown state
?>
invalid populated entry
<%s> { id = %lld, state = %d, transaction = %s }
Could not copy XPC event for stream/token/subscriber: %s/%llu/%d: %d: %s
0x%llx
Flags
key-value pair contains extra elements
send once
BUG IN (CLIENT OF?) LIBXPC: invalid disconnect oldsendp 0x%x, conn %s
/usr/lib/system/libsystem_trace.dylib
Disposing non-empty string cache
Data corruption: Destructor set on inline object graph.
string
jetsam-priority
der_vm_execute_string_prefix_value_allowed
B16@?0r*8
Unable to consume send-once notification, error = %d, msgh_id = %x
com.apple.xpc.bundle
Utility
[%s]: %s\n
Unknown numeric string encoding
Unknown DER entitlements encoding
Reconnect failed at receive right creation with error %d - %s
Bad context on connection port: notify: 0x%x self: %p pctx: %p recvp: 0x%x
Kernel bug: MACH_SEND_NO_BUFFER returned for reliable message size.
out-entitlements
Attempt to set instance on a listening connection.
(invalid descriptor)
Connection init failed at no-senders registration with error %d - %s
\" }
dispatch_main
os_transaction: [%p] '%s', created %llu sec ago\n
eligible
loaded
send_message_with_reply_sync is not allowed with a non-launching Mach service
cmd
entitlements
OK
Data corruption: Invalid disposition in payload.
token.pid
Sealing is only possible for listeners.
Configuration error: XPCService is not a dictionary.
Attempting to activate a canceling session
Operation not permitted while System Integrity Protection is engaged
Maintenance
libdispatch bug: Non-check-in message without context.
Codesigning issue
XPC_EXIT_REASON_ABANDONED
_xpc_connection_activate_if_needed
<%s: %p> %s
com.apple.diagnosticd
XPCExtensionPID
job-handle
hostpid
bootout-error
exception
anonymous
!(ready_only && (self->_type == XC_TYPE_PEER))
lwcr
suspended
Attempt to set instance on a live connection.
Out-of-line descriptor count is out-of-sync. Actual/expected: %lu/%lu
name
extra data at the end of element
Message types other than dictionaries are not supported.
/MacOS
Resources
%Y-%m-%dT%H:%M:%SZ
Attach handler is already NULL.
%d.%d
Swap operation not supported: %d
block device
Data corruption: Message buffer was shorter than mach_msg_header
archpref
mach send once right
asid
Attempt to set target session UID, but user sessions are not enabled.
Unimplemented routine: %s
Configuration error: Bundle Info.plist has no CFBundleIdentifier.
v20@?0^{dispatch_data_s=}8i16
, port = 0x%x
Invalid path
array
Client
der_vm_execute_nocopy
libdispatch bug: Disconnect with invalid receive port
Configuration error: Invalid XPCService dictionary.
%s
Invalid property list
com.apple.xpc.service-instance
NetworkDownloadSize
[%zu] -> %p
<
 (from wire)
<none>
libdispatch bug: _sendp is still valid
Bug in libxpc: _xpc_objc_uimain() is not supposed to return
%s%s
dictionary keys are not sorted or not unique
pre-exec
Data corruption: Out-of-bounds descriptor append attempt.
DuetAttributeCost
, %s
der_vm_execute_match_string
key contains an embedded NUL
could not decode tag for next DER sub-sequence
Attempt to grow an array to a smaller size.
enabled
checked-allocations
connection must be internal lifecycle.
Attempt to fetch the bs_checkin_info on a non-peer connection.
v12@?0c8
CPUIntensive
Walking
der_decode_entitlements
descriptor
event publisher must be cancelled to be disposed
Configuration error: Invalid bootstrap port.
self
Library/LoginItems
com.apple.xpc.activity.%s
}
Endpoint is hidden
handle
RandomInitialDelay
This is not what you want to do.
(dummy)
XPCExtensionHostPID
Listener must be canceled before it's disposed
Not yet implemented
der_vm_execute_select_key
Configuration error: unreasonably large PID or execcnt
Data corruption: Malformed Mach message or kernel bug.
<%s: %p> { name = %s, mutgen = %llu, count = %zu, peak_count = %zu, 
Attempt to clear sent descriptors on a serializer created from the wire.
extension
Cannot create endpoint from invalid mach port.
Malformed bundle
Security policy issue
__libxpcunittest
LANG
Invalid rest suffix in dictionary element format specifier!
Attempting to send message using a canceled session
Result
noop
bool decode failure
additional-properties
!(consume_suspend_cnt && ready_only)
Attempt to clear sent descriptors on an unpacked serializer.
unknown number encoding
<%s: %p> { string cache = %p, length = %zu, contents = \"
XPC_EXIT_REASON_UNKNOWN_IPC
[]
Session must be canceled before it's disposed
signing-identifier
Run
List
entitlements blob does not have CCDER_CONSTRUCTED_SET coding
libdispatch bug: Invalid reply-received event delivered.
Service name already exists
s
encountered invalid tag
%s%c
<%s: %p> { name = %s, listener = %s, pid = %d, euid = %u, egid = %u, asid = %u }
Given object not of required type. Given: %s, required: %s
check-in
Unknown string encoding
Attempting to send reply dictionary without valid reply port. Did you call xpc_dictionary_create_reply() or XPCDictionary.createReply()?
XPCExtensionBundleVersion
all
%s%s%s%s%s
DuetPowerBudgeting
Unknown service name
Cycling
string decode failure
Activation of a connection without an event handler.
<%s: %p> %s (approx)
Peer rejected with reason: %s
i24@?0r^v8r^v16
Configuration error: Bundle XPCService dictionary does not declare specified service name.
Bug in libxpc: unhandled error in session
$in
Request type is no longer supported
der_vm_execute_match_bool
%p
Contents/MacOS
Download
dictionary
/Contents
Versions/Current
<%s: %p> { name = %s }
Repeating
encountered invalid element in an iterable
event
init-note
out
Kernel bug: Unexpected error from pipe mach_port_construct()
der_validate_array
0x0
bootstrap-error
service-ctl-reply-port
MemoryIntensive
state
<%s: %p>: %f
comp
no value for key: %s
RequiresClassA
Could not find specified domain
Out of order requests
Couldn't retrieve XPCService dictionary from service bundle. Cause: %s
Attempting to activate a canceled session
Attempt to configure non-configurable service instance.
This SPI may not be called on non-configurable services.
userreboot_purpose
Could not get service identifier for token: %llu: %d: %s
Failed to check-in, peer may have been unloaded: mach_error=%x
Attempt to set instance binpref on a listening connection.
BUG IN CLIENT OF libxpc: attempt to create file transfer from unusual file type
The specified username does not exist
instance
XPC_NULL_BOOTSTRAP
invalid dictionary element
Could not kickstart service: %d: %s
XPCExtensionXPCBundle
%s<%s>
Publisher %s is removed by launchd
Normal message received by listener connection. Ignoring.
Bug in libxpc: invalid state passed to _xpc_session_message_error_during_cancelation()
String contains an embedded NUL
RunLoopType
Bug in libxpc: Could not create pipe to bootstrap server!
Data corruption: mach_port_destroy() called on send right referenced by an XPC object.
invalid flags value %llu
The system encountered a condition where behavior was undefined
RequiresBuddyComplete
XPC_EXIT_REASON_FAST_LOGOUT
Attempting to set privileged flag on connection to XPC Service.
bundle
file transfer
initial-load-completed
_xpc_connection_set_event_handler_f called after connection activation
%x
XPCEventStreamName
XPCServiceEndpoints
mach receive right
AppRefresh
Stationary
]
Routine not yet implemented
Data corruption: Too many objects
init-term
Given object not of required type.
Configuration error: UIKit does not exist.
set incoming session handler
apos
/private/preboot/Cryptexes/OS/
Object is not an XPC object
checked in
%svoucher = %p, 
%f
Domain creation with that UID is not allowed anymore
Invalid or missing service identifier
An extension with the same bundle ID already exists with a different path
sub-sequence size is larger than sequence size
Listener
<%s: %p> { id = %lld, state = %d, transaction = %s }
Requestor is not a platform binary
%d %s
/System/Cryptexes/OS/
XPC_EXIT_REASON_EXTENSION_CHECK_IN_TIMEOUT
Only peer connections have a filter policy
, value = %f
, value = %lli
null
service instance
[\"%s\"] -> %p
Kernel bug: Misfired notification: port-deleted.
Bogus event received by listener connection:\n%s
Data corruption: Out-of-line descriptor count is out-of-sync.
Requestor lacks required entitlement
CLASSIC
names
Could not signal service %s: %d: %s
Invalid payload transport for dictionary creation
Attempting to cancel an inactive session
xpc-fault
amp
RequiresClassB
key length is invalid
%s (backtrace follows)
Attempt to do a per-user lookup, but user sessions are not enabled.
bundle_identifier
Bug in libxpc: xpc_listener_t configured without session handler
(consumed)
Service does not support the specified action
DASData
xpc_connection_cancel()
Configuration error: Service does not have NSString.
__XPC_
Attempting to activate an already active session
Data corruption: CoreEntitlements has aborted due to an unrecoverable error
dictionary decoding failure
foreground_uid
/Contents/MacOS
Attempting to select a string value from a non-string DER object
Attempt to set the bs_checkin_info on a live connection.
_UIApplicationMain
XPC_DEBUG_SERVICES
CFBundleExecutable
MotionState
Entitlements element not allowed
Connection init failed at send right creation with error %d - %s
uint64
Contents/Resources
resolved = %d,\n
com.apple.xpc.file_transfer.outgoing
unhandled opcode
XPC_EXIT_REASON_SANDBOX_FILTERED_IPC
pid domain
API Misuse
XPCServiceEndpointActive
shmem
Kernel bug: The kernel cannot allocate memory needed for the pseudo-receive.
<%s: %s %s>
RequireInexpensiveNetworkConnectivity
NetworkTransferSize
key / value decoding failure
%d: [
*+
com.apple.xpc
XPC API Misuse: %s
Attempt to set target session UID on a non-MachService connection.
Underlying connection extracted
Attempting to activate an already active listener
character device
RequireBatteryLevel
CommunicatesWithPairedDevice
A memory allocation has failed
Connection invalid
der_vm_execute_select_longest_matching_key
boolean should be exactly 1 byte
events
service-port
_debug
(none)
Service cannot be loaded on this hardware
RequireScreenSleep
der_decode_number
bootstrap
xpc_user_sessions_get_session_uid() must not be called if xpc_user_sessions_enabled() is false
Could not signal service: %d: %s
Attempting to send a message using a session that is neither active or canceled.
paths
Unable to allocate reply port, possible port leak
type
der_vm_execute_string_value_allowed
Attempt to fetch the bs_checkin_info on a live connection.
libdispatch bug: Unexpected send result.
voucher = %p, 
XPCServices
Service name is reserved or invalid
Service cannot be launched because of BTM policy
PowerNap
kern.osproductversion
 }
Underlying connection was invalidated
true
, transport = %d, dest port = 0x%x, dest msg id = 0x%llx, transaction = %d, voucher = %p
string_prefix_allowed_iterate
fifo
Could not set event state: %s: %d: %s
Attempting to merge reply with non-received dictionary
false
```
