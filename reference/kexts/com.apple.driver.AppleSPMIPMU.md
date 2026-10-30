# `com.apple.driver.AppleSPMIPMU`

- Name: AppleSPMIPMU
- Version: `1.0.1`
- UUID: `5CFDA83A-41AA-3237-A952-7382FA8954E0`
- Source version: `1372.40.4.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleDialogPMU`](com.apple.driver.AppleDialogPMU.md) 1.0.0, [`com.apple.driver.AppleEmbeddedTempSensor`](com.apple.driver.AppleEmbeddedTempSensor.md) 1.0.0, [`com.apple.driver.AppleSMC`](com.apple.driver.AppleSMC.md) 1.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.4, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (2) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) | `AppleDialogSPMIPMU` | `pmu,spmi` |
| [`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main/pmu-secondary`](../devicetree/root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main__pmu-secondary.md) | `AppleDialogSPMIPMU` | `pmu,spmi` |

## IOKit personalities (2) [KC]

### PMU
- `CFBundleIdentifier`: `com.apple.driver.AppleSPMIPMU`
- `IOClass`: `AppleDialogSPMIPMU`
- `IOMatchCategory`: `AppleSPMIPMU`
- `IONameMatch`: `pmu,spmi`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPMIPMU`
- `IOPlatformActiveAction`: `3000`
- `IOPlatformQuiesceAction`: `98000`
- `IOPlatformSleepAction`: `400`
- `IOPlatformWakeAction`: `400`
- `IOProviderClass`: `AppleARMSPMIDevice`

### PMURTC
- `CFBundleIdentifier`: `com.apple.driver.AppleSPMIPMU`
- `IOClass`: `AppleDialogSPMIPMURTC`
- `IOMatchCategory`: `AppleSPMIPMURTC`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPMIPMU`
- `IOProviderClass`: `AppleDialogSPMIPMU`


## C++ classes (4) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleDialogSPMIPMU` | 0x1e8 | IOService → IORegistryEntry |
| `AppleDialogSPMIPMUFunction` | 0x38 | AppleARMFunction |
| `AppleDialogSPMIPMUNub` | 0x88 | IOService → IORegistryEntry |
| `AppleDialogSPMIPMURTC` | 0x148 | AppleARMRTC → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000032de off=0x0076fa30-0x00772d0e addr=0xfffffe0007773a30-0xfffffe0007776d0e r--/r--   __TEXT            
	sz=0x00000016 off=0x00770100-0x00770116 addr=0xfffffe0007774100-0xfffffe0007774116               __TEXT.__const            
	sz=0x00002bf8 off=0x00770116-0x00772d0e addr=0xfffffe0007774116-0xfffffe0007776d0e               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x0000cbd8 off=0x026ae7f0-0x026bb3c8 addr=0xfffffe00096b27f0-0xfffffe00096bf3c8 r-x/r-x   __TEXT_EXEC       
	sz=0x0000c708 off=0x026ae7f0-0x026baef8 addr=0xfffffe00096b27f0-0xfffffe00096beef8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000004d0 off=0x026baef8-0x026bb3c8 addr=0xfffffe00096beef8-0xfffffe00096bf3c8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000548 off=0x04997c40-0x04998188 addr=0xfffffe000b99bc40-0xfffffe000b99c188 rw-/rw-   __DATA            
	sz=0x00000320 off=0x04997c40-0x04997f60 addr=0xfffffe000b99bc40-0xfffffe000b99bf60               __DATA.__data             
	sz=0x000000e8 off=0x00000000-0x000000e8 addr=0xfffffe000b99bf60-0xfffffe000b99c048               __DATA.__common           (Zerofill)
	sz=0x00000140 off=0x00000000-0x00000140 addr=0xfffffe000b99c048-0xfffffe000b99c188               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001a78 off=0x01206118-0x01207b90 addr=0xfffffe000820a118-0xfffffe000820bb90 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x01206118-0x01206130 addr=0xfffffe000820a118-0xfffffe000820a130         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x01206130-0x01206148 addr=0xfffffe000820a130-0xfffffe000820a148         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001520 off=0x01206148-0x01207668 addr=0xfffffe000820a148-0xfffffe000820b668         __DATA_CONST.__const            
	sz=0x00000180 off=0x01207668-0x012077e8 addr=0xfffffe000820b668-0xfffffe000820b7e8         __DATA_CONST.__kalloc_type      
	sz=0x00000268 off=0x012077e8-0x01207a50 addr=0xfffffe000820b7e8-0xfffffe000820ba50         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000130 off=0x01207a50-0x01207b80 addr=0xfffffe000820ba50-0xfffffe000820bb80         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000010 off=0x01207b80-0x01207b90 addr=0xfffffe000820bb80-0xfffffe000820bb90         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 192 at 0x04ae5c90
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     5CFDA83A-41AA-3237-A952-7382FA8954E0
008: LC_SOURCE_VERSION           1372.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab1c18 size=0x120
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleSPMIPMU`
- `CFBundleIdentifier`: `com.apple.driver.AppleSPMIPMU`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSPMIPMU`
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
- `OSBundleCompatibleVersion`: `1.0.1`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleSPMIPMU.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898001360`
- `_PrelinkExecutableRelativePath`: `AppleSPMIPMU`
- `_PrelinkExecutableSize`: `73334`
- `_PrelinkExecutableSourceAddr`: `-2198898001360`
- `_PrelinkKmodInfo`: `-2198828630976`

## Strings (381) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `info-pm_setting`
- `lpm3`
- `pmu extshdn\n`
- `SOCD: BASE 0x%04X, COUNT 0x%04X\n`
- `Failed to read info-leg_scrpad\n`
- `info-rtc_alarm_monitor_mask`
- `No change to PM Setting (%02Xh)\n`
- `injection_stage`
- `SOCD: Attempted to read past the end of the storage. Addr: 0x%x, rem. size: %u, req. size: %u\n`
- `%s::%scannot set alarm (%x)\n`
- `_readOff2WakeSource`
- `_hasForceShutdown %u\n`
- `_disableResetIn2`
- `%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 23:20:05 Oct 13 2026\n`
- `nvramReadSI64`
- `Not registering for PM callbacks because _pmSettingBase is NULL\n`
- `updatePMSetting`
- `pmu-rtc-offset-use-nvram`
- `failed to create AppleSMC dictionary\n`
- `Failed to read info-rtc_alarm_monitor_mask\n`
- `programRTCAlarm`
- `function-rtc_write_helper`
- `%s::%sDEBUG: %s:%d %s()\n\n`
- `_interruptAction`
- `PMU-LPM: LPEM control dictionary is uninitialized\n`
- `site.AppleDialogSPMIPMUFunction`
- `callFunction`
- `Read RTC offset from leg_scrpad\n`
- `PMURTCNVRAMHelper`
- `function-suspend_helper`
- `IOPMUSPMITimeoutCount`
- `utc-offset`
- `%s::%s [%02x%02x%02x%02x%02x%02x] offsetTicks=%lld\n`
- `IOPMUBootLPMState`
- `info-has_slpsmc`
- `has-socd-fw-sram`
- `%s::%s%sSupport DISABLE_RESET_IN2\n\n`
- `IOPMUBootLPMFWSCC`
- `IOPMUBootStage`
- `%s::%sPMU-LPM: log save error (%x)\n\n`
- `pmu fault log:%s\n`
- `IOPMUBootLPMCtrl`
- `Primary`
- `pmu-enable-ulpm`
- `Cannot read PM Setting (%Xh)\n`
- `%s::%s cannot update boot state (%x)\n\n`
- `pmu-debug-rtc`
- `IU`
- `nvram_offset_usecs`
- `%s::%sAppleDialogPMU:: No info-has_aapc in EDT\n`
- `_readFaultLog`
- `pmu bootErrorStage=%x\n`
- `pre-standbyok %d, vbus %d\n`
- `TMS0`
- `AppleDialogSPMIPMURTC\"::setCurrentDateTime() should not be called\" @%s:%d`
- `PDD0`
- `failed to create SMC notification type string\n`
- `Sync RTC offset: %lld\n`
- `Updating PM Setting (%02Xh => %02Xh)\n`
- `CAPA`
- `Failed to read info-rtc_alarm_ctrl\n`
- `info-scrpad_lpm_log`
- `standbyok %d\n`
- `Unsupported Clock Offset Count (%hu)\n`
- `AppleDialogSPMIPMUNub`
- `\"SMCFW failed to handle shutdown request\\n\" @%s:%d`
- `AppleEFIDump`
- `1211111212221212112222222211211111122222212111111212222211122`
- `info-fault_name-%d`
- `\"SMCFW failed to handle suspend/lpem request\\n\" @%s:%d`
- `%s::%sDisble RESET_IN2 ([%04Xh] %02Xh): %Xh\n\n`
- `PDDc`
- `12111112122212121211111111122222221112112`
- `is-primary`
- `%s::%s%s:%d %s() _bootKeyBase=%x offset=%x, data=%x count=%d (%x)\n`
- `%s::%sFailed to read RESET_IN2_CFG [%04Xh] (%Xh)\n\n`
- `monotonicclock`
- `monotonicclock_rate_usecs`
- `info-rtc_alarm_offset`
- `info-rtc_irq_mask_offset`
- `Failed to read info-rtc_irq_mask_offset\n`
- `info-ulpm_enable_mask`
- `/Library/Caches/com.apple.xbs/D1D3EE44-E60F-4D19-92CF-26ECE31C940B/TemporaryDirectory.cHA6be/Sources/AppleDialogPMU/SPMI/AppleDialogSPMIPMU.cpp`
- `_exitTestMode`
- `%s::%scannot change interrupt mask (%d)\n`
- `%s::%s now=%x scheduling wakeup at %x rtca=%x prta=%x\n`
- `%s::%svalue=%lld sync=%d success=%d\n`
- `%s::%sdata=%p\n`
- `info-fault_shadow`
- `%s::%s%s() _o2wsBase=%x _o2wsCount=%d (%x)\n`
- `lpm2`
- `rd`
- `system-state-notify`
- `info-rtc_alarm_ctrl`
- `Failed to read info-rtc_alarm_event\n`
- `Failed to read info-rtc_alarm_offset\n`
- `%s::%sAppleDialogPMU:: Enabled AAPC (info-has_aapc in EDT)\n`
- `info-exit_test_mode`
- `_handleSpmiError`
- `AppleDialogPMU::%s Unable to write beyond SRAM size limit\n`
- `lpm1`
- `elapsed time rate`
- `failed to register for SMC notifications\n`
- `Failed to read info-rtc_alarm_mask\n`
- `pmu-spmi-retry`
- `AppleDialogPMU::%s Unable to read beyond SRAM size limit\n`
- `%s::%s%s:%d %s() _faultLogBase=%x _faultLogCount=%d (%x)\n`
- `/chosen`
- `%s::%s new offset=%llx readonly offset=%llx\n`
- `%s::%scannot read offset (%d)\n`
- `RTC count backward detected (%08llXh -> %08llXh), or (%llu us -> %llu us)!\n`
- `scheduleRTCWakeAlarm`
- `function-external_shutdown`
- `function-get_pdod`
- `%s::%sArm of Peripheral MCU Reset failed\n`
- `pmu o2ws:%s (%s)\n`
- `System shutdown complete\n`
- `VOLT`
- `SOCD: Found valid container of size %llu at 0x%x\n`
- `SOCD: Failed to read container data at 0x%x: 0x%x\n`
- `function-arm_peripheral_reset`
- `%s::%srtc_write_helper isLegacy=%d\n`
- `info-scrpad_socd`
- `%s::%sAppleDialogPMU::%s failed: %08x address=%04x data=%p count=%d retry=%d\n`
- `SOCD: Container goes past the end of the storage. Addr: 0x%x, rem. size: %u, req. size: %u\n`
- `AppleDialogSPMIPMURTC`
- `%s::%sAppleDialogPMU:: Enabled SLPSMC (info-has_slpsmc in EDT)\n`
- `AppleDialogPMU::%s Invalid SRAM Registers\n`
- `imgIdx`
- `upo: standbyok=%d\n`
- `%s::%sPMU-LPM: error (%x)\n\n`
- `GGTm`
- `calendar time NVRAM offset`
- `Sync RTC offset ignored: _rtcOffsetReadOnly = 0\n`
- `no-halt_restart`
- `\"AppleDialogPMU::%s Error 0x%x (NAK=%d,Parity=%d,Timeout=%d)\" @%s:%d`
- `IOPMUBootErrorStage`
- `PMU-LPM: log header: %08Xh:%08Xh:%08Xh:%08Xh\n`
- `SOCD: Total duration %llu ns\n`
- `%s::%snumber=%p buffer=%s value=%lld\n`
- `SOCD: Failed to read/invalidate container header at 0x%x: 0x%x\n`
- `calendar time offset`
- `AppleSMC`
- `info-rtc_alarm_mask`
- `AppleDialogPMU::%s Failed to read from _sramAddrBaseReg\n`
- `o2ws_%d`
- `IODTNVRAM`
- `info-clock_offset`
- `%s::%s [%02x%02x%02x%02x][%02x%02x] offsetTicks=%lld\n`
- `%s::%scannot program alarm (%d)\n`
- `IOHibernateState`
- `has-lpem-fw-scc`
- `IOPMUBootReasonLPMSU`
- `lpm0`
- `IOPMUBootErrorClear`
- `ULPM error (%x)\n`
- `Q`
- `%s::%sFailed to read info-rtc_alarm_event_mask, will use 0x1 as default\n`
- `function-get_vbus_detect`
- `%s::%sAppleDialogPMU::%s Error 0x%x (NAK=%d,Parity=%d,Timeout=%d)\n`
- `IOPMUBootSOCD`
- `IONVRAM-FORCESYNCNOW-PROPERTY`
- `IOPMUPrimary`
- `flt_%d`
- `AppleDialogSPMIPMURTC tick read!&&&&&&&\n`
- `%s::%scannot write to offset (%d)\n`
- `initWithProvider`
- `function-panic_reset`
- `info-fault_log`
- `%s::%sPMU-LPM: Unable to write phra LPM log (%x)\n\n`
- `CCCs`
- `_readConfiguration`
- `PMU-LPM: Log data is NOT valid. 0x%x 0x%x\n`
- `22211`
- `pmu-lpem-rev`
- `\"lpmLogDataEntries[] has invalid size\\n\" @%s:%d`
- `%s::%sFailed to exit Test Mode (%Xh)\n\n`
- `pmu-disable-panic`
- `%s::%sAppleDialogPMU:: Enabled MCURST (info-has_mcurst in EDT)\n`
- `IOPMUBootErrorFailCount`
- `IOPMUSPMIParityErrCount`
- `IOPMURequestMCUReset`
- `seaship-su-boot`
- `%s::%sAppleDialogPMU::%s failed: %08x address=%04x data=%02x mask=%02x retry=%d\n`
- `IOPMUBootErrorPanicCount`
- `_enterTestMode`
- `_setClockOffsetTicks`
- `AppleDialogSPMIPMURTC\"::getCurrentDateTime() should not be called\" @%s:%d`
- `AppleDialogSPMIPMURTC.cpp`
- `%s::%sAppleDialogPMU: NewFunction 0x%x\n\n`
- `info-scrpad_lpm_ctrl`
- `AppleDialogPMU::%s Failed to write to _sramAddrBaseReg\n`
- `IOPMUBootAppName`
- `info-o2ws_name-%d`
- `initWithTargetDataAndSymbol`
- `info-rtc`
- `info-rtc_alarm_event_mask`
- `Automatic Restart On Power Connect`
- `IOPMrootDomain`
- `PMU-LPM: ctrl write failed\n`
- `%s::%s upcountTicks=%08llx (%x)\n`
- `Non-primary`
- `Cannot update PM Setting because _pmSettingBase is NULL\n`
- `_readRegs`
- `%s::%sPMU-LPM: get PDOD error (%x)\n\n`
- ` `
- `Failed to read info-rtc\n`
- `%s: late vbus detect. scheduling rtc immediate wake\n`
- `Sync RTC offset to NVRAM: %lld\n`
- `function-external_standby`
- `%s::%sAppleDialogPMU:: info-has_mcurst in EDT but function-arm_peripheral_reset not specified\n`
- `RTC upcountTicks=%08llx, regs=%02x:%02x:%02x:%02x:%02x:%02x (%x)\n`
- `site.PMURTCHelper`
- `%s::%sAppleDialogPMU:: No info-has_slpsmc in EDT\n`
- `_readBootKey`
- `%s::%s%s:%d %s() _updateBootProperties(false) failed (%x)\n`
- `%s::%sPMU-LPM: Unable to write LPM log (%x)\n\n`
- `injection_action`
- `info-rtc_alarm_event`
- `Failed to read info-rtc_alarm_ctrl_en_mask\n`
- `site.PMURTCNVRAMHelper`
- `pmu-debug`
- `info-disable_reset_in2`
- `modReg`
- `AppleDialogPMU::%s Failed to set _sramAddrLoReg\n`
- `PMU-LPM: LPMS cleared\n`
- `IOPMPowerSource`
- `0x%llx`
- `upo-shutdown-delay`
- `%s::%sregisterPMSettingController failed (%d)\n\n`
- `_resetLpemInRestoreMode`
- `PMU-LPM: FWOK=%d FLAGS=0x%x\n`
- `AppleDialogSPMIPMUFunction`
- `CCCn`
- `BTLC`
- `IOPMUBootAAPC`
- `%s::%sFailed to create/initialize LPEM control dictionary\n`
- `PMU-LPM: ctrl read failed\n`
- `\"Failed to read kAppleDialogBootStateOffset\\n\" @%s:%d`
- `%s::handleStart: %s _pmuNub: %p ** stopped (non-primary PMU detected) **\n`
- `function-rtc_read_helper`
- `%s::%sAppleDialogPMU:: No info-has_sysrst in EDT\n`
- `debug`
- `failed to allocate SMC threadcall\n`
- `PMURTCHelper`
- `%s::start: %s _pmuNub: %p ** configuration not found ** built 23:20:06 Oct 13 2026\n`
- `%s::start: %s PMU detected\n`
- `info-has_mcurst`
- `setDebugProperties`
- `upo: wake in %d\n`
- `site.AppleDialogSPMIPMURTC`
- `pmu-rtc-offset-readonly`
- `rtc-offset-use-nvram`
- `%s::start: %s _pmuNub: %p built 23:20:06 Oct 13 2026\n`
- `force-shutdown`
- `registerPMCallback`
- `IOPMUBootErrorAppName`
- `IOPMUBootLPMLog`
- `AppleDialogSPMIPMURTC started!******\n`
- `info-rtc_alarm_ctrl_en_mask`
- `nvramWriteSI64`
- `IOPMUDisableResetIn2`
- `info-id`
- `rtc`
- `_writeRegs`
- `imgIdxFindMy`
- `SOCD: Container size too small. Size: %llu, header size: %u\n`
- `_readCurrentOffsetTicks`
- `site.AppleDialogSPMIPMU`
- `IOPMURequestSystemReset`
- `RootDomain not found\n`
- `%s::%s%sSupport PHRA\n\n`
- `%s::%s(Debug) debug=%d\n`
- `IOPMUBootErrorFaults`
- `STAT`
- `B2CA`
- `pmu-spmi-delay`
- `info-has_aapc`
- `IOPMUBootDebug`
- `\"Failed to write kAppleDialogBootStateOffset\\n\" @%s:%d`
- `AppleDialogSPMIPMU: Unknown UPSI action 0x%llx - ignoring\n`
- `SOCD: Container goes past the end of the storage. Addr: 0x%x, rem. size: %u, req. size: %llu\n`
- `SOCD: Failed to allocate OSData\n`
- `monotonicclock_usecs`
- `copyDebugProperty`
- `info-has_lpem`
- `%s::%sAppleDialogPMU:: Enabled SYSRST (info-has_sysrst in EDT)\n`
- `info-fw-sram`
- `info-off2wake_source`
- `setProperties`
- `IOPMUBootFaultInfo`
- `smc go stdby\n`
- `info-has_aapf`
- `debugWake`
- `%s::%sFailed to enter Test Mode (%Xh)\n\n`
- `%s::%sRegAccess flags %x len %x addr %x data %llx mask %llx\n`
- `B2PD`
- `SOCD: Container size too small. Size: %u, header size: %u\n`
- `%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 23:20:05 Oct 13 2026\n`
- `_readRTCUpcountTicks`
- `lpm4`
- `PMU-LPM: lpms=0x%x lpmi=0x%x lpmi2=0x%x\n`
- `%s::%sAppleDialogPMU:: About to set slp3\n`
- `AppleDialogSPMIPMU: UPSI injecting action 0x%llx at boot stage 0x%x\n`
- `rtc-offset-readonly`
- `%s::%scannot enable alarm (%d)\n`
- `%s::%shit <rdar://problem/31800609> (retries=%d)\n`
- `AppleDialogSPMIPMURTC\"::readRTCUpcountTicks() ret=0x%x\" @%s:%d`
- `Automatic Restart On Power Loss`
- `IOPMUSetBootStagePanicSafe`
- `pmu go hib (0x%x)\n`
- `upo error (%x)\n`
- `_handlePEHaltRestart`
- `\"UPSI test panic in PMU kext at boot stage 0x%x\" @%s:%d`
- `1211112`
- `elapsed time`
- `rootdev`
- `TMSc`
- `SOCD: Failed to read/invalidate container mutexes at 0x%x: 0x%x\n`
- `pmu-debug-wake`
- `_writeBootKey`
- `_shutdownGated`
- `pre-standbyok %d, usb %d\n`
- `%s::%sAppleDialogSPMIPMUFunction has bad format\n`
- `12111112122212121`
- `CCCu`
- `site.AppleDialogSPMIPMUNub`
- `start`
- `callPlatformFunction`
- `info-ulpm_enable_offset`
- `%s::%sAppleDialogPMU:: No info-has_aapf in EDT\n`
- `AppleDialogPMU::%s Failed to set _sramAddrHiReg\n`
- `%s::%s%s:%d %s() _bootKeyBase=%x offset=%d, data=%x count=%d \n`
- `AppleDialogSPMIPMURTC ending!%%%%%%\n`
- `info-has_phra`
- `_writeMem`
- `IOPMUSPMINakCount`
- `upo clear (%x)\n`
- `AppleDialogSPMIPMU: UPSI injection configured - stage=0x%llx, action=0x%llx\n`
- `B2VT`
- `monotoniclock_offset_usecs`
- `%s::%sretry reading RTC (retries=%d)\n`
- `IOPMUBootUPOState`
- `pmu restarting\n`
- `IOPMUBootLPMFWOK`
- `%s::%s Cannot register function parent (%x)\n`
- ` %02hX`
- `\"SMCFW failed to handle restart request\\n\" @%s:%d`
- `211`
- `readRTCUpcountTicksLegacy`
- `%s::%sAppleDialogPMU:: Enabled LPEM\n`
- `info-has_sysrst`
- `%s::%sAppleDialogPMU:: No info-has_mcurst in EDT\n`
- `AppleDialogSPMIPMU.cpp`
- `_readMem`
- `IOPMUBootUPOCounter`
- `PMU-LPM: get log data error\n`
- `IOPMUBootOff2WakeSource`
- `pmu-bringup`
- `%s::%sCannot update PM Setting (%Xh)\n\n`
- `%s::%sAppleDialogPMU:: Enabled AAPF (info-has_aapf in EDT)\n`
- `Not `
- `SOCD: Found valid container of size %u at 0x%x\n`
- `AppleSMC service not found\n`
- `%s::%s%sBoot Reason LPMSU\n\n`
- `%s::%sdiags add=0x%x, size=%d (%x)\n`
- `info-scrpad`
- `\"AppleDialogPMU::%s _socdCount(%d) > _scratchCount(%d)\" @%s:%d`
- `%s::%s smc shutdown failed (%x)\n\n`
- `SOCD: Found valid magic at 0x%x\n`
- `setChargerWakeAlarm`
- `info-leg_scrpad`
- `has-disable_reset_in2`
- `AppleDialogSPMIPMU: pmu offwake\n`
- `AppleDialogSPMIPMU`
- `IOPMUBootSOCDClear`
- `%s::%sAppleDialogPMU:: No LPEM enable in EDT\n`
- `info-enter_test_mode`
- `_writeLpemLogData`
- `\"SMCFW failed to handle system reset request\\n\" @%s:%d`
- `com.apple.System.rtc-offset`
