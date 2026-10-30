# `com.apple.driver.usb.AppleSynopsysUSBXHCI`

- Name: AppleSynopsysUSBXHCI
- Version: `1`
- UUID: `DC51D431-549C-3209-9CC4-9ECE2C072649`
- Source version: `717.40.5.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleEmbeddedUSBHost`](com.apple.driver.AppleEmbeddedUSBHost.md) 1.0, [`com.apple.driver.AppleTypeCPhy`](com.apple.driver.AppleTypeCPhy.md) 1.0, [`com.apple.driver.usb.AppleUSBCommon`](com.apple.driver.usb.AppleUSBCommon.md) 1.0, [`com.apple.driver.usb.AppleUSBXHCI`](com.apple.driver.usb.AppleUSBXHCI.md) 1.2, [`com.apple.iokit.IOAccessoryManager`](com.apple.iokit.IOAccessoryManager.md) 1.0.0, [`com.apple.iokit.IOPortFamily`](com.apple.iokit.IOPortFamily.md) 1.0, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.2, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 15.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 15.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 15.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 15.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 16.5.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 15.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) | `AppleT8160USBXHCI` | `usb-drd,t8160` |

## IOKit personalities (7) [KC]

### AppleT8027USBXHCI
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleSynopsysUSBXHCI`
- `IOClass`: `AppleT8027USBXHCI`
- `IOMatchCategory`: `usb-host`
- `IONameMatch`: `usb-drd,t8027`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleSynopsysUSBXHCI`
- `IOProbeScore`: `9998`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8030USBXHCI
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleSynopsysUSBXHCI`
- `IOClass`: `AppleT8030USBXHCI`
- `IOMatchCategory`: `usb-host`
- `IONameMatch`: `usb-drd,t8030`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleSynopsysUSBXHCI`
- `IOProbeScore`: `9999`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8101USBXHCI
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleSynopsysUSBXHCI`
- `IOClass`: `AppleT8101USBXHCI`
- `IOMatchCategory`: `usb-host`
- `IONameMatch`: `usb-drd,t8101`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleSynopsysUSBXHCI`
- `IOProbeScore`: `10000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8130USBXHCI
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleSynopsysUSBXHCI`
- `IOClass`: `AppleT8130USBXHCI`
- `IOMatchCategory`: `usb-host`
- `IONameMatch`: `usb-drd,t8130`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleSynopsysUSBXHCI`
- `IOProbeScore`: `10001`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8140USBXHCI
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleSynopsysUSBXHCI`
- `IOClass`: `AppleT8140USBXHCI`
- `IOMatchCategory`: `usb-host`
- `IONameMatch`: `usb-drd,t8140`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleSynopsysUSBXHCI`
- `IOProbeScore`: `10002`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8150USBXHCI
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleSynopsysUSBXHCI`
- `IOClass`: `AppleT8150USBXHCI`
- `IOMatchCategory`: `usb-host`
- `IONameMatch`: `usb-drd,t8150`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleSynopsysUSBXHCI`
- `IOProbeScore`: `10001`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8160USBXHCI
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleSynopsysUSBXHCI`
- `IOClass`: `AppleT8160USBXHCI`
- `IOMatchCategory`: `usb-host`
- `IONameMatch`: `usb-drd,t8160`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleSynopsysUSBXHCI`
- `IOProbeScore`: `10001`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (18) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleSynopsysDRDUSBXHCI` | 0xfc8 | AppleUSBXHCIARM → AppleUSBXHCI → AppleUSBHostController → IOService → IORegistryEntry |
| `AppleSynopsysDRDUSBXHCICommandRing` | 0x1868 | AppleUSBXHCICommandRing |
| `AppleT8027USBXHCI` | 0xfe0 | AppleT8030USBXHCI → AppleT8101USBXHCI → AppleSynopsysDRDUSBXHCI → AppleUSBXHCIARM → AppleUSBXHCI → AppleUSBHostController → IOService → IORegistryEntry |
| `AppleT8027USBXHCICommandRing` | 0x1a98 | AppleSynopsysDRDUSBXHCICommandRing → AppleUSBXHCICommandRing |
| `AppleT8030USBXHCI` | 0xfe0 | AppleT8101USBXHCI → AppleSynopsysDRDUSBXHCI → AppleUSBXHCIARM → AppleUSBXHCI → AppleUSBHostController → IOService → IORegistryEntry |
| `AppleT8030USBXHCICommandRing` | 0x1870 | AppleSynopsysDRDUSBXHCICommandRing → AppleUSBXHCICommandRing |
| `AppleT8101USB20XHCILightningPort` | 0x450 | AppleUSB20XHCILightningPort → AppleUSB20XHCITypeCPort → AppleUSB20XHCIPort → AppleUSBXHCIPort → AppleUSBHostPort → IOService → IORegistryEntry |
| `AppleT8101USBXHCI` | 0xfd8 | AppleSynopsysDRDUSBXHCI → AppleUSBXHCIARM → AppleUSBXHCI → AppleUSBHostController → IOService → IORegistryEntry |
| `AppleT8130USBXHCI` | 0x1000 | AppleUSBXHCIARM → AppleUSBXHCI → AppleUSBHostController → IOService → IORegistryEntry |
| `AppleT8130USBXHCICommandRing` | 0x1868 | AppleUSBXHCICommandRing |
| `AppleT8140USBXHCI` | 0xff8 | AppleUSBXHCIARM → AppleUSBXHCI → AppleUSBHostController → IOService → IORegistryEntry |
| `AppleT8150USBXHCI` | 0x1010 | AppleUSBXHCIARM → AppleUSBXHCI → AppleUSBHostController → IOService → IORegistryEntry |
| `AppleT8160USBXHCI` | 0x1010 | AppleUSBXHCIARM → AppleUSBXHCI → AppleUSBHostController → IOService → IORegistryEntry |
| `AppleUSB20XHCIARMPort` | 0x438 | AppleUSB20XHCITypeCPort → AppleUSB20XHCIPort → AppleUSBXHCIPort → AppleUSBHostPort → IOService → IORegistryEntry |
| `AppleUSB20XHCILightningPort` | 0x438 | AppleUSB20XHCITypeCPort → AppleUSB20XHCIPort → AppleUSBXHCIPort → AppleUSBHostPort → IOService → IORegistryEntry |
| `AppleUSB30XHCIARMPort` | 0x438 | AppleUSB30XHCITypeCPort → AppleUSB30XHCIPort → AppleUSBXHCIPort → AppleUSBHostPort → IOService → IORegistryEntry |
| `AppleUSBXHCIARM` | 0xfa0 | AppleUSBXHCI → AppleUSBHostController → IOService → IORegistryEntry |
| `AppleUSBXHCIARMEndpointSoftRetry` | 0x70 | AppleUSBXHCIEndpointSoftRetry → AppleUSBXHCIEndpoint |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000d74a off=0x00b413d0-0x00b4eb1a addr=0xfffffe0007b453d0-0xfffffe0007b52b1a r--/r--   __TEXT            
	sz=0x000044d0 off=0x00b41a98-0x00b45f68 addr=0xfffffe0007b45a98-0xfffffe0007b49f68               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000020 off=0x00b45f70-0x00b45f90 addr=0xfffffe0007b49f70-0xfffffe0007b49f90               __TEXT.__const            
	sz=0x00008b8a off=0x00b45f90-0x00b4eb1a addr=0xfffffe0007b49f90-0xfffffe0007b52b1a               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0004b7f0 off=0x0379e1d0-0x037e99c0 addr=0xfffffe000a7a21d0-0xfffffe000a7ed9c0 r-x/r-x   __TEXT_EXEC       
	sz=0x0004b210 off=0x0379e1d0-0x037e93e0 addr=0xfffffe000a7a21d0-0xfffffe000a7ed3e0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000005e0 off=0x037e93e0-0x037e99c0 addr=0xfffffe000a7ed3e0-0xfffffe000a7ed9c0          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000003c8 off=0x04a1b800-0x04a1bbc8 addr=0xfffffe000ba1f800-0xfffffe000ba1fbc8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a1b800-0x04a1b8c8 addr=0xfffffe000ba1f800-0xfffffe000ba1f8c8               __DATA.__data             
	sz=0x000002e0 off=0x00000000-0x000002e0 addr=0xfffffe000ba1f8c8-0xfffffe000ba1fba8               __DATA.__common           (Zerofill)
	sz=0x00000020 off=0x00000000-0x00000020 addr=0xfffffe000ba1fba8-0xfffffe000ba1fbc8               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00009e48 off=0x01457ef0-0x01461d38 addr=0xfffffe000845bef0-0xfffffe0008465d38 rw-/rw-   __DATA_CONST      
	sz=0x00000090 off=0x01457ef0-0x01457f80 addr=0xfffffe000845bef0-0xfffffe000845bf80         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000090 off=0x01457f80-0x01458010 addr=0xfffffe000845bf80-0xfffffe000845c010         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00009288 off=0x01458010-0x01461298 addr=0xfffffe000845c010-0xfffffe0008465298         __DATA_CONST.__const            
	sz=0x00000680 off=0x01461298-0x01461918 addr=0xfffffe0008465298-0xfffffe0008465918         __DATA_CONST.__kalloc_type      
	sz=0x000002f0 off=0x01461918-0x01461c08 addr=0xfffffe0008465918-0xfffffe0008465c08         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000130 off=0x01461c08-0x01461d38 addr=0xfffffe0008465c08-0xfffffe0008465d38         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 226 at 0x04afa804
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     DC51D431-549C-3209-9CC4-9ECE2C072649
008: LC_SOURCE_VERSION           717.40.5.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac9c18 size=0x360
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleSynopsysUSBXHCI`
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleSynopsysUSBXHCI`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSynopsysUSBXHCI`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
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
- `NSHumanReadableCopyright`: `Copyright © 2021 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/AppleSynopsysUSBXHCI.kext`
- `_PrelinkExecutableLoadAddr`: `-2198893997104`
- `_PrelinkExecutableRelativePath`: `AppleSynopsysUSBXHCI`
- `_PrelinkExecutableSize`: `405834`
- `_PrelinkExecutableSourceAddr`: `-2198893997104`
- `_PrelinkKmodInfo`: `-2198828091392`

## Strings (421) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.AppleUSB20XHCILightningPort`
- `site.AppleUSB20XHCIARMPort`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_PHY_MUX_SELECT.PIPE_CLK_EN = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_PHY_MUX_SELECT.PIPE_MODE = 0x%x\n`
- `applyAllTunables`
- `setActive`
- `copyPhandleDriverFromProvider`
- `AppleT8027USBXHCI`
- `UsbHostControllerSoftRetryPolicy`
- `%s@%s: %s::%s: DWC_USB31_BLOCK_GBL_GUSB2PHYCFG_REGS_GUSB2_PHYCFG.SUSPENDUSB20 = 0x%x\n`
- `AppleSynopsysDRDUSBXHCICommandRing`
- `%s: %s::%s: unable to assign %d dummy endpoints (mask 0x%08x)\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_AUSBC_AON_GENERAL_REGS.ATC_USB31_DRD_SW_VCC_RESET = 0x%x\n`
- `tunable_DRD_USB31_GBL_DEFAULT`
- `tunable_DRD_USB31_DBG_DEFAULT`
- `%s@%s: %s::%s: port %d unsupported protocol %s %x.%x\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_AUSBC_AON_GENERAL_REGS.ATC_USB31_DRD_FORCE_CLAMP_EN = 0x%x\n`
- `requestUSB3Mode`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE.NATIVE_RESET = 0x%x\n`
- `probe`
- `%s@%s: %s::%s: failed to find %s for %s\n`
- `%s@%s: %s::%s: %s completed with 0x%08x (%d attempts)\n`
- `121111121222121211211111222222222222222222222222222222222222222222222222222222222222222212121121111122222222222222221211222222222222222222222222222222222222222222222222212111111111222122222222222211222211112222211211111111111111111111111111111111111111111111111111111111111111111111111111111111111111`
- `%s@%s: %s::%s: USB3 mode change\n`
- `%s@%s: %s::%s: unexpected transition from mode %d to %d\n`
- `%s@%s: %s::%s: tunable range %d offset 0x%08x mask 0x%08x value 0x%08x (read 0x%08x wrote 0x%08x)\n`
- `%s@%s: %s::%s: hibernate power loss\n`
- `ss-companion-controller`
- `%s@%s: %s::%s: timed out waiting for SLEEP HIBERNATION_UNMASKED_STATUS 0x%08x HIBERNATION_STATUS 0x%08x\n`
- `%s@%s: %s::%s: %lu\n`
- `Success`
- `%s@%s: %s::%s: tunable offset 0x%08x mask 0x%08x value 0x%08x (read 0x%08x wrote 0x%08x)\n`
- `allow`
- `UsbHostControllerPersistFullSpeedIsochronous`
- `ss-companion-port-number`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.CFG_USB2PHY_REGS_FORCE_CLK_ON = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE.DUMMY_PHY_READY = 0x%x\n`
- `addEndpoint`
- `site.AppleT8101USB20XHCILightningPort`
- `AppleEmbeddedUSBXHCIFL1100`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_BEFORE_2_GUCTL6 = 0x%x\n`
- `%s@%s: %s::%s: creating _pmcBWRRegistersMap failed\n`
- `setPowerStateGated`
- `setMaximumPortLinkSpeed_block_invoke`
- `%s@%s: %s::%s: port %d USB 2.%x with %d speed IDs\n`
- `regWriteSram32`
- `%s@%s: %s::%s: sleep power loss\n`
- `atc-phy-parent`
- `%s@%s: %s::%s: AUSBC_PWR_CTRL_BLK_TXDETRX_LOCK_REQ.FLD = 0x%x\n`
- `%s@%s: %s::%s: regIndex %d invalid, failed to apply tunable tag '%s'\n`
- `AppleT8140USBXHCI`
- `%s@%s: %s::%s: failed to create AppleTypeCPhy session\n`
- `%s@%s: %s::%s: waiting for resource %s, result %s\n`
- `copyPhandleDriver`
- `site.AppleT8140USBXHCI`
- `%s@%s: %s::%s: performance floor: none\n`
- `tunable_PIPE_HANDLER_DEFAULT`
- `AppleT8130USBXHCICommandRing`
- `createPort`
- `211`
- `%s: %s::%s: drop dummy endpoint mask 0x%08x\n`
- `121111121222121211211111222222222222222222222222222222222222222222222222222222222222222212121121111122222222222222221211222222222222222222222222222222222222222222222222212111111111222122222222222211222211112222211211111111111111111111111111111111111111111111111111111111111111111111111111111111111111`
- `%s@%s: %s::%s: PMC disabled via boot arg\n`
- `disableMapper`
- `AppleTypeCPhy`
- `%s@%s: %s::%s: failed to find phyService\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_GUSB3PIPECTL_REGS_GUSB3_PIPECTL.SUSPENDENABLE = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_VALUES0.RECIEVER_DETECT_OVERRIDE_VALUE = 0x%x\n`
- `%s@%s: %s::%s: timed out waiting for D0_ON interrupt HIBERNATION_UNMASKED_STATUS 0x%08x HIBERNATION_STATUS 0x%08x\n`
- `getPeriodicBandwidthUsage`
- `locationID`
- `getCompanionControllerGated`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_BEFORE_0_GCTL.PWRDNSCALE = 0x%x\n`
- `%s@%s: %s::%s: PIPE_HANDLER_LOCK_PIPE_IF_ACK did not clear\n`
- `enableMapper`
- `%s@%s: %s::%s: DWC_USB31_BLOCK_GBL_BEFORE_0_GCTL.PRTCAPDIR = 0x%x\n`
- `site.AppleT8030USBXHCICommandRing`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.DRD_TOP_REGS_FORCE_CLK_ON = 0x%x\n`
- `AppleT8140USBXHCI.cpp`
- `%s@%s: %s::%s: setPowerLevel failed with 0x%08x\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_HOST_CNTRL_PORT_REG_SET_PORTSC_30_REGS_PORTSC_30.PP = 0x%x\n`
- `tunable_LINK_REGS_DEFAULT`
- `AppleUSBXHCIARM`
- `%s@%s: %s::%s: %s matching has been disabled\n`
- `%s@%s: %s::%s: found companion controller %p (%s) for speed %d\n`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.DEBUG_WRAP_REGS_FORCE_CLK_ON = 0x%x\n`
- `%s@%s: %s::%s: copyMapperForDevice() failed\n`
- `AppleUSBXHCIARM.cpp`
- `AppleUSB20XHCILightningPort`
- `121211211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `companion-id`
- `121211211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `AppleT8150USBXHCI`
- `AppleT8150USBXHCI.cpp`
- `AppleT8030USBXHCI`
- `%s: %s::%s: hardware is unavailable\n`
- `usbdrd-disablepmcbwr`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE.NATIVE_POWER_DOWN = 0x%x\n`
- `%s@%s: %s::%s: DVFM_IF_BWR_AGENT_INTERFACE_AGENT_BWR = 0x%llx\n`
- `site.T`
- `%s@%s: %s::%s: Applying tunable tag '%s' (block offset 0x%08x)\n`
- `121111121222121211211111222222222222222222222222222222222222222222222222222222222222222212121121111122222222222222221211222222222222222222222222222222222222222222222222212111111111222122222222222211222211112222211211111111111111111111111111111111111111111111111111111111111111111111111111111111111111`
- `%s: %s::%s: slot %u endpoint %u\n`
- `site.AppleT8130USBXHCI`
- `%s@%s: %s::%s: port %d is not a USB3 port\n`
- `ATCPhyParrotSoftReset`
- `kUSBSleepSupported`
- `%s@%s: %s::%s: start waiting for resource %s\n`
- `site.AppleSynopsysDRDUSBXHCICommandRing`
- `%s@%s: %s::%s: unknown speed\n`
- `%s@%s: %s::%s: creating _configRegistersMap failed\n`
- `%s@%s: %s::%s: unexpected LOCK_PIPE_IF_ACK 1\n`
- `%s@%s: %s::%s: AUSBC_PWR_CTRL_BLK_HIBERNATION_CLEAR.INTR = 0x%x\n`
- `i8@?0`
- `%s@%s: %s::%s: tunable offset 0x%08x mask 0x%08x value 0x%08x already set (read 0x%08x)\n`
- `AAPL,phandle`
- `%s@%s: %s::%s: failed to attach or start port %d\n`
- `%s@%s: %s::%s: DWC_USB31_BLOCK_GBL_GUSB3PIPECTL_REGS_GUSB3_PIPECTL.SUSPENDENABLE = 0x%x\n`
- ` @%s:%d`
- `updateSystemPowerManagement`
- `site.AppleT8027USBXHCICommandRing`
- `tunable_DRD_USB31_GBL_HOST`
- `site.AppleT8130USBXHCICommandRing`
- `%s: %s::%s: isochronous dummy endpoint mask 0x%08x -> 0x%08x\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_GUSB2PHYCFG_REGS_GUSB2_PHYCFG.SUSPENDUSB20 = 0x%x\n`
- `%s@%s: %s::%s: ping list head index %u\n`
- `%s: %s::%s: fallback completed with result code %u\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_CFG.ENABLE_RXVALID_OVERRIDE = 0x%x\n`
- `%s@%s: %s::%s: PIPE_HANDLER_LOCK_PIPE_IF_ACK did not set\n`
- `updateEndpoint`
- `printPeriodicSchedule`
- `%s-disable`
- `%s@%s: %s::%s: port %d USB 3.%x with %d speed IDs\n`
- `AppleSynopsysDRDUSBXHCI`
- `addEndpointWithDummy`
- `%s: %s::%s: command with dummy endpoint failed, attempting to configure without dummy endpoint\n`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.BULK_FABRIC_REGS_FORCE_CLK_ON = 0x%x\n`
- `waitForExternalResources`
- `12211121122122`
- `AppleT8130USBXHCI`
- `%s@%s: %s::%s: creating _powerControlRegistersMap failed\n`
- `%s@%s: %s::%s: creating _coreEvtRegistersMap failed\n`
- `tunable_DRD_USB31_CFG_HOST`
- `dropEndpoint`
- `%s@%s: %s::%s: failed to create or open AppleTypeCPhy session\n`
- `site.AppleT8027USBXHCI`
- `function-vote_force_wakeup_dram`
- `UsbHostControllerDeferRegisterService`
- `site.AppleUSBXHCIARM`
- `%s@%s: %s::%s: _systemPowerChangeThread is already scheduled\n`
- `%s@%s: %s::%s: creating _ctlRegistersMap failed\n`
- `%s@%s: %s::%s: failed to enable phy\n`
- `ParrotSoftResetWorkAroundActive`
- `AppleT8030USBXHCICommandRing`
- `AppleT8160USBXHCI.cpp`
- `systemPowerChange`
- `getCompanionPort`
- `AppleUSBXHCIARMEndpointSoftRetry`
- `121111121222121211211111222222222222222222222222222222222222222222222222222222222222222212121121111122222222222222221211222222222222222222222222222222222222222222222222212111111111222122222222222211222211112222211211111111111111111111111111111111111111111111111111111111111111111111111111111111111111`
- `%s@%s: %s::%s: timed out waiting for VVDD_USB_OFF interrupt HIBERNATION_UNMASKED_STATUS 0x%08x HIBERNATION_STATUS 0x%08x\n`
- `powerControlInterrupt`
- `usb-host-wait-resource`
- `%s@%s: %s::%s: %s completed with 0x%08x\n`
- `powerStateWillChangeTo_block_invoke`
- `dropEndpointWithDummy`
- `%s@%s: %s::%s: searching for port with locationID 0x%08x\n`
- `%s: %s::%s: forcing endpoint interval from %d uFrames to %d uFrames\n`
- `%s: %s::%s: slot context 0x%08x 0x%08x 0x%08x 0x%08x\n`
- `%s@%s: %s::%s: failed to enable USB2 phy\n`
- `raiseOnePowerStateTo`
- `%s@%s: %s::%s: \n`
- `%s@%s: %s::%s: in bandwidth: %u KB/µFrame, out bandwidth: %u KB/µFrame\n`
- `121111121222121211222222212222222222222222222222222222222222222222222222222221221111122221112112222222222211122112111111111111111112221`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_LOCK_PIPE_IF_REQ.LOCK_PIPE_IF_REQ = 0x%x\n`
- `applyTunables`
- `site.tSystemPowerNotifyParams`
- `ParrotSoftResetDigitalIDArray`
- `%s@%s: %s::%s: remote wake: LFPS started after %llums, duration %llums\n`
- `tunable_PIPE_HANDLER_HOST`
- `%s@%s: %s::%s: ATC_LINK_REGS_BLK_LLUCTL.FORCE_GEN1 = 0x%x\n`
- `tunable_BULK_FABRIC_DEFAULT`
- `%s@%s: %s::%s: skipping wait for resource %s\n`
- `121111121222121211211111222222222222222222222222222222222222222222222222222222222222222212121121111122222222222222221211222222222222222222222222222222222222222222222222212111111111222122222222222211222211112222211211111111111111111111111111111111111111111111111111111111111111111111111111111111111111`
- `tunable_CTLREG_DEFAULT`
- `AppleUSB20XHCIARMPort`
- `%s@%s: %s::%s: pong list head index %u\n`
- `121111121222121211211111222222222222222222222222222222222222222222222222222222222222222212121121111122222222222222221211222222222222222222222222222222222222222222222222212111111111222122222222222211222211112222211211111111111111111111111111111111111111111111111111111111111111111111111111111111111111`
- `tunable`
- `applySDBTunables`
- `systemPowerChangeThreadCall`
- `start`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_BEFORE_0_GCTL.GBL_HIBERNATION_EN = 0x%x\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_BEFORE_0_GCTL.PRTCAPDIR = 0x%x\n`
- `%s@%s: %s::%s: mode %d -> %d\n`
- `%s@%s: %s::%s: AUSBC_PWR_CTRL_BLK_HIBERNATION_ENABLE.INTR = 0x%x\n`
- `site.AppleSynopsysDRDUSBXHCI`
- `%s@%s: %s::%s: provider is not AppleUSBXHCIARM\n`
- `setUSB3Mode`
- `112`
- `%s@%s: %s::%s: tunable range %d offset 0x%08x invalid (rangeLength 0x%08llx)\n`
- `121111121222121211222222212222222222222222222222222222222222222222222222222221221111122221112112222222222211122112111111111111111112222112`
- `%s@%s: %s::%s: %s DCS power gating\n`
- `site.AppleT8030USBXHCI`
- `site.AppleT8160USBXHCI`
- `%s@%s: %s::%s: setPowerLevel or open failed with 0x%08x\n`
- `tunable_AUSBC_DEBUG_DEFAULT`
- `AppleT8027USBXHCICommandRing.cpp`
- `NULL`
- `site.AppleT8150USBXHCI`
- `site.AppleUSBXHCIARMEndpointSoftRetry`
- `%s@%s: %s::%s: failed to find USB3 protocol capability\n`
- `%s@%s: %s::%s: offset 0x%08x invalid (rangeLength 0x%08llx)\n`
- `UsbAllowSoftRetry`
- `AppleT8027USBXHCICommandRing`
- `site.AppleUSB30XHCIARMPort`
- `%s@%s: %s::%s: performance floor: high bandwidth\n`
- `%s@%s: %s::%s: RAM0_WR_ACTIVE is still set\n`
- `%s@%s: %s::%s: 0x%08x: forcing to kPowerStateOff\n`
- `%s@%s: %s::%s: couldn't find property %s\n`
- `AppleUSBRemovablePort-debug`
- `%s@%s: %s::%s: unable to get device memory\n`
- `%s@%s: %s::%s: AUSBC_PWR_CTRL_BLK_HIBERNATION_CFG.PM_POWER_STATE_REQ = 0x%x\n`
- `%s@%s: %s::%s: unexpected _mapperReferenceCount %u\n`
- `parrotSoftResetWorkaroundInit`
- `AppleT8101USBXHCI`
- `tunable_PWR_CTRL_DEFAULT`
- `inhibit`
- `AppleUSB30XHCIARMPort`
- `%s@%s: %s::%s: USB31DRD_PIPE_PHY_READY is not set\n`
- `%s@%s: %s::%s: tunable range %d invalid\n`
- `%s@%s: %s::%s: Tag not in device tree, continuing\n`
- `usb-port-number`
- `%s@%s: %s::%s: calling allowPowerChange\n`
- `%s@%s: %s::%s: offset 0x%05x = 0x%08x\n`
- `cableChangeOccurred`
- `%s@%s: %s::%s: function-vote_force_wakeup_dram not found\n`
- `%s@%s: %s::%s: couldn't find phy service\n`
- `AppleUSBHostPort`
- `%s@%s: %s::%s: failed to allocate _interruptSource[%d]\n`
- `created`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_CFG.CFG_ENABLE_RECIEVER_DETECT_OVERRIDE = 0x%x\n`
- `%s@%s: %s::%s: port %s@%s has companion port %s@%s for speed %d\n`
- `IOHibernateState`
- `AppleT8130USBXHCI.cpp`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.PIPE_HANDLER_REGS_FORCE_CLK_ON = 0x%x\n`
- `UsbTunnel`
- `%s@%s: %s::%s: failed to create _usb3ModeLock\n`
- `121111121222121211211111222222222222222222222222222222222222222222222222222222222222222212121121111122222222222222221211222222222222222222222222222222222222222222222222212111111111222122222222222211222211112222211211111111111111111111111111111111111111111111111111111111111111111111111111111111111111`
- `121211211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `%s: %s::%s: dummy mask 0x%08x context 0x%08x 0x%08x 0x%016llx 0x%08x\n`
- `Usb3Mode`
- `site.AppleT8101USBXHCI`
- `121111121222121211222222212222222222222222222222222222222222222222222222222221221111122221112112222222222211122112111111111111111112222`
- `AppleT8160USBXHCI`
- `%s@%s: %s::%s: USB31DRD_PIPE_PHY_READY is 0\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_VALUES0.PHYSTATUS_OVERRIDE_VALUE = 0x%x\n`
- `%s@%s: %s::%s: tunable range %d offset 0x%08x mask 0x%08x value 0x%08x already set (read 0x%08x)\n`
- `%s@%s: %s::%s: 0x%08x: restoring default power behavior\n`
- `%s@%s: %s::%s: performance floor: low bandwidth\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_HOST_CNTRL_PORT_REG_SET_PORTSC_30_REGS_PORTSC_30 = 0x%x\n`
- `%s@%s: %s::%s: port %u max link speed %u\n`
- `%s@%s: %s::%s: periodic list entry %u 0x%08x %08x %08x %08x %08x\n`
- `usb-repeater`
- `%s@%s: %s::%s: _powerControlInterrupt %s\n`
- `usb-host-skip-wait-resource`
- `AppleT8101USB20XHCILightningPort`
- `AppleUSBLightningPort-debug`
- `not created`
- `%s@%s: %s::%s: failed to build dictionary for %s\n`
- `%s: %s::%s: completed with result code %u\n`
- `%s@%s: %s::%s: TXDETRX_LOCK_ACK did not set\n`
- `port`
- `%s@%s: %s::%s: creating _pipeHandlerRegistersMap failed\n`
- `%s@%s: %s::%s: controller hardware is not available\n`
- `Failure`
- `%s: %s::%s: dropping and adding endpoint with separate commands\n`
- `%s@%s: %s::%s: floor bandwidth: %u safe bandwidth: %u\n`
- `reset`
- `11`
- `%s: %s::%s: target index %d context 0x%08x 0x%08x 0x%016llx 0x%08x\n`
- `%s@%s: %s::%s: performance floor: low isoch bandwidth\n`
- `%s@%s: %s::%s: TXDETRX_LOCK_ACK did not clear\n`
- `%s@%s: %s::%s: failed to enable USB3 phy\n`

**[__TEXT.__os_log]**

- `%s@%s: %s::%s: searching for port with locationID 0x%08x\n`
- `%s@%s: %s::%s: TXDETRX_LOCK_ACK did not clear\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_LOCK_PIPE_IF_REQ.LOCK_PIPE_IF_REQ = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PWR_CTRL_BLK_HIBERNATION_CFG.PM_POWER_STATE_REQ = 0x%x\n`
- `%s@%s: %s::%s: timed out waiting for SLEEP HIBERNATION_UNMASKED_STATUS 0x%08x HIBERNATION_STATUS 0x%08x\n`
- `%s@%s: %s::%s: \n`
- `%s@%s: %s::%s: start waiting for resource %s\n`
- `%s@%s: %s::%s: %s completed with 0x%08x\n`
- `%s@%s: %s::%s: DWC_USB31_BLOCK_GBL_GUSB2PHYCFG_REGS_GUSB2_PHYCFG.SUSPENDUSB20 = 0x%x\n`
- `%s@%s: %s::%s: failed to allocate _interruptSource[%d]\n`
- `%s@%s: %s::%s: _powerControlInterrupt %s\n`
- `%s@%s: %s::%s: unexpected LOCK_PIPE_IF_ACK 1\n`
- `%s@%s: %s::%s: DVFM_IF_BWR_AGENT_INTERFACE_AGENT_BWR = 0x%llx\n`
- `%s@%s: %s::%s: tunable range %d offset 0x%08x mask 0x%08x value 0x%08x (read 0x%08x wrote 0x%08x)\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE.NATIVE_POWER_DOWN = 0x%x\n`
- `%s@%s: %s::%s: failed to build dictionary for %s\n`
- `%s@%s: %s::%s: USB3 mode change\n`
- `%s@%s: %s::%s: failed to create or open AppleTypeCPhy session\n`
- `%s@%s: %s::%s: failed to create AppleTypeCPhy session\n`
- `%s@%s: %s::%s: unexpected transition from mode %d to %d\n`
- `%s@%s: %s::%s: tunable offset 0x%08x mask 0x%08x value 0x%08x (read 0x%08x wrote 0x%08x)\n`
- `%s@%s: %s::%s: _systemPowerChangeThread is already scheduled\n`
- `%s@%s: %s::%s: 0x%08x: forcing to kPowerStateOff\n`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.BULK_FABRIC_REGS_FORCE_CLK_ON = 0x%x\n`
- `%s@%s: %s::%s: failed to find phyService\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_BEFORE_0_GCTL.PWRDNSCALE = 0x%x\n`
- `%s: %s::%s: dummy mask 0x%08x context 0x%08x 0x%08x 0x%016llx 0x%08x\n`
- `%s@%s: %s::%s: provider is not AppleUSBXHCIARM\n`
- `%s@%s: %s::%s: failed to find USB3 protocol capability\n`
- `%s@%s: %s::%s: tunable range %d invalid\n`
- `%s@%s: %s::%s: offset 0x%08x invalid (rangeLength 0x%08llx)\n`
- `%s@%s: %s::%s: offset 0x%05x = 0x%08x\n`
- `%s: %s::%s: isochronous dummy endpoint mask 0x%08x -> 0x%08x\n`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.PIPE_HANDLER_REGS_FORCE_CLK_ON = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_AUSBC_AON_GENERAL_REGS.ATC_USB31_DRD_SW_VCC_RESET = 0x%x\n`
- `%s@%s: %s::%s: setPowerLevel failed with 0x%08x\n`
- `%s@%s: %s::%s: %s completed with 0x%08x (%d attempts)\n`
- `%s@%s: %s::%s: DWC_USB31_BLOCK_GBL_GUSB3PIPECTL_REGS_GUSB3_PIPECTL.SUSPENDENABLE = 0x%x\n`
- `%s: %s::%s: fallback aborted\n`
- `%s@%s: %s::%s: sleep power loss\n`
- `%s@%s: %s::%s: USB31DRD_PIPE_PHY_READY is not set\n`
- `%s@%s: %s::%s: failed to create _usb3ModeLock\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_BEFORE_0_GCTL.GBL_HIBERNATION_EN = 0x%x\n`
- `%s@%s: %s::%s: %s matching has been disabled\n`
- `%s@%s: %s::%s: skipping wait for resource %s\n`
- `%s@%s: %s::%s: %s DCS power gating\n`
- `%s@%s: %s::%s: AUSBC_PWR_CTRL_BLK_TXDETRX_LOCK_REQ.FLD = 0x%x\n`
- `%s@%s: %s::%s: timed out waiting for VVDD_USB_OFF interrupt HIBERNATION_UNMASKED_STATUS 0x%08x HIBERNATION_STATUS 0x%08x\n`
- `%s@%s: %s::%s: regIndex %d invalid, failed to apply tunable tag '%s'\n`
- `%s@%s: %s::%s: TXDETRX_LOCK_ACK did not set\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_CFG.CFG_ENABLE_RECIEVER_DETECT_OVERRIDE = 0x%x\n`
- `%s@%s: %s::%s: ATC_LINK_REGS_BLK_LLUCTL.FORCE_GEN1 = 0x%x\n`
- `%s@%s: %s::%s: tunable offset 0x%08x mask 0x%08x value 0x%08x already set (read 0x%08x)\n`
- `%s@%s: %s::%s: calling allowPowerChange\n`
- `%s@%s: %s::%s: couldn't find property %s\n`
- `%s: %s::%s: fallback completed with result code %u\n`
- `%s@%s: %s::%s: performance floor: low bandwidth\n`
- `%s: %s::%s: target index %d context 0x%08x 0x%08x 0x%016llx 0x%08x\n`
- `%s@%s: %s::%s: unable to get device memory\n`
- `%s: %s::%s: completed with result code %u\n`
- `%s@%s: %s::%s: creating _ctlRegistersMap failed\n`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.DEBUG_WRAP_REGS_FORCE_CLK_ON = 0x%x\n`
- `%s@%s: %s::%s: mode %d -> %d\n`
- `%s@%s: %s::%s: controller hardware is not available\n`
- `%s@%s: %s::%s: waiting for resource %s, result %s\n`
- `%s@%s: %s::%s: pong list head index %u\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_HOST_CNTRL_PORT_REG_SET_PORTSC_30_REGS_PORTSC_30 = 0x%x\n`
- `%s@%s: %s::%s: PMC disabled via boot arg\n`
- `%s@%s: %s::%s: RAM0_WR_ACTIVE is still set\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_VALUES0.RECIEVER_DETECT_OVERRIDE_VALUE = 0x%x\n`
- `%s@%s: %s::%s: port %u max link speed %u\n`
- `%s@%s: %s::%s: 0x%08x: restoring default power behavior\n`
- `%s@%s: %s::%s: unknown speed\n`
- `%s@%s: %s::%s: creating _powerControlRegistersMap failed\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_PHY_MUX_SELECT.PIPE_CLK_EN = 0x%x\n`
- `%s: %s::%s: slot %u endpoint %u\n`
- `%s: %s::%s: slot context 0x%08x 0x%08x 0x%08x 0x%08x\n`
- `%s@%s: %s::%s: creating _configRegistersMap failed\n`
- `%s@%s: %s::%s: hibernate power loss\n`
- `%s@%s: %s::%s: DWC_USB31_BLOCK_GBL_BEFORE_0_GCTL.PRTCAPDIR = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE.DUMMY_PHY_READY = 0x%x\n`
- `%s@%s: %s::%s: in bandwidth: %u KB/µFrame, out bandwidth: %u KB/µFrame\n`
- `%s@%s: %s::%s: tunable range %d offset 0x%08x mask 0x%08x value 0x%08x already set (read 0x%08x)\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_VALUES0.PHYSTATUS_OVERRIDE_VALUE = 0x%x\n`
- `%s@%s: %s::%s: Applying tunable tag '%s' (block offset 0x%08x)\n`
- `%s@%s: %s::%s: found companion controller %p (%s) for speed %d\n`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.CFG_USB2PHY_REGS_FORCE_CLK_ON = 0x%x\n`
- `%s@%s: %s::%s: PIPE_HANDLER_LOCK_PIPE_IF_ACK did not set\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE.NATIVE_RESET = 0x%x\n`
- `%s@%s: %s::%s: failed to enable USB2 phy\n`
- `%s@%s: %s::%s: failed to enable USB3 phy\n`
- `%s@%s: %s::%s: port %d USB 2.%x with %d speed IDs\n`
- `%s@%s: %s::%s: port %d unsupported protocol %s %x.%x\n`
- `%s: %s::%s: unable to assign %d dummy endpoints (mask 0x%08x)\n`
- `%s: %s::%s: aborted\n`
- `%s@%s: %s::%s: remote wake: LFPS started after %llums, duration %llums\n`
- `%s@%s: %s::%s: ping list head index %u\n`
- `%s: %s::%s: command with dummy endpoint failed, attempting to configure without dummy endpoint\n`
- `%s: %s::%s: drop dummy endpoint mask 0x%08x\n`
- `%s@%s: %s::%s: performance floor: high bandwidth\n`
- `%s@%s: %s::%s: creating _pmcBWRRegistersMap failed\n`
- `%s@%s: %s::%s: setPowerLevel or open failed with 0x%08x\n`
- `%s@%s: %s::%s: failed to enable phy\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_GUSB3PIPECTL_REGS_GUSB3_PIPECTL.SUSPENDENABLE = 0x%x\n`
- `%s@%s: %s::%s: PIPE_HANDLER_LOCK_PIPE_IF_ACK did not clear\n`
- `%s@%s: %s::%s: port %d USB 3.%x with %d speed IDs\n`
- `%s@%s: %s::%s: couldn't find phy service\n`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.DRD_TOP_REGS_FORCE_CLK_ON = 0x%x\n`
- `%s@%s: %s::%s: floor bandwidth: %u safe bandwidth: %u\n`
- `%s@%s: %s::%s: creating _coreEvtRegistersMap failed\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_GUSB2PHYCFG_REGS_GUSB2_PHYCFG.SUSPENDUSB20 = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_CFG.ENABLE_RXVALID_OVERRIDE = 0x%x\n`
- `%s@%s: %s::%s: port %d is not a USB3 port\n`
- `%s@%s: %s::%s: tunable range %d offset 0x%08x invalid (rangeLength 0x%08llx)\n`
- `%s@%s: %s::%s: copyMapperForDevice() failed\n`
- `%s@%s: %s::%s: AUSBC_PWR_CTRL_BLK_HIBERNATION_ENABLE.INTR = 0x%x\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_HOST_CNTRL_PORT_REG_SET_PORTSC_30_REGS_PORTSC_30.PP = 0x%x\n`
- `%s@%s: %s::%s: port %s@%s has companion port %s@%s for speed %d\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_BEFORE_2_GUCTL6 = 0x%x\n`
- `%s@%s: %s::%s: failed to find %s for %s\n`
- `%s@%s: %s::%s: periodic list entry %u 0x%08x %08x %08x %08x %08x\n`
- `%s: %s::%s: dropping and adding endpoint with separate commands\n`
- `%s@%s: %s::%s: performance floor: low isoch bandwidth\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_BEFORE_0_GCTL.PRTCAPDIR = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PWR_CTRL_BLK_HIBERNATION_CLEAR.INTR = 0x%x\n`
- `%s@%s: %s::%s: failed to attach or start port %d\n`
- `%s: %s::%s: hardware is unavailable\n`
- `%s@%s: %s::%s: performance floor: none\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_PHY_MUX_SELECT.PIPE_MODE = 0x%x\n`
- `%s@%s: %s::%s: timed out waiting for D0_ON interrupt HIBERNATION_UNMASKED_STATUS 0x%08x HIBERNATION_STATUS 0x%08x\n`
- `%s@%s: %s::%s: Tag not in device tree, continuing\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_AUSBC_AON_GENERAL_REGS.ATC_USB31_DRD_FORCE_CLAMP_EN = 0x%x\n`
- `%s: %s::%s: forcing endpoint interval from %d uFrames to %d uFrames\n`
- `%s@%s: %s::%s: %lu\n`
- `%s@%s: %s::%s: creating _pipeHandlerRegistersMap failed\n`
- `%s@%s: %s::%s: function-vote_force_wakeup_dram not found\n`
- `%s@%s: %s::%s: USB31DRD_PIPE_PHY_READY is 0\n`
- `%s@%s: %s::%s: unexpected _mapperReferenceCount %u\n`
