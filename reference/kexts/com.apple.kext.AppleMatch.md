# `com.apple.kext.AppleMatch`

- Name: Regular Expression Matching Engine
- Version: `1.0.0d1`
- UUID: `814EA817-3A2F-3D9F-B84A-6FD0CD355F19`
- Source version: `50.40.2.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 7.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 10.0.0d3

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
Commands      = 10 (Size: 1160)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000547 off=0x0065b9b0-0x0065bef7 addr=0xfffffe000765f9b0-0xfffffe000765fef7 r--/r--   __TEXT            
	sz=0x0000005f off=0x0065be98-0x0065bef7 addr=0xfffffe000765fe98-0xfffffe000765fef7               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00002594 off=0x0223fa90-0x02242024 addr=0xfffffe0009243a90-0xfffffe0009246024 r-x/r-x   __TEXT_EXEC       
	sz=0x000024e4 off=0x0223fa90-0x02241f74 addr=0xfffffe0009243a90-0xfffffe0009245f74          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000000b0 off=0x02241f74-0x02242024 addr=0xfffffe0009245f74-0xfffffe0009246024          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000000dc off=0x04979340-0x0497941c addr=0xfffffe000b97d340-0xfffffe000b97d41c rw-/rw-   __DATA            
	sz=0x000000dc off=0x04979340-0x0497941c addr=0xfffffe000b97d340-0xfffffe000b97d41c               __DATA.__data             
003: LC_SEGMENT_64 sz=0x000002d0 off=0x0116a218-0x0116a4e8 addr=0xfffffe000816e218-0xfffffe000816e4e8 rw-/rw-   __DATA_CONST      
	sz=0x00000180 off=0x0116a218-0x0116a398 addr=0xfffffe000816e218-0xfffffe000816e398         __DATA_CONST.__kalloc_type      
	sz=0x000000f0 off=0x0116a398-0x0116a488 addr=0xfffffe000816e398-0xfffffe000816e488         __DATA_CONST.__kalloc_var       
	sz=0x00000058 off=0x0116a488-0x0116a4e0 addr=0xfffffe000816e488-0xfffffe000816e4e0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000008 off=0x0116a4e0-0x0116a4e8 addr=0xfffffe000816e4e0-0xfffffe000816e4e8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 23 at 0x04adf10c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     814EA817-3A2F-3D9F-B84A-6FD0CD355F19
008: LC_SOURCE_VERSION           50.40.2.0.0
009: LC_FUNCTION_STARTS          offset=0x004aaa480 size=0x38
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleMatch`
- `CFBundleIdentifier`: `com.apple.kext.AppleMatch`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `Regular Expression Matching Engine`
- `CFBundleNumericVersion`: `16785409`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `50.40.2`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0d1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2008-2023 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0d1`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleMatch.kext`
- `_PrelinkExecutableLoadAddr`: `-2198899131984`
- `_PrelinkExecutableRelativePath`: `AppleMatch`
- `_PrelinkExecutableSize`: `11911`
- `_PrelinkExecutableSourceAddr`: `-2198899131984`
- `_PrelinkKmodInfo`: `-2198828756160`

## Strings (7) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.struct __matchExpr`
- `211112111`
- `site.reNFA_t.reGraphNode_t`
- `1211223`
- `23`
- `site.rePackedNFA_t`
- `112`
