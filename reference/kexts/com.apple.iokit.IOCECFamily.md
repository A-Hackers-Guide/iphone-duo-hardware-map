# `com.apple.iokit.IOCECFamily`

- Name: IOCECFamily
- Version: `1`
- UUID: `858813EA-4DB8-3088-820B-9B571C618F9C`
- Source version: `69.0.2.0.0`
- Depends on: [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOCECMergeProperties` | 0x90 | IOService → IORegistryEntry |
| `IOCECService` | 0xf0 | IOService → IORegistryEntry |
| `IOCECUserClient` | 0xe8 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000a36 off=0x009c35e0-0x009c4016 addr=0xfffffe00079c75e0-0xfffffe00079c8016 r--/r--   __TEXT            
	sz=0x0000040e off=0x009c3c08-0x009c4016 addr=0xfffffe00079c7c08-0xfffffe00079c8016               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00002468 off=0x03081370-0x030837d8 addr=0xfffffe000a085370-0xfffffe000a0877d8 r-x/r-x   __TEXT_EXEC       
	sz=0x00002348 off=0x03081370-0x030836b8 addr=0xfffffe000a085370-0xfffffe000a0876b8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000120 off=0x030836b8-0x030837d8 addr=0xfffffe000a0876b8-0xfffffe000a0877d8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000150 off=0x049ef190-0x049ef2e0 addr=0xfffffe000b9f3190-0xfffffe000b9f32e0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049ef190-0x049ef258 addr=0xfffffe000b9f3190-0xfffffe000b9f3258               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000b9f3258-0xfffffe000b9f32e0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001590 off=0x01354908-0x01355e98 addr=0xfffffe0008358908-0xfffffe0008359e98 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x01354908-0x01354920 addr=0xfffffe0008358908-0xfffffe0008358920         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x01354920-0x01354938 addr=0xfffffe0008358920-0xfffffe0008358938         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001388 off=0x01354938-0x01355cc0 addr=0xfffffe0008358938-0xfffffe0008359cc0         __DATA_CONST.__const            
	sz=0x000000c0 off=0x01355cc0-0x01355d80 addr=0xfffffe0008359cc0-0xfffffe0008359d80         __DATA_CONST.__kalloc_type      
	sz=0x00000050 off=0x01355d80-0x01355dd0 addr=0xfffffe0008359d80-0xfffffe0008359dd0         __DATA_CONST.__assert           
	sz=0x00000090 off=0x01355dd0-0x01355e60 addr=0xfffffe0008359dd0-0xfffffe0008359e60         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000038 off=0x01355e60-0x01355e98 addr=0xfffffe0008359e60-0xfffffe0008359e98         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 43 at 0x04af0e70
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     858813EA-4DB8-3088-820B-9B571C618F9C
008: LC_SOURCE_VERSION           69.0.2.0.0
009: LC_FUNCTION_STARTS          offset=0x004abe1f0 size=0x80
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOCECFamily`
- `CFBundleIdentifier`: `com.apple.iokit.IOCECFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOCECFamily`
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
- `NSHumanReadableCopyright`: `Copyright © 2013 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOCECFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895561248`
- `_PrelinkExecutableRelativePath`: `IOCECFamily`
- `_PrelinkExecutableSize`: `17790`
- `_PrelinkExecutableSourceAddr`: `-2198895561248`
- `_PrelinkKmodInfo`: `-2198828273264`

## Strings (34) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%s: ok=%u\n`
- `%s: enter\n`
- `virtual IOReturn IOCECUserClient::open()`
- `(unsigned int)n < sizeof(string.c_str)`
- `virtual IOReturn IOCECUserClient::close()`
- `receiveCECGated`
- `notifying hpd = %d hibernate = %d physicalAddress = 0x%04x\n`
- `IOCECMergeProperties`
- `121111121222121211`
- `IOProviderMergeProperties`
- `site.IOCECService`
- `IOUserClientClass`
- `sendStatusUpdate`
- `n > 0`
- `12111112122212121111111111111`
- `virtual IOReturn IOCECUserClient::clientClose()`
- `virtual IOReturn IOCECUserClient::clientMemoryForType(UInt32, IOOptionBits *, IOMemoryDescriptor **)`
- ` hpd = %d\n`
- `%*D`
- `virtual bool IOCECUserClient::didTerminate(IOService *, IOOptionBits, bool *)`
- `site.IOCECMergeProperties`
- `IOCECService`
- `%s: message frame received with no _queue; this is a bug!\n`
- `%x.%x.%x.%x`
- `virtual bool IOCECUserClient::start(IOService *)`
- `%s: ret=0x%08x\n`
- `%s: overflow - queue is full, frame dropped!\n`
- `hibernate = %d\n`
- `IOCECTypes.c`
- `IOCECUserClient`
- `virtual IOReturn IOCECUserClient::registerNotificationPort(mach_port_t, UInt32, io_user_reference_t)`
- `121111121222121211122222222222`
- ` `
- `site.IOCECUserClient`
