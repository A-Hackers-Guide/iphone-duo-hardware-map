# `com.apple.driver.AppleCS42L79Audio`

- Name: AppleCS42L79Audio
- Version: `1010.2`
- UUID: `E1BE67AB-2CFE-369B-8B68-D906F7C83C61`
- Source version: `1010.2.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0, [`com.apple.driver.AppleCSEmbeddedAudio`](com.apple.driver.AppleCSEmbeddedAudio.md) 1.1, [`com.apple.driver.AppleEmbeddedAudio`](com.apple.driver.AppleEmbeddedAudio.md) 1.1.0, [`com.apple.driver.AppleEmbeddedAudioLibs`](com.apple.driver.AppleEmbeddedAudioLibs.md) 1.0, [`com.apple.driver.AppleIISController`](com.apple.driver.AppleIISController.md) 1.0, [`com.apple.iokit.AppleARMIISAudio`](com.apple.iokit.AppleARMIISAudio.md) 1.0, [`com.apple.iokit.IOAudio2Family`](com.apple.iokit.IOAudio2Family.md) 1.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.5, [`com.apple.iokit.IOMikeyBusFamily`](com.apple.iokit.IOMikeyBusFamily.md) 1.0, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0, [`com.apple.kec.Libm`](com.apple.kec.Libm.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) | `AppleCS42L79Audio` | `audio-control,cs42l79` |

## IOKit personalities (1) [KC]

### AppleCS42L77Audio
- `CFBundleIdentifier`: `com.apple.driver.AppleCS42L79Audio`
- `IOClass`: `AppleCS42L79Audio`
- `IONameMatch`:
  - `audio-control,cs42l79`
- `IOPersonalityPublisher`: `com.apple.driver.AppleCS42L79Audio`
- `IOProviderClass`: `AppleARMIICDevice`


## C++ classes (5) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleCS42L79Audio` | 0x498 | AppleEmbeddedAudio → IOService → IORegistryEntry |
| `CS42L79FlickerBiasRequest` | 0x38 | AppleARMFunction |
| `CS42L79HallRequest` | 0x38 | AppleARMFunction |
| `CS42L79ListeningRequest` | 0x38 | AppleARMFunction |
| `CS42L79StreamingRequest` | 0x38 | AppleARMFunction |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00005370 off=0x004380d0-0x0043d440 addr=0xfffffe000743c0d0-0xfffffe0007441440 r--/r--   __TEXT            
	sz=0x00001fc5 off=0x00438748-0x0043a70d addr=0xfffffe000743c748-0xfffffe000743e70d               __TEXT.__cstring          (CstringLiterals)
	sz=0x00002951 off=0x0043a70d-0x0043d05e addr=0xfffffe000743e70d-0xfffffe000744105e               __TEXT.__os_log           
	sz=0x000003e0 off=0x0043d060-0x0043d440 addr=0xfffffe0007441060-0xfffffe0007441440               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00011364 off=0x01c02190-0x01c134f4 addr=0xfffffe0008c06190-0xfffffe0008c174f4 r-x/r-x   __TEXT_EXEC       
	sz=0x00011054 off=0x01c02190-0x01c131e4 addr=0xfffffe0008c06190-0xfffffe0008c171e4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000310 off=0x01c131e4-0x01c134f4 addr=0xfffffe0008c171e4-0xfffffe0008c174f4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000210 off=0x0493e2e8-0x0493e4f8 addr=0xfffffe000b9422e8-0xfffffe000b9424f8 rw-/rw-   __DATA            
	sz=0x000000d0 off=0x0493e2e8-0x0493e3b8 addr=0xfffffe000b9422e8-0xfffffe000b9423b8               __DATA.__data             
	sz=0x00000140 off=0x00000000-0x00000140 addr=0xfffffe000b9423b8-0xfffffe000b9424f8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001b00 off=0x01076528-0x01078028 addr=0xfffffe000807a528-0xfffffe000807c028 rw-/rw-   __DATA_CONST      
	sz=0x00000028 off=0x01076528-0x01076550 addr=0xfffffe000807a528-0xfffffe000807a550         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000028 off=0x01076550-0x01076578 addr=0xfffffe000807a550-0xfffffe000807a578         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001310 off=0x01076578-0x01077888 addr=0xfffffe000807a578-0xfffffe000807b888         __DATA_CONST.__const            
	sz=0x000005c0 off=0x01077888-0x01077e48 addr=0xfffffe000807b888-0xfffffe000807be48         __DATA_CONST.__kalloc_type      
	sz=0x00000188 off=0x01077e48-0x01077fd0 addr=0xfffffe000807be48-0xfffffe000807bfd0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000058 off=0x01077fd0-0x01078028 addr=0xfffffe000807bfd0-0xfffffe000807c028         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 109 at 0x04ad7ec4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     E1BE67AB-2CFE-369B-8B68-D906F7C83C61
008: LC_SOURCE_VERSION           1010.2.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9e8c0 size=0x210
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleCS42L79Audio`
- `CFBundleIdentifier`: `com.apple.driver.AppleCS42L79Audio`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleCS42L79Audio`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1010.2`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1010.2`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleEmbeddedAudio.kext/PlugIns/AppleCS42L79Audio.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901374768`
- `_PrelinkExecutableRelativePath`: `AppleCS42L79Audio`
- `_PrelinkExecutableSize`: `99300`
- `_PrelinkExecutableSourceAddr`: `-2198901374768`
- `_PrelinkKmodInfo`: `-2198828997912`

## Strings (468) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%s::%s(..) invalidPSClData encountered [errorCode : 0x%x]\n`
- `Failed to setup interrupt handling\n`
- `Hall InRequest %s:%d super::initWithTargetDataAndSymbol failed\n`
- `virtual IOReturn AEA::FakeBusDevice::readReg(UInt32, UInt32 &)`
- `Failed to enable PDM path to speaker ret=0x%x\n`
- `%s::%s:%d mReceiverPDMFunction = NULL\n`
- `Controller`
- `CS42L79 Failed Reset\n\n`
- `NULL`
- `virtual IOReturn AEA::ARMIICDevice::writeMultiple(UInt32, UInt8 *, IOByteCount)`
- `Unsupported Mic Bias:%d\n`
- `disableFlicker failed disableRoute :%x\n`
- `site.Component`
- `site.AppleCS42L79Audio`
- `L79Events`
- `FlickerBiasRequest %s:%d data = NULL\n`
- `Already configured\n`
- `fmic`
- `ASP Unsupported bitsPerChannel:%d\n`
- `11222222`
- `Loading Hall config from EDT failed. Using default value.\n`
- `CS42L79StreamingRequest %s:%d data = NULL\n`
- `L79IntMax`
- `Failed to disable Hall\n`
- `%s(inData=%p, inLength=%u) unexpected running checksum (0x%x)\n`
- `\n`
- `Invalid Rate:%d\n`
- `ASP3/ASP4 not supported on PCMBus1\n`
- `mixer disalbeSoftRamp failed\n`
- `kAudioMessage_MicState`
- `L79Debug`
- `i8@?0`
- `virtual IOReturn AEA::ARMIICDevice::readMultiple(UInt32, UInt8 *, IOByteCount)`
- `EQ1 Unable to set EQ B SRC on Bus2\n`
- `device-Model`
- `int-id`
- `ASP1/ASP2 not supported on PCMBus2\n`
- `CS42L79ListeningRequest`
- `EQ2 Unable to set EQ B SRC on Bus1\n`
- `adc-gains`
- `CS42L79StreamingRequest`
- `disableFlicker failed disableBclkFsync :%x\n`
- `Failed to HallStreaming enable:%d client:%#x\n`
- `initWithTargetDataAndSymbol`
- `CS42L79FlickerBiasRequest`
- `11222`
- `mixer Unsupported rate:%x\n`
- `Hall`
- `CodecRegisterStartIndex`
- ` fail`
- `disableTempSensor Failed disablePCMBus :%x\n`
- `EQ2 Unable to set EQ A SRC on Bus2\n`
- `virtual IOReturn AEA::ARMIICDevice::readReg(UInt32, UInt32 &)`
- `virtual IOReturn AEA::FakeBusDevice::writeReg(UInt32, UInt32)`
- `11212`
- `smic`
- `ASP does not support channel:%d\n`
- `112111111221111111123133133133133133133133133132212221212221221222222222222222222221111222111111222222222`
- `invalid channel count\n`
- `site.CS42L79FlickerBiasRequest`
- `121111121222121211212121112111111111211111112111211121111121111112211111111231331331331331331331331331322222211212222222111111111112222212222222222`
- `drv-ctrl`
- `halle-calibration`
- `%s Invalid mSystemStateNotificationService\n`
- `%s(inData=%p, inLength=%u) PSCl version 3,unexpected size [expected=%u]\n`
- `Failed to set blockControlExchange ret:%x\n`
- `CS42L79 Failed handleStart\n\n`
- `FlickerBiasRequest %s:%d Incorrect Signature: Expected=0x%x Received=0x%x pHandle=0x%x\n`
- `Unsupported ADC Ax Gain:%d\n\n`
- `_notifySystemStateBool`
- `CS42L79 Check DEBUG:%x AutoStart\n`
- `%s(inData=%p, inLength=%u) invalid magic key (0x%x) [expected:0x%x]\n`
- `disableFlicker failed CS42L79_GLOBAL_BLOCK_EN1 :%x\n`
- `site.CS42L79HallRequest`
- `Hall InRequest %s:%d No Codec param1=%p _codec=%p\n`
- `Hall InRequest %s:%d _micBiasData = NULL\n`
- `virtual IOReturn AEA::FakeBusDevice::writeMultiple(UInt32, UInt8 *, IOByteCount)`
- `HPMic Failed to disableBclkFsync\n`
- `%s::%s(..) unable to create OSNumber. [selectorIndex=%u]\n`
- `DeviceAttached`
- `%s Register Ranges Not in order previous address:%x current:%#x\n`
- `%s(inData=%p, inLength=%u) PSCl version 2, unexpected size [expected=%u]\n`
- `FlickerBiasRequest %s:%d Invalid parameters param1=%p param2:%p _codec=%p\n`
- `CodecRegisterDisplayBase`
- `Failed setMCLKEnabled(false)\n`
- `Failed to enable PLL\n`
- `Failed to setVoltage mic:%d\n`
- `virtual IOReturn AEA::FakeBusDevice::readMultiple(UInt32, UInt8 *, IOByteCount)`
- `Secondary Found LPMic:%d Flicker:%d Hall:%d Receiver:%d\n`
- `getHallConfig`
- `_waitForEQInit`
- `CS42L79StreamingRequest %s:%d super::initWithTargetDataAndSymbol failed\n`
- `CS42L79StreamingRequest %s:%d Invalid parameters param1=%p param2:%p _codec=%p\n`
- `EQ enabled without being configured\n`
- `TempSensor`
- `int-offset`
- `unmuted`
- `Failed setMCLKEnabled(true)\n`
- `ASP3/ASP4 not supported as INTP source\n`
- `EQ2 Unable to set EQ A SRC on Bus1\n`
- `CS42L79 Not Available\n`
- `getPSClVersion`
- `Failed to disable PDM path to speaker ret=0x%x\n`
- `CS42L79StreamingRequest %s:%d _codec = NULL\n`
- `disableFlicker failed setPCMSource :%x\n`
- `Hall InRequest %s:%d Incorrect Signature: Expected=0x%x Received=0x%x pHandle=0x%x\n`
- `%s::%s [%u] unable to StateNotificationItemCreate for Mic\n`
- `%s-mic`
- `%s:%s ioControlList is passed as nullptr.\n`
- `ListeningRequest %s:%d data = NULL\n`
- `imic`
- `%s::%s provider=%s super:start failed.\n`
- `disableHall Failed CS42L79_GLOBAL_BLOCK_EN1 :%x\n`
- `AOP`
- `Asp.cpp`
- `Failed to setPCMSource mic:%d\n`
- `Unsupport ADC gain entry:%d\n\n`
- `Failed ASP->disableRoute\n`
- `device-UID`
- `%s::%s [%u] unable to StateNotificationItemCreate for Receiver\n`
- `_setupInterrupt`
- `Mixer Unsupported samplerate:%d\n`
- `CS42L79: %s:%d timed out waiting for EQ Init\n`
- `%s::%s [%u] unable to CopySystemStateNotificationService\n`
- `Not enough memory\n`
- `getSelectorControlMap`
- `site.CS42L79StreamingRequest`
- `1211111`
- `PCMBus2 does not support source:%x\n`
- `virtual IOReturn AEA::ARMIICDevice::writeReg(UInt32, UInt32)`
- `AppleCS42L79Audio`
- `listening-mic-mask`
- `%s(inData=%p, inLength=%u) unexpected PSCl version (%u) encountered.\n`
- `mixer Unsupported volume:%x\n`
- `Failed to disableADCC mic:%d\n`
- `Unsupported samplerate:%d for Interpolator\n`
- `ListeningRequest %s:%d Incorrect Signature: Expected=0x%x Received=0x%x pHandle=0x%x\n`
- `kAudioMessage_ReceiverOn`
- `/Library/Caches/com.apple.xbs/7374CF14-96FD-494A-A9F3-D02707F144CC/TemporaryDirectory.6UQLML/Sources/AppleEmbeddedAudio/CS42L79/AppleCS42L79Audio.cpp`
- `Invalid ASP Intance:%d\n`
- `\"Bclk/Fsync calculations are bad inRate:%d FsyncNM:%d:%d BclkNM:%d:%d\" @%s:%d`
- `Failed to disableADCA mic:%d\n`
- `ListeningRequest %s:%d _codec = NULL\n`
- `ASPx`
- `Interrupt Storm detected, disabling interrupts\n`
- `1122`
- `Flicker`
- `Target`
- `Failed setClockMode:%d ret:%x\n`
- `Hall InRequest %s:%d _codec = NULL\n`
- `function-pdm_rx_control`
- `Skip turning off MClk Source\n`
- `CS42L79HallRequest`
- `EQ1 Unable to set EQ A SRC on Bus1\n`
- `null route config\n`
- `1222221231331331331331331331331331111222222`
- `%s failed to read:%x result=%#x\n`
- `%s failed address:%08x size:%d result=%#x\n`
- `kAudioMessage_ReceiverState`
- `kAudioMessage_MicOn`
- `Receiver`
- `updatePropertyControlsForSecondary`
- `disableHall Failed disablePCMBus :%x\n`
- `%s Invalid address:%08x size:%d result=%#x\n`
- `%s(inData=%p, inLength=%u) PSCl version %d,unexpected size [expected=%u]\n`
- `disableFlicker failed disablePCMBus :%x\n`
- `Invalid LPMic Listening mask:%x\n\n`
- `MClk Error client:%x already disabled mask:%x\n`
- `%s(inData=%p, inLength=%u) PSCl version 4,unexpected size [expected=%u]\n`
- `%s I2C failed to read:%x err:%x\n\n`
- `\"ASP BCLK already disabled\" @%s:%d`
- `disableTempSensor Failed disableBclkFsync :%x\n`
- `Failed to find EDT property:%s\n`
- `muted`
- `%s(inData=%p, inLength=%d) inData can't be nullptr\n`
- `ASP Unsupported samplerate:%d\n`
- `FlickerBiasRequest %s:%d super::initWithTargetDataAndSymbol failed\n`
- `start`
- `Unsupported GP Bias:%d\n`
- `Unsupported ASP:%d for receiverRoute\n`
- `ListeningRequest %s:%d Invalid parameters param1=%p param2:%p _codec=%p\n`
- `%s Invalid address:%x result=%#x\n`
- `%s failed to find address:%x result=%#x\n`
- `MClk Error client:%x already enabled mask:%x\n`
- `CS42L79 Failed Ping\n\n`
- `CS42L79StreamingRequest %s:%d Incorrect Signature: Expected=0x%x Received=0x%x pHandle=0x%x\n`
- `disableTempSensor Failed CS42L79_GLOBAL_BLOCK_EN1 :%x\n`
- `ListeningRequest %s:%d super::initWithTargetDataAndSymbol failed\n`
- `EQ Unsupported samplerate:%d\n`
- `lmic`
- `success`
- `%s::%s(%s@%p) _interruptEventSource == NULL\n`
- `CS42L79.cpp`
- `site.ARMIICDevice`
- `site.Controller`
- `validatePSClData`
- `Unsupported ADC Cx Gain:%d\n\n`
- `disableTempSensor Failed disableRoute :%x\n`
- `function-aop_lpmic`
- `flicker-config`
- `callFunction`
- `EQ1 Unable to set EQ B SRC on Bus1\n`
- `IOReturn AEA::FakeBusDevice::getRegisterBufferOffset(UInt32, UInt32 &)`
- `initReceiverPDMFunction`
- `\"FAILED disableADCA(%d, %d) when already disabled. Count:%d\" @%s:%d`
- `LPMic Failed to disableBclkFsync\n`
- `EQ2 Unable to set EQ B SRC on Bus2\n`
- `CS42L79:%s:%d Maybe took too long. tries=%d\n\n`
- `mixer Unsupported volume:%x:%x\n`
- `%s bad inAddr:%x offset:%x result=%#x\n`
- `FlickerBiasRequest %s:%d _codec = NULL\n`
- `LPMic`
- `%s::%s(..) unable to find syscfg/PSCl [errorCode: 0x%x]\n`
- `Unsupported ADC Bx Gain:%d\n\n`
- `disableFlickerBias failed setVoltage :%x\n`
- `site.CS42L79ListeningRequest`
- `EQ1 Unable to set EQ A SRC on Bus2\n`
- `CodecRegisterAddressIncrement`
- `disableHall Failed disableBclkFsync :%x\n`
- `%s failed to write:%x result=%#x\n`
- `HPMic`
- `%s::%s(...) unknown PSCl data structure encountered [PSCl_Version=%d]\n`
- `enableHallStreaming invalid client:%#x\n`
- `PCMBus1 does not support source:%x\n`
- `Failed to setBiquads ret:%x\n`
- `OSObject *AEA::BusDevice::debugCopyRegisters()`
- `112`

**[__TEXT.__os_log]**

- `disableTempSensor Failed disableRoute :%x`
- `Interrupt index:%d count:%d`
- `notifySecondaryAudioEnableGated called when service is not available key:%s`
- `mixer Unsupported volume:%x:%x`
- `%s failed to read:%x result=%#x`
- `%s(inData=%p, inLength=%u) invalid magic key (0x%x) [expected:0x%x]`
- `CS42L79StreamingRequest %s:%d Incorrect Signature: Expected=0x%x Received=0x%x pHandle=0x%x`
- `HPMics already disabled`
- `ListeningRequest %s:%d Incorrect Signature: Expected=0x%x Received=0x%x pHandle=0x%x`
- `Write Adr:%08x Val:%08x`
- `Loading Hall config from EDT failed. Using default value.`
- `Setup listening-mic-mask:%x\n`
- `enableLPMicListening state already set enable:%d`
- `MClk Error client:%x already enabled mask:%x`
- `CS42L79 AutoStart LPMic`
- `EQ2 Unable to set EQ B SRC on Bus1`
- `Setup %s: %x:%x:%x:%x:%x:%x\n`
- `%s::SetMultiControl(%u, %p)`
- `MClk Error client:%x already disabled mask:%x`
- `Set Internal MClk client:%x  mask:%x`
- `Detected Rev:%x`
- `Hall InRequest %s:%d _codec = %p ret = true `
- `CS42L79 Failed handleStart\n`
- `%s::%s [%u] unable to StateNotificationItemCreate for Mic`
- `%s Invalid mSystemStateNotificationService`
- `Failed to setVoltage mic:%d`
- `EQ2 Unable to set EQ A SRC on Bus1`
- `CS42L79: %s:%d timed out waiting for EQ Init`
- `fake TempSensor with Diagnostic Generator`
- `Hall InRequest %s:%d client=%#x Success`
- `Create CS42L79ListeningRequest pHandle:%#x signature:%#x`
- `Unsupported Mic Bias:%d`
- `%s::SetControl(%u, %u)`
- `Failed setMCLKEnabled(false)`
- `%s(inData=%p, inLength=%u) unexpected running checksum (0x%x)`
- `enableFlicker Src:%x Ch:%d`
- `Hall already enabled`
- `disableTempSensor Failed disableBclkFsync :%x`
- `%s::SecondarySetControl(%u, %u)`
- `CS42L79StreamingRequest %s:%d super::initWithTargetDataAndSymbol failed`
- `CS42L79StreamingRequest %s:%d Invalid parameters param1=%p param2:%p _codec=%p`
- `Controller::powerUp()`
- `LPMic Failed to disableBclkFsync`
- `enableFlickerBias inEnable:%d`
- `Failed to enable PDM path to speaker ret=0x%x`
- `%s(inData=%p, inLength=%u) PSCl version %d,unexpected size [expected=%u]`
- `FlickerBiasRequest %s:%d super::initWithTargetDataAndSymbol failed`
- `HPMics already enabled`
- `Failed ASP->disableRoute`
- `EQ2 Unable to set EQ A SRC on Bus2`
- `LPMic Bias discharge mask:%x`
- `disableLPMics Ch:%d Bias:%d`
- `Hall Enable Failed:%x`
- `Enable Mic Mask:%x rate:%d`
- `update route disable start:%d ch:%d `
- `CS42L79 AutoStart Receiver`
- `%s:%s using Fake register device`
- `%s::%s:%d provider=%s`
- `%s::callPlatformFunction(%s, %d, %p, %p, %p, %p)`
- `mixer Unsupported rate:%x`
- `Hall InRequest %s:%d super::initWithTargetDataAndSymbol failed`
- `%s::%s [%u] unable to CopySystemStateNotificationService`
- `Failed to set blockControlExchange ret:%x`
- `CS42L79StreamingRequest Enable=%d Change=%d ret:%x`
- `invalid channel count`
- `Mixer Unsupported samplerate:%d`
- `TempSensor already disabled`
- `Hall InRequest %s:%d No Codec param1=%p _codec=%p`
- `Unsupported samplerate:%d for Interpolator`
- `%s::%s provider=%s super:start failed.`
- `enableSidetone`
- `CS42L79StreamingRequest %s:%d data = NULL`
- `fake Hall with Diagnostic Generator`
- `%s bad inAddr:%x offset:%x result=%#x`
- `Invalid Rate:%d`
- `Disable Route ASP:%d Tx:%d Ch:%d Start:%d`
- `PCMBus2 does not support source:%x`
- `Failed setClockMode:%d ret:%x`
- `TempSensor Enable Failed:%x`
- `ASP3/ASP4 not supported as INTP source`
- `enableAudioOutput set:%d cur:%d available:%d`
- `%s I2C failed to read:%x err:%x\n`
- `Unsupport ADC gain entry:%d\n`
- `+ Hall InRequest %s:%d param1=%p _codec=%p`
- `Unsupported GP Bias:%d`
- `mixer disalbeSoftRamp failed`
- `Unsupported ADC Cx Gain:%d\n`
- `disableSidetone`
- `TempSensor already enabled`
- `Interrupt Storm detected, disabling interrupts`
- `EQ1 Unable to set EQ A SRC on Bus1`
- `Failed to disable PDM path to speaker ret=0x%x`
- `Hall InRequest %s:%d Incorrect Signature: Expected=0x%x Received=0x%x pHandle=0x%x`
- `%s Invalid address:%08x size:%d result=%#x`
- `%s:%s:%d mReceiverPDMFunction=%p`
- `%s(inData=%p, inLength=%u) PSCl version 4,unexpected size [expected=%u]`
- `%s(inData=%p, inLength=%d) inData can't be nullptr`
- `EQ1 Unable to set EQ B SRC on Bus1`
- `Not enough memory`
- `enableHallStreaming inEnable:%d client:%#x mask:%#x->%#x`
- `Setup FlickConfig:%x:%x\n`
- `Enter Sleep with LPMic Streaming so switch to kInternalMclk`
- `blockControlExchange id:%x dir:%d`
- `enableHPMics Src:%x Ch:%d bias:%d`
- `%s::%s:%d provider=%s ret=%s`
- `%s(inData=%p, inLength=%u) unexpected PSCl version (%u) encountered.`
- `Enable Route ASP:%d Tx:%d Ch:%d Start:%d`
- `Setup drv-ctrl:%x\n`
- `Int offset:%d count:%d`
- `Failed to enable PLL`
- `Receiver %s`
- `Invalid ASP Intance:%d`
- `CS42L79 AutoStart Hall`
- `setSidetoneBiquads`
- `%s(inData=%p, inLength=%u) PSCl version 2, unexpected size [expected=%u]`
- `FlickerBiasRequest %s:%d _codec = NULL`
- `disableFlicker failed disableRoute :%x`
- `EQ Unsupported samplerate:%d`
- `%s::%s:%d mReceiverPDMFunction = NULL`
- `Set External MClk client:%x  mask:%x`
- `Already configured`
- `disableFlicker failed setPCMSource :%x`
- `%s::%s(%s@%p) _interruptEventSource == NULL`
- `Enable Receiver Failed :%d :%d :%d :%d :%d :%d :%d :%d :%d ret:%x`
- `disableHPMics Ch:%d bias:%d`
- `enableLPMics Src:%x Ch:%d bias:%d`
- `ListeningRequest %s:%d _codec = NULL`
- `EQ1 Unable to set EQ A SRC on Bus2`
- `Setup %s: %x:%x:%x:%x:%x\n`
- `Failed to find EDT property:%s`
- `Setup Route:%s: %x:%x:%x:%x:%x\n`
- `ASP1/ASP2 not supported on PCMBus2`
- `disableFlickerBias failed setVoltage :%x`
- `%s failed to find address:%x result=%#x`
- `%s::%s [%u] unable to StateNotificationItemCreate for Receiver`
- `Stop\n`
- `enableFlickerBias state already set enable:%d`
- `%s::notifySecondaryActiveChangeGated(%s) enable:%d direction:%x `
- `CS42L79StreamingRequest %s:%d _codec = NULL`
- `Hall already disabled`
- `%s Invalid address:%x result=%#x`
- `Disable Mic Mask:%x`
- `enableLPMicListening inEnable:%d mask:%x`
- `- Hall InRequest %s:%d param1=%p _codec=%p ret=%#x`
- `PCMBus1 does not support source:%x`
- `fake flicker with Diagnostic Generator`
- `Hall InRequest %s:%d _codec = %p`
- `Invalid LPMic Listening mask:%x\n`
- `disableHall Failed disableBclkFsync :%x`
- `ListeningRequest Enable=%d Change=%d ret:%x`
- `messageClients(%#x)`
- `Unsupported ASP:%d for receiverRoute`
- `disableFlicker failed disableBclkFsync :%x`
- `EQ2 Unable to set EQ B SRC on Bus2`
- `Secondary Found LPMic:%d Flicker:%d Hall:%d Receiver:%d`
- `using Debug:%x`
- `Skip turning off MClk Source`
- `ASP:%d is configured in mode:%s`
- `Setup ASP:%d Clocking Bclk:%x:%x Fsync:%x:%x rate:%d`
- `Failed to disableADCA mic:%d`
- `Update route enable start:%d ch:%d `
- `CS42L79 Failed Ping\n`
- `%s:%s ioControlList is passed as nullptr.`
- `HPMic Bias must discharge before being set. Prev:%x`
- `LPMics: already enabled curMask:%x inMask:%x`
- `Failed to disableADCC mic:%d`
- `Hall InRequest::initWithTargetDataAndSymbol _data->_phandle = %#x`
- `CS42L79:%s:%d Maybe took too long. tries=%d\n`
- `CS42L79 Failed Reset\n`
- `Setup Interrupts count:%d %d:%d %d:%d\n`
- `mixer Unsupported volume:%x`
- `Failed to HallStreaming enable:%d client:%#x`
- `Failed setMCLKEnabled(true)`
- `ASP does not support channel:%d`
- `FlickerBiasRequest %s:%d Incorrect Signature: Expected=0x%x Received=0x%x pHandle=0x%x`
- `disableHall Failed disablePCMBus :%x`
- `enableLPMicStreaming inEnable:%d mask:%x`
- `Config for 24MHz MClk`
- `ASP Unsupported bitsPerChannel:%d`
- `Unsupported ADC Ax Gain:%d\n`
- `Hall InRequest::initWithTargetDataAndSymbol _data->_signature = %#x`
- `FlickerBiasRequest Enable=%d ret:%x`
- `CS42L79 AutoStart HPMic`
- `Failed to setup interrupt handling`
- `%s::%s(..) unable to find syscfg/PSCl [errorCode: 0x%x]`
- `LPMics already disabled`
- `Hall InRequest %s:%d _micBiasData = NULL`
- `Failed to setBiquads ret:%x`
- `%s failed address:%08x size:%d result=%#x`
- `Create FlickerBiasRequest pHandle:%#x signature:%#x`
- `getADCGain result:%d adc:%d gain:%x\n`
- `disableFlicker failed disablePCMBus :%x`
- `enableAudioInput state already set enable:%d`
- `null route config`
- `EQ1 Unable to set EQ B SRC on Bus2`
- `FlickerBiasRequest %s:%d Invalid parameters param1=%p param2:%p _codec=%p`
- `ASP Unsupported samplerate:%d`
- `Failed to setPCMSource mic:%d`
- `%s failed to write:%x result=%#x`
- `handleStart\n`
- `%s::%s(...) unknown PSCl data structure encountered [PSCl_Version=%d]`
- `CS42L79 AutoStart Flicker`
- `enableHallStreaming invalid client:%#x`
- `Failed to disable Hall`
- `%s(inData=%p, inLength=%u) PSCl version 3,unexpected size [expected=%u]`
- `fake mics with Diagnostic Generator`
- `ASP3/ASP4 not supported on PCMBus1`
- `getSidetoneBiquads`
- `%s Register Ranges Not in order previous address:%x current:%#x`
- `Setup ADC Gain A:%x:%x:%x:%x B:%x:%x C:%x:%x:%x:%x\n`
- `disableFlicker failed CS42L79_GLOBAL_BLOCK_EN1 :%x`
- `CS42L79 Auto start GPBias`
- `Disable Receiver`
- `disableFlicker Ch:%d`
- `%s::%s(..) invalidPSClData encountered [errorCode : 0x%x]`
- `Enable Receiver`
- `EQ enabled without being configured`
- `enableLPMicStreaming state already set enable:%d`
- `FlickerBiasRequest %s:%d data = NULL`
- `setSidetoneVolumeDB:%d`
- `disableTempSensor Failed CS42L79_GLOBAL_BLOCK_EN1 :%x`
- `disableTempSensor Failed disablePCMBus :%x`
- `ListeningRequest %s:%d Invalid parameters param1=%p param2:%p _codec=%p`
- `%s::%s(..) unable to create OSNumber. [selectorIndex=%u]`
- `Codec has not been enabled for FlickerBias:%d`
- `enableFlicker state already set enable:%d`
- `Create CS42L79StreamingRequest pHandle:%#x signature:%#x`
- `CS42L79 Check DEBUG:%x AutoStart`
- `HPMic Failed to disableBclkFsync`
- `disableHall Failed CS42L79_GLOBAL_BLOCK_EN1 :%x`
- `Hall InRequest %s:%d _codec = NULL`
- `Unsupported ADC Bx Gain:%d\n`
- `LPMics:%x enabled`
- `ListeningRequest %s:%d data = NULL`
- `ListeningRequest %s:%d super::initWithTargetDataAndSymbol failed`
- `Read  Adr:%08x Val:%08x`
- `CS42L79 Not Available`
- `enableAudioOutput state already set enable:%d`
- `MClk Enable:%d client:%x mask:%x`
- `Override rapid interrupt count:%d`
- `MClk Error:%x count:%d`
