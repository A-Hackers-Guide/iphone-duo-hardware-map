# `com.apple.iokit.IOPortFamily`

- Name: IOPortFamily
- Version: `1.0`
- UUID: `ED366707-43CA-3EE2-95B8-739968D06642`
- Source version: `95.0.0.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0.0b1, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

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
000: LC_SEGMENT_64 sz=0x00004000 off=0x00a4d380-0x00a51380 addr=0xfffffe0007a51380-0xfffffe0007a55380 r--/r--   __TEXT            
001: LC_SEGMENT_64 sz=0x00000084 off=0x03355390-0x03355414 addr=0xfffffe000a359390-0xfffffe000a359414 r-x/r-x   __TEXT_EXEC       
	sz=0x00000084 off=0x03355390-0x03355414 addr=0xfffffe000a359390-0xfffffe000a359414          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
002: LC_SEGMENT_64 sz=0x000000d8 off=0x04a14f20-0x04a14ff8 addr=0xfffffe000ba18f20-0xfffffe000ba18ff8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a14f20-0x04a14fe8 addr=0xfffffe000ba18f20-0xfffffe000ba18fe8               __DATA.__data             
	sz=0x00000010 off=0x00000000-0x00000010 addr=0xfffffe000ba18fe8-0xfffffe000ba18ff8               __DATA.__common           (Zerofill)
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
006: LC_UUID                     ED366707-43CA-3EE2-95B8-739968D06642
007: LC_SOURCE_VERSION           95.0.0.0.0
008: LC_FUNCTION_STARTS          offset=0x004ac4400 size=0x10
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `IOPortFamily`
- `CFBundleIdentifier`: `com.apple.iokit.IOPortFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOPortFamily`
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
- `NSHumanReadableCopyright`: `Copyright © 2023 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOPortFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198894996608`
- `_PrelinkExecutableRelativePath`: `IOPortFamily`
- `_PrelinkExecutableSize`: `16732`
- `_PrelinkExecutableSourceAddr`: `-2198894996608`
- `_PrelinkKmodInfo`: `-2198828118240`

## Strings (0) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.
