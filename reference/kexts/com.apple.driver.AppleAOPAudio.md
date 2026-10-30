# `com.apple.driver.AppleAOPAudio`

- Name: AppleAOPAudio
- Version: `600.1`
- UUID: `99095D8B-4235-36B3-AB64-21C9B33F5C6D`
- Source version: `600.1.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleEmbeddedAudioLibs`](com.apple.driver.AppleEmbeddedAudioLibs.md) 1.0, [`com.apple.driver.AppleSPU`](com.apple.driver.AppleSPU.md) 1.0.0, [`com.apple.iokit.IOAudio2Family`](com.apple.iokit.IOAudio2Family.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 9.0.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 9.0.0

## Device-tree nodes it binds (6) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/aop/iop-aop-nub/aop-audio`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-audio.md) | `AppleAOPAudioController` | `aop-audio` |
| [`/arm-io/iop-audio-controller/audio-hp`](../devicetree/root__arm-io__iop-audio-controller__audio-hp.md) | `AppleAOPAudioClientManager` | `audio-hp` |
| [`/arm-io/iop-audio-controller/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback.md) | `AppleAOPAudioClientManager` | `audio-leap-internal-loopback` |
| [`/arm-io/iop-audio-controller/audio-leap-internal-loopback/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback__audio-leap-internal-loopback.md) | `AppleAOPAudioClientManager` | `audio-leap-internal-loopback` |
| [`/arm-io/iop-audio-controller/audio-hw-pcm-audiomgr`](../devicetree/root__arm-io__iop-audio-controller__audio-hw-pcm-audiomgr.md) | `AppleAOPAudioPCMAssetManagerDevice` | `audio-hw-pcm-audiomgr` |
| [`/arm-io/iop-audio-controller/audio-haptic-leap`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic-leap.md) | `AppleAOPAudioHapticLEAP` | `audio-haptic-leap` |

## IOKit personalities (20) [KC]

### AppleAOPAudioAmpManagerDevice
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioAmpManagerDevice`
- `IOMatchCategory`: `AppleAOPAudioAmpManagerDevice`
- `IONameMatch`:
  - `audio-amp`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`
- `IOResourceMatch`: `IOKit`

### AppleAOPAudioButtonHapticDevice
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioButtonHapticDevice`
- `IONameMatch`:
  - `audio-aop-bhap`
  - `audio-bhap`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`
- `IOResourceMatch`: `IOKit`
- `IOUserClientClass`: `AppleAOPButtonHapticsServiceUserClient`

### AppleAOPAudioButtonOutput
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioButtonOutputDevice`
- `IONameMatch`:
  - `audio-aop-buttonout`
  - `audio-buttonout`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`
- `IOResourceMatch`: `IOKit`

### AppleAOPAudioClientManager
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioClientManager`
- `IONameMatch`:
  - `audio-hp`
  - `audio-aop-ldcm`
  - `audio-aop-hawking`
  - `audio-leap-internal-loopback`
  - `audio-leap-mca-loopback`
  - `audio-aop-speaker-manager`
  - `audio-aud-mca-baseband`
  - `audio-aud-mca-loopback`
  - `audio-aop-mca2-pmgr`
  - `audio-aop-mca3-pmgr`
  - `audio-aop-mca4-pmgr`
  - `audio-aop-mca5-pmgr`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`
- `IOResourceMatch`: `IOKit`

### AppleAOPAudioController
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioController`
- `IONameMatch`:
  - `aop-audio`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOPlatformPanicAction`: `89000`
- `IOProviderClass`: `AppleSPUAppInterface`
- `IOResourceMatch`: `IOKit`
- `IOUserClientClass`: `AppleAOPAudioUserClient`

### AppleAOPAudioDevice
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioDevice`
- `IOMatchCategory`: `AppleAOPAudioDevice`
- `IONameMatch`:
  - `audio-aop-edt-config`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`
- `IOResourceMatch`: `IOKit`

### AppleAOPAudioDeviceProvider
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioDeviceProvider`
- `IOMatchCategory`: `AppleAOPAudioDeviceProvider`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOPropertyMatch`:
  - `compatible`: `aop-audio-control`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`

### AppleAOPAudioFWdtAssetManagerDevice
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioFWdtAssetManagerDevice`
- `IONameMatch`:
  - `audio-fwdt-asset-mgr`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`
- `IOResourceMatch`: `IOKit`

### AppleAOPAudioHallDevice
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioHallDevice`
- `IONameMatch`:
  - `audio-hall`
  - `audio-aop-hall`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOProviderClass`: `IOService`
- `IOResourceMatch`: `IOKit`

### AppleAOPAudioHapticControlDevice
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioDeviceProvider`
- `IOMatchCategory`: `AppleAOPAudioDeviceProvider`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOPropertyMatch`:
  - `compatible`: `aop-audio-haptic`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`

### AppleAOPAudioHapticDebugControlDevice
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioDeviceProvider`
- `IOMatchCategory`: `AppleAOPAudioDeviceProvider`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOPropertyMatch`:
  - `compatible`: `aop-audio-hpdbg`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`

### AppleAOPAudioHapticLEAP
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioHapticLEAP`
- `IONameMatch`:
  - `audio-aop-haptic-leap`
  - `audio-haptic-leap`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`
- `IOResourceMatch`: `IOKit`

### AppleAOPAudioLEAP
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioLEAP`
- `IONameMatch`:
  - `audio-aop-leap`
  - `audio-leap`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`
- `IOResourceMatch`: `IOKit`

### AppleAOPAudioLEAPClientManager
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioLEAPClientManager`
- `IONameMatch`:
  - `audio-aop-hapticmgr`
  - `audio-hapticmgr`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`
- `IOResourceMatch`: `IOKit`

### AppleAOPAudioLPMicInDevice
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioLPMicInDevice`
- `IONameMatch`:
  - `audio-lp-mic-in`
  - `audio-aop-lp-mic-in`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`
- `IOResourceMatch`: `IOKit`

### AppleAOPAudioMCA2Device 
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioMCA2Device`
- `IOMatchCategory`: `AppleAOPAudioMCA2Device`
- `IONameMatch`:
  - `audio-mca0`
  - `audio-mca1`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`
- `IOResourceMatch`: `IOKit`

### AppleAOPAudioPCMAssetManagerDevice
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioPCMAssetManagerDevice`
- `IONameMatch`:
  - `audio-aop-pcmaudiomgr`
  - `audio-pcmaudiomgr`
  - `audio-hw-pcm-audiomgr`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`
- `IOResourceMatch`: `IOKit`
- `IOUserClientClass`: `AppleAOPAudioPCMAssetManagerUserClient`

### AppleAOPAudioPDM2Device
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioPDM2Device`
- `IONameMatch`:
  - `audio-aop-pdm2`
  - `audio-pdm2`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`
- `IOResourceMatch`: `IOKit`

### AppleAOPAudioSpeakerClientManager
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioSpeakerClientManager`
- `IONameMatch`:
  - `audio-aop-spkrmgr`
  - `audio-spkrmgr`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`
- `IOResourceMatch`: `IOKit`

### AppleAOPAudioSpeakerControlDevice
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `IOClass`: `AppleAOPAudioDeviceProvider`
- `IOMatchCategory`: `AppleAOPAudioDeviceProvider`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPAudio`
- `IOPropertyMatch`:
  - `compatible`: `aop-audio-speaker`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`


## C++ classes (32) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleAOPAudioAmpManagerDevice` | 0xa8 | AppleAOPAudioDevice → IOService → IORegistryEntry |
| `AppleAOPAudioAmpStateFunction` | 0x38 | AppleARMFunction |
| `AppleAOPAudioAssetManagerDevice` | 0xb8 | AppleAOPAudioDevice → IOService → IORegistryEntry |
| `AppleAOPAudioButtonHapticDevice` | 0xb0 | AppleAOPAudioDevice → IOService → IORegistryEntry |
| `AppleAOPAudioButtonOutputDevice` | 0xa8 | AppleAOPAudioDevice → IOService → IORegistryEntry |
| `AppleAOPAudioClientManager` | 0xc0 | AppleAOPAudioDevice → IOService → IORegistryEntry |
| `AppleAOPAudioCodecRequestCompletionFunction` | 0x38 | AppleARMFunction |
| `AppleAOPAudioController` | 0xf0 | AppleBaseAudioController → IOService → IORegistryEntry |
| `AppleAOPAudioDevice` | 0xa8 | IOService → IORegistryEntry |
| `AppleAOPAudioDeviceController` | 0x10 |  |
| `AppleAOPAudioDeviceControllerObject` | 0x18 | AppleAOPAudioDeviceController |
| `AppleAOPAudioDeviceNode` | 0x98 | IOService → IORegistryEntry |
| `AppleAOPAudioDeviceProvider` | 0xb8 | AppleAOPAudioDevice → IOService → IORegistryEntry |
| `AppleAOPAudioFWdtAssetManagerDevice` | 0xb8 | AppleAOPAudioAssetManagerDevice → AppleAOPAudioDevice → IOService → IORegistryEntry |
| `AppleAOPAudioHallDevice` | 0xa8 | AppleAOPAudioDevice → IOService → IORegistryEntry |
| `AppleAOPAudioHapticLEAP` | 0xb8 | AppleAOPAudioLEAP → AppleAOPAudioDevice → IOService → IORegistryEntry |
| `AppleAOPAudioLEAP` | 0xb8 | AppleAOPAudioDevice → IOService → IORegistryEntry |
| `AppleAOPAudioLEAPClientManager` | 0xd8 | AppleAOPAudioClientManager → AppleAOPAudioDevice → IOService → IORegistryEntry |
| `AppleAOPAudioLPMicInDevice` | 0xcf0 | AppleAOPAudioDevice → IOService → IORegistryEntry |
| `AppleAOPAudioMCA2Device` | 0xa8 | AppleAOPAudioDevice → IOService → IORegistryEntry |
| `AppleAOPAudioPCMAssetManagerDevice` | 0xb8 | AppleAOPAudioAssetManagerDevice → AppleAOPAudioDevice → IOService → IORegistryEntry |
| `AppleAOPAudioPCMAssetManagerUserClient` | 0xf8 | IOUserClient → IOService → IORegistryEntry |
| `AppleAOPAudioPDM2Device` | 0xb0 | AppleAOPAudioDevice → IOService → IORegistryEntry |
| `AppleAOPAudioSawDevice` | 0xa8 | AppleAOPAudioDevice → IOService → IORegistryEntry |
| `AppleAOPAudioService` | 0x90 | AppleAOPAudioServiceBase → IOService → IORegistryEntry |
| `AppleAOPAudioServiceBase` | 0x88 | IOService → IORegistryEntry |
| `AppleAOPAudioSpeakerClientManager` | 0xe0 | AppleAOPAudioLEAPClientManager → AppleAOPAudioClientManager → AppleAOPAudioDevice → IOService → IORegistryEntry |
| `AppleAOPAudioUserClient` | 0xf0 | IOUserClient → IOService → IORegistryEntry |
| `AppleAOPButtonHapticsServiceUserClient` | 0xf0 | IOUserClient → IOService → IORegistryEntry |
| `AppleAudioSequenceList` | 0x28 |  |
| `AppleAudioSequenceOperation` | 0x10 |  |
| `AppleBaseAudioController` | 0xc0 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000cdf5 off=0x001566d0-0x001634c5 addr=0xfffffe000715a6d0-0xfffffe00071674c5 r--/r--   __TEXT            
	sz=0x0000c591 off=0x00156de8-0x00163379 addr=0xfffffe000715ade8-0xfffffe0007167379               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000136 off=0x00163380-0x001634b6 addr=0xfffffe0007167380-0xfffffe00071674b6               __TEXT.__const            
	sz=0x0000000f off=0x001634b6-0x001634c5 addr=0xfffffe00071674b6-0xfffffe00071674c5               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0002f178 off=0x01690620-0x016bf798 addr=0xfffffe0008694620-0xfffffe00086c3798 r-x/r-x   __TEXT_EXEC       
	sz=0x0002eb28 off=0x01690620-0x016bf148 addr=0xfffffe0008694620-0xfffffe00086c3148          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000650 off=0x016bf148-0x016bf798 addr=0xfffffe00086c3148-0xfffffe00086c3798          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000999 off=0x0492ea30-0x0492f3c9 addr=0xfffffe000b932a30-0xfffffe000b9333c9 rw-/rw-   __DATA            
	sz=0x000002f0 off=0x0492ea30-0x0492ed20 addr=0xfffffe000b932a30-0xfffffe000b932d20               __DATA.__data             
	sz=0x00000660 off=0x00000000-0x00000660 addr=0xfffffe000b932d20-0xfffffe000b933380               __DATA.__common           (Zerofill)
	sz=0x00000049 off=0x00000000-0x00000049 addr=0xfffffe000b933380-0xfffffe000b9333c9               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x0000c7a8 off=0x00f9e5c0-0x00faad68 addr=0xfffffe0007fa25c0-0xfffffe0007faed68 rw-/rw-   __DATA_CONST      
	sz=0x000000e8 off=0x00f9e5c0-0x00f9e6a8 addr=0xfffffe0007fa25c0-0xfffffe0007fa26a8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x000000e0 off=0x00f9e6a8-0x00f9e788 addr=0xfffffe0007fa26a8-0xfffffe0007fa2788         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x0000b7c8 off=0x00f9e788-0x00fa9f50 addr=0xfffffe0007fa2788-0xfffffe0007fadf50         __DATA_CONST.__const            
	sz=0x00000a00 off=0x00fa9f50-0x00faa950 addr=0xfffffe0007fadf50-0xfffffe0007fae950         __DATA_CONST.__kalloc_type      
	sz=0x00000328 off=0x00faa950-0x00faac78 addr=0xfffffe0007fae950-0xfffffe0007faec78         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000e8 off=0x00faac78-0x00faad60 addr=0xfffffe0007faec78-0xfffffe0007faed60         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x00faad60-0x00faad68 addr=0xfffffe0007faed60-0xfffffe0007faed68         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 231 at 0x04ad16ac
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     99095D8B-4235-36B3-AB64-21C9B33F5C6D
008: LC_SOURCE_VERSION           600.1.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a96b38 size=0x608
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleAOPAudio`
- `CFBundleGetInfoString`: `600.1, Copyright Apple Computer, Inc. 2015`
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPAudio`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleAOPAudio`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `600.1`
- `CFBundleSignature`: `aapl`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `600.1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2022 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.1`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleAOPAudio.kext`
- `_PrelinkExecutableLoadAddr`: `-2198904396080`
- `_PrelinkExecutableRelativePath`: `AppleAOPAudio`
- `_PrelinkExecutableSize`: `299182`
- `_PrelinkExecutableSourceAddr`: `-2198904396080`
- `_PrelinkKmodInfo`: `-2198829061584`

## Strings (1152) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `%s`

**[__TEXT.__cstring]**

- `hfdConfig`
- `+ %s::%s() {this: %p} built %s %s\n`
- `historicalDataCallback`
- `<unknown>`
- `param2`
- `matching`
- `site.AppleAOPAudioDeviceProvider`
- `Util::addDictionaryEntry(ioEventReport, keyDriftDetect, mDriftDetectInfo.driftDetect)`
- `audioService->attach(inProvider)`
- `mCommandGate->runAction(OSMemberFunctionCast(IOCommandGate::Action, this, &AppleBaseAudioController::_accessRegister), reinterpret_cast<void *>(inDeviceId), static_cast<void *>(inDescriptor))`
- `mAudStatus`
- `AppleAOPAudioCodecRequestCompletionFunction::%s(...) mLPMicInDevice cannot be nullptr\n`
- `- PDM2Device::getMicTuningParameters err: 0x%x\n`
- `PDM2Device:: Failed to get HFDec coeff`
- `+-Device::start() {identifier: '%c%c%c%c'} -> %d, err: 0x%x\n`
- `mController->mService->initChannelControl(mChannelControl, &mChannelStatus)`
- `mController->setDeviceProperty(kClientListeningInput,ClientManagerProperties::kCurrentPowerRequest,&req,sizeof(req))`
- `mIdentifierVec`
- ` LPMicInDevice::%s ret=%#x\n`
- `state`
- `121111121222121211121212112`
- `AppleAOPAudioLPMicInDevice::%s stopIO failed, ret=%#x\n`
- `site.AppleAOPAudioSpeakerClientManager`
- `mLPMicInDevice->enableListening(inControlValue, inControlID)`
- `%c%c%c%c`
- `registerWrite`
- `site.AppleAOPAudioAmpStateFunction`
- `processDeviceTreeConfig`
- `setChannelControl(cc)`
- `%s::%s() failed to %s property (@0x%x): 0x%x\n`
- `TxAOutputPadFailure`
- `Client is reqesting null device controller '%c%c%c%c'\n`
- `initClockConfig`
- `LPMicInDevice::%s woke up from sleep commandSleepResult=%#x.retries=%d \n`
- `pdmFrequency`
- `- %s::%s('%c%c%c%c', %p, %p) -> 0x%x\n`
- `LPMicInDevice::%s State change was successful. replyStatus=%#x. Breaking out of sleep loop, retries=%d \n`
- `AppleAudioSequenceList`
- `rxFifoHiWatermark`
- `+ MCA2Device::getStatusReport(%p)\n`
- `%s::%s() registerFunctionParent failed [kIOReturn: 0x%x]\n`
- `AppleAOPAudioLPMicInDevice::%s inEnable=%d. isListeningEnabled()=%d \n`
- `site.AppleAudioSequenceList`
- `+ PDM2Device::getCoeffecients\n`
- ` MCA2Device::getStatusReport() added %d entries\n`
- `+ AppleAOPAudioDeviceProvider::setDevicePowerState('%c%c%c%c', '%c%c%c%c')\n`
- `enableListening`
- `transferEdtProperty`
- `compatible`
- `aop host time`
- `<%c%c%c%c>(): ClkDomain Read <%c%c%c%c> size:%zu\n`
- `PDM2Device::%s invalid gain struct size for Trim Gain V2 header.mSizeSt:%#x cfg->gainInfo[0]:%#lx\n`
- `super::handleStart(inProvider)`
- `%s::%s('%c%c%c%c', 0x%x)  unexpected device state: '%c%c%c%c'(%d)\n`
- `setSampleRate`
- `LPMicInDevice::enableListening<%c%c%c%c>, pwr state = <%c%c%c%c> \n`
- `param3`
- `channelStatus`
- `IODeviceTree:/chosen`
- `%s::%s() service has %d devices\n`
- `_waitTillAwake`
- `getNumberOfSupportedAssets`
- `aopInternalDataPacket`
- `AppleAOPAudioLEAPClientManager`
- `AppleAOPAudioLPMicInDevice::%s inEnable=%d. isListeningEnabled()=%d calling stopIO\n`
- `site.AppleAOPAudioUserClient`
- `inFirmwareData`
- `!(inFirmwareData->getLength() > maxLeapFirmwareBufferSizeBytes)`
- `mIOReporter->updateReport(inChannels, inAction, outResult, inDestination, theStatusReport)`
- `startHardware`
- `LPMicInDevice::%s codecReply->replyTime (%llx) <= mPendingConfigureCodecRequest.requestTime (%llx)\n`
- `+-PDM2Device::init(%p, %p) -> %d\n`
- `%s::%s(ty %d, buf %p) failed, err: 0x%x\n`
- `!(1)`
- `_initChannelControl()`
- `LPMicInDevice::%s codecReply->replyState (%d) , mPendingConfigureCodecRequest.requestState (%d)\n`
- `- UserClient::method_Close() -> 0x%x\n`
- `AppleAOPAudioDeviceControllerObject`
- `Create`
- `site.AppleAOPAudioIOReporter`
- `getBuffer`
- `%s:%s: Adding operation with code: '%c%c%c%c'`
- `PDM2Device::getMicTuningParameters channelCount:%d TurnOn:%d Settle:%d Sensitivity:%d/1000000 Cal:%d\n`
- `- PDM2Device::getCoeffecientsForHFD err: 0x%x\n`
- `Util::addDictionaryEntry(theSubgroupReport, keyTxADMAFifoOverflow, txStatus.TxADMAFifoOverflow)`
- `%s::%s() returns %p\n`
- `PanicHandler::%s Error Registering. Max reached!`
- `processDeviceTreeU32Entry(keyEnableTimeoutUs, AppleAOPAudioFirmware::ButtonProperties::kHapticsEnableTimeoutPeriodUs)`
- `AppleAOPAudioLPMicInDevice::%s could not find property for \"%s\"`
- `!(0 == streamDesc.mSampleRate)`
- `%s::%s() -> 0x%x\n`
- `AppleAOPAudioLPMicInDevice::%s enable=%d. notifyCodecOfFailure=%d\n`
- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNameFastClockSpeed, &lowPowerConfig.fastClockSpeed )`
- `AppleAOPAudioLPMicInDevice`
- `theSubgroupReport`
- `- UserClient::method_SetControlValue() -> 0x%x\n`
- `mInputHandler->_handleHistoricMailboxData(pAudioPayload, audioPayloadSizeBytes, aopTimestamp, aopByteCount)`
- `Util::addDictionaryEntry(ioEventReport, keyDriftEventCount, mDriftDetectInfo.driftEventCount)`
- `%s::%s() iodir 0x%x ==> 0x%x\n`
- `- %s::%s('%c%c%c%c', %p) -> 0x%x\n`
- `%s{} detected %d inconsistent Hist byte seq in packets - byteCnt: %lld, expected: %lld\n`
- `_getDeviceProperty`
- `Util::addDictionaryEntry(ioEventReport, buf, ioEvents.audIOEvents[i].IOEvent[AOPAudIOEventInfo::kAOPIOEventStart].AudIOStat[ii])`
- `sizeof(mState) == sz`
- `+ %s::%s(control id: 0x%x, value: 0x%x)\n`
- `!(0 == attachedDevices)`
- `i8@?0`
- `12`
- `%s - no such control index %d\n`
- `sHistoricalDataCallback`
- `site.AppleAOPAudioDeviceControllerObject`
- `_getProperty(IOHandlerProperties::kListeningOnGestureEnabledProp, mListeningOnGestureEnabled, true)`
- `+ %s::%s, unsupported input sample rate = %d\n`
- `aop zero host time`
- `\n`
- `ratios`
- `121111121222121211`
- `TxBIOTimeout`
- `mListeningOnGestureSupported`
- `mExternalKernelInterface`
- `- %s::%s() {this: %p} -> %s\n`
- `mController`
- `getDeviceProperty`
- `AudioDevice:%c%c%c%c`
- `Util::addDictionaryEntry(ioEventReport, keyFirstDriftIOEventID, mDriftDetectInfo.firstDriftIOEventID)`
- `mController->setDeviceProperty(getIdentifier(), property, reinterpret_cast<const void*>(&internalProp), sizeof(AppleAOPButtonHapticsAssetInternalProp))`
- `Util::addDictionaryEntry(theSubgroupReport, keyTxAFifoUnderflow, txStatus.TxAFifoUnderflow)`
- `%s::%s() was not supplied with status buffer %p or data buffer %p\n`
- `inData`
- `\"%s::%s(requestState=%d, replyState=%d) should not be called without owning workloop\" @%s:%d`
- `updateAsset`
- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNamePdmcFrequency, &lowPowerConfig.pdmcFrequency )`
- `PDM2Device::%s cannot handle Gain Trim version-%d syscfg\n`
- `Util::addDictionaryEntry(theSubgroupReport, keyStateErrorCount, mStateErrorCount)`
- `Util::addDictionaryEntry(theSubgroupReport, keyTxBFifoFrameError, txStatus.TxBFifoFrameError)`
- `_publishBelow`
- `audio-lp-mic-in`
- `mService->notifySystemShutdownEvent(static_cast<uint32_t>(lpmsVal))`
- `site.AppleAOPAudioMCA2Device`
- `mController->mService`
- `- IOReporter::updateReport(%p, 0x%x, %p, %p, %p) -> 0x%x\n`
- `_getIdentifersFromDeviceTree()`
- `setControlValue`
- `!(inoutPropertyLength < property->getLength())`
- `AppleAOPAudioCodecRequestCompletionFunction::%s(...) inTarget cannot be nullptr\n`
- `PDM2Device:: Failed to get HFDec latency`
- `listening on gesture enabled`
- `loadLeapFirmware(firmwareData)`
- `- LPMicInDevice::configureCodec ret=%#x isCodecConfigurationSupported()=%d\n`
- `- UserClient::method_Open() -> 0x%x\n`
- `_enableListening(inControlValue)`
- `AppleAOPAudioDevice`
- `- %s::%s inDeviceID=%d ret=%#x\n`
- `info`
- `mCommandGate->runAction(_getBuffer, &inBufferType, &theBuffer)`
- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNameSlowClockSpeed, &lowPowerConfig.slowClockSpeed )`
- `micSettleTimeMs`
- `PDM2Device::getCoeffecients() failed to get 'coefficients' property, error: 0x%x\n`
- `theUserClient->mProvider->stopHardware()`
- `RxBFifoOverflow`
- `_enableListeningIOHandler`
- `%s::%s() node %c%c%c%c, propertyId %u propertyVal is NULL\n`
- `site.AppleAOPAudioLEAPClientManager`
- `channelCount <= kMaxPDMNodeMicrophoneCount`
- `mProvider`
- `mInputHandler->_handleMailboxData(pAudioPacket->payload, packetPayloadBytes - sizeof(AppleAOPAudioFirmware::SubPacket), aopMachAbsTimestamp, byteCount, spuTimestamp)`
- `bytes per sample`
- `_initIOConfigurations`
- `+ ButtonOutputDevice::getStatusReport(%p)\n`
- `Util::addDictionaryEntry(ioEventReport, keyMaxDriftTimeDelta, mDriftDetectInfo.maxDriftTimeDelta)`
- ` LPMicInDevice::%s Failed to send request to the codec ret=%#x\n`
- `outStatus`
- `mCommandGate->runAction(action, reinterpret_cast<void *>(inDeviceId), reinterpret_cast<void *>(inClientId), NULL, NULL)`
- `Util::addDictionaryEntry(theSubgroupReport, keyRxBDMAFifoUnderflow, rxStatus.RxBDMAFifoUnderflow)`
- `%s::%s() failed to transfer node %c%c%c%c, propertyId %u, ret = %d\n`
- `AppleAOPAudioLPMicInDevice::%s enable=%d. Request the codec to enable listening\n`
- `+ UserClient::method_StopHardware()\n`
- `RxBFifoFrameError`
- `processDeviceTreeU32Entry`
- `AppleAOPAudioLEAP`
- `AppleAOPAudioAmpStateFunction::%s(...) mAmpManagerDevice cannot be nullptr\n`
- `+-%s::%s()\n`
- `_createIOReport`
- `1211111212221212111111111111111`
- `mService->RetrieveHistoricalData(AppleAOPAudioController::sHistoricalDataCallback, static_cast<OSObject*>(this))`
- `!(count > kMaxIdentifiers)`
- `%s [stop]_%d`
- `AppleAOPAudioLPMicInDevice::%s configureCodec failed for kAOPLPMicInDeviceStopIO, ret=%#x\n`
- `mAssetResourceData->prepare(::kIODirectionInOut)`
- `%s::%s() got service controller '%c%c%c%c'\n`
- `+ UserClient::method_Close()\n`
- `_setPowerState`
- `- %s::%s(%d, 0x%x, %d) -> 0x%x\n`
- `%s failed [errorCode: 0x%x]`
- `method_StopHardware`
- `Util::addDictionaryEntry(theSubgroupReport, keyTxAIOTimeout, txStatus.TxAIOTimeout)`
- `AppleAOPAudioDeviceNode`
- `mDeviceActiveDirections`
- `+ UserClient::clientMemoryForType(type: %d)\n`
- `_setupAudioService`
- `productSpecificExternalClientRequestCallGated(inRequest)`
- `inAddress`
- `+ PDM2Device::getCoeffecientsForHFD\n`
- `TxAFifoFrameError`
- `AppleARMFunction::registerFunctionParent(provider, this)`
- `mController->_setDeviceProperty(mIdentifier, inPropertyId, &inPropertyValue, sizeof(inPropertyValue))`
- `publishStreamProperties()`
- `+-%s::%s(provider: %p) -> %d, err: 0x%x\n`
- `AppleAOPAudioLPMicInDevice::%s configureCodec failed for kAOPLPMicInDeviceListeningDisabled, ret=%#x\n`
- `handleHistoricMailboxData`
- `PDM2Device:: Failed to get HFDec length`
- `entitlement == kOSBooleanTrue`
- `%s{} detected %d inconsistent Live byte seq in packets - byteCnt: %lld, expected: %lld\n`
- `mDevices->setObject(nm, inDevice)`
- `AppleAOPAudioCodecRequestCompletionFunction %s:%d inParam1=%d result=%#x\n`
- `mController->attachDevice(id, mClientId)`
- `ReportToAggD`
- `getHFDecimatorConfig(inProvider, kPropertyNameHfdConfigForHighPowerClks, *hfDecCfg)`
- `+ %s::%s('%c%c%c%c', 0x%x)\n`
- `+ UserClient::method_SetControlValue()\n`
- `- %s::%s(%ld) -> 0x%x\n`
- `+ LPMicInDevice::%s inReqState=%d\n`
- `mController->getDeviceProperty(kAppleAOPAudioPDMDeviceId, AppleAOPPDM2Properties::kHFDecimatorCfgForHighPowerClock, hfDecCfg, &hfDecCfgSize)`
- `AppleAOPAudioHapticLEAP`
- `Controller::%s() Power Up On Gesture state change, listening %sabled\n`
- `+-%s::%s\n`
- `getState()`
- `AppleAOPAudioHallDevice`
- ` %s{} haveLPMicInNub: %d\n`
- `_setControlValue`
- `+ %s::%s(%d, .., %d)\n`
- `AppleAOPAudioAmpStateFunction::%s(...) failed.\n`
- `theBuffer`
- `setActiveChannelMask`
- `enabledChannels`
- `Util::addDictionaryEntry(theSubgroupReport, keyTxAOutputPadFailure, txStatus.TxAOutputPadFailure)`
- `mInputHandler->_handleHardwareError(pAudioPacket)`
- ` AmpManagerDevice::getStatusReport() added %d entries\n`
- `AppleAOPAudioFWdtAssetManagerDevice`
- `Util`
- `+ %s::%s('%c%c%c%c', 0x%llx, 0x%llx)\n`
- `super::start(provider)`
- `AppleAOPAudioAmpStateFunction::%s(...) inTarget cannot be nullptr\n`
- `close`
- `%s::%s THREAD_AWAKENED retries=%d\n`
- `IOUserClient::initWithTask(inOwningTask, inSecurityToken, inType, inProperties)`
- `mController->setDeviceProperty(getIdentifier(static_cast<uint32_t>(LEAPIdentifierIndex::LEAPFirmwareAsset)), AppleAOPAudioFirmware::FirmwareAssetProperties::kFirmware, inFirmwareData->getBytesNoCopy(), inFirmwareData->getLength())`
- `_setupAudioService(inProvider)`
- `theioEventKey`
- `startIO`
- `mController->getDeviceProperty(kAppleAOPAudioPDMDeviceId, AppleAOPPDM2Properties::kLowPowerConfiguration, &lowPowerConfig, &lowPowerConfigSize)`
- `+-%s::%s('%c%c%c%c', %p) -> 0x%x\n`
- `%s [drift]`
- `function-codec_lpmic`
- `LPMicInDevice::%s codecReply->requestID (%lld) != mPendingConfigureCodecRequest.requestID (%lld)\n`
- `mDeviceController`
- `TxAIOTimeout`
- `outProperty`
- `PanicHandler::%s Disabled!`
- `EnableTimeoutCount`
- `publishBelow(inProvider)`
- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNameChannelPolaritySelect, &lowPowerConfig.channelPolaritySelect, sizeof(lowPowerConfig.channelPolaritySelect) )`
- `decimatorConfigForHighPowerClks`
- `- %s::%s(%p) {published %d kids} -> 0x%x\n`
- `theDriver->historicalDataCallback(packetType, timestamp, payload, size, options)`
- `site.AppleAOPAudioCodecRequestCompletionFunction`
- `checkDataPacket(inData, inDataSize)`
- `AppleAOPAudioService::getNamedProperty(inService, kPropertyNameChannelCount, &channelCount)`
- `AppleAOPAudioUserClient`
- `+-%s::%s(0x%x, %lld, %p, %zu, 0x%x)\n`
- `Util::addDictionaryEntry(ioEventReport, buf, ioEvents.audIOEvents[i].IOEventID)`
- `reset`
- `AppleAOPAudioService::getNamedProperty(inService, kPropertyNameMicTurnOnTimeMs, &micParams.micTurnOnTimeMs.value[0])`
- `mController->_setDeviceProperty(mIdentifier, IOHandlerProperties::kChannelControlProperty, &mChannelControl, sizeof(AOPChannelControl))`
- `AOPDevice.RegWriteRetry`
- `callFunction`
- `AOPDevice.RegWriteCommProtocolFailure`
- `inDevice`
- `initClockConfig()`
- `+%s::%s(%p)\n`
- `AppleAOPAudioPDM2Device`
- `getDeviceActiveDirections(deviceNum, activeDirection)`
- `%s::%s('%c%c%c%c', %sable, 0x%x) err: 0x%x\n`
- `%s: %c%c%c%c, restype: %c%c%c%c, id: %04hx, size: %u, start: 0x%02hhx%02hhx, end: 0x%02hhx%02hhx\n`
- `inDescriptor`
- `callPlatformFunction`
- `kPacketTypeServiceInterrupted`
- `stopHardware`
- `processResourceUpdateRequest`
- `mList`
- `+-SawDevice::init(%p) -> %d\n`
- `%s::%s() kSpuPacketTypeMCAReport payload size %zu, less than expected %zu\n`
- `mMemoryResourceData`
- `device2Id(deviceNum, id)`
- `!(currentPtr == nullptr)`
- `sizeof(uint32_t) == disableCountSz`
- `theDriver->_getBuffer(*theBufferType, *theBuffer)`
- `initChannelControl()`
- `+-PDM2Device::init(%p) -> %d\n`
- `registerRead`
- `outBuffer`
- `%s::%s() processed %llu bytes of historic data\n`
- `MB::%s Timestamp(drift) Host(AP)=%llu, ZeroTS(AOP)=%llu \n`
- `get`
- `Util::addDictionaryEntry(theSubgroupReport, keyRxAFifoFrameError, rxStatus.RxAFifoFrameError)`
- `Util::addDictionaryEntry(theSubgroupReport, keyTxBShimDrainFailure, txStatus.TxBShimDrainFailure)`
- `mInputHandler->_startIO()`
- `serviceCallback`
- `inoutPropertyLength`
- `mService->detachDevice(inDeviceId, inClientId)`
- `ap io host time`
- `%s::%s('%c%c%c%c', %d, ..) failed, status: 0x%x\n`
- `_accessRegister`
- `aop zero frame cnt`
- `historyChannels`
- `- MCA2Device::getStatusReport(%p) -> 0x%x\n`
- `getNamedProperty(inName, static_cast<void*>(outProperty), &sz)`
- `Util::addDictionaryEntry(ioEventReport, buf, ioEvents.audIOEvents[i].IOEvent[AOPAudIOEventInfo::kAOPIOEventStop].AudIOStat[ii])`
- `%s:%c%c%c%c`
- `121111121222121211111111111112`
- `cb count`
- `_setDeviceProperty`
- `Util::addDictionaryEntry(ioEventReport, keyDriftThreshold24MHz, AOPAudioDriftDetect::kDriftThreshold24MHz)`
- `site.AppleAOPAudioController`
- `mController->setDeviceProperty(getIdentifier(), propertyId, inArgs, inArgsSize)`
- `mCommandGate->runAction(_startHardware, &inDeviceID)`
- `%s:%s: Failed to execute operation '%c%c%c%c': %x`
- `%s::%s('%c%c%c%c', %d) complete, status 0x%x\n`
- `listening enabled`
- `%s::%s() wake buffer filled with %d bytes\n`
- `+ LPMicInDevice::%s\n`
- `1211111212221212111`
- `mController->setDeviceProperty(kAppleAOPAudioPDMDeviceId, AppleAOPPDM2Properties::kLowPowerConfiguration, &lowPowerConfig, sizeof(LowPowerPDM2Configuration))`
- `_enableListening`
- `!(((histPacket->size - sizeof(SpuMCAPacket)) > histBytes))`
- `this->_initIOConfigurations()`
- `%s::%s() unknown buffer type: 0x%x\n`
- `%s::%s(inPropertyID=%d, inAmpState=%d) setDeviceProperty(kAmpState) failed. [errorCode: 0x%x]\n`
- `handleStart`
- `mController->getDeviceProperty(id, ClientManagerProperties::kState, &state, &sz)`
- `AppleAOPAudioMCA2Device`
- `mController->getDeviceProperty(getIdentifier(), MCA2Properties::kMCATxStatus, &txStatus, &txStatusSz)`
- `PDM2Device:: Failed to get Dec latency`
- `mController->getDeviceProperty(getIdentifier(static_cast<uint32_t>(LEAPIdentifierIndex::LEAPFirmwareAsset)), AppleAOPAudioFirmware::FirmwareAssetProperties::kFirmwareBufferBytesMax, (void*)&maxLeapFirmwareBufferSizeBytes, &argSize)`
- `- AmpManagerDevice::getStatusReport(%p) -> 0x%x\n`
- `AppleAOPAudioCodecRequestCompletionFunction %s:%d Incorrect Signature: Expected=0x%x Received=0x%x pHandle=0x%x`
- `%s::%s skip=%d disableAccFw=%d waitLEAPFwLoad=%d`
- `debug`
- `+-ButtonOutputDevice::start(provider: %p) -> %d, err: 0x%x\n`
- `theUserClient->mProvider->startHardware()`
- `!(nullptr != mInputHandler && nullptr != mLPMicInDevice)`
- `Async AOP event '%s'(0x%x): aop time %lldns, ap time %lldns, delta %lldns\n`
- `site.AppleAOPAudioIOHandler`
- `- %s::%s(%d, 0x%x) -> 0x%x\n`
- `resourceType == kAppleAOPAudioResourceType_Firmware`
- `channelPhaseSelect`
- `Button Haptics Asset Interface`
- `mService->GetProperty(inProperty, outPayload, outPayloadLength)`
- `device input latency in frames`
- `%s [strt]_%d`
- `- LPMicInDevice::%s <%c%c%c%c>() inEnable=%d mHardwareEnabled=%d -> 0x%x\n`
- `outMemory`
- `TxAShimDrainFailure`
- `Util::addDictionaryEntry(theSubgroupReport, keyTxBDMAFifoOverflow, txStatus.TxBDMAFifoOverflow)`
- `121111121222121212111111`
- `initForPM`
- `first drift io event id`
- `expression \"%s\" FAILED, %s::%s(), line %d, status: 0x%x\n`
- `PDM2Device:: Failed to get Dec ratios`
- `%s::%s(%s) length (%d) is to big for destination (%d), truncating\n`
- `%s::%s() error: 0x%x\n`
- `_setActiveChannelMask`
- `updateReport`
- `initCodecConfigurationHandle(inProvider)`
- `site.AppleAOPAudioAssetManagerDevice`
- `setProperty`
- `MCA2RxAShimOverrun`
- `_getProperty(IOHandlerProperties::kSupportsListeningOnGestureProp, mListeningOnGestureSupported, true)`
- `reporterObject`
- `initCommandGate()`
- `LPMicInDevice::stopIO<%c%c%c%c>, pwr state = <%c%c%c%c> \n`
- `mController->getDeviceProperty(getIdentifier(), AppleAOPButtonHapticsProperties::kNumAssets, static_cast<void*>(&mMaxAssets), &sz)`
- `verbose level`
- `+ %s::%s, supported sample rate(s) = %d\n`
- `+ %s::%s inDeviceID=%d\n`
- `resourceType`
- `Util::addDictionaryEntry(theSubgroupReport, keyTxBOutputPadFailure, txStatus.TxBOutputPadFailure)`
- `function`
- `unRegisterMemoryForZeroOut`
- `audioSampleData`
- `initChannelControl`
- `TimeElapsedToPublishMs`
- `+ AppleAOPAudioDeviceProvider::setDevicePowerState('%c%c%c%c', %d)\n`
- `startAddress`
- `LPMicInDevice::startIO<%c%c%c%c>, pwr state = <%c%c%c%c> \n`
- `RxAFifoFrameError`
- `  AppleAOPAudioIOHandler::_stopIO() unknown state value: '%c%c%c%c' (0x%x)\n`
- `AppleAudioSequenceOperation`
- `mController->setDeviceProperty(id, ClientManagerProperties::kCurrentPowerRequest, &req, sizeof(req))`
- `mLPMSKeyFunction->callFunction(&lpmsVal)`
- `mController->getDeviceProperty(getIdentifier(), propertyId, outArgs, outArgsSize)`
- `mCommandGate->runAction(_stopHardware, &inDeviceID)`
- `success`
- `Util::addDictionaryEntry(theSubgroupReport, keyRxBFifoOverflow, rxStatus.RxBFifoOverflow)`
- `%s::%s(%d) low power audio input now %sabled\n`
- `%s::%s() unknown power state ordinal '0x%lx'\n`
- `_updateReport`
- `initInputBuffer()`
- `handlePropertyAccess`
- `mController->getDeviceProperty(kAppleAOPAudioPDMDeviceId, AppleAOPPDM2Properties::kHFDecimatorCfg, hfDecCfg, &hfDecCfgSize)`
- `mLPMicInDevice->handleHistoricMailboxData(pAudioPayload, audioPayloadSizeBytes, aopTimestamp, aopByteCount, pSPUPacket->timestamp)`
- `historicalBytesSinceWake`
- `_setProperty(AudioNodeProperties::kIORunning, false)`
- `FillBuffer`
- `copyNamedAudioPropertyFromDeviceTree(inPropertyName, static_cast<void*>(outPropertyValue), sz)`
- `sizeof(histDataSupported) == szHistDataSupported`
- `PDM2Device:: Failed to get Dec Serv`
- `parkingInfoData`
- `+-UserClient::initWithTask(%p, ...) -> %s\n`
- `%s::%s() kPacketTypeHistoricData requires mLPMicInDevice `
- `initForPM(inProvider)`
- `_addDevice`
- `121111121222121211121222222212222122222211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `result`
- `mController->setDeviceProperty(kAppleAOPAudioPDMDeviceId, AppleAOPPDM2Properties::kHFDecimatorCfg, hfDecCfg, sizeof(RTKitAudioDrivers::PDMStreamConfig::HFDecimator))`
- `121`
- `assetData`
- `input clock domain`
- `id%d`
- `Util::addDictionaryEntry(ioEventReport, buf, ioEvents.audIOEvents[i].apWakeTSAbs)`
- `getDeviceProperty(AppleAOPAudioFirmware::ClientManagerProperties::kState, &mState, &sz)`
- `aop-audio-mca2`
- `RxADMAFifoUnderflow`
- `%s::%s() failed to transfer node %u, propId %u, value %u, ret = %d\n`
- `_publishStreamPropInRegistry`
- `LEAPClientManager:: Received Matching Notification - RegisterService!\n`
- `- LPMicInDevice::enableListening<%c%c%c%c>() -> 0x%x\n`
- `+ AppleAOPAudioLPMicInDevice::%s \n`
- `data`
- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNamePdmFrequency, &lowPowerConfig.pdmFrequency )`
- `channelCount`
- `+-Device::initForPM() -> 0x%x\n`
- ` AppleAOPAudioRingBuffer::Create() failed to allocate historical buffers\n`
- `AppleAOPAudioClientManager`
- `%s::%s('%c%c%c%c', 0x%x) complete, status 0x%x\n`
- `transferOptionalEdtProperty`
- `%s [hist] %d`
- `processDeviceTreeConfig()`
- `mController->setDeviceProperty(kAppleAOPAudioPDMDeviceId, AppleAOPPDM2Properties::kHFDecimatorCfgForHighPowerClock, hfDecCfg, sizeof(RTKitAudioDrivers::PDMStreamConfig::HFDecimator))`
- `theSubgroupKey`
- `theUserClient->mProvider`
- `+ AppleAOPAudioCodecRequestCompletionFunction %s:%d inParam1=%p mLPMicInDevice=%p\n`
- `%s:%s: Initializing`
- `getNamedProperty`
- `Enter %s::%s(provider: %p)\n`
- `channelControl`
- `Device::setDeviceProperty('%c%c%c%c', %d, %p %zu) failed, status: 0x%x\n`
- `_getChannelControl`
- `AppleBaseAudioController.cpp`
- `site.AppleAOPAudioPCMAssetManagerUserClient`
- `+-SawDevice::start(provider: %p) -> %d, err: 0x%x\n`
- `bytesPerSample`
- `function-get_lpms`
- `getNamedProperty(kAppleAOPLPMicEnabledChannels, &mChannelControl.enabledChannels)`
- `publishStreamProperties`
- `pointer \"%s\" is null, cannot continue, %s::%s(), line %d, status: 0x%x\n`
- `ret`
- `setInterruptAction`
- `en`
- `_getProperty(IOHandlerProperties::kSupportsHistoricalData, supportsHistoricalData)`
- `ListeningOnGesture %sabled\n`
- `AOPDevice.RegReadFailure`
- `%s::%s() msgType:%#x`
- `loadLeapFirmware`
- `-%s::%s\n`
- `decimatorConfig`
- `Util::addDictionaryEntry(theSubgroupReport, keyMCA2RxAShimOverrun, iMCA2RxAShimOverrun)`
- `inController`
- `mController->accessRegister(mIdentifier, &regDescriptor)`
- `mController->addDevice(id, this)`
- `!(AppleAOPAudioFirmware::AudioNodeStates::kRunning == mState)`
- `mCommandGate->runAction(action, reinterpret_cast<void *>(root), NULL, NULL, NULL)`
- `theDriver->_startHardware(*theDeviceID)`
- `mLPMicInDevice->startHardware(false)`
- `mInputHandler->_getBuffer(inBufferType, outBuffer)`
- `%s::%s has been interrupted commandSleepResult=%#x\n`
- `AppleAOPAudioCodecRequestCompletionFunction::initWithTargetDataAndSymbol mFunctionData->_phandle = %#x mFunctionData->_signature = %#x\n`
- `set`
- `supports-user-client`
- `mService->SetProperty(inProperty, inPayload, inPayloadSize)`
- `_hasListenOnGesture`
- `setDeviceProperty`
- `ClientMgr`
- `+-%s::%s(%d)\n`
- `AppleAOPAudioServiceBase`
- `initForPM(provider)`
- `- AmpManagerDevice::getStatusReport(%p)\n`
- `codecReplyHandlerGated`
- `%s: %c%c%c%c is AKCI for '%s'\n`
- `%s::%s('%c%c%c%c', %d) state: '%c%c%c%c'(%d)\n`
- `Util::addDictionaryEntry(theSubgroupReport, keyRxAFifoOverflow, rxStatus.RxAFifoOverflow)`
- `mLEAPNodeMatchingNotifier`
- `kReadBufferSize > 0`
- `AppleAOPAudioDeviceNode::_getIdentifersFromDeviceTree() failed to get property '%s' from registry\n`
- `mCommandGate->runAction(action, reinterpret_cast<void *>(inDeviceId), reinterpret_cast<void*>(inPropertyId), outPayload, reinterpret_cast<void *>(outPayloadSize))`
- `messageClients(kIOMessageServicePropertyChange)`
- `12111112122212121`
- `%s_%d`
- `+ PDM2Device::readPDM2Configuration\n`
- `populateHFDConfiguration(inProvider)`
- `setInterruptEnable`
- `TxBFifoUnderflow`
- `AppleAOPAudioCodecRequestCompletionFunction::%s(...) inParam1 cannot be nullptr\n`
- `%s: %c%c%c%c\n`
- `PDM2Device::%s invalid gain size for Trim Gain V1`
- `clientMemoryForType`
- `registerMemoryForZeroOut`
- `mCommandGate->runAction(action, reinterpret_cast<void *>(inDeviceId), reinterpret_cast<void*>(inPropertyId), const_cast<void*>(inPayload), reinterpret_cast<void *>(inPayloadSize))`
- `com.apple.private.aop-audio.user-access`
- `initWithRegistryEntry`
- `setChannelControl`
- `LPMicInDevice::%s send commandWakeup\n`
- `- UserClient::method_StartHardware() -> 0x%x\n`
- `initIOHandlerControl()`
- `error`
- `EnableHistoricalDataDeferredStart`
- `AppleAOPAudioSpeakerClientManager`
- `drift threshold 24MHz`
- `mService->getDeviceCount(devCount)`
- `+-%s::%s(%p %zu %lld %lld)\n`
- `site.AppleAOPAudioLEAP`
- `mController->getDeviceProperty(getIdentifier(), AppleAOPAudioFirmware::ButtonProperties::kHapticsEnableTimeoutPeriodUs, &enableTimeoutCount, &enableCountSz)`
- `codecReplyHandler`
- `site.AppleAOPAudioButtonHapticDevice`
- `%s::%s() service has no devices!?!\n`
- `1211112`
- `inDevice->getStatusReport(theReportDictionary)`
- `theUserClient`
- `AppleAOPAudioAmpStateFunction::%s(...) armFunctionData cannot be nullptr\n`
- `DisableTimeoutCount`
- `_waitTillAwake()`
- `+ %s::callPlatformFunction(%s, %d, %p, %p, %p, %p)\n`
- `setEnabledChannelMask`
- `AppleAOPAudioLPMicInDevice::%s startIO failed, ret=%#x\n`
- `PDM2Device:: Failed to get HFDec ratios`
- `UpdateSSHBWaveformAsset`
- `121111121222121211121212`
- `%s::%s() unknown audio packet type 0x%x\n`
- `mController->_getDeviceProperty(mIdentifier, IOHandlerProperties::kChannelControlProperty, &mChannelControl, &propertySize)`
- `%s::%s() failed to accessRegister, status: 0x%x\n`
- `theDriver->_waitTillAwake()`
- `+ LPMicInDevice::stop()\n`
- `handleRegisterAccess`
- `1211111212221212111212`
- `PDM2Device::getMicTuningParameters micCalibrationdB not present in EDT, default applied = (%d/100) \n`
- `site.AppleAOPAudioServiceBase`
- `AppleAOPAudioPCMAssetManagerUserClient`
- `%s:%s: Execute operation with code: '%c%c%c%c'`
- `sizeof(uint32_t) == ovrrrunSz`
- `_enableLPMicInput(isStarting)`
- `device-property-list`
- `PanicHandler::%s Registered(%u): %p [%llu]`
- `+ %s::%s('%c%c%c%c', %sable, 0x%x)\n`
- `+-%s::%s() {buffer size: %d bytes, frame size: %d bytes, zero ts wrap: %d frames}\n`
- `getDecimatorConfig(inProvider, kPropertyNameDecimatorConfigForHighPowerClks, decCfg)`
- `mController->setDeviceProperty(id, kReqIODirectionPId, newIODirection)`
- `%s::%s() unknown state value: '%c%c%c%c' (0x%x)\n`
- `+ %s::%s(%d, 0x%x)\n`
- `getDeviceTreeAudioProperty`
- `initInputBuffer`
- `!(0 == streamDesc.mChannelsPerFrame)`
- `invalidateState`
- `PDM2Device::%s invalid header 0x%x headerVal:0x%x\n`
- `supportedChannels`
- `_stopIO`
- `isValidReply`
- `stopIO`
- `entitlement`
- `PDM2Device:: Failed to get Dec length`
- `processDeviceTreeU32Entry() device tree property has unexpected size %lu bytes, expected %lu\n`
- `stop`
- `site.AppleAOPAudioPDM2Device`
- `requestIterator`
- `AppleAOPAudioLPMicInDevice::%s inEnable=%d. Notify the codec to turn on\n`
- `skipWaitingForFirmware`
- `inoutStatusDictionary->setObject(theSubgroupKey, theSubgroupReport)`
- `!(edtKeyName == nullptr)`
- `AppleAOPAudioDeviceController`
- `audioBitDepth`
- `mInputHandler`
- `%s::%s(%d, %p) -> 0x%x\n`
- `+ %s::%s(control id: 0x%x)\n`
- `%s::callPlatformFunction(%s, signature=%#x, AppleAOPAudioCodecRequestCompletionFunction::kSignature=%#x)\n`
- `setDeviceProperty(ClientManagerProperties::kCurrentPowerRequest, &req, sizeof(req))`
- `PDM2Device:: Failed to get Dec coeff`
- `parking-node-id`
- `dis`
- `nm`
- `- %s::%s(control id: 0x%x, value: 0x%x) -> 0x%x\n`
- `!(sizeof(SpuMCAPacket) > size)`
- `init`
- `mAOPStateChangeEventSource`
- `audioService`
- `mLPMicInDevice->handleMailboxData(pAudioPacket->payload, packetPayloadBytes - sizeof(AppleAOPAudioFirmware::SubPacket), aopMachAbsTimestamp, byteCount, spuTimestamp)`
- `writeRegister`
- `initFeatureAttributes`
- `AppleARMFunction::registerFunctionParent(inProvider, this)`
- `failed, status: 0x%x, %s::%s(), line %d: `
- `!(theUserClient->isInactive())`
- `AppleAOPAudioController`
- `+ %s::%s(%ld)\n`
- `_setProperty(AudioNodeProperties::kIORunning, true)`
- `%s::%s() no historical data to copy. (inByteCount: %llu, unpackedFrameSize %d, packedFrameSize %d)\n`
- `_getReporterForName`
- `%s::%s: Input payload {%d bytes} exceeds input buffer size {%ld bytes}! \n`
- `getNamedProperty(kAppleAOPLPMicVoiceTriggerChannels, &mChannelControl.voiceTriggerChannels)`
- `mController->setDeviceProperty(kAppleAOPAudioPDMDeviceId, AppleAOPPDM2Properties::kDecimatorCfgForHighPowerClock, &decCfg, sizeof(LowPowerPDM2Configuration::DecimatorConfig))`
- `_startHardware`
- `mLPMicInDevice->handleHistoricMailboxData(histPacket->payload, histPacket->size - sizeof(SpuMCAPacket), mService->sputime_to_absolutetime(histPacket->timestamp), histPacket->byteCount, histPacket->timestamp)`
- `AppleAOPAudioDeviceProvider`
- `!(inResource->assetIndex >= mMaxAssets)`
- `mService->getIOHandlerCount(ioHandlerCount)`
- `%s::%s() 0 bytes in historical data payload\n`
- `AppleBaseAudioController`
- `mService->attachDevice(inDeviceId, inClientId)`
- `LPMicInDevice::%s Going to sleep retries=%d \n`
- `AppleAOPAudioLPMicInDevice::%s enable=%d. isHardwareEnabled()=%d \n`
- `%s::%s(id %d, val 0x%x) failed, err: 0x%x\n`
- `aop-buttonoutput`
- `%s::%s() - _createIOReport() failed\n`
- `mIOReporter->configureReport(inChannels, inAction, outResult, inDestination)`
- `initCommandGate`
- `LPMicInDevice::%s Invalid reply received from Codec\n`
- `pSPUPacket`
- `121212222222222`
- `mController->getDeviceProperty(mIdentifier, AudioNodeProperties::kDownstreamFormatProperty, &streamDescription, &streamDescriptionSize)`
- `mDevices`
- `%s: found %d devices\n`
- `mAssetResourceData`
- `mController->getDeviceProperty(mParkingNodeIdentifier, LEAPParkingProperties::kParkingInfo, (void*)&parkingInfo, &propertySize)`
- `copyNamedAudioPropertyFromDeviceTree(kAppleAOPLPMicEnabledChannels, &mChannelControl.enabledChannels)`
- `getMicTuningParameters`
- `device-ui32-property-list`
- `ap-aop time delta abs`
- `isListeningClientEnabled(mListeningEnabled)`
- `createRequestPacket`
- `Util::addDictionaryEntry(theSubgroupReport, keyTxAFifoFrameError, txStatus.TxAFifoFrameError)`
- `mDeviceNodes`
- `inPayload`
- `AppleAOPAudioLPMicInDevice::%s() device tree property has unexpected size %lu bytes, expected %lu\n`
- `+ UserClient::method_StopHardware() -> 0x%x\n`
- `_initChannelControl`
- `%s{} detected %d inconsistent Hist byte seq.  Received an historical buffer after a live buffer\n`
- `sizeof(uint32_t) == enableCountSz`
- `thePowerStateOrdinal`
- `micCalibrationReversed`
- `%s::%s() node %c%c%c%c: failed to get kState (ret = %x)\n`
- `site.AppleAOPAudioDeviceController`
- `mChannelStatus.enabledChannels`
- `_setProperty`
- `%s::%s: Input historic payload {%d bytes} exceeds input buffer size {%ld bytes}, skipping first %d bytes!\n`
- `coefficients`
- `mCommandGate->runAction(_setControlValue, &inControlID, &inControlValue)`
- `getIdentity(val)`
- `_handleHistoricMailboxData`
- `_setChannelControl`
- `LPMicInDevice::%s codecReply->requestID (%lld) , mPendingConfigureCodecRequest.requestID (%lld)\n`
- `StateErrorCount`
- `input samples per sec`
- `processDeviceTreeU32Entry(keyDisableTimeoutUs, AppleAOPAudioFirmware::ButtonProperties::kHapticsDisableTimeoutPeriodUs)`
- `_detachDevice`
- `Util::addDictionaryEntry(ioEventReport, keyUsingNominalTimestamps, mIOHandlerConfig.mPreferNominalTimeStamping)`
- `LPMicInDevice::%s codecReply->replyState (%d) , mPendingConfigureCodecRequest.requestState (%d) codecReply->replyStatus=%#x\n`
- `preferNominalTimestamp`
- `%c%c%c%c.%s`
- `write`
- `getHFDecimatorConfig(inProvider, kPropertyNameHfdConfig, *hfDecCfg)`
- `aop-audio-clientmanager`
- `stopDevice(deviceNum, activeDirection)`
- `mDevice`
- `12111112122212121112122`
- `AppleAOPAudioLPMicInDevice.cpp`
- `mController->setDeviceProperty(inId, ClientManagerProperties::kCurrentPowerRequest, &req, sizeof(req))`
- `_publishStreamPropInRegistry()`
- `site.AppleAOPAudioFWdtAssetManagerDevice`
- `%s::%s() err: 0x%x\n`
- `true`
- `driver safety offset in frames`
- `RingBufferImpl::Create() was not supplied sane audio parameters bytesPerFrame %d, inBytesPerSample %d, ZeroTS %d, sampleRate %d, inHistoryChannels %08X\n`
- `AppleAOPAudioIOReporter`
- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNameBytesPerSample, &lowPowerConfig.bytesPerSample )`
- `hfdConfigForHighPowerClks`
- `- %s::%s('%c%c%c%c', 0x%llx, 0x%llx) -> 0x%x\n`
- `%s::%s(), unsupported input sample rate = %d\n`
- `%u`
- `site.AppleAOPAudioService`
- `Util::addDictionaryEntry(theSubgroupReport, keyTxAShimDrainFailure, txStatus.TxAShimDrainFailure)`
- `_setEnabledChannelMask`
- `theDeviceIterator`
- `getNamedProperty(kAppleAOPLPMicHistoryChannels, &mChannelControl.historyChannels)`
- `%s::%s Unexpected OSObject. Expect an OSData.`
- `resourceData`
- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNameMicSettleTimeMs, &lowPowerConfig.pdmMicTuningParams.micSettleTimeMs.value[0])`
- `mService->getVersion(version, sizeof(version))`
- `_getControlValue`
- `!((packetPayloadBytes < sizeof(AppleAOPAudioFirmware::SubPacket)))`
- `%s::%s() ByteOffset=%d, nodeID %c%c%c%c, propertyID %d edtKeyName:%s\n`
- `initCodecConfigurationHandle`
- `_enableListeningIOHandler(inControlValue)`
- `+-AppleAOPAudioDeviceProvider::start(provider: %p) -> err: 0x%x\n`
- `site.AppleBaseAudioController`
- `AppleAOPAudioCodecRequestCompletionFunction %s:%d mLPMicInDevice = %p result = %d \n`
- `TxBFifoFrameError`
- `registerData`
- `+ IOReporter::updateReport(%p, 0x%x, %p, %p, %p)\n`
- `site.AppleAOPAudioAmpManagerDevice`
- `mService->getDeviceProperty(inDeviceId, static_cast<AppleAOPAudioFirmware::PropertyID>(inPropertyId), outPayload, outPayloadSize)`
- `%s::%s() registerFunctionParent failed [ret: %#x]\n`
- ` ButtonHapticDevice::start() max assets: %d\n`
- `sizeof(uint32_t) == sz`
- `setDeviceActiveDirections(deviceNum, activeDirection)`
- `mController->getDeviceProperty(id, kCurIODirectionPId, &currentIODirection, &currentIODirectionSize)`
- `mController->setDeviceProperty(getIdentifier(), inNodePropertyNum, val)`
- `AppleAOPAudioAmpStateFunction::%s(...) failed. [errorCode: 0x%x]\n`
- `mController->getDeviceProperty(kClientListeningInput, ClientManagerProperties::kState, &nodeState, &szNodeState)`
- `+-SawDevice::init(%p, %p) -> %d\n`
- `getDeviceCount(val)`
- `AOPDevice.RegReadRetry`
- `ioMemory`
- `- LEAP::getStatusReport(%p) -> 0x%x\n`
- `disableTimeoutUs`
- `\"%s::%s(), should not be called without owning the workloop\" @%s:%d`
- `AppleAOPAudioCodecRequestCompletionFunction::%s(...) mFunctionData cannot be nullptr\n`
- `voiceTriggerChannels`
- `sizeof(txStatus) == txStatusSz`
- `drift detect`
- `+ %s::%s('%c%c%c%c', %p)\n`
- `_configureReport`
- `getControlValue`
- `theControlValue`
- `!(0 == streamDesc.mSampleFormat)`
- `inStatusDictionary`
- `drift event count`
- `kci-name`
- `device2Id`
- `+-UserClient::didTerminate(%p) {mProvider: %p} -> %s\n`
- `mChannelStatus.voiceTriggerChannels`
- `ioData`
- `mController->setDeviceProperty(kClientListenOnGesture, ListenOnGestureManagerProperties::kListeningOnGestureEnabledProp, &log, sizeof(log))`
- `mController->getDeviceProperty(kAppleAOPAudioPDMDeviceId, AppleAOPPDM2Properties::kDecimatorCfgForHighPowerClock, &decCfg, &decCfgSize)`
- `micSensitivitydB`
- `+ ButtonHapticDevice::UpdateSSHBWaveformAsset()\n`
- `Audio`
- `booleanResult`
- `site.AppleAOPAudioDeviceNode`
- `using nominal timestamps`
- `setActive`
- `site.AppleAOPAudioButtonOutputDevice`
- `AppleAOPAudioCodecRequestCompletionFunction::%s(...) inData cannot be nullptr\n`
- `mInputBuffer`
- `mController->messageClients(kIOMessageServicePropertyChange)`
- ` ButtonOutputDevice::getStatusReport() added %d entries\n`
- `%s::%s() - mIOReporter->addIOReporters() failed\n`
- `copyNamedAudioPropertyFromDeviceTree(kAppleAOPLPMicSupportedChannels, &mChannelControl.supportedChannels)`
- `- LPMicInDevice::%s ret=%#x\n`
- `mLPMicInDevice->getBuffer(inBufferType, outBuffer)`
- `externalClientRequestCallGated`
- `!(0 == count)`
- `LPMicInDevice::%s codecReply->replyState (%d) != mPendingConfigureCodecRequest.requestState (%d)\n`
- `%s:%s: Initialized: %s`
- `- PDM2Device::populateHFDConfiguraiton err: 0x%x\n`
- `- PDM2Device::getCoeffecients err: 0x%x\n`
- `rxFifoLoWatermark`
- `GetNumberOfSupportedAssets`
- `- %s::%s('%c%c%c%c', %sable, 0x%x) -> 0x%x\n`
- `%s::%s() invalid property size: %d\n`
- `- ButtonOutputDevice::getStatusReport(%p) -> 0x%x\n`
- `LPMicInDevice::%s woke up from sleep requestState=%d replyState=%d replyStatus=%d\n`
- `mService->PerformCommand(kAOPCommandCode, buf, packet->header.size, outPayload, outPayloadLength)`
- `TxBDMAFifoOverflow`
- `getStatusReport`
- `UserClient::clientClose() stopHardware\n`
- `theControlID`
- `setListeningOnGesture`
- `Oct 13 2026`
- `mLPMicInDevice->handleHardwareError(pAudioPacket)`
- `_setProperty(AudioNodeProperties::kPreWarmed, false)`
- `+ IOReporter::addIOReporters(%p)\n`
- `AppleAOPAudioIOReporter::addIOReporters() - reporter->addChannel(%llx, %s) returned 0x%x\n`
- `max drift time delta`
- `(nullptr == mCodecConfigurationHandle)`
- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNameClockSource, &lowPowerConfig.clockSource )`
- `- UserClient::clientMemoryForType(type: %d) -> 0x%x\n`
- `mController->getDeviceProperty(getIdentifier(), MCA2Properties::kMCA2RxAShimOverrun, &iMCA2RxAShimOverrun, &ovrrrunSz)`
- `_getBuffer`
- `getDeviceProperty(AppleAOPAudioFirmware::LPAudioInputManagerProperties::kChannelControlProperty, &mChannelControl, &ccSize)`
- `sendCodecRequest`
- `static IOReturn AppleAOPAudioPCMAssetManagerUserClient::UpdatePCMAudioAsset(OSObject *, void *, IOExternalMethodArguments *)`
- `%s::%s() inEnableListening=%d mListeningEnabled=%d\n`
- `%s kSpuPacketTypeServicePrivate not compatible with kPacketTypeAudio`
- `_initIOHandlerControl`
- `+ LEAP::getStatusReport(%p)\n`
- `theReportDictionary`
- `supportsHistoricalData`
- `1211111`
- `PDM2Device:: Failed to get HFDec Serv`
- `+- ButtonHapticDevice::start(provider: %p) -> %d, err: 0x%x\n`
- `resourceTypeEnum == AudioKernelClientInterfaceResourceType::PCM`
- `- %s::%s(control id: 0x%x) {outControlValue: 0x%x} -> 0x%x\n`
- `121111121222121211111111111111`
- `LPMicInDevice::%s mPendingConfigureCodecRequest.requestState=%d  mPendingConfigureCodecRequest.requestTime (%llx) mPendingConfigureCodecRequest.requestID=%lld mCodecRequestID=%lld\n`
- `site.AppleAOPAudioSawDevice`
- `121111121222121211121`
- `%s::%s() kSpuPacketTypeServicePrivate payload size %zu, less than expected %zu\n`
- `+-%s::%s(0x%x, %lld, %p, %zu, 0x%x) {%p, %d}\n`
- `getNamedProperty() device tree property has unexpected size %lu bytes, expected %lu\n`
- `23:20:27`
- `byte cnt`
- `slowClockSpeed`
- `publishBelow`
- `!(histBytes < sizeof(SpuMCAPacket))`
- `%s::%s() was not supplied with time functions\n`
- `audiodev-waits-for-leapfwload`
- `updateAsset(static_cast<void *>(aopInternalDataPacket), aopInternalDataPacketSize)`
- `this->_setChannelControl()`
- `+ LPMicInDevice::%s<%c%c%c%c>() inEnable=%d mHardwareEnabled=%d\n`
- `getDecimatorConfig(inProvider, kPropertyNameDecimatorConfig, lowPowerConfig.decimatorConfig)`
- `- %s::%s('%c%c%c%c', 0x%x) -> 0x%x\n`
- `method_SetControlValue`
- `Device::getDeviceProperty('%c%c%c%c', %d, %p %zu) failed, status: 0x%x\n`
- `- %s::%s() '%c%c%c%c', -> 0x%x\n`
- `+-DeviceNode::initWithRegistryEntry(from %p, provider %p), IOReturn: 0x%x\n`
- `accessRegister`
- `outNumberOfSupportedAssets`
- `micTurnOnTimeMs`
- `+ %s::%s() mLPAIEnabled=%d inEnableLPMic=%d\n`
- `_createIOHandlerDeprecated`
- `theDriver->_stopHardware(*theDeviceID)`
- `copyNamedAudioPropertyFromDeviceTree(kAppleAOPLPMicHistoryChannels, &mChannelControl.historyChannels)`
- `read`
- `latency`
- `RxBDMAFifoUnderflow`
- `site.AppleAOPAudioRingBuffer`
- `- LPMicInDevice::stop()\n`
- ` LPMicInDevice::%s\n`
- `isListeningClientEnabled`
- `Codec AppleAOPAudioCodecRequestCompletionFunction %s:%d mLPMicInDevice = %p\n`
- `fastClockSpeed`
- `method_GetControlValue`
- `mLPMicInDevice->startHardware(true)`
- `+ %s::%s() '%c%c%c%c'\n`
- `AppleAOPAudio Status`
- `- IOReporter::addIOReporters(%p) -> 0x%x\n`
- `copyNamedAudioPropertyFromDeviceTree`
- `packet`
- `+ UserClient::method_GetControlValue()\n`
- `Util::addDictionaryEntry(theSubgroupReport, keyRxBFifoFrameError, rxStatus.RxBFifoFrameError)`
- `param4`
- `readRegister`
- `mController->getDeviceProperty(getIdentifier(), AppleAOPAudioFirmware::ButtonProperties::kHapticsDisableTimeoutPeriodUs, &disableTimeoutCount, &disableCountSz)`
- `AppleAOPAudioLPMicInDevice::%s configureCodec failed for kAOPLPMicInDeviceListeningEnabled ret=%#x\n`
- `sizeof(nodeState) == szNodeState`
- `start`
- `performCommandWithAddress`
- `1211111212221212111212121122`
- `!((packetPayloadBytes > audioPacketSize))`
- `_setProperty(IOHandlerProperties::kListeningOnGestureEnabledProp, inEnable)`
- `subRequestList`
- `pdmcFrequency`
- `11111`
- `io event id`
- `getMicTuningParameters(inProvider, lowPowerConfig.pdmMicTuningParams)`
- `PDM2Device::%s Unable to read the header\n`
- `method_StartHardware`
- `1111`
- `micCalibrationdB`
- `getTrimGain`
- `%s: %c%c%c%c, restype: %c%c%c%c, id: %04hx, size: %hu, start: 0x%02hhx%02hhx, end: 0x%02hhx%02hhx, pre: %hu, post: %hu, loop: %u\n`
- `AppleAOPAudioLPMicInDevice::%s inEnable=%d. Notify the codec to turn off \n`
- `%s::%s('%c%c%c%c', 0x%x) state: '%c%c%c%c'(%d)\n`
- `mInputBuffer->GetDataBufferDescriptor()`
- `AppleAOPAudioCodecRequestCompletionFunction::%s(...) failed. [result: 0x%x]\n`
- `disable-accessory-firmware`
- `inoutStatusDictionary->setObject(theioEventKey, ioEventReport)`
- `waitForCodecReply`
- `B24@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{IONotifier=^^?i}16`
- `Util::addDictionaryEntry(ioEventReport, buf, ioEvents.audIOEvents[i].IOHistStatus.HistStat[ii])`
- `_hasListenOnGesture(hasListenOnGesture)`
- `theDeviceID`
- `mService->setDeviceProperty(inDeviceId, static_cast<AppleAOPAudioFirmware::PropertyID>(inPropertyId), inPayload, inPayloadSize)`
- `AppleAOPAudioService::getNamedProperty(inService, kPropertyNameMicSettleTimeMs, &micParams.micSettleTimeMs.value[0])`
- `status`
- `transferOptionalEdtProperty(\"device-ui32-property-list\")`
- `mController->_getDeviceProperty(mIdentifier, inPropertyId, &propertyValue, &propertySize)`
- `warning`
- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNameChannelPhaseSelect, &lowPowerConfig.channelPhaseSelect, sizeof(lowPowerConfig.channelPhaseSelect) )`
- `AppleAOPAudioIOReporter::addIOReporters() - IOReportLegend::addReporterLegend(group: %s) returned 0x%x\n`
- `Util::addDictionaryEntry(theSubgroupReport, keyHapticsDisableTimeoutCount, disableTimeoutCount)`
- `_enableLPMicInput`
- `LEAPClientManager:: notifier didn't match (%p) (%p)!\n`
- `mObjectMap`
- ` LPMicInDevice::initCodecConfigurationHandle registerFunctionParent\n`
- `notice`
- `AppleAOPAudioService::getNamedProperty(inService, kPropertyNameMicSensitivitydB, &micSensitivitydB)`
- `+ %s::%s('%c%c%c%c', %p, %p)\n`
- `!(pSPUPacket->size > size)`
- `com.apple.private.aea.haptics.user-access`
- `_attachDevice`
- `AppleAOPAudioAmpStateFunction::%s(...) inData cannot be nullptr\n`
- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNameMicTurnOnTimeMs, &lowPowerConfig.pdmMicTuningParams.micTurnOnTimeMs.value[0])`
- `filterLengths`
- `registerMatchingNotification`
- `configureCodec`
- `[%s](%s) %s%s`
- `+-PDM2Device::start(provider: %p) -> %d, err: 0x%x\n`
- `audioService->start(inProvider)`
- `mInputBuffer->GetStatusBufferDescriptor()`
- `listening on gesture supported`
- `mChannelIDMap`
- `AppleAOPAudioAssetManagerDevice`
- `condition \"%s\" failed, %s::%s() line %d, status: 0x%x\n`
- `expression \"%s\" failed, %s::%s(), line %d, status: 0x%x\n`
- `hfDecCfg`
- `(entitlement = copyClientEntitlement(inOwningTask, kAppleAOPAudioUserClientEntitlement))`
- `theDriver`
- `Util::addDictionaryEntry(theSubgroupReport, keyHapticsEnableTimeoutCount, enableTimeoutCount)`
- `%s::%s THREAD_TIMED_OUT retries=%d\n`
- `populateHFDConfiguration`
- `PDM2Device::getCoeffecientsForHFD() failed to get 'coefficients' property, error: 0x%x\n`
- `23:20:29`
- ` %s::%s() attach and start %p (%s), class is %s\n`
- `!(0 == inPayloadBytes)`
- `AppleAOPAudioAmpStateFunction::%s(...) inParam1 cannot be nullptr\n`
- `clockDomain`
- `site.AppleAOPAudioHapticLEAP`
- `AppleAOPAudioIOHandler`
- `super::start(inProvider)`
- `%s::%s(%d) hardware now %sabled\n`
- `messageClients`
- `- AppleAOPAudioLPMicInDevice::%s \n`
- `_getProperty(AudioNodeProperties::kState, state, true)`
- `mWorkLoop`
- `%s::%s() failed to %s register (@0x%x): 0x%x\n`
- `StateChange`
- `failure`
- `theDriver->_setControlValue(*theControlID, *theControlValue)`
- `+ PDM2Device::populateHFDConfiguraiton\n`
- `+-%s::%s(provider: %p) -> err: 0x%x\n`
- `getInterruptStatus`
- `AppleAOPAudioPCMAssetManagerDevice`
- `+ UserClient::method_Open()\n`
- `TxADMAFifoOverflow`
- `getDeviceProperty(AppleAOPAudioAssetManagerProperties::kNumberOfSupportedAssets, static_cast<void*>(&mMaximumNumberOfSupportedAssets), &dataSize)`
- `initFeatureAttributes(mController->getListenOnGestureSupported())`
- `%s::%s<%c%c%c%c>(): ClkDomain set to <%c%c%c%c>\n`
- `+ AppleAOPAudioLPMicInDevice::%s inEnable=%d. mListeningEnabled=%d\n`
- `mService->RegisterCallback(AppleAOPAudioController::sServiceCallback, this)`
- `site.AppleAudioSequenceOperation`
- `payload`
- `!((*inoutPropertyLength) < property->getLength())`
- `_setHWInStrmSRate`
- `AppleAOPButtonHapticsServiceUserClient`
- `site.AppleAOPAudioLPMicInDevice`
- `LPMicInDevice::%s COdec reply status was not OK, returned %#x\n`
- `AppleAOPAudioCodecRequestCompletionFunction::%s(...) failed.\n`
- `mService->registerRead(inDeviceId, inDescriptor->mAddressWidth, inDescriptor->mAddress, inDescriptor->mDataWidth, &dataSize, inDescriptor->mOutData, inDescriptor->optionBits, inDescriptor->qualifier)`
- `- %s::callPlatformFunction(%s, %d, %p, %p, %p, %p) result=%#x\n`
- `%s::%s(<0x%x 0x%x 0x%x 0x%x>) failed, status: 0x%x\n`
- `_initIOHandlerControl()`
- `+-RingBuffer::Create() {buffer size: %d bytes, sample size: %d bytes, zero ts wrap: %d frames}\n`
- `PDM2Device::%s invalid checkSum(Original:0x%x Calculated:0x%x)\n`
- `outNum`
- `AOPDevice.RegWriteVerifFailure`
- `spu io time raw`
- ` LPMicInDevice::%s ret=%#x retries=%d\n`
- `resourceID`
- `%s::%s(%d) listening now %sabled\n`
- `%s::%s() unknown control value '%c%c%c%c' (0x%x)\n`
- `theStatusDictionaryIterator`
- `%s:%s: Failed parsing operation '%c%c%c%c'`
- `- %s::%s('%c%c%c%c', %d) -> 0x%x\n`
- `RxAFifoOverflow`
- `TxBShimDrainFailure`
- `sizeof(uint32_t*) == data->getLength()`
- `initWithTargetDataAndSymbol`
- ` LPMicInDevice::initCodecConfigurationHandle mCodecConfigurationHandle=%p\n`
- `AppleAOPAudioLPMicInDevice::%s inEnable=%d. notifyCodecOfFailure=%d\n`
- `AOPAudioPCMAssetMgrUC`
- `clockSource`
- `- ButtonHapticDevice::UpdateSSHBWaveformAsset(asset #%d) -> 0x%x\n`
- `mService`
- `%s::%s() inEnableListening=%d mListeningEnabled=%d ret=%#x\n`
- `_aopStateChangeEvent`
- `IO '%c%c%c%c' %s`
- `mController->setDeviceProperty(getIdentifier(static_cast<uint32_t>(LEAPIdentifierIndex::LEAP)), AppleAOPAudioFirmware::LEAPProperties::kFirmwareReset, &kReset, sizeof(kReset))`
- `theBufferType`
- `enableHPClientMngr`
- `productSpecificExternalClientRequestCallGated`
- `getProperty`
- `initWithTask`
- `mController->getDeviceProperty(getIdentifier(), MCA2Properties::kMCARxStatus, &rxStatus, &rxStatusSz)`
- `_setProperty(AudioNodeProperties::kPreWarmed, true)`
- `+ %s::%s<%c%c%c%c>()\n`
- `%s::%s(%p, %zu bytes, ts %lld, byte count %lld)\n`
- `Util::addDictionaryEntry(theSubgroupReport, keyTxBFifoUnderflow, txStatus.TxBFifoUnderflow)`
- `getState`
- `+ LPMicInDevice::configureCodec mCodecRequestID=%lld inReqState=%d isCodecConfigurationSupported()=%d\n`
- `AppleAOPAudioCodecRequestCompletionFunction`
- `%s aopInternalDataPacket cannot be nullptr`
- `+ PDM2Device::getMicTuningParameters\n`
- `sizeof(currentIODirection) == currentIODirectionSize`
- `zero timestamp wrap frames`
- `site.AppleAOPAudioRingBufferImpl`
- `+ %s::%s('%c%c%c%c', %d)\n`
- `setDeviceActiveDirections(deviceNum, direction)`
- `audioService->init()`
- `!(AudioNodeStates::kRunning == mState)`
- `_copyData`
- `site.AppleAOPButtonHapticsServiceUserClient`
- `getDeviceProperty(kStreamFormatPropertyId, &streamDesc, &szStreamDesc)`
- `- %s::%s('%c%c%c%c', %p) {status: 0x%llx} -> 0x%x\n`
- `TxAFifoUnderflow`
- `22221112222122222222222221`
- `+-%s::%s() -> 0x%x\n`
- `getDeviceProperty(AppleAOPAudioFirmware::LPAudioInputManagerProperties::kLPAISupportsHistoricalData, &histDataSupported, &szHistDataSupported)`
- `- %s::%s<%c%c%c%c>() -> 0x%x\n`
- `12111112122212121112112`
- `Util::addDictionaryEntry(theSubgroupReport, keyTxBIOTimeout, txStatus.TxBIOTimeout)`
- `site.AppleAOPAudioDevice`
- `mController->setDeviceProperty(mIdentifier, ClientManagerProperties::kCurrentPowerRequest, &req, sizeof(req))`
- `AppleAOPAudioButtonOutputDevice`
- `Util::addDictionaryEntry(ioEventReport, keyControllerStartTimeAbs, mDriftDetectInfo.controllerStartTimeAbs)`
- `AppleAOPAudioLPMicInDevice::%s could not find registry entry at path \"%s\"`
- `%s::%s(), supported sample rate(s) = %d\n`
- `AppleAOPAudioAmpStateFunction`
- `AppleAOPAudioLPMicInDevice::%s configureCodec for kAOPLPMicInDeviceStartIO failed ret=%#x\n`
- `AppleAOPAudioLPMicInDevice::%s enable=%d. Request the codec to disable listening\n`
- `!(0 == kHistFramesPerMs)`
- `+-SawDevice::probe(%p, %d) -> %p\n`
- `TxBOutputPadFailure`
- `- AppleAOPAudioCodecRequestCompletionFunction %s:%d inParam1=%p mLPMicInDevice=%p result=%#x\n`
- `processResourceUpdateRequest(inRequest)`
- `%s unexpected mBufferSize(%u) (max:%zd)`
- `%s::%s() super::start() failed [kIOReturn: 0x%x, result: %d]\n`
- `setAmpState`
- `+-%s::%s('%c%c%c%c', 0x%x) -> 0x%x\n`
- `hasMicTuningConfig`
- `startStopDevice`
- `channelNameBuffer`
- `_createIOReport(theStatusReport)`
- `mService->registerWrite(inDeviceId, inDescriptor->mAddressWidth, inDescriptor->mAddress, inDescriptor->mDataWidth, inDescriptor->mDataSize, inDescriptor->mInData, inDescriptor->optionBits, inDescriptor->qualifier)`
- `+ LPMicInDevice::enableListening<%c%c%c%c>()\n`
- `AppleAOPAudioButtonHapticDevice`
- `_handleMailboxData`
- `PanicHandler::%s MemBuffer (%p) not found!`
- `- %s::%s() mLPAIEnabled=%d inEnableLPMic=%d ret=%#x\n`
- `_getIdentifersFromDeviceTree`
- `IODeviceTree:/product/audio`
- `- AppleAOPAudioLPMicInDevice::%s enable=%d. mListeningEnabled=%d ret=%#x\n`
- `channelPolaritySelect`
- `!((histPacket->size < sizeof(SpuMCAPacket)))`
- `HardwareError`
- `setChannelControl(mChannelControl)`
- `LPMicInDevice::initChannelControl(<0x%x 0x%x 0x%x 0x%x>), status: 0x%x\n`
- `12111`
- ` %s::%s() added %d entries\n`
- `mInputHandler->_stopIO()`
- `processDeviceTreeU32Entry() failed to read property %s from device tree for node '%c%c%c%c', err: 0x%x\n`
- `detachDevice`
- `site.AppleAOPAudioHallDevice`
- `stopDevice`
- `+-MCA2Device::start(provider: %p) -> %d, err: 0x%x\n`
- `%s::%s(inPropertyID=%d, inAmpState=%d) failed [errorCode: 0x%x]\n`
- `setDeviceProperty(AppleAOPAudioFirmware::LPAudioInputManagerProperties::kChannelControlProperty, &cc, sizeof(cc))`
- `AOPAudio`
- `transferEdtProperty()`
- `setDevicePowerState`
- `_startIO`
- `pAudioPayload`
- `enableTimeoutUs`
- `+ UserClient::method_StartHardware()\n`
- `mCommandGate`
- `handleStart(provider)`
- `AppleAOPAudioAmpManagerDevice`
- `enableListeningClientManager`
- `startDevice`
- `sServiceCallback`
- `%s::%s('%c%c%c%c')  unexpected device state: '%c%c%c%c'(%d)\n`
- `121111121222121212111111121112`
- `+ %s::%s(%p)\n`
- `readPDM2Configuration`
- `_stopHardware`
- `resourceTypeObj`
- `+-PDM2Device::attach(%p) -> %d\n`
- `site.AppleAOPAudioPCMAssetManagerDevice`
- `method_Close`
- `mLPMicInDevice->enableListening(inEnableListening)`
- `No input node '%c%c%c%c' found, continuing\n`
- `mController->_attachDevice(mIdentifier, reinterpret_cast<uint64_t>(this))`
- `%s::%s() aborting attempt to wait till driver is awake, commandSleep returned 0x%x\n`
- `Util::addDictionaryEntry(ioEventReport, buf, mDriftDetectInfo.firstDriftTime.AudIOStat[i])`
- `readPDM2Configuration( inProvider )`
- `AppleAOPAudioDeviceProvider::setDevicePowerState() err: 0x%x\n`
- `controller start time abs`
- `getNamedProperty(kAppleAOPLPMicSupportedChannels, &mChannelControl.supportedChannels)`
- `- %s::%s(%p) -> 0x%x\n`
- `notifySystemShutdown`
- `%s::%s() Listening %sabled\n`
- `%s::%s Incorrect data length. Expected a uint32_t`
- `audioSampleRate`
- `Util::addDictionaryEntry(theSubgroupReport, keyRxADMAFifoUnderflow, rxStatus.RxADMAFifoUnderflow)`
- `mController->registerLPMicInDeviceDeprecated(this)`
- `addIOReporters`
- `aop-audio-lp-mic-in`
- `copyNamedAudioPropertyFromDeviceTree(kAppleAOPLPMicVoiceTriggerChannels, &mChannelControl.voiceTriggerChannels)`
- `AppleAOPAudioSawDevice`
- `sizeof(rxStatus) == rxStatusSz`
- `mIOReporter->addIOReporters(theReportDictionary)`
- `- UserClient::method_GetControlValue() -> 0x%x\n`
- `_enableInputIOHandler`
- `_enableInputIOHandler(isStarting)`
- `AppleAOPAudioRingBufferImpl`
- `%s::%s() super::start() failed\n`
- `firmwareData`
- `historicDataSupported`
- `AppleAOPAudioLPMicInDevice::%s enableListeningClientManager failed, ret=%#x\n`
- `- PDM2Device::readPDM2Configuration err: 0x%x\n`
- `inoutStatusDictionary`
- `mIOReporter`
- `%s::%s('%c%c%c%c', 0x%x) -> 0x%x\n`
- `handleMailboxData`
- `%s::%s() unable to set the result`
- `attachDevice`
- `+-SawDevice::attach(%p) -> %d\n`
- `site.AppleAOPAudioClientManager`
- `method_Open`
- `_systemWillShutdownGated`
- `channels per frame`
- `outPropertyValue`
- `false`
- `frames per packet`
- `_getProperty`
- `inGroupName`
- `theDriver->_setPowerState(*thePowerStateOrdinal)`
- `ap wake time abs`
- `AppleAOPAudioLPMicInDevice::%s configureCodec ret=%#x\n`
- `_setListeningOnGesture`
- `AOPDevice.RegWriteFailure`
- `AOPDevice.RegReadCommProtocolFailure`
- `!(0 == streamDesc.mBytesPerChannel)`
- `LPMicInDevice::%s codecReply->replyTime (%llx) , mPendingConfigureCodecRequest.requestTime (%llx)\n`
