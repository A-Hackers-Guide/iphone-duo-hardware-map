# `com.apple.driver.AppleThunderboltDPInAdapter`

- Name: AppleThunderboltDPInAdapter
- Version: `8.5.1`
- UUID: `9CA7D8F1-534F-31D9-8C95-EF1062E6A1B9`
- Source version: `876.40.3.0.0`
- Depends on: [`com.apple.driver.AppleThunderboltDPAdapterFamily`](com.apple.driver.AppleThunderboltDPAdapterFamily.md) 1.0.0, [`com.apple.iokit.IOThunderboltFamily`](com.apple.iokit.IOThunderboltFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (5) [KC]

### AppleThunderboltDPInAdapter
- `Adapter Type`: `917761`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltDPInAdapter`
- `IOClass`: `AppleThunderboltDPInAdapter`
- `IOPersonalityPublisher`: `com.apple.driver.AppleThunderboltDPInAdapter`
- `IOProbeScore`: `9`
- `IOProviderClass`: `IOThunderboltPort`

### AppleThunderboltDPInAdapterBase
- `Adapter Type`: `917761`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltDPInAdapter`
- `IOClass`: `AppleThunderboltDPInAdapterBase`
- `IOPersonalityPublisher`: `com.apple.driver.AppleThunderboltDPInAdapter`
- `IOProbeScore`: `10`
- `IOProviderClass`: `IOThunderboltPort`

### AppleThunderboltDPInAdapterCM
- `Adapter Type`: `917761`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltDPInAdapter`
- `IOClass`: `AppleThunderboltDPInAdapterCM`
- `IOPersonalityPublisher`: `com.apple.driver.AppleThunderboltDPInAdapter`
- `IOProbeScore`: `11`
- `IOProviderClass`: `IOThunderboltPort`

### AppleThunderboltDPInAdapterOS
- `Adapter Type`: `917761`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltDPInAdapter`
- `IOClass`: `AppleThunderboltDPInAdapterOS`
- `IOPersonalityPublisher`: `com.apple.driver.AppleThunderboltDPInAdapter`
- `IOProbeScore`: `11`
- `IOProviderClass`: `IOThunderboltPort`

### AppleThunderboltDPInAdapterOS2
- `Adapter Type`: `917761`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltDPInAdapter`
- `IOClass`: `AppleThunderboltDPInAdapterOS2`
- `IOPersonalityPublisher`: `com.apple.driver.AppleThunderboltDPInAdapter`
- `IOProbeScore`: `11`
- `IOProviderClass`: `IOThunderboltPort`


## C++ classes (5) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleThunderboltDPInAdapter` | 0x1d0 | AppleThunderboltDPAdapterFamily → IOThunderboltTunnelDriver → IOService → IORegistryEntry |
| `AppleThunderboltDPInAdapterBase` | 0x198 | AppleThunderboltDPAdapterFamilyBase → IOThunderboltTunnelDriver → IOService → IORegistryEntry |
| `AppleThunderboltDPInAdapterCM` | 0x198 | AppleThunderboltDPInAdapterBase → AppleThunderboltDPAdapterFamilyBase → IOThunderboltTunnelDriver → IOService → IORegistryEntry |
| `AppleThunderboltDPInAdapterOS` | 0x1a0 | AppleThunderboltDPInAdapterCM → AppleThunderboltDPInAdapterBase → AppleThunderboltDPAdapterFamilyBase → IOThunderboltTunnelDriver → IOService → IORegistryEntry |
| `AppleThunderboltDPInAdapterOS2` | 0x1a0 | AppleThunderboltDPInAdapterOS → AppleThunderboltDPInAdapterCM → AppleThunderboltDPInAdapterBase → AppleThunderboltDPAdapterFamilyBase → IOThunderboltTunnelDriver → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000282b off=0x007fbf80-0x007fe7ab addr=0xfffffe00077fff80-0xfffffe00078027ab r--/r--   __TEXT            
	sz=0x00002253 off=0x007fc558-0x007fe7ab addr=0xfffffe0007800558-0xfffffe00078027ab               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00007f18 off=0x0290f020-0x02916f38 addr=0xfffffe0009913020-0xfffffe000991af38 r-x/r-x   __TEXT_EXEC       
	sz=0x00007d28 off=0x0290f020-0x02916d48 addr=0xfffffe0009913020-0xfffffe000991ad48          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001f0 off=0x02916d48-0x02916f38 addr=0xfffffe000991ad48-0xfffffe000991af38          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001a0 off=0x049cd5e0-0x049cd780 addr=0xfffffe000b9d15e0-0xfffffe000b9d1780 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049cd5e0-0x049cd6a8 addr=0xfffffe000b9d15e0-0xfffffe000b9d16a8               __DATA.__data             
	sz=0x000000d8 off=0x00000000-0x000000d8 addr=0xfffffe000b9d16a8-0xfffffe000b9d1780               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00003340 off=0x012758b0-0x01278bf0 addr=0xfffffe00082798b0-0xfffffe000827cbf0 rw-/rw-   __DATA_CONST      
	sz=0x00000028 off=0x012758b0-0x012758d8 addr=0xfffffe00082798b0-0xfffffe00082798d8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000028 off=0x012758d8-0x01275900 addr=0xfffffe00082798d8-0xfffffe0008279900         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00003048 off=0x01275900-0x01278948 addr=0xfffffe0008279900-0xfffffe000827c948         __DATA_CONST.__const            
	sz=0x00000140 off=0x01278948-0x01278a88 addr=0xfffffe000827c948-0xfffffe000827ca88         __DATA_CONST.__kalloc_type      
	sz=0x000000f8 off=0x01278a88-0x01278b80 addr=0xfffffe000827ca88-0xfffffe000827cb80         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000070 off=0x01278b80-0x01278bf0 addr=0xfffffe000827cb80-0xfffffe000827cbf0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 76 at 0x04ae9520
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     9CA7D8F1-534F-31D9-8C95-EF1062E6A1B9
008: LC_SOURCE_VERSION           876.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab56b8 size=0xd8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleThunderboltDPInAdapter`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltDPInAdapter`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleThunderboltDPInAdapter`
- `CFBundleNumericVersion`: `139558912`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `8.5.1`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `8.5.1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `AppleThunderboltDPAdapters version 8.5.1, Copyright © 2009-2021 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Local-Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleThunderboltDPAdapters.kext/PlugIns/AppleThunderboltDPInAdapter.kext`
- `_PrelinkExecutableLoadAddr`: `-2198897426560`
- `_PrelinkExecutableRelativePath`: `AppleThunderboltDPInAdapter`
- `_PrelinkExecutableSize`: `56355`
- `_PrelinkExecutableSourceAddr`: `-2198897426560`
- `_PrelinkKmodInfo`: `-2198828411424`

## Strings (114) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.AppleThunderboltDPInAdapter`
- `%lldus AppleThunderboltDPInAdapter<%p>::start - ERROR: DP crossbar not found\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::setGPUIsMuxedAway - gpuIsMuxedAway = %d, fGPUIsMuxedAway = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::getDPAdapterCapOffset - WARNING: fTerminated = true\n`
- `AppleThunderboltDPInAdapterCM`
- `%lldus AppleThunderboltDPInAdapter<%p>::earlyWakeThread\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::earlyWakeThread - value = 0x%08x lc_hpd = true\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::lateSleep\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::reserveDPPortInternal - messageClients( kIOThunderboltMessageDPStateChange )\n`
- `Cached Local DP Capabilities`
- `AppleThunderboltDPInAdapterCM<%p>(%x:%llx:%x)::setupNotifiers - ERROR: couldn't register with the DP connection manager! status = 0x%08x\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::setTunnelProhibited - tunnelProhibited = %d, fTunnelProhibited = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::setTunnelProhibited - messageClients( kIOThunderboltMessageDPStateChange )\n`
- `Cached Common DP Capabilities`
- `AppleThunderboltDPInAdapterOS`
- `Sink`
- `%lldus AppleThunderboltDPInAdapter<%p>::agcCallback - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::enableDP - WARNING: enableDP failed with 0x%08x (hardware removed?)\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::reserveDPPortInternal - reserve = %d, client = %p, fReservedClient = %p\n`
- `site.AppleThunderboltDPInAdapterOS`
- `AppleThunderboltDPInAdapter`
- `%lldus AppleThunderboltDPInAdapter<%p>::earlyWake\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::getGPUIsMuxedAway - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::getGPUIsMuxedAway - gpu_muxed_away = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::isAdapterAvailableForClient - client = %p\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::reserveDPPortInternal - messageClients( kIOThunderboltMessageDPStateChange )\n`
- `AppleThunderboltDPInAdapterBase<%p>::clearHPD - ERROR: failed to set DPI HPD Output Clear bit! status = 0x%08x\n`
- `%lldus AppleThunderboltDPInAdapterOS<%p>::probe - service = %p\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::start - fSinkNumber = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::earlyWake - inDPPMode = 1, spawning early wake thread\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::reserveDPPortInternal - reserve = %d, client = %p, fReservedClient = %p\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::enableDP - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapterCM<%p>::probe - service = %p\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::finalize\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::lateSleep - lc[%d]: data = 0x%08x, dpp_in_use = %d\n`
- `AppleThunderboltDPInAdapterBase`
- `DPI BWAM Support`
- `%lldus AppleThunderboltDPInAdapter<%p>::enableDP - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::start - ERROR: fSinkNumber not found\n`
- `AppleGraphicsControl`
- `%lldus AppleThunderboltDPInAdapter<%p>::earlyWakeThread - status = 0x%08x, lc_hpd = %d, dpi_hpd_unsuppressed = %d, took %d ms (%d ms propagation + %d ms suppression)\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::agcCallback - invoking fAGCThreadCall\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::enableDP - DPI HPD propagation workaround\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::probe - service = %p\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::clearHPD - WARNING: fTerminated = true\n`
- `Common ALPM Support Is Simulated`
- `%lldus AppleThunderboltDPInAdapter<%p>::setGPUIsMuxedAway - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapterOS2<%p>::probe - service = %p\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::isAdapterAvailableForClient - available = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::start\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::needsEarlyWake - needs_early_wake = %d\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::enableDP - enable = %d\n`
- `AppleThunderboltDPInAdapterBase<%p>::clearHPD - ERROR: failed to clear DPI HPD Output Clear bit! status = 0x%08x\n`
- `tbdp`
- `%lldus AppleThunderboltDPInAdapter<%p>::agcThreadCall - messaging AGC: tunneled_dp_in_use = %p\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::isAdapterAvailableForClient - fArbitrateSNKUseWithLC = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::controlPathListenerCallback - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::start - fStarted = true, calling registerService\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::isAdapterAvailableForClient - dpp_in_use = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::reserveDPPortInternal - WARNING: fTerminated = true, not invoking fAGCThreadCall\n`
- `121111121222121211122222211111111111112222222211122`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::free\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::controlPathListenerCallback - WARNING: fTerminated = true\n`
- `site.AppleThunderboltDPInAdapterCM`
- `%lldus AppleThunderboltDPInAdapterOS<%p>[%u:0x%llx:0x%x]::processDPBandwidthNotification\n`
- `%lldus AppleThunderboltDPInAdapterOS<%p>[%u:0x%llx:0x%x]::processDPBandwidthNotification - status = %08x\n`
- `DPI BWAM Support Is Simulated`
- `%lldus AppleThunderboltDPInAdapter<%p>::earlyWakeThread - route = 0x%08llx, port = 0x%x, value = 0x%08x, dpi_hpd_unsuppressed = true\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::agcCallback - ERROR: fIOGraphicsControl = %p, newService = %p\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::getTunnelProhibited - tunnel_prohibited = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::enableDP - ERROR: enableDP failed with 0x%08x\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::reserveDPPortInternal - invoking fAGCThreadCall\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::getDPInVSECOffset - ERROR: finding fDPInVSECOffset failed with 0x%08x\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::createResources\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::setupNotifiers\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::agcThreadCall - WARNING: fIOGraphicsControl = NULL\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::finalize\n`
- `%lldus AppleThunderboltDPInAdapterCM<%p>(%x:%llx:%x)::controlPathListenerCallback - WARNING: fTerminated = true\n`
- `AppleThunderboltDPInAdapterOS2`
- `site.AppleThunderboltDPInAdapterOS2`
- `%lldus AppleThunderboltDPInAdapter<%p>::probe - service = %p\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::finalize - commandSleep( fWaitingForNotifiers )\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::free\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::earlyWake\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::getDPInVSECOffset - fDPInVSECOffset = 0x%x\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::agcCallback - tunneled_dp_in_use = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::agcThreadCall - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::controlPathListenerCallback - messageClients( kIOThunderboltMessageDPStateChange )\n`
- `site.AppleThunderboltDPInAdapterBase`
- `%lldus AppleThunderboltDPInAdapterOS<%p>[%u:0x%llx:0x%x]::processDPBandwidthNotification - notifying dp adapter at [%u:0x%llx:0x%x] about DP BW request\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::needsEarlyWake - lc[%d]->inDPPMode = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::isAdapterAvailableForClient - WARNING: fTerminated = true\n`
- `1211111212221212111222222111111111111222222222211122111112`
- `%lldus AppleThunderboltDPInAdapter<%p>::finalize - fWaitingForNotifiers woke up\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::getTunnelProhibited - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::prepareForTunnelDeactivation - fMuxType1InterruptSource: enabled = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::setupNotifiers - addMatchingNotification( AppleGraphicsControl )\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::setGPUIsMuxedAway - messageClients( kIOThunderboltMessageDPStateChange )\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::isAdapterAvailableForClient - tunnel_prohibited %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::prepareForTunnelDeactivation - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::needsEarlyWake - needs_early_wake = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::destroyResources\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::setTunnelProhibited - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::start - fStarted = true, calling registerService\n`
- `%lldus AppleThunderboltDPInAdapterCM<%p>(%x:%llx:%x)::setupNotifiers\n`
- `Common ALPM Support`
- `%lldus AppleThunderboltDPInAdapter<%p>::start - ERROR: failed to startup\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::lateSleep\n`
- `1211111212221212111222222111111111111122222222111222`
- `%lldus AppleThunderboltDPInAdapter<%p>::enableDP - enable = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::clearHPD - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::start - ERROR: failed to startup\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::isAdapterAvailableForClient - SUPER::isAdapterAvailableForClient = %d\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::start\n`
