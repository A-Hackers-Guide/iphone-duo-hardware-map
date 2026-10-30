# `com.apple.driver.usb.AppleUSBHostiOSDevice`

- Name: AppleUSBHostiOSDevice
- Version: `1.0`
- UUID: `BFB68D85-75E1-36A4-B67D-7CD35C9B2AB3`
- Source version: `1617.40.10.0.0`
- Depends on: [`com.apple.driver.usb.AppleUSBCommon`](com.apple.driver.usb.AppleUSBCommon.md) 1.0, [`com.apple.driver.usb.AppleUSBHostCompositeDevice`](com.apple.driver.usb.AppleUSBHostCompositeDevice.md) 1.2, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.2, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 23.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 23.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 23.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 23.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 23.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleUSBHostiOSDevice
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHostiOSDevice`
- `IOClass`: `AppleUSBHostiOSDevice`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHostiOSDevice`
- `IOProbeScore`: `10000`
- `IOProviderClass`: `IOUSBHostDevice`
- `idProductArray`:
  - `4752`
  - `4768`
  - `4784`
- `idProductMask`: `65520`
- `idVendor`: `1452`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBHostiOSDevice` | 0xd0 | AppleUSBHostCompositeDevice → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000dfa off=0x00b522c0-0x00b530ba addr=0xfffffe0007b562c0-0xfffffe0007b570ba r--/r--   __TEXT            
	sz=0x00000008 off=0x00b52938-0x00b52940 addr=0xfffffe0007b56938-0xfffffe0007b56940               __TEXT.__const            
	sz=0x00000444 off=0x00b52940-0x00b52d84 addr=0xfffffe0007b56940-0xfffffe0007b56d84               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000336 off=0x00b52d84-0x00b530ba addr=0xfffffe0007b56d84-0xfffffe0007b570ba               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00001924 off=0x037f13a0-0x037f2cc4 addr=0xfffffe000a7f53a0-0xfffffe000a7f6cc4 r-x/r-x   __TEXT_EXEC       
	sz=0x00001844 off=0x037f13a0-0x037f2be4 addr=0xfffffe000a7f53a0-0xfffffe000a7f6be4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000000e0 off=0x037f2be4-0x037f2cc4 addr=0xfffffe000a7f6be4-0xfffffe000a7f6cc4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x04a1c140-0x04a1c240 addr=0xfffffe000ba20140-0xfffffe000ba20240 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a1c140-0x04a1c208 addr=0xfffffe000ba20140-0xfffffe000ba20208               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000ba20208-0xfffffe000ba20240               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000718 off=0x01464648-0x01464d60 addr=0xfffffe0008468648-0xfffffe0008468d60 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01464648-0x01464650 addr=0xfffffe0008468648-0xfffffe0008468650         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01464650-0x01464658 addr=0xfffffe0008468650-0xfffffe0008468658         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000620 off=0x01464658-0x01464c78 addr=0xfffffe0008468658-0xfffffe0008468c78         __DATA_CONST.__const            
	sz=0x00000040 off=0x01464c78-0x01464cb8 addr=0xfffffe0008468c78-0xfffffe0008468cb8         __DATA_CONST.__kalloc_type      
	sz=0x00000070 off=0x01464cb8-0x01464d28 addr=0xfffffe0008468cb8-0xfffffe0008468d28         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000038 off=0x01464d28-0x01464d60 addr=0xfffffe0008468d28-0xfffffe0008468d60         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 35 at 0x04afafb4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     BFB68D85-75E1-36A4-B67D-7CD35C9B2AB3
008: LC_SOURCE_VERSION           1617.40.10.0.0
009: LC_FUNCTION_STARTS          offset=0x004aca078 size=0x28
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleUSBHostiOSDevice`
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHostiOSDevice`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUSBHostiOSDevice`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/AppleUSBHostiOSDevice.kext`
- `_PrelinkExecutableLoadAddr`: `-2198893927744`
- `_PrelinkExecutableRelativePath`: `AppleUSBHostiOSDevice`
- `_PrelinkExecutableSize`: `12086`
- `_PrelinkExecutableSourceAddr`: `-2198893927744`
- `_PrelinkKmodInfo`: `-2198828089024`

## Strings (37) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `%s: %s::%s: fall back to host extended function preference %d\n`
- `%s: %s::%s: rejecting non-Apple device with vendor string: %s\n`
- `%s: %s::%s: preferred config %d\n`
- `%s: %s::%s: preferred config host %d device %d default %d device function %d\n`
- `%s: %s::%s: device extended function preference %d -> %d\n`
- `%s: %s::%s: device config preference %d -> %d\n`
- `%s: %s::%s: device does not support extended function %d, fall back to host config preference %d\n`
- `%s: %s::%s: device doesn't support the kAppleUSBVendorRequestPreferredConfig request\n`
- `%s: %s::%s: preferred config host %d device %d default %d\n`
- `%s: %s::%s: preferred config request completed with 0x%08x\n`
- `%s: %s::%s: host config preference %d -> %d\n`
- `%s: %s::%s: host config preference %d\n`
- `%s: %s::%s: device extended function preference %d\n`
- `%s: %s::%s: device config preference %d\n`

**[__TEXT.__cstring]**

- `AppleUSBHostiOSDevice`
- `kUSBVendorString`
- `probe`
- `getPreferredConfiguration`
- `%s: %s::%s: preferred config host %d device %d default %d\n`
- `%s: %s::%s: preferred config host %d device %d default %d device function %d\n`
- `%s: %s::%s: host config preference %d -> %d\n`
- `%s: %s::%s: device extended function preference %d -> %d\n`
- `%s: %s::%s: rejecting non-Apple device with vendor string: %s\n`
- `%s: %s::%s: device doesn't support the kAppleUSBVendorRequestPreferredConfig request\n`
- `%s: %s::%s: preferred config %d\n`
- `%s: %s::%s: device config preference %d -> %d\n`
- `%s: %s::%s: host config preference %d\n`
- `%s: %s::%s: device extended function preference %d\n`
- `%s: %s::%s: device config preference %d\n`
- `%s: %s::%s: fall back to host extended function preference %d\n`
- `12111112122212121121121112`
- `Apple`
- `v16@?0^{IOTimerEventSource=^^?i^{IOEventSource}^{OSObject}^?B^{IOWorkLoop}^v^{ExpansionData}^vQ^{ExpansionData}}8`
- `kUSBCurrentConfiguration`
- `%s: %s::%s: preferred config request completed with 0x%08x\n`
- `site.AppleUSBHostiOSDevice`
- `%s: %s::%s: device does not support extended function %d, fall back to host config preference %d\n`
