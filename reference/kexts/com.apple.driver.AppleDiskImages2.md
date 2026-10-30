# `com.apple.driver.AppleDiskImages2`

- Name: AppleDiskImages2
- Version: `598.40.4`
- UUID: `DB71DA43-1D49-39A6-B645-1F4C460F784D`
- Source version: `598.40.4.0.0`
- Depends on: [`com.apple.iokit.IOStorageFamily`](com.apple.iokit.IOStorageFamily.md) 2.1, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 17.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 17.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 17.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 17.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 17.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 17.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleDiskImageDevice
- `CFBundleIdentifier`: `com.apple.driver.AppleDiskImages2`
- `IOClass`: `AppleDiskImagesController`
- `IOMatchCategory`: `AppleDiskImageDevice`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDiskImages2`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOKit`
- `IOUserClientClass`: `DIDeviceCreatorUserClient`


## C++ classes (6) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleDiskImageDevice` | 0x7238 | IOBlockStorageDevice → IOService → IORegistryEntry |
| `AppleDiskImagesController` | 0x98 | IOService → IORegistryEntry |
| `DIDeviceCreatorUserClient` | 0xf8 | IOUserClient → IOService → IORegistryEntry |
| `DIDeviceIOUserClient` | 0x158 | IOUserClient → IOService → IORegistryEntry |
| `DIDeviceRequestPool` | 0xb8 |  |
| `DIFracturedMemoryMap` | 0x28 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1800)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000066b8 off=0x00418160-0x0041e818 addr=0xfffffe000741c160-0xfffffe0007422818 r--/r--   __TEXT            
	sz=0x00003a16 off=0x004188c8-0x0041c2de addr=0xfffffe000741c8c8-0xfffffe00074202de               __TEXT.__cstring          (CstringLiterals)
	sz=0x00002522 off=0x0041c2de-0x0041e800 addr=0xfffffe00074202de-0xfffffe0007422800               __TEXT.__os_log           
	sz=0x00000018 off=0x0041e800-0x0041e818 addr=0xfffffe0007422800-0xfffffe0007422818               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x000123dc off=0x01b703d0-0x01b827ac addr=0xfffffe0008b743d0-0xfffffe0008b867ac r-x/r-x   __TEXT_EXEC       
	sz=0x00011e2c off=0x01b703d0-0x01b821fc addr=0xfffffe0008b743d0-0xfffffe0008b861fc          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000005b0 off=0x01b821fc-0x01b827ac addr=0xfffffe0008b861fc-0xfffffe0008b867ac          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000631 off=0x0493ca88-0x0493d0b9 addr=0xfffffe000b940a88-0xfffffe000b9410b9 rw-/rw-   __DATA            
	sz=0x000004e8 off=0x0493ca88-0x0493cf70 addr=0xfffffe000b940a88-0xfffffe000b940f70               __DATA.__data             
	sz=0x00000148 off=0x00000000-0x00000148 addr=0xfffffe000b940f70-0xfffffe000b9410b8               __DATA.__common           (Zerofill)
	sz=0x00000001 off=0x00000000-0x00000001 addr=0xfffffe000b9410b8-0xfffffe000b9410b9               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000025a0 off=0x0104cff0-0x0104f590 addr=0xfffffe0008050ff0-0xfffffe0008053590 rw-/rw-   __DATA_CONST      
	sz=0x00000030 off=0x0104cff0-0x0104d020 addr=0xfffffe0008050ff0-0xfffffe0008051020         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000030 off=0x0104d020-0x0104d050 addr=0xfffffe0008051020-0xfffffe0008051050         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001e40 off=0x0104d050-0x0104ee90 addr=0xfffffe0008051050-0xfffffe0008052e90         __DATA_CONST.__const            
	sz=0x00000280 off=0x0104ee90-0x0104f110 addr=0xfffffe0008052e90-0xfffffe0008053110         __DATA_CONST.__kalloc_type      
	sz=0x00000014 off=0x0104f110-0x0104f124 addr=0xfffffe0008053110-0xfffffe0008053124         __DATA_CONST.__assert           
	sz=0x000000f0 off=0x0104f128-0x0104f218 addr=0xfffffe0008053128-0xfffffe0008053218         __DATA_CONST.__kalloc_var       
	sz=0x000002d8 off=0x0104f218-0x0104f4f0 addr=0xfffffe0008053218-0xfffffe00080534f0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000a0 off=0x0104f4f0-0x0104f590 addr=0xfffffe00080534f0-0xfffffe0008053590         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 202 at 0x04ad6e74
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     DB71DA43-1D49-39A6-B645-1F4C460F784D
008: LC_SOURCE_VERSION           598.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9d328 size=0x250
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleDiskImages2`
- `CFBundleIdentifier`: `com.apple.driver.AppleDiskImages2`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleDiskImages2`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `598.40.4`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `598.40.4`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2000-2018 Apple Inc. All rights reserved.`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleDiskImages2.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901505696`
- `_PrelinkExecutableRelativePath`: `AppleDiskImages2`
- `_PrelinkExecutableSize`: `112229`
- `_PrelinkExecutableSourceAddr`: `-2198901505696`
- `_PrelinkKmodInfo`: `-2198829004152`

## Strings (400) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `didevice_cache_fully_satisfied`
- `Physical Interconnect Location`
- `didevice_trace`
- `autodiskmount`
- `uint32_t AppleDiskImageDevice::getCreatorUCPID() const`
- `site.AppleDiskImageDevice`
- `site.DIDeviceRequestPool`
- `static IOReturn DIDeviceIOUserClient::StashFileInformation(OSObject *, void *, IOExternalMethodArguments *)`
- `site.DIDeviceCreatorUserClient`
- `virtual void AppleDiskImagesController::free()`
- `virtual void AppleDiskImageDevice::free()`
- `kIOReturnSuccess == ( status )`
- `Disk Image`
- `PersistentAttach`
- `static IOReturn DIDeviceIOUserClient::GetCacheStats(OSObject *, void *, IOExternalMethodArguments *)`
- `I`
- `( 0 != fBarrierQueueLock )`
- `Solid State`
- `kIOReturnSuccess == ( ret )`
- `fDirect.fMem.fMap`
- `RAM`
- `site.T`
- `IOReturn AppleDiskImageDevice::SetDeviceParams(const DICreateDeviceParams *)`
- `void AppleDiskImageDevice::CompleteCommand(uint32_t, int)`
- `bool AppleDiskImageDevice::sendDaemonRespawnMessage()`
- `static IOReturn DIDeviceIOUserClient::DrainDormantQueue(OSObject *, void *, IOExternalMethodArguments *)`
- `/Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/AppleDiskImages2/AppleDiskImagesController.cpp`
- `IOReturn AppleDiskImageDevice::HandleUnmappedDIORequest(DIDeviceRequest *)`
- `bool AppleDiskImageDevice::AddStorageFeaturesDict(bool, bool)`
- `void AppleDiskImageDevice::cleanupDormantState()`
- `site.AppleDiskImagesController`
- `( 0 != controllerEntry )`
- `void AppleDiskImageDevice::AbortAllCommands()`
- `bounded_ptr<T>::operator+=(n): Calculating the number of bytes to add to the offset (n * sizeof(T)) would trigger an overflow`
- `12122`
- `IOServiceBusyTimeoutExtensions`
- `static IOReturn DIDeviceCreatorUserClient::CreateDevice(OSObject *, void *, IOExternalMethodArguments *)`
- `LU`
- `didevice read by kernel bytes`
- `( 0 != devicesIterator )`
- `void AppleDiskImageDevice::CompleteRequest(DIDeviceRequest *, int, bool)`
- `bool AppleDiskImageDevice::setCreatorUC(DIDeviceCreatorUserClient *)`
- `bool AppleDiskImageDevice::requestGracefulShutdown(bool)`
- `DIDeviceRequestPool`
- `Medium Type`
- `owner-gid`
- `didevice_thread_cache_reads`
- `IOReturn AppleDiskImagesController::FindExistingDevice(DICreateDeviceParams *, DICreateDeviceReply *)`
- `ShadowURL`
- `void AppleDiskImageDevice::TerminateMightFaultThread(MightFaultCopier_t &)`
- `IOReturn AppleDiskImageDevice::boostAnyRequest(uint8_t)`
- `IOReturn AppleDiskImageDevice::PrepareMappedBuffersForIO(DIDeviceRequest *, bool)`
- `virtual void DIDeviceRequestPool::free()`
- `didevice_queue_depth`
- `AppleDiskImageDevice`
- `IOReturn AppleDiskImageDevice::PrepareRequest(DIDeviceRequest *, enum kDIIO, KernelInflightGuard, bool, IOStorageAttributes *, bool)`
- `DIDeviceRequestPool.h`
- `1211111111122212112222222222122`
- `( 0 != element )`
- `virtual void DIDeviceCreatorUserClient::stop(IOService *)`
- `IOReturn AppleDiskImageDevice::SetupDormantRequestBuffers(DIDeviceRequest *)`
- `UsingDirectIO`
- `uint64_t DIDeviceIOUserClient::ioMem(IOMemoryDescriptor *, size_t, uint64_t, size_t, kDIIODirectDir)`
- `IOReturn AppleDiskImagesController::CreateDevice(DICreateDeviceParams *, DICreateDeviceReply *, OSSharedPtr<AppleDiskImageDevice> &)`
- `1211111212221212111111111112121112122112112`
- `v32@?0^{?=II^{ipc_port}^{ipc_port}Ii}8^(?={?=(?=^{ipc_port}^{ipc_port}^{ipc_port})b16b8b8I}{?=IIb8b8b8b8}{?=IIb8b8b8b8}{?=IIb24b8}{?=IIb16b8b8})16^v24`
- `File`
- `virtual void DIDeviceIOUserClient::stop(IOService *)`
- `IOReturn AppleDiskImageDevice::executeBarrierQueueElement(DIDeviceRequest *, bool)`
- `virtual IOReturn DIDeviceCreatorUserClient::message(UInt32, IOService *, void *)`
- `virtual void AppleDiskImageDevice::stop(IOService *)`
- `bool AppleDiskImageDevice::onIOClientClose(DIDeviceIOUserClient *)`
- `site.DIFracturedMemoryMap`
- `bool DIDeviceRequestPool::AllocateRequests(size_t, user_addr_t, size_t, unsigned int)`
- `static void DIDeviceRequestPool::ReleasePoolElements(uint32_t &, ::IOLWPool<TElem> &, Mode) [TElem = DIDeviceRequest]`
- `quarantine`
- `/Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/AppleDiskImages2/AppleDiskImageDevice.cpp`
- `num_outstanding_requests <= MAX_OUTSTANDING_REQUESTS`
- `121111121222121211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `virtual IOReturn DIDeviceCreatorUserClient::clientClose()`
- `didevice default cache size in bytes`
- `CacheURL`
- `External`
- `!notification_ports[ type ]`
- `didevice_enable_cache`
- `void AppleDiskImageDevice::dormantIOTimeoutOccurred(OSObject *, IOTimerEventSource *)`
- `bool AppleDiskImageDevice::onCreatorClientClose()`
- `virtual IOReturn AppleDiskImageDevice::doEjectMedia()`
- `IOReturn AppleDiskImageDevice::ValidateAndSetupCommonParams(DIDeviceIOUserClient *, DIDeviceIOParams *, uint16_t)`
- `\"attempting to advance map iterator past end (currentOffset=%zu, endOffset=%zu)\" @%s:%d`
- `/Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/AppleDiskImages2/DIDeviceIOUserClient.cpp`
- `didevice_cache_spared_bytes`
- `( 0 != instanceIDString )`
- `fDirect.fMem.fBuffer`
- `DIControllerGlobals::~DIControllerGlobals()`
- `Apple`
- `Physical Interconnect`
- `bool AppleDiskImageDevice::flushDeviceWithTimeout(uint32_t)`
- `( 0 != fUserClientsLock )`
- `IOReturn AppleDiskImageDevice::enqueueRequest(DIDeviceRequest *, bool)`
- `RootDeviceEntryID`
- `IOMaximumByteCountRead`
- `DIFracturedMemoryMap`
- `Q`
- `%x`
- `Protocol Characteristics`
- `static IOReturn DIDeviceIOUserClient::Connect(OSObject *, void *, IOExternalMethodArguments *)`
- `didevice_thread_mapped_buf_writes`
- `IU`
- `site.DIDeviceIOUserClient`
- `com.apple.diskimages.creator-uc`
- `didevice write by kernel bytes`
- `598.40.4`
- `Device is not clean`
- `didevice count of cache reads by thread`
- `( 0 != dict )`
- `maxIdx == curIdx + 1 || maxIdx == curIdx`
- `Product Revision Level`
- `Daemon died during drain`
- `virtual bool DISharedBuffer::init(user_addr_t, unsigned int)`
- `selector < ARRAY_LENGTH ( gMethods )`
- `didevice_write_by_kernel_bytes`
- `Virtual Interface`
- `status == 0 `
- `\"invalid slice (startOffset=%zu, endOffset=%zu, mdSize=%zu)\" @%s:%d`
- `mach_port_t DIDeviceIOUserClient::findNotificationPort(unsigned int)`
- `didevice spared bytes by cache`
- `Device Characteristics`
- `Unmap`
- `1211111212221212112`
- `didevice count of page faulted buffers that initiated read/write requests`
- `Vendor Name`
- `\"attempting to access iterator past end (currentOffset=%zu, endOffset=%zu)\" @%s:%d`
- `12212111221211122121112`
- `IOReturn DIDeviceRequestPool::AllocateBuffersForRequest(DIDeviceRequest *, size_t, bool, abort_request_allocation_fn_t, void *)`
- `virtual IOReturn DIDeviceCreatorUserClient::externalMethod(uint32_t, IOExternalMethodArguments *, IOExternalMethodDispatch *, OSObject *, void *)`
- `InstanceID`
- `owner-mode`
- `type < getMaxPorts ( )`
- `virtual void DIDeviceCreatorUserClient::free()`
- `didevice enable cache`
- `sparse-backend`
- `virtual bool DIDeviceIOUserClient::start(IOService *)`
- `index < num_notification_ports`
- `virtual bool DIDeviceCreatorUserClient::initWithTask(task_t, void *, UInt32)`
- `didevice no bounce count`
- `didevice fully satisfied by cache`
- `( 0 != instanceIDKey )`
- `userClient`
- `( 0 != mappedAddress )`
- `Product Name`
- `static IOReturn DIDeviceIOUserClient::RequestGracefulShutdown(OSObject *, void *, IOExternalMethodArguments *)`
- `didevice_no_bounce_count`
- `void AppleDiskImageDevice::mightFaultThread()`
- `DiskImageURL`
- `kIOReturnSuccess == ( ret_code )`
- `DaemonPID`
- `void AppleDiskImageDevice::respawnRetryTimerFired(OSObject *, IOTimerEventSource *)`
- `bool AppleDiskImageDevice::triggerDaemonRespawn()`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `/Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/AppleDiskImages2/DIDeviceRequestPool.cpp`
- `size_t DIDeviceRequestPool::AddBuffersForReconnection(user_addr_t, size_t, unsigned int)`
- `static IOReturn DIDeviceIOUserClient::AllocPortsArray(OSObject *, void *, IOExternalMethodArguments *)`
- `DIDeviceCreatorUserClient`
- `( 0 != controllerIterator )`
- `virtual bool AppleDiskImagesController::start(IOService *)`
- `( 0 != fCreateLock )`
- `deviceNum`
- `IOMaximumByteCountWrite`
- `IOReturn IOLWPool<DISharedBuffer>::dequeueElements(Mode, size_t, queue_head_t *, bool *, size_t) [T = DISharedBuffer]`
- `AssertMacros: %s, %s file: %s, line: %d, value: %lld\n`
- `bucketIdx < fNrWriteSeqCounters`
- `Priority`
- `port`
- `minIdx == curIdx - 1 || minIdx == curIdx`
- `DIDeviceRequest *DIDeviceRequestPool::GetReservedRequest()`
- `static IOReturn DIDeviceCreatorUserClient::QuarantineDevice(OSObject *, void *, IOExternalMethodArguments *)`
- `/Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/AppleDiskImages2/DIDeviceCreatorUserClient.cpp`
- `result`
- `virtual bool AppleDiskImageDevice::willTerminate(IOService *, IOOptionBits)`
- `IOReturn AppleDiskImageDevice::prepareUnmapCommand(DIDeviceRequest *, bool)`
- `PCI-Express`
- `res`
- `void AppleDiskImageDevice::DIOThread()`
- `DIDeviceIntervalMap.cpp`
- `IOUnit`
- `Serial Number`
- `owner-uid`
- `fPrepareBuffers != NULL`
- `Network`
- `bool AppleDiskImageDevice::drainDormantIOQueue()`
- `OSBoundedPtr.h`
- `High Throughput Options`
- `\"%s\" @%s:%d`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `virtual void DIDeviceIOUserClient::free()`
- `DIDeviceIOUserClient`
- `virtual bool AppleDiskImageDevice::terminate(IOOptionBits)`
- `Barrier`
- `bounded_array_ref: Can't construct from a size greater than UINT32_MAX`
- `index <= fRequestsCount`
- `void DIDeviceRequestPool::ReleaseReservedRequest()`
- `[disk image 2]`
- `( 0 != request )`
- `void AppleDiskImageDevice::cleanupForDaemonRespawn()`
- `didevice_thread_mapped_buf_unmaps`
- `image-encrypted`
- `( 0 != fWriteSeqCountersAllocation )`
- `IOReturn AppleDiskImageDevice::ReconnectForIO(DIDeviceIOUserClient *, DIDeviceIOParams *, uint16_t)`
- `bool AppleDiskImageDevice::setIOProvider(DIDeviceIOUserClient *)`
- `virtual IOReturn DIDeviceIOUserClient::clientClose()`
- `workLoop`
- `image-format-read-only`
- `( 0 != fRequestPool )`
- `IOMaximumBlockCountRead`
- `IOReturn AppleDiskImageDevice::CopyFromSharedBuffers(DIDeviceRequest *)`
- `DIFracturedMemoryMap.cpp`
- `virtual bool DIDeviceIOUserClient::initWithTask(task_t, void *, UInt32)`
- `bs-apple-quarantine-info`
- `AppleDiskImagesController`
- `IOStorageFeatures`
- `bool AppleDiskImageDevice::AddOwnerCredentials()`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `( 0 != pool )`
- `didevice_bounce_count`
- `didevice_read_by_kernel_bytes`
- `IOReturn AppleDiskImageDevice::boostAllPending(uint8_t)`
- `void AppleDiskImageDevice::executeBarrierQueueLocked()`
- `static IOReturn DIDeviceIOUserClient::GetRequestsStats(OSObject *, void *, IOExternalMethodArguments *)`
- `\"diskimages: attempt to dereference a null containing object\" @%s:%d`
- `1211111212221212111111111111112`
- `deviceProps`
- `Graceful shutdown failed`
- `1`
- `didevice bounce count`
- `IOReturn AppleDiskImageDevice::claimDormantDevice(uint32_t)`
- `1211111122112112`
- `didevice count of page faulted buffers that initiated unmap requests`
- `IOMaximumBlockCountWrite`
- `static void DIDeviceRequestPool::ReleasePoolElements(uint32_t &, ::IOLWPool<TElem> &, Mode) [TElem = DISharedBuffer]`
- `didevice_cache_size_default`
- `( 0 != map )`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `virtual bool DIDeviceCreatorUserClient::start(IOService *)`
- `didevice default max queue depth`
- `com.apple.diskimages.io-uc`
- `didevice trace`
- `IOReturn AppleDiskImageDevice::InitForIO(DIDeviceIOUserClient *, DIDeviceIOParams *, uint16_t)`
- `The offset of the pointer inside its valid memory range can't be represented using int32_t`

**[__TEXT.__os_log]**

- `[%d] %s::%d: Aborting barrier queue request %d\n`
- `[%d] %s::%d: AppleDiskImages2: DIO thread exit\n`
- `[%d (ctx)] %s::%d: Requested %zu buffers - does not fit the request buffer count\n`
- `[%d] %s::%d: done\n`
- `[%d] %s::%d: Timeout expired - daemon failed to respawn within 30 seconds, ejecting device\n`
- `[%d] %s::%d: DIO memory: Trying to write beyond end-of-buffer\n`
- `[%d] %s::%d: DIO memory: IOMD copied too few bytes?`
- `[%d] %s::%d: Too many files stashed: %u (max=%u)\n`
- `[%d] %s::%d: Device is not clean - attempting flush with timeout\n`
- `[%d] %s::%d: Terminated\n`
- `[%d] %s::%d: Storage features: unmap=%d, barrier=%d\n`
- `[%d] %s::%d: Device reconnection - setting new IO provider %p (PID=%u)\n`
- `[%d] %s::%d: Device is clean - performing graceful shutdown\n`
- `[%d (ctx)] %s::%d: Can't map buffer at user address=0x%llx size %u to kernel\n`
- `[%d (ctx)] %s::%d: Failed to add any buffers for reconnection (requested %zu)\n`
- `[%d] %s::%d: DIO memory isn't mapped\n`
- `[%d] %s::%d: Init for direct IO returned an error %d, continue anyway with fallback mode\n`
- `[%d] %s::%d: Provider was not set\n`
- `[%d] %s::%d: Quarantine device called when fDevice is null\n`
- `[%d] %s::%d: AppleDiskImages2: Cache copier thread exit\n`
- `[%d] %s::%d: Device is not active - cannot perform graceful shutdown\n`
- `[%d] %s::%d: Successfully sent respawn message for instance ID %s with fOldDaemonPID=%u\n`
- `[%d] %s::%d: block_count=%llu block_size=%u\n`
- `[%d (ctx)] %s::%d: kext version: %s\n`
- `[%d (ctx)] %s::%d: Can't allocate all buffers, allocated %zu/%zu`
- `[%d] %s::%d: mach port number is invalid\n`
- `[%d] %s::%d: Respawn retries exhausted\n`
- `[%d] %s::%d: No persistent attach support\n`
- `[%d] %s::%d: Buffer allocation succeeded (fNumBuffers=%u)\n`
- `[%d] %s::%d: Enqueue failed during dormant mode\n`
- `[%d] %s::%d: Respawn send failed, retrying (%u left)\n`
- `[%d] %s::%d: provider_name=%s\n`
- `[%d] %s::%d: AllocPortsArray wasn't called before Connect`
- `[%d] %s::%d: AllocPortsArray was called twice, existing %u, got %u`
- `[%d (ctx)] %s::%d: Found an existing device with instance ID %s and entry ID 0x%llx\n`
- `[%d] %s::%d: DI Error: IO daemon returned wrong offset, requested 0x%llx, got 0x%llx\n`
- `[%d] %s::%d: Reconnection failed: newProvider->isInactive()=%d\n`
- `[%d] %s::%d: Completed successfully\n`
- `[%d (ctx)] %s::%d: Can't allocate reserved flush request\n`
- `[%d] %s::%d: Bad provider\n`
- `[%d] %s::%d: Drain failed during reconnection (PID=%u)\n`
- `[%d] %s::%d: Cancelled timeout during cleanup\n`
- `[%d] %s::%d: Device is inactive/terminating - aborting respawn\n`
- `[%d] %s::%d: \n`
- `[%d] %s::%d: no extents available (fUnmapExtents=%p)\n`
- `[%d] %s::%d: InitForIO called but device is not inactive\n`
- `[%d] %s::%d: Failed to write data on completion\n`
- `[%d] %s::%d: Cancelled dormant I/O timeout during drain\n`
- `[%d] %s::%d: Client is not entitled to use DIDeviceIOUserClient\n`
- `[%d] %s::%d: Client has entitlement to use DIDeviceCreatorUserClient.\n`
- `[%d] %s::%d: Aborting request %d\n`
- `[%d] %s::%d: Device is shutting down or dormant - terminating old user client %p\n`
- `[%d] %s::%d: Failed to claim dormant device during reconnection (status=0x%x)\n`
- `[%d] %s::%d: Flush did not complete - ejecting device instead of going dormant\n`
- `[%d] %s::%d: Failed to get instance ID from device registry\n`
- `[%d (ctx)] %s::%d: PoolCount=%d, dequeue failed\n`
- `[%d] %s::%d: Failed setting quarantine info\n`
- `[%d] %s::%d: Infrastructure destroyed during drain - failing request\n`
- `[%d] %s::%d: Can't write to client\n`
- `[%d] %s::%d: block_count = %llu, block_size = %u, instance ID = %s\n`
- `[%d] %s::%d: request %d not found\n`
- `[%d] %s::%d: Device already clean - skipping flush\n`
- `[%d] %s::%d: \n `
- `[%d] %s::%d: STALE_COMPLETION: req[%u] - dropping completion from dying daemon (status=%d)\n`
- `[%d] %s::%d: Invalid buffer size\n`
- `[%d] %s::%d: Timeout scheduled for daemon reconnection (%u ms)\n`
- `[%d] %s::%d: Client has entitlement to use DIDeviceIOUserClient.\n`
- `[%d] %s::%d: Duplicate dormant device claim rejected\n`
- `[%d] %s::%d: Client is not entitled to use DIDeviceCreatorUserClient\n`
- `[%d] %s::%d: Bad provider class %s\n`
- `[%d] %s::%d: Terminating\n`
- `[%d] %s::%d: ReconnectForIO called but device is not dormant/draining\n`
- `[%d] %s::%d: Eject request is complete`
- `[%d] %s::%d: Reserved request is null or already in use - cannot perform flush\n`
- `[%d] %s::%d: IO daemon hasn't fulfilled %zu of the required bytes of %zu. Total size is %zu, Response size is %llu Offsets: %llu/%llu, #buffers=%u\n`
- `[%d] %s::%d: Device was already created\n`
- `[%d (ctx)] %s::%d: No existing device matches the instance ID, creating a new one\n`
- `[%d] %s::%d: Cancelled dormant I/O timeout during terminate\n`
- `[%d] %s::%d: Dormant request transitioning to active (cmd=%d, offset=%llu, size=%zu)\n`
- `[%d] %s::%d: Creator user client closed but there's no IO user client, terminating.\n`
- `[%d] %s::%d: %s, ejecting device\n`
- `[%d] %s::%d: Drain completed successfully\n`
- `[%d] %s::%d: Can't allocate lock for DIDeviceCreatorUserClient\n`
- `[%d (ctx)] %s::%d: registry entry ID: 0x%llx`
- `[%d] %s::%d: Graceful shutdown completed successfully - device is now dormant\n`
- `[%d] %s::%d: Already triggered, returning early\n`
- `[%d (ctx)] %s::%d: Can't allocate all requests, allocated %zu/%zu`
- `[%d] %s::%d: Persistent attach not supported - rejecting file stashing\n`
- `[%d] %s::%d: Timeout callback fired but timeout was cancelled - ignoring\n`
- `[%d] %s::%d: Driver's ABI version: %d, Controller's ABI version: %d\n`
- `[%d] %s::%d: User-client PID mismatch with creator user-client PID: %d\n`
- `[%d] %s::%d: Failed to prepare dormant request (fIndex=%u): %d\n`
- `[%d] %s::%d: Stopping barrier queue execution - device is dormant\n`
- `[%d] %s::%d: Dormant request (fIndex=%u) fully satisfied from cache\n`
- `[%d] %s::%d: queue or buffer user addresses are nullptr`
- `[%d] %s::%d: Can't get current qos to boost to tier %u\n`
- `[%d] %s::%d: Released %u vnode references during cleanup\n`
- `[%d] %s::%d: Flush submit failed with status=%d\n`
- `[%d] %s::%d: Device was not initialized correctly.\n`
- `[%d] %s::%d: Reconnection failed: could only allocate %zu of %u buffers\n`
- `[%d] %s::%d: Failed to allocate mach ports`
- `[%d] %s::%d: Attempting to quarantine device with buffer size %hu\n`
- `[%d] %s::%d: Reconnection: successfully allocated %zu new buffers\n`
- `[%d] %s::%d: Flush completed with status=%d\n`
- `[%d] %s::%d: Device is active - not triggering respawn\n`
- `[%d (ctx)] %s::%d: Reserved request already in use\n`
- `[%d] %s::%d: Failed to map quarantine params\n`
- `[%d] %s::%d: Keeping device as IO user is connected\n`
- `[%d] %s::%d: Failed to parse instance ID UUID: %s\n`
- `[%d (ctx)] %s::%d: Allocated reserved flush request with index %u (not in pool)\n`
- `[%d] %s::%d: vnode_ref failed for file %u: error=%d - disabling persistent attach\n`
- `[%d] %s::%d: Wrong argument size, %lu. Actual %llu\n`
- `[%d] %s::%d: First queued I/O - triggering daemon respawn and starting timeout\n`
- `[%d (ctx)] %s::%d: done\n`
- `[%d] %s::%d: Reconnection failed (status=0x%x) - terminating device\n`
- `[%d] %s::%d: vnode_getfromfd failed for file %u (fd=%lld): error=%d - disabling persistent attach\n`
- `[%d] %s::%d: No device initialized for drain\n`
- `[%d] %s::%d: Failed setting a property\n`
- `[%d] %s::%d: Flush timed out after %ums\n`
- `[%d] %s::%d: Setting fClientPID to %u (was %u), fOldDaemonPID was %u\n`
- `[%d] %s::%d: queue_depth = %u mach_ports = %u\n`
- `[%d] %s::%d: Invalid provider - IO UC exists=%d Creator UC exists=%d\n`
- `[%d] %s::%d: Got kIOMessageServiceIsTerminated from %s\n`
- `[%d] %s::%d: Device reconnection - replacing old provider %p with new provider %p (PID=%u)\n`
- `[%d] %s::%d: No creator UC to get PID for\n`
- `[%d] %s::%d: Pool deactivated - all buffers freed\n`
- `[%d] %s::%d: Driver's ABI version: %d, Daemon's ABI version: %d\n`
- `[%d] %s::%d: Incompatible client: expected ABI version %d actual %d\n`
- `[%d] %s::%d: Moved %zu pending requests to barrier queue\n`
- `[%d] %s::%d: Drain already in progress - concurrent drain attempt detected\n`
- `[%d] %s::%d: Beginning drain\n`
- `[%d] %s::%d: host_get_diskimagesiod_port failed: 0x%x\n`
- `[%d] %s::%d: Successfully stashed file %u: ino=%llu fsid=%d:%d (total files: %u)\n`
- `[%d] %s::%d: mach_msg_send_from_kernel_proper failed: 0x%x\n`
- `[%d] %s::%d: Timeout scheduled for %u ms from now\n`
- `[%d] %s::%d: DIO: tried to write %zu, but actually wrote %llu\n`
- `[%d] %s::%d: Invalid device flags: 0x%02x\n`
- `[%d (ctx)] %s::%d: Reserved request released\n`
- `[%d] %s::%d: Bad argument: fileInfo is NULL\n`
- `[%d] %s::%d: Failed setting quarantine flag\n`
- `[%d] %s::%d: A new creator UC tried to connect to an existing device.\n`
- `[%d] %s::%d: Device does not support persistent attach - rejecting\n`
- `[%d] %s::%d: All kernel requests completed\n`
- `[%d] %s::%d: Device is not clean and flush not allowed - failing graceful shutdown\n`
- `[%d] %s::%d: Drain aborted: device no longer in dormant state\n`
- `[%d] %s::%d: Drain aborted: timeout was not active\n`
- `[%d (ctx)] %s::%d: Can't allocate IOMD for buffer at user address=0x%llx size %u\n`
- `[%d (ctx)] %s::%d: \n`
- `[%d] %s::%d: Failed to complete request from completion thread\n`
- `[%d (ctx)] %s::%d: PoolCount=%d\n`
- `[%d (ctx)] %s::%d: Not enough elements in pool, requested = %zu, numElements = %zu, reserved = %zu\n`
