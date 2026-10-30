# `com.apple.iokit.IOMikeyBusFamily`

- Name: IOMikeyBusFamily
- Version: `1.0.0`
- UUID: `D81E34F0-1F28-3401-8DBC-AA0F6F9671D2`
- Source version: `109.40.3.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.iokit.IOAccessoryManager`](com.apple.iokit.IOAccessoryManager.md) 1.0.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 2.0.0, [`com.apple.iokit.IOPortFamily`](com.apple.iokit.IOPortFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0.0b1, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### IOMikeyBusEAInterface
- `CFBundleIdentifier`: `com.apple.iokit.IOMikeyBusFamily`
- `IOClass`: `IOMikeyBusEAInterface`
- `IOMikeyBusMatchFunctionGroupType`: `5`
- `IOPersonalityPublisher`: `com.apple.iokit.IOMikeyBusFamily`
- `IOProviderClass`: `IOMikeyBusFunctionGroup`

### IOMikeyBusHIDDevice
- `CFBundleIdentifier`: `com.apple.iokit.IOMikeyBusFamily`
- `HIDDefaultBehavior`: ``
- `IOClass`: `IOMikeyBusHIDDevice`
- `IOMikeyBusMatchFunctionGroupType`: `6`
- `IOPersonalityPublisher`: `com.apple.iokit.IOMikeyBusFamily`
- `IOProviderClass`: `IOMikeyBusFunctionGroup`


## C++ classes (14) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOMikeyBusAudioDevice` | 0xf8 | IOService → IORegistryEntry |
| `IOMikeyBusBulkPipe` | 0xa8 | IOEventSource |
| `IOMikeyBusBulkPipeUserClient` | 0x100 | IOUserClient → IOService → IORegistryEntry |
| `IOMikeyBusController` | 0x3d8 | IOService → IORegistryEntry |
| `IOMikeyBusDevice` | 0x100 | IOService → IORegistryEntry |
| `IOMikeyBusDeviceUserClient` | 0x118 | IOMikeyBusBulkPipeUserClient → IOUserClient → IOService → IORegistryEntry |
| `IOMikeyBusDockPort` | 0x130 | IOMikeyBusPort → IOService → IORegistryEntry |
| `IOMikeyBusEAInterface` | 0xb0 | IOAccessoryEAInterface → IOService → IORegistryEntry |
| `IOMikeyBusFunctionGroup` | 0x98 | IOService → IORegistryEntry |
| `IOMikeyBusFunctionGroupUserClient` | 0x108 | IOMikeyBusBulkPipeUserClient → IOUserClient → IOService → IORegistryEntry |
| `IOMikeyBusHIDDevice` | 0xf0 | IOHIDDevice → IOService → IORegistryEntry |
| `IOMikeyBusPort` | 0xf0 | IOService → IORegistryEntry |
| `IOMikeyBusTrafficChannel` | 0x30 |  |
| `OSValueObject<IOMikeyBusBulkPipeUserClient::AsyncParams>` | 0x18 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1800)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001d58 off=0x00a00ac0-0x00a02818 addr=0xfffffe0007a04ac0-0xfffffe0007a06818 r--/r--   __TEXT            
	sz=0x0000100a off=0x00a01228-0x00a02232 addr=0xfffffe0007a05228-0xfffffe0007a06232               __TEXT.__cstring          (CstringLiterals)
	sz=0x000003de off=0x00a02232-0x00a02610 addr=0xfffffe0007a06232-0xfffffe0007a06610               __TEXT.__os_log           
	sz=0x00000208 off=0x00a02610-0x00a02818 addr=0xfffffe0007a06610-0xfffffe0007a06818               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x0001b258 off=0x031fe9d0-0x03219c28 addr=0xfffffe000a2029d0-0xfffffe000a21dc28 r-x/r-x   __TEXT_EXEC       
	sz=0x0001ad68 off=0x031fe9d0-0x03219738 addr=0xfffffe000a2029d0-0xfffffe000a21d738          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000004f0 off=0x03219738-0x03219c28 addr=0xfffffe000a21d738-0xfffffe000a21dc28          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000638 off=0x049f3298-0x049f38d0 addr=0xfffffe000b9f7298-0xfffffe000b9f78d0 rw-/rw-   __DATA            
	sz=0x00000188 off=0x049f3298-0x049f3420 addr=0xfffffe000b9f7298-0xfffffe000b9f7420               __DATA.__data             
	sz=0x00000488 off=0x00000000-0x00000488 addr=0xfffffe000b9f7420-0xfffffe000b9f78a8               __DATA.__common           (Zerofill)
	sz=0x00000028 off=0x00000000-0x00000028 addr=0xfffffe000b9f78a8-0xfffffe000b9f78d0               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00005d30 off=0x0139df98-0x013a3cc8 addr=0xfffffe00083a1f98-0xfffffe00083a7cc8 rw-/rw-   __DATA_CONST      
	sz=0x00000070 off=0x0139df98-0x0139e008 addr=0xfffffe00083a1f98-0xfffffe00083a2008         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000068 off=0x0139e008-0x0139e070 addr=0xfffffe00083a2008-0xfffffe00083a2070         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000050f0 off=0x0139e070-0x013a3160 addr=0xfffffe00083a2070-0xfffffe00083a7160         __DATA_CONST.__const            
	sz=0x00000540 off=0x013a3160-0x013a36a0 addr=0xfffffe00083a7160-0xfffffe00083a76a0         __DATA_CONST.__kalloc_type      
	sz=0x000002d0 off=0x013a36a0-0x013a3970 addr=0xfffffe00083a76a0-0xfffffe00083a7970         __DATA_CONST.__kalloc_var       
	sz=0x00000278 off=0x013a3970-0x013a3be8 addr=0xfffffe00083a7970-0xfffffe00083a7be8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000d8 off=0x013a3be8-0x013a3cc0 addr=0xfffffe00083a7be8-0xfffffe00083a7cc0         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x013a3cc0-0x013a3cc8 addr=0xfffffe00083a7cc0-0xfffffe00083a7cc8         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 185 at 0x04af357c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     D81E34F0-1F28-3401-8DBC-AA0F6F9671D2
008: LC_SOURCE_VERSION           109.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac1518 size=0x398
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOMikeyBusFamily`
- `CFBundleIdentifier`: `com.apple.iokit.IOMikeyBusFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOMikeyBusFamily`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersion`: `1.0.0`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2024 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOMikeyBusFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895310144`
- `_PrelinkExecutableRelativePath`: `IOMikeyBusFamily`
- `_PrelinkExecutableSize`: `144152`
- `_PrelinkExecutableSourceAddr`: `-2198895310144`
- `_PrelinkKmodInfo`: `-2198828256616`

## Strings (186) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `ConfigurationNumber`
- `IOMikeyBusPort`
- `TCA`
- `IOMikeyBusEAInterface`
- `%s: traffic channel assignment error: %s\n`
- `FirmwareRevision`
- `CreateStringFromUTF16LE`
- `Reset`
- `IOAccessoryAccessorySerialNumber`
- `IOMikeyBusFunctionGroupUserClient`
- `%s: received unexpected segment number %u (window %u-%u)\n`
- `%s: unknown packet received command %02x length %lu\n`
- `InterfaceChipProductID`
- `mb-enum-timeout-ms`
- `12111112122212121112121212222211112111`
- `121111121222121211111122221111111111111111111111111111111111111111111111111111111111111111112221222222222222222222222211111`
- `IsLowPowerState`
- `MikeyBusVersion`
- `IOMikeyBusDevice`
- `site.IOMikeyBusDevice`
- `mb-soup-disconnect`
- `%s: link lost for %llu ms\n`
- `site.IOMikeyBusBulkPipe`
- `IOMikeyBusDockPort`
- `Resetting accessory power`
- `IOMikeyBusAudioDevice`
- `terminate`
- `8b10b code`
- `device name`
- `%s: could not start %s on %s\n`
- `MikeyBus VID %u`
- `ConfigurationSubclass`
- `FunctionGroupProperty%02x`
- `Disabling accessory power!`
- `IOMikeyBusMatchDeviceSubclass`
- `VendorName`
- `VoltageClass`
- `%s: unexpected device command %#x length %llu\n`
- `Bulk Channel`
- `1111111112`
- `PacketErrorCount`
- `SODP`
- `%s: link lock took %llu ms\n`
- `Suspend`
- `_receiveLinkStatusGated`
- `IOMikeyBusMatchVendorID`
- `%s: failed to get device info: %s\n`
- `TrafficErrorCount`
- `IOMikeyBusBulkPipe`
- `MikeyBus PID %u`
- `BroadcastPacket`
- `MikeyBus`
- `IOMikeyBusMatchDeviceAnyConfiguration`
- `ConfigurationClass`
- `transport type`
- `site.IOMikeyBusFunctionGroupUserClient`
- `IOMikeyBusHIDDevice`
- `IOMikeyBusMatchDeviceClass`
- `Lightning Headset`
- `site.IOMikeyBusFunctionGroup`
- `Packets`
- `CRC`
- `Traffic Channel`
- `MikeyBus.%u.%u.%u.%llu`
- `IOMikeyBusTrafficChannel`
- `%s: Warning: packetLen of %llu, using value of 0 or numProperty \n`
- `%s: Warning: unexpected packetLen of %llu, using value of 0 to set property length in setProperty(...) \n`
- `%s: Warning: packetLen of %llu is too large, using UINT32_MAX to set property length in setProperty(...) \n`
- `BulkErrorCount`
- `DeviceErrorCount`
- `1211111212221212111111`
- `InterfaceChipSerialNumber`
- `BCC`
- `IOAccessoryAccessoryModelNumber`
- `site.IOMikeyBusAudioDevice`
- `InterfaceChipVendorID`
- `ModelNumber`
- `12111112122212121112111122112122`
- `RetainBusCount`
- `crc error`
- `%s: received RST_SEG packet from device\n`
- `HardwareRevision`
- `%X`
- `site.IOMikeyBusDesignatorPacketSetFunctionGroupPropertyInfo.UInt8`
- `121111121222121211121212122222`
- `IOAccessoryAccessoryManufacturer`
- `121111121222121211211122211111`
- `stop`
- `IOMikeyBusMatchFunctionGroupID`
- `IOMikeyBusDeviceUserClient`
- `mb-linkup-timeout-ms`
- `InfoState`
- `IOMikeyBusMatchFunctionGroupType`
- `mb-force-port-toggle`
- `12111112122212121111111111111111211`
- `site.T`
- `%s: bad packet length %llu\n`
- `SOUPErrorCount`
- `LinkSOUPLost`
- `121112111111122111111`
- `start`
- `IOMikeyBusMatchDeviceConfigurationNumber`
- `Configurations`
- `FunctionGroupType`
- `site.IOMikeyBusTrafficChannel`
- `_receivePacketGated`
- `site.IOMikeyBusHIDReportCommand.UInt8`
- `InterfaceChipRevision`
- `IOAccessoryAccessoryName`
- `12111112122212121111111111111111`
- `VendorID`
- `IOMikeyBusDevice %s:%s entry\n`
- `length invalid`
- `site.IOMikeyBusEAInterface`
- `_linkValidationTimeoutHandler`
- `%s: truncating report from %lu to %lu bytes\n`
- `%s: Warning: packetLen of %llu is too large, using UINT32_MAX as numProperty \n`
- `extraneous data`
- `_audioDeviceGetChannelAssignmentsGated`
- `site.IOMikeyBusController`
- `_portStatusChangedGated`
- `Authenticated`
- `site.PacketCompletion`
- `device UID`
- `ProductName`
- `site.IOMikeyBusPort`
- `length 8b10b error`
- `IOMikeyBusBulkPipeUserClient`
- `OSValueObject<IOMikeyBusBulkPipeUserClient::AsyncParams>`
- `\"%s: invalid immediate packet\" @%s:%d`
- `_audioDeviceSetDeviceFormatGated`
- `IOUserClientClass`
- `IOMikeyBusDevice %s - stringLength too large, returning ...\n`
- `ConnectStatus`
- `121`
- `1211111212221212111111111112222`
- `site.IOMikeyBusBulkPayloadPacket.UInt8`
- `SOS`
- `site.IOMikeyBusDeviceUserClient`
- `site.io_user_reference_t`
- `NeedPowerUpOnRetain`
- `IOMikeyBusController.cpp`
- `121222`
- `DeviceAddress`
- `StartError`
- `IOMikeyBusFunctionGroup`
- `1211111212221212112`
- `BCAST Header`
- `%s: received unexpected RetReport\n`
- `ProductID`
- `Lightning Adapter`
- `site.IOMikeyBusHIDDevice`
- `IOMikeyBusMatchProductID`
- `SerialNumber`
- `FunctionGroupID`
- `device manufacturer`
- `8b10b disparity`
- `112222111`
- `ControllerEnabled`
- `_enumerationTimeoutAction`
- `site.IOMikeyBusDockPort`
- `121111121222121211111111111111111`
- `site.IOMikeyBusBulkPipeUserClient`
- `1`
- `IOMikeyBusController`
- `site.PendingBulkSendPacket`

**[__TEXT.__os_log]**

- `%s:%s:%d kIOReturnNotAttached direction=0x%x`
- `%s:%s:%d kIOReturnNoSpace direction=0x%x`
- `%s:%s:%d kIOReturnError direction=0x%x`
- `%s:%s failed to create _retransmitTimer`
- `%s:%s failed to create _linkValidationTimeout`
- `%s:%s:%d kIOReturnDeviceError direction=0x%x`
- `%s:%s Toggle Port and re-enumerate new device`
- `%s:%s Error : Enumeraton Timeout. Toggle port to recover`
- `%s:%s CreateRootPort() failed`
- `%s:%s _rootPort->start() failed`
- `%s:%s connected=%d wakeFromSleep=%d _ControllerEnabled=%d _suspend=%d _pendingDisconnect=%d`
- `%s:%s No Linkup observed in %d ms. Remove port power`
- `%s:%s Warning: Dropped ACK detected. Received segn=%d TXQ segn=%d flags=0x%x `
- `%s:%s Warning: SendQ - ACK mismatch. Received segn=%d TXQ segn=%d flags=0x%x`
- `%s:%s:%d kIOReturnNoChannels direction=0x%x`
- `%s:%s handleStart() failed`
- `%s:%s Link Locked = %d`
- `%s:%s Error : No device connected. Do not toggle port.`
- `%s:%s failed to create _completionTimeout`
- `%s:%s _rootPort->attach() failed`
