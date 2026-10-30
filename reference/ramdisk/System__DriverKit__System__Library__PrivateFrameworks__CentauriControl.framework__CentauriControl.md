# `/System/DriverKit/System/Library/PrivateFrameworks/CentauriControl.framework/CentauriControl`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,173,680 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 2504)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/System/DriverKit/System/Library/PrivateFrameworks/CentauriControl.framework/CentauriControl (compatibility version 1.0.0, current version 1.0.0)`
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

## Strings (2,138)

```
%s::%s: diagnostic type %u already in progress for ss %u \n
%s::%s: remote service unavailable. wait for %u ms \n
name
%s::%s: remote log collection not in progress \n
%s::%s: failed to copy service name (ret = 0x%x) \n
%s::%s: log collection failed (ret = 0x%x) \n
WFL5G.regdump.bin
Crashlog.WDMAInfo.txt
CollectLogs
newValue
Crashlog.WFL5G.bin
TriggerFaultReport
%s::%s: match notification for CentauriRemoteInterface \n
errorDataObj != nullptr
%s::%s: failed to get user client service \n
ExecuteDeferredWork
SaveDeviceState
eventNameObject
dict->setObject(\"DiagnosticType\", diagnosticTypeObject)
errorTypeObject
IsValidClient
PrepareChipForReset
%s::%s: My msiAddr::%llx msiData::%x \n
%s::%s: null watermark pointers: name: %s srcAddress: 0x%llx compIndex: %u chainID: %u startNode: %u \n
SendDiagnosticsCompletion
ReleasePMAssertion(ivars->pmAssertionID) == kIOReturnSuccess
AppleCentauriManager::SetChipInfo(this, dict) == kIOReturnSuccess
%s::%s: failed to get ecid hi \n
%s::%s: failed to setobject in coredumpdict \n
%s::%s: link node not valid \n
LogWDMAResult
%s::%s: cpl status: crashlog 0x%x coredump 0x%x \n
centauri-disable-coredump
%s::%s: unable to allocate crashlogData \n
%s::%s: driver offline - ignoring airship error notification \n
RD
%s::%s: %s \n
%s::%s: system state notifications activated \n
%s::%s: timed out while paused \n
%s::%s: failed to enable ptm (ret = 0x%x) \n
SetIPCProperties
dict->setObject(key, kOSBooleanTrue)
%s::%s: PCI dart error \n
%s::%s: invalid driver state %u for dext crash recovery state %u \n
%s::%s: Requested buffer size::%x \n
FAIL
SetPTMProperty
%s::%s: client: %s \n
Crashlog.WFP2G.bin
%s::%s: invalid control service \n
%s::%s: Segment: 0x%x Cannot be accessed via WDMA \n
%s::%s: state: 0x%x \n
RealTimestamp
CollectLogsFatal
%s::%s: unable to allocate crashlog dictionary \n
%s::%s: failed to get coredump info \n
CompletionCallback_Impl
%06llu.%06llu CollectDiagnostics Start %s %s\n
%s::%s: crashlog segment observed index: %d address: 0x%x length: 0x%x \n
%s::%s: Watermark saved fileName: %s chainID: %d \n
%s::%s: SS0 offset: %llu size: %u SS1 offset: %llu size: %u SS2 offset: %llu size: %u \n
%s::%s: invalid parameters \n
PrintCrashlogInfo
PartiallyBooted
OSAction_CentauriControlDiagnosticControllerWDMA_TimerOccurred
hasReenumeratedDict
WakeupLoggerQueue
%s::%s: crashlog table invalid magic::%llx \n
SetupServiceMatchingNotification
%s::%s: sleeping for %u ms... \n
%s::%s: WDMA is busy !!! \n
%s::%s: bad size of sectionInfoOSData (expected: %lu got: %lu) \n
%s::%s: no shared endpoint info \n
com.apple.ConnectivityDriver.DiagnosticsCollectionResult
%s::%s: failed to get default queue (ret = 0x%x) \n
%s::%s: failed to allocate pending work item \n
RestoreDeviceState
%s::%s: Crashlog Reason not found from the Crashlog data \n
%s::%s: WDMA dump cfg::%x ext_cfg::%x \n
%s::%s: coredump/crashlog completion failed (ret=0x%x) \n
userClient
%s::%s: replacing existing client \n
Crashlog.WFTX.bin
BTSEC.regdump.bin
GetSubsystemTimeout
%s::%s: local log collection not in progress \n
%s::%s: selector %llu dispatch provided %s \n
        coredumpPending: %d\n
%s::%s: failed to set SS ID object \n
fCoredumpInfo.numCores
%s::%s: invalid number of cores for ss %u \n
%s::%s: GetCrashlogMaxNumSegments failed \n
dextRelaunchObj != nullptr
InitializeMSI
%s::%s: Invalid segname or segdump \n
coredumpFile
SetCrashlogHandler_block_invoke
%s::%s: unable to allocate segment name \n
DirectoryName
No
CancelPropertyUpdateNotificationHandler
CollectLogsCallback_Impl_block_invoke
%s::%s: failed to copy reg colon2 in segmentdump \n
%s::%s: failed to allocate crashlog dictionary \n
!ivars->completionCopy
SendWatchdogNotification
i40@?0^^{OSDictionary}8^^{OSDictionary}16^^{OSDictionary}24^^{OSString}32
ServiceNotificationReady_Impl_block_invoke_2
%s::%s: FLR limit (%u) reached \n
copy
%s::%s: Invalid args \n
SetupMemSwapRegions
busy
waitingForReadyForReset
WFRX.imem.bin
%s::%s: invalid fileStoreIndex: %d \n
SendChipCrashFiq
Stop
%s::%s: timer expired waiting for remote service in dext crash recovery state \n
WatchdogCallback_Impl_block_invoke
WFL2G.rxscr.bin
%s::%s: WDMA buffer allocation failed::%x \n
CrashlogTable
CollectImmediateFaultDataCb
AirshipDriverDK
%s::%s: error handler not registered \n
%s::%s: working copy content: 0x%x len: %llu \n
%06llu.%06llu CollectLogs Start 0x%04x %s\n
ivars->resetTimestamps
%s::%s: number of system events required is unsupported (0x%x), ignoring unsupported bits \n
%s::%s: No Controller error status observed::%d \n
StartWDMAConfig
GetCrashlogMaxNumSegments
%s::%s: invalid metadata dict \n
%s::%s: error source %u code %u arg %llu \n
%s::%s: invalid fileStoreIndex: %u \n
ret == kIOReturnSuccess || ret == kIOReturnNotFound
%s::%s: pci device not open \n
%s::%s: dmaconfig failed::%x \n
%s::%s: WDMA channel is errored out !!! \n
%s::%s: os action wait failed (ret = 0x%x) \n
%s::%s: selector %llu \n
errorData->isWrite < 2
abort handler
%s::%s: wdma link node not valid \n
ivars->diagnosticState == kCentauriDiagnosticStateCrashlog || ivars->diagnosticState == kCentauriDiagnosticStateCoredump
%s::%s: failed to create IOBMD (ret = 0x%x) \n
is not
%s::%s: failed to  SearchProperty (ret = 0x%x) \n
WaitForRemote
    type: %s\n
ashpRet == AIRSHIP_OK || ashpRet == AIRSHIP_ENOTREADY
%s::%s: failed to save FLR timestamps \n
ivars->timerSource
%s::%s: failed to create memory map (ret = 0x%x) \n
ivars->cachedCrashlogsArray
%s::%s: crashlog table info - address 0x%x, length 0x%x \n
prevState == kCentauriDextRecoveryStateIdle || prevState == kCentauriDextRecoveryStateWaitForRemote
LPMBoot
ptmInfoDict
CacheCrashlogs
%s::%s: FLR timeout override: %u ms \n
dataObject->getLength() == sizeof(uint32_t)
%s::%s: failed to merge dictionaries \n
CoredumpCompletion
CopyClientMemoryForType_Impl
%s::%s: FLR limit override boot-arg is set \n
%s::%s: cmd id %u ret 0x%x \n
%s::%s: failed to get airship driver \n
BadWatermark
%s::%s: StartTimer failed \n
EnqueueDeferredWork(blockCopy, kCentauriDeferredWorkTypeOther)
ClientClose
%s::%s: invalid parameter (ss = %u) \n
%s::%s: airship service not ready \n
CentauriConfigAccessLog.txt
prevState == kCentauriDextRecoveryStateIdle
WFMAIN.itcm.bin
%s::%s: failed to copy system state service (ret = 0x%x) \n
%s::%s: Using FLR limit: %u \n
%s::%s: error handler already exists \n
%s::%s: failed to create sharedInfoDict \n
ivars->sharedEndpointInfo && ivars->sharedEndpointInfo->setObject(kCentauriPropertyPTMEnabledOnEndpoint, ptmEnabled)
CreateMetadataDict
%s::%s: requesting coredump failed (ret=0x%x) \n
%s::%s: clearing cfg mbx at offset 0x%x \n
GetNumMSIVectorsFromEndpoint
key
%s::%s: create timer set handler failed \n
%s::%s: WDMA completes successfully after %u continous errors. Resetting error count \n
%s::%s: WDMA numChains: %u exceeds maxChains: %u \n
%s::%s: subsystem %u, component %u, numSegments %u \n
%s::%s: failed to configure interrupts (ret = 0x%x) \n
%s::%s: failed to get MSI data (ret = 0x%x) \n
ivars->inFlightWork < UINT32_MAX
AppleCentauriManager::SaveClientProperty(this, key, nullptr, 0) == kIOReturnSuccess
%s::%s: Stop ret = 0x%x \n
!ivars->remoteInterfaceAvailable
%s::%s: error arg not an OSNumber \n
AppleCentauri-129
remoteInterfaceAvailable: %d\n
WFL5G.recipeoverride.bin
%s::%s: MSI address not valid \n
%s::%s: crash handler has been deregistered \n
key && val
%s::%s: failed to SaveDeviceState (ret = 0x%x) \n
%s::%s: failed to create os action for watchdog notification (ret = 0x%x) \n
Reset_block_invoke
NumMSIs
%s::%s: WDMA chain count is more than expected::%d \n
%s::%s: WDMA dump lnkl::%x lnkh::%x \n
%s::%s: ptm not supported \n
ClientReady_Impl
ivars->systemStateResetItemDict->setObject(kCentauriSystemStateNotificationResetKey, inReset ? kOSBooleanTrue : kOSBooleanFalse)
%s::%s: FLR timed out \n
BTMAIN.aslr.bin
dict
%s::%s: failed to get default queue \n
%s::%s: failed to set properties (ret = 0x%x) \n
InitializeDiagnosticsMSI
%s::%s: failed to create data log stream \n
fCoredumpInfo.cores && (coreId < fCoredumpInfo.numCores) && fCoredumpInfo.cores[coreId].segments && fSegmentsPerCore
%s::%s: error source not found for %s \n
WFL2G.rtmem.bin
%s::%s: BAR0 size::%llx and type::%d \n
blockCopy
%s::%s: skipping during dext crash recovery \n
 r 
CentauriPowerStateLog.txt
logCollectionInfo:\n
%s::%s: invalid crashlog segment observed index: %d address: 0x%x length: 0x%x \n
%s::%s: WDMA dump src_addrl::%x src_addrh::%x \n
%s::%s: in reset state \n
%s::%s: MSICapOffset::%llx \n
Control
startTimeObject && endTimeObject
Crashlog.BT5G.bin
fSubsystemList[kSubsystemControl]
%s::%s: tearing down monitor \n
%s::%s: WDMA decrementor error::%d \n
%s::%s: failed to get owner object \n
errorInfo
 w 
BTSEC.dtcm.bin
BTLPS.regdump.bin
%s::%s: Force the WDMA to clear its errors \n
%s::%s: reenumeration already triggered \n
%s::%s: remote diagnostics completion callback for ss %u failed (ret = 0x%x) \n
centauri-recovery
!ivars->deferredWork.reset
TimeElapsed
%s::%s: failed to get IOPCIDevice \n
%s::%s: ss: %u \n
%s::%s: Writing bar4offset to bar0 failed, readback got::%x \n
%s::%s: collected coredump for ss %u, core %u, memory segment %s, total size 0x%x \n
ServiceNotificationReady_Impl_block_invoke
WFSC.regdump.bin
%s::%s: failed to set %s property (ret = 0x%x) \n
%s::%s: segment name is invalid for id %u\n \n
%s::%s: no pending requests \n
%s::%s: AppleCentauriManager::Open failed (ret = 0x%x) \n
%s::%s: failed to create dispatch src (ret = 0x%x) \n
%s::%s: poll count %u \n
%s::%s: Performance check - Total time taken for %s collection for subsystem::%d is::%llu nano seconds \n
LogFileName
%s::%s: failed to enable timer (ret = 0x%x) \n
%s::%s: failed to set ptm status in subsystem properties (ret = 0x%x) \n
bootTimestampKey
AllocateSecondaryMemory
%s::%s: invalid viddid 0x%x \n
%s::%s: failed to get logging properties dict \n
ivars->loggerQueue->OnQueue()
%s::%s: caching crashlog \n
%s::%s: system events required: 0x%x \n
%s::%s: deliver notification error (ret = 0x%x) \n
%s::%s: deferring due to low power \n
%s::%s: centauri-driverkit=0 \n
%s::%s: state %u \n
readData
ContinueWDMA
%s::%s: AppleCentauriManager::ChipReset failed (ret = 0x%x) \n
%s::%s: crashlog table not configured \n
%06llu.%06llu RestoreDeviceState ret: 0x%03x\n
Crashlog.BT2G.bin
HandleBadWatermark
%s::%s: failed to copy reg data in segmentdump \n
%s::%s: failed to create sharedEndpointInfo dictionary \n
TriggerReenumeration
null
%s::%s: failed to create msi interrupt source (ret = 0x%x) \n
crashlogEnd
Crashlog.WFRX.bin
OSAction_CentauriSubsystem_InterruptOccurred
%s::%s: ss %d \n
!ivars->logCollectionInfo.localLogCollectionInProgress && !ivars->logCollectionInfo.remoteLogCollectionInProgress
FiqCompletion
DerivedCentauriManagerErrorHandler_block_invoke
%s::%s: remote chip reset callback for ss %u failed (ret = 0x%x) \n
fChipDiagnostics
%s::%s: service matching set up for %s \n
%s::%s: propertyUpdateNotification handler not registered \n
systemStateEventArray
%s::%s: WDMA subordinate error::%d \n
%s::%s: no ptm key - bailing out \n
ivars->clientName
%s::%s: driver offline (state = %u) \n
flrCountDict
SetASPMState
%s::%s: failed to allocate osstring \n
ivars->memSwapAction && ivars->completionAction && ivars->chipResetAction && ivars->collectLogsAction && ivars->watchdogAction
%06llu.%06llu 0x%x\n
Off
(ss < fNumSubsystems) && fSubsystemList && fSubsystemList[ss]
%s::%s: airship reported fatal error: %s \n
%s::%s: About to reset \n
%s::%s: failed to copy reg colon1 in segmentdump \n
%s::%s: invalid callback parameters \n
CollectLogsCallback_Impl
%s::%s: failed to serialize \n
CTRL.regdump.bin
%s::%s: For subsystem: %d total wdma nodes created: %d \n
StateSnapshots
%s::%s: added file %s, size %zu \n
CollectEventLog
%s::%s: failed to copy provider properties \n
LogCollection
obj
%s::%s: skipping invalid crashlog item - index %u, id %u, address 0x%x, length %u \n
%s::%s: invalid subsystem core info \n
%s::%s: failed to create osdata object for StateDump \n
%s::%s: failed to open doorbell \n
%s::%s: wdma is error free !!! \n
hasReenumeratedDict->setObject(kCentauriControlPropertyHasReenumerated, ivars->hasReenumerated ? kOSBooleanTrue : kOSBooleanFalse)
SetRequireClientProperty
%s::%s: coredump for ss %u %s permitted \n
%s::%s: invalid cmd id: %u \n
%s::%s: fw crash reason string is not supported with non-fatal log collection \n
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu \n
Unknown
%s::%s: Driver offline. Ignoring state change %u \n
%s::%s: failed to create memswap os action (ret = 0x%x) \n
GetNumMSIVectorsRequested
CTRL.memswapptt.bin
Stop_Impl
%s::%s: WDMA buffer addresses are invalid::%x \n
%s::%s: failed to get logger queue \n
%s::%s: timeout::current time::%llx, expected time::%llx - redundant timer happened, so skip \n
%s::%s: Invalid WDMA buffer address \n
%s::%s: subsystem: %u status: 0x%x \n
numSubsystemsObj != nullptr
AdditionalPipeOwners
%s::%s: failed to create data log pipe \n
ivars->finalizeHandler
GetFirmwareState
%s::%s: failed to allocate comp buffer \n
%s::%s: Invalid FIQ address \n
        remoteLogCollectionInProgress: %d\n
LoggingProperties
pci-get-dart-error
CollectLogsStateDumps
TriggerChipCrash
BTMAIN.regdump.bin
GetSharedEndpointInfo
dict->setObject(kAppleCentauriManagerNumClientsProperty, numSubsystemsObj)
LogIdentifier
%s::%s: failed to update the FW crash reason string \n
%s::%s: crash log buffer too small: %zu bytes \n
OSAction_CentauriSubsystem_ServiceNotificationReady
Close_Impl
%s::%s: Invalid segmentName or segmentDump observed \n
cachedError->getLength() == sizeof(CentauriCachedErrorInfo)
MSI-1
WFTX.aslr.bin
WFL5G.aslr.bin
OSAction_CentauriSubsystem_WatchdogCallback
centauri-wdma-force-panic
%s::%s: failed to get CentauriControlRemoteInterface \n
CollectLogsCompletion_Impl
%s::%s: stream: failed to copy log identifier %s \n
PartiallyBootedLPM
%s::%s: failed to set os action handler (ret = 0x%x) \n
%s::%s: unable to allocate crashlogKey \n
Crashlog
GetCrashlogs
%s::%s: reserved MSIs via provider \n
%s::%s: msiaddr::%llx \n
%s::%s: BAR4 size::%llx and type::%d \n
InduceFaultCb
flrCount && *flrCount
%s::%s: WDMA timed out: continuous error count %u, ss %u state %s \n
%s::%s: StartWDMAConfig failed in config \n
v24@?0^{AirshipDriverDK=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})(?=^{AirshipDriverDK_IVars}^{AirshipDriverDK_LocalIVars})}8r^{OSString=^^?Aii^{OSMetaClass}^^?(?=^{OSObje
WaitForPCIErrorNotifications
%s::%s: failed to allocate statedump buffer \n
flrLimit: %d\n
WFSC.aslr.bin
WFSC.rtmem.bin
%s::%s: no system event notifications required \n
%s::%s: failed to acquire resource \n
%s::%s: chip crash successful \n
Success
%s::%s: datapipe: failed to copy directory name %s \n
CTRL.sram.clientport.bin
WFL2G.imem.bin
BTMAIN.sram.bin
InitAirshipDoorbell
%s::%s: Create Timer failed \n
%s::%s: FillMSINode failed \n
v12@?0i8
%s::%s: %s; adding to queue \n
ivars->logCollectionInfo.metadata
LPW
WFMAIN.socram.bin
%s::%s: wakeattime for start timer failed ret::%x \n
ResetCompletion
ValidateReceivedCrashlogTable
PrepareDMACommand
ReadMSIData
%s::%s: section too small \n
subsystemNameObject
BT2G.aslr.bin
    isASPMEnabled: %d\n
%s::%s: failed to get chip id \n
%s::%s: errorCode %u, reason %s \n
Start_Impl_block_invoke_2
action == ivars->timerAction
%06llu.%06llu 0x%08llx %s 0x%08x\n
GetCachedErrorCount
not null
%s::%s: segment %s cannot be accessed via MMIO \n
%s::%s: failed to create reset timestamps dict \n
CollectChipInfo
v8@?0
SystemStateNotificationReady_Impl
%s::%s: chip id: %u \n
%s::%s: invalid segment info (addr: 0x%qx len: 0x%qx) \n
%s::%s: invalid number of MSIs configured: %u \n
system-events-required
StoreRegCoredumpDataWithTLV
%s::%s: failed to get platform (ret = 0x%x) \n
%s::%s: lpw -> on \n
offline
WFP5G.aslr.bin
SetChipIdentifiersInRegistry
%s::%s: invalid viddid \n
%s::%s: log collection in progress/enqueued \n
Crashlog.CTRL.bin
%s::%s: failed to create os action (ret = 0x%x) \n
%s::%s: failed to copy reg addr in segmentdump \n
%s::%s: setObject failed for fileName: %s \n
%s::%s: failed to copy prepareCb block \n
Coredump
sacObj != nullptr
%s::%s: failed to create reason string copy \n
FillWDMANode
%s::%s: Invalid coreName or crashlogData observed \n
%s::%s: PCI dart error %u: [%s] addressLo: 0x%x addressHi: 0x%x \n
%s::%s: client already registered (%s) \n
ivars->state == kCentauriStateLogCollection
%s::%s: failed to alloc metadata \n
OS
pci-dart-error-data
Crashlog.WFP5G.bin
WFL5G.txscr.bin
%s::%s: fault reporter is busy \n
id == kCentauriSubsystem0
%s::%s: subsystem id: %u \n
Idle
%s::%s: found crashlog data for %s \n
WFL5G.rxscr.bin
ClearWDMAIntr
%s::%s: ss %u \n
%s::%s: unable to allocate crashlog table \n
TriggerDiagnosticsForSubsystem
SetupRemoteActionCallbacks
%s::%s: failed to create chip reset os action (ret = 0x%x) \n
%s::%s: unexpected crash log completion \n
bufferSize
SACFunctionAvailable
%s::%s: termination notification for AirshipDriverDK \n
%s::%s: airship not up; returning %s \n
ModuleName
%s::%s: chunkBase 0x%x, chunkOffset 0x%x, bar4Size 0x%x, chunkLimit %u, chunkLength %d\n \n
%s::%s: number of MSIs requested: %u (SingleMSI mode) \n
CentauriStateDump.txt
WFMAIN.memswapptt.bin
%s::%s: failed to activate doorbell \n
fatal
WFP5G.imem.bin
incomplete-
%s::%s: CentauriCrashlog item - index %u, id %u, address 0x%x, length %u \n
TriggerPanic
%s::%s: resuming fatal log collection (state = 0x%x) \n
%s::%s: failed to create monitor \n
CollectMemoryLog
%s::%s: ret = 0x%x \n
CentauriControlSystemEvents
FillWatermarkNode
CompleteFiq
%s::%s: secondary memory is not allocated \n
IsValidBootStage
ivars->cachedErrorsArray
flrCountObject != nullptr
%s::%s: CentauriCrashlog info - magic %llx, version %u, numberOfLogs %u \n
%s::%s: error reported by %s error code %u \n
%s::%s: error handler has been deregistered \n
NotifyPropertyUpdate
version: %s\n
%s::%s: ASPM state: %u \n
com.apple.ConnectivityDriver.TimeSinceLastFLR
fatalLogCollectionTriggered
ivars->chip
PrepareFaultReportCb
ivars->pendingWork[kCentauriSubsystem0][kCentauriDiagnosticsFiq]
WFP5G.dmem.bin
OSAction_CentauriSubsystem_MemSwapCallback
%s::%s: failed to create airship client \n
%s::%s: Wdma runs had errors Continuously for max allowable times, cannot proceed to collect logs \n
SetLPMMode
%s::%s: failed to get log file name \n
WFMAIN.dtcm.bin
WFL2G.mascr.bin
BT2G.dmem.bin
NO
ReadMSIAddr
WFL5G.mascr.bin
%s::%s: MSI received is spurious or may be a response previous log collection timeout \n
Metadata
%s::%s: logpipe: failed to copy log identifier %s \n
count  primaryStart    secondaryStart  end           type\n
ROM
setFLRBit
%s::%s: Valid file::%s added \n
%s::%s: Bar4size::%llx greater than 16MB so reducing to 16MB \n
%s::%s: invalid notifier \n
%s::%s: invalid link control value \n
LPMOS
%s::%s: experienced an error earlier, ending coredump \n
%s::%s: in low power \n
%s::%s: failed to set enable int source (ret = 0x%x) \n
%s::%s: unable to allocate crashlog buffer \n
v20@?0^{AirshipDriverDK=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})(?=^{AirshipDriverDK_IVars}^{AirshipDriverDK_LocalIVars})}8I16
dict && dict->setObject(\"RequireClient\", kOSBooleanTrue)
%s::%s: log collection already enqueued \n
item->block
Start_Impl
PopulateWDMAStatusInfo
RecoverWDMA
%s::%s: failed to create memswap working copy OSData \n
%s::%s: returned from SetProperties (ret = 0x%x) \n
%s::%s: invalid state for log collection %u \n
%s::%s: Crashlog processing \n
%s::%s: failed super Start (ret = 0x%x) \n
%s::%s: failed to read BAR4 info \n
CollectDeferredFaultDataCb
ivars->timerAction
centauri-wdma-debug-level
md
ivars->pendingWork[i][j]
ready for reset
chipId: %s\n
%s::%s: empty crash log buffer \n
BTLPS.aslr.bin
%s::%s: failed to alloc OSData \n
success
%s::%s: Open error (ret = 0x%x) \n
%s::%s: timer expired waiting for memswap info in dext crash recovery state \n
Running
%s::%s: likely interrupted by host sleep on segment name: %s srcAddress: 0x%llx chainID: %u compIndex: %u startNode: %u \n
%s::%s: CollectCoredump allocated buffer sizeKB::%d \n
derivedStop
centauri-ccloglevel
oldValue != nullptr
inLowPower: %d\n
UnexpectedDextTermination
WFL2G.recipeoverridesram.bin
Resume
%s::%s: WDMA dump err_addrl::%x err_addrh::%x \n
%s::%s: Trying to clear out WDMA errors \n
dict->setObject(\"Success\", success ? kOSBooleanTrue : kOSBooleanFalse)
%s::%s: replacing existing client info for ss %u \n
%s::%s: remote memswap call failed (ret = 0x%x) \n
%s::%s: failed to copy completionCb block \n
%s::%s: failed to allocate metadata dict \n
false
derivedStart
length < sizeof(configName)
airshipService: %s\n
ivars->cachedCrashlogsArray->setObject(copy)
fLock
Crashlog.BTS.bin
        localLogCollectionInProgress: %d\n
%s::%s: escalate FLR failure \n
val && ivars->resetTimestamps->setObject(eventName, val)
WFL5G.rtmem.bin
OSAction_CentauriSubsystem_CollectLogsCallback
%s::%s: wdmaChIntrStatus::%x \n
%s::%s: failed to set dext relaunch property (ret = 0x%x) \n
WFL5G.imem.bin
BTMAIN.apiram.bin
Default
%s::%s: WDMA Failed continuous error count: %u ss: %u state: %s \n
%s::%s: unexpected crashlog completion \n
%s::%s: InitWithOptions failed \n
%s::%s: failed to create pci error queue (ret = 0x%x) \n
%s::%s: %s property exists - skipping dext crash \n
no
%s::%s: failed to alloc OSNumber for real time \n
%s::%s: super InitWithOptions failed \n
%s::%s: MSI data address are invalid \n
    secMemMD: %s\n
CollectDiagnosticsForSubsystem_block_invoke
%s::%s: enable: %u \n
%s::%s: failed to set require client property (ret = 0x%x) \n
%s::%s: ErrorDetected's value type is not a dictionary \n
ret == kIOReturnSuccess || ret == kIOReturnNotOpen
IOService
%s::%s: manager failed to set chip identifiers (ret = 0x%x) \n
%s::%s: crashlog size::%x is invalid \n
MSI-2
ClearConfigSpaceMailboxes
ReadyForReset
durationObject != nullptr
COEX.rta.bin
%s::%s: Prerequisite for collecting coredump completed \n
ret == kIOReturnSuccess || ret == kIOReturnInvalid
force panic on fatal error for ss %u (type %u)
%s::%s: failed to create function name copy \n
%06llu.%06llu %s 0x%08x 0x%08x\n
    updateFWReasonString: %d\n
%s::%s: initialized MSI-1 \n
%s::%s: data::%x \n
%s::%s: failed to allocate segmentname \n
%s::%s: testID: %u \n
WFL5G.recipeoverridesram.bin
WFP2G.imem.bin
WFP2G.regdump.bin
fSubsystemList[kSubsystemBT]
CollectDiagnosticsForSubsystem
%s::%s: id::%d crashlogTableAllocatedSize::%x numComponents::%d \n
%s::%s: errorSource: %u, errorCode: %u, arg: 0x%llx \n
%s::%s: crashlog too small: %zu bytes \n
PrepareForReset
%s::%s: msi recieved but response sent, WDMA Continuous error count::%d \n
%s::%s: Partial fill file name exceeds max strlen \n
CompleteCrashlogCoredump
CollectLogsFatalOnDefaultQueue
%s::%s: failed to create timer action (ret = 0x%x) \n
%s::%s: airship reported error: 0x%x \n
%s::%s: deferring (state = 0x%x) \n
%s::%s: invalid state: 0x%x \n
CentauriControl:\n
%s::%s: chip crash timed out \n
true
%s::%s: bad arguments \n
%s::%s: create timer failed ret::%x \n
%s::%s: watchdog cb no longer registered \n
ChipResetCallback_Impl
ErrorCode
%s::%s: getCrashlogTableInfo failed: 0x%x \n
GetCrashlogTableInfo
coredumpStart
errorData
!ivars->deferredWork.logCollection
InterruptOccurred_Impl
Reason
i < kSystemEventsCount
%s::%s: failed to create service (ret = 0x%x) \n
ErrorType
key && dict
%s::%s: reset already enqueued \n
CentauriChipInfo.txt
CollectDeferredFaultDataCb_block_invoke
IOPCIPMCSState
%s::%s: failed to create IODMACommand (ret = 0x%x) \n
WFMAIN.sram.bin
WFL2G.aslr.bin
BT5G.regdump.bin
CreateWDMABuffer
%s::%s: failure on segment name: %s srcAddress: 0x%llx chainID: %u compIndex: %u startNode: %u \n
v32@?0Q8^{IOService=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})}16Q24
Reset
%s::%s: failed to set reason object \n
SystemEvents
%s::%s: failed to copy reg newline in segmentdump \n
%s::%s: Get buffer size failed: 0x%x \n
%s::%s: failed to alloc OSNumber for up time \n
CollectConfigLogs
%s::%s: pmcsr 0x%04x \n
data
%s::%s: buffer size invalid::%x \n
DerivedCentauriManagerErrorHandler
RegisterServiceOrStartDextRecovery_block_invoke
FetchMemSwap
WriteToChain
%s::%s: logpipe: failed to copy directory name %s \n
%s::%s: deferring reset \n
%s::%s: bad size (got %u max %u) \n
%06llu.%06llu SaveDeviceState ret: 0x%03x\n
CheckWatermarks
%s::%s: Forcefully abort the currently running WDMA channel \n
%s::%s: adding new client info for ss %u \n
SendChipResetNotification
GetASPMState
%s::%s: WDMA recovery failed with status::%d\n \n
ptmInfoDict->setObject(kCentauriPropertyPTMEnabledOnEndpoint, ptmEnabled)
DerivedLogState
%s::%s: failed to gather coredump for ss %u, core %u, memory segment %s \n
centauri-flr-limit
%s::%s: invalid segment count %u \n
OSAction_CentauriSubsystem_TimerOccurred
%s::%s: WDMA retry didn't work, state::%x \n
%s::%s: failed to create ss1 sub memory descriptor (ret = 0x%x) \n
Boot
%s::%s: failed to start super (ret = 0x%x) \n
receiverOn != nullptr
%s::%s: timer source is invalid \n
subsystemInfo
%s::%s: secondary mem not allocated \n
FetchMemSwapInfo_Impl
%s::%s: chip reset callback not ready for ss %u \n
%s::%s: failed to create log stream \n
%s::%s: missing memswap config; triggering client launch \n
t2026
/Library/Caches/com.apple.xbs/558FE645-4E39-4399-A06E-8DC20AC536F1/TemporaryDirectory.VSeWMb/Sources/AppleCentauri_driverkit/CentauriSubsystem/CentauriSubsystem.cpp
%s::%s: system-events-required property search failed (ret = 0x%x) \n
%s::%s: invalid watchdog status (0x%x) \n
[Fatal]
%06llu.%06llu CollectDiagnostics Complete %s %s ret: 0x%03x\n
nonfatal
msi-reservation-size
ErrorDetected
CentauriDebug
%s::%s: StartWDMAConfig failed \n
%s::%s: using cc log level %u \n
%s::%s: failed to allocate memory \n
%s::%s: failed to create array \n
com.apple.queue.centauri-pcierrors
%s::%s: driver offline - ignoring airship fatal error notification \n
RequireClient
%s::%s: failed to set dict object for %s \n
%s::%s: failed to find msi capability (ret = 0x%x) \n
Invalid
%s::%s: Invalid compIndex: %u \n
%s::%s: Diagnostics MSI not enabled \n
coredumpEnd
%s::%s: not permitted for ss id %u \n
%s::%s: release PM assertion \n
ivars->logCollectionInfo.completion
SetDextRecoveryState
Crashed
%s::%s: failed to create doorbell \n
SUCCESS
%s::%s: Invalid config exists state: %d segmentDump: %u compIndex: %u fileStoreIndex: %u \n
%s::%s: crashlogTable numberOfLogs: %d \n
%s::%s: crashlog handler already exists \n
%s::%s: invalid chipInfo 0x%x \n
%s::%s: SART not enabled (capabilities = 0x%x) \n
diagnosticType && diagnosticName
%s::%s: failed to create IOServiceStateNotificationDispatchSource (ret = 0x%x) \n
%s::%s: prepare dma failed::%x \n
%s::%s: powerFlags: %s \n
%s::%s: failed to prepare for DMA (ret = 0x%x) \n
OSAction_CentauriSubsystem_CompletionCallback
%s::%s: ValidateReceivedCrashlogTable failed \n
%s::%s: exceeded maximum number of descriptors, nodeIndex: %u maxDescriptors: %u \n
SetPowerOverride(true) == kIOReturnSuccess
%s::%s: cachedErrorCount: %u \n
Crashlog.WFMAIN.bin
WFP5G.rtmem.bin
BT5G.imem.bin
DerivedInterruptOccurred
CollectDiagnostics_Impl
ExecStageChanged
%s::%s: crashlog header reports empty: %zu bytes \n
%s::%s: Wdma runs had errors Continuously for max allowable times, need to reset the chip \n
%s::%s: subsystem: %d \n
completionCopy
%s::%s: failed to get provider \n
%s::%s: invalid ss id (ss = %u) \n
%s::%s: error code not found \n
%s::%s: failed to set dict object \n
ivars->pciDevice
%s::%s: WDMA buffer addresses are invalid: 0x%x \n
%s::%s: log collection completion already exists \n
%s::%s: Close ret = 0x%x \n
OpenRemoteService
%s::%s: function reset already in progress \n
%06llu.%06llu Reset Complete ret: 0x%03x\n
SendAnalytics
%s::%s: Prerequisite for collecting crashlog table info is completed \n
%s::%s: secondary memory already allocated \n
ControlDextCrashError
centauri-consoleloglevel
FaultReporter
index < fSegmentsPerCore[coreId]
yes
%s::%s: boot stage = %s \n
FillMSINode
ValidateCrashlogTableSize
%s::%s: failed HasPCIPowerManagement (ret = 0x%x) \n
%s::%s: invalid number of MSIs requested: %u available: %u \n
SetPowerState_Impl
CollectMSILog
0x%04llu %06llu.%06llu - %06llu.%06llu - %06llu.%06llu %s\n
dextRecoveryState: %s\n
%s::%s: chip rev: 0x%x \n
SetErrorHandler_block_invoke
ReadyForResetDuration
WFMAIN.aslr.bin
BTMAIN.itcm.bin
%s::%s: ss %u type %u \n
init
%s::%s: failed to create os action for collect logs (ret = 0x%x) \n
DeferReset
%s::%s: in fatal error state (%u) \n
%s::%s: invalid number of MSIs requested: %u \n
%s::%s: failed to find ptm capability (ret = 0x%x) \n
timeElapsedObject != nullptr
%s::%s: bad section info: overlaps \n
Subsystem
%s::%s: Not a valid Crashlog table, magic recieved::%llx \n
%s::%s: failed to allocate coredump dictionary \n
%s::%s: bad section info for ss1: zero offset/len \n
    reenumerationTriggered: %d\n
CollectLogsCompletion
ClientOpen
%s::%s: failed to create working copy IOBMD (ret = 0x%x) \n
%s::%s: ret: 0x%x flags: 0x%qx cnt: %d addr: 0x%qx len: 0x%qx \n
%s::%s: failure on fiq srcAddress: 0x%llx dstAddress: 0x%llx \n
%s::%s: WDMA failed to recover with status::%d \n
Stop_Impl_block_invoke
%s::%s: timer expired waiting for remote service in reset failed state \n
centauri-flr-timeout-ms
StartTimer
%s::%s: exceeded maximum number of components, numComponents: %u maxComponents: %u \n
%s::%s: unexpected coredump completion \n
ClientCrashlogHandler
%s::%s: memswap cb no longer registered \n
cachedError
CollectLogs_block_invoke
%s::%s: bad max size \n
%s::%s: exec stage change to OS \n
ivars->controlPciService->SetASPMState(false) == kIOReturnSuccess
%s::%s: WDMA timedout but no errors observed!! \n
%s::%s: bad section info for ss0: zero offset/len \n
(null)
%s::%s: offline \n
%s::%s: failed to allocate OSData \n
ExecuteDeferredWorkAsync_block_invoke
%s::%s: WDMA buffer creation failed::%x \n
%s::%s: failed to create timer src (ret = 0x%x) \n
%s::%s: failed to save timestamp \n
%s::%s: pci read invalid data \n
WFP2G.dmem.bin
BTMAIN.dtcm.bin
%s::%s: WDMA failed to start, WDMA Continuous error count::%d \n
%s::%s: log collection failed (ret=0x%x) \n
com.apple.ConnectivityDriver.FLRPerformanceStats
WFL2G.dmem.bin
WFP5G.regdump.bin
ivars->collectLogsCompletionBlock
%s::%s: bad arg \n
%s::%s: failed to create completion os action (ret = 0x%x) \n
length < sizeof(fullReason)
%s::%s: memswap memory map is already set \n
%s::%s: boot stage = ready for reset \n
%s::%s: failed to alloc OSNumber for monotonic time \n
HandleChipCrashTimeout
segmentsPerCore && numCores && lpmStatePerCore
WaitForReadyForReset
WFRX.rtmem.bin
WFRX.regdump.bin
OSAction_CentauriSubsystem_CentauriManagerErrorHandler
ReleaseSecondaryMemory
%s::%s: LPM \n
%s::%s: failed to create dict \n
%s::%s: failed to create reset state item (ret=0x%x) \n
%s::%s: segment is null \n
CreateChipObject
%s::%s: chip class not initialized \n
%s::%s: failed to alloc OSString \n
%s::%s: dispatching propertyUpdateNotification \n
%s::%s: failed to create osdata object \n
%s::%s: invalid state (%u) \n
%s::%s: no pending completion (ss = %u) \n
DextRelaunchState
EndWork
%s::%s: failed to set object in dict \n
%s::%s: In paused state \n
%s::%s: WDMA is available and working!! \n
%s::%s: remote log collection failed (ret = 0x%x) \n
SubsystemID
in low power
%s::%s: Timer period set to %llu milliseconds and next timer expiry expected at ::%llu current time in ns::%llu \n
TimerOccurred_Impl
%s::%s: FillChainLinkNode failed \n
%s::%s: failed to get ecid lo \n
WiFi
systemEventsRequiredObj
%s::%s: time::%llu \n
UserClientTerminated
    hasReenumerated: %d\n
%s::%s: failed to get chip object \n
ChangePowerState(kIOServicePowerCapabilityOn) == kIOReturnSuccess
CheckErrorPolicyForKey
CancelErrorHandler
PrepareNode
%s::%s: Chain::%llu srcaddr::%llx dstaddr::%llx bytes::%x nodenum::%x \n
%s::%s: failed to allocate lock \n
%s::%s: failed to get log id \n
%s::%s: requesting crashlog failed (ret=0x%x) \n
%s::%s: device control reg val: 0x%x \n
BootComplete
Crashlog.WFL2G.bin
%s::%s: bad chain watermark at chainID: %u, failed before attempting to access an address from cores \n
%s::%s: buffer filled, totalBytesPrinted: %u bufferSize: %u \n
CopyName(&serviceName) == kIOReturnSuccess
InitMemSwapWorkingCopy
CollectLogsFatal_block_invoke
TimeToTriggerCollectLogs
BT5G.aslr.bin
%s::%s: new doorbell value: 0x%x \n
%s::%s: crashlog handler is not registered \n
%s::%s: didDextRelaunch = %s (reason %u) \n
%s::%s: first power on \n
%s::%s: SetProperties failed \n
%s::%s: crash poll iterations = %u \n
%s::%s: failed to set monotonic time object \n
%s::%s: failed to set handler (ret = 0x%x) \n
%s::%s: Clear WDMA from further running \n
%s::%s: failed to copy deferredCb block \n
ExternalMethod
dict && dict->setObject(kCentauriPropertyUnexpectedDextTermination, (ivars->dextRelaunchReason == kCentauriManagerDextRelaunchReasonCrash) ? kOSBooleanTrue : kOSBooleanFalse)
ServiceNotificationReady_Impl
%s::%s: LPM log collection mode unsupported \n
%s::%s: boot stage: %s, fw state: %s \n
v12@?0I8
%s::%s: size %u \n
%s::%s: using console log level %u \n
%s::%s: failed to get core count for ss %u \n
0
memSwapMapT0: %s\n
UnexpectedDextTermination-UserspaceReboot
resetStart
%s::%s: memswap info not available yet \n
%s::%s: skipping boot stage check \n
execStage <= kCentauriBootStageMax
CentauriEventLog.txt
    crashlogPending: %d\n
errorSource == kCentauriErrorSourceCentauri
%s::%s: ready for reset timed out \n
%s::%s: setobject failed for segmentName::%s \n
SetState
%s::%s: invalid state for reset %u \n
ivars->logCollectionInfo.type == kCentauriLogCollectionFatal
%06llu.%06llu CollectLogs Complete ret: 0x%03x\n
%s::%s: crashlog size larger than buffer (%zu > %zu) \n
OSAction_CentauriControlRemoteInterface_ClientReady
%s::%s: ValidateReceivedCrashlogTable failed for numComponents::%d \n
%s::%s: failed to get MSI addr (ret = 0x%x) \n
TriggerClientLaunch
%s::%s: failed to create user client (ret = 0x%x) \n
[NonFatal]
%s::%s: ptm enabled, clock granularity: %u ns \n
%s::%s: Timer expired with reset flag set \n
kAudioMessage_ReceiverOn
%s::%s: link down detected after error detect \n
%s::%s: tp poll count %u \n
FetchMemSwapInfo
SetDextRecoveryState_block_invoke
InReset
ClearWDMA
%s::%s: sizeof got::%x CrashlogInfo::%lx CrashlogItemInfo::%lx maxComponents::%d minSize::%x maxSize::%x \n
%s::%s: invalid client \n
NA
ret == kIOReturnSuccess
is
%s::%s: invalid memswap DMA command \n
ivars->completionCopy
%s::%s: failed to allocate inFlightLock \n
%s::%s: failed to set up time object \n
FLRCount
%s::%s: wdma debug level not matching \n
dict->setObject(\"DiagnosticName\", diagnosticNameObject)
dict->setObject(\"ErrorType\", errorTypeObject)
ssID < kNumSubsystems
pmcsr != nullptr
%s::%s: reset failed (ret = 0x%x) \n
WFP2G.rtmem.bin
%s::%s: FillWDMANode failed \n
%s::%s: Logging prop: owner: %s dir: %s file: %s id: %s \n
BTSEC.aslr.bin
%s::%s: susbsyteminfo is invalid \n
%s::%s: driver offline - ignoring MSI notification \n
AirshipDriverConfigName
%06llu.%06llu SetupMemSwapRegion ret: 0x%03x\n
prevState == kCentauriDextRecoveryStateCollectLogs
TimeToOSBootStage
Crashlog.WFSC.bin
%s::%s: failed to create osdata object for %s \n
action == ivars->msiAction
eventName && payload
WFSC.dmem.bin
%s::%s: ProcessCrashlogTable total::%d \n
%s::%s: failed to allocate chip object for CentauriChipControlT2026 \n
crashlogStart
%s::%s: unexpected match notification \n
CentauriManagerErrorHandler_Impl
address && length && coredump
WFL5G.dmem.bin
BTLPS.seqdmem.bin
%s::%s: reading crashlog item - index %u, id %u, address 0x%x, length %u \n
i8@?0
%s::%s: get timeout failed \n
EnablePTM
Start_Impl_block_invoke_3
val
%s::%s: module name not found \n
%s::%s: options 0x%x reason %s \n
CreateTimer
%s::%s: Corrupted crash log table size::%x \n
crashlogFile
HandleAnyPartialCollections
%s::%s: failed to get addr range (ret = 0x%x) \n
%s::%s: AppleCentauriManager::DoReenumeration failed (ret = 0x%x) \n
YES
ivars->inFlightWork > 0
test
%s::%s: failed to set real time object \n
%s::%s: bad section info for ss2: zero offset/len \n
%s::%s: initialized MSI-%u \n
%s::%s: failed to create airship transport \n
%s::%s: ValidateCrashlogTableSize failed \n
centauri-fatal-err-panic
    promoteToFullReset: %d\n
EnablePTMOnEndpoint
WFMAIN.rtascripter.bin
%s::%s: failed to alloc metadata dict \n
%s::%s: device id: 0x%x \n
WFTX.regdump.bin
%s::%s: Invalid diagnosticState: %s \n
%s::%s: Link is down, coredump is not permitted \n
diagnosticTypeObject && diagnosticNameObject && dict
Open_Impl
Fiq
Yes
Recovery
%s::%s: register coredump disabled \n
RemoteServiceProperties
CancelCrashlogHandler
%s::%s: no \n
%s::%s: logpipe: failed to copy file name %s \n
loggerstream
%s::%s: not permitted \n
%s::%s: reset in progress. ignoring error \n
%s::%s: pci device not available \n
%s::%s: failed to create os action (ret = 0x%x) for client %u \n
%s::%s: ss: %u accessType: %u state: %s \n
%s::%s: WDMA buffer getaddressrange is invalid::%x phyMemSegment.length::%llx verifyRange.length::%llx \n
%s::%s: failed to allocate segmentDump \n
%s::%s: Failed to collect partial collected files \n
OSAction_CentauriControl_DiagnosticsInterruptOccurred
%s::%s: Empty crashlog table::%x size: 0x%x \n
%s::%s: FillWatermarkNode failed \n
!GetInLowPower()
%s::%s: failed to get airship probe result \n
%s::%s: invalid length (working copy %llu t0 %llu) \n
state: %s\n
%s::%s: resuming reset (state = 0x%x) \n
%s::%s: Crashlog Reason: \"%s\" \n
CleanUp
%s::%s: bad args (ss id %u type %u) \n
CentauriMSILog.txt
%s::%s: ptm requester role not supported \n
prepareChipForResetEnd
N/A
%s::%s: WDMA max Continuous error count reached \n
%s::%s: failed to alloc OSNumber for SS ID \n
GetDiagnosticState
WatchdogCallback_Impl
%s::%s: failed to find aer capability (ret = 0x%x) \n
v20@?0i8^{OSDictionary=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{OSContainer_IVars}^{OSContainer_LocalIVars})^^?(?=^{OSCollection_IVars}^{OSCollection_LocalIVars})(?=^{OSDictionary_IVars}^{OSDictionary_LocalIVar
%s::%s: invalid parameters (ss = %u type = %u) \n
%s::%s: client no longer valid; dropping completion \n
centauri-driverkit
%s::%s: state = %u \n
%s::%s: signature mismatch \n
WFTX.rtmem.bin
%s::%s: failed to copy block \n
%s::%s: invalid input dictionary - bailing out \n
ConfigureEndpointForMemSwap
wdma-error-
ProcessCrashlogTable
%s::%s: Crashlog table address: 0x%x table size: 0x%x \n
centauri-crashlog-coredump-via-mmio
    logCollectionInfo:\n
MemSwapWorkingCopy.bin
com.apple.centauri.reset.ccpu
ivars->cachedErrorsArray->setObject(cachedError)
%s::%s: invalid bootstage 0x%x \n
DiagnosticName
%s::%s: id::%d crashlogTableSize::%x \n
centauri-allow-panic
%s::%s: ignoring based on boot-arg \n
%s::%s: failed to schedule immediate wake \n
SetPropertyUpdateNotificationHandler
%s::%s: completion \n
%s::%s: WDMA chain corrupt currChain: %u numChains: %u \n
%s::%s: invalid section info \n
AppleCentauriManagerStateDump.txt
%s::%s: empty crashlog table info \n
/Library/Caches/com.apple.xbs/558FE645-4E39-4399-A06E-8DC20AC536F1/TemporaryDirectory.VSeWMb/Sources/AppleCentauri_driverkit/CentauriSubsystem/CentauriSubsystemUserClient.cpp
maxNumSegments
%s::%s: failed to create osdict \n
BadChain
CrashlogCompletion
%s::%s: allocated metadata copy \n
DiagnosticsInterruptOccurred_Impl
SetupMemSwapRegion
CrashlogDuration
WFSC.imem.bin
FillWDMAConf
%s::%s: failed to get sharedClientInfo (ret = 0x%x) \n
WaitForClients
%s::%s: SART not enabled, skipping FIQ \n
%s::%s: ValidateReceivedCrashlogTable failed for size allocated::%d current::%d \n
BTMAIN.memswapptt.bin
%s::%s: failed to make a copy of sharedClientInfo \n
%s::%s: failed to create os action token (ret = 0x%x) \n
SetProperties_Impl
CollectStateSnapshots
serializedBuffer && serializedLength
%s::%s: failed to validate segment length (ret = 0x%x expected %llu got %llu) \n
Crashlog.BTLPS.bin
%s::%s: invalid stopIndex: %u \n
PTM
v24@?0I8I12^v16
GetBootStageMirror
%s::%s: invalid provider \n
ivars->dmaChains.comp[compIndex].startNodeIndex != 0
%s::%s: failed to allocate fileStore buffer \n
%s::%s: failed to copy properties \n
DriverLogs
%s::%s: failed to create log pipe with provider %s \n
%s::%s: failed to set dict object for StateDump \n
isASPMEnabled
%s::%s: failed to create user class dict \n
%s::%s: service notification (type: %llu) \n
AppleCentauriManager::SaveClientProperty(this, key, newValue, kCentauriAutoClearOnChipReset) == kIOReturnSuccess
BT
%s::%s: WDMA dump ctrl::%x status::%x \n
%s::%s: Invalid crash log table size::%x \n
ivars->clientArray[i].callbacks.clientReadyAction
%s::%s: handler already exists \n
dict && dict->setObject(kCentauriPropertyBootComplete, kOSBooleanTrue)
    resetFailed: %d\n
FillChainLinkNode
%s::%s: failure on crashlog table: 0x%llx dstAddress: 0x%llx \n
completion
CollectLogsCompletion_Impl_block_invoke
%s::%s: super init failed \n
suspended
SetResetTimestamp
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x \n
ForceClearWDMAErrors
GetSubsystemCoreCount
B16@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8
CoredumpDuration
ErrorArg
fSubsystemList[kSubsystemWiFi]
BTSEC.seqsram.bin
val != nullptr
%s::%s: requesting full wake \n
%s::%s: memory allocation crashlog reason string failed \n
%s::%s: failed to send %s (ret=0x%x) \n
BT2G.imem.bin
%s::%s: WDMA buffer size is too small for this Coredump collection size: 0x%x CoreDumpOffset: 0x%x \n
!isFiq || ivars->subsystemId == 0
        crashlogPending: %d\n
ReportError_Impl
flrCountDict->setObject(kCentauriFLRCount, flrCountObject)
STATUS:\nCrashlog table: %s\nCrashlog: %s\n
%s::%s: skipping %s \n
%s::%s: match notification for AirshipDriverDK \n
%s::%s: new exec stage: %u \n
ExitLPW
dict->setObject(kCentauriSystemStateNotificationResetKey, kOSBooleanTrue)
%s::%s: full chip reset in progress \n
AirshipStateDump.bin
%s::%s: allocated buffer size: 0x%x \n
centauri-force-diagnostics
%s::%s: failed to create logger queue (ret = 0x%x) \n
WFTX.imem.bin
OSAction_CentauriSubsystem_ChipResetCallback
%s::%s: failed to alloc dict \n
%s::%s: centauri-disable-coredump=%u \n
bootStageOSControl
%s::%s: termination notification for CentauriRemoteInterface \n
ReportError
MonotonicTimestamp
%s::%s: failed to allocate fileName \n
%s::%s: error appending bytes to bufferObject \n
buffer->setObject(\"MemSwapWorkingCopy.bin\", ivars->memSwapWorkingCopyData)
MemoryReadBAR4
SendLogCollectionRequest
WR
%s::%s: failed to find PCI capability (ret = 0x%x) \n
WFRX.aslr.bin
%s::%s: bad args \n
TriggerClientLaunch() == kIOReturnSuccess
time          flags\n
Crashlog.COEX.bin
CheckWDMAStatus
%s::%s: number of MSIs requested: %u \n
Suspend
%s::%s: subsystem %d, numSegments %d \n
CollectCrashlogForSubsystem
%s::%s: collect logs callback not ready for ss %u \n
Paused
%s::%s: finalize %d \n
%s::%s: FLR count: %u \n
ivars->cachedCrashlogsArray->getCount() > 0
%s::%s: Exceeded collection timeout \n
%s::%s: WDMA is recovered from errors \n
%s::%s: invalid filename/statedump \n
%s
!ivars->logCollectionInfo.metadata && !ivars->logCollectionInfo.completion
resetInfo:\n
WFL2G.recipeoverride.bin
%s::%s: invalid parameter \n
report-error
MemSwapCallback_Impl
BTMAIN.seqsram.bin
InitWithProviderAndOptions
GetSecondaryMemoryDescriptor_block_invoke
IsCoredumpPermitted
%s::%s: failed to gather crashlog for ss %u, {0x%x, 0x%x} \n
%s::%s: failed to setobject in crashlogdict \n
%s::%s: failed to copy immediateCb block \n
CompleteFaultReportCb
%s::%s: driver offline - ignoring exec stage notification \n
centauri-wdma-regdump-disable
%s::%s: timer action attach failed \n
ForceAbortWDMA
%s::%s: invalid capabilities \n
%s::%s: unable to allocate coredump buffer \n
%s::%s: buffer size %u exceeds expected max %u \n
CollectPowerStateLog
%s::%s: MSI handler: boot stage = %u \n
FillChainWatermarkNode
numSubsystems
%s::%s: failed to get the fault reporter additional owner \n
%s::%s: invalid state: %u \n
%s::%s: failed to report error (ret = 0x%x) \n
CreateSystemStateNotificationItems
MaskUnsupportedRequestAER
FLRDuration
%s::%s: Not valid controlPciService or queue \n
DoReset
%s::%s: dispatching cached errors \n
Crashlog.BTMAIN.bin
BTLPS.dmem.bin
OSAction_CentauriControlSystemEvents_SystemStateNotificationReady
%s::%s: failed to copy collectLogs block \n
time          offset     r/w data\n
functionResetEnd
BT5G.dmem.bin
free
%s::%s: failed to get queue (ret = 0x%x) \n
%s::%s: ContinueWDMA chain ends \n
DerivedCollectLogs_block_invoke
%s::%s: failed to add metadata to crashlog dict (ss %u) \n
metadata = GetLogCollectionMetadata()
%s::%s: GetBusyState ret = 0x%x \n
%s::%s: power assertion already held \n
action == ivars->diagnosticsMsiAction
%s::%s: bad args (ss = %u) \n
%s::%s: failed to create fault reporter \n
GetDiagnosticState() == kCentauriDiagnosticStateIdle
CentauriUserClientProperties
%s::%s: failed to copy reset block \n
systemStateEventName
%s::%s: failed to store data in fileStore \n
%s::%s: failed to open IOPCIDevice (ret = 0x%x) \n
time          r/w address    value\n
Offline
prepareForResetEnd
PreBoot
%s::%s: dext crash error property exists \n
%s::%s: get crashlog table failed::%x \n
Owner
%s::%s: failed to create chip object for family %u \n
%s::%s: driver %s - ignoring MSI notification \n
SendTimeSinceLastFLRAnalytics
UpTimestamp
%s::%s: WDMA busy, retry after sleep \n
%s::%s: ss %u watchdog reported \n
CollectAirshipStateDumps
WFL2G.regdump.bin
%s::%s: bad diagnosticState: %s \n
%s::%s: memswap callback not available for ss %u \n
com.apple.queue.centauri-corecapture
%s::%s: failed to trigger fault report (ret = 0x%x) \n
%s::%s: cached crashlogs not available \n
CancelDeferredWork
crashlogFile && coredumpFile
%s::%s: remote watchdog notification failed (ret = 0x%x) \n
%s::%s: ss: %u accessType: %u state: %s bufferSize: %u \n
%s::%s: failed to set airship driver config \n
%s::%s: requesting deferral (low power: %u, defer for memswap: %s) \n
%s::%s: number of crashlogs: %u \n
NumClients
CentauriMemoryAccessLog.txt
%s::%s: invalid state for watchdog notification: %u \n
!ivars->inLowPower
%s::%s: invalid crashlog data \n
MSIReceived
%s::%s: Invalid address, corrupt global address \n
%s::%s: WDMA no interrupts to clear \n
%s::%s: bad arg (type: %llu) \n
ExtractCrashlogReason
CrashlogTable%u
ivars->queue->OnQueue()
%s::%s: chip crash with fiq timed out \n
-
ScheduleImmediateWake
%s::%s: failed to remove property (ret = 0x%x) \n
%s::%s:  \n
InitAirshipDoorbell_block_invoke
kAudioMessage_ReceiverState
CollectCoredumpForSubsystem
%s::%s: failed to save control dext timestamps, ret = 0x%x \n
!ivars->logCollectionInfo.crashlogPending && !ivars->logCollectionInfo.coredumpPending
ivars->numRemoteSubsystems && ivars->numRemoteSubsystems <= kCentauriRemoteSubsystemCount
%s::%s: failed to create file name copy \n
CollectLogsAbort
%s::%s: remote interface error (ret = 0x%x) \n
AbortHandler
WFP2G.aslr.bin
%s::%s: Watermark buffer size is not enough \n
%s::%s: bad arg (sectionInfoOSData) \n
%s::%s: block copy failed \n
%06llu.%06llu Reset Start\n
%06llu.%06llu SetBusLeadEnable Start enable: %s\n
%s::%s: wdmaBuffer create failed::%x \n
WDMA timed out for ss %u %s
B24@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}16
%s::%s: powerFlags: %u \n
DartMapMemSwapWorkingCopy
clientName && doorbellName
%s::%s: failed to get ptm capability (ret = 0x%x) \n
ClearUnsupportedRequestAER
BTSEC.itcm.bin
AppleCentauriManager::SaveClientProperty(this, key, val, 0) == kIOReturnSuccess
    coredumpPending: %d\n
%s::%s: invalid length \n
WFMAIN.regdump.bin
%s::%s: ivars creation failed \n
%s::%s: trying to recover WDMA \n
%s::%s: deferred work is canceled \n
%s::%s: failed to EnablePCIPowerManagement (ret = 0x%x) \n
%s::%s: unexpected termination notification \n
%s::%s: memswap memory is already DART mapped \n
IsBackToBack
readyForReset
%s::%s: WDMA dump dst_addrl::%x dst_addrh::%x \n
*crashlogFile
%s::%s: failed to get iopcidevice \n
DiagnosticType
%s::%s: failed to set boot complete property (ret = 0x%x) \n
%s::%s: WDMA dump inter::%x err::%x \n
%s::%s: Transaction pending poll timed out. Proceeding to FLR \n
RunningLPM
%s::%s: subsystem: %u \n
%s::%s: invalid crashlog size: 0x%x \n
%s::%s: invalid fileName: %s \n
remoteService: %s\n
%s::%s: failed to RestoreDeviceState (ret = 0x%x) \n
PrepareChipForResetDuration
%s::%s: error filling buffer, bytesPrinted: %d kLineLength: %u \n
ctx
%s::%s: %u \n
fwCrashReported
%s::%s: driver offline \n
buffer
%s::%s: failed to create ss2 sub memory descriptor (ret = 0x%x) \n
%s::%s: unable to allocate segmentDump \n
%s::%s: invalid state (%s) \n
SetErrorHandler
WFTX.dmem.bin
%s::%s: failed to get crashlog table info (ret = 0x%x) \n
%s::%s: bad section info: exceeds sec mem range \n
handler
BT2G.regdump.bin
BTLPS.imem.bin
systemStateEventArray->setObject(systemStateEventName)
%s::%s: invalid parameters (ss = %u) \n
derivedProbeDevice
collect-logs
systemEventsRequiredObj->getLength() == sizeof(ivars->systemEventsRequired)
ivars->controlPciService->SetASPMState(true) == kIOReturnSuccess
DerivedCollectLogs
SetCrashlogHandler
%s::%s: remote collect logs callback for ss %u failed (ret = 0x%x) \n
%s::%s: invalid diagnostic access type \n
dict && dict->setObject(kCentauriPropertyPTMEnabledOnEndpoint, ptmStatus)
%s::%s: invalid crash log buffer \n
%s::%s: state: %s \n
%s::%s: id: %u state: %s \n
GetSubsystemBufferSize
WFL2G.txscr.bin
%s::%s: ss %u not yet registered \n
%s::%s: provider not available \n
AppleCentauriManager::SaveClientProperty(this, key, newValue, autoClearConditions) == kIOReturnSuccess
%s::%s: remote interface unavailable \n
WFRX.dmem.bin
%s::%s: timedout, current time: 0%llx, expected time: 0%llx - In idle state, ignoring timeout \n
RegisterServiceOrStartDextRecovery
%s::%s: failed to read BAR0 info \n
SendMemSwapInfoToSubsystem
NewUserClient_Impl
%s::%s: invalid memswap map or working copy desc \n
%s::%s: failed to copy completion block \n
FunctionReset
%s::%s: system-events-required property value: 0x%x \n
%s::%s: encountered error when writing to chain \n
%s::%s: invalid diagnostic controller \n
SendMemSwapInfo
%s::%s: failed to create error event action ret = 0x%x \n
ivars->dextRecoveryState == kCentauriDextRecoveryStateFetchMemSwap
ResetDone
On
%s::%s: WDMA bus error::%d \n
HasReenumerated
%s::%s: failed to get logging properties object \n
EnqueueDeferredWork
%s::%s: current timestamp is older than last reset timestamp, ignoring \n
prepareChipForResetStart
%s::%s: collecting coredump for ss %u, core %u, memory segments %u \n
%s::%s: failed to get dir name \n
%s::%s: failed to find MSI property \n
GetFilesFromHostBuffer
IsSartEnabled
%s::%s: failed to get provider queue \n
ivars->clientArray[id].client == client
%s::%s: For subsystem: %d total wdma nodes created: %d
%s::%s: failed to alloc metadata dict
%s::%s: allocated metadata copy
%s::%s: memswap callback not available for ss %u
%s::%s: airship service not ready
%s::%s: WDMA failed to start, WDMA Continuous error count::%d
%s::%s: WDMA buffer size is too small for this Coredump collection size: 0x%x CoreDumpOffset: 0x%x
%s::%s: unable to allocate crashlog buffer
%s::%s: invalid ss id (ss = %u)
%s::%s: finalize %d
%s::%s: ready for reset timed out
%s::%s: failed to trigger fault report (ret = 0x%x)
%s::%s: failed to set %s property (ret = 0x%x)
%s::%s: exec stage change to OS
%s::%s: msi recieved but response sent, WDMA Continuous error count::%d
%s::%s: bad args (ss id %u type %u)
%s::%s: ss: %u accessType: %u state: %s bufferSize: %u
%s::%s: driver offline - ignoring airship fatal error notification
%s::%s: crashlog size larger than buffer (%zu > %zu)
%s::%s: id: %u state: %s
%s::%s: time::%llu
%s::%s: create timer failed ret::%x
%s::%s: buffer filled, totalBytesPrinted: %u bufferSize: %u
%s::%s: skipping invalid crashlog item - index %u, id %u, address 0x%x, length %u
%s::%s: failed to get airship probe result
%s::%s: added file %s, size %zu
%s::%s: invalid bootstage 0x%x
%s::%s: fault reporter is busy
%s::%s: failed to create timer src (ret = 0x%x)
%s::%s: service notification (type: %llu)
%s::%s: bad size (got %u max %u)
%s::%s: resuming fatal log collection (state = 0x%x)
%s::%s: WDMA numChains: %u exceeds maxChains: %u
%s::%s: Clear WDMA from further running
%s::%s: failed to create pci error queue (ret = 0x%x)
%s::%s: failed to find msi capability (ret = 0x%x)
%s::%s: invalid crash log buffer
%s::%s: WDMA buffer addresses are invalid: 0x%x
%s::%s: bad section info for ss1: zero offset/len
%s::%s: crashlog table not configured
%s::%s: crashlog table invalid magic::%llx
%s::%s: returned from SetProperties (ret = 0x%x)
%s::%s: invalid cmd id: %u
%s::%s: crash poll iterations = %u
%s::%s: Prerequisite for collecting crashlog table info is completed
%s::%s: remote diagnostics completion callback for ss %u failed (ret = 0x%x)
%s::%s: service matching set up for %s
%s::%s: unexpected crash log completion
%s::%s: WDMA is busy !!!
%s::%s: FillChainLinkNode failed
%s::%s: failed to create array
%s::%s: secondary memory is not allocated
%s::%s: testID: %u
%s::%s: system-events-required property value: 0x%x
%s::%s: null watermark pointers: name: %s srcAddress: 0x%llx compIndex: %u chainID: %u startNode: %u
%s::%s: FillWDMANode failed
%s::%s: get crashlog table failed::%x
%s::%s: memswap cb no longer registered
%s::%s: match notification for AirshipDriverDK
%s::%s: failed to create osdata object for StateDump
%s::%s: FillMSINode failed
%s::%s: remote log collection not in progress
%s::%s: ss: %u
%s::%s: deferring due to low power
%s::%s: segment %s cannot be accessed via MMIO
%s::%s: failed to create os action token (ret = 0x%x)
%s::%s: failed to create memswap os action (ret = 0x%x)
%s::%s: reset already enqueued
%s::%s: selector %llu dispatch provided %s
%s::%s: failed to open doorbell
%s::%s: chip id: %u
%s::%s: bad arg
%s::%s: failed to create osdata object for %s
%s::%s: failed to serialize
%s::%s: encountered error when writing to chain
%s::%s: invalid fileName: %s
%s::%s: failed to get CentauriControlRemoteInterface
%s::%s: failed to enable ptm (ret = 0x%x)
%s::%s: error handler already exists
%s::%s: likely interrupted by host sleep on segment name: %s srcAddress: 0x%llx chainID: %u compIndex: %u startNode: %u
%s::%s: number of system events required is unsupported (0x%x), ignoring unsupported bits
%s::%s: new doorbell value: 0x%x
%s::%s: failed to copy reg newline in segmentdump
%s::%s: failure on fiq srcAddress: 0x%llx dstAddress: 0x%llx
%s::%s: bad args
%s::%s: failed to allocate pending work item
%s::%s: device control reg val: 0x%x
%s::%s: bad size of sectionInfoOSData (expected: %lu got: %lu)
%s::%s: reenumeration already triggered
%s::%s: Not valid controlPciService or queue
%s::%s: failed to alloc dict
%s::%s: link node not valid
%s::%s: BAR0 size::%llx and type::%d
%s::%s: Logging prop: owner: %s dir: %s file: %s id: %s
%s::%s: invalid diagnostic controller
%s::%s: empty crashlog table info
%s::%s: no pending requests
%s::%s: failed to get addr range (ret = 0x%x)
%s::%s: failed to alloc OSNumber for SS ID
%s::%s: InitWithOptions failed
%s::%s: unable to allocate coredump buffer
%s::%s: failed to copy deferredCb block
%s::%s: powerFlags: %s
%s::%s: requesting deferral (low power: %u, defer for memswap: %s)
%s::%s: setobject failed for segmentName::%s
%s::%s: register coredump disabled
%s::%s: enable: %u
%s::%s: unable to allocate crashlogData
%s::%s: failed to validate segment length (ret = 0x%x expected %llu got %llu)
%s::%s: MSICapOffset::%llx
%s::%s: failed to get default queue (ret = 0x%x)
%s::%s: susbsyteminfo is invalid
%s::%s: WDMA busy, retry after sleep
%s::%s: failed to merge dictionaries
%s::%s: failed to gather coredump for ss %u, core %u, memory segment %s
%s::%s: lpw -> on
%s::%s: invalid memswap map or working copy desc
%s::%s: function reset already in progress
%s::%s: no system event notifications required
%s::%s: timedout, current time: 0%llx, expected time: 0%llx - In idle state, ignoring timeout
%s::%s: Wdma runs had errors Continuously for max allowable times, cannot proceed to collect logs
%s::%s: failed to create sharedEndpointInfo dictionary
%s::%s: failed to create ss1 sub memory descriptor (ret = 0x%x)
%s::%s: failed to alloc OSNumber for real time
%s::%s: failed to copy collectLogs block
%s::%s: number of MSIs requested: %u
%s::%s: Watermark buffer size is not enough
%s::%s: driver offline - ignoring MSI notification
%s::%s: failed to create fault reporter
%s::%s: crashlog too small: %zu bytes
%s::%s: failed to allocate coredump dictionary
%s::%s: invalid state: 0x%x
%s::%s: Writing bar4offset to bar0 failed, readback got::%x
%s::%s: Invalid coreName or crashlogData observed
%s::%s: SART not enabled, skipping FIQ
%s::%s: airship reported fatal error: %s
%s::%s: SS0 offset: %llu size: %u SS1 offset: %llu size: %u SS2 offset: %llu size: %u
%s::%s: ss: %u accessType: %u state: %s
%s::%s: offline
%s::%s: remote interface unavailable
%s::%s: FLR count: %u
%s::%s: My msiAddr::%llx msiData::%x
%s::%s: failure on segment name: %s srcAddress: 0x%llx chainID: %u compIndex: %u startNode: %u
%s::%s: Invalid crash log table size::%x
%s::%s: cpl status: crashlog 0x%x coredump 0x%x
%s::%s: failed to save timestamp
%s::%s: not permitted
%s::%s: requesting crashlog failed (ret=0x%x)
%s::%s: failed to copy provider properties
%s::%s: prepare dma failed::%x
%s::%s: Transaction pending poll timed out. Proceeding to FLR
%s::%s: release PM assertion
%s::%s: skipping boot stage check
%s::%s: failed to save FLR timestamps
%s::%s: failed to copy reset block
%s::%s: reset failed (ret = 0x%x)
%s::%s: failed to set object in dict
%s::%s: failed to allocate fileName
%s::%s: FillWatermarkNode failed
%s::%s: deferred work is canceled
%s::%s: bad arguments
%s::%s: WDMA max Continuous error count reached
%s::%s: wdmaBuffer create failed::%x
%s::%s: match notification for CentauriRemoteInterface
%s::%s: ignoring based on boot-arg
%s::%s: failed to set reason object
%s::%s: failed super Start (ret = 0x%x)
%s::%s: failed to get airship driver
%s::%s: bad chain watermark at chainID: %u, failed before attempting to access an address from cores
%s::%s: Watermark saved fileName: %s chainID: %d
%s::%s: chip crash successful
%s::%s: chip reset callback not ready for ss %u
%s::%s: LPM log collection mode unsupported
%s::%s: failed to create sharedInfoDict
%s::%s: number of MSIs requested: %u (SingleMSI mode)
%s::%s: 
%s::%s: Invalid address, corrupt global address
%s::%s: WDMA buffer creation failed::%x
%s::%s: invalid parameter (ss = %u)
%s::%s: invalid number of cores for ss %u
%s::%s: failed to create IODMACommand (ret = 0x%x)
%s::%s: invalid number of MSIs requested: %u
%s::%s: %s; adding to queue
%s::%s: Invalid args
%s::%s: Prerequisite for collecting coredump completed
%s::%s: remote watchdog notification failed (ret = 0x%x)
%s::%s: failed to enable timer (ret = 0x%x)
%s::%s: completion
%s::%s: driver offline (state = %u)
%s::%s: pci read invalid data
%s::%s: failed to get core count for ss %u
%s::%s: crashlog segment observed index: %d address: 0x%x length: 0x%x
%s::%s: driver offline
%s::%s: Empty crashlog table::%x size: 0x%x
%s::%s: FLR limit (%u) reached
%s::%s: invalid segment info (addr: 0x%qx len: 0x%qx)
%s::%s: dmaconfig failed::%x
%s::%s: failed to open IOPCIDevice (ret = 0x%x)
%s::%s: error handler not registered
%s::%s: skipping during dext crash recovery
%s::%s: cached crashlogs not available
%s::%s: failed to set handler (ret = 0x%x)
%s::%s: WDMA dump err_addrl::%x err_addrh::%x
%s::%s: datapipe: failed to copy directory name %s
%s::%s: invalid fileStoreIndex: %u
%s::%s: Invalid WDMA buffer address
%s::%s: failed to add metadata to crashlog dict (ss %u)
%s::%s: failed to alloc metadata
%s::%s: failed to get logger
%s::%s: WDMA dump lnkl::%x lnkh::%x
%s::%s: failed to get IOPCIDevice
%s::%s: invalid diagnostic access type
%s::%s: errorSource: %u, errorCode: %u, arg: 0x%llx
%s::%s: no ptm key - bailing out
%s::%s: failed to get default queue
%s::%s: failed to get ecid lo
%s::%s: no
%s::%s: failed to set ptm status in subsystem properties (ret = 0x%x)
%s::%s: device id: 0x%x
%s::%s: WDMA failed to recover with status::%d
%s::%s: failed to get logger queue
%s::%s: crashlog table info - address 0x%x, length 0x%x
%s::%s: failed to create data log stream
%s::%s: failed to schedule immediate wake
%s::%s: caching crashlog
%s::%s: invalid driver state %u for dext crash recovery state %u
%s::%s: empty crash log buffer
%s::%s: ValidateReceivedCrashlogTable failed
%s::%s: failed to set enable int source (ret = 0x%x)
%s::%s: failed to get provider
%s::%s: ContinueWDMA chain ends
%s::%s: failed to get logging properties object
%s::%s: failed to get MSI data (ret = 0x%x)
%s::%s: timer expired waiting for memswap info in dext crash recovery state
%s::%s: memory allocation crashlog reason string failed
%s::%s: current timestamp is older than last reset timestamp, ignoring
%s::%s: timed out while paused
%s::%s: WDMA retry didn't work, state::%x
%s::%s: first power on
%s::%s: chip class not initialized
%s::%s: Crashlog Reason: \"%s\"
%s::%s: About to reset
%s::%s: failed to create IOBMD (ret = 0x%x)
%s::%s: Invalid segmentName or segmentDump observed
%s::%s: invalid length (working copy %llu t0 %llu)
%s::%s: chip crash timed out
%s::%s: secondary mem not allocated
%s::%s: failed to get chip object
%s::%s: unable to allocate segment name
%s::%s: failed to read BAR0 info
%s::%s: Stop ret = 0x%x
%s::%s: failed to create user client (ret = 0x%x)
%s::%s: failed to create doorbell
%s::%s: failed to activate doorbell
%s::%s: AppleCentauriManager::DoReenumeration failed (ret = 0x%x)
%s::%s: failed to EnablePCIPowerManagement (ret = 0x%x)
%s::%s: failed to configure interrupts (ret = 0x%x)
%s::%s: failed to report error (ret = 0x%x)
%s::%s: invalid state (%u)
%s::%s: remote collect logs callback for ss %u failed (ret = 0x%x)
%s::%s: failed to create data log pipe
%s::%s: failed to set boot complete property (ret = 0x%x)
%s::%s: memswap memory is already DART mapped
%s::%s: FLR timeout override: %u ms
%s::%s: failed to allocate fileStore buffer
%s::%s: WDMA buffer addresses are invalid::%x
%s::%s: failed to read BAR4 info
%s::%s: replacing existing client info for ss %u
%s::%s: driver offline - ignoring exec stage notification
%s::%s: driver offline - ignoring airship error notification
%s::%s: failed to set airship driver config
%s::%s: log collection already enqueued
%s::%s: initialized MSI-%u
%s::%s: failed to allocate lock
%s::%s: failed to get dir name
%s::%s: centauri-driverkit=0
%s::%s: unexpected termination notification
%s::%s: new exec stage: %u
%s::%s: failed to create reason string copy
%s::%s: state %u
%s::%s: timer action attach failed
%s::%s: WDMA channel is errored out !!!
%s::%s: in low power
%s::%s: centauri-disable-coredump=%u
%s::%s: client: %s
%s::%s: failed to set up time object
%s::%s: failed to create osdict
%s::%s: failed to find MSI property
%s::%s: exceeded maximum number of components, numComponents: %u maxComponents: %u
%s::%s: LPM
%s::%s: invalid capabilities
%s::%s: BAR4 size::%llx and type::%d
%s::%s: failed to create logger queue (ret = 0x%x)
%s::%s: Trying to clear out WDMA errors
%s::%s: memswap info not available yet
%s::%s: failed to get ptm capability (ret = 0x%x)
%s::%s: failed to copy properties
%s::%s: found crashlog data for %s
%s::%s: Not a valid Crashlog table, magic recieved::%llx
%s::%s: bad args (ss = %u)
%s::%s: invalid crashlog data
%s::%s: crashlog size::%x is invalid
%s::%s: invalid parameter
%s::%s: timer expired waiting for remote service in reset failed state
%s::%s: cmd id %u ret 0x%x
%s::%s: boot stage = ready for reset
%s::%s: log collection in progress/enqueued
%s::%s: failed to RestoreDeviceState (ret = 0x%x)
%s::%s: timeout::current time::%llx, expected time::%llx - redundant timer happened, so skip
%s::%s: experienced an error earlier, ending coredump
%s::%s: AppleCentauriManager::Open failed (ret = 0x%x)
%s::%s: failed to  SearchProperty (ret = 0x%x)
%s::%s: invalid client
%s::%s: failed to alloc OSNumber for up time
%s::%s: failed to create function name copy
%s::%s: invalid memswap DMA command
%s::%s: trying to recover WDMA
%s::%s: Invalid diagnosticState: %s
%s::%s: invalid parameters
%s::%s: GetBusyState ret = 0x%x
%s::%s: Close ret = 0x%x
%s::%s: poll count %u
%s::%s: failed to copy block
%s::%s: StartWDMAConfig failed in config
%s::%s: bad section info for ss0: zero offset/len
%s::%s: msiaddr::%llx
%s::%s: getCrashlogTableInfo failed: 0x%x
%s::%s: unexpected crashlog completion
%s::%s: collect logs callback not ready for ss %u
%s::%s: client no longer valid; dropping completion
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu
%s::%s: failed to allocate comp buffer
%s::%s: failed to make a copy of sharedClientInfo
%s::%s: reset in progress. ignoring error
%s::%s: dispatching cached errors
%s::%s: ASPM state: %u
%s::%s: ivars creation failed
%s::%s: wdma is error free !!!
%s::%s: failed to copy immediateCb block
%s::%s: failed HasPCIPowerManagement (ret = 0x%x)
%s::%s: WDMA no interrupts to clear
%s::%s: stream: failed to copy log identifier %s
%s::%s: invalid subsystem core info
%s::%s: pmcsr 0x%04x
%s::%s: requesting coredump failed (ret=0x%x)
%s::%s: MSI received is spurious or may be a response previous log collection timeout
%s::%s: tearing down monitor
%s::%s: setObject failed for fileName: %s
%s::%s: wdmaChIntrStatus::%x
%s::%s: manager failed to set chip identifiers (ret = 0x%x)
%s::%s: failed to get sharedClientInfo (ret = 0x%x)
%s::%s: using console log level %u
%s::%s: logger not available
%s::%s: failed to get queue (ret = 0x%x)
%s::%s: super InitWithOptions failed
%s::%s: failed to copy prepareCb block
%s::%s: replacing existing client
%s::%s: bad max size
%s::%s: reserved MSIs via provider
%s::%s: WDMA Failed continuous error count: %u ss: %u state: %s
%s::%s: Chain::%llu srcaddr::%llx dstaddr::%llx bytes::%x nodenum::%x
%s::%s: No Controller error status observed::%d
%s::%s: error source not found for %s
%s::%s: invalid fileStoreIndex: %d
%s::%s: ProcessCrashlogTable total::%d
%s::%s: WDMA dump cfg::%x ext_cfg::%x
%s::%s: invalid number of MSIs requested: %u available: %u
%s::%s: id::%d crashlogTableSize::%x
%s::%s: failed to allocate metadata dict
%s::%s: crash log buffer too small: %zu bytes
%s::%s: %s
%s::%s: WDMA bus error::%d
%s::%s: WDMA timedout but no errors observed!!
%s::%s: invalid chipInfo 0x%x
%s::%s: logpipe: failed to copy directory name %s
%s::%s: options 0x%x reason %s
%s::%s: airship not up; returning %s
%s::%s: failed to save control dext timestamps, ret = 0x%x
%s::%s: local log collection not in progress
%s::%s: SART not enabled (capabilities = 0x%x)
%s::%s: using cc log level %u
%s::%s: invalid state for watchdog notification: %u
%s::%s: cachedErrorCount: %u
%s::%s: remote log collection failed (ret = 0x%x)
%s::%s: invalid viddid 0x%x
%s::%s: ss %u
%s::%s: remote interface error (ret = 0x%x)
%s::%s: sleeping for %u ms...
%s::%s: failed to set dext relaunch property (ret = 0x%x)
%s::%s: Timer period set to %llu milliseconds and next timer expiry expected at ::%llu current time in ns::%llu
%s::%s: wdma link node not valid
%s::%s: failed to copy reg addr in segmentdump
%s::%s: WDMA recovery failed with status::%d\n
%s::%s: failed to create os action (ret = 0x%x) for client %u
%s::%s: invalid segment count %u
%s::%s: failed to allocate segmentname
%s::%s: WDMA chain count is more than expected::%d
%s::%s: size %u
%s::%s: failed to create dict
%s::%s: failed to alloc OSString
%s::%s: invalid input dictionary - bailing out
%s::%s: PCI dart error
%s::%s: invalid length
%s::%s: failed to allocate segmentDump
%s::%s: failed to get ecid hi
%s::%s: ss %u not yet registered
%s::%s: failed to get log id
%s::%s: failed to prepare for DMA (ret = 0x%x)
%s::%s: pci device not open
%s::%s: failed to send %s (ret=0x%x)
%s::%s: failed to create IOServiceStateNotificationDispatchSource (ret = 0x%x)
%s::%s: exceeded maximum number of descriptors, nodeIndex: %u maxDescriptors: %u
%s::%s: id::%d crashlogTableAllocatedSize::%x numComponents::%d
%s::%s: invalid notifier
%s::%s: Diagnostics MSI not enabled
%s::%s: reading crashlog item - index %u, id %u, address 0x%x, length %u
%s::%s: failed to get the fault reporter additional owner
%s::%s: failed to update the FW crash reason string
%s::%s: error handler has been deregistered
%s::%s: failed to set dict object for StateDump
%s::%s: In paused state
%s::%s: WDMA chain corrupt currChain: %u numChains: %u
%s::%s: WDMA dump inter::%x err::%x
%s::%s: chip crash with fiq timed out
%s::%s: data::%x
%s::%s: invalid control service
%s::%s: failed to create memswap working copy OSData
%s::%s: log collection completion already exists
%s::%s: deliver notification error (ret = 0x%x)
%s::%s: error arg not an OSNumber
%s::%s: resuming reset (state = 0x%x)
%s::%s: WDMA buffer allocation failed::%x
%s::%s: MSI data address are invalid
%s::%s: allocated buffer size: 0x%x
%s::%s: invalid parameters (ss = %u)
%s::%s: invalid parameters (ss = %u type = %u)
%s::%s: ValidateCrashlogTableSize failed
%s::%s: failed to create memory map (ret = 0x%x)
%s::%s: failed to create error event action ret = 0x%x
%s::%s: ret = 0x%x
%s::%s: WDMA dump ctrl::%x status::%x
%s::%s: ss %u type %u
%s::%s: crashlog handler already exists
%s::%s: chunkBase 0x%x, chunkOffset 0x%x, bar4Size 0x%x, chunkLimit %u, chunkLength %d\n
%s::%s: no pending completion (ss = %u)
%s::%s: skipping %s
%s::%s: failed to copy system state service (ret = 0x%x)
%s::%s: invalid provider
%s::%s: failed to acquire resource
%s::%s: get timeout failed
%s::%s: invalid section info
%s::%s: failed to allocate chip object for CentauriChipControlT2026
%s::%s: logpipe: failed to copy log identifier %s
%s::%s: ValidateReceivedCrashlogTable failed for numComponents::%d
%s::%s: invalid crashlog segment observed index: %d address: 0x%x length: 0x%x
%s::%s: unable to allocate crashlog table
%s::%s: failed to get MSI addr (ret = 0x%x)
%s::%s: powerFlags: %u
%s::%s: PCI dart error %u: [%s] addressLo: 0x%x addressHi: 0x%x
%s::%s: failed to set dict object for %s
%s::%s: buffer size %u exceeds expected max %u
%s::%s: state: %s
%s::%s: WDMA subordinate error::%d
%s::%s: WDMA decrementor error::%d
%s::%s: failed to create msi interrupt source (ret = 0x%x)
%s::%s: failed to allocate osstring
%s::%s: CentauriCrashlog info - magic %llx, version %u, numberOfLogs %u
%s::%s: failed to set monotonic time object
%s::%s: invalid watchdog status (0x%x)
%s::%s: watchdog cb no longer registered
%s::%s: failed to get owner object
%s::%s: failed to get coredump info
%s::%s: FLR limit override boot-arg is set
%s::%s: %u
%s::%s: client already registered (%s)
%s::%s: log collection failed (ret = 0x%x)
%s::%s: Corrupted crash log table size::%x
%s::%s: error appending bytes to bufferObject
%s::%s: invalid viddid
%s::%s: dispatching propertyUpdateNotification
%s::%s: failed to set real time object
%s::%s: ptm not supported
%s::%s: logpipe: failed to copy file name %s
%s::%s: errorCode %u, reason %s
%s::%s: in reset state
%s::%s: failed to get user client service
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x
%s::%s: Performance check - Total time taken for %s collection for subsystem::%d is::%llu nano seconds
%s::%s: invalid state: %u
%s::%s: module name not found
%s::%s: Requested buffer size::%x
%s::%s: failed to create os action (ret = 0x%x)
%s::%s: Failed to collect partial collected files
%s::%s: invalid callback parameters
%s::%s: failed to get logging properties dict
%s::%s: invalid state (%s)
%s::%s: crashlog header reports empty: %zu bytes
%s::%s: MSI address not valid
%s::%s: subsystem: %d
%s::%s: chip rev: 0x%x
%s::%s: failed to get crashlog table info (ret = 0x%x)
%s::%s: failed to create timer action (ret = 0x%x)
%s::%s: boot stage: %s, fw state: %s
%s::%s: Create Timer failed
%s::%s: Invalid config exists state: %d segmentDump: %u compIndex: %u fileStoreIndex: %u
%s::%s: subsystem: %u status: 0x%x
%s::%s: failed to create service (ret = 0x%x)
%s::%s: failed to set os action handler (ret = 0x%x)
%s::%s: failed to get iopcidevice
%s::%s: ret: 0x%x flags: 0x%qx cnt: %d addr: 0x%qx len: 0x%qx
%s::%s: Link is down, coredump is not permitted
%s::%s: pci device not available
%s::%s: failed to SaveDeviceState (ret = 0x%x)
%s::%s: Open error (ret = 0x%x)
%s::%s: failed to create dispatch src (ret = 0x%x)
%s::%s: failed to copy completion block
%s::%s: failed to allocate statedump buffer
%s::%s: failed to allocate OSData
%s::%s: crashlogTable numberOfLogs: %d
%s::%s: system state notifications activated
%s::%s: failed to set properties (ret = 0x%x)
%s::%s: failed to set SS ID object
%s::%s: failed to create log pipe with provider %s
%s::%s: SetProperties failed
%s::%s: failed to create working copy IOBMD (ret = 0x%x)
%s::%s: invalid stopIndex: %u
%s::%s: wdma debug level not matching
%s::%s: coredump/crashlog completion failed (ret=0x%x)
%s::%s: failed to create os action for watchdog notification (ret = 0x%x)
%s::%s: initialized MSI-1
%s::%s: clearing cfg mbx at offset 0x%x
%s::%s: bad section info for ss2: zero offset/len
%s::%s: StartWDMAConfig failed
%s::%s: StartTimer failed
%s::%s: failed to setobject in crashlogdict
%s::%s: adding new client info for ss %u
%s::%s: super init failed
%s::%s: Driver offline. Ignoring state change %u
%s::%s: number of crashlogs: %u
%s::%s: WDMA is recovered from errors
%s::%s: Invalid FIQ address
%s::%s: Force the WDMA to clear its errors
%s::%s: unexpected coredump completion
%s::%s: segment name is invalid for id %u\n
%s::%s: subsystem id: %u
%s::%s: error code not found
%s::%s: section too small
%s::%s: bad arg (sectionInfoOSData)
%s::%s: failed to remove property (ret = 0x%x)
%s::%s: deferring reset
%s::%s: boot stage = %s
%s::%s: ptm requester role not supported
%s::%s: no shared endpoint info
%s::%s: failed to gather crashlog for ss %u, {0x%x, 0x%x}
%s::%s: escalate FLR failure
%s::%s: failed to copy service name (ret = 0x%x)
%s::%s: failed to create file name copy
%s::%s: secondary memory already allocated
%s::%s: ss %d
%s::%s: AppleCentauriManager::ChipReset failed (ret = 0x%x)
%s::%s: crash handler has been deregistered
%s::%s: unable to allocate crashlog dictionary
%s::%s: power assertion already held
%s::%s: unable to allocate segmentDump
%s::%s: timer expired waiting for remote service in dext crash recovery state
%s::%s: working copy content: 0x%x len: %llu
%s::%s: invalid metadata dict
%s::%s: Segment: 0x%x Cannot be accessed via WDMA
%s::%s: failed to get log file name
%s::%s: bad arg (type: %llu)
%s::%s: Using FLR limit: %u
%s::%s: failed to create chip reset os action (ret = 0x%x)
%s::%s: invalid number of MSIs configured: %u
%s::%s: failed to copy reg data in segmentdump
%s::%s: failure on crashlog table: 0x%llx dstAddress: 0x%llx
%s::%s: failed to setobject in coredumpdict
%s::%s: os action wait failed (ret = 0x%x)
%s::%s: ErrorDetected's value type is not a dictionary
%s::%s: in fatal error state (%u)
%s::%s: failed to create monitor
%s::%s: WDMA buffer getaddressrange is invalid::%x phyMemSegment.length::%llx verifyRange.length::%llx
%s::%s: subsystem: %u
%s::%s: bad section info: overlaps
%s::%s: provider not available
%s::%s: failed to create airship transport
%s::%s: didDextRelaunch = %s (reason %u)
%s::%s: invalid state for reset %u
%s::%s: failed to start super (ret = 0x%x)
%s::%s: WDMA timed out: continuous error count %u, ss %u state %s
%s::%s: missing memswap config; triggering client launch
%s::%s: coredump for ss %u %s permitted
%s::%s: failed to create log stream
%s::%s: invalid filename/statedump
%s::%s: log collection failed (ret=0x%x)
%s::%s: fw crash reason string is not supported with non-fatal log collection
%s::%s: remote memswap call failed (ret = 0x%x)
%s::%s: unexpected match notification
%s::%s: crashlog handler is not registered
%s::%s: failed to create reset timestamps dict
%s::%s: failed to create reset state item (ret=0x%x)
%s::%s: propertyUpdateNotification handler not registered
%s::%s: WDMA dump dst_addrl::%x dst_addrh::%x
%s::%s: driver %s - ignoring MSI notification
%s::%s: failed to create airship client
%s::%s: failed to store data in fileStore
%s::%s: Bar4size::%llx greater than 16MB so reducing to 16MB
%s::%s: WDMA is available and working!!
%s::%s: failed to allocate inFlightLock
%s::%s: %s property exists - skipping dext crash
%s::%s: WDMA completes successfully after %u continous errors. Resetting error count
%s::%s: failed to create os action for collect logs (ret = 0x%x)
%s::%s: failed to create osdata object
%s::%s: dext crash error property exists
%s::%s: failed to create user class dict
%s::%s: failed to copy reg colon1 in segmentdump
%s::%s: Get buffer size failed: 0x%x
%s::%s: diagnostic type %u already in progress for ss %u
%s::%s: sizeof got::%x CrashlogInfo::%lx CrashlogItemInfo::%lx maxComponents::%d minSize::%x maxSize::%x
%s::%s: termination notification for AirshipDriverDK
%s::%s: error source %u code %u arg %llu
%s::%s: tp poll count %u
%s::%s: failed to find ptm capability (ret = 0x%x)
%s::%s: Partial fill file name exceeds max strlen
%s::%s: block copy failed
%s::%s: MSI handler: boot stage = %u
%s::%s: invalid link control value
%s::%s: timer source is invalid
%s::%s: Crashlog processing
%s::%s: link down detected after error detect
%s::%s: failed to get provider queue
%s::%s: failed to copy completionCb block
%s::%s: failed to set require client property (ret = 0x%x)
%s::%s: Invalid segname or segdump
%s::%s: WDMA dump src_addrl::%x src_addrh::%x
%s::%s: selector %llu
%s::%s: not permitted for ss id %u
%s::%s: full chip reset in progress
%s::%s: deferring (state = 0x%x)
%s::%s: failed to find PCI capability (ret = 0x%x)
%s::%s: signature mismatch
%s::%s: segment is null
%s::%s: GetCrashlogMaxNumSegments failed
%s::%s: failed to find aer capability (ret = 0x%x)
%s::%s: create timer set handler failed
%s::%s: invalid crashlog size: 0x%x
%s::%s: collected coredump for ss %u, core %u, memory segment %s, total size 0x%x
%s::%s: ptm enabled, clock granularity: %u ns
%s::%s: Timer expired with reset flag set
%s::%s: collecting coredump for ss %u, core %u, memory segments %u
%s::%s: failed to get platform (ret = 0x%x)
%s::%s: error reported by %s error code %u
%s::%s: invalid state for log collection %u
%s::%s: system-events-required property search failed (ret = 0x%x)
%s::%s: Invalid compIndex: %u
%s::%s: Crashlog table address: 0x%x table size: 0x%x
%s::%s: bad section info: exceeds sec mem range
%s::%s: unable to allocate crashlogKey
%s::%s: CentauriCrashlog item - index %u, id %u, address 0x%x, length %u
%s::%s: wakeattime for start timer failed ret::%x
%s::%s: failed to copy reg colon2 in segmentdump
%s::%s: error filling buffer, bytesPrinted: %d kLineLength: %u
%s::%s: failed to create chip object for family %u
%s::%s: FLR timed out
%s::%s: failed to allocate crashlog dictionary
%s::%s: Wdma runs had errors Continuously for max allowable times, need to reset the chip
%s::%s: subsystem %u, component %u, numSegments %u
%s::%s: state = %u
%s::%s: handler already exists
%s::%s: memswap memory map is already set
%s::%s: ss %u watchdog reported
%s::%s: airship reported error: 0x%x
%s::%s: remote service unavailable. wait for %u ms
%s::%s: failed to set dict object
%s::%s: Crashlog Reason not found from the Crashlog data
%s::%s: bad diagnosticState: %s
%s::%s: Exceeded collection timeout
%s::%s: buffer size invalid::%x
%s::%s: Valid file::%s added
%s::%s: CollectCoredump allocated buffer sizeKB::%d
%s::%s: Forcefully abort the currently running WDMA channel
%s::%s: failed to get chip id
%s::%s: ValidateReceivedCrashlogTable failed for size allocated::%d current::%d
%s::%s: failed to create ss2 sub memory descriptor (ret = 0x%x)
%s::%s: subsystem %d, numSegments %d
%s::%s: remote chip reset callback for ss %u failed (ret = 0x%x)
%s::%s: failed to allocate memory
%s::%s: termination notification for CentauriRemoteInterface
%s::%s: failed to create completion os action (ret = 0x%x)
%s::%s: requesting full wake
%s::%s: failed to alloc OSNumber for monotonic time
%s::%s: system events required: 0x%x
%s::%s: failed to alloc OSData
```
