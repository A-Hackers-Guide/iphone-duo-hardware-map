# `com.apple.driver.IOPHaptics`

- Name: IOPHaptics
- Version: `1010.2`
- UUID: `F2CB4021-D81D-39AD-B282-2D8E986E5EB5`
- Source version: `1010.2.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0, [`com.apple.driver.AppleEmbeddedAudio`](com.apple.driver.AppleEmbeddedAudio.md) 1.1.0, [`com.apple.driver.AppleIISController`](com.apple.driver.AppleIISController.md) 1.0, [`com.apple.driver.IOPEmbeddedAudio`](com.apple.driver.IOPEmbeddedAudio.md) 1.0, [`com.apple.iokit.AppleARMIISAudio`](com.apple.iokit.AppleARMIISAudio.md) 1.0, [`com.apple.iokit.IOAudio2Family`](com.apple.iokit.IOAudio2Family.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (2) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) | `IOPHaptics` | `audio-control,audio-iop-haptics` |
| [`/arm-io/iop-audio-controller/audio-hpdbg`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg.md) | `IOPHapticDebug` | `audio-control,audio-iop-haptic-debug` |

## IOKit personalities (2) [KC]

### IOPHapticDebug
- `CFBundleIdentifier`: `com.apple.driver.IOPHaptics`
- `IOClass`: `IOPHapticDebug`
- `IONameMatch`:
  - `audio-control,audio-iop-haptic-debug`
- `IOPersonalityPublisher`: `com.apple.driver.IOPHaptics`
- `IOProviderClass`: `IOPAudioNode`

### IOPHaptics
- `CFBundleIdentifier`: `com.apple.driver.IOPHaptics`
- `IOClass`: `IOPHaptics`
- `IONameMatch`:
  - `audio-control,audio-iop-haptics`
- `IOPersonalityPublisher`: `com.apple.driver.IOPHaptics`
- `IOProviderClass`: `IOPAudioNode`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOPHapticDebug` | 0x238 | IOPEmbeddedAudio → AppleEmbeddedAudio → IOService → IORegistryEntry |
| `IOPHaptics` | 0x278 | IOPEmbeddedAudio → AppleEmbeddedAudio → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000ef5 off=0x0043f470-0x00440365 addr=0xfffffe0007443470-0xfffffe0007444365 r--/r--   __TEXT            
	sz=0x00000117 off=0x0043fb38-0x0043fc4f addr=0xfffffe0007443b38-0xfffffe0007443c4f               __TEXT.__const            
	sz=0x000004d7 off=0x0043fc4f-0x00440126 addr=0xfffffe0007443c4f-0xfffffe0007444126               __TEXT.__cstring          (CstringLiterals)
	sz=0x0000023f off=0x00440126-0x00440365 addr=0xfffffe0007444126-0xfffffe0007444365               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00002828 off=0x01c181e0-0x01c1aa08 addr=0xfffffe0008c1c1e0-0xfffffe0008c1ea08 r-x/r-x   __TEXT_EXEC       
	sz=0x000026b8 off=0x01c181e0-0x01c1a898 addr=0xfffffe0008c1c1e0-0xfffffe0008c1e898          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000170 off=0x01c1a898-0x01c1aa08 addr=0xfffffe0008c1e898-0xfffffe0008c1ea08          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000129 off=0x0493e760-0x0493e889 addr=0xfffffe000b942760-0xfffffe000b942889 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0493e760-0x0493e828 addr=0xfffffe000b942760-0xfffffe000b942828               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b942828-0xfffffe000b942888               __DATA.__common           (Zerofill)
	sz=0x00000001 off=0x00000000-0x00000001 addr=0xfffffe000b942888-0xfffffe000b942889               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001920 off=0x010799f8-0x0107b318 addr=0xfffffe000807d9f8-0xfffffe000807f318 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x010799f8-0x01079a08 addr=0xfffffe000807d9f8-0xfffffe000807da08         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x01079a08-0x01079a18 addr=0xfffffe000807da08-0xfffffe000807da18         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001720 off=0x01079a18-0x0107b138 addr=0xfffffe000807da18-0xfffffe000807f138         __DATA_CONST.__const            
	sz=0x00000100 off=0x0107b138-0x0107b238 addr=0xfffffe000807f138-0xfffffe000807f238         __DATA_CONST.__kalloc_type      
	sz=0x000000b8 off=0x0107b238-0x0107b2f0 addr=0xfffffe000807f238-0xfffffe000807f2f0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000028 off=0x0107b2f0-0x0107b318 addr=0xfffffe000807f2f0-0xfffffe000807f318         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 51 at 0x04ad81ec
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     F2CB4021-D81D-39AD-B282-2D8E986E5EB5
008: LC_SOURCE_VERSION           1010.2.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9eba0 size=0x80
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOPHaptics`
- `CFBundleIdentifier`: `com.apple.driver.IOPHaptics`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOPHaptics`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1010.2`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1010.2`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleEmbeddedAudio.kext/PlugIns/IOPHaptics.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901345168`
- `_PrelinkExecutableRelativePath`: `IOPHaptics`
- `_PrelinkExecutableSize`: `20838`
- `_PrelinkExecutableSourceAddr`: `-2198901345168`
- `_PrelinkKmodInfo`: `-2198828996768`

## Strings (40) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `_setupAudioEnableWarmupDelay`
- `site.IOPHapticDebug`
- `12111112122212121121212111211111111121111111211121112111122112211112211`
- `%s::%s(inSelectors=%p) failed [result: 0x%x]\n`
- `IOPHapticDebug`
- `/Library/Caches/com.apple.xbs/7374CF14-96FD-494A-A9F3-D02707F144CC/TemporaryDirectory.6UQLML/Sources/AppleEmbeddedAudio/src/kext/IOPHaptics/IOPHaptics.cpp`
- `%s::%s() __hallCtrlFunction is null\n`
- `%s::%s() using default parking timeout value of %d ms\n`
- `%s::%s() using default audio enable warm up time %d ms\n`
- `start`
- `%s::Unable to notify Haptics Session %s %d\n`
- `IOPHaptics`
- `site.IOPHaptics`
- `_enableHall`
- `site.AppleEmbeddedAudioRangeInfo`
- `/Library/Caches/com.apple.xbs/7374CF14-96FD-494A-A9F3-D02707F144CC/TemporaryDirectory.6UQLML/Sources/AppleEmbeddedAudio/src/kext/IOPHaptics/IOPHapticDebug.cpp`
- `_setupParkingTimeout`
- `_notifyHapticsSessionStartStop`
- `stop`
- `handleStart`
- `Unable to locate _powerPeakBudgetChangeFunction handler.\n`
- `1211111212221212112121211121111111112111111121112111211112211221111221122211111`
- `%s::%s handleStartFailed\n`
- `%s::%s(%d) hall_ctrl failed [0x%x]\n`
- `%s::%s() Unable to create hall disable timer event source \n`
- `DeviceAttached`
- `preflightMultiControl`
- `Unable to locate __powerThermalBudgetChangeFunction handler.\n`
- `IODeviceTree:/product/audio`
- `SetMultiControl`

**[__TEXT.__os_log]**

- `%s::Unable to notify Haptics Session %s %d`
- `%s::%s handleStartFailed`
- `%s::%s(%d) hall_ctrl failed [0x%x]`
- `%s::%s() using default parking timeout value of %d ms`
- `%s::%s() Unable to create hall disable timer event source `
- `%s::%s() using default audio enable warm up time %d ms`
- `%s::%s(inSelectors=%p) failed [result: 0x%x]`
- `Unable to locate _powerPeakBudgetChangeFunction handler.`
- `Unable to locate __powerThermalBudgetChangeFunction handler.`
- `%s::%s() __hallCtrlFunction is null`
