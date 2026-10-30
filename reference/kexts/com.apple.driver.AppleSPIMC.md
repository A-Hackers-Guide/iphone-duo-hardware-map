# `com.apple.driver.AppleSPIMC`

- Name: AppleSPIMC
- Version: `1`
- UUID: `70A6BE8D-10E9-365C-9EA4-C92E3E712D14`
- Source version: `40.40.4.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/spi1`](../devicetree/root__arm-io__spi1.md) | `AppleSPIMCController` | `spi-1,spimc` |

## IOKit personalities (1) [KC]

### AppleSPIMCController
- `CFBundleIdentifier`: `com.apple.driver.AppleSPIMC`
- `IOClass`: `AppleSPIMCController`
- `IONameMatch`: `spi-1,spimc`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPIMC`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleSPIMCController` | 0x1e10 | AppleARMSPIController → IOService → IORegistryEntry |
| `AppleSPIMCControllerStats` | 0x378 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001e07 off=0x0076a930-0x0076c737 addr=0xfffffe000776e930-0xfffffe0007770737 r--/r--   __TEXT            
	sz=0x00000010 off=0x0076afb0-0x0076afc0 addr=0xfffffe000776efb0-0xfffffe000776efc0               __TEXT.__const            
	sz=0x00001777 off=0x0076afc0-0x0076c737 addr=0xfffffe000776efc0-0xfffffe0007770737               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00006d1c off=0x0269c910-0x026a362c addr=0xfffffe00096a0910-0xfffffe00096a762c r-x/r-x   __TEXT_EXEC       
	sz=0x00006acc off=0x0269c910-0x026a33dc addr=0xfffffe00096a0910-0xfffffe00096a73dc          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000250 off=0x026a33dc-0x026a362c addr=0xfffffe00096a73dc-0xfffffe00096a762c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000130 off=0x04997a08-0x04997b38 addr=0xfffffe000b99ba08-0xfffffe000b99bb38 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x04997a08-0x04997acc addr=0xfffffe000b99ba08-0xfffffe000b99bacc               __DATA.__data             
	sz=0x00000068 off=0x00000000-0x00000068 addr=0xfffffe000b99bad0-0xfffffe000b99bb38               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000ae8 off=0x01202bd0-0x012036b8 addr=0xfffffe0008206bd0-0xfffffe00082076b8 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01202bd0-0x01202bd8 addr=0xfffffe0008206bd0-0xfffffe0008206bd8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01202bd8-0x01202be0 addr=0xfffffe0008206bd8-0xfffffe0008206be0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000840 off=0x01202be0-0x01203420 addr=0xfffffe0008206be0-0xfffffe0008207420         __DATA_CONST.__const            
	sz=0x00000080 off=0x01203420-0x012034a0 addr=0xfffffe0008207420-0xfffffe00082074a0         __DATA_CONST.__kalloc_type      
	sz=0x000000a0 off=0x012034a0-0x01203540 addr=0xfffffe00082074a0-0xfffffe0008207540         __DATA_CONST.__kalloc_var       
	sz=0x00000128 off=0x01203540-0x01203668 addr=0xfffffe0008207540-0xfffffe0008207668         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000050 off=0x01203668-0x012036b8 addr=0xfffffe0008207668-0xfffffe00082076b8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 84 at 0x04ae5978
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     70A6BE8D-10E9-365C-9EA4-C92E3E712D14
008: LC_SOURCE_VERSION           40.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab1a20 size=0xb0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleSPIMC`
- `CFBundleIdentifier`: `com.apple.driver.AppleSPIMC`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSPIMC`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
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
- `NSHumanReadableCopyright`: `Copyright © 2019 Apple, Inc. All rights reserved.`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleSPIMC.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898022096`
- `_PrelinkExecutableRelativePath`: `AppleSPIMC`
- `_PrelinkExecutableSize`: `38715`
- `_PrelinkExecutableSourceAddr`: `-2198898022096`
- `_PrelinkKmodInfo`: `-2198828631544`

## Strings (166) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%s:%s: %s, %s, status %#x, resid %#x\n`
- `xfer_hist_count != nullptr`
- `_spiProvider != nullptr`
- `%s.hwdelay`
- `spiCommand->spiCompletion.target == NULL`
- `%s: No hardware delay: pre=%#llX pst=%#llX kCS=%llX CSs=%d ics=%d enabled=%d\n`
- `%s: USING hardware delay pre: %d post: %d\n`
- `_spiRxDMAES is NULL`
- `%s:%s: timeout panicked, status=0x%08x\n`
- `%s:%s: command completed status=0x%08x, time=%lluns\n`
- `AppleSPIMCController::start: canot create Stats\n`
- `%s:%s: active cmd=%p, status=0x%08x\n`
- `%s: inactive cmd=%p, status=0x%08x\n`
- `multiDesc is NULL`
- `%s: start cmd=%p, status=0x%08x\n`
- `%s: _spiCommand is NULL\n`
- `%s:%s: status=0x%08x, _spiCommandDone=%d\n`
- `pollTimeouts != nullptr`
- `%s.debug`
- `Stats`
- `(_spiIES != NULL) || (_spiPollCtl.enable != 0)`
- `TX Byte count must be a 32 bit integer`
- `%s:%s: No hardware delay: pre=%#llX pst=%#llX kCS=%llX CSs=%d ics=%d enabled=%d\n`
- `_configureHardwareDelay`
- `no DMA and PIO`
- `_executeSPICommandDMA`
- `nclk`
- `%s %s:%d: _spiBaseAddress = %#lx:%#lx, _spiInternalCS = %d, allowHWDelay = %d, usePSD=%d, powerOffDelay=%u\n`
- `%s %s:%d: no IES\n`
- `%s: rx start cmd=%p, status=0x%08x\n`
- `%s: rx end/tx start cmd=%p, status=0x%08x\n`
- `%s:%s: thread awakened status=0x%08x, _spiCommandDone=%d\n`
- `\"%s: Calling thread needs to own the gate!\" @%s:%d`
- `%s %s:%d: transaction timeout!\n`
- `/Library/Caches/com.apple.xbs/6DC2BD53-8FF0-4378-84F7-E41C36CCEAA0/TemporaryDirectory.WTwA5y/Sources/AppleSPIMC/Kernel/AppleSPIMC.cpp`
- `%s:%s: rx start cmd=%p, status=0x%08x\n`
- `%s:%s: interrupt done break, status=0x%08x\n`
- `size_array != nullptr`
- `internal-cs`
- `idle-off-delay-us`
- `%s:%s: idle off\n`
- `_dmaAbort`
- `AppleSPIMCControllerStats`
- `intrTimeouts != nullptr`
- `autoPollCount != nullptr`
- `osn != nullptr`
- `%s: %s, %s, status %#x, resid %#x\n`
- `_dmaStop`
- `%s:%s: status=0x%08x, _spiConReg=0x%08x, _spiConRegCurrent=0x%08x\n`
- `%s: timeout panicked, status=0x%08x\n`
- `poll_hist_count != nullptr`
- `121111121222121211111221112121121111122122211222221122222112222221111112111111211111121111112111111211111121111112111111211111121111112111111211111121111112111111211111121111112111111211111121111112111111211111121111112111111211111121111112111111211111121111112111111211111121111112111111211111121111`
- `spiCommand->txByteCount <= UINT32_MAX`
- `_spiTxDMAES is NULL`
- `descs != NULL`
- `%s:%s: start cmd=%p, status=0x%08x\n`
- `_executeSPICommandPIO`
- `%s: Thread timeout premature, dt %lld, status=0x%08x\n`
- `xfer_hist_count`
- `site.IOMemoryDescriptor *`
- `\"%s: Timeout polling for completion\" @%s:%d`
- `disb_intrs_active != nullptr`
- `disb_intrs_active`
- `size`
- `AppleSPIMCController`
- `AppleSPIMCAssert: %s: %s, %s file: %s, line: %d\n`
- `%s.cclk`
- `%s:%s: rx end/tx start cmd=%p, status=0x%08x\n`
- `%s:%s: thread timeout, polling status=0x%08x\n`
- `%s:%s: %s, %s, direction %#x, status %#x, %#x\n`
- `%s: %s: sleeping...\n`
- `%s:%s: _spiCommand is NULL\n`
- `%s:%s: interrupt done, status=0x%08x\n`
- `spiCommand->rxByteCount <= UINT32_MAX`
- `_spiTxDMAES != NULL`
- `rxBuffer is NULL`
- `%s: command completed status=0x%08x, time=%lluns\n`
- `121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221`
- `multiDesc != NULL`
- `%s:%s: enabled status=0x%08x\n`
- `%s: SPCON programmed status=0x%08x\n`
- `%s:%s: direction %s, status %#x\n`
- `disb_intrs_inactive != nullptr`
- `async completion not supported`
- `_interruptActionSubr`
- `site.AppleSPIMCControllerStats`
- `poll_array != nullptr`
- `site.AppleSPIMCController`
- `RX Byte count must be a 32 bit integer`
- `txBuffer is NULL`
- `_interruptPoll`
- `disb_intrs_inactive`
- `xfer_array != nullptr`
- `exec_array != nullptr`
- `exec`
- `%s %s:%d: using CCLK %llu`
- `%s:%s: SPCON programmed status=0x%08x\n`
- `%s: thread timeout, polling status=0x%08x\n`
- `awakened`
- `%s: active=%d\n`
- `xfer`
- `%s::%s: return false\n`
- `Stats != nullptr`
- `_spiCClkFrequency != 0`
- `%s:%s: inactive cmd=%p, status=0x%08x\n`
- `%s: idle off\n`
- `%s:%s: tx end cmd=%p, status=0x%08x, time=%llxns\n`
- `\"%d -- %s: Timeout waiting for completion rdar://16910843\" @%s:%d`
- `poll_hist_count`
- `start`
- `startDMACommand (RX) error`
- `rx`
- `%s: interrupt done break, status=0x%08x\n`
- `_spiMemoryMap != 0`
- `%s: status=0x%08x, _spiConReg=0x%08x, _spiConRegCurrent=0x%08x\n`
- `intrTimeouts`
- `autoPollCount`
- `_spiIES is NULL and _spiPollCtl disabled`
- `1`
- `%s: thread awakened status=0x%08x, _spiCommandDone=%d\n`
- `OSNumber::withNumber ret NULL\n`
- `nix poll_array->setObject ret false\n`
- `_enableDeviceClock`
- `%s: tx end cmd=%p, status=0x%08x, time=%llxns\n`
- `%s: enabled status=0x%08x\n`
- `_dmaWait`
- `%s:%s: %s: stopDMACommand error %x\n`
- `%s: active cmd=%p, status=0x%08x\n`
- `_spiRxDMAES != NULL`
- `result == kIOReturnSuccess`
- `tx`
- `%s:%s: Thread timeout premature, dt %lld, status=0x%08x\n`
- `_powerOffTimerCallback`
- `_dmaEventAction`
- `nix size_array->setObject ret false\n`
- `extraTXPage != nullptr`
- `startDMACommand (TX) error`
- `%s:%s: %s: woke %d, status %#x\n`
- `%s:%s: active=%d\n`
- `(_spiTxCount == 0) || (_spiTxBuffer != NULL)`
- `%s: %s: woke %d, status %#x\n`
- `%s: %s: stopDMACommand error %x\n`
- `%s: direction %s, status %#x\n`
- `nix xfer_array->setObject ret false\n`
- `service-gates`
- `AppleSPIMC.cpp`
- `%s: %s, %s, direction %#x, status %#x, %#x\n`
- `%s: interrupt done, status=0x%08x\n`
- `%s: status=0x%08x, _spiCommandDone=%d\n`
- `success`
- `serialize`
- `%s:%s: USING hardware delay pre: %d post: %d\n`
- `(_spiRxCount == 0 || spiCommand->rxBufferMD != NULL) && (_spiTxCount == 0 || spiCommand->txBufferMD != NULL)`
- `pollTimeouts`
- `OSArray::withCapacity ret NULL\n`
- `poll`
- `%s %s:%d: Done.\n`
- `function-spi_cs%d`
- `dictionary`
- `nix exec_array->setObject ret false\n`
- `descs allocation failed`
- `(_spiRxCount == 0) || (_spiRxBuffer != NULL)`
- `transferSizeAtTimeout`
- `timed out`
- `%s:%s: %s: sleeping...\n`
- `setSPIControllerActive`
