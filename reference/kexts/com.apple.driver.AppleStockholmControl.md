# `com.apple.driver.AppleStockholmControl`

- Name: AppleStockholmControl
- Version: `1.0.0`
- UUID: `1028A697-3DA9-3403-8649-3093676BD596`
- Source version: `371.8.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleOnboardSerial`](com.apple.driver.AppleOnboardSerial.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 22.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (4) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/aop-spmi0/stockholm-spmi`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi.md) | `AppleStockholmSPMI` | `nfc,primary,spmi` |
| [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) | `AppleStockholmControl` | `nfc,primary,gpio` |
| [`/arm-io/aop-spmi0/hammerfest-spmi`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi.md) | `AppleStockholmSPMI` | `nfc,secondary,spmi` |
| [`/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi__hammerfest.md) | `AppleStockholmControl` | `nfc,secondary,gpio` |

## IOKit personalities (4) [KC]

### AppleHammerfestControl
- `CFBundleIdentifier`: `com.apple.driver.AppleStockholmControl`
- `IOClass`: `AppleStockholmControl`
- `IOMatchCategory`: `AppleStockholmControl`
- `IONameMatch`: `nfc,secondary,gpio`
- `IOPersonalityPublisher`: `com.apple.driver.AppleStockholmControl`
- `IOProviderClass`: `IOService`
- `IOUserClientClass`: `AppleStockholmControlUserClient`

### AppleHammerfestSPMI
- `CFBundleIdentifier`: `com.apple.driver.AppleStockholmControl`
- `IOClass`: `AppleStockholmSPMI`
- `IOMatchCategory`: `AppleStockholmControl`
- `IONameMatch`: `nfc,secondary,spmi`
- `IOPersonalityPublisher`: `com.apple.driver.AppleStockholmControl`
- `IOProviderClass`: `AppleARMSPMIDevice`

### AppleStockholmControl
- `CFBundleIdentifier`: `com.apple.driver.AppleStockholmControl`
- `IOClass`: `AppleStockholmControl`
- `IOMatchCategory`: `AppleStockholmControl`
- `IONameMatch`: `nfc,primary,gpio`
- `IOPersonalityPublisher`: `com.apple.driver.AppleStockholmControl`
- `IOProviderClass`: `IOService`
- `IOUserClientClass`: `AppleStockholmControlUserClient`

### AppleStockholmSPMI
- `CFBundleIdentifier`: `com.apple.driver.AppleStockholmControl`
- `IOClass`: `AppleStockholmSPMI`
- `IOMatchCategory`: `AppleStockholmControl`
- `IONameMatch`: `nfc,primary,spmi`
- `IOPersonalityPublisher`: `com.apple.driver.AppleStockholmControl`
- `IOProviderClass`: `AppleARMSPMIDevice`


## C++ classes (6) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleStockholmControl` | 0x100 | IOService → IORegistryEntry |
| `AppleStockholmControlConfig` | 0x88 | IOService → IORegistryEntry |
| `AppleStockholmControlUserClient` | 0xe0 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `AppleStockholmDebugDevice` | 0x10 |  |
| `AppleStockholmRingBuffer` | 0x58 |  |
| `AppleStockholmSPMI` | 0x128 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00004e20 off=0x00795750-0x0079a570 addr=0xfffffe0007799750-0xfffffe000779e570 r--/r--   __TEXT            
	sz=0x000047a1 off=0x00795d78-0x0079a519 addr=0xfffffe0007799d78-0xfffffe000779e519               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000050 off=0x0079a520-0x0079a570 addr=0xfffffe000779e520-0xfffffe000779e570               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00014090 off=0x02767130-0x0277b1c0 addr=0xfffffe000976b130-0xfffffe000977f1c0 r-x/r-x   __TEXT_EXEC       
	sz=0x00013b90 off=0x02767130-0x0277acc0 addr=0xfffffe000976b130-0xfffffe000977ecc0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000500 off=0x0277acc0-0x0277b1c0 addr=0xfffffe000977ecc0-0xfffffe000977f1c0          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x0000039e off=0x049a0d38-0x049a10d6 addr=0xfffffe000b9a4d38-0xfffffe000b9a50d6 rw-/rw-   __DATA            
	sz=0x00000219 off=0x049a0d38-0x049a0f51 addr=0xfffffe000b9a4d38-0xfffffe000b9a4f51               __DATA.__data             
	sz=0x0000017e off=0x00000000-0x0000017e addr=0xfffffe000b9a4f58-0xfffffe000b9a50d6               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00002238 off=0x01232070-0x012342a8 addr=0xfffffe0008236070-0xfffffe00082382a8 rw-/rw-   __DATA_CONST      
	sz=0x00000030 off=0x01232070-0x012320a0 addr=0xfffffe0008236070-0xfffffe00082360a0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000030 off=0x012320a0-0x012320d0 addr=0xfffffe00082360a0-0xfffffe00082360d0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001d58 off=0x012320d0-0x01233e28 addr=0xfffffe00082360d0-0xfffffe0008237e28         __DATA_CONST.__const            
	sz=0x00000180 off=0x01233e28-0x01233fa8 addr=0xfffffe0008237e28-0xfffffe0008237fa8         __DATA_CONST.__kalloc_type      
	sz=0x00000280 off=0x01233fa8-0x01234228 addr=0xfffffe0008237fa8-0xfffffe0008238228         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000080 off=0x01234228-0x012342a8 addr=0xfffffe0008238228-0xfffffe00082382a8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 176 at 0x04ae7494
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     1028A697-3DA9-3403-8649-3093676BD596
008: LC_SOURCE_VERSION           371.8.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab33b8 size=0x158
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleStockholmControl`
- `CFBundleGetInfoString`: `Copyright © 2023 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleStockholmControl`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleStockholmControl`
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
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleStockholmControl.kext`
- `_PrelinkExecutableLoadAddr`: `-2198897846448`
- `_PrelinkExecutableRelativePath`: `AppleStockholmControl`
- `_PrelinkExecutableSize`: `111750`
- `_PrelinkExecutableSourceAddr`: `-2198897846448`
- `_PrelinkKmodInfo`: `-2198828593864`

## Strings (465) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `publishBelow`
- `[%llu] ERR: %s::%s:%d failed to start providers start`
- `function-se_boot_measurements`
- `support_icf_download_request`
- `AppleStockholmControlSPMIErrorTimeStamp`
- `Rx: `
- `_dataPushMbuf`
- `_setVirtualGPIOGated`
- `clearDebugRegisterInfo`
- `com.apple.spmi.nfc.hammerfest`
- `disable`
- `[%llu] %s::%s:%d Not resetting SPMI error registers...`
- `_configureHammerfestSPMIGated`
- `[%llu] ERR: %s::%s:%d failed to get matching for %s`
- `setEnable`
- `%s:%d: no ring buffer for %s\n`
- `%s`
- `sleepWakeNotificationGated`
- `[%llu] WARN: %s::%s:%d no more mbufs - waiting..`
- `[%llu] ERR: %s:%d Invalid clear error size %zu`
- `[%llu] ERR: %s::%s:%d No property \"required-gpios\"`
- `%s:%d:Forcing VEN OFF\n`
- `[%llu] WARN: %s::%s:%d could not get interrupt source for MBUF SW events`
- `nfc.log.level`
- `[%llu] %s::%s:%d capacity=%u hWatermark=%u`
- `[%llu] %s::%s:%d coppied %lu bytes  w=%lu r=%lu`
- `[%llu] ERR: %s::%s:%d No property \"%s\"`
- `support_venable`
- `[%llu] %s::%s:%d Boot stop not supported`
- `_spmiErrorInterruptHandler`
- `ERR: %s::%s:%d _rxSPMIData failed for %lu bytes: %x\n`
- `[%llu] ERR: %s::%s:%d support_venable is not defined`
- `AppleStockholmControlSPMIError`
- `[%llu] %s::%s:%d Using UART`
- `%s:%d: %s log is enabled\n`
- `IOPlatformSleepAction`
- `ERR: %s::%s:%d Hammerfest SPMI cannot be configured via itself\n`
- `ERR: %s::%s:%d Error : failed to re-assert enable !\n`
- `setSEBootMeasurements`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `EosB0`
- `ERR: %s:%d Invalid CRC param size %zu\n`
- `[%llu] ERR: %s::%s:%d failed to add commandGate to workLoop: %d`
- `_vGPIOWriteGated`
- `[%llu] ERR: %s::%s:%d Invalid buffer length.`
- `function-batt_vcc_bermuda`
- `%s:%d:Forcing VEN ON\n`
- `WARN: %s::%s:%d Poll on SPMI error overiden\n`
- `[%llu] %s::%s:%d Waiting for BSD`
- `ERR: %s::%s:%d power is off - cannot validate SPMI config!\n`
- `PN600V`
- `[%llu] %s::%s:%d Defaulting NFCC model`
- `[%llu] ERR: %s::%s:%d failed waiting for %s`
- `SPMI`
- `[%llu] ERR: %s::%s:%d Failed to get SPMI config : 0x%x`
- `com.apple.stockholm.kext.entitlement`
- `ERR: %s::%s:%d Invalid NFCC model\n`
- `[%llu] %s:%d Returning follower ID 0x%x`
- `ERR: %s::%s:%d no setStandbyEnable function registered! :-o\n`
- `removeData`
- `ERR: %s::%s:%d Unsupported command: cmd=%lx direction=%x\n`
- `support_wakeup_enable`
- `ERR: %s::%s:%d could not find boot measurement function\n`
- `ERR: %s::%s:%d Attempt to reconfigure Stockholm SPMI - denied!\n`
- `followerID`
- `[%llu] %s::%s:%d `
- `getNfccModel`
- `support_device_wake`
- `nfc.no_errors`
- `AppleStockholmDebugDevice`
- `[%llu] %s::%s:%d Failed to register for interrupt (%d)`
- `12`
- `ERR: %s::%s:%d No property \"%s\"\n`
- `ERR: %s::%s:%d Not enough bytes to store data.\n`
- `bounded_array_ref: Can't construct from a size greater than UINT32_MAX`
- `sendvGPIO`
- `ERR: %s::%s:%d failed to write %lu bytes to SPMI: %x\n`
- `ERR: %s::%s:%d failed to write to SPMI[0x%02X]:0x%02x - 0x%x, %d attempts\n`
- `ERR: %s::%s:%d Resetting SPMI error registers...\n`
- `ERR: %s::%s:%d Property \"required-gpios\" is not of the expected type, it is a %s\n`
- `ERR: %s::%s:%d Failed to enable interrupt\n`
- `NCI hdr: `
- `Unknown`
- `AppleStockholmControlConfig`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `1211111212221212121111111122221221112`
- `enable`
- `_requiresGPIO`
- `ERR: %s:%d Failed to init ring buffer for %u bytes\n`
- `hammerfest.controller`
- `_freeMbufCluster`
- `_setStandbyEnableGated`
- `[%llu] %s::%s:%d opt=%d`
- `[%llu] %s::%s:%d Secure Timer property found`
- `ERR: %s::%s:%d not powered up!\n`
- `[%llu] %s::%s:%d _dataMode=%d _pendingSPMIData=%d`
- `[%llu] ERR: %s::%s:%d Parity status 0 == 0x%02X`
- `ctl_disconnectGated`
- `function-download_request`
- `support_virtual_gpio`
- `AppleHammerfestSPMI`
- `[%llu] %s::%s:%d mbuf_len=%lu`
- `DevWrite: debugLevel=%u`
- `_txSPMIData`
- `[%llu] %s::%s:%d Querying SPMI error registers...`
- `AppleStockholmControlUserClient`
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `nfc.disableentitlements`
- `initWith`
- `resetBuffer`
- `ERR: %s::%s:%d could not enqueue data (%d)\n`
- `ERR: %s::%s:%d Error: boot stop is toggled while disabled !.\n`
- `Error : invalid parameter count : in=%d, out=%d\n`
- `[%llu] ERR: %s::%s:%d Failed to create AppleStockholmControlConfig`
- `ERR: %s::%s:%d %s model is 0x%x\n`
- `[%llu] ERR: %s::%s:%d Error ! Unexpected property type : %s`
- `[%llu] %s::%s:%d SPMI config is correct (followerID: %02x irqOffset: %02x)`
- `ctl_getoptGated`
- `%s:%d error send <loglevel>\n`
- `ERR: %s::%s:%d Property \"%s\" is not of the expected type, it is a %s\n`
- `ERR: %s::%s:%d data ready but unable to send to client - drop\n`
- `ERR: %s::%s:%d buffer overrun!\n`
- `ERR: %s::%s:%d failed to attach AppleStockholmControlConfig\n`
- `ERR: %s::%s:%d failed to write to SPMI[0x%02X]:0x%02x - %02x\n`
- `AppleStockholmControl`
- `[%llu] %s::%s:%d PM Register`
- `function-boot_measurements`
- `ERR: %s::%s:%d Error ! Unexpected property type : %s\n`
- `[%llu] ERR: %s::%s:%d Error registering error interrupt`
- `ERR: %s::%s:%d failed to write data: %x\n`
- `ERR: %s::%s:%d bad argument: len = %lu command len = %lu\n`
- `ERR: %s::%s:%d No property \"required-gpios\"\n`
- `[%llu] ERR: %s::%s:%d could not find wakeup enable function`
- `[%llu] %s::%s:%d PM init`
- `[%llu] %s::%s:%d validating Hammerfest SPMI config...`
- `function-wakeup_enable`
- `[%llu] ERR: %s::%s:%d could not find boot measurement function`
- `ERR: %s::%s:%d failed waiting for %s\n`
- `WARN: %s::%s:%d _hostWakeDelay overiden to %u\n`
- `nfc.pollSPMIOnError`
- `[%llu] %s::%s:%d dataLength=%lu`
- `ERR: %s::%s:%d failed to read %lu bytes from SPMI: %x\n`
- `ERR: %s:%d failed to allocate cluster for %lu bytes; err=%d clSize=%lu\n`
- `WARN: %s::%s:%d Already open!\n`
- `ERR: %s::%s:%d No data in entry\n`
- `[%llu] ERR: %s::%s:%d could not find enable function`
- `_configDebugDevice`
- `%s:%d: no major for %s\n`
- `12212122222`
- `_bootStopInterruptHandler`
- `support_bootstop-interrupts`
- `[%llu] ERR: %s::%s:%d Failed to create interrupt source`
- `_initForPM`
- `nfc.controller`
- `WAKE_IRQ_H`
- `[%llu] ERR: %s::%s:%d _rxSPMIData failed for %lu bytes: %x`
- `[%llu] %s::%s:%d data ready but unable to send to client - enqueuing.`
- `ERR: %s::%s:%d Error status 1 == 0x%02X\n`
- `stockholm-spmi-data-socket`
- `_rxMbufInterruptHandler`
- `ctl_setoptGated`
- `[%llu] ERR: %s::%s:%d failed to attach AppleStockholmControlConfig`
- `ioctl`
- `validateSPMIConfig`
- `bufferDataLength`
- `[%llu] WARN: %s::%s:%d Reconfiguring Hammerfest SPMI...`
- `ERR: %s:%d Invalid clear error size %zu\n`
- `configureHammerfestSPMI`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `WARN: %s::%s:%d originally allocated buffer is too small (%zu). Requesting extra size (%zu, total=%zu) ...\n`
- `primary`
- `getBootStopState`
- `[%llu] ERR: %s::%s:%d No SPMI support! :-o`
- `%s %lu.%03lu `
- `[%llu] ERR: %s::%s:%d No property \"required-functions\"`
- `ERR: %s::%s:%d Parity status 1 == 0x%02X\n`
- `[%llu] %s::%s:%d Halley property detected, halley absent, powering ON and using follower reset`
- `1211111212221212111111111111`
- `[%llu] ERR: %s::%s:%d Could not make kernel control socket for %s: %d`
- `_dataReadMbuf`
- `ctl_connectGated`
- `[%llu] ERR: %s:%d not found!`
- `[%llu] ERR: %s::%s:%d Property \"required-functions\" is not of the expected type, it is a %s`
- `_allocMbuf`
- `[%llu] %s::%s:%d PM Join`
- `[%llu] ERR: %s::%s:%d not a socket client!`
- `ERR: %s::%s:%d Invalid buffer length.\n`
- `[%llu] ERR: %s:%d Invalid On demand param size %zu`
- `nfc.externalLoadSwitchDrain`
- `Serial`
- `[%llu] ERR: %s::%s:%d Error : failed to re-assert enable !`
- `eos-halley-config`
- `[%llu] %s::%s:%d Attaching`
- `[%llu] ERR: %s::%s:%d failed to get commandGate`
- `function-boot_stop_state`
- `[%llu] ERR: %s::%s:%d could not find boot stop function`
- `[%llu] %s::%s:%d Halley property found`
- `[%llu] %s::%s:%d Follower reset requested - resetting crc flag`
- `[%llu] %s::%s:%d vGPIO 0x%02X requested`
- `ERR: %s::%s:%d failed to read SPMI[0x%02X] - %02x\n`
- `[%llu] ERR: %s::%s:%d bad argument: cmd=%lx direction=%x`
- `[%llu] %s::%s:%d SPMI error clear`
- `bounded_ptr<T>::discard_bounds: Discarding the bounds on this pointer would lose the fact that it is outside of the bounds set originally`
- `[%llu] %s::%s:%d No SPMI support`
- `[%llu] %s::%s:%d w=%lu r=%lu`
- `EosB20`
- `com.apple.hammerfest.kext.entitlement`
- `ERR: %s::%s:%d Could not make kernel control socket for %s: %d\n`
- `requestDebugRegisterInfo`
- `ERR: %s::%s:%d failed to write SPMI[0x%02X] - %02x\n`
- `[%llu] %s::%s:%d found SPMI driver %s`
- `ERR: %s::%s:%d could not find device wake function\n`
- `[%llu] ERR: %s::%s:%d failed to write to SPMI[0x%02X]:0x%02x - 0x%x, %d attempts`
- `[%llu] %s::%s:%d SPMI reconfig is not supported on this device`
- `ERR: %s::%s:%d Invalid buffer.\n`
- `[%llu] ERR: %s::%s:%d Error status 1 == 0x%02X`
- `[%llu] ERR: %s::%s:%d could not enqueue data (%d)`
- `[%llu] ERR: %s:%d Failed to init ring buffer for %u bytes`
- `[%llu] %s::%s:%d started stockholm`
- `[%llu] ERR: %s:%d failed to allocate mbuf; err=%d`
- `[%llu] %s::%s:%d second write to SPMI[0x%02X] - %02x`
- `[%llu] %s::%s:%d validating Stockholm SPMI config...`
- `ctl_connect`
- `[%llu] %s::%s:%d w=%lu r=%lu  dataLen=%lu`
- `[%llu] %s::%s:%d reading %lu`
- `[%llu] ERR: %s::%s:%d External load switch drain override set`
- `[%llu] %s::%s:%d PM set state`
- `[%llu] %s::%s:%d data ready - sending to user`
- `[%llu] %s::%s:%d kIOMessageSystemWillSleep`
- `_sendFollowerResetGated`
- `_setDownloadRequestGated`
- `[%llu] ERR: %s::%s:%d failed to write SPMI[0x%02X] - %02x`
- `WARN: %s::%s:%d more than one subnode in device tree!  Ignoring all but the first.\n`
- `[%llu] ERR: %s::%s:%d failed starting AppleStockholmControlConfig`
- `[%llu] %s::%s:%d Registering`
- `ERR: %s::%s:%d not a socket client!\n`
- `ERR: %s::%s:%d failed starting AppleStockholmControlConfig\n`
- `ERR: %s::%s:%d failed to get commandGate\n`
- `IOBSD`
- `ERR: %s::%s:%d wrong data mode: %d?!\n`
- `spmiFollowerReset`
- `OSBoundedPtr.h`
- `[%llu] ERR: %s::%s:%d Failed to init AppleStockholmControlConfig`
- `ERR: %s::%s:%d failed to start providers start\n`
- `[%llu] %s::%s:%d Rx interrupts enabled`
- `disabled`
- `[%llu] %s::%s:%d _ctlUnit=%d`
- `[%llu] %s::%s:%d data mode set to %s`
- `DNLD`
- `[%llu] %s::%s:%d providerName = %s\n`
- `sn450WithLoadSwitch`
- `support_bootstop_state`
- `nfccModel`
- `2025 Secondary`
- `ERR: %s::%s:%d unexpected follower ID: %02x (%02x)\n`
- `support_boot_measurements`
- `ERR: %s::%s:%d Unknown message type: %x\n`
- `stockholm`
- `[%llu] ERR: %s::%s:%d failed to write %lu bytes to SPMI: %x`
- `ERR: %s::%s:%d Got error interrupt\n`
- `toggleEnable`
- `NCI`
- `ERR: %s::%s:%d No SPMI support! :-o\n`
- `compatible`
- `WARN: %s::%s:%d could not get interrupt source for MBUF SW events\n`
- `[%llu] %s::%s:%d Setting up error interrupt`
- `ERR: %s::%s:%d could not find boot stop function\n`
- `se-lpem-enabled`
- `%s:%d: no node for %s\n`
- `[%llu] ERR: %s::%s:%d could not get interrupt source for NFC_TO_AP_OUT_MSG_IRQ`
- `ERR: %s::%s:%d Error status 0 == 0x%02X\n`
- `ERR: %s::%s:%d Failed to create interrupt source\n`
- `[%llu] ERR: %s::%s:%d Failed to enable interrupt`
- `[%llu] %s::%s:%d write to SPMI[0x%02X] - %02x, attempt %d`
- `[%llu] %s::%s:%d gIOPlatformWakeActionKey - pendingInts=%u`
- `[%llu] %s:%d more user data - triggering IRQ`
- `_debugDevWrite`
- `site.AppleStockholmControlConfig`
- `_requiresFunction`
- `secondary`
- `[%llu] %s::%s:%d Rx interrupts disabled`
- `[%llu] ERR: %s::%s:%d Got error interrupt`
- `[%llu] %s::%s:%d Matching SPMI`
- `WARN: %s::%s:%d overriding %s to 0x%x in EDT\n`
- `bufferHasRoom`
- `enabled`
- `[%llu] %s:%d [%d]`
- `IOPlatformWakeAction`
- `[%llu] ERR: %s::%s:%d Not enough bytes to store data.`
- `ERR: %s::%s:%d Parity status 0 == 0x%02X\n`
- `[%llu] ERR: %s::%s:%d unexpected IRQ Offset: %02x (%02x)`
- `[%llu] %s::%s:%d Setting up data interrupts`
- `ERR: %s::%s:%d failed to get matching for %s\n`
- `[%llu] %s::%s:%d SPMI error request`
- `[%llu] ERR: %s::%s:%d could not find device wake function`
- `createDebugLogger`
- `start`
- `ERR: %s::%s:%d Error registering error interrupt\n`
- `[%llu] %s::%s:%d gIOPlatformSleepActionKey`
- `[%llu] %s::%s:%d Follower reset not supported`
- `ERR: %s:%d failed to allocate mbuf; err=%d\n`
- `BootMeasurements`
- `[%llu] %s::%s:%d enabled=%d`
- `[%llu] ERR: %s::%s:%d bad argument: len = %lu command len = %lu`
- `site.AppleStockholmDebugDevice`
- `[%llu] ERR: %s::%s:%d Unknown message type: %x`
- `[%llu] ERR: %s::%s:%d Resetting SPMI error registers...`
- `[%llu] ERR: %s::%s:%d Attempt to reconfigure Stockholm SPMI - denied!`
- `ctl_data_callback`
- `[%llu] %s::%s:%d Enabling boot stop interrupt.`
- `site.AppleStockholmControlUserClient`
- `[%llu] ERR: %s::%s:%d Invalid buffer.`
- `[%llu] ERR: %s::%s:%d Unsupported command: cmd=%lx direction=%x`
- `ERR: %s::%s:%d Invalid parameter to get command\n`
- `required-gpios`
- `[%llu] %s::%s:%d power toggle = %llu`
- `addData`
- `[%llu] WARN: %s::%s:%d Error overriding model to 0x%x in EDT`
- `[%llu] %s::%s:%d Setting up wake interrupts`
- `function-device_wake`
- `sendFollowerReset`
- `12111112122212121`
- `Error : invalid target\n`
- `com.apple.spmi.nfc`
- `_rxSPMIData`
- `ERR: %s::%s:%d Error : failed to de-assert enable !\n`
- `[%llu] %s::%s:%d Starting`
- `nfc.dev_wake_delay`
- `[%llu] ERR: %s::%s:%d failed to read SPMI[0x%02X] - %02x`
- `ERR: %s::%s:%d Unexpected icefall download request function\n`
- `IOUserClientEntitlements`
- `Juno`
- `.%s`
- `[%llu] ERR: %s::%s:%d Unexpected icefall download request function`
- `setVBATEnable`
- `IOUserClientDefaultLocking`
- `_validateSPMIConfigGated`
- `[%llu] ERR: %s::%s:%d unexpected follower ID: %02x (%02x)`
- `ERR: %s::%s:%d failed to add commandGate to workLoop: %d\n`
- `[%llu] ERR: %s::%s:%d %s model is 0x%x`
- `Legacy`
- `initForSPMI`
- `function-enable`
- `support_download_request`
- `support_data_over_spmi`
- `[%llu] ERR: %s::%s:%d Hammerfest SPMI cannot be configured via itself`
- `[%llu] %s::%s:%d data ready but no user to notify - drop`
- `AppleStockholmSPMI`
- `[%llu] ERR: %s::%s:%d not powered up!`
- `[%llu] %s::%s:%d done with %lu bytes`
- `[%llu] ERR: %s::%s:%d Parity status 2 == 0x%02X`
- `ERR: %s::%s:%d Parity status 2 == 0x%02X\n`
- `ERR: %s::%s:%d bad argument: cmd=%lx direction=%x\n`
- `ERR: %s:%d Failed to allocate new ring buffer\n`
- `%s:%d cannot read data retval=%d\n`
- `ERR: %s::%s:%d No property \"required-functions\"\n`
- `\"%s\" @%s:%d`
- `[%llu] ERR: %s:%d failed to allocate cluster for %lu bytes; err=%d clSize=%lu`
- `ERR: %s::%s:%d failed to read header: %x\n`
- `12111112122212121211111111112112`
- `ERR: %s::%s:%d could not find wakeup enable function\n`
- `[%llu] %s::%s:%d Full SPMI support`
- `AppleStockholmRingBuffer`
- `[%llu] ERR: %s::%s:%d buffer overrun!`
- `[%llu] ERR: %s::%s:%d failed to read %lu bytes from SPMI: %x`
- `ERR: %s:%d Invalid On demand param size %zu\n`
- `[%llu] ERR: %s::%s:%d could not find download request function`
- `[%llu] %s::%s:%d PM Done`
- `[%llu] %s::%s:%d Halley detected, no need to power up or use follower reset`
- `[%llu] ERR: %s::%s:%d failed to read payload: %x`
- `[%llu] ERR: %s::%s:%d Parity status 1 == 0x%02X`
- `ERR: %s::%s:%d Failed to init AppleStockholmControlConfig\n`
- `support_host_wake_spmi`
- `ERR: %s::%s:%d Failed to get SPMI config : 0x%x\n`
- `ERR: %s::%s:%d could not get interrupt source for NFC_TO_AP_OUT_MSG_IRQ\n`
- `OUT_MSG_IRQ`
- `[%llu] %s::%s:%d no more data`
- `[%llu] %s::%s:%d kIOMessageSystemHasPoweredOn`
- `nfc.log.size`
- `hammerfest`
- `[%llu] WARN: %s::%s:%d Warning: boot stop is toggled.`
- `[%llu] ERR: %s::%s:%d no setStandbyEnable function registered! :-o`
- `[%llu] %s::%s:%d coppied %lu bytes  w=%lu r=%lu  dataLen=%lu`
- `[%llu] ERR: %s::%s:%d Error: boot stop is toggled while disabled !.`
- `[%llu] ERR: %s::%s:%d Invalid parameter to get command`
- `setPMUStandbyPowerEnable`
- `ERR: %s::%s:%d Failed to create AppleStockholmControlConfig\n`
- `[%llu] ERR: %s::%s:%d power is off - cannot validate SPMI config!`
- `WARN: %s::%s:%d Reconfiguring Hammerfest SPMI...\n`
- `setNFCCBootMeasurements`
- `[%llu] ERR: %s::%s:%d No data in entry`
- `ERR: %s::%s:%d failed to read payload: %x\n`
- `WARN: %s::%s:%d Warning: boot stop is toggled.\n`
- `ERR: %s::%s:%d support_venable is not defined\n`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `site.AppleStockholmSPMI`
- `[%llu] WARN: %s::%s:%d Already open!`
- `[%llu] %s::%s:%d starting`
- `ERR: %s::%s:%d failed to get workLoop\n`
- `_sendvGPIOGated`
- `[%llu] %s::%s:%d On Demand Client mode %s`
- `[%llu] %s::%s:%d Boot stop get returned %d (error 0x%x)`
- `Warning : entitlements disabled\n`
- `WARN: %s::%s:%d Error overriding model to 0x%x in EDT\n`
- `setStandbyEnable`
- `bounded_ptr<T>::operator+=(n): Calculating the number of bytes to add to the offset (n * sizeof(T)) would trigger an overflow`
- `IOUserClientDefaultLockingSetProperties`
- `[%llu] WARN: %s::%s:%d _hostWakeDelay overiden to %u`
- `_rxInterruptHandler`
- `[%llu] ERR: %s::%s:%d Mbuf list (len=%lu) too short for extra %lu bytes!`
- `[%llu] ERR: %s::%s:%d failed to read header: %x`
- `%s:%d: %s errors suppressed\n`
- `required-functions`
- `[%llu] ERR: %s::%s:%d Property \"%s\" is not of the expected type, it is a %s`
- `site.AppleStockholmControl`
- `[%llu] WARN: %s::%s:%d Poll on SPMI error overiden`
- `[%llu] %s::%s:%d registering socket name: %s`
- `[%llu] ERR: %s::%s:%d could not find VCC function`
- `site.AppleStockholmRingBuffer`
- `[%llu] WARN: %s::%s:%d more than one subnode in device tree!  Ignoring all but the first.`
- `2025 Primary`
- `createWith`
- `[%llu] ERR: %s::%s:%d wrong data mode: %d?!`
- `[%llu] ERR: %s::%s:%d Property \"required-gpios\" is not of the expected type, it is a %s`
- `setDownloadRequest`
- `%s:%d: no instance for %s\n`
- `[%llu] ERR: %s::%s:%d Invalid NFCC model`
- `DNLD hdr: `
- `[%llu] ERR: %s::%s:%d data ready but unable to send to client - drop`
- `support_batt_vcc_bermuda`
- `callPlatformFunction`
- `_dataWrite`
- `ERR: %s::%s:%d unexpected IRQ Offset: %02x (%02x)\n`
- `[%llu] ERR: %s:%d Failed to allocate new ring buffer`
- `[%llu] %s::%s:%d Done`
- `[%llu] ERR: %s::%s:%d failed to write to SPMI[0x%02X]:0x%02x - %02x`
- `[%llu] %s::%s:%d CRC %s`
- `ERR: %s:%d not found!\n`
- `ERR: %s::%s:%d could not find enable function\n`
- `_requiresPowerToSE`
- `EosB1`
- `[%llu] ERR: %s::%s:%d Error status 0 == 0x%02X`
- `ERR: %s::%s:%d could not find download request function\n`
- `[%llu] %s::%s:%d Done Registering`
- `ERR: %s::%s:%d Property \"required-functions\" is not of the expected type, it is a %s\n`
- `[%llu] ERR: %s::%s:%d failed to get workLoop`
- `%s:%d: %s %s is selected\n`
- `ERR: %s::%s:%d could not find VCC function\n`
- `_needsPowerEnableOnBoot`
- `[%llu] WARN: %s::%s:%d overriding %s to 0x%x in EDT`
- `ERR: %s::%s:%d Mbuf list (len=%lu) too short for extra %lu bytes!\n`
- `AppleHammerfestControl`
- `[%llu] ERR: %s::%s:%d Error : failed to de-assert enable !`
- `[%llu] ERR: %s:%d Invalid CRC param size %zu`
- `skip-spmi-reconfig`
- `ERR: %s::%s:%d External load switch drain override set\n`
- `[%llu] %s::%s:%d count=%d`
- `[%llu] WARN: %s::%s:%d originally allocated buffer is too small (%zu). Requesting extra size (%zu, total=%zu) ...`
- `nfc.log`
- `Tx: `
- `[%llu] ERR: %s::%s:%d failed to write data: %x`
- `_matchProperty`
- `WARN: %s::%s:%d no more mbufs - waiting..\n`
- `[%llu] %s::%s:%d Setting up functions`
- `DevWrite: _debugLevel=%d\n`
