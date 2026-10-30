# `/System/DriverKit/usr/lib/system/libdispatch.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 586,384 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 29 (Size: 2608)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (9)

- `/System/DriverKit/usr/lib/system/libdispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
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

## Strings (507)

```
BUG IN LIBDISPATCH: QoS Maintenance support required
>, 
_dispatch_kevent_mach_msg_drain: message reception failed
type = %s %s, fd = 0x%lx, fd_entry = %p, channel = %p, queue = %p -> %s[%p], target = %s[%p], offset = %lld, length = %zu, done = %zu, undelivered = %zu, flags = %u, err = 0x%x, low = 0x%zx, high = 0x%zx, interval%s = %llu 
BUG IN DISPATCH: Invalid wi flags = %u
BUG IN CLIENT OF LIBDISPATCH: Over-resume of an object
BUG IN LIBDISPATCH: Root queue initialization failed
cur_wg == NULL
BUG IN CLIENT OF LIBDISPATCH: Unexpected EV_VANISHED (do not destroy random mach ports or file descriptors)
BUG IN LIBDISPATCH: message received without expected trailer
EVFILT_USER
os_workgroup_create_with_workload_id_and_workgroup
BUG IN CLIENT OF LIBDISPATCH: Release of a suspended object
Changing the target of a source after it has been activated
BUG IN LIBDISPATCH: Missing Kevent WORKQ support
queue_global
BUG IN CLIENT OF LIBDISPATCH: Channel never connected
timer (fixed-clock)
com.apple.root.maintenance-qos.overcommit
disk
queue_cooperative
source
BUG IN CLIENT OF LIBDISPATCH: Premature release of a locked queue
BUG IN CLIENT OF LIBDISPATCH: Changing target queue hierarchy after xpc connection was activated
BUG IN CLIENT OF LIBDISPATCH: Changing target queue hierarchy after mach channel was connected
mach_recv (channel)
syslog
BUG IN LIBDISPATCH: Unexpected error from kevent
monitor
EVFILT_MEMORYSTATUS
BUG IN LIBDISPATCH: Waking up a kq with cooperative thread request is not supported
EVFILT_PROC
com.apple.root.background-qos.overcommit
BUG IN CLIENT OF LIBDISPATCH: workloop qos class or priority must be set before cpupercent
Join token provided is for a different thread
queue_main
, in-barrier
kern.wq_limit_cooperative_threads
BUG IN CLIENT OF LIBDISPATCH: Unexpected EV_VANISHED (do not destroy random mach ports)
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_send_with_result_and_wait_for_reply is XPC only
BUG IN LIBDISPATCH: dispatch_data_create_subrange out of bounds
BUG IN CLIENT of %s: Invalid attribute pointer
com.apple.root.workloop-custom.overcommit
LIBDISPATCH_STRICT
BUG IN LIBDISPATCH: firehose_mig_server doesn't handle replies
BUG IN CLIENT of %s: Mismatched workload ID and attribute interval type: %s vs %hd
BUG IN LIBDISPATCH: free destructor called
BUG IN CLIENT OF LIBDISPATCH: Cannot specify an overcommit attribute and use this kind of target queue
BUG IN CLIENT OF LIBDISPATCH: Voucher importance count underflow
  %s\n
BUG IN CLIENT OF LIBDISPATCH: Workload identifier must not be NULL
BUG IN CLIENT OF LIBDISPATCH: Too many calls to dispatch_suspend() prior to calling dispatch_set_target_queue() or dispatch_set_*_handler()
BUG IN LIBDISPATCH: apply continuation has invalid flags
DISPATCH_EVFILT_CUSTOM_REPLACE
Y
Command: %u, 
com.apple.backboardd.displaythread
BUG IN CLIENT OF LIBDISPATCH: Cannot target source to the cooperative root queue - not implemented
BUG IN CLIENT OF LIBDISPATCH: Corruption: failed to clear bit exclusively
API MISUSE: Voucher over-release
BUG IN LIBDISPATCH: Invalid wlh state
BUG IN CLIENT OF LIBDISPATCH: Attempting to modify timer clock
 %02x
<unknown>
, activating
runloop-queue
BUG IN CLIENT OF LIBDISPATCH: Unable to allocate reply port, possible port leak
BUG IN LIBDISPATCH: Unsupported wlh configuration
vm (deprecated)
BUG IN CLIENT OF LIBDISPATCH: Unexpected error from kevent
com.apple.debug-channel
BUG in libdispatch client: _dispatch_kevent_mach_msg_drain: dropped message too large to fit in memory: id = 0x%x, size = %u
com.apple.libdispatch-io.dev_lockq
os_workgroup_interval_create_with_workload_id
BUG IN LIBDISPATCH: Corrupt thread event value
timer = { target = 0x%llx, deadline = 0x%llx, interval = 0x%llx, flags = 0x%x }, 
bits <l %u, r %u
 } }
EVFILT_READ
missing do_debug vtable slot: 
data-replace
workloop
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_kevent_vanished
BUG IN CLIENT OF LIBDISPATCH: dispatch_apply_attr not initialized using dispatch_apply_attr_init
BUG IN CLIENT OF LIBDISPATCH: Message already enqueued
read
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
com.apple.coreaudio.hal.iothread
v8@?0
stderr
%s  %04lx 
BUG IN LIBDISPATCH: ulock_wake() failed
BUG IN CLIENT OF LIBDISPATCH: Filter id should be non-NULL
BUG IN CLIENT OF LIBDISPATCH: Unable to make memory port
BUG IN CLIENT OF LIBDISPATCH: Corrupt activation state
data-or
com.apple.root.utility-qos.cooperative
BUG IN LIBDISPATCH: Cannot raise oneself to manager
BUG IN CLIENT OF LIBDISPATCH: Cannot set width of a serial queue
EVFILT_AIO
BUG IN CLIENT OF LIBDISPATCH: Invalid arguments
BUG IN CLIENT OF LIBDISPATCH: NULL was passed where a block should have been
BUG IN CLIENT OF LIBDISPATCH: trying to lock recursively
BUG IN CLIENT OF LIBDISPATCH: _dispatch_main_queue_callback_4CF called after dispatch_main()
com.apple.libdispatch-io.deviceq.%d
operation
BUG IN LIBDISPATCH: Allocation should always fail
B40@?0^{dispatch_data_s=[0{dispatch_object_s=[0{_os_object_s=^{_os_object_vtable_s}ii}]^{dispatch_object_vtable_s}ii^{dispatch_object_s}^{dispatch_queue_s}^v(?=^?^v)}][0{_os_object_s=^{_os_object_vtable_s}ii}]^{dispatch_data_vtable_s}ii^{di
com.apple.root.workloop-custom
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_notify()
opts/err = 0x%x, msgh[%p] = { 
BUG IN CLIENT OF LIBDISPATCH: Mach port notification collision
BUG IN CLIENT: Releasing last reference to workgroup interval while an interval has been started
The arena associated with workgroup is not to be partitioned
BUG IN CLIENT OF LIBDISPATCH: _dispatch_mach_default_async_reply_handler called
BUG IN CLIENT OF LIBDISPATCH: Too many nested calls to dispatch_suspend()
port = 0x%x, 
BUG IN LIBDISPATCH: dq_activate called
BUG IN CLIENT OF LIBDISPATCH: Invalid pthread root queue observer hooks
size %u, 
, o 0x%x
com.apple.root.utility-qos
BUG IN CLIENT OF LIBDISPATCH: pthread_start os_workgroup_join failed
API MISUSE: Resurrection of an over-released object
BUG IN CLIENT OF LIBDISPATCH: trying to install hooks with unsupported version
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_kevent_client
, inactive
data-add
BUG IN LIBDISPATCH: Invalid wlh
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_mach_client
BUG in libdispatch client: %s, monitored resource vanished before the source cancel handler was invoked { %p[%s], ident: %d / 0x%x, handler: %p }
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_deprecated
BUG IN CLIENT OF LIBDISPATCH: Waiter pushed onto manager
DISPATCH_EVFILT_CUSTOM_OR
com.apple.root.maintenance-qos
channel
TRUE
sref = %d, target = %s[%p], width = 0x%x, state = 0x%016llx
}
EVFILT_TIMER
BUG IN LIBDISPATCH: Unexpected error from mach recv
BUG IN LIBDISPATCH: Unexpected event
BUG IN LIBDISPATCH: Interrupted drain on manager queue
BUG IN CLIENT OF LIBDISPATCH: attribute's properties are invalid or meaningless on this system
BUG IN CLIENT OF LIBDISPATCH: Unable to copyout msg, possible port leak
deleted, 
BUG IN CLIENT OF LIBDISPATCH: Unable to create signal thread
EVFILT_SOCK
DISPATCH_EVFILT_CUSTOM_ADD
BUG IN LIBDISPATCH: Invalid workgroup port
BUG IN CLIENT OF LIBDISPATCH: Release of a queue with corrupt state
, enqueued
BUG IN CLIENT OF LIBDISPATCH: Release of a workloop while items are enqueued
BUG IN CLIENT OF LIBDISPATCH: The executable is already multithreaded
%s
BUG IN CLIENT OF LIBDISPATCH: Changing target queue hierarchy after source was activated
, flatbuf = %p 
BUG IN CLIENT OF LIBDISPATCH: Passing an invalid leeway
EVFILT_WRITE
BUG IN CLIENT OF LIBDISPATCH: Absurd publen
data[%p] = { 
BUG IN CLIENT OF LIBDISPATCH: Owner in ulock is unknown - possible memory corruption
BUG IN CLIENT OF LIBDISPATCH: Release of a locked workloop
LIBDISPATCH_COOPERATIVE_POOL_STRICT
IMPORTANCE INFO: %s
Recipe Contents
semaphore
data
leaf, size = %zd, buf = %p 
com.apple.root.maintenance-qos.cooperative
group
API MISUSE: Over-release of an object
BUG IN CLIENT OF LIBDISPATCH: Use-after-free of dispatch_semaphore_t or dispatch_group_t
BUG IN CLIENT OF LIBDISPATCH: Voucher corruption
Key: %u, 
com.apple.coreaudio.hal.clientthread
BUG IN CLIENT OF LIBDISPATCH: Invalid reply port
 (pending)
EVFILT_EXCLAVES_NOTIFICATION
BUG IN CLIENT OF LIBDISPATCH: Could not get unprivileged host port
BUG IN CLIENT of %s: Workgroup already cancelled
io
mach
com.apple.libdispatch.workloop_fallback
BUG IN CLIENT OF LIBDISPATCH: _dispatch_main_queue_callback_4CF called from the wrong thread
firehose
BUG IN CLIENT OF LIBDISPATCH: firehose_drain_notifications_once() failed
Exceeded the maximum number of workers who can access the arena
com.apple.backboardd.hid
value = %ld, orig = %ld }
BUG IN LIBDISPATCH: Unregistration failed
   
BUG IN LIBDISPATCH: Release while enqueued
BUG IN CLIENT OF LIBDISPATCH: sync waiter found on channel
BUG IN CLIENT OF LIBDISPATCH: Release of a source that has not been cancelled, but has a mandatory cancel handler
BUG IN CLIENT OF LIBDISPATCH: Trying to handoff IPC from non IPC context
BUG IN LIBDISPATCH: Invalid msg aux data size.
EVFILT_VNODE
BUG IN CLIENT OF LIBDISPATCH: Failed to initalize workqueue kevent
%s%s:\n
com.apple.main-thread
BUG in libdispatch client: %s %s{ 0x%llx[%s], ident: %lld / 0x%llx, handler: %p }
BUG IN CLIENT OF LIBDISPATCH: Corrupt thread event value
BUG IN CLIENT OF LIBDISPATCH: Cannot change the target of this object after it has been activated
BUG IN LIBDISPATCH: Invalid way to wake up a workloop
BUG IN CLIENT OF LIBDISPATCH: unsupported vah_version
BUG IN LIBDISPATCH: firehose_push_reply should never be sent to the buffer receive port
BUG IN CLIENT of %s: Invalid mach port 0x%x
BUG IN CLIENT OF LIBDISPATCH: Not a runloop queue
EVFILT_missing
BUG IN CLIENT OF LIBDISPATCH: Do not close random Unix descriptors
LIBDISPATCH_CONTINUATION_ALLOCATOR
Thread is not a member of the workgroup
com.apple.root.background-qos.cooperative
BUG IN LIBDISPATCH: Trailer format is invalid
\n
BUG IN LIBDISPATCH: do_invoke called
BUG IN CLIENT of %s: Non-default attribute flags: 0x%x
MIG_REPLY_MISMATCH
BUG IN LIBDISPATCH: mach semaphore API failure
BUG IN CLIENT OF LIBDISPATCH: Cannot change the target of a queue already targeted by other dispatch objects
EVFILT_MACHPORT
queue_serial
BUG IN LIBDISPATCH: Cannot turn a manager thread into a normal one
BUG IN CLIENT OF LIBDISPATCH: A block object may not be waited for more than once
dispatch_mig_server: mach_msg() failed
BUG IN CLIENT OF LIBDISPATCH: Invalid workloop owner, possible memory corruption
BUG IN CLIENT of %s: Invalid workload interval type: %s (%hd)
 (armed)
Previous voucher: 0x%x, 
com.apple.root.default-qos
YES
id 0x%x, 
timer
API MISUSE: Resurrection of an object
, draining on 0x%x
BUG IN CLIENT OF LIBDISPATCH: Used Swift only SPI to enqueue non-Swift runtime objects into dispatch
cancelled, 
BUG IN LIBDISPATCH: Premature thread exit while a dispatch queue is running
kevent = %p%s, filter = %s }
DISPATCH_EVFILT_TIMER
composite, size = %zd, num_records = %zd 
BUG IN LIBDISPATCH: Unexpected __ulock_wait error
count = %u, gen = %d, waiters = %d, notifs = %d }
BUG IN CLIENT OF LIBDISPATCH: dispatch_set_qos_class_fallback called on invalid object type
BUG IN LIBDISPATCH: Don't try to wake up or override the manager
BUG IN CLIENT OF LIBDISPATCH: Queue type doesn't support dispatch_sync
BUG IN LIBDISPATCH: Premature thread exit while a dispatch context is set
BUG IN CLIENT OF LIBDISPATCH: Invalid source type
sock
v16@?0^{dispatch_fd_entry_s=i^{dispatch_io_path_data_s}iiiI{dispatch_stat_s=iS}[2^{dispatch_stream_s}]^{dispatch_disk_s}^{dispatch_queue_s}^{dispatch_queue_s}^{dispatch_group_s}^{dispatch_io_s}{?=^{dispatch_operation_s}^^{dispatch_operation
not 
dispatch source activated with no event handler set
mach reply
os_workgroup_create_with_workload_id
_os_workgroup_join_update_wg
BUG IN LIBDISPATCH: none destructor called
BUG IN LIBDISPATCH: Changing the QoS while on the manager queue
mach_notification
enable
BUG IN CLIENT OF LIBDISPATCH: Invalid size for the firehose buffer
stopped, 
BUG IN CLIENT: Thread exiting without leaving workgroup '%s'
com.apple.libdispatch-manager
%s[%p] = { 
BUG IN CLIENT OF LIBDISPATCH: Release of an inactive object
Changing target queue hierarchy after mach channel was connected
BUG IN LIBDISPATCH: Corrupt unote action
BUG IN LIBDISPATCH: Invalid values for MADVISE_CHUNK_COUNT / CHUNK_SIZE
BUG IN CLIENT OF LIBDISPATCH: Unable to allocate mach port
delete
BUG IN LIBDISPATCH: Unable to get the unique pid (error)
queue_concurrent
Changing target queue hierarchy after xpc connection was activated
BUG IN CLIENT OF LIBDISPATCH: Semaphore object deallocated while in use (current value < original value)
BUG IN LIBDISPATCH: Invalid workload ID type
com.apple.root.utility-qos.overcommit
BUG IN CLIENT OF LIBDISPATCH: Process has too many threads.
timer (after)
BUG IN CLIENT OF LIBDISPATCH: Log is too large
com.apple.root.user-initiated-qos.cooperative
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_wait()
local 0x%x, remote 0x%x
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_mig_demux: mach_msg(MACH_SEND_MSG) failed
_os_workgroup_set_work_interval_workload_id
BUG IN LIBDISPATCH: Don't try to wake up or override a root queue
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_hooks_install_4libxpc called twice
BUG IN CLIENT OF LIBDISPATCH: A block object may not be both run more than once and observed
Changing the target of a queue already targeted by other dispatch objects
BUG IN CLIENT OF LIBDISPATCH: dispatch queue/source property setter called after activation
BUG IN CLIENT OF LIBDISPATCH: 0 is an invalid threads_per_cluster value
vfs
EVFILT_SIGNAL
closed, 
BUG IN CLIENT of %s: Mismatched workload ID and port interval type: %s vs %hd
BUG IN CLIENT OF LIBDISPATCH: invalid queue passed to dispatch_assert_queue()
com.apple.root.default-qos.overcommit
com.apple.libsystem.libdispatch
BUG IN LIBDISPATCH: _pthread_set_properties_self failed
BUG IN CLIENT OF LIBDISPATCH: Queue doesn't support dispatch_queue_set_specific
BUG IN CLIENT OF LIBDISPATCH: Overlarge message
queue_pthread_root
com.apple.coremedia
com.apple.root.user-interactive-qos.cooperative
BUG IN CLIENT OF LIBDISPATCH: _dispatch_source_will_reenable_kevent_4NW not called from within the event handler
BUG IN LIBDISPATCH: Unexpected error from mach_msg_receive
BUG IN CLIENT OF LIBDISPATCH: Calling dispatch_mach_handoff_reply multiple times from the same context
mach_recv
BUG IN LIBDISPATCH: Invalid kevent priority
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_testcancel()
BUG IN CLIENT OF LIBDISPATCH: Reply port needed for async send with reply
xref = %d, ref = %d, 
BUG IN CLIENT OF LIBDISPATCH: Bound thread attribute set multiple times
 (direct)
signal
Creating an os_workgroup of unknown type
BUG IN CLIENT OF LIBDISPATCH: Dispatch source used after last release
no ports
proc
type = %s, fd = 0x%lx, %sfd_entry = %p, queue = %p, target = %s[%p], barrier_queue = %p, barrier_group = %p, err = 0x%x, low = 0x%zx, high = 0x%zx, interval%s = %llu 
(strict)
Join token provided is for a different workgroup than the last one joined by thread
BUG IN CLIENT OF LIBDISPATCH: Unknown entity
Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?
mach_mig_demux
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_mig_demux_get_context not called from dispatch_mach_mig_demux context
BUG IN LIBDISPATCH: Broken priority
com.apple.root.user-initiated-qos.overcommit
BUG IN CLIENT OF LIBDISPATCH: Invalid queue attribute
BUG IN CLIENT OF LIBDISPATCH: Cannot change label for this queue
BUG IN LIBDISPATCH: Unable to limit cooperative pool size
write
Changing target queue hierarchy with a dispatch_sync in flight
BUG IN LIBDISPATCH: EVFILT_MACHPORT with no message
com.apple.root.default-qos.cooperative
com.apple.root.user-initiated-qos
BUG IN LIBDISPATCH: do_dispose called
BUG IN CLIENT OF LIBDISPATCH: Called peek after drain
target = %s[%p], receive = 0x%x, send = 0x%x, send-possible = 0x%x%s, checkin = 0x%x%s, send state = %016llx, disconnected = %d, canceled = %d 
file
BUG IN CLIENT OF LIBDISPATCH: Unsupported interface
sigterm (xpc)
queue_runloop
workgroup.c
BUG IN LIBDISPATCH: unexpected receipt of no-more-senders
BUG IN CLIENT OF LIBDISPATCH: Channel already connected
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_cancel()
, thread = 0x%x 
BUG IN CLIENT OF LIBDISPATCH: Source is suspended
NULL: 
BUG IN CLIENT OF LIBDISPATCH: Voucher port corruption
BUG IN LIBDISPATCH: Disposing of timer still in its heap
com.apple.root.background-qos
com.apple.root.user-interactive-qos
%s%s%s
Changing target queue hierarchy after source was activated
BUG IN CLIENT OF LIBDISPATCH: Invalid send flags
BUG IN CLIENT OF LIBDISPATCH: Memory corruption in the logging buffers
BUG IN LIBDISPATCH: Deferred continuation on source, mach channel or mgr
BUG IN CLIENT OF LIBDISPATCH: Attempt to set timer on a non-timer source
BUG in libdispatch client: %s %s: \"%s\" - 0x%x { 0x%llx[%s], ident: %lld / 0x%llx, handler: %p }
EVFILT_WORKLOOP
BUG IN CLIENT OF LIBDISPATCH: Could not create task mach voucher
LIBDISPATCH_LOG
BUG IN CLIENT OF LIBDISPATCH: Too many nested calls to dispatch_group_enter()
BUG IN CLIENT OF LIBDISPATCH: Waking up an inactive workloop
Setting registration handler after the source has been activated
BUG IN CLIENT OF LIBDISPATCH: invalid queue passed to dispatch_am_i_on_queue_4swiftonly()
BUG IN CLIENT OF LIBDISPATCH: Over-resume of an inactive object
os_workgroup_create_with_workload_id_and_port
mach_msg
BUG IN CLIENT OF LIBDISPATCH: Release of a workloop with corrupt state
BUG IN LIBDISPATCH: Lingering DISPATCH_WLH_ANON
BUG IN CLIENT OF LIBDISPATCH: Setting interval to 0
kevent
BUG IN CLIENT of %s: Unable to set kernel workload ID: %s (0x%x) -> %d (0x%x)
BUG IN CLIENT OF LIBDISPATCH: Unexpected non message event
BUG IN CLIENT of %s: Mismatched workload ID and workgroup interval type: %s vs %hd
BUG IN CLIENT OF LIBDISPATCH: Invalid flags passed to dispatch_block_perform()
BUG IN CLIENT OF LIBDISPATCH: Cannot specify both overcommit and a non-global target queue
BUG IN CLIENT OF LIBDISPATCH: Source has a cancel handler
add
LIBDISPATCH_TIMERS_FORCE_MAX_LEEWAY
BUG IN LIBDISPATCH: dispatch_data_copy_region out of bounds
BUG IN CLIENT of %s: Invalid workgroup port 0x%x
=== log file opened for %s[%u] at %ld.%06u ===\n
BUG IN CLIENT OF LIBDISPATCH: Unexpected dispatch object type
, pending-barrier
%sBlock was %sexpected to execute on queue [%s (%p)]
Clearing handler after the source has been activated
BUG IN CLIENT OF LIBDISPATCH: Reply received on unexpected port
BUG IN CLIENT OF LIBDISPATCH: Corrupt channel state
BUG IN CLIENT OF LIBDISPATCH: dispatch_set_qos_class_floor called on invalid object type
BUG IN LIBDISPATCH: Unexpected object type
remote 0x%x
BUG IN LIBDISPATCH: MACH_RCV_LARGE_IDENTITY with no identity
BUG IN CLIENT OF LIBDISPATCH: Could not allocate heap
BUG IN CLIENT OF LIBDISPATCH: Invalid threads_per_entity value for CPU entity
BUG IN CLIENT OF LIBDISPATCH: Messsage should be non-NULL
BUG IN CLIENT OF LIBDISPATCH: Received message with MACH_PORT_NULL msgh_local_port
BUG IN CLIENT OF LIBDISPATCH: mach_port_construct() failed: cannot create receive right
BUG IN CLIENT OF LIBDISPATCH: dispatch_set_qos_class called on invalid object type
BUG IN CLIENT OF LIBDISPATCH: Release of a channel that has not been cancelled, but has a cancel acknowledgement callback
com.apple.libdispatch-io.closeq
queue_attr
/var/tmp/libdispatch.%d.log
BUG IN CLIENT OF LIBDISPATCH: A block object may not be both run more than once and waited for
BUG IN CLIENT OF LIBDISPATCH: dispatch_main() must be called on the main thread
BUG in libdispatch client: dispatch_mach_send_and_wait_for_reply: dropped message too large to fit in memory: id = 0x%x, size = %u
vnode
Voucher: 0x%x Failed to get contents %s\n
BUG in libdispatch: %s - %lu - 0x%llx
BUG IN CLIENT OF LIBDISPATCH: Release of a queue while items are enqueued
BUG IN LIBDISPATCH: Pending thread request underflow
BUG IN CLIENT OF LIBDISPATCH: Could not generate an activity ID
com.apple.libdispatch-io.fd_lockq
BUG IN LIBDISPATCH: Joined count underflowed
BUG IN CLIENT OF LIBDISPATCH: Called drain twice in the same invoke
%sBlock was expected to act as a barrier on queue [%s (%p)]
target = %s[%p], ident = 0x%llx, mask = 0x%x, pending_data = 0x%llx, registered = %d, armed = %d, %s%s%s
mach_send (mach)
BUG IN LIBDISPATCH: base voucher has nested base voucher
Content size: %u\n
Join token is corrupt
API MISUSE: Object type does not support suspension
com.apple.libdispatch-io.streamq
DEPRECATED USE in libdispatch client: %s; set a breakpoint on _dispatch_bug_deprecated to debug
BUG IN CLIENT OF LIBDISPATCH: Corruption of dispatch block object
BUG IN CLIENT OF LIBDISPATCH: Cannot target object to cooperative root queue - not implemented
BUG IN LIBDISPATCH: Locking the manager should not fail
DISPATCH_EVFILT_TIMER_WITH_CLOCK
BUG IN CLIENT OF LIBDISPATCH: Transition to multithreaded is prohibited
MallocStackLogging
BUG in libdispatch client: %s %s - 0x%x
BUG IN CLIENT OF LIBDISPATCH: Channel didn't call dispatch_channel_drain
BUG IN LIBDISPATCH: Premature thread exit with unhandled deferred items
BUG IN LIBDISPATCH: Too many deferred free items
BUG IN LIBDISPATCH: base voucher has non-zero activity value
, dirty
BUG IN LIBDISPATCH: Underflow of tbkqwl count
stream
DISPATCH_EVFILT_MACH_NOTIFICATION
BUG IN CLIENT OF LIBDISPATCH: Assertion failed: 
BUG IN CLIENT OF LIBDISPATCH: Empty message
exclaves_notification
BUG in libdispatch: %s: \"%s\" - 0x%x{ 0x%llx[%s], ident: %lld / 0x%llx, handler: %p }
Voucher: 0x%x\n
, suspended = %d
BUG IN CLIENT OF LIBDISPATCH: Unsupported callbacks version
memorystatus
Voucher: 0x%x has no contents\n
RESOURCE ACCOUNTING INFO: %s
BUG IN CLIENT OF LIBDISPATCH: invalid queue passed to dispatch_assert_queue_not()
BUG IN CLIENT OF LIBDISPATCH: Overlarge message received
BUG IN CLIENT OF LIBDISPATCH: lock not owned by current thread
BUG IN CLIENT OF LIBDISPATCH: dispatch_main called from a block on the main queue
<released queue, pending free>
com.apple.libdispatch-io.channelq
BUG IN LIBDISPATCH: Premature thread exit while a dispatch frame is active
BUG IN CLIENT OF LIBDISPATCH: Cannot change a handler of this source after it has been activated
BUG IN CLIENT OF LIBDISPATCH: Start value is not DISPATCH_TIME_NOW or DISPATCH_TIME_FOREVER
nw_channel
BUG IN CLIENT OF LIBDISPATCH: voucher_activity_initialize_4libtrace called twice
, max qos %d
BUG IN CLIENT OF LIBDISPATCH: dispatch_source_cancel_and_wait called from a source handler
BUG IN LIBDISPATCH: Unable to get the unique pid (size)
v20@?0^{dispatch_data_s=[0{dispatch_object_s=[0{_os_object_s=^{_os_object_vtable_s}ii}]^{dispatch_object_vtable_s}ii^{dispatch_object_s}^{dispatch_queue_s}^v(?=^?^v)}][0{_os_object_s=^{_os_object_vtable_s}ii}]^{dispatch_data_vtable_s}ii^{di
BUG IN CLIENT OF LIBDISPATCH: Cannot target the cooperative root queue - not implemented
BUG IN CLIENT OF LIBDISPATCH: Group object deallocated while in use
API MISUSE: Voucher resurrection
com.apple.root.user-interactive-qos.overcommit
queue_mgr
mach_send
Invalid voucher: 0x%x\n
BUG IN LIBDISPATCH: vmdeallocate destructor called
BUG IN CLIENT OF LIBDISPATCH: Corrupted priority
apply
timer (interval)
, in-flight = %d
BUG IN CLIENT OF LIBDISPATCH: dispatch_sync called on queue already owned by current thread
BUG IN LIBDISPATCH: EVFILT_MACHPORT with overlarge message
v12@?0i8
com.apple.libdispatch-io.barrierq
com.apple.libdispatch-io.opq
BUG IN CLIENT OF LIBDISPATCH: Message size too large
BUG IN CLIENT of %s: Non-default workload type: %s (%hd)
BUG IN LIBDISPATCH: inline destructor called
BUG IN CLIENT OF LIBDISPATCH: Unbalanced call to dispatch_group_leave()
BUG IN CLIENT OF LIBDISPATCH: Invalid threads_per_cluster value, only acceptable value is 1
record[%zd] = { from = %zd, length = %zd, data_object = %p }, 
BUG IN LIBDISPATCH: ulock_wait() failed
BUG IN LIBDISPATCH: Source finalized twice
BUG IN CLIENT OF LIBDISPATCH: Couldn't get debug control port
BUG IN CLIENT OF LIBDISPATCH: Unable to register with logd
BUG IN LIBDISPATCH: unexpected receipt of port-destroyed
needs-event, 
local 0x%x
EVFILT_FS
BUG IN LIBDISPATCH: EVFILT_MACHPORT with no message size
BUG IN LIBDISPATCH: mach_voucher_attr_command(BANK_PERSONA_ADOPT_ANY) failed
random
API MISUSE: Object type does not support resume
, activated
BUG IN CLIENT OF LIBDISPATCH: Invalid queue type
BUG IN CLIENT OF LIBDISPATCH: dispatch_workloop os_workgroup_join failed
BUG IN LIBDISPATCH: Trailer doesn't contain filter policy id
v24@?0B8^{dispatch_data_s=[0{dispatch_object_s=[0{_os_object_s=^{_os_object_vtable_s}ii}]^{dispatch_object_vtable_s}ii^{dispatch_object_s}^{dispatch_queue_s}^v(?=^?^v)}][0{_os_object_s=^{_os_object_vtable_s}ii}]^{dispatch_data_vtable_s}ii^{
```
