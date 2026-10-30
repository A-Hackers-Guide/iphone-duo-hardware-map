# `com.apple.driver.AppleT8160PCIe`

- Name: AppleT8160PCIe
- Version: `1`
- UUID: `FC1C92AB-E98E-3165-BC7B-08FD97657186`
- Source version: `1042.40.10.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleEmbeddedPCIE`](com.apple.driver.AppleEmbeddedPCIE.md) 1.0.0, [`com.apple.driver.AppleFirmwareKit`](com.apple.driver.AppleFirmwareKit.md) 1, [`com.apple.iokit.IOPCIFamily`](com.apple.iokit.IOPCIFamily.md) 2.7, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (5) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | `AppleT8160PCIe` | `apcie,t8160` |
| [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) | `APCIECoreRCGen5p1HostBridge` | `apcie-bridge` |
| [`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) | `APCIECoreRCGen5p1HostBridge` | `apcie-bridge` |
| [`/arm-io/apcie0-plce`](../devicetree/root__arm-io__apcie0-plce.md) | `APCIECoreRCGen5PLCE` | `plce,t8160` |
| [`/arm-io/apcie1-plce`](../devicetree/root__arm-io__apcie1-plce.md) | `APCIECoreRCGen5PLCE` | `plce,t8160` |

## IOKit personalities (5) [KC]

### APCIECoreRCGen5PLCE
- `CFBundleIdentifier`: `com.apple.driver.AppleT8160PCIe`
- `IOClass`: `APCIECoreRCGen5PLCE`
- `IONameMatch`: `plce,t8160`
- `IOPersonalityPublisher`: `com.apple.driver.AppleT8160PCIe`
- `IOProbeScore`: `5000`
- `IOProviderClass`: `AppleARMIODevice`

### APCIECoreRCGen5p1HostBridge
- `CFBundleIdentifier`: `com.apple.driver.AppleT8160PCIe`
- `IOClass`: `APCIECoreRCGen5p1HostBridge`
- `IONameMatch`: `apcie-bridge`
- `IOPersonalityPublisher`: `com.apple.driver.AppleT8160PCIe`
- `IOProbeScore`: `5000`
- `IOProviderClass`: `IOPCIDevice`

### AppleT8160PCIe
- `CFBundleIdentifier`: `com.apple.driver.AppleT8160PCIe`
- `IOClass`: `AppleT8160PCIe`
- `IONameMatch`: `apcie,t8160`
- `IOPersonalityPublisher`: `com.apple.driver.AppleT8160PCIe`
- `IOPlatformActiveAction`: `1500`
- `IOPlatformHaltRestartAction`: `4000`
- `IOPlatformQuiesceAction`: `4000`
- `IOProviderClass`: `AppleARMIODevice`

### RTKitPCIeTBClient0
- `CFBundleIdentifier`: `com.apple.driver.AppleT8160PCIe`
- `IOClass`: `AFKTightbeamEndpoint`
- `IONameMatch`: `com.apple.aop2.afksmplkext-0-com.apple.aop2.afksmplkext-0.ap.client-fwd`
- `IOPersonalityPublisher`: `com.apple.driver.AppleT8160PCIe`
- `IOProviderClass`: `AFKEndpointInterface`
- `port`: `0`
- `role`: `RTKitPCIeTBClient`

### RTKitPCIeTBClient1
- `CFBundleIdentifier`: `com.apple.driver.AppleT8160PCIe`
- `IOClass`: `AFKTightbeamEndpoint`
- `IONameMatch`: `com.apple.aop2.afksmplkext-1-com.apple.aop2.afksmplkext-1.ap.client-fwd`
- `IOPersonalityPublisher`: `com.apple.driver.AppleT8160PCIe`
- `IOProviderClass`: `AFKEndpointInterface`
- `port`: `1`
- `role`: `RTKitPCIeTBClient`


## C++ classes (11) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `APCIECoreRCGen5` | 0x250 | AppleEmbeddedPCIE → IOPCIHostBridge → IOPCIBridge → IOService → IORegistryEntry |
| `APCIECoreRCGen5PLCE` | 0x1d0 | ApplePLCE → IOService → IORegistryEntry |
| `APCIECoreRCGen5Port` | 0x1f68 | AppleEmbeddedPCIEPort → IOInterruptController → IOService → IORegistryEntry |
| `APCIECoreRCGen5p1` | 0x250 | APCIECoreRCGen5 → AppleEmbeddedPCIE → IOPCIHostBridge → IOPCIBridge → IOService → IORegistryEntry |
| `APCIECoreRCGen5p1HostBridge` | 0x178 | ApplePCIEHostBridge → IOPCI2PCIBridge → IOPCIBridge → IOService → IORegistryEntry |
| `APCIECoreRCGen5p1Port` | 0x1f88 | APCIECoreRCGen5Port → AppleEmbeddedPCIEPort → IOInterruptController → IOService → IORegistryEntry |
| `ApplePLCE` | 0x1c0 | IOService → IORegistryEntry |
| `ApplePLCELinkScripts` | 0x128 |  |
| `ApplePLCESequence` | 0xf0 |  |
| `AppleT8160PCIe` | 0x270 | APCIECoreRCGen5p1 → APCIECoreRCGen5 → AppleEmbeddedPCIE → IOPCIHostBridge → IOPCIBridge → IOService → IORegistryEntry |
| `AppleT8160PCIePort` | 0x1f88 | APCIECoreRCGen5p1Port → APCIECoreRCGen5Port → AppleEmbeddedPCIEPort → IOInterruptController → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00008166 off=0x007c9b50-0x007d1cb6 addr=0xfffffe00077cdb50-0xfffffe00077d5cb6 r--/r--   __TEXT            
	sz=0x000057bf off=0x007ca218-0x007cf9d7 addr=0xfffffe00077ce218-0xfffffe00077d39d7               __TEXT.__cstring          (CstringLiterals)
	sz=0x00002067 off=0x007cf9d7-0x007d1a3e addr=0xfffffe00077d39d7-0xfffffe00077d5a3e               __TEXT.__os_log           
	sz=0x00000276 off=0x007d1a40-0x007d1cb6 addr=0xfffffe00077d5a40-0xfffffe00077d5cb6               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00027d7c off=0x028878a0-0x028af61c addr=0xfffffe000988b8a0-0xfffffe00098b361c r-x/r-x   __TEXT_EXEC       
	sz=0x000275dc off=0x028878a0-0x028aee7c addr=0xfffffe000988b8a0-0xfffffe00098b2e7c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000007a0 off=0x028aee7c-0x028af61c addr=0xfffffe00098b2e7c-0xfffffe00098b361c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000298 off=0x049ccac8-0x049ccd60 addr=0xfffffe000b9d0ac8-0xfffffe000b9d0d60 rw-/rw-   __DATA            
	sz=0x000000d0 off=0x049ccac8-0x049ccb98 addr=0xfffffe000b9d0ac8-0xfffffe000b9d0b98               __DATA.__data             
	sz=0x000001c8 off=0x00000000-0x000001c8 addr=0xfffffe000b9d0b98-0xfffffe000b9d0d60               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00005ea0 off=0x0125fd58-0x01265bf8 addr=0xfffffe0008263d58-0xfffffe0008269bf8 rw-/rw-   __DATA_CONST      
	sz=0x00000048 off=0x0125fd58-0x0125fda0 addr=0xfffffe0008263d58-0xfffffe0008263da0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000048 off=0x0125fda0-0x0125fde8 addr=0xfffffe0008263da0-0xfffffe0008263de8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000053f8 off=0x0125fde8-0x012651e0 addr=0xfffffe0008263de8-0xfffffe00082691e0         __DATA_CONST.__const            
	sz=0x000002c0 off=0x012651e0-0x012654a0 addr=0xfffffe00082691e0-0xfffffe00082694a0         __DATA_CONST.__kalloc_type      
	sz=0x00000280 off=0x012654a0-0x01265720 addr=0xfffffe00082694a0-0xfffffe0008269720         __DATA_CONST.__kalloc_var       
	sz=0x000003d0 off=0x01265720-0x01265af0 addr=0xfffffe0008269720-0xfffffe0008269af0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000108 off=0x01265af0-0x01265bf8 addr=0xfffffe0008269af0-0xfffffe0008269bf8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 277 at 0x04ae8b64
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     FC1C92AB-E98E-3165-BC7B-08FD97657186
008: LC_SOURCE_VERSION           1042.40.10.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab4998 size=0x310
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleT8160PCIe`
- `CFBundleIdentifier`: `com.apple.driver.AppleT8160PCIe`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleT8160PCIe`
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
- `NSHumanReadableCopyright`: `Copyright © 2023 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleT8160PCIe.kext`
- `_PrelinkExecutableLoadAddr`: `-2198897632432`
- `_PrelinkExecutableRelativePath`: `AppleT8160PCIe`
- `_PrelinkExecutableSize`: `221210`
- `_PrelinkExecutableSourceAddr`: `-2198897632432`
- `_PrelinkKmodInfo`: `-2198828414264`

## Strings (541) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `sid < _maxSIDs`
- `(sid != 0) || !valid`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s apcie[%u:%s]::%s: %s linksts=0x%08x pcielint=0x%08x%s\n\n`
- `_readPhyLaneReg`
- `I8@?0`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Updating the MSI Vector Offset Table restore sequence\n`
- `allocateFireAndForgetBuffer`
- `createEPTeardownSequence`
- `_regIndex.port_slots != UINT8_MAX`
- `[PCIe:%u %llu ns] %s::%s Port %d Config reg index = %d\n`
- `appclk-auto-dis`
- `_constructMSITableRestoreSequence`
- `apcie-path`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Sent doorbell properties to RTKitPCIe, result=0x%08X\n\n`
- `(*offset & (bytes - 1)) == 0`
- `dtRegMapPhyIndex`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s getLinkRcvryDebugTracer buf is Null!\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Link recovery debug: 0x%llx = 0x%x\n\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Sequence table virtual  address: 0x%llx\n\n`
- `IOBufferMemoryDescriptor *ApplePLCE::createScriptIOMD(ApplePLCESequence **, unsigned int, bool)`
- `APCIECoreRCGen5p1`
- `_ltssm.mapMemory(armioProvider, index)`
- `virtual uint32_t APCIECoreRCGen5PLCE::readScratchRegister(unsigned int)`
- `site.struct ApplePLCEDoorbell`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Updating %u:%u:%u's VID/DID check sequence\n`
- `id < numRestoreSeqIDs`
- `id < numTeardownSeqIDs`
- `APCIECoreRCGen5.cpp`
- `dtRegMapPortConfigIndex`
- `lookupPerstFunction`
- `region-base`
- `void ApplePLCE::transmitDoorbellInformation()`
- `installDoorbellShmemMatchingNotification_block_invoke_2`
- `\"apcie[%u:%s]: Timeout waiting for Link Reset register: OUTS_TRANS_STS\" @%s:%d`
- `\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `_phyInterruptEventSource != nullptr`
- `Link shutdown`
- `installTightbeamClientMatchingNotification`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Fire-and-forget base PA:  %p\n\n`
- `createCfgVidDidCheckSequence`
- `restoreSequences[id]`
- `Request address is greater than 32 bits`
- `\"TB_ASSERT: \" \"(vErr == TB_ERROR_SUCCESS) && \\\"tb_message_subrange failed\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `constructPollingReadCommand`
- `\"Invalid size %u for configSpaceRMWCommand()\" @%s:%d`
- `uint64_t ApplePLCELinkScripts::calculateDoorbellAddress(IOPCIDevice *, struct ApplePLCEDoorbell *)`
- `void APCIECoreRCGen5Port::_initializeRootComplex()`
- `v24@?0Q8r^{rtkitpcietb_plce_doorbell_property_s=CCCICC}16`
- `virtual void APCIECoreRCGen5PLCE::writeScriptRun(unsigned int, uint32_t)`
- `12111112122212121212111221222111211111211111211111211212`
- `restoreDARTMappings`
- `constructRMWCommand`
- `_configRegSpace`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Link recovery debug: 0x%llx = 0x%x\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Unable to allocate buffer for link recovery debug tracer!\n`
- `dtRegMapPortIntr2AxiIndex`
- `_phyLane.mapMemory(armioProvider, index)`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s port linkRcvry Memory Map:\n`
- `linkReady_block_invoke_2`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s maximumLinkSpeed = %d\n`
- `_captureLinkSpeedDebugTracer`
- `APCIECoreRCGen5p1Port.cpp`
- `_updateRIDToSIDRestoreSequence`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Updating the restore end sequence\n`
- `_cfgSpaceMemoryMap != nullptr`
- `_commandGate != NULL`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s no property matching dict\n\n`
- `i < _numDoorbells`
- `[PCIe:%u %llu ns] %s::%s Port %d LTSSM debug reg index = %d\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Updating the RID-to-SID restore sequence\n`
- `virtual IOReturn APCIECoreRCGen5p1Port::enableLinkTraining(bool)`
- `site.APCIECoreRCGen5`
- `_dartLock != nullptr`
- `\"apcie[%u:%s]: Timeout waiting for LANE_PIPE_RESET_STATUS or LANE_UCTRL_IDLE_ACK: Were 0x%04x, 0x%04x Expected 0x%04x, 0x%04x\" @%s:%d`
- `logLinkState`
- `\"TB_ASSERT: \" \"(rtkitpcietb_plce_doorbell_property__decode(msg, &item) == TB_ERROR_SUCCESS) && \\\"failed to decode type: RTKitPCIeTB.plce_doorbell_property\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `failed to encode type: RTKitPCIeTB.plce_doorbell_property`
- `apcie-smpl-disable`
- `AFKTightbeamEndpoint`
- `void ApplePLCE::installTightbeamClientMatchingNotification()_block_invoke_2`
- `virtual void APCIECoreRCGen5Port::serializedConfigRegSpace()`
- `\"apcie[%u:%s]: ** Errata #55 ** LTSSM stuck in S_L1_IDLE\" @%s:%d`
- `_enableRASCounters`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s getLinkRcvryDebugTracer size is Null!\n`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s \n`
- `installDoorbellScripts`
- `RTKitPCIeTB_c.c`
- `implementation for smpl_ready is not present`
- `\"TB_ASSERT: \" \"(rtkitpcietb_plce_doorbell_property__v_decode(msg, &dbArray) == TB_ERROR_SUCCESS) && \\\"failed to decode type: RTKitPCIeTB.plce_doorbell_property\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `_allocateTracerMemory`
- `cfgEndSequence`
- `dtRegMapPortConfigLTSSMDebugIndex`
- `armioProvider != nullptr`
- `virtual void APCIECoreRCGen5Port::allocateConfigSpaceBuffer()`
- `_enableLinkSpeedDebugTracer`
- `_writeLTSSMDbgReg`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Unable to allocate buffer for ltssm debug tracer\n`
- `socCfgStatusStatusData`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Sent SMPL ready %u message to RTKitPCIe, response=0x%08X\n\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Reinstalling fire-and-forget script for doorbell %u\n`
- `getLinkSpeedDebugTracer`
- `\"TB_FATAL: \" \"invalid tag in '[RTKitPCIeTB.plce_doorbell_property]' metadata: 0x%x\" @%s:%d`
- `\"TB_FATAL: \" \"unrecognized selector: %llu\" @%s:%d`
- `APCIECoreRCGen5p1HostBridge`
- `apcie-plce`
- `virtual bool AppleT8160PCIe::configure(IOService *)`
- `handleErrorInterrupt`
- `_kickScriptIDAllocator->allocate(1, &scriptID) == true`
- `Multiple bad request interrupt bits set.`
- `APCIECoreRCGen5p1Port`
- `1211111212221212121211122122211121111121111121111121121222`
- `plce-link-teardown-script`
- `void ApplePLCE::configureInterrupts(IOService *)`
- `bool ApplePLCELinkScripts::isTeardownSequenceInstalled(enum teardownSeqID)`
- `site.IOBufferMemoryDescriptor *`
- `v12@?0I8`
- `_installScript`
- `createRPTeardownSequence`
- `virtual bool APCIECoreRCGen5Port::initWithAPCIeAndRegistryEntry(AppleEmbeddedPCIE *, IORegistryEntry *)`
- `_readLinkSpeedDbgReg`
- `configure`
- `port`
- `handleDoorbellShmemMatch`
- `ApplePLCESequence *ApplePLCELinkScripts::getRestoreSequence(enum restoreSeqID)`
- `void ApplePLCELinkScripts::resetRestoreSequence(enum restoreSeqID)`
- `_phyIndex < PHY_SLOTS`
- `enable-ptm`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s PTM enabled\n`
- `readStatusReg`
- `writeStatusReg`
- `_scriptIOMDs[scriptIdx]`
- `portConfigExcludedRegions != nullptr`
- `enablePortPTM`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s INTR2AXI: 0x%llx = 0x%x\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s MMIO doorbell %u using script %u\n`
- `teardownDARTMappings`
- `1`
- `phandleDictionary != nullptr`
- `smpl`
- `site.APCIECoreRCGen5p1HostBridge`
- `[PCIe:%u %llu ns] APCIECoreRCGen5PLCE[%u]::%s Link init1 script error\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Sequence table physical address: 0x%llx\n\n`
- `plce-link-init0-script`
- `installRestoreScript`
- `\"[ApplePLCELinkScripts::%s()] IOPCIDevice nub's expressCapability should always be non-zero\" @%s:%d`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s \tbaseAddress:     0x%016llX\n`
- `\"apcie[%u:%s]: RET_PIPE_RESET_EN must be 1\" @%s:%d`
- `virtual void APCIECoreRCGen5Port::_updateRIDToSIDMappings(uint32_t)`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s link speed debug tracer empty,  number speed changes: 0x%08x\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s getLinkSpeedDebugTracer size is Null!\n`
- `plce-link-restore-script`
- `_mapper`
- `\"Can't create a write command specifying %u regs\" @%s:%d`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s source address 0x%llx, destination address 0x%llx\n`
- `_enableLTSSMDebugTracer`
- `\"TB_ASSERT: \" \"(server->send_doorbell_properties != ((void*)0)) && \\\"implementation for send_doorbell_properties is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_FATAL: \" \"overflow detected when multiplying\" @%s:%d`
- `site.rtkitpcietb_plce_doorbell_property_s`
- `constructNOPCommand`
- `linkDownRecovery`
- `^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16`
- `\"PCIe link trained after Link Init1 script timeout; review PCIELINT polling duration\" @%s:%d`
- `_phyIP.mapMemory(provider, index)`
- `12111112122212121111111111211222222222221112212`
- `Unexpected`
- `void ApplePLCE::allocateFireAndForgetBuffer()`
- `void ApplePLCE::_programSequenceTable(uint16_t)`
- `\"apcie[%u:%s]: Timeout waiting for Link Reset register: PORT_STS\" @%s:%d`
- `RTKitPCIeTBClient`
- `_doneIntES != nullptr`
- `_doorbells != NULL`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s base 0x%llx = 0x%x\n`
- `site.ApplePLCESequence`
- `constructCfgEndCommand`
- `assigned-addresses`
- `[PCIe:%u %llu ns] %s::%s APCIe Common reg index = %d\n`
- `_plceLinkUpPollTimerEventSource != nullptr`
- `port-id`
- `ApplePLCE.cpp`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Fire-and-forget base DVA: %p\n\n`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Updating %u:%u:%u's restore sequence\n`
- `APCIECoreRCGen5Port.cpp`
- `_dartRequestSIDFunction != nullptr`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s port intr2Axi Memory Map:\n`
- `_linkScripts`
- `[PCIe:%u %llu ns] %s::%s phyIP Memory Map:\n`
- `reg < 16`
- `getLinkRcvryDebugTracer`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS) && \\\"failed to wrap packed buffer\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `completion block must be called before returning`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Waiting for matching PLCE service...\n\n`
- `121111121222121211111212122222211222112211111112112221111111221122122122211221`
- `B24@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{IONotifier=^^?i}16`
- `smpl-ready`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Installing script in PLCE slot %u\n`
- `bool ApplePLCELinkScripts::isRestoreSequenceInstalled(enum restoreSeqID)`
- `lane-cfg`
- `(dataBufferIndex + 1) < dataBufferCapacityInWords`
- `_seqTableMemoryMap`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Resetting script in PLCE slot %u\n`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Installing restore sequence %u\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Unable to allocate buffer for RAS counter capture\n`
- `_readLinkRcvryDbgReg`
- `\"%s:%u: REQUIRE failed: %s\" @%s:%d`
- `dtRegMapApcieCommonIndex`
- `REG_FIELD_XTRCT(APCIE_CFG_LINKSTS_N, CORE_RST_PEND)(linksts) == 1`
- `virtual void APCIECoreRCGen5Port::configMSIRange()`
- `\"TB_ASSERT: \" \"(rtkitpcietb_plce_doorbell_property__sizeof(value, &__sz) == TB_ERROR_SUCCESS) && \\\"marshal_sizeof\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `PCLE`
- `plceMatchingDictionary != nullptr`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s [%s()] Using PLCE, skipped PERST lookup\n\n`
- `virtual void APCIECoreRCGen5PLCE::writeScriptDone(unsigned int, uint32_t)`
- `_socCfgStatus.mapMemory(provider, DT_REG_MAP_PLCE_SOC_CFG_STATUS_INDEX) == true`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s no matching dict\n\n`
- `_scriptIODCs[scriptIdx]->gen64IOVMSegments(&offset, &seg64, &numSegs) == kIOReturnSuccess`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Script %u virtual address: %p\n\n`
- `_scriptIODCs`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s 0x%llx = 0x%x\n`
- `IODTResolveAddressCell(parentEntry, reg, &phys, &len) == true`
- `_apcieCoreRCGen5 != nullptr`
- `PCIE RC`
- `MSI Data Miscompare`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Link speed debug: 0x%llx = 0x%x\n`
- `APCIECoreRCGen5p1HostBridge.cpp`
- `site.IODMACommand *`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s aop2.smpl.doorbell's service cannot be cast to AFKSharedMemoryRegionBase\n\n`
- `iomd`
- `resetScript`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s  Failed to get device memory for nub %s, bar %u\n`
- `fastsim`
- `[PCIe:%u %llu ns] %s::%s Port %d INTR2AXI reg index = %d\n`
- `domain-id`
- `_sharedMemIOMD->getLength() >= (_portId + 1) * _numScripts * 4`
- `(data->getLength() % sizeof(struct PLCEDoorbellDTProp)) == 0`
- `void *ApplePLCESequence::getBytesNoCopy()`
- `APCIECoreRCGen5Port`
- `site.APCIECoreRCGen5Port`
- `\"apcie[%u:%s]: Timeout waiting for LANE_UCTRL_IDLE_ACK: Was 0x%04x Expected 0x%04x\" @%s:%d`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s LTSSM debug: 0x%llx = 0x%x\n`
- `121111121222121211111121111221111111111111111111111112122222222111211222221111111222222222222222222222222222222222212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212`
- `virtual bool APCIECoreRCGen5p1HostBridge::start(IOService *)`
- `role`
- `writeIPCEReg`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s address 0x%llx, mask 0x%x, data 0x%x\n`
- `[PCIe:%u %llu ns] %s::%s phy Memory Map:\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s getLinkSpeedDebugTracer buf is Null!\n`
- `_writeIntr2AxiReg`
- `_constructRestoreEndSequence`
- `site.APCIECoreRCGen5PLCE`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s MMIO doorbell %u: EP function %u, BAR%u, type %u, offset 0x%x\n`
- `_sequenceIOMD`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s offset 0x%llx <- data 0x%x\n`
- `failed to wrap packed buffer`
- `tb_message_subrange failed`
- `implementation for send_doorbell_properties is not present`
- `\"kAPCIE_DEBUG_LINK_ACTIVE_IN_SLP is only allowed on links with SMPL enabled\" @%s:%d`
- `[PCIe:%u %llu ns] %s::%s phy IP: 0x%llx = 0x%x\n`
- `providerNub`
- `virtual bool ApplePLCE::start(IOService *)`
- `transmitDoorbellInformation_block_invoke`
- `parentEntry`
- `perst-to-refclk-delay-us`
- `\"apcie[%u:%s]::%s: %s linksts=0x%08x pcielint=0x%08x%s\\n\" @%s:%d`
- `virtual void APCIECoreRCGen5PLCE::writeScratchRegister(unsigned int, uint32_t)`
- `doorbellProp[i].type < kApplePLCENumDoorbellTypes`
- `_doorbells[i].doorbellSequence`
- `resetTeardownScript`
- `site.AppleT8160PCIePort`
- `dataBuffer`
- `_writeLinkSpeedDbgReg`
- `failed to decode type: RTKitPCIeTB.plce_doorbell_property`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s In the doorbell notifier handler\n\n`
- `doorbell-cfg`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s address 0x%llx, data 0x%x, mask 0x%x\n`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Constructing the teardown start sequence\n`
- `_plce != nullptr`
- `_scriptIODCs[scriptIdx]`
- `constructSetAddressOffsetCommand`
- `[PCIe:%u %llu ns] %s::%s Port %d Link recovery debug reg index = %d\n`
- `\"apcie[%u:%s]: Timeout waiting for LANE_PIPE_RESET_STATUS: Was 0x%04x, Expected 0x%04x\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->smpl_ready != ((void*)0)) && \\\"implementation for smpl_ready is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `ret == kIOReturnSuccess`
- `[PCIe:%u %llu ns] %s::%s \tphysicalAddress: 0x%016llX\n`
- `_readPhyASDCUcCfgReg`
- `_socCfgIPCE.mapMemory(provider, DT_REG_MAP_PLCE_SOC_CFG_IPCE_INDEX) == true`
- `_afkClientEndpointParent != NULL`
- `_fireAndForgetIODC->gen64IOVMSegments(&offset, &seg64, &numSegs) == kIOReturnSuccess`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s AFKSharedMemoryRegionBase's IOMD is NULL\n`
- `readIPCEReg`
- `AppleT8160PCIe.cpp`
- `\"Attempt to access invalid script ID %u\" @%s:%d`
- `Link init0`
- `plce-num-scripts`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Done status: 0x%x 0x%x 0x%x\n`
- `_fireAndForgetIODC`
- `allocateDoorbellScripts`
- `121222222222222222222222222221`
- `i8@?0`
- `void ApplePLCE::restoreDARTMappings()`
- `teardownSequences[id]`
- `_regIndex.common_slots != UINT8_MAX`
- `_intr2Axi.mapMemory(armioProvider, index)`
- `(_msiVectors + _msiVectorBase) <= REG_COUNT(APCIE_CFG_MSI_VECTOR_OFFSET_TABLE_N)`
- `_readIntr2AxiReg`
- `virtual uint32_t APCIECoreRCGen5PLCE::readScriptDone(unsigned int)`
- `installTightbeamClientMatchingNotification_block_invoke_2`
- `_fireAndForgetIOMD`
- `void ApplePLCE::_installScript(uint16_t, ApplePLCESequence **, unsigned int, bool)`
- `reinstallFireAndForgetDoorbellScripts`
- `1211111111111111111111111111111122221`
- `createTeardownStartSequence`
- `dtRegMapPortLinkSpeedDebugIndex`
- `data != NULL`
- `_scriptIODCs[scriptIdx]->setMemoryDescriptor(_scriptIOMDs[scriptIdx]) == kIOReturnSuccess`
- `121111121222121211111121111221111111111111111111111112122222222111211222221111111222222222222222222222222222222222212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212212`
- `_dartReleaseSIDFunction != nullptr`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s port linkSpeed Memory Map:\n`
- `_initializeRootComplex`
- `virtual void APCIECoreRCGen5Port::linkDownRecovery()`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s ltssm debug tracer empty or too large, status 0x%08x\n`
- `_scriptIOMDs`
- `1221212`
- `void ApplePLCE::allocateDoorbellScripts()`
- `constructWordCopyCommand`
- `void ApplePLCELinkScripts::resetTeardownSequence(enum teardownSeqID)`
- `AppleT8160PCIePort`
- `AppleT8160PCIePort.cpp`
- `PCIE RC GEN4 SHADOW`
- `enableRootPort`
- `virtual bool APCIECoreRCGen5PLCE::start(IOService *)`
- `_doorbellScriptIDAllocator != nullptr`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s wrIndex %u, cpSrcIndex %u, cpDstIndex %u, dmaSrcIndex %u, dmaDstIndex %u\n`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Invalid doorbell offset (0x%x, 0x%x)\n`
- `_provider != nullptr`
- `virtual bool APCIECoreRCGen5::configure(IOService *)`
- `dtRegMapPortLinkRcvryDebugIndex`
- `apcie-plce-disable`
- `virtual void APCIECoreRCGen5p1Port::disableRootPort(bool, bool, uint32_t *)`
- `virtual uint64_t APCIECoreRCGen5PLCE::getScratchPhysAddr(unsigned int)`
- `_programSequenceTable`
- `dtRegMapPortPhyGlueIndex`
- `_linkSpeed.mapMemory(armioProvider, index)`
- `_writePhyLaneReg`
- `_readLTSSMDbgReg`
- `virtual bool APCIECoreRCGen5p1Port::initWithAPCIeAndRegistryEntry(AppleEmbeddedPCIE *, IORegistryEntry *)`
- `disableRootPort`
- `APCIECoreRCGen5PLCE.cpp`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s RTKitPCIe tightbeam client init failed\n\n`
- `_doorbells[i].kickSequence`
- `APCIECoreRCGen5`
- `I16@?0^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}8`
- `\"TB_FATAL: \" \"overflow detected when adding\" @%s:%d`
- `site.APCIECoreRCGen5p1Port`
- `virtual uint32_t APCIECoreRCGen5PLCE::readErrorStatus(unsigned int)`
- `[PCIe:%u %llu ns] APCIECoreRCGen5PLCE[%u]::%s Link restore script error\n`
- `_doorbellScriptIDAllocator->allocate(1, &scriptID) == true`
- `[PCIe:%u %llu ns] %s::%s Port %d PHY_GLUE reg index = %d\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s PHY lane: 0x%llx = 0x%x\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Link speed debug: 0x%llx = 0x%x\n\n`
- `_writeLinkRcvryDbgReg`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s No doorbell-cfg property found\n`
- `sequences[i]->getBufferedCommandCount() == 0`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Script %u physical address: %p\n\n`
- `resetRestoreScript`
- `\"Unsupported link width %u on port %d\" @%s:%d`
- `_deviceCString != NULL`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s apcie[%u:%s]::%s: %s linksts=0x%08x pcielint=0x%08x%s linkcdmsts=0x%08x (ltssm 0x%x=%s)\n\n`
- `doorbellProp[i].bar < 6`
- `site.ApplePLCE`
- `doorbellProp[i].func < 8`
- `constructWriteCommand`
- `_dartSelfFunction != nullptr`
- `APCIE Config`
- `I12@?0I8`
- `ApplePLCE`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Unable to allocate buffer for link speed debug tracer\n`
- `sequenceTable != NULL`
- `handleDoneInterrupt`
- `newIOMD`
- `void ApplePLCELinkScripts::getRMWMaskOffset(uint32_t *, uint8_t, uint32_t *, uint32_t *)`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Constructing %u:%u:%u's teardown sequence\n`
- `virtual unsigned int APCIECoreRCGen5::dtRegMapPhyIndex(uint32_t) const`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Could not find client ep\n\n`
- `doorbells != nullptr`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Installing teardown sequence %u\n`
- `NULL != addressProperty`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Creating doorbell script %u\n`
- `PCIE RC GEN5 SHADOW`
- `rcSerializingRegions != nullptr`
- `_enableLinkRcvryDebugTracer`
- `initWithAPCIeAndRegistryEntry`
- `AppleT8160PCIe`
- `region-size`
- `aop2.smpl.doorbell`
- `void ApplePLCESequence::resizeSequence()`
- `installTeardownScript`
- `createCfgRestoreSequence`
- `calculateDoorbellAddress`
- `_expressCapOffset != 0`
- `virtual uint32_t APCIECoreRCGen5PLCE::readScriptRun(unsigned int)`
- `\"%s script error (0x%x, 0x%x, 0x%x)\" @%s:%d`
- `_numDoorbellScripts <= (_numScripts - _numReservedScripts)`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s MMIO doorbell %u using kick script %u\n`
- `12111112122212121111121212222221122211221111111211222111111122112212212221`
- `virtual bool APCIECoreRCGen5::start(IOService *)`
- `_phyRegistersMemoryMap != 0`
- `site.AppleT8160PCIe`
- `[ApplePLCE::%s()] Failing matching due to boot-arg apcie-plce-disable\n`
- `start`
- `_workLoop != NULL`
- `struct ApplePLCEDoorbell *ApplePLCE::getDoorbell(uint8_t)`
- `_linkRcvry.mapMemory(armioProvider, index)`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s _expressCapOffset = 0x%x\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s expected link width = %d\n`
- `virtual void APCIECoreRCGen5p1Port::handleLinkUp(bool)`
- `\"AUS5 error: uc_wrap_out_intr_status=0x%x, uc_top_misc_reg_0=0x%x\" @%s:%d`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s \tphysicalAddress: 0x%016llX\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s port ltssm Memory Map:\n`
- `\"apcie[%u:%s]::%s: %s linksts=0x%08x pcielint=0x%08x%s linkcdmsts=0x%08x (ltssm 0x%x=%s)\\n\" @%s:%d`
- `marshal_sizeof`
- `\"TB_ASSERT: \" \"(rtkitpcietb_plce_doorbell_property__v_raw_encode(&msg, dbArray) == TB_ERROR_SUCCESS) && \\\"failed to encode type: RTKitPCIeTB.plce_doorbell_property\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `[PCIe:%u %llu ns] %s::%s \tbaseAddress:     0x%016llX\n`
- `APCIECoreRCGen5PLCE`
- `Link teardown`
- `_kickScriptIDAllocator != nullptr`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s In the tightbeam notifier handler\n\n`
- `_errorIntES != nullptr`
- `ApplePLCELinkScripts`
- `PCIE RC GEN3 SHADOW`
- `plce-link-init1-script`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Tearing down DART mappings\n\n`
- `site.APCIECoreRCGen5p1`
- `[PCIe:%u %llu ns] %s::%s PHY %d reg index = %d\n`
- `[PCIe:%u %llu ns] %s::%s Port %d Link speed debug reg index = %d\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s port phyLane Memory Map:\n`
- `\"Timeout waiting for hot reset link down\" @%s:%d`
- `Read Response Error`
- `reg < 3`
- `ApplePLCESequence`
- `ApplePLCESequence *ApplePLCELinkScripts::getTeardownSequence(enum teardownSeqID)`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s \n`
- `_captureLTSSMDebugTracer`
- `unexpected tb_error_t returned`
- `plce-link-shutdown-script`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s base address 0x%llx and %u regs\n`
- `site.ApplePLCELinkScripts`

**[__TEXT.__os_log]**

- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s no property matching dict\n\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Done status: 0x%x 0x%x 0x%x\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s MMIO doorbell %u using kick script %u\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Resetting script in PLCE slot %u\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Script %u physical address: %p\n\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Installing script in PLCE slot %u\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s getLinkSpeedDebugTracer size is Null!\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Link recovery debug: 0x%llx = 0x%x\n\n`
- `[PCIe:%u %llu ns] %s::%s \tbaseAddress:     0x%016llX\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Could not find client ep\n\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Sent doorbell properties to RTKitPCIe, result=0x%08X\n\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s MMIO doorbell %u: EP function %u, BAR%u, type %u, offset 0x%x\n`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Updating %u:%u:%u's restore sequence\n`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s \n`
- `[PCIe:%u %llu ns] %s::%s Port %d INTR2AXI reg index = %d\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Unable to allocate buffer for ltssm debug tracer\n`
- `[PCIe:%u %llu ns] APCIECoreRCGen5PLCE[%u]::%s Link restore script error\n`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s offset 0x%llx <- data 0x%x\n`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Updating %u:%u:%u's VID/DID check sequence\n`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Constructing %u:%u:%u's teardown sequence\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s \tbaseAddress:     0x%016llX\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s getLinkRcvryDebugTracer buf is Null!\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s port ltssm Memory Map:\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Unable to allocate buffer for RAS counter capture\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Unable to allocate buffer for link speed debug tracer\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s base 0x%llx = 0x%x\n`
- `[PCIe:%u %llu ns] %s::%s Port %d LTSSM debug reg index = %d\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s port linkRcvry Memory Map:\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s getLinkRcvryDebugTracer size is Null!\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s [%s()] Using PLCE, skipped PERST lookup\n\n`
- `[PCIe:%u %llu ns] APCIECoreRCGen5PLCE[%u]::%s Link init1 script error\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Fire-and-forget base DVA: %p\n\n`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Installing restore sequence %u\n`
- `[PCIe:%u %llu ns] %s::%s phy Memory Map:\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s port phyLane Memory Map:\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s apcie[%u:%s]::%s: %s linksts=0x%08x pcielint=0x%08x%s linkcdmsts=0x%08x (ltssm 0x%x=%s)\n\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Updating the RID-to-SID restore sequence\n`
- `[PCIe:%u %llu ns] %s::%s \tphysicalAddress: 0x%016llX\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s In the doorbell notifier handler\n\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s No doorbell-cfg property found\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Script %u virtual address: %p\n\n`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Invalid doorbell offset (0x%x, 0x%x)\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Link recovery debug: 0x%llx = 0x%x\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Sequence table physical address: 0x%llx\n\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s INTR2AXI: 0x%llx = 0x%x\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Fire-and-forget base PA:  %p\n\n`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s address 0x%llx, mask 0x%x, data 0x%x\n`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Installing teardown sequence %u\n`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Creating doorbell script %u\n`
- `[PCIe:%u %llu ns] %s::%s Port %d PHY_GLUE reg index = %d\n`
- `[PCIe:%u %llu ns] %s::%s Port %d Link speed debug reg index = %d\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s PTM enabled\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s getLinkSpeedDebugTracer buf is Null!\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Sequence table virtual  address: 0x%llx\n\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s no matching dict\n\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s RTKitPCIe tightbeam client init failed\n\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s 0x%llx = 0x%x\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Tearing down DART mappings\n\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s _expressCapOffset = 0x%x\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s ltssm debug tracer empty or too large, status 0x%08x\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s PHY lane: 0x%llx = 0x%x\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Waiting for matching PLCE service...\n\n`
- `[PCIe:%u %llu ns] %s::%s phyIP Memory Map:\n`
- `[PCIe:%u %llu ns] %s::%s phy IP: 0x%llx = 0x%x\n`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s base address 0x%llx and %u regs\n`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s  Failed to get device memory for nub %s, bar %u\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s expected link width = %d\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s link speed debug tracer empty,  number speed changes: 0x%08x\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Updating the restore end sequence\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Unable to allocate buffer for link recovery debug tracer!\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s AFKSharedMemoryRegionBase's IOMD is NULL\n`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s wrIndex %u, cpSrcIndex %u, cpDstIndex %u, dmaSrcIndex %u, dmaDstIndex %u\n`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s address 0x%llx, data 0x%x, mask 0x%x\n`
- `[PCIe:%u %llu ns] %s::%s Port %d Config reg index = %d\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s port intr2Axi Memory Map:\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Updating the MSI Vector Offset Table restore sequence\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s MMIO doorbell %u using script %u\n`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s source address 0x%llx, destination address 0x%llx\n`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Constructing the teardown start sequence\n`
- `[PCIe:%u %llu ns] %s::%s Port %d Link recovery debug reg index = %d\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s \tphysicalAddress: 0x%016llX\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s aop2.smpl.doorbell's service cannot be cast to AFKSharedMemoryRegionBase\n\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Reinstalling fire-and-forget script for doorbell %u\n`
- `[PCIe:%u %llu ns] %s::%s APCIe Common reg index = %d\n`
- `[PCIe:%u %llu ns] %s::%s PHY %d reg index = %d\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s port linkSpeed Memory Map:\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s apcie[%u:%s]::%s: %s linksts=0x%08x pcielint=0x%08x%s\n\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Link speed debug: 0x%llx = 0x%x\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s Link speed debug: 0x%llx = 0x%x\n\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s In the tightbeam notifier handler\n\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Sent SMPL ready %u message to RTKitPCIe, response=0x%08X\n\n`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s \n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s maximumLinkSpeed = %d\n`
- `[PCIe:%u %llu ns] apcie[%u:%s]::%s LTSSM debug: 0x%llx = 0x%x\n`
