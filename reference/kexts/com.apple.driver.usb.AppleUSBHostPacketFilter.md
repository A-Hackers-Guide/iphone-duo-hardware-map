# `com.apple.driver.usb.AppleUSBHostPacketFilter`

- Name: USB Packet Filter
- Version: `1.0`
- UUID: `8C2F3236-7D58-3A3A-900D-038AA9731F60`
- Source version: `1617.40.10.0.0`
- Depends on: [`com.apple.driver.usb.AppleUSBCommon`](com.apple.driver.usb.AppleUSBCommon.md) 1.0, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.2, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 23.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 23.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 23.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 23.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 23.0.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 23.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleUSBHostPacketFilter
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHostPacketFilter`
- `IOClass`: `AppleUSBHostPacketFilter`
- `IOMatchCategory`: `AppleUSBHostPacketFilter`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHostPacketFilter`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOBSD`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBHostPacketFilter` | 0x88 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000011e9 off=0x00b510d0-0x00b522b9 addr=0xfffffe0007b550d0-0xfffffe0007b562b9 r--/r--   __TEXT            
	sz=0x00000018 off=0x00b51798-0x00b517b0 addr=0xfffffe0007b55798-0xfffffe0007b557b0               __TEXT.__const            
	sz=0x00000a5a off=0x00b517b0-0x00b5220a addr=0xfffffe0007b557b0-0xfffffe0007b5620a               __TEXT.__cstring          (CstringLiterals)
	sz=0x000000af off=0x00b5220a-0x00b522b9 addr=0xfffffe0007b5620a-0xfffffe0007b562b9               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00001eb4 off=0x037ef4e0-0x037f1394 addr=0xfffffe000a7f34e0-0xfffffe000a7f5394 r-x/r-x   __TEXT_EXEC       
	sz=0x00001c34 off=0x037ef4e0-0x037f1114 addr=0xfffffe000a7f34e0-0xfffffe000a7f5114          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000280 off=0x037f1114-0x037f1394 addr=0xfffffe000a7f5114-0xfffffe000a7f5394          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000120 off=0x04a1c020-0x04a1c140 addr=0xfffffe000ba20020-0xfffffe000ba20140 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a1c020-0x04a1c0e8 addr=0xfffffe000ba20020-0xfffffe000ba200e8               __DATA.__data             
	sz=0x00000048 off=0x00000000-0x00000048 addr=0xfffffe000ba200e8-0xfffffe000ba20130               __DATA.__common           (Zerofill)
	sz=0x00000010 off=0x00000000-0x00000010 addr=0xfffffe000ba20130-0xfffffe000ba20140               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000008b8 off=0x01463d90-0x01464648 addr=0xfffffe0008467d90-0xfffffe0008468648 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01463d90-0x01463d98 addr=0xfffffe0008467d90-0xfffffe0008467d98         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01463d98-0x01463da0 addr=0xfffffe0008467d98-0xfffffe0008467da0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000005f0 off=0x01463da0-0x01464390 addr=0xfffffe0008467da0-0xfffffe0008468390         __DATA_CONST.__const            
	sz=0x00000140 off=0x01464390-0x014644d0 addr=0xfffffe0008468390-0xfffffe00084684d0         __DATA_CONST.__kalloc_type      
	sz=0x00000140 off=0x014644d0-0x01464610 addr=0xfffffe00084684d0-0xfffffe0008468610         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000038 off=0x01464610-0x01464648 addr=0xfffffe0008468610-0xfffffe0008468648         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 87 at 0x04afae58
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     8C2F3236-7D58-3A3A-900D-038AA9731F60
008: LC_SOURCE_VERSION           1617.40.10.0.0
009: LC_FUNCTION_STARTS          offset=0x004aca040 size=0x38
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleUSBHostPacketFilter`
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHostPacketFilter`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `USB Packet Filter`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
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
- `NSHumanReadableCopyright`: `Copyright © 2000-2016 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/AppleUSBHostPacketFilter.kext`
- `_PrelinkExecutableLoadAddr`: `-2198893932336`
- `_PrelinkExecutableRelativePath`: `AppleUSBHostPacketFilter`
- `_PrelinkExecutableSize`: `14965`
- `_PrelinkExecutableSourceAddr`: `-2198893932336`
- `_PrelinkKmodInfo`: `-2198828089312`

## Strings (34) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `packetFilterInterfaceAddProto`
- `site.AppleUSBHostPacketFilter`
- `AppleUSBHostController`
- `AppleUSBVHCI`
- `OHC`
- `packetFilterInterfaceDemux`
- `AppleUSBHostPacketFilter`
- `UHC`
- `freePacketFilterInterface`
- `site.AppleUSBHostPacketFilterInterfaceQueue`
- `AppleUSBOHCI`
- `AppleUSBXHCI`
- `packetFilterInterfaceOutput`
- `AppleUSBEHCI`
- `12111112122212121`
- `UserHC`
- `usb-filter-debug`
- `%06lu.%06u %s::%s: protocol already set on %s%d\n`
- `1`
- `locationID`
- `EHC`
- `%s%d`
- `%06lu.%06u %s::%s: \n`
- `AppleUSBUHCI`
- `212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `AppleUSBHostPacketFilterInterface`
- `packetFilterInterfaceDelProto`
- `packetFilterInterfaceIoctl`
- `AppleUSBUserHCI`
- `XHC`
- `VHC`
- `site.AppleUSBHostPacketFilterInterface`

**[__TEXT.__os_log]**

- `%06lu.%06u %s::%s: \n`
- `%06lu.%06u %s::%s: protocol already set on %s%d\n`
