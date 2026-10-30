# `com.apple.driver.AppleGPIOCanary`

- Name: AppleGPIOCanary
- Version: `1.0.0`
- UUID: `F6C8AAD4-11B1-3828-AC28-1CAE98D59683`
- Source version: `68.0.0.0.0`
- Depends on: [`com.apple.iokit.CoreAnalyticsFamily`](com.apple.iokit.CoreAnalyticsFamily.md) 1.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/gpio-canary`](../devicetree/root__arm-io__gpio-canary.md) | `AppleGPIOCanary` | `gpio-canary,t8101` |

## IOKit personalities (1) [KC]

### AppleGPIOCanary
- `CFBundleIdentifier`: `com.apple.driver.AppleGPIOCanary`
- `IOClass`: `AppleGPIOCanary`
- `IONameMatch`: `gpio-canary,t8101`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGPIOCanary`
- `IOProviderClass`: `IOService`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleGPIOCanary` | 0x98 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000006c6 off=0x00472910-0x00472fd6 addr=0xfffffe0007476910-0xfffffe0007476fd6 r--/r--   __TEXT            
	sz=0x000000ee off=0x00472ee8-0x00472fd6 addr=0xfffffe0007476ee8-0xfffffe0007476fd6               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00000914 off=0x01cfe800-0x01cff114 addr=0xfffffe0008d02800-0xfffffe0008d03114 r-x/r-x   __TEXT_EXEC       
	sz=0x000007f4 off=0x01cfe800-0x01cfeff4 addr=0xfffffe0008d02800-0xfffffe0008d02ff4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000120 off=0x01cfeff4-0x01cff114 addr=0xfffffe0008d02ff4-0xfffffe0008d03114          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x04942208-0x04942308 addr=0xfffffe000b946208-0xfffffe000b946308 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04942208-0x049422d0 addr=0xfffffe000b946208-0xfffffe000b9462d0               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9462d0-0xfffffe000b946308               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000700 off=0x010af588-0x010afc88 addr=0xfffffe00080b3588-0xfffffe00080b3c88 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x010af588-0x010af590 addr=0xfffffe00080b3588-0xfffffe00080b3590         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x010af590-0x010af598 addr=0xfffffe00080b3590-0xfffffe00080b3598         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000005f0 off=0x010af598-0x010afb88 addr=0xfffffe00080b3598-0xfffffe00080b3b88         __DATA_CONST.__const            
	sz=0x00000040 off=0x010afb88-0x010afbc8 addr=0xfffffe00080b3b88-0xfffffe00080b3bc8         __DATA_CONST.__kalloc_type      
	sz=0x00000090 off=0x010afbc8-0x010afc58 addr=0xfffffe00080b3bc8-0xfffffe00080b3c58         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000030 off=0x010afc58-0x010afc88 addr=0xfffffe00080b3c58-0xfffffe00080b3c88         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 42 at 0x04ada268
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     F6C8AAD4-11B1-3828-AC28-1CAE98D59683
008: LC_SOURCE_VERSION           68.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa07e0 size=0x20
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleGPIOCanary`
- `CFBundleGetInfoString`: `Copyright © 2020 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleGPIOCanary`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleGPIOCanary`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
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
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleGPIOCanary.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901135088`
- `_PrelinkExecutableRelativePath`: `AppleGPIOCanary`
- `_PrelinkExecutableSize`: `6106`
- `_PrelinkExecutableSourceAddr`: `-2198901135088`
- `_PrelinkKmodInfo`: `-2198828981752`

## Strings (12) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AppleGPIOCanary`
- `site.AppleGPIOCanary`
- `1211111212221212111`
- `canary-pins`
- `attachCoreAnalyticsService`
- `com.apple.canary.gpio`
- `CoreAnalyticsHub`
- `AppleGPIOCanary::start: this: %p\n`
- `\"%s:pinsCount > kMaxPins\" @%s:%d`
- `AppleGPIOCanary.cpp`
- `GPIO%03d%d`
- `%08x`
