# `com.apple.driver.AppleNANDConfigAccess`

- Name: AppleNANDConfigAccess
- Version: `1.0.0`
- UUID: `0AAB3CB9-AB99-3E72-BF54-D14EAFB21ACB`
- Source version: `8.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleNANDConfigAccess` | 0x88 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000061b off=0x00685700-0x00685d1b addr=0xfffffe0007689700-0xfffffe0007689d1b r--/r--   __TEXT            
	sz=0x00000043 off=0x00685cd8-0x00685d1b addr=0xfffffe0007689cd8-0xfffffe0007689d1b               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00000454 off=0x022dd930-0x022ddd84 addr=0xfffffe00092e1930-0xfffffe00092e1d84 r-x/r-x   __TEXT_EXEC       
	sz=0x000003e4 off=0x022dd930-0x022ddd14 addr=0xfffffe00092e1930-0xfffffe00092e1d14          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000070 off=0x022ddd14-0x022ddd84 addr=0xfffffe00092e1d14-0xfffffe00092e1d84          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x049827d8-0x049828d8 addr=0xfffffe000b9867d8-0xfffffe000b9868d8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049827d8-0x049828a0 addr=0xfffffe000b9867d8-0xfffffe000b9868a0               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9868a0-0xfffffe000b9868d8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000006a0 off=0x0117fd68-0x01180408 addr=0xfffffe0008183d68-0xfffffe0008184408 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x0117fd68-0x0117fd70 addr=0xfffffe0008183d68-0xfffffe0008183d70         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x0117fd70-0x0117fd78 addr=0xfffffe0008183d70-0xfffffe0008183d78         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000610 off=0x0117fd78-0x01180388 addr=0xfffffe0008183d78-0xfffffe0008184388         __DATA_CONST.__const            
	sz=0x00000040 off=0x01180388-0x011803c8 addr=0xfffffe0008184388-0xfffffe00081843c8         __DATA_CONST.__kalloc_type      
	sz=0x00000038 off=0x011803c8-0x01180400 addr=0xfffffe00081843c8-0xfffffe0008184400         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000008 off=0x01180400-0x01180408 addr=0xfffffe0008184400-0xfffffe0008184408         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 15 at 0x04ae0ba8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     0AAB3CB9-AB99-3E72-BF54-D14EAFB21ACB
008: LC_SOURCE_VERSION           8.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aab6d8 size=0x20
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleNANDConfigAccess`
- `CFBundleIdentifier`: `com.apple.driver.AppleNANDConfigAccess`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleNANDConfigAccess`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleSignature`: `????`
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
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleNANDConfigAccess.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898960640`
- `_PrelinkExecutableRelativePath`: `AppleNANDConfigAccess`
- `_PrelinkExecutableSize`: `4623`
- `_PrelinkExecutableSourceAddr`: `-2198898960640`
- `_PrelinkKmodInfo`: `-2198828718120`

## Strings (3) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AppleNANDConfigAccess`
- `site.AppleNANDConfigAccess`
- `12111112122212121`
