# `/System/Library/PrivateFrameworks/AirshipCentauriHelper.framework/AirshipCentauriHelper`

iOS 27.2 dyld shared cache image. Version `592.0.3.0.0`. **[DSC]**

## Linked libraries (5)

- `/System/Library/PrivateFrameworks/Airship.framework/Airship`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`

## Strings (172)

```
stop_notifier
[%s:%d:%s] read: count=%u, size=%u, write count=%u, size=%u
ring_index_pair
Vendor
[%s:%d:%s] sendImage: timed out status=%llu, response=%#x
fetch_rx
set_close_handler
BUG in client of Airship: attempted to open already-open handle
ALLOCATION FAILURE (or BUG) in Airship
BUG in Airship: 
optional.hpp
BUG in client of Airship: attempted blocking read with handler active
operator()
BUG in client of Airship: attempted blocking write with handler active
advance_tail_index
BUG in Airship: invalid tail index update operation
set_stop_handler
value
stage_rx_meta
impl_prepare_write
wait_for_tx_DROPS_LOCK
[%s:%d:%s] interface disconnected
exec_set_up_matcher
operator[]
write_register
send_image
[%s:%d:%s] sendImage: result=%#x
set_buffer_info
airship_ch_interface_destroy
BUG in Airship: ring size cannot be zero
advance_head_index
BUG in client of Airship: attempted to open without queue
[%s:%d:%s] invoke stop handler
[%s:%d:%s] sendImage: service inactive
[%s:%d:%s] sendImage: status=%llu, response=%#x
ring_index_pair.hpp
airship_ch_memregion_buffer_create
round_up_to_page_size
Centauri
state_machine
wait_for_write
set_queue
typed_delete
impl_commit_write
BUG in Airship: bad optional access
read_register
[%s:%d:%s] creating mappable buffer of size %u
BUG in client of Airship: attempted consume_read without preceding peek_read
commit_write
start
common.cpp
set_read_handler
CentauriAlpha
start_rx
wait_for_rx_DROPS_LOCK
[%s:%d:%s] cancelling pending open
[%s:%d:%s] invoke stop_handler
com.apple.airship.centauri-helper.timesync
airship-debug
com.apple.airship.centauri-helper.boot
[%s:%d:%s] unexpected error code 0x%08x
consume_read
refill_rx
set_event_handler
runloop_runner
exec_await_service
buffer
com.apple.airship.centauri-helper.interface
BUG in client of Airship: attempted oversize consume_read
timesync.cpp
[%s:%d:%s] force=%u
[%s:%d:%s] sendImage: timed out
set_write_handler
write
BUG in client of Airship: attempted commit_write without preceding prepare_write
IOUserClass
CentauriControl
impl_consume_read
com.apple.airship.centauri-helper
[%s:%d:%s] 
IOUserService
IOServiceFirstMatch
consume_result
exec_open_service
disconnect
start_tx
memregion.cpp
read
log
create
BUG in Airship: access to null buffer
run
[%s:%d:%s] sendImage: disconnected
get_ring_sizes
[%s:%d:%s] unexpected error code (0x%08x)
logging.cpp
BUG in client of Airship: attempted to reconfigure open handle
emplace_back
BUG in Airship: invalid head index update operation
exec_await_retry_flush
dynamic_array.hpp
set_ring_sizes
flush_tx
BUG in Airship: invalid tail index advance operation
BUG in Airship: invalid head index advance operation
execute
boot.cpp
reduce_size
BUG in client of Airship: attempted oversize commit_write
update_head_index
close
typed_allocators.hpp
CentauriBeta
impl_wait_for_read_DROPS_LOCK
[%s:%d:%s] unable to map buffer
open
mappable_buffer.cpp
get_addr
service_matcher
impl_wait_for_write_DROPS_LOCK
airship_ch_interface_create
exec_done
v8@?0
cancel
IOGeneralInterest
exec_invoke_driver_open
interface.cpp
prepare_write
[%s:%d:%s] interface not open
com.apple.airship.centauri-helper.memregion
impl_peek_read
[%s:%d:%s] interface_id=%u, timeout=%u ms
stage_tx_meta
update_tail_index
disconnect_from_service
AirshipDriverDK
Role
[%s:%d:%s] stage_id=%u, timeout=%u ms
[%s:%d:%s] complete
termination_notifier
peek_read
get_page_size
consume_tx
BUG in Airship: bad array access
airship_ch_boot_image_buffer_create
set_interposer_id
wait_for_read
IOPropertyMatch
Airship [%{public}s:%d:%{public}s] interface disconnected
Airship [%{public}s:%d:%{public}s] %{public}s
Airship [%{public}s:%d:%{public}s] unexpected GUARD_ELSE failure
Airship [%{public}s:%d:%{public}s] 
Airship [%{public}s:%d:%{public}s] complete
Airship [%{public}s:%d:%{public}s] sendImage: result=%#x
Airship [%{public}s:%d:%{public}s] sendImage: status=%llu, response=%#x
Airship [%{public}s:%d:%{public}s] read: count=%u, size=%u, write count=%u, size=%u
Airship [%{public}s:%u:%{public}s] unexpected nonzero error code 0x%llx
Airship [%{public}s:%d:%{public}s] force=%u
Airship [%{public}s:%d:%{public}s] sendImage: service inactive
Airship [%{public}s:%d:%{public}s] sendImage: timed out
Airship [%{public}s:%d:%{public}s] creating mappable buffer of size %u
Airship [%{public}s:%d:%{public}s] cancelling pending open
Airship [%{public}s:%d:%{public}s] stage_id=%u, timeout=%u ms
Airship [%{public}s:%d:%{public}s] sendImage: disconnected
Airship [%{public}s:%d:%{public}s] sendImage: timed out status=%llu, response=%#x
Airship [%{public}s:%d:%{public}s] interface_id=%u, timeout=%u ms
Airship [%{public}s:%d:%{public}s] unexpected error code (0x%08x)
Airship [%{public}s:%d:%{public}s] interface not open
Airship [%{public}s:%d:%{public}s] invoke stop handler
Airship [%{public}s:%d:%{public}s] unexpected error code 0x%08x
Airship [%{public}s:%d:%{public}s] unable to map buffer
Airship [%{public}s:%d:%{public}s] invoke stop_handler
```
