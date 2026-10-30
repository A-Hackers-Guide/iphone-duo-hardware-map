# `/System/DriverKit/System/Library/PrivateFrameworks/AirshipDK.framework/AirshipDK`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,063,248 bytes.

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
[%s:%d:%s] power flags (%u), current IPC power state (%u)
shortcomp_complete_subsequent_transfers
[%s:%d:%s] crid: %u
BUG in Airship: unaligned device memory access @%s:%u
classify_image_response_code
get_size
[%s:%d:%s] main ipc state is not set
[%s:%d:%s] region %s (id=%hu) cannot be used due to name conflict with id %hu
direct_buffer.cpp
clear_context
[%s:%d:%s] starting device
send_tr_open_message
errata
get_entry_at_index
BUG in client of Airship: attempted to register handler for inactive driver
doorbell_timer_tolerance_us
image_table
completion_rings
[%s:%d:%s] adding interrupt source %u
[%s:%d:%s] tr_open 
[%s:%d:%s] failed to aquire resource for %s
[%s:%d:%s] invoking exec stage change handler: %u
BUG in Airship: unexpected flush notice @%s:%u
[%s:%d:%s] (trid %hu) registering doorbell %s, selector %u
append_debug_stats
round_up_to_page_size
update_completion_desc_debug_info
direct_tr_controller.cpp
completion_groups
BUG in Airship: wrong index @%s:%u
getGlobalQueue_block_invoke
BUG in Airship: attempted to access terminated driver
set_exec_stage
get_flattened_name_sel_string
ring_index_pair
transfer_header_size
Airship IPC power on timed out
[%s:%d:%s] power state change deadline expired
transfer_queue
 %02x
copy_and_zerofill
async_callback
handle_mem_write8
[%s:%d:%s] (crid %hu) new availability blockers 0x%08x
[%s:%d:%s] suspending doorbell coordinator
handle_get_nominal_state_dump_size
airship-trap-on-ipc-power-on-timeout
[%s:%d:%s] initializing driver
get_page_size
ALLOCATION FAILURE (or BUG) in Airship
airship_platform_get_sleep_queue_block_invoke
[%s:%d:%s] reset=%u, boot_state=%s, ipc_state=%s
BUG in client of Airship: attempted to activate canceled interrupt
id
[%s:%d:%s] (ctxid %hu) close complete
clearTransportBlocker
device_power_off_timeout_ms
[%s:%d:%s] no devices to attach to
resources
acipc_get_health_status
AirshipDeviceClass
[%s:%d:%s] current blockers (%u), blockers cleared (%u)
[%s:%d:%s] pending IPC error broadcast
clear_transport
isPoweringOff
completion_mirror.cpp
[%s:%d:%s] not ready for ipc status interrupt
register overlap
in_place
%zu
[%s:%d:%s] failed to aquire resource for %s[%u]
com.apple.AirshipDriverDK.service-default
[%s:%d:%s] closing context id %hu
BUG in client of Airship: attempted to reconfigure active memregion @%s:%u
BUG in Airship: invalid tail index advance operation
[%s:%d:%s] exec stage interrupt occurred: value %u
[%s:%d:%s] msi stats overflow: resetting count for vector %u
[%s:%d:%s] in_reset %u, activated %u
device_transport.hpp
populate_state_dump_info
[%s:%d:%s] registering service
[%s:%d:%s] sw timeout scale for proxima protium platform: %llu
BUG in Airship: refcount_mixin retained after release @%s:%u
AirshipDevice attach timeout
BUG in client of Airship: Failed to locate completion ring config @%s:%u
[%s:%d:%s] (trid %hu) moving queued transfers into pending state
~ring_manager
add_tr
stop_tr
airship-sw-timeout-scale
device-signalled error
out-of-place completion requires completion ring
[%s:%d:%s] region id %hu exec stage mismatch %u
tr_controller
[%s:%d:%s] context id %hu has unmessaged lifecycle, setting open
airship-read-before-sleep-update
[%s:%d:%s] acipc driver activate complete
[%s:%d:%s] no exec stage found for value %u
send_memory_map_message
driver_client.cpp
airship-unknown-errors
~intrusive_list_link
AirshipDeviceDK.cpp
active
direct_monitor.cpp
value out of bounds
constraints
open_context
BUG in Airship: bad optional access
mutex.hpp
[%s:%d:%s] (bc %s) no image response code
direct_memregion.cpp
suspend
BUG in Airship: ring size cannot be zero
BUG in client of Airship: Cannot destroy handle before ring has been closed. @%s:%u
BUG in Airship: invalid head index advance operation
interrupts
disable_interrupt_vector
BUG in Airship: attempted to insert element at position not in list
copy_descriptor
add
dump_list
finalize_indices
[%s:%d:%s] index %hu, message length %u
send_cr_open_message
[%s:%d:%s] trid %hu has unmessaged lifecycle, setting open
[%s:%d:%s] setting trid %hu open
dequeue_batch
parse_number
clear_cr_indices
enable_interrupt_vector
~direct_client_object
[%s:%d:%s] updating cr close requests
copy_debug_info
OSAction_AirshipDriverDK_ServiceNotificationReady
BUG in Airship: ring size cannot be zero @%s:%u
[%s:%d:%s] trid: %u, state %u
set_error
[%s:%d:%s] located transfer ring configuration, adding %u instances
[%s:%d:%s] tearing down mcr
[%s:%d:%s] crid %hu is not associated with any open trs
set_mode
unknown
ipc_status_interrupt
[%s:%d:%s] result=0x%x
Airship device power on timed out
probe_image_response
[%s:%d:%s] device : active %u, registered %u, power init complete %u
[%s:%d:%s] removed trid %hu
BUG in client of Airship: attempted to reconfigure active TR
update_ipc_control_register
count_where
AirshipDriverDK.cpp
BUG in Airship: attempted to use inactive object @%s:%u
recomputePowerRequest
bad-cd
retrieveDriverStateDumpInfo
[%s:%d:%s] (trid %hu) open failed 0x%x
handle_get_mem_window_info
process_completion_descriptors
flush_tr_settlement
mutex
update_mem_window_base_and_size
[%s:%d:%s] object manager list not empty; dumping direct client objects
[%s:%d:%s] pending IPC exec stage broadcast
[%s:%d:%s] (trid %hu) tag %hu must belong to first in chain
set_completion_group
check_all_cr_close_requests
[%s:%d:%s] added trid %hu
BUG in client of Airship: attempted to access inactive TR @%s:%u
[%s:%d:%s] (trid %hu) new mode (%u)
BUG in Airship: attempted to access boxed dictionary with null key @%s:%u
release_image_transfer_resources
enqueue_message_in_mtr
main
[%s:%d:%s] context id %hu status %u
[%s:%d:%s] setting trid %hu closed
max
compute_io_status_for_transfers
flush_with_action
[%s:%d:%s] (trid %hu) invalid ti: %hu
read_register
check_all_context_close_requests
BUG in Airship: attempted to insert element already in list
cr_ring
[%s:%d:%s] copying peripheral info, initial exec stage value=%u
BUG in client of Airship: out of bounds access to buffer @%s:%u
cancelTimer
[%s:%d:%s] Airship error description: %s
BUG in client of Airship: attempted to register handler for inactive driver @%s:%u
create
[%s:%d:%s] context id %hu set as open
[%s:%d:%s] (trid %hu) new interrupt %s[%u]
BUG in client of Airship: mode must be AIRSHIP_ACIPC_TR_MODE_STANDARD
[%s:%d:%s] unblocking device access
create_handle
BUG in Airship: attempted to access terminated driver @%s:%u
[%s:%d:%s] driver added successfully
is_ipc_status_valid
width
window_base_mask
parse_array_or_singleton
request_region_unmap
BUG in Airship: invalid src @%s:%u
probe_exec_stage
close_cr
t2026-CentauriAlpha_AlphaPrimeFPGA
reserve
[%s:%d:%s] (bc %s) adding controller to boot manager
update_sleep_control_register
tr_index_count
[%s:%d:%s] failed to get resource
queues
BUG in client of Airship: attempted to access inactive driver @%s:%u
[%s:%d:%s] invoking action
built-in
[%s:%d:%s] unknown proxima-platform: %llu
[%s:%d:%s] reset type: %s
BUG in Airship: oversize ring
[%s:%d:%s] (trid %hu) registering interrupt and setting up index array signaler vector %hu
BUG in client of Airship: attempted to set interrupt execution queue for terminated driver
remove_participant
teardown_current_ipc_stage
unknown target
[%s:%d:%s] region id %hu conflict %u
acipc_types.cpp
[%s:%d:%s] (trid %hu) offset %hu exceeds fetched transfer count %hu
handle_mem_write16
request_context_close
get_source_maintenance_in_progress
read_tail_index
create_state_monitor
[%s:%d:%s] sending close message for trid %hu
[%s:%d:%s] setting context id %hu open
with_capacity
driver_ioservice_params
BUG in Airship: access to null buffer @%s:%u
[%s:%d:%s] activate
cr_controller.cpp
Airship IPC power off timed out @%s:%u
local
[%s:%d:%s] type=%u, debug meta-data=0x%llx, name=%s
BUG in Airship: attempted to activate object without required configuration
set_capacity
[%s:%d:%s] setting crid %hu closed
[%s:%d:%s] trid %hu set as open
min
bounds overflow
set_device_context_status
[%s:%d:%s] (ctxid %hu) controller reset
release
BUG in client of Airship: attempted to reconfigure active CR
downlink-buffer-count-len-error
[%s:%d:%s] (crid %hu) controller reset
remove_controller
airship-trap-on-device-power-on-timeout
handlePendingDevicePowerOffIfNeeded
get_queue
append_outstanding_transfer_state
advance_tail_index
bad key
flush_DROPS_LOCK
complete_transfer
~interrupt_manager
timedwait
BUG in client of Airship: attempted to activate interrupt with event handlers but without queue @%s:%u
CentauriHelperBootUserClient
false
consume_elements
[%s:%d:%s] sleep status: active
create_sync_monitor
stop_cr
missing object
~devmem_mapping_manager
arm_tr_index_vector
trigger
length
BUG in client of Airship: Invalid mode: AIRSHIP_ACIPC_TR_MODE_STANDARD (method not accessible) @%s:%u
BUG in Airship: attempted to create boxed symbol from null C string @%s:%u
[%s:%d:%s] reset type=%u
wait_context.cpp
BUG in client of Airship: nonzero selector for NULL resource @%s:%u
BUG in Airship: index out of range
[%s:%d:%s] activating %s[%u]
[%s:%d:%s] removing interrupt source %u
BUG in Airship: invalid head index update operation
???
existing_for_str
[%s:%d:%s] running power state change wait context
add_handler
BUG in client of Airship: attempted to register handler for terminated driver
IOPCIDeviceMemoryMapSize
open_cr
BUG in Airship: refcount_mixin retained after release
BUG in Airship: access to non-held resource
[%s:%d:%s] not ready to probe exec stage register
BUG in Airship: invalid tail index update operation
BUG in client of Airship: attempted to access inactive CR
sleep-failure
send_tr_close_message
update_debug_client_overrides
~devmem_mapping
getGlobalQueue
destroy_handle
driverkit_maintenance_block_invoke
ipc_reset_occurred
[%s:%d:%s] deleted %hu items from mirror
BUG in Airship: bad parameter - 'memory'
BUG in Airship: oversize ring @%s:%u
[%s:%d:%s] (trid %hu) controller closed
BUG in client of Airship: mode must be AIRSHIP_ACIPC_TR_MODE_BATCH @%s:%u
BUG in client of Airship: Invalid mode: AIRSHIP_ACIPC_TR_MODE_STANDARD (method not accessible)
reliable
[%s:%d:%s] image sent for ipc stage %s
role
mem_write32
[%s:%d:%s] recomputing closed ring availability
device_memory.cpp
register
[%s:%d:%s] region id %hu sending memory map message
BUG in Airship: bad parameter - 'header_length' @%s:%u
airship-poweron-timeout-waiting-for-pci-device
[%s:%d:%s] Airship: device attach deadline %u ms, starting timer
B16@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8
[%s:%d:%s] unknown device viddid=%#x
add_controller
append_tr_index_info
create_exec_stage_monitor
reap
update_interrupt_debug_state
BUG in client of Airship: attempted to retrieve first completed tag of ring without completed transfers
read
[%s:%d:%s] (trid %hu) first transfer not found
check_async
%s %s@%u
[%s:%d:%s] creating handle for transfer ring with trid %u
get_maintenance_in_progress
direct_client_object.cpp
handle_create_memory_mapping
init
BUG in Airship: attempted truncate to larger size
BUG in Airship: index out of range @%s:%u
[%s:%d:%s] probing exec stage register
parse_optional
[%s:%d:%s] IPC power state callout enabled
find_completion_target
BUG in client of Airship: attempted to set interrupt execution queue for terminated driver @%s:%u
BUG in Airship: attempted to use inactive object
[%s:%d:%s] (bc %s) detail=%u
BUG in client of Airship: attempted to reconfigure active monitor
accumulation
[%s:%d:%s] (trid %hu) failed to complete transfer tag %hu
[%s:%d:%s] message canceled
[%s:%d:%s] removed crid %hu
[%s:%d:%s] sending open message for crid %hu
[%s:%d:%s] setting up main ipc stage
devicePowerStateChanged
[%s:%d:%s] getting device criteria
BUG in Airship: attempted to activate object without required configuration @%s:%u
[%s:%d:%s] boot ipc stage name %s
interrupt_moderation
Airship device power off timed out @%s:%u
BUG in client of Airship: selector is invalid
Airship timer watchdog expired: expected at 0x%llx (currently 0x%llx)
~direct_cr_controller
BUG in client of Airship: attempted to reconfigure active driver
mem_read
BUG in client of Airship: mode must be AIRSHIP_ACIPC_TR_MODE_BATCH
Centauri
CentauriBeta
[%s:%d:%s] %s[%u] state %u, detail 0x%u
set_footer_size
handle_is_memory_mapping_active
BUG in client of Airship: nonzero offset/length for NULL resource
BUG in Airship: Ring is disconnected or in limbo. @%s:%u
transfer_rings
BUG in Airship: bad parameter - 'header_length'
add_flusher
[%s:%d:%s] window base: 0x%llx, window size: 0x%llx
[%s:%d:%s] invalid configuration: %s at %s
auxiliary_context
[%s:%d:%s] region id %hu is in limbo, attempting to unmap
set_settled
[%s:%d:%s] (crid %hu) applied client overrides
[%s:%d:%s] participant 0x%llx added to doorbell %s[%u]
memory_map_message_completed
[%s:%d:%s] (trid %hu) free transfers %hu must exceed dead space size %hu
BUG in client of Airship: attempted to unregister handler for terminated driver @%s:%u
Airship device power off timed out
t2026-CentauriBeta
BUG in client of Airship: attempted to access inactive mirror
set_configuration
unregister_client_statedump_handler
[%s:%d:%s] context id %hu close message result %u
read_index_array
airship-transport-setup-failure
[%s:%d:%s] trid %hu in limbo
ipc-running-timeout
~reaper_target
BUG in client of Airship: attempted to reconfigure active monitor @%s:%u
image_address_hi
value exceedes auxiliary context limit
[%s:%d:%s] creating boot controller for %s
[%s:%d:%s] (crid %hu) sending open message
tr_settled
loadBundleResourceByName
[%s:%d:%s] debugInfo capture complete, size %u
consume_transfers
update_debug_ring_state
write_tr_head_index
[%s:%d:%s] (ctxid %hu) applied client overrides
driverkit_event_call
stop
validate_buffer_bounds
[%s:%d:%s] updating register at bank=%u, offset=%u
print_queue_stats
[%s:%d:%s] (trid %hu) stopping controller
[%s:%d:%s] no custom statedump handlers registered
[%s:%d:%s] (crid %hu) update bad cd
OSAction_AirshipOSActionProxy_TimerOccurred
setBusLeadAndMemoryEnable
AirshipDriverName
[%s:%d:%s] destroying transfer ring handle for trid %hu
read_head_index
remove_cr
append_cr_index_info
AirshipAutoExitReset
get_mh_uuid
optional.hpp
CentauriHelperMemregionUserClient
move_transfers
BUG in client of Airship: attempted to set external interrupt handler for terminated driver @%s:%u
[%s:%d:%s] sending overflow messages
[%s:%d:%s] stop reason %u
ipc_handshake_timeout_occurred
[%s:%d:%s] wake requested=%u, target host sleep=%u, permit device sleep=%u
skip_window_configuration
operator=
[%s:%d:%s] Deregistering tail index update handler for trid %hu at vector %hu
[%s:%d:%s] creating memregion controller for %s[%u]
CentauriHelperTimesyncUserClient
async_accelerator_private.cpp
[%s:%d:%s] (trid %hu) new doorbell interval (%u us), new leeway (%u us)
in-place completion requires in-order
[%s:%d:%s] (trid %hu) transfer at index %hu is in state %u
start_block_invoke
not privileged
BUG in Airship: attempted to reconfigure active object @%s:%u
handle_mem_read16
get_and_advance_inorder_idx_for_completion
is_healthy
BUG in client of Airship: attempt to reconfigure active TR
BUG in client of Airship: attempted to activate canceled monitor @%s:%u
selector
BUG in client of Airship: attempted to access inactive CR @%s:%u
state_dump_manager.cpp
[%s:%d:%s] starting messenger
[%s:%d:%s] copying message payload
completion_group
[%s:%d:%s] (trid %hu) controller opened
rw_mutex.hpp
set_doorbell_moderation
device-sleep-exit-timeout
[%s:%d:%s] deferring message send
[%s:%d:%s] index %hu
[%s:%d:%s] suspending transport
BUG in client of Airship: attempted to activate active interrupt @%s:%u
Start_Impl_block_invoke_5
[%s:%d:%s] creating airship driver handle
[%s:%d:%s] device power off deadline expired
BUG in client of Airship: attempted to activate already-active CR
true
open_tr
send_context_close_message
config_from_doorbell_spec
[%s:%d:%s] sleep status: host sleep
response code is ambiguous
[%s:%d:%s] %s[%u] old status %u, new status %u
airship-poweroff-timeout-waiting-for-driver-quiesce
[%s:%d:%s] (crid %hu) registering with doorbell coordinator with doorbell %s
[%s:%d:%s] context id %hu in limbo
uint64_value
BUG in Airship: attempted to insert null value into boxed dictionary @%s:%u
[%s:%d:%s] ipc handshake complete
multi
[%s:%d:%s] region id %hu deferring unmap message
populate_descriptor
stop_block_invoke
set_maintenance_completion_notifier
com.apple.iokit.pm.wakedescription.continuous-time-offset
change_to_ipc_stage
boot_manager.cpp
[%s:%d:%s] set transport result 0x%x
~driver
device_transport.cpp
unknown-error
[%s:%d:%s] (bc %s) sending image
BUG in Airship: requested CD element is inactive @%s:%u
external
[%s:%d:%s] ipc status invalid
BUG in client of Airship: attempted to await inactive monitor
BUG in client of Airship: attempted to destroy client with subordinate object handles
initDriverIOServiceParams
BUG in Airship: list element destroyed while in list
BUG in client of Airship: attempt to reconfigure active context
enqueue_batch
swizzle_proxima_viddid_for_platform
unknown keys present
completion_ring_stride
com.apple.airship.debug-%s
not ready
BUG in client of Airship: nonzero selector for NULL resource
[%s:%d:%s] (crid %hu) close complete
unsupported value
ring_size
BUG in Airship: Attempted to perform a health check in driver_client @%s:%u
[%s:%d:%s] sending message now
tr_open_message_completed
tr_close_message_completed
[%s:%d:%s] stopping context id %hu for reason %u
[%s:%d:%s] adding crid %hu flush tracking for trid %hu
resume
[%s:%d:%s] ipc stage not torn down, boot stage valid: %u, main stage valid: %u
[%s:%d:%s] messenger failed to map mtr/mcr memory
[%s:%d:%s] airship driver service is not active
airship-debug
[%s:%d:%s] consuming transfers
[%s:%d:%s] invalid params
truncate
BUG in Airship: airship_acipc_tr_disconnect: not implemented @%s:%u
invalid value
write_index_array
[%s:%d:%s] (trid %hu) seek %hu exceeds pending transfer count %hu
set_ipc_error_handler
[%s:%d:%s] (bc %s) old state=0x%llx, new state=0x%llx
set_context
BUG in Airship: list element destroyed while in list @%s:%u
device_classifier.cpp
instance count is zero
index
map_region
set_interrupt_handler
BUG in client of Airship: attempted to set external interrupt handler for inactive driver
[%s:%d:%s] context id %hu open message result %u
read_exec_stage_register
min_interval_usec
BUG in client of Airship: attempted to create client for inactive driver
ring_index_pair.hpp
environment.cpp
set_value
[%s:%d:%s] main ipc stage name %s
save_transfer_completion
[%s:%d:%s] (crid %hu) invalid completion descriptor at idx=%hu
[%s:%d:%s] opening mtr
[%s:%d:%s] cr_open 
get_debug_object_alloc_size
[%s:%d:%s] entering reset, dropping any pending doorbells
driver_object
dump_object_info
[%s:%d:%s] (bc %s) image_state=%u
is_cr_required_completion_context_for_any_open_tr
intrusive_list.hpp
unsupported register width
nominal_transfer_size
memregion_manager.cpp
Airship ACIPC protocol error
[%s:%d:%s] new ipc status=%u
header_size
tr_controller.cpp
[%s:%d:%s] (trid %hu) sending open message
[%s:%d:%s] copying appendix
AirshipDeviceDK_IVars
reset
insert
resource
resource_stride
nominal_state_dump_size
~client_interrupt
[%s:%d:%s] (crid %hu) open failed 0x%x
set_cr_open
BUG in Airship: bad array access @%s:%u
BUG in client of Airship: attempted to activate already-active TR @%s:%u
BUG in Airship: attempted to create boxed string from null C string @%s:%u
BUG in Airship: attempted to create boxed string from null format string @%s:%u
stop_region
[%s:%d:%s] running power state changed wait context
trigger_async
log
[%s:%d:%s] begin power change; power flags %u
BUG in Airship: flat array size multiplication overflow @%s:%u
completion_mirror
[%s:%d:%s] destroying completion ring handle for crid %hu
typed_allocators.cpp
wait
clearPowerAssertion
[%s:%d:%s] Initializing device
ensure_free_space
BUG in Airship: Ring is disconnected or in limbo.
[%s:%d:%s] tearing down current ipc stage
[%s:%d:%s] (ctxid %hu) failed to validate client override
[%s:%d:%s] driver ioservice params: ipcPowerOn %u ms, ipcPowerOff %u ms, devicePowerOn %u ms, devicePowerOff %u ms
[%s:%d:%s] (trid %hu) transfer tag %hu does not match next in-order tag %hu
set_notifier
cr_close_message_completed
[%s:%d:%s] ring manager already out of reset
BUG in client of Airship: attempted to reconfigure active memregion
read_tr_tail_index
[%s:%d:%s] releasing ring with selector %u
get_free_space
cldma-rx-error
get_max_message_length
finalize_tr_settlement_if_ready
[%s:%d:%s] context_open 
clear_tr_indices
get_image_response
[%s:%d:%s] opening mcr
BUG in client of Airship: attempted to activate active monitor
[%s:%d:%s] message success, setting state for region id %hu
register_cr_index_vector_action
acipc_create_doorbell_controller
BUG in Airship: access to null buffer mapping @%s:%u
set_context_closed
[%s:%d:%s] stopping context id %hu
[%s:%d:%s] failed to flatten name/sel into string
[%s:%d:%s] exec_stage during power-on=%u
[%s:%d:%s] cannot wake
[%s:%d:%s] IPC driver state_dump complete
[%s:%d:%s] (bc %s) checking for image response
with_cstr_nocopy
BUG in Airship: bad parameter - 'footer_length'
ipc_power_on_timeout_ms
handle_is_interrupt_source_connected
stop_context
BUG in Airship: attempted to insert element already in list @%s:%u
airship_platform_get_conttime_offset
completion_ring
operation canceled
unable to map memory
BUG in client of Airship: attempted to access inactive context
driver_debug_object.hpp
[%s:%d:%s] updating context info address register
[%s:%d:%s] IPC handshake timer expired
BUG in client of Airship: attempted to activate monitor with event handlers but without queue @%s:%u
set_image_sent
[%s:%d:%s] region id %hu sending unmap message
deregister_cr_index_vector_action
[%s:%d:%s] (trid %hu) new device ring status=%u
destroy_client
BUG in client of Airship: attempt to reconfigure active TR @%s:%u
sleep_state_machine
disallowed name
[%s:%d:%s] (trid %hu) close complete
sync
context_open_message_completed
BUG in client of Airship: attempted to access inactive interrupt @%s:%u
[%s:%d:%s] creating tr controller for %s[%u]
[%s:%d:%s] context id %hu has unmessaged lifecycle, closing
[%s:%d:%s] setting boot controller for ipc stage %s to unavailable
default
already in use (exclusive access)
[%s:%d:%s] property '%s' is not numeric
[%s:%d:%s] closing mcr
[%s:%d:%s] sending open message for trid %hu
[%s:%d:%s] ACIPC protocol error 0x%08x (%s)
write
[%s:%d:%s] (trid %hu) controller reset
BUG in Airship: attempted to remove element not in list
ignore_zeroed_cd
BUG in client of Airship: Cannot destroy handle before ring has been closed.
BUG in client of Airship: attempted to activate already-active TR
teardown_boot_ipc_stage
[%s:%d:%s] message failed, setting state for region id %hu
BUG in Airship: unexpected flush notice
matchesCriteria
[%s:%d:%s] crid %hu in limbo
deviceMatched
requestDevicePower
~reaper
device sleep
[%s:%d:%s] value %u matches to exec stage: %s
constraints not satisfied by default
[%s:%d:%s] (ctxid %hu) new availability blockers 0x%08x
BUG in Airship: invalid src
completed_transfer_log_depth
ipc_running_timeout
context_controller_block_invoke
acipc_driver_client.cpp
process_inplace_completions
[%s:%d:%s] driver create client end %s
[%s:%d:%s] sending any overflow messages
context_close_message_completed
BUG in Airship: attempted to create boxed symbol from null string
parse
transfer_footer_size
channel-update-failure
[%s:%d:%s] failed to retrieve property '%s'
AncestorRegistryID
OSAction_AirshipOSActionProxy_InterruptOccurred
handle_probe_exec_stage
leeway_usec
BUG in Airship: attempted access to terminated client @%s:%u
BUG in Airship: attempted to create cr_controller in driver_client @%s:%u
[%s:%d:%s] %s[%u] unavailable
[%s:%d:%s] (trid %hu) first index %hu exceeds size %hu
mappable_buffer.cpp
BUG in client of Airship: attempted to activate already-active context @%s:%u
unknown context
[%s:%d:%s] image has already been sent
BUG in client of Airship: attempted to set interrupt execution queue for inactive driver @%s:%u
handle_mem_read8
main_ipc_state_machine
[%s:%d:%s] stopping boot controller for ipc stage %s
completion_ring_will_flush
~messenger
get_proxima_platform
BUG in Airship: invalid head index advance operation @%s:%u
~driver_resource
configurator.cpp
interval_usec
IOService
isIpcPowerStateValidForDriverPowerState
swizzleConfigName
with_format
peripheral_info_interrupt_occurred
register_tr_index_vector_action
compute_hdrftr_size_fields
[%s:%d:%s] not in reset
[%s:%d:%s] clearing in reset transport blocker
nil
mem_read32
[%s:%d:%s] automatically placing driver in reset
[%s:%d:%s] (trid %hu) sending close message
[%s:%d:%s] syncing mcr head index update
[%s:%d:%s] power flags changed to %u
BUG in client of Airship: nonzero offset/length for NULL resource @%s:%u
remove_context
add_doorbells
unexpected-sleep-status
change_to_exec_stage
[%s:%d:%s] device service does not match criteria
get_first_free_tag
BUG in client of Airship: attempted to reconfigure active CR @%s:%u
BUG in Airship: attempted to create client for terminated driver @%s:%u
operator[]
BUG in Airship: attempted to create boxed symbol from null string @%s:%u
memregion_controller
handle_get_mmio_physical_address
dynamic_array.hpp
[%s:%d:%s] crid %hu has unmessaged lifecycle, setting closed
BUG in Airship: refcount_mixin overreleased
[%s:%d:%s] setting up ipc status interrupt
get_prev_transfer_in_queue
[%s:%d:%s] (trid %hu) create tx_queue: size %hu, hdrlen %u, ftrlen %u, out-of-order %u
BUG in Airship: access to null buffer
static_array.hpp
[%s:%d:%s] num of objects pending deletion %u
v12@?0I8
BUG in client of Airship: attempted to activate active interrupt
completion_footer_size
non-default completion group requires out-of-order
[%s:%d:%s] map successful
airship-trap-on-device-power-off-timeout
mem_write16
[%s:%d:%s] stopping trid %hu for reason %u
BUG in client of Airship: attempted to activate already-active memregion @%s:%u
acipc_driver.cpp
[%s:%d:%s] setting up peripheral info interrupt
buffer_create
[%s:%d:%s] setting up timer
[%s:%d:%s] IPC driver state dump size %u
BUG in Airship: attempted to activate canceled object @%s:%u
[%s:%d:%s] (bc %s) image address 0x%llx, length 0x%x
[%s:%d:%s] adding boot controller for ipc stage %s
create_device_memory_mapping
addPowerAssertion
[%s:%d:%s] stopping crid %hu
[%s:%d:%s] setting context id %hu closed
[%s:%d:%s] failed to find stage for value, %u
acipc_create_context_controller
[%s:%d:%s] insufficient buffer
BUG in Airship: attempted to insert element at position not in list @%s:%u
validate_client_overrides
[%s:%d:%s] current main ipc stage and transport must be set
completion_group_stride
parse_dict
acipc_private.cpp
[%s:%d:%s] updated exec stage: %u, current %u
derivedStart
mode
image_response
BUG in Airship: attempted to activate active object @%s:%u
[%s:%d:%s] trigger superdispatch for SetPowerState
acquire_resource
BUG in Airship: attempted to create cr_controller in driver_client
[%s:%d:%s] removing boot controller for ipc stage %s
acipc_create_boot_controller
BUG in Airship: attempted to activate terminated driver @%s:%u
BUG in Airship: unaligned device memory access
doorbell_coordinator.cpp
[%s:%d:%s] added %u instances of doorbell %s
buffer_array
tr_ring
[%s:%d:%s] creating handle for completion ring with crid %u
[%s:%d:%s] reserving ring with selector %u
interrupt.cpp
acipc
~driver_object_manager
window_size
loadIpcConfig
NewUserClient_Impl
set_exec_stage_change_handler
[%s:%d:%s] creating dispatch queue
[%s:%d:%s] device is not active
CentauriControl
did_set_transport
shared_constant
~async_accelerator
device error
pci_transport.cpp
[%s:%d:%s] (crid %hu) new device ring status=%u
setPowerAssertion
AirshipPCIDeviceDK.cpp
handle_activate
BUG in client of Airship: attempted to set interrupt execution queue for inactive driver
setup_tr_settlement_tracking
unexpected-transport-revocation
ipc_stage
doorbell value not configured in shared constant mode
release_resource
[%s:%d:%s] capture streaming logs
~state_dump_manager
[%s:%d:%s] already in reset
open
get_device_sw_scaled_timeout
synchronized
context_controller
%s.plist
[%s:%d:%s] currentPower %u, pendingPower %u, device valid %s
multicomp_find_first_transfer
[%s:%d:%s] (crid %hu) controller closed
addDriver
with_str
doorbell_moderation
value exceeds ipc stage limit
AirshipDeviceDK
errorOccurred
ring_pool
[%s:%d:%s] setting up mcr
remove_tr
doorbell_controller.cpp
advance_head_index
BUG in client of Airship: attempted to await inactive monitor @%s:%u
create_cr_controller
[%s:%d:%s] (trid %hu) do not overwrite existing bad tx completion buffer
0x%08x:
BUG in Airship: bad boxed access
[%s:%d:%s] viddid=%#x
[%s:%d:%s] entering host sleep
success_code
BUG in Airship: wrong index
create_tr_controller
unknown result code
[%s:%d:%s] updated power state: %u, current %u
get_element
registers
BUG in client of Airship: attempted to destroy client with subordinate object handles @%s:%u
[%s:%d:%s] setting external interrupt handler for vector %u
async_notifier.cpp
unregister_statedump_collection_handler
[%s:%d:%s] sending close message for context id %hu
ipc_status
device_memory.hpp
direct_cr_controller.cpp
driverkit_queue_callback
[%s:%d:%s] creating mtr
buffer
direct_interrupt.cpp
[%s:%d:%s] (trid %hu) new availability blockers 0x%08x
ok
set_backing_ring_size
[%s:%d:%s] (crid %hu) sending close message
[%s:%d:%s] (crid %hu) reaping cr
ipc_control
no-error
BUG in Airship: attempted truncate to larger size @%s:%u
BUG in Airship: access to non-held resource @%s:%u
unexpected-ipc-status
[%s:%d:%s] dbs : total %lu, active %lu, pending %d
merge_location
~driver_client
[%s:%d:%s] failed to look up configuration for %s[%u]
BUG in client of Airship: attempted to access inactive driver
~cr_controller
image_address_lo
[%s:%d:%s] creating doorbell controller for %s[%u]
[%s:%d:%s] starting driver
[%s:%d:%s] creating new ring pool for transfer ring %s
BUG in client of Airship: attempted to access inactive mirror @%s:%u
request_cr_close
capability
add_region
compute_state_detail
set_mirror_enabled
set_open_clientdata
set_event_handler
[%s:%d:%s] (crid %hu) inserting completion with trid %hu and first tag %hu
set_transfer_footer_size
CentauriAlpha
<nil>
[%s:%d:%s] entering device sleep
[%s:%d:%s] region id %hu adding memregion_controller
device_power_on_timeout_ms
acquire
ring_manager.cpp
retain_obj
teardown_main_ipc_stage
find_exec_stage_with_value
BUG in Airship: bad parameter - 'size' @%s:%u
[%s:%d:%s] %s[%u] stopped
trigger_driverkit_maintenance
BUG in client of Airship: attempt to reconfigure active CR
[%s:%d:%s] (bc %s) detail=0
[%s:%d:%s] airship sw scaling %llu
BUG in Airship: out of bounds access to boxed array
platform_private.cpp
airship_platform_get_conttime_offset_block_invoke
[%s:%d:%s] setting client overrides for %s[%u]
setTransportBlocker
[%s:%d:%s] kIOServiceNotificationTypeTerminated
[%s:%d:%s] (bc %s) computing image table
index_array_vector
get_transfer_completion
transfer_ring_opened
start
release_obj
BUG in Airship: attempted to create boxed symbol from null C string
BUG in Airship: attempted to find existing boxed symbol from null string @%s:%u
[%s:%d:%s] region id %hu removing memregion_controller
AirshipDriverDK
/System/DriverKit/System/Library/PrivateFrameworks/AirshipDK.framework
doorbell_coordinator
[%s:%d:%s] initializing PCI device
[%s:%d:%s] (ctxid %hu) sending close message
BUG in Airship: bad parameter - 'footer_length' @%s:%u
interrupt_occurred
[%s:%d:%s] driver create client begin %s
~direct_client_object_manager
BUG in Airship: attempted to activate terminated driver
[%s:%d:%s] setting up message buffer for main ipc stage %s
BUG in client of Airship: attempted to activate already-active context
BUG in Airship: attempted to add duplicate resource @%s:%u
BUG in client of Airship: attempted to overwrite driver transport @%s:%u
IOPCIDeviceMemoryMapBase
setup_main_ipc_stage
BUG in client of Airship: out of bounds access to buffer
[%s:%d:%s] creating context controller for %s[%u]
I/O error
set_interrupt
BUG in client of Airship: attempted to reconfigure active interrupt
channel-sync-failure
handle_create_interrupt_source
activate_block_invoke
[%s:%d:%s] boot manager is already out of reset
populate_context_info
get_inplace_completion
BUG in Airship: Attempted to perform a health check in driver_client
airship-ipc-error(%s)
set_cr_closed
BUG in Airship: airship_acipc_tr_disconnect: not implemented
peripheral_info_interrupt
window_base_lo
invalid completion style
device_info
unmap_region
set_device_region_status
[%s:%d:%s] (trid %hu) completions synthesized
[%s:%d:%s] (trid %hu) completing transfer tag %hu
remove_flusher
mtr
airship-driverkit-timer-watchdog
set_ipc_stage
~direct_tr_controller
~monitor
name
emplace
BUG in Airship: invalid tail index update operation @%s:%u
logging.cpp
set_power_state_change_handler
[%s:%d:%s] messenger already out of reset
offset
bytes
shared_timestamp
[%s:%d:%s] boot manager entering reset
finishExitResetIfNeeded
[%s:%d:%s] Airship statedump complete: provided buffer size %u copied %u
[%s:%d:%s] no handles available in pool
create_free_space_monitor
~driver_object_termination_list
refcount_mixin.hpp
send_memory_unmap_message
direct_client.cpp
get_completed_transfer_count
sync_action_flush_pending_transfers
write_tail_index
[%s:%d:%s] trid %hu close message result %u
BUG in client of Airship: Packet is null for queue entry. @%s:%u
BUG in Airship: refcount_mixin retain overflow
finish_queued_partial_chain
bad argument
BUG in client of Airship: attempted to retrieve first free tag of ring without free space @%s:%u
with_cstr
BUG in client of Airship: attempted to access inactive interrupt
com.apple.AirshipDriverDK.global.%s
[%s:%d:%s] message failure
erase
[%s:%d:%s] sending close message for crid %hu
[%s:%d:%s] new ipc stage: %s
[%s:%d:%s] mapping region of size %u for %s[%u]
protocol
[%s:%d:%s] debugInfo capture start
[%s:%d:%s] (trid %hu) transfer enqueue size %u exceeds maximum transfer size %u
update_power_state
handle_mem_read32
handle_mem_write64
(nil)
will_set_transport
Vendor
Start_Impl_block_invoke_6
[%s:%d:%s] marking driver state as running; trigger IPC driver exit_reset
[%s:%d:%s] (trid %hu) attempt to consume %hu transfers, %hu fetched
BUG in client of Airship: attempted to overwrite driver transport
BUG in client of Airship: attempted to set external interrupt handler for terminated driver
[%s:%d:%s] platform_config=%u, probed viddid=0x%#x,  proxima_viddid=0x%#x
footer_size
completion_ring_did_flush
set_cancel_handler
AirshipBuiltIn
[%s:%d:%s] closing trid %hu
[%s:%d:%s] crid %hu close message result %u
driver_resource.cpp
BUG in Airship: attempted to create tr_controller in direct_client
ServiceNotificationReady_Impl
[%s:%d:%s] (trid %hu) unexpected flush notice from CRID %hu
[%s:%d:%s] (trid %hu) update bad transfer completion
[%s:%d:%s] exiting reset
removeDriver
cr_open_message_completed
BUG in client of Airship: Packet is null for queue entry.
BUG in Airship: attempted to create boxed string from null format string
handle_append_ipc_driver_state_dump
[%s:%d:%s] not ready for exec stage interrupt
~memregion_manager
BUG in Airship: attempted to initialize optional with sentinel value
consume_mirror_elements
typed_allocators.hpp
BUG in client of Airship: attempted to retrieve first free tag of ring without free space
~driver_object
BUG in client of Airship: selector is not available @%s:%u
close
[%s:%d:%s] Added context id %hu
set_completion_ring
BUG in client of Airship: attempted to access inactive TR
driverkit_maintenance
direct_context.cpp
BUG in Airship: bad optional access @%s:%u
vector
completion_header_size
doorbell
[%s:%d:%s] %s[%u] reset
base.cpp
com.apple.AirshipDeviceDK.service-default
appendDeviceStateDump
[%s:%d:%s] sleep status invalid
interrupt_stride
BUG in Airship: requested TD element is inactive @%s:%u
BUG in Airship: invalid dst
connect_interrupt
get_mirror_element
[%s:%d:%s] window_base=%#llx, size=%#llx
parse_symbol
no space for data
wakeup
SetPowerState_Impl
image_doorbell
set_map_clientdata
BUG in client of Airship: attempted to activate already-active memregion
refresh_mapping
BUG in Airship: _memory is NULL @%s:%u
getExecStage
airship_platform_get_fallback_queue_block_invoke
[%s:%d:%s] Enable BusLead and Memory
ipc stage
[%s:%d:%s] (trid %hu) free=%hu, queued=%hu, pending=%hu, completed=%hu, fetched=%hu
synthesize_reset_completions
sync_action_process_ti_update
io-timeout
cr_controller
enqueue_transfer_with_ioun_packet
BUG in client of Airship: attempted to activate interrupt with event handlers but without queue
buffer_create_with_iomd
create_client
[%s:%d:%s] (bc %s) image sent, recomputing state
[%s:%d:%s] complete
enter_reset
memory_regions
BUG in Airship: bad parameter - 'memory' @%s:%u
startTimer
flush_queued_transfers
append_context_state_dump
BUG in Airship: out of bounds access to boxed array @%s:%u
BUG in Airship: size is too big
[%s:%d:%s] reaping %s[%u]
TargetName
interrupt
cldma-tx-error
restricted
context_info_address_hi
[%s:%d:%s] getting auto-exit reset
timeout
set_external_execution_queue
BUG in Airship: attempted to activate active object
add_context
BUG in Airship: requested CD element is inactive
peripheral_info_update_filter
[%s:%d:%s] cannot set transport, %s ipc stage is not null
[%s:%d:%s] tearing down main ipc stage
failure_code
t2026-CentauriAlpha
[%s:%d:%s] reserve %u complete
rw_mutex
process_pending
BUG in Airship: attempted to create boxed string from null C string
raise_ipc_error
[%s:%d:%s] unmapping memory region for %s[%u]
BUG in client of Airship: attempted to activate active driver @%s:%u
[%s:%d:%s] enqueuing message in mtr
[%s:%d:%s] (trid %hu) failed to validate client override
timer.cpp
channel-quiesce-failure
set_availability_blockers
messenger.cpp
set_tr_closed
set_source_maintenance_completion_handler
doorbells
auxiliary_contexts
create_resource_monitor
[%s:%d:%s] loading device configuration
[%s:%d:%s] Airship error occurred (0x%x), ipcErrorState (0x%x)
multiple-errors
update_head_index
acipc doorbell
probe_exec_stage_register_if_ready
traffic_class
group_stride
timerExpired
[%s:%d:%s] getting device class
update_exec_stage
[%s:%d:%s] (crid %hu) registering interrupt and setting up index array signaler vector %hu
schedule_update
[%s:%d:%s] resuming doorbell coordinator
set_completion_footer_size
reaper.cpp
[%s:%d:%s] (ctxid %hu) stopping controller
BUG in Airship: attempted to create tr_controller in direct_client @%s:%u
BUG in client of Airship: externally managed ring @%s:%u
set_interrupt_execution_queue
[%s:%d:%s] tearing down boot ipc stage
get_first_completed_tag
[%s:%d:%s] (crid %hu) failed to validate client override
[%s:%d:%s] (crid %hu) cr terminated
BUG in Airship: attempted message send in reset
process_completions
request_tr_close
[%s:%d:%s] updating context close requests
BUG in client of Airship: attempted to reconfigure active TR @%s:%u
[%s:%d:%s] performing health check.
get_inorder_tag_for_enqueue
[%s:%d:%s] (trid %hu) predecessor completion ID %hu does not equal completion ID %hu
[%s:%d:%s] (trid %hu) failed: hi=%hu, ti=%hu
create_debug_object
not open
direct_client_object
boxed_types.cpp
ipc_status_interrupt_occurred
unexpected object type
BUG in Airship: unrecognized detail bits in context controller. @%s:%u
Airship IPC power on timed out @%s:%u
[%s:%d:%s] (crid %hu) stopping controller
send_message
[%s:%d:%s] crid %hu is associated with trid %hu
[%s:%d:%s] removing participant 0x%llx from pending queue
scribble_descriptor
map
exitReset
[%s:%d:%s] current blockers (%u), set blockers (%u)
set_external_management
typed_delete
[%s:%d:%s] (ctxid %hu) controller state=%u, detail=%u
[%s:%d:%s] resourceFileName=%s
~ring_pool
register_client_statedump_handler
set_backing_memory
[%s:%d:%s] setting crid %hu open
[%s:%d:%s] trid %hu open message result %u
BUG in client of Airship: attempted to activate active monitor @%s:%u
deregister_tr_index_vector_action
ipcCalloutOccurred
t2026-CentauriBeta_BetaPrimeFPGA
disconnected (no device)
get_addr
update_context_info_addr_registers
[%s:%d:%s] attaching pending device to driver
recompute_state
[%s:%d:%s] (crid %hu) do not overwrite existing bad_cd buffer
[%s:%d:%s] oversize host memory window reduced from %#llx to UINT32_MAX
[%s:%d:%s] (trid %hu) state=%u, activated=%u
BUG in client of Airship: attempted to activate active driver
handle_enter_reset
airship-trap-on-acipc-error
count
[%s:%d:%s] invalid device
[%s:%d:%s] associating crid %hu <-> trid %hu
BUG in Airship: bad array access
bad-cr-hi-update
BUG in client of Airship: externally managed ring
BUG in client of Airship: attempted to unregister handler for terminated driver
[%s:%d:%s] timer deadline missed!!
driver_object.cpp
ring_header_footer_scaling
out_of_order
AirshipDeviceCriteria
reserve_next
BUG in client of Airship: attempted to activate already-active CR @%s:%u
mem_write
set_size
unmap
[%s:%d:%s] detaching from device
[%s:%d:%s] (bc %s) reseting boot controller
[%s:%d:%s] (bc %s) stopping boot controller
BUG in Airship: attempted to retrieve max message length in reset
t2026
recomputePowerRequest_block_invoke
close_context
context_info_address_lo
buffer_size_ring
[%s:%d:%s] Registering head index update handler for crid %hu at vector %hu
[%s:%d:%s] failed to set client overrides for %s[%u]
AirshipDriverConfigName
[%s:%d:%s] (trid %hu) transfer flush failed
host-sleep-failure
[%s:%d:%s] synthesizing completions if needed
[%s:%d:%s] ts: last_write %llx, schedule %llx, deadline %llx, 
copy_to
image_size
[%s:%d:%s] boot manager is in reset
write_cr_tail_index
[%s:%d:%s] capture AirshipDeviceDK state
[%s:%d:%s] (trid %hu) invalid in-place completion at idx=%hu
BUG in client of Airship: attempted to set external interrupt handler for inactive driver @%s:%u
get_current_ipc_stage_name
unexpected mode string
window_base_hi
~direct_client
BUG in Airship: attempted to activate canceled object
save_overflow_message
[%s:%d:%s] payload length %u, appendix length %u
exit_reset
com.apple.airship.global-timer-queue
acipc_create_memregion_controller
[%s:%d:%s] starting timer with interval (%u)
BUG in client of Airship: Failed to locate transfer ring config @%s:%u
ALLOCATION FAILURE (or BUG) in Airship @%s:%u
[%s:%d:%s] crid %hu has unmessaged lifecycle, closing
[%s:%d:%s] removed context id %hu
[%s:%d:%s] context id %hu has unmessaged lifecycle, setting closed
BUG in Airship: refcount_mixin overreleased @%s:%u
invalid alignment
[%s:%d:%s] (trid %hu) TR is now settled
handle_get_mmio_size
[%s:%d:%s] saving overflow message
[%s:%d:%s] crid %hu has unmessaged lifecycle, setting open
remove
advance_buffer_pointer
isDevicePowerStateValidForDriverPowerState
set_mcr_event_handler
enterReset
v16@?0^v8
notify_transfer_ring_when_flushed
[%s:%d:%s] completion count %hu
[%s:%d:%s] message success
BUG in Airship: 
close_tr
handle_exit_reset
version
[%s:%d:%s] region %s (id=%hu) cannot be used due to id conflict with name %s
ring_controller.cpp
general error
isPoweredOnWithAssertion
[%s:%d:%s] trid %hu is settled
[%s:%d:%s] exec stage reg value=%u
doorbell_stride
[%s:%d:%s] clearing transport
downlink-update-failure
IOPCIDeviceMapperPageSize
handle_append_state_dump
[%s:%d:%s] creating mcr
[%s:%d:%s] added crid %hu
chain
airship-trap-on-device-attach-timeout
[%s:%d:%s] kIOServiceNotificationTypeMatched
write_head_index
BUG in Airship: access to null buffer mapping
host-wake-failure
[%s:%d:%s] stopping crid %hu for reason %u
system-error
BUG in Airship: attempted to add duplicate resource
[%s:%d:%s] main ipc state is not running (%u) or transport is not set
[%s:%d:%s] acquiring resource %s
BUG in Airship:  @%s:%u
[%s:%d:%s] trid %hu close message requested
BUG in Airship: attempted to access boxed dictionary with null key
probe
[%s:%d:%s] exiting host sleep
cr_index_count
parse_array
[%s:%d:%s] starting power off deadline timer
BUG in Airship: invalid dst @%s:%u
[%s:%d:%s] (crid %hu) new interrupt %s[%u]
dal25
dump_pending_transfer_stats
context_controller.cpp
BUG in Airship: attempted to reconfigure active object
get_mirror_count
transfer_ring_settled
[%s:%d:%s] (crid %hu) trid %hu does not accept completions from this cr
add_cr
BUG in client of Airship: attempted to reconfigure active interrupt @%s:%u
queue
image_interrupt
send_overflow_messages
[%s:%d:%s] syncing mtr tail index update and fetching completions
send_context_open_message
[%s:%d:%s] ring manager already in reset
[%s:%d:%s] stopping trid %hu
derivedProbeDevice
get_health_status
[%s:%d:%s] creating device memory
ambiguous value
detachFromDevice
BUG in client of Airship: attempted to register handler for terminated driver @%s:%u
read_ipc_status_register
scratch_size
roles
airship-poweron-timeout-waiting-for-firmware
handle_mem_write32
sync_action_process_hi_update
[%s:%d:%s] trid %hu status %u
[%s:%d:%s] (trid %hu) failed to find first transfer
write_register
get_and_advance_inorder_idx_for_enqueue
Stop_Impl
[%s:%d:%s] failed to allocate/map device memory
mcr
activate
BUG in client of Airship: attempted to access inactive context @%s:%u
bad-tr-ti-update
~acipc_driver
Airship ACIPC protocol error @%s:%u
[%s:%d:%s] not ready for peripheral info interrupt
disconnect_interrupt
append_state_dump
hexdump
[%s:%d:%s] image response %u, code %u
airship_acipc_tr_disconnect
[%s:%d:%s] setting up message rings
limits
read_cr_head_index
[%s:%d:%s] power state not ready, setting transport blocker
Start_Impl_block_invoke
[%s:%d:%s] trid %hu has unmessaged lifecycle, closing
insert_before
boot
CentauriHelperInterfaceUserClient
[%s:%d:%s] setting up callout notifier
BUG in client of Airship: Failed to locate transfer ring config
value
BUG in Airship: bad parameter - 'size'
attachToPendingDeviceIfNeeded
[%s:%d:%s] (trid %hu) completing chain
set_external_handler
BUG in client of Airship: attempt to reconfigure active CR @%s:%u
[%s:%d:%s] (crid %hu) invalid hi: %hu
operator()
BUG in Airship: bad boxed access @%s:%u
[%s:%d:%s] ipc status=%u
Chipset
ipc_power_off_timeout_ms
set_client_overrides
get_state
[%s:%d:%s] crid %hu status %u
[%s:%d:%s] notifying crid %hu that trid %hu is settled
transfer_queue.cpp
cancel_participant
acipc.cpp
create_interrupt
[%s:%d:%s] failed to look up configuration for %s
[%s:%d:%s] activating doorbell coordinator with %u doorbell instances
[%s:%d:%s] created completion mirror object
setup_interrupt
bind_active_object
[%s:%d:%s] creating new ring pool for completion ring %s
get_next_transfer_in_queue
[%s:%d:%s] handle_activate: result 0x%x
~boot_manager
cldma-link-error
[%s:%d:%s] (bc %s) out code=%u
dequeue_batch_with_limit
airship_acipc_tr_dequeue_batch
BUG in Airship: requested TD element is inactive
com.apple.AirshipDriverDK.per-device.%s
BUG in client of Airship: attempted to reconfigure active driver @%s:%u
[%s:%d:%s] (bc %s) image response code=%u
exec_stage_interrupt_occurred
[%s:%d:%s] change to exec stage %s (%u) from %s
exec_stage
debug
ring_pool.cpp
is_sleep_status_valid
boot_ipc_stages
airship-poweroff-timeout-waiting-for-firmware
[%s:%d:%s] (trid %hu) index %hu exceeds size %hu
uplink-update-failure
[%s:%d:%s] setting up mtr
[%s:%d:%s] reset type %u
[%s:%d:%s] provider 0x%llx\n
add_participant
bad-inplace-completion
airship_platform_get_timer_queue_block_invoke
[%s:%d:%s] no ipc stage set
BUG in Airship: unrecognized detail bits in context controller.
Role
initDriverIOServiceParams_block_invoke
setup_notifier
v32@?0Q8^{IOService=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})}16Q24
~tr_controller
~interrupt
driver.cpp
BUG in client of Airship: invalid queue role @%s:%u
set_power_target
handle_mem_read64
BUG in Airship: flat array size multiplication overflow
shared_counter
memregion_controller.cpp
set_queue
[%s:%d:%s] tearing down mtr
Start_Impl
debug_infra.hpp
arm_cr_index_vector
Airship device power on timed out @%s:%u
BUG in client of Airship: attempted to unregister handler for inactive driver @%s:%u
send_image
[%s:%d:%s] closing mtr
B24@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}16
[%s:%d:%s] context id %hu close message requested
[%s:%d:%s] value for shared constant doorbell: %u
[%s:%d:%s] applied errata window_base_mask=%#llx, masked_base=%#llx
client_registers
airship-multiple-errors(0x%08x,0x%08x)
[%s:%d:%s] clearing power state not ready blocker
[%s:%d:%s] device attach deadline expired
unknown ipc stage
[%s:%d:%s] creating cr controller for %s[%u]
boot_controller.cpp
[%s:%d:%s] stopping provider
instance resolution failure
recompute_region_availability
[%s:%d:%s] driver name: %s
update_tail_index
[%s:%d:%s] getting transfer completion for tag %hu
proxima-platform
BUG in client of Airship: Failed to locate completion ring config
[%s:%d:%s] setting external execution queue for vector %u
retain
chipset
get_vector_for_interrupt
BUG in client of Airship: attempted to create client for inactive driver @%s:%u
[%s:%d:%s] DART page size 0x%llx, memory map: base 0x%llx, size 0x%llx)
[%s:%d:%s] requesting close for trid %hu
Airship IPC power off timed out
[%s:%d:%s] canceling timer
BUG in client of Airship: mode must be AIRSHIP_ACIPC_TR_MODE_STANDARD @%s:%u
monitor.cpp
append_element
[%s:%d:%s] new item at index %hu
group
compute_offsets
[%s:%d:%s] boot manager exiting reset
BUG in Airship: attempted message send in reset @%s:%u
Default
is_cr_completion_context_for_tr
traffic_wake
BUG in client of Airship: attempted to activate canceled monitor
count_intersection
[%s:%d:%s] (crid %hu) new doorbell interval (%u us), new leeway (%u us)
retrieve_state_dump
devmem_mapping
[%s:%d:%s] controller ipc stage: %s
boot_controller
[%s:%d:%s] (crid %hu) failed to complete transfer
[%s:%d:%s] crid %hu open message result %u
BUG in Airship: attempted to remove element not in list @%s:%u
emplace_back
[%s:%d:%s] derivedStart successful\n
BUG in client of Airship: attempted to retrieve first completed tag of ring without completed transfers @%s:%u
None
BUG in client of Airship: selector is invalid @%s:%u
com.apple.iokit.pm.wakedescription
driverkit_event_callback
[%s:%d:%s] closing crid %hu
reduce_size
exec_stages
[%s:%d:%s] entering reset
[%s:%d:%s] sending open message for context id %hu
[%s:%d:%s] probing device
%s-%u
handle_clear_transport
optimized_completion
vendor
[%s:%d:%s] ring manager is in reset
Dale
BUG in Airship: refcount_mixin retain overflow @%s:%u
[%s:%d:%s] setting up boot ipc stage
ambiguous name
resolve
[%s:%d:%s] boot manager is already in reset
[%s:%d:%s] updated error state: %u, current %u
BUG in client of Airship: attempt to reconfigure active context @%s:%u
exec_stage_interrupt
virtual
get_paddr
set_ipc_error_flags
set_tr_open
[%s:%d:%s] requesting close for context id %hu
size
cr_ring.cpp
~monitor_target
setup_boot_ipc_stage
main_ipc_stages
[%s:%d:%s] (ctxid %hu) reaping context controller
BUG in Airship: size is too big @%s:%u
multicomp_complete_prior_transfers
BUG in Airship: attempted to create client for terminated driver
[%s:%d:%s] coordinator state=%u, new IPC stage=%s
reap_single_DROPS_LOCK
com.apple.airship.global-sleep-queue
BUG in client of Airship: attempted to activate monitor with event handlers but without queue
does_region_conflict_with_any_mapped_region
BUG in Airship: _memory is NULL
[%s:%d:%s] located completion ring configuration, adding %u instances
enqueue_transfer
BUG in Airship: attempted to insert null value into boxed dictionary
[%s:%d:%s] adding %u instances of resource %s
sleep_control
AirshipDevice attach timeout @%s:%u
[%s:%d:%s] getting driver name
BUG in client of Airship: attempted to unregister handler for inactive driver
BUG in Airship: invalid head index update operation @%s:%u
set_context_open
get_value
[%s:%d:%s] starting ipc handshake timer; timeout=%u ms
priority
[%s:%d:%s] (ctxid %hu) open failed 0x%x
[%s:%d:%s] Registering tail index update handler for trid %hu at vector %hu
fixup_remain_count
airship-trap-on-ipc-power-off-timeout
compute_free_space
copy_from
[%s:%d:%s] sleep status: %s
memory_unmap_message_completed
BuiltIn
BUG in client of Airship: attempted to activate canceled interrupt @%s:%u
[%s:%d:%s] canceling power off deadline timer
BUG in client of Airship: selector is not available
[%s:%d:%s] (trid %hu) predecessor state %u does not valid
maintenance_complete
BUG in client of Airship: invalid queue role
[%s:%d:%s] (crid %hu) controller opened
send_cr_close_message
BUG in Airship: attempted to find existing boxed symbol from null string
AirshipDeviceAttachTimeoutMS
set_transport
check_for_image_response
BUG in Airship: attempted to retrieve max message length in reset @%s:%u
[%s:%d:%s] processing completions
v8@?0
[%s:%d:%s] requesting close for crid %hu
getDriverNominalStateDumpSize
set_device_ring_status
BUG in Airship: invalid tail index advance operation @%s:%u
bank
BUG in Airship: attempted access to terminated client
BUG in Airship: attempted to initialize optional with sentinel value @%s:%u
interrupt_manager
system-failure
[%s:%d:%s] (bc %s) image valid : %s 
append_bytes
com.apple.airship.global-fallback
remove_region
tr_ring.cpp
[%s:%d:%s] crid %hu belongs to the same group as %hu
[%s:%d:%s] failed to get device memory window config
doorbell value out of range
append
Airship [%{public}s:%d:%{public}s] window_base=%#llx, size=%#llx
Airship [%{public}s:%d:%{public}s] boot manager entering reset
Airship [%{public}s:%d:%{public}s] region id %hu is in limbo, attempting to unmap
Airship [%{public}s:%d:%{public}s] (ctxid %hu) stopping controller
Airship [%{public}s:%d:%{public}s] closing mtr
Airship [%{public}s:%d:%{public}s] result=0x%x
Airship [%{public}s:%d:%{public}s] (crid %hu) open failed 0x%x
Airship [%{public}s:%d:%{public}s] starting device
Airship [%{public}s:%d:%{public}s] context id %hu has unmessaged lifecycle, setting closed
Airship [%{public}s:%d:%{public}s] exiting reset
Airship [%{public}s:%d:%{public}s] (ctxid %hu) failed to validate client override
Airship [%{public}s:%d:%{public}s] begin power change; power flags %u
Airship [%{public}s:%d:%{public}s] (bc %s) detail=%u
Airship [%{public}s:%d:%{public}s] updated power state: %u, current %u
Airship [%{public}s:%d:%{public}s] value for shared constant doorbell: %u
Airship [%{public}s:%d:%{public}s] exec stage interrupt occurred: value %u
Airship [%{public}s:%d:%{public}s] (trid %hu) failed to complete transfer tag %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) do not overwrite existing bad tx completion buffer
Airship [%{public}s:%d:%{public}s] reset type=%u
Airship [%{public}s:%d:%{public}s] getting device criteria
Airship [%{public}s:%d:%{public}s] removing participant 0x%llx from pending queue
Airship [%{public}s:%d:%{public}s] new item at index %hu
Airship [%{public}s:%d:%{public}s] region id %hu adding memregion_controller
Airship [%{public}s:%d:%{public}s] copying message payload
Airship [%{public}s:%d:%{public}s] tearing down boot ipc stage
Airship [%{public}s:%d:%{public}s] (ctxid %hu) new availability blockers 0x%08x
Airship [%{public}s:%d:%{public}s] (crid %hu) update bad cd
Airship [%{public}s:%d:%{public}s] message canceled
Airship [%{public}s:%d:%{public}s] (trid %hu) create tx_queue: size %hu, hdrlen %u, ftrlen %u, out-of-order %u
Airship [%{public}s:%d:%{public}s] %{public}s
Airship [%{public}s:%d:%{public}s] (trid %hu) stopping controller
Airship [%{public}s:%d:%{public}s] context_open %.*P
Airship [%{public}s:%d:%{public}s] trid %hu close message result %u
Airship [%{public}s:%d:%{public}s] (bc %s) checking for image response
Airship [%{public}s:%d:%{public}s] closing trid %hu
Airship [%{public}s:%d:%{public}s] pending IPC error broadcast
Airship [%{public}s:%d:%{public}s] tr_open %.*P
Airship [%{public}s:%d:%{public}s] (trid %hu) close complete
Airship [%{public}s:%d:%{public}s] debugInfo capture complete, size %u
Airship [%{public}s:%d:%{public}s] (crid %hu) controller closed
Airship [%{public}s:%d:%{public}s] trid %hu is settled
Airship [%{public}s:%d:%{public}s] trid %hu close message requested
Airship [%{public}s:%d:%{public}s] sw timeout scale for proxima protium platform: %llu
Airship [%{public}s:%d:%{public}s] clearing in reset transport blocker
Airship [%{public}s:%d:%{public}s] (bc %s) old state=0x%llx, new state=0x%llx
Airship [%{public}s:%d:%{public}s] starting messenger
Airship [%{public}s:%d:%{public}s] loading device configuration
Airship [%{public}s:%d:%{public}s] reserving ring with selector %u
Airship [%{public}s:%d:%{public}s] sending message now
Airship [%{public}s:%d:%{public}s] (trid %hu) offset %hu exceeds fetched transfer count %hu
Airship [%{public}s:%d:%{public}s] invalid device
Airship [%{public}s:%d:%{public}s] DART page size 0x%llx, memory map: base 0x%llx, size 0x%llx)
Airship [%{public}s:%d:%{public}s] crid %hu has unmessaged lifecycle, closing
Airship [%{public}s:%d:%{public}s] (trid %hu) predecessor state %u does not valid
Airship [%{public}s:%d:%{public}s] sending any overflow messages
Airship [%{public}s:%d:%{public}s] removed context id %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) new mode (%u)
Airship [%{public}s:%d:%{public}s] setting client overrides for %s[%u]
Airship [%{public}s:%d:%{public}s] Airship error occurred (0x%x), ipcErrorState (0x%x)
Airship [%{public}s:%d:%{public}s] (trid %hu) transfer at index %hu is in state %u
Airship [%{public}s:%d:%{public}s] opening mtr
Airship [%{public}s:%d:%{public}s] removed trid %hu
Airship [%{public}s:%d:%{public}s] trid: %u, state %u
Airship [%{public}s:%d:%{public}s] region id %hu removing memregion_controller
Airship [%{public}s:%d:%{public}s] capture AirshipDeviceDK state
Airship [%{public}s:%d:%{public}s] (crid %hu) registering with doorbell coordinator with doorbell %s
Airship [%{public}s:%d:%{public}s] trid %hu in limbo
Airship %s %s@%u
Airship [%{public}s:%d:%{public}s] tearing down main ipc stage
Airship [%{public}s:%d:%{public}s] no handles available in pool
Airship [%{public}s:%d:%{public}s] (trid %hu) new interrupt %s[%u]
Airship [%{public}s:%d:%{public}s] marking driver state as running; trigger IPC driver exit_reset
Airship [%{public}s:%d:%{public}s] synthesizing completions if needed
Airship [%{public}s:%d:%{public}s] ipc status invalid
Airship [%{public}s:%d:%{public}s] (crid %hu) trid %hu does not accept completions from this cr
Airship [%{public}s:%d:%{public}s] creating device memory
Airship [%{public}s:%d:%{public}s] setting external execution queue for vector %u
Airship [%{public}s:%d:%{public}s] no custom statedump handlers registered
Airship [%{public}s:%d:%{public}s] closing context id %hu
Airship [%{public}s:%d:%{public}s] context id %hu close message result %u
Airship [%{public}s:%d:%{public}s] not ready for ipc status interrupt
Airship [%{public}s:%d:%{public}s] failed to find stage for value, %u
Airship [%{public}s:%d:%{public}s] sleep status: host sleep
Airship [%{public}s:%d:%{public}s] controller ipc stage: %s
Airship [%{public}s:%d:%{public}s] kIOServiceNotificationTypeMatched
Airship [%{public}s:%d:%{public}s] removed crid %hu
Airship [%{public}s:%d:%{public}s] unexpected GUARD_ELSE failure
Airship [%{public}s:%d:%{public}s] (trid %hu) transfer flush failed
Airship [%{public}s:%d:%{public}s] entering reset, dropping any pending doorbells
Airship [%{public}s:%d:%{public}s] (ctxid %hu) reaping context controller
Airship [%{public}s:%d:%{public}s] creating airship driver handle
Airship [%{public}s:%d:%{public}s] (crid %hu) applied client overrides
Airship [%{public}s:%d:%{public}s] (crid %hu) controller opened
Airship [%{public}s:%d:%{public}s] context id %hu open message result %u
Airship [%{public}s:%d:%{public}s] unknown device viddid=%#x
Airship [%{public}s:%d:%{public}s] message failed, setting state for region id %hu
Airship [%{public}s:%d:%{public}s] (ctxid %hu) applied client overrides
Airship [%{public}s:%d:%{public}s] (trid %hu) tag %hu must belong to first in chain
Airship [%{public}s:%d:%{public}s] (bc %s) adding controller to boot manager
Airship [%{public}s:%d:%{public}s] (trid %hu) registering doorbell %s, selector %u
Airship [%{public}s:%d:%{public}s] syncing mtr tail index update and fetching completions
Airship [%{public}s:%d:%{public}s] registering service
Airship [%{public}s:%d:%{public}s] (trid %hu) controller reset
Airship [%{public}s:%d:%{public}s] setting up main ipc stage
Airship [%{public}s:%d:%{public}s] provider 0x%llx\n
Airship [%{public}s:%d:%{public}s] unknown proxima-platform: %llu
Airship [%{public}s:%d:%{public}s] new ipc stage: %s
Airship [%{public}s:%d:%{public}s] located transfer ring configuration, adding %u instances
Airship [%{public}s:%d:%{public}s] property '%s' is not numeric
Airship [%{public}s:%d:%{public}s] trigger superdispatch for SetPowerState
Airship [%{public}s:%d:%{public}s] crid %hu status %u
Airship [%{public}s:%d:%{public}s] crid %hu is not associated with any open trs
Airship [%{public}s:%d:%{public}s] reset=%u, boot_state=%s, ipc_state=%s
Airship [%{public}s:%d:%{public}s] failed to look up configuration for %s[%u]
Airship [%{public}s:%d:%{public}s] entering reset
Airship [%{public}s:%d:%{public}s] performing health check.
Airship [%{public}s:%d:%{public}s] adding interrupt source %u
Airship [%{public}s:%d:%{public}s] activate
Airship [%{public}s:%d:%{public}s] (crid %hu) sending close message
Airship [%{public}s:%d:%{public}s] invoking action
Airship [%{public}s:%d:%{public}s] sleep status: %s
Airship [%{public}s:%d:%{public}s] creating memregion controller for %s[%u]
Airship [%{public}s:%d:%{public}s] destroying transfer ring handle for trid %hu
Airship [%{public}s:%d:%{public}s] reserve %u complete
Airship [%{public}s:%d:%{public}s] (trid %hu) free=%hu, queued=%hu, pending=%hu, completed=%hu, fetched=%hu
Airship [%{public}s:%d:%{public}s] (crid %hu) failed to validate client override
Airship [%{public}s:%d:%{public}s] failed to get resource
Airship [%{public}s:%d:%{public}s] setting crid %hu closed
Airship [%{public}s:%d:%{public}s] notifying crid %hu that trid %hu is settled
Airship [%{public}s:%d:%{public}s] timer deadline missed!!
Airship [%{public}s:%d:%{public}s] dbs : total %lu, active %lu, pending %d
Airship [%{public}s:%d:%{public}s] msi stats overflow: resetting count for vector %u
Airship [%{public}s:%d:%{public}s] opening mcr
Airship [%{public}s:%d:%{public}s] context id %hu status %u
Airship [%{public}s:%d:%{public}s] (trid %hu) completing chain
Airship [%{public}s:%d:%{public}s] updated error state: %u, current %u
Airship [%{public}s:%d:%{public}s] (bc %s) reseting boot controller
Airship [%{public}s:%d:%{public}s] reset type: %s
Airship [%{public}s:%d:%{public}s] Airship: device attach deadline %u ms, starting timer
Airship [%{public}s:%d:%{public}s] (trid %hu) transfer enqueue size %u exceeds maximum transfer size %u
Airship [%{public}s:%d:%{public}s] completion count %hu
Airship [%{public}s:%d:%{public}s] getting transfer completion for tag %hu
Airship [%{public}s:%d:%{public}s] crid %hu has unmessaged lifecycle, setting closed
Airship [%{public}s:%d:%{public}s] updating register at bank=%u, offset=%u
Airship [%{public}s:%d:%{public}s] getting device class
Airship [%{public}s:%d:%{public}s] acipc driver activate complete
Airship [%{public}s:%d:%{public}s] stopping boot controller for ipc stage %s
Airship [%{public}s:%d:%{public}s] creating cr controller for %s[%u]
Airship [%{public}s:%d:%{public}s] trid %hu open message result %u
Airship [%{public}s:%d:%{public}s] derivedStart successful\n
Airship [%{public}s:%d:%{public}s] ipc stage not torn down, boot stage valid: %u, main stage valid: %u
Airship [%{public}s:%d:%{public}s] getting auto-exit reset
Airship [%{public}s:%d:%{public}s] (trid %hu) index %hu exceeds size %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) controller opened
Airship [%{public}s:%d:%{public}s] creating mtr
Airship [%{public}s:%d:%{public}s] trid %hu has unmessaged lifecycle, closing
Airship [%{public}s:%d:%{public}s] context id %hu set as open
Airship [%{public}s:%d:%{public}s] (crid %hu) do not overwrite existing bad_cd buffer
Airship [%{public}s:%d:%{public}s] (trid %hu) new doorbell interval (%u us), new leeway (%u us)
Airship [%{public}s:%d:%{public}s] creating dispatch queue
Airship [%{public}s:%d:%{public}s] ring manager already in reset
Airship [%{public}s:%d:%{public}s] Enable BusLead and Memory
Airship [%{public}s:%d:%{public}s] image sent for ipc stage %s
Airship [%{public}s:%d:%{public}s] (trid %hu) moving queued transfers into pending state
Airship [%{public}s:%d:%{public}s] (crid %hu) new doorbell interval (%u us), new leeway (%u us)
Airship [%{public}s:%d:%{public}s] driver name: %s
Airship [%{public}s:%d:%{public}s] automatically placing driver in reset
Airship [%{public}s:%d:%{public}s] detaching from device
Airship [%{public}s:%d:%{public}s] (crid %hu) new availability blockers 0x%08x
Airship [%{public}s:%d:%{public}s] context id %hu has unmessaged lifecycle, closing
Airship [%{public}s:%d:%{public}s] IPC handshake timer expired
Airship [%{public}s:%d:%{public}s] (trid %hu) completing transfer tag %hu
Airship [%{public}s:%d:%{public}s] window base: 0x%llx, window size: 0x%llx
Airship [%{public}s:%d:%{public}s] recomputing closed ring availability
Airship [%{public}s:%d:%{public}s] sending open message for context id %hu
Airship [%{public}s:%d:%{public}s] activating doorbell coordinator with %u doorbell instances
Airship [%{public}s:%d:%{public}s] message success
Airship [%{public}s:%d:%{public}s] closing crid %hu
Airship [%{public}s:%d:%{public}s] failed to get device memory window config
Airship [%{public}s:%d:%{public}s] oversize host memory window reduced from %#llx to UINT32_MAX
Airship [%{public}s:%d:%{public}s] requesting close for crid %hu
Airship [%{public}s:%d:%{public}s] ipc status=%u
Airship [%{public}s:%d:%{public}s] (trid %hu) free transfers %hu must exceed dead space size %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) new device ring status=%u
Airship [%{public}s:%d:%{public}s] (crid %hu) invalid hi: %hu
Airship [%{public}s:%d:%{public}s] Initializing device
Airship [%{public}s:%d:%{public}s] updating context info address register
Airship [%{public}s:%d:%{public}s] region %s (id=%hu) cannot be used due to id conflict with name %s
Airship [%{public}s:%d:%{public}s] message success, setting state for region id %hu
Airship [%{public}s:%d:%{public}s] canceling timer
Airship [%{public}s:%d:%{public}s] type=%u, debug meta-data=0x%llx, name=%s
Airship [%{public}s:%d:%{public}s] sending close message for trid %hu
Airship [%{public}s:%d:%{public}s] creating tr controller for %s[%u]
Airship [%{public}s:%d:%{public}s] power flags changed to %u
Airship [%{public}s:%d:%{public}s] current blockers (%u), blockers cleared (%u)
Airship [%{public}s:%d:%{public}s] (trid %hu) invalid in-place completion at idx=%hu
Airship [%{public}s:%d:%{public}s] in_reset %u, activated %u
Airship [%{public}s:%d:%{public}s] setting up mcr
Airship [%{public}s:%d:%{public}s] driver added successfully
Airship [%{public}s:%d:%{public}s] tearing down current ipc stage
Airship [%{public}s:%d:%{public}s] ACIPC protocol error 0x%08x (%s)
Airship [%{public}s:%d:%{public}s] debugInfo capture start
Airship [%{public}s:%d:%{public}s] (crid %hu) cr terminated
Airship [%{public}s:%d:%{public}s] stopping context id %hu for reason %u
Airship [%{public}s:%d:%{public}s] (ctxid %hu) controller reset
Airship [%{public}s:%d:%{public}s] %s[%u] reset
Airship [%{public}s:%d:%{public}s] sending open message for crid %hu
Airship [%{public}s:%u:%{public}s] unexpected nonzero error code 0x%llx
Airship [%{public}s:%d:%{public}s] (bc %s) stopping boot controller
Airship [%{public}s:%d:%{public}s] stopping trid %hu for reason %u
Airship [%{public}s:%d:%{public}s] ring manager already out of reset
Airship [%{public}s:%d:%{public}s] crid %hu close message result %u
Airship [%{public}s:%d:%{public}s] (bc %s) detail=0
Airship [%{public}s:%d:%{public}s] (bc %s) sending image
Airship [%{public}s:%d:%{public}s] trid %hu set as open
Airship [%{public}s:%d:%{public}s] (bc %s) image sent, recomputing state
Airship [%{public}s:%d:%{public}s] acquiring resource %s
Airship [%{public}s:%d:%{public}s] creating boot controller for %s
Airship [%{public}s:%d:%{public}s] getting driver name
Airship [%{public}s:%d:%{public}s] (trid %hu) new availability blockers 0x%08x
Airship [%{public}s:%d:%{public}s] message failure
Airship [%{public}s:%d:%{public}s] cr_open %.*P
Airship [%{public}s:%d:%{public}s] ipc handshake complete
Airship [%{public}s:%d:%{public}s] updating cr close requests
Airship [%{public}s:%d:%{public}s] boot ipc stage name %s
Airship [%{public}s:%d:%{public}s] currentPower %u, pendingPower %u, device valid %s
Airship [%{public}s:%d:%{public}s] (bc %s) image_state=%u
Airship [%{public}s:%d:%{public}s] Added context id %hu
Airship [%{public}s:%d:%{public}s] crid %hu open message result %u
Airship [%{public}s:%d:%{public}s] power state change deadline expired
Airship [%{public}s:%d:%{public}s] (trid %hu) first transfer not found
Airship [%{public}s:%d:%{public}s] (trid %hu) failed to validate client override
Airship [%{public}s:%d:%{public}s] not ready for exec stage interrupt
Airship [%{public}s:%d:%{public}s] %s[%u] stopped
Airship [%{public}s:%d:%{public}s] destroying completion ring handle for crid %hu
Airship [%{public}s:%d:%{public}s] (crid %hu) registering interrupt and setting up index array signaler vector %hu
Airship [%{public}s:%d:%{public}s] context id %hu has unmessaged lifecycle, setting open
Airship [%{public}s:%d:%{public}s] device power off deadline expired
Airship [%{public}s:%d:%{public}s] (trid %hu) invalid ti: %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) update bad transfer completion
Airship [%{public}s:%d:%{public}s] updated exec stage: %u, current %u
Airship [%{public}s:%d:%{public}s] setting up mtr
Airship [%{public}s:%d:%{public}s] adding crid %hu flush tracking for trid %hu
Airship [%{public}s:%d:%{public}s] located completion ring configuration, adding %u instances
Airship [%{public}s:%d:%{public}s] invalid params
Airship [%{public}s:%d:%{public}s] driver create client end %s
Airship [%{public}s:%d:%{public}s] not ready for peripheral info interrupt
Airship [%{public}s:%d:%{public}s] entering device sleep
Airship [%{public}s:%d:%{public}s] failed to set client overrides for %s[%u]
Airship [%{public}s:%d:%{public}s] not in reset
Airship [%{public}s:%d:%{public}s] setting up message buffer for main ipc stage %s
Airship [%{public}s:%d:%{public}s] probing device
Airship [%{public}s:%d:%{public}s] region id %hu conflict %u
Airship [%{public}s:%d:%{public}s] creating new ring pool for completion ring %s
Airship [%{public}s:%d:%{public}s] (trid %hu) predecessor completion ID %hu does not equal completion ID %hu
Airship [%{public}s:%d:%{public}s] deferring message send
Airship [%{public}s:%d:%{public}s] requesting close for trid %hu
Airship [%{public}s:%d:%{public}s] setting up ipc status interrupt
Airship [%{public}s:%d:%{public}s] (trid %hu) failed: hi=%hu, ti=%hu
Airship [%{public}s:%d:%{public}s] (crid %hu) failed to complete transfer
Airship [%{public}s:%d:%{public}s] initializing driver
Airship [%{public}s:%d:%{public}s] image response %u, code %u
Airship [%{public}s:%d:%{public}s] (crid %hu) controller reset
Airship [%{public}s:%d:%{public}s] resuming doorbell coordinator
Airship [%{public}s:%d:%{public}s] capture streaming logs
Airship [%{public}s:%d:%{public}s] (trid %hu) state=%u, activated=%u
Airship [%{public}s:%d:%{public}s] handle_activate: result 0x%x
Airship [%{public}s:%d:%{public}s] (crid %hu) close complete
Airship [%{public}s:%d:%{public}s] enqueuing message in mtr
Airship [%{public}s:%d:%{public}s] trid %hu status %u
Airship [%{public}s:%d:%{public}s] no ipc stage set
Airship [%{public}s:%d:%{public}s] region id %hu sending memory map message
Airship [%{public}s:%d:%{public}s] reaping %s[%u]
Airship [%{public}s:%d:%{public}s] failed to look up configuration for %s
Airship [%{public}s:%d:%{public}s] (crid %hu) invalid completion descriptor at idx=%hu
Airship [%{public}s:%d:%{public}s] device is not active
Airship [%{public}s:%d:%{public}s] failed to flatten name/sel into string
Airship [%{public}s:%d:%{public}s] (ctxid %hu) controller state=%u, detail=%u
Airship [%{public}s:%d:%{public}s] (trid %hu) transfer tag %hu does not match next in-order tag %hu
Airship [%{public}s:%d:%{public}s] messenger already out of reset
Airship [%{public}s:%d:%{public}s] sending close message for context id %hu
Airship [%{public}s:%d:%{public}s] removing boot controller for ipc stage %s
Airship [%{public}s:%d:%{public}s] %s[%u] unavailable
Airship [%{public}s:%d:%{public}s] sending overflow messages
Airship [%{public}s:%d:%{public}s] crid %hu belongs to the same group as %hu
Airship [%{public}s:%d:%{public}s] main ipc state is not set
Airship [%{public}s:%d:%{public}s] (trid %hu) registering interrupt and setting up index array signaler vector %hu
Airship [%{public}s:%d:%{public}s] removing interrupt source %u
Airship [%{public}s:%d:%{public}s] crid %hu has unmessaged lifecycle, setting open
Airship [%{public}s:%d:%{public}s] updating context close requests
Airship [%{public}s:%d:%{public}s] deleted %hu items from mirror
Airship [%{public}s:%d:%{public}s] cannot set transport, %s ipc stage is not null
Airship [%{public}s:%d:%{public}s] mapping region of size %u for %s[%u]
Airship [%{public}s:%d:%{public}s] closing mcr
Airship [%{public}s:%d:%{public}s] copying peripheral info, initial exec stage value=%u
Airship [%{public}s:%d:%{public}s] power state not ready, setting transport blocker
Airship [%{public}s:%d:%{public}s] clearing power state not ready blocker
Airship [%{public}s:%d:%{public}s] creating new ring pool for transfer ring %s
Airship [%{public}s:%d:%{public}s] index %hu
Airship [%{public}s:%d:%{public}s] airship sw scaling %llu
Airship [%{public}s:%d:%{public}s] context id %hu close message requested
Airship [%{public}s:%d:%{public}s] Airship statedump complete: provided buffer size %u copied %u
Airship [%{public}s:%d:%{public}s] participant 0x%llx added to doorbell %s[%u]
Airship [%{public}s:%d:%{public}s] starting driver
Airship [%{public}s:%d:%{public}s] (crid %hu) reaping cr
Airship [%{public}s:%d:%{public}s] creating doorbell controller for %s[%u]
Airship [%{public}s:%d:%{public}s] resourceFileName=%s
Airship [%{public}s:%d:%{public}s] complete
Airship [%{public}s:%d:%{public}s] added %u instances of doorbell %s
Airship [%{public}s:%d:%{public}s] setting up boot ipc stage
Airship [%{public}s:%d:%{public}s] setting up message rings
Airship [%{public}s:%d:%{public}s] starting ipc handshake timer; timeout=%u ms
Airship [%{public}s:%d:%{public}s] Registering head index update handler for crid %hu at vector %hu
Airship [%{public}s:%d:%{public}s] processing completions
Airship [%{public}s:%d:%{public}s] syncing mcr head index update
Airship [%{public}s:%d:%{public}s] not ready to probe exec stage register
Airship [%{public}s:%d:%{public}s] sending open message for trid %hu
Airship [%{public}s:%d:%{public}s] probing exec stage register
Airship [%{public}s:%d:%{public}s] main ipc stage name %s
Airship [%{public}s:%d:%{public}s] entering host sleep
Airship [%{public}s:%d:%{public}s] (trid %hu) completions synthesized
Airship [%{public}s:%d:%{public}s] tearing down mcr
Airship [%{public}s:%d:%{public}s] associating crid %hu <-> trid %hu
Airship [%{public}s:%d:%{public}s] setting boot controller for ipc stage %s to unavailable
Airship [%{public}s:%d:%{public}s] already in reset
Airship [%{public}s:%d:%{public}s] object manager list not empty; dumping direct client objects
Airship [%{public}s:%d:%{public}s] driver create client begin %s
Airship [%{public}s:%d:%{public}s] failed to retrieve property '%s'
Airship [%{public}s:%d:%{public}s] (bc %s) image valid : %s 
Airship [%{public}s:%d:%{public}s] attaching pending device to driver
Airship [%{public}s:%d:%{public}s] unblocking device access
Airship [%{public}s:%d:%{public}s] (crid %hu) new device ring status=%u
Airship [%{public}s:%d:%{public}s] boot manager is already out of reset
Airship [%{public}s:%d:%{public}s] setting up callout notifier
Airship [%{public}s:%d:%{public}s] coordinator state=%u, new IPC stage=%s
Airship [%{public}s:%d:%{public}s] wake requested=%u, target host sleep=%u, permit device sleep=%u
Airship [%{public}s:%d:%{public}s] applied errata window_base_mask=%#llx, masked_base=%#llx
Airship [%{public}s:%d:%{public}s] stop reason %u
Airship [%{public}s:%d:%{public}s] (ctxid %hu) sending close message
Airship [%{public}s:%d:%{public}s] Deregistering tail index update handler for trid %hu at vector %hu
Airship [%{public}s:%d:%{public}s] power flags (%u), current IPC power state (%u)
Airship [%{public}s:%d:%{public}s] releasing ring with selector %u
Airship [%{public}s:%d:%{public}s] (trid %hu) first index %hu exceeds size %hu
Airship [%{public}s:%d:%{public}s] copying appendix
Airship [%{public}s:%d:%{public}s] invalid configuration: %s at %s
Airship [%{public}s:%d:%{public}s] cannot wake
Airship [%{public}s:%d:%{public}s] image has already been sent
Airship [%{public}s:%d:%{public}s] failed to aquire resource for %s
Airship [%{public}s:%d:%{public}s] starting power off deadline timer
Airship [%{public}s:%d:%{public}s] (trid %hu) attempt to consume %hu transfers, %hu fetched
Airship [%{public}s:%d:%{public}s] failed to allocate/map device memory
Airship [%{public}s:%d:%{public}s] stopping context id %hu
Airship [%{public}s:%d:%{public}s] setting trid %hu open
Airship [%{public}s:%d:%{public}s] (bc %s) out code=%u
Airship [%{public}s:%d:%{public}s] suspending doorbell coordinator
Airship [%{public}s:%d:%{public}s] region id %hu deferring unmap message
Airship [%{public}s:%d:%{public}s] device service does not match criteria
Airship [%{public}s:%d:%{public}s] pending IPC exec stage broadcast
Airship [%{public}s:%d:%{public}s] IPC power state callout enabled
Airship [%{public}s:%d:%{public}s] exiting host sleep
Airship [%{public}s:%d:%{public}s] no exec stage found for value %u
Airship [%{public}s:%d:%{public}s] clearing transport
Airship [%{public}s:%d:%{public}s] (crid %hu) stopping controller
Airship [%{public}s:%d:%{public}s] added trid %hu
Airship [%{public}s:%d:%{public}s] initializing PCI device
Airship [%{public}s:%d:%{public}s] failed to aquire resource for %s[%u]
Airship [%{public}s:%d:%{public}s] airship driver service is not active
Airship [%{public}s:%d:%{public}s] kIOServiceNotificationTypeTerminated
Airship [%{public}s:%d:%{public}s] crid: %u
Airship [%{public}s:%d:%{public}s] (bc %s) computing image table
Airship [%{public}s:%d:%{public}s] region id %hu sending unmap message
Airship [%{public}s:%d:%{public}s] stopping trid %hu
Airship [%{public}s:%d:%{public}s] sleep status: active
Airship [%{public}s:%d:%{public}s] value %u matches to exec stage: %s
Airship [%{public}s:%d:%{public}s] Airship error description: %s
Airship [%{public}s:%d:%{public}s] (bc %s) image address 0x%llx, length 0x%x
Airship [%{public}s:%d:%{public}s] creating mcr
Airship [%{public}s:%d:%{public}s] region id %hu exec stage mismatch %u
Airship [%{public}s:%d:%{public}s] exec stage reg value=%u
Airship [%{public}s:%d:%{public}s] main ipc state is not running (%u) or transport is not set
Airship [%{public}s:%d:%{public}s] set transport result 0x%x
Airship [%{public}s:%d:%{public}s] num of objects pending deletion %u
Airship [%{public}s:%d:%{public}s] boot manager exiting reset
Airship [%{public}s:%d:%{public}s] ts: last_write %llx, schedule %llx, deadline %llx, 
Airship [%{public}s:%d:%{public}s] created completion mirror object
Airship [%{public}s:%d:%{public}s] setting up peripheral info interrupt
Airship [%{public}s:%d:%{public}s] stopping provider
Airship [%{public}s:%d:%{public}s] platform_config=%u, probed viddid=0x%#x,  proxima_viddid=0x%#x
Airship [%{public}s:%d:%{public}s] sending close message for crid %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) open failed 0x%x
Airship [%{public}s:%d:%{public}s] requesting close for context id %hu
Airship [%{public}s:%d:%{public}s] new ipc status=%u
Airship [%{public}s:%d:%{public}s] current blockers (%u), set blockers (%u)
Airship [%{public}s:%d:%{public}s] insufficient buffer
Airship [%{public}s:%d:%{public}s] setting trid %hu closed
Airship [%{public}s:%d:%{public}s] device attach deadline expired
Airship [%{public}s:%d:%{public}s] (crid %hu) inserting completion with trid %hu and first tag %hu
Airship [%{public}s:%d:%{public}s] device : active %u, registered %u, power init complete %u
Airship [%{public}s:%d:%{public}s] setting context id %hu open
Airship [%{public}s:%d:%{public}s] adding %u instances of resource %s
Airship [%{public}s:%d:%{public}s] exec_stage during power-on=%u
Airship [%{public}s:%d:%{public}s] (ctxid %hu) open failed 0x%x
Airship [%{public}s:%d:%{public}s] (trid %hu) TR is now settled
Airship [%{public}s:%d:%{public}s] current main ipc stage and transport must be set
Airship [%{public}s:%d:%{public}s] boot manager is in reset
Airship [%{public}s:%d:%{public}s] (ctxid %hu) close complete
Airship [%{public}s:%d:%{public}s] setting up timer
Airship [%{public}s:%d:%{public}s] IPC driver state dump size %u
Airship [%{public}s:%d:%{public}s] (trid %hu) failed to find first transfer
Airship [%{public}s:%d:%{public}s] payload length %u, appendix length %u
Airship [%{public}s:%d:%{public}s] suspending transport
Airship [%{public}s:%d:%{public}s] boot manager is already in reset
Airship [%{public}s:%d:%{public}s] creating handle for completion ring with crid %u
Airship [%{public}s:%d:%{public}s] stopping crid %hu
Airship [%{public}s:%d:%{public}s] context id %hu in limbo
Airship [%{public}s:%d:%{public}s] creating handle for transfer ring with trid %u
Airship [%{public}s:%d:%{public}s] (trid %hu) seek %hu exceeds pending transfer count %hu
Airship [%{public}s:%d:%{public}s] activating %s[%u]
Airship [%{public}s:%d:%{public}s] running power state changed wait context
Airship [%{public}s:%d:%{public}s] unmapping memory region for %s[%u]
Airship [%{public}s:%d:%{public}s] driver ioservice params: ipcPowerOn %u ms, ipcPowerOff %u ms, devicePowerOn %u ms, devicePowerOff %u ms
Airship [%{public}s:%d:%{public}s] adding boot controller for ipc stage %s
Airship [%{public}s:%d:%{public}s] (bc %s) image response code=%u
Airship [%{public}s:%d:%{public}s] viddid=%#x
Airship [%{public}s:%d:%{public}s] %s[%u] old status %u, new status %u
Airship [%{public}s:%d:%{public}s] running power state change wait context
Airship [%{public}s:%d:%{public}s] setting external interrupt handler for vector %u
Airship [%{public}s:%d:%{public}s] (crid %hu) new interrupt %s[%u]
Airship [%{public}s:%d:%{public}s] crid %hu in limbo
Airship [%{public}s:%d:%{public}s] setting crid %hu open
Airship [%{public}s:%d:%{public}s] sleep status invalid
Airship [%{public}s:%d:%{public}s] Registering tail index update handler for trid %hu at vector %hu
Airship [%{public}s:%d:%{public}s] creating context controller for %s[%u]
Airship [%{public}s:%d:%{public}s] index %hu, message length %u
Airship [%{public}s:%d:%{public}s] stopping crid %hu for reason %u
Airship [%{public}s:%d:%{public}s] change to exec stage %s (%u) from %s
Airship [%{public}s:%d:%{public}s] (bc %s) no image response code
Airship [%{public}s:%d:%{public}s] (crid %hu) sending open message
Airship [%{public}s:%d:%{public}s] canceling power off deadline timer
Airship [%{public}s:%d:%{public}s] invoking exec stage change handler: %u
Airship [%{public}s:%d:%{public}s] tearing down mtr
Airship [%{public}s:%d:%{public}s] region %s (id=%hu) cannot be used due to name conflict with id %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) sending open message
Airship [%{public}s:%d:%{public}s] (trid %hu) unexpected flush notice from CRID %hu
Airship [%{public}s:%d:%{public}s] messenger failed to map mtr/mcr memory
Airship [%{public}s:%d:%{public}s] map successful
Airship [%{public}s:%d:%{public}s] %s[%u] state %u, detail 0x%u
Airship [%{public}s:%d:%{public}s] starting timer with interval (%u)
Airship [%{public}s:%d:%{public}s] (trid %hu) sending close message
Airship [%{public}s:%d:%{public}s] IPC driver state_dump complete
Airship [%{public}s:%d:%{public}s] saving overflow message
Airship [%{public}s:%d:%{public}s] added crid %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) controller closed
Airship [%{public}s:%d:%{public}s] consuming transfers
Airship [%{public}s:%d:%{public}s] reset type %u
Airship [%{public}s:%d:%{public}s] trid %hu has unmessaged lifecycle, setting open
Airship [%{public}s:%d:%{public}s] crid %hu is associated with trid %hu
Airship [%{public}s:%d:%{public}s] no devices to attach to
Airship [%{public}s:%d:%{public}s] ring manager is in reset
Airship [%{public}s:%d:%{public}s] setting context id %hu closed
```
