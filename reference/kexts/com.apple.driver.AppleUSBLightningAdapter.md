# `com.apple.driver.AppleUSBLightningAdapter`

- Name: AppleUSBLightningAdapter
- Version: `1`
- UUID: `66372671-51C4-39A4-AB36-AB139C16A1AB`
- Source version: `95.0.0.0.0`
- Depends on: [`com.apple.driver.AppleUVDM`](com.apple.driver.AppleUVDM.md) 1.0.0, [`com.apple.iokit.IOAccessoryManager`](com.apple.iokit.IOAccessoryManager.md) 1.0.0, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.2, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 21.5, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 21.5

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (4) [KC]

### A2868-EmbeddedUSB
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBLightningAdapter`
- `IOClass`: `AppleUSBLightningAdapterBOS`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBLightningAdapter`
- `IOProviderClass`: `AppleEmbeddedUSBDevice`
- `idProduct`: `5904`
- `idVendor`: `1452`

### A2868-PD
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBLightningAdapter`
- `IOClass`: `AppleUSBLightningAdapter`
- `IOParentMatch`:
  - `IOPropertyMatch`:
    - `Product ID`: `5904`
    - `Vendor ID`: `1452`
  - `IOProviderClass`: `IOPortTransportProtocolAppleUVDM`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBLightningAdapter`
- `IOPropertyMatch`:
  - `Protocol ID`: `9`
- `IOProviderClass`: `AppleUVDMEndpoint`

### A2868-USB
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBLightningAdapter`
- `IOClass`: `AppleUSBLightningAdapterBOS`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBLightningAdapter`
- `IOProviderClass`: `IOUSBHostDevice`
- `idProduct`: `5904`
- `idVendor`: `1452`

### A2869-USB
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBLightningAdapter`
- `IOClass`: `AppleUSBLightningAdapterBOS`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBLightningAdapter`
- `IOProviderClass`: `IOUSBHostDevice`
- `idProduct`: `5905`
- `idVendor`: `1452`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBLightningAdapter` | 0xe90 | IOAccessoryManager → IOPort → IOPortFamily → IOService → IORegistryEntry |
| `AppleUSBLightningAdapterBOS` | 0x88 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000027e9 off=0x008d8960-0x008db149 addr=0xfffffe00078dc960-0xfffffe00078df149 r--/r--   __TEXT            
	sz=0x00000008 off=0x008d9028-0x008d9030 addr=0xfffffe00078dd028-0xfffffe00078dd030               __TEXT.__const            
	sz=0x0000135b off=0x008d9030-0x008da38b addr=0xfffffe00078dd030-0xfffffe00078de38b               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000dbe off=0x008da38b-0x008db149 addr=0xfffffe00078de38b-0xfffffe00078df149               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00006030 off=0x02b45ec0-0x02b4bef0 addr=0xfffffe0009b49ec0-0xfffffe0009b4fef0 r-x/r-x   __TEXT_EXEC       
	sz=0x00005ce0 off=0x02b45ec0-0x02b4bba0 addr=0xfffffe0009b49ec0-0xfffffe0009b4fba0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000350 off=0x02b4bba0-0x02b4bef0 addr=0xfffffe0009b4fba0-0xfffffe0009b4fef0          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x0000012a off=0x049d17b8-0x049d18e2 addr=0xfffffe000b9d57b8-0xfffffe000b9d58e2 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x049d17b8-0x049d187c addr=0xfffffe000b9d57b8-0xfffffe000b9d587c               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b9d5880-0xfffffe000b9d58e0               __DATA.__common           (Zerofill)
	sz=0x00000002 off=0x00000000-0x00000002 addr=0xfffffe000b9d58e0-0xfffffe000b9d58e2               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001190 off=0x012ade60-0x012aeff0 addr=0xfffffe00082b1e60-0xfffffe00082b2ff0 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x012ade60-0x012ade70 addr=0xfffffe00082b1e60-0xfffffe00082b1e70         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x012ade70-0x012ade80 addr=0xfffffe00082b1e70-0xfffffe00082b1e80         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000ea0 off=0x012ade80-0x012aed20 addr=0xfffffe00082b1e80-0xfffffe00082b2d20         __DATA_CONST.__const            
	sz=0x00000080 off=0x012aed20-0x012aeda0 addr=0xfffffe00082b2d20-0xfffffe00082b2da0         __DATA_CONST.__kalloc_type      
	sz=0x000001a8 off=0x012aeda0-0x012aef48 addr=0xfffffe00082b2da0-0xfffffe00082b2f48         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000a8 off=0x012aef48-0x012aeff0 addr=0xfffffe00082b2f48-0xfffffe00082b2ff0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 127 at 0x04aec538
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     66372671-51C4-39A4-AB36-AB139C16A1AB
008: LC_SOURCE_VERSION           95.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab79c8 size=0x90
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleUSBLightningAdapter`
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBLightningAdapter`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUSBLightningAdapter`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
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
- `NSHumanReadableCopyright`: `Copyright © 2022 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleUSBLightningAdapter.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896522912`
- `_PrelinkExecutableRelativePath`: `AppleUSBLightningAdapter`
- `_PrelinkExecutableSize`: `39635`
- `_PrelinkExecutableSourceAddr`: `-2198896522912`
- `_PrelinkKmodInfo`: `-2198828394568`

## Strings (180) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `[ERROR] %s::%s(): Failed to create ACC_PWR toggle timer!\n`
- `free`
- `[ERROR] %s::%s(): Failed to read AUVDM USBMode! (status:%08x) (failCode: %u), returnLen: %d\n`
- `[ERROR] %s::%s(): Failed to write AUVDM BOS string descriptor index! (failCode: %u, stringIndex: %u)\n`
- `[ERROR] %s::%s(): Failed to read AUVDM BOS string descriptor! (failCode: %u, stringIndex: %u, currentRegAddr: 0x%02x)\n`
- `[ERROR] %s::%s(): Invalid string index for AID Accessory Name!\n`
- `[ERROR] %s::%s(): Invalid string index for MB Product Name!\n`
- `Accessory Vendor`
- `Interface Chip Product ID`
- `Interface Chip Serial Number`
- `[ERROR] %s::%s(): Skipping current limit updates due to no upstream manager!\n`
- `getAccessoryAttached`
- `auxpRearPortControlAccessoryUSBMode`
- `[ERROR] %s::%s(): Invalid string index!\n`
- `auxpReadBOSString`
- `Digital ID`
- `B24@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{IONotifier=^^?i}16`
- `Accessory Name`
- `Active Configuration Number`
- `auxpProtocolVersion`
- `Interface Device Revision`
- `[ERROR] %s::%s(): Failed to open AUVDM endpoint!\n`
- `[ERROR] %s::%s(): Failed to write AUVDM current limit! (failCode: %u)\n`
- `IMSN`
- `iAPAuthenticationRequired`
- `96F08FA9-7B44-4781-8733-15E25E61B8AA`
- `[ERROR] %s::%s(): Invalid string index for AID Accessory Model!\n`
- `Accessory Hardware Version Minor`
- `v16@?0^{IOTimerEventSource=^^?i^{IOEventSource}^{OSObject}^?B^{IOWorkLoop}^v^{ExpansionData}^vQ^{ExpansionData}}8`
- `[ERROR] %s::%s(): Invalid string index for IMSN!\n`
- `[ERROR] %s::%s(): Error. Failed to create _startGatedTimer\n\n`
- `NULL`
- `Product Model Number`
- `Product Vendor ID`
- `[ERROR] %s::%s(): Invalid string index for MB Product Vendor Name!\n`
- `[ERROR] %s::%s(): Failed to read AUVDM bos descriptor header! (status:%08x) (failCode: %u), returnLen: %d\n`
- `site.AppleUSBLightningAdapterBOS`
- `setAccessoryDigitalID`
- `[ERROR] %s::%s(): Invalid string index for MB Product SN!\n`
- `[ERROR] %s::%s(): Failed to read AUVDM bos descriptor! (status:%08x) (failCode: %u), returnLen: %d\n`
- `IDSN`
- `Version`
- `site.AppleUSBLightningAdapter`
- `Product Hardware Revision`
- `auxpBosInfo`
- `AppleUSBLightningAdapterBOS`
- `Accessory Firmware Version Major`
- `Product ID`
- `121111121222121211111121111121222222221122111111121221111222222122221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211221211`
- `[ERROR] %s::%s(): AppleUSBLightningAdapter: super::start failed\n`
- `i36@?0I8^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}12^v20Q28`
- `startGated`
- `Accessory Firmware Version Rev`
- `Accessory HID PID`
- `startCurrentLimitUpdates`
- `handleAccessoryDetect`
- `[ERROR] %s::%s(): Invalid string index for MB Product FW Rev!\n`
- `[ERROR] %s::%s(): !workloop\n`
- `YES`
- `Accessory HID VID`
- `Interface Chip Vendor ID`
- `[ERROR] %s::%s(): Invalid string length! (stringLength: %u)\n`
- `[ERROR] %s::%s(): Invalid string index for MB Product Model!\n`
- `getAccessoryDigitalID`
- `[ERROR] %s::%s(): Failed to read AUVDM BOS string length! (failCode: %u, stringIndex: %u)\n`
- `Product Serial Number`
- `stop`
- `getUpstreamManager`
- `[ERROR] %s::%s(): Failed to open AUVDM endpoint! (stringIndex: %u)\n`
- `[ERROR] %s::%s(): kIOAccessoryPortIDInvalid\n`
- `[ERROR] %s::%s(): Error. Failed to create _powerSourceUpdateEvent\n\n`
- `start_block_invoke_2`
- `auxpRearPortControlAccPower`
- `Accessory Model`
- `Product Firmware Revision`
- `handlePowerSourceUpdateEvent`
- `Product Vendor Name`
- `Interface Device PID`
- `Interface Chip Revision`
- `[ERROR] %s::%s(): Failed to read AUVDM protocol version! (status:%08x) (failCode: %u), returnLen: %d\n`
- `Accessory Hardware Version Major`
- `start_block_invoke`
- `Interface Device VID`
- `IOAccessoryManagerAccessoryPowerModeOnAtStart`
- `MikeyBus Info`
- `AID Info`
- `[ERROR] %s::%s(): Failed to write AUVDM update command! (failCode: %u)\n`
- `Protocol ID`
- `NO`
- `[ERROR] %s::%s(): Invalid string index for ASN!\n`
- `[ERROR] %s::%s(): BOS wTotalLength changed mid-read: was %u, now %u\n`
- `[ERROR] %s::%s(): Error starting %s!\n`
- `auxpRearPortControlHostUSBReady`
- `readBOSStrings`
- `[ERROR] %s::%s(): Invalid string index for AID Accessory Manufacturer!\n`
- `[ERROR] %s::%s(): Invalid string index for MB Product HW Rev!\n`
- `[ERROR] %s::%s(): Incorrect wTotalLength: %d\n`
- `Total Configurations`
- `IOAccessoryManagerSleepPower`
- `Accessory Manufacturer`
- `Differential Voltage Class`
- `AppleUSBLightningAdapter`
- `[ERROR] %s::%s(): No power source items found!\n`
- `[ERROR] %s::%s(): Failed to write AUVDM AccPower! (failCode: %u)\n`
- `auxpCurrentLimit`
- `12111112122212121`
- `Accessory Hardware Version Rev`
- `start`
- `USB Mode`
- `setAccessoryPower`
- `v8@?0`
- `ASN`
- `Product Name`
- `Accessory Firmware Version Minor`
- `[ERROR] %s::%s(): No power source found!\n`
- `[ERROR] %s::%s(): Failed to write AUVDM HostUSBReady! (failCode: %u)\n`

**[__TEXT.__os_log]**

- `%s::%s(): auxpRearPortControlAccessoryUSBMode %s\n`
- `%s::%s(): stringLength: %u, stringIndex: %u, readCount: %u\n`
- `%s::%s(): auxpBosInfo %s\n`
- `Unable to open USB device!`
- `Accessory Info Version not available!`
- `%s::%s(): Registering for USB2 transport notifications...\n`
- `%s::%s(): startGated: protocol version: %d\n`
- `Could not read USB string descriptor! (index: %d)`
- `%s::%s(): Implicitly marking transport as user authorized...\n`
- `%s::%s(): auxpProtocolVersion %s: %d\n`
- `%s::%s(): auxpRearPortControlHostUSBReady %s\n`
- `%s::%s(): stringLength: %u, stringIndex: %u, readCount: %u, currentRegAddr: 0x%04x\n`
- `!pCapabilityData`
- `Starting %s...`
- `mikeyBusInfoDict->count: %u`
- `%s::%s(): Stopping %s...\n`
- `%s::%s(): Freeing %s...\n`
- `Invalid platform descriptor length!`
- `%s::%s(): startGated: digitalId: %02x %02x %02x %02x %02x %02x\n`
- `%s::%s(): auxpRearPortControlAccPower: %d\n`
- `%s::%s(): Received authorization state change for USB2 transport... (authorizationStatus: %d [%s], transportRestricted: %s)\n`
- `currentPlatformDescriptor->bLength: %u, payloadLength: %lu`
- `Platform descriptor length larger than expected! (bLength: %u, expectedDescriptorLength: %u)`
- `HID Descriptor not available!`
- `%s::%s(): _start\n`
- `%s::%s(): Matched on USB2 transport service... (transport: %s)\n`
- `%s::%s(): USB2 transport has been unrestricted!\n`
- `%s::%s(): getAccessoryAttached %s\n`
- `%s::%s(): getAccessoryDigitalID %s\n`
- `!aidInfoDict`
- `%s::%s(): Toggling ACC_PWR for %d ms...\n`
- `%s::%s(): setAccessoryPower %d\n`
- `%s::%s(): Current limit base: %d host: %d resolved %d\n`
- `%s::%s(): Finished stopping %s!\n`
- `%s::%s(): upstreamService is NULL\n`
- `%s::%s(): parentService is NULL\n`
- `Accessory Info Strings not available!`
- `_getCapabilityData`
- `Could not find the platform capability descriptor!`
- `%s::%s(): Received active state change for USB2 transport... (transportActive: %s)\n`
- `%s::%s(): currentSystemUptimeS: %llu, m_explicitUserAuthorizationTimestampS: %llu\n`
- `%s::%s(): AppleUSBLightningAdapter::startGated\n`
- `%s::%s(): handleAccessoryDetect: accessoryDetect:%d\n`
- `%s::%s(): USB2 transport has been user authorized!\n`
- `%s::%s(): requestProbe\n`
- `Could not read BOS descriptor!`
- `%s::%s(): Registering for interest notifications on USB2 transport service... (transport: %s)\n`
- `Could not find pCapabilityData!`
- `MikeyBus info not available!`
- `%s::%s(): Updated user authorization timestamp for USB2! (m_explicitUserAuthorizationTimestampS: %llu)\n`
- `%s::%s(): getAccessoryAttached: attached:%d\n`
- `%s::%s(): auxpProtocolVersion %s\n`
- `%s::%s(): auxpRearPortControlAccessoryUSBMode %s: %d\n`
- `Found platform capability descriptor! (uuid: %s)`
- `%s::%s(): setAccessoryDigitalID %s\n`
- `%s::%s(): stringIndex: %u, string: %s\n`
- `readAccess failed with: %08x`
- `!mikeyBusInfoDict`
- `aidInfoDict->count: %u`
- `Could not parse UUID string!`
- `%s::%s(): Finished starting %s!\n`
- `%s::%s(): auxpCurrentLimit %s %d\n`
- `pCapabilityData->supportedFields: 0x%04X`
- `%s::%s(): handleAccessoryDetect %s\n`
