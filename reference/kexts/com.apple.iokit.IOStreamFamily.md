# `com.apple.iokit.IOStreamFamily`

- Name: IOStreamFamily
- Version: `1.1.0`
- UUID: `E18D7509-A7F0-36A0-AE1C-1F0746A95644`
- Source version: `120.0.0.0.0`
- Depends on: [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (4) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOStream` | 0xe8 | IOService → IORegistryEntry |
| `IOStreamBuffer` | 0x38 |  |
| `IOStreamUserClient` | 0xf8 | IOUserClient → IOService → IORegistryEntry |
| `IOStreamUserClientInit` | 0x88 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000764 off=0x00a5f7e0-0x00a5ff44 addr=0xfffffe0007a637e0-0xfffffe0007a63f44 r--/r--   __TEXT            
	sz=0x00000008 off=0x00a5fe08-0x00a5fe10 addr=0xfffffe0007a63e08-0xfffffe0007a63e10               __TEXT.__const            
	sz=0x00000134 off=0x00a5fe10-0x00a5ff44 addr=0xfffffe0007a63e10-0xfffffe0007a63f44               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x000037ac off=0x033e75b0-0x033ead5c addr=0xfffffe000a3eb5b0-0xfffffe000a3eed5c r-x/r-x   __TEXT_EXEC       
	sz=0x0000364c off=0x033e75b0-0x033eabfc addr=0xfffffe000a3eb5b0-0xfffffe000a3eebfc          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000160 off=0x033eabfc-0x033ead5c addr=0xfffffe000a3eebfc-0xfffffe000a3eed5c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000178 off=0x04a16e50-0x04a16fc8 addr=0xfffffe000ba1ae50-0xfffffe000ba1afc8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a16e50-0x04a16f18 addr=0xfffffe000ba1ae50-0xfffffe000ba1af18               __DATA.__data             
	sz=0x000000b0 off=0x00000000-0x000000b0 addr=0xfffffe000ba1af18-0xfffffe000ba1afc8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001920 off=0x013f42c0-0x013f5be0 addr=0xfffffe00083f82c0-0xfffffe00083f9be0 rw-/rw-   __DATA_CONST      
	sz=0x00000020 off=0x013f42c0-0x013f42e0 addr=0xfffffe00083f82c0-0xfffffe00083f82e0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000020 off=0x013f42e0-0x013f4300 addr=0xfffffe00083f82e0-0xfffffe00083f8300         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000016d8 off=0x013f4300-0x013f59d8 addr=0xfffffe00083f8300-0xfffffe00083f99d8         __DATA_CONST.__const            
	sz=0x00000100 off=0x013f59d8-0x013f5ad8 addr=0xfffffe00083f99d8-0xfffffe00083f9ad8         __DATA_CONST.__kalloc_type      
	sz=0x000000b0 off=0x013f5ad8-0x013f5b88 addr=0xfffffe00083f9ad8-0xfffffe00083f9b88         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000058 off=0x013f5b88-0x013f5be0 addr=0xfffffe00083f9b88-0xfffffe00083f9be0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 55 at 0x04af831c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     E18D7509-A7F0-36A0-AE1C-1F0746A95644
008: LC_SOURCE_VERSION           120.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac59a0 size=0xc8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOStreamFamily`
- `CFBundleIdentifier`: `com.apple.iokit.IOStreamFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOStreamFamily`
- `CFBundleNumericVersion`: `17858560`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.1.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOStreamFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198894921760`
- `_PrelinkExecutableRelativePath`: `IOStreamFamily`
- `_PrelinkExecutableSize`: `22952`
- `_PrelinkExecutableSourceAddr`: `-2198894921760`
- `_PrelinkKmodInfo`: `-2198828110256`

## Strings (15) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `IOStream`
- `IOStreamUserClient`
- `site.IOStreamBuffer`
- `1211212`
- `IOStreamUserClientInit`
- `IOStreamUserClientClass`
- `12111112122212121121111111112`
- `IOProviderMergeProperties`
- `IOUserClientClass`
- `site.IOStream`
- `IOStreamBuffer`
- `site.IOStreamUserClient`
- `1211111212221212111111111111111`
- `site.IOStreamUserClientInit`
- `12111112122212121`
