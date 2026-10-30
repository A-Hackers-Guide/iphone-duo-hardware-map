# `com.apple.driver.IOPEmbeddedAudio`

- Name: IOPEmbeddedAudio
- Version: `1010.2`
- UUID: `A530AA59-6B40-3056-8A0A-FE1BB79715ED`
- Source version: `1010.2.0.0.0`
- Depends on: [`com.apple.driver.AppleEmbeddedAudio`](com.apple.driver.AppleEmbeddedAudio.md) 1.1.0, [`com.apple.iokit.IOPAudioDriverFamily`](com.apple.iokit.IOPAudioDriverFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### IOPEmbeddedAudio
- `CFBundleIdentifier`: `com.apple.driver.IOPEmbeddedAudio`
- `IOClass`: `IOPEmbeddedAudio`
- `IONameMatch`:
  - `audio-control,iop-embeddedaudio`
- `IOPersonalityPublisher`: `com.apple.driver.IOPEmbeddedAudio`
- `IOProviderClass`: `IOPAudioNode`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOPEmbeddedAudio` | 0x228 | AppleEmbeddedAudio → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001315 off=0x0043e150-0x0043f465 addr=0xfffffe0007442150-0xfffffe0007443465 r--/r--   __TEXT            
	sz=0x00000018 off=0x0043e7c8-0x0043e7e0 addr=0xfffffe00074427c8-0xfffffe00074427e0               __TEXT.__const            
	sz=0x000009bc off=0x0043e7e0-0x0043f19c addr=0xfffffe00074427e0-0xfffffe000744319c               __TEXT.__cstring          (CstringLiterals)
	sz=0x000002c9 off=0x0043f19c-0x0043f465 addr=0xfffffe000744319c-0xfffffe0007443465               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00002928 off=0x01c158b0-0x01c181d8 addr=0xfffffe0008c198b0-0xfffffe0008c1c1d8 r-x/r-x   __TEXT_EXEC       
	sz=0x00002808 off=0x01c158b0-0x01c180b8 addr=0xfffffe0008c198b0-0xfffffe0008c1c0b8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000120 off=0x01c180b8-0x01c181d8 addr=0xfffffe0008c1c0b8-0xfffffe0008c1c1d8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000168 off=0x0493e5f8-0x0493e760 addr=0xfffffe000b9425f8-0xfffffe000b942760 rw-/rw-   __DATA            
	sz=0x00000130 off=0x0493e5f8-0x0493e728 addr=0xfffffe000b9425f8-0xfffffe000b942728               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b942728-0xfffffe000b942760               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000d20 off=0x01078cd8-0x010799f8 addr=0xfffffe000807ccd8-0xfffffe000807d9f8 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01078cd8-0x01078ce0 addr=0xfffffe000807ccd8-0xfffffe000807cce0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01078ce0-0x01078ce8 addr=0xfffffe000807cce0-0xfffffe000807cce8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000c10 off=0x01078ce8-0x010798f8 addr=0xfffffe000807cce8-0xfffffe000807d8f8         __DATA_CONST.__const            
	sz=0x00000040 off=0x010798f8-0x01079938 addr=0xfffffe000807d8f8-0xfffffe000807d938         __DATA_CONST.__kalloc_type      
	sz=0x00000090 off=0x01079938-0x010799c8 addr=0xfffffe000807d938-0xfffffe000807d9c8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000030 off=0x010799c8-0x010799f8 addr=0xfffffe000807d9c8-0xfffffe000807d9f8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 42 at 0x04ad8144
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     A530AA59-6B40-3056-8A0A-FE1BB79715ED
008: LC_SOURCE_VERSION           1010.2.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9eb28 size=0x78
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleExecutable`: `IOPEmbeddedAudio`
- `CFBundleIdentifier`: `com.apple.driver.IOPEmbeddedAudio`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOPEmbeddedAudio`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1010.2`
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
- `NSHumanReadableCopyright`: `Copyright © 2023 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleEmbeddedAudio.kext/PlugIns/IOPEmbeddedAudio.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901350064`
- `_PrelinkExecutableRelativePath`: `IOPEmbeddedAudio`
- `_PrelinkExecutableSize`: `19141`
- `_PrelinkExecutableSourceAddr`: `-2198901350064`
- `_PrelinkKmodInfo`: `-2198828997128`

## Strings (53) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `prewarm-state`
- `!((outConfig.modelName) == nullptr)`
- `totalSelectorCount > 0`
- `!((selectorMap) == nullptr)`
- `IOPEmbeddedAudio::Helper`
- `!((value) == nullptr)`
- `model-name`
- `zerofill-buffer-size-ms`
- `!((dataPtr) == nullptr)`
- `/Library/Caches/com.apple.xbs/7374CF14-96FD-494A-A9F3-D02707F144CC/TemporaryDirectory.6UQLML/Sources/AppleEmbeddedAudio/src/kext/IOPEmbeddedAudio/IOPEmbeddedAudioHelpers.h`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `static_cast<bool>(theControl)`
- `uid`
- `output-data-source-selectors`
- `totalEntryCount > 0`
- `\"%s\" @%s:%d`
- `ret = Helper::retrieveConfigurationFromIORegistry(inProvider, mConfig) == 0 `
- `ret = setNodeProperty(IOPAudio::MakeSetPropertyDescriptor(kPropertyID, pingValue)) == 0 `
- `ret = getNodeInterface()->setNodeProperty(inPropertyDescriptor) == 0 `
- `DeviceAttached`
- `input-data-source-selectors`
- `default-input-data-sources`
- `fixed-input-data-sources`
- `fixed-output-data-sources`
- `ret = setClientManagerPowerRequest(newPowerRequest) == 0 `
- `!(mLastPowerRequest.state == inPowerRequest.state && mLastPowerRequestResult == 0)`
- `i8@?0`
- `!((defaultSelectors) == nullptr)`
- `!(defaultSelectors->getCount() > selectorMap->getCount())`
- `!((theArray) == nullptr)`
- `OSBoundedPtr.h`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `IOPEmbeddedAudio`
- `input-latency`
- `!((inRegistryEntry) == nullptr)`
- `/Library/Caches/com.apple.xbs/7374CF14-96FD-494A-A9F3-D02707F144CC/TemporaryDirectory.6UQLML/Sources/AppleEmbeddedAudio/src/kext/IOPEmbeddedAudio/IOPEmbeddedAudioHelpers.cpp`
- `!((outConfig.uid) == nullptr)`
- `The offset of the pointer inside its valid memory range can't be represented using int32_t`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `site.IOPEmbeddedAudio`
- `121111121222121211212121112111111111211111112111211121111221122111122`
- `output-latency`
- `powered-on-state`
- `default-output-data-sources`
- `/Library/Caches/com.apple.xbs/7374CF14-96FD-494A-A9F3-D02707F144CC/TemporaryDirectory.6UQLML/Sources/AppleEmbeddedAudio/src/kext/IOPEmbeddedAudio/IOPEmbeddedAudio.cpp`
- `ret = getNodeInterface()->getNodeProperty(ioPropertyDescriptor) == 0 `
- `Unknown`
- `!((inRawData) == nullptr)`
- `!((boundedArray) == nullptr)`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `!((mNodeInterface) == nullptr)`
- `ret = getNodeProperty(IOPAudio::MakeGetPropertyDescriptor(kPropertyID, pingValue)) == 0 `

**[__TEXT.__os_log]**

- `%s: %s, %s file: %s, line: %d\n`
