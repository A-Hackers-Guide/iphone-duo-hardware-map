# `com.apple.driver.IOPAudioSpeaker`

- Name: IOPAudioSpeaker
- Version: `1010.2`
- UUID: `47B95CE3-3C18-3A3D-9939-DD0BBC3D947B`
- Source version: `1010.2.0.0.0`
- Depends on: [`com.apple.driver.AppleAOPAudio`](com.apple.driver.AppleAOPAudio.md) 1.1, [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0, [`com.apple.driver.AppleEmbeddedAudio`](com.apple.driver.AppleEmbeddedAudio.md) 1.1.0, [`com.apple.driver.AppleIISController`](com.apple.driver.AppleIISController.md) 1.0, [`com.apple.iokit.AppleARMIISAudio`](com.apple.iokit.AppleARMIISAudio.md) 1.0, [`com.apple.iokit.IOAudio2Family`](com.apple.iokit.IOAudio2Family.md) 1.0, [`com.apple.iokit.IOPAudioDriverFamily`](com.apple.iokit.IOPAudioDriverFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (2) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/iop-audio-controller/audio-speaker`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker.md) | `IOPAudioSpeaker` | `audio-iop-speaker` |
| [`/arm-io/iop-audio-controller/audio-speaker`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker.md) | `IOPAudioSpeaker` | `audio-iop-speaker` |

## IOKit personalities (2) [KC]

### AOPAudioSpeaker
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioSpeaker`
- `IOClass`: `IOPAudioSpeaker`
- `IONameMatch`:
  - `audio-iop-speaker`
- `IOPersonalityPublisher`: `com.apple.driver.IOPAudioSpeaker`
- `IOProviderClass`: `AppleAOPAudioDeviceProvider`

### IOPAudioSpeaker
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioSpeaker`
- `IOClass`: `IOPAudioSpeaker`
- `IONameMatch`:
  - `audio-iop-speaker`
- `IOPersonalityPublisher`: `com.apple.driver.IOPAudioSpeaker`
- `IOProviderClass`: `IOPAudioNode`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOPAudioSpeaker` | 0x1f8 | AppleEmbeddedAudio → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000d01 off=0x0043d440-0x0043e141 addr=0xfffffe0007441440-0xfffffe0007442141 r--/r--   __TEXT            
	sz=0x00000018 off=0x0043dab8-0x0043dad0 addr=0xfffffe0007441ab8-0xfffffe0007441ad0               __TEXT.__const            
	sz=0x000004c3 off=0x0043dad0-0x0043df93 addr=0xfffffe0007441ad0-0xfffffe0007441f93               __TEXT.__cstring          (CstringLiterals)
	sz=0x000001ae off=0x0043df93-0x0043e141 addr=0xfffffe0007441f93-0xfffffe0007442141               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x000023a4 off=0x01c13500-0x01c158a4 addr=0xfffffe0008c17500-0xfffffe0008c198a4 r-x/r-x   __TEXT_EXEC       
	sz=0x00002254 off=0x01c13500-0x01c15754 addr=0xfffffe0008c17500-0xfffffe0008c19754          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000150 off=0x01c15754-0x01c158a4 addr=0xfffffe0008c19754-0xfffffe0008c198a4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x0493e4f8-0x0493e5f8 addr=0xfffffe000b9424f8-0xfffffe000b9425f8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0493e4f8-0x0493e5c0 addr=0xfffffe000b9424f8-0xfffffe000b9425c0               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9425c0-0xfffffe000b9425f8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000cb0 off=0x01078028-0x01078cd8 addr=0xfffffe000807c028-0xfffffe000807ccd8 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01078028-0x01078030 addr=0xfffffe000807c028-0xfffffe000807c030         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01078030-0x01078038 addr=0xfffffe000807c030-0xfffffe000807c038         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000b70 off=0x01078038-0x01078ba8 addr=0xfffffe000807c038-0xfffffe000807cba8         __DATA_CONST.__const            
	sz=0x00000040 off=0x01078ba8-0x01078be8 addr=0xfffffe000807cba8-0xfffffe000807cbe8         __DATA_CONST.__kalloc_type      
	sz=0x000000a8 off=0x01078be8-0x01078c90 addr=0xfffffe000807cbe8-0xfffffe000807cc90         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000048 off=0x01078c90-0x01078cd8 addr=0xfffffe000807cc90-0xfffffe000807ccd8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 51 at 0x04ad8078
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     47B95CE3-3C18-3A3D-9939-DD0BBC3D947B
008: LC_SOURCE_VERSION           1010.2.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9ead0 size=0x58
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOPAudioSpeaker`
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioSpeaker`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOPAudioSpeaker`
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
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleEmbeddedAudio.kext/PlugIns/IOPAudioSpeaker.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901353408`
- `_PrelinkExecutableRelativePath`: `IOPAudioSpeaker`
- `_PrelinkExecutableSize`: `15957`
- `_PrelinkExecutableSourceAddr`: `-2198901353408`
- `_PrelinkKmodInfo`: `-2198828997384`

## Strings (40) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `pdm-amp-id`
- `output-data-source-selectors`
- `device-property-list`
- `output-latency`
- `DeviceAttached`
- `121111121222121211212121112111111111211111112111211121111221212`
- `transferEdtDeviceProperties`
- `%s setMCLKFrequency ret:%x\n`
- `setInputMCLKEnabled`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `%s %s::%s:%d Failed to set %s ret=0x%x\n`
- `input-data-source-selectors`
- `speaker-config-`
- `bounded_ptr<T>::discard_bounds: Discarding the bounds on this pointer would lose the fact that it is outside of the bounds set originally`
- `site.IOPAudioSpeaker`
- `%s::%s() node %c%c%c%c, propertyId %u propertyVal is NULL\n\n`
- `getSupportedBitsPerSampleList`
- `Speaker`
- `%s::%s() failed to transfer node %c%c%c%c, propertyId %u, ret = %x\n\n`
- `IOPAudioSpeaker`
- `%s%u`
- `%s::%s(enabled=%d) failed [errorCode: 0x%x]\n`
- `The offset of the pointer inside its valid memory range can't be represented using int32_t`
- `OSBoundedPtr.h`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `model-name`
- `CS35L28`
- `setEDTSpeakerConfig`
- `input-latency`
- `\"%s\" @%s:%d`

**[__TEXT.__os_log]**

- `%s::%s line:%d inDirection:%u outCurrentBitsPerSample=%u ret=%d`
- `%s::%s(enabled=%d) failed [errorCode: 0x%x]`
- `%s::%s() node %c%c%c%c, propertyId %u propertyVal is NULL\n`
- `%s %s::%s:%d Failed to set %s ret=0x%x`
- `%s setMCLKEnabled(%d) ret:%x`
- `%s setMCLKFrequency ret:%x`
- `%s::%s() ByteOffset=%d, nodeID %c%c%c%c, propertyID %d edtKeyName:%s\n`
- `%s::%s() failed to transfer node %c%c%c%c, propertyId %u, ret = %x\n`
- `%s::%s line:%d inDirection:%u`
