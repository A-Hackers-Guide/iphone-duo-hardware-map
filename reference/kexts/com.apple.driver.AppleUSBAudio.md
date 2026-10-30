# `com.apple.driver.AppleUSBAudio`

- Name: AppleUSBAudio
- Version: `910.2`
- UUID: `8D022D2F-9610-3253-B0D4-6E8F22F5583B`
- Source version: `910.2.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleAudioClockLibs`](com.apple.driver.AppleAudioClockLibs.md) 1.0, [`com.apple.driver.usb.AppleUSBHostCompositeDevice`](com.apple.driver.usb.AppleUSBHostCompositeDevice.md) 1.1, [`com.apple.iokit.IOAudio2Family`](com.apple.iokit.IOAudio2Family.md) 1.0, [`com.apple.iokit.IOUSBDeviceFamily`](com.apple.iokit.IOUSBDeviceFamily.md) 2.0.0, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.0.1, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 14.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 14.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 20.4.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (10) [KC]

### Adapter HID
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBAudio`
- `IOProviderClass`: `IOHIDDevice`
- `IOProviderMergeProperties`:
  - `kUSBHIDDeviceIdlePolicy`: `2000`
- `ProductID`: `4362`
- `Transport`: `USB`
- `VendorID`: `1452`

### AppleUSBADCAudioDevice
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBAudio`
- `IOClass`: `AppleUSBADCAudioDevice`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBAudio`
- `IOProviderClass`: `AppleUSBADCAudioNub`

### AppleUSBAudioComposite
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBAudio`
- `IOClass`: `AppleUSBAudioComposite`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBAudio`
- `IOProviderClass`: `IOUSBHostDevice`
- `bDeviceClass`: `0`
- `bDeviceSubClass`: `0`

### AppleUSBAudioControl
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBAudio`
- `IOClass`: `AppleUSBAudioDevice`
- `IOMatchDefer`: `True`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBAudio`
- `IOProviderClass`: `IOUSBHostInterface`
- `bInterfaceClass`: `1`
- `bInterfaceSubClass`: `1`

### AppleUSBAudioControlNub
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBAudio`
- `IOClass`: `AppleUSBAudioControlNub`
- `IOMatchDefer`: `True`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBAudio`
- `IOProviderClass`: `IOUSBHostInterface`
- `bInterfaceClass`: `1`
- `bInterfaceSubClass`: `1`

### AppleUSBAudioStream
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBAudio`
- `IOClass`: `AppleUSBAudioStreamNode`
- `IOMatchDefer`: `True`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBAudio`
- `IOProviderClass`: `IOUSBHostInterface`
- `bInterfaceClass`: `1`
- `bInterfaceSubClass`: `2`

### AppleUSBDeviceAudioDevice
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBAudio`
- `IOClass`: `AppleUSBDeviceAudioDevice`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBAudio`
- `IOProviderClass`: `AppleUSBDeviceAudioNub`

### AppleUSBTrinityAudioControl
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBAudio`
- `IOClass`: `AppleUSBTrinityAudioDevice`
- `IOMatchDefer`: `True`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBAudio`
- `IOProviderClass`: `IOUSBHostInterface`
- `bConfigurationValue`: `1`
- `bInterfaceNumber`: `0`
- `idProduct`: `4353`
- `idVendor`: `1452`

### InterfaceAssociationClass
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBAudio`
- `IOClass`: `AppleUSBAudioComposite`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBAudio`
- `IOProviderClass`: `IOUSBHostDevice`
- `bDeviceClass`: `239`
- `bDeviceProtocol`: `1`
- `bDeviceSubClass`: `2`

### InterfaceDriver
- `CFBundleIdentifier`: `com.apple.kpi.iokit`
- `IOClass`: `IOService`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBAudio`
- `IOProviderClass`: `IOUSBHostInterface`
- `bConfigurationValue`: `1`
- `bInterfaceNumber`: `3`
- `idProduct`: `4359`
- `idVendor`: `1452`


## C++ classes (40) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AUAADC3ClassSpecificDescriptorFetcher` | 0x18 |  |
| `AUAASEndpointDictionary` | 0x28 | AUAEndpointDictionary → AppleUSBAudioDictionary → OSDictionary → OSCollection |
| `AUAClockMultiplierDictionary` | 0x28 | AUAUnitDictionary → AppleUSBAudioDictionary → OSDictionary → OSCollection |
| `AUAClockSelectorDictionary` | 0x28 | AUAUnitDictionary → AppleUSBAudioDictionary → OSDictionary → OSCollection |
| `AUAClockSourceDictionary` | 0x28 | AUAUnitDictionary → AppleUSBAudioDictionary → OSDictionary → OSCollection |
| `AUAConfigurationDictionary` | 0x28 | AppleUSBAudioDictionary → OSDictionary → OSCollection |
| `AUAControlDictionary` | 0x30 | AppleUSBAudioDictionary → OSDictionary → OSCollection |
| `AUAEffectUnitDictionary` | 0x28 | AUAUnitDictionary → AppleUSBAudioDictionary → OSDictionary → OSCollection |
| `AUAEndpointDictionary` | 0x28 | AppleUSBAudioDictionary → OSDictionary → OSCollection |
| `AUAExtensionUnitDictionary` | 0x28 | AUAUnitDictionary → AppleUSBAudioDictionary → OSDictionary → OSCollection |
| `AUAFeatureUnitDictionary` | 0x28 | AUAUnitDictionary → AppleUSBAudioDictionary → OSDictionary → OSCollection |
| `AUAInputTerminalDictionary` | 0x30 | AUAUnitDictionary → AppleUSBAudioDictionary → OSDictionary → OSCollection |
| `AUAMixerUnitDictionary` | 0x28 | AUAUnitDictionary → AppleUSBAudioDictionary → OSDictionary → OSCollection |
| `AUAOutputTerminalDictionary` | 0x30 | AUAUnitDictionary → AppleUSBAudioDictionary → OSDictionary → OSCollection |
| `AUAProcessingUnitDictionary` | 0x28 | AUAUnitDictionary → AppleUSBAudioDictionary → OSDictionary → OSCollection |
| `AUASelectorUnitDictionary` | 0x28 | AUAUnitDictionary → AppleUSBAudioDictionary → OSDictionary → OSCollection |
| `AUAStreamDictionary` | 0x28 | AppleUSBAudioDictionary → OSDictionary → OSCollection |
| `AUAUnitDictionary` | 0x28 | AppleUSBAudioDictionary → OSDictionary → OSCollection |
| `AppleUSBADCAudioDevice` | 0x1f8 | AppleUSBAudioDevice → Audio2Device → IOService → IORegistryEntry |
| `AppleUSBADCAudioNubBase` | 0x88 | IOService → IORegistryEntry |
| `AppleUSBAudioComposite` | 0xc0 | AppleUSBHostCompositeDevice → IOService → IORegistryEntry |
| `AppleUSBAudioControlInterface` | 0x40 |  |
| `AppleUSBAudioControlNub` | 0x88 | IOService → IORegistryEntry |
| `AppleUSBAudioDevice` | 0x1e8 | Audio2Device → IOService → IORegistryEntry |
| `AppleUSBAudioDictionary` | 0x28 | OSDictionary → OSCollection |
| `AppleUSBAudioEngine` | 0x40320 | Audio2Engine → IOAudio2Device → IOService → IORegistryEntry |
| `AppleUSBAudioInterruptPipe` | 0x28 |  |
| `AppleUSBAudioIsocFrameList` | 0x30 |  |
| `AppleUSBAudioIsocPipe` | 0x30 |  |
| `AppleUSBAudioStream` | 0x4e0 | Audio2Stream → IOService → IORegistryEntry |
| `AppleUSBAudioStreamNode` | 0x88 | IOService → IORegistryEntry |
| `AppleUSBDeviceAudioDevice` | 0x1f0 | AppleUSBAudioDevice → Audio2Device → IOService → IORegistryEntry |
| `AppleUSBDeviceAudioNubBase` | 0x88 | IOService → IORegistryEntry |
| `Audio2Control` | 0x40 |  |
| `Audio2Device` | 0xb0 | IOService → IORegistryEntry |
| `Audio2Engine` | 0x178 | IOAudio2Device → IOService → IORegistryEntry |
| `Audio2LevelControl` | 0x50 | Audio2Control |
| `Audio2SelectorControl` | 0x48 | Audio2Control |
| `Audio2Stream` | 0x110 | IOService → IORegistryEntry |
| `Audio2ToggleControl` | 0x40 | Audio2Control |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00004030 off=0x008cb550-0x008cf580 addr=0xfffffe00078cf550-0xfffffe00078d3580 r--/r--   __TEXT            
	sz=0x0000332b off=0x008cbc18-0x008cef43 addr=0xfffffe00078cfc18-0xfffffe00078d2f43               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000630 off=0x008cef50-0x008cf580 addr=0xfffffe00078d2f50-0xfffffe00078d3580               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00071020 off=0x02a9ff80-0x02b10fa0 addr=0xfffffe0009aa3f80-0xfffffe0009b14fa0 r-x/r-x   __TEXT_EXEC       
	sz=0x000707f0 off=0x02a9ff80-0x02b10770 addr=0xfffffe0009aa3f80-0xfffffe0009b14770          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000830 off=0x02b10770-0x02b10fa0 addr=0xfffffe0009b14770-0xfffffe0009b14fa0          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000718 off=0x049d00e8-0x049d0800 addr=0xfffffe000b9d40e8-0xfffffe000b9d4800 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x049d00e8-0x049d01ac addr=0xfffffe000b9d40e8-0xfffffe000b9d41ac               __DATA.__data             
	sz=0x00000650 off=0x00000000-0x00000650 addr=0xfffffe000b9d41b0-0xfffffe000b9d4800               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x0000b5c8 off=0x01295bb8-0x012a1180 addr=0xfffffe0008299bb8-0xfffffe00082a5180 rw-/rw-   __DATA_CONST      
	sz=0x00000088 off=0x01295bb8-0x01295c40 addr=0xfffffe0008299bb8-0xfffffe0008299c40         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000088 off=0x01295c40-0x01295cc8 addr=0xfffffe0008299c40-0xfffffe0008299cc8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00009c50 off=0x01295cc8-0x0129f918 addr=0xfffffe0008299cc8-0xfffffe00082a3918         __DATA_CONST.__const            
	sz=0x00000a00 off=0x0129f918-0x012a0318 addr=0xfffffe00082a3918-0xfffffe00082a4318         __DATA_CONST.__kalloc_type      
	sz=0x00000960 off=0x012a0318-0x012a0c78 addr=0xfffffe00082a4318-0xfffffe00082a4c78         __DATA_CONST.__kalloc_var       
	sz=0x00000418 off=0x012a0c78-0x012a1090 addr=0xfffffe00082a4c78-0xfffffe00082a5090         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000e8 off=0x012a1090-0x012a1178 addr=0xfffffe00082a5090-0xfffffe00082a5178         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x012a1178-0x012a1180 addr=0xfffffe00082a5178-0xfffffe00082a5180         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 291 at 0x04aeb004
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     8D022D2F-9610-3253-B0D4-6E8F22F5583B
008: LC_SOURCE_VERSION           910.2.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab69d8 size=0x8e0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleUSBAudio`
- `CFBundleGetInfoString`: `AppleUSBAudio 910.2, Copyright © 2000-2024 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBAudio`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUSBAudio`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `910.2`
- `CFBundleSignature`: `aaud`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `910.2`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `AppleUSBAudio 910.2, Copyright © 2000-2024 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Safe Boot`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
  - `2`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleUSBAudio.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896577200`
- `_PrelinkExecutableRelativePath`: `AppleUSBAudio`
- `_PrelinkExecutableSize`: `527664`
- `_PrelinkExecutableSourceAddr`: `-2198896577200`
- `_PrelinkKmodInfo`: `-2198828400408`

## Strings (492) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AUAUnitDictionary`
- `121111121222121211121212111111211112111121211121211212111222212`
- `ControlInterfaceNumber`
- `UnitID`
- `AssocTerminal`
- `sound isolating`
- `site.AppleUSBADCAudioDevice`
- `USB Sound assertion in %s at line %d\n`
- `EffectUnits`
- `AUAEffectUnitDictionary`
- `output latency`
- `1211121122`
- `/Library/Caches/com.apple.xbs/B5FDCB36-D853-46D3-9503-186FD0AD7D5C/TemporaryDirectory.BTvKfA/Sources/AppleUSBAudio/KEXT/AppleUSBAudioIsocPipe.cpp`
- `/Library/Caches/com.apple.xbs/B5FDCB36-D853-46D3-9503-186FD0AD7D5C/TemporaryDirectory.BTvKfA/Sources/AppleUSBAudio/KEXT/AppleUSBAudioDevice.cpp`
- `TerminalType`
- `HasMaxPacketsOnly`
- `InterfaceProtocol`
- `passthruvolcontrols`
- `Low Frequency Effects Speaker`
- `Down Line Phone`
- `Resetting engine due to error returned in Read Handler`
- `:`
- `Streams wrapping on different frames (off by 2)`
- `Invalid length`
- `LockDelayUnits`
- `third party`
- `AppleUSBAudioInterruptPipe`
- `AppleUSBAudioStreamNode`
- `121`
- `USBDeviceFunction`
- `Telephone`
- `FormatTag`
- `Front Left of Center`
- `12111211`
- `ControlsArray`
- `ChannelConfig`
- `Embedded Multitrack Recorder`
- `121212`
- `USB Vendor Name`
- ` Failed to change sample rate`
- `custom property info`
- `Internal Fixed Clock`
- `input safety offset`
- `1`
- `WARNING: AppleUSBAudio has detected that a connected USB audio device is sending too much audio data.\n`
- `site.UInt16`
- `InputTerminals`
- `NumSampleRates`
- `\"AppleUSBAudioStream::WatchdogTimer - no callbacks for a while\\n\" @%s:%d`
- `USB streaming`
- `/Library/Caches/com.apple.xbs/B5FDCB36-D853-46D3-9503-186FD0AD7D5C/TemporaryDirectory.BTvKfA/Sources/AppleUSBAudio/KEXT/AppleUSBAudioEngine.cpp`
- `model UID`
- `%d`
- `Resetting engine due to immediate error during prime`
- `Output Undefined`
- `121111121222121211211211`
- `NumEndpoints`
- `usbDevice:%s`
- `voice activity detect enable`
- `StreamDictionaries`
- `site.AUAProcessingUnitDictionary`
- `Device`
- `iOS USB Audio 2.0 Device`
- `Embedded Analog Tape`
- `output streams`
- `site.IOGeneralMemoryDescriptor *`
- `\"AppleUSBAudioStream::processWrite - general error on write\\n\" @%s:%d`
- `IOAudioEngineIsHidden`
- `passthrupathsarray`
- `External 1394 DA Stream`
- `site.AppleUSBAudioComposite`
- `site.AppleUSBADCAudioNubBase`
- `Back Left of Center`
- `setting externalSecureMute to %d`
- `AppleUSBDeviceAudioNubBase`
- `earpiece design`
- `Bad List Descriptor`
- `AppleUSBAudioControlNub`
- `driver tag`
- `usbaudio_startupdelay`
- `inputmutecontrols`
- `Desktop Speaker`
- `AUAStreamDictionary`
- `ProcessType`
- `Attributes`
- `secureMute`
- `UseSingleAudioEngine`
- `MPEGCapabilities`
- `site.AUAMixerUnitDictionary`
- `Device Mode engine failed to start in time`
- `AppleUSBAudioStream::memInterruptReceived: setting kAppleUSBAudioPropertyVoiceActivityDetectEnable to %d`
- `External Line Connector`
- `Embedded CD Player`
- `/Library/Caches/com.apple.xbs/B5FDCB36-D853-46D3-9503-186FD0AD7D5C/TemporaryDirectory.BTvKfA/Sources/AppleUSBAudio/KEXT/AppleUSBAudioDictionary.cpp`
- `ControlDictionaries`
- `Embedded Synthesizer`
- `SynchAddress`
- `site.AppleUSBDeviceAudioNubBase`
- `AC3Features`
- `site.Audio2ToggleControl`
- `IOAudioEngineChannelNames`
- `AppleUSBAudioIsocFrameList`
- `false`
- `122282`
- `Back Right of Center`
- `12111112122212121112121211111121111211112121112121121211122221`
- `Embedded Phonograph`
- `Setting Alt Setting 0 on ADC2 interface - sending Active Alt Setting and Clock Validity Change interrupts to host`
- `probe OverrideWantsHidden returned %s\n`
- `outputvolcontrols`
- `Embedded DVD Audio`
- `IOAudioDeviceName`
- `ExtensionUnits`
- `AppleUSBAudioEngine`
- `IOAudioEngineCoreAudioPlugIn`
- `Bottom Center`
- `USB Sound assertion return 0x%X in %s at line %d\n`
- `InputUndefined`
- `StreamInterfaceNumbers`
- `Transactions`
- `Reserved`
- `/Library/Caches/com.apple.xbs/B5FDCB36-D853-46D3-9503-186FD0AD7D5C/TemporaryDirectory.BTvKfA/Sources/AppleUSBAudio/KEXT/AppleUSBAudioIsocFrameList.cpp`
- `/Library/Caches/com.apple.xbs/B5FDCB36-D853-46D3-9503-186FD0AD7D5C/TemporaryDirectory.BTvKfA/Sources/AppleUSBAudio/KEXT/AUATapStreams.cpp`
- `IOAudioEngineSampleOffset`
- `TerminalLink`
- `AUAFeatureUnitDictionary`
- `CSourceID`
- `mismatched service intervals`
- `NumStreamInterfaces`
- `site.AUAClockSourceDictionary`
- `Top Side Right`
- `kUSBVendorString`
- `inputgaincontrols`
- `outputmutecontrols`
- `unknown ADC3 subclass`
- `FunctionProtocol`
- `USB IDAM`
- `AppleUSBAudioStream::controlInterruptReceived: AS_ACT_ALT_SETTING_CONTROL - something happened on the device. Resetting Engine`
- `Unknown Manufacturer`
- `Output Fell Behind`
- `AppleUSBAudioStream::WatchdogTimer - USB stream seems to have stopped unexpectedly`
- `Clock Domain`
- `Bidirectional Echo Canceling Speakerphone`
- `Telephone Line`
- `AlternateSetting`
- `USB Product Name`
- `input channel layout`
- `site.IOSubMemoryDescriptor*`
- `121112`
- `function category`
- `site.AppleUSBAudioControlInterface`
- `Omnidirectional Microphone`
- `Embedded Video Disc Audio`
- `AppleUSBAudioStream::controlInterruptReceived: unknown control`
- `AppleUSBAudioStream.cpp`
- `AppleUSBAudio.kext`
- `All Channels`
- `AppleUSBAudioControlInterface`
- `/Library/Caches/com.apple.xbs/B5FDCB36-D853-46D3-9503-186FD0AD7D5C/TemporaryDirectory.BTvKfA/Sources/AppleUSBAudio/IDAM/AppleUSBDeviceAudioDevice.cpp`
- `InterfaceNumber`
- `Audio2Engine::addDefaultAudioControl`
- `AppleUSBDeviceAudioDevice`
- `Embedded Undefined`
- `site.AUAFeatureUnitDictionary`
- `AUAExtensionUnitDictionary`
- `Audio2LevelControl`
- `connector detect`
- `AUAOutputTerminalDictionary`
- `site.Audio2Engine`
- `AppleUSBAudioStream`
- `DisplayRouting`
- `/Library/Caches/com.apple.xbs/B5FDCB36-D853-46D3-9503-186FD0AD7D5C/TemporaryDirectory.BTvKfA/Sources/AppleUSBAudio/KEXT/IOAudio2/Audio2Control.cpp`
- `Modem Audio`
- `12112212`
- `Apple Inc`
- `AppleUSBAudioDictionary`
- `site.AppleUSBAudioDictionary`
- `Top Side Left`
- `Unknown Toggle Control Subtype`
- `ProcessingUnits`
- `site.IOMultiMemoryDescriptor*`
- `IOAudioDeviceConfigurationApplication`
- `IOAudioSelectorControlAvailableSelections`
- `Microphone`
- `AppleUSBAudioComposite`
- `Bidirectional Headset`
- `USBADC`
- `copyPipe Failed`
- `Resetting Logitech QuickCam`
- `InvalidSampleRates`
- `site.AUAEndpointDictionary`
- `InputChannel%u`
- `device manufacturer`
- `ClockMultipliers`
- `vendor-id`
- `SubType`
- `Left Low Frequency Effects`
- `AppleUSBAudioDevice:: initialization failed!`
- `External 1394 DV Stream Soundtrack`
- `AUAInputTerminalDictionary`
- `AUASelectorUnitDictionary`
- `NumInPins`
- `mic design`
- `WARNING: AppleUSBAudio has detected an unsupported format type: Type II AC-3`
- ` & `
- `Delay`
- `AUAMixerUnitDictionary`
- `output channel layout`
- `Back Center`
- `1211111212221212111212121111112111121111212111212112121112222`
- `%s:%04X:%04X`
- `Head Mounted Display Audio`
- `Internal Programmable Clock`
- `Streams wrapping on different frames (off by more than 2)`
- `AppleUSBAudioStreamPropertiesReady`
- `Back Left`
- `sample rate`
- `External Legacy Audio Connector`
- `ClockSelectors`
- `site.AUAInputTerminalDictionary`
- `12111`
- `wants input trap`
- `input latency`
- `Couldn't get the endpoint direction!`
- `usbaudio_ignoreZLPInput`
- `Communication Speaker`
- `Embedded TV Tuner Audio`
- `Embedded Satellite Receiver Audio`
- `Embedded Cable Tuner Audio`
- `usbaudio_ignoreAlignment`
- `InterfaceClass`
- `Side Right`
- `usbaudio_deviceModeWatchdog`
- `Microphone Array`
- `Embedded Radio Transmitter`
- `site.AUAClockSelectorDictionary`
- `IOPCITunnelled`
- `%x`
- `io buffer frame size`
- `IOAudioEngineOutputSampleLatency`
- `Embedded Mini Disc`
- `SelectorUnits`
- `Apple Audio 2.0 Device`
- `input streams`
- `Processing Microphone Array`
- `Bidirectional Undefined`
- `site.AUAConfigurationDictionary`
- `Endpoints`
- `NumChannels`
- `ControlSize`
- `connector channels`
- `usbaudio_engines`
- `AppleUSBADCAudioNubBase`
- `12111112122212121212222111221222111112121221121`
- `site.AUASelectorUnitDictionary`
- `Audio2Stream`
- `site.Audio2Stream`
- `1211111212221212111212`
- `site.UInt64*`
- `STSubEnable`
- `Input Fell Behind`
- `Little Endian`
- `OutputChannel%u`
- `121111121222121211111222221121212122222212222222222222222222222222222222222222222221111111111111111111111112211222222122222222212222222222122222222111212222`
- `IOAudioEngineInputSampleLatency`
- `Bidirectional Handset`
- `Bidirectional Speakerphone No Echo Redx`
- `iPHS ID`
- `no service intervals found`
- `could not start engine`
- `Embedded DCC`
- `Resetting engine due to error returned in Write Handler`
- `site.AUAClockMultiplierDictionary`
- `BitResolution`
- `AppleUSBAudioIsocPipe`
- `headset info`
- `SourceIDs`
- `Address`
- `Transfer Alignment`
- `External SPDIF Interface`
- `iPad`
- `Top Back Right`
- `passthrutogglecontrols`
- `IOAudioDeviceModelID`
- `/Library/Caches/com.apple.xbs/B5FDCB36-D853-46D3-9503-186FD0AD7D5C/TemporaryDirectory.BTvKfA/Sources/AppleUSBAudio/KEXT/AppleUSBAudioControlInterface.cpp`
- `/Library/Caches/com.apple.xbs/B5FDCB36-D853-46D3-9503-186FD0AD7D5C/TemporaryDirectory.BTvKfA/Sources/AppleUSBAudio/ADCDevice/AppleUSBADCAudioDevice.cpp`
- `site.Audio2LevelControl`
- `NumControls`
- `Raw Data`
- `Resetting engine for Centrance MicroPort`
- `AppleUSBAudioDevice`
- `true`
- `oob speech`
- `Embedded DAT`
- `Resetting engine due to immediate error on write`
- `hasSampleFreqControl`
- `Interval`
- `Side Left`
- `microphone`
- `Audio2Control`
- `1211111212221212111112222211212121`
- `site.Audio2Device`
- `FeatureUnits`
- `AppleUSBHostController`
- `/Library/Caches/com.apple.xbs/B5FDCB36-D853-46D3-9503-186FD0AD7D5C/TemporaryDirectory.BTvKfA/Sources/AppleUSBAudio/KEXT/IOAudio2/Audio2Engine.cpp`
- `site.Audio2Control`
- `site.AppleUSBDeviceAudioDevice`
- `AppleUSBAudioDevice::setVoiceActivityDetectState on stream %d - need to send %d to the host\n`
- `Room Speaker`
- `AUAEndpointDictionary`
- `12111112122212121`
- `mic connector reversed`
- `/Library/Caches/com.apple.xbs/B5FDCB36-D853-46D3-9503-186FD0AD7D5C/TemporaryDirectory.BTvKfA/Sources/AppleUSBAudio/KEXT/IOAudio2/Audio2Stream.cpp`
- `Yes`
- `OutputTerminals`
- `AC3BSID`
- `InterfaceSubClass`
- `device name`
- `Resetting engine to switch to adaptive mode`
- `engine`
- `IOAudioSelectorControlSelectionValue`
- `AUAControlDictionary`
- `transport type`
- `site.AUAExtensionUnitDictionary`
- `AUAClockSourceDictionary`
- `AAPL,xhci-clock-id`
- `,`
- `111`
- `EUModeOnByDefault`
- `MaxPacketSize`
- `output safety offset`
- `AppleUSBAudioEngine:%s:%s:%s`
- `site.Audio2SelectorControl`
- `site.AppleUSBAudioStreamNode`
- `Adding the voice activity detected control to interface %d`
- `Front Left`
- `IOAudioStreamFormat`
- `device UID`
- `Interface doesn't have any supported formats!`
- `Speaker`
- `Headphones`
- `HasAdaptiveAsynchronousOutput`
- `LockDelay`
- `STGain`
- `Personal Microphone`
- `Unable to find path`
- `Mac Sync`
- `clock domain`
- `Resetting engine due to excess data from device`
- `Embedded Level Calibration Noise Source`
- `MixerUnits`
- `SourceID`
- `transmitter tone id`
- `usbaudio_ignoretapstreams`
- `site.UInt64`
- `usbaudio_useKEXT`
- `Resetting engine due to zero length packets at the beginning of a stream`
- `12228`
- `site.AUAOutputTerminalDictionary`
- `Low Frequency Effects`
- `site.AppleUSBAudioControlNub`
- `usbDevice:`
- `External Clock`
- `usbaudio_tsoffset`
- `wants output trap`
- `Internal Variable Clock`
- `hasPitchControl`
- `site.IOBufferMemoryDescriptor*`
- `kUSBSerialNumberString`
- `AppleUSBAudioDevice::doToggleControlChange(uVAD) to %d`
- `Top Front Right`
- `Top Front Left of Center`
- `External Digital Audio Interface`
- `invalid Protocol in IAD`
- `site.AUAEffectUnitDictionary`
- `Right Low Frequency Effects`
- `idProduct`
- `FunctionSubclass`
- `ChannelNames`
- `Index`
- `Resetting engine due to immediate error on feedback pipe at start`
- `Unknown USB Audio Device`
- `altsetting`
- `SampleRanges`
- `MaxBitRate`
- `Front Right`
- `External Analog Connector`
- `IOAudioDeviceManufacturerName`
- `2222121`
- `Resetting engine due to error returned to Feedback`
- `site.AppleUSBAudioEngine`
- `Top Back Center`
- `Desktop Microphone`
- `AUAProcessingUnitDictionary`
- `IOAudioStreamTap`
- `property selector`
- `AUAClockMultiplierDictionary`
- `site.AppleUSBAudioIndividualFrameInfo`
- `Resetting engine due to immediate error on feedback`
- `site.AUAControlDictionary`
- `ClockSources`
- `site.AUAASEndpointDictionary`
- `mode`
- `Audio2Engine`
- `idVendor`
- `usbaudio_allowusbidling`
- `Back Right`
- `registry key`
- `Unknown`
- `isoch-out-alignment`
- `USB bcdUSB 1 with invalid endpoint interval - forcing 1ms interval`
- `AUAClockSelectorDictionary`
- `CSourceIDs`
- `Top Front Center`
- `Top Center`
- `%s:`
- `kUSBPreferredConfiguration`
- `MPEGFeatures`
- `interface`
- `Resetting engine due to immediate error on read`
- `StringIndex`
- `IOAudioEngineInputSampleOffset`
- `EQ192Flat`
- `Resetting engine to switch to sync mode`
- `Bidirectional Echo Suppressing Speakerphone`
- `Audio2ToggleControl`
- `locationID`
- `site.AppleUSBAudioIsocFrameList`
- `value`
- `Audio2SelectorControl`
- `IOAudioDeviceShortName`
- `/Library/Caches/com.apple.xbs/B5FDCB36-D853-46D3-9503-186FD0AD7D5C/TemporaryDirectory.BTvKfA/Sources/AppleUSBAudio/KEXT/AppleUSBAudioStream.cpp`
- `button`
- `multiple buttons`
- `current state`
- `212`
- `IOAudioDeviceLocalizedBundle`
- `Embedded Radio Receiver`
- `AUAADC3ClassSpecificDescriptorFetcher`
- `Formats`
- `Top Front Right of Center`
- `Resetting engine after delay`
- `AppleUSBADCAudioDevice`
- `site.IOUSBHostIsochronousCompletion`
- `Front Center`
- `STEnable`
- `Embedded DSS Audio`
- `Top Front Left`
- `controls`
- `read only`
- `usbaudio_outputsafetyoffset`
- `Unknown location`
- `IOAudioStreamDirection`
- `AppleUSBAudioStream::controlInterruptReceived: AS_VAL_ALT_SETTINGS_CONTROL - not handled`
- `SubframeSize`
- `site.AUAUnitDictionary`
- `site.AppleUSBAudioIsocPipe`
- `site.AppleUSBAudioInterruptPipe`
- `IOAudioStreamSampleFormatByteOrder`
- `Top Back Left`
- `site.AppleUSBAudioDevice`
- `External Undefined`
- `Embedded Equalization Noise`
- `EUModeOnNow`
- `unknown entity\n`
- `ASIsocEndpoint`
- `product-id`
- `site.AppleUSBAudioTransferInfo`
- `Embedded VCR Audio`
- `site.AUAADC3ClassSpecificDescriptorFetcher`
- `AUAConfigurationDictionary`
- `passthruselectorcontrol`
- `AUAASEndpointDictionary`
- `%lx`
- `kSamplesPerFrame`
- `WARNING: This USB audio device may not function properly. Please notify the device manufacturer.\n`
- `EQ48Flat`
- `Front Right of Center`
- `121112111`
- `USB Sound assertion (%s) in %s at line %d\n`
- `Telephone Undefined`
- `TimeStampOffset`
- `%s%s%d`
- `/Library/Caches/com.apple.xbs/B5FDCB36-D853-46D3-9503-186FD0AD7D5C/TemporaryDirectory.BTvKfA/Sources/AppleUSBAudio/KEXT/IOAudio2/Audio2Device.cpp`
- `SampleRates`
- `Audio2Device`
- `site.AppleUSBAudioStream`
- `usbaudio_deviceModePanicOnWriteError`
- `EffectType`
- `RefreshInt`
- `EQMicFlat`
- `site.AUAStreamDictionary`
