# `com.apple.driver.ApplePhotonDetector`

- Name: ApplePhotonDetector
- Version: `1.0`
- UUID: `2BB33D5B-A962-3D2A-817A-41C01C9DBC0B`
- Source version: `11.4.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### generic
- `CFBundleIdentifier`: `com.apple.driver.ApplePhotonDetector`
- `IOClass`: `ApplePhotonDetector`
- `IONameMatch`: `aop,vd5b704`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePhotonDetector`
- `IOProviderClass`: `AppleARMIODevice`

### t8101
- `CFBundleIdentifier`: `com.apple.driver.ApplePhotonDetector`
- `IOClass`: `ApplePhotonDetector`
- `IONameMatch`: `i2c,vd5b704`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePhotonDetector`
- `IOProviderClass`: `AppleARMIICDevice`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `ApplePhotonDetector` | 0xe8 | IOService → IORegistryEntry |
| `ApplePhotonDetectorUserClient` | 0x170 | IOUserClient → IOService → IORegistryEntry |
| `OSValueObject<ApplePhotonDetectorClientContext>` | 0x18 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000dbd off=0x006ba4c0-0x006bb27d addr=0xfffffe00076be4c0-0xfffffe00076bf27d r--/r--   __TEXT            
	sz=0x000001d7 off=0x006bab38-0x006bad0f addr=0xfffffe00076beb38-0xfffffe00076bed0f               __TEXT.__cstring          (CstringLiterals)
	sz=0x0000056e off=0x006bad0f-0x006bb27d addr=0xfffffe00076bed0f-0xfffffe00076bf27d               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00002774 off=0x023dcd20-0x023df494 addr=0xfffffe00093e0d20-0xfffffe00093e3494 r-x/r-x   __TEXT_EXEC       
	sz=0x00002584 off=0x023dcd20-0x023df2a4 addr=0xfffffe00093e0d20-0xfffffe00093e32a4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001f0 off=0x023df2a4-0x023df494 addr=0xfffffe00093e32a4-0xfffffe00093e3494          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000150 off=0x04985198-0x049852e8 addr=0xfffffe000b989198-0xfffffe000b9892e8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04985198-0x04985260 addr=0xfffffe000b989198-0xfffffe000b989260               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b989260-0xfffffe000b9892c0               __DATA.__common           (Zerofill)
	sz=0x00000028 off=0x00000000-0x00000028 addr=0xfffffe000b9892c0-0xfffffe000b9892e8               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000010c0 off=0x011a4280-0x011a5340 addr=0xfffffe00081a8280-0xfffffe00081a9340 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x011a4280-0x011a4298 addr=0xfffffe00081a8280-0xfffffe00081a8298         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x011a4298-0x011a42a8 addr=0xfffffe00081a8298-0xfffffe00081a82a8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000e48 off=0x011a42a8-0x011a50f0 addr=0xfffffe00081a82a8-0xfffffe00081a90f0         __DATA_CONST.__const            
	sz=0x00000100 off=0x011a50f0-0x011a51f0 addr=0xfffffe00081a90f0-0xfffffe00081a91f0         __DATA_CONST.__kalloc_type      
	sz=0x000000f8 off=0x011a51f0-0x011a52e8 addr=0xfffffe00081a91f0-0xfffffe00081a92e8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000058 off=0x011a52e8-0x011a5340 addr=0xfffffe00081a92e8-0xfffffe00081a9340         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 73 at 0x04ae2978
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     2BB33D5B-A962-3D2A-817A-41C01C9DBC0B
008: LC_SOURCE_VERSION           11.4.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aad5a8 size=0x78
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `ApplePhotonDetector`
- `CFBundleIdentifier`: `com.apple.driver.ApplePhotonDetector`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `ApplePhotonDetector`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/ApplePhotonDetector.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898744128`
- `_PrelinkExecutableRelativePath`: `ApplePhotonDetector`
- `_PrelinkExecutableSize`: `18241`
- `_PrelinkExecutableSourceAddr`: `-2198898744128`
- `_PrelinkKmodInfo`: `-2198828707432`

## Strings (45) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.ApplePhotonDetectorUserClient`
- `free`
- `site.ApplePhotonDetector`
- `site.T`
- `ApplePhotonDetectorUserClient`
- `com.apple.photondetector.iokit-user-access`
- `init`
- `start`
- `ApplePhotonDetector`
- `function-grimaldi-device-id`
- `function-grimaldi-power-get`
- `1211111212221212111111111111122222222222222222`
- `clientDied`
- `12111112122212121211111111112`
- `OSValueObject<ApplePhotonDetectorClientContext>`
- `aop,vd5b704`
- `function-grimaldi-gain`
- `1`
- `compatible`
- `function-grimaldi-power-set`
- `i2c,vd5b704`
- `function-power`

**[__TEXT.__os_log]**

- `ApplePhotonDetectorUserClient - %s: New UserClient for process: %s (pid %d)\n`
- `ApplePhotonDetectorUserClient - %s: Invalid provider\n`
- `ApplePhotonDetectorUserClient - %s\n`
- `ApplePhotonDetector - %s: Could not read compatible property\n`
- `ApplePhotonDetector - %s: Matched with AOP node\n`
- `ApplePhotonDetector - %s: Could not get the IO Nub\n`
- `ApplePhotonDetector - %s: ARM Functions to control hardware not available! Check registry\n`
- `ApplePhotonDetector - %s: Matched with I2C node\n`
- `ApplePhotonDetectorUserClient - %s: Process %s (pid %d) was denied access\n`
- `ApplePhotonDetectorUserClient - %s: Could not start IOService\n`
- `ApplePhotonDetector - %s: Could not find function to control power to PhotonDetector\n`
- `ApplePhotonDetector - %s: Could not create command gate\n`
- `ApplePhotonDetector - %s: Could not add command gate to workloop\n`
- `ApplePhotonDetector - %s: Could not read compatible string\n`
- `ApplePhotonDetctor - %s: Error matching with EDT node\n`
- `ApplePhotonDetector - %s: Could not create photon detector workloop\n`
- `ApplePhotonDetector = %s: Could not power on the device, err = 0x%x. Exiting\n`
- `ApplePhotonDetectorUserClient - %s: Freeing UserClient for process %s (pid %d)\n`
- `ApplePhotonDetector - %s:\n`
- `ApplePhotonDetector - %s: Could not start IOService\n`
- `ApplePhotonDetector - %s: Could not get the IIC Nub\n`
- `ApplePhotonDetector - %s: %d: failed to read deviceID\n`
- `ApplePhotonDetector - %s: deviceID = 0x%x\n`
