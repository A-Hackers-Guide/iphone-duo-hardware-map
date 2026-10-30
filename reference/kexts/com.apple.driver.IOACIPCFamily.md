# `com.apple.driver.IOACIPCFamily`

- Name: IOACIPCFamily
- Version: `1`
- UUID: `8F44AE19-1366-31E0-AD52-34F24BB2BA70`
- Source version: `313.0.0.0.0`
- Depends on: [`com.apple.iokit.IOPCIFamily`](com.apple.iokit.IOPCIFamily.md) 2.7.3, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 10.0.0d1

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (31) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOACIPCDebugUserClient` | 0x110 | IOUserClient → IOService → IORegistryEntry |
| `IOAppleConvergedIPCBTIDevice` | 0x100 | IOService → IORegistryEntry |
| `IOAppleConvergedIPCBTIInterface` | 0x138 | IOAppleConvergedIPCInterface → IOService → IORegistryEntry |
| `IOAppleConvergedIPCCallee` | 0x18 |  |
| `IOAppleConvergedIPCCompletionRing` | 0x100 | IOAppleConvergedIPCRing → IOEventSource |
| `IOAppleConvergedIPCControl` | 0x1a0 | IOService → IORegistryEntry |
| `IOAppleConvergedIPCControlUserClient` | 0x110 | IOUserClient → IOService → IORegistryEntry |
| `IOAppleConvergedIPCDebug` | 0x300 | IOService → IORegistryEntry |
| `IOAppleConvergedIPCDebugService` | 0xa8 | IOService → IORegistryEntry |
| `IOAppleConvergedIPCIOCommand` | 0xe8 | IOCommand |
| `IOAppleConvergedIPCIOCommandPool` | 0x70 | IOAppleConvergedIPCPool → IOCommandPool |
| `IOAppleConvergedIPCInterface` | 0xe0 | IOService → IORegistryEntry |
| `IOAppleConvergedIPCKernelTraceBuffer` | 0x68 | IOAppleConvergedIPCTraceBuffer |
| `IOAppleConvergedIPCMemoryPolicy` | 0x68 |  |
| `IOAppleConvergedIPCMemoryPolicyInfo` | 0x60 |  |
| `IOAppleConvergedIPCMessageQueueBase` | 0x70 | IOEventSource |
| `IOAppleConvergedIPCPool` | 0x60 | IOCommandPool |
| `IOAppleConvergedIPCRTIContext` | 0x140 | IOService → IORegistryEntry |
| `IOAppleConvergedIPCRTIDevice` | 0x440 | IOService → IORegistryEntry |
| `IOAppleConvergedIPCRTIInterface` | 0x200 | IOAppleConvergedIPCInterface → IOService → IORegistryEntry |
| `IOAppleConvergedIPCRTISharedInterface` | 0x208 | IOAppleConvergedIPCRTIInterface → IOAppleConvergedIPCInterface → IOService → IORegistryEntry |
| `IOAppleConvergedIPCRing` | 0xd0 | IOEventSource |
| `IOAppleConvergedIPCTraceBackend` | 0xa8 | IOService → IORegistryEntry |
| `IOAppleConvergedIPCTraceBackendRaw` | 0xb8 | IOAppleConvergedIPCTraceBackend → IOService → IORegistryEntry |
| `IOAppleConvergedIPCTraceBuffer` | 0x58 |  |
| `IOAppleConvergedIPCTraceBufferQueue` | 0x40 |  |
| `IOAppleConvergedIPCTraceUserClient` | 0x240 | IOUserClient → IOService → IORegistryEntry |
| `IOAppleConvergedIPCTransferRing` | 0x120 | IOAppleConvergedIPCRing → IOEventSource |
| `IOAppleConvergedIPCUserClient` | 0x138 | IOUserClient → IOService → IORegistryEntry |
| `IOAppleConvergedPCI` | 0x3a0 | IOService → IORegistryEntry |
| `_AppleConvergedIPCMemoryDescriptorHelper` | 0xb0 | IOGeneralMemoryDescriptor → IOMemoryDescriptor |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, DylibInCache
000: LC_SEGMENT_64 sz=0x00003d40 off=0x0096fb80-0x009738c0 addr=0xfffffe0007973b80-0xfffffe00079778c0 r--/r--   __TEXT            
	sz=0x00003441 off=0x00970298-0x009736d9 addr=0xfffffe0007974298-0xfffffe00079776d9               __TEXT.__cstring          (CstringLiterals)
	sz=0x000001e0 off=0x009736e0-0x009738c0 addr=0xfffffe00079776e0-0xfffffe00079778c0               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x000541d8 off=0x02eaddb0-0x02f01f88 addr=0xfffffe0009eb1db0-0xfffffe0009f05f88 r-x/r-x   __TEXT_EXEC       
	sz=0x00053918 off=0x02eaddb0-0x02f016c8 addr=0xfffffe0009eb1db0-0xfffffe0009f056c8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000008c0 off=0x02f016c8-0x02f01f88 addr=0xfffffe0009f056c8-0xfffffe0009f05f88          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000810 off=0x049eb5b8-0x049ebdc8 addr=0xfffffe000b9ef5b8-0xfffffe000b9efdc8 rw-/rw-   __DATA            
	sz=0x00000278 off=0x049eb5b8-0x049eb830 addr=0xfffffe000b9ef5b8-0xfffffe000b9ef830               __DATA.__data             
	sz=0x00000508 off=0x00000000-0x00000508 addr=0xfffffe000b9ef830-0xfffffe000b9efd38               __DATA.__common           (Zerofill)
	sz=0x00000090 off=0x00000000-0x00000090 addr=0xfffffe000b9efd38-0xfffffe000b9efdc8               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00010c88 off=0x012f6b30-0x013077b8 addr=0xfffffe00082fab30-0xfffffe000830b7b8 rw-/rw-   __DATA_CONST      
	sz=0x000000e0 off=0x012f6b30-0x012f6c10 addr=0xfffffe00082fab30-0xfffffe00082fac10         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x000000d0 off=0x012f6c10-0x012f6ce0 addr=0xfffffe00082fac10-0xfffffe00082face0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x0000b6f0 off=0x012f6ce0-0x013023d0 addr=0xfffffe00082face0-0xfffffe00083063d0         __DATA_CONST.__const            
	sz=0x00000010 off=0x013023d0-0x013023e0 addr=0xfffffe00083063d0-0xfffffe00083063e0         __DATA_CONST.__weak_got         (NonLazySymbolPointers)
	sz=0x00003500 off=0x013023e0-0x013058e0 addr=0xfffffe00083063e0-0xfffffe00083098e0         __DATA_CONST.__kalloc_type      
	sz=0x00001950 off=0x013058e0-0x01307230 addr=0xfffffe00083098e0-0xfffffe000830b230         __DATA_CONST.__kalloc_var       
	sz=0x00000460 off=0x01307230-0x01307690 addr=0xfffffe000830b230-0xfffffe000830b690         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000128 off=0x01307690-0x013077b8 addr=0xfffffe000830b690-0xfffffe000830b7b8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 319 at 0x04aef69c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     8F44AE19-1366-31E0-AD52-34F24BB2BA70
008: LC_SOURCE_VERSION           313.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aba448 size=0xca8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOACIPCFamily`
- `CFBundleIdentifier`: `com.apple.driver.IOACIPCFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOACIPCFamily`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `0.8`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2017 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `0.8.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOACIPCFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895903872`
- `_PrelinkExecutableRelativePath`: `IOACIPCFamily`
- `_PrelinkExecutableSize`: `431024`
- `_PrelinkExecutableSourceAddr`: `-2198895903872`
- `_PrelinkKmodInfo`: `-2198828288584`

## Strings (547) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `com.apple.driver.AppleConvergedIPCTrace.user-access`
- `IOAppleConvergedIPCInterface.cpp`
- `kACIPCDirectionInvalid`
- `Type`
- `site.IOAppleConvergedIPCTraceBuffer`
- `%s%u`
- `ACIPCRTIDevice`
- `IOAppleConvergedIPCBTIDevice.cpp`
- `site._MSIRange`
- `12111112122212121112222222221121111111111211211111111112121111222`
- `2113111111`
- `scratch_buffer`
- `kACIPCUnexpectedSleepMessageState`
- `site.acipcBTIDeviceParams`
- `kACIPCPipeOpenFailed`
- `kACIPCLinkUpTimeout`
- `kACIPCLinkStateManualDown`
- `Before publish`
- `kACIPCCompletionOutOfRange`
- `kACIPCPipeCloseFailed`
- `IOAppleConvergedIPCCompletionRing`
- `12111112122212121111112`
- `v12@?0i8`
- `222222211222222121111111111111111`
- `doorbells`
- `ACIPCInterfaceProtocol`
- `AppleConvergedIPCRingSize`
- `B24@?0r^{OSSymbol=^^?ib14b18*{smrq_slink={?=^{smrq_slink}}}}8^{OSObject=^^?i}16`
- `enable`
- `success`
- `kACIPCTransferMissingEvent`
- `ACIPCSharedInterfaceUnit`
- `site.IOACIPCRTIIOTableAtomic`
- `IOAppleConvergedIPCRTIInterface.cpp`
- `virtual`
- `121112111212222222221211112122111111`
- `111`
- `site.T`
- `AppleConvergedIPCGroupIndex`
- `IOAppleConvergedIPCBTIDevice`
- `site.registerData`
- `kACIPCCommandRingFull`
- `acipc-skip-entitlement`
- `completion_rings`
- `index`
- `size`
- `peripheral_ID`
- `site.IOAppleConvergedIPCRTIContext *`
- `site.IOAppleConvergedIPCRTIContext`
- `IOAppleConvergedIPCRTIContext.cpp`
- `site.IOAppleConvergedIPCPool`
- `211`
- `message_ring`
- `IOAppleConvergedIPCBTIInterface.cpp`
- `</array>`
- `site.acipcRTIOpenCompletionCall`
- `RTIContext`
- `opened`
- `Code`
- `site.IOAppleConvergedIPCTraceUserClient`
- `site.asyncBlock`
- `IOAppleConvergedIPCDebug: %p, register service\n`
- `kACIPCTransferCompletionPartialUnexpected`
- `kACIPCInvalidSharedMemoryRegionId`
- `kACIPCInvalidTag`
- `IOAppleConvergedIPCDebug::init failed\n`
- `kACIPCChannelStopFailed`
- `kACIPCReadFail`
- `%s::%s: super init failed\n`
- `site.IOACIPCDebugUserClient`
- `IOAppleConvergedIPCTraceBackend.h`
- `foot_size`
- `group_completion`
- `cr_low`
- `registerErrorHandler`
- `site.IOAppleConvergedIPCControlUserClient`
- `site.IOAppleConvergedIPCRTISharedInterface`
- `1`
- `%s::%s:super failed\n`
- `kACIPCDeviceInvalidStateTransition`
- `</dict>`
- `IOAppleConvergedIPCRTISharedInterface::initWithInfo: super::init failed\n`
- `site.IOAppleConvergedIPCCallee`
- `12111211122112`
- `setup`
- `kACIPCTransferCompletionSizeUnexpected`
- `running`
- `21111`
- `1211111212221212111111111111111112`
- `11211212111`
- `DARTErrorHandlerCallback`
- `kACIPCChannelStopFailedFatal`
- `kACIPCLinkStateSoftDown`
- `Line`
- `IOACIPCBTIPipe.cpp`
- `site.errorInfo`
- `1211112121211`
- `site.acipcMappedIO`
- `AppleConvergedIPCRingDirection`
- `site.IOAppleConvergedIPCTraceBufferQueue`
- `IOAppleConvergedIPCBTIInterface::initWithInfo: super::init failed\n`
- `<key>Codes</key>`
- `site.IOAppleConvergedIPCDebug`
- `Failed to allocate wrapper\n`
- `num_pipes`
- `site.IOAppleConvergedIPCMemoryPolicyInfo`
- `rom`
- `12111122111`
- `ACIPCInterfaceProtocolRole`
- `iavector`
- `site.pciMessageData`
- `IOAppleConvergedIPCRTIContext::initWithInfo: super::init failed\n`
- `site.LogBuffer`
- `ACIPCControlVariant`
- `kACIPCDeviceErrorStateTransition`
- `121111121222121211111`
- `db_index`
- `121111121222121211111111111111111211212`
- `num_CRs_primary_context`
- `site.IOACIPCNullDevice`
- `CodeRegistryTracePointListOffsetOf`
- `cr_index`
- `AppleConvergedIPCCompletionIndex`
- `site.IOAppleConvergedIPCBTIDevice`
- `num_TRs`
- `kACIPCLinkDownTimeout`
- `failed to allocate Trace Buffer (%s)\n`
- `kACIPCUnexpectedSleepMessageTarget`
- `kACIPCLinkStateUp`
- `enable-ptm`
- `(peripheral sleep)`
- `\"Double Free on IOACIPCTrace Buffer\" @%s:%d`
- `threadcall allocation failed\n`
- `max_io_chunk`
- `%s::%s:\n`
- `Arguments`
- `1121`
- `site.acipcImageScatterGather`
- `%s::%s: invalid callback set: ec%u eb%u dc%u db%u\n`
- `uninit`
- `identifier`
- `111221222222221122222222121221111111111111111111212`
- `1211112211122`
- `kACIPCInvalidRingId`
- `site.IOAppleConvergedIPCBTIInterface`
- `IOAppleConvergedIPCRing`
- `IOAppleConvergedIPCTraceUserClient`
- `IOAppleConvergedIPCMessageQueueBase`
- `kACIPCBadRequestError`
- `site.acipcRTIMSIEntity`
- `AppleConvergedIPCTransferRingShared`
- `msi_range`
- `site.hdr_ty.acipcRTIDoorbell`
- `on_demand`
- `IOAppleConvergedIPCTraceBackend`
- `12111211121222222222121111111111`
- `IOACIPCRTIDevice.cpp`
- `IOACIPCNullDevice`
- `2111`
- `i8@?0`
- `site.IOAppleConvergedIPCInterface`
- `121111121222121211212222222222222222222222222222222221111111121212121212121211211111122222222221`
- `Before open`
- `ACIPCTrace attach/start failed %p\n`
- `msi_mod_bytes`
- `ACIPCInterfaceProviderDevice`
- `site.IOAppleConvergedIPCRTISharedInterface *`
- `num_msi_ranges`
- `memory_alloc_limit`
- `site.IOAppleConvergedIPCTracePipeRegistry`
- `AppleConvergedIPCTransferRingProperties`
- `1211111212221212111221111222222222111111`
- `kACIPCPipeAbortFailed`
- `kACIPCSendImageFailed`
- `site.acipcImageIOV`
- `IOAppleConvergedIPCTraceBackendRaw`
- `%s: Error - client object is NULL\n`
- `IOAppleConvergedIPCControlUserClient.cpp`
- `AppleConvergedIPCRingIdentifier`
- `msi_mod_time`
- `site.PipeInfo *`
- `11111111`
- `After terminate`
- `invalid`
- `site.acipcRTIDeviceParams`
- `TracePipe %lu unregistered.\n`
- `Text`
- `IOAppleConvergedIPCRTISharedInterface`
- `site.IOAppleConvergedIPCTraceCodeRegistry`
- `mem_alignment`
- `kACIPCCompletionUnaligned`
- `kACIPCDeviceSleepStateInvalid`
- `IOAppleConvergedIPCBTIInterface`
- `site.acipcRTIPipeParams *`
- `site.IOAppleConvergedIPCRTIInterface`
- `di_msi`
- `site.IOAppleConvergedIPCRTIInterface *`
- `kACIPCDeviceInAbortHandler`
- `TracePipes`
- `(host wake wait)`
- `TraceBufferOffsetOfBuffer`
- `site._AppleConvergedIPCMemoryDescriptorHelper`
- `21121212122222222221111122222222212111111111111111`
- `(unknown)`
- `111111`
- `kACIPCTransferCompletionUnexpectedChannel`
- `kACIPCLinkDown`
- `init`
- `count`
- `site.acipcRTIPipeParams`
- `12121111`
- `site.TracePoint`
- `site.acipcRTIMSIEventCall`
- `kACIPCAERError`
- `kACIPCTagNotInUse`
- `role`
- `IOACIPCBTIDevice`
- `IOAppleConvergedIPCMemoryPolicyInfo`
- `kACIPCTransferUnexpectedEvent`
- `kACIPCControlUnexpectedExecutionEnvironment`
- `12111211121222222222121111`
- `exception_protocol`
- `11211`
- `Before terminate`
- `image_table`
- `site.IOACIPCRTIContext *`
- `IOAppleConvergedIPCInterface`
- `<integer size=\"4\">0x2</integer>`
- `initWithOptions`
- `2211`
- `%s::%s:user client missing access entitlement\n`
- `%s::%s\n`
- `completion_ring`
- `site.IOAppleConvergedIPCDebugService`
- `enqueue callback/block missing\n`
- `IOAppleConvergedIPCControl`
- `site.acipcRTIContextParams`
- `kACIPCDeviceUnknownStateTransition`
- `kACIPCPortEnableFailed`
- `<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">`
- `ACIPCRTIPipe`
- `kACIPCEnterLowPowerFailed`
- `PoolArrayOffset`
- `121`
- `RTIPipe`
- `TraceBufferOffsetOfSize`
- `client_data`
- `1112`
- `IOAppleConvergedIPCDebugGroup`
- `IOAppleConvergedIPCTraceBufferQueue`
- `11`
- `caching_capability`
- `terminating\n`
- `site.crOpenInfo`
- `IOAppleConvergedIPCKernelTraceBuffer`
- `site.acipcImage`
- `site.shmemInfo`
- `2`
- `AppleConvergedIPCRingIndex`
- `td_ring`
- `time`
- `1111111`
- `Raw`
- `kACIPCDeviceWakeTimeout`
- `21222`
- `CoreInfo`
- `recovery`
- `(host sleep)`
- `site.IOACIPCRTIIOTableAtomic *`
- `IOAppleConvergedIPCControl::start: super failed\n`
- `kACIPCTransferCompletionCodeInvalid`
- `kACIPCEventUnexpectedCompletionType`
- `12112111122121`
- `kACIPCLinkBWNotification`
- `AppleConvergedIPCFooterSize`
- `context`
- `AppleConvergedIPCHeaderSize`
- `site.IOAppleConvergedIPCIOCommand`
- `acipc-trace-max-buffer-size`
- `initWithTask`
- `2112111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111112`
- `ACIPCControl`
- `\"assertion failed\" @%s:%d`
- `trace-codes`
- `2222222122122212222111111`
- `IOAppleConvergedIPCDebug::start failed\n`
- `memory_pool`
- `IOPlatformExpertDevice`
- `site.IOAppleConvergedIPCTraceBackend`
- `site.IOAppleConvergedIPCIOCommandPool`
- `TraceBufferQueueOffsetOfKernelBuffer`
- `IOUserClientClass`
- `protocol`
- `site.IOAppleConvergedIPCRTIContext*`
- `IOACIPCPort`
- `Filename`
- `site.IOAppleConvergedIPCTraceBufferQueue *`
- `head_size`
- `BTIDevice`
- `device_wake_dead_time`
- `121121222111`
- `IOAppleConvergedIPCTraceUserClient.cpp`
- `site.msgInfo`
- `%s::%s:client lacks access entitlement\n`
- `site.AsyncEvent`
- `tr_low`
- `site.IOAppleConvergedIPCKernelTraceBuffer`
- `disabled`
- `kACIPCTransferCompletionCodeUndefined`
- `21`
- `num_CRs`
- `IOACIPCRTIContext.cpp`
- `site.acipcPortAction`
- `nonce`
- `kACIPCTransferCompletionUnregisteredChannel`
- `kACIPCTLPCompletionTimeout`
- `oc`
- `IOAppleConvergedIPCMemoryPolicy.cpp`
- `kACIPCTransferCompletionCodeUnknown`
- `CodeLocation`
- `<plist version=\"1.0\">`
- `pci-l1pm-control-postrom`
- `pipes`
- `AppleConvergedIPCClientData`
- `num_contexts`
- `bootstage`
- `IOAppleConvergedIPCTransferRing`
- `sharedinterface`
- `error`
- `site.acipcRTISharedMemoryRegion`
- `auto_open`
- `IOAppleConvergedIPCControl::start: failed to allocate workloop\n`
- `<array>`
- `IOPlatformMapperPresent`
- `IOACIPCDebugUserClient::initWithTask: Client lacks entitlement\n`
- `TraceBufferQueueOffsetOfActiveBuffer`
- `site.OSAsyncReference64`
- `site.IOAppleConvergedIPCMessageQueueBase::MessageQueueEntry`
- `alignment`
- `disable`
- `site.IOAppleConvergedIPCControl`
- `acc_mod_time`
- `IOACIPCRTIPipe.cpp`
- `kACIPCMessageRingFull`
- `21211`
- `site.hdr_ty.IOACIPCTagEntry`
- `model`
- `ooo`
- `site.IOACIPCRTIPipe`
- `async event allocation failed\n`
- `create`
- `site.IOAppleConvergedIPCMemoryPolicyQueue`
- `<key>TraceCodeSize</key>`
- `IOAppleConvergedIPCTraceBackend.cpp`
- `IOACIPCTagList.cpp`
- `IOAppleConvergedPCI`
- `IOAppleConvergedPCI.cpp`
- `AppleConvergedIPCMSIIndex`
- `acipc-aer`
- `IOAppleConvergedIPCCallee`
- `2121`
- `IOAppleConvergedIPCControl.cpp`
- `12111121111222122222211221211`
- `site.acipcGroupHashEntry`
- `sync`
- `tr_high`
- `112111`
- `kACIPCTransferCompletionOverflowUnexpected`
- `Size`
- `acipc-disable-config-protect`
- `site.acipcRTINotificationMSICtx`
- `1211111212221212112111111111111111222221111111112212`
- `kACIPCEnterLowPowerTimeout`
- `kACIPCDirectionOut`
- `site.asyncCallbackInfo`
- `com.apple.driver.IOAppleConvergedIPCDebug.user-access`
- `PoolArrayOffsetOfCount`
- `site.DebugServiceWrapper`
- `After publish`
- `Debug servicequeue empty; return\n`
- `IOAppleConvergedIPCBTIDevice::initWithInfo: super::init failed\n`
- `site.acipcRTICRParams *`
- `11111`
- `site.IOACIPCRTIIOTable<acipcSubIO> *`
- `site.hdr_ty.acipcRTICompletionRing`
- `ipc_version`
- `failed to create ACIPCTrace\n`
- `kACIPCCommandUnexpectedCompletion`
- `1112111111`
- `(active)`
- `(host sleep wait)`
- `IOAppleConvergedIPCRTIInterface::initWithInfo: super::init failed\n`
- `11122211111111111111`
- `i24@?0^^{IOACIPCDescriptor}8^I16`
- `1211111212221212111222222222111111211221212121211111111111112111121111112111111211111121111112111111211111121111112111111111111111111222`
- `acipc-debug`
- `IOAppleConvergedIPCRTISharedInterface.cpp`
- `AppleConvergedIPCTrace`
- `site.signalingInfo`
- `1211111212221212111222222222112111111111121121111111111212111122`
- `kACIPCDARTError`
- `IOAppleConvergedIPCIOCommand`
- `CodeRegistryOffsetOf`
- `1112121111111`
- `kACIPCContextCloseFailed`
- `211111`
- `global`
- `site.acipcRTICRParams`
- `IOACIPCBTIDevice.cpp`
- `site.IOAppleConvergedIPCMemoryPolicy`
- `kACIPCLinkStateUnpoweredUp`
- `site.IOACIPCBTIPipe`
- `Attachments`
- `\"IOAppleConvergedIPCTraceBackend message queue congested\" @%s:%d`
- `AppleConvergedIPCContextIndex`
- `IOAppleConvergedIPCControlUserClient`
- `kACIPCContextOpenFailed`
- `IOAppleConvergedIPCTraceBackend%s`
- `site.acipcRTIMemoryEventCall`
- `acipc-trace-min-buffer-size`
- `priority`
- `_AppleConvergedIPCMemoryDescriptorHelper`
- `kACIPCSleepMessageCompletionFailed`
- `221111111`
- `1211111212221212111222222222`
- `kACIPCTransferCompletionEndUnexpected`
- `site.acipcRTIMSITarget`
- `Scratch Buffer too small`
- `IOAppleConvergedIPCUserClient.cpp`
- `site.IOACIPCUserClientAsyncParamBlock`
- `site.IOACIPCBTIDevice`
- `11122112211111211111111112`
- `IOAppleConvergedIPCTraceBuffer`
- `site.ringInfo`
- `acipc-slowlu-panic`
- `IOACIPCDebugUserClient`
- `IOAppleConvergedIPCUserClient`
- `ACIPCDeviceExceptionProtocol`
- `site.signalingInfoHead`
- `12221`
- `enabled`
- `kACIPCAERCorrectableError`
- `12111112122212121211212111121111111111111111111111111111111111111111111111111111111111111111111122222222222222222222`
- `v20@?0S8^{IOACIPCTagEntry=(?={?=SS}I)III^v^v}12`
- `site.IOAppleConvergedIPCMessageQueueBase`
- `</plist>`
- `num_pipes_primary_context`
- `Sim`
- `ACIPCBTIPipe`
- `1212`
- `direction`
- `IOAppleConvergedIPCPool`
- `212221111111`
- `site.ioStagingEntry`
- `1211111212221212111111111111111121`
- `kACIPCHostConfigError`
- `acipc-devicewaketime-ms`
- `log_binary`
- `12111112122212121112222222221211`
- `site.IOACIPCPort`
- `IOAppleConvergedIPCRTIContext`
- `site.IOAppleConvergedIPCRing`
- `v12@?0I8`
- `shared`
- `site.IOAppleConvergedPCI`
- `site.IOACIPCRTIIOTableInstType`
- `cr_high`
- `group`
- `IOAppleConvergedIPCMemoryPolicy`
- `kACIPCChannelResetFailed`
- `site.IOAppleConvergedIPCTraceBackendRaw`
- `121111121222121211111111111112211122122122122122122122122122122122122122`
- `threshold`
- `12212`
- `in_place`
- `IOAppleConvergedIPCRTIDevice.cpp`
- `site.acipcPortActionQueue`
- `\"ACIPCTrace Backend already loaded.\" @%s:%d`
- `22111111`
- `doorbell`
- `1111211`
- `121111121222121211122222222211111112111`
- `IOPMResetPowerStateOnWake`
- `site.acipcRTIMessage`
- `ACIPCInterfaceUnit`
- `site.IOACIPCDescriptor *`
- `IOAppleConvergedIPCDebug.cpp`
- `IOAppleConvergedIPCRing.cpp`
- `site.IOAppleConvergedIPCTransferRing`
- `121121111221`
- `site.acipcRTITimeEventCall`
- `reliable`
- `acc_mod_bytes`
- `tx_writeback`
- `RTIDevice`
- `site.IOACIPCRTIContext`
- `IOACIPCPort.cpp`
- `site.IOACIPCRTIPipe *`
- `dead`
- `closed`
- `kACIPCInvalidAsyncCDType`
- `kACIPCDirectionIn`
- `site.IOAppleConvergedIPCCompletionRing`
- `unknown`
- `IOAppleConvergedIPCDebugService`
- `retrieveVMLimits`
- `Name`
- `site.IOAppleConvergedIPCRTIDevice`
- `site.acipcCompletionSignalCall`
- `site.asyncCallEntry`
- `kACIPCTransferCompletionSuccessUnexpected`
- `IOAppleConvergedIPCIOCommandPool`
- `IOAppleConvergedIPCIOCommand.cpp`
- `pci-wake-l1pm-disable`
- `site.IOACIPCTagList`
- `site.acipcRTIMessageQueue`
- `IOACIPCControl.cpp`
- `kACIPCDeviceConfigError`
- `kACIPCAERNonFatalError`
- `TraceBufferOffsetOfHeadPos`
- `AppleConvergedIPCCompletionRingProperties`
- `site.IOAppleConvergedIPCUserClient`
- `kACIPCTransferCompletionUnexpected`
- `ACIPCTrace: unable to create logging pipe (%s)\n`
- `doorbell_index_mode`
- `121111121222121212111`
- `kACIPCAERFatalError`
- `IOAppleConvergedIPCDebug`
- `IOAppleConvergedIPCRTIDevice::initWithInfo: super::init failed\n`
- `<?xml version=\"1.0\" encoding=\"UTF-8\"?>`
- `B60@?0Q8i16r^{TraceParam=*Q^v*Q}20r*28^B36^^v44^^{ProbeTable}52`
- `IOAppleConvergedIPCRTIInterface`
- `offset`
- `ACIPCRTIContext`
- `kACIPCCROpenFailed`
- `kACIPCLinkStateHardDown`
- `<dict>`
- `msi`
- `\"_pciBridgePtr %p is not equal to _pciService->getBridge() %p\\n\" @%s:%d`
- `2221111122222222211211111111`
- `1211212121221213221321`
- `1222222222212212222`
- `setting`
- `IOAppleConvergedIPCRTIDevice`
- `RTIInterface`
- `kACIPCChannelStartFailed`
- `acipc-sleeptime-ms`
