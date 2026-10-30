# `com.apple.driver.AppleUSBDeviceAudioController`

- Name: AppleUSBDeviceAudioController
- Version: `910.2`
- UUID: `B8074DF4-F1DA-3736-B2BF-4EBEDA071EDB`
- Source version: `910.2.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleUSBAudio`](com.apple.driver.AppleUSBAudio.md) 410.11, [`com.apple.iokit.IOAudio2Family`](com.apple.iokit.IOAudio2Family.md) 1.0, [`com.apple.iokit.IOUSBDeviceFamily`](com.apple.iokit.IOUSBDeviceFamily.md) 2.0.0, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.0.1, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 14.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 14.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 20.4.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (3) [KC]

### AppleUSBDeviceAudioControl
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBDeviceAudioController`
- `IOClass`: `AppleUSBDeviceAudioController`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBDeviceAudioController`
- `IOPropertyMatch`:
  - `USBDeviceFunction`: `USBAudio2Control`
- `IOProviderClass`: `IOUSBDeviceInterface`

### AppleUSBDeviceAudioStreamIN
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBDeviceAudioController`
- `IOClass`: `AppleUSBDeviceAudioController`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBDeviceAudioController`
- `IOPropertyMatch`:
  - `USBDeviceFunction`: `USBAudio2StreamIN`
- `IOProviderClass`: `IOUSBDeviceInterface`

### AppleUSBDeviceAudioStreamOUT
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBDeviceAudioController`
- `IOClass`: `AppleUSBDeviceAudioController`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBDeviceAudioController`
- `IOPropertyMatch`:
  - `USBDeviceFunction`: `USBAudio2StreamOUT`
- `IOProviderClass`: `IOUSBDeviceInterface`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBDeviceAudioController` | 0xf0 | IOService → IORegistryEntry |
| `AppleUSBDeviceAudioNub` | 0x90 | AppleUSBDeviceAudioNubBase → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000a42 off=0x008d0970-0x008d13b2 addr=0xfffffe00078d4970-0xfffffe00078d53b2 r--/r--   __TEXT            
	sz=0x000000b0 off=0x008d0f98-0x008d1048 addr=0xfffffe00078d4f98-0xfffffe00078d5048               __TEXT.__const            
	sz=0x0000036a off=0x008d1048-0x008d13b2 addr=0xfffffe00078d5048-0xfffffe00078d53b2               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x0000342c off=0x02b19120-0x02b1c54c addr=0xfffffe0009b1d120-0xfffffe0009b2054c r-x/r-x   __TEXT_EXEC       
	sz=0x0000328c off=0x02b19120-0x02b1c3ac addr=0xfffffe0009b1d120-0xfffffe0009b203ac          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001a0 off=0x02b1c3ac-0x02b1c54c addr=0xfffffe0009b203ac-0xfffffe0009b2054c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x049d0b08-0x049d0c30 addr=0xfffffe000b9d4b08-0xfffffe000b9d4c30 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x049d0b08-0x049d0bcc addr=0xfffffe000b9d4b08-0xfffffe000b9d4bcc               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b9d4bd0-0xfffffe000b9d4c30               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000df8 off=0x012a3050-0x012a3e48 addr=0xfffffe00082a7050-0xfffffe00082a7e48 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x012a3050-0x012a3060 addr=0xfffffe00082a7050-0xfffffe00082a7060         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x012a3060-0x012a3070 addr=0xfffffe00082a7060-0xfffffe00082a7070         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000c28 off=0x012a3070-0x012a3c98 addr=0xfffffe00082a7070-0xfffffe00082a7c98         __DATA_CONST.__const            
	sz=0x00000080 off=0x012a3c98-0x012a3d18 addr=0xfffffe00082a7c98-0xfffffe00082a7d18         __DATA_CONST.__kalloc_type      
	sz=0x000000d0 off=0x012a3d18-0x012a3de8 addr=0xfffffe00082a7d18-0xfffffe00082a7de8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000060 off=0x012a3de8-0x012a3e48 addr=0xfffffe00082a7de8-0xfffffe00082a7e48         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 64 at 0x04aeb7ac
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     B8074DF4-F1DA-3736-B2BF-4EBEDA071EDB
008: LC_SOURCE_VERSION           910.2.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab7418 size=0x70
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleUSBDeviceAudioController`
- `CFBundleGetInfoString`: `AppleUSBDeviceAudioController 910.2, Copyright © 2000-2024 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBDeviceAudioController`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUSBDeviceAudioController`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `910.2`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `910.2`
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
  - `2`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleUSBDeviceAudioController.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896555664`
- `_PrelinkExecutableRelativePath`: `AppleUSBDeviceAudioController`
- `_PrelinkExecutableSize`: `19854`
- `_PrelinkExecutableSourceAddr`: `-2198896555664`
- `_PrelinkKmodInfo`: `-2198828397816`

## Strings (26) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `USB Vendor Name`
- `IDAM Audio`
- `kUSBSerialNumberString`
- `USBAudio2StreamOUT`
- `Yes`
- `USB Sound assertion (%s) in %s at line %d\n`
- `Apple Inc.`
- `IOPlatformSerialNumber`
- `/Library/Caches/com.apple.xbs/B5FDCB36-D853-46D3-9503-186FD0AD7D5C/TemporaryDirectory.BTvKfA/Sources/AppleUSBAudio/IDAM/AppleUSBDeviceAudioNub.cpp`
- `121111121222121211111112111111`
- `AppleUSBDeviceAudioGroup`
- `USB Sound assertion in %s at line %d\n`
- `/Library/Caches/com.apple.xbs/B5FDCB36-D853-46D3-9503-186FD0AD7D5C/TemporaryDirectory.BTvKfA/Sources/AppleUSBAudio/IDAM/AppleUSBDeviceAudioController.cpp`
- `USB Sound assertion return 0x%X in %s at line %d\n`
- `USBDeviceFunction`
- `USBAudio2StreamIN`
- `AppleUSBAudioStreamPropertiesReady`
- `Unknown provider type`
- `AppleUSBDeviceAudioNub`
- `site.AppleUSBDeviceAudioNub`
- `USB Product Name`
- `AppleUSBDeviceAudioController`
- `site.AppleUSBDeviceAudioController`
- `USBAudio2Control`
- `enable-full-idam`
- `121111121222121211`
