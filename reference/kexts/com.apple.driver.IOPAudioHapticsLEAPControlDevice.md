# `com.apple.driver.IOPAudioHapticsLEAPControlDevice`

- Name: IOPAudioHapticsLEAPControlDevice
- Version: `400.36`
- UUID: `1FE97B8D-61F4-33C9-AC60-32165C901FAC`
- Source version: `400.36.0.0.0`
- Depends on: [`com.apple.driver.IOPAudioLEAPControlDevice`](com.apple.driver.IOPAudioLEAPControlDevice.md) 1.0, [`com.apple.iokit.IOPAudioDriverFamily`](com.apple.iokit.IOPAudioDriverFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/iop-audio-controller/audio-haptic-leap`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic-leap.md) | `IOPAudioHapticsLEAPControlDevice` | `iop-audio,haptics-leap-control-device` |

## IOKit personalities (1) [KC]

### IOPAudioHapticsLEAPControlDevice
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioHapticsLEAPControlDevice`
- `IOClass`: `IOPAudioHapticsLEAPControlDevice`
- `IONameMatch`:
  - `iop-audio,haptics-leap-control-device`
- `IOPersonalityPublisher`: `com.apple.driver.IOPAudioHapticsLEAPControlDevice`
- `IOProviderClass`: `IOPAudioNode`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOPAudioHapticsLEAPControlDevice` | 0xb8 | IOPAudioLEAPControlDevice → IOPAudioDevice → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000a07 off=0x00a32ed0-0x00a338d7 addr=0xfffffe0007a36ed0-0xfffffe0007a378d7 r--/r--   __TEXT            
	sz=0x000002e7 off=0x00a334f8-0x00a337df addr=0xfffffe0007a374f8-0xfffffe0007a377df               __TEXT.__cstring          (CstringLiterals)
	sz=0x000000f8 off=0x00a337df-0x00a338d7 addr=0xfffffe0007a377df-0xfffffe0007a378d7               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00000af4 off=0x032f8850-0x032f9344 addr=0xfffffe000a2fc850-0xfffffe000a2fd344 r-x/r-x   __TEXT_EXEC       
	sz=0x00000a24 off=0x032f8850-0x032f9274 addr=0xfffffe000a2fc850-0xfffffe000a2fd274          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000000d0 off=0x032f9274-0x032f9344 addr=0xfffffe000a2fd274-0xfffffe000a2fd344          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x04a141e0-0x04a142e0 addr=0xfffffe000ba181e0-0xfffffe000ba182e0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a141e0-0x04a142a8 addr=0xfffffe000ba181e0-0xfffffe000ba182a8               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000ba182a8-0xfffffe000ba182e0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000720 off=0x013ca148-0x013ca868 addr=0xfffffe00083ce148-0xfffffe00083ce868 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x013ca148-0x013ca150 addr=0xfffffe00083ce148-0xfffffe00083ce150         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x013ca150-0x013ca158 addr=0xfffffe00083ce150-0xfffffe00083ce158         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000648 off=0x013ca158-0x013ca7a0 addr=0xfffffe00083ce158-0xfffffe00083ce7a0         __DATA_CONST.__const            
	sz=0x00000040 off=0x013ca7a0-0x013ca7e0 addr=0xfffffe00083ce7a0-0xfffffe00083ce7e0         __DATA_CONST.__kalloc_type      
	sz=0x00000068 off=0x013ca7e0-0x013ca848 addr=0xfffffe00083ce7e0-0xfffffe00083ce848         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000020 off=0x013ca848-0x013ca868 addr=0xfffffe00083ce848-0xfffffe00083ce868         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 30 at 0x04af59bc
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     1FE97B8D-61F4-33C9-AC60-32165C901FAC
008: LC_SOURCE_VERSION           400.36.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac3b90 size=0x28
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleExecutable`: `IOPAudioHapticsLEAPControlDevice`
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioHapticsLEAPControlDevice`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOPAudioHapticsLEAPControlDevice`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `400.36`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `400.36`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2023 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOPAudioHapticsLEAPControlDevice.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895104304`
- `_PrelinkExecutableRelativePath`: `IOPAudioHapticsLEAPControlDevice`
- `_PrelinkExecutableSize`: `7451`
- `_PrelinkExecutableSourceAddr`: `-2198895104304`
- `_PrelinkKmodInfo`: `-2198828121632`

## Strings (15) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `ret = inParkingNodeInterface->getNodeProperty(propertyDescriptor) == 0 `
- `IOPAudio::HapticsLEAPControlDevice`
- `data != nullptr`
- `IOPAudioHapticsLEAPControlDevice`
- `12111112122212121111212`
- `ret = super::_handleStart(inProvider) == 0 `
- `/Library/Caches/com.apple.xbs/20732553-D3E1-4B38-B5F5-87A23D935C9E/TemporaryDirectory.oCjbCa/Sources/IOPAudioDrivers/src/kext/HapticsLEAPControlDevice/HapticsLEAPControlDevice.cpp`
- `!((parkingInfoData) == nullptr)`
- `InterfaceUtil::SetData(inRequest, parkingInfoData.get())`
- `ret = (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2c7) == 0 `
- `parking-node-id`
- `site.IOPAudioHapticsLEAPControlDevice`
- `!((parkingNodeInterface) == nullptr)`
- `ret = retrieveParkingInfoFromIOP(parkingNodeInterface, parkingInfoData) == 0 `

**[__TEXT.__os_log]**

- `%s: %s, %s file: %s, line: %d\n`
