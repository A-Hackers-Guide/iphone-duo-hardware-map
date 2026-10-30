# `com.apple.driver.AppleThunderboltUSBUpAdapter`

- Name: AppleThunderboltUSBUpAdapter
- Version: `1.0.4`
- UUID: `36A2CF8F-1627-3DEB-BE02-34ECA5C14652`
- Source version: `138.40.3.0.0`
- Depends on: [`com.apple.driver.AppleThunderboltUSBDownAdapter`](com.apple.driver.AppleThunderboltUSBDownAdapter.md) 1.0.0, [`com.apple.iokit.IOThunderboltFamily`](com.apple.iokit.IOThunderboltFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### AppleThunderboltUSBUpAdapter
- `Adapter Type`: `2097410`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltUSBUpAdapter`
- `IOClass`: `AppleThunderboltUSBUpAdapter`
- `IOPersonalityPublisher`: `com.apple.driver.AppleThunderboltUSBUpAdapter`
- `IOProbeScore`: `4096`
- `IOProviderClass`: `IOThunderboltPort`

### AppleThunderboltUSBUpAdapter,TR
- `Adapter Type`: `2097409`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltUSBUpAdapter`
- `Device ID`: `5610`
- `IOClass`: `AppleThunderboltUSBUpAdapter`
- `IOPersonalityPublisher`: `com.apple.driver.AppleThunderboltUSBUpAdapter`
- `IOProbeScore`: `6000`
- `IOProviderClass`: `IOThunderboltPort`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleThunderboltUSBUpAdapter` | 0x138 | IOThunderboltTunnelDriver → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000352d off=0x008932c0-0x008967ed addr=0xfffffe00078972c0-0xfffffe000789a7ed r--/r--   __TEXT            
	sz=0x00001901 off=0x008938e8-0x008951e9 addr=0xfffffe00078978e8-0xfffffe00078991e9               __TEXT.__cstring          (CstringLiterals)
	sz=0x00001604 off=0x008951e9-0x008967ed addr=0xfffffe00078991e9-0xfffffe000789a7ed               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00009074 off=0x029ffa40-0x02a08ab4 addr=0xfffffe0009a03a40-0xfffffe0009a0cab4 r-x/r-x   __TEXT_EXEC       
	sz=0x00008eb4 off=0x029ffa40-0x02a088f4 addr=0xfffffe0009a03a40-0xfffffe0009a0c8f4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001c0 off=0x02a088f4-0x02a08ab4 addr=0xfffffe0009a0c8f4-0xfffffe0009a0cab4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000220 off=0x049cf218-0x049cf438 addr=0xfffffe000b9d3218-0xfffffe000b9d3438 rw-/rw-   __DATA            
	sz=0x000001e8 off=0x049cf218-0x049cf400 addr=0xfffffe000b9d3218-0xfffffe000b9d3400               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9d3400-0xfffffe000b9d3438               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000928 off=0x0128ea60-0x0128f388 addr=0xfffffe0008292a60-0xfffffe0008293388 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x0128ea60-0x0128ea68 addr=0xfffffe0008292a60-0xfffffe0008292a68         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x0128ea68-0x0128ea70 addr=0xfffffe0008292a68-0xfffffe0008292a70         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000007a8 off=0x0128ea70-0x0128f218 addr=0xfffffe0008292a70-0xfffffe0008293218         __DATA_CONST.__const            
	sz=0x00000040 off=0x0128f218-0x0128f258 addr=0xfffffe0008293218-0xfffffe0008293258         __DATA_CONST.__kalloc_type      
	sz=0x000000e0 off=0x0128f258-0x0128f338 addr=0xfffffe0008293258-0xfffffe0008293338         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000050 off=0x0128f338-0x0128f388 addr=0xfffffe0008293338-0xfffffe0008293388         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 66 at 0x04aea8e8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     36A2CF8F-1627-3DEB-BE02-34ECA5C14652
008: LC_SOURCE_VERSION           138.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab6510 size=0x58
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleThunderboltUSBUpAdapter`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltUSBUpAdapter`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleThunderboltUSBUpAdapter`
- `CFBundleNumericVersion`: `17072128`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.4`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.4`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `AppleThunderboltUSBAdapters version 1.0.4, Copyright © 2018-2020 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Local-Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleThunderboltUSBAdapters.kext/PlugIns/AppleThunderboltUSBUpAdapter.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896807232`
- `_PrelinkExecutableRelativePath`: `AppleThunderboltUSBUpAdapter`
- `_PrelinkExecutableSize`: `53481`
- `_PrelinkExecutableSourceAddr`: `-2198896807232`
- `_PrelinkKmodInfo`: `-2198828404200`

## Strings (141) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - our_switch = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::createPaths - fTxPath->allocate() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setupPowerManagement - status = 0x%x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::wake\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - createPaths status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateSync\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::destroyPaths\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setPowerState - state = %ld\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setPowerState - kThunderboltPMPauseState\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - fUSBDownPort = %p fUpSwitchUSBUpPort = %p status=0x%llx \n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::suspendSync\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateAsync fIsAsleep=0x%d\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateAsync fUpSwitchUSBUpAdapter->fActivated=%d fStarted=%d status=0x%llx\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - fRxPath->activateSynchronous() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - deactivateAsync status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::suspendInternal\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::suspendInternal - suspend fRxPath\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateInternal - deactivate fRxPath\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateInternal - deactivate fTxPath\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::createPaths - ERROR: fRxPath = NULL\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::destroyPowerManagement\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::lateSleep\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::finalize - success = %d\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - fTxPath->activateSynchronous() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::createPaths - fRxPath->allocate() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::sleep\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - the_switch->getPathsDisabledForUpdate() returned %d\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - checkPathsDisabledByProtocol() returned %d\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::suspendInternal - suspend fTxPath\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - up_switch_up_adapter = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setPowerState - kThunderboltPMSleepState\n`
- `%lldus AppleThunderboltUSBUpAdapter<%p>::message - type = 0x%x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - upstream_port = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::createPaths - destroyPaths() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setPowerState - kThunderboltPMWakeState\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setPowerState - unkonwn power state %ld\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::earlyWake\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - parent_switch = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - down_adapter = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - status = 0x%x fUSBDownPort = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::finalize\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateSync\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - enableAdapter( true ) status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x:%llx:%x)::requestTerminate\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateInternal - fUSBDownAdapter->enableAdapter( false )\n`
- `%lldus AppleThunderboltUSBUpAdapter<%p>::message - type = 0x%x calling activatesync\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - fRxRequiredBandwidth = %d fRxMaximumBandwidth = %d fTxRequiredBandwidth = %d fTxMaximumBandwidth = %d\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - before setting tunnel source and dest ports, status = 0x%x fUSBDownPort = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateAsync fActivated=%d\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateInternal\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::createPaths - ERROR: fTxPath = NULL\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - upstream_parent_port = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - fActivated = true status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::free\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::suspendAsync\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::enableAdapter - enable = %d status=0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter<%p>::message - type = 0x%x calling deactivateAsync\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - fUSBDownAdapter->enableAdapter( true ) status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter::createResources status = 0x%x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateAsync fUpSwitchUSBUpAdapter->fActivated=%d fStarted=%d fUpSwitchUSBUpAdapter->fIsPendingActivation=%d\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateInternal - enableAdapter( false )\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setPowerState - return\n`

**[__TEXT.__cstring]**

- `usb_cr`
- `site.AppleThunderboltUSBUpAdapter`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - before setting tunnel source and dest ports, status = 0x%x fUSBDownPort = %p\n`
- `AppleThunderboltUSBUpAdapter.cpp`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::free\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::createPaths - destroyPaths() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::lateSleep\n`
- `%lldus Thunderbolt USB - deactivating upstream path - SRC [%d:0x%llx:0x%x] DST [%d:0x%llx:0x%x] - req_bandwidth = %d\n`
- `Thunderbolt USB - paths are disabled by protocol (%x:%llx:%x)\n`
- `%lldus AppleThunderboltUSBUpAdapter<%p>::message - type = 0x%x calling deactivateAsync\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - parent_switch = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter::createResources status = 0x%x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateAsync fUpSwitchUSBUpAdapter->fActivated=%d fStarted=%d fUpSwitchUSBUpAdapter->fIsPendingActivation=%d\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - enableAdapter( true ) status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter<%p>::message - type = 0x%x calling activatesync\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - checkPathsDisabledByProtocol() returned %d\n`
- `\"AppleThunderboltUSBUpAdapter(%x:%llx:%x)::requestTerminate - ERROR: terminatePhase1 on workloop thread not permitted.\\n\" @%s:%d`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setPowerState - unkonwn power state %ld\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - up_switch_up_adapter = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - createPaths status = 0x%08x\n`
- `AppleThunderboltUSBUpAdapter`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - status = 0x%x fUSBDownPort = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - fTxPath->activateSynchronous() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::enableAdapter - enable = %d status=0x%08x\n`
- `tb`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - our_switch = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateInternal - deactivate fRxPath\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::createPaths - ERROR: fTxPath = NULL\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setPowerState - return\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::sleep\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - upstream_parent_port = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - down_adapter = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x:%llx:%x)::requestTerminate\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateSync\n`
- `%lldus Thunderbolt USB - activating downstream path - SRC [%d:0x%llx:0x%x] DST [%d:0x%llx:0x%x] - req_bandwidth = %d\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::destroyPowerManagement\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setPowerState - state = %ld\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateInternal - fUSBDownAdapter->enableAdapter( false )\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateInternal - enableAdapter( false )\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateInternal - deactivate fTxPath\n`
- `121111121222121211122222212111111221122`
- `Thunderbolt USB - paths are disabled for update (%x:%llx:%x)\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateAsync fIsAsleep=0x%d\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::suspendInternal\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::suspendInternal - suspend fTxPath\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - the_switch->getPathsDisabledForUpdate() returned %d\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - fRxPath->activateSynchronous() status = 0x%08x\n`
- `%lldus Thunderbolt USB - activating upstream path - SRC [%d:0x%llx:0x%x] DST [%d:0x%llx:0x%x] - req_bandwidth = %d\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::suspendSync\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateInternal\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::createPaths - ERROR: fRxPath = NULL\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::destroyPaths\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setPowerState - kThunderboltPMPauseState\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - fRxRequiredBandwidth = %d fRxMaximumBandwidth = %d fTxRequiredBandwidth = %d fTxMaximumBandwidth = %d\n`
- `Paths Disabled By Protocol`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::finalize\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - deactivateAsync status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateAsync fActivated=%d\n`
- `%lldus Thunderbolt USB - deactivating downstream path - SRC [%d:0x%llx:0x%x] DST [%d:0x%llx:0x%x] - req_bandwidth = %d\n`
- `Paths Disabled For Update`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::createPaths - fTxPath->allocate() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setPowerState - kThunderboltPMWakeState\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::earlyWake\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateAsync fUpSwitchUSBUpAdapter->fActivated=%d fStarted=%d status=0x%llx\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateSync\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::createPaths - fRxPath->allocate() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::wake\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - upstream_port = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - fActivated = true status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::suspendAsync\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setPowerState - kThunderboltPMSleepState\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::finalize - success = %d\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - fUSBDownPort = %p fUpSwitchUSBUpPort = %p status=0x%llx \n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - fUSBDownAdapter->enableAdapter( true ) status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::suspendInternal - suspend fRxPath\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setupPowerManagement - status = 0x%x\n`
- `%lldus AppleThunderboltUSBUpAdapter<%p>::message - type = 0x%x\n`
