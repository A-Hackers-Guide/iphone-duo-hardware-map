# `com.apple.driver.AppleUSBEthernetDevice`

- Name: AppleUSBEthernetDevice
- Version: `7.0`
- UUID: `7B0DAC3F-7A4A-35DE-8D36-867CD60EA66B`
- Source version: `170.40.1.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.iokit.IONetworkingFamily`](com.apple.iokit.IONetworkingFamily.md) 1.7.0, [`com.apple.iokit.IOUSBDeviceFamily`](com.apple.iokit.IOUSBDeviceFamily.md) 2.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0b2, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0b2, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 10.0.0d1

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### USB Device Ethernet
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBEthernetDevice`
- `IOClass`: `AppleUSBEthernetDevice`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBEthernetDevice`
- `IOPropertyMatch`:
  - `USBDeviceFunction`: `AppleUSBEthernet`
- `IOProviderClass`: `IOUSBDeviceInterface`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBEthernetDevice` | 0x1e8 | IOEthernetController → IONetworkController → IOService → IORegistryEntry |
| `AppleUSBEthernetDeviceCommand` | 0x48 | IOCommand |
| `AppleUSBEthernetDeviceCommandPool` | 0x70 | IOCommandPool |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001252 off=0x008d6510-0x008d7762 addr=0xfffffe00078da510-0xfffffe00078db762 r--/r--   __TEXT            
	sz=0x00000016 off=0x008d6b88-0x008d6b9e addr=0xfffffe00078dab88-0xfffffe00078dab9e               __TEXT.__const            
	sz=0x00000bc4 off=0x008d6b9e-0x008d7762 addr=0xfffffe00078dab9e-0xfffffe00078db762               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00003e94 off=0x02b3e1c0-0x02b42054 addr=0xfffffe0009b421c0-0xfffffe0009b46054 r-x/r-x   __TEXT_EXEC       
	sz=0x00003b84 off=0x02b3e1c0-0x02b41d44 addr=0xfffffe0009b421c0-0xfffffe0009b45d44          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000310 off=0x02b41d44-0x02b42054 addr=0xfffffe0009b45d44-0xfffffe0009b46054          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000150 off=0x049d1450-0x049d15a0 addr=0xfffffe000b9d5450-0xfffffe000b9d55a0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049d1450-0x049d1518 addr=0xfffffe000b9d5450-0xfffffe000b9d5518               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000b9d5518-0xfffffe000b9d55a0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000e88 off=0x012abb28-0x012ac9b0 addr=0xfffffe00082afb28-0xfffffe00082b09b0 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x012abb28-0x012abb30 addr=0xfffffe00082afb28-0xfffffe00082afb30         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x012abb30-0x012abb38 addr=0xfffffe00082afb30-0xfffffe00082afb38         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000b30 off=0x012abb38-0x012ac668 addr=0xfffffe00082afb38-0xfffffe00082b0668         __DATA_CONST.__const            
	sz=0x000000c0 off=0x012ac668-0x012ac728 addr=0xfffffe00082b0668-0xfffffe00082b0728         __DATA_CONST.__kalloc_type      
	sz=0x000000a0 off=0x012ac728-0x012ac7c8 addr=0xfffffe00082b0728-0xfffffe00082b07c8         __DATA_CONST.__kalloc_var       
	sz=0x00000188 off=0x012ac7c8-0x012ac950 addr=0xfffffe00082b07c8-0xfffffe00082b0950         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000060 off=0x012ac950-0x012ac9b0 addr=0xfffffe00082b0950-0xfffffe00082b09b0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 110 at 0x04aec224
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     7B0DAC3F-7A4A-35DE-8D36-867CD60EA66B
008: LC_SOURCE_VERSION           170.40.1.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab7898 size=0x98
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleUSBEthernetDevice`
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBEthernetDevice`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUSBEthernetDevice`
- `CFBundleNumericVersion`: `117473280`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `7.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `7.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2000-2013 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleUSBEthernetDevice.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896532208`
- `_PrelinkExecutableRelativePath`: `AppleUSBEthernetDevice`
- `_PrelinkExecutableSize`: `24766`
- `_PrelinkExecutableSourceAddr`: `-2198896532208`
- `_PrelinkKmodInfo`: `-2198828395440`

## Strings (73) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AppleUSBEthernetDevice::%s: device-mac-address not found for device in the device-tree, generating a fake one\n`
- `AppleUSBEthernetDevice::%s: Write pipe failed, result - %08x\n`
- `AppleUSBEthernetDevice::%s: failed to allocate read context\n`
- `12112112212221`
- `start`
- `AppleUSBEthernetDevice::%s: provider start failed\n`
- `AppleUSBEthernetDevice::%s: applying 0x%08x flags on interface\n`
- `sendLinkStatusToHost`
- `AppleUSBEthernetDevice::%s: Async Write returned error, %08x\n`
- `device-mac-address`
- `startBulkWrite`
- `bulkWriteComplete`
- `AppleUSBEthernetDeviceCommandPool`
- `site.AppleUSBEthernetDeviceCommandPool`
- `1211111212221212111111122121111111121122111112211111111111222`
- `AppleUSBEthernetDevice::%s: host-mac-address not found for host in the device-tree, generating a fake one\n`
- `AppleUSBEthernetDevice::%s: Read failed, %08x\n`
- `AppleUSBEthernetDevice::%s: invalid transfer size\n`
- `bulkWriteZlpComplete`
- `AppleUSBEthernetDevice::%s: provider is NULL\n`
- `AppleUSBEthernetDevice::%s: no device-mac-address present\n`
- `startBulkWriteZLP`
- `1`
- `AppleUSBEthernetDevice::%s: publishMediumDictionary failed \n`
- `AppleUSBEthernetDevice::%s: Unsupported property\n`
- `AppleUSBEthernetDevice::%s: memDesc is NULL\n`
- `AppleUSBEthernetDevice::%s: sendLinkStatusToHost failed\n`
- `AppleUSBEthernetDevice::%s: no connection\n`
- `AppleUSBEthernetDevice::%s: Write failed, %08x\n`
- `AppleUSBEthernetDevice::%s: Error: pending reads are zero %d\n`
- `bulkReadComplete`
- `site.IOCommand *`
- `AppleUSBEthernetDevice`
- `AppleUSBEthernetDevice::%s: createPipe failed for V3 Bulk OUT\n`
- `host-mac-address`
- `AppleUSBEthernetDevice::%s: can't create command gate\n`
- `AppleUSBEthernetDevice::%s: startBulkWriteZLP failed\n`
- `AppleUSBEthernetDevice::%s: Bulk ZLP write failed, result - %08x\n`
- `site.AppleUSBEthernetDevice`
- `hw.memsize`
- `LinkStatus`
- `AppleUSBEthernetDevice::%s: failed to start bulk read, dropping \n`
- `site.AppleUSBEthernetDeviceCommand`
- `handleControlRequest`
- `startBulkReadGated`
- `AppleUSBEthernetDevice::%s: Error: read context is NULL!\n`
- `AppleUSBEthernetDevice::%s: attachInterface failed\n`
- `AppleUSBEthernetDevice::%s: Async Write ZLP returned error, %08x\n`
- `usb-eth-nomac`
- `AppleUSBEthernetDevice::%s: createPipe failed for V%d Bulk IN\n`
- `AppleUSBEthernetDevice::%s: failed to allocate Link Status MD\n`
- `AppleUSBEthernetDevice::%s: failed to add mCommandGate to work-loop\n`
- `HostAttached`
- `outputStart`
- `restart_cmds`
- `AppleUSBEthernetDevice::%s: no host-mac-address present\n`
- `AppleUSBEthernetDevice::%s: Empty dictionary\n`
- `IONetworkStatsKey`
- `outputStartNCMLite`
- `AppleUSBEthernetDevice::%s: ZLP  failed, result - %08x\n`
- `startBulkRead`
- `AppleUSBEthernetDevice::%s: Async Read returned error, %08x\n`
- `AppleUSBEthernetDeviceCommand`
- `121111112`
- `AppleUSBEthernetDevice::%s: addAltSetting %d failed\n`
- `AppleUSBEthernetDevice::%s: failed to send link status to host \n`
- `AppleUSBEthernetDevice::%s: mbuf length > %d, dropping packet\n`
- `AppleUSBEthernetDevice::%s: Error: pending writes are zero %d\n`
- `setPropertiesGated`
- `AppleUSBEthernetDevice::%s: unable to acquire ifnet pointer\n`
- `InterfaceFlags`
- `AppleUSBEthernetDevice::%s: Bulk write failed, result - %08x\n`
- `AppleUSBEthernet`
