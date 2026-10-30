# `/System/Library/PrivateFrameworks/Airship.framework/Airship`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 968,880 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 2272)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (4)

- `/System/Library/PrivateFrameworks/Airship.framework/Airship (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (1,607)

```
BUG in client of Airship: attempt to reconfigure active TR
device_memory.cpp
[%s:%d:%s] (crid %hu) cr terminated
[%s:%d:%s] Deregistering tail index update handler for trid %hu at vector %hu
reap
[%s:%d:%s] controller ipc stage: %s
instance count is zero
synchronized
airship-read-before-sleep-update
[%s:%d:%s] airship sw scaling %llu
[%s:%d:%s] (bc %s) computing image table
set_interrupt_handler
accumulation
[%s:%d:%s] unknown proxima-platform: %llu
[%s:%d:%s] creating new ring pool for transfer ring %s
BUG in Airship: unexpected flush notice
stop_tr
destroy_handle
handle_append_ipc_driver_state_dump
cr_ring.cpp
BUG in Airship: attempted to insert null value into boxed dictionary
[%s:%d:%s] stopping context id %hu for reason %u
[%s:%d:%s] crid %hu is associated with trid %hu
[%s:%d:%s] reset=%u, boot_state=%s, ipc_state=%s
direct_client_object
[%s:%d:%s] (crid %hu) invalid hi: %hu
value out of bounds
[%s:%d:%s] boot ipc stage name %s
[%s:%d:%s] (bc %s) out code=%u
write_head_index
[%s:%d:%s] (trid %hu) invalid ti: %hu
ambiguous value
completion_group_stride
uplink-update-failure
ipc-running-timeout
not privileged
buffer_array
[%s:%d:%s] exiting reset
[%s:%d:%s] (crid %hu) inserting completion with trid %hu and first tag %hu
image_table
get_current_ipc_stage_name
remove_flusher
~driver_resource
direct_context.cpp
[%s:%d:%s] cannot set transport, %s ipc stage is not null
~driver_object
BUG in Airship: invalid dst
[%s:%d:%s] (trid %hu) attempt to consume %hu transfers, %hu fetched
BUG in client of Airship: attempted to activate already-active CR
activate
[%s:%d:%s] (trid %hu) open failed 0x%x
open_context
[%s:%d:%s] (trid %hu) tag %hu must belong to first in chain
[%s:%d:%s] (bc %s) no image response code
direct_cr_controller.cpp
tr_ring
[%s:%d:%s] acquiring resource %s
set_cr_closed
[%s:%d:%s] context id %hu open message result %u
set_notifier
set_transfer_footer_size
ipc_reset_occurred
[%s:%d:%s] image response %u, code %u
check_all_cr_close_requests
[%s:%d:%s] updating cr close requests
[%s:%d:%s] (crid %hu) stopping controller
ring_header_footer_scaling
enable_interrupt_vector
finish_queued_partial_chain
remove
BUG in Airship: wrong index
[%s:%d:%s] closing context id %hu
[%s:%d:%s] closing mtr
create_client
memregion_controller
start
BUG in Airship: attempted to activate active object
[%s:%d:%s] IPC driver state_dump complete
max
[%s:%d:%s] tearing down current ipc stage
[%s:%d:%s] copying message payload
bind_active_object
~interrupt
[%s:%d:%s] removing interrupt source %u
BUG in client of Airship: Failed to locate transfer ring config
add_participant
[%s:%d:%s] stopping boot controller for ipc stage %s
[%s:%d:%s] wake requested=%u, target host sleep=%u, permit device sleep=%u
BUG in Airship: oversize ring
set_mode
device-signalled error
[%s:%d:%s] failed to get resource
[%s:%d:%s] removed crid %hu
unmap_region
boot_controller
BUG in client of Airship: attempted to reconfigure active CR
[%s:%d:%s] trid %hu close message requested
[%s:%d:%s] removing boot controller for ipc stage %s
window_base_mask
[%s:%d:%s] not ready for exec stage interrupt
[%s:%d:%s] payload length %u, appendix length %u
[%s:%d:%s] syncing mtr tail index update and fetching completions
set_mirror_enabled
[%s:%d:%s] (trid %hu) update bad transfer completion
create
success_code
resources
[%s:%d:%s] current main ipc stage and transport must be set
[%s:%d:%s] value %u matches to exec stage: %s
[%s:%d:%s] sw timeout scale for proxima protium platform: %llu
BUG in client of Airship: attempted to activate already-active TR
transfer_queue
release_image_transfer_resources
remove_participant
~direct_cr_controller
setup_interrupt
mem_write32
transfer_header_size
[%s:%d:%s] change to exec stage %s (%u) from %s
get_source_maintenance_in_progress
BUG in Airship: access to non-held resource
swizzle_proxima_viddid_for_platform
[%s:%d:%s] (trid %hu) moving queued transfers into pending state
BUG in Airship: list element destroyed while in list
cr_open_message_completed
[%s:%d:%s] sending close message for context id %hu
boot_manager.cpp
[%s:%d:%s] main ipc state is not set
add_region
[%s:%d:%s] (bc %s) detail=0
[%s:%d:%s] (trid %hu) close complete
append_bytes
[%s:%d:%s] closing crid %hu
response code is ambiguous
ipc_handshake_timeout_occurred
arm_cr_index_vector
bad-cr-hi-update
config_from_doorbell_spec
group_stride
BUG in client of Airship: attempted to reconfigure active interrupt
[%s:%d:%s] boot manager exiting reset
acipc_get_health_status
deregister_cr_index_vector_action
get_element
set_external_execution_queue
get_completed_transfer_count
BUG in client of Airship: attempted to access inactive mirror
BUG in client of Airship: attempted to access inactive driver
validate_buffer_bounds
create_cr_controller
create_debug_object
register_cr_index_vector_action
[%s:%d:%s] resuming doorbell coordinator
acipc
update_mem_window_base_and_size
write_index_array
BUG in client of Airship: attempted to activate active interrupt
connect_interrupt
t2026
get_first_completed_tag
[%s:%d:%s] creating handle for completion ring with crid %u
~direct_client_object
BUG in Airship: attempted to create client for terminated driver
[%s:%d:%s] crid %hu has unmessaged lifecycle, setting closed
[%s:%d:%s] creating doorbell controller for %s[%u]
unregister_client_statedump_handler
round_up_to_page_size
[%s:%d:%s] tearing down boot ipc stage
disconnect_interrupt
move_transfers
[%s:%d:%s] %s[%u] unavailable
append_context_state_dump
cr_controller
[%s:%d:%s] copying peripheral info, initial exec stage value=%u
does_region_conflict_with_any_mapped_region
[%s:%d:%s] message failed, setting state for region id %hu
set_client_overrides
create_device_memory_mapping
check_all_context_close_requests
[%s:%d:%s] added crid %hu
boot_ipc_stages
[%s:%d:%s] (trid %hu) completing transfer tag %hu
existing_for_str
set_context_open
BUG in client of Airship: attempted to activate already-active memregion
[%s:%d:%s] creating new ring pool for completion ring %s
[%s:%d:%s] updated exec stage: %u, current %u
compute_hdrftr_size_fields
[%s:%d:%s] map successful
cr_close_message_completed
[%s:%d:%s] stopping trid %hu
BUG in Airship: attempted to initialize optional with sentinel value
[%s:%d:%s] (crid %hu) reaping cr
update_ipc_control_register
activate_block_invoke
get_inorder_tag_for_enqueue
BUG in client of Airship: attempted to retrieve first completed tag of ring without completed transfers
main
unregister_statedump_collection_handler
[%s:%d:%s] creating memregion controller for %s[%u]
ring_size
invalid completion style
update_sleep_control_register
save_overflow_message
BUG in client of Airship: mode must be AIRSHIP_ACIPC_TR_MODE_STANDARD
[%s:%d:%s] boot manager is already in reset
get_image_response
[%s:%d:%s] (bc %s) old state=0x%llx, new state=0x%llx
~intrusive_list_link
[%s:%d:%s] ring manager already in reset
~driver_object_manager
channel-sync-failure
[%s:%d:%s] boot manager is in reset
[%s:%d:%s] new ipc stage: %s
[%s:%d:%s] index %hu
CentauriAlpha
value exceeds ipc stage limit
[%s:%d:%s] message failure
[%s:%d:%s] (trid %hu) free=%hu, queued=%hu, pending=%hu, completed=%hu, fetched=%hu
set_ipc_error_handler
image_address_hi
sleep_state_machine
[%s:%d:%s] window_base=%#llx, size=%#llx
[%s:%d:%s] region id %hu exec stage mismatch %u
compute_offsets
get_and_advance_inorder_idx_for_enqueue
[%s:%d:%s] platform_config=%u, probed viddid=0x%#x,  proxima_viddid=0x%#x
[%s:%d:%s] failed to get device memory window config
get_proxima_platform
BUG in Airship: invalid tail index update operation
BUG in Airship: attempted to create cr_controller in driver_client
request_region_unmap
BUG in client of Airship: attempt to reconfigure active context
[%s:%d:%s] (trid %hu) seek %hu exceeds pending transfer count %hu
debug_infra.hpp
teardown_current_ipc_stage
[%s:%d:%s] (ctxid %hu) failed to validate client override
[%s:%d:%s] creating mcr
CentauriControl
cldma-rx-error
probe
consume_mirror_elements
BUG in Airship: attempted to create boxed string from null C string
request_context_close
[%s:%d:%s] (ctxid %hu) reaping context controller
buffer
traffic_class
Vendor
setup_boot_ipc_stage
BUG in Airship: attempted to activate object without required configuration
[%s:%d:%s] context_open 
parse_optional
[%s:%d:%s] message canceled
[%s:%d:%s] (trid %hu) registering doorbell %s, selector %u
with_str
create_interrupt
[%s:%d:%s] setting crid %hu open
[%s:%d:%s] tearing down mtr
[%s:%d:%s] in_reset %u, activated %u
set_doorbell_moderation
~reaper_target
set_map_clientdata
recompute_state
driver.cpp
set_transport
[%s:%d:%s] setting trid %hu open
main_ipc_state_machine
BUG in client of Airship: out of bounds access to buffer
BUG in Airship: attempted to access terminated driver
[%s:%d:%s] %s[%u] reset
read_tail_index
unknown result code
[%s:%d:%s] trid %hu status %u
ambiguous name
save_transfer_completion
refresh_mapping
schedule_update
append_tr_index_info
BUG in client of Airship: attempted to activate active driver
not ready
async_accelerator_private.cpp
send_memory_unmap_message
downlink-update-failure
compute_io_status_for_transfers
probe_image_response
BUG in Airship: bad parameter - 'footer_length'
BUG in Airship: access to null buffer mapping
[%s:%d:%s] context id %hu close message result %u
unexpected mode string
[%s:%d:%s] (trid %hu) stopping controller
[%s:%d:%s] ring manager is in reset
[%s:%d:%s] setting up mcr
create_tr_controller
completion_rings
[%s:%d:%s] entering host sleep
BUG in Airship: attempted to activate canceled object
BUG in Airship: attempted to activate terminated driver
BUG in client of Airship: attempted to access inactive CR
reset
index
image_address_lo
[%s:%d:%s] oversize host memory window reduced from %#llx to UINT32_MAX
[%s:%d:%s] msi stats overflow: resetting count for vector %u
[%s:%d:%s] (bc %s) checking for image response
advance_buffer_pointer
tr_close_message_completed
BUG in client of Airship: attempted to activate canceled monitor
[%s:%d:%s] stopping crid %hu for reason %u
add_controller
[%s:%d:%s] failed to look up configuration for %s
[%s:%d:%s] boot manager is already out of reset
driver_object.cpp
~interrupt_manager
BUG in Airship: requested CD element is inactive
[%s:%d:%s] context id %hu close message requested
mode
add_handler
exit_reset
[%s:%d:%s] handle_activate: result 0x%x
[%s:%d:%s] (crid %hu) registering interrupt and setting up index array signaler vector %hu
arm_tr_index_vector
io-timeout
[%s:%d:%s] activating %s[%u]
~state_dump_manager
dump_pending_transfer_stats
out-of-place completion requires completion ring
append
set_settled
BUG in client of Airship: attempted to reconfigure active memregion
send_message
channel-update-failure
direct_client_object.cpp
[%s:%d:%s] viddid=%#x
[%s:%d:%s] (trid %hu) free transfers %hu must exceed dead space size %hu
[%s:%d:%s] reaping %s[%u]
BUG in Airship: refcount_mixin retained after release
wait
populate_context_info
[%s:%d:%s] unknown device viddid=%#x
get_state
request_tr_close
[%s:%d:%s] sending close message for trid %hu
finalize_indices
window_size
~messenger
device-sleep-exit-timeout
set_completion_footer_size
BUG in client of Airship: attempted to set external interrupt handler for inactive driver
cr_ring
retain
???
remove_context
group
[%s:%d:%s] setting up main ipc stage
set_tr_open
[%s:%d:%s] setting boot controller for ipc stage %s to unavailable
auxiliary_contexts
devmem_mapping
unsupported register width
handle_enter_reset
teardown_boot_ipc_stage
set_source_maintenance_completion_handler
BUG in Airship: attempted truncate to larger size
memregion_controller.cpp
ring_index_pair
with_format
direct_buffer.cpp
get_prev_transfer_in_queue
ring_pool
direct_monitor.cpp
 %02x
[%s:%d:%s] no custom statedump handlers registered
selector
shared_counter
reduce_size
sync_action_process_ti_update
[%s:%d:%s] (trid %hu) unexpected flush notice from CRID %hu
bad argument
write_tail_index
copy_to
[%s:%d:%s] (trid %hu) completing chain
already in use (exclusive access)
send_tr_open_message
[%s:%d:%s] crid %hu has unmessaged lifecycle, setting open
[%s:%d:%s] trid %hu is settled
[%s:%d:%s] cr_open 
unexpected object type
errata
invalid value
[%s:%d:%s] failed to flatten name/sel into string
reap_single_DROPS_LOCK
window_base_hi
handle_clear_transport
context_controller_block_invoke
[%s:%d:%s] (ctxid %hu) controller reset
driver_object
[%s:%d:%s] deleted %hu items from mirror
mtr
get_value
add_cr
[%s:%d:%s] setting context id %hu open
[%s:%d:%s] trid %hu open message result %u
[%s:%d:%s] index %hu, message length %u
[%s:%d:%s] sending any overflow messages
BUG in client of Airship: attempted to access inactive TR
BUG in Airship: unaligned device memory access
[%s:%d:%s] (trid %hu) new availability blockers 0x%08x
[%s:%d:%s] notifying crid %hu that trid %hu is settled
completion_group
timedwait
[%s:%d:%s] exec stage reg value=%u
ring_controller.cpp
context_controller
[%s:%d:%s] trid %hu has unmessaged lifecycle, closing
configurator.cpp
register
completion_footer_size
device sleep
[%s:%d:%s] num of objects pending deletion %u
v12@?0I8
set_power_target
acipc_create_doorbell_controller
[%s:%d:%s] creating context controller for %s[%u]
sleep_control
virtual
[%s:%d:%s] exiting host sleep
~client_interrupt
[%s:%d:%s] (bc %s) image valid : %s 
airship_acipc_tr_disconnect
populate_descriptor
missing object
[%s:%d:%s] (trid %hu) new mode (%u)
[%s:%d:%s] removing participant 0x%llx from pending queue
update_power_state
BUG in client of Airship: attempted to set interrupt execution queue for terminated driver
open
sync
[%s:%d:%s] (trid %hu) failed to validate client override
retain_obj
tr_settled
~reaper
read_exec_stage_register
[%s:%d:%s] stop reason %u
BUG in client of Airship: attempted to activate interrupt with event handlers but without queue
BUG in Airship: attempted to retrieve max message length in reset
exec_stage_interrupt
static_array.hpp
[%s:%d:%s] (ctxid %hu) controller state=%u, detail=%u
read
[%s:%d:%s] object manager list not empty; dumping direct client objects
set_ipc_error_flags
set_availability_blockers
get_page_size
no space for data
reaper.cpp
[%s:%d:%s] (crid %hu) controller reset
constraints not satisfied by default
BUG in Airship: attempted to add duplicate resource
BUG in client of Airship: selector is invalid
driver_debug_object.hpp
vector
[%s:%d:%s] synthesizing completions if needed
release
truncate
fixup_remain_count
find_exec_stage_with_value
acquire_resource
[%s:%d:%s] tearing down mcr
[%s:%d:%s] coordinator state=%u, new IPC stage=%s
[%s:%d:%s] setting up message rings
insert
get_paddr
stop
[%s:%d:%s] no exec stage found for value %u
find_completion_target
is_healthy
validate_client_overrides
tr_open_message_completed
setup_main_ipc_stage
[%s:%d:%s] IPC handshake timer expired
memregion_manager.cpp
get_vector_for_interrupt
[%s:%d:%s] setting external interrupt handler for vector %u
[%s:%d:%s] (bc %s) image_state=%u
%s %s@%u
[%s:%d:%s] failed to find stage for value, %u
BUG in Airship: attempted message send in reset
[%s:%d:%s] (trid %hu) predecessor state %u does not valid
set_size
[%s:%d:%s] destroying transfer ring handle for trid %hu
[%s:%d:%s] located transfer ring configuration, adding %u instances
v16@?0^v8
sync_action_flush_pending_transfers
general error
clear_tr_indices
[%s:%d:%s] participant 0x%llx added to doorbell %s[%u]
setup_tr_settlement_tracking
[%s:%d:%s] stopping crid %hu
acipc_driver.cpp
ipc_status_interrupt_occurred
wait_context.cpp
BUG in client of Airship: attempted to activate active monitor
[%s:%d:%s] reset type=%u
unknown context
interrupt_stride
[%s:%d:%s] invalid configuration: %s at %s
downlink-buffer-count-len-error
system-failure
get_maintenance_in_progress
[%s:%d:%s] (trid %hu) failed to find first transfer
BUG in Airship: bad optional access
[%s:%d:%s] failed to set client overrides for %s[%u]
[%s:%d:%s] sending open message for context id %hu
transfer_ring_opened
~ring_manager
close_context
tr_index_count
role
clear_transport
ensure_free_space
nominal_state_dump_size
None
unknown-error
process_pending
BUG in Airship: invalid src
set_configuration
[%s:%d:%s] creating cr controller for %s[%u]
unknown
compute_free_space
doorbell_timer_tolerance_us
completion_ring_stride
[%s:%d:%s] type=%u, debug meta-data=0x%llx, name=%s
BUG in Airship: requested TD element is inactive
doorbell_moderation
[%s:%d:%s] region id %hu removing memregion_controller
set_device_region_status
optional.hpp
BUG in Airship: bad parameter - 'size'
send_cr_close_message
[%s:%d:%s] added trid %hu
[%s:%d:%s] message success
BUG in Airship: attempted to insert element already in list
with_cstr_nocopy
skip_window_configuration
ipc_control
exec_stage_interrupt_occurred
BUG in Airship: attempted to reconfigure active object
unexpected-transport-revocation
[%s:%d:%s] messenger failed to map mtr/mcr memory
get_first_free_tag
unmap
BUG in Airship: attempted access to terminated client
remove_cr
update_head_index
check_for_image_response
with_cstr
send_context_open_message
boot
reserve_next
BUG in client of Airship: attempted to create client for inactive driver
resource_stride
image_response
set_cancel_handler
BUG in client of Airship: selector is not available
acipc.cpp
debug
is_ipc_status_valid
[%s:%d:%s] syncing mcr head index update
[%s:%d:%s] releasing ring with selector %u
register_client_statedump_handler
completion_mirror
BUG in Airship: invalid tail index advance operation
~monitor_target
peripheral_info_interrupt
populate_state_dump_info
[%s:%d:%s] entering device sleep
direct_tr_controller.cpp
[%s:%d:%s] dbs : total %lu, active %lu, pending %d
refcount_mixin.hpp
create_exec_stage_monitor
context_controller.cpp
set_device_context_status
consume_elements
Role
complete_transfer
set_exec_stage_change_handler
state_dump_manager.cpp
BUG in client of Airship: attempted to unregister handler for terminated driver
ipc_status_interrupt
constraints
create_handle
unexpected-sleep-status
operator[]
queue
capability
device_classifier.cpp
[%s:%d:%s] (trid %hu) registering interrupt and setting up index array signaler vector %hu
memory_map_message_completed
[%s:%d:%s] messenger already out of reset
flush_queued_transfers
Centauri
~driver
BUG in client of Airship: invalid queue role
BUG in client of Airship: attempted to await inactive monitor
[%s:%d:%s] (crid %hu) registering with doorbell coordinator with doorbell %s
transfer_footer_size
completion_header_size
[%s:%d:%s] region %s (id=%hu) cannot be used due to id conflict with name %s
unknown target
read_cr_head_index
messenger.cpp
get_and_advance_inorder_idx_for_completion
[%s:%d:%s] already in reset
[%s:%d:%s] opening mcr
uint64_value
notify_transfer_ring_when_flushed
[%s:%d:%s] (crid %hu) sending close message
handle_probe_exec_stage
[%s:%d:%s] setting up boot ipc stage
dump_list
proxima-platform
BUG in Airship: attempted to use inactive object
[%s:%d:%s] requesting close for context id %hu
[%s:%d:%s] crid %hu is not associated with any open trs
limits
[%s:%d:%s] no ipc stage set
direct_memregion.cpp
[%s:%d:%s] %s[%u] old status %u, new status %u
typed_delete
mem_write16
transfer_rings
raise_ipc_error
read_register
timeout
airship_platform_get_fallback_queue_block_invoke
ipc_stage
dal25
ring_pool.cpp
[%s:%d:%s] sending open message for crid %hu
multi
[%s:%d:%s] region id %hu sending unmap message
read_tr_tail_index
BUG in client of Airship: Unsupported mode: AIRSHIP_ACIPC_TR_MODE_BATCH (missing IOUserNetworkPacket)
enqueue_transfer
completion_ring_will_flush
boxed_types.cpp
BUG in client of Airship: attempted to activate monitor with event handlers but without queue
set_image_sent
[%s:%d:%s] failed to aquire resource for %s
set_tr_closed
[%s:%d:%s] Added context id %hu
[%s:%d:%s] context id %hu status %u
in-place completion requires in-order
[%s:%d:%s] Registering head index update handler for crid %hu at vector %hu
[%s:%d:%s] starting messenger
multicomp_find_first_transfer
[%s:%d:%s] (bc %s) adding controller to boot manager
BUG in Airship: ring size cannot be zero
image_size
value exceedes auxiliary context limit
clear_cr_indices
no-error
[%s:%d:%s] failed to look up configuration for %s[%u]
index_array_vector
chipset
[%s:%d:%s] ipc status=%u
BUG in client of Airship: attempted to activate canceled interrupt
cldma-link-error
system-error
BUG in client of Airship: attempted to overwrite driver transport
mem_read32
remove_tr
%s-%u
read_head_index
flush_with_action
~monitor
[%s:%d:%s] (trid %hu) failed: hi=%hu, ti=%hu
count_intersection
[%s:%d:%s] region id %hu conflict %u
resource
write_register
[%s:%d:%s] (trid %hu) new device ring status=%u
bytes
invalid alignment
BUG in client of Airship: attempted to unregister handler for inactive driver
enqueue_message_in_mtr
Chipset
send_memory_map_message
[%s:%d:%s] message success, setting state for region id %hu
send_overflow_messages
[%s:%d:%s] (bc %s) reseting boot controller
[%s:%d:%s] ring manager already out of reset
destroy_client
[%s:%d:%s] (trid %hu) failed to complete transfer tag %hu
[%s:%d:%s] crid %hu status %u
driver_ioservice_params
[%s:%d:%s] acipc driver activate complete
direct_interrupt.cpp
operator()
BUG in Airship: attempted to create tr_controller in direct_client
[%s:%d:%s] removed context id %hu
acipc_create_boot_controller
[%s:%d:%s] updating context info address register
[%s:%d:%s] (ctxid %hu) stopping controller
[%s:%d:%s] Registering tail index update handler for trid %hu at vector %hu
device_memory.hpp
ring_manager.cpp
send_tr_close_message
window_base_lo
change_to_ipc_stage
[%s:%d:%s] invoking action
monitor.cpp
[%s:%d:%s] (trid %hu) sending close message
buffer_create
[%s:%d:%s] (trid %hu) transfer tag %hu does not match next in-order tag %hu
copy_debug_info
airship-sw-timeout-scale
client_registers
advance_tail_index
sleep-failure
[%s:%d:%s] value for shared constant doorbell: %u
create_state_monitor
close_tr
failure_code
cr_index_count
tr_controller.cpp
shared_timestamp
[%s:%d:%s] sleep status invalid
[%s:%d:%s] getting transfer completion for tag %hu
[%s:%d:%s] (trid %hu) first transfer not found
[%s:%d:%s] (trid %hu) completions synthesized
bounds overflow
add_flusher
BUG in client of Airship: attempted to activate already-active context
[%s:%d:%s] driver create client begin %s
[%s:%d:%s] trid %hu set as open
com.apple.airship.global-fallback
nominal_transfer_size
[%s:%d:%s] starting ipc handshake timer; timeout=%u ms
nil
bad-cd
set_power_state_change_handler
update_tail_index
register_tr_index_vector_action
v8@?0
BUG in client of Airship: attempted to set external interrupt handler for terminated driver
with_capacity
merge_location
[%s:%d:%s] enqueuing message in mtr
doorbell_coordinator
[%s:%d:%s] opening mtr
host-sleep-failure
clear_context
[%s:%d:%s] (crid %hu) open failed 0x%x
context_info_address_hi
[%s:%d:%s] (trid %hu) first index %hu exceeds size %hu
create_free_space_monitor
ipc_status
deregister_tr_index_vector_action
[%s:%d:%s] created completion mirror object
acquire
send_image
classify_image_response_code
context_close_message_completed
width
peripheral_info_interrupt_occurred
[%s:%d:%s] (trid %hu) new interrupt %s[%u]
set_interrupt
[%s:%d:%s] (crid %hu) new interrupt %s[%u]
BUG in Airship: attempted to find existing boxed symbol from null string
[%s:%d:%s] crid %hu close message result %u
recompute_region_availability
memory_unmap_message_completed
get_time_metadata
[%s:%d:%s] (bc %s) detail=%u
[%s:%d:%s] (trid %hu) transfer flush failed
~cr_controller
memory_regions
interrupt.cpp
[%s:%d:%s] reserving ring with selector %u
[%s:%d:%s] crid: %u
[%s:%d:%s] (trid %hu) TR is now settled
vendor
size
async_callback
process_completions
[%s:%d:%s] activating doorbell coordinator with %u doorbell instances
[%s:%d:%s] not ready for peripheral info interrupt
set_context_closed
[%s:%d:%s] requesting close for trid %hu
create_sync_monitor
[%s:%d:%s] copying appendix
suspend
change_to_exec_stage
[%s:%d:%s] exec stage interrupt occurred: value %u
[%s:%d:%s] (ctxid %hu) open failed 0x%x
[%s:%d:%s] (trid %hu) create tx_queue: size %hu, hdrlen %u, ftrlen %u, out-of-order %u
[%s:%d:%s] (bc %s) stopping boot controller
BUG in Airship: bad array access
set_open_clientdata
get_mirror_count
[%s:%d:%s] trid %hu in limbo
name
[%s:%d:%s] region id %hu sending memory map message
BUG in Airship: flat array size multiplication overflow
[%s:%d:%s] entering reset, dropping any pending doorbells
ALLOCATION FAILURE (or BUG) in Airship
process_completion_descriptors
~async_accelerator
[%s:%d:%s] region %s (id=%hu) cannot be used due to name conflict with id %hu
append_outstanding_transfer_state
bank
device_transport.cpp
BUG in Airship: bad parameter - 'header_length'
get_addr
[%s:%d:%s] sending open message for trid %hu
[%s:%d:%s] boot manager entering reset
[%s:%d:%s] sleep status: %s
trigger_async
set_device_ring_status
scribble_descriptor
[%s:%d:%s] context id %hu has unmessaged lifecycle, closing
ring_index_pair.hpp
[%s:%d:%s] creating mtr
[%s:%d:%s] consuming transfers
direct_client.cpp
add_doorbells
completion_ring_did_flush
acipc_driver_client.cpp
unknown keys present
[%s:%d:%s] updating register at bank=%u, offset=%u
trigger
print_queue_stats
[%s:%d:%s] reserve %u complete
get_queue
mcr
BUG in client of Airship: Failed to locate completion ring config
update_exec_stage
mem_read
BUG in Airship: attempted to access boxed dictionary with null key
operation canceled
close_cr
check_async
[%s:%d:%s] reset type %u
traffic_wake
[%s:%d:%s] region id %hu adding memregion_controller
set_backing_ring_size
[%s:%d:%s] (crid %hu) new doorbell interval (%u us), new leeway (%u us)
BUG in Airship: Attempted to perform a health check in driver_client
[%s:%d:%s] crid %hu belongs to the same group as %hu
get_health_status
[%s:%d:%s] ACIPC protocol error 0x%08x (%s)
[%s:%d:%s] region id %hu deferring unmap message
[%s:%d:%s] creating handle for transfer ring with trid %u
get_flattened_name_sel_string
platform_private.cpp
<nil>
append_cr_index_info
reserve
BUG in Airship: size is too big
BUG in Airship: refcount_mixin retain overflow
header_size
interrupt_occurred
resume
~tr_controller
[%s:%d:%s] (crid %hu) failed to validate client override
completion_ring
chain
get_mirror_element
[%s:%d:%s] region id %hu is in limbo, attempting to unmap
base.cpp
BUG in client of Airship: attempted to access inactive interrupt
set_interrupt_execution_queue
stop_context
context_info_address_lo
map_region
add
false
enter_reset
BUG in client of Airship: attempted to reconfigure active monitor
[%s:%d:%s] result=0x%x
log
~driver_object_termination_list
[%s:%d:%s] setting up mtr
[%s:%d:%s] setting up message buffer for main ipc stage %s
BUG in client of Airship: externally managed ring
BUG in Airship: _memory is NULL
BUG in Airship: attempted to create boxed symbol from null string
[%s:%d:%s] crid %hu open message result %u
device_info
main_ipc_stages
teardown_main_ipc_stage
[%s:%d:%s] applied errata window_base_mask=%#llx, masked_base=%#llx
get_next_transfer_in_queue
[%s:%d:%s] sleep status: host sleep
~devmem_mapping
[%s:%d:%s] added %u instances of doorbell %s
unknown ipc stage
exec_stages
BUG in Airship: invalid head index advance operation
channel-quiesce-failure
~ring_pool
BUG in Airship: out of bounds access to boxed array
add_context
[%s:%d:%s] trid %hu has unmessaged lifecycle, setting open
[%s:%d:%s] (trid %hu) offset %hu exceeds fetched transfer count %hu
[%s:%d:%s] crid %hu in limbo
parse_symbol
parse_number
[%s:%d:%s] exec_stage during power-on=%u
synthesize_reset_completions
[%s:%d:%s] (crid %hu) trid %hu does not accept completions from this cr
acipc_create_context_controller
multicomp_complete_prior_transfers
BUG in client of Airship: attempted to reconfigure active TR
[%s:%d:%s] (trid %hu) controller opened
set_value
set_exec_stage
flush_tr_settlement
[%s:%d:%s] setting crid %hu closed
priority
BUG in client of Airship: attempted to register handler for terminated driver
BUG in Airship: invalid head index update operation
airship-trap-on-acipc-error
update_context_info_addr_registers
[%s:%d:%s] creating boot controller for %s
~direct_client_object_manager
disable_interrupt_vector
intrusive_list.hpp
emplace_back
airship-debug
[%s:%d:%s] creating tr controller for %s[%u]
id
dump_object_info
[%s:%d:%s] entering reset
[%s:%d:%s] sending overflow messages
[%s:%d:%s] (trid %hu) do not overwrite existing bad tx completion buffer
device error
update_completion_desc_debug_info
[%s:%d:%s] sleep status: active
cldma-tx-error
[%s:%d:%s] (crid %hu) sending open message
set_external_handler
is_cr_completion_context_for_tr
[%s:%d:%s] stopping trid %hu for reason %u
parse
write_cr_tail_index
[%s:%d:%s] (trid %hu) transfer at index %hu is in state %u
[%s:%d:%s] suspending doorbell coordinator
set_queue
release_resource
non-default completion group requires out-of-order
async_notifier.cpp
set_maintenance_completion_notifier
BUG in client of Airship: attempted to register handler for inactive driver
context_open_message_completed
doorbells
[%s:%d:%s] setting up peripheral info interrupt
append_element
open_cr
setup_notifier
[%s:%d:%s] failed to allocate/map device memory
copy_and_zerofill
get_max_message_length
[%s:%d:%s] no handles available in pool
unexpected-ipc-status
BUG in client of Airship: nonzero selector for NULL resource
process_inplace_completions
[%s:%d:%s] removed trid %hu
[%s:%d:%s] tr_open 
[%s:%d:%s] context id %hu set as open
[%s:%d:%s] processing completions
[%s:%d:%s] setting trid %hu closed
doorbell_stride
[%s:%d:%s] timer deadline missed!!
[%s:%d:%s] (crid %hu) controller opened
ipc_running_timeout
typed_allocators.cpp
is_cr_required_completion_context_for_any_open_tr
[%s:%d:%s] (crid %hu) invalid completion descriptor at idx=%hu
BUG in client of Airship: attempted to access inactive context
get_free_space
[%s:%d:%s] mapping region of size %u for %s[%u]
release_obj
send_context_close_message
shared_constant
[%s:%d:%s] located completion ring configuration, adding %u instances
typed_allocators.hpp
I/O error
[%s:%d:%s] failed to aquire resource for %s[%u]
completion_mirror.cpp
driver_resource.cpp
[%s:%d:%s] setting client overrides for %s[%u]
get_entry_at_index
send_cr_open_message
[%s:%d:%s] (bc %s) image address 0x%llx, length 0x%x
bad-tr-ti-update
BUG in Airship: attempted to remove element not in list
set_error
[%s:%d:%s] (ctxid %hu) new availability blockers 0x%08x
[%s:%d:%s] (trid %hu) controller reset
did_set_transport
write_tr_head_index
set_completion_ring
[%s:%d:%s] (bc %s) sending image
BUG in Airship: bad boxed access
hexdump
finalize_tr_settlement_if_ready
[%s:%d:%s] performing health check.
BUG in Airship: attempted to insert element at position not in list
BUG in Airship: unrecognized detail bits in context controller.
[%s:%d:%s] updated power state: %u, current %u
[%s:%d:%s] crid %hu has unmessaged lifecycle, closing
disallowed name
cr_controller.cpp
auxiliary_context
driver_client.cpp
open_tr
[%s:%d:%s] context id %hu has unmessaged lifecycle, setting closed
probe_exec_stage_register_if_ready
boot_controller.cpp
dynamic_array.hpp
BUG in client of Airship: attempt to reconfigure active CR
[%s:%d:%s] (crid %hu) do not overwrite existing bad_cd buffer
doorbell
completion_groups
consume_transfers
transfer_ring_settled
[%s:%d:%s] (crid %hu) update bad cd
interrupt
[%s:%d:%s] main ipc state is not running (%u) or transport is not set
add_tr
[%s:%d:%s] sending close message for crid %hu
[%s:%d:%s] stopping context id %hu
[%s:%d:%s] (crid %hu) applied client overrides
leeway_usec
instance resolution failure
doorbell value not configured in shared constant mode
optimized_completion
external
read_ipc_status_register
[%s:%d:%s] (crid %hu) new availability blockers 0x%08x
stop_region
append_state_dump
[%s:%d:%s] (trid %hu) new doorbell interval (%u us), new leeway (%u us)
[%s:%d:%s] destroying completion ring handle for crid %hu
multiple-errors
BUG in client of Airship: attempted to reconfigure active driver
BUG in Airship: 
parse_array_or_singleton
copy_from
transfer_queue.cpp
[%s:%d:%s] (trid %hu) controller closed
parse_dict
acipc_types.cpp
true
[%s:%d:%s] updated error state: %u, current %u
set_backing_memory
length
remove_controller
reliable
bad key
[%s:%d:%s] (trid %hu) index %hu exceeds size %hu
set_completion_group
BUG in client of Airship: nonzero offset/length for NULL resource
tr_ring.cpp
not open
emplace
resolve
out_of_order
%zu
[%s:%d:%s] sending message now
[%s:%d:%s] completion count %hu
request_cr_close
[%s:%d:%s] closing trid %hu
image_doorbell
set_mcr_event_handler
BUG in Airship: index out of range
host-wake-failure
cancel_participant
[%s:%d:%s] activate
0x%08x:
~driver_client
~acipc_driver
[%s:%d:%s] unmapping memory region for %s[%u]
[%s:%d:%s] %s[%u] stopped
interval_usec
BUG in client of Airship: attempted to destroy client with subordinate object handles
(nil)
logging.cpp
handle_activate
[%s:%d:%s] reset type: %s
BUG in client of Airship: attempted to set interrupt execution queue for inactive driver
[%s:%d:%s] (crid %hu) close complete
operator=
will_set_transport
[%s:%d:%s] main ipc stage name %s
[%s:%d:%s] setting up ipc status interrupt
remove_region
advance_head_index
[%s:%d:%s] adding interrupt source %u
doorbell_controller.cpp
[%s:%d:%s] recomputing closed ring availability
completed_transfer_log_depth
[%s:%d:%s] (ctxid %hu) applied client overrides
get_transfer_completion
airship-driverkit-timer-watchdog
set_footer_size
[%s:%d:%s] updating context close requests
timer.cpp
[%s:%d:%s] (ctxid %hu) close complete
doorbell_coordinator.cpp
[%s:%d:%s] requesting close for crid %hu
min
protocol
write
set_ipc_stage
retrieve_state_dump
BUG in Airship: bad parameter - 'memory'
min_interval_usec
restricted
[%s:%d:%s] ipc handshake complete
~devmem_mapping_manager
copy_descriptor
sync_action_process_hi_update
offset
scratch_size
[%s:%d:%s] cannot wake
insert_before
image_interrupt
[%s:%d:%s] (bc %s) image sent, recomputing state
[%s:%d:%s] (trid %hu) state=%u, activated=%u
[%s:%d:%s] (crid %hu) failed to complete transfer
unsupported value
bad-inplace-completion
close
[%s:%d:%s] (trid %hu) sending open message
ignore_zeroed_cd
~memregion_manager
erase
BUG in Airship: refcount_mixin overreleased
[%s:%d:%s] context id %hu in limbo
[%s:%d:%s] new ipc status=%u
[%s:%d:%s] (trid %hu) predecessor completion ID %hu does not equal completion ID %hu
BUG in client of Airship: attempted to retrieve first free tag of ring without free space
BUG in Airship: airship_acipc_tr_disconnect: not implemented
[%s:%d:%s] trid %hu close message result %u
exec_stage
[%s:%d:%s] closing mcr
~direct_client
~boot_manager
[%s:%d:%s] (crid %hu) controller closed
value
[%s:%d:%s] not ready to probe exec stage register
read_index_array
compute_state_detail
registers
[%s:%d:%s] deferring message send
[%s:%d:%s] driver create client end %s
ok
set_cr_open
ipc stage
mappable_buffer.cpp
interrupt_moderation
Dale
tr_controller
create_resource_monitor
[%s:%d:%s] image has already been sent
is_sleep_status_valid
[%s:%d:%s] tearing down main ipc stage
[%s:%d:%s] creating device memory
[%s:%d:%s] new item at index %hu
map
[%s:%d:%s] (trid %hu) invalid in-place completion at idx=%hu
[%s:%d:%s] image sent for ipc stage %s
register overlap
handle_exit_reset
mem_write
[%s:%d:%s] adding boot controller for ipc stage %s
buffer_size_ring
Airship ACIPC protocol error
handle_get_nominal_state_dump_size
[%s:%d:%s] probing exec stage register
set_context
footer_size
active
peripheral_info_update_filter
[%s:%d:%s] (ctxid %hu) sending close message
set_capacity
BUG in Airship: access to null buffer
[%s:%d:%s] adding %u instances of resource %s
set_event_handler
[%s:%d:%s] (trid %hu) transfer enqueue size %u exceeds maximum transfer size %u
[%s:%d:%s] %s[%u] state %u, detail 0x%u
count
[%s:%d:%s] (crid %hu) new device ring status=%u
doorbell value out of range
[%s:%d:%s] ipc stage not torn down, boot stage valid: %u, main stage valid: %u
flush_DROPS_LOCK
disconnected (no device)
[%s:%d:%s] context id %hu has unmessaged lifecycle, setting open
[%s:%d:%s] adding crid %hu flush tracking for trid %hu
acipc_create_memregion_controller
version
in_place
environment.cpp
probe_exec_stage
count_where
[%s:%d:%s] not ready for ipc status interrupt
[%s:%d:%s] setting external execution queue for vector %u
[%s:%d:%s] ts: last_write %llx, schedule %llx, deadline %llx, 
get_debug_object_alloc_size
set_external_management
unable to map memory
interrupts
parse_array
append_debug_stats
get_device_sw_scaled_timeout
[%s:%d:%s] saving overflow message
CentauriBeta
shortcomp_complete_subsequent_transfers
get_inplace_completion
[%s:%d:%s] setting context id %hu closed
[%s:%d:%s] (bc %s) image response code=%u
stop_cr
[%s:%d:%s] associating crid %hu <-> trid %hu
[%s:%d:%s] ipc status invalid
update_interrupt_debug_state
Airship [%{public}s:%d:%{public}s] requesting close for trid %hu
Airship [%{public}s:%d:%{public}s] (crid %hu) failed to validate client override
Airship [%{public}s:%d:%{public}s] tearing down current ipc stage
Airship [%{public}s:%d:%{public}s] reset type: %s
Airship [%{public}s:%d:%{public}s] current main ipc stage and transport must be set
Airship [%{public}s:%d:%{public}s] (ctxid %hu) open failed 0x%x
Airship [%{public}s:%d:%{public}s] (ctxid %hu) stopping controller
Airship [%{public}s:%d:%{public}s] deferring message send
Airship [%{public}s:%d:%{public}s] (trid %hu) do not overwrite existing bad tx completion buffer
Airship [%{public}s:%d:%{public}s] context id %hu has unmessaged lifecycle, setting open
Airship [%{public}s:%d:%{public}s] stopping trid %hu for reason %u
Airship [%{public}s:%d:%{public}s] image sent for ipc stage %s
Airship [%{public}s:%d:%{public}s] (crid %hu) controller closed
Airship [%{public}s:%d:%{public}s] ipc stage not torn down, boot stage valid: %u, main stage valid: %u
Airship [%{public}s:%d:%{public}s] (ctxid %hu) reaping context controller
Airship [%{public}s:%d:%{public}s] (trid %hu) transfer at index %hu is in state %u
Airship [%{public}s:%d:%{public}s] creating doorbell controller for %s[%u]
Airship [%{public}s:%d:%{public}s] not ready to probe exec stage register
Airship [%{public}s:%d:%{public}s] copying peripheral info, initial exec stage value=%u
Airship [%{public}s:%d:%{public}s] created completion mirror object
Airship [%{public}s:%d:%{public}s] (trid %hu) new interrupt %s[%u]
Airship [%{public}s:%d:%{public}s] creating handle for completion ring with crid %u
Airship [%{public}s:%d:%{public}s] no handles available in pool
Airship [%{public}s:%d:%{public}s] stopping context id %hu
Airship [%{public}s:%d:%{public}s] main ipc state is not set
Airship [%{public}s:%d:%{public}s] unmapping memory region for %s[%u]
Airship [%{public}s:%d:%{public}s] (trid %hu) failed to complete transfer tag %hu
Airship [%{public}s:%d:%{public}s] added trid %hu
Airship [%{public}s:%d:%{public}s] (crid %hu) close complete
Airship [%{public}s:%d:%{public}s] (crid %hu) new device ring status=%u
Airship [%{public}s:%d:%{public}s] exec_stage during power-on=%u
Airship [%{public}s:%d:%{public}s] region id %hu exec stage mismatch %u
Airship [%{public}s:%d:%{public}s] region %s (id=%hu) cannot be used due to name conflict with id %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) predecessor state %u does not valid
Airship [%{public}s:%d:%{public}s] closing context id %hu
Airship [%{public}s:%d:%{public}s] setting up boot ipc stage
Airship [%{public}s:%d:%{public}s] unknown device viddid=%#x
Airship [%{public}s:%d:%{public}s] (bc %s) image sent, recomputing state
Airship [%{public}s:%d:%{public}s] (bc %s) out code=%u
Airship [%{public}s:%d:%{public}s] creating handle for transfer ring with trid %u
Airship [%{public}s:%d:%{public}s] resuming doorbell coordinator
Airship [%{public}s:%d:%{public}s] updated exec stage: %u, current %u
Airship [%{public}s:%d:%{public}s] sending close message for trid %hu
Airship [%{public}s:%d:%{public}s] crid %hu in limbo
Airship [%{public}s:%d:%{public}s] setting crid %hu closed
Airship [%{public}s:%d:%{public}s] (crid %hu) applied client overrides
Airship [%{public}s:%d:%{public}s] (ctxid %hu) close complete
Airship [%{public}s:%d:%{public}s] completion count %hu
Airship [%{public}s:%d:%{public}s] crid %hu has unmessaged lifecycle, setting open
Airship [%{public}s:%d:%{public}s] updating context info address register
Airship [%{public}s:%d:%{public}s] (trid %hu) first index %hu exceeds size %hu
Airship [%{public}s:%d:%{public}s] (bc %s) stopping boot controller
Airship [%{public}s:%d:%{public}s] %s[%u] old status %u, new status %u
Airship [%{public}s:%d:%{public}s] crid %hu belongs to the same group as %hu
Airship [%{public}s:%d:%{public}s] (crid %hu) reaping cr
Airship [%{public}s:%d:%{public}s] syncing mcr head index update
Airship [%{public}s:%d:%{public}s] (trid %hu) sending close message
Airship [%{public}s:%d:%{public}s] setting crid %hu open
Airship [%{public}s:%d:%{public}s] failed to find stage for value, %u
Airship [%{public}s:%d:%{public}s] ipc handshake complete
Airship [%{public}s:%d:%{public}s] new ipc status=%u
Airship [%{public}s:%d:%{public}s] syncing mtr tail index update and fetching completions
Airship [%{public}s:%d:%{public}s] platform_config=%u, probed viddid=0x%#x,  proxima_viddid=0x%#x
Airship [%{public}s:%d:%{public}s] (trid %hu) new doorbell interval (%u us), new leeway (%u us)
Airship [%{public}s:%d:%{public}s] trid %hu has unmessaged lifecycle, setting open
Airship [%{public}s:%d:%{public}s] context_open %.*P
Airship [%{public}s:%d:%{public}s] trid %hu set as open
Airship [%{public}s:%d:%{public}s] adding boot controller for ipc stage %s
Airship [%{public}s:%d:%{public}s] sleep status: active
Airship [%{public}s:%d:%{public}s] copying appendix
Airship [%{public}s:%d:%{public}s] (bc %s) detail=0
Airship [%{public}s:%d:%{public}s] (bc %s) sending image
Airship [%{public}s:%d:%{public}s] sending close message for crid %hu
Airship [%{public}s:%d:%{public}s] Registering tail index update handler for trid %hu at vector %hu
Airship [%{public}s:%d:%{public}s] located transfer ring configuration, adding %u instances
Airship [%{public}s:%d:%{public}s] ts: last_write %llx, schedule %llx, deadline %llx, 
Airship [%{public}s:%d:%{public}s] updated error state: %u, current %u
Airship [%{public}s:%d:%{public}s] trid %hu open message result %u
Airship [%{public}s:%d:%{public}s] (trid %hu) unexpected flush notice from CRID %hu
Airship [%{public}s:%d:%{public}s] (crid %hu) open failed 0x%x
Airship [%{public}s:%d:%{public}s] creating device memory
Airship [%{public}s:%d:%{public}s] setting client overrides for %s[%u]
Airship [%{public}s:%d:%{public}s] (crid %hu) stopping controller
Airship [%{public}s:%d:%{public}s] creating boot controller for %s
Airship [%{public}s:%d:%{public}s] (bc %s) no image response code
Airship [%{public}s:%d:%{public}s] entering reset, dropping any pending doorbells
Airship [%{public}s:%d:%{public}s] driver create client begin %s
Airship [%{public}s:%d:%{public}s] ring manager already in reset
Airship [%{public}s:%d:%{public}s] (trid %hu) invalid ti: %hu
Airship [%{public}s:%d:%{public}s] stop reason %u
Airship [%{public}s:%d:%{public}s] oversize host memory window reduced from %#llx to UINT32_MAX
Airship [%{public}s:%d:%{public}s] removing participant 0x%llx from pending queue
Airship [%{public}s:%d:%{public}s] window_base=%#llx, size=%#llx
Airship [%{public}s:%d:%{public}s] region id %hu sending memory map message
Airship [%{public}s:%d:%{public}s] object manager list not empty; dumping direct client objects
Airship [%{public}s:%d:%{public}s] setting external execution queue for vector %u
Airship [%{public}s:%d:%{public}s] (trid %hu) free=%hu, queued=%hu, pending=%hu, completed=%hu, fetched=%hu
Airship [%{public}s:%d:%{public}s] updated power state: %u, current %u
Airship [%{public}s:%d:%{public}s] recomputing closed ring availability
Airship [%{public}s:%d:%{public}s] (crid %hu) sending close message
Airship [%{public}s:%d:%{public}s] exec stage reg value=%u
Airship [%{public}s:%d:%{public}s] sleep status: %s
Airship [%{public}s:%d:%{public}s] setting up message buffer for main ipc stage %s
Airship [%{public}s:%d:%{public}s] starting messenger
Airship [%{public}s:%d:%{public}s] setting external interrupt handler for vector %u
Airship [%{public}s:%d:%{public}s] msi stats overflow: resetting count for vector %u
Airship [%{public}s:%d:%{public}s] crid %hu status %u
Airship [%{public}s:%d:%{public}s] trid %hu close message result %u
Airship [%{public}s:%d:%{public}s] probing exec stage register
Airship [%{public}s:%u:%{public}s] unexpected nonzero error code 0x%llx
Airship [%{public}s:%d:%{public}s] added crid %hu
Airship [%{public}s:%d:%{public}s] crid %hu has unmessaged lifecycle, setting closed
Airship [%{public}s:%d:%{public}s] (crid %hu) do not overwrite existing bad_cd buffer
Airship [%{public}s:%d:%{public}s] adding %u instances of resource %s
Airship [%{public}s:%d:%{public}s] setting up ipc status interrupt
Airship [%{public}s:%d:%{public}s] not ready for exec stage interrupt
Airship [%{public}s:%d:%{public}s] copying message payload
Airship [%{public}s:%d:%{public}s] (trid %hu) transfer flush failed
Airship [%{public}s:%d:%{public}s] context id %hu set as open
Airship [%{public}s:%d:%{public}s] context id %hu close message result %u
Airship [%{public}s:%d:%{public}s] creating new ring pool for transfer ring %s
Airship [%{public}s:%d:%{public}s] ipc status=%u
Airship [%{public}s:%d:%{public}s] not ready for ipc status interrupt
Airship [%{public}s:%d:%{public}s] num of objects pending deletion %u
Airship [%{public}s:%d:%{public}s] unknown proxima-platform: %llu
Airship [%{public}s:%d:%{public}s] already in reset
Airship [%{public}s:%d:%{public}s] tearing down mcr
Airship [%{public}s:%d:%{public}s] index %hu, message length %u
Airship [%{public}s:%d:%{public}s] %s[%u] reset
Airship [%{public}s:%d:%{public}s] stopping context id %hu for reason %u
Airship [%{public}s:%d:%{public}s] message failed, setting state for region id %hu
Airship [%{public}s:%d:%{public}s] image response %u, code %u
Airship [%{public}s:%d:%{public}s] %s[%u] unavailable
Airship [%{public}s:%d:%{public}s] crid %hu is not associated with any open trs
Airship [%{public}s:%d:%{public}s] (bc %s) image_state=%u
Airship [%{public}s:%d:%{public}s] handle_activate: result 0x%x
Airship [%{public}s:%d:%{public}s] failed to set client overrides for %s[%u]
Airship [%{public}s:%d:%{public}s] (trid %hu) open failed 0x%x
Airship [%{public}s:%d:%{public}s] (trid %hu) registering doorbell %s, selector %u
Airship [%{public}s:%d:%{public}s] no custom statedump handlers registered
Airship [%{public}s:%d:%{public}s] reset type=%u
Airship [%{public}s:%d:%{public}s] applied errata window_base_mask=%#llx, masked_base=%#llx
Airship [%{public}s:%d:%{public}s] synthesizing completions if needed
Airship [%{public}s:%d:%{public}s] (bc %s) old state=0x%llx, new state=0x%llx
Airship [%{public}s:%d:%{public}s] result=0x%x
Airship [%{public}s:%d:%{public}s] trid %hu has unmessaged lifecycle, closing
Airship [%{public}s:%d:%{public}s] notifying crid %hu that trid %hu is settled
Airship [%{public}s:%d:%{public}s] new ipc stage: %s
Airship [%{public}s:%d:%{public}s] (crid %hu) inserting completion with trid %hu and first tag %hu
Airship [%{public}s:%d:%{public}s] starting ipc handshake timer; timeout=%u ms
Airship [%{public}s:%d:%{public}s] entering device sleep
Airship [%{public}s:%d:%{public}s] region id %hu adding memregion_controller
Airship [%{public}s:%d:%{public}s] (trid %hu) new availability blockers 0x%08x
Airship [%{public}s:%d:%{public}s] (trid %hu) TR is now settled
Airship %s %s@%u
Airship [%{public}s:%d:%{public}s] boot manager is already in reset
Airship [%{public}s:%d:%{public}s] boot ipc stage name %s
Airship [%{public}s:%d:%{public}s] (ctxid %hu) failed to validate client override
Airship [%{public}s:%d:%{public}s] new item at index %hu
Airship [%{public}s:%d:%{public}s] deleted %hu items from mirror
Airship [%{public}s:%d:%{public}s] (trid %hu) failed to validate client override
Airship [%{public}s:%d:%{public}s] removed trid %hu
Airship [%{public}s:%d:%{public}s] no exec stage found for value %u
Airship [%{public}s:%d:%{public}s] (bc %s) adding controller to boot manager
Airship [%{public}s:%d:%{public}s] (bc %s) computing image table
Airship [%{public}s:%d:%{public}s] crid %hu is associated with trid %hu
Airship [%{public}s:%d:%{public}s] failed to flatten name/sel into string
Airship [%{public}s:%d:%{public}s] (crid %hu) invalid hi: %hu
Airship [%{public}s:%d:%{public}s] region id %hu removing memregion_controller
Airship [%{public}s:%d:%{public}s] (ctxid %hu) controller state=%u, detail=%u
Airship [%{public}s:%d:%{public}s] Deregistering tail index update handler for trid %hu at vector %hu
Airship [%{public}s:%d:%{public}s] messenger already out of reset
Airship [%{public}s:%d:%{public}s] setting up mcr
Airship [%{public}s:%d:%{public}s] (trid %hu) new device ring status=%u
Airship [%{public}s:%d:%{public}s] cr_open %.*P
Airship [%{public}s:%d:%{public}s] creating mtr
Airship [%{public}s:%d:%{public}s] (bc %s) detail=%u
Airship [%{public}s:%d:%{public}s] driver create client end %s
Airship [%{public}s:%d:%{public}s] context id %hu status %u
Airship [%{public}s:%d:%{public}s] context id %hu has unmessaged lifecycle, setting closed
Airship [%{public}s:%d:%{public}s] ACIPC protocol error 0x%08x (%s)
Airship [%{public}s:%d:%{public}s] (trid %hu) transfer tag %hu does not match next in-order tag %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) completing transfer tag %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) controller opened
Airship [%{public}s:%d:%{public}s] creating memregion controller for %s[%u]
Airship [%{public}s:%d:%{public}s] setting up peripheral info interrupt
Airship [%{public}s:%d:%{public}s] exiting host sleep
Airship [%{public}s:%d:%{public}s] (ctxid %hu) applied client overrides
Airship [%{public}s:%d:%{public}s] %{public}s
Airship [%{public}s:%d:%{public}s] sending message now
Airship [%{public}s:%d:%{public}s] getting transfer completion for tag %hu
Airship [%{public}s:%d:%{public}s] ring manager is in reset
Airship [%{public}s:%d:%{public}s] associating crid %hu <-> trid %hu
Airship [%{public}s:%d:%{public}s] crid %hu open message result %u
Airship [%{public}s:%d:%{public}s] region %s (id=%hu) cannot be used due to id conflict with name %s
Airship [%{public}s:%d:%{public}s] (trid %hu) predecessor completion ID %hu does not equal completion ID %hu
Airship [%{public}s:%d:%{public}s] added %u instances of doorbell %s
Airship [%{public}s:%d:%{public}s] reaping %s[%u]
Airship [%{public}s:%d:%{public}s] setting boot controller for ipc stage %s to unavailable
Airship [%{public}s:%d:%{public}s] IPC handshake timer expired
Airship [%{public}s:%d:%{public}s] setting up mtr
Airship [%{public}s:%d:%{public}s] message failure
Airship [%{public}s:%d:%{public}s] (trid %hu) tag %hu must belong to first in chain
Airship [%{public}s:%d:%{public}s] %s[%u] state %u, detail 0x%u
Airship [%{public}s:%d:%{public}s] (trid %hu) registering interrupt and setting up index array signaler vector %hu
Airship [%{public}s:%d:%{public}s] trid %hu in limbo
Airship [%{public}s:%d:%{public}s] creating context controller for %s[%u]
Airship [%{public}s:%d:%{public}s] invalid configuration: %s at %s
Airship [%{public}s:%d:%{public}s] region id %hu sending unmap message
Airship [%{public}s:%d:%{public}s] acquiring resource %s
Airship [%{public}s:%d:%{public}s] removed crid %hu
Airship [%{public}s:%d:%{public}s] sending close message for context id %hu
Airship [%{public}s:%d:%{public}s] requesting close for context id %hu
Airship [%{public}s:%d:%{public}s] (crid %hu) registering interrupt and setting up index array signaler vector %hu
Airship [%{public}s:%d:%{public}s] setting up main ipc stage
Airship [%{public}s:%d:%{public}s] sleep status: host sleep
Airship [%{public}s:%d:%{public}s] creating new ring pool for completion ring %s
Airship [%{public}s:%d:%{public}s] updating cr close requests
Airship [%{public}s:%d:%{public}s] stopping boot controller for ipc stage %s
Airship [%{public}s:%d:%{public}s] removing boot controller for ipc stage %s
Airship [%{public}s:%d:%{public}s] image has already been sent
Airship [%{public}s:%d:%{public}s] invoking action
Airship [%{public}s:%d:%{public}s] unexpected GUARD_ELSE failure
Airship [%{public}s:%d:%{public}s] change to exec stage %s (%u) from %s
Airship [%{public}s:%d:%{public}s] type=%u, debug meta-data=0x%llx, name=%s
Airship [%{public}s:%d:%{public}s] region id %hu is in limbo, attempting to unmap
Airship [%{public}s:%d:%{public}s] closing mcr
Airship [%{public}s:%d:%{public}s] tearing down mtr
Airship [%{public}s:%d:%{public}s] opening mtr
Airship [%{public}s:%d:%{public}s] located completion ring configuration, adding %u instances
Airship [%{public}s:%d:%{public}s] stopping trid %hu
Airship [%{public}s:%d:%{public}s] sending open message for context id %hu
Airship [%{public}s:%d:%{public}s] creating tr controller for %s[%u]
Airship [%{public}s:%d:%{public}s] (ctxid %hu) new availability blockers 0x%08x
Airship [%{public}s:%d:%{public}s] payload length %u, appendix length %u
Airship [%{public}s:%d:%{public}s] message canceled
Airship [%{public}s:%d:%{public}s] activating %s[%u]
Airship [%{public}s:%d:%{public}s] boot manager exiting reset
Airship [%{public}s:%d:%{public}s] failed to get resource
Airship [%{public}s:%d:%{public}s] closing trid %hu
Airship [%{public}s:%d:%{public}s] trid %hu close message requested
Airship [%{public}s:%d:%{public}s] (crid %hu) controller reset
Airship [%{public}s:%d:%{public}s] (crid %hu) registering with doorbell coordinator with doorbell %s
Airship [%{public}s:%d:%{public}s] (crid %hu) invalid completion descriptor at idx=%hu
Airship [%{public}s:%d:%{public}s] failed to aquire resource for %s[%u]
Airship [%{public}s:%d:%{public}s] requesting close for crid %hu
Airship [%{public}s:%d:%{public}s] setting trid %hu open
Airship [%{public}s:%d:%{public}s] (crid %hu) update bad cd
Airship [%{public}s:%d:%{public}s] enqueuing message in mtr
Airship [%{public}s:%d:%{public}s] sending overflow messages
Airship [%{public}s:%d:%{public}s] (trid %hu) transfer enqueue size %u exceeds maximum transfer size %u
Airship [%{public}s:%d:%{public}s] (bc %s) reseting boot controller
Airship [%{public}s:%d:%{public}s] IPC driver state_dump complete
Airship [%{public}s:%d:%{public}s] controller ipc stage: %s
Airship [%{public}s:%d:%{public}s] airship sw scaling %llu
Airship [%{public}s:%d:%{public}s] index %hu
Airship [%{public}s:%d:%{public}s] consuming transfers
Airship [%{public}s:%d:%{public}s] activating doorbell coordinator with %u doorbell instances
Airship [%{public}s:%d:%{public}s] mapping region of size %u for %s[%u]
Airship [%{public}s:%d:%{public}s] (trid %hu) update bad transfer completion
Airship [%{public}s:%d:%{public}s] failed to allocate/map device memory
Airship [%{public}s:%d:%{public}s] updating register at bank=%u, offset=%u
Airship [%{public}s:%d:%{public}s] Registering head index update handler for crid %hu at vector %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) free transfers %hu must exceed dead space size %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) completing chain
Airship [%{public}s:%d:%{public}s] reset type %u
Airship [%{public}s:%d:%{public}s] context id %hu has unmessaged lifecycle, closing
Airship [%{public}s:%d:%{public}s] context id %hu in limbo
Airship [%{public}s:%d:%{public}s] boot manager is in reset
Airship [%{public}s:%d:%{public}s] cannot set transport, %s ipc stage is not null
Airship [%{public}s:%d:%{public}s] entering host sleep
Airship [%{public}s:%d:%{public}s] timer deadline missed!!
Airship [%{public}s:%d:%{public}s] dbs : total %lu, active %lu, pending %d
Airship [%{public}s:%d:%{public}s] crid %hu has unmessaged lifecycle, closing
Airship [%{public}s:%d:%{public}s] failed to look up configuration for %s[%u]
Airship [%{public}s:%d:%{public}s] (crid %hu) new interrupt %s[%u]
Airship [%{public}s:%d:%{public}s] (trid %hu) controller closed
Airship [%{public}s:%d:%{public}s] (trid %hu) invalid in-place completion at idx=%hu
Airship [%{public}s:%d:%{public}s] updating context close requests
Airship [%{public}s:%d:%{public}s] context id %hu close message requested
Airship [%{public}s:%d:%{public}s] (crid %hu) new availability blockers 0x%08x
Airship [%{public}s:%d:%{public}s] region id %hu deferring unmap message
Airship [%{public}s:%d:%{public}s] value for shared constant doorbell: %u
Airship [%{public}s:%d:%{public}s] creating mcr
Airship [%{public}s:%d:%{public}s] processing completions
Airship [%{public}s:%d:%{public}s] (trid %hu) create tx_queue: size %hu, hdrlen %u, ftrlen %u, out-of-order %u
Airship [%{public}s:%d:%{public}s] (bc %s) image address 0x%llx, length 0x%x
Airship [%{public}s:%d:%{public}s] closing crid %hu
Airship [%{public}s:%d:%{public}s] Added context id %hu
Airship [%{public}s:%d:%{public}s] crid %hu close message result %u
Airship [%{public}s:%d:%{public}s] context id %hu open message result %u
Airship [%{public}s:%d:%{public}s] tearing down main ipc stage
Airship [%{public}s:%d:%{public}s] (ctxid %hu) sending close message
Airship [%{public}s:%d:%{public}s] performing health check.
Airship [%{public}s:%d:%{public}s] (ctxid %hu) controller reset
Airship [%{public}s:%d:%{public}s] message success
Airship [%{public}s:%d:%{public}s] (trid %hu) failed to find first transfer
Airship [%{public}s:%d:%{public}s] releasing ring with selector %u
Airship [%{public}s:%d:%{public}s] (crid %hu) new doorbell interval (%u us), new leeway (%u us)
Airship [%{public}s:%d:%{public}s] boot manager entering reset
Airship [%{public}s:%d:%{public}s] (crid %hu) sending open message
Airship [%{public}s:%d:%{public}s] tearing down boot ipc stage
Airship [%{public}s:%d:%{public}s] adding interrupt source %u
Airship [%{public}s:%d:%{public}s] participant 0x%llx added to doorbell %s[%u]
Airship [%{public}s:%d:%{public}s] sending open message for crid %hu
Airship [%{public}s:%d:%{public}s] boot manager is already out of reset
Airship [%{public}s:%d:%{public}s] (crid %hu) controller opened
Airship [%{public}s:%d:%{public}s] failed to aquire resource for %s
Airship [%{public}s:%d:%{public}s] closing mtr
Airship [%{public}s:%d:%{public}s] suspending doorbell coordinator
Airship [%{public}s:%d:%{public}s] trid %hu status %u
Airship [%{public}s:%d:%{public}s] setting context id %hu open
Airship [%{public}s:%d:%{public}s] sending open message for trid %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) index %hu exceeds size %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) first transfer not found
Airship [%{public}s:%d:%{public}s] destroying transfer ring handle for trid %hu
Airship [%{public}s:%d:%{public}s] failed to look up configuration for %s
Airship [%{public}s:%d:%{public}s] reset=%u, boot_state=%s, ipc_state=%s
Airship [%{public}s:%d:%{public}s] main ipc stage name %s
Airship [%{public}s:%d:%{public}s] wake requested=%u, target host sleep=%u, permit device sleep=%u
Airship [%{public}s:%d:%{public}s] cannot wake
Airship [%{public}s:%d:%{public}s] (trid %hu) moving queued transfers into pending state
Airship [%{public}s:%d:%{public}s] (trid %hu) new mode (%u)
Airship [%{public}s:%d:%{public}s] (trid %hu) stopping controller
Airship [%{public}s:%d:%{public}s] (crid %hu) failed to complete transfer
Airship [%{public}s:%d:%{public}s] trid %hu is settled
Airship [%{public}s:%d:%{public}s] messenger failed to map mtr/mcr memory
Airship [%{public}s:%d:%{public}s] exec stage interrupt occurred: value %u
Airship [%{public}s:%d:%{public}s] exiting reset
Airship [%{public}s:%d:%{public}s] removing interrupt source %u
Airship [%{public}s:%d:%{public}s] (bc %s) image valid : %s 
Airship [%{public}s:%d:%{public}s] coordinator state=%u, new IPC stage=%s
Airship [%{public}s:%d:%{public}s] %s[%u] stopped
Airship [%{public}s:%d:%{public}s] (bc %s) checking for image response
Airship [%{public}s:%d:%{public}s] (trid %hu) state=%u, activated=%u
Airship [%{public}s:%d:%{public}s] stopping crid %hu
Airship [%{public}s:%d:%{public}s] tr_open %.*P
Airship [%{public}s:%d:%{public}s] not ready for peripheral info interrupt
Airship [%{public}s:%d:%{public}s] (trid %hu) attempt to consume %hu transfers, %hu fetched
Airship [%{public}s:%d:%{public}s] stopping crid %hu for reason %u
Airship [%{public}s:%d:%{public}s] region id %hu conflict %u
Airship [%{public}s:%d:%{public}s] message success, setting state for region id %hu
Airship [%{public}s:%d:%{public}s] viddid=%#x
Airship [%{public}s:%d:%{public}s] map successful
Airship [%{public}s:%d:%{public}s] (trid %hu) completions synthesized
Airship [%{public}s:%d:%{public}s] entering reset
Airship [%{public}s:%d:%{public}s] (crid %hu) trid %hu does not accept completions from this cr
Airship [%{public}s:%d:%{public}s] (crid %hu) cr terminated
Airship [%{public}s:%d:%{public}s] (bc %s) image response code=%u
Airship [%{public}s:%d:%{public}s] reserve %u complete
Airship [%{public}s:%d:%{public}s] setting context id %hu closed
Airship [%{public}s:%d:%{public}s] setting up message rings
Airship [%{public}s:%d:%{public}s] activate
Airship [%{public}s:%d:%{public}s] in_reset %u, activated %u
Airship [%{public}s:%d:%{public}s] (trid %hu) controller reset
Airship [%{public}s:%d:%{public}s] removed context id %hu
Airship [%{public}s:%d:%{public}s] setting trid %hu closed
Airship [%{public}s:%d:%{public}s] adding crid %hu flush tracking for trid %hu
Airship [%{public}s:%d:%{public}s] main ipc state is not running (%u) or transport is not set
Airship [%{public}s:%d:%{public}s] saving overflow message
Airship [%{public}s:%d:%{public}s] destroying completion ring handle for crid %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) sending open message
Airship [%{public}s:%d:%{public}s] (trid %hu) close complete
Airship [%{public}s:%d:%{public}s] ring manager already out of reset
Airship [%{public}s:%d:%{public}s] creating cr controller for %s[%u]
Airship [%{public}s:%d:%{public}s] ipc status invalid
Airship [%{public}s:%d:%{public}s] sleep status invalid
Airship [%{public}s:%d:%{public}s] (trid %hu) failed: hi=%hu, ti=%hu
Airship [%{public}s:%d:%{public}s] acipc driver activate complete
Airship [%{public}s:%d:%{public}s] (trid %hu) offset %hu exceeds fetched transfer count %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) seek %hu exceeds pending transfer count %hu
Airship [%{public}s:%d:%{public}s] crid: %u
Airship [%{public}s:%d:%{public}s] no ipc stage set
Airship [%{public}s:%d:%{public}s] failed to get device memory window config
Airship [%{public}s:%d:%{public}s] value %u matches to exec stage: %s
Airship [%{public}s:%d:%{public}s] sw timeout scale for proxima protium platform: %llu
Airship [%{public}s:%d:%{public}s] opening mcr
Airship [%{public}s:%d:%{public}s] sending any overflow messages
Airship [%{public}s:%d:%{public}s] reserving ring with selector %u
```
