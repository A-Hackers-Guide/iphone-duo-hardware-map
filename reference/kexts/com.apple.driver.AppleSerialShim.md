# `com.apple.driver.AppleSerialShim`

- Name: AppleSerialShim
- Version: `1`
- UUID: `6A0EBE0F-0BEE-3441-AEAA-02B17D50F2C3`
- Source version: `15.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (2) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/dockchannel-uart`](../devicetree/root__arm-io__dockchannel-uart.md) | `AppleSerialShim` | `dockchannel-uart` |
| [`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) | `AppleSerialShim` | `uart0` |

## IOKit personalities (2) [KC]

### AppleSerialShimGeneral
- `CFBundleIdentifier`: `com.apple.driver.AppleSerialShim`
- `IOClass`: `AppleSerialShim`
- `IONameMatch`:
  - `dockchannel-uart`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSerialShim`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleSerialShimUart
- `CFBundleIdentifier`: `com.apple.driver.AppleSerialShim`
- `IOClass`: `AppleSerialShim`
- `IONameMatch`:
  - `uart0`
  - `uart1`
  - `uart2`
  - `uart3`
  - `uart4`
  - `uart5`
  - `uart6`
  - `uart7`
  - `uart8`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSerialShim`
- `IOProbeScore`: `1000`
- `IOPropertyMatch`:
  - `boot-console`: ``
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleSerialShim` | 0xa0 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000007ca off=0x007824a0-0x00782c6a addr=0xfffffe00077864a0-0xfffffe0007786c6a r--/r--   __TEXT            
	sz=0x000001f2 off=0x00782a78-0x00782c6a addr=0xfffffe0007786a78-0xfffffe0007786c6a               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00000c04 off=0x02728c00-0x02729804 addr=0xfffffe000972cc00-0xfffffe000972d804 r-x/r-x   __TEXT_EXEC       
	sz=0x00000b24 off=0x02728c00-0x02729724 addr=0xfffffe000972cc00-0xfffffe000972d724          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000000e0 off=0x02729724-0x02729804 addr=0xfffffe000972d724-0xfffffe000972d804          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x0499a470-0x0499a570 addr=0xfffffe000b99e470-0xfffffe000b99e570 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x0499a470-0x0499a534 addr=0xfffffe000b99e470-0xfffffe000b99e534               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b99e538-0xfffffe000b99e570               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000006c8 off=0x01227db8-0x01228480 addr=0xfffffe000822bdb8-0xfffffe000822c480 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01227db8-0x01227dc0 addr=0xfffffe000822bdb8-0xfffffe000822bdc0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01227dc0-0x01227dc8 addr=0xfffffe000822bdc0-0xfffffe000822bdc8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000005f0 off=0x01227dc8-0x012283b8 addr=0xfffffe000822bdc8-0xfffffe000822c3b8         __DATA_CONST.__const            
	sz=0x00000040 off=0x012283b8-0x012283f8 addr=0xfffffe000822c3b8-0xfffffe000822c3f8         __DATA_CONST.__kalloc_type      
	sz=0x00000070 off=0x012283f8-0x01228468 addr=0xfffffe000822c3f8-0xfffffe000822c468         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000018 off=0x01228468-0x01228480 addr=0xfffffe000822c468-0xfffffe000822c480         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 31 at 0x04ae6d6c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     6A0EBE0F-0BEE-3441-AEAA-02B17D50F2C3
008: LC_SOURCE_VERSION           15.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab2d98 size=0x20
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleSerialShim`
- `CFBundleIdentifier`: `com.apple.driver.AppleSerialShim`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSerialShim`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
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
- `NSHumanReadableCopyright`: `Copyright © 2019, 2020 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleSerialShim.kext`
- `_PrelinkExecutableLoadAddr`: `-2198897924960`
- `_PrelinkExecutableRelativePath`: `AppleSerialShim`
- `_PrelinkExecutableSize`: `7062`
- `_PrelinkExecutableSourceAddr`: `-2198897924960`
- `_PrelinkKmodInfo`: `-2198828620688`

## Strings (16) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AppleSerialShim`
- `Failed to start parent.\n`
- `[%s] Started AppleSerialShim.\n`
- `dockchannel`
- `site.AppleSerialShim`
- `12111112122212121211`
- `name`
- `dockchannel-uart`
- `Failed to start: attached to unknown device.\n`
- `[%s] Failed to start: failed to create work loop.\n`
- `[%s] couldn't register filterInterruptEventSource\n`
- `[%s] Failed to start: could not add interrupt source to work loop.\n`
- `Unable to get provider name.\n`
- `[%s] Failed to start: platform serial driver does not support interrupts for this device.\n`
- `uart`
- `unknown`
