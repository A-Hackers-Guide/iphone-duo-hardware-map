# `com.apple.driver.AppleS5L8960XNCO`

- Name: AppleS5L8960XNCO
- Version: `1`
- UUID: `57494A53-DBB0-34DB-922C-C122D04ED90B`
- Source version: `195.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleS5L8960XNCO
- `CFBundleIdentifier`: `com.apple.driver.AppleS5L8960XNCO`
- `IOClass`: `AppleS5L8960XNCO`
- `IONameMatch`: `nco,s5l8960x`
- `IOPersonalityPublisher`: `com.apple.driver.AppleS5L8960XNCO`
- `IOPlatformActiveAction`: `85000`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleS5L8960XNCO` | 0xb8 | IOService → IORegistryEntry |
| `AppleS5L8960XNCOFrequencyFunction` | 0x38 | AppleARMFunction |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000006d8 off=0x006d38e0-0x006d3fb8 addr=0xfffffe00076d78e0-0xfffffe00076d7fb8 r--/r--   __TEXT            
	sz=0x000000b0 off=0x006d3f08-0x006d3fb8 addr=0xfffffe00076d7f08-0xfffffe00076d7fb8               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00001158 off=0x0247bfd0-0x0247d128 addr=0xfffffe000947ffd0-0xfffffe0009481128 r-x/r-x   __TEXT_EXEC       
	sz=0x00001078 off=0x0247bfd0-0x0247d048 addr=0xfffffe000947ffd0-0xfffffe0009481048          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000000e0 off=0x0247d048-0x0247d128 addr=0xfffffe0009481048-0xfffffe0009481128          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x0498fea0-0x0498ffc8 addr=0xfffffe000b993ea0-0xfffffe000b993fc8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0498fea0-0x0498ff68 addr=0xfffffe000b993ea0-0xfffffe000b993f68               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b993f68-0xfffffe000b993fc8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000008c0 off=0x011c1910-0x011c21d0 addr=0xfffffe00081c5910-0xfffffe00081c61d0 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x011c1910-0x011c1918 addr=0xfffffe00081c5910-0xfffffe00081c5918         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x011c1918-0x011c1920 addr=0xfffffe00081c5918-0xfffffe00081c5920         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000728 off=0x011c1920-0x011c2048 addr=0xfffffe00081c5920-0xfffffe00081c6048         __DATA_CONST.__const            
	sz=0x00000080 off=0x011c2048-0x011c20c8 addr=0xfffffe00081c6048-0xfffffe00081c60c8         __DATA_CONST.__kalloc_type      
	sz=0x00000050 off=0x011c20c8-0x011c2118 addr=0xfffffe00081c60c8-0xfffffe00081c6118         __DATA_CONST.__kalloc_var       
	sz=0x00000070 off=0x011c2118-0x011c2188 addr=0xfffffe00081c6118-0xfffffe00081c6188         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000048 off=0x011c2188-0x011c21d0 addr=0xfffffe00081c6188-0xfffffe00081c61d0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 37 at 0x04ae35e0
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     57494A53-DBB0-34DB-922C-C122D04ED90B
008: LC_SOURCE_VERSION           195.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aaebe8 size=0x38
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleS5L8960XNCO`
- `CFBundleIdentifier`: `com.apple.driver.AppleS5L8960XNCO`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleS5L8960XNCO`
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
- `NSHumanReadableCopyright`: `Copyright © 2011-2013 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleS5L8960XNCO.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898640672`
- `_PrelinkExecutableRelativePath`: `AppleS5L8960XNCO`
- `_PrelinkExecutableSize`: `8728`
- `_PrelinkExecutableSourceAddr`: `-2198898640672`
- `_PrelinkKmodInfo`: `-2198828663136`

## Strings (8) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.AppleS5L8960XNCO`
- `12111112122212121112212`
- `pmgr-nco-page-size`
- `site.UInt32`
- `AppleS5L8960XNCOFrequencyFunction`
- `site.AppleS5L8960XNCOFrequencyFunction`
- `1211112`
- `AppleS5L8960XNCO`
