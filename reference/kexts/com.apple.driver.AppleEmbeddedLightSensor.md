# `com.apple.driver.AppleEmbeddedLightSensor`

- Name: AppleEmbeddedLightSensor
- Version: `1.0.0d1`
- UUID: `E97DF39D-D25F-3480-96A2-04BF6C952D3E`
- Source version: `2300.52.5.0.0`
- Depends on: [`com.apple.EXBrightCalibrationConsumer`](com.apple.EXBrightCalibrationConsumer.md) 1.0.0, [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleSPU`](com.apple.driver.AppleSPU.md) 1.0.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.4, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 14.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (6) [KC]

### AppleCT819
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedLightSensor`
- `IOClass`: `AppleCT819`
- `IONameMatch`: `als,ct819`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedLightSensor`
- `IOProviderClass`: `AppleARMIICDevice`

### AppleCT821
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedLightSensor`
- `IOClass`: `AppleCT821`
- `IONameMatch`: `als,ct821`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedLightSensor`
- `IOProviderClass`: `AppleARMIICDevice`

### AppleISL29023
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedLightSensor`
- `IOClass`: `AppleISL29023`
- `IONameMatch`: `als,isl29023`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedLightSensor`
- `IOProviderClass`: `AppleARMIICDevice`

### AppleSPUCT836
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedLightSensor`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `4`
    - `DeviceUsagePage`: `65280`
- `IOClass`: `AppleSPUCT836`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedLightSensor`
- `IOProviderClass`: `IOHIDInterface`
- `manufacturer`: `Goldeen`

### AppleTSL2561
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedLightSensor`
- `IOClass`: `AppleTSL2561`
- `IONameMatch`: `als,tsl2561`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedLightSensor`
- `IOProviderClass`: `AppleARMIICDevice`

### AppleTSL2581
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedLightSensor`
- `IOClass`: `AppleTSL2581`
- `IONameMatch`: `als,tsl2581`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedLightSensor`
- `IOProviderClass`: `AppleARMIICDevice`


## C++ classes (8) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleCT819` | 0x2d8 | AppleEmbeddedI2CLightSensor → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleCT821` | 0x348 | AppleEmbeddedI2CLightSensor → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleEmbeddedI2CLightSensor` | 0x188 | AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleISL29023` | 0x1a8 | AppleEmbeddedI2CLightSensor → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUALSLuxDriver` | 0x280 | AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUCT836` | 0x410 | AppleSPUALSLuxDriver → AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleTSL2561` | 0x210 | AppleEmbeddedI2CLightSensor → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleTSL2581` | 0x2e8 | AppleEmbeddedI2CLightSensor → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00005d93 off=0x00449570-0x0044f303 addr=0xfffffe000744d570-0xfffffe0007453303 r--/r--   __TEXT            
	sz=0x000015b8 off=0x00449bf0-0x0044b1a8 addr=0xfffffe000744dbf0-0xfffffe000744f1a8               __TEXT.__const            
	sz=0x0000412f off=0x0044b1a8-0x0044f2d7 addr=0xfffffe000744f1a8-0xfffffe00074532d7               __TEXT.__cstring          (CstringLiterals)
	sz=0x0000002c off=0x0044f2d7-0x0044f303 addr=0xfffffe00074532d7-0xfffffe0007453303               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0001508c off=0x01c2e510-0x01c4359c addr=0xfffffe0008c32510-0xfffffe0008c4759c r-x/r-x   __TEXT_EXEC       
	sz=0x00014cbc off=0x01c2e510-0x01c431cc addr=0xfffffe0008c32510-0xfffffe0008c471cc          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000003d0 off=0x01c431cc-0x01c4359c addr=0xfffffe0008c471cc-0xfffffe0008c4759c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000005e0 off=0x0493ee10-0x0493f3f0 addr=0xfffffe000b942e10-0xfffffe000b9433f0 rw-/rw-   __DATA            
	sz=0x00000488 off=0x0493ee10-0x0493f298 addr=0xfffffe000b942e10-0xfffffe000b943298               __DATA.__data             
	sz=0x00000158 off=0x00000000-0x00000158 addr=0xfffffe000b943298-0xfffffe000b9433f0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00004920 off=0x0107ec10-0x01083530 addr=0xfffffe0008082c10-0xfffffe0008087530 rw-/rw-   __DATA_CONST      
	sz=0x00000040 off=0x0107ec10-0x0107ec50 addr=0xfffffe0008082c10-0xfffffe0008082c50         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000040 off=0x0107ec50-0x0107ec90 addr=0xfffffe0008082c50-0xfffffe0008082c90         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00004400 off=0x0107ec90-0x01083090 addr=0xfffffe0008082c90-0xfffffe0008087090         __DATA_CONST.__const            
	sz=0x00000200 off=0x01083090-0x01083290 addr=0xfffffe0008087090-0xfffffe0008087290         __DATA_CONST.__kalloc_type      
	sz=0x000001e8 off=0x01083290-0x01083478 addr=0xfffffe0008087290-0xfffffe0008087478         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000b8 off=0x01083478-0x01083530 addr=0xfffffe0008087478-0xfffffe0008087530         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 145 at 0x04ad878c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     E97DF39D-D25F-3480-96A2-04BF6C952D3E
008: LC_SOURCE_VERSION           2300.52.5.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9ef38 size=0x1d0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleEmbeddedLightSensor`
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedLightSensor`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleEmbeddedLightSensor`
- `CFBundleNumericVersion`: `16785409`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0d1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91014`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91014`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2007-2018 Apple Inc. All rights reserved.`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleEmbeddedLightSensor.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901303952`
- `_PrelinkExecutableRelativePath`: `AppleEmbeddedLightSensor`
- `_PrelinkExecutableSize`: `130335`
- `_PrelinkExecutableSourceAddr`: `-2198901303952`
- `_PrelinkKmodInfo`: `-2198828995056`

## Strings (444) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `ERROR: The numRegions in LSCI4.5 calibration data is too large.`
- `AppleTSL2561::handleStart -- No LUX extrapolation curve information\n`
- `ALS: [AppleTSL2561] setPropertiesGated: requested ReportInterval=0 turn OFF sensor\n`
- `ALSSensorMax`
- `is-accessory`
- `alsCalibrationHeader.majorVers = %d\n`
- `rapidModeGain = %d\n`
- `AppleCT819`
- `AppleTSL2581::handleStart - _blLeakageCh0 = %ld\n`
- `AppleTSL2581::handleStart -- vers=%d.%d, size=%d, chksum=%d\n`
- `AppleEmbeddedI2CLightSensor::%s: preemptive startup interrupt fired \n`
- `121111121222121211111112111122222212211111111112222222222222222221`
- `121111121222121211111112111122222212211111111112222222222222222222222222222222222222222222221`
- `ch0GainFactor16X = %ld/1000\n`
- `placement = %d\n`
- `ALS: [AppleCT821] setPropertiesGated: newGain =%d\n`
- `IOHIDALSRunHistorical`
- `AppleTSL2561::handleStart -- Too many curve segments.. \n`
- `ALS: [AppleTSL2561] setPropertiesGated: Requested: interval=%ld mics, Setting: interval=%ld mics\n`
- `AppleTSL2581::probe - Probing hardware failed (%s) \n`
- `AppleTSL2581::probe - Probing hardware found (%d) \n`
- `AppleCT821::handleStart -- Insufficient ratioLimits.. \n`
- `AppleCT821::handleStart -- vers=%d.%d, size=%d, chksum=%d\n`
- `ALSLPannelValues`
- `AOP ALSS Function instantiated!\n`
- `com.apple.CoreBrightness`
- `ReportInterval`
- `alsCalibrationDataHeader.chksum = %d\n`
- `ch1GainFactor16X = %d/1000\n`
- `ch1GainFactor32X_64X = %lld / 1000\n`
- `ALS: [AppleCT821] %s: _blLeakageNits updated to: %d / 1000 | %d / 1000 | %d / 1000 \n`
- `AppleISL29023::handleStart -- Probing hardware failed (%s).\n`
- `%s: override lux %s \n`
- `ALSCalibrationData`
- `yCurrentRegion negative!, window %d!!\n`
- `_setProperties`
- `ch0MedBacklightLeakageCounts = %d\n`
- `ALS: [AppleCT819] setPropertiesGated: newGain =%d\n`
- `ALSSuperFastIntegrationTime`
- `probe-for-hardware`
- `AppleTSL2581`
- `alsCalibrationDataWords13_17.ch1DarkCounts = %d\n`
- `OverRideIntegrationTime`
- `rapidModeIntegrationTime = %d\n`
- `AppleCT819::handleStart -- No LUX extrapolation curve information\n`
- `1`
- `%s::%s getPowerState()=%u powerStateOrdinal=%lu _reportInterval_us=%u\n`
- `AppleEmbeddedI2CLightSensor::setPropertiesGated: override value: %u \n`
- `NoInterrupts`
- `AppleCT819::probe - Probing hardware found (%d) \n`
- `ch0Coeff1 = %lld / 1000\n`
- `AppleSPUALSLuxDriver`
- `getPlacement`
- `ALSSAvailable`
- `12`
- `key press`
- `AppleTSL2581::probe - ALS_INT is in proper state - result = %x (%s), and isINTasserted= %x \n`
- `[%ld %ld]\n`
- `site.AppleCT821`
- `ALSTestMode`
- `GreenCoefficient`
- `3`
- `10`
- `AppleEmbeddedI2CLightSensor::%s: Turn ON Sensor on %s\n`
- `function-int_status`
- `AppleTSL2581::handleStart - Too Many custom curve segments. Actual: %d, Expected: %d\n`
- `ch1GainFactor1X = %ld/1000\n`
- `IOHIDPlacementType`
- `skip-sensor-calibration`
- `AppleCT821::handleStart - gain for luxCurves reg= 0x%x\n`
- `AppleCT821::handleStart - Need at least header size bytes. Actual: %d, Expected: %ld\n`
- `slowModeGain = %d\n`
- `_blLeakageNits[0] = %ld / 1000 \n`
- `IOHIDALSRawMode`
- `ALSRunHistorical`
- `ALSSetProperty`
- `AppleSPUCT836::%s: AODALSMode = %d\n`
- `AppleTSL2561::handleStart -- Insufficient intercepts.. \n`
- `alsCalibrationDataHeader.size = %d\n`
- `AppleCT821::handleStart\n`
- `ch0GainFactor8X = %d/1000\n`
- `loadCalibrationData`
- `ALSSCalDBV`
- `DefaultInterval`
- `ch1GainFactor8X = %ld/1000\n`
- `[%ld %ld %ld], `
- `size = %d\n`
- `AppleISL29023`
- `setIntegrationMode`
- `AppleSPUALSLuxDriver:%s AOP orientation = %d`
- `MultiTouchPowerChild`
- `site.AppleTSL2561`
- `backlight-leakage-channel1`
- `alsCalibrationDataHeader.numLuxCurves = %d\n`
- `\nalsLuxSingleCurveCoefficients(divide by 100 to get float value) -`
- `ch0GainFactor64X_140X = %lld / 1000\n`
- `Override`
- `ALSSlowIntegrationTime`
- `ALSIntegrationMode`
- `alsCalibrationDataWords13_17.ch0HighBacklightLeakageCounts = %d\n`
- `%s::%s - CRITICAL ERROR: attempt to access memory out of bounds - skipping calibration (probably bad calibration)\n`
- `ch0GainFactor4X = %d/1000\n`
- `ch0GainFactor140X = %d/1000\n`
- `SupportDynamicGain`
- `ALSS: Display ALSS Function %p\n`
- `handleStart`
- `ch0GainFactor32X = %d/1000\n`
- `alsCalibrationHeader.chksum = %d\n`
- `ch1GainFactor0 = %lld / 1000\n`
- `off`
- `ON`
- `AppleCT819::handleStart -- Too many curve segments.. \n`
- `CBAODSendSamplesToDCP`
- `DelayedALSOverride`
- `useFDRCalibration`
- `9`
- `IOHIDEventService`
- `ch1GainFactor16X = %ld/1000\n`
- `AppleCT821`
- `sensorType = %d\n`
- `%s::%s - calibrated successfully!\n`
- `Goldeen driver found\n`
- `AppleARMBacklight`
- `RGB coeffs IOFixed %x, %x, %x\n`
- `Ch0LowThreshold`
- `AppleCT819::handleStart -- Insufficient ratioLimits.. \n`
- `AppleCT819::handleStart - gain for luxCurves reg= 0x%x\n`
- `ch0GainFactor128X = %d/1000\n`
- `AppleTSL2561::setSensorEnabled *** FAILED ***: _writeReg8 kTSL256xControl=%x result=%s\n`
- `AppleCT821::handleStart -- Insufficient intercepts.. \n`
- `slowModeIntegrationTime = %d\n`
- `ch0GainFactor1X_2X = %lld / 1000\n`
- `ALS: [AppleCT819] setPropertiesGated: _alsRawMode=%d\n`
- `AppleSPUCT836`
- `AppleCT821::handleStart -- Too many curve segments.. \n`
- `AppleCT821::handleStart -- Clipping integration cycles (%d) to max allowed (%d).. \n`
- `_backlightLeakageCh0Slope[0] = %ld / 1000 \n`
- `_backlightLeakageCh1Offset[1] = %ld / 1000 \n`
- `ALS: [AppleCT821] setPropertiesGated: ch0 override set to %d \n`
- `getOrientation`
- `ERROR: '%s' is empty!\n`
- `11`
- `AppleTSL2581::handleStart - Using a single equation for ALS Lux translation\n`
- `alsCalibrationDataWords13_17.ch0GainFactor16X_111X = %ld/1000\n`
- `ch1GainFactor64X = %d/1000\n`
- `ch0LowBacklightLeakageCounts = %d\n`
- `_backlightLeakageCh0Offset[1] = %ld / 1000 \n`
- `site.AppleSPUCT836`
- `ALS: [AppleCT821] setPropertiesGated: channel override turned %s \n`
- `site.AppleCT819`
- `_eventServiceCallbackGated`
- `ch1GainFactor140X = %d/1000\n`
- `ALS: [AppleCT821] setPropertiesGated: _alsRawMode=%d\n`
- `Ch1OverrideValue`
- `site.AppleISL29023`
- `AppleCT819::handleStart -- Insufficient intercepts.. \n`
- `AppleCT819::Fudge factor = 0x%X\n`
- `ALSOverrideState`
- `AppleMultitouchSPI`
- `backlight-leakage-channel0`
- `ALSIntegrationCycles`
- `alsCalibrationDataWords13_17.ch1MedBacklightLeakageCounts = %d\n`
- `ch0GainFactor64X = %d/1000\n`
- `ch0GainFactor2X_4X = %lld / 1000\n`
- `ch0GainFactor1X_8X = %lld / 1000\n`
- `AABSensorOverrideOrientation`
- `AppleSPUCT836::%s failed to create event\n`
- `AppleTSL2581::handleStart -- Too many curve segments.. \n`
- `alsCalibrationDataWords13_17.ch0GainFactor1X_8X = %ld/1000\n`
- `ALS: [AppleTSL2581] _setALSReportingInterval: Requested: interval=%ld mics, Setting: interval=%ld mics\n`
- `AppleTSL2581::_calculateAmbient -- unknown _gainUsedForLuxCurves\n`
- `ALS: [AppleCT821] _setALSReportingInterval: Requested: interval=%d mics, Setting: interval=%d mics\n`
- `on`
- `AppleEmbeddedI2CLightSensor::%s: interrupt handling for preemptive startup \n`
- `IOHIDALSGain`
- `aCoeff1 = %lld / 1000\n`
- `ch1DarkCounts = %d\n`
- `ch0GainFactor16X_32X = %lld / 1000\n`
- `ALS: [AppleCT821] setPropertiesGated: _alsContinuousMode=%d\n`
- `ratio = %lld / 1000\n`
- `LogLevel`
- `ERROR: Coefficient '%s' is empty!\n`
- `PrimaryUsagePage`
- `AppleEmbeddedI2CLightSensor::setPropertiesGated: request to turn OFF the sensor\n`
- `ch0GainFactor8X = %ld/1000\n`
- `AppleCT821::probe - Probing hardware found (%d) \n`
- `ALS: [AppleCT821] setPropertiesGated: dynamic gain support turned %s \n`
- `lux-scale`
- `ALSS COEFF r %#x, g %#x, b %#x\n`
- `2`
- `IOHIDALSTestMode`
- `7`
- `setPowerStateGated`
- `AppleEmbeddedI2CLightSensor::setPropertiesGated: override %s \n`
- `AppleEmbeddedI2CLightSensor::%s: ktrace first sample (0x%X) \n`
- `AppleTSL2581::handleStart -- Insufficient ratioLimits.. \n`
- `disabled`
- `AppleTSL2561`
- `AppleTSL2561::handleStart -- Insufficient ratioLimits.. \n`
- `ch0GainFactor16X = %d/1000\n`
- `bCoeff2 = %lld / 1000\n`
- `_backlightLeakageCh1Offset[0] = %ld / 1000 \n`
- `Ch0HighThreshold`
- `AppleEmbeddedI2CLightSensor::_setProperties - could not initWithDictionary \n`
- `alsCalibrationDataHeader.majorVers = %d\n`
- `AppleCT821::handleStart - integCycles = %d\n`
- `ch0GainFactor16X_111X = %lld / 1000\n`
- `Successfully obtained ALS placement=%u and orientation=%u!\n`
- `AppleSPUCT836::%s: CBAODSendSamplesToDCP = %d\n`
- `AABSensorOverrideValue`
- `BlueCoefficient`
- `default`
- `DeviceUsagePairs`
- `IOHIDBacklightLevel`
- `alsCalibrationHeader.size = %d\n`
- `enabled`
- `AppleSPUALSLuxDriver::%s Setting mode %d\n`
- `FDRCalibration`
- `AppleTSL2561::handleStart - Probing hardware failed (%s) \n`
- `alsCalibrationDataWords13_17.ch1GainFactor16X_111X = %ld/1000\n`
- `Cal Data for Sensor --\n`
- `ALS: [AppleCT821] setPropertiesGated: low threshold cap set to %d percent \n`
- `AppleCT819::handleStart Could not find calibration data for placement: %d, orientation: %d\n`
- `%s: manufacturer %s\n`
- `eventServiceCallback`
- `AppleTSL2581::handleStart -- Insufficient intercepts.. \n`
- `AppleCT821::probe - ALS_INT is stuck low.. Disabling ALS. result = %x (%s), and isINTasserted= %x \n`
- `AppleCT819::probe - ALS_INT is in proper state - result = %x (%s), and isINTasserted= %x \n`
- `AppleSPUALSLuxDriver:%s EDT placement = %d`
- `%s: Unrecognized command %d received for ALSS!\n`
- `OverrideDelay`
- `13`
- `ch1GainFactor1X_2X = %lld / 1000\n`
- `AutoRateControl`
- `ALSS: IOMFB says ALSS is available but can't find function-alss, might be a DCP platform`
- `ERROR: The LSCI4.x calibration key is too small\n`
- `DeviceUsagePage`
- `integrationCycles`
- `alsCalibrationDataWords13_17.ch1GainFactor8X_16X = %ld/1000\n`
- `Length is not even, shouldn't be the case (%d)\n`
- `ch1GainFactor8X = %d/1000\n`
- `AppleSPUALSLuxDriver:%s AOP placement = %d`
- `AppleTSL2581::handleStart wrong chksum for the ALS calibration data\n`
- `alsCalibrationResverveBytes.integrationTime = %d\n`
- `ch1GainFactor4X = %d/1000\n`
- `aCoeff2 = %lld / 1000\n`
- `ch1GainFactor2X_4X = %lld / 1000\n`
- `Value`
- `ALSSSupported`
- `ALSSlotEnable`
- `alsCalibrationResverveBytes.rapidModeIntegrationTime = %d\n`
- `alsCalibrationDataWords13_17.ch1HighBacklightLeakageCounts = %d\n`
- `calibrationFudgeForLux = %d / 1000\n`
- `AppleCT819::probe - ALS_INT is stuck low.. Disabling ALS. result = %x (%s), and isINTasserted= %x \n`
- `AppleCT819::handleStart\n`
- `ALSRawMode`
- `slopes`
- `AppleISL29023::_timerExpired -- couldn't read sensor data. Reason: %s\n`
- `AppleTSL2581::handleStart - integCycles = %ld\n`
- `AppleCT821::_calculateAmbient -- unknown _gainUsedForLuxCurves\n`
- `AppleCT819::probe - Probing hardware failed (%s) \n`
- `AppleCT819::handleStart - Need at least header size bytes. Actual: %d, Expected: %ld\n`
- `ALSSNumRects`
- `ALSSWindowCoefficients`
- `AppleEmbeddedI2CLightSensor::setReportingThresholdPercentage -- Could not power on the sensor error:(%s)\n`
- `ALSCh1Gain`
- `alsCalibrationResverveBytes.gain = %d\n`
- `alsCalibrationDataWords13_17.ch1LowBacklightLeakageCounts = %d\n`
- `ch1GainFactor16X_32X = %lld / 1000\n`
- `ch1Coeff1 = %lld / 1000\n`
- `AppleSPUALSLuxDriver:%s EDT orientation = %d`
- `ERROR: The LSCI5.x calibration key is too small\n`
- `AppleEmbeddedI2CLightSensor::_copyEvent returned error (%s)\n`
- `ch1GainFactor128X = %ld/1000\n`
- `ALS: [AppleTSL2581] setPropertiesGated: _alsRawMode=%ld\n`
- `bCoeff1 = %lld / 1000\n`
- `ch1HighBacklightLeakageCounts = %d\n`
- `ch1GainFactor64X_140X = %lld / 1000\n`
- `FastModeReportInterval`
- `14`
- `calibration`
- `ch0GainFactor2X = %d/1000\n`
- `_blLeakageNits[2] = %ld / 1000 \n`
- `_pickGain`
- `OFF`
- `ch1GainFactor1X_8X = %lld / 1000\n`
- `setPropertiesGated`
- `%s::%s *** Button Pressed ***\n`
- `gainForLuxCurves`
- `alsCalibrationResverveBytes.calibrationFudgeForLux = %d\n`
- `ALS: [AppleCT819] setPropertiesGated: enableTestMode=%d\n`
- `SuperFastModeReportInterval`
- `ALSFastIntegrationTime`
- `%s::%s *** Button Released ***\n`
- `IOHIDALSContinuousMode`
- `ALS: [AppleTSL2581] setPropertiesGated: newGain =%ld\n`
- `ch0HighBacklightLeakageCounts = %d\n`
- `ch0GainFactor4X_8X = %lld / 1000\n`
- `AppleCT819::handleStart -- vers=%d.%d, size=%d, chksum=%d\n`
- `kIOAOPALSAbortCapture recvd, stopping ALS\n`
- `installHomeButtonListener`
- `useAABPlugin`
- `AppleEmbeddedI2CLightSensor::_setProperties - could not merge \n`
- `AppleTSL2561::handleStart - ALS_INT is stuck low.. Disabling ALS. result = %x (%s), and isINTasserted= %x \n`
- `ratioLimits`
- `ch0DarkCounts = %d\n`
- `ALS: [AppleCT819] setPropertiesGated: _alsContinuousMode=%d\n`
- `SlowModeReportInterval`
- `probe`
- `hidMatchingNotification`
- `alsCalibrationDataHeader.minorVers = %d\n`
- `ALSS RECT[%d]: x %d y %d w %d h %d\n`
- `ALSS is not supported, ALS lux values may be incorrect!\n`
- `ALSSRectConfig`
- `AppleEmbeddedI2CLightSensor::%s - Not powered yet or not open yet. Caching properties\n`
- `ch1GainFactor2X = %d/1000\n`
- `fastModeGain = %d\n`
- `_backlightLeakageCh1Slope[1] = %ld / 1000 \n`
- `copyEvent`
- `_copyEvent`
- `Could not obtain ALS placement!\n`
- `wake event`
- `AppleTSL2581::handleStart - gain for luxCurves reg= 0x%lx\n`
- `121111121222121211111112111122222212211111111112222222222222222222222222222222222222222222222222222222122`
- `ALS: [AppleCT821] setPropertiesGated: gain override to %d \n`
- `ALS: [AppleCT819] _setALSReportingInterval: Requested: interval=%d mics, Setting: interval=%d mics\n`
- `IOHIDALSDumpCalibration`
- `alsCalibration`
- `ERROR: The LSCI4.5 calibration key is too small\n`
- `ALSSRGBCoefficients`
- `_backlightLeakageCh0Slope[1] = %ld / 1000 \n`
- `ch1Coeff = %lld / 1000\n`
- `AppleEmbeddedI2CLightSensor`
- `site.AppleEmbeddedI2CLightSensor`
- `AppleTSL2581::probe - ALS_INT is stuck low.. Disabling ALS. result = %x (%s), and isINTasserted= %x \n`
- `ch1GainFactor1X = %d/1000\n`
- `orientation = %d\n`
- `upperRange = %lld / 1000\n`
- `ch1MedBacklightLeakageCounts = %d\n`
- `ch0GainFactor32X_64X = %lld / 1000\n`
- `alsCalibrationDataWords13_17.ch0MedBacklightLeakageCounts = %d\n`
- `ALS: [AppleTSL2581] setPropertiesGated: _alsContinuousMode=%d\n`
- `alsCalibrationHeader.numSensor = %d\n`
- `function-alss`
- `ERROR: The numRegions in LSCI4.x calibration data is too large.`
- `AppleEmbeddedI2CLightSensor::setPropertiesGated: requested ReportInterval=0 turn OFF sensor\n`
- `site.AppleTSL2581`
- `ALS: [AppleTSL2581] setPropertiesGated: enableTestMode=%ld\n`
- `external-scaling-resistor-ohm`
- `ch0Coeff = %lld / 1000\n`
- `AppleSPUALSLuxDriver::%s: ALSCalibrationData with size %d\n`
- `ERROR: The ALS calibration key is too small\n`
- `0`
- `8`
- `AppleCT821::handleStart -- No LUX extrapolation curve information\n`
- `ch1LowBacklightLeakageCounts = %d\n`
- `_backlightLeakageCh1Slope[0] = %ld / 1000 \n`
- `DeviceUsage`
- `numCurves`
- `AppleTSL2581::handleStart - _blLeakageCh1 = %ld\n`
- `ch0GainFactor0 = %lld / 1000\n`
- `ALSOverRideIntegrationTime`
- `PrimaryUsage`
- `%s::%s: ERROR: unable to crete button event interrupt source`
- `ALS: [AppleTSL2561] setPropertiesGated: enableTestMode=%ld\n`
- `ch0GainFactor128X = %ld/1000\n`
- `ch1GainFactor32X = %d/1000\n`
- `Calibration Header -- \n`
- `fastModeIntegrationTime = %d\n`
- `AppleSPUCT836::%s failed with error (%s)\n`
- `15`
- `AppleEmbeddedI2CLightSensor::preEmptiveSensorStartup. Turning on early\n`
- `hidEventPreEmptiveSensorStartupHandler`
- `AppleTSL2581::handleStart -- No LUX extrapolation curve information\n`
- `\nalsCalibratedLuxCurves(divide by 100 to get float value) -`
- `AppleCT821::probe - Probing hardware failed (%s) \n`
- `AppleCT821::readSensorData: gain=%d orientation=%d data0=%u (%u) data1=%u (%u) lux=%u interval=%lld\n`
- `UseAABPlugin`
- `CurrentNits`
- `handleFrameBufferMsg`
- `AppleEmbeddedI2CLightSensor::_updatePowerState: _parentPowered=%d isChipPowered()=%d _suspended=%lu isOpen=%d\n`
- `ch0GainFactor1X = %ld/1000\n`
- `ALSCh0Gain`
- `ChannelOverride`
- `%s: override value %u \n`
- `ALSSRect`
- `AppleSPUHIDDriver`
- `AppleTSL2581::handleStart -- Clipping integration cycles (%ld) to max allowed (%d).. \n`
- `alsCalibrationDataWords13_17.ch0GainFactor8X_16X = %ld/1000\n`
- `12111112122212121111111211112222221221111111111222222`
- `1211111212221212111111121111222222122111111111122222222222222222222222222222222222222222122`
- `kIOAOPALSAbortCapture recvd, resuming ALS in slow mode.......\n`
- `RedCoefficient`
- `5`
- `6`
- `alsCalibrationDataWords13_17.ch0DarkCounts = %d\n`
- `vers = %d\n`
- `_backlightLeakageCh0Offset[0] = %ld / 1000 \n`
- `IOHIDALSOverRideIntegrationTime`
- `numberOfGains=%d \n`
- `AppleTSL2581::handleStart - Too little calibration data. Actual: %d, Expected: %ld\n`
- `12111112122212121111111211111112222221211211222222222221112111121111212221122222`
- `Calibrated`
- `ALSSensorMin`
- `alsCalibrationHeader.calDataOffset = %d\n`
- `AppleCT821::%s gain changed to %d | low threshold(gap): %d(%d%%) | hight threshold(gap): %d(%d%%) \n`
- `ALS: [AppleCT821] setPropertiesGated: high threshold cap set to %d percent \n`
- `AppleCT819::handleStart -- Clipping integration cycles (%d) to max allowed (%d).. \n`
- `%s: ALS Log level = %d\n`
- `LuxOverride`
- `AppleSPUALSLuxDriver: Calibration successfull.`
- `Could not obtain ALS orientation!\n`
- `IOMobileFramebuffer`
- `%s::%s\n`
- `intercepts`
- `\n`
- `site.AppleSPUALSLuxDriver`
- `alsCalibrationDataWords13_17.ch0LowBacklightLeakageCounts = %d\n`
- `alsCalibrationDataWords13_17.ch1GainFactor1X_8X = %ld/1000\n`
- `AppleCT821::handleStart Could not find calibration data for placement: %d, orientation: %d\n`
- `ch1GainFactor4X_8X = %lld / 1000\n`
- `_blLeakageNits[1] = %ld / 1000 \n`
- `ALS: [AppleCT821] setPropertiesGated: enableTestMode=%d\n`
- `Ch0OverrideValue`
- `ERROR: Insufficient calibration key version - %d.%d\n`
- `IOHIDOrientationType`
- `reportEvent`
- `ch0GainFactor1X = %d/1000\n`
- `\n DEPENDENT SETTINGS \n`
- `AppleCT819::Overriding bad fudge factor 0x%X with 1.0 (0xFF)\n`
- `ch1GainFactor128X = %d/1000\n`
- `ALSGainOverride`
- `1211111212221212111111121111111222222121121122222222222111211112111121222112222211212111222222222222222222222222222222222222221221`
- `AODALSMode`
- `alsCalibrationHeader.minorVers = %d\n`
- `4`
- `1211111212221212111111121111222222122111111111122`
- `AppleCT821::probe - ALS_INT is in proper state - result = %x (%s), and isINTasserted= %x \n`
- `ch0GainFactor8X_16X = %lld / 1000\n`
- `ch1GainFactor8X_16X = %lld / 1000\n`
- `AppleCT821::_timerExpired -- couldn't read sensor data. Reason: %s\n`
- `AppleCT819::handleStart - integCycles = %d\n`
- `AppleCT819::_calculateAmbient -- unknown _gainUsedForLuxCurves\n`

**[__TEXT.__os_log]**

- `Failed to create CoreBrightness default log`
