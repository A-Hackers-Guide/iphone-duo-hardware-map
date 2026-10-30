# `/System/DriverKit/System/Library/PrivateFrameworks/AirshipDK.framework/AirshipDK`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,063,248 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 2136)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (4)

- `/System/DriverKit/System/Library/PrivateFrameworks/AirshipDK.framework/AirshipDK (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/System/Library/Frameworks/PCIDriverKit.framework/PCIDriverKit (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/usr/lib/libc++.dylib (compatibility version 1.0.0, current version 2200.32.0)`

## Entitlements

```xml
  - no entitlements
```

## Strings (2,073)

```
instance resolution failure
[%s:%d:%s] new ipc stage: %s
loadIpcConfig
synthesize_reset_completions
[%s:%d:%s] (trid %hu) failed to validate client override
[%s:%d:%s] (trid %hu) open failed 0x%x
[%s:%d:%s] change to exec stage %s (%u) from %s
invalid completion style
IOService
set_device_context_status
BUG in Airship: wrong index
reap
[%s:%d:%s] (trid %hu) invalid ti: %hu
ok
completed_transfer_log_depth
[%s:%d:%s] creating new ring pool for transfer ring %s
BUG in Airship: attempted to initialize optional with sentinel value
[%s:%d:%s] msi stats overflow: resetting count for vector %u
timedwait
[%s:%d:%s] activate
mem_read32
IOPCIDeviceMemoryMapSize
set_image_sent
disable_interrupt_vector
[%s:%d:%s] failed to aquire resource for %s
finishExitResetIfNeeded
[%s:%d:%s] starting power off deadline timer
flush_queued_transfers
set_external_execution_queue
BUG in client of Airship: attempted to unregister handler for terminated driver
airship_acipc_tr_disconnect
virtual
[%s:%d:%s] (trid %hu) predecessor state %u does not valid
[%s:%d:%s] adding interrupt source %u
[%s:%d:%s] property '%s' is not numeric
[%s:%d:%s] DART page size 0x%llx, memory map: base 0x%llx, size 0x%llx)
~state_dump_manager
save_overflow_message
count_where
bind_active_object
create_handle
[%s:%d:%s] (crid %hu) new availability blockers 0x%08x
[%s:%d:%s] (crid %hu) controller opened
[%s:%d:%s] payload length %u, appendix length %u
[%s:%d:%s] sending overflow messages
appendDeviceStateDump
update_sleep_control_register
vector
id
operator=
[%s:%d:%s] (trid %hu) invalid in-place completion at idx=%hu
[%s:%d:%s] updated error state: %u, current %u
BUG in Airship: attempted to reconfigure active object @%s:%u
[%s:%d:%s] registering service
[%s:%d:%s] Enable BusLead and Memory
[%s:%d:%s] boot manager is already in reset
get_completed_transfer_count
set_interrupt
[%s:%d:%s] (bc %s) adding controller to boot manager
stop_context
[%s:%d:%s] setting crid %hu closed
[%s:%d:%s] crid %hu open message result %u
[%s:%d:%s] creating boot controller for %s
[%s:%d:%s] power state not ready, setting transport blocker
set_maintenance_completion_notifier
BUG in client of Airship: attempt to reconfigure active CR
unknown-error
BuiltIn
[%s:%d:%s] recomputing closed ring availability
[%s:%d:%s] trid %hu has unmessaged lifecycle, closing
set_completion_footer_size
BUG in Airship: out of bounds access to boxed array @%s:%u
did_set_transport
read_ipc_status_register
direct_monitor.cpp
context_info_address_lo
write
getGlobalQueue
BUG in client of Airship: mode must be AIRSHIP_ACIPC_TR_MODE_STANDARD @%s:%u
doorbells
read_cr_head_index
tr_ring.cpp
[%s:%d:%s] set transport result 0x%x
[%s:%d:%s] capture AirshipDeviceDK state
[%s:%d:%s] (trid %hu) offset %hu exceeds fetched transfer count %hu
BUG in Airship: access to null buffer mapping
copy_from
unmap
direct_client_object
BUG in client of Airship: attempted to activate active driver
register_client_statedump_handler
device_transport.hpp
handle_is_interrupt_source_connected
[%s:%d:%s] adding crid %hu flush tracking for trid %hu
BUG in Airship: Ring is disconnected or in limbo.
deregister_cr_index_vector_action
BUG in Airship: size is too big @%s:%u
[%s:%d:%s] performing health check.
[%s:%d:%s] (trid %hu) completing transfer tag %hu
get_first_free_tag
I/O error
maintenance_complete
[%s:%d:%s] setting up peripheral info interrupt
synchronized
[%s:%d:%s] running power state change wait context
handle_append_state_dump
~messenger
dynamic_array.hpp
[%s:%d:%s] updating cr close requests
platform_private.cpp
BUG in Airship: unrecognized detail bits in context controller.
clear_cr_indices
TargetName
[%s:%d:%s] initializing driver
com.apple.airship.debug-%s
handle_mem_read8
context_close_message_completed
parse
window_size
[%s:%d:%s] Registering tail index update handler for trid %hu at vector %hu
map
BUG in Airship: invalid tail index update operation
set_backing_memory
BUG in client of Airship: nonzero offset/length for NULL resource @%s:%u
BUG in Airship: index out of range
BUG in client of Airship: attempted to reconfigure active driver @%s:%u
intrusive_list.hpp
selector
doorbell value not configured in shared constant mode
completion_group_stride
append
create_exec_stage_monitor
clear_context
[%s:%d:%s] stopping context id %hu for reason %u
BUG in client of Airship: attempted to activate canceled interrupt
Airship IPC power on timed out @%s:%u
com.apple.AirshipDriverDK.per-device.%s
[%s:%d:%s] (trid %hu) controller closed
[%s:%d:%s] driver create client end %s
BUG in client of Airship: attempted to activate already-active memregion @%s:%u
airship_platform_get_conttime_offset
AirshipDeviceAttachTimeoutMS
connect_interrupt
direct_cr_controller.cpp
read_register
BUG in Airship: bad optional access
does_region_conflict_with_any_mapped_region
role
BUG in client of Airship: attempted to access inactive CR @%s:%u
open_context
BUG in Airship: bad array access @%s:%u
[%s:%d:%s] activating doorbell coordinator with %u doorbell instances
BUG in Airship: attempted to create boxed symbol from null string @%s:%u
copy_to
setup_boot_ipc_stage
[%s:%d:%s] adding %u instances of resource %s
create_cr_controller
save_transfer_completion
[%s:%d:%s] (crid %hu) inserting completion with trid %hu and first tag %hu
[%s:%d:%s] ipc handshake complete
register overlap
clear_tr_indices
BUG in client of Airship: Failed to locate completion ring config @%s:%u
cldma-tx-error
[%s:%d:%s] device is not active
OSAction_AirshipDriverDK_ServiceNotificationReady
BUG in Airship: invalid head index advance operation @%s:%u
unmap_region
no-error
channel-sync-failure
configurator.cpp
ignore_zeroed_cd
BUG in client of Airship: out of bounds access to buffer @%s:%u
acquire
create_free_space_monitor
append_outstanding_transfer_state
~interrupt
handle_mem_write64
[%s:%d:%s] provider 0x%llx\n
cr_ring.cpp
traffic_wake
[%s:%d:%s] region id %hu conflict %u
[%s:%d:%s] creating context controller for %s[%u]
Role
airship-ipc-error(%s)
isPoweredOnWithAssertion
BUG in Airship: attempted to create boxed symbol from null C string @%s:%u
existing_for_str
Airship ACIPC protocol error
memory_map_message_completed
[%s:%d:%s] (trid %hu) failed to complete transfer tag %hu
append_state_dump
[%s:%d:%s] trid %hu in limbo
[%s:%d:%s] reset type: %s
airship-trap-on-device-power-on-timeout
CentauriHelperBootUserClient
get_maintenance_in_progress
bounds overflow
image_address_hi
unknown ipc stage
ring_controller.cpp
BUG in Airship: attempted to retrieve max message length in reset
[%s:%d:%s] tearing down mcr
[%s:%d:%s] setting up message buffer for main ipc stage %s
[%s:%d:%s] new ipc status=%u
airship_platform_get_conttime_offset_block_invoke
setup_interrupt
[%s:%d:%s] copying peripheral info, initial exec stage value=%u
read
acipc_get_health_status
BUG in client of Airship: attempted to register handler for inactive driver @%s:%u
[%s:%d:%s] (crid %hu) controller closed
add_context
BUG in client of Airship: attempted to activate canceled monitor
disconnect_interrupt
BUG in Airship: attempted to use inactive object @%s:%u
[%s:%d:%s] closing trid %hu
[%s:%d:%s] trid %hu status %u
[%s:%d:%s] sending close message for crid %hu
[%s:%d:%s] IPC handshake timer expired
cr_index_count
[%s:%d:%s] clearing in reset transport blocker
[%s:%d:%s] (trid %hu) predecessor completion ID %hu does not equal completion ID %hu
[%s:%d:%s] saving overflow message
SetPowerState_Impl
BUG in client of Airship: attempted to activate already-active context @%s:%u
[%s:%d:%s] requesting close for trid %hu
external
[%s:%d:%s] controller ipc stage: %s
context_controller
[%s:%d:%s] Airship error description: %s
[%s:%d:%s] (trid %hu) tag %hu must belong to first in chain
timer.cpp
BUG in client of Airship: invalid queue role @%s:%u
[%s:%d:%s] not ready to probe exec stage register
BUG in client of Airship: attempted to set interrupt execution queue for inactive driver @%s:%u
[%s:%d:%s] closing mcr
[%s:%d:%s] updating context close requests
[%s:%d:%s] trid %hu close message requested
[%s:%d:%s] setting up message rings
tr_controller
[%s:%d:%s] stopping provider
get_state
resources
BUG in Airship: attempted access to terminated client
BUG in Airship: attempted to create tr_controller in direct_client
acipc_driver_client.cpp
[%s:%d:%s] (trid %hu) transfer at index %hu is in state %u
handle_is_memory_mapping_active
[%s:%d:%s] index %hu
buffer
BUG in Airship: out of bounds access to boxed array
refresh_mapping
com.apple.airship.global-timer-queue
change_to_exec_stage
priority
compute_state_detail
get_and_advance_inorder_idx_for_completion
[%s:%d:%s] copying appendix
scribble_descriptor
BUG in client of Airship: attempt to reconfigure active TR @%s:%u
exec_stages
count_intersection
[%s:%d:%s] synthesizing completions if needed
[%s:%d:%s] added %u instances of doorbell %s
errata
[%s:%d:%s] (ctxid %hu) controller state=%u, detail=%u
BUG in client of Airship: selector is not available
[%s:%d:%s] (bc %s) image address 0x%llx, length 0x%x
[%s:%d:%s] copying message payload
(nil)
sleep_state_machine
limits
[%s:%d:%s] (ctxid %hu) sending close message
interrupt_manager
[%s:%d:%s] message canceled
close
stop_cr
add_controller
set_notifier
update_exec_stage
[%s:%d:%s] (crid %hu) close complete
[%s:%d:%s] trid %hu close message result %u
BUG in Airship: refcount_mixin retain overflow @%s:%u
Airship IPC power off timed out
setup_tr_settlement_tracking
BUG in Airship: bad parameter - 'memory'
BUG in Airship: attempted to create tr_controller in direct_client @%s:%u
[%s:%d:%s] message failure
<nil>
BUG in client of Airship: attempted to activate active monitor @%s:%u
memregion_controller
BUG in client of Airship: Failed to locate transfer ring config
BUG in Airship: access to null buffer
[%s:%d:%s] (bc %s) checking for image response
ring_index_pair.hpp
recompute_state
BUG in client of Airship: attempted to activate already-active TR
None
completion_group
0x%08x:
airship-debug
AirshipDeviceDK_IVars
BUG in client of Airship: attempted to retrieve first free tag of ring without free space @%s:%u
airship_platform_get_sleep_queue_block_invoke
BUG in client of Airship: attempted to activate active monitor
context_controller_block_invoke
arm_tr_index_vector
~tr_controller
BUG in client of Airship: attempted to unregister handler for inactive driver @%s:%u
handle_get_mmio_size
AirshipPCIDeviceDK.cpp
[%s:%d:%s] deleted %hu items from mirror
direct_interrupt.cpp
BUG in Airship: attempted to create cr_controller in driver_client @%s:%u
[%s:%d:%s] no handles available in pool
true
start
[%s:%d:%s] messenger already out of reset
BUG in client of Airship: attempted to reconfigure active TR
[%s:%d:%s] trid: %u, state %u
com.apple.airship.global-fallback
interrupt_stride
BUG in client of Airship: selector is invalid @%s:%u
flush_with_action
BUG in Airship: attempted to access terminated driver @%s:%u
write_register
BUG in client of Airship: attempted to retrieve first completed tag of ring without completed transfers @%s:%u
[%s:%d:%s] boot ipc stage name %s
response code is ambiguous
remove_controller
remove_region
CentauriHelperTimesyncUserClient
BUG in client of Airship: attempt to reconfigure active CR @%s:%u
trigger
[%s:%d:%s] window_base=%#llx, size=%#llx
~direct_client
Start_Impl_block_invoke_5
[%s:%d:%s] getting driver name
[%s:%d:%s] loading device configuration
[%s:%d:%s] detaching from device
BUG in Airship: unexpected flush notice @%s:%u
[%s:%d:%s] updated exec stage: %u, current %u
BUG in client of Airship: attempted to retrieve first completed tag of ring without completed transfers
handle_activate
get_source_maintenance_in_progress
[%s:%d:%s] canceling power off deadline timer
[%s:%d:%s] driver ioservice params: ipcPowerOn %u ms, ipcPowerOff %u ms, devicePowerOn %u ms, devicePowerOff %u ms
trigger_async
BUG in client of Airship: attempted to register handler for terminated driver
[%s:%d:%s] completion count %hu
airship_platform_get_fallback_queue_block_invoke
ring_header_footer_scaling
Airship device power on timed out
BUG in Airship: invalid src @%s:%u
addDriver
[%s:%d:%s] crid %hu has unmessaged lifecycle, setting open
[%s:%d:%s] crid %hu has unmessaged lifecycle, closing
[%s:%d:%s] notifying crid %hu that trid %hu is settled
BUG in client of Airship: attempted to retrieve first free tag of ring without free space
ipc_stage
recomputePowerRequest_block_invoke
BUG in client of Airship: attempted to access inactive context
OSAction_AirshipOSActionProxy_TimerOccurred
BUG in client of Airship: Invalid mode: AIRSHIP_ACIPC_TR_MODE_STANDARD (method not accessible) @%s:%u
BUG in Airship: attempted to create boxed string from null C string @%s:%u
ipc stage
airship-unknown-errors
initDriverIOServiceParams_block_invoke
[%s:%d:%s] clearing transport
[%s:%d:%s] creating new ring pool for completion ring %s
unknown result code
completion_mirror
interrupt.cpp
BUG in Airship: attempted to activate object without required configuration
cr_controller
validate_client_overrides
add_cr
get_debug_object_alloc_size
reaper.cpp
invalid value
[%s:%d:%s] device service does not match criteria
[%s:%d:%s] setting external interrupt handler for vector %u
doorbell_stride
fixup_remain_count
acipc
size
proxima-platform
buffer_create
[%s:%d:%s] airship driver service is not active
ensure_free_space
BUG in Airship: attempted to insert element already in list
[%s:%d:%s] suspending doorbell coordinator
unknown
restricted
completion_footer_size
[%s:%d:%s] setting client overrides for %s[%u]
[%s:%d:%s] attaching pending device to driver
channel-quiesce-failure
[%s:%d:%s] deferring message send
resume
retain_obj
com.apple.iokit.pm.wakedescription.continuous-time-offset
[%s:%d:%s] no exec stage found for value %u
AirshipDriverDK
queues
%s.plist
[%s:%d:%s] (trid %hu) transfer tag %hu does not match next in-order tag %hu
~driver_object_manager
retain
populate_descriptor
[%s:%d:%s] pending IPC error broadcast
sync_action_process_ti_update
add_handler
set_ipc_stage
[%s:%d:%s] context id %hu has unmessaged lifecycle, setting open
append_bytes
reap_single_DROPS_LOCK
ambiguous value
nominal_state_dump_size
acipc_create_context_controller
[%s:%d:%s] creating doorbell controller for %s[%u]
handle_mem_read32
tr_open_message_completed
[%s:%d:%s] entering reset, dropping any pending doorbells
[%s:%d:%s] failed to allocate/map device memory
chain
swizzleConfigName
[%s:%d:%s] getting device class
BUG in Airship: unaligned device memory access @%s:%u
cldma-rx-error
[%s:%d:%s] exiting host sleep
acquire_resource
copy_descriptor
stop_tr
activate_block_invoke
BUG in Airship: bad parameter - 'memory' @%s:%u
airship-multiple-errors(0x%08x,0x%08x)
v12@?0I8
operator[]
exitReset
set_exec_stage_change_handler
[%s:%d:%s] trid %hu open message result %u
interrupt_moderation
[%s:%d:%s] boot manager entering reset
AirshipDriverName
handle_mem_read64
acipc_driver.cpp
AirshipAutoExitReset
ring_pool
handle_get_mmio_physical_address
[%s:%d:%s] no custom statedump handlers registered
validate_buffer_bounds
with_capacity
boot
BUG in client of Airship: attempted to await inactive monitor
unknown keys present
[%s:%d:%s] IPC power state callout enabled
[%s:%d:%s] releasing ring with selector %u
write_tail_index
BUG in Airship: airship_acipc_tr_disconnect: not implemented
[%s:%d:%s] running power state changed wait context
[%s:%d:%s] (bc %s) no image response code
truncate
[%s:%d:%s] unknown device viddid=%#x
completion_rings
[%s:%d:%s] result=0x%x
update_interrupt_debug_state
typed_allocators.hpp
[%s:%d:%s] ring manager is in reset
group
append_tr_index_info
BUG in Airship: attempted access to terminated client @%s:%u
create_tr_controller
getExecStage
device error
BUG in Airship: attempted to reconfigure active object
device_memory.cpp
BUG in client of Airship: attempted to activate interrupt with event handlers but without queue
BUG in Airship: bad parameter - 'size'
[%s:%d:%s] debugInfo capture start
multicomp_find_first_transfer
[%s:%d:%s] IPC driver state_dump complete
[%s:%d:%s] invoking action
set_transfer_footer_size
getGlobalQueue_block_invoke
destroy_handle
driverkit_maintenance_block_invoke
device-sleep-exit-timeout
ALLOCATION FAILURE (or BUG) in Airship @%s:%u
BUG in Airship: bad parameter - 'footer_length'
get_inplace_completion
wait
[%s:%d:%s] setting up mcr
~memregion_manager
map_region
write_tr_head_index
[%s:%d:%s] %s[%u] old status %u, new status %u
[%s:%d:%s] resourceFileName=%s
[%s:%d:%s] num of objects pending deletion %u
BUG in Airship: attempted to activate terminated driver @%s:%u
set_availability_blockers
set_value
update_context_info_addr_registers
[%s:%d:%s] marking driver state as running; trigger IPC driver exit_reset
BUG in Airship: unaligned device memory access
[%s:%d:%s] starting messenger
[%s:%d:%s] opening mcr
[%s:%d:%s] trigger superdispatch for SetPowerState
emplace_back
failure_code
[%s:%d:%s] reset type=%u
[%s:%d:%s] region id %hu removing memregion_controller
[%s:%d:%s] map successful
[%s:%d:%s] driver name: %s
handle_create_memory_mapping
update_head_index
dequeue_batch
handle_probe_exec_stage
length
airship_acipc_tr_dequeue_batch
[%s:%d:%s] (crid %hu) invalid hi: %hu
[%s:%d:%s] Added context id %hu
[%s:%d:%s] ts: last_write %llx, schedule %llx, deadline %llx, 
[%s:%d:%s] sw timeout scale for proxima protium platform: %llu
[%s:%d:%s] failed to look up configuration for %s[%u]
direct_client_object.cpp
dump_list
BUG in client of Airship: externally managed ring @%s:%u
downlink-update-failure
pci_transport.cpp
Airship ACIPC protocol error @%s:%u
handle_append_ipc_driver_state_dump
[%s:%d:%s] updating context info address register
queue
dump_pending_transfer_stats
transfer_queue.cpp
enqueue_transfer
[%s:%d:%s] updated power state: %u, current %u
[%s:%d:%s] (trid %hu) index %hu exceeds size %hu
BUG in client of Airship: attempted to access inactive driver @%s:%u
BUG in Airship: attempted to activate active object @%s:%u
v8@?0
ipc_handshake_timeout_occurred
[%s:%d:%s] (crid %hu) reaping cr
set_map_clientdata
tr_index_count
[%s:%d:%s] image sent for ipc stage %s
acipc_create_doorbell_controller
set_external_handler
set_power_target
[%s:%d:%s] (crid %hu) controller reset
[%s:%d:%s] stopping trid %hu for reason %u
raise_ipc_error
[%s:%d:%s] entering host sleep
[%s:%d:%s] region id %hu exec stage mismatch %u
[%s:%d:%s] invoking exec stage change handler: %u
[%s:%d:%s] debugInfo capture complete, size %u
BUG in client of Airship: attempted to set external interrupt handler for terminated driver @%s:%u
???
CentauriAlpha
update_ipc_control_register
[%s:%d:%s] entering device sleep
transfer_footer_size
[%s:%d:%s] (ctxid %hu) stopping controller
erase
BUG in Airship: attempted to create boxed string from null format string
AirshipDeviceDK
set_exec_stage
request_context_close
BUG in Airship: bad parameter - 'header_length' @%s:%u
open
~driver_client
BUG in Airship: refcount_mixin retained after release
[%s:%d:%s] sleep status invalid
[%s:%d:%s] starting timer with interval (%u)
BUG in Airship: invalid src
BUG in client of Airship: attempted to activate monitor with event handlers but without queue @%s:%u
scratch_size
getDriverNominalStateDumpSize
get_free_space
BUG in Airship: attempted to activate canceled object @%s:%u
[%s:%d:%s] (bc %s) reseting boot controller
[%s:%d:%s] (crid %hu) update bad cd
is_cr_completion_context_for_tr
stop_region
CentauriHelperMemregionUserClient
completion_ring_did_flush
[%s:%d:%s] (trid %hu) completions synthesized
[%s:%d:%s] (trid %hu) update bad transfer completion
wakeup
BUG in Airship: bad array access
parse_optional
BUG in Airship: Attempted to perform a health check in driver_client
Chipset
[%s:%d:%s] (trid %hu) stopping controller
device-signalled error
leeway_usec
doorbell_moderation
[%s:%d:%s] creating memregion controller for %s[%u]
[%s:%d:%s] (bc %s) image sent, recomputing state
insert
offset
shortcomp_complete_subsequent_transfers
[%s:%d:%s] (trid %hu) registering interrupt and setting up index array signaler vector %hu
exit_reset
CentauriBeta
advance_tail_index
BUG in client of Airship: attempted to activate canceled interrupt @%s:%u
[%s:%d:%s] boot manager is in reset
BUG in client of Airship: attempted to destroy client with subordinate object handles
driver_client.cpp
[%s:%d:%s] IPC driver state dump size %u
[%s:%d:%s] closing context id %hu
[%s:%d:%s] failed to look up configuration for %s
[%s:%d:%s] type=%u, debug meta-data=0x%llx, name=%s
[%s:%d:%s] driver create client begin %s
sleep-failure
downlink-buffer-count-len-error
create
IOPCIDeviceMemoryMapBase
[%s:%d:%s] (bc %s) sending image
parse_array
[%s:%d:%s] region id %hu sending memory map message
devicePowerStateChanged
set_interrupt_execution_queue
[%s:%d:%s] (bc %s) stopping boot controller
[%s:%d:%s] (crid %hu) failed to validate client override
[%s:%d:%s] opening mtr
BUG in Airship: 
[%s:%d:%s] setting boot controller for ipc stage %s to unavailable
[%s:%d:%s] message failed, setting state for region id %hu
retrieveDriverStateDumpInfo
[%s:%d:%s] reserve %u complete
get_paddr
not privileged
ipc_reset_occurred
[%s:%d:%s] device : active %u, registered %u, power init complete %u
init
[%s:%d:%s] main ipc stage name %s
missing object
[%s:%d:%s] currentPower %u, pendingPower %u, device valid %s
[%s:%d:%s] (trid %hu) registering doorbell %s, selector %u
mem_read
populate_state_dump_info
[%s:%d:%s] index %hu, message length %u
BUG in client of Airship: attempted to access inactive interrupt
reserve_next
[%s:%d:%s] image response %u, code %u
[%s:%d:%s] (crid %hu) cr terminated
get_element
[%s:%d:%s] (trid %hu) free transfers %hu must exceed dead space size %hu
handle_create_interrupt_source
unexpected object type
ipc_status_interrupt
[%s:%d:%s] failed to set client overrides for %s[%u]
BUG in Airship: access to null buffer @%s:%u
BUG in Airship: attempted to find existing boxed symbol from null string
BUG in client of Airship: attempted to activate active interrupt @%s:%u
resource
optimized_completion
populate_context_info
create_interrupt
bad argument
transfer_ring_opened
get_proxima_platform
BUG in Airship: attempted to insert null value into boxed dictionary @%s:%u
buffer_array
interval_usec
BUG in client of Airship: attempted to reconfigure active CR
read_head_index
[%s:%d:%s] crid %hu status %u
[%s:%d:%s] associating crid %hu <-> trid %hu
boxed_types.cpp
registers
completion_groups
[%s:%d:%s] boot manager is already out of reset
[%s:%d:%s] creating tr controller for %s[%u]
[%s:%d:%s] (trid %hu) transfer flush failed
v16@?0^v8
[%s:%d:%s] already in reset
name
check_async
[%s:%d:%s] message success
context_open_message_completed
[%s:%d:%s] tr_open 
[%s:%d:%s] invalid params
max
[%s:%d:%s] starting driver
[%s:%d:%s] current blockers (%u), blockers cleared (%u)
[%s:%d:%s] (trid %hu) controller opened
[%s:%d:%s] getting transfer completion for tag %hu
close_tr
[%s:%d:%s] updating register at bank=%u, offset=%u
non-default completion group requires out-of-order
direct_client.cpp
set_mirror_enabled
uplink-update-failure
[%s:%d:%s] (crid %hu) registering interrupt and setting up index array signaler vector %hu
~ring_manager
tr_settled
BUG in Airship: bad parameter - 'footer_length' @%s:%u
BUG in client of Airship: attempted to set external interrupt handler for inactive driver
[%s:%d:%s] context id %hu close message requested
~driver_resource
update_mem_window_base_and_size
compute_io_status_for_transfers
get_first_completed_tag
get_device_sw_scaled_timeout
with_str
BUG in Airship: attempted to access boxed dictionary with null key @%s:%u
main_ipc_state_machine
airship-trap-on-device-attach-timeout
[%s:%d:%s] canceling timer
[%s:%d:%s] failed to retrieve property '%s'
find_exec_stage_with_value
bank
image_interrupt
compute_hdrftr_size_fields
NewUserClient_Impl
reduce_size
ring_index_pair
exec_stage
interrupts
BUG in Airship: Ring is disconnected or in limbo. @%s:%u
BUG in client of Airship: attempted to reconfigure active TR @%s:%u
teardown_boot_ipc_stage
[%s:%d:%s] (ctxid %hu) close complete
[%s:%d:%s] pending IPC exec stage broadcast
[%s:%d:%s] destroying completion ring handle for crid %hu
[%s:%d:%s] context id %hu close message result %u
BUG in client of Airship: attempted to access inactive TR @%s:%u
teardown_current_ipc_stage
window_base_lo
recompute_region_availability
loadBundleResourceByName
print_queue_stats
B24@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}16
t2026
skip_window_configuration
set_queue
[%s:%d:%s] setting up mtr
operator()
is_healthy
[%s:%d:%s] airship sw scaling %llu
[%s:%d:%s] failed to find stage for value, %u
constraints
[%s:%d:%s] creating airship driver handle
[%s:%d:%s] in_reset %u, activated %u
[%s:%d:%s] (crid %hu) trid %hu does not accept completions from this cr
image_size
[%s:%d:%s] (trid %hu) unexpected flush notice from CRID %hu
[%s:%d:%s] (trid %hu) do not overwrite existing bad tx completion buffer
[%s:%d:%s] (bc %s) out code=%u
debug_infra.hpp
ipc-running-timeout
~reaper
active
[%s:%d:%s] creating device memory
debug
stop_block_invoke
destroy_client
[%s:%d:%s] initializing PCI device
BUG in Airship: attempted to add duplicate resource @%s:%u
v32@?0Q8^{IOService=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})}16Q24
BUG in Airship: attempted to insert element at position not in list @%s:%u
BUG in client of Airship: attempted to reconfigure active CR @%s:%u
BUG in client of Airship: invalid queue role
BUG in client of Airship: attempted to set interrupt execution queue for terminated driver
handle_mem_read16
BUG in Airship: attempted to create boxed string from null format string @%s:%u
refcount_mixin.hpp
enterReset
BUG in client of Airship: attempted to set external interrupt handler for terminated driver
Stop_Impl
removeDriver
request_cr_close
OSAction_AirshipOSActionProxy_InterruptOccurred
cancel_participant
environment.cpp
consume_elements
airship-trap-on-ipc-power-on-timeout
BUG in Airship: unexpected flush notice
BUG in client of Airship: attempted to register handler for terminated driver @%s:%u
[%s:%d:%s] crid %hu is associated with trid %hu
[%s:%d:%s] (trid %hu) new doorbell interval (%u us), new leeway (%u us)
driver_object.cpp
~devmem_mapping_manager
device sleep
set_source_maintenance_completion_handler
BUG in Airship: attempted to create cr_controller in driver_client
Airship device power off timed out @%s:%u
[%s:%d:%s] current blockers (%u), set blockers (%u)
swizzle_proxima_viddid_for_platform
BUG in Airship: invalid head index advance operation
get_size
%s %s@%u
[%s:%d:%s] sleep status: host sleep
image_table
[%s:%d:%s] object manager list not empty; dumping direct client objects
[%s:%d:%s] Registering head index update handler for crid %hu at vector %hu
mutex
[%s:%d:%s] sleep status: %s
request_tr_close
[%s:%d:%s] added trid %hu
[%s:%d:%s] context_open 
BUG in Airship: attempted to remove element not in list @%s:%u
compute_offsets
BUG in Airship: _memory is NULL @%s:%u
release_resource
t2026-CentauriBeta
t2026-CentauriBeta_BetaPrimeFPGA
multiple-errors
channel-update-failure
[%s:%d:%s] (bc %s) image_state=%u
~monitor_target
doorbell_timer_tolerance_us
merge_location
BUG in client of Airship: nonzero offset/length for NULL resource
close_context
BUG in Airship: attempted to remove element not in list
[%s:%d:%s] participant 0x%llx added to doorbell %s[%u]
[%s:%d:%s] tearing down main ipc stage
arm_cr_index_vector
AirshipDeviceClass
optional.hpp
driver_debug_object.hpp
airship-trap-on-device-power-off-timeout
driverkit_event_call
BUG in client of Airship: attempted to access inactive mirror @%s:%u
[%s:%d:%s] closing mtr
BUG in Airship: bad optional access @%s:%u
acipc.cpp
[%s:%d:%s] acipc driver activate complete
window_base_hi
set_device_region_status
acipc_create_memregion_controller
~async_accelerator
get_and_advance_inorder_idx_for_enqueue
driver_object
[%s:%d:%s] Airship: device attach deadline %u ms, starting timer
close_cr
[%s:%d:%s] derivedStart successful\n
is_sleep_status_valid
mode
BUG in Airship: refcount_mixin retain overflow
[%s:%d:%s] mapping region of size %u for %s[%u]
[%s:%d:%s] getting auto-exit reset
BUG in client of Airship: attempted to access inactive CR
recomputePowerRequest
check_all_cr_close_requests
send_cr_close_message
bad-inplace-completion
handle_exit_reset
BUG in client of Airship: out of bounds access to buffer
append_cr_index_info
acipc_types.cpp
BUG in client of Airship: selector is invalid
hexdump
set_ipc_error_handler
process_pending
boot_ipc_stages
[%s:%d:%s] reaping %s[%u]
nil
~direct_client_object_manager
driverkit_queue_callback
IOPCIDeviceMapperPageSize
BUG in client of Airship: attempted to access inactive context @%s:%u
[%s:%d:%s] region id %hu adding memregion_controller
[%s:%d:%s] creating handle for transfer ring with trid %u
~cr_controller
cr_open_message_completed
with_format
exec_stage_interrupt_occurred
BUG in Airship: invalid head index update operation @%s:%u
send_context_open_message
doorbell
boot_controller
[%s:%d:%s] enqueuing message in mtr
BUG in Airship: list element destroyed while in list @%s:%u
acipc_create_boot_controller
[%s:%d:%s] removing interrupt source %u
create_state_monitor
BUG in Airship: bad boxed access
value out of bounds
[%s:%d:%s] stopping boot controller for ipc stage %s
[%s:%d:%s] message success, setting state for region id %hu
ipc_power_on_timeout_ms
[%s:%d:%s] probing device
register_cr_index_vector_action
[%s:%d:%s] failed to get resource
main
BUG in client of Airship: attempted to activate monitor with event handlers but without queue
header_size
deregister_tr_index_vector_action
enable_interrupt_vector
chipset
CentauriHelperInterfaceUserClient
release
is_cr_required_completion_context_for_any_open_tr
ipc_running_timeout
Airship device power on timed out @%s:%u
[%s:%d:%s] reserving ring with selector %u
find_completion_target
logging.cpp
mem_write32
Default
[%s:%d:%s] context id %hu status %u
set_mode
handle_mem_write16
get_image_response
[%s:%d:%s] setting context id %hu closed
index
trigger_driverkit_maintenance
retrieve_state_dump
mem_write
[%s:%d:%s] crid %hu close message result %u
[%s:%d:%s] (trid %hu) seek %hu exceeds pending transfer count %hu
remove_flusher
~driver
insert_before
[%s:%d:%s] image has already been sent
ring_pool.cpp
~direct_client_object
[%s:%d:%s] trid %hu set as open
BUG in Airship: airship_acipc_tr_disconnect: not implemented @%s:%u
async_callback
[%s:%d:%s] (trid %hu) sending close message
[%s:%d:%s] (trid %hu) close complete
BUG in Airship: index out of range @%s:%u
~driver_object_termination_list
deviceMatched
airship-poweron-timeout-waiting-for-pci-device
base.cpp
timeout
get_vector_for_interrupt
BUG in Airship: invalid head index update operation
handlePendingDevicePowerOffIfNeeded
driverkit_event_callback
[%s:%d:%s] (crid %hu) new device ring status=%u
get_max_message_length
[%s:%d:%s] context id %hu has unmessaged lifecycle, closing
capability
context_info_address_hi
reliable
attachToPendingDeviceIfNeeded
set_context_closed
[%s:%d:%s] cannot set transport, %s ipc stage is not null
driver_ioservice_params
[%s:%d:%s] setting up callout notifier
false
with_cstr
[%s:%d:%s] exec stage reg value=%u
[%s:%d:%s] (trid %hu) attempt to consume %hu transfers, %hu fetched
handle_mem_write8
set_context_open
update_debug_ring_state
[%s:%d:%s] stop reason %u
~devmem_mapping
BUG in Airship: requested TD element is inactive
[%s:%d:%s] %s[%u] reset
get_mh_uuid
create_debug_object
BUG in Airship: attempted to activate active object
[%s:%d:%s] context id %hu open message result %u
BUG in client of Airship: attempted to reconfigure active memregion
BUG in Airship: requested CD element is inactive @%s:%u
BUG in Airship: attempted to insert null value into boxed dictionary
[%s:%d:%s] applied errata window_base_mask=%#llx, masked_base=%#llx
count
boot_manager.cpp
[%s:%d:%s] %s[%u] stopped
requestDevicePower
BUG in Airship: flat array size multiplication overflow @%s:%u
[%s:%d:%s] probing exec stage register
[%s:%d:%s] device power off deadline expired
~ring_pool
async_accelerator_private.cpp
completion_ring_will_flush
rw_mutex.hpp
BUG in client of Airship: externally managed ring
BUG in Airship: refcount_mixin overreleased
BUG in Airship: Attempted to perform a health check in driver_client @%s:%u
disconnected (no device)
mappable_buffer.cpp
set_configuration
[%s:%d:%s] (crid %hu) stopping controller
[%s:%d:%s] (crid %hu) do not overwrite existing bad_cd buffer
BUG in Airship: list element destroyed while in list
BUG in client of Airship: attempted to reconfigure active monitor @%s:%u
memory_unmap_message_completed
[%s:%d:%s] (ctxid %hu) open failed 0x%x
vendor
[%s:%d:%s] no devices to attach to
open_tr
set_tr_open
[%s:%d:%s] entering reset
BUG in client of Airship: attempted to activate already-active memregion
invalid alignment
mtr
sync_action_flush_pending_transfers
set_cancel_handler
Start_Impl_block_invoke
B16@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8
[%s:%d:%s] begin power change; power flags %u
BUG in Airship: refcount_mixin overreleased @%s:%u
set_size
peripheral_info_interrupt
send_memory_map_message
[%s:%d:%s] creating handle for completion ring with crid %u
tr_controller.cpp
BUG in client of Airship: attempted to activate active driver @%s:%u
compute_free_space
driver.cpp
system-failure
host-wake-failure
[%s:%d:%s] requesting close for crid %hu
[%s:%d:%s] setting crid %hu open
[%s:%d:%s] context id %hu set as open
BUG in Airship: attempted to find existing boxed symbol from null string @%s:%u
monitor.cpp
[%s:%d:%s] tearing down current ipc stage
[%s:%d:%s] setting up boot ipc stage
dump_object_info
[%s:%d:%s] (bc %s) image response code=%u
~intrusive_list_link
[%s:%d:%s] power flags changed to %u
BUG in client of Airship: attempted to reconfigure active interrupt
register_tr_index_vector_action
consume_transfers
[%s:%d:%s] (crid %hu) new doorbell interval (%u us), new leeway (%u us)
AncestorRegistryID
remove_cr
flush_tr_settlement
[%s:%d:%s] closing crid %hu
[%s:%d:%s] timer deadline missed!!
handle_enter_reset
startTimer
[%s:%d:%s] power state change deadline expired
set_open_clientdata
[%s:%d:%s] coordinator state=%u, new IPC stage=%s
[%s:%d:%s] main ipc state is not running (%u) or transport is not set
AirshipDeviceCriteria
round_up_to_page_size
BUG in client of Airship: attempted to create client for inactive driver @%s:%u
BUG in client of Airship: attempted to set interrupt execution queue for terminated driver @%s:%u
check_for_image_response
direct_tr_controller.cpp
request_region_unmap
t2026-CentauriAlpha_AlphaPrimeFPGA
transfer_queue
enter_reset
BUG in Airship: attempted to insert element already in list @%s:%u
BUG in Airship: ring size cannot be zero
bad-tr-ti-update
Dale
[%s:%d:%s] (bc %s) old state=0x%llx, new state=0x%llx
sync_action_process_hi_update
[%s:%d:%s] trid %hu is settled
BUG in client of Airship: attempted to activate active interrupt
~direct_cr_controller
process_completions
send_overflow_messages
[%s:%d:%s] (trid %hu) new mode (%u)
is_ipc_status_valid
[%s:%d:%s] setting up ipc status interrupt
[%s:%d:%s] ipc status=%u
buffer_size_ring
copy_and_zerofill
[%s:%d:%s] (trid %hu) controller reset
image_response
unexpected-sleep-status
[%s:%d:%s] cannot wake
[%s:%d:%s] oversize host memory window reduced from %#llx to UINT32_MAX
shared_timestamp
constraints not satisfied by default
[%s:%d:%s] region id %hu is in limbo, attempting to unmap
[%s:%d:%s] Deregistering tail index update handler for trid %hu at vector %hu
BUG in client of Airship: Packet is null for queue entry. @%s:%u
probe_exec_stage_register_if_ready
completion_header_size
parse_symbol
buffer_create_with_iomd
BUG in Airship: bad parameter - 'size' @%s:%u
reserve
operation canceled
[%s:%d:%s] exec_stage during power-on=%u
airship-trap-on-ipc-power-off-timeout
emplace
get_queue
[%s:%d:%s] creating mtr
[%s:%d:%s] sending open message for trid %hu
ambiguous name
ipc_control
[%s:%d:%s] (ctxid %hu) new availability blockers 0x%08x
BUG in Airship: requested TD element is inactive @%s:%u
BUG in client of Airship: Failed to locate completion ring config
get_addr
add
BUG in client of Airship: attempted to reconfigure active driver
[%s:%d:%s] dbs : total %lu, active %lu, pending %d
BUG in client of Airship: mode must be AIRSHIP_ACIPC_TR_MODE_BATCH @%s:%u
BUG in Airship: attempted to create boxed symbol from null C string
ring_size
[%s:%d:%s] region id %hu deferring unmap message
BUG in client of Airship: attempted to create client for inactive driver
BUG in client of Airship: attempted to set interrupt execution queue for inactive driver
BUG in Airship: attempted to activate canceled object
BUG in client of Airship: mode must be AIRSHIP_ACIPC_TR_MODE_STANDARD
set_backing_ring_size
[%s:%d:%s] sending message now
[%s:%d:%s] processing completions
Start_Impl
send_context_close_message
[%s:%d:%s] crid %hu in limbo
[%s:%d:%s] sending open message for crid %hu
get_mirror_element
consume_mirror_elements
[%s:%d:%s] (crid %hu) registering with doorbell coordinator with doorbell %s
clearPowerAssertion
[%s:%d:%s] Initializing device
BUG in client of Airship: attempt to reconfigure active context @%s:%u
remove_context
[%s:%d:%s] reset type %u
set_completion_ring
nominal_transfer_size
acipc_private.cpp
[%s:%d:%s] (trid %hu) free=%hu, queued=%hu, pending=%hu, completed=%hu, fetched=%hu
send_tr_open_message
cr_close_message_completed
suspend
doorbell_controller.cpp
airship-trap-on-acipc-error
device_info
[%s:%d:%s] power flags (%u), current IPC power state (%u)
move_transfers
unregister_statedump_collection_handler
[%s:%d:%s] failed to flatten name/sel into string
BUG in Airship: oversize ring
setTransportBlocker
interrupt
[%s:%d:%s] (crid %hu) open failed 0x%x
[%s:%d:%s] removed trid %hu
image_address_lo
[%s:%d:%s] (ctxid %hu) controller reset
AirshipDevice attach timeout
update_power_state
state_dump_manager.cpp
set_cr_closed
~boot_manager
Airship IPC power off timed out @%s:%u
mem_write16
send_image
com.apple.AirshipDeviceDK.service-default
open_cr
copy_debug_info
airship_platform_get_timer_queue_block_invoke
BUG in Airship: attempted to add duplicate resource
version
[%s:%d:%s] (trid %hu) new device ring status=%u
BUG in Airship: attempted to access terminated driver
[%s:%d:%s] (bc %s) image valid : %s 
update_completion_desc_debug_info
[%s:%d:%s] (crid %hu) invalid completion descriptor at idx=%hu
release_obj
BUG in client of Airship: attempted to await inactive monitor @%s:%u
BUG in client of Airship: attempted to access inactive driver
ALLOCATION FAILURE (or BUG) in Airship
typed_delete
enqueue_batch
BUG in Airship: refcount_mixin retained after release @%s:%u
BUG in client of Airship: attempted to activate canceled monitor @%s:%u
update_tail_index
BUG in Airship: invalid tail index update operation @%s:%u
BUG in client of Airship: attempted to overwrite driver transport
host-sleep-failure
BUG in Airship: attempted message send in reset
BUG in Airship: attempted to access boxed dictionary with null key
tr_ring
[%s:%d:%s] Airship statedump complete: provided buffer size %u copied %u
set_footer_size
[%s:%d:%s] tearing down mtr
AirshipDeviceDK.cpp
set_cr_open
BUG in client of Airship: attempt to reconfigure active TR
Centauri
BUG in client of Airship: nonzero selector for NULL resource
[%s:%d:%s] viddid=%#x
devmem_mapping
[%s:%d:%s] invalid configuration: %s at %s
value exceeds ipc stage limit
[%s:%d:%s] adding boot controller for ipc stage %s
get_entry_at_index
create_device_memory_mapping
AirshipDriverDK.cpp
[%s:%d:%s] removing participant 0x%llx from pending queue
[%s:%d:%s] (trid %hu) new interrupt %s[%u]
[%s:%d:%s] main ipc state is not set
[%s:%d:%s] not ready for peripheral info interrupt
set_error
ipc_power_off_timeout_ms
[%s:%d:%s] (bc %s) detail=0
check_all_context_close_requests
doorbell_coordinator.cpp
unexpected-ipc-status
t2026-CentauriAlpha
flush_DROPS_LOCK
ring_manager.cpp
CentauriControl
[%s:%d:%s] invalid device
finalize_indices
BUG in Airship: access to non-held resource @%s:%u
transfer_rings
detachFromDevice
airship-transport-setup-failure
multicomp_complete_prior_transfers
device_memory.hpp
isPoweringOff
set_capacity
[%s:%d:%s] new item at index %hu
handle_get_nominal_state_dump_size
BUG in Airship: size is too big
[%s:%d:%s] (trid %hu) failed to find first transfer
advance_buffer_pointer
unknown context
[%s:%d:%s] (ctxid %hu) failed to validate client override
get_page_size
driverkit_maintenance
cldma-link-error
direct_context.cpp
send_cr_open_message
append_context_state_dump
derivedProbeDevice
dequeue_batch_with_limit
image_doorbell
auxiliary_contexts
BUG in Airship: attempted to retrieve max message length in reset @%s:%u
[%s:%d:%s] ring manager already out of reset
[%s:%d:%s] sending close message for context id %hu
BUG in Airship: flat array size multiplication overflow
out-of-place completion requires completion ring
accumulation
[%s:%d:%s] failed to aquire resource for %s[%u]
process_inplace_completions
BUG in client of Airship: nonzero selector for NULL resource @%s:%u
[%s:%d:%s] stopping context id %hu
[%s:%d:%s] platform_config=%u, probed viddid=0x%#x,  proxima_viddid=0x%#x
[%s:%d:%s] value %u matches to exec stage: %s
[%s:%d:%s] (ctxid %hu) reaping context controller
Start_Impl_block_invoke_6
set_ipc_error_flags
BUG in client of Airship: attempted to reconfigure active interrupt @%s:%u
write_cr_tail_index
[%s:%d:%s] unmapping memory region for %s[%u]
not open
async_notifier.cpp
with_cstr_nocopy
ipc_status_interrupt_occurred
setup_notifier
com.apple.AirshipDriverDK.global.%s
BUG in Airship: invalid dst
Airship timer watchdog expired: expected at 0x%llx (currently 0x%llx)
unregister_client_statedump_handler
BUG in client of Airship: attempted to activate already-active context
[%s:%d:%s] unknown proxima-platform: %llu
handle_clear_transport
remove
BUG in Airship: attempted to create boxed symbol from null string
out_of_order
clearTransportBlocker
[%s:%d:%s] (trid %hu) first index %hu exceeds size %hu
not ready
set_doorbell_moderation
system-error
[%s:%d:%s] region %s (id=%hu) cannot be used due to id conflict with name %s
[%s:%d:%s] device attach deadline expired
[%s:%d:%s] stopping crid %hu for reason %u
finalize_tr_settlement_if_ready
BUG in Airship: attempted truncate to larger size
add_doorbells
BUG in client of Airship: Packet is null for queue entry.
com.apple.airship.global-sleep-queue
memregion_controller.cpp
[%s:%d:%s] activating %s[%u]
cancelTimer
[%s:%d:%s] value for shared constant doorbell: %u
cr_ring
enqueue_transfer_with_ioun_packet
teardown_main_ipc_stage
parse_number
BUG in Airship: attempted to insert element at position not in list
BUG in client of Airship: attempted to unregister handler for inactive driver
create_sync_monitor
airship-read-before-sleep-update
boot_controller.cpp
process_completion_descriptors
[%s:%d:%s] (crid %hu) failed to complete transfer
BUG in client of Airship: mode must be AIRSHIP_ACIPC_TR_MODE_BATCH
airship-sw-timeout-scale
[%s:%d:%s] %s[%u] unavailable
[%s:%d:%s] (trid %hu) first transfer not found
BUG in client of Airship: attempted to activate already-active CR
%s-%u
[%s:%d:%s] setting trid %hu open
[%s:%d:%s] tearing down boot ipc stage
AirshipDevice attach timeout @%s:%u
[%s:%d:%s] not in reset
read_tail_index
already in use (exclusive access)
[%s:%d:%s] (crid %hu) sending close message
direct_memregion.cpp
min
resolve
completion_ring
[%s:%d:%s] getting device criteria
 %02x
BUG in client of Airship: attempted to register handler for inactive driver
send_memory_unmap_message
[%s:%d:%s] setting trid %hu closed
~direct_tr_controller
BUG in Airship: attempted to create boxed string from null C string
append_element
[%s:%d:%s] starting ipc handshake timer; timeout=%u ms
[%s:%d:%s] clearing power state not ready blocker
typed_allocators.cpp
[%s:%d:%s] starting device
[%s:%d:%s] cr_open 
in_place
protocol
[%s:%d:%s] kIOServiceNotificationTypeTerminated
[%s:%d:%s] capture streaming logs
[%s:%d:%s] (trid %hu) transfer enqueue size %u exceeds maximum transfer size %u
write_head_index
AirshipBuiltIn
BUG in Airship: bad boxed access @%s:%u
derivedStart
bad key
errorOccurred
airship-driverkit-timer-watchdog
start_block_invoke
BUG in Airship: attempted to create client for terminated driver @%s:%u
get_mirror_count
set_tr_closed
BUG in client of Airship: attempted to reconfigure active memregion @%s:%u
acipc doorbell
BUG in client of Airship: attempted to activate already-active TR @%s:%u
setup_main_ipc_stage
group_stride
[%s:%d:%s] Airship error occurred (0x%x), ipcErrorState (0x%x)
unable to map memory
[%s:%d:%s] setting external execution queue for vector %u
[%s:%d:%s] resuming doorbell coordinator
completion_mirror.cpp
[%s:%d:%s] ACIPC protocol error 0x%08x (%s)
BUG in Airship: wrong index @%s:%u
BUG in client of Airship: selector is not available @%s:%u
BUG in client of Airship: attempted to set external interrupt handler for inactive driver @%s:%u
io-timeout
set_event_handler
BUG in Airship: ring size cannot be zero @%s:%u
bad-cr-hi-update
register
[%s:%d:%s] setting up timer
log
mcr
remove_tr
[%s:%d:%s] added crid %hu
mutex.hpp
get_health_status
unsupported value
multi
resource_stride
shared_constant
airship-poweroff-timeout-waiting-for-firmware
local
remove_participant
BUG in client of Airship: Cannot destroy handle before ring has been closed. @%s:%u
unexpected mode string
get_prev_transfer_in_queue
interrupt_occurred
[%s:%d:%s] window base: 0x%llx, window size: 0x%llx
cr_controller.cpp
BUG in Airship:  @%s:%u
schedule_update
get_current_ipc_stage_name
static_array.hpp
[%s:%d:%s] crid: %u
BUG in Airship: attempted to create client for terminated driver
BUG in client of Airship: attempted to unregister handler for terminated driver @%s:%u
[%s:%d:%s] crid %hu has unmessaged lifecycle, setting closed
unexpected-transport-revocation
advance_head_index
unsupported register width
parse_dict
BUG in Airship: attempted to use inactive object
notify_transfer_ring_when_flushed
[%s:%d:%s] stopping trid %hu
[%s:%d:%s] trid %hu has unmessaged lifecycle, setting open
BUG in client of Airship: attempted to access inactive TR
instance count is zero
transfer_header_size
[%s:%d:%s] handle_activate: result 0x%x
BUG in client of Airship: attempted to overwrite driver transport @%s:%u
send_message
setPowerAssertion
add_tr
tr_close_message_completed
[%s:%d:%s] crid %hu belongs to the same group as %hu
get_value
/System/DriverKit/System/Library/PrivateFrameworks/AirshipDK.framework
BUG in Airship: attempted message send in reset @%s:%u
[%s:%d:%s] context id %hu has unmessaged lifecycle, setting closed
[%s:%d:%s] messenger failed to map mtr/mcr memory
~client_interrupt
addPowerAssertion
[%s:%d:%s] removed crid %hu
[%s:%d:%s] %s[%u] state %u, detail 0x%u
com.apple.AirshipDriverDK.service-default
airship-poweron-timeout-waiting-for-firmware
messenger.cpp
peripheral_info_update_filter
[%s:%d:%s] ipc status invalid
[%s:%d:%s] sleep status: active
read_index_array
AirshipDriverConfigName
[%s:%d:%s] located transfer ring configuration, adding %u instances
general error
BUG in client of Airship: Invalid mode: AIRSHIP_ACIPC_TR_MODE_STANDARD (method not accessible)
bad-cd
[%s:%d:%s] ipc stage not torn down, boot stage valid: %u, main stage valid: %u
BUG in client of Airship: attempted to access inactive interrupt @%s:%u
context_controller.cpp
get_inorder_tag_for_enqueue
[%s:%d:%s] (trid %hu) completing chain
BUG in Airship: attempted to activate terminated driver
device_classifier.cpp
[%s:%d:%s] created completion mirror object
[%s:%d:%s] setting up main ipc stage
min_interval_usec
BUG in Airship: oversize ring @%s:%u
handle_mem_write32
[%s:%d:%s] (bc %s) computing image table
[%s:%d:%s] creating mcr
isIpcPowerStateValidForDriverPowerState
probe_exec_stage
[%s:%d:%s] creating dispatch queue
[%s:%d:%s] sending close message for trid %hu
sync
send_tr_close_message
BUG in Airship: attempted truncate to larger size @%s:%u
will_set_transport
change_to_ipc_stage
[%s:%d:%s] region %s (id=%hu) cannot be used due to name conflict with id %hu
BUG in client of Airship: attempted to destroy client with subordinate object handles @%s:%u
device_power_on_timeout_ms
finish_queued_partial_chain
~interrupt_manager
BUG in client of Airship: attempted to activate already-active CR @%s:%u
[%s:%d:%s] acquiring resource %s
get_next_transfer_in_queue
[%s:%d:%s] (trid %hu) sending open message
append_debug_stats
[%s:%d:%s] sending any overflow messages
activate
get_flattened_name_sel_string
[%s:%d:%s] crid %hu is not associated with any open trs
device_transport.cpp
update_debug_client_overrides
BUG in Airship: requested CD element is inactive
~monitor
BUG in client of Airship: attempted to activate interrupt with event handlers but without queue @%s:%u
[%s:%d:%s] boot manager exiting reset
[%s:%d:%s] region id %hu sending unmap message
set_external_management
set_interrupt_handler
set_context
driver_resource.cpp
[%s:%d:%s] current main ipc stage and transport must be set
main_ipc_stages
BUG in Airship: unrecognized detail bits in context controller. @%s:%u
[%s:%d:%s] automatically placing driver in reset
[%s:%d:%s] destroying transfer ring handle for trid %hu
[%s:%d:%s] (trid %hu) moving queued transfers into pending state
[%s:%d:%s] (trid %hu) state=%u, activated=%u
[%s:%d:%s] failed to get device memory window config
[%s:%d:%s] creating cr controller for %s[%u]
default
[%s:%d:%s] located completion ring configuration, adding %u instances
BUG in Airship: invalid dst @%s:%u
[%s:%d:%s] (trid %hu) TR is now settled
[%s:%d:%s] exiting reset
[%s:%d:%s] syncing mcr head index update
doorbell_coordinator
~acipc_driver
[%s:%d:%s] wake requested=%u, target host sleep=%u, permit device sleep=%u
BUG in client of Airship: attempted to reconfigure active monitor
success_code
BUG in Airship: attempted to initialize optional with sentinel value @%s:%u
stop
transfer_ring_settled
config_from_doorbell_spec
create_resource_monitor
BUG in Airship: access to null buffer mapping @%s:%u
[%s:%d:%s] (crid %hu) sending open message
BUG in client of Airship: attempt to reconfigure active context
[%s:%d:%s] stopping crid %hu
[%s:%d:%s] context id %hu in limbo
%zu
[%s:%d:%s] (trid %hu) create tx_queue: size %hu, hdrlen %u, ftrlen %u, out-of-order %u
[%s:%d:%s] (trid %hu) new availability blockers 0x%08x
set_client_overrides
[%s:%d:%s] consuming transfers
matchesCriteria
[%s:%d:%s] ring manager already in reset
[%s:%d:%s] removed context id %hu
[%s:%d:%s] unblocking device access
BUG in client of Airship: Failed to locate transfer ring config @%s:%u
[%s:%d:%s] (crid %hu) new interrupt %s[%u]
set_device_ring_status
[%s:%d:%s] sending open message for context id %hu
BUG in client of Airship: Cannot destroy handle before ring has been closed.
dal25
ipc_status
BUG in Airship: bad parameter - 'header_length'
isDevicePowerStateValidForDriverPowerState
set_transport
handle_get_mem_window_info
release_image_transfer_resources
~reaper_target
window_base_mask
traffic_class
[%s:%d:%s] (crid %hu) applied client overrides
[%s:%d:%s] suspending transport
[%s:%d:%s] requesting close for context id %hu
[%s:%d:%s] setting context id %hu open
BUG in Airship: access to non-held resource
set_mcr_event_handler
[%s:%d:%s] not ready for ipc status interrupt
shared_counter
value exceedes auxiliary context limit
wait_context.cpp
bytes
direct_buffer.cpp
[%s:%d:%s] (ctxid %hu) applied client overrides
Vendor
rw_mutex
BUG in Airship: attempted to activate object without required configuration @%s:%u
add_participant
built-in
com.apple.iokit.pm.wakedescription
in-place completion requires in-order
footer_size
disallowed name
parse_array_or_singleton
[%s:%d:%s] (trid %hu) failed: hi=%hu, ti=%hu
setBusLeadAndMemoryEnable
peripheral_info_interrupt_occurred
sleep_control
index_array_vector
[%s:%d:%s] removing boot controller for ipc stage %s
BUG in Airship: _memory is NULL
roles
[%s:%d:%s] insufficient buffer
memory_regions
add_region
airship-poweroff-timeout-waiting-for-driver-quiesce
[%s:%d:%s] kIOServiceNotificationTypeMatched
set_settled
set_completion_group
set_power_state_change_handler
classify_image_response_code
uint64_value
BUG in Airship: invalid tail index advance operation @%s:%u
read_exec_stage_register
[%s:%d:%s] exec stage interrupt occurred: value %u
auxiliary_context
write_index_array
Airship IPC power on timed out
timerExpired
[%s:%d:%s] no ipc stage set
ipcCalloutOccurred
initDriverIOServiceParams
no space for data
BUG in client of Airship: attempted to access inactive mirror
[%s:%d:%s] (bc %s) detail=%u
enqueue_message_in_mtr
[%s:%d:%s] complete
probe
BUG in Airship: invalid tail index advance operation
unknown target
client_registers
ServiceNotificationReady_Impl
Airship device power off timed out
device_power_off_timeout_ms
reset
[%s:%d:%s] reset=%u, boot_state=%s, ipc_state=%s
width
doorbell value out of range
get_transfer_completion
create_client
[%s:%d:%s] syncing mtr tail index update and fetching completions
[%s:%d:%s] driver added successfully
value
~driver_object
exec_stage_interrupt
completion_ring_stride
memregion_manager.cpp
read_tr_tail_index
add_flusher
clear_transport
probe_image_response
[%s:%d:%s] not ready for exec stage interrupt
complete_transfer
Airship [%{public}s:%d:%{public}s] probing exec stage register
Airship [%{public}s:%d:%{public}s] region id %hu is in limbo, attempting to unmap
Airship [%{public}s:%d:%{public}s] debugInfo capture start
Airship [%{public}s:%d:%{public}s] (crid %hu) controller opened
Airship [%{public}s:%d:%{public}s] starting power off deadline timer
Airship [%{public}s:%d:%{public}s] (trid %hu) seek %hu exceeds pending transfer count %hu
Airship [%{public}s:%d:%{public}s] failed to retrieve property '%s'
Airship [%{public}s:%d:%{public}s] setting up mtr
Airship [%{public}s:%d:%{public}s] trid %hu has unmessaged lifecycle, setting open
Airship [%{public}s:%d:%{public}s] setting up boot ipc stage
Airship [%{public}s:%d:%{public}s] sleep status: host sleep
Airship [%{public}s:%d:%{public}s] Airship error occurred (0x%x), ipcErrorState (0x%x)
Airship [%{public}s:%d:%{public}s] (trid %hu) attempt to consume %hu transfers, %hu fetched
Airship [%{public}s:%d:%{public}s] IPC driver state_dump complete
Airship [%{public}s:%d:%{public}s] destroying transfer ring handle for trid %hu
Airship [%{public}s:%d:%{public}s] tearing down current ipc stage
Airship [%{public}s:%d:%{public}s] boot ipc stage name %s
Airship [%{public}s:%d:%{public}s] applied errata window_base_mask=%#llx, masked_base=%#llx
Airship [%{public}s:%d:%{public}s] messenger failed to map mtr/mcr memory
Airship [%{public}s:%d:%{public}s] starting driver
Airship [%{public}s:%d:%{public}s] (trid %hu) controller opened
Airship [%{public}s:%d:%{public}s] (bc %s) detail=0
Airship [%{public}s:%d:%{public}s] sleep status invalid
Airship [%{public}s:%d:%{public}s] crid %hu belongs to the same group as %hu
Airship [%{public}s:%d:%{public}s] setting up ipc status interrupt
Airship [%{public}s:%d:%{public}s] %s[%u] reset
Airship [%{public}s:%d:%{public}s] setting up timer
Airship [%{public}s:%d:%{public}s] setting external execution queue for vector %u
Airship [%{public}s:%d:%{public}s] change to exec stage %s (%u) from %s
Airship [%{public}s:%d:%{public}s] getting transfer completion for tag %hu
Airship [%{public}s:%d:%{public}s] stopping trid %hu
Airship [%{public}s:%d:%{public}s] context id %hu open message result %u
Airship [%{public}s:%d:%{public}s] deleted %hu items from mirror
Airship [%{public}s:%d:%{public}s] region %s (id=%hu) cannot be used due to id conflict with name %s
Airship [%{public}s:%d:%{public}s] (trid %hu) failed: hi=%hu, ti=%hu
Airship [%{public}s:%d:%{public}s] exec stage reg value=%u
Airship [%{public}s:%d:%{public}s] airship driver service is not active
Airship [%{public}s:%d:%{public}s] %{public}s
Airship [%{public}s:%d:%{public}s] (trid %hu) update bad transfer completion
Airship [%{public}s:%d:%{public}s] (crid %hu) failed to validate client override
Airship [%{public}s:%d:%{public}s] (ctxid %hu) open failed 0x%x
Airship [%{public}s:%d:%{public}s] (trid %hu) sending open message
Airship [%{public}s:%d:%{public}s] trid %hu close message requested
Airship [%{public}s:%d:%{public}s] updated power state: %u, current %u
Airship [%{public}s:%d:%{public}s] closing mcr
Airship [%{public}s:%d:%{public}s] crid %hu close message result %u
Airship [%{public}s:%d:%{public}s] property '%s' is not numeric
Airship [%{public}s:%d:%{public}s] driver ioservice params: ipcPowerOn %u ms, ipcPowerOff %u ms, devicePowerOn %u ms, devicePowerOff %u ms
Airship [%{public}s:%d:%{public}s] ring manager already out of reset
Airship [%{public}s:%d:%{public}s] cr_open %.*P
Airship [%{public}s:%d:%{public}s] region id %hu exec stage mismatch %u
Airship [%{public}s:%d:%{public}s] window_base=%#llx, size=%#llx
Airship [%{public}s:%d:%{public}s] (crid %hu) stopping controller
Airship [%{public}s:%d:%{public}s] (crid %hu) cr terminated
Airship [%{public}s:%d:%{public}s] performing health check.
Airship [%{public}s:%d:%{public}s] detaching from device
Airship [%{public}s:%d:%{public}s] starting timer with interval (%u)
Airship [%{public}s:%d:%{public}s] (trid %hu) failed to complete transfer tag %hu
Airship [%{public}s:%d:%{public}s] crid %hu open message result %u
Airship [%{public}s:%d:%{public}s] (bc %s) image address 0x%llx, length 0x%x
Airship [%{public}s:%d:%{public}s] sending open message for context id %hu
Airship [%{public}s:%d:%{public}s] context id %hu close message result %u
Airship [%{public}s:%d:%{public}s] complete
Airship [%{public}s:%d:%{public}s] IPC handshake timer expired
Airship [%{public}s:%d:%{public}s] capture streaming logs
Airship [%{public}s:%d:%{public}s] (trid %hu) predecessor state %u does not valid
Airship [%{public}s:%d:%{public}s] acipc driver activate complete
Airship [%{public}s:%d:%{public}s] located completion ring configuration, adding %u instances
Airship [%{public}s:%d:%{public}s] type=%u, debug meta-data=0x%llx, name=%s
Airship [%{public}s:%d:%{public}s] copying appendix
Airship [%{public}s:%d:%{public}s] context id %hu set as open
Airship [%{public}s:%d:%{public}s] added %u instances of doorbell %s
Airship [%{public}s:%d:%{public}s] creating boot controller for %s
Airship [%{public}s:%d:%{public}s] not in reset
Airship [%{public}s:%d:%{public}s] trid %hu is settled
Airship [%{public}s:%d:%{public}s] failed to set client overrides for %s[%u]
Airship [%{public}s:%d:%{public}s] IPC power state callout enabled
Airship [%{public}s:%d:%{public}s] probing device
Airship [%{public}s:%d:%{public}s] current blockers (%u), blockers cleared (%u)
Airship [%{public}s:%d:%{public}s] (trid %hu) completing transfer tag %hu
Airship [%{public}s:%d:%{public}s] dbs : total %lu, active %lu, pending %d
Airship [%{public}s:%d:%{public}s] registering service
Airship [%{public}s:%d:%{public}s] message canceled
Airship [%{public}s:%d:%{public}s] not ready for peripheral info interrupt
Airship [%{public}s:%d:%{public}s] boot manager entering reset
Airship [%{public}s:%d:%{public}s] pending IPC exec stage broadcast
Airship [%{public}s:%d:%{public}s] (bc %s) computing image table
Airship [%{public}s:%d:%{public}s] image response %u, code %u
Airship [%{public}s:%d:%{public}s] setting trid %hu open
Airship [%{public}s:%d:%{public}s] Registering head index update handler for crid %hu at vector %hu
Airship [%{public}s:%d:%{public}s] result=0x%x
Airship [%{public}s:%d:%{public}s] index %hu, message length %u
Airship [%{public}s:%d:%{public}s] activating %s[%u]
Airship [%{public}s:%d:%{public}s] already in reset
Airship [%{public}s:%d:%{public}s] invoking exec stage change handler: %u
Airship [%{public}s:%d:%{public}s] (trid %hu) invalid in-place completion at idx=%hu
Airship [%{public}s:%d:%{public}s] (crid %hu) applied client overrides
Airship [%{public}s:%d:%{public}s] tr_open %.*P
Airship [%{public}s:%d:%{public}s] value for shared constant doorbell: %u
Airship [%{public}s:%d:%{public}s] region id %hu adding memregion_controller
Airship [%{public}s:%d:%{public}s] no devices to attach to
Airship [%{public}s:%d:%{public}s] opening mtr
Airship [%{public}s:%d:%{public}s] setting trid %hu closed
Airship [%{public}s:%d:%{public}s] (crid %hu) close complete
Airship [%{public}s:%d:%{public}s] boot manager is in reset
Airship [%{public}s:%d:%{public}s] power flags changed to %u
Airship [%{public}s:%d:%{public}s] (trid %hu) transfer at index %hu is in state %u
Airship [%{public}s:%d:%{public}s] (trid %hu) unexpected flush notice from CRID %hu
Airship [%{public}s:%d:%{public}s] num of objects pending deletion %u
Airship [%{public}s:%d:%{public}s] Initializing device
Airship [%{public}s:%d:%{public}s] region id %hu sending memory map message
Airship [%{public}s:%d:%{public}s] (ctxid %hu) controller reset
Airship [%{public}s:%d:%{public}s] (trid %hu) free transfers %hu must exceed dead space size %hu
Airship [%{public}s:%d:%{public}s] device is not active
Airship [%{public}s:%d:%{public}s] failed to flatten name/sel into string
Airship [%{public}s:%d:%{public}s] (ctxid %hu) failed to validate client override
Airship [%{public}s:%d:%{public}s] (trid %hu) first index %hu exceeds size %hu
Airship [%{public}s:%d:%{public}s] no custom statedump handlers registered
Airship [%{public}s:%d:%{public}s] message failure
Airship [%{public}s:%d:%{public}s] requesting close for context id %hu
Airship [%{public}s:%d:%{public}s] trid %hu set as open
Airship [%{public}s:%d:%{public}s] oversize host memory window reduced from %#llx to UINT32_MAX
Airship [%{public}s:%d:%{public}s] current blockers (%u), set blockers (%u)
Airship [%{public}s:%d:%{public}s] trid %hu in limbo
Airship [%{public}s:%d:%{public}s] recomputing closed ring availability
Airship [%{public}s:%d:%{public}s] main ipc state is not running (%u) or transport is not set
Airship [%{public}s:%d:%{public}s] entering device sleep
Airship [%{public}s:%d:%{public}s] stop reason %u
Airship [%{public}s:%d:%{public}s] creating doorbell controller for %s[%u]
Airship [%{public}s:%d:%{public}s] (trid %hu) first transfer not found
Airship [%{public}s:%d:%{public}s] (trid %hu) close complete
Airship [%{public}s:%d:%{public}s] (ctxid %hu) reaping context controller
Airship [%{public}s:%d:%{public}s] capture AirshipDeviceDK state
Airship [%{public}s:%d:%{public}s] destroying completion ring handle for crid %hu
Airship [%{public}s:%d:%{public}s] (crid %hu) registering interrupt and setting up index array signaler vector %hu
Airship [%{public}s:%d:%{public}s] sw timeout scale for proxima protium platform: %llu
Airship [%{public}s:%d:%{public}s] adding %u instances of resource %s
Airship [%{public}s:%d:%{public}s] power state not ready, setting transport blocker
Airship [%{public}s:%d:%{public}s] (trid %hu) tag %hu must belong to first in chain
Airship [%{public}s:%d:%{public}s] (crid %hu) registering with doorbell coordinator with doorbell %s
Airship [%{public}s:%d:%{public}s] failed to allocate/map device memory
Airship [%{public}s:%d:%{public}s] coordinator state=%u, new IPC stage=%s
Airship [%{public}s:%d:%{public}s] message success, setting state for region id %hu
Airship [%{public}s:%d:%{public}s] (bc %s) no image response code
Airship [%{public}s:%d:%{public}s] setting up message rings
Airship [%{public}s:%d:%{public}s] failed to look up configuration for %s
Airship [%{public}s:%d:%{public}s] copying peripheral info, initial exec stage value=%u
Airship [%{public}s:%d:%{public}s] not ready for ipc status interrupt
Airship [%{public}s:%d:%{public}s] (trid %hu) transfer tag %hu does not match next in-order tag %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) new device ring status=%u
Airship [%{public}s:%d:%{public}s] (trid %hu) state=%u, activated=%u
Airship [%{public}s:%d:%{public}s] (ctxid %hu) close complete
Airship [%{public}s:%d:%{public}s] (trid %hu) transfer flush failed
Airship [%{public}s:%d:%{public}s] unexpected GUARD_ELSE failure
Airship [%{public}s:%d:%{public}s] value %u matches to exec stage: %s
Airship [%{public}s:%d:%{public}s] removed crid %hu
Airship [%{public}s:%d:%{public}s] removing boot controller for ipc stage %s
Airship [%{public}s:%d:%{public}s] creating new ring pool for transfer ring %s
Airship [%{public}s:%d:%{public}s] copying message payload
Airship [%{public}s:%d:%{public}s] added crid %hu
Airship [%{public}s:%d:%{public}s] suspending transport
Airship [%{public}s:%d:%{public}s] creating device memory
Airship [%{public}s:%d:%{public}s] (ctxid %hu) sending close message
Airship [%{public}s:%d:%{public}s] (trid %hu) registering interrupt and setting up index array signaler vector %hu
Airship [%{public}s:%d:%{public}s] adding crid %hu flush tracking for trid %hu
Airship [%{public}s:%d:%{public}s] creating context controller for %s[%u]
Airship [%{public}s:%d:%{public}s] ipc status=%u
Airship [%{public}s:%d:%{public}s] (crid %hu) failed to complete transfer
Airship [%{public}s:%d:%{public}s] setting crid %hu open
Airship [%{public}s:%d:%{public}s] invalid params
Airship [%{public}s:%d:%{public}s] sending close message for crid %hu
Airship [%{public}s:%d:%{public}s] notifying crid %hu that trid %hu is settled
Airship [%{public}s:%d:%{public}s] main ipc stage name %s
Airship [%{public}s:%d:%{public}s] ipc status invalid
Airship [%{public}s:%d:%{public}s] sleep status: active
Airship [%{public}s:%d:%{public}s] failed to aquire resource for %s[%u]
Airship [%{public}s:%d:%{public}s] (trid %hu) failed to find first transfer
Airship [%{public}s:%d:%{public}s] opening mcr
Airship [%{public}s:%d:%{public}s] updated exec stage: %u, current %u
Airship [%{public}s:%d:%{public}s] (crid %hu) sending open message
Airship [%{public}s:%d:%{public}s] tearing down mtr
Airship [%{public}s:%d:%{public}s] reserving ring with selector %u
Airship [%{public}s:%d:%{public}s] (bc %s) reseting boot controller
Airship [%{public}s:%d:%{public}s] (bc %s) image_state=%u
Airship [%{public}s:%d:%{public}s] updating context close requests
Airship [%{public}s:%d:%{public}s] exec_stage during power-on=%u
Airship [%{public}s:%d:%{public}s] wake requested=%u, target host sleep=%u, permit device sleep=%u
Airship [%{public}s:%d:%{public}s] (trid %hu) predecessor completion ID %hu does not equal completion ID %hu
Airship [%{public}s:%d:%{public}s] Enable BusLead and Memory
Airship [%{public}s:%d:%{public}s] unknown device viddid=%#x
Airship [%{public}s:%d:%{public}s] (trid %hu) TR is now settled
Airship [%{public}s:%d:%{public}s] (crid %hu) new interrupt %s[%u]
Airship [%{public}s:%d:%{public}s] tearing down boot ipc stage
Airship [%{public}s:%d:%{public}s] main ipc state is not set
Airship [%{public}s:%d:%{public}s] failed to aquire resource for %s
Airship [%{public}s:%d:%{public}s] power state change deadline expired
Airship [%{public}s:%d:%{public}s] (trid %hu) do not overwrite existing bad tx completion buffer
Airship [%{public}s:%d:%{public}s] saving overflow message
Airship [%{public}s:%d:%{public}s] entering host sleep
Airship [%{public}s:%d:%{public}s] image sent for ipc stage %s
Airship [%{public}s:%d:%{public}s] region id %hu deferring unmap message
Airship [%{public}s:%d:%{public}s] attaching pending device to driver
Airship [%{public}s:%d:%{public}s] (trid %hu) controller closed
Airship [%{public}s:%d:%{public}s] context_open %.*P
Airship [%{public}s:%d:%{public}s] activating doorbell coordinator with %u doorbell instances
Airship [%{public}s:%d:%{public}s] driver name: %s
Airship [%{public}s:%d:%{public}s] (trid %hu) completing chain
Airship [%{public}s:%d:%{public}s] no ipc stage set
Airship [%{public}s:%d:%{public}s] sending any overflow messages
Airship [%{public}s:%d:%{public}s] context id %hu has unmessaged lifecycle, setting closed
Airship [%{public}s:%d:%{public}s] (trid %hu) open failed 0x%x
Airship [%{public}s:%d:%{public}s] creating mtr
Airship [%{public}s:%d:%{public}s] trigger superdispatch for SetPowerState
Airship [%{public}s:%d:%{public}s] trid %hu has unmessaged lifecycle, closing
Airship [%{public}s:%d:%{public}s] ipc handshake complete
Airship [%{public}s:%d:%{public}s] setting client overrides for %s[%u]
Airship [%{public}s:%d:%{public}s] getting device criteria
Airship [%{public}s:%d:%{public}s] automatically placing driver in reset
Airship [%{public}s:%d:%{public}s] (trid %hu) failed to validate client override
Airship [%{public}s:%d:%{public}s] resuming doorbell coordinator
Airship [%{public}s:%d:%{public}s] %s[%u] stopped
Airship [%{public}s:%d:%{public}s] consuming transfers
Airship [%{public}s:%d:%{public}s] tearing down main ipc stage
Airship [%{public}s:%d:%{public}s] updating context info address register
Airship [%{public}s:%d:%{public}s] (trid %hu) offset %hu exceeds fetched transfer count %hu
Airship [%{public}s:%d:%{public}s] driver added successfully
Airship [%{public}s:%d:%{public}s] stopping trid %hu for reason %u
Airship [%{public}s:%d:%{public}s] creating memregion controller for %s[%u]
Airship [%{public}s:%d:%{public}s] removed context id %hu
Airship [%{public}s:%d:%{public}s] provider 0x%llx\n
Airship [%{public}s:%d:%{public}s] no exec stage found for value %u
Airship [%{public}s:%d:%{public}s] Registering tail index update handler for trid %hu at vector %hu
Airship [%{public}s:%d:%{public}s] creating handle for transfer ring with trid %u
Airship [%{public}s:%d:%{public}s] (bc %s) out code=%u
Airship [%{public}s:%d:%{public}s] context id %hu status %u
Airship [%{public}s:%d:%{public}s] viddid=%#x
Airship [%{public}s:%d:%{public}s] setting boot controller for ipc stage %s to unavailable
Airship [%{public}s:%d:%{public}s] boot manager exiting reset
Airship [%{public}s:%d:%{public}s] crid: %u
Airship [%{public}s:%d:%{public}s] (crid %hu) controller reset
Airship [%{public}s:%d:%{public}s] Airship error description: %s
Airship [%{public}s:%d:%{public}s] (crid %hu) reaping cr
Airship [%{public}s:%d:%{public}s] starting device
Airship [%{public}s:%d:%{public}s] removed trid %hu
Airship [%{public}s:%d:%{public}s] IPC driver state dump size %u
Airship [%{public}s:%d:%{public}s] (trid %hu) sending close message
Airship [%{public}s:%d:%{public}s] handle_activate: result 0x%x
Airship [%{public}s:%d:%{public}s] DART page size 0x%llx, memory map: base 0x%llx, size 0x%llx)
Airship [%{public}s:%d:%{public}s] (bc %s) stopping boot controller
Airship [%{public}s:%d:%{public}s] controller ipc stage: %s
Airship [%{public}s:%d:%{public}s] reaping %s[%u]
Airship [%{public}s:%d:%{public}s] crid %hu status %u
Airship [%{public}s:%d:%{public}s] updating register at bank=%u, offset=%u
Airship [%{public}s:%d:%{public}s] Deregistering tail index update handler for trid %hu at vector %hu
Airship [%{public}s:%d:%{public}s] device power off deadline expired
Airship [%{public}s:%d:%{public}s] activate
Airship [%{public}s:%d:%{public}s] starting messenger
Airship [%{public}s:%d:%{public}s] creating handle for completion ring with crid %u
Airship [%{public}s:%d:%{public}s] completion count %hu
Airship [%{public}s:%d:%{public}s] region %s (id=%hu) cannot be used due to name conflict with id %hu
Airship [%{public}s:%d:%{public}s] (ctxid %hu) applied client overrides
Airship [%{public}s:%d:%{public}s] clearing transport
Airship [%{public}s:%d:%{public}s] updated error state: %u, current %u
Airship [%{public}s:%d:%{public}s] (crid %hu) controller closed
Airship [%{public}s:%d:%{public}s] sending open message for trid %hu
Airship [%{public}s:%d:%{public}s] not ready for exec stage interrupt
Airship [%{public}s:%d:%{public}s] power flags (%u), current IPC power state (%u)
Airship [%{public}s:%d:%{public}s] creating new ring pool for completion ring %s
Airship [%{public}s:%d:%{public}s] (trid %hu) transfer enqueue size %u exceeds maximum transfer size %u
Airship [%{public}s:%d:%{public}s] driver create client end %s
Airship [%{public}s:%d:%{public}s] device attach deadline expired
Airship [%{public}s:%d:%{public}s] (trid %hu) invalid ti: %hu
Airship [%{public}s:%d:%{public}s] setting up mcr
Airship [%{public}s:%d:%{public}s] begin power change; power flags %u
Airship [%{public}s:%d:%{public}s] syncing mcr head index update
Airship [%{public}s:%d:%{public}s] setting up peripheral info interrupt
Airship [%{public}s:%d:%{public}s] device service does not match criteria
Airship [%{public}s:%d:%{public}s] invalid configuration: %s at %s
Airship [%{public}s:%d:%{public}s] cannot set transport, %s ipc stage is not null
Airship [%{public}s:%d:%{public}s] not ready to probe exec stage register
Airship [%{public}s:%d:%{public}s] creating dispatch queue
Airship [%{public}s:%d:%{public}s] clearing in reset transport blocker
Airship [%{public}s:%d:%{public}s] (bc %s) detail=%u
Airship [%{public}s:%d:%{public}s] (bc %s) image valid : %s 
Airship [%{public}s:%d:%{public}s] (crid %hu) sending close message
Airship [%{public}s:%d:%{public}s] (crid %hu) new device ring status=%u
Airship [%{public}s:%d:%{public}s] reset type=%u
Airship [%{public}s:%d:%{public}s] pending IPC error broadcast
Airship [%{public}s:%d:%{public}s] reserve %u complete
Airship [%{public}s:%d:%{public}s] object manager list not empty; dumping direct client objects
Airship [%{public}s:%d:%{public}s] (crid %hu) new doorbell interval (%u us), new leeway (%u us)
Airship [%{public}s:%d:%{public}s] device : active %u, registered %u, power init complete %u
Airship [%{public}s:%d:%{public}s] (trid %hu) new doorbell interval (%u us), new leeway (%u us)
Airship [%{public}s:%d:%{public}s] unblocking device access
Airship [%{public}s:%d:%{public}s] (trid %hu) controller reset
Airship [%{public}s:%d:%{public}s] sleep status: %s
Airship [%{public}s:%d:%{public}s] Airship: device attach deadline %u ms, starting timer
Airship [%{public}s:%d:%{public}s] (crid %hu) invalid completion descriptor at idx=%hu
Airship [%{public}s:%d:%{public}s] participant 0x%llx added to doorbell %s[%u]
Airship [%{public}s:%d:%{public}s] ipc stage not torn down, boot stage valid: %u, main stage valid: %u
Airship [%{public}s:%d:%{public}s] (trid %hu) moving queued transfers into pending state
Airship [%{public}s:%d:%{public}s] closing mtr
Airship [%{public}s:%d:%{public}s] adding boot controller for ipc stage %s
Airship [%{public}s:%d:%{public}s] image has already been sent
Airship [%{public}s:%d:%{public}s] starting ipc handshake timer; timeout=%u ms
Airship [%{public}s:%d:%{public}s] region id %hu removing memregion_controller
Airship [%{public}s:%d:%{public}s] (bc %s) old state=0x%llx, new state=0x%llx
Airship [%{public}s:%d:%{public}s] stopping crid %hu
Airship [%{public}s:%d:%{public}s] crid %hu has unmessaged lifecycle, setting closed
Airship [%{public}s:%d:%{public}s] failed to get device memory window config
Airship [%{public}s:%d:%{public}s] creating airship driver handle
Airship [%{public}s:%d:%{public}s] (trid %hu) create tx_queue: size %hu, hdrlen %u, ftrlen %u, out-of-order %u
Airship [%{public}s:%d:%{public}s] msi stats overflow: resetting count for vector %u
Airship [%{public}s:%d:%{public}s] payload length %u, appendix length %u
Airship [%{public}s:%d:%{public}s] context id %hu close message requested
Airship [%{public}s:%d:%{public}s] ts: last_write %llx, schedule %llx, deadline %llx, 
Airship [%{public}s:%d:%{public}s] entering reset
Airship [%{public}s:%d:%{public}s] loading device configuration
Airship [%{public}s:%d:%{public}s] insufficient buffer
Airship [%{public}s:%d:%{public}s] (crid %hu) new availability blockers 0x%08x
Airship [%{public}s:%d:%{public}s] requesting close for crid %hu
Airship [%{public}s:%d:%{public}s] initializing PCI device
Airship [%{public}s:%d:%{public}s] %s[%u] state %u, detail 0x%u
Airship [%{public}s:%d:%{public}s] canceling power off deadline timer
Airship [%{public}s:%d:%{public}s] canceling timer
Airship [%{public}s:%d:%{public}s] adding interrupt source %u
Airship [%{public}s:%d:%{public}s] syncing mtr tail index update and fetching completions
Airship [%{public}s:%d:%{public}s] trid %hu status %u
Airship [%{public}s:%d:%{public}s] Added context id %hu
Airship [%{public}s:%d:%{public}s] reset type: %s
Airship [%{public}s:%d:%{public}s] cannot wake
Airship [%{public}s:%d:%{public}s] getting auto-exit reset
Airship [%{public}s:%d:%{public}s] located transfer ring configuration, adding %u instances
Airship [%{public}s:%d:%{public}s] trid %hu open message result %u
Airship [%{public}s:%d:%{public}s] unknown proxima-platform: %llu
Airship [%{public}s:%d:%{public}s] Airship statedump complete: provided buffer size %u copied %u
Airship [%{public}s:%d:%{public}s] (crid %hu) invalid hi: %hu
Airship [%{public}s:%d:%{public}s] (crid %hu) do not overwrite existing bad_cd buffer
Airship [%{public}s:%d:%{public}s] sending close message for trid %hu
Airship [%{public}s:%d:%{public}s] (bc %s) image sent, recomputing state
Airship [%{public}s:%d:%{public}s] reset type %u
Airship [%{public}s:%d:%{public}s] ring manager is in reset
Airship [%{public}s:%d:%{public}s] (ctxid %hu) stopping controller
Airship [%{public}s:%d:%{public}s] (bc %s) checking for image response
Airship [%{public}s:%d:%{public}s] stopping context id %hu for reason %u
Airship [%{public}s:%d:%{public}s] suspending doorbell coordinator
Airship [%{public}s:%d:%{public}s] sending close message for context id %hu
Airship [%{public}s:%d:%{public}s] crid %hu is associated with trid %hu
Airship [%{public}s:%d:%{public}s] sending open message for crid %hu
Airship [%{public}s:%d:%{public}s] releasing ring with selector %u
Airship [%{public}s:%d:%{public}s] airship sw scaling %llu
Airship [%{public}s:%d:%{public}s] index %hu
Airship [%{public}s:%d:%{public}s] context id %hu has unmessaged lifecycle, closing
Airship [%{public}s:%d:%{public}s] entering reset, dropping any pending doorbells
Airship [%{public}s:%d:%{public}s] (trid %hu) index %hu exceeds size %hu
Airship [%{public}s:%d:%{public}s] closing context id %hu
Airship [%{public}s:%d:%{public}s] setting context id %hu open
Airship [%{public}s:%d:%{public}s] current main ipc stage and transport must be set
Airship [%{public}s:%d:%{public}s] removing interrupt source %u
Airship [%{public}s:%d:%{public}s] crid %hu is not associated with any open trs
Airship [%{public}s:%d:%{public}s] region id %hu conflict %u
Airship [%{public}s:%d:%{public}s] currentPower %u, pendingPower %u, device valid %s
Airship [%{public}s:%d:%{public}s] closing trid %hu
Airship [%{public}s:%d:%{public}s] exiting reset
Airship [%{public}s:%d:%{public}s] new ipc stage: %s
Airship [%{public}s:%d:%{public}s] marking driver state as running; trigger IPC driver exit_reset
Airship [%{public}s:%d:%{public}s] resourceFileName=%s
Airship [%{public}s:%d:%{public}s] crid %hu has unmessaged lifecycle, closing
Airship [%{public}s:%d:%{public}s] creating cr controller for %s[%u]
Airship [%{public}s:%d:%{public}s] synthesizing completions if needed
Airship [%{public}s:%d:%{public}s] setting crid %hu closed
Airship [%{public}s:%d:%{public}s] failed to find stage for value, %u
Airship [%{public}s:%d:%{public}s] message failed, setting state for region id %hu
Airship [%{public}s:%d:%{public}s] getting driver name
Airship [%{public}s:%d:%{public}s] clearing power state not ready blocker
Airship [%{public}s:%d:%{public}s] processing completions
Airship [%{public}s:%d:%{public}s] derivedStart successful\n
Airship [%{public}s:%d:%{public}s] unmapping memory region for %s[%u]
Airship [%{public}s:%d:%{public}s] kIOServiceNotificationTypeTerminated
Airship %s %s@%u
Airship [%{public}s:%d:%{public}s] driver create client begin %s
Airship [%{public}s:%d:%{public}s] context id %hu has unmessaged lifecycle, setting open
Airship [%{public}s:%d:%{public}s] associating crid %hu <-> trid %hu
Airship [%{public}s:%d:%{public}s] setting context id %hu closed
Airship [%{public}s:%d:%{public}s] %s[%u] unavailable
Airship [%{public}s:%d:%{public}s] map successful
Airship [%{public}s:%d:%{public}s] running power state change wait context
Airship [%{public}s:%d:%{public}s] new ipc status=%u
Airship [%{public}s:%d:%{public}s] invalid device
Airship [%{public}s:%d:%{public}s] (crid %hu) open failed 0x%x
Airship [%{public}s:%d:%{public}s] (trid %hu) new mode (%u)
Airship [%{public}s:%d:%{public}s] boot manager is already in reset
Airship [%{public}s:%d:%{public}s] getting device class
Airship [%{public}s:%d:%{public}s] set transport result 0x%x
Airship [%{public}s:%d:%{public}s] running power state changed wait context
Airship [%{public}s:%d:%{public}s] debugInfo capture complete, size %u
Airship [%{public}s:%d:%{public}s] creating mcr
Airship [%{public}s:%d:%{public}s] setting up message buffer for main ipc stage %s
Airship [%{public}s:%d:%{public}s] ring manager already in reset
Airship [%{public}s:%d:%{public}s] requesting close for trid %hu
Airship [%{public}s:%d:%{public}s] crid %hu has unmessaged lifecycle, setting open
Airship [%{public}s:%d:%{public}s] stopping crid %hu for reason %u
Airship [%{public}s:%d:%{public}s] updating cr close requests
Airship [%{public}s:%d:%{public}s] removing participant 0x%llx from pending queue
Airship [%{public}s:%d:%{public}s] region id %hu sending unmap message
Airship [%{public}s:%d:%{public}s] window base: 0x%llx, window size: 0x%llx
Airship [%{public}s:%d:%{public}s] closing crid %hu
Airship [%{public}s:%d:%{public}s] timer deadline missed!!
Airship [%{public}s:%d:%{public}s] created completion mirror object
Airship [%{public}s:%d:%{public}s] exec stage interrupt occurred: value %u
Airship [%{public}s:%d:%{public}s] failed to look up configuration for %s[%u]
Airship [%{public}s:%d:%{public}s] enqueuing message in mtr
Airship [%{public}s:%d:%{public}s] ACIPC protocol error 0x%08x (%s)
Airship [%{public}s:%d:%{public}s] (crid %hu) update bad cd
Airship [%{public}s:%d:%{public}s] sending message now
Airship [%{public}s:%d:%{public}s] trid %hu close message result %u
Airship [%{public}s:%d:%{public}s] new item at index %hu
Airship [%{public}s:%d:%{public}s] kIOServiceNotificationTypeMatched
Airship [%{public}s:%d:%{public}s] (ctxid %hu) controller state=%u, detail=%u
Airship [%{public}s:%d:%{public}s] stopping provider
Airship [%{public}s:%d:%{public}s] setting external interrupt handler for vector %u
Airship [%{public}s:%d:%{public}s] setting up main ipc stage
Airship [%{public}s:%d:%{public}s] stopping boot controller for ipc stage %s
Airship [%{public}s:%d:%{public}s] tearing down mcr
Airship [%{public}s:%d:%{public}s] deferring message send
Airship [%{public}s:%d:%{public}s] platform_config=%u, probed viddid=0x%#x,  proxima_viddid=0x%#x
Airship [%{public}s:%d:%{public}s] boot manager is already out of reset
Airship [%{public}s:%d:%{public}s] (trid %hu) stopping controller
Airship [%{public}s:%d:%{public}s] in_reset %u, activated %u
Airship [%{public}s:%d:%{public}s] stopping context id %hu
Airship [%{public}s:%d:%{public}s] failed to get resource
Airship [%{public}s:%d:%{public}s] setting up callout notifier
Airship [%{public}s:%d:%{public}s] no handles available in pool
Airship [%{public}s:%d:%{public}s] invoking action
Airship [%{public}s:%d:%{public}s] sending overflow messages
Airship [%{public}s:%d:%{public}s] crid %hu in limbo
Airship [%{public}s:%u:%{public}s] unexpected nonzero error code 0x%llx
Airship [%{public}s:%d:%{public}s] acquiring resource %s
Airship [%{public}s:%d:%{public}s] (bc %s) adding controller to boot manager
Airship [%{public}s:%d:%{public}s] (bc %s) sending image
Airship [%{public}s:%d:%{public}s] %s[%u] old status %u, new status %u
Airship [%{public}s:%d:%{public}s] context id %hu in limbo
Airship [%{public}s:%d:%{public}s] (trid %hu) completions synthesized
Airship [%{public}s:%d:%{public}s] message success
Airship [%{public}s:%d:%{public}s] added trid %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) new interrupt %s[%u]
Airship [%{public}s:%d:%{public}s] creating tr controller for %s[%u]
Airship [%{public}s:%d:%{public}s] (trid %hu) registering doorbell %s, selector %u
Airship [%{public}s:%d:%{public}s] (crid %hu) trid %hu does not accept completions from this cr
Airship [%{public}s:%d:%{public}s] (crid %hu) inserting completion with trid %hu and first tag %hu
Airship [%{public}s:%d:%{public}s] trid: %u, state %u
Airship [%{public}s:%d:%{public}s] exiting host sleep
Airship [%{public}s:%d:%{public}s] initializing driver
Airship [%{public}s:%d:%{public}s] reset=%u, boot_state=%s, ipc_state=%s
Airship [%{public}s:%d:%{public}s] (ctxid %hu) new availability blockers 0x%08x
Airship [%{public}s:%d:%{public}s] (trid %hu) new availability blockers 0x%08x
Airship [%{public}s:%d:%{public}s] messenger already out of reset
Airship [%{public}s:%d:%{public}s] mapping region of size %u for %s[%u]
Airship [%{public}s:%d:%{public}s] (trid %hu) free=%hu, queued=%hu, pending=%hu, completed=%hu, fetched=%hu
Airship [%{public}s:%d:%{public}s] (bc %s) image response code=%u
```
