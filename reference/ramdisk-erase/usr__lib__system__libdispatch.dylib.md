# `/usr/lib/system/libdispatch.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 639,136 bytes.

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
Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?
os_workgroup_create_with_workload_id
cur_wg == NULL
BUG in libdispatch client: dispatch_mach_send_and_wait_for_reply: dropped message too large to fit in memory: id = 0x%x, size = %u
EVFILT_WRITE
LIBDISPATCH_DEBUG_MISSING_POOLS
BUG IN CLIENT OF LIBDISPATCH: Unsupported callbacks version
BUG IN CLIENT OF LIBDISPATCH: Too many calls to dispatch_suspend() prior to calling dispatch_set_target_queue() or dispatch_set_*_handler()
Setting registration handler after the source has been activated
EVFILT_EXCLAVES_NOTIFICATION
BUG IN CLIENT OF LIBDISPATCH: firehose_drain_notifications_once() failed
Exceeded the maximum number of workers who can access the arena
com.apple.backboardd.hid
BUG IN CLIENT OF LIBDISPATCH: Unexpected error from kevent
v24@?0B8^{dispatch_data_s=^v^{dispatch_queue_s}^v^?^v@?QQ[0{range_record_s=^{dispatch_data_s}QQ}]}12i20
LIBDISPATCH_STRICT: _dispatch_bug_kevent_client
BUG IN CLIENT OF LIBDISPATCH: dispatch_set_qos_class_fallback called on invalid object type
BUG IN CLIENT OF LIBDISPATCH: Queue type doesn't support dispatch_sync
Changing target queue hierarchy after mach channel was connected
BUG IN LIBDISPATCH: message received without expected trailer
BUG IN CLIENT OF LIBDISPATCH: Couldn't get debug control port
OBJC_DEBUG_MISSING_POOLS
<%s: %s>
BUG IN CLIENT OF LIBDISPATCH: Release of a source that has not been cancelled, but has a mandatory cancel handler
wg[%p] = {xref = %d, ref = %d, name = %s}
EVFILT_MACHPORT
DISPATCH_EVFILT_CUSTOM_REPLACE
NSString
BUG IN LIBDISPATCH: Changing the QoS while on the manager queue
com.apple.main-thread
API MISUSE: Object type does not support resume
workgroup.c
write
BUG IN LIBDISPATCH: mach_voucher_attr_command(BANK_PERSONA_ADOPT_ANY) failed
dispatch source activated with no event handler set
BUG IN CLIENT OF LIBDISPATCH: Source is suspended
BUG IN LIBDISPATCH: Trailer doesn't contain filter policy id
BUG IN LIBDISPATCH: Invalid kevent priority
EVFILT_SOCK
com.apple.root.maintenance-qos.overcommit
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_kevent_client
<unknown>
not 
BUG IN LIBDISPATCH: Source finalized twice
BUG IN LIBDISPATCH: Unable to get the unique pid (error)
com.apple.libdispatch
Content size: %u\n
EVFILT_missing
Voucher: 0x%x has no contents\n
BUG IN LIBDISPATCH: Invalid workgroup port
BUG IN CLIENT OF LIBDISPATCH: Corruption: failed to clear bit exclusively
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_notify()
, thread = 0x%x 
BUG IN CLIENT OF LIBDISPATCH: Too many nested calls to dispatch_suspend()
com.apple.libdispatch-io.fd_lockq
record[%zd] = { from = %zd, length = %zd, data_object = %p }, 
com.apple.root.user-interactive-qos.cooperative
, in-barrier
BUG IN LIBDISPATCH: Don't try to wake up or override a root queue
BUG IN CLIENT OF LIBDISPATCH: Unable to create signal thread
BUG IN CLIENT OF LIBDISPATCH: dispatch_apply_attr not initialized using dispatch_apply_attr_init
BUG IN CLIENT OF LIBDISPATCH: Unexpected EV_VANISHED (do not destroy random mach ports)
, kvoucher%s 0x%x [\n
firehose
BUG IN CLIENT OF LIBDISPATCH: dispatch_set_qos_class called on invalid object type
BUG IN CLIENT OF LIBDISPATCH: Release of a queue while items are enqueued
BUG IN LIBDISPATCH: Root queue initialization failed
add
 & ipc kvoucher
com.apple.libdispatch-io.dev_lockq
BUG IN CLIENT OF LIBDISPATCH: Use-after-free of dispatch_semaphore_t or dispatch_group_t
BUG IN LIBDISPATCH: Broken priority
LIBDISPATCH_CONTINUATION_ALLOCATOR
DEPRECATED USE in libdispatch client: %s; set a breakpoint on _dispatch_bug_deprecated to debug
com.apple.libdispatch.workloop_fallback
 (pending)
EVFILT_VNODE
%s[%p] = { 
Changing the target of a source after it has been activated
bits <l %u, r %u
BUG IN CLIENT OF LIBDISPATCH: Messsage should be non-NULL
BUG IN LIBDISPATCH: Allocation should always fail
mach_recv
Voucher: 0x%x Failed to get contents %s\n
com.apple.libdispatch-io.closeq
Changing target queue hierarchy after xpc connection was activated
BUG IN CLIENT OF LIBDISPATCH: voucher_activity_initialize_4libtrace called twice
BUG IN CLIENT OF LIBDISPATCH: Transition to multithreaded is prohibited
BUG IN CLIENT OF LIBDISPATCH: unsupported vah_version
]
  %s\n
io
apply
dispatch_mig_server: mach_msg() failed
com.apple.libdispatch-io.channelq
BUG IN CLIENT OF LIBDISPATCH: Changing target queue hierarchy after xpc connection was activated
timer
BUG IN CLIENT OF LIBDISPATCH: Unexpected dispatch object type
BUG IN CLIENT of %s: Invalid workgroup port 0x%x
Changing target queue hierarchy with a dispatch_sync in flight
com.apple.root.workloop-custom.overcommit
YES
BUG IN CLIENT OF LIBDISPATCH: Trying to handoff IPC from non IPC context
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_hooks_install_4libxpc called twice
BUG IN LIBDISPATCH: vmdeallocate destructor called
target = %s[%p], receive = 0x%x, send = 0x%x, send-possible = 0x%x%s, checkin = 0x%x%s, send state = %016llx, disconnected = %d, canceled = %d 
stderr
BUG IN CLIENT of %s: Mismatched workload ID and attribute interval type: %s vs %hd
>, 
nw_channel
BUG IN LIBDISPATCH: unexpected receipt of port-destroyed
BUG IN LIBDISPATCH: do_dispose called
BUG IN LIBDISPATCH: Release while enqueued
BUG IN CLIENT OF LIBDISPATCH: Cannot target the cooperative root queue - not implemented
BUG IN CLIENT OF LIBDISPATCH: Group object deallocated while in use
EVFILT_USER
_dispatch_kevent_mach_msg_drain: message reception failed
com.apple.debug-channel
com.apple.libsystem.libdispatch
 (armed)
BUG IN LIBDISPATCH: EVFILT_MACHPORT with no message size
\n
v16@?0^{dispatch_fd_entry_s=i^{dispatch_io_path_data_s}iiiI{dispatch_stat_s=iS}[2^{dispatch_stream_s}]^{dispatch_disk_s}^{dispatch_queue_s}^{dispatch_queue_s}^{dispatch_group_s}^{dispatch_io_s}{?=^{dispatch_operation_s}^^{dispatch_operation
port = 0x%x, 
BUG IN CLIENT OF LIBDISPATCH: A block object may not be both run more than once and observed
, enqueued
DISPATCH_EVFILT_CUSTOM_OR
BUG in libdispatch: %s - %lu - 0x%llx
BUG IN CLIENT OF LIBDISPATCH: Release of an inactive object
BUG IN LIBDISPATCH: Premature thread exit while a dispatch queue is running
BUG IN CLIENT OF LIBDISPATCH: trying to install hooks with unsupported version
LIBDISPATCH_LOG
BUG IN CLIENT of %s: Non-default workload type: %s (%hd)
exclaves_notification
BUG IN CLIENT OF LIBDISPATCH: Could not create task mach voucher
com.apple.root.utility-qos.cooperative
com.apple.root.user-initiated-qos.overcommit
BUG in libdispatch client: %s, monitored resource vanished before the source cancel handler was invoked { %p[%s], ident: %d / 0x%x, handler: %p }
BUG IN LIBDISPATCH: dq_activate called
BUG IN CLIENT OF LIBDISPATCH: Called peek after drain
BUG IN CLIENT OF LIBDISPATCH: Changing target queue hierarchy after source was activated
BUG IN LIBDISPATCH: Invalid wlh
com.apple.root.workloop-custom
The arena associated with workgroup is not to be partitioned
BUG IN LIBDISPATCH: Corrupt unote action
   
MallocStackLogging
BUG in libdispatch client: %s %s: \"%s\" - 0x%x { 0x%llx[%s], ident: %lld / 0x%llx, handler: %p }
BUG IN CLIENT OF LIBDISPATCH: Cannot specify an overcommit attribute and use this kind of target queue
BUG IN LIBDISPATCH: Lingering DISPATCH_WLH_ANON
timer (fixed-clock)
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_deprecated
BUG IN LIBDISPATCH: Unable to limit cooperative pool size
BUG IN CLIENT OF LIBDISPATCH: Invalid send flags
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_wait()
BUG IN CLIENT OF LIBDISPATCH: Cannot change the target of this object after it has been activated
BUG IN CLIENT OF LIBDISPATCH: Release of a channel that has not been cancelled, but has a cancel acknowledgement callback
BUG IN CLIENT OF LIBDISPATCH: dispatch_workloop os_workgroup_join failed
, draining on 0x%x
BUG IN LIBDISPATCH: QoS Maintenance support required
com.apple.backboardd.displaythread
local 0x%x
BUG IN LIBDISPATCH: Unexpected event
BUG IN CLIENT OF LIBDISPATCH: Dispatch source used after last release
timer (after)
BUG IN LIBDISPATCH: Cannot turn a manager thread into a normal one
BUG IN CLIENT OF LIBDISPATCH: Over-resume of an inactive object
BUG in libdispatch client: _dispatch_kevent_mach_msg_drain: dropped message too large to fit in memory: id = 0x%x, size = %u
BUG IN CLIENT OF LIBDISPATCH: Start value is not DISPATCH_TIME_NOW or DISPATCH_TIME_FOREVER
BUG IN CLIENT OF LIBDISPATCH: Message size too large
BUG IN CLIENT OF LIBDISPATCH: Log is too large
B40@?0^{dispatch_data_s=^v^{dispatch_queue_s}^v^?^v@?QQ[0{range_record_s=^{dispatch_data_s}QQ}]}8Q16r^v24Q32
BUG IN LIBDISPATCH: Deferred continuation on source, mach channel or mgr
BUG IN CLIENT OF LIBDISPATCH: Invalid threads_per_entity value for CPU entity
signal
API MISUSE: Voucher over-release
BUG IN LIBDISPATCH: mach semaphore API failure
BUG IN CLIENT OF LIBDISPATCH: Release of a locked workloop
mach_mig_demux
, base voucher %p
v12@?0i8
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_kevent_vanished
BUG IN LIBDISPATCH: Invalid wlh state
timer = { target = 0x%llx, deadline = 0x%llx, interval = 0x%llx, flags = 0x%x }, 
data-add
BUG IN CLIENT OF LIBDISPATCH: Invalid arguments
(strict)
BUG IN CLIENT OF LIBDISPATCH: A block object may not be both run more than once and waited for
BUG IN LIBDISPATCH: Don't try to wake up or override the manager
BUG IN CLIENT OF LIBDISPATCH: Cannot specify both overcommit and a non-global target queue
com.apple.root.user-interactive-qos.overcommit
BUG IN LIBDISPATCH: do_invoke called
BUG IN CLIENT OF LIBDISPATCH: Passing an invalid leeway
mach_msg
LIBDISPATCH_NO_FAULTS
BUG IN CLIENT OF LIBDISPATCH: Process has too many threads.
BUG IN LIBDISPATCH: Trailer format is invalid
Invalid voucher: 0x%x\n
BUG IN CLIENT OF LIBDISPATCH: Release of a workloop while items are enqueued
BUG IN CLIENT OF LIBDISPATCH: Waiter pushed onto manager
BUG IN CLIENT of %s: Mismatched workload ID and port interval type: %s vs %hd
, o 0x%x
vnode
IMPORTANCE INFO: %s
LIBDISPATCH_STRICT: _dispatch_bug_kevent_vanished
BUG IN CLIENT OF LIBDISPATCH: Corrupt thread event value
<released queue, pending free>
com.apple.root.default-qos.overcommit
com.apple.root.user-interactive-qos
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_cancel()
BUG IN CLIENT OF LIBDISPATCH: Over-resume of an object
BUG IN CLIENT of %s: Invalid attribute pointer
EVFILT_MEMORYSTATUS
BUG IN CLIENT OF LIBDISPATCH: Unable to allocate mach port
BUG IN CLIENT OF LIBDISPATCH: The executable is already multithreaded
BUG IN CLIENT OF LIBDISPATCH: Assertion failed: 
BUG IN CLIENT of %s: Unable to set kernel workload ID: %s (0x%x) -> %d (0x%x)
com.apple.root.default-qos.cooperative
=== log file opened for %s[%u] at %ld.%06u ===\n
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_mig_demux_get_context not called from dispatch_mach_mig_demux context
BUG IN CLIENT OF LIBDISPATCH: Mach port notification collision
com.apple.libdispatch-io.deviceq.%d
BUG IN CLIENT OF LIBDISPATCH: Semaphore object deallocated while in use (current value < original value)
, activated
BUG IN CLIENT: Releasing last reference to workgroup interval while an interval has been started
BUG IN LIBDISPATCH: Unexpected error from kevent
DISPATCH_EVFILT_CUSTOM_ADD
, activity 0x%llx (pid: 0x%16llx, parent 0x%llx)
BUG IN CLIENT OF LIBDISPATCH: Invalid flags passed to dispatch_block_perform()
BUG IN LIBDISPATCH: none destructor called
API MISUSE: Over-release of an object
BUG IN CLIENT OF LIBDISPATCH: Called drain twice in the same invoke
BUG IN CLIENT OF LIBDISPATCH: Invalid pthread root queue observer hooks
BUG IN LIBDISPATCH: Missing Kevent WORKQ support
BUG IN CLIENT OF LIBDISPATCH: Source has a cancel handler
BUG IN CLIENT OF LIBDISPATCH: Waking up an inactive workloop
target = %s[%p], ident = 0x%llx, mask = 0x%x, pending_data = 0x%llx, registered = %d, armed = %d, %s%s%s
memorystatus
vm (deprecated)
EVFILT_FS
BUG IN CLIENT OF LIBDISPATCH: Unable to register with logd
composite, size = %zd, num_records = %zd 
, flatbuf = %p 
BUG IN LIBDISPATCH: unexpected receipt of no-more-senders
syslog
BUG IN CLIENT OF LIBDISPATCH: Cannot change the target of a queue already targeted by other dispatch objects
BUG IN CLIENT OF LIBDISPATCH: Used Swift only SPI to enqueue non-Swift runtime objects into dispatch
sigterm (xpc)
BUG IN CLIENT OF LIBDISPATCH: Unsupported interface
BUG IN CLIENT OF LIBDISPATCH: Unexpected non message event
com.apple.libdispatch-io.streamq
BUG IN CLIENT OF LIBDISPATCH: Channel didn't call dispatch_channel_drain
no ports
BUG IN CLIENT OF LIBDISPATCH: Channel never connected
BUG IN CLIENT OF LIBDISPATCH: Release of a workloop with corrupt state
runloop-queue
BUG IN CLIENT OF LIBDISPATCH: Unknown entity
BUG IN CLIENT OF LIBDISPATCH: Invalid source type
BUG IN CLIENT OF LIBDISPATCH: dispatch_source_cancel_and_wait called from a source handler
BUG IN LIBDISPATCH: Joined count underflowed
BUG IN CLIENT OF LIBDISPATCH: pthread_start os_workgroup_join failed
Recipe Contents
com.apple.root.background-qos.overcommit
EVFILT_PROC
BUG IN LIBDISPATCH: Invalid msg aux data size.
LIBDISPATCH_STRICT: _dispatch_bug_mach_client
BUG IN CLIENT OF LIBDISPATCH: workloop qos class or priority must be set before cpupercent
LIBDISPATCH_COOPERATIVE_POOL_STRICT
 } }
type = %s %s, fd = 0x%lx, fd_entry = %p, channel = %p, queue = %p -> %s[%p], target = %s[%p], offset = %lld, length = %zu, done = %zu, undelivered = %zu, flags = %u, err = 0x%x, low = 0x%zx, high = 0x%zx, interval%s = %llu 
BUG IN CLIENT OF LIBDISPATCH: Queue doesn't support dispatch_queue_set_specific
, max qos %d
remote 0x%x
data-or
%s  %04lx 
API MISUSE: Voucher resurrection
kern.wq_limit_cooperative_threads
Clearing handler after the source has been activated
BUG IN LIBDISPATCH: MACH_RCV_LARGE_IDENTITY with no identity
BUG IN CLIENT OF LIBDISPATCH: Overlarge message received
BUG IN LIBDISPATCH: inline destructor called
BUG IN CLIENT OF LIBDISPATCH: Release of a queue with corrupt state
BUG IN CLIENT OF LIBDISPATCH: Setting interval to 0
BUG IN CLIENT of %s: Mismatched workload ID and workgroup interval type: %s vs %hd
Join token is corrupt
Join token provided is for a different thread
mach reply
com.apple.root.user-initiated-qos.cooperative
%s%s%s
enable
EVFILT_WORKLOOP
DISPATCH_EVFILT_TIMER_WITH_CLOCK
, suspended = %d
BUG IN CLIENT OF LIBDISPATCH: sync waiter found on channel
BUG IN CLIENT OF LIBDISPATCH: Failed to initalize workqueue kevent
BUG IN CLIENT OF LIBDISPATCH: dispatch_main called from a block on the main queue
BUG IN LIBDISPATCH: Premature thread exit while a dispatch frame is active
opts/err = 0x%x, msgh[%p] = { 
EVFILT_READ
BUG IN CLIENT OF LIBDISPATCH: LIBDISPATCH_STRICT: _dispatch_bug_mach_client
BUG IN CLIENT OF LIBDISPATCH: Too many nested calls to dispatch_group_enter()
os_workgroup_create_with_workload_id_and_workgroup
_os_workgroup_join_update_wg
BUG IN CLIENT OF LIBDISPATCH: Filter id should be non-NULL
BUG IN LIBDISPATCH: EVFILT_MACHPORT with overlarge message
closed, 
missing do_debug vtable slot: 
 (direct)
mach_send
BUG IN CLIENT OF LIBDISPATCH: Received message with MACH_PORT_NULL msgh_local_port
BUG IN CLIENT OF LIBDISPATCH: mach_port_construct() failed: cannot create receive right
%s%s:\n
BUG IN CLIENT OF LIBDISPATCH: Invalid queue type
data-replace
DISPATCH_EVFILT_MACH_NOTIFICATION
BUG IN LIBDISPATCH: base voucher has non-zero activity value
, activating
, pending-barrier
local 0x%x, remote 0x%x
BUG IN CLIENT OF LIBDISPATCH: Changing target queue hierarchy after mach channel was connected
RESOURCE ACCOUNTING INFO: %s
, inactive
BUG IN LIBDISPATCH: Pending thread request underflow
com.apple.coremedia
BUG IN CLIENT OF LIBDISPATCH: Channel already connected
BUG IN LIBDISPATCH: Interrupted drain on manager queue
vfs
com.apple.coreaudio.hal.iothread
BUG IN LIBDISPATCH: dispatch_data_copy_region out of bounds
xref = %d, ref = %d, 
BUG IN CLIENT OF LIBDISPATCH: dispatch queue/source property setter called after activation
BUG IN LIBDISPATCH: Premature thread exit with unhandled deferred items
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_send_with_result_and_wait_for_reply is XPC only
stream
com.apple.root.utility-qos.overcommit
BUG IN CLIENT OF LIBDISPATCH: _dispatch_mach_default_async_reply_handler called
BUG IN CLIENT OF LIBDISPATCH: trying to lock recursively
BUG IN LIBDISPATCH: Cannot raise oneself to manager
BUG IN CLIENT OF LIBDISPATCH: Cannot target source to the cooperative root queue - not implemented
BUG IN CLIENT: Thread exiting without leaving workgroup '%s'
BUG in libdispatch: %s: \"%s\" - 0x%x{ 0x%llx[%s], ident: %lld / 0x%llx, handler: %p }
LIBDISPATCH_STRICT: _dispatch_bug_deprecated
file
BUG IN CLIENT OF LIBDISPATCH: Owner in ulock is unknown - possible memory corruption
BUG IN CLIENT OF LIBDISPATCH: Corrupt activation state
os_workgroup_create_with_workload_id_and_port
mach_notification
, dirty
EVFILT_TIMER
Voucher: 0x%x\n
BUG IN LIBDISPATCH: base voucher has nested base voucher
delete
data[%p] = { 
BUG IN CLIENT OF LIBDISPATCH: Voucher port corruption
v8@?0
BUG IN LIBDISPATCH: Locking the manager should not fail
Key: %u, 
BUG IN LIBDISPATCH: dispatch_data_create_subrange out of bounds
com.apple.root.utility-qos
BUG IN CLIENT OF LIBDISPATCH: Cannot set width of a serial queue
BUG IN CLIENT OF LIBDISPATCH: Voucher importance count underflow
 %02x
BUG IN CLIENT OF LIBDISPATCH: lock not owned by current thread
Changing the target of a queue already targeted by other dispatch objects
BUG IN CLIENT OF LIBDISPATCH: Do not close random Unix descriptors
com.apple.root.maintenance-qos
BUG IN CLIENT OF LIBDISPATCH: Corrupt channel state
com.apple.root.user-initiated-qos
MIG_REPLY_MISMATCH
BUG IN CLIENT OF LIBDISPATCH: _dispatch_main_queue_callback_4CF called from the wrong thread
BUG IN LIBDISPATCH: Waking up a kq with cooperative thread request is not supported
BUG IN CLIENT OF LIBDISPATCH: Could not get unprivileged host port
 }
BUG IN CLIENT OF LIBDISPATCH: A block object may not be waited for more than once
BUG IN CLIENT OF LIBDISPATCH: Not a runloop queue
BUG IN CLIENT OF LIBDISPATCH: Reply port needed for async send with reply
monitor
BUG IN CLIENT OF LIBDISPATCH: Unable to make memory port
BUG IN CLIENT OF LIBDISPATCH: NULL was passed where a block should have been
BUG IN CLIENT OF LIBDISPATCH: Invalid workloop owner, possible memory corruption
BUG IN LIBDISPATCH: firehose_mig_server doesn't handle replies
BUG IN CLIENT OF LIBDISPATCH: Unable to allocate reply port, possible port leak
BUG IN LIBDISPATCH: Unexpected error from mach_msg_receive
TRUE
}
API MISUSE: Resurrection of an object
BUG IN CLIENT OF LIBDISPATCH: invalid queue passed to dispatch_am_i_on_queue_4swiftonly()
Creating an os_workgroup of unknown type
kevent
        
BUG IN LIBDISPATCH: Unable to get the unique pid (size)
stopped, 
BUG IN CLIENT OF LIBDISPATCH: dispatch_set_qos_class_floor called on invalid object type
EVFILT_SIGNAL
, ipc kvoucher 0x%x [\n
BUG IN LIBDISPATCH: _pthread_set_properties_self failed
BUG IN LIBDISPATCH: Unexpected object type
BUG IN CLIENT OF LIBDISPATCH: Overlarge message
BUG IN CLIENT OF LIBDISPATCH: Reply received on unexpected port
BUG IN LIBDISPATCH: ulock_wait() failed
BUG IN CLIENT OF LIBDISPATCH: Release of a suspended object
source
BUG IN CLIENT OF LIBDISPATCH: Cannot change a handler of this source after it has been activated
BUG IN LIBDISPATCH: free destructor called
BUG IN CLIENT OF LIBDISPATCH: dispatch_sync called on queue already owned by current thread
leaf, size = %zd, buf = %p 
NULL: 
BUG IN CLIENT OF LIBDISPATCH: invalid queue passed to dispatch_assert_queue()
sref = %d, target = %s[%p], width = 0x%x, state = 0x%016llx
id 0x%x, 
BUG IN LIBDISPATCH: ulock_wake() failed
BUG IN CLIENT OF LIBDISPATCH: Premature release of a locked queue
BUG IN CLIENT OF LIBDISPATCH: Unexpected EV_VANISHED (do not destroy random mach ports or file descriptors)
timer (interval)
mach_send (mach)
com.apple.libdispatch-manager
BUG in libdispatch client: %s %s{ 0x%llx[%s], ident: %lld / 0x%llx, handler: %p }
BUG IN CLIENT OF LIBDISPATCH: -init called directly
kevent = %p%s, filter = %s }
proc
v20@?0^{dispatch_data_s=^v^{dispatch_queue_s}^v^?^v@?QQ[0{range_record_s=^{dispatch_data_s}QQ}]}8i16
count = %u, gen = %d, waiters = %d, notifs = %d }
Changing target queue hierarchy after source was activated
BUG IN CLIENT of %s: Invalid workload interval type: %s (%hd)
_os_workgroup_set_work_interval_workload_id
BUG IN LIBDISPATCH: EVFILT_MACHPORT with no message
com.apple.libdispatch-io.opq
Thread is not a member of the workgroup
BUG IN CLIENT OF LIBDISPATCH: Workload identifier must not be NULL
EVFILT_AIO
BUG in libdispatch client: %s %s - 0x%x
BUG IN CLIENT OF LIBDISPATCH: Corruption of dispatch block object
value = %ld, orig = %ld }
BUG IN LIBDISPATCH: apply continuation has invalid flags
BUG IN CLIENT OF LIBDISPATCH: Voucher corruption
Command: %u, 
BUG IN LIBDISPATCH: Corrupt thread event value
%sBlock was %sexpected to execute on queue [%s (%p)]
BUG IN LIBDISPATCH: Unregistration failed
BUG IN CLIENT OF LIBDISPATCH: Unbalanced call to dispatch_group_leave()
, in-flight = %d
needs-event, 
%sBlock was expected to act as a barrier on queue [%s (%p)]
BUG IN LIBDISPATCH: Underflow of tbkqwl count
BUG IN LIBDISPATCH: Premature thread exit while a dispatch context is set
BUG IN CLIENT OF LIBDISPATCH: _dispatch_source_will_reenable_kevent_4NW not called from within the event handler
BUG IN CLIENT OF LIBDISPATCH: Attempting to modify timer clock
BUG IN DISPATCH: Invalid wi flags = %u
BUG IN CLIENT OF LIBDISPATCH: Calling dispatch_mach_handoff_reply multiple times from the same context
API MISUSE: Resurrection of an over-released object
BUG IN CLIENT OF LIBDISPATCH: Cannot change label for this queue
mach_recv (channel)
BUG IN LIBDISPATCH: Too many deferred free items
BUG IN CLIENT OF LIBDISPATCH: Invalid size for the firehose buffer
BUG IN CLIENT OF LIBDISPATCH: Memory corruption in the logging buffers
com.apple.root.background-qos.cooperative
BUG IN CLIENT OF LIBDISPATCH: dispatch_main() must be called on the main thread
com.apple.coreaudio.hal.clientthread
size %u, 
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
BUG IN CLIENT OF LIBDISPATCH: Invalid block object passed to dispatch_block_testcancel()
BUG IN CLIENT OF LIBDISPATCH: Corrupted priority
BUG IN CLIENT of %s: Invalid mach port 0x%x
BUG IN CLIENT OF LIBDISPATCH: Could not generate an activity ID
BUG IN CLIENT OF LIBDISPATCH: _dispatch_main_queue_callback_4CF called after dispatch_main()
com.apple.root.background-qos
BUG IN CLIENT OF LIBDISPATCH: Invalid threads_per_cluster value, only acceptable value is 1
com.apple.root.maintenance-qos.cooperative
DISPATCH_DEBUG_MISSING_POOLS
deleted, 
LIBDISPATCH_STRICT
%s
BUG IN CLIENT OF LIBDISPATCH: Cannot target object to cooperative root queue - not implemented
BUG IN CLIENT of %s: Workgroup already cancelled
BUG IN CLIENT OF LIBDISPATCH: Empty message
BUG IN CLIENT OF LIBDISPATCH: Attempt to set timer on a non-timer source
BUG IN CLIENT OF LIBDISPATCH: dispatch_mach_mig_demux: mach_msg(MACH_SEND_MSG) failed
BUG IN LIBDISPATCH: Disposing of timer still in its heap
BUG IN CLIENT OF LIBDISPATCH: Unable to copyout msg, possible port leak
Previous voucher: 0x%x, 
random
BUG IN CLIENT OF LIBDISPATCH: Bound thread attribute set multiple times
BUG IN CLIENT of %s: Non-default attribute flags: 0x%x
sock
BUG IN LIBDISPATCH: Unexpected error from mach recv
BUG IN LIBDISPATCH: Invalid values for MADVISE_CHUNK_COUNT / CHUNK_SIZE
type = %s, fd = 0x%lx, %sfd_entry = %p, queue = %p, target = %s[%p], barrier_queue = %p, barrier_group = %p, err = 0x%x, low = 0x%zx, high = 0x%zx, interval%s = %llu 
BUG IN CLIENT OF LIBDISPATCH: Invalid queue attribute
Y
API MISUSE: Object type does not support suspension
BUG IN LIBDISPATCH: Invalid way to wake up a workloop
BUG IN CLIENT OF LIBDISPATCH: Invalid reply port
com.apple.libdispatch-io.barrierq
/var/tmp/libdispatch.%d.log
BUG IN CLIENT OF LIBDISPATCH: Message already enqueued
voucher[%p] = { xref = %d, ref = %d
BUG IN CLIENT OF LIBDISPATCH: invalid queue passed to dispatch_assert_queue_not()
DISPATCH_EVFILT_TIMER
com.apple.root.default-qos
BUG IN LIBDISPATCH: Invalid workload ID type
BUG IN CLIENT OF LIBDISPATCH: attribute's properties are invalid or meaningless on this system
os_workgroup_interval_create_with_workload_id
Join token provided is for a different workgroup than the last one joined by thread
read
LIBDISPATCH_TIMERS_FORCE_MAX_LEEWAY
BUG IN LIBDISPATCH: Unexpected __ulock_wait error
BUG IN CLIENT OF LIBDISPATCH: 0 is an invalid threads_per_cluster value
BUG IN LIBDISPATCH: Unsupported wlh configuration
BUG IN LIBDISPATCH: firehose_push_reply should never be sent to the buffer receive port
cancelled, 
BUG IN CLIENT OF LIBDISPATCH: Absurd publen
BUG IN CLIENT OF LIBDISPATCH: Could not allocate heap
OS_dispatch_source_proc
OS_dispatch_source_mach_recv
OS_dispatch_source_data_replace
OS_dispatch_group
OS_os_workgroup
OS_object
OS_dispatch_source
OS_dispatch_mach
OS_dispatch_queue_concurrent
OS_dispatch_queue
NSObject
OS_dispatch_source_data_or
OS_dispatch_queue_serial
OS_dispatch_queue_main
OS_dispatch_queue_mgr
OS_dispatch_mach_msg
OS_os_workgroup_interval
OS_dispatch_channel
OS_dispatch_source_exclaves_notification
OS_dispatch_source_nw_channel
OS_dispatch_queue_serial_executor
OS_dispatch_queue_pthread_root
OS_os_eventlink
OS_dispatch_source_vm
OS_dispatch_source_interval
OS_dispatch_source_vnode
OS_dispatch_source_data_add
OS_dispatch_operation
OS_dispatch_object
OS_dispatch_source_sock
OS_dispatch_source_write
OS_dispatch_queue_runloop
OS_dispatch_queue_global
OS_dispatch_queue_cooperative
OS_dispatch_io
OS_dispatch_data
OS_dispatch_source_memorystatus
OS_dispatch_semaphore
OS_dispatch_disk
OS_os_workgroup_parallel
OS_dispatch_data_empty
OS_dispatch_source_timer
OS_dispatch_source_signal
OS_dispatch_source_read
OS_dispatch_source_memorypressure
OS_dispatch_source_mach_send
OS_dispatch_workloop
OS_dispatch_queue_attr
OS_voucher
OS_dispatch_source_vfs
TQ,R
release
_setContext:
bytes
conformsToProtocol:
hash
initWithBytes:length:copy:freeWhenDone:bytesAreVM:
isKindOfClass:
T@\"NSString\",?,R,C
dealloc
isEqual:
isMemberOfClass:
respondsToSelector:
zone
_getContext
_setFinalizer:
allowsWeakReference
debugDescription
description
getBytes:maxLength:usedLength:encoding:options:range:remainingRange:
length
performSelector:withObject:withObject:
T@\"NSString\",R,C
_activate
_setTargetQueue:
class
retain
self
stringWithFormat:
stringWithUTF8String:
_resume
isProxy
_bytesAreVM
autorelease
init
performSelector:
retainCount
superclass
T#,R
Tr^v,R,N
_isCompact
_suspend
_xref_dispose
allocWithZone:
TQ,R,N
performSelector:withObject:
retainWeakReference
Vv16@0:8
Q16@0:8
B16@0:8
@32@0:8:16@24
@24@0:8^{_NSZone=}16
^v16@0:8
r^v16@0:8
@16@0:8
v16@0:8
#16@0:8
B24@0:8@\"Protocol\"16
B24@0:8@16
B24@0:8#16
B24@0:8:16
@\"NSString\"16@0:8
v24@0:8^v16
v24@0:8@16
@24@0:8:16
@40@0:8:16@24@32
^{_NSZone=}16@0:8
@44@0:8^v16Q24B32B36B40
v24@0:8^?16
```
