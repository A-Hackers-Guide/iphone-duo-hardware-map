# `com.apple.audio.TrustedClockingKEXT`

- Name: TrustedClockingKEXT
- Version: `1.0.0`
- UUID: `03118B2E-232F-359C-9CC7-612F4936B595`
- Source version: `95.202.0.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### TrustedClockingKEXT
- `CFBundleIdentifier`: `com.apple.audio.TrustedClockingKEXT`
- `IOClass`: `TrustedClockingKEXT`
- `IOMatchCategory`: `TrustedClockingKEXT`
- `IOPersonalityPublisher`: `com.apple.audio.TrustedClockingKEXT`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOBSD`
- `IOUserClientClass`: `TrustedClockingUserClient`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `TrustedClockingKEXT` | 0x18c8 | IOService → IORegistryEntry |
| `TrustedClockingUserClient` | 0xf0 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00003809 off=0x00da54c0-0x00da8cc9 addr=0xfffffe0007da94c0-0xfffffe0007daccc9 r--/r--   __TEXT            
	sz=0x00000080 off=0x00da5b38-0x00da5bb8 addr=0xfffffe0007da9b38-0xfffffe0007da9bb8               __TEXT.__const            
	sz=0x00003111 off=0x00da5bb8-0x00da8cc9 addr=0xfffffe0007da9bb8-0xfffffe0007daccc9               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x0000c7dc off=0x0399d040-0x039a981c addr=0xfffffe000a9a1040-0xfffffe000a9ad81c r-x/r-x   __TEXT_EXEC       
	sz=0x0000c2dc off=0x0399d040-0x039a931c addr=0xfffffe000a9a1040-0xfffffe000a9ad31c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000500 off=0x039a931c-0x039a981c addr=0xfffffe000a9ad31c-0xfffffe000a9ad81c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000160 off=0x04a35b80-0x04a35ce0 addr=0xfffffe000ba39b80-0xfffffe000ba39ce0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a35b80-0x04a35c48 addr=0xfffffe000ba39b80-0xfffffe000ba39c48               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000ba39c48-0xfffffe000ba39ca8               __DATA.__common           (Zerofill)
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000ba39ca8-0xfffffe000ba39ce0               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001bc0 off=0x014a00c0-0x014a1c80 addr=0xfffffe00084a40c0-0xfffffe00084a5c80 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x014a00c0-0x014a00d0 addr=0xfffffe00084a40c0-0xfffffe00084a40d0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x014a00d0-0x014a00e0 addr=0xfffffe00084a40d0-0xfffffe00084a40e0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001860 off=0x014a00e0-0x014a1940 addr=0xfffffe00084a40e0-0xfffffe00084a5940         __DATA_CONST.__const            
	sz=0x00000080 off=0x014a1940-0x014a19c0 addr=0xfffffe00084a5940-0xfffffe00084a59c0         __DATA_CONST.__kalloc_type      
	sz=0x00000280 off=0x014a19c0-0x014a1c40 addr=0xfffffe00084a59c0-0xfffffe00084a5c40         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000040 off=0x014a1c40-0x014a1c80 addr=0xfffffe00084a5c40-0xfffffe00084a5c80         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 168 at 0x04afe628
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     03118B2E-232F-359C-9CC7-612F4936B595
008: LC_SOURCE_VERSION           95.202.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004accb40 size=0x248
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `TrustedClockingKEXT`
- `CFBundleGetInfoString`: `Copyright © 2025 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.audio.TrustedClockingKEXT`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `TrustedClockingKEXT`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/TrustedClockingKEXT.kext`
- `_PrelinkExecutableLoadAddr`: `-2198891490112`
- `_PrelinkExecutableRelativePath`: `TrustedClockingKEXT`
- `_PrelinkExecutableSize`: `72965`
- `_PrelinkExecutableSourceAddr`: `-2198891490112`
- `_PrelinkKmodInfo`: `-2198827984000`

## Strings (138) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `121111121222121211111111111112`
- `\"TB_ASSERT: \" \"(server->starthwattime != ((void*)0)) && \\\"implementation for startHWAtTime is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->startioattime != ((void*)0)) && \\\"implementation for startIOAtTime is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `TrustedClockingUserClient::start - Failed to cast provider to TrustedClockingKEXT\n`
- `v24@?0Q8r^{coreaudiodevicetypes_coreaudiostreamdescription_s=III{coreaudiodevicetypes_coreaudioformatdescription_s=IIIIIII}}16`
- `TrustedClockingWorkloopContext::stopHardware [%u] - Failed to stop modulus: %d\n`
- `\"TB_FATAL: \" \"invalid value: unexpected case value, %llx\" @%s:%d`
- `TrustedClockingKEXTImpl::startKernelWorkloop - No state for useCaseID %u\n`
- `TrustedClockingKEXT::setupTransportAndPublisherForCallbacks - transport=%p publisher=%p\n`
- `TrustedClockingUserClient::externalMethod - Invalid selector %u\n`
- `TrustedClockingWorkloopContext::setupTightbeamComponents - Failed to initialize modulus tightbeam client: %d\n`
- `TrustedClockingKEXT::trustedStartIO - transport service unavailable\n`
- `TrustedClockingKEXT::stop - Stopping AoE Clocking driver...\n`
- `TrustedClockingWorkloopContext::tryStartKernelWorkloop - Workloop already running\n`
- `TrustedClockingWorkloopContext::triggerWorkloopDataAvailability - Semaphore not initialized for useCaseID %u\n`
- `TrustedClockingWorkloopContext::setupTightbeamComponents - Failed to initialize courier io tightbeam client: %d\n`
- `\"TB_ASSERT: \" \"(vErr == TB_ERROR_SUCCESS) && \\\"tb_message_subrange failed\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_FATAL: \" \"overflow detected when adding\" @%s:%d`
- `TightbeamDeviceService::stopHW - Tightbeam call failed: %d\n`
- `PMAssertionStateMachine::notifyWorkloopStarted - record invalid for useCaseId %u\n`
- `PMAssertionStateMachine::notifyWorkloopStopped - assertion ID is already zero for useCaseId %u\n`
- `TrustedClockingKEXTImpl::stopKernelWorkloop [%u] - stop failed\n`
- `TrustedClockingWorkloopContext::startKernelWorkloop - Signaling workloop to start with use case ID: %u\n`
- `TrustedClockingWorkloopContext::tryStopKernelWorkloop - semaphore timed wait failed: 0x%x\n`
- `TrustedClockingKEXT::start - AoE Clocking driver started successfully!\n`
- `\"TB_FATAL: \" \"unrecognized selector: %llu\" @%s:%d`
- `TrustedClockingWorkloopContext::startKernelWorkloop - Semaphores not valid for use case ID: %u\n`
- `\"TB_ASSERT: \" \"(server->stopio != ((void*)0)) && \\\"implementation for stopIO is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `TrustedClockingWorkloopContext::ioCycleIteration - Semaphore operation returned kern aborted\n`
- `TrustedClockingKEXT::probe - Probing hardware...\n`
- `\"TB_ASSERT: \" \"(server->stophw != ((void*)0)) && \\\"implementation for stopHW is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `site.TrustedClockingKEXT`
- `\"TB_ASSERT: \" \"(server->writetostream != ((void*)0)) && \\\"implementation for writeToStream is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `TightbeamDeviceService::initialize - Failed: %d\n`
- `TrustedClockingUserClient::stop - User client stopping\n`
- `\"TB_ASSERT: \" \"(server->stop != ((void*)0)) && \\\"implementation for stop is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `TightbeamDeviceService::destroy - Destroying device client\n`
- `PMAssertionStateMachine::notifyWorkloopInvalidated - releasing orphaned assertion for useCaseId %u\n`
- `TrustedClockingKEXTImpl::processKernelWorkloop [%u] - Exiting\n`
- `TrustedClockingWorkloopContext::startHardware - Failed to call startHW on device transport: %d\n`
- `TrustedClockingWorkloopContext::processKernelWorkloop - Capturing workloop\n`
- `TrustedClockingKEXT::free - Goodbye from the kernel!\n`
- `I16@?0^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}8`
- `CourierMessageHandler::sendSync - waiting on semaphore for sync message delivery confirmation failed\n`
- `TrustedClockingKEXT::trustedSignalIO - transport service unavailable\n`
- `^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16`
- `\"TB_ASSERT: \" \"(server->readfromstream != ((void*)0)) && \\\"implementation for readFromStream is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `TightbeamCourierService::courierSendMessage - Failed: %d\n`
- `TrustedClockingWorkloopContext::setupTightbeamComponents - Failed to initialize device tightbeam client: %d\n`
- `TrustedClockingUserClient::externalMethod - Access denied for selector %u: missing entitlement\n`
- `\"TB_ASSERT: \" \"(coreaudiocourier_couriermessage__decode(msg, &courierMessage) == TB_ERROR_SUCCESS) && \\\"failed to decode type: CoreAudioCourier.CourierMessage\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS) && \\\"failed to wrap packed buffer\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_FATAL: \" \"invalid tag in '[CoreAudioDeviceTypes.CoreAudioStreamDescription]' metadata: 0x%x\" @%s:%d`
- `TightbeamCourierService::initialize - Failed: %d\n`
- `TightbeamModulusService::initialize - Failed: %d\n`
- `PMAssertionStateMachine::notifyWorkloopStarted - createPMAssertion failed for useCaseId %u\n`
- `TrustedClockingKEXTImpl::stopKernelWorkloop - No state for useCaseID %u\n`
- `TrustedClockingKEXT_c.c`
- `TightbeamModulusService::getRendezvous - Failed: %d\n`
- `CourierMessageHandler::deliver - failed to deliver transaction %llu to useCaseId %u\n`
- `PMAssertionStateMachine::notifyWorkloopStopped - releasePMAssertion failed for useCaseId %u\n`
- `TrustedClockingWorkloopContext::triggerWorkloopDataAvailability - Workloop not running\n`
- `TrustedClockingKEXT::trustedTransactionalMessage - Trusted domain is sending message %llu to identifier %llu\n`
- `\"TB_ASSERT: \" \"(server->messagearrived != ((void*)0)) && \\\"implementation for messageArrived is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `v8@?0`
- `TrustedClockingWorkloopContext::tryStopKernelWorkloop - Workloop already stopped\n`
- `TrustedClockingKEXT::trustedStopIO - Trusted domain called StopIO for identifier %llu\n`
- `TrustedClockingKEXTImpl::registerUseCaseState - add failed for useCaseId %u\n`
- `PMAssertionStateMachine::addRecord - unable to add record for useCaseId %u\n`
- `TrustedClockingUserClient::clientDied - Client died unexpectedly\n`
- `\"TB_ASSERT: \" \"(server->getupdatedperiodictimestamp != ((void*)0)) && \\\"implementation for getUpdatedPeriodicTimestamp is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `I24@?0{coreaudiobasetypes_coreaudiotimestamp_s=QQ}8`
- `PMAssertionStateMachine::notifyWorkloopStarted - assertion ID non-zero for useCaseId %u\n`
- `v16@?0^{WorkloopContext={WorkloopSetup=QIQQQI}^{KernelSemaphore}^{KernelSemaphore}^{KernelSemaphore}^{KernelSemaphore}^{KernelMutex}ABABAB^{ServicesContainer}^{KernelUtilities}}8`
- `TrustedClockingWorkloopContext::init - Invalid frameSize %llu or SampleRate %u for use case ID: %u\n`
- `TrustedClockingWorkloopContext::handleStart - Waiting on start failed\n`
- `TrustedClockingWorkloopContext::processKernelWorkloop - Exiting captured workloop\n`
- `\"TB_ASSERT: \" \"(server->getrendezvous != ((void*)0)) && \\\"implementation for getRendezvous is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `TrustedClockingWorkloopContext::getRendezvous [%u] - getRendezvous failed: %d, %d\n`
- `TrustedClockingKEXT::trustedTransactionalMessage - Message Transaction %llu successfully sent to identifier %llu\n`
- `site.TrustedClockingUserClient`
- `TrustedClockingUserClient::start - User client starting\n`
- `TrustedClockingUserClient::start - Failed to start super\n`
- `\"TB_FATAL: \" \"overflow detected when multiplying\" @%s:%d`
- `TightbeamDeviceService::startHW - Tightbeam call failed: %d\n`
- `Cycle %llu: wake time %llu (current %llu)\n`
- `I12@?0I8`
- `TightbeamModulusService::start - Failed: %d\n`
- `TrustedClockingWorkloopContext::tryStartKernelWorkloop - Semaphore signal failed: 0x%x\n`
- `TrustedClockingWorkloopContext::stopKernelWorkloop - Semaphores not valid for use case ID: %u\n`
- `TrustedClockingKEXT::trustedStopIO - transport service unavailable\n`
- `TrustedClockingKEXT::trustedSignalIO - Trusted domain called SignalIO for identifier %llu\n`
- `TrustedClockingUserClient: Client does not have entitlement '%s' and is operating with limited functionality.\n`
- `I24@?0{coreaudiomodulus_rendezvousresult_s=iQ}8`
- `v24@?0{coreaudiomodulus_rendezvousresult_s=iQ}8`
- `TrustedClockingKEXTImpl::stopKernelWorkloop [%u] - PM notify failed\n`
- `WARNING [%u]: waitUntilAbsoluteTime failed: 0x%x\n`
- `TrustedClockingWorkloopContext::stopKernelWorkloop - Signaling workloop to stop with use case ID: %u\n`
- `TrustedClockingKEXT::trustedTransactionalMessage - message service unavailable\n`
- `TrustedClockingUserClient::initWithTask - Failed to initialize super\n`
- `TrustedClocking PM Assertion active`
- `TrustedClockingWorkloopContext::startHardware - startHW returned error: %u\n`
- `TrustedClockingWorkloopContext::handleStop [%u] - Unable to signal thread stopped\n`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `TightbeamModulusService::stop - Failed: %d\n`
- `PMAssertionStateMachine::notifyWorkloopStopped - record invalid for useCaseId %u\n`
- `\"TB_FATAL: \" \"invalid tag in '[UInt64]' metadata: 0x%x\" @%s:%d`
- `PMAssertionStateMachine::notifyWorkloopInvalidated - record not found for useCaseId %u\n`
- `TrustedClockingKEXTImpl::startKernelWorkloop [%u] - failed to signal start\n`
- `v16@?0^{TrustedClockingWorkloopContext={TightbeamServicesContainer=^^?{TightbeamModulusService=^^?B{coreaudiomodulus_coreaudiomodulusservice_s=^{tb_connection_s}}}{TightbeamDeviceService=^^?B{coreaudiodevice_coreaudiodevicetransportservice_s=^{tb_connection_s}}}{TightbeamCourierService=^^?B{coreaudi`
- `TrustedClockingUserClient`
- `com.apple.private.trustedclocking.workloop-control`
- `TrustedClockingUserClient::start - User client started successfully\n`
- `I8@?0`
- `v16@?0^{WorkloopAssertionRecord=QII}8`
- `TrustedClockingKEXT::start - Starting AoE Clocking driver...\n`
- `TrustedClockingUserClient::initWithTask - User client initializing\n`
- `TrustedClockingKEXTImpl::triggerWorkloopDataAvailability - No state for useCaseID %u\n`
- `TrustedClockingKEXT`
- `\"TB_ASSERT: \" \"(server->requestisolatedaudio != ((void*)0)) && \\\"implementation for requestIsolatedAudio is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `TrustedClockingWorkloopContext::init - Invalid kernel primitive for use case ID: %u\n`
- `TrustedClockingWorkloopContext::stopHardware [%u] - stopHW returned error: %u\n`
- `\"TB_ASSERT: \" \"(server->starthw != ((void*)0)) && \\\"implementation for startHW is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->start != ((void*)0)) && \\\"implementation for start is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `v12@?0I8`
- `TrustedClockingWorkloopContext::tryStopKernelWorkloop - semaphore signal failed: 0x%x\n`
- `TrustedClockingWorkloopContext::triggerWorkloopDataAvailability - Failed to signal semaphore for useCaseID %u: 0x%x\n`
- `TrustedClockingKEXTImpl::startKernelWorkloop [%u] - PM notify failed\n`
- `TrustedClockingWorkloopContext::handleStart [%u] - Unable to signal thread started\n`
- `121111121222121211111111112211222112221122211222112221122211222112221122211222112221122211222112221122211211112111121121121111211211211211222222111112111121121121121111211211211211222222111112111121121121121111211211211211222222111112111121121121121111211211211211222222111112111121121121121111211211`
- `TrustedClockingKEXT::init - Hello from the kernel!\n`
- `TrustedClockingUserClient::clientClose - Client closing connection\n`
- `TrustedClockingKEXTImpl::registerUseCaseState - registered useCaseId %u\n`
- `TrustedClockingWorkloopContext::startHardware - Failed to start modulus service: %d\n`
- `TrustedClockingWorkloopContext::tryStartKernelWorkloop - Semaphore timed wail failed: 0x%x\n`
- `TrustedClockingKEXT::start - Failed to start super class\n`
- `TrustedClockingKEXT::start - Failed to start impl\n`
