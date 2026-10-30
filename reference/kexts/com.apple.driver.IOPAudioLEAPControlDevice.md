# `com.apple.driver.IOPAudioLEAPControlDevice`

- Name: IOPAudioLEAPControlDevice
- Version: `400.36`
- UUID: `B32D7AEA-B01E-3515-AA3B-F0C30F2B5702`
- Source version: `400.36.0.0.0`
- Depends on: [`com.apple.iokit.IOPAudioDriverFamily`](com.apple.iokit.IOPAudioDriverFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### IOPAudioLEAPControlDevice
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioLEAPControlDevice`
- `IOClass`: `IOPAudioLEAPControlDevice`
- `IONameMatch`:
  - `iop-audio,leap-control-device`
- `IOPersonalityPublisher`: `com.apple.driver.IOPAudioLEAPControlDevice`
- `IOProviderClass`: `IOPAudioNode`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOPAudioLEAPControlDevice` | 0xb0 | IOPAudioDevice → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000cf4 off=0x00a35ca0-0x00a36994 addr=0xfffffe0007a39ca0-0xfffffe0007a3a994 r--/r--   __TEXT            
	sz=0x0000049e off=0x00a362c8-0x00a36766 addr=0xfffffe0007a3a2c8-0xfffffe0007a3a766               __TEXT.__cstring          (CstringLiterals)
	sz=0x0000022e off=0x00a36766-0x00a36994 addr=0xfffffe0007a3a766-0xfffffe0007a3a994               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00001604 off=0x032fded0-0x032ff4d4 addr=0xfffffe000a301ed0-0xfffffe000a3034d4 r-x/r-x   __TEXT_EXEC       
	sz=0x00001484 off=0x032fded0-0x032ff354 addr=0xfffffe000a301ed0-0xfffffe000a303354          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000180 off=0x032ff354-0x032ff4d4 addr=0xfffffe000a303354-0xfffffe000a3034d4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x04a14540-0x04a14640 addr=0xfffffe000ba18540-0xfffffe000ba18640 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a14540-0x04a14608 addr=0xfffffe000ba18540-0xfffffe000ba18608               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000ba18608-0xfffffe000ba18640               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000788 off=0x013cc6a8-0x013cce30 addr=0xfffffe00083d06a8-0xfffffe00083d0e30 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x013cc6a8-0x013cc6b0 addr=0xfffffe00083d06a8-0xfffffe00083d06b0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x013cc6b0-0x013cc6b8 addr=0xfffffe00083d06b0-0xfffffe00083d06b8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000648 off=0x013cc6b8-0x013ccd00 addr=0xfffffe00083d06b8-0xfffffe00083d0d00         __DATA_CONST.__const            
	sz=0x00000040 off=0x013ccd00-0x013ccd40 addr=0xfffffe00083d0d00-0xfffffe00083d0d40         __DATA_CONST.__kalloc_type      
	sz=0x000000c0 off=0x013ccd40-0x013cce00 addr=0xfffffe00083d0d40-0xfffffe00083d0e00         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000030 off=0x013cce00-0x013cce30 addr=0xfffffe00083d0e00-0xfffffe00083d0e30         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 54 at 0x04af5b80
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     B32D7AEA-B01E-3515-AA3B-F0C30F2B5702
008: LC_SOURCE_VERSION           400.36.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac3cb8 size=0x40
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleExecutable`: `IOPAudioLEAPControlDevice`
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioLEAPControlDevice`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOPAudioLEAPControlDevice`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOPAudioLEAPControlDevice.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895092576`
- `_PrelinkExecutableRelativePath`: `IOPAudioLEAPControlDevice`
- `_PrelinkExecutableSize`: `11136`
- `_PrelinkExecutableSourceAddr`: `-2198895092576`
- `_PrelinkKmodInfo`: `-2198828120768`

## Strings (23) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `ret = super::_handleStart(inProvider) == 0 `
- `!((interfaceName) == nullptr)`
- `ret = PrivateAPI::handleMemoryAccessRequest( getNodeInterface(), inRequest, inParentRequestType) == 0 `
- `/Library/Caches/com.apple.xbs/20732553-D3E1-4B38-B5F5-87A23D935C9E/TemporaryDirectory.oCjbCa/Sources/IOPAudioDrivers/src/kext/LEAPControlDevice/LEAPControlDeviceHelpers.cpp`
- `site.IOPAudioLEAPControlDevice`
- `/Library/Caches/com.apple.xbs/20732553-D3E1-4B38-B5F5-87A23D935C9E/TemporaryDirectory.oCjbCa/Sources/IOPAudioDrivers/src/kext/LEAPControlDevice/LEAPControlDevice.cpp`
- `ret = _configure(inProvider) == 0 `
- `!((subRequestList) == nullptr)`
- `ret = _handleDeviceSpecificClientRequest(inRequest) == 0 `
- `IOPAudio::LEAPControlDevice::Helper`
- `!((startAddressPtr) == nullptr)`
- `1211111212221212111121`
- `!((data) == nullptr)`
- `!((registerData) == nullptr)`
- `ret = (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2c7) == 0 `
- `KernelInterfaceUtil::SetData(inRequest, returnMemoryData.get())`
- `kci-name`
- `IOPAudioLEAPControlDevice`
- `!((requestIterator) == nullptr)`
- `ret = inNode->memoryAccess(descriptor) == 0 `
- `ret = (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2c2) == 0 `
- `!((returnMemoryData) == nullptr)`

**[__TEXT.__os_log]**

- `%s: %s, %s file: %s, line: %d\n`
