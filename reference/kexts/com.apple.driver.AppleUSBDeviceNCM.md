# `com.apple.driver.AppleUSBDeviceNCM`

- Name: AppleUSBDeviceNCM
- Version: `5.0.0`
- UUID: `201775AA-B938-339E-8660-FFD518004A5A`
- Source version: `404.40.4.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.usb.networking`](com.apple.driver.usb.networking.md) 5.0, [`com.apple.iokit.IONetworkingFamily`](com.apple.iokit.IONetworkingFamily.md) 3.3, [`com.apple.iokit.IOUSBDeviceFamily`](com.apple.iokit.IOUSBDeviceFamily.md) 2.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 14.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 14.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 14.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (5) [KC]

### USB Device NCM Control
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBDeviceNCM`
- `IOClass`: `AppleUSBDeviceNCM11Control`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBDeviceNCM`
- `IOPropertyMatch`:
  - `USBDeviceFunction`: `AppleUSBNCMControl`
- `IOProviderClass`: `IOUSBDeviceInterface`

### USB Device NCM Control Aux
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBDeviceNCM`
- `IOClass`: `AppleUSBDeviceNCM11Control`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBDeviceNCM`
- `IOPropertyMatch`:
  - `USBDeviceFunction`: `AppleUSBNCMControlAux`
- `IOProviderClass`: `IOUSBDeviceInterface`
- `NetworkInterfaceFlags`: `536870912`
- `ncm-control-use-aux`: `<data 20 chars>`

### USB Device NCM Control Direct
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBDeviceNCM`
- `IOClass`: `AppleUSBDeviceNCM11Control`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBDeviceNCM`
- `IOPropertyMatch`:
  - `USBDeviceFunction`: `AppleUSBNCMControlDirect`
- `IOProviderClass`: `IOUSBDeviceInterface`
- `InterfaceDescriptionString`: `NCM Control Direct`
- `NetworkInterfaceFlags`: `536870912`

### USB Device NCM Data
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBDeviceNCM`
- `IOClass`: `AppleUSBDeviceNCM11Data`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBDeviceNCM`
- `IOPropertyMatch`:
  - `USBDeviceFunction`: `AppleUSBNCMData`
- `IOProviderClass`: `IOUSBDeviceInterface`

### USB Device NCM Data Aux
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBDeviceNCM`
- `IOClass`: `AppleUSBDeviceNCM11Data`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBDeviceNCM`
- `IOPropertyMatch`:
  - `USBDeviceFunction`: `AppleUSBNCMDataAux`
- `IOProviderClass`: `IOUSBDeviceInterface`


## C++ classes (5) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBDeviceNCM11Control` | 0x168 | AppleUSBDeviceNCMControl → IOService → IORegistryEntry |
| `AppleUSBDeviceNCM11Data` | 0x230 | AppleUSBDeviceNCMData → IOEthernetController → IONetworkController → IOService → IORegistryEntry |
| `AppleUSBDeviceNCMControl` | 0x120 | IOService → IORegistryEntry |
| `AppleUSBDeviceNCMData` | 0x230 | IOEthernetController → IONetworkController → IOService → IORegistryEntry |
| `AppleUSBDeviceNCMPrivateEthernetInterface` | 0x148 | IOEthernetInterface → IONetworkInterface → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000016a0 off=0x008d2dd0-0x008d4470 addr=0xfffffe00078d6dd0-0xfffffe00078d8470 r--/r--   __TEXT            
	sz=0x00000ff5 off=0x008d33f8-0x008d43ed addr=0xfffffe00078d73f8-0xfffffe00078d83ed               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000080 off=0x008d43f0-0x008d4470 addr=0xfffffe00078d83f0-0xfffffe00078d8470               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00008d48 off=0x02b22230-0x02b2af78 addr=0xfffffe0009b26230-0xfffffe0009b2ef78 r-x/r-x   __TEXT_EXEC       
	sz=0x00008718 off=0x02b22230-0x02b2a948 addr=0xfffffe0009b26230-0xfffffe0009b2e948          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000630 off=0x02b2a948-0x02b2af78 addr=0xfffffe0009b2e948-0xfffffe0009b2ef78          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001a0 off=0x049d0d68-0x049d0f08 addr=0xfffffe000b9d4d68-0xfffffe000b9d4f08 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049d0d68-0x049d0e30 addr=0xfffffe000b9d4d68-0xfffffe000b9d4e30               __DATA.__data             
	sz=0x000000d8 off=0x00000000-0x000000d8 addr=0xfffffe000b9d4e30-0xfffffe000b9d4f08               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00002af8 off=0x012a4cd8-0x012a77d0 addr=0xfffffe00082a8cd8-0xfffffe00082ab7d0 rw-/rw-   __DATA_CONST      
	sz=0x00000020 off=0x012a4cd8-0x012a4cf8 addr=0xfffffe00082a8cd8-0xfffffe00082a8cf8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000020 off=0x012a4cf8-0x012a4d18 addr=0xfffffe00082a8cf8-0xfffffe00082a8d18         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000025a8 off=0x012a4d18-0x012a72c0 addr=0xfffffe00082a8d18-0xfffffe00082ab2c0         __DATA_CONST.__const            
	sz=0x00000140 off=0x012a72c0-0x012a7400 addr=0xfffffe00082ab2c0-0xfffffe00082ab400         __DATA_CONST.__kalloc_type      
	sz=0x00000318 off=0x012a7400-0x012a7718 addr=0xfffffe00082ab400-0xfffffe00082ab718         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000b8 off=0x012a7718-0x012a77d0 addr=0xfffffe00082ab718-0xfffffe00082ab7d0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 221 at 0x04aebb34
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     201775AA-B938-339E-8660-FFD518004A5A
008: LC_SOURCE_VERSION           404.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab7518 size=0x120
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleUSBDeviceNCM`
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBDeviceNCM`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUSBDeviceNCM`
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
- `NSHumanReadableCopyright`: `Copyright © 2016 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleUSBDeviceNCM.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896546352`
- `_PrelinkExecutableRelativePath`: `AppleUSBDeviceNCM`
- `_PrelinkExecutableSize`: `53376`
- `_PrelinkExecutableSourceAddr`: `-2198896546352`
- `_PrelinkKmodInfo`: `-2198828397208`

## Strings (130) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `kIOUSBDeviceInterfaceMessageTypeSetAlternateSetting`
- `SIM`
- `%06lu.%06u %s::%s: featureSelector 0x%x returning 0x%x\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: IN 0x%x, status 0x%x, transferSize %d\n`
- `device-mac-address`
- `sim`
- `1211111212221212111111122121111111111111111111222222222221122221211222`
- `updateLinkState`
- `%06lu.%06u [0x%llx] %s::%s: interface interrupt disabled = %d\n`
- `%06lu.%06u [0x%llx] %s::%s: use ECID %d\n`
- `enabled`
- `%06lu.%06u [0x%llx] %s::%s: `
- `%06lu.%06u %s::%s: NCM 1.1 NO-OP for reportLinkRate\n`
- `handleLinkChangeGated`
- `readBulkPipeGated`
- `bulkReadCompleteGated`
- `productID`
- `%06lu.%06u [0x%llx] %s::%s: EP0 OUT data phase %s due to %s=%d\n`
- `reportLinkRate`
- `%06lu.%06u [0x%llx] %s::%s: device-mac-address not found for device in the device-tree, generating a fake one\n`
- `unknown`
- `site.AppleUSBDeviceNCM11Data`
- `ncm-self-name`
- `%llx`
- `%06lu.%06u [0x%llx][%s] %s::%s: status %d\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: kNCMCommandSetMaxDatagramSize\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: kNCMCommandSetCRCMode\n`
- `HiddenInterface`
- `HostAttached`
- `%06lu.%06u [0x%llx][%s] %s::%s: applying 0x%08x flags on interface\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: kSet_Ethernet_Packet_Filter\n`
- `121111121222121211111122222222222222`
- `%06lu.%06u %s::%s: featureSelector 0x%x reqStatus 0x%x returning 0x%x\n`
- `ncm-no-remote-wake`
- `%06lu.%06u [0x%llx] %s::%s: AppleUSBNCM host version %#x (%s)\n`
- `%06lu.%06u %s::%s: isExtendedRequest cmd 0x%lx returning 0x%x\n`
- `Link Up`
- `%06lu.%06u [0x%llx][%s] %s::%s: IN 0x%x\n`
- `shouldSelfNameInterface`
- `AppleUSBDeviceNCMData`
- `ncm-control-use-aux`
- `%06lu.%06u [0x%llx][%s] %s::%s: %d\n`
- `NCM Data`
- `free`
- `ncm-self-name-unit`
- `bulkWriteCompleteGated`
- `NCM Control`
- `%06lu.%06u [0x%llx][%s] %s::%s: baseCommand 0x%x, featureSelector 0x%x, commandStatus 0x%x\n`
- `disable`
- `site.AppleUSBDeviceNCM11Control`
- `%06lu.%06u [0x%llx][%s] %s::%s: warning - gave up waiting: _pendingInCount %d, _pendingOutCount %d, _pendingLinkChange %d\n`
- `Disabled`
- `ncm-control-ecid-mac`
- `NetworkInterfaceFlags`
- `InterfaceDescriptionString`
- `handleControlRequest`
- `site.AppleUSBDeviceNCMData`
- `SelfNamed`
- `messageGated`
- `%06lu.%06u [0x%llx][%s] %s::%s: %s, %s\n`
- `DeviceDescription`
- `-restore`
- `completeSetExtendedFeature`
- `site.AppleUSBDeviceNCMPrivateEthernetInterface`
- `shouldSelfConfigureInterface`
- `BSD Name`
- `12111112122212121111111112222111211211121`
- `device-ncm-maxntb`
- `device-ncm-maxseg`
- `ncm-self-configure`
- `kIOUSBDeviceInterfaceMessageTypeWasDeactivated`
- `%06lu.%06u [0x%llx][%s] %s::%s: OUT 0x%x\n`
- `IONetworkStatsKey`
- `ncm-interrupt-ep-disabled`
- `AppleUSBDeviceNCM11Data`
- `stop`
- `getSelfNameBSDUnitNumber`
- `AppleSynopsysOTGDevice`
- `/chosen`
- `kIOUSBDeviceInterfaceMessageTypeWasActivated`
- `%06lu.%06u [0x%llx][%s] %s::%s: unable to acquire ifnet pointer\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: kNCMCommandSetNetworkAddress\n`
- `%02X%02X%02X%02X%02X%02X`
- `%06lu.%06u [0x%llx] %s::%s: iMACAddress %d\n`
- `unique-chip-id`
- `AppleUSBDeviceNCM11Control`
- `121111121222121211111122222222222222222222222`
- `Link Down`
- `dequeueAndTransmitPackets`
- `device-ncm-ctrl-debug`
- `%06lu.%06u [0x%llx] %s::%s: host-mac-address not found for host in the device-tree, generating a fake one\n`
- `%u.%u.%u`
- `updateDeviceRemoteWakePolicy() returned 0x%x\n`
- `device-ncm-data-debug`
- `start`
- `enable`
- `rdar://104231430 (productID)`
- `buildExtendedCapabilityDescriptor`
- `waitControlStart`
- `waitControlFinish`
- `site.AppleUSBDeviceNCMControl`
- `host-mac-address`
- `%06lu.%06u [0x%llx] %s::%s: EP0 OUT data phase disabled due to %s\n`
- `ncm-no-hide`
- `AppleUSBDeviceNCMPrivateEthernetInterface`
- `commandCallbackGated`
- `%06lu.%06u [0x%llx][%s] %s::%s: %s (%s)\n`
- `Index`
- `%06lu.%06u %s::%s: bRequest 0x%x, handlerStatus 0x%x\n`
- `ncm-control-interface-subtype`
- `%06lu.%06u [0x%llx] %s::%s: status %d\n`
- `controlRequestCompletion`
- `AppleUSBDeviceNCMControl`
- `Enabled`
- `%06lu.%06u [0x%llx][%s] %s::%s: kNCMCommandSetNTBInputSize\n`
- `Error reading out pipe\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: OUT 0x%x, status 0x%x, transferSize %d\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: %s curr = %d, alt = %d\n`
- `Error allocating rxCommand\n`
- `disabled`
- `i8@?0`
- `%06lu.%06u [0x%llx][%s] %s::%s: kNCMCommandSetNTBFormat\n`
- `%06lu.%06u [0x%llx][%s] %s::%s: %s\n`
- `IOMACAddress`
- `writeZLPGated`
- `anpi`
- `rdar://104231430 (hw.target)`
- `handleSetExtendedFeature`
- `%06lu.%06u [0x%llx][%s] %s::%s: \n`
- `device-ncm-promiscuous`
