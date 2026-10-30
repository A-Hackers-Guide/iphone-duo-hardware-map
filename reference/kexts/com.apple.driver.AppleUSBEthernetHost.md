# `com.apple.driver.AppleUSBEthernetHost`

- Name: AppleUSBEthernetHost
- Version: `8.1.1`
- UUID: `86C6C731-489A-326D-A1D4-D313D628BF4D`
- Source version: `170.40.1.0.0`
- Depends on: [`com.apple.iokit.IONetworkingFamily`](com.apple.iokit.IONetworkingFamily.md) 3.0, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.0.1, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### AppleUSBEthernetHost
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBEthernetHost`
- `IOClass`: `AppleUSBEthernetHostAQM`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBEthernetHost`
- `IOProviderClass`: `IOUSBHostInterface`
- `bConfigurationValue`: `*`
- `bInterfaceClass`: `255`
- `bInterfaceNumber`: `*`
- `bInterfaceProtocol`: `1`
- `bInterfaceSubClass`: `253`
- `idProduct`: `4752`
- `idProductMask`: `65520`
- `idVendor`: `1452`

### AppleUSBEthernetHost2
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBEthernetHost`
- `IOClass`: `AppleUSBEthernetHostAQM`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBEthernetHost`
- `IOProviderClass`: `IOUSBHostInterface`
- `bConfigurationValue`: `*`
- `bInterfaceClass`: `255`
- `bInterfaceNumber`: `*`
- `bInterfaceProtocol`: `1`
- `bInterfaceSubClass`: `253`
- `idProduct`: `4768`
- `idProductMask`: `65520`
- `idVendor`: `1452`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBEthernetHost` | 0x1f8 | IOEthernetController → IONetworkController → IOService → IORegistryEntry |
| `AppleUSBEthernetHostAQM` | 0x1f8 | AppleUSBEthernetHost → IOEthernetController → IONetworkController → IOService → IORegistryEntry |
| `PacketMemoryDescriptorEx` | 0x30 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000011ec off=0x008d7770-0x008d895c addr=0xfffffe00078db770-0xfffffe00078dc95c r--/r--   __TEXT            
	sz=0x00000bc4 off=0x008d7d98-0x008d895c addr=0xfffffe00078dbd98-0xfffffe00078dc95c               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00003e60 off=0x02b42060-0x02b45ec0 addr=0xfffffe0009b46060-0xfffffe0009b49ec0 r-x/r-x   __TEXT_EXEC       
	sz=0x00003be0 off=0x02b42060-0x02b45c40 addr=0xfffffe0009b46060-0xfffffe0009b49c40          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000280 off=0x02b45c40-0x02b45ec0 addr=0xfffffe0009b49c40-0xfffffe0009b49ec0          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000214 off=0x049d15a0-0x049d17b4 addr=0xfffffe000b9d55a0-0xfffffe000b9d57b4 rw-/rw-   __DATA            
	sz=0x00000188 off=0x049d15a0-0x049d1728 addr=0xfffffe000b9d55a0-0xfffffe000b9d5728               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000b9d5728-0xfffffe000b9d57b0               __DATA.__common           (Zerofill)
	sz=0x00000004 off=0x00000000-0x00000004 addr=0xfffffe000b9d57b0-0xfffffe000b9d57b4               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000014b0 off=0x012ac9b0-0x012ade60 addr=0xfffffe00082b09b0-0xfffffe00082b1e60 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x012ac9b0-0x012ac9c0 addr=0xfffffe00082b09b0-0xfffffe00082b09c0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x012ac9c0-0x012ac9d0 addr=0xfffffe00082b09c0-0xfffffe00082b09d0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001258 off=0x012ac9d0-0x012adc28 addr=0xfffffe00082b09d0-0xfffffe00082b1c28         __DATA_CONST.__const            
	sz=0x000000c0 off=0x012adc28-0x012adce8 addr=0xfffffe00082b1c28-0xfffffe00082b1ce8         __DATA_CONST.__kalloc_type      
	sz=0x00000140 off=0x012adce8-0x012ade28 addr=0xfffffe00082b1ce8-0xfffffe00082b1e28         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000038 off=0x012ade28-0x012ade60 addr=0xfffffe00082b1e28-0xfffffe00082b1e60         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 87 at 0x04aec3dc
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     86C6C731-489A-326D-A1D4-D313D628BF4D
008: LC_SOURCE_VERSION           170.40.1.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab7930 size=0x98
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleUSBEthernetHost`
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBEthernetHost`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUSBEthernetHost`
- `CFBundleNumericVersion`: `135364608`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `8.1.1`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `8.1.1`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleUSBEthernetHost.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896527504`
- `_PrelinkExecutableRelativePath`: `AppleUSBEthernetHost`
- `_PrelinkExecutableSize`: `26384`
- `_PrelinkExecutableSourceAddr`: `-2198896527504`
- `_PrelinkKmodInfo`: `-2198828395104`

## Strings (66) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `IONetworkStatsKey`
- `AppleUSBEthernetHost::%s: failed to set alt interface 0, %08x\n`
- `AppleUSBEthernetHost::%s: intf is not enabled, dropping packet. Driver State: %u\n`
- `AppleUSBEthernetHost::%s: request failed, %08x\n`
- `startBulkReadGated`
- `AppleUSBEthernetHost::%s: Read complete returned, but mOutstandingIOCount was 0\n`
- `site.AppleUSBEthernetHostAQM`
- `AppleUSBEthernetHost::%s: provider start failed\n`
- `AppleUSBEthernetHost::%s: Could not allocate packet descriptor\n`
- `AppleUSBEthernetHost::%s: Unexpected refcon in bulkReadComplete`
- `\"failed to lock netif, status = 0x%08x\\n\" @%s:%d`
- `121112`
- `AppleUSBEthernetHost`
- `AppleUSBEthernetHost::%s: Interface already enabled\n`
- `AppleUSBEthernetHost::%s: Going into sleep mode\n`
- `AppleUSBEthernetHost::%s: can't create command gate`
- `AppleUSBEthernetHost::%s: No bulk out pipe\n`
- `disable`
- `getInterfaceFlags`
- `NetworkInterfaceFlags`
- `AppleUSBEthernetHost::%s: Async Write returned error, %08x\n`
- `AppleUSBEthernetHost::%s: intf is not enabled, ignoring ...  st: %llu\n`
- `Product Name`
- `AppleUSBEthernetHost::%s: Error: pending writes are zero %d\n`
- `AppleUSBEthernetHost::%s: provider is NULL\n`
- `AppleUSBEthernetHost::%s: interface open failed \n`
- `AppleUSBEthernetHost::%s: failed to get MAC address\n`
- `enable`
- `AppleUSBEthernetHost::%s: mOutstandingIOCount not 0, current value - %llu\n`
- `site.PacketMemoryDescriptorEx`
- `AppleUSBEthernetHost::%s: Async write retry failed\n`
- `powerStateChangeOccurred`
- `AppleUSBEthernetHost::%s: Interface seems to be gone, just return\n`
- `AppleUSBEthernetHost::%s: No bulk in pipe\n`
- `AppleUSBEthernetHost::%s: error waiting for IO abort completions [%d] - mOutstandingIOCount = %llu\n`
- `tryEnablingNCMEncapsulation`
- `startBulkWrite`
- `bulkWriteComplete`
- `AppleUSBEthernetHostAQM`
- `AppleUSBEthernetHost::%s: mbuf length > %d, dropping packet\n`
- `getHardwareEthernetAddress`
- `AppleUSBEthernetHost::%s: Could not allocate ZLP descriptor\n`
- `AppleUSBEthernetHost::%s: ZLP  failed, result - %08x\n`
- `AppleUSBEthernetHost::%s: Async Read returned error 0x%08x bytesRead 0x%08x\n`
- `AppleUSBEthernetHost::%s: unable to acquire ifnet pointer\n`
- `AppleUSBEthernetHost::%s: failed to start bulk read, dropping \n`
- `121111121222121211111112212111111112111111211122211122222221212`
- `AppleUSBEthernetHost::%s: can't allocate power change source\n`
- `AppleUSBEthernetHost::%s: publishMediumDictionary failed \n`
- `AppleUSBEthernetHost::%s: attachInterface failed\n`
- `AppleUSBEthernetHost::%s: Alt setting not selected yet, dropping packet.  Current Alt-setting: %d\n`
- `bulkReadComplete`
- `outputPacket`
- `AppleUSBEthernetHost::%s: Bulk write failed, result - %08x\n`
- `AppleUSBEthernetHost::%s: applying 0x%08x flags on interface\n`
- `AppleUSBEthernetHost::%s: Write complete returned, but mOutstandingIOCount was 0\n`
- `AppleUSBEthernetHost::%s: failed to add mPowerChangeSource to work-loop\n`
- `AppleUSBEthernetHost::%s: failed to set alt interface %d, %08x\n`
- `AppleUSBEthernetHost::%s: Read failed, %08x\n`
- `didTerminateGated`
- `AppleUSBEthernetHost.cpp`
- `PacketMemoryDescriptorEx`
- `site.AppleUSBEthernetHost`
- `getPreferredAltSetting`
- `AppleUSBEthernetHost::%s: Write pipe failed, result - %08x\n`
- `start`
