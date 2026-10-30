# `/System/DriverKit/System/Library/PrivateFrameworks/AirshipCentauriHelperServices.framework/AirshipCentauriHelperServices`

From the upgrade restore ramdisk (141-29011-104.dmg). 317,808 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 2104)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (4)

- `/System/DriverKit/System/Library/PrivateFrameworks/AirshipCentauriHelperServices.framework/AirshipCentauriHelperServices (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/System/Library/PrivateFrameworks/AirshipDK.framework/AirshipDK (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/usr/lib/libc++.dylib (compatibility version 1.0.0, current version 2200.32.0)`

## Entitlements

```xml
  - no entitlements
```

## Strings (437)

```
BUG in client of Airship: attempted access to closed interposer
cancel
[%s:%d:%s] airship read register returned status 0x%x
AirshipCentauriHelperInterfaceUserClient.cpp
aonsensed-tx
BUG in Airship: attempted truncate to larger size
[%s:%d:%s] successfully started memregion user client
airship.centauri-interface.tx-ready
[%s:%d:%s] length %u is too large
acl-rx
exec_createControllers_block_invoke
[%s:%d:%s] stopping interface user client
BUG in Airship: invalid tail index advance operation
with_capacity
set_limits
lea-rx
tsi
[%s:%d:%s] creating meta buffer descriptor
exec_awaitResponse
[%s:%d:%s] close successful
loopback-tx
buffer
BUG in Airship: 
dispatch_flushTx
[%s:%d:%s] opening timesync user client
dispatch_close
domain_mode
[%s:%d:%s] writing register
v8@?0
BUG in Airship: invalid tail index update operation
timesync
signal
default
Default
lmp
[%s:%d:%s] user client cannot be open
BUG in Airship: bad array access @%s:%u
dispatch_sendImage
[%s:%d:%s] creating airship direct client
[%s:%d:%s] register read successful
airship.centauri-interface.rx-data
[%s:%d:%s] starting interface user client
common.cpp
BUG in Airship: attempted to create boxed string from null C string @%s:%u
[%s:%d:%s] unexpected error code 0x%08x
emplace
with_cstr_nocopy
CentauriHelperBoot
exec_sendImage
[%s:%d:%s] starting boot user client
createStateMonitorIfNotPresent_block_invoke
[%s:%d:%s] creating airship buffer
binlogger-rx
dispatch_setBufferInfo
refillRx
[%s:%d:%s] invalid requested rx count %llu
BUG in Airship: invalid tail index update operation @%s:%u
start
[%s:%d:%s] starting memregion user client
airship.centauri-interface.stopped
processTxCompletions
host_platform_sub_variant_id
[%s:%d:%s] informing userspace of stoppage (boot handle became unusable)
dispatch_startTx
tsi-tx
[%s:%d:%s] %s: suspend tx: clientIndex %u transferSize %u
ensure_free_space
acquire
AirshipCentauriHelperTimesyncUserClient.cpp
[%s:%d:%s] invalid length %llu
value
lea
invalid channel @%s:%u
rom
[%s:%d:%s] user client is not active
ring_index_pair.hpp
[%s:%d:%s] user client must be open
ALLOCATION FAILURE (or BUG) in Airship @%s:%u
dispatch_open
boot_nonce_doorbell
[%s:%d:%s] SetPowerState %u -> %u
BUG in Airship: bad optional access @%s:%u
createStateMonitorIfNotPresent
binlogger
[%s:%d:%s] informing userspace of stoppage (ring state became non-open)
erase
BUG in Airship: attempted to create boxed string from null C string
[%s:%d:%s] not in target exec stage
SetPowerState_Impl
close
advance_tail_index
dispatch_readRegister
readRegister
sendImage
dispatch_cancelSendImage
processRxCompletions
interposerResumed
not support external buffer
airship.centauri-timesync.stopped
get_id
stateMachine
exec_createController
[%s:%d:%s] stage arg not recognized
[%s:%d:%s] region arg %llu
[%s:%d:%s] region not ready
events
lla-tx
stewie-control-rx
exec_createControllers
suspend
BUG in Airship:  @%s:%u
execute
exec_awaitReady
[%s:%d:%s] successfully started boot user client
[%s:%d:%s] boot user client muse be open
[%s:%d:%s] source id arg %llu
[%s:%d:%s] resource acquisition not permitted
[%s:%d:%s] closing boot user client
[%s:%d:%s] boot user client must be open
le
setBufferInfo
dispatch_refillRx
debug_infra.hpp
BUG in Airship: bad array access
[%s:%d:%s] ready to boot
consumeRxTransfers
sendTxTransfers
airship.centauri-interface.opened
truncate
[%s:%d:%s] creating memory descriptor
[%s:%d:%s] successfully started interface user client
[%s:%d:%s] %s: resume rx
dynamic_array.hpp
operator[]
get_limits
[%s:%d:%s] image sent monitor handler
boot
dispatch_writeRegister
exec_awaitResponse_block_invoke
boot_mode
[%s:%d:%s] send image complete (0x%08x)
aonsensed-rx
management
[%s:%d:%s] invalid requested tx count %llu
update_tail_index
exec_done
[%s:%d:%s] reading register %s
getInterposerFreeSpace
[%s:%d:%s] %s: drop tx: clientIndex %u transferSize %u
start_block_invoke
ExternalMethod
cancelSendImage
get_context
CentauriHelperMemregion
region-debug
loopback
aonsensed
reduce_size
secondary_ftab_header_name
BUG in Airship: bad optional access
BUG in Airship: attempted to initialize optional with sentinel value @%s:%u
fw_debug
[%s:%d:%s] interface index %llu
[%s:%d:%s] %s: resume tx
exec_awaitReady_block_invoke
[%s:%d:%s] send image already in progress
coexlogger
sco-rx
sco-tx
le-tx
lmp-rx
[%s:%d:%s] invalid requested rx size %llu
set_capacity
operator()
not support external buffer @%s:%u
[%s:%d:%s] creating data buffer descriptor
startTx
refillRxTransfers
exec_acquireResource
exec_acquireResource_block_invoke
ecid
[%s:%d:%s] region arg not recognized
tsi-rx
[%s:%d:%s] %s: inject tx tag:%u length:%u
emplace_back
get_free_space
cmd-response
[%s:%d:%s] interface user client muse be open
[%s:%d:%s] %s: suspend tx
(nil)
hci-rx
resume
IOUserClientQueueExternalMethod
[%s:%d:%s] unexpected error code (0x%08x)
[%s:%d:%s] resource in use
[%s:%d:%s] user client is not open
mutex.hpp
BUG in Airship: attempted to initialize optional with sentinel value
acl-tx
v40@?0r^v8r^v16I24r^v28I36
init
[%s:%d:%s] user client is already open
[%s:%d:%s] boot state not ready
CentauriHelperInterface
v32@?0Q8^{IOService=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})}16Q24
lea-tx
cmd-request
sco
[%s:%d:%s] %s: removed injected tag %u (%lu remaining tags)
[%s:%d:%s] received time event
airship.centauri-boot.stopped
boot_nonce_hash
[%s:%d:%s] invalid offset %llu
AirshipCentauriHelperMemregionUserClient.cpp
invalid channel
interposerResumed_block_invoke
BUG in Airship: invalid head index advance operation @%s:%u
AirshipCentauriHelperInterposer.cpp
Start_Impl_block_invoke
cchi-rx
startRx
set_context
setStopHandler_block_invoke
[%s:%d:%s] sending image
exec_mapRegion
injectInterposerData
boxed_types.cpp
[%s:%d:%s] successfully started timesync user client
[%s:%d:%s] closing timesync user client
consumeResult
dispatch_cancelOpen
[%s:%d:%s] resource acquired
acl
advance_head_index
airship.centauri-timesync.opened
[%s:%d:%s] informing userspace of stoppage (exec stage became non-os)
get_driver
[%s:%d:%s] airship write register returned status 0x%x
validate_buffer_bounds
BUG in Airship: invalid head index advance operation
airship.centauri-boot.opened
stewie-data
flushTx
debug
hci-tx
BUG in Airship: invalid tail index advance operation @%s:%u
snoop_data
dispatch_setStopHandler
[%s:%d:%s] could not find name for register selector %llu
[%s:%d:%s] opening memregion user client
v24@?0^v8^{debug_info_capture=*II}16
lla
dispatch_startRx
[%s:%d:%s] mapping data buffer
AirshipCentauriHelperBootUserClient.cpp
Start_Impl
[%s:%d:%s] %s: suspend rx: tag %u length %u
append_zeroes
[%s:%d:%s] stopping timesync user client
logging.cpp
boot_nonce
mutex
loopback-rx
stewie-data-tx
setInterposer
interposer.cpp
open
unavailable
hci
[%s:%d:%s] setting up interface client buffer
chip_info
airship.centauri-memregion.stopped
interposerMatched
stewie-control
[%s:%d:%s] open already in progress
dbg
command
[%s:%d:%s] %s: suspend rx
BUG in Airship: attempted truncate to larger size @%s:%u
lpm-boot
writeRegister
[%s:%d:%s] ret: 0x%08x
[%s:%d:%s] creating airship memregion
[%s:%d:%s] mapping region
[%s:%d:%s] closing memregion user client
ring_index_pair
airship-debug
inject_data
airship.centauri-boot.image-sent
cancelOpen
get_direction
airship.centauri-memregion.opened
IORegistryEntryID
ALLOCATION FAILURE (or BUG) in Airship
[%s:%d:%s] open complete (0x%08x)
exec_awaitMapRegionResult
[%s:%d:%s] informing userspace of stoppage (region state became non-mapped)
cchi
debug-rx
[%s:%d:%s] %s: drop rx: tag %u length %u
BUG in Airship: ring size cannot be zero
airship.centauri-timesync.event
host_platform_id
[%s:%d:%s] stopping memregion user client
interposerSuspended
[%s:%d:%s] invalid requested tx size %llu
[%s:%d:%s] mapping meta buffer
setStopHandler
[%s:%d:%s] stopping boot user client
[%s:%d:%s] image response %u (0x%08x)
[%s:%d:%s] active=%u, pendingSendImage=%u
stewie-control-tx
exec_openInterposer
[%s:%d:%s] closing interface user client
[%s:%d:%s] creating external buffer
BUG in Airship: ring size cannot be zero @%s:%u
[%s:%d:%s] ready for timesync
[%s:%d:%s] stop handler already set
optional.hpp
coexlogger-rx
[%s:%d:%s] %s: inject rx length:%u
dispatch_start
Stop_Impl
cchi-tx
???
[%s:%d:%s] starting timesync user client
CentauriHelperTimesync
OSAction_AirshipCentauriHelperInterfaceUserClient_ServiceNotificationReady
le-rx
BUG in client of Airship: attempted access to closed interposer @%s:%u
binlogger-tx
dbg-rx
stewie-data-rx
[%s:%d:%s] source id arg not recognized
[%s:%d:%s] stage arg %llu
advance_buffer_pointer
[%s:%d:%s] unknown interface
log
Airship [%{public}s:%d:%{public}s] invalid offset %llu
Airship [%{public}s:%d:%{public}s] invalid requested rx count %llu
Airship [%{public}s:%d:%{public}s] invalid requested tx count %llu
Airship [%{public}s:%d:%{public}s] successfully started timesync user client
Airship [%{public}s:%d:%{public}s] active=%u, pendingSendImage=%u
Airship [%{public}s:%d:%{public}s] user client cannot be open
Airship [%{public}s:%d:%{public}s] resource acquisition not permitted
Airship [%{public}s:%d:%{public}s] resource acquired
Airship [%{public}s:%d:%{public}s] informing userspace of stoppage (ring state became non-open)
Airship [%{public}s:%d:%{public}s] %s: removed injected tag %u (%lu remaining tags)
Airship [%{public}s:%d:%{public}s] closing timesync user client
Airship [%{public}s:%d:%{public}s] stage arg %llu
Airship [%{public}s:%d:%{public}s] stage arg not recognized
Airship [%{public}s:%d:%{public}s] invalid length %llu
Airship [%{public}s:%d:%{public}s] creating memory descriptor
Airship [%{public}s:%d:%{public}s] creating airship buffer
Airship [%{public}s:%d:%{public}s] unexpected error code (0x%08x)
Airship [%{public}s:%d:%{public}s] %s: suspend rx
Airship [%{public}s:%d:%{public}s] unexpected GUARD_ELSE failure
Airship [%{public}s:%d:%{public}s] starting boot user client
Airship [%{public}s:%d:%{public}s] image response %u (0x%08x)
Airship [%{public}s:%d:%{public}s] stopping memregion user client
Airship [%{public}s:%d:%{public}s] closing interface user client
Airship [%{public}s:%d:%{public}s] could not find name for register selector %llu
Airship [%{public}s:%d:%{public}s] register read successful
Airship [%{public}s:%d:%{public}s] user client is not open
Airship [%{public}s:%d:%{public}s] starting interface user client
Airship [%{public}s:%d:%{public}s] %s: suspend rx: tag %u length %u
Airship [%{public}s:%d:%{public}s] source id arg not recognized
Airship [%{public}s:%d:%{public}s] user client is already open
Airship [%{public}s:%d:%{public}s] boot user client muse be open
Airship [%{public}s:%d:%{public}s] open already in progress
Airship [%{public}s:%d:%{public}s] creating airship memregion
Airship [%{public}s:%d:%{public}s] opening timesync user client
Airship [%{public}s:%d:%{public}s] stopping boot user client
Airship [%{public}s:%d:%{public}s] length %u is too large
Airship [%{public}s:%d:%{public}s] reading register %s
Airship [%{public}s:%d:%{public}s] opening memregion user client
Airship [%{public}s:%d:%{public}s] unexpected error code 0x%08x
Airship [%{public}s:%d:%{public}s] unknown interface
Airship [%{public}s:%d:%{public}s] setting up interface client buffer
Airship [%{public}s:%d:%{public}s] starting timesync user client
Airship [%{public}s:%d:%{public}s] successfully started boot user client
Airship [%{public}s:%d:%{public}s] boot user client must be open
Airship [%{public}s:%d:%{public}s] resource in use
Airship [%{public}s:%d:%{public}s] stopping interface user client
Airship [%{public}s:%d:%{public}s] %s: suspend tx: clientIndex %u transferSize %u
Airship [%{public}s:%d:%{public}s] %s: resume tx
Airship [%{public}s:%u:%{public}s] unexpected nonzero error code 0x%llx
Airship [%{public}s:%d:%{public}s] ready to boot
Airship [%{public}s:%d:%{public}s] closing memregion user client
Airship [%{public}s:%d:%{public}s] stop handler already set
Airship [%{public}s:%d:%{public}s] successfully started interface user client
Airship [%{public}s:%d:%{public}s] %s: resume rx
Airship [%{public}s:%d:%{public}s] ready for timesync
Airship [%{public}s:%d:%{public}s] send image complete (0x%08x)
Airship [%{public}s:%d:%{public}s] ret: 0x%08x
Airship [%{public}s:%d:%{public}s] region arg %llu
Airship [%{public}s:%d:%{public}s] informing userspace of stoppage (region state became non-mapped)
Airship [%{public}s:%d:%{public}s] closing boot user client
Airship [%{public}s:%d:%{public}s] informing userspace of stoppage (boot handle became unusable)
Airship [%{public}s:%d:%{public}s] sending image
Airship [%{public}s:%d:%{public}s] starting memregion user client
Airship [%{public}s:%d:%{public}s] creating airship direct client
Airship [%{public}s:%d:%{public}s] SetPowerState %u -> %u
Airship [%{public}s:%d:%{public}s] mapping region
Airship [%{public}s:%d:%{public}s] invalid requested rx size %llu
Airship [%{public}s:%d:%{public}s] %s: drop rx: tag %u length %u
Airship [%{public}s:%d:%{public}s] writing register
Airship [%{public}s:%d:%{public}s] region not ready
Airship [%{public}s:%d:%{public}s] user client must be open
Airship [%{public}s:%d:%{public}s] interface index %llu
Airship [%{public}s:%d:%{public}s] %s: inject tx tag:%u length:%u
Airship [%{public}s:%d:%{public}s] %{public}s
Airship [%{public}s:%d:%{public}s] stopping timesync user client
Airship [%{public}s:%d:%{public}s] not in target exec stage
Airship [%{public}s:%d:%{public}s] boot state not ready
Airship [%{public}s:%d:%{public}s] successfully started memregion user client
Airship [%{public}s:%d:%{public}s] user client is not active
Airship [%{public}s:%d:%{public}s] invalid requested tx size %llu
Airship [%{public}s:%d:%{public}s] creating external buffer
Airship [%{public}s:%d:%{public}s] %s: drop tx: clientIndex %u transferSize %u
Airship [%{public}s:%d:%{public}s] %s: suspend tx
Airship [%{public}s:%d:%{public}s] received time event
Airship [%{public}s:%d:%{public}s] airship read register returned status 0x%x
Airship [%{public}s:%d:%{public}s] interface user client muse be open
Airship [%{public}s:%d:%{public}s] %s: inject rx length:%u
Airship [%{public}s:%d:%{public}s] source id arg %llu
Airship [%{public}s:%d:%{public}s] region arg not recognized
Airship [%{public}s:%d:%{public}s] open complete (0x%08x)
Airship [%{public}s:%d:%{public}s] mapping meta buffer
Airship [%{public}s:%d:%{public}s] informing userspace of stoppage (exec stage became non-os)
Airship [%{public}s:%d:%{public}s] send image already in progress
Airship [%{public}s:%d:%{public}s] image sent monitor handler
Airship [%{public}s:%d:%{public}s] close successful
Airship [%{public}s:%d:%{public}s] creating data buffer descriptor
Airship [%{public}s:%d:%{public}s] creating meta buffer descriptor
Airship [%{public}s:%d:%{public}s] mapping data buffer
Airship [%{public}s:%d:%{public}s] airship write register returned status 0x%x
```
