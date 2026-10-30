# `/System/DriverKit/System/Library/PrivateFrameworks/CentauriBeta.framework/CentauriBeta`

From the upgrade restore ramdisk (141-29011-104.dmg). 450,880 bytes.

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
centauri-driverkit
%s::%s: memswap memory is already DART mapped \n
%s::%s: failed to set monotonic time object \n
%s::%s: log collection in progress/enqueued \n
%s::%s: failed to get provider queue \n
%s::%s: failed to get logging properties object \n
ivars->queue->OnQueue()
%s::%s: returned from SetProperties (ret = 0x%x) \n
val && ivars->resetTimestamps->setObject(eventName, val)
coredumpEnd
%s::%s: unexpected match notification \n
%s::%s: failed to create chip object for family %u \n
%s::%s: working copy content: 0x%x len: %llu \n
!ivars->logCollectionInfo.metadata && !ivars->logCollectionInfo.completion
true
item->block
Recovery
kCentauriBetaMemswapTimeoutErrorKey
%s::%s: selector %llu \n
B24@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}16
%s::%s: failed to get default queue (ret = 0x%x) \n
%s::%s: failed HasPCIPowerManagement (ret = 0x%x) \n
centauri-flr-limit
ivars->timerAction
%s::%s: in low power \n
%06llu.%06llu 0x%08llx %s 0x%08x\n
serializedBuffer && serializedLength
%s::%s: failed to allocate pending work item \n
EnqueueDeferredWork
%s::%s: pci device not open \n
Unknown
OSAction_CentauriSubsystem_CentauriManagerErrorHandler
%s::%s: invalid state (%s) \n
%s::%s: invalid cmd id: %u \n
%s::%s: boot stage: %s, fw state: %s \n
%s::%s: cachedErrorCount: %u \n
%s::%s: invalid segment info (addr: 0x%qx len: 0x%qx) \n
CentauriUserClientProperties
%s::%s: failed to create user client (ret = 0x%x) \n
CollectEventLog
    crashlogPending: %d\n
SetDextRecoveryState
centauri-flr-timeout-ms
%s::%s: FLR timed out \n
derivedStart
%s::%s: failed to get log file name \n
%s::%s: new exec stage: %u \n
SetState
%s::%s: state = %u \n
%s::%s: not permitted \n
%s::%s: unexpected crash log completion \n
%s::%s: failed to set dict object \n
%s::%s: failed to create data log pipe \n
pci-get-dart-error
null
%s::%s: cached crashlogs not available \n
UnexpectedDextTermination
%s::%s: initialized MSI-1 \n
MaskUnsupportedRequestAER
%s::%s: invalid crash log buffer \n
%s::%s: failed to copy prepareCb block \n
i40@?0^^{OSDictionary}8^^{OSDictionary}16^^{OSDictionary}24^^{OSString}32
SetupServiceMatchingNotification
%s::%s: failed to set os action handler (ret = 0x%x) \n
TriggerClientLaunch() == kIOReturnSuccess
IOPCIPMCSState
%s::%s: invalid input dictionary - bailing out \n
InitMemSwapWorkingCopy
%s::%s: Using FLR limit: %u \n
%s::%s: failed to create dispatch src (ret = 0x%x) \n
PrepareChipForReset
%s::%s: FLR limit (%u) reached \n
%s::%s: fw crash reason string is not supported with non-fatal log collection \n
CentauriMSILog.txt
    coredumpPending: %d\n
%s::%s: resuming fatal log collection (state = 0x%x) \n
%s::%s: failed to get IOPCIDevice \n
PartiallyBooted
%s::%s: resuming reset (state = 0x%x) \n
%s::%s: invalid number of MSIs configured: %u \n
Boot
v12@?0i8
CentauriStateDump.txt
GetCrashlogs
Idle
LogCollection
LPW
%s::%s: failed to create dict \n
CollectLogsCallback_Impl_block_invoke
%s::%s: requesting deferral (low power: %u, defer for memswap: %s) \n
OSAction_CentauriSubsystem_MemSwapCallback
OSAction_CentauriSubsystem_WatchdogCallback
com.apple.centauri.reset.bluetooth
%s::%s: SetProperties failed \n
%s::%s: cmd id %u ret 0x%x \n
WatchdogCallback_Impl_block_invoke
CollectLogsFatal_block_invoke
ivars->logCollectionInfo.metadata
%s::%s: ASPM state: %u \n
waitingForReadyForReset
%s::%s: failed to create pci error queue (ret = 0x%x) \n
%s::%s: dispatching cached errors \n
ivars->state == kCentauriStateLogCollection
flrCountDict->setObject(kCentauriFLRCount, flrCountObject)
ClearUnsupportedRequestAER
startTimeObject && endTimeObject
Reset
time          flags\n
crashlogStart
%s::%s: failed to create reset state item (ret=0x%x) \n
%s::%s: deferring (state = 0x%x) \n
time          r/w address    value\n
%s::%s: failed to find MSI property \n
resetStart
setFLRBit
%s::%s: failed to set SS ID object \n
ErrorArg
CompleteFaultReportCb
ReportError
%s::%s: failed to create file name copy \n
CollectConfigLogs
%s::%s: failed to create msi interrupt source (ret = 0x%x) \n
AppleCentauriManager::SaveClientProperty(this, key, newValue, kCentauriAutoClearOnChipReset) == kIOReturnSuccess
%s::%s: failed super Start (ret = 0x%x) \n
(null)
%s::%s: failed to create timer src (ret = 0x%x) \n
v32@?0Q8^{IOService=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})}16Q24
ChangePowerState(kIOServicePowerCapabilityOn) == kIOReturnSuccess
ClientClose
%s::%s: failed to find PCI capability (ret = 0x%x) \n
ServiceNotificationReady_Impl_block_invoke
%s::%s: power assertion already held \n
%s::%s: testID: %u \n
%s::%s: failed to set dict object for StateDump \n
%s::%s: failed to set enable int source (ret = 0x%x) \n
%s::%s: device control reg val: 0x%x \n
TriggerPanic
%s::%s: client already registered (%s) \n
%s::%s: ready for reset timed out \n
%s::%s: failed to set up time object \n
action == ivars->msiAction
%s::%s: data::%x \n
ModuleName
Crashlog
/Library/Caches/com.apple.xbs/558FE645-4E39-4399-A06E-8DC20AC536F1/TemporaryDirectory.VSeWMb/Sources/AppleCentauri_driverkit/CentauriSubsystem/CentauriSubsystem.cpp
%s::%s: failed to get log id \n
WR
CollectLogs_block_invoke
%06llu.%06llu SaveDeviceState ret: 0x%03x\n
ROM
%s::%s: driver %s - ignoring MSI notification \n
eventNameObject
CollectImmediateFaultDataCb
%s::%s: error source %u code %u arg %llu \n
CollectLogsStateDumps
AbortHandler
PartiallyBootedLPM
OSAction_CentauriSubsystem_ChipResetCallback
%s::%s:  \n
%s::%s: failed to create log pipe with provider %s \n
%s::%s: driver offline \n
NotifyPropertyUpdate
%s::%s: invalid state for log collection %u \n
FetchMemSwap
OS
%s::%s: log collection failed (ret=0x%x) \n
flrCountObject != nullptr
%s::%s: match notification for AirshipDriverDK \n
CreateChipObject
%s::%s: failed to get user client service \n
OSAction_CentauriSubsystem_ServiceNotificationReady
ivars->dextRecoveryState == kCentauriDextRecoveryStateFetchMemSwap
%s::%s: deferring reset \n
dextRelaunchObj != nullptr
newValue
key && dict
DirectoryName
%s::%s: remote service unavailable. wait for %u ms \n
%s::%s: module name not found \n
CancelErrorHandler
%s::%s: failed to alloc metadata \n
CancelDeferredWork
ClearConfigSpaceMailboxes
IsBackToBack
SetPowerOverride(true) == kIOReturnSuccess
no
%s::%s: failed to copy collectLogs block \n
remoteService: %s\n
%s::%s: sleeping for %u ms... \n
OpenRemoteService
%s::%s: failed to copy service name (ret = 0x%x) \n
!ivars->inLowPower
%s::%s: boot stage = ready for reset \n
%s::%s: failed to alloc OSNumber for SS ID \n
%s::%s: failed to enable timer (ret = 0x%x) \n
%s::%s: errorSource: %u, errorCode: %u, arg: 0x%llx \n
false
%s::%s: failed to alloc dict \n
AirshipDriverConfigName
%s::%s: invalid state (%u) \n
%s::%s: log collection failed (ret = 0x%x) \n
ReadMSIAddr
%s::%s: invalid callback parameters \n
CollectDeferredFaultDataCb
Stop_Impl_block_invoke
%s::%s: failed to report error (ret = 0x%x) \n
blockCopy
AppleCentauri-129
logCollectionInfo:\n
DerivedLogState
dict->setObject(key, kOSBooleanTrue)
ResetDone
%s::%s: in fatal error state (%u) \n
TimeToTriggerCollectLogs
%s::%s: failed to create logger queue (ret = 0x%x) \n
%s::%s: driver offline - ignoring exec stage notification \n
%s::%s: ErrorDetected's value type is not a dictionary \n
yes
DeferReset
oldValue != nullptr
%s::%s: FLR timeout override: %u ms \n
BootComplete
%s::%s: failed to allocate lock \n
%s::%s: failed to set airship driver config \n
%s::%s: invalid state for reset %u \n
%s::%s: deferring due to low power \n
%s::%s: full chip reset in progress \n
%s::%s: failed to allocate metadata dict \n
name
%s::%s: using cc log level %u \n
%s::%s: failed to get the fault reporter additional owner \n
%s::%s: failed to EnablePCIPowerManagement (ret = 0x%x) \n
%s::%s: failed to create reset timestamps dict \n
%s::%s: FLR count: %u \n
%s::%s: LPM log collection mode unsupported \n
%s::%s: reset failed (ret = 0x%x) \n
%s::%s: ret: 0x%x flags: 0x%qx cnt: %d addr: 0x%qx len: 0x%qx \n
%s::%s: service matching set up for %s \n
ExecStageChanged
ivars->cachedErrorsArray
ExitLPW
length < sizeof(configName)
%s::%s: handler already exists \n
PrepareForReset
flrCount && *flrCount
%s::%s: stream: failed to copy log identifier %s \n
%s::%s: invalid number of MSIs requested: %u available: %u \n
%s::%s: failed to save timestamp \n
userClient
%s::%s: failed to remove property (ret = 0x%x) \n
%s::%s: invalid client \n
%s::%s: failed to copy provider properties \n
%s::%s: reserved MSIs via provider \n
%s::%s: datapipe: failed to copy directory name %s \n
%s::%s: failed to get MSI addr (ret = 0x%x) \n
RegisterServiceOrStartDextRecovery_block_invoke
%s::%s: %u \n
%s::%s: failed to set dict object for %s \n
%s::%s: MSI handler: boot stage = %u \n
%s::%s: memory allocation crashlog reason string failed \n
BT
%s::%s: failed to create fault reporter \n
%s::%s: errorCode %u, reason %s \n
%s::%s: failed to  SearchProperty (ret = 0x%x) \n
SetPropertyUpdateNotificationHandler
time          offset     r/w data\n
EnablePTMOnEndpoint
%s::%s: ptm enabled, clock granularity: %u ns \n
OSAction_CentauriSubsystem_InterruptOccurred
LogIdentifier
%s::%s: invalid filename/statedump \n
Yes
WatchdogCallback_Impl
%s::%s: invalid crashlog data \n
FaultReporter
dict && dict->setObject(kCentauriPropertyUnexpectedDextTermination, (ivars->dextRelaunchReason == kCentauriManagerDextRelaunchReasonCrash) ? kOSBooleanTrue : kOSBooleanFalse)
ivars->cachedErrorsArray->setObject(cachedError)
%s::%s: block copy failed \n
%s::%s: client: %s \n
SetupMemSwapRegion
%s::%s: crash poll iterations = %u \n
%06llu.%06llu SetBusLeadEnable Start enable: %s\n
%s::%s: invalid state for watchdog notification: %u \n
CreateMetadataDict
ivars->logCollectionInfo.completion
CentauriConfigAccessLog.txt
On
%s::%s: GetBusyState ret = 0x%x \n
%s::%s: termination notification for AirshipDriverDK \n
centauri-recovery
handler
SendAnalytics
Offline
coredumpStart
TriggerClientLaunch
CollectLogsCallback_Impl
%s::%s: failed to alloc OSNumber for up time \n
%s::%s: failed to copy block \n
%06llu.%06llu SetupMemSwapRegion ret: 0x%03x\n
Coredump
LPMBoot
%s::%s: logpipe: failed to copy directory name %s \n
%s::%s: number of MSIs requested: %u (SingleMSI mode) \n
dict->setObject(kCentauriSystemStateNotificationResetKey, kOSBooleanTrue)
%s::%s: requesting crashlog failed (ret=0x%x) \n
%s::%s: invalid driver state %u for dext crash recovery state %u \n
ReadyForResetDuration
%s::%s: buffer filled, totalBytesPrinted: %u bufferSize: %u \n
%s::%s: logpipe: failed to copy log identifier %s \n
ivars->loggerQueue->OnQueue()
centauri-fatal-err-panic
ivars->finalizeHandler
%s::%s: chip crash timed out \n
SetPowerState_Impl
%s::%s: invalid viddid 0x%x \n
%s::%s: failed to set real time object \n
data
%s::%s: %s \n
%s::%s: failed to send %s (ret=0x%x) \n
SubsystemID
Reason
v8@?0
CollectLogs
val
test
MemSwapCallback_Impl
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu \n
Crashlog.CTRL.bin
dict && dict->setObject(\"RequireClient\", kOSBooleanTrue)
%s::%s: timer expired waiting for remote service in dext crash recovery state \n
%s::%s: timer expired waiting for memswap info in dext crash recovery state \n
%s::%s: pci read invalid data \n
Crashlog.BTMAIN.bin
RequireClient
com.apple.queue.centauri-pcierrors
%s::%s: Open error (ret = 0x%x) \n
SetupRemoteActionCallbacks
CollectAirshipStateDumps
CollectMSILog
flrLimit: %d\n
CollectChipInfo
%s::%s: caching crashlog \n
Invalid
%s::%s: ret = 0x%x \n
%s::%s: finalize %d \n
CheckErrorPolicyForKey
%s::%s: options 0x%x reason %s \n
ivars->cachedCrashlogsArray->getCount() > 0
prevState == kCentauriDextRecoveryStateCollectLogs
StateSnapshots
%s::%s: failed to update the FW crash reason string \n
errorInfo
MSI-2
readData
crashlogEnd
%s::%s: failed to copy deferredCb block \n
RD
WaitForReadyForReset
CoredumpDuration
ret == kIOReturnSuccess
ivars->clientName
%s::%s: remote interface error (ret = 0x%x) \n
version: %s\n
%s::%s: ptm requester role not supported \n
UpTimestamp
%s::%s: failed to copy properties \n
LoggingProperties
%s::%s: failed to create data log stream \n
PrepareFaultReportCb
ResetCompletion
AirshipStateDump.bin
CollectMemoryLog
%s::%s: failed to serialize \n
%s::%s: driver offline - ignoring airship error notification \n
%s::%s: driver offline - ignoring airship fatal error notification \n
LPMOS
%s::%s: logpipe: failed to copy file name %s \n
%s::%s: airship reported fatal error: %s \n
execStage <= kCentauriBootStageMax
%s::%s: error code not found \n
%s::%s: failed to alloc OSString \n
ivars->cachedCrashlogsArray->setObject(copy)
%s::%s: bad arguments \n
%s::%s: using console log level %u \n
ivars->inFlightWork < UINT32_MAX
%s::%s: failed to create memswap os action (ret = 0x%x) \n
%s::%s: powerFlags: %u \n
inLowPower: %d\n
%s::%s: failed to allocate OSData \n
%s::%s: invalid length \n
%s::%s: number of MSIs requested: %u \n
SetIPCProperties
flrCountDict
%s::%s: failed to create osdict \n
prepareChipForResetStart
%s::%s: failed to get airship probe result \n
%s::%s: hint: %u \n
%s::%s: not permitted for ss id %u \n
%s::%s: chip class not initialized \n
%s::%s: failed to set reason object \n
[NonFatal]
%s::%s: bad size (got %u max %u) \n
prevState == kCentauriDextRecoveryStateIdle
free
%s::%s: failed to allocate inFlightLock \n
%s::%s: failed to create os action for watchdog notification (ret = 0x%x) \n
EnqueueDeferredWork(blockCopy, kCentauriDeferredWorkTypeOther)
SendTimeSinceLastFLRAnalytics
TimeToOSBootStage
%s::%s: Logging prop: owner: %s dir: %s file: %s id: %s \n
%s::%s: failed to allocate memory \n
%s::%s: failed to open IOPCIDevice (ret = 0x%x) \n
CopyName(&serviceName) == kIOReturnSuccess
%s::%s: timer expired waiting for remote service in reset failed state \n
dict && dict->setObject(kCentauriPropertyBootComplete, kOSBooleanTrue)
completionCopy
CollectPowerStateLog
%s::%s: failed to create airship transport \n
%s::%s: invalid viddid \n
EndWork
cachedError->getLength() == sizeof(CentauriCachedErrorInfo)
%s::%s: propertyUpdateNotification handler not registered \n
%s::%s: coredump/crashlog completion failed (ret=0x%x) \n
%s::%s: failed to create osdata object for StateDump \n
copy
%s::%s: FLR limit override boot-arg is set \n
%s::%s: failed to set boot complete property (ret = 0x%x) \n
%s::%s: bad max size \n
state: %s\n
prevState == kCentauriDextRecoveryStateIdle || prevState == kCentauriDextRecoveryStateWaitForRemote
%s::%s: failed to prepare for DMA (ret = 0x%x) \n
TimeElapsed
RealTimestamp
%s::%s: super init failed \n
errorData
%s::%s: invalid memswap map or working copy desc \n
 w 
airshipService: %s\n
SetDextRecoveryState_block_invoke
offline
%s::%s: Crashlog Reason not found from the Crashlog data \n
Default
%s::%s: Driver offline. Ignoring state change %u \n
%s::%s: error arg not an OSNumber \n
%s::%s: error handler has been deregistered \n
!ivars->deferredWork.reset
%s::%s: device id: 0x%x \n
%s::%s: MSICapOffset::%llx \n
fLock
v24@?0I8I12^v16
%s::%s: failed to set require client property (ret = 0x%x) \n
ctx
%s::%s: failed to set properties (ret = 0x%x) \n
%s::%s: log collection already enqueued \n
RestoreDeviceState
%s::%s: poll count %u \n
%s::%s: section too small \n
ivars->memSwapAction && ivars->completionAction && ivars->chipResetAction && ivars->collectLogsAction && ivars->watchdogAction
SetErrorHandler
%s::%s: driver offline (state = %u) \n
%s::%s: failed to create working copy IOBMD (ret = 0x%x) \n
fatal
FLRDuration
SetPTMProperty
%s::%s: memswap memory map is already set \n
nonfatal
WiFi
fwCrashReported
centauri-allow-panic
WaitForPCIErrorNotifications
address && length && coredump
subsystemNameObject
ErrorCode
PreBoot
DextRelaunchState
%s::%s: boot stage = %s \n
MSI-1
%s::%s: failed to create IODMACommand (ret = 0x%x) \n
%s::%s: invalid number of MSIs requested: %u \n
readyForReset
Stop
%s::%s: failed to create memory map (ret = 0x%x) \n
%s::%s: failed to copy completion block \n
%s::%s: failed to get provider \n
PTM
ClientOpen
%06llu.%06llu CollectLogs Start 0x%04x %s\n
CentauriMemoryAccessLog.txt
%s::%s: number of crashlogs: %u \n
GetCachedErrorCount
CentauriDebug
prepareChipForResetEnd
Control
%s::%s: failed to create user class dict \n
%s::%s: remote interface unavailable \n
%s::%s: empty crash log buffer \n
t2026
AdditionalPipeOwners
key
%s
%s::%s: reset in progress. ignoring error \n
CreateSystemStateNotificationItems
CollectStateSnapshots
ExtractCrashlogReason
LogFileName
%s::%s: Invalid coreName or crashlogData observed \n
%s::%s: airship reported error: 0x%x \n
%s::%s: lpw -> on \n
%s::%s: unexpected coredump completion \n
ChipResetCallback_Impl
%06llu.%06llu CollectDiagnostics Start %s %s\n
SaveDeviceState
%s::%s: failed to create error event action ret = 0x%x \n
%s::%s: failed to get addr range (ret = 0x%x) \n
CrashlogDuration
Off
AirshipDriverDK
%s::%s: release PM assertion \n
%06llu.%06llu %s 0x%08x 0x%08x\n
%s::%s: airship not up; returning %s \n
%s::%s: Transaction pending poll timed out. Proceeding to FLR \n
GetASPMState
InReset
Fiq
centauri-ccloglevel
init
    type: %s\n
kCentauriBetaRemoteServiceTimeoutErrorKey
Stop_Impl
TriggerFaultReport
i8@?0
%s::%s: failed to set ptm status in subsystem properties (ret = 0x%x) \n
errorDataObj != nullptr
%s::%s: reset already enqueued \n
%s::%s: msiaddr::%llx \n
length < sizeof(fullReason)
CompletionCallback_Impl
%s::%s: crashlog size larger than buffer (%zu > %zu) \n
isASPMEnabled
Crashed
OSAction_CentauriSubsystem_CollectLogsCallback
ready for reset
DoReset
DriverLogs
%s::%s: failed to create log stream \n
%s::%s: failed to SaveDeviceState (ret = 0x%x) \n
%s::%s: escalate FLR failure \n
cachedError
NewUserClient_Impl
ExternalMethod
No
sacObj != nullptr
%s::%s: unexpected termination notification \n
%s::%s: skipping during dext crash recovery \n
IOService
%s::%s: no ptm key - bailing out \n
!ivars->deferredWork.logCollection
v20@?0^{AirshipDriverDK=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})(?=^{AirshipDriverDK_IVars}^{AirshipDriverDK_LocalIVars})}8I16
SetRequireClientProperty
GetBootStageMirror
%s::%s: tp poll count %u \n
timeElapsedObject != nullptr
ReadyForReset
Crashlog.WFMAIN.bin
abort handler
loggerstream
%s::%s: bad arg \n
%s::%s: match notification for CentauriRemoteInterface \n
%s::%s: error source not found for %s \n
%s::%s: PCI dart error %u: [%s] addressLo: 0x%x addressHi: 0x%x \n
%s::%s: failed to create osdata object \n
not null
%s::%s: failed to copy system state service (ret = 0x%x) \n
    resetHint: %u\n
%s::%s: failed to configure interrupts (ret = 0x%x) \n
%s::%s: ignoring based on boot-arg \n
WaitForRemote
%06llu.%06llu CollectLogs Complete ret: 0x%03x\n
OSAction_CentauriSubsystem_CompletionCallback
OSAction_CentauriSubsystem_TimerOccurred
GetResetHint
%s::%s: invalid parameters \n
centauri-consoleloglevel
%s::%s: fault reporter is busy \n
%s::%s: didDextRelaunch = %s (reason %u) \n
%s::%s: Close ret = 0x%x \n
%s::%s: failed to copy reset block \n
CollectDeferredFaultDataCb_block_invoke
SACFunctionAvailable
%s::%s: failed to create os action (ret = 0x%x) \n
-
%06llu.%06llu CollectDiagnostics Complete %s %s ret: 0x%03x\n
%s::%s: invalid segment count %u \n
MonotonicTimestamp
%s::%s: failed to get logging properties dict \n
ConfigureEndpointForMemSwap
GetNumMSIVectorsFromEndpoint
ivars->pciDevice
bootStageOSBeta
derivedProbeDevice
report-error
%s::%s: pmcsr 0x%04x \n
%06llu.%06llu RestoreDeviceState ret: 0x%03x\n
UnexpectedDextTermination-UserspaceReboot
%s::%s: invalid link control value \n
%s::%s: offline \n
action == ivars->timerAction
%06llu.%06llu Reset Complete ret: 0x%03x\n
InterruptOccurred_Impl
dataObject->getLength() == sizeof(uint32_t)
%s::%s: error filling buffer, bytesPrinted: %d kLineLength: %u \n
ivars->timerSource
%s::%s: function reset already in progress \n
%s::%s: signature mismatch \n
%s::%s: crashlog header reports empty: %zu bytes \n
Subsystem
ivars->resetTimestamps
functionResetEnd
/Library/Caches/com.apple.xbs/558FE645-4E39-4399-A06E-8DC20AC536F1/TemporaryDirectory.VSeWMb/Sources/AppleCentauri_driverkit/CentauriSubsystem/CentauriSubsystemUserClient.cpp
%s::%s: service notification (type: %llu) \n
%s::%s: failed to allocate statedump buffer \n
CentauriChipInfo.txt
InitializeMSI
ExecuteDeferredWorkAsync_block_invoke
RunningLPM
CentauriControlRemoteInterface
%s::%s: failed to get MSI data (ret = 0x%x) \n
%s::%s: powerFlags: %s \n
%s::%s: failed to schedule immediate wake \n
%s::%s: failed to get dir name \n
com.apple.queue.centauri-corecapture
pmcsr != nullptr
PrepareDMACommand
SetResetTimestamp
%s::%s: failed to copy immediateCb block \n
%s::%s: failed to get platform (ret = 0x%x) \n
%s::%s: requesting coredump failed (ret=0x%x) \n
kCentauriBetaFLRCount
%s::%s: bad args \n
TimerOccurred_Impl
CentauriPowerStateLog.txt
NumMSIs
%s::%s: deliver notification error (ret = 0x%x) \n
ReleasePMAssertion(ivars->pmAssertionID) == kIOReturnSuccess
Reset_block_invoke
%s::%s: failed to alloc OSNumber for monotonic time \n
[Fatal]
%s::%s: current timestamp is older than last reset timestamp, ignoring \n
CollectLogsFatal
remoteInterfaceAvailable: %d\n
ivars->cachedCrashlogsArray
%s::%s: state %u \n
v24@?0^{AirshipDriverDK=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})(?=^{AirshipDriverDK_IVars}^{AirshipDriverDK_LocalIVars})}8r^{OSString=^^?Aii^{OSMetaClass}^^?(?=^{OSObje
%s::%s: failed to save FLR timestamps \n
%s::%s: airship service not ready \n
%s::%s: dispatching propertyUpdateNotification \n
collect-logs
%06llu.%06llu 0x%x\n
CacheCrashlogs
PrepareChipForResetDuration
ssID < kNumSubsystems
ivars->inFlightWork > 0
%s::%s: completion \n
IsValidBootStage
FLRCount
%s::%s: AppleCentauriManager::Open failed (ret = 0x%x) \n
%s::%s: PCI dart error \n
errorData->isWrite < 2
%s::%s: failed to alloc OSNumber for real time \n
dextRecoveryState: %s\n
ExecuteDeferredWork
InitWithProviderAndOptions
%s::%s: termination notification for CentauriRemoteInterface \n
%s::%s: replacing existing client \n
chipId: %s\n
GetFirmwareState
com.apple.ConnectivityDriver.FLRPerformanceStats
%s::%s: first power on \n
count  primaryStart    secondaryStart  end           type\n
    promoteToFullReset: %d\n
%s::%s: invalid memswap DMA command \n
Start_Impl
%s::%s: invalid metadata dict \n
ivars->systemStateResetItemDict->setObject(kCentauriSystemStateNotificationResetKey, inReset ? kOSBooleanTrue : kOSBooleanFalse)
CancelPropertyUpdateNotificationHandler
MemSwapWorkingCopy.bin
InduceFaultCb
AppleCentauriManager::SaveClientProperty(this, key, newValue, autoClearConditions) == kIOReturnSuccess
SetProperties_Impl
%s::%s: failed to create osdata object for %s \n
memSwapMapT0: %s\n
%s::%s: error appending bytes to bufferObject \n
ServiceNotificationReady_Impl_block_invoke_2
bootTimestampKey
obj
DartMapMemSwapWorkingCopy
ivars->logCollectionInfo.type == kCentauriLogCollectionFatal
    resetFailed: %d\n
%s::%s: failed to RestoreDeviceState (ret = 0x%x) \n
%s::%s: centauri-driverkit=0 \n
%s::%s: failed to create completion os action (ret = 0x%x) \n
ScheduleImmediateWake
B16@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8
durationObject != nullptr
%s::%s: skipping %s \n
%s::%s: error handler not registered \n
%s::%s: failed to create reason string copy \n
CentauriEventLog.txt
%06llu.%06llu Reset Start\n
%s::%s: failed to validate segment length (ret = 0x%x expected %llu got %llu) \n
TriggerChipCrash
GetNumMSIVectorsRequested
%s::%s: failed to create chip reset os action (ret = 0x%x) \n
dict && dict->setObject(kCentauriPropertyPTMEnabledOnEndpoint, ptmStatus)
force panic on fatal error for ss %u (type %u)
%s::%s: deferred work is canceled \n
%s::%s: state: 0x%x \n
%s::%s: Crashlog Reason: \"%s\" \n
prepareForResetEnd
Start_Impl_block_invoke_3
ServiceNotificationReady_Impl
CollectLogsCompletion
eventName && payload
dict
com.apple.ConnectivityDriver.TimeSinceLastFLR
fatalLogCollectionTriggered
SetResetHint
N/A
resetInfo:\n
in low power
%s::%s: crash log buffer too small: %zu bytes \n
%s::%s: provider not available \n
Owner
%s::%s: failed to create timer action (ret = 0x%x) \n
%s::%s: Stop ret = 0x%x \n
CentauriManagerErrorHandler_Impl
%s::%s: invalid length (working copy %llu t0 %llu) \n
%s::%s: failed to create function name copy \n
0x%04llu %06llu.%06llu - %06llu.%06llu - %06llu.%06llu %s\n
!ivars->remoteInterfaceAvailable
%s::%s: %s property exists - skipping dext crash \n
%s::%s: failed to create os action for collect logs (ret = 0x%x) \n
ret == kIOReturnSuccess || ret == kIOReturnNotFound
%s::%s: error handler already exists \n
completion
Start_Impl_block_invoke_2
ret == kIOReturnSuccess || ret == kIOReturnNotOpen
 r 
Running
%s::%s: invalid notifier \n
success
%s::%s: error reported by %s error code %u \n
    updateFWReasonString: %d\n
%s::%s: clearing cfg mbx at offset 0x%x \n
%s::%s: failed to find aer capability (ret = 0x%x) \n
%s::%s: found crashlog data for %s \n
ErrorDetected
%s::%s: failed to get owner object \n
%s::%s: added file %s, size %zu \n
%s::%s: Invalid segmentName or segmentDump observed \n
%s::%s: requesting full wake \n
pci-dart-error-data
SetErrorHandler_block_invoke
%s::%s: failed to trigger fault report (ret = 0x%x) \n
FunctionReset
%s::%s: failed to set dext relaunch property (ret = 0x%x) \n
%s::%s: invalid bootstage 0x%x \n
msi-reservation-size
%s::%s: failed to find msi capability (ret = 0x%x) \n
%s::%s: failed to find ptm capability (ret = 0x%x) \n
ReadMSIData
%s::%s: crashlog too small: %zu bytes \n
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x \n
derivedStop
CentauriBeta:\n
%s::%s: failed to copy completionCb block \n
%s::%s: failed to alloc OSNumber for SS ID
%s::%s: sleeping for %u ms...
%s::%s: invalid parameters
%s::%s: failed to get dir name
%s::%s: failed to allocate inFlightLock
%s::%s: FLR limit override boot-arg is set
%s::%s: error arg not an OSNumber
%s::%s: invalid length (working copy %llu t0 %llu)
%s::%s: failed to copy completionCb block
%s::%s: using console log level %u
%s::%s: failed to get log file name
%s::%s: Close ret = 0x%x
%s::%s: offline
%s::%s: failed to alloc OSNumber for up time
%s::%s: log collection failed (ret = 0x%x)
%s::%s: Crashlog Reason: \"%s\"
%s::%s: failed to copy deferredCb block
%s::%s: errorSource: %u, errorCode: %u, arg: 0x%llx
%s::%s: %u
%s::%s: failed to create osdata object
%s::%s: invalid segment info (addr: 0x%qx len: 0x%qx)
%s::%s: failed to create data log stream
%s::%s: bad arg
%s::%s: Open error (ret = 0x%x)
%s::%s: airship service not ready
%s::%s: driver offline (state = %u)
%s::%s: failed to set real time object
%s::%s: failed to create data log pipe
%s::%s: data::%x
%s::%s: failed to create memswap os action (ret = 0x%x)
%s::%s: error handler already exists
%s::%s: invalid state for log collection %u
%s::%s: in fatal error state (%u)
%s::%s: Crashlog Reason not found from the Crashlog data
%s::%s: failed to create log stream
%s::%s: Stop ret = 0x%x
%s::%s: failed to create file name copy
%s::%s: ErrorDetected's value type is not a dictionary
%s::%s: failed to set airship driver config
%s::%s: tp poll count %u
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x
%s::%s: failed to set ptm status in subsystem properties (ret = 0x%x)
%s::%s: AppleCentauriManager::Open failed (ret = 0x%x)
%s::%s: in low power
%s::%s: log collection already enqueued
%s::%s: client: %s
%s::%s: invalid cmd id: %u
%s::%s: crash poll iterations = %u
%s::%s: ready for reset timed out
%s::%s: service matching set up for %s
%s::%s: skipping %s
%s::%s: Invalid segmentName or segmentDump observed
%s::%s: failed to create completion os action (ret = 0x%x)
%s::%s: error source not found for %s
%s::%s: failed to create timer action (ret = 0x%x)
%s::%s: failed to get airship probe result
%s::%s: failed to allocate memory
%s::%s: logpipe: failed to copy log identifier %s
%s::%s: state %u
%s::%s: failed to validate segment length (ret = 0x%x expected %llu got %llu)
%s::%s: invalid callback parameters
%s::%s: centauri-driverkit=0
%s::%s: failed to get default queue (ret = 0x%x)
%s::%s: failed to enable timer (ret = 0x%x)
%s::%s: failed to alloc metadata
%s::%s: match notification for CentauriRemoteInterface
%s::%s: requesting full wake
%s::%s: number of MSIs requested: %u
%s::%s: error filling buffer, bytesPrinted: %d kLineLength: %u
%s::%s: errorCode %u, reason %s
%s::%s: termination notification for AirshipDriverDK
%s::%s: Driver offline. Ignoring state change %u
%s::%s: failed to set require client property (ret = 0x%x)
%s::%s: skipping during dext crash recovery
%s::%s: unexpected crash log completion
%s::%s: pmcsr 0x%04x
%s::%s: remote service unavailable. wait for %u ms
%s::%s: cmd id %u ret 0x%x
%s::%s: options 0x%x reason %s
%s::%s: msiaddr::%llx
%s::%s: error reported by %s error code %u
%s::%s: failed to alloc dict
%s::%s: failed to alloc OSNumber for monotonic time
%s::%s: block copy failed
%s::%s: handler already exists
%s::%s: failed to copy block
%s::%s: failed to set enable int source (ret = 0x%x)
%s::%s: failed to find MSI property
%s::%s: ptm enabled, clock granularity: %u ns
%s::%s: invalid crash log buffer
%s::%s: 
%s::%s: failed to create reset timestamps dict
%s::%s: powerFlags: %s
%s::%s: cachedErrorCount: %u
%s::%s: failed to RestoreDeviceState (ret = 0x%x)
%s::%s: invalid number of MSIs configured: %u
%s::%s: airship reported fatal error: %s
%s::%s: not permitted for ss id %u
%s::%s: release PM assertion
%s::%s: failed to set SS ID object
%s::%s: failed to get logging properties dict
%s::%s: Invalid coreName or crashlogData observed
%s::%s: unexpected termination notification
%s::%s: invalid state (%s)
%s::%s: logger not available
%s::%s: failed to create msi interrupt source (ret = 0x%x)
%s::%s: %s property exists - skipping dext crash
%s::%s: timer expired waiting for remote service in dext crash recovery state
%s::%s: failed to allocate metadata dict
%s::%s: failed to create osdict
%s::%s: clearing cfg mbx at offset 0x%x
%s::%s: found crashlog data for %s
%s::%s: empty crash log buffer
%s::%s: powerFlags: %u
%s::%s: driver offline - ignoring airship error notification
%s::%s: failed to create chip reset os action (ret = 0x%x)
%s::%s: invalid state for reset %u
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu
%s::%s: ret = 0x%x
%s::%s: module name not found
%s::%s: caching crashlog
%s::%s: ptm requester role not supported
%s::%s: section too small
%s::%s: PCI dart error
%s::%s: failed to find aer capability (ret = 0x%x)
%s::%s: driver offline - ignoring exec stage notification
%s::%s: escalate FLR failure
%s::%s: failed to report error (ret = 0x%x)
%s::%s: super init failed
%s::%s: failed to create user client (ret = 0x%x)
%s::%s: deferred work is canceled
%s::%s: coredump/crashlog completion failed (ret=0x%x)
%s::%s: bad size (got %u max %u)
%s::%s: airship reported error: 0x%x
%s::%s: error handler not registered
%s::%s: testID: %u
%s::%s: chip crash timed out
%s::%s: initialized MSI-1
%s::%s: MSI handler: boot stage = %u
%s::%s: memory allocation crashlog reason string failed
%s::%s: failed to get logger
%s::%s: failed to copy system state service (ret = 0x%x)
%s::%s: new exec stage: %u
%s::%s: lpw -> on
%s::%s: failed to get user client service
%s::%s: dispatching cached errors
%s::%s: failed to copy properties
%s::%s: failed to get logging properties object
%s::%s: Using FLR limit: %u
%s::%s: failed to save FLR timestamps
%s::%s: invalid input dictionary - bailing out
%s::%s: failed to allocate OSData
%s::%s: failed to create IODMACommand (ret = 0x%x)
%s::%s: invalid number of MSIs requested: %u available: %u
%s::%s: finalize %d
%s::%s: reset in progress. ignoring error
%s::%s: invalid memswap map or working copy desc
%s::%s: LPM log collection mode unsupported
%s::%s: FLR timed out
%s::%s: crashlog size larger than buffer (%zu > %zu)
%s::%s: failed to get provider queue
%s::%s: GetBusyState ret = 0x%x
%s::%s: failed to create user class dict
%s::%s: driver offline - ignoring airship fatal error notification
%s::%s: requesting deferral (low power: %u, defer for memswap: %s)
%s::%s: boot stage = ready for reset
%s::%s: reset failed (ret = 0x%x)
%s::%s: invalid metadata dict
%s::%s: invalid segment count %u
%s::%s: ASPM state: %u
%s::%s: failed to update the FW crash reason string
%s::%s: hint: %u
%s::%s: failed to configure interrupts (ret = 0x%x)
%s::%s: timer expired waiting for memswap info in dext crash recovery state
%s::%s: memswap memory is already DART mapped
%s::%s: failed to set monotonic time object
%s::%s: boot stage: %s, fw state: %s
%s::%s: resuming fatal log collection (state = 0x%x)
%s::%s: didDextRelaunch = %s (reason %u)
%s::%s: failed to EnablePCIPowerManagement (ret = 0x%x)
%s::%s: failed to create chip object for family %u
%s::%s: invalid client
%s::%s: deferring (state = 0x%x)
%s::%s: failed to set dext relaunch property (ret = 0x%x)
%s::%s: service notification (type: %llu)
%s::%s: propertyUpdateNotification handler not registered
%s::%s: failed to copy provider properties
%s::%s: logpipe: failed to copy directory name %s
%s::%s: failed to create logger queue (ret = 0x%x)
%s::%s: invalid notifier
%s::%s: failed to schedule immediate wake
%s::%s: returned from SetProperties (ret = 0x%x)
%s::%s: error source %u code %u arg %llu
%s::%s: reset already enqueued
%s::%s: failed to create osdata object for StateDump
%s::%s: match notification for AirshipDriverDK
%s::%s: deliver notification error (ret = 0x%x)
%s::%s: no ptm key - bailing out
%s::%s: memswap memory map is already set
%s::%s: deferring reset
%s::%s: FLR limit (%u) reached
%s::%s: invalid state (%u)
%s::%s: crashlog header reports empty: %zu bytes
%s::%s: FLR timeout override: %u ms
%s::%s: failed to send %s (ret=0x%x)
%s::%s: failed to get addr range (ret = 0x%x)
%s::%s: FLR count: %u
%s::%s: buffer filled, totalBytesPrinted: %u bufferSize: %u
%s::%s: error appending bytes to bufferObject
%s::%s: failed to create fault reporter
%s::%s: failed to remove property (ret = 0x%x)
%s::%s: unexpected coredump completion
%s::%s: failed to create function name copy
%s::%s: error handler has been deregistered
%s::%s: failed to copy reset block
%s::%s: failed to create timer src (ret = 0x%x)
%s::%s: failed to get MSI addr (ret = 0x%x)
%s::%s: not permitted
%s::%s: requesting coredump failed (ret=0x%x)
%s::%s: MSICapOffset::%llx
%s::%s: invalid crashlog data
%s::%s: state = %u
%s::%s: working copy content: 0x%x len: %llu
%s::%s: driver offline
%s::%s: failed to get provider
%s::%s: stream: failed to copy log identifier %s
%s::%s: number of MSIs requested: %u (SingleMSI mode)
%s::%s: log collection in progress/enqueued
%s::%s: failed to set dict object for StateDump
%s::%s: failed to save timestamp
%s::%s: PCI dart error %u: [%s] addressLo: 0x%x addressHi: 0x%x
%s::%s: remote interface error (ret = 0x%x)
%s::%s: failed to set dict object for %s
%s::%s: invalid length
%s::%s: failed to find ptm capability (ret = 0x%x)
%s::%s: failed super Start (ret = 0x%x)
%s::%s: selector %llu
%s::%s: using cc log level %u
%s::%s: failed to get log id
%s::%s: unexpected match notification
%s::%s: ret: 0x%x flags: 0x%qx cnt: %d addr: 0x%qx len: 0x%qx
%s::%s: added file %s, size %zu
%s::%s: full chip reset in progress
%s::%s: failed to trigger fault report (ret = 0x%x)
%s::%s: bad max size
%s::%s: crash log buffer too small: %zu bytes
%s::%s: invalid link control value
%s::%s: remote interface unavailable
%s::%s: failed to alloc OSNumber for real time
%s::%s: failed to set reason object
%s::%s: failed to set up time object
%s::%s: failed to find PCI capability (ret = 0x%x)
%s::%s: logpipe: failed to copy file name %s
%s::%s: power assertion already held
%s::%s: Transaction pending poll timed out. Proceeding to FLR
%s::%s: invalid viddid
%s::%s: termination notification for CentauriRemoteInterface
%s::%s: first power on
%s::%s: error code not found
%s::%s: chip class not initialized
%s::%s: airship not up; returning %s
%s::%s: failed to find msi capability (ret = 0x%x)
%s::%s: replacing existing client
%s::%s: pci device not open
%s::%s: fault reporter is busy
%s::%s: invalid filename/statedump
%s::%s: bad args
%s::%s: failed to create dispatch src (ret = 0x%x)
%s::%s: SetProperties failed
%s::%s: boot stage = %s
%s::%s: failed to copy collectLogs block
%s::%s: bad arguments
%s::%s: failed to get IOPCIDevice
%s::%s: Logging prop: owner: %s dir: %s file: %s id: %s
%s::%s: device id: 0x%x
%s::%s: invalid number of MSIs requested: %u
%s::%s: current timestamp is older than last reset timestamp, ignoring
%s::%s: ignoring based on boot-arg
%s::%s: invalid viddid 0x%x
%s::%s: failed to set dict object
%s::%s: cached crashlogs not available
%s::%s: function reset already in progress
%s::%s: failed to copy completion block
%s::%s: resuming reset (state = 0x%x)
%s::%s: invalid memswap DMA command
%s::%s: signature mismatch
%s::%s: failed to get MSI data (ret = 0x%x)
%s::%s: failed to create os action for collect logs (ret = 0x%x)
%s::%s: invalid bootstage 0x%x
%s::%s: failed to serialize
%s::%s: pci read invalid data
%s::%s: provider not available
%s::%s: failed to create pci error queue (ret = 0x%x)
%s::%s: failed to get platform (ret = 0x%x)
%s::%s: failed to copy service name (ret = 0x%x)
%s::%s: invalid state for watchdog notification: %u
%s::%s: fw crash reason string is not supported with non-fatal log collection
%s::%s: failed to create airship transport
%s::%s: failed to create log pipe with provider %s
%s::%s: log collection failed (ret=0x%x)
%s::%s: deferring due to low power
%s::%s: requesting crashlog failed (ret=0x%x)
%s::%s: failed to copy prepareCb block
%s::%s: failed to open IOPCIDevice (ret = 0x%x)
%s::%s: failed to create os action (ret = 0x%x)
%s::%s: failed to  SearchProperty (ret = 0x%x)
%s::%s: dispatching propertyUpdateNotification
%s::%s: client already registered (%s)
%s::%s: failed to create reason string copy
%s::%s: failed to get the fault reporter additional owner
%s::%s: failed to set boot complete property (ret = 0x%x)
%s::%s: failed to allocate statedump buffer
%s::%s: failed to create dict
%s::%s: failed to set os action handler (ret = 0x%x)
%s::%s: failed to create working copy IOBMD (ret = 0x%x)
%s::%s: failed to allocate pending work item
%s::%s: failed to prepare for DMA (ret = 0x%x)
%s::%s: driver %s - ignoring MSI notification
%s::%s: failed to allocate lock
%s::%s: failed HasPCIPowerManagement (ret = 0x%x)
%s::%s: failed to SaveDeviceState (ret = 0x%x)
%s::%s: failed to alloc OSString
%s::%s: number of crashlogs: %u
%s::%s: reserved MSIs via provider
%s::%s: failed to create error event action ret = 0x%x
%s::%s: timer expired waiting for remote service in reset failed state
%s::%s: failed to create reset state item (ret=0x%x)
%s::%s: failed to create osdata object for %s
%s::%s: invalid driver state %u for dext crash recovery state %u
%s::%s: %s
%s::%s: crashlog too small: %zu bytes
%s::%s: failed to get owner object
%s::%s: datapipe: failed to copy directory name %s
%s::%s: failed to set properties (ret = 0x%x)
%s::%s: completion
%s::%s: failed to create memory map (ret = 0x%x)
%s::%s: device control reg val: 0x%x
%s::%s: poll count %u
%s::%s: failed to copy immediateCb block
%s::%s: failed to create os action for watchdog notification (ret = 0x%x)
```
