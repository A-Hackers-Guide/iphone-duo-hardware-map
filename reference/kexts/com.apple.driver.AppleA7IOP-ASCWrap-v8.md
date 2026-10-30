# `com.apple.driver.AppleA7IOP-ASCWrap-v8`

- Name: AppleA7IOP-ASCWrap-v8
- Version: `1.0.2`
- UUID: `E21E7311-F03C-3153-8A3F-97265DDC7460`
- Source version: `342.40.3.0.0`
- Depends on: [`com.apple.driver.AppleA7IOP`](com.apple.driver.AppleA7IOP.md) 1.0.0, [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0

## Device-tree nodes it binds (16) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/aop`](../devicetree/root__arm-io__aop.md) | `AppleASCWrapV8` | `iop,ascwrap-v8` |
| [`/arm-io/aop2`](../devicetree/root__arm-io__aop2.md) | `AppleASCWrapV8` | `iop,ascwrap-v8` |
| [`/arm-io/pmp`](../devicetree/root__arm-io__pmp.md) | `AppleASCWrapV8` | `iop,ascwrap-v8` |
| [`/arm-io/sep`](../devicetree/root__arm-io__sep.md) | `AppleASCWrapV8SEP` | `iop-sep,ascwrap-v8` |
| [`/arm-io/sio`](../devicetree/root__arm-io__sio.md) | `AppleASCWrapV8` | `iop,ascwrap-v8` |
| [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) | `AppleASCWrapV8` | `iop,ascwrap-v8` |
| [`/arm-io/smc`](../devicetree/root__arm-io__smc.md) | `AppleASCWrapV8` | `iop,ascwrap-v8` |
| [`/arm-io/mtp`](../devicetree/root__arm-io__mtp.md) | `AppleASCWrapV8` | `iop,ascwrap-v8` |
| [`/arm-io/dcp`](../devicetree/root__arm-io__dcp.md) | `AppleASCWrapV8` | `iop,ascwrap-v8` |
| [`/arm-io/dcpsec`](../devicetree/root__arm-io__dcpsec.md) | `AppleASCWrapV8` | `iop,ascwrap-v8` |
| [`/arm-io/dcpext0`](../devicetree/root__arm-io__dcpext0.md) | `AppleASCWrapV8` | `iop,ascwrap-v8` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `AppleASCWrapV8SISP` | `iop-isp,ascwrap-v8` |
| [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) | `AppleASCWrapV8ANE` | `iop-ane,ascwrap-v8` |
| [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) | `AppleASCWrapV8ANE` | `iop-ane,ascwrap-v8` |
| [`/arm-io/gfx-asc`](../devicetree/root__arm-io__gfx-asc.md) | `AppleASCWrapV8` | `iop,ascwrap-v8` |
| [`/arm-io/gfx1-asc`](../devicetree/root__arm-io__gfx1-asc.md) | `AppleASCWrapV8` | `iop,ascwrap-v8` |

## IOKit personalities (4) [KC]

### AppleASCWrapV8
- `CFBundleIdentifier`: `com.apple.driver.AppleA7IOP-ASCWrap-v8`
- `IOClass`: `AppleASCWrapV8`
- `IONameMatch`:
  - `iop,ascwrap-v8`
- `IOPersonalityPublisher`: `com.apple.driver.AppleA7IOP-ASCWrap-v8`
- `IOProviderClass`: `AppleARMIODevice`

### AppleASCWrapV8ANE
- `CFBundleIdentifier`: `com.apple.driver.AppleA7IOP-ASCWrap-v8`
- `IOClass`: `AppleASCWrapV8ANE`
- `IONameMatch`:
  - `iop-ane,ascwrap-v8`
- `IOPersonalityPublisher`: `com.apple.driver.AppleA7IOP-ASCWrap-v8`
- `IOProviderClass`: `AppleARMIODevice`

### AppleASCWrapV8SEP
- `CFBundleIdentifier`: `com.apple.driver.AppleA7IOP-ASCWrap-v8`
- `IOClass`: `AppleASCWrapV8SEP`
- `IONameMatch`:
  - `iop-sep,ascwrap-v8`
- `IOPersonalityPublisher`: `com.apple.driver.AppleA7IOP-ASCWrap-v8`
- `IOProviderClass`: `AppleARMIODevice`

### AppleASCWrapV8SISP
- `CFBundleIdentifier`: `com.apple.driver.AppleA7IOP-ASCWrap-v8`
- `IOClass`: `AppleASCWrapV8SISP`
- `IONameMatch`:
  - `iop-isp,ascwrap-v8`
- `IOPersonalityPublisher`: `com.apple.driver.AppleA7IOP-ASCWrap-v8`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (4) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleASCWrapV8` | 0x1d8 | AppleA7IOP → AppleIOP → IOSlaveCPU → IOService → IORegistryEntry |
| `AppleASCWrapV8ANE` | 0x1d8 | AppleASCWrapV8 → AppleA7IOP → AppleIOP → IOSlaveCPU → IOService → IORegistryEntry |
| `AppleASCWrapV8SEP` | 0x1d8 | AppleASCWrapV8 → AppleA7IOP → AppleIOP → IOSlaveCPU → IOService → IORegistryEntry |
| `AppleASCWrapV8SISP` | 0x1d8 | AppleASCWrapV8 → AppleA7IOP → AppleIOP → IOSlaveCPU → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000b49 off=0x0014e030-0x0014eb79 addr=0xfffffe0007152030-0xfffffe0007152b79 r--/r--   __TEXT            
	sz=0x00000571 off=0x0014e608-0x0014eb79 addr=0xfffffe0007152608-0xfffffe0007152b79               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x000023c4 off=0x016667b0-0x01668b74 addr=0xfffffe000866a7b0-0xfffffe000866cb74 r-x/r-x   __TEXT_EXEC       
	sz=0x00002264 off=0x016667b0-0x01668a14 addr=0xfffffe000866a7b0-0xfffffe000866ca14          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000160 off=0x01668a14-0x01668b74 addr=0xfffffe000866ca14-0xfffffe000866cb74          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000178 off=0x0492e0a0-0x0492e218 addr=0xfffffe000b9320a0-0xfffffe000b932218 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0492e0a0-0x0492e168 addr=0xfffffe000b9320a0-0xfffffe000b932168               __DATA.__data             
	sz=0x000000b0 off=0x00000000-0x000000b0 addr=0xfffffe000b932168-0xfffffe000b932218               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00002160 off=0x00f90e20-0x00f92f80 addr=0xfffffe0007f94e20-0xfffffe0007f96f80 rw-/rw-   __DATA_CONST      
	sz=0x00000020 off=0x00f90e20-0x00f90e40 addr=0xfffffe0007f94e20-0xfffffe0007f94e40         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000020 off=0x00f90e40-0x00f90e60 addr=0xfffffe0007f94e40-0xfffffe0007f94e60         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001f60 off=0x00f90e60-0x00f92dc0 addr=0xfffffe0007f94e60-0xfffffe0007f96dc0         __DATA_CONST.__const            
	sz=0x00000100 off=0x00f92dc0-0x00f92ec0 addr=0xfffffe0007f96dc0-0xfffffe0007f96ec0         __DATA_CONST.__kalloc_type      
	sz=0x000000b0 off=0x00f92ec0-0x00f92f70 addr=0xfffffe0007f96ec0-0xfffffe0007f96f70         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000010 off=0x00f92f70-0x00f92f80 addr=0xfffffe0007f96f70-0xfffffe0007f96f80         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 46 at 0x04ad0ea8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     E21E7311-F03C-3153-8A3F-97265DDC7460
008: LC_SOURCE_VERSION           342.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004a96548 size=0xb8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleA7IOP-ASCWrap-v8`
- `CFBundleIdentifier`: `com.apple.driver.AppleA7IOP-ASCWrap-v8`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleA7IOP-ASCWrap-v8`
- `CFBundleNumericVersion`: `16941056`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.2`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2024-2025 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleA7IOP-ASCWrap-v8.kext`
- `_PrelinkExecutableLoadAddr`: `-2198904430544`
- `_PrelinkExecutableRelativePath`: `AppleA7IOP-ASCWrap-v8`
- `_PrelinkExecutableSize`: `20965`
- `_PrelinkExecutableSourceAddr`: `-2198904430544`
- `_PrelinkKmodInfo`: `-2198829064032`

## Strings (35) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AppleASCWrapCommon.cpp`
- `_msgboxRegisterMap != nullptr`
- `mailboxItemCount != nullptr`
- `AppleASCWrapV8SEP`
- `12111112122212121112221111121211121121211222221112111122121`
- `_coreRegisterMap != nullptr`
- `AppleASCWrapV8`
- `site.AppleASCWrapV8`
- `\"%s:%s:%u REQUIRE failed: %s\" @%s:%d`
- `msgbox-using-alias`
- `site.AppleASCWrapV8SISP`
- `/Library/Caches/com.apple.xbs/AABFBD85-A37C-455C-9336-D4CF01B07B8C/TemporaryDirectory.eyQ48x/Sources/AppleA7IOP/AppleMessageBoxMailbox.cpp`
- `AppleMessageBoxMailbox::AppleMessageBoxMailbox(IOVirtualAddress, uint32_t, Aperture)`
- `_coreMappedRegs != 0`
- `msgbox-mailbox-num`
- `site.AppleASCWrapV8SEP`
- `AppleASCWrapV8ANE`
- `site.AppleASCWrapV8ANE`
- `nmi-ext-irq`
- `ext-irq-reg-index`
- `device_memory`
- `virtual IOReturn AppleASCWrapV8::getMailboxBulk(void *, unsigned int *)`
- `mailboxItem != nullptr`
- `AppleASCWrapV8SISP`
- `/Library/Caches/com.apple.xbs/AABFBD85-A37C-455C-9336-D4CF01B07B8C/TemporaryDirectory.eyQ48x/Sources/AppleA7IOP/AppleASCWrapCommon.cpp`
- `msgbox-using-postoffice`
- `idle-ctrl-check`
- `\"ASC firmware must be loaded by iBoot\" @%s:%d`
- `virtual bool AppleASCWrapV8::initialize()`
- `offset + sizeof(uint32_t) <= device_memory->getLength()`
- `_nmi_ext_irq_mapped`
- `ASC_RUNNING: False\n`
- `_msgboxMappedRegs != 0`
- `AppleMessageBoxMailbox.cpp`
- `Mailbox Status:\t0x%08x\n                                   Mailbox IRQRaw:\t0x%08x\n                                   Mailbox Link:\t0x%08x\n                                   Mailbox Credit:\t0x%08x\n`
