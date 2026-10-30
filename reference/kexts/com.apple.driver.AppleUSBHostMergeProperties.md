# `com.apple.driver.AppleUSBHostMergeProperties`

- Name: Properties Applier for USB Services
- Version: `1.2`
- UUID: `0A19D85B-8096-3FA7-803E-618802E3BB41`
- Source version: `1617.40.10.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 23.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 23.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 23.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 23.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (29) [KC]

### AnkerUsbPowerSinkCapability-3000
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `UsbPowerSinkCapability`: `3000`
- `idProductArray`:
  - `405`
- `idVendor`: `10522`

### Apple 0x9226-7 Device
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBDevice`
- `IOProviderMergeProperties`:
  - `ExtendedData`:
    - `66980129`
- `idProductArray`:
  - `37414`
  - `37415`
  - `37430`
- `idVendor`: `1452`

### Apple 0x9226-7 Interface
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBInterface`
- `IOProviderMergeProperties`:
  - `ExtendedData`:
    - `66980129`
- `bConfigurationValue`: `*`
- `bInterfaceNumber`: `*`
- `idProductArray`:
  - `37414`
  - `37415`
  - `37430`
- `idVendor`: `1452`

### Apple Acrylic Keyboard
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBInterface`
- `IOProviderMergeProperties`:
  - `kUSBResumeRecoveryTime`: `250`
- `idProductArray`:
  - `523`
  - `524`
  - `525`
- `idVendor`: `1452`

### Apple LED Display Audio Device
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBDevice`
- `IOProviderMergeProperties`:
  - `DisplayRouting`: `0`
  - `kUSBDescriptorOverride`:
    - `descriptor`: `<data 64 chars>`
    - `index`: `UsbDescriptorOverrideProductStringIndex`
    - `languageID`: `1033`
- `idProductArray`:
  - `10514`
  - `4357`
  - `4359`
- `idVendor`: `1452`

### Apple Studio Display
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBPreferredConfiguration`: `3`
- `idProductArray`:
  - `4372`
  - `4374`
  - `4376`
- `idVendor`: `1452`

### Apple WS Device
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBDevice`
- `IOProviderMergeProperties`:
  - `ExtendedData`:
    - `50399521`
    - `50465057`
- `idProductArray`:
  - `547`
  - `548`
  - `549`
  - `560`
  - `561`
  - `562`
  - `566`
  - `567`
  - `568`
  - `575`
  - `576`
  - `577`
  - `578`
  - `579`
  - `580`
  - `581`
  - `582`
  - `583`
  - `594`
  - `595`
  - `596`
  - `585`
  - `586`
  - `587`
  - `588`
  - `589`
  - `590`
  - `601`
  - `602`
  - `603`
  - `610`
  - `611`
  - `612`
- `idVendor`: `1452`

### Apple WS Interface
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBInterface`
- `IOProviderMergeProperties`:
  - `ExtendedData`:
    - `50399521`
    - `50465057`
- `bConfigurationValue`: `*`
- `bInterfaceNumber`: `0`
- `idProductArray`:
  - `547`
  - `548`
  - `549`
  - `560`
  - `561`
  - `562`
  - `566`
  - `567`
  - `568`
  - `575`
  - `576`
  - `577`
  - `578`
  - `579`
  - `580`
  - `581`
  - `582`
  - `583`
  - `594`
  - `595`
  - `596`
  - `585`
  - `586`
  - `587`
  - `588`
  - `589`
  - `590`
  - `601`
  - `602`
  - `603`
  - `610`
  - `611`
  - `612`
- `idVendor`: `1452`

### AppleUsbPowerSinkCapability-1000
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `UsbPowerSinkCapability`: `1000`
- `idProductArray`:
  - `4615`
  - `4616`
  - `4617`
  - `4705`
  - `4752`
  - `4753`
  - `4754`
  - `4755`
  - `4756`
  - `4759`
  - `4761`
  - `4764`
  - `4766`
  - `4768`
  - `4778`
  - `5010`
  - `5018`
  - `5019`
  - `5020`
  - `5021`
  - `5022`
  - `5023`
  - `5024`
- `idVendor`: `1452`

### AppleUsbPowerSinkCapability-1300
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `UsbPowerSinkCapability`: `1300`
- `idProductArray`:
  - `613`
  - `617`
  - `803`
  - `804`
- `idVendor`: `1452`

### AppleUsbPowerSinkCapability-1500
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `UsbPowerSinkCapability`: `1500`
- `idProductArray`:
  - `4751`
  - `4781`
  - `4782`
- `idVendor`: `1452`

### AppleUsbPowerSinkCapability-2100
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `UsbPowerSinkCapability`: `2100`
- `idProductArray`:
  - `4361`
- `idVendor`: `1452`

### AppleUsbPowerSinkCapability-2400
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `UsbPowerSinkCapability`: `2400`
- `idProductArray`:
  - `4762`
  - `4767`
  - `4770`
  - `4771`
  - `4772`
  - `4773`
  - `4774`
  - `4777`
  - `4779`
  - `5013`
  - `5008`
  - `4116`
  - `4117`
  - `5014`
  - `5124`
  - `5016`
  - `5017`
  - `666`
  - `667`
  - `668`
  - `671`
- `idVendor`: `1452`

### AppleUsbPowerSinkCapability-3000
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `UsbPowerSinkCapability`: `3000`
- `idProductArray`:
  - `5015`
  - `622`
  - `623`
  - `1280`
  - `1281`
  - `1282`
  - `1105`
  - `1108`
  - `1109`
- `idVendor`: `1452`

### AppleUsbPowerSinkCapability-500
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `UsbPowerSinkCapability`: `500`
- `idProductArray`:
  - `615`
  - `620`
  - `800`
  - `801`
  - `802`
  - `4377`
  - `4610`
  - `4613`
  - `4618`
  - `4704`
  - `4706`
  - `4707`
  - `4709`
  - `4710`
  - `4711`
  - `4866`
  - `4867`
  - `5011`
  - `5028`
  - `5029`
- `idVendor`: `1452`

### AppleUsbPowerSinkCapability-700
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `UsbPowerSinkCapability`: `700`
- `idProductArray`:
  - `5025`
  - `5027`
  - `5031`
- `idVendor`: `1452`

### AppleUsbPowerSinkCapability-800
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `UsbPowerSinkCapability`: `800`
- `idProductArray`:
  - `4364`
  - `4375`
- `idVendor`: `1452`

### BelkinUsbPowerSinkCapability-1500
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `UsbPowerSinkCapability`: `1500`
- `idProductArray`:
  - `408`
- `idVendor`: `1293`

### DisplayiSight - 0x219
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBDevice`
- `IOProviderMergeProperties`:
  - `kUSBDescriptorOverride`:
    - `descriptor`: `<data 2624 chars>`
    - `index`: `0`
    - `languageID`: `0`
- `bcdDevice`: `537`
- `idProduct`: `34056`
- `idVendor`: `1452`

### Lightning Digital AV Adapter
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBDevice`
- `IOProviderMergeProperties`:
  - `kUSBDescriptorOverride`:
    - `descriptor`: `<data 120 chars>`
    - `index`: `UsbDescriptorOverrideProductStringIndex`
    - `languageID`: `1033`
- `idProduct`: `4781`
- `idVendor`: `1452`

### Lightning VGA Adapter
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBDevice`
- `IOProviderMergeProperties`:
  - `kUSBDescriptorOverride`:
    - `descriptor`: `<data 92 chars>`
    - `index`: `UsbDescriptorOverrideProductStringIndex`
    - `languageID`: `1033`
- `idProduct`: `4782`
- `idVendor`: `1452`

### Linksys USB3GIGV1
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHostDeviceEnableLPM`: `False`
- `idProductArray`:
  - `65`
- `idVendor`: `5041`

### LogitechUsbPowerSinkCapability-2400
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `UsbPowerSinkCapability`: `2400`
- `idProductArray`:
  - `53505`
- `idVendor`: `1133`

### Moshi USB 10/100/1000 LAN
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHostDeviceEnableLPM`: `False`
- `idProductArray`:
  - `33107`
- `idVendor`: `3034`

### SIXAXIS controller
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBInterface`
- `IOProviderMergeProperties`:
  - `SIXAXIS compatibility`: `True`
- `bConfigurationValue`: `1`
- `bInterfaceNumber`: `0`
- `idProduct`: `616`
- `idVendor`: `1356`

### eLicenser Enable Data Toggle Reset
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBHostInterface`
- `IOProviderMergeProperties`:
  - `UsbUserClientEnableDataToggleReset`: `True`
- `bConfigurationValue`: `*`
- `bInterfaceNumber`: `*`
- `idProduct`: `257`
- `idVendor`: `2073`

### iPhoneUsbPowerSinkCapability-1000
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `UsbPowerSinkCapability`: `1000`
- `bcdDeviceRange`:
  - `0`
  - `1791`
- `idProduct`: `4776`
- `idVendor`: `1452`

### iPhoneUsbPowerSinkCapability-2400
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `UsbPowerSinkCapability`: `2400`
- `bcdDeviceRange`:
  - `1792`
  - `65535`
- `idProduct`: `4776`
- `idVendor`: `1452`

### iPod
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBResumeRecoveryTime`: `400`
- `idProductArray`:
  - `4608`
  - `4864`
- `idProductMask`: `65408`
- `idVendor`: `1452`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBHostMergeProperties` | 0x88 | IOProviderPropertyMerger → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000006b1 off=0x00b50a10-0x00b510c1 addr=0xfffffe0007b54a10-0xfffffe0007b550c1 r--/r--   __TEXT            
	sz=0x00000089 off=0x00b51038-0x00b510c1 addr=0xfffffe0007b55038-0xfffffe0007b550c1               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00000acc off=0x037eea10-0x037ef4dc addr=0xfffffe000a7f2a10-0xfffffe000a7f34dc r-x/r-x   __TEXT_EXEC       
	sz=0x00000a2c off=0x037eea10-0x037ef43c addr=0xfffffe000a7f2a10-0xfffffe000a7f343c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000000a0 off=0x037ef43c-0x037ef4dc addr=0xfffffe000a7f343c-0xfffffe000a7f34dc          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000101 off=0x04a1bf18-0x04a1c019 addr=0xfffffe000ba1ff18-0xfffffe000ba20019 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a1bf18-0x04a1bfe0 addr=0xfffffe000ba1ff18-0xfffffe000ba1ffe0               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000ba1ffe0-0xfffffe000ba20018               __DATA.__common           (Zerofill)
	sz=0x00000001 off=0x00000000-0x00000001 addr=0xfffffe000ba20018-0xfffffe000ba20019               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000006c8 off=0x014636c8-0x01463d90 addr=0xfffffe00084676c8-0xfffffe0008467d90 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x014636c8-0x014636d0 addr=0xfffffe00084676c8-0xfffffe00084676d0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x014636d0-0x014636d8 addr=0xfffffe00084676d0-0xfffffe00084676d8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000600 off=0x014636d8-0x01463cd8 addr=0xfffffe00084676d8-0xfffffe0008467cd8         __DATA_CONST.__const            
	sz=0x00000040 off=0x01463cd8-0x01463d18 addr=0xfffffe0008467cd8-0xfffffe0008467d18         __DATA_CONST.__kalloc_type      
	sz=0x00000050 off=0x01463d18-0x01463d68 addr=0xfffffe0008467d18-0xfffffe0008467d68         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000028 off=0x01463d68-0x01463d90 addr=0xfffffe0008467d68-0xfffffe0008467d90         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 25 at 0x04afadf4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     0A19D85B-8096-3FA7-803E-618802E3BB41
008: LC_SOURCE_VERSION           1617.40.10.0.0
009: LC_FUNCTION_STARTS          offset=0x004aca020 size=0x20
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleUSBHostMergeProperties`
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `Properties Applier for USB Services`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/AppleUSBHostMergeProperties.kext`
- `_PrelinkExecutableLoadAddr`: `-2198893934064`
- `_PrelinkExecutableRelativePath`: `AppleUSBHostMergeProperties`
- `_PrelinkExecutableSize`: `6470`
- `_PrelinkExecutableSourceAddr`: `-2198893934064`
- `_PrelinkKmodInfo`: `-2198828089576`

## Strings (5) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AppleUSBHostMergeProperties`
- `site.AppleUSBHostMergeProperties`
- `12111112122212121`
- `IOProviderParentMergeProperties`
- `IOProviderMergeProperties`
