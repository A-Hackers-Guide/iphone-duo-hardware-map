# `/System/Library/Extensions/AppleSPURose.kext/PlugIns/RoseControllerLib.plugin/RoseControllerLib`

From the upgrade restore ramdisk (141-29011-104.dmg). 120,032 bytes.

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
/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/common/Controller/RTKitCommHelpers.cpp
_blob_rx_complete
size >= __builtin_offsetof(RTKOS_sik_info_event, start) + sizeof(RTKOS_sik_info_event::start)
RoseFirmwareState
_commandQueue
in_size >= _response_size
desc
crashlog is too small
crashlog trigger with status %d
deleting SIK blob session
IOService
v8@?0
rose hw state is %d
rose_time
unhandled endpoint %d on RTKOS comms interface
crash_type < RoseTriggerCrashCount
in_size >= _buf_size
SIK response with session id %d status %d
_notificationQueue
continuous_time
core < RoseCoreCount
delay_ms == 0
%s
unique_lock::unlock: not locked
crashlog trigger failed with status %d
unable to query rose f/w state
Rose SIK Blob session already in progress
rose firmware reset asynchronously
core/logtype(%d/%d) size:%llu corrupted:%d id:%llu
unsupported command 0x%02x
ok
SIK data collection for session id %u %u sz %u
RoseRTKReady
SIK Blob: out size %u
interface < ROSE_INTERFACE_MAX
header->mt == RTKOS_comms_type_response
_buf
com.apple.RoseController.notificationQueue
fatal
intProperty
_clientQueue
out_len
queueMemory
SIK data collection started from session id %u %u sz %u
non-fatal
sending boot nonce command to firmware
SIK generation for session id %d failed with status %d
header->eid == RTKOS_endpoint_security
Boot Nonce response with status %d
append status %u st %u sz %u wr %u
wait for SIK data rx completion
Rose SIK Blob collection session(%d) timed out (size(%d)/rx(%d))
out_size
RoseServiceState
time_dictionary
calling getchiprev
_reportQueue
_asyncEventSource
in_size >= size
Nonce generation failed with status %d
Boot Nonce is %lu
status != -1
unhandled packetType: %d
size > sizeof(RTKitCommsPacketHeader)
%02x 
default
session
result == 0 
size > __builtin_offsetof(RTKOS_sik_info_event, cont) + sizeof(RTKOS_sik_info_event::cont)
SecureROMStatus
_asyncEventsourceCancelGroup
crashlog(%llu) dequeued: corrupt:%d, size in hdr/real size (%llu/%llu)
_stream
rose _rtkRead set to %d
IOGeneralInterest
triggering %s rose crashlog
out_size == sizeof(response)
info
RosePowerState
append data of size %u to SIK blob
unable to query rose boot_done value
_servicePort
buffer
error_code %d
error packet too large (size %d)
SetPowerState called with on = %d
SetDeepSleepState called with on = %d
header->cmd == RTKOS_boot_nonce
sikEvent->start.sessionID == session->GetID()
com.apple.RoseController.commandQueue
received a %s crashlog
_queuePort
com.apple.RoseController.reportQueue
nextEntry
triggering rose NMI crash
%s: AssertMacros: %s, %s file: %s, line: %d value:%x\n
!_blob_rx_complete
service
rose f/w state set to %d
event.header.interface < ROSE_INTERFACE_MAX
received packet error report size %d
eid:%d, mt:%d, mp:%d, mpt:%d, size %d
%08x: 
/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/Rose/RoseControllerLib/RoseSIKDataSession.cpp
time_base
timed out waiting for boot_done event
_buffer
triggering %s rose crashlog with delay %u
com.apple.RoseControllerLib
_buf == __null
/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/Rose/RoseControllerLib/RoseController.cpp
%s\n
%s
```
