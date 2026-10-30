# `/usr/lib/libIOACIPC.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 134,992 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 2024)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (5)

- `/usr/lib/libIOACIPC.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (202)

```
IOACIPCTraceClass.cpp
openPipe
kACIPCTransferCompletionSuccessUnexpected
kACIPCInvalidRingId
fEventNotificationPort
kACIPCLinkStateUp
IOAppleConvergedIPCTraceBackendRaw
open_nl
kACIPCTransferCompletionUnregisteredChannel
kACIPCInvalidAsyncCDType
kACIPCDirectionOut
loggerTune
unmapMemory
kACIPCTransferCompletionCodeUndefined
kACIPCDeviceErrorStateTransition
kACIPCEventUnexpectedCompletionType
kACIPCCommandUnexpectedCompletion
kACIPCBadRequestError
IOACIPCTraceClass::%s: could not get matching service\n
readRegister
kACIPCAERError
setNotificationPort
deactivateTracePoint
kACIPCLinkDownTimeout
IOServiceFirstMatch
mapMemory
updateMemoryAsync
TracePipes
fNotificationPort
\n
~IOACIPCControlClass
invalid
IOACIPCClass.cpp
getTransferRingInfo
ioAsync
kACIPCTransferCompletionCodeUnknown
enableKernelTraceBuffers
v8@?0
v24@?0I8I12^v16
getCompletionRingInfo
kACIPCDeviceInvalidStateTransition
kACIPCDeviceWakeTimeout
abortTransferRingAsync
connect
IOACIPCTraceClass::%s: buff %p, size %u\n
IOACIPCTraceClass::%s: no async port\n
IOACIPCTraceClass::%s: no connection\n
activateTracePoint
!fEventQueue
currentLogSnapshotBufferSize
triggerCollectTriaging
mapMemoryAsync
updateMemory
kACIPCUnexpectedSleepMessageState
kACIPCEnterLowPowerTimeout
kACIPCLinkBWNotification
dumpRegistry
IOACIPCTraceClass::%s: TraceCode invalid\n
open
kACIPCCompletionUnaligned
kACIPCTransferCompletionUnexpectedChannel
kACIPCMessageRingFull
kACIPCTLPCompletionTimeout
~IOACIPCTraceClass
kACIPCPipeCloseFailed
kACIPCTagNotInUse
!queue
DEFAULT
deregisterEventNotification_nl
unmapMemoryAsync
!fEventRunLoopRef
AppleConvergedIPCTransferRingProperties
kACIPCDARTError
IOACIPCTraceClass::%s: could not create matching dictionary\n
activateAllTracePoints
kACIPCTransferUnexpectedEvent
kACIPCTransferMissingEvent
kACIPCHostConfigError
setUpNotificationCallback
sendImageAsync
kACIPCChannelResetFailed
kACIPCReadFail
kACIPCInvalidTag
kACIPCCROpenFailed
kACIPCAERFatalError
setEventNotificationPort
generateNonce
kACIPCDeviceSleepStateInvalid
kACIPCContextOpenFailed
kACIPCLinkStateHardDown
kACIPCLinkStateManualDown
vector
kACIPCTransferCompletionSizeUnexpected
kACIPCLinkDown
kACIPCInvalidSharedMemoryRegionId
kACIPCDirectionIn
IOACIPCTraceClass::%s: --done\n
demo
disableKernelTraceBuffers
start_nl
clearNotificationPort
kACIPCTransferCompletionCodeInvalid
kACIPCDeviceInAbortHandler
kACIPCChannelStopFailedFatal
deactivateAllTracePoints
clearEventNotificationPort
!fQueue
kACIPCChannelStartFailed
kACIPCPortEnableFailed
IOACIPCTraceClass::%s: \n
IOACIPCTraceClass::%s: could not open service\n
Code
bootstage
~IOACIPCClass
kACIPCPipeOpenFailed
kACIPCUnexpectedSleepMessageTarget
stop
Name
getTraceCode
basic_string
close
notifyMemoryAsync
kACIPCDeviceUnknownStateTransition
kACIPCTransferCompletionOverflowUnexpected
kACIPCTransferCompletionUnexpected
openService
enablePipe
kACIPCPipeAbortFailed
kACIPCSendImageFailed
kACIPCLinkStateSoftDown
kACIPCAERCorrectableError
flushTraceBuffers
AppleConvergedIPCCompletionRingProperties
close_nl
kACIPCChannelStopFailed
kACIPCEnterLowPowerFailed
IOACIPCTraceClass::%s: ret = %x\n
readLogsAsync
IOACIPCControlClass.cpp
sendImage
writeRegister
kACIPCSleepMessageCompletionFailed
kACIPCLinkUpTimeout
notifyMemory
v12@?0I8
kACIPCControlUnexpectedExecutionEnvironment
 
IOGeneralInterest
kACIPCDirectionInvalid
start
collectSnapshotAsync
kACIPCCommandRingFull
kACIPCLinkStateUnpoweredUp
!fRunLoopRef
abortTransferRing
kACIPCCompletionOutOfRange
SnapshotBufferSize
getRegistryInfo
registerEventNotification_nl
v20@?0I8^v12
IOServiceTerminate
io
kACIPCAERNonFatalError
closePipe
kACIPCTransferCompletionEndUnexpected
kACIPCTransferCompletionPartialUnexpected
kACIPCDeviceConfigError
kACIPCContextCloseFailed
IOACIPCClass::%s: trIndex %u, buff %p, size %u, footer %p, size %u\n
IOACIPCClass::%s: buff %p, size %u\n
IOACIPCClass::%s: --done\n
IOACIPCClass::%s: \n
IOACIPCControlClass::%s: block must be provided\n
IOACIPCControlClass::%s: could not add interest notification on service: %#x\n
IOACIPCControlClass::%s: +\n
IOACIPCClass::%s: reg %u, buff %p, size %u\n
IOACIPCControlClass::%s: \n
IOACIPCControlClass::%s: buff %p, size %u\n
IOACIPCControlClass::%s: a notification block is already registered. deregister it before registering a new block
IOACIPCClass::%s: already stopped, returning true\n
IOACIPCClass::%s: ret 0x%x, buff %p, size %u, cookie %u\n
IOACIPCClass::%s: TR index %u\n
IOACIPCControlClass::%s: --done\n
IOACIPCControlClass::%s: -\n
IOACIPCClass::%s: CR properties are not available\n
IOACIPCClass::%s: region %u, size %u\n
IOACIPCControlClass::%s: subsystem %u, index %u, arg1 %p, arg2 %p\n
IOACIPCClass::%s: TR properties has invalid type\n
IOACIPCClass::%s: not open, return success\n
IOACIPCClass::%s: IOServiceAddMatchingNotification (kIOFirstMatchNotification) failed, ret = 0x%08x
IOACIPCControlClass::%s: could not get matching service\n
IOACIPCControlClass::%s: no async port\n
IOACIPCControlClass::%s: service is NULL - must successfully start() first\n
IOACIPCClass::%s: region %u\n
IOACIPCClass::%s: CR properties has invalid type\n
IOACIPCClass::%s: Could not add interest notification on service: %#x\n
IOACIPCClass::%s: trIndex %u, buff %p, size %u\n
IOACIPCClass::%s: no async port\n
IOACIPCClass::%s: ret 0x%x\n
IOACIPCClass::%s: region %u, prio -> %u, tc -> %u\n
IOACIPCClass::%s: IOServiceAddMatchingNotification (kIOTerminatedNotification) failed, ret = 0x%08x
IOACIPCClass::%s: TR properties are not available\n
```
