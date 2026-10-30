# `com.apple.driver.AppleCSEmbeddedAudio`

- Name: AppleCSEmbeddedAudio
- Version: `1010.2`
- UUID: `936BD614-3F33-343D-A86A-C6ECA2DF717B`
- Source version: `1010.2.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0, [`com.apple.driver.AppleEmbeddedAudio`](com.apple.driver.AppleEmbeddedAudio.md) 1.1, [`com.apple.driver.AppleIISController`](com.apple.driver.AppleIISController.md) 1.0.0, [`com.apple.iokit.AppleARMIISAudio`](com.apple.iokit.AppleARMIISAudio.md) 1.0, [`com.apple.iokit.IOAudio2Family`](com.apple.iokit.IOAudio2Family.md) 1.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.5, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (7) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleCSCodecMikey` | 0x190 | AppleMikeyReceiver → AppleEmbeddedButtonController → AppleEmbeddedAudioButtons → IOHIDDevice → IOService → IORegistryEntry |
| `AppleCSDS911CodecMikey` | 0x190 | AppleCSCodecMikey → AppleMikeyReceiver → AppleEmbeddedButtonController → AppleEmbeddedAudioButtons → IOHIDDevice → IOService → IORegistryEntry |
| `AppleCSHTDCodecMikey` | 0x1b0 | AppleCSDS911CodecMikey → AppleCSCodecMikey → AppleMikeyReceiver → AppleEmbeddedButtonController → AppleEmbeddedAudioButtons → IOHIDDevice → IOService → IORegistryEntry |
| `AppleEmbeddedAudioButtons` | 0xf8 | IOHIDDevice → IOService → IORegistryEntry |
| `AppleEmbeddedAudioHeadsetSwitch` | 0x88 | IOService → IORegistryEntry |
| `AppleEmbeddedButtonController` | 0x138 | AppleEmbeddedAudioButtons → IOHIDDevice → IOService → IORegistryEntry |
| `AppleMikeyReceiver` | 0x180 | AppleEmbeddedButtonController → AppleEmbeddedAudioButtons → IOHIDDevice → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000e90 off=0x003bc0d0-0x003bcf60 addr=0xfffffe00073c00d0-0xfffffe00073c0f60 r--/r--   __TEXT            
	sz=0x0000059d off=0x003bc798-0x003bcd35 addr=0xfffffe00073c0798-0xfffffe00073c0d35               __TEXT.__cstring          (CstringLiterals)
	sz=0x000001ea off=0x003bcd35-0x003bcf1f addr=0xfffffe00073c0d35-0xfffffe00073c0f1f               __TEXT.__os_log           
	sz=0x00000040 off=0x003bcf20-0x003bcf60 addr=0xfffffe00073c0f20-0xfffffe00073c0f60               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x0000992c off=0x01a24aa0-0x01a2e3cc addr=0xfffffe0008a28aa0-0xfffffe0008a323cc r-x/r-x   __TEXT_EXEC       
	sz=0x000096cc off=0x01a24aa0-0x01a2e16c addr=0xfffffe0008a28aa0-0xfffffe0008a3216c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000260 off=0x01a2e16c-0x01a2e3cc addr=0xfffffe0008a3216c-0xfffffe0008a323cc          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000378 off=0x049345e8-0x04934960 addr=0xfffffe000b9385e8-0xfffffe000b938960 rw-/rw-   __DATA            
	sz=0x00000188 off=0x049345e8-0x04934770 addr=0xfffffe000b9385e8-0xfffffe000b938770               __DATA.__data             
	sz=0x00000198 off=0x00000000-0x00000198 addr=0xfffffe000b938770-0xfffffe000b938908               __DATA.__common           (Zerofill)
	sz=0x00000058 off=0x00000000-0x00000058 addr=0xfffffe000b938908-0xfffffe000b938960               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00003e78 off=0x01002020-0x01005e98 addr=0xfffffe0008006020-0xfffffe0008009e98 rw-/rw-   __DATA_CONST      
	sz=0x00000028 off=0x01002020-0x01002048 addr=0xfffffe0008006020-0xfffffe0008006048         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000028 off=0x01002048-0x01002070 addr=0xfffffe0008006048-0xfffffe0008006070         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00003a98 off=0x01002070-0x01005b08 addr=0xfffffe0008006070-0xfffffe0008009b08         __DATA_CONST.__const            
	sz=0x000001c0 off=0x01005b08-0x01005cc8 addr=0xfffffe0008009b08-0xfffffe0008009cc8         __DATA_CONST.__kalloc_type      
	sz=0x00000130 off=0x01005cc8-0x01005df8 addr=0xfffffe0008009cc8-0xfffffe0008009df8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000a0 off=0x01005df8-0x01005e98 addr=0xfffffe0008009df8-0xfffffe0008009e98         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 96 at 0x04ad448c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     936BD614-3F33-343D-A86A-C6ECA2DF717B
008: LC_SOURCE_VERSION           1010.2.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9b270 size=0x158
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleCSEmbeddedAudio`
- `CFBundleIdentifier`: `com.apple.driver.AppleCSEmbeddedAudio`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleCSEmbeddedAudio`
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
- `OSBundleCompatibleVersion`: `1.1`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleCSEmbeddedAudio.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901882672`
- `_PrelinkExecutableRelativePath`: `AppleCSEmbeddedAudio`
- `_PrelinkExecutableSize`: `59820`
- `_PrelinkExecutableSourceAddr`: `-2198901882672`
- `_PrelinkKmodInfo`: `-2198829038104`

## Strings (84) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `DetectHistory`
- `sound isolating`
- `short`
- `HIDDefaultBehavior`
- `WaitingForMic`
- `121111121222121211211122211121211221121111121222222112`
- `Audio`
- `Detached`
- `function-headset_switch`
- `HPDetectInvert`
- `site.AppleEmbeddedAudioButtons`
- `MikeyButton is not attached\n`
- `third party`
- `12111112122212121121112221112121122112111112122222`
- `HeadphonesOnly`
- `function-diff_mic_sel`
- `hp-switch-ramp`
- `function-ext_sw1`
- `hs-switch-workaround`
- `site.AppleEmbeddedAudioHeadsetSwitch`
- `hp-detect-invert`
- `site.AppleMikeyReceiver`
- `1211111212221212112111222111212`
- `AppleVendorSupported`
- `Built-In`
- `NoneWillNotify`
- `hp-switch-force-config`
- `AppleCSHTDCodecMikey`
- `CompleteFinal`
- `Mikey`
- `_continueMicDetectGated device is not attached\n`
- `open`
- `timeout`
- `121111121222121211211122211121211221121`
- `mic`
- `Button handleReportWithTime:%x\n`
- `site.AppleEmbeddedButtonController`
- `microphone`
- `121111121222121211211122211121211221121111121222`
- `button`
- `earpiece design`
- `reverse-bias`
- `site.AppleCSDS911CodecMikey`
- `NoneNoNotify`
- `AppleEmbeddedButtonController`
- `HeadphonesWaiting`
- `SingleButton`
- `_disableMicDetectGated device is not attached\n`
- `transmitter tone id`
- `multiple buttons`
- `site.AppleCSHTDCodecMikey`
- `startMicDetected device is not attached\n`
- `AppleCSCodecMikey`
- `hp-pop-workaround`
- `Headset`
- `AppleCSDS911CodecMikey`
- `function-ext_sw2`
- `AppleEmbeddedAudioHeadsetSwitch`
- `AppleEmbeddedAudioButtons`
- `Apple`
- `mic connector reversed`
- `headphone-pop-workaround`
- `mic design`
- `CompleteCanChange`
- `12111112122212121`
- `headset info`
- `AppleMikeyReceiver`
- `MicOpen`
- `site.AppleCSCodecMikey`

**[__TEXT.__os_log]**

- `Button S0 pressed:%d`
- `Headphones detected. Begin mic detection`
- `Detect Complete:%d confidence:%s`
- `startMicDetected device is not attached`
- `_disableMicDetectGated device is not attached`
- `Button set state:%d`
- `Button handleReportWithTime:%x`
- `_continueMicDetectGated device is not attached`
- `Button Volume Down pressed:%d`
- `Button Volume Up pressed:%d`
- `Button terminate release s0`
- `Found mic:%d earpieceDesign:%d micDesign:%d`
- `Power down mikey`
- `MikeyButton is not attached`
- `Mikey headset type detect timeout!\n`
