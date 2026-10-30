# `/System/Library/PrivateFrameworks/CentauriController.framework/CentauriController`

From the upgrade restore ramdisk (141-29011-104.dmg). 174,944 bytes.

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
servicePublishNotification
CentauriController::%s: failed to create notification port\n
CentauriController::%s: timed out waiting for driver match\n
FirmwareBootDurations
openROMStart
CentauriController::%s: failed to set properties: 0x%08x\n
CentauriController::%s: failed to get reset hint 0x%08x\n
no thread context
CentauriController::%s: cancelled\n
cancel
BootTimestamps
openSecondStageStart
CentauriController::%s: failed to register with service: 0x%x\n
CentauriController::%s: mismatching driver UIDs, ignoring reset. received: 0x%llx current: 0x%llx\n
CentauriController::%s: collectLogs call failed 0x%08x\n
CentauriController::%s: no controller\n
CentauriController::%s: Got %u crashlogs\n
getCachedErrorCount
default
openCCHIEnd
setWakeOnROM
CentauriController::%s: failed to get service name: 0x%x\n
CentauriControllerClass.cpp
CentauriController::%s: failed to open 0x%08x\n
ChipPowerState
CentauriController::%s: timed out waiting for driver\n
CentauriController::%s: failed to map secondary memory 0x%08x\n
CentauriController::%s: invalid secondary memory mapping: address %p, size %llu\n
CentauriController::%s: failed to get runloop source\n
CentauriController::%s: failed to allocate CFString\n
CentauriController::%s: failed to allocate CFDictionary\n
getManagerProperty
CentauriController::%s: unexpected match for reenumerated dext\n
CentauriController::%s: error creating notifier: %s\n
CentauriController::%s: only control can map secondary memory\n
CentauriController::%s: reset failed with 0x%08x, waiting for dext re-publish\n
memswapHandOffStart
CentauriController::%s: no notifier\n
CentauriController::%s: service publish before terminate\n
CentauriController::%s: mismatching driver UIDs, ignoring collectLogs. received: 0x%llx current: 0x%llx\n
CentauriController::%s: set crashlog handler call failed 0x%08x\n
openCCHIStart
CentauriController::%s: failed to re-initialize error handler 0x%08x\n
CentauriController::%s: reset completion ret 0x%08x state %u\n
CentauriController::%s: unserialize failed with error %s\n
CentauriController::%s: failed to re-initialize crashlog handler 0x%08x\n
CentauriController::%s: chip state has invalid length %u\n
no block
CentauriController::%s: uid 0x%llx\n
CentauriController::%s: only control can allocate secondary memory\n
HasReenumerated
CentauriController::%s: ignoring redundant service publish\n
CentauriController::%s: collect logs completion ret 0x%08x state %u\n
registerCrashlogHandler
CentauriController::%s: invalid chip state %llu\n
CentauriController::%s: only control can register a crashlog handler\n
CentauriController::%s: failed to open device\n
CentauriController::%s: timeout waiting for reset completion or termination\n
multiple thread contexts
bind
v8@?0
FirmwareBootTimestamps
memswapHandOffEnd
CentauriController::%s: already deregistered\n
unmapSecondaryMemory
CentauriController::%s: failed to unmap secondary memory 0x%08x\n
setResetHint
PowerTableVersions
setChipPower
CentauriController::%s: timeout waiting for collectLogs completion or termination\n
start
CentauriController::%s: no driver\n
getChipState
CentauriController::%s: set error handler call failed 0x%08x\n
CentauriController::%s: failed to copy block\n
getCrashlogs
CentauriAlpha
FirmwareBootArgs
FusingConfig
CentauriController::%s: \n
CentauriController::%s: provided driverUID before registering error handler\n
CentauriController::%s: failed to register for interest notifications 0x%08x\n
CentauriController::%s: no args\n
CentauriController::%s: unserialized data not found\n
CentauriController::%s: only beta can get reset hint\n
AppleCentauriManager
no controller
CentauriController::%s: failed to allocate secondary memory 0x%08x\n
registerWithService
operator()
setHardwareHealth
CentauriController::%s: no reason\n
failed to copy block
bindCrashlogNotifierToController
setMemSwapRegions
IOServiceTerminate
CentauriControl
ccpuPingEnd
getCurrentDriverUID
CentauriController::%s: only control can unmap secondary memory\n
CentauriController::%s: failed to add publish notification: 0x%x\n
stop
unique_lock::lock: already locked
CentauriController::%s: collectLogs completion result 0x%08x terminated %u\n
openSecondStageEnd
CentauriController::%s: no power property\n
CentauriController::%s: property: %s\n
CentauriController::%s: already registered crashlog handler\n
CentauriController::%s: failed to get cached error count 0x%08x countLen %u\n
CentauriController::%s: only applicable to control\n
unordered_map::at: key not found
allocateSecondaryMemory
getResetHint
CentauriController::%s: reset completion result 0x%08x terminated %u\n
unique_lock::unlock: not locked
CentauriController::%s: failed to get chip state 0x%08x\n
getChipPower
CentauriController::%s: wrong type on power property\n
CentauriController::%s: failed to create property name\n
CentauriController::%s: failed to set mem swap regions 0x%08x\n
haveReenumeratedService
thread constructor failed
firstSendImageEnd
setManagerProperty
com.apple.centauricontroller
CentauriController::%s: result 0x%08x\n
openROMEnd
secondSendImageStart
CentauriController::%s: property not found: %s\n
CentauriController::%s: no mach port\n
mapSecondaryMemory
ModuleVendor
firstSendImageStart
CentauriController::%s: reset call failed 0x%08x\n
CentauriController::%s: only control can set mem swap regions\n
IOServicePublish
CentauriController::%s: failed to add terminate notification: 0x%x\n
unique_lock::lock: references null mutex
deregisterErrorHandler
reset
portOff
CentauriController::%s: detected a new driver, skipping reset\n
unbind
replaceErrorBlock
registerErrorHandler
CentauriController::%s: only beta can set reset hint\n
CentauriController::%s: invalid property\n
CentauriBeta
CentauriController::%s: failed to open service: 0x%x\n
collectLogs
IOGeneralInterest
CentauriController::%s: CancelErrorHandler failed 0x%08x\n
CentauriController::%s: result 0x%08x, source %u, code %u, arg %llu, uid 0x%llx\n
completionCopy
CentauriController::%s: no driver, saving error handler\n
CentauriController::%s: failed to get crashlogs 0x%08x\n
serviceTerminateNotification
CentauriController::%s: failed to set reset hint 0x%08x\n
invoke
CentauriController::%s: invalid number of args: %u\n
CentauriController::%s: unserialize data is not an array\n
secondSendImageEnd
ccpuPingStart
CentauriController::%s: failed: 0x%08x
```
