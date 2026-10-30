# `/System/DriverKit/System/Library/PrivateFrameworks/AirshipCentauriHelperServices.framework/AirshipCentauriHelperServices`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 317,808 bytes.

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
interposerResumed
dispatch_open
exec_awaitReady
cancelOpen
[%s:%d:%s] reading register %s
BUG in Airship: invalid tail index advance operation @%s:%u
BUG in Airship: attempted to create boxed string from null C string @%s:%u
airship.centauri-timesync.event
ALLOCATION FAILURE (or BUG) in Airship @%s:%u
dispatch_close
boot_nonce_doorbell
BUG in Airship: ring size cannot be zero
[%s:%d:%s] ready for timesync
Default
stateMachine
[%s:%d:%s] creating airship buffer
emplace
BUG in Airship: invalid tail index update operation @%s:%u
command
airship.centauri-interface.tx-ready
injectInterposerData
common.cpp
dispatch_cancelOpen
[%s:%d:%s] SetPowerState %u -> %u
[%s:%d:%s] sending image
[%s:%d:%s] active=%u, pendingSendImage=%u
BUG in Airship: attempted to initialize optional with sentinel value
stewie-control-tx
boxed_types.cpp
v24@?0^v8^{debug_info_capture=*II}16
stewie-data-tx
[%s:%d:%s] user client must be open
SetPowerState_Impl
[%s:%d:%s] user client is already open
coexlogger-rx
aonsensed-tx
with_cstr_nocopy
airship-debug
get_id
Start_Impl_block_invoke
setBufferInfo
dispatch_readRegister
hci-rx
[%s:%d:%s] invalid requested tx size %llu
boot_nonce
exec_createControllers
sendTxTransfers
start
get_context
[%s:%d:%s] mapping region
BUG in Airship: attempted truncate to larger size
[%s:%d:%s] resource in use
lea-rx
BUG in client of Airship: attempted access to closed interposer @%s:%u
IOUserClientQueueExternalMethod
open
[%s:%d:%s] image sent monitor handler
sco-tx
setInterposer
validate_buffer_bounds
[%s:%d:%s] closing interface user client
[%s:%d:%s] setting up interface client buffer
[%s:%d:%s] creating data buffer descriptor
[%s:%d:%s] starting boot user client
[%s:%d:%s] creating memory descriptor
AirshipCentauriHelperMemregionUserClient.cpp
[%s:%d:%s] stopping memregion user client
AirshipCentauriHelperBootUserClient.cpp
optional.hpp
operator()
lla
emplace_back
append_zeroes
BUG in Airship: bad array access @%s:%u
[%s:%d:%s] invalid offset %llu
airship.centauri-memregion.opened
not support external buffer
[%s:%d:%s] %s: suspend rx: tag %u length %u
[%s:%d:%s] successfully started boot user client
[%s:%d:%s] open complete (0x%08x)
CentauriHelperMemregion
debug-rx
lmp
set_capacity
rom
exec_createController
startTx
processTxCompletions
log
BUG in Airship: attempted to initialize optional with sentinel value @%s:%u
[%s:%d:%s] not in target exec stage
sendImage
[%s:%d:%s] send image complete (0x%08x)
CentauriHelperInterface
startRx
[%s:%d:%s] mapping meta buffer
???
writeRegister
[%s:%d:%s] stage arg not recognized
[%s:%d:%s] closing boot user client
[%s:%d:%s] could not find name for register selector %llu
[%s:%d:%s] creating airship memregion
binlogger-rx
cmd-request
dispatch_startRx
interposerResumed_block_invoke
[%s:%d:%s] %s: inject rx length:%u
operator[]
[%s:%d:%s] stop handler already set
exec_mapRegion
dispatch_flushTx
[%s:%d:%s] %s: suspend tx: clientIndex %u transferSize %u
BUG in Airship:  @%s:%u
[%s:%d:%s] informing userspace of stoppage (boot handle became unusable)
[%s:%d:%s] airship read register returned status 0x%x
[%s:%d:%s] airship write register returned status 0x%x
BUG in Airship: bad optional access
coexlogger
erase
start_block_invoke
domain_mode
reduce_size
BUG in Airship: invalid head index advance operation
[%s:%d:%s] close successful
[%s:%d:%s] register read successful
[%s:%d:%s] opening memregion user client
acl-tx
airship.centauri-interface.stopped
[%s:%d:%s] successfully started interface user client
[%s:%d:%s] interface user client muse be open
close
loopback-rx
advance_buffer_pointer
BUG in Airship: bad array access
get_limits
ALLOCATION FAILURE (or BUG) in Airship
cancel
exec_acquireResource
value
refillRx
interposerSuspended
exec_sendImage
[%s:%d:%s] resource acquired
[%s:%d:%s] closing memregion user client
IORegistryEntryID
[%s:%d:%s] invalid requested rx size %llu
loopback
[%s:%d:%s] successfully started timesync user client
resume
lpm-boot
dispatch_writeRegister
region-debug
aonsensed
acl
le-rx
consumeRxTransfers
[%s:%d:%s] mapping data buffer
BUG in Airship: attempted to create boxed string from null C string
[%s:%d:%s] starting timesync user client
[%s:%d:%s] starting memregion user client
dbg-rx
lea-tx
dispatch_setBufferInfo
dispatch_startTx
[%s:%d:%s] closing timesync user client
ExternalMethod
dispatch_setStopHandler
cmd-response
[%s:%d:%s] stage arg %llu
[%s:%d:%s] unexpected error code (0x%08x)
[%s:%d:%s] user client is not open
[%s:%d:%s] send image already in progress
createStateMonitorIfNotPresent_block_invoke
dbg
consumeResult
[%s:%d:%s] invalid length %llu
mutex
aonsensed-rx
acl-rx
invalid channel @%s:%u
[%s:%d:%s] informing userspace of stoppage (ring state became non-open)
AirshipCentauriHelperTimesyncUserClient.cpp
[%s:%d:%s] stopping timesync user client
inject_data
sco
BUG in client of Airship: attempted access to closed interposer
dispatch_sendImage
cancelSendImage
chip_info
[%s:%d:%s] image response %u (0x%08x)
unavailable
cchi-tx
hci-tx
[%s:%d:%s] unknown interface
[%s:%d:%s] %s: drop tx: clientIndex %u transferSize %u
[%s:%d:%s] %s: resume tx
BUG in Airship: attempted truncate to larger size @%s:%u
BUG in Airship: 
stewie-data-rx
[%s:%d:%s] stopping boot user client
[%s:%d:%s] open already in progress
[%s:%d:%s] ready to boot
[%s:%d:%s] writing register
le-tx
lea
BUG in Airship: invalid tail index advance operation
get_free_space
[%s:%d:%s] unexpected error code 0x%08x
events
getInterposerFreeSpace
ensure_free_space
CentauriHelperBoot
airship.centauri-boot.image-sent
[%s:%d:%s] boot user client muse be open
binlogger
le
tsi-rx
(nil)
signal
[%s:%d:%s] resource acquisition not permitted
exec_openInterposer
refillRxTransfers
[%s:%d:%s] invalid requested rx count %llu
with_capacity
exec_acquireResource_block_invoke
AirshipCentauriHelperInterfaceUserClient.cpp
cchi
loopback-tx
[%s:%d:%s] %s: drop rx: tag %u length %u
v40@?0r^v8r^v16I24r^v28I36
Start_Impl
airship.centauri-interface.opened
advance_head_index
interposer.cpp
get_driver
boot_nonce_hash
boot_mode
[%s:%d:%s] boot state not ready
update_tail_index
[%s:%d:%s] user client cannot be open
init
host_platform_id
[%s:%d:%s] user client is not active
[%s:%d:%s] successfully started memregion user client
[%s:%d:%s] region not ready
v32@?0Q8^{IOService=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})}16Q24
ring_index_pair.hpp
BUG in Airship: invalid head index advance operation @%s:%u
advance_tail_index
[%s:%d:%s] source id arg not recognized
boot
airship.centauri-interface.rx-data
[%s:%d:%s] %s: inject tx tag:%u length:%u
[%s:%d:%s] opening timesync user client
readRegister
exec_awaitResponse
[%s:%d:%s] invalid requested tx count %llu
timesync
[%s:%d:%s] informing userspace of stoppage (exec stage became non-os)
mutex.hpp
ring_index_pair
Stop_Impl
airship.centauri-boot.stopped
exec_awaitMapRegionResult
airship.centauri-memregion.stopped
stewie-control
invalid channel
BUG in Airship: invalid tail index update operation
ecid
[%s:%d:%s] region arg %llu
dispatch_refillRx
BUG in Airship: ring size cannot be zero @%s:%u
set_context
setStopHandler
[%s:%d:%s] creating airship direct client
[%s:%d:%s] informing userspace of stoppage (region state became non-mapped)
stewie-data
airship.centauri-timesync.stopped
[%s:%d:%s] source id arg %llu
logging.cpp
default
execute
[%s:%d:%s] ret: 0x%08x
binlogger-tx
lla-tx
tsi-tx
processRxCompletions
acquire
snoop_data
tsi
stewie-control-rx
[%s:%d:%s] creating external buffer
truncate
dispatch_start
debug
exec_createControllers_block_invoke
[%s:%d:%s] %s: removed injected tag %u (%lu remaining tags)
airship.centauri-boot.opened
[%s:%d:%s] boot user client must be open
OSAction_AirshipCentauriHelperInterfaceUserClient_ServiceNotificationReady
sco-rx
not support external buffer @%s:%u
[%s:%d:%s] starting interface user client
[%s:%d:%s] creating meta buffer descriptor
suspend
exec_done
secondary_ftab_header_name
v8@?0
[%s:%d:%s] received time event
setStopHandler_block_invoke
dispatch_cancelSendImage
host_platform_sub_variant_id
debug_infra.hpp
[%s:%d:%s] interface index %llu
buffer
AirshipCentauriHelperInterposer.cpp
airship.centauri-timesync.opened
set_limits
management
get_direction
exec_awaitResponse_block_invoke
cchi-rx
[%s:%d:%s] stopping interface user client
CentauriHelperTimesync
dynamic_array.hpp
[%s:%d:%s] length %u is too large
fw_debug
hci
exec_awaitReady_block_invoke
BUG in Airship: bad optional access @%s:%u
createStateMonitorIfNotPresent
lmp-rx
[%s:%d:%s] %s: suspend rx
[%s:%d:%s] %s: suspend tx
[%s:%d:%s] %s: resume rx
[%s:%d:%s] region arg not recognized
interposerMatched
flushTx
Airship [%{public}s:%d:%{public}s] unknown interface
Airship [%{public}s:%d:%{public}s] %s: inject tx tag:%u length:%u
Airship [%{public}s:%d:%{public}s] open complete (0x%08x)
Airship [%{public}s:%d:%{public}s] unexpected error code (0x%08x)
Airship [%{public}s:%d:%{public}s] user client is not open
Airship [%{public}s:%d:%{public}s] creating meta buffer descriptor
Airship [%{public}s:%d:%{public}s] %{public}s
Airship [%{public}s:%d:%{public}s] stopping timesync user client
Airship [%{public}s:%d:%{public}s] stage arg %llu
Airship [%{public}s:%d:%{public}s] writing register
Airship [%{public}s:%d:%{public}s] %s: drop tx: clientIndex %u transferSize %u
Airship [%{public}s:%u:%{public}s] unexpected nonzero error code 0x%llx
Airship [%{public}s:%d:%{public}s] successfully started timesync user client
Airship [%{public}s:%d:%{public}s] stage arg not recognized
Airship [%{public}s:%d:%{public}s] ready to boot
Airship [%{public}s:%d:%{public}s] length %u is too large
Airship [%{public}s:%d:%{public}s] register read successful
Airship [%{public}s:%d:%{public}s] sending image
Airship [%{public}s:%d:%{public}s] unexpected error code 0x%08x
Airship [%{public}s:%d:%{public}s] closing memregion user client
Airship [%{public}s:%d:%{public}s] mapping meta buffer
Airship [%{public}s:%d:%{public}s] ready for timesync
Airship [%{public}s:%d:%{public}s] received time event
Airship [%{public}s:%d:%{public}s] send image already in progress
Airship [%{public}s:%d:%{public}s] send image complete (0x%08x)
Airship [%{public}s:%d:%{public}s] creating airship direct client
Airship [%{public}s:%d:%{public}s] region not ready
Airship [%{public}s:%d:%{public}s] mapping data buffer
Airship [%{public}s:%d:%{public}s] airship read register returned status 0x%x
Airship [%{public}s:%d:%{public}s] creating data buffer descriptor
Airship [%{public}s:%d:%{public}s] %s: resume tx
Airship [%{public}s:%d:%{public}s] unexpected GUARD_ELSE failure
Airship [%{public}s:%d:%{public}s] starting timesync user client
Airship [%{public}s:%d:%{public}s] reading register %s
Airship [%{public}s:%d:%{public}s] image sent monitor handler
Airship [%{public}s:%d:%{public}s] active=%u, pendingSendImage=%u
Airship [%{public}s:%d:%{public}s] interface index %llu
Airship [%{public}s:%d:%{public}s] not in target exec stage
Airship [%{public}s:%d:%{public}s] ret: 0x%08x
Airship [%{public}s:%d:%{public}s] invalid offset %llu
Airship [%{public}s:%d:%{public}s] creating external buffer
Airship [%{public}s:%d:%{public}s] user client must be open
Airship [%{public}s:%d:%{public}s] stopping interface user client
Airship [%{public}s:%d:%{public}s] closing interface user client
Airship [%{public}s:%d:%{public}s] opening timesync user client
Airship [%{public}s:%d:%{public}s] starting memregion user client
Airship [%{public}s:%d:%{public}s] user client cannot be open
Airship [%{public}s:%d:%{public}s] informing userspace of stoppage (region state became non-mapped)
Airship [%{public}s:%d:%{public}s] invalid requested rx size %llu
Airship [%{public}s:%d:%{public}s] %s: removed injected tag %u (%lu remaining tags)
Airship [%{public}s:%d:%{public}s] starting boot user client
Airship [%{public}s:%d:%{public}s] stopping boot user client
Airship [%{public}s:%d:%{public}s] boot user client muse be open
Airship [%{public}s:%d:%{public}s] resource in use
Airship [%{public}s:%d:%{public}s] mapping region
Airship [%{public}s:%d:%{public}s] invalid requested tx count %llu
Airship [%{public}s:%d:%{public}s] interface user client muse be open
Airship [%{public}s:%d:%{public}s] closing boot user client
Airship [%{public}s:%d:%{public}s] %s: drop rx: tag %u length %u
Airship [%{public}s:%d:%{public}s] user client is already open
Airship [%{public}s:%d:%{public}s] informing userspace of stoppage (boot handle became unusable)
Airship [%{public}s:%d:%{public}s] boot user client must be open
Airship [%{public}s:%d:%{public}s] airship write register returned status 0x%x
Airship [%{public}s:%d:%{public}s] successfully started memregion user client
Airship [%{public}s:%d:%{public}s] region arg %llu
Airship [%{public}s:%d:%{public}s] opening memregion user client
Airship [%{public}s:%d:%{public}s] stop handler already set
Airship [%{public}s:%d:%{public}s] invalid requested tx size %llu
Airship [%{public}s:%d:%{public}s] %s: suspend tx: clientIndex %u transferSize %u
Airship [%{public}s:%d:%{public}s] %s: inject rx length:%u
Airship [%{public}s:%d:%{public}s] source id arg %llu
Airship [%{public}s:%d:%{public}s] stopping memregion user client
Airship [%{public}s:%d:%{public}s] SetPowerState %u -> %u
Airship [%{public}s:%d:%{public}s] user client is not active
Airship [%{public}s:%d:%{public}s] resource acquired
Airship [%{public}s:%d:%{public}s] setting up interface client buffer
Airship [%{public}s:%d:%{public}s] source id arg not recognized
Airship [%{public}s:%d:%{public}s] closing timesync user client
Airship [%{public}s:%d:%{public}s] successfully started boot user client
Airship [%{public}s:%d:%{public}s] creating airship buffer
Airship [%{public}s:%d:%{public}s] %s: suspend rx
Airship [%{public}s:%d:%{public}s] informing userspace of stoppage (exec stage became non-os)
Airship [%{public}s:%d:%{public}s] boot state not ready
Airship [%{public}s:%d:%{public}s] could not find name for register selector %llu
Airship [%{public}s:%d:%{public}s] image response %u (0x%08x)
Airship [%{public}s:%d:%{public}s] creating memory descriptor
Airship [%{public}s:%d:%{public}s] open already in progress
Airship [%{public}s:%d:%{public}s] resource acquisition not permitted
Airship [%{public}s:%d:%{public}s] creating airship memregion
Airship [%{public}s:%d:%{public}s] starting interface user client
Airship [%{public}s:%d:%{public}s] invalid requested rx count %llu
Airship [%{public}s:%d:%{public}s] informing userspace of stoppage (ring state became non-open)
Airship [%{public}s:%d:%{public}s] %s: resume rx
Airship [%{public}s:%d:%{public}s] %s: suspend rx: tag %u length %u
Airship [%{public}s:%d:%{public}s] %s: suspend tx
Airship [%{public}s:%d:%{public}s] close successful
Airship [%{public}s:%d:%{public}s] region arg not recognized
Airship [%{public}s:%d:%{public}s] invalid length %llu
Airship [%{public}s:%d:%{public}s] successfully started interface user client
```
