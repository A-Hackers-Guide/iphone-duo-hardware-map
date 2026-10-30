# `com.apple.driver.AppleHapticsSupportNVM`

- Name: AppleHapticsSupportNVM
- Version: `11.6`
- UUID: `2A063DB1-42A0-3E46-B938-9BFC98E504DA`
- Source version: `11.6.0.0.0`
- Depends on: [`com.apple.driver.AppleSPU`](com.apple.driver.AppleSPU.md) 1.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 11.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 11.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleHapticsSupportArcEEPROM
- `CFBundleIdentifier`: `com.apple.driver.AppleHapticsSupportNVM`
- `IOClass`: `AppleHapticsSupportArcEEPROM`
- `IONameMatch`:
  - `arc-eeprom-i2c`
- `IOPersonalityPublisher`: `com.apple.driver.AppleHapticsSupportNVM`
- `IOProviderClass`: `AppleSPUAppInterface`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleHapticsSupportArcEEPROM` | 0x88 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000009d0 off=0x00518930-0x00519300 addr=0xfffffe000751c930-0xfffffe000751d300 r--/r--   __TEXT            
	sz=0x00000059 off=0x00518f58-0x00518fb1 addr=0xfffffe000751cf58-0xfffffe000751cfb1               __TEXT.__const            
	sz=0x0000034f off=0x00518fb1-0x00519300 addr=0xfffffe000751cfb1-0xfffffe000751d300               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00000b34 off=0x01ff9510-0x01ffa044 addr=0xfffffe0008ffd510-0xfffffe0008ffe044 r-x/r-x   __TEXT_EXEC       
	sz=0x00000a64 off=0x01ff9510-0x01ff9f74 addr=0xfffffe0008ffd510-0xfffffe0008ffdf74          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000000d0 off=0x01ff9f74-0x01ffa044 addr=0xfffffe0008ffdf74-0xfffffe0008ffe044          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x0494cdd0-0x0494ced0 addr=0xfffffe000b950dd0-0xfffffe000b950ed0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0494cdd0-0x0494ce98 addr=0xfffffe000b950dd0-0xfffffe000b950e98               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b950e98-0xfffffe000b950ed0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000006c8 off=0x0110dd18-0x0110e3e0 addr=0xfffffe0008111d18-0xfffffe00081123e0 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x0110dd18-0x0110dd20 addr=0xfffffe0008111d18-0xfffffe0008111d20         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x0110dd20-0x0110dd28 addr=0xfffffe0008111d20-0xfffffe0008111d28         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000005f0 off=0x0110dd28-0x0110e318 addr=0xfffffe0008111d28-0xfffffe0008112318         __DATA_CONST.__const            
	sz=0x00000040 off=0x0110e318-0x0110e358 addr=0xfffffe0008112318-0xfffffe0008112358         __DATA_CONST.__kalloc_type      
	sz=0x00000068 off=0x0110e358-0x0110e3c0 addr=0xfffffe0008112358-0xfffffe00081123c0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000020 off=0x0110e3c0-0x0110e3e0 addr=0xfffffe00081123c0-0xfffffe00081123e0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 30 at 0x04adcd48
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     2A063DB1-42A0-3E46-B938-9BFC98E504DA
008: LC_SOURCE_VERSION           11.6.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa5110 size=0x30
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleHapticsSupportNVM`
- `CFBundleIdentifier`: `com.apple.driver.AppleHapticsSupportNVM`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleHapticsSupportNVM`
- `CFBundleNumericVersion`: `291536896`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `11.6`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `11.6`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2018 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleHapticsSupportNVM.kext`
- `_PrelinkExecutableLoadAddr`: `-2198900455120`
- `_PrelinkExecutableRelativePath`: `AppleHapticsSupportNVM`
- `_PrelinkExecutableSize`: `7372`
- `_PrelinkExecutableSourceAddr`: `-2198900455120`
- `_PrelinkKmodInfo`: `-2198828937776`

## Strings (15) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.AppleHapticsSupportArcEEPROM`
- `ArcSerialNumber`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `AppleHapticsSupportArcEEPROM`
- `12111112122212121`
- `IsArcSerialNumberValid`
- `The offset of the pointer inside its valid memory range can't be represented using int32_t`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `Calibration`
- `\"%s\" @%s:%d`
- `OSBoundedPtr.h`
- `bounded_array_ref: Can't construct from a size greater than UINT32_MAX`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `bounded_array_ref: n + m is larger than the size of any bounded_array_ref`
