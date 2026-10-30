# `com.apple.driver.AppleEmbeddedGPS`

- Name: AppleEmbeddedGPS
- Version: `1.0.0d1`
- UUID: `A517316A-D183-3ED5-BA1E-F9AE284B6FE5`
- Source version: `27.40.1.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### AppleBCM4750
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedGPS`
- `IOClass`: `AppleBCM4750`
- `IONameMatch`: `gps,bcm4750`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedGPS`
- `IOProviderClass`: `AppleARMIICDevice`

### AppleEmbeddedGPSControl
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedGPS`
- `IOClass`: `AppleEmbeddedGPSControl`
- `IOMatchCategory`: `AppleEmbeddedGPSControl`
- `IONameMatch`:
  - `gps,bcm4750`
  - `gps,bcm4773`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedGPS`
- `IOProviderClass`: `IOService`
- `IOUserClientClass`: `AppleEmbeddedGPSControlUserClient`


## C++ classes (4) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleBCM4750` | 0x518 | AppleEmbeddedI2CGPS → IOService → IORegistryEntry |
| `AppleEmbeddedGPSControl` | 0x100 | IOService → IORegistryEntry |
| `AppleEmbeddedGPSControlUserClient` | 0xe0 | IOUserClient → IOService → IORegistryEntry |
| `AppleEmbeddedI2CGPS` | 0x500 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000a39 off=0x00448b30-0x00449569 addr=0xfffffe000744cb30-0xfffffe000744d569 r--/r--   __TEXT            
	sz=0x00000411 off=0x00449158-0x00449569 addr=0xfffffe000744d158-0xfffffe000744d569               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00003798 off=0x01c2ad70-0x01c2e508 addr=0xfffffe0008c2ed70-0xfffffe0008c32508 r-x/r-x   __TEXT_EXEC       
	sz=0x000034f8 off=0x01c2ad70-0x01c2e268 addr=0xfffffe0008c2ed70-0xfffffe0008c32268          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000002a0 off=0x01c2e268-0x01c2e508 addr=0xfffffe0008c32268-0xfffffe0008c32508          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000201 off=0x0493ec08-0x0493ee09 addr=0xfffffe000b942c08-0xfffffe000b942e09 rw-/rw-   __DATA            
	sz=0x00000140 off=0x0493ec08-0x0493ed48 addr=0xfffffe000b942c08-0xfffffe000b942d48               __DATA.__data             
	sz=0x000000c0 off=0x00000000-0x000000c0 addr=0xfffffe000b942d48-0xfffffe000b942e08               __DATA.__common           (Zerofill)
	sz=0x00000001 off=0x00000000-0x00000001 addr=0xfffffe000b942e08-0xfffffe000b942e09               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001c18 off=0x0107cff8-0x0107ec10 addr=0xfffffe0008080ff8-0xfffffe0008082c10 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x0107cff8-0x0107d010 addr=0xfffffe0008080ff8-0xfffffe0008081010         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x0107d010-0x0107d028 addr=0xfffffe0008081010-0xfffffe0008081028         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001960 off=0x0107d028-0x0107e988 addr=0xfffffe0008081028-0xfffffe0008082988         __DATA_CONST.__const            
	sz=0x00000100 off=0x0107e988-0x0107ea88 addr=0xfffffe0008082988-0xfffffe0008082a88         __DATA_CONST.__kalloc_type      
	sz=0x00000150 off=0x0107ea88-0x0107ebd8 addr=0xfffffe0008082a88-0xfffffe0008082bd8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000038 off=0x0107ebd8-0x0107ec10 addr=0xfffffe0008082bd8-0xfffffe0008082c10         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 91 at 0x04ad8620
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     A517316A-D183-3ED5-BA1E-F9AE284B6FE5
008: LC_SOURCE_VERSION           27.40.1.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9ee88 size=0xb0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleEmbeddedGPS`
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedGPS`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleEmbeddedGPS`
- `CFBundleNumericVersion`: `16785409`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0d1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleEmbeddedGPS.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901306576`
- `_PrelinkExecutableRelativePath`: `AppleEmbeddedGPS`
- `_PrelinkExecutableSize`: `24554`
- `_PrelinkExecutableSourceAddr`: `-2198901306576`
- `_PrelinkKmodInfo`: `-2198828995576`

## Strings (34) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.AppleEmbeddedGPSControlUserClient`
- `1211111212221212111111111111`
- `1211111212221212111122222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221121212`
- `read-hack`
- `_interruptAction`
- `%s_%d`
- `function-gps_time-mark`
- `AppleEmbeddedGPSControlUserClient`
- `1211111212221212111122222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221121`
- `insertData`
- `AppleEmbeddedGPSControl`
- `start`
- `function-gps_reset`
- `site.AppleEmbeddedGPSControl`
- `function-gps_standby`
- `function-pmu_hostwake`
- `min_toggle`
- `AppleEmbeddedI2CGPS`
- `%s: failed to setup GPS interrupt\n`
- `AppleBCM4750`
- `max_toggle`
- `%s::%s receiver overrun\n`
- `site.AppleEmbeddedI2CGPS`
- `IOBSD`
- `12111112122212121111111111121221`
- `function-gps_clock`
- `function-gps_low-pwr-status`
- `site.AppleBCM4750`
- `%s::%s couldn't setup the interrupt\n`
- `\"Could not get GPS to wake up after %u tries\\n\" @%s:%d`
- `%s::%s succeeded\n`
- `%s::%s dropping %u bytes\n`
- `AppleEmbeddedGPSControl.cpp`
- `function-gps_wake`
