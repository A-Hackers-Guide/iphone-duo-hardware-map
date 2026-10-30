# `com.apple.driver.AppleThunderboltPCIUpAdapter`

- Name: AppleThunderboltPCIUpAdapter
- Version: `4.1.1`
- UUID: `63075BEA-2355-3F1B-842D-168489D51182`
- Source version: `443.40.2.0.0`
- Depends on: [`com.apple.driver.AppleThunderboltPCIDownAdapter`](com.apple.driver.AppleThunderboltPCIDownAdapter.md) 1.0.0, [`com.apple.iokit.IOPCIFamily`](com.apple.iokit.IOPCIFamily.md) 1.0.0b1, [`com.apple.iokit.IOThunderboltFamily`](com.apple.iokit.IOThunderboltFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleThunderboltPCIUpAdapter
- `Adapter Type`: `1048834`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltPCIUpAdapter`
- `IOClass`: `AppleThunderboltPCIUpAdapter`
- `IOPersonalityPublisher`: `com.apple.driver.AppleThunderboltPCIUpAdapter`
- `IOProbeScore`: `4096`
- `IOProviderClass`: `IOThunderboltPort`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleThunderboltPCIUpAdapter` | 0x208 | IOThunderboltTunnelDriver → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000487e off=0x00888940-0x0088d1be addr=0xfffffe000788c940-0xfffffe00078911be r--/r--   __TEXT            
	sz=0x000042a6 off=0x00888f18-0x0088d1be addr=0xfffffe000788cf18-0xfffffe00078911be               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x0001710c off=0x029db110-0x029f221c addr=0xfffffe00099df110-0xfffffe00099f621c r-x/r-x   __TEXT_EXEC       
	sz=0x00016ddc off=0x029db110-0x029f1eec addr=0xfffffe00099df110-0xfffffe00099f5eec          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000330 off=0x029f1eec-0x029f221c addr=0xfffffe00099f5eec-0xfffffe00099f621c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000258 off=0x049ceba0-0x049cedf8 addr=0xfffffe000b9d2ba0-0xfffffe000b9d2df8 rw-/rw-   __DATA            
	sz=0x00000220 off=0x049ceba0-0x049cedc0 addr=0xfffffe000b9d2ba0-0xfffffe000b9d2dc0               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9d2dc0-0xfffffe000b9d2df8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000be0 off=0x0128c410-0x0128cff0 addr=0xfffffe0008290410-0xfffffe0008290ff0 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x0128c410-0x0128c418 addr=0xfffffe0008290410-0xfffffe0008290418         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x0128c418-0x0128c420 addr=0xfffffe0008290418-0xfffffe0008290420         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000948 off=0x0128c420-0x0128cd68 addr=0xfffffe0008290420-0xfffffe0008290d68         __DATA_CONST.__const            
	sz=0x00000040 off=0x0128cd68-0x0128cda8 addr=0xfffffe0008290d68-0xfffffe0008290da8         __DATA_CONST.__kalloc_type      
	sz=0x00000198 off=0x0128cda8-0x0128cf40 addr=0xfffffe0008290da8-0xfffffe0008290f40         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000b0 off=0x0128cf40-0x0128cff0 addr=0xfffffe0008290f40-0xfffffe0008290ff0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 124 at 0x04aea4c4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     63075BEA-2355-3F1B-842D-168489D51182
008: LC_SOURCE_VERSION           443.40.2.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab6388 size=0xc8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleThunderboltPCIUpAdapter`
- `CFBundleGetInfoString`: `AppleThunderboltPCIAdapters version 4.1.1, Copyright © 2009-2020 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltPCIUpAdapter`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleThunderboltPCIUpAdapter`
- `CFBundleNumericVersion`: `68255744`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `4.1.1`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `4.1.1`
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
- `OSBundleRequired`: `Local-Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleThunderboltPCIAdapters.kext/PlugIns/AppleThunderboltPCIUpAdapter.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896850624`
- `_PrelinkExecutableRelativePath`: `AppleThunderboltPCIUpAdapter`
- `_PrelinkExecutableSize`: `116674`
- `_PrelinkExecutableSourceAddr`: `-2198896850624`
- `_PrelinkKmodInfo`: `-2198828405856`

## Strings (210) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%lldus AppleThunderboltPCIUpAdapter(%x:%llx:%x)::preAdapterEnable\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::destroyPowerManagement\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - first port, link is lateral\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::waitForDownAdapters - route = 0x%llx port = 0x%x - waiting\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::destroyPaths\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::pathActivationCallback - fRxPath status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::startActivatingFindDownAdapterPCICapability\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findUpstreamParentPCIDevice - status = 0x%08x parent_pci_device = %p\n`
- `IOPCIDevice`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::beginPathRouting - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath - use new path, same bandwidth but a better source port\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::pathActivationCallback - fTxPath status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter(%x:%llx:%x)::preAdapterEnable - enable extended encapsulation on downstream port - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::processDownAdapterEnableWriteResults - status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::startPCICorrelation (2) - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::startDeactivatingFindDownAdapterPCICapability\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::processUpAdapterResetEnableWriteResults - status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::start - (1) fRxRequiredBandwidth = %d fRxMaximumBandwidth = %d fTxRequiredBandwidth = %d fTxMaximumBandwidth = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - port is too far upstream - discard\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath - free_upstream_bandwidth = %d free_downstream_bandwidth = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter::preAdapterEnable - lc2 offset = 0x%llx link_control_2 = 0x%x\n`
- `AppleThunderboltPCIUpAdapter - route = 0x%llx PCI link active time %llu ms status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter(%x:%llx:%x)::finishDeactivateContext - we're deactivated\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - found a loop, ignoring next port\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::start - the_switch->getPathsDisabledForUpdate() returned %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::finalize - success = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath ------------------------- \n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::setupPaths - status = 0x%x fState = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::activatePaths - status = 0x%x fState = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::startPCICorrelation (1) - set correlation properties - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>[%u:0x%llx:0x%x]::wake - fState = %d\n`
- `AppleThunderboltPCIUpAdapter.cpp`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::start - IONVRAM not available\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::waitForDownAdapters\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::processActivatingFindDownAdapterPCICapabilityResults - fPCIDownAdapter->getPCICapabilityOffset() = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::postAdapterEnable - waiting for PCI link active indication\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::lateSleep - fState = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::earlyWakeDelay - delay %lld ms\n`
- `%lldus AppleThunderboltPCIUpAdapter::postAdapterEnable\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::pathDeactivationCallback - fTxPath status = 0x%x \n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::wake\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::syncActivate - waiting on activation\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::start - (2) fRxRequiredBandwidth = %d fRxMaximumBandwidth = %d fTxRequiredBandwidth = %d fTxMaximumBandwidth = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::configCommandCallback - status = 0x%x, command = %p\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findExistingPaths - ERROR only found some paths\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - port is downstream - discard\n`
- `TBTFlags`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findUpstreamParentPCIDevice - fPCIDownAdapter = %p\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::startDeactivatingFindUpAdapterPCICapability\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findExistingPaths - fPCIDownAdapter = %p, status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - even port index\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::waitForDownAdapters - route = 0x%llx port = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath - downstream\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath - use new path, longest\n`
- `%lldus AppleThunderboltPCIUpAdapter::startPreAdapterEnable\n`
- `%lldus Thunderbolt PCI - activating downstream path - SRC [%d:0x%llx:0x%x] DST [%d:0x%llx:0x%x] - req_bandwidth = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - add port route = 0x%llx port = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - next_switch = 0x%llx check_switch = 0x%llx\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::createPaths - fTxPath %p\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::startPCICorrelation (1) - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::processDeactivatingFindUpAdapterPCICapabilityResults - status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::setPowerState - kThunderboltPMSleepState\n`
- `12111112122212121112222221111111111112222112211211221122122212122`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::start - status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getExistingPortList - existing_port_list = %p status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath - fRxMaximumBandwidth = %d fTxMaximumBandwidth = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::activatePaths - fTxPath status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findPCIChildFromDevice - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::processDeactivatingFindUpAdapterPCICapabilityResults - fPCICapabilityOffset = 0x%x\n`
- `Thunderbolt PCI - paths are disabled by protocol (%x:%llx:%x)\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findCapabilityCommandCallback - status = 0x%x, command = %p\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findCandidatePaths ------------------------- \n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath - use new path, better ideal bandwidth\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::processActivatingFindDownAdapterPCICapabilityResults - status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findUpstreamParentPCIDevice - status = 0x%08x parent_path = %p\n`
- `%lldus TBT Timing - PCI Up adapter %p driver start\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath - use new path, already ideal, but a better source port\n`
- `%lldus AppleThunderboltPCIUpAdapter::preAdapterEnable - new link_control_2 = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::setPCIAdapterBusyState - decrement scan count (2), balances increment scan count (2)\n`
- `%lldus AppleThunderboltPCIUpAdapter(%x:%llx:%x)::startPreAdapterDisable\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::setPowerState - unkonwn power state %ld\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::pause\n`
- `site.AppleThunderboltPCIUpAdapter`
- `%lldus AppleThunderboltPCIUpAdapter(%x:%llx:%x)::requestTerminate\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::createPaths - fRxPath %p\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::startUpAdapterResetEnableWrite - packet = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter(%x:%llx:%x)::startPreAdapterDisable - unable to dispatch\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::earlyWakeDelay - fEnabledTimeStamp = %lld ms timestamp = %lld ms\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::start - could not create NVRAM /options handle\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - port has a peer - route = 0x%llx port = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter::preAdapterEnable\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::finishActivate - fState = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::earlyWakeDelay - done\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::waitForDownAdapters - we're waiting for down adapters - let pause continue\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::setPowerState - kThunderboltPMPauseState\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::finalize - fState = %d\n`
- `pcie_cr_null`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::processActivatingFindUpAdapterPCICapabilityResults - fPCICapabilityOffset = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::postAdapterEnable - up adapter poll results : %llu ms status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter(%x:%llx:%x)::preAdapterEnable - disable extended encapsulation on downstream port - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::setupPowerManagement - status = 0x%x\n`
- `Paths Disabled By Protocol`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findExistingPaths - down_adapter = %p\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - switch = %p 0x%llx port = %p 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter::postAdapterEnable - lc2 offset = 0x%llx link_control_2 = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::finishActivate - timestamp = %lld ms\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::processDownAdapterDisableWriteResults - status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter(%x:%llx:%x)::finishDeactivateContext - we're deactivated - let pause continue\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::setPowerState - state = %ld\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath - use new path, better worst bandwidth\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath - Best Path ------------------------- \n`
- `Tunnel Endpoint Device Model ID`
- `%lldus AppleThunderboltPCIUpAdapter(%x:%llx:%x)::finishDeactivate - status = 0x%08x\n`
- `status`
- `%lldus AppleThunderboltPCIUpAdapter(%x:%llx:%x)::finishDeactivateContext - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::sleep\n`
- `AppleThunderboltPCIUpAdapter`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - port is upstream - route = 0x%llx port = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath - test_free_upstream_bandwidth = %d test_free_downstream_bandwidth = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::earlyWake\n`
- `tbpciwd`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - port is over internal link\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath - upstream\n`
- `%lldus TBT Timing - PCI Up adapter %p activate done\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findPCIChildFromDeviceFunction - parent_device = %p\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::upstreamPCIDeviceNotification - newService = %p name = %s\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::processDeactivatingFindDownAdapterPCICapabilityResults - status = 0x%x\n`
- `IONVRAM`
- `tbt-options`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findExistingPaths - couldn't find fRxPath\n`
- `%lldus AppleThunderboltPCIUpAdapter::postAdapterEnable - new link_control_2 = 0x%x\n`
- `PCI Entry ID`
- `Thunderbolt Entry ID`
- `\"AppleThunderboltPCIUpAdapter(%x:%llx:%x)::finishDeactivate - ERROR: context = %p queue = %p\\n\" @%s:%d`
- `%lldus AppleThunderboltPCIUpAdapter(%x:%llx:%x)::finishDeactivateContext - we're deactivated - let termination complete\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::start\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - found upstream primary lane - discard\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath - status = 0x%08x\n`
- `pcie_cr_adap`
- `%lldus AppleThunderboltPCIUpAdapter(%x:%llx:%x)::preAdapterEnable - enable extended encapsulation on upstream port - status = 0x%08x\n`
- `%lldus Thunderbolt PCI - activating upstream path - SRC [%d:0x%llx:0x%x] DST [%d:0x%llx:0x%x] - req_bandwidth = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::finishActivate - we're activated - let pause continue\n`
- `PCI Path`
- `%lldus AppleThunderboltPCIUpAdapter<%p>[%u:0x%llx:0x%x]::findExistingPaths - we're asleep, continue when we wake\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findCandidatePaths - path %d - route = 0x%llx port = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath - path %d - route = 0x%llx port = 0x%x hw_bw = %d max_alloc_bw = %d max_bw = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::finishActivate - status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::finishActivate - we're activated\n`
- `Thunderbolt Path`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::syncDeactivate - waiting on deactivation - fState = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::processDeactivatingFindDownAdapterPCICapabilityResults - fPCIDownAdapter->getPCICapabilityOffset() = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::allocatePaths\n`
- `/options`
- `Thunderbolt PCI - paths are disabled for update (%x:%llx:%x)\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - (2) add port route = 0x%llx port = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::setPCIAdapterBusyState - increment scan count (2), balanced by decrement scan count (2)\n`
- `%lldus AppleThunderboltPCIUpAdapter(%x:%llx:%x)::preAdapterEnable - disable extended encapsulation on upstream port - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::processUpAdapterDisableWriteResults - status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::startActivatingFindUpAdapterPCICapability\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::finishActivate - fDeactivationRequested - begin deactivation\n`
- `Tunnel Endpoint Device Vendor ID`
- `%lldus Thunderbolt PCI - deactivating upstream path - SRC [%d:0x%llx:0x%x] DST [%d:0x%llx:0x%x] - req_bandwidth = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::setPowerState - kThunderboltPMWakeState\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::setPowerState - return\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findExistingPaths - found existing paths\n`
- `State`
- `Peer Port Number`
- `pathcr`
- `%lldus TBT Timing - PCI Up adapter %p activate begin\n`
- `%lldus AppleThunderboltPCIUpAdapter::postAdapterEnable - delay end\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::startUpAdapterDisableWrite - packet = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::pathDeactivationCallback - fRxPath status = 0x%x \n`
- `\"AppleThunderboltPCIUpAdapter(%x:%llx:%x)::requestTerminate - ERROR: terminatePhase1 on workloop thread not permitted.\\n\" @%s:%d`
- `%lldus AppleThunderboltPCIUpAdapter::createResources status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findExistingPaths - ERROR found no paths\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getExistingPortList\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::upstreamPCIDeviceNotification - newService = %p name = %s - FOUND!\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::deactivatePaths\n`
- `Paths Disabled For Update`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::start - checkPathsDisabledByProtocol() returned %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findCandidatePaths\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::beginPathRouting\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath (1) - temp_status = 0x%08x\n`
- `%lldus Thunderbolt PCI - deactivating downstream path - SRC [%d:0x%llx:0x%x] DST [%d:0x%llx:0x%x] - req_bandwidth = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::free\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath (2) - temp_status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::startDownAdapterEnableWrite - packet = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter::startPostAdapterEnable\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::pathDeactivationCallback - status = 0x%x path = %p\n`
- `tb`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - port has a peer - route = 0x%llx port = 0x%x next_port = %p\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath (3) - temp_status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::activatePaths - fRxPath status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::didPause - let setPowerState continue\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::earlyWakeDelay - fThunderboltWakeDelay = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::start - fRxRequiredBandwidth = %d fRxMaximumBandwidth = %d fTxRequiredBandwidth = %d fTxMaximumBandwidth = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - odd port index\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - port is over secondary - discard\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>[%u:0x%llx:0x%x]::waitForDownAdapters - we're asleep, continue when we wake\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::waitForDownAdapters - exit\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath - path %d - route = 0x%llx port = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::processActivatingFindUpAdapterPCICapabilityResults - status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::finishActivate - we're activated - let termination complete\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findExistingPaths - fProviderPort = %p, up_paths count = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::allocatePaths - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::startUpAdapterEnableWrite - packet = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::processUpAdapterEnableWriteResults - status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter::postAdapterEnable - delay start\n`
- `Tunnel Endpoint GUID`
