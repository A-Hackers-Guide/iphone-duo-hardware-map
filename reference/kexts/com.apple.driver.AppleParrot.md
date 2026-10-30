# `com.apple.driver.AppleParrot`

- Name: AppleParrot
- Version: `1`
- UUID: `A33B3A2B-F310-31CD-992F-9231FAFD7CD8`
- Source version: `4.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 16.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 16.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 16.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleParrot
- `CFBundleIdentifier`: `com.apple.driver.AppleParrot`
- `IOClass`: `AppleParrot`
- `IONameMatch`: `parrot-i2c,a0`
- `IOPersonalityPublisher`: `com.apple.driver.AppleParrot`
- `IOProviderClass`: `AppleARMIICDevice`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleParrot` | 0x98 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000078b off=0x006a0200-0x006a098b addr=0xfffffe00076a4200-0xfffffe00076a498b r--/r--   __TEXT            
	sz=0x000001b3 off=0x006a07d8-0x006a098b addr=0xfffffe00076a47d8-0xfffffe00076a498b               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00001044 off=0x023768c0-0x02377904 addr=0xfffffe000937a8c0-0xfffffe000937b904 r-x/r-x   __TEXT_EXEC       
	sz=0x00000f94 off=0x023768c0-0x02377854 addr=0xfffffe000937a8c0-0xfffffe000937b854          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000000b0 off=0x02377854-0x02377904 addr=0xfffffe000937b854-0xfffffe000937b904          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x049843d8-0x049844d8 addr=0xfffffe000b9883d8-0xfffffe000b9884d8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049843d8-0x049844a0 addr=0xfffffe000b9883d8-0xfffffe000b9884a0               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9884a0-0xfffffe000b9884d8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000006f8 off=0x011995f0-0x01199ce8 addr=0xfffffe000819d5f0-0xfffffe000819dce8 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x011995f0-0x011995f8 addr=0xfffffe000819d5f0-0xfffffe000819d5f8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x011995f8-0x01199600 addr=0xfffffe000819d5f8-0xfffffe000819d600         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000628 off=0x01199600-0x01199c28 addr=0xfffffe000819d600-0xfffffe000819dc28         __DATA_CONST.__const            
	sz=0x00000040 off=0x01199c28-0x01199c68 addr=0xfffffe000819dc28-0xfffffe000819dc68         __DATA_CONST.__kalloc_type      
	sz=0x00000058 off=0x01199c68-0x01199cc0 addr=0xfffffe000819dc68-0xfffffe000819dcc0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000028 off=0x01199cc0-0x01199ce8 addr=0xfffffe000819dcc0-0xfffffe000819dce8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 27 at 0x04ae1d1c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     A33B3A2B-F310-31CD-992F-9231FAFD7CD8
008: LC_SOURCE_VERSION           4.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aacb28 size=0x30
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleParrot`
- `CFBundleIdentifier`: `com.apple.driver.AppleParrot`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleParrot`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
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
- `NSHumanReadableCopyright`: `Copyright © 2017 Apple. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleParrot.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898851328`
- `_PrelinkExecutableRelativePath`: `AppleParrot`
- `_PrelinkExecutableSize`: `8135`
- `_PrelinkExecutableSourceAddr`: `-2198898851328`
- `_PrelinkKmodInfo`: `-2198828710952`

## Strings (21) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `1211111212221212112`
- `writeRegister`
- `softReset`
- `dump`
- `site.AppleParrot`
- `readRegister`
- `%s::%s: portNum = %d\n`
- `callPlatformFunction`
- `AppleParrot`
- `%s::%s: \n`
- `free`
- `%s::%s: address 0x%02x, value 0x%02x returned %s\n`
- `tunable_setting`
- `%s::%s: Failed to read/write tunable - Offset 0x%08x Value 0x%08x\n`
- `trigger`
- `AppleParrot-debug`
- `start`
- `%s::%s: Applying EDT tunable settings\n`
- `applyTunables`
- `%s::%s: Applying EDT tunable: Offset 0x%08x Value 0x%08x\n`
- `portReset`
