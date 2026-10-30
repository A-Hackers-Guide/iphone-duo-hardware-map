# `/System/DriverKit/usr/lib/system/libdispatch_profile.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 661,136 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 29 (Size: 2776)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (9)

- `/System/DriverKit/usr/lib/system/libdispatch_profile.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/System/DriverKit/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/System/DriverKit/usr/lib/system/libcompiler_rt.dylib (compatibility version 1.0.0, current version 103.4.0)`
- `/System/DriverKit/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.1)`
- `/System/DriverKit/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/System/DriverKit/usr/lib/system/libsystem_pthread.dylib (compatibility version 1.0.0, current version 553.40.2)`
- `/System/DriverKit/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/System/DriverKit/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/System/DriverKit/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Strings (517)

```
BUG IN CLIENT OF LIBDISPATCH: Release of a locked workloop
BUG IN LIBDISPATCH: Source finalized twice
BUG IN CLIENT OF LIBDISPATCH: Passing an invalid leeway
no ports
Command: %u, 
  %s\n
v12@?0i8
BUG IN LIBDISPATCH: do_dispose called
BUG IN CLIENT OF LIBDISPATCH: _dispatch_main_queue_callback_4CF called from the wrong thread
com.apple.libdispatch-io.streamq
BUG IN CLIENT of %s: Invalid workload interval type: %s (%hd)
, max qos %d
EVFILT_READ
BUG in libdispatch client: _dispatch_kevent_mach_msg_drain: dropped message too large to fit in memory: id = 0x%x, size = %u
BUG IN CLIENT OF LIBDISPATCH: Release of a workloop with corrupt state
BUG IN CLIENT OF LIBDISPATCH: Invalid size for the firehose buffer
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_deprecated
syslog
BUG IN CLIENT OF LIBDISPATCH: Cannot set width of a serial queue
, in-barrier
com.apple.root.default-qos
BUG IN CLIENT OF LIBDISPATCH: Changing target queue hierarchy after source was activated
API MISUSE: Voucher resurrection
BUG IN LIBDISPATCH: Manager queue invoked with kevent workqueue enabled
BUG IN CLIENT OF LIBDISPATCH: Unexpected EV_VANISHED (do not destroy random mach ports)
Changing the target of a queue already targeted by other dispatch objects
BUG IN CLIENT OF LIBDISPATCH: attribute's properties are invalid or meaningless on this system
bits <l %u, r %u
EVFILT_WRITE
BUG IN LIBDISPATCH: EVFILT_MACHPORT with no message size
BUG IN LIBDISPATCH: Corrupt unote action
%s[%p] = { 
queue_attr
com.apple.root.user-initiated-qos.overcommit
BUG IN LIBDISPATCH: Joined count underflowed
target = %s[%p], ident = 0x%llx, mask = 0x%x, pending_data = 0x%llx, registered = %d, armed = %d, %s%s%s
BUG IN LIBDISPATCH: Allocation should always fail
, activating
BUG IN CLIENT OF LIBDISPATCH: Reply received on unexpected port
os_workgroup_create_with_workload_id_and_workgroup
BUG IN CLIENT OF LIBDISPATCH: Waiter pushed onto manager
dispatch_mig_server: mach_msg() failed
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_mig_demux: mach_msg(MACH_SEND_MSG) failed
BUG IN LIBDISPATCH: Waking up a kq with cooperative thread request is not supported
BUG IN CLIENT OF LIBDISPATCH: Unable to make memory port
_os_workgroup_set_work_interval_workload_id
BUG IN LIBDISPATCH: Lingering DISPATCH_WLH_ANON
opts/err = 0x%x, msgh[%p] = { 
proc
EVFILT_WORKLOOP
mach_msg
BUG IN LIBDISPATCH: unexpected receipt of port-destroyed
BUG IN LIBDISPATCH: Don't try to wake up or override a root queue
BUG IN CLIENT OF LIBDISPATCH: Invalid source type
data-add
DISPATCH_EVFILT_CUSTOM_OR
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
com.apple.libdispatch-manager
BUG IN LIBDISPATCH: Unable to limit cooperative pool size
BUG IN CLIENT OF LIBDISPATCH: Over-resume of an inactive object
BUG IN CLIENT OF LIBDISPATCH: Cannot change the target of a queue already targeted by other dispatch objects
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_mig_demux_get_context not called from dispatch_mach_mig_demux context
BUG IN CLIENT OF LIBDISPATCH: Message already enqueued
LIBDISPATCH_TIMERS_FORCE_MAX_LEEWAY
BUG IN LIBDISPATCH: Missing Kevent WORKQ support
BUG IN LIBDISPATCH: Invalid wlh state
BUG IN LIBDISPATCH: Premature thread exit while a dispatch frame is active
Voucher: 0x%x has no contents\n
BUG IN LIBDISPATCH: firehose_push_reply should never be sent to the buffer receive port
BUG IN LIBDISPATCH: firehose_mig_server doesn't handle replies
stream
BUG in libdispatch client: %s %s{ 0x%llx[%s], ident: %lld / 0x%llx, handler: %p }
 (armed)
mach_recv (channel)
enable
DISPATCH_EVFILT_CUSTOM_REPLACE
BUG IN CLIENT OF LIBDISPATCH: Corruption: failed to clear bit exclusively
dispatch source activated with no event handler set
>, 
data-or
firehose
BUG IN LIBDISPATCH: dispatch_data_create_subrange out of bounds
runloop-queue
xref = %d, ref = %d, 
, enqueued
BUG IN LIBDISPATCH: Premature thread exit while a dispatch queue is running
, o 0x%x
com.apple.debug-channel
com.apple.root.background-qos
LIBDISPATCH_LOG
BUG IN LIBDISPATCH: Trailer format is invalid
BUG IN CLIENT OF LIBDISPATCH: Corrupt channel state
sock
stderr
BUG IN CLIENT OF LIBDISPATCH: invalid queue passed to dispatch_am_i_on_queue_4swiftonly()
BUG IN CLIENT OF LIBDISPATCH: Waking up an inactive workloop
deleted, 
BUG IN LIBDISPATCH: Deferred continuation on source, mach channel or mgr
BUG IN LIBDISPATCH: Underflow of tbkqwl count
BUG IN CLIENT OF LIBDISPATCH: Unable to create signal thread
BUG IN LIBDISPATCH: Premature thread exit with unhandled deferred items
BUG IN CLIENT OF LIBDISPATCH: A block object may not be both run more than once and observed
BUG IN LIBDISPATCH: Unexpected contents in DDI TSD
BUG IN CLIENT OF LIBDISPATCH: Start value is not DISPATCH_TIME_NOW or DISPATCH_TIME_FOREVER
BUG IN CLIENT OF LIBDISPATCH: Invalid workloop owner, possible memory corruption
Invalid voucher: 0x%x\n
BUG IN LIBDISPATCH: base voucher has non-zero activity value
v24@?0B8^{dispatch_data_s=[0{dispatch_object_s=[0{_os_object_s=^{_os_object_vtable_s}ii}]^{dispatch_object_vtable_s}ii^{dispatch_object_s}^{dispatch_queue_s}^v(?=^?^v)}][0{_os_object_s=^{_os_object_vtable_s}ii}]^{dispatch_data_vtable_s}ii^{
com.apple.root.user-interactive-qos
group
BUG in libdispatch client: %s %s: \"%s\" - 0x%x { 0x%llx[%s], ident: %lld / 0x%llx, handler: %p }
com.apple.libsystem.libdispatch
BUG IN CLIENT OF LIBDISPATCH: Cannot change label for this queue
delete
Join token provided is for a different thread
BUG IN CLIENT OF LIBDISPATCH: Use-after-free of dispatch_semaphore_t or dispatch_group_t
BUG IN CLIENT OF LIBDISPATCH: trying to lock recursively
BUG IN CLIENT OF LIBDISPATCH: Too many nested calls to dispatch_suspend()
BUG IN CLIENT OF LIBDISPATCH: Channel never connected
EVFILT_PROC
DISPATCH_EVFILT_TIMER
operation
BUG IN CLIENT OF LIBDISPATCH: dispatch_set_qos_class called on invalid object type
BUG IN CLIENT OF LIBDISPATCH: Release of a queue with corrupt state
needs-event, 
BUG IN CLIENT OF LIBDISPATCH: Message size too large
B40@?0^{dispatch_data_s=[0{dispatch_object_s=[0{_os_object_s=^{_os_object_vtable_s}ii}]^{dispatch_object_vtable_s}ii^{dispatch_object_s}^{dispatch_queue_s}^v(?=^?^v)}][0{_os_object_s=^{_os_object_vtable_s}ii}]^{dispatch_data_vtable_s}ii^{di
stopped, 
type = %s %s, fd = 0x%lx, fd_entry = %p, channel = %p, queue = %p -> %s[%p], target = %s[%p], offset = %lld, length = %zu, done = %zu, undelivered = %zu, flags = %u, err = 0x%x, low = 0x%zx, high = 0x%zx, interval%s = %llu 
BUG IN CLIENT of %s: Non-default attribute flags: 0x%x
BUG IN CLIENT OF LIBDISPATCH: dispatch_workloop os_workgroup_join failed
BUG IN CLIENT OF LIBDISPATCH: Attempt to set timer on a non-timer source
timer = { target = 0x%llx, deadline = 0x%llx, interval = 0x%llx, flags = 0x%x }, 
target = %s[%p], receive = 0x%x, send = 0x%x, send-possible = 0x%x%s, checkin = 0x%x%s, send state = %016llx, disconnected = %d, canceled = %d 
, flatbuf = %p 
%s%s%s
BUG IN CLIENT OF LIBDISPATCH: The executable is already multithreaded
Voucher: 0x%x\n
BUG IN CLIENT of %s: Non-default workload type: %s (%hd)
BUG IN LIBDISPATCH: Trailer doesn't contain filter policy id
os_workgroup_create_with_workload_id_and_port
BUG IN LIBDISPATCH: dq_activate called
BUG IN LIBDISPATCH: message received without expected trailer
API MISUSE: Over-release of an object
BUG IN LIBDISPATCH: _pthread_set_properties_self failed
BUG IN CLIENT OF LIBDISPATCH: Channel didn't call dispatch_channel_drain
BUG IN CLIENT OF LIBDISPATCH: Reply port needed for async send with reply
BUG IN CLIENT OF LIBDISPATCH: Failed to initalize workqueue kevent
com.apple.backboardd.hid
BUG IN LIBDISPATCH: Cannot turn a manager thread into a normal one
block
BUG IN CLIENT OF LIBDISPATCH: Memory corruption in the logging buffers
com.apple.libdispatch-io.dev_lockq
BUG IN LIBDISPATCH: none destructor called
NULL: 
BUG IN CLIENT of %s: Invalid workgroup port 0x%x
com.apple.root.workloop-custom.overcommit
BUG IN LIBDISPATCH: Invalid workgroup port
cancelled, 
BUG IN CLIENT OF LIBDISPATCH: Source is suspended
YES
BUG IN CLIENT OF LIBDISPATCH: dispatch_apply_attr not initialized using dispatch_apply_attr_init
BUG IN LIBDISPATCH: EVFILT_MACHPORT with no message
BUG in libdispatch client: %s, monitored resource vanished before the source cancel handler was invoked { %p[%s], ident: %d / 0x%x, handler: %p }
/var/tmp/libdispatch.%d.log
BUG IN LIBDISPATCH: Unexpected object type
BUG IN LIBDISPATCH: Locking the manager should not fail
BUG IN CLIENT OF LIBDISPATCH: Empty message
EVFILT_SOCK
}
BUG IN CLIENT OF LIBDISPATCH: 0 is an invalid threads_per_cluster value
com.apple.libdispatch-io.fd_lockq
_os_workgroup_join_update_wg
BUG IN CLIENT OF LIBDISPATCH: Unexpected error from kevent
com.apple.libdispatch-io.closeq
BUG IN LIBDISPATCH: dispatch_data_copy_region out of bounds
port = 0x%x, 
BUG IN CLIENT OF LIBDISPATCH: Source has a cancel handler
BUG IN CLIENT OF LIBDISPATCH: Do not close random Unix descriptors
BUG IN CLIENT OF LIBDISPATCH: sync waiter found on channel
BUG IN LIBDISPATCH: Interrupted drain on manager queue
EVFILT_SIGNAL
BUG IN CLIENT OF LIBDISPATCH: Voucher importance count underflow
os_workgroup_create_with_workload_id
semaphore
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_mach_client
, activated
BUG IN CLIENT OF LIBDISPATCH: Invalid queue type
com.apple.libdispatch-io.channelq
, dirty
BUG IN LIBDISPATCH: Pending thread request underflow
BUG IN LIBDISPATCH: Disposing of timer still in its heap
mach_send (mach)
BUG IN LIBDISPATCH: kqueue() failure
RESOURCE ACCOUNTING INFO: %s
type = %s, fd = 0x%lx, %sfd_entry = %p, queue = %p, target = %s[%p], barrier_queue = %p, barrier_group = %p, err = 0x%x, low = 0x%zx, high = 0x%zx, interval%s = %llu 
BUG IN CLIENT OF LIBDISPATCH: Workload identifier must not be NULL
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_wait()
BUG IN CLIENT: Thread exiting without leaving workgroup '%s'
=== log file opened for %s[%u] at %ld.%06u ===\n
BUG IN CLIENT of %s: Invalid attribute pointer
BUG IN LIBDISPATCH: inline destructor called
%sBlock was %sexpected to execute on queue [%s (%p)]
BUG IN CLIENT OF LIBDISPATCH: dispatch queue/source property setter called after activation
timer (fixed-clock)
Creating an os_workgroup of unknown type
Changing target queue hierarchy after xpc connection was activated
BUG IN CLIENT OF LIBDISPATCH: Unexpected non message event
(strict)
Setting registration handler after the source has been activated
read
BUG IN LIBDISPATCH: Unexpected error from mach recv
queue_concurrent
BUG IN LIBDISPATCH: Invalid way to wake up a workloop
apply
BUG IN CLIENT OF LIBDISPATCH: firehose_drain_notifications_once() failed
record[%zd] = { from = %zd, length = %zd, data_object = %p }, 
LIBDISPATCH_CONTINUATION_ALLOCATOR
com.apple.root.utility-qos.cooperative
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_kevent_vanished
IMPORTANCE INFO: %s
com.apple.libdispatch-io.opq
BUG IN CLIENT of %s: Workgroup already cancelled
com.apple.backboardd.displaythread
API MISUSE: Object type does not support suspension
BUG IN CLIENT OF LIBDISPATCH: Over-resume of an object
BUG IN LIBDISPATCH: Unregistration failed
nw_channel
DISPATCH_EVFILT_CUSTOM_ADD
com.apple.root.default-qos.overcommit
, pending-barrier
BUG IN CLIENT OF LIBDISPATCH: Dispatch source used after last release
kevent = %p%s, filter = %s }
 } }
BUG IN CLIENT OF LIBDISPATCH: Voucher port corruption
BUG IN LIBDISPATCH: Invalid values for MADVISE_CHUNK_COUNT / CHUNK_SIZE
v16@?0^{dispatch_fd_entry_s=i^{dispatch_io_path_data_s}iiiI{dispatch_stat_s=iS}[2^{dispatch_stream_s}]^{dispatch_disk_s}^{dispatch_queue_s}^{dispatch_queue_s}^{dispatch_group_s}^{dispatch_io_s}{?=^{dispatch_operation_s}^^{dispatch_operation
queue_mgr
mach
BUG IN CLIENT of %s: Unable to set kernel workload ID: %s (0x%x) -> %d (0x%x)
EVFILT_USER
BUG IN CLIENT OF LIBDISPATCH: dispatch_main called from a block on the main queue
BUG IN LIBDISPATCH: ulock_wake() failed
remote 0x%x
com.apple.root.libdispatch-manager
BUG IN LIBDISPATCH: Unexpected __ulock_wait error
BUG IN CLIENT OF LIBDISPATCH: Release of a suspended object
Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?
Content size: %u\n
BUG IN CLIENT OF LIBDISPATCH: pthread_start os_workgroup_join failed
count = %u, gen = %d, waiters = %d, notifs = %d }
, in-flight = %d
, thread = 0x%x 
BUG IN CLIENT OF LIBDISPATCH: workloop qos class or priority must be set before cpupercent
mach reply
cur_wg == NULL
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_send_with_result_and_wait_for_reply is XPC only
BUG IN LIBDISPATCH: Unexpected event
BUG IN CLIENT of %s: Mismatched workload ID and port interval type: %s vs %hd
v20@?0^{dispatch_data_s=[0{dispatch_object_s=[0{_os_object_s=^{_os_object_vtable_s}ii}]^{dispatch_object_vtable_s}ii^{dispatch_object_s}^{dispatch_queue_s}^v(?=^?^v)}][0{_os_object_s=^{_os_object_vtable_s}ii}]^{dispatch_data_vtable_s}ii^{di
BUG IN CLIENT OF LIBDISPATCH: Unable to allocate mach port
BUG IN CLIENT OF LIBDISPATCH: Used Swift only SPI to enqueue non-Swift runtime objects into dispatch
BUG IN CLIENT OF LIBDISPATCH: Invalid send flags
BUG IN LIBDISPATCH: base voucher has nested base voucher
BUG IN CLIENT OF LIBDISPATCH: Called drain twice in the same invoke
BUG IN LIBDISPATCH: Premature thread exit while a dispatch context is set
EVFILT_MACHPORT
BUG IN CLIENT OF LIBDISPATCH: Log is too large
BUG IN CLIENT OF LIBDISPATCH: Trying to handoff IPC from non IPC context
BUG IN LIBDISPATCH: Too many deferred free items
Changing the target of a source after it has been activated
EVFILT_MEMORYSTATUS
com.apple.root.maintenance-qos.overcommit
com.apple.root.user-initiated-qos.cooperative
workloop
BUG IN CLIENT OF LIBDISPATCH: Unsupported interface
BUG IN CLIENT OF LIBDISPATCH: dispatch_main() must be called on the main thread
BUG IN CLIENT OF LIBDISPATCH: Cannot specify an overcommit attribute and use this kind of target queue
Changing target queue hierarchy after source was activated
mach_notification
BUG IN CLIENT OF LIBDISPATCH: Group object deallocated while in use
data-replace
EVFILT_TIMER
BUG IN LIBDISPATCH: Broken priority
BUG IN LIBDISPATCH: Unable to get the unique pid (error)
disk
TRUE
API MISUSE: Resurrection of an over-released object
BUG IN CLIENT OF LIBDISPATCH: Not a runloop queue
<released queue, pending free>
BUG IN LIBDISPATCH: Root queue initialization failed
signal
monitor
%sBlock was expected to act as a barrier on queue [%s (%p)]
BUG IN LIBDISPATCH: QoS Maintenance support required
 (direct)
BUG in libdispatch client: dispatch_mach_send_and_wait_for_reply: dropped message too large to fit in memory: id = 0x%x, size = %u
BUG IN CLIENT OF LIBDISPATCH: kqueue() failure: process is out of file descriptors
com.apple.root.background-qos.cooperative
BUG IN CLIENT OF LIBDISPATCH: Semaphore object deallocated while in use (current value < original value)
BUG IN CLIENT OF LIBDISPATCH: Overlarge message received
Previous voucher: 0x%x, 
BUG IN DISPATCH: Invalid wi flags = %u
com.apple.root.user-interactive-qos.overcommit
<unknown>
BUG IN CLIENT of %s: Mismatched workload ID and workgroup interval type: %s vs %hd
BUG IN CLIENT OF LIBDISPATCH: Cannot target object to cooperative root queue - not implemented
Clearing handler after the source has been activated
BUG IN CLIENT OF LIBDISPATCH: Changing target queue hierarchy after mach channel was connected
EVFILT_missing
BUG IN CLIENT OF LIBDISPATCH: Cannot target the cooperative root queue - not implemented
BUG IN CLIENT OF LIBDISPATCH: unsupported vah_version
BUG IN CLIENT OF LIBDISPATCH: Unable to register with logd
queue_global
DEPRECATED USE in libdispatch client: %s; set a breakpoint on _dispatch_bug_deprecated to debug
BUG IN CLIENT OF LIBDISPATCH: Corruption of dispatch block object
BUG IN LIBDISPATCH: mach semaphore API failure
id 0x%x, 
BUG IN CLIENT OF LIBDISPATCH: Unexpected EV_VANISHED (do not destroy random mach ports or file descriptors)
MIG_REPLY_MISMATCH
BUG IN CLIENT OF LIBDISPATCH: Channel already connected
BUG IN CLIENT OF LIBDISPATCH: Changing target queue hierarchy after xpc connection was activated
BUG IN LIBDISPATCH: Invalid kevent priority
EVFILT_VNODE
queue_main
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_notify()
LIBDISPATCH_COOPERATIVE_POOL_STRICT
LIBDISPATCH_DISABLE_KEVENT_WQ
BUG IN CLIENT OF LIBDISPATCH: Cannot specify both overcommit and a non-global target queue
BUG IN CLIENT OF LIBDISPATCH: Unknown entity
BUG IN CLIENT OF LIBDISPATCH: Invalid threads_per_cluster value, only acceptable value is 1
BUG IN CLIENT OF LIBDISPATCH: Filter id should be non-NULL
com.apple.root.utility-qos
BUG IN CLIENT OF LIBDISPATCH: dispatch_set_qos_class_floor called on invalid object type
BUG IN CLIENT OF LIBDISPATCH: Corrupted priority
BUG IN CLIENT OF LIBDISPATCH: Queue type doesn't support dispatch_sync
os_workgroup_interval_create_with_workload_id
BUG IN CLIENT OF LIBDISPATCH: Called peek after drain
BUG IN CLIENT OF LIBDISPATCH: Unsupported callbacks version
BUG IN CLIENT OF LIBDISPATCH: Couldn't get debug control port
BUG IN CLIENT OF LIBDISPATCH: _dispatch_mach_default_async_reply_handler called
BUG IN CLIENT OF LIBDISPATCH: Cannot target source to the cooperative root queue - not implemented
BUG IN CLIENT OF LIBDISPATCH: Setting interval to 0
BUG IN CLIENT OF LIBDISPATCH: mach_port_construct() failed: cannot create receive right
leaf, size = %zd, buf = %p 
com.apple.root.background-qos.overcommit
BUG IN CLIENT OF LIBDISPATCH: Too many nested calls to dispatch_group_enter()
BUG IN CLIENT OF LIBDISPATCH: Absurd publen
BUG IN CLIENT OF LIBDISPATCH: Unexpected dispatch object type
BUG IN CLIENT OF LIBDISPATCH: dispatch_sync called on queue already owned by current thread
mach_mig_demux
BUG IN CLIENT OF LIBDISPATCH: Corrupt activation state
BUG IN CLIENT OF LIBDISPATCH: Cannot change a handler of this source after it has been activated
DISPATCH_EVFILT_MACH_NOTIFICATION
channel
BUG IN LIBDISPATCH: do_invoke called
BUG IN CLIENT OF LIBDISPATCH: Messsage should be non-NULL
vfs
com.apple.libdispatch.workloop_fallback
BUG IN CLIENT OF LIBDISPATCH: kqueue() failure: kernel is out of memory
BUG IN CLIENT OF LIBDISPATCH: Invalid arguments
com.apple.coreaudio.hal.clientthread
kern.wq_limit_cooperative_threads
BUG IN CLIENT: Releasing last reference to workgroup interval while an interval has been started
BUG IN CLIENT OF LIBDISPATCH: Premature release of a locked queue
BUG IN CLIENT OF LIBDISPATCH: Transition to multithreaded is prohibited
BUG IN CLIENT OF LIBDISPATCH: Attempting to modify timer clock
BUG IN CLIENT OF LIBDISPATCH: Unable to allocate reply port, possible port leak
BUG IN CLIENT OF LIBDISPATCH: Could not create task mach voucher
BUG in libdispatch client: %s %s - 0x%x
BUG IN CLIENT OF LIBDISPATCH: Release of a queue while items are enqueued
BUG IN CLIENT OF LIBDISPATCH: Release of a workloop while items are enqueued
vnode
BUG IN CLIENT OF LIBDISPATCH: voucher_activity_initialize_4libtrace called twice
BUG IN LIBDISPATCH: Corrupt thread event value
BUG IN CLIENT OF LIBDISPATCH: Bound thread attribute set multiple times
BUG IN CLIENT OF LIBDISPATCH: Received message with MACH_PORT_NULL msgh_local_port
BUG IN LIBDISPATCH: Invalid msg aux data size.
BUG IN LIBDISPATCH: Unexpected error from mach_msg_receive
BUG IN CLIENT OF LIBDISPATCH: Unbalanced call to dispatch_group_leave()
exclaves_notification
BUG IN LIBDISPATCH: Invalid wlh
BUG IN CLIENT OF LIBDISPATCH: Could not allocate heap
Y
value = %ld, orig = %ld }
BUG IN CLIENT OF LIBDISPATCH: Release of an inactive object
BUG IN CLIENT OF LIBDISPATCH: Corrupt thread event value
BUG IN CLIENT OF LIBDISPATCH: invalid queue passed to dispatch_assert_queue()
BUG IN CLIENT OF LIBDISPATCH: Invalid flags passed to dispatch_block_perform()
, inactive
local 0x%x, remote 0x%x
Changing target queue hierarchy after mach channel was connected
BUG in libdispatch: %s - %lu - 0x%llx
mach_recv
EVFILT_EXCLAVES_NOTIFICATION
BUG IN LIBDISPATCH: apply continuation has invalid flags
local 0x%x
BUG IN CLIENT OF LIBDISPATCH: Could not get unprivileged host port
com.apple.coreaudio.hal.iothread
com.apple.root.maintenance-qos
API MISUSE: Resurrection of an object
BUG IN LIBDISPATCH: Changing the QoS while on the manager queue
API MISUSE: Voucher over-release
BUG IN LIBDISPATCH: Unsupported wlh configuration
sigterm (xpc)
MallocStackLogging
BUG IN CLIENT OF LIBDISPATCH: lock not owned by current thread
EVFILT_FS
DISPATCH_EVFILT_TIMER_WITH_CLOCK
BUG IN CLIENT OF LIBDISPATCH: Unable to copyout msg, possible port leak
 (pending)
data[%p] = { 
Thread is not a member of the workgroup
, suspended = %d
BUG IN CLIENT of %s: Invalid mach port 0x%x
Join token provided is for a different workgroup than the last one joined by thread
BUG IN CLIENT OF LIBDISPATCH: _dispatch_main_queue_callback_4CF called after dispatch_main()
write
%s  %04lx 
queue_pthread_root
com.apple.root.user-initiated-qos
Recipe Contents
composite, size = %zd, num_records = %zd 
data
com.apple.libdispatch-io.deviceq.%d
Join token is corrupt
BUG IN LIBDISPATCH: unexpected receipt of no-more-senders
sref = %d, target = %s[%p], width = 0x%x, state = 0x%016llx
BUG IN CLIENT OF LIBDISPATCH: Could not generate an activity ID
queue_runloop
source
BUG IN CLIENT OF LIBDISPATCH: trying to install hooks with unsupported version
add
BUG IN LIBDISPATCH: MACH_RCV_LARGE_IDENTITY with no identity
com.apple.libdispatch-io.barrierq
BUG IN LIBDISPATCH: vmdeallocate destructor called
BUG IN CLIENT OF LIBDISPATCH: NULL was passed where a block should have been
, draining on 0x%x
vm (deprecated)
BUG IN LIBDISPATCH: EVFILT_MACHPORT with overlarge message
 %02x
closed, 
BUG IN CLIENT OF LIBDISPATCH: Invalid queue attribute
BUG IN CLIENT OF LIBDISPATCH: dispatch_source_cancel_and_wait called from a source handler
timer
_dispatch_kevent_mach_msg_drain: message reception failed
BUG IN CLIENT OF LIBDISPATCH: kqueue() failure: system is out of file descriptors
The arena associated with workgroup is not to be partitioned
BUG IN LIBDISPATCH: Invalid workload ID type
queue_cooperative
BUG IN CLIENT OF LIBDISPATCH: Invalid pthread root queue observer hooks
BUG IN CLIENT OF LIBDISPATCH: Assertion failed: 
BUG IN CLIENT OF LIBDISPATCH: Invalid threads_per_entity value for CPU entity
EVFILT_AIO
%s%s:\n
BUG IN CLIENT OF LIBDISPATCH: Owner in ulock is unknown - possible memory corruption
BUG IN LIBDISPATCH: ulock_wait() failed
%s
BUG IN CLIENT OF LIBDISPATCH: Calling dispatch_mach_handoff_reply multiple times from the same context
mach_send
\n
com.apple.main-thread
API MISUSE: Object type does not support resume
BUG IN LIBDISPATCH: mach_voucher_attr_command(BANK_PERSONA_ADOPT_ANY) failed
com.apple.root.utility-qos.overcommit
BUG IN CLIENT OF LIBDISPATCH: dispatch_set_qos_class_fallback called on invalid object type
LIBDISPATCH_STRICT
BUG IN CLIENT OF LIBDISPATCH: Release of a source that has not been cancelled, but has a mandatory cancel handler
BUG IN CLIENT OF LIBDISPATCH: Mach port notification collision
BUG IN CLIENT OF LIBDISPATCH: Invalid reply port
Voucher: 0x%x Failed to get contents %s\n
queue_serial
missing do_debug vtable slot: 
not 
com.apple.coremedia
io
file
v8@?0
BUG IN CLIENT OF LIBDISPATCH: Cannot change the target of this object after it has been activated
BUG IN LIBDISPATCH: Unexpected error from kevent
BUG IN LIBDISPATCH: Unable to get the unique pid (size)
com.apple.root.maintenance-qos.cooperative
BUG IN LIBDISPATCH: free destructor called
BUG IN LIBDISPATCH: Don't try to wake up or override the manager
BUG IN CLIENT OF LIBDISPATCH: Too many calls to dispatch_suspend() prior to calling dispatch_set_target_queue() or dispatch_set_*_handler()
BUG IN CLIENT OF LIBDISPATCH: Queue doesn't support dispatch_queue_set_specific
com.apple.root.workloop-custom
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_kevent_client
BUG IN CLIENT OF LIBDISPATCH: A block object may not be both run more than once and waited for
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_cancel()
BUG IN CLIENT OF LIBDISPATCH: Overlarge message
timer (interval)
Key: %u, 
   
com.apple.root.user-interactive-qos.cooperative
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_testcancel()
BUG IN CLIENT OF LIBDISPATCH: Release of a channel that has not been cancelled, but has a cancel acknowledgement callback
size %u, 
Changing target queue hierarchy with a dispatch_sync in flight
function
BUG IN CLIENT OF LIBDISPATCH: Process has too many threads.
BUG IN CLIENT of %s: Mismatched workload ID and attribute interval type: %s vs %hd
workgroup.c
BUG in libdispatch: %s: \"%s\" - 0x%x{ 0x%llx[%s], ident: %lld / 0x%llx, handler: %p }
BUG IN CLIENT OF LIBDISPATCH: invalid queue passed to dispatch_assert_queue_not()
BUG IN CLIENT OF LIBDISPATCH: A block object may not be waited for more than once
BUG IN CLIENT OF LIBDISPATCH: _dispatch_source_will_reenable_kevent_4NW not called from within the event handler
timer (after)
memorystatus
random
Exceeded the maximum number of workers who can access the arena
BUG IN LIBDISPATCH: Release while enqueued
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_hooks_install_4libxpc called twice
BUG IN LIBDISPATCH: Cannot raise oneself to manager
kevent
BUG IN CLIENT OF LIBDISPATCH: Voucher corruption
com.apple.root.default-qos.cooperative
```
