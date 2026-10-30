# `/System/DriverKit/System/Library/PrivateFrameworks/CentauriAlpha.framework/CentauriAlpha`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 459,008 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 2504)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/System/DriverKit/System/Library/PrivateFrameworks/CentauriAlpha.framework/CentauriAlpha (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/System/Library/PrivateFrameworks/AirshipDK.framework/AirshipDK (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/System/Library/PrivateFrameworks/CentauriManager.framework/CentauriManager (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/System/Library/PrivateFrameworks/CoreCaptureDriverKit.framework/CoreCaptureDriverKit (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/System/Library/Frameworks/PCIDriverKit.framework/PCIDriverKit (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/usr/lib/libc++.dylib (compatibility version 1.0.0, current version 2200.32.0)`

## Entitlements

```xml
  - no entitlements
```

## Strings (1,146)

```
centauri-fatal-err-panic
blockCopy
%s::%s: coredump/crashlog completion failed (ret=0x%x) \n
%s::%s: ptm requester role not supported \n
%s::%s: failed to create log stream \n
%s::%s: prepare for reset handler is not registered \n
%s::%s: service matching set up for %s \n
%s::%s: first power on \n
ChangePowerState(kIOServicePowerCapabilityOn) == kIOReturnSuccess
%s::%s: block copy failed \n
%s::%s: requesting deferral (low power: %u, defer for memswap: %s) \n
flrCountDict
    crashlogPending: %d\n
serializedBuffer && serializedLength
%s::%s: failed to create error event action ret = 0x%x \n
%s::%s: failed to set os action handler (ret = 0x%x) \n
%s::%s: timer expired waiting for remote service in dext crash recovery state \n
CancelPropertyUpdateNotificationHandler
!ivars->deferredWork.reset
PrepareDMACommand
ExtractCrashlogReason
ErrorCode
i8@?0
SACFunctionAvailable
SetupServiceMatchingNotification
%s::%s: reset in progress. ignoring error \n
%s::%s: PCI dart error \n
CollectLogsCompletion
resetInfo:\n
%s::%s: state %u \n
ivars->systemStateResetItemDict->setObject(kCentauriSystemStateNotificationResetKey, inReset ? kOSBooleanTrue : kOSBooleanFalse)
%s::%s: memswap memory map is already set \n
ConfigureEndpointForMemSwap
val && ivars->resetTimestamps->setObject(eventName, val)
%s::%s: failed to find MSI property \n
BT
%s::%s: failed to copy prepareCb block \n
AdditionalPipeOwners
report-error
SetErrorHandler
%s::%s: failed to set dict object \n
%s::%s: resuming fatal log collection (state = 0x%x) \n
Running
%s::%s: errorCode %u, reason %s \n
SetCrashlogHandler_block_invoke
ssID < kNumSubsystems
%s::%s: failed HasPCIPowerManagement (ret = 0x%x) \n
CentauriUserClientProperties
msi-reservation-size
GetASPMState
LPMOS
%s::%s: invalid fault reporter \n
com.apple.centauri.reset.wifi
%s::%s: centauri-driverkit=0 \n
Default
%s::%s: failed to create logger queue (ret = 0x%x) \n
AppleCentauriManager::SaveClientProperty(this, key, newValue, kCentauriAutoClearOnChipReset) == kIOReturnSuccess
    type: %s\n
UnexpectedDextTermination
%s::%s: failed to create timer src (ret = 0x%x) \n
OpenRemoteService
%s::%s: %s property exists - skipping dext crash \n
obj
%s::%s: dispatching propertyUpdateNotification \n
flrCountObject != nullptr
%s::%s: failed to allocate statedump buffer \n
UnexpectedDextTermination-UserspaceReboot
%s::%s: AppleCentauriManager::Open failed (ret = 0x%x) \n
%s::%s: failed to create os action for collect logs (ret = 0x%x) \n
%s::%s: invalid state (%s) \n
GetCrashlogs
dataObject->getLength() == sizeof(uint32_t)
LPW
loggerstream
Start_Impl
WaitForRemote
 w 
%s::%s: empty crash log buffer \n
!ivars->resetPrepareHandler
CancelCrashlogHandler_block_invoke
init
completion
FLRCount
%s::%s: failed to get default queue (ret = 0x%x) \n
%s::%s: no prepare for reset handler \n
CollectLogsStateDumps
SetDextRecoveryState_block_invoke
Invalid
%s::%s: failed to get owner object \n
%s::%s: failed to SaveDeviceState (ret = 0x%x) \n
%s::%s: GetBusyState ret = 0x%x \n
EndWork
%s::%s: failed to create memswap os action (ret = 0x%x) \n
%s::%s: module name not found \n
%s::%s: airship service not ready \n
ExecuteDeferredWork
%s::%s: device id: 0x%x \n
%s::%s: finalize %d \n
%s::%s: fw crash reason string is not supported with non-fatal log collection \n
IsBackToBack
CoredumpDuration
%s::%s: invalid parameters \n
%s::%s:  \n
ServiceNotificationReady_Impl
%s::%s: invalid notifier \n
%s::%s: failed to  SearchProperty (ret = 0x%x) \n
Reset
%s::%s: chip crash timed out \n
count  primaryStart    secondaryStart  end           type\n
EnqueueDeferredWork
ExitLPW
WaitForReadyForReset
    promoteToFullReset: %d\n
CacheCrashlogs
%s::%s: airship not up; returning %s \n
ExecuteDeferredWorkAsync_block_invoke
%s::%s: failed to validate segment length (ret = 0x%x expected %llu got %llu) \n
PreBoot
CollectLogsCallback_Impl
%06llu.%06llu SetBusLeadEnable Start enable: %s\n
CollectPowerStateLog
ClearUnsupportedRequestAER
%s::%s: number of MSIs requested: %u \n
EnablePTMOnEndpoint
ModuleName
centauri-flr-limit
ivars->inFlightWork < UINT32_MAX
%s::%s: errorSource: %u, errorCode: %u, arg: 0x%llx \n
AppleCentauri-129
setFLRBit
Owner
No
%s::%s: ignoring based on boot-arg \n
%s::%s: ErrorDetected's value type is not a dictionary \n
%s::%s: failed to create osdata object \n
%06llu.%06llu 0x%08llx %s 0x%08x\n
%s::%s: failed to get platform (ret = 0x%x) \n
%s::%s: testID: %u \n
centauri-flr-timeout-ms
InterruptOccurred_Impl
%s::%s: Crashlog Reason: \"%s\" \n
WaitForPCIErrorNotifications
dict
%s::%s: boot stage = %s \n
CentauriMSILog.txt
crashlogEnd
%s::%s: bad arg \n
%s::%s: match notification for CentauriRemoteInterface \n
PartiallyBooted
UpTimestamp
FetchMemSwap
%s::%s: error arg not an OSNumber \n
%s::%s: failed to alloc OSNumber for monotonic time \n
%s::%s: failed to set dict object for %s \n
%s::%s: reset failed (ret = 0x%x) \n
%s::%s: ret: 0x%x flags: 0x%qx cnt: %d addr: 0x%qx len: 0x%qx \n
v8@?0
%s::%s: invalid cmd id: %u \n
B24@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}16
key && dict
MSI-1
item->block
InitializeMSI
ServiceNotificationReady_Impl_block_invoke_2
%s::%s: not permitted for ss id %u \n
ivars->cachedErrorsArray->setObject(cachedError)
test
%s::%s: MSICapOffset::%llx \n
ivars->pciDevice
%s::%s: not permitted \n
SetProperties_Impl
CentauriManagerErrorHandler_Impl
ivars->dextRecoveryState == kCentauriDextRecoveryStateFetchMemSwap
Off
ivars->finalizeHandler
%s::%s: service notification (type: %llu) \n
%s::%s: driver offline - ignoring exec stage notification \n
%s::%s: dispatching cached errors \n
%s::%s: invalid state for reset %u \n
%s::%s: deferring reset \n
address && length && coredump
ErrorArg
N/A
length < sizeof(fullReason)
DoReset
eventName && payload
fatalLogCollectionTriggered
%s::%s: failed to update the FW crash reason string \n
%s::%s: failed to allocate lock \n
newValue
AirshipDriverConfigName
CollectLogsFatal
state: %s\n
%s::%s: MSI handler: boot stage = %u \n
CollectDeferredFaultDataCb
%s::%s: termination notification for AirshipDriverDK \n
%s::%s: full chip reset in progress \n
InReset
CentauriControlRemoteInterface
0x%04llu %06llu.%06llu - %06llu.%06llu - %06llu.%06llu %s\n
prevState == kCentauriDextRecoveryStateCollectLogs
%s::%s: failed to allocate pending work item \n
%s::%s: failed to find aer capability (ret = 0x%x) \n
%s::%s: sleeping for %u ms... \n
%s::%s: failed to get provider queue \n
ExternalMethod
OSAction_CentauriSubsystem_ChipResetCallback
%s::%s: pmcsr 0x%04x \n
[Fatal]
time          r/w address    value\n
TriggerChipCrash
%s::%s: Crashlog Reason not found from the Crashlog data \n
ret == kIOReturnSuccess
%s::%s: requesting full wake \n
flrCount && *flrCount
%s::%s: bad size (got %u max %u) \n
ClearConfigSpaceMailboxes
%s::%s: crashlog too small: %zu bytes \n
fLock
resetStart
%s::%s: failed to report error (ret = 0x%x) \n
SetupRemoteActionCallbacks
%s::%s: failed to set airship driver config \n
%s::%s: invalid state for watchdog notification: %u \n
inLowPower: %d\n
chipId: %s\n
SetDextRecoveryState
%s::%s: failed to copy immediateCb block \n
ivars->cachedErrorsArray
/Library/Caches/com.apple.xbs/558FE645-4E39-4399-A06E-8DC20AC536F1/TemporaryDirectory.VSeWMb/Sources/AppleCentauri_driverkit/CentauriSubsystem/CentauriSubsystem.cpp
Reset_block_invoke
%s::%s: failed to create function name copy \n
%06llu.%06llu RestoreDeviceState ret: 0x%03x\n
timeElapsedObject != nullptr
BootComplete
prepareChipForResetEnd
NotifyPropertyUpdate
%s::%s: ASPM state: %u \n
OS
Crashed
%s::%s: stream: failed to copy log identifier %s \n
ClientCrashlogHandler
%s::%s: selector %llu \n
OSAction_CentauriSubsystem_TimerOccurred
%s::%s: handler already exists \n
%s::%s: failed to create memory map (ret = 0x%x) \n
%s::%s: failed to copy provider properties \n
%s::%s: data::%x \n
%s::%s: invalid crashlog data \n
%s::%s: Logging prop: owner: %s dir: %s file: %s id: %s \n
%s::%s: failed to allocate memory \n
FaultReporter
%s::%s: failed to create reset state item (ret=0x%x) \n
InitMemSwapWorkingCopy
no
ivars->cachedCrashlogsArray->getCount() > 0
%s::%s: in fatal error state (%u) \n
%s::%s: ptm enabled, clock granularity: %u ns \n
%s::%s: crashlog header reports empty: %zu bytes \n
%s::%s: skipping %s \n
%s::%s: Open error (ret = 0x%x) \n
errorData
%s::%s: failed to create reason string copy \n
%s::%s: invalid queue \n
!ivars->crashlogHandler
%s
MemSwapCallback_Impl
data
%s::%s: clearing cfg mbx at offset 0x%x \n
Crashlog.BTMAIN.bin
%s::%s: airship reported error: 0x%x \n
success
pmcsr != nullptr
-
pci-dart-error-data
%s::%s: crash poll iterations = %u \n
Offline
StateSnapshots
%s::%s: driver offline - ignoring airship fatal error notification \n
%s::%s: deferred work is canceled \n
functionResetEnd
%s::%s: failed to get log file name \n
TriggerFaultReport
%s::%s: unexpected match notification \n
SetupMemSwapRegion
CollectLogs_block_invoke
%s::%s: failed to serialize \n
%s::%s: failed to set enable int source (ret = 0x%x) \n
%s::%s: failed to get MSI addr (ret = 0x%x) \n
ivars->logCollectionInfo.metadata
%s::%s: boot stage: %s, fw state: %s \n
DextRelaunchState
%s::%s: failed to get IOPCIDevice \n
SetRequireClientProperty
force panic on fatal error for ss %u (type %u)
CollectLogsCallback_Impl_block_invoke
%s::%s: invalid memswap map or working copy desc \n
%06llu.%06llu Reset Complete ret: 0x%03x\n
prevState == kCentauriDextRecoveryStateIdle || prevState == kCentauriDextRecoveryStateWaitForRemote
%s::%s: failed to alloc OSString \n
GetCachedErrorCount
ReadyForResetDuration
coredumpStart
%s::%s: using console log level %u \n
LogFileName
SetPrepareForResetHandler_block_invoke
ClientOpen_block_invoke
%s::%s: failed to create pci error queue (ret = 0x%x) \n
centauri-recovery
GetFirmwareState
prepareChipForResetStart
TimerOccurred_Impl
%s::%s: unexpected crash log completion \n
%06llu.%06llu %s 0x%08x 0x%08x\n
MaskUnsupportedRequestAER
MonotonicTimestamp
%s::%s: logpipe: failed to copy log identifier %s \n
%s::%s: failed to get provider \n
AirshipDriverDK
%s::%s: failed to set properties (ret = 0x%x) \n
%06llu.%06llu Reset Start\n
CollectChipInfo
AbortHandler
%s::%s: logpipe: failed to copy file name %s \n
%s::%s: failed to get airship probe result \n
OSAction_CentauriSubsystem_CollectLogsCallback
free
dextRelaunchObj != nullptr
ReleasePMAssertion(ivars->pmAssertionID) == kIOReturnSuccess
%s::%s: failed to create chip object for family %u \n
%s::%s: function reset already in progress \n
%s::%s: crashlog size larger than buffer (%zu > %zu) \n
OSAction_CentauriSubsystem_WatchdogCallback
OSAction_CentauriSubsystem_CentauriManagerErrorHandler
ivars->inFlightWork > 0
SetErrorHandler_block_invoke
%s::%s: added file %s, size %zu \n
sacObj != nullptr
ExecStageChanged
%s::%s: timer expired waiting for remote service in reset failed state \n
%s::%s: invalid number of MSIs configured: %u \n
%s::%s: invalid viddid 0x%x \n
completionCopy
%s::%s: resuming reset (state = 0x%x) \n
%s::%s: failed to copy properties \n
TimeToTriggerCollectLogs
SetPrepareForResetHandler
%s::%s: error filling buffer, bytesPrinted: %d kLineLength: %u \n
%s::%s: pci device not open \n
RunningLPM
action == ivars->timerAction
ReadMSIData
%s::%s: failed to send %s (ret=0x%x) \n
com.apple.ConnectivityDriver.TimeSinceLastFLR
dict && dict->setObject(kCentauriPropertyPTMEnabledOnEndpoint, ptmStatus)
ROM
TriggerPanic
errorInfo
%s::%s: deferring due to low power \n
subsystemNameObject
CollectImmediateFaultDataCb
Stop_Impl_block_invoke
%s::%s: failed to create osdata object for %s \n
CentauriStateDump.txt
GetNumMSIVectorsRequested
TimeElapsed
SetState
%s::%s: client: %s \n
%s::%s: failed to RestoreDeviceState (ret = 0x%x) \n
Subsystem
%s::%s: failed to create fault reporter \n
%s::%s: failed to get the fault reporter additional owner \n
%s::%s: skipping during dext crash recovery \n
NewUserClient_Impl
%s::%s: error handler has been deregistered \n
PrepareChipForReset
%s::%s: failed to find msi capability (ret = 0x%x) \n
%s::%s: current timestamp is older than last reset timestamp, ignoring \n
On
DartMapMemSwapWorkingCopy
%s::%s: failed to create file name copy \n
flrLimit: %d\n
in low power
SendTimeSinceLastFLRAnalytics
FLRDuration
%s::%s: failed to copy deferredCb block \n
%s::%s: escalate FLR failure \n
false
dict->setObject(key, kOSBooleanTrue)
CollectMemoryLog
CentauriMemoryAccessLog.txt
%s::%s: failed to create osdata object for StateDump \n
%s::%s: log collection failed (ret = 0x%x) \n
PrepareFaultReportCb
%s::%s: unexpected termination notification \n
ivars->queue->OnQueue()
%s::%s: remote interface error (ret = 0x%x) \n
%s::%s: poll count %u \n
%s::%s: found crashlog data for %s \n
GetFaultReporter
v12@?0i8
%s::%s: boot stage = ready for reset \n
%s::%s: failed to alloc OSNumber for SS ID \n
!ivars->deferredWork.logCollection
%s::%s: pci read invalid data \n
WiFi
CreateSystemStateNotificationItems
%s::%s: LPM log collection mode unsupported \n
%s::%s: crashlog handler is not registered \n
cachedError
ivars->timerSource
centauri-allow-panic
prevState == kCentauriDextRecoveryStateIdle
OSAction_CentauriSubsystem_InterruptOccurred
%s::%s: offline \n
errorDataObj != nullptr
%s::%s: invalid client \n
%s::%s: state: 0x%x \n
%s::%s: log collection already enqueued \n
CancelDeferredWork
%s::%s: failed to configure interrupts (ret = 0x%x) \n
ResetDone
%s::%s: log collection in progress/enqueued \n
Fiq
fwCrashReported
%s::%s: invalid bootstage 0x%x \n
ClientClose
%s::%s: FLR limit (%u) reached \n
dextRecoveryState: %s\n
%s::%s: caching crashlog \n
%s::%s: failed to get logging properties object \n
kCentauriAlphaRemoteServiceTimeoutErrorKey
%s::%s: failed to create reset timestamps dict \n
%s::%s: failed to create dispatch src (ret = 0x%x) \n
isASPMEnabled
centauri-consoleloglevel
Start_Impl_block_invoke_3
val
%s::%s: error source not found for %s \n
%s::%s: completion \n
%s::%s: failed to set reason object \n
CollectConfigLogs
waitingForReadyForReset
CancelPrepareForResetHandler
kCentauriAlphaFLRCount
super::ClientOpen(clientNameCopy->getCStringNoCopy(), cookie) == kIOReturnSuccess
WatchdogCallback_Impl_block_invoke
oldValue != nullptr
%s::%s: failed to set real time object \n
null
copy
NumMSIs
durationObject != nullptr
logCollectionInfo:\n
ivars->resetPrepareHandler
v24@?0I8I12^v16
!ivars->remoteInterfaceAvailable
%s::%s: new exec stage: %u \n
%s::%s: failed to schedule immediate wake \n
%s::%s: failed to get addr range (ret = 0x%x) \n
%s::%s: buffer filled, totalBytesPrinted: %u bufferSize: %u \n
ErrorDetected
Crashlog
%s::%s: invalid callback parameters \n
%s::%s: airship reported fatal error: %s \n
%s::%s: failed to save FLR timestamps \n
%s::%s: failed to copy completion block \n
abort handler
%s::%s: failed to set up time object \n
TimeToOSBootStage
com.apple.ConnectivityDriver.FLRPerformanceStats
CancelPrepareForResetHandler_block_invoke
%s::%s: invalid number of MSIs requested: %u available: %u \n
ServiceNotificationReady_Impl_block_invoke
TriggerClientLaunch
ret == kIOReturnSuccess || ret == kIOReturnNotFound
%s::%s: PCI dart error %u: [%s] addressLo: 0x%x addressHi: 0x%x \n
%s::%s: failed to get user client service \n
CancelErrorHandler
%s::%s: failed to set dict object for StateDump \n
%s::%s: failed to create os action (ret = 0x%x) \n
execStage <= kCentauriBootStageMax
%s::%s: failed to create os action for watchdog notification (ret = 0x%x) \n
version: %s\n
%s::%s: cachedErrorCount: %u \n
%s::%s: %s \n
%s::%s: signature mismatch \n
LPMBoot
%s::%s: Driver offline. Ignoring state change %u \n
%s::%s: failed to set require client property (ret = 0x%x) \n
pci-get-dart-error
%06llu.%06llu SaveDeviceState ret: 0x%03x\n
%06llu.%06llu SetupMemSwapRegion ret: 0x%03x\n
CollectStateSnapshots
    updateFWReasonString: %d\n
%s::%s: crash log buffer too small: %zu bytes \n
centauri-driverkit
%s::%s: number of MSIs requested: %u (SingleMSI mode) \n
%s::%s: deliver notification error (ret = 0x%x) \n
ctx
ScheduleImmediateWake
CentauriConfigAccessLog.txt
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x \n
Control
%s::%s: Stop ret = 0x%x \n
ret == kIOReturnSuccess || ret == kIOReturnNotOpen
!ivars->logCollectionInfo.metadata && !ivars->logCollectionInfo.completion
%06llu.%06llu 0x%x\n
%s::%s: failed to create osdict \n
ivars->resetTimestamps
Reason
%s::%s: failed to copy completionCb block \n
v20@?0^{AirshipDriverDK=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})(?=^{AirshipDriverDK_IVars}^{AirshipDriverDK_LocalIVars})}8I16
%s::%s: failed to create user client (ret = 0x%x) \n
fatal
%s::%s: failed to find PCI capability (ret = 0x%x) \n
readData
Idle
ReadyForReset
(null)
ivars->loggerQueue->OnQueue()
%s::%s: driver offline - ignoring airship error notification \n
WR
%s::%s: FLR timed out \n
%s::%s: using cc log level %u \n
%s::%s: powerFlags: %s \n
ClientOpen
%s::%s: cmd id %u ret 0x%x \n
%s::%s: section too small \n
SendAnalytics
LogIdentifier
kCentauriAlphaMemswapTimeoutErrorKey
bootStageOSAlpha
v32@?0Q8^{IOService=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})}16Q24
IOPCIPMCSState
%s::%s: error code not found \n
remoteInterfaceAvailable: %d\n
CrashlogDuration
SubsystemID
OSAction_CentauriSubsystem_CompletionCallback
%s::%s: remote service unavailable. wait for %u ms \n
%s::%s: requesting crashlog failed (ret=0x%x) \n
CollectAirshipStateDumps
Recovery
CancelCrashlogHandler
derivedProbeDevice
%s::%s: timer expired waiting for memswap info in dext crash recovery state \n
userClient
yes
%s::%s: invalid state (%u) \n
%s::%s: FLR timeout override: %u ms \n
startTimeObject && endTimeObject
%s::%s: driver offline \n
%s::%s: match notification for AirshipDriverDK \n
dict && dict->setObject(\"RequireClient\", kOSBooleanTrue)
SetPowerState_Impl
AppleCentauriManager::SaveClientProperty(this, key, newValue, autoClearConditions) == kIOReturnSuccess
name
%s::%s: options 0x%x reason %s \n
ivars->cachedCrashlogsArray
%s::%s: failed to open IOPCIDevice (ret = 0x%x) \n
%s::%s: FLR limit override boot-arg is set \n
%s::%s: error handler not registered \n
key
%s::%s: state = %u \n
dict->setObject(kCentauriSystemStateNotificationResetKey, kOSBooleanTrue)
remoteService: %s\n
%s::%s: invalid driver state %u for dext crash recovery state %u \n
%s::%s: failed to create chip reset os action (ret = 0x%x) \n
WatchdogCallback_Impl
 r 
action == ivars->msiAction
%s::%s: failed to create log pipe with provider %s \n
%s::%s: provider not available \n
%s::%s: propertyUpdateNotification handler not registered \n
%s::%s: failed to set boot complete property (ret = 0x%x) \n
%s::%s: failed to alloc OSNumber for real time \n
ivars->logCollectionInfo.completion
ivars->cachedCrashlogsArray->setObject(copy)
LogCollection
CentauriDebug
%s::%s: failed to create data log pipe \n
%s::%s: failed super Start (ret = 0x%x) \n
%s::%s: failed to alloc metadata \n
%s::%s: reserved MSIs via provider \n
%s::%s: failed to find ptm capability (ret = 0x%x) \n
%s::%s: datapipe: failed to copy directory name %s \n
PrepareForReset
CollectDeferredFaultDataCb_block_invoke
%s::%s: invalid filename/statedump \n
/Library/Caches/com.apple.xbs/558FE645-4E39-4399-A06E-8DC20AC536F1/TemporaryDirectory.VSeWMb/Sources/AppleCentauri_driverkit/CentauriSubsystem/CentauriSubsystemUserClient.cpp
%s::%s: failed to create airship transport \n
ivars->memSwapAction && ivars->completionAction && ivars->chipResetAction && ivars->collectLogsAction && ivars->watchdogAction
%s::%s: chip class not initialized \n
%s::%s: returned from SetProperties (ret = 0x%x) \n
%06llu.%06llu CollectLogs Complete ret: 0x%03x\n
%s::%s: Transaction pending poll timed out. Proceeding to FLR \n
LoggingProperties
%s::%s: fault reporter is busy \n
%s::%s: no ptm key - bailing out \n
[NonFatal]
%s::%s: tp poll count %u \n
%s::%s: didDextRelaunch = %s (reason %u) \n
SetPTMProperty
%s::%s: failed to set monotonic time object \n
%s::%s: warning: prepare for reset handler is not registered \n
%s::%s: no crashlog handler \n
t2026
OSAction_CentauriSubsystem_ServiceNotificationReady
%s::%s: failed to enable timer (ret = 0x%x) \n
%s::%s: Using FLR limit: %u \n
CopyName(&serviceName) == kIOReturnSuccess
%s::%s: error reported by %s error code %u \n
SetPropertyUpdateNotificationHandler
DeferReset
AirshipStateDump.bin
derivedStop
cachedError->getLength() == sizeof(CentauriCachedErrorInfo)
%s::%s: memswap memory is already DART mapped \n
%s::%s: deferring (state = 0x%x) \n
CentauriEventLog.txt
FunctionReset
%s::%s: failed to allocate inFlightLock \n
%s::%s: SetProperties failed \n
GetBootStageMirror
SetIPCProperties
%s::%s: %u \n
%s::%s: error handler already exists \n
DirectoryName
SetCrashlogHandler
IsValidBootStage
!ivars->inLowPower
%s::%s: invalid segment count %u \n
%s::%s: invalid length \n
%s::%s: invalid link control value \n
clientNameCopy
%s::%s: failed to create dict \n
%s::%s: failed to create completion os action (ret = 0x%x) \n
%s::%s: requesting coredump failed (ret=0x%x) \n
Crashlog.CTRL.bin
%s::%s: bad max size \n
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu \n
%s::%s: memory allocation crashlog reason string failed \n
ClientPrepareForReset
Start_Impl_block_invoke_2
Yes
%s::%s: failed to set ptm status in subsystem properties (ret = 0x%x) \n
bootTimestampKey
%s::%s: powerFlags: %u \n
%s::%s: working copy content: 0x%x len: %llu \n
MSI-2
%s::%s: msiaddr::%llx \n
%s::%s: release PM assertion \n
%s::%s: failed to alloc dict \n
ivars->clientName
EnqueueDeferredWork(blockCopy, kCentauriDeferredWorkTypeOther)
%s::%s: device control reg val: 0x%x \n
%s::%s: logpipe: failed to copy directory name %s \n
ivars->crashlogHandler
%s::%s: failed to create user class dict \n
RegisterServiceOrStartDextRecovery_block_invoke
errorData->isWrite < 2
%s::%s: replacing existing client \n
memSwapMapT0: %s\n
%s::%s: failed to allocate OSData \n
%s::%s: invalid memswap DMA command \n
%s::%s: failed to get MSI data (ret = 0x%x) \n
length < sizeof(configName)
RD
handler
dict && dict->setObject(kCentauriPropertyBootComplete, kOSBooleanTrue)
time          offset     r/w data\n
%s::%s: initialized MSI-1 \n
%s::%s: failed to create IODMACommand (ret = 0x%x) \n
%s::%s: power assertion already held \n
%s::%s: failed to copy reset block \n
flrCountDict->setObject(kCentauriFLRCount, flrCountObject)
collect-logs
eventNameObject
PrepareChipForResetDuration
coredumpEnd
Boot
%s::%s: failed to set dext relaunch property (ret = 0x%x) \n
%s::%s: Close ret = 0x%x \n
%s::%s: termination notification for CentauriRemoteInterface \n
ChipResetCallback_Impl
%s::%s: FLR count: %u \n
%s::%s: failed to get logging properties dict \n
%s::%s: failed to create data log stream \n
InduceFaultCb
Stop_Impl
%s::%s: invalid input dictionary - bailing out \n
%s::%s: client already registered (%s) \n
CollectLogsFatal_block_invoke
%06llu.%06llu CollectLogs Start 0x%04x %s\n
RealTimestamp
PartiallyBootedLPM
OSAction_CentauriSubsystem_MemSwapCallback
%s::%s: invalid metadata dict \n
%s::%s: failed to remove property (ret = 0x%x) \n
%06llu.%06llu CollectDiagnostics Complete %s %s ret: 0x%03x\n
%s::%s: invalid number of MSIs requested: %u \n
Crashlog.WFMAIN.bin
Stop
%s::%s: failed to EnablePCIPowerManagement (ret = 0x%x) \n
RequireClient
ready for reset
    coredumpPending: %d\n
RestoreDeviceState
super::SetErrorHandler(handler) == kIOReturnSuccess
%s::%s: failed to save timestamp \n
%s::%s: invalid length (working copy %llu t0 %llu) \n
%s::%s: reset already enqueued \n
CreateMetadataDict
CollectEventLog
readyForReset
crashlogStart
dict && dict->setObject(kCentauriPropertyUnexpectedDextTermination, (ivars->dextRelaunchReason == kCentauriManagerDextRelaunchReasonCrash) ? kOSBooleanTrue : kOSBooleanFalse)
v24@?0^{AirshipDriverDK=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})(?=^{AirshipDriverDK_IVars}^{AirshipDriverDK_LocalIVars})}8r^{OSString=^^?Aii^{OSMetaClass}^^?(?=^{OSObje
CheckErrorPolicyForKey
%s::%s: in low power \n
%s::%s: failed to copy collectLogs block \n
time          flags\n
MemSwapWorkingCopy.bin
%s::%s: invalid segment info (addr: 0x%qx len: 0x%qx) \n
%s::%s: failed to copy system state service (ret = 0x%x) \n
%s::%s: failed to trigger fault report (ret = 0x%x) \n
ivars->logCollectionInfo.type == kCentauriLogCollectionFatal
CentauriPowerStateLog.txt
%s::%s: driver %s - ignoring MSI notification \n
super::SetPropertyUpdateNotificationHandler(handler) == kIOReturnSuccess
CompletionCallback_Impl
%s::%s: remote interface unavailable \n
%06llu.%06llu CollectDiagnostics Start %s %s\n
%s::%s: failed to get log id \n
%s::%s: failed to copy block \n
nonfatal
%s::%s: failed to create msi interrupt source (ret = 0x%x) \n
SetResetTimestamp
GetNumMSIVectorsFromEndpoint
%s::%s: Invalid segmentName or segmentDump observed \n
%s::%s: logger not ready \n
%s::%s: ready for reset timed out \n
CentauriChipInfo.txt
offline
%s::%s: failed to get dir name \n
%s::%s: invalid viddid \n
%s::%s: failed to create timer action (ret = 0x%x) \n
B16@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8
%s::%s: driver offline (state = %u) \n
CollectLogs
not null
%s::%s: bad arguments \n
InitWithProviderAndOptions
DriverLogs
%s::%s: bad args \n
CreateChipObject
%s::%s: failed to copy service name (ret = 0x%x) \n
%s::%s: error source %u code %u arg %llu \n
%s::%s: unexpected coredump completion \n
%s::%s: log collection failed (ret=0x%x) \n
%s::%s: failed to allocate metadata dict \n
%s::%s: error appending bytes to bufferObject \n
com.apple.queue.centauri-corecapture
IOService
SetPowerOverride(true) == kIOReturnSuccess
ivars->state == kCentauriStateLogCollection
%s::%s: failed to create working copy IOBMD (ret = 0x%x) \n
ResetCompletion
%s::%s: failed to set SS ID object \n
CollectMSILog
TriggerClientLaunch() == kIOReturnSuccess
%s::%s: lpw -> on \n
%s::%s: failed to alloc OSNumber for up time \n
true
%s::%s: failed to prepare for DMA (ret = 0x%x) \n
CompleteFaultReportCb
%s::%s: ret = 0x%x \n
derivedStart
ReadMSIAddr
prepareForResetEnd
%s::%s: super init failed \n
%s::%s: Invalid coreName or crashlogData observed \n
SetPropertyUpdateNotificationHandler_block_invoke
i40@?0^^{OSDictionary}8^^{OSDictionary}16^^{OSDictionary}24^^{OSString}32
com.apple.queue.centauri-pcierrors
ivars->timerAction
%s::%s: invalid state for log collection %u \n
airshipService: %s\n
%s::%s: cached crashlogs not available \n
%s::%s: number of crashlogs: %u \n
SaveDeviceState
ReportError
%s::%s: invalid crash log buffer \n
PTM
Coredump
centauri-ccloglevel
    resetFailed: %d\n
Unknown
%s::%s: boot stage = %s
%s::%s: ready for reset timed out
%s::%s: boot stage: %s, fw state: %s
%s::%s: failed to alloc dict
%s::%s: no ptm key - bailing out
%s::%s: failed to create logger queue (ret = 0x%x)
%s::%s: failed to copy system state service (ret = 0x%x)
%s::%s: bad arg
%s::%s: airship reported error: 0x%x
%s::%s: failed to copy service name (ret = 0x%x)
%s::%s: invalid input dictionary - bailing out
%s::%s: failed to create reset state item (ret=0x%x)
%s::%s: invalid state for reset %u
%s::%s: failed to get IOPCIDevice
%s::%s: in low power
%s::%s: working copy content: 0x%x len: %llu
%s::%s: failed to create reason string copy
%s::%s: failed to set dict object for StateDump
%s::%s: caching crashlog
%s::%s: in fatal error state (%u)
%s::%s: airship not up; returning %s
%s::%s: AppleCentauriManager::Open failed (ret = 0x%x)
%s::%s: pmcsr 0x%04x
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x
%s::%s: errorCode %u, reason %s
%s::%s: failed to get provider queue
%s::%s: failed to create dict
%s::%s: first power on
%s::%s: remote interface error (ret = 0x%x)
%s::%s: clearing cfg mbx at offset 0x%x
%s::%s: sleeping for %u ms...
%s::%s: device id: 0x%x
%s::%s: ptm enabled, clock granularity: %u ns
%s::%s: section too small
%s::%s: invalid metadata dict
%s::%s: release PM assertion
%s::%s: invalid viddid 0x%x
%s::%s: failed to set properties (ret = 0x%x)
%s::%s: FLR limit (%u) reached
%s::%s: logger not available
%s::%s: failed to copy provider properties
%s::%s: Crashlog Reason: \"%s\"
%s::%s: centauri-driverkit=0
%s::%s: number of MSIs requested: %u (SingleMSI mode)
%s::%s: Driver offline. Ignoring state change %u
%s::%s: failed to set up time object
%s::%s: failed to allocate statedump buffer
%s::%s: failed to create osdata object
%s::%s: %s
%s::%s: pci device not open
%s::%s: driver offline - ignoring exec stage notification
%s::%s: failed to save FLR timestamps
%s::%s: power assertion already held
%s::%s: LPM log collection mode unsupported
%s::%s: reserved MSIs via provider
%s::%s: invalid number of MSIs configured: %u
%s::%s: invalid crash log buffer
%s::%s: crashlog header reports empty: %zu bytes
%s::%s: failed to enable timer (ret = 0x%x)
%s::%s: failed to create memswap os action (ret = 0x%x)
%s::%s: deferring due to low power
%s::%s: failed to create msi interrupt source (ret = 0x%x)
%s::%s: crashlog too small: %zu bytes
%s::%s: failed to get owner object
%s::%s: termination notification for CentauriRemoteInterface
%s::%s: returned from SetProperties (ret = 0x%x)
%s::%s: failed to find aer capability (ret = 0x%x)
%s::%s: current timestamp is older than last reset timestamp, ignoring
%s::%s: super init failed
%s::%s: skipping %s
%s::%s: no crashlog handler
%s::%s: didDextRelaunch = %s (reason %u)
%s::%s: PCI dart error %u: [%s] addressLo: 0x%x addressHi: 0x%x
%s::%s: failed to create function name copy
%s::%s: requesting coredump failed (ret=0x%x)
%s::%s: cached crashlogs not available
%s::%s: failed to get log id
%s::%s: added file %s, size %zu
%s::%s: warning: prepare for reset handler is not registered
%s::%s: failed to open IOPCIDevice (ret = 0x%x)
%s::%s: invalid notifier
%s::%s: termination notification for AirshipDriverDK
%s::%s: error source %u code %u arg %llu
%s::%s: deferring reset
%s::%s: buffer filled, totalBytesPrinted: %u bufferSize: %u
%s::%s: failed to update the FW crash reason string
%s::%s: no prepare for reset handler
%s::%s: not permitted for ss id %u
%s::%s: failed to create working copy IOBMD (ret = 0x%x)
%s::%s: crash poll iterations = %u
%s::%s: failed to alloc OSNumber for up time
%s::%s: failed to trigger fault report (ret = 0x%x)
%s::%s: invalid segment info (addr: 0x%qx len: 0x%qx)
%s::%s: selector %llu
%s::%s: failed to create reset timestamps dict
%s::%s: not permitted
%s::%s: log collection in progress/enqueued
%s::%s: failed to allocate OSData
%s::%s: ptm requester role not supported
%s::%s: failed to create os action for watchdog notification (ret = 0x%x)
%s::%s: log collection already enqueued
%s::%s: failed to get logging properties object
%s::%s: ret = 0x%x
%s::%s: provider not available
%s::%s: reset in progress. ignoring error
%s::%s: error source not found for %s
%s::%s: unexpected coredump completion
%s::%s: failed to set dict object
%s::%s: failed to create osdata object for StateDump
%s::%s: signature mismatch
%s::%s: failed to copy completionCb block
%s::%s: failed to create dispatch src (ret = 0x%x)
%s::%s: deferred work is canceled
%s::%s: failed to create osdata object for %s
%s::%s: failed to prepare for DMA (ret = 0x%x)
%s::%s: failed to create data log stream
%s::%s: chip class not initialized
%s::%s: testID: %u
%s::%s: failed to alloc OSNumber for monotonic time
%s::%s: failed to copy collectLogs block
%s::%s: FLR timeout override: %u ms
%s::%s: driver %s - ignoring MSI notification
%s::%s: error reported by %s error code %u
%s::%s: using cc log level %u
%s::%s: logpipe: failed to copy directory name %s
%s::%s: failed to create airship transport
%s::%s: failed to get platform (ret = 0x%x)
%s::%s: timer expired waiting for remote service in dext crash recovery state
%s::%s: crashlog size larger than buffer (%zu > %zu)
%s::%s: datapipe: failed to copy directory name %s
%s::%s: failed to EnablePCIPowerManagement (ret = 0x%x)
%s::%s: error handler already exists
%s::%s: completion
%s::%s: failed to set monotonic time object
%s::%s: fw crash reason string is not supported with non-fatal log collection
%s::%s: failed to copy properties
%s::%s: invalid link control value
%s::%s: Close ret = 0x%x
%s::%s: invalid state (%s)
%s::%s: failed to create user client (ret = 0x%x)
%s::%s: handler already exists
%s::%s: number of MSIs requested: %u
%s::%s: Crashlog Reason not found from the Crashlog data
%s::%s: failed to create chip reset os action (ret = 0x%x)
%s::%s: error handler not registered
%s::%s: powerFlags: %s
%s::%s: FLR count: %u
%s::%s: failed to set reason object
%s::%s: invalid parameters
%s::%s: state = %u
%s::%s: log collection failed (ret=0x%x)
%s::%s: bad args
%s::%s: memswap memory map is already set
%s::%s: failed to find PCI capability (ret = 0x%x)
%s::%s: crash log buffer too small: %zu bytes
%s::%s: failed to copy immediateCb block
%s::%s: deliver notification error (ret = 0x%x)
%s::%s: failed to  SearchProperty (ret = 0x%x)
%s::%s: failed to remove property (ret = 0x%x)
%s::%s: dispatching cached errors
%s::%s: unexpected crash log completion
%s::%s: failed to copy block
%s::%s: pci read invalid data
%s::%s: ASPM state: %u
%s::%s: failed to get MSI addr (ret = 0x%x)
%s::%s: %u
%s::%s: failed to alloc OSNumber for SS ID
%s::%s: deferring (state = 0x%x)
%s::%s: bad size (got %u max %u)
%s::%s: device control reg val: 0x%x
%s::%s: failed to find MSI property
%s::%s: driver offline (state = %u)
%s::%s: invalid length
%s::%s: stream: failed to copy log identifier %s
%s::%s: failed to set dict object for %s
%s::%s: 
%s::%s: driver offline
%s::%s: failed to get default queue (ret = 0x%x)
%s::%s: service matching set up for %s
%s::%s: chip crash timed out
%s::%s: failed to find ptm capability (ret = 0x%x)
%s::%s: Logging prop: owner: %s dir: %s file: %s id: %s
%s::%s: Invalid coreName or crashlogData observed
%s::%s: GetBusyState ret = 0x%x
%s::%s: failed to create os action (ret = 0x%x)
%s::%s: offline
%s::%s: invalid client
%s::%s: invalid cmd id: %u
%s::%s: failed to set real time object
%s::%s: failed to create fault reporter
%s::%s: failed to get logger
%s::%s: failed to SaveDeviceState (ret = 0x%x)
%s::%s: errorSource: %u, errorCode: %u, arg: 0x%llx
%s::%s: timer expired waiting for memswap info in dext crash recovery state
%s::%s: error arg not an OSNumber
%s::%s: failed to alloc OSNumber for real time
%s::%s: memory allocation crashlog reason string failed
%s::%s: failed to get logging properties dict
%s::%s: coredump/crashlog completion failed (ret=0x%x)
%s::%s: invalid state for watchdog notification: %u
%s::%s: options 0x%x reason %s
%s::%s: Transaction pending poll timed out. Proceeding to FLR
%s::%s: failed to get provider
%s::%s: new exec stage: %u
%s::%s: block copy failed
%s::%s: error handler has been deregistered
%s::%s: resuming reset (state = 0x%x)
%s::%s: failed to RestoreDeviceState (ret = 0x%x)
%s::%s: failed to report error (ret = 0x%x)
%s::%s: unexpected match notification
%s::%s: Stop ret = 0x%x
%s::%s: invalid driver state %u for dext crash recovery state %u
%s::%s: reset failed (ret = 0x%x)
%s::%s: failed to create log pipe with provider %s
%s::%s: failed to create error event action ret = 0x%x
%s::%s: failed to set os action handler (ret = 0x%x)
%s::%s: match notification for AirshipDriverDK
%s::%s: SetProperties failed
%s::%s: invalid bootstage 0x%x
%s::%s: cmd id %u ret 0x%x
%s::%s: invalid state (%u)
%s::%s: requesting crashlog failed (ret=0x%x)
%s::%s: failed to configure interrupts (ret = 0x%x)
%s::%s: failed to create timer action (ret = 0x%x)
%s::%s: service notification (type: %llu)
%s::%s: replacing existing client
%s::%s: invalid memswap map or working copy desc
%s::%s: poll count %u
%s::%s: msiaddr::%llx
%s::%s: data::%x
%s::%s: airship service not ready
%s::%s: remote interface unavailable
%s::%s: failed to create file name copy
%s::%s: log collection failed (ret = 0x%x)
%s::%s: resuming fatal log collection (state = 0x%x)
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu
%s::%s: failed to get log file name
%s::%s: invalid viddid
%s::%s: escalate FLR failure
%s::%s: full chip reset in progress
%s::%s: invalid state for log collection %u
%s::%s: failed to create IODMACommand (ret = 0x%x)
%s::%s: empty crash log buffer
%s::%s: invalid filename/statedump
%s::%s: bad arguments
%s::%s: failed to allocate pending work item
%s::%s: MSICapOffset::%llx
%s::%s: using console log level %u
%s::%s: driver offline - ignoring airship error notification
%s::%s: failed to set require client property (ret = 0x%x)
%s::%s: dispatching propertyUpdateNotification
%s::%s: number of crashlogs: %u
%s::%s: failed to serialize
%s::%s: failed to copy prepareCb block
%s::%s: failed to create log stream
%s::%s: prepare for reset handler is not registered
%s::%s: failed to allocate inFlightLock
%s::%s: FLR limit override boot-arg is set
%s::%s: propertyUpdateNotification handler not registered
%s::%s: initialized MSI-1
%s::%s: crashlog handler is not registered
%s::%s: lpw -> on
%s::%s: ErrorDetected's value type is not a dictionary
%s::%s: invalid number of MSIs requested: %u available: %u
%s::%s: failed to set ptm status in subsystem properties (ret = 0x%x)
%s::%s: failed to create os action for collect logs (ret = 0x%x)
%s::%s: client: %s
%s::%s: invalid queue
%s::%s: unexpected termination notification
%s::%s: failed to create completion os action (ret = 0x%x)
%s::%s: failed to set enable int source (ret = 0x%x)
%s::%s: logpipe: failed to copy file name %s
%s::%s: invalid length (working copy %llu t0 %llu)
%s::%s: memswap memory is already DART mapped
%s::%s: invalid memswap DMA command
%s::%s: failed to create pci error queue (ret = 0x%x)
%s::%s: failed to get MSI data (ret = 0x%x)
%s::%s: match notification for CentauriRemoteInterface
%s::%s: requesting full wake
%s::%s: %s property exists - skipping dext crash
%s::%s: failed to set dext relaunch property (ret = 0x%x)
%s::%s: failed to alloc metadata
%s::%s: error filling buffer, bytesPrinted: %d kLineLength: %u
%s::%s: failed to create data log pipe
%s::%s: failed to create timer src (ret = 0x%x)
%s::%s: invalid number of MSIs requested: %u
%s::%s: remote service unavailable. wait for %u ms
%s::%s: error appending bytes to bufferObject
%s::%s: failed to create memory map (ret = 0x%x)
%s::%s: failed to set SS ID object
%s::%s: failed to allocate metadata dict
%s::%s: failed to copy deferredCb block
%s::%s: failed to set airship driver config
%s::%s: failed to create chip object for family %u
%s::%s: boot stage = ready for reset
%s::%s: Invalid segmentName or segmentDump observed
%s::%s: failed to create user class dict
%s::%s: invalid segment count %u
%s::%s: error code not found
%s::%s: failed to copy completion block
%s::%s: failed to copy reset block
%s::%s: state %u
%s::%s: found crashlog data for %s
%s::%s: failed to get dir name
%s::%s: failed super Start (ret = 0x%x)
%s::%s: driver offline - ignoring airship fatal error notification
%s::%s: reset already enqueued
%s::%s: failed to allocate memory
%s::%s: skipping during dext crash recovery
%s::%s: client already registered (%s)
%s::%s: bad max size
%s::%s: FLR timed out
%s::%s: module name not found
%s::%s: failed to get addr range (ret = 0x%x)
%s::%s: Using FLR limit: %u
%s::%s: failed to schedule immediate wake
%s::%s: failed to find msi capability (ret = 0x%x)
%s::%s: invalid callback parameters
%s::%s: powerFlags: %u
%s::%s: timer expired waiting for remote service in reset failed state
%s::%s: finalize %d
%s::%s: airship reported fatal error: %s
%s::%s: PCI dart error
%s::%s: failed to create osdict
%s::%s: cachedErrorCount: %u
%s::%s: failed to validate segment length (ret = 0x%x expected %llu got %llu)
%s::%s: failed to save timestamp
%s::%s: function reset already in progress
%s::%s: tp poll count %u
%s::%s: MSI handler: boot stage = %u
%s::%s: failed to send %s (ret=0x%x)
%s::%s: fault reporter is busy
%s::%s: logger not ready
%s::%s: failed to get airship probe result
%s::%s: Open error (ret = 0x%x)
%s::%s: failed to get user client service
%s::%s: requesting deferral (low power: %u, defer for memswap: %s)
%s::%s: invalid fault reporter
%s::%s: failed to allocate lock
%s::%s: ignoring based on boot-arg
%s::%s: failed to alloc OSString
%s::%s: ret: 0x%x flags: 0x%qx cnt: %d addr: 0x%qx len: 0x%qx
%s::%s: invalid crashlog data
%s::%s: logpipe: failed to copy log identifier %s
%s::%s: failed to get the fault reporter additional owner
%s::%s: failed HasPCIPowerManagement (ret = 0x%x)
%s::%s: failed to set boot complete property (ret = 0x%x)
```
