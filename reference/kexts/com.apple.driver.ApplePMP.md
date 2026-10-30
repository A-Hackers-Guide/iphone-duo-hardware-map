# `com.apple.driver.ApplePMP`

- Name: ApplePMP
- Version: `1`
- UUID: `664DBD1A-DC9C-3A2E-98C5-7695CF774D1F`
- Source version: `1661.40.5.0.0`
- Depends on: [`com.apple.driver.AppleA7IOP`](com.apple.driver.AppleA7IOP.md) 1.0, [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.driver.RTBuddy`](com.apple.driver.RTBuddy.md) 1.0.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.4, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (3) [KC]

### ApplePMP
- `CFBundleIdentifier`: `com.apple.driver.ApplePMP`
- `IOClass`: `ApplePMP`
- `IONameMatch`: `PMPEndpoint1`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePMP`
- `IOPlatformSleepAction`: `610`
- `IOPlatformWakeAction`: `610`
- `IOProviderClass`: `RTBuddyEndpointService`

### ApplePMPThermal
- `CFBundleIdentifier`: `com.apple.driver.ApplePMP`
- `IOClass`: `ApplePMPThermal`
- `IONameMatch`: `PMPEndpoint2`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePMP`
- `IOProviderClass`: `RTBuddyEndpointService`

### ApplePMPv2
- `CFBundleIdentifier`: `com.apple.driver.ApplePMP`
- `IOClass`: `ApplePMPv2`
- `IONameMatch`:
  - `PMPEndpoint1`
  - `PMP0Endpoint1`
  - `PMP1Endpoint1`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePMP`
- `IOPlatformSleepAction`: `610`
- `IOPlatformWakeAction`: `610`
- `IOProviderClass`: `RTBuddyEndpointService`


## C++ classes (9) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `ApplePMP` | 0x220 | IOService → IORegistryEntry |
| `ApplePMPControlFunction` | 0x30 | AppleARMFunction |
| `ApplePMPEvent` | 0xf8 | AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `ApplePMPThermal` | 0xd0 | IOService → IORegistryEntry |
| `ApplePMPThermalUserClient` | 0xe0 | IOUserClient → IOService → IORegistryEntry |
| `ApplePMPUserClient` | 0xe0 | IOUserClient → IOService → IORegistryEntry |
| `ApplePMPv2` | 0x118 | IOService → IORegistryEntry |
| `ApplePMPv2RegistryEntry` | 0x38 |  |
| `ApplePMPv2UserClient` | 0xe0 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001b7c off=0x0069a960-0x0069c4dc addr=0xfffffe000769e960-0xfffffe00076a04dc r--/r--   __TEXT            
	sz=0x0000003c off=0x0069b028-0x0069b064 addr=0xfffffe000769f028-0xfffffe000769f064               __TEXT.__const            
	sz=0x00001478 off=0x0069b064-0x0069c4dc addr=0xfffffe000769f064-0xfffffe00076a04dc               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x0000d208 off=0x0235c5a0-0x023697a8 addr=0xfffffe00093605a0-0xfffffe000936d7a8 r-x/r-x   __TEXT_EXEC       
	sz=0x0000cdb8 off=0x0235c5a0-0x02369358 addr=0xfffffe00093605a0-0xfffffe000936d358          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000450 off=0x02369358-0x023697a8 addr=0xfffffe000936d358-0xfffffe000936d7a8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000448 off=0x04983b60-0x04983fa8 addr=0xfffffe000b987b60-0xfffffe000b987fa8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04983b60-0x04983c28 addr=0xfffffe000b987b60-0xfffffe000b987c28               __DATA.__data             
	sz=0x00000178 off=0x00000000-0x00000178 addr=0xfffffe000b987c28-0xfffffe000b987da0               __DATA.__common           (Zerofill)
	sz=0x00000208 off=0x00000000-0x00000208 addr=0xfffffe000b987da0-0xfffffe000b987fa8               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00003a30 off=0x01192fc8-0x011969f8 addr=0xfffffe0008196fc8-0xfffffe000819a9f8 rw-/rw-   __DATA_CONST      
	sz=0x00000038 off=0x01192fc8-0x01193000 addr=0xfffffe0008196fc8-0xfffffe0008197000         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000038 off=0x01193000-0x01193038 addr=0xfffffe0008197000-0xfffffe0008197038         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00003330 off=0x01193038-0x01196368 addr=0xfffffe0008197038-0xfffffe000819a368         __DATA_CONST.__const            
	sz=0x00000240 off=0x01196368-0x011965a8 addr=0xfffffe000819a368-0xfffffe000819a5a8         __DATA_CONST.__kalloc_type      
	sz=0x00000140 off=0x011965a8-0x011966e8 addr=0xfffffe000819a5a8-0xfffffe000819a6e8         __DATA_CONST.__kalloc_var       
	sz=0x00000228 off=0x011966e8-0x01196910 addr=0xfffffe000819a6e8-0xfffffe000819a910         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000e8 off=0x01196910-0x011969f8 addr=0xfffffe000819a910-0xfffffe000819a9f8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 167 at 0x04ae1708
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     664DBD1A-DC9C-3A2E-98C5-7695CF774D1F
008: LC_SOURCE_VERSION           1661.40.5.0.0
009: LC_FUNCTION_STARTS          offset=0x004aac750 size=0x200
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `ApplePMP`
- `CFBundleIdentifier`: `com.apple.driver.ApplePMP`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `ApplePMP`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
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
- `NSHumanReadableCopyright`: `Copyright © 2015 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/ApplePMP.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898874016`
- `_PrelinkExecutableRelativePath`: `ApplePMP`
- `_PrelinkExecutableSize`: `76796`
- `_PrelinkExecutableSourceAddr`: `-2198898874016`
- `_PrelinkKmodInfo`: `-2198828713120`

## Strings (154) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.ApplePMPv2RegistryEntry`
- `_pmCommandPending[domain]`
- `_state == kStateWaitingForReady`
- `static IOReturn ApplePMPUserClient::_getNumDVFSDomains(OSObject *, void *, IOExternalMethodArguments *)`
- `ehub_msg_get_cmd(ack_msg) == (command + 1)`
- `\"ApplePMPUserClient: %s:%u REQUIRE failed: %s\" @%s:%d`
- `static IOReturn ApplePMPUserClient::_pmuTelemetryEnable(OSObject *, void *, IOExternalMethodArguments *)`
- `ApplePMPThermal`
- `ret == kIOReturnSuccess`
- `IOReturn ApplePMP::_sendEHubNodeCommand(UInt32, UInt64)`
- `static IOReturn ApplePMPUserClient::_pBattDisable(OSObject *, void *, IOExternalMethodArguments *)`
- `virtual bool ApplePMP::start(IOService *)`
- `number`
- `ApplePMPUserClient.cpp`
- `12111112122212121121111111111111121`
- `_clpcPerfController`
- `void ApplePMP::_pmonMessageHandler(mbi_msg_t)`
- `static IOReturn ApplePMPUserClient::_fastDieControllerDisable(OSObject *, void *, IOExternalMethodArguments *)`
- `pio-reg-index`
- `format`
- `_endpoint`
- `iodc`
- `ExternalControlEffort`
- `_domainIndex <= _getNumDVFSDomains()`
- `reg`
- `ApplePMPThermalUserClient`
- `dram-capacity`
- `energy-model-dram-configs`
- `IOReturn ApplePMP::_powerStateHandlerGated(void *, void *, void *)`
- `stateName`
- `_pmp`
- `_armIODevice`
- `pbatt_memory`
- `static IOReturn ApplePMPUserClient::_pBattEnable(OSObject *, void *, IOExternalMethodArguments *)`
- `site.ApplePMPThermal`
- `121111`
- `_endpointService`
- `/ApplePMP/ApplePMPv2UserClient.cpp`
- `client->pmp`
- `com.apple.private.pmp.performance-spi`
- `setActive`
- `void ApplePMP::_pBattMessageHandler(mbi_msg_t)`
- `site.ApplePMPv2UserClient`
- `root`
- `static IOReturn ApplePMPUserClient::_fastDieControllerSetLifeTimeServoTempTarget(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn ApplePMPUserClient::_samplerEnable(OSObject *, void *, IOExternalMethodArguments *)`
- `B16@?0^{OSObject=^^?i}8`
- `_memoryMap`
- `static IOReturn ApplePMPUserClient::_ping(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn ApplePMPUserClient::_setDVFSStates(OSObject *, void *, IOExternalMethodArguments *)`
- `ApplePMPv2.cpp`
- `site.ApplePMPThermalUserClient`
- `_workLoop`
- `AppleDieTempController`
- `_eHubCommandPending == NULL`
- `*watchdog.timer`
- `static IOReturn ApplePMPUserClient::_fastDieControllerEnable(OSObject *, void *, IOExternalMethodArguments *)`
- `%s: started\n`
- `%s(%s) found matching service %s\n`
- `\"Unknown message: %#llx\" @%s:%d`
- `_eHubTimeSeriesBuffers`
- `void ApplePMP::_createWatchdogTimers()`
- `static IOReturn ApplePMPUserClient::_pmuTelemetryDisable(OSObject *, void *, IOExternalMethodArguments *)`
- `site.ApplePMPv2`
- `ApplePMPEvent`
- `wait-for`
- `chip-id`
- `_memoryDescriptor`
- `pm_msg_get_cmd(ack_msg) == (command + 1)`
- `success`
- `static IOReturn ApplePMPUserClient::_samplerDisable(OSObject *, void *, IOExternalMethodArguments *)`
- `site.const OSSymbol*`
- `ApplePMP: CLPC setAETSMaxControlEffortFunction failed\n`
- `name`
- `pmp-msg-timout-panic`
- `props`
- `_state == kStateMemoryInit`
- `void ApplePMP::_readyMessageHandler(mbi_msg_t)`
- `_events[event]`
- `_pmCommandPending[i] == NULL`
- `result`
- `_memory`
- `void ApplePMP::_initMemoryAckHandler(mbi_msg_t)`
- `1`
- `%s: starting...\n`
- `IODeviceTree:/arm-io/pmgr`
- `unit`
- `_commandGate`
- `_slaveProcessor`
- `IOReturn ApplePMP::_sendEHubTimeSeriesCommand(UInt32, UInt32, IOMemoryDescriptor *, UInt32 *)`
- `client`
- `AppleCLPC`
- `ApplePMP: Connected to AppleCLPC\n`
- `void ApplePMP::_messageHandler(void *, void *)`
- `1211111212221212111111121112122`
- `Battery`
- `ApplePMPv2UserClient`
- `_eHubMemory`
- `void ApplePMP::_getNumDVFSStates(UInt64, UInt64 *, UInt64 *, UInt64 *)`
- `static IOReturn ApplePMPUserClient::_pmSendCommand(OSObject *, void *, IOExternalMethodArguments *)`
- `ApplePMPv2RegistryEntry`
- `ApplePMP`
- `PMP workloop`
- `\"ApplePMP: %s:%u REQUIRE failed: %s\" @%s:%d`
- `virtual IOReturn ApplePMP::setProperties(OSObject *)`
- `properties`
- `IOReturn ApplePMP::_sendPMCommand(UInt32, UInt64, UInt64, UInt64, UInt64)`
- `site.ApplePMPUserClient`
- `virtual bool ApplePMPUserClient::start(IOService *)`
- `1211112`
- `i8@?0`
- `pmptool-config`
- `1211111212221212111111111111`
- `IODeviceTree:/chosen`
- `_iopNub`
- `key`
- `static IOReturn ApplePMPUserClient::_getDVFSDomainName(OSObject *, void *, IOExternalMethodArguments *)`
- `B24@?0r^{OSSymbol=^^?ib14b18*{smrq_slink={?=^{smrq_slink}}}}8^{OSObject=^^?i}16`
- `dram-vendor-id`
- `LifetimeServoDieTemperatureTargetPropertyKey`
- `dict`
- `_pmuTelemetryAgentCount <= kPMUTelemetryAgentMaxCount`
- `site.ApplePMPControlFunction`
- `PMP thermal workloop`
- `ApplePMPv2`
- `registry-dictionary`
- `bool ApplePMP::clpcPerfControllerArrivalHandler(void *, IOService *, IONotifier *)`
- `result == kIOReturnSuccess`
- `static IOReturn ApplePMPUserClient::_samplerConfigCustomReg(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn ApplePMPUserClient::_getNumDVFSStates(OSObject *, void *, IOExternalMethodArguments *)`
- `ApplePMP.cpp`
- `_samplerAgentCount <= kSamplerAgentMaxCount`
- `AssertMacros: %s, %s file: %s, line: %d, value: %lld\n`
- `static IOReturn ApplePMPUserClient::_setProperty(OSObject *, void *, IOExternalMethodArguments *)`
- `site.ApplePMPEvent`
- `ReportInterval`
- `%s(%s) started\n`
- `ApplePMPUserClient`
- `ApplePMPControlFunction`
- `static IOReturn ApplePMPUserClient::_getDVFSStateName(OSObject *, void *, IOExternalMethodArguments *)`
- `12111112122212121211211121121221112111111212121212122111121111111211`
- `_eHubMemoryMap`
- `site.UInt32`
- `pm_msg_get_device(ack_msg) == device`
- `setAETSMaxControlEffortFunction`
- `domainName`
- `site.ApplePMP`
- `_dieTempController`
- `site.UInt64*`
- `pm_msg_get_domain(ack_msg) == domain`
- `12111112122212121221111211`
- `pmp`
- `role`
- `ptd-update-reg-index`
