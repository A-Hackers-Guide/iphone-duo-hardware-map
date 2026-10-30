# `com.apple.driver.AppleUSBTopCaseDriver`

- Name: AppleUSBTopCaseDriver
- Version: `1000.22`
- UUID: `DAB1FAFC-38A5-3454-B036-E98D2F1C6701`
- Source version: `10100.22.0.0.0`
- Depends on: [`com.apple.driver.AppleUSBHostMergeProperties`](com.apple.driver.AppleUSBHostMergeProperties.md) 1.0, [`com.apple.driver.usb.IOUSBHostHIDDevice`](com.apple.driver.usb.IOUSBHostHIDDevice.md) 1.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.5, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.0.1, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### Magic Devices - AppleUSBTopCaseHIDDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBTopCaseDriver`
- `IOClass`: `AppleUSBTopCaseHIDDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBTopCaseDriver`
- `IOProviderClass`: `IOUSBHostInterface`
- `bConfigurationValue`: `1`
- `bInterfaceNumber`: `*`
- `idProductArray`:
  - `615`
  - `620`
- `idVendor`: `1452`

### Magic Keyboards - AppleUSBTopCaseHIDDriver, Device Management
- `Accessory Category`: `Keyboard`
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBTopCaseDriver`
- `ExtendedData`:
  - `50399649`
  - `50465185`
  - `50530721`
  - `50596257`
  - `53741985`
  - `61868449`
  - `61933985`
  - `61999521`
  - `62065057`
  - `62261665`
- `IOClass`: `AppleUSBTopCaseHIDDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBTopCaseDriver`
- `IOProviderClass`: `IOUSBHostInterface`
- `bConfigurationValue`: `1`
- `bInterfaceNumber`: `0`
- `idProductArray`:
  - `615`
  - `620`
- `idVendor`: `1452`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBTopCaseHIDDriver` | 0x168 | IOUSBHostHIDDevice → IOHIDDevice → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000007d2 off=0x00898a70-0x00899242 addr=0xfffffe000789ca70-0xfffffe000789d242 r--/r--   __TEXT            
	sz=0x00000075 off=0x00899098-0x0089910d addr=0xfffffe000789d098-0xfffffe000789d10d               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000135 off=0x0089910d-0x00899242 addr=0xfffffe000789d10d-0xfffffe000789d242               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x000006a4 off=0x02a10f50-0x02a115f4 addr=0xfffffe0009a14f50-0xfffffe0009a155f4 r-x/r-x   __TEXT_EXEC       
	sz=0x00000614 off=0x02a10f50-0x02a11564 addr=0xfffffe0009a14f50-0xfffffe0009a15564          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000090 off=0x02a11564-0x02a115f4 addr=0xfffffe0009a15564-0xfffffe0009a155f4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x049cf5b0-0x049cf6b0 addr=0xfffffe000b9d35b0-0xfffffe000b9d36b0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049cf5b0-0x049cf678 addr=0xfffffe000b9d35b0-0xfffffe000b9d3678               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9d3678-0xfffffe000b9d36b0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000848 off=0x01291730-0x01291f78 addr=0xfffffe0008295730-0xfffffe0008295f78 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01291730-0x01291738 addr=0xfffffe0008295730-0xfffffe0008295738         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01291738-0x01291740 addr=0xfffffe0008295738-0xfffffe0008295740         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000790 off=0x01291740-0x01291ed0 addr=0xfffffe0008295740-0xfffffe0008295ed0         __DATA_CONST.__const            
	sz=0x00000040 off=0x01291ed0-0x01291f10 addr=0xfffffe0008295ed0-0xfffffe0008295f10         __DATA_CONST.__kalloc_type      
	sz=0x00000048 off=0x01291f10-0x01291f58 addr=0xfffffe0008295f10-0xfffffe0008295f58         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000020 off=0x01291f58-0x01291f78 addr=0xfffffe0008295f58-0xfffffe0008295f78         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 22 at 0x04aeab80
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     DAB1FAFC-38A5-3454-B036-E98D2F1C6701
008: LC_SOURCE_VERSION           10100.22.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab6648 size=0x20
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleUSBTopCaseDriver`
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBTopCaseDriver`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUSBTopCaseDriver`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1000.22`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1000.22`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2012 Apple Inc. All rights reserved.`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleTopCase.kext/PlugIns/AppleUSBTopCaseDriver.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896784784`
- `_PrelinkExecutableRelativePath`: `AppleUSBTopCaseDriver`
- `_PrelinkExecutableSize`: `6078`
- `_PrelinkExecutableSourceAddr`: `-2198896784784`
- `_PrelinkKmodInfo`: `-2198828403280`

## Strings (9) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AppleUSBTopCaseHIDDriver`
- `site.AppleUSBTopCaseHIDDriver`
- `121111121222121211211122211111111111111112221`
- `ATC`
- `handleStart`

**[__TEXT.__os_log]**

- `[HID] [%s] [Error] %s::%s Failed to cast provider to IOUSBHostInterface!\n`
- `[HID] [%s] [Error] %s::%s hostInterfaceProvider->setIdlePolicy() returned 0x%08X\n`
- `[HID] [%s] [Error] %s::%s _interruptPipe->setIdlePolicy() returned 0x%08X\n`
- `[HID] [%s] [Error] %s::%s _interruptOutPipe->setIdlePolicy() returned 0x%08X\n`
