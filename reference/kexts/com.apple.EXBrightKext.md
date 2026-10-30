# `com.apple.EXBrightKext`

- Name: EXBrightKext
- Version: `1.0.0`
- UUID: `97A4B3E0-C427-3BC4-A5EF-9368D9557EAB`
- Source version: `2300.52.5.0.0`
- Depends on: [`com.apple.EXBrightCalibrationConsumer`](com.apple.EXBrightCalibrationConsumer.md) 1.0.0, [`com.apple.iokit.CoreAnalyticsFamily`](com.apple.iokit.CoreAnalyticsFamily.md) 1.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.4, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/exbright`](../devicetree/root__exbright.md) | `EXBrightKext` | `exbright` |

## IOKit personalities (1) [KC]

### DeviceTreeName
- `CFBundleIdentifier`: `com.apple.EXBrightKext`
- `IOClass`: `EXBrightKext`
- `IOExclaveProxy`: `True`
- `IONameMatch`: `exbright`
- `IOPersonalityPublisher`: `com.apple.EXBrightKext`
- `IOProbeScore`: `10000`
- `IOProviderClass`: `IOService`
- `IOUserClientClass`: `EXBrightKextUserClient`


## C++ classes (7) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `BoundaryStats` | 0x48 | TelemetryDataI |
| `EXBrightCalibrationLoader` | 0x78 |  |
| `EXBrightKext` | 0x1b0 | IOHIDEventService → IOService → IORegistryEntry |
| `EXBrightKextUserClient` | 0xe0 | IOUserClient → IOService → IORegistryEntry |
| `HealthCounters` | 0x38 | TelemetryDataI |
| `TelemetryDataI` | 0x10 |  |
| `TelemetryManager` | 0x30 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000553c off=0x0091a600-0x0091fb3c addr=0xfffffe000791e600-0xfffffe0007923b3c r--/r--   __TEXT            
	sz=0x00000120 off=0x0091ac78-0x0091ad98 addr=0xfffffe000791ec78-0xfffffe000791ed98               __TEXT.__const            
	sz=0x00004da4 off=0x0091ad98-0x0091fb3c addr=0xfffffe000791ed98-0xfffffe0007923b3c               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x000181bc off=0x02c39690-0x02c5184c addr=0xfffffe0009c3d690-0xfffffe0009c5584c r-x/r-x   __TEXT_EXEC       
	sz=0x00017abc off=0x02c39690-0x02c5114c addr=0xfffffe0009c3d690-0xfffffe0009c5514c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000700 off=0x02c5114c-0x02c5184c addr=0xfffffe0009c5514c-0xfffffe0009c5584c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x0000020a off=0x049dbf40-0x049dc14a addr=0xfffffe000b9dff40-0xfffffe000b9e014a rw-/rw-   __DATA            
	sz=0x000000d8 off=0x049dbf40-0x049dc018 addr=0xfffffe000b9dff40-0xfffffe000b9e0018               __DATA.__data             
	sz=0x00000130 off=0x00000000-0x00000130 addr=0xfffffe000b9e0018-0xfffffe000b9e0148               __DATA.__common           (Zerofill)
	sz=0x00000002 off=0x00000000-0x00000002 addr=0xfffffe000b9e0148-0xfffffe000b9e014a               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000025f0 off=0x012d7828-0x012d9e18 addr=0xfffffe00082db828-0xfffffe00082dde18 rw-/rw-   __DATA_CONST      
	sz=0x00000030 off=0x012d7828-0x012d7858 addr=0xfffffe00082db828-0xfffffe00082db858         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000030 off=0x012d7858-0x012d7888 addr=0xfffffe00082db858-0xfffffe00082db888         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001fc0 off=0x012d7888-0x012d9848 addr=0xfffffe00082db888-0xfffffe00082dd848         __DATA_CONST.__const            
	sz=0x000001c0 off=0x012d9848-0x012d9a08 addr=0xfffffe00082dd848-0xfffffe00082dda08         __DATA_CONST.__kalloc_type      
	sz=0x00000380 off=0x012d9a08-0x012d9d88 addr=0xfffffe00082dda08-0xfffffe00082ddd88         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000090 off=0x012d9d88-0x012d9e18 addr=0xfffffe00082ddd88-0xfffffe00082dde18         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 242 at 0x04aee850
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     97A4B3E0-C427-3BC4-A5EF-9368D9557EAB
008: LC_SOURCE_VERSION           2300.52.5.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab9898 size=0x330
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `EXBrightKext`
- `CFBundleGetInfoString`: `Copyright © 2022 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.EXBrightKext`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `EXBrightKext`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91014`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91014`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2026 Apple Inc. All rights reserved.`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/EXBrightKext.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896253440`
- `_PrelinkExecutableRelativePath`: `EXBrightKext`
- `_PrelinkExecutableSize`: `130802`
- `_PrelinkExecutableSourceAddr`: `-2198896253440`
- `_PrelinkKmodInfo`: `-2198828351680`

## Strings (319) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `exdpFindServiceCallback`
- `\"TB_ASSERT: \" \"(server->processalssamplesandfetchmib != ((void*)0)) && \\\"implementation for processALSSamplesAndFetchMIB is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `[%s] [ERR] Could not create timer for lux sample dispatching\n`
- `EXBrightSILEnabledTrusted`
- `v104@?0{exbrightkextinterfacedebug_softboundarydebugstate__opt_s=B{exbrightkextinterfacedebug_softboundarydebugstate_s=BBffff{exbrightdefines_exbrightcolorfactorstb_s=Q(?={?={exbrightdefines_exbrightrgbfactorstb_s=fff}}{?={exbrightdefines_exbrightxyzfactorstb_s=fff}}{?={exbrightdefines_exbrightrgbfa`
- `\"TB_ASSERT: \" \"(server->getlastxtalkestimates != ((void*)0)) && \\\"implementation for getLastXTalkEstimates is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `[%s] [INF] Telemetry dump - Total display entries: %u\n`
- `fetchIndicatorStates_block_invoke_2`
- `[%s] EXBright calibration: alsPlacement=%u alsOrientation=%u success=%d\n`
- `[%s] [ERR] [getSILDebug] null ptr was provided\n`
- `[%s] [CL] [ERR] No calibration result for ALS with placement=%u and orientation=%u (i=%u)\n`
- `[%s] [CL] Sending calibration info to ALS client (i=%u, alsPlacement=%u, alsOrientation=%u, calibrated=%u)\n`
- `[%s] %s %s with value %d for display %d\n`
- `[%s] [ERR] Calibration process failed: EXBright returned nil!\n`
- `en`
- `I48@?0{exbrightkextinterface_exbrightindicatordata_v_s=C(?={?=^{exbrightkextinterface_exbrightindicatordata_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}8`
- `\"TB_ASSERT: \" \"(server->setarbitraryalscalibration != ((void*)0)) && \\\"implementation for setArbitraryALSCalibration is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `site.HealthCounters`
- `[%s] [ERR] Invalid eventName!\n`
- `[%s] Created telemetry dictionary for display %u\n`
- `\"TB_ASSERT: \" \"(server->setindicatorstate != ((void*)0)) && \\\"implementation for setIndicatorState is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `[%s] [INF] Session ID = %s\n`
- `[%s] [CL] [ERR] This is *bad*! Cannot register another client. There are more clients than expected (_alsCalibrationClientsCnt=%d, _expectedALSCalibrationClientsCnt=%d).\n`
- `[%s] [ERR] [getSILDebug] Insufficient buffer size (got=%u needed=%zu).\n`
- `[%s] [ERR] [%s] EXDisplayPipe is already configured!\n`
- `[%s] [CL] [ERR] Could not add timer for calibration to the workloop, res: %d\n`
- `[%s] Disabling nits override\n`
- `CoreAnalyticsHub`
- `totalBrightnessFailures`
- `TelemetryManager`
- `site.TelemetryManager`
- `secure-sample-timeout`
- `[%s] [ERR] [%s] Could not create matching dictionaries!\n`
- `I16@?0^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}8`
- `[%s] [ERR] Aggregated telemetry array not initialized!\n`
- `displayID`
- `SessionID`
- `EXBrightKext`
- `exbright_alss_test_calibration`
- `\"TB_ASSERT: \" \"(exbrightkextinterface_exbrightindicatordata__decode(msg, &item) == TB_ERROR_SUCCESS) && \\\"failed to decode type: EXBrightKextInterface.EXBrightIndicatorData\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `[%s] [CL] [%s] Wating for ALS companion drivers (_alsCalibrationClientsCnt=%d)\n`
- `percentContrastFailures`
- `[%s] [INF] \tRampUp State = %u%% (%u)\n`
- `[%s] [ERR] Failed to cast CoreAnalyticsHub\n`
- `EXBrightCalibrationLoader`
- `[%s] [CL] Calibration process will start in %ums (_alsCalibrationCnt=%d)\n`
- `\"TB_FATAL: \" \"invalid tag in '[ALSDefines.CalibrationBufferElement (aka. UInt8)]' metadata: 0x%x\" @%s:%d`
- `[%s] [ERR] Failed to initialize OSArray with capacity %u\n`
- `registerALSCalibrationClient_block_invoke`
- `[%s] [DEB] user client start\n`
- `[%s] [ERR] Provided output buffer is nullptr\n`
- `[%s] [ERR] EXBrightKextInterface.processALSSamplesAndFetchMIB failed! (%u)\n`
- `v48@?0{exbrightkextinterface_exbrightindicatordata_v_s=C(?={?=^{exbrightkextinterface_exbrightindicatordata_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}8`
- `v72@?0{exbrightkextinterface_exbrighttelemetryhealthdata__opt_s=B{exbrightkextinterface_exbrighttelemetryhealthdata_s={exbrightkextinterface_exbrighttelemetryhealthcounters_s=IIIIIIIIQ}{exbrightkextinterface_exbrighttelemetryboundarystats_s=IQ}}}8`
- `v12@?0B8`
- `[%s] EXBright xtalk calibrated: %d\n`
- `[%s] [ERR] Failed to submit telemetry '%s' for display %u, error: 0x%x\n`
- `EXBrightKextUserClient`
- `EXBrightSILStateUntrusted`
- `[%s] calibrate XTalk, size = %lu\n`
- `[%s] [ERR] [%s] kLoadALSSCalibration failed! Returned: 0x%x.\n`
- `[%s] [ERR] Failed to set CoreAnalytics service\n`
- `[%s] [ERR] Buffer for xtalk estimate is too small to fit\n`
- `v24@?0{exbrightkextinterfacedebug_exbrightalsarbitrarycalibrationresponse__opt_s=B{exbrightkextinterfacedebug_exbrightalsarbitrarycalibrationresponse_s=CII}}8`
- `[%s] [DEB] user client stop\n`
- `[%s] [ERR] Failed to create event source!\n`
- `[%s] [ERR] tb_endpoint_create_with_value failed for the release service!\n`
- `[%s] [ERR] Failed to set UI brightness\n`
- `\"TB_ASSERT: \" \"(server->calibratextalk != ((void*)0)) && \\\"implementation for calibrateXTalk is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `[%s] [ERR] Failed to transform aggregated telemetry to OSDictionary for type %s\n`
- `[%s] [INF] = Display %u =\n`
- `EXBrightKext.cpp`
- `AppleSPUALSLuxDriver`
- `[%s] [ERR] [%s] Received nullptr!\n`
- `1222222`
- `[%s] [ERR] Failed to send event!\n`
- `[%s] [CL] [ERR] Could not create a timer for calibration.\n`
- `registerALSCalibrationClient`
- `[%s] [CL] [ERR] This is *bad*! A client with placement=%u and orientation=%u already exists!\n`
- `EXBrightALSCalibrationInterest`
- `[%s] [ERR] [%s] Could not create a matching dictionary!\n`
- `[%s] [%s] kLoadALSSCalibration suceeded!\n`
- `[%s] [ERR] Failed to create iterator for telemetry dump of display %u\n`
- `[%s] [CL] [ERR] No ALS is configured in EDT.\n`
- `[%s] [DEB] Dumping aggregated telemetry...\n`
- `EXBrightUIBrightness`
- `coreAnalyticsMatchNotificationHandler`
- `[%s] [ERR] No DeviceTree service found!\n`
- `EXBrightKextInterface_c.c`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `[%s] [CL] [ERR] [%s] Late! Calibration process has already started!\n`
- `[%s] EXBright AlsS calibrated: %d\n`
- `[%s] [ERR] [%s] No EXDisplayPipe!\n`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS) && \\\"failed to wrap packed buffer\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `I52@?0{exbrightkextinterface_exbrightalscalibrationresults__opt_s=B{exbrightkextinterface_exbrightalscalibrationresults_s=[3{exbrightkextinterface_exbrightalscalibrationresult_s=IIB}]C}}8`
- `totalCheckedFrames`
- `percentContrastFailuresSessionStart`
- `[%s] [ERR] Could not add timer for submitting telemetry to the workloop, res: %d\n`
- `EXBrightMIBOverrideDisplayID`
- `^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16`
- `\"TB_FATAL: \" \"invalid tag in '[ALSDefines.ALSCFSNBufferElement (aka. UInt8)]' metadata: 0x%x\" @%s:%d`
- `percentBrightnessFailuresRampUp`
- `[%s] [ERR] Failed to set telemetry dictionary in array for display id %u\n`
- `EXBrightMIB`
- `\"TB_ASSERT: \" \"(server->setuibrightness != ((void*)0)) && \\\"implementation for setUIBrightness is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `[%s] [ERR] Failed to send event to CoreAnalytics for type %s\n`
- `EXBrightUserspaceForwardedFDRBundles`
- `[%s] [ERR] Failed to calibrate XTalk (%u)\n`
- `[%s] [ERR] %s not found!\n`
- `\"TB_ASSERT: \" \"(server->start != ((void*)0)) && \\\"implementation for Start is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->overridepanelbrightness != ((void*)0)) && \\\"implementation for overridePanelBrightness is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `121112`
- `TotalDurationMS`
- `[%s] EXBrightKext::start\n`
- `[%s] [ERR] Could not add _upcallNotificationES to workloop!\n`
- `[%s] [CL] [ERR] Bad input!\n`
- `[%s] [CL] [ERR] Calibration failed (err=%u)\n`
- `[%s] [CL] [ERR] Init failed!\n`
- `EXBrightToggleFakeMIBStreamingDisplayID`
- `\"TB_ASSERT: \" \"(server->overridesoftboundaryhint != ((void*)0)) && \\\"implementation for overrideSoftBoundaryHint is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `[%s] [ERR] No telemetry data found for type %s\n`
- `[%s] [CL] Starting calibration process! (_alsCalibrationClientsCnt=%u, _expectedALSCalibrationClientsCnt=%u)\n`
- `ProtectedAccess`
- `EXBrightMIBOverride`
- `[%s] Enabling panel brightness override: %d\n`
- `[%s] [ERR] [%s] The notifier already exists!\n`
- `[%s] [ERR] [%s] Incorrect buffer size (got=%d needed=%lu).\n`
- `EXBrightToggleFakeMIBStreaming`
- `[%s] [ERR] Failed to initialize TelemetryManager\n`
- `[%s] [CL] [ERR] Calibration process failed: EXBright returned nil!\n`
- `[%s] [ERR] Out type is too small! Expected at least %u bytes, got %zu bytes\n`
- `\"TB_ASSERT: \" \"(u8__v_decode(msg, &calibration) == TB_ERROR_SUCCESS) && \\\"failed to decode type: UInt8\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `[%s] [ERR] No telemetry to dump!\n`
- `[%s] [ERR] Failed to create command gate!\n`
- `[%s] [ERR] Could not add timer for lux sample dispatching timer to workloop, res: %d\n`
- `[%s] Enabling soft boundary override: %d\n`
- `[%s] %s called\n`
- `\"TB_ASSERT: \" \"(server->calibrateambientlightsensors != ((void*)0)) && \\\"implementation for calibrateAmbientLightSensors is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `[%s] [INF] Total Duration = %llu ms\n`
- `[%s] A new ALS calibration path will be used on this product!\n`
- `[%s] [ERR] Received calibration interest but calibration loader is missing.\n`
- `[%s] [DEB] upcallNotificationCallback()\n`
- `\"TB_ASSERT: \" \"(server->getindicatorstates != ((void*)0)) && \\\"implementation for getIndicatorStates is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `I72@?0{exbrightkextinterface_exbrighttelemetryhealthdata__opt_s=B{exbrightkextinterface_exbrighttelemetryhealthdata_s={exbrightkextinterface_exbrighttelemetryhealthcounters_s=IIIIIIIIQ}{exbrightkextinterface_exbrighttelemetryboundarystats_s=IQ}}}8`
- `[%s] [ERR] Invalid eventPayload!\n`
- `[%s] [CL] _expectedALSCalibrationClientsCnt = %u _waitTillUserspaceForwardsFDRBundles=%d\n`
- `v20@?0Q8C16`
- `[%s] [ERR] null buffer was provided, can't obtain soft boundary debug state\n`
- `[%s] Fake streaming %sabled for display %u\n`
- `[%s] [ERR] Failed to create dictionary with capactiy %d\n`
- `[%s] [INF] Activations = %u\n`
- `i8@?0`
- `[%s] [INF] Updating sample timeout %ums -> %ums\n`
- `EXBrightUIBrightnessValue`
- `[%s] [ERR] [%s:%d] Disallowed!\n`
- `[%s] [INF] [%s] exbright_alss_enabled=%d\n`
- `EXBrightMessageFunction`
- `[%s] [ERR] Provided buffer is too small to fix SoftBoundaryDebug (%u/%lu)\n`
- `[%s] [ERR] Could not configure upcall notifications!\n`
- `[%s] [ERR] EXBrightColorFactors - neither case matched\n`
- `\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `I12@?0B8`
- `\"TB_ASSERT: \" \"(server->calibratextalkfromblob != ((void*)0)) && \\\"implementation for calibrateXTalkFromBlob is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `I48@?0{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}8`
- `totalContrastFailuresRampUp`
- `[%s] [ERR] Failed to add telemetry data to dictionary for type %s for display %u\n`
- `userspaceForwardedFDRBundles`
- `[%s] [ERR] __init failed for the debug service (error=%d)!\n`
- `[%s] [ERR] Failed to allocate telemetry IOLock\n`
- `121111121222121211111112111111121111112222212111111112`
- `[%s] [ERR] Unknown type of xtalk estimate\n`
- `\"TB_FATAL: \" \"overflow detected when adding\" @%s:%d`
- `[%s] TelemetryManager ready to send events!\n`
- `[%s] [ERR] Could not create timer for submitting telemetry\n`
- `EXBrightToggleFakeMIBStreamingEnable`
- `EXBrightSILStateUntrustedEnable`
- `dis`
- `AppleSPUALSColorDriver`
- `I56@?0{exbrightkextinterface_exbrightmibdata_v__opt_s=B{exbrightkextinterface_exbrightmibdata_v_s=C(?={?=^{exbrightkextinterface_exbrightmibdata_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}8`
- `totalBrightnessFailuresRampUp`
- `percentBrightnessFailures`
- `[%s] [ERR] Failed to alloc BoundaryStats\n`
- `\"TB_FATAL: \" \"invalid tag in '[UInt8]' metadata: 0x%x\" @%s:%d`
- `totalBrightnessFailuresSteady`
- `[%s] [INF] \tSession Start = %u%% (%u)\n`
- `v56@?0{exbrightkextinterface_exbrightmibdata_v__opt_s=B{exbrightkextinterface_exbrightmibdata_v_s=C(?={?=^{exbrightkextinterface_exbrightmibdata_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}8`
- `Enabling`
- `\"TB_ASSERT: \" \"(server->getsoftboundarystate != ((void*)0)) && \\\"implementation for getSoftBoundaryState is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `[%s] [ERR] Failed to initalize HealthCounters\n`
- `Disabling`
- `[%s] [DEB] [%s] Sending kLoadALSSCalibration to EXDisplayPipe.\n`
- `\"TB_ASSERT: \" \"(vErr == TB_ERROR_SUCCESS) && \\\"tb_message_subrange failed\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `[%s] [ERR] Invalid telemetry data for key: %s\n`
- `[%s] [ERR] Failed to create %s matching dictionary\n`
- `\"TB_ASSERT: \" \"(server->overridesensortemperature != ((void*)0)) && \\\"implementation for overrideSensorTemperature is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `[%s] [ERR] Failed to alloc TelemetryManager!\n`
- `[%s] [INF] Total Frames Checked = %u\n`
- `[%s] [ERR] [%s] Invalid display id %u\n`
- `[%s] Disabling soft boundary override\n`
- `BoundaryStats`
- `[%s] [ERR] Could not create TelemetryManager\n`
- `EXBrightMIBOverrideValue`
- `I8@?0`
- `[%s] [CL] [%s] The calibration process has already finished!\n`
- `[%s] [INF] \t=== Contrast Failures ===\n`
- `[%s] [ERR] Failed to setup upcall notifications!\n`
- `[%s] [ERR] Fetched MIB data with invalid display id %u\n`
- `I88@?0{exbrightkextinterfacedebug_exbrightxtalkestimatesframedata__opt_s=B{exbrightkextinterfacedebug_exbrightxtalkestimatesframedata_s=QIffQ{exbrightkextinterfacedebug_exbrightxtalkestimates_s=Q(?={?={exbrightkextinterfacedebug_exbrightalsschannelestimates_s=Q(?={?=[2f]}{?=[5f]})}})}}}8`
- `HealthCounters`
- `[%s] [ERR] Failed to cast TelemetryData to HealthCounters\n`
- `percentBrightnessFailuresSteady`
- `v52@?0{exbrightkextinterface_exbrightalscalibrationresults__opt_s=B{exbrightkextinterface_exbrightalscalibrationresults_s=[3{exbrightkextinterface_exbrightalscalibrationresult_s=IIB}]C}}8`
- `als-new-calibration-path`
- `v24@?0Q8r^{exbrightkextinterface_exbrightmibdata_s=QfBfC}16`
- `v24@?0Q8r^{exbrightkextinterface_exbrightindicatordata_s=C{exbrightkextinterface_exbrightindicatorstate_s=Q(?={?=S})}}16`
- `[%s] Enabling sensor temperature override: %d\n`
- `toleranceMask`
- `[%s] [ERR] Failed to create iterator for telemetry dump\n`
- `Activations`
- `[%s] [ERR] Received '%s' but calibration loader is missing.\n`
- `v48@?0{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}8`
- `isALSSEnabled`
- `[%s] [ERR] Failed to alloc HealthCounters\n`
- `[%s] [INF] == HealthCounters Summary ==\n`
- `[%s] [INF] Max Tolerance Consumed (ms) = %u\n`
- `[%s] [ERR] Failed to cast TelemetryDataI to BoundaryStats\n`
- `\"TB_FATAL: \" \"overflow detected when multiplying\" @%s:%d`
- `\"TB_FATAL: \" \"invalid value: unexpected case value, %llx\" @%s:%d`
- `[%s] [INF] Tolerance Mask = 0x%llx\n`
- `TelemetryDataI`
- `[%s] [ERR] __init failed for the release service (error=%d)!\n`
- `[%s] [ERR] Invalid display id %d for property %s\n`
- `v40@?0{exbrightkextinterface_exbrightindicatordata__opt_s=B{exbrightkextinterface_exbrightindicatordata_s=C{exbrightkextinterface_exbrightindicatorstate_s=Q(?={?=S})}}}8`
- `[%s] [DEB] Dispatched MIB - CBMIBData.(ts=%llu mib=%d lux=%d}.\n`
- `\"TB_ASSERT: \" \"(server->configureupcallnotification != ((void*)0)) && \\\"implementation for configureUpcallNotification is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `[%s] [ERR] Failed to create OSNumber for display id %u\n`
- `[%s] [ERR] Display dictionary missing displayID key\n`
- `setArbitraryALSCalibration`
- `[%s] [INF] \tTotal = %u%% (%u)\n`
- `site.EXBrightKext`
- `[%s] [ERR] buffer size provided (%u) is too small to fit soft boundary debug state (%lu)\n`
- `[%s] [ERR] [%s] Could not create a matching notification!\n`
- `\"TB_FATAL: \" \"invalid tag in '[EXBrightKextInterface.EXBrightIndicatorData]' metadata: 0x%x\" @%s:%d`
- `I40@?0{exbrightkextinterface_exbrightindicatordata__opt_s=B{exbrightkextinterface_exbrightindicatordata_s=C{exbrightkextinterface_exbrightindicatorstate_s=Q(?={?=S})}}}8`
- `[%s] %s=0b%d\n`
- `[%s] [ERR] Failed to initialize BoundaryStats\n`
- `site.EXBrightCalibrationLoader`
- `alsCalibrationTimerCallback`
- `\"TB_FATAL: \" \"invalid tag in '[EXBrightKextInterface.EXBrightMIBData]' metadata: 0x%x\" @%s:%d`
- `I24@?0{exbrightkextinterfacedebug_exbrightalsarbitrarycalibrationresponse__opt_s=B{exbrightkextinterfacedebug_exbrightalsarbitrarycalibrationresponse_s=CII}}8`
- `maxToleranceConsumptionMs`
- `com.apple.EXBright.BoundaryStats`
- `121112121212122`
- `userspaceForwardedFDRBundles_block_invoke`
- `[%s] [ERR] Could not add timer for fake streaming to the workloop, res: %d\n`
- `[%s] [ERR] tb_endpoint_create_with_value failed for the debug service!\n`
- `[%s] [ERR] Failed to get indicator state\n`
- `setupALSKextMatchingNotification`
- `totalContrastFailuresSessionStart`
- `[%s] [ERR] Invalid display id %u\n`
- `[%s] [INF] == BoundaryStats Summary ==\n`
- `[%s] [ERR] [%s] newService == nullptr!\n`
- `[%s] [%s] calibrationSize = %lu calibrationResponseSize = %u\n`
- `\"TB_ASSERT: \" \"(server->fetchtelemetryhealthdata != ((void*)0)) && \\\"implementation for fetchTelemetryHealthData is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->getsildebug != ((void*)0)) && \\\"implementation for getSILDebug is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `[%s] [ERR] Failed to create calibrateALS event source!\n`
- `[%s] [ERR] Could not create timer for fake streaming\n`
- `calibration-source`
- `[%s] [DEB] [SILDebug] IOMemoryDescriptor=false size=%u\n`
- `percentContrastFailuresSteady`
- `122222222`
- `[%s] [CL] Registered a new ALS calibration client with placement=%u and orientation=%u (_alsCalibrationClientsCnt=%d).\n`
- `site.EXBrightKextUserClient`
- `[%s] [DEB] terminating user client\n`
- `[%s] [ERR] null buffer pointer was provided for obtaining last xtalk estimates\n`
- `alsKextMatchNotificationHandler`
- `setArbitraryALSCalibration_block_invoke_2`
- `als-types`
- `com.apple.EXBright.HealthCounters`
- `[%s] [ERR] Failed to create iterator over telemetry array!\n`
- `[%s] [ERR] Failed to update telemetry data for type %s for display %u\n`
- `[%s] [ERR] [getSILDebug] invalid display id %d\n`
- `exdpLoadCalibration`
- `\"TB_ASSERT: \" \"(server->handlehibernationwake != ((void*)0)) && \\\"implementation for handleHibernationWake is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `I104@?0{exbrightkextinterfacedebug_softboundarydebugstate__opt_s=B{exbrightkextinterfacedebug_softboundarydebugstate_s=BBffff{exbrightdefines_exbrightcolorfactorstb_s=Q(?={?={exbrightdefines_exbrightrgbfactorstb_s=fff}}{?={exbrightdefines_exbrightxyzfactorstb_s=fff}}{?={exbrightdefines_exbrightrgbfa`
- `[%s] Disabling sensor temperature override\n`
- `[%s] [INF] \t=== Brightness Failures ===\n`
- `[%s] [ERR] Failed to create telemetry dictionary for display %u\n`
- `[%s] [ERR] Failed to set indicator state\n`
- `[%s] [ERR] No CoreAnalytics Service set, cannot send events!\n`
- `[%s] [CL] [ERR] [%s] Not configured!\n`
- `totalContrastFailures`
- `totalContrastFailuresSteady`
- `percentBrightnessFailuresSessionStart`
- `[%s] [DEB] [SILDebug] IOMemoryDescriptor=true size=%u\n`
- `[%s] [ERR] Failed to create OSString eventName %s\n`
- `[%s] Configuring upcall notifications with ID = %u\n`
- `EXBrightMIBOverrideEnable`
- `EXBrightSILStateTrusted`
- `[%s] [ERR] Failed to setup TelemetryManager!\n`
- `[%s] [ERR] Empty telemetry array, nothing to update\n`
- `[%s] [ERR] Failed to calibrate ALS (%u)\n`
- `[%s] [ERR] No telemetry dictionary found for display %u\n`
- `[%s] [DEB] EXBrightKextUserClient::externalMethod - %u\n`
- `\"TB_FATAL: \" \"unrecognized selector: %llu\" @%s:%d`
- `totalBrightnessFailuresSessionStart`
- `percentContrastFailuresRampUp`
- `site.TelemetryDataI`
- `12`
- `[%s] [CL] [ERR] [%s] Calibration process has already started!\n`
- `1211111212221212111111111111`
- `EXBrightUIBrightnessDisplayID`
- `v88@?0{exbrightkextinterfacedebug_exbrightxtalkestimatesframedata__opt_s=B{exbrightkextinterfacedebug_exbrightxtalkestimatesframedata_s=QIffQ{exbrightkextinterfacedebug_exbrightxtalkestimates_s=Q(?={?={exbrightkextinterfacedebug_exbrightalsschannelestimates_s=Q(?={?=[2f]}{?=[5f]})}})}}}8`
- `[%s] [INF] \tSteady State = %u%% (%u)\n`
- `Unknown`
- `site.BoundaryStats`
- `EXBrightSILStateUntrustedDisplayID`
- `[%s] [ERR] Unknown channel count for estimates\n`
- `exdpFindService`
