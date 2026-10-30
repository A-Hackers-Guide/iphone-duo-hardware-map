# `com.apple.driver.IOPAudioIOBufferDevice`

- Name: IOPAudioIOBufferDevice
- Version: `400.36`
- UUID: `438F00FC-FC07-310A-8CAA-B41CAC47D593`
- Source version: `400.36.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.iokit.IOPAudioDriverFamily`](com.apple.iokit.IOPAudioDriverFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### IOBufferDevice
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioIOBufferDevice`
- `IOClass`: `IOPAudioIOBufferDevice`
- `IONameMatch`:
  - `iop-audio,io-buffer-device`
- `IOPersonalityPublisher`: `com.apple.driver.IOPAudioIOBufferDevice`
- `IOProviderClass`: `IOPAudioNode`
- `IOUserClientClass`: `IOPAudioIOBufferDeviceUserClient`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOPAudioIOBufferDevice` | 0xc0 | IOPAudioDevice → IOService → IORegistryEntry |
| `IOPAudioIOBufferDeviceUserClient` | 0xe8 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001161 off=0x00a338e0-0x00a34a41 addr=0xfffffe0007a378e0-0xfffffe0007a38a41 r--/r--   __TEXT            
	sz=0x000007a4 off=0x00a33f58-0x00a346fc addr=0xfffffe0007a37f58-0xfffffe0007a386fc               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000345 off=0x00a346fc-0x00a34a41 addr=0xfffffe0007a386fc-0xfffffe0007a38a41               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0000202c off=0x032f9350-0x032fb37c addr=0xfffffe000a2fd350-0xfffffe000a2ff37c r-x/r-x   __TEXT_EXEC       
	sz=0x00001f1c off=0x032f9350-0x032fb26c addr=0xfffffe000a2fd350-0xfffffe000a2ff26c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000110 off=0x032fb26c-0x032fb37c addr=0xfffffe000a2ff26c-0xfffffe000a2ff37c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000130 off=0x04a142e0-0x04a14410 addr=0xfffffe000ba182e0-0xfffffe000ba18410 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a142e0-0x04a143a8 addr=0xfffffe000ba182e0-0xfffffe000ba183a8               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000ba183a8-0xfffffe000ba18408               __DATA.__common           (Zerofill)
	sz=0x00000008 off=0x00000000-0x00000008 addr=0xfffffe000ba18408-0xfffffe000ba18410               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00000e28 off=0x013ca868-0x013cb690 addr=0xfffffe00083ce868-0xfffffe00083cf690 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x013ca868-0x013ca878 addr=0xfffffe00083ce868-0xfffffe00083ce878         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x013ca878-0x013ca888 addr=0xfffffe00083ce878-0xfffffe00083ce888         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000cb8 off=0x013ca888-0x013cb540 addr=0xfffffe00083ce888-0xfffffe00083cf540         __DATA_CONST.__const            
	sz=0x00000080 off=0x013cb540-0x013cb5c0 addr=0xfffffe00083cf540-0xfffffe00083cf5c0         __DATA_CONST.__kalloc_type      
	sz=0x00000088 off=0x013cb5c0-0x013cb648 addr=0xfffffe00083cf5c0-0xfffffe00083cf648         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000048 off=0x013cb648-0x013cb690 addr=0xfffffe00083cf648-0xfffffe00083cf690         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 43 at 0x04af5a34
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     438F00FC-FC07-310A-8CAA-B41CAC47D593
008: LC_SOURCE_VERSION           400.36.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac3bb8 size=0x68
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleExecutable`: `IOPAudioIOBufferDevice`
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioIOBufferDevice`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOPAudioIOBufferDevice`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `400.36`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `400.36`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOPAudioIOBufferDevice.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895101728`
- `_PrelinkExecutableRelativePath`: `IOPAudioIOBufferDevice`
- `_PrelinkExecutableSize`: `16613`
- `_PrelinkExecutableSourceAddr`: `-2198895101728`
- `_PrelinkKmodInfo`: `-2198828121376`

## Strings (40) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `ret = super::_handleStart(inProvider) == 0 `
- `*ioBufferSizePtr > 0`
- `io-buffer-size`
- `!((outOptions) == nullptr)`
- `entitlement == kOSBooleanTrue`
- `!((mDevice) == nullptr)`
- `/Library/Caches/com.apple.xbs/20732553-D3E1-4B38-B5F5-87A23D935C9E/TemporaryDirectory.oCjbCa/Sources/IOPAudioDrivers/src/kext/IOBufferDevice/IOBufferDevice.cpp`
- `!((mMapper) == nullptr)`
- `!((mIODMACommand) == nullptr)`
- `12111112122212121111111111111`
- `IOPAudioIOBufferDevice`
- `ret = _configure(inProvider) == 0 `
- `!((ioBufferSizeData) == nullptr)`
- `ret = getAndSendSingleVMSegmentInfo(getNodeInterface(), mIODMACommand) == 0 `
- `vmSegmentCount == kDefaultVMSegmentCount`
- `IOUserClient::initWithTask(inOwningTask, inSecurityToken, inType, inProperties)`
- `com.apple.private.aop-audio.user-access`
- `IOPAudio::IOBufferDevice::UserClient`
- `!((mIOBufferMemoryDescriptor) == nullptr)`
- `ret = mMapper->callPlatformFunction(\"setActive\", false, reinterpret_cast<void *>(true), reinterpret_cast<void *>(false), nullptr, nullptr) == 0 `
- `ret = mIODMACommand->setMemoryDescriptor(mIOBufferMemoryDescriptor.get(), kDMACommandAudioPrepare) == 0 `
- `ret = (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2c7) == 0 `
- `ret = inDMACommand->genIOVMSegments(&vmSegmentOffset, vmSegments, &vmSegmentCount) == 0 `
- `ret = sendVMSegmentInfo(inNode, vmSegments[0]) == 0 `
- `ret = inNode->setNodeProperty(kPropertyDescriptor) == 0 `
- `site.IOPAudioIOBufferDevice`
- `ret = super::_handleDeviceReady(inProvider) == 0 `
- `ret = mIODMACommand->prepare() == 0 `
- `IOPAudioIOBufferDeviceUserClient`
- `site.IOPAudioIOBufferDeviceUserClient`
- `mDevice->open(this)`
- `121111121222121211112111`
- `!((ioBufferSizePtr) == nullptr)`
- `setActive`
- `IOPAudio::IOBufferDevice`
- `ret = mDevice->getClientMemoryForType(inType, *outOptions, memoryDescriptor) == 0 `
- `/Library/Caches/com.apple.xbs/20732553-D3E1-4B38-B5F5-87A23D935C9E/TemporaryDirectory.oCjbCa/Sources/IOPAudioDrivers/src/kext/IOBufferDevice/UserClient/IOBufferDeviceUserClient.cpp`
- `super::start(inProvider)`
- `!((outMemory) == nullptr)`

**[__TEXT.__os_log]**

- `%s: %s, %s file: %s, line: %d\n`
