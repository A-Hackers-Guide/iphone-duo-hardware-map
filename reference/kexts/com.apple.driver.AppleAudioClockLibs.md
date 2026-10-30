# `com.apple.driver.AppleAudioClockLibs`

- Name: AppleAudioClockLibs
- Version: `600.6`
- UUID: `23F4AD15-258C-3D8A-8E42-38BF9C143F43`
- Source version: `600.6.0.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (0) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1240)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000083b off=0x003902d0-0x00390b0b addr=0xfffffe00073942d0-0xfffffe0007394b0b r--/r--   __TEXT            
	sz=0x00000103 off=0x00390808-0x0039090b addr=0xfffffe0007394808-0xfffffe000739490b               __TEXT.__os_log           
	sz=0x00000200 off=0x0039090b-0x00390b0b addr=0xfffffe000739490b-0xfffffe0007394b0b               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00000820 off=0x0198b6f0-0x0198bf10 addr=0xfffffe000898f6f0-0xfffffe000898ff10 r-x/r-x   __TEXT_EXEC       
	sz=0x000007d0 off=0x0198b6f0-0x0198bec0 addr=0xfffffe000898f6f0-0xfffffe000898fec0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000050 off=0x0198bec0-0x0198bf10 addr=0xfffffe000898fec0-0xfffffe000898ff10          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000000f0 off=0x04932fd0-0x049330c0 addr=0xfffffe000b936fd0-0xfffffe000b9370c0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04932fd0-0x04933098 addr=0xfffffe000b936fd0-0xfffffe000b937098               __DATA.__data             
	sz=0x00000010 off=0x00000000-0x00000010 addr=0xfffffe000b937098-0xfffffe000b9370a8               __DATA.__common           (Zerofill)
	sz=0x00000018 off=0x00000000-0x00000018 addr=0xfffffe000b9370a8-0xfffffe000b9370c0               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00000038 off=0x00fe8838-0x00fe8870 addr=0xfffffe0007fec838-0xfffffe0007fec870 rw-/rw-   __DATA_CONST      
	sz=0x00000028 off=0x00fe8838-0x00fe8860 addr=0xfffffe0007fec838-0xfffffe0007fec860         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000010 off=0x00fe8860-0x00fe8870 addr=0xfffffe0007fec860-0xfffffe0007fec870         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 12 at 0x04ad37cc
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     23F4AD15-258C-3D8A-8E42-38BF9C143F43
008: LC_SOURCE_VERSION           600.6.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9a288 size=0x18
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleAudioClockLibs`
- `CFBundleIdentifier`: `com.apple.driver.AppleAudioClockLibs`
- `CFBundleInfoDictionaryVersion`: `1.0`
- `CFBundleName`: `AppleAudioClockLibs`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `600.6`
- `CFBundleSignature`: `aapl`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `600.6`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleAudioClockLibs.kext`
- `_PrelinkExecutableLoadAddr`: `-2198902062384`
- `_PrelinkExecutableRelativePath`: `AppleAudioClockLibs`
- `_PrelinkExecutableSize`: `4483`
- `_PrelinkExecutableSourceAddr`: `-2198902062384`
- `_PrelinkKmodInfo`: `-2198829043760`

## Strings (22) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `%s: Invalid key(%p) or devPath(%p).`
- `%s: Could not find registry entry for \"%s\"`
- `%s: Invalid value output argument.`
- `%s: \"%s/%s\" property data incompatible.`
- `%s: nullptr for inController`
- `%s: %s type expect OSData got %s`
- `%s: %s property malformed, expected uint32`

**[__TEXT.__cstring]**

- `%s: %s type expect OSData got %s\n`
- `%s: Invalid key(%p) or devPath(%p).\n`
- `getPropertyUint32t`
- `IODeviceTree:/product/audio`
- `mach-time-audio-max-drift`
- `static Domain AppleAudioClock::Utility::getClockDomainOverride(const IOService *, const char *const)`
- `%s: nullptr for inController\n`
- `mach-time-audio-alignment`
- `%s: %s property malformed, expected uint32\n`
- `clock-domain`
- `getProperty`
- `%s: Could not find registry entry for \"%s\"\n`
- `%s: Invalid value output argument.\n`
- `%s: \"%s/%s\" property data incompatible.\n`
- `usb-uses-audio-clock`
