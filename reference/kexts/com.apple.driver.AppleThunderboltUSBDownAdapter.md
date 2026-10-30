# `com.apple.driver.AppleThunderboltUSBDownAdapter`

- Name: AppleThunderboltUSBDownAdapter
- Version: `1.0.4`
- UUID: `A26B2A1B-F82F-3906-B5F4-8D918CAA0450`
- Source version: `138.40.3.0.0`
- Depends on: [`com.apple.iokit.IOThunderboltFamily`](com.apple.iokit.IOThunderboltFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleThunderboltUSBDownAdapter
- `Adapter Type`: `2097409`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltUSBDownAdapter`
- `IOClass`: `AppleThunderboltUSBDownAdapter`
- `IOPersonalityPublisher`: `com.apple.driver.AppleThunderboltUSBDownAdapter`
- `IOProbeScore`: `4096`
- `IOProviderClass`: `IOThunderboltPort`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleThunderboltUSBDownAdapter` | 0xe0 | IOThunderboltTunnelDriver → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000b91 off=0x0088d1c0-0x0088dd51 addr=0xfffffe00078911c0-0xfffffe0007891d51 r--/r--   __TEXT            
	sz=0x000002e6 off=0x0088d7e8-0x0088dace addr=0xfffffe00078917e8-0xfffffe0007891ace               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000283 off=0x0088dace-0x0088dd51 addr=0xfffffe0007891ace-0xfffffe0007891d51               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x000013f8 off=0x029f2220-0x029f3618 addr=0xfffffe00099f6220-0xfffffe00099f7618 r-x/r-x   __TEXT_EXEC       
	sz=0x000012f8 off=0x029f2220-0x029f3518 addr=0xfffffe00099f6220-0xfffffe00099f7518          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000100 off=0x029f3518-0x029f3618 addr=0xfffffe00099f7518-0xfffffe00099f7618          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x049cedf8-0x049ceef8 addr=0xfffffe000b9d2df8-0xfffffe000b9d2ef8 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x049cedf8-0x049ceebc addr=0xfffffe000b9d2df8-0xfffffe000b9d2ebc               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9d2ec0-0xfffffe000b9d2ef8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000830 off=0x0128cff0-0x0128d820 addr=0xfffffe0008290ff0-0xfffffe0008291820 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x0128cff0-0x0128cff8 addr=0xfffffe0008290ff0-0xfffffe0008290ff8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x0128cff8-0x0128d000 addr=0xfffffe0008290ff8-0xfffffe0008291000         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000730 off=0x0128d000-0x0128d730 addr=0xfffffe0008291000-0xfffffe0008291730         __DATA_CONST.__const            
	sz=0x00000040 off=0x0128d730-0x0128d770 addr=0xfffffe0008291730-0xfffffe0008291770         __DATA_CONST.__kalloc_type      
	sz=0x00000080 off=0x0128d770-0x0128d7f0 addr=0xfffffe0008291770-0xfffffe00082917f0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000030 off=0x0128d7f0-0x0128d820 addr=0xfffffe00082917f0-0xfffffe0008291820         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 38 at 0x04aea6b4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     A26B2A1B-F82F-3906-B5F4-8D918CAA0450
008: LC_SOURCE_VERSION           138.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab6450 size=0x30
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleThunderboltUSBDownAdapter`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltUSBDownAdapter`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleThunderboltUSBDownAdapter`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleThunderboltUSBAdapters.kext/PlugIns/AppleThunderboltUSBDownAdapter.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896832064`
- `_PrelinkExecutableRelativePath`: `AppleThunderboltUSBDownAdapter`
- `_PrelinkExecutableSize`: `10425`
- `_PrelinkExecutableSourceAddr`: `-2198896832064`
- `_PrelinkKmodInfo`: `-2198828405256`

## Strings (22) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `1211111212221212111222222112`
- `tb`
- `%lldus AppleThunderboltUSBDownAdapter(%x@%llx:%x)::free\n`
- `%lldus AppleThunderboltUSBDownAdapter(%x@%llx:%x)::createResources status = 0x%x\n`
- `%lldus AppleThunderboltUSBDownAdapter(%x@%llx:%x)::setThunderboltClient = %p success = %d\n`
- `%lldus AppleThunderboltUSBDownAdapter(%x@%llx:%x)::enableAdapter - enable = %d status=0x%08x\n`
- `%lldus AppleThunderboltUSBDownAdapter(%x@%llx:%x)::lateSleep\n`
- `AppleThunderboltUSBDownAdapter`
- `%lldus AppleThunderboltUSBDownAdapter(%x@%llx:%x)::start\n`
- `%lldus AppleThunderboltUSBDownAdapter(%x@%llx:%x)::start - status = 0x%08x\n`
- `%lldus AppleThunderboltUSBDownAdapter(%x@%llx:%x)::finalize\n`
- `%lldus AppleThunderboltUSBDownAdapter(%x@%llx:%x)::earlyWake\n`
- `site.AppleThunderboltUSBDownAdapter`

**[__TEXT.__os_log]**

- `%lldus AppleThunderboltUSBDownAdapter(%x@%llx:%x)::setThunderboltClient = %p success = %d\n`
- `%lldus AppleThunderboltUSBDownAdapter(%x@%llx:%x)::earlyWake\n`
- `%lldus AppleThunderboltUSBDownAdapter(%x@%llx:%x)::start\n`
- `%lldus AppleThunderboltUSBDownAdapter(%x@%llx:%x)::start - status = 0x%08x\n`
- `%lldus AppleThunderboltUSBDownAdapter(%x@%llx:%x)::finalize\n`
- `%lldus AppleThunderboltUSBDownAdapter(%x@%llx:%x)::free\n`
- `%lldus AppleThunderboltUSBDownAdapter(%x@%llx:%x)::enableAdapter - enable = %d status=0x%08x\n`
- `%lldus AppleThunderboltUSBDownAdapter(%x@%llx:%x)::lateSleep\n`
- `%lldus AppleThunderboltUSBDownAdapter(%x@%llx:%x)::createResources status = 0x%x\n`
