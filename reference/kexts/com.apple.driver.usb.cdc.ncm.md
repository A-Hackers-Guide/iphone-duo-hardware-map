# `com.apple.driver.usb.cdc.ncm`

- Name: AppleUSBNCM
- Version: `5.0.0`
- UUID: `1FDF1809-FCC7-3027-BF33-99F065DF4CE5`
- Source version: `404.40.4.0.0`
- Depends on: [`com.apple.driver.usb.AppleUSBHostCompositeDevice`](com.apple.driver.usb.AppleUSBHostCompositeDevice.md) 1.0, [`com.apple.driver.usb.cdc`](com.apple.driver.usb.cdc.md) 5.0, [`com.apple.driver.usb.networking`](com.apple.driver.usb.networking.md) 5.0, [`com.apple.iokit.IONetworkingFamily`](com.apple.iokit.IONetworkingFamily.md) 3.3, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.0.1, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 14.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 14.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 14.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (5) [KC]

### AppleUSBNCM11Control
- `CFBundleIdentifier`: `com.apple.driver.usb.cdc.ncm`
- `IOClass`: `AppleUSBNCM11Control`
- `IOPersonalityPublisher`: `com.apple.driver.usb.cdc.ncm`
- `IOProviderClass`: `IOUSBHostInterface`
- `bInterfaceClass`: `2`
- `bInterfaceProtocol`: `*`
- `bInterfaceSubClass`: `13`

### AppleUSBNCM11Data0
- `CFBundleIdentifier`: `com.apple.driver.usb.cdc.ncm`
- `IOClass`: `AppleUSBNCM11Data`
- `IOPersonalityPublisher`: `com.apple.driver.usb.cdc.ncm`
- `IOProviderClass`: `AppleUSBNCM11Control`

### AppleUSBNCMControl
- `CFBundleIdentifier`: `com.apple.driver.usb.cdc.ncm`
- `IOClass`: `AppleUSBNCMControl`
- `IOPersonalityPublisher`: `com.apple.driver.usb.cdc.ncm`
- `IOProviderClass`: `IOUSBHostInterface`
- `bInterfaceClass`: `2`
- `bInterfaceProtocol`: `*`
- `bInterfaceSubClass`: `13`

### AppleUSBNCMData0
- `CFBundleIdentifier`: `com.apple.driver.usb.cdc.ncm`
- `IOClass`: `AppleUSBNCMData`
- `IOPersonalityPublisher`: `com.apple.driver.usb.cdc.ncm`
- `IOProviderClass`: `AppleUSBNCMControl`

### AppleUSBNCMData13
- `CFBundleIdentifier`: `com.apple.driver.usb.cdc.ncm`
- `IOClass`: `AppleUSBNCMData`
- `IOPersonalityPublisher`: `com.apple.driver.usb.cdc.ncm`
- `IOProviderClass`: `AppleUSBNCMControl`


## C++ classes (6) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBHostNCMRestrictedEthernetInterface` | 0x148 | IOEthernetInterface → IONetworkInterface → IOService → IORegistryEntry |
| `AppleUSBNCM11Control` | 0x1e8 | AppleUSBNCMControl → AppleUSBCDCControl → IOService → IORegistryEntry |
| `AppleUSBNCM11Data` | 0x848 | AppleUSBNCMData → IOEthernetController → IONetworkController → IOService → IORegistryEntry |
| `AppleUSBNCMControl` | 0x1a8 | AppleUSBCDCControl → IOService → IORegistryEntry |
| `AppleUSBNCMData` | 0x848 | IOEthernetController → IONetworkController → IOService → IORegistryEntry |
| `AppleUSBNCMDataPoller` | 0x48 | IOEventSource |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00002bda off=0x008dcdb0-0x008df98a addr=0xfffffe00078e0db0-0xfffffe00078e398a r--/r--   __TEXT            
	sz=0x0000248b off=0x008dd428-0x008df8b3 addr=0xfffffe00078e1428-0xfffffe00078e38b3               __TEXT.__cstring          (CstringLiterals)
	sz=0x000000ca off=0x008df8c0-0x008df98a addr=0xfffffe00078e38c0-0xfffffe00078e398a               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x0000d0a8 off=0x02b52170-0x02b5f218 addr=0xfffffe0009b56170-0xfffffe0009b63218 r-x/r-x   __TEXT_EXEC       
	sz=0x0000cae8 off=0x02b52170-0x02b5ec58 addr=0xfffffe0009b56170-0xfffffe0009b62c58          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000005c0 off=0x02b5ec58-0x02b5f218 addr=0xfffffe0009b62c58-0xfffffe0009b63218          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001cc off=0x049d1a38-0x049d1c04 addr=0xfffffe000b9d5a38-0xfffffe000b9d5c04 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049d1a38-0x049d1b00 addr=0xfffffe000b9d5a38-0xfffffe000b9d5b00               __DATA.__data             
	sz=0x00000100 off=0x00000000-0x00000100 addr=0xfffffe000b9d5b00-0xfffffe000b9d5c00               __DATA.__common           (Zerofill)
	sz=0x00000004 off=0x00000000-0x00000004 addr=0xfffffe000b9d5c00-0xfffffe000b9d5c04               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00002d98 off=0x012afb38-0x012b28d0 addr=0xfffffe00082b3b38-0xfffffe00082b68d0 rw-/rw-   __DATA_CONST      
	sz=0x00000020 off=0x012afb38-0x012afb58 addr=0xfffffe00082b3b38-0xfffffe00082b3b58         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000020 off=0x012afb58-0x012afb78 addr=0xfffffe00082b3b58-0xfffffe00082b3b78         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00002870 off=0x012afb78-0x012b23e8 addr=0xfffffe00082b3b78-0xfffffe00082b63e8         __DATA_CONST.__const            
	sz=0x00000180 off=0x012b23e8-0x012b2568 addr=0xfffffe00082b63e8-0xfffffe00082b6568         __DATA_CONST.__kalloc_type      
	sz=0x000002e0 off=0x012b2568-0x012b2848 addr=0xfffffe00082b6568-0xfffffe00082b6848         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000088 off=0x012b2848-0x012b28d0 addr=0xfffffe00082b6848-0xfffffe00082b68d0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 201 at 0x04aec928
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     1FDF1809-FCC7-3027-BF33-99F065DF4CE5
008: LC_SOURCE_VERSION           404.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab7ac0 size=0x1e0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleUSBNCM`
- `CFBundleIdentifier`: `com.apple.driver.usb.cdc.ncm`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUSBNCM`
- `CFBundleNumericVersion`: `83918848`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `5.0.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `5.0.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2017 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `5.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleUSBNCM.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896505424`
- `_PrelinkExecutableRelativePath`: `AppleUSBNCM`
- `_PrelinkExecutableSize`: `76774`
- `_PrelinkExecutableSourceAddr`: `-2198896505424`
- `_PrelinkKmodInfo`: `-2198828393928`

## Strings (241) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%06lu.%06u [0x%llx] %s::%s: Transmit Offload descriptor too small (%u bytes)\n`
- `cacheExtendedDescriptors`
- `NTBFormat`
- `%06lu.%06u [0x%llx][%s] %s::%s: unable to allocate thread call\n`
- `configureInterface`
- `InterfaceRole`
- `%06lu.%06u [0x%llx] %s::%s: Device supports segmentation transmit offload (TSO)\n`
- `InputSizeMax`
- `OutputSize`
- `setPacketFilter`
- `getNTBInputSize`
- `NO`
- `Out Frames`
- `device-idle-timeout`
- `cacheNTBParameters`
- `%06lu.%06u [0x%llx] %s::%s: Extended Capability Mode: %u status: 0x%x\n`
- `DatagramOutputCount`
- `%06lu.%06u [0x%llx] %s::%s:     - TCP/UDP Port: %s\n`
- `DatagramOutputCountCalculatedMax`
- `DatagramSizePreferred`
- `In Length`
- `ncm_interface_flags`
- `%06lu.%06u [0x%llx] %s::%s:     - Any Packet: %s\n`
- `Never`
- `%06lu.%06u [0x%llx] %s::%s: NCM 1.1 probe result %p, score %d\n`
- `%06lu.%06u [0x%llx] %s::%s: Device supports coalescing receive offload\n`
- `site.AppleUSBNCMDataPoller`
- `%06lu.%06u [0x%llx][%s] %s::%s: provider %p, fControlDriver %p\n`
- `AppleUSBNCMData.cpp`
- `%06lu.%06u [0x%llx][%s] %s::%s: Status: 0x%x\n`
- `Ethernet`
- `%06lu.%06u [0x%llx] %s::%s: Device supports mDNS presence offload\n`
- `powerStateDidChangeTo`
- `IPv4`
- `CarPlay`
- `getDatagramLimit`
- `getExtendedCapabilities`
- `getExtendedFeatureWake`
- `setExtendedFeatureWake`
- `%06lu.%06u [0x%llx] %s::%s: Device supports unknown wake type: 0x%02x\n`
- `%06lu.%06u [0x%llx] %s::%s:     - Media Connect: %s\n`
- `%06lu.%06u [0x%llx] %s::%s:       • Coalescing: %s\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: newMedium, bMediumType 0x%x, bmFeatureFlags 0x%x, dwSpeed 0x%x, bmMediumParameters 0x%x\n`
- `getMACAddressFromDescriptor`
- `%06lu.%06u [0x%llx] %s::%s: filter: %u status: %#x\n`
- `1211111212221212111111122121111111112112112111221111211112111121111211112111121111211112111121111211112111121111211112111121111211112111112111112111112111112111112111112111112111112111112111112111112111112111112111112111112112222211221111122222222112111211222222222`
- `setCarPlayProperties`
- `probe`
- `%06lu.%06u [0x%llx] %s::%s:     - Parameters: 0x%08x\n`
- `notificationCallbackGated`
- `Patching invalid NCM 1.1 NTB parameter wNdpOutAlignment %d\n`
- `%06lu.%06u [0x%llx] %s::%s: fEaddr : %02x:%02x:%02x:%02x:%02x:%02x, stringIndex %d\n`
- `%06lu.%06u [0x%llx] %s::%s: Device supports VLAN transmit offload\n`
- `IPv6`
- `%06lu.%06u [0x%llx] %s::%s: Device supports NS presence offload\n`
- `%06lu.%06u [0x%llx] %s::%s:     - Media Disconnect: %s\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: result: %d\n`
- `setNetworkAddress`
- `%06lu.%06u [0x%llx] %s::%s: %x \n`
- `%06lu.%06u [0x%llx][%s] %s::%s: status %#x\n`
- `NetworkConfigurationOverrides`
- `IOEthernetStatsKey`
- `NCMOperatingMode`
- `setDatagramLimit`
- `%06lu.%06u [0x%llx] %s::%s:     - mDNS Responder: %s\n`
- `%06lu.%06u [0x%llx] %s::%s:     - Pattern Filter: %s\n`
- `setCRCMode`
- `%06lu.%06u [0x%llx] %s::%s: Device supports VLAN receive offload\n`
- `%06lu.%06u [0x%llx] %s::%s:     - Medium Type: %s (0x%02x)\n`
- `USB NCM Data Stats`
- `%06lu.%06u [0x%llx][%s] %s::%s: fNetifEnabled %d, result %#x, bytesTransferred %d\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: too many consecutive IO errors (%u), not re-enqueueing\n`
- `%06lu.%06u [0x%llx] %s::%s: length: %u supported formats: %u reserved: %u\n`
- `%06lu.%06u [0x%llx] %s::%s: Receive Offload descriptor too small (%u bytes)\n`
- `%06lu.%06u [0x%llx] %s::%s:     - Speed: %u\n`
- `setPropertiesForInterfaceRole`
- `YES`
- `idVendor`
- `OutputRecordCount`
- `willTerminate`
- `%06lu.%06u [0x%llx][%s] %s::%s: linkStatus %d, fNetifEnabled %d\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: re-enqueue after stall returned 0x%x\n`
- `%06lu.%06u [0x%llx] %s::%s: [OUT] max size: %u divisor: %u payload remainder: %u alignment: %u max datagrams: %u\n`
- `%06lu.%06u [0x%llx] %s::%s: Attempting to switch to NCM 1.1 mode\n`
- `Unknown`
- `%06lu.%06u [0x%llx][%s] %s::%s: failed to clear stall : 0x%x\n`
- `AppleUSBNCMControl`
- `%06lu.%06u [0x%llx] %s::%s: returning %p\n`
- `%06lu.%06u [0x%llx] %s::%s: Device supports unknown transmit offload type: 0x%02x\n`
- `AppleUSBNCM11Control`
- `%06lu.%06u [0x%llx] %s::%s: Device feature summary:\n`
- `ncm-data-maxpool`
- `Patching invalid HU NTB parameter wNdpInAlignment %d\n`
- `%06lu.%06u [0x%llx] %s::%s: [IN] max size: %u divisor: %u payload remainder: %u alignment: %u\n`
- `%06lu.%06u [0x%llx] %s::%s: Successfully switched to NCM 1.1 mode\n`
- `%06lu.%06u [0x%llx] %s::%s: Presence Offload Type: %u length: %u status: 0x%x\n`
- `%06lu.%06u [0x%llx] %s::%s: Device supports checksum transmit offload\n`
- `HiddenConfiguration`
- `%06lu.%06u [0x%llx] %s::%s: NCM 1.0 probe result %p, score %d\n`
- `%06lu.%06u [0x%llx] %s::%s: Parsing NCM Extended Capabilities (total length: %u)\n`
- `waitBsdFailure`
- `%06lu.%06u [0x%llx][%s] %s::%s: Unsupported role: %s\n`
- `getNTBFormat`
- `%06lu.%06u [0x%llx] %s::%s: Receive Offload Type: %u length: %u status: 0x%x\n`
- `ncm-data-maxntb`
- `waitBsdSuccess`
- `%06lu.%06u [0x%llx] %s::%s: Extended Capabilities length: %u status: 0x%x\n`
- `%06lu.%06u [0x%llx] %s::%s: `
- `getPacketFilter`
- `%06lu.%06u [0x%llx] %s::%s: Device supports checksum receive offload\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: error waiting for BSD name %#x\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: result: %#x\n`
- `iBridge`
- `setNTBInputSize`
- `%06lu.%06u [0x%llx] %s::%s: Datagram limit: %u status: %d\n`
- `%06lu.%06u [0x%llx] %s::%s: Medium Type: %u status: 0x%x\n`
- `%06lu.%06u [0x%llx] %s::%s:       • Segmentation (TSO): %s\n`
- `%06lu.%06u [0x%llx] %s::%s:     - Presence Offload: %s\n`
- `%06lu.%06u [0x%llx] %s::%s:     - Transmit Offload: %s\n`
- `%06lu.%06u [0x%llx] %s::%s:       • Store Bad Packets: %s\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: unhandled notification %d\n`
- `anri`
- `copyDataInterface`
- `AppleUSBNCM11Data`
- `dbg-ncm-netif`
- `%06lu.%06u [0x%llx] %s::%s: Medium Handling descriptor too small (%u bytes)\n`
- `%06lu.%06u [0x%llx] %s::%s:       • RSS: %s\n`
- `NTBFormatsSupported`
- `setExtendedCapabilityMode`
- `USB NCM`
- `DatagramSizeMax`
- `configureData`
- `IONetworkStatsKey`
- `%06lu.%06u [0x%llx] %s::%s:     - Receive Offload: %s\n`
- `AppleUSBNCMData`
- `armRead`
- `Patching invalid NCM 1.1 NTB parameter wNdpInAlignment %d\n`
- `AppleUSBHostNCMRestrictedEthernetInterface`
- `InputRecordCount`
- `%06lu.%06u [0x%llx][%s] %s::%s: result: %d, IN EP 0x%x, OUT EP 0x%x\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: bNotification 0x%x\n`
- `setMulticastFilter`
- `%06lu.%06u [0x%llx] %s::%s: result: %d\n`
- `%06lu.%06u [0x%llx] %s::%s: Attempting to fetch extended capabilities\n`
- `ncm-data-debug`
- `waitBsdStart`
- `setAlternate`
- `dataReadComplete`
- `DHCP`
- `ncm-ctrl-debug`
- `%06lu.%06u [0x%llx] %s::%s: len: %u status: %d\n`
- `%06lu.%06u [0x%llx] %s::%s: NCM 1.1 driver: device supports extended capabilities, probe score increased to %d\n`
- `init`
- `InputSize`
- `setupDataTransfers`
- `io-idle-timeout`
- `Automatic`
- `%06lu.%06u [0x%llx] %s::%s: Device supports ARP presence offload\n`
- `getExtendedFeaturePresenceOffload`
- `HiddenInterface`
- `%06lu.%06u [0x%llx][%s] %s::%s: provider %p\n`
- `12111112122212121111112111211211112222222222222222221`
- `getExtendedCapabilityMode`
- `%06lu.%06u [0x%llx] %s::%s:       • Checksum: %s\n`
- `%06lu.%06u [0x%llx] %s::%s:       • VLAN: %s\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: start waiting for BSD name\n`
- `site.AppleUSBNCMData`
- `%06lu.%06u [0x%llx] %s::%s: filter: %u status: %d\n`
- `site.AppleUSBNCM11Data`
- `transmitRecord`
- `%06lu.%06u [0x%llx] %s::%s: result %d for [0x%llx]\n`
- `%06lu.%06u [0x%llx] %s::%s: Device supports RSS receive offload\n`
- `%06lu.%06u [0x%llx] %s::%s:       • NS: %s\n`
- `%06lu.%06u [0x%llx] %s::%s: Device supports unknown presence offload type: 0x%02x\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: capabilities %#lx\n`
- `configureBSDInterfaceThreadCall`
- `setNTBFormat`
- `%06lu.%06u [0x%llx] %s::%s: CRC Mode: %u status: %d\n`
- `%06lu.%06u [0x%llx] %s::%s: Device supports unknown feature selector: 0x%02x\n`
- `i8@?0`
- `site.AppleUSBNCMControl`
- `setExtendedFeaturePresenceOffload`
- `%06lu.%06u [0x%llx] %s::%s:     - Feature Flags: 0x%02x\n`
- `idProduct`
- `AppleNCMVersion`
- `%06lu.%06u [0x%llx] %s::%s: Presence Offload descriptor too small (%u bytes)\n`
- `%06lu.%06u [0x%llx] %s::%s:   Wake Support: %s\n`
- `AppleUSBNCMDataPoller`
- `setDataAlternate`
- `disable`
- `Patching invalid HU NTB parameter wNdpOutAlignment %d\n`
- `%06lu.%06u [0x%llx] %s::%s: NTB format: %u status: %d\n`
- `121112111`
- `site.AppleUSBHostNCMRestrictedEthernetInterface`
- `%06lu.%06u [0x%llx][%s] %s::%s: result %d\n`
- `NetworkInterfaceFlags`
- `powerStateWillChangeTo`
- `ncm11-enabled`
- `Virtual Wire`
- `%06lu.%06u [0x%llx][%s] %s::%s: linkStatus %d\n`
- `ConfigMethod`
- `%06lu.%06u [0x%llx] %s::%s: NTB Input size: %u status: %d\n`
- `getExtendedFeatureMediumHandling`
- `%06lu.%06u [0x%llx] %s::%s:   Medium Handling: %s\n`
- `%06lu.%06u [0x%llx] %s::%s:   Offload Support: %s\n`
- `OutputSizeMax`
- `updateLinkStatus`
- `parseExtendedCapabilities`
- `stop`
- `USB`
- `getCRCMode`
- `setExtendedFeatureReceiveOffload`
- `Product Name`
- `%06lu.%06u [0x%llx][%s] %s::%s: upSpeed %d, downSpeed %d\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: unable to acquire ifnet pointer\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: Setting CarPlay properties.`
- `%06lu.%06u [0x%llx] %s::%s: _dataInterface %p\n`
- `1211111212221212111111211121121111222222222222222222122222222`
- `PrimaryRank`
- `%06lu.%06u [0x%llx] %s::%s:       • mDNS: %s\n`
- `%06lu.%06u [0x%llx] %s::%s:     - Magic Packet: %s\n`
- `start`
- `AppleNCMEnvironment`
- `site.AppleUSBNCM11Control`
- `%06lu.%06u [0x%llx] %s::%s: Wake Type: %u length: %u status: 0x%x\n`
- `dataWriteComplete`
- `%06lu.%06u [0x%llx][%s] %s::%s: result %#x\n`
- `%06lu.%06u [0x%llx] %s::%s: result %d\n`
- `BSD Name`
- `enable`
- `setExtendedFeatureMediumHandling`
- `Out Length`
- `In Frames`
- `12111112122212121111111112222111211211121`
- `getExtendedFeatureReceiveOffload`
- `%06lu.%06u [0x%llx] %s::%s: Device supports store bad packets receive offload\n`
- `%06lu.%06u [0x%llx] %s::%s: Device supports unknown receive offload type: 0x%02x\n`
- `%06lu.%06u [0x%llx] %s::%s:       • ARP: %s\n`
- `DatagramOutputCountMax`
- `%06lu.%06u [0x%llx][%s] %s::%s: terminating\n`
- `\"failed to lock netif, status = 0x%08x\\n\" @%s:%d`
