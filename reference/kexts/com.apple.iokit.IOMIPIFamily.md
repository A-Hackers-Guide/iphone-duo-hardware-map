# `com.apple.iokit.IOMIPIFamily`

- Name: DCPMIPIProxy
- Version: `1`
- UUID: `BC89D73B-568B-3C98-A7BE-E762FA0B5E2A`
- Source version: `216.40.3.0.0`
- Depends on: [`com.apple.driver.AppleFirmwareKit`](com.apple.driver.AppleFirmwareKit.md) 1.0.0, [`com.apple.driver.DCPAVFamilyProxy`](com.apple.driver.DCPAVFamilyProxy.md) 1.0.0, [`com.apple.iokit.IOAVFamily`](com.apple.iokit.IOAVFamily.md) 1.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### AppleDCPMIPIRemotePowerController
- `CFBundleIdentifier`: `com.apple.iokit.IOMIPIFamily`
- `IOClass`: `AppleDCPMIPIRemotePowerController`
- `IONameMatch`: `dcp-mipi-power-controller`
- `IOPersonalityPublisher`: `com.apple.iokit.IOMIPIFamily`
- `IOProviderClass`: `IOService`

### DCPMIPIControllerProxy
- `CFBundleIdentifier`: `com.apple.iokit.IOMIPIFamily`
- `IOClass`: `DCPMIPIControllerProxy`
- `IOPersonalityPublisher`: `com.apple.iokit.IOMIPIFamily`
- `IOPropertyMatch`:
  - `EPICName`: `dcpmipi-controller-epic`
- `IOProviderClass`: `AFKEndpointInterface`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleDCPMIPIRemotePowerController` | 0xa8 | DCPAVRemotePowerController → IOService → IORegistryEntry |
| `DCPMIPIControllerProxy` | 0x650 | DCPAVProxy → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000a77 off=0x00916d10-0x00917787 addr=0xfffffe000791ad10-0xfffffe000791b787 r--/r--   __TEXT            
	sz=0x00000030 off=0x00917338-0x00917368 addr=0xfffffe000791b338-0xfffffe000791b368               __TEXT.__const            
	sz=0x0000041f off=0x00917368-0x00917787 addr=0xfffffe000791b368-0xfffffe000791b787               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00001a34 off=0x02c2e300-0x02c2fd34 addr=0xfffffe0009c32300-0xfffffe0009c33d34 r-x/r-x   __TEXT_EXEC       
	sz=0x00001894 off=0x02c2e300-0x02c2fb94 addr=0xfffffe0009c32300-0xfffffe0009c33b94          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001a0 off=0x02c2fb94-0x02c2fd34 addr=0xfffffe0009c33b94-0xfffffe0009c33d34          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x049dbaf0-0x049dbc18 addr=0xfffffe000b9dfaf0-0xfffffe000b9dfc18 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049dbaf0-0x049dbbb8 addr=0xfffffe000b9dfaf0-0xfffffe000b9dfbb8               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b9dfbb8-0xfffffe000b9dfc18               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000e80 off=0x012d4e60-0x012d5ce0 addr=0xfffffe00082d8e60-0xfffffe00082d9ce0 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x012d4e60-0x012d4e70 addr=0xfffffe00082d8e60-0xfffffe00082d8e70         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x012d4e70-0x012d4e80 addr=0xfffffe00082d8e70-0xfffffe00082d8e80         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000cd0 off=0x012d4e80-0x012d5b50 addr=0xfffffe00082d8e80-0xfffffe00082d9b50         __DATA_CONST.__const            
	sz=0x00000080 off=0x012d5b50-0x012d5bd0 addr=0xfffffe00082d9b50-0xfffffe00082d9bd0         __DATA_CONST.__kalloc_type      
	sz=0x000000d0 off=0x012d5bd0-0x012d5ca0 addr=0xfffffe00082d9bd0-0xfffffe00082d9ca0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000040 off=0x012d5ca0-0x012d5ce0 addr=0xfffffe00082d9ca0-0xfffffe00082d9ce0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 60 at 0x04aee31c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     BC89D73B-568B-3C98-A7BE-E762FA0B5E2A
008: LC_SOURCE_VERSION           216.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab96c8 size=0x58
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `DCPMIPIProxy`
- `CFBundleIdentifier`: `com.apple.iokit.IOMIPIFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `DCPMIPIProxy`
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
- `NSHumanReadableCopyright`: `Copyright © 2019-2021 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/DCPMIPIProxy.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896268016`
- `_PrelinkExecutableRelativePath`: `DCPMIPIProxy`
- `_PrelinkExecutableSize`: `13395`
- `_PrelinkExecutableSourceAddr`: `-2198896268016`
- `_PrelinkKmodInfo`: `-2198828352784`

## Strings (35) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `ESD interrupt detected! Debouncing... %d/%d\n`
- `DCP requested ESD interrupt %s\n`
- `\"super::start() failed\" @%s:%d`
- `ESD INT went Lo. hiCount=%d\n`
- `dispatch ESD msg failed: 0x%x\n`
- `ESD interrupt is LO, panel auto-recovered\n`
- `\"_lcdLDOFunction null\" @%s:%d`
- `HI`
- `function-esd`
- `LO`
- `ESD trigger failed: 0x%x\n`
- `1211111212221212112222211221221111212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112122211111222`
- `mipi-command`
- `Valid`
- `ESD interrupt is HI, triggering recovery\n`
- `DCPMIPIControllerProxy`
- `site.DCPMIPIControllerProxy`
- `MIPIESDInterruptEnable`
- `esd-debounce-hi`
- `mipi-receive-data`
- `ESD Interrupt enable requested while interrupt is HIGH!\n`
- `AppleDCPMIPIRemotePowerController`
- `AppleDCPMIPIRemotePowerController.cpp`
- `esd-debounce-lo`
- `Initialized ESD gpio with debounce values %d/%d\n`
- `121111121222121211111`
- `site.AppleDCPMIPIRemotePowerController`
- `function-lcd_ldo`
- `esd-gpio`
- `ESD INT went Hi. loCount=%d\n`
- `Enable`
- `Disable`
- `mipi-send-data`
- `ESD interrupt ignored: pin is %s / thread is %s\n`
- `INVALID`
