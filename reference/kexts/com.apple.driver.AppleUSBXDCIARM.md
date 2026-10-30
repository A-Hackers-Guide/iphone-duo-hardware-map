# `com.apple.driver.AppleUSBXDCIARM`

- Name: AppleUSBXDCIARM
- Version: `1.0`
- UUID: `627900FA-B183-302F-B1D3-B2A96129D31A`
- Source version: `896.40.5.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.2, [`com.apple.driver.AppleTypeCPhy`](com.apple.driver.AppleTypeCPhy.md) 1.0, [`com.apple.driver.AppleUSBXDCI`](com.apple.driver.AppleUSBXDCI.md) 1.0, [`com.apple.driver.usb.AppleUSBCommon`](com.apple.driver.usb.AppleUSBCommon.md) 1.0, [`com.apple.iokit.IOAccessoryManager`](com.apple.iokit.IOAccessoryManager.md) 1.0, [`com.apple.iokit.IOPortFamily`](com.apple.iokit.IOPortFamily.md) 1.0, [`com.apple.iokit.IOUSBDeviceFamily`](com.apple.iokit.IOUSBDeviceFamily.md) 2.0, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.2, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 20.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 20.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 20.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 20.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 20.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) | `AppleT8160USBXDCI` | `usb-drd,t8160` |

## IOKit personalities (12) [KC]

### AppleT8027USBXDCI
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBXDCIARM`
- `IOClass`: `AppleT8027USBXDCI`
- `IOMatchCategory`: `usb-device`
- `IONameMatch`: `usb-drd,t8027`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBXDCIARM`
- `IOPlatformPanicAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8030USBXDCI
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBXDCIARM`
- `IOClass`: `AppleT8030USBXDCI`
- `IOMatchCategory`: `usb-device`
- `IONameMatch`: `usb-drd,t8030`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBXDCIARM`
- `IOPlatformPanicAction`: `1000`
- `IOProbeScore`: `2000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8103USBXDCI
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBXDCIARM`
- `IOClass`: `AppleT8103USBXDCI`
- `IOMatchCategory`: `usb-device`
- `IONameMatch`: `usb-drd,t8103`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBXDCIARM`
- `IOPlatformPanicAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8112USBXDCI
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBXDCIARM`
- `IOClass`: `AppleT8112USBXDCI`
- `IOMatchCategory`: `usb-device`
- `IONameMatch`: `usb-drd,t8112`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBXDCIARM`
- `IOPlatformPanicAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8122USBXDCI
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBXDCIARM`
- `IOClass`: `AppleT8122USBXDCI`
- `IOMatchCategory`: `usb-device`
- `IONameMatch`: `usb-drd,t8122`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBXDCIARM`
- `IOPlatformPanicAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8130USBXDCI
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBXDCIARM`
- `IOClass`: `AppleT8130USBXDCI`
- `IOMatchCategory`: `usb-device`
- `IONameMatch`: `usb-drd,t8130`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBXDCIARM`
- `IOPlatformPanicAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8132USBXDCI
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBXDCIARM`
- `IOClass`: `AppleT8132USBXDCI`
- `IOMatchCategory`: `usb-device`
- `IONameMatch`: `usb-drd,t8132`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBXDCIARM`
- `IOPlatformPanicAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8140USBXDCI
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBXDCIARM`
- `IOClass`: `AppleT8140USBXDCI`
- `IOMatchCategory`: `usb-device`
- `IONameMatch`: `usb-drd,t8140`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBXDCIARM`
- `IOPlatformPanicAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8142USBXDCI
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBXDCIARM`
- `IOClass`: `AppleT8142USBXDCI`
- `IOMatchCategory`: `usb-device`
- `IONameMatch`: `usb-drd,t8142`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBXDCIARM`
- `IOPlatformPanicAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8150USBXDCI
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBXDCIARM`
- `IOClass`: `AppleT8150USBXDCI`
- `IOMatchCategory`: `usb-device`
- `IONameMatch`: `usb-drd,t8150`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBXDCIARM`
- `IOPlatformPanicAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8152USBXDCI
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBXDCIARM`
- `IOClass`: `AppleT8152USBXDCI`
- `IOMatchCategory`: `usb-device`
- `IONameMatch`: `usb-drd,t8152`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBXDCIARM`
- `IOPlatformPanicAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8160USBXDCI
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBXDCIARM`
- `IOClass`: `AppleT8160USBXDCI`
- `IOMatchCategory`: `usb-device`
- `IONameMatch`: `usb-drd,t8160`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBXDCIARM`
- `IOPlatformPanicAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (13) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleT8027USBXDCI` | 0x2720 | AppleUSBXDCIARM → AppleUSBXDCI → IOUSBDeviceController → IOService → IORegistryEntry |
| `AppleT8030USBXDCI` | 0x2720 | AppleT8027USBXDCI → AppleUSBXDCIARM → AppleUSBXDCI → IOUSBDeviceController → IOService → IORegistryEntry |
| `AppleT8103USBXDCI` | 0x2780 | AppleUSBXDCIARM → AppleUSBXDCI → IOUSBDeviceController → IOService → IORegistryEntry |
| `AppleT8112USBXDCI` | 0x2780 | AppleUSBXDCIARM → AppleUSBXDCI → IOUSBDeviceController → IOService → IORegistryEntry |
| `AppleT8122USBXDCI` | 0x2780 | AppleUSBXDCIARM → AppleUSBXDCI → IOUSBDeviceController → IOService → IORegistryEntry |
| `AppleT8130USBXDCI` | 0x2780 | AppleUSBXDCIARM → AppleUSBXDCI → IOUSBDeviceController → IOService → IORegistryEntry |
| `AppleT8132USBXDCI` | 0x2740 | AppleUSBXDCIARM → AppleUSBXDCI → IOUSBDeviceController → IOService → IORegistryEntry |
| `AppleT8140USBXDCI` | 0x2740 | AppleUSBXDCIARM → AppleUSBXDCI → IOUSBDeviceController → IOService → IORegistryEntry |
| `AppleT8142USBXDCI` | 0x2758 | AppleUSBXDCIARM → AppleUSBXDCI → IOUSBDeviceController → IOService → IORegistryEntry |
| `AppleT8150USBXDCI` | 0x2798 | AppleUSBXDCIARM → AppleUSBXDCI → IOUSBDeviceController → IOService → IORegistryEntry |
| `AppleT8152USBXDCI` | 0x2758 | AppleUSBXDCIARM → AppleUSBXDCI → IOUSBDeviceController → IOService → IORegistryEntry |
| `AppleT8160USBXDCI` | 0x2798 | AppleUSBXDCIARM → AppleUSBXDCI → IOUSBDeviceController → IOService → IORegistryEntry |
| `AppleUSBXDCIARM` | 0x2710 | AppleUSBXDCI → IOUSBDeviceController → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000e8b2 off=0x00b0b3b0-0x00b19c62 addr=0xfffffe0007b0f3b0-0xfffffe0007b1dc62 r--/r--   __TEXT            
	sz=0x00000050 off=0x00b0ba30-0x00b0ba80 addr=0xfffffe0007b0fa30-0xfffffe0007b0fa80               __TEXT.__const            
	sz=0x00004614 off=0x00b0ba80-0x00b10094 addr=0xfffffe0007b0fa80-0xfffffe0007b14094               __TEXT.__cstring          (CstringLiterals)
	sz=0x00009bce off=0x00b10094-0x00b19c62 addr=0xfffffe0007b14094-0xfffffe0007b1dc62               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00046920 off=0x0365b0f0-0x036a1a10 addr=0xfffffe000a65f0f0-0xfffffe000a6a5a10 r-x/r-x   __TEXT_EXEC       
	sz=0x000462c0 off=0x0365b0f0-0x036a13b0 addr=0xfffffe000a65f0f0-0xfffffe000a6a53b0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000660 off=0x036a13b0-0x036a1a10 addr=0xfffffe000a6a53b0-0xfffffe000a6a5a10          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000308 off=0x04a1a618-0x04a1a920 addr=0xfffffe000ba1e618-0xfffffe000ba1e920 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a1a618-0x04a1a6e0 addr=0xfffffe000ba1e618-0xfffffe000ba1e6e0               __DATA.__data             
	sz=0x00000240 off=0x00000000-0x00000240 addr=0xfffffe000ba1e6e0-0xfffffe000ba1e920               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00008990 off=0x01439408-0x01441d98 addr=0xfffffe000843d408-0xfffffe0008445d98 rw-/rw-   __DATA_CONST      
	sz=0x00000068 off=0x01439408-0x01439470 addr=0xfffffe000843d408-0xfffffe000843d470         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000068 off=0x01439470-0x014394d8 addr=0xfffffe000843d470-0xfffffe000843d4d8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00008180 off=0x014394d8-0x01441658 addr=0xfffffe000843d4d8-0xfffffe0008445658         __DATA_CONST.__const            
	sz=0x00000340 off=0x01441658-0x01441998 addr=0xfffffe0008445658-0xfffffe0008445998         __DATA_CONST.__kalloc_type      
	sz=0x00000330 off=0x01441998-0x01441cc8 addr=0xfffffe0008445998-0xfffffe0008445cc8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000d0 off=0x01441cc8-0x01441d98 addr=0xfffffe0008445cc8-0xfffffe0008445d98         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 230 at 0x04af9b08
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     627900FA-B183-302F-B1D3-B2A96129D31A
008: LC_SOURCE_VERSION           896.40.5.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac8c48 size=0x260
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleUSBXDCIARM`
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBXDCIARM`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUSBXDCIARM`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2015 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOUSBDeviceFamily.kext/PlugIns/AppleUSBXDCIARM.kext`
- `_PrelinkExecutableLoadAddr`: `-2198894218320`
- `_PrelinkExecutableRelativePath`: `AppleUSBXDCIARM`
- `_PrelinkExecutableSize`: `384618`
- `_PrelinkExecutableSourceAddr`: `-2198894218320`
- `_PrelinkKmodInfo`: `-2198828095976`

## Strings (383) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `tunable_ATC_LINK_REGS`
- `site.AppleT8030USBXDCI`
- `%s@%s: %s::%s: ATC_USB31DRD_CFG_BLK_ISOCTHROTTLE_CTL.ISOCTHROTTLE_RD_LIMIT = 0x%x\n`
- `%s@%s: %s::%s: failed to set up cable change notification\n`
- `AppleT8130USBXDCI.cpp`
- `AppleT8152USBXDCI`
- `i8@?0`
- `forceReEnumeration`
- `hardwareException`
- `%s@%s: %s::%s: could not find USB31DRD Configuration register map\n`
- `%s@%s: %s::%s: AppleEmbeddedUSBArbitrator-force-usbhost set in boot-args, forcing host mode\n`
- `%s@%s: %s::%s: link training approval result %d\n`
- `%s@%s: %s::%s: creating _pipeHandlerRegistersMap failed\n`
- `powerOn`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_CFG.ENABLE_RXVALID_OVERRIDE = 0x%x\n`
- `AppleUSBXDCIARM`
- `AAPL,phandle`
- `removeClockReference`
- `%s@%s: %s::%s: start waiting for resource %s\n`
- `AppleT8142USBXDCI`
- `site.AppleT8112USBXDCI`
- `%s@%s: %s::%s: system wake\n`
- `%s@%s: %s::%s: USB test mode speed (%i) specified\n`
- `site.AppleT8140USBXDCI`
- `AppleT8132USBXDCI`
- `121111121222121211121221222222212212222112121111111212122222112222222222222222222222222222222222222222222222222222222222222221122222222221111121111111111111111111111111111111122221111111112121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121`
- `%s@%s: %s::%s: _hasPsdService = %d\n`
- `%s@%s: %s::%s: failed to sendEndpointCommand(kEpCommandStartXfer) status 0x%08x\n`
- `%s@%s: %s::%s: C0_UTMI_CLK_ACTIVE_EVT_CNT is 0\n`
- `usb-max-speed-capability`
- `addMapperReference`
- `121111121222121211121221222222212212222112121111111212122222112222222222222222222222222222222222222222222222222222222222222221122222222221111121111111111111111111111111111111122221111111112121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121`
- `startEp0Out`
- `AppleT8140USBXDCI.cpp`
- `%s@%s: %s::%s: creating _coreEvtRegistersMap failed\n`
- `enableClock`
- `%s@%s: %s::%s: USB restricted, powering off\n`
- `tunable_CTLREG_DEFAULT`
- `AppleT8150USBXDCI.cpp`
- `%s@%s: %s::%s: creating _atcusbPipeClkCfgRegMap failed\n`
- `%s@%s: %s::%s: timed out waiting for BULKTHROTTLE_CTL.BULKTHROTTLE_OUTSTANDING_WR = 0x%x\n`
- `%s@%s: %s::%s: _atcusbClkCfgRegister 0x%lx\n`
- `atc-phy-parent`
- `site.AppleT8103USBXDCI`
- `%s@%s: %s::%s: kXDCIExceptionStartXferErr (%s). Reinitializing the device controller.\n`
- `%s@%s: %s::%s: creating _atcLinkRegsMap failed\n`
- `AppleT8112USBXDCI`
- `disableClock`
- `AppleT8160USBXDCI`
- `usb-device-skip-wait-resource`
- `%s@%s: %s::%s: transportState is invalid\n`
- `tunable_DRD_USB31_DEV`
- `%s@%s: %s::%s: creating _pmcBWRAUSBCRegistersMap failed\n`
- `AppleT8132USBXDCI.cpp`
- `AppleT8160USBXDCI.cpp`
- `%s@%s: %s::%s: %s completed with 0x%08x\n`
- `AppleT8103USBXDCI`
- `Failure`
- `tunable_DRD_USB31_DBG_DEFAULT`
- `%s@%s: %s::%s: unexpected _clockReferenceCount %u\n`
- `%s@%s: %s::%s: function-vote_force_wakeup_dram not found\n`
- `force-usb-host`
- `%s@%s: %s::%s: failed to create _nextTransportStateLocks[%d]\n`
- `updatePortState`
- `controllerReset`
- `site.AppleT8122USBXDCI`
- `%s@%s: %s::%s: AppleEmbeddedUSBArbitrator-force-usb3host set in boot-args, forcing host mode\n`
- `usb-device-slpddr`
- `%s@%s: %s::%s: negative _clockReferenceCount\n`
- `%s@%s: %s::%s: kExceptionProviderUnavailable: Power cycling the device controller.\n`
- `ep0InEventOccurred`
- `%s@%s: %s::%s: failed PIPE_HANDLER_LOCK_PIPE_IF_ACK\n`
- `site.AppleT8130USBXDCI`
- `121111121222121211121221222222212212222112121111111212122222112222222222222222222222222222222222222222222222222222222222222221122222222221111121111111111111111111111111111111122221111111112121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121`
- `tunable_AUSBC_DEBUG_DEFAULT`
- `AppleT8122USBXDCI`
- `%s@%s: %s::%s: \n`
- `%s@%s: %s::%s: creating _ausbcCtlRegistersMap failed\n`
- `%s@%s: %s::%s: ATC_USB31DRD_CFG_BLK_LLTTHROTTLE_CTL.LLTTHROTTLE_RD_LIMIT = 0x%x\n`
- `site.AppleT8160USBXDCI`
- `AppleT8142USBXDCI.cpp`
- `usb-repeater`
- `%s@%s: %s::%s: failed to create AppleTypeCPhy session\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_AUSBC_AON_GENERAL_REGS.ATC_USB31_DRD_FORCE_CLAMP_EN = 0x%x\n`
- `%s@%s: %s::%s: ATC_USB31DRD_CFG_BLK_LLTTHROTTLE_CTL.LLTTHROTTLE_WR_LIMIT = 0x%x\n`
- `handleUSBWakeFromSlpDDR`
- `AppleT8152USBXDCI.cpp`
- `%s@%s: %s::%s: waiting for resource %s, result %s\n`
- `%s@%s: %s::%s: transferLength %d completionStatus 0x%x (setupPending %d)\n`
- `site.AppleT8027USBXDCI`
- `%s@%s: %s::%s: physical address for registers - 0x%016llx\n`
- `tunable_PIPE_HANDLER_DEVICE`
- `%s@%s: %s::%s: failed to allocate _clockReferenceLock\n`
- `usb-device-wait-resource`
- `Success`
- `%s@%s: %s::%s: could not find register map\n`
- `tunable_AUSBC_PIPE_HANDLER`
- `%s@%s: %s::%s: creating _atcusbClkCfgRegMap failed\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE.NATIVE_POWER_DOWN = 0x%x\n`
- `AppleEmbeddedUSBArbitrator-force-usbhost`
- `%s@%s: %s::%s: skipping wait for resource %s\n`
- `force-usb2-device`
- `USB 2.0`
- `%s@%s: %s::%s: ATC_USB31DRD_CFG_BLK_ISOCTHROTTLE_CTL.ISOCTHROTTLE_WR_LIMIT = 0x%x\n`
- `%s@%s: %s::%s: _atcusbPipeClkCfgRegister 0x%x\n`
- `%s@%s: %s::%s: cable disconnected, powering off\n`
- `%s@%s: %s::%s: unexpected event %d (EP0 IN not active)\n`
- ` @%s:%d`
- `%s@%s: %s::%s: creating _ausbBulkFabricMap failed\n`
- `force-usb-test-mode`
- `powerStateWillChangeTo`
- `%s@%s: %s::%s: creating _pwrCtlRegistersMap failed\n`
- `%s@%s: %s::%s: cable detect disabled: _cableConnected usb2 %d usb3 %d\n`
- `tunable_AUSBC_CTLREG`
- `%s@%s: %s::%s: super::start() failed\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE.NATIVE_RESET = 0x%x\n`
- `%s-disable`
- `usbdevice-disableparrotreset`
- `%s@%s: %s::%s: invalid USB generation %d\n`
- `USB 3.x`
- `ep0OutEventOccurred`
- `%s@%s: %s::%s: sent %d\n completionStatus 0x%08x (setupPending %d)\n`
- `usbdrd-disablepmcbwr`
- `function-parrot_srst`
- `registerTransportNotifications`
- `%s@%s: %s::%s: Port-%s@%d %s ignoring new transport with no USB data role\n`
- `121111121222121211121221222222212212222112121111111212122222112222222222222222222222222222222222222222222222222222222222222221122222222221111121111111111111111111111111111111122221111111112121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121`
- `%s@%s: %s::%s: count %d\n`
- `%s@%s: %s::%s: failed to create _transportMessageNotifiers[%d]\n`
- `USB2`
- `%s@%s: %s::%s: control transfer in %d state\n`
- `%s@%s: %s::%s: timed out waiting for LLTTHROTTLE_CTL.LLTTHROTTLE_OUTSTANDING_WR = 0x%x\n`
- `usb-psd-disable`
- `USB3 + USB2`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_GUSB3PIPECTL_REGS_GUSB3_PIPECTL.SUSPENDENABLE = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_PHY_MUX_SELECT.PIPE_MODE = 0x%x\n`
- `%s@%s: %s::%s: creating _registerMap failed\n`
- `tunable_DRD_CIO_REGS_DEFAULT`
- `%s@%s: %s::%s: failed to open AppleTypeCPhy session\n`
- `%s@%s: %s::%s: creating _ausbintr2axiRegsMap failed\n`
- `%s@%s: %s::%s: timed out waiting for BULKTHROTTLE_CTL.BULKTHROTTLE_OUTSTANDING_RD = 0x%x\n`
- `%s@%s: %s::%s: unexpected _mapperReferenceCount %u\n`
- `tunable_AUSBC_BULK_FABRIC`
- `AppleT8150USBXDCI`
- `%s@%s: %s::%s: in bandwidth: %u KB/µFrame, out bandwidth: %u KB/µFrame\n`
- `%s@%s: %s::%s: failed to build dictionary for atc-phy-parent\n`
- `%s@%s: %s::%s: waiting for link training approval\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_PHY_MUX_SELECT.PIPE_CLK_EN = 0x%x\n`
- `%s@%s: %s::%s: failed to prepareControlTRBs(setup) - length %d\n`
- `121111121222121211121221222222212212222112121111111212122222112222222222222222222222222222222222222222222222222222222222222221122222222221111121111111111111111111111111111111122221111111112121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121`
- `tunable_BULK_FABRIC_DEFAULT`
- `disableMapper`
- `%s@%s: %s::%s: Port-%s@%d %s transport state created\n`
- `%s@%s: %s::%s: received XferNotReady in Status Phase, setting up EP0 IN now\n`
- `%s@%s: %s::%s: force-usb-host set in boot-args, forcing host mode\n`
- `transportCreated`
- `cableChangeOccurred`
- `%s@%s: %s::%s: failed to get provider or invalid provider type\n`
- `%s@%s: %s::%s: failed to create _cableChangeTimer\n`
- `%s@%s: %s::%s: Port-%s@%d %s IOPortTransportState terminated\n`
- `%s@%s: %s::%s: event %d controlState %d\n`
- `site.AppleT8142USBXDCI`
- `%s@%s: %s::%s: ATC_USB31DRD_CFG_BLK_BULKTHROTTLE_CTL.BULKTHROTTLE_WR_LIMIT = 0x%x\n`
- `service-gates`
- `%s@%s: %s::%s: negative _mapperReferenceLock\n`
- `%s@%s: %s::%s: Could not get matchingDict\n`
- `%s@%s: %s::%s: function-parrot_srst on port %d found\n`
- `%s@%s: %s::%s: Unauthorized protocol - %s %s\n`
- `TestConfigSpeed`
- `%s@%s: %s::%s: Port-%s@%d %s: connected: %d (tunneled: %d, role: %s, trm: %d:%d, authorized: %d -> %d)\n`
- `%s@%s: %s::%s: Port-%s@%d %s: connected: %d-> %d (no IOPortTransportState)\n`
- `AppleT8140USBXDCI`
- `site.AppleT8132USBXDCI`
- `%s@%s: %s::%s: timed out waiting for ISOCTHROTTLE_CTL.ISOCTHROTTLE_OUTSTANDING_WR = 0x%x\n`
- `%s@%s: %s::%s: %s matching has been disabled\n`
- `AppleT8027USBXDCI.cpp`
- `%s@%s: %s::%s: failed to find AppleTypeCPhy driver\n`
- `%s@%s: %s::%s: force-usb-device set in boot-args, forcing device mode\n`
- `AppleT8112USBXDCI.cpp`
- `tunable_AUSBC_PWR_CTRL`
- `%s@%s: %s::%s: _atcusbPipeClkCfgRegister 0x%lx\n`
- `parrot-port-number`
- `AppleT8030USBXDCI`
- `AppleUSBXDCIARM.cpp`
- `usb-restore-disable`
- `waitCableChangeNotificationResource`
- `AppleT8122USBXDCI.cpp`
- `%s@%s: %s::%s: unable to allocate _mapperReferenceLock\n`
- `addClockReference`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_LOCK_PIPE_IF_REQ.LOCK_PIPE_IF_REQ = 0x%x\n`
- `%s@%s: %s::%s: kT8027USB31DRD_CFG_PHY_STATUS_PIPE_PHY_READY is not set\n`
- `usb-device-slp-ddr`
- `%s@%s: %s::%s: DVFM_IF_BWR_AGENT_INTERFACE_AGENT_BWR = 0x%llx\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_GUSB2PHYCFG_REGS_GUSB2_PHYCFG.SUSPENDUSB20 = 0x%x\n`
- `start`
- `%s@%s: %s::%s: failed to open AppleTypeCPhy USB2 session\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_CFG.CFG_ENABLE_RECIEVER_DETECT_OVERRIDE = 0x%x\n`
- `AppleT8130USBXDCI`
- `%s@%s: %s::%s: ATC_USB31DRD_CFG_BLK_BULKTHROTTLE_CTL.BULKTHROTTLE_RD_LIMIT = 0x%x\n`
- `%s@%s: %s::%s: timed out waiting for LLTTHROTTLE_CTL.LLTTHROTTLE_OUTSTANDING_RD = 0x%x\n`
- `getPeriodicBandwidthUsage`
- `%s@%s: %s::%s: _atcusbClkCfgRegister 0x%x\n`
- `enableMapper`
- `powerStateDidChangeTo`
- `%s@%s: %s::%s: %s completed with 0x%08x (%d attempts)\n`
- `EP0_OUT`
- `force-usb-device`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE.DUMMY_PHY_READY = 0x%x\n`
- `%s@%s: %s::%s: Port-%s@%d %s new IOPortTransportState\n`
- `%s@%s: %s::%s: received XferNotReady in Status Phase, setting up EP0 OUT now\n`
- `121111121222121211121221222222212212222112121111111212122222112222222222222222222222222222222222222222222222222222222222222221122222222221111121111111111111111111111111111111122221111111112121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121`
- `%s@%s: %s::%s: USB31DRD_PIPE_PHY_READY is 0\n`
- `tunable_LINK_REGS_DEFAULT`
- `%s@%s: %s::%s: cable connected, powering on %s\n`
- `%s@%s: %s::%s: RAM0_WR_ACTIVE is still set\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_VALUES0.RECIEVER_DETECT_OVERRIDE_VALUE = 0x%x\n`
- `AppleTypeCPhy`
- `%s@%s: %s::%s: force-usb-test-mode set in boot-args, forcing device mode\n`
- `USB3`
- `setupDriverRequest`
- `setActive`
- `USB2 only`
- `%s@%s: %s::%s: endpoint 0 not active\n`
- `%s@%s: %s::%s: endpoint has already started\n`
- `%s@%s: %s::%s: No active TRBs, ignoring the event %d\n`
- `site.AppleT8150USBXDCI`
- `%s@%s: %s::%s: _ioPort is NULL, defaulting to device mode\n`
- `removeMapperReference`
- `%s@%s: %s::%s: failed to allocate TRB block from _controlTRBPool\n`
- `enumDoneTimerExpired`
- `%s@%s: %s::%s: creating _configRegistersMap failed\n`
- `function-vote_force_wakeup_dram`
- `%s@%s: %s::%s: system sleep\n`
- `tunable_DRD_USB31_GBL_DEV`
- `%s@%s: %s::%s: usb-restore-disable is set\n`
- `AppleEmbeddedUSBArbitrator-force-usb3host`
- `transportMessage`
- `powerOff`
- `tunable_PWR_CTRL_DEFAULT`
- `%s@%s: %s::%s: kXDCIExceptionPowerOnErr (%s). Reinitializing the device controller.\n`
- `%s@%s: %s::%s: Invalid speed override, stalling request.\n`
- `%s@%s: %s::%s: unexpected transfer complete event on EP0_IN endpoint\n`
- `handleUSBSlpDDR`
- `AppleT8103USBXDCI.cpp`
- `AppleT8027USBXDCI`
- `site.AppleT8152USBXDCI`
- `updateSystemPowerManagement`
- `%s@%s: %s::%s: force-usb2-device set in boot-args, forcing usb2 device mode\n`
- `tunable_DRD_USB31_GBL_DEFAULT`
- `tunable_PIPE_HANDLER_DEFAULT`
- `site.AppleUSBXDCIARM`
- `%s@%s: %s::%s: Could not get _transportPublishNotifiers\n`
- `%s@%s: %s::%s: unexpected event %d (EP0 OUT not active)\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_AUSBC_AON_GENERAL_REGS.ATC_USB31_DRD_SW_VCC_RESET = 0x%x\n`
- `startUSBStack`
- `%s@%s: %s::%s: timed out waiting for ISOCTHROTTLE_CTL.ISOCTHROTTLE_OUTSTANDING_RD = 0x%x\n`
- `-restore`

**[__TEXT.__os_log]**

- `%s@%s: %s::%s: system wake\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_GUSB3PIPECTL_REGS_GUSB3_PIPECTL.SUSPENDENABLE = 0x%x\n`
- `%s@%s: %s::%s: Port-%s@%d %s IOPortTransportState terminated\n`
- `%s@%s: %s::%s: USB restricted, powering off\n`
- `%s@%s: %s::%s: failed to prepareControlTRBs(setup) - length %d\n`
- `%s@%s: %s::%s: creating _registerMap failed\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_PHY_MUX_SELECT.PIPE_MODE = 0x%x\n`
- `%s@%s: %s::%s: Port-%s@%d %s: connected: %d-> %d (no IOPortTransportState)\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE.DUMMY_PHY_READY = 0x%x\n`
- `%s@%s: %s::%s: Port-%s@%d %s: connected: %d (tunneled: %d, role: %s, trm: %d:%d, authorized: %d -> %d)\n`
- `%s@%s: %s::%s: unexpected event %d (EP0 OUT not active)\n`
- `%s@%s: %s::%s: creating _coreEvtRegistersMap failed\n`
- `%s@%s: %s::%s: failed to allocate _clockReferenceLock\n`
- `%s@%s: %s::%s: sent %d\n completionStatus 0x%08x (setupPending %d)\n`
- `%s@%s: %s::%s: could not find register map\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_PHY_MUX_SELECT.PIPE_CLK_EN = 0x%x\n`
- `%s@%s: %s::%s: RAM0_WR_ACTIVE is still set\n`
- `%s@%s: %s::%s: force-usb-test-mode set in boot-args, forcing device mode\n`
- `%s@%s: %s::%s: count %d\n`
- `%s@%s: %s::%s: received XferNotReady in Status Phase, setting up EP0 OUT now\n`
- `%s@%s: %s::%s: in bandwidth: %u KB/µFrame, out bandwidth: %u KB/µFrame\n`
- `%s@%s: %s::%s: failed to find AppleTypeCPhy driver\n`
- `%s@%s: %s::%s: No active TRBs, ignoring the event %d\n`
- `%s@%s: %s::%s: received XferNotReady in Status Phase, setting up EP0 IN now\n`
- `%s@%s: %s::%s: C0_UTMI_CLK_ACTIVE_EVT_CNT is 0\n`
- `%s@%s: %s::%s: creating _ausbcCtlRegistersMap failed\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_AUSBC_AON_GENERAL_REGS.ATC_USB31_DRD_FORCE_CLAMP_EN = 0x%x\n`
- `%s@%s: %s::%s: _atcusbClkCfgRegister 0x%lx\n`
- `%s@%s: %s::%s: Port-%s@%d %s transport state created\n`
- `%s@%s: %s::%s: cable detect disabled: _cableConnected usb2 %d usb3 %d\n`
- `%s@%s: %s::%s: kXDCIExceptionPowerOnErr (%s). Reinitializing the device controller.\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE.NATIVE_POWER_DOWN = 0x%x\n`
- `%s@%s: %s::%s: creating _atcusbPipeClkCfgRegMap failed\n`
- `%s@%s: %s::%s: failed to build dictionary for atc-phy-parent\n`
- `%s@%s: %s::%s: link training approval result %d\n`
- `%s@%s: %s::%s: %s completed with 0x%08x\n`
- `%s@%s: %s::%s: USB test mode speed (%i) specified\n`
- `%s@%s: %s::%s: unexpected _clockReferenceCount %u\n`
- `%s@%s: %s::%s: timed out waiting for BULKTHROTTLE_CTL.BULKTHROTTLE_OUTSTANDING_RD = 0x%x\n`
- `%s@%s: %s::%s: skipping wait for resource %s\n`
- `%s@%s: %s::%s: creating _pwrCtlRegistersMap failed\n`
- `%s@%s: %s::%s: creating _ausbBulkFabricMap failed\n`
- `%s@%s: %s::%s: function-vote_force_wakeup_dram not found\n`
- `%s@%s: %s::%s: negative _clockReferenceCount\n`
- `%s@%s: %s::%s: Port-%s@%d %s new IOPortTransportState\n`
- `%s@%s: %s::%s: creating _atcLinkRegsMap failed\n`
- `%s@%s: %s::%s: failed PIPE_HANDLER_LOCK_PIPE_IF_ACK\n`
- `%s@%s: %s::%s: _ioPort is NULL, defaulting to device mode\n`
- `%s@%s: %s::%s: cable connected, powering on %s\n`
- `%s@%s: %s::%s: cable disconnected, powering off\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_CFG.CFG_ENABLE_RECIEVER_DETECT_OVERRIDE = 0x%x\n`
- `%s@%s: %s::%s: timed out waiting for ISOCTHROTTLE_CTL.ISOCTHROTTLE_OUTSTANDING_WR = 0x%x\n`
- `%s@%s: %s::%s: usb-restore-disable is set\n`
- `%s@%s: %s::%s: _atcusbClkCfgRegister 0x%x\n`
- `%s@%s: %s::%s: _hasPsdService = %d\n`
- `%s@%s: %s::%s: force-usb-device set in boot-args, forcing device mode\n`
- `%s@%s: %s::%s: %s completed with 0x%08x (%d attempts)\n`
- `%s@%s: %s::%s: negative _mapperReferenceLock\n`
- `%s@%s: %s::%s: creating _atcusbClkCfgRegMap failed\n`
- `%s@%s: %s::%s: function-parrot_srst on port %d found\n`
- `%s@%s: %s::%s: control transfer in %d state\n`
- `%s@%s: %s::%s: failed to open AppleTypeCPhy session\n`
- `%s@%s: %s::%s: creating _pipeHandlerRegistersMap failed\n`
- `%s@%s: %s::%s: super::start() failed\n`
- `%s@%s: %s::%s: Could not get _transportPublishNotifiers\n`
- `%s@%s: %s::%s: creating _configRegistersMap failed\n`
- `%s@%s: %s::%s: ATC_USB31DRD_CFG_BLK_ISOCTHROTTLE_CTL.ISOCTHROTTLE_WR_LIMIT = 0x%x\n`
- `%s@%s: %s::%s: timed out waiting for ISOCTHROTTLE_CTL.ISOCTHROTTLE_OUTSTANDING_RD = 0x%x\n`
- `%s@%s: %s::%s: Invalid speed override, stalling request.\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_VALUES0.RECIEVER_DETECT_OVERRIDE_VALUE = 0x%x\n`
- `%s@%s: %s::%s: ATC_USB31DRD_CFG_BLK_ISOCTHROTTLE_CTL.ISOCTHROTTLE_RD_LIMIT = 0x%x\n`
- `%s@%s: %s::%s: AppleEmbeddedUSBArbitrator-force-usbhost set in boot-args, forcing host mode\n`
- `%s@%s: %s::%s: transportState is invalid\n`
- `%s@%s: %s::%s: system sleep\n`
- `%s@%s: %s::%s: unexpected _mapperReferenceCount %u\n`
- `%s@%s: %s::%s: waiting for resource %s, result %s\n`
- `%s@%s: %s::%s: _atcusbPipeClkCfgRegister 0x%lx\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE.NATIVE_RESET = 0x%x\n`
- `%s@%s: %s::%s: failed to get provider or invalid provider type\n`
- `%s@%s: %s::%s: failed to create _nextTransportStateLocks[%d]\n`
- `%s@%s: %s::%s: force-usb2-device set in boot-args, forcing usb2 device mode\n`
- `%s@%s: %s::%s: kExceptionProviderUnavailable: Power cycling the device controller.\n`
- `%s@%s: %s::%s: transferLength %d completionStatus 0x%x (setupPending %d)\n`
- `%s@%s: %s::%s: unable to allocate _mapperReferenceLock\n`
- `%s@%s: %s::%s: AppleEmbeddedUSBArbitrator-force-usb3host set in boot-args, forcing host mode\n`
- `%s@%s: %s::%s: unexpected transfer complete event on EP0_IN endpoint\n`
- `%s@%s: %s::%s: ATC_USB31DRD_CFG_BLK_LLTTHROTTLE_CTL.LLTTHROTTLE_WR_LIMIT = 0x%x\n`
- `%s@%s: %s::%s: timed out waiting for BULKTHROTTLE_CTL.BULKTHROTTLE_OUTSTANDING_WR = 0x%x\n`
- `%s@%s: %s::%s: timed out waiting for LLTTHROTTLE_CTL.LLTTHROTTLE_OUTSTANDING_RD = 0x%x\n`
- `%s@%s: %s::%s: ATC_USB31DRD_CFG_BLK_LLTTHROTTLE_CTL.LLTTHROTTLE_RD_LIMIT = 0x%x\n`
- `%s@%s: %s::%s: failed to create _transportMessageNotifiers[%d]\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_GUSB2PHYCFG_REGS_GUSB2_PHYCFG.SUSPENDUSB20 = 0x%x\n`
- `%s@%s: %s::%s: kT8027USB31DRD_CFG_PHY_STATUS_PIPE_PHY_READY is not set\n`
- `%s@%s: %s::%s: creating _ausbintr2axiRegsMap failed\n`
- `%s@%s: %s::%s: failed to sendEndpointCommand(kEpCommandStartXfer) status 0x%08x\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_AUSBC_AON_GENERAL_REGS.ATC_USB31_DRD_SW_VCC_RESET = 0x%x\n`
- `%s@%s: %s::%s: creating _pmcBWRAUSBCRegistersMap failed\n`
- `%s@%s: %s::%s: ATC_USB31DRD_CFG_BLK_BULKTHROTTLE_CTL.BULKTHROTTLE_WR_LIMIT = 0x%x\n`
- `%s@%s: %s::%s: invalid USB generation %d\n`
- `%s@%s: %s::%s: unexpected event %d (EP0 IN not active)\n`
- `%s@%s: %s::%s: \n`
- `%s@%s: %s::%s: ATC_USB31DRD_CFG_BLK_BULKTHROTTLE_CTL.BULKTHROTTLE_RD_LIMIT = 0x%x\n`
- `%s@%s: %s::%s: waiting for link training approval\n`
- `%s@%s: %s::%s: physical address for registers - 0x%016llx\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_CFG.ENABLE_RXVALID_OVERRIDE = 0x%x\n`
- `%s@%s: %s::%s: failed to open AppleTypeCPhy USB2 session\n`
- `%s@%s: %s::%s: DVFM_IF_BWR_AGENT_INTERFACE_AGENT_BWR = 0x%llx\n`
- `%s@%s: %s::%s: _atcusbPipeClkCfgRegister 0x%x\n`
- `%s@%s: %s::%s: start waiting for resource %s\n`
- `%s@%s: %s::%s: Could not get matchingDict\n`
- `%s@%s: %s::%s: Port-%s@%d %s ignoring new transport with no USB data role\n`
- `%s@%s: %s::%s: kXDCIExceptionStartXferErr (%s). Reinitializing the device controller.\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_LOCK_PIPE_IF_REQ.LOCK_PIPE_IF_REQ = 0x%x\n`
- `%s@%s: %s::%s: failed to set up cable change notification\n`
- `%s@%s: %s::%s: endpoint 0 not active\n`
- `%s@%s: %s::%s: endpoint has already started\n`
- `%s@%s: %s::%s: event %d controlState %d\n`
- `%s@%s: %s::%s: USB31DRD_PIPE_PHY_READY is 0\n`
- `%s@%s: %s::%s: %s matching has been disabled\n`
- `%s@%s: %s::%s: could not find USB31DRD Configuration register map\n`
- `%s@%s: %s::%s: timed out waiting for LLTTHROTTLE_CTL.LLTTHROTTLE_OUTSTANDING_WR = 0x%x\n`
- `%s@%s: %s::%s: failed to create AppleTypeCPhy session\n`
- `%s@%s: %s::%s: failed to create _cableChangeTimer\n`
- `%s@%s: %s::%s: force-usb-host set in boot-args, forcing host mode\n`
- `%s@%s: %s::%s: Unauthorized protocol - %s %s\n`
- `%s@%s: %s::%s: failed to allocate TRB block from _controlTRBPool\n`
