# `/System/Library/PrivateFrameworks/CentauriController.framework/CentauriController`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 174,944 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2384)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (5)

- `/System/Library/PrivateFrameworks/CentauriController.framework/CentauriController (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (165)

```
%{public}s
CentauriController::%s: failed to set properties: 0x%08x\n
CentauriController::%s: detected a new driver, skipping reset\n
registerErrorHandler
getResetHint
CentauriController::%s: failed to get runloop source\n
HasReenumerated
ModuleVendor
secondSendImageEnd
CentauriController::%s: timeout waiting for reset completion or termination\n
CentauriController::%s: collect logs completion ret 0x%08x state %u\n
no thread context
CentauriController::%s: failed to map secondary memory 0x%08x\n
getCachedErrorCount
ChipPowerState
openSecondStageEnd
setHardwareHealth
CentauriController::%s: mismatching driver UIDs, ignoring reset. received: 0x%llx current: 0x%llx\n
CentauriController::%s: failed to set mem swap regions 0x%08x\n
FusingConfig
CentauriController::%s: property not found: %s\n
CentauriController::%s: failed to get service name: 0x%x\n
CentauriController::%s: only control can register a crashlog handler\n
CentauriController::%s: failed to add terminate notification: 0x%x\n
CentauriController::%s: invalid property\n
setChipPower
reset
CentauriController::%s: mismatching driver UIDs, ignoring collectLogs. received: 0x%llx current: 0x%llx\n
CentauriController::%s: timeout waiting for collectLogs completion or termination\n
CentauriController::%s: failed to get chip state 0x%08x\n
operator()
CentauriController::%s: invalid number of args: %u\n
v8@?0
registerWithService
FirmwareBootTimestamps
openROMEnd
openCCHIEnd
CentauriController::%s: ignoring redundant service publish\n
CentauriController::%s: failed to get reset hint 0x%08x\n
CentauriController::%s: no notifier\n
com.apple.centauricontroller
CentauriBeta
memswapHandOffStart
CentauriController::%s: failed to allocate secondary memory 0x%08x\n
CentauriController::%s: unserialize failed with error %s\n
start
CentauriController::%s: failed to allocate CFString\n
CentauriController::%s: service publish before terminate\n
CentauriController::%s: reset completion ret 0x%08x state %u\n
CentauriController::%s: CancelErrorHandler failed 0x%08x\n
CentauriController::%s: no args\n
replaceErrorBlock
deregisterErrorHandler
CentauriController::%s: wrong type on power property\n
bind
CentauriController::%s: result 0x%08x, source %u, code %u, arg %llu, uid 0x%llx\n
registerCrashlogHandler
CentauriController::%s: only control can map secondary memory\n
CentauriController::%s: failed to add publish notification: 0x%x\n
BootTimestamps
memswapHandOffEnd
CentauriController::%s: property: %s\n
CentauriController::%s: only beta can set reset hint\n
CentauriAlpha
ccpuPingEnd
CentauriController::%s: failed to re-initialize error handler 0x%08x\n
CentauriController::%s: chip state has invalid length %u\n
no block
setMemSwapRegions
CentauriController::%s: result 0x%08x\n
getManagerProperty
CentauriController::%s: already deregistered\n
CentauriController::%s: failed: 0x%08x
bindCrashlogNotifierToController
CentauriController::%s: set crashlog handler call failed 0x%08x\n
ccpuPingStart
CentauriController::%s: failed to create property name\n
CentauriController::%s: \n
CentauriController::%s: failed to copy block\n
getCrashlogs
setWakeOnROM
servicePublishNotification
CentauriController::%s: failed to open service: 0x%x\n
multiple thread contexts
unbind
CentauriController::%s: no controller\n
allocateSecondaryMemory
IOServicePublish
CentauriController::%s: failed to register with service: 0x%x\n
CentauriController::%s: no reason\n
CentauriController::%s: collectLogs call failed 0x%08x\n
cancel
CentauriController::%s: error creating notifier: %s\n
CentauriController::%s: already registered crashlog handler\n
CentauriController::%s: unserialize data is not an array\n
CentauriController::%s: failed to open 0x%08x\n
haveReenumeratedService
unique_lock::lock: references null mutex
openSecondStageStart
failed to copy block
CentauriController::%s: failed to register for interest notifications 0x%08x\n
unmapSecondaryMemory
CentauriController::%s: reset completion result 0x%08x terminated %u\n
CentauriController::%s: reset failed with 0x%08x, waiting for dext re-publish\n
unique_lock::lock: already locked
firstSendImageEnd
openCCHIStart
portOff
getCurrentDriverUID
unordered_map::at: key not found
PowerTableVersions
CentauriController::%s: no driver\n
CentauriController::%s: no mach port\n
CentauriController::%s: set error handler call failed 0x%08x\n
CentauriController::%s: only beta can get reset hint\n
CentauriController::%s: failed to create notification port\n
default
CentauriController::%s: cancelled\n
CentauriController::%s: no driver, saving error handler\n
CentauriController::%s: failed to get crashlogs 0x%08x\n
CentauriController::%s: Got %u crashlogs\n
setResetHint
thread constructor failed
CentauriController::%s: timed out waiting for driver\n
CentauriController::%s: unserialized data not found\n
IOServiceTerminate
FirmwareBootArgs
openROMStart
CentauriController::%s: failed to re-initialize crashlog handler 0x%08x\n
CentauriController::%s: uid 0x%llx\n
AppleCentauriManager
FirmwareBootDurations
firstSendImageStart
setManagerProperty
CentauriController::%s: unexpected match for reenumerated dext\n
serviceTerminateNotification
stop
CentauriController::%s: only applicable to control\n
unique_lock::unlock: not locked
CentauriController::%s: invalid chip state %llu\n
invoke
CentauriController::%s: failed to unmap secondary memory 0x%08x\n
CentauriController::%s: timed out waiting for driver match\n
CentauriController::%s: failed to open device\n
getChipPower
CentauriController::%s: failed to allocate CFDictionary\n
getChipState
mapSecondaryMemory
CentauriController::%s: invalid secondary memory mapping: address %p, size %llu\n
CentauriController::%s: only control can set mem swap regions\n
CentauriControl
CentauriController::%s: failed to set reset hint 0x%08x\n
CentauriController::%s: only control can unmap secondary memory\n
CentauriController::%s: provided driverUID before registering error handler\n
no controller
completionCopy
CentauriController::%s: no power property\n
CentauriController::%s: reset call failed 0x%08x\n
IOGeneralInterest
collectLogs
CentauriControllerClass.cpp
CentauriController::%s: only control can allocate secondary memory\n
CentauriController::%s: failed to get cached error count 0x%08x countLen %u\n
CentauriController::%s: collectLogs completion result 0x%08x terminated %u\n
secondSendImageStart
```
