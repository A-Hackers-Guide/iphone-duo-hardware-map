# `/System/Library/Extensions/AppleSPURose.kext/PlugIns/RoseControllerLib.plugin/RoseControllerLib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 120,032 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = BUNDLE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 18 (Size: 2032)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak
```

## Linked libraries (4)

- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (113)

```
service
RoseFirmwareState
com.apple.RoseController.commandQueue
RoseServiceState
time_dictionary
buffer
rose hw state is %d
received a %s crashlog
_asyncEventsourceCancelGroup
unsupported command 0x%02x
triggering %s rose crashlog with delay %u
%s\n
%08x: 
default
_blob_rx_complete
out_size
size > __builtin_offsetof(RTKOS_sik_info_event, cont) + sizeof(RTKOS_sik_info_event::cont)
fatal
calling getchiprev
interface < ROSE_INTERFACE_MAX
core/logtype(%d/%d) size:%llu corrupted:%d id:%llu
unhandled endpoint %d on RTKOS comms interface
unable to query rose f/w state
non-fatal
timed out waiting for boot_done event
_buf == __null
ok
/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/Rose/RoseControllerLib/RoseController.cpp
rose firmware reset asynchronously
_queuePort
crashlog is too small
received packet error report size %d
delay_ms == 0
crashlog trigger failed with status %d
header->cmd == RTKOS_boot_nonce
Boot Nonce response with status %d
append status %u st %u sz %u wr %u
SIK data collection for session id %u %u sz %u
unable to query rose boot_done value
rose _rtkRead set to %d
sending boot nonce command to firmware
time_base
rose_time
error_code %d
_reportQueue
_asyncEventSource
nextEntry
in_size >= size
size > sizeof(RTKitCommsPacketHeader)
IOService
_servicePort
v8@?0
/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/Rose/RoseControllerLib/RoseSIKDataSession.cpp
SIK generation for session id %d failed with status %d
result == 0 
_buffer
queueMemory
Nonce generation failed with status %d
SIK response with session id %d status %d
size >= __builtin_offsetof(RTKOS_sik_info_event, start) + sizeof(RTKOS_sik_info_event::start)
rose f/w state set to %d
RoseRTKReady
com.apple.RoseController.notificationQueue
intProperty
RosePowerState
%s: AssertMacros: %s, %s file: %s, line: %d value:%x\n
session
sikEvent->start.sessionID == session->GetID()
_clientQueue
out_len
com.apple.RoseController.reportQueue
crashlog(%llu) dequeued: corrupt:%d, size in hdr/real size (%llu/%llu)
triggering rose NMI crash
_notificationQueue
in_size >= _response_size
event.header.interface < ROSE_INTERFACE_MAX
%02x 
unique_lock::unlock: not locked
crashlog trigger with status %d
SIK data collection started from session id %u %u sz %u
info
continuous_time
desc
error packet too large (size %d)
eid:%d, mt:%d, mp:%d, mpt:%d, size %d
crash_type < RoseTriggerCrashCount
append data of size %u to SIK blob
!_blob_rx_complete
Rose SIK Blob collection session(%d) timed out (size(%d)/rx(%d))
_commandQueue
unhandled packetType: %d
%s
com.apple.RoseControllerLib
deleting SIK blob session
SecureROMStatus
core < RoseCoreCount
SIK Blob: out size %u
SetPowerState called with on = %d
SetDeepSleepState called with on = %d
/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/common/Controller/RTKitCommHelpers.cpp
header->eid == RTKOS_endpoint_security
Rose SIK Blob session already in progress
IOGeneralInterest
out_size == sizeof(response)
_buf
header->mt == RTKOS_comms_type_response
Boot Nonce is %lu
status != -1
wait for SIK data rx completion
triggering %s rose crashlog
_stream
in_size >= _buf_size
%s
```
