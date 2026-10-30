# `com.apple.driver.ASIOKit`

- Name: ASIOKit
- Version: `27.2.9`
- UUID: `76021278-0FB7-3FF9-9746-A2F676504B0F`
- Source version: `27.2.9.0.0`
- Depends on: [`com.apple.driver.AppleSSE`](com.apple.driver.AppleSSE.md) 1.0, [`com.apple.iokit.IOAccessoryManager`](com.apple.iokit.IOAccessoryManager.md) 1.0.0, [`com.apple.kec.corecrypto`](com.apple.kec.corecrypto.md) 1, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 9.3.1

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### ASIOKit
- `CFBundleIdentifier`: `com.apple.driver.ASIOKit`
- `IOClass`: `ASIOKit`
- `IOKitDebug`: `0`
- `IOMatchCategory`: `ASIOKit`
- `IOPersonalityPublisher`: `com.apple.driver.ASIOKit`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOKit`
- `IOUserClientClass`: `ASIOKitUserClient`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `ASIOKit` | 0x98 | IOService → IORegistryEntry |
| `ASIOKitUserClient` | 0xf0 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000098d0 off=0x00141a70-0x0014b340 addr=0xfffffe0007145a70-0xfffffe000714f340 r--/r--   __TEXT            
	sz=0x000000d2 off=0x00142098-0x0014216a addr=0xfffffe0007146098-0xfffffe000714616a               __TEXT.__cstring          (CstringLiterals)
	sz=0x000091d0 off=0x00142170-0x0014b340 addr=0xfffffe0007146170-0xfffffe000714f340               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00050c30 off=0x0160dc70-0x0165e8a0 addr=0xfffffe0008611c70-0xfffffe00086628a0 r-x/r-x   __TEXT_EXEC       
	sz=0x00050a40 off=0x0160dc70-0x0165e6b0 addr=0xfffffe0008611c70-0xfffffe00086626b0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001f0 off=0x0165e6b0-0x0165e8a0 addr=0xfffffe00086626b0-0xfffffe00086628a0          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001b8 off=0x0492dd30-0x0492dee8 addr=0xfffffe000b931d30-0xfffffe000b931ee8 rw-/rw-   __DATA            
	sz=0x00000158 off=0x0492dd30-0x0492de88 addr=0xfffffe000b931d30-0xfffffe000b931e88               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b931e88-0xfffffe000b931ee8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000036b0 off=0x00f8c100-0x00f8f7b0 addr=0xfffffe0007f90100-0xfffffe0007f937b0 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x00f8c100-0x00f8c110 addr=0xfffffe0007f90100-0xfffffe0007f90110         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x00f8c110-0x00f8c120 addr=0xfffffe0007f90110-0xfffffe0007f90120         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000034c0 off=0x00f8c120-0x00f8f5e0 addr=0xfffffe0007f90120-0xfffffe0007f935e0         __DATA_CONST.__const            
	sz=0x00000080 off=0x00f8f5e0-0x00f8f660 addr=0xfffffe0007f935e0-0xfffffe0007f93660         __DATA_CONST.__kalloc_type      
	sz=0x000000f8 off=0x00f8f660-0x00f8f758 addr=0xfffffe0007f93660-0xfffffe0007f93758         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000058 off=0x00f8f758-0x00f8f7b0 addr=0xfffffe0007f93758-0xfffffe0007f937b0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 73 at 0x04ad0b90
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     76021278-0FB7-3FF9-9746-A2F676504B0F
008: LC_SOURCE_VERSION           27.2.9.0.0
009: LC_FUNCTION_STARTS          offset=0x004a96380 size=0x90
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `ASIOKit`
- `CFBundleIdentifier`: `com.apple.driver.ASIOKit`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `ASIOKit`
- `CFBundleNumericVersion`: `657031168`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `27.2.9`
- `CFBundleSignature`: `APPL`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `27.2.9`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2008-2026 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/ASIOKit.kext`
- `_PrelinkExecutableLoadAddr`: `-2198904481168`
- `_PrelinkExecutableRelativePath`: `ASIOKit`
- `_PrelinkExecutableSize`: `384360`
- `_PrelinkExecutableSourceAddr`: `-2198904481168`
- `_PrelinkKmodInfo`: `-2198829064912`

## Strings (11) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `IOAccessoryManager`
- `site.ASIOKitUserClient`
- `site.ASIOKit`
- `1211111212221212111`
- `IOPortTransportState`
- `ASIOKitUserClient`
- `121111121222121211111111111112`
- `com.apple.private.asiokit.allow`
- `ASIOKit`
- `IOPMPowerSource`
- `AppleSSE`
