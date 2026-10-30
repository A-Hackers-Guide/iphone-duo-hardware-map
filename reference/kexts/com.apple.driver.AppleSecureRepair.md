# `com.apple.driver.AppleSecureRepair`

- Name: AppleSecureRepair
- Version: `1.0.0`
- UUID: `3D0A1A5F-1F99-31C2-B304-0B61AA7E5016`
- Source version: `1307.52.1.0.0`
- Depends on: [`com.apple.driver.AppleGPIOICController`](com.apple.driver.AppleGPIOICController.md) 1.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 20.2, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 20.2, [`com.apple.kpi.private`](com.apple.kpi.private.md) 22.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/secure-repair`](../devicetree/root__arm-io__secure-repair.md) | `AppleSecureRepair` | `secure-repair,1` |

## IOKit personalities (1) [KC]

### AppleSecureRepair
- `CFBundleIdentifier`: `com.apple.driver.AppleSecureRepair`
- `IOClass`: `AppleSecureRepair`
- `IONameMatch`: `secure-repair,1`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSecureRepair`
- `IOProviderClass`: `AppleARMIODevice`
- `IOUserClientClass`: `AppleSecureRepairUserClient`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleSecureRepair` | 0x98 | IOService → IORegistryEntry |
| `AppleSecureRepairUserClient` | 0xe0 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000009cf off=0x00781ad0-0x0078249f addr=0xfffffe0007785ad0-0xfffffe000778649f r--/r--   __TEXT            
	sz=0x00000048 off=0x007820f8-0x00782140 addr=0xfffffe00077860f8-0xfffffe0007786140               __TEXT.__const            
	sz=0x0000035f off=0x00782140-0x0078249f addr=0xfffffe0007786140-0xfffffe000778649f               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x000011e8 off=0x02727a10-0x02728bf8 addr=0xfffffe000972ba10-0xfffffe000972cbf8 r-x/r-x   __TEXT_EXEC       
	sz=0x000010f8 off=0x02727a10-0x02728b08 addr=0xfffffe000972ba10-0xfffffe000972cb08          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000000f0 off=0x02728b08-0x02728bf8 addr=0xfffffe000972cb08-0xfffffe000972cbf8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x0499a348-0x0499a470 addr=0xfffffe000b99e348-0xfffffe000b99e470 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x0499a348-0x0499a40c addr=0xfffffe000b99e348-0xfffffe000b99e40c               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b99e410-0xfffffe000b99e470               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000e18 off=0x01226fa0-0x01227db8 addr=0xfffffe000822afa0-0xfffffe000822bdb8 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x01226fa0-0x01226fb0 addr=0xfffffe000822afa0-0xfffffe000822afb0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x01226fb0-0x01226fc0 addr=0xfffffe000822afb0-0xfffffe000822afc0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000cc8 off=0x01226fc0-0x01227c88 addr=0xfffffe000822afc0-0xfffffe000822bc88         __DATA_CONST.__const            
	sz=0x00000080 off=0x01227c88-0x01227d08 addr=0xfffffe000822bc88-0xfffffe000822bd08         __DATA_CONST.__kalloc_type      
	sz=0x00000078 off=0x01227d08-0x01227d80 addr=0xfffffe000822bd08-0xfffffe000822bd80         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000038 off=0x01227d80-0x01227db8 addr=0xfffffe000822bd80-0xfffffe000822bdb8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 37 at 0x04ae6cd8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     3D0A1A5F-1F99-31C2-B304-0B61AA7E5016
008: LC_SOURCE_VERSION           1307.52.1.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab2d50 size=0x48
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleSecureRepair`
- `CFBundleIdentifier`: `com.apple.driver.AppleSecureRepair`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSecureRepair`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2023 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleSecureRepair.kext`
- `_PrelinkExecutableLoadAddr`: `-2198897927472`
- `_PrelinkExecutableRelativePath`: `AppleSecureRepair`
- `_PrelinkExecutableSize`: `10999`
- `_PrelinkExecutableSourceAddr`: `-2198897927472`
- `_PrelinkKmodInfo`: `-2198828620984`

## Strings (40) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `start`
- `%s::%s: en=%u\n`
- `%s::%s: set pin %u -> %u\n`
- `%s::%s: no-op\n`
- `unable to get chosen\n`
- `unable to start GPIO controller\n`
- `Not use inverted GPIO polarity for 0x%x\n`
- `%s::%s(%p)\n`
- `site.AppleSecureRepair`
- `stop`
- `chip-id`
- `unable to get chip-id\n`
- `AppleSecureRepairUserClient`
- `IOUserClientEntitlements`
- `gpio-repair_en`
- `%s::%s`
- `assertRepair`
- `1211111212221212112`
- `Use inverted GPIO polarity for 0x%x\n`
- `site.AppleSecureRepairUserClient`
- `1211111212221212111111111111`
- `free`
- `%s::%s\n`
- `getRepairState`
- `IOUserClientDefaultLocking`
- `%s::%s(%p, %p, %u, %p)\n`
- `initWithTask`
- `AppleSecureRepair`
- `AppleGPIOICController`
- `unable to find GPIO controller\n`
- `%s::%s, result = %u`
- `unable to find GPIO\n`
- `Failed to get chip-id\n`
- `IOUserClientDefaultLockingSetProperties`
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `unable to open GPIO\n`
- `IODeviceTree:/chosen`
- `com.apple.private.AppleSecureRepair.allow`
- `%s::%s()\n`
- `clientClose`
