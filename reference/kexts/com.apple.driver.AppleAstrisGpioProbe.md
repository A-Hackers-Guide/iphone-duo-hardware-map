# `com.apple.driver.AppleAstrisGpioProbe`

- Name: AppleAstrisGpioProbe
- Version: `1.0.1`
- UUID: `DD43EF01-4077-35E9-BDEE-978BEA0CE2DB`
- Source version: `31.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleAstrisGpioProbe
- `CFBundleIdentifier`: `com.apple.driver.AppleAstrisGpioProbe`
- `IOClass`: `AppleAstrisGpioProbe`
- `IONameMatch`: `aod`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAstrisGpioProbe`
- `IOProviderClass`: `AppleARMIODevice`
- `IOUserClientClass`: `AppleAstrisGpioProbeUserClient`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleAstrisGpioProbe` | 0x328 | IOService → IORegistryEntry |
| `AppleAstrisGpioProbeUserClient` | 0xd8 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, DylibInCache
000: LC_SEGMENT_64 sz=0x00000e31 off=0x0038f490-0x003902c1 addr=0xfffffe0007393490-0xfffffe00073942c1 r--/r--   __TEXT            
	sz=0x0000008a off=0x0038fb58-0x0038fbe2 addr=0xfffffe0007393b58-0xfffffe0007393be2               __TEXT.__const            
	sz=0x000006df off=0x0038fbe2-0x003902c1 addr=0xfffffe0007393be2-0xfffffe00073942c1               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00004758 off=0x01986f90-0x0198b6e8 addr=0xfffffe000898af90-0xfffffe000898f6e8 r-x/r-x   __TEXT_EXEC       
	sz=0x000045b8 off=0x01986f90-0x0198b548 addr=0xfffffe000898af90-0xfffffe000898f548          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001a0 off=0x0198b548-0x0198b6e8 addr=0xfffffe000898f548-0xfffffe000898f6e8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000334 off=0x04932c98-0x04932fcc addr=0xfffffe000b936c98-0xfffffe000b936fcc rw-/rw-   __DATA            
	sz=0x000000cc off=0x04932c98-0x04932d64 addr=0xfffffe000b936c98-0xfffffe000b936d64               __DATA.__data             
	sz=0x00000064 off=0x00000000-0x00000064 addr=0xfffffe000b936d68-0xfffffe000b936dcc               __DATA.__common           (Zerofill)
	sz=0x000001fc off=0x00000000-0x000001fc addr=0xfffffe000b936dd0-0xfffffe000b936fcc               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001088 off=0x00fe77b0-0x00fe8838 addr=0xfffffe0007feb7b0-0xfffffe0007fec838 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x00fe77b0-0x00fe77b8 addr=0xfffffe0007feb7b0-0xfffffe0007feb7b8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x00fe77b8-0x00fe77c0 addr=0xfffffe0007feb7b8-0xfffffe0007feb7c0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000ef0 off=0x00fe77c0-0x00fe86b0 addr=0xfffffe0007feb7c0-0xfffffe0007fec6b0         __DATA_CONST.__const            
	sz=0x00000008 off=0x00fe86b0-0x00fe86b8 addr=0xfffffe0007fec6b0-0xfffffe0007fec6b8         __DATA_CONST.__weak_auth_got    (NonLazySymbolPointers)
	sz=0x00000080 off=0x00fe86b8-0x00fe8738 addr=0xfffffe0007fec6b8-0xfffffe0007fec738         __DATA_CONST.__kalloc_type      
	sz=0x000000c8 off=0x00fe8738-0x00fe8800 addr=0xfffffe0007fec738-0xfffffe0007fec800         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000038 off=0x00fe8800-0x00fe8838 addr=0xfffffe0007fec800-0xfffffe0007fec838         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 59 at 0x04ad36e0
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     DD43EF01-4077-35E9-BDEE-978BEA0CE2DB
008: LC_SOURCE_VERSION           31.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9a1c8 size=0xc0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleAstrisGpioProbe`
- `CFBundleIdentifier`: `com.apple.driver.AppleAstrisGpioProbe`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleAstrisGpioProbe`
- `CFBundleNumericVersion`: `16875520`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.1`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.1`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleAstrisGpioProbe.kext`
- `_PrelinkExecutableLoadAddr`: `-2198902066032`
- `_PrelinkExecutableRelativePath`: `AppleAstrisGpioProbe`
- `_PrelinkExecutableSize`: `26949`
- `_PrelinkExecutableSourceAddr`: `-2198902066032`
- `_PrelinkKmodInfo`: `-2198829044584`

## Strings (44) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AppleAstrisGpioProbe::%s():[%s] Bailing out.. Set swd_updates_arg boot-arg to allow swd updates!\n`
- `AppleAstrisGpioProbe::%s():[%s] could not do platform initialization\n`
- `start`
- `root`
- `AppleAstrisGpioProbe::%s():[%s] target is not an instance of AppleAstrisGpioProbe\n`
- `AppleAstrisGpioProbe::%s():[%s] Failed to IOMalloc for buffer cmd\n`
- `AppleAstrisGpioProbe`
- `platformInit`
- `WARNING`
- `function-aod_swclk`
- `121111121222121211111111111`
- `extParseCSProtocol`
- `AppleAstrisGpioProbe::%s():[%s] Unimplemented reset function\n`
- `function-grape_cs`
- `AppleAstrisGpioProbe::%s():[%s] super failed to start\n`
- `externalMethod`
- `AppleAstrisGpioProbe::%s():[%s] arguments->structureOutputSize < sizeof(port) (0x%x < 0x%x), can cause buffer overflow\n`
- `AppleAstrisGpioProbe::%s():[%s] Unimplemented RelaySet function\n\n`
- `AppleAstrisGpioProbe::%s():[%s] SecureRoot check api failed\n`
- `ERROR`
- `function-aod_swdio`
- `AppleAstrisGpioProbe::%s():[%s] unknown external method %u\n`
- `SetGrapeCS`
- `function-reset`
- `probe-port`
- `site.AppleAstrisGpioProbeUserClient`
- `AppleAstrisGpioProbe::%s():[%s] bug in kext matching\n`
- `AppleAstrisGpioProbe::%s():[%s] structureInputSize - 0x%x less than sizeof(cscommand_t) - 0x%x, can lead to out of bounds access\n`
- `extGetProbePortNumber`
- `AppleAstrisGpioProbe::%s():[%s] No function-grape_cs available\n\n`
- `AppleAstrisGpioProbe::%s():[%s] Unimplemented RelayGet command\n\n`
- `SecureRoot`
- `RelayGet`
- `RelaySet`
- `site.AppleAstrisGpioProbe`
- `allow_swd_updates`
- `AppleAstrisGpioProbe::%s():[%s] unknown signal id\n`
- `AppleAstrisGpioProbe::%s():[%s] not authorized\n`
- `AppleAstrisGpioProbe::%s():[%s] structureOutputSize - 0x%x less than structureInputSize - 0x%x \n\n`
- `JtagSRST`
- `12111112122212121221111111222222222222222222222222222222222222222222222222222222222222222222221111122`
- `default-tck`
- `AppleAstrisGpioProbeUserClient`
- `wiggle`
