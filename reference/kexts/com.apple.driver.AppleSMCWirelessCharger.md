# `com.apple.driver.AppleSMCWirelessCharger`

- Name: AppleSMCWirelessCharger
- Version: `1.0.1`
- UUID: `6C2ACC4F-0C48-3317-A536-D6018CCAFFA6`
- Source version: `155.40.5.0.0`
- Depends on: [`com.apple.driver.AppleARMPMU`](com.apple.driver.AppleARMPMU.md) 1.0.0, [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleC26Charger`](com.apple.driver.AppleC26Charger.md) 1.0.1, [`com.apple.driver.AppleEmbeddedTempSensor`](com.apple.driver.AppleEmbeddedTempSensor.md) 1.0.0, [`com.apple.driver.RTBuddy`](com.apple.driver.RTBuddy.md) 1.0.0, [`com.apple.iokit.IOAccessoryManager`](com.apple.iokit.IOAccessoryManager.md) 1.0.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.4, [`com.apple.iokit.IOPortFamily`](com.apple.iokit.IOPortFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) | `AppleSMCWirelessCharger` | `smc-ext-charger` |

## IOKit personalities (1) [KC]

### SMCWirelessCharger
- `CFBundleIdentifier`: `com.apple.driver.AppleSMCWirelessCharger`
- `IOClass`: `AppleSMCWirelessCharger`
- `IONameMatch`:
  - `smc-ext-charger`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSMCWirelessCharger`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleSMCInterface`
- `IOUserClientClass`: `AppleSMCWirelessChargerUserClient`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleC26FWLogChannel` | 0x410 | RTBuddyBinaryLogEntryHandler |
| `AppleSMCWirelessCharger` | 0x458 | AppleAirPowerCharger → AppleC26Charger → IOService → IORegistryEntry |
| `AppleSMCWirelessChargerUserClient` | 0xf8 | AppleC26ChargerUserClient → IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1800)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000463c off=0x007662f0-0x0076a92c addr=0xfffffe000776a2f0-0xfffffe000776e92c r--/r--   __TEXT            
	sz=0x0000008c off=0x00766a60-0x00766aec addr=0xfffffe000776aa60-0xfffffe000776aaec               __TEXT.__const            
	sz=0x00003850 off=0x00766aec-0x0076a33c addr=0xfffffe000776aaec-0xfffffe000776e33c               __TEXT.__cstring          (CstringLiterals)
	sz=0x000005f0 off=0x0076a33c-0x0076a92c addr=0xfffffe000776e33c-0xfffffe000776e92c               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x000112f8 off=0x0268b610-0x0269c908 addr=0xfffffe000968f610-0xfffffe00096a0908 r-x/r-x   __TEXT_EXEC       
	sz=0x00010d18 off=0x0268b610-0x0269c328 addr=0xfffffe000968f610-0xfffffe00096a0328          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000005e0 off=0x0269c328-0x0269c908 addr=0xfffffe00096a0328-0xfffffe00096a0908          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001ec off=0x04997818-0x04997a04 addr=0xfffffe000b99b818-0xfffffe000b99ba04 rw-/rw-   __DATA            
	sz=0x000000cd off=0x04997818-0x049978e5 addr=0xfffffe000b99b818-0xfffffe000b99b8e5               __DATA.__data             
	sz=0x00000090 off=0x00000000-0x00000090 addr=0xfffffe000b99b8e8-0xfffffe000b99b978               __DATA.__common           (Zerofill)
	sz=0x0000008c off=0x00000000-0x0000008c addr=0xfffffe000b99b978-0xfffffe000b99ba04               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000016c8 off=0x01201508-0x01202bd0 addr=0xfffffe0008205508-0xfffffe0008206bd0 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01201508-0x01201510 addr=0xfffffe0008205508-0xfffffe0008205510         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01201510-0x01201518 addr=0xfffffe0008205510-0xfffffe0008205518         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001050 off=0x01201518-0x01202568 addr=0xfffffe0008205518-0xfffffe0008206568         __DATA_CONST.__const            
	sz=0x000000c0 off=0x01202568-0x01202628 addr=0xfffffe0008206568-0xfffffe0008206628         __DATA_CONST.__kalloc_type      
	sz=0x000001e0 off=0x01202628-0x01202808 addr=0xfffffe0008206628-0xfffffe0008206808         __DATA_CONST.__kalloc_var       
	sz=0x000002f0 off=0x01202808-0x01202af8 addr=0xfffffe0008206808-0xfffffe0008206af8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000d0 off=0x01202af8-0x01202bc8 addr=0xfffffe0008206af8-0xfffffe0008206bc8         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x01202bc8-0x01202bd0 addr=0xfffffe0008206bc8-0xfffffe0008206bd0         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 214 at 0x04ae5620
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     6C2ACC4F-0C48-3317-A536-D6018CCAFFA6
008: LC_SOURCE_VERSION           155.40.5.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab18e0 size=0x140
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleSMCWirelessCharger`
- `CFBundleIdentifier`: `com.apple.driver.AppleSMCWirelessCharger`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSMCWirelessCharger`
- `CFBundleNumericVersion`: `16875520`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.1`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2017 Apple Inc. All rights reserved.`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleSMCWirelessCharger.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898040080`
- `_PrelinkExecutableRelativePath`: `AppleSMCWirelessCharger`
- `_PrelinkExecutableSize`: `94696`
- `_PrelinkExecutableSourceAddr`: `-2198898040080`
- `_PrelinkKmodInfo`: `-2198828632040`

## Strings (470) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `2211`
- `AppleSMCWirelessCharger: successfully registered for audio notifications\n`
- `RTBuddyService`
- `%s::%s:_ppmService=null\n`
- `IOAccessoryManagerInductiveOOBPairingHostInfo`
- `%s::%s:camera driver class name='%s'\n\n`
- `%s::%s:invalid soc value = %d\n`
- `ThermalStatus`
- `on `
- `CRC 159 attempt %d/%d: Fail; computed 0x%x, expected 0x%x; reset Chromite\n`
- `%s::%s:failed to write mailbox\n`
- `/Library/Caches/com.apple.xbs/A89B338A-901F-4901-9BB6-565FF3779AD0/TemporaryDirectory.NfDpto/Sources/AppleC26Charger/AppleSMCWirelessCharger.cpp`
- `%s::%s:%s() buffer invalid\n\n`
- `%s: kInBandCommsStateChange(CommsEventStateChanged) payload=0x%02x\n`
- `%s::%s:kSMCNotifyWirelessLogsAvailable: logs high watermark notification\n\n`
- `ESP: set property %s = [0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x]\n`
- `OTP read : Bad OTP status\n`
- `IOAccessoryManagerInductiveFamilyID`
- `RamID`
- `ChargingEOC`
- `ConnectState`
- `%s::%s:sendPacketGated, stream num %d: Ready to send packet to SMC\n`
- `%s: auth failed, timeout: %d (status 0x%llx)\n`
- `n/a`
- `%s::%s:ackClientBudget failed\n`
- `%s: kInBandCommsStateChange(PtxInfoUpdated) (PTX_INFO_REGION_CODE)\n`
- `%s::%s:getCount() %d %d %d %d\n`
- `%s%02x%s`
- `%s:%s:%d usbSourceType(%d), usbSourceCurrent(%d), UPA(%d)\n`
- `%s::%s:failed to write address %08x and length %08zx to key WADR\n`
- `%s::%s:Not ready to start link info\n`
- `site.AppleC26FWLogChannel`
- `chg-plog-poll-ms`
- `value`
- `checkDockFeatures`
- `bcm59365_otp_lock_burn_to_row : PROG_WORD_FAIL = 1\n`
- `txSetBoost: kHostTxSetBoost failed with ret=0x%x\n`
- `firmwareUpdateBypass`
- `%s::%s:%s:%d %s %llx\n\n`
- `TooHot`
- `%s: failed CPMS client registration\n`
- `chg-pwr-contract`
- `function-dock_wired`
- `%s: Chip Variant %x\n`
- `start`
- `%s::%s:Puck classification: legitmate\n`
- `Failed-Stream`
- `checkLinkInfo`
- `touch-coex-max-throttle-ms`
- `FrontRenoCameraStreaming`
- `%s: kInBandCommsStateChange(PresentDevReady)\n`
- `peripheralLogWorkHandler`
- `%s::%s:DEBUG coil v %d i %d p %d\n`
- `HFPolicy`
- `AppleSMCWirelessCharger: stopping\n`
- `touchCoexThrottleStateMachineSetState`
- `idle_check_status : OTP status: 0x%x\n`
- `%s: kInBandCommsStateChange(ErrorReported) EOP-reason:%02x\n`
- `M`
- `%s::%s:Puck classification: suspected counterfeit\n`
- `Maximum throttle time passed; invoke unthrottle immediately\n`
- `hd-mic-coex`
- `chg-panic-err`
- `chg-dis-ccoex`
- `site.AppleThrottleableClient`
- `%s failed to set SMC WATS key (ret=%d)\n`
- `coexPwrLimitInputChangedGated`
- `BackCameraActive`
- `bcm59365_read_row_check_status : OTP status: 0x%x\n`
- `allow-hf-fod-threshold-q16`
- `%s: received CPMS esp budget: %dmW (requested %d)\n`
- `%s::%s:failed to cast '%s' to OSNumber\n`
- `bcm59365_check_otp_status_write : BCM59365_OTP_OTPSTATUS: 0x%x\n`
- `%s::%s:failed to write WAVC key\n`
- `%s::%s: now: %llu cs: %llu qcast: %llu qcattps: %llu\n`
- `SlotRequest`
- `OpenLoopCharging`
- `supports-hf-touchcoex`
- `DeviceInfoChipVariant`
- `%s::%s:no matchingService for RTBuddy with SMC endpoint\n`
- `%s: inductive rcv CPMS esp budget update: %dmW\n`
- `write32`
- `AppleSMCWirelessCharger: dumping register memory\n`
- `ForeignObjectDetect`
- `resetConnection`
- `%s: failed to read fw mode: ret=0x%x\n`
- `%s::%s:failed to alloc strings\n`
- `%s::%s:failed to read mailbox\n`
- `%s::%s:sendPacketGated, streamNumber %d\n`
- `%s::%s:failed to enter fod\n`
- `%s: link efficiency %u%% below required %u%% for HF; defaulting to LF\n`
- `%s: read SMC key: WASM=%d\n`
- `chg-nfc-power-pause-disable`
- `chg-qipp-1p4`
- `%s::%s:failed to fetch '%s'\n`
- `\"hw error pending: (status 0x%llx) this=0x%llx\" @%s:%d`
- `1222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `OSBoundedPtr.h`
- `has-espresso`
- `chg-c26-debug`
- `mtpUpdate`
- `%s: FFB comms enabled\n`
- `IOAccessoryManagerInductiveOOBPairingAccessoryData`
- `setBudgetToKernelClientFunction`
- `backlight-control`
- `%s::%s:class=%s\n`
- `handlePPMServiceArrivalNotification`
- ` %02x`
- `ESP: smcReadKey(WABO) failed with ret=0x%x\n`
- `ChargingVrect`
- `auth timeout; %llums > %llums; (attached %llus); timeout!\n`
- `chg-esp-dis-coex-mask`
- `chg-fod-req`
- `%s: touch coex begin\n`
- `AppleSMCWirelessCharger::_wirelessDockNotificationCallout: %d\n`
- `%s::%s:failed to allocate log channel class\n`
- `%s: failed to register inductive fw log channel (ret=%d)\n`
- `%s::%s:camera-driver not found in dt\n`
- `%s::%s:fw length invalid\n`
- `BCM59365_RECT_RECTBOOTCTRL: 0x%x\n`
- `%s: failed to read chip id: ret=0x%x\n`
- `ApplePPM`
- `RCAM active: %d -> %d\n`
- `bcm59365_otp_lock_burn_to_row: wrote register=0x%x with value 0x%x\n`
- `CRC 159 attempt %d/%d: Pass; computed 0x%x, expected 0x%x\n`
- `%s::%s:failed to write WASF key\n`
- `bcm59365_read_row_check_status : ECC_DED_FLAG_STATUS = 1`
- `AppleSMCWirelessCharger`
- `chg-dis-wcoex`
- `%s: Chip ID %x\n`
- `%s: peripheral log collection method: %d\n`
- `IOPMPowerSource`
- `%s::%s:unexpected address %08llx from key, expected %08x\n`
- `BCM59365_PWRMANGR_BG_CTRL1: 0x%x\n`
- `%s::%s:updating firmware, otp 0x%x\n`
- `fod-threshold-q16`
- `CurrentCapacity`
- `Failed to reset Chromite via WAFC/Fw_Ctrl_Cmd_Blocking_Fw_Update; ret=0x%x\n`
- `AppleSMCWirelessCharger: dumping exception frame\n`
- `  0x%08x\n`
- `AppleSMCWirelessCharger: region code 0x%x\n`
- `getQippCommsActiveUptimeNs`
- `setConnectionStatusGated`
- `%s::%s:read camera-driver='%s' from dt\n`
- `%s::%s:ppmKernelClient null\n`
- `readExtended`
- `%s::%s:failed to write data\n`
- `%s: kSMCNotifyWirelessFW; fw-mode=%02x\n`
- `TimeToAuth`
- `%s::%s:num msg to be sent %d\n\n`
- `{n:%d s:%d e:%d str:%d}`
- `handlePDMControllerNotification`
- `handleMatchingNotificationCamera`
- `%s: kSMCNotifySharedDeviceDetected\n`
- `sendPacketGated`
- ` | `
- `handlePuckClassification`
- `AdapterAuthClassification`
- `%s::%s:check dummyload\n`
- `readBatteryStatusGated`
- `%s::%s:mtp cal length invalid\n`
- `bcm59365_check_otp_status_read : BCM59365_OTP_OTPSTATUS: 0x%x\n`
- `%s::%s:no RTBuddyService found\n`
- `puck-classifier-thresh`
- `audio-driver`
- `%s::%s:fw base address 0x%x\n`
- `Connected`
- `txSetBoost: error: rsp_error=%d\n`
- `registerWithRTBuddySMCService`
- `fod-threshold`
- `upa-threshold-ma`
- `%s::%s:touchCoexSubstate: (%d)=>(%d)\n`
- `%s::%s:_wiredAttached:%d rcamActive=%d _coexLimitPower=%d coexLimitPower=%d\n`
- `%s::%s:fw ram %d coil %d state %x  version 0x%x\n`
- `has-peripheral-logs`
- `firmwareUpdateSMC`
- `%s: pdmcontrollerService = NULL\n`
- `handleFirmwareErrors`
- `%s::%s:Retrieved %d bytes of logs\n`
- `AppleSMCWirelessCharger: Puck classifier evt %d: %d => %d\n`
- `chg-walm`
- `function-dock_parent`
- `IronmanCharging`
- `handleWiredDockNotification`
- `AppleSMCWirelessCharger: map %d: base 0x%x length 0x%x\n`
- `OpenLoop`
- `DoNothing`
- `getAuthStatus`
- `has-ironman-charging`
- `AppleSMCWirelessCharger::_displayNotificationCallout: %d\n`
- `AppleSMCWirelessCharger::_wiredDockNotificationCallout: %d\n`
- `FrontCameraStreaming`
- `%s::%s:mtp cfg length invalid\n`
- `ThermalEvent`
- `AppleSMCWirelessCharger: too hot !!!\n`
- `ClosedLoopCharging`
- `puck-classifier-enable`
- `%s: rcam-active=%d, soc=%d; ptx-family=%d; SET_CLOAK_COEX=%d\n`
- `%s::%s:cmd %x data %x\n`
- `dataStreamsEnableGated`
- `%s::%s:failed to send fod cmd\n`
- `%s::%s:fod dummyload: %d\n`
- `%s: failed to update thermal profile %d\n`
- `getCameraProperty`
- `%s::%s:presentdev packet=%s\n`
- `ESP: set property %s = (%d) [0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x]\n`
- `BrickID(%d) Contract(%dmA) UPA(%d)`
- `writeFWLogDataToOSLog`
- `bounded_ptr<T>::operator->: Accessing a member through this pointer would access memory outside of the bounds set originally`
- `chg-dis-bbcoex`
- `chg-dis-roleswap`
- `AppleInductive`
- `off`
- `done  sleep for 260ms (txSetBoost done)\n`
- `%s::%s:hw error pending: (status 0x%llx)\n`
- `IOAccessoryManagerInductiveLocalDeviceID`
- `%s:%s:%d ret(%s)\n`
- `AppleH13CamIn`
- `receivePresentDevPacket`
- `ESP: err, received OOBP evt while detached\n`
- `%s: canceling auth\n`
- `%s::%s:failed to set service\n`
- `%s::%s:failed to read result from key WADE for address %08x, %d\n`
- `NegotiatePower`
- `%s: auth already passed\n`
- `\"%s\" @%s:%d`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `%s: failed to read chip variant: ret=0x%x\n`
- `ironmanCameraCloakCoex`
- `%s::%s:failed to write address %016llx to key WADA\n`
- `volatileCal`
- `sendSigMailboxCmdGated`
- `IOAccessoryManagerInductiveRegionCodeData`
- `ESP: smcReadKey(WBOP) failed with ret=0x%x\n`
- `ClosedLoopEntry`
- `site.AppleFastPuckClassifier`
- `%s::%s:property '%s' does not exist\n`
- `mtpSetupAddressFilter`
- `AppleSMCWirelessCharger: dumping global reserve map\n`
- `%s: kInBandCommsStateChange(AttachChange); %s datastreams (active: %d->%d); pend.tx(%d)\n`
- `periphLogs`
- `DeviceInfoRegionCode`
- `Charging`
- `%s::%s:failed to add binary log entry handler\n`
- `handleBacklightUpdate`
- `OTP lock complete\n`
- `%s: comms reset (while attached); data streams will torn down and brought up\n`
- `%s::%s:RetryCount %d sent tx packet via WACT key (smc result = 0x%X)\n`
- `%s: auth still running (status 0x%llx)\n`
- `%s::%s:failed to receive rx packet\n`
- `%s::%s:failed already. aborting\n`
- `chg-mpp`
- `handleMatchingNotificationPDMController`
- `AppleSMCWirelessCharger: failed to register for audio notifications\n`
- `%s: kInBandCommsStateChange(ProvideEntropy) (%02x)\n`
- `%s: kInBandCommsStateChange(PtxInfoUpdated) payload=%02x\n`
- `IOAccessoryManagerInductiveFwMode`
- `SignalStrength`
- `%s::%s:Waiting for auth to pass before starting link info\n`
- `idle_check_status : Command could not complete within 200ms\n`
- `%s::%s:mtp cal file length invalid\n`
- `%s::%s:fw error pending: %x  (status 0x%llx)\n`
- `IOAccessoryManagerInductiveDeviceID`
- `%s:%s (%d)\n`
- `WaitForSlot`
- `IOAccessoryManagerInductiveAuthTimedOut`
- `%s: auth passed: 0x%x\n`
- `extended-otp-cal`
- `%s::%s:failed to write WAFC key\n`
- `readIndMailboxCmdGated`
- `%s: kInBandCommsStateChange(kInBandCommsEventEspressoInfoUpdated) payload=0x%02x\n`
- `%s::%s:Failed to read logs\n`
- `%s: failed link info: %s, RETRY(%d/%d)\n`
- `brightness`
- `sendMailboxCmdGated`
- `sendExtMailboxCmdGated`
- `%s::%s:DEBUG vrect %d pwr %d\n`
- `site.AppleSMCWirelessChargerUserClient`
- `1211111212221212111111111111111`
- `%s: update charging policy %d\n`
- `%s::%s:%d\n`
- `BackCameraStreaming`
- `has-ironman-camera-cloak`
- `%s: kInBandCommsStateChange(Unknown) payload=[0x%02x 0x%02x]\n`
- `%s::%s:Failed to allocate enough memory to read logs\n`
- `LinkInfo`
- `%s::%s:getCount() %d %d %d\n`
- `%s::%s:failed casting to RTBuddyService\n`
- `pmu-debug`
- `chg-dis-tcoex`
- `call bcm59365_otp_lock_burn_to_row: row=%d val=0x%x\n`
- `smcWriteKey(WASM,0x%x) failed with smcKeyStatus=%d`
- `retrievePeripheralLogsGated`
- `ESP: set property %s = %d\n`
- `TimeToLinkInfo`
- `chg-auth-req`
- `chg-espresso-debug`
- `%s: successfully registered inductive fw log channel\n`
- `Camera bitmask: 0x%x -> 0x%x\n`
- `%s::%s:unexpected address %08x from key, expected %08x\n`
- `USBPowerInfo`
- `q`
- `Failed-Dock`
- `\"failed to write WASF key: (filterNonMtpAddresses = 0x%x)\" @%s:%d`
- `%s::%s:failed to read WAVC key\n`
- `Cloaked`
- `%s: Attempted to reset comms while cloaked\n`
- `registerKernelClientToApplePPMFunction`
- `Failed to unthrottle touch coex (ilim): %d\n`
- `%s::%s:failed to find matching PPM service\n`
- `%s::%s:mtp cal sector invalid\n`
- `%s::%s:MTP read verify failed\n`
- `updateFirmwareGated`
- `%s::%s:Failed to get peripheral log metadata: %d\n`
- `IOAccessoryManagerInductiveOOBPairingEarlyInfo`
- `%s: inductive rcv CPMS esp update but no 1s UPO budget\n`
- `LowPowerMode`
- `%s: Failed to get power in regulation %u.%uV; %u.%02uA\n`
- `power-state-notify`
- `chg-disable-comms`
- `AppleSMCWirelessCharger::_audioNotificationCallout: %d\n`
- `%s::%s:_coexLimitPower %d -> %d; notify SMC via WAFC/coexpwrlimit=%d\n`
- `%s::%s:%s:%d failed to write updated entropy to WAUE key: 0x%x\n`
- `resume`
- `%s::%s:Failed to read log metadata\n`
- `PowerTransfer`
- `chg-hold-reset`
- `OTP Write : Bad OTP status\n`
- `%s: comms reset (while detached); do nothing\n`
- `%s: link efficiency %u%%\n`
- `MaxCapacity`
- `txSetBoost: rsp.tx=%d rsp.rx=%d rsp.id=%d rsp.payload[0]=%d\n`
- `handleHardwareErrors`
- `updateDriverEntropy`
- `AuthFodStatus`
- `%s: FOD already passed\n`
- `%s: link reading failed\n`
- `[b:%s, b-sw:%s, b-tele:%s, b-str:%s, fo-str:%s, fi-str:%s]`
- `%s::%s:failed to write key\n`
- `%s::%s:fw crc16 0x%x\n`
- `%s::%s:%s() failed to read PresentDev packet (0x%X)\n\n`
- `ascii`
- `LinkEfficiency`
- `Quiesce`
- ` `
- `supports-hf-charging`
- `SMC`
- `%s::%s:error reading camera-driver property\n`
- `%s: kInBandCommsStateChange(CommsEnabled) (%d)\n`
- `pause`
- `%s: mtype=0x%X, payload=[0x%02x 0x%02x]\n`
- `AppleC26FWLogChannel`
- `%s: touch coex end\n`
- `%s::%s:audio coex: %d, 0x%x\n`
- `Identification`
- `commReceiveData`
- `ESP: smcWriteKey(WBHB) failed with ret=0x%x\n`
- `read32`
- `base64`
- `IOAccessoryManagerInductiveFwVersionData`
- `%s:%s:%d dock not found`
- `BackSuperWideCameraActive`
- `bcm59365_otp_lock_burn_to_row : OTP status: 0x%x\n`
- `%s::%s:data = 0x%x\n`
- `fod-retry`
- `%s::%s:mtp fw length invalid\n`
- `SYSTEM BROWNOUT: 0x%x\n`
- `%s: kSMCNotifyWirelessFW; payload=[%02x %02x] invalid\n`
- `setEspressoPowerBudget`
- `role`
- `registerForPPMArrivalNotification`
- `1211111212221212122122111222122111112121211122222111111111111111111111111111112222222222222222222222222222112211111211121111111111111111121`
- `chg-force-128k`
- `failed to get reference to IOPMPowerSource\n`
- `backlight-detection`
- `checkUnderpoweredAdapter`
- `BackTeleCameraActive`
- `camera-driver`
- `begin sleep for 260ms (txSetBoost done)\n`
- `%s: failed CPMS admission check\n`
- `chg-%s`
- `%s: failed to write to WAEB key for CPMS esp budget\n`
- `%s::%s:_wiredAttached: %d -> %d\n`
- `mtpCfg`
- `%s::%s:Failed to set WACQ value from boot-arg.\n`
- `site.AppleSMCWirelessCharger`
- `chg-panic-disable`
- `IODisplayParameters`
- `%s::%s:'%s' value is not boolean\n`
- `\"fw error pending: %d (status 0x%llx) this=0x%llx\" @%s:%d`
- `ESP: set property %s = (%d) [0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x]\n`
- `%s: holding charger in reset\n`
- `chg-esp-keyfob-risk`
- `12122221111111`
- `Failed to unthrottle touch coex (HF): %d\n`
- `bcm59365_otp_lock_burn_to_row : Command could not complete within 2s\n`
- `%s::%s:MTP multiple read check failed\n`
- `Write OTPWDATA1: 0x%x\n`
- `%s: resetComms blocked — streams active, puck likely not ready for GetString yet\n`
- `chg-qi-cloak`
- `getCameraDriverClassName`
- `has-ironbull-camera-cloak`
- `%s::%s:failed to read result from key WADD for address %08x, %d\n`
- `AppleSMCWirelessCharger.cpp`
- `IOAccessoryManagerInductiveDeviceType`
- `commSendData`
- `%s: WACR (i:%d) failed (ERR); ret=0x%x\n`
- `_cameraState:%s\n`
- `sendCtrlCmdGated`
- `ESP: smcReadKey(WABI) failed with ret=0x%x\n`
- `Configuration`
- `%s: WACR (i:%d) failed; buffer empty\n`
- `PuckClassification`
- `%s: starting link info, fo_limit(%u%%)\n`
- `%s: failed link info: %s\n`
- `ESP: host_bt_addr avail notif [0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x]\n`
- `%s::%s:inductive rcv esp budget %dmW for reason %d\n`
- `_smcNotifyPowerStateCallout`
- `%02x`
- `IOAccessoryManagerInductiveOOBPairingAccessoryInfo`
- `Disconnected`
- `FWStatus`
- `%s: WACR (i:%d) failed (EOS); ret=0x%x\n`
- `ESP: host_bt_addr property rd fail\n`
- `EndPower`
- `%s::%s:failed to send fod exit cmd\n`
- `%s: link efficiency %u%% below required %u%%\n`
- `%s::%s:Failed to remove logs from peripheral\n`
- `IOAccessoryManagerInductiveExtendedID`
- `ESP: err, received OOBP+ evt while detached\n`
- `%s: check auth status\n`
- `%s:%s:%d no stream\n`
- `AppleSMCWirelessCharger: starting\n`
- `bcm59365_read_row_check_status : Command could not complete within 200ms\n`
- `BCM59365_RCO_RCOCTRL2: 0x%x\n`
- `getLinkInfo`
- `AppleSMCWirelessChargerUserClient`

**[__TEXT.__os_log]**

- `%s dlog_addr: %08x, words_to_read: %d, active_buf_words: %d`
- `%s: comms paused; resend data after resume\n`
- `%s: unable to parse received packet\n`
- `%s:unexpected ACK (stream=%02x, seq=%02x)\n`
- `AppleSMCWirelessCharger: comms not ready\n`
- `%s: DLOG throttle disabled`
- `%s: tx msg buffer full! txAckQ:%d txPktQ:%d\n`
- `%s: packet is NULL, cannot send packet to SMC\n`
- `%s:received ACK (stream=%02x, seq=%02x)\n`
- `%s:unexpected sequence number (stream=%02x, seq=%02x)\n`
- `%s: log entry too large (%d bytes)`
- `%s: kInBandCommsStateChange(ReceivedDataReady)\n`
- `%s: no connection; cannot send packet to SMC\n`
- `%s: Received NACK\n`
- `%s: DLOG throttle enabled`
- `%s:successfully sent packet to SMC via WACT; retries-used: %d; %s\n`
- `%s::%s id:%d fw_mode:%d encoding:%s idx:%d max_idx:%d payload:%s\n`
- `%s: not ready to send; fwRunning, state==charging, commsEnabled (%d, %d, %d); _fwConnectState=%02x\n`
- `%s: unable to get serialized packet\n`
- `%s: Disconnect during fod: connectState: %d; connected: %d\n`
- `%s: no ACK for packet %02x after %d attempts\n`
- `%s: rxSequence=%d\n`
- `%s:received NACK (stream=%02x, seq=%02x, code=%02x)\n`
- `%s: reset comms . tx buffer full %d  delta %lld\n`
- `%s:Data sent to SMC: %s\n`
- `%s:data=%s length=%u (type=%u)\n`
- `%s: WACR (i:%d) read %d bytes\n`
- `%s:Data [%s] received from SMC: {n:%d s:%d e:%d str:%d}: %s\n`
- `%s:data=%s length=%lu (type=%u)\n`
- `%s: resetting stream %d sequence state (rxSeq=%d, txSeq=%llu)\n`
- `%s: Tx: not ready to send; _commsDisabled (%d)\n`
- `%s:failed to send packet to SMC via WACT; ret=0x%x; retries-used: %d; %s\n`
- `%s: qipp stream reception error ret(%s)\n`
