# `/System/DriverKit/System/Library/PrivateFrameworks/CentauriDebug.framework/CentauriDebug`

From the upgrade restore ramdisk (141-29011-104.dmg). 232,240 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 2120)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (5)

- `/System/DriverKit/System/Library/PrivateFrameworks/CentauriDebug.framework/CentauriDebug (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/System/Library/PrivateFrameworks/AirshipDK.framework/AirshipDK (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/System/Library/PrivateFrameworks/CoreCaptureDriverKit.framework/CoreCaptureDriverKit (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit (compatibility version 1.0.0, current version 1.0.0)`
- `/System/DriverKit/usr/lib/libc++.dylib (compatibility version 1.0.0, current version 2200.32.0)`

## Entitlements

```xml
  - no entitlements
```

## Strings (534)

```
%s::%s: TR open successful %s \n
CRStateChangeCallback
%s::%s: memory allocation ring info failed \n
Filename
CRBufSize
%s::%s: unable to allocate tr sync monitor \n
%s::%s: opening completion ring failed \n
%s::%s: invalid ring name \n
%s::%s: finished opening a ring %s \n
%s::%s: super::Start failed with error: 0x%08x. \n
%s::%s: invalid ring handle \n
%s::%s: memory allocation to nubs failed \n
%s::%s: copy properties of provider failed \n
%s::%s: getting pipe size failed \n
NotifyTimeout_Impl
%s::%s: ring name %s \n
CreatePipesAndStreams
%s::%s: memory allocation to footer failed \n
%s::%s: TR %s state is open \n
ConfigureTRSyncMonitor
%s::%s: none enqueued \n
%s::%s: invalid provider \n
%s::%s: setting a name failed for %s nub, error: 0x%08x. \n
%s::%s: creating TR failed %s \n
TRStateChangeCallback
%s::%s: rings are already opened \n
TransportResources
%s::%s: invalid transport resources \n
ret == kIOReturnSuccess
EnqueueRx
%s::%s: tag %u, len %u completion size %u \n
CreateAllNubs
%s::%s: destroying a ring failed \n
%s::%s: nub name %s successful \n
%s::%s: memory allocation to work item failed \n
%s::%s: ring entries %u, bufsize %u \n
%s::%s: enqueue failed \n
EnqueueRxByExtBuf
ModuleName
%s::%s: super init() failed \n
DebugDriverLogs
%s::%s: getting pipe config failed \n
%s::%s: getting log id failed \n
%s::%s: getting tr name failed \n
%s::%s: invalid enabled ring \n
%s::%s: creating a pipe failed for ring %s \n
%s::%s: memory allocation to TR name failed \n
%s::%s: failed to alloc OSString for module name \n
%s::%s: unable to get provider's provider \n
%s::%s: ring entries %u, Ringbufsize %u \n
CreateBufferPool
%s::%s: invalid enabled rings \n
%s::%s: invalid logAction callback \n
%s::%s: failed with error: 0x%08x. \n
%s::%s: invalid numRings pointer \n
%s::%s: getting pipe name failed for ring %s \n
InPlaceCompletion
%s::%s: getting InPlaceCompletion object failed \n
ReportError
%s::%s: owner %s, pipe %s entry \n
%s::%s: cannot set error code key \n
%s::%s: firmware logging is disabled centauri-debug=0 \n
%s::%s: getting file size failed \n
%s::%s: getting log type failed \n
%s::%s: max count reached %u \n
%s::%s: empty airship resources \n
CRName
%s::%s: TR open failed %s \n
%s::%s: setting up TR state monitor failed \n
Start_Impl
ConstructOpenParams
%s::%s: invalid log pipe \n
%s::%s: invalid dispatch queue \n
%s::%s: sync monitor setup completed for CR %s \n
%s::%s: completion size is zero for tag %u \n
%s::%s: invalid log stream \n
bufferTypeFooter
StreamConfig
%s::%s: getting num files failed \n
%s::%s: invalid argument \n
%s::%s: enqueueRx operation failed \n
%s::%s: CR open failed %s \n
PopulatePipeOptions
%s::%s: cannot set module key \n
%s::%s: sync monitor setup completed for TR %s \n
%s::%s: unable to allocate cr sync monitor \n
B24@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}16
LogFileName
LogTypeCircular
%s::%s: invalid airship resource name \n
%s::%s: getting TRBufSize failed \n
%s::%s: failed to set default dispatch queue (ret = 0x%x) \n
CreateRing
DestroyRing
%s::%s: first tag %u, processed count %u, completion count %u \n
%s::%s: no nubs in CentauriDebug \n
loggerstream
%s::%s: failed to report error (ret = 0x%x) \n
%s::%s: TR activate failed %s retVal = 0x%08x \n
%s::%s: memory allocation to buf item failed \n
Name
%s::%s: getting stream config failed for ring %s \n
%s::%s: invalid ring parameters \n
%s::%s: trname %s, trsize %u \n
%s::%s: cancelling the timer failed 0x%08x. \n
ErrorDetected
%s::%s: finished successfully \n
CentauriDebugEnabledRings
EnqueueRxByFooterMem
ReOpenRings
DebugNubs
%s::%s: ring open failed %s state %d, flags 0x%x \n
OpenCR
%s::%s: memory allocation to array failed \n
%s::%s: create stream failed for ring %s \n
%s::%s: open failed with error: 0x%08x. \n
TRBufSize
%s::%s: TR %s state is available \n
%s::%s: invalid handle \n
%s::%s: invalid nub \n
%s::%s: crname %s, crsize %u, crbufsize %u \n
%s::%s: creating CR state monitor failed %s \n
%s::%s: super::Start() failed \n
CreateNub
CopyIPCRingProps
Owner
%s::%s: creating pipes and streams failed \n
%s::%s: owner %s, pipe %s exit \n
%s::%s: cannot set props dictionary \n
%s::%s: invalid trsize %s \n
%s::%s: register service failed \n
%s::%s: invalid logaction callback \n
%s::%s: TR %s state is un-open \n
%s::%s: completion size zero for tag %u \n
%s::%s: failed to get default dispatch queue (ret = 0x%x) \n
%s::%s: setting up TR sync monitor failed \n
%s::%s: invalid context \n
%s::%s: register service on failed \n
%s::%s: CR activate failed %s, retVal = 0x%08x \n
%s::%s: exit \n
isEnabled
%s::%s: creating pipe options failed for ring %s \n
%s::%s: invalid ipc ring dictionary \n
%s::%s: invalid TR handle \n
%s::%s: creating CR failed %s \n
v24@?0*8Q16
CreateNub_block_invoke
RearmNotifyTimer
%s::%s: instantiating CentauriDebug transport failed \n
%s::%s: setting an object failed \n
%s::%s: %s enqueue request.. free space available:%u \n
%s::%s: first tag %u, completion count %u \n
%s::%s: registering nubs failed with error: 0x%08x. \n
Close
%s::%s: invalid ring params list \n
%s::%s: getting CRBufSize failed \n
%s::%s: completion count %s is 0 \n
%s::%s: enabled ring name %s \n
%s::%s: no rings are Enabled \n
%s::%s: isBufferTypeFooter %d, inplacecompletion %d \n
%s::%s: failed to alloc OSNumber for error code \n
ProcessRxCompletionsByExtBuf
%s::%s: opening rings failed \n
%s::%s: getting CRName failed \n
%s::%s: invalid nub properties \n
%s::%s: getting log policy failed \n
%s::%s: invalid ioctx \n
%s::%s: invalid nub name \n
TRName
%s::%s: invalid transport handle \n
%s::%s: invalid completionBlock \n
%s::%s: memory allocation to CentauriDebugAirshipIOContext failed \n
%s::%s: memory allocation to CR name failed \n
ProcessRxCompletionsByFooterMem
LogDataTypePcap
%s::%s: creating a buffer pool failed \n
%s::%s: invalid pipe properties \n
CreatePipe
%s::%s: timer start failed 0x%08x. \n
%s::%s: getting TRName failed \n
%s::%s: opening more than enabled rings numRings =  %u, enabledRings = %u \n
%s::%s: getting enabled rings failed \n
%s::%s: stream name %s entry \n
%s::%s: %s unable to enqueue the buffer to Airship ret = 0x%08x \n
%s::%s: invalid ring paramenters \n
%s::%s: setting props failed for %s nub, error: 0x%08x. \n
%s::%s: copy properties of Plugin failed \n
%s::%s: transport client creation failed \n
%s::%s: failed to open a ring %s \n
%s::%s: iterateObjects failed \n
%s::%s: nub name %s \n
%s::%s: invalid nub props \n
%s::%s: block copy failed \n
%s::%s: memory allocation to ringinfo list failed \n
%s::%s: getting ring buffer type failed \n
%s::%s: %s successully processed %u \n
%s::%s: instatiating pipe object failed \n
CreateStream
init
%s::%s: invalid debug nub props dictionary \n
%s::%s: invalid transport driver \n
%s::%s: getting TRSize failed \n
airship_acipc_tr_get_in_place(ioctx->trInfo.tr) == ioctx->inPlaceCompletion
%s::%s: CR %s state is available \n
Stop_Impl
AirshipResources
DirectoryName
FreeResources
%s::%s: memory allocation transport client name failed \n
%s::%s: completion %s starting completion processing with count:%u tag:%u \n
TRSize
false
ErrorCode
%s::%s: airship buffer creation failed \n
%s::%s: finished ret = 0x%08x. \n
%s::%s: callback finished \n
%s::%s: opening transfer ring failed \n
%s::%s: close failed with error : 0x%08x. \n
OpenOnQueue
%s::%s: creating a ring failed \n
%s::%s: registering a nub failed 0x%08x. \n
NubProperties
LogIdentifier
FileSize
%s::%s: failed to close a %s ring \n
%s::%s: failed to create an ioservice for %s, error: 0x%08x. \n
%s::%s: creating stream options failed for ring %s \n
NumberOfFiles
%s::%s: CR %s state is open \n
%s::%s: %s enqueued %u.. free space available was:%u \n
v8@?0
%s::%s: getting stream name failed for ring %s \n
%s::%s: acquire airship resource failed %s, resource status = 0x%08x \n
%s::%s: opening completion Ring failed \n
%s::%s: number of rings zero \n
%s::%s: copying properties failed 0x%08x. \n
%s::%s: finished %x \n
InitWithProviderAndOptions
CreatePipeAndStream
%s::%s: getting log datatype failed \n
%s::%s: instatiating stream object failed \n
Default
Open
CopyIPCRingProps_block_invoke
%s::%s: constructing open params failed \n
%s::%s: invalid logger argument \n
CRSize
%s::%s: CR open successful %s \n
%s::%s: transfer completion failed completion io result = 0x%08x \n
%s::%s: getting dictionary for %s failed \n
%s::%s: ring Info found \n
index < numRings
PopulateStreamOptions
OpenTR
ProcessRxCompletions
completion.size <= ioctx->footerSize
%s::%s: copying dispatch queue failed with error: 0x%08x. \n
PipeConfig
%s::%s: Deferring opening rings based on logging policy \n
%s::%s: starting a pipe failed for ring %s \n
%s::%s: getting CRSize failed \n
airshipResult == AIRSHIP_OK
%s::%s: iterateObjects on nub prop failed \n
FreeOpenParams
%s::%s: super::init() failed \n
centauri-debug-loglevel
LoggingProperties
%s::%s: getting dir name failed \n
%s::%s: getting tr size failed \n
%s::%s: free space not available \n
%s::%s: %s unable to enqueue to Airship \n
%s::%s: calling open for ring %s \n
CloseOnQueue
%s::%s: invalid airship resources \n
%s::%s: invalid resources argument \n
%s::%s: setting up CR monitor failed \n
%s::%s: Ring state Not Open is handled as part of TR Not Open \n
%s::%s: rings already closed \n
%s::%s: creating a pipe and stream failed \n
%s::%s: getting pipe owner failed for ring %s \n
CompressionDisabled
CentauriDebug
%s::%s: memory allocation to properties dictionary failed \n
completion.size <= item->extbuf_length
%s::%s: memory allocation to dictionary failed \n
%s::%s: getting file name failed \n
%s::%s: super::Stop failed with error: 0x%08x. \n
free
%s::%s: finished \n
centauri-debug
PipeSize
InitWithOptions
%s::%s: trname %s, trsize %u, trbufsize %u \n
%s::%s: invalid ring props \n
%s::%s: memory allocation to open params failed \n
logLevelChanged
%s::%s: invalid CR handle \n
ConfigureCRSyncMonitor
%s::%s: transfer completion failed completion io result 0x%08x \n
buf != nullptr
%s::%s:  \n
CreateAllNubs_block_invoke
%s::%s: invalid key \n
%s::%s: invalid plugin rings \n
LogPolicyCapture
%s::%s: creating TR state monitor failed %s \n
%s::%s: finished %x
%s::%s: failed to copy properties
%s::%s: memory allocation to open params failed
%s::%s: getting tr size failed
%s::%s: memory allocation to work item failed
%s::%s: memory allocation transport client name failed
%s::%s: super::Start failed with error: 0x%08x.
%s::%s: getting TRBufSize failed
%s::%s: cannot set error code key
%s::%s: ring open failed %s state %d, flags 0x%x
%s::%s: creating CR failed %s
%s::%s: completion %s starting completion processing with count:%u tag:%u
%s::%s: invalid logAction callback
%s::%s: invalid nub properties
%s::%s: owner %s, pipe %s exit
%s::%s: invalid logaction callback
%s::%s: memory allocation to CR name failed
%s::%s: creating TR failed %s
%s::%s: sync monitor setup completed for TR %s
%s::%s: failed with error: 0x%08x.
%s::%s: creating a ring failed
%s::%s: invalid transport driver
%s::%s: trname %s, trsize %u, trbufsize %u
%s::%s: TR %s state is available
%s::%s: invalid debug nub props dictionary
%s::%s: opening rings failed
%s::%s: create stream failed for ring %s
%s::%s: exit
%s::%s: copying dispatch queue failed with error: 0x%08x.
%s::%s: transport client creation failed
%s::%s: instatiating pipe object failed
%s::%s: cancelling the timer failed 0x%08x.
%s::%s: getting pipe size failed
%s::%s: failed to get owner object
%s::%s: invalid argument
%s::%s: invalid logger argument
%s::%s: invalid ioctx
%s::%s: tag %u, len %u completion size %u
%s::%s: memory allocation to ringinfo list failed
%s::%s: memory allocation to nubs failed
%s::%s: getting ring buffer type failed
%s::%s: enqueue failed
%s::%s: completion count %s is 0
%s::%s: free space not available
%s::%s: instantiating CentauriDebug transport failed
%s::%s: invalid nub
%s::%s: failed to create an ioservice for %s, error: 0x%08x.
%s::%s: nub name %s successful
%s::%s: failed to get dir name
%s::%s: constructing open params failed
%s::%s: isBufferTypeFooter %d, inplacecompletion %d
%s::%s: setting up TR sync monitor failed
%s::%s: getting dir name failed
%s::%s: invalid nub name
%s::%s: invalid enabled ring
%s::%s: getting stream config failed for ring %s
%s::%s: unable to allocate cr sync monitor
%s::%s: first tag %u, processed count %u, completion count %u
%s::%s: creating stream options failed for ring %s
%s::%s: invalid ring parameters
%s::%s: transfer completion failed completion io result = 0x%08x
%s::%s: invalid ring props
%s::%s: ring Info found
%s::%s: invalid ivars
%s::%s: getting log datatype failed
%s::%s: block copy failed
%s::%s: invalid key
%s::%s: failed to allocate memory
%s::%s: creating a buffer pool failed
%s::%s: invalid CR handle
%s::%s: setting up CR monitor failed
%s::%s: %s enqueued %u.. free space available was:%u
%s::%s: failed to create log pipe
%s::%s: owner %s, pipe %s entry
%s::%s: invalid transport handle
%s::%s: enabled ring name %s
%s::%s: memory allocation ring info failed
%s::%s: getting file name failed
%s::%s: Ring state Not Open is handled as part of TR Not Open
%s::%s: opening more than enabled rings numRings =  %u, enabledRings = %u
%s::%s: getting CRBufSize failed
%s::%s: finished opening a ring %s
%s::%s: registering nubs failed with error: 0x%08x.
%s::%s: copy properties of Plugin failed
%s::%s: getting CRSize failed
%s::%s: invalid provider
%s::%s: finished
%s::%s: registering a nub failed 0x%08x.
%s::%s: getting stream name failed for ring %s
%s::%s: completion size zero for tag %u
%s::%s: super init() failed
%s::%s: register service on failed
%s::%s: max count reached %u
%s::%s: invalid log stream
%s::%s: ring entries %u, Ringbufsize %u
%s::%s: CR %s state is available
%s::%s: unable to allocate tr sync monitor
%s::%s: invalid transport resources
%s::%s: setting a name failed for %s nub, error: 0x%08x.
%s::%s: failed to get logging properties object
%s::%s: creating pipes and streams failed
%s::%s: getting pipe name failed for ring %s
%s::%s: invalid airship resource name
%s::%s: cannot set props dictionary
%s::%s: failed to report error (ret = 0x%x)
%s::%s: instatiating stream object failed
%s::%s: first tag %u, completion count %u
%s::%s: completion size is zero for tag %u
%s::%s: 
%s::%s: failed to open a ring %s
%s::%s: no nubs in CentauriDebug
%s::%s: getting log policy failed
%s::%s: opening transfer ring failed
%s::%s: TR %s state is open
%s::%s: %s unable to enqueue the buffer to Airship ret = 0x%08x
%s::%s: failed to get logger
%s::%s: memory allocation to dictionary failed
%s::%s: %s enqueue request.. free space available:%u
%s::%s: no rings are Enabled
%s::%s: finished ret = 0x%08x.
%s::%s: failed to alloc OSNumber for error code
%s::%s: opening completion ring failed
%s::%s: copying properties failed 0x%08x.
%s::%s: failed to create log stream
%s::%s: getting tr name failed
%s::%s: getting TRSize failed
%s::%s: invalid ring paramenters
%s::%s: close failed with error : 0x%08x.
%s::%s: getting CRName failed
%s::%s: invalid airship resources
%s::%s: invalid trsize %s
%s::%s: finished successfully
%s::%s: invalid plugin rings
%s::%s: invalid context
%s::%s: number of rings zero
%s::%s: getting dictionary for %s failed
%s::%s: copy properties of provider failed
%s::%s: getting enabled rings failed
%s::%s: ring entries %u, bufsize %u
%s::%s: CR open failed %s
%s::%s: %s unable to enqueue to Airship
%s::%s: rings are already opened
%s::%s: super::init() failed
%s::%s: setting up TR state monitor failed
%s::%s: invalid ipc ring dictionary
%s::%s: airship buffer creation failed
%s::%s: callback finished
%s::%s: getting TRName failed
%s::%s: failed to set default dispatch queue (ret = 0x%x)
%s::%s: failed to get logging properties dict
%s::%s: invalid resources argument
%s::%s: empty airship resources
%s::%s: TR open failed %s
%s::%s: memory allocation to ivars failed
%s::%s: creating a pipe failed for ring %s
%s::%s: acquire airship resource failed %s, resource status = 0x%08x
%s::%s: enqueueRx operation failed
%s::%s: super::Start() failed
%s::%s: trname %s, trsize %u
%s::%s: memory allocation to properties dictionary failed
%s::%s: destroying a ring failed
%s::%s: failed to get log file name
%s::%s: invalid factory method parameters
%s::%s: memory allocation to footer failed
%s::%s: super init failed
%s::%s: getting log id failed
%s::%s: failed to alloc OSString for module name
%s::%s: CR activate failed %s, retVal = 0x%08x
%s::%s: invalid enabled rings
%s::%s: nub name %s
%s::%s: getting pipe config failed
%s::%s: creating TR state monitor failed %s
%s::%s: memory allocation to buf item failed
%s::%s: calling open for ring %s
%s::%s: unable to get provider's provider
%s::%s: transfer completion failed completion io result 0x%08x
%s::%s: failed to instantiate the logger object
%s::%s: getting num files failed
%s::%s: %s successully processed %u
%s::%s: super::Stop failed with error: 0x%08x.
%s::%s: Deferring opening rings based on logging policy
%s::%s: creating a pipe and stream failed
%s::%s: cannot set module key
%s::%s: setting an object failed
%s::%s: setting props failed for %s nub, error: 0x%08x.
%s::%s: timer start failed 0x%08x.
%s::%s: sync monitor setup completed for CR %s
%s::%s: invalid pipe properties
%s::%s: stream name %s entry
%s::%s: invalid TR handle
%s::%s: creating CR state monitor failed %s
%s::%s: firmware logging is disabled centauri-debug=0
%s::%s: invalid ring params list
%s::%s: getting file size failed
%s::%s: invalid completionBlock
%s::%s: TR open successful %s
%s::%s: none enqueued
%s::%s: ring name %s
%s::%s: open failed with error: 0x%08x.
%s::%s: rings already closed
%s::%s: failed to get log id
%s::%s: opening completion Ring failed
%s::%s: invalid log pipe
%s::%s: TR activate failed %s retVal = 0x%08x
%s::%s: TR %s state is un-open
%s::%s: invalid handle
%s::%s: invalid ring handle
%s::%s: memory allocation to array failed
%s::%s: memory allocation to CentauriDebugAirshipIOContext failed
%s::%s: CR %s state is open
%s::%s: failed to get default dispatch queue (ret = 0x%x)
%s::%s: invalid ring name
%s::%s: register service failed
%s::%s: getting pipe owner failed for ring %s
%s::%s: invalid dispatch queue
%s::%s: failed to close a %s ring
%s::%s: iterateObjects failed
%s::%s: starting a pipe failed for ring %s
%s::%s: invalid nub props
%s::%s: Logging prop: owner: %s dir: %s file: %s id: %s
%s::%s: creating pipe options failed for ring %s
%s::%s: getting log type failed
%s::%s: crname %s, crsize %u, crbufsize %u
%s::%s: memory allocation to TR name failed
%s::%s: iterateObjects on nub prop failed
%s::%s: invalid numRings pointer
%s::%s: getting InPlaceCompletion object failed
%s::%s: CR open successful %s
```
