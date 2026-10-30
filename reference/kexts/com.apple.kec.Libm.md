# `com.apple.kec.Libm`

- Name: Libm.kext
- Version: `1`
- UUID: `C3EB3438-717A-30B4-9B9D-E3F4B920FCC5`
- Source version: `3326.40.2.0.0`
- Depends on: [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0d0

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
Commands      = 10 (Size: 720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00007098 off=0x00110000-0x00117098 addr=0xfffffe0007114000-0xfffffe000711b098 r--/r--   __TEXT            
	sz=0x00006d68 off=0x00110330-0x00117098 addr=0xfffffe0007114330-0xfffffe000711b098               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00003988 off=0x01510000-0x01513988 addr=0xfffffe0008514000-0xfffffe0008517988 r-x/r-x   __TEXT_EXEC       
	sz=0x00003988 off=0x01510000-0x01513988 addr=0xfffffe0008514000-0xfffffe0008517988          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
002: LC_SEGMENT_64 sz=0x000000dc off=0x04924000-0x049240dc addr=0xfffffe000b928000-0xfffffe000b9280dc rw-/rw-   __DATA            
	sz=0x000000dc off=0x04924000-0x049240dc addr=0xfffffe000b928000-0xfffffe000b9280dc               __DATA.__data             
003: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
004: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
005: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: None
	 External Reloc Entries: None
	    Local Reloc Entries: None
006: LC_UUID                     C3EB3438-717A-30B4-9B9D-E3F4B920FCC5
007: LC_BUILD_VERSION            Platform: iOSKernelKit, MinOS: 27.2, SDK: 27.2, Tool: ld (27106)
008: LC_SOURCE_VERSION           3326.40.2.0.0
009: LC_FUNCTION_STARTS          offset=0x004a94cf0 size=0x50
```

## Info.plist keys [KC]

- `AppleKernelExternalComponent`: `True`
- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `Libm`
- `CFBundleIdentifier`: `com.apple.kec.Libm`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `Libm.kext`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `KernelKit.iPhoneOS`
- `CFBundleVersion`: `1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `kernelkit.iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: ``
- `DTSDKName`: `kernelkit.iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `NSHumanReadableCopyright`: `Copyright © 2003-2013 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0d0`
- `OSBundleRequired`: `Console`
- `OSBundleUUID`: `<data 32 chars>`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/KernelKit/System/Library/Extensions/Libm.kext`
- `_PrelinkExecutableLoadAddr`: `-2198904684544`
- `_PrelinkExecutableRelativePath`: `Libm`
- `_PrelinkExecutableSize`: `43772`
- `_PrelinkExecutableSourceAddr`: `-2198904684544`
- `_PrelinkKmodInfo`: `-2198829105152`

## Strings (0) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.
