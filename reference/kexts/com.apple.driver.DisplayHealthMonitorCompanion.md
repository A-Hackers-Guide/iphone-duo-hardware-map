# `com.apple.driver.DisplayHealthMonitorCompanion`

- Name: DisplayHealthMonitorCompanion
- Version: `1.0.0d1`
- UUID: `56C95294-B650-39C9-B724-18A23CE06A8F`
- Source version: `5.0.0.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.4.1, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/display-health-monitor`](../devicetree/root__display-health-monitor.md) | `DisplayHealthMonitorCompanion` | `display-health-monitor` |

## IOKit personalities (1) [KC]

### DeviceTreeName
- `CFBundleIdentifier`: `com.apple.driver.DisplayHealthMonitorCompanion`
- `IOClass`: `DisplayHealthMonitorCompanion`
- `IOExclaveProxy`: `True`
- `IONameMatch`: `display-health-monitor`
- `IOPersonalityPublisher`: `com.apple.driver.DisplayHealthMonitorCompanion`
- `IOProbeScore`: `10000`
- `IOProviderClass`: `IOService`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `DisplayHealthMonitorCompanion` | 0xc0 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000013ae off=0x009183e0-0x0091978e addr=0xfffffe000791c3e0-0xfffffe000791d78e r--/r--   __TEXT            
	sz=0x00000028 off=0x00918a08-0x00918a30 addr=0xfffffe000791ca08-0xfffffe000791ca30               __TEXT.__const            
	sz=0x00000d5e off=0x00918a30-0x0091978e addr=0xfffffe000791ca30-0xfffffe000791d78e               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00003ddc off=0x02c34940-0x02c3871c addr=0xfffffe0009c38940-0xfffffe0009c3c71c r-x/r-x   __TEXT_EXEC       
	sz=0x00003acc off=0x02c34940-0x02c3840c addr=0xfffffe0009c38940-0xfffffe0009c3c40c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000310 off=0x02c3840c-0x02c3871c addr=0xfffffe0009c3c40c-0xfffffe0009c3c71c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x049dbd40-0x049dbe40 addr=0xfffffe000b9dfd40-0xfffffe000b9dfe40 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049dbd40-0x049dbe08 addr=0xfffffe000b9dfd40-0xfffffe000b9dfe08               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9dfe08-0xfffffe000b9dfe40               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000998 off=0x012d6c60-0x012d75f8 addr=0xfffffe00082dac60-0xfffffe00082db5f8 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x012d6c60-0x012d6c68 addr=0xfffffe00082dac60-0xfffffe00082dac68         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x012d6c68-0x012d6c70 addr=0xfffffe00082dac68-0xfffffe00082dac70         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000007a0 off=0x012d6c70-0x012d7410 addr=0xfffffe00082dac70-0xfffffe00082db410         __DATA_CONST.__const            
	sz=0x00000040 off=0x012d7410-0x012d7450 addr=0xfffffe00082db410-0xfffffe00082db450         __DATA_CONST.__kalloc_type      
	sz=0x00000188 off=0x012d7450-0x012d75d8 addr=0xfffffe00082db450-0xfffffe00082db5d8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000020 off=0x012d75d8-0x012d75f8 addr=0xfffffe00082db5d8-0xfffffe00082db5f8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 102 at 0x04aee61c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     56C95294-B650-39C9-B724-18A23CE06A8F
008: LC_SOURCE_VERSION           5.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab97d8 size=0x90
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `DisplayHealthMonitorCompanion`
- `CFBundleGetInfoString`: `Copyright © 2026 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.DisplayHealthMonitorCompanion`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `DisplayHealthMonitorCompanion`
- `CFBundleNumericVersion`: `16785409`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
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
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/DisplayHealthMonitorCompanion.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896262176`
- `_PrelinkExecutableRelativePath`: `DisplayHealthMonitorCompanion`
- `_PrelinkExecutableSize`: `23586`
- `_PrelinkExecutableSourceAddr`: `-2198896262176`
- `_PrelinkKmodInfo`: `-2198828352192`

## Strings (53) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `global_health`
- `hw_link_failures`
- `121111121222121211111122`
- `dhm-ca-interval`
- `DisplayHealthMonitorCompanion::start: IOService::start failed\n`
- `dhm-log-interval`
- `sca_driver`
- `\"TB_FATAL: \" \"unrecognized selector: %llu\" @%s:%d`
- `DisplayHealthMonitorCompanion`
- `DisplayHealthMonitorCompanion::logHealthCheck: display=%llu powerMask=%llu | globalHealth=%llu periodicHealthCheck=%llu failureRatio=%llu%%\n`
- `sca_algorithm`
- `scl_driver`
- `\"TB_ASSERT: \" \"(server->snapshot != ((void*)0)) && \\\"implementation for snapshot is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->updatepower != ((void*)0)) && \\\"implementation for updatePower is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `DisplayHealthMonitorCompanion::start: startTightbeam failed\n`
- `DisplayHealthMonitorCompanion::initTightbeam: tb_endpoint_create_with_value failed\n`
- `DisplayHealthMonitorCompanion::loggingTimerFired: snapshot failed (%u)\n`
- `sil_health`
- `tcon_hpd`
- `\"TB_ASSERT: \" \"(server->getpowermask != ((void*)0)) && \\\"implementation for getPowerMask is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `DisplayHealthMonitorCompanion::initTightbeam: exclaveStart failed\n`
- `link`
- `DisplayHealthMonitorCompanion: CoreAnalyticsSendEvent failed (display=%llu, powerMask=%llu, err=%d)\n`
- `DisplayHealthMonitorCompanionInterface_c.c`
- `\"TB_ASSERT: \" \"(server->incrementhealthcheckcounters != ((void*)0)) && \\\"implementation for incrementHealthCheckCounters is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `brightness`
- `DisplayHealthMonitorCompanion::initTightbeam: Companion interface init error (%u)\n`
- `site.DisplayHealthMonitorCompanion`
- `DisplayHealthMonitorCompanion::start: startCoreAnalyticsTimer failed\n`
- `v544@?0{displayhealthmonitorcompanioninterface_displaytelemetry_s=Q[2{displayhealthmonitorcompanioninterface_displaytelemetryrecord_s=Q[2{displayhealthmonitorcompanioninterface_displaytelemetrypowerbucket_s=Q{displayhealthmonitortelemetryclient_healthcheckcounters_s=QQQQQQQQQQQQQQQ}}]}]}8`
- `pipe`
- `tcon_health`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `dhm-ignore-empty`
- `DisplayHealthMonitorCompanion::startLoggingTimer: failed to create timer\n`
- `DisplayHealthMonitorCompanion: logging enabled with interval %u seconds (boot-arg)\n`
- `DisplayHealthMonitorCompanion::coreAnalyticsTimerFired: snapshot failed (%u)\n`
- `display_id`
- `display_power_mask`
- `periodic_health_check`
- `^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16`
- `DisplayHealthMonitorCompanion: CoreAnalytics interval overridden to %u seconds (boot-arg)\n`
- `DisplayHealthMonitorCompanion::init: IOService::init failed\n`
- `dcp_transport_health`
- `non_authentic_panel`
- `\"TB_ASSERT: \" \"(server->getmaxpowerstates != ((void*)0)) && \\\"implementation for getMaxPowerStates is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `DisplayHealthMonitorCompanion::startCoreAnalyticsTimer: failed to create timer\n`
- `tcon_crc`
- `com.apple.display.HealthCheck`
- `I544@?0{displayhealthmonitorcompanioninterface_displaytelemetry_s=Q[2{displayhealthmonitorcompanioninterface_displaytelemetryrecord_s=Q[2{displayhealthmonitorcompanioninterface_displaytelemetrypowerbucket_s=Q{displayhealthmonitortelemetryclient_healthcheckcounters_s=QQQQQQQQQQQQQQQ}}]}]}8`
- `I8@?0`
- `I16@?0Q8`
