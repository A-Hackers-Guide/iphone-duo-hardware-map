# `com.apple.driver.AppleDisplayCrossbar`

- Name: AppleDisplayCrossbar
- Version: `1.0.0`
- UUID: `4426D4CE-DF87-3904-B6F5-A8E7B0FD1F24`
- Source version: `417.40.10.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.2, [`com.apple.driver.AppleTypeCPhy`](com.apple.driver.AppleTypeCPhy.md) 1.0, [`com.apple.iokit.IOAVFamily`](com.apple.iokit.IOAVFamily.md) 1.0, [`com.apple.iokit.IOAccessoryManager`](com.apple.iokit.IOAccessoryManager.md) 1.0, [`com.apple.iokit.IODisplayPortFamily`](com.apple.iokit.IODisplayPortFamily.md) 1.0, [`com.apple.iokit.IOPortFamily`](com.apple.iokit.IOPortFamily.md) 1.0, [`com.apple.iokit.IOThunderboltFamily`](com.apple.iokit.IOThunderboltFamily.md) 1.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 20.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 20.0

## Device-tree nodes it binds (2) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/display-crossbar0`](../devicetree/root__arm-io__display-crossbar0.md) | `AppleT8112DisplayCrossbar` | `display-crossbar,t8112` |
| [`/arm-io/atc0-dpxbar`](../devicetree/root__arm-io__atc0-dpxbar.md) | `AppleT602XATCDPXBAR` | `atc-dpxbar,t602x` |

## IOKit personalities (25) [KC]

### AppleATCDPAltModePort
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleATCDPAltModePort`
- `IONameMatch`: `AAPL,atc-dpphy`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOPropertyMatch`:
  - `port-type`: `<data 22 chars>`
- `IOProviderClass`: `AppleARMIODevice`

### AppleATCDPHDMIPort
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleATCDPHDMIPort`
- `IONameMatch`: `AAPL,atc-dpphy`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOPropertyMatch`:
  - `port-type`: `<data 22 chars>`
- `IOProviderClass`: `AppleARMIODevice`

### AppleATCDPINAdapterPort
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleATCDPINAdapterPort`
- `IONameMatch`: `AAPL,atc-dpin`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProviderClass`: `AppleARMIODevice`

### AppleATCDPOUTAdapterPort
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleATCDPOUTAdapterPort`
- `IONameMatch`: `AAPL,atc-dpout`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProviderClass`: `AppleARMIODevice`

### AppleDisplayConnectionManager
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleDisplayConnectionManager`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProviderClass`: `AppleDisplayCrossbar`

### AppleDisplayCrossbar
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleDisplayCrossbar`
- `IONameMatch`: `AAPL,display-crossbar`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT600XATCDPXBAR
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleT600XATCDPXBAR`
- `IONameMatch`:
  - `atc-dpxbar,t600x`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProviderClass`: `AppleARMIODevice`
- `tunables`: `5`

### AppleT600xDisplayCrossbar
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleT600xDisplayCrossbar`
- `IONameMatch`: `display-crossbar,t600x`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProbeScore`: `100000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT602XATCDPXBAR
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleT602XATCDPXBAR`
- `IONameMatch`:
  - `atc-dpxbar,t602x`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT602XDPTXPort
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleT602XDPTXPort`
- `IONameMatch`:
  - `dptx-phy,t602x`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT602XDisplayCrossbar
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleT602XDisplayCrossbar`
- `IONameMatch`: `display-crossbar,t602x`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProbeScore`: `100000`
- `IOProviderClass`: `AppleARMIODevice`
- `dfp-endpoints`:
  - `atc0`
  - `atc1`
  - `atc2`
  - `atc3`
  - `lpdptx`
- `ufp-endpoints`:
  - `dispext0`
  - `dispext1`
  - `dispext2`
  - `dispext3`
  - `scodec0`

### AppleT603XDisplayCrossbar
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleT603XDisplayCrossbar`
- `IONameMatch`: `display-crossbar,t603x`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProbeScore`: `100000`
- `IOProviderClass`: `AppleARMIODevice`
- `dfp-endpoints`:
  - `atc0`
  - `atc1`
  - `atc2`
  - `atc3`
  - `lpdptx`
- `ufp-endpoints`:
  - `dispext0`
  - `dispext1`
  - `dispext2`
  - `dispext3`
  - `scodec0`

### AppleT604XATCDPXBAR
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleT604XATCDPXBAR`
- `IONameMatch`:
  - `atc-dpxbar,t604x`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT6050DPTXPort
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleT6050DPTXPort`
- `IONameMatch`:
  - `dptx-phy,t6050`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT6050DisplayCrossbar
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleT6050DisplayCrossbar`
- `IONameMatch`: `display-crossbar,t6050`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProbeScore`: `100000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8103ATCDPXBAR
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleT8103ATCDPXBAR`
- `IONameMatch`:
  - `atc-dpxbar,t8103`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProviderClass`: `AppleARMIODevice`
- `tunables`: `0`

### AppleT8112ATCDPXBAR
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleT8112ATCDPXBAR`
- `IONameMatch`:
  - `atc-dpxbar,t8112`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8112DPTXPort
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleT8112DPTXPort`
- `IONameMatch`:
  - `dptx-phy,t8112`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8112DisplayCrossbar
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleT8112DisplayCrossbar`
- `IONameMatch`: `display-crossbar,t8112`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProbeScore`: `100000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8122DPTXPort
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleT8122DPTXPort`
- `IONameMatch`:
  - `dptx-phy,t8122`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8132DPTXPort
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleT8132DPTXPort`
- `IONameMatch`:
  - `dptx-phy,t8132`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8132DisplayCrossbar
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleT8132DisplayCrossbar`
- `IONameMatch`: `display-crossbar,t8132`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProbeScore`: `100000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8142ATCDPXBAR
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleT8142ATCDPXBAR`
- `IONameMatch`:
  - `atc-dpxbar,t8142`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8142DisplayCrossbar
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleT8142DisplayCrossbar`
- `IONameMatch`: `display-crossbar,t8142`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProbeScore`: `100000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleT8152DPTXPort
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `IOClass`: `AppleT8152DPTXPort`
- `IONameMatch`:
  - `dptx-phy,t8152`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDisplayCrossbar`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (33) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleATCDPAltModePort` | 0x2e8 | AppleATCDPNativePort → AppleATCDPPort → IODPTXPort → IOService → IORegistryEntry |
| `AppleATCDPHDMIPort` | 0x2f8 | AppleATCDPNativePort → AppleATCDPPort → IODPTXPort → IOService → IORegistryEntry |
| `AppleATCDPINAdapterPort` | 0x328 | AppleATCDPINAdapterPortBase → AppleATCDPPort → IODPTXPort → IOService → IORegistryEntry |
| `AppleATCDPINAdapterPortBase` | 0x288 | AppleATCDPPort → IODPTXPort → IOService → IORegistryEntry |
| `AppleATCDPNativePort` | 0x2e8 | AppleATCDPPort → IODPTXPort → IOService → IORegistryEntry |
| `AppleATCDPOUTAdapterPort` | 0x108 | AppleATCDPOUTAdapterPortBase → IODPRXPort → IOService → IORegistryEntry |
| `AppleATCDPOUTAdapterPortBase` | 0xe0 | IODPRXPort → IOService → IORegistryEntry |
| `AppleATCDPPort` | 0x278 | IODPTXPort → IOService → IORegistryEntry |
| `AppleATCDPXBAR` | 0xd0 | IOService → IORegistryEntry |
| `AppleDPTXPort` | 0x340 | IODPTXPort → IOService → IORegistryEntry |
| `AppleDisplayConnection` | 0xb8 | IOAVDisplayConnection |
| `AppleDisplayConnectionManager` | 0xa8 | IOAVDisplayConnectionManager → IOService → IORegistryEntry |
| `AppleDisplayCrossbar` | 0x170 | IODPSwitch → IOService → IORegistryEntry |
| `AppleHDMIPortController` | 0x248 | IODPHDMIPortController → IOPort → IOPortFamily → IOService → IORegistryEntry |
| `AppleT600XATCDPXBAR` | 0xd0 | AppleT8103ATCDPXBAR → AppleATCDPXBAR → IOService → IORegistryEntry |
| `AppleT600xDisplayCrossbar` | 0x170 | AppleDisplayCrossbar → IODPSwitch → IOService → IORegistryEntry |
| `AppleT602XATCDPXBAR` | 0xd0 | AppleATCDPXBAR → IOService → IORegistryEntry |
| `AppleT602XDPTXPort` | 0x390 | AppleT8112DPTXPort → AppleDPTXPort → IODPTXPort → IOService → IORegistryEntry |
| `AppleT602XDisplayCrossbar` | 0x170 | AppleDisplayCrossbar → IODPSwitch → IOService → IORegistryEntry |
| `AppleT603XDisplayCrossbar` | 0x170 | AppleT602XDisplayCrossbar → AppleDisplayCrossbar → IODPSwitch → IOService → IORegistryEntry |
| `AppleT604XATCDPXBAR` | 0xd0 | AppleT602XATCDPXBAR → AppleATCDPXBAR → IOService → IORegistryEntry |
| `AppleT6050DPTXPort` | 0x3b0 | AppleT8132DPTXPort → AppleT8122DPTXPort → AppleT8112DPTXPort → AppleDPTXPort → IODPTXPort → IOService → IORegistryEntry |
| `AppleT6050DisplayCrossbar` | 0x178 | AppleT8142DisplayCrossbar → AppleT8132DisplayCrossbar → AppleT603XDisplayCrossbar → AppleT602XDisplayCrossbar → AppleDisplayCrossbar → IODPSwitch → IOService → IORegistryEntry |
| `AppleT8103ATCDPXBAR` | 0xd0 | AppleATCDPXBAR → IOService → IORegistryEntry |
| `AppleT8112ATCDPXBAR` | 0xd0 | AppleT8103ATCDPXBAR → AppleATCDPXBAR → IOService → IORegistryEntry |
| `AppleT8112DPTXPort` | 0x390 | AppleDPTXPort → IODPTXPort → IOService → IORegistryEntry |
| `AppleT8112DisplayCrossbar` | 0x170 | AppleDisplayCrossbar → IODPSwitch → IOService → IORegistryEntry |
| `AppleT8122DPTXPort` | 0x3a8 | AppleT8112DPTXPort → AppleDPTXPort → IODPTXPort → IOService → IORegistryEntry |
| `AppleT8132DPTXPort` | 0x3b0 | AppleT8122DPTXPort → AppleT8112DPTXPort → AppleDPTXPort → IODPTXPort → IOService → IORegistryEntry |
| `AppleT8132DisplayCrossbar` | 0x170 | AppleT603XDisplayCrossbar → AppleT602XDisplayCrossbar → AppleDisplayCrossbar → IODPSwitch → IOService → IORegistryEntry |
| `AppleT8142ATCDPXBAR` | 0xd0 | AppleT604XATCDPXBAR → AppleT602XATCDPXBAR → AppleATCDPXBAR → IOService → IORegistryEntry |
| `AppleT8142DisplayCrossbar` | 0x178 | AppleT8132DisplayCrossbar → AppleT603XDisplayCrossbar → AppleT602XDisplayCrossbar → AppleDisplayCrossbar → IODPSwitch → IOService → IORegistryEntry |
| `AppleT8152DPTXPort` | 0x3a8 | AppleT8122DPTXPort → AppleT8112DPTXPort → AppleDPTXPort → IODPTXPort → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000c958 off=0x0041e820-0x0042b178 addr=0xfffffe0007422820-0xfffffe000742f178 r--/r--   __TEXT            
	sz=0x000002d0 off=0x0041eef0-0x0041f1c0 addr=0xfffffe0007422ef0-0xfffffe00074231c0               __TEXT.__const            
	sz=0x00005318 off=0x0041f1c0-0x004244d8 addr=0xfffffe00074231c0-0xfffffe00074284d8               __TEXT.__cstring          (CstringLiterals)
	sz=0x00006ca0 off=0x004244d8-0x0042b178 addr=0xfffffe00074284d8-0xfffffe000742f178               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00040174 off=0x01b827b0-0x01bc2924 addr=0xfffffe0008b867b0-0xfffffe0008bc6924 r-x/r-x   __TEXT_EXEC       
	sz=0x0003fb34 off=0x01b827b0-0x01bc22e4 addr=0xfffffe0008b867b0-0xfffffe0008bc62e4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000640 off=0x01bc22e4-0x01bc2924 addr=0xfffffe0008bc62e4-0xfffffe0008bc6924          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000600 off=0x0493d0c0-0x0493d6c0 addr=0xfffffe000b9410c0-0xfffffe000b9416c0 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x0493d0c0-0x0493d184 addr=0xfffffe000b9410c0-0xfffffe000b941184               __DATA.__data             
	sz=0x00000538 off=0x00000000-0x00000538 addr=0xfffffe000b941188-0xfffffe000b9416c0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00013408 off=0x0104f590-0x01062998 addr=0xfffffe0008053590-0xfffffe0008066998 rw-/rw-   __DATA_CONST      
	sz=0x00000100 off=0x0104f590-0x0104f690 addr=0xfffffe0008053590-0xfffffe0008053690         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000100 off=0x0104f690-0x0104f790 addr=0xfffffe0008053690-0xfffffe0008053790         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00012510 off=0x0104f790-0x01061ca0 addr=0xfffffe0008053790-0xfffffe0008065ca0         __DATA_CONST.__const            
	sz=0x00000840 off=0x01061ca0-0x010624e0 addr=0xfffffe0008065ca0-0xfffffe00080664e0         __DATA_CONST.__kalloc_type      
	sz=0x000000a0 off=0x010624e0-0x01062580 addr=0xfffffe00080664e0-0xfffffe0008066580         __DATA_CONST.__kalloc_var       
	sz=0x00000320 off=0x01062580-0x010628a0 addr=0xfffffe0008066580-0xfffffe00080668a0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000f8 off=0x010628a0-0x01062998 addr=0xfffffe00080668a0-0xfffffe0008066998         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 231 at 0x04ad719c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     4426D4CE-DF87-3904-B6F5-A8E7B0FD1F24
008: LC_SOURCE_VERSION           417.40.10.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9d578 size=0xb38
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleDisplayCrossbar`
- `CFBundleIdentifier`: `com.apple.driver.AppleDisplayCrossbar`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleDisplayCrossbar`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91018`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91018`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleDisplayCrossbar.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901479392`
- `_PrelinkExecutableRelativePath`: `AppleDisplayCrossbar`
- `_PrelinkExecutableSize`: `394452`
- `_PrelinkExecutableSourceAddr`: `-2198901479392`
- `_PrelinkKmodInfo`: `-2198829002560`

## Strings (881) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `ret=0x%08x\n`
- `warning: ignoring inactive sink notification on inactive port.\n`
- `_phyInterface->openTunnel() ret=0x%08x\n`
- `site.AppleHDMIPortController`
- `AppleHDMIPortController.cpp`
- `%s HDMI-CEC FET on PCON 0x%x\n`
- `DCDADJ`
- `updateDisplayAllocation`
- `1211111212221212111112222211111111111122222222222222222222222222222222222222222222222222222222222222222211111112121221`
- `\"%s::%s(): \" \"no ACK to POWER UP command after 16us\" @%s:%d`
- `AppleT8132DPTXPort`
- `AppleATCDPOUTAdapterPort.cpp`
- `site.AppleT602XDPTXPort`
- `transports-supported`
- `start`
- `peerUFP`
- `AppleDisplayConnectionManager`
- `dfp(0x%llx): reallocate for newly available peer pipes \n`
- `dispext%u,%u -> (self) ret=0x%08x\n`
- `With`
- `function-hdmi_cec_en`
- `Attempting to over disable PCON`
- `dispext%u,%u -> atc%u,%u (atc%u-%s); ufpBit=0x%08x dfpBit=0x%08x pclk=%s (pclk_sel=%u)\n`
- `InfoFlags`
- `lane-shm-regs-2-tunables`
- `changeHPDLevel(false) ret=0x%08x\n`
- `_xbar->takeConnectionDown(*ufp, *this) ret=0x%08x\n`
- `handleDeviceBusyTimeout`
- `enableDevicePower`
- `site.AppleT6050DisplayCrossbar`
- `PLL not locked!\n`
- `\"Config error: HDMI_HPD is not defined\\n\" @%s:%d`
- `dispext%u,%u -> atc%u,%u (atc%u-%s) => mux_select=%u\n`
- `site.AppleDisplayCrossbar`
- `dpxbar-max-bit-rate-per-internal-pipe`
- `update dfp(%d,%d)=%d option=0x%x\n`
- `Port Number`
- `hpd level=%s ret=0x%08x\n`
- `site.AppleT8132DisplayCrossbar`
- `warning: _workLoop is null; returning default work loop!\n`
- `ignoring redundant tunnel state change notification, _tunnelActive=%s\n`
- `\"%s::%s(): \" \"PLL still locked after power down?!\\n\" @%s:%d`
- `checkInitialHPDState`
- `121111121222121211111222221111111111112222222222222222222222222222222222211111222222222222221`
- `DP Alt Mode no longer enabled\n`
- `message=%s dpTransportAvailable=%s\n isPortActivated=%s\n`
- `site.AppleT602XATCDPXBAR`
- `AppleATCDPAltModePort`
- `inactive UFP(0x%llx) - DFP(0x%llx) is found, defer non-preferred UFP(0x%llx) - DFP(0x%llx) allocation\n`
- `takeConnectionDown`
- `dispext%u,%u -> atc%u,%u (atc%u-%s): ret=0x%08x\n`
- `asdc-txd-cfg-3-tunables`
- `asdc-txspl-cfg-1-tunables`
- `makeDPOUTAdapterPortActive_block_invoke`
- `synthesizing displayRequest due to !_displayAllocated...\n`
- `dpxbar-use-cycle-slip-wa`
- `Latching in HDMI_HPD=%d\n`
- `forceHotPlugDetect`
- `AppleATCDPINAdapterPort.cpp`
- `interruptRequestOccurred_block_invoke`
- `always ON`
- `site.AppleATCDPNativePort`
- `DP Alt Mode with PHY still in use\n`
- `writeReg`
- `DCOCFG`
- `synthesizing hotPlugDetectChangeOccurred due to _hpdAsserted...\n`
- `peerUFP(0x%llx) (dispext%u,%u): allocated peerUFP is busy\n`
- `failed to map device memory reg[1]\n`
- `MaxW`
- `display disconnect timeout\n`
- `current _dpOutAdapterHPDAsserted=%s level=%s\n`
- `HDMI HPD %s\n`
- `invoked when ufp == NULL!\n`
- `failed to deallocate peer ufp for dispext%u\n`
- `notice: synthesizing plug event for PCON FW update\n`
- `UFP(0x%llx) (dispext%u,%u): allocated UFP is busy\n`
- `asdc-aux-shm-tunables`
- `\"%s::%s(): \" \"no ACK to POWER DOWN command after 16us\" @%s:%d`
- `hdmi_cec_enabled`
- `getDriveSettings`
- `laneCount=%u ret=0x%08x\n`
- `block=0x%08x reg=0x%08x value=0x%08x\n`
- `AppleT8142ATCDPXBAR`
- `%s HDMI_HPD control\n`
- `HDMI_HPD-Debounced`
- `handleInactiveSinkDetected`
- `deferred`
- `AppleT8142DisplayCrossbar`
- `site.AppleATCDPOUTAdapterPort`
- `AppleATCDPHDMIPort`
- `validateConnection`
- `dfp.role(%u) > max DFP Role(%u)\n`
- `%s::%s(): uhbr-rates expected size = %lu, actual size = %u`
- `pipe-sharing`
- `allowed-disp-count`
- `unexpected initial link rate: %lluGbps\n`
- `12222222222222222222222`
- `supports-limited-pipe`
- `handleClose`
- `setHDMIPCONEnabled`
- `TileH`
- `\"%s::%s(): \" \"PHY impediance calibration failed!\" @%s:%d`
- `site.AppleT603XDisplayCrossbar`
- `getAvailableUFPForDFP_block_invoke`
- `%s::%s(): pll failed to lock`
- `HDMI_HPD`
- `B16@?0^{OSObject=^^?i}8`
- `%s::%s(): PHY impediance calibration failed!`
- `handleOpen`
- `linkUp() ret=0x%08x\n`
- `AppleDisplayCrossbar`
- `MaxVerticalImageSize`
- `got DPTX_INACTIVE_ACK=%u\n`
- `\"%s::%s: \" \"%s::%s(0x%llx): deactivate() incomplete %u seconds after displayRelease()! (check DCPEXT)\\n\" \"\\n\" @%s:%d`
- `NOT %s HDMI PCON 0x%x (PCON power/reset control not configured)\n`
- `dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s): found peerDFP(0x%llx): atc%u,%u (atc%u-%s): allocated to peerUFP(0x%llx) (dispext%u,%u)\n`
- `setDisplayHints_block_invoke`
- `IOAVController`
- `super::takeConnectionDown() ret=0x%08x\n`
- `Using uhbr-rates=%u\n`
- `%s HDMI +5V control\n`
- `%s PCON Reset control\n`
- `setHDMIPCONEnabledInternal(false) ret=0x%08x\n`
- `DFP`
- `super::handleDeactivate() ret=0x%08x (ignored)\n`
- `v16@?0^{IOTimerEventSource=^^?i^{IOEventSource}^{OSObject}^?B^{IOWorkLoop}^v^{ExpansionData}^vQ^{ExpansionData}}8`
- `AppleATCDPXBAR`
- `asdc-txspl-cfg-3-tunables`
- `Unknown`
- `no available ufp peer found\n`
- `pllPowerUp`
- `dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s): %s; allocating to separate display pipe.\n`
- `connect ufp(%d,%d) to dfp(%d,%d)\n`
- `tunables`
- `decrementTunnelUse`
- `set DPRX_INACTIVE=%u, polling for DPRX_INACTIVE_ACK=%u...\n`
- `not defined`
- `reg=0x%08x value=0x%08x\n`
- `HDMI port controller attach failed`
- `dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s): peer UFP is a tiled display requiring %u display pipes; allocating to separate display pipe.\n`
- `DCDADJ = %x\n`
- `%s::%s(): RCAL impedance failed`
- `getLinkRate`
- `port-type`
- `stays ON`
- `kIOHibernateStateKey OSData property not found.\n`
- `getAvailablePeerUFPForDFP`
- `B16@?0^{IODPTXPort=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}^^?^^?^^?^^?i[8I]^{IODPSwitch}^{IOService}^{IODPTXPort}^{IOWorkLoop}^{IOCommandGate}^{IODPTXPortEventLog}^{IOTimerEventSource}^?^?^?^?^{thread_cal`
- `tiled display doesn't support peer pipe\n`
- `i16@?0^{IODPSwitchAllocationState=^^?i^{OSData}^{IODPTXPortConnectionState}I}8`
- `warning: _interruptSource disabled; ignoring interrupt\n`
- `DPOUT Adapter Count == 0\n`
- `failed to open AppleTypeCPhy\n`
- `ret=0x%x\n`
- `\"%s::%s: attempt to access out-of-range register 0x%08x (map size = 0x%08llx).\\n\" @%s:%d`
- `no available ufp found\n`
- `deallocatePeerUFP_block_invoke`
- `IOHibernateState`
- `_hdmiPortController->setHDMIPortEnabled() ret=0x%08x\n`
- `%c%c%c`
- `site.AppleT8122DPTXPort`
- `failed to create AppleTypeCPhyDisplayPortInterface\n`
- `changeHPDLevel_block_invoke`
- `pclkdrv-select`
- `_workLoop->addEventSource(_deactivateTimeoutSource) failed\n`
- `PipeIDs`
- `121111121222121211111222221111111111112222222222222222222222222222222222222222222222222222222222222222221111111212122`
- `_dpinIndex(%u) ≥ DPIN Adapter Count (%u)\n`
- `wait until tunnel is inactive\n`
- `function-dp2hdmi_pwr_en`
- `%s: Vendor: %02x-%02x-%02x Product: 0x%04x Serial Number: 0x%08x\n`
- `-restore`
- `DP-Split support disabled`
- `AppleATCDPINAdapterPortBase.cpp`
- `DTCVREG`
- `12111112122212121122222112211111111112111222222`
- `\"%s::%s(0x%llx): _cioInterface->isTunnelInUse(): isTunnelInUse() returned false after successful call to _cioInterface->startUsingTunnel()!\\n\" @%s:%d`
- `lane-shm-regs-0-tunables`
- `forceInactiveSink`
- `Unplug`
- `dfp(0x%llx): atc%u,%u (atc%u-%s): Bogus tile assignment detected for secondary UFP and %d-%d-%d-%d\n`
- `_phyInterface->getDriveSettings() ret=0x%08x\n`
- `_phyInterface->getLinkRate() ret=0x%08x\n`
- `didChangeLinkConfiguration_block_invoke`
- `no owner\n`
- `AppleT602XDisplayCrossbar`
- `appledptx-limited-pipe`
- `makeDPINAdapterPortActive(false) ret=0x%08x\n`
- `super::bringConnectionUp() ret=0x%08x\n`
- `hpd state updated\n`
- `_phyInterface->setLinkRate() ret=0x%08x\n`
- `lpdptx-phy-eqtx-cal-code-offset`
- `12111112122212121111122222111111111111222222222222222222222222222222222221111122222222222222112`
- `dpxbar-disable-split`
- `reachedDispCountLimit`
- `_phyInterface->open() ret=kIOReturnTimeout; dpTransportAvailable=%s\n`
- `no available peer pipe for rearrangement\n`
- `asdc-cmn-tunables`
- `\"%s::%s(): \" \"pclkdrv-select expected size = %lu, actual size = %u\" @%s:%d`
- `dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s): searching for allocated peer %u (%s)...\n`
- `ufp.role(%u) > max UFP role(%u)\n`
- `super::handleStart() failed`
- `enabling ACIO_BRIDGES interrupts\n`
- `marking tunnel inactive\n`
- `_debugEnabledConfiguration=%s _panicOnDeactivateTimeout=%s\n`
- `connect_block_invoke`
- `tunnelStateChangeThreadCallFunc`
- `tunnelStateChangeNotification_block_invoke`
- `changeHPDLevel(true) ret=0x%08x\n`
- `handleDisplayRequest`
- `HPD event: hpd=%u (lvlchg=%s) plug=%s irqhpd=%s unplug=%s\n`
- `warning: cleaning up after error...\n`
- `getWorkLoop`
- `TileW`
- `super::handleOpen() ret=0x%08x\n`
- `makeDPOUTAdapterPortActive(true) ret=0x%08x\n`
- `%s::%s(): lpdptx-phy-eqtx-cal-code-offset expected size = %lu, actual size = %u`
- `dpin3`
- `site.AppleDisplayConnectionManager`
- `failed to open IOTBTTunnelClientInterfaceManager\n`
- `incrementTunnelUse() ret=0x%08x\n`
- `%s::%s(): no ACK to POWER DOWN command after 16us`
- `\"%s::%s(): \" \"RCAL impedance failed\" @%s:%d`
- `superclass ret=0x%08x\n`
- `%s::%s(): pclkdrv-select expected size = %lu, actual size = %u`
- `STAT_FIFO_RD_%s_EN & 0x%08x != 0\n`
- `maxPixelWidthPerInternalPipe`
- `dp2hdmi-gpio-parent`
- `ufp.role(%u) < min UFP role(%u)\n`
- `site.AppleT8112DisplayCrossbar`
- `handleTunnelActive`
- `AppleT8152DPTXPort`
- `site.AppleATCDPPort`
- `notice: ignoring inactive sink notification during PCON FW update\n`
- `site.AppleT8112ATCDPXBAR`
- `AppleT8122DPTXPort.cpp`
- `requested zero laneCount with wake=%d, exiting..`
- `enabling`
- `handleDeviceNotResponding`
- `setDriveSettings`
- `makeDPINAdapterPortActive(true) ret=0x%08x\n`
- `asdc-dppll-top-tunables`
- `1211111212221212111112222211111111111122222222222222222222222222222222222111112`
- `%s%s HDMI port power\n`
- `UID`
- `notice: ignoring %s event on inactive port.\n`
- `Using pclkdrv-select=%u\n`
- `Unsupported size %#x for tunable within %s\n`
- `readReg`
- `AppleT600XATCDPXBAR`
- `12111112122212121111122222111111111111222222222222222222222222222222222221111121111112222222222222222`
- `makeActive=%s ret=0x%08x\n`
- `AutoConnect`
- `site.AppleATCDPXBAR`
- `RODCOROLEAKCOMP = %x\n`
- `current _dpOutAdapterPortActive=%s makeActive=%s\n`
- `uhbr-rates`
- `init`
- `AppleT600xDisplayCrossbar`
- `didDisplayAllocation_block_invoke`
- `_xbar->connect(ufp, this) ret=0x%08x\n`
- `link rate returned by PHY(%u) does not match link rate previously set (%u)\n`
- `calling _cioInterface->stopUsingTunnel()...\n`
- `allocated=%s activated=%s interruptsEnabled=%s _dpTunnelActive=%s _dpinAdapterPortActive=%s _hpdAsserted=%s\n`
- `waking from hibernate, need to re-enable HDMI port\n`
- `_phyInterface->open() ret=0x%08x\n`
- `AppleT603XDisplayCrossbar`
- `RODCOROLEAKCOMP`
- `new linkRate=%llubps, ret=0x%08x\n`
- `HDMI PCON Power %s\n`
- `handleStart`
- `ProductName`
- `willChangeLinkConfiguration_block_invoke`
- `peer UFP is not a tiled display`
- `IOTimerEventSource::timerEventSource(...) failed\n`
- `notice: ignoring IRQ_HPD event during system sleep.\n`
- `AppleT8112DisplayCrossbar`
- `%s::%s(): no ACK to POWER UP command after 100us`
- `role`
- `STAT_FIFO_RD_N_CLK_EN & 0x%08x != 0\n`
- `dpin0`
- `-dp2hdmi-update-mode`
- `notice: forcing %s event\n`
- `%s does not have valid length in DT\n`
- `dfp(0x%llx): reallocate for newly available ext pipes\n`
- `AppleATCDPNativePort`
- `ConnectionMapping`
- `121111121222121211111222221111111111112222222222222222222222222222222222211111211`
- `current _dpinAdapterPortActive=%s makeActive=%s\n`
- `\"unsupported link rate: %llu\\n\" @%s:%d`
- `Received HDMI_HPD interrupt with hpdState=%lld, _hdmiHPDStateIRQ=%d\n`
- `DTCVREG = %x\n`
- `dfp(0x%llx): atc%u,%u (atc%u-%s): do real DFP display pipe assignment\n`
- `handleDPSwitchWillSleep`
- `drive settings returned by PHY do not match drive settings previously set\n`
- `dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s): Bogus tile assignment detected (%d/%d/%d), revisit DFP display pipe assignment\n`
- `AppleT604XATCDPXBAR`
- `failed to allocate IODPPortService\n`
- `allocate mainUFP 0x%08x peerUFP 0x%08x\n`
- `can't allocate interrupt event source\n`
- `hpd-always-on`
- `dpxbar-allowed-disp-count`
- `\"%s::%s: attempt to access register without memory mapping.\\n\" @%s:%d`
- `AppleATCDPINAdapterPortBase`
- `tunnelStateChangeNotification`
- `makeDPOUTAdapterPortActive(false) ret=0x%08x\n`
- `handleDeviceNotStarted`
- `MaxBpc`
- `appledptx-no-aux-only`
- `DFP(%llx) (Domain%u, atc%u-%s) allocation is %s\n`
- `_phyInterface->open() try %u asking for %u lanes\n`
- `atc-phy`
- `\"%s::%s(): \" \"uhbr-rates expected size = %lu, actual size = %u\" @%s:%d`
- `\"Missing EDT property %s in %s(%llu)\\n\" @%s:%d`
- `ok=%s\n`
- `success`
- `_phyInterface->setDriveSettings() ret=0x%08x\n`
- `Wrong provider type\n`
- `dp2hdmi-gpio%u`
- `PCLK1`
- `YES`
- `super::handleActivate() ret=0x%08x\n`
- `121111121222121211112`
- `supports-aux-only`
- `makeDPINAdapterPortActive_block_invoke`
- `lane-shm-regs-1-tunables`
- `deactivate_block_invoke`
- `bringConnectionUp`
- `AppleDPTXPort`
- `PCLK4`
- `site.AppleT8152DPTXPort`
- `\"%s::%s(): \" \"no ACK to POWER UP command after 100us\" @%s:%d`
- `HDMI PCON power is disabled\n`
- `dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s): DP Split display detected but no resource to enumerate 2nd link\n`
- `lane count returned by PHY(%u) does not match lane count previously set (%u)\n`
- `writeTunables`
- `AppleT8152DPTXPort.cpp`
- `got DPRX_INACTIVE_ACK=%u\n`
- `12111112122212121111122222111111111111222222222222222222222222222222222222222222222222222222222222222222`
- `auto connect must be disabled for seamless update\n`
- `Failed to add command gate to work loop\n`
- `Detected PCON enable leak`
- `site.AppleT604XATCDPXBAR`
- `i8@?0`
- `error: self->runActionBlock() ret 0x%08x\n`
- `hotPlugDetectChangeOccurred_block_invoke`
- `reset`
- `maxBitRatePerInternalPipe`
- `registerInterestedDriver() failed!\n`
- `failed to cast to IOTBTTunnelDPClientInterface\n`
- `calling _cioInterface->startUsingTunnel()...\n`
- `site.AppleT8142ATCDPXBAR`
- `DPOUT_HPD_LEVEL_STATUS %s cleared\n`
- `STAT_FIFO_WR_DPTX_CLK_EN & 0x%08x != 0\n`
- `Address`
- `site.AppleT600XATCDPXBAR`
- `setDPTXSourceSelect(*ufp) ret=0x%08x\n`
- `thread_call_allocate_with_options() failed\n`
- `getWorkLoop() failed\n`
- `_tunnelUseCount=%u\n`
- `_xbar->bringConnectionUp(*ufp, *this) ret=0x%08x\n`
- `didChangeLinkConfiguration`
- `dfp(0x%llx): atc%u,%u (atc%u-%s): revisit DFP display pipe assignment\n`
- `connect peer ufp(%d,%d) to ufp(%d,%d) flags 0x%x\n`
- `function-hdmi_pwr_en`
- `_phyInterface->close() ret=0x%08x (ignored)\n`
- `_phyInterface->getLinkRate(&_linkRate) ret=0x%08x\n`
- `deallocate peerUFP dispext%u from dispext%u\n`
- `error: self->_tunnelStateChangeThreadCall is null!\n`
- `asdc-txd-cfg-1-tunables`
- `Without`
- `ignoring message=%s\n`
- `disconnect ufp(%d,%d) from dfp(%d,%d)\n`
- `AppleATCDPINAdapterPort`
- `\"%s::%s(0x%llx): _cioInterface->isTunnelInUse() returned false while _tunnelUseCount=%u!\\n\" @%s:%d`
- `thread call was pending=%s\n`
- `setLinkRate_block_invoke`
- `notice: ignoring IRQ_HPD event on inactive port.\n`
- `deactivateTimeoutOccurred`
- `%s(%s)`
- `DCOCFG = %x RODCO_ENCAP_EFUSE = %x RODCO_BIASADJ_EFUSE = %x\n`
- `handleTunnelStateChange`
- `set DPOUT_HPD_LEVEL_STATUS mask=0x%x, value=0x%x, polling for clearing...\n`
- `dptxphy-panic-on-assert-failure`
- `synthesizing message=%s: HPD %u\n`
- `MaxHorizontalImageSize`
- `_requireAuxPhyWA %d\n`
- `failed to add interrupt event source to workloop\n`
- `interruptOccurred`
- `failed to open AppleATCDPXBAR\n`
- `dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s); Topology ID mismatch; allocating to a separate display pipe.\n`
- `checkInitialHPDState_block_invoke`
- `testOnly with success\n`
- `%s::%s(0x%llx): deactivate() incomplete %u seconds after displayRelease()! (check DCPEXT)\n\n`
- `warning: ignoring redundant deactivate()\n`
- `%s HDMI-CEC FET control\n`
- `dpphy`
- `connectTo`
- `IRQ`
- `AppleT8112DPTXPort`
- `TileID`
- `DLFCFG`
- `recoverHDMIPort`
- `12111112122212121122222112`
- `super::handleStart() failed\n`
- `full pipe requested but only limited pipe available\n`
- `AppleATCDPOUTAdapterPort`
- `NOT `
- `PCON 0x%x enable count: %u\n`
- `getAvailableUFPForDFP`
- `getMainPort`
- `_dp2hdmiUpdateMode %d\n`
- `_hdmiPortController->init() failed!\n`
- `_hdmiPortController->start() failed!\n`
- `failed to map device memory reg[0]\n`
- `\"%s::%s(0x%llx): attempt to access register 0x%08x from non-gated context.\\n\" @%s:%d`
- `DTCCAL`
- `failed to create AppleHDMIPortController!\n`
- `failed to init IODPPortService\n`
- `unexpected available DP lane count: %u\n`
- `MaxH`
- `MaxTotalPixelRate`
- `makeDPINAdapterPortActive() ret=0x%08x (ignored)\n`
- `no`
- `PCLK3`
- `source-select-offset`
- `notice: ignoring DisplayRequest during system sleep.\n`
- `phySetActiveLaneCount`
- `setHDMIPCONEnabledInternal`
- `\"%s::%s(0x%llx): deactivate() incomplete %u seconds after displayRelease()! (check DCPEXT)\\n\" @%s:%d`
- `AppleATCDPOUTAdapterPortBase`
- `attempt HDMI port recovery\n`
- `message=%s dpTransportAvailable=%s\n`
- `%s HDMI PCON 0x%x using %s control\n`
- `_cioInterface->startUsingTunnel() ret=0x%08x\n`
- `_workLoop->addEventSource(_hpdTimerSource) failed\n`
- `stop`
- `None`
- `AppleDisplayConnection`
- `AppleT8122DPTXPort`
- `site.AppleT6050DPTXPort`
- `AppleT602XDPTXPort`
- `synthesizing message=%s: HPD %u->%u\n`
- `TileX`
- `ret=0x%08x`
- `reset _hpdAsserted due to tunnel state change\n`
- `site.AppleATCDPHDMIPort`
- `handlePortMessage`
- `activePipeMask`
- `site.AppleATCDPOUTAdapterPortBase`
- `\"%s::%s(): \" \"PLL not locked!\\n\" @%s:%d`
- `interruptAction`
- `Set main port for DFP(%d,%d,%d) as (%d,%d,%d)\n`
- `setDisplayHints`
- `MaxPipes`
- `AppleT602XATCDPXBAR`
- `linkRate=%lluGbps ret=0x%08x\n`
- `%s: %s\n`
- `\"InterruptAction is NULL\\n\" @%s:%d`
- `Starting`
- `1211111212221212111111211111212222222211221111111212212122222111111111122`
- `getActiveLaneCount`
- `site.DTTunableData`
- `performImpedanceCalibration`
- `_phyInterface->setLinkRate(%lluGbps) ret=0x%08x\n`
- `Failed to create _transport\n`
- `no_entry`
- `pllPowerDown`
- `site.AppleT8132DPTXPort`
- `STAT_FIFO_WR_N_CLK_EN & 0x%08x != 0\n`
- `handleDeactivate`
- `site.AppleDisplayConnection`
- `WeekOfManufacture`
- `NOT %s HDMI-CEC FET on PCON 0x%x (HDMI-CEC FET control not configured)\n`
- `ConfigChange`
- `err = 0x%x\n`
- `rearrange only support single pipe\n`
- `AppleATCDPOUTAdapterPortBase.cpp`
- `_phyInterface->closeTunnel() ret=0x%08x (ignored)\n`
- `ASSERT`
- `setLinkRate`
- `%s PCON Power control\n`
- `power`
- `unknown`
- `_phyInterface->open() succeeded after %u tries.\n`
- `asdc-dppll-core-tunables`
- `Failed to allocate command gate\n`
- `AppleATCDPPort.cpp`
- `\"%s::%s(): \" \"lpdptx-phy-eqtx-cal-code-offset expected size = %lu, actual size = %u\" @%s:%d`
- `port-number`
- `dpxbar-max-pixel-width-per-internal-pipe`
- `displayRequest_block_invoke`
- `site.AppleT8103ATCDPXBAR`
- `ret=0x%08x _tunnelUseCount=%u\n`
- `configureDPPortObject failed\n`
- `PCLK2`
- `Plug`
- `AppleT8112DPTXPort.cpp`
- `notice: forwarding inactive sink notification on idle port...\n`
- `disconnect ufp(%d,%d) from ufp(%d,%d) seamlessly\n`
- `site.AppleATCDPINAdapterPortBase`
- `DLFCFG = %x\n`
- `%s::%s(): no ACK to POWER UP command after 16us`
- `dpxbar-active-pipe-mask`
- `121111121222121211111222221111111111112222222222222222222222222222222222222222222222222222222222222222221111111212`
- `_sourceSelectOffset %d\n`
- `%u.%u.%u`
- `TileY`
- `super::setLinkRate() ret=0x%08x\n`
- `function-reset`
- `incrementTunnelUse`
- `_cioInterface->stopUsingTunnel() ret=0x%08x (ignored). This should never occur! Please file a radar under 'AppleANDXPTX | all'.)\n`
- `invoked while !_portActivated!\n`
- `AppleDPTXPort.cpp`
- `willChangeLinkConfiguration`
- `handleSystemWillWake`
- `%s does not exist in DT\n`
- `asdc-txspl-cfg-0-tunables`
- `AppleHDMIPortController`
- `notice: ignoring force inactive sink during PCON FW update\n`
- `Display allocation limit %d(<=%d) is reached.\n`
- `handleActivate`
- `superclass err = 0x%x\n`
- `YearOfManufacture`
- `ufp.address.port(%u) must be zero for %s\n`
- `failed to add IOTBTTunnelClientInterface\n`
- `\"%s::%s(): \" \"pll failed to lock\" @%s:%d`
- `DPOUT Adapter Count = %u\n`
- `DEASSERT`
- `STAT_OUT_N_CLK_EN & 0x%08x != 0\n`
- `failed to get PMRootDomain!\n`
- `Route String`
- `lane-shm-regs-3-tunables`
- `%s::%s(): no ACK to POWER DOWN command after 100us`
- `none`
- `setActiveLaneCount`
- `site.AppleT8112DPTXPort`
- `1211111212221212112222211111`
- `121111121222121211222221111111112`
- `Failed to create serializer\n`
- `takeConnectionDown_block_invoke`
- `Not able to find main DFP port\n`
- `handleSetPllCoreCfgTunables`
- `warning: timeout: no response from firmware after %ums; giving up.\n`
- `asdc-txd-cfg-0-tunables`
- `bringConnectionUp_block_invoke`
- `NO`
- `\"%s::%s(): \" \"no ACK to POWER DOWN command after 100us\" @%s:%d`
- `recoverHDMIPort() ret=0x%08x\n`
- `configured for native DP\n`
- `notice: hpd status: HPD_LEVEL_STATUS=0x%08x\n`
- `site.AppleDPTXPort`
- `setHDMIPortEnabled() ret=0x%08x\n`
- `AppleT8132DisplayCrossbar`
- `invalid dfp.address.port(%u)\n`
- `dpxbar-deactivate-timeout-panic`
- `PLL still locked after power down?!\n`
- `setHPDStateInternal`
- `incorrect kIOHibernateStateKey length = %d\n`
- `dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s): peer UFP is a tiled display; assuming DP-Split (incorrect if this is a second display).\n`
- `no available ufp peer found seamlessly\n`
- `AppleATCDPXBAR.cpp`
- `super::init() failed\n`
- `open failed`
- `_hdmiPortController->setHDMIPCONEnabled() ret=0x%08x\n`
- `TileFlag`
- `\"%s::%s(0x%llx): attempt to access register 0x%08x while registers inaccessible.\\n\" @%s:%d`
- `HDMI transport failed to remove\n`
- `invalid pclk_sel - this is a programming error\n`
- `1211111212221212112222211221111111111211122222`
- `MaxActivePixelRate`
- `site.AppleATCDPAltModePort`
- `site.AppleATCDPINAdapterPort`
- `AppleT6050DPTXPort`
- `dfp.address.port(%u) >= %u\n`
- `AppleT8103ATCDPXBAR`
- `AppleT8112ATCDPXBAR`
- `yes`
- `AppleATCDPPort`
- `dpin1`
- `ProductID`
- `ufp.address.endpoint(%u) >= %u\n`
- `STAT_OUT_%s_EN & 0x%08x != 0\n`
- `dpin2`
- `asdc-txspl-cfg-2-tunables`
- `warning: forcing deactivate()...\n`
- `notice: ignoring %s event during system sleep.\n`
- `takeConnectionDown() ret=0x%08x\n`
- `failed to allocate peer ufp for mainUFP 0x%08x\n`
- `TileNumV`
- `ufp.address.port(%u) >= %u\n`
- `tunnelActive: %d\n`
- `dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s) CIO product ID mismatch: dfp(0x%llx) != peerDFP(0x%llx); allocating to a separate display pipe (incorrect for tiled displays)\n`
- `deallocatePeerUFPGated`
- `AppleT6050DisplayCrossbar`
- `acio-parent`
- `getIOPortDelegate::setLinkRate failed! ret=0x%x\n`
- `default policy`
- `disabling`
- `_phyInterface->setActiveLaneCount() ret=0x%08x\n`
- `logTiledDisplayID`
- `require-aux-phy-wa`
- `DTCCAL = %x\n`
- `Dropping activation request while going to sleep\n`
- `pcon-stays-on`
- `Error: No transport found!!`
- `IOWorkLoop::workLoop() failed\n`
- `disabling ACIO_BRIDGES interrupts\n`
- `asdc-txd-cfg-2-tunables`
- `peerDFP`
- `releasing display...\n`
- `site.AppleT602XDisplayCrossbar`
- `site.AppleT8142DisplayCrossbar`
- `dpxbar-parent`
- `function-hdmi_hpd`
- `???`
- `\"unexpected block: %u\\n\" @%s:%d`
- `TileNumH`
- `\"%s::%s(0x%llx): Unbalanced call!\\n\" @%s:%d`
- `set DPTX_INACTIVE=%u, polling for DPTX_INACTIVE_ACK=%u...\n`
- `setHDMIPortEnabled`
- `site.AppleT600xDisplayCrossbar`
- `activate_block_invoke`

**[__TEXT.__os_log]**

- `IOAV[%d] %s<0x%llx>::%s: ret=0x%x\n`
- `IOAV[%d] %s<0x%llx>::%s: _hdmiPortController->setHDMIPCONEnabled() ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: _phyInterface->close() ret=0x%08x (ignored)\n`
- `IOAV[%d] %s<0x%llx>::%s: _workLoop->addEventSource(_deactivateTimeoutSource) failed\n`
- `IOAV[%d] %s<0x%llx>::%s: warning: cleaning up after error...\n`
- `IOAV[%d] %s<0x%llx>::%s: makeDPINAdapterPortActive(false) ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: RODCOROLEAKCOMP = %x\n`
- `IOAV[%d] %s<0x%llx>::%s: notice: forcing %s event\n`
- `IOAV[%d] %s<0x%llx>::%s: allocated=%s activated=%s interruptsEnabled=%s _dpTunnelActive=%s _dpinAdapterPortActive=%s _hpdAsserted=%s\n`
- `IOAV[%d] %s<0x%llx>::%s: HPD event: hpd=%u (lvlchg=%s) plug=%s irqhpd=%s unplug=%s\n`
- `IOAV[%d] %s<0x%llx>::%s: _phyInterface->getLinkRate() ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: synthesizing message=%s: HPD %u->%u\n`
- `IOAV[%d] %s<0x%llx>::%s: IOTimerEventSource::timerEventSource(...) failed\n`
- `IOAV[%d] %s<0x%llx>::%s: %s HDMI +5V control\n`
- `IOAV[%d] %s<0x%llx>::%s: configureDPPortObject failed\n`
- `IOAV[%d] %s<0x%llx>::%s: new linkRate=%llubps, ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: kIOHibernateStateKey OSData property not found.\n`
- `IOAV[%d] %s<0x%llx>::%s: incorrect kIOHibernateStateKey length = %d\n`
- `IOAV[%d] %s<0x%llx>::%s: _phyInterface->open() succeeded after %u tries.\n`
- `IOAV[%d] %s<0x%llx>::%s: notice: forwarding inactive sink notification on idle port...\n`
- `IOAV[%d] %s<0x%llx>::%s: dfp.address.port(%u) >= %u\n`
- `IOAV[%d] %s<0x%llx>::%s: warning: forcing deactivate()...\n`
- `IOAV[%d] %s<0x%llx>::%s: %s::%s(): pclkdrv-select expected size = %lu, actual size = %u`
- `IOAV[%d] %s<0x%llx>::%s: dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s); Topology ID mismatch; allocating to a separate display pipe.\n`
- `IOAV[%d] %s<0x%llx>::%s: configured for native DP\n`
- `IOAV[%d] %s<0x%llx>::%s: Attempting to over disable PCON`
- `IOAV[%d] %s<0x%llx>::%s: Failed to create serializer\n`
- `IOAV[%d] %s<0x%llx>::%s: allocate mainUFP 0x%08x peerUFP 0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: %s::%s(): RCAL impedance failed`
- `IOAV[%d] %s<0x%llx>::%s: attempt HDMI port recovery\n`
- `IOAV[%d] %s<0x%llx>::%s: notice: ignoring DisplayRequest during system sleep.\n`
- `IOAV[%d] %s<0x%llx>::%s: DCOCFG = %x RODCO_ENCAP_EFUSE = %x RODCO_BIASADJ_EFUSE = %x\n`
- `IOAV[%d] %s<0x%llx>::%s: takeConnectionDown() ret=0x%08x\n`
- `%s::%s(): PLL still locked after power down?!\n`
- `IOAV[%d] %s<0x%llx>::%s: super::handleStart() failed\n`
- `IOAV[%d] %s<0x%llx>::%s: HDMI port controller attach failed`
- `IOAV[%d] %s<0x%llx>::%s: notice: ignoring force inactive sink during PCON FW update\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to get PMRootDomain!\n`
- `IOAV[%d] %s<0x%llx>::%s: notice: ignoring IRQ_HPD event during system sleep.\n`
- `IOAV[%d] %s<0x%llx>::%s: synthesizing displayRequest due to !_displayAllocated...\n`
- `IOAV[%d] %s<0x%llx>::%s: ufp.role(%u) > max UFP role(%u)\n`
- `IOAV[%d] %s<0x%llx>::%s: thread call was pending=%s\n`
- `IOAV[%d] %s<0x%llx>::%s: notice: synthesizing plug event for PCON FW update\n`
- `IOAV[%d] %s<0x%llx>::%s: error: self->runActionBlock() ret 0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: Dropping activation request while going to sleep\n`
- `%s::%s(): PLL not locked!\n`
- `IOAV[%d] %s<0x%llx>::%s: linkUp() ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: super::init() failed\n`
- `IOAV[%d] %s<0x%llx>::%s: %s%s HDMI port power\n`
- `IOAV[%d] %s<0x%llx>::%s: %s does not have valid length in DT\n`
- `IOAV[%d] %s<0x%llx>::%s: dfp.role(%u) > max DFP Role(%u)\n`
- `IOAV[%d] %s<0x%llx>::%s: makeActive=%s ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: synthesizing hotPlugDetectChangeOccurred due to _hpdAsserted...\n`
- `IOAV[%d] %s<0x%llx>::%s: invoked while !_portActivated!\n`
- `IOAV[%d] %s<0x%llx>::%s: current _dpinAdapterPortActive=%s makeActive=%s\n`
- `IOAV[%d] %s<0x%llx>::%s: PLL still locked after power down?!\n`
- `IOAV[%d] %s<0x%llx>::%s: dispext%u,%u -> atc%u,%u (atc%u-%s); ufpBit=0x%08x dfpBit=0x%08x pclk=%s (pclk_sel=%u)\n`
- `IOAV[%d] %s<0x%llx>::%s: %s: Vendor: %02x-%02x-%02x Product: 0x%04x Serial Number: 0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: disabling ACIO_BRIDGES interrupts\n`
- `IOAV[%d] %s<0x%llx>::%s: _phyInterface->setLinkRate() ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: STAT_FIFO_WR_DPTX_CLK_EN & 0x%08x != 0\n`
- `IOAV[%d] %s<0x%llx>::%s: ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: %s::%s(): PHY impediance calibration failed!`
- `IOAV[%d] %s<0x%llx>::%s: dfp(0x%llx): atc%u,%u (atc%u-%s): do real DFP display pipe assignment\n`
- `IOAV[%d] %s<0x%llx>::%s: super::setLinkRate() ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s): %s; allocating to separate display pipe.\n`
- `IOAV[%d] %s<0x%llx>::%s: _requireAuxPhyWA %d\n`
- `IOAV[%d] %s<0x%llx>::%s: dfp(0x%llx): reallocate for newly available ext pipes\n`
- `IOAV[%d] %s<0x%llx>::%s: ret=0x%08x _tunnelUseCount=%u\n`
- `IOAV[%d] %s<0x%llx>::%s: _phyInterface->setActiveLaneCount() ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: marking tunnel inactive\n`
- `IOAV[%d] %s<0x%llx>::%s: tunnelActive: %d\n`
- `IOAV[%d] %s<0x%llx>::%s: current _dpOutAdapterPortActive=%s makeActive=%s\n`
- `IOAV[%d] %s<0x%llx>::%s: STAT_FIFO_WR_N_CLK_EN & 0x%08x != 0\n`
- `IOAV[%d] %s<0x%llx>::%s: STAT_FIFO_RD_%s_EN & 0x%08x != 0\n`
- `IOAV[%d] %s<0x%llx>::%s: calling _cioInterface->stopUsingTunnel()...\n`
- `IOAV[%d] %s<0x%llx>::%s: _hdmiPortController->setHDMIPortEnabled() ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: releasing display...\n`
- `IOAV[%d] %s<0x%llx>::%s: _phyInterface->open() ret=kIOReturnTimeout; dpTransportAvailable=%s\n`
- `IOAV[%d] %s<0x%llx>::%s: drive settings returned by PHY do not match drive settings previously set\n`
- `IOAV[%d] %s<0x%llx>::%s: incrementTunnelUse() ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: Set main port for DFP(%d,%d,%d) as (%d,%d,%d)\n`
- `IOAV[%d] %s<0x%llx>::%s: message=%s dpTransportAvailable=%s\n isPortActivated=%s\n`
- `IOAV[%d] %s<0x%llx>::%s: thread_call_allocate_with_options() failed\n`
- `IOAV[%d] %s<0x%llx>::%s: setDPTXSourceSelect(*ufp) ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: _dpinIndex(%u) ≥ DPIN Adapter Count (%u)\n`
- `IOAV[%d] %s<0x%llx>::%s: dfp(0x%llx): atc%u,%u (atc%u-%s): Bogus tile assignment detected for secondary UFP and %d-%d-%d-%d\n`
- `IOAV[%d] %s<0x%llx>::%s: synthesizing message=%s: HPD %u\n`
- `IOAV[%d] %s<0x%llx>::%s: DTCVREG = %x\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to add interrupt event source to workloop\n`
- `IOAV[%d] %s<0x%llx>::%s: ignoring message=%s\n`
- `IOAV[%d] %s<0x%llx>::%s: Not able to find main DFP port\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to open IOTBTTunnelClientInterfaceManager\n`
- `IOAV[%d] %s<0x%llx>::%s: %s PCON Reset control\n`
- `IOAV[%d] %s<0x%llx>::%s: Detected PCON enable leak`
- `IOAV[%d] %s<0x%llx>::%s: Failed to create _transport\n`
- `IOAV[%d] %s<0x%llx>::%s: block=0x%08x reg=0x%08x value=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: makeDPINAdapterPortActive() ret=0x%08x (ignored)\n`
- `IOAV[%d] %s<0x%llx>::%s: %s::%s(): pll failed to lock`
- `IOAV[%d] %s<0x%llx>::%s: superclass ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: dispext%u,%u -> atc%u,%u (atc%u-%s) => mux_select=%u\n`
- `IOAV[%d] %s<0x%llx>::%s: invalid pclk_sel - this is a programming error\n`
- `IOAV[%d] %s<0x%llx>::%s: dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s): DP Split display detected but no resource to enumerate 2nd link\n`
- `IOAV[%d] %s<0x%llx>::%s: _phyInterface->open() ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: _cioInterface->stopUsingTunnel() ret=0x%08x (ignored). This should never occur! Please file a radar under 'AppleANDXPTX | all'.)\n`
- `IOAV[%d] %s<0x%llx>::%s: STAT_FIFO_RD_N_CLK_EN & 0x%08x != 0\n`
- `IOAV[%d] %s<0x%llx>::%s: super::handleStart() failed`
- `IOAV[%d] %s<0x%llx>::%s: DTCCAL = %x\n`
- `IOAV[%d] %s<0x%llx>::%s: hpd level=%s ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: %s HDMI-CEC FET control\n`
- `IOAV[%d] %s<0x%llx>::%s: waking from hibernate, need to re-enable HDMI port\n`
- `IOAV[%d] %s<0x%llx>::%s: dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s): peer UFP is a tiled display requiring %u display pipes; allocating to separate display pipe.\n`
- `IOAV[%d] %s<0x%llx>::%s: error: self->_tunnelStateChangeThreadCall is null!\n`
- `IOAV[%d] %s<0x%llx>::%s: _cioInterface->startUsingTunnel() ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: reset _hpdAsserted due to tunnel state change\n`
- `IOAV[%d] %s<0x%llx>::%s: wait until tunnel is inactive\n`
- `IOAV[%d] %s<0x%llx>::%s: IOWorkLoop::workLoop() failed\n`
- `IOAV[%d] %s<0x%llx>::%s: _phyInterface->getLinkRate(&_linkRate) ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: err = 0x%x\n`
- `IOAV[%d] %s<0x%llx>::%s: Starting`
- `IOAV[%d] %s<0x%llx>::%s: requested zero laneCount with wake=%d, exiting..`
- `IOAV[%d] %s<0x%llx>::%s: failed to create AppleTypeCPhyDisplayPortInterface\n`
- `IOAV[%d] %s<0x%llx>::%s: setHDMIPortEnabled() ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: notice: ignoring inactive sink notification during PCON FW update\n`
- `IOAV[%d] %s<0x%llx>::%s: unexpected initial link rate: %lluGbps\n`
- `IOAV[%d] %s<0x%llx>::%s: Display allocation limit %d(<=%d) is reached.\n`
- `IOAV[%d] %s<0x%llx>::%s: peerUFP(0x%llx) (dispext%u,%u): allocated peerUFP is busy\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to allocate peer ufp for mainUFP 0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: Error: No transport found!!`
- `IOAV[%d] %s<0x%llx>::%s: DPOUT_HPD_LEVEL_STATUS %s cleared\n`
- `IOAV[%d] %s<0x%llx>::%s: Wrong provider type\n`
- `IOAV[%d] %s<0x%llx>::%s: registerInterestedDriver() failed!\n`
- `IOAV[%d] %s<0x%llx>::%s: Failed to add command gate to work loop\n`
- `IOAV[%d] %s<0x%llx>::%s: makeDPOUTAdapterPortActive(false) ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: _dp2hdmiUpdateMode %d\n`
- `IOAV[%d] %s<0x%llx>::%s: DP Alt Mode no longer enabled\n`
- `IOAV[%d] %s<0x%llx>::%s: inactive UFP(0x%llx) - DFP(0x%llx) is found, defer non-preferred UFP(0x%llx) - DFP(0x%llx) allocation\n`
- `IOAV[%d] %s<0x%llx>::%s: HDMI PCON power is disabled\n`
- `IOAV[%d] %s<0x%llx>::%s: _sourceSelectOffset %d\n`
- `IOAV[%d] %s<0x%llx>::%s: warning: _workLoop is null; returning default work loop!\n`
- `IOAV[%d] %s<0x%llx>::%s: super::handleOpen() ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: HDMI HPD %s\n`
- `IOAV[%d] %s<0x%llx>::%s: enabling ACIO_BRIDGES interrupts\n`
- `IOAV[%d] %s<0x%llx>::%s: _xbar->connect(ufp, this) ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: _xbar->takeConnectionDown(*ufp, *this) ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: Received HDMI_HPD interrupt with hpdState=%lld, _hdmiHPDStateIRQ=%d\n`
- `IOAV[%d] %s<0x%llx>::%s: message=%s dpTransportAvailable=%s\n`
- `IOAV[%d] %s<0x%llx>::%s: makeDPINAdapterPortActive(true) ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: DPOUT Adapter Count == 0\n`
- `IOAV[%d] %s<0x%llx>::%s: got DPRX_INACTIVE_ACK=%u\n`
- `IOAV[%d] %s<0x%llx>::%s: dispext%u,%u -> (self) ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: ret=0x%08x`
- `IOAV[%d] %s<0x%llx>::%s: HDMI PCON Power %s\n`
- `IOAV[%d] %s<0x%llx>::%s: unexpected available DP lane count: %u\n`
- `IOAV[%d] %s<0x%llx>::%s: _phyInterface->getDriveSettings() ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: invoked when ufp == NULL!\n`
- `IOAV[%d] %s<0x%llx>::%s: warning: ignoring inactive sink notification on inactive port.\n`
- `IOAV[%d] %s<0x%llx>::%s: got DPTX_INACTIVE_ACK=%u\n`
- `IOAV[%d] %s<0x%llx>::%s: _phyInterface->open() try %u asking for %u lanes\n`
- `IOAV[%d] %s<0x%llx>::%s: DCDADJ = %x\n`
- `IOAV[%d] %s<0x%llx>::%s: _phyInterface->closeTunnel() ret=0x%08x (ignored)\n`
- `IOAV[%d] %s<0x%llx>::%s: hpd state updated\n`
- `IOAV[%d] %s<0x%llx>::%s: NOT %s HDMI-CEC FET on PCON 0x%x (HDMI-CEC FET control not configured)\n`
- `IOAV[%d] %s<0x%llx>::%s: dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s): peer UFP is a tiled display; assuming DP-Split (incorrect if this is a second display).\n`
- `IOAV[%d] %s<0x%llx>::%s: UFP(0x%llx) (dispext%u,%u): allocated UFP is busy\n`
- `IOAV[%d] %s<0x%llx>::%s: _phyInterface->openTunnel() ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: set DPTX_INACTIVE=%u, polling for DPTX_INACTIVE_ACK=%u...\n`
- `IOAV[%d] %s<0x%llx>::%s: _debugEnabledConfiguration=%s _panicOnDeactivateTimeout=%s\n`
- `IOAV[%d] %s<0x%llx>::%s: dfp(0x%llx): atc%u,%u (atc%u-%s): revisit DFP display pipe assignment\n`
- `IOAV[%d] %s<0x%llx>::%s: %s HDMI-CEC FET on PCON 0x%x\n`
- `IOAV[%d] %s<0x%llx>::%s: setHDMIPCONEnabledInternal(false) ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: STAT_OUT_N_CLK_EN & 0x%08x != 0\n`
- `IOAV[%d] %s<0x%llx>::%s: %s::%s(): no ACK to POWER DOWN command after 16us`
- `IOAV[%d] %s<0x%llx>::%s: link rate returned by PHY(%u) does not match link rate previously set (%u)\n`
- `IOAV[%d] %s<0x%llx>::%s: %s: %s\n`
- `IOAV[%d] %s<0x%llx>::%s: NOT %s HDMI PCON 0x%x (PCON power/reset control not configured)\n`
- `IOAV[%d] %s<0x%llx>::%s: dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s) CIO product ID mismatch: dfp(0x%llx) != peerDFP(0x%llx); allocating to a separate display pipe (incorrect for tiled displays)\n`
- `IOAV[%d] %s<0x%llx>::%s: dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s): found peerDFP(0x%llx): atc%u,%u (atc%u-%s): allocated to peerUFP(0x%llx) (dispext%u,%u)\n`
- `IOAV[%d] %s<0x%llx>::%s: dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s): Bogus tile assignment detected (%d/%d/%d), revisit DFP display pipe assignment\n`
- `IOAV[%d] %s<0x%llx>::%s: DP Alt Mode with PHY still in use\n`
- `IOAV[%d] %s<0x%llx>::%s: warning: ignoring redundant deactivate()\n`
- `IOAV[%d] %s<0x%llx>::%s: %s::%s(): lpdptx-phy-eqtx-cal-code-offset expected size = %lu, actual size = %u`
- `IOAV[%d] %s<0x%llx>::%s: dfp(0x%llx): Domain%u, atc%u,%u (atc%u-%s): searching for allocated peer %u (%s)...\n`
- `IOAV[%d] %s<0x%llx>::%s: DFP(%llx) (Domain%u, atc%u-%s) allocation is %s\n`
- `IOAV[%d] %s<0x%llx>::%s: _phyInterface->setDriveSettings() ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: ufp.address.endpoint(%u) >= %u\n`
- `IOAV[%d] %s<0x%llx>::%s: ignoring redundant tunnel state change notification, _tunnelActive=%s\n`
- `IOAV[%d] %s<0x%llx>::%s: super::takeConnectionDown() ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: super::handleActivate() ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: super::bringConnectionUp() ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: %s HDMI_HPD control\n`
- `IOAV[%d] %s<0x%llx>::%s: recoverHDMIPort() ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: ufp.address.port(%u) must be zero for %s\n`
- `IOAV[%d] %s<0x%llx>::%s: %s::%s(): no ACK to POWER UP command after 16us`
- `IOAV[%d] %s<0x%llx>::%s: set DPOUT_HPD_LEVEL_STATUS mask=0x%x, value=0x%x, polling for clearing...\n`
- `IOAV[%d] %s<0x%llx>::%s: %s PCON Power control\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to init IODPPortService\n`
- `IOAV[%d] %s<0x%llx>::%s: Failed to allocate command gate\n`
- `IOAV[%d] %s<0x%llx>::%s: no owner\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to create AppleHDMIPortController!\n`
- `IOAV[%d] %s<0x%llx>::%s: notice: hpd status: HPD_LEVEL_STATUS=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: ok=%s\n`
- `IOAV[%d] %s<0x%llx>::%s: superclass err = 0x%x\n`
- `IOAV[%d] %s<0x%llx>::%s: reg=0x%08x value=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: changeHPDLevel(false) ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: warning: _interruptSource disabled; ignoring interrupt\n`
- `IOAV[%d] %s<0x%llx>::%s: makeDPOUTAdapterPortActive(true) ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: Latching in HDMI_HPD=%d\n`
- `IOAV[%d] %s<0x%llx>::%s: laneCount=%u ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: dispext%u,%u -> atc%u,%u (atc%u-%s): ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: notice: ignoring IRQ_HPD event on inactive port.\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to add IOTBTTunnelClientInterface\n`
- `IOAV[%d] %s<0x%llx>::%s: calling _cioInterface->startUsingTunnel()...\n`
- `IOAV[%d] %s<0x%llx>::%s: _hdmiPortController->start() failed!\n`
- `IOAV[%d] %s<0x%llx>::%s: invalid dfp.address.port(%u)\n`
- `IOAV[%d] %s<0x%llx>::%s: _xbar->bringConnectionUp(*ufp, *this) ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: getIOPortDelegate::setLinkRate failed! ret=0x%x\n`
- `IOAV[%d] %s<0x%llx>::%s: Using uhbr-rates=%u\n`
- `IOAV[%d] %s<0x%llx>::%s: DLFCFG = %x\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to open AppleTypeCPhy\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to open AppleATCDPXBAR\n`
- `IOAV[%d] %s<0x%llx>::%s: %s::%s(0x%llx): deactivate() incomplete %u seconds after displayRelease()! (check DCPEXT)\n\n`
- `IOAV[%d] %s<0x%llx>::%s: Using pclkdrv-select=%u\n`
- `IOAV[%d] %s<0x%llx>::%s: PCON 0x%x enable count: %u\n`
- `IOAV[%d] %s<0x%llx>::%s: %s HDMI PCON 0x%x using %s control\n`
- `IOAV[%d] %s<0x%llx>::%s: HDMI transport failed to remove\n`
- `IOAV[%d] %s<0x%llx>::%s: lane count returned by PHY(%u) does not match lane count previously set (%u)\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to map device memory reg[0]\n`
- `IOAV[%d] %s<0x%llx>::%s: _tunnelUseCount=%u\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to map device memory reg[1]\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to cast to IOTBTTunnelDPClientInterface\n`
- `IOAV[%d] %s<0x%llx>::%s: set DPRX_INACTIVE=%u, polling for DPRX_INACTIVE_ACK=%u...\n`
- `IOAV[%d] %s<0x%llx>::%s: %s::%s(): uhbr-rates expected size = %lu, actual size = %u`
- `IOAV[%d] %s<0x%llx>::%s: %s::%s(): no ACK to POWER UP command after 100us`
- `IOAV[%d] %s<0x%llx>::%s: PLL not locked!\n`
- `IOAV[%d] %s<0x%llx>::%s: _hdmiPortController->init() failed!\n`
- `IOAV[%d] %s<0x%llx>::%s: ufp.address.port(%u) >= %u\n`
- `IOAV[%d] %s<0x%llx>::%s: ufp.role(%u) < min UFP role(%u)\n`
- `IOAV[%d] %s<0x%llx>::%s: current _dpOutAdapterHPDAsserted=%s level=%s\n`
- `IOAV[%d] %s<0x%llx>::%s: linkRate=%lluGbps ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: STAT_OUT_%s_EN & 0x%08x != 0\n`
- `IOAV[%d] %s<0x%llx>::%s: can't allocate interrupt event source\n`
- `IOAV[%d] %s<0x%llx>::%s: warning: timeout: no response from firmware after %ums; giving up.\n`
- `IOAV[%d] %s<0x%llx>::%s: changeHPDLevel(true) ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: notice: ignoring %s event during system sleep.\n`
- `IOAV[%d] %s<0x%llx>::%s: notice: ignoring %s event on inactive port.\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to allocate IODPPortService\n`
- `IOAV[%d] %s<0x%llx>::%s: %s does not exist in DT\n`
- `IOAV[%d] %s<0x%llx>::%s: dfp(0x%llx): reallocate for newly available peer pipes \n`
- `IOAV[%d] %s<0x%llx>::%s: getWorkLoop() failed\n`
- `IOAV[%d] %s<0x%llx>::%s: _phyInterface->setLinkRate(%lluGbps) ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: %s::%s(): no ACK to POWER DOWN command after 100us`
- `IOAV[%d] %s<0x%llx>::%s: _workLoop->addEventSource(_hpdTimerSource) failed\n`
- `IOAV[%d] %s<0x%llx>::%s: super::handleDeactivate() ret=0x%08x (ignored)\n`
- `IOAV[%d] %s<0x%llx>::%s: Unsupported size %#x for tunable within %s\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to deallocate peer ufp for dispext%u\n`
- `IOAV[%d] %s<0x%llx>::%s: deallocate peerUFP dispext%u from dispext%u\n`
- `IOAV[%d] %s<0x%llx>::%s: DPOUT Adapter Count = %u\n`
