# `com.apple.driver.usb.AppleUSBHostDeviceSupport`

- Name: AppleUSBHostDeviceSupport
- Version: `1.0`
- UUID: `EB08F9AE-3B52-3191-B229-0F10AB86CE6F`
- Source version: `1617.40.10.0.0`
- Depends on: [`com.apple.driver.usb.AppleUSBCommon`](com.apple.driver.usb.AppleUSBCommon.md) 1.0, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.2, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 23.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 23.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 23.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 23.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 23.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### Apple USB-C Digital AV Multiport Adapter
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHostDeviceSupport`
- `IOClass`: `AppleUSBHostDeviceSupport`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHostDeviceSupport`
- `IOProbeScore`: `10000`
- `IOProviderClass`: `IOUSBHostDevice`
- `USBSpeed`: `1`
- `idProductArray`:
  - `4111`
  - `4113`
- `idVendor`: `1452`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBHostDeviceSupport` | 0x90 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000753 off=0x00b502b0-0x00b50a03 addr=0xfffffe0007b542b0-0xfffffe0007b54a03 r--/r--   __TEXT            
	sz=0x000000c8 off=0x00b508d8-0x00b509a0 addr=0xfffffe0007b548d8-0xfffffe0007b549a0               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000063 off=0x00b509a0-0x00b50a03 addr=0xfffffe0007b549a0-0xfffffe0007b54a03               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x000008e4 off=0x037ee120-0x037eea04 addr=0xfffffe000a7f2120-0xfffffe000a7f2a04 r-x/r-x   __TEXT_EXEC       
	sz=0x00000814 off=0x037ee120-0x037ee934 addr=0xfffffe000a7f2120-0xfffffe000a7f2934          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000000d0 off=0x037ee934-0x037eea04 addr=0xfffffe000a7f2934-0xfffffe000a7f2a04          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x04a1be18-0x04a1bf18 addr=0xfffffe000ba1fe18-0xfffffe000ba1ff18 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a1be18-0x04a1bee0 addr=0xfffffe000ba1fe18-0xfffffe000ba1fee0               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000ba1fee0-0xfffffe000ba1ff18               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000006d8 off=0x01462ff0-0x014636c8 addr=0xfffffe0008466ff0-0xfffffe00084676c8 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01462ff0-0x01462ff8 addr=0xfffffe0008466ff0-0xfffffe0008466ff8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01462ff8-0x01463000 addr=0xfffffe0008466ff8-0xfffffe0008467000         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000005f0 off=0x01463000-0x014635f0 addr=0xfffffe0008467000-0xfffffe00084675f0         __DATA_CONST.__const            
	sz=0x00000040 off=0x014635f0-0x01463630 addr=0xfffffe00084675f0-0xfffffe0008467630         __DATA_CONST.__kalloc_type      
	sz=0x00000068 off=0x01463630-0x01463698 addr=0xfffffe0008467630-0xfffffe0008467698         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000030 off=0x01463698-0x014636c8 addr=0xfffffe0008467698-0xfffffe00084676c8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 32 at 0x04afad74
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     EB08F9AE-3B52-3191-B229-0F10AB86CE6F
008: LC_SOURCE_VERSION           1617.40.10.0.0
009: LC_FUNCTION_STARTS          offset=0x004aca000 size=0x20
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleUSBHostDeviceSupport`
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHostDeviceSupport`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUSBHostDeviceSupport`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.2`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0`
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
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/AppleUSBHostDeviceSupport.kext`
- `_PrelinkExecutableLoadAddr`: `-2198893935952`
- `_PrelinkExecutableRelativePath`: `AppleUSBHostDeviceSupport`
- `_PrelinkExecutableSize`: `6159`
- `_PrelinkExecutableSourceAddr`: `-2198893935952`
- `_PrelinkKmodInfo`: `-2198828089832`

## Strings (8) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `idProduct`
- `%s: %s::%s: USB Device 0x%04x/%04x (%s) is incorrectly operating at full speed. Reset the device.\n`
- `probe`
- `AppleUSBHostDeviceSupport`
- `site.AppleUSBHostDeviceSupport`
- `121111121222121212`
- `idVendor`

**[__TEXT.__os_log]**

- `%s: %s::%s: USB Device 0x%04x/%04x (%s) is incorrectly operating at full speed. Reset the device.\n`
