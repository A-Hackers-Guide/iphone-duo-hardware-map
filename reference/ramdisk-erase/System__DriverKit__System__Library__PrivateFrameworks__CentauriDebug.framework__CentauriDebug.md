# `/System/DriverKit/System/Library/PrivateFrameworks/CentauriDebug.framework/CentauriDebug`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 232,240 bytes.

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
%s::%s: enqueueRx operation failed \n
%s::%s: creating CR state monitor failed %s \n
%s::%s: getting dictionary for %s failed \n
DebugNubs
isEnabled
%s::%s: starting a pipe failed for ring %s \n
%s::%s: getting pipe size failed \n
%s::%s: ring entries %u, bufsize %u \n
%s::%s: memory allocation to ringinfo list failed \n
%s::%s: invalid ring handle \n
%s::%s: setting a name failed for %s nub, error: 0x%08x. \n
%s::%s: getting enabled rings failed \n
CRBufSize
%s::%s: crname %s, crsize %u, crbufsize %u \n
%s::%s: failed to alloc OSString for module name \n
OpenOnQueue
%s::%s: trname %s, trsize %u \n
ret == kIOReturnSuccess
%s::%s: getting TRName failed \n
bufferTypeFooter
%s::%s: TR open failed %s \n
airshipResult == AIRSHIP_OK
%s::%s: rings are already opened \n
%s::%s: super::Start failed with error: 0x%08x. \n
CompressionDisabled
%s::%s: invalid logger argument \n
%s::%s: getting CRBufSize failed \n
%s::%s: unable to get provider's provider \n
%s::%s: creating a buffer pool failed \n
EnqueueRx
%s::%s: getting CRSize failed \n
%s::%s: %s unable to enqueue the buffer to Airship ret = 0x%08x \n
%s::%s: super init() failed \n
centauri-debug-loglevel
%s::%s: block copy failed \n
OpenTR
%s::%s: finished \n
CreateAllNubs
DebugDriverLogs
%s::%s: getting tr size failed \n
%s::%s: invalid resources argument \n
CreateNub
%s::%s: constructing open params failed \n
%s::%s: getting file size failed \n
ReportError
%s::%s: enqueue failed \n
ProcessRxCompletionsByFooterMem
%s::%s: first tag %u, processed count %u, completion count %u \n
%s::%s: copy properties of provider failed \n
CreatePipeAndStream
%s::%s: getting InPlaceCompletion object failed \n
completion.size <= item->extbuf_length
%s::%s: memory allocation to buf item failed \n
%s::%s: owner %s, pipe %s entry \n
%s::%s: invalid log pipe \n
%s::%s: TR activate failed %s retVal = 0x%08x \n
%s::%s: ring entries %u, Ringbufsize %u \n
LogIdentifier
%s::%s: invalid enabled ring \n
%s::%s: memory allocation ring info failed \n
TRSize
%s::%s: getting CRName failed \n
%s::%s: memory allocation to properties dictionary failed \n
OpenCR
%s::%s: invalid logAction callback \n
Close
%s::%s: callback finished \n
%s::%s: invalid dispatch queue \n
%s::%s: cannot set error code key \n
%s::%s: invalid ioctx \n
%s::%s: completion %s starting completion processing with count:%u tag:%u \n
%s::%s: getting pipe config failed \n
%s::%s: memory allocation to CentauriDebugAirshipIOContext failed \n
ModuleName
%s::%s: super::Start() failed \n
%s::%s: CR open failed %s \n
%s::%s: invalid nub props \n
NumberOfFiles
%s::%s: creating a ring failed \n
PopulatePipeOptions
%s::%s: invalid trsize %s \n
%s::%s: memory allocation to nubs failed \n
%s::%s: no rings are Enabled \n
%s::%s: getting num files failed \n
%s::%s: finished ret = 0x%08x. \n
%s::%s: memory allocation to TR name failed \n
%s::%s: memory allocation to footer failed \n
%s::%s: setting up TR sync monitor failed \n
%s::%s: failed to create an ioservice for %s, error: 0x%08x. \n
LoggingProperties
%s::%s: failed to close a %s ring \n
InPlaceCompletion
%s::%s: TR %s state is un-open \n
EnqueueRxByFooterMem
%s::%s: invalid key \n
%s::%s: setting an object failed \n
LogFileName
%s::%s: timer start failed 0x%08x. \n
%s::%s: cannot set props dictionary \n
%s::%s: invalid CR handle \n
%s::%s: Ring state Not Open is handled as part of TR Not Open \n
%s::%s: calling open for ring %s \n
centauri-debug
%s::%s: ring Info found \n
%s::%s: getting TRSize failed \n
%s::%s: invalid airship resources \n
%s::%s: failed with error: 0x%08x. \n
%s::%s: instantiating CentauriDebug transport failed \n
CreatePipesAndStreams
%s::%s: failed to report error (ret = 0x%x) \n
%s::%s: setting up CR monitor failed \n
%s::%s: finished successfully \n
%s::%s: creating pipes and streams failed \n
%s::%s: cannot set module key \n
airship_acipc_tr_get_in_place(ioctx->trInfo.tr) == ioctx->inPlaceCompletion
%s::%s: CR %s state is available \n
Start_Impl
%s::%s: failed to set default dispatch queue (ret = 0x%x) \n
%s::%s: super::Stop failed with error: 0x%08x. \n
%s::%s: invalid ring paramenters \n
Open
%s::%s: getting stream config failed for ring %s \n
%s::%s: invalid logaction callback \n
DestroyRing
%s::%s: finished opening a ring %s \n
%s::%s: invalid transport resources \n
InitWithProviderAndOptions
%s::%s: invalid plugin rings \n
%s::%s: create stream failed for ring %s \n
%s::%s: max count reached %u \n
%s::%s: invalid context \n
%s::%s: exit \n
CreateNub_block_invoke
%s::%s: close failed with error : 0x%08x. \n
%s::%s: memory allocation to open params failed \n
%s::%s: invalid pipe properties \n
CreateBufferPool
ProcessRxCompletionsByExtBuf
%s::%s: getting TRBufSize failed \n
%s::%s: isBufferTypeFooter %d, inplacecompletion %d \n
%s::%s: getting dir name failed \n
%s::%s: instatiating pipe object failed \n
%s::%s: owner %s, pipe %s exit \n
%s::%s: none enqueued \n
CloseOnQueue
NubProperties
%s::%s: creating a pipe and stream failed \n
%s::%s: tag %u, len %u completion size %u \n
%s::%s: invalid numRings pointer \n
%s::%s: open failed with error: 0x%08x. \n
%s::%s: creating TR failed %s \n
%s::%s: stream name %s entry \n
%s::%s: %s unable to enqueue to Airship \n
buf != nullptr
%s::%s: invalid nub name \n
PipeSize
ReOpenRings
%s::%s: iterateObjects on nub prop failed \n
DirectoryName
%s::%s: copy properties of Plugin failed \n
%s::%s: Deferring opening rings based on logging policy \n
%s::%s: TR %s state is available \n
%s::%s: unable to allocate tr sync monitor \n
ConfigureCRSyncMonitor
%s::%s: unable to allocate cr sync monitor \n
%s::%s: registering nubs failed with error: 0x%08x. \n
%s::%s: invalid nub properties \n
CentauriDebug
false
%s::%s: CR open successful %s \n
%s::%s: CR %s state is open \n
ProcessRxCompletions
CreateRing
TRStateChangeCallback
%s::%s: %s enqueued %u.. free space available was:%u \n
%s::%s: invalid ring params list \n
Name
%s::%s: invalid completionBlock \n
%s::%s: creating TR state monitor failed %s \n
%s::%s: %s successully processed %u \n
%s::%s:  \n
%s::%s: creating stream options failed for ring %s \n
%s::%s: invalid ring parameters \n
CreateStream
%s::%s: register service failed \n
logLevelChanged
%s::%s: opening completion ring failed \n
%s::%s: copying dispatch queue failed with error: 0x%08x. \n
AirshipResources
%s::%s: creating pipe options failed for ring %s \n
%s::%s: getting ring buffer type failed \n
%s::%s: ring open failed %s state %d, flags 0x%x \n
%s::%s: invalid handle \n
%s::%s: firmware logging is disabled centauri-debug=0 \n
%s::%s: destroying a ring failed \n
%s::%s: getting pipe name failed for ring %s \n
TRName
CRStateChangeCallback
CreateAllNubs_block_invoke
%s::%s: enabled ring name %s \n
%s::%s: invalid ipc ring dictionary \n
%s::%s: CR activate failed %s, retVal = 0x%08x \n
%s::%s: failed to get default dispatch queue (ret = 0x%x) \n
CentauriDebugEnabledRings
%s::%s: getting tr name failed \n
%s::%s: invalid airship resource name \n
%s::%s: free space not available \n
%s::%s: invalid enabled rings \n
%s::%s: opening rings failed \n
FileSize
%s::%s: instatiating stream object failed \n
InitWithOptions
%s::%s: empty airship resources \n
%s::%s: TR open successful %s \n
%s::%s: setting up TR state monitor failed \n
%s::%s: rings already closed \n
%s::%s: finished %x \n
%s::%s: nub name %s successful \n
FreeOpenParams
%s::%s: getting pipe owner failed for ring %s \n
%s::%s: invalid transport driver \n
%s::%s: creating CR failed %s \n
%s::%s: transfer completion failed completion io result 0x%08x \n
PopulateStreamOptions
%s::%s: opening completion Ring failed \n
B24@?0^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}8^{OSObject=^^?Aii^{OSMetaClass}^^?(?=^{OSObject_IVars}^{OSObject_LocalIVars})}16
%s::%s: getting log id failed \n
LogPolicyCapture
%s::%s: sync monitor setup completed for TR %s \n
%s::%s: completion size is zero for tag %u \n
%s::%s: transfer completion failed completion io result = 0x%08x \n
%s::%s: airship buffer creation failed \n
free
%s::%s: memory allocation to dictionary failed \n
CopyIPCRingProps_block_invoke
%s::%s: creating a pipe failed for ring %s \n
ConfigureTRSyncMonitor
%s::%s: %s enqueue request.. free space available:%u \n
Default
%s::%s: iterateObjects failed \n
loggerstream
%s::%s: invalid transport handle \n
NotifyTimeout_Impl
CRSize
%s::%s: completion count %s is 0 \n
%s::%s: nub name %s \n
%s::%s: setting props failed for %s nub, error: 0x%08x. \n
%s::%s: getting log type failed \n
%s::%s: invalid argument \n
%s::%s: invalid TR handle \n
Stop_Impl
v8@?0
%s::%s: ring name %s \n
PipeConfig
%s::%s: memory allocation to work item failed \n
%s::%s: memory allocation to CR name failed \n
%s::%s: opening transfer ring failed \n
%s::%s: copying properties failed 0x%08x. \n
%s::%s: registering a nub failed 0x%08x. \n
Owner
%s::%s: register service on failed \n
LogDataTypePcap
%s::%s: super::init() failed \n
ErrorDetected
index < numRings
TransportResources
%s::%s: invalid debug nub props dictionary \n
%s::%s: invalid ring props \n
CopyIPCRingProps
%s::%s: trname %s, trsize %u, trbufsize %u \n
%s::%s: sync monitor setup completed for CR %s \n
completion.size <= ioctx->footerSize
init
%s::%s: opening more than enabled rings numRings =  %u, enabledRings = %u \n
%s::%s: failed to open a ring %s \n
v24@?0*8Q16
%s::%s: getting stream name failed for ring %s \n
%s::%s: TR %s state is open \n
%s::%s: completion size zero for tag %u \n
%s::%s: memory allocation to array failed \n
%s::%s: memory allocation transport client name failed \n
CRName
%s::%s: invalid ring name \n
%s::%s: no nubs in CentauriDebug \n
ConstructOpenParams
%s::%s: getting log policy failed \n
LogTypeCircular
%s::%s: number of rings zero \n
%s::%s: getting file name failed \n
RearmNotifyTimer
%s::%s: acquire airship resource failed %s, resource status = 0x%08x \n
EnqueueRxByExtBuf
ErrorCode
StreamConfig
Filename
%s::%s: getting log datatype failed \n
CreatePipe
%s::%s: cancelling the timer failed 0x%08x. \n
TRBufSize
%s::%s: failed to alloc OSNumber for error code \n
%s::%s: first tag %u, completion count %u \n
%s::%s: invalid provider \n
%s::%s: invalid nub \n
FreeResources
%s::%s: invalid log stream \n
%s::%s: transport client creation failed \n
%s::%s: invalid ring props
%s::%s: cancelling the timer failed 0x%08x.
%s::%s: invalid transport driver
%s::%s: getting TRName failed
%s::%s: failed to get owner object
%s::%s: copy properties of provider failed
%s::%s: create stream failed for ring %s
%s::%s: getting log id failed
%s::%s: getting TRBufSize failed
%s::%s: memory allocation to properties dictionary failed
%s::%s: cannot set props dictionary
%s::%s: registering nubs failed with error: 0x%08x.
%s::%s: failed with error: 0x%08x.
%s::%s: timer start failed 0x%08x.
%s::%s: trname %s, trsize %u
%s::%s: TR open failed %s
%s::%s: opening rings failed
%s::%s: invalid numRings pointer
%s::%s: instatiating pipe object failed
%s::%s: invalid dispatch queue
%s::%s: invalid CR handle
%s::%s: memory allocation to open params failed
%s::%s: invalid airship resource name
%s::%s: getting CRName failed
%s::%s: creating CR state monitor failed %s
%s::%s: %s enqueue request.. free space available:%u
%s::%s: tag %u, len %u completion size %u
%s::%s: invalid log pipe
%s::%s: getting tr name failed
%s::%s: TR activate failed %s retVal = 0x%08x
%s::%s: creating TR state monitor failed %s
%s::%s: CR %s state is available
%s::%s: %s unable to enqueue the buffer to Airship ret = 0x%08x
%s::%s: invalid completionBlock
%s::%s: CR open successful %s
%s::%s: memory allocation to ivars failed
%s::%s: failed to get default dispatch queue (ret = 0x%x)
%s::%s: invalid enabled rings
%s::%s: invalid factory method parameters
%s::%s: getting pipe size failed
%s::%s: getting TRSize failed
%s::%s: isBufferTypeFooter %d, inplacecompletion %d
%s::%s: registering a nub failed 0x%08x.
%s::%s: instatiating stream object failed
%s::%s: callback finished
%s::%s: setting up CR monitor failed
%s::%s: register service failed
%s::%s: getting enabled rings failed
%s::%s: completion size is zero for tag %u
%s::%s: super::Start() failed
%s::%s: creating a pipe and stream failed
%s::%s: getting pipe name failed for ring %s
%s::%s: unable to allocate tr sync monitor
%s::%s: completion %s starting completion processing with count:%u tag:%u
%s::%s: crname %s, crsize %u, crbufsize %u
%s::%s: memory allocation to work item failed
%s::%s: enqueueRx operation failed
%s::%s: creating pipes and streams failed
%s::%s: invalid trsize %s
%s::%s: Ring state Not Open is handled as part of TR Not Open
%s::%s: invalid handle
%s::%s: failed to create log pipe
%s::%s: trname %s, trsize %u, trbufsize %u
%s::%s: ring entries %u, bufsize %u
%s::%s: %s enqueued %u.. free space available was:%u
%s::%s: %s successully processed %u
%s::%s: failed to get logger
%s::%s: finished successfully
%s::%s: creating a buffer pool failed
%s::%s: invalid TR handle
%s::%s: TR %s state is un-open
%s::%s: invalid key
%s::%s: memory allocation to ringinfo list failed
%s::%s: invalid resources argument
%s::%s: memory allocation transport client name failed
%s::%s: CR activate failed %s, retVal = 0x%08x
%s::%s: memory allocation to buf item failed
%s::%s: creating stream options failed for ring %s
%s::%s: setting up TR state monitor failed
%s::%s: %s unable to enqueue to Airship
%s::%s: finished opening a ring %s
%s::%s: register service on failed
%s::%s: memory allocation to array failed
%s::%s: getting pipe owner failed for ring %s
%s::%s: memory allocation to CentauriDebugAirshipIOContext failed
%s::%s: finished
%s::%s: failed to instantiate the logger object
%s::%s: Deferring opening rings based on logging policy
%s::%s: TR %s state is open
%s::%s: constructing open params failed
%s::%s: invalid ring parameters
%s::%s: failed to close a %s ring
%s::%s: invalid nub props
%s::%s: setting an object failed
%s::%s: open failed with error: 0x%08x.
%s::%s: getting tr size failed
%s::%s: rings already closed
%s::%s: Logging prop: owner: %s dir: %s file: %s id: %s
%s::%s: getting dir name failed
%s::%s: invalid ipc ring dictionary
%s::%s: empty airship resources
%s::%s: failed to allocate memory
%s::%s: copy properties of Plugin failed
%s::%s: first tag %u, processed count %u, completion count %u
%s::%s: getting log datatype failed
%s::%s: opening transfer ring failed
%s::%s: creating CR failed %s
%s::%s: CR %s state is open
%s::%s: completion count %s is 0
%s::%s: number of rings zero
%s::%s: no rings are Enabled
%s::%s: close failed with error : 0x%08x.
%s::%s: memory allocation to CR name failed
%s::%s: failed to alloc OSNumber for error code
%s::%s: invalid nub
%s::%s: invalid plugin rings
%s::%s: creating TR failed %s
%s::%s: ring entries %u, Ringbufsize %u
%s::%s: opening completion ring failed
%s::%s: starting a pipe failed for ring %s
%s::%s: super::Start failed with error: 0x%08x.
%s::%s: opening completion Ring failed
%s::%s: invalid logAction callback
%s::%s: no nubs in CentauriDebug
%s::%s: invalid nub properties
%s::%s: stream name %s entry
%s::%s: TR open successful %s
%s::%s: TR %s state is available
%s::%s: unable to allocate cr sync monitor
%s::%s: completion size zero for tag %u
%s::%s: iterateObjects on nub prop failed
%s::%s: getting file name failed
%s::%s: sync monitor setup completed for CR %s
%s::%s: copying properties failed 0x%08x.
%s::%s: exit
%s::%s: 
%s::%s: invalid ring name
%s::%s: copying dispatch queue failed with error: 0x%08x.
%s::%s: finished %x
%s::%s: nub name %s
%s::%s: failed to get logging properties dict
%s::%s: invalid ivars
%s::%s: invalid logaction callback
%s::%s: failed to report error (ret = 0x%x)
%s::%s: first tag %u, completion count %u
%s::%s: invalid airship resources
%s::%s: getting stream config failed for ring %s
%s::%s: unable to get provider's provider
%s::%s: failed to get dir name
%s::%s: memory allocation to footer failed
%s::%s: getting stream name failed for ring %s
%s::%s: invalid argument
%s::%s: memory allocation to TR name failed
%s::%s: invalid ring paramenters
%s::%s: instantiating CentauriDebug transport failed
%s::%s: getting log policy failed
%s::%s: getting log type failed
%s::%s: none enqueued
%s::%s: super::Stop failed with error: 0x%08x.
%s::%s: destroying a ring failed
%s::%s: creating pipe options failed for ring %s
%s::%s: getting num files failed
%s::%s: block copy failed
%s::%s: getting CRBufSize failed
%s::%s: transfer completion failed completion io result 0x%08x
%s::%s: getting dictionary for %s failed
%s::%s: invalid pipe properties
%s::%s: setting props failed for %s nub, error: 0x%08x.
%s::%s: memory allocation to nubs failed
%s::%s: super init failed
%s::%s: ring name %s
%s::%s: ring Info found
%s::%s: transport client creation failed
%s::%s: CR open failed %s
%s::%s: free space not available
%s::%s: opening more than enabled rings numRings =  %u, enabledRings = %u
%s::%s: firmware logging is disabled centauri-debug=0
%s::%s: invalid enabled ring
%s::%s: getting CRSize failed
%s::%s: cannot set module key
%s::%s: cannot set error code key
%s::%s: ring open failed %s state %d, flags 0x%x
%s::%s: setting up TR sync monitor failed
%s::%s: failed to set default dispatch queue (ret = 0x%x)
%s::%s: failed to copy properties
%s::%s: failed to get logging properties object
%s::%s: super::init() failed
%s::%s: failed to open a ring %s
%s::%s: invalid ring handle
%s::%s: failed to get log id
%s::%s: super init() failed
%s::%s: rings are already opened
%s::%s: failed to create log stream
%s::%s: invalid provider
%s::%s: enabled ring name %s
%s::%s: invalid log stream
%s::%s: sync monitor setup completed for TR %s
%s::%s: enqueue failed
%s::%s: transfer completion failed completion io result = 0x%08x
%s::%s: iterateObjects failed
%s::%s: memory allocation to dictionary failed
%s::%s: invalid ring params list
%s::%s: creating a pipe failed for ring %s
%s::%s: owner %s, pipe %s exit
%s::%s: getting InPlaceCompletion object failed
%s::%s: calling open for ring %s
%s::%s: invalid transport resources
%s::%s: invalid debug nub props dictionary
%s::%s: invalid nub name
%s::%s: setting a name failed for %s nub, error: 0x%08x.
%s::%s: memory allocation ring info failed
%s::%s: invalid ioctx
%s::%s: getting pipe config failed
%s::%s: max count reached %u
%s::%s: failed to alloc OSString for module name
%s::%s: airship buffer creation failed
%s::%s: getting file size failed
%s::%s: failed to create an ioservice for %s, error: 0x%08x.
%s::%s: invalid transport handle
%s::%s: acquire airship resource failed %s, resource status = 0x%08x
%s::%s: nub name %s successful
%s::%s: failed to get log file name
%s::%s: owner %s, pipe %s entry
%s::%s: finished ret = 0x%08x.
%s::%s: invalid logger argument
%s::%s: getting ring buffer type failed
%s::%s: creating a ring failed
%s::%s: invalid context
```
