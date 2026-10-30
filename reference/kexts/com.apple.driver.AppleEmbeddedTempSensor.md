# `com.apple.driver.AppleEmbeddedTempSensor`

- Name: AppleEmbeddedTempSensor
- Version: `1.0.0`
- UUID: `CC7BE7ED-AD07-3D6A-9173-9068F7302E4C`
- Source version: `189.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.4, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (9) [KC]

### AMCTempSensor
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedTempSensor`
- `IOClass`: `AMCTempSensor`
- `IONameMatch`: `amctempsensor,s5l8960x`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedTempSensor`
- `IOProbeScore`: `100`
- `IOProviderClass`: `AppleARMIODevice`
- `IOResourceMatch`: `IOKit`
- `QueueSize`: `0`

### AppleDieTempController
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedTempSensor`
- `IOClass`: `AppleDieTempController`
- `IONameMatch`:
  - `dietempctl,s5l8960x`
  - `dietempctl,t7000`
  - `dietempctl,t7001`
  - `dietempctl,s8000`
  - `dietempctl,t8010`
  - `dietempctl,t8012`
  - `dietempctl,t8015`
  - `dietempctl,t8020`
  - `dietempctl,t8027`
  - `dietempctl,t8030`
  - `dietempctl,t8004`
  - `dietempctl,t8006`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedTempSensor`
- `IOProbeScore`: `100`
- `IOProviderClass`: `AppleARMIODevice`
- `IOResourceMatch`: `IOKit`
- `QueueSize`: `0`

### ApplePMGRTempSensor
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedTempSensor`
- `IOClass`: `ApplePMGRTempSensor`
- `IONameMatch`: `tempsensor,s5l8945x`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedTempSensor`
- `IOProbeScore`: `100`
- `IOProviderClass`: `AppleARMIODevice`
- `IOResourceMatch`: `IOKit`
- `IOUserClientClass`: `ApplePMGRTempUserClient`
- `QueueSize`: `0`

### AppleSCCTempSensor
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedTempSensor`
- `IOClass`: `AppleSCCTempSensor`
- `IONameMatch`: `scctempsensor,s5l8950x`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedTempSensor`
- `IOProbeScore`: `100`
- `IOProviderClass`: `AppleARMIODevice`
- `IOResourceMatch`: `IOKit`
- `QueueSize`: `0`

### AppleSocHot
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedTempSensor`
- `IOClass`: `AppleSocHot`
- `IONameMatch`: `sochot,s5l8955x`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedTempSensor`
- `IOPlatformActiveAction`: `950`
- `IOPlatformQuiesceAction`: `250`
- `IOProbeScore`: `100`
- `IOProviderClass`: `AppleARMIODevice`
- `IOResourceMatch`: `IOKit`
- `QueueSize`: `0`

### AppleT700XTempSensor
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedTempSensor`
- `IOClass`: `AppleT700XTempSensor`
- `IONameMatch`:
  - `tempsensor,t7000`
  - `tempsensor,t7001`
  - `tempsensor,s8000`
  - `tempsensor,t8010`
  - `tempsensor,t8012`
  - `tempsensor,t8006`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedTempSensor`
- `IOPlatformActiveAction`: `90010`
- `IOPlatformQuiesceAction`: `90010`
- `IOProbeScore`: `100`
- `IOProviderClass`: `AppleARMIODevice`
- `IOResourceMatch`: `IOKit`
- `IOUserClientClass`: `AppleT700XTempSensorUserClient`
- `QueueSize`: `0`

### AppleT8015TempSensor
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedTempSensor`
- `IOClass`: `AppleT8015TempSensor`
- `IONameMatch`:
  - `tempsensor,t8015`
  - `tempsensor,t8020`
  - `tempsensor,t8027`
  - `tempsensor,t8030`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedTempSensor`
- `IOPlatformActiveAction`: `950`
- `IOPlatformQuiesceAction`: `250`
- `IOProbeScore`: `100`
- `IOProviderClass`: `AppleARMIODevice`
- `IOResourceMatch`: `IOKit`
- `QueueSize`: `0`

### AppleT8020MTRTempSensor
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedTempSensor`
- `IOClass`: `AppleT8020MTRTempSensor`
- `IONameMatch`:
  - `mtrtempsensor,t8020`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedTempSensor`
- `IOPlatformActiveAction`: `950`
- `IOPlatformQuiesceAction`: `250`
- `IOProbeScore`: `100`
- `IOProviderClass`: `AppleARMIODevice`
- `IOResourceMatch`: `IOKit`
- `QueueSize`: `0`

### AppleVTempDispatcher
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedTempSensor`
- `IOClass`: `AppleVTempDispatcher`
- `IONameMatch`:
  - `vtempctl,t8010`
  - `vtempctl,s8003`
  - `vtempctl,s8001`
  - `vtempctl,s8000`
  - `vtempctl,t8015`
  - `vtempctl,t8020`
  - `vtempctl,t8027`
  - `vtempctl,t8030`
  - `vtempctl,t8006`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedTempSensor`
- `IOProbeScore`: `100`
- `IOProviderClass`: `AppleARMIODevice`
- `IOResourceMatch`: `IOKit`
- `QueueSize`: `0`


## C++ classes (19) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AMCTempSensor` | 0x138 | AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleARMPMUPowerSensor` | 0x100 | AppleARMPMUSensor → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleARMPMUSensor` | 0xf0 | AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleARMPMUTempSensor` | 0xf0 | AppleARMPMUSensor → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleDieTempController` | 0x2e8 | IOService → IORegistryEntry |
| `AppleDieTempControllerUserClient` | 0xe0 | IOUserClient → IOService → IORegistryEntry |
| `AppleMobsiTmpSADC` | 0xe0 | AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `ApplePMGRTempSensor` | 0x138 | IOService → IORegistryEntry |
| `ApplePMGRTempUserClient` | 0x108 | AppleTempSensorUserClient → IOUserClient → IOService → IORegistryEntry |
| `AppleSCCTempSensor` | 0x108 | AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSetDroopUtilizationControlEffortFunction` | 0x30 | AppleARMFunction |
| `AppleSocHot` | 0x198 | IOService → IORegistryEntry |
| `AppleT700XTempSensor` | 0x198 | ApplePMGRTempSensor → IOService → IORegistryEntry |
| `AppleT700XTempSensorDisableSensorFunction` | 0x30 | AppleARMFunction |
| `AppleT700XTempSensorUserClient` | 0x108 | AppleTempSensorUserClient → IOUserClient → IOService → IORegistryEntry |
| `AppleT8015TempSensor` | 0x1b8 | AppleT700XTempSensor → ApplePMGRTempSensor → IOService → IORegistryEntry |
| `AppleT8020MTRTempSensor` | 0x1d8 | AppleT8015TempSensor → AppleT700XTempSensor → ApplePMGRTempSensor → IOService → IORegistryEntry |
| `AppleTempSensorUserClient` | 0x100 | IOUserClient → IOService → IORegistryEntry |
| `AppleVTempDispatcher` | 0xa8 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000032f0 off=0x0045a100-0x0045d3f0 addr=0xfffffe000745e100-0xfffffe00074613f0 r--/r--   __TEXT            
	sz=0x00002be8 off=0x0045a778-0x0045d360 addr=0xfffffe000745e778-0xfffffe0007461360               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000090 off=0x0045d360-0x0045d3f0 addr=0xfffffe0007461360-0xfffffe00074613f0               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x0001569c off=0x01c77b30-0x01c8d1cc addr=0xfffffe0008c7bb30-0xfffffe0008c911cc r-x/r-x   __TEXT_EXEC       
	sz=0x0001523c off=0x01c77b30-0x01c8cd6c addr=0xfffffe0008c7bb30-0xfffffe0008c90d6c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000460 off=0x01c8cd6c-0x01c8d1cc addr=0xfffffe0008c90d6c-0xfffffe0008c911cc          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000007f8 off=0x0493f958-0x04940150 addr=0xfffffe000b943958-0xfffffe000b944150 rw-/rw-   __DATA            
	sz=0x000003f0 off=0x0493f958-0x0493fd48 addr=0xfffffe000b943958-0xfffffe000b943d48               __DATA.__data             
	sz=0x00000308 off=0x00000000-0x00000308 addr=0xfffffe000b943d48-0xfffffe000b944050               __DATA.__common           (Zerofill)
	sz=0x00000100 off=0x00000000-0x00000100 addr=0xfffffe000b944050-0xfffffe000b944150               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00008070 off=0x01086cd0-0x0108ed40 addr=0xfffffe000808acd0-0xfffffe0008092d40 rw-/rw-   __DATA_CONST      
	sz=0x00000078 off=0x01086cd0-0x01086d48 addr=0xfffffe000808acd0-0xfffffe000808ad48         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000078 off=0x01086d48-0x01086dc0 addr=0xfffffe000808ad48-0xfffffe000808adc0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000077e0 off=0x01086dc0-0x0108e5a0 addr=0xfffffe000808adc0-0xfffffe00080925a0         __DATA_CONST.__const            
	sz=0x000004c0 off=0x0108e5a0-0x0108ea60 addr=0xfffffe00080925a0-0xfffffe0008092a60         __DATA_CONST.__kalloc_type      
	sz=0x00000230 off=0x0108ea60-0x0108ec90 addr=0xfffffe0008092a60-0xfffffe0008092c90         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000b0 off=0x0108ec90-0x0108ed40 addr=0xfffffe0008092c90-0xfffffe0008092d40         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 162 at 0x04ad8f30
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     CC7BE7ED-AD07-3D6A-9173-9068F7302E4C
008: LC_SOURCE_VERSION           189.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9f3f0 size=0x298
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleEmbeddedTempSensor`
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedTempSensor`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleEmbeddedTempSensor`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSignature`: `????`
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
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleEmbeddedTempSensor.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901235456`
- `_PrelinkExecutableRelativePath`: `AppleEmbeddedTempSensor`
- `_PrelinkExecutableSize`: `135668`
- `_PrelinkExecutableSourceAddr`: `-2198901235456`
- `_PrelinkKmodInfo`: `-2198828992168`

## Strings (348) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `assert-count-value-1`
- `121111121222121211111112111222221222222`
- `die_alarm1_temp`
- `sensor-offset-CTL0-set`
- `ApplePMGRTempSensor::start: checking for expect-dietmpctl\n`
- `createTimerEvent`
- `AETS: %s is not entitled\n`
- `AppleDieTempController::%s: Loop%d Sensors: %c%c%c%c\n`
- `AppleDieTempController::%s: Got CLPC version %d\n`
- `%s::%s: missing device tree value (%s)\n`
- `121111121222121211112222222112111111221222222222222`
- `sensor-offset-alarm1`
- `sensor-offset-readSum`
- `site.AppleDieTempController`
- `CameraStrobeMaxLoad`
- `ApplePMGR`
- `\"No loop config data found for %s\" @%s:%d`
- `Avg: `
- `AppleDieTempController::%s: Loop: %d kp: 0x%x kits: 0x%x ctlType: 0x%x numSensors: %d\n`
- `AppleDieTempController::%s: Override loop %d kits to 0x%x\n`
- `dockchanneltotGraphInit`
- `mitigation_mode`
- `skip-trip-temp-config`
- `AMC`
- `CH1RNKCFG0`
- `%s: Sensor off\n`
- `dvd-factor`
- `CH3RNKCFG1`
- `ApplePMGR: Missing Device Tree value\n`
- `121111121222121211111111111222222222222222222222211222222211222222211222222211222222211221111`
- `\"Bad uart_dock_data_base base for tGraphModeEnable \" @%s:%d`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d, Ids %d/%d/%d/%d)\" @%s:%d`
- `DVFM SCC`
- `CH1RNKCFG1`
- `AppleVTempDispatcher::%s: Empty setProperty\n`
- `site.AppleARMPMUTempSensor`
- `121111121222121211111111111111111`
- `%s::%s: couldn't create interrupt handler\n`
- `AppleARMPMUSensor`
- `1211111212221212111122222221121111112212222222222222212`
- `site.ApplePMGRTempSensor`
- `loop%d-control`
- `\"Bad uart_control_base base for tGraphModeEnable \" @%s:%d`
- `PerfMaxTarget`
- `sensor-offset-status`
- `sensor-accuracy`
- `AppleSocHot`
- `sensor-offset-statMask`
- `printLoopConfigs`
- `LifetimeServoDieTemperatureTargetPropertyKey`
- `sochot_ctl`
- `assert_count_0`
- `gpuPerfControllerArrivalHandler`
- `AppleDieTempController::%s: Printing all configured loop data\n`
- `dietempctl_kits`
- `stop`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d)\" @%s:%d`
- `AppleT700XTempSensorUserClient`
- `%s::%s: couldn't create command gate\n`
- `reg-64-bit`
- `%s: Couldn't find AppleSocHot instance\n`
- `loop-release-temp`
- `UnderVoltageEventCount`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d, Ids %d/%d/%d/%d/%d/%d/%d/%d/%d)\" @%s:%d`
- `AppleDieTempController::%s: Override loop %d kp to 0x%x\n`
- `gpu-temperature-offset-value`
- `apply-trim-workaround`
- `site.AppleT700XTempSensorDisableSensorFunction`
- `%s %s`
- `site.AppleARMPMUPowerSensor`
- `AppleDieTempController::%s: In handleBootArgs routine\n`
- `AppleDieTempController::%s: Override kp to %d\n`
- `die_alarm_temp`
- `T8015 Die Temp Sensor`
- `sensor-offset-CTL0`
- `dietempctl_loop%d_kp`
- `assert-count-value-0`
- `AppleSCCTempSensor`
- `CH0RNKCFG0`
- `%s::%s: alarm temp (%d C)\n`
- `%s: Failed to create command gate!\n`
- `1211111212221212111111111111`
- `\"Couldn't find any data for loop-sensor-set%d\" @%s:%d`
- `GPUMaxPerf`
- `deassert-count-value-1`
- `site.AppleVTempDispatcher`
- `12111112122212121111111111111111`
- `1211111212221212111111121122`
- `loop-interval`
- `rearmSensors`
- `odts`
- `start`
- `sensor-offset-CTL2-set`
- `121111121222121211111112111121`
- `failsafe_ctrl`
- `disable-aets-fastdie`
- `AppleDieTempController::%s: couldn't start provider\n`
- `has-two-p-clusters`
- `dietempctl_interval`
- `failsafe_en_ctrl_offset`
- `offset`
- `GPUMtrAverageTemp`
- `AppleVTempDispatcher::%s: Error could not find sensor %s in dictionary\n`
- `AppleDieTempController::%s: No loops exist for registering this sensor\n`
- `site.AppleSetDroopUtilizationControlEffortFunction`
- `site.AppleT8020MTRTempSensor`
- `location-%s`
- `gfx_divider_0`
- `AppleSocHot::start _tempSensorSochotDebugHackEnabled\n`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d, Ids %d/%d/%d/%d/%d/%d/%d/%d/%d)\" @%s:%d`
- `QueueSize`
- `%s::%s: couldn't add timer event source to work loop\n`
- `AppleDieTempController.cpp`
- `\"Too many loops defined\" @%s:%d`
- `AppleDieTempController::%s: boot_dvd_factor 0x%08x\n`
- `sensor-offset-CTL1`
- `DieTempControllerResource`
- `%s: Couldn't match AppleSocHot service\n`
- `SetCLTMPerfMax`
- `AMCTempSensor`
- `AMC TempSensor: Missing Device Tree value\n`
- `sensor-offset-readBK`
- `root`
- `\"Bad dock_agent_base disabling tGraphModeEnable \" @%s:%d`
- `AppleDieTempController::%s: pmgr null dict\n`
- `AppleDieTempController::%s: props is NULL\n`
- `ODTS-TempDrtEn`
- `ApplePMGRTempUserClient`
- `AppleT700XTempSensor`
- `sensor-offset-CTL2-clr`
- `AppleDieTempController::%s: couldn't create command gate\n`
- `\"Couldn't configure fast die control loop(s)\" @%s:%d`
- `AppleDieTempController::%s: _cpuPerfController is NULL\n`
- `gfx_divider_1`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d, Ids %d/%d/%d/%d)\" @%s:%d`
- `T8020 MTR Die Temp Sensor`
- `AppleTempSensorUserClient`
- `location-id-%s`
- `invokes-sochot`
- `AppleDieTempController::%s: Override kits to %d\n`
- `%s::%s: couldn't create max temp sensor\n`
- `setPropertiesGated`
- `AppleARMPMUPowerSensor`
- `sochot-temperature-tolerance`
- `%s::%s: sochot tolerance (%d C)\n`
- `ApplePMGRTempSensor`
- `%s::%s: couldn't create timer event source\n`
- `loop-kp`
- `T700X Die Temp Sensor`
- `handleBootArgs`
- `dietempctl_kp`
- `getDieTemperatures`
- `AppleDieTempController::%s: NULL properties dictionary\n`
- `AppleDieTempController::%s:  Config Complete %x\n`
- `target-dvfm-state-0`
- `odts_mapping`
- `alarm0-temp`
- `AppleDieTempController::%s: pmgr null propData\n`
- `AppleDieTempController::%s: could not connect to %s\n\n`
- `AppleDieTempController::%s: iterator is NULL\n`
- `use_int`
- `site.AMCTempSensor`
- `sensor-offset-alarm2`
- `%s: Skipping sochot panic due to low temp: %d alarm1: %d tolerance: %d`
- `AppleDieTempController::%s: sensor data length doesn't make sense: %d\n`
- `AppleDieTempController::%s: couldn't cast dictionary\n`
- `loop-count`
- `loop%d-sensor-set`
- `pmgr`
- `AppleSetDroopUtilizationControlEffortFunction`
- `AppleSOCHOT could not connect to %s\n`
- `AppleSCCTempSensor provider is not AppleARMIODevice\n`
- `_timeoutOccurredGated`
- `AppleSocHot: Sochot0 using trip temp %d\n`
- `temp_sensor_sochot_debug_hack`
- `sochot_temp0`
- `sochot_temp1`
- `%s::%s: could not connect to %s\n\n`
- `%s: Max String name too long!\n`
- `loop%d-ki`
- `cpuPerfControllerArrivalHandler`
- `setGPUMaxPerfState`
- `site.AppleT700XTempSensorUserClient`
- `%s::%s: provider is not AppleARMIODevice\n`
- `%s%s`
- `%s: Failed creation of interrupt handler !\n`
- `dietempctl_release`
- `AppleDieTempController::%s: Override interval to %d\n`
- `SetMaxGPUUtilization`
- `CH2RNKCFG0`
- `AppleDieTempController::%s:  _tGraphModeEnable(%x) config complete\n`
- `trip_temp_1`
- `AppleT8020MTRTempSensor`
- `%s::%s: couldn't map device memory\n`
- `AppleARMPMUTempSensor`
- `ApplePMGRTempSensor::start: past _fDieTempController init code with _fDieTempController %p\n`
- `clpcPerfControllerArrivalHandler`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d, Ids %d/%d/%d/%d/%d/%d/%d/%d/%d)\" @%s:%d`
- `location-name`
- `location-id`
- `Service arrived\n`
- `sensor-offset-readCnt`
- `initLoopConfig`
- `ApplePMGRTempSensor provider is not AppleARMIODevice\n`
- `\"Bad dockChannelIndex %d for tGraphModeEnable \" @%s:%d`
- `readBootDVDFactor`
- `AppleSocHot: Disable sochot1\n`
- `AMC TempSensor provider is not AppleARMIODevice\n`
- `%s::%s: couldn't start provider\n`
- `%s::%s: invalid data packet\n`
- `calculateLoopMaxDieTemperatures`
- `site.AppleSCCTempSensor`
- `scc`
- `sensor-offset-alarm3`
- `setAETSMaxControlEffortFunction`
- `AppleDieTempController::%s: Loop %d control type: %d\n`
- `tGraphClient`
- `site.ApplePMGRTempUserClient`
- `AppleDieTempController::%s: couldn't create dieTempSensorsSnapshot\n`
- `CH2RNKCFG1`
- `alarm1-temp`
- `sensor-offset-CTL2`
- `sensor-offset-readBK1`
- `site.AppleTempSensorUserClient`
- `handleInterrupt`
- `PMGR SOC DIE Temp Sensor`
- `AppleCLPC`
- `setupLegacyControlLoop`
- `%s::%s: couldn't create average temp sensor\n`
- `Max: `
- `sochot_tolerance`
- `\"Sensor registered with ADTC, but was not assigned to any control loop\" @%s:%d`
- `AppleSocHot provider is not AppleARMIODevice\n`
- `AppleSocHot.cpp`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d, Ids %d/%d/%d)\" @%s:%d`
- `setCPUMaxPerfState`
- `site.AppleSocHot`
- `AppleDieTempController::%s: pmgr null service\n`
- `loop%d-kp`
- `AppleDieTempController::%s: Loop %d kp: 0x%x\n`
- `#clpc-version`
- `Target`
- `AppleSocHot: Disable sochot0\n`
- `ODTSMAPPING`
- `sensor-offset-CTL0-clr`
- `alarm-temp`
- `%s: Avg String name too long!\n`
- `AppleARMPerformanceControllerDVDFactor1`
- `sochot0`
- `failsafe_en_ctrl`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d, Ids %d/%d/%d/%d/%d/%d/%d/%d/%d)\" @%s:%d`
- `AppleSCCTempSensor: Missing Device Tree value\n`
- `AppleDieTempController::%s: couldn't create loop %d sensor set\n`
- `function-clear_dither`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d, Ids %d/%d/%d/%d/%d/%d)\" @%s:%d`
- `CH0RNKCFG1`
- `gpu-sensor-max`
- `%s::%s: Initiating SOCHOT, temp=%d, sensor=%x\n`
- `121111121222121211112222222112111111221`
- `site.AppleDieTempControllerUserClient`
- `AppleDieTempController::%s: No loop sensor data for loop %d\n`
- `AppleDieTempController::%s: Override release temp to %d\n`
- `target-dvfm-state-1`
- `AppleSocHot: provider missing function-clear_dither\n`
- `AppleDieTempController::%s: couldn't create _dieTempSensors\n`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d)\" @%s:%d`
- `slope`
- `%s::%s: alarm 1 temp (%d C)\n`
- `AppleDieTempController::%s: key is NULL\n`
- `121111121222121211111`
- `DieTempControl`
- `calibration_address`
- `site.AppleT8015TempSensor`
- `AppleDieTempControllerUserClient`
- `deassert_count_1`
- `skip-assert-count-config`
- `sochotX`
- `AppleDieTempController`
- `GPUPowerTarget`
- `assert_count_1`
- `sensor-offset-params`
- `AppleDieTempController::%s: couldn't create loopSensorsSnapshot\n`
- `AppleSocHot: Sochot1 using trip temp %d\n`
- `trip_temp_0`
- `scc_tmp_sen_rslt`
- `sensor-offset-alarm0`
- `%s: Override Alarm Temp with %dC\n`
- `\"Bad uart_data_base base for tGraphModeEnable \" @%s:%d`
- `SOCHOT`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d)\" @%s:%d`
- `site.AppleT700XTempSensor`
- `AppleT700XTempSensorDisableSensorFunction`
- `AppleDieTempController::%s: Loop %d ki: 0x%x\n`
- `loop-kits`
- `trim-workaround-value`
- `ApplePMGRTempSensor::start: useFastDieTempController %d\n`
- `AppleMobsiTmpSADC`
- `scc_divider_0`
- `scc_divider_1`
- `deassert-count-value-0`
- `AppleVTempDispatcher`
- `AppleVTempDispatcher::%s: Could not add command gate to workloop\n`
- `AppleDieTempController::%s: provider is not AppleARMIODevice\n`
- `AppleDieTempController::%s: Successfully configured %d loops\n`
- `setGPUMaxPower`
- `AppleDieTempController::%s: couldn't create _dieTempControllerLock\n`
- `sensor-AvgMax`
- `sensor-offset-CTL3-clr`
- `121111`
- `dietempctl_loop%d_kits`
- `temperature-offset-value`
- `GPUMtrMaxOverallTemp`
- `AppleVTempDispatcher::%s: Could not init dict\n`
- `expect-dietempctl`
- `site.AppleMobsiTmpSADC`
- `ExternalControlEffort`
- `deassert_count_0`
- `12111112122212121111222222211211111122122222222222222121222`
- `AppleVTempDispatcher::%s: AppleVTempDispatcher provider is not AppleARMIODevice\n`
- `12111112122212121111111211112122`
- `AppleT8015TempSensor`
- `sochot1`
- `%s::%s: alarm 0 temp (%d C)\n`
- `%s::%s: sensor off\n`
- `cluster-sensor`
- `%s::%s: Got temperatureOffsetValue of %d for locationID 0x%x\n`
- `%s: sensor:0x%x status: 0x%llx current CTL0 value: 0x%llx alarm0: 0x%llx alarm1: 0x%x\n`
- `AppleDieTempController::%s: couldn't create _loopTimer\n`
- `\"AppleSocHot: Hot Hot Hot source\" @%s:%d`
- `sensor-offset-CTL1-set`
- `sensor-offset-CTL1-clr`
- `sensor-offset-CTL4-set`
- `sensor-offset-CTL4-clr`
- `%s: Couldn't find die temp controller\n`
- `registerSensorInstance`
- `PrintFastDieLoopConfig`
- `121111121222121211111112112112222`
- `sensor-offset-CTL3-set`
- `site.AppleARMPMUSensor`
- `com.apple.private.aets.user-access`
- `AppleDieTempController::%s: \n`
- `AppleDieTempController::%s: couldn't add timer to workloop\n`
- `AppleDieTempController::%s: Setting up legacy style (single loop) fast die control\n`
- `GPUMaxPower`
- `CH3RNKCFG0`
- `IOAcceleratorES`
- `tgraph-dock-ch-index`
- `121111121222121212111111111222222222222222122122221`
