# `com.apple.driver.AppleEmbeddedUSBHost`

- Name: AppleEmbeddedUSBHost
- Version: `1`
- UUID: `9CF7986D-1BE6-362A-A52A-2514AFFAD322`
- Source version: `717.40.5.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleMobileFileIntegrity`](com.apple.driver.AppleMobileFileIntegrity.md) 1.0.2, [`com.apple.driver.AppleUSBHostMergeProperties`](com.apple.driver.AppleUSBHostMergeProperties.md) 1.2, [`com.apple.driver.usb.AppleUSBCommon`](com.apple.driver.usb.AppleUSBCommon.md) 1.0, [`com.apple.driver.usb.AppleUSBHostCompositeDevice`](com.apple.driver.usb.AppleUSBHostCompositeDevice.md) 1.2, [`com.apple.driver.usb.AppleUSBHub`](com.apple.driver.usb.AppleUSBHub.md) 1.2, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.2, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0b1, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0b2, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0b2, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0b2, [`com.apple.kpi.private`](com.apple.kpi.private.md) 16.5.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (16) [KC]

### AppleEmbeddedUSBCardReader
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBConfigurationCurrentOverride`: `0`
- `idProduct`: `1826`
- `idVendor`: `1507`

### AppleEmbeddedUSBCardReaderPrototype
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBConfigurationCurrentOverride`: `0`
- `idProduct`: `33795`
- `idVendor`: `1452`

### AppleEmbeddedUSBDeviceSupport
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOClass`: `AppleEmbeddedUSBDeviceSupport`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOProviderClass`: `AppleEmbeddedUSBDevice`
- `USBSpeed`: `1`
- `idProduct`: `*`
- `idVendor`: `*`

### AppleTICD2E22
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOClass`: `AppleTICD2E22`
- `IONameMatch`: `usb-repeater-i2c,ticd2e22`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOProviderClass`: `AppleARMIICDevice`

### AppleUSB20AccessoryHub0
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOClass`: `AppleUSB20AccessoryHub`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOProviderClass`: `AppleEmbeddedUSBDevice`
- `bDeviceClass`: `9`
- `bDeviceSubClass`: `0`

### AppleUSB20AccessoryHub1
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOClass`: `AppleUSB20AccessoryHub`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOProviderClass`: `AppleEmbeddedUSBDevice`
- `bDeviceClass`: `9`
- `bDeviceSubClass`: `1`

### AppleUSB20Hub_32789
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOClass`: `AppleUSB20Hub_32789`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOProviderClass`: `IOUSBHostDevice`
- `bcdDevice`: `1061`
- `idProduct`: `32789`
- `idVendor`: `1452`

### AppleUSB20Hub_32789_merge
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBDescriptorOverride`:
    - `descriptor`: `<data 32 chars>`
    - `index`: `UsbDescriptorOverrideVendorStringIndex`
    - `languageID`: `1033`
- `bcdDevice`: `1061`
- `idProduct`: `32789`
- `idVendor`: `1452`

### AppleUSB30AccessoryHub0
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOClass`: `AppleUSB30AccessoryHub`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOProviderClass`: `AppleEmbeddedUSBDevice`
- `bDeviceClass`: `9`
- `bDeviceSubClass`: `0`

### AppleUSB30AccessoryHub1
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOClass`: `AppleUSB30AccessoryHub`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOProviderClass`: `AppleEmbeddedUSBDevice`
- `bDeviceClass`: `9`
- `bDeviceSubClass`: `1`

### AppleUSBHubIICDevice
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOClass`: `AppleUSBHubIICDevice`
- `IONameMatch`: `usb-hub-i2c`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOProviderClass`: `AppleARMIICDevice`

### ParrotUSBResetLockup
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOProviderClass`: `AppleT8101USB20XHCILightningPort`
- `IOProviderMergeProperties`:
  - `ParrotSoftResetDigitalIDArray`:
    - `<data 24 chars>`

### iOSDFU-AppleEmbeddedUSBDevice
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOClass`: `IOService`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOProviderClass`: `AppleEmbeddedUSBDevice`
- `idProductArray`:
  - `4646`
  - `4647`
  - `4648`
  - `4649`
- `idVendor`: `1452`

### iOSDFU-Merge
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOProviderClass`: `AppleEmbeddedUSBDevice`
- `IOProviderMergeProperties`:
  - `Authenticated`: `True`
  - `kUSBConfigurationCurrentOverride`: `0`
  - `kUSBResetDurationOverride`: `75`
- `idProductArray`:
  - `4646`
  - `4647`
  - `4648`
  - `4649`
- `idVendor`: `1452`

### iOSRecovery-AppleEmbeddedUSBDevice
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOClass`: `IOService`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOProviderClass`: `AppleEmbeddedUSBDevice`
- `idProduct`: `4737`
- `idVendor`: `1452`

### iOSRecovery-Merge
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedUSBHost`
- `IOProviderClass`: `AppleEmbeddedUSBDevice`
- `IOProviderMergeProperties`:
  - `Authenticated`: `True`
  - `kUSBConfigurationCurrentOverride`: `0`
- `idProduct`: `4737`
- `idVendor`: `1452`


## C++ classes (10) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleEmbeddedUSBDevice` | 0x158 | IOUSBHostDevice → IOUSBDevice → IODMACommand → IOCommand |
| `AppleEmbeddedUSBDeviceSupport` | 0x88 | IOService → IORegistryEntry |
| `AppleTICD2E22` | 0xb0 | AppleUSB2RepeaterIICDevice → IOService → IORegistryEntry |
| `AppleUSB20AccessoryHub` | 0x258 | AppleUSB20Hub → AppleUSBHub → IOService → IORegistryEntry |
| `AppleUSB20AccessoryHubPort` | 0x410 | AppleUSB20HubPort → AppleUSBHubPort → AppleUSBHostPort → IOService → IORegistryEntry |
| `AppleUSB20Hub_32789` | 0x258 | AppleUSB20Hub → AppleUSBHub → IOService → IORegistryEntry |
| `AppleUSB2RepeaterIICDevice` | 0xb0 | IOService → IORegistryEntry |
| `AppleUSB30AccessoryHub` | 0x258 | AppleUSB30Hub → AppleUSBHub → IOService → IORegistryEntry |
| `AppleUSB30AccessoryHubPort` | 0x420 | AppleUSB30HubPort → AppleUSBHubPort → AppleUSBHostPort → IOService → IORegistryEntry |
| `AppleUSBHubIICDevice` | 0xb8 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000017d0 off=0x004610f0-0x004628c0 addr=0xfffffe00074650f0-0xfffffe00074668c0 r--/r--   __TEXT            
	sz=0x00000cec off=0x00461768-0x00462454 addr=0xfffffe0007465768-0xfffffe0007466454               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000421 off=0x00462454-0x00462875 addr=0xfffffe0007466454-0xfffffe0007466875               __TEXT.__os_log           
	sz=0x00000048 off=0x00462878-0x004628c0 addr=0xfffffe0007466878-0xfffffe00074668c0               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00006a98 off=0x01c98c30-0x01c9f6c8 addr=0xfffffe0008c9cc30-0xfffffe0008ca36c8 r-x/r-x   __TEXT_EXEC       
	sz=0x000067b8 off=0x01c98c30-0x01c9f3e8 addr=0xfffffe0008c9cc30-0xfffffe0008ca33e8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000002e0 off=0x01c9f3e8-0x01c9f6c8 addr=0xfffffe0008ca33e8-0xfffffe0008ca36c8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000002a0 off=0x049409d0-0x04940c70 addr=0xfffffe000b9449d0-0xfffffe000b944c70 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049409d0-0x04940a98 addr=0xfffffe000b9449d0-0xfffffe000b944a98               __DATA.__data             
	sz=0x000001d8 off=0x00000000-0x000001d8 addr=0xfffffe000b944a98-0xfffffe000b944c70               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00004aa8 off=0x01091980-0x01096428 addr=0xfffffe0008095980-0xfffffe000809a428 rw-/rw-   __DATA_CONST      
	sz=0x00000040 off=0x01091980-0x010919c0 addr=0xfffffe0008095980-0xfffffe00080959c0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000040 off=0x010919c0-0x01091a00 addr=0xfffffe00080959c0-0xfffffe0008095a00         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00004558 off=0x01091a00-0x01095f58 addr=0xfffffe0008095a00-0xfffffe0008099f58         __DATA_CONST.__const            
	sz=0x00000280 off=0x01095f58-0x010961d8 addr=0xfffffe0008099f58-0xfffffe000809a1d8         __DATA_CONST.__kalloc_type      
	sz=0x00000170 off=0x010961d8-0x01096348 addr=0xfffffe000809a1d8-0xfffffe000809a348         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000e0 off=0x01096348-0x01096428 addr=0xfffffe000809a348-0xfffffe000809a428         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 120 at 0x04ad9524
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     9CF7986D-1BE6-362A-A52A-2514AFFAD322
008: LC_SOURCE_VERSION           717.40.5.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9f800 size=0x110
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleEmbeddedUSBHost`
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedUSBHost`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleEmbeddedUSBHost`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1`
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
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleEmbeddedUSBHost.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901206800`
- `_PrelinkExecutableRelativePath`: `AppleEmbeddedUSBHost`
- `_PrelinkExecutableSize`: `53168`
- `_PrelinkExecutableSourceAddr`: `-2198901206800`
- `_PrelinkKmodInfo`: `-2198828987952`

## Strings (120) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.AppleUSB20AccessoryHubPort`
- `powerStateWillChangeTo`
- `site.AppleUSB30AccessoryHub`
- `%06lu.%06u %s::%s: data interface match\n`
- `%s@%s: %s::%s: failed to enable port %d\n`
- `%s@%s: %s::%s: skipping offset 0x%02x mask 0x%02x value 0x%02x (already set)\n`
- `writeVendorRegister`
- `AppleUSBHubIICDeviceTunables`
- `%s: %s::%s: address 0x%02x, value 0x%02x returned %s\n`
- `AppleUSBHostiOSDevice`
- `probe`
- `%06lu.%06u %s::%s: control interface match\n`
- `%06lu.%06u %s::%s: sending simulated connect\n`
- `%s@%s: %s::%s: disabled port %d\n`
- `AppleUSB2RepeaterIICDevice`
- `%06lu.%06u %s::%s: \n`
- `site.AppleUSB30AccessoryHubPort`
- `AppleUSBHostCompositeDevice`
- `iAPAuthenticationRequired`
- `isIAPInterface`
- `AppleUSBEHCIRemovablePort`
- `Unknown`
- `%s@%s: %s::%s: enabled port %d\n`
- `site.AppleUSBHubIICDevice`
- `AppleUSBHostPort`
- `open`
- `site.AppleUSB20AccessoryHub`
- `%s: %s::%s: %d\n`
- `%s: %s::%s: applying offset 0x%02x mask 0x%02x value 0x%02x\n`
- `%s: %s::%s: skipping offset 0x%02x mask 0x%02x value 0x%02x (already set)\n`
- `%s: %s::%s: failed to find AppleUSBHostPort for %s\n`
- `AppleEmbeddedUSBDevice`
- `Unconfigured`
- `%s@%s: %s::%s: failed to disable port %d\n`
- `powerStateDidChangeTo`
- `UsbAllowSoftRetry`
- `AppleTICD2E22`
- `B24@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{IONotifier=^^?i}16`
- `%s@%s: %s::%s: register 0x%04x value 0x%02x -> 0x%02x\n`
- `AppleUSB20AccessoryHub`
- `tunable`
- `UsbHostControllerSoftRetryPolicy`
- `idVendor`
- `%06lu.%06u %s::%s: interface string match\n`
- `site.AppleTICD2E22`
- `Device`
- `tunable-vlf0`
- `%s: %s::%s: port powering on\n`
- `writeRegister`
- `12111112122212121`
- `%06lu.%06u %s::%s: CarPlay device or hub connected at full-speed.  Attempting to recover to high-speed\n`
- `isNCMInterface`
- `hubReset`
- `applyTunables`
- `%s: %s::%s: failed offset 0x%08x\n`
- `%06lu.%06u %s::%s: Recovery device connected at full-speed.  Attempting to recover to high-speed\n`
- `%s@%s: %s::%s: address 0x%02x, value 0x%02x returned %s\n`
- `%s@%s: %s::%s: register 0x%04x failed with 0x%08x\n`
- `site.AppleEmbeddedUSBDeviceSupport`
- `121111121222121211211111111111212222111111111111111111222222222222222222221`
- `AppleUSB20AccessoryHubPort`
- `AppleUSB30AccessoryHub`
- `AppleUSBHubIICDevice`
- `readRegister`
- `%s: %s::%s: failed to build dictionary for %s\n`
- `AppleEmbeddedUSBDeviceSupport`
- `function-reset`
- `tunable-gl`
- `site.AppleEmbeddedUSBDevice`
- `%06lu.%06u %s::%s: interface match\n`
- `AppleUSB2RepeaterIICDevicePortState`
- `%s@%s: %s::%s: applying offset 0x%02x mask 0x%02x value 0x%02x\n`
- `AppleUSB20Hub_32789`
- `site.AppleUSB20Hub_32789`
- `AppleUSB30AccessoryHubPort`
- `12111112122212121112112`
- `%s: %s::%s: port powered off\n`
- `AAPL,phandle`
- `copyPortForPhandle`
- `B16@?0^{OSSerialize=^^?i*III^{OSArray}^{OSArray}BB^v^v^{OSData}I}8`
- `%s@%s: %s::%s: failed offset 0x%08x\n`
- `%s@%s: %s::%s: register 0x%04x value 0x%02x already set\n`
- `1211111212221212112222222122222222222222222222222222222222222222222222222222212211111222211121122222222222111221121111111111111121`
- `121111121222121211222222212222222222222222222222222222222222222222222222222221221111122221112112222222222211122112111111111111112122`
- `usb-port`
- `close`
- `Genesys Logic`
- `VIA Labs`
- `AppleUSBHostMergeProperties`
- `iAP Interface`
- `1211111212221212111112`
- `Host`
- `site.AppleUSB2RepeaterIICDevice`
- `AppleUSBHubIICDeviceVendor`
- `tunable-vl`
- `AppleUSBHubIICDeviceResetFunction`
- `1211111212221212121111112111221112121222212`
- `AppleEmbeddedDeviceSupport`
- `idProduct`
- `attemptRecovery`

**[__TEXT.__os_log]**

- `%s: %s::%s: %d\n`
- `%s: %s::%s: applying offset 0x%02x mask 0x%02x value 0x%02x\n`
- `%s: %s::%s: skipping offset 0x%02x mask 0x%02x value 0x%02x (already set)\n`
- `%s@%s: %s::%s: disabled port %d\n`
- `%s@%s: %s::%s: address 0x%02x, value 0x%02x returned %s\n`
- `%s@%s: %s::%s: skipping offset 0x%02x mask 0x%02x value 0x%02x (already set)\n`
- `%s@%s: %s::%s: failed offset 0x%08x\n`
- `%s: %s::%s: port powering on\n`
- `%s: %s::%s: port powered off\n`
- `%s: %s::%s: address 0x%02x, value 0x%02x returned %s\n`
- `%s: %s::%s: failed to build dictionary for %s\n`
- `%s@%s: %s::%s: failed to enable port %d\n`
- `%s: %s::%s: failed offset 0x%08x\n`
- `%s@%s: %s::%s: enabled port %d\n`
- `%s@%s: %s::%s: failed to disable port %d\n`
- `%s@%s: %s::%s: applying offset 0x%02x mask 0x%02x value 0x%02x\n`
- `%s@%s: %s::%s: register 0x%04x value 0x%02x already set\n`
- `%s@%s: %s::%s: register 0x%04x failed with 0x%08x\n`
- `%s: %s::%s: failed to find AppleUSBHostPort for %s\n`
- `%s@%s: %s::%s: register 0x%04x value 0x%02x -> 0x%02x\n`
