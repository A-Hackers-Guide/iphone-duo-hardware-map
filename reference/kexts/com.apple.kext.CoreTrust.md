# `com.apple.kext.CoreTrust`

- Name: CoreTrust
- Version: `1`
- UUID: `57837CF6-87D5-35E7-A4FA-AC6FA70A7A5D`
- Source version: `207.40.4.0.0`
- Depends on: [`com.apple.kec.corecrypto`](com.apple.kec.corecrypto.md) 1.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 17.5, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (0) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1240)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00009458 off=0x00908c80-0x009120d8 addr=0xfffffe000790cc80-0xfffffe00079160d8 r--/r--   __TEXT            
	sz=0x00008f18 off=0x009091c0-0x009120d8 addr=0xfffffe000790d1c0-0xfffffe00079160d8               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x0000afdc off=0x02c08f50-0x02c13f2c addr=0xfffffe0009c0cf50-0xfffffe0009c17f2c r-x/r-x   __TEXT_EXEC       
	sz=0x0000adbc off=0x02c08f50-0x02c13d0c addr=0xfffffe0009c0cf50-0xfffffe0009c17d0c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000220 off=0x02c13d0c-0x02c13f2c addr=0xfffffe0009c17d0c-0xfffffe0009c17f2c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000000e8 off=0x049db468-0x049db550 addr=0xfffffe000b9df468-0xfffffe000b9df550 rw-/rw-   __DATA            
	sz=0x000000d8 off=0x049db468-0x049db540 addr=0xfffffe000b9df468-0xfffffe000b9df540               __DATA.__data             
	sz=0x00000010 off=0x00000000-0x00000010 addr=0xfffffe000b9df540-0xfffffe000b9df550               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00004408 off=0x012c4c20-0x012c9028 addr=0xfffffe00082c8c20-0xfffffe00082cd028 rw-/rw-   __DATA_CONST      
	sz=0x000042e0 off=0x012c4c20-0x012c8f00 addr=0xfffffe00082c8c20-0xfffffe00082ccf00         __DATA_CONST.__const            
	sz=0x00000110 off=0x012c8f00-0x012c9010 addr=0xfffffe00082ccf00-0xfffffe00082cd010         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000008 off=0x012c9010-0x012c9018 addr=0xfffffe00082cd010-0xfffffe00082cd018         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000010 off=0x012c9018-0x012c9028 addr=0xfffffe00082cd018-0xfffffe00082cd028         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 69 at 0x04aedd18
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     57837CF6-87D5-35E7-A4FA-AC6FA70A7A5D
008: LC_SOURCE_VERSION           207.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab9048 size=0xf8
```

## Info.plist keys [KC]

- `AppleSecurityExtension`: `True`
- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `CoreTrust`
- `CFBundleIdentifier`: `com.apple.kext.CoreTrust`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `CoreTrust`
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
- `NSHumanReadableCopyright`: `Copyright © 2017-2018 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/CoreTrust.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896325504`
- `_PrelinkExecutableRelativePath`: `CoreTrust`
- `_PrelinkExecutableSize`: `100644`
- `_PrelinkExecutableSourceAddr`: `-2198896325504`
- `_PrelinkKmodInfo`: `-2198828354456`

## Strings (0) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.
