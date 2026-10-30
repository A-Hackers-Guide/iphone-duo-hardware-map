# `com.apple.driver.AppleT8160CLPC`

- Name: AppleT8160CLPC
- Version: `1`
- UUID: `BA0A87B9-C255-3BAD-9107-183BF2C28645`
- Source version: `1794.40.23.0.1`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.ApplePMGR`](com.apple.driver.ApplePMGR.md) 1.0, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0, [`com.apple.iokit.IOSurface`](com.apple.iokit.IOSurface.md) 52.6.0, [`com.apple.kec.Libm`](com.apple.kec.Libm.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) | `AppleCLPC` | `clpc,t8160` |

## IOKit personalities (1) [KC]

### AppleT8160CLPC
- `CFBundleIdentifier`: `com.apple.driver.AppleT8160CLPC`
- `IOClass`: `AppleCLPC`
- `IOMatchCategory`: `IODefaultMatchCategory`
- `IONameMatch`: `clpc,t8160`
- `IOPersonalityPublisher`: `com.apple.driver.AppleT8160CLPC`
- `IOPlatformHaltRestartAction`: `500`
- `IOPlatformSleepAction`: `500`
- `IOPlatformWakeAction`: `500`
- `IOPropertyMatch`:
  - `clpc-match-version`: `3`
- `IOProviderClass`: `ApplePMGRNub`
- `IOUserClientClass`: `AppleCLPCUserClient`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleCLPC` | 0xb0 | IOService → IORegistryEntry |
| `AppleCLPCUserClient` | 0xe8 | IOUserClient → IOService → IORegistryEntry |
| `AppleCLPCWorkLoop` | 0x50 | IOWorkLoop |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00005410 off=0x007bb870-0x007c0c80 addr=0xfffffe00077bf870-0xfffffe00077c4c80 r--/r--   __TEXT            
	sz=0x00003c3b off=0x007bbf88-0x007bfbc3 addr=0xfffffe00077bff88-0xfffffe00077c3bc3               __TEXT.__cstring          (CstringLiterals)
	sz=0x000010b0 off=0x007bfbd0-0x007c0c80 addr=0xfffffe00077c3bd0-0xfffffe00077c4c80               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00069e54 off=0x02806a70-0x028708c4 addr=0xfffffe000980aa70-0xfffffe00098748c4 r-x/r-x   __TEXT_EXEC       
	sz=0x000694c4 off=0x02806a70-0x0286ff34 addr=0xfffffe000980aa70-0xfffffe0009873f34          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000990 off=0x0286ff34-0x028708c4 addr=0xfffffe0009873f34-0xfffffe00098748c4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00010000 off=0x049a2f00-0x049b2f00 addr=0xfffffe000b9a6f00-0xfffffe000b9c5680 rw-/rw-   __DATA            
	sz=0x0000f720 off=0x049a2f00-0x049b2620 addr=0xfffffe000b9a6f00-0xfffffe000b9b6620               __DATA.__data             
	sz=0x0000ed61 off=0x00000000-0x0000ed61 addr=0xfffffe000b9b6680-0xfffffe000b9c53e1               __DATA.__common           (Zerofill)
	sz=0x00000298 off=0x00000000-0x00000298 addr=0xfffffe000b9c53e8-0xfffffe000b9c5680               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00007cd8 off=0x01254368-0x0125c040 addr=0xfffffe0008258368-0xfffffe0008260040 rw-/rw-   __DATA_CONST      
	sz=0x00000128 off=0x01254368-0x01254490 addr=0xfffffe0008258368-0xfffffe0008258490         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x01254490-0x012544a8 addr=0xfffffe0008258490-0xfffffe00082584a8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00006ef8 off=0x012544a8-0x0125b3a0 addr=0xfffffe00082584a8-0xfffffe000825f3a0         __DATA_CONST.__const            
	sz=0x00000380 off=0x0125b3a0-0x0125b720 addr=0xfffffe000825f3a0-0xfffffe000825f720         __DATA_CONST.__kalloc_type      
	sz=0x00000370 off=0x0125b720-0x0125ba90 addr=0xfffffe000825f720-0xfffffe000825fa90         __DATA_CONST.__kalloc_var       
	sz=0x000004c8 off=0x0125ba90-0x0125bf58 addr=0xfffffe000825fa90-0xfffffe000825ff58         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000e0 off=0x0125bf58-0x0125c038 addr=0xfffffe000825ff58-0xfffffe0008260038         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x0125c038-0x0125c040 addr=0xfffffe0008260038-0xfffffe0008260040         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 334 at 0x04ae82f4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     BA0A87B9-C255-3BAD-9107-183BF2C28645
008: LC_SOURCE_VERSION           1794.40.23.0.1
009: LC_FUNCTION_STARTS          offset=0x004ab3ec8 size=0x7e8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleT8160CLPC`
- `CFBundleGetInfoString`: `Copyright © 2025 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleT8160CLPC`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleT8160CLPC`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2025 Apple. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleT8160CLPC.kext`
- `_PrelinkExecutableLoadAddr`: `-2198897690512`
- `_PrelinkExecutableRelativePath`: `AppleT8160CLPC`
- `_PrelinkExecutableSize`: `612028`
- `_PrelinkExecutableSourceAddr`: `-2198897690512`
- `_PrelinkKmodInfo`: `-2198828585216`

## Strings (548) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `Filtered`
- `Instantaneous`
- `false`
- `PCORE`
- `PowerZones`
- `state != nullptr`
- `clpc-disable-pmc`
- `package_target_100ms`
- `channel_info.get() != nullptr`
- `MapEntries`
- `map_registers(config.acc_mem_start, config.acc_mem_length, acc_map, acc_virtual_address)`
- `AFR`
- `performance_change_interrupt.get() && work_loop->addEventSource(performance_change_interrupt.get()) == kIOReturnSuccess`
- `function-ptd_read_mult`
- `DRAMTemp1s`
- `OnlineClusterMask`
- `config.soc_sensor_layout.count < 2 && config.ane_sensor_layout.count < 2`
- `PMGRDomain`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/memory_dvf_manager.cpp`
- `cpu_topology.init()`
- `InternalRep`
- `thread_group_data->thread_group_size >= sizeof(ThreadGroupContainer)`
- `CoreToClusterMap`
- `PerfStateValues`
- `setAGXGameModeKey`
- `init_dvfm_tables()`
- `MaxPerfScore`
- `clpc::lock_group_attributes->get()`
- `cpu_uncore_perf_sampler.init(uncorePerfSamplerConfig())`
- `package_power_limiter.init()`
- `AbsoluteTarget`
- `getDPE`
- `Result`
- `clpc`
- `CPU DVFM`
- `threadGroupPowerLimit`
- `Average`
- `cpu_workload_power_map.init(cpu_perf_map, cpu_core_power_maps)`
- `SetMaxGPUAbsolutePower`
- `Low Power Mode is now %s (budget: %.1fW)\n`
- `entry_dict.get() != nullptr`
- `DCS`
- `Effort`
- `AssignedClusters`
- `Sustained Execution Mode is now enabled as developer opt-in mode\n`
- `steal_allowed`
- `channels_array != nullptr`
- `PerfLevels`
- `ACC`
- `ERROR: setUSToTicksProperty does not fit in uint32_t`
- `K`
- `BinnedVoltage`
- `IOReportGroupName`
- `result == kCLPCReturnSuccess`
- `Inputs`
- `AppleCLPCWorkLoop`
- `getPowerMap`
- `channel_type_key.get() != nullptr`
- `clpc-assume-new-budgets`
- `NumCores`
- `IOAcceleratorES`
- `ANESHARED`
- `sgx`
- `ANE0`
- `getProperties`
- `Latest`
- `SwitchCap`
- `FabricComputePowerRatio`
- `ppm_sleep_wake_interrupt.get() && work_loop->addEventSource(ppm_sleep_wake_interrupt.get()) == kIOReturnSuccess`
- `%d.%d.%d`
- `PerfRanges`
- `IOPlatformQuiesceAction`
- `getCLPCStandbyCountKey`
- `cpuworkload`
- `ANEFrequencies`
- `MembersByCluster`
- `first_bytes == 0`
- `RecommendedCoreMasks`
- `Leakage`
- `fabric_power_limiter.init()`
- `HiP Mode is now %s\n`
- `BuildVariant`
- `value`
- `GPUCSSRAM`
- `mem_stall_core_maps[0].counter_base_address == 0`
- `clpc-enable-tg-block`
- `GPUAccumulatedEnergy`
- `4e5b2a0c448a6f860f66`
- `cpu_power_limiter.init()`
- `ApplePPM`
- `Invalid`
- `ranges`
- `AppleCLPCUserClient`
- `ane_forced_idle_limiter.init()`
- `GPUSRAM`
- `SetCLPCDeadlineControlEffort`
- `base_address != 0`
- `DRAMTempInstantaneous`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/fabric_dvfm_table.cpp`
- `cpus`
- `CurrentValue`
- `ANE Shared Cluster`
- `getPerfMap`
- `CLPC Stats`
- `pz`
- `Limits`
- `SharedCPU`
- `override_state < num_states`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/ane_perf_sampler_impl.hpp`
- `DRAMTemp100ms`
- `energy_sampler.init()`
- `type`
- `Output`
- `clpc-cpu-min-perf-config`
- `Normal`
- `Critical`
- `fANE0`
- `site.AppleCLPC`
- `work_loop`
- `memory_dvf_manager.enable(enabled)`
- `%s:%d Assertion failed: %s : failed to enable uncore perf counter sampler`
- `getPowerInfo`
- `SOCREST`
- `Members`
- `DVFMStates`
- `clpc-disable-perf-map-warp`
- `Initialized`
- `package_target_1s`
- `Engaged`
- `Advanced`
- `DefaultValue`
- `acc_map.get() == nullptr && ext_map.get() == nullptr`
- `CPU Preference`
- `ECPM`
- `GPU`
- `StateID`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_cluster_perf_sampler.cpp`
- `MaxFrequency`
- `ControlFabric`
- `MinPerfScore`
- `ReferencePower`
- `ptd-ranges`
- `_clpc->cpu_uncore_perf_sampler.enable( available, _clpc->cpu_uncore_saved_counters)`
- `channel_entry.get() != nullptr`
- `AppleCLPCv3 start\n`
- `initProperties()`
- `GPULimitReason`
- `sched_interface.enable(enabled)`
- `migration_allowed`
- `first_cluster != -1`
- `PerfScoreOffset`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/clpc.cpp`
- `IDS`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/perf_map_impl.hpp`
- `ANE`
- `cpu_uncore_perf_sampler.enable( true, cpu_uncore_saved_counters)`
- `ControlCPU`
- `ControlGroupPreferences`
- `PACC0`
- `setProperties`
- `AverageUPOAvoidance`
- `Splitter`
- `clpc_efficient_groups`
- `com.apple.private.clpc.seeding`
- `migration_weight`
- `ret == kCLPCReturnSuccess && client != nullptr`
- `VDEC`
- `Tasking Mode is now %s\n`
- `fane0_number != nullptr && fane1_number != nullptr && fane2_number != nullptr`
- `CLPC: Unsupported work_interval type = %d`
- `ClusterTypeToClusterMask`
- `power_notifier`
- `setEdgeMatrix`
- `init_constraint_interface()`
- `cpucore`
- `fane0_index_number != nullptr && fane1_index_number != nullptr && fane2_index_number != nullptr`
- `cpushared`
- `getDashboard`
- `ERROR: setSimpleProperty does not fit in uint32_t`
- `SOC`
- `wloop`
- `pmc_voter_interface.init(pmcCLPCPerfStateFloorRegister())`
- `ane_id <= 9`
- `clpc-disable-cpu-turbo`
- `GPUCS`
- `CLPC: index %lu out of bounds for array of size %lu at %p`
- `hard_timer_interrupt.get() && work_loop->addEventSource(hard_timer_interrupt.get()) == kIOReturnSuccess`
- `Type`
- `group_id`
- `33656c499ea26d0c30c4`
- `cpu-critical-create-enable`
- `Input`
- `pmgr_soc_perf_sampler.initForDirectSampling(socPerfMemoryRegions(), socPerfSamplerConfig())`
- `memory_power_limiter.init()`
- `cpu_preference_manager.enable(enabled)`
- `method`
- `CPUSHARED`
- `Energy Model`
- `PeakUPOAvoidance`
- `params`
- `disabled`
- `1368bb2e03a4731a4bc6`
- `CLPC: bad chain type %u`
- `Low`
- `timestamp`
- `flags`
- `Attributes`
- `IncomingMembers`
- `listThreadGroups`
- `ERROR: setMSToTicksProperty does not fit in uint32_t`
- `MaxTemperature`
- `event_interrupt.get() && work_loop->addEventSource(event_interrupt.get()) == kIOReturnSuccess`
- `perf_sampler.template sync<S>(cluster.saved_throttle_counters)`
- `CPU core perf counter`
- `MEMORY_QOS`
- `cpm_virtual_address`
- `DieMask`
- `root`
- `CPU uncore perf counter`
- `18dcf18db157d3b75a44`
- `floor_reg_addr`
- `%s:%d Assertion failed: %s : CLPC: init called multiple times for group %llu`
- `num_elements > kAGXNumOperatingStatesIdx`
- `aneshared`
- `scaler`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/ptd_interface_impl.hpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/apple_clpc.cpp`
- `com.apple.private.clpc.reporting`
- `Alpha`
- `handle-non-monotonic-power`
- `MaxVoltage`
- `Version`
- `cpu-power-map-ignore-ane`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_topology.cpp`
- `syspriv::init(*clpc::_clpc, *provider, *this, work_loop) && syspriv::enable(*clpc::_clpc, true)`
- `cpu_core_memstall_sampler.init(coreMemStallSamplerConfig(), requiresRemoteIPIMemStallSampling())`
- `getThreadGroup`
- `aon-ptd-int-imm`
- `registerKernelClientToApplePPMFunction`
- `LowPeak`
- `set_thread_policy(INT32_MAX) == kIOReturnSuccess`
- `db3b00b72a324575a29a`
- `PerfScores`
- `Shared ANE`
- `1211111212221212111111`
- `legacy_report_names && legacy_report_actions && num_legacy_reports > 0`
- `afc`
- `HiP`
- `voltage`
- `clpc-pmgr-energy-node-validate`
- `ANE job tracking`
- `legend_entry != nullptr`
- `initProperties(urgent_property_names, urgent_property_setters, num_urgent_properties)`
- `#cpu-utility-limiter-perf-ceil`
- `ISP`
- `Beta`
- `ID`
- `MinState`
- `num_operating_states <= kMaxRows`
- `n/a`
- `CoreMask`
- `DCS DVFM`
- `PerfScoreGain`
- `MemoryComputePowerRatio`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_temperature_sampler.cpp`
- `kpc_power_counter_mask == 0 && aon_core_maps[0].counter_base_address == 0`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_sched_interface.cpp`
- `ptd_interface.init(ptdLayoutConfig())`
- `Assistant Mode : LPM budget updated to %s LPM target.\n`
- `ane_id_data->getLength() == sizeof(uint32_t)`
- `getCurrentStateKTrace`
- `AMCC`
- `virtual_address`
- `IOReportLegend`
- `ContextualPowerMode`
- `clpc-direct-access-energy-node-enable`
- `entries`
- `%s:%d Assertion failed: %s : bad limiter info?`
- `BuildTag`
- `CoreTypeMap`
- `descriptor.get() != nullptr`
- `ppz`
- `container != nullptr`
- `number != nullptr`
- `AFC`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_cluster_perf_sampler_impl.hpp`
- `aon_cluster_maps[0].counter_base_address == 0`
- `WeightMap`
- `CLPC: Unsupported work_interval sub_type = %d`
- `map.get()`
- `site.AppleCLPCWorkLoop`
- `EACC0`
- `getPerfDomainInfo`
- `PeakHeatPipe`
- `clpc-assert-energy`
- `work_loop_thread_id`
- `AFI`
- `performance_change_thread_call`
- `#implct-wi-enabled`
- `cpu_timer.init(hard_timer_interrupt_handler, soft_timer_interrupt_handler, work_loop, clpc_service)`
- `DebugBuild`
- `BandWidth`
- `AppleCLPC`
- `site.AppleCLPCUserClient`
- `getCLPCPowerSamplePeriodKey`
- `ane`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/clpc.hpp`
- `ControlEfforts`
- `ECPU`
- `CPU`
- `1211111212`
- `Ratio`
- `AveragePower`
- `Simple`
- `voltage and frequency`
- `cpu_cluster_perf_sampler.enable( true)`
- `site.T`
- `memory_dvf_manager.init(keepAliveRegisters(), dcsQOSThrottleRegister())`
- `ane_job_tracking.init()`
- `names`
- `-restore`
- `AverageSustainableMode`
- `ControlCPUDynamicCoreRotation`
- `name`
- `com.apple.private.pmgr.nrg.reporting`
- `DISPEXT`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/ane_topology.cpp`
- `hist_dict.get() != nullptr`
- `Frequency`
- `provider != nullptr && IOService::start(pmgr_nub)`
- `%s:%d Assertion failed: %s : failed to disable %s`
- `message`
- `AppleCLPC start failed\n`
- `Efficient`
- `VirusPower`
- `container != nullptr && is_aligned<16>(container)`
- `energy_sampler.enable( true)`
- `memory`
- `getStatus`
- `E`
- `V0`
- `com.apple.private.clpc.policy`
- `ok`
- `normal`
- `IOReportChannels`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/dashboard_manager_impl.hpp`
- `'cpu-peak-power-max-w2r`
- `setAETSMaxControlEffortFunction`
- `FAB`
- `PCPM`
- `%s:%d Assertion failed: %s : Could not find ptd entry with 4cc 0x%x in PTD %u`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/ane_job_tracking_impl.hpp`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_timer.cpp`
- `Voltage`
- `interrupts`
- `%s:%d Assertion failed: %s : failed to enable %s sampler`
- `result == kIOReturnSuccess`
- `%s:%d Assertion failed: %s : failed to enable ANE perf sampler`
- `AllowP`
- `frequency`
- `Virus`
- `map_registers(config.ext_mem_start, config.ext_mem_length, ext_map, ext_virtual_address)`
- `ane-id`
- `getTopology`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_core_perf_sampler_impl.hpp`
- `SOCAON`
- `domain_id == kAGXClockDomainMGPU`
- `fabric`
- `enable`
- `Limiters`
- `ClusterMask`
- `Assistant Mode is now %s\n`
- `%s:%d Assertion failed: %s : non-monotonic %s in dvfm table provided by PMGR for %s cluster %u, between state %u (%umV, %uMHZ) and %u (%umV, %uMHz). If expected, disable panic with boot-arg \"%s=1\"`
- `MaxWeight`
- `DieID`
- `MEMORY`
- `ane_topology.hasCluster(ane_id)`
- `Islands`
- `soft_timer_interrupt.get() && work_loop->addEventSource(soft_timer_interrupt.get()) == kIOReturnSuccess`
- `writeDashboardEntry`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/pmc_voter_interface.cpp`
- `Target`
- `DISPALL`
- `CoreRatio`
- `OperatingState`
- `NumClusters`
- `clpc::lock_attributes->get()`
- `client`
- `<invalid>`
- `keep_alive_reg_maps[i].reg_virtual_address`
- `direct_access_energy_sampler.enable( true)`
- `memory_qos`
- `getVersionInfo`
- `clampThreadGroup`
- `IOReportChannelConfig`
- `mem-data-rates-size`
- `BuildDate`
- `CLPC: Unable to poll '%s'; PTD entry is not provisioned.\n`
- `MaxState`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_core_memstall_sampler.cpp`
- `ane_job_tracking.enable(now)`
- `report_names && report_actions && num_reports > 0`
- `Sustained Execution Mode is now disabled\n`
- `ECORE`
- `getCLPCPerfCtrlTargetKey`
- `cpu_core_perf_sampler.enable( true)`
- `Sustained Execution Mode is now enabled as auto mode\n`
- `aon_cluster_maps[0].counter_base_address != 0`
- `setBudgetToAGXFunction`
- `init_power_maps()`
- `GPUCLPCSharedData`
- `Enabled`
- `getDVFMTable`
- `ids`
- `getCurrentState`
- `num_clusters <= Config::maxNumClusters()`
- `cluster`
- `Name`
- `clpc_normal_groups`
- `setCLPCDeadlineControlEffortKey`
- `getCPUCoreMask`
- `setCPUCoreMask`
- `I_ds`
- `ane_topology.init(cpu_topology)`
- `ControlMemory`
- `AppleKeyStore`
- `Power`
- `setBudgetToKernelClientFunction`
- `reg_map.get()`
- `getCLPCDynamicSplitRatioDictKey`
- `pmp`
- `PreSplitFloor`
- `Vdd0`
- `ClusterTypeToFirstCluster`
- `clpc-debug`
- `_clpc->cpu_core_perf_sampler.enableKPCCounters( available)`
- `AppleCLPC-1794.40.23.0.1`
- `gpu`
- `FABRIC`
- `LowPowerMode`
- `P`
- `CLPC: Called function on invalid thread group.`
- `ane-disabled`
- `cff5ee83b50849222d9b`
- `NumBands`
- `getCLPCStandbyDurationKey`
- `Fabric DVFM`
- `map_perf_scores[perf_level][base_index] >= bottom_first`
- `CLPC: Unable to register interrupts for PTD entry '%s'; PTD entry is not provisioned.\n`
- `CPU Sched Interface`
- `IOBlockStorageDriver`
- `CLPC-TO-SMC`
- `com.apple.private.clpc.analysis`
- `fabric_dvf_manager.enable(enabled)`
- `cpu`
- `CPUWORKLOAD`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/direct_access_energy_sampler_impl.hpp`
- `2026-10-13T23:28:49-07:00`
- `CLPC: Power of %llu mW over %llu ms nodemask 0x%llx`
- `fANE1`
- `fANE2`
- `IOReportSubGroupName`
- `BandOffset`
- `SharedANEClusterMask`
- `domain`
- `ret == kCLPCReturnSuccess`
- `Beta0`
- `descriptor.get()`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/gpu_dvfm_table.cpp`
- `setAETSANEMaxControlEffortFunction`
- `assistant`
- `DieToClusterMask`
- `validation_disables`
- `initReporting()`
- `init_preference_manager()`
- `dashboard_manager.init()`
- `direct access package energy`
- `getEdgeMatrix`
- `Clusters`
- `urgent_property_names && urgent_property_setters && property_names && property_setters && num_properties > 0`
- `LowPeakPower`
- `AVE`
- `afi`
- `IOUserBlockStorageDevice`
- `aon-ptd-poll`
- `dvfm_states != nullptr`
- `PeakCLVR`
- `Outputs`
- `PCPU`
- `MSR`
- `AverageThermal`
- `a981c13a92c1a50cc5db`
- `fabric_dvf_manager.init()`
- `PropertyID`
- `id`
- `CPUCORE`
- `Reference`
- `IOHibernateState`
- `map.get() != nullptr`
- `ExternalTargets`
- `Rows`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/power_map.cpp`
- `num_elements > kAGXNumOperatingStatesIdx + num_operating_states * (1 + 3 * valid_voltages_per_perf_state)`
- `wdt`
- `scratch_dict && scratch_number && scratch_number2`
- `GetGPUMaxPower`
- `report_legend_entries.get() != nullptr`
- `gpu_max_power_number != nullptr`
- `ANE1`
- `channel_type_number.get() != nullptr && channel_id_number.get() != nullptr`
- `MaxPower`
- `IOReportChannelInfo`
- `direct_access_energy_sampler.init(accDPEOffsets(), directAccessMemoryRegions())`
- `FAST-DIE-CE`
- `CPMRatio`
- `IOReportLegendPublic`
- `enabled`
- `preferThreadGroups`
- `LTS-VOLT-CAP`
- `PMU-TO-CLPC`
- `OperatingStates`
- `sched_interface.init()`
- `MaxDVMRWeight`
- `12111112122212121111111111112`
- `IOAccelerator`
- `DISP`
- `CLPC: Bad thread group type %u`
- `ApplePTD`
- `High`
- `CLPC: AON PTD EmbeddedHeader and PlatformConfig mismatch?`
- `initProperties(property_names, property_setters, num_properties)`
- `BandTable`
- `ids_number != nullptr`
- `%s:%d Assertion failed: %s : failed to enable core perf counter sampler`
- `getPerfBandTable`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_uncore_perf_sampler.cpp`
- `cpu_dvf_manager.init(pmgr_nub)`
- `package energy`
- `CPU cluster perf counter`
- `%s:%d Assertion failed: %s : failed to enable %s`
- `name.createSymbol()`
- `/Library/Caches/com.apple.xbs/43CF14CD-1F68-4D44-BB56-14124418B18D/TemporaryDirectory.6CwZ1F/Sources/AppleCLPC/CLPC/source/cpu_dvfm_table_impl.hpp`
- `ptd-data-table`
- `IOReportChannelUnit`
- `DRAM`
- `ACCSRAM`
- `cpu_dvf_manager.enable(enabled)`
- `AON PTD CLVR`
