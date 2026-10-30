# `/System/DriverKit/System/Library/PrivateFrameworks/CentauriAlpha.framework/CentauriAlpha`

From the upgrade restore ramdisk (141-29011-104.dmg). 459,008 bytes.

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
LPMOS
%s::%s: fault reporter is busy \n
%s::%s: failed to update the FW crash reason string \n
OSAction_CentauriSubsystem_MemSwapCallback
%s::%s: failed to create timer action (ret = 0x%x) \n
%s::%s: boot stage = ready for reset \n
%s::%s: cached crashlogs not available \n
%s::%s: invalid number of MSIs requested: %u \n
%s::%s: bad args \n
%s::%s: failed to create os action (ret = 0x%x) \n
%s::%s: failed to save FLR timestamps \n
%s::%s: Driver offline. Ignoring state change %u \n
dict && dict->setObject(kCentauriPropertyPTMEnabledOnEndpoint, ptmStatus)
completionCopy
CentauriConfigAccessLog.txt
offline
%s::%s: failed to set dict object \n
%s::%s: ASPM state: %u \n
On
LPMBoot
OSAction_CentauriSubsystem_CompletionCallback
centauri-fatal-err-panic
%s::%s: airship service not ready \n
ivars->clientName
GetCrashlogs
Idle
Off
%s::%s: invalid callback parameters \n
%s::%s: failed to get logging properties dict \n
%s::%s: Close ret = 0x%x \n
N/A
%s::%s: unexpected crash log completion \n
%s::%s: failed to serialize \n
%s::%s: Logging prop: owner: %s dir: %s file: %s id: %s \n
%s::%s: failed to create log pipe with provider %s \n
%s::%s: failed to create error event action ret = 0x%x \n
%s::%s: escalate FLR failure \n
%s::%s: failed to create user client (ret = 0x%x) \n
AirshipStateDump.bin
NumMSIs
CancelCrashlogHandler_block_invoke
EndWork
%s::%s: invalid state (%s) \n
%s::%s: no ptm key - bailing out \n
userClient
test
%s::%s: deferring (state = 0x%x) \n
ExecuteDeferredWork
RestoreDeviceState
%s::%s: Using FLR limit: %u \n
%s::%s: chip class not initialized \n
dict->setObject(key, kOSBooleanTrue)
name
SetupMemSwapRegion
%s::%s: empty crash log buffer \n
fatalLogCollectionTriggered
InitWithProviderAndOptions
%s::%s: finalize %d \n
Stop_Impl_block_invoke
B24@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}16
%s::%s: failed to alloc OSNumber for up time \n
eventNameObject
ExternalMethod
/Library/Caches/com.apple.xbs/558FE645-4E39-4399-A06E-8DC20AC536F1/TemporaryDirectory.VSeWMb/Sources/AppleCentauri_driverkit/CentauriSubsystem/CentauriSubsystemUserClient.cpp
%s::%s: testID: %u \n
fatal
%s::%s: failed to create osdict \n
!ivars->deferredWork.reset
%s::%s: failed to find PCI capability (ret = 0x%x) \n
FLRDuration
centauri-flr-limit
v20@?0^{AirshipDriverDK=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})(?=^{AirshipDriverDK_IVars}^{AirshipDriverDK_LocalIVars})}8I16
%s::%s: offline \n
%s::%s: bad size (got %u max %u) \n
    crashlogPending: %d\n
PrepareDMACommand
%s::%s: failed to find ptm capability (ret = 0x%x) \n
%s::%s: failed to save timestamp \n
%s::%s: release PM assertion \n
CreateMetadataDict
%s::%s: failed to set require client property (ret = 0x%x) \n
cachedError
%s::%s: pci read invalid data \n
eventName && payload
%s::%s: datapipe: failed to copy directory name %s \n
SetPrepareForResetHandler_block_invoke
%06llu.%06llu CollectDiagnostics Start %s %s\n
%s::%s: resuming fatal log collection (state = 0x%x) \n
%s::%s: found crashlog data for %s \n
%s::%s: errorCode %u, reason %s \n
report-error
%s::%s: failed to alloc OSNumber for monotonic time \n
inLowPower: %d\n
%s::%s: failed to copy provider properties \n
%s::%s: crashlog size larger than buffer (%zu > %zu) \n
functionResetEnd
CollectDeferredFaultDataCb
%s::%s: failed to create os action for watchdog notification (ret = 0x%x) \n
%s::%s: failed to  SearchProperty (ret = 0x%x) \n
%s::%s: invalid input dictionary - bailing out \n
%s::%s: failed to create reset state item (ret=0x%x) \n
%s::%s: remote interface unavailable \n
DeferReset
CollectLogs_block_invoke
ErrorArg
%s::%s: power assertion already held \n
oldValue != nullptr
%06llu.%06llu SaveDeviceState ret: 0x%03x\n
address && length && coredump
%s::%s: invalid driver state %u for dext crash recovery state %u \n
%s::%s: crashlog too small: %zu bytes \n
AbortHandler
OSAction_CentauriSubsystem_ChipResetCallback
%s::%s: failed to allocate inFlightLock \n
%s::%s: bad arg \n
%s::%s: powerFlags: %s \n
%s::%s: module name not found \n
AirshipDriverConfigName
%s::%s: FLR limit (%u) reached \n
%s::%s: failed to allocate statedump buffer \n
%s::%s: invalid crashlog data \n
SetRequireClientProperty
%s::%s: ignoring based on boot-arg \n
SetPropertyUpdateNotificationHandler
dict && dict->setObject(kCentauriPropertyBootComplete, kOSBooleanTrue)
subsystemNameObject
FLRCount
ExecStageChanged
%s::%s: first power on \n
%s
%s::%s: failed to find MSI property \n
PartiallyBootedLPM
GetFaultReporter
%s::%s: failed to create airship transport \n
%s::%s: Open error (ret = 0x%x) \n
%s::%s: client: %s \n
%s::%s: deferring due to low power \n
%s::%s: fw crash reason string is not supported with non-fatal log collection \n
ivars->logCollectionInfo.type == kCentauriLogCollectionFatal
%s::%s: msiaddr::%llx \n
i8@?0
ivars->memSwapAction && ivars->completionAction && ivars->chipResetAction && ivars->collectLogsAction && ivars->watchdogAction
Subsystem
%s::%s: using cc log level %u \n
%s::%s: failed to get owner object \n
%s::%s: unexpected termination notification \n
centauri-recovery
key
%s::%s: returned from SetProperties (ret = 0x%x) \n
%s::%s: failed to get addr range (ret = 0x%x) \n
CollectLogsFatal_block_invoke
remoteService: %s\n
%s::%s: failed to create dispatch src (ret = 0x%x) \n
key && dict
ClientClose
%s::%s: failed to allocate metadata dict \n
 r 
%s::%s: skipping %s \n
%s::%s: failed to create memswap os action (ret = 0x%x) \n
%s::%s: invalid viddid 0x%x \n
%s::%s: failed to create msi interrupt source (ret = 0x%x) \n
Owner
LogIdentifier
%06llu.%06llu Reset Start\n
Start_Impl_block_invoke_3
%s::%s: unexpected match notification \n
%s::%s: failed to schedule immediate wake \n
ret == kIOReturnSuccess || ret == kIOReturnNotOpen
handler
InitMemSwapWorkingCopy
WaitForPCIErrorNotifications
[NonFatal]
time          offset     r/w data\n
    resetFailed: %d\n
Offline
%s::%s: failed to remove property (ret = 0x%x) \n
CollectAirshipStateDumps
%s::%s: data::%x \n
Start_Impl
%s::%s: service matching set up for %s \n
%s::%s: not permitted \n
%s::%s: dispatching cached errors \n
    coredumpPending: %d\n
resetInfo:\n
SetErrorHandler_block_invoke
flrCountObject != nullptr
CollectLogsFatal
ClientPrepareForReset
ssID < kNumSubsystems
SACFunctionAvailable
%s::%s: deliver notification error (ret = 0x%x) \n
length < sizeof(fullReason)
ExecuteDeferredWorkAsync_block_invoke
TimeToTriggerCollectLogs
t2026
%s::%s: failed to EnablePCIPowerManagement (ret = 0x%x) \n
ivars->inFlightWork < UINT32_MAX
obj
EnqueueDeferredWork(blockCopy, kCentauriDeferredWorkTypeOther)
blockCopy
DartMapMemSwapWorkingCopy
%s::%s: state %u \n
%s::%s: Invalid segmentName or segmentDump observed \n
%s::%s: airship reported error: 0x%x \n
ivars->systemStateResetItemDict->setObject(kCentauriSystemStateNotificationResetKey, inReset ? kOSBooleanTrue : kOSBooleanFalse)
%s::%s: failed to copy properties \n
timeElapsedObject != nullptr
waitingForReadyForReset
%s::%s: failed to copy system state service (ret = 0x%x) \n
%s::%s: failed to create user class dict \n
execStage <= kCentauriBootStageMax
dict && dict->setObject(kCentauriPropertyUnexpectedDextTermination, (ivars->dextRelaunchReason == kCentauriManagerDextRelaunchReasonCrash) ? kOSBooleanTrue : kOSBooleanFalse)
DoReset
completion
Recovery
%s::%s: using console log level %u \n
(null)
super::SetErrorHandler(handler) == kIOReturnSuccess
derivedStart
%s::%s: failed to set dext relaunch property (ret = 0x%x) \n
SetupRemoteActionCallbacks
errorInfo
ROM
%s::%s: number of MSIs requested: %u \n
CrashlogDuration
ivars->crashlogHandler
%s::%s: provider not available \n
ChangePowerState(kIOServicePowerCapabilityOn) == kIOReturnSuccess
%s::%s: failed to alloc OSString \n
RD
 w 
%s::%s: invalid segment count %u \n
%s::%s: failed to get logging properties object \n
%s::%s: warning: prepare for reset handler is not registered \n
super::ClientOpen(clientNameCopy->getCStringNoCopy(), cookie) == kIOReturnSuccess
Default
v32@?0Q8^{IOService=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})}16Q24
%s::%s: failed to copy service name (ret = 0x%x) \n
ivars->cachedCrashlogsArray
%s::%s: invalid number of MSIs configured: %u \n
OSAction_CentauriSubsystem_InterruptOccurred
%s::%s: failed to get platform (ret = 0x%x) \n
!ivars->remoteInterfaceAvailable
pci-get-dart-error
CollectLogsCompletion
%s::%s: clearing cfg mbx at offset 0x%x \n
FunctionReset
%s::%s: match notification for CentauriRemoteInterface \n
nonfatal
%s::%s: sleeping for %u ms... \n
%s::%s: GetBusyState ret = 0x%x \n
yes
!ivars->inLowPower
CentauriMSILog.txt
CollectMemoryLog
%s::%s: failed to allocate OSData \n
ClearConfigSpaceMailboxes
%s::%s: service notification (type: %llu) \n
ivars->timerAction
%s::%s: failed to alloc metadata \n
%s::%s: failed to set dict object for %s \n
%s::%s: section too small \n
loggerstream
ivars->cachedErrorsArray
pci-dart-error-data
%s::%s: failed to get user client service \n
ivars->state == kCentauriStateLogCollection
/Library/Caches/com.apple.xbs/558FE645-4E39-4399-A06E-8DC20AC536F1/TemporaryDirectory.VSeWMb/Sources/AppleCentauri_driverkit/CentauriSubsystem/CentauriSubsystem.cpp
WatchdogCallback_Impl
%s::%s: in fatal error state (%u) \n
%s::%s: pci device not open \n
dextRelaunchObj != nullptr
ServiceNotificationReady_Impl_block_invoke_2
CancelPropertyUpdateNotificationHandler
ExtractCrashlogReason
TimeElapsed
CoredumpDuration
centauri-ccloglevel
%s::%s: remote service unavailable. wait for %u ms \n
length < sizeof(configName)
%s::%s: propertyUpdateNotification handler not registered \n
ivars->dextRecoveryState == kCentauriDextRecoveryStateFetchMemSwap
%s::%s: failed to set up time object \n
time          flags\n
ReadyForReset
%s::%s: logpipe: failed to copy directory name %s \n
i40@?0^^{OSDictionary}8^^{OSDictionary}16^^{OSDictionary}24^^{OSString}32
CopyName(&serviceName) == kIOReturnSuccess
centauri-allow-panic
%s::%s: ret: 0x%x flags: 0x%qx cnt: %d addr: 0x%qx len: 0x%qx \n
ConfigureEndpointForMemSwap
%s::%s: Transaction pending poll timed out. Proceeding to FLR \n
Stop
%s::%s: failed to create data log pipe \n
ServiceNotificationReady_Impl
%s::%s: timer expired waiting for remote service in dext crash recovery state \n
SetIPCProperties
%s::%s: block copy failed \n
%s::%s: function reset already in progress \n
%s::%s: failed to set real time object \n
collect-logs
0x%04llu %06llu.%06llu - %06llu.%06llu - %06llu.%06llu %s\n
com.apple.queue.centauri-pcierrors
%s::%s: failed to get IOPCIDevice \n
IOService
%s::%s: caching crashlog \n
RunningLPM
super::SetPropertyUpdateNotificationHandler(handler) == kIOReturnSuccess
%s::%s: logger not ready \n
%s::%s: failed to get provider queue \n
%s::%s: failed to get default queue (ret = 0x%x) \n
MSI-1
%s::%s: boot stage: %s, fw state: %s \n
in low power
%s::%s: logpipe: failed to copy log identifier %s \n
%s::%s: timer expired waiting for remote service in reset failed state \n
%s::%s: invalid bootstage 0x%x \n
%s::%s: %u \n
%s::%s: failed to create reason string copy \n
null
flrLimit: %d\n
SetDextRecoveryState
v24@?0I8I12^v16
centauri-driverkit
bootTimestampKey
WatchdogCallback_Impl_block_invoke
%s::%s: failed to create file name copy \n
kCentauriAlphaRemoteServiceTimeoutErrorKey
bootStageOSAlpha
%s::%s: invalid viddid \n
%s::%s: failed super Start (ret = 0x%x) \n
ExitLPW
SetResetTimestamp
OSAction_CentauriSubsystem_CentauriManagerErrorHandler
%s::%s: failed to copy completion block \n
ready for reset
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu \n
%s::%s: invalid filename/statedump \n
CompleteFaultReportCb
ivars->finalizeHandler
%s::%s: skipping during dext crash recovery \n
ivars->cachedErrorsArray->setObject(cachedError)
%s::%s: client already registered (%s) \n
MaskUnsupportedRequestAER
RealTimestamp
%s::%s: centauri-driverkit=0 \n
%s::%s: failed to SaveDeviceState (ret = 0x%x) \n
%s::%s: failed to get MSI addr (ret = 0x%x) \n
%s::%s: failed to create fault reporter \n
SetPowerOverride(true) == kIOReturnSuccess
%s::%s: requesting crashlog failed (ret=0x%x) \n
DextRelaunchState
CreateSystemStateNotificationItems
%s::%s: chip crash timed out \n
    type: %s\n
%s::%s: %s property exists - skipping dext crash \n
%s::%s: driver offline (state = %u) \n
%s::%s: log collection in progress/enqueued \n
PartiallyBooted
%s::%s: tp poll count %u \n
%s::%s: poll count %u \n
CancelPrepareForResetHandler
%s::%s: selector %llu \n
errorData
CentauriUserClientProperties
%s::%s: failed to send %s (ret=0x%x) \n
IOPCIPMCSState
AppleCentauriManager::SaveClientProperty(this, key, newValue, autoClearConditions) == kIOReturnSuccess
%s::%s: error code not found \n
CentauriManagerErrorHandler_Impl
    promoteToFullReset: %d\n
%s::%s: initialized MSI-1 \n
%s::%s: crash log buffer too small: %zu bytes \n
%s::%s: invalid link control value \n
success
OpenRemoteService
%s::%s: failed to set monotonic time object \n
ivars->cachedCrashlogsArray->getCount() > 0
LPW
OS
%s::%s: failed to get dir name \n
%s::%s:  \n
com.apple.queue.centauri-corecapture
%s::%s: invalid memswap map or working copy desc \n
%06llu.%06llu SetupMemSwapRegion ret: 0x%03x\n
MSI-2
kCentauriAlphaFLRCount
%s::%s: termination notification for AirshipDriverDK \n
RegisterServiceOrStartDextRecovery_block_invoke
SetState
Crashlog.BTMAIN.bin
SetCrashlogHandler_block_invoke
%s::%s: error arg not an OSNumber \n
ScheduleImmediateWake
ResetCompletion
clientNameCopy
%s::%s: airship not up; returning %s \n
ErrorCode
%s::%s: AppleCentauriManager::Open failed (ret = 0x%x) \n
ServiceNotificationReady_Impl_block_invoke
%s::%s: powerFlags: %u \n
ctx
%s::%s: state: 0x%x \n
[Fatal]
GetFirmwareState
%s::%s: failed to copy deferredCb block \n
%s::%s: Stop ret = 0x%x \n
%s::%s: driver offline - ignoring exec stage notification \n
%s::%s: driver offline - ignoring airship fatal error notification \n
chipId: %s\n
EnqueueDeferredWork
Reason
MonotonicTimestamp
%s::%s: invalid queue \n
%s::%s: failed HasPCIPowerManagement (ret = 0x%x) \n
count  primaryStart    secondaryStart  end           type\n
%s::%s: ret = 0x%x \n
!ivars->resetPrepareHandler
SetPropertyUpdateNotificationHandler_block_invoke
%s::%s: no crashlog handler \n
CreateChipObject
cachedError->getLength() == sizeof(CentauriCachedErrorInfo)
serializedBuffer && serializedLength
ivars->resetTimestamps
prepareChipForResetStart
%s::%s: error handler has been deregistered \n
CollectPowerStateLog
Control
%s::%s: failed to create data log stream \n
%s::%s: errorSource: %u, errorCode: %u, arg: 0x%llx \n
newValue
%s::%s: state = %u \n
errorDataObj != nullptr
%s::%s: options 0x%x reason %s \n
Unknown
Boot
InduceFaultCb
-
startTimeObject && endTimeObject
%s::%s: failed to copy completionCb block \n
derivedProbeDevice
%s::%s: driver offline \n
ret == kIOReturnSuccess
%s::%s: reset already enqueued \n
%s::%s: failed to allocate pending work item \n
%s::%s: failed to RestoreDeviceState (ret = 0x%x) \n
ErrorDetected
crashlogEnd
PrepareFaultReportCb
init
TriggerClientLaunch() == kIOReturnSuccess
version: %s\n
%s::%s: device control reg val: 0x%x \n
%s::%s: Invalid coreName or crashlogData observed \n
%s::%s: error appending bytes to bufferObject \n
SaveDeviceState
InterruptOccurred_Impl
action == ivars->msiAction
Coredump
AdditionalPipeOwners
%s::%s: invalid fault reporter \n
%s::%s: termination notification for CentauriRemoteInterface \n
NotifyPropertyUpdate
%s::%s: invalid state for reset %u \n
AppleCentauriManager::SaveClientProperty(this, key, newValue, kCentauriAutoClearOnChipReset) == kIOReturnSuccess
flrCountDict
%s::%s: failed to alloc OSNumber for SS ID \n
%s::%s: failed to copy block \n
%s::%s: requesting coredump failed (ret=0x%x) \n
%s::%s: didDextRelaunch = %s (reason %u) \n
ret == kIOReturnSuccess || ret == kIOReturnNotFound
%s::%s: failed to set airship driver config \n
ClientOpen
CompletionCallback_Impl
Reset_block_invoke
remoteInterfaceAvailable: %d\n
%s::%s: failed to create osdata object for %s \n
%s::%s: failed to enable timer (ret = 0x%x) \n
val
dict->setObject(kCentauriSystemStateNotificationResetKey, kOSBooleanTrue)
CentauriStateDump.txt
ivars->cachedCrashlogsArray->setObject(copy)
prevState == kCentauriDextRecoveryStateIdle || prevState == kCentauriDextRecoveryStateWaitForRemote
%s::%s: %s \n
SubsystemID
%s::%s: memswap memory is already DART mapped \n
%s::%s: failed to create osdata object \n
airshipService: %s\n
logCollectionInfo:\n
item->block
TriggerChipCrash
GetNumMSIVectorsFromEndpoint
ReadyForResetDuration
%s::%s: invalid metadata dict \n
%s::%s: timer expired waiting for memswap info in dext crash recovery state \n
%s::%s: working copy content: 0x%x len: %llu \n
Reset
%s::%s: FLR timed out \n
%s::%s: invalid crash log buffer \n
Crashed
Crashlog.CTRL.bin
v24@?0^{AirshipDriverDK=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})(?=^{AirshipDriverDK_IVars}^{AirshipDriverDK_LocalIVars})}8r^{OSString=^^?Aii^{OSMetaClass}^^?(?=^{OSObje
SetPTMProperty
Crashlog
CollectImmediateFaultDataCb
%s::%s: crashlog handler is not registered \n
OSAction_CentauriSubsystem_WatchdogCallback
%s::%s: invalid notifier \n
%s::%s: match notification for AirshipDriverDK \n
%s::%s: failed to create os action for collect logs (ret = 0x%x) \n
CheckErrorPolicyForKey
%s::%s: failed to set boot complete property (ret = 0x%x) \n
%s::%s: remote interface error (ret = 0x%x) \n
%06llu.%06llu RestoreDeviceState ret: 0x%03x\n
AppleCentauri-129
%s::%s: failed to set os action handler (ret = 0x%x) \n
%s::%s: PCI dart error %u: [%s] addressLo: 0x%x addressHi: 0x%x \n
%06llu.%06llu CollectDiagnostics Complete %s %s ret: 0x%03x\n
data
CacheCrashlogs
%s::%s: failed to set enable int source (ret = 0x%x) \n
val && ivars->resetTimestamps->setObject(eventName, val)
SendAnalytics
%s::%s: failed to create dict \n
%s::%s: failed to create chip object for family %u \n
%s::%s: log collection failed (ret=0x%x) \n
%s::%s: failed to alloc OSNumber for real time \n
GetCachedErrorCount
PrepareChipForResetDuration
BootComplete
setFLRBit
%s::%s: failed to alloc dict \n
not null
%s::%s: failed to get the fault reporter additional owner \n
ivars->resetPrepareHandler
kCentauriAlphaMemswapTimeoutErrorKey
SetPowerState_Impl
MemSwapCallback_Impl
CollectLogsCallback_Impl_block_invoke
prevState == kCentauriDextRecoveryStateCollectLogs
PTM
%s::%s: failed to copy prepareCb block \n
LogFileName
%s::%s: failed to get log file name \n
free
SetProperties_Impl
ivars->pciDevice
%s::%s: failed to create log stream \n
%s::%s: failed to get provider \n
OSAction_CentauriSubsystem_ServiceNotificationReady
%s::%s: failed to create logger queue (ret = 0x%x) \n
WaitForRemote
%s::%s: memswap memory map is already set \n
%s::%s: deferring reset \n
%s::%s: crash poll iterations = %u \n
%s::%s: new exec stage: %u \n
%s::%s: failed to create completion os action (ret = 0x%x) \n
%06llu.%06llu 0x%08llx %s 0x%08x\n
CollectLogsStateDumps
%s::%s: logpipe: failed to copy file name %s \n
%s::%s: added file %s, size %zu \n
CollectDeferredFaultDataCb_block_invoke
%s::%s: failed to allocate lock \n
%s::%s: failed to open IOPCIDevice (ret = 0x%x) \n
false
%s::%s: PCI dart error \n
%s::%s: failed to create osdata object for StateDump \n
dict
%s::%s: failed to trigger fault report (ret = 0x%x) \n
%s::%s: ptm requester role not supported \n
com.apple.ConnectivityDriver.FLRPerformanceStats
BT
FaultReporter
OSAction_CentauriSubsystem_TimerOccurred
Stop_Impl
%s::%s: dispatching propertyUpdateNotification \n
state: %s\n
SetPrepareForResetHandler
ReleasePMAssertion(ivars->pmAssertionID) == kIOReturnSuccess
PrepareChipForReset
%s::%s: resuming reset (state = 0x%x) \n
InReset
%s::%s: lpw -> on \n
CentauriEventLog.txt
dextRecoveryState: %s\n
%s::%s: ptm enabled, clock granularity: %u ns \n
SendTimeSinceLastFLRAnalytics
TriggerFaultReport
v8@?0
sacObj != nullptr
%s::%s: failed to report error (ret = 0x%x) \n
%s::%s: reset in progress. ignoring error \n
%s::%s: boot stage = %s \n
%s::%s: FLR count: %u \n
!ivars->deferredWork.logCollection
com.apple.ConnectivityDriver.TimeSinceLastFLR
ivars->logCollectionInfo.metadata
%s::%s: bad max size \n
time          r/w address    value\n
%s::%s: stream: failed to copy log identifier %s \n
%s::%s: prepare for reset handler is not registered \n
AirshipDriverDK
%s::%s: airship reported fatal error: %s \n
pmcsr != nullptr
ivars->queue->OnQueue()
memSwapMapT0: %s\n
%s::%s: reserved MSIs via provider \n
%s::%s: cmd id %u ret 0x%x \n
%s::%s: invalid state for watchdog notification: %u \n
%s::%s: no prepare for reset handler \n
%s::%s: driver offline - ignoring airship error notification \n
dict && dict->setObject(\"RequireClient\", kOSBooleanTrue)
%s::%s: replacing existing client \n
%s::%s: completion \n
%s::%s: log collection already enqueued \n
%s::%s: number of crashlogs: %u \n
%s::%s: failed to find msi capability (ret = 0x%x) \n
%s::%s: crashlog header reports empty: %zu bytes \n
%s::%s: failed to set ptm status in subsystem properties (ret = 0x%x) \n
%s::%s: failed to set reason object \n
!ivars->logCollectionInfo.metadata && !ivars->logCollectionInfo.completion
%s::%s: failed to find aer capability (ret = 0x%x) \n
readyForReset
%s::%s: failed to get airship probe result \n
%s::%s: failed to create reset timestamps dict \n
%s::%s: failed to create memory map (ret = 0x%x) \n
%s::%s: error filling buffer, bytesPrinted: %d kLineLength: %u \n
%s::%s: bad arguments \n
derivedStop
Start_Impl_block_invoke_2
No
%s::%s: failed to configure interrupts (ret = 0x%x) \n
RequireClient
%s::%s: error source %u code %u arg %llu \n
%s::%s: invalid cmd id: %u \n
v12@?0i8
%s::%s: ready for reset timed out \n
%s::%s: invalid state (%u) \n
%06llu.%06llu Reset Complete ret: 0x%03x\n
CollectMSILog
CentauriChipInfo.txt
copy
ClearUnsupportedRequestAER
ReadMSIAddr
GetASPMState
%s::%s: ErrorDetected's value type is not a dictionary \n
%s::%s: error handler already exists \n
B16@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8
%s::%s: buffer filled, totalBytesPrinted: %u bufferSize: %u \n
    updateFWReasonString: %d\n
%s::%s: memory allocation crashlog reason string failed \n
resetStart
Running
%s::%s: failed to create pci error queue (ret = 0x%x) \n
%s::%s: not permitted for ss id %u \n
force panic on fatal error for ss %u (type %u)
IsValidBootStage
prevState == kCentauriDextRecoveryStateIdle
%s::%s: Crashlog Reason not found from the Crashlog data \n
TimeToOSBootStage
crashlogStart
%s::%s: number of MSIs requested: %u (SingleMSI mode) \n
SetupServiceMatchingNotification
action == ivars->timerAction
CollectLogs
CollectEventLog
CollectStateSnapshots
centauri-flr-timeout-ms
ModuleName
%s::%s: requesting deferral (low power: %u, defer for memswap: %s) \n
%06llu.%06llu SetBusLeadEnable Start enable: %s\n
InitializeMSI
UpTimestamp
fwCrashReported
durationObject != nullptr
%s::%s: failed to copy immediateCb block \n
DriverLogs
ivars->loggerQueue->OnQueue()
%s::%s: failed to get MSI data (ret = 0x%x) \n
%s::%s: log collection failed (ret = 0x%x) \n
centauri-consoleloglevel
%s::%s: failed to get log id \n
%s::%s: failed to allocate memory \n
SetCrashlogHandler
ClientCrashlogHandler
%s::%s: deferred work is canceled \n
abort handler
CollectConfigLogs
%s::%s: FLR timeout override: %u ms \n
Crashlog.WFMAIN.bin
DirectoryName
StateSnapshots
com.apple.centauri.reset.wifi
TimerOccurred_Impl
%s::%s: SetProperties failed \n
GetBootStageMirror
%06llu.%06llu %s 0x%08x 0x%08x\n
WiFi
%s::%s: super init failed \n
ClientOpen_block_invoke
WR
%s::%s: failed to copy reset block \n
flrCountDict->setObject(kCentauriFLRCount, flrCountObject)
%06llu.%06llu CollectLogs Start 0x%04x %s\n
MemSwapWorkingCopy.bin
Invalid
%s::%s: invalid parameters \n
LoggingProperties
flrCount && *flrCount
UnexpectedDextTermination
CancelDeferredWork
msi-reservation-size
LogCollection
OSAction_CentauriSubsystem_CollectLogsCallback
PrepareForReset
ivars->logCollectionInfo.completion
true
%s::%s: current timestamp is older than last reset timestamp, ignoring \n
%s::%s: failed to set dict object for StateDump \n
prepareForResetEnd
CentauriControlRemoteInterface
errorData->isWrite < 2
%s::%s: invalid client \n
CollectChipInfo
UnexpectedDextTermination-UserspaceReboot
%s::%s: MSICapOffset::%llx \n
CancelPrepareForResetHandler_block_invoke
SetErrorHandler
%s::%s: invalid memswap DMA command \n
%s::%s: pmcsr 0x%04x \n
%s::%s: error source not found for %s \n
%s::%s: unexpected coredump completion \n
%s::%s: invalid length (working copy %llu t0 %llu) \n
WaitForReadyForReset
dataObject->getLength() == sizeof(uint32_t)
ReadMSIData
readData
ReportError
NewUserClient_Impl
%s::%s: coredump/crashlog completion failed (ret=0x%x) \n
%s::%s: cachedErrorCount: %u \n
%s::%s: Crashlog Reason: \"%s\" \n
IsBackToBack
CancelCrashlogHandler
no
%s::%s: LPM log collection mode unsupported \n
CentauriPowerStateLog.txt
%s::%s: device id: 0x%x \n
GetNumMSIVectorsRequested
%s::%s: failed to create chip reset os action (ret = 0x%x) \n
prepareChipForResetEnd
PreBoot
ivars->inFlightWork > 0
%s::%s: failed to set properties (ret = 0x%x) \n
%s::%s: full chip reset in progress \n
ResetDone
%s::%s: invalid state for log collection %u \n
EnablePTMOnEndpoint
isASPMEnabled
CentauriDebug
%s::%s: handler already exists \n
ChipResetCallback_Impl
%s::%s: failed to create working copy IOBMD (ret = 0x%x) \n
%s::%s: failed to set SS ID object \n
fLock
coredumpEnd
coredumpStart
!ivars->crashlogHandler
Yes
%s::%s: error handler not registered \n
CancelErrorHandler
%s::%s: failed to create function name copy \n
Fiq
TriggerPanic
%s::%s: failed to copy collectLogs block \n
%06llu.%06llu 0x%x\n
CentauriMemoryAccessLog.txt
SetDextRecoveryState_block_invoke
%s::%s: failed to validate segment length (ret = 0x%x expected %llu got %llu) \n
FetchMemSwap
%s::%s: invalid number of MSIs requested: %u available: %u \n
%s::%s: FLR limit override boot-arg is set \n
TriggerClientLaunch
%s::%s: requesting full wake \n
%s::%s: error reported by %s error code %u \n
CollectLogsCallback_Impl
%s::%s: in low power \n
%s::%s: reset failed (ret = 0x%x) \n
%s::%s: failed to create timer src (ret = 0x%x) \n
ivars->timerSource
%06llu.%06llu CollectLogs Complete ret: 0x%03x\n
%s::%s: invalid length \n
%s::%s: driver %s - ignoring MSI notification \n
%s::%s: MSI handler: boot stage = %u \n
%s::%s: signature mismatch \n
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x \n
%s::%s: failed to create IODMACommand (ret = 0x%x) \n
%s::%s: failed to prepare for DMA (ret = 0x%x) \n
%s::%s: invalid segment info (addr: 0x%qx len: 0x%qx) \n
%s::%s: termination notification for AirshipDriverDK
%s::%s: cachedErrorCount: %u
%s::%s: failed to set enable int source (ret = 0x%x)
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu
%s::%s: invalid number of MSIs requested: %u available: %u
%s::%s: log collection in progress/enqueued
%s::%s: failed to create pci error queue (ret = 0x%x)
%s::%s: release PM assertion
%s::%s: %u
%s::%s: logpipe: failed to copy log identifier %s
%s::%s: finalize %d
%s::%s: error arg not an OSNumber
%s::%s: failed to schedule immediate wake
%s::%s: failed to create reason string copy
%s::%s: failed to create osdata object
%s::%s: failed to set dict object
%s::%s: failed to get owner object
%s::%s: failed to update the FW crash reason string
%s::%s: failed to get default queue (ret = 0x%x)
%s::%s: FLR limit override boot-arg is set
%s::%s: error handler not registered
%s::%s: ret = 0x%x
%s::%s: warning: prepare for reset handler is not registered
%s::%s: crashlog handler is not registered
%s::%s: failed to get airship probe result
%s::%s: boot stage: %s, fw state: %s
%s::%s: failed to copy properties
%s::%s: failed to create log pipe with provider %s
%s::%s: SetProperties failed
%s::%s: failed to set properties (ret = 0x%x)
%s::%s: invalid input dictionary - bailing out
%s::%s: number of MSIs requested: %u
%s::%s: failed to open IOPCIDevice (ret = 0x%x)
%s::%s: pmcsr 0x%04x
%s::%s: testID: %u
%s::%s: error appending bytes to bufferObject
%s::%s: buffer filled, totalBytesPrinted: %u bufferSize: %u
%s::%s: failed to create IODMACommand (ret = 0x%x)
%s::%s: timer expired waiting for memswap info in dext crash recovery state
%s::%s: module name not found
%s::%s: match notification for AirshipDriverDK
%s::%s: Close ret = 0x%x
%s::%s: remote interface error (ret = 0x%x)
%s::%s: state %u
%s::%s: clearing cfg mbx at offset 0x%x
%s::%s: failed to get the fault reporter additional owner
%s::%s: failed to allocate inFlightLock
%s::%s: not permitted for ss id %u
%s::%s: log collection failed (ret=0x%x)
%s::%s: failed to copy completion block
%s::%s: logger not available
%s::%s: failed to get logging properties dict
%s::%s: added file %s, size %zu
%s::%s: unexpected termination notification
%s::%s: failed to set airship driver config
%s::%s: error handler has been deregistered
%s::%s: function reset already in progress
%s::%s: deferring (state = 0x%x)
%s::%s: requesting crashlog failed (ret=0x%x)
%s::%s: failed to validate segment length (ret = 0x%x expected %llu got %llu)
%s::%s: failed to find aer capability (ret = 0x%x)
%s::%s: 
%s::%s: bad arg
%s::%s: invalid bootstage 0x%x
%s::%s: failed to alloc OSNumber for up time
%s::%s: error filling buffer, bytesPrinted: %d kLineLength: %u
%s::%s: device control reg val: 0x%x
%s::%s: logpipe: failed to copy directory name %s
%s::%s: no crashlog handler
%s::%s: failed to create error event action ret = 0x%x
%s::%s: failed to create os action for watchdog notification (ret = 0x%x)
%s::%s: coredump/crashlog completion failed (ret=0x%x)
%s::%s: failed to create timer src (ret = 0x%x)
%s::%s: replacing existing client
%s::%s: failed to set os action handler (ret = 0x%x)
%s::%s: airship reported error: 0x%x
%s::%s: new exec stage: %u
%s::%s: invalid state for watchdog notification: %u
%s::%s: memory allocation crashlog reason string failed
%s::%s: failed to get log file name
%s::%s: invalid viddid
%s::%s: failed to get addr range (ret = 0x%x)
%s::%s: failed to allocate memory
%s::%s: timer expired waiting for remote service in dext crash recovery state
%s::%s: block copy failed
%s::%s: invalid cmd id: %u
%s::%s: unexpected crash log completion
%s::%s: failed to alloc OSNumber for SS ID
%s::%s: failed to create function name copy
%s::%s: crashlog too small: %zu bytes
%s::%s: driver offline - ignoring exec stage notification
%s::%s: driver offline
%s::%s: Stop ret = 0x%x
%s::%s: unexpected coredump completion
%s::%s: full chip reset in progress
%s::%s: reset already enqueued
%s::%s: failed to allocate OSData
%s::%s: invalid crash log buffer
%s::%s: failed to allocate lock
%s::%s: data::%x
%s::%s: datapipe: failed to copy directory name %s
%s::%s: driver offline (state = %u)
%s::%s: service notification (type: %llu)
%s::%s: failed to create completion os action (ret = 0x%x)
%s::%s: invalid client
%s::%s: completion
%s::%s: options 0x%x reason %s
%s::%s: %s
%s::%s: invalid metadata dict
%s::%s: failed to report error (ret = 0x%x)
%s::%s: lpw -> on
%s::%s: remote service unavailable. wait for %u ms
%s::%s: failed to get user client service
%s::%s: failed to allocate pending work item
%s::%s: crashlog size larger than buffer (%zu > %zu)
%s::%s: skipping %s
%s::%s: termination notification for CentauriRemoteInterface
%s::%s: memswap memory map is already set
%s::%s: failed to set boot complete property (ret = 0x%x)
%s::%s: failed to create osdict
%s::%s: bad arguments
%s::%s: invalid segment count %u
%s::%s: invalid memswap DMA command
%s::%s: section too small
%s::%s: %s property exists - skipping dext crash
%s::%s: bad max size
%s::%s: resuming fatal log collection (state = 0x%x)
%s::%s: ptm requester role not supported
%s::%s: MSICapOffset::%llx
%s::%s: Invalid segmentName or segmentDump observed
%s::%s: failed to copy block
%s::%s: failed to set dict object for %s
%s::%s: number of crashlogs: %u
%s::%s: failed to create chip object for family %u
%s::%s: centauri-driverkit=0
%s::%s: didDextRelaunch = %s (reason %u)
%s::%s: failed to create timer action (ret = 0x%x)
%s::%s: invalid notifier
%s::%s: ready for reset timed out
%s::%s: failed to create dispatch src (ret = 0x%x)
%s::%s: offline
%s::%s: powerFlags: %u
%s::%s: invalid segment info (addr: 0x%qx len: 0x%qx)
%s::%s: sleeping for %u ms...
%s::%s: propertyUpdateNotification handler not registered
%s::%s: FLR limit (%u) reached
%s::%s: failed to set up time object
%s::%s: failed to allocate statedump buffer
%s::%s: initialized MSI-1
%s::%s: ptm enabled, clock granularity: %u ns
%s::%s: crash log buffer too small: %zu bytes
%s::%s: failed to copy service name (ret = 0x%x)
%s::%s: deferring reset
%s::%s: prepare for reset handler is not registered
%s::%s: failed to get logger
%s::%s: Open error (ret = 0x%x)
%s::%s: invalid length (working copy %llu t0 %llu)
%s::%s: invalid state for log collection %u
%s::%s: failed to find ptm capability (ret = 0x%x)
%s::%s: errorSource: %u, errorCode: %u, arg: 0x%llx
%s::%s: first power on
%s::%s: requesting coredump failed (ret=0x%x)
%s::%s: failed to get IOPCIDevice
%s::%s: Using FLR limit: %u
%s::%s: powerFlags: %s
%s::%s: failed to create file name copy
%s::%s: Crashlog Reason: \"%s\"
%s::%s: fault reporter is busy
%s::%s: failed to SaveDeviceState (ret = 0x%x)
%s::%s: log collection already enqueued
%s::%s: failed to copy collectLogs block
%s::%s: airship not up; returning %s
%s::%s: pci device not open
%s::%s: failed to copy deferredCb block
%s::%s: driver offline - ignoring airship error notification
%s::%s: failed to create os action for collect logs (ret = 0x%x)
%s::%s: failed to alloc dict
%s::%s: failed to allocate metadata dict
%s::%s: FLR timed out
%s::%s: super init failed
%s::%s: stream: failed to copy log identifier %s
%s::%s: ASPM state: %u
%s::%s: invalid state (%s)
%s::%s: failed to set real time object
%s::%s: invalid number of MSIs requested: %u
%s::%s: failed to create data log pipe
%s::%s: failed to set require client property (ret = 0x%x)
%s::%s: invalid state (%u)
%s::%s: failed to RestoreDeviceState (ret = 0x%x)
%s::%s: invalid parameters
%s::%s: failed to get logging properties object
%s::%s: logger not ready
%s::%s: failed to create logger queue (ret = 0x%x)
%s::%s: chip crash timed out
%s::%s: failed to alloc metadata
%s::%s: invalid length
%s::%s: failed to copy completionCb block
%s::%s: failed to create airship transport
%s::%s: failed to configure interrupts (ret = 0x%x)
%s::%s: failed to create reset timestamps dict
%s::%s: failed to set reason object
%s::%s: current timestamp is older than last reset timestamp, ignoring
%s::%s: failed to create fault reporter
%s::%s: escalate FLR failure
%s::%s: ErrorDetected's value type is not a dictionary
%s::%s: failed to create memory map (ret = 0x%x)
%s::%s: invalid link control value
%s::%s: failed to send %s (ret=0x%x)
%s::%s: airship reported fatal error: %s
%s::%s: failed to create osdata object for StateDump
%s::%s: empty crash log buffer
%s::%s: failed to enable timer (ret = 0x%x)
%s::%s: invalid state for reset %u
%s::%s: failed to alloc OSNumber for monotonic time
%s::%s: ret: 0x%x flags: 0x%qx cnt: %d addr: 0x%qx len: 0x%qx
%s::%s: handler already exists
%s::%s: crash poll iterations = %u
%s::%s: crashlog header reports empty: %zu bytes
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x
%s::%s: failed to copy immediateCb block
%s::%s: invalid queue
%s::%s: failed to get MSI data (ret = 0x%x)
%s::%s: client: %s
%s::%s: client already registered (%s)
%s::%s: found crashlog data for %s
%s::%s: invalid filename/statedump
%s::%s: returned from SetProperties (ret = 0x%x)
%s::%s: failed to create reset state item (ret=0x%x)
%s::%s: requesting deferral (low power: %u, defer for memswap: %s)
%s::%s: LPM log collection mode unsupported
%s::%s: reset failed (ret = 0x%x)
%s::%s: failed to get provider queue
%s::%s: failed to copy system state service (ret = 0x%x)
%s::%s: ignoring based on boot-arg
%s::%s: airship service not ready
%s::%s: failed to alloc OSString
%s::%s: PCI dart error %u: [%s] addressLo: 0x%x addressHi: 0x%x
%s::%s: boot stage = %s
%s::%s: failed to find PCI capability (ret = 0x%x)
%s::%s: FLR timeout override: %u ms
%s::%s: AppleCentauriManager::Open failed (ret = 0x%x)
%s::%s: failed to set dext relaunch property (ret = 0x%x)
%s::%s: timer expired waiting for remote service in reset failed state
%s::%s: dispatching propertyUpdateNotification
%s::%s: device id: 0x%x
%s::%s: signature mismatch
%s::%s: no prepare for reset handler
%s::%s: failed super Start (ret = 0x%x)
%s::%s: bad args
%s::%s: reserved MSIs via provider
%s::%s: pci read invalid data
%s::%s: failed to get dir name
%s::%s: failed to get MSI addr (ret = 0x%x)
%s::%s: GetBusyState ret = 0x%x
%s::%s: Driver offline. Ignoring state change %u
%s::%s: not permitted
%s::%s: invalid viddid 0x%x
%s::%s: no ptm key - bailing out
%s::%s: error handler already exists
%s::%s: deferring due to low power
%s::%s: unexpected match notification
%s::%s: service matching set up for %s
%s::%s: bad size (got %u max %u)
%s::%s: failed to alloc OSNumber for real time
%s::%s: fw crash reason string is not supported with non-fatal log collection
%s::%s: failed to set dict object for StateDump
%s::%s: failed to prepare for DMA (ret = 0x%x)
%s::%s: invalid crashlog data
%s::%s: deliver notification error (ret = 0x%x)
%s::%s: error source %u code %u arg %llu
%s::%s: invalid driver state %u for dext crash recovery state %u
%s::%s: driver %s - ignoring MSI notification
%s::%s: failed to create log stream
%s::%s: failed to create data log stream
%s::%s: cached crashlogs not available
%s::%s: failed to create dict
%s::%s: driver offline - ignoring airship fatal error notification
%s::%s: failed to create memswap os action (ret = 0x%x)
%s::%s: error source not found for %s
%s::%s: working copy content: 0x%x len: %llu
%s::%s: log collection failed (ret = 0x%x)
%s::%s: invalid callback parameters
%s::%s: failed to set ptm status in subsystem properties (ret = 0x%x)
%s::%s: failed to create chip reset os action (ret = 0x%x)
%s::%s: power assertion already held
%s::%s: poll count %u
%s::%s: selector %llu
%s::%s: failed to get platform (ret = 0x%x)
%s::%s: failed to set SS ID object
%s::%s: logpipe: failed to copy file name %s
%s::%s: failed to get provider
%s::%s: resuming reset (state = 0x%x)
%s::%s: using cc log level %u
%s::%s: Logging prop: owner: %s dir: %s file: %s id: %s
%s::%s: errorCode %u, reason %s
%s::%s: failed HasPCIPowerManagement (ret = 0x%x)
%s::%s: deferred work is canceled
%s::%s: failed to copy reset block
%s::%s: boot stage = ready for reset
%s::%s: failed to create osdata object for %s
%s::%s: invalid number of MSIs configured: %u
%s::%s: FLR count: %u
%s::%s: chip class not initialized
%s::%s: failed to create os action (ret = 0x%x)
%s::%s: state = %u
%s::%s: failed to remove property (ret = 0x%x)
%s::%s: MSI handler: boot stage = %u
%s::%s: failed to copy provider properties
%s::%s: failed to find MSI property
%s::%s: caching crashlog
%s::%s: failed to  SearchProperty (ret = 0x%x)
%s::%s: failed to create user client (ret = 0x%x)
%s::%s: in low power
%s::%s: failed to create working copy IOBMD (ret = 0x%x)
%s::%s: failed to find msi capability (ret = 0x%x)
%s::%s: msiaddr::%llx
%s::%s: failed to copy prepareCb block
%s::%s: failed to EnablePCIPowerManagement (ret = 0x%x)
%s::%s: failed to create user class dict
%s::%s: failed to save timestamp
%s::%s: failed to serialize
%s::%s: failed to create msi interrupt source (ret = 0x%x)
%s::%s: using console log level %u
%s::%s: failed to get log id
%s::%s: Invalid coreName or crashlogData observed
%s::%s: skipping during dext crash recovery
%s::%s: error reported by %s error code %u
%s::%s: invalid fault reporter
%s::%s: failed to save FLR timestamps
%s::%s: reset in progress. ignoring error
%s::%s: dispatching cached errors
%s::%s: cmd id %u ret 0x%x
%s::%s: remote interface unavailable
%s::%s: memswap memory is already DART mapped
%s::%s: failed to set monotonic time object
%s::%s: failed to trigger fault report (ret = 0x%x)
%s::%s: number of MSIs requested: %u (SingleMSI mode)
%s::%s: match notification for CentauriRemoteInterface
%s::%s: error code not found
%s::%s: PCI dart error
%s::%s: in fatal error state (%u)
%s::%s: tp poll count %u
%s::%s: Crashlog Reason not found from the Crashlog data
%s::%s: requesting full wake
%s::%s: Transaction pending poll timed out. Proceeding to FLR
%s::%s: provider not available
%s::%s: invalid memswap map or working copy desc
```
