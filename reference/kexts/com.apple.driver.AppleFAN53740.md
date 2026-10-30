# `com.apple.driver.AppleFAN53740`

- Name: AppleFAN53740
- Version: `1`
- UUID: `93A22CA9-75B8-3A0F-B78D-19CBE0B1A7A8`
- Source version: `12.40.3.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 16.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 16.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 16.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleFAN53740
- `CFBundleIdentifier`: `com.apple.driver.AppleFAN53740`
- `IOClass`: `AppleFAN53740`
- `IONameMatch`: `accbuck,fan53740`
- `IOPersonalityPublisher`: `com.apple.driver.AppleFAN53740`
- `IOProviderClass`: `AppleARMIICDevice`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleFAN53740` | 0xb0 | IOService → IORegistryEntry |
| `AppleFAN53740VoltageFunction` | 0x38 | AppleARMFunction |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000007ae off=0x004659e0-0x0046618e addr=0xfffffe00074699e0-0xfffffe000746a18e r--/r--   __TEXT            
	sz=0x00000186 off=0x00466008-0x0046618e addr=0xfffffe000746a008-0xfffffe000746a18e               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x000015e8 off=0x01ca39c0-0x01ca4fa8 addr=0xfffffe0008ca79c0-0xfffffe0008ca8fa8 r-x/r-x   __TEXT_EXEC       
	sz=0x000014e8 off=0x01ca39c0-0x01ca4ea8 addr=0xfffffe0008ca79c0-0xfffffe0008ca8ea8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000100 off=0x01ca4ea8-0x01ca4fa8 addr=0xfffffe0008ca8ea8-0xfffffe0008ca8fa8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000134 off=0x04940fa8-0x049410dc addr=0xfffffe000b944fa8-0xfffffe000b9450dc rw-/rw-   __DATA            
	sz=0x000000d0 off=0x04940fa8-0x04941078 addr=0xfffffe000b944fa8-0xfffffe000b945078               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b945078-0xfffffe000b9450d8               __DATA.__common           (Zerofill)
	sz=0x00000004 off=0x00000000-0x00000004 addr=0xfffffe000b9450d8-0xfffffe000b9450dc               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00000888 off=0x010983d8-0x01098c60 addr=0xfffffe000809c3d8-0xfffffe000809cc60 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x010983d8-0x010983e0 addr=0xfffffe000809c3d8-0xfffffe000809c3e0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x010983e0-0x010983e8 addr=0xfffffe000809c3e0-0xfffffe000809c3e8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000740 off=0x010983e8-0x01098b28 addr=0xfffffe000809c3e8-0xfffffe000809cb28         __DATA_CONST.__const            
	sz=0x00000080 off=0x01098b28-0x01098ba8 addr=0xfffffe000809cb28-0xfffffe000809cba8         __DATA_CONST.__kalloc_type      
	sz=0x00000080 off=0x01098ba8-0x01098c28 addr=0xfffffe000809cba8-0xfffffe000809cc28         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000038 off=0x01098c28-0x01098c60 addr=0xfffffe000809cc28-0xfffffe000809cc60         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 39 at 0x04ad9930
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     93A22CA9-75B8-3A0F-B78D-19CBE0B1A7A8
008: LC_SOURCE_VERSION           12.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9f9e8 size=0x48
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleFAN53740`
- `CFBundleIdentifier`: `com.apple.driver.AppleFAN53740`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleFAN53740`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleFAN53740.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901188128`
- `_PrelinkExecutableRelativePath`: `AppleFAN53740`
- `_PrelinkExecutableSize`: `10066`
- `_PrelinkExecutableSourceAddr`: `-2198901188128`
- `_PrelinkKmodInfo`: `-2198828986456`

## Strings (14) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AppleFAN53740VoltageFunction`
- `site.AppleFAN53740VoltageFunction`
- `1211121`
- `AppleFAN53740`
- `site.AppleFAN53740`
- `1211111212221212111112`
- `function-accbuck_en`
- `(no provider)`
- `%s::%s: %s: desiredVoltageMv %u, desiredCurrentMa %u returning %#x\n`
- `%s::%s: %s: desiredVoltageMv %u returning %#x\n`
- `selectOutputLdoGated`
- `selectOutputBuckGated`
- `%s::%s: %s: desiredCurrentMa %u returning %#x\n`
- `selectOutputBypassGated`
