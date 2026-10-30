# `/System/Library/PrivateFrameworks/AirshipCentauriHelper.framework/AirshipCentauriHelper`

From the upgrade restore ramdisk (141-29011-104.dmg). 186,432 bytes.

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
emplace_back
[%s:%d:%s] unexpected error code (0x%08x)
com.apple.airship.centauri-helper
typed_allocators.hpp
send_image
[%s:%d:%s] stage_id=%u, timeout=%u ms
[%s:%d:%s] unexpected error code 0x%08x
wait_for_rx_DROPS_LOCK
[%s:%d:%s] invoke stop_handler
BUG in client of Airship: attempted to reconfigure open handle
[%s:%d:%s] sendImage: disconnected
consume_tx
mappable_buffer.cpp
IOUserService
consume_result
write_register
read
impl_peek_read
write
impl_prepare_write
BUG in Airship: invalid head index advance operation
Role
BUG in Airship: bad optional access
[%s:%d:%s] complete
get_page_size
exec_invoke_driver_open
Vendor
get_ring_sizes
stage_tx_meta
termination_notifier
set_ring_sizes
set_buffer_info
wait_for_write
impl_commit_write
airship_ch_interface_create
ring_index_pair.hpp
boot.cpp
set_write_handler
BUG in Airship: invalid tail index advance operation
advance_head_index
airship_ch_boot_image_buffer_create
CentauriAlpha
impl_wait_for_read_DROPS_LOCK
interface.cpp
ring_index_pair
BUG in Airship: invalid head index update operation
wait_for_read
BUG in client of Airship: attempted blocking write with handler active
impl_wait_for_write_DROPS_LOCK
BUG in client of Airship: attempted commit_write without preceding prepare_write
BUG in Airship: ring size cannot be zero
set_interposer_id
consume_read
[%s:%d:%s] interface not open
set_event_handler
set_close_handler
service_matcher
BUG in Airship: bad array access
BUG in Airship: access to null buffer
[%s:%d:%s] invoke stop handler
[%s:%d:%s] sendImage: service inactive
[%s:%d:%s] sendImage: timed out
prepare_write
set_queue
optional.hpp
reduce_size
CentauriBeta
BUG in client of Airship: attempted blocking read with handler active
com.apple.airship.centauri-helper.timesync
cancel
com.apple.airship.centauri-helper.boot
refill_rx
disconnect_from_service
IOUserClass
IOPropertyMatch
operator[]
value
common.cpp
IOGeneralInterest
start_tx
peek_read
fetch_rx
advance_tail_index
start
BUG in client of Airship: attempted to open already-open handle
round_up_to_page_size
exec_await_service
dynamic_array.hpp
wait_for_tx_DROPS_LOCK
update_head_index
log
execute
exec_done
memregion.cpp
IOServiceFirstMatch
[%s:%d:%s] creating mappable buffer of size %u
close
[%s:%d:%s] 
open
buffer
BUG in Airship: invalid tail index update operation
timesync.cpp
com.apple.airship.centauri-helper.memregion
runloop_runner
CentauriControl
start_rx
BUG in client of Airship: attempted consume_read without preceding peek_read
impl_consume_read
BUG in client of Airship: attempted oversize commit_write
get_addr
stop_notifier
flush_tx
airship_ch_interface_destroy
BUG in client of Airship: attempted to open without queue
AirshipDriverDK
exec_open_service
operator()
ALLOCATION FAILURE (or BUG) in Airship
read_register
disconnect
com.apple.airship.centauri-helper.interface
[%s:%d:%s] read: count=%u, size=%u, write count=%u, size=%u
state_machine
v8@?0
airship-debug
airship_ch_memregion_buffer_create
[%s:%d:%s] sendImage: timed out status=%llu, response=%#x
set_read_handler
[%s:%d:%s] cancelling pending open
[%s:%d:%s] unable to map buffer
[%s:%d:%s] interface disconnected
BUG in Airship: 
[%s:%d:%s] force=%u
[%s:%d:%s] sendImage: status=%llu, response=%#x
commit_write
[%s:%d:%s] interface_id=%u, timeout=%u ms
set_stop_handler
create
run
exec_await_retry_flush
stage_rx_meta
exec_set_up_matcher
typed_delete
[%s:%d:%s] sendImage: result=%#x
BUG in client of Airship: attempted oversize consume_read
update_tail_index
logging.cpp
Centauri
Airship [%{public}s:%d:%{public}s] read: count=%u, size=%u, write count=%u, size=%u
Airship [%{public}s:%d:%{public}s] unable to map buffer
Airship [%{public}s:%d:%{public}s] cancelling pending open
Airship [%{public}s:%d:%{public}s] force=%u
Airship [%{public}s:%d:%{public}s] sendImage: disconnected
Airship [%{public}s:%d:%{public}s] sendImage: status=%llu, response=%#x
Airship [%{public}s:%d:%{public}s] creating mappable buffer of size %u
Airship [%{public}s:%d:%{public}s] interface_id=%u, timeout=%u ms
Airship [%{public}s:%d:%{public}s] unexpected GUARD_ELSE failure
Airship [%{public}s:%d:%{public}s] complete
Airship [%{public}s:%d:%{public}s] sendImage: service inactive
Airship [%{public}s:%d:%{public}s] sendImage: timed out
Airship [%{public}s:%d:%{public}s] unexpected error code (0x%08x)
Airship [%{public}s:%d:%{public}s] interface not open
Airship [%{public}s:%d:%{public}s] sendImage: result=%#x
Airship [%{public}s:%d:%{public}s] invoke stop_handler
Airship [%{public}s:%d:%{public}s] interface disconnected
Airship [%{public}s:%d:%{public}s] %{public}s
Airship [%{public}s:%u:%{public}s] unexpected nonzero error code 0x%llx
Airship [%{public}s:%d:%{public}s] 
Airship [%{public}s:%d:%{public}s] stage_id=%u, timeout=%u ms
Airship [%{public}s:%d:%{public}s] invoke stop handler
Airship [%{public}s:%d:%{public}s] unexpected error code 0x%08x
Airship [%{public}s:%d:%{public}s] sendImage: timed out status=%llu, response=%#x
```
