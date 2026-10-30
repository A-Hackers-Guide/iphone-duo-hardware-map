# `com.apple.kec.Compression`

- Name: Compression
- Version: `1.0`
- UUID: `DE66FEEF-02AD-3A59-B058-71B95EAB609E`
- Source version: `212.40.2.0.0`
- Depends on: [`com.apple.kec.corecrypto`](com.apple.kec.corecrypto.md) 1.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 21.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 21.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 21.0

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
Commands      = 10 (Size: 1080)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000004a0 off=0x00904970-0x00904e10 addr=0xfffffe0007908970-0xfffffe0007908e10 r--/r--   __TEXT            
	sz=0x00000008 off=0x00904e08-0x00904e10 addr=0xfffffe0007908e08-0xfffffe0007908e10               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00003c94 off=0x02bfc880-0x02c00514 addr=0xfffffe0009c00880-0xfffffe0009c04514 r-x/r-x   __TEXT_EXEC       
	sz=0x00003c34 off=0x02bfc880-0x02c004b4 addr=0xfffffe0009c00880-0xfffffe0009c044b4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000060 off=0x02c004b4-0x02c00514 addr=0xfffffe0009c044b4-0xfffffe0009c04514          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000000dc off=0x049db1b8-0x049db294 addr=0xfffffe000b9df1b8-0xfffffe000b9df294 rw-/rw-   __DATA            
	sz=0x000000dc off=0x049db1b8-0x049db294 addr=0xfffffe000b9df1b8-0xfffffe000b9df294               __DATA.__data             
003: LC_SEGMENT_64 sz=0x00000080 off=0x012c2a90-0x012c2b10 addr=0xfffffe00082c6a90-0xfffffe00082c6b10 rw-/rw-   __DATA_CONST      
	sz=0x00000048 off=0x012c2a90-0x012c2ad8 addr=0xfffffe00082c6a90-0xfffffe00082c6ad8         __DATA_CONST.__const            
	sz=0x00000030 off=0x012c2ad8-0x012c2b08 addr=0xfffffe00082c6ad8-0xfffffe00082c6b08         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000008 off=0x012c2b08-0x012c2b10 addr=0xfffffe00082c6b08-0xfffffe00082c6b10         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 13 at 0x04aedab0
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     DE66FEEF-02AD-3A59-B058-71B95EAB609E
008: LC_SOURCE_VERSION           212.40.2.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab8eb0 size=0x40
```

## Info.plist keys [KC]

- `AppleKernelExternalComponent`: `True`
- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `Compression`
- `CFBundleIdentifier`: `com.apple.kec.Compression`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `Compression`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
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
- `NSHumanReadableCopyright`: `Copyright © 2021 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/Compression.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896342672`
- `_PrelinkExecutableRelativePath`: `Compression`
- `_PrelinkExecutableSize`: `17040`
- `_PrelinkExecutableSourceAddr`: `-2198896342672`
- `_PrelinkKmodInfo`: `-2198828355144`

## Strings (0) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.
