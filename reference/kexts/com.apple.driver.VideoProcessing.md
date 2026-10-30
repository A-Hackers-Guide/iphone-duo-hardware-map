# `com.apple.driver.VideoProcessing`

- Name: VCPDRM
- Version: `1.0`
- UUID: `E5E75784-9862-3F90-9AB9-01EF37B1D5DA`
- Source version: `1415.6.1.0.0`
- Depends on: [`com.apple.driver.AppleMobileFileIntegrity`](com.apple.driver.AppleMobileFileIntegrity.md) 1.0.1, [`com.apple.iokit.IOSurface`](com.apple.iokit.IOSurface.md) 87.0, [`com.apple.kec.Libm`](com.apple.kec.Libm.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0b1, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0b1, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0b1, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0b1, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 9.0.0b1

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### VideoProcessingDRM
- `CFBundleIdentifier`: `com.apple.driver.VideoProcessing`
- `IOClass`: `VCPDRMService`
- `IOMatchCategory`: `VCPDRMService`
- `IOPersonalityPublisher`: `com.apple.driver.VideoProcessing`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOBSD`
- `IOUserClientClass`: `VCPDRMServiceUserClient`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `VCPDRMService` | 0x98 | IOService → IORegistryEntry |
| `VCPDRMUserClient` | 0x410 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000a7c off=0x00da8cd0-0x00da974c addr=0xfffffe0007daccd0-0xfffffe0007dad74c r--/r--   __TEXT            
	sz=0x000000a9 off=0x00da9398-0x00da9441 addr=0xfffffe0007dad398-0xfffffe0007dad441               __TEXT.__os_log           
	sz=0x00000008 off=0x00da9448-0x00da9450 addr=0xfffffe0007dad448-0xfffffe0007dad450               __TEXT.__const            
	sz=0x000002fc off=0x00da9450-0x00da974c addr=0xfffffe0007dad450-0xfffffe0007dad74c               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x000012fc off=0x039a9820-0x039aab1c addr=0xfffffe000a9ad820-0xfffffe000a9aeb1c r-x/r-x   __TEXT_EXEC       
	sz=0x0000111c off=0x039a9820-0x039aa93c addr=0xfffffe000a9ad820-0xfffffe000a9ae93c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001e0 off=0x039aa93c-0x039aab1c addr=0xfffffe000a9ae93c-0xfffffe000a9aeb1c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x04a35ce0-0x04a35e08 addr=0xfffffe000ba39ce0-0xfffffe000ba39e08 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x04a35ce0-0x04a35da4 addr=0xfffffe000ba39ce0-0xfffffe000ba39da4               __DATA.__data             
	sz=0x00000010 off=0x00000000-0x00000010 addr=0xfffffe000ba39da8-0xfffffe000ba39db8               __DATA.__common           (Zerofill)
	sz=0x00000050 off=0x00000000-0x00000050 addr=0xfffffe000ba39db8-0xfffffe000ba39e08               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00000e98 off=0x014a1c80-0x014a2b18 addr=0xfffffe00084a5c80-0xfffffe00084a6b18 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x014a1c80-0x014a1c90 addr=0xfffffe00084a5c80-0xfffffe00084a5c90         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x014a1c90-0x014a1ca0 addr=0xfffffe00084a5c90-0xfffffe00084a5ca0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000cc0 off=0x014a1ca0-0x014a2960 addr=0xfffffe00084a5ca0-0xfffffe00084a6960         __DATA_CONST.__const            
	sz=0x00000080 off=0x014a2960-0x014a29e0 addr=0xfffffe00084a6960-0xfffffe00084a69e0         __DATA_CONST.__kalloc_type      
	sz=0x000000f0 off=0x014a29e0-0x014a2ad0 addr=0xfffffe00084a69e0-0xfffffe00084a6ad0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000048 off=0x014a2ad0-0x014a2b18 addr=0xfffffe00084a6ad0-0xfffffe00084a6b18         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 69 at 0x04afe8c8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     E5E75784-9862-3F90-9AB9-01EF37B1D5DA
008: LC_SOURCE_VERSION           1415.6.1.0.0
009: LC_FUNCTION_STARTS          offset=0x004accd88 size=0x30
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `VCPDRM`
- `CFBundleIdentifier`: `com.apple.driver.VideoProcessing`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `VCPDRM`
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
- `NSHumanReadableCopyright`: `Copyright © 2020 Apple. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Safe Boot`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/VCPDRM.kext`
- `_PrelinkExecutableLoadAddr`: `-2198891475760`
- `_PrelinkExecutableRelativePath`: `VCPDRM`
- `_PrelinkExecutableSize`: `11576`
- `_PrelinkExecutableSourceAddr`: `-2198891475760`
- `_PrelinkKmodInfo`: `-2198827983648`

## Strings (21) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `%s: %p newConnect: %p\n`
- `%s: %p init: %p succeeded\n`
- `%s: %p attaching %p succeeded\n`
- `%s: %p starting %p succeeded\n`
- `%s: failed to find IOSurfaceRoot service`
- `%s: %p: type %d\n`

**[__TEXT.__cstring]**

- `site.VCPDRMService`
- `IOCoreSurfaceRoot`
- `B24@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{IONotifier=^^?i}16`
- `VCPDRMUserClient`
- `1211111212221212111111111111112222211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221`
- `\"Specified surface size (%i) not within expected size (%i,%i)\" @%s:%d`
- `VCPDRMHitCountImpl.cpp`
- `VCPDRMService`
- `start_block_invoke`
- `\"VCPDPUserClient: missing mapping for mapping id %lld\\n\" @%s:%d`
- `\"VCPDRMHitCount: too many calls in current period (%i)\" @%s:%d`
- `1211111212221212111`
- `virtual IOReturn VCPDRMService::newUserClient(task_t, void *, UInt32, IOUserClient **)`
- `site.VCPDRMUserClient`
- `VCPDRMUserClient.cpp`
