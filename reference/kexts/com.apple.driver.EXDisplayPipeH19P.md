# `com.apple.driver.EXDisplayPipeH19P`

- Name: EXDisplayPipeH19P
- Version: `1.0.0`
- UUID: `F0A97EE9-828B-3B5E-B021-4DB4F9853C5E`
- Source version: `9.2.10.5.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.4.1, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (2) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/exdisplaypipe`](../devicetree/root__arm-io__exdisplaypipe.md) | `EXDisplayPipe` | `exdisplaypipe,t8160` |
| [`/arm-io/exdisplaypipe1`](../devicetree/root__arm-io__exdisplaypipe1.md) | `EXDisplayPipe` | `exdisplaypipe1,t8160` |

## IOKit personalities (1) [KC]

### EXDisplayPipe
- `CFBundleIdentifier`: `com.apple.driver.EXDisplayPipeH19P`
- `IOClass`: `EXDisplayPipe`
- `IOExclaveProxy`: `True`
- `IONameMatch`:
  - `exdisplaypipe,t8160`
  - `exdisplaypipe1,t8160`
- `IOPersonalityPublisher`: `com.apple.driver.EXDisplayPipeH19P`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `EXDisplayPipe` | 0x958 | IOService → IORegistryEntry |
| `EXDisplayPipeUserClient` | 0xe0 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000030b2 off=0x0091fb40-0x00922bf2 addr=0xfffffe0007923b40-0xfffffe0007926bf2 r--/r--   __TEXT            
	sz=0x00000050 off=0x009201b8-0x00920208 addr=0xfffffe00079241b8-0xfffffe0007924208               __TEXT.__const            
	sz=0x000029ea off=0x00920208-0x00922bf2 addr=0xfffffe0007924208-0xfffffe0007926bf2               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00009ebc off=0x02c51850-0x02c5b70c addr=0xfffffe0009c55850-0xfffffe0009c5f70c r-x/r-x   __TEXT_EXEC       
	sz=0x00009a0c off=0x02c51850-0x02c5b25c addr=0xfffffe0009c55850-0xfffffe0009c5f25c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000004b0 off=0x02c5b25c-0x02c5b70c addr=0xfffffe0009c5f25c-0xfffffe0009c5f70c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000138 off=0x049dc150-0x049dc288 addr=0xfffffe000b9e0150-0xfffffe000b9e0288 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x049dc150-0x049dc214 addr=0xfffffe000b9e0150-0xfffffe000b9e0214               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b9e0218-0xfffffe000b9e0278               __DATA.__common           (Zerofill)
	sz=0x00000010 off=0x00000000-0x00000010 addr=0xfffffe000b9e0278-0xfffffe000b9e0288               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000012e8 off=0x012d9e18-0x012db100 addr=0xfffffe00082dde18-0xfffffe00082df100 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x012d9e18-0x012d9e30 addr=0xfffffe00082dde18-0xfffffe00082dde30         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x012d9e30-0x012d9e40 addr=0xfffffe00082dde30-0xfffffe00082dde40         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000fb0 off=0x012d9e40-0x012dadf0 addr=0xfffffe00082dde40-0xfffffe00082dedf0         __DATA_CONST.__const            
	sz=0x00000080 off=0x012dadf0-0x012dae70 addr=0xfffffe00082dedf0-0xfffffe00082dee70         __DATA_CONST.__kalloc_type      
	sz=0x00000258 off=0x012dae70-0x012db0c8 addr=0xfffffe00082dee70-0xfffffe00082df0c8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000038 off=0x012db0c8-0x012db100 addr=0xfffffe00082df0c8-0xfffffe00082df100         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 157 at 0x04aeec18
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     F0A97EE9-828B-3B5E-B021-4DB4F9853C5E
008: LC_SOURCE_VERSION           9.2.10.5.0
009: LC_FUNCTION_STARTS          offset=0x004ab9bc8 size=0x118
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `EXDisplayPipeH19P`
- `CFBundleGetInfoString`: `Copyright © 2022 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.EXDisplayPipeH19P`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `EXDisplayPipeH19P`
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
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
  - `2`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/EXDisplayPipeH19P.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896231616`
- `_PrelinkExecutableRelativePath`: `EXDisplayPipeH19P`
- `_PrelinkExecutableSize`: `58254`
- `_PrelinkExecutableSourceAddr`: `-2198896231616`
- `_PrelinkKmodInfo`: `-2198828351152`

## Strings (250) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `EXDisplayPipe::%s: m_frame_num_stale_timeout is %d\n`
- `EXDisplayPipe::%s Exits <-- \n`
- `EXDisplayPipe::%s SCA IOWorkLoop creation failed\n`
- `setup_timers`
- `pipe_failure_ratio`
- `EXDisplayPipe: error: showIndicator(%u, ...) failed\n`
- `[EXDisplayPipe]: %s: m_display_index %d \n`
- `[EXDisplayPipe]: Hide Indicator %s\n`
- `\"watchdog timed out\" @%s:%d`
- `crc_failures_beyond_thresh`
- `display-index`
- `EXDisplayPipe::%s exclaveStart failed\n`
- `[EXDisplayPipe]: %s: edk_service %s \n`
- `EXDisplayPipe::%s Telemetry IOWorkLoop creation failed\n`
- `v13@?0{exdisplaypipetightbeamcommon_exdisplaypipescasessionstatus_s=[5B]}8`
- `EXDisplayPipe: error: args->structureOutputSize (0x%x) != sizeof(EXDisplayPipeHealthStats) (0x%lx)\n`
- `EXDisplayPipe: error: setPower(%u) failed\n`
- `FAIL!!`
- `v48@?0{exdisplaypipetightbeamcommon_exdisplaypipeframeinfo__opt_s=B{exdisplaypipetightbeamcommon_exdisplaypipeframeinfo_s=Bffffffff}}8`
- `globalhealth_failure_time`
- `hwlinkfailures_cp`
- `average_sca_variance`
- `brightness_failure_ratio`
- `ChillPillMetrics`
- `[EXDisplayPipe]: %s: exclave_service_prop is NULL \n`
- `EXDisplayPipe: error: getFrameInfo(...) failed\n`
- `silHealth_failure_counter`
- `scldriver_failure_time`
- `v392@?0{exdisplaypipetightbeamcommon_exdisplaypipecompanionstatus__opt_s=B{exdisplaypipetightbeamcommon_exdisplaypipecompanionstatus_s=QQBBB[4{exdisplaypipetightbeamcommon_exdisplaypipeindicatorstatus_s={exdisplaypipetightbeamcommon_exdisplaypipeindicator__opt_s=BI}SSSSfBB}]{exdisplaypipetightbeamco`
- `EXDisplayPipe::%s setup_exclave_async_notification failed\n`
- `EXDisplayPipe::%s failed!!! \n`
- `globalhealth_cp`
- `tconhpd_failure_ratio`
- `[EXDisplayPipe]: %s: disp_index %d \n`
- `submitChillPillMetrics`
- `EXDisplayPipe::%s get_display_index failed\n`
- `EXDisplayPipe::%s complete for ID %d \n`
- `EXDisplayPipe::%s: Couldn't map device memory.\n`
- `%s.%s.stream0`
- `EXDisplayPipe::%s addEventSource failed for IOInterruptEventSource at index %d \n`
- `EXDisplayPipeUserClient: init failed\n`
- `setup_debug_tightbeam`
- `link_cp`
- `dumpDroppedQueue`
- `EXDisplayPipe::setIndicators tightbeam call failed, has_value is false\n`
- `EXDisplayPipe::%s addEventSource failed with 0x%x\n`
- `[EXDisplayPipe]: setPowerInternal: power is already %s\n`
- `scadriver_failure_ratio`
- `EXDisplayPipe::%s tightbeam call failed with 0x%x\n`
- `EXDisplayPipe::%s failed to get IODeviceTree:/options\n`
- `display-post`
- `EXDisplayPipe::setLogMask tightbeam call failed with 0x%x\n`
- `submitFailureTimes`
- `scadriver_cp`
- `globalhealth_failure_ratio`
- `EXDisplayPipe::%s telemetry IOTimerEventSource creation failed \n`
- `EXDisplayPipe::%s addEventSource failed for telemetry IOTimerEventSource \n`
- `EXDisplayPipe::%s: OSNumber allocation failed\n`
- `nonauthenticpanel_failure_time`
- `silhealth_cp`
- `silHealth_failure_ratio`
- `EXDisplayPipe::%s failed to allocate IOInterruptEventSource\n`
- `EXDisplayPipe: error: getScaSessionHealth(...) failed\n`
- `hwlinkfailures_failure_time`
- `dcptransporthealth_cp`
- `sca_failures_beyond_thresh`
- `EXDisplayPipe::%s Exclave IOWorkLoop creation failed\n`
- `FailureTimes`
- `periodic_health_check_counter`
- `[EXDisplayPipe]: %s: edk_service_prop is NULL \n`
- `IONVRAM-FORCESYNCNOW-PROPERTY`
- `EXDisplayPipe::%s Unexpected message size!\n`
- `scaalgorithm_failure_counter`
- `scadriver_failure_time`
- `%s: Dropped queue: at %d swapID %llu \n`
- `v552@?0{exdisplaypipetightbeamcommon_exdisplaypipesecuretestatus__opt_s=B{exdisplaypipetightbeamcommon_exdisplaypipesecuretestatus_s={exdisplaypipetightbeamcommon_exdisplaypipehealthrecord_s=BQ}QQQQBi[10{exdisplaypipetightbeamcommon_exdisplaypipesecureteinfo_s=QQQQQQ}]}}8`
- `non_authentic_panel`
- `EXDisplayPipe::%s exclaveAsyncNotificationRegister failed with 0x%x\n`
- `[EXDisplayPipe] %s: stuck setting power to %u\n`
- `tconhpd_failure_counter`
- `dcptransporthealth_failure_counter`
- `EXDisplayPipe::%s watchdog IOTimerEventSource creation failed \n`
- `EXDisplayPipeUserClient`
- `start`
- `EXDisplayPipe::%s setup_sca_done_async_notification failed\n`
- `parse_edt_properties`
- `EXDisplayPipe: error: args->scalarInputCount (0x%x) != 1\n`
- `EXDisplayPipe: error: getStatus(...) failed\n`
- `EXDisplayPipe::%s exdisplaypipecompanioninterface__init failed with 0x%x\n`
- `v384@?0{exdisplaypipetightbeamcommon_exdisplaypipetelemetrycounters_s=QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ}8`
- `EXDisplayPipe: error: structureOutputSize mismatch for GetFrameInfo\n`
- `setActive`
- `EXDisplayPipe.cpp`
- `EXDisplayPipe::%s getNVRAMWriteInfo failed\n`
- `EXDisplayPipe::getSecureTEStatus unable to get status\n`
- `EXDisplayPipe::%s registerPrioritySleepWakeInterest failed\n`
- `dcptransporthealth_failure_ratio`
- `EXDisplayPipe::%s Received shutdown notification (messageType=0x%x)\n`
- `EXBrightMessageFunction`
- `SUCCESS!!`
- `EXDisplayPipe::hideIndicator tightbeam call failed, has_value is false\n`
- `EXDisplayPipe: error: submitTelemetry(...) failed\n`
- `EXDisplayPipeCompanionInterface_C.c`
- `\"[EXDisplayPipe] %s: failed to set power to %u in time\\n\" @%s:%d`
- `EXDisplayPipe::%s watchdog IOWorkLoop creation failed\n`
- `on`
- `setup_exclave_async_notification`
- `EXDisplayPipeDebug.cpp`
- `tconhealth_failure_counter`
- `tconcrc_failure_ratio`
- `v20@?0^{IOInterruptEventSource=^^?i^{IOEventSource}^{OSObject}^?B^{IOWorkLoop}^v^{ExpansionData}^{IOService}iIIBB^{ExpansionData}}8i16`
- `EXDisplayPipe::%s failed to allocate OSString\n`
- `EXDisplayPipe: error: getStats(...) failed\n`
- `EXDisplayPipe::%s NVRAM display-post set successfully\n`
- `dumpCancelledQueue`
- `EXDisplayPipe::showIndicator tightbeam call failed with 0x%x\n`
- `EXDisplayPipe::getStatus unable to get status\n`
- `EXDisplayPipe::%s setup_tightbeam failed\n`
- `submitFailureRatios`
- `EXDisplayPipe::%s IOTimerEventSource creation failed \n`
- `EXDisplayPipe::%s setup_sca_start_async_notification failed\n`
- `tconhpd_failure_time`
- `scaalgorithm_failure_ratio`
- `setup_sca_start_async_notification`
- `power_change_handler`
- `wait_for_action_complete`
- `display_id`
- `scldriver_failure_counter`
- `EXDisplayPipe: error: args->structureInputSize (0x%x) != sizeof(EXDisplayPipeStatus) (0x%lx)\n`
- `site.EXDisplayPipe`
- `FailureCounters`
- `tconcrc_failure_counter`
- `EXDisplayPipe::%s: CoreAnalyticsSendEvent failed (0x%x)\n`
- `exclave-edk-service`
- `brightness_failure_counter`
- `EXDisplayPipe::%s interruptEventSource creation failed at interrupt index %d \n`
- `EXDisplayPipeUserClient: start failed\n`
- `Unexpected selector\n`
- `EXDisplayPipe::setPowerInternal failed to set power\n`
- `hw_link_failure_counters`
- `scaalgorithm_failure_time`
- `tconhealth_failure_ratio`
- `[EXDisplayPipe]: %s: exclave_service %s \n`
- `setup_interrupts`
- `<unknown>`
- `Created EXDisplayPipeUserClient successfully\n`
- `set_nvram_property`
- `\"[EXDisplayPipe] %s: failed to complete for swapID 0x%llx\\n\" @%s:%d`
- `INDICATOR_CAM`
- `get_nvram_service`
- `EXDisplayPipe: error: hideIndicator(%u) failed\n`
- `exdisplaypipe_rack_debug`
- `EXDisplayPipe`
- `com.apple.driver.EXDisplayPipe`
- `scldriver_failure_ratio`
- `EXDisplayPipe::%s addEventSource failed for watchdog IOTimerEventSource \n`
- `EXDisplayPipeUserClient: netconnect is null\n`
- `%s: Cancelled queue: at %d swapID %llu \n`
- `off`
- `EXDisplayPipe::%s submitTelemetry failed\n`
- `dcptransporthealth_failure_time`
- `EXDisplayPipe::%s exdisplaypipecompaniondebuginterface__init failed with 0x%x\n`
- `tconhealth_cp`
- `tconhpd_cp`
- `setup_tightbeam`
- `EXDisplayPipe::%s: m_rack_debug_enable is true\n`
- `EXDisplayPipe::%s parse_edt_properties failed\n`
- `EXDisplayPipe: error: setLogLevel(...) failed\n`
- `EXDisplayPipe::showIndicator tightbeam call failed, has_value is false\n`
- `telemetry_timer_wrapper`
- `EXDisplayPipe::%s: m_frame_num_stale_panic is true\n`
- `average_crc_variance`
- `EXDisplayPipe::setLogLevel tightbeam call failed with 0x%x\n`
- `brightness_failure_time`
- `exdisplaypipe`
- `exdisp_frame_num_stale_panic`
- `link_failure_time`
- `scaalgorithm_cp`
- `brightness_cp`
- `EXDisplayPipe::%s tb_endpoint_create_with_value for m_tb_endpoint failed\n`
- `true`
- `1211111212221212111111111111`
- `EXDisplayPipe::getStatus tightbeam call failed with 0x%x\n`
- `EXDisplayPipe watchdog timed out\n`
- `EXDisplayPipe::%s setup_interrupts failed\n`
- `stop`
- `silhealth_failure_time`
- `EXDisplayPipe::%s m_sca_workloop is NULL\n`
- `EXDisplayPipe: error: args->structureInputSize (0x%x) != sizeof(EXDisplayPipeIndicatorParams) (0x%lx)\n`
- `INDICATOR_MIC_ALT_ACCESSIBILITY`
- `FailureRatios`
- `tconhealth_failure_time`
- `EXDisplayPipe::%s IOCommandGate creation failed\n`
- `IODeviceTree:/options`
- `EXDisplayPipe::setPowerInternal tightbeam call failed with 0x%x\n`
- `EXDisplayPipe: error: setALSSEnable(...) failed\n`
- `[EXDisplayPipe] %s: failed to complete for swapID 0x%llx\n`
- `globalhealth_failure_counter`
- `link_failure_ratio`
- `EXDisplayPipe: error: getSecureTEStatus(...) failed\n`
- `hw_link_failure_ratio`
- `Creating EXDisplayPipeUserClient..\n`
- `EXDisplayPipe::%s set_nvram_display_post failed\n`
- `scadriver_failure_counter`
- `EXDisplayPipe::%s TB failed to get nvram write info\n`
- `EXDisplayPipe: error: args->structureOutputSize (0x%x) != sizeof(uint32_t) (0x%lx)\n`
- `nonauthenticpanel_cp`
- `map_device_memory`
- `EXDisplayPipe: error: args->structureOutputSize (0x%x) != sizeof(EXDisplayPipeSecureTEStatus) (0x%lx)\n`
- `exclave-service`
- `EXDisplayPipe: Show Indicator %s (%u, %u) alpha:0x%x\n`
- `EXDisplayPipe: Hide Indicator returns %s \n`
- `exdisp_frame_num_stale`
- `pipe_failure_counter`
- `EXDisplayPipe::%s m_exclave_workloop is NULL\n`
- `EXDisplayPipeUserClient: attach failed\n`
- `v9@?0{exdisplaypipetightbeamcommon_exdisplaypipenvramwriteinfo_s=B}8`
- `EXDisplayPipe: error: setLogMask(...) failed\n`
- `operator()`
- `EXDisplayPipe::%s setup_workloop failed\n`
- `EXDisplayPipe::%s setup_timer failed\n`
- `tconcrc_failure_time`
- `\"TB_FATAL: \" \"invalid value: unexpected case value, %llx\" @%s:%d`
- `v12@?0B8`
- `INDICATOR_MIC`
- `EXDisplayPipe::hideIndicator tightbeam call failed with 0x%x\n`
- `submitFailureCounters`
- `12111112122212121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111221111111111111111112111112`
- `EXDisplayPipe::%s SCA Session health is %x\n`
- `site.EXDisplayPipeUserClient`
- `EXDisplayPipe: error: setIndicators(...) failed\n`
- `v24@?0{u64__opt_s=BQ}8`
- `EXDisplayPipe::setIndicators tightbeam call failed with 0x%x\n`
- `link_failure_counter`
- `pipe_cp`
- `tconcrc_cp`
- `EXDisplayPipe::%s addEventSource failed for IOCommandGate \n`
- `setup_sca_done_async_notification`
- `callPlatformFunction`
- `wait_for_power`
- `pipe_failure_time`
- `EXDisplayPipe::%s setup_debug_tightbeam failed\n`
- `scldriver_cp`
- `setup_workloops`
- `[EXDisplayPipe]: %s: disp_index_prop is NULL \n`
- `EXDisplayPipe::%s addEventSource failed for IOTimerEventSource \n`
- `EXDisplayPipe::%s failed to set nvram property %s\n`
- `EXDisplayPipe::%s TB failed to get sca session health\n`
- `EXDisplayPipe: error: args->structureOutputSize (0x%x) != sizeof(EXDisplayPipeStatus) (0x%lx)\n`
- `EXDisplayPipe::%s tb_endpoint_create_with_value for m_tb_debug_endpoint failed\n`
