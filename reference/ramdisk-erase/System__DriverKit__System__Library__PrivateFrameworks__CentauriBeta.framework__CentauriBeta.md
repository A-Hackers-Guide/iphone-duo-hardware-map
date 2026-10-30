# `/System/DriverKit/System/Library/PrivateFrameworks/CentauriBeta.framework/CentauriBeta`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 450,880 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 2496)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/System/DriverKit/System/Library/PrivateFrameworks/CentauriBeta.framework/CentauriBeta (compatibility version 1.0.0, current version 1.0.0)`
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

## Strings (1,116)

```
bootStageOSBeta
%s::%s: super init failed \n
(null)
FLRDuration
%s::%s: failed to allocate lock \n
handler
%s::%s: invalid crashlog data \n
timeElapsedObject != nullptr
OSAction_CentauriSubsystem_ServiceNotificationReady
%s::%s: failed to copy deferredCb block \n
%s::%s: SetProperties failed \n
%s::%s: returned from SetProperties (ret = 0x%x) \n
dict->setObject(kCentauriSystemStateNotificationResetKey, kOSBooleanTrue)
SetErrorHandler_block_invoke
DeferReset
CollectMemoryLog
force panic on fatal error for ss %u (type %u)
MemSwapWorkingCopy.bin
%s::%s: state %u \n
%s::%s: failed to find msi capability (ret = 0x%x) \n
derivedStart
Reset
%s::%s: chip crash timed out \n
%s::%s: cached crashlogs not available \n
ClearConfigSpaceMailboxes
%s::%s: driver %s - ignoring MSI notification \n
centauri-flr-limit
CollectStateSnapshots
CancelDeferredWork
%s::%s: hint: %u \n
%s::%s: failed to create timer action (ret = 0x%x) \n
ChangePowerState(kIOServicePowerCapabilityOn) == kIOReturnSuccess
ExitLPW
CancelPropertyUpdateNotificationHandler
%s::%s: invalid state for watchdog notification: %u \n
ResetCompletion
%s::%s: resuming fatal log collection (state = 0x%x) \n
%s::%s: invalid bootstage 0x%x \n
    updateFWReasonString: %d\n
SaveDeviceState
MaskUnsupportedRequestAER
SetResetTimestamp
%s::%s: ptm requester role not supported \n
OSAction_CentauriSubsystem_CentauriManagerErrorHandler
TriggerClientLaunch() == kIOReturnSuccess
%s::%s: powerFlags: %u \n
%s::%s: not permitted \n
key && dict
%s::%s: failed to create IODMACommand (ret = 0x%x) \n
IsBackToBack
Off
derivedProbeDevice
%s::%s: ret = 0x%x \n
CollectLogs
%s::%s: failed to create dispatch src (ret = 0x%x) \n
dextRecoveryState: %s\n
%s::%s: MSI handler: boot stage = %u \n
fwCrashReported
%s::%s: failed to get default queue (ret = 0x%x) \n
-
%s::%s: error handler already exists \n
%s::%s: requesting deferral (low power: %u, defer for memswap: %s) \n
%s::%s: failed to create function name copy \n
CentauriMemoryAccessLog.txt
%s::%s: FLR timed out \n
CoredumpDuration
%s::%s: no ptm key - bailing out \n
 r 
%s::%s: in fatal error state (%u) \n
val && ivars->resetTimestamps->setObject(eventName, val)
SetPowerState_Impl
%s::%s: testID: %u \n
%s::%s: failed to alloc OSNumber for real time \n
inLowPower: %d\n
copy
%s::%s: log collection failed (ret = 0x%x) \n
%s::%s: resuming reset (state = 0x%x) \n
bootTimestampKey
false
test
WatchdogCallback_Impl
CollectLogsFatal_block_invoke
nonfatal
%s::%s: current timestamp is older than last reset timestamp, ignoring \n
ErrorArg
%s::%s: failed to copy properties \n
com.apple.queue.centauri-pcierrors
v32@?0Q8^{IOService=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})}16Q24
/Library/Caches/com.apple.xbs/558FE645-4E39-4399-A06E-8DC20AC536F1/TemporaryDirectory.VSeWMb/Sources/AppleCentauri_driverkit/CentauriSubsystem/CentauriSubsystem.cpp
%s::%s: remote interface error (ret = 0x%x) \n
address && length && coredump
ExternalMethod
SACFunctionAvailable
SetErrorHandler
%s::%s: unexpected crash log completion \n
%s::%s: failed to set SS ID object \n
%06llu.%06llu SaveDeviceState ret: 0x%03x\n
subsystemNameObject
    resetHint: %u\n
%s::%s: failed to create timer src (ret = 0x%x) \n
report-error
%s::%s: error arg not an OSNumber \n
%s::%s: log collection in progress/enqueued \n
%s::%s: ASPM state: %u \n
%s::%s: failed super Start (ret = 0x%x) \n
SetResetHint
SetState
%s::%s: failed to create memory map (ret = 0x%x) \n
%06llu.%06llu Reset Complete ret: 0x%03x\n
0x%04llu %06llu.%06llu - %06llu.%06llu - %06llu.%06llu %s\n
Default
%s::%s: unexpected termination notification \n
%s::%s: error reported by %s error code %u \n
%s::%s: ready for reset timed out \n
collect-logs
%s::%s: invalid state (%u) \n
ROM
v24@?0I8I12^v16
%s::%s: deliver notification error (ret = 0x%x) \n
pci-dart-error-data
errorData->isWrite < 2
%s::%s: log collection failed (ret=0x%x) \n
GetCachedErrorCount
%s::%s: invalid memswap DMA command \n
%s::%s: msiaddr::%llx \n
centauri-consoleloglevel
%s::%s: logpipe: failed to copy directory name %s \n
AppleCentauriManager::SaveClientProperty(this, key, newValue, autoClearConditions) == kIOReturnSuccess
SetIPCProperties
AirshipDriverConfigName
CentauriManagerErrorHandler_Impl
serializedBuffer && serializedLength
%s::%s: reset failed (ret = 0x%x) \n
N/A
%s::%s: failed to  SearchProperty (ret = 0x%x) \n
 w 
%s::%s: ret: 0x%x flags: 0x%qx cnt: %d addr: 0x%qx len: 0x%qx \n
%s::%s: MSICapOffset::%llx \n
%s::%s: crash log buffer too small: %zu bytes \n
GetASPMState
LPMOS
DextRelaunchState
%s::%s: invalid number of MSIs requested: %u available: %u \n
%s::%s: requesting full wake \n
ctx
!ivars->inLowPower
CollectMSILog
%s::%s: failed to create msi interrupt source (ret = 0x%x) \n
%s::%s: failed to find PCI capability (ret = 0x%x) \n
%s::%s: failed to set reason object \n
%s::%s: deferring (state = 0x%x) \n
CollectConfigLogs
EnqueueDeferredWork
%s::%s: crashlog header reports empty: %zu bytes \n
Subsystem
BootComplete
MonotonicTimestamp
%s::%s: AppleCentauriManager::Open failed (ret = 0x%x) \n
%s::%s: memswap memory is already DART mapped \n
[NonFatal]
%s::%s: skipping %s \n
TriggerPanic
%s::%s: PCI dart error \n
WR
InitMemSwapWorkingCopy
%s::%s: boot stage = %s \n
%06llu.%06llu CollectDiagnostics Complete %s %s ret: 0x%03x\n
MSI-2
abort handler
%s::%s: failed to EnablePCIPowerManagement (ret = 0x%x) \n
GetBootStageMirror
dict->setObject(key, kOSBooleanTrue)
%s::%s: error source %u code %u arg %llu \n
ivars->systemStateResetItemDict->setObject(kCentauriSystemStateNotificationResetKey, inReset ? kOSBooleanTrue : kOSBooleanFalse)
%s::%s: dispatching cached errors \n
    coredumpPending: %d\n
%s::%s: errorCode %u, reason %s \n
%s::%s: failed to create dict \n
Reason
init
i40@?0^^{OSDictionary}8^^{OSDictionary}16^^{OSDictionary}24^^{OSString}32
%s::%s: failed to set os action handler (ret = 0x%x) \n
%s::%s: cmd id %u ret 0x%x \n
WatchdogCallback_Impl_block_invoke
%s::%s: fw crash reason string is not supported with non-fatal log collection \n
%s::%s: failed to set dict object \n
    type: %s\n
free
%s::%s: failed to create user class dict \n
%s::%s: match notification for CentauriRemoteInterface \n
%s::%s: failed to set ptm status in subsystem properties (ret = 0x%x) \n
CollectLogsCallback_Impl_block_invoke
ready for reset
%s::%s: state: 0x%x \n
%s::%s: failed to RestoreDeviceState (ret = 0x%x) \n
%s::%s: failed to set real time object \n
Start_Impl_block_invoke_2
CentauriBeta:\n
CollectDeferredFaultDataCb
%s::%s: failed to update the FW crash reason string \n
%s::%s: invalid link control value \n
%s::%s: using console log level %u \n
RegisterServiceOrStartDextRecovery_block_invoke
name
CancelErrorHandler
CacheCrashlogs
ExecuteDeferredWork
%s::%s: found crashlog data for %s \n
dextRelaunchObj != nullptr
%s::%s: finalize %d \n
success
%s::%s: error source not found for %s \n
%s::%s: invalid viddid 0x%x \n
%s::%s: failed to create reason string copy \n
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu \n
LPMBoot
%s::%s: failed to save FLR timestamps \n
%s::%s: errorSource: %u, errorCode: %u, arg: 0x%llx \n
%s::%s: function reset already in progress \n
completionCopy
ivars->logCollectionInfo.metadata
%s::%s: requesting crashlog failed (ret=0x%x) \n
%s::%s: bad arguments \n
GetNumMSIVectorsRequested
CreateMetadataDict
flrCountDict
CentauriConfigAccessLog.txt
null
RealTimestamp
OSAction_CentauriSubsystem_WatchdogCallback
sacObj != nullptr
%s::%s: failed to set boot complete property (ret = 0x%x) \n
ivars->logCollectionInfo.completion
crashlogEnd
Coredump
PartiallyBootedLPM
%s::%s: logpipe: failed to copy file name %s \n
DoReset
!ivars->logCollectionInfo.metadata && !ivars->logCollectionInfo.completion
%06llu.%06llu %s 0x%08x 0x%08x\n
data
SetDextRecoveryState
msi-reservation-size
%s::%s: Logging prop: owner: %s dir: %s file: %s id: %s \n
%s::%s: Stop ret = 0x%x \n
%s::%s: %u \n
DartMapMemSwapWorkingCopy
%s::%s: deferring reset \n
CollectEventLog
%s::%s: failed to validate segment length (ret = 0x%x expected %llu got %llu) \n
offline
kCentauriBetaFLRCount
RD
%s::%s: remote interface unavailable \n
dict && dict->setObject(\"RequireClient\", kOSBooleanTrue)
version: %s\n
%s::%s: poll count %u \n
prepareForResetEnd
Crashlog
FetchMemSwap
%s::%s: driver offline - ignoring exec stage notification \n
%s::%s: termination notification for CentauriRemoteInterface \n
ivars->timerSource
%s::%s: failed to remove property (ret = 0x%x) \n
%s::%s: LPM log collection mode unsupported \n
t2026
v12@?0i8
%s::%s: failed to get log file name \n
%s::%s: invalid notifier \n
CompletionCallback_Impl
%s::%s: failed to copy reset block \n
%06llu.%06llu CollectLogs Start 0x%04x %s\n
%s::%s: Transaction pending poll timed out. Proceeding to FLR \n
CentauriControlRemoteInterface
%s::%s: failed to create data log stream \n
RequireClient
errorDataObj != nullptr
%s::%s: failed to serialize \n
OpenRemoteService
%s::%s: failed to create memswap os action (ret = 0x%x) \n
key
CentauriEventLog.txt
%s::%s: pci read invalid data \n
%s::%s: Crashlog Reason: \"%s\" \n
PrepareChipForResetDuration
OSAction_CentauriSubsystem_InterruptOccurred
flrCount && *flrCount
remoteService: %s\n
%s::%s: FLR timeout override: %u ms \n
AbortHandler
%s::%s: provider not available \n
%s::%s: failed to get owner object \n
%s::%s: failed to configure interrupts (ret = 0x%x) \n
CollectLogsCallback_Impl
%s::%s: sleeping for %u ms... \n
%s::%s: centauri-driverkit=0 \n
i8@?0
%s::%s: unexpected match notification \n
%s::%s: termination notification for AirshipDriverDK \n
CreateSystemStateNotificationItems
%s::%s: handler already exists \n
%s::%s: boot stage = ready for reset \n
%s::%s: airship not up; returning %s \n
CompleteFaultReportCb
%s::%s: failed to trigger fault report (ret = 0x%x) \n
ReadyForReset
CollectImmediateFaultDataCb
%s::%s: number of MSIs requested: %u (SingleMSI mode) \n
%s::%s: bad arg \n
CreateChipObject
errorInfo
%s::%s: invalid cmd id: %u \n
GetFirmwareState
%s::%s: %s \n
%s::%s: failed to create airship transport \n
%s::%s: failed to create data log pipe \n
%s::%s: failed to create os action for watchdog notification (ret = 0x%x) \n
newValue
%s::%s: invalid client \n
fatal
%s::%s: failed to create os action for collect logs (ret = 0x%x) \n
centauri-recovery
%s::%s: error handler has been deregistered \n
%s::%s: replacing existing client \n
CollectLogsCompletion
%s::%s: invalid driver state %u for dext crash recovery state %u \n
%s::%s: Crashlog Reason not found from the Crashlog data \n
%s::%s: failed to create fault reporter \n
ScheduleImmediateWake
%s::%s: failed to alloc OSNumber for SS ID \n
%s::%s: failed to set up time object \n
CollectPowerStateLog
logCollectionInfo:\n
CollectChipInfo
%s::%s: device control reg val: 0x%x \n
InitWithProviderAndOptions
%s::%s: failed to create user client (ret = 0x%x) \n
%s::%s: failed to copy completion block \n
ResetDone
SetDextRecoveryState_block_invoke
CrashlogDuration
Crashed
durationObject != nullptr
centauri-driverkit
%s::%s: airship reported fatal error: %s \n
ivars->inFlightWork < UINT32_MAX
ret == kIOReturnSuccess || ret == kIOReturnNotFound
blockCopy
%s::%s: failed to get addr range (ret = 0x%x) \n
%s::%s: failed to create osdata object for %s \n
v20@?0^{AirshipDriverDK=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})(?=^{AirshipDriverDK_IVars}^{AirshipDriverDK_LocalIVars})}8I16
ExecStageChanged
%s::%s: offline \n
    crashlogPending: %d\n
%s::%s: empty crash log buffer \n
dict && dict->setObject(kCentauriPropertyPTMEnabledOnEndpoint, ptmStatus)
%s::%s: failed to alloc OSNumber for monotonic time \n
prevState == kCentauriDextRecoveryStateCollectLogs
%s::%s: invalid segment count %u \n
%s::%s: invalid length \n
No
%s::%s: skipping during dext crash recovery \n
userClient
com.apple.ConnectivityDriver.TimeSinceLastFLR
%s::%s: failed to copy immediateCb block \n
%s::%s: deferred work is canceled \n
!ivars->deferredWork.logCollection
%s::%s: failed to prepare for DMA (ret = 0x%x) \n
dataObject->getLength() == sizeof(uint32_t)
%s::%s: reset in progress. ignoring error \n
PrepareChipForReset
%s::%s: coredump/crashlog completion failed (ret=0x%x) \n
ClearUnsupportedRequestAER
InduceFaultCb
ServiceNotificationReady_Impl_block_invoke
%s::%s: invalid state (%s) \n
%s::%s: in low power \n
%s::%s: invalid state for log collection %u \n
in low power
coredumpEnd
%s::%s: failed to create chip object for family %u \n
CentauriDebug
PreBoot
%s::%s: failed to get platform (ret = 0x%x) \n
%s::%s: failed to create file name copy \n
%s::%s: invalid number of MSIs requested: %u \n
InReset
%s::%s: failed to get airship probe result \n
com.apple.centauri.reset.bluetooth
TimerOccurred_Impl
chipId: %s\n
ReportError
%s::%s: powerFlags: %s \n
length < sizeof(fullReason)
CentauriUserClientProperties
%s::%s: failed to allocate OSData \n
UnexpectedDextTermination-UserspaceReboot
OSAction_CentauriSubsystem_CollectLogsCallback
resetInfo:\n
NumMSIs
ExtractCrashlogReason
isASPMEnabled
coredumpStart
%s::%s: failed to get provider queue \n
ClientClose
PrepareForReset
completion
%s::%s: boot stage: %s, fw state: %s \n
%s::%s: failed to send %s (ret=0x%x) \n
Crashlog.BTMAIN.bin
%s::%s: selector %llu \n
%s::%s: logpipe: failed to copy log identifier %s \n
B24@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}16
centauri-fatal-err-panic
%s::%s: failed to create os action (ret = 0x%x) \n
action == ivars->timerAction
pci-get-dart-error
ivars->cachedCrashlogsArray
%s::%s: error code not found \n
airshipService: %s\n
ivars->cachedCrashlogsArray->setObject(copy)
ConfigureEndpointForMemSwap
%s::%s: failed to copy provider properties \n
fatalLogCollectionTriggered
AdditionalPipeOwners
dict && dict->setObject(kCentauriPropertyUnexpectedDextTermination, (ivars->dextRelaunchReason == kCentauriManagerDextRelaunchReasonCrash) ? kOSBooleanTrue : kOSBooleanFalse)
SetupMemSwapRegion
%s::%s: working copy content: 0x%x len: %llu \n
startTimeObject && endTimeObject
%s::%s: invalid parameters \n
%s::%s: datapipe: failed to copy directory name %s \n
%s::%s: state = %u \n
%s::%s: requesting coredump failed (ret=0x%x) \n
true
FaultReporter
%s::%s: Close ret = 0x%x \n
%s::%s: Open error (ret = 0x%x) \n
IOService
SetPowerOverride(true) == kIOReturnSuccess
WaitForPCIErrorNotifications
%s::%s: client: %s \n
%s::%s: invalid state for reset %u \n
%s::%s: crash poll iterations = %u \n
%s::%s: log collection already enqueued \n
%06llu.%06llu SetBusLeadEnable Start enable: %s\n
time          r/w address    value\n
%s::%s: tp poll count %u \n
%s::%s: device id: 0x%x \n
%s::%s: failed to find MSI property \n
%s::%s: invalid crash log buffer \n
%s::%s: failed to open IOPCIDevice (ret = 0x%x) \n
ServiceNotificationReady_Impl_block_invoke_2
%s::%s: airship service not ready \n
SetPropertyUpdateNotificationHandler
ivars->clientName
Reset_block_invoke
%06llu.%06llu 0x%x\n
%s::%s: failed to set enable int source (ret = 0x%x) \n
ivars->queue->OnQueue()
%s::%s: invalid filename/statedump \n
v24@?0^{AirshipDriverDK=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})(?=^{AirshipDriverDK_IVars}^{AirshipDriverDK_LocalIVars})}8r^{OSString=^^?Aii^{OSMetaClass}^^?(?=^{OSObje
WaitForRemote
%s::%s: failed to create reset state item (ret=0x%x) \n
time          flags\n
TimeToOSBootStage
FLRCount
GetResetHint
Stop_Impl
%s::%s: failed to create working copy IOBMD (ret = 0x%x) \n
%s::%s: failed to create osdata object for StateDump \n
prevState == kCentauriDextRecoveryStateIdle || prevState == kCentauriDextRecoveryStateWaitForRemote
ExecuteDeferredWorkAsync_block_invoke
waitingForReadyForReset
crashlogStart
%s::%s: not permitted for ss id %u \n
ivars->dextRecoveryState == kCentauriDextRecoveryStateFetchMemSwap
dict && dict->setObject(kCentauriPropertyBootComplete, kOSBooleanTrue)
ivars->logCollectionInfo.type == kCentauriLogCollectionFatal
flrLimit: %d\n
readData
Recovery
/Library/Caches/com.apple.xbs/558FE645-4E39-4399-A06E-8DC20AC536F1/TemporaryDirectory.VSeWMb/Sources/AppleCentauri_driverkit/CentauriSubsystem/CentauriSubsystemUserClient.cpp
%s::%s: failed to get dir name \n
%s::%s: Using FLR limit: %u \n
length < sizeof(configName)
not null
%s::%s: signature mismatch \n
OSAction_CentauriSubsystem_MemSwapCallback
%s::%s: failed to create reset timestamps dict \n
%s::%s: ptm enabled, clock granularity: %u ns \n
ReadyForResetDuration
ivars->loggerQueue->OnQueue()
%s::%s: invalid metadata dict \n
%s::%s: timer expired waiting for remote service in reset failed state \n
%s::%s: ErrorDetected's value type is not a dictionary \n
dict
%s::%s: failed to get user client service \n
%s::%s: FLR limit (%u) reached \n
FunctionReset
%s::%s: failed to create log stream \n
%s::%s: added file %s, size %zu \n
IOPCIPMCSState
NotifyPropertyUpdate
InterruptOccurred_Impl
TimeElapsed
ivars->resetTimestamps
Crashlog.WFMAIN.bin
%s::%s: using cc log level %u \n
%s::%s: Driver offline. Ignoring state change %u \n
%s::%s: %s property exists - skipping dext crash \n
obj
%s::%s: options 0x%x reason %s \n
%06llu.%06llu 0x%08llx %s 0x%08x\n
%s::%s: FLR limit override boot-arg is set \n
!ivars->remoteInterfaceAvailable
PTM
DriverLogs
%s::%s: stream: failed to copy log identifier %s \n
%s::%s: failed to create pci error queue (ret = 0x%x) \n
%s::%s: failed to create error event action ret = 0x%x \n
%s::%s: new exec stage: %u \n
%s::%s: PCI dart error %u: [%s] addressLo: 0x%x addressHi: 0x%x \n
%s::%s: FLR count: %u \n
%s::%s: bad size (got %u max %u) \n
%s::%s: error handler not registered \n
ivars->cachedErrorsArray->setObject(cachedError)
%s::%s: deferring due to low power \n
%06llu.%06llu SetupMemSwapRegion ret: 0x%03x\n
CentauriPowerStateLog.txt
%s::%s: invalid number of MSIs configured: %u \n
LPW
resetStart
%s::%s: failed to get the fault reporter additional owner \n
%s::%s: failed to set dext relaunch property (ret = 0x%x) \n
count  primaryStart    secondaryStart  end           type\n
%s::%s: caching crashlog \n
OSAction_CentauriSubsystem_CompletionCallback
%s::%s: GetBusyState ret = 0x%x \n
yes
%s::%s: failed to set dict object for %s \n
    promoteToFullReset: %d\n
GetCrashlogs
functionResetEnd
SubsystemID
WiFi
%s::%s:  \n
Owner
Start_Impl_block_invoke_3
%s::%s: failed to create logger queue (ret = 0x%x) \n
ivars->inFlightWork > 0
EndWork
%s::%s: failed to create completion os action (ret = 0x%x) \n
val
%s::%s: service matching set up for %s \n
%s::%s: unexpected coredump completion \n
%s::%s: invalid segment info (addr: 0x%qx len: 0x%qx) \n
com.apple.ConnectivityDriver.FLRPerformanceStats
Unknown
OSAction_CentauriSubsystem_ChipResetCallback
%s::%s: escalate FLR failure \n
ivars->timerAction
[Fatal]
CollectLogsStateDumps
!ivars->deferredWork.reset
%s::%s: failed to allocate memory \n
%s::%s: failed to copy collectLogs block \n
SendAnalytics
Offline
Running
centauri-ccloglevel
LoggingProperties
LogIdentifier
TriggerFaultReport
Stop_Impl_block_invoke
%s::%s: service notification (type: %llu) \n
cachedError->getLength() == sizeof(CentauriCachedErrorInfo)
MemSwapCallback_Impl
flrCountDict->setObject(kCentauriFLRCount, flrCountObject)
%s::%s: failed to copy completionCb block \n
DirectoryName
CollectDeferredFaultDataCb_block_invoke
ServiceNotificationReady_Impl
TriggerClientLaunch
CollectAirshipStateDumps
AirshipStateDump.bin
%s::%s: fault reporter is busy \n
%s::%s: failed to report error (ret = 0x%x) \n
ivars->memSwapAction && ivars->completionAction && ivars->chipResetAction && ivars->collectLogsAction && ivars->watchdogAction
%s::%s: release PM assertion \n
ivars->state == kCentauriStateLogCollection
CentauriChipInfo.txt
item->block
%s::%s: data::%x \n
kCentauriBetaMemswapTimeoutErrorKey
v8@?0
StateSnapshots
errorData
oldValue != nullptr
PrepareDMACommand
centauri-flr-timeout-ms
TimeToTriggerCollectLogs
IsValidBootStage
ReleasePMAssertion(ivars->pmAssertionID) == kIOReturnSuccess
%s::%s: failed to schedule immediate wake \n
NewUserClient_Impl
%s::%s: client already registered (%s) \n
%06llu.%06llu Reset Start\n
On
UpTimestamp
%s::%s: driver offline - ignoring airship fatal error notification \n
%s
%s::%s: failed to set properties (ret = 0x%x) \n
setFLRBit
%s::%s: invalid viddid \n
%s::%s: failed to get log id \n
%s::%s: failed to get MSI data (ret = 0x%x) \n
SetupServiceMatchingNotification
ret == kIOReturnSuccess || ret == kIOReturnNotOpen
    resetFailed: %d\n
%s::%s: invalid input dictionary - bailing out \n
%s::%s: driver offline (state = %u) \n
%s::%s: invalid memswap map or working copy desc \n
%s::%s: failed to alloc metadata \n
%s::%s: failed to alloc OSNumber for up time \n
%s::%s: failed to copy block \n
RestoreDeviceState
prepareChipForResetStart
Start_Impl
%s::%s: driver offline - ignoring airship error notification \n
%s::%s: pmcsr 0x%04x \n
%s::%s: remote service unavailable. wait for %u ms \n
%s::%s: memswap memory map is already set \n
UnexpectedDextTermination
EnablePTMOnEndpoint
Invalid
%s::%s: failed HasPCIPowerManagement (ret = 0x%x) \n
%s::%s: failed to enable timer (ret = 0x%x) \n
%s::%s: airship reported error: 0x%x \n
pmcsr != nullptr
ClientOpen
SetProperties_Impl
no
readyForReset
OS
%s::%s: Invalid coreName or crashlogData observed \n
%s::%s: ignoring based on boot-arg \n
%s::%s: pci device not open \n
eventNameObject
prepareChipForResetEnd
OSAction_CentauriSubsystem_TimerOccurred
derivedStop
SetupRemoteActionCallbacks
ivars->cachedCrashlogsArray->getCount() > 0
%s::%s: crashlog too small: %zu bytes \n
%s::%s: Invalid segmentName or segmentDump observed \n
com.apple.queue.centauri-corecapture
cachedError
flrCountObject != nullptr
CollectLogsFatal
%s::%s: failed to allocate pending work item \n
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x \n
%s::%s: memory allocation crashlog reason string failed \n
centauri-allow-panic
%s::%s: invalid length (working copy %llu t0 %llu) \n
%06llu.%06llu CollectDiagnostics Start %s %s\n
%s::%s: failed to find aer capability (ret = 0x%x) \n
Boot
%s::%s: failed to SaveDeviceState (ret = 0x%x) \n
%s::%s: failed to get MSI addr (ret = 0x%x) \n
%s::%s: failed to copy system state service (ret = 0x%x) \n
InitializeMSI
%s::%s: failed to find ptm capability (ret = 0x%x) \n
%s::%s: crashlog size larger than buffer (%zu > %zu) \n
%s::%s: failed to get IOPCIDevice \n
%s::%s: initialized MSI-1 \n
%s::%s: reserved MSIs via provider \n
%s::%s: section too small \n
fLock
ModuleName
%s::%s: error filling buffer, bytesPrinted: %d kLineLength: %u \n
ssID < kNumSubsystems
%s::%s: failed to set monotonic time object \n
%s::%s: number of crashlogs: %u \n
Fiq
%s::%s: invalid callback parameters \n
%s::%s: failed to get logging properties dict \n
%s::%s: bad args \n
CheckErrorPolicyForKey
%s::%s: chip class not initialized \n
%s::%s: failed to set airship driver config \n
%s::%s: buffer filled, totalBytesPrinted: %u bufferSize: %u \n
ret == kIOReturnSuccess
LogFileName
%s::%s: didDextRelaunch = %s (reason %u) \n
execStage <= kCentauriBootStageMax
SetPTMProperty
AppleCentauri-129
loggerstream
AirshipDriverDK
%s::%s: timer expired waiting for memswap info in dext crash recovery state \n
%s::%s: failed to allocate statedump buffer \n
%06llu.%06llu CollectLogs Complete ret: 0x%03x\n
SendTimeSinceLastFLRAnalytics
ErrorCode
%s::%s: failed to create log pipe with provider %s \n
Yes
%s::%s: failed to create chip reset os action (ret = 0x%x) \n
prevState == kCentauriDextRecoveryStateIdle
eventName && payload
ErrorDetected
RunningLPM
%s::%s: module name not found \n
%s::%s: failed to copy service name (ret = 0x%x) \n
%s::%s: completion \n
MSI-1
action == ivars->msiAction
%s::%s: number of MSIs requested: %u \n
Control
%s::%s: failed to allocate metadata dict \n
CentauriStateDump.txt
TriggerChipCrash
%s::%s: failed to set dict object for StateDump \n
%s::%s: cachedErrorCount: %u \n
%s::%s: failed to copy prepareCb block \n
%s::%s: failed to save timestamp \n
%s::%s: dispatching propertyUpdateNotification \n
%s::%s: clearing cfg mbx at offset 0x%x \n
time          offset     r/w data\n
%s::%s: failed to create osdict \n
ivars->finalizeHandler
%s::%s: first power on \n
%s::%s: timer expired waiting for remote service in dext crash recovery state \n
%s::%s: bad max size \n
PrepareFaultReportCb
%s::%s: failed to alloc dict \n
%s::%s: power assertion already held \n
Idle
Stop
SetRequireClientProperty
B16@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8
ChipResetCallback_Impl
EnqueueDeferredWork(blockCopy, kCentauriDeferredWorkTypeOther)
%s::%s: reset already enqueued \n
ReadMSIData
ivars->pciDevice
%s::%s: failed to set require client property (ret = 0x%x) \n
ivars->cachedErrorsArray
state: %s\n
LogCollection
BT
%s::%s: failed to get logging properties object \n
%s::%s: error appending bytes to bufferObject \n
CopyName(&serviceName) == kIOReturnSuccess
%s::%s: block copy failed \n
memSwapMapT0: %s\n
%s::%s: failed to get provider \n
DerivedLogState
%s::%s: lpw -> on \n
%s::%s: propertyUpdateNotification handler not registered \n
CollectLogs_block_invoke
%s::%s: failed to create osdata object \n
remoteInterfaceAvailable: %d\n
GetNumMSIVectorsFromEndpoint
kCentauriBetaRemoteServiceTimeoutErrorKey
%s::%s: failed to allocate inFlightLock \n
%s::%s: failed to alloc OSString \n
%s::%s: full chip reset in progress \n
AppleCentauriManager::SaveClientProperty(this, key, newValue, kCentauriAutoClearOnChipReset) == kIOReturnSuccess
%06llu.%06llu RestoreDeviceState ret: 0x%03x\n
CentauriMSILog.txt
%s::%s: driver offline \n
%s::%s: match notification for AirshipDriverDK \n
WaitForReadyForReset
PartiallyBooted
Crashlog.CTRL.bin
ReadMSIAddr
%s::%s: failed to allocate lock
%s::%s: failed to EnablePCIPowerManagement (ret = 0x%x)
%s::%s: failed to set require client property (ret = 0x%x)
%s::%s: remote interface error (ret = 0x%x)
%s::%s: MSI handler: boot stage = %u
%s::%s: invalid callback parameters
%s::%s: failed to create error event action ret = 0x%x
%s::%s: state = %u
%s::%s: failed to set properties (ret = 0x%x)
%s::%s: failed to get log id
%s::%s: failed to get default queue (ret = 0x%x)
%s::%s: new exec stage: %u
%s::%s: powerFlags: %u
%s::%s: invalid state for reset %u
%s::%s: invalid state (%u)
%s::%s: failed to allocate OSData
%s::%s: reserved MSIs via provider
%s::%s: Invalid segmentName or segmentDump observed
%s::%s: no ptm key - bailing out
%s::%s: client: %s
%s::%s: completion
%s::%s: invalid state for watchdog notification: %u
%s::%s: logger not available
%s::%s: Invalid coreName or crashlogData observed
%s::%s: error handler has been deregistered
%s::%s: failed to set real time object
%s::%s: fw crash reason string is not supported with non-fatal log collection
%s::%s: FLR timed out
%s::%s: crashlog size larger than buffer (%zu > %zu)
%s::%s: memory allocation crashlog reason string failed
%s::%s: failed to get dir name
%s::%s: airship service not ready
%s::%s: failed to create chip object for family %u
%s::%s: requesting coredump failed (ret=0x%x)
%s::%s: failed to remove property (ret = 0x%x)
%s::%s: failed to set up time object
%s::%s: invalid state for log collection %u
%s::%s: failed to get log file name
%s::%s: error handler not registered
%s::%s: boot stage: %s, fw state: %s
%s::%s: invalid number of MSIs requested: %u
%s::%s: invalid parameters
%s::%s: failed to enable timer (ret = 0x%x)
%s::%s: failed to create memswap os action (ret = 0x%x)
%s::%s: resuming reset (state = 0x%x)
%s::%s: failed to find aer capability (ret = 0x%x)
%s::%s: device id: 0x%x
%s::%s: pci device not open
%s::%s: crash log buffer too small: %zu bytes
%s::%s: failed to get the fault reporter additional owner
%s::%s: error filling buffer, bytesPrinted: %d kLineLength: %u
%s::%s: logpipe: failed to copy directory name %s
%s::%s: failed to create data log stream
%s::%s: failed HasPCIPowerManagement (ret = 0x%x)
%s::%s: bad arg
%s::%s: failed to create completion os action (ret = 0x%x)
%s::%s: failed to  SearchProperty (ret = 0x%x)
%s::%s: driver offline
%s::%s: provider not available
%s::%s: airship reported fatal error: %s
%s::%s: requesting full wake
%s::%s: dispatching cached errors
%s::%s: memswap memory is already DART mapped
%s::%s: failed to alloc OSNumber for real time
%s::%s: failed to set reason object
%s::%s: failed to get logging properties object
%s::%s: failed to create logger queue (ret = 0x%x)
%s::%s: invalid number of MSIs requested: %u available: %u
%s::%s: failed to create dict
%s::%s: failed to create os action (ret = 0x%x)
%s::%s: deferring (state = 0x%x)
%s::%s: failed to create msi interrupt source (ret = 0x%x)
%s::%s: found crashlog data for %s
%s::%s: driver offline - ignoring airship error notification
%s::%s: failed to save timestamp
%s::%s: not permitted
%s::%s: full chip reset in progress
%s::%s: cachedErrorCount: %u
%s::%s: failed to create IODMACommand (ret = 0x%x)
%s::%s: invalid segment count %u
%s::%s: invalid crashlog data
%s::%s: centauri-driverkit=0
%s::%s: invalid bootstage 0x%x
%s::%s: invalid input dictionary - bailing out
%s::%s: driver offline (state = %u)
%s::%s: boot stage = ready for reset
%s::%s: failed to validate segment length (ret = 0x%x expected %llu got %llu)
%s::%s: clearing cfg mbx at offset 0x%x
%s::%s: %s
%s::%s: failed to SaveDeviceState (ret = 0x%x)
%s::%s: replacing existing client
%s::%s: working copy content: 0x%x len: %llu
%s::%s: FLR count: %u
%s::%s: resuming fatal log collection (state = 0x%x)
%s::%s: Crashlog Reason not found from the Crashlog data
%s::%s: failed to RestoreDeviceState (ret = 0x%x)
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu
%s::%s: LPM log collection mode unsupported
%s::%s: Transaction pending poll timed out. Proceeding to FLR
%s::%s: failed to create data log pipe
%s::%s: failed to report error (ret = 0x%x)
%s::%s: unexpected termination notification
%s::%s: FLR limit (%u) reached
%s::%s: failed to alloc OSNumber for SS ID
%s::%s: failed to alloc OSNumber for up time
%s::%s: tp poll count %u
%s::%s: failed to get IOPCIDevice
%s::%s: errorSource: %u, errorCode: %u, arg: 0x%llx
%s::%s: failed to set airship driver config
%s::%s: power assertion already held
%s::%s: PCI dart error
%s::%s: invalid cmd id: %u
%s::%s: AppleCentauriManager::Open failed (ret = 0x%x)
%s::%s: failed to copy service name (ret = 0x%x)
%s::%s: invalid client
%s::%s: failed to set SS ID object
%s::%s: caching crashlog
%s::%s: in fatal error state (%u)
%s::%s: Logging prop: owner: %s dir: %s file: %s id: %s
%s::%s: fault reporter is busy
%s::%s: number of MSIs requested: %u (SingleMSI mode)
%s::%s: GetBusyState ret = 0x%x
%s::%s: service matching set up for %s
%s::%s: match notification for CentauriRemoteInterface
%s::%s: lpw -> on
%s::%s: block copy failed
%s::%s: failed to create airship transport
%s::%s: first power on
%s::%s: failed to get addr range (ret = 0x%x)
%s::%s: number of MSIs requested: %u
%s::%s: ptm enabled, clock granularity: %u ns
%s::%s: didDextRelaunch = %s (reason %u)
%s::%s: failed to create timer action (ret = 0x%x)
%s::%s: datapipe: failed to copy directory name %s
%s::%s: service notification (type: %llu)
%s::%s: SetProperties failed
%s::%s: log collection already enqueued
%s::%s: failed to set dict object for StateDump
%s::%s: using cc log level %u
%s::%s: failed to copy properties
%s::%s: failed to allocate memory
%s::%s: failed to create chip reset os action (ret = 0x%x)
%s::%s: remote interface unavailable
%s::%s: in low power
%s::%s: deferring reset
%s::%s: ready for reset timed out
%s::%s: failed to create timer src (ret = 0x%x)
%s::%s: Driver offline. Ignoring state change %u
%s::%s: timer expired waiting for remote service in reset failed state
%s::%s: error source not found for %s
%s::%s: failed to get user client service
%s::%s: failed to set dict object
%s::%s: failed to find ptm capability (ret = 0x%x)
%s::%s: 
%s::%s: failed to set os action handler (ret = 0x%x)
%s::%s: failed to alloc OSString
%s::%s: dispatching propertyUpdateNotification
%s::%s: unexpected coredump completion
%s::%s: crash poll iterations = %u
%s::%s: cached crashlogs not available
%s::%s: reset failed (ret = 0x%x)
%s::%s: failed to copy completion block
%s::%s: log collection failed (ret = 0x%x)
%s::%s: data::%x
%s::%s: current timestamp is older than last reset timestamp, ignoring
%s::%s: failed to create log stream
%s::%s: module name not found
%s::%s: failed to allocate metadata dict
%s::%s: bad size (got %u max %u)
%s::%s: logpipe: failed to copy file name %s
%s::%s: failed to create fault reporter
%s::%s: FLR limit override boot-arg is set
%s::%s: bad args
%s::%s: initialized MSI-1
%s::%s: failed to get MSI data (ret = 0x%x)
%s::%s: match notification for AirshipDriverDK
%s::%s: unexpected match notification
%s::%s: invalid length
%s::%s: device control reg val: 0x%x
%s::%s: Close ret = 0x%x
%s::%s: %s property exists - skipping dext crash
%s::%s: failed to get airship probe result
%s::%s: super init failed
%s::%s: failed to set dext relaunch property (ret = 0x%x)
%s::%s: deliver notification error (ret = 0x%x)
%s::%s: timer expired waiting for memswap info in dext crash recovery state
%s::%s: bad max size
%s::%s: airship not up; returning %s
%s::%s: failed to create user class dict
%s::%s: not permitted for ss id %u
%s::%s: boot stage = %s
%s::%s: failed to create dispatch src (ret = 0x%x)
%s::%s: failed to create os action for watchdog notification (ret = 0x%x)
%s::%s: memswap memory map is already set
%s::%s: ASPM state: %u
%s::%s: failed to get provider
%s::%s: failed to alloc metadata
%s::%s: failed to trigger fault report (ret = 0x%x)
%s::%s: failed to copy provider properties
%s::%s: failed to find MSI property
%s::%s: signature mismatch
%s::%s: invalid metadata dict
%s::%s: failed to configure interrupts (ret = 0x%x)
%s::%s: reset in progress. ignoring error
%s::%s: error code not found
%s::%s: failed to prepare for DMA (ret = 0x%x)
%s::%s: invalid number of MSIs configured: %u
%s::%s: driver offline - ignoring airship fatal error notification
%s::%s: failed to create reset state item (ret=0x%x)
%s::%s: log collection failed (ret=0x%x)
%s::%s: failed to allocate statedump buffer
%s::%s: failed to copy immediateCb block
%s::%s: buffer filled, totalBytesPrinted: %u bufferSize: %u
%s::%s: returned from SetProperties (ret = 0x%x)
%s::%s: failed to set boot complete property (ret = 0x%x)
%s::%s: invalid memswap DMA command
%s::%s: pci read invalid data
%s::%s: escalate FLR failure
%s::%s: offline
%s::%s: failed to create memory map (ret = 0x%x)
%s::%s: requesting crashlog failed (ret=0x%x)
%s::%s: skipping %s
%s::%s: logpipe: failed to copy log identifier %s
%s::%s: failed to create pci error queue (ret = 0x%x)
%s::%s: failed to alloc dict
%s::%s: failed to copy block
%s::%s: failed to create file name copy
%s::%s: FLR timeout override: %u ms
%s::%s: crashlog too small: %zu bytes
%s::%s: failed to update the FW crash reason string
%s::%s: failed to create reason string copy
%s::%s: failed to create osdict
%s::%s: Crashlog Reason: \"%s\"
%s::%s: failed super Start (ret = 0x%x)
%s::%s: failed to get platform (ret = 0x%x)
%s::%s: Open error (ret = 0x%x)
%s::%s: log collection in progress/enqueued
%s::%s: ptm requester role not supported
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x
%s::%s: added file %s, size %zu
%s::%s: Stop ret = 0x%x
%s::%s: failed to set ptm status in subsystem properties (ret = 0x%x)
%s::%s: ignoring based on boot-arg
%s::%s: failed to create user client (ret = 0x%x)
%s::%s: deferring due to low power
%s::%s: invalid segment info (addr: 0x%qx len: 0x%qx)
%s::%s: msiaddr::%llx
%s::%s: failed to get logging properties dict
%s::%s: invalid memswap map or working copy desc
%s::%s: number of crashlogs: %u
%s::%s: state %u
%s::%s: failed to get logger
%s::%s: %u
%s::%s: testID: %u
%s::%s: deferred work is canceled
%s::%s: failed to set dict object for %s
%s::%s: failed to set enable int source (ret = 0x%x)
%s::%s: sleeping for %u ms...
%s::%s: failed to copy deferredCb block
%s::%s: invalid filename/statedump
%s::%s: error handler already exists
%s::%s: failed to copy collectLogs block
%s::%s: bad arguments
%s::%s: finalize %d
%s::%s: remote service unavailable. wait for %u ms
%s::%s: failed to copy reset block
%s::%s: failed to create osdata object
%s::%s: Using FLR limit: %u
%s::%s: error source %u code %u arg %llu
%s::%s: function reset already in progress
%s::%s: failed to allocate pending work item
%s::%s: failed to get owner object
%s::%s: propertyUpdateNotification handler not registered
%s::%s: failed to create working copy IOBMD (ret = 0x%x)
%s::%s: hint: %u
%s::%s: failed to open IOPCIDevice (ret = 0x%x)
%s::%s: failed to get MSI addr (ret = 0x%x)
%s::%s: failed to create reset timestamps dict
%s::%s: skipping during dext crash recovery
%s::%s: chip class not initialized
%s::%s: failed to find PCI capability (ret = 0x%x)
%s::%s: driver %s - ignoring MSI notification
%s::%s: failed to allocate inFlightLock
%s::%s: termination notification for AirshipDriverDK
%s::%s: failed to create os action for collect logs (ret = 0x%x)
%s::%s: powerFlags: %s
%s::%s: PCI dart error %u: [%s] addressLo: 0x%x addressHi: 0x%x
%s::%s: chip crash timed out
%s::%s: failed to alloc OSNumber for monotonic time
%s::%s: poll count %u
%s::%s: stream: failed to copy log identifier %s
%s::%s: failed to copy system state service (ret = 0x%x)
%s::%s: invalid driver state %u for dext crash recovery state %u
%s::%s: invalid crash log buffer
%s::%s: crashlog header reports empty: %zu bytes
%s::%s: invalid link control value
%s::%s: failed to get provider queue
%s::%s: failed to save FLR timestamps
%s::%s: failed to schedule immediate wake
%s::%s: options 0x%x reason %s
%s::%s: selector %llu
%s::%s: client already registered (%s)
%s::%s: MSICapOffset::%llx
%s::%s: failed to copy prepareCb block
%s::%s: failed to create log pipe with provider %s
%s::%s: failed to create function name copy
%s::%s: failed to find msi capability (ret = 0x%x)
%s::%s: failed to send %s (ret=0x%x)
%s::%s: ret = 0x%x
%s::%s: invalid notifier
%s::%s: driver offline - ignoring exec stage notification
%s::%s: termination notification for CentauriRemoteInterface
%s::%s: pmcsr 0x%04x
%s::%s: handler already exists
%s::%s: cmd id %u ret 0x%x
%s::%s: requesting deferral (low power: %u, defer for memswap: %s)
%s::%s: using console log level %u
%s::%s: error appending bytes to bufferObject
%s::%s: invalid viddid
%s::%s: unexpected crash log completion
%s::%s: coredump/crashlog completion failed (ret=0x%x)
%s::%s: failed to create osdata object for StateDump
%s::%s: failed to copy completionCb block
%s::%s: invalid state (%s)
%s::%s: timer expired waiting for remote service in dext crash recovery state
%s::%s: error arg not an OSNumber
%s::%s: reset already enqueued
%s::%s: release PM assertion
%s::%s: ErrorDetected's value type is not a dictionary
%s::%s: invalid length (working copy %llu t0 %llu)
%s::%s: failed to serialize
%s::%s: ret: 0x%x flags: 0x%qx cnt: %d addr: 0x%qx len: 0x%qx
%s::%s: empty crash log buffer
%s::%s: errorCode %u, reason %s
%s::%s: airship reported error: 0x%x
%s::%s: error reported by %s error code %u
%s::%s: invalid viddid 0x%x
%s::%s: failed to create osdata object for %s
%s::%s: failed to set monotonic time object
%s::%s: section too small
```
