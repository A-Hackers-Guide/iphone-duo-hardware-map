# `/usr/lib/libIOACIPC.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 134,992 bytes.

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
TracePipes
open_nl
unmapMemory
kACIPCAERNonFatalError
IOACIPCTraceClass::%s: could not open service\n
\n
abortTransferRingAsync
IOACIPCTraceClass::%s: no async port\n
~IOACIPCControlClass
currentLogSnapshotBufferSize
kACIPCEventUnexpectedCompletionType
v8@?0
setUpNotificationCallback
ioAsync
kACIPCChannelResetFailed
kACIPCTLPCompletionTimeout
deactivateTracePoint
clearNotificationPort
kACIPCUnexpectedSleepMessageState
Name
start
~IOACIPCClass
kACIPCDeviceConfigError
kACIPCControlUnexpectedExecutionEnvironment
kACIPCChannelStopFailedFatal
kACIPCLinkStateHardDown
fEventNotificationPort
sendImage
flushTraceBuffers
activateAllTracePoints
!fQueue
kACIPCTransferMissingEvent
kACIPCInvalidTag
readRegister
unmapMemoryAsync
notifyMemory
kACIPCTransferCompletionUnexpected
kACIPCInvalidAsyncCDType
kACIPCDirectionIn
enablePipe
kACIPCChannelStopFailed
kACIPCCommandRingFull
kACIPCDeviceWakeTimeout
kACIPCHostConfigError
IOACIPCTraceClass::%s: \n
DEFAULT
triggerCollectTriaging
basic_string
setEventNotificationPort
collectSnapshotAsync
io
writeRegister
abortTransferRing
kACIPCTransferCompletionUnregisteredChannel
IOACIPCTraceClass::%s: buff %p, size %u\n
IOACIPCControlClass.cpp
IOACIPCClass.cpp
kACIPCDeviceInvalidStateTransition
kACIPCDeviceErrorStateTransition
kACIPCCommandUnexpectedCompletion
connect
IOACIPCTraceClass::%s: could not get matching service\n
Code
IOServiceFirstMatch
!fRunLoopRef
kACIPCTransferCompletionPartialUnexpected
kACIPCDirectionInvalid
IOACIPCTraceClass.cpp
getRegistryInfo
close
kACIPCTransferCompletionEndUnexpected
kACIPCTransferUnexpectedEvent
kACIPCLinkDownTimeout
kACIPCLinkBWNotification
kACIPCLinkStateUp
IOACIPCTraceClass::%s: could not create matching dictionary\n
IOACIPCTraceClass::%s: ret = %x\n
IOGeneralInterest
v12@?0I8
notifyMemoryAsync
kACIPCCompletionUnaligned
kACIPCChannelStartFailed
kACIPCMessageRingFull
IOACIPCTraceClass::%s: --done\n
getTraceCode
sendImageAsync
updateMemory
kACIPCLinkDown
kACIPCLinkStateSoftDown
kACIPCLinkStateManualDown
!queue
readLogsAsync
updateMemoryAsync
kACIPCTransferCompletionUnexpectedChannel
deactivateAllTracePoints
 
vector
!fEventQueue
loggerTune
kACIPCPipeOpenFailed
openPipe
kACIPCDeviceUnknownStateTransition
kACIPCSleepMessageCompletionFailed
kACIPCPortEnableFailed
kACIPCAERError
closePipe
!fEventRunLoopRef
kACIPCTransferCompletionCodeUndefined
kACIPCPipeCloseFailed
kACIPCLinkUpTimeout
kACIPCDeviceInAbortHandler
kACIPCCROpenFailed
kACIPCAERCorrectableError
fNotificationPort
kACIPCTransferCompletionSizeUnexpected
kACIPCAERFatalError
v24@?0I8I12^v16
deregisterEventNotification_nl
invalid
IOServiceTerminate
getTransferRingInfo
AppleConvergedIPCCompletionRingProperties
kACIPCTransferCompletionCodeInvalid
kACIPCLinkStateUnpoweredUp
open
kACIPCTransferCompletionOverflowUnexpected
kACIPCDeviceSleepStateInvalid
kACIPCTransferCompletionSuccessUnexpected
~IOACIPCTraceClass
stop
openService
activateTracePoint
disableKernelTraceBuffers
registerEventNotification_nl
mapMemory
SnapshotBufferSize
dumpRegistry
kACIPCTransferCompletionCodeUnknown
kACIPCPipeAbortFailed
kACIPCInvalidRingId
IOACIPCTraceClass::%s: TraceCode invalid\n
v20@?0I8^v12
kACIPCCompletionOutOfRange
kACIPCUnexpectedSleepMessageTarget
kACIPCReadFail
kACIPCDARTError
kACIPCDirectionOut
IOACIPCTraceClass::%s: no connection\n
setNotificationPort
getCompletionRingInfo
close_nl
mapMemoryAsync
kACIPCTagNotInUse
AppleConvergedIPCTransferRingProperties
generateNonce
kACIPCSendImageFailed
kACIPCContextOpenFailed
kACIPCContextCloseFailed
IOAppleConvergedIPCTraceBackendRaw
bootstage
start_nl
kACIPCBadRequestError
demo
kACIPCEnterLowPowerFailed
kACIPCEnterLowPowerTimeout
enableKernelTraceBuffers
clearEventNotificationPort
kACIPCInvalidSharedMemoryRegionId
IOACIPCControlClass::%s: \n
IOACIPCControlClass::%s: could not add interest notification on service: %#x\n
IOACIPCClass::%s: Could not add interest notification on service: %#x\n
IOACIPCClass::%s: no async port\n
IOACIPCClass::%s: region %u\n
IOACIPCControlClass::%s: service is NULL - must successfully start() first\n
IOACIPCControlClass::%s: a notification block is already registered. deregister it before registering a new block
IOACIPCControlClass::%s: subsystem %u, index %u, arg1 %p, arg2 %p\n
IOACIPCClass::%s: not open, return success\n
IOACIPCClass::%s: \n
IOACIPCClass::%s: buff %p, size %u\n
IOACIPCClass::%s: reg %u, buff %p, size %u\n
IOACIPCControlClass::%s: block must be provided\n
IOACIPCControlClass::%s: +\n
IOACIPCControlClass::%s: -\n
IOACIPCClass::%s: CR properties has invalid type\n
IOACIPCClass::%s: region %u, prio -> %u, tc -> %u\n
IOACIPCClass::%s: --done\n
IOACIPCClass::%s: TR properties are not available\n
IOACIPCClass::%s: CR properties are not available\n
IOACIPCClass::%s: TR index %u\n
IOACIPCControlClass::%s: could not get matching service\n
IOACIPCClass::%s: IOServiceAddMatchingNotification (kIOFirstMatchNotification) failed, ret = 0x%08x
IOACIPCClass::%s: IOServiceAddMatchingNotification (kIOTerminatedNotification) failed, ret = 0x%08x
IOACIPCClass::%s: already stopped, returning true\n
IOACIPCClass::%s: TR properties has invalid type\n
IOACIPCClass::%s: trIndex %u, buff %p, size %u, footer %p, size %u\n
IOACIPCClass::%s: ret 0x%x\n
IOACIPCClass::%s: region %u, size %u\n
IOACIPCControlClass::%s: --done\n
IOACIPCControlClass::%s: buff %p, size %u\n
IOACIPCControlClass::%s: no async port\n
IOACIPCClass::%s: trIndex %u, buff %p, size %u\n
IOACIPCClass::%s: ret 0x%x, buff %p, size %u, cookie %u\n
```
