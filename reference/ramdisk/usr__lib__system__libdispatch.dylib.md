# `/usr/lib/system/libdispatch.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 639,136 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 33 (Size: 4144)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (12)

- `/usr/lib/system/libdispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libcompiler_rt.dylib (compatibility version 1.0.0, current version 103.4.0)`
- `/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.1)`
- `/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/usr/lib/system/libsystem_pthread.dylib (compatibility version 1.0.0, current version 553.40.2)`
- `/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0)`
- `/usr/lib/system/libsystem_darwin.dylib (compatibility version 1.0.0, current version 1.0.0, upward)`
- `/usr/lib/system/libunwind.dylib (compatibility version 1.0.0, current version 2200.5.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0, upward)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (30 classes, 46 protocols)

Classes: `OS_dispatch_channel`, `OS_dispatch_data`, `OS_dispatch_data_empty`, `OS_dispatch_disk`, `OS_dispatch_group`, `OS_dispatch_io`, `OS_dispatch_mach`, `OS_dispatch_mach_msg`, `OS_dispatch_object`, `OS_dispatch_operation`, `OS_dispatch_queue`, `OS_dispatch_queue_attr`, `OS_dispatch_queue_concurrent`, `OS_dispatch_queue_cooperative`, `OS_dispatch_queue_global`, `OS_dispatch_queue_main`, `OS_dispatch_queue_mgr`, `OS_dispatch_queue_pthread_root`, `OS_dispatch_queue_runloop`, `OS_dispatch_queue_serial`, `OS_dispatch_queue_serial_executor`, `OS_dispatch_semaphore`, `OS_dispatch_source`, `OS_dispatch_workloop`, `OS_object`, `OS_os_eventlink`, `OS_os_workgroup`, `OS_os_workgroup_interval`, `OS_os_workgroup_parallel`, `OS_voucher`

Protocols: `NSObject`, `OS_dispatch_channel`, `OS_dispatch_data`, `OS_dispatch_disk`, `OS_dispatch_group`, `OS_dispatch_io`, `OS_dispatch_mach`, `OS_dispatch_mach_msg`, `OS_dispatch_object`, `OS_dispatch_operation`, `OS_dispatch_queue`, `OS_dispatch_queue_attr`, `OS_dispatch_queue_concurrent`, `OS_dispatch_queue_cooperative`, `OS_dispatch_queue_global`, `OS_dispatch_queue_main`, `OS_dispatch_queue_mgr`, `OS_dispatch_queue_pthread_root`, `OS_dispatch_queue_runloop`, `OS_dispatch_queue_serial`, `OS_dispatch_queue_serial_executor`, `OS_dispatch_semaphore`, `OS_dispatch_source`, `OS_dispatch_source_data_add`, `OS_dispatch_source_data_or`, `OS_dispatch_source_data_replace`, `OS_dispatch_source_exclaves_notification`, `OS_dispatch_source_interval`, `OS_dispatch_source_mach_recv`, `OS_dispatch_source_mach_send`, `OS_dispatch_source_memorypressure`, `OS_dispatch_source_memorystatus`, `OS_dispatch_source_nw_channel`, `OS_dispatch_source_proc`, `OS_dispatch_source_read`, `OS_dispatch_source_signal`, `OS_dispatch_source_sock`, `OS_dispatch_source_timer`, `OS_dispatch_source_vfs`, `OS_dispatch_source_vm`, `OS_dispatch_source_vnode`, `OS_dispatch_source_write`, `OS_dispatch_workloop`, `OS_object`, `OS_os_workgroup_interval`, `OS_os_workgroup_parallel`

## Strings (631)

```
^v16@0:8
@16@0:8
v16@0:8
B24@0:8@16
#16@0:8
B24@0:8:16
B24@0:8@\"Protocol\"16
@\"NSString\"16@0:8
v24@0:8^?16
Vv16@0:8
Q16@0:8
@40@0:8:16@24@32
B24@0:8#16
^{_NSZone=}16@0:8
@24@0:8^{_NSZone=}16
@44@0:8^v16Q24B32B36B40
v24@0:8@16
@24@0:8:16
@32@0:8:16@24
r^v16@0:8
B16@0:8
v24@0:8^v16
BUG IN LIBDISPATCH: do_dispose called
BUG IN CLIENT OF LIBDISPATCH: Release of a locked workloop
timer (interval)
BUG IN CLIENT OF LIBDISPATCH: Unable to make memory port
composite, size = %zd, num_records = %zd 
DISPATCH_DEBUG_MISSING_POOLS
BUG IN CLIENT OF LIBDISPATCH: Not a runloop queue
BUG IN CLIENT OF LIBDISPATCH: Cannot target source to the cooperative root queue - not implemented
BUG IN LIBDISPATCH: Trailer doesn't contain filter policy id
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_mig_demux: mach_msg(MACH_SEND_MSG) failed
com.apple.coremedia
BUG IN LIBDISPATCH: Invalid kevent priority
BUG IN LIBDISPATCH: Corrupt thread event value
BUG IN CLIENT OF LIBDISPATCH: invalid queue passed to dispatch_assert_queue()
Changing the target of a source after it has been activated
BUG IN CLIENT OF LIBDISPATCH: invalid queue passed to dispatch_assert_queue_not()
BUG IN CLIENT OF LIBDISPATCH: Called peek after drain
<unknown>
BUG IN CLIENT OF LIBDISPATCH: dispatch_apply_attr not initialized using dispatch_apply_attr_init
BUG IN CLIENT of %s: Mismatched workload ID and port interval type: %s vs %hd
mach_send (mach)
EVFILT_MEMORYSTATUS
BUG IN CLIENT OF LIBDISPATCH: Corruption: failed to clear bit exclusively
source
BUG IN CLIENT OF LIBDISPATCH: Release of a source that has not been cancelled, but has a mandatory cancel handler
Changing target queue hierarchy after xpc connection was activated
data-or
vm (deprecated)
BUG IN LIBDISPATCH: MACH_RCV_LARGE_IDENTITY with no identity
BUG IN CLIENT OF LIBDISPATCH: Unexpected error from kevent
=== log file opened for %s[%u] at %ld.%06u ===\n
API MISUSE: Object type does not support suspension
BUG IN CLIENT OF LIBDISPATCH: Channel didn't call dispatch_channel_drain
timer = { target = 0x%llx, deadline = 0x%llx, interval = 0x%llx, flags = 0x%x }, 
BUG IN CLIENT OF LIBDISPATCH: trying to install hooks with unsupported version
EVFILT_FS
BUG IN LIBDISPATCH: mach_voucher_attr_command(BANK_PERSONA_ADOPT_ANY) failed
BUG IN CLIENT OF LIBDISPATCH: _dispatch_mach_default_async_reply_handler called
BUG IN LIBDISPATCH: Joined count underflowed
BUG IN CLIENT OF LIBDISPATCH: Workload identifier must not be NULL
monitor
 & ipc kvoucher
BUG IN CLIENT OF LIBDISPATCH: Invalid pthread root queue observer hooks
workgroup.c
BUG IN LIBDISPATCH: Unable to get the unique pid (error)
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_deprecated
BUG IN CLIENT OF LIBDISPATCH: invalid queue passed to dispatch_am_i_on_queue_4swiftonly()
BUG IN LIBDISPATCH: QoS Maintenance support required
BUG IN CLIENT of %s: Non-default workload type: %s (%hd)
BUG IN LIBDISPATCH: Trailer format is invalid
vfs
sigterm (xpc)
EVFILT_USER
OBJC_DEBUG_MISSING_POOLS
%s[%p] = { 
BUG IN CLIENT OF LIBDISPATCH: Group object deallocated while in use
BUG IN CLIENT OF LIBDISPATCH: Unexpected dispatch object type
com.apple.coreaudio.hal.iothread
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_mig_demux_get_context not called from dispatch_mach_mig_demux context
Changing target queue hierarchy with a dispatch_sync in flight
EVFILT_AIO
BUG IN CLIENT OF LIBDISPATCH: Unbalanced call to dispatch_group_leave()
BUG IN LIBDISPATCH: Don't try to wake up or override the manager
LIBDISPATCH_COOPERATIVE_POOL_STRICT
DISPATCH_EVFILT_CUSTOM_ADD
LIBDISPATCH_TIMERS_FORCE_MAX_LEEWAY
BUG IN CLIENT OF LIBDISPATCH: Failed to initalize workqueue kevent
Voucher: 0x%x has no contents\n
MallocStackLogging
BUG in libdispatch client: %s, monitored resource vanished before the source cancel handler was invoked { %p[%s], ident: %d / 0x%x, handler: %p }
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_testcancel()
BUG IN LIBDISPATCH: Invalid way to wake up a workloop
BUG IN CLIENT OF LIBDISPATCH: Message already enqueued
Invalid voucher: 0x%x\n
%s%s:\n
BUG IN CLIENT OF LIBDISPATCH: Too many nested calls to dispatch_group_enter()
BUG IN CLIENT OF LIBDISPATCH: Cannot change a handler of this source after it has been activated
com.apple.root.utility-qos.cooperative
BUG IN LIBDISPATCH: _pthread_set_properties_self failed
Changing the target of a queue already targeted by other dispatch objects
>, 
EVFILT_WORKLOOP
BUG IN CLIENT OF LIBDISPATCH: Unable to copyout msg, possible port leak
BUG IN CLIENT OF LIBDISPATCH: Corruption of dispatch block object
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_wait()
BUG IN CLIENT OF LIBDISPATCH: Invalid source type
size %u, 
LIBDISPATCH_STRICT: _dispatch_bug_mach_client
v20@?0^{dispatch_data_s=^v^{dispatch_queue_s}^v^?^v@?QQ[0{range_record_s=^{dispatch_data_s}QQ}]}8i16
BUG IN CLIENT OF LIBDISPATCH: Invalid queue attribute
, thread = 0x%x 
target = %s[%p], receive = 0x%x, send = 0x%x, send-possible = 0x%x%s, checkin = 0x%x%s, send state = %016llx, disconnected = %d, canceled = %d 
BUG IN CLIENT OF LIBDISPATCH: Unable to allocate mach port
com.apple.libdispatch-io.barrierq
com.apple.root.workloop-custom.overcommit
_os_workgroup_join_update_wg
Previous voucher: 0x%x, 
BUG IN LIBDISPATCH: EVFILT_MACHPORT with no message
\n
apply
BUG IN LIBDISPATCH: Unexpected event
BUG IN CLIENT OF LIBDISPATCH: Could not allocate heap
BUG IN CLIENT OF LIBDISPATCH: dispatch_source_cancel_and_wait called from a source handler
BUG IN LIBDISPATCH: EVFILT_MACHPORT with overlarge message
BUG IN CLIENT OF LIBDISPATCH: Release of a queue with corrupt state
BUG IN CLIENT OF LIBDISPATCH: dispatch_main() must be called on the main thread
BUG IN CLIENT of %s: Mismatched workload ID and workgroup interval type: %s vs %hd
The arena associated with workgroup is not to be partitioned
BUG IN CLIENT OF LIBDISPATCH: Trying to handoff IPC from non IPC context
BUG IN CLIENT OF LIBDISPATCH: Owner in ulock is unknown - possible memory corruption
BUG IN CLIENT OF LIBDISPATCH: 0 is an invalid threads_per_cluster value
BUG IN CLIENT OF LIBDISPATCH: Messsage should be non-NULL
BUG IN LIBDISPATCH: dispatch_data_create_subrange out of bounds
com.apple.root.background-qos.cooperative
count = %u, gen = %d, waiters = %d, notifs = %d }
mach_recv
type = %s %s, fd = 0x%lx, fd_entry = %p, channel = %p, queue = %p -> %s[%p], target = %s[%p], offset = %lld, length = %zu, done = %zu, undelivered = %zu, flags = %u, err = 0x%x, low = 0x%zx, high = 0x%zx, interval%s = %llu 
BUG IN CLIENT OF LIBDISPATCH: workloop qos class or priority must be set before cpupercent
BUG IN CLIENT OF LIBDISPATCH: Unsupported callbacks version
BUG IN CLIENT OF LIBDISPATCH: Corrupted priority
com.apple.coreaudio.hal.clientthread
BUG IN LIBDISPATCH: firehose_mig_server doesn't handle replies
BUG IN CLIENT OF LIBDISPATCH: NULL was passed where a block should have been
BUG IN DISPATCH: Invalid wi flags = %u
BUG in libdispatch client: dispatch_mach_send_and_wait_for_reply: dropped message too large to fit in memory: id = 0x%x, size = %u
BUG IN CLIENT OF LIBDISPATCH: Received message with MACH_PORT_NULL msgh_local_port
BUG IN CLIENT OF LIBDISPATCH: Could not create task mach voucher
com.apple.root.user-initiated-qos.overcommit
<%s: %s>
com.apple.libdispatch
BUG IN LIBDISPATCH: Invalid values for MADVISE_CHUNK_COUNT / CHUNK_SIZE
BUG IN LIBDISPATCH: Deferred continuation on source, mach channel or mgr
com.apple.main-thread
com.apple.root.user-interactive-qos.overcommit
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_kevent_client
BUG IN CLIENT OF LIBDISPATCH: Semaphore object deallocated while in use (current value < original value)
, in-barrier
BUG IN CLIENT OF LIBDISPATCH: voucher_activity_initialize_4libtrace called twice
firehose
BUG IN LIBDISPATCH: Interrupted drain on manager queue
vnode
Command: %u, 
BUG IN LIBDISPATCH: vmdeallocate destructor called
LIBDISPATCH_STRICT: _dispatch_bug_kevent_client
<released queue, pending free>
BUG IN LIBDISPATCH: firehose_push_reply should never be sent to the buffer receive port
 } }
BUG IN CLIENT OF LIBDISPATCH: Invalid reply port
EVFILT_READ
Key: %u, 
com.apple.root.default-qos.cooperative
BUG IN LIBDISPATCH: none destructor called
BUG IN CLIENT OF LIBDISPATCH: A block object may not be both run more than once and observed
BUG IN CLIENT OF LIBDISPATCH: Release of a suspended object
needs-event, 
BUG IN LIBDISPATCH: Unable to get the unique pid (size)
BUG IN CLIENT OF LIBDISPATCH: Used Swift only SPI to enqueue non-Swift runtime objects into dispatch
BUG IN CLIENT: Releasing last reference to workgroup interval while an interval has been started
com.apple.backboardd.displaythread
mach_recv (channel)
opts/err = 0x%x, msgh[%p] = { 
type = %s, fd = 0x%lx, %sfd_entry = %p, queue = %p, target = %s[%p], barrier_queue = %p, barrier_group = %p, err = 0x%x, low = 0x%zx, high = 0x%zx, interval%s = %llu 
, in-flight = %d
BUG IN CLIENT OF LIBDISPATCH: Cannot specify an overcommit attribute and use this kind of target queue
BUG IN CLIENT OF LIBDISPATCH: Unable to create signal thread
target = %s[%p], ident = 0x%llx, mask = 0x%x, pending_data = 0x%llx, registered = %d, armed = %d, %s%s%s
BUG in libdispatch client: %s %s: \"%s\" - 0x%x { 0x%llx[%s], ident: %lld / 0x%llx, handler: %p }
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_cancel()
BUG IN CLIENT OF LIBDISPATCH: Release of a queue while items are enqueued
BUG IN LIBDISPATCH: Premature thread exit with unhandled deferred items
BUG IN CLIENT of %s: Mismatched workload ID and attribute interval type: %s vs %hd
BUG IN CLIENT OF LIBDISPATCH: Message size too large
com.apple.root.user-interactive-qos
NSString
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_mach_client
API MISUSE: Object type does not support resume
BUG IN CLIENT OF LIBDISPATCH: Release of an inactive object
BUG IN CLIENT OF LIBDISPATCH: Unexpected EV_VANISHED (do not destroy random mach ports)
Content size: %u\n
Recipe Contents
BUG IN LIBDISPATCH: Release while enqueued
BUG IN CLIENT OF LIBDISPATCH: Transition to multithreaded is prohibited
BUG IN CLIENT OF LIBDISPATCH: dispatch_workloop os_workgroup_join failed
BUG IN LIBDISPATCH: Unregistration failed
BUG IN LIBDISPATCH: Invalid wlh
  %s\n
com.apple.libdispatch-io.dev_lockq
BUG IN CLIENT OF LIBDISPATCH: Passing an invalid leeway
EVFILT_SIGNAL
, activity 0x%llx (pid: 0x%16llx, parent 0x%llx)
Join token provided is for a different thread
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_send_with_result_and_wait_for_reply is XPC only
BUG IN LIBDISPATCH: Allocation should always fail
 %02x
BUG IN CLIENT OF LIBDISPATCH: dispatch_set_qos_class called on invalid object type
mach_notification
EVFILT_EXCLAVES_NOTIFICATION
BUG IN CLIENT OF LIBDISPATCH: Log is too large
BUG IN CLIENT OF LIBDISPATCH: Invalid size for the firehose buffer
random
BUG IN CLIENT OF LIBDISPATCH: Cannot change the target of this object after it has been activated
BUG IN CLIENT OF LIBDISPATCH: dispatch_main called from a block on the main queue
BUG IN LIBDISPATCH: Invalid workgroup port
BUG IN LIBDISPATCH: Too many deferred free items
com.apple.libdispatch-io.channelq
com.apple.libdispatch.workloop_fallback
BUG IN CLIENT OF LIBDISPATCH: Release of a workloop while items are enqueued
%sBlock was expected to act as a barrier on queue [%s (%p)]
BUG IN CLIENT OF LIBDISPATCH: Filter id should be non-NULL
BUG IN CLIENT OF LIBDISPATCH: Unexpected EV_VANISHED (do not destroy random mach ports or file descriptors)
BUG IN CLIENT OF LIBDISPATCH: Changing target queue hierarchy after mach channel was connected
BUG IN LIBDISPATCH: Disposing of timer still in its heap
com.apple.root.user-initiated-qos.cooperative
BUG IN CLIENT OF LIBDISPATCH: Queue doesn't support dispatch_queue_set_specific
com.apple.libdispatch-io.deviceq.%d
BUG IN CLIENT OF LIBDISPATCH: dispatch_set_qos_class_fallback called on invalid object type
BUG IN CLIENT OF LIBDISPATCH: Cannot target object to cooperative root queue - not implemented
BUG IN CLIENT OF LIBDISPATCH: Too many nested calls to dispatch_suspend()
BUG IN CLIENT OF LIBDISPATCH: sync waiter found on channel
com.apple.root.maintenance-qos.cooperative
com.apple.root.background-qos
BUG IN CLIENT OF LIBDISPATCH: Release of a workloop with corrupt state
BUG IN CLIENT OF LIBDISPATCH: dispatch queue/source property setter called after activation
Setting registration handler after the source has been activated
(strict)
leaf, size = %zd, buf = %p 
LIBDISPATCH_STRICT: _dispatch_bug_deprecated
missing do_debug vtable slot: 
MIG_REPLY_MISMATCH
port = 0x%x, 
BUG IN CLIENT OF LIBDISPATCH: Over-resume of an inactive object
BUG IN CLIENT of %s: Invalid workload interval type: %s (%hd)
cur_wg == NULL
, o 0x%x
BUG IN CLIENT OF LIBDISPATCH: Cannot change label for this queue
BUG IN CLIENT OF LIBDISPATCH: Source is suspended
BUG IN CLIENT OF LIBDISPATCH: Start value is not DISPATCH_TIME_NOW or DISPATCH_TIME_FOREVER
local 0x%x, remote 0x%x
BUG IN CLIENT OF LIBDISPATCH: Absurd publen
LIBDISPATCH_LOG
BUG IN CLIENT OF LIBDISPATCH: Cannot change the target of a queue already targeted by other dispatch objects
dispatch_mig_server: mach_msg() failed
data-add
, ipc kvoucher 0x%x [\n
Y
, suspended = %d
BUG IN CLIENT OF LIBDISPATCH: Dispatch source used after last release
Join token is corrupt
BUG IN LIBDISPATCH: Invalid workload ID type
NULL: 
com.apple.root.maintenance-qos.overcommit
timer (fixed-clock)
BUG IN LIBDISPATCH: Broken priority
BUG IN LIBDISPATCH: unexpected receipt of no-more-senders
BUG IN CLIENT OF LIBDISPATCH: Release of a channel that has not been cancelled, but has a cancel acknowledgement callback
com.apple.backboardd.hid
BUG IN CLIENT OF LIBDISPATCH: Reply received on unexpected port
BUG IN LIBDISPATCH: Unsupported wlh configuration
EVFILT_PROC
BUG IN CLIENT OF LIBDISPATCH: Invalid send flags
com.apple.libdispatch-io.opq
com.apple.root.user-initiated-qos
Exceeded the maximum number of workers who can access the arena
 (armed)
Voucher: 0x%x Failed to get contents %s\n
BUG IN CLIENT OF LIBDISPATCH: Memory corruption in the logging buffers
BUG IN LIBDISPATCH: dispatch_data_copy_region out of bounds
com.apple.root.workloop-custom
com.apple.libsystem.libdispatch
BUG IN CLIENT OF LIBDISPATCH: Use-after-free of dispatch_semaphore_t or dispatch_group_t
EVFILT_missing
voucher[%p] = { xref = %d, ref = %d
v16@?0^{dispatch_fd_entry_s=i^{dispatch_io_path_data_s}iiiI{dispatch_stat_s=iS}[2^{dispatch_stream_s}]^{dispatch_disk_s}^{dispatch_queue_s}^{dispatch_queue_s}^{dispatch_group_s}^{dispatch_io_s}{?=^{dispatch_operation_s}^^{dispatch_operation
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_notify()
BUG IN LIBDISPATCH: Pending thread request underflow
stream
BUG IN CLIENT OF LIBDISPATCH: Called drain twice in the same invoke
kevent = %p%s, filter = %s }
memorystatus
BUG IN CLIENT OF LIBDISPATCH: Assertion failed: 
os_workgroup_create_with_workload_id_and_workgroup
BUG IN LIBDISPATCH: Waking up a kq with cooperative thread request is not supported
BUG in libdispatch: %s - %lu - 0x%llx
BUG IN CLIENT OF LIBDISPATCH: attribute's properties are invalid or meaningless on this system
BUG IN CLIENT OF LIBDISPATCH: Corrupt thread event value
mach_mig_demux
BUG IN CLIENT OF LIBDISPATCH: Overlarge message
BUG IN CLIENT OF LIBDISPATCH: Channel never connected
com.apple.root.default-qos
com.apple.root.background-qos.overcommit
BUG IN LIBDISPATCH: free destructor called
BUG IN LIBDISPATCH: Root queue initialization failed
BUG IN CLIENT OF LIBDISPATCH: Channel already connected
BUG IN CLIENT OF LIBDISPATCH: Unable to allocate reply port, possible port leak
BUG IN CLIENT OF LIBDISPATCH: Do not close random Unix descriptors
BUG IN LIBDISPATCH: Unable to limit cooperative pool size
BUG IN CLIENT OF LIBDISPATCH: Calling dispatch_mach_handoff_reply multiple times from the same context
BUG IN LIBDISPATCH: ulock_wake() failed
_os_workgroup_set_work_interval_workload_id
v12@?0i8
, flatbuf = %p 
BUG IN CLIENT OF LIBDISPATCH: dispatch_set_qos_class_floor called on invalid object type
BUG IN CLIENT OF LIBDISPATCH: Waiter pushed onto manager
BUG IN CLIENT of %s: Unable to set kernel workload ID: %s (0x%x) -> %d (0x%x)
BUG IN CLIENT OF LIBDISPATCH: Empty message
BUG IN CLIENT OF LIBDISPATCH: Voucher importance count underflow
B40@?0^{dispatch_data_s=^v^{dispatch_queue_s}^v^?^v@?QQ[0{range_record_s=^{dispatch_data_s}QQ}]}8Q16r^v24Q32
, max qos %d
BUG IN CLIENT of %s: Invalid workgroup port 0x%x
bits <l %u, r %u
, activating
BUG IN LIBDISPATCH: apply continuation has invalid flags
BUG IN LIBDISPATCH: Source finalized twice
os_workgroup_create_with_workload_id_and_port
delete
DISPATCH_EVFILT_CUSTOM_OR
com.apple.root.user-interactive-qos.cooperative
API MISUSE: Voucher over-release
BUG IN LIBDISPATCH: Lingering DISPATCH_WLH_ANON
Clearing handler after the source has been activated
BUG IN CLIENT OF LIBDISPATCH: Setting interval to 0
proc
BUG IN LIBDISPATCH: unexpected receipt of port-destroyed
io
BUG IN LIBDISPATCH: Premature thread exit while a dispatch context is set
dispatch source activated with no event handler set
BUG IN CLIENT of %s: Workgroup already cancelled
DISPATCH_EVFILT_MACH_NOTIFICATION
com.apple.libdispatch-io.fd_lockq
com.apple.root.utility-qos.overcommit
TRUE
BUG IN CLIENT OF LIBDISPATCH: Invalid threads_per_cluster value, only acceptable value is 1
Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?
BUG IN CLIENT OF LIBDISPATCH: unsupported vah_version
BUG IN LIBDISPATCH: Changing the QoS while on the manager queue
EVFILT_SOCK
BUG IN CLIENT OF LIBDISPATCH: Voucher port corruption
data-replace
BUG IN LIBDISPATCH: Unexpected __ulock_wait error
BUG IN CLIENT OF LIBDISPATCH: Corrupt activation state
BUG IN CLIENT OF LIBDISPATCH: Couldn't get debug control port
BUG IN LIBDISPATCH: dq_activate called
%s
BUG IN CLIENT OF LIBDISPATCH: _dispatch_main_queue_callback_4CF called from the wrong thread
BUG IN CLIENT OF LIBDISPATCH: Corrupt channel state
exclaves_notification
BUG IN LIBDISPATCH: do_invoke called
API MISUSE: Voucher resurrection
BUG IN LIBDISPATCH: Premature thread exit while a dispatch frame is active
/var/tmp/libdispatch.%d.log
BUG IN CLIENT OF LIBDISPATCH: The executable is already multithreaded
Creating an os_workgroup of unknown type
BUG IN CLIENT OF LIBDISPATCH: Mach port notification collision
read
DISPATCH_EVFILT_TIMER_WITH_CLOCK
BUG in libdispatch client: %s %s{ 0x%llx[%s], ident: %lld / 0x%llx, handler: %p }
LIBDISPATCH_DEBUG_MISSING_POOLS
BUG IN LIBDISPATCH: Cannot turn a manager thread into a normal one
BUG IN CLIENT OF LIBDISPATCH: Cannot set width of a serial queue
 (direct)
BUG IN CLIENT OF LIBDISPATCH: Invalid workloop owner, possible memory corruption
BUG IN CLIENT OF LIBDISPATCH: Invalid queue type
BUG IN CLIENT OF LIBDISPATCH: Too many calls to dispatch_suspend() prior to calling dispatch_set_target_queue() or dispatch_set_*_handler()
BUG IN CLIENT OF LIBDISPATCH: Invalid threads_per_entity value for CPU entity
LIBDISPATCH_NO_FAULTS
   
os_workgroup_create_with_workload_id
BUG IN LIBDISPATCH: Unexpected error from mach_msg_receive
kevent
EVFILT_MACHPORT
com.apple.libdispatch-io.streamq
LIBDISPATCH_CONTINUATION_ALLOCATOR
BUG IN CLIENT OF LIBDISPATCH: trying to lock recursively
}
deleted, 
v24@?0B8^{dispatch_data_s=^v^{dispatch_queue_s}^v^?^v@?QQ[0{range_record_s=^{dispatch_data_s}QQ}]}12i20
%s%s%s
]
file
no ports
BUG in libdispatch client: _dispatch_kevent_mach_msg_drain: dropped message too large to fit in memory: id = 0x%x, size = %u
BUG IN CLIENT OF LIBDISPATCH: Bound thread attribute set multiple times
closed, 
com.apple.libdispatch-manager
BUG IN LIBDISPATCH: mach semaphore API failure
add
EVFILT_TIMER
BUG IN CLIENT OF LIBDISPATCH: Voucher corruption
stopped, 
runloop-queue
BUG IN CLIENT OF LIBDISPATCH: Process has too many threads.
EVFILT_WRITE
BUG IN LIBDISPATCH: Corrupt unote action
, kvoucher%s 0x%x [\n
IMPORTANCE INFO: %s
EVFILT_VNODE
BUG IN LIBDISPATCH: base voucher has nested base voucher
BUG IN CLIENT OF LIBDISPATCH: -init called directly
mach reply
        
BUG IN LIBDISPATCH: base voucher has non-zero activity value
syslog
%sBlock was %sexpected to execute on queue [%s (%p)]
, dirty
, draining on 0x%x
BUG IN LIBDISPATCH: Premature thread exit while a dispatch queue is running
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_hooks_install_4libxpc called twice
API MISUSE: Resurrection of an object
BUG IN CLIENT OF LIBDISPATCH: Waking up an inactive workloop
BUG IN CLIENT OF LIBDISPATCH: _dispatch_main_queue_callback_4CF called after dispatch_main()
BUG IN CLIENT of %s: Non-default attribute flags: 0x%x
timer
BUG IN CLIENT OF LIBDISPATCH: pthread_start os_workgroup_join failed
YES
BUG in libdispatch client: %s %s - 0x%x
sref = %d, target = %s[%p], width = 0x%x, state = 0x%016llx
BUG IN CLIENT OF LIBDISPATCH: dispatch_sync called on queue already owned by current thread
BUG IN CLIENT OF LIBDISPATCH: Cannot specify both overcommit and a non-global target queue
BUG IN LIBDISPATCH: Invalid wlh state
BUG IN CLIENT OF LIBDISPATCH: Changing target queue hierarchy after source was activated
BUG IN CLIENT of %s: Invalid attribute pointer
BUG IN LIBDISPATCH: Underflow of tbkqwl count
BUG IN LIBDISPATCH: Locking the manager should not fail
BUG IN LIBDISPATCH: Unexpected error from mach recv
Thread is not a member of the workgroup
Changing target queue hierarchy after mach channel was connected
os_workgroup_interval_create_with_workload_id
mach_msg
BUG IN CLIENT OF LIBDISPATCH: Overlarge message received
BUG IN CLIENT OF LIBDISPATCH: Could not generate an activity ID
LIBDISPATCH_STRICT: _dispatch_bug_kevent_vanished
Voucher: 0x%x\n
DEPRECATED USE in libdispatch client: %s; set a breakpoint on _dispatch_bug_deprecated to debug
kern.wq_limit_cooperative_threads
BUG IN CLIENT: Thread exiting without leaving workgroup '%s'
 (pending)
DISPATCH_EVFILT_TIMER
BUG IN CLIENT OF LIBDISPATCH: A block object may not be both run more than once and waited for
com.apple.root.maintenance-qos
BUG IN CLIENT OF LIBDISPATCH: Premature release of a locked queue
BUG IN CLIENT OF LIBDISPATCH: mach_port_construct() failed: cannot create receive right
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
com.apple.root.default-qos.overcommit
, pending-barrier
BUG IN CLIENT of %s: Invalid mach port 0x%x
BUG IN LIBDISPATCH: message received without expected trailer
BUG IN CLIENT OF LIBDISPATCH: Could not get unprivileged host port
, base voucher %p
BUG IN CLIENT OF LIBDISPATCH: A block object may not be waited for more than once
BUG IN LIBDISPATCH: Don't try to wake up or override a root queue
local 0x%x
write
BUG IN CLIENT OF LIBDISPATCH: Over-resume of an object
cancelled, 
BUG IN CLIENT OF LIBDISPATCH: Unknown entity
BUG IN CLIENT OF LIBDISPATCH: Attempting to modify timer clock
mach_send
sock
 }
value = %ld, orig = %ld }
BUG IN LIBDISPATCH: Missing Kevent WORKQ support
id 0x%x, 
BUG IN CLIENT OF LIBDISPATCH: Unable to register with logd
BUG in libdispatch: %s: \"%s\" - 0x%x{ 0x%llx[%s], ident: %lld / 0x%llx, handler: %p }
stderr
xref = %d, ref = %d, 
BUG IN LIBDISPATCH: Cannot raise oneself to manager
BUG IN CLIENT OF LIBDISPATCH: Queue type doesn't support dispatch_sync
BUG IN CLIENT OF LIBDISPATCH: Unexpected non message event
BUG IN LIBDISPATCH: ulock_wait() failed
Join token provided is for a different workgroup than the last one joined by thread
BUG IN CLIENT OF LIBDISPATCH: Changing target queue hierarchy after xpc connection was activated
BUG IN LIBDISPATCH: EVFILT_MACHPORT with no message size
BUG IN LIBDISPATCH: Invalid msg aux data size.
BUG IN CLIENT OF LIBDISPATCH: Invalid arguments
%s  %04lx 
BUG IN CLIENT OF LIBDISPATCH: firehose_drain_notifications_once() failed
LIBDISPATCH_STRICT
BUG IN LIBDISPATCH: Unexpected object type
enable
BUG IN CLIENT OF LIBDISPATCH: Invalid flags passed to dispatch_block_perform()
BUG IN CLIENT OF LIBDISPATCH: Unsupported interface
, enqueued
Changing target queue hierarchy after source was activated
wg[%p] = {xref = %d, ref = %d, name = %s}
timer (after)
API MISUSE: Resurrection of an over-released object
, inactive
DISPATCH_EVFILT_CUSTOM_REPLACE
_dispatch_kevent_mach_msg_drain: message reception failed
BUG IN CLIENT OF LIBDISPATCH: Reply port needed for async send with reply
RESOURCE ACCOUNTING INFO: %s
com.apple.root.utility-qos
API MISUSE: Over-release of an object
BUG IN LIBDISPATCH: Unexpected error from kevent
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_kevent_vanished
BUG IN CLIENT OF LIBDISPATCH: _dispatch_source_will_reenable_kevent_4NW not called from within the event handler
signal
remote 0x%x
com.apple.libdispatch-io.closeq
data[%p] = { 
, activated
not 
nw_channel
record[%zd] = { from = %zd, length = %zd, data_object = %p }, 
v8@?0
BUG IN LIBDISPATCH: inline destructor called
BUG IN CLIENT OF LIBDISPATCH: Cannot target the cooperative root queue - not implemented
BUG IN CLIENT OF LIBDISPATCH: Source has a cancel handler
BUG IN CLIENT OF LIBDISPATCH: Attempt to set timer on a non-timer source
com.apple.debug-channel
BUG IN CLIENT OF LIBDISPATCH: lock not owned by current thread
OS_dispatch_source_memorystatus
OS_dispatch_source_proc
OS_dispatch_source_data_or
OS_dispatch_group
OS_dispatch_queue_main
NSObject
OS_dispatch_source_vfs
OS_dispatch_data
OS_dispatch_source_exclaves_notification
OS_dispatch_source_vnode
OS_dispatch_source_mach_recv
OS_dispatch_source_data_replace
OS_dispatch_source_data_add
OS_dispatch_queue_serial_executor
OS_os_workgroup
OS_os_workgroup_parallel
OS_object
OS_dispatch_source_sock
OS_dispatch_source_vm
OS_dispatch_source_interval
OS_dispatch_semaphore
OS_os_eventlink
OS_voucher
OS_dispatch_workloop
OS_dispatch_queue_cooperative
OS_dispatch_io
OS_dispatch_data_empty
OS_dispatch_channel
OS_dispatch_source_write
OS_dispatch_source_timer
OS_dispatch_source_mach_send
OS_dispatch_queue_runloop
OS_dispatch_queue_serial
OS_dispatch_queue_concurrent
OS_dispatch_queue_global
OS_dispatch_source
OS_dispatch_source_signal
OS_dispatch_source_memorypressure
OS_dispatch_queue_pthread_root
OS_dispatch_queue_mgr
OS_dispatch_queue_attr
OS_dispatch_mach_msg
OS_dispatch_disk
OS_dispatch_queue
OS_dispatch_source_nw_channel
OS_dispatch_source_read
OS_dispatch_mach
OS_dispatch_operation
OS_os_workgroup_interval
OS_dispatch_object
isProxy
TQ,R,N
_bytesAreVM
isMemberOfClass:
length
stringWithFormat:
T@\"NSString\",R,C
init
zone
T#,R
dealloc
Tr^v,R,N
_isCompact
_suspend
class
conformsToProtocol:
hash
_resume
_setContext:
bytes
isEqual:
isKindOfClass:
performSelector:
performSelector:withObject:
respondsToSelector:
_setFinalizer:
allocWithZone:
getBytes:maxLength:usedLength:encoding:options:range:remainingRange:
initWithBytes:length:copy:freeWhenDone:bytesAreVM:
retain
self
release
_activate
_getContext
_xref_dispose
allowsWeakReference
performSelector:withObject:withObject:
retainWeakReference
superclass
autorelease
retainCount
stringWithUTF8String:
T@\"NSString\",?,R,C
TQ,R
_setTargetQueue:
debugDescription
description
```
