# `com.apple.driver.usb.AppleSynopsysUSB40XHCI`

- Name: AppleSynopsysUSB40XHCI
- Version: `1`
- UUID: `65787E54-95F4-3D56-BE0C-8C1DA2BB1546`
- Source version: `717.40.5.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleEmbeddedUSBHost`](com.apple.driver.AppleEmbeddedUSBHost.md) 1.0, [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](com.apple.driver.usb.AppleSynopsysUSBXHCI.md) 1.0, [`com.apple.driver.usb.AppleUSBCommon`](com.apple.driver.usb.AppleUSBCommon.md) 1.0, [`com.apple.driver.usb.AppleUSBXHCI`](com.apple.driver.usb.AppleUSBXHCI.md) 1.2, [`com.apple.iokit.IOAccessoryManager`](com.apple.iokit.IOAccessoryManager.md) 1.0.0, [`com.apple.iokit.IOPortFamily`](com.apple.iokit.IOPortFamily.md) 1.0, [`com.apple.iokit.IOThunderboltFamily`](com.apple.iokit.IOThunderboltFamily.md) 1.0.0, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.2, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 15.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 15.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 15.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 15.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 16.5.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 15.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (7) [KC]

### AppleT6000USBXHCI
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleSynopsysUSB40XHCI`
- `IOClass`: `AppleT6000USBXHCI`
- `IOMatchCategory`: `usb-host`
- `IONameMatch`: `usb-drd,t6000`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleSynopsysUSB40XHCI`
- `IOProbeScore`: `10002`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8103USBXHCI
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleSynopsysUSB40XHCI`
- `IOClass`: `AppleT8103USBXHCI`
- `IOMatchCategory`: `usb-host`
- `IONameMatch`: `usb-drd,t8103`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleSynopsysUSB40XHCI`
- `IOProbeScore`: `10001`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8112USBXHCI
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleSynopsysUSB40XHCI`
- `IOClass`: `AppleT8112USBXHCI`
- `IOMatchCategory`: `usb-host`
- `IONameMatch`: `usb-drd,t8112`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleSynopsysUSB40XHCI`
- `IOProbeScore`: `10000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8122USBXHCI
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleSynopsysUSB40XHCI`
- `IOClass`: `AppleT8122USBXHCI`
- `IOMatchCategory`: `usb-host`
- `IONameMatch`: `usb-drd,t8122`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleSynopsysUSB40XHCI`
- `IOProbeScore`: `10001`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8132USBXHCI
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleSynopsysUSB40XHCI`
- `IOClass`: `AppleT8132USBXHCI`
- `IOMatchCategory`: `usb-host`
- `IONameMatch`: `usb-drd,t8132`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleSynopsysUSB40XHCI`
- `IOProbeScore`: `10001`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8142USBXHCI
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleSynopsysUSB40XHCI`
- `IOClass`: `AppleT8142USBXHCI`
- `IOMatchCategory`: `usb-host`
- `IONameMatch`: `usb-drd,t8142`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleSynopsysUSB40XHCI`
- `IOProbeScore`: `10001`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8152USBXHCI
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleSynopsysUSB40XHCI`
- `IOClass`: `AppleT8152USBXHCI`
- `IOMatchCategory`: `usb-host`
- `IONameMatch`: `usb-drd,t8152`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleSynopsysUSB40XHCI`
- `IOProbeScore`: `10001`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (15) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleT6000USBXHCI` | 0x1030 | AppleT8103USBXHCI → AppleSynopsysDRDUSBXHCI → AppleUSBXHCIARM → AppleUSBXHCI → AppleUSBHostController → IOService → IORegistryEntry |
| `AppleT6000USBXHCICommandRing` | 0x1870 | AppleSynopsysDRDUSBXHCICommandRing → AppleUSBXHCICommandRing |
| `AppleT8103USB30XHCIPort` | 0x440 | AppleUSB30XHCIARMPort → AppleUSB30XHCITypeCPort → AppleUSB30XHCIPort → AppleUSBXHCIPort → AppleUSBHostPort → IOService → IORegistryEntry |
| `AppleT8103USBXHCI` | 0x1030 | AppleSynopsysDRDUSBXHCI → AppleUSBXHCIARM → AppleUSBXHCI → AppleUSBHostController → IOService → IORegistryEntry |
| `AppleT8103USBXHCICommandRing` | 0x1870 | AppleSynopsysDRDUSBXHCICommandRing → AppleUSBXHCICommandRing |
| `AppleT8112USBXHCI` | 0x1008 | AppleUSBXHCIARM → AppleUSBXHCI → AppleUSBHostController → IOService → IORegistryEntry |
| `AppleT8112USBXHCICommandRing` | 0x1868 | AppleUSBXHCICommandRing |
| `AppleT8122USBXHCI` | 0x1008 | AppleUSBXHCIARM → AppleUSBXHCI → AppleUSBHostController → IOService → IORegistryEntry |
| `AppleT8122USBXHCICommandRing` | 0x1868 | AppleUSBXHCICommandRing |
| `AppleT8132USBXHCI` | 0xff8 | AppleUSBXHCIARM → AppleUSBXHCI → AppleUSBHostController → IOService → IORegistryEntry |
| `AppleT8132USBXHCICommandRing` | 0x1868 | AppleUSBXHCICommandRing |
| `AppleT8142USBXHCI` | 0x1008 | AppleUSBXHCIARM → AppleUSBXHCI → AppleUSBHostController → IOService → IORegistryEntry |
| `AppleT8142USBXHCICommandRing` | 0x1868 | AppleUSBXHCICommandRing |
| `AppleT8152USBXHCI` | 0x1008 | AppleUSBXHCIARM → AppleUSBXHCI → AppleUSBHostController → IOService → IORegistryEntry |
| `AppleT8152USBXHCICommandRing` | 0x1868 | AppleUSBXHCICommandRing |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00012738 off=0x00b2ec90-0x00b413c8 addr=0xfffffe0007b32c90-0xfffffe0007b453c8 r--/r--   __TEXT            
	sz=0x00002eb1 off=0x00b2f358-0x00b32209 addr=0xfffffe0007b33358-0xfffffe0007b36209               __TEXT.__cstring          (CstringLiterals)
	sz=0x0000f1b4 off=0x00b32209-0x00b413bd addr=0xfffffe0007b36209-0xfffffe0007b453bd               __TEXT.__os_log           
	sz=0x00000008 off=0x00b413c0-0x00b413c8 addr=0xfffffe0007b453c0-0xfffffe0007b453c8               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x0006d750 off=0x03730a80-0x0379e1d0 addr=0xfffffe000a734a80-0xfffffe000a7a21d0 r-x/r-x   __TEXT_EXEC       
	sz=0x0006d460 off=0x03730a80-0x0379dee0 addr=0xfffffe000a734a80-0xfffffe000a7a1ee0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000002f0 off=0x0379dee0-0x0379e1d0 addr=0xfffffe000a7a1ee0-0xfffffe000a7a21d0          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000360 off=0x04a1b4a0-0x04a1b800 addr=0xfffffe000ba1f4a0-0xfffffe000ba1f800 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a1b4a0-0x04a1b568 addr=0xfffffe000ba1f4a0-0xfffffe000ba1f568               __DATA.__data             
	sz=0x00000268 off=0x00000000-0x00000268 addr=0xfffffe000ba1f568-0xfffffe000ba1f7d0               __DATA.__common           (Zerofill)
	sz=0x00000030 off=0x00000000-0x00000030 addr=0xfffffe000ba1f7d0-0xfffffe000ba1f800               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00006e48 off=0x014510a8-0x01457ef0 addr=0xfffffe00084550a8-0xfffffe000845bef0 rw-/rw-   __DATA_CONST      
	sz=0x00000078 off=0x014510a8-0x01451120 addr=0xfffffe00084550a8-0xfffffe0008455120         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000078 off=0x01451120-0x01451198 addr=0xfffffe0008455120-0xfffffe0008455198         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000065f8 off=0x01451198-0x01457790 addr=0xfffffe0008455198-0xfffffe000845b790         __DATA_CONST.__const            
	sz=0x00000540 off=0x01457790-0x01457cd0 addr=0xfffffe000845b790-0xfffffe000845bcd0         __DATA_CONST.__kalloc_type      
	sz=0x00000178 off=0x01457cd0-0x01457e48 addr=0xfffffe000845bcd0-0xfffffe000845be48         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000a8 off=0x01457e48-0x01457ef0 addr=0xfffffe000845be48-0xfffffe000845bef0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 115 at 0x04afa638
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     65787E54-95F4-3D56-BE0C-8C1DA2BB1546
008: LC_SOURCE_VERSION           717.40.5.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac9948 size=0x2d0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleSynopsysUSB40XHCI`
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleSynopsysUSB40XHCI`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSynopsysUSB40XHCI`
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
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/AppleSynopsysUSB40XHCI.kext`
- `_PrelinkExecutableLoadAddr`: `-2198894072688`
- `_PrelinkExecutableRelativePath`: `AppleSynopsysUSB40XHCI`
- `_PrelinkExecutableSize`: `553008`
- `_PrelinkExecutableSourceAddr`: `-2198894072688`
- `_PrelinkKmodInfo`: `-2198828092256`

## Strings (284) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%s@%s: %s::%s: TXDETRX_LOCK_ACK did not clear\n`
- `%s@%s: %s::%s: ATC_LINK_REGS_BLK_LLUCTL.FORCE_GEN1 = 0x%x\n`
- `%s@%s: %s::%s: performance floor: none\n`
- `warmReset`
- `AppleT6000USBXHCICommandRing`
- `site.AppleT8122USBXHCICommandRing`
- `AppleT8103USBXHCI.cpp`
- `%s@%s: %s::%s: unexpected LOCK_PIPE_IF_ACK 1\n`
- `%s@%s: %s::%s: failed to create _usb3ModeLock\n`
- `%s@%s: %s::%s: CIO_REGS_BLK_CIOLFPSOFFSET.AP_LFPS_OFFSET = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PWR_CTRL_BLK_HIBERNATION_ENABLE.INTR = 0x%x\n`
- `AppleT8142USBXHCICommandRing`
- `AppleT8112USBXHCICommandRing`
- `%s@%s: %s::%s: CIO_REGS_BLK_CIOBWNGTOFFSET.MAC_BW_NGT_OFFSET = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE.DUMMY_PHY_READY = 0x%x\n`
- `%s@%s: %s::%s: refusing to power on due to pending hardware exception\n`
- `powerControlInterrupt`
- `tunable_DRD_USB31_GBL_HOST`
- `%s@%s: %s::%s: creating _pmcBWRRegistersMap failed\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PWR_CTRL_BLK_HIBERNATION_CLEAR.INTR = 0x%x\n`
- `121111121222121211211111222222222222222222222222222222222222222222222222222222222222222212121121111122222222222222221211222222222222222222222222222222222222222222222222212111111111222122222222222211222211112222211211111111111111111111111111111111111111111111111111111111111111111111111111111111111111`
- `inhibit`
- `updateEndpoint`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_GUSB3PIPECTL_REGS_GUSB3_PIPECTL.SUSPENDENABLE = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PWR_CTRL_BLK_TXDETRX_LOCK_REQ.FLD = 0x%x\n`
- `%s@%s: %s::%s: timed out waiting for SLEEP HIBERNATION_UNMASKED_STATUS 0x%08x HIBERNATION_STATUS 0x%08x\n`
- `%s@%s: %s::%s: performance floor: high bandwidth\n`
- `AppleT8132USBXHCICommandRing`
- `IOTBTTunnelClientInterfaceManager`
- `%s@%s: %s::%s: did not find cioService, tunneled USB is not supported\n`
- `%s@%s: %s::%s: setPowerLevel failed with 0x%08x\n`
- `%s@%s: %s::%s: failed to enable USB2 phy\n`
- `AppleT8122USBXHCI.cpp`
- `%s@%s: %s::%s: creating _ctlRegistersMap failed\n`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.DRD_TOP_REGS_FORCE_CLK_ON = 0x%x\n`
- `allow`
- ` @%s:%d`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_PHY_MUX_SELECT.PIPE_CLK_EN = 0x%x\n`
- `%s@%s: %s::%s: controller hardware is not available\n`
- `site.AppleT8132USBXHCICommandRing`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.CFG_USB2PHY_REGS_FORCE_CLK_ON = 0x%x\n`
- `site.AppleT6000USBXHCICommandRing`
- `AppleT8152USBXHCICommandRing`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_HOST_CNTRL_PORT_REG_SET_PORTSC_30_REGS_PORTSC_30 = 0x%x\n`
- `getPeriodicBandwidthUsage`
- `AppleT8132USBXHCI`
- `%s@%s: %s::%s: performance floor: low bandwidth\n`
- `%s@%s: %s::%s: failed to create CIO session\n`
- `%s@%s: %s::%s: CIO_REGS_BLK_CIOLINKTIM1.PM_LC_TIMER = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_CFG.CFG_ENABLE_RECIEVER_DETECT_OVERRIDE = 0x%x\n`
- `%s@%s: %s::%s: PIPE_HANDLER_LOCK_PIPE_IF_ACK did not set\n`
- `%s@%s: %s::%s: timed out waiting for VVDD_USB_OFF interrupt HIBERNATION_UNMASKED_STATUS 0x%08x HIBERNATION_STATUS 0x%08x\n`
- `tunable_PIPE_HANDLER_DEFAULT`
- `tunable_PWR_CTRL_DEFAULT`
- `tunable_DRD_USB31_DBG_DEFAULT`
- `%s: %s::%s: forcing endpoint interval from %d uFrames to %d uFrames\n`
- `reset`
- `%s@%s: %s::%s: mode %d -> %d\n`
- `%s@%s: %s::%s: floor bandwidth: %u safe bandwidth: %u\n`
- `%s@%s: %s::%s: failed to enable phy\n`
- `%s@%s: %s::%s: applied errata for RxDetect issue (rdar://problem/64584969)\n`
- `AppleT6000USBXHCI`
- `start`
- `%s@%s: %s::%s: failed to create AppleTypeCPhy session\n`
- `setUSB3Mode`
- `updateSystemPowerManagement`
- `AppleT8103USBXHCI`
- `usbdrd-disablepmcbwr`
- `%s@%s: %s::%s: powerFloor.startSession(kPowerStateSuspended) failed with 0x%08x\n`
- `121211211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_BEFORE_0_GCTL.GBL_HIBERNATION_EN = 0x%x\n`
- `tunable_BULK_FABRIC_DEFAULT`
- `applyAllTunables`
- `112`
- `121111121222121211211111222222222222222222222222222222222222222222222222222222222222222212121121111122222222222222221211222222222222222222222222222222222222222222222222212111111111222122222222222211222211112222211211111111111111111111111111111111111111111111111111111111111111111111111111111111111111`
- `AppleT8142USBXHCI.cpp`
- `UsbHostControllerDeferRegisterService`
- `%s@%s: %s::%s: startUsingTunnel failed with 0x%08x\n`
- `tunable_AUSBC_DEBUG_DEFAULT`
- `site.T`
- `LinkInactiveReason`
- `%s@%s: %s::%s: USB31DRD_PIPE_PHY_READY is 0\n`
- `requestUSB3Mode`
- `%s@%s: %s::%s: unexpected transition from mode %d to %d\n`
- `AppleT8142USBXHCI`
- `%s@%s: %s::%s: timed out waiting for D0_ON interrupt HIBERNATION_UNMASKED_STATUS 0x%08x HIBERNATION_STATUS 0x%08x\n`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.PIPE_HANDLER_REGS_FORCE_CLK_ON = 0x%x\n`
- `%s@%s: %s::%s: PIPE_HANDLER didn't power down\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_CFG.ENABLE_RXVALID_OVERRIDE = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_LOCK_PIPE_IF_REQ.LOCK_PIPE_IF_REQ = 0x%x\n`
- `%s@%s: %s::%s: in bandwidth: %u KB/µFrame, out bandwidth: %u KB/µFrame\n`
- `tunable_LINK_REGS_DEFAULT`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.BULK_FABRIC_REGS_FORCE_CLK_ON = 0x%x\n`
- `site.AppleT8152USBXHCICommandRing`
- `%s@%s: %s::%s: creating _coreEvtRegistersMap failed\n`
- `%s@%s: %s::%s: failed to enable USB3 phy\n`
- `tunable_PIPE_HANDLER_HOST`
- `site.AppleT8132USBXHCI`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.DEBUG_WRAP_REGS_FORCE_CLK_ON = 0x%x\n`
- `site.AppleT8103USBXHCI`
- `%s@%s: %s::%s: creating _pipeHandlerRegistersMap failed\n`
- `%s@%s: %s::%s: CIO_REGS_BLK_CIOLFPSOFFSET.MAC_LFPS_OFFSET = 0x%x\n`
- `%s@%s: %s::%s: RAM0_WR_ACTIVE is still set\n`
- `tunable_DRD_CIO_REGS_DEFAULT`
- `AppleT8132USBXHCI.cpp`
- `site.AppleT8122USBXHCI`
- `tunable_CTLREG_DEFAULT`
- `1211111212221212112222222122222222222222222222222222222222222222222222222222212211111222211121122222222222111221121111111111111111122211`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_BEFORE_0_GCTL.PRTCAPDIR = 0x%x\n`
- `%s@%s: %s::%s: PIPE_HANDLER_LOCK_PIPE_IF_ACK did not clear\n`
- `tunable`
- `121111121222121211211111222222222222222222222222222222222222222222222222222222222222222212121121111122222222222222221211222222222222222222222222222222222222222222222222212111111111222122222222222211222211112222211211111111111111111111111111111111111111111111111111111111111111111111111111111111111111`
- `%s@%s: %s::%s: CIO_REGS_BLK_CIOLINKTIM1.PENDING_HP_TIMER = 0x%x\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_HOST_CNTRL_PORT_REG_SET_PORTSC_30_REGS_PORTSC_30.PP = 0x%x\n`
- `AppleT8122USBXHCI`
- `%s@%s: %s::%s: port %d is not a USB3 port\n`
- `site.AppleT6000USBXHCI`
- `%s@%s: %s::%s: unable to get device memory\n`
- `%s@%s: %s::%s: TXDETRX_LOCK_ACK did not set\n`
- `%s@%s: %s::%s: setPowerLevel or open failed with 0x%08x\n`
- `%s@%s: %s::%s: remote wake: LFPS started after %llums, duration %llums\n`
- `%s@%s: %s::%s: port %u max link speed %u\n`
- `setMaximumPortLinkSpeed_block_invoke`
- `i8@?0`
- `%s@%s: %s::%s: clientWillWake failed with 0x%08x\n`
- `%s@%s: %s::%s: PIPE_HANDLER_NON_SELECTED_OVERRIDE did not set\n`
- `tunable_DRD_USB31_CFG_HOST`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_BEFORE_2_GUCTL6 = 0x%x\n`
- `11`
- `AppleT8152USBXHCI`
- `AppleT8112USBXHCI`
- `atc-phy-parent`
- `AppleTypeCPhy`
- `%s@%s: %s::%s: _cioSession does not exist, tunneled USB is not supported\n`
- `site.AppleT8112USBXHCI`
- `121111121222121211211111222222222222222222222222222222222222222222222222222222222222222212121121111122222222222222221211222222222222222222222222222222222222222222222222212111111111222122222222222211222211112222211211111111111111111111111111111111111111111111111111111111111111111111111111111111111111`
- `IOHibernateState`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_AUSBC_AON_GENERAL_REGS.ATC_USB31_DRD_FORCE_CLAMP_EN = 0x%x\n`
- `created`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_VALUES0.RECIEVER_DETECT_OVERRIDE_VALUE = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_VALUES0.PHYSTATUS_OVERRIDE_VALUE = 0x%x\n`
- `site.AppleT8142USBXHCICommandRing`
- `%s@%s: %s::%s: failed to create or open AppleTypeCPhy session\n`
- `%s@%s: %s::%s: failed to allocate _interruptSource[%d]\n`
- `%s@%s: %s::%s: _powerControlInterrupt %s\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_BEFORE_0_GCTL.PWRDNSCALE = 0x%x\n`
- `%s@%s: %s::%s: unexpected LOCK_PIPE_IF_ACK\n`
- `%s@%s: %s::%s: AUSBC_PWR_CTRL_BLK_HIBERNATION_CFG.PM_POWER_STATE_REQ = 0x%x\n`
- `site.AppleT8103USBXHCICommandRing`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_GUSB3PIPECTL_REGS_GUSB3_PIPECTL.PHY_SOFT_RST = 0x%x\n`
- `%s@%s: %s::%s: CIO_REGS_BLK_CIOBWNGTOFFSET.AP_BW_NGT_OFFSET = 0x%x\n`
- `%s@%s: %s::%s: CIO_REGS_BLK_CIOLINKTIM1.PM_ENTRY_TIMER = 0x%x\n`
- `%s@%s: %s::%s: \n`
- `tunable_DRD_USB31_GBL_DEFAULT`
- `%s@%s: %s::%s: %s DCS power gating\n`
- `AppleT8103USB30XHCIPort`
- `site.AppleT8142USBXHCI`
- `%s@%s: %s::%s: failed to find phyService\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_GUSB2PHYCFG_REGS_GUSB2_PHYCFG.SUSPENDUSB20 = 0x%x\n`
- `AppleT8103USBXHCICommandRing`
- `site.AppleT8152USBXHCI`
- `AppleT8112USBXHCI.cpp`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE.NATIVE_POWER_DOWN = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE.NATIVE_RESET = 0x%x\n`
- `kUSBSleepSupported`
- `121211211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `%s@%s: %s::%s: copyMapperForDevice() failed\n`
- `AppleT8122USBXHCICommandRing`
- `site.AppleT8112USBXHCICommandRing`
- `applySSInactiveErrata`
- `%s@%s: %s::%s: creating _configRegistersMap failed\n`
- `AppleUSBXHCICommandRing`
- `addEndpoint`
- `acio-parent`
- `%s@%s: %s::%s: DVFM_IF_BWR_AGENT_INTERFACE_AGENT_BWR = 0x%llx\n`
- `AppleT8152USBXHCI.cpp`
- `%s@%s: %s::%s: performance floor: low isoch bandwidth\n`
- `site.AppleT8103USB30XHCIPort`
- `%s@%s: %s::%s: creating _powerControlRegistersMap failed\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_AUSBC_AON_GENERAL_REGS.ATC_USB31_DRD_SW_VCC_RESET = 0x%x\n`
- `not created`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_PHY_MUX_SELECT.PIPE_MODE = 0x%x\n`
- `setPowerStateGated`
- `%s@%s: %s::%s: %lu\n`
- `raiseOnePowerStateTo`
- `%s@%s: %s::%s: failed to find USB3 protocol capability\n`

**[__TEXT.__os_log]**

- `%s@%s: %s::%s: TXDETRX_LOCK_ACK did not clear\n`
- `%s@%s: %s::%s: PIPE_HANDLER_NON_SELECTED_OVERRIDE did not set\n`
- `%s@%s: %s::%s: PIPE_HANDLER didn't power down\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_GUSB3PIPECTL_REGS_GUSB3_PIPECTL.PHY_SOFT_RST = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE.DUMMY_PHY_READY = 0x%x\n`
- `%s@%s: %s::%s: _cioSession does not exist, tunneled USB is not supported\n`
- `%s@%s: %s::%s: \n`
- `%s@%s: %s::%s: port %d is not a USB3 port\n`
- `%s@%s: %s::%s: failed to create or open AppleTypeCPhy session\n`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.PIPE_HANDLER_REGS_FORCE_CLK_ON = 0x%x\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_GUSB3PIPECTL_REGS_GUSB3_PIPECTL.SUSPENDENABLE = 0x%x\n`
- `%s@%s: %s::%s: failed to create _usb3ModeLock\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_PHY_MUX_SELECT.PIPE_CLK_EN = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.CFG_USB2PHY_REGS_FORCE_CLK_ON = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PWR_CTRL_BLK_TXDETRX_LOCK_REQ.FLD = 0x%x\n`
- `%s@%s: %s::%s: unexpected LOCK_PIPE_IF_ACK\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_CFG.ENABLE_RXVALID_OVERRIDE = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PWR_CTRL_BLK_HIBERNATION_CFG.PM_POWER_STATE_REQ = 0x%x\n`
- `%s@%s: %s::%s: powerFloor.startSession(kPowerStateSuspended) failed with 0x%08x\n`
- `%s@%s: %s::%s: PIPE_HANDLER_LOCK_PIPE_IF_ACK did not clear\n`
- `%s@%s: %s::%s: creating _powerControlRegistersMap failed\n`
- `%s@%s: %s::%s: creating _pmcBWRRegistersMap failed\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_AUSBC_AON_GENERAL_REGS.ATC_USB31_DRD_FORCE_CLAMP_EN = 0x%x\n`
- `%s@%s: %s::%s: PIPE_HANDLER_LOCK_PIPE_IF_ACK did not set\n`
- `%s@%s: %s::%s: in bandwidth: %u KB/µFrame, out bandwidth: %u KB/µFrame\n`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.DRD_TOP_REGS_FORCE_CLK_ON = 0x%x\n`
- `%s@%s: %s::%s: failed to enable phy\n`
- `%s@%s: %s::%s: CIO_REGS_BLK_CIOLFPSOFFSET.AP_LFPS_OFFSET = 0x%x\n`
- `%s@%s: %s::%s: CIO_REGS_BLK_CIOLINKTIM1.PM_LC_TIMER = 0x%x\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_BEFORE_0_GCTL.GBL_HIBERNATION_EN = 0x%x\n`
- `%s@%s: %s::%s: creating _coreEvtRegistersMap failed\n`
- `%s@%s: %s::%s: failed to create CIO session\n`
- `%s@%s: %s::%s: unable to get device memory\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_CFG.CFG_ENABLE_RECIEVER_DETECT_OVERRIDE = 0x%x\n`
- `%s@%s: %s::%s: remote wake: LFPS started after %llums, duration %llums\n`
- `%s@%s: %s::%s: CIO_REGS_BLK_CIOBWNGTOFFSET.AP_BW_NGT_OFFSET = 0x%x\n`
- `%s@%s: %s::%s: startUsingTunnel failed with 0x%08x\n`
- `%s@%s: %s::%s: AUSBC_PWR_CTRL_BLK_HIBERNATION_ENABLE.INTR = 0x%x\n`
- `%s@%s: %s::%s: %lu\n`
- `%s@%s: %s::%s: refusing to power on due to pending hardware exception\n`
- `%s@%s: %s::%s: port %u max link speed %u\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_BEFORE_2_GUCTL6 = 0x%x\n`
- `%s@%s: %s::%s: creating _ctlRegistersMap failed\n`
- `%s@%s: %s::%s: CIO_REGS_BLK_CIOLINKTIM1.PENDING_HP_TIMER = 0x%x\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_BEFORE_0_GCTL.PRTCAPDIR = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_LOCK_PIPE_IF_REQ.LOCK_PIPE_IF_REQ = 0x%x\n`
- `%s@%s: %s::%s: timed out waiting for VVDD_USB_OFF interrupt HIBERNATION_UNMASKED_STATUS 0x%08x HIBERNATION_STATUS 0x%08x\n`
- `%s@%s: %s::%s: ATC_LINK_REGS_BLK_LLUCTL.FORCE_GEN1 = 0x%x\n`
- `%s@%s: %s::%s: %s DCS power gating\n`
- `%s@%s: %s::%s: CIO_REGS_BLK_CIOLINKTIM1.PM_ENTRY_TIMER = 0x%x\n`
- `%s@%s: %s::%s: clientWillWake failed with 0x%08x\n`
- `%s@%s: %s::%s: setPowerLevel or open failed with 0x%08x\n`
- `%s@%s: %s::%s: performance floor: low bandwidth\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE.NATIVE_RESET = 0x%x\n`
- `%s: %s::%s: forcing endpoint interval from %d uFrames to %d uFrames\n`
- `%s@%s: %s::%s: creating _configRegistersMap failed\n`
- `%s@%s: %s::%s: USB31DRD_PIPE_PHY_READY is 0\n`
- `%s@%s: %s::%s: mode %d -> %d\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_VALUES0.RECIEVER_DETECT_OVERRIDE_VALUE = 0x%x\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_HOST_CNTRL_PORT_REG_SET_PORTSC_30_REGS_PORTSC_30.PP = 0x%x\n`
- `%s@%s: %s::%s: performance floor: none\n`
- `%s@%s: %s::%s: setPowerLevel failed with 0x%08x\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE = 0x%x\n`
- `%s@%s: %s::%s: unexpected transition from mode %d to %d\n`
- `%s@%s: %s::%s: failed to enable USB2 phy\n`
- `%s@%s: %s::%s: AUSBC_PWR_CTRL_BLK_HIBERNATION_CLEAR.INTR = 0x%x\n`
- `%s@%s: %s::%s: timed out waiting for SLEEP HIBERNATION_UNMASKED_STATUS 0x%08x HIBERNATION_STATUS 0x%08x\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_HOST_CNTRL_PORT_REG_SET_PORTSC_30_REGS_PORTSC_30 = 0x%x\n`
- `%s@%s: %s::%s: controller hardware is not available\n`
- `%s@%s: %s::%s: failed to find USB3 protocol capability\n`
- `%s@%s: %s::%s: performance floor: low isoch bandwidth\n`
- `%s@%s: %s::%s: performance floor: high bandwidth\n`
- `%s@%s: %s::%s: applied errata for RxDetect issue (rdar://problem/64584969)\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_PHY_MUX_SELECT.PIPE_MODE = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_OVERRIDE_VALUES0.PHYSTATUS_OVERRIDE_VALUE = 0x%x\n`
- `%s@%s: %s::%s: failed to create AppleTypeCPhy session\n`
- `%s@%s: %s::%s: did not find cioService, tunneled USB is not supported\n`
- `%s@%s: %s::%s: failed to allocate _interruptSource[%d]\n`
- `%s@%s: %s::%s: CIO_REGS_BLK_CIOBWNGTOFFSET.MAC_BW_NGT_OFFSET = 0x%x\n`
- `%s@%s: %s::%s: floor bandwidth: %u safe bandwidth: %u\n`
- `%s@%s: %s::%s: unexpected LOCK_PIPE_IF_ACK 1\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_GUSB2PHYCFG_REGS_GUSB2_PHYCFG.SUSPENDUSB20 = 0x%x\n`
- `%s@%s: %s::%s: failed to find phyService\n`
- `%s@%s: %s::%s: _powerControlInterrupt %s\n`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.DEBUG_WRAP_REGS_FORCE_CLK_ON = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_CTLREG_BLK_AUSBC_FORCE_CLK_ON.BULK_FABRIC_REGS_FORCE_CLK_ON = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_AUSBC_AON_GENERAL_REGS.ATC_USB31_DRD_SW_VCC_RESET = 0x%x\n`
- `%s@%s: %s::%s: ATC_DWC_USB31_BLOCK_GBL_BEFORE_0_GCTL.PWRDNSCALE = 0x%x\n`
- `%s@%s: %s::%s: TXDETRX_LOCK_ACK did not set\n`
- `%s@%s: %s::%s: failed to enable USB3 phy\n`
- `%s@%s: %s::%s: timed out waiting for D0_ON interrupt HIBERNATION_UNMASKED_STATUS 0x%08x HIBERNATION_STATUS 0x%08x\n`
- `%s@%s: %s::%s: DVFM_IF_BWR_AGENT_INTERFACE_AGENT_BWR = 0x%llx\n`
- `%s@%s: %s::%s: copyMapperForDevice() failed\n`
- `%s@%s: %s::%s: AUSBC_PIPE_HANDLER_BLK_PIPE_HANDLER_NON_SELECTED_OVERRIDE.NATIVE_POWER_DOWN = 0x%x\n`
- `%s@%s: %s::%s: creating _pipeHandlerRegistersMap failed\n`
- `%s@%s: %s::%s: CIO_REGS_BLK_CIOLFPSOFFSET.MAC_LFPS_OFFSET = 0x%x\n`
- `%s@%s: %s::%s: RAM0_WR_ACTIVE is still set\n`
