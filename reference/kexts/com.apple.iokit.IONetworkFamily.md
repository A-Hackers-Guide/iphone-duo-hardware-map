# `com.apple.iokit.IONetworkFamily`

- Name: IONetworkFamily
- Version: `1.0`
- UUID: `D3AFED30-EAAD-38E4-8735-3843FA47C31C`
- Source version: `598.0.0.0.0`
- Depends on: [`com.apple.iokit.IOSkywalkFamily`](com.apple.iokit.IOSkywalkFamily.md) 1.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 18.6.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 18.6.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IONetworkFamily` | 0x208 | IOUserNetworkWLAN → IOUserNetworkEthernet → IOSkywalkEthernetInterface → IOSkywalkNetworkInterface → IOSkywalkInterface → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000063f off=0x00a27cc0-0x00a282ff addr=0xfffffe0007a2bcc0-0xfffffe0007a2c2ff r--/r--   __TEXT            
	sz=0x00000067 off=0x00a28298-0x00a282ff addr=0xfffffe0007a2c298-0xfffffe0007a2c2ff               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x0000041c off=0x032c2fd0-0x032c33ec addr=0xfffffe000a2c6fd0-0xfffffe000a2c73ec r-x/r-x   __TEXT_EXEC       
	sz=0x000003ac off=0x032c2fd0-0x032c337c addr=0xfffffe000a2c6fd0-0xfffffe000a2c737c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000070 off=0x032c337c-0x032c33ec addr=0xfffffe000a2c737c-0xfffffe000a2c73ec          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x04a13550-0x04a13650 addr=0xfffffe000ba17550-0xfffffe000ba17650 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a13550-0x04a13618 addr=0xfffffe000ba17550-0xfffffe000ba17618               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000ba17618-0xfffffe000ba17650               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000860 off=0x013bed08-0x013bf568 addr=0xfffffe00083c2d08-0xfffffe00083c3568 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x013bed08-0x013bed10 addr=0xfffffe00083c2d08-0xfffffe00083c2d10         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x013bed10-0x013bed18 addr=0xfffffe00083c2d10-0xfffffe00083c2d18         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000007d0 off=0x013bed18-0x013bf4e8 addr=0xfffffe00083c2d18-0xfffffe00083c34e8         __DATA_CONST.__const            
	sz=0x00000040 off=0x013bf4e8-0x013bf528 addr=0xfffffe00083c34e8-0xfffffe00083c3528         __DATA_CONST.__kalloc_type      
	sz=0x00000038 off=0x013bf528-0x013bf560 addr=0xfffffe00083c3528-0xfffffe00083c3560         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000008 off=0x013bf560-0x013bf568 addr=0xfffffe00083c3560-0xfffffe00083c3568         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 15 at 0x04af4e74
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     D3AFED30-EAAD-38E4-8735-3843FA47C31C
008: LC_SOURCE_VERSION           598.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac3318 size=0x20
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `IONetworkFamily`
- `CFBundleIdentifier`: `com.apple.iokit.IONetworkFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IONetworkFamily`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2022 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IONetworkFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895149888`
- `_PrelinkExecutableRelativePath`: `IONetworkFamily`
- `_PrelinkExecutableSize`: `5051`
- `_PrelinkExecutableSourceAddr`: `-2198895149888`
- `_PrelinkKmodInfo`: `-2198828124848`

## Strings (3) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `12111112122212121111111211121222111111112122222222222222222222221`
- `IONetworkFamily`
- `site.IONetworkFamily`
