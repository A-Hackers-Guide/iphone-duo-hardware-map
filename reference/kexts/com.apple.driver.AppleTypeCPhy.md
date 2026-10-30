# `com.apple.driver.AppleTypeCPhy`

- Name: AppleTypeCPhy
- Version: `1`
- UUID: `87267D2C-4C26-3CDA-8360-30EA1301B2FA`
- Source version: `317.40.3.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.2, [`com.apple.driver.usb.AppleUSBCommon`](com.apple.driver.usb.AppleUSBCommon.md) 1.0, [`com.apple.iokit.IOAccessoryManager`](com.apple.iokit.IOAccessoryManager.md) 1.0, [`com.apple.iokit.IOPortFamily`](com.apple.iokit.IOPortFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 19.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 19.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 19.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 19.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 19.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (5) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleTypeCPhy` | 0x158 | IOService → IORegistryEntry |
| `AppleTypeCPhyCIOInterface` | 0x50 | AppleTypeCPhyInterface |
| `AppleTypeCPhyDisplayPortInterface` | 0xb8 | AppleTypeCPhyInterface |
| `AppleTypeCPhyInterface` | 0x50 |  |
| `AppleTypeCPhyUSBInterface` | 0x50 | AppleTypeCPhyInterface |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000352e off=0x00899250-0x0089c77e addr=0xfffffe000789d250-0xfffffe00078a077e r--/r--   __TEXT            
	sz=0x000019f7 off=0x008998c8-0x0089b2bf addr=0xfffffe000789d8c8-0xfffffe000789f2bf               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000024 off=0x0089b2c0-0x0089b2e4 addr=0xfffffe000789f2c0-0xfffffe000789f2e4               __TEXT.__const            
	sz=0x0000149a off=0x0089b2e4-0x0089c77e addr=0xfffffe000789f2e4-0xfffffe00078a077e               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0001268c off=0x02a11600-0x02a23c8c addr=0xfffffe0009a15600-0xfffffe0009a27c8c r-x/r-x   __TEXT_EXEC       
	sz=0x000123bc off=0x02a11600-0x02a239bc addr=0xfffffe0009a15600-0xfffffe0009a279bc          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000002d0 off=0x02a239bc-0x02a23c8c addr=0xfffffe0009a279bc-0xfffffe0009a27c8c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001a0 off=0x049cf6b0-0x049cf850 addr=0xfffffe000b9d36b0-0xfffffe000b9d3850 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049cf6b0-0x049cf778 addr=0xfffffe000b9d36b0-0xfffffe000b9d3778               __DATA.__data             
	sz=0x000000d8 off=0x00000000-0x000000d8 addr=0xfffffe000b9d3778-0xfffffe000b9d3850               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001600 off=0x01291f78-0x01293578 addr=0xfffffe0008295f78-0xfffffe0008297578 rw-/rw-   __DATA_CONST      
	sz=0x00000028 off=0x01291f78-0x01291fa0 addr=0xfffffe0008295f78-0xfffffe0008295fa0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000028 off=0x01291fa0-0x01291fc8 addr=0xfffffe0008295fa0-0xfffffe0008295fc8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001280 off=0x01291fc8-0x01293248 addr=0xfffffe0008295fc8-0xfffffe0008297248         __DATA_CONST.__const            
	sz=0x00000140 off=0x01293248-0x01293388 addr=0xfffffe0008297248-0xfffffe0008297388         __DATA_CONST.__kalloc_type      
	sz=0x00000168 off=0x01293388-0x012934f0 addr=0xfffffe0008297388-0xfffffe00082974f0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000088 off=0x012934f0-0x01293578 addr=0xfffffe00082974f0-0xfffffe0008297578         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 107 at 0x04aeabd8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     87267D2C-4C26-3CDA-8360-30EA1301B2FA
008: LC_SOURCE_VERSION           317.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab6668 size=0x158
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleTypeCPhy`
- `CFBundleIdentifier`: `com.apple.driver.AppleTypeCPhy`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleTypeCPhy`
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
- `NSHumanReadableCopyright`: `Copyright © 2019-2022 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleTypeCPhy.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896782768`
- `_PrelinkExecutableRelativePath`: `AppleTypeCPhy`
- `_PrelinkExecutableSize`: `95066`
- `_PrelinkExecutableSourceAddr`: `-2198896782768`
- `_PrelinkKmodInfo`: `-2198828403024`

## Strings (265) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `open_block_invoke`
- `Transport`
- `%s@%s: %s::%s: pclk %d already configured: %s link rate %02x options 0x%08x\n`
- `setLinkRate`
- `IOService`
- `%s@%s: %s::%s: CIO mode is required (current mode %s)\n`
- `%s@%s: %s::%s: client %s already has tunnel %d open\n`
- `%s@%s: %s::%s: configureLanes failed: 0x%08x\n`
- `%s@%s: %s::%s: owner %s options 0x%08x\n`
- `%s@%s: %s::%s: assigning lane %d to owner %s type %d options 0x%08x\n`
- `%s@%s: %s::%s: unwinding owner %s type %d options 0x%08x\n`
- `%s@%s: %s::%s: client %s requesting link rate 0x%02x options 0x%08x pclk %d completed with 0x%08x\n`
- `%s@%s: %s::%s: Invalid ffe_preset value in DP Drive Settings index %d\n`
- `2.70Gbps/lane (HBR)`
- `5.40Gbps/lane (HBR2)`
- `%s@%s: %s::%s: found IOAccessoryManagerUSBC %s@%s\n`
- `%s@%s: %s::%s: USB2 wait aborted: current owner %s\n`
- `close_block_invoke`
- `AppleTypeCPhyDisplayPortInterface.cpp`
- `%s: %s::%s: %s type %d: %d completed with 0x%08x\n`
- `open`
- `none`
- `%s@%s: %s::%s: got lane session owner %s type %d options 0x%08x lanes %d\n`
- `%s@%s: %s::%s: no tunnels available\n`
- `displayPortLinkRateChange_block_invoke`
- `displayPortDriveSettingsChange`
- `%s@%s: %s::%s: Invalid eq level in DP Drive Settings index %d\n`
- `CIO`
- `Power Level`
- `powerStateWillChangeTo_block_invoke`
- `1.62Gbps/lane (RBR)`
- `downspread`
- `IOHibernateState`
- `%s@%s: %s::%s: %s owner %s type %d powerLevel %d options 0x%08x\n`
- `%s@%s: %s::%s: client is already waiting for a session\n`
- `%s@%s: %s::%s: waiting for lane session owner %s type %d options 0x%08x timeoutMs %d\n`
- `%s@%s: %s::%s: failed to configure usb-repeater %s\n`
- `displayPortLinkRateChange`
- `NULL`
- `checkForPowerLoss`
- `function-dock_parent`
- `%s@%s: %s::%s: \n`
- `%s@%s: %s::%s: USB2 timeout: blocked by %s (type %d, power %d)\n`
- `assignUSB2Client_block_invoke`
- `assignLaneClient_block_invoke`
- `AAPL,phandle`
- `%s@%s: %s::%s: USB3 waiting for DP client to close\n`
- `%s@%s: %s::%s: client %s completed with 0x%08x\n`
- `%s@%s: %s::%s: hibernate power loss\n`
- `%s: %s::%s: %s type %d: powerLevel %d options 0x%08x timeoutMs %dms\n`
- `%s@%s: %s::%s: %s transport %d unexpected power level %d\n`
- `ATCPhyLane0TransportTypeOverride`
- `%s@%s: %s::%s: USB2 client '%s' %s -> %s\n`
- `%s@%s: %s::%s: Invalid voltage level in DP Drive Settings index %d\n`
- `%s@%s: %s::%s: failed to build dictionary for %s\n`
- `setDownspread`
- `%s: %s::%s: %s type %d: scaling timeoutMs from %d -> %d due to logging mask\n`
- `1211122221`
- `start`
- `AppleTypeCPhyDisplayPortPclk`
- `%s@%s: %s::%s: open failed: NULL client\n`
- `%s@%s: %s::%s: invalid power level (%d)\n`
- `%s@%s: %s::%s: DP or multifunction mode is required (current mode %s)\n`
- `getPhyPlugOrientation`
- `getAvailableLaneCount`
- `%s@%s: %s::%s: failed to create _pclkState clients\n`
- `%s@%s: %s::%s: open USB2 session\n`
- `openDisplayPortTunnel_block_invoke`
- `no connection`
- `%s@%s: %s::%s: got USB2 session owner %s options 0x%08x\n`
- `%s@%s: %s::%s: tx %d rx %d\n`
- `configureLanes`
- `atc-lane-config`
- `AppleTypeCPhyLane`
- `powerStateDidChangeTo_block_invoke`
- `site.AppleTypeCPhyUSBInterface`
- ` @%s:%d`
- `i8@?0`
- `Link Rate`
- `Clients`
- `ATCPhyLane1TransportTypeOverride`
- `configureUSB2`
- `8.10Gbps/lane (HBR3)`
- `Tunnel %d`
- `other`
- `%s@%s: %s::%s: Plug orientation: %d\n`
- `AppleTypeCPhyDisplayPortInterface`
- `site.AppleTypeCPhyDisplayPortInterface`
- `%s: %s::%s: %s type %d: %d\n`
- `close`
- `PCLK %d`
- `multifunction`
- `getPhyLaneConfiguration`
- `%s@%s: %s::%s: client %s released tunnel %d\n`
- `displayPortTunnelLinkRateChange`
- `%s@%s: %s::%s: owner %s type %d options 0x%08x\n`
- `usb-repeater`
- `atcphy-unit-test-mode`
- `AppleTypeCPhyDisplayPortTunnel`
- `Client`
- `off`
- `%s@%s: %s::%s: owner %s type %d powerLevel %d options 0x%08x result 0x%08x\n`
- `%s@%s: %s::%s: lane wait aborted: have %d/%d lanes. Owners: L0=%s, L1=%s\n`
- `Options`
- `%s@%s: %s::%s: ACIO client '%s' %s -> %s (ACIOPHY %s -> %s)\n`
- `kAppleTypeCPhyPropertyDebugOptions`
- `atc-plug-orientation`
- `%s@%s: %s::%s: Error: no orientation information found.`
- `AppleTypeCPhyInterface`
- `%s@%s: %s::%s: DP open got unexpected result %d waiting for USB3 client to exit S2R\n`
- `%s@%s: %s::%s: Mismatch mode in DP Drive Settings index %d\n`
- `sleep`
- `%s: %s::%s: %s type %d: \n`
- `setPowerLevel`
- `%s@%s: %s::%s: atcphy-unit-test-mode set in boot-args\n`
- `%s@%s: %s::%s: assigned lanes %d max lanes %d\n`
- `%s@%s: %s::%s: DP didn't close\n`
- `%s@%s: %s::%s: USB3 finished waiting for DP\n`
- `%s@%s: %s::%s: invalid power level (%d) for kAppleTypeCPhyTransportTypeUnknown\n`
- `DP`
- `%s@%s: %s::%s: Error: no lane configuration information found.`
- `B16@?0^{OSObject=^^?i}8`
- `displayPortTunnelLinkRateChange_block_invoke`
- `copyPhandleDriver`
- `%s@%s: %s::%s: Error: data size mismatch.`
- `addDisplayPortPclkClient_block_invoke`
- `USB2`
- `DisplayPort`
- `getRequiresDownspread`
- `%s: %s::%s: %s type %d: missing downspread option for this link rate\n`
- `AppleTypeCPhy`
- `Lane %d`
- `%s@%s: %s::%s: unable to identify client for lane mask 0x%08x\n`
- `getClientForLaneMask`
- `%s@%s: %s::%s: _lostPower handling is still pending\n`
- `getDownspread`
- `1211111212221212111111112121212121112111122`
- `%s@%s: %s::%s: %s function-dock_parent completed with 0x%08x\n`
- `%s@%s: %s::%s: failed to find IOAccessoryManagerUSBC\n`
- `usb-repeater-options`
- `%s@%s: %s::%s: DisplayPort client failed type checks\n`
- `%s@%s: %s::%s: unable to find tunnel for client %s\n`
- `%s@%s: %s::%s: client %s link rate 0x%02x pclk %d completed with 0x%08x\n`
- `%s@%s: %s::%s: failed to find %s for %s\n`
- `AppleTypeCPhy.cpp`
- `%s@%s: %s::%s: %s owner %s type %d powerLevel %d options 0x%08x: waiting for hibernate resume handling\n`
- `%s@%s: %s::%s: CIO client failed type checks\n`
- `closeDisplayPortTunnel_block_invoke`
- `AppleTypeCPhyDownspreadCapability`
- `%s: %s::%s: %s type %d: link rate 0x%02x options 0x%08x pclk %d completed with 0x%08x\n`
- `getSupportsDownspread`
- `%s@%s: %s::%s: open session at lane %d\n`
- `%s@%s: %s::%s: lane timeout: need %d lanes, have %d. Owners: L0=%s, L1=%s\n`
- `%s@%s: %s::%s: client does not have an open session\n`
- `%s@%s: %s::%s: %d:%d\n`
- `USB3`
- `%s@%s: %s::%s: Plug orientation override found.\n`
- `site.AppleTypeCPhy`
- `instance`
- `%d`
- `%s@%s: %s::%s: waiting for USB2 session owner %s options 0x%08x timeoutMs %d\n`
- `site.AppleTypeCPhyCIOInterface`
- `site.AppleTypeCPhyInterface`
- `AppleTypeCPhyUSB2`
- `%s@%s: %s::%s: hibernate resume timeout: USB2=%s, Lane0=%s, Lane1=%s\n`
- `%s@%s: %s::%s: %s owner %s type %d powerLevel %d options 0x%08x: client must handle hibernate resume before powering on\n`
- `getLaneConfigurationFromDock`
- `%s@%s: %s::%s: mode '%s' orientation %d\n`
- `on`
- `AppleTypeCPhyCIOInterface`
- `AppleTypeCPhyID`
- `%s@%s: %s::%s: found usb-repeater %s\n`
- `%s@%s: %s::%s: USB3 going to S2R got unexpected result %d waiting for DP client to close\n`
- `%s@%s: %s::%s: client %s reserved tunnel %d\n`
- `removeDisplayPortPclkClient_block_invoke`
- `stop`
- `%s@%s: %s::%s: configureUSB2 failed: 0x%08x\n`
- `%s@%s: %s::%s: tunnel %d still in use by %s\n`
- `%s@%s: %s::%s: USB client failed type checks\n`
- `unknown`
- `12111222212222222222222`
- `\"AppleTypeCPhyDisplayPortInterface::free called while there is an open tunnel %d\\n\" @%s:%d`
- `AppleTypeCPhyUSBInterface`

**[__TEXT.__os_log]**

- `%s@%s: %s::%s: Mismatch mode in DP Drive Settings index %d\n`
- `%s@%s: %s::%s: Error: data size mismatch.`
- `%s@%s: %s::%s: Error: no orientation information found.`
- `%s@%s: %s::%s: %d:%d\n`
- `%s@%s: %s::%s: USB client failed type checks\n`
- `%s@%s: %s::%s: failed to find %s for %s\n`
- `%s@%s: %s::%s: USB3 waiting for DP client to close\n`
- `%s@%s: %s::%s: USB2 client '%s' %s -> %s\n`
- `%s@%s: %s::%s: _lostPower handling is still pending\n`
- `%s@%s: %s::%s: open session at lane %d\n`
- `%s@%s: %s::%s: tunnel %d still in use by %s\n`
- `%s@%s: %s::%s: unable to identify client for lane mask 0x%08x\n`
- `%s@%s: %s::%s: tx %d rx %d\n`
- `%s@%s: %s::%s: Invalid ffe_preset value in DP Drive Settings index %d\n`
- `%s@%s: %s::%s: assigned lanes %d max lanes %d\n`
- `%s@%s: %s::%s: USB3 going to S2R got unexpected result %d waiting for DP client to close\n`
- `%s@%s: %s::%s: DP open got unexpected result %d waiting for USB3 client to exit S2R\n`
- `%s@%s: %s::%s: open USB2 session\n`
- `%s@%s: %s::%s: %s owner %s type %d powerLevel %d options 0x%08x: client must handle hibernate resume before powering on\n`
- `%s@%s: %s::%s: %s owner %s type %d powerLevel %d options 0x%08x: waiting for hibernate resume handling\n`
- `%s@%s: %s::%s: USB2 wait aborted: current owner %s\n`
- `%s@%s: %s::%s: configureLanes failed: 0x%08x\n`
- `%s@%s: %s::%s: waiting for USB2 session owner %s options 0x%08x timeoutMs %d\n`
- `%s@%s: %s::%s: client does not have an open session\n`
- `%s@%s: %s::%s: failed to configure usb-repeater %s\n`
- `%s@%s: %s::%s: DP or multifunction mode is required (current mode %s)\n`
- `%s: %s::%s: %s type %d: %d completed with 0x%08x\n`
- `%s@%s: %s::%s: failed to create _pclkState clients\n`
- `%s@%s: %s::%s: assigning lane %d to owner %s type %d options 0x%08x\n`
- `%s@%s: %s::%s: client %s released tunnel %d\n`
- `%s@%s: %s::%s: unable to find tunnel for client %s\n`
- `%s@%s: %s::%s: client %s requesting link rate 0x%02x options 0x%08x pclk %d completed with 0x%08x\n`
- `%s@%s: %s::%s: Plug orientation: %d\n`
- `%s: %s::%s: %s type %d: link rate 0x%02x options 0x%08x pclk %d completed with 0x%08x\n`
- `%s: %s::%s: %s type %d: \n`
- `%s@%s: %s::%s: found usb-repeater %s\n`
- `%s@%s: %s::%s: %s transport %d unexpected power level %d\n`
- `%s@%s: %s::%s: lane wait aborted: have %d/%d lanes. Owners: L0=%s, L1=%s\n`
- `%s@%s: %s::%s: failed to find IOAccessoryManagerUSBC\n`
- `%s@%s: %s::%s: \n`
- `%s@%s: %s::%s: client %s reserved tunnel %d\n`
- `%s@%s: %s::%s: hibernate power loss\n`
- `%s@%s: %s::%s: client is already waiting for a session\n`
- `%s@%s: %s::%s: invalid power level (%d)\n`
- `%s@%s: %s::%s: pclk %d already configured: %s link rate %02x options 0x%08x\n`
- `%s: %s::%s: %s type %d: missing downspread option for this link rate\n`
- `%s@%s: %s::%s: atcphy-unit-test-mode set in boot-args\n`
- `%s@%s: %s::%s: USB2 timeout: blocked by %s (type %d, power %d)\n`
- `%s@%s: %s::%s: configureUSB2 failed: 0x%08x\n`
- `%s@%s: %s::%s: lane timeout: need %d lanes, have %d. Owners: L0=%s, L1=%s\n`
- `%s@%s: %s::%s: DP didn't close\n`
- `%s@%s: %s::%s: ACIO client '%s' %s -> %s (ACIOPHY %s -> %s)\n`
- `%s@%s: %s::%s: Plug orientation override found.\n`
- `%s: %s::%s: %s type %d: powerLevel %d options 0x%08x timeoutMs %dms\n`
- `%s@%s: %s::%s: found IOAccessoryManagerUSBC %s@%s\n`
- `%s@%s: %s::%s: %s owner %s type %d powerLevel %d options 0x%08x\n`
- `%s@%s: %s::%s: USB3 finished waiting for DP\n`
- `%s@%s: %s::%s: invalid power level (%d) for kAppleTypeCPhyTransportTypeUnknown\n`
- `%s@%s: %s::%s: no tunnels available\n`
- `%s@%s: %s::%s: failed to build dictionary for %s\n`
- `%s: %s::%s: %s type %d: %d\n`
- `%s@%s: %s::%s: owner %s type %d powerLevel %d options 0x%08x result 0x%08x\n`
- `%s@%s: %s::%s: unwinding owner %s type %d options 0x%08x\n`
- `%s@%s: %s::%s: mode '%s' orientation %d\n`
- `%s@%s: %s::%s: %s function-dock_parent completed with 0x%08x\n`
- `%s@%s: %s::%s: open failed: NULL client\n`
- `%s@%s: %s::%s: got lane session owner %s type %d options 0x%08x lanes %d\n`
- `%s@%s: %s::%s: owner %s type %d options 0x%08x\n`
- `%s@%s: %s::%s: CIO mode is required (current mode %s)\n`
- `%s@%s: %s::%s: Invalid voltage level in DP Drive Settings index %d\n`
- `%s@%s: %s::%s: Invalid eq level in DP Drive Settings index %d\n`
- `%s@%s: %s::%s: client %s link rate 0x%02x pclk %d completed with 0x%08x\n`
- `%s@%s: %s::%s: got USB2 session owner %s options 0x%08x\n`
- `%s@%s: %s::%s: DisplayPort client failed type checks\n`
- `%s@%s: %s::%s: CIO client failed type checks\n`
- `%s@%s: %s::%s: client %s already has tunnel %d open\n`
- `%s@%s: %s::%s: client %s completed with 0x%08x\n`
- `%s@%s: %s::%s: Error: no lane configuration information found.`
- `%s: %s::%s: %s type %d: scaling timeoutMs from %d -> %d due to logging mask\n`
- `%s@%s: %s::%s: hibernate resume timeout: USB2=%s, Lane0=%s, Lane1=%s\n`
- `%s@%s: %s::%s: waiting for lane session owner %s type %d options 0x%08x timeoutMs %d\n`
- `%s@%s: %s::%s: owner %s options 0x%08x\n`
