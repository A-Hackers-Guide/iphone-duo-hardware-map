# `com.apple.driver.AppleBSDKextStarter`

- Name: AppleBSDKextStarter
- Version: `3`
- UUID: `E068997D-AAA1-32A7-B9B2-8A613DA2DEA4`
- Source version: `18.0.0.0.0`
- Depends on: [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleBSDKextStarter` | 0x88 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000068a off=0x00395640-0x00395cca addr=0xfffffe0007399640-0xfffffe0007399cca r--/r--   __TEXT            
	sz=0x000000b2 off=0x00395c18-0x00395cca addr=0xfffffe0007399c18-0xfffffe0007399cca               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00000668 off=0x019a68d0-0x019a6f38 addr=0xfffffe00089aa8d0-0xfffffe00089aaf38 r-x/r-x   __TEXT_EXEC       
	sz=0x000005b8 off=0x019a68d0-0x019a6e88 addr=0xfffffe00089aa8d0-0xfffffe00089aae88          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000000b0 off=0x019a6e88-0x019a6f38 addr=0xfffffe00089aae88-0xfffffe00089aaf38          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x04933490-0x04933590 addr=0xfffffe000b937490-0xfffffe000b937590 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04933490-0x04933558 addr=0xfffffe000b937490-0xfffffe000b937558               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b937558-0xfffffe000b937590               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000006b0 off=0x00fef320-0x00fef9d0 addr=0xfffffe0007ff3320-0xfffffe0007ff39d0 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x00fef320-0x00fef328 addr=0xfffffe0007ff3320-0xfffffe0007ff3328         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x00fef328-0x00fef330 addr=0xfffffe0007ff3328-0xfffffe0007ff3330         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000005f0 off=0x00fef330-0x00fef920 addr=0xfffffe0007ff3330-0xfffffe0007ff3920         __DATA_CONST.__const            
	sz=0x00000040 off=0x00fef920-0x00fef960 addr=0xfffffe0007ff3920-0xfffffe0007ff3960         __DATA_CONST.__kalloc_type      
	sz=0x00000058 off=0x00fef960-0x00fef9b8 addr=0xfffffe0007ff3960-0xfffffe0007ff39b8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000018 off=0x00fef9b8-0x00fef9d0 addr=0xfffffe0007ff39b8-0xfffffe0007ff39d0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 25 at 0x04ad3aac
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     E068997D-AAA1-32A7-B9B2-8A613DA2DEA4
008: LC_SOURCE_VERSION           18.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9a5f8 size=0x20
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleBSDKextStarter`
- `CFBundleIdentifier`: `com.apple.driver.AppleBSDKextStarter`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleBSDKextStarter`
- `CFBundleNumericVersion`: `50364416`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `3`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleBSDKextStarter.kext`
- `_PrelinkExecutableLoadAddr`: `-2198902041024`
- `_PrelinkExecutableRelativePath`: `AppleBSDKextStarter`
- `_PrelinkExecutableSize`: `5282`
- `_PrelinkExecutableSourceAddr`: `-2198902041024`
- `_PrelinkKmodInfo`: `-2198829042544`

## Strings (7) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AppleBSDKextStarterBundleIdentifiers`
- `Failed to create iterator %d\n`
- `Load request for %s failed: %d\n`
- `AppleBSDKextStarter`
- `site.AppleBSDKextStarter`
- `12111112122212121`
- `IOMatchCategory`
