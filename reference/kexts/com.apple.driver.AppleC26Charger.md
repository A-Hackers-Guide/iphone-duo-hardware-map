# `com.apple.driver.AppleC26Charger`

- Name: AppleC26Charger
- Version: `1.0.1`
- UUID: `0E2EB569-5DAA-34C8-9DCB-7ACA9607939A`
- Source version: `155.40.5.0.0`
- Depends on: [`com.apple.driver.AppleARMPMU`](com.apple.driver.AppleARMPMU.md) 1.0.0, [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleEmbeddedTempSensor`](com.apple.driver.AppleEmbeddedTempSensor.md) 1.0.0, [`com.apple.iokit.IOAccessoryManager`](com.apple.iokit.IOAccessoryManager.md) 1.0.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.4, [`com.apple.iokit.IOPortFamily`](com.apple.iokit.IOPortFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (8) [KC]

### AppleB237DockInfo
- `CFBundleIdentifier`: `com.apple.driver.AppleC26Charger`
- `IOClass`: `AppleB237DockInfo`
- `IOPersonalityPublisher`: `com.apple.driver.AppleC26Charger`
- `IOProviderClass`: `AppleC26DeviceStream`
- `ProtocolType`: `0`
- `StreamType`: `4`

### AppleC26AuthProtocol
- `CFBundleIdentifier`: `com.apple.driver.AppleC26Charger`
- `IOAccessoryDeviceDynamicPort`: `True`
- `IOClass`: `AppleC26AuthProtocol`
- `IOMatchCategory`: `AppleC26AuthProtocol`
- `IOPersonalityPublisher`: `com.apple.driver.AppleC26Charger`
- `IOProviderClass`: `AppleC26DeviceStream`
- `ProtocolType`: `1`
- `StreamType`: `1`

### AppleC26AuthProtocolWatch
- `CFBundleIdentifier`: `com.apple.driver.AppleC26Charger`
- `IOAccessoryDeviceDynamicPort`: `True`
- `IOClass`: `AppleC26AuthProtocolWatch`
- `IOMatchCategory`: `AppleC26AuthProtocolWatch`
- `IOPersonalityPublisher`: `com.apple.driver.AppleC26Charger`
- `IOProviderClass`: `AppleC26DeviceStream`
- `ProtocolType`: `1`
- `StreamType`: `11`

### AppleC26ConfigStream
- `CFBundleIdentifier`: `com.apple.driver.AppleC26Charger`
- `IOClass`: `AppleC26ConfigStream`
- `IOMatchCategory`: `AppleC26ConfigStream`
- `IOPersonalityPublisher`: `com.apple.driver.AppleC26Charger`
- `IOProviderClass`: `AppleC26DeviceStream`
- `ProtocolType`: `1`
- `StreamType`: `0`

### AppleC26EA
- `CFBundleIdentifier`: `com.apple.driver.AppleC26Charger`
- `IOClass`: `AppleC26EA`
- `IOMatchCategory`: `AppleC26EA`
- `IOPersonalityPublisher`: `com.apple.driver.AppleC26Charger`
- `IOProviderClass`: `AppleC26DeviceStream`
- `ProtocolType`: `0`
- `StreamType`: `5`

### AppleC26HID
- `CFBundleIdentifier`: `com.apple.driver.AppleC26Charger`
- `IOClass`: `AppleC26HID`
- `IOMatchCategory`: `AppleC26HID`
- `IOPersonalityPublisher`: `com.apple.driver.AppleC26Charger`
- `IOProviderClass`: `AppleC26DeviceStream`
- `ProtocolType`: `1`
- `StreamType`: `3`

### AppleC26HIDWatch
- `CFBundleIdentifier`: `com.apple.driver.AppleC26Charger`
- `IOClass`: `AppleC26HIDWatch`
- `IOMatchCategory`: `AppleC26HIDWatch`
- `IOPersonalityPublisher`: `com.apple.driver.AppleC26Charger`
- `IOProviderClass`: `AppleC26DeviceStream`
- `ProtocolType`: `0`
- `StreamType`: `10`

### AppleQiAuthProtocol
- `CFBundleIdentifier`: `com.apple.driver.AppleC26Charger`
- `IOAccessoryDeviceDynamicPort`: `True`
- `IOClass`: `AppleQiAuthProtocol`
- `IOMatchCategory`: `AppleQiAuthProtocol`
- `IOPersonalityPublisher`: `com.apple.driver.AppleC26Charger`
- `IOProviderClass`: `AppleC26DeviceStream`
- `ProtocolType`: `2`
- `StreamType`: `1`


## C++ classes (23) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleAirPowerCharger` | 0x168 | AppleC26Charger → IOService → IORegistryEntry |
| `AppleB237DockInfo` | 0xb8 | AppleC26DockInfo → IOService → IORegistryEntry |
| `AppleC26AuthProtocol` | 0xb8 | IOAccessoryAuthProtocolInterface → IOAccessoryPort → IOAccessoryTransport → IOService → IORegistryEntry |
| `AppleC26AuthProtocolWatch` | 0xb8 | IOAccessoryAuthProtocolInterface → IOAccessoryPort → IOAccessoryTransport → IOService → IORegistryEntry |
| `AppleC26Charger` | 0x138 | IOService → IORegistryEntry |
| `AppleC26ChargerUserClient` | 0xf0 | IOUserClient → IOService → IORegistryEntry |
| `AppleC26ConfigStream` | 0x558 | IOAccessoryConfigStreamInterface → IOService → IORegistryEntry |
| `AppleC26DataStream` | 0x78 | IOEventSource |
| `AppleC26DeviceStream` | 0x98 | IOService → IORegistryEntry |
| `AppleC26DockInfo` | 0x88 | IOService → IORegistryEntry |
| `AppleC26EA` | 0xf0 | IOAccessoryEAInterface → IOService → IORegistryEntry |
| `AppleC26FFBDataStream` | 0x78 | AppleC26DataStream → IOEventSource |
| `AppleC26FFBPacket` | 0x80 | AppleC26Packet |
| `AppleC26HID` | 0x120 | IOAccessoryHIDDeviceInterface → IOService → IORegistryEntry |
| `AppleC26HIDWatch` | 0x120 | IOAccessoryHIDDeviceInterface → IOService → IORegistryEntry |
| `AppleC26Packet` | 0x68 |  |
| `AppleC26Stream` | 0x28 |  |
| `AppleC26TelegramStream` | 0xa8 | AppleC26DataStream → IOEventSource |
| `AppleCallistoPacket` | 0x78 | AppleC26Packet |
| `AppleCallistoTelegramStream` | 0xe0 | AppleC26TelegramStream → AppleC26DataStream → IOEventSource |
| `AppleQiAuthProtocol` | 0xb8 | IOAccessoryAuthProtocolInterface → IOAccessoryPort → IOAccessoryTransport → IOService → IORegistryEntry |
| `AppleWirelessPowerPacket` | 0x78 | AppleC26Packet |
| `AppleWirelessPowerTelegramStream` | 0xc8 | AppleC26TelegramStream → AppleC26DataStream → IOEventSource |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00003018 off=0x003b90b0-0x003bc0c8 addr=0xfffffe00073bd0b0-0xfffffe00073c00c8 r--/r--   __TEXT            
	sz=0x000027a6 off=0x003b9778-0x003bbf1e addr=0xfffffe00073bd778-0xfffffe00073bff1e               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000157 off=0x003bbf20-0x003bc077 addr=0xfffffe00073bff20-0xfffffe00073c0077               __TEXT.__const            
	sz=0x00000051 off=0x003bc077-0x003bc0c8 addr=0xfffffe00073c0077-0xfffffe00073c00c8               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00013638 off=0x01a11460-0x01a24a98 addr=0xfffffe0008a15460-0xfffffe0008a28a98 r-x/r-x   __TEXT_EXEC       
	sz=0x000131e8 off=0x01a11460-0x01a24648 addr=0xfffffe0008a15460-0xfffffe0008a28648          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000450 off=0x01a24648-0x01a24a98 addr=0xfffffe0008a28648-0xfffffe0008a28a98          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000488 off=0x04934160-0x049345e8 addr=0xfffffe000b938160-0xfffffe000b9385e8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04934160-0x04934228 addr=0xfffffe000b938160-0xfffffe000b938228               __DATA.__data             
	sz=0x000003c0 off=0x00000000-0x000003c0 addr=0xfffffe000b938228-0xfffffe000b9385e8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00006b50 off=0x00ffb4d0-0x01002020 addr=0xfffffe0007fff4d0-0xfffffe0008006020 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x00ffb4d0-0x00ffb4e8 addr=0xfffffe0007fff4d0-0xfffffe0007fff4e8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x00ffb4e8-0x00ffb500 addr=0xfffffe0007fff4e8-0xfffffe0007fff500         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00006250 off=0x00ffb500-0x01001750 addr=0xfffffe0007fff500-0xfffffe0008005750         __DATA_CONST.__const            
	sz=0x000005c0 off=0x01001750-0x01001d10 addr=0xfffffe0008005750-0xfffffe0008005d10         __DATA_CONST.__kalloc_type      
	sz=0x00000228 off=0x01001d10-0x01001f38 addr=0xfffffe0008005d10-0xfffffe0008005f38         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000e0 off=0x01001f38-0x01002018 addr=0xfffffe0008005f38-0xfffffe0008006018         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x01002018-0x01002020 addr=0xfffffe0008006018-0xfffffe0008006020         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 166 at 0x04ad41f4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     0E2EB569-5DAA-34C8-9DCB-7ACA9607939A
008: LC_SOURCE_VERSION           155.40.5.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9af80 size=0x2f0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleC26Charger`
- `CFBundleIdentifier`: `com.apple.driver.AppleC26Charger`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleC26Charger`
- `CFBundleNumericVersion`: `16875520`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.1`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.1`
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
- `OSBundleCompatibleVersion`: `1.0.1`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleC26Charger.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901894992`
- `_PrelinkExecutableRelativePath`: `AppleC26Charger`
- `_PrelinkExecutableSize`: `120360`
- `_PrelinkExecutableSourceAddr`: `-2198901894992`
- `_PrelinkKmodInfo`: `-2198829039264`

## Strings (270) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `completeSendData`
- `%s: Error on final packet: checksumbyte=%02x checksum=%02x (should be 0x00), fragmentflags=%02x (should be 0x3 or 0x2) in stream #%02x\n`
- `%s: Attempted to tear down comms while disconnected\n`
- `%s: Address Rolled %0x %0x %0x %0x %0x %0x --> %0x %0x %0x %0x %0x %0x\n`
- `%s failed to create OSData to hold new address!\n`
- `DeviceInfoInterfaceVendorID`
- `%s: New MPP Devicestream (1) created\n`
- `virtual IOReturn AppleC26HIDWatch::sendOutData(const void *, IOByteCount)`
- `%s: device stream init or attach failed; str:%d typ:%d prot:%d\n`
- `declareStreamsSupport`
- `Resolvable Address`
- `%s: AuthProtocol attached to dock\n`
- `AppleC26ConfigStream: could not open ConfigStream\n`
- `%s: Request to restore stream type: %d, protocol: %d\n`
- `kC26UserClientMethodRemovePresentAirPowerDevice: (%p) %s\n`
- `12221`
- `site.AppleQiAuthProtocol`
- `site.AppleB237DockInfo`
- `site.AppleC26FFBPacket`
- `AppleCallistoTelegramStream`
- `%s: QiAuthProtocol registered service\n`
- `%s: ***** QiAuthProtocol SENDING AUTH DATA ***** (len=%d bytes)\n`
- `AppleC26Packet`
- `%s:%s: error sending data: %s\n`
- `i8@?0`
- `AppleC26EA`
- `site.AppleC26HIDWatch`
- `%s: Processing RetDevInfo response\n`
- `%s: data queue full\n`
- `dock-a`
- `%s: AppleC26AuthProtocol super::start() failed\n`
- `%s: AuthProtocolWatch registered service\n`
- `%s: received AuthProtocolWatch telegram:%s\n`
- `%s: could not open QiAuthProtocol stream\n`
- `%s: copyDeviceString aborted. resetting comms.\n`
- `Build Packet: ilen %lu, nb %d, len %d, byte[0] %02x`
- `121111121222121211111111111111`
- `site.AppleC26ConfigStream`
- `%s: receivePacketFromController() called with NULL packet or wrong AppleC26Packet subclass (%p %p)\n`
- `%s: resetting comms\n`
- `site.AppleC26EA`
- `%s: detected cable-a\n`
- `AppleC26AuthProtocol`
- `site.AppleC26AuthProtocol`
- `%s: QiAuthProtocol stream created successfully\n`
- `%s: AppleC26AuthProtocolWatch super::start() failed\n`
- `AppleQiAuthProtocol`
- `chg-therm-profile`
- `%s: AuthProtocolWatch attached to dock\n`
- `%s: could not start device stream, detached; str:%d typ:%d prot:%d\n`
- `AppleC26FFBDataStream`
- `AppleC26TelegramStream`
- `sendData`
- `121112111122111211222`
- `%s: received unexpected non-first fragment (flags=%02x) in stream #%02x\n`
- `%s: detach complete\n`
- `restoreDeviceStream`
- `%s: stop, detachFromParent %s\n`
- `122222222222222`
- `DeviceInfoInterfaceSerialNumber`
- `%s: received AuthProtocol telegram:%s\n`
- `%s: AuthProtocolWatch stream created\n`
- `site.AppleC26Packet`
- `%s: received unexpected start marker in stream #%02x\n`
- `str:%d; rx packet incomplete (%lu / %d bytes)\n`
- `DeviceInfoInterfaceVersion`
- `%s: error sending data: %s\n`
- `%s: Process not allowed to set properties\n`
- `%s: AppleQiAuthProtocol provider is not AppleC26DeviceStream\n`
- `%s: could not start device configuration: %s\n`
- `%s: Sending GetConfig command to enumerate streams\n`
- `AppleC26HIDWatch`
- `site.AppleWirelessPowerPacket`
- `%s: Processing RetConfig response - payloadDataLen=%zu\n`
- `%s:%s:%d _streamsSupported(%d), typeMask(%d)\n`
- `%s: Properties is not a dictionary\n`
- `cable-b`
- `%s: QiAuthProtocol attached to dock\n`
- `site.AppleC26Stream`
- `%s: error sending comms control telegram: %s\n`
- `updatePresentDeviceAddress`
- `%s: AppleC26AuthProtocolWatch::sendData called with %d bytes\n`
- `%s: serialNumber(%s) 4E code(0x%x) 7E code(0x%llx) \n`
- `%s: AppleC26AuthProtocolWatch is not AppleC26DeviceStream\n`
- `%s: AppleC26AuthProtocolWatch::start() completed successfully\n`
- `AppleQiAuthProtocol::stop()\n`
- `Error Received: foreign object detected on charger\n`
- `trySendingTelegramGated(): no telegram to send! (stream=%d queuecount=%d)\n`
- `trySendingTelegramGated from completeSendTelegramGated\n`
- `str:%d; rx packet {s:%d e:%d}; rx %d bytes [%lu/%d]; first chunk; wait for end bit\n`
- `%s: no device with old address found\n`
- `12111112122212121111112`
- `AppleC26AuthProtocolWatch`
- `%s: could not open dock info stream\n`
- `site.AppleC26TelegramStream`
- `restoreDeviceStream: could not start device stream, detached\n`
- `root`
- `%s: could not open iAUP stream\n`
- `%s: Attempted to reset comms while disconnected\n`
- `%s: Config stream enabled, sending GetDevInfo command\n`
- `%s: Failed to find device stream with stream type: %d, protocol: %d\n`
- `%s: passed NULL device\n`
- `1211111212221212112`
- `site.AppleC26AuthProtocolWatch`
- `%s: sending AuthProtocolWatch telegram:%s\n`
- `%s: copyStreamProperty aborted. Resetting comms\n`
- `%s: detected cable-d\n`
- `%s: AuthProtocol stream enabled\n`
- `%s: AppleC26AuthProtocol::sendData called with %d bytes\n`
- `DeviceInfoInterfaceRevision`
- `DeviceInfoInterfaceProductName`
- `%s: unable to allocate OSData to buffer device\n`
- `121111121222121211111111121222`
- `site.AppleC26DockInfo`
- `%s: RetConfig: configVersion=0x%04x, numStreams=%zu\n`
- `121111121222121212212211122212211111212121112`
- `%s: completeSendTelegramGated() called with ACK packet of the wrong AppleC26Packet subclass (%p %p)\n`
- `%s: ===== AppleQiAuthProtocol::start() SUCCESS =====\n`
- `site.AppleC26DataStream`
- `ProtocolType`
- `cable-e`
- `%s: could not open AuthProtocol stream\n`
- `AppleC26HIDWatch::%s: received HID telegram:%s\n`
- `AppleC26ConfigStream`
- `1222222222222222`
- `AppleWirelessPowerPacket`
- `Cloaked`
- `%s: unexpected packet command %02x payload %lu bytes\n`
- `com.apple.private.appleairpowercharger.set-property`
- `unexpected OSObject type found in present device list\n`
- `%s: received iAUP telegram:%s\n`
- `site.AppleCallistoPacket`
- `Received telegram complete\n`
- `site.AppleC26Charger`
- `AppleC26DeviceStream`
- `%s: received unexpected data before start byte (%02x)\n`
- `%s: ***** QiAuthProtocol RECEIVED AUTH DATA ***** (len=%lu bytes)\n`
- `%s: failed to fetch address for device\n`
- `StreamNumber`
- `AppleC26HID`
- `%s: could not open HID stream\n`
- `%s: QiAuthProtocol auth data sent successfully\n`
- `site.AppleAirPowerCharger`
- `updatePresentDeviceFromPresentDevPacket`
- `%s: sending iAUP telegram:%s\n`
- `%s: received HID telegram:%s\n`
- `AppleB237DockInfo`
- `%s:%s:%d Duplicate Stream Enumeration`
- `Address`
- `kC26UserClientMethodPublishPresentAirPowerDevice: (%p) %s\n`
- `121111121222121211212111221112112112`
- `%s: received final fragment with only %d of expected %lu bytes in stream #%02x\n`
- `%s: cloaked: %d, reason: %d\n`
- `cable-a`
- `c26-auth-loopback`
- `str:%d; rx packet {s:%d e:%d}; rx %d bytes [%lu/%d]\n`
- `%s: createDeviceStream: streamNumber=%d, streamType=%d, protocolType=%d, deferStart=%d\n`
- `createDeviceStream`
- `Error Received: device needs to be repositioned on charger\n`
- `%s: detected dock-a\n`
- `%s::%s:%s:%s call registerService\n`
- `AppleC26Stream`
- `publishCloakedState`
- `%s: setting thermal profile: %d\n`
- `Present AirPower Devices`
- `AppleC26ChargerUserClient`
- `%s: AppleC26AuthProtocol got device stream (number=%d, type=%d)\n`
- `%s: AuthProtocol stream created\n`
- `%s: could not open AuthProtocolWatch stream\n`
- `%s: device stream started successfully; str:%d typ:%d prot:%d deferStart:%d\n`
- `121112111122111`
- `trySendingTelegramGated from sendDataGated\n`
- `%s::%s:AppleWirelessPowerTelegramStream::sendData, Build wireless packet: startbit %d endbit %d, streamPosition %d payloadRemaining %lu payloadDataLen %lu toCopy %lu\n`
- `AppleC26Charger`
- `%s: Starting config stream setup\n`
- `Error Received: charger has insufficient power available\n`
- `%s::%s:stream #%d is not a telegram stream\n`
- `DeviceInfoInterfaceFWRev`
- `%s: Received config data - cmdID=0x%02x, dataLen=%zu\n`
- `site.AppleC26HID`
- `AppleC26FFBPacket`
- `12111112122212121`
- `%s: AppleQiAuthProtocol got device stream (number=%d, type=%d, protocol=%d)\n`
- `%s: Failed to create an iterator\n`
- `%s: received unexpected data %02x in stream #%02x\n`
- `site.AppleCallistoTelegramStream`
- `%s::%s:AppleWirelessPowerTelegramStream::sendData pdl %lu, pd %lld\n`
- `site.AppleWirelessPowerTelegramStream`
- `%s: detected cable-c\n`
- `%s: AuthProtocolWatch stream enabled\n`
- `%s: sending HID telegram [len %d]:%s\n`
- `AppleC26HIDWatch::%s: sending HID telegram:%s\n`
- `AppleCallistoPacket`
- `AppleWirelessPowerTelegramStream`
- `1211121111221112112221122`
- `121111121222121212212211122212211111212`
- `%s: beginning attach\n`
- `tearDownCommsStreamType`
- `%s: AppleC26AuthProtocol is not AppleC26DeviceStream\n`
- `%s: AppleC26AuthProtocol::start() completed successfully\n`
- `%s: QiAuthProtocol stream enabled\n`
- `str:%d; rx packet {s:%d e:%d}; rx %d bytes [%lu/%d]; second chunk\n`
- `DeviceInfoInterfaceVendorName`
- `%s: New Qipp Devicestream (%lu) created\n`
- `121111121222121211211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111122112`
- `%s: received bad checksum byte %02x (checksum %02x) in stream #%02x\n`
- `completeTelegramGated`
- `StreamType`
- `%X`
- `receiveConfigData`
- ` %02x`
- `%s: sending ConfigStream telegram:%s\n`
- `DeviceInfoInterfaceHWRev`
- `%s: Config stream setup complete, registered service\n`
- `AppleAirPowerCharger`
- `New C26 Devicestream (streamNumber=%lu, streamType=%d)\n`
- `site.AppleC26FFBDataStream`
- `%s: sending AuthProtocol telegram:%s\n`
- `AppleWirelessPowerTelegramStream:receivePacketFromController mp(%d) el(%d) il(%d) rs(%d) pdl(%d) rel(%d) rl(%d) rml(%d)\n`
- `dock`
- `%s: unknown product serialNumber(%s) 4E code(0x%x) 7E code(0x%llx) \n`
- `AppleC26DataStream`
- `%s: comms reset request received\n`
- `unexpected packet command %02x payload %lu bytes\n`
- `%s: received unexpected start marker. Previous telegram at %d/%d bytes\n`
- `%s: detected cable (generic)\n`
- `cable`
- `%s: AppleC26AuthProtocolWatch got device stream (number=%d, type=%d)\n`
- `1211121111221112112221121112`
- `str:%d; rx packet complete (%lu bytes); send to client\n`
- `AppleC26DockInfo`
- `%s:%s calling completeAction for streamNumber(%d)\n`
- `DeviceInfoInterfaceModelNumber`
- `%s: Request to terminate stream type: %d, protocol: %d\n`
- `ThermalProfile`
- `AppleC26AuthProtocolWatch::start()\n`
- `void AppleC26HIDWatch::_receiveData(AppleC26DataStream *, const void *, size_t)`
- `%s: %p, group=%d, device=%d\n`
- `site.AppleC26ChargerUserClient`
- `%s: start, attachToParent %s\n`
- `%s: detected cable-b\n`
- `cable-d`
- `%s:%s call registerService\n`
- `%02x `
- `%s: detected cable-e\n`
- `12111112122212121111212`
- `Telegram stream received unexpected packet: ACK=%d, NACK=%d, noResponseComing=%d, error=%d\n`
- `CloakReason`
- `%s: invalid zero-length data\n`
- `%s: resolvable addres is not valid data\n`
- `%s: comms control stream torn down\n`
- `Unexpected Error Received: 0x%X\n`
- `%s: detected dock (generic)\n`
- `%s: detected 7E cable-e\n`
- `%s: Failed to find device stream for stream type: %d, protocol: %d\n`
- `site.AppleC26DeviceStream`
- `%s: start, cannot attachToParent, no dock\n`
- `%s: AuthProtocol registered service\n`
- `%s: AppleC26AuthProtocol::start() called\n`
- `%s: calling _c26Stream->sendData\n`
- `%s: received ConfigStream telegram:%s\n`
- `cable-c`
- `%s: AppleQiAuthProtocol super::start() failed\n`
- `start`
- `%s:ConfigStream created\n`
- `chg-c26-debug`
- `DeviceInfoInterfaceProductID`
- `1222222222222`

**[__TEXT.__os_log]**

- `%s: sending QiAuthProtocol telegram:%s\n`
- `%s: received QiAuthProtocol telegram:%s\n`
