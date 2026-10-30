# `com.apple.driver.RTBuddy`

- Name: RTBuddy
- Version: `1.0.0`
- UUID: `4F6C4445-D10C-30D9-B182-A8E24DE161F2`
- Source version: `778.40.12.0.0`
- Depends on: [`com.apple.driver.AppleA7IOP`](com.apple.driver.AppleA7IOP.md) 1.0, [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.iokit.CoreAnalyticsFamily`](com.apple.iokit.CoreAnalyticsFamily.md) 1.0, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0, [`com.apple.kec.corecrypto`](com.apple.kec.corecrypto.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (15) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) | `RTBuddy` | `iop-nub,rtbuddy-v2` |
| [`/arm-io/aop2/iop-aop2-nub`](../devicetree/root__arm-io__aop2__iop-aop2-nub.md) | `RTBuddy` | `iop-nub,rtbuddy-v2` |
| [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) | `RTBuddy` | `iop-nub,rtbuddy-v2` |
| [`/arm-io/sio/iop-sio-nub`](../devicetree/root__arm-io__sio__iop-sio-nub.md) | `RTBuddy` | `iop-nub,rtbuddy-v2` |
| [`/arm-io/ans/iop-ans-nub`](../devicetree/root__arm-io__ans__iop-ans-nub.md) | `RTBuddy` | `iop-nub,rtbuddy-v2` |
| [`/arm-io/smc/iop-smc-nub`](../devicetree/root__arm-io__smc__iop-smc-nub.md) | `RTBuddy` | `iop-nub,rtbuddy-v2` |
| [`/arm-io/mtp/iop-mtp-nub`](../devicetree/root__arm-io__mtp__iop-mtp-nub.md) | `RTBuddy` | `iop-nub,rtbuddy-v2` |
| [`/arm-io/dcp/iop-dcp-nub`](../devicetree/root__arm-io__dcp__iop-dcp-nub.md) | `RTBuddy` | `iop-nub,rtbuddy-v2` |
| [`/arm-io/dcpsec/iop-dcpsec-nub`](../devicetree/root__arm-io__dcpsec__iop-dcpsec-nub.md) | `RTBuddy` | `iop-nub,rtbuddy-v2` |
| [`/arm-io/dcpext0/iop-dcpext0-nub`](../devicetree/root__arm-io__dcpext0__iop-dcpext0-nub.md) | `RTBuddy` | `iop-nub,rtbuddy-v2` |
| [`/arm-io/ispRtb/iop-isp-nub`](../devicetree/root__arm-io__ispRtb__iop-isp-nub.md) | `RTBuddy` | `iop-nub,rtbuddy-v2` |
| [`/arm-io/ane0/iop-ane0-nub`](../devicetree/root__arm-io__ane0__iop-ane0-nub.md) | `RTBuddy` | `iop-nub,rtbuddy-v2` |
| [`/arm-io/ane1/iop-ane1-nub`](../devicetree/root__arm-io__ane1__iop-ane1-nub.md) | `RTBuddy` | `iop-nub,rtbuddy-v2` |
| [`/arm-io/gfx-asc/iop-gfx-nub`](../devicetree/root__arm-io__gfx-asc__iop-gfx-nub.md) | `RTBuddy` | `iop-nub,rtbuddy-v2` |
| [`/arm-io/gfx1-asc/iop-gfx1-nub`](../devicetree/root__arm-io__gfx1-asc__iop-gfx1-nub.md) | `RTBuddy` | `iop-nub,rtbuddy-v2` |

## IOKit personalities (5) [KC]

### RTBuddy
- `CFBundleIdentifier`: `com.apple.driver.RTBuddy`
- `IOClass`: `RTBuddy`
- `IONameMatch`: `iop-nub,rtbuddy-v2`
- `IOPersonalityPublisher`: `com.apple.driver.RTBuddy`
- `IOProviderClass`: `AppleA7IOPNub`

### RTBuddy64
- `CFBundleIdentifier`: `com.apple.driver.RTBuddy`
- `IOClass`: `RTBuddy64`
- `IONameMatch`: `iop-nub,rtbuddy`
- `IOPersonalityPublisher`: `com.apple.driver.RTBuddy`
- `IOProviderClass`: `AppleA7IOPNub`

### RTBuddyARG
- `CFBundleIdentifier`: `com.apple.driver.RTBuddy`
- `IOClass`: `RTBuddyARG`
- `IONameMatch`: `iop-nub,rtbuddy-arg`
- `IOPersonalityPublisher`: `com.apple.driver.RTBuddy`
- `IOProviderClass`: `AppleA7IOPNub`

### RTBuddyRouteOnly
- `CFBundleIdentifier`: `com.apple.driver.RTBuddy`
- `IOClass`: `RTBuddyRouteOnly`
- `IONameMatch`: `iop-nub,rtbuddy-route-only`
- `IOPersonalityPublisher`: `com.apple.driver.RTBuddy`
- `IOProviderClass`: `AppleA7IOPNub`

### RTBuddyService
- `CFBundleIdentifier`: `com.apple.driver.RTBuddy`
- `IOClass`: `RTBuddyService`
- `IOMatchCategory`: `RTBuddyService`
- `IOPersonalityPublisher`: `com.apple.driver.RTBuddy`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `RTBuddy`


## C++ classes (74) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `RTBKeyObjectPair` | 0x20 |  |
| `RTBuddy` | 0x66a0 | IOSlaveProcessor → IOService → IORegistryEntry |
| `RTBuddy64` | 0x66a0 | RTBuddy → IOSlaveProcessor → IOService → IORegistryEntry |
| `RTBuddyARG` | 0x66a0 | RTBuddy → IOSlaveProcessor → IOService → IORegistryEntry |
| `RTBuddyAscDecoder` | 0x18 | RTBuddyCrashlogSectionDecoder |
| `RTBuddyAutoBKPDecoder` | 0x18 | RTBuddyHexDecoder → RTBuddyCrashlogSectionDecoder |
| `RTBuddyBinaryLogEntryHandler` | 0x10 |  |
| `RTBuddyBinaryLogEntryHandlerMetric` | 0x68 | RTBuddyBinaryLogEntryHandler |
| `RTBuddyBinaryLogEntryHandlerOSLog` | 0x50 | RTBuddyBinaryLogEntryHandler |
| `RTBuddyBinaryLogEntryHandlerSysLog` | 0x20 | RTBuddyBinaryLogEntryHandler |
| `RTBuddyBinaryLogEntryHandlerTraceKit` | 0x68 | RTBuddyBinaryLogEntryHandler |
| `RTBuddyBinaryLogHandler` | 0x50 |  |
| `RTBuddyBinaryLogSourceInfo` | 0x40 |  |
| `RTBuddyBuiltinEndpoint` | 0xa8 | IOService → IORegistryEntry |
| `RTBuddyCL4Coredump` | 0xa0 |  |
| `RTBuddyCallStackDecoder` | 0x18 | RTBuddyCrashlogSectionDecoder |
| `RTBuddyCoprocDrivenCoredump` | 0x868 | RTBuddyCoredump |
| `RTBuddyCoreAnalyticsEndpoint` | 0xd8 | RTBuddyBuiltinEndpoint → IOService → IORegistryEntry |
| `RTBuddyCoredump` | 0x868 |  |
| `RTBuddyCoredumpDecoder` | 0x18 | RTBuddyCrashlogSectionDecoder |
| `RTBuddyCoredumpMap` | 0x30 |  |
| `RTBuddyCoredumpMapEntry` | 0x20 |  |
| `RTBuddyCrashlogDecoder` | 0x90 |  |
| `RTBuddyCrashlogEndpoint` | 0x130 | RTBuddyBuiltinEndpoint → IOService → IORegistryEntry |
| `RTBuddyCrashlogSectionDecoder` | 0x18 |  |
| `RTBuddyEndpoint` | 0xe8 | IOSlaveEndpoint → IOEventSource |
| `RTBuddyEndpointPSEventSource` | 0x50 | IOEventSource |
| `RTBuddyEndpointService` | 0x98 | IOService → IORegistryEntry |
| `RTBuddyEntropyEndpoint` | 0xb8 | RTBuddyBuiltinEndpoint → IOService → IORegistryEntry |
| `RTBuddyFirmware` | 0xe8 | IOSlaveFirmware → IOService → IORegistryEntry |
| `RTBuddyFirmwareBundle` | 0x20 |  |
| `RTBuddyFirmwareService` | 0x98 | IOService → IORegistryEntry |
| `RTBuddyHeapDecoder` | 0x18 | RTBuddyCrashlogSectionDecoder |
| `RTBuddyHexDecoder` | 0x18 | RTBuddyCrashlogSectionDecoder |
| `RTBuddyIOReportingEndpoint` | 0xf8 | RTBuddyBuiltinEndpoint → IOService → IORegistryEntry |
| `RTBuddyKdebugEndpoint` | 0x138 | RTBuddyEndpoint → IOSlaveEndpoint → IOEventSource |
| `RTBuddyMailboxDecoder` | 0x18 | RTBuddyCrashlogSectionDecoder |
| `RTBuddyManagementEndpoint` | 0x138 | RTBuddyEndpoint → IOSlaveEndpoint → IOEventSource |
| `RTBuddyNativeSlaveMemoryDescriptor` | 0x28 | IOSlaveMemory |
| `RTBuddyNvramDecoder` | 0x18 | RTBuddyCrashlogSectionDecoder |
| `RTBuddyOSLogEndpoint` | 0x3d0 | RTBuddyEndpoint → IOSlaveEndpoint → IOEventSource |
| `RTBuddyOSLogSegmentSlice` | 0x30 | RTBuddySegmentSlice |
| `RTBuddyPatchBay` | 0x20 |  |
| `RTBuddyProductVersionDecoder` | 0x18 | RTBuddyCrashlogSectionDecoder |
| `RTBuddyRegisterFrameDecoder` | 0x58 | RTBuddyCrashlogSectionDecoder |
| `RTBuddyRemoteSlaveMemoryDescriptor` | 0x30 | RTBuddySlaveMemoryDescriptor → RTBuddySlaveMemory |
| `RTBuddyRoute` | 0x10 |  |
| `RTBuddyRouteAdaptor` | 0x18 | RTBuddyRoute |
| `RTBuddyRouteOnly` | 0x66a0 | RTBuddy → IOSlaveProcessor → IOService → IORegistryEntry |
| `RTBuddyRouteProvider` | 0x88 | IOService → IORegistryEntry |
| `RTBuddyRtkitDecoder` | 0x18 | RTBuddyCrashlogSectionDecoder |
| `RTBuddySavedSegment` | 0x30 |  |
| `RTBuddyScmDecoder` | 0x18 | RTBuddyCrashlogSectionDecoder |
| `RTBuddySegment` | 0x48 |  |
| `RTBuddySegmentSlice` | 0x20 |  |
| `RTBuddyService` | 0xa8 | IOService → IORegistryEntry |
| `RTBuddySlaveBuffer` | 0x20 | RTBuddySlaveMemory |
| `RTBuddySlaveMemory` | 0x10 |  |
| `RTBuddySlaveMemoryBuffer` | 0x38 | IOSlaveMemoryBuffer → IOSlaveMemory |
| `RTBuddySlaveMemoryDescriptor` | 0x20 | RTBuddySlaveMemory |
| `RTBuddySmbDecoder` | 0x18 | RTBuddyCrashlogSectionDecoder |
| `RTBuddyStatisticsDecoder` | 0x18 | RTBuddyCrashlogSectionDecoder |
| `RTBuddyStringDecoder` | 0x18 | RTBuddyCrashlogSectionDecoder |
| `RTBuddySymbolsDecoder` | 0x18 | RTBuddyCrashlogSectionDecoder |
| `RTBuddySyslogEndpoint` | 0x1b8 | RTBuddyEndpoint → IOSlaveEndpoint → IOEventSource |
| `RTBuddyTimeDecoder` | 0x18 | RTBuddyCrashlogSectionDecoder |
| `RTBuddyTraceKitEndpoint` | 0xd8 | RTBuddyBuiltinEndpoint → IOService → IORegistryEntry |
| `RTBuddyTraceKitSession` | 0x68 |  |
| `RTBuddyUnknownDecoder` | 0x18 | RTBuddyHexDecoder → RTBuddyCrashlogSectionDecoder |
| `RTBuddyUserClient` | 0x110 | IOUserClient → IOService → IORegistryEntry |
| `RTBuddyVersionDecoder` | 0x18 | RTBuddyCrashlogSectionDecoder |
| `RTBuddyVisibleMemory` | 0x10 |  |
| `RTBuddyVisibleMemoryImpl` | 0x30 | RTBuddyVisibleMemory |
| `RTBuddyVisibleSlaveBuffer` | 0x28 | RTBuddySlaveMemory |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000c258 off=0x00b9a640-0x00ba6898 addr=0xfffffe0007b9e640-0xfffffe0007baa898 r--/r--   __TEXT            
	sz=0x0000aa16 off=0x00b9ad58-0x00ba576e addr=0xfffffe0007b9ed58-0xfffffe0007ba976e               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000e93 off=0x00ba576e-0x00ba6601 addr=0xfffffe0007ba976e-0xfffffe0007baa601               __TEXT.__os_log           
	sz=0x00000288 off=0x00ba6610-0x00ba6898 addr=0xfffffe0007baa610-0xfffffe0007baa898               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00046428 off=0x03908de0-0x0394f208 addr=0xfffffe000a90cde0-0xfffffe000a953208 r-x/r-x   __TEXT_EXEC       
	sz=0x000458e8 off=0x03908de0-0x0394e6c8 addr=0xfffffe000a90cde0-0xfffffe000a9526c8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000b40 off=0x0394e6c8-0x0394f208 addr=0xfffffe000a9526c8-0xfffffe000a953208          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000cc0 off=0x04a1f440-0x04a20100 addr=0xfffffe000ba23440-0xfffffe000ba24100 rw-/rw-   __DATA            
	sz=0x00000128 off=0x04a1f440-0x04a1f568 addr=0xfffffe000ba23440-0xfffffe000ba23568               __DATA.__data             
	sz=0x00000b98 off=0x00000000-0x00000b98 addr=0xfffffe000ba23568-0xfffffe000ba24100               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x0000de60 off=0x01489c08-0x01497a68 addr=0xfffffe000848dc08-0xfffffe000849ba68 rw-/rw-   __DATA_CONST      
	sz=0x00000140 off=0x01489c08-0x01489d48 addr=0xfffffe000848dc08-0xfffffe000848dd48         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000140 off=0x01489d48-0x01489e88 addr=0xfffffe000848dd48-0xfffffe000848de88         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x0000bea0 off=0x01489e88-0x01495d28 addr=0xfffffe000848de88-0xfffffe0008499d28         __DATA_CONST.__const            
	sz=0x00001380 off=0x01495d28-0x014970a8 addr=0xfffffe0008499d28-0xfffffe000849b0a8         __DATA_CONST.__kalloc_type      
	sz=0x000001a4 off=0x014970a8-0x0149724c addr=0xfffffe000849b0a8-0xfffffe000849b24c         __DATA_CONST.__assert           
	sz=0x000000f0 off=0x01497250-0x01497340 addr=0xfffffe000849b250-0xfffffe000849b340         __DATA_CONST.__kalloc_var       
	sz=0x000005a0 off=0x01497340-0x014978e0 addr=0xfffffe000849b340-0xfffffe000849b8e0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000188 off=0x014978e0-0x01497a68 addr=0xfffffe000849b8e0-0xfffffe000849ba68         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 409 at 0x04afcfb8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     4F6C4445-D10C-30D9-B182-A8E24DE161F2
008: LC_SOURCE_VERSION           778.40.12.0.0
009: LC_FUNCTION_STARTS          offset=0x004acb758 size=0xc28
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `RTBuddy`
- `CFBundleGetInfoString`: `Copyright © 2014-2023 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.RTBuddy`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `RTBuddy`
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
- `NSHumanReadableCopyright`: `Copyright © 2014-2023 Apple. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/RTBuddy.kext`
- `_PrelinkExecutableLoadAddr`: `-2198893631936`
- `_PrelinkExecutableRelativePath`: `RTBuddy`
- `_PrelinkExecutableSize`: `397728`
- `_PrelinkExecutableSourceAddr`: `-2198893631936`
- `_PrelinkKmodInfo`: `-2198828075968`

## Strings (1168) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `error: fp is invalid => possible stack corruption`
- `Translation table walk synchronous external abort (2nd level)`
- `entropy`
- `_rtbuddy->getWorkLoop()->inGate()`
- `powerOff() == kIOReturnSuccess`
- `kIOReturnSuccess == _processor->getWorkLoop()->addEventSource(_watchdogTimer)`
- `indexOfVirt`
- `site.RTBuddyTimeDecoder`
- ` ASC L2C %s bit error l2c_err_sts %#018llx, l2c_err_adr %#018llx, l2c_err_inf %#018llx,`
- `IOMemoryMap *RTBuddyCoredumpMap::readwriteMapForIopVirtual(IOVirtualAddress, IOVirtualAddress *)`
- `\"RTBuddy(%s)::%s \" \"message %llx for unknown endpoint %d\" \"\\n%s\" @%s:%d`
- `watchdog-enable`
- `index >= MBI_ENDPOINT_FIRST_USER`
- `RTBuddyCoredump`
- `_handleNewCoalescerRequest`
- ` - %s(%lu)`
- `RTBuddy(%s)::%s: 'crashlog-region' data invalid: %p:%p\n`
- `coredump-active-only`
- `DATA ABORT`
- `_handleRequestSyslogBuffer`
- `site.RTBuddySegmentSlice`
- `12111112122212121111111111111211111122`
- `kRtbIopStatusVersionOk == _processor->getIopStatus()`
- `%sASC MMU error, `
- `IODTNVRAM`
- `Illegal Execution State`
- `%s coredump: invalid coredump server version: %llu\n`
- `%s coredump: failed to count pages. error = %s\n`
- `nullptr != _epCrashlog`
- `_builtinEntryHandlers`
- `void RTBuddyTraceKitEndpoint::_setEndpointActiveGated(bool)`
- `OUTBOX not ready `
- `RTBuddyHeapDecoder`
- `site.RTBuddyNvramDecoder`
- `Asynchronous external abort`
- `site.RTBuddyUserClient`
- `            ... IOP only coredumps when it panics.\n`
- `IOReturn RTBuddyKdebugEndpoint::_kdebugSendFlushRequest()`
- `IOReturn RTBuddyTraceKitEndpoint::_configureGated(rtbuddy_trace_config_t, OSSharedPtr<RTBuddyTraceKitSession> &)`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `OSBoundedPtr.h`
- `attachCoreAnalyticsService`
- `RTBuddyUserClient`
- `Data Abort taken without a change in Exception level`
- `endpoints`
- `rtb_syslog_verbosity`
- `1222121121`
- `  Faulting pc=0x%08x`
- `Outbox overflow `
- `RTBuddyCoredumpDecoder`
- `site.RTBuddyCoredumpMap`
- `restoreSRAM`
- `Stack guard fault`
- `Instruction Abort from a lower Exception level`
- `Synchronous external abort on translation table walk`
- `kIOReturnSuccess == getWorkLoop()->removeEventSource(ep)`
- `_createReporters`
- `IOReturn RTBuddyManagementEndpoint::_handlePowerAck(mbi_msg_t)`
- `Non-fatal crashlog`
- `_waitForOutstandingRequestsGated`
- `_OSLogRegisteredSourceInfosLock`
- `site.RTBuddyBinaryLogEntryHandlerSysLog`
- `Inbox overflow `
- ` Outbox%d overflow`
- `Permission fault (page)`
- `121221212`
- `_signalNmi`
- `%s NMI: %s\n%s`
- `forceCrashlog`
- `_setStandaloneStateGated`
- `nullptr != service`
- `copySegmentDescriptorWithName`
- `_handleHello`
- `_kdebugSendEnabledState`
- `virtual void RTBuddyTraceKitEndpoint::kdebugCallback(kd_callback_type, void *)`
- `attach_block_invoke`
- `CoreAnalyticsHub`
- `site.RTBuddyRouteAdaptor`
- `getSegmentForIopVirtual`
- `client5`
- `bool RTBuddyBuiltinEndpoint::initWithOptions(IOSlaveProcessor *, IOSlaveEndpoint::Action, void *, uint32_t, const char *, unsigned int)`
- `site.RTBKeyObjectPair`
- `unique-chip-id`
- `RTBuddy`
- `Recoverable Panic`
- `oslog-slices`
- `_setRole`
- `NVRAM section skipped due to AP preemption being disabled (panic or hibernation)\n`
- `Floating-point exception`
- `region-size`
- `Force Reset`
- `void RTBuddyEntropyEndpoint::_handleEntropyRequest(mbi_msg_t)`
- `12111211111121111211221111121212211122111221112211122111221112211122111221112211122111221112211122111221112211222121121111`
- `_setPowerStateGuardExitGated`
- `RTBuddyService`
- `Failed to quiesce watchdog in %ds`
- ` far=0x%08x`
- `virtual IOReturn RTBuddy::loadFirmware(RTBuddyFirmware *)`
- `client2`
- `site.RTBuddyBuiltinEndpoint`
- `Failed to create NVRAM key '%s'\n`
- `Implementation defined (Coprocessor abort)`
- `disable`
- `RTBuddy(%s): %s%s%s\n`
- `SUSPENDED `
- `Build: %s\n`
- `RTBuddyVisibleSlaveBuffer`
- `RTBuddySlaveMemoryDescriptor`
- `RTBuddy(%s): start(%p) - (%s@%s)\n`
- `_copyBuffer`
- `site.RTBuddyCoredump`
- `(nullptr == _tempSourceInfo) && (0 == _roleSize) && !_uuidValid && coalescerBufferValid(_coalescers[id])`
- `!os_add3_overflow(offset, sizeof(core_analytics_event_t), event->data_size, &size_needed)`
- `mapFirmware`
- `Crash with invalid header signature: 0x%x, should be 0x%x\n`
- `IOReturn RTBuddyKdebugEndpoint::_kdebugSendEnabledState()`
- `%s_%s`
- `RTBuddyDictionaryDecoder.cpp`
- `void RTBuddyKdebugEndpoint::_handleFlush(mbi_msg_t)`
- `Permission fault`
- `_iopStatus = %#x\n`
- `RTBuddySymbolsDecoder`
- `Access to SIMD or floating-point registers`
- `nullptr != (_legend = IOReportLegend::with(nullptr))`
- `\"RTBuddy(%s)::%s \" \"invalid reporter type (%d) for reporter %s (0x%llx)\" \"\\n%s\" @%s:%d`
- `_validDimensions && !os_mul_overflow(_maxEntries, _maxEntrySize(), &required_buffer_size) && (required_buffer_size <= _bufferSize)`
- `RTBuddy(%s)::%s: Unimplemented kdebug command: %x\n`
- `Unable to add frame to coredump for %s. %u bytes\n`
- `failed to receive idle message`
- `_getReporter`
- `nullptr != (rep = OSDynamicCast(RTBKeyObjectPair, _reporters->getObject(i)))`
- `site.RTBuddyTraceKitSession`
- `\"%s:%u: Single segment mapping does not cover entire memory descriptor.\" @%s:%d`
- `Access flag fault`
- `index >= MBI_ENDPOINT_NUM_BUILT_IN`
- `writeBackPatchBay`
- `_multiCrashlogFindFirstCrash`
- `OS Version: `
- `Alignment fault`
- `bool RTBuddy::_foundFirmwareService(void *, IOService *, IONotifier *)`
- `no-shutdown`
- `\"RTBuddy(%s)::%s \" \"Unable to restore SRAM contents\" \"\\n%s\" @%s:%d`
- `role`
- `_apInitiatedUpdateGated`
- `  mcnt : 0x%08x\n`
- `management`
- `endpointForHandle`
- `Incomplete crash log, IOP crashed during logging (%x)\n`
- `void RTBuddyKdebugEndpoint::_handleHereIsMyBuffer(mbi_msg_t)`
- `IOReturn RTBuddyTraceKitEndpoint::releaseChunkCPUTrace(rtbuddy_cputrace_chunk_t)_block_invoke`
- `site.RTBuddyCoprocDrivenCoredump`
- `_kdebugCoreID = kdebug_register_coproc(_iopRole->getCStringNoCopy(), _continuousTimestamps ? KDCP_CONTINUOUS_TIME : (kdebug_coproc_flags_t)0, OSMemberFunctionCast(kd_callback_fn, this, &RTBuddy::_kdebugCallback), this )`
- `stand-alone`
- `1212121`
- `_builtinEntryHandlers[kTraceKitHandlerIndex]`
- `void RTBuddyOSLogEndpoint::_handleNewCoalescerRequest(const mbi_msg_t)`
- `site.RTBuddy`
- `!should_block || !getWorkLoop()->inGate()`
- `reboot-firmware`
- `names.empty()`
- `iop != nullptr`
- `_enableGated`
- `_handleEntropyRequest`
- `\"RTBuddy(%s)::%s \" \"failed to start (%x)\" \"\\n%s\" @%s:%d`
- `%sEndpoint%u`
- `%s(%d)`
- ` [truncated]`
- `  fpexc=0x%08x  fpscr=0x%08x`
- `ok`
- `_powerStateChangeLocked = %s\n`
- `            ... crashlog endpoint was not found.\n`
- `_handleSourceInfoRole`
- `user%02d`
- `virtual IOReturn RTBuddy::_setPowerStatePerformChangeGated(const RTBuddyPowerState *, const bool *)`
- `IOReporter *RTBuddyIOReportingEndpoint::_addReporter(const io_reporting_reporter_t &, OSBoundedPtr<const uint8_t>)`
- `_builtinEntryHandlers[kOSLogHandlerIndex]`
- `%s coredump: failed to save segment description. error = %s\n`
- `virtual IOSlaveEndpoint *RTBuddy::endpointForHandle(OSObject *, IOSlaveEndpoint::Action, UInt32, void *)`
- `saveSRAM`
- `%s:%d Assertion failed: %s : RTBuddyEndpointService doesn't work with built-in endpoints: %u\n`
- `RTBuddyCrashlogDecoder.cpp`
- `client8`
- `nullptr != endpoint`
- `coredump-dependency`
- `RTBuddyPatchBay.h`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `12111`
- `IOReturn RTBuddyIOReportingEndpoint::_updateRemoteReportersGated()`
- `Unknown exception`
- `unsigned int RTBuddySyslogEndpoint::_maxEntrySize() const`
- `true`
- `bool RTBuddyCoredump::initWithOptions(RTBuddy *, RTBuddyCoredumpArch)`
- `kern`
- `\"%s\" @%s:%d`
- `[TX]`
- `RTBuddyARG`
- `takeBackupBufferAssertion`
- `1211111212221212111111111111212211`
- `_coalescers[id].buffer != nullptr`
- `%s%s`
- `Synchronous parity error on memory access`
- `RTBuddyFirmwareService`
- `site.RTBuddyMailboxDecoder`
- `aot-power-wake-reason`
- `  pc=%#010x  fsr=%#010x (%s)  far=%#010x `
- `truncated `
- `RTBuddyMessageQueue.cpp`
- `\"RTBuddy(%s)::%s \" \"Invalid Pstate passed: %d\" \"\\n%s\" @%s:%d`
- `site.RTBuddyARG`
- `Proxy Host Log`
- `_rtb->getWorkLoop()->inGate()`
- `INBOX not ready `
- `Unknow reason`
- `NULL != (_akfNub = OSDynamicCast(AppleA7IOPNub, provider))`
- `!getWorkLoop()->inGate()`
- `!_didBackupSRAM`
- `RTBuddyVisibleMemory`
- `nullptr != (_reporterPowerState = IOStateReporter::with(this, kIOReportCategoryPower, kRtbNumPowerStates))`
- `clog-str-buff-size`
- `void RTBuddySyslogEndpoint::_handleDimensions(mbi_msg_t)`
- `_flushGated`
- `RTBuddyProductVersionDecoder`
- `virtual IOReturn RTBuddy::_setPowerStateGuardEntryGated(const RTBuddyPowerState *, const bool *)`
- `rtb_timeout`
- `RTBuddyRtkitDecoder`
- `double`
- `RTBuddyRouteAdaptor`
- `result == kIOReturnSuccess`
- `121111121222121211111`
- `\"RTBuddy(%s)::%s \" \"Invalid pinger sequence number received: 0x%x (timestamp 0x%x), expected 0x%x\" \"\\n%s\" @%s:%d`
- `sendMessage(&resp) == kIOReturnSuccess`
- `\"RTBuddy(%s)::%s \" \"remote-only must be defined for RTBuddyARG\" \"\\n%s\" @%s:%d`
- `rtb_force_dram`
- `site.RTBuddyMessageQueue`
- `IOReturn RTBuddyCrashlogDecoder::decodeLog(RTBuddyCrashlogDecodeResult &)`
- `RTBuddyUserClient::registerNotificationPort (0x%x)\n`
- `client1`
- `\"RTBuddy(%s)::%s \" \"Invalid tracekit command %x (%llx)\" \"\\n%s\" @%s:%d`
- `Access Flag fault (section)`
- `_registerKdebug`
- `kIOReturnSuccess == getWorkLoop()->addEventSource(_endpointPSEventSource)`
- `%s: Force non-fatal crashlog`
- `\"Assertion failed: \" \"0\" @%s:%d`
- `\"Assertion failed: \" \"_layoutLock.has_value()\" @%s:%d`
- `_handleSourceInfoUUID`
- `SMB Registers: %s\n`
- `Syslog`
- `Data Abort from a lower Exception level`
- `buffer`
- `_allocateLocalBuffer`
- `\"RTBuddy(%s)::%s \" \"Incompatible protocol version: %s=[%x,%x] kext=%x\" \"\\n%s\" @%s:%d`
- `site.RTBuddyRegisterFrameDecoder`
- `Timeout`
- `RTBuddyKdebugEndpoint`
- `RTBuddyCoreAnalyticsEndpoint`
- `false`
- `RTBuddyCrashlogEndpoint`
- `RTBuddySyslogEndpoint`
- `Translation table walk synchronous external abort (1st level)`
- `RTBuddyIOReportingEndpoint.cpp`
- `expected buffer to be release-able`
- `_updateRemoteReportersGated`
- `!_rtb->getWorkLoop()->inGate()`
- `bool RTBuddyManagementEndpoint::_initWithOptions(IOSlaveProcessor *)`
- `_supportsPowerManagement()`
- `\"RTBuddy(%s)::%s \" \"DART provided a 0 DVA\" \"\\n%s\" @%s:%d`
- `_crashlogString`
- `Crash with invalid (short) log length.  Log %u bytes, Minimum valid length is %lu \n`
- `Access Flag fault (page)`
- `i8@?0`
- `asc-dram-mask`
- `exception`
- `  psr=%#08x        cpacr=%#08x           fpsr=%#08x           fpcr=%#08x\n`
- `121111121222121211121111222111112221222222121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `virtual bool RTBuddy::start(IOService *)`
- `SError interrupt`
- `i >= 0`
- `bytes_read == sizeof(CrashLogHeader_t)`
- `IOReturn RTBuddyOSLogEndpoint::_freeOSLogSegment()`
- `AKF_AP_MAILBOX_SET  = 0x%08x\n`
- `Translation fault (page)`
- `_handleEvent`
- `Mailbox Status:\n`
- `NMI requested from RTBuddyTool`
- `Unknown`
- `site.RTBuddyVisibleSlaveBuffer`
- `callPatchbayCallback`
- `nullptr != (_reporters = OSArray::withCapacity(4))`
- `_setEndpointActiveGated`
- `unknown%02d`
- `IOReturn RTBuddy::_setPowerStateGuardExitGated(const RTBuddyPowerState *, const bool *, const bool *)`
- `no-firmware-service`
- `void RTBuddy::releaseBackupBufferAssertion()`
- `copyToTarget`
- `_handleTimeType`
- `\"RTBuddy(%s)::%s \" \"%s:%u: REQUIRE failed: %s\" @%s:%d`
- `_OSLogRegisteredSourceInfos`
- `Unable to add frame to coredump for %s. %zu bytes\n`
- `\"RTBuddy: memcpy_from32 requires 4-byte alignment (src=%p, size=%zu)\" @%s:%d`
- `reporter != nullptr`
- `site.RTBuddyCrashlogEndpoint`
- `setCrashlogBufferAddress`
- `            ... crashlog buffer was not available.\n`
- `Unknown register section with 0x%zx bytes data\n`
- `virtual IOReturn RTBuddy64::sendMessage(UInt32, void *, void *, bool)`
- `site.RTBuddySlaveMemoryBuffer`
- `RTBuddyManagementEndpoint`
- `_hostVersionGated`
- `TLB conflict abort`
- `RTBuddyCoredumpMap.cpp`
- `RTBuddyRouteProviderKey`
- `RTBuddyBinaryLogHandler.cpp`
- `RTBuddyBinaryLogSourceInfo`
- `site.RTBuddyBinaryLogEntryHandlerMetric`
- `NVRAM value string [%s]:[%s]\n`
- `Oct 13 2026`
- `_setPowerStateGuardEntryGated`
- `%s queue overflow for %s endpoint (id=%d, queue size=%u)\n%s`
- `%s NMI: %s`
- `coprocessor`
- `RTBuddySegment *RTBuddyFirmware::getSegmentForIopVirtual(IOVirtualAddress)`
- `bool RTBuddyVisibleMemoryImpl::initWithMemoryDescriptor(IOMemoryDescriptor *, RTBuddyCoredumpMap *, IOMapper *, IOPhysicalAddress, uint8_t)`
- `virtual IOReturn RTBuddy::_slaveMemoryFromIOPPhysGated(const IOPhysicalAddress *, const IOByteCount *, RTBuddySlaveMemory **)`
- `\"RTBuddy(%s)::%s \" \"sleep-on-hibernate applies only to IOPs that are not power-managed or user-power-managed\" \"\\n%s\" @%s:%d`
- `site.RTBuddyBinaryLogSourceInfo`
- `ACIPC-perf`
- `(!_rtb->hibernateReuseMappings() || cmdType == CRASHLOG_BUFFER)`
- `void RTBuddyFirmware::writeBackPatchBay()`
- `PANIC`
- `\"Unabled to attach route: %p\\n\" @%s:%d`
- `site.RTBuddyIOReportingEndpoint`
- `releaseFirmware`
- `_waitForBusyACKGated`
- ` - pc=0x%08x`
- `nullptr != (obj = RTBKeyObjectPair::withOptions (reporter.id, state))`
- `site.RTBuddyBinaryLogEntryHandler`
- `void RTBuddyIOReportingEndpoint::_messageHandler(void *, void *)`
- `void RTBuddyCrashlogDecoder::writeCrashlog(const char *, va_list)`
- `RTBuddyBuiltinEndpoint`
- `[RX]`
- `ASC FED error, `
- `void RTBuddy::_changePowerState(RTBuddyPowerState, bool)`
- `ep %s - unknown reason`
- `_builtinEntryHandlers[kSysLogHandlerIndex]`
- `void RTBuddyTraceKitEndpoint::_waitForStateTransitionsGated()`
- `site.RTBuddySavedSegment`
- `data->getLength() == sizeof(T)`
- `site.RTBuddySymbolsDecoder`
- `Stack check fault`
- `_validDimensions`
- `_resetGated`
- `_addReporter`
- `_builtinEntryHandlers == nullptr`
- `\"Assertion failed: \" \"blob\" @%s:%d`
- `_registerSourceInfo`
- `site.RTBuddyStringDecoder`
- ` OUTBOX%d not ready`
- `double and single`
- `RTBuddyCoreAnalyticsEndpoint.cpp`
- `remoteReporter.num_elem <= 256`
- `oslog`
- `\nFaulting task %3u Call Stack:`
- `bool RTBuddyIOReportingEndpoint::_initWithOptions(IOSlaveProcessor *)`
- `site.RTBuddyBinaryLogHandler`
- `site.RTBuddyEntropyEndpoint`
- `com.apple.rtbuddy.%s`
- `\n!UUID: %s\n`
- `\"RTBuddy(%s)::%s \" \"power-managed and user-power-managed are mutually exclusive device tree flags\" \"\\n%s\" @%s:%d`
- `Unhandled SWI`
- `site.RTBuddyUnknownDecoder`
- `single`
- `site.RTBuddyCL4Coredump`
- `121222`
- `pre-loaded`
- `NULL != _watchdogTimer`
- `_session == nullptr`
- `Section size error.  Crashlog section header (%zu bytes) larger than remaining buffer (%llu bytes)`
- `HARDFAULT`
- `UNKNOWN`
- `The offset of the pointer inside its valid memory range can't be represented using int32_t`
- `%2lu %-23s | %03d%s | %5llu/%-5llu | %s | %#llx | `
- ` Inbox%d underflow`
- `Not supported`
- `_panicString && _crashlogString`
- `RTBuddyBinaryLogEntryHandlerSysLog`
- ` far_physical=%#018llx`
- `size < UINT32_MAX`
- `_onPowerStateGated`
- `void RTBuddySyslogEndpoint::_messageHandler(void *, void *)`
- `IOReturn RTBuddyBinaryLogHandler::addEntryHandler(RTBuddyBinaryLogEntryHandler *)`
- `running`
- ` - Recoverable`
- `\"RTBuddy(%s)::%s \" \"Invalid oslog command %x\" \"\\n%s\" @%s:%d`
- `Crashlog decoder for section with signature == %#0x is implemented using a deprecated method: 'RTBuddyCrashlogSectionDecoder::decode(CrashLogSignature_t,uint32_t, void *, size_t)'\n`
- `\"RTBuddy(%s)::%s \" \"invalid IO reporting buffer signature: %x != %x\" \"\\n%s\" @%s:%d`
- `Crash with invalid log length.  Log %u bytes, buffer is %lu \n`
- `RTKit Task List:\n   name                    | pri     | stack use | status     | resource | warning\n`
- `virtual OSArray *RTBuddy::getOSLogSegmentSlices(RTBuddySegment *) const`
- `coredump-rel-privacy-approved`
- `1`
- `rtb`
- `kIOReturnSuccess == _processor->getWorkLoop()->runAction(OSMemberFunctionCast(IOWorkLoop::Action, this, &RTBuddyKdebugEndpoint::_kdebugTypefilterChangedGated), this, arg)`
- `121111121222121211111212121`
- `Instruction Abort taken without a change in Exception level`
- `Debug event`
- `remotefs`
- `com.apple.`
- `void RTBuddy::_signalNmi(RTBuddyNmiType, OSString *, bool, bool)`
- `_iopRole->getLength() >= 3`
- `Memory access asynchronous parity error`
- `_configureGated_block_invoke`
- `error: non-code address`
- `offset < _md->getLength()`
- `RTBuddyEndpoint.cpp`
- `\n    dir   endpoint      timestamp           msg\n    ====  ============  ==================  ==================\n`
- `121111`
- `remote-only`
- `oslog-uuids`
- `_initForwarding`
- `site.RTBuddyEndpointService`
- `RTBuddyOSLogEndpoint`
- ` far=%#018llx`
- `12111112122212121`
- `\"RTBuddy(%s)::%s \" \"mapFirmware is deprecated.\" @%s:%d`
- `[%s:%s] %s%s\n`
- `12221122`
- ` Exception class=%#04x (%s), IL=%u, iss=%#x`
- `%s coredump: iop is not active\n`
- `map`
- ` Outbox%d underflow`
- `site.RTBuddyHeapDecoder`
- `RTBuddyCrashlogSectionDecoder`
- `nullptr != analytics`
- `kIOReturnSuccess == initializePowerManagement(_akf)`
- `%s: send msg=0x%llx error=0x%x`
- `const void *RTBuddyFirmware::iopVirtualToApVirtual(IOVirtualAddress, size_t)`
- `segment`
- `  r00=0x%08x  r01=0x%08x  r02=0x%08x  r03=0x%08x\n  r04=0x%08x  r05=0x%08x  r06=0x%08x  r07=0x%08x\n  r08=0x%08x  r09=0x%08x  r10=0x%08x  r11=0x%08x\n  r12=0x%08x   sp=0x%08x   lr=0x%08x   pc=0x%08x\n  psr=0x%08x`
- `12222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221121222222222222222222222222222222222222222222222222222222222222222222`
- `writePanicString`
- `site.RTBuddyRouteOnly`
- `site.RTBuddyEndpointPSEventSource`
- `_kdebugMemoryDecriptor`
- `site.RTBuddyRemoteSlaveMemoryDescriptor`
- `_buffer != nullptr`
- `  r00=0x%08x r01=0x%08x r02=0x%08x r03=0x%08x\n  r04=0x%08x r05=0x%08x r06=0x%08x r07=0x%08x\n  r08=0x%08x r09=0x%08x r10=0x%08x r11=0x%08x\n  r12=0x%08x  lr=0x%08x  pc=0x%08x sp=0x%08x\n  xpsr=0x%08x exc_ret=0x%08x expt_num=0x%08x pri_masks=0x%08x\n  fsr=0x%08x control=0x%08x extra=0x%08x`
- `\n!!!! Unsupported Crashlog info section version %u.%u !!!!\n`
- `Translation fault`
- `1211111212221212111`
- ` INBOX%d not ready`
- `site.RTBuddyCoreAnalyticsEndpoint`
- `\"RTBuddy(%s)::%s \" \"Failed to validate IOP: status=%x, _iopStatus=%x\" \"\\n%s\" @%s:%d`
- `\"RTBuddy(%s)::%s \" \"dont-power-on is not compatible with power-managed\" \"\\n%s\" @%s:%d`
- `client3`
- `coalescerBufferValid(_coalescers[id])`
- `BLOCKED   `
- `Implementation defined (Lockdown)`
- `RTBuddyCoredumpMapEntry`
- `RTBuddyARG.cpp`
- `IOReportLegendPublic`
- `\"RTBuddy(%s)::%s \" \"%s:%u: REQUIRE failed: %s, %s\" @%s:%d`
- `kIOReturnSuccess == _rtb->getWorkLoop()->runActionBlock(^IOReturn { switch (_state) { case TraceKitState::Unconfigured: return kIOReturnSuccess; case TraceKitState::Configured: case TraceKitState::Started: case TraceKitState::Stopped: break; } if (!_session->config.kdebug_managed) return kIOReturnSu`
- `\n     `
- `site.RTBuddyHexDecoder`
- `Management`
- `site.RTBuddyTraceKitEndpoint`
- ` ASC FED error fed_err_sts %#018llx,`
- `RTBuddySavedSegment`
- `OSArray *RTBuddy::getSegmentMap() const`
- `nclk`
- `ASC LSU error, `
- `IODARTMapper`
- `void RTBuddy::_initForwarding()`
- `mgmt`
- `client4`
- `site.RTBuddySlaveMemory`
- `nullptr != (legend = IOReportLegend::with(nullptr))`
- `_messageHandler`
- `Wrong frame size for %s. Got %u bytes (section), expected %zu or %zu\n`
- `  imask: 0x%08x\n`
- `coredump-copy-buffer`
- `RTBuddySlaveMemory.cpp`
- `rtb_ping_rate`
- `no-hibernate-sleep`
- `UNDEF`
- `RTBuddyMailboxDecoder`
- `kIOReturnSuccess != result || nullptr != _mapper`
- `data->getLength() == (sizeof(uint64_t) * 2)`
- ` - nested %s @ 0x%08llx`
- `crashlog-region`
- `nullptr != entropy`
- `-restore`
- `_commonServiceRegister`
- `IOReturn RTBuddyKdebugEndpoint::_kdebugSendHostReadyAction()`
- `[Faulting task]`
- `site.T`
- `RTBuddyFirmware.cpp`
- `site.RTBuddyBinaryLogEntryHandlerTraceKit`
- `OK`
- `epList`
- `continuous-time`
- `mc`
- `\"RTBuddy(%s)::%s \" \"EDT property '%s' is not supported in RTBuddyARG.\" \"\\n%s\" @%s:%d`
- `\"RTBuddy(%s)::%s \" \"releaseFirmware is deprecated.  Call 'release' instead.\" @%s:%d`
- `\"Assertion failed: \" \"_layoutBuffer\" @%s:%d`
- `\"Assertion failed: \" \"_decodeBuffer\" @%s:%d`
- `RTBKeyObjectPair`
- `void RTBuddy::_registerKdebug()`
- `KERN_SUCCESS == ret || KERN_NOT_SUPPORTED == ret`
- `Release`
- `Mailbox (%d): (%x)\n  Inbox  AKF_KIC_INBOX_CTRL = 0x%08x, AKF_KIC_MAILBOX_SET = 0x%08x\n  Outbox AKF_AP_OUTBOX_CTRL = 0x%08x, `
- `12`
- `\"RTBuddy(%s)::%s \" \"Unable to save SRAM contents\" \"\\n%s\" @%s:%d`
- `_slaveMemoryFromIOPPhysGated`
- `No response to AP power notification in %ds`
- `RTBuddyRouteOnly`
- `RTBuddy(%s)::%s: Unimplemented kernel callback reason: %x\n`
- `size_needed <= caSpan.size()`
- `\nFaulting task stack frame:\n`
- `nullptr != (obj = RTBKeyObjectPair::withOptions (reporter.id, simple))`
- `interrupt`
- `_unconfigureGated`
- `_initWithOptions`
- `RTBuddyVersionDecoder`
- `Invalid architecture`
- `Crashlog`
- `RTBuddyOSLogEndpoint.cpp`
- `RTBuddyVisibleMemoryImpl`
- `backupSegment != nullptr`
- `nullptr != (simple = IOSimpleReporter::with (this, static_cast<IOReportCategories>(reporter.category), reporter.unit))`
- `site.RTBuddyManagementEndpoint`
- `\nAutoBKP Data (size = %zu):\n`
- `epServicesList`
- `idle-msg`
- `void RTBuddy::_commonServiceRegister()`
- `_resetGated() == kIOReturnSuccess`
- `_checkForUnsupportedEDTProperties`
- `RTBuddySegmentSlice`
- `nullptr != _epTraceKit`
- `RTBuddyEntropyEndpoint`
- `void RTBuddyOSLogEndpoint::_handleSourceInfoRegister(const mbi_msg_t)`
- `Domain fault (page)`
- `virtual void RTBuddy::_initConfigEDT()`
- `IOReporter *RTBuddyIOReportingEndpoint::_getReporter(uint64_t)`
- `build`
- `mailbox`
- `1211121111`
- `rtb_cputrace_carveout_mb`
- `region_map`
- `FirmwareUUID`
- `unknown   `
- `RTBuddyPatchBay`
- `setPowerState`
- `configuration`
- `site.RTBuddyOSLogEndpoint`
- ` %#018llx`
- `MSR, MRS, or System instruction execution, that is not reported using EC 0x00, 0x01, or 0x07`
- `forwarded-crashlog`
- `RTBuddy64.cpp`
- `last update`
- `version`
- `_kdebugTypefilter`
- `RTBuddySlaveMemoryDescriptor *RTBuddyCoredumpMap::slaveMemoryForPhysicalRange(IOPhysicalAddress, IOByteCount, IODirection)`
- `\"Variable read size (%ld) does not match patch variable size(%d)\" @%s:%d`
- `_stateIOP == TraceKitState::Configured`
- `panic-priority`
- `crashlog-non-fatal`
- `121221112212212211`
- `RTBuddy(%s)::%s: Kdebug: Illegal request from firmware to change the timestamp timetypemsg=%llx, _continuousTimestamps=%u\n`
- `void RTBuddyCoreAnalyticsEndpoint::_messageHandler(void *, void *)`
- `site.RTBuddyService`
- `RTKitVersion`
- `RTBuddyScmDecoder`
- `12111122222222221111`
- `hibernate-reuse-mappings`
- `getSegmentMap`
- `40A0DDD2-77F8-4392-B4A3-1E7304206516:`
- `RTBuddyEndpoint *RTBuddy::createEndpoint(unsigned int)`
- `user-power-managed`
- `KDebugCoreID`
- `virtual IOReturn RTBuddy::setPowerState(unsigned long, IOService *)`
- `void RTBuddyKdebugEndpoint::_handleBufferRequest(mbi_msg_t)`
- `_state == TraceKitState::Unconfigured`
- `nullptr != _rtb`
- `core-analytics`
- `header`
- `IOReturn RTBuddy::_createReporters()`
- `RTBuddyUserClient.cpp`
- `void RTBuddyTraceKitEndpoint::_waitForOutstandingRequestsGated()`
- `_state == _stateIOP`
- `site.struct logSourceInfo`
- `\n\n`
- `site.RTBuddyCallStackDecoder`
- `mapper-index`
- `void RTBuddyOSLogEndpoint::_handleSourceInfoRole(const mbi_msg_t)`
- `RTBuddyVisibleMemoryImpl.cpp`
- `failed to transition to state %d (_iopStatus=%x)`
- `_checkForCrashGated`
- `\"RTBuddy(%s)::%s \" \"Firmware will not fit in the target memory region.\" \"\\n%s\" @%s:%d`
- `\"RTBuddy(%s)::%s \" \"invalid management message %llx received: %d, status = %x\\n\" \"\\n%s\" @%s:%d`
- `void RTBuddyKdebugEndpoint::_handleHereIsMyTypefilter(mbi_msg_t)`
- `virtual IOReturn RTBuddy::restoreSRAM()`
- `decodeLog`
- `kIOReturnSuccess == _processor->getWorkLoop()->runAction (OSMemberFunctionCast(IOWorkLoop::Action, this, &RTBuddyKdebugEndpoint::_kdebugSendEnabledState), this)`
- `\"RTBuddy(%s)::%s \" \"Failed to attach to CoreAnalyticsHub\" \"\\n%s\" @%s:%d`
- `RTBuddyCoredump.cpp`
- `SERROR`
- `_waitForStateTransitionsGated`
- `121112`
- `void RTBuddy::allocateBackupBuffers()`
- `uuids.empty()`
- `ASLR slide: %s\n`
- `site.RTBuddyAscDecoder`
- `RTBuddyRoute`
- `RTBuddyOSLogSegmentSlice`
- `OSData *RTBuddyFirmware::copy32FromIopVirtual(IOVirtualAddress, size_t)`
- `/chosen`
- `RTBuddyEndpointPSEventSource`
- `RTBuddyTraceKitEndpoint.cpp`
- `_initConfigEDT`
- `RTBuddy.cpp`
- `IO Reporting statistics`
- `RTBuddyCrashlogEndpoint.cpp`
- `iopVirtualToApVirtual`
- `site.RTBuddyVisibleMemory`
- `IOReturn RTBuddyTraceKitEndpoint::_hostVersionGated()`
- ` - Invalid call stack, Depth of %u (%zu bytes) with %zu bytes remaining`
- `claim-wake-endpoint-flags`
- `allocateBackupBuffers`
- `RTBuddySlaveMemory *RTBuddy::slaveMemoryFromIOPPhys(IOPhysicalAddress, IOByteCount)`
- `routes`
- `OSLog`
- `  pc=%#018llx`
- `dont-power-on`
- `_foundFirmwareService`
- `_unknownSectionDecoder`
- `void RTBuddyTraceKitEndpoint::_waitForBusyACKGated(void *)`
- `RTBuddyUnknownDecoder`
- `unknown`
- `__OS_LOG`
- `status == kIOReturnSuccess`
- `crash of unknown type 0x%0x`
- `void RTBuddyOSLogEndpoint::_handleFlushRequest(const mbi_msg_t)`
- `Default`
- `Machine: %s\n`
- `Inbox underflow `
- `IONVRAM-FORCESYNCNOW-PROPERTY`
- `Instruction cache maintenance fault`
- `region_descriptor`
- `oslogSegment != nullptr`
- `void RTBuddy::callPatchbayCallback(RTBuddyFirmware *)`
- `!_validDimensions || (_processor->hibernateReuseMappings() && _maxEntries == syslog_get_max_entries(msg) && _maxMessageSize == syslog_get_max_message_size(msg))`
- `No mapping found for coredump section: %p - %p\n`
- `site.RTBuddyFirmwareService`
- `rtb_recoverable_ap_panics`
- `IOReturn RTBuddyCrashlogEndpoint::_synchronize(IsPolling, bool, IOCommandGate::Action, void *, void *, void *, void *)`
- `void RTBuddyBinaryLogHandler::initBuiltinEntryHandlers()`
- `RTBuddyBinaryLogEntryHandler.cpp`
- `_session`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `default_role.size() + _roleSize + (_roleSize ? 1 : 0) + 1 <= sizeof(source_info->role)`
- `\n%sASC Async error info: `
- `void RTBuddy::releaseEndpoint(unsigned int)`
- `IOReturn RTBuddyTraceKitEndpoint::attach(rtbuddy_trace_attach_t, OSSharedPtr<RTBuddyTraceKitSession> &)_block_invoke`
- `%s level %u`
- `\nUnknown Section: Section '%c%c%c%c' [%#x], Version %u.%u, size %zu\n`
- `\"RTBuddy(%s)::%s \" \"IOReporting: invalid message 0x%016llx received (cmd=0x%x)\" \"\\n%s\" @%s:%d`
- `\"Assertion failed: \" \"entry.key_len <= RTK_CAS_KEY_STR_MAX_SIZE\" @%s:%d`
- `void RTBuddyCrashlogEndpoint::setCrashlogBufferAddress(IOPhysicalAddress, size_t)`
- `IOReturn RTBuddyTraceKitEndpoint::_resetGated()`
- `site.RTBuddyVisibleMemoryImpl`
- `site.RTBuddyStatisticsDecoder`
- `\"RTBuddy(%s)::%s \" \"%s:%u: REQUIRE failed: %s, \" \"IOP provided invalid segment for coredump (base 0x%llx, size 0x%lx)\" @%s:%d`
- `_kdebugSendTypefilterChangedNotification`
- `Wrong frame size for %s. Got %u bytes, expected %zu\n`
- `Marin `
- `Image[%zu] %s slide=0x%016llx\n`
- `_incomingMessageAction`
- `site.RTBuddySegment`
- `_commonStart`
- `IOReturn RTBuddyTraceKitEndpoint::_powerStateCallbackGated(const unsigned long *, const unsigned long *)`
- `Outbox underflow `
- `site.RTBuddySmbDecoder`
- `Translation table walk synchronous parity error (1st level)`
- `_endpointActive`
- `    %s  %12s  0x%016llx  0x%016llx\n`
- ` ASC LSU error lsu_err_sts %#018llx,`
- `_setPowerStatePerformChangeGated`
- `shutdown-sleep`
- `void RTBuddyCrashlogEndpoint::_messageHandler(void *, void *)`
- `iodevice != nullptr`
- `_handlePingAck`
- `AP-requested crash`
- `  xfsta: 0x%08x\n`
- `Failed to create NVRAM value string '%s'\n`
- `tracekit`
- `Role`
- `RTBuddyEndpointService`
- `121112111111211112112211111212212222221`
- `_maxEntrySize`
- `_processor->getWorkLoop()->inGate()`
- `site.RTBuddyAutoBKPDecoder`
- `site.RTBuddyScmDecoder`
- `coredump-region`
- `site.RTBuddyPatchBay`
- `getOSLogSegmentSlices`
- `12111112122212121111111121122`
- `(kRtbIopStatusWaitingForVersion == _processor->getIopStatus()) || (kRtbIopStatusUnsupportedRemote == _processor->getIopStatus())`
- `_handleFlush`
- `12111112122212121111121`
- `dpc_err_sts %#018llx\n`
- `_attemptFirmwareLoad`
- `\"RTBuddy(%s)::%s \" \"Unable to determine target memory for firmware.\" \"\\n%s\" @%s:%d`
- `NULL != _buffer`
- `void RTBuddyOSLogEndpoint::_handleSourceInfoUUID(const mbi_msg_t)`
- ` %s`
- `_handleHereIsMyTypefilter`
- `  r%02d=%#018llx`
- `RTBuddySlaveBuffer`
- `site.RTBuddyRouteProvider`
- `hist != nullptr`
- `1221212111`
- `releaseChunkCPUTrace_block_invoke`
- `IOReturn RTBuddyTraceKitEndpoint::_unconfigureGated()`
- `12122222222`
- `RTBuddyRouteProvider`
- `_performPowerStateChangeGated`
- `nullptr != _crashlogDecoder`
- `_handlePowerAck`
- `1212222111122`
- `RTBuddyStatisticsDecoder`
- `size <= UINT_MAX`
- `kIOReturnSuccess == _processor->getWorkLoop()->runAction (OSMemberFunctionCast(IOWorkLoop::Action, this, &RTBuddyKdebugEndpoint::_kdebugSendHostReadyAction), this)`
- `121121`
- `IOUserClientClass`
- `\"%s: Unable to allocate %u byte heap\" @%s:%d`
- `_incomingMsgAction`
- `%#010lx,`
- `Debug`
- `Stack Pointer Alignment exception`
- `RTBuddySlaveMemory`
- `RTBuddy(AP): Debug info:\n`
- `Section size error.  Signature %#0x, version %#0x, section (%u bytes) larger than remaining buffer (%llu bytes)`
- `!rtb->hibernateReuseMappings() || _bufferMemoryDescriptor == nullptr || _bufferMemoryDescriptor->getLength() >= _bufferSize`
- `_powerStateCallbackGated`
- `(nullptr != _tempSourceInfo) && (0 != _roleSize) && !_uuidValid && coalescerBufferValid(_coalescers[id]) && curr_size <= RTK_BITS_TO_BYTES(LOG_COALESCER_SOURCE_INFO_ROLE_MSG_ROLE_BITS) && (shift + curr_size <= sizeof(_tempSourceInfo->role))`
- `NMI FIQ`
- `syslog`
- `nullptr != _buffer`
- `RTBuddySyslogEndpoint.cpp`
- `RTBuddy(%s)::%s: Initial configuration failed with status 0x%x\n`
- `IOReturn RTBuddyTraceKitEndpoint::_enableGated(const bool)`
- `\nFaulting Int Call Stack:`
- `nullptr != ism`
- `AP Panicked`
- `AP instance uninitialized\n`
- `Synchronous external abort`
- `virtual void RTBuddy::_initMapper()`
- `Mailbox error`
- `kdebugCallback`
- `222221`
- `bounded_ptr<T>::discard_bounds: Discarding the bounds on this pointer would lose the fact that it is outside of the bounds set originally`
- `\"RTBuddy(%s)::%s \" \"CoreAnalytics: invalid message 0x%016llx received (cmd=0x%x)\" \"\\n%s\" @%s:%d`
- `cold-boot-after-hibernate`
- `copy32FromIopVirtual`
- `initWithOptions`
- `bounded_ptr<T>::operator+=(n): Calculating the number of bytes to add to the offset (n * sizeof(T)) would trigger an overflow`
- `site.RTBuddyVersionDecoder`
- `RTBuddyUtils.cpp`
- `RTBuddyRegisterFrameDecoder`
- `%s coredump: error = %s\n`
- `\"RTBuddy(%s)::%s \" \"Selected firmware does not match the target IOP. (%s)\" \"\\n%s\" @%s:%d`
- `claim-wake`
- `slaveMemoryFromIOPPhys`
- `%s.MBIEndpoint.%u`
- `/arm-io`
- `RTBuddy64`
- `!_rtb->hibernateReuseMappings() || _bufferMemoryDescriptor == nullptr || _bufferMemoryDescriptor->getLength() >= _bufferSize`
- `_processor->getIopStatus() == kRtbIopStatusPoweringDown`
- `_handleSourceInfoRegister`
- `error: stack too big for crash log`
- `_backups`
- `enable`
- `\nHex Data: %s\n`
- `readwriteMapForIopVirtual`
- `endpointHandle < _endpoints.size()`
- `NULL != (_akf = OSDynamicCast(AppleIOP,_akfNub->getAKFProvider()))`
- `powerOn() == kIOReturnSuccess`
- `SEMWAIT   `
- `_backupAssertionCount == 1`
- `!os_mul_and_add_overflow(sizeof(CrashLogAgentInfo_t), i, sizeof(CrashLogMultiAgentHeader_t), &agent_hdr_offset)`
- `site.RTBuddyKdebugEndpoint`
- `\"RTBuddy(%s)::%s \" \"failed to stop (%x)\" \"\\n%s\" @%s:%d`
- `chip-id`
- `_forwardingBuddy`
- `RTBuddySlaveMemoryBuffer`
- `RTBuddyFirmware`
- `error: fp is null => possible stack corruption`
- `1211`
- `site.RTBuddySlaveMemoryDescriptor`
- `remote data`
- `watchdog timeout: No response in over %llu sec.`
- `status`
- `%s: Force fatal crashlog`
- `client6`
- `\nl2c_err_sts %#018llx, l2c_err_adr %#018llx, l2c_err_inf %#018llx\nlsu_err_sts %#018llx, fed_err_sts %#018llx, mmu_err_sts %#018llx\n`
- `1222121121121`
- `  Section size too small.  Got %zu, expected >= %zu`
- `RTBuddyCoredumpMap`
- `/%03d`
- `RUNNABLE  `
- `Unable to add coredump section %u\n`
- `NVRAM Not enough memory %zu:%zu\n`
- `\"RTBuddy(%s)::%s \" \"Unexpected flow, somehow already sent AP state\" \"\\n%s\" @%s:%d`
- `!getWorkLoop()->onThread()`
- `segment-ranges`
- `kIOReturnSuccess == _processor->getWorkLoop()->runAction (OSMemberFunctionCast (IOWorkLoop::Action, this, &RTBuddyKdebugEndpoint::_kdebugSendFlushRequest), this)`
- `NULL != (_iopRole = OSDynamicCast(OSString, _akf->getProperty(\"role\")))`
- `Errors: Skipped %s coredump because ...\n`
- `RTBuddyBinaryLogEntryHandlerTraceKit`
- `IOVirtualAddress RTBuddyCoredumpMap::physToVirt(IOPhysicalAddress, IOByteCount)`
- `site.RTBuddyCoredumpMapEntry`
- `Power State`
- `rtb_disable_fw_load`
- `121111121222121211111111221`
- `checkForZeroDVA`
- `!_endpointActive`
- `FirmwareVersion`
- `Multilog crash with invalid (short) log length. %u bytes. Minimum valid length is %lu \n`
- `IOReturn RTBuddyKdebugEndpoint::_kdebugSendTypefilterChangedNotification()`
- `Sleep Count: %llu\nWake Count:  %llu\nDuty Cycle:  %u\n`
- `...`
- `site.RTBuddyProductVersionDecoder`
- `power-managed`
- `RTBuddyAscDecoder`
- `23:29:55`
- ` - nested unknown 0x%x @ 0x%08llx`
- `RTBuddyEntropyEndpoint.cpp`
- `void RTBuddy::_attemptFirmwareLoad()`
- `sleep-on-hibernate`
- `RTBuddyCrashlogDecoder`
- `addEntryHandler`
- `rtb_log_flags`
- `Wrong frame size for ARMv7m. Got %U bytes, expected %zu or %zu\n`
- `_synchronize`
- `patchbay_virt + patchbay_size <= map_base + map->getLength()`
- `OSBoundedPtr<const uint8_t> RTBuddyCrashlogDecoder::_multiCrashlogFindFirstCrash(OSBoundedPtr<const uint8_t>, size_t *)`
- `1212`
- `site.RTBuddyCrashlogSectionDecoder`
- ` Inbox%d overflow`
- `int RTBuddyCoredumpMap::indexOfVirt(IOPhysicalAddress)`
- `bool RTBuddyCoreAnalyticsEndpoint::_handleEvent(unsigned int)`
- `\"RTBuddy(%s)::%s \" \"already running (current state: %d)\" \"\\n%s\" @%s:%d`
- `nullptr != ep`
- `site.RTBuddyCoredumpDecoder`
- `Domain fault`
- `RTBuddyCoprocDrivenCoredump`
- `firmwareService`
- `releaseBackupBufferAssertion`
- `\"RTBuddy(%s)::%s \" \"Entropy: invalid message 0x%016llx received (cmd=0x%x)\" \"\\n%s\" @%s:%d`
- `121`
- `Invalid version`
- `RTBuddy force power off initiated by client driver\n`
- `RTBuddyEndpoint`
- `nullptr != (_stats = IOSimpleReporter::with (this, kIOReportCategoryDebug, kIOReportUnitNone))`
- `_coredumpMap`
- `RTBuddySegment`
- `ep %s: %s`
- `void RTBuddyKdebugEndpoint::_messageHandler(void *, void *)`
- `0x%016llx`
- `should-control-sram`
- `Kdebug`
- `nullptr != (state = IOStateReporter::with (this, static_cast<IOReportCategories>(reporter.category), reporter.num_elem, reporter.unit))`
- `IOReturn RTBuddyManagementEndpoint::_handleHello(mbi_msg_t)`
- `\n`
- `%s coredump: failed to read firmware metadata. error = %s\n`
- `segment-names`
- `RTBuddyIOReportingEndpoint`
- `%s NMI: Unknown reason`
- `(oslog_phys_addr & PAGE_MASK) == 0`
- `Permission fault (section)`
- `crashlog`
- `void RTBuddy::takeBackupBufferAssertion()`
- `!_rtb->getWorkLoop()->onThread()`
- `            ... IOP was not running.\n`
- `B20@?0i8Q12`
- ` - pc=%#010x  fsr=%#010x (%s)  far=%#010x`
- `getWorkLoop()->inGate()`
- `createEndpoint`
- `quiesced`
- `_copyBufferMemoryDescriptor`
- `count <= UINT8_MAX`
- `_handleFlushRequest`
- `\n   sp=%#018llx   lr=%#018llx   pc=%#018llx  psr=%#08x\n`
- `IDLE      `
- `\"RTBuddy: memcpy_to32 requires 4-byte alignment (dst=%p, size=%zu)\" @%s:%d`
- `kIOReturnSuccess == getWorkLoop()->addEventSource(ep)`
- `oldBufferSize >= _bufferSize`
- `void RTBuddyFirmware::copyToTarget(RTBuddy *)`
- `rtb_enable_tracing`
- `_freeOSLogSegment`
- `function-force_wake`
- `\"RTBuddy(%s)::%s \" \"unsupported message received on management endpoint: 0x%016llx\" \"\\n%s\" @%s:%d`
- `No crashlog entry found in multi-crashlog header\n`
- `_initDefaultSectionDecoders`
- `IOReturn RTBuddyTraceKitEndpoint::_configureGated(rtbuddy_trace_config_t, OSSharedPtr<RTBuddyTraceKitSession> &)_block_invoke`
- `_votePstate`
- `virtual IOReturn RTBuddy::saveSRAM()`
- `Other`
- `12111211111121111211221111121`
- `void RTBuddyCrashlogDecoder::_initDefaultSectionDecoders()`
- `crashlogBuffer != nullptr`
- `entropy_protocol.h`
- `RTBuddySmbDecoder`
- `_waitingOnFirmwareService`
- `void RTBuddy::_setRole()`
- `void RTBuddyIOReportingEndpoint::_apInitiatedUpdateGated()`
- `_handleBufferRequest`
- `0x%08x 0x%08x 0x%08x 0x%08x | %c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n`
- `ioreporting`
- `site.RTBuddyRoute`
- `site.RTBuddySlaveBuffer`
- `RTBuddyRemoteSlaveMemoryDescriptor`
- `RTBuddyNativeSlaveMemoryDescriptor`
- `site.RTBuddyNativeSlaveMemoryDescriptor`
- `_loadFirmwareGated`
- `automatic-rail-gating-enabled`
- `_bufferMemoryDescriptor->getRetainCount() == 1`
- `%s %s - %s%s%s\n%s`
- `site.RTBuddyFirmware`
- `_handleEPRollCall`
- `_panicString`
- `RTBuddyBinaryLogEntryHandler`
- `RTBuddyCallStackDecoder`
- `_changePowerState`
- `initBuiltinEntryHandlers`
- `1221`
- `update count`
- `\"RTBuddy(%s)::%s \" \"forceCrashlog() called with unexpected RTBuddyNmiType: %d\" \"\\n%s\" @%s:%d`
- `void RTBuddyCrashlogEndpoint::_allocateLocalBuffer()`
- `power`
- `client7`
- `reset() == kIOReturnSuccess`
- `bounded_ptr<T>::operator->: Accessing a member through this pointer would access memory outside of the bounds set originally`
- `\"Assertion failed: \" \"dict\" @%s:%d`
- `Crash with unsupported log (major version: %u, should be %u)\n`
- `RTBuddyKdebugEndpoint.cpp`
- `Invalid data`
- `nullptr != (_reporterIopState = IOStateReporter::with(this, kIOReportCategoryPower, kRtbIopStatusCount))`
- `IOP State`
- `_kdebugBuffer`
- `_userEntryHandlers`
- `nullptr != (_reporterList = OSSet::withCapacity(4))`
- `Multilog crash with unsupported log (major version: %u, should be %u)\n`
- `[Possible stack overflow]`
- `WFI or WFE`
- `rtb_disable_watchdog`
- `_verifyBufferGated`
- `IOReturn RTBuddyFirmware::copySegmentDescriptorWithName(const char *, RTBuddySegmentDescriptor *)`
- `End header does not match log header, log might be corrupted\n`
- `timesync`
- `loadFirmware`
- `            ... crashlog was not received.\n`
- `            ... coredump segment information was not received.\n`
- `Section size too small.  Signature %#0x, version %#0x, section (%u bytes) should be at least %zu bytes`
- `site.RTBuddyRtkitDecoder`
- `IOReturn RTBuddy::resizeEndpointList(unsigned int)`
- `void RTBuddyCrashlogDecoder::writePanicString(const char *, va_list)`
- `site.RTBuddySyslogEndpoint`
- `main bin spec`
- `Time: 0x%016llx\n`
- `power state`
- `disable-in-restore`
- `_buffer->enableNoAllocLocalCopy() == kIOReturnSuccess`
- `RTBuddyBinaryLogHandler`
- `Misaligned PC exception`
- `Asynchronous parity error on memory access`
- `firmware`
- `\"RTBuddy(%s)::%s \" \"No response received in %llds, %s not started? (%x)\" \"\\n%s\" @%s:%d`
- `releaseEndpoint`
- `wdt`
- `%s(%s)`
- `Multilog crash with invalid header signature: 0x%x, should be 0x%x\n`
- `  smsta: 0x%08x\n`
- `Translation table walk synchronous parity error (2nd level)`
- `site.RTBuddyFirmwareBundle`
- `RTBuddyCL4Coredump.cpp`
- `%s coredump: failed to save data. error = %s\n`
- `client9`
- `start`
- `os leg ep not ready\n`
- `patchbay_virt >= map_base`
- `RTBuddyUserClient::clientMemoryForType (0x%x)\n`
- `_handleHereIsMyBuffer`
- `getEndpoint()->sendMessage(&msg) == kIOReturnSuccess`
- `nub != nullptr`
- `user`
- `_handleDimensions`
- `Domain fault (section)`
- `Synchronous parity error on memory access on translation table walk`
- `void RTBuddy::notifyPowerStateChange(RTBuddyPowerState, RTBuddyPowerState)`
- `121112111111211112112211111211111222221`
- `RTBuddyBinaryLogEntryHandlerOSLog`
- `obj != nullptr`
- `RTBuddyTraceKitEndpoint`
- `Failed to write NVRAM value string '%s':'%s'\n`
- `Unknown IOP`
- `Found %sSCM Data: %s\n`
- `(nullptr != _tempSourceInfo) && _uuidValid && coalescerBufferValid(_coalescers[id]) && (shift + sizeof(uint32_t) <= sizeof(_tempSourceInfo->uuid))`
- `WAITING   `
- `%s coredump: server does not support coredump. flags: 0x%llx\n`
- `data`
- `Warnings: During %s coredump ...\n`
- `true == IOSlaveProcessor::start(_akf)`
- `_buffer != NULL && _validDimensions`
- `RTBuddyAutoBKPDecoder`
- `RTBuddyFirmwareBundle`
- `!_alreadySentRemoteMessage`
- `!os_sub_overflow(_crashlogBufferSize, crashlogOffset, &crashLogBufferSize)`
- `virtual void RTBuddyKdebugEndpoint::kdebugCallback(kd_callback_type, void *)`
- `RTBuddyBuiltinEndpoint.cpp`
- `site.RTBuddyEndpoint`
- `ASC L2C %s bit error, `
- `forward-crashlog-to`
- `void RTBuddy::_commonStart(IOService *)`
- `entropy_msg_cmd(msg) == ENTROPY_MSG_ENTROPY_GENERATE`
- `Chinook `
- `chip-revision`
- `\"RTBuddy(%s)::%s \" \"Failed to copy entries\" \"\\n%s\" @%s:%d`
- `ap-recoverable-panics`
- `!uuid_is_null(uuid)`
- `RTBuddyManagementEndpoint.cpp`
- `\"RTBuddy(%s)::%s \" \"could not add %s to source info map\\n\" \"\\n%s\" @%s:%d`
- `IOHibernateState`
- `!_isStandAlone || _endpoints.size() == 0`
- `IOReturn RTBuddyManagementEndpoint::_handleEPRollCall(mbi_msg_t)`
- `success`
- `Metadata not cached`
- `PREFETCH ABORT`
- `_initializationThread`
- `resizeEndpointList`
- `virtual bool RTBuddyIOReportingEndpoint::start(IOService *)`
- `RTBuddyCL4Coredump`
- `coredump-enable`
- `RTBuddy(%s): %s - %s%s%s\n`
- `RTBuddyBinaryLogEntryHandlerMetric`
- ` - `
- ` %sASC MMU error mmu_err_sts %#018llx,`
- `kdebug`
- `physToVirt`
- `sendMessage`
- `virtual IOReturn RTBuddy::sendMessage(UInt32, void *, void *, bool)`
- `virtual void RTBuddyKdebugEndpoint::enable()`
- `RTBuddy(%s)::%s: kdebug IOP flush timed out. Some trace entries may not be collected\n\n`
- `bool RTBuddyOSLogEndpoint::_initWithOptions(IOSlaveProcessor *)`
- `NVRAM not available\n`
- `site.RTBuddyBinaryLogEntryHandlerOSLog`
- `RTBuddyTraceKitSession`
- `IOReturn RTBuddyTraceKitEndpoint::_flushGated()`
- `reconfig-firmware`
- `\"RTBuddy(%s)::%s \" \"unsupported power state: 0x%x\" \"\\n%s\" @%s:%d`
- `slaveMemoryForPhysicalRange`
- `rtb_allow_all_fw`
- `_kdebugSendHostReadyAction`
- `_kdebugMemoryDecriptor->getRetainCount() == 1`
- `Translation fault (section)`
- `\"Property '%s' of registry entry '%s' is %u bytes long.  Expected %lu bytes.\" @%s:%d`
- `notifyPowerStateChange`
- `nullptr != (_epIOReporting = RTBuddyIOReportingEndpoint::withOptions(this))`
- `region-base`
- `void RTBuddyTraceKitEndpoint::_waitForEndpointActiveGated()`
- `bounded_ptr<T>::operator-=(n): Subtracting the specified number of bytes from the offset representing the current position would overflow.`
- `1211121111112111121122111112121122211111111111111111121`
- `_waitForEndpointActiveGated`
- `far_physical=%#018llx `
- `Heap Usage: %llu / %llu\n`
- `site.RTBuddy64`
- `_initMapper`
- `could not find role uuid\n`
- `_configureGated`
- `RTBuddyHexDecoder`
- `site.RTBuddyOSLogSegmentSlice`
- `sizeof(_ascDramMask) == tmp->getLength()`
- `IOPlatformPanicAction`
- `\"Variable write size (%ld) does not match patch variable size(%d)\" @%s:%d`
- `_builtinEntryHandlers[kMetricHandlerIndex]`
- `%s`
- `segment != NULL`
- `1211111212221212111111122211112`
- `_kdebugSendFlushRequest`
- `Memory access synchronous parity error`
- `\"Assertion failed: \" \"item_count\" @%s:%d`
- `void RTBuddySyslogEndpoint::_handleRequestSyslogBuffer(mbi_msg_t)`
- `1222121122211`
- `RTBuddyStringDecoder`
- `RTBuddyTimeDecoder`
- `site.RTBuddyCrashlogDecoder`
- `%s %s%s%s\n%s`
- `IOReturn RTBuddyCrashlogEndpoint::_checkForCrashGated(uintptr_t)`
- `  pc=0x%08x `
- `Not ready`
- `_kdebugIOPReady`
- `IOReportLegend`
- `watchdog error: Unable to send ping in %u attempts.`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `timeout`
- `writeCrashlog`
- `RTBuddyNvramDecoder`
- `\"Assertion failed: \" \"buffer.size_bytes() >= entry.key_len + data_len\" @%s:%d`

**[__TEXT.__os_log]**

- `RTBuddy(%s): Unable to reserve layout space: %llu bytes`
- `RTBuddy(%s): Registering log role for %s/%s`
- `RTBuddy(%s): Resuming...\n`
- `RTBuddy(%s): Failed to send flush completion message to IOP - %x`
- `RTBuddy(%s): image_layout_t was not sequential: (%u, %u)`
- `RTBuddy(%s): Metric entry from unregistered source %u, dropping`
- `RTBuddy: metric label resolve failed: source %u label_offset 0x%x below string table base 0x%x`
- `RTBuddy(%s): IOP start explicitly disabled by boot-arg`
- `RTBuddy(%s): Unimplemented syslog command: %x`
- `RTBuddy(%s): Time out, failed to process kdebug traces before power gating\n`
- `RTBuddy(%s): Metric collection header entry too small: %u < %zu bytes`
- `RTBuddy(%s): oslog segment size. found oslog slice for uuid %s. length is %llu\n`
- `Failed to send event - no coreAnalyticsService`
- `RTBuddy(%s): WARNING: Bypassing firmware validation.`
- `RTBuddy(%s): invalidate layout`
- `RTBuddy(%s): received system layout with %u address spaces`
- `RTBuddy(%s): space_layout_t was not sequential: (%u, %u)`
- `RTBuddy(%s): String table info not found for source %u, missing collection header`
- `RTBuddy(%s): Finding route %d`
- `RTBuddy(%s): no log handler for type %u`
- `RTBuddy(%s): received image layout for space %u image %u`
- `RTBuddy(%s): decode buffer too small: %zu < %zu bytes`
- `RTBuddy(%s): Error processing metric in log entry`
- `RTBuddy(%s): configure hw_trace %u`
- `RTBuddy(%s): Loaded firmware: %s - %s\n`
- `RTBuddy(%s): %s%s`
- `Entropy (count: %zu) requested`
- `RTBuddy(%s): OSLog log_entry from source %s is corrupt, dropping buffer`
- `RTBuddy(%s): Boot args override: %s = %lld`
- `RTBuddy(%s): received space layout for space %u with %u images`
- `RTBuddy(%s): log entry size too small: %zu < %zu bytes`
- `RTBuddy(%s): tracekit version mismatch: msg=%u expected=%u type=%u`
- `RTBuddy(%s): No string table matches offset 0x%x for source %u`
- `RTBuddy(%s): String table info not found for source_info`
- `RTBuddy(%s): configure sw_trace %u`
- `RTBuddy(%s): IOP start disabled by device tree`
- `RTBuddy(%s): could not find oslog slice for role %s\n`
- `RTBuddy(%s): tracekit message too small: %zu < %llu bytes`
- `RTBuddy(%s): OSLog log_coalescer_entry from source %s is corrupt, dropping buffer`
- `RTBuddy(%s): IOP start disabled in restore`
- `RTBuddy(%s): Success route %d`
- `RTBuddy(%s): system_layout_t was not received`
- `RTBuddy(%s): %s`
- `RTBuddy(%s): Failed to append/create string table chunk`
- `RTBuddy: metric label resolve failed: source %u label_offset 0x%x: string table is null`
- `RTBuddy(%s): OSLog endpoint registering to logd(uuid: %s, role: %s, range_start: %u, range_end: %u, fw_type: %u)`
- `RTBuddy(%s): Boot args override: %s = %d`
- `RTBuddy(%s): image_layout_t did not match current space: (%u, %u)`
- `RTBuddy: metric label resolve failed: source %u label_offset 0x%x: offset %u exceeds string table length %u`
- `RTBuddy(%s): cL4 coredump region identified`
- `RTBuddy(%s): WARNING: ping timeout.`
- `RTBuddy(%s): WARNING: failed to send ping.`
- `RTBuddy(%s): No string table available for source %u`
- `RTBuddy(%s): OSLog segment methods. uuid %s. method %u\n`
- `RTBuddy(%s): added oslog segment slice. uuid %s. offset %d. len %d\n`
- `RTBuddy(%s): OSLog log_entry size from source %s is corrupt, dropping buffer`
- `RTBuddy User client. Lookup oslog uuid for role %s. Status is %x\n`
- `RTBuddy(%s): copy oslog. found oslog slice for uuid %s. length is %llu. offset is %llu\n`
- `RTBuddy(%s): OSLog log_entry from source has corrupt source_info, dropping entry`
