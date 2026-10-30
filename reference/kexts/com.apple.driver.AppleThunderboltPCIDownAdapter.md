# `com.apple.driver.AppleThunderboltPCIDownAdapter`

- Name: AppleThunderboltPCIDownAdapter
- Version: `4.1.1`
- UUID: `98CCC22E-F186-3DFA-9564-D97074A55639`
- Source version: `443.40.2.0.0`
- Depends on: [`com.apple.driver.AppleEmbeddedPCIE`](com.apple.driver.AppleEmbeddedPCIE.md) 1.0.0, [`com.apple.iokit.IOPCIFamily`](com.apple.iokit.IOPCIFamily.md) 1.0.0b1, [`com.apple.iokit.IOThunderboltFamily`](com.apple.iokit.IOThunderboltFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (3) [KC]

### AppleThunderboltPCIDownAdapter
- `Adapter Type`: `1048833`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltPCIDownAdapter`
- `IOClass`: `AppleThunderboltPCIDownAdapter`
- `IOPersonalityPublisher`: `com.apple.driver.AppleThunderboltPCIDownAdapter`
- `IOProbeScore`: `4096`
- `IOProviderClass`: `IOThunderboltPort`

### AppleThunderboltPCIDownAdapterType5
- `Adapter Type`: `1048833`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltPCIDownAdapter`
- `Device ID`: `0x00002000&0x0000ff00`
- `IOClass`: `AppleThunderboltPCIDownAdapterType5`
- `IOPersonalityPublisher`: `com.apple.driver.AppleThunderboltPCIDownAdapter`
- `IOProbeScore`: `8192`
- `IOProviderClass`: `IOThunderboltPort`
- `Vendor ID`: `1452`

### AppleThunderboltPCIDownAdapterType5Compatible
- `Adapter Type`: `1048833`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltPCIDownAdapter`
- `Device ID`: `1`
- `IOClass`: `AppleThunderboltPCIDownAdapterType5`
- `IOPersonalityPublisher`: `com.apple.driver.AppleThunderboltPCIDownAdapter`
- `IOProbeScore`: `8192`
- `IOProviderClass`: `IOThunderboltPort`
- `Vendor ID`: `2599`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleThunderboltPCIDownAdapter` | 0x128 | IOThunderboltTunnelDriver → IOService → IORegistryEntry |
| `AppleThunderboltPCIDownAdapterType5` | 0x130 | AppleThunderboltPCIDownAdapter → IOThunderboltTunnelDriver → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000018cd off=0x00887070-0x0088893d addr=0xfffffe000788b070-0xfffffe000788c93d r--/r--   __TEXT            
	sz=0x000012f5 off=0x00887648-0x0088893d addr=0xfffffe000788b648-0xfffffe000788c93d               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00005260 off=0x029d5eb0-0x029db110 addr=0xfffffe00099d9eb0-0xfffffe00099df110 r-x/r-x   __TEXT_EXEC       
	sz=0x00005000 off=0x029d5eb0-0x029daeb0 addr=0xfffffe00099d9eb0-0xfffffe00099deeb0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000260 off=0x029daeb0-0x029db110 addr=0xfffffe00099deeb0-0xfffffe00099df110          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x049cea78-0x049ceba0 addr=0xfffffe000b9d2a78-0xfffffe000b9d2ba0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049cea78-0x049ceb40 addr=0xfffffe000b9d2a78-0xfffffe000b9d2b40               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b9d2b40-0xfffffe000b9d2ba0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001210 off=0x0128b200-0x0128c410 addr=0xfffffe000828f200-0xfffffe0008290410 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x0128b200-0x0128b210 addr=0xfffffe000828f200-0xfffffe000828f210         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x0128b210-0x0128b220 addr=0xfffffe000828f210-0xfffffe000828f220         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000f90 off=0x0128b220-0x0128c1b0 addr=0xfffffe000828f220-0xfffffe00082901b0         __DATA_CONST.__const            
	sz=0x00000080 off=0x0128c1b0-0x0128c230 addr=0xfffffe00082901b0-0xfffffe0008290230         __DATA_CONST.__kalloc_type      
	sz=0x00000130 off=0x0128c230-0x0128c360 addr=0xfffffe0008290230-0xfffffe0008290360         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000b0 off=0x0128c360-0x0128c410 addr=0xfffffe0008290360-0xfffffe0008290410         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 98 at 0x04aea33c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     98CCC22E-F186-3DFA-9564-D97074A55639
008: LC_SOURCE_VERSION           443.40.2.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab6320 size=0x68
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleThunderboltPCIDownAdapter`
- `CFBundleGetInfoString`: `AppleThunderboltPCIAdapters version 4.1.1, Copyright © 2009-2020 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltPCIDownAdapter`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleThunderboltPCIDownAdapter`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleThunderboltPCIAdapters.kext/PlugIns/AppleThunderboltPCIDownAdapter.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896856976`
- `_PrelinkExecutableRelativePath`: `AppleThunderboltPCIDownAdapter`
- `_PrelinkExecutableSize`: `32357`
- `_PrelinkExecutableSourceAddr`: `-2198896856976`
- `_PrelinkKmodInfo`: `-2198828406152`

## Strings (67) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%lldus AppleThunderboltPCIDownAdapter<%p>::setupRootPCICorrelationPath - eeprom - status = 0x%0x port number = %d\n`
- `IOPCIDevice`
- `AAPL,phandle`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::lateSleep\n`
- `AppleThunderboltPCIDownAdapterType5`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath - phandle_func_object = %p\n`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath - phandle_dictionary = %p status = 0x%08x\n`
- `Thunderbolt Path`
- `%lldus AppleThunderboltPCIDownAdapter::setupRootPCICorrelationPath - Disabled?!?\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::setupRootPCICorrelationPath - status = 0x%0x\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::upstreamPCIDeviceNotification - newService = %p name = %s - FOUND!\n`
- `PCI Entry ID`
- `%lldus AppleThunderboltPCIDownAdapter(%x:%llx:%x)::deactivateRemoveLegacyProperty - remove legacy property from correlated PCI\n`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath: No RootBridge\n`
- `PCI-Thunderbolt-Legacy`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath - phandle_key = %p\n`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath - Disabled by boot-arg\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::setupPCICorrelationPathFromAdapter - status = 0x%08x parent_path = %p\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::createResources status = 0x%x\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::setupPCICorrelationPathFromAdapter - status = 0x%08x parent_pci_device = %p\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::setupPCICorrelationFromPCIDevice\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::finishPCICorrelation (2) - set pci correlation properties, status = 0x%08x\n`
- `site.AppleThunderboltPCIDownAdapterType5`
- `12111112122212121112222221111111212122`
- `acio`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::start\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::upstreamPCIDeviceNotification - newService = %p name = %s\n`
- `%lldus AppleThunderboltPCIDownAdapter(%x:%llx:%x)::activateSetLegacyProperty - switch needs extended link training, add legacy property to correlated PCI\n`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupBootArgs\n`
- `%lldus AppleThunderboltPCIDownAdapterType5<%p>::postAdapterEnable - tmp_status = 0x%08x\n`
- `1211111212221212111222222111111121212`
- `%X,%X`
- `PCI Path`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::earlyWake\n`
- `%lldus AppleThunderboltPCIDownAdapter::setupRootPCICorrelationPath\n`
- `%lldus AppleThunderboltPCIDownAdapter::setupPCICorrelationFromPCIDevice: dev %d func %d portnum %d\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::setThunderboltClient = %p success = %d\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::start - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::setupPCICorrelationFromPCIDevice - status = 0x%0x\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::findPCIChildFromDeviceFunction - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath - phandle_object = %p\n`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath - ERROR: failed to find service for \"%s\" phandle.\n`
- `site.AppleThunderboltPCIDownAdapter`
- `%lldus AppleThunderboltPCIDownAdapterType5<%p>::postAdapterEnable - port_control_prop = %p\n`
- `%lldus AppleThunderboltPCIDownAdapterType5<%p>::postAdapterEnable - port_control = %p\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::finalize\n`
- `%lldus AppleThunderboltPCIDownAdapter(%x:%llx:%x)::activateSetLegacyProperty - the_switch = %p\n`
- `%lldus AppleThunderboltPCIDownAdapterType5<%p>::postAdapterEnable - hal = %p\n`
- `Thunderbolt Entry ID`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::free\n`
- `%X`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::findPCIChildFromDeviceFunction - parent_device = %p, dev = %x, fn = %x\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::finishPCICorrelation (1) - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIDownAdapterType5<%p>::postAdapterEnable - nhi = %p\n`
- `tb`
- `PCI Device`
- `PCI Function`
- `%lldus AppleThunderboltPCIDownAdapterType5<%p>::postAdapterEnable - nhi_device = %p\n`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::setupPCICorrelationFromPCIDevice - eeprom - status = 0x%0x port number = %d\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::finishPCICorrelation (2) - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIDownAdapter(%x:%llx:%x)::activateSetLegacyProperty - fCorrelatedPCIDevice = %p, fProviderPort = %p\n`
- `function-pcie_port_control`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath - status = 0x%0x\n`
- `AppleThunderboltPCIDownAdapter`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::setupPCICorrelationPathFromAdapter - parent_adapter = %p\n`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath - matching_dictionary = %p\n`
