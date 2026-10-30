# `com.apple.driver.IOPAudioAssetManagerDevice`

- Name: IOPAudioAssetManagerDevice
- Version: `400.36`
- UUID: `77E9BE58-B6C0-308B-B03A-20AADBDBF473`
- Source version: `400.36.0.0.0`
- Depends on: [`com.apple.iokit.IOPAudioDriverFamily`](com.apple.iokit.IOPAudioDriverFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AssetManagerDevice
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioAssetManagerDevice`
- `IOClass`: `IOPAudioAssetManagerDevice`
- `IOPersonalityPublisher`: `com.apple.driver.IOPAudioAssetManagerDevice`
- `IOProviderClass`: `IOPAudioNode`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOPAudioAssetManagerDevice` | 0xb8 | IOPAudioDevice → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000bd1 off=0x00a29b90-0x00a2a761 addr=0xfffffe0007a2db90-0xfffffe0007a2e761 r--/r--   __TEXT            
	sz=0x00000473 off=0x00a2a1b8-0x00a2a62b addr=0xfffffe0007a2e1b8-0xfffffe0007a2e62b               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000136 off=0x00a2a62b-0x00a2a761 addr=0xfffffe0007a2e62b-0xfffffe0007a2e761               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00000d38 off=0x032df260-0x032dff98 addr=0xfffffe000a2e3260-0xfffffe000a2e3f98 r-x/r-x   __TEXT_EXEC       
	sz=0x00000c78 off=0x032df260-0x032dfed8 addr=0xfffffe000a2e3260-0xfffffe000a2e3ed8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000000c0 off=0x032dfed8-0x032dff98 addr=0xfffffe000a2e3ed8-0xfffffe000a2e3f98          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x04a13b58-0x04a13c58 addr=0xfffffe000ba17b58-0xfffffe000ba17c58 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a13b58-0x04a13c20 addr=0xfffffe000ba17b58-0xfffffe000ba17c20               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000ba17c20-0xfffffe000ba17c58               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000718 off=0x013c5cc8-0x013c63e0 addr=0xfffffe00083c9cc8-0xfffffe00083ca3e0 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x013c5cc8-0x013c5cd0 addr=0xfffffe00083c9cc8-0xfffffe00083c9cd0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x013c5cd0-0x013c5cd8 addr=0xfffffe00083c9cd0-0xfffffe00083c9cd8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000648 off=0x013c5cd8-0x013c6320 addr=0xfffffe00083c9cd8-0xfffffe00083ca320         __DATA_CONST.__const            
	sz=0x00000040 off=0x013c6320-0x013c6360 addr=0xfffffe00083ca320-0xfffffe00083ca360         __DATA_CONST.__kalloc_type      
	sz=0x00000060 off=0x013c6360-0x013c63c0 addr=0xfffffe00083ca360-0xfffffe00083ca3c0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000020 off=0x013c63c0-0x013c63e0 addr=0xfffffe00083ca3c0-0xfffffe00083ca3e0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 28 at 0x04af55b8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     77E9BE58-B6C0-308B-B03A-20AADBDBF473
008: LC_SOURCE_VERSION           400.36.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac3788 size=0x38
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleExecutable`: `IOPAudioAssetManagerDevice`
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioAssetManagerDevice`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOPAudioAssetManagerDevice`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOPAudioAssetManagerDevice.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895142000`
- `_PrelinkExecutableRelativePath`: `IOPAudioAssetManagerDevice`
- `_PrelinkExecutableSize`: `8481`
- `_PrelinkExecutableSourceAddr`: `-2198895142000`
- `_PrelinkKmodInfo`: `-2198828123304`

## Strings (22) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `IOPAudioAssetManagerDevice`
- `ret = super::_handleStart(inProvider) == 0 `
- `/Library/Caches/com.apple.xbs/20732553-D3E1-4B38-B5F5-87A23D935C9E/TemporaryDirectory.oCjbCa/Sources/IOPAudioDrivers/src/kext/AssetManagerDevice/AssetManagerDevice.cpp`
- `!((interfaceName) == nullptr)`
- `!((data) == nullptr)`
- `12111112122212121111212`
- `ret = PrivateAPI::registerUserClientIfPublished(inProvider, this) == 0 `
- `/Library/Caches/com.apple.xbs/20732553-D3E1-4B38-B5F5-87A23D935C9E/TemporaryDirectory.oCjbCa/Sources/IOPAudioDrivers/src/kext/AssetManagerDevice/AssetManagerDeviceHelper.cpp`
- `!((supportedUserClientVersion) == nullptr)`
- `thisService->setProperty(\"Button Haptics Asset Interface\", *supportedUserClientVersion, sizeof(uint32_t) * 8)`
- `kci-name`
- `ret = _configure(inProvider) == 0 `
- `ret = _processResourceUpdateRequest(inRequest) == 0 `
- `ret = (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2c7) == 0 `
- `IOPAudioPCMAssetManagerDeviceUserClient`
- `site.IOPAudioAssetManagerDevice`
- `Button Haptics Asset Interface`
- `IOUserClientClass`
- `thisService->setProperty(\"IOUserClientClass\", kIOUserClientClassName)`
- `IOPAudio::AssetManagerDevice::Helper`
- `publish-user-client`

**[__TEXT.__os_log]**

- `%s: %s, %s file: %s, line: %d\n`
