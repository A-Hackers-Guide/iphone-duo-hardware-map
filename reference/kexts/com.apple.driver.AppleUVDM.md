# `com.apple.driver.AppleUVDM`

- Name: AppleUVDM
- Version: `1.0.0`
- UUID: `E8BC238B-6DBB-3868-A10C-9EE0C1E50198`
- Source version: `29.0.0.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 22.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUVDMEndpointInterface` | 0x90 | IOService → IORegistryEntry |
| `AppleUVDMUserClient` | 0xf0 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000a2a off=0x008e0630-0x008e105a addr=0xfffffe00078e4630-0xfffffe00078e505a r--/r--   __TEXT            
	sz=0x00000452 off=0x008e0c08-0x008e105a addr=0xfffffe00078e4c08-0xfffffe00078e505a               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00001f4c off=0x02b630c0-0x02b6500c addr=0xfffffe0009b670c0-0xfffffe0009b6900c r-x/r-x   __TEXT_EXEC       
	sz=0x00001e2c off=0x02b630c0-0x02b64eec addr=0xfffffe0009b670c0-0xfffffe0009b68eec          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000120 off=0x02b64eec-0x02b6500c addr=0xfffffe0009b68eec-0xfffffe0009b6900c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000130 off=0x049d1d58-0x049d1e88 addr=0xfffffe000b9d5d58-0xfffffe000b9d5e88 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049d1d58-0x049d1e20 addr=0xfffffe000b9d5d58-0xfffffe000b9d5e20               __DATA.__data             
	sz=0x00000068 off=0x00000000-0x00000068 addr=0xfffffe000b9d5e20-0xfffffe000b9d5e88               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000f20 off=0x012b2f60-0x012b3e80 addr=0xfffffe00082b6f60-0xfffffe00082b7e80 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x012b2f60-0x012b2f70 addr=0xfffffe00082b6f60-0xfffffe00082b6f70         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x012b2f70-0x012b2f80 addr=0xfffffe00082b6f70-0xfffffe00082b6f80         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000dc8 off=0x012b2f80-0x012b3d48 addr=0xfffffe00082b6f80-0xfffffe00082b7d48         __DATA_CONST.__const            
	sz=0x00000080 off=0x012b3d48-0x012b3dc8 addr=0xfffffe00082b7d48-0xfffffe00082b7dc8         __DATA_CONST.__kalloc_type      
	sz=0x00000090 off=0x012b3dc8-0x012b3e58 addr=0xfffffe00082b7dc8-0xfffffe00082b7e58         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000028 off=0x012b3e58-0x012b3e80 addr=0xfffffe00082b7e58-0xfffffe00082b7e80         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 41 at 0x04aecd90
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     E8BC238B-6DBB-3868-A10C-9EE0C1E50198
008: LC_SOURCE_VERSION           29.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab7d60 size=0x50
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleUVDM`
- `CFBundleGetInfoString`: `Copyright © 2022-2023 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleUVDM`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUVDM`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2022-2023 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleLibraries_x86_64`: `{}`
- `OSBundleRequired`: `Local-Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleUVDM.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896490960`
- `_PrelinkExecutableRelativePath`: `AppleUVDM`
- `_PrelinkExecutableSize`: `14790`
- `_PrelinkExecutableSourceAddr`: `-2198896490960`
- `_PrelinkKmodInfo`: `-2198828393128`

## Strings (40) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `getTransportParameters`
- `AppleUVDMEndpointInterface`
- `site.AppleUVDMEndpointInterface`
- `121111121222121211`
- `IOUserClientEntitlements`
- `initWithTask`
- `open`
- `readAccess`
- `%s::%s - failCode 0x%X\n`
- `unlockBus`
- `%s::%s - Provider not an AppleUVDMEndpoint\n`
- `writeStream`
- `readStream`
- `root`
- `%s::%s - Endpoint provider open() failed. Already opened for exclsuive access by another service\n`
- `%s::%s - outBufLen %u\n\n`
- `%s::%s - inBufLen %u, protoLen %u\n\n`
- `%s::%s - User client does NOT have admin priviledge!\n`
- `%s::%s - Not open\n`
- `%s::%s - outBufLen %u, protoBufLen %u\n\n`
- `AppleUVDMUserClient`
- `site.AppleUVDMUserClient`
- `com.apple.private.AppleUVDMUserClient.access`
- `%s::%s - Could not open user client\n`
- `%s::%s - Can't create descriptor\n`
- `%s::%s - inBufLen %u, offset 0x%X\n\n`
- `121111121222121211111111111112`
- `IOUserClientDefaultLocking`
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `%s::%s - Failed\n`
- `writeAccess`
- `start`
- `IOUserClientDefaultLockingSetProperties`
- `%s::%s - Service inactive\n`
- `%s::%s - Attempting to close for a different client\n`
- `%s::%s - Not attached\n`
- `lockBus`
- `%s::%s - Attempting to open for a different client\n`
- `close`
- `%s::%s - Cannot lock\n`
