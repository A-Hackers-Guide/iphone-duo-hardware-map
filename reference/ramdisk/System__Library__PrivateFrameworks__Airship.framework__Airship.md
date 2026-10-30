# `/System/Library/PrivateFrameworks/Airship.framework/Airship`

From the upgrade restore ramdisk (141-29011-104.dmg). 968,880 bytes.

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
[%s:%d:%s] setting external execution queue for vector %u
[%s:%d:%s] destroying completion ring handle for crid %hu
[%s:%d:%s] timer deadline missed!!
typed_allocators.cpp
BUG in Airship: unaligned device memory access
BUG in Airship: attempted to find existing boxed symbol from null string
not privileged
[%s:%d:%s] no ipc stage set
get_image_response
unknown ipc stage
read_head_index
create_cr_controller
configurator.cpp
set_external_execution_queue
count_where
no-error
get_value
airship-debug
[%s:%d:%s] recomputing closed ring availability
[%s:%d:%s] setting trid %hu open
update_completion_desc_debug_info
[%s:%d:%s] (crid %hu) registering interrupt and setting up index array signaler vector %hu
doorbell
[%s:%d:%s] region id %hu exec stage mismatch %u
reap_single_DROPS_LOCK
[%s:%d:%s] map successful
[%s:%d:%s] (trid %hu) unexpected flush notice from CRID %hu
ipc_control
group
[%s:%d:%s] not ready for ipc status interrupt
print_queue_stats
send_context_close_message
direct_client_object
[%s:%d:%s] region id %hu sending unmap message
copy_to
[%s:%d:%s] opening mcr
get_paddr
[%s:%d:%s] suspending doorbell coordinator
~direct_cr_controller
image_table
footer_size
[%s:%d:%s] object manager list not empty; dumping direct client objects
set_interrupt
get_time_metadata
buffer_array
create_state_monitor
[%s:%d:%s] (trid %hu) close complete
[%s:%d:%s] crid %hu open message result %u
unsupported value
limits
[%s:%d:%s] sleep status: host sleep
clear_cr_indices
~driver
[%s:%d:%s] sleep status invalid
[%s:%d:%s] consuming transfers
[%s:%d:%s] (trid %hu) create tx_queue: size %hu, hdrlen %u, ftrlen %u, out-of-order %u
[%s:%d:%s] located completion ring configuration, adding %u instances
[%s:%d:%s] (crid %hu) new device ring status=%u
mode
peripheral_info_interrupt_occurred
[%s:%d:%s] ipc handshake complete
multicomp_find_first_transfer
BUG in client of Airship: invalid queue role
get_mirror_count
setup_interrupt
[%s:%d:%s] (trid %hu) failed: hi=%hu, ti=%hu
create_exec_stage_monitor
bounds overflow
auxiliary_contexts
cancel_participant
reduce_size
operator[]
not ready
set_device_context_status
get_completed_transfer_count
copy_debug_info
acquire_resource
vendor
[%s:%d:%s] (ctxid %hu) controller reset
static_array.hpp
[%s:%d:%s] creating memregion controller for %s[%u]
[%s:%d:%s] tearing down boot ipc stage
[%s:%d:%s] new item at index %hu
cr_ring.cpp
notify_transfer_ring_when_flushed
[%s:%d:%s] IPC handshake timer expired
set_source_maintenance_completion_handler
[%s:%d:%s] (trid %hu) free transfers %hu must exceed dead space size %hu
remove_participant
BUG in client of Airship: externally managed ring
is_ipc_status_valid
send_message
get_and_advance_inorder_idx_for_enqueue
set_size
BUG in client of Airship: selector is not available
ok
parse_array_or_singleton
memregion_controller
[%s:%d:%s] context id %hu status %u
get_prev_transfer_in_queue
unexpected mode string
parse_optional
find_exec_stage_with_value
BUG in client of Airship: attempted to reconfigure active TR
update_head_index
[%s:%d:%s] (trid %hu) free=%hu, queued=%hu, pending=%hu, completed=%hu, fetched=%hu
classify_image_response_code
~devmem_mapping
set_settled
host-wake-failure
[%s:%d:%s] located transfer ring configuration, adding %u instances
set_external_management
[%s:%d:%s] stopping context id %hu
refresh_mapping
[%s:%d:%s] Added context id %hu
[%s:%d:%s] setting up message rings
read_cr_head_index
downlink-buffer-count-len-error
[%s:%d:%s] (trid %hu) transfer at index %hu is in state %u
airship_acipc_tr_disconnect
[%s:%d:%s] dbs : total %lu, active %lu, pending %d
acipc
handle_clear_transport
ipc_handshake_timeout_occurred
BUG in client of Airship: out of bounds access to buffer
[%s:%d:%s] (trid %hu) new mode (%u)
close_cr
peripheral_info_interrupt
did_set_transport
update_context_info_addr_registers
~interrupt_manager
read_register
[%s:%d:%s] (trid %hu) TR is now settled
set_cr_closed
memregion_manager.cpp
[%s:%d:%s] (ctxid %hu) close complete
release
tr_open_message_completed
value out of bounds
driver_debug_object.hpp
emplace
handle_enter_reset
map_region
[%s:%d:%s] opening mtr
get_vector_for_interrupt
CentauriAlpha
[%s:%d:%s] %s[%u] stopped
BUG in Airship: access to null buffer mapping
set_backing_ring_size
[%s:%d:%s] added crid %hu
ipc stage
[%s:%d:%s] type=%u, debug meta-data=0x%llx, name=%s
does_region_conflict_with_any_mapped_region
append_cr_index_info
[%s:%d:%s] tearing down mcr
false
BUG in client of Airship: nonzero offset/length for NULL resource
tr_controller.cpp
[%s:%d:%s] stopping boot controller for ipc stage %s
[%s:%d:%s] message failed, setting state for region id %hu
[%s:%d:%s] setting up mcr
bad-cd
doorbell_coordinator
set_mirror_enabled
BUG in Airship: attempted to access boxed dictionary with null key
unknown-error
add_doorbells
schedule_update
optional.hpp
[%s:%d:%s] (crid %hu) sending open message
remove_region
BUG in client of Airship: attempted to unregister handler for inactive driver
[%s:%d:%s] context id %hu has unmessaged lifecycle, closing
teardown_current_ipc_stage
monitor.cpp
write
complete_transfer
[%s:%d:%s] setting context id %hu open
remove_controller
create_sync_monitor
traffic_class
arm_tr_index_vector
consume_mirror_elements
~tr_controller
send_context_open_message
[%s:%d:%s] notifying crid %hu that trid %hu is settled
get_element
direct_buffer.cpp
device_memory.cpp
devmem_mapping
BUG in client of Airship: attempted to unregister handler for terminated driver
[%s:%d:%s] added trid %hu
bad-cr-hi-update
[%s:%d:%s] entering reset, dropping any pending doorbells
set_availability_blockers
transfer_footer_size
ring_controller.cpp
get_addr
boot_manager.cpp
[%s:%d:%s] region id %hu deferring unmap message
set_notifier
set_device_region_status
[%s:%d:%s] %s[%u] unavailable
driver_ioservice_params
~acipc_driver
[%s:%d:%s] sleep status: active
BUG in client of Airship: attempted to reconfigure active interrupt
[%s:%d:%s] starting messenger
channel-sync-failure
device-sleep-exit-timeout
cldma-tx-error
[%s:%d:%s] acquiring resource %s
invalid completion style
advance_head_index
enqueue_transfer
[%s:%d:%s] (bc %s) computing image table
set_ipc_error_flags
stop_tr
[%s:%d:%s] stopping crid %hu
state_dump_manager.cpp
memory_map_message_completed
clear_tr_indices
t2026
[%s:%d:%s] participant 0x%llx added to doorbell %s[%u]
already in use (exclusive access)
logging.cpp
[%s:%d:%s] trid %hu set as open
[%s:%d:%s] not ready for peripheral info interrupt
[%s:%d:%s] oversize host memory window reduced from %#llx to UINT32_MAX
[%s:%d:%s] processing completions
BUG in client of Airship: attempted to activate already-active context
[%s:%d:%s] destroying transfer ring handle for trid %hu
check_all_context_close_requests
unexpected object type
main_ipc_stages
BUG in client of Airship: attempted to activate active interrupt
clear_transport
reap
handle_exit_reset
[%s:%d:%s] synthesizing completions if needed
unmap
[%s:%d:%s] (crid %hu) failed to validate client override
acipc_create_memregion_controller
[%s:%d:%s] (trid %hu) transfer tag %hu does not match next in-order tag %hu
get_transfer_completion
[%s:%d:%s] (bc %s) stopping boot controller
update_tail_index
[%s:%d:%s] sending close message for crid %hu
[%s:%d:%s] boot manager is in reset
response code is ambiguous
context_info_address_lo
set_interrupt_handler
reset
[%s:%d:%s] (trid %hu) invalid in-place completion at idx=%hu
???
[%s:%d:%s] trid %hu open message result %u
wait_context.cpp
[%s:%d:%s] Registering head index update handler for crid %hu at vector %hu
set_transport
BUG in client of Airship: attempted to set interrupt execution queue for terminated driver
[%s:%d:%s] updated power state: %u, current %u
[%s:%d:%s] (trid %hu) sending close message
[%s:%d:%s] sending open message for context id %hu
unsupported register width
handle_activate
reserve
BUG in Airship: invalid tail index update operation
cr_controller
ipc_status
v8@?0
typed_delete
process_inplace_completions
%s-%u
wait
airship-sw-timeout-scale
BUG in Airship: unrecognized detail bits in context controller.
compute_offsets
ring_index_pair.hpp
create_handle
[%s:%d:%s] (trid %hu) new availability blockers 0x%08x
[%s:%d:%s] acipc driver activate complete
[%s:%d:%s] setting up peripheral info interrupt
[%s:%d:%s] (ctxid %hu) new availability blockers 0x%08x
[%s:%d:%s] syncing mcr head index update
add
boot_controller
[%s:%d:%s] releasing ring with selector %u
BUG in Airship: attempted to create boxed symbol from null string
disallowed name
write_index_array
[%s:%d:%s] already in reset
direct_context.cpp
[%s:%d:%s] driver create client end %s
I/O error
doorbell_timer_tolerance_us
[%s:%d:%s] message success, setting state for region id %hu
[%s:%d:%s] enqueuing message in mtr
[%s:%d:%s] removing participant 0x%llx from pending queue
[%s:%d:%s] %s[%u] reset
update_mem_window_base_and_size
send_overflow_messages
BUG in client of Airship: Unsupported mode: AIRSHIP_ACIPC_TR_MODE_BATCH (missing IOUserNetworkPacket)
instance resolution failure
mem_read32
(nil)
in-place completion requires in-order
constraints
bad key
set_mcr_event_handler
[%s:%d:%s] crid %hu belongs to the same group as %hu
write_tail_index
[%s:%d:%s] ipc stage not torn down, boot stage valid: %u, main stage valid: %u
BUG in Airship: attempted message send in reset
cr_ring
clear_context
acipc_driver.cpp
update_ipc_control_register
[%s:%d:%s] region %s (id=%hu) cannot be used due to name conflict with id %hu
[%s:%d:%s] (bc %s) image valid : %s 
close_context
[%s:%d:%s] setting crid %hu closed
get_max_message_length
append_context_state_dump
[%s:%d:%s] trid %hu status %u
non-default completion group requires out-of-order
add_region
driver_object.cpp
async_notifier.cpp
driver.cpp
%s %s@%u
[%s:%d:%s] (crid %hu) reaping cr
role
operator=
[%s:%d:%s] (ctxid %hu) open failed 0x%x
[%s:%d:%s] adding %u instances of resource %s
[%s:%d:%s] starting ipc handshake timer; timeout=%u ms
transfer_queue
[%s:%d:%s] (crid %hu) controller reset
restricted
scratch_size
completion_ring_stride
create_debug_object
direct_interrupt.cpp
~messenger
~driver_client
main_ipc_state_machine
[%s:%d:%s] region id %hu is in limbo, attempting to unmap
set_cr_open
[%s:%d:%s] cr_open 
acipc_create_boot_controller
value exceeds ipc stage limit
process_completions
[%s:%d:%s] removing interrupt source %u
BUG in client of Airship: attempted to create client for inactive driver
activate
[%s:%d:%s] requesting close for trid %hu
proxima-platform
deregister_tr_index_vector_action
completion_mirror.cpp
[%s:%d:%s] updated error state: %u, current %u
[%s:%d:%s] unmapping memory region for %s[%u]
BUG in Airship: _memory is NULL
not open
[%s:%d:%s] crid %hu is associated with trid %hu
[%s:%d:%s] (crid %hu) registering with doorbell coordinator with doorbell %s
[%s:%d:%s] (crid %hu) cr terminated
get_health_status
dump_object_info
[%s:%d:%s] invoking action
[%s:%d:%s] creating cr controller for %s[%u]
accumulation
~direct_client_object
[%s:%d:%s] messenger already out of reset
get_next_transfer_in_queue
true
~intrusive_list_link
[%s:%d:%s] resuming doorbell coordinator
[%s:%d:%s] entering host sleep
[%s:%d:%s] value %u matches to exec stage: %s
BUG in Airship: attempted to remove element not in list
enter_reset
BUG in Airship: unexpected flush notice
mappable_buffer.cpp
BUG in Airship: attempted to create boxed string from null C string
[%s:%d:%s] closing trid %hu
[%s:%d:%s] updating context close requests
direct_tr_controller.cpp
BUG in Airship: attempted to access terminated driver
compute_free_space
set_context_closed
offset
channel-quiesce-failure
interrupt.cpp
set_maintenance_completion_notifier
BUG in Airship: list element destroyed while in list
mem_write
BUG in Airship: requested CD element is inactive
round_up_to_page_size
[%s:%d:%s] reset type=%u
resource_stride
read_ipc_status_register
flush_with_action
register_tr_index_vector_action
fixup_remain_count
cr_index_count
sleep_control
doorbell_stride
interrupt_stride
trigger_async
memory_unmap_message_completed
~direct_client
BUG in Airship: ring size cannot be zero
[%s:%d:%s] tr_open 
[%s:%d:%s] image has already been sent
ignore_zeroed_cd
[%s:%d:%s] closing mtr
[%s:%d:%s] (bc %s) out code=%u
populate_descriptor
transfer_ring_opened
[%s:%d:%s] Deregistering tail index update handler for trid %hu at vector %hu
[%s:%d:%s] value for shared constant doorbell: %u
[%s:%d:%s] in_reset %u, activated %u
copy_descriptor
disconnected (no device)
[%s:%d:%s] ring manager is in reset
[%s:%d:%s] context id %hu in limbo
[%s:%d:%s] (crid %hu) invalid hi: %hu
teardown_boot_ipc_stage
[%s:%d:%s] (trid %hu) attempt to consume %hu transfers, %hu fetched
[%s:%d:%s] reserving ring with selector %u
[%s:%d:%s] (trid %hu) controller opened
[%s:%d:%s] (trid %hu) transfer flush failed
parse_array
[%s:%d:%s] failed to get device memory window config
BUG in client of Airship: attempted to access inactive driver
image_size
interrupt_moderation
[%s:%d:%s] (ctxid %hu) controller state=%u, detail=%u
enqueue_message_in_mtr
operator()
send_tr_close_message
~monitor
BUG in client of Airship: attempted to access inactive TR
image_doorbell
send_memory_map_message
read_tr_tail_index
[%s:%d:%s] setting up ipc status interrupt
BUG in Airship: invalid head index advance operation
set_exec_stage_change_handler
BUG in Airship: requested TD element is inactive
BUG in Airship: Attempted to perform a health check in driver_client
remove_tr
reaper.cpp
driver_object
finalize_tr_settlement_if_ready
[%s:%d:%s] creating tr controller for %s[%u]
shared_timestamp
peripheral_info_update_filter
[%s:%d:%s] region id %hu adding memregion_controller
BUG in client of Airship: attempted to set external interrupt handler for inactive driver
mtr
remove_context
[%s:%d:%s] controller ipc stage: %s
copy_and_zerofill
update_interrupt_debug_state
success_code
set_completion_footer_size
debug_infra.hpp
[%s:%d:%s] context id %hu open message result %u
BUG in Airship: attempted to initialize optional with sentinel value
min
BUG in Airship: attempted to reconfigure active object
[%s:%d:%s] (bc %s) adding controller to boot manager
BUG in Airship: bad parameter - 'memory'
[%s:%d:%s] (trid %hu) update bad transfer completion
[%s:%d:%s] wake requested=%u, target host sleep=%u, permit device sleep=%u
stop_region
dynamic_array.hpp
[%s:%d:%s] (trid %hu) open failed 0x%x
[%s:%d:%s] ring manager already in reset
[%s:%d:%s] failed to flatten name/sel into string
[%s:%d:%s] %s[%u] state %u, detail 0x%u
count
[%s:%d:%s] (crid %hu) close complete
create_tr_controller
completion_groups
[%s:%d:%s] exec stage interrupt occurred: value %u
ALLOCATION FAILURE (or BUG) in Airship
[%s:%d:%s] setting context id %hu closed
[%s:%d:%s] removed crid %hu
[%s:%d:%s] image response %u, code %u
update_exec_stage
BUG in client of Airship: attempted to set interrupt execution queue for inactive driver
BUG in Airship: attempted truncate to larger size
BUG in Airship: refcount_mixin retained after release
get_page_size
general error
cr_open_message_completed
[%s:%d:%s] adding interrupt source %u
tr_ring
parse_dict
populate_context_info
synthesize_reset_completions
get_first_completed_tag
validate_client_overrides
exec_stage
enable_interrupt_vector
acipc_types.cpp
[%s:%d:%s] (trid %hu) offset %hu exceeds fetched transfer count %hu
[%s:%d:%s] reserve %u complete
setup_tr_settlement_tracking
[%s:%d:%s] crid %hu is not associated with any open trs
queue
register overlap
multicomp_complete_prior_transfers
BUG in client of Airship: Failed to locate transfer ring config
set_power_target
setup_boot_ipc_stage
[%s:%d:%s] (bc %s) image sent, recomputing state
[%s:%d:%s] crid %hu status %u
synchronized
[%s:%d:%s] unknown proxima-platform: %llu
get_inplace_completion
platform_private.cpp
in_place
get_mirror_element
mem_write32
set_image_sent
resolve
write_cr_tail_index
BUG in Airship: invalid tail index advance operation
add_handler
consume_transfers
operation canceled
[%s:%d:%s] sending open message for crid %hu
[%s:%d:%s] image sent for ipc stage %s
BUG in Airship: invalid dst
get_queue
BUG in Airship: bad parameter - 'footer_length'
invalid value
copy_from
[%s:%d:%s] msi stats overflow: resetting count for vector %u
BUG in client of Airship: selector is invalid
unexpected-transport-revocation
release_resource
[%s:%d:%s] removed trid %hu
image_response
async_callback
set_completion_ring
skip_window_configuration
nominal_transfer_size
check_for_image_response
unregister_client_statedump_handler
BUG in client of Airship: attempted to activate already-active CR
BUG in Airship: refcount_mixin overreleased
BUG in Airship: access to null buffer
[%s:%d:%s] boot ipc stage name %s
dump_list
[%s:%d:%s] crid: %u
BUG in Airship: attempted access to terminated client
ipc_running_timeout
unmap_region
device_classifier.cpp
BUG in client of Airship: attempted to activate already-active TR
typed_allocators.hpp
[%s:%d:%s] (trid %hu) controller closed
close_tr
[%s:%d:%s] stopping trid %hu
get_current_ipc_stage_name
[%s:%d:%s] no exec stage found for value %u
~async_accelerator
set_map_clientdata
set_ipc_error_handler
BUG in Airship: attempted to create tr_controller in direct_client
send_tr_open_message
active
[%s:%d:%s] Registering tail index update handler for trid %hu at vector %hu
compute_io_status_for_transfers
intrusive_list.hpp
completion_ring_did_flush
[%s:%d:%s] sending close message for trid %hu
[%s:%d:%s] (crid %hu) inserting completion with trid %hu and first tag %hu
[%s:%d:%s] failed to look up configuration for %s
[%s:%d:%s] boot manager exiting reset
BUG in Airship: attempted to activate object without required configuration
send_cr_close_message
exec_stage_interrupt
parse_number
[%s:%d:%s] IPC driver state_dump complete
[%s:%d:%s] (trid %hu) do not overwrite existing bad tx completion buffer
[%s:%d:%s] failed to look up configuration for %s[%u]
leeway_usec
debug
deregister_cr_index_vector_action
[%s:%d:%s] sending any overflow messages
[%s:%d:%s] boot manager entering reset
chain
[%s:%d:%s] created completion mirror object
[%s:%d:%s] (bc %s) image address 0x%llx, length 0x%x
create
tr_settled
context_open_message_completed
[%s:%d:%s] removed context id %hu
chipset
airship-read-before-sleep-update
~interrupt
~client_interrupt
no space for data
parse_symbol
finish_queued_partial_chain
shortcomp_complete_subsequent_transfers
[%s:%d:%s] added %u instances of doorbell %s
sync
sync_action_process_ti_update
parse
[%s:%d:%s] messenger failed to map mtr/mcr memory
device-signalled error
[%s:%d:%s] mapping region of size %u for %s[%u]
BUG in Airship: attempted to activate canceled object
refcount_mixin.hpp
[%s:%d:%s] (trid %hu) stopping controller
append_bytes
missing object
out_of_order
id
cldma-link-error
disconnect_interrupt
add_tr
transfer_ring_settled
register
base.cpp
insert_before
doorbell_controller.cpp
acipc_get_health_status
setup_notifier
[%s:%d:%s] deleted %hu items from mirror
direct_memregion.cpp
ring_index_pair
count_intersection
~devmem_mapping_manager
external
[%s:%d:%s] change to exec stage %s (%u) from %s
~direct_client_object_manager
send_memory_unmap_message
index
version
tr_index_count
BUG in Airship: bad parameter - 'size'
[%s:%d:%s] associating crid %hu <-> trid %hu
~state_dump_manager
[%s:%d:%s] (crid %hu) applied client overrides
[%s:%d:%s] new ipc stage: %s
name
group_stride
[%s:%d:%s] ipc status invalid
[%s:%d:%s] index %hu, message length %u
bind_active_object
get_inorder_tag_for_enqueue
[%s:%d:%s] closing crid %hu
save_transfer_completion
set_backing_memory
timeout
driver_client.cpp
[%s:%d:%s] ipc status=%u
messenger.cpp
BUG in Airship: attempted to use inactive object
ipc_reset_occurred
cr_close_message_completed
add_participant
[%s:%d:%s] (trid %hu) invalid ti: %hu
remove_cr
[%s:%d:%s] creating device memory
~monitor_target
BUG in client of Airship: attempted to reconfigure active monitor
hexdump
transfer_rings
existing_for_str
[%s:%d:%s] setting up main ipc stage
BUG in Airship: attempted to insert element at position not in list
memregion_controller.cpp
with_format
[%s:%d:%s] context id %hu has unmessaged lifecycle, setting closed
airship-trap-on-acipc-error
~driver_object
[%s:%d:%s] creating mcr
[%s:%d:%s] trid %hu close message result %u
acipc_create_doorbell_controller
[%s:%d:%s] performing health check.
map
tr_ring.cpp
BUG in Airship: refcount_mixin retain overflow
log
activate_block_invoke
BUG in client of Airship: attempt to reconfigure active CR
scribble_descriptor
append_debug_stats
mem_read
main
[%s:%d:%s] trid %hu close message requested
[%s:%d:%s] (crid %hu) failed to complete transfer
registers
failure_code
memory_regions
[%s:%d:%s] invalid configuration: %s at %s
validate_buffer_bounds
[%s:%d:%s] creating context controller for %s[%u]
ambiguous value
[%s:%d:%s] deferring message send
system-failure
read
set_event_handler
find_completion_target
[%s:%d:%s] (trid %hu) failed to validate client override
[%s:%d:%s] sending open message for trid %hu
[%s:%d:%s] no custom statedump handlers registered
[%s:%d:%s] (crid %hu) sending close message
ambiguous name
[%s:%d:%s] main ipc stage name %s
BUG in Airship: attempted to activate active object
[%s:%d:%s] (crid %hu) new interrupt %s[%u]
[%s:%d:%s] context id %hu set as open
cr_controller.cpp
setup_main_ipc_stage
dal25
[%s:%d:%s] (bc %s) checking for image response
BUG in client of Airship: nonzero selector for NULL resource
with_cstr
ipc_status_interrupt
trigger
set_mode
[%s:%d:%s] setting client overrides for %s[%u]
sync_action_flush_pending_transfers
airship_platform_get_fallback_queue_block_invoke
nominal_state_dump_size
timer.cpp
boxed_types.cpp
[%s:%d:%s] boot manager is already out of reset
handle_get_nominal_state_dump_size
context_controller.cpp
context_controller
BUG in client of Airship: attempted to activate canceled interrupt
connect_interrupt
[%s:%d:%s] (trid %hu) transfer enqueue size %u exceeds maximum transfer size %u
[%s:%d:%s] (trid %hu) sending open message
ipc_stage
interrupt
update_sleep_control_register
[%s:%d:%s] (bc %s) no image response code
set_power_state_change_handler
create_resource_monitor
~boot_manager
image_address_lo
[%s:%d:%s] num of objects pending deletion %u
unknown target
arm_cr_index_vector
[%s:%d:%s] copying appendix
[%s:%d:%s] exiting reset
length
recompute_state
truncate
doorbell_moderation
[%s:%d:%s] (bc %s) old state=0x%llx, new state=0x%llx
send_cr_open_message
instance count is zero
doorbells
size
[%s:%d:%s] (trid %hu) tag %hu must belong to first in chain
unknown result code
interval_usec
min_interval_usec
value exceedes auxiliary context limit
[%s:%d:%s] setting up message buffer for main ipc stage %s
~cr_controller
open
direct_monitor.cpp
[%s:%d:%s] (ctxid %hu) reaping context controller
[%s:%d:%s] tearing down mtr
BUG in Airship: attempted to insert element already in list
retrieve_state_dump
[%s:%d:%s] activating %s[%u]
read_exec_stage_register
register_cr_index_vector_action
[%s:%d:%s] (ctxid %hu) applied client overrides
BUG in client of Airship: attempted to access inactive interrupt
unexpected-ipc-status
[%s:%d:%s] crid %hu has unmessaged lifecycle, closing
[%s:%d:%s] adding boot controller for ipc stage %s
finalize_indices
reliable
unknown context
device_info
[%s:%d:%s] (trid %hu) new interrupt %s[%u]
device_transport.cpp
[%s:%d:%s] reset type %u
optimized_completion
BUG in Airship: flat array size multiplication overflow
[%s:%d:%s] (trid %hu) seek %hu exceeds pending transfer count %hu
close
BUG in Airship: oversize ring
acipc_create_context_controller
ring_pool.cpp
get_entry_at_index
BUG in client of Airship: attempted to destroy client with subordinate object handles
vector
cldma-rx-error
[%s:%d:%s] (trid %hu) completing transfer tag %hu
[%s:%d:%s] (trid %hu) failed to complete transfer tag %hu
[%s:%d:%s] ring manager already out of reset
flush_DROPS_LOCK
[%s:%d:%s] (trid %hu) controller reset
[%s:%d:%s] (trid %hu) state=%u, activated=%u
window_base_mask
completed_transfer_log_depth
[%s:%d:%s] entering device sleep
sync_action_process_hi_update
dump_pending_transfer_stats
[%s:%d:%s] creating mtr
BUG in client of Airship: attempted to overwrite driver transport
uint64_value
[%s:%d:%s] crid %hu has unmessaged lifecycle, setting closed
[%s:%d:%s] creating new ring pool for completion ring %s
image_address_hi
[%s:%d:%s] activate
[%s:%d:%s] setting boot controller for ipc stage %s to unavailable
[%s:%d:%s] creating boot controller for %s
BUG in client of Airship: mode must be AIRSHIP_ACIPC_TR_MODE_STANDARD
get_debug_object_alloc_size
[%s:%d:%s] (trid %hu) registering doorbell %s, selector %u
unknown keys present
flush_tr_settlement
[%s:%d:%s] adding crid %hu flush tracking for trid %hu
[%s:%d:%s] reset type: %s
BUG in Airship: invalid src
advance_tail_index
[%s:%d:%s] (bc %s) reseting boot controller
[%s:%d:%s] (trid %hu) new device ring status=%u
CentauriControl
BUG in client of Airship: attempted to reconfigure active CR
append_outstanding_transfer_state
stop_cr
selector
client_registers
header_size
buffer_size_ring
exec_stage_interrupt_occurred
read_index_array
[%s:%d:%s] crid %hu in limbo
[%s:%d:%s] context id %hu has unmessaged lifecycle, setting open
[%s:%d:%s] requesting close for context id %hu
traffic_wake
[%s:%d:%s] syncing mtr tail index update and fetching completions
Role
move_transfers
[%s:%d:%s] creating handle for completion ring with crid %u
BUG in Airship: out of bounds access to boxed array
exec_stages
BUG in Airship: index out of range
start
BUG in Airship: airship_acipc_tr_disconnect: not implemented
v16@?0^v8
exit_reset
BUG in client of Airship: attempted to set external interrupt handler for terminated driver
[%s:%d:%s] (trid %hu) registering interrupt and setting up index array signaler vector %hu
BUG in Airship: attempted to insert null value into boxed dictionary
[%s:%d:%s] trid %hu is settled
completion_group_stride
suspend
[%s:%d:%s] (trid %hu) completions synthesized
buffer
completion_group
get_proxima_platform
get_free_space
probe_exec_stage
[%s:%d:%s] updated exec stage: %u, current %u
set_footer_size
retain_obj
stop_context
[%s:%d:%s] closing context id %hu
[%s:%d:%s] failed to aquire resource for %s
context_info_address_hi
BUG in Airship: access to non-held resource
[%s:%d:%s] no handles available in pool
[%s:%d:%s] sleep status: %s
BUG in Airship: size is too big
release_obj
[%s:%d:%s] exec stage reg value=%u
[%s:%d:%s] setting up mtr
mcr
[%s:%d:%s] (crid %hu) trid %hu does not accept completions from this cr
append_element
save_overflow_message
Vendor
ensure_free_space
~ring_manager
get_flattened_name_sel_string
[%s:%d:%s] requesting close for crid %hu
create_free_space_monitor
add_cr
width
[%s:%d:%s] current main ipc stage and transport must be set
nil
Centauri
[%s:%d:%s] new ipc status=%u
~memregion_manager
write_tr_head_index
config_from_doorbell_spec
[%s:%d:%s] exiting host sleep
interrupt_occurred
[%s:%d:%s] creating handle for transfer ring with trid %u
BUG in Airship: attempted to activate terminated driver
BUG in Airship: bad optional access
[%s:%d:%s] tearing down main ipc stage
get_and_advance_inorder_idx_for_completion
[%s:%d:%s] index %hu
probe_image_response
set_interrupt_execution_queue
BUG in client of Airship: attempted to register handler for inactive driver
get_state
[%s:%d:%s] failed to set client overrides for %s[%u]
[%s:%d:%s] setting external interrupt handler for vector %u
BUG in client of Airship: attempted to reconfigure active driver
create_interrupt
[%s:%d:%s] setting crid %hu open
errata
recompute_region_availability
[%s:%d:%s] (bc %s) sending image
request_tr_close
[%s:%d:%s] (trid %hu) moving queued transfers into pending state
send_image
[%s:%d:%s] updating context info address register
completion_mirror
[%s:%d:%s] (trid %hu) predecessor completion ID %hu does not equal completion ID %hu
BUG in client of Airship: attempted to activate active monitor
[%s:%d:%s] region id %hu conflict %u
swizzle_proxima_viddid_for_platform
ring_pool
remove
BUG in Airship: attempted to create client for terminated driver
BUG in client of Airship: attempted to access inactive mirror
request_context_close
[%s:%d:%s] message failure
[%s:%d:%s] saving overflow message
mem_write16
set_value
add_context
handle_probe_exec_stage
set_device_ring_status
[%s:%d:%s] (bc %s) image response code=%u
[%s:%d:%s] (bc %s) image_state=%u
virtual
[%s:%d:%s] sending overflow messages
[%s:%d:%s] (trid %hu) failed to find first transfer
destroy_client
bad argument
open_cr
value
BUG in Airship: attempted to add duplicate resource
set_cancel_handler
emplace_back
[%s:%d:%s] (crid %hu) open failed 0x%x
direct_client_object.cpp
downlink-update-failure
is_healthy
advance_buffer_pointer
[%s:%d:%s] completion count %hu
with_capacity
[%s:%d:%s] creating doorbell controller for %s[%u]
async_accelerator_private.cpp
[%s:%d:%s] stop reason %u
driver_resource.cpp
BUG in client of Airship: attempt to reconfigure active TR
completion_ring_will_flush
BUG in client of Airship: attempted to await inactive monitor
 %02x
set_tr_open
priority
<nil>
device sleep
consume_elements
BUG in client of Airship: attempted to activate canceled monitor
0x%08x:
check_all_cr_close_requests
is_cr_completion_context_for_tr
window_base_lo
sleep_state_machine
[%s:%d:%s] not ready for exec stage interrupt
host-sleep-failure
add_controller
[%s:%d:%s] (crid %hu) controller closed
[%s:%d:%s] exec_stage during power-on=%u
get_source_maintenance_in_progress
[%s:%d:%s] getting transfer completion for tag %hu
get_maintenance_in_progress
[%s:%d:%s] viddid=%#x
[%s:%d:%s] platform_config=%u, probed viddid=0x%#x,  proxima_viddid=0x%#x
com.apple.airship.global-fallback
[%s:%d:%s] failed to aquire resource for %s[%u]
index_array_vector
handle_append_ipc_driver_state_dump
[%s:%d:%s] setting up boot ipc stage
environment.cpp
CentauriBeta
get_first_free_tag
tr_controller
tr_close_message_completed
[%s:%d:%s] context_open 
doorbell value out of range
[%s:%d:%s] (trid %hu) new doorbell interval (%u us), new leeway (%u us)
acipc.cpp
set_ipc_stage
resume
append
[%s:%d:%s] sending message now
direct_client.cpp
create_client
retain
resources
[%s:%d:%s] ACIPC protocol error 0x%08x (%s)
[%s:%d:%s] (ctxid %hu) sending close message
[%s:%d:%s] handle_activate: result 0x%x
direct_cr_controller.cpp
BUG in client of Airship: attempted to access inactive CR
[%s:%d:%s] trid %hu in limbo
[%s:%d:%s] crid %hu close message result %u
ring_size
probe_exec_stage_register_if_ready
get_device_sw_scaled_timeout
~driver_object_manager
[%s:%d:%s] sending close message for context id %hu
[%s:%d:%s] removing boot controller for ipc stage %s
change_to_exec_stage
[%s:%d:%s] region %s (id=%hu) cannot be used due to id conflict with name %s
~driver_resource
io-timeout
with_cstr_nocopy
[%s:%d:%s] trid %hu has unmessaged lifecycle, setting open
max
multi
image_interrupt
[%s:%d:%s] closing mcr
[%s:%d:%s] (trid %hu) predecessor state %u does not valid
BUG in client of Airship: Failed to locate completion ring config
[%s:%d:%s] trid %hu has unmessaged lifecycle, closing
release_image_transfer_resources
airship-driverkit-timer-watchdog
process_pending
[%s:%d:%s] updating cr close requests
[%s:%d:%s] (crid %hu) do not overwrite existing bad_cd buffer
acipc_driver_client.cpp
merge_location
bank
set_queue
BUG in Airship: bad parameter - 'header_length'
unregister_statedump_collection_handler
completion_footer_size
acquire
set_transfer_footer_size
ring_header_footer_scaling
boot_ipc_stages
[%s:%d:%s] reset=%u, boot_state=%s, ipc_state=%s
[%s:%d:%s] cannot wake
[%s:%d:%s] window_base=%#llx, size=%#llx
[%s:%d:%s] coordinator state=%u, new IPC stage=%s
request_cr_close
context_close_message_completed
[%s:%d:%s] boot manager is already in reset
channel-update-failure
uplink-update-failure
[%s:%d:%s] context id %hu close message requested
set_context
transfer_queue.cpp
v12@?0I8
[%s:%d:%s] (bc %s) detail=%u
constraints not satisfied by default
raise_ipc_error
[%s:%d:%s] failed to allocate/map device memory
[%s:%d:%s] airship sw scaling %llu
[%s:%d:%s] entering reset
device_memory.hpp
system-error
[%s:%d:%s] copying peripheral info, initial exec stage value=%u
add_flusher
destroy_handle
set_doorbell_moderation
[%s:%d:%s] stopping crid %hu for reason %u
unknown
[%s:%d:%s] cannot set transport, %s ipc stage is not null
[%s:%d:%s] payload length %u, appendix length %u
[%s:%d:%s] creating new ring pool for transfer ring %s
populate_state_dump_info
[%s:%d:%s] (crid %hu) invalid completion descriptor at idx=%hu
doorbell value not configured in shared constant mode
window_base_hi
is_sleep_status_valid
BUG in client of Airship: attempted to access inactive context
append_state_dump
[%s:%d:%s] (trid %hu) first transfer not found
write_head_index
boot
request_region_unmap
[%s:%d:%s] message success
[%s:%d:%s] (trid %hu) completing chain
unexpected-sleep-status
set_completion_group
create_device_memory_mapping
teardown_main_ipc_stage
[%s:%d:%s] updating register at bank=%u, offset=%u
probe
[%s:%d:%s] reaping %s[%u]
with_str
~reaper
invalid alignment
window_size
[%s:%d:%s] (ctxid %hu) failed to validate client override
Chipset
write_register
unable to map memory
[%s:%d:%s] ts: last_write %llx, schedule %llx, deadline %llx, 
erase
interrupts
remove_flusher
boot_controller.cpp
register_client_statedump_handler
is_cr_required_completion_context_for_any_open_tr
[%s:%d:%s] region id %hu sending memory map message
append_tr_index_info
BUG in client of Airship: attempted to retrieve first completed tag of ring without completed transfers
bad-tr-ti-update
BUG in Airship: 
[%s:%d:%s] main ipc state is not set
[%s:%d:%s] region id %hu removing memregion_controller
[%s:%d:%s] copying message payload
flush_queued_transfers
set_capacity
BUG in Airship: bad array access
shared_counter
capability
reserve_next
device error
set_tr_closed
None
timedwait
context_controller_block_invoke
set_configuration
[%s:%d:%s] %s[%u] old status %u, new status %u
bytes
set_exec_stage
[%s:%d:%s] (crid %hu) controller opened
[%s:%d:%s] (crid %hu) update bad cd
transfer_header_size
[%s:%d:%s] probing exec stage register
[%s:%d:%s] not ready to probe exec stage register
sleep-failure
[%s:%d:%s] setting trid %hu closed
~reaper_target
resource
shared_constant
completion_header_size
out-of-place completion requires completion ring
completion_ring
Dale
read_tail_index
[%s:%d:%s] main ipc state is not running (%u) or transport is not set
~driver_object_termination_list
[%s:%d:%s] unknown device viddid=%#x
[%s:%d:%s] (trid %hu) first index %hu exceeds size %hu
[%s:%d:%s] (bc %s) detail=0
update_power_state
[%s:%d:%s] failed to get resource
[%s:%d:%s] result=0x%x
ring_manager.cpp
open_context
[%s:%d:%s] stopping trid %hu for reason %u
[%s:%d:%s] context id %hu close message result %u
set_error
[%s:%d:%s] tearing down current ipc stage
[%s:%d:%s] (ctxid %hu) stopping controller
set_open_clientdata
set_client_overrides
compute_state_detail
BUG in Airship: bad boxed access
BUG in Airship: attempted to create cr_controller in driver_client
change_to_ipc_stage
doorbell_coordinator.cpp
disable_interrupt_vector
process_completion_descriptors
BUG in Airship: invalid head index update operation
[%s:%d:%s] (crid %hu) new doorbell interval (%u us), new leeway (%u us)
BUG in client of Airship: attempted to activate monitor with event handlers but without queue
[%s:%d:%s] applied errata window_base_mask=%#llx, masked_base=%#llx
compute_hdrftr_size_fields
BUG in client of Airship: attempted to register handler for terminated driver
open_tr
protocol
insert
set_external_handler
BUG in client of Airship: attempted to activate active driver
[%s:%d:%s] message canceled
[%s:%d:%s] (trid %hu) index %hu exceeds size %hu
BUG in client of Airship: attempted to retrieve first free tag of ring without free space
ipc-running-timeout
[%s:%d:%s] (crid %hu) new availability blockers 0x%08x
BUG in client of Airship: attempted to activate already-active memregion
BUG in Airship: attempted to retrieve max message length in reset
BUG in client of Airship: attempt to reconfigure active context
bad-inplace-completion
[%s:%d:%s] crid %hu has unmessaged lifecycle, setting open
Airship ACIPC protocol error
[%s:%d:%s] sw timeout scale for proxima protium platform: %llu
stop
BUG in client of Airship: attempted to activate interrupt with event handlers but without queue
~ring_pool
[%s:%d:%s] activating doorbell coordinator with %u doorbell instances
BUG in Airship: wrong index
will_set_transport
[%s:%d:%s] driver create client begin %s
buffer_create
set_context_open
[%s:%d:%s] (crid %hu) stopping controller
%zu
ipc_status_interrupt_occurred
[%s:%d:%s] failed to find stage for value, %u
check_async
[%s:%d:%s] stopping context id %hu for reason %u
auxiliary_context
completion_rings
BUG in client of Airship: attempted to reconfigure active memregion
multiple-errors
Airship [%{public}s:%d:%{public}s] (trid %hu) registering doorbell %s, selector %u
Airship [%{public}s:%d:%{public}s] failed to aquire resource for %s
Airship [%{public}s:%d:%{public}s] (bc %s) adding controller to boot manager
Airship [%{public}s:%d:%{public}s] destroying transfer ring handle for trid %hu
Airship [%{public}s:%d:%{public}s] activating %s[%u]
Airship [%{public}s:%d:%{public}s] (trid %hu) transfer flush failed
Airship [%{public}s:%d:%{public}s] sending close message for trid %hu
Airship [%{public}s:%d:%{public}s] context_open %.*P
Airship [%{public}s:%d:%{public}s] (crid %hu) update bad cd
Airship [%{public}s:%d:%{public}s] crid: %u
Airship [%{public}s:%d:%{public}s] stopping trid %hu
Airship [%{public}s:%d:%{public}s] crid %hu is not associated with any open trs
Airship [%{public}s:%d:%{public}s] sleep status: active
Airship [%{public}s:%d:%{public}s] deleted %hu items from mirror
Airship [%{public}s:%d:%{public}s] activate
Airship [%{public}s:%d:%{public}s] stopping crid %hu for reason %u
Airship [%{public}s:%d:%{public}s] tearing down current ipc stage
Airship [%{public}s:%d:%{public}s] Deregistering tail index update handler for trid %hu at vector %hu
Airship [%{public}s:%d:%{public}s] (bc %s) checking for image response
Airship [%{public}s:%d:%{public}s] removed crid %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) completions synthesized
Airship [%{public}s:%d:%{public}s] (trid %hu) update bad transfer completion
Airship [%{public}s:%d:%{public}s] message failed, setting state for region id %hu
Airship [%{public}s:%d:%{public}s] setting up mtr
Airship [%{public}s:%d:%{public}s] resuming doorbell coordinator
Airship [%{public}s:%d:%{public}s] timer deadline missed!!
Airship [%{public}s:%d:%{public}s] associating crid %hu <-> trid %hu
Airship [%{public}s:%d:%{public}s] new ipc stage: %s
Airship [%{public}s:%d:%{public}s] performing health check.
Airship [%{public}s:%d:%{public}s] setting up message rings
Airship [%{public}s:%d:%{public}s] processing completions
Airship [%{public}s:%d:%{public}s] (trid %hu) new mode (%u)
Airship [%{public}s:%d:%{public}s] requesting close for trid %hu
Airship [%{public}s:%d:%{public}s] failed to aquire resource for %s[%u]
Airship [%{public}s:%d:%{public}s] %{public}s
Airship [%{public}s:%d:%{public}s] crid %hu in limbo
Airship [%{public}s:%d:%{public}s] (crid %hu) new availability blockers 0x%08x
Airship [%{public}s:%d:%{public}s] (crid %hu) controller closed
Airship [%{public}s:%d:%{public}s] main ipc stage name %s
Airship [%{public}s:%d:%{public}s] region id %hu sending unmap message
Airship [%{public}s:%d:%{public}s] (ctxid %hu) failed to validate client override
Airship [%{public}s:%d:%{public}s] closing mcr
Airship [%{public}s:%d:%{public}s] failed to flatten name/sel into string
Airship [%{public}s:%d:%{public}s] stopping boot controller for ipc stage %s
Airship [%{public}s:%d:%{public}s] entering reset, dropping any pending doorbells
Airship [%{public}s:%d:%{public}s] result=0x%x
Airship [%{public}s:%d:%{public}s] (crid %hu) failed to complete transfer
Airship [%{public}s:%d:%{public}s] (crid %hu) inserting completion with trid %hu and first tag %hu
Airship [%{public}s:%d:%{public}s] creating mcr
Airship [%{public}s:%d:%{public}s] message canceled
Airship [%{public}s:%d:%{public}s] msi stats overflow: resetting count for vector %u
Airship [%{public}s:%d:%{public}s] (trid %hu) index %hu exceeds size %hu
Airship [%{public}s:%d:%{public}s] destroying completion ring handle for crid %hu
Airship [%{public}s:%d:%{public}s] creating cr controller for %s[%u]
Airship [%{public}s:%d:%{public}s] failed to find stage for value, %u
Airship [%{public}s:%d:%{public}s] main ipc state is not set
Airship [%{public}s:%d:%{public}s] synthesizing completions if needed
Airship [%{public}s:%d:%{public}s] (trid %hu) stopping controller
Airship [%{public}s:%d:%{public}s] reset type=%u
Airship [%{public}s:%d:%{public}s] reset type: %s
Airship [%{public}s:%d:%{public}s] (bc %s) out code=%u
Airship [%{public}s:%d:%{public}s] trid %hu is settled
Airship [%{public}s:%d:%{public}s] boot manager entering reset
Airship [%{public}s:%d:%{public}s] exec stage reg value=%u
Airship [%{public}s:%d:%{public}s] setting up main ipc stage
Airship [%{public}s:%d:%{public}s] (ctxid %hu) new availability blockers 0x%08x
Airship [%{public}s:%d:%{public}s] already in reset
Airship [%{public}s:%d:%{public}s] (bc %s) sending image
Airship [%{public}s:%d:%{public}s] activating doorbell coordinator with %u doorbell instances
Airship [%{public}s:%d:%{public}s] setting context id %hu closed
Airship [%{public}s:%d:%{public}s] removing boot controller for ipc stage %s
Airship [%{public}s:%d:%{public}s] creating tr controller for %s[%u]
Airship [%{public}s:%d:%{public}s] acipc driver activate complete
Airship [%{public}s:%d:%{public}s] setting up boot ipc stage
Airship [%{public}s:%d:%{public}s] setting context id %hu open
Airship [%{public}s:%d:%{public}s] deferring message send
Airship [%{public}s:%d:%{public}s] (trid %hu) first transfer not found
Airship [%{public}s:%d:%{public}s] %s[%u] reset
Airship [%{public}s:%d:%{public}s] (crid %hu) new device ring status=%u
Airship [%{public}s:%d:%{public}s] (trid %hu) close complete
Airship [%{public}s:%d:%{public}s] (trid %hu) state=%u, activated=%u
Airship [%{public}s:%d:%{public}s] ring manager already out of reset
Airship [%{public}s:%d:%{public}s] tr_open %.*P
Airship [%{public}s:%d:%{public}s] (crid %hu) failed to validate client override
Airship [%{public}s:%d:%{public}s] region id %hu removing memregion_controller
Airship [%{public}s:%d:%{public}s] sending overflow messages
Airship [%{public}s:%d:%{public}s] platform_config=%u, probed viddid=0x%#x,  proxima_viddid=0x%#x
Airship [%{public}s:%d:%{public}s] context id %hu status %u
Airship [%{public}s:%d:%{public}s] cr_open %.*P
Airship [%{public}s:%d:%{public}s] (crid %hu) registering with doorbell coordinator with doorbell %s
Airship [%{public}s:%d:%{public}s] (ctxid %hu) close complete
Airship [%{public}s:%d:%{public}s] opening mcr
Airship [%{public}s:%d:%{public}s] setting external execution queue for vector %u
Airship [%{public}s:%d:%{public}s] removing interrupt source %u
Airship [%{public}s:%d:%{public}s] creating new ring pool for completion ring %s
Airship [%{public}s:%d:%{public}s] trid %hu status %u
Airship [%{public}s:%d:%{public}s] tearing down boot ipc stage
Airship [%{public}s:%d:%{public}s] (trid %hu) completing transfer tag %hu
Airship [%{public}s:%d:%{public}s] (bc %s) image valid : %s 
Airship [%{public}s:%d:%{public}s] releasing ring with selector %u
Airship [%{public}s:%d:%{public}s] added %u instances of doorbell %s
Airship [%{public}s:%d:%{public}s] suspending doorbell coordinator
Airship [%{public}s:%d:%{public}s] unexpected GUARD_ELSE failure
Airship [%{public}s:%d:%{public}s] ring manager already in reset
Airship [%{public}s:%d:%{public}s] closing crid %hu
Airship [%{public}s:%d:%{public}s] syncing mtr tail index update and fetching completions
Airship [%{public}s:%d:%{public}s] %s[%u] stopped
Airship [%{public}s:%d:%{public}s] added trid %hu
Airship [%{public}s:%d:%{public}s] setting trid %hu closed
Airship [%{public}s:%d:%{public}s] notifying crid %hu that trid %hu is settled
Airship [%{public}s:%d:%{public}s] (crid %hu) open failed 0x%x
Airship [%{public}s:%d:%{public}s] num of objects pending deletion %u
Airship [%{public}s:%d:%{public}s] tearing down mtr
Airship [%{public}s:%d:%{public}s] (trid %hu) failed to find first transfer
Airship [%{public}s:%d:%{public}s] entering reset
Airship [%{public}s:%d:%{public}s] closing context id %hu
Airship [%{public}s:%d:%{public}s] crid %hu status %u
Airship [%{public}s:%d:%{public}s] crid %hu has unmessaged lifecycle, setting closed
Airship [%{public}s:%d:%{public}s] (crid %hu) sending close message
Airship [%{public}s:%d:%{public}s] window_base=%#llx, size=%#llx
Airship [%{public}s:%d:%{public}s] region id %hu conflict %u
Airship [%{public}s:%d:%{public}s] (ctxid %hu) controller reset
Airship [%{public}s:%d:%{public}s] trid %hu close message result %u
Airship [%{public}s:%d:%{public}s] oversize host memory window reduced from %#llx to UINT32_MAX
Airship [%{public}s:%d:%{public}s] starting messenger
Airship [%{public}s:%d:%{public}s] unknown device viddid=%#x
Airship [%{public}s:%d:%{public}s] no handles available in pool
Airship [%{public}s:%d:%{public}s] (crid %hu) new interrupt %s[%u]
Airship [%{public}s:%d:%{public}s] (trid %hu) failed to complete transfer tag %hu
Airship [%{public}s:%d:%{public}s] ring manager is in reset
Airship [%{public}s:%d:%{public}s] context id %hu set as open
Airship [%{public}s:%d:%{public}s] exec_stage during power-on=%u
Airship [%{public}s:%d:%{public}s] sending open message for crid %hu
Airship [%{public}s:%d:%{public}s] change to exec stage %s (%u) from %s
Airship [%{public}s:%d:%{public}s] viddid=%#x
Airship [%{public}s:%d:%{public}s] (bc %s) image address 0x%llx, length 0x%x
Airship [%{public}s:%d:%{public}s] driver create client end %s
Airship [%{public}s:%d:%{public}s] updated exec stage: %u, current %u
Airship [%{public}s:%d:%{public}s] trid %hu has unmessaged lifecycle, setting open
Airship [%{public}s:%d:%{public}s] stopping context id %hu for reason %u
Airship [%{public}s:%d:%{public}s] failed to allocate/map device memory
Airship [%{public}s:%d:%{public}s] value %u matches to exec stage: %s
Airship [%{public}s:%d:%{public}s] (trid %hu) create tx_queue: size %hu, hdrlen %u, ftrlen %u, out-of-order %u
Airship [%{public}s:%d:%{public}s] %s[%u] old status %u, new status %u
Airship [%{public}s:%d:%{public}s] (crid %hu) invalid hi: %hu
Airship [%{public}s:%d:%{public}s] setting up peripheral info interrupt
Airship [%{public}s:%d:%{public}s] exiting reset
Airship [%{public}s:%d:%{public}s] located transfer ring configuration, adding %u instances
Airship [%{public}s:%d:%{public}s] (trid %hu) new availability blockers 0x%08x
Airship [%{public}s:%d:%{public}s] (trid %hu) failed to validate client override
Airship [%{public}s:%d:%{public}s] (trid %hu) controller closed
Airship [%{public}s:%d:%{public}s] closing trid %hu
Airship [%{public}s:%d:%{public}s] sending open message for context id %hu
Airship [%{public}s:%d:%{public}s] failed to look up configuration for %s
Airship [%{public}s:%d:%{public}s] Registering tail index update handler for trid %hu at vector %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) first index %hu exceeds size %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) sending open message
Airship [%{public}s:%d:%{public}s] trid %hu close message requested
Airship [%{public}s:%d:%{public}s] copying peripheral info, initial exec stage value=%u
Airship [%{public}s:%d:%{public}s] messenger failed to map mtr/mcr memory
Airship [%{public}s:%d:%{public}s] new ipc status=%u
Airship [%{public}s:%d:%{public}s] not ready for peripheral info interrupt
Airship [%{public}s:%d:%{public}s] type=%u, debug meta-data=0x%llx, name=%s
Airship [%{public}s:%d:%{public}s] (trid %hu) controller reset
Airship [%{public}s:%d:%{public}s] crid %hu belongs to the same group as %hu
Airship [%{public}s:%d:%{public}s] boot manager is in reset
Airship [%{public}s:%d:%{public}s] creating doorbell controller for %s[%u]
Airship [%{public}s:%d:%{public}s] sending any overflow messages
Airship [%{public}s:%d:%{public}s] completion count %hu
Airship [%{public}s:%d:%{public}s] saving overflow message
Airship [%{public}s:%d:%{public}s] (trid %hu) new interrupt %s[%u]
Airship [%{public}s:%d:%{public}s] (trid %hu) failed: hi=%hu, ti=%hu
Airship [%{public}s:%d:%{public}s] ipc status invalid
Airship [%{public}s:%d:%{public}s] updating register at bank=%u, offset=%u
Airship [%{public}s:%d:%{public}s] copying appendix
Airship [%{public}s:%d:%{public}s] message success
Airship [%{public}s:%d:%{public}s] (trid %hu) attempt to consume %hu transfers, %hu fetched
Airship [%{public}s:%d:%{public}s] (trid %hu) new doorbell interval (%u us), new leeway (%u us)
Airship [%{public}s:%d:%{public}s] (bc %s) no image response code
Airship [%{public}s:%d:%{public}s] (trid %hu) sending close message
Airship [%{public}s:%d:%{public}s] crid %hu has unmessaged lifecycle, closing
Airship [%{public}s:%d:%{public}s] failed to get device memory window config
Airship [%{public}s:%d:%{public}s] getting transfer completion for tag %hu
Airship [%{public}s:%d:%{public}s] image response %u, code %u
Airship [%{public}s:%d:%{public}s] ts: last_write %llx, schedule %llx, deadline %llx, 
Airship [%{public}s:%d:%{public}s] in_reset %u, activated %u
Airship [%{public}s:%d:%{public}s] setting client overrides for %s[%u]
Airship [%{public}s:%d:%{public}s] setting crid %hu open
Airship [%{public}s:%d:%{public}s] adding boot controller for ipc stage %s
Airship [%{public}s:%d:%{public}s] not ready to probe exec stage register
Airship [%{public}s:%d:%{public}s] exec stage interrupt occurred: value %u
Airship [%{public}s:%d:%{public}s] updated error state: %u, current %u
Airship [%{public}s:%d:%{public}s] mapping region of size %u for %s[%u]
Airship [%{public}s:%d:%{public}s] (trid %hu) do not overwrite existing bad tx completion buffer
Airship [%{public}s:%d:%{public}s] setting crid %hu closed
Airship [%{public}s:%d:%{public}s] crid %hu open message result %u
Airship %s %s@%u
Airship [%{public}s:%d:%{public}s] (crid %hu) trid %hu does not accept completions from this cr
Airship [%{public}s:%d:%{public}s] creating boot controller for %s
Airship [%{public}s:%d:%{public}s] not ready for exec stage interrupt
Airship [%{public}s:%d:%{public}s] creating mtr
Airship [%{public}s:%d:%{public}s] (trid %hu) unexpected flush notice from CRID %hu
Airship [%{public}s:%d:%{public}s] trid %hu set as open
Airship [%{public}s:%d:%{public}s] no custom statedump handlers registered
Airship [%{public}s:%d:%{public}s] (crid %hu) applied client overrides
Airship [%{public}s:%d:%{public}s] entering host sleep
Airship [%{public}s:%d:%{public}s] applied errata window_base_mask=%#llx, masked_base=%#llx
Airship [%{public}s:%d:%{public}s] region id %hu sending memory map message
Airship [%{public}s:%d:%{public}s] opening mtr
Airship [%{public}s:%d:%{public}s] trid %hu has unmessaged lifecycle, closing
Airship [%{public}s:%d:%{public}s] sending open message for trid %hu
Airship [%{public}s:%d:%{public}s] image has already been sent
Airship [%{public}s:%d:%{public}s] (crid %hu) reaping cr
Airship [%{public}s:%d:%{public}s] sleep status: %s
Airship [%{public}s:%d:%{public}s] (ctxid %hu) applied client overrides
Airship [%{public}s:%d:%{public}s] adding interrupt source %u
Airship [%{public}s:%d:%{public}s] dbs : total %lu, active %lu, pending %d
Airship [%{public}s:%d:%{public}s] boot manager is already out of reset
Airship [%{public}s:%d:%{public}s] (crid %hu) controller reset
Airship [%{public}s:%d:%{public}s] (ctxid %hu) controller state=%u, detail=%u
Airship [%{public}s:%d:%{public}s] (bc %s) stopping boot controller
Airship [%{public}s:%d:%{public}s] driver create client begin %s
Airship [%{public}s:%d:%{public}s] %s[%u] unavailable
Airship [%{public}s:%d:%{public}s] context id %hu has unmessaged lifecycle, closing
Airship [%{public}s:%d:%{public}s] context id %hu open message result %u
Airship [%{public}s:%d:%{public}s] (crid %hu) registering interrupt and setting up index array signaler vector %hu
Airship [%{public}s:%d:%{public}s] (crid %hu) cr terminated
Airship [%{public}s:%d:%{public}s] sleep status: host sleep
Airship [%{public}s:%d:%{public}s] (trid %hu) free transfers %hu must exceed dead space size %hu
Airship [%{public}s:%d:%{public}s] reset type %u
Airship [%{public}s:%d:%{public}s] trid %hu open message result %u
Airship [%{public}s:%d:%{public}s] invalid configuration: %s at %s
Airship [%{public}s:%d:%{public}s] creating device memory
Airship [%{public}s:%d:%{public}s] ACIPC protocol error 0x%08x (%s)
Airship [%{public}s:%d:%{public}s] IPC handshake timer expired
Airship [%{public}s:%d:%{public}s] (trid %hu) predecessor completion ID %hu does not equal completion ID %hu
Airship [%{public}s:%d:%{public}s] controller ipc stage: %s
Airship [%{public}s:%d:%{public}s] image sent for ipc stage %s
Airship [%{public}s:%d:%{public}s] (ctxid %hu) reaping context controller
Airship [%{public}s:%d:%{public}s] index %hu
Airship [%{public}s:%d:%{public}s] Added context id %hu
Airship [%{public}s:%d:%{public}s] no ipc stage set
Airship [%{public}s:%d:%{public}s] enqueuing message in mtr
Airship [%{public}s:%d:%{public}s] (bc %s) image sent, recomputing state
Airship [%{public}s:%d:%{public}s] exiting host sleep
Airship [%{public}s:%d:%{public}s] removed context id %hu
Airship [%{public}s:%d:%{public}s] crid %hu is associated with trid %hu
Airship [%{public}s:%d:%{public}s] creating memregion controller for %s[%u]
Airship [%{public}s:%d:%{public}s] reset=%u, boot_state=%s, ipc_state=%s
Airship [%{public}s:%d:%{public}s] cannot set transport, %s ipc stage is not null
Airship [%{public}s:%d:%{public}s] syncing mcr head index update
Airship [%{public}s:%d:%{public}s] message failure
Airship [%{public}s:%d:%{public}s] (trid %hu) open failed 0x%x
Airship [%{public}s:%d:%{public}s] (trid %hu) new device ring status=%u
Airship [%{public}s:%d:%{public}s] setting trid %hu open
Airship [%{public}s:%d:%{public}s] (crid %hu) stopping controller
Airship [%{public}s:%d:%{public}s] adding %u instances of resource %s
Airship [%{public}s:%d:%{public}s] (bc %s) detail=0
Airship [%{public}s:%d:%{public}s] reserving ring with selector %u
Airship [%{public}s:%d:%{public}s] value for shared constant doorbell: %u
Airship [%{public}s:%d:%{public}s] requesting close for crid %hu
Airship [%{public}s:%d:%{public}s] requesting close for context id %hu
Airship [%{public}s:%d:%{public}s] (crid %hu) invalid completion descriptor at idx=%hu
Airship [%{public}s:%d:%{public}s] entering device sleep
Airship [%{public}s:%d:%{public}s] setting up message buffer for main ipc stage %s
Airship [%{public}s:%d:%{public}s] creating new ring pool for transfer ring %s
Airship [%{public}s:%d:%{public}s] handle_activate: result 0x%x
Airship [%{public}s:%d:%{public}s] updated power state: %u, current %u
Airship [%{public}s:%d:%{public}s] (trid %hu) controller opened
Airship [%{public}s:%d:%{public}s] (trid %hu) invalid in-place completion at idx=%hu
Airship [%{public}s:%d:%{public}s] acquiring resource %s
Airship [%{public}s:%d:%{public}s] updating cr close requests
Airship [%{public}s:%d:%{public}s] Registering head index update handler for crid %hu at vector %hu
Airship [%{public}s:%d:%{public}s] copying message payload
Airship [%{public}s:%d:%{public}s] object manager list not empty; dumping direct client objects
Airship [%{public}s:%d:%{public}s] map successful
Airship [%{public}s:%d:%{public}s] region id %hu adding memregion_controller
Airship [%{public}s:%d:%{public}s] setting external interrupt handler for vector %u
Airship [%{public}s:%d:%{public}s] (trid %hu) offset %hu exceeds fetched transfer count %hu
Airship [%{public}s:%d:%{public}s] creating handle for completion ring with crid %u
Airship [%{public}s:%d:%{public}s] IPC driver state_dump complete
Airship [%{public}s:%d:%{public}s] (crid %hu) new doorbell interval (%u us), new leeway (%u us)
Airship [%{public}s:%d:%{public}s] context id %hu has unmessaged lifecycle, setting closed
Airship [%{public}s:%d:%{public}s] setting boot controller for ipc stage %s to unavailable
Airship [%{public}s:%d:%{public}s] (ctxid %hu) open failed 0x%x
Airship [%{public}s:%d:%{public}s] sw timeout scale for proxima protium platform: %llu
Airship [%{public}s:%d:%{public}s] consuming transfers
Airship [%{public}s:%u:%{public}s] unexpected nonzero error code 0x%llx
Airship [%{public}s:%d:%{public}s] stopping context id %hu
Airship [%{public}s:%d:%{public}s] crid %hu has unmessaged lifecycle, setting open
Airship [%{public}s:%d:%{public}s] context id %hu in limbo
Airship [%{public}s:%d:%{public}s] stopping trid %hu for reason %u
Airship [%{public}s:%d:%{public}s] updating context close requests
Airship [%{public}s:%d:%{public}s] ipc handshake complete
Airship [%{public}s:%d:%{public}s] no exec stage found for value %u
Airship [%{public}s:%d:%{public}s] region id %hu deferring unmap message
Airship [%{public}s:%d:%{public}s] (trid %hu) invalid ti: %hu
Airship [%{public}s:%d:%{public}s] setting up ipc status interrupt
Airship [%{public}s:%d:%{public}s] created completion mirror object
Airship [%{public}s:%d:%{public}s] payload length %u, appendix length %u
Airship [%{public}s:%d:%{public}s] context id %hu has unmessaged lifecycle, setting open
Airship [%{public}s:%d:%{public}s] unmapping memory region for %s[%u]
Airship [%{public}s:%d:%{public}s] added crid %hu
Airship [%{public}s:%d:%{public}s] failed to get resource
Airship [%{public}s:%d:%{public}s] stop reason %u
Airship [%{public}s:%d:%{public}s] stopping crid %hu
Airship [%{public}s:%d:%{public}s] boot ipc stage name %s
Airship [%{public}s:%d:%{public}s] ipc status=%u
Airship [%{public}s:%d:%{public}s] not ready for ipc status interrupt
Airship [%{public}s:%d:%{public}s] (bc %s) image response code=%u
Airship [%{public}s:%d:%{public}s] adding crid %hu flush tracking for trid %hu
Airship [%{public}s:%d:%{public}s] (crid %hu) close complete
Airship [%{public}s:%d:%{public}s] ipc stage not torn down, boot stage valid: %u, main stage valid: %u
Airship [%{public}s:%d:%{public}s] tearing down mcr
Airship [%{public}s:%d:%{public}s] setting up mcr
Airship [%{public}s:%d:%{public}s] sending message now
Airship [%{public}s:%d:%{public}s] (trid %hu) predecessor state %u does not valid
Airship [%{public}s:%d:%{public}s] reserve %u complete
Airship [%{public}s:%d:%{public}s] context id %hu close message requested
Airship [%{public}s:%d:%{public}s] (crid %hu) do not overwrite existing bad_cd buffer
Airship [%{public}s:%d:%{public}s] sleep status invalid
Airship [%{public}s:%d:%{public}s] region id %hu exec stage mismatch %u
Airship [%{public}s:%d:%{public}s] unknown proxima-platform: %llu
Airship [%{public}s:%d:%{public}s] invoking action
Airship [%{public}s:%d:%{public}s] (trid %hu) tag %hu must belong to first in chain
Airship [%{public}s:%d:%{public}s] %s[%u] state %u, detail 0x%u
Airship [%{public}s:%d:%{public}s] probing exec stage register
Airship [%{public}s:%d:%{public}s] main ipc state is not running (%u) or transport is not set
Airship [%{public}s:%d:%{public}s] index %hu, message length %u
Airship [%{public}s:%d:%{public}s] failed to look up configuration for %s[%u]
Airship [%{public}s:%d:%{public}s] updating context info address register
Airship [%{public}s:%d:%{public}s] (trid %hu) transfer tag %hu does not match next in-order tag %hu
Airship [%{public}s:%d:%{public}s] (bc %s) image_state=%u
Airship [%{public}s:%d:%{public}s] coordinator state=%u, new IPC stage=%s
Airship [%{public}s:%d:%{public}s] reaping %s[%u]
Airship [%{public}s:%d:%{public}s] region id %hu is in limbo, attempting to unmap
Airship [%{public}s:%d:%{public}s] messenger already out of reset
Airship [%{public}s:%d:%{public}s] (trid %hu) seek %hu exceeds pending transfer count %hu
Airship [%{public}s:%d:%{public}s] (bc %s) computing image table
Airship [%{public}s:%d:%{public}s] failed to set client overrides for %s[%u]
Airship [%{public}s:%d:%{public}s] sending close message for crid %hu
Airship [%{public}s:%d:%{public}s] (crid %hu) sending open message
Airship [%{public}s:%d:%{public}s] (crid %hu) controller opened
Airship [%{public}s:%d:%{public}s] tearing down main ipc stage
Airship [%{public}s:%d:%{public}s] cannot wake
Airship [%{public}s:%d:%{public}s] (trid %hu) transfer enqueue size %u exceeds maximum transfer size %u
Airship [%{public}s:%d:%{public}s] (trid %hu) moving queued transfers into pending state
Airship [%{public}s:%d:%{public}s] (trid %hu) free=%hu, queued=%hu, pending=%hu, completed=%hu, fetched=%hu
Airship [%{public}s:%d:%{public}s] sending close message for context id %hu
Airship [%{public}s:%d:%{public}s] boot manager exiting reset
Airship [%{public}s:%d:%{public}s] current main ipc stage and transport must be set
Airship [%{public}s:%d:%{public}s] starting ipc handshake timer; timeout=%u ms
Airship [%{public}s:%d:%{public}s] removing participant 0x%llx from pending queue
Airship [%{public}s:%d:%{public}s] region %s (id=%hu) cannot be used due to name conflict with id %hu
Airship [%{public}s:%d:%{public}s] (ctxid %hu) sending close message
Airship [%{public}s:%d:%{public}s] (bc %s) reseting boot controller
Airship [%{public}s:%d:%{public}s] (trid %hu) TR is now settled
Airship [%{public}s:%d:%{public}s] removed trid %hu
Airship [%{public}s:%d:%{public}s] creating context controller for %s[%u]
Airship [%{public}s:%d:%{public}s] wake requested=%u, target host sleep=%u, permit device sleep=%u
Airship [%{public}s:%d:%{public}s] closing mtr
Airship [%{public}s:%d:%{public}s] (trid %hu) transfer at index %hu is in state %u
Airship [%{public}s:%d:%{public}s] located completion ring configuration, adding %u instances
Airship [%{public}s:%d:%{public}s] message success, setting state for region id %hu
Airship [%{public}s:%d:%{public}s] (ctxid %hu) stopping controller
Airship [%{public}s:%d:%{public}s] new item at index %hu
Airship [%{public}s:%d:%{public}s] (trid %hu) completing chain
Airship [%{public}s:%d:%{public}s] (bc %s) detail=%u
Airship [%{public}s:%d:%{public}s] (bc %s) old state=0x%llx, new state=0x%llx
Airship [%{public}s:%d:%{public}s] creating handle for transfer ring with trid %u
Airship [%{public}s:%d:%{public}s] participant 0x%llx added to doorbell %s[%u]
Airship [%{public}s:%d:%{public}s] (trid %hu) registering interrupt and setting up index array signaler vector %hu
Airship [%{public}s:%d:%{public}s] recomputing closed ring availability
Airship [%{public}s:%d:%{public}s] trid %hu in limbo
Airship [%{public}s:%d:%{public}s] crid %hu close message result %u
Airship [%{public}s:%d:%{public}s] context id %hu close message result %u
Airship [%{public}s:%d:%{public}s] boot manager is already in reset
Airship [%{public}s:%d:%{public}s] region %s (id=%hu) cannot be used due to id conflict with name %s
Airship [%{public}s:%d:%{public}s] airship sw scaling %llu
```
