# `com.apple.driver.usb.AppleUSBHostBillboardDevice`

- Name: AppleUSBHostBillboardDevice
- Version: `1.0`
- UUID: `2C1197FC-0E8C-3046-9626-36C80BB10BB4`
- Source version: `1617.40.10.0.0`
- Depends on: [`com.apple.driver.usb.AppleUSBCommon`](com.apple.driver.usb.AppleUSBCommon.md) 1.0, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.2, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 23.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 23.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 23.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 23.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (4) [KC]

### Billboard Device
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHostCompositeDevice`
- `IOClass`: `AppleUSBHostCompositeDevice`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHostBillboardDevice`
- `IOProviderClass`: `IOUSBHostDevice`
- `bDeviceClass`: `17`
- `bDeviceSubClass`: `0`

### Billboard Device Properties
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHostBillboardDevice`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `UsbIdlePolicy`: `1000`
  - `UsbUserClientEntitlementRequired`:
    - `UsbUserClientEntitlement`: `com.apple.developer.usb.billboard`
    - `UsbUserClientEntitlementExceptionAllowUnlocked`: `True`
- `bDeviceClass`: `17`
- `bDeviceSubClass`: `0`

### Billboard Interface
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHostBillboardDevice`
- `IOClass`: `AppleUSBHostBillboardDevice`
- `IOMatchCategory`: `AppleUSBHostBillboardDevice`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHostBillboardDevice`
- `IOProviderClass`: `IOUSBHostInterface`
- `bInterfaceClass`: `17`
- `bInterfaceSubClass`: `0`

### Billboard Interface Properties
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHostBillboardDevice`
- `IOProviderClass`: `IOUSBHostInterface`
- `IOProviderMergeProperties`:
  - `UsbUserClientEntitlementRequired`:
    - `UsbUserClientEntitlement`: `com.apple.developer.usb.billboard`
    - `UsbUserClientEntitlementExceptionAllowUnlocked`: `True`
- `bInterfaceClass`: `17`
- `bInterfaceSubClass`: `0`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBHostBillboardDevice` | 0xb0 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000b1d off=0x00b4eb20-0x00b4f63d addr=0xfffffe0007b52b20-0xfffffe0007b5363d r--/r--   __TEXT            
	sz=0x00000008 off=0x00b4f198-0x00b4f1a0 addr=0xfffffe0007b53198-0xfffffe0007b531a0               __TEXT.__const            
	sz=0x00000314 off=0x00b4f1a0-0x00b4f4b4 addr=0xfffffe0007b531a0-0xfffffe0007b534b4               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000189 off=0x00b4f4b4-0x00b4f63d addr=0xfffffe0007b534b4-0xfffffe0007b5363d               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0000169c off=0x037e99c0-0x037eb05c addr=0xfffffe000a7ed9c0-0xfffffe000a7ef05c r-x/r-x   __TEXT_EXEC       
	sz=0x0000151c off=0x037e99c0-0x037eaedc addr=0xfffffe000a7ed9c0-0xfffffe000a7eeedc          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000180 off=0x037eaedc-0x037eb05c addr=0xfffffe000a7eeedc-0xfffffe000a7ef05c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x04a1bbc8-0x04a1bcc8 addr=0xfffffe000ba1fbc8-0xfffffe000ba1fcc8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a1bbc8-0x04a1bc90 addr=0xfffffe000ba1fbc8-0xfffffe000ba1fc90               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000ba1fc90-0xfffffe000ba1fcc8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000788 off=0x01461d38-0x014624c0 addr=0xfffffe0008465d38-0xfffffe00084664c0 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01461d38-0x01461d40 addr=0xfffffe0008465d38-0xfffffe0008465d40         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01461d40-0x01461d48 addr=0xfffffe0008465d40-0xfffffe0008465d48         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000630 off=0x01461d48-0x01462378 addr=0xfffffe0008465d48-0xfffffe0008466378         __DATA_CONST.__const            
	sz=0x00000040 off=0x01462378-0x014623b8 addr=0xfffffe0008466378-0xfffffe00084663b8         __DATA_CONST.__kalloc_type      
	sz=0x000000c0 off=0x014623b8-0x01462478 addr=0xfffffe00084663b8-0xfffffe0008466478         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000048 off=0x01462478-0x014624c0 addr=0xfffffe0008466478-0xfffffe00084664c0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 57 at 0x04afab8c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     2C1197FC-0E8C-3046-9626-36C80BB10BB4
008: LC_SOURCE_VERSION           1617.40.10.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac9f78 size=0x30
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleUSBHostBillboardDevice`
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHostBillboardDevice`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUSBHostBillboardDevice`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.2`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0`
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
- `OSBundleRequired`: `Console`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/AppleUSBHostBillboardDevice.kext`
- `_PrelinkExecutableLoadAddr`: `-2198893941984`
- `_PrelinkExecutableRelativePath`: `AppleUSBHostBillboardDevice`
- `_PrelinkExecutableSize`: `10817`
- `_PrelinkExecutableSourceAddr`: `-2198893941984`
- `_PrelinkKmodInfo`: `-2198828090424`

## Strings (37) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%s: %s::%s: Billboard version 0x%04x is not supported\n`
- `UsbBillboardVersion`
- `UsbBillboardAltModeFailed`
- `%s: %s::%s: failed to allocate _commandGate\n`
- `%s: %s::%s: super::start failed\n`
- `start`
- `%s: %s::%s: unable to obtain IOUSBHostInterface provider\n`
- `%s: %s::%s: unable to obtain Billboard descriptor\n`
- `UsbBillboardPreferredMode`
- `%s: %s::%s: disabling idle policy\n`
- `i8@?0`
- `%s: %s::%s: enabling idle policy\n`
- `AppleUSBHostBillboardDevice`
- `%x.%02x`
- `UsbBillboardAltModePowerFailed`
- `UsbBillboardCurrentMode`
- `powerStateWillChangeTo_block_invoke`
- `USB4`
- `DisplayPort`
- `SVID 0x%04x VDO 0x%08x`
- `UsbBillboardSupportedModes`
- `UsbIdlePolicy`
- `powerStateDidChangeTo_block_invoke`
- `Thunderbolt`
- `site.AppleUSBHostBillboardDevice`
- `1211111212221212121122`
- `%s: %s::%s: unable to obtain device\n`
- `%s: %s::%s: unable to obtain BOS descriptor\n`

**[__TEXT.__os_log]**

- `%s: %s::%s: super::start failed\n`
- `%s: %s::%s: unable to obtain device\n`
- `%s: %s::%s: unable to obtain BOS descriptor\n`
- `%s: %s::%s: Billboard version 0x%04x is not supported\n`
- `%s: %s::%s: failed to allocate _commandGate\n`
- `%s: %s::%s: disabling idle policy\n`
- `%s: %s::%s: unable to obtain IOUSBHostInterface provider\n`
- `%s: %s::%s: unable to obtain Billboard descriptor\n`
- `%s: %s::%s: enabling idle policy\n`
