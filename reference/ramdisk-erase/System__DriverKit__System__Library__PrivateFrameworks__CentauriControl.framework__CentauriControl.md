# `/System/DriverKit/System/Library/PrivateFrameworks/CentauriControl.framework/CentauriControl`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,173,680 bytes.

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
errorDataObj != nullptr
%s::%s: sleeping for %u ms... \n
%s::%s: driver %s - ignoring MSI notification \n
LPMOS
%s::%s: failed to alloc OSData \n
CentauriControl:\n
%s::%s: ValidateReceivedCrashlogTable failed for numComponents::%d \n
centauri-recovery
ReleasePMAssertion(ivars->pmAssertionID) == kIOReturnSuccess
%s::%s: invalid state for watchdog notification: %u \n
%s::%s: exec stage change to OS \n
ForceAbortWDMA
DoReset
DerivedCollectLogs_block_invoke
%s::%s: collected coredump for ss %u, core %u, memory segment %s, total size 0x%x \n
No
%s::%s: GetBusyState ret = 0x%x \n
CollectLogsCallback_Impl
%s::%s: For subsystem: %d total wdma nodes created: %d \n
md
%s::%s: allocated metadata copy \n
Stop_Impl_block_invoke
%s::%s: Open error (ret = 0x%x) \n
%s::%s: new exec stage: %u \n
MSI-2
CollectMemoryLog
%s::%s: WDMA is recovered from errors \n
%s::%s: ss %u type %u \n
%s::%s: using cc log level %u \n
%s::%s: failed to create timer action (ret = 0x%x) \n
%s::%s: SetProperties failed \n
WFL5G.regdump.bin
%s::%s: Invalid segname or segdump \n
HandleBadWatermark
%s::%s: bad args \n
%s::%s: finalize %d \n
%s::%s: invalid notifier \n
airshipService: %s\n
%s::%s: failed to find MSI property \n
ExtractCrashlogReason
CollectLogsFatal
%s::%s: failed to copy deferredCb block \n
%s::%s: subsystem id: %u \n
report-error
WatchdogCallback_Impl
%s::%s: Watermark buffer size is not enough \n
%s::%s: StartWDMAConfig failed in config \n
%s::%s: failed to report error (ret = 0x%x) \n
%s::%s: ignoring based on boot-arg \n
%s::%s: reset failed (ret = 0x%x) \n
%s::%s: failed to set SS ID object \n
%s::%s: failed to get provider \n
%s::%s: invalid diagnostic access type \n
Fiq
%s::%s: selector %llu dispatch provided %s \n
%s::%s: failed to send %s (ret=0x%x) \n
FetchMemSwap
Crashlog.WFRX.bin
%s::%s: failed to start super (ret = 0x%x) \n
B24@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}16
EndWork
Crashlog.WFL2G.bin
obj
timeElapsedObject != nullptr
waitingForReadyForReset
Crashlog.WFSC.bin
%s::%s: failed to enable ptm (ret = 0x%x) \n
%s::%s: failed to get coredump info \n
%s::%s: failed to create dispatch src (ret = 0x%x) \n
%s::%s: PCI dart error %u: [%s] addressLo: 0x%x addressHi: 0x%x \n
WFL2G.recipeoverride.bin
%s::%s: Create Timer failed \n
%s::%s: wdma debug level not matching \n
%s::%s: no shared endpoint info \n
TriggerReenumeration
%s::%s: offline \n
SetRequireClientProperty
%s::%s: current timestamp is older than last reset timestamp, ignoring \n
%s::%s: wakeattime for start timer failed ret::%x \n
completion
bootStageOSControl
%s::%s: deliver notification error (ret = 0x%x) \n
flrCount && *flrCount
WFTX.regdump.bin
metadata = GetLogCollectionMetadata()
val != nullptr
MemoryReadBAR4
%s::%s: timer expired waiting for remote service in reset failed state \n
InitMemSwapWorkingCopy
readyForReset
WFP2G.aslr.bin
BT2G.imem.bin
%s::%s: wdma is error free !!! \n
%s::%s: WDMA dump src_addrl::%x src_addrh::%x \n
ivars->controlPciService->SetASPMState(false) == kIOReturnSuccess
%s::%s: failed to copy completionCb block \n
%s::%s: failed to set dext relaunch property (ret = 0x%x) \n
%s::%s: failed to alloc OSString \n
hasReenumeratedDict->setObject(kCentauriControlPropertyHasReenumerated, ivars->hasReenumerated ? kOSBooleanTrue : kOSBooleanFalse)
Metadata
SendWatchdogNotification
i8@?0
%s::%s: match notification for CentauriRemoteInterface \n
BTMAIN.regdump.bin
%s::%s: failed to get logging properties object \n
%s::%s: empty crash log buffer \n
TimeElapsed
WFL2G.txscr.bin
Stop_Impl
ashpRet == AIRSHIP_OK || ashpRet == AIRSHIP_ENOTREADY
CentauriConfigAccessLog.txt
CollectStateSnapshots
CreateWDMABuffer
%s::%s: log collection completion already exists \n
ClientOpen
%s::%s: failed to alloc OSNumber for real time \n
    type: %s\n
OSAction_CentauriSubsystem_TimerOccurred
%s::%s: subsystem: %u status: 0x%x \n
!ivars->logCollectionInfo.crashlogPending && !ivars->logCollectionInfo.coredumpPending
ValidateCrashlogTableSize
%s::%s: failed to get platform (ret = 0x%x) \n
%s::%s: resuming reset (state = 0x%x) \n
Crashlog.BT2G.bin
systemStateEventName
TriggerFaultReport
%s::%s: state: 0x%x \n
ROM
%s::%s: failed to validate segment length (ret = 0x%x expected %llu got %llu) \n
kAudioMessage_ReceiverOn
errorSource == kCentauriErrorSourceCentauri
%s::%s: no pending completion (ss = %u) \n
LoggingProperties
ivars->cachedCrashlogsArray->getCount() > 0
WFL5G.recipeoverride.bin
        crashlogPending: %d\n
%s::%s: invalid watchdog status (0x%x) \n
SendChipResetNotification
CollectLogs
%s::%s: no ptm key - bailing out \n
%06llu.%06llu CollectLogs Complete ret: 0x%03x\n
%s::%s: remote diagnostics completion callback for ss %u failed (ret = 0x%x) \n
%s::%s: requesting full wake \n
%s::%s: failed to remove property (ret = 0x%x) \n
SetErrorHandler_block_invoke
SendTimeSinceLastFLRAnalytics
WFL2G.imem.bin
BTMAIN.memswapptt.bin
%s::%s: ss %u \n
%s::%s: invalid client \n
SystemStateNotificationReady_Impl
ivars->controlPciService->SetASPMState(true) == kIOReturnSuccess
%s::%s: bad section info for ss2: zero offset/len \n
*crashlogFile
%s::%s: get crashlog table failed::%x \n
CollectLogsCompletion_Impl_block_invoke
startTimeObject && endTimeObject
OSAction_CentauriControl_DiagnosticsInterruptOccurred
%s::%s: invalid state (%s) \n
val
%s::%s: In paused state \n
FillWDMAConf
%s::%s: susbsyteminfo is invalid \n
blockCopy
diagnosticType && diagnosticName
GetDiagnosticState() == kCentauriDiagnosticStateIdle
CheckWatermarks
ContinueWDMA
ControlDextCrashError
%s::%s: invalid viddid \n
%s::%s: stream: failed to copy log identifier %s \n
PrintCrashlogInfo
%s::%s: match notification for AirshipDriverDK \n
userClient
IsValidClient
%s::%s: logpipe: failed to copy log identifier %s \n
%s::%s: bad size (got %u max %u) \n
com.apple.ConnectivityDriver.FLRPerformanceStats
WFRX.dmem.bin
BTLPS.imem.bin
%s::%s: ContinueWDMA chain ends \n
%s::%s: bad args (ss id %u type %u) \n
DerivedInterruptOccurred
%s::%s: failed to gather coredump for ss %u, core %u, memory segment %s \n
%s::%s: failed to copy service name (ret = 0x%x) \n
Control
Crashlog.WFP2G.bin
OSAction_CentauriSubsystem_WatchdogCallback
is
%s::%s: segment name is invalid for id %u\n \n
fChipDiagnostics
Start_Impl_block_invoke_2
AbortHandler
i40@?0^^{OSDictionary}8^^{OSDictionary}16^^{OSDictionary}24^^{OSString}32
AppleCentauri-129
%s::%s: ASPM state: %u \n
wdma-error-
%s::%s: failed to create os action (ret = 0x%x) for client %u \n
%s::%s: found crashlog data for %s \n
NA
%s::%s: coredump/crashlog completion failed (ret=0x%x) \n
%s::%s: InitWithOptions failed \n
%s::%s: failed to get provider queue \n
InitializeMSI
UpTimestamp
v8@?0
%s::%s: remote log collection not in progress \n
%s::%s: ValidateCrashlogTableSize failed \n
SetProperties_Impl
%s::%s: Invalid FIQ address \n
%s::%s: failed to setobject in crashlogdict \n
Crashlog
%s::%s: failed to create completion os action (ret = 0x%x) \n
WatchdogCallback_Impl_block_invoke
%s::%s: invalid number of MSIs requested: %u \n
ErrorCode
WFRX.rtmem.bin
StartTimer
N/A
null
%s::%s: Link is down, coredump is not permitted \n
CompleteFaultReportCb
%s::%s: powerFlags: %u \n
Reset
ClientCrashlogHandler
%s::%s: failed to get MSI addr (ret = 0x%x) \n
SetupRemoteActionCallbacks
%06llu.%06llu SetupMemSwapRegion ret: 0x%03x\n
CollectMSILog
OSAction_CentauriSubsystem_CentauriManagerErrorHandler
%s::%s: invalid subsystem core info \n
ivars->timerSource
ivars->pciDevice
%s::%s: Invalid crash log table size::%x \n
%s::%s: provider not available \n
%s::%s: error handler not registered \n
%s::%s: chip crash timed out \n
CollectConfigLogs
true
OSAction_CentauriSubsystem_MemSwapCallback
%s::%s: system-events-required property search failed (ret = 0x%x) \n
buffer
crashlogFile
Close_Impl
%s::%s: failed to  SearchProperty (ret = 0x%x) \n
B16@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8
%s::%s: failed to allocate statedump buffer \n
BTSEC.itcm.bin
%s::%s: failure on fiq srcAddress: 0x%llx dstAddress: 0x%llx \n
%s::%s: failed to allocate fileStore buffer \n
%s::%s: register coredump disabled \n
%s::%s: failed super Start (ret = 0x%x) \n
CollectImmediateFaultDataCb
segmentsPerCore && numCores && lpmStatePerCore
(ss < fNumSubsystems) && fSubsystemList && fSubsystemList[ss]
remoteInterfaceAvailable: %d\n
%s::%s: setObject failed for fileName: %s \n
%s::%s: ss %u not yet registered \n
ValidateReceivedCrashlogTable
ChipResetCallback_Impl
!ivars->deferredWork.logCollection
%s::%s: poll count %u \n
%s::%s: Crashlog Reason: \"%s\" \n
WiFi
%s::%s: ss: %u \n
DriverLogs
%s::%s: failed to get core count for ss %u \n
%s::%s: msi recieved but response sent, WDMA Continuous error count::%d \n
coredumpFile
%s::%s: failed to copy completion block \n
0x%04llu %06llu.%06llu - %06llu.%06llu - %06llu.%06llu %s\n
%s::%s: errorSource: %u, errorCode: %u, arg: 0x%llx \n
%s::%s: %s \n
%s::%s: ss %d \n
loggerstream
%06llu.%06llu SaveDeviceState ret: 0x%03x\n
InReset
centauri-flr-limit
%s::%s: failed to copy reg colon2 in segmentdump \n
%s::%s: WDMA channel is errored out !!! \n
!isFiq || ivars->subsystemId == 0
%s::%s: failed to create array \n
%s::%s: enable: %u \n
CheckWDMAStatus
%s::%s: WDMA retry didn't work, state::%x \n
FaultReporter
suspended
%s::%s: id::%d crashlogTableSize::%x \n
%s::%s: failed to get user client service \n
%s::%s: driver offline (state = %u) \n
%s::%s: tp poll count %u \n
ret == kIOReturnSuccess
%s::%s: BAR0 size::%llx and type::%d \n
LogFileName
PrepareFaultReportCb
ivars->finalizeHandler
flrCountDict->setObject(kCentauriFLRCount, flrCountObject)
fLock
LPMBoot
%s::%s: failed to get airship driver \n
%s::%s: unable to allocate crashlogKey \n
FetchMemSwapInfo_Impl
%s::%s: chip reset callback not ready for ss %u \n
ExecStageChanged
%s::%s: new doorbell value: 0x%x \n
GetCrashlogMaxNumSegments
%s::%s: termination notification for AirshipDriverDK \n
%s::%s: options 0x%x reason %s \n
%s::%s: device control reg val: 0x%x \n
LogIdentifier
InitWithProviderAndOptions
IOService
%s::%s: likely interrupted by host sleep on segment name: %s srcAddress: 0x%llx chainID: %u compIndex: %u startNode: %u \n
BadWatermark
%s::%s: bad max size \n
UnexpectedDextTermination
WFL2G.aslr.bin
%s::%s: logpipe: failed to copy file name %s \n
%s::%s: datapipe: failed to copy directory name %s \n
%s::%s: About to reset \n
%s::%s: failed to copy collectLogs block \n
BTMAIN.seqsram.bin
ivars->dmaChains.comp[compIndex].startNodeIndex != 0
ivars->cachedErrorsArray->setObject(cachedError)
%s::%s: returned from SetProperties (ret = 0x%x) \n
%s::%s: failed to set up time object \n
%s::%s: invalid state for log collection %u \n
FetchMemSwapInfo
%s::%s: service matching set up for %s \n
SetPropertyUpdateNotificationHandler
%s::%s: log collection already enqueued \n
CollectPowerStateLog
%s::%s: boot stage: %s, fw state: %s \n
%s::%s: invalid crash log buffer \n
%s::%s: failed to alloc OSNumber for up time \n
%s::%s: failed to set dict object for StateDump \n
CTRL.sram.clientport.bin
WFL5G.txscr.bin
%s::%s: invalid fileName: %s \n
%s::%s: crashlog table invalid magic::%llx \n
%s::%s: Invalid segmentName or segmentDump observed \n
%s::%s: centauri-driverkit=0 \n
%s::%s: invalid length (working copy %llu t0 %llu) \n
CollectChipInfo
WFP2G.imem.bin
%s::%s: invalid viddid 0x%x \n
%s::%s: memswap memory is already DART mapped \n
%s::%s: invalid state (%u) \n
AppleCentauriManager::SaveClientProperty(this, key, nullptr, 0) == kIOReturnSuccess
%s::%s: failed to allocate chip object for CentauriChipControlT2026 \n
%s::%s: adding new client info for ss %u \n
%s::%s: Invalid coreName or crashlogData observed \n
GetSubsystemBufferSize
%s::%s: ValidateReceivedCrashlogTable failed for size allocated::%d current::%d \n
state: %s\n
%s::%s: failed to open doorbell \n
kAudioMessage_ReceiverState
ReleaseSecondaryMemory
Crashlog.WFMAIN.bin
%s::%s: failed to create service (ret = 0x%x) \n
%s::%s: added file %s, size %zu \n
index < fSegmentsPerCore[coreId]
flrLimit: %d\n
%s::%s: MSI data address are invalid \n
%s::%s: WDMA max Continuous error count reached \n
TriggerDiagnosticsForSubsystem
%s::%s: full chip reset in progress \n
CollectLogs_block_invoke
%s::%s: ValidateReceivedCrashlogTable failed \n
%s::%s: WDMA chain count is more than expected::%d \n
SetPowerState_Impl
    crashlogPending: %d\n
InitAirshipDoorbell
%s::%s: failed to create doorbell \n
StartWDMAConfig
%s::%s: FillWDMANode failed \n
%s::%s: failed to alloc OSNumber for SS ID \n
%s::%s: chip crash with fiq timed out \n
ret == kIOReturnSuccess || ret == kIOReturnNotFound
systemStateEventArray->setObject(systemStateEventName)
%s::%s: invalid stopIndex: %u \n
        remoteLogCollectionInProgress: %d\n
(null)
%s::%s: CentauriCrashlog item - index %u, id %u, address 0x%x, length %u \n
com.apple.queue.centauri-pcierrors
!ivars->remoteInterfaceAvailable
IsBackToBack
centauri-fatal-err-panic
%s::%s: in fatal error state (%u) \n
GetASPMState
OSAction_CentauriControlRemoteInterface_ClientReady
%s::%s: buffer size invalid::%x \n
ClearWDMA
%s::%s: invalid state: 0x%x \n
%s::%s: in low power \n
ivars->inFlightWork > 0
GetBootStageMirror
CentauriMemoryAccessLog.txt
val && ivars->resetTimestamps->setObject(eventName, val)
%s::%s: watchdog cb no longer registered \n
%s::%s: Logging prop: owner: %s dir: %s file: %s id: %s \n
v24@?0^{AirshipDriverDK=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})(?=^{AirshipDriverDK_IVars}^{AirshipDriverDK_LocalIVars})}8r^{OSString=^^?Aii^{OSMetaClass}^^?(?=^{OSObje
errorData
%s::%s: pci read invalid data \n
Subsystem
%s::%s: timed out while paused \n
NumClients
%s::%s: deferring due to low power \n
%s::%s: failed to copy properties \n
Paused
derivedStop
%s::%s: using console log level %u \n
TriggerChipCrash
WFRX.regdump.bin
%s::%s: experienced an error earlier, ending coredump \n
ivars->clientArray[i].callbacks.clientReadyAction
%s::%s: failed to create os action token (ret = 0x%x) \n
ChangePowerState(kIOServicePowerCapabilityOn) == kIOReturnSuccess
ivars->clientName
Start_Impl
%s::%s: Invalid args \n
CollectCoredumpForSubsystem
GetSharedEndpointInfo
%s::%s: invalid diagnostic controller \n
%s::%s: failed to alloc metadata dict \n
%s::%s: failed HasPCIPowerManagement (ret = 0x%x) \n
%s::%s: not permitted \n
%s::%s: null watermark pointers: name: %s srcAddress: 0x%llx compIndex: %u chainID: %u startNode: %u \n
%s::%s: Bar4size::%llx greater than 16MB so reducing to 16MB \n
ErrorType
%s::%s: failed to get log id \n
%s::%s: GetCrashlogMaxNumSegments failed \n
%s::%s: driver offline - ignoring airship error notification \n
bootTimestampKey
!ivars->inLowPower
%s::%s: timer action attach failed \n
%06llu.%06llu Reset Complete ret: 0x%03x\n
%s::%s: cached crashlogs not available \n
%s::%s: failed to copy provider properties \n
RunningLPM
WFL5G.rxscr.bin
%s::%s: WDMA timed out: continuous error count %u, ss %u state %s \n
UserClientTerminated
Default
%s::%s: exceeded maximum number of components, numComponents: %u maxComponents: %u \n
%s::%s: Force the WDMA to clear its errors \n
%s::%s: missing memswap config; triggering client launch \n
%s::%s: unable to allocate crashlog dictionary \n
ExternalMethod
SaveDeviceState
%s::%s: Diagnostics MSI not enabled \n
serializedBuffer && serializedLength
RestoreDeviceState
%s::%s: Invalid address, corrupt global address \n
ivars->clientArray[id].client == client
%s::%s: invalid parameters \n
%s::%s: powerFlags: %s \n
SetIPCProperties
WFTX.rtmem.bin
WFSC.regdump.bin
%s::%s:  \n
%s::%s: invalid callback parameters \n
ivars->logCollectionInfo.type == kCentauriLogCollectionFatal
    updateFWReasonString: %d\n
SendMemSwapInfoToSubsystem
cachedError->getLength() == sizeof(CentauriCachedErrorInfo)
    promoteToFullReset: %d\n
%s::%s: trying to recover WDMA \n
%s::%s: errorCode %u, reason %s \n
%s::%s: subsystem %u, component %u, numSegments %u \n
name
/Library/Caches/com.apple.xbs/558FE645-4E39-4399-A06E-8DC20AC536F1/TemporaryDirectory.VSeWMb/Sources/AppleCentauri_driverkit/CentauriSubsystem/CentauriSubsystem.cpp
%s::%s: memswap memory map is already set \n
GetCrashlogs
BTMAIN.apiram.bin
%s::%s: skipping invalid crashlog item - index %u, id %u, address 0x%x, length %u \n
v20@?0^{AirshipDriverDK=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})(?=^{AirshipDriverDK_IVars}^{AirshipDriverDK_LocalIVars})}8I16
WR
%s::%s: invalid state for reset %u \n
DerivedLogState
coredumpStart
SendDiagnosticsCompletion
init
%s::%s: driver offline - ignoring exec stage notification \n
%s::%s: timer expired waiting for remote service in dext crash recovery state \n
FunctionReset
%s::%s: failed to allocate inFlightLock \n
%s::%s: invalid driver state %u for dext crash recovery state %u \n
%s::%s: WDMA busy, retry after sleep \n
v12@?0I8
FiqCompletion
Stop
%s::%s: invalid cmd id: %u \n
action == ivars->msiAction
msi-reservation-size
WFP2G.rtmem.bin
%s::%s: no system event notifications required \n
%s::%s: failed to update the FW crash reason string \n
ssID < kNumSubsystems
%s::%s: buffer size %u exceeds expected max %u \n
ScheduleImmediateWake
Offline
%s::%s: super InitWithOptions failed \n
%s::%s: wdma link node not valid \n
%s::%s: bad chain watermark at chainID: %u, failed before attempting to access an address from cores \n
%s::%s: wdmaBuffer create failed::%x \n
%s::%s: id: %u state: %s \n
GetSubsystemTimeout
%s::%s: bad section info: overlaps \n
CreateSystemStateNotificationItems
%s::%s: Valid file::%s added \n
%s::%s: chunkBase 0x%x, chunkOffset 0x%x, bar4Size 0x%x, chunkLimit %u, chunkLength %d\n \n
ready for reset
[Fatal]
logCollectionInfo:\n
TimeToTriggerCollectLogs
CTRL.memswapptt.bin
WFL2G.rtmem.bin
%s::%s: WDMA buffer size is too small for this Coredump collection size: 0x%x CoreDumpOffset: 0x%x \n
%s::%s: failed to create log stream \n
%s::%s: reset already enqueued \n
memSwapMapT0: %s\n
MonotonicTimestamp
WFP2G.regdump.bin
%s::%s: Performance check - Total time taken for %s collection for subsystem::%d is::%llu nano seconds \n
0
%s::%s: escalate FLR failure \n
%s::%s: completion \n
OSAction_CentauriSubsystem_CollectLogsCallback
ptmInfoDict
%s::%s: unable to allocate crashlog table \n
%s::%s: Stop ret = 0x%x \n
BTMAIN.sram.bin
CrashlogTable%u
%s::%s: airship reported fatal error: %s \n
%s::%s: chip class not initialized \n
%s::%s: failed to schedule immediate wake \n
%s::%s: MSI handler: boot stage = %u \n
BTLPS.dmem.bin
free
%s::%s: WDMA buffer getaddressrange is invalid::%x phyMemSegment.length::%llx verifyRange.length::%llx \n
%s::%s: in reset state \n
prepareChipForResetStart
%s::%s: invalid fileStoreIndex: %u \n
%s::%s: failed to get addr range (ret = 0x%x) \n
dict->setObject(kAppleCentauriManagerNumClientsProperty, numSubsystemsObj)
%s::%s: not permitted for ss id %u \n
%s::%s: pci device not open \n
%s::%s: Wdma runs had errors Continuously for max allowable times, need to reset the chip \n
Suspend
%s::%s: invalid crashlog size: 0x%x \n
%s::%s: StartWDMAConfig failed \n
%s::%s: WDMA dump inter::%x err::%x \n
%s::%s: WDMA bus error::%d \n
CollectLogsAbort
%s::%s: bad arg (type: %llu) \n
centauri-force-diagnostics
%s::%s: crash handler has been deregistered \n
TriggerClientLaunch
%s::%s: failed to set airship driver config \n
%s::%s: deferring reset \n
abort handler
%s::%s: FLR limit (%u) reached \n
%s::%s: failed to create function name copy \n
CreateTimer
chipId: %s\n
ConfigureEndpointForMemSwap
CoredumpDuration
functionResetEnd
%s::%s: memswap info not available yet \n
%s::%s: AppleCentauriManager::ChipReset failed (ret = 0x%x) \n
CreateChipObject
CollectDiagnostics_Impl
ivars->collectLogsCompletionBlock
ReportError
action == ivars->timerAction
%s::%s: reset in progress. ignoring error \n
%s::%s: Timer expired with reset flag set \n
StoreRegCoredumpDataWithTLV
%s::%s: subsystem: %d \n
Start_Impl_block_invoke_3
%s::%s: pmcsr 0x%04x \n
inLowPower: %d\n
prevState == kCentauriDextRecoveryStateIdle
PrepareChipForResetDuration
RD
%06llu.%06llu %s 0x%08x 0x%08x\n
%s::%s: signature mismatch \n
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x \n
WFMAIN.aslr.bin
%s::%s: failed to create IOBMD (ret = 0x%x) \n
ptmInfoDict->setObject(kCentauriPropertyPTMEnabledOnEndpoint, ptmEnabled)
%s::%s: ss: %u accessType: %u state: %s bufferSize: %u \n
%s::%s: unexpected termination notification \n
RequireClient
centauri-flr-timeout-ms
Crashlog.BTMAIN.bin
!ivars->logCollectionInfo.localLogCollectionInProgress && !ivars->logCollectionInfo.remoteLogCollectionInProgress
%s::%s: failed to get default queue (ret = 0x%x) \n
%s::%s: release PM assertion \n
%s::%s: LPM log collection mode unsupported \n
%s::%s: caching crashlog \n
/Library/Caches/com.apple.xbs/558FE645-4E39-4399-A06E-8DC20AC536F1/TemporaryDirectory.VSeWMb/Sources/AppleCentauri_driverkit/CentauriSubsystem/CentauriSubsystemUserClient.cpp
copy
Invalid
Crashlog.WFP5G.bin
FillWDMANode
%s::%s: failed to save control dext timestamps, ret = 0x%x \n
%s::%s: unable to allocate crashlog buffer \n
CheckErrorPolicyForKey
%s::%s: airship service not ready \n
errorInfo
PartiallyBooted
LPW
%s::%s: Requested buffer size::%x \n
%s::%s: unexpected coredump completion \n
crashlogStart
%s::%s: PCI dart error \n
%s::%s: error source %u code %u arg %llu \n
time          offset     r/w data\n
%s::%s: invalid segment count %u \n
readData
centauri-wdma-regdump-disable
%s::%s: Not a valid Crashlog table, magic recieved::%llx \n
errorTypeObject
%s::%s: failed to find msi capability (ret = 0x%x) \n
BT2G.aslr.bin
%s::%s: Using FLR limit: %u \n
DeferReset
%s::%s: deferring (state = 0x%x) \n
BTSEC.regdump.bin
BTLPS.seqdmem.bin
FAIL
%s::%s: bad section info: exceeds sec mem range \n
no
nonfatal
BT5G.aslr.bin
%s::%s: Forcefully abort the currently running WDMA channel \n
hasReenumeratedDict
SendMemSwapInfo
%s::%s: failed to copy prepareCb block \n
centauri-crashlog-coredump-via-mmio
Open_Impl
%s::%s: client no longer valid; dropping completion \n
Idle
%s::%s: failed to set boot complete property (ret = 0x%x) \n
WFP5G.aslr.bin
%s::%s: MSI address not valid \n
success
dict->setObject(\"Success\", success ? kOSBooleanTrue : kOSBooleanFalse)
%s::%s: timer source is invalid \n
FillMSINode
ResetCompletion
InduceFaultCb
%s::%s: WDMA is busy !!! \n
%s::%s: WDMA buffer creation failed::%x \n
%s::%s: replacing existing client info for ss %u \n
DextRelaunchState
CollectLogsFatal_block_invoke
%s::%s: invalid number of MSIs configured: %u \n
ErrorDetected
Reason
%s::%s: failed to copy system state service (ret = 0x%x) \n
%s::%s: failed to allocate fileName \n
%s::%s: unexpected match notification \n
WFTX.aslr.bin
%s::%s: crashlog handler already exists \n
%s::%s: Trying to clear out WDMA errors \n
!ivars->completionCopy
CentauriStateDump.txt
PreBoot
Crashlog.COEX.bin
CancelErrorHandler
%s::%s: ProcessCrashlogTable total::%d \n
SetLPMMode
ret == kIOReturnSuccess || ret == kIOReturnNotOpen
CentauriEventLog.txt
%s::%s: failed to serialize \n
eventName && payload
On
%s::%s: invalid crashlog segment observed index: %d address: 0x%x length: 0x%x \n
IsCoredumpPermitted
%s::%s: Writing bar4offset to bar0 failed, readback got::%x \n
%s::%s: deferred work is canceled \n
SACFunctionAvailable
SetupServiceMatchingNotification
pmcsr != nullptr
%s::%s: failed to create airship client \n
%s::%s: WDMA chain corrupt currChain: %u numChains: %u \n
InitializeDiagnosticsMSI
EnqueueDeferredWork(blockCopy, kCentauriDeferredWorkTypeOther)
%s::%s: failed to create data log pipe \n
fCoredumpInfo.numCores
%s::%s: failed to create osdata object for StateDump \n
%s::%s: initialized MSI-1 \n
%s::%s: FLR timeout override: %u ms \n
StateSnapshots
dict && dict->setObject(\"RequireClient\", kOSBooleanTrue)
time          r/w address    value\n
ClearConfigSpaceMailboxes
Crashed
setFLRBit
%s::%s: My msiAddr::%llx msiData::%x \n
%s::%s: unable to allocate segmentDump \n
%s::%s: logpipe: failed to copy directory name %s \n
%s::%s: ss: %u accessType: %u state: %s \n
ivars->state == kCentauriStateLogCollection
%s::%s: Chain::%llu srcaddr::%llx dstaddr::%llx bytes::%x nodenum::%x \n
%s::%s: bad arg \n
CopyClientMemoryForType_Impl
ServiceNotificationReady_Impl_block_invoke
CopyName(&serviceName) == kIOReturnSuccess
SystemEvents
%s::%s: Invalid WDMA buffer address \n
%s::%s: failed to SaveDeviceState (ret = 0x%x) \n
v32@?0Q8^{IOService=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{IOService_IVars}^{IOService_LocalIVars})}16Q24
%s::%s: Driver offline. Ignoring state change %u \n
WaitForReadyForReset
%s::%s: Partial fill file name exceeds max strlen \n
%s::%s: invalid filename/statedump \n
%s::%s: %s property exists - skipping dext crash \n
    coredumpPending: %d\n
%s::%s: ret: 0x%x flags: 0x%qx cnt: %d addr: 0x%qx len: 0x%qx \n
BTLPS.aslr.bin
not null
%s::%s: error arg not an OSNumber \n
GetFirmwareState
BT
WFMAIN.sram.bin
%s::%s: WDMA dump cfg::%x ext_cfg::%x \n
crashlogFile && coredumpFile
com.apple.ConnectivityDriver.DiagnosticsCollectionResult
CompletionCallback_Impl
%s::%s: FLR count: %u \n
%06llu.%06llu SetBusLeadEnable Start enable: %s\n
item->block
FillWatermarkNode
flrCountObject != nullptr
ivars->cachedCrashlogsArray->setObject(copy)
%s::%s: Crashlog processing \n
%s::%s: Empty crashlog table::%x size: 0x%x \n
%s::%s: FillWatermarkNode failed \n
MemSwapWorkingCopy.bin
%s::%s: failed to allocate osstring \n
%s::%s: failed to allocate memory \n
errorData->isWrite < 2
ClearUnsupportedRequestAER
%s::%s: failed to get ecid hi \n
com.apple.centauri.reset.ccpu
%s::%s: invalid ss id (ss = %u) \n
%s::%s: failed to create timer src (ret = 0x%x) \n
BTMAIN.itcm.bin
%s::%s: WDMA buffer addresses are invalid::%x \n
DiagnosticsInterruptOccurred_Impl
ReportError_Impl
derivedStart
%06llu.%06llu 0x%08llx %s 0x%08x\n
%s::%s: failed to find aer capability (ret = 0x%x) \n
BTMAIN.dtcm.bin
%s::%s: failed to copy block \n
%s::%s: StartTimer failed \n
%s::%s: Invalid diagnosticState: %s \n
DerivedCentauriManagerErrorHandler_block_invoke
%s::%s: collecting coredump for ss %u, core %u, memory segments %u \n
%s::%s: crashlog table info - address 0x%x, length 0x%x \n
%s::%s: failed to get airship probe result \n
busy
SetPowerOverride(true) == kIOReturnSuccess
%s::%s: crash log buffer too small: %zu bytes \n
WFP2G.dmem.bin
BTSEC.seqsram.bin
%s::%s: failed to create sharedInfoDict \n
%s::%s: failed to get logging properties dict \n
CentauriDebug
WFL5G.recipeoverridesram.bin
%s::%s: failed to copy reg addr in segmentdump \n
%s::%s: failed to create sharedEndpointInfo dictionary \n
%s::%s: failed to get log file name \n
%s::%s: lpw -> on \n
%06llu.%06llu CollectDiagnostics Start %s %s\n
SetDextRecoveryState
durationObject != nullptr
COEX.rta.bin
%s::%s: failed to merge dictionaries \n
%s::%s: LPM \n
is not
derivedProbeDevice
%s::%s: SART not enabled, skipping FIQ \n
%s::%s: failed to set require client property (ret = 0x%x) \n
%s::%s: failed to create reset state item (ret=0x%x) \n
WFL2G.recipeoverridesram.bin
key
%s::%s: create timer failed ret::%x \n
RecoverWDMA
ret == kIOReturnSuccess || ret == kIOReturnInvalid
%s::%s: failed to get sharedClientInfo (ret = 0x%x) \n
%s::%s: dispatching propertyUpdateNotification \n
dict && dict->setObject(kCentauriPropertyBootComplete, kOSBooleanTrue)
%06llu.%06llu Reset Start\n
maxNumSegments
WFP5G.regdump.bin
%s::%s: driver offline - ignoring MSI notification \n
%s::%s: id::%d crashlogTableAllocatedSize::%x numComponents::%d \n
%s::%s: failed to create memory map (ret = 0x%x) \n
Off
WFL2G.dmem.bin
OSAction_CentauriSubsystem_InterruptOccurred
%s::%s: invalid parameters (ss = %u) \n
ivars->inFlightWork < UINT32_MAX
%s::%s: crashlog header reports empty: %zu bytes \n
ReadyForReset
WFMAIN.dtcm.bin
WFL5G.rtmem.bin
system-events-required
%s::%s: Wdma runs had errors Continuously for max allowable times, cannot proceed to collect logs \n
WFL5G.aslr.bin
BT2G.dmem.bin
%s::%s: invalid provider \n
%s::%s: local log collection not in progress \n
v20@?0i8^{OSDictionary=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})(?=^{OSContainer_IVars}^{OSContainer_LocalIVars})^^?(?=^{OSCollection_IVars}^{OSCollection_LocalIVars})(?=^{OSDictionary_IVars}^{OSDictionary_LocalIVar
CrashlogCompletion
%s::%s: remote watchdog notification failed (ret = 0x%x) \n
AppleCentauriManager::SaveClientProperty(this, key, newValue, autoClearConditions) == kIOReturnSuccess
%s::%s: invalid input dictionary - bailing out \n
EnqueueDeferredWork
%s::%s: failed to read BAR0 info \n
%s::%s: segment %s cannot be accessed via MMIO \n
%s::%s: collect logs callback not ready for ss %u \n
Yes
%s::%s: driver offline - ignoring airship fatal error notification \n
%s::%s: failed to create memswap os action (ret = 0x%x) \n
ctx
%s::%s: error code not found \n
%s::%s: failed to create IOServiceStateNotificationDispatchSource (ret = 0x%x) \n
coredumpEnd
SetState
%s::%s: crashlog size larger than buffer (%zu > %zu) \n
WFMAIN.socram.bin
OSAction_CentauriControlDiagnosticControllerWDMA_TimerOccurred
t2026
-
%s::%s: invalid memswap DMA command \n
%s::%s: failed to RestoreDeviceState (ret = 0x%x) \n
dataObject->getLength() == sizeof(uint32_t)
%s::%s: prepare dma failed::%x \n
dict->setObject(\"ErrorType\", errorTypeObject)
%s::%s: invalid link control value \n
%s::%s: testID: %u \n
Boot
WFL5G.mascr.bin
TimerOccurred_Impl
%s::%s: service notification (type: %llu) \n
%s::%s: ErrorDetected's value type is not a dictionary \n
%s::%s: timeout::current time::%llx, expected time::%llx - redundant timer happened, so skip \n
%s::%s: failed to allocate coredump dictionary \n
CompleteFiq
    logCollectionInfo:\n
DerivedCentauriManagerErrorHandler
com.apple.queue.centauri-corecapture
%s::%s: invalid number of MSIs requested: %u available: %u \n
AirshipStateDump.bin
CleanUp
%s::%s: FillMSINode failed \n
%s::%s: Watermark saved fileName: %s chainID: %d \n
%s::%s: failed to get MSI data (ret = 0x%x) \n
%s::%s: skipping during dext crash recovery \n
ReadMSIAddr
fSubsystemList[kSubsystemControl]
WFSC.aslr.bin
GetFilesFromHostBuffer
%s::%s: WDMA failed to recover with status::%d \n
%s::%s: failed to get dir name \n
%s::%s: timer expired waiting for memswap info in dext crash recovery state \n
BTSEC.aslr.bin
%s::%s: failed to create os action (ret = 0x%x) \n
%s::%s: invalid bootstage 0x%x \n
centauri-allow-panic
%s::%s: crashlog too small: %zu bytes \n
%s::%s: failed to alloc dict \n
CollectDiagnosticsForSubsystem_block_invoke
%s::%s: unable to allocate coredump buffer \n
%s::%s: failed to save timestamp \n
%s::%s: remote service unavailable. wait for %u ms \n
 r 
%s::%s: error reported by %s error code %u \n
%s::%s: No Controller error status observed::%d \n
%s::%s: getCrashlogTableInfo failed: 0x%x \n
%s::%s: Crashlog table address: 0x%x table size: 0x%x \n
%s::%s: bad arg (sectionInfoOSData) \n
CollectDeferredFaultDataCb
%s::%s: failed to create working copy IOBMD (ret = 0x%x) \n
Recovery
%s::%s: Exceeded collection timeout \n
%s::%s: failed to allocate comp buffer \n
%s::%s: boot stage = %s \n
CollectLogsCompletion
%s::%s: block copy failed \n
CentauriMSILog.txt
count  primaryStart    secondaryStart  end           type\n
%06llu.%06llu 0x%x\n
subsystemNameObject
%s::%s: system events required: 0x%x \n
%s::%s: number of MSIs requested: %u (SingleMSI mode) \n
%s::%s: Close ret = 0x%x \n
OpenRemoteService
dict->setObject(kCentauriSystemStateNotificationResetKey, kOSBooleanTrue)
 w 
CollectLogsStateDumps
LogCollection
%s::%s: clearing cfg mbx at offset 0x%x \n
FLRCount
WFL5G.imem.bin
%s::%s: timedout, current time: 0%llx, expected time: 0%llx - In idle state, ignoring timeout \n
WriteToChain
%s::%s: bad diagnosticState: %s \n
%s::%s: unexpected crashlog completion \n
%s::%s: log collection in progress/enqueued \n
%s::%s: invalid crashlog data \n
WFP5G.imem.bin
%s::%s: setobject failed for segmentName::%s \n
%s::%s: failed to allocate crashlog dictionary \n
SetASPMState
%s::%s: remote memswap call failed (ret = 0x%x) \n
centauri-driverkit
%s::%s: function reset already in progress \n
SendChipCrashFiq
GetSecondaryMemoryDescriptor_block_invoke
%s::%s: AppleCentauriManager::Open failed (ret = 0x%x) \n
%s::%s: invalid segment info (addr: 0x%qx len: 0x%qx) \n
systemEventsRequiredObj->getLength() == sizeof(ivars->systemEventsRequired)
%s::%s: failed to create memswap working copy OSData \n
%s::%s: bad size of sectionInfoOSData (expected: %lu got: %lu) \n
%s::%s: remote chip reset callback for ss %u failed (ret = 0x%x) \n
%s::%s: handler already exists \n
oldValue != nullptr
SendAnalytics
%s::%s: WDMA dump err_addrl::%x err_addrh::%x \n
%s::%s: segment is null \n
%s::%s: failed to get IOPCIDevice \n
HandleChipCrashTimeout
%s::%s: remote collect logs callback for ss %u failed (ret = 0x%x) \n
%s::%s: failed to create reset timestamps dict \n
%s::%s: remote interface error (ret = 0x%x) \n
%s::%s: dmaconfig failed::%x \n
action == ivars->diagnosticsMsiAction
ReadMSIData
OSAction_CentauriSubsystem_ChipResetCallback
%s::%s: create timer set handler failed \n
%s::%s: buffer filled, totalBytesPrinted: %u bufferSize: %u \n
CoredumpCompletion
CancelCrashlogHandler
%s::%s: failed to set ptm status in subsystem properties (ret = 0x%x) \n
%s::%s: failed to create chip object for family %u \n
%s::%s: failed to find ptm capability (ret = 0x%x) \n
ErrorArg
receiverOn != nullptr
%s::%s: CollectCoredump allocated buffer sizeKB::%d \n
GetCrashlogTableInfo
%s::%s: empty crashlog table info \n
%s::%s: failed to create fault reporter \n
%s::%s: invalid state: %u \n
%s::%s: failed to create reason string copy \n
%s::%s: failed to allocate segmentDump \n
dict->setObject(\"DiagnosticType\", diagnosticTypeObject)
%s::%s: invalid parameter (ss = %u) \n
SetErrorHandler
UnexpectedDextTermination-UserspaceReboot
fatalLogCollectionTriggered
OS
PrepareForReset
RemoteServiceProperties
%s::%s: failed to set properties (ret = 0x%x) \n
%s::%s: number of crashlogs: %u \n
%s::%s: failed to create IODMACommand (ret = 0x%x) \n
BT2G.regdump.bin
OSAction_CentauriSubsystem_ServiceNotificationReady
%s::%s: WDMA Failed continuous error count: %u ss: %u state: %s \n
%s::%s: invalid fileStoreIndex: %d \n
%s::%s: initialized MSI-%u \n
ivars->timerAction
WaitForRemote
SetupMemSwapRegion
%s::%s: failed to find PCI capability (ret = 0x%x) \n
ivars->memSwapAction && ivars->completionAction && ivars->chipResetAction && ivars->collectLogsAction && ivars->watchdogAction
WFP5G.rtmem.bin
InitAirshipDoorbell_block_invoke
%s::%s: fault reporter is busy \n
%s::%s: didDextRelaunch = %s (reason %u) \n
execStage <= kCentauriBootStageMax
ivars->cachedErrorsArray
pci-dart-error-data
%s::%s: failed to alloc OSNumber for monotonic time \n
Resume
%s::%s: failure on segment name: %s srcAddress: 0x%llx chainID: %u compIndex: %u startNode: %u \n
%s::%s: failed to create chip reset os action (ret = 0x%x) \n
%06llu.%06llu CollectLogs Start 0x%04x %s\n
fatal
BT5G.dmem.bin
%s::%s: WDMA failed to start, WDMA Continuous error count::%d \n
%s::%s: failed to set %s property (ret = 0x%x) \n
    reenumerationTriggered: %d\n
Owner
AdditionalPipeOwners
%s::%s: failed to open IOPCIDevice (ret = 0x%x) \n
WFRX.aslr.bin
cachedError
%s::%s: system state notifications activated \n
%s::%s: WDMA dump lnkl::%x lnkh::%x \n
%s::%s: Get buffer size failed: 0x%x \n
SubsystemID
%s::%s: failed to acquire resource \n
AppleCentauriManager::SetChipInfo(this, dict) == kIOReturnSuccess
%s::%s: state = %u \n
CrashlogDuration
BT5G.imem.bin
newValue
%s::%s: Invalid compIndex: %u \n
SetupMemSwapRegions
WaitForPCIErrorNotifications
CollectAirshipStateDumps
%s::%s: failed to allocate OSData \n
%s::%s: invalid section info \n
%s::%s: pci device not available \n
DiagnosticName
ivars->loggerQueue->OnQueue()
pci-get-dart-error
CentauriUserClientProperties
%s::%s: failed to alloc metadata \n
CentauriChipInfo.txt
centauri-wdma-force-panic
centauri-ccloglevel
%s::%s: client already registered (%s) \n
%s::%s: airship not up; returning %s \n
BootComplete
%s::%s: WDMA buffer addresses are invalid: 0x%x \n
%s::%s: chip rev: 0x%x \n
%s::%s: ret = 0x%x \n
PrepareNode
PTM
%s::%s: no pending requests \n
%s::%s: %u \n
%s::%s: requesting coredump failed (ret=0x%x) \n
GetDiagnosticState
%s::%s: failed to create ss1 sub memory descriptor (ret = 0x%x) \n
%s::%s: WDMA dump dst_addrl::%x dst_addrh::%x \n
%s::%s: WDMA numChains: %u exceeds maxChains: %u \n
%s::%s: failed to copy reg newline in segmentdump \n
%s::%s: bad args (ss = %u) \n
ClientClose
SetDextRecoveryState_block_invoke
FillChainWatermarkNode
%s::%s: invalid parameter \n
CentauriPowerStateLog.txt
%s::%s: resuming fatal log collection (state = 0x%x) \n
HasReenumerated
ClientReady_Impl
isASPMEnabled
%s::%s: crashlog handler is not registered \n
%s::%s: no \n
%s::%s: invalid number of cores for ss %u \n
Running
WFL5G.dmem.bin
systemEventsRequiredObj
%s::%s: Invalid config exists state: %d segmentDump: %u compIndex: %u fileStoreIndex: %u \n
AllocateSecondaryMemory
CollectLogsFatalOnDefaultQueue
id == kCentauriSubsystem0
%s::%s: sizeof got::%x CrashlogInfo::%lx CrashlogItemInfo::%lx maxComponents::%d minSize::%x maxSize::%x \n
%s::%s: failed to create pci error queue (ret = 0x%x) \n
%s::%s: failed to create file name copy \n
%s::%s: bad section info for ss0: zero offset/len \n
%s::%s: dext crash error property exists \n
%s::%s: failed to gather crashlog for ss %u, {0x%x, 0x%x} \n
dict && dict->setObject(kCentauriPropertyPTMEnabledOnEndpoint, ptmStatus)
    resetFailed: %d\n
data
OSAction_CentauriControlSystemEvents_SystemStateNotificationReady
ivars->sharedEndpointInfo && ivars->sharedEndpointInfo->setObject(kCentauriPropertyPTMEnabledOnEndpoint, ptmEnabled)
%s::%s: error filling buffer, bytesPrinted: %d kLineLength: %u \n
SetChipIdentifiersInRegistry
%s::%s: failed to configure interrupts (ret = 0x%x) \n
RegisterServiceOrStartDextRecovery_block_invoke
%s
%s::%s: error source not found for %s \n
version: %s\n
%s::%s: tearing down monitor \n
%s::%s: allocated buffer size: 0x%x \n
IOPCIPMCSState
%s::%s: failed to create user client (ret = 0x%x) \n
remoteService: %s\n
dextRecoveryState: %s\n
%s::%s: bad arguments \n
ExecuteDeferredWork
dict
%s::%s: failed to store data in fileStore \n
%s::%s: exceeded maximum number of descriptors, nodeIndex: %u maxDescriptors: %u \n
%s::%s: secondary memory is not allocated \n
%s::%s: failed to set os action handler (ret = 0x%x) \n
%s::%s: crashlog table not configured \n
%s::%s: super init failed \n
%s::%s: failed to create osdict \n
%s::%s: SS0 offset: %llu size: %u SS1 offset: %llu size: %u SS2 offset: %llu size: %u \n
NO
NumMSIs
length < sizeof(fullReason)
%06llu.%06llu RestoreDeviceState ret: 0x%03x\n
%s::%s: failed to copy reg data in segmentdump \n
EnablePTM
%s::%s: selector %llu \n
%s::%s: %s; adding to queue \n
length < sizeof(configName)
CacheCrashlogs
GetCachedErrorCount
%s::%s: state %u \n
ivars->diagnosticState == kCentauriDiagnosticStateCrashlog || ivars->diagnosticState == kCentauriDiagnosticStateCoredump
%s::%s: wdmaChIntrStatus::%x \n
%s::%s: Segment: 0x%x Cannot be accessed via WDMA \n
!GetInLowPower()
ivars->logCollectionInfo.metadata
ivars->logCollectionInfo.completion
SUCCESS
%s::%s: power assertion already held \n
%s::%s: SART not enabled (capabilities = 0x%x) \n
%s::%s: failed to read BAR4 info \n
%s::%s: invalid parameters (ss = %u type = %u) \n
%s::%s: failed to create os action for watchdog notification (ret = 0x%x) \n
WFMAIN.itcm.bin
%s::%s: remote log collection failed (ret = 0x%x) \n
%s::%s: memswap cb no longer registered \n
GetSubsystemCoreCount
%s::%s: termination notification for CentauriRemoteInterface \n
offline
prepareForResetEnd
false
%s::%s: WDMA timedout but no errors observed!! \n
AppleCentauriManager::SaveClientProperty(this, key, val, 0) == kIOReturnSuccess
%s::%s: propertyUpdateNotification handler not registered \n
ivars->queue->OnQueue()
    hasReenumerated: %d\n
%s::%s: failed to setobject in coredumpdict \n
%s::%s: failed to allocate lock \n
ivars->numRemoteSubsystems && ivars->numRemoteSubsystems <= kCentauriRemoteSubsystemCount
CollectDeferredFaultDataCb_block_invoke
AirshipDriverDK
%s::%s: number of system events required is unsupported (0x%x), ignoring unsupported bits \n
%s::%s: failed to set enable int source (ret = 0x%x) \n
%s::%s: coredump for ss %u %s permitted \n
%s::%s: failed to EnablePCIPowerManagement (ret = 0x%x) \n
%s::%s: failed to set reason object \n
%s::%s: FLR timed out \n
WFSC.rtmem.bin
%s::%s: link node not valid \n
%s::%s: FillChainLinkNode failed \n
CollectLogsCallback_Impl_block_invoke
%s::%s: remote interface unavailable \n
CreateMetadataDict
%s::%s: Crashlog Reason not found from the Crashlog data \n
Crashlog.BTLPS.bin
%s::%s: MSI received is spurious or may be a response previous log collection timeout \n
%s::%s: failed to allocate segmentname \n
%s::%s: failed to get logger queue \n
WaitForClients
key && dict
fwCrashReported
fSubsystemList[kSubsystemBT]
MSIReceived
        localLogCollectionInProgress: %d\n
IsValidBootStage
%s::%s: FLR limit override boot-arg is set \n
SetPTMProperty
ivars->resetTimestamps
%s::%s: failed to get iopcidevice \n
%s::%s: failed to get ecid lo \n
%s::%s: failed to make a copy of sharedClientInfo \n
centauri-consoleloglevel
ivars->pendingWork[kCentauriSubsystem0][kCentauriDiagnosticsFiq]
%s::%s: requesting deferral (low power: %u, defer for memswap: %s) \n
PartiallyBootedLPM
%s::%s: ivars creation failed \n
%s::%s: Not valid controlPciService or queue \n
%s::%s: WDMA completes successfully after %u continous errors. Resetting error count \n
    secMemMD: %s\n
IsSartEnabled
ivars->pendingWork[i][j]
Coredump
%s::%s: failed to save FLR timestamps \n
%s::%s: system-events-required property value: 0x%x \n
Crashlog.WDMAInfo.txt
buffer->setObject(\"MemSwapWorkingCopy.bin\", ivars->memSwapWorkingCopyData)
%s::%s: BAR4 size::%llx and type::%d \n
ExitLPW
dict->setObject(key, kOSBooleanTrue)
[NonFatal]
%s::%s: failed to create osdata object \n
%s::%s: state: %s \n
%s::%s: secondary mem not allocated \n
        coredumpPending: %d\n
ServiceNotificationReady_Impl_block_invoke_2
%s::%s: reserved MSIs via provider \n
GetNumMSIVectorsFromEndpoint
com.apple.ConnectivityDriver.TimeSinceLastFLR
WFSC.imem.bin
%s::%s: failed to create monitor \n
%s::%s: WDMA no interrupts to clear \n
%s::%s: ss %u watchdog reported \n
resetStart
WFTX.imem.bin
OSAction_CentauriSubsystem_CompletionCallback
%s::%s: failed to copy reset block \n
%s::%s: invalid length \n
CollectCrashlogForSubsystem
%s::%s: airship reported error: 0x%x \n
%s::%s: boot stage = ready for reset \n
centauri-disable-coredump
%s::%s: failed to enable timer (ret = 0x%x) \n
%s::%s: error handler already exists \n
CollectEventLog
WFL2G.mascr.bin
WFL2G.regdump.bin
%s::%s: WDMA subordinate error::%d \n
%s::%s: invalid capabilities \n
%s::%s: failed to create data log stream \n
%s::%s: cmd id %u ret 0x%x \n
%s::%s: device id: 0x%x \n
ReadyForResetDuration
BTLPS.regdump.bin
clientName && doorbellName
handler
SetCrashlogHandler_block_invoke
dextRelaunchObj != nullptr
%s::%s: unexpected crash log completion \n
%s::%s: log collection failed (ret=0x%x) \n
resetInfo:\n
%s::%s: failed to prepare for DMA (ret = 0x%x) \n
RealTimestamp
CTRL.regdump.bin
%s::%s: Corrupted crash log table size::%x \n
WakeupLoggerQueue
TriggerClientLaunch() == kIOReturnSuccess
%s::%s: unable to allocate crashlogData \n
%s::%s: invalid metadata dict \n
%s::%s: Transaction pending poll timed out. Proceeding to FLR \n
BadChain
%s::%s: centauri-disable-coredump=%u \n
%s::%s: failed to get the fault reporter additional owner \n
%s::%s: module name not found \n
DartMapMemSwapWorkingCopy
prepareChipForResetEnd
%s::%s: WDMA dump ctrl::%x status::%x \n
ForceClearWDMAErrors
DirectoryName
bufferSize
%s::%s: chip id: %u \n
TriggerPanic
ExecuteDeferredWorkAsync_block_invoke
%s::%s: msiaddr::%llx \n
Crashlog.BTS.bin
WFMAIN.regdump.bin
HandleAnyPartialCollections
CompleteCrashlogCoredump
%s::%s: error appending bytes to bufferObject \n
%s::%s: failed to create msi interrupt source (ret = 0x%x) \n
%s::%s: working copy content: 0x%x len: %llu \n
%s::%s: section too small \n
WFP5G.dmem.bin
centauri-wdma-debug-level
%s::%s: encountered error when writing to chain \n
%s::%s: failed to get crashlog table info (ret = 0x%x) \n
%s::%s: failed to create airship transport \n
!ivars->logCollectionInfo.metadata && !ivars->logCollectionInfo.completion
%06llu.%06llu CollectDiagnostics Complete %s %s ret: 0x%03x\n
ivars->cachedCrashlogsArray
SetResetTimestamp
%s::%s: invalid control service \n
    isASPMEnabled: %d\n
DiagnosticType
%s::%s: memswap callback not available for ss %u \n
%s::%s: failed to copy immediateCb block \n
%s::%s: dispatching cached errors \n
prevState == kCentauriDextRecoveryStateCollectLogs
PrepareDMACommand
%s::%s: failed to get CentauriControlRemoteInterface \n
%s::%s: failed to create logger queue (ret = 0x%x) \n
yes
%s::%s: failed to trigger fault report (ret = 0x%x) \n
%s::%s: memory allocation crashlog reason string failed \n
%s::%s: failed to activate doorbell \n
%s::%s: crashlog size::%x is invalid \n
%s::%s: skipping %s \n
force panic on fatal error for ss %u (type %u)
CentauriManagerErrorHandler_Impl
%s::%s: error handler has been deregistered \n
PrepareChipForReset
%s::%s: failed to set monotonic time object \n
i < kSystemEventsCount
%s::%s: get timeout failed \n
%s::%s: crash poll iterations = %u \n
MaskUnsupportedRequestAER
%s::%s: WDMA decrementor error::%d \n
FLRDuration
v12@?0i8
SetCrashlogHandler
CollectLogsCompletion_Impl
%s::%s: cachedErrorCount: %u \n
EnablePTMOnEndpoint
eventNameObject
Unknown
Crashlog.BT5G.bin
STATUS:\nCrashlog table: %s\nCrashlog: %s\n
%s::%s: failed to get chip id \n
ivars->chip
%s::%s: failed to set real time object \n
NewUserClient_Impl
%s::%s: failed to set dict object \n
MSI-1
!ivars->deferredWork.reset
WFTX.dmem.bin
%s::%s: failed to create error event action ret = 0x%x \n
%s::%s: client: %s \n
%s::%s: crashlog segment observed index: %d address: 0x%x length: 0x%x \n
%s::%s: secondary memory already allocated \n
Crashlog.CTRL.bin
%s::%s: time::%llu \n
%s::%s: failed to get default queue \n
RegisterServiceOrStartDextRecovery
flrCountDict
time          flags\n
%s::%s: bad section info for ss1: zero offset/len \n
%s::%s: os action wait failed (ret = 0x%x) \n
sacObj != nullptr
%s::%s: invalid memswap map or working copy desc \n
%s::%s: ptm enabled, clock granularity: %u ns \n
%s::%s: Prerequisite for collecting coredump completed \n
%s::%s: WDMA is available and working!! \n
AppleCentauriManagerStateDump.txt
%s::%s: unable to allocate segment name \n
key && val
CancelPropertyUpdateNotificationHandler
AppleCentauriManager::SaveClientProperty(this, key, newValue, kCentauriAutoClearOnChipReset) == kIOReturnSuccess
%s::%s: fw crash reason string is not supported with non-fatal log collection \n
%s::%s: data::%x \n
WFMAIN.rtascripter.bin
%s::%s: chip crash successful \n
CancelDeferredWork
ModuleName
WFMAIN.memswapptt.bin
%s::%s: failure on crashlog table: 0x%llx dstAddress: 0x%llx \n
%s::%s: link down detected after error detect \n
%s::%s: requesting crashlog failed (ret=0x%x) \n
BTSEC.dtcm.bin
%s::%s: Timer period set to %llu milliseconds and next timer expiry expected at ::%llu current time in ns::%llu \n
subsystemInfo
%s::%s: failed to add metadata to crashlog dict (ss %u) \n
Success
%s::%s: failed to get owner object \n
%s::%s: failed to create dict \n
prevState == kCentauriDextRecoveryStateIdle || prevState == kCentauriDextRecoveryStateWaitForRemote
%s::%s: number of MSIs requested: %u \n
%s::%s: WDMA buffer allocation failed::%x \n
%s::%s: failed to copy reg colon1 in segmentdump \n
v24@?0I8I12^v16
%s::%s: ptm requester role not supported \n
WFRX.imem.bin
BTMAIN.aslr.bin
%s::%s: Prerequisite for collecting crashlog table info is completed \n
CollectDiagnosticsForSubsystem
ResetDone
%s::%s: failed to create osdata object for %s \n
ClearWDMAIntr
%s::%s: Clear WDMA from further running \n
%s::%s: failed to create ss2 sub memory descriptor (ret = 0x%x) \n
%s::%s: failed to get chip object \n
%s::%s: first power on \n
AirshipDriverConfigName
NotifyPropertyUpdate
%s::%s: log collection failed (ret = 0x%x) \n
%s::%s: CentauriCrashlog info - magic %llx, version %u, numberOfLogs %u \n
%s::%s: diagnostic type %u already in progress for ss %u \n
Reset_block_invoke
collect-logs
GetNumMSIVectorsRequested
Crashlog.WFL5G.bin
%s::%s: failed to create user class dict \n
ivars->systemStateResetItemDict->setObject(kCentauriSystemStateNotificationResetKey, inReset ? kOSBooleanTrue : kOSBooleanFalse)
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu \n
%s::%s: driver offline \n
ProcessCrashlogTable
%s::%s: failed to get ptm capability (ret = 0x%x) \n
DerivedCollectLogs
%s::%s: MSICapOffset::%llx \n
Crashlog.WFTX.bin
%s::%s: failed to get queue (ret = 0x%x) \n
incomplete-
%s::%s: subsystem: %u \n
%s::%s: failed to allocate metadata dict \n
in low power
numSubsystemsObj != nullptr
ivars->completionCopy
LogWDMAResult
WFL2G.rxscr.bin
%s::%s: size %u \n
%s::%s: replacing existing client \n
address && length && coredump
InterruptOccurred_Impl
systemStateEventArray
%s::%s: failed to set handler (ret = 0x%x) \n
crashlogEnd
%s::%s: ptm not supported \n
completionCopy
%s::%s: failed to create log pipe with provider %s \n
%s::%s: failed to set dict object for %s \n
fSubsystemList[kSubsystemWiFi]
WFSC.dmem.bin
WDMA timed out for ss %u %s
%s::%s: AppleCentauriManager::DoReenumeration failed (ret = 0x%x) \n
dict->setObject(\"DiagnosticName\", diagnosticNameObject)
%s::%s: reading crashlog item - index %u, id %u, address 0x%x, length %u \n
fCoredumpInfo.cores && (coreId < fCoredumpInfo.numCores) && fCoredumpInfo.cores[coreId].segments && fSegmentsPerCore
ivars->dextRecoveryState == kCentauriDextRecoveryStateFetchMemSwap
%s::%s: crashlogTable numberOfLogs: %d \n
%s::%s: subsystem %d, numSegments %d \n
diagnosticTypeObject && diagnosticNameObject && dict
%s::%s: reenumeration already triggered \n
%s::%s: invalid chipInfo 0x%x \n
ServiceNotificationReady_Impl
%s::%s: failed to allocate pending work item \n
%s::%s: Failed to collect partial collected files \n
SendLogCollectionRequest
%s::%s: ready for reset timed out \n
TimeToOSBootStage
PopulateWDMAStatusInfo
FillChainLinkNode
CrashlogTable
%s::%s: manager failed to set chip identifiers (ret = 0x%x) \n
numSubsystems
dict && dict->setObject(kCentauriPropertyUnexpectedDextTermination, (ivars->dextRelaunchReason == kCentauriManagerDextRelaunchReasonCrash) ? kOSBooleanTrue : kOSBooleanFalse)
%s::%s: failed to create os action for collect logs (ret = 0x%x) \n
BT5G.regdump.bin
%s::%s: WDMA recovery failed with status::%d\n \n
%s::%s: failed to set object in dict \n
%s::%s: cpl status: crashlog 0x%x coredump 0x%x \n
YES
test
MemSwapCallback_Impl
CentauriControlSystemEvents
%s::%s: skipping boot stage check \n
%s::%s: testID: %u
%s::%s: failed to copy completion block
%s::%s: state %u
%s::%s: skipping invalid crashlog item - index %u, id %u, address 0x%x, length %u
%s::%s: invalid number of MSIs requested: %u available: %u
%s::%s: Crashlog processing
%s::%s: encountered error when writing to chain
%s::%s: failed to allocate crashlog dictionary
%s::%s: WDMA recovery failed with status::%d\n
%s::%s: block copy failed
%s::%s: collecting coredump for ss %u, core %u, memory segments %u
%s::%s: failed to copy system state service (ret = 0x%x)
%s::%s: failed to alloc OSData
%s::%s: failed to allocate fileStore buffer
%s::%s: failed to get IOPCIDevice
%s::%s: failed to get default queue
%s::%s: deferred work is canceled
%s::%s: logpipe: failed to copy file name %s
%s::%s: power assertion already held
%s::%s: msi recieved but response sent, WDMA Continuous error count::%d
%s::%s: remote collect logs callback for ss %u failed (ret = 0x%x)
%s::%s: AppleCentauriManager::Open failed (ret = 0x%x)
%s::%s: match notification for CentauriRemoteInterface
%s::%s: error handler already exists
%s::%s: failed to set up time object
%s::%s: resuming fatal log collection (state = 0x%x)
%s::%s: Transaction pending poll timed out. Proceeding to FLR
%s::%s: Invalid segmentName or segmentDump observed
%s::%s: No Controller error status observed::%d
%s::%s: Crashlog table address: 0x%x table size: 0x%x
%s::%s: invalid provider
%s::%s: MSI address not valid
%s::%s: error arg not an OSNumber
%s::%s: reset failed (ret = 0x%x)
%s::%s: section too small
%s::%s: failed to create sharedEndpointInfo dictionary
%s::%s: invalid viddid 0x%x
%s::%s: failed to allocate inFlightLock
%s::%s: errorSource: %u, errorCode: %u, arg: 0x%llx
%s::%s: 
%s::%s: ivars creation failed
%s::%s: ProcessCrashlogTable total::%d
%s::%s: For subsystem: %d total wdma nodes created: %d
%s::%s: invalid section info
%s::%s: failed to create ss2 sub memory descriptor (ret = 0x%x)
%s::%s: failed to set os action handler (ret = 0x%x)
%s::%s: failed to set enable int source (ret = 0x%x)
%s::%s: timer source is invalid
%s::%s: failed to get MSI addr (ret = 0x%x)
%s::%s: invalid length (working copy %llu t0 %llu)
%s::%s: failed to find MSI property
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x
%s::%s: WDMA decrementor error::%d
%s::%s: WDMA is available and working!!
%s::%s: enable: %u
%s::%s: centauri-driverkit=0
%s::%s: error reported by %s error code %u
%s::%s: options 0x%x reason %s
%s::%s: cached crashlogs not available
%s::%s: Using FLR limit: %u
%s::%s: WDMA dump lnkl::%x lnkh::%x
%s::%s: unable to allocate crashlog buffer
%s::%s: replacing existing client
%s::%s: invalid memswap map or working copy desc
%s::%s: number of system events required is unsupported (0x%x), ignoring unsupported bits
%s::%s: failed to copy reg newline in segmentdump
%s::%s: wdma is error free !!!
%s::%s: Trying to clear out WDMA errors
%s::%s: failed to make a copy of sharedClientInfo
%s::%s: failed to set boot complete property (ret = 0x%x)
%s::%s: allocated metadata copy
%s::%s: bad arg
%s::%s: ss: %u accessType: %u state: %s bufferSize: %u
%s::%s: failed to get MSI data (ret = 0x%x)
%s::%s: driver offline - ignoring exec stage notification
%s::%s: device control reg val: 0x%x
%s::%s: buffer size invalid::%x
%s::%s: log collection in progress/enqueued
%s::%s: Clear WDMA from further running
%s::%s: failed to set ptm status in subsystem properties (ret = 0x%x)
%s::%s: pmcsr 0x%04x
%s::%s: error source %u code %u arg %llu
%s::%s: invalid memswap DMA command
%s::%s: failed to alloc metadata dict
%s::%s: failed to read BAR0 info
%s::%s: failed to get logging properties dict
%s::%s: buffer size %u exceeds expected max %u
%s::%s: number of MSIs requested: %u (SingleMSI mode)
%s::%s: failed to RestoreDeviceState (ret = 0x%x)
%s::%s: failed to allocate fileName
%s::%s: subsystem: %u
%s::%s: WDMA bus error::%d
%s::%s: failed to get ptm capability (ret = 0x%x)
%s::%s: unable to allocate coredump buffer
%s::%s: failed super Start (ret = 0x%x)
%s::%s: unexpected match notification
%s::%s: not permitted
%s::%s: ready for reset timed out
%s::%s: FLR count: %u
%s::%s: SART not enabled (capabilities = 0x%x)
%s::%s: provider not available
%s::%s: failed to create os action for watchdog notification (ret = 0x%x)
%s::%s: invalid driver state %u for dext crash recovery state %u
%s::%s: Invalid WDMA buffer address
%s::%s: segment %s cannot be accessed via MMIO
%s::%s: datapipe: failed to copy directory name %s
%s::%s: GetBusyState ret = 0x%x
%s::%s: remote interface error (ret = 0x%x)
%s::%s: failed to allocate segmentDump
%s::%s: invalid bootstage 0x%x
%s::%s: failed to allocate lock
%s::%s: memswap callback not available for ss %u
%s::%s: failed to SaveDeviceState (ret = 0x%x)
%s::%s: failed to set dict object for StateDump
%s::%s: failed to find msi capability (ret = 0x%x)
%s::%s: failed to create doorbell
%s::%s: time::%llu
%s::%s: memswap cb no longer registered
%s::%s: invalid viddid
%s::%s: failed to create dict
%s::%s: error handler has been deregistered
%s::%s: logger not available
%s::%s: failed to copy reg addr in segmentdump
%s::%s: StartWDMAConfig failed
%s::%s: secondary memory is not allocated
%s::%s: failed to set SS ID object
%s::%s: unable to allocate crashlogData
%s::%s: failed to set monotonic time object
%s::%s: number of crashlogs: %u
%s::%s: sizeof got::%x CrashlogInfo::%lx CrashlogItemInfo::%lx maxComponents::%d minSize::%x maxSize::%x
%s::%s: failed to create log stream
%s::%s: ValidateCrashlogTableSize failed
%s::%s: driver offline - ignoring airship fatal error notification
%s::%s: initialized MSI-1
%s::%s: Timer period set to %llu milliseconds and next timer expiry expected at ::%llu current time in ns::%llu
%s::%s: WDMA dump ctrl::%x status::%x
%s::%s: crashlog table not configured
%s::%s: errorCode %u, reason %s
%s::%s: invalid number of cores for ss %u
%s::%s: failed to EnablePCIPowerManagement (ret = 0x%x)
%s::%s: Prerequisite for collecting coredump completed
%s::%s: WDMA buffer creation failed::%x
%s::%s: chip crash successful
%s::%s: create timer failed ret::%x
%s::%s: WDMA failed to recover with status::%d
%s::%s: CollectCoredump allocated buffer sizeKB::%d
%s::%s: WDMA is recovered from errors
%s::%s: failed to get crashlog table info (ret = 0x%x)
%s::%s: failed to create os action (ret = 0x%x) for client %u
%s::%s: invalid client
%s::%s: failed to allocate OSData
%s::%s: failed to create sharedInfoDict
%s::%s: ptm not supported
%s::%s: failed to create reset timestamps dict
%s::%s: failed to create user class dict
%s::%s: service matching set up for %s
%s::%s: bad args
%s::%s: failed to alloc OSNumber for SS ID
%s::%s: failed to serialize
%s::%s: susbsyteminfo is invalid
%s::%s: airship reported error: 0x%x
%s::%s: invalid input dictionary - bailing out
%s::%s: chip crash timed out
%s::%s: wakeattime for start timer failed ret::%x
%s::%s: wdmaBuffer create failed::%x
%s::%s: failed to create IOBMD (ret = 0x%x)
%s::%s: client already registered (%s)
%s::%s: subsystem %d, numSegments %d
%s::%s: WDMA busy, retry after sleep
%s::%s: failed to set properties (ret = 0x%x)
%s::%s: coredump/crashlog completion failed (ret=0x%x)
%s::%s: no
%s::%s: logpipe: failed to copy log identifier %s
%s::%s: failed HasPCIPowerManagement (ret = 0x%x)
%s::%s: failed to configure interrupts (ret = 0x%x)
%s::%s: WDMA channel is errored out !!!
%s::%s: client: %s
%s::%s: log collection already enqueued
%s::%s: number of MSIs requested: %u
%s::%s: MSICapOffset::%llx
%s::%s: failed to copy immediateCb block
%s::%s: failed to trigger fault report (ret = 0x%x)
%s::%s: invalid length
%s::%s: failed to find ptm capability (ret = 0x%x)
%s::%s: crashlog segment observed index: %d address: 0x%x length: 0x%x
%s::%s: MSI data address are invalid
%s::%s: Bar4size::%llx greater than 16MB so reducing to 16MB
%s::%s: ss %u not yet registered
%s::%s: failed to save timestamp
%s::%s: failed to open doorbell
%s::%s: failed to create monitor
%s::%s: ignoring based on boot-arg
%s::%s: Crashlog Reason: \"%s\"
%s::%s: WDMA buffer addresses are invalid: 0x%x
%s::%s: failed to add metadata to crashlog dict (ss %u)
%s::%s: crashlog table invalid magic::%llx
%s::%s: using cc log level %u
%s::%s: no ptm key - bailing out
%s::%s: requesting coredump failed (ret=0x%x)
%s::%s: invalid crash log buffer
%s::%s: missing memswap config; triggering client launch
%s::%s: timer expired waiting for remote service in reset failed state
%s::%s: timer expired waiting for memswap info in dext crash recovery state
%s::%s: WDMA no interrupts to clear
%s::%s: wdma link node not valid
%s::%s: failed to create memswap working copy OSData
%s::%s: ss %u
%s::%s: failed to gather coredump for ss %u, core %u, memory segment %s
%s::%s: adding new client info for ss %u
%s::%s: watchdog cb no longer registered
%s::%s: subsystem id: %u
%s::%s: failed to allocate statedump buffer
%s::%s: StartWDMAConfig failed in config
%s::%s: Corrupted crash log table size::%x
%s::%s: failed to create array
%s::%s: Link is down, coredump is not permitted
%s::%s: CentauriCrashlog item - index %u, id %u, address 0x%x, length %u
%s::%s: offline
%s::%s: failed to create memswap os action (ret = 0x%x)
%s::%s: lpw -> on
%s::%s: WDMA dump dst_addrl::%x dst_addrh::%x
%s::%s: size %u
%s::%s: dext crash error property exists
%s::%s: chip id: %u
%s::%s: remote diagnostics completion callback for ss %u failed (ret = 0x%x)
%s::%s: Logging prop: owner: %s dir: %s file: %s id: %s
%s::%s: failed to create pci error queue (ret = 0x%x)
%s::%s: state = %u
%s::%s: %s
%s::%s: Stop ret = 0x%x
%s::%s: invalid notifier
%s::%s: current timestamp is older than last reset timestamp, ignoring
%s::%s: WDMA dump cfg::%x ext_cfg::%x
%s::%s: failed to read BAR4 info
%s::%s: no pending requests
%s::%s: failed to create timer src (ret = 0x%x)
%s::%s: FLR limit override boot-arg is set
%s::%s: unexpected termination notification
%s::%s: failed to  SearchProperty (ret = 0x%x)
%s::%s: bad arguments
%s::%s: failed to get logger queue
%s::%s: failed to get addr range (ret = 0x%x)
%s::%s: failed to enable ptm (ret = 0x%x)
%s::%s: replacing existing client info for ss %u
%s::%s: invalid callback parameters
%s::%s: failed to get owner object
%s::%s: device id: 0x%x
%s::%s: msiaddr::%llx
%s::%s: failed to activate doorbell
%s::%s: tearing down monitor
%s::%s: bad section info for ss2: zero offset/len
%s::%s: failed to save control dext timestamps, ret = 0x%x
%s::%s: deferring due to low power
%s::%s: airship reported fatal error: %s
%s::%s: remote interface unavailable
%s::%s: driver offline (state = %u)
%s::%s: failed to create airship client
%s::%s: failure on crashlog table: 0x%llx dstAddress: 0x%llx
%s::%s: chip rev: 0x%x
%s::%s: unable to allocate crashlog table
%s::%s: failed to get logging properties object
%s::%s: in reset state
%s::%s: diagnostic type %u already in progress for ss %u
%s::%s: boot stage = %s
%s::%s: in low power
%s::%s: memswap info not available yet
%s::%s: no shared endpoint info
%s::%s: failed to alloc OSNumber for up time
%s::%s: ret: 0x%x flags: 0x%qx cnt: %d addr: 0x%qx len: 0x%qx
%s::%s: bad section info for ss0: zero offset/len
%s::%s: failed to gather crashlog for ss %u, {0x%x, 0x%x}
%s::%s: failed to create osdata object for StateDump
%s::%s: failed to find aer capability (ret = 0x%x)
%s::%s: crashlog too small: %zu bytes
%s::%s: link node not valid
%s::%s: failed to get the fault reporter additional owner
%s::%s: failed to create completion os action (ret = 0x%x)
%s::%s: function reset already in progress
%s::%s: reset already enqueued
%s::%s: failed to set object in dict
%s::%s: Force the WDMA to clear its errors
%s::%s: invalid parameter (ss = %u)
%s::%s: failed to get dir name
%s::%s: SART not enabled, skipping FIQ
%s::%s: failed to create os action for collect logs (ret = 0x%x)
%s::%s: propertyUpdateNotification handler not registered
%s::%s: likely interrupted by host sleep on segment name: %s srcAddress: 0x%llx chainID: %u compIndex: %u startNode: %u
%s::%s: airship service not ready
%s::%s: %u
%s::%s: failed to alloc metadata
%s::%s: invalid number of MSIs configured: %u
%s::%s: ptm requester role not supported
%s::%s: remote log collection not in progress
%s::%s: failed to allocate osstring
%s::%s: handler already exists
%s::%s: requesting deferral (low power: %u, defer for memswap: %s)
%s::%s: bad size (got %u max %u)
%s::%s: failed to create IOServiceStateNotificationDispatchSource (ret = 0x%x)
%s::%s: WDMA chain count is more than expected::%d
%s::%s: chunkBase 0x%x, chunkOffset 0x%x, bar4Size 0x%x, chunkLimit %u, chunkLength %d\n
%s::%s: link down detected after error detect
%s::%s: no pending completion (ss = %u)
%s::%s: failed to create reason string copy
%s::%s: failed to acquire resource
%s::%s: Exceeded collection timeout
%s::%s: wdmaChIntrStatus::%x
%s::%s: register coredump disabled
%s::%s: Get buffer size failed: 0x%x
%s::%s: WDMA retry didn't work, state::%x
%s::%s: chip reset callback not ready for ss %u
%s::%s: finalize %d
%s::%s: exceeded maximum number of descriptors, nodeIndex: %u maxDescriptors: %u
%s::%s: failed to merge dictionaries
%s::%s: failed to create data log stream
%s::%s: remote service unavailable. wait for %u ms
%s::%s: reset in progress. ignoring error
%s::%s: invalid state for reset %u
%s::%s: Requested buffer size::%x
%s::%s: failed to copy reg colon1 in segmentdump
%s::%s: null watermark pointers: name: %s srcAddress: 0x%llx compIndex: %u chainID: %u startNode: %u
%s::%s: failed to get coredump info
%s::%s: failed to create dispatch src (ret = 0x%x)
%s::%s: sleeping for %u ms...
%s::%s: reenumeration already triggered
%s::%s: failed to get provider
%s::%s: added file %s, size %zu
%s::%s: CentauriCrashlog info - magic %llx, version %u, numberOfLogs %u
%s::%s: failed to report error (ret = 0x%x)
%s::%s: failed to create osdata object for %s
%s::%s: failed to create IODMACommand (ret = 0x%x)
%s::%s: invalid fileName: %s
%s::%s: bad section info: exceeds sec mem range
%s::%s: invalid state: %u
%s::%s: deferring (state = 0x%x)
%s::%s: airship not up; returning %s
%s::%s: no system event notifications required
%s::%s: WDMA failed to start, WDMA Continuous error count::%d
%s::%s: Invalid crash log table size::%x
%s::%s: Diagnostics MSI not enabled
%s::%s: client no longer valid; dropping completion
%s::%s: failed to get default queue (ret = 0x%x)
%s::%s: log collection failed (ret = 0x%x)
%s::%s: WDMA max Continuous error count reached
%s::%s: failed to allocate segmentname
%s::%s: failed to create msi interrupt source (ret = 0x%x)
%s::%s: initialized MSI-%u
%s::%s: failed to setobject in crashlogdict
%s::%s: failed to allocate coredump dictionary
%s::%s: id: %u state: %s
%s::%s: invalid watchdog status (0x%x)
%s::%s: selector %llu
%s::%s: not permitted for ss id %u
%s::%s: in fatal error state (%u)
%s::%s: FillMSINode failed
%s::%s: Timer expired with reset flag set
%s::%s: failed to copy block
%s::%s: invalid state (%u)
%s::%s: %s property exists - skipping dext crash
%s::%s: failed to get user client service
%s::%s: requesting crashlog failed (ret=0x%x)
%s::%s: Wdma runs had errors Continuously for max allowable times, need to reset the chip
%s::%s: failed to get CentauriControlRemoteInterface
%s::%s: invalid ss id (ss = %u)
%s::%s: completion
%s::%s: LPM log collection mode unsupported
%s::%s: bad section info for ss1: zero offset/len
%s::%s: skipping %s
%s::%s: selector %llu dispatch provided %s
%s::%s: failed to set airship driver config
%s::%s: poll count %u
%s::%s: logpipe: failed to copy directory name %s
%s::%s: failed to set handler (ret = 0x%x)
%s::%s: failure on fiq srcAddress: 0x%llx dstAddress: 0x%llx
%s::%s: unable to allocate segment name
%s::%s: found crashlog data for %s
%s::%s: failed to start super (ret = 0x%x)
%s::%s: ret = 0x%x
%s::%s: WDMA Failed continuous error count: %u ss: %u state: %s
%s::%s: Driver offline. Ignoring state change %u
%s::%s: failed to create chip object for family %u
%s::%s: unexpected crash log completion
%s::%s: setObject failed for fileName: %s
%s::%s: setobject failed for segmentName::%s
%s::%s: Segment: 0x%x Cannot be accessed via WDMA
%s::%s: Watermark saved fileName: %s chainID: %d
%s::%s: invalid parameters
%s::%s: %s; adding to queue
%s::%s: PCI dart error %u: [%s] addressLo: 0x%x addressHi: 0x%x
%s::%s: WDMA buffer size is too small for this Coredump collection size: 0x%x CoreDumpOffset: 0x%x
%s::%s: FillWatermarkNode failed
%s::%s: chip crash with fiq timed out
%s::%s: bad max size
%s::%s: failed to get queue (ret = 0x%x)
%s::%s: create timer set handler failed
%s::%s: failed to store data in fileStore
%s::%s: failed to get provider queue
%s::%s: subsystem %u, component %u, numSegments %u
%s::%s: Close ret = 0x%x
%s::%s: driver offline - ignoring airship error notification
%s::%s: skipping during dext crash recovery
%s::%s: Invalid config exists state: %d segmentDump: %u compIndex: %u fileStoreIndex: %u
%s::%s: WDMA is busy !!!
%s::%s: Performance check - Total time taken for %s collection for subsystem::%d is::%llu nano seconds
%s::%s: BAR0 size::%llx and type::%d
%s::%s: crashlog table info - address 0x%x, length 0x%x
%s::%s: PCI dart error
%s::%s: failed to create memory map (ret = 0x%x)
%s::%s: invalid state for log collection %u
%s::%s: StartTimer failed
%s::%s: invalid segment count %u
%s::%s: reserved MSIs via provider
%s::%s: Crashlog Reason not found from the Crashlog data
%s::%s: failed to alloc dict
%s::%s: invalid diagnostic controller
%s::%s: crashlog size::%x is invalid
%s::%s: failed to copy deferredCb block
%s::%s: match notification for AirshipDriverDK
%s::%s: invalid cmd id: %u
%s::%s: invalid crashlog data
%s::%s: empty crash log buffer
%s::%s: driver offline
%s::%s: WDMA subordinate error::%d
%s::%s: id::%d crashlogTableAllocatedSize::%x numComponents::%d
%s::%s: failed to create logger queue (ret = 0x%x)
%s::%s: failed to get platform (ret = 0x%x)
%s::%s: failed to create chip reset os action (ret = 0x%x)
%s::%s: failed to schedule immediate wake
%s::%s: failed to allocate metadata dict
%s::%s: timed out while paused
%s::%s: Not a valid Crashlog table, magic recieved::%llx
%s::%s: bad args (ss = %u)
%s::%s: Failed to collect partial collected files
%s::%s: boot stage: %s, fw state: %s
%s::%s: invalid link control value
%s::%s: dmaconfig failed::%x
%s::%s: bad arg (sectionInfoOSData)
%s::%s: skipping boot stage check
%s::%s: ptm enabled, clock granularity: %u ns
%s::%s: Create Timer failed
%s::%s: buffer filled, totalBytesPrinted: %u bufferSize: %u
%s::%s: failed to get ecid hi
%s::%s: Writing bar4offset to bar0 failed, readback got::%x
%s::%s: remote watchdog notification failed (ret = 0x%x)
%s::%s: failed to set require client property (ret = 0x%x)
%s::%s: bad diagnosticState: %s
%s::%s: remote log collection failed (ret = 0x%x)
%s::%s: coredump for ss %u %s permitted
%s::%s: failed to get chip id
%s::%s: unable to allocate segmentDump
%s::%s: super InitWithOptions failed
%s::%s: prepare dma failed::%x
%s::%s: WDMA completes successfully after %u continous errors. Resetting error count
%s::%s: empty crashlog table info
%s::%s: log collection completion already exists
%s::%s: failed to get log file name
%s::%s: chip class not initialized
%s::%s: WDMA timed out: continuous error count %u, ss %u state %s
%s::%s: experienced an error earlier, ending coredump
%s::%s: get timeout failed
%s::%s: failed to get sharedClientInfo (ret = 0x%x)
%s::%s: collect logs callback not ready for ss %u
%s::%s: invalid state (%s)
%s::%s: failed to create working copy IOBMD (ret = 0x%x)
%s::%s: failed to create function name copy
%s::%s: FillWDMANode failed
%s::%s: ss: %u
%s::%s: crash handler has been deregistered
%s::%s: failed to get chip object
%s::%s: ValidateReceivedCrashlogTable failed for numComponents::%d
%s::%s: Not valid controlPciService or queue
%s::%s: MSI received is spurious or may be a response previous log collection timeout
%s::%s: Chain::%llu srcaddr::%llx dstaddr::%llx bytes::%x nodenum::%x
%s::%s: Invalid segname or segdump
%s::%s: InitWithOptions failed
%s::%s: invalid parameters (ss = %u)
%s::%s: failed to open IOPCIDevice (ret = 0x%x)
%s::%s: remote chip reset callback for ss %u failed (ret = 0x%x)
%s::%s: failed to create os action (ret = 0x%x)
%s::%s: About to reset
%s::%s: invalid crashlog size: 0x%x
%s::%s: fault reporter is busy
%s::%s: invalid metadata dict
%s::%s: deferring reset
%s::%s: failed to create osdata object
%s::%s: memory allocation crashlog reason string failed
%s::%s: failure on segment name: %s srcAddress: 0x%llx chainID: %u compIndex: %u startNode: %u
%s::%s: driver offline - ignoring MSI notification
%s::%s: get crashlog table failed::%x
%s::%s: failed to validate segment length (ret = 0x%x expected %llu got %llu)
%s::%s: exec stage change to OS
%s::%s: timeout::current time::%llx, expected time::%llx - redundant timer happened, so skip
%s::%s: invalid crashlog segment observed index: %d address: 0x%x length: 0x%x
%s::%s: allocated buffer size: 0x%x
%s::%s: WDMA timedout but no errors observed!!
%s::%s: SS0 offset: %llu size: %u SS1 offset: %llu size: %u SS2 offset: %llu size: %u
%s::%s: powerFlags: %u
%s::%s: clearing cfg mbx at offset 0x%x
%s::%s: WDMA buffer allocation failed::%x
%s::%s: Forcefully abort the currently running WDMA channel
%s::%s: invalid fileStoreIndex: %d
%s::%s: collected coredump for ss %u, core %u, memory segment %s, total size 0x%x
%s::%s: escalate FLR failure
%s::%s: dispatching propertyUpdateNotification
%s::%s: failed to create file name copy
%s::%s: invalid control service
%s::%s: failed to copy reg data in segmentdump
%s::%s: failed to copy service name (ret = 0x%x)
%s::%s: boot stage = ready for reset
%s::%s: failed to create airship transport
%s::%s: failed to set dext relaunch property (ret = 0x%x)
%s::%s: failed to alloc OSString
%s::%s: failed to get log id
%s::%s: deliver notification error (ret = 0x%x)
%s::%s: failed to set reason object
%s::%s: tp poll count %u
%s::%s: crashlog header reports empty: %zu bytes
%s::%s: Invalid FIQ address
%s::%s: bad size of sectionInfoOSData (expected: %lu got: %lu)
%s::%s: failed to create reset state item (ret=0x%x)
%s::%s: failed to set real time object
%s::%s: driver %s - ignoring MSI notification
%s::%s: ss %d
%s::%s: termination notification for AirshipDriverDK
%s::%s: FLR timed out
%s::%s: system-events-required property value: 0x%x
%s::%s: failed to get airship driver
%s::%s: getCrashlogTableInfo failed: 0x%x
%s::%s: failed to create service (ret = 0x%x)
%s::%s: secondary memory already allocated
%s::%s: invalid state: 0x%x
%s::%s: crashlog handler is not registered
%s::%s: failed to allocate pending work item
%s::%s: failed to get logger
%s::%s: new doorbell value: 0x%x
%s::%s: state: %s
%s::%s: failed to set dict object for %s
%s::%s: crash log buffer too small: %zu bytes
%s::%s: Partial fill file name exceeds max strlen
%s::%s: unexpected crashlog completion
%s::%s: reading crashlog item - index %u, id %u, address 0x%x, length %u
%s::%s: bad arg (type: %llu)
%s::%s: module name not found
%s::%s: signature mismatch
%s::%s: Watermark buffer size is not enough
%s::%s: WDMA dump err_addrl::%x err_addrh::%x
%s::%s: AppleCentauriManager::ChipReset failed (ret = 0x%x)
%s::%s: centauri-disable-coredump=%u
%s::%s: resuming reset (state = 0x%x)
%s::%s: ss: %u accessType: %u state: %s
%s::%s: failed to create timer action (ret = 0x%x)
%s::%s: WDMA buffer addresses are invalid::%x
%s::%s: system-events-required property search failed (ret = 0x%x)
%s::%s: invalid stopIndex: %u
%s::%s: ss %u type %u
%s::%s: failed to create error event action ret = 0x%x
%s::%s: FLR limit (%u) reached
%s::%s: system state notifications activated
%s::%s: bad args (ss id %u type %u)
%s::%s: os action wait failed (ret = 0x%x)
%s::%s: failed to get airship probe result
%s::%s: new exec stage: %u
%s::%s: ASPM state: %u
%s::%s: My msiAddr::%llx msiData::%x
%s::%s: exceeded maximum number of components, numComponents: %u maxComponents: %u
%s::%s: super init failed
%s::%s: dispatching cached errors
%s::%s: WDMA chain corrupt currChain: %u numChains: %u
%s::%s: crashlog size larger than buffer (%zu > %zu)
%s::%s: cpl status: crashlog 0x%x coredump 0x%x
%s::%s: pci device not available
%s::%s: invalid chipInfo 0x%x
%s::%s: invalid parameter
%s::%s: GetCrashlogMaxNumSegments failed
%s::%s: ValidateReceivedCrashlogTable failed for size allocated::%d current::%d
%s::%s: failed to save FLR timestamps
%s::%s: MSI handler: boot stage = %u
%s::%s: Valid file::%s added
%s::%s: WDMA dump src_addrl::%x src_addrh::%x
%s::%s: Prerequisite for collecting crashlog table info is completed
%s::%s: Invalid diagnosticState: %s
%s::%s: secondary mem not allocated
%s::%s: error source not found for %s
%s::%s: timedout, current time: 0%llx, expected time: 0%llx - In idle state, ignoring timeout
%s::%s: failed to allocate memory
%s::%s: error handler not registered
%s::%s: failed to copy reset block
%s::%s: bad chain watermark at chainID: %u, failed before attempting to access an address from cores
%s::%s: trying to recover WDMA
%s::%s: local log collection not in progress
%s::%s: failed to allocate chip object for CentauriChipControlT2026
%s::%s: failed to copy properties
%s::%s: failed to create log pipe with provider %s
%s::%s: invalid subsystem core info
%s::%s: memswap memory is already DART mapped
%s::%s: WDMA dump inter::%x err::%x
%s::%s: failed to get iopcidevice
%s::%s: cachedErrorCount: %u
%s::%s: failed to copy provider properties
%s::%s: failed to allocate comp buffer
%s::%s: remote memswap call failed (ret = 0x%x)
%s::%s: failed to create fault reporter
%s::%s: returned from SetProperties (ret = 0x%x)
%s::%s: full chip reset in progress
%s::%s: failed to set dict object
%s::%s: failed to prepare for DMA (ret = 0x%x)
%s::%s: bad section info: overlaps
%s::%s: failed to get ecid lo
%s::%s: using console log level %u
%s::%s: release PM assertion
%s::%s: failed to create user client (ret = 0x%x)
%s::%s: invalid state for watchdog notification: %u
%s::%s: data::%x
%s::%s: failed to send %s (ret=0x%x)
%s::%s: WDMA numChains: %u exceeds maxChains: %u
%s::%s: failed to create ss1 sub memory descriptor (ret = 0x%x)
%s::%s: manager failed to set chip identifiers (ret = 0x%x)
%s::%s: failed to create os action token (ret = 0x%x)
%s::%s: timer expired waiting for remote service in dext crash recovery state
%s::%s: Invalid compIndex: %u
%s::%s: Empty crashlog table::%x size: 0x%x
%s::%s: LPM
%s::%s: failed to copy prepareCb block
%s::%s: failed to create data log pipe
%s::%s: didDextRelaunch = %s (reason %u)
%s::%s: ValidateReceivedCrashlogTable failed
%s::%s: Wdma runs had errors Continuously for max allowable times, cannot proceed to collect logs
%s::%s: failed to copy completionCb block
%s::%s: working copy content: 0x%x len: %llu
%s::%s: fw crash reason string is not supported with non-fatal log collection
%s::%s: ContinueWDMA chain ends
%s::%s: subsystem: %d
%s::%s: segment name is invalid for id %u\n
%s::%s: invalid diagnostic access type
%s::%s: error filling buffer, bytesPrinted: %d kLineLength: %u
%s::%s: Open error (ret = 0x%x)
%s::%s: invalid capabilities
%s::%s: id::%d crashlogTableSize::%x
%s::%s: failed to find PCI capability (ret = 0x%x)
%s::%s: invalid number of MSIs requested: %u
%s::%s: timer action attach failed
%s::%s: In paused state
%s::%s: WDMA buffer getaddressrange is invalid::%x phyMemSegment.length::%llx verifyRange.length::%llx
%s::%s: failed to copy reg colon2 in segmentdump
%s::%s: wdma debug level not matching
%s::%s: BAR4 size::%llx and type::%d
%s::%s: error code not found
%s::%s: memswap memory map is already set
%s::%s: Invalid args
%s::%s: ss %u watchdog reported
%s::%s: unable to allocate crashlog dictionary
%s::%s: failed to get core count for ss %u
%s::%s: caching crashlog
%s::%s: pci device not open
%s::%s: system events required: 0x%x
%s::%s: FillChainLinkNode failed
%s::%s: unexpected coredump completion
%s::%s: Invalid coreName or crashlogData observed
%s::%s: stream: failed to copy log identifier %s
%s::%s: requesting full wake
%s::%s: ErrorDetected's value type is not a dictionary
%s::%s: crash poll iterations = %u
%s::%s: failed to alloc OSNumber for real time
%s::%s: Invalid address, corrupt global address
%s::%s: failed to update the FW crash reason string
%s::%s: failed to alloc OSNumber for monotonic time
%s::%s: failed to copy collectLogs block
%s::%s: failed to create osdict
%s::%s: invalid segment info (addr: 0x%qx len: 0x%qx)
%s::%s: invalid fileStoreIndex: %u
%s::%s: crashlogTable numberOfLogs: %d
%s::%s: error appending bytes to bufferObject
%s::%s: unable to allocate crashlogKey
%s::%s: service notification (type: %llu)
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu
%s::%s: powerFlags: %s
%s::%s: pci read invalid data
%s::%s: segment is null
%s::%s: crashlog handler already exists
%s::%s: failed to enable timer (ret = 0x%x)
%s::%s: termination notification for CentauriRemoteInterface
%s::%s: cmd id %u ret 0x%x
%s::%s: log collection failed (ret=0x%x)
%s::%s: FLR timeout override: %u ms
%s::%s: subsystem: %u status: 0x%x
%s::%s: invalid parameters (ss = %u type = %u)
%s::%s: failed to set %s property (ret = 0x%x)
%s::%s: failed to setobject in coredumpdict
%s::%s: first power on
%s::%s: failed to remove property (ret = 0x%x)
%s::%s: AppleCentauriManager::DoReenumeration failed (ret = 0x%x)
%s::%s: invalid filename/statedump
%s::%s: SetProperties failed
```
