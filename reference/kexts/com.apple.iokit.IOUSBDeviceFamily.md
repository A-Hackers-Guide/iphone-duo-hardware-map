# `com.apple.iokit.IOUSBDeviceFamily`

- Name: IOUSBDeviceFamily
- Version: `2.0.0`
- UUID: `E082D6D3-8C6F-3D44-B5C6-E78228ABAD25`
- Source version: `896.40.5.0.0`
- Depends on: [`com.apple.driver.usb.AppleUSBCommon`](com.apple.driver.usb.AppleUSBCommon.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 20.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 20.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 20.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 20.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 20.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (6) [KC]

### Configuration-iBridgeBringup
- `CFBundleIdentifier`: `com.apple.iokit.IOUSBDeviceFamily`
- `DeviceDescription`:
  - `ConfigurationDescriptors`:
    -
      - `Attributes`: `192`
      - `Interfaces`:
        - `AppleUSBMux`
        - `AppleUSBNCMControl`
        - `AppleUSBNCMData`
      - `MaxPower`: `0`
- `IOClass`: `IOUSBDeviceConfigurator`
- `IOPersonalityPublisher`: `com.apple.iokit.IOUSBDeviceFamily`
- `IOPropertyMatch`:
  - `ConfigurationType`: `iBridgeBringup`
- `IOProviderClass`: `IOUSBDeviceController`

### Configuration-ncmAuxBringup
- `CFBundleIdentifier`: `com.apple.iokit.IOUSBDeviceFamily`
- `DeviceDescription`:
  - `ConfigurationDescriptors`:
    -
      - `Attributes`: `192`
      - `Interfaces`:
        - `AppleUSBNCMControl`
        - `AppleUSBNCMData`
        - `AppleUSBNCMControlAux`
        - `AppleUSBNCMDataAux`
      - `MaxPower`: `0`
- `IOClass`: `IOUSBDeviceConfigurator`
- `IOPersonalityPublisher`: `com.apple.iokit.IOUSBDeviceFamily`
- `IOPropertyMatch`:
  - `ConfigurationType`: `ncmAuxBringup`
- `IOProviderClass`: `IOUSBDeviceController`

### Configuration-ncmAuxOnlyBringup
- `CFBundleIdentifier`: `com.apple.iokit.IOUSBDeviceFamily`
- `DeviceDescription`:
  - `ConfigurationDescriptors`:
    -
      - `Attributes`: `192`
      - `Interfaces`:
        - `AppleUSBNCMControlAux`
        - `AppleUSBNCMDataAux`
      - `MaxPower`: `0`
- `IOClass`: `IOUSBDeviceConfigurator`
- `IOPersonalityPublisher`: `com.apple.iokit.IOUSBDeviceFamily`
- `IOPropertyMatch`:
  - `ConfigurationType`: `ncmAuxOnlyBringup`
- `IOProviderClass`: `IOUSBDeviceController`

### Configuration-ncmBringup
- `CFBundleIdentifier`: `com.apple.iokit.IOUSBDeviceFamily`
- `DeviceDescription`:
  - `ConfigurationDescriptors`:
    -
      - `Attributes`: `192`
      - `Interfaces`:
        - `AppleUSBNCMControl`
        - `AppleUSBNCMData`
      - `MaxPower`: `0`
- `IOClass`: `IOUSBDeviceConfigurator`
- `IOPersonalityPublisher`: `com.apple.iokit.IOUSBDeviceFamily`
- `IOPropertyMatch`:
  - `ConfigurationType`: `ncmBringup`
- `IOProviderClass`: `IOUSBDeviceController`

### Configuration-standardBringup
- `CFBundleIdentifier`: `com.apple.iokit.IOUSBDeviceFamily`
- `DeviceDescription`:
  - `ConfigurationDescriptors`:
    -
      - `Interfaces`:
        - `AppleUSBMux`
- `IOClass`: `IOUSBDeviceConfigurator`
- `IOPersonalityPublisher`: `com.apple.iokit.IOUSBDeviceFamily`
- `IOPropertyMatch`:
  - `ConfigurationType`: `standardBringup`
- `IOProviderClass`: `IOUSBDeviceController`

### ReservedInterface
- `CFBundleIdentifier`: `com.apple.iokit.IOUSBDeviceFamily`
- `IOClass`: `IOUSBDeviceInterfaceReserved`
- `IOPersonalityPublisher`: `com.apple.iokit.IOUSBDeviceFamily`
- `IOPropertyMatch`:
  - `USBDeviceFunction`: `Reserved`
- `IOProviderClass`: `IOUSBDeviceInterface`


## C++ classes (13) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBCapabilityDescriptor` | 0x88 | IOService → IORegistryEntry |
| `IOUSBDeviceConfigurator` | 0x88 | IOService → IORegistryEntry |
| `IOUSBDeviceControlRequest` | 0xa0 |  |
| `IOUSBDeviceController` | 0x448 | IOService → IORegistryEntry |
| `IOUSBDeviceDMACommand` | 0x90 | IODMACommand → IOCommand |
| `IOUSBDeviceInterface` | 0x138 | IOService → IORegistryEntry |
| `IOUSBDeviceInterfaceReserved` | 0x88 | IOService → IORegistryEntry |
| `IOUSBDeviceInterfaceUserClient` | 0x1b8 | IOUserClient → IOService → IORegistryEntry |
| `IOUSBDevicePipe` | 0x78 |  |
| `OSValueObject<AltInfo>` | 0x18 |  |
| `USBConfiguration` | 0x38 |  |
| `USBInterfaceAssociation` | 0x28 |  |
| `USBStringIndex` | 0x18 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1800)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00005fdc off=0x00afcc10-0x00b02bec addr=0xfffffe0007b00c10-0xfffffe0007b06bec r--/r--   __TEXT            
	sz=0x00003414 off=0x00afd378-0x00b0078c addr=0xfffffe0007b01378-0xfffffe0007b0478c               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000260 off=0x00b00790-0x00b009f0 addr=0xfffffe0007b04790-0xfffffe0007b049f0               __TEXT.__const            
	sz=0x000021fc off=0x00b009f0-0x00b02bec addr=0xfffffe0007b049f0-0xfffffe0007b06bec               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x000299fc off=0x036135f0-0x0363cfec addr=0xfffffe000a6175f0-0xfffffe000a640fec r-x/r-x   __TEXT_EXEC       
	sz=0x000292fc off=0x036135f0-0x0363c8ec addr=0xfffffe000a6175f0-0xfffffe000a6408ec          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000700 off=0x0363c8ec-0x0363cfec addr=0xfffffe000a6408ec-0xfffffe000a640fec          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000308 off=0x04a1a148-0x04a1a450 addr=0xfffffe000ba1e148-0xfffffe000ba1e450 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a1a148-0x04a1a210 addr=0xfffffe000ba1e148-0xfffffe000ba1e210               __DATA.__data             
	sz=0x00000218 off=0x00000000-0x00000218 addr=0xfffffe000ba1e210-0xfffffe000ba1e428               __DATA.__common           (Zerofill)
	sz=0x00000028 off=0x00000000-0x00000028 addr=0xfffffe000ba1e428-0xfffffe000ba1e450               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000044c0 off=0x014336a8-0x01437b68 addr=0xfffffe00084376a8-0xfffffe000843bb68 rw-/rw-   __DATA_CONST      
	sz=0x00000058 off=0x014336a8-0x01433700 addr=0xfffffe00084376a8-0xfffffe0008437700         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000050 off=0x01433700-0x01433750 addr=0xfffffe0008437700-0xfffffe0008437750         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00003760 off=0x01433750-0x01436eb0 addr=0xfffffe0008437750-0xfffffe000843aeb0         __DATA_CONST.__const            
	sz=0x000006c0 off=0x01436eb0-0x01437570 addr=0xfffffe000843aeb0-0xfffffe000843b570         __DATA_CONST.__kalloc_type      
	sz=0x00000190 off=0x01437570-0x01437700 addr=0xfffffe000843b570-0xfffffe000843b700         __DATA_CONST.__kalloc_var       
	sz=0x00000380 off=0x01437700-0x01437a80 addr=0xfffffe000843b700-0xfffffe000843ba80         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000e0 off=0x01437a80-0x01437b60 addr=0xfffffe000843ba80-0xfffffe000843bb60         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x01437b60-0x01437b68 addr=0xfffffe000843bb60-0xfffffe000843bb68         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 252 at 0x04af9430
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     E082D6D3-8C6F-3D44-B5C6-E78228ABAD25
008: LC_SOURCE_VERSION           896.40.5.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac86b8 size=0x400
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOUSBDeviceFamily`
- `CFBundleIdentifier`: `com.apple.iokit.IOUSBDeviceFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOUSBDeviceFamily`
- `CFBundleNumericVersion`: `33587200`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `2.0.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `2.0.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2006-2023 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `2.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOUSBDeviceFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198894277616`
- `_PrelinkExecutableRelativePath`: `IOUSBDeviceFamily`
- `_PrelinkExecutableSize`: `213408`
- `_PrelinkExecutableSourceAddr`: `-2198894277616`
- `_PrelinkKmodInfo`: `-2198828097208`

## Strings (554) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%s: %s::%s: %02x %02x %04x %04x %04x\n`
- `%s@%s: %s::%s: Failed to get current device description\n`
- `FirstInterface`
- `12111112122212121`
- `site.IOUSBDeviceIsocFrame`
- `SetDebugFlag`
- `driver-registration-timeout`
- `gotoDeviceState`
- `TestConfigSpeed`
- `ioGated`
- `%s: %s::%s: Unexpected data in state %d. Dropping %u bytes.\n`
- `11111111111211`
- `vendorID`
- `manufacturerString`
- `AllowMultipleCreates`
- `%s@%s: %s::%s: Got new configuration descriptor from \"%s\"\n`
- `site.IOUSBDeviceController`
- `bcd-usb-version`
- `%s@%s: %s::%s: \n`
- `iPod`
- `kPowerStateOff`
- `%s@%s: %s::%s: Failed to create interface name strings\n`
- `iMac`
- `ForceOffBusDisable`
- `Apple Inc.`
- `Description`
- `Mac`
- `SetDeviceDescription`
- `%s: %s::%s: Premature setup packet. Aborting endpoint 0x%x\n`
- `Attributes`
- `%s@%s: %s::%s: Unregistered function: %s\n`
- `%s@%s: %s::%s: Activating ncmAuxOnly fallback configuration\n`
- `%s@%s: %s::%s: Successfully created ncmAuxOnly fallback configuration\n`
- `BcdUSBVersion`
- `gated_handleUSBCableConnect`
- `sendControlOutStatus`
- `vendor-id`
- `manufacturer-string`
- `device-protocol`
- `%s@%s: %s::%s: Failed to copy device description\n`
- `iProd`
- `LockedConfiguration`
- `%s@%s: %s::%s: found invalid interface association information\n`
- `IOUSBDeviceFamily.kext/PlugIns/IOUSBDeviceLib.plugin`
- `%s: %s::%s: Descriptor length truncated: required 0x%x and copied 0x%x\n`
- `inputDataPacket`
- `IOUSBDeviceInterfaceUserClient::start : invalid provider\n`
- `DeviceAddress`
- `%s@%s: %s::%s: Failed to allocate FD capability descriptor\n`
- `%s@%s: %s::%s: didn't get a dictionary\n`
- `%s@%s: %s::%s: kVendorRequestCurrentLimit received, extra current %d mA, suspend current %d mA\n`
- `Reserved`
- `isochronousIoGated`
- `site.IOUSBDeviceControlRequest`
- `%s: %s::%s: Unexpected error - 0x%x\n`
- `%s@%s: %s::%s: failed to parse model name\n`
- `%s@%s: %s::%s: can't start function %s\n`
- `site.IOUSBDeviceConfigurator`
- `121111121222121211121122221111211111112`
- `AppleUSBNCMControlAux`
- `%s@%s: %s::%s: Successfully built fallback device description\n`
- `%s@%s: %s::%s: USB board-reset request received\n`
- `setupDeviceSetAddress`
- `Default`
- `%s: %s::%s: failed to validate the buffer and length\n`
- `12111112122212121112122122222221221222211212111111121212222211222222222222222222222222222222222222222222222222222222222222222112222222222`
- `Mac mini`
- `12222`
- `%s@%s: %s::%s: configuration: %s\n`
- `%s@%s: %s::%s: kVendorRequestSelectExtendedFunction: Did not find configuration for function %ld\n`
- `%s: %s::%s: invalid controller argument\n`
- `%s: %s::%s: Unexpected call to sendControlInData in state %d\n`
- `%d`
- `com.apple.private.usbdevice.setdescription`
- `InterfaceAssociation`
- `USBDeviceCommandParameter`
- `%s@%s: %s::%s: %s\n`
- `site.USBDeviceIsocAsyncParam`
- `USBStringIndex`
- `%s@%s: %s::%s: starting usb stack\n`
- `Powered`
- `%s: %s::%s: failed to deactivate pipe, result = 0x%x\n`
- `12222111111121121211`
- `%s: %s::%s: Premature status packet. Aborting endpoint 0x%x\n`
- `IOUSBDeviceController.cpp`
- `%s@%s: %s::%s: Unable to allocate serializer\n`
- `%s@%s: %s::%s: Failed to allocate config dictionary\n`
- `OverrideProtocol`
- `%s@%s: %s::%s: Unable to allocate _remoteWakeThreadcall\n`
- `ActiveSpeed`
- `\"Data packet not expected in the current state - %d\\n\" @%s:%d`
- `dataStageWriteCompletion`
- `IOUSBDeviceController`
- `kPowerStateSleep`
- `2111122223111`
- `121`
- `DeviceDescription`
- `uniqueDeviceID`
- `IOUSBDeviceInterfaceUserClient::start : failed to start provider\n`
- ` @%s:%d`
- `%s@%s: %s::%s: force-usb-fullspeed specified\n`
- `%s@%s: %s::%s: Unable to allocate IOCommandPool\n`
- `ConfigurationDescriptors`
- `IOPlatformUUID`
- `%s: %s::%s:  sent %u bytes\n`
- `kPowerStateSuspended`
- `DefaultBcdUSBVersion`
- `%s@%s: %s::%s: USB test mode (%u) specified\n`
- `%s@%s: %s::%s: thread_call_t failure\n`
- `%s@%s: %s::%s: Failed to create config attributes\n`
- `MacBookAir`
- `%s-R`
- `0A374CE4-7623-47C9-880E-1AC31513476F`
- `%s: %s::%s: invalid speed: %d\n`
- `%s: %s::%s: failed to validate the buffer\n`
- `AppleUSBCapabilityDescriptor`
- `product-id`
- `configuration-string`
- `usb_max_current`
- `\"unexpected power state %ld\" @%s:%d`
- `5EDBC6C9-1442-4917-86C0-9A76C9DFF098`
- `FinalizedDurationMS`
- `%s@%s: %s::%s: force-usb-highspeed specified\n`
- `joinPowerPlane`
- `ncmAuxOnly_fallback`
- `AppleTV`
- `No Description Provided`
- `setupDeviceSetConfiguration`
- `%s: %s::%s: Premature setup packet. Ending current transaction.\n`
- `%s: %s::%s:  received %u bytes\n`
- `product-string`
- `force-usb-fullspeed`
- `%s@%s: %s::%s: received kIOUSBDeviceCommandGoOffAndOnBus from \"%s\"\n`
- `%s@%s: %s::%s: configuration %d -> %d\n`
- `%s@%s: %s::%s: device not configured\n`
- `copyDescriptorGated`
- `IOUSBDeviceInterfaceUserClient`
- `IOUSBDeviceControlRequest.cpp`
- `processSetupPacket`
- `usb_compliance_mode`
- `stopThreadCallGated`
- `hasFailedNCMFunctions`
- `MacBook Pro`
- `%s: %s::%s: invalid endpoint type: 0x%x\n`
- `getInterval`
- `1211111212221212111111111111111111122222111111111222122`
- `\"Failed to allocate descriptors\" @%s:%d`
- `initSpeedOverride`
- `MapperPageSize`
- `addFailedFunctionsCapabilityDescriptor`
- `MacBookPro`
- `deactivateEndpointGated`
- `%s: %s::%s: Unexpected call to setControlOutResponse in state %d\n`
- `handleUserlandCommand`
- `force-usb-superspeed`
- `enable-acsleep`
- `bus-number`
- `handleUSBEnumerationTimeout`
- `%s@%s: %s::%s: direction is invalid\n`
- `DeviceState`
- `site.IOUSBDeviceInterfaceReserved`
- `%s: %s::%s: unexpected pipe state\n`
- `usb_dev_reset`
- `recordFailedFunctions`
- `AppleUSBCommonDebug`
- `Configuration`
- `AppleUSBEthernet`
- `\"Invalid maxPacketSize\" @%s:%d`
- `appendToStandardDescriptor`
- `force-usb-test-mode`
- `hw.cachelinesize`
- `%s@%s: %s::%s: %d function(s) failed to register within timeout\n`
- `Valeria`
- `ForceOffBusEnable`
- `setProperties`
- `CurrentState`
- `%s@%s: %s::%s: Added failed function to BOS descriptor: %s (string index %d)\n`
- `AppleUSBNCM`
- `site.IOUSBDeviceIORequest`
- `USBConfiguration`
- `%s@%s: %s::%s: cable connected, but not all interface drivers have registered yet\n`
- `%02x%02x%02x%02x%02x%02x`
- `%x`
- `StartedTimestamp`
- `site.IOUSBDeviceInterfaceUserClient`
- `%s@%s: %s::%s: Successfully added failed functions capability descriptor to BOS (length=%d)\n`
- `HomePod`
- `%s@%s: %s::%s: All functions registered - cancelling timeout timer\n`
- `\"failed to append device capability descriptor, totalLength: %d, bLength: %d\\n\" @%s:%d`
- `-restore`
- `site.IOUSBDeviceDMACommand`
- `%s: %s::%s: failed to to perform io, result = 0x%x\n`
- `deviceID`
- `%s@%s: %s::%s: Performing first USB suspend since boot\n`
- `serialNumber`
- `Addressed`
- `IsActive`
- `9E72217E-8A60-11DB-BF57-000D936D06D2`
- `%s@%s: %s::%s: IOUSBDeviceController::joinPowerPlane\n`
- `AudioAccessory`
- `USB NMI Request Received`
- `IOUSBDeviceController-debug`
- `LinkState`
- `site.USBConfiguration`
- `setCurrentLimit`
- `tryRemoteWakeThreadCallGated`
- `%s@%s: %s::%s: Device Remote Wake status 0x%08x\n`
- `IOUSBDeviceConfigurator: controller->createUSBDevice()=0x%08x\n`
- `FinalizedTimestamp`
- `%s@%s: %s::%s: Already in ncmAuxOnly fallback mode but %d function(s) still failed to register - giving up\n`
- `site.USBStringIndex`
- `DefaultConfiguration`
- `Not provided`
- `USBDeviceCommand`
- `SetDevicePreferredConfiguration`
- `sendControlInData`
- `site.USBDeviceCompletionParam`
- `kPowerStateUsable`
- `IOUSBDeviceController-configuration`
- `RealityDevice`
- `%s@%s: %s::%s: Removing config index %d\n`
- `%s@%s: %s::%s: interface association: %s (First: %d, Count: %d)\n`
- `DeviceDestroy`
- `initWithControllerOptions`
- `%s: %s::%s: Premature setup packet while in state - %d\n`
- `%s: %s::%s:  %02x %02x %04x %04x %04x\n`
- `device-subclass`
- `USBInterfaceAssociation`
- `1212112`
- `%s@%s: %s::%s: register function %s\n`
- `local-mac-address`
- `%s: %s::%s: Received more data than specified in the setup packet. Dropping %u bytes.\n`
- `productID`
- `%s@%s: %s::%s: USB enumeration did not complete in %d seconds. Timeout in state %d.\n`
- `%s@%s: %s::%s: Failed to create config description\n`
- `%s@%s: %s::%s: cable connected, but don't have device configuration yet\n`
- `IOPlatformSerialNumber`
- `ShowDeviceDebug`
- `%s@%s: %s::%s: waiting for these interface driver(s) to register:\n`
- `IOUSBDeviceInterface`
- `121222221112112`
- `%s: %s::%s: failed to get the workLoop\n`
- `product-version`
- `soft-disconnect-interval`
- `stop`
- `%s@%s: %s::%s: Driver registration timeout triggered\n`
- `%s@%s: %s::%s: ignoring kIOUSBDeviceCommandForceOffBusDisable from \"%s\" as we are already off bus\n`
- `%s@%s: %s::%s: Failed to allocate configurations array\n`
- `%s@%s: %s::%s: forcing device off USB due to \"%s\"\n`
- `%s: %s::%s: failed to allocate command gate\n`
- `DefaultPreferredConfiguration`
- `SelectedConfiguration`
- `ConnectionSpeed`
- `unique-chip-id`
- `activateFallbackConfiguration`
- `copyDescriptor`
- `getCurrentLimit`
- `max-power`
- `buildFallbackDeviceDescription`
- `%s@%s: %s::%s: charger type %lu, charging rate %lu mA\n`
- `%s@%s: %s::%s: Found required function in active configurations - %ld\n`
- `121112221112221211`
- `IOCFPlugInTypes`
- `configureEndpointGated`
- `%s: %s::%s: Aborting control transaction from state - %d\n`
- `deviceSubClass`
- `%s@%s: %s::%s: Found failed NCM interface: %s\n`
- `startUSBStack`
- `site.T`
- `%s@%s: %s::%s: No failed functions to add to BOS descriptor\n`
- `io`
- `prepareDefaults`
- `stopThreadCall`
- `Vision Pro`
- `%s@%s: %s::%s: going to state %d\n`
- `AccessoryResistorSwap`
- `%s@%s: %s::%s:    interface: %s\n`
- `zlpCompletion`
- `%s@%s: %s::%s: unrecognized model name %s\n`
- `force-usb-highspeed`
- `%s@%s: %s::%s: U1SEL %d U1PEL %d U2SEL %d U2PEL %d\n`
- `IOUSBDeviceInterfaceReserved`
- `%s: %s::%s: activating with settings, address: 0x%x, type: 0x%x, maxPacketSize: 0x%x, interval: 0x%x, pipeProperty: 0x%x\n`
- `%s: %s::%s: ZLP expected in the status phase (%d). Dropping %u bytes.\n`
- `Undefined Exception`
- `%s@%s: %s::%s: did not provide a completion for I/O\n`
- `ADP`
- `deviceClass`
- `site.USBInterfaceAssociation`
- `createUSBDevice`
- `%s@%s: %s::%s: no command provided\n`
- `IOUserClientClass`
- `IOUSBDeviceInterfaceUserClient::start : failed to allocate _classCommandTimer\n`
- `setPowerStateGated`
- `hardwareException`
- `Index`
- `InterfaceCount`
- `GoOffAndOnBus`
- `%s: %s::%s: Lost Status IN ACK from host. Aborting endpoint 0x%x\n`
- `11111111121`
- `DefaultDeviceDescription`
- `MacBook Air`
- `NCM Control`
- `%s: %s::%s: failed to activate pipe, result = 0x%x\n`
- `receiveControlOutData`
- `IOUSBDeviceInterfaceUserClient::start : failed to allocate _commandGate\n`
- `%s@%s: %s::%s: model %s version %lu.%lu\n`
- `%s@%s: %s::%s: _speedOverride = (%i).\n`
- `AppleUSBNCMDataAux`
- `%s@%s: %s::%s: Failed to create fallback USB device: 0x%x\n`
- `OverrideClass`
- `%s: %s::%s: sendControlInDataGated failed: result = 0x%x`
- `IOUSBDeviceInterfaceUserClient::start : failed to get WorkLoop\n`
- `site.AppleUSBCapabilityDescriptor`
- `Fallback Configuration - ncmAux`
- `%s@%s: %s::%s: NCM interfaces are in the failed functions list - cannot fallback to NCM-only configuration. Giving up with %d function(s) unregistered\n`
- `Watch`
- `%s@%s: %s::%s: setting USB device address %d\n`
- `%s@%s: %s::%s: Function Remote Wake for function %d failed with status 0x%08x\n`
- `PreferredConfiguration`
- `/chosen`
- `%s: %s::%s: can't allocate memory!\n`
- `\"Invalid state %d\\n\" @%s:%d`
- `%s: %s::%s: Unexpected call to sendControlOutStatus in state %d\n`
- `deviceProtocol`
- `usb-device-slp-ddr`
- `getDMACommand`
- `site.IOUSBDeviceInterface`
- `setPipeProperty`
- `%s: %s::%s: Setup packet not available to process (Current State %d)\n`
- `%s@%s: %s::%s: parsed product-string %s product-id 0x%04x product-version 0x%04x\n`
- `MaxPower`
- `usb_dev_nmi`
- `%s@%s: %s::%s: Failed to build fallback device description - unable to proceed with fallback configuration\n`
- `MPS0`
- `%s@%s: %s::%s: Failed to allocate interfaces array\n`
- `%s@%s: %s::%s: Performing USB suspend. Num suspends since boot: %llu. Nanoseconds since last suspend: %llu\n`
- `%s@%s: %s::%s: missing required entitlement\n`
- `gated_setProperties`
- `SetDeviceConfiguration`
- `%s@%s: %s::%s: waiting to get device configuration\n`
- `SetEnableTestConfig`
- `%s@%s: %s::%s: Found required function in all configurations - %ld\n`
- `unknownHardware`
- `productString`
- `NCM Control Direct`
- `%s@%s: %s::%s: no longer forcing device off USB due to \"%s\"\n`
- `%s: %s::%s: invalid direction argument\n`
- `removePotentialOwner`
- `%s@%s: %s::%s: force-usb-superspeed specified\n`
- `handleUnregisteredFunctionsTimeout`
- `IOUSBDeviceDMACommand`
- `allow-subpage-mapping`
- `%s: %s::%s: invalid completion\n`
- `statusStageWriteCompletion`
- `start`
- `IOUSBDeviceDevice.cpp`
- `%s@%s: %s::%s: device configuration not found\n`
- `21`
- `sendControlInDataGated`
- `device-class`
- `%s@%s: %s::%s: did not find a mapper\n`
- `%s@%s: %s::%s: Creating failed functions capability descriptor for %d failed functions\n`
- `setupDriverRequest`
- `setupDeviceSetSELDataCompletion`
- `IOUSBDeviceControlRequest`
- `Macmini`
- `usb_enumeration_timeout`
- `activateEndpointGated`
- `%s: %s::%s: failed to allocate workloop\n`
- `ConfigurationType`
- `EnableTestConfig`
- `%s@%s: %s::%s: unknown command %s\n`
- `IOUSBDeviceConfigurator`
- `OSValueObject<AltInfo>`
- `%s@%s: %s::%s: failed to allocate dma command\n`
- `Developer Transition Kit`
- `ExtendedConfiguration`
- `CreatedTimestamp`
- `%s@%s: %s::%s: base current=%d extra=%d suspend=%d usb state=%d(%s)\n`
- `i8@?0`
- `IOUSBDevicePipe.cpp`
- `copyAppendedStandardDescriptor`
- `copyClassSpecificDescriptors`
- `stallSetupRequest`
- `%s@%s: %s::%s: SetDebugFlag - 0x%08x\n`
- `attributes`
- `%s@%s: %s::%s: Failed functions capability descriptor size limit reached\n`
- `initWithControllerAndSettings`
- `reset`
- `%s: %s::%s: setup packet %lld not handled\n`
- `kPowerStateOn`
- `A745B2DF-FB29-4E45-844D-BEFD6D125F9A`
- `%s@%s: %s::%s: unrecognized charger type %u\n`
- `gated_registerFunction`
- `handleUSBSuspend`
- `IOUSBDevicePipe`
- `site.IOUSBDevicePipe`
- `%s: %s::%s: Interface Descriptor buffer not sufficient: 0x%x\n`
- `\"Invalid mps %d for type %d\\n\" @%s:%d`
- `%s@%s: %s::%s: %s -> %s\n`
- `RemoteWakeEnabled`
- `Interfaces`
- `iPad`
- `%s: %s::%s: failed to init the commandGate\n`
- `%s: %s::%s: deactivating with settings, address: 0x%x, type: 0x%x, maxPacketSize: 0x%x, interval: 0x%x, pipeProperty: 0x%x\n`
- `%s: %s::%s: Unexpected call to stallSetupRequest in state %d\n`
- `%s-configuration`
- `%s::%s: buffer size not sufficient: 0x%x\n`
- `getCurMinServiceInterval`
- `Disconnected`
- `USBDeviceFunction`
- `%s: %s::%s: \n`
- `IOUSBDeviceControlRequest-debug`
- `iPhone`
- `OverrideSubClass`
- `%s@%s: %s::%s: for config %d is %u. Status 0x%08x.\n`
- `Configured`
- `%s: %s::%s: state change %d -> %d\n`
- `inputSetupPacket`

**[__TEXT.__os_log]**

- `%s@%s: %s::%s:    interface: %s\n`
- `%s: %s::%s:  %02x %02x %04x %04x %04x\n`
- `%s: %s::%s: failed to to perform io, result = 0x%x\n`
- `%s: %s::%s: Unexpected call to setControlOutResponse in state %d\n`
- `%s@%s: %s::%s: model %s version %lu.%lu\n`
- `%s@%s: %s::%s: Device Remote Wake status 0x%08x\n`
- `%s: %s::%s: failed to get the workLoop\n`
- `%s: %s::%s: activating with settings, address: 0x%x, type: 0x%x, maxPacketSize: 0x%x, interval: 0x%x, pipeProperty: 0x%x\n`
- `%s@%s: %s::%s: Failed to create interface name strings\n`
- `%s@%s: %s::%s: missing required entitlement\n`
- `%s@%s: %s::%s: IOUSBDeviceController::joinPowerPlane\n`
- `%s@%s: %s::%s: Failed to copy device description\n`
- `%s@%s: %s::%s: Got new configuration descriptor from \"%s\"\n`
- `%s@%s: %s::%s: force-usb-fullspeed specified\n`
- `%s@%s: %s::%s: Unable to allocate serializer\n`
- `%s: %s::%s: \n`
- `%s: %s::%s: failed to activate pipe, result = 0x%x\n`
- `%s@%s: %s::%s: ignoring kIOUSBDeviceCommandForceOffBusDisable from \"%s\" as we are already off bus\n`
- `%s: %s::%s: Unexpected call to stallSetupRequest in state %d\n`
- `%s@%s: %s::%s: Failed functions capability descriptor size limit reached\n`
- `%s@%s: %s::%s: Failed to allocate config dictionary\n`
- `%s@%s: %s::%s: Failed to create config description\n`
- `%s@%s: %s::%s: U1SEL %d U1PEL %d U2SEL %d U2PEL %d\n`
- `%s@%s: %s::%s: device configuration not found\n`
- `%s: %s::%s:  received %u bytes\n`
- `%s@%s: %s::%s: unrecognized model name %s\n`
- `%s@%s: %s::%s: All functions registered - cancelling timeout timer\n`
- `%s: %s::%s: Premature setup packet. Ending current transaction.\n`
- `%s: %s::%s: Unexpected call to sendControlOutStatus in state %d\n`
- `%s: %s::%s: Unexpected error - 0x%x\n`
- `%s@%s: %s::%s: Already in ncmAuxOnly fallback mode but %d function(s) still failed to register - giving up\n`
- `%s@%s: %s::%s: no command provided\n`
- `%s: %s::%s: Setup packet not available to process (Current State %d)\n`
- `%s@%s: %s::%s: USB test mode (%u) specified\n`
- `%s::%s: buffer size not sufficient: 0x%x\n`
- `%s@%s: %s::%s: kVendorRequestSelectExtendedFunction: Did not find configuration for function %ld\n`
- `%s: %s::%s: failed to deactivate pipe, result = 0x%x\n`
- `%s@%s: %s::%s: USB enumeration did not complete in %d seconds. Timeout in state %d.\n`
- `%s@%s: %s::%s: didn't get a dictionary\n`
- `%s: %s::%s: failed to validate the buffer and length\n`
- `%s: %s::%s: ZLP expected in the status phase (%d). Dropping %u bytes.\n`
- `%s@%s: %s::%s: Failed to create fallback USB device: 0x%x\n`
- `%s@%s: %s::%s: no longer forcing device off USB due to \"%s\"\n`
- `%s@%s: %s::%s: did not find a mapper\n`
- `%s: %s::%s: failed to allocate workloop\n`
- `%s: %s::%s: Received more data than specified in the setup packet. Dropping %u bytes.\n`
- `%s: %s::%s: sendControlInDataGated failed: result = 0x%x`
- `%s: %s::%s: %02x %02x %04x %04x %04x\n`
- `%s@%s: %s::%s: %d function(s) failed to register within timeout\n`
- `%s@%s: %s::%s: configuration: %s\n`
- `%s@%s: %s::%s: interface association: %s (First: %d, Count: %d)\n`
- `%s: %s::%s: Descriptor length truncated: required 0x%x and copied 0x%x\n`
- `%s: %s::%s: Premature setup packet. Aborting endpoint 0x%x\n`
- `%s: %s::%s: Lost Status IN ACK from host. Aborting endpoint 0x%x\n`
- `%s: %s::%s:  sent %u bytes\n`
- `%s@%s: %s::%s: Removing config index %d\n`
- `%s@%s: %s::%s: unknown command %s\n`
- `%s@%s: %s::%s: device not configured\n`
- `%s: %s::%s: can't allocate memory!\n`
- `%s: %s::%s: Premature setup packet while in state - %d\n`
- `%s@%s: %s::%s: starting usb stack\n`
- `%s: %s::%s: deactivating with settings, address: 0x%x, type: 0x%x, maxPacketSize: 0x%x, interval: 0x%x, pipeProperty: 0x%x\n`
- `%s@%s: %s::%s: Unable to allocate IOCommandPool\n`
- `%s@%s: %s::%s: \n`
- `%s@%s: %s::%s: Driver registration timeout triggered\n`
- `%s@%s: %s::%s: direction is invalid\n`
- `%s@%s: %s::%s: cable connected, but not all interface drivers have registered yet\n`
- `%s: %s::%s: state change %d -> %d\n`
- `%s@%s: %s::%s: Failed to create config attributes\n`
- `%s@%s: %s::%s: Successfully built fallback device description\n`
- `%s: %s::%s: invalid speed: %d\n`
- `%s: %s::%s: failed to allocate command gate\n`
- `%s@%s: %s::%s: going to state %d\n`
- `%s@%s: %s::%s: Failed to allocate FD capability descriptor\n`
- `%s@%s: %s::%s: failed to allocate dma command\n`
- `%s@%s: %s::%s: for config %d is %u. Status 0x%08x.\n`
- `%s@%s: %s::%s: SetDebugFlag - 0x%08x\n`
- `%s@%s: %s::%s: IOUSBDeviceController::hardwareException: Type: 0x%08x %s`
- `%s@%s: %s::%s: Failed to get current device description\n`
- `%s@%s: %s::%s: charger type %lu, charging rate %lu mA\n`
- `%s@%s: %s::%s: Performing USB suspend. Num suspends since boot: %llu. Nanoseconds since last suspend: %llu\n`
- `%s@%s: %s::%s: parsed product-string %s product-id 0x%04x product-version 0x%04x\n`
- `%s@%s: %s::%s: failed to parse model name\n`
- `%s@%s: %s::%s: force-usb-highspeed specified\n`
- `%s: %s::%s: Unexpected data in state %d. Dropping %u bytes.\n`
- `%s@%s: %s::%s: _speedOverride = (%i).\n`
- `%s@%s: %s::%s: NCM interfaces are in the failed functions list - cannot fallback to NCM-only configuration. Giving up with %d function(s) unregistered\n`
- `%s@%s: %s::%s: found invalid interface association information\n`
- `%s: %s::%s: invalid endpoint type: 0x%x\n`
- `%s@%s: %s::%s: kVendorRequestCurrentLimit received, extra current %d mA, suspend current %d mA\n`
- `%s@%s: %s::%s: Found required function in all configurations - %ld\n`
- `%s@%s: %s::%s: setting USB device address %d\n`
- `%s: %s::%s: invalid completion\n`
- `%s: %s::%s: Aborting control transaction from state - %d\n`
- `%s@%s: %s::%s: can't start function %s\n`
- `%s: %s::%s: failed to validate the buffer\n`
- `%s: %s::%s: Unexpected call to sendControlInData in state %d\n`
- `%s@%s: %s::%s: thread_call_t failure\n`
- `%s@%s: %s::%s: Performing first USB suspend since boot\n`
- `%s@%s: %s::%s: waiting for these interface driver(s) to register:\n`
- `%s: %s::%s: Interface Descriptor buffer not sufficient: 0x%x\n`
- `%s: %s::%s: invalid direction argument\n`
- `%s: %s::%s: unexpected pipe state\n`
- `%s@%s: %s::%s: %s -> %s\n`
- `%s@%s: %s::%s: Unregistered function: %s\n`
- `%s@%s: %s::%s: Found failed NCM interface: %s\n`
- `%s@%s: %s::%s: Successfully created ncmAuxOnly fallback configuration\n`
- `%s@%s: %s::%s: waiting to get device configuration\n`
- `%s@%s: %s::%s: Unable to allocate _remoteWakeThreadcall\n`
- `%s@%s: %s::%s: Added failed function to BOS descriptor: %s (string index %d)\n`
- `%s@%s: %s::%s: Failed to build fallback device description - unable to proceed with fallback configuration\n`
- `%s@%s: %s::%s: No failed functions to add to BOS descriptor\n`
- `%s@%s: %s::%s: did not provide a completion for I/O\n`
- `%s@%s: %s::%s: cable connected, but don't have device configuration yet\n`
- `%s@%s: %s::%s: Found required function in active configurations - %ld\n`
- `%s@%s: %s::%s: %s\n`
- `%s@%s: %s::%s: base current=%d extra=%d suspend=%d usb state=%d(%s)\n`
- `%s@%s: %s::%s: Creating failed functions capability descriptor for %d failed functions\n`
- `%s@%s: %s::%s: Failed to allocate interfaces array\n`
- `%s@%s: %s::%s: register function %s\n`
- `%s@%s: %s::%s: received kIOUSBDeviceCommandGoOffAndOnBus from \"%s\"\n`
- `%s@%s: %s::%s: USB board-reset request received\n`
- `%s: %s::%s: invalid controller argument\n`
- `%s: %s::%s: Premature status packet. Aborting endpoint 0x%x\n`
- `%s@%s: %s::%s: Activating ncmAuxOnly fallback configuration\n`
- `%s@%s: %s::%s: force-usb-superspeed specified\n`
- `%s@%s: %s::%s: Failed to allocate configurations array\n`
- `%s@%s: %s::%s: forcing device off USB due to \"%s\"\n`
- `%s@%s: %s::%s: configuration %d -> %d\n`
- `%s@%s: %s::%s: Function Remote Wake for function %d failed with status 0x%08x\n`
- `%s: %s::%s: failed to init the commandGate\n`
- `%s: %s::%s: setup packet %lld not handled\n`
- `%s@%s: %s::%s: Successfully added failed functions capability descriptor to BOS (length=%d)\n`
- `%s@%s: %s::%s: unrecognized charger type %u\n`
