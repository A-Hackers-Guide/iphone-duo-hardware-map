# `/usr/lib/libIOABP.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 112,768 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 1936)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (5)

- `/usr/lib/libIOABP.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (176)

```
kABPBadRequestError
kABPBHIOEMPkHash
~IOABPControlClass
readLogsAsync
~IOABPClass
IOABPClass.cpp
kABPBTIMaxRegisters
open
IOABPControlClass::%s: a notification block is already registered. deregister it before registering a new block
readRegister
IOABPClass::%s: direction %s\n
connect
TracePipes
DEFAULT
IOABPTraceClass::%s: no connection\n
IOABPControlClass::%s: block must be provided\n
invalid
IOABPClass::%s: Could not add interest notification on service: %#x\n
write
abortChannelAsync
start
IOABPControlClass::%s: service is NULL - must successfully start() first\n
IOABPControlClass::%s: -\n
!fQueue
IOABPClass::%s: buff %p, size %u\n
kABPDeviceErrorStateTransition
kABPEnterLowPowerFailed
kABPLinkDown
registerEventNotification_nl
kABPCompletionOutOfRange
kABPChannelStopFailed
kABPLinkStateUnpoweredUp
kABPAERNonFatalError
openPipe
IOABPControlClass::%s: buff %p, size %u\n
IOGeneralInterest
kABPChannelResetFailed
kABPControlUnexpectedExecutionEnvironment
kABPLinkUpTimeout
kABPDeviceInvalidStateTransition
kABPBHIMSMHwId
~IOABPTraceClass
IOABPTraceClass::%s: could not open service\n
IOABPTraceClass::%s: --done\n
demo
IOABPControlClass::%s: \n
loggerTune
kABPTransferCompletionEndUnexpected
kABPTransferUnexpectedEvent
kABPPipeOpenFailed
kABPPipeCloseFailed
AppleBasebandPCITraceBackendRaw
start_nl
IOServiceFirstMatch
kABPInvalidTimesyncDomain
kABPLinkStateSoftDown
closePipe
IOABPClass::%s: for %s\n
IOABPClass::%s: --done\n
kABPCompletionUnaligned
kABPLinkStateManualDown
kABPAERFatalError
IOABPTraceClass::%s: TraceCode invalid\n
kABPTransferCompletionCodeUnknown
kABPTLPCompletionTimeout
kABPLinkSpeedMismatch
kABPBHINumSeg
IOABPTraceClass::%s: could not create matching dictionary\n
IOABPTraceClass::%s: no async port\n
getRegistryInfo
IOABPControlClass.cpp
close
!fRunLoopRef
IOABPClass::%s: already stopped, returning true\n
readAsync
IOABPClass::%s: ret 0x%x, buff %p, size %u, cookie %u\n
kABPSendImageFailed
v8@?0
IOABPClass::%s: reg %u, buff %p, size %u\n
startChannelAsync
IOABPControlClass::%s: no async port\n
IOABPClass::%s: \n
IOABPClass::%s: no async port\n
sendImage
kABPTransferCompletionUnregisteredChannel
kABPEnterLowPowerTimeout
kABPDeviceWakeTimeout
kABPDARTError
IOABPClass::%s: IOServiceAddMatchingNotification (kIOTerminatedNotification) failed, ret = 0x%08x
sendImageAsync
unmapMemoryAsync
kABPTransferCompletionSizeUnexpected
kABPInvalidTimeUnit
kABPBHIMaxRegisters
kABPAERCorrectableError
getTraceCode
!fEventRunLoopRef
close_nl
read
open_nl
kABPTransferCompletionUnexpectedChannel
kABPUnexpectedSleepMessageState
kABPDeviceSleepStateInvalid
vector
kABPSleepMessageCompletionFailed
kABPLinkStateUp
IOABPTraceClass.cpp
!fEventQueue
mapMemoryAsync
kABPEventUnexpectedCompletionType
Name
IOABPControlClass::%s: --done\n
logSnapshotBufferSize
writeAsync
kABPUnexpectedSleepMessageTarget
kABPBHISerialNum
setEventNotificationPort
IOABPControlClass::%s: +\n
kABPTransferCompletionOverflowUnexpected
kABPLinkStateHardDown
fNotificationPort
IOABPControlClass::%s: could not add interest notification on service: %#x\n
ABPInterfaceProtocol
IOABPClass::%s: not open, return success\n
setUpNotificationCallback
kABPTransferCompletionCodeInvalid
bootstage
IOABPClass::%s: IOServiceAddMatchingNotification (kIOFirstMatchNotification) failed, ret = 0x%08x
AppleBasebandPCIControl
IOServiceTerminate
kABPTransferMissingEvent
kABPDirectionIn
dumpRegistry
flushTraceBuffers
fEventNotificationPort
deregisterEventNotification_nl
IOABPClass::%s: could not create matching dictionary\n
clearNotificationPort
kABPTransferCompletionPartialUnexpected
kABPReadFail
SnapshotBufferSize
stop
!queue
kABPTransferCompletionCodeUndefined
kABPTransferCompletionSuccessUnexpected
kABPPipeAbortFailed
kABPDeviceConfigError
kABPLinkBWNotification
kABPBTIChipInfo
IOABPControlClass::%s: subsystem %u, index %u, arg1 %p, arg2 %p\n
kABPLinkDownTimeout
IOABPTraceClass::%s: \n
IOABPTraceClass::%s: could not get matching service\n
kABPMessageRingFull
IOABPControlClass::%s: could not create matching dictionary\n
timeSyncAsync
IOABPClass::%s: region %u, size %u\n
kABPTransferCompletionUnexpected
kABPDeviceUnknownStateTransition
IOABPControlClass::%s: could not get matching service\n
v12@?0I8
IOABPClass::%s: region %u\n
kABPAERError
kABPDirectionOut
IOABPTraceClass::%s: buff %p, size %u\n
basic_string
v24@?0I8I12^v16
AppleBasebandPCIInterface
kABPChannelStartFailed
kABPBHISBLAntiRollover
Code
setNotificationPort
clearEventNotificationPort
kABPCommandRingFull
kABPCommandUnexpectedCompletion
kABPPortEnableFailed
```
