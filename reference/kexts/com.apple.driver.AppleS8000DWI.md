# `com.apple.driver.AppleS8000DWI`

- Name: AppleS8000DWI
- Version: `1.0.0d1`
- UUID: `E8FA85F7-4223-34CB-82DB-C11101C4EF70`
- Source version: `140.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleS8000DWI
- `CFBundleIdentifier`: `com.apple.driver.AppleS8000DWI`
- `IOClass`: `AppleS8000DWI`
- `IONameMatch`: `dwi,s8000`
- `IOPersonalityPublisher`: `com.apple.driver.AppleS8000DWI`
- `IOPlatformActiveAction`: `80000`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleS8000DWI` | 0x140 | IOService → IORegistryEntry |
| `AppleS8000DWIBacklightFunction` | 0x38 | AppleARMFunction |
| `AppleS8000DWIVoltageFunction` | 0x38 | AppleARMFunction |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000083f off=0x006d59f0-0x006d622f addr=0xfffffe00076d99f0-0xfffffe00076da22f r--/r--   __TEXT            
	sz=0x00000008 off=0x006d6018-0x006d6020 addr=0xfffffe00076da018-0xfffffe00076da020               __TEXT.__const            
	sz=0x0000020f off=0x006d6020-0x006d622f addr=0xfffffe00076da020-0xfffffe00076da22f               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00001958 off=0x02481480-0x02482dd8 addr=0xfffffe0009485480-0xfffffe0009486dd8 r-x/r-x   __TEXT_EXEC       
	sz=0x000017b8 off=0x02481480-0x02482c38 addr=0xfffffe0009485480-0xfffffe0009486c38          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001a0 off=0x02482c38-0x02482dd8 addr=0xfffffe0009486c38-0xfffffe0009486dd8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000150 off=0x04990230-0x04990380 addr=0xfffffe000b994230-0xfffffe000b994380 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04990230-0x049902f8 addr=0xfffffe000b994230-0xfffffe000b9942f8               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000b9942f8-0xfffffe000b994380               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000a50 off=0x011c2b40-0x011c3590 addr=0xfffffe00081c6b40-0xfffffe00081c7590 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x011c2b40-0x011c2b48 addr=0xfffffe00081c6b40-0xfffffe00081c6b48         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x011c2b48-0x011c2b50 addr=0xfffffe00081c6b48-0xfffffe00081c6b50         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000860 off=0x011c2b50-0x011c33b0 addr=0xfffffe00081c6b50-0xfffffe00081c73b0         __DATA_CONST.__const            
	sz=0x000000c0 off=0x011c33b0-0x011c3470 addr=0xfffffe00081c73b0-0xfffffe00081c7470         __DATA_CONST.__kalloc_type      
	sz=0x000000d0 off=0x011c3470-0x011c3540 addr=0xfffffe00081c7470-0xfffffe00081c7540         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000050 off=0x011c3540-0x011c3590 addr=0xfffffe00081c7540-0xfffffe00081c7590         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 62 at 0x04ae379c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     E8FA85F7-4223-34CB-82DB-C11101C4EF70
008: LC_SOURCE_VERSION           140.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aaeca8 size=0x50
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleS8000DWI`
- `CFBundleIdentifier`: `com.apple.driver.AppleS8000DWI`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleS8000DWI`
- `CFBundleNumericVersion`: `16785409`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
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
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
  - `2`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleS8000DWI.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898632208`
- `_PrelinkExecutableRelativePath`: `AppleS8000DWI`
- `_PrelinkExecutableSize`: `11575`
- `_PrelinkExecutableSourceAddr`: `-2198898632208`
- `_PrelinkKmodInfo`: `-2198828662224`

## Strings (21) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AppleS8000DWI`
- `nclk-div`
- `polarity-config`
- `lockout-us`
- `voltages-buck%x`
- `AppleS8000DWI.cpp`
- `\"AppleS5L8940DWI::_waitTransaction timeout for register %x\" @%s:%d`
- `soc-buck`
- `slave-select`
- `1211111`
- `AppleS8000DWIBacklightFunction`
- `dwi-version`
- `start`
- `site.AppleS8000DWIVoltageFunction`
- `site.AppleS8000DWIBacklightFunction`
- `site.AppleS8000DWI`
- `1211111212221212111212222222212221222122`
- `str-delay`
- `AppleS8000DWI::%s v%u _dwiBaseAddress: %#lx, buck mask = 0x%08x\n`
- `\"AppleS8000DWI::sendWLED: version: %x is unsupported\\n\" @%s:%d`
- `AppleS8000DWIVoltageFunction`
