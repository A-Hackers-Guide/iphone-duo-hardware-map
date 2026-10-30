# `com.apple.driver.usb.cdc.ecm`

- Name: AppleUSBECM
- Version: `5.0.0`
- UUID: `C293D10D-C176-3900-8858-AD16FBDB7575`
- Source version: `404.40.4.0.0`
- Depends on: [`com.apple.driver.AppleUSBHostMergeProperties`](com.apple.driver.AppleUSBHostMergeProperties.md) 1.0, [`com.apple.driver.usb.cdc`](com.apple.driver.usb.cdc.md) 5.0, [`com.apple.driver.usb.networking`](com.apple.driver.usb.networking.md) 5.0, [`com.apple.iokit.IONetworkingFamily`](com.apple.iokit.IONetworkingFamily.md) 3.2, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.0.1, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 14.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 14.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (3) [KC]

### AppleUSBECMControl
- `CFBundleIdentifier`: `com.apple.driver.usb.cdc.ecm`
- `IOClass`: `AppleUSBECMControl`
- `IOMatchDefer`: `True`
- `IOPersonalityPublisher`: `com.apple.driver.usb.cdc.ecm`
- `IOProviderClass`: `IOUSBHostInterface`
- `bInterfaceClass`: `2`
- `bInterfaceProtocol`: `*`
- `bInterfaceSubClass`: `6`

### AppleUSBECMData0
- `CFBundleIdentifier`: `com.apple.driver.usb.cdc.ecm`
- `IOClass`: `AppleUSBECMData`
- `IOPersonalityPublisher`: `com.apple.driver.usb.cdc.ecm`
- `IOProviderClass`: `IOUSBHostInterface`
- `bInterfaceClass`: `10`
- `bInterfaceSubClass`: `0`
- `ioNetBootable`: `<data 16 chars>`

### AppleUSBECMData6
- `CFBundleIdentifier`: `com.apple.driver.usb.cdc.ecm`
- `IOClass`: `AppleUSBECMDataNC`
- `IOPersonalityPublisher`: `com.apple.driver.usb.cdc.ecm`
- `IOProviderClass`: `IOUSBHostInterface`
- `bInterfaceClass`: `10`
- `bInterfaceSubClass`: `6`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBECMControl` | 0x140 | AppleUSBCDCControl → IOService → IORegistryEntry |
| `AppleUSBECMData` | 0xcd0 | IOEthernetController → IONetworkController → IOService → IORegistryEntry |
| `AppleUSBECMDataNC` | 0xcd0 | AppleUSBECMData → IOEthernetController → IONetworkController → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000009cc off=0x008d4470-0x008d4e3c addr=0xfffffe00078d8470-0xfffffe00078d8e3c r--/r--   __TEXT            
	sz=0x0000032c off=0x008d4ae8-0x008d4e14 addr=0xfffffe00078d8ae8-0xfffffe00078d8e14               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000028 off=0x008d4e14-0x008d4e3c addr=0xfffffe00078d8e14-0xfffffe00078d8e3c               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00004048 off=0x02b2af80-0x02b2efc8 addr=0xfffffe0009b2ef80-0xfffffe0009b32fc8 r-x/r-x   __TEXT_EXEC       
	sz=0x00003d28 off=0x02b2af80-0x02b2eca8 addr=0xfffffe0009b2ef80-0xfffffe0009b32ca8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000320 off=0x02b2eca8-0x02b2efc8 addr=0xfffffe0009b32ca8-0xfffffe0009b32fc8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000274 off=0x049d0f08-0x049d117c addr=0xfffffe000b9d4f08-0xfffffe000b9d517c rw-/rw-   __DATA            
	sz=0x000001e8 off=0x049d0f08-0x049d10f0 addr=0xfffffe000b9d4f08-0xfffffe000b9d50f0               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000b9d50f0-0xfffffe000b9d5178               __DATA.__common           (Zerofill)
	sz=0x00000004 off=0x00000000-0x00000004 addr=0xfffffe000b9d5178-0xfffffe000b9d517c               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001af8 off=0x012a77d0-0x012a92c8 addr=0xfffffe00082ab7d0-0xfffffe00082ad2c8 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x012a77d0-0x012a77e8 addr=0xfffffe00082ab7d0-0xfffffe00082ab7e8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x012a77e8-0x012a7800 addr=0xfffffe00082ab7e8-0xfffffe00082ab800         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000017b8 off=0x012a7800-0x012a8fb8 addr=0xfffffe00082ab800-0xfffffe00082acfb8         __DATA_CONST.__const            
	sz=0x00000140 off=0x012a8fb8-0x012a90f8 addr=0xfffffe00082acfb8-0xfffffe00082ad0f8         __DATA_CONST.__kalloc_type      
	sz=0x00000190 off=0x012a90f8-0x012a9288 addr=0xfffffe00082ad0f8-0xfffffe00082ad288         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000040 off=0x012a9288-0x012a92c8 addr=0xfffffe00082ad288-0xfffffe00082ad2c8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 108 at 0x04aebea8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     C293D10D-C176-3900-8858-AD16FBDB7575
008: LC_SOURCE_VERSION           404.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab7638 size=0xb8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleUSBECM`
- `CFBundleIdentifier`: `com.apple.driver.usb.cdc.ecm`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUSBECM`
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
- `OSBundleCompatibleVersion`: `5.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleUSBECM.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896540560`
- `_PrelinkExecutableRelativePath`: `AppleUSBECM`
- `_PrelinkExecutableSize`: `26496`
- `_PrelinkExecutableSourceAddr`: `-2198896540560`
- `_PrelinkKmodInfo`: `-2198828396792`

## Strings (21) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AppleUSBECMControl`
- `USB Ethernet ECM`
- `USB`
- `IONetworkStatsKey`
- `site.OutputPipeRecordQueue`
- `ecm-data-debug`
- `Product Name`
- `%06lu.%06u %s::%s: status %#x\n`
- `\"failed to lock netif, status = 0x%08x\\n\" @%s:%d`
- `AppleUSBECMData.cpp`
- `site.AppleUSBECMControl`
- `ecm-ctrl-debug`
- `IOEthernetStatsKey`
- `1211111212221212111111211121121111222222`
- `site.AppleUSBECMDataNC`
- `site.AppleUSBECMData`
- `enable`
- `AppleUSBECMDataNC`
- `11`
- `AppleUSBECMData`
- `121111121222121211111112212111111111112112221121122111121111211112111121111211112111121111211112111121111211112111121111211112111121111211112111121111211112111121111211112111121111211112111121111211112111121111211112111112111112111112111112111112111112111112111112111112111112111112111112111112111112`
