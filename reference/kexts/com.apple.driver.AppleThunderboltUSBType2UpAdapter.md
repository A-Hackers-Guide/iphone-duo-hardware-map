# `com.apple.driver.AppleThunderboltUSBType2UpAdapter`

- Name: AppleThunderboltUSBType2UpAdapter
- Version: `1.0.4`
- UUID: `AC639FE4-8A19-3FB1-AFBD-02D5179A151B`
- Source version: `138.40.3.0.0`
- Depends on: [`com.apple.driver.AppleThunderboltUSBType2DownAdapter`](com.apple.driver.AppleThunderboltUSBType2DownAdapter.md) 1.0.0, [`com.apple.iokit.IOThunderboltFamily`](com.apple.iokit.IOThunderboltFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleThunderboltUSBType2UpAdapter
- `Adapter Type`: `2162946`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltUSBType2UpAdapter`
- `IOClass`: `AppleThunderboltUSBType2UpAdapter`
- `IOPersonalityPublisher`: `com.apple.driver.AppleThunderboltUSBType2UpAdapter`
- `IOProbeScore`: `4096`
- `IOProviderClass`: `IOThunderboltPort`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleThunderboltUSBType2UpAdapter` | 0x130 | IOThunderboltTunnelDriverType2 → IOThunderboltTunnelDriver → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000442e off=0x0088ee90-0x008932be addr=0xfffffe0007892e90-0xfffffe00078972be r--/r--   __TEXT            
	sz=0x0000206b off=0x0088f4b8-0x00891523 addr=0xfffffe00078934b8-0xfffffe0007895523               __TEXT.__cstring          (CstringLiterals)
	sz=0x00001d9b off=0x00891523-0x008932be addr=0xfffffe0007895523-0xfffffe00078972be               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0000a404 off=0x029f5630-0x029ffa34 addr=0xfffffe00099f9630-0xfffffe0009a03a34 r-x/r-x   __TEXT_EXEC       
	sz=0x0000a254 off=0x029f5630-0x029ff884 addr=0xfffffe00099f9630-0xfffffe0009a03884          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001b0 off=0x029ff884-0x029ffa34 addr=0xfffffe0009a03884-0xfffffe0009a03a34          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000220 off=0x049ceff8-0x049cf218 addr=0xfffffe000b9d2ff8-0xfffffe000b9d3218 rw-/rw-   __DATA            
	sz=0x000001e8 off=0x049ceff8-0x049cf1e0 addr=0xfffffe000b9d2ff8-0xfffffe000b9d31e0               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9d31e0-0xfffffe000b9d3218               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000998 off=0x0128e0c8-0x0128ea60 addr=0xfffffe00082920c8-0xfffffe0008292a60 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x0128e0c8-0x0128e0d0 addr=0xfffffe00082920c8-0xfffffe00082920d0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x0128e0d0-0x0128e0d8 addr=0xfffffe00082920d0-0xfffffe00082920d8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000828 off=0x0128e0d8-0x0128e900 addr=0xfffffe00082920d8-0xfffffe0008292900         __DATA_CONST.__const            
	sz=0x00000040 off=0x0128e900-0x0128e940 addr=0xfffffe0008292900-0xfffffe0008292940         __DATA_CONST.__kalloc_type      
	sz=0x000000d8 off=0x0128e940-0x0128ea18 addr=0xfffffe0008292940-0xfffffe0008292a18         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000048 off=0x0128ea18-0x0128ea60 addr=0xfffffe0008292a18-0xfffffe0008292a60         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 63 at 0x04aea7ec
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     AC639FE4-8A19-3FB1-AFBD-02D5179A151B
008: LC_SOURCE_VERSION           138.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab64b0 size=0x60
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleThunderboltUSBType2UpAdapter`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltUSBType2UpAdapter`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleThunderboltUSBType2UpAdapter`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleThunderboltUSBAdapters.kext/PlugIns/AppleThunderboltUSBType2UpAdapter.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896824688`
- `_PrelinkExecutableRelativePath`: `AppleThunderboltUSBType2UpAdapter`
- `_PrelinkExecutableSize`: `62442`
- `_PrelinkExecutableSourceAddr`: `-2198896824688`
- `_PrelinkKmodInfo`: `-2198828404744`

## Strings (172) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `\"AppleThunderboltUSBType2UpAdapter(%x:%llx:%x)::requestTerminate - ERROR: terminatePhase1 on workloop thread not permitted.\\n\" @%s:%d`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal2 fUSBType2Port=0x%x status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - fActivated = true status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateInternal - enableAdapter( false )\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::configureActiveLinkRate - data = 0x%lx status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::start bootargs=0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start - fRxRequiredBandwidth = %d fRxMaximumBandwidth = %d fTxRequiredBandwidth = %d fTxMaximumBandwidth = %d\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal1 status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setBundleWeight - data = 0x%lx fPortCount = 0x%lx status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setupPowerManagement - status = 0x%x\n`
- `tbusb`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - fTxPath->activateSynchronous() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::suspendInternal - suspend fTxPath\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateInternal - deactivate fRxPath status = 0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateInternal - deactivate fTxPath status = 0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - Rx path is using Dedicated FC\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - Rx path is using Shared FC\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setPowerState - unkonwn power state %ld\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateSync\n`
- `%lldus Thunderbolt USB Type2 - activating downstream path - SRC [%d:0x%llx:0x%x] DST [%d:0x%llx:0x%x] - req_bandwidth = %d\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal-final status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setBundleWeight0 - status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter<%p>::message - type = 0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter::createResources status = 0x%x\n`
- `%lldus Thunderbolt USB Type2 - activating upstream path - SRC [%d:0x%llx:0x%x] DST [%d:0x%llx:0x%x] - req_bandwidth = %d\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateInternal - fUSBType2DownAdapter->enableAdapter( false )\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::configureLinkCommandsAggregation\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::enableAdapter - findCapability failed status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start - down_adapter = %p\n`
- `Paths Disabled For Update`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - fRxPath->activateSynchronous() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateSync\n`
- `%lldus Thunderbolt USB Type2 - deactivating upstream path - SRC [%d:0x%llx:0x%x] DST [%d:0x%llx:0x%x] - req_bandwidth = %d\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - fRxPath->allocate() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::sleep\n`
- `AppleThunderboltUSBType2UpAdapter`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::finalize - success = %d\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - fUSBType2DownAdapter->enableAdapter( true ) status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - deactivateAsync status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::suspendInternal\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - fTxPath->allocate() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - destroyPaths() status = 0x%08x\n`
- `Paths Disabled By Protocol`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x:%llx:%x)::requestTerminate\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - enableAdapter( ) status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::enableAdapter - enable = %d status=0x%08x fCurrentPortIndex=0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::destroyPowerManagement\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::earlyWake waiting for all clients to be awake\n`
- `%lldus Thunderbolt USB Type2 - paths are disabled by protocol (%x:%llx:%x)\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateAsync\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - ERROR: fRxPath = NULL\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setPowerState - return\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::free\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::suspendSync\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::suspendInternal - suspend fRxPath\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setPowerState - kThunderboltPMWakeState\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setPowerState - state = %ld\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setPowerState - kThunderboltPMSleepState\n`
- `%lldus AppleThunderboltUSBType2UpAdapter<%p>::message - type = 0x%x calling activateSync with fUSBType2Port=0x%x\n`
- `%lldus Thunderbolt USB Type2 - deactivating downstream path - SRC [%d:0x%llx:0x%x] DST [%d:0x%llx:0x%x] - req_bandwidth = %d\n`
- `usbtype2_cr`
- `site.AppleThunderboltUSBType2UpAdapter`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start - parent_switch = %p\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateAsync status= 0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - configureActiveLinkRate( ) status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateInternal fUSBType2Port=0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::getPortCount1 - status=0x%08x data=0x%lx\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start - status = 0x%x fUSBType2DownPort = %p\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - Tx path is using Dedicated FC\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - Tx path is using Shared FC\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::destroyPaths\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::wake\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::finalize\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - createPaths status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::configureLinkCommandsAggregation - downsteramPortDepth = 0x%lx upstreamPortDepth = 0x%lx status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::getPortCount0 - status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::earlyWake\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start - checkPathsDisabledByProtocol() returned %d\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal0 fUSBType2Port=0x%x status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::suspendAsync\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateAsync\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::configureLinkCommandsAggregation - mask = 0x%lx status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setPowerState - kThunderboltPMPauseState\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::lateSleep\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start - the_switch->getPathsDisabledForUpdate() returned %d\n`
- `AppleThunderboltUSBType2UpAdapter.cpp`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - ERROR: fTxPath = NULL\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::getPortCount - data = 0x%lx fPortCount = 0x%lx status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter<%p>::message - type = 0x%x calling deactivateSync\n`
- `12111112122212121112222221111111222222`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start - fUSBType2DownPort = %p\n`
- `%lldus Thunderbolt USB - paths are disabled for update (%x:%llx:%x)\n`

**[__TEXT.__os_log]**

- `%lldus Thunderbolt USB - paths are disabled for update (%x:%llx:%x)\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::suspendAsync\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - Tx path is using Dedicated FC\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - Rx path is using Shared FC\n`
- `%lldus AppleThunderboltUSBType2UpAdapter<%p>::message - type = 0x%x calling activateSync with fUSBType2Port=0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setPowerState - kThunderboltPMWakeState\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::configureLinkCommandsAggregation - downsteramPortDepth = 0x%lx upstreamPortDepth = 0x%lx status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start - fRxRequiredBandwidth = %d fRxMaximumBandwidth = %d fTxRequiredBandwidth = %d fTxMaximumBandwidth = %d\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::finalize - success = %d\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal0 fUSBType2Port=0x%x status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal1 status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - createPaths status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateInternal - fUSBType2DownAdapter->enableAdapter( false )\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setPowerState - kThunderboltPMSleepState\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - enableAdapter( ) status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start - fUSBType2DownPort = %p\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateInternal - deactivate fTxPath status = 0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - fTxPath->allocate() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setBundleWeight0 - status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setBundleWeight - data = 0x%lx fPortCount = 0x%lx status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter<%p>::message - type = 0x%x calling deactivateSync\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start - down_adapter = %p\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::finalize\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::free\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateInternal fUSBType2Port=0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateInternal - enableAdapter( false )\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::sleep\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::lateSleep\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start - checkPathsDisabledByProtocol() returned %d\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - fActivated = true status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::getPortCount0 - status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - fUSBType2DownAdapter->enableAdapter( true ) status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - configureActiveLinkRate( ) status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::destroyPaths\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::getPortCount - data = 0x%lx fPortCount = 0x%lx status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::suspendInternal - suspend fRxPath\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateInternal - deactivate fRxPath status = 0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setupPowerManagement - status = 0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateAsync\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - deactivateAsync status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::suspendInternal - suspend fTxPath\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - fRxPath->allocate() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - destroyPaths() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::configureLinkCommandsAggregation - mask = 0x%lx status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - Rx path is using Dedicated FC\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setPowerState - kThunderboltPMPauseState\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::wake\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::earlyWake waiting for all clients to be awake\n`
- `%lldus Thunderbolt USB Type2 - paths are disabled by protocol (%x:%llx:%x)\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal-final status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::suspendSync\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateSync\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - ERROR: fRxPath = NULL\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::getPortCount1 - status=0x%08x data=0x%lx\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x:%llx:%x)::requestTerminate\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - fRxPath->activateSynchronous() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::enableAdapter - enable = %d status=0x%08x fCurrentPortIndex=0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setPowerState - return\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start - the_switch->getPathsDisabledForUpdate() returned %d\n`
- `%lldus AppleThunderboltUSBType2UpAdapter::createResources status = 0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateAsync status= 0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::configureLinkCommandsAggregation\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::enableAdapter - findCapability failed status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::configureActiveLinkRate - data = 0x%lx status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::destroyPowerManagement\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::suspendInternal\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateAsync\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - ERROR: fTxPath = NULL\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - Tx path is using Shared FC\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setPowerState - state = %ld\n`
- `%lldus AppleThunderboltUSBType2UpAdapter<%p>::message - type = 0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start - status = 0x%x fUSBType2DownPort = %p\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateSync\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal2 fUSBType2Port=0x%x status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setPowerState - unkonwn power state %ld\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start - parent_switch = %p\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - fTxPath->activateSynchronous() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::earlyWake\n`
