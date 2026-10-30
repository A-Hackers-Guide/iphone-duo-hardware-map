# `com.apple.driver.AppleCameraPhotonDetector`

- Name: AppleCameraPhotonDetector
- Version: `1.0`
- UUID: `9839DA14-8950-3085-88B8-7041255378BB`
- Source version: `20.112.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/grimaldi`](../devicetree/root__arm-io__grimaldi.md) | `AppleCameraPhotonDetector` | `aop,h16,vd5b704` |

## IOKit personalities (1) [KC]

### generic
- `CFBundleIdentifier`: `com.apple.driver.AppleCameraPhotonDetector`
- `IOClass`: `AppleCameraPhotonDetector`
- `IONameMatch`: `aop,h16,vd5b704`
- `IOPersonalityPublisher`: `com.apple.driver.AppleCameraPhotonDetector`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleCameraPhotonDetector` | 0xe8 | IOService → IORegistryEntry |
| `AppleCameraPhotonDetectorUserClient` | 0x100 | IOUserClient → IOService → IORegistryEntry |
| `OSValueObject<AppleCameraPhotonDetectorClientContext>` | 0x18 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000ec1 off=0x003f9ae0-0x003fa9a1 addr=0xfffffe00073fdae0-0xfffffe00073fe9a1 r--/r--   __TEXT            
	sz=0x000001fe off=0x003fa158-0x003fa356 addr=0xfffffe00073fe158-0xfffffe00073fe356               __TEXT.__cstring          (CstringLiterals)
	sz=0x0000064b off=0x003fa356-0x003fa9a1 addr=0xfffffe00073fe356-0xfffffe00073fe9a1               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00002c04 off=0x01ad5510-0x01ad8114 addr=0xfffffe0008ad9510-0xfffffe0008adc114 r-x/r-x   __TEXT_EXEC       
	sz=0x00002a04 off=0x01ad5510-0x01ad7f14 addr=0xfffffe0008ad9510-0xfffffe0008adbf14          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000200 off=0x01ad7f14-0x01ad8114 addr=0xfffffe0008adbf14-0xfffffe0008adc114          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000160 off=0x04936ba8-0x04936d08 addr=0xfffffe000b93aba8-0xfffffe000b93ad08 rw-/rw-   __DATA            
	sz=0x000000d8 off=0x04936ba8-0x04936c80 addr=0xfffffe000b93aba8-0xfffffe000b93ac80               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b93ac80-0xfffffe000b93ace0               __DATA.__common           (Zerofill)
	sz=0x00000028 off=0x00000000-0x00000028 addr=0xfffffe000b93ace0-0xfffffe000b93ad08               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000010c8 off=0x0101fb50-0x01020c18 addr=0xfffffe0008023b50-0xfffffe0008024c18 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x0101fb50-0x0101fb68 addr=0xfffffe0008023b50-0xfffffe0008023b68         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x0101fb68-0x0101fb78 addr=0xfffffe0008023b68-0xfffffe0008023b78         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000e48 off=0x0101fb78-0x010209c0 addr=0xfffffe0008023b78-0xfffffe00080249c0         __DATA_CONST.__const            
	sz=0x00000100 off=0x010209c0-0x01020ac0 addr=0xfffffe00080249c0-0xfffffe0008024ac0         __DATA_CONST.__kalloc_type      
	sz=0x00000100 off=0x01020ac0-0x01020bc0 addr=0xfffffe0008024ac0-0xfffffe0008024bc0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000058 off=0x01020bc0-0x01020c18 addr=0xfffffe0008024bc0-0xfffffe0008024c18         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 75 at 0x04ad5118
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     9839DA14-8950-3085-88B8-7041255378BB
008: LC_SOURCE_VERSION           20.112.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9bdd0 size=0x78
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleCameraPhotonDetector`
- `CFBundleIdentifier`: `com.apple.driver.AppleCameraPhotonDetector`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleCameraPhotonDetector`
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
- `NSHumanReadableCopyright`: `Copyright © 2016-2017 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleCameraPhotonDetector.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901630240`
- `_PrelinkExecutableRelativePath`: `AppleCameraPhotonDetector`
- `_PrelinkExecutableSize`: `19693`
- `_PrelinkExecutableSourceAddr`: `-2198901630240`
- `_PrelinkKmodInfo`: `-2198829028440`

## Strings (48) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AppleCameraPhotonDetectorUserClient`
- `site.AppleCameraPhotonDetectorUserClient`
- `clientDied`
- `compatible`
- `function-grimaldi-device-id`
- `kext`
- `com.apple.photondetector.iokit-user-access`
- `free`
- `12111112122212121211111111112`
- `start`
- `aop,h16,vd5b704`
- `function-power`
- `AppleCameraPhotonDetector`
- `function-grimaldi-power-get`
- `function-grimaldi-gain`
- `com.apple.isp`
- `site.T`
- `12111112122212121111111111111222`
- `init`
- `site.AppleCameraPhotonDetector`
- `OSValueObject<AppleCameraPhotonDetectorClientContext>`
- `function-grimaldi-power-set`
- `i2c,vd5b704`
- `1`

**[__TEXT.__os_log]**

- `AppleCameraPhotonDetectorUserClient:%s - New UserClient for process: %s (pid %d)\n`
- `AppleCameraPhotonDetectorUserClient:%s - client died\n`
- `AppleCameraPhotonDetector:%s - Could not start IOService\n`
- `AppleCameraPhotonDetector:%s - Could not get the IO Nub\n`
- `ApplePhotonDetctor:%s - Error matching with EDT node\n`
- `AppleCameraPhotonDetector:%s - %d: failed to read deviceID\n`
- `AppleCameraPhotonDetectorUserClient:%s - Could not start IOService\n`
- `AppleCameraPhotonDetector:%s - starting\n`
- `AppleCameraPhotonDetector:%s - Could not read compatible property\n`
- `AppleCameraPhotonDetector:%s - Could not get the IIC Nub\n`
- `AppleCameraPhotonDetectorUserClient:%s - Invalid provider\n`
- `AppleCameraPhotonDetector:%s - Matched with AOP node\n`
- `AppleCameraPhotonDetector:%s - ARM Functions to control hardware not available! Check registry\n`
- `AppleCameraPhotonDetector:%s - Matched with I2C node\n`
- `AppleCameraPhotonDetector:%s - Could not find function to control power to PhotonDetector\n`
- `AppleCameraPhotonDetector:%s - Could not create photon detector workloop\n`
- `AppleCameraPhotonDetector:%s - Could not add command gate to workloop\n`
- `AppleCameraPhotonDetectorUserClient:%s - Process %s (pid %d) was denied access\n`
- `AppleCameraPhotonDetectorUserClient:%s - Freeing UserClient for process %s (pid %d)\n`
- `AppleCameraPhotonDetector:%s - Could not read compatible string\n`
- `AppleCameraPhotonDetector:%s - Could not create command gate\n`
- `AppleCameraPhotonDetector:%s - Could not power on the device, err = 0x%x. Exiting\n`
- `AppleCameraPhotonDetector:%s - Could not allocate an array to store the list of clients\n\n`
- `AppleCameraPhotonDetector:%s - deviceID = 0x%x\n`
