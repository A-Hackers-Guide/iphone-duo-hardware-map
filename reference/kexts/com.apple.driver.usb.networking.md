# `com.apple.driver.usb.networking`

- Name: AppleUSBNetworking
- Version: `5.0.0`
- UUID: `26D1DEAA-36B3-3A58-B60E-19BF0153C80F`
- Source version: `404.40.4.0.0`
- Depends on: [`com.apple.iokit.IONetworkingFamily`](com.apple.iokit.IONetworkingFamily.md) 3.3, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.0.1, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 14.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 14.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 14.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBNetworkingCommand` | 0x38 | IOCommand |
| `AppleUSBNetworkingCommandPool` | 0x50 | IOCommandPool |
| `AppleUSBNetworkingHostCommandPool` | 0x58 | AppleUSBNetworkingCommandPool → IOCommandPool |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000c97 off=0x008df990-0x008e0627 addr=0xfffffe00078e3990-0xfffffe00078e4627 r--/r--   __TEXT            
	sz=0x00000010 off=0x008dffb8-0x008dffc8 addr=0xfffffe00078e3fb8-0xfffffe00078e3fc8               __TEXT.__const            
	sz=0x0000065f off=0x008dffc8-0x008e0627 addr=0xfffffe00078e3fc8-0xfffffe00078e4627               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00003e94 off=0x02b5f220-0x02b630b4 addr=0xfffffe0009b63220-0xfffffe0009b670b4 r-x/r-x   __TEXT_EXEC       
	sz=0x00003c44 off=0x02b5f220-0x02b62e64 addr=0xfffffe0009b63220-0xfffffe0009b66e64          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000250 off=0x02b62e64-0x02b630b4 addr=0xfffffe0009b66e64-0xfffffe0009b670b4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000150 off=0x049d1c08-0x049d1d58 addr=0xfffffe000b9d5c08-0xfffffe000b9d5d58 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049d1c08-0x049d1cd0 addr=0xfffffe000b9d5c08-0xfffffe000b9d5cd0               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000b9d5cd0-0xfffffe000b9d5d58               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000690 off=0x012b28d0-0x012b2f60 addr=0xfffffe00082b68d0-0xfffffe00082b6f60 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x012b28d0-0x012b28d8 addr=0xfffffe00082b68d0-0xfffffe00082b68d8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x012b28d8-0x012b28e0 addr=0xfffffe00082b68d8-0xfffffe00082b68e0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000460 off=0x012b28e0-0x012b2d40 addr=0xfffffe00082b68e0-0xfffffe00082b6d40         __DATA_CONST.__const            
	sz=0x000000c0 off=0x012b2d40-0x012b2e00 addr=0xfffffe00082b6d40-0xfffffe00082b6e00         __DATA_CONST.__kalloc_type      
	sz=0x00000128 off=0x012b2e00-0x012b2f28 addr=0xfffffe00082b6e00-0xfffffe00082b6f28         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000038 off=0x012b2f28-0x012b2f60 addr=0xfffffe00082b6f28-0xfffffe00082b6f60         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 81 at 0x04aecc4c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     26D1DEAA-36B3-3A58-B60E-19BF0153C80F
008: LC_SOURCE_VERSION           404.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab7ca0 size=0xc0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleUSBNetworking`
- `CFBundleIdentifier`: `com.apple.driver.usb.networking`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUSBNetworking`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleUSBNetworking.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896494192`
- `_PrelinkExecutableRelativePath`: `AppleUSBNetworking`
- `_PrelinkExecutableSize`: `21259`
- `_PrelinkExecutableSourceAddr`: `-2198896494192`
- `_PrelinkKmodInfo`: `-2198828393464`

## Strings (53) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%s  WARNING: Feature descriptor %u has invalid length %u (minimum %u)\n`
- `%s  WARNING: Feature descriptor %u extends beyond buffer (offset %u + length %u > buffer %u)\n`
- `IOInterfaceUnit`
- `nameBSDInterface`
- ` %s() [%s %d] returning 0x%08x\n`
- `enableBSDInterface`
- ` %s() [%s], IPv6 %s returning 0x%08x\n`
- `configureIPv6LLOnBSDInterface`
- `site.AppleUSBNetworkingHostCommandPool`
- `12112112211`
- `site.AppleUSBNetworkingCommand`
- `1211111`
- `%s  bLength: %u\n`
- `%s    WARNING: Unexpected descriptor subtype (expected 0x%02x)\n`
- `%s  Additional data (%u bytes): `
- `%s  wTotalLength: %u\n`
- `%s  WARNING: Unexpected descriptor type (expected 0x%02x)\n`
- `%s  WARNING: Not enough data for feature descriptor %u at offset %u\n`
- `%sTotal feature descriptors found: %u\n`
- `IONetworkStack`
- `...`
- `%s  WARNING: Buffer length (%u) smaller than total descriptor length (%u)\n`
- `disable`
- `disableTrafficShapingOnBSDInterface`
- `AppleUSBNetworkingCommandPool`
- `1211211221`
- ` (Wake)\n`
- ` (Unknown)\n`
- `\n`
- `%s  WARNING: Descriptor length too small (minimum %u)\n`
- ` %s() [%s], size %u returning 0x%08x\n`
- `configureDatagramSizeOnBSDInterface`
- ` %s() [%s], disable traffic shaping returning 0x%08x\n`
- `AppleUSBNetworkingHostCommandPool`
- ` (Transmit Offload)\n`
- `%02x `
- `IOPathMatch`
- `%s%d`
- `enable`
- `site.AppleUSBNetworkingCommandPool`
- `AppleUSBNetworkingCommand`
- `%s  bDescriptorSubtype: 0x%02x\n`
- ` (Receive Offload)\n`
- `%sNCM Extended Feature Descriptor %u:\n`
- `%s  bDescriptorType: 0x%02x\n`
- ` (Medium Handling)\n`
- `%sNCM Extended Capability Descriptor:\n`
- `NONE`
- ` %s() [%s], returning 0x%08x\n`
- `%s  bNcmFeatureSelector: 0x%02x`
- ` (Presence Offload)\n`
- `%s    WARNING: Unexpected descriptor type (expected 0x%02x)\n`
- `%s  WARNING: Unexpected descriptor subtype (expected 0x%02x)\n`
