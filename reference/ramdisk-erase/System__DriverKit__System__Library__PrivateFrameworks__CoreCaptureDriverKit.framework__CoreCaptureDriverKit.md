# `/System/DriverKit/System/Library/PrivateFrameworks/CoreCaptureDriverKit.framework/CoreCaptureDriverKit`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 498,240 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 19 (Size: 2048)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (3)

- `/System/DriverKit/System/Library/PrivateFrameworks/CoreCaptureDriverKit.framework/CoreCaptureDriverKit (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/usr/lib/libc++.dylib (compatibility version 1.0.0, current version 2200.32.0)`

## Entitlements

```xml
  - no entitlements
```

## Strings (574)

```
initWithStreamDispatchQueue
CCDataPipe::dumpToDiskComplete owner: %s pipe: %s\n
armNotifyTimerIfNeeded
CCLogPipe::setDumpCompleteCb failed to allocate dump complete callback block owner: %s pipe: %s\n
CCLogPipe::updateStreamLogFlags stream:%s flags: 0x%s\n
Failed in super::init\n
CCDataPipeUserClient::ExternalMethod[%qd] return ioret:%d, msg:%s\n
%s - IOLockAlloc failed\n
%s::%s(): Invalid log policy - %d Owner:%s Pipe:%s\n
%s::%s() Failed to create ivars->fSharedRingStateMD\n
setNotifyTimeout
%s::%s():Failed to set pipe policy property (%d) Owner:%s Pipe:%s\n
cc.logging.oslog
CCDataPipe::setDumpCompleteCb dump complete callback already set owner: %s pipe: %s\n
withPipeAndName
bufSize >= totalSize\n
CCLogPipe::init\n
%s DataPipe UC Stop 0x%x \n
FaultReporter is stopped\n
CCFaultReporterUserClient::free\n
CCDataStream
%s::%s():Failed to set notify timeout property (%u)\n
%s::%s(): LogType is overriden %s\n
%s::%s():Failed to set pipe Log type property (%d) Owner:%s Pipe:%s\n
Start_Impl
i8@?0
CCLogPipe
invalid argument
CCLogStream::init\n
CCLogPipe::%s: Timer already disarmed for %s/%s\n
ERROR CCIOService::UpdateReport_Impl called with no ivars->fCCObject attached\n
%s::%s():Failed to set Console Flag property (%llx) \n
setWatermarkLevelToNotify
Failed to do start registration\n
%s core capture enable %d\n
Failed to arm timer (ret = 0x%x)\n
CoreCapture errorCodeStr for last fault reason code %d : \n
%s::%s(): CCLevel is overriden %s\n
virtual bool CCStream::initWithPipeAndName(CCPipe *, const char *, const struct CCStreamOptions *)
%s::%s():Failed to set total file size property (%u) Owner:%s Pipe:%s\n
%s - Unable to create timer for deferred data collection\n
panic@
CCIOReportLogStream
%s::%s():Failed to set set property dictionary \n
CCPipe::withOwnerNameCapacity pipeOwner %s pipeName %s\n
%s::%s(): ConsoleFlags is overriden %s\n
Failed to create ring state Owner:%s Pipe:%s\n
ERROR  CCIOService::UpdateReport_Impl Failed updateAllReports on OSDynamicCast'd logPipe\n
CCCapture
%s - Unable to set the capture action to the deferred data collection timer\n
CCFaultReporter: Failed to create service name string\n
missing pipeOptions Owner:%s Pipe:%s\n
SUCCESS CCIOService::%s(%d) offset at %llu for capacity %llu outElementCount %d\n
Done calling all complete report callbacks\n
Set Action to %x\n
CCLogPipe::notifyUserSpace capture notification dropped - no user client for owner: %s pipe: %s\n
IOMallocType failed pipeOwner %s, pipeName %s\n
%s Failed to dump dext pipes %0x08x\n
%s:%06u: ERROR: Return code not sucessfull [%08x]\n
CCFaultReporterService
Owners
fail to record addFile %s\n
CCLogPipe::setStreamLogFlags Flags: 0x%llx\n
CCLogPipe::updateLogFlags: Unknown flag action\n
CCLogPipe::setStreamConsoleLogFlags stream:%s flags: 0x%llx\n
History.txt
%s::%s(): Invalid parameters\n
unknown
CCFaultReporterUserClient: Provider is not a CCIOService
CCLogStream::initWithPipeAndName failed CCStream init\n
CCLogPipe::setStreamLogLevel - Unknown Stream %s\n
%s::%s(): Min Log Size To Notify(%zd) is greater than Log Size(%zd)\n
open
IOMallocType failed\n
CCFaultReporterExternalMethodDispatchQueue
%s::%s() retVal:%d:\n
%s::%s(): Min Log Size To Notify(%zd) is greater than Log Size(%zd) Owner:%s Pipe:%s\n
%s::%s():Failed to set pipe policy property (%d)\n
%s - INVALID CCPipe\n
CCFaultReporter::updateDumpProgress action type %d numpipes %d
CCDataPipe::dequeueBlob - no IOUC to RX blob\n
CCDataPipe::notifyTimeout notification sent user client for owner: %s pipe: %s\n
%s::%s():Failed to set CC Flag property (%llu) \n
Owner
AddFileList.txt
invalid summary and reason string lengths
Failed to create Notify action - %x\n
NewUserClient() - Failed to create UserClientProperties with error: 0x%08x.
%s::%s(): FileSize is overriden %s\n
CCDataPipe
setConsoleLevel
Created CCLogPipe (Owner: %s - Name: %s)\n
ERROR CCIOService::ConfigureReport_Impl OSDynamicCast(CCLogPipe, ivars->fCCObject) failed\n
Pipe
missing argument\n
[FaultReporter] will watchdog due to: %s \n
CCDataPipe::setDumpCompleteCb failed to allocate dump complete callback block owner: %s pipe: %s\n
CoreCaptureDataPipeUserClientProperties
setLevel
missing dispatch queue\n
(%s:%s) Failed to create CCIOService while creating Owner:%s Name:%s ret:%x\n
PipeType
*
%06llu.%06llu %s.%c[%lu] %s
%s::%s(): Called with invalid ivars\n
CoreCaptureIOServiceProperties
CCFaultReporter::updateDumpProgress dump already completed, ignoring duplicate callback
%s::%s():Failed to set Console Level property (%d) \n
CCLogStream::profileLoaded failed setIORegistry\n
%s::%s():Failed to set pipe name property (%s) Owner:%s Pipe:%s\n
WiFiDKCoreCapture
initWithOwnerNameCapacity
Failed to re-arm timer in deferred path (ret=0x%x)\n
empty Client list!\n
Begin calling all complete report callbacks\n
Failed to add %s\n
Failed to create set Notify action - %x\n
updatePipeStreamConsoleLogFlags
CCLogPipeUserClient::setPipeStreamConsoleLogLevel stream: %s, level: %d\n
v8@?0
GetFaultData
CCPipe::initWithOwnerNameCapacity failed Owner:%s Pipe:%s\n
setPolicyInt
stopPipe
Begin calling all prepare report callbacks\n
CCFaultReporter::updateDumpProgress id mismatch
Unknown stream type\n
%s::%s(): LogPolicy is overriden %s\n
%s %s
CCFaultReporterUserClient: Failure in IOUserClient::Start
%s::%s() ring buffer allocation is deferred\n
%llu.%llu\t %s\n
Fail: Could not save %s as data, retval 0x%x, dat %p, len %zu\n
%s::%s:%d logFlags:0x%llx
%s COMPLETE REPORT FAILED %x\n
%s::%s(): Failed to create OSData\n
setLogFlag
setStreamLogFlags
CCLogPipe::updateStreamLogFlags - Unknown Stream %s\n
%s::%s():Failed to set unified log policy property (%d) Owner:%s Pipe:%s\n
setCCaptureInRegistryLocked
OSAction_CCDataPipe_NotifyTimeout
CCFaultReporter::callCompleteReportCallbacks already completed, skipping\n
UnifiedPolicy
cc.logging.iolog
StreamHeader
LogPipe UC Stop 0x%x \n
%s does not have deferred capture callback\n
Created CCDataStream (Name: %s)\n
CCLogPipe::setStreamConsoleLogFlags - Unknown Stream %s\n
%s::%s(): Terminating CCCapture object\n
OSAction_CCFaultReporter_SpinDeferredCapture
setPipeNotifyTimeout
no in progress fault reporter and reason string can't be updated
cc.debug.logThrottleCount
CCFaultReporter: Failed to create properties dictionary\n
%s::%s(): WARNING: overwriting unconsumed fault data (reason=%s)\n
Failed to add FaultReportState.txt\n
empty file name
empty file data
ERROR CCIOService::UpdateReport_Impl OSDynamicCast(CCLogPipe, ivars->fCCObject) failed\n
cc.internal
Stop_Impl
%s::%s(): Boot-Arg cc.debug.logAfterWD, Value=%d\n
%s::%s():Failed to set CC Level property (%d) \n
disarmNotifyTimer
Unexpected memory descriptor typeId\n
~%s
ConsoleFlag
LogPolicy
initWithPipeAndName
mapPipe
invoke %s complete report callback\n
CCFaultReporter::updateDumpProgress fault reporter freed
buildFaultNotification
%s::%s(): Boot-Arg Key: %s, Value=%s\n
%s::%s(): CCFlags is overriden %s\n
%s::%s():Failed to set total file number property (%u) Owner:%s Pipe:%s\n
CCLogPipeUserClient::setPipeStreamLogLevel DEXT stream: %s, level: %d\n
%s:%d IOUserClient::Stop ret:0x%x\n
FaultReportState.txt
updateFile failed for %s
_
NumberOfFiles
CCLogPipeUserClient::setPipePolicy policy: %d\n
dumping to disk is disabled\n
setConsoleFlags
%s::%s():Failed to set stream name property (%s) \n
%s::%s(): CCPipeUserClient::Start failed\n
%s::%s:%d flag:0x%llx
getLevel
%s::%s(): LogSize is overriden %s\n
Failure in IOUserClient::Start
setPipeStreamLogLevel
Bad extraFileData\n
Stop
allocCapture
%s:%d No stream found or err:%d
%s:%d Failure in IODispatchQueue::Create :%d\n
CCLogPipe::%s: logging disabled for %s/%s\n
CCLogPipe::updateStreamConsoleLogFlags - Unknown Stream %s\n
readData
setPipeStreamConsoleLogFlags
(%s) startReg failure = 0x%x\n
LogType
%s::%s() Failed to createReportersAndLegend\n
CCLogPipeUserClient::ExternalMethod[%qd] returns ioret:%x, msg:%s\n
Failed to add History.txt\n
Fail: Could not save %s as data, retval 0x%x, pMem %p, len %zu\n
Created CCLogStream (Name: %s)\n
%s::%s() Failed to createReportSet\n
OSAction_CCLogPipe_NotifyTimeout
Done calling all immediate callbacks\n
CCFaultReport::initWithFaultInfo called with 0 length fileName\n
FileOptions
Failed to create fPipeName\n
(%s::%s) startReg Capture::CCIOService success
CCLogStream::initWithPipeAndName failed setIORegistry\n
Someone changed state@readPtr %d.\n
NewUserClient() - Failed to create CCFaultReporterUserClient with error: 0x%08x.
collect immediate data %d\n
Callback %s is not OnQueue!!!\n
CoreCaptureFlag
%s - OSString::withCString failed\n
CCLogPipe::getMemoryDescriptor mapPipe(1) failed rv:0x%x map:%p owner:%s pipe:%s
UpdateReport_Impl
cc.debug.enable
%s fLogAfterWatchDog:%d fEnableCoreCapture:%d needCaptureLog:%d needsWatchdog:%d dumpFaultReportToDisk:%d needsBlockingFaultReporter:%d doCapture=%d
MISSING OWNER\n
CCLogPipe::%s: Failed to arm timer (ret=0x%x)\n
No subGroupName provided
CoreCapture
%s::%s(): Pipe is not started. Bail.\n
%s::%s(): Failed to get log policy - %d\n
%s::%s(): CCDataPipeUserClient::Start failed\n
Fail: Could not save %s as string, retval 0x%x\n
ConsoleLevel
pipe is not a CCDataPipe\n
watchdog@
withOwnerNameCapacity
CCPipe::createReportersAndLegend no getReportersSet()
CCDataPipeUserClient::externalMethodGated Unexpected selector %llu value\n
[%s] Failed to set External Method Dispatch Queue ret:0x%x\n
%s - Missing CCIOService\n
CCFaultReporter::stopFaultReporter completing report from cancel handler\n
Failed to prepare the report\n
CCDataPipe::notifyTimeout Failed notify user client for owner: %s pipe: %s \n
IOUC is not entitled
%s:%d ivars->fCCExternalMethodDispatchQueue NULL!!\n
(%s) super::init failed\n
(%s) Provider is not a CCPipe\n
Bad extraFileName\n
Someone changed readPtr %d->%d.\n
%s privilege:%d corecaptureIsDevFusedOrCSRInternal:%d seed build %d
%s Failed to dump kernel pipes %0x08x\n
%s::%s:%d Name: %s LogIdentifier: %s
%s - CCIOService::Attach FAILED\n
%s::%s():Failed to set Min Log Size To Notify property (%zd) Owner:%s Pipe:%s\n
DirectoryName
CCPipe::init\n
%s does not have complete report callback\n
SpinDeferredCapture_Impl
Triggering faultReport with reason '%s'\n
too long summary string
clearLogFlag
CCLogStream::profileRemoved failed setIORegistry\n
updateStreamConsoleLogFlags
CCLogPipe::setDumpCompleteCb dump complete callback already set owner: %s pipe: %s\n
CCDataPipe::enqueueBlob queue full, dropping blob: %s session: %s Owner: %s Name: %s queueSize: %zu maxSize: %zu
Failed to create ring MD\n
updateStreamLogFlags
CCLogPipe::setStreamConsoleLogLevel: stream:%s level:%u\n
%s::%s() Failed to set property dictionary Owner:%s Pipe:%s\n
%s::%s() Done Creating Legend for owner: %s pipe %s\n
CCDataPipe::capture pipe not ready for capture owner: %s pipe %s\n
%s::%s CCStreamLogLevel:%d ccLevel:%d\n
CCFaultReport::initWithFaultInfo called with 0 length functionName\n
inducer@
Created CCDataPipe (Owner: %s - Name: %s)\n
NotifyThreshold
profileLoaded
%s::%s Invalid ivars
Failed to create scratch bufferes Owner:%s Pipe:%s\n
CCLogPipe::%s: Deferred allocation is requested for %s/%s\n
%s::%s(): Boot-Arg cc.debug.logThrottleCount, Value=%d\n
B16@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8
invoke %s immediate callback\n
invoke %s deferred capture\n
%s::%s():Failed to set stream log identifier property (%s) \n
DKReporter::CCIOService::addReporterLegend %p groupName %s subGroupName %s from owner: %s pipe %s ret %d\n
%s - Unable to create deferred capture action\n
ERROR CCIOService::ConfigureReport_Impl(%d) ivars->fReporters count %u outCount %d IOReturn %x
Failed to process extraFiles\n
%s::%s(): Invalid log data type - %d Owner:%s Pipe:%s\n
%s privilege:%d bootArgsAndDebuggerChecked:%d, corecaptureIsDevFusedOrCSRInternal:%d
   Log Messages Dropped Short Of Buffer
CCIOServiceObjType
No
CCFaultReporterUserClient: IOUC is not entitled
Invalid argument(s) are being passed to CCPipeAndStreamCreate\n
IOUserClass
CCFaultReporter enable is %d\n
Failed to do Publish and Register Service\n
CCRegistryCopyStreamsLocal
cc.debug.logThrottleWindow
CCDataPipe::withOwnerNameCapacity: Invalid pipe type(%d)\n
CCIOService Waiting for CoreCapture IORegistry plane\n
Filename
CompressionDisabled
CCLogPipeUserClient::setPipeWatermarkLevel watermarkLevel: %d\n
%s::%s(): super failed to init!\n
clearConsoleLogFlag
CCOSSerializeDataStream
ERROR CCIOService::%s(%d) failed write at %llu for capacity %llu outElementCount %d IOReturn %x\n
capturePipesWithOwnerAndCCIOService
(%s) Failed to set %s property \n
addOwner
%s %p \t\tpriority %d\n
Fail: Could not save %s as dict, retval 0x%x\n
init
 Failed to create fRingBufferMap ret %x\n
ERROR CCIOService::ConfigureReport_Impl Failed configureAllReports on OSDynamicCast'd logPipe\n
cc.debug.CollectLogAtLowPriority
CCFaultReporter::updateDumpProgress dump to disk completed\n
                       Capture Requests
CCExternalMethodDispatchQueue
IOLockAlloc failed Owner:%s Pipe:%s\n
Failed to create Notify timer - %x\n
CCOSSerializeWithIOReportDataStream
%s Look for dext pipes with owner: %s\n
OSString alloc fail
Id
Cannot resize in ring buffers
setStreamConsoleLogFlags
recording %s\n
%s Dumped (%d/%d) dext pipes Owner:%s Plane:%s\n
Yes
invoke %s prepare callback\n
\n\nduration: %lld.%llds\n
CoreCaptureLevel
%s::%s():Failed to set objType property (%s) \n
%s::%s:%d Owner: %s Name: %s LogIdentifier: %s
queryMetaDataDispatch
dumpToDiskComplete
CCLogStream
CCLogPipe::log -- Attempting to write outside ring buffer\n
CoreCaptureLogPipeUserClientProperties
removeCapture
updatePipeStreamLogFlags
fail to record History [%lld] %s\n
CCStream::withPipeAndName failed pipeOwner %s, pipeName %s\n
%s - Missing parameter\n
%s::%s(): CCCapture object already exists. Bail.\n
createReportersAndLegend
%s PREPARE REPORT FAILED %x\n
-------------- Fault Report State ------------- \n%s\n%s:%d:%s\nTimestamp: %llu.%llu\nPC: 0x%llx LR: 0x%llx\nfAction 0x%x\nfEventID 0x%x\n
CCLogStream::logHeaderAndBuf - Comment too long (%d)\n
IOUserUserClient
IOUserClientQueueExternalMethod
generateOptionPacket - Insufficient room to add opt_endofopt to this buffer in subsequent call (%zd)\n
CCLogPipe::capture DeferredAlloc failed owner:%s pipe:%s\n
CCFaultReporter::stopFaultReporter timer cancelled before SpinDeferredCommonCapture\n
%s Failed RPC to kext CopyCCIOServicesWithOwner Owner:%s Plane:%s 0x%08x\n
CCCaptureIOServiceProperties
CCDataPipe::capture No privilege, not capturing owner: %s pipe %s\n
startPipe failed pipeOwner %s, pipeName %s\n
Begin calling all deferred capture callbacks\n
NamedFlags
%s:%d Unknown Stream %s\n
ERROR CCIOService::ConfigureReport_Impl(%d) No reporters in OSet ivars->fReporters
cc.internal.client
getting provider's DQ failed
creating a history string failed for %s
CCPipe::createReportersAndLegend failed tp create ivars->fCoreCapturePipeReporter %p
generateOptionPacket - insufficient space in destination buffer (%zd)\n
CCIOService Failed to create fReporters OSSet\n
%s::%s():Failed to set pipe file option flags property (%u) Owner:%s Pipe:%s\n
%s::%s(): Failed to add CCCapture nub\n
com.apple.corecapture.userclient
Fault reporter is busy - Active: %s - New request: %s\n
ccstream:
%s::%s():Failed to set CC Flag property (%llx) \n
%s:%06u: ERROR: Return code not successful [%08x]\n
%s::%s(): Boot-Arg cc.debug.logThrottleWindow, Value=%d\n
%s does not have prepare callback\n
Failed to collected immediate data for report\n
%s::%s():Failed to set stream ID property (%u) \n
CCLogStream::initWithPipeAndName requires valid name\n
CCLogPipe::getMemoryDescriptor mapPipe(0) failed rv:0x%x map:%p owner:%s pipe:%s
%s::%s() IOReporters setup for %s\n
Provider is not a CCIOService
%s COLLECT IMMEDIATE FAILED %x\n
Timer start failed (ret = 0x%x)\n
LogIdentifier
CCLogPipe::%s: Timer already armed for %s/%s\n
CCLogPipe::capture pipe not ready for capture owner: %s pipe %s\n
missing pipeOptions\n
setStreamLogLevel
CCPipe::withOwnerNameCapacity failed pipeOwner %s, pipeName %s\n
OSDynamicCast stream failed pipeOwner %s, pipeName %s\n
%s::%s():Failed to set notify timeout property (%u) Owner:%s Pipe:%s\n
                              Log Calls
profileRemoved
setPipeWatermarkLevel
free
%s:%s fCCIOService retainCount:%d line:%d\n
cc.debug.logAfterWD
completeReport
CCFaultReporterUserClient::init: IOMallocType failed\n
%s:%06u: ERROR: Return code not expected [%08x]\n
%s::%s():Failed to set pipe data type property (%d) Owner:%s Pipe:%s\n
%s::%s():Failed to set pipe directory name property (%s) Owner:%s Pipe:%s\n
CCLogStream::%s: invalid stream log level %d\n
readDataDispatchStruct
(%s) CopyProperties failed (ret value=0x%x)\n
%s::%s Invalid fCCIOService
[%lld]%llu.%llu\t %s\t - Logged: %s watchdog result=%s\n
%s::%s(): No cached fault data available\n
%s::%s(): ConsoleLevel is overriden %s\n
CCLogPipe::dumpToDiskComplete owner: %s pipe: %s\n
startPipe
%s::%s Failed SetProperties\n
DKReporter::CCIOService::addReporterLegend %p groupName %s subGroupName %s ret %d\n
CCFaultReporter::stopFaultReporter clearDumpCompleteCb dataPipe owner='%s' pipe='%s'\n
readDataDispatchDesc
Begin calling all immediate callbacks\n
%s%s~%s
%s::%s():Failed to set pipe type property (%d) Owner:%s Pipe:%s\n
Force panic for %x\n
%s::%s: invalid stream log level %d\n
Failed to create fPipeOwner\n
%s DEFERRED CAPTURE FAILED %x\n
CCFaultReporterUserClient::init: super::init() failed\n
CCFaultReporterUserClient: Unable to access CCFaultReporter provider
CopyProperties failed\n
Name
Invalid CC service to call NewUserClient\n
PipeSize
invalid report\n
%s~%s
triggerCoreCapture: Unexpected typeID %p\n
CCLogPipe::capture Failed notify user client for owner: %s pipe: %s\n
CCLogPipeUserClient::setPipeNotifyTimeout notify timeout: %d\n
CCLogPipeUserClient::dumpToDiskComplete Owner:%s Pipe:%s\n
(%s) Failed to set IOClass property \n
%s:%d CCFaultReporterUserClient::Stop ret:0x%x\n
setStreamConsoleLogLevel
DumpKernelCCPipesWithOwner_Impl
setPipeStreamLogFlags
CCLogPipeUserClient::setPipeStreamConsoleLogFlags stream: %s, flags: 0x%llx\n
(%s) Failed to create CCIOService (ret value=0x%x)\n
%s does not have immediate callback\n
IOMallocType failed Owner:%s Pipe:%s\n
CCLogPipe::withOwnerNameCapacity: Invalid pipe type(%d)\n
No groupName provided
freeCCCaptureObject
reason string is not updated during report fault
Dropping log of size %ld larger than max allowable of size %ld\n
Failed to create lock Owner:%s Pipe:%s\n
CCLogPipe::log - Required size (%zu) is greater than max (%zu)\n
%s:%d pipe is stopped\n
CCPipe::withOwnerNameCapacity Unsupported pipe type(%d) \n
Disabled. Bail.\n
dumping to disk has started and reason string can not be modified
CCPipe
(%s:%s) AttachToDKPlane fail Owner:%s Name:%s ret:%x\n
CCDataPipe::cleanupPendingCallback: Aborting pending capture - owner='%s' pipe='%s' session=%llu.%llu queueSize=%u
%s::%s(): Log Size must be non-zero Owner:%s Pipe:%s\n
Missing ivars in %s\n
%s::%s():Failed to set Min Log Size To Notify property (%zd)\n
LogDataType
collect deferred data %d\n
Done calling all deferred capture callbacks\n
%s::%s(): NotifyTimeout is overriden %s\n
%s::%s(): Failed to start log pipe\n
<unknown>
CCLogPipe::capture Failed to add capture event for owner: %s pipe: %s\n
%s::%s Kext RPC call failed 0x%08x\n
%s::%s():Failed to set pipe owner property (%s) Owner:%s Pipe:%s\n
(%s) Failed CCSetProperties (ret value=0x%x)\n
CCLogStream::initWithPipeAndName requires valid stream options\n
setFlags
%d
%s::%s:invalid stream log level %d\n
Updating a reason string failed
IOLockAlloc failed\n
ERROR CCIOService::%s(%d) No reporters in OSet ivars->fReporters
%s::%s Invalid (pipe) provider
CCFaultReporter::stopFaultReporter fault reporter already stopped\n
CCLogPipe::setStreamLogLevel stream:%s Level: 0x%x\n
OSDynamicCast failed pipeOwner %s, pipeName %s\n
corecaptureIsDebuggbleUnified
%s::%s  startPipe fail
CCFaultReporterUserClient
CCFaultReporter::stopFaultReporter clearDumpCompleteCb logPipe owner='%s' pipe='%s'\n
0x%08x
%s::%s(): Invalid Boot_Arg[%d] %s
 Failed to create ivars->fRingStateMap\n
%s::%s():Failed to set pipe size property (%zd) Owner:%s Pipe:%s\n
fInitCCCapture was freed already %s::%s()
Failed to create User client\n
Done calling all prepare report callbacks\n
CoreCaptureStreamProperties
CCLogPipe::capture No privilege, not capturing owner: %s pipe %s\n
ERROR CCIOService::ConfigureReport_Impl called with no ivars->fCCObject attached\n
(%s::%s) Failed to set %s property Owner:%s Pipe:%s\n
%s::%s():Failed to set pipe compression property (%d) Owner:%s Pipe:%s\n
Unable to access CCPipe provider
setPipePolicy
IOClass
Not appending. Bail.\n
setConsoleLogFlag
%s::%s(): Pipe size resolved to zero Owner:%s Pipe:%s\n
ccpipe:
removeInitCapture
B24@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}16
MiscInfo
getPolicy
%s::%s(): \n
queryMetaData
%s - StartReg fail on CCService ret:%d\n
CCDataPipe::Stop Owner: %s Name: %s enqueued: %llu dequeued: %llu dropped: %llu
%s::%s(): Invalid log policy - %d\n
[%lld]%llu.%llu\t %s - Logged: %s\n
corecaptureIsDebuggble
capture
CCLogPipe::updateStreamConsoleLogFlags stream:%s flags: 0x%s\n
DumpDextCCPipesWithOwner
%s::%s():Failed to set pipe file name property (%s) Owner:%s Pipe:%s\n
%s::%s(): No active streams attached to the ccplane\n
%s::%s(): Unknown arg[%d] Value is %s\n
%s::%s:%d level:%d
%s::%s(): Invalid log type - %d Owner:%s Pipe:%s\n
Failed to create ring buffer\n
CCLogPipeUserClient already open. Bail. Owner:%s Pipe:%s
v32@?0{CCTimestamp=QQ}8i24I28
%llu.%llu
CCFaultReport::saveFileName called with 0 length fileName
[DriverKit] CCFaultReporterUserClient entitlement check failed\n
%s::%s(): initWithOwnerNameCapacity failed Owner:%s Pipe:%s\n
setPolicy
%d extraFiles\n
%s::%s(): Too many owners (%u), truncated to %u\n
CCFaultReporterUserClient::ExternalMethod[%llu] returns ioret:0x%x\n
CCLogPipe::setStreamConsoleLogLevel - Unknown Stream %s\n
%s::%s(): MinLogSizeToNotify is overriden %s\n
FileSize
close
CCFaultReporter
CoreCapture errorCodeStr for last fault status code %d : \n
Unknown
scratchBuffer\n
%s:%d AttachToPipeInDKPlane fail ret:%d
MinLogSizeToNotify
CCLogPipeUserClient::setPipeStreamLogFlags stream: %s, flags: 0x%llx\n
[DriverKit] entitlement check failed:%d\n
CCFaultReporterUserClientProperties
%s::%s(): Sending fault notification to daemon (ownerCount=%u, reason=%s)\n
%s\n
%s::%s():Failed to set pipe log identifier property (%s) Owner:%s Pipe:%s\n
%s::%s(): Boot-Arg cc.debug.CollectLogAtLowPriority, Value=%d\n
bool CCFaultReporter::initWithStreamDispatchQueue(IOService *, CCDataStream *, IODispatchQueue *)
memory allocation failed
CoreCapture logging throttled for fault %llu:%llu - %s\n
%s::%s:%d flags:0x%llx
CCLogPipe::cleanupPendingCallback: Aborting pending capture - owner='%s' pipe='%s' session=%llu.%llu
Ignoring timer notification\n
%s::%s(): NumberOfFiles is overriden %s\n
setPipeStreamConsoleLogLevel
enableCoreCapture
?
%06llu.%06llu %{public}s.%c[%lu] %{public}s
DeferredAlloc failed
corecapture:%{public}s
```
