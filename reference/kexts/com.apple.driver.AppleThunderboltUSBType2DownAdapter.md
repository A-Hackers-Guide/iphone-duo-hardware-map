# `com.apple.driver.AppleThunderboltUSBType2DownAdapter`

- Name: AppleThunderboltUSBType2DownAdapter
- Version: `1.0.4`
- UUID: `4F68B116-67D4-39B0-BDA2-65231C0BE439`
- Source version: `138.40.3.0.0`
- Depends on: [`com.apple.iokit.IOThunderboltFamily`](com.apple.iokit.IOThunderboltFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleThunderboltUSBType2DownAdapter
- `Adapter Type`: `2162945`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltUSBType2DownAdapter`
- `IOClass`: `AppleThunderboltUSBType2DownAdapter`
- `IOPersonalityPublisher`: `com.apple.driver.AppleThunderboltUSBType2DownAdapter`
- `IOProbeScore`: `4096`
- `IOProviderClass`: `IOThunderboltPort`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleThunderboltUSBType2DownAdapter` | 0xe8 | IOThunderboltTunnelDriverType2 → IOThunderboltTunnelDriver → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001124 off=0x0088dd60-0x0088ee84 addr=0xfffffe0007891d60-0xfffffe0007892e84 r--/r--   __TEXT            
	sz=0x000005a6 off=0x0088e388-0x0088e92e addr=0xfffffe0007892388-0xfffffe000789292e               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000556 off=0x0088e92e-0x0088ee84 addr=0xfffffe000789292e-0xfffffe0007892e84               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00002008 off=0x029f3620-0x029f5628 addr=0xfffffe00099f7620-0xfffffe00099f9628 r-x/r-x   __TEXT_EXEC       
	sz=0x00001ef8 off=0x029f3620-0x029f5518 addr=0xfffffe00099f7620-0xfffffe00099f9518          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000110 off=0x029f5518-0x029f5628 addr=0xfffffe00099f9518-0xfffffe00099f9628          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x049ceef8-0x049ceff8 addr=0xfffffe000b9d2ef8-0xfffffe000b9d2ff8 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x049ceef8-0x049cefbc addr=0xfffffe000b9d2ef8-0xfffffe000b9d2fbc               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9d2fc0-0xfffffe000b9d2ff8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000008a8 off=0x0128d820-0x0128e0c8 addr=0xfffffe0008291820-0xfffffe00082920c8 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x0128d820-0x0128d828 addr=0xfffffe0008291820-0xfffffe0008291828         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x0128d828-0x0128d830 addr=0xfffffe0008291828-0xfffffe0008291830         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000007a0 off=0x0128d830-0x0128dfd0 addr=0xfffffe0008291830-0xfffffe0008291fd0         __DATA_CONST.__const            
	sz=0x00000040 off=0x0128dfd0-0x0128e010 addr=0xfffffe0008291fd0-0xfffffe0008292010         __DATA_CONST.__kalloc_type      
	sz=0x00000088 off=0x0128e010-0x0128e098 addr=0xfffffe0008292010-0xfffffe0008292098         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000030 off=0x0128e098-0x0128e0c8 addr=0xfffffe0008292098-0xfffffe00082920c8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 40 at 0x04aea74c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     4F68B116-67D4-39B0-BDA2-65231C0BE439
008: LC_SOURCE_VERSION           138.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab6480 size=0x30
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleThunderboltUSBType2DownAdapter`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltUSBType2DownAdapter`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleThunderboltUSBType2DownAdapter`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleThunderboltUSBAdapters.kext/PlugIns/AppleThunderboltUSBType2DownAdapter.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896829088`
- `_PrelinkExecutableRelativePath`: `AppleThunderboltUSBType2DownAdapter`
- `_PrelinkExecutableSize`: `15060`
- `_PrelinkExecutableSourceAddr`: `-2198896829088`
- `_PrelinkKmodInfo`: `-2198828405000`

## Strings (33) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AppleThunderboltUSBType2DownAdapter`
- `site.AppleThunderboltUSBType2DownAdapter`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::finalize\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::setBundleWeight0 - status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::setBundleWeight - data = 0x%lx fPortCount = 0x%lx status=0x%08x\n`
- `tbusb`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::start - status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::free\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::createResources status = 0x%x\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::lateSleep\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::enableAdapter - findCapability failed status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::enableAdapter - enable = %d status=0x%08x transportPort=0x%x\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::start\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::setThunderboltClient = %p success = %d\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::earlyWake\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::configureActiveLinkRate - data = 0x%lx status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::configureLinkCommandsAggregation - mask = 0x%lx status=0x%08x\n`
- `12111112122212121112222221212`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::start bootargs=0x%x\n`

**[__TEXT.__os_log]**

- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::start\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::finalize\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::free\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::createResources status = 0x%x\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::setThunderboltClient = %p success = %d\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::earlyWake\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::enableAdapter - findCapability failed status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::enableAdapter - enable = %d status=0x%08x transportPort=0x%x\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::start - status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::lateSleep\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::configureActiveLinkRate - data = 0x%lx status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::configureLinkCommandsAggregation - mask = 0x%lx status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::setBundleWeight0 - status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2DownAdapter(%x@%llx:%x)::setBundleWeight - data = 0x%lx fPortCount = 0x%lx status=0x%08x\n`
