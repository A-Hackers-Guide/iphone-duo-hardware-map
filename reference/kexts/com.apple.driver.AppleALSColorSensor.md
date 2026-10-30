# `com.apple.driver.AppleALSColorSensor`

- Name: AppleALSColorSensor
- Version: `1.0.0d1`
- UUID: `389781BB-A643-36AD-BE2A-95AECE9D6A95`
- Source version: `2300.52.5.0.0`
- Depends on: [`com.apple.EXBrightCalibrationConsumer`](com.apple.EXBrightCalibrationConsumer.md) 1.0.0, [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleSPU`](com.apple.driver.AppleSPU.md) 1.0.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.4, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 14.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (11) [KC]

### AppleCT711
- `CFBundleIdentifier`: `com.apple.driver.AppleALSColorSensor`
- `IOClass`: `AppleCT711`
- `IONameMatch`:
  - `als,ct711`
  - `als,tcs3490`
- `IOPersonalityPublisher`: `com.apple.driver.AppleALSColorSensor`
- `IOProviderClass`: `AppleARMIICDevice`

### AppleSPUCT709
- `CFBundleIdentifier`: `com.apple.driver.AppleALSColorSensor`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `4`
    - `DeviceUsagePage`: `65280`
- `IOClass`: `AppleSPUCT709`
- `IOPersonalityPublisher`: `com.apple.driver.AppleALSColorSensor`
- `IOProviderClass`: `IOHIDInterface`

### AppleSPUCT720
- `CFBundleIdentifier`: `com.apple.driver.AppleALSColorSensor`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `4`
    - `DeviceUsagePage`: `65280`
- `IOClass`: `AppleSPUCT720`
- `IOPersonalityPublisher`: `com.apple.driver.AppleALSColorSensor`
- `IOProviderClass`: `IOHIDInterface`

### AppleSPUCT721
- `CFBundleIdentifier`: `com.apple.driver.AppleALSColorSensor`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `4`
    - `DeviceUsagePage`: `65280`
- `IOClass`: `AppleSPUCT721`
- `IOPersonalityPublisher`: `com.apple.driver.AppleALSColorSensor`
- `IOProviderClass`: `IOHIDInterface`

### AppleSPUCT724
- `CFBundleIdentifier`: `com.apple.driver.AppleALSColorSensor`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `4`
    - `DeviceUsagePage`: `65280`
- `IOClass`: `AppleSPUCT724`
- `IOPersonalityPublisher`: `com.apple.driver.AppleALSColorSensor`
- `IOProviderClass`: `IOHIDInterface`

### AppleSPUCT725
- `CFBundleIdentifier`: `com.apple.driver.AppleALSColorSensor`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `4`
    - `DeviceUsagePage`: `65280`
- `IOClass`: `AppleSPUCT725`
- `IOPersonalityPublisher`: `com.apple.driver.AppleALSColorSensor`
- `IOProviderClass`: `IOHIDInterface`

### AppleSPUCT726
- `CFBundleIdentifier`: `com.apple.driver.AppleALSColorSensor`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `4`
    - `DeviceUsagePage`: `65280`
- `IOClass`: `AppleSPUCT726`
- `IOPersonalityPublisher`: `com.apple.driver.AppleALSColorSensor`
- `IOProviderClass`: `IOHIDInterface`

### AppleSPUVD6286
- `CFBundleIdentifier`: `com.apple.driver.AppleALSColorSensor`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `4`
    - `DeviceUsagePage`: `65280`
- `IOClass`: `AppleSPUVD6286`
- `IOPersonalityPublisher`: `com.apple.driver.AppleALSColorSensor`
- `IOProviderClass`: `IOHIDInterface`

### AppleSPUVD6287
- `CFBundleIdentifier`: `com.apple.driver.AppleALSColorSensor`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `4`
    - `DeviceUsagePage`: `65280`
- `IOClass`: `AppleSPUVD6287`
- `IOPersonalityPublisher`: `com.apple.driver.AppleALSColorSensor`
- `IOProviderClass`: `IOHIDInterface`

### AppleSPUVL628
- `CFBundleIdentifier`: `com.apple.driver.AppleALSColorSensor`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `4`
    - `DeviceUsagePage`: `65280`
- `IOClass`: `AppleSPUVL628`
- `IOPersonalityPublisher`: `com.apple.driver.AppleALSColorSensor`
- `IOProviderClass`: `IOHIDInterface`

### AppleTCS3490
- `CFBundleIdentifier`: `com.apple.driver.AppleALSColorSensor`
- `IOClass`: `AppleTCS3490`
- `IONameMatch`:
  - `als,tcs3490`
  - `als,ct709`
- `IOPersonalityPublisher`: `com.apple.driver.AppleALSColorSensor`
- `IOProviderClass`: `AppleARMIICDevice`


## C++ classes (13) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleALSColorSensor` | 0x1c0 | AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleCT711` | 0x16b0 | AppleALSColorSensor → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUALSColorDriver` | 0x310 | AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUCT709` | 0x3a8 | AppleSPUALSColorDriver → AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUCT720` | 0x3a8 | AppleSPUALSColorDriver → AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUCT721` | 0x3f0 | AppleSPUALSColorDriver → AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUCT724` | 0x3f0 | AppleSPUALSColorDriver → AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUCT725` | 0x3f0 | AppleSPUALSColorDriver → AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUCT726` | 0x318 | AppleSPUALSColorDriver → AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUVD6286` | 0x3f8 | AppleSPUALSColorDriver → AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUVD6287` | 0x318 | AppleSPUALSColorDriver → AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSPUVL628` | 0x318 | AppleSPUALSColorDriver → AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleTCS3490` | 0x370 | AppleALSColorSensor → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00005168 off=0x00150110-0x00155278 addr=0xfffffe0007154110-0xfffffe0007159278 r--/r--   __TEXT            
	sz=0x00000148 off=0x00150790-0x001508d8 addr=0xfffffe0007154790-0xfffffe00071548d8               __TEXT.__const            
	sz=0x0000490a off=0x001508d8-0x001551e2 addr=0xfffffe00071548d8-0xfffffe00071591e2               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000096 off=0x001551e2-0x00155278 addr=0xfffffe00071591e2-0xfffffe0007159278               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0001dbfc off=0x0166f050-0x0168cc4c addr=0xfffffe0008673050-0xfffffe0008690c4c r-x/r-x   __TEXT_EXEC       
	sz=0x0001d56c off=0x0166f050-0x0168c5bc addr=0xfffffe0008673050-0xfffffe00086905bc          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000690 off=0x0168c5bc-0x0168cc4c addr=0xfffffe00086905bc-0xfffffe0008690c4c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000003a8 off=0x0492e390-0x0492e738 addr=0xfffffe000b932390-0xfffffe000b932738 rw-/rw-   __DATA            
	sz=0x00000188 off=0x0492e390-0x0492e518 addr=0xfffffe000b932390-0xfffffe000b932518               __DATA.__data             
	sz=0x00000220 off=0x00000000-0x00000220 addr=0xfffffe000b932518-0xfffffe000b932738               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00008030 off=0x00f94ef8-0x00f9cf28 addr=0xfffffe0007f98ef8-0xfffffe0007fa0f28 rw-/rw-   __DATA_CONST      
	sz=0x00000068 off=0x00f94ef8-0x00f94f60 addr=0xfffffe0007f98ef8-0xfffffe0007f98f60         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000068 off=0x00f94f60-0x00f94fc8 addr=0xfffffe0007f98f60-0xfffffe0007f98fc8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000076a8 off=0x00f94fc8-0x00f9c670 addr=0xfffffe0007f98fc8-0xfffffe0007fa0670         __DATA_CONST.__const            
	sz=0x000004c0 off=0x00f9c670-0x00f9cb30 addr=0xfffffe0007fa0670-0xfffffe0007fa0b30         __DATA_CONST.__kalloc_type      
	sz=0x00000348 off=0x00f9cb30-0x00f9ce78 addr=0xfffffe0007fa0b30-0xfffffe0007fa0e78         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000b0 off=0x00f9ce78-0x00f9cf28 addr=0xfffffe0007fa0e78-0xfffffe0007fa0f28         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 232 at 0x04ad1110
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     389781BB-A643-36AD-BE2A-95AECE9D6A95
008: LC_SOURCE_VERSION           2300.52.5.0.0
009: LC_FUNCTION_STARTS          offset=0x004a96748 size=0x340
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleALSColorSensor`
- `CFBundleIdentifier`: `com.apple.driver.AppleALSColorSensor`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleALSColorSensor`
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
- `NSHumanReadableCopyright`: `Copyright © 2014-2018 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0d1`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleALSColorSensor.kext`
- `_PrelinkExecutableLoadAddr`: `-2198904422128`
- `_PrelinkExecutableRelativePath`: `AppleALSColorSensor`
- `_PrelinkExecutableSize`: `176444`
- `_PrelinkExecutableSourceAddr`: `-2198904422128`
- `_PrelinkKmodInfo`: `-2198829063280`

## Strings (451) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `dark counts = %d\n`
- `%s: ExtraSettings\n`
- `%d: Gain[%d->%d] scale factor channel 3: %d/1000 \n`
- `i8@?0`
- `ALSWatchdogCountLog`
- `ExponentModeRescaling`
- `AppleSPUALSColorDriver::%s: HOLD Enable = %d\n`
- `AppleALSColorSensor_c.c`
- `AppleSPUVL628::handleStart\n`
- `^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16`
- `numberOfGains=%d \n`
- `AppleSPUALSColorDriver:%s EDT placement = %d \n`
- `%d: CAL DATA STRUCT SIZE: %lu \n`
- `%d: %s::%s: full saturation, report maximum lux \n`
- `AppleSPUCT724`
- `AppleSPUALSColorDriver:%s AOP orientation (%d) doesn't match with kext Orientation (%d), exiting`
- `setSensorEnabled`
- `%d: %s::%s: high threshold=%d, low threshold=%d \n`
- `12111112122212121111111211111112222221211211222222222221112111121111212212222222222222222222222221`
- `%s: Lux dim threshold value %u/1000 \n`
- `%d: fastModeIntegrationTime = %d\n`
- `IOHIDBacklightLevel`
- `%d: %s::%s: increase integration time (%u -> %u) \n`
- `Channel %d --\n`
- `SupportDynamicGain`
- `IceFish`
- `%d: backlight leakage low counts = %d \n`
- `\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `Cal Data for Sensor --\n`
- `%s::%s - Sensor with orientation %d is calibrated \n`
- `AppleSPUCT724::handleStart`
- `scale factor %d = %d / 1000\n`
- `site.AppleSPUCT725`
- `FoxBat`
- `backlight leakage high counts = %d \n`
- `ALSCalibrationData`
- `%d: %s::%s allAbove=%d, anyBelow=%d, threshold hit=%d, level=%d, max=%d\n`
- `%d: rapidModeIntegrationTime = %d\n`
- `\"TB_ASSERT: \" \"(alsdefines_alsreport__decode(msg, &report) == TB_ERROR_SUCCESS) && \\\"failed to decode type: ALSDefines.ALSReport\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `AppleALSColorSensor::%s: override %s \n`
- `SysConfigCalibration`
- `%s: override lux %s \n`
- `CurrentLux`
- `%s::%s - unexpected algo version \n`
- `AppleSPUVD6287::handleStart\n`
- `AppleSPUALSColorDriver::%s: IOHIDALSRawMode = %d\n`
- `AppleSPUALSColorDriver::%s: SYNC mode = %d\n`
- `AppleALSColorSensor::%s failed to create event\n`
- `AppleSPUCT724::%s: Send calibration data (size = %d) to the AOP driver.\n`
- `\"TB_ASSERT: \" \"(server->setreportinterval != ((void*)0)) && \\\"implementation for setReportInterval is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `slowModeGain = %d\n`
- `site.AppleSPUALSColorDriver`
- `SYNC`
- `Successfully obtained ALS placement=%u and orientation=%u!\n`
- `%s::%s lux=%d ch0=%d ch1=%d ch2=%d ch3=%d ch4=%d ch5=%d CCT=%d gain=%d intTime=%d\n`
- `%d: fastModeGain = %d\n`
- `\"TB_FATAL: \" \"invalid value: unexpected case value, %llx\" @%s:%d`
- `%s driver found\n`
- `%d: %s::%s: enable ASATInt \n`
- `%d: AppleCT711::setPropertiesGated\n`
- `getSensorAnalytics`
- `ALSSuperFastIntegrationTime`
- `occlusionModeIntegrationTime = %d\n`
- `%s::%s: ch5 override set to %d \n`
- `[ALSColorCalibration] Sent color calibration to the AOP driver. Result=%s(code=%d).\n`
- `AppleSPUVD6286: ALS Power Function instantiated!\n`
- `IOHIDALSRawMode`
- `ALSLuxDimThreshold`
- `_setProperties`
- `12111112122212121111111212111212222222222222222222221112222222222222222222222222222222222222222222222222222222`
- `rescaleChannels`
- `Calibration Header -- \n`
- `ChannelRatioMitigation`
- `ExponentMode`
- `CalibrationData`
- `%d: alsCalibrationHeader.majorVers = %d\n`
- `%d: rapidModeGain = %d\n`
- `site.AppleSPUVD6287`
- `Could not register AppleARMFunction; EDT node missing?`
- `AppleSPUALSColorDriver::%s: Sending luxErrorOverride[%s] = %d/65536\n`
- `luxCalculation`
- `FDRCalibration`
- `%s::%s: ch2 override set to %d \n`
- `Icefish driver found\n`
- `VL628`
- `alsCalibrationHeader.version = %d\n`
- `IOHIDALSTestMode`
- `IceFish2`
- `%d: \n`
- `AppleSPUALSColorDriver::%s: Disable luxErrorOverride[%s]\n`
- `OcclusionDetection`
- `AppleSPUCT726::%s\n`
- `updateDynamicIntegrationParameters`
- `ALSFastIntegrationTime`
- `ReadAZOffsets`
- `AppleTCS3490`
- `ALSCalibrationSpectrumToProcess`
- `probe`
- `%d: %s::%s: ch3 override set to %d \n`
- `%d: %s::%s: saturation - cancel integration time boost (%d -> %d us) \n`
- `[%s:%d] getPowerState()=%u powerStateOrdinal=%lu _reportInterval_us=%u\n`
- `%d: Channel %d --\n`
- `VD6287`
- `ALSIntegrationMode`
- `ALSLuxBrightenThreshold`
- `Could not obtain ALS placement!\n`
- `CBALSHistory`
- `site.AppleSPUCT724`
- `FDR`
- `com.apple.CoreBrightness`
- `AppleSPUCT725`
- `chip_id`
- `\"TB_ASSERT: \" \"(calibrationbufferelement__v_decode(msg, &calib) == TB_ERROR_SUCCESS) && \\\"failed to decode type: ALSDefines.CalibrationBufferElement (aka. UInt8)\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `AppleSPUCT725::%s: Send calibration data (size = %d) to the AOP driver.\n`
- `AppleSPUALSColorDriver::%s failed with error (%s)\n`
- `SYNCMode`
- `AppleSPUALSColorDriver::%s: Reload CFSN \n`
- `AppleSPUALSColorDriver`
- `%s: Failed to create interrupt event source!\n`
- `dumpALSCalData`
- `alsCalibration`
- `IOHIDOrientationType`
- `%s::%s: ch0 override set to %d \n`
- `%d: sensorType = %d\n`
- `%d: backlight leakage high counts = %d \n`
- `updateMissingSerial`
- `AppleSPUVD6286:%s: Get CFSN failed`
- `\"TB_FATAL: \" \"invalid result returned from getManifest\" @%s:%d`
- `ALSGain`
- `als-logging`
- `%s::%s: ktrace first sample (0x%X) \n`
- `%d: alsCalibrationHeader.numSensor = %d\n`
- `%d: %s::%s - _alsRawMode=%d\n`
- `site.AppleCT711`
- `AppleSPUALSColorDriver::%s: OcclusionDetection = %d\n`
- `%s::%s: ch1 override set to %d \n`
- `AppleSPUALSColorDriver::%s: Median history size changed to %u \n`
- `Driver %s is using %s to dispatch als events\n`
- `AppleCT711`
- `%d: %s::%s - integCycles=%u (%d) referenceIntegCycles=%u (%d) scaleForIntegrationTime=%d/1000 \n`
- `%d: %s::%s - ch1=%d ch2=%d ch3=%d ch4=%d ch5=%d ch6=%d \n`
- `%d: alsCalibrationHeader.calDataOffset = %d\n`
- `on`
- `polled-mode`
- `Lux coefficients: a1=%d/1000000 a2=%d/1000000 a3=%d/1000000 a4=%d/1000000 a5=%d/1000000 a6=%d/1000000\n`
- `AppleSPUALSColorDriver::%s: copy ALS event with lux = %d/1000\n`
- `%d: alsCalibrationHeader.minorVers = %d\n`
- `%d: Gain[%d->%d] scale factor channel 1: %d/1000 \n`
- `clk-freq-sync`
- `site.AppleALSColorSensor`
- `Channel ratio mitigation = %d.`
- `alsCalibrationHeader.size = %d\n`
- `site.AppleSPUCT726`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS) && \\\"failed to wrap packed buffer\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `Firefish driver found\n`
- `%s: Failed to create command gate!\n`
- `%d: slowModeGain = %d\n`
- `%d: %s::%s: lux=%d R=%d/1000 G=%d/1000 B=%d/1000 C=%d/1000 \n`
- `AppleSPUVL628`
- `AppleSPUALSColorDriver::%s: Invalid luxErrorOverride request\n`
- `AppleSPUCT726::%s: alsreport unmarshal failed (tb_error=%u, size=%zu)\n`
- `ReportInterval`
- `%s: Failed to create timer event source!\n`
- `AppleSPUVD6286 %s: manufacturer %s\n`
- `doSerialUpdate`
- `AppleSPUCT720`
- `disabled`
- `CalibrationResult`
- `v240@?0{alsdefines_alsreport_s=IfQQ{alsdefines_vendordata_s=Q(?={?={alsdefines_vendorvd6286_s=I[5i][5i][5s]fIfIIfI[5I]}}{?={alsdefines_vendormorayfamily_s=QQQQ[5f][5f][5f][5f][5f]IfIIffIIII{f32__opt_s=Bf}SSCCCBBB}}{?={alsdefines_vendormorayfamily_s=QQQQ[5f][5f][5f][5f][5f]IfIIffIIII{f32__opt_s=Bf}SS`
- `I60@?0{alsdefines_alsfrontendbase_getsensoranalytics__result_s=C(?=I{alsdefines_sensoranalyticsreport_s=[6{alsdefines_sensorfault_s=II}]})}8`
- `AppleSPUALSColorDriver::%s Invalid ALS event\n`
- `AppleSPUCT726`
- `TryFDRCalibrationFirst`
- `\"TB_FATAL: \" \"invalid result returned from getSensorAnalytics\" @%s:%d`
- `rapidModeIntegrationTime = %d\n`
- `clk-freq-async`
- `AppleSPUVD6287`
- `%s: invalid input`
- `fastModeGain = %d\n`
- `Ch0OverrideValue`
- `LogLevel`
- `\"TB_FATAL: \" \"invalid tag in '[ALSDefines.ALSCFSNBufferElement (aka. UInt8)]' metadata: 0x%x\" @%s:%d`
- `ALSMedianHistorySize`
- `%s::%s Found device with ID = 0x%x\n`
- `%d: Gain[%d->%d] scale factor G channel: %d/1000 \n`
- `%d: %s::%s: ch1 override set to %d \n`
- `%d: AppleCT711::handleStart -- vers=%d.%d, size=%d, chksum=%d\n`
- `alsCalibrationHeader.calibrationType = %d\n`
- `AppleALSColorSensor`
- `%d: %s::%s: ch2 override set to %d \n`
- `ALSSlowIntegrationTime`
- `luxErrorOffsetOverride`
- `ASYNC`
- `ALSOcclusionIntegrationTime`
- `ColorCalcCalibrated`
- `AppleSPUCT721`
- `%d: %s::%s: integration time change refused - [%d] could cross threshold (%d->%d) \n`
- `Syslog`
- `%s: unexpected size: %d, expected: %ld`
- `FoxBat driver found\n`
- `121111121222121211111112121112122222222222222222222211122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `CCT coefficients: a1=%d/1000000 a2=%d/1000000 a3=%d/1000000 a4=%d/1000000 a5=%d/1000000 a6=%d/1000000\n`
- `Lux coefficients: a1=%d/1000000 a2=%d/1000000 a3=%d/1000000 a4=%d/1000000\n`
- `IOHIDALSDumpCalibration`
- `%d: %s::%s - Disabling the sensor \n`
- `121111121222121211111112111111122222212112112222222222211121111211112122122222222222222222222222212222222222222222222`
- `AppleSPUVL628::%s\n`
- `I72@?0{alsdefines_alscontrol_getmanifest__result_s=C(?=I{alsdefines_alsmanifest_s=II{alscfsnbufferelement_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}I})}8`
- `\"TB_FATAL: \" \"invalid tag in '[ALSDefines.CalibrationBufferElement (aka. UInt8)]' metadata: 0x%x\" @%s:%d`
- `getManifest`
- `121111121222121211111112111111122222212112112222222222211121111211112122122222222222222222222222212222222222222222222222222222`
- `WatchdogCount`
- `%s::%s - channel offset compensation enabled: R=%d/1000 G=%d/1000 B=%d/1000 C=%d/1000`
- `CCT coefficients: a1=%d/1000000 a2=%d/1000000`
- `AppleSPUALSColorDriver::%s: ALSQELogs = %d\n`
- `[ALSColorCalibration] size=%d`
- `AppleSPUVL628::%s: alsreport unmarshal failed (tb_error=%u, size=%zu)\n`
- `%d: %s::%s - result: %s (status=%d) \n`
- `\"TB_ASSERT: \" \"(server->getsensoranalytics != ((void*)0)) && \\\"implementation for getSensorAnalytics is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `UseAABPlugin`
- `ALSSensorMin`
- `Redbird`
- `rapidModeGain = %d\n`
- `site.AppleSPUCT720`
- `121111121222121211111112111111122222212112112222222222211121111211112122122222222222222222222222212`
- `%s::%s lux=%d ch0=%d ch1=%d ch2=%d ch3=%d CCT=%d gain=%d intTime=%d\n`
- `AppleSPUALSColorDriver::%s: ExponentMode = %d\n`
- `%s::%s: ch3 override set to %d \n`
- `AppleALSColorSensor::handleStart entered\n`
- `polled mode`
- `%d: %s::%s - Ch1scale=%d/1000 Ch2scale=%d/1000 Ch3scale=%d/1000 Ch4scale=%d/1000 Ch5scale=%d/1000 Ch6scale=%d/1000 \n`
- `\"TB_ASSERT: \" \"(server->getmanifest != ((void*)0)) && \\\"implementation for getManifest is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `[ALSColorCalibration] unexpected size %lu (expected <=%lu)`
- `\"TB_ASSERT: \" \"(server->setintegrationmode != ((void*)0)) && \\\"implementation for setIntegrationMode is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `tint-time-async`
- `\"TB_ASSERT: \" \"(server->settrustedreportinterval != ((void*)0)) && \\\"implementation for setTrustedReportInterval is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `ALSQELogs`
- `IOHIDPlacementType`
- `%d: Gain[%d->%d] scale factor C channel: %d/1000 \n`
- `%d: %s::%s: read data: R=%d G=%d B=%d C=%d \n`
- `%d: numberOfGains=%d \n`
- `%s: override value %u \n`
- `\"TB_ASSERT: \" \"(server->handlepowerevent != ((void*)0)) && \\\"implementation for handlePowerEvent is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `NumberOfChannels`
- `AppleSPUALSColorDriver::%s: ReadAZOffsets = %d\n`
- `%d: numberOfRegions=%d \n`
- `%d: %s::%s: result: %s (status=%d) \n`
- `ExtraSettings`
- `I12@?0I8`
- `IOHIDALSGain`
- `\n`
- `%s::%s Skip initialization of ALS with orientation %d (%d)\n`
- `Value`
- `CFSN`
- `%016llX`
- `LuxOverride`
- `AppleSPUCT709::%s: Send calibration data (size = %d) to the AOP driver.\n`
- `%d: Gain[%d->%d] scale factor channel 2: %d/1000 \n`
- `\"TB_ASSERT: \" \"(vErr == TB_ERROR_SUCCESS) && \\\"tb_message_subrange failed\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `%s::%s: channel override turned %s \n`
- `setALSReportInterval`
- `%s::%s - probed HW is not CT711 \n`
- `%d: backlight leakage mid counts = %d \n`
- `%d: %s::%s - Enabling sensor with gain %d\n`
- `%s: manufacturer %s\n`
- `%d: %s::%s: gain change refused - [%d] could cross threshold (%d->%d) \n`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `occlusionModeGain = %d\n`
- `AppleALSColorSensor::%s failed with error (%s)\n`
- `%d: orientation = %d\n`
- `reportEvent`
- `%s::%s - Need at least header size bytes. Actual: %d, Expected: %ld\n`
- `I12@?0B8`
- `AODDispatchAllSamples`
- `sync2-lower-freq-range-en`
- `AppleSPUALSColorDriver::%s: SupportDynamicGain = %d\n`
- `AZInterval`
- `%d: scale factor %d = %lld / 1000\n`
- `updateDynamicGainThresholds`
- `%s::%s Found device with ID = 0x%x (CT711 chip) \n`
- `RedBird driver found\n`
- `Ch1OverrideValue`
- `%s::%s - probed HW is not CT709 \n`
- `%s: CalibrationResult %d\n`
- `loadCFSN`
- `%s: Sent calibration data (size = %d) to the AOP driver. Result=%s(code=%d).\n`
- `%d: %s::%s - newGain = 2^%d\n`
- `AppleSPUCT721::%s: Send calibration data (size = %d) to the AOP driver.\n`
- `ALSTestMode`
- `AppleSPUALSColorDriver::%s: ReportInterval = %d\n`
- `AppleSPUCT724::probe`
- `copyEvent`
- `AppleSPUALSColorDriver::%s: ALSCalibrationData with size %d\n`
- `interrupts`
- `%d: Cal Data for Sensor --\n`
- `%d: size = %d\n`
- `_copyEvent`
- `%d: %s::%s: crossed high threshold - gain switched %d->%d \n`
- `%d: %s::%s: spurious interrupt \n`
- `calibrationFudgeForLux = %d / 1000\n`
- `Override`
- `%d: alsCalibrationHeader.size = %d\n`
- `product`
- `\"TB_ASSERT: \" \"(server->setsamplingconfig != ((void*)0)) && \\\"implementation for setSamplingConfig is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `AppleSPUVD6287::%s\n`
- `alsCalibrationHeader.numSensor = %d\n`
- `handleStart`
- `%s: ALS Log level is overridden by boot-arg to %d\n`
- `site.AppleTCS3490`
- `1211111212221212111111121111111222222121121122222222222111211112111121221222222222222222222222222122222222222222222222222222221`
- `\"TB_ASSERT: \" \"(server->isactive != ((void*)0)) && \\\"implementation for isActive is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->setcalibration != ((void*)0)) && \\\"implementation for setCalibration is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `AppleSPUALSColorDriver::%s: Watchdog Count: %u\n`
- `AppleTCS3490 - Probing hardware failed (%s) \n`
- `%s::%s - Could not find calibration data for placement: %d, orientation: %d\n`
- `%d: chip type = %d\n`
- `%d: %s::%s - Enabling sensor with gain %d and integration time %u\n`
- `Foxhound`
- `Foxhound SPU driver found\n`
- `crgb`
- `off`
- `ReloadCFSN`
- `AppleALSColorSensor::%s:: override value: %u \n`
- `%d: %s::%s - setting report interval %u us \n`
- `%d: %s::%s: Rscale=%d/1000 Gscale=%d/1000 Bscale=%d/1000 Cscale=%d/1000 \n`
- `AppleALSColorSensor::setPropertiesGated: requested ReportInterval=0 turn OFF sensor\n`
- `site.AppleSPUCT709`
- `%d: slowModeIntegrationTime = %d\n`
- `\"TB_ASSERT: \" \"(server->setbrightness != ((void*)0)) && \\\"implementation for setBrightness is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `slowModeIntegrationTime = %d\n`
- `default`
- `AppleSPUVD6286 %s: late waking ALS found; populating serial in \"product\"\n`
- `I16@?0^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}8`
- `AppleSPUALSColorDriver::%s: HOLD Delay = %d\n`
- `%s: ALS Log level = %d\n`
- `%d: %s::%s: crossed low threshold - gain switched %d->%d \n`
- `tint-time-sync`
- `Ch5OverrideValue`
- `AppleSPUALSColorDriver:%s EDT orientation = %d \n`
- `freq`
- `%d: channel offset counts = %d/1000 \n`
- `%d:  === Other settings === \n`
- `CalibrationType`
- `AppleSPUVL628 %s: device name %s\n`
- `Failed to get IOInterruptEventSource`
- `AppleCT711 - Probing hardware failed (%s) \n`
- `getPlacement`
- `AppleSPUALSColorDriver:%s AOP placement = %d`
- `ALSRawMode`
- `%s::%s - unsupported calibration version \n`
- `%s: Sent calibration data (size = %d) to the AOP driver.\n`
- `FastModeFilter`
- `AppleSPUALSColorDriver::%s failed to create event\n`
- `%s: Lux brighten threshold value %u/1000 \n`
- `12111112122212121111111212111212222222222222222222221112`
- `%d: Lux coefficients: a1=%d/1000000 a2=%d/1000000 a3=%d/1000000 a4=%d/1000000\n`
- `%d: Gain[%d->%d] scale factor B channel: %d/1000 \n`
- `%d: %s::%s - _alsTestMode=%d\n`
- `%d: %s::%s: increase of integration time refused - [%d] could backfire (%d->%d) \n`
- `mode`
- `site.AppleSPUCT721`
- `%d: Gain[%d->%d] scale factor channel 5: %d/1000 \n`
- `%s::%s lux=%d ch0=%d ch1=%d ch2=%d ch3=%d ch4=%d CCT=%d gain=%d intTime=%d\n`
- `populate-serial`
- `\"TB_FATAL: \" \"invalid error returned from %s\" @%s:%d`
- `Icefish2 driver found\n`
- `channel-ratio-mitigation`
- `AppleSPUCT726::handleStart\n`
- `%d: Calibration Header -- \n`
- `AlgoVersion`
- `AppleSPUVD6287 %s: device name %s\n`
- `I8@?0`
- `AppleSPUALSColorDriver::%s: AODDispatchAllSamples = %d\n`
- `enabled`
- `value`
- `AppleSPUALSColorDriver:%s AOP orientation = %d \n`
- `AppleALSColorSensor::%s: ktrace first sample (0x%X) \n`
- `sync2-1p2v-en`
- `loadCalibrationData`
- `ALSSetProperty`
- `AppleALSColorSensor::setPropertiesGated: state is suspended; setting report interval is discarded\n`
- `%s::%s\n`
- `%d: Gain[%d->%d] scale factor R channel: %d/1000 \n`
- `setPropertiesGated`
- `handleInterrupt`
- `%d: %s::%s: raw readings: Ch0=%d, Ch1=%d, Ch2=%d, Ch3=%d \n`
- `probe-for-hardware`
- `%s::%s - CRITICAL ERROR: attempt to access memory out of bounds - skipping calibration (probably bad calibration)\n`
- `%d: calibrationFudgeForLux = %d / 1000\n`
- `site.AppleSPUVL628`
- `CAL DATA STRUCT SIZE: %lu \n`
- `channel offset counts = %d/1000 \n`
- `AppleSPUALSColorDriver::%s: ExponentModeRescaling = %d\n`
- `Ch3OverrideValue`
- `ChannelOverride`
- `getOrientation`
- `%d: %s::%s: disable ASATInt \n`
- `ALSGainOverride`
- `HOLDDelay`
- `AppleSPUCT724::loadCalibrationData`
- `site.AppleSPUVD6286`
- `AppleSPUCT726 %s: device name %s\n`
- `CT726`
- `AppleSPUCT726::%s: alsreport unmarshal failed (tb_error=%u, size=%u)\n`
- `%s::%s: ch4 override set to %d \n`
- `als_skip_initialization`
- `Could not obtain ALS orientation!\n`
- `%d: Gain[%d->%d] scale factor channel 4: %d/1000 \n`
- `AppleSPUVD6286`
- `%d: placement = %d\n`
- `%d: %s::%s: integCycles=%u referenceIntegCycles=%u scaleForIntegrationTime=%d/1000 \n`
- `AppleSPUCT709`
- `AppleSPUVD6286 %s: Using %s\n`
- `AppleSPUALSColorDriver::%s: IOHIDALSTestMode = %d\n`
- `site.ALSSamplesHistory`
- `ALSSensorMax`
- `%d: %s::%s: rescaled channel values: Ch1=%d, Ch2=%d, Ch3=%d, Ch4=%d, Ch5=%d, Ch6=%d, SF=%d/1000 \n`
- `AppleSPUALSColorDriver::%s: ALSAMUI = %d\n`
- `%s: Support color is %s\n`
- `%d: %s::%s: saturation decrease gain (%d -> %d) \n`
- `fastModeIntegrationTime = %d\n`
- `%d: alsCalibrationHeader.chksum = %d\n`
- `ALSSensorType`
- `ChipType`
- `AODALSMode`
- `AppleSPUALSColorDriver::%s: IOHIDALSGain = %d\n`
- `HOLDEn`
- `Ch2OverrideValue`
- `AppleSPUALSColorDriver:%s: Get CFSN failed \n`
- `AppleSPUVD6287.cpp`
- `AppleSPUALSColorDriver::%s: AZInterval = %d\n`
- `Ch4OverrideValue`
- `%d: dark counts = %d\n`
- `%d: Gain[%d->%d] scale factor channel 6: %d/1000 \n`
- `\"TB_ASSERT: \" \"(server->handlereport != ((void*)0)) && \\\"implementation for handleReport is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_FATAL: \" \"overflow detected when adding\" @%s:%d`
- `\"TB_FATAL: \" \"unrecognized selector: %llu\" @%s:%d`
- `handleInterruptReport`
- `AppleSPUALSColorDriver::%s: ALSIntegrationMode = %d\n`
- `%s::%s - vers=%d.%d, size=%d, chksum=%d algoVersion=%d\n`
- `Calibrated`
- `%d: AppleTCS3490::setPropertiesGated\n`
- `%d: %s::%s: channel override turned %s \n`
- `CCT coefficients: kCCT=%d bCCT=%d\n`
- `alsCalibrationHeader.chipType = %d\n`
- `Syncen`
- `ALSColorCalibration`
- `%d: %s::%s: ch0 override set to %d \n`
- `AppleSPUVL628::%s: alsreport unmarshal failed (tb_error=%u, size=%u)\n`

**[__TEXT.__os_log]**

- `AppleSPUALSColorDriver:handleStart AOP orientation (%d) doesn't match with kext Orientation (%d), exiting`
- `Failed to create CoreBrightness default log`
