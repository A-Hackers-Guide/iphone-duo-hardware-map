# `com.apple.driver.AppleIOPADMAStream`

- Name: AppleIOPADMAStream
- Version: `400.12`
- UUID: `10DD8AF3-50E0-3795-9A16-BDFDFC0E43A6`
- Source version: `400.12.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleAudioClockLibs`](com.apple.driver.AppleAudioClockLibs.md) 1.0, [`com.apple.driver.AppleEmbeddedAudioLibs`](com.apple.driver.AppleEmbeddedAudioLibs.md) 1.0, [`com.apple.driver.AppleIISController`](com.apple.driver.AppleIISController.md) 1.0.0, [`com.apple.driver.AudioDMAFamily`](com.apple.driver.AudioDMAFamily.md) 1.0, [`com.apple.iokit.IOPAudioDriverFamily`](com.apple.iokit.IOPAudioDriverFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (11) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/iop-audio-controller/audio-hp`](../devicetree/root__arm-io__iop-audio-controller__audio-hp.md) | `AppleIOPADMAStream` | `iop-adma-stream,mca` |
| [`/arm-io/iop-audio-controller/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback.md) | `AppleIOPADMAStream` | `iop-adma-stream,leap` |
| [`/arm-io/iop-audio-controller/audio-mca-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-mca-loopback.md) | `AppleIOPADMAStream` | `iop-adma-stream,mca` |
| [`/arm-io/iop-audio-controller/audio-receiver`](../devicetree/root__arm-io__iop-audio-controller__audio-receiver.md) | `AppleIOPADMAStream` | `iop-adma-stream,mca` |
| [`/arm-io/iop-audio-controller/audio-flicker`](../devicetree/root__arm-io__iop-audio-controller__audio-flicker.md) | `AppleIOPADMAStream` | `iop-adma-stream,mca` |
| [`/arm-io/iop-audio-controller/audio-s-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-s-leap-internal-loopback.md) | `AppleIOPADMAStream` | `iop-adma-stream,leap` |
| [`/arm-io/iop-audio-controller/lp-mic-injection-device`](../devicetree/root__arm-io__iop-audio-controller__lp-mic-injection-device.md) | `AppleIOPADMAStream` | `iop-adma-stream,mca` |
| [`/arm-io/iop-audio-controller/audio-speaker-mca`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker-mca.md) | `AppleIOPADMAStream` | `iop-adma-stream,mca` |
| [`/arm-io/iop-audio-controller/audio-speaker-tap`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker-tap.md) | `AppleIOPADMAStream` | `iop-adma-stream,mca` |
| [`/arm-io/iop-audio-controller/audio-haptic-transport`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic-transport.md) | `AppleIOPADMAStream` | `iop-adma-stream,leap` |
| [`/arm-io/iop-audio-controller/audio-hpdbg-transport`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg-transport.md) | `AppleIOPADMAStream` | `iop-adma-stream,leap` |

## IOKit personalities (1) [KC]

### AppleIOPADMAStream
- `CFBundleIdentifier`: `com.apple.driver.AppleIOPADMAStream`
- `IOClass`: `AppleIOPADMAStream`
- `IONameMatch`:
  - `iop-adma-stream,mca`
  - `iop-adma-stream,leap`
  - `iop-adma-stream,sense`
  - `iop-adma-stream,aspen`
- `IOPersonalityPublisher`: `com.apple.driver.AppleIOPADMAStream`
- `IOProviderClass`: `IOPAudioNode`
- `mca-uses-iopm-overrides`: `true`


## C++ classes (4) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleIASMCA` | 0x3c8 | AppleARMIISController → IOService → IORegistryEntry |
| `AppleIOPADMAStream` | 0x700 | AppleIASMCA → AppleARMIISController → IOService → IORegistryEntry |
| `IASClientManager` | 0x50 |  |
| `IASDMAChannelManager` | 0x28 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000059cc off=0x0051cfa0-0x0052296c addr=0xfffffe0007520fa0-0xfffffe000752696c r--/r--   __TEXT            
	sz=0x000000f9 off=0x0051d670-0x0051d769 addr=0xfffffe0007521670-0xfffffe0007521769               __TEXT.__const            
	sz=0x000035f8 off=0x0051d769-0x00520d61 addr=0xfffffe0007521769-0xfffffe0007524d61               __TEXT.__cstring          (CstringLiterals)
	sz=0x00001c0b off=0x00520d61-0x0052296c addr=0xfffffe0007524d61-0xfffffe000752696c               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00013a64 off=0x02009fd0-0x0201da34 addr=0xfffffe000900dfd0-0xfffffe0009021a34 r-x/r-x   __TEXT_EXEC       
	sz=0x000135b4 off=0x02009fd0-0x0201d584 addr=0xfffffe000900dfd0-0xfffffe0009021584          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000004b0 off=0x0201d584-0x0201da34 addr=0xfffffe0009021584-0xfffffe0009021a34          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000238 off=0x0494d398-0x0494d5d0 addr=0xfffffe000b951398-0xfffffe000b9515d0 rw-/rw-   __DATA            
	sz=0x00000188 off=0x0494d398-0x0494d520 addr=0xfffffe000b951398-0xfffffe000b951520               __DATA.__data             
	sz=0x000000b0 off=0x00000000-0x000000b0 addr=0xfffffe000b951520-0xfffffe000b9515d0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001708 off=0x01111840-0x01112f48 addr=0xfffffe0008115840-0xfffffe0008116f48 rw-/rw-   __DATA_CONST      
	sz=0x00000020 off=0x01111840-0x01111860 addr=0xfffffe0008115840-0xfffffe0008115860         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000020 off=0x01111860-0x01111880 addr=0xfffffe0008115860-0xfffffe0008115880         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001228 off=0x01111880-0x01112aa8 addr=0xfffffe0008115880-0xfffffe0008116aa8         __DATA_CONST.__const            
	sz=0x00000180 off=0x01112aa8-0x01112c28 addr=0xfffffe0008116aa8-0xfffffe0008116c28         __DATA_CONST.__kalloc_type      
	sz=0x00000050 off=0x01112c28-0x01112c78 addr=0xfffffe0008116c28-0xfffffe0008116c78         __DATA_CONST.__kalloc_var       
	sz=0x00000258 off=0x01112c78-0x01112ed0 addr=0xfffffe0008116c78-0xfffffe0008116ed0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000078 off=0x01112ed0-0x01112f48 addr=0xfffffe0008116ed0-0xfffffe0008116f48         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 165 at 0x04add140
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     10DD8AF3-50E0-3795-9A16-BDFDFC0E43A6
008: LC_SOURCE_VERSION           400.12.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa5378 size=0x160
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleIOPADMAStream`
- `CFBundleIdentifier`: `com.apple.driver.AppleIOPADMAStream`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleIOPADMAStream`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `400.12`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `400.12`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2023 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
  - `2`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleIOPADMAStream.kext`
- `_PrelinkExecutableLoadAddr`: `-2198900437088`
- `_PrelinkExecutableRelativePath`: `AppleIOPADMAStream`
- `_PrelinkExecutableSize`: `109936`
- `_PrelinkExecutableSourceAddr`: `-2198900437088`
- `_PrelinkKmodInfo`: `-2198828936296`

## Strings (509) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `IASClientManager.cpp`
- `getAPMCAConfig`
- `%s::%s@%d: Dropping Computed Tx Fifo %d on the floor\n`
- `%s::%s@%d: config has no active TX %d nor RX %d channels\n`
- `%s@%s::%s:%d: %p, %p \"%s\", %p vs. %p\n`
- `nub != nullptr`
- `/Library/Caches/com.apple.xbs/0B7523CF-8499-456F-8339-DF1B4FF76BA8/TemporaryDirectory.0iB1H1/Sources/AppleIOPADMAStream/Source/AppleIOPADMAStream.cpp`
- `%s::%s:%d: no iisConfig 'reg' property in %s\n`
- ` smpl: %dbits`
- `validIISConfigLeap`
- `%s::%s@%d: icTxBitsPerChannel %d > iisTxBitsPerSlot %d\n`
- `stopDevice`
- `%s::%s:%d: iisConfig 'reg' property too short in %s\n`
- `%s::%s:%d: Can't set %s dma action\n`
- `%s::%s@%d: can't create name symbol, no memory\n`
- `%s::%s@%d: RegisterOn '%-4.4s' StartIO '%-4.4s'\n`
- `%s::%s@%d: Tx dataDelay %d >= frame size %d\n`
- `current`
- `%s::%s@%d: Ignoring: no MCLK configured\n`
- `%s::%s@%d: SyncGen redefinition was '%4.4s' now '%4.4s'\n`
- `registerPowerDriver failed`
- `%s::%s@%d: %s: data delay %d longer than frame %d\n`
- `setTxFIFODepth`
- `dis`
- `%s::%s@%d: Unable to get node state while attempting to set active mode = %x: %s(%x)\n`
- `\"%s::%s:\" \"Name char buf too small %d < %d\" @%s:%d`
- `setConfig`
- `\"%s::%s:\" \"[%s->%s] called, no override?\" @%s:%d`
- `%s::%s@%d: Error setting config %s(%#x)\n`
- `%s::%s@%d: icTxBitsPerChannel %d too large\n`
- `%s::%s@%d: max rxChannelMask %#x > iisNumChannels %d\n`
- `%s::%s@%d: Invalid IISConfig\n`
- `%s::%s@%d: Idle request failed %s(%x)\n`
- `%s@%s::%s:%d: cannot get phandle at index=%u of %u\n`
- `external-power-provider`
- `%s@%s::%s:%d: dir%d txm%x rxm%x nc%d mm%x cpf%d\n`
- `%s::%s@%d: Tx unexpected bits per slot %d\n`
- `%s::%s@%d: Bad timing in iisConfig, use LogMask::kIisCfg for details\n`
- `%s::%s@%d: Unexpected node state %-4.4s\n`
- `%s::%s@%d: TxSerDes redefinition was '%4.4s' now '%4.4s'\n`
- `%s::%s@%d: Unable to register IOInterruptEventSource: %s(%#x)\n`
- `powerStateWillChangeToGated`
- `ControllerActive`
- `%s::%s:%d: enter: %p\n`
- `v24@?0^v8^{AppleARMIISCommand=^^?i{queue_entry=^{queue_entry}^{queue_entry}}^vQQII^{IOMapper}^{IOMemoryDescriptor}^?IIIII^{IODMACommandInternal}I^{AppleARMIISController}^{IOMemoryDescriptor}IQQ{mach_timespec=Ii}Qi{AppleARMIISCompletion=^v^?^v}{queue_entry=^{queue_entry}^{queue_entry}}}16`
- `initForPM`
- `\"%s::%s:\" \"Unexpected property size %d\" @%s:%d`
- `dma-provider-tx`
- `completeCommands`
- `control-only`
- `falling`
- `setActive`
- `%s::%s@%d: inactive '%-4.4s' %s(%#x)\n`
- `mcaExternalPower.manager != nullptr`
- `%s::%s@%d: Incompatible rx channel count %d %d\n`
- `%s::%s@%d: Non NCO computed frequency %d\n`
- `request`
- `%s::%s@%d: PowerOn %x(%s%s) request failed %s(%x)\n`
- `submitCommand`
- `%s::%s:%d: Deactivation failed: %s(%#x).\n`
- `%s::%s@%d: dataDelay %d >= frame size %d\n`
- `%s::%s@%d: icRxBitsPerChannel %d > iisRxBitsPerSlot %d\n`
- `%s::%s@%d: no channels\n`
- `/Library/Caches/com.apple.xbs/0B7523CF-8499-456F-8339-DF1B4FF76BA8/TemporaryDirectory.0iB1H1/Sources/AppleIOPADMAStream/Source/AppleIASMCA.cpp`
- `%s@%s::%s:%d: AppleIASMCA::newDeviceWithRegistryEntry returned NULL\n`
- `%s::%s@%d: Unexpected error setting IOPDeviceNode(%#x), %s(%x)\n`
- `prepareStream`
- `%s::%s@%d: Rx unexpected bits per slot %d\n`
- `12112`
- `initWithIODMAEventSource`
- `%s::%s:%d: No %s dma-channel configured\n`
- `%s::%s:%d: Timeout received from AOP, silenced.\n`
- `id: '%-4.4s' src: '%-4.4s' div: %u`
- `%s::%s@%d: Invalid: changing immutable configuration\n`
- `%s::%s@%d: Rx dataDelay %d >= frame size %d\n`
- `%s::%s@%d: ClockGen redefinition was '%4.4s' now '%4.4s'\n`
- `IASDMAChannelManager.cpp`
- `%s::%s@%d: No dma-parent defined\n`
- `%s::%s:%d: \n`
- `-ias_drop_iop_comms_to`
- `%s::%s:%d: Bad direction %x\n`
- `rv == kIOReturnSuccess`
- `getNodeState`
- `%s::%s@%d: Command memory descriptor unexpectedly changed\n`
- `self != nullptr`
- `powerStateDidChangeToGated`
- `probe`
- `%s: Activating the controller returned \"%s\"`
- `MSBFirst`
- `\"%s::%s:\" \"Lock assertion failed\" @%s:%d`
- `%s::%s@%d: Unexpected error getting current value from IOPDeviceNode(%#x), %s(%x)\n`
- `%s::%s@%d: Marking device inactive without calling stop\n`
- `%s::%s@%d: DC MCLK frequency not supported\n`
- `start`
- `%s::%s:%d: with no active channels\n`
- `%s::%s:%d: Bad argument: no direction given\n`
- `%s::%s@%d: iisTxBitsPerSlot %d too large\n`
- `%s::%s@%d: NCO computed frequency %d\n`
- `%s::%s@%d: Ignoring: independent MCLK enable not available\n`
- `\"%s::%s:\" \"No ADMAC suspend ARMFunction for %s\" @%s:%d`
- `%s::%s@%d: No DMA for %s\n`
- `%s::%s@%d: Configured blck %d too small for %d bit frame\n\n`
- `%s::%s@%d: Searching for %s\n`
- `copyAdmacPowerProvider`
- `\"%s::%s:\" \"Repeat transfer completion without pending command\" @%s:%d`
- `1`
- `matchingNotificationHandlerGated`
- `provider is NULL`
- `%s@%-4.4s`
- `id: '%-4.4s' src: '%-4.4s' edge: %s pulse: %s count: %u`
- `Rx`
- `site.AppleIASMCA`
- `cannot allocate AppleExternalPowerManager`
- `%s::%s:%d: ret %u\n`
- `%s::%s@%d: %s: numChannels out of range %d\n`
- `%s::%s@%d: %s: Tx channelMask %x mismatches numChannels %d\n`
- `%s::%s@%d: %s: RX channelMask %x mismatches numChannels %d\n`
- `setIISControllerActive_Forced`
- `\"%s::%s[%s]@%u: called, no override?\" @%s:%d`
- `setDMAConfig failed`
- `clkgen %s`
- `%s::%s@%d: %s: Tx bits per channel %d out of range\n`
- `iis`
- `%s::%s@%d: abortTransfers returned %s(%#x)\n`
- `%s::%s@%d: Unable to read kCMStartIOStateID from iopNode: %s(%#x)\n`
- `%s::%s@%d: Malformed dma-parent data\n`
- `rv`
- `mcaExternalPower.matchingNotifiers != nullptr`
- `%s@%s::%s:%d: ret %u\n`
- `getDefaultIISConfig`
- `%s::%s@%d: %s: Unexpected error reading IOPDeviceNode property id(%#x), %s(%x)\n`
- `%s::%s@%d: Error reading config %s(%#x)\n`
- `%s::%s@%d: Unable to get node state while attempting to start device %x(%s%s): %s(%x)\n`
- `%s::%s@%d: Ignoring provider '%s': no dma property found, or it was wrong type\n\n`
- `setMCLKEnabled`
- `tx`
- `%s::%s@%d: owner->getProvider() returned null\n`
- `%s::%s@%d: MCA reset failed: %s(%#x)\n`
- `%s::%s@%d: requested IISConfig is incompatible with default\n`
- `%s::%s@%d: Error reading DMA configuration for %s: %s(%#x)\n`
- `%s::%s@%d: No active %s DMA\n`
- `%s::%s@%d: Unable to register eventsource: %s(%#x)\n`
- `\"%s::%s:\" \"[%s] called, no override?\" @%s:%d`
- `%s.%s`
- `\"%s::%s:\" \"Failed to deactivate ADMAC due to %s(%x)\" @%s:%d`
- `rising`
- `Tx`
- `%s::%s@%d: Transition down to Prewarm failed, %s(%x)\n`
- `\"%s::%s:\" \"Gate not held\" @%s:%d`
- `%s::%s:%d: return: %p, line %u, %#x\n`
- `%s::%s:%d: direction %#x\n`
- `id: '%-4.4s' edge: %s delay: %u channels: %d(%#llx) slot: %ubits(%s)`
- `%s::%s@%d: %s: Legacy I2S Mode requires an even framesize %d\n`
- `%s::%s@%d: Failed to allocate IOInterruptEventSource\n`
- `%s::%s@%d: bad config cc%d, bpc%d hz%d: %s(%#x)\n`
- `v16@?0r^{CompletionCallbackContext=QI}8`
- `startIISCommand`
- `initWithIOPNode`
- `setGetNodeProperty`
- `%s::%s@%d: ClockGenOutputPinMask redefinition was %x now %x\n`
- `%s::%s@%d: Found %s channel\n`
- `bad provider`
- `iisCommandGate is NULL`
- `debug`
- `%s::%s@%d: can't create mcaName string, no memory\n`
- `setGetAPMCAConfig`
- `%s::%s@%d: %s: Tx channelMask %x mismatches channelCount %d\n`
- `%s::%s@%d: RxSerDes redefinition was '%4.4s' now '%4.4s'\n`
- `self is NULL`
- `site.AppleIOPADMAStream`
- `site.IASClientManager`
- `%s::%s@%d: Couldn't find channel %s\n`
- `%s::%s@%d: Unable to allocate IODMAEventSource\n`
- `validConfig`
- `apmcaconfig '%-4.4s' %s`
- `mclk: %x blck: %x txs: %x txl %x rxs: %x rxl: %x`
- `%s::%s@%d: icRxBitsPerChannel %d too large\n`
- `mergeAPMCA`
- `%s::%s@%d: SyncGen BCLK redefinition was '%4.4s' now '%4.4s'\n`
- `%s::%s@%d: MCLKOutputPinMask redefinition was %x now %x\n`
- `%s::%s:%d: Can't init power management %s(%x)\n`
- `%s::%s@%d: setConfigSwitch request failed %s(%x)\n`
- `setIISConfigMca`
- `mcaDeferredStartCallout != nullptr`
- `result == kIOReturnSuccess`
- `iisConfig`
- `safety`
- `%s::%s@%d: Bad dma-config %d\n`
- `%s::%s@%d: Unable to startDMACommand: %s(%#x)\n`
- `%s::%s@%d: Unable to transfer memory descriptor: %s(%#x)\n`
- `validDMAConfig`
- `iop-adma-stream,mca`
- `\"%s::%s:\" \"No ADMAC suspend ARMFunction\" @%s:%d`
- `%s::%s@%d: external-power-provider: %s\n`
- `IOPowerManagement`
- `Name`
- `%s::%s@%d: Reset error %s(%#x)\n`
- `LSBFirst`
- `%s::%s@%d: Only Fixed MCLKs are currently supported\n`
- `thread_call_allocate returned NULL`
- `setIISConfig`
- `publishBelow`
- `%s::%s@%d: MCLK redefinition was '%4.4s' now '%4.4s'\n`
- `%s::%s@%d: ClockGen MCLK redefinition was '%4.4s' now '%4.4s'\n`
- `%s::%s@%d: Error trying to reset a Leap?: %s(%#x)\n`
- `%s::%s@%d: Failed to set stream cc%d, bpc%d hz%d: %s(%#x)\n`
- `\"%s::%s:\" \"Internal Error: No completion block\" @%s:%d`
- `%s::%s:%d: super::start failed\n`
- `start_block_invoke`
- `AppleIOPADMAStream.cpp`
- `iisConfig default`
- `%s::%s@%d: MCLK%s%s\n`
- `\"%s::%s:\" \"Internal error, bad size returned %ld\" @%s:%d`
- `%s::%s@%d: Can not determine bitsPerChannel\n\n`
- `%s::%s@%d: %s'%s' Bad direction %x, expected half duplex\n`
- `%s@%s::%s:%d: cannot create matching property index=%u of %u\n`
- `active`
- `stopIISCommand`
- `%s::%s@%d: MCA has%s MCLK Control, does%s routing validation and is%s immutable\n`
- `startDevice`
- `%s-%s@%s`
- `222211111111111211112`
- ` no`
- `%s::%s@%d: Unable to get node state while attempting to stop device: %s(%x)\n`
- `dma-provider-rx`
- `reg`
- `%s::%s@%d: \n`
- `%s::%s@%d: RxSerDesPinMask redefinition was %x or lbPinMask was %x now %x\n`
- `%s::%s@%d: Configured blck %d too small for number of Rx bits specified %d\n\n`
- `abortStream`
- `1211111212221212121222111111111121222222222222222222222222222222222222222222222222222221221112222222212221111111111111112`
- `%s@%s::%s:%d: device %s, powerStateOrdinal %lu, iisSuspend %u\n`
- `%s::%s:%d: %s-%s = %d frames\n`
- `%s::%s@%d: Unable to read kCMRegistersOnStateID from iopNode: %s(%#x)\n`
- `%s::%s@%d: %s: Rx channelMask %x mismatches channelCount %d\n`
- `, invalid auto`
- `%s::%s:%d: direction %#x, stopDMACommand returned %#x\n`
- `latency`
- `resetAPMCAStream`
- `tx serdes %s`
- `%s::%s@%d: Only iisMCLKTypeFixed is supported, %d is unexpected\n`
- `%s::%s@%d: TxSerDesPinMask redefinition was %x now %x\n`
- `%s::%s@%d: Can not parse dma-channels property\n`
- `%s::%s:%d: prepareStream failed %s(%x)\n`
- `rx serdes %s`
- `%s::%s@%d: %s: syncPulse len %d longer than frame %d\n`
- `%s::%s@%d: %s: Invalid default IISConfig('reg')\n`
- `%s::%s@%d: active '%-4.4s'\n`
- `%s::%s@%d: Mismatch channel %s IODirection is %s\n`
- `%s::%s@%d: df %x\n`
- `%s::%s@%d: iisRxBitsPerSlot %d too large\n`
- `%s::%s@%d: mclkCount %d must be greated than bits required %d\n\n`
- `i8@?0`
- `err == 0 `
- `syncgen %s`
- `%s::%s@%d: MCLK count %d not equivalent to frame frequency %d\n`
- `%s::%s@%d: Internal error: Failed to merge given iisConfig\n`
- `%s::%s@%d: Legacy i2s mode Frame too small %d for 2 %dbit channels\n`
- `static`
- `site.IONotifier *`
- `cannot allocate phandles array`
- `cannot setPopwerState 1`
- `ias`
- `getDefaultIISConfig failed`
- `%s::%s@%d: Incompatible tx channel count %d %d\n`
- `%s::%s@%d: Leap\n`
- `%s::%s@%d: MCLK Source redefinition was '%4.4s' now '%4.4s'\n`
- `cannot init deferred start`
- `function-admac_powerswitch`
- `v20@?0^{IOInterruptEventSource=^^?i^{IOEventSource}^{OSObject}^?B^{IOWorkLoop}^v^{ExpansionData}^{IOService}iIIBB^{ExpansionData}}8i16`
- `\"%s::%s:\" \"No ADMAC power managed driver found\" @%s:%d`
- `bad self`
- `executeIISCommand`
- `\"%s::%s:\" \"%llu %s: Failed to update controller state (%s => %s).\" @%s:%d`
- `setDMAConfig`
- `%s::%s@%d: Internal error: can't generate APMCAConfig from IIS\n`
- `%s::%s@%d: %sabling MCLK @%dhz, AOP %sabled\n`
- `\"%s::%s:\" \"Internal error, invalid IISConfig\" @%s:%d`
- `AssertMacros: %s: %s, %s file: %s, line: %d\n`
- `ndebug`
- `%s@%s`
- `%s::%s:%d: exit %s(%x)\n`
- `%s::%s@%d: PreWarm request failed %s(%x)\n`
- `%s::%s@%d: allocation failed\n`
- `%s::%s@%d: Unable to set DMAConfig for index %d: %s(%#x)\n`
- `%s::%s:%d: device %s, powerStateOrdinal %lu, iisSuspend %u\n`
- `device_type`
- ` out`
- `%s::%s@%d: %s: Rx bits per channel %d out of range\n`
- `AppleIASMCA.cpp`
- `getLatency`
- `generateAPMCAFromIIS`
- `dma-parent`
- `%s::%s@%d: mclkDivider %d is out of range\n`
- `(null)`
- `abortIISCommand`
- `%s::%s:%d: %s transferData requested with now dma configured\n`
- `%s::%s:%d: Ignore initial call from AppleARMIISController::start()\n`
- `\"%s::%s:\" \"Unexpected node type\" @%s:%d`
- `%s::%s@%d: '%-4.4s' %s(%#x)\n`
- `\"%s::%s:\" \"No workloop\" @%s:%d`
- `%s@%s::%s:%d: capabilities %#lx, device %s, powerStateOrdinal %lu, iisSuspend %u\n`
- `setPowerStateGated`
- `iisConfig valid`
- `%s::%s@%d: %s: Unexpected error reading node state: %s(%x)\n`
- `validIISConfigCommon`
- `%s::%s@%d: Tx Channel Mask requires larger than frame size\n`
- `%s::%s@%d: RX Channel Mask requires larger than frame size\n`
- `%s@%s::%s:%d: device %s, powerStateOrdinal %lu, super::setPowerStateGated returned %#x\n`
- `setIISConfig failed`
- ` not`
- `initForOwner`
- `%s::%s@%d: Unable to set depth to %d: %s(%#x)\n`
- `nub is NULL`
- `%s::%s@%d: MCLK frequency %d not supported\n`
- `site.IASDMAChannelManager`
- `hasDMAProperties`
- `%s::%s@%d: Internal error: iopNode null or wrong type\n`
- `generateMCATiming`
- `initWithADMAInterface`
- `computeParameters`
- `%s@%s::%s:%d: Name %s\n`
- `dmaConfig valid`
- `ret`
- `deactivate`
- `%s@%s::%s:%d: mcaExternalPower.manager %p addPowerProvider \"%s\", result %#x\n`
- `inactive`
- `provider != NULL`
- `%s::%s@%d: Starting device in '%-4.4s' direction %d that isn't in preWarm\n`
- `computeIISConfigAutos`
- `mca != nullptr`
- `actoffpanic`
- `rx`
- `1211112222`
- ` nco`
- `%s::%s@%d: Configured blck %d too small for number of Tx bits specified %d\n\n`
- `dmaCompleted`
- `dmaESCompleteAction`
- `getSupportedChannelCounts`
- `%s::%s:%d: Unexpectedly matching on wrong type provider, %s\n`
- `\"%s@%llu: Not all external devices on (%u) at sPS(1).\" @%s:%d`
- `en`
- `%s::%s@%d: Unknown MCLKType %#x\n\n`
- `deferredStartGated`
- `unknown class?`
- `reset`
- `mclk %s`
- ` rate: %u`
- `%s::%s@%d: Invalid bitsPerChannel %d%s\n`
- `site.T`
- `iisCommandGate != nullptr`
- `validIISConfig`
- `err == kIOReturnSuccess`
- `\"%s::%s:\" \"setDMAConfig failed with %#x.\" @%s:%d`
- `%s::%s@%d: Unsupported MCLK frequency %d\n`
- `%s::%s@%d: Specified BCLK %d is incompatible with PerFS clock type\n\n`
- `%s::%s@%d: name %s OSString failed\n`
- `%s::%s@%d: stopDMACommand returned %s(%#x)\n`
- `initExternalPowerGated`
- `%s::%s:%d: IAS Clientmanager stopDevice failed %s(%x)\n`
- `%s::%s@%d: Rx unexpected bits per channel %d\n`
- `%s::%s@%d: %d frequency does not agree with AAAFW %d nor adjusted %d\n`
- `%s::%s@%d: Preventative abortTransfers returned %s(%#x)\n`
- `super::start failed`
- `mca->iisCommandGate != nullptr`
- `uses-adma-latency-getter`
- `\"%s::%s:\" \"Failed to activate ADMAC due to %s(%x)\" @%s:%d`
- `id: '%-4.4s' src: '%-4.4s' freq: %u`
- `routing masks %s`
- `validIISConfigMca`
- `%s::%s@%d: max txChannelMask %#x > iisNumChannels %d\n`
- `12111112122212121212221111111111212222222222222222222222222222222222222222222222222222212211122222222122211111111111111122111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `initDMA`
- `%s::%s:%d: Bad argument error: both directions given\n`
- `getNodeProperty`

**[__TEXT.__os_log]**

- `%s::%s@%d: %s: Unexpected error reading IOPDeviceNode property id(%#x), %s(%x)\n`
- `%s::%s@%d: %s: Tx channelMask %x mismatches numChannels %d\n`
- `%s::%s@%d: MCLK count %d not equivalent to frame frequency %d\n`
- `%s::%s@%d: DC MCLK frequency not supported\n`
- `%s::%s@%d: Found %s channel\n`
- `%s::%s@%d: allocation failed\n`
- `%s::%s@%d: no channels\n`
- `%s::%s@%d: can't create mcaName string, no memory\n`
- `%s::%s@%d: Error trying to reset a Leap?: %s(%#x)\n`
- `%s::%s@%d: Error setting config %s(%#x)\n`
- `%s::%s@%d: iisRxBitsPerSlot %d too large\n`
- `%s::%s@%d: '%-4.4s' %s(%#x)\n`
- `%s::%s@%d: Invalid bitsPerChannel %d%s\n`
- `%s::%s@%d: Configured blck %d too small for %d bit frame\n\n`
- `%s::%s@%d: %s: Rx channelMask %x mismatches channelCount %d\n`
- `%s::%s@%d: MCLK frequency %d not supported\n`
- `%s::%s@%d: NCO computed frequency %d\n`
- `%s::%s@%d: SyncGen redefinition was '%4.4s' now '%4.4s'\n`
- `%s::%s@%d: Unknown MCLKType %#x\n\n`
- `%s::%s@%d: No dma-parent defined\n`
- `%s::%s@%d: MCA has%s MCLK Control, does%s routing validation and is%s immutable\n`
- `%s::%s@%d: %s: syncPulse len %d longer than frame %d\n`
- `%s::%s@%d: Invalid: changing immutable configuration\n`
- `%s::%s@%d: icRxBitsPerChannel %d too large\n`
- `%s::%s@%d: Rx dataDelay %d >= frame size %d\n`
- `%s::%s@%d: ClockGenOutputPinMask redefinition was %x now %x\n`
- `%s::%s@%d: Mismatch channel %s IODirection is %s\n`
- `%s::%s@%d: %s: RX channelMask %x mismatches numChannels %d\n`
- `%s::%s@%d: Internal error: can't generate APMCAConfig from IIS\n`
- `%s::%s@%d: Bad timing in iisConfig, use LogMask::kIisCfg for details\n`
- `%s::%s@%d: Can not determine bitsPerChannel\n\n`
- `%s::%s@%d: Error reading DMA configuration for %s: %s(%#x)\n`
- `%s::%s@%d: Unable to set depth to %d: %s(%#x)\n`
- `%s::%s@%d: Internal error: iopNode null or wrong type\n`
- `%s::%s@%d: Unable to read kCMStartIOStateID from iopNode: %s(%#x)\n`
- `%s::%s@%d: Incompatible tx channel count %d %d\n`
- `%s::%s@%d: Tx unexpected bits per slot %d\n`
- `%s::%s@%d: TxSerDesPinMask redefinition was %x now %x\n`
- `%s::%s@%d: Tx dataDelay %d >= frame size %d\n`
- `%s::%s@%d: inactive '%-4.4s' %s(%#x)\n`
- `%s::%s@%d: ClockGen MCLK redefinition was '%4.4s' now '%4.4s'\n`
- `%s::%s@%d: Unable to register eventsource: %s(%#x)\n`
- `%s::%s@%d: Failed to set stream cc%d, bpc%d hz%d: %s(%#x)\n`
- `%s::%s@%d: MCA reset failed: %s(%#x)\n`
- `%s::%s@%d: %s: Unexpected error reading node state: %s(%x)\n`
- `%s::%s@%d: Unexpected error getting current value from IOPDeviceNode(%#x), %s(%x)\n`
- `%s::%s@%d: icTxBitsPerChannel %d too large\n`
- `%s::%s@%d: Starting device in '%-4.4s' direction %d that isn't in preWarm\n`
- `%s::%s@%d: MCLK redefinition was '%4.4s' now '%4.4s'\n`
- `%s::%s@%d: Configured blck %d too small for number of Rx bits specified %d\n\n`
- `%s::%s@%d: MCLK%s%s\n`
- `%s::%s@%d: Couldn't find channel %s\n`
- `%s::%s@%d: Unable to startDMACommand: %s(%#x)\n`
- `%s::%s@%d: Invalid IISConfig\n`
- `%s::%s@%d: Unable to get node state while attempting to set active mode = %x: %s(%x)\n`
- `%s::%s@%d: Idle request failed %s(%x)\n`
- `%s::%s@%d: Transition down to Prewarm failed, %s(%x)\n`
- `%s::%s@%d: ClockGen redefinition was '%4.4s' now '%4.4s'\n`
- `%s::%s@%d: Unable to transfer memory descriptor: %s(%#x)\n`
- `%s::%s@%d: Rx unexpected bits per slot %d\n`
- `%s::%s@%d: Marking device inactive without calling stop\n`
- `%s::%s@%d: mclkCount %d must be greated than bits required %d\n\n`
- `%s::%s@%d: Specified BCLK %d is incompatible with PerFS clock type\n\n`
- `%s::%s@%d: Error reading config %s(%#x)\n`
- `%s::%s@%d: Ignoring: no MCLK configured\n`
- `%s::%s@%d: Ignoring: independent MCLK enable not available\n`
- `%s::%s@%d: PreWarm request failed %s(%x)\n`
- `%s::%s@%d: %s: Tx channelMask %x mismatches channelCount %d\n`
- `%s::%s@%d: Unable to get node state while attempting to start device %x(%s%s): %s(%x)\n`
- `%s::%s@%d: Only iisMCLKTypeFixed is supported, %d is unexpected\n`
- `%s::%s@%d: MCLK Source redefinition was '%4.4s' now '%4.4s'\n`
- `%s::%s@%d: RxSerDesPinMask redefinition was %x or lbPinMask was %x now %x\n`
- `%s::%s@%d: Malformed dma-parent data\n`
- `%s::%s@%d: external-power-provider: %s\n`
- `%s::%s@%d: icTxBitsPerChannel %d > iisTxBitsPerSlot %d\n`
- `%s::%s@%d: active '%-4.4s'\n`
- `%s::%s@%d: No DMA for %s\n`
- `%s::%s@%d: PowerOn %x(%s%s) request failed %s(%x)\n`
- `%s::%s@%d: stopDMACommand returned %s(%#x)\n`
- `%s::%s@%d: Preventative abortTransfers returned %s(%#x)\n`
- `%s::%s@%d: RegisterOn '%-4.4s' StartIO '%-4.4s'\n`
- `%s::%s@%d: Internal error: Failed to merge given iisConfig\n`
- `%s::%s@%d: %sabling MCLK @%dhz, AOP %sabled\n`
- `%s::%s@%d: Searching for %s\n`
- `%s::%s@%d: df %x\n`
- `%s::%s@%d: setConfigSwitch request failed %s(%x)\n`
- `%s::%s@%d: dataDelay %d >= frame size %d\n`
- `%s::%s@%d: \n`
- `%s::%s@%d: Unsupported MCLK frequency %d\n`
- `%s::%s@%d: TxSerDes redefinition was '%4.4s' now '%4.4s'\n`
- `%s::%s@%d: Unable to read kCMRegistersOnStateID from iopNode: %s(%#x)\n`
- `%s::%s@%d: %s: Tx bits per channel %d out of range\n`
- `%s::%s@%d: %s: Legacy I2S Mode requires an even framesize %d\n`
- `%s::%s@%d: Legacy i2s mode Frame too small %d for 2 %dbit channels\n`
- `%s::%s@%d: owner->getProvider() returned null\n`
- `%s::%s@%d: Rx unexpected bits per channel %d\n`
- `%s::%s@%d: SyncGen BCLK redefinition was '%4.4s' now '%4.4s'\n`
- `%s::%s@%d: Command memory descriptor unexpectedly changed\n`
- `%s::%s@%d: %s: numChannels out of range %d\n`
- `%s::%s@%d: mclkDivider %d is out of range\n`
- `%s::%s@%d: requested IISConfig is incompatible with default\n`
- `%s::%s@%d: max txChannelMask %#x > iisNumChannels %d\n`
- `%s::%s@%d: Non NCO computed frequency %d\n`
- `%s::%s@%d: Unexpected node state %-4.4s\n`
- `%s::%s@%d: bad config cc%d, bpc%d hz%d: %s(%#x)\n`
- `%s::%s@%d: can't create name symbol, no memory\n`
- `%s::%s@%d: max rxChannelMask %#x > iisNumChannels %d\n`
- `%s::%s@%d: Dropping Computed Tx Fifo %d on the floor\n`
- `%s::%s@%d: Failed to allocate IOInterruptEventSource\n`
- `%s::%s@%d: Unable to register IOInterruptEventSource: %s(%#x)\n`
- `%s::%s@%d: iisTxBitsPerSlot %d too large\n`
- `%s::%s@%d: %s: Rx bits per channel %d out of range\n`
- `%s::%s@%d: %s: Invalid default IISConfig('reg')\n`
- `%s::%s@%d: Unable to get node state while attempting to stop device: %s(%x)\n`
- `%s::%s@%d: Can not parse dma-channels property\n`
- `%s::%s@%d: Bad dma-config %d\n`
- `%s::%s@%d: %s: data delay %d longer than frame %d\n`
- `%s::%s@%d: Only Fixed MCLKs are currently supported\n`
- `%s::%s@%d: Incompatible rx channel count %d %d\n`
- `%s::%s@%d: RX Channel Mask requires larger than frame size\n`
- `%s::%s@%d: Leap\n`
- `%s::%s@%d: RxSerDes redefinition was '%4.4s' now '%4.4s'\n`
- `%s::%s@%d: MCLKOutputPinMask redefinition was %x now %x\n`
- `%s::%s@%d: config has no active TX %d nor RX %d channels\n`
- `%s::%s@%d: Configured blck %d too small for number of Tx bits specified %d\n\n`
- `%s::%s@%d: Unable to allocate IODMAEventSource\n`
- `%s::%s@%d: Unable to set DMAConfig for index %d: %s(%#x)\n`
- `%s::%s@%d: abortTransfers returned %s(%#x)\n`
- `%s::%s@%d: Reset error %s(%#x)\n`
- `%s::%s@%d: icRxBitsPerChannel %d > iisRxBitsPerSlot %d\n`
- `%s::%s@%d: %d frequency does not agree with AAAFW %d nor adjusted %d\n`
- `%s::%s@%d: Unexpected error setting IOPDeviceNode(%#x), %s(%x)\n`
- `%s::%s@%d: Tx Channel Mask requires larger than frame size\n`
- `%s::%s@%d: No active %s DMA\n`
