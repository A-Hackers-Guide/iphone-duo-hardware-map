# `/usr/lib/libIOABP.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 112,768 bytes.

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
fNotificationPort
deregisterEventNotification_nl
start_nl
kABPAERNonFatalError
connect
closePipe
registerEventNotification_nl
IOABPClass::%s: could not create matching dictionary\n
writeAsync
kABPSleepMessageCompletionFailed
kABPDeviceWakeTimeout
vector
IOGeneralInterest
IOABPClass::%s: \n
kABPLinkBWNotification
IOABPControlClass::%s: could not add interest notification on service: %#x\n
close_nl
IOABPClass::%s: Could not add interest notification on service: %#x\n
IOABPClass::%s: no async port\n
unmapMemoryAsync
kABPTransferCompletionCodeInvalid
kABPTransferCompletionUnregisteredChannel
kABPChannelStartFailed
IOABPClass::%s: already stopped, returning true\n
IOABPControlClass.cpp
IOServiceFirstMatch
IOABPClass::%s: direction %s\n
kABPLinkUpTimeout
kABPBHIMaxRegisters
kABPAERFatalError
kABPMessageRingFull
IOABPControlClass::%s: could not create matching dictionary\n
IOABPControlClass::%s: --done\n
stop
fEventNotificationPort
v8@?0
IOABPClass::%s: region %u\n
IOABPTraceClass::%s: \n
bootstage
kABPCommandRingFull
kABPDeviceSleepStateInvalid
TracePipes
SnapshotBufferSize
IOABPTraceClass::%s: no connection\n
!fQueue
IOABPClass::%s: IOServiceAddMatchingNotification (kIOTerminatedNotification) failed, ret = 0x%08x
IOABPClass.cpp
ABPInterfaceProtocol
demo
IOABPClass::%s: ret 0x%x, buff %p, size %u, cookie %u\n
kABPTransferCompletionEndUnexpected
kABPControlUnexpectedExecutionEnvironment
~IOABPTraceClass
sendImage
startChannelAsync
kABPChannelStopFailed
kABPLinkSpeedMismatch
IOABPTraceClass::%s: --done\n
~IOABPClass
IOABPClass::%s: reg %u, buff %p, size %u\n
kABPDeviceUnknownStateTransition
kABPTransferCompletionUnexpectedChannel
!fEventQueue
open
IOABPControlClass::%s: a notification block is already registered. deregister it before registering a new block
setUpNotificationCallback
sendImageAsync
kABPEventUnexpectedCompletionType
kABPAERCorrectableError
IOABPTraceClass.cpp
IOABPClass::%s: IOServiceAddMatchingNotification (kIOFirstMatchNotification) failed, ret = 0x%08x
timeSyncAsync
kABPDeviceErrorStateTransition
kABPBTIChipInfo
Name
DEFAULT
clearEventNotificationPort
IOABPControlClass::%s: service is NULL - must successfully start() first\n
loggerTune
clearNotificationPort
readRegister
kABPTransferCompletionSizeUnexpected
kABPLinkDown
~IOABPControlClass
IOABPClass::%s: region %u, size %u\n
IOABPTraceClass::%s: could not open service\n
dumpRegistry
getRegistryInfo
setEventNotificationPort
read
kABPPipeOpenFailed
kABPPipeCloseFailed
kABPDeviceInvalidStateTransition
kABPDeviceConfigError
IOABPClass::%s: for %s\n
mapMemoryAsync
kABPCompletionUnaligned
kABPBHISBLAntiRollover
kABPLinkStateUnpoweredUp
kABPLinkStateManualDown
logSnapshotBufferSize
kABPTransferCompletionPartialUnexpected
kABPTransferCompletionSuccessUnexpected
kABPUnexpectedSleepMessageTarget
kABPEnterLowPowerTimeout
kABPBHISerialNum
kABPDirectionIn
openPipe
readAsync
kABPInvalidTimesyncDomain
kABPBHINumSeg
IOABPTraceClass::%s: could not create matching dictionary\n
IOABPTraceClass::%s: no async port\n
kABPUnexpectedSleepMessageState
open_nl
AppleBasebandPCIInterface
v12@?0I8
abortChannelAsync
kABPInvalidTimeUnit
IOABPControlClass::%s: +\n
invalid
IOABPClass::%s: not open, return success\n
kABPCommandUnexpectedCompletion
kABPSendImageFailed
kABPLinkStateUp
kABPTransferCompletionCodeUnknown
kABPTransferCompletionOverflowUnexpected
kABPTransferCompletionUnexpected
IOServiceTerminate
start
setNotificationPort
IOABPControlClass::%s: subsystem %u, index %u, arg1 %p, arg2 %p\n
kABPEnterLowPowerFailed
IOABPControlClass::%s: \n
AppleBasebandPCIControl
IOABPControlClass::%s: could not get matching service\n
!fEventRunLoopRef
kABPTransferMissingEvent
kABPPipeAbortFailed
kABPLinkStateHardDown
AppleBasebandPCITraceBackendRaw
!queue
IOABPControlClass::%s: -\n
write
kABPTransferUnexpectedEvent
kABPTLPCompletionTimeout
Code
IOABPTraceClass::%s: buff %p, size %u\n
getTraceCode
IOABPClass::%s: --done\n
kABPChannelResetFailed
kABPBHIOEMPkHash
IOABPControlClass::%s: buff %p, size %u\n
kABPTransferCompletionCodeUndefined
kABPReadFail
kABPLinkDownTimeout
kABPDARTError
kABPDirectionOut
IOABPControlClass::%s: no async port\n
v24@?0I8I12^v16
!fRunLoopRef
kABPCompletionOutOfRange
kABPBadRequestError
close
kABPPortEnableFailed
kABPBHIMSMHwId
kABPBTIMaxRegisters
basic_string
IOABPClass::%s: buff %p, size %u\n
readLogsAsync
IOABPControlClass::%s: block must be provided\n
kABPAERError
kABPLinkStateSoftDown
IOABPTraceClass::%s: could not get matching service\n
flushTraceBuffers
IOABPTraceClass::%s: TraceCode invalid\n
```
