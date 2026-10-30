# `com.apple.driver.DCPDPFamilyProxy`

- Name: DCPDPFamilyProxy
- Version: `1`
- UUID: `4455D384-1884-33DE-8443-8E19900EE038`
- Source version: `301.40.3.0.0`
- Depends on: [`com.apple.driver.AppleFirmwareKit`](com.apple.driver.AppleFirmwareKit.md) 1.0.0, [`com.apple.driver.DCPAVFamilyProxy`](com.apple.driver.DCPAVFamilyProxy.md) 1.0.0, [`com.apple.iokit.IOAVFamily`](com.apple.iokit.IOAVFamily.md) 1.0, [`com.apple.iokit.IODisplayPortFamily`](com.apple.iokit.IODisplayPortFamily.md) 1.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (3) [KC]

### DCPDPControllerProxy
- `CFBundleIdentifier`: `com.apple.driver.DCPDPFamilyProxy`
- `IOClass`: `DCPDPControllerProxy`
- `IOPersonalityPublisher`: `com.apple.driver.DCPDPFamilyProxy`
- `IOPropertyMatch`:
  - `EPICName`: `dcpdp-controller-epic`
- `IOProviderClass`: `AFKEndpointInterface`

### DCPDPDeviceProxy
- `CFBundleIdentifier`: `com.apple.driver.DCPDPFamilyProxy`
- `IOClass`: `DCPDPDeviceProxy`
- `IOPersonalityPublisher`: `com.apple.driver.DCPDPFamilyProxy`
- `IOPropertyMatch`:
  - `EPICName`: `dcpdp-device-epic`
- `IOProviderClass`: `AFKEndpointInterface`

### DCPDPServiceProxy
- `CFBundleIdentifier`: `com.apple.driver.DCPDPFamilyProxy`
- `IOClass`: `DCPDPServiceProxy`
- `IOPersonalityPublisher`: `com.apple.driver.DCPDPFamilyProxy`
- `IOPropertyMatch`:
  - `EPICName`: `dcpdp-service-epic`
- `IOProviderClass`: `AFKEndpointInterface`


## C++ classes (6) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `DCPDPControllerProxy` | 0x618 | DCPAVProxy → IOService → IORegistryEntry |
| `DCPDPControllerProxyUserClient` | 0x108 | IODPControllerUserClient → IOAVUserClient → IOUserClient → IOService → IORegistryEntry |
| `DCPDPDeviceProxy` | 0x618 | DCPAVProxy → IOService → IORegistryEntry |
| `DCPDPDeviceProxyUserClient` | 0x108 | IODPDeviceUserClient → IOAVUserClient → IOUserClient → IOService → IORegistryEntry |
| `DCPDPServiceProxy` | 0x618 | DCPAVProxy → IOService → IORegistryEntry |
| `DCPDPServiceProxyUserClient` | 0x108 | IODPServiceUserClient → IOAVUserClient → IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000bd8 off=0x00916130-0x00916d08 addr=0xfffffe000791a130-0xfffffe000791ad08 r--/r--   __TEXT            
	sz=0x00000090 off=0x009167a8-0x00916838 addr=0xfffffe000791a7a8-0xfffffe000791a838               __TEXT.__const            
	sz=0x000003b8 off=0x00916838-0x00916bf0 addr=0xfffffe000791a838-0xfffffe000791abf0               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000118 off=0x00916bf0-0x00916d08 addr=0xfffffe000791abf0-0xfffffe000791ad08               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00004108 off=0x02c2a1f0-0x02c2e2f8 addr=0xfffffe0009c2e1f0-0xfffffe0009c322f8 r-x/r-x   __TEXT_EXEC       
	sz=0x00003ee8 off=0x02c2a1f0-0x02c2e0d8 addr=0xfffffe0009c2e1f0-0xfffffe0009c320d8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000220 off=0x02c2e0d8-0x02c2e2f8 addr=0xfffffe0009c320d8-0xfffffe0009c322f8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001c8 off=0x049db928-0x049dbaf0 addr=0xfffffe000b9df928-0xfffffe000b9dfaf0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049db928-0x049db9f0 addr=0xfffffe000b9df928-0xfffffe000b9df9f0               __DATA.__data             
	sz=0x00000100 off=0x00000000-0x00000100 addr=0xfffffe000b9df9f0-0xfffffe000b9dfaf0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00002c48 off=0x012d2218-0x012d4e60 addr=0xfffffe00082d6218-0xfffffe00082d8e60 rw-/rw-   __DATA_CONST      
	sz=0x00000030 off=0x012d2218-0x012d2248 addr=0xfffffe00082d6218-0xfffffe00082d6248         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000030 off=0x012d2248-0x012d2278 addr=0xfffffe00082d6248-0xfffffe00082d6278         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000028d8 off=0x012d2278-0x012d4b50 addr=0xfffffe00082d6278-0xfffffe00082d8b50         __DATA_CONST.__const            
	sz=0x00000180 off=0x012d4b50-0x012d4cd0 addr=0xfffffe00082d8b50-0xfffffe00082d8cd0         __DATA_CONST.__kalloc_type      
	sz=0x00000110 off=0x012d4cd0-0x012d4de0 addr=0xfffffe00082d8cd0-0xfffffe00082d8de0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000080 off=0x012d4de0-0x012d4e60 addr=0xfffffe00082d8de0-0xfffffe00082d8e60         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 84 at 0x04aee1cc
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     4455D384-1884-33DE-8443-8E19900EE038
008: LC_SOURCE_VERSION           301.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab95c0 size=0x108
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `DCPDPFamilyProxy`
- `CFBundleIdentifier`: `com.apple.driver.DCPDPFamilyProxy`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `DCPDPFamilyProxy`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/DCPDPFamilyProxy.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896271056`
- `_PrelinkExecutableRelativePath`: `DCPDPFamilyProxy`
- `_PrelinkExecutableSize`: `31472`
- `_PrelinkExecutableSourceAddr`: `-2198896271056`
- `_PrelinkKmodInfo`: `-2198828353240`

## Strings (32) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.DCPDPDeviceProxy`
- `Unable to convert branch deviceID to OSString\n`
- `setMaxLaneCount`
- `<rdar://problem/67769074> Re-enable DCPDPControllerProxy::setMaxLaneCount() (fix 'displayPort -maxlc')\n`
- `121111121222121211111111111112111`
- `DCPDPDeviceProxyUserClient`
- `site.DCPDPDeviceProxyUserClient`
- `start`
- `SinkDeviceID`
- `site.DCPDPServiceProxyUserClient`
- `site.DCPDPServiceProxy`
- `/product`
- `coverglass-serial-number`
- `IOUserClientClass`
- `DCPDPDeviceProxy`
- `BranchIEEEOUI`
- `Unable to convert sink deviceID to OSString for sink\n`
- `DCPDPControllerProxy`
- `121111121222121211222221122122111121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212221`
- `DCPDPControllerProxyUserClient`
- `site.DCPDPControllerProxyUserClient`
- `color-accuracy-index-key`
- `BranchDeviceID`
- `SinkIEEEOUI`
- `DCPDPServiceProxy`
- `color-accuracy-index`
- `site.DCPDPControllerProxy`
- `DCPDPServiceProxyUserClient`
- `coverglass-serial-number-key`

**[__TEXT.__os_log]**

- `IOAV[%d] %s<0x%llx>::%s: Unable to convert branch deviceID to OSString\n`
- `IOAV[%d] %s<0x%llx>::%s: Unable to convert sink deviceID to OSString for sink\n`
- `IOAV[%d] %s<0x%llx>::%s: <rdar://problem/67769074> Re-enable DCPDPControllerProxy::setMaxLaneCount() (fix 'displayPort -maxlc')\n`
