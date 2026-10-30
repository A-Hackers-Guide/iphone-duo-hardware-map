# `com.apple.driver.IOSlaveProcessor`

- Name: IOSlaveProcessor
- Version: `1`
- UUID: `A54D778B-E0B2-3118-8AB8-31AAADAF0779`
- Source version: `26.0.0.0.0`
- Depends on: [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (6) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOSlaveCPU` | 0x90 | IOService → IORegistryEntry |
| `IOSlaveEndpoint` | 0x70 | IOEventSource |
| `IOSlaveFirmware` | 0x88 | IOService → IORegistryEntry |
| `IOSlaveMemory` | 0x10 |  |
| `IOSlaveMemoryBuffer` | 0x30 | IOSlaveMemory |
| `IOSlaveProcessor` | 0xa8 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000706 off=0x00a5c3c0-0x00a5cac6 addr=0xfffffe0007a603c0-0xfffffe0007a60ac6 r--/r--   __TEXT            
	sz=0x0000012e off=0x00a5c998-0x00a5cac6 addr=0xfffffe0007a60998-0xfffffe0007a60ac6               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00001958 off=0x033c7720-0x033c9078 addr=0xfffffe000a3cb720-0xfffffe000a3cd078 r-x/r-x   __TEXT_EXEC       
	sz=0x000017f8 off=0x033c7720-0x033c8f18 addr=0xfffffe000a3cb720-0xfffffe000a3ccf18          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000160 off=0x033c8f18-0x033c9078 addr=0xfffffe000a3ccf18-0xfffffe000a3cd078          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001c8 off=0x04a167a0-0x04a16968 addr=0xfffffe000ba1a7a0-0xfffffe000ba1a968 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a167a0-0x04a16868 addr=0xfffffe000ba1a7a0-0xfffffe000ba1a868               __DATA.__data             
	sz=0x00000100 off=0x00000000-0x00000100 addr=0xfffffe000ba1a868-0xfffffe000ba1a968               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001950 off=0x013ec248-0x013edb98 addr=0xfffffe00083f0248-0xfffffe00083f1b98 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x013ec248-0x013ec250 addr=0xfffffe00083f0248-0xfffffe00083f0250         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x013ec250-0x013ec258 addr=0xfffffe00083f0250-0xfffffe00083f0258         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000016c8 off=0x013ec258-0x013ed920 addr=0xfffffe00083f0258-0xfffffe00083f1920         __DATA_CONST.__const            
	sz=0x00000180 off=0x013ed920-0x013edaa0 addr=0xfffffe00083f1920-0xfffffe00083f1aa0         __DATA_CONST.__kalloc_type      
	sz=0x000000b0 off=0x013edaa0-0x013edb50 addr=0xfffffe00083f1aa0-0xfffffe00083f1b50         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000048 off=0x013edb50-0x013edb98 addr=0xfffffe00083f1b50-0xfffffe00083f1b98         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 53 at 0x04af7cbc
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     A54D778B-E0B2-3118-8AB8-31AAADAF0779
008: LC_SOURCE_VERSION           26.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac55a8 size=0x80
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOSlaveProcessor`
- `CFBundleIdentifier`: `com.apple.driver.IOSlaveProcessor`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOSlaveProcessor`
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
- `NSHumanReadableCopyright`: `Copyright © 2021 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOSlaveProcessor.kext`
- `_PrelinkExecutableLoadAddr`: `-2198894935104`
- `_PrelinkExecutableRelativePath`: `IOSlaveProcessor`
- `_PrelinkExecutableSize`: `15222`
- `_PrelinkExecutableSourceAddr`: `-2198894935104`
- `_PrelinkKmodInfo`: `-2198828111968`

## Strings (18) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.IOSlaveProcessor`
- `IOSlaveEndpoint`
- `site.IOSlaveEndpoint`
- `12111211111121`
- `IOSlaveMemory`
- `site.IOSlaveFirmware`
- `12111112122212121`
- `IOSlaveProcessor`
- `12`
- `site.IOSlaveMemoryBuffer`
- `121212`
- `121111121222121211121`
- `IOSlaveMemoryBuffer`
- `site.IOSlaveMemory`
- `IOSlaveFirmware`
- `IOSlaveCPU`
- `site.IOSlaveCPU`
- `121111121222121211`
