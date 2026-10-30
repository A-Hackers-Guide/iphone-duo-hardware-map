# `com.apple.driver.usb.AppleUSBHostCompositeDevice`

- Name: I/O Kit Driver for USB Composite Devices
- Version: `1.2`
- UUID: `C814A627-DED9-3435-B450-1A31411CED4F`
- Source version: `1617.40.10.0.0`
- Depends on: [`com.apple.driver.usb.AppleUSBCommon`](com.apple.driver.usb.AppleUSBCommon.md) 1.0, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.2, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 23.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 23.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 23.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 23.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 23.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (4) [KC]

### AppleUSBHostCompositeDevice
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHostCompositeDevice`
- `IOClass`: `AppleUSBHostCompositeDevice`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHostCompositeDevice`
- `IOProviderClass`: `IOUSBHostDevice`
- `bDeviceClass`: `0`
- `bDeviceSubClass`: `0`

### AppleUSBPrinterDevice0
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHostCompositeDevice`
- `IOClass`: `AppleUSBHostCompositeDevice`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHostCompositeDevice`
- `IOProviderClass`: `IOUSBHostDevice`
- `bDeviceClass`: `7`
- `bDeviceSubClass`: `0`

### AppleUSBPrinterDevice1
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHostCompositeDevice`
- `IOClass`: `AppleUSBHostCompositeDevice`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHostCompositeDevice`
- `IOProviderClass`: `IOUSBHostDevice`
- `bDeviceClass`: `7`
- `bDeviceSubClass`: `1`

### InterfaceAssociationClass
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHostCompositeDevice`
- `IOClass`: `AppleUSBHostCompositeDevice`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHostCompositeDevice`
- `IOProviderClass`: `IOUSBHostDevice`
- `bDeviceClass`: `239`
- `bDeviceProtocol`: `1`
- `bDeviceSubClass`: `2`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBConfigurationDescriptorOrderedSet` | 0x48 | OSOrderedSet → OSCollection |
| `AppleUSBHostCompositeDevice` | 0xc0 | IOService → IORegistryEntry |
| `AppleUSBSortableConfigurationDescriptor` | 0x20 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000c67 off=0x00b4f640-0x00b502a7 addr=0xfffffe0007b53640-0xfffffe0007b542a7 r--/r--   __TEXT            
	sz=0x00000439 off=0x00b4fc68-0x00b500a1 addr=0xfffffe0007b53c68-0xfffffe0007b540a1               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000206 off=0x00b500a1-0x00b502a7 addr=0xfffffe0007b540a1-0xfffffe0007b542a7               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x000030b4 off=0x037eb060-0x037ee114 addr=0xfffffe000a7ef060-0xfffffe000a7f2114 r-x/r-x   __TEXT_EXEC       
	sz=0x00002f14 off=0x037eb060-0x037edf74 addr=0xfffffe000a7ef060-0xfffffe000a7f1f74          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001a0 off=0x037edf74-0x037ee114 addr=0xfffffe000a7f1f74-0xfffffe000a7f2114          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000150 off=0x04a1bcc8-0x04a1be18 addr=0xfffffe000ba1fcc8-0xfffffe000ba1fe18 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a1bcc8-0x04a1bd90 addr=0xfffffe000ba1fcc8-0xfffffe000ba1fd90               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000ba1fd90-0xfffffe000ba1fe18               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000b30 off=0x014624c0-0x01462ff0 addr=0xfffffe00084664c0-0xfffffe0008466ff0 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x014624c0-0x014624d0 addr=0xfffffe00084664c0-0xfffffe00084664d0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x014624d0-0x014624e0 addr=0xfffffe00084664d0-0xfffffe00084664e0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000918 off=0x014624e0-0x01462df8 addr=0xfffffe00084664e0-0xfffffe0008466df8         __DATA_CONST.__const            
	sz=0x000000c0 off=0x01462df8-0x01462eb8 addr=0xfffffe0008466df8-0xfffffe0008466eb8         __DATA_CONST.__kalloc_type      
	sz=0x000000d0 off=0x01462eb8-0x01462f88 addr=0xfffffe0008466eb8-0xfffffe0008466f88         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000068 off=0x01462f88-0x01462ff0 addr=0xfffffe0008466f88-0xfffffe0008466ff0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 65 at 0x04afac70
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     C814A627-DED9-3435-B450-1A31411CED4F
008: LC_SOURCE_VERSION           1617.40.10.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac9fa8 size=0x58
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleUSBHostCompositeDevice`
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHostCompositeDevice`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `I/O Kit Driver for USB Composite Devices`
- `CFBundleNumericVersion`: `18907136`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.2`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.2`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2000-2025 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/AppleUSBHostCompositeDevice.kext`
- `_PrelinkExecutableLoadAddr`: `-2198893939136`
- `_PrelinkExecutableRelativePath`: `AppleUSBHostCompositeDevice`
- `_PrelinkExecutableSize`: `18843`
- `_PrelinkExecutableSourceAddr`: `-2198893939136`
- `_PrelinkKmodInfo`: `-2198828090168`

## Strings (39) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `kUSBDesiredChargingCurrent`
- `AppleUSBConfigurationDescriptorOrderedSet`
- `122111221`
- `%s: %s::%s: %s@%s: getConfigurationDescriptor(%u) failed\n`
- `%s: %s::%s: %s@%s: power sink capability %dmA\n`
- `%s: %s::%s: %s@%s: wake %dmA sleep %dmA\n`
- `%s: %s::%s: %s@%s: insufficient power for current configuration %d\n`
- `1211`
- `%s: %s::%s: %s@%s: failed current limit vendor request with 0x%08x\n`
- `kUSBBusCurrentSleepAllocation`
- `site.AppleUSBConfigurationDescriptorOrderedSet`
- `negotiatePower`
- `%s: %s::%s: %s@%s: preferred configuration %d\n`
- `%s: %s::%s: %s@%s: limiting power sink capability to %dmA\n`
- `kUSBBusCurrentAllocation`
- `getPreferredConfiguration`
- `%s: %s::%s: %s@%s: no descriptor for preferred configuration property %d\n`
- `AppleUSBSortableConfigurationDescriptor`
- `AppleUSBHostCompositeDevice`
- `IOPrimaryDriverTerminateOptions`
- `iAP Interface`
- `site.AppleUSBHostCompositeDevice`
- `121111121222121211211211`
- `UsbPowerSinkCapability`
- `locationID`
- `kUSBConfigurationCurrentOverride`
- `site.AppleUSBSortableConfigurationDescriptor`
- `kUSBPreferredConfiguration`
- `%s: %s::%s: %s@%s: preferred configuration property %d\n`
- `kUSBWakePortCurrentLimit`

**[__TEXT.__os_log]**

- `%s: %s::%s: %s@%s: getConfigurationDescriptor(%u) failed\n`
- `%s: %s::%s: %s@%s: preferred configuration %d\n`
- `%s: %s::%s: %s@%s: power sink capability %dmA\n`
- `%s: %s::%s: %s@%s: limiting power sink capability to %dmA\n`
- `%s: %s::%s: %s@%s: failed current limit vendor request with 0x%08x\n`
- `%s: %s::%s: %s@%s: preferred configuration property %d\n`
- `%s: %s::%s: %s@%s: no descriptor for preferred configuration property %d\n`
- `%s: %s::%s: %s@%s: wake %dmA sleep %dmA\n`
- `%s: %s::%s: %s@%s: insufficient power for current configuration %d\n`
