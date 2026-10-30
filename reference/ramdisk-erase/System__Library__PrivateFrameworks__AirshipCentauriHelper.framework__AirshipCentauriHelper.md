# `/System/Library/PrivateFrameworks/AirshipCentauriHelper.framework/AirshipCentauriHelper`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 186,432 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2320)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/System/Library/PrivateFrameworks/AirshipCentauriHelper.framework/AirshipCentauriHelper (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/Airship.framework/Airship (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (172)

```
set_ring_sizes
set_buffer_info
fetch_rx
consume_tx
[%s:%d:%s] read: count=%u, size=%u, write count=%u, size=%u
BUG in Airship: access to null buffer
run
exec_done
BUG in client of Airship: attempted oversize consume_read
stage_tx_meta
dynamic_array.hpp
wait_for_read
round_up_to_page_size
[%s:%d:%s] force=%u
airship-debug
BUG in client of Airship: attempted to open without queue
Centauri
IOServiceFirstMatch
stop_notifier
optional.hpp
BUG in client of Airship: attempted commit_write without preceding prepare_write
read_register
com.apple.airship.centauri-helper.interface
impl_peek_read
[%s:%d:%s] stage_id=%u, timeout=%u ms
get_ring_sizes
advance_head_index
logging.cpp
IOUserClass
exec_set_up_matcher
exec_open_service
operator()
read
commit_write
execute
typed_allocators.hpp
ring_index_pair
update_head_index
BUG in Airship: bad array access
impl_wait_for_write_DROPS_LOCK
set_close_handler
BUG in Airship: bad optional access
write_register
CentauriBeta
refill_rx
airship_ch_interface_destroy
exec_invoke_driver_open
[%s:%d:%s] sendImage: result=%#x
[%s:%d:%s] sendImage: status=%llu, response=%#x
disconnect
write
BUG in client of Airship: attempted oversize commit_write
log
cancel
common.cpp
reduce_size
BUG in client of Airship: attempted blocking read with handler active
wait_for_write
BUG in Airship: invalid tail index update operation
memregion.cpp
set_queue
create
[%s:%d:%s] sendImage: service inactive
stage_rx_meta
[%s:%d:%s] complete
[%s:%d:%s] interface disconnected
ring_index_pair.hpp
AirshipDriverDK
termination_notifier
emplace_back
advance_tail_index
com.apple.airship.centauri-helper.memregion
com.apple.airship.centauri-helper
set_read_handler
BUG in Airship: invalid tail index advance operation
set_event_handler
set_stop_handler
get_addr
Vendor
Role
exec_await_retry_flush
[%s:%d:%s] sendImage: timed out
BUG in client of Airship: attempted blocking write with handler active
impl_prepare_write
[%s:%d:%s] invoke stop_handler
BUG in Airship: invalid head index advance operation
prepare_write
BUG in client of Airship: attempted to reconfigure open handle
airship_ch_memregion_buffer_create
get_page_size
impl_consume_read
value
CentauriAlpha
start_rx
airship_ch_interface_create
[%s:%d:%s] cancelling pending open
disconnect_from_service
set_write_handler
impl_wait_for_read_DROPS_LOCK
peek_read
update_tail_index
airship_ch_boot_image_buffer_create
[%s:%d:%s] sendImage: timed out status=%llu, response=%#x
start_tx
BUG in client of Airship: attempted consume_read without preceding peek_read
wait_for_rx_DROPS_LOCK
wait_for_tx_DROPS_LOCK
[%s:%d:%s] interface_id=%u, timeout=%u ms
BUG in client of Airship: attempted to open already-open handle
com.apple.airship.centauri-helper.timesync
mappable_buffer.cpp
runloop_runner
BUG in Airship: 
state_machine
exec_await_service
IOGeneralInterest
IOUserService
send_image
[%s:%d:%s] unexpected error code 0x%08x
[%s:%d:%s] sendImage: disconnected
flush_tx
[%s:%d:%s] unexpected error code (0x%08x)
timesync.cpp
start
consume_result
BUG in Airship: invalid head index update operation
close
ALLOCATION FAILURE (or BUG) in Airship
interface.cpp
consume_read
[%s:%d:%s] 
open
service_matcher
buffer
[%s:%d:%s] unable to map buffer
v8@?0
boot.cpp
CentauriControl
[%s:%d:%s] invoke stop handler
[%s:%d:%s] creating mappable buffer of size %u
impl_commit_write
BUG in Airship: ring size cannot be zero
IOPropertyMatch
operator[]
set_interposer_id
typed_delete
com.apple.airship.centauri-helper.boot
[%s:%d:%s] interface not open
Airship [%{public}s:%d:%{public}s] invoke stop handler
Airship [%{public}s:%d:%{public}s] unexpected error code 0x%08x
Airship [%{public}s:%d:%{public}s] sendImage: disconnected
Airship [%{public}s:%d:%{public}s] interface_id=%u, timeout=%u ms
Airship [%{public}s:%d:%{public}s] unable to map buffer
Airship [%{public}s:%d:%{public}s] complete
Airship [%{public}s:%d:%{public}s] force=%u
Airship [%{public}s:%d:%{public}s] sendImage: timed out
Airship [%{public}s:%d:%{public}s] sendImage: result=%#x
Airship [%{public}s:%d:%{public}s] read: count=%u, size=%u, write count=%u, size=%u
Airship [%{public}s:%u:%{public}s] unexpected nonzero error code 0x%llx
Airship [%{public}s:%d:%{public}s] sendImage: service inactive
Airship [%{public}s:%d:%{public}s] sendImage: status=%llu, response=%#x
Airship [%{public}s:%d:%{public}s] creating mappable buffer of size %u
Airship [%{public}s:%d:%{public}s] invoke stop_handler
Airship [%{public}s:%d:%{public}s] interface not open
Airship [%{public}s:%d:%{public}s] %{public}s
Airship [%{public}s:%d:%{public}s] unexpected GUARD_ELSE failure
Airship [%{public}s:%d:%{public}s] cancelling pending open
Airship [%{public}s:%d:%{public}s] stage_id=%u, timeout=%u ms
Airship [%{public}s:%d:%{public}s] sendImage: timed out status=%llu, response=%#x
Airship [%{public}s:%d:%{public}s] unexpected error code (0x%08x)
Airship [%{public}s:%d:%{public}s] interface disconnected
Airship [%{public}s:%d:%{public}s] 
```
