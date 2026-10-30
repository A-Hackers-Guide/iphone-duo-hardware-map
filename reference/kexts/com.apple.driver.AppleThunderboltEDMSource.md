# `com.apple.driver.AppleThunderboltEDMSource`

- Name: AppleThunderboltEDMSource
- Version: `5.0.3`
- UUID: `C1F86423-5AC7-3126-8C89-2DE74E567C84`
- Source version: `513.0.0.0.0`
- Depends on: [`com.apple.driver.AppleThunderboltDPAdapterFamily`](com.apple.driver.AppleThunderboltDPAdapterFamily.md) 1.0.0, [`com.apple.driver.AppleThunderboltDPInAdapter`](com.apple.driver.AppleThunderboltDPInAdapter.md) 1.0.0, [`com.apple.iokit.IOThunderboltFamily`](com.apple.iokit.IOThunderboltFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleThunderboltEDMSource
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltEDMSource`
- `IOClass`: `AppleThunderboltEDMSource`
- `IOPCIPauseCompatible`: `True`
- `IOPersonalityPublisher`: `com.apple.driver.AppleThunderboltEDMSource`
- `IOProbeScore`: `4096`
- `IOPropertyMatch`:
  - `Protocol Revision`: `1`
  - `Protocol Version`: `1`
  - `Service Key`: `extdisp`
- `IOProviderClass`: `IOThunderboltXDomainService`


## C++ classes (5) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleThunderboltEDMRequestCommand` | 0xc0 | IOThunderboltConfigXDomainRequestCommand → IOThunderboltConfigXDomainCommand → IOThunderboltConfigCommand → IOThunderboltCommand → IOCommand |
| `AppleThunderboltEDMSource` | 0x150 | IOService → IORegistryEntry |
| `AppleThunderboltEDMSourceGFXPolicy1` | 0x248 | AppleThunderboltEDMSource → IOService → IORegistryEntry |
| `AppleThunderboltEDMSourceGFXPolicy2` | 0x248 | AppleThunderboltEDMSource → IOService → IORegistryEntry |
| `AppleThunderboltEDMSourceUserClient` | 0xe0 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001c2c off=0x0081b660-0x0081d28c addr=0xfffffe000781f660-0xfffffe000782128c r--/r--   __TEXT            
	sz=0x000015e4 off=0x0081bc88-0x0081d26c addr=0xfffffe000781fc88-0xfffffe000782126c               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000020 off=0x0081d26c-0x0081d28c addr=0xfffffe000782126c-0xfffffe000782128c               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x000086d4 off=0x0295ba10-0x029640e4 addr=0xfffffe000995fa10-0xfffffe00099680e4 r-x/r-x   __TEXT_EXEC       
	sz=0x000083b4 off=0x0295ba10-0x02963dc4 addr=0xfffffe000995fa10-0xfffffe0009967dc4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000320 off=0x02963dc4-0x029640e4 addr=0xfffffe0009967dc4-0xfffffe00099680e4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000002c0 off=0x049cdc00-0x049cdec0 addr=0xfffffe000b9d1c00-0xfffffe000b9d1ec0 rw-/rw-   __DATA            
	sz=0x000001e8 off=0x049cdc00-0x049cdde8 addr=0xfffffe000b9d1c00-0xfffffe000b9d1de8               __DATA.__data             
	sz=0x000000d8 off=0x00000000-0x000000d8 addr=0xfffffe000b9d1de8-0xfffffe000b9d1ec0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00002500 off=0x0127de58-0x01280358 addr=0xfffffe0008281e58-0xfffffe0008284358 rw-/rw-   __DATA_CONST      
	sz=0x00000028 off=0x0127de58-0x0127de80 addr=0xfffffe0008281e58-0xfffffe0008281e80         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000028 off=0x0127de80-0x0127dea8 addr=0xfffffe0008281e80-0xfffffe0008281ea8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00002110 off=0x0127dea8-0x0127ffb8 addr=0xfffffe0008281ea8-0xfffffe0008283fb8         __DATA_CONST.__const            
	sz=0x00000140 off=0x0127ffb8-0x012800f8 addr=0xfffffe0008283fb8-0xfffffe00082840f8         __DATA_CONST.__kalloc_type      
	sz=0x00000190 off=0x012800f8-0x01280288 addr=0xfffffe00082840f8-0xfffffe0008284288         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000d0 off=0x01280288-0x01280358 addr=0xfffffe0008284288-0xfffffe0008284358         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 126 at 0x04ae9880
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     C1F86423-5AC7-3126-8C89-2DE74E567C84
008: LC_SOURCE_VERSION           513.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab5b08 size=0x138
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleThunderboltEDMSource`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltEDMSource`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleThunderboltEDMSource`
- `CFBundleNumericVersion`: `84115456`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `5.0.3`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `5.0.3`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `AppleThunderboltEDMService version 5.0.3, Copyright © 2010-2020 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleThunderboltEDMService.kext/PlugIns/AppleThunderboltEDMSource.kext`
- `_PrelinkExecutableLoadAddr`: `-2198897297824`
- `_PrelinkExecutableRelativePath`: `AppleThunderboltEDMSource`
- `_PrelinkExecutableSize`: `51904`
- `_PrelinkExecutableSourceAddr`: `-2198897297824`
- `_PrelinkKmodInfo`: `-2198828409856`

## Strings (79) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AppleThunderboltEDMSource<%p>::setPathSetConfigDataSourcePort - ERROR: base class function called instead of subclass\n`
- `1211111212221212111111112211111111222222221211111111122211222222222111111`
- `Mac-827FB448E656EC26`
- `Protocol Revision`
- `EDM State`
- `AppleThunderboltEDMSource<%p>::createDPPathManager - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::getDPInPort - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::getDPPMPathTypeAuxRx - ERROR: base class function called instead of subclass\n`
- `site.AppleThunderboltEDMRequestCommand`
- `Mac-827FAC58A8FDFA22`
- `Mac-27AD2F918AE68F61`
- `AppleThunderboltEDMSource<%p>::destroyEDMPathSet - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::createDPInAdapterMatchingDictionary - ERROR: base class function called instead of subclass\n`
- `Mac-AA95B1DDAB278B95`
- `AppleThunderboltEDMSource<%p>::setDPPathManagerBandwidthOptions - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMRequestCommand`
- `site.AppleThunderboltEDMSource`
- `Protocol ID`
- `edm`
- `AppleThunderboltEDMSource<%p>::setDPPathsPathSetType - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::getAuxTxPathAllocatedDestinationHopID - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::getAuxRxPathAllocatedSourceHopID - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::getDPPMPathTypeAuxTx - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::setDPInRemoteDPCapabilities - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::checkDPInAdapterValid - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::getVideoPathAllocatedDestinationHopID - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::getDPPMDefaultAuxPathHopIDRange - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSourceGFXPolicy2`
- `AppleThunderboltDPInAdapter`
- `AppleThunderboltEDMSource<%p>::setDPPathManagerLaneRoutingOptions - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::extractDPInPortFromIOService - ERROR: base class function called instead of subclass\n`
- `121111121222121211111111221111111122222222`
- `Mac-63001698E7A34814`
- `AppleThunderboltEDMSourceUserClient`
- `AppleThunderboltEDMSource<%p>::destroyDPPathManager - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::getAuxRxPathAllocatedDestinationHopID - ERROR: base class function called instead of subclass\n`
- `Protocol Settings`
- `AppleThunderboltEDMSink`
- `AppleThunderboltEDMSource<%p>::setDPInPort - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::clearDPInHPD - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::getAuxTxPathAllocatedSourceHopID - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::getDPPMNULLHopIDRange - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::clearPathSetConfigData - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::setPathSetConfigDataSinkPort - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource`
- `Mac-77E8E67C6DB170AA`
- `AppleThunderboltEDMSource<%p>::getRootDPInPortCount - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::getDPPMDefaultVideoPathHopIDRange - ERROR: base class function called instead of subclass\n`
- `1211111212221212111111111111`
- `site.AppleThunderboltEDMSourceGFXPolicy2`
- `tbdp`
- `121111211112221222121121`
- `AppleThunderboltEDMSource<%p>::enableDPIn - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::getDPPMPathSetTypeDirect - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSourceGFXPolicy1`
- `Mac-226CB3C6A851A671`
- `Mac-1E7E29AD0135F9BC`
- `board-id`
- `AppleThunderboltEDMSource<%p>::configDPInHopIDs - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::getDPPMAnyFreePort - ERROR: base class function called instead of subclass\n`
- `site.AppleThunderboltEDMSourceUserClient`
- `AppleThunderboltDPInAdapterBase`
- `site.AppleThunderboltEDMSourceGFXPolicy1`
- `Mac-7BA5B2DFE22DDD8C`
- `Protocol Version`
- `AppleThunderboltEDMSource<%p>::setDPPathManagerHopIDRanges - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::findDPInPortAtRoute - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::getDPInLocalDPCapabilities - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::getVideoPathAllocatedSourceHopID - ERROR: base class function called instead of subclass\n`
- `Mac-937A206F2EE63C01`
- `Mac-B234B1456C785320`
- `AppleThunderboltEDMSource<%p>::getGPUIsMuxedAway - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::getDPPMPathTypeVideo - ERROR: base class function called instead of subclass\n`
- `Mac-53FDB3D8DB8CA971`
- `Mac-E1008331FDC96864`
- `AppleThunderboltEDMSource<%p>::getSSCOffset - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::createEDMPathSet - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::reserveDPInPort - ERROR: base class function called instead of subclass\n`
- `AppleThunderboltEDMSource<%p>::setPathSetConfigDataPathsToCreate - ERROR: base class function called instead of subclass\n`
