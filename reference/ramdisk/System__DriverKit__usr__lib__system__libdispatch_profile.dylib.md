# `/System/DriverKit/usr/lib/system/libdispatch_profile.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 661,136 bytes.

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
xref = %d, ref = %d, 
BUG IN CLIENT OF LIBDISPATCH: Message size too large
BUG IN CLIENT OF LIBDISPATCH: Release of a suspended object
BUG IN CLIENT OF LIBDISPATCH: Too many calls to dispatch_suspend() prior to calling dispatch_set_target_queue() or dispatch_set_*_handler()
BUG IN CLIENT OF LIBDISPATCH: Cannot target source to the cooperative root queue - not implemented
BUG IN CLIENT OF LIBDISPATCH: Passing an invalid leeway
count = %u, gen = %d, waiters = %d, notifs = %d }
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_cancel()
BUG IN LIBDISPATCH: firehose_push_reply should never be sent to the buffer receive port
EVFILT_missing
BUG IN CLIENT OF LIBDISPATCH: Cannot set width of a serial queue
apply
BUG IN CLIENT OF LIBDISPATCH: Dispatch source used after last release
BUG IN LIBDISPATCH: Trailer format is invalid
mach_notification
BUG IN LIBDISPATCH: Unexpected error from mach recv
com.apple.libdispatch-io.closeq
BUG IN CLIENT of %s: Invalid workgroup port 0x%x
=== log file opened for %s[%u] at %ld.%06u ===\n
BUG IN LIBDISPATCH: Cannot turn a manager thread into a normal one
BUG IN CLIENT OF LIBDISPATCH: Unable to register with logd
data[%p] = { 
BUG IN CLIENT OF LIBDISPATCH: Cannot target the cooperative root queue - not implemented
BUG IN CLIENT OF LIBDISPATCH: Semaphore object deallocated while in use (current value < original value)
size %u, 
stream
BUG IN CLIENT of %s: Invalid attribute pointer
com.apple.root.utility-qos.overcommit
queue_serial
function
vm (deprecated)
EVFILT_WORKLOOP
BUG IN CLIENT OF LIBDISPATCH: Received message with MACH_PORT_NULL msgh_local_port
com.apple.root.user-initiated-qos
, enqueued
BUG IN CLIENT OF LIBDISPATCH: Overlarge message
EVFILT_WRITE
Voucher: 0x%x has no contents\n
/var/tmp/libdispatch.%d.log
BUG IN CLIENT OF LIBDISPATCH: Invalid pthread root queue observer hooks
BUG IN CLIENT OF LIBDISPATCH: Unexpected EV_VANISHED (do not destroy random mach ports or file descriptors)
   
, pending-barrier
BUG IN CLIENT OF LIBDISPATCH: Calling dispatch_mach_handoff_reply multiple times from the same context
mach_send
mach_recv
BUG IN LIBDISPATCH: EVFILT_MACHPORT with no message
BUG IN LIBDISPATCH: vmdeallocate destructor called
BUG IN LIBDISPATCH: Unexpected contents in DDI TSD
BUG IN CLIENT OF LIBDISPATCH: Unexpected EV_VANISHED (do not destroy random mach ports)
BUG IN LIBDISPATCH: base voucher has nested base voucher
  %s\n
BUG IN LIBDISPATCH: none destructor called
BUG IN LIBDISPATCH: ulock_wait() failed
BUG IN LIBDISPATCH: Premature thread exit while a dispatch context is set
BUG IN CLIENT OF LIBDISPATCH: Invalid workloop owner, possible memory corruption
BUG IN CLIENT OF LIBDISPATCH: Could not allocate heap
needs-event, 
vnode
BUG IN CLIENT OF LIBDISPATCH: NULL was passed where a block should have been
bits <l %u, r %u
BUG IN CLIENT OF LIBDISPATCH: kqueue() failure: process is out of file descriptors
com.apple.root.default-qos.overcommit
com.apple.root.utility-qos
local 0x%x
com.apple.root.background-qos
com.apple.root.default-qos
random
BUG IN CLIENT OF LIBDISPATCH: Attempt to set timer on a non-timer source
BUG IN LIBDISPATCH: Invalid wlh state
DISPATCH_EVFILT_CUSTOM_OR
(strict)
%s%s%s
BUG IN CLIENT OF LIBDISPATCH: A block object may not be both run more than once and waited for
BUG IN LIBDISPATCH: Premature thread exit with unhandled deferred items
BUG IN CLIENT OF LIBDISPATCH: Channel already connected
Invalid voucher: 0x%x\n
com.apple.libdispatch-io.streamq
BUG IN CLIENT OF LIBDISPATCH: Cannot change the target of a queue already targeted by other dispatch objects
EVFILT_FS
BUG IN LIBDISPATCH: EVFILT_MACHPORT with no message size
BUG IN LIBDISPATCH: mach_voucher_attr_command(BANK_PERSONA_ADOPT_ANY) failed
BUG IN LIBDISPATCH: dispatch_data_create_subrange out of bounds
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
BUG IN CLIENT OF LIBDISPATCH: Voucher corruption
Creating an os_workgroup of unknown type
group
mach_msg
BUG IN LIBDISPATCH: Locking the manager should not fail
BUG IN CLIENT OF LIBDISPATCH: Changing target queue hierarchy after mach channel was connected
 (armed)
EVFILT_MACHPORT
os_workgroup_create_with_workload_id_and_port
BUG IN CLIENT OF LIBDISPATCH: Cannot change label for this queue
BUG IN CLIENT OF LIBDISPATCH: Changing target queue hierarchy after xpc connection was activated
Voucher: 0x%x\n
BUG IN LIBDISPATCH: base voucher has non-zero activity value
BUG IN LIBDISPATCH: Invalid workload ID type
com.apple.libsystem.libdispatch
BUG IN CLIENT OF LIBDISPATCH: Failed to initalize workqueue kevent
, activated
BUG IN CLIENT OF LIBDISPATCH: Waking up an inactive workloop
com.apple.coreaudio.hal.iothread
BUG in libdispatch: %s - %lu - 0x%llx
BUG IN CLIENT OF LIBDISPATCH: Owner in ulock is unknown - possible memory corruption
, inactive
LIBDISPATCH_TIMERS_FORCE_MAX_LEEWAY
com.apple.root.user-interactive-qos
BUG IN CLIENT OF LIBDISPATCH: Release of an inactive object
BUG IN LIBDISPATCH: Interrupted drain on manager queue
BUG IN CLIENT OF LIBDISPATCH: _dispatch_source_will_reenable_kevent_4NW not called from within the event handler
BUG IN CLIENT OF LIBDISPATCH: Messsage should be non-NULL
data-or
%s  %04lx 
BUG IN LIBDISPATCH: inline destructor called
, thread = 0x%x 
BUG IN CLIENT OF LIBDISPATCH: Called peek after drain
com.apple.libdispatch-io.barrierq
BUG IN CLIENT of %s: Invalid workload interval type: %s (%hd)
com.apple.backboardd.hid
com.apple.root.background-qos.overcommit
BUG IN LIBDISPATCH: Invalid way to wake up a workloop
EVFILT_READ
Content size: %u\n
com.apple.root.utility-qos.cooperative
BUG IN LIBDISPATCH: Release while enqueued
, flatbuf = %p 
BUG IN LIBDISPATCH: do_dispose called
BUG IN CLIENT OF LIBDISPATCH: dispatch_main() must be called on the main thread
com.apple.libdispatch.workloop_fallback
BUG IN CLIENT OF LIBDISPATCH: Reply received on unexpected port
BUG IN LIBDISPATCH: Unregistration failed
BUG IN CLIENT: Thread exiting without leaving workgroup '%s'
BUG IN CLIENT OF LIBDISPATCH: Mach port notification collision
BUG IN LIBDISPATCH: Missing Kevent WORKQ support
BUG IN LIBDISPATCH: Premature thread exit while a dispatch queue is running
EVFILT_TIMER
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_mach_client
, in-barrier
BUG in libdispatch client: dispatch_mach_send_and_wait_for_reply: dropped message too large to fit in memory: id = 0x%x, size = %u
EVFILT_PROC
EVFILT_MEMORYSTATUS
v16@?0^{dispatch_fd_entry_s=i^{dispatch_io_path_data_s}iiiI{dispatch_stat_s=iS}[2^{dispatch_stream_s}]^{dispatch_disk_s}^{dispatch_queue_s}^{dispatch_queue_s}^{dispatch_group_s}^{dispatch_io_s}{?=^{dispatch_operation_s}^^{dispatch_operation
BUG IN CLIENT OF LIBDISPATCH: Unexpected non message event
BUG IN CLIENT OF LIBDISPATCH: lock not owned by current thread
BUG IN CLIENT OF LIBDISPATCH: Bound thread attribute set multiple times
BUG IN CLIENT OF LIBDISPATCH: Assertion failed: 
local 0x%x, remote 0x%x
no ports
timer
Exceeded the maximum number of workers who can access the arena
BUG IN CLIENT OF LIBDISPATCH: Corruption of dispatch block object
API MISUSE: Resurrection of an object
BUG IN LIBDISPATCH: Unexpected error from mach_msg_receive
com.apple.debug-channel
BUG IN CLIENT OF LIBDISPATCH: unsupported vah_version
BUG IN LIBDISPATCH: firehose_mig_server doesn't handle replies
v20@?0^{dispatch_data_s=[0{dispatch_object_s=[0{_os_object_s=^{_os_object_vtable_s}ii}]^{dispatch_object_vtable_s}ii^{dispatch_object_s}^{dispatch_queue_s}^v(?=^?^v)}][0{_os_object_s=^{_os_object_vtable_s}ii}]^{dispatch_data_vtable_s}ii^{di
BUG IN CLIENT OF LIBDISPATCH: _dispatch_mach_default_async_reply_handler called
BUG IN LIBDISPATCH: Don't try to wake up or override the manager
BUG IN CLIENT OF LIBDISPATCH: Changing target queue hierarchy after source was activated
BUG IN CLIENT of %s: Mismatched workload ID and attribute interval type: %s vs %hd
%s%s:\n
DEPRECATED USE in libdispatch client: %s; set a breakpoint on _dispatch_bug_deprecated to debug
NULL: 
timer = { target = 0x%llx, deadline = 0x%llx, interval = 0x%llx, flags = 0x%x }, 
BUG IN LIBDISPATCH: Waking up a kq with cooperative thread request is not supported
BUG IN LIBDISPATCH: Broken priority
queue_mgr
BUG IN CLIENT OF LIBDISPATCH: Over-resume of an inactive object
sref = %d, target = %s[%p], width = 0x%x, state = 0x%016llx
, draining on 0x%x
BUG IN CLIENT OF LIBDISPATCH: Log is too large
BUG IN LIBDISPATCH: Unable to get the unique pid (error)
BUG IN LIBDISPATCH: Allocation should always fail
BUG IN CLIENT: Releasing last reference to workgroup interval while an interval has been started
com.apple.root.maintenance-qos.overcommit
v8@?0
com.apple.root.user-initiated-qos.overcommit
BUG IN CLIENT OF LIBDISPATCH: Unable to allocate mach port
v24@?0B8^{dispatch_data_s=[0{dispatch_object_s=[0{_os_object_s=^{_os_object_vtable_s}ii}]^{dispatch_object_vtable_s}ii^{dispatch_object_s}^{dispatch_queue_s}^v(?=^?^v)}][0{_os_object_s=^{_os_object_vtable_s}ii}]^{dispatch_data_vtable_s}ii^{
com.apple.libdispatch-io.fd_lockq
queue_attr
BUG IN CLIENT OF LIBDISPATCH: Source has a cancel handler
com.apple.main-thread
Changing target queue hierarchy after source was activated
target = %s[%p], ident = 0x%llx, mask = 0x%x, pending_data = 0x%llx, registered = %d, armed = %d, %s%s%s
Changing target queue hierarchy after xpc connection was activated
BUG IN CLIENT OF LIBDISPATCH: Corrupt channel state
com.apple.libdispatch-io.dev_lockq
BUG IN LIBDISPATCH: Lingering DISPATCH_WLH_ANON
BUG IN LIBDISPATCH: Source finalized twice
BUG IN LIBDISPATCH: Disposing of timer still in its heap
BUG IN CLIENT OF LIBDISPATCH: Could not get unprivileged host port
type = %s %s, fd = 0x%lx, fd_entry = %p, channel = %p, queue = %p -> %s[%p], target = %s[%p], offset = %lld, length = %zu, done = %zu, undelivered = %zu, flags = %u, err = 0x%x, low = 0x%zx, high = 0x%zx, interval%s = %llu 
remote 0x%x
data-replace
BUG IN CLIENT OF LIBDISPATCH: Unexpected error from kevent
BUG IN CLIENT OF LIBDISPATCH: Invalid threads_per_entity value for CPU entity
BUG IN CLIENT OF LIBDISPATCH: Unable to allocate reply port, possible port leak
Recipe Contents
LIBDISPATCH_LOG
os_workgroup_create_with_workload_id
_os_workgroup_join_update_wg
operation
BUG IN LIBDISPATCH: apply continuation has invalid flags
read
nw_channel
BUG IN CLIENT of %s: Invalid mach port 0x%x
proc
BUG IN CLIENT OF LIBDISPATCH: Invalid arguments
, suspended = %d
API MISUSE: Object type does not support suspension
BUG IN CLIENT OF LIBDISPATCH: dispatch_set_qos_class_fallback called on invalid object type
%sBlock was %sexpected to execute on queue [%s (%p)]
BUG IN CLIENT OF LIBDISPATCH: Channel didn't call dispatch_channel_drain
BUG IN LIBDISPATCH: Don't try to wake up or override a root queue
BUG IN LIBDISPATCH: Unable to limit cooperative pool size
BUG IN LIBDISPATCH: Corrupt unote action
BUG in libdispatch client: %s, monitored resource vanished before the source cancel handler was invoked { %p[%s], ident: %d / 0x%x, handler: %p }
com.apple.libdispatch-io.deviceq.%d
vfs
BUG IN CLIENT OF LIBDISPATCH: voucher_activity_initialize_4libtrace called twice
BUG IN CLIENT OF LIBDISPATCH: Could not generate an activity ID
com.apple.root.user-interactive-qos.cooperative
BUG IN LIBDISPATCH: Cannot raise oneself to manager
BUG IN CLIENT OF LIBDISPATCH: A block object may not be waited for more than once
not 
BUG IN CLIENT OF LIBDISPATCH: Source is suspended
timer (fixed-clock)
os_workgroup_create_with_workload_id_and_workgroup
BUG IN CLIENT OF LIBDISPATCH: Release of a queue while items are enqueued
BUG IN LIBDISPATCH: Manager queue invoked with kevent workqueue enabled
<released queue, pending free>
BUG IN CLIENT OF LIBDISPATCH: dispatch_source_cancel_and_wait called from a source handler
BUG IN CLIENT OF LIBDISPATCH: Release of a locked workloop
id 0x%x, 
Changing target queue hierarchy after mach channel was connected
_dispatch_kevent_mach_msg_drain: message reception failed
BUG IN LIBDISPATCH: kqueue() failure
YES
write
Changing target queue hierarchy with a dispatch_sync in flight
BUG IN CLIENT OF LIBDISPATCH: Corrupt activation state
target = %s[%p], receive = 0x%x, send = 0x%x, send-possible = 0x%x%s, checkin = 0x%x%s, send state = %016llx, disconnected = %d, canceled = %d 
workgroup.c
BUG IN LIBDISPATCH: Joined count underflowed
Join token provided is for a different thread
BUG IN LIBDISPATCH: free destructor called
BUG IN CLIENT OF LIBDISPATCH: mach_port_construct() failed: cannot create receive right
data
Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?
, o 0x%x
v12@?0i8
missing do_debug vtable slot: 
BUG IN CLIENT OF LIBDISPATCH: _dispatch_main_queue_callback_4CF called after dispatch_main()
BUG IN LIBDISPATCH: Unexpected error from kevent
DISPATCH_EVFILT_TIMER_WITH_CLOCK
leaf, size = %zd, buf = %p 
com.apple.root.maintenance-qos.cooperative
BUG IN CLIENT OF LIBDISPATCH: dispatch_sync called on queue already owned by current thread
BUG IN CLIENT OF LIBDISPATCH: Invalid reply port
BUG IN CLIENT OF LIBDISPATCH: Corruption: failed to clear bit exclusively
BUG IN LIBDISPATCH: _pthread_set_properties_self failed
BUG IN CLIENT OF LIBDISPATCH: Release of a queue with corrupt state
com.apple.root.user-interactive-qos.overcommit
BUG IN CLIENT OF LIBDISPATCH: Over-resume of an object
BUG IN CLIENT OF LIBDISPATCH: Empty message
EVFILT_VNODE
DISPATCH_EVFILT_CUSTOM_ADD
RESOURCE ACCOUNTING INFO: %s
MallocStackLogging
com.apple.root.background-qos.cooperative
BUG IN LIBDISPATCH: do_invoke called
BUG IN CLIENT OF LIBDISPATCH: Group object deallocated while in use
BUG IN CLIENT OF LIBDISPATCH: Release of a workloop while items are enqueued
%s
BUG IN CLIENT OF LIBDISPATCH: Unsupported interface
runloop-queue
BUG IN CLIENT OF LIBDISPATCH: Release of a source that has not been cancelled, but has a mandatory cancel handler
BUG IN LIBDISPATCH: Invalid wlh
BUG IN CLIENT OF LIBDISPATCH: Start value is not DISPATCH_TIME_NOW or DISPATCH_TIME_FOREVER
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_deprecated
BUG IN CLIENT OF LIBDISPATCH: Attempting to modify timer clock
BUG IN CLIENT OF LIBDISPATCH: Corrupt thread event value
BUG IN CLIENT OF LIBDISPATCH: invalid queue passed to dispatch_assert_queue()
BUG IN CLIENT OF LIBDISPATCH: invalid queue passed to dispatch_assert_queue_not()
BUG IN CLIENT OF LIBDISPATCH: Not a runloop queue
BUG IN CLIENT OF LIBDISPATCH: Cannot specify both overcommit and a non-global target queue
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_send_with_result_and_wait_for_reply is XPC only
add
BUG IN CLIENT OF LIBDISPATCH: Unable to copyout msg, possible port leak
The arena associated with workgroup is not to be partitioned
queue_global
port = 0x%x, 
BUG IN CLIENT OF LIBDISPATCH: dispatch_set_qos_class_floor called on invalid object type
 (direct)
com.apple.libdispatch-manager
io
BUG IN CLIENT OF LIBDISPATCH: Invalid queue type
%sBlock was expected to act as a barrier on queue [%s (%p)]
BUG IN CLIENT OF LIBDISPATCH: Cannot specify an overcommit attribute and use this kind of target queue
kevent
BUG IN CLIENT OF LIBDISPATCH: firehose_drain_notifications_once() failed
os_workgroup_interval_create_with_workload_id
BUG IN CLIENT of %s: Workgroup already cancelled
Voucher: 0x%x Failed to get contents %s\n
disk
%s[%p] = { 
BUG IN CLIENT OF LIBDISPATCH: Used Swift only SPI to enqueue non-Swift runtime objects into dispatch
BUG IN LIBDISPATCH: Unexpected object type
BUG IN CLIENT OF LIBDISPATCH: Invalid send flags
DISPATCH_EVFILT_MACH_NOTIFICATION
BUG IN CLIENT of %s: Non-default attribute flags: 0x%x
queue_main
syslog
BUG IN CLIENT OF LIBDISPATCH: Invalid flags passed to dispatch_block_perform()
BUG IN CLIENT OF LIBDISPATCH: Unsupported callbacks version
BUG IN LIBDISPATCH: unexpected receipt of no-more-senders
queue_concurrent
queue_pthread_root
BUG in libdispatch: %s: \"%s\" - 0x%x{ 0x%llx[%s], ident: %lld / 0x%llx, handler: %p }
signal
monitor
B40@?0^{dispatch_data_s=[0{dispatch_object_s=[0{_os_object_s=^{_os_object_vtable_s}ii}]^{dispatch_object_vtable_s}ii^{dispatch_object_s}^{dispatch_queue_s}^v(?=^?^v)}][0{_os_object_s=^{_os_object_vtable_s}ii}]^{dispatch_data_vtable_s}ii^{di
BUG IN DISPATCH: Invalid wi flags = %u
BUG IN CLIENT OF LIBDISPATCH: Too many nested calls to dispatch_group_enter()
BUG IN CLIENT OF LIBDISPATCH: Cannot change the target of this object after it has been activated
BUG IN CLIENT OF LIBDISPATCH: workloop qos class or priority must be set before cpupercent
BUG IN CLIENT OF LIBDISPATCH: Called drain twice in the same invoke
API MISUSE: Voucher over-release
BUG IN LIBDISPATCH: Pending thread request underflow
BUG IN LIBDISPATCH: Premature thread exit while a dispatch frame is active
BUG IN CLIENT OF LIBDISPATCH: trying to lock recursively
mach_recv (channel)
Previous voucher: 0x%x, 
 %02x
composite, size = %zd, num_records = %zd 
record[%zd] = { from = %zd, length = %zd, data_object = %p }, 
BUG IN LIBDISPATCH: dispatch_data_copy_region out of bounds
com.apple.coreaudio.hal.clientthread
API MISUSE: Object type does not support resume
IMPORTANCE INFO: %s
BUG IN LIBDISPATCH: Too many deferred free items
enable
EVFILT_EXCLAVES_NOTIFICATION
BUG IN LIBDISPATCH: Unable to get the unique pid (size)
BUG IN CLIENT OF LIBDISPATCH: trying to install hooks with unsupported version
queue_runloop
stderr
Changing the target of a source after it has been activated
kern.wq_limit_cooperative_threads
dispatch_mig_server: mach_msg() failed
com.apple.root.libdispatch-manager
BUG IN LIBDISPATCH: unexpected receipt of port-destroyed
API MISUSE: Voucher resurrection
LIBDISPATCH_STRICT
LIBDISPATCH_DISABLE_KEVENT_WQ
EVFILT_AIO
BUG IN CLIENT OF LIBDISPATCH: Invalid queue attribute
workloop
API MISUSE: Over-release of an object
BUG IN LIBDISPATCH: Unsupported wlh configuration
mach reply
BUG IN LIBDISPATCH: QoS Maintenance support required
Clearing handler after the source has been activated
 } }
BUG IN CLIENT OF LIBDISPATCH: Channel never connected
 (pending)
EVFILT_SIGNAL
BUG IN LIBDISPATCH: Invalid msg aux data size.
cancelled, 
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_mig_demux_get_context not called from dispatch_mach_mig_demux context
com.apple.backboardd.displaythread
, dirty
BUG IN CLIENT OF LIBDISPATCH: Voucher importance count underflow
BUG IN CLIENT of %s: Mismatched workload ID and port interval type: %s vs %hd
BUG in libdispatch client: %s %s{ 0x%llx[%s], ident: %lld / 0x%llx, handler: %p }
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_kevent_vanished
BUG IN CLIENT OF LIBDISPATCH: A block object may not be both run more than once and observed
BUG IN CLIENT OF LIBDISPATCH: Waiter pushed onto manager
BUG IN CLIENT OF LIBDISPATCH: Invalid source type
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_hooks_install_4libxpc called twice
BUG IN LIBDISPATCH: Invalid kevent priority
com.apple.libdispatch-io.opq
LIBDISPATCH_CONTINUATION_ALLOCATOR
Y
MIG_REPLY_MISMATCH
BUG IN LIBDISPATCH: mach semaphore API failure
BUG IN LIBDISPATCH: Deferred continuation on source, mach channel or mgr
kevent = %p%s, filter = %s }
timer (interval)
com.apple.root.workloop-custom.overcommit
file
BUG IN CLIENT OF LIBDISPATCH: Queue doesn't support dispatch_queue_set_specific
Command: %u, 
BUG IN CLIENT OF LIBDISPATCH: Unable to make memory port
}
block
BUG IN CLIENT OF LIBDISPATCH: Corrupted priority
BUG IN CLIENT OF LIBDISPATCH: Unknown entity
BUG IN CLIENT OF LIBDISPATCH: Use-after-free of dispatch_semaphore_t or dispatch_group_t
BUG IN CLIENT OF LIBDISPATCH: dispatch queue/source property setter called after activation
BUG IN CLIENT OF LIBDISPATCH: Invalid threads_per_cluster value, only acceptable value is 1
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_mig_demux: mach_msg(MACH_SEND_MSG) failed
BUG IN CLIENT OF LIBDISPATCH: kqueue() failure: kernel is out of memory
BUG IN CLIENT OF LIBDISPATCH: Could not create task mach voucher
mach
BUG IN CLIENT OF LIBDISPATCH: Unbalanced call to dispatch_group_leave()
, max qos %d
BUG IN CLIENT OF LIBDISPATCH: _dispatch_main_queue_callback_4CF called from the wrong thread
BUG IN CLIENT OF LIBDISPATCH: dispatch_workloop os_workgroup_join failed
BUG IN CLIENT OF LIBDISPATCH: Cannot change a handler of this source after it has been activated
queue_cooperative
BUG in libdispatch client: %s %s: \"%s\" - 0x%x { 0x%llx[%s], ident: %lld / 0x%llx, handler: %p }
BUG IN LIBDISPATCH: ulock_wake() failed
LIBDISPATCH_COOPERATIVE_POOL_STRICT
dispatch source activated with no event handler set
BUG IN LIBDISPATCH: Root queue initialization failed
>, 
BUG IN CLIENT OF LIBDISPATCH: Unable to create signal thread
closed, 
BUG IN CLIENT OF LIBDISPATCH: Setting interval to 0
BUG IN CLIENT OF LIBDISPATCH: Message already enqueued
BUG IN LIBDISPATCH: message received without expected trailer
BUG IN CLIENT OF LIBDISPATCH: kqueue() failure: system is out of file descriptors
API MISUSE: Resurrection of an over-released object
BUG IN CLIENT OF LIBDISPATCH: Unexpected dispatch object type
BUG IN CLIENT of %s: Mismatched workload ID and workgroup interval type: %s vs %hd
cur_wg == NULL
Join token is corrupt
BUG IN CLIENT OF LIBDISPATCH: Filter id should be non-NULL
BUG IN CLIENT OF LIBDISPATCH: Trying to handoff IPC from non IPC context
sock
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_wait()
Changing the target of a queue already targeted by other dispatch objects
Setting registration handler after the source has been activated
opts/err = 0x%x, msgh[%p] = { 
stopped, 
BUG IN CLIENT OF LIBDISPATCH: pthread_start os_workgroup_join failed
BUG IN CLIENT of %s: Unable to set kernel workload ID: %s (0x%x) -> %d (0x%x)
channel
BUG IN CLIENT OF LIBDISPATCH: dispatch_set_qos_class called on invalid object type
BUG IN CLIENT OF LIBDISPATCH: Premature release of a locked queue
, in-flight = %d
BUG IN CLIENT OF LIBDISPATCH: Cannot target object to cooperative root queue - not implemented
BUG IN CLIENT OF LIBDISPATCH: Process has too many threads.
BUG IN LIBDISPATCH: dq_activate called
BUG IN LIBDISPATCH: Trailer doesn't contain filter policy id
com.apple.root.default-qos.cooperative
EVFILT_SOCK
BUG IN CLIENT OF LIBDISPATCH: Absurd publen
, activating
BUG IN LIBDISPATCH: MACH_RCV_LARGE_IDENTITY with no identity
BUG IN CLIENT OF LIBDISPATCH: Memory corruption in the logging buffers
BUG IN CLIENT OF LIBDISPATCH: dispatch_main called from a block on the main queue
BUG IN CLIENT of %s: Non-default workload type: %s (%hd)
_os_workgroup_set_work_interval_workload_id
BUG IN LIBDISPATCH: Corrupt thread event value
BUG IN LIBDISPATCH: Changing the QoS while on the manager queue
Key: %u, 
deleted, 
semaphore
source
BUG IN CLIENT OF LIBDISPATCH: Release of a channel that has not been cancelled, but has a cancel acknowledgement callback
BUG IN CLIENT OF LIBDISPATCH: Transition to multithreaded is prohibited
BUG IN CLIENT OF LIBDISPATCH: sync waiter found on channel
BUG IN CLIENT OF LIBDISPATCH: Voucher port corruption
DISPATCH_EVFILT_CUSTOM_REPLACE
TRUE
DISPATCH_EVFILT_TIMER
BUG in libdispatch client: _dispatch_kevent_mach_msg_drain: dropped message too large to fit in memory: id = 0x%x, size = %u
BUG IN CLIENT OF LIBDISPATCH: Couldn't get debug control port
<unknown>
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_testcancel()
BUG IN CLIENT OF LIBDISPATCH: Queue type doesn't support dispatch_sync
timer (after)
BUG IN CLIENT OF LIBDISPATCH: invalid queue passed to dispatch_am_i_on_queue_4swiftonly()
com.apple.libdispatch-io.channelq
type = %s, fd = 0x%lx, %sfd_entry = %p, queue = %p, target = %s[%p], barrier_queue = %p, barrier_group = %p, err = 0x%x, low = 0x%zx, high = 0x%zx, interval%s = %llu 
BUG IN CLIENT OF LIBDISPATCH: Workload identifier must not be NULL
com.apple.coremedia
BUG in libdispatch client: %s %s - 0x%x
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_kevent_client
BUG IN LIBDISPATCH: Underflow of tbkqwl count
BUG IN CLIENT OF LIBDISPATCH: dispatch_apply_attr not initialized using dispatch_apply_attr_init
mach_mig_demux
BUG IN CLIENT OF LIBDISPATCH: Do not close random Unix descriptors
BUG IN LIBDISPATCH: Invalid workgroup port
com.apple.root.workloop-custom
BUG IN CLIENT OF LIBDISPATCH: Reply port needed for async send with reply
memorystatus
BUG IN CLIENT OF LIBDISPATCH: Invalid size for the firehose buffer
com.apple.root.user-initiated-qos.cooperative
BUG IN CLIENT OF LIBDISPATCH: The executable is already multithreaded
delete
BUG IN CLIENT OF LIBDISPATCH: Overlarge message received
value = %ld, orig = %ld }
BUG IN CLIENT OF LIBDISPATCH: attribute's properties are invalid or meaningless on this system
data-add
exclaves_notification
sigterm (xpc)
\n
Join token provided is for a different workgroup than the last one joined by thread
Thread is not a member of the workgroup
com.apple.root.maintenance-qos
BUG IN LIBDISPATCH: Unexpected __ulock_wait error
BUG IN CLIENT OF LIBDISPATCH: Release of a workloop with corrupt state
BUG IN CLIENT OF LIBDISPATCH: Too many nested calls to dispatch_suspend()
mach_send (mach)
EVFILT_USER
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_notify()
BUG IN CLIENT OF LIBDISPATCH: 0 is an invalid threads_per_cluster value
BUG IN LIBDISPATCH: EVFILT_MACHPORT with overlarge message
BUG IN LIBDISPATCH: Unexpected event
BUG IN LIBDISPATCH: Invalid values for MADVISE_CHUNK_COUNT / CHUNK_SIZE
firehose
```
