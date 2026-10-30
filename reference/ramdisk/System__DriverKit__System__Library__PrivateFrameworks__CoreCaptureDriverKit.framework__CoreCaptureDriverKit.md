# `/System/DriverKit/System/Library/PrivateFrameworks/CoreCaptureDriverKit.framework/CoreCaptureDriverKit`

From the upgrade restore ramdisk (141-29011-104.dmg). 498,240 bytes.

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
%06llu.%06llu %{public}s.%c[%lu] %{public}s
DeferredAlloc failed
corecapture:%{public}s
(%s::%s) Failed to set %s property Owner:%s Pipe:%s\n
missing argument\n
LogIdentifier
CCLogPipe::setDumpCompleteCb failed to allocate dump complete callback block owner: %s pipe: %s\n
CCLogPipeUserClient::setPipePolicy policy: %d\n
IOClass
%s::%s Invalid (pipe) provider
Begin calling all complete report callbacks\n
CCFaultReporter enable is %d\n
%s::%s(): Too many owners (%u), truncated to %u\n
%s::%s(): No cached fault data available\n
stopPipe
%s::%s Invalid ivars
%s does not have prepare callback\n
CoreCaptureStreamProperties
%s - OSString::withCString failed\n
Failed to create scratch bufferes Owner:%s Pipe:%s\n
%s::%s():Failed to set notify timeout property (%u) Owner:%s Pipe:%s\n
IOMallocType failed\n
%s:%d CCFaultReporterUserClient::Stop ret:0x%x\n
CCLogPipe::%s: Timer already armed for %s/%s\n
fInitCCCapture was freed already %s::%s()
%s::%s(): Invalid parameters\n
too long summary string
setPipeStreamLogLevel
fail to record History [%lld] %s\n
CCFaultReporterUserClient: Provider is not a CCIOService
CCDataPipe::notifyTimeout notification sent user client for owner: %s pipe: %s\n
?
setNotifyTimeout
%s Failed to dump dext pipes %0x08x\n
Bad extraFileName\n
%d
%s::%s():Failed to set total file number property (%u) Owner:%s Pipe:%s\n
UnifiedPolicy
cc.debug.CollectLogAtLowPriority
creating a history string failed for %s
CCLogPipe::setStreamLogLevel - Unknown Stream %s\n
ERROR CCIOService::%s(%d) No reporters in OSet ivars->fReporters
%s::%s():Failed to set Min Log Size To Notify property (%zd) Owner:%s Pipe:%s\n
%s::%s():Failed to set unified log policy property (%d) Owner:%s Pipe:%s\n
%s::%s(): Pipe is not started. Bail.\n
clearConsoleLogFlag
%s::%s(): Invalid log policy - %d\n
NewUserClient() - Failed to create CCFaultReporterUserClient with error: 0x%08x.
%s:%d Failure in IODispatchQueue::Create :%d\n
%s::%s(): Boot-Arg cc.debug.CollectLogAtLowPriority, Value=%d\n
Unexpected memory descriptor typeId\n
CCLogPipe::setStreamConsoleLogLevel: stream:%s level:%u\n
startPipe failed pipeOwner %s, pipeName %s\n
CCLogPipeUserClient already open. Bail. Owner:%s Pipe:%s
IOUserClientQueueExternalMethod
%s PREPARE REPORT FAILED %x\n
Failed to create set Notify action - %x\n
CCLogStream::initWithPipeAndName failed setIORegistry\n
%s::%s():Failed to set CC Flag property (%llu) \n
CCLogStream::profileRemoved failed setIORegistry\n
Failed to re-arm timer in deferred path (ret=0x%x)\n
StreamHeader
CCIOReportLogStream
%s::%s():Failed to set pipe directory name property (%s) Owner:%s Pipe:%s\n
%s\n
Someone changed readPtr %d->%d.\n
setStreamConsoleLogFlags
CoreCaptureLogPipeUserClientProperties
CCPipe::withOwnerNameCapacity failed pipeOwner %s, pipeName %s\n
collect immediate data %d\n
invalid report\n
[DriverKit] CCFaultReporterUserClient entitlement check failed\n
mapPipe
%s Failed to dump kernel pipes %0x08x\n
Disabled. Bail.\n
CCDataPipe::notifyTimeout Failed notify user client for owner: %s pipe: %s \n
CCPipe::withOwnerNameCapacity pipeOwner %s pipeName %s\n
empty Client list!\n
%s::%s: invalid stream log level %d\n
Cannot resize in ring buffers
CCLogPipeUserClient::setPipeStreamLogLevel DEXT stream: %s, level: %d\n
%s::%s(): CCPipeUserClient::Start failed\n
%s::%s(): Boot-Arg cc.debug.logThrottleWindow, Value=%d\n
Triggering faultReport with reason '%s'\n
CCFaultReporterUserClient: IOUC is not entitled
CCLogStream::init\n
IOLockAlloc failed\n
%s::%s():Failed to set pipe log identifier property (%s) Owner:%s Pipe:%s\n
%s~%s
CCCaptureIOServiceProperties
invoke %s complete report callback\n
Failed in super::init\n
ERROR  CCIOService::UpdateReport_Impl Failed updateAllReports on OSDynamicCast'd logPipe\n
LogPipe UC Stop 0x%x \n
%d extraFiles\n
missing pipeOptions\n
initWithPipeAndName
virtual bool CCStream::initWithPipeAndName(CCPipe *, const char *, const struct CCStreamOptions *)
Missing ivars in %s\n
getPolicy
ERROR CCIOService::ConfigureReport_Impl(%d) No reporters in OSet ivars->fReporters
%s DataPipe UC Stop 0x%x \n
queryMetaDataDispatch
CCFaultReporterService
updateFile failed for %s
%s::%s(): Failed to create OSData\n
~%s
OSDynamicCast failed pipeOwner %s, pipeName %s\n
%s::%s:%d Owner: %s Name: %s LogIdentifier: %s
CCFaultReport::initWithFaultInfo called with 0 length functionName\n
triggerCoreCapture: Unexpected typeID %p\n
%s::%s:%d level:%d
setLogFlag
corecaptureIsDebuggbleUnified
(%s:%s) Failed to create CCIOService while creating Owner:%s Name:%s ret:%x\n
NumberOfFiles
memory allocation failed
Failed to add History.txt\n
CCLogStream::initWithPipeAndName requires valid stream options\n
Failed to do start registration\n
cc.debug.logThrottleWindow
CCFaultReporter::stopFaultReporter timer cancelled before SpinDeferredCommonCapture\n
DumpDextCCPipesWithOwner
%s privilege:%d corecaptureIsDevFusedOrCSRInternal:%d seed build %d
Failed to create fPipeOwner\n
(%s::%s) startReg Capture::CCIOService success
%s - Unable to create deferred capture action\n
<unknown>
-------------- Fault Report State ------------- \n%s\n%s:%d:%s\nTimestamp: %llu.%llu\nPC: 0x%llx LR: 0x%llx\nfAction 0x%x\nfEventID 0x%x\n
UpdateReport_Impl
DKReporter::CCIOService::addReporterLegend %p groupName %s subGroupName %s ret %d\n
 Failed to create ivars->fRingStateMap\n
CCPipe::initWithOwnerNameCapacity failed Owner:%s Pipe:%s\n
Dropping log of size %ld larger than max allowable of size %ld\n
%s - Missing parameter\n
Failed to create lock Owner:%s Pipe:%s\n
%s::%s() Failed to create ivars->fSharedRingStateMD\n
Pipe
%s::%s:%d flags:0x%llx
%s::%s():Failed to set CC Flag property (%llx) \n
%s::%s(): FileSize is overriden %s\n
*
setPipeNotifyTimeout
[%lld]%llu.%llu\t %s\t - Logged: %s watchdog result=%s\n
%s::%s(): WARNING: overwriting unconsumed fault data (reason=%s)\n
%s does not have immediate callback\n
CCOSSerializeDataStream
CCLogPipe::setStreamConsoleLogFlags stream:%s flags: 0x%llx\n
setStreamConsoleLogLevel
%s::%s(): LogSize is overriden %s\n
Failed to create Notify timer - %x\n
LogType
CCLogPipeUserClient::setPipeStreamConsoleLogLevel stream: %s, level: %d\n
%llu.%llu\t %s\n
%s does not have deferred capture callback\n
generateOptionPacket - insufficient space in destination buffer (%zd)\n
getLevel
%s - Unable to create timer for deferred data collection\n
%s Dumped (%d/%d) dext pipes Owner:%s Plane:%s\n
SUCCESS CCIOService::%s(%d) offset at %llu for capacity %llu outElementCount %d\n
%s::%s():Failed to set pipe policy property (%d) Owner:%s Pipe:%s\n
%s::%s() Failed to set property dictionary Owner:%s Pipe:%s\n
%s:%s fCCIOService retainCount:%d line:%d\n
%s::%s():Failed to set stream log identifier property (%s) \n
setStreamLogFlags
%s::%s():Failed to set notify timeout property (%u)\n
CCLogPipe
%s - StartReg fail on CCService ret:%d\n
%s - Unable to set the capture action to the deferred data collection timer\n
Fail: Could not save %s as dict, retval 0x%x\n
WiFiDKCoreCapture
%s::%s():Failed to set pipe size property (%zd) Owner:%s Pipe:%s\n
Updating a reason string failed
IOLockAlloc failed Owner:%s Pipe:%s\n
setConsoleFlags
%s::%s() ring buffer allocation is deferred\n
%s::%s():Failed to set pipe name property (%s) Owner:%s Pipe:%s\n
%s does not have complete report callback\n
buildFaultNotification
ERROR CCIOService::ConfigureReport_Impl called with no ivars->fCCObject attached\n
CCDataPipeUserClient::ExternalMethod[%qd] return ioret:%d, msg:%s\n
CCLogPipeUserClient::ExternalMethod[%qd] returns ioret:%x, msg:%s\n
%s::%s(): Sending fault notification to daemon (ownerCount=%u, reason=%s)\n
fail to record addFile %s\n
watchdog@
CCLogStream::%s: invalid stream log level %d\n
%s::%s:%d logFlags:0x%llx
%s::%s():Failed to set pipe Log type property (%d) Owner:%s Pipe:%s\n
%s::%s(): ConsoleLevel is overriden %s\n
CCLogStream::logHeaderAndBuf - Comment too long (%d)\n
CCLogPipe::%s: logging disabled for %s/%s\n
                              Log Calls
                       Capture Requests
Failed to create Notify action - %x\n
CCDataPipe::Stop Owner: %s Name: %s enqueued: %llu dequeued: %llu dropped: %llu
withPipeAndName
Fail: Could not save %s as data, retval 0x%x, dat %p, len %zu\n
 Failed to create fRingBufferMap ret %x\n
(%s) Failed to set IOClass property \n
pipe is not a CCDataPipe\n
CCDataStream
Timer start failed (ret = 0x%x)\n
CCLogPipe::%s: Timer already disarmed for %s/%s\n
IOMallocType failed pipeOwner %s, pipeName %s\n
CCPipe::init\n
unknown
v32@?0{CCTimestamp=QQ}8i24I28
%s fLogAfterWatchDog:%d fEnableCoreCapture:%d needCaptureLog:%d needsWatchdog:%d dumpFaultReportToDisk:%d needsBlockingFaultReporter:%d doCapture=%d
invalid summary and reason string lengths
profileLoaded
CCLogPipeUserClient::setPipeNotifyTimeout notify timeout: %d\n
CCLogPipe::setDumpCompleteCb dump complete callback already set owner: %s pipe: %s\n
LogPolicy
%s::%s  startPipe fail
   Log Messages Dropped Short Of Buffer
dumpToDiskComplete
Unable to access CCPipe provider
(%s) Failed to create CCIOService (ret value=0x%x)\n
CoreCaptureFlag
queryMetaData
GetFaultData
%s::%s(): Min Log Size To Notify(%zd) is greater than Log Size(%zd)\n
%s::%s():Failed to set pipe file option flags property (%u) Owner:%s Pipe:%s\n
(%s) Provider is not a CCPipe\n
CCFaultReporter::updateDumpProgress action type %d numpipes %d
CCFaultReporterUserClient::init: IOMallocType failed\n
IOMallocType failed Owner:%s Pipe:%s\n
CCOSSerializeWithIOReportDataStream
Failed to create ring MD\n
NewUserClient() - Failed to create UserClientProperties with error: 0x%08x.
ccpipe:
%s::%s(): Boot-Arg Key: %s, Value=%s\n
%s::%s(): ConsoleFlags is overriden %s\n
%s::%s(): Log Size must be non-zero Owner:%s Pipe:%s\n
%s::%s(): Failed to get log policy - %d\n
%s::%s(): Failed to start log pipe\n
CCLogPipeUserClient::setPipeStreamConsoleLogFlags stream: %s, flags: 0x%llx\n
CCLogPipeUserClient::setPipeWatermarkLevel watermarkLevel: %d\n
Provider is not a CCIOService
CCFaultReporter::updateDumpProgress dump already completed, ignoring duplicate callback
CCDataPipe::dequeueBlob - no IOUC to RX blob\n
Ignoring timer notification\n
No subGroupName provided
createReportersAndLegend
CCLogPipeUserClient::dumpToDiskComplete Owner:%s Pipe:%s\n
%s::%s(): Invalid log type - %d Owner:%s Pipe:%s\n
%s::%s:invalid stream log level %d\n
setPolicyInt
setPipePolicy
CCIOServiceObjType
Begin calling all immediate callbacks\n
no in progress fault reporter and reason string can't be updated
CCFaultReport::saveFileName called with 0 length fileName
armNotifyTimerIfNeeded
Done calling all complete report callbacks\n
invalid argument
Fail: Could not save %s as data, retval 0x%x, pMem %p, len %zu\n
initWithOwnerNameCapacity
setPolicy
%s COLLECT IMMEDIATE FAILED %x\n
B24@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}16
Failed to prepare the report\n
%llu.%llu
%s %s
profileRemoved
CCFaultReporterUserClientProperties
CCFaultReporter::stopFaultReporter clearDumpCompleteCb logPipe owner='%s' pipe='%s'\n
CoreCapture errorCodeStr for last fault reason code %d : \n
%s%s~%s
setConsoleLevel
FileOptions
setPipeWatermarkLevel
CCFaultReporter::stopFaultReporter completing report from cancel handler\n
Callback %s is not OnQueue!!!\n
CCDataPipe::capture No privilege, not capturing owner: %s pipe %s\n
Failed to arm timer (ret = 0x%x)\n
dumping to disk has started and reason string can not be modified
MISSING OWNER\n
%s Failed RPC to kext CopyCCIOServicesWithOwner Owner:%s Plane:%s 0x%08x\n
%s::%s(): Called with invalid ivars\n
%s::%s(): \n
OSAction_CCFaultReporter_SpinDeferredCapture
free
CCDataPipe::dumpToDiskComplete owner: %s pipe: %s\n
setFlags
cc.logging.oslog
cc.logging.iolog
Failed to create fPipeName\n
setPipeStreamConsoleLogFlags
Stop
Failed to create ring buffer\n
%s:%d pipe is stopped\n
Invalid argument(s) are being passed to CCPipeAndStreamCreate\n
LogDataType
B16@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8
missing pipeOptions Owner:%s Pipe:%s\n
%s::%s() retVal:%d:\n
%s::%s():Failed to set set property dictionary \n
CCPipe::withOwnerNameCapacity Unsupported pipe type(%d) \n
close
bufSize >= totalSize\n
Someone changed state@readPtr %d.\n
updatePipeStreamConsoleLogFlags
[DriverKit] entitlement check failed:%d\n
Owners
CCFaultReporterUserClient::init: super::init() failed\n
CCLogPipe::%s: Failed to arm timer (ret=0x%x)\n
CCLogPipe::getMemoryDescriptor mapPipe(0) failed rv:0x%x map:%p owner:%s pipe:%s
%s::%s() IOReporters setup for %s\n
%s::%s(): No active streams attached to the ccplane\n
%s:%d No stream found or err:%d
%s - IOLockAlloc failed\n
CCLogPipe::capture DeferredAlloc failed owner:%s pipe:%s\n
%s::%s():Failed to set Min Log Size To Notify property (%zd)\n
cc.internal.client
(%s) super::init failed\n
(%s) CopyProperties failed (ret value=0x%x)\n
%s::%s():Failed to set stream name property (%s) \n
DKReporter::CCIOService::addReporterLegend %p groupName %s subGroupName %s from owner: %s pipe %s ret %d\n
CCFaultReporter: Failed to create service name string\n
Filename
%s %p \t\tpriority %d\n
ConsoleLevel
CCDataPipeUserClient::externalMethodGated Unexpected selector %llu value\n
i8@?0
%s:%06u: ERROR: Return code not sucessfull [%08x]\n
%s::%s Invalid fCCIOService
invoke %s prepare callback\n
CCFaultReporter::callCompleteReportCallbacks already completed, skipping\n
SpinDeferredCapture_Impl
CCFaultReporter::updateDumpProgress dump to disk completed\n
%s:%06u: ERROR: Return code not expected [%08x]\n
(%s) startReg failure = 0x%x\n
Created CCDataStream (Name: %s)\n
updateStreamLogFlags
DumpKernelCCPipesWithOwner_Impl
CompressionDisabled
CCRegistryCopyStreamsLocal
%s COMPLETE REPORT FAILED %x\n
CCFaultReporter::updateDumpProgress id mismatch
Not appending. Bail.\n
CCDataPipe::cleanupPendingCallback: Aborting pending capture - owner='%s' pipe='%s' session=%llu.%llu queueSize=%u
setConsoleLogFlag
Begin calling all prepare report callbacks\n
CCDataPipe::withOwnerNameCapacity: Invalid pipe type(%d)\n
CCDataPipe::setDumpCompleteCb dump complete callback already set owner: %s pipe: %s\n
CCLogPipe::withOwnerNameCapacity: Invalid pipe type(%d)\n
CCDataPipe
allocCapture
freeCCCaptureObject
CCFaultReporterUserClient
CCLogPipe::capture Failed to add capture event for owner: %s pipe: %s\n
ERROR CCIOService::ConfigureReport_Impl(%d) ivars->fReporters count %u outCount %d IOReturn %x
OSDynamicCast stream failed pipeOwner %s, pipeName %s\n
reason string is not updated during report fault
%s::%s():Failed to set Console Flag property (%llx) \n
Name
%s - INVALID CCPipe\n
%s::%s(): CCDataPipeUserClient::Start failed\n
startPipe
%s::%s Kext RPC call failed 0x%08x\n
%s::%s():Failed to set total file size property (%u) Owner:%s Pipe:%s\n
CCFaultReporter
CCFaultReporterExternalMethodDispatchQueue
%s - CCIOService::Attach FAILED\n
%s::%s(): Invalid log policy - %d Owner:%s Pipe:%s\n
Fault reporter is busy - Active: %s - New request: %s\n
CCLogStream::initWithPipeAndName requires valid name\n
setLevel
%s::%s(): initWithOwnerNameCapacity failed Owner:%s Pipe:%s\n
CCLogPipe::cleanupPendingCallback: Aborting pending capture - owner='%s' pipe='%s' session=%llu.%llu
CCStream::withPipeAndName failed pipeOwner %s, pipeName %s\n
%s:%d ivars->fCCExternalMethodDispatchQueue NULL!!\n
%s::%s(): Boot-Arg cc.debug.logAfterWD, Value=%d\n
ERROR CCIOService::ConfigureReport_Impl Failed configureAllReports on OSDynamicCast'd logPipe\n
CoreCaptureIOServiceProperties
No
Done calling all prepare report callbacks\n
empty file data
CCPipe
CCDataPipe::setDumpCompleteCb failed to allocate dump complete callback block owner: %s pipe: %s\n
Created CCLogStream (Name: %s)\n
CCLogPipe::getMemoryDescriptor mapPipe(1) failed rv:0x%x map:%p owner:%s pipe:%s
Failed to collected immediate data for report\n
CCLogPipe::capture No privilege, not capturing owner: %s pipe %s\n
CCLogPipe::capture pipe not ready for capture owner: %s pipe %s\n
NotifyThreshold
CCLogPipe::init\n
%s::%s():Failed to set pipe data type property (%d) Owner:%s Pipe:%s\n
cc.debug.logThrottleCount
bool CCFaultReporter::initWithStreamDispatchQueue(IOService *, CCDataStream *, IODispatchQueue *)
CCLogPipe::log -- Attempting to write outside ring buffer\n
CCLogPipe::updateStreamLogFlags stream:%s flags: 0x%s\n
[%s] Failed to set External Method Dispatch Queue ret:0x%x\n
_
clearLogFlag
Unknown stream type\n
%s privilege:%d bootArgsAndDebuggerChecked:%d, corecaptureIsDevFusedOrCSRInternal:%d
FaultReporter is stopped\n
%s:%d AttachToPipeInDKPlane fail ret:%d
OSString alloc fail
IOUC is not entitled
CCFaultReporter: Failed to create properties dictionary\n
CCLogPipe::dumpToDiskComplete owner: %s pipe: %s\n
CCLogPipe::capture Failed notify user client for owner: %s pipe: %s\n
CCIOService Waiting for CoreCapture IORegistry plane\n
0x%08x
CCLogStream::profileLoaded failed setIORegistry\n
%s::%s(): NotifyTimeout is overriden %s\n
%s::%s(): Failed to add CCCapture nub\n
Begin calling all deferred capture callbacks\n
ccstream:
%s::%s(): CCFlags is overriden %s\n
CCPipe::createReportersAndLegend no getReportersSet()
CoreCapture logging throttled for fault %llu:%llu - %s\n
Set Action to %x\n
CopyProperties failed\n
Id
Failed to create ring state Owner:%s Pipe:%s\n
ERROR CCIOService::%s(%d) failed write at %llu for capacity %llu outElementCount %d IOReturn %x\n
Start_Impl
open
disarmNotifyTimer
%s Look for dext pipes with owner: %s\n
cc.internal
CoreCapture
readDataDispatchDesc
empty file name
generateOptionPacket - Insufficient room to add opt_endofopt to this buffer in subsequent call (%zd)\n
%s::%s():Failed to set CC Level property (%d) \n
Invalid CC service to call NewUserClient\n
Failure in IOUserClient::Start
(%s) Failed to set %s property \n
Fail: Could not save %s as string, retval 0x%x\n
CCFaultReporterUserClient: Unable to access CCFaultReporter provider
%s::%s(): super failed to init!\n
%s::%s():Failed to set objType property (%s) \n
MinLogSizeToNotify
DirectoryName
CCFaultReporter::stopFaultReporter fault reporter already stopped\n
CCFaultReporterUserClient: Failure in IOUserClient::Start
%s::%s(): Min Log Size To Notify(%zd) is greater than Log Size(%zd) Owner:%s Pipe:%s\n
ERROR CCIOService::ConfigureReport_Impl OSDynamicCast(CCLogPipe, ivars->fCCObject) failed\n
%s::%s(): MinLogSizeToNotify is overriden %s\n
setCCaptureInRegistryLocked
OSAction_CCDataPipe_NotifyTimeout
IOUserClass
%s:%d IOUserClient::Stop ret:0x%x\n
Done calling all deferred capture callbacks\n
CCDataPipe::capture pipe not ready for capture owner: %s pipe %s\n
%s::%s:%d Name: %s LogIdentifier: %s
Yes
panic@
CCFaultReporterUserClient::free\n
setWatermarkLevelToNotify
CCFaultReporter::updateDumpProgress fault reporter freed
%s::%s(): Pipe size resolved to zero Owner:%s Pipe:%s\n
CCLogPipe::log - Required size (%zu) is greater than max (%zu)\n
Failed to create User client\n
%s::%s() Failed to createReportSet\n
CCLogPipe::%s: Deferred allocation is requested for %s/%s\n
%s::%s():Failed to set pipe type property (%d) Owner:%s Pipe:%s\n
CCCapture
collect deferred data %d\n
Created CCDataPipe (Owner: %s - Name: %s)\n
%s::%s(): Unknown arg[%d] Value is %s\n
%s::%s:%d flag:0x%llx
Created CCLogPipe (Owner: %s - Name: %s)\n
CCLogPipe::updateLogFlags: Unknown flag action\n
ERROR CCIOService::UpdateReport_Impl OSDynamicCast(CCLogPipe, ivars->fCCObject) failed\n
completeReport
%s::%s(): LogPolicy is overriden %s\n
%s::%s():Failed to set pipe owner property (%s) Owner:%s Pipe:%s\n
PipeSize
capturePipesWithOwnerAndCCIOService
updatePipeStreamLogFlags
(%s) Failed CCSetProperties (ret value=0x%x)\n
Failed to process extraFiles\n
ConsoleFlag
%s::%s(): NumberOfFiles is overriden %s\n
[FaultReporter] will watchdog due to: %s \n
init
%s::%s(): Invalid Boot_Arg[%d] %s
CCLogPipe::notifyUserSpace capture notification dropped - no user client for owner: %s pipe: %s\n
CCExternalMethodDispatchQueue
com.apple.corecapture.userclient
addOwner
enableCoreCapture
Failed to add %s\n
ERROR CCIOService::UpdateReport_Impl called with no ivars->fCCObject attached\n
capture
OSAction_CCLogPipe_NotifyTimeout
IOUserUserClient
AddFileList.txt
History.txt
dumping to disk is disabled\n
scratchBuffer\n
%s::%s():Failed to set pipe policy property (%d)\n
Failed to do Publish and Register Service\n
FileSize
CCLogPipeUserClient::setPipeStreamLogFlags stream: %s, flags: 0x%llx\n
%s - Missing CCIOService\n
CCLogPipe::setStreamConsoleLogFlags - Unknown Stream %s\n
CCIOService Failed to create fReporters OSSet\n
CoreCaptureDataPipeUserClientProperties
readDataDispatchStruct
CoreCaptureLevel
No groupName provided
%s::%s(): Boot-Arg cc.debug.logThrottleCount, Value=%d\n
v8@?0
FaultReportState.txt
%s::%s():Failed to set stream ID property (%u) \n
corecaptureIsDebuggble
invoke %s deferred capture\n
%s:%d Unknown Stream %s\n
CCLogPipe::updateStreamConsoleLogFlags stream:%s flags: 0x%s\n
withOwnerNameCapacity
cc.debug.logAfterWD
CCDataPipe::enqueueBlob queue full, dropping blob: %s session: %s Owner: %s Name: %s queueSize: %zu maxSize: %zu
Owner
getting provider's DQ failed
initWithStreamDispatchQueue
Bad extraFileData\n
setStreamLogLevel
updateStreamConsoleLogFlags
(%s:%s) AttachToDKPlane fail Owner:%s Name:%s ret:%x\n
readData
Force panic for %x\n
missing dispatch queue\n
CCLogPipe::setStreamLogFlags Flags: 0x%llx\n
%s::%s() Done Creating Legend for owner: %s pipe %s\n
%s:%06u: ERROR: Return code not successful [%08x]\n
CCLogPipe::setStreamLogLevel stream:%s Level: 0x%x\n
CCLogPipe::setStreamConsoleLogLevel - Unknown Stream %s\n
cc.debug.enable
PipeType
setPipeStreamLogFlags
setPipeStreamConsoleLogLevel
Failed to add FaultReportState.txt\n
inducer@
NamedFlags
removeCapture
%s::%s():Failed to set pipe file name property (%s) Owner:%s Pipe:%s\n
[%lld]%llu.%llu\t %s - Logged: %s\n
%s core capture enable %d\n
CoreCapture errorCodeStr for last fault status code %d : \n
CCLogStream::initWithPipeAndName failed CCStream init\n
%s::%s(): CCLevel is overriden %s\n
%s::%s(): CCCapture object already exists. Bail.\n
CCLogPipe::updateStreamLogFlags - Unknown Stream %s\n
%s::%s(): LogType is overriden %s\n
Stop_Impl
Done calling all immediate callbacks\n
%s::%s():Failed to set Console Level property (%d) \n
MiscInfo
%s::%s(): Invalid log data type - %d Owner:%s Pipe:%s\n
%s::%s(): Terminating CCCapture object\n
CCFaultReporter::stopFaultReporter clearDumpCompleteCb dataPipe owner='%s' pipe='%s'\n
%s::%s Failed SetProperties\n
recording %s\n
\n\nduration: %lld.%llds\n
Unknown
%06llu.%06llu %s.%c[%lu] %s
invoke %s immediate callback\n
CCFaultReporterUserClient::ExternalMethod[%llu] returns ioret:0x%x\n
CCLogPipe::updateStreamConsoleLogFlags - Unknown Stream %s\n
%s::%s():Failed to set pipe compression property (%d) Owner:%s Pipe:%s\n
%s::%s() Failed to createReportersAndLegend\n
removeInitCapture
CCPipe::createReportersAndLegend failed tp create ivars->fCoreCapturePipeReporter %p
%s DEFERRED CAPTURE FAILED %x\n
CCFaultReport::initWithFaultInfo called with 0 length fileName\n
CCLogStream
%s::%s CCStreamLogLevel:%d ccLevel:%d\n
```
