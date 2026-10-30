# `com.apple.driver.AppleEmbeddedAudio`

- Name: AppleEmbeddedAudio
- Version: `1010.2`
- UUID: `9BD42F4A-B043-3BB8-9953-7171E66AADBF`
- Source version: `1010.2.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0, [`com.apple.driver.AppleEmbeddedAudioLibs`](com.apple.driver.AppleEmbeddedAudioLibs.md) 1.0, [`com.apple.driver.AppleIISController`](com.apple.driver.AppleIISController.md) 1.0.0, [`com.apple.iokit.AppleARMIISAudio`](com.apple.iokit.AppleARMIISAudio.md) 1.0, [`com.apple.iokit.IOAudio2Family`](com.apple.iokit.IOAudio2Family.md) 1.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.5, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (7) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/iop-audio-controller/audio-leap-internal-loopback/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback__audio-leap-internal-loopback.md) | `AppleExternalSecondaryAudio` | `audio-data,external` |
| [`/arm-io/iop-audio-controller/audio-mca-loopback/audio-mca-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-mca-loopback__audio-mca-loopback.md) | `AppleSecondaryAudio` | `audio-data,audio-loopback` |
| [`/arm-io/iop-audio-controller/audio-receiver/audio-receiver`](../devicetree/root__arm-io__iop-audio-controller__audio-receiver__audio-receiver.md) | `AppleExternalSecondaryAudio` | `audio-data,external` |
| [`/arm-io/iop-audio-controller/audio-flicker/audio-flicker`](../devicetree/root__arm-io__iop-audio-controller__audio-flicker__audio-flicker.md) | `AppleExternalSecondaryAudio` | `audio-data,external` |
| [`/arm-io/iop-audio-controller/audio-s-leap-internal-loopback/audio-s-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-s-leap-internal-loopback__audio-s-leap-internal-loopback.md) | `AppleExternalSecondaryAudio` | `audio-data,external` |
| [`/arm-io/iop-audio-controller/lp-mic-injection-device/lp-mic-injection-device`](../devicetree/root__arm-io__iop-audio-controller__lp-mic-injection-device__lp-mic-injection-device.md) | `AppleExternalSecondaryAudio` | `audio-data,external` |
| [`/arm-io/iop-audio-controller/audio-speaker-tap/audio-speaker-tap`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker-tap__audio-speaker-tap.md) | `AppleExternalSecondaryAudio` | `audio-data,external` |

## IOKit personalities (24) [KC]

### AppleAOPMCALoopbackAudio
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IOMatchCategory`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,audio-aop-mca-loopback`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `AOPMCALoopback`
- `device name`: `AOPMCALoopback`

### AppleActuatorAudio
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleActuatorSecondaryAudio`
- `IOMatchCategory`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,actuator`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `Actuator`
- `device name`: `Actuator`

### AppleBasebandAudio
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IOMatchCategory`: `AppleBasebandAudio`
- `IONameMatch`: `audio-data,baseband`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `Baseband`
- `device name`: `Baseband`

### AppleBasebandVoice
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IOMatchCategory`: `AppleBasebandVoiceAudio`
- `IONameMatch`: `audio-data,baseband-voice`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `Baseband Voice`
- `device name`: `Baseband Voice`

### AppleBluetoothVoice
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IOMatchCategory`: `AppleBluetoothVoiceAudio`
- `IONameMatch`: `audio-data,bluetooth-voice`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `Bluetooth Voice`
- `device name`: `Bluetooth Voice`

### AppleCS42L83InputAudio
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IOMatchCategory`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,cs42l83-input`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `Codec Input`
- `device name`: `CS42L83 Input`

### AppleCS42L84InputAudio
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IOMatchCategory`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,cs42l84-input`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `Codec Input`
- `device name`: `CS42L84 Input`

### AppleDSPDebug1
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IOMatchCategory`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,dsp-debug1`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `DSP Debug1`
- `device name`: `DSP Debug1`

### AppleDSPDebug2
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IOMatchCategory`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,dsp-debug2`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `DSP Debug2`
- `device name`: `DSP Debug2`

### AppleExtendedHapticDebug
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IOMatchCategory`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,ext-haptic-debug`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `Extended Haptic Debug`
- `device name`: `Extended Haptic Debug`

### AppleExternalAudio
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleExternalSecondaryAudio`
- `IOMatchCategory`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,external`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProviderClass`: `AppleARMIISDevice`

### AppleHalogen
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IOMatchCategory`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,halogen`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `Halogen`
- `device name`: `Halogen`

### AppleHapticDebug
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IOMatchCategory`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,haptic-debug`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `Haptic Debug`
- `device name`: `Haptic Debug`

### AppleHapticsExternalAudio
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleHapticsExternalSecondaryAudio`
- `IOMatchCategory`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,haptics-external`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProviderClass`: `AppleARMIISDevice`

### AppleHawkingAudio
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IOMatchCategory`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,hawking`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `Hawking`
- `device name`: `Hawking`

### AppleLoopbackAudio
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IOMatchCategory`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,audio-loopback`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `Loopback`
- `device name`: `Loopback`

### AppleMCKAudio
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleMCKAudio`
- `IONameMatch`: `audio-data,mck-only`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProviderClass`: `AppleARMIISDevice`

### AppleMaggieDebugAudio
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IOMatchCategory`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,maggie-debug`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `MaggieDebug`
- `device name`: `MaggieDebug`

### AppleMikeyBusSecondaryAudio
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IOMatchCategory`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,mikeybus-secondary`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `Mikeybus Secondary`
- `device name`: `Mikeybus Secondary`

### AppleReferenceAudio
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IOMatchCategory`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,reference`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `Reference`
- `device name`: `Reference`

### AppleSecondaryAudio
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,secondary`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProviderClass`: `AppleARMIISDevice`

### AppleTapAudio
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IOMatchCategory`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,audio-tap`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `Tap`
- `device name`: `Tap`

### AppleVirtualSecondary
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IOMatchCategory`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,virtual-secondary`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `Virtual Secondary Device`
- `device name`: `Virtual Secondary`

### AppleVoiceAudio
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `IOClass`: `AppleSecondaryAudio`
- `IOMatchCategory`: `AppleSecondaryAudio`
- `IONameMatch`: `audio-data,voice`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudio`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleARMIISDevice`
- `device UID`: `Voice`
- `device name`: `Voice`


## C++ classes (25) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AEARuntimeRegisterPatch` | 0x10 |  |
| `AEARuntimeRegisterPatchForI2C` | 0x20 | AEARuntimeRegisterPatch |
| `AppleActuatorSecondaryAudio` | 0x300 | AppleSecondaryAudio → AppleARMIISAudioDevice → AppleARMDMAAudioDevice → IOAudio2Device → IOService → IORegistryEntry |
| `AppleCSI2CAudio` | 0x1e0 | AppleI2CAudio → AppleEmbeddedAudio → IOService → IORegistryEntry |
| `AppleCSI2CMultipleAudio` | 0x1e0 | AppleI2CMultipleAudio → AppleEmbeddedAudio → IOService → IORegistryEntry |
| `AppleCSSPIAudio` | 0x1d0 | AppleEmbeddedAudio → IOService → IORegistryEntry |
| `AppleCSSPIv2Audio` | 0x340 | AppleCSSPIAudio → AppleEmbeddedAudio → IOService → IORegistryEntry |
| `AppleEmbeddedAudio` | 0x1c0 | IOService → IORegistryEntry |
| `AppleEmbeddedAudioDevice` | 0x308 | AppleARMIISAudioDevice → AppleARMDMAAudioDevice → IOAudio2Device → IOService → IORegistryEntry |
| `AppleEmbeddedAudioGroup` | 0x28 | OSArray → OSCollection |
| `AppleEmbeddedExternalAudioObject` | 0xa0 | IOService → IORegistryEntry |
| `AppleExternalSecondaryAudio` | 0x318 | AppleSecondaryAudio → AppleARMIISAudioDevice → AppleARMDMAAudioDevice → IOAudio2Device → IOService → IORegistryEntry |
| `AppleHapticsExternalSecondaryAudio` | 0x338 | AppleExternalSecondaryAudio → AppleSecondaryAudio → AppleARMIISAudioDevice → AppleARMDMAAudioDevice → IOAudio2Device → IOService → IORegistryEntry |
| `AppleI2CAudio` | 0x1e0 | AppleEmbeddedAudio → IOService → IORegistryEntry |
| `AppleI2CMultipleAudio` | 0x1e0 | AppleEmbeddedAudio → IOService → IORegistryEntry |
| `AppleI2CPagedAudio` | 0x1e8 | AppleI2CAudio → AppleEmbeddedAudio → IOService → IORegistryEntry |
| `AppleI2CRangedAudio` | 0x1f0 | AppleI2CAudio → AppleEmbeddedAudio → IOService → IORegistryEntry |
| `AppleI2CRangedMultipleAudio` | 0x1f8 | AppleI2CMultipleAudio → AppleEmbeddedAudio → IOService → IORegistryEntry |
| `AppleMAXI2CAudio` | 0x1e0 | AppleI2CAudio → AppleEmbeddedAudio → IOService → IORegistryEntry |
| `AppleMCKAudio` | 0x98 | IOService → IORegistryEntry |
| `AppleMCKAudioFunction` | 0x38 | AppleARMFunction |
| `AppleSecondaryAudio` | 0x300 | AppleARMIISAudioDevice → AppleARMDMAAudioDevice → IOAudio2Device → IOService → IORegistryEntry |
| `AppleSecondaryAudioFunction` | 0x50 | AppleARMFunction |
| `AppleTII2CAudio` | 0x1e0 | AppleI2CMultipleAudio → AppleEmbeddedAudio → IOService → IORegistryEntry |
| `iBootAudioVolumeManager` | 0x18 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00007f24 off=0x0042ef70-0x00436e94 addr=0xfffffe0007432f70-0xfffffe000743ae94 r--/r--   __TEXT            
	sz=0x000044f8 off=0x0042f638-0x00433b30 addr=0xfffffe0007433638-0xfffffe0007437b30               __TEXT.__cstring          (CstringLiterals)
	sz=0x000000b0 off=0x00433b30-0x00433be0 addr=0xfffffe0007437b30-0xfffffe0007437be0               __TEXT.__const            
	sz=0x000032b4 off=0x00433be0-0x00436e94 addr=0xfffffe0007437be0-0xfffffe000743ae94               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00033de0 off=0x01bcb5c0-0x01bff3a0 addr=0xfffffe0008bcf5c0-0xfffffe0008c033a0 r-x/r-x   __TEXT_EXEC       
	sz=0x000333d0 off=0x01bcb5c0-0x01bfe990 addr=0xfffffe0008bcf5c0-0xfffffe0008c02990          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000a10 off=0x01bfe990-0x01bff3a0 addr=0xfffffe0008c02990-0xfffffe0008c033a0          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000760 off=0x0493da38-0x0493e198 addr=0xfffffe000b941a38-0xfffffe000b942198 rw-/rw-   __DATA            
	sz=0x00000308 off=0x0493da38-0x0493dd40 addr=0xfffffe000b941a38-0xfffffe000b941d40               __DATA.__data             
	sz=0x00000458 off=0x00000000-0x00000458 addr=0xfffffe000b941d40-0xfffffe000b942198               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x0000e968 off=0x010656d0-0x01074038 addr=0xfffffe00080696d0-0xfffffe0008078038 rw-/rw-   __DATA_CONST      
	sz=0x00000078 off=0x010656d0-0x01065748 addr=0xfffffe00080696d0-0xfffffe0008069748         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000078 off=0x01065748-0x010657c0 addr=0xfffffe0008069748-0xfffffe00080697c0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x0000d0d0 off=0x010657c0-0x01072890 addr=0xfffffe00080697c0-0xfffffe0008076890         __DATA_CONST.__const            
	sz=0x00000740 off=0x01072890-0x01072fd0 addr=0xfffffe0008076890-0xfffffe0008076fd0         __DATA_CONST.__kalloc_type      
	sz=0x00000a50 off=0x01072fd0-0x01073a20 addr=0xfffffe0008076fd0-0xfffffe0008077a20         __DATA_CONST.__kalloc_var       
	sz=0x00000508 off=0x01073a20-0x01073f28 addr=0xfffffe0008077a20-0xfffffe0008077f28         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000110 off=0x01073f28-0x01074038 addr=0xfffffe0008077f28-0xfffffe0008078038         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 356 at 0x04ad7834
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     9BD42F4A-B043-3BB8-9953-7171E66AADBF
008: LC_SOURCE_VERSION           1010.2.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9e218 size=0x5f0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleEmbeddedAudio`
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudio`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleEmbeddedAudio`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleEmbeddedAudio.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901411984`
- `_PrelinkExecutableRelativePath`: `AppleEmbeddedAudio`
- `_PrelinkExecutableSize`: `306636`
- `_PrelinkExecutableSourceAddr`: `-2198901411984`
- `_PrelinkKmodInfo`: `-2198829000136`

## Strings (720) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `master_index`
- `%s: Failed to disable injection on client close.\n`
- `dependency-name_%s`
- `%s %s:%d instance = NULL. AppleCSSPIAudio::probe() Failed\n`
- `device-name`
- `AppleEmbeddedAudio::%s HW failure detected\n`
- `matchingNotificationHandlerGated`
- `stopIOEngineWithFlags`
- `%s::%s(deviceIndex=%d, _addressByteCount=%d, startAddress=0x%x, bufferSize=%llu) I2C register write failed : %s\n`
- `aea-power-provider`
- `Speaker N voltage`
- `MikeyBus channel N`
- `registerWithPrimary`
- `site.AppleHapticsExternalSecondaryAudio`
- `%s::%s Unable to locate _powerPeakBudgetChangeFunction handler.\n`
- `_writeMultipleWord`
- `%s::%s unable to retrieve kIOAudio2DeviceKey_ControlList property\n`
- `enableAudioInput`
- `IODeviceTree:/product/audio`
- `earpiece design`
- `_setAudioEnabledGated`
- `%s::%s(..) failed.\n`
- `updatePropertyControls`
- `button`
- `setDeviceSampleRate`
- `%s %s::%s invalid gain size for Trim Gain V1\n`
- `CodecExtendedRegisterData`
- `default-input-data-sources`
- `codec-calibration`
- `Codec`
- `_powerStateWillChangeToGated`
- `%s %s::%s could not get read the header\n`
- `CodecUID`
- `AppleEmbeddedAudioGroup`
- `enableAudioOutput`
- `%s: I2C _writeReg page write failed (%#x): %s\n\n`
- `\"%s\" @%s:%d`
- `\"%s::%s should not be called without owning workloop\" @%s:%d`
- `%s %s:%d _readDataBlock cannot transfer SPI polls. ret=0x%x\n`
- `%s::%s unexpected error. _hapticsSessionStartEndFunction is NULL\n`
- `function-clock_src_baseband`
- `%s AppleCSSPIAudio::%s:%d _spiNub = %p. Ping() Failed\n`
- `%s AppleCSSPIv2Audio::%s:%d Write. Status was not OK address = 0x%x \n`
- `Output reference left`
- `%s::%s(..) super::stopTransportComplete(..) failed\n`
- `:%sFailed to create AppleBridgeAudio\n\n`
- `multiple buttons`
- `headset info`
- `%s::%s:%d failed. requested sampleRate=%lld\n`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `MicDetect`
- `acoustic-trim-gains`
- `AppleMCKAudioFunction::%s enable parameter (param1) cannot be a null pointer\n`
- `%s %s:%d _writeDataBlock cannot transfer SPI data. ret=0x%x\n`
- `LowPowerEnableChannelMask`
- `data-sources`
- `Version`
- `site.const DataSourceConfig*`
- `default-output-data-sources`
- `site.AppleSecondaryAudioFunction`
- `function-input_power_enable`
- `registry key`
- `%s inConfigData cannot be nullptr\n`
- `kAppleEmbeddedAudioDependencyMatchingProperties`
- `mic-trim-gains`
- `Internal microphone`
- `Output reference right`
- `aea_debug`
- `Ping`
- `IOReportLegendPublic`
- `site.AppleMCKAudio`
- `externalSampleRateChangeGated`
- `\"%s::%s [%u] unable to allocate array of pointers (array size = %u)\\n\" @%s:%d`
- `%s AppleCSSPIv2Audio::%s:%d Codec: SPI not ready AF2AF2AF2AF2AF2AF2AF2AF2\n`
- `1211111212221212121222211122112212221112211111111111111221111112221111211121211111121121121111121111112`
- `AppleI2CPagedAudio`
- `external-power-provider`
- `%s::%s enableAudioOutput failed. direction=0x%x enabled=%d ret=%s(0x%x)\n`
- `%s::%s:%d setAudioStreamFormats failed with %s\n\n`
- `Speaker N PDM Mon`
- `%s::%s _externalPowerManager=%p failed to addPowerProvider (%s)\n`
- `Unable to get simple IO reporter information from the driver\n`
- `mic connector reversed`
- `\"%s::%s[%u] unable to allocate IOTimerEventSource for iBootVolume.\" @%s:%d`
- `%s %s:%d _readDataBlock cannot de assert CS. ret=0x%x\n`
- `%s %s::%s cannot handle Gain Trim ver%d syscfg\n`
- `%s %s:%d cannot set auto increment. ret=0x%x\n`
- `%s::%s(inDeviceIndex=%u, inAddress=0x%x, inMask=0x%x, inData=0x%x) failed to get write only mask [errorCode:0x%x]\n`
- `_readControlReg`
- `AppleEmbeddedExternalAudioObject`
- `site.AppleEmbeddedAudio`
- `site.IONotifier *`
- `virtual IOReturn AEARuntimeRegisterPatchForI2C::addRegisterPatch(const RegisterPatch &)`
- `AppleMCKAudioFunction::%s setUpClock failed -> ret = %#x\n`
- `site.AppleCSI2CAudio`
- `AppleHapticsExternalSecondaryAudio::start(..) failed.\n\n\n`
- `121111121222121211212121112111111111211111112111211121111222212`
- `iBootAudioVolumeManager`
- `controls`
- `%s %s::%s invalid header 0x%x for %s\n`
- `site.AppleCSSPIAudio`
- `DelayBeforeRequestConfigChangeMS`
- `MiGa`
- `AppleCSSPIAudio`
- `1211111212221212121222211122112212221112211111111111111221111112221111211121111111111122111222211`
- `TestcaseRunTimeMS`
- `Landscape`
- `applySetControlValue`
- `AppleEmbeddedAudio.cpp`
- `Speaker`
- `mikey`
- `%s AppleCSSPIv2Audio::%s:%d encountered failure. address=0x%x keepCSAsserted=%d result=0x%x\n`
- `SpeakerCalibrationDesc`
- `HSSwitchDetect`
- `enableAudioHW failed\n`
- `MaxNumberFilters`
- `IOReportLegend`
- `calibration-MiGa`
- `Internal error microphone`
- `Voice`
- `%s: Error parsing clock-sources; offset %u\n`
- `site.AppleI2CMultipleAudio`
- `_writeMultiple`
- `tdm-host`
- `_setPowerStage`
- `sysclk-48000`
- `%d`
- `mic design`
- `%s::%s enableAudioInput failed. direction=0x%x enabled=%d ret=%s(0x%x)\n`
- `CodecRegisterStartIndex`
- `%s::%s(deviceIndex=%d, address=0x%x) I2C register read failed: '%s' (%d)\n\n`
- `%s AppleCSSPIv2Audio::%s:%d Read. Status after data was not OK 0x%x \n`
- `input streams`
- `Speaker N keepalive`
- `site.AppleEmbeddedAudioGroup`
- `applyMultiControlValue`
- `%s:%s IOAudio2ControlDictionary::createSliderControl returned nullptr\n`
- `%s: I2C register read failed (%#x): %s\n\n`
- `%s%u`
- `static-volume`
- `_readMultipleWord`
- `Speaker N power supply voltage`
- `%s: Memory allocation error.\n`
- `dependency-timeout-us_%s`
- `updateDebuggingControls`
- `AppleExternalSecondaryAudio`
- `outputArrayCal`
- `%s::%s(inDeviceIndex=%u, inAddress=0x%x) encountered error reading register [errorCode:0x%x]\n`
- `kAppleEmbeddedAudioDependencyMatchingTimeoutInNS`
- `function-default-gpio`
- `%s::%s failed to validate operation (%u, %p, %p)\n`
- `_read32Reg`
- `DetectInfoFinal`
- `SPIv2 Unsupported command:%x\n\n`
- `on`
- `site.OSArray*`
- `terminal-type-input`
- `DeviceAttached`
- `%s failed to write onto NVRAM result=%#x\n`
- `virtual bool AppleEmbeddedAudio::start(IOService *)`
- `\"%s: invalid power stage %d\" @%s:%d`
- `Baseband`
- `%s AppleCSSPIv2Audio::%s:%d Codec: Bus Write not ready AF1AF1AF1AF1AF1AF1AF1AF1\n`
- `%s::%s(controlID = %u) controlBaseClassID = %u, copySelectorControlSelectorMap returns NULL \n`
- `121111121222121212122221112211221222111221111111111111122111111222111121112121111112112112111112111`
- `AppleHapticsExternalSecondaryAudio::start(..) super::start(..) failed\n\n`
- `%s: I2C _writeReg page write failed (%#x, %#x): %s\n\n`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `i8@?0`
- `readTrimGainV1`
- `startIOEngine`
- `%s::%s(extended=%d) _readMultiple(startRegister=%u,..., numberOfRegisters=%u) failed [errorCode : 0x%x]\n`
- `/options`
- `ANC playback monitor`
- `device-uid`
- `site.DataSourceConfig.IOAudio2Fixed64`
- `SpGa`
- `SimulateNoAudioDC`
- `DoNotReturnAfterRequestConfigChange`
- `%s::%s(inControlID = %d) getControlByID returns NULL\n`
- `%s::%s: Failed to disable GPIO [result: 0x%x]\n`
- `preflightMultiControlValue`
- `AppleCSSPIv2Audio`
- `site.AppleEmbeddedAudioDevice`
- `%s::%s:%d Failed to enable prewarm. result=%s(0x%x)\n`
- `NumSpkCalibs`
- `MaxOutputChannelCount`
- `ANC monitor`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `%s: does not support per device register patch\n`
- `on-demand`
- `%s:%s failed for %d. theAnswer=%s(0x%x)\n`
- `%s::%s(extended=%d) unable to allocate OSData (capacity = %u)\n`
- `site.AppleEmbeddedExternalAudioObject`
- `System`
- `%s::%s HPDetectKey: BadArgument\n`
- `AppleCSI2CMultipleAudio`
- `off`
- `tdm-guest%u`
- `%s::%s [%u] unable to get phandle at index=%d [NumPhandles=%d]\n`
- `BytesPerSpkCalib`
- `site.const DataDestinationConfig*`
- `%s:%s create injection control failed\n`
- `%s::%s(%d) failed\n`
- `Audio Output Traffic`
- `CodecRegisterPatch`
- `find-speaker-id`
- `usePrimaryWorkloop`
- `_changePowerState`
- `%s: could not allocate control %u\n`
- `%s: SPI register write failed (%#x:%llu): %s\n\n`
- `Portrait`
- `%s::%s(..) super::startAudio(..) failed\n`
- `%s::%s() unexpected error : MCLK is left enabled.\n`
- `%s::%s:%d Aborting power-down sequence _powerStage=%d\n`
- `AEARuntimeRegisterPatch`
- `_notifyHapticsSessionStartStop`
- `AppleMCKAudio`
- `_publishSpeakerId`
- `site.OSString *`
- `%s::Not enough memory\n`
- `function-%s_primary`
- `DelayInPerformConfigChange`
- `function-data_source_route_XXXX`
- `output-data-source-selectors`
- `site.AppleActuatorSecondaryAudio`
- `%s:%s ioControlList is is nullptr\n`
- `121111121222121212122221112211221222111221111111111111122111111222111121112121111112112112111112`
- `site.IONotifier*`
- `SpeakerCalibrationData`
- `%s I2C failed to read:%x err:%d\n\n`
- `_startStopIOEngineWithFlagsGated`
- `output-data-selectors`
- `site.AppleExternalSecondaryAudio`
- `ButtonDetect`
- `Forcing %s to be disabled\n`
- `dependency-flag_%s`
- `%s AppleCSSPIv2Audio::%s:%d Invalid Register Address = 0x%x \n`
- `21111`
- `AppleMAXI2CAudio`
- `%s: I2C _readMultiple page write failed (%#x): %s\n\n`
- `AppleI2CRangedMultipleAudio`
- `kIOMessageSystemWillNotSleep`
- `at-scale-xxxx`
- `%s AppleCSSPIv2Audio::%s:%d encountered failure. address=0x%x data=0x%x keepCSAsserted=%d result=0x%x\n`
- `%s::%s(..) unable to create OSNumber. [selectorIndex=%d]\n`
- `stopIOEngine`
- `%s::%s(..) super::start(..) failed\n`
- `%s %s::%s:%d _resetFunction failed ret=0x%x\n`
- `_initializeCodecRegisters`
- `TestcaseNumber`
- `is prewarmed`
- `stopTransportComplete`
- `%s AppleCSSPIv2Audio::%s:%d Read. Status was not OK address = 0x%x \n`
- `MikeyBus channel 1N`
- `AppleSecondaryAudioFunction`
- `kIOMessageSystemWillRestart`
- `site.AEARuntimeRegisterPatch`
- `_writeRegNoIncrement`
- `canSetDataSourceSelector`
- `site.OSObject *`
- `%s: I2C register write failed (%#x, %#x): %s\n\n`
- `%s::%s [%u] unable to create matching property index=%d [NumPhandles=%d]\n`
- `%s::%s OSArray allocation failed\n`
- `setControlValue`
- `default-input-data-selectors`
- `Power State`
- `TestcaseTimeoutMS`
- `Voice left`
- `%s: Error parsing data-destinations.\n`
- `sysclk-44100`
- `Output reference (mono)`
- `AppleSecondaryAudio`
- `site.const ClockSourceConfig*`
- `%s: I2C register page write failed (%#x, %#x): %s\n\n`
- `12`
- `current state`
- `%s: Missing data-sources or data-sources-config property.\n`
- `%s: Unsupported data-source-config version: %hhu\n`
- `skip-ext-power-dep-on-iis-nub`
- `%s: SPI register read failed (%#x): %s\n\n`
- `getStreamFormatSupportedSampleRate`
- `function-input-data-selectors`
- `_maskWrite32Reg`
- `third party`
- `%s AppleCSSPIv2Audio::%s:%d DMA DEBUG Register #3. %x-%x-%x-%x-%x-%x-%x-%x-%x-%x\n`
- `registerPrimaryFunctionGated`
- `calibration-WFEQ`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `%s %s:%d _spiNub = NULL. AppleCSSPIAudio::probe() Failed\n`
- `data-sources-config`
- `IOReturn iBootAudioVolumeManager::writeNVRAMVariable(uint16_t)`
- `dependency-flag`
- `Hawking Channel 2`
- `%s::%s(controlID = %u) failed [errorCode : 0x%x]\n`
- `%s::%s(inDeviceIndex=%u, inAddress=0x%x, inMask=0x%x, inData=0x%x) encountered error writing register (dataToWrite=0x%x) [errorCode:0x%x]\n`
- `%s: I2C _transferData to %s failed (Address : 0x%x): %s\n`
- `site.AppleI2CPagedAudio`
- `_setMultiControlValueGated`
- `input-data-selectors`
- `iboot-audio-volume`
- `%s AppleCSSPIv2Audio::%s:%d failed. address=0x%x wordTransfer=%d result=0x%x\n`
- `is private`
- `startAudio`
- `SampleRate`
- `%s: updateTimestamp not ready yet.\n\n`
- `TCal`
- `\"%s: unknown base class %#x for control ID %u\" @%s:%d`
- `1211112111`
- `site.AppleI2CRangedAudio`
- `Sidetone`
- `AppleActuatorSecondaryAudio`
- `site.OSString*`
- `AppleCSI2CAudio`
- `Speaker N current`
- `terminal-type-output`
- `%s::%s:%d canPrimaryFunctionEnableAudio failed. result=%#x\n`
- `calibration-SpEQ`
- `%s::%s(deviceIndex=%d, address=0x%x) I2C register read from failed : %s\n`
- `AEARuntimeRegisterPatchForI2C`
- `DelayAfterRequestConfigChangeMS`
- `site.OSObject*`
- `function-reset2`
- `site.void *`
- `dependency-timeout-us`
- `1211111`
- `site.AppleSecondaryAudio`
- `clock-domain`
- `getDeviceTreeAudioNodeProperty`
- `SimulateAudioHwError`
- `%s AppleCSSPIv2Audio::%s:%d DMA DEBUG Register #2. %x-%x-%x-%x-%x-%x-%x-%x-%x-%x\n`
- `spkr-prot-latency-override`
- `%s failed to initialize an AppleExternalPowerManager object\n`
- `DetectConfidence`
- `dependency-name`
- `_enableControlI2C`
- `SpEQ`
- `default-gpio-post-delay-ms`
- `AppleBridgeAudio`
- `clock-frequency`
- `1212`
- `speaker-protection`
- `site.AppleSpeakerCalibration`
- `AppleAudioDeviceTreeHelper::%s could not find property for \"%s\"\n`
- `Speaker N boost voltage`
- `input-data-source-selectors`
- `%s: I2C _writeMultiple page write failed (%#x): %s\n\n`
- `Audio Input Traffic`
- `%s %s:%d _writeDataBlock cannot de assert CS. ret=0x%x\n`
- `output streams`
- `function-data_dest_route_XXXX`
- `samplerate-subset`
- `Internal secondary microphone`
- `%s::%s:%d kIOReturnNotReady\n`
- `startStopIOEngineWithFlags`
- `_maskWrite32RegAll`
- `CodecRegisterData`
- `%s::%s:%d failed. sampleRate=%lld ret=%s(0x%x)\n`
- `setDataSourceSelector`
- `site.AppleI2CAudio`
- `DetectTime`
- `%s: I2C register write failed (%#x:%llu): %s\n\n`
- `%s::%s(deviceIndex=%d, _addressByteCount=%d, startAddress=0x%x, bufferSize=%llu) I2C register read from failed : %s\n`
- `1211111212221212112121211121111111112111111121112111211112221`
- `12111112122212121121212111211111111121111111211121112111`
- `AppleMCKAudioFunction::%s could not get data\n`
- `supports prewarming`
- `%s::%s:%d Failed to turn %s. result=%s(0x%x)\n`
- `Speaker N audio`
- `AppleEmbeddedAudio`
- `debugWriteRegister`
- `MinCoefficientValue`
- `%s %s:%d _writeDataBlock cannot transfer SPI header. ret=0x%x\n`
- `MaxInputChannelCount`
- `Voice right`
- `startIOEngineWithFlags`
- `12111112122212121121212111211111111121111111211121112111122212`
- `site.AppleTII2CAudio`
- `%s: SPI register write failed (%#x, %#x): %s\n\n`
- `%s AppleCSSPIv2Audio::%s:%d encountered failure. address=0x%x data=0x%x result=0x%x\n`
- `Reference`
- `CodecRegisterPatchList`
- `%s::%s(extended=%d) _registerCount = %u, _startRegister= %u yields zero register\n`
- `%s::%s(inDeviceIndex=%u, inAddress=0x%x, inMask=0x%x, inData=0x%x) encountered error reading register [errorCode:0x%x]\n`
- `_powerNotificationGated`
- `function-%s_active`
- `%s::%s(provider=%s) failed -> ret = %#x\n`
- `External microphone`
- `Internal microphone  `
- `property selector`
- `CCal`
- `value`
- `%s (Requested device : %s) unable to to find dependent service (timeout = %llu ns)\n`
- `site.AppleEmbeddedAudioRangeInfo`
- `121111121222121211212121112111111111211111112111211121111222`
- `LowPowerActiveChannelMask`
- `speakerID`
- `AppleI2CRangedAudio`
- `SystemAudioVolumeExtension`
- `function-clock_src_route_XXXX`
- `%s::%s(inAddress=%u, inMask=0x%x, inData=0x%x, writeVerify=%d) _maskWrite32Reg(deviceIndex=%u,...) failed [errorCode:0x%x]\n`
- `\"minimum value cannot be greater than maximum\" @%s:%d`
- `callFunction`
- `%s AppleCSSPIv2Audio::%s:%d DMA DEBUG Register #1. %x-%x-%x-%x-%x-%x-%x-%x-%x-%x\n`
- `%u`
- `Speaker N flags`
- `CodecRegisterDisplayBase`
- `performConfigChange`
- `Bottom Speaker`
- `transmitter tone id`
- `%s::%s() failed [errorCode: 0x%x]\n`
- `OSBoundedPtr.h`
- `%s AppleCSSPIv2Audio::%s:%d Write. Status after data transfer was not OK 0x%x \n`
- `%s::%s:%d inValue(%d) is outside of the range [%u - %u]\n\n`
- `<unknown name>`
- `12228`
- `%s::Read Data address 0x%x:: 0x%x !=0x%x\n`
- `%s::%s unable to update DependencyRequirement due to missing deviceName\n\n`
- `BridgeAudio`
- `setProperties`
- `%s: SPI register read failed (%#x:%llu): %s\n\n`
- `%s %s:%d _readDataBlock cannot transfer SPI data. ret=0x%x\n`
- `data-destinations`
- `enableHWPreWarm`
- `AppleHapticsExternalSecondaryAudio`
- `%s::%s(inDeviceIndex=%u, inAddress=0x%x, inMask=0x%x, inData=0x%x, writeVerify=%d) dataRead (0x%x) != dataWritten(0x%x) [errorCode:0x%x]\n`
- `1`
- `actuator-calibration`
- `kIOMessageSystemWillPowerOff`
- `%s::%s OSDictionary allocation failed\n`
- `microphone`
- `%s::%s failed. inControlID=%d inValue=%d ret=%s(0x%x)\n`
- `site.AppleARMFunctionIISRoute*`
- `default-output-data-selectors`
- `%s::%s(inDirection=0x%x, inSelectors=%p) selectors cannot be nullptr\n`
- `site.AppleI2CRangedMultipleAudio`
- `Reset`
- `samplerate-default`
- `getTrimGain`
- `setInputMCLKEnabled`
- `%s::%s(enabled=%d) failed [errorCode: 0x%x]\n`
- `site.AppleMAXI2CAudio`
- `%s::%s:%d failed result=%s(0x%x)\n`
- `inputArrayCal`
- `AppleTII2CAudio`
- `_enableControlI2C currentControlReg =  0x%x \n`
- `clock-sources`
- `WFEQ`
- `kAppleEmbeddedAudioDependencyMatchingFlag`
- `%s %s::%s:%d _resetFunction2 failed ret=0x%x\n`
- `_fakeNotifyHPDetect`
- `Internal lower microphone`
- `Top Speaker`
- `function-speaker-id%d`
- `speaker-calib`
- `_readMultiple`
- `probe`
- `1211111212221212112`
- `updateControlListProperty`
- `%s::%s(inControlID=0x%x, ...) not allowed [result: 0x%x]\n`
- `spkr`
- `site.AppleCSSPIv2Audio`
- `%s %s:%d _readDataBlock cannot transfer SPI header. ret=0x%x\n`
- `Hawking Channel 1`
- `%s: Error processing property '%s'.\n`
- `%s::%s(controlID = %u) unsupported controlBaseClassID = %u encountered\n`
- `input-data-source-read-only`
- `%s::%s [%u] unable to allocate AppleExternalPowerManager\n`
- `%s: getSupportedSampleRates returned nullptr\n`
- `Kessel N Data`
- `site.iBootAudioVolumeManager`
- `Unable to locate nvram service\n`
- `12111112122212121111`
- `function-reset`
- `data exchange blocks`
- `%s failed to allocate an AppleExternalPowerManager object\n`
- `No support for disappearing controls at the moment\n`
- `MaxCoefficientValue`
- `AppleMCKAudioFunction`
- `site.AppleCSI2CMultipleAudio`
- `12111112122212121121212111211111111121111111211121112111112122222222222222222222222222222222222222222222`
- `_setControlValueGated`
- `AppleI2CMultipleAudio`
- `HPDetect`
- `BeginTestcaseWithRunCount`
- `validateOperation`
- `initWithTargetDataAndSymbol`
- `_enableControlPLL`
- `_readDataBlock`
- `AppleEmbeddedAudioDevice`
- `start`
- `1211111212221212112121211121111111112111111121112111211111`
- `%s %s:%d _writeDataBlock cannot transfer SPI polls. ret=0x%x\n`
- `DebuggingInfo`
- `Disabled`
- `AudioHardwareError`
- `function-clock_src_system`
- `sound isolating`
- `_writeControlReg`
- `%s::%s:%d Failed to enable prewarm. ret=%s(0x%x)\n`
- `function-output-data-selectors`
- `AppleMCKAudioFunction::%s could not get target instance\n`
- `122`
- `private_audio_devices`
- `%s AppleCSSPIv2Audio::%s:%d encountered failure. startAddress=0x%x size=%llu result=0x%x\n`
- `maxChannelCount`
- `ANC monitor 2`
- `calibration-SpGa`
- `\"%s::%s[%u] unable to allocate IOTimerEventSource for powerChange.\" @%s:%d`
- `function-%s_master`
- `site.AppleMCKAudioFunction`
- `AppleMCKAudioFunction::%s super::initWithTargetDataAndSymbol failed\n`
- `_readRegNoIncrement`
- `SpkrProtLatencyOverride`
- `State`
- `debugCopyRegisters`
- `device UID`
- `kIOMessageSystemHasPoweredOn`
- `_writeDataBlock`
- `Line in right`
- `%s: I2C register read failed (%#x:%llu): %s\n\n`
- `private`
- `site.AEARuntimeRegisterPatchForI2C`
- `custom property info`
- `enableAudioHW failed but continuing on...\n`
- `%s::%s:%d failed inFlags=0x%x result=%s(0x%x)\n`
- `ignoreDataSourceCount`
- `%s::%s: Failed to enable GPIO [result: 0x%x]\n`
- `AppleI2CAudio`
- `_waitPowerState`
- `valid-speaker-ids`
- `Line in left`
- `_readReg`
- `AppleARMIISDevice`
- `%s::%s failed to start\n`
- `actCal`
- `%s::%s encountered error with _hapticsSessionStartEndFunction->callFunction(%u) [errorCode : 0x%x]\n`
- `static iBootAudioVolumeManager *iBootAudioVolumeManager::withTargetSpecificConfig(const OSData *)`
- `device name`
- `_writeReg`
- `streaming audio`

**[__TEXT.__os_log]**

- `%s %s:%d _readDataBlock cannot de assert CS. ret=0x%x`
- `%s::%s(inAddress=%u, inMask=0x%x, inData=0x%x, writeVerify=%d) _maskWrite32Reg(deviceIndex=%u,...) failed [errorCode:0x%x]`
- `%s::%s unable to update DependencyRequirement due to missing deviceName\n`
- `%s::%s failed to start`
- `%s: does not support per device register patch`
- `AppleMCKAudioFunction::%s could not get data`
- `%s %s:%d _spiNub = NULL. AppleCSSPIAudio::probe() Failed`
- `%s AppleCSSPIv2Audio::%s:%d encountered failure. address=0x%x keepCSAsserted=%d result=0x%x`
- `%s %s:%d _writeDataBlock cannot transfer SPI data. ret=0x%x`
- `%s::%s(deviceIndex=%d, _addressByteCount=%d, startAddress=0x%x, bufferSize=%llu) I2C register read from failed : %s`
- `%s::%s encountered error with _hapticsSessionStartEndFunction->callFunction(%u) [errorCode : 0x%x]`
- `%s: I2C register write failed (%#x:%llu): %s\n`
- `%s %s::%s could not get read the header`
- `%s %s::%s invalid header 0x%x for %s`
- `AppleMCKAudioFunction::%s super::initWithTargetDataAndSymbol failed`
- `%s %s:%d _readDataBlock cannot transfer SPI polls. ret=0x%x`
- `%s::%s:%d failed result=%s(0x%x)`
- `%s::%s(extended=%d) _registerCount = %u, _startRegister= %u yields zero register`
- `%s::%s(inDeviceIndex=%u, inAddress=0x%x) encountered error reading register [errorCode:0x%x]`
- `%s::%s:%d - %s (%#x)`
- `%s: default sample rate is not supported`
- `%s AppleCSSPIv2Audio::%s:%d DMA DEBUG Register #2. %x-%x-%x-%x-%x-%x-%x-%x-%x-%x`
- `%s AppleCSSPIv2Audio::%s:%d encountered failure. startAddress=0x%x size=%llu result=0x%x`
- `%s::%s enableAudioOutput failed. direction=0x%x enabled=%d ret=%s(0x%x)`
- `%s::%s(..) unable to create OSNumber. [selectorIndex=%d]`
- `%s::%s(deviceIndex=%d, _addressByteCount=%d, startAddress=0x%x, bufferSize=%llu) I2C register write failed : %s`
- `%s:%s Forcing transition to the lowest power state (deferral = %x us)\n`
- `%s::%s OSArray allocation failed`
- `%s::%s() failed [errorCode: 0x%x]`
- `%s::%s enableAudioInput failed. direction=0x%x enabled=%d ret=%s(0x%x)`
- `%s::%s:%d failed inFlags=0x%x result=%s(0x%x)`
- `%s::%s(..) super::stopTransportComplete(..) failed`
- `%s::%s(inDirection=0x%x, inSelectors=%p) selectors cannot be nullptr`
- `%s::%s:%d _powerStage=%d`
- `%s::%s:%d inValue(%d) is outside of the range [%u - %u]\n`
- `%s::%s unable to retrieve kIOAudio2DeviceKey_ControlList property`
- `%s::%s(controlID = %u) failed [errorCode : 0x%x]`
- `%s::%s(..) super::startAudio(..) failed`
- `%s::%s(inControlID=0x%x, ...)[line:%d] failed [result: 0x%x]`
- `%s::%s(inDirection=0x%x, inSelectors=%p) failed [result: 0x%x]`
- `%s::%s unexpected error. _hapticsSessionStartEndFunction is NULL`
- `%s::%s(extended=%d) unable to allocate OSData (capacity = %u)`
- `%s: Disabled input stream injection on client close.`
- `%s::%s(enabled=%d) failed [errorCode: 0x%x]`
- `%s::%s:%d Valid SpeakerIDs: numIds:%d`
- `%s: Memory allocation error.`
- `%s::stopIOEngineWithFlags() inFlags=0x%x`
- `%s::%s(..) super::start(..) failed`
- `AppleAudioDeviceTreeHelper::%s could not find property for \"%s\"`
- `%s::%s() unexpected error : MCLK is left enabled.`
- `AppleMCKAudioFunction::%s enable parameter (param1) cannot be a null pointer`
- `%s AppleCSSPIv2Audio::%s:%d encountered failure. address=0x%x data=0x%x keepCSAsserted=%d result=0x%x`
- `%s::%s(inControlID=0x%x, ...)[line:%d] super::%s(..) failed [result: 0x%x]`
- `%s::%s:%d - kIOMessageCanSystemSleep (%#x)`
- `%s AppleCSSPIv2Audio::%s:%d encountered failure. address=0x%x data=0x%x result=0x%x`
- `%s AppleCSSPIv2Audio::%s(startAddress=0x%x, buffer=%p, size=%llu autoIncrement=%u) called with buffer size of 0.`
- `%s::%s numberOfRegisters = %d, _registerCount = %u, _startRegister= %u `
- `%s %s::%s:%d _resetFunction failed ret=0x%x`
- `%s AppleCSSPIv2Audio::%s:%d DMA DEBUG Register #1. %x-%x-%x-%x-%x-%x-%x-%x-%x-%x`
- `SPIv2 Unsupported command:%x\n`
- `%s %s:%d _writeDataBlock cannot transfer SPI header. ret=0x%x`
- `%s %s:%d _readDataBlock cannot transfer SPI header. ret=0x%x`
- `%s::%s(inDeviceIndex=%u, inAddress=0x%x, inMask=0x%x, inData=0x%x, writeVerify=%d) dataRead (0x%x) != dataWritten(0x%x) [errorCode:0x%x]`
- `%s::%s(inDeviceIndex=%u, inAddress=0x%x, inMask=0x%x, inData=0x%x) encountered error reading register [errorCode:0x%x]`
- `enableAudioHW failed`
- `%s AppleCSSPIv2Audio::%s:%d failed. address=0x%x wordTransfer=%d result=0x%x`
- `%s::%s:%d setProperty speakerID value:%u`
- `%s: Unsupported data-source-config version: %hhu`
- `%s::%s:%d Failed to enable prewarm. result=%s(0x%x)`
- `%s::%s(..) failed.`
- `%s::%s [%u] unable to create matching property index=%d [NumPhandles=%d]`
- `%s %s::%s cannot handle Gain Trim ver%d syscfg`
- `%s::%s _externalPowerManager=%p failed to addPowerProvider (%s)`
- `%s::%s:%d - vetoSleepWakeNotification(%p)`
- `%s::%s:%d Aborting power-down sequence _powerStage=%d`
- `No support for disappearing controls at the moment`
- `%s AppleCSSPIAudio::%s:%d _spiNub = %p. Ping() Failed`
- `%s AppleCSSPIv2Audio::%s:%d DMA DEBUG Register #3. %x-%x-%x-%x-%x-%x-%x-%x-%x-%x`
- `%s::%s:%d canPrimaryFunctionEnableAudio failed. result=%#x`
- `%s::%s: Failed to enable GPIO [result: 0x%x]`
- `%s:%s IOAudio2ControlDictionary::createSliderControl returned nullptr`
- `%s::Read Data address 0x%x:: 0x%x !=0x%x`
- `Forcing %s to be disabled`
- `enableAudioHW failed but continuing on...`
- `%s::%s external power dependency is satisfied`
- `Unable to get simple IO reporter information from the driver`
- `%s: SPI register read failed (%#x:%llu): %s\n`
- `%s::%s:%d Failed to turn %s. result=%s(0x%x)`
- `%s::%s(inDeviceIndex=%u, inAddress=0x%x, inMask=0x%x, inData=0x%x) failed to get write only mask [errorCode:0x%x]`
- `%s: Failed to disable injection on client close.`
- `%s::%s OSDictionary allocation failed`
- `%s::%s:%d setAudioStreamFormats failed with %s\n`
- `%s: Missing data-sources or data-sources-config property.`
- `%s: Error parsing clock-sources; offset %u`
- `%s::%s(extended=%d) _readMultiple(startRegister=%u,..., numberOfRegisters=%u) failed [errorCode : 0x%x]`
- `%s: I2C _readMultiple page write failed (%#x): %s\n`
- `%s::%s [%u] unable to allocate AppleExternalPowerManager`
- `_enableControlI2C currentControlReg =  0x%x `
- `%s AppleCSSPIv2Audio::%s:%d Read. Status after data was not OK 0x%x `
- `%s: Error processing property '%s'.`
- `%s::%s(inControlID=0x%x, ...) not allowed [result: 0x%x]`
- `%s::%s HPDetectKey: BadArgument`
- `%s AppleCSSPIv2Audio::%s:%d Write. Status was not OK address = 0x%x `
- `%s: Using default speakerID\n`
- `%s::%s(inControlID = %d) getControlByID returns NULL`
- `%s::%s(controlID = %u) controlBaseClassID = %u, copySelectorControlSelectorMap returns NULL `
- `%s: I2C _writeMultiple page write failed (%#x): %s\n`
- `%s::Not enough memory`
- `%s %s:%d _writeDataBlock cannot transfer SPI polls. ret=0x%x`
- `%s::%s:%d failed. sampleRate=%lld ret=%s(0x%x)`
- `%s:%s failed for %d. theAnswer=%s(0x%x)`
- `AppleMCKAudioFunction::%s could not get target instance`
- `%s::%s address = %u, value = %u, result = 0x%x `
- `messageClients(%#x)`
- `%s: %s\n`
- `%s::%s: Failed to disable GPIO [result: 0x%x]`
- `%s: I2C _writeReg page write failed (%#x): %s\n`
- `:%sFailed to create AppleBridgeAudio\n`
- `%s %s:%d Set PowerStage (%d -> %d)`
- `%s %s:%d instance = NULL. AppleCSSPIAudio::probe() Failed`
- `%s %s:%d cannot set auto increment. ret=0x%x`
- `%s:%s ioControlList is is nullptr`
- `Unable to locate nvram service`
- `%s::%s kPowerStageDesiredFastOn : commandSleep(&_externalPowerManager) has been interrupted %x. Retrying`
- `%s: SPI register read failed (%#x): %s\n`
- `%s: Error parsing data-destinations.`
- `%s::startIOEngineWithFlags() inFlags=0x%x`
- `%s::%s(%d) failed`
- `%s::%s:%d - kIOMessageCanSystemSleep (%#x) vetoSleepWakeNotification(%p) getAudioEnabled(kIODirectionNone)=%d`
- `%s::%s failed to validate operation (%u, %p, %p)`
- `%s %s:%d _writeDataBlock cannot de assert CS. ret=0x%x`
- `%s::%s(controlID = %u) unsupported controlBaseClassID = %u encountered`
- `AppleHapticsExternalSecondaryAudio::start(..) super::start(..) failed\n`
- `%s: I2C _writeReg page write failed (%#x, %#x): %s\n`
- `%s::%s(inDeviceIndex=%u, inAddress=0x%x, inMask=0x%x, inData=0x%x) encountered error writing register (dataToWrite=0x%x) [errorCode:0x%x]`
- `%s: I2C register read failed (%#x): %s\n`
- `%s: I2C _transferData to %s failed (Address : 0x%x): %s`
- `%s: I2C register page write failed (%#x, %#x): %s\n`
- `%s failed to initialize an AppleExternalPowerManager object`
- `%s::%s [%u] unable to get phandle at index=%d [NumPhandles=%d]`
- `%s failed to allocate an AppleExternalPowerManager object`
- `%s: could not allocate control %u`
- `%s (Requested device : %s) unable to to find dependent service (timeout = %llu ns)`
- `%s::%s(provider=%s) failed -> ret = %#x`
- `%s AppleCSSPIv2Audio::%s:%d Codec: SPI not ready AF2AF2AF2AF2AF2AF2AF2AF2`
- `AppleEmbeddedAudio::%s HW failure detected`
- `%s::%s (inRefCon = %p, inService = %p [%s], inNotifier = %p \n`
- `%s AppleCSSPIv2Audio::%s:%d Read. Status was not OK address = 0x%x `
- `%s::%s:%d Failed to enable prewarm. ret=%s(0x%x)`
- `%s::%s failed. inControlID=%d inValue=%d ret=%s(0x%x)`
- `%s::%s Unable to locate _powerPeakBudgetChangeFunction handler.`
- `%s: SPI register write failed (%#x:%llu): %s\n`
- `%s %s:%d _readDataBlock cannot transfer SPI data. ret=0x%x`
- `%s::%s:%d Found SpeakerID:%s value:%d`
- `%s::%s(deviceIndex=%d, address=0x%x) I2C register read from failed : %s`
- `%s::%s(deviceIndex=%d, address=0x%x) I2C register read failed: '%s' (%d)\n`
- `%s inConfigData cannot be nullptr`
- `%s %s::%s invalid gain size for Trim Gain V1`
- `%s: updateTimestamp not ready yet.\n`
- `%s::%s:%d kIOReturnNotReady`
- `%s:%s create injection control failed`
- `%s AppleCSSPIv2Audio::%s:%d Invalid Register Address = 0x%x `
- `%s::%s:%d SpeakerID:%u`
- `%s::stopIOEngineWithFlags() inFlags=0x%x result=%s(0x%x)`
- `%s: I2C register write failed (%#x, %#x): %s\n`
- `%s I2C failed to read:%x err:%d\n`
- `AppleMCKAudioFunction::%s setUpClock failed -> ret = %#x`
- `%s::%s:%d failed. requested sampleRate=%lld`
- `%s::%s awating for pending external power device(s)`
- `%s: getSupportedSampleRates returned nullptr`
- `%s: SPI register write failed (%#x, %#x): %s\n`
- `%s::startIOEngineWithFlags() inFlags=0x%x result=%s(0x%x)`
- `AppleHapticsExternalSecondaryAudio::start(..) failed.\n\n`
- `%s: I2C register read failed (%#x:%llu): %s\n`
- `%s failed to write onto NVRAM result=%#x`
- `%s %s::%s:%d _resetFunction2 failed ret=0x%x`
- `%s::%s kPowerStageDesiredFastOn : one of the dependencies is met; checking for others\n`
- `%s AppleCSSPIv2Audio::%s:%d Codec: Bus Write not ready AF1AF1AF1AF1AF1AF1AF1AF1`
- `%s AppleCSSPIv2Audio::%s:%d Write. Status after data transfer was not OK 0x%x `
