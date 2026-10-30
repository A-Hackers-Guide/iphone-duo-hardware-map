# `com.apple.AGXFirmwareKextRTBuddy64`

- Name: AGXFirmwareKextRTBuddy64
- Version: `362.5`
- UUID: `879AFFDB-B9AF-301C-847A-EC9256574A1A`
- Source version: `362.5.0.0.0`
- Depends on: [`com.apple.driver.RTBuddy`](com.apple.driver.RTBuddy.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0

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
Commands      = 9 (Size: 688)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00004000 off=0x0011b190-0x0011f190 addr=0xfffffe000711f190-0xfffffe0007123190 r--/r--   __TEXT            
001: LC_SEGMENT_64 sz=0x00000048 off=0x01529710-0x01529758 addr=0xfffffe000852d710-0xfffffe000852d758 r-x/r-x   __TEXT_EXEC       
	sz=0x00000048 off=0x01529710-0x01529758 addr=0xfffffe000852d710-0xfffffe000852d758          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
002: LC_SEGMENT_64 sz=0x000000d8 off=0x04924530-0x04924608 addr=0xfffffe000b928530-0xfffffe000b928608 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x04924530-0x049245f4 addr=0xfffffe000b928530-0xfffffe000b9285f4               __DATA.__data             
	sz=0x00000010 off=0x00000000-0x00000010 addr=0xfffffe000b9285f8-0xfffffe000b928608               __DATA.__common           (Zerofill)
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
006: LC_UUID                     879AFFDB-B9AF-301C-847A-EC9256574A1A
007: LC_SOURCE_VERSION           362.5.0.0.0
008: LC_FUNCTION_STARTS          offset=0x004a94fd0 size=0x8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AGXFirmwareKextRTBuddy64`
- `CFBundleIdentifier`: `com.apple.AGXFirmwareKextRTBuddy64`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AGXFirmwareKextRTBuddy64`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `362.5`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `362.5`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2014 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AGXFirmwareKextRTBuddy64.kext`
- `_PrelinkExecutableLoadAddr`: `-2198904639088`
- `_PrelinkExecutableRelativePath`: `AGXFirmwareKextRTBuddy64`
- `_PrelinkExecutableSize`: `16672`
- `_PrelinkExecutableSourceAddr`: `-2198904639088`
- `_PrelinkKmodInfo`: `-2198829103824`

## Strings (0) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.
