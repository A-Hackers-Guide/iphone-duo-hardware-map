# `com.apple.driver.AppleTypeCPhyAUSBC`

- Name: AppleTypeCPhyAUSBC
- Version: `1`
- UUID: `DE260EA7-CCE5-3C0B-9BEB-B9391C2E5D36`
- Source version: `317.40.3.0.0`
- Depends on: [`com.apple.driver.AppleTypeCPhy`](com.apple.driver.AppleTypeCPhy.md) 1.0, [`com.apple.iokit.IOAccessoryManager`](com.apple.iokit.IOAccessoryManager.md) 1.0, [`com.apple.iokit.IOPortFamily`](com.apple.iokit.IOPortFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 19.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 19.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 19.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 19.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleTypeCPhyAUSBC
- `CFBundleIdentifier`: `com.apple.driver.AppleTypeCPhyAUSBC`
- `IOClass`: `AppleTypeCPhyAUSBC`
- `IONameMatch`: `atc-phy,ausbc`
- `IOPersonalityPublisher`: `com.apple.driver.AppleTypeCPhyAUSBC`
- `IOProbeScore`: `10000`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleTypeCPhyAUSBC` | 0x220 | AppleTypeCPhy → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001c53 off=0x008c98f0-0x008cb543 addr=0xfffffe00078cd8f0-0xfffffe00078cf543 r--/r--   __TEXT            
	sz=0x00000008 off=0x008c9f68-0x008c9f70 addr=0xfffffe00078cdf68-0xfffffe00078cdf70               __TEXT.__const            
	sz=0x000008f4 off=0x008c9f70-0x008ca864 addr=0xfffffe00078cdf70-0xfffffe00078ce864               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000cdf off=0x008ca864-0x008cb543 addr=0xfffffe00078ce864-0xfffffe00078cf543               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x000050dc off=0x02a9aea0-0x02a9ff7c addr=0xfffffe0009a9eea0-0xfffffe0009aa3f7c r-x/r-x   __TEXT_EXEC       
	sz=0x00004fac off=0x02a9aea0-0x02a9fe4c addr=0xfffffe0009a9eea0-0xfffffe0009aa3e4c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000130 off=0x02a9fe4c-0x02a9ff7c addr=0xfffffe0009aa3e4c-0xfffffe0009aa3f7c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x049cffe8-0x049d00e8 addr=0xfffffe000b9d3fe8-0xfffffe000b9d40e8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049cffe8-0x049d00b0 addr=0xfffffe000b9d3fe8-0xfffffe000b9d40b0               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9d40b0-0xfffffe000b9d40e8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000938 off=0x01295280-0x01295bb8 addr=0xfffffe0008299280-0xfffffe0008299bb8 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01295280-0x01295288 addr=0xfffffe0008299280-0xfffffe0008299288         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01295288-0x01295290 addr=0xfffffe0008299288-0xfffffe0008299290         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000828 off=0x01295290-0x01295ab8 addr=0xfffffe0008299290-0xfffffe0008299ab8         __DATA_CONST.__const            
	sz=0x00000040 off=0x01295ab8-0x01295af8 addr=0xfffffe0008299ab8-0xfffffe0008299af8         __DATA_CONST.__kalloc_type      
	sz=0x00000098 off=0x01295af8-0x01295b90 addr=0xfffffe0008299af8-0xfffffe0008299b90         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000028 off=0x01295b90-0x01295bb8 addr=0xfffffe0008299b90-0xfffffe0008299bb8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 43 at 0x04aeaf58
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     DE260EA7-CCE5-3C0B-9BEB-B9391C2E5D36
008: LC_SOURCE_VERSION           317.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab6988 size=0x50
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleTypeCPhyAUSBC`
- `CFBundleIdentifier`: `com.apple.driver.AppleTypeCPhyAUSBC`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleTypeCPhyAUSBC`
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
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleTypeCPhyAUSBC.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896584464`
- `_PrelinkExecutableRelativePath`: `AppleTypeCPhyAUSBC`
- `_PrelinkExecutableSize`: `30567`
- `_PrelinkExecutableSourceAddr`: `-2198896584464`
- `_PrelinkKmodInfo`: `-2198828400664`

## Strings (75) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%s@%s: %s::%s: failed to find register range %d\n`
- `eusb2phy_init`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_SIG.VBUS_VALID_EXT_FORCE_EN = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_CTL.USB2PHY_SIDDQ = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_MISC_TUNE.USB2PHY_APBCLK_GATEOFF = 0x%x\n`
- `i8@?0`
- `%s@%s: %s::%s: index %d offset 0x%08x invalid (rangeLength 0x%08llx)\n`
- `%s@%s: %s::%s: PA 0x%llx mask 0x%08x value 0x%08x (read 0x%08x wrote 0x%08x)\n`
- `12111112122212121111111121212121211121111221122112211221122112211222`
- ` @%s:%d`
- `tunable_ATC_FABRIC`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_SIG.VBUS_DETECT_FORCE_EN = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_CORE_EVT_BLK_C0_USB2_CTL = 0x%08x\n`
- `start`
- `%s@%s: %s::%s: Using PSD services for power management\n`
- `tunable_ATC0AXI2AF_LOCK_LOCK`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_SIG.OTG_DPDMPULLDOWN_FORCE_EN = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_SIG.VBUS_VALID_EXT_FORCE_VAL = 0x%x\n`
- `AppleTypeCPhyAUSBC.cpp`
- `%s@%s: %s::%s: failed to find required register ranges\n`
- `%s@%s: %s::%s: applying %s\n`
- `tunable_ATC0AXI2AF`
- `tunable_ATC_COMMON_CFG`
- `%s@%s: %s::%s: C0_UTMI_CLK_ACTIVE.EVT_CNT is 0\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB_CTL.USB_MODE = 0x%x\n`
- `eusb2phy_s2r_enter`
- `%s@%s: %s::%s: found register range %d at 0x%016llx (0x%016llx)\n`
- `service-gates`
- `%s@%s: %s::%s: var value field AUSBC_CORE_EVT_BLK_C0_USB2_CTL.LOAD_CNT = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_CTL.USB2PHY_APB_RESETN = 0x%x\n`
- `eusb2phy_shutdown`
- `usb2PhyPortReset_block_invoke`
- `applyTunables`
- `%s@%s: %s::%s: PA 0x%llx mask 0x%08x value 0x%08x already set (read 0x%08x)\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_CTL.USB2PHY_RESET = 0x%x\n`
- `site.AppleTypeCPhyAUSBC`
- `atcphy_apply_usb_tunables`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_SIG.OTG_DMPULLDOWN_FORCE_VAL = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_SIG.VBUS_DETECT_FORCE_VAL = 0x%x\n`
- `%s@%s: %s::%s: \n`
- `usb2PhyPortReset`
- `AppleTypeCPhyAUSBC`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_SIG.OTG_DPPULLDOWN_FORCE_VAL = 0x%x\n`
- `%s@%s: %s::%s: var value field AUSBC_CORE_EVT_BLK_C0_USB2_CTL.EVT_EN = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_MISC_TUNE.USB2PHY_REFCLK_GATEOFF = 0x%x\n`
- `tunable_ATC0AXI2AF_WR_DIS`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_CTL.USB2PHY_PORT_RESET = 0x%x\n`
- `eusb2phy_s2r_exit`

**[__TEXT.__os_log]**

- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_CTL.USB2PHY_RESET = 0x%x\n`
- `%s@%s: %s::%s: var value field AUSBC_CORE_EVT_BLK_C0_USB2_CTL.LOAD_CNT = 0x%x\n`
- `%s@%s: %s::%s: var value field AUSBC_CORE_EVT_BLK_C0_USB2_CTL.EVT_EN = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_CORE_EVT_BLK_C0_USB2_CTL = 0x%08x\n`
- `%s@%s: %s::%s: applying %s\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_SIG.OTG_DPPULLDOWN_FORCE_VAL = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_SIG.VBUS_DETECT_FORCE_EN = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_CTL.USB2PHY_SIDDQ = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_MISC_TUNE.USB2PHY_APBCLK_GATEOFF = 0x%x\n`
- `%s@%s: %s::%s: C0_UTMI_CLK_ACTIVE.EVT_CNT is 0\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB_CTL.USB_MODE = 0x%x\n`
- `%s@%s: %s::%s: \n`
- `%s@%s: %s::%s: failed to find register range %d\n`
- `%s@%s: %s::%s: Using PSD services for power management\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_SIG.OTG_DPDMPULLDOWN_FORCE_EN = 0x%x\n`
- `%s@%s: %s::%s: index %d offset 0x%08x invalid (rangeLength 0x%08llx)\n`
- `%s@%s: %s::%s: PA 0x%llx mask 0x%08x value 0x%08x already set (read 0x%08x)\n`
- `%s@%s: %s::%s: found register range %d at 0x%016llx (0x%016llx)\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_SIG.VBUS_VALID_EXT_FORCE_VAL = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_CTL.USB2PHY_PORT_RESET = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_CTL.USB2PHY_APB_RESETN = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_MISC_TUNE.USB2PHY_REFCLK_GATEOFF = 0x%x\n`
- `%s@%s: %s::%s: PA 0x%llx mask 0x%08x value 0x%08x (read 0x%08x wrote 0x%08x)\n`
- `%s@%s: %s::%s: failed to find required register ranges\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_SIG.OTG_DMPULLDOWN_FORCE_VAL = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_SIG.VBUS_DETECT_FORCE_VAL = 0x%x\n`
- `%s@%s: %s::%s: AUSBC_CFG_USB2PHY_BLK_USB2PHY_SIG.VBUS_VALID_EXT_FORCE_EN = 0x%x\n`
