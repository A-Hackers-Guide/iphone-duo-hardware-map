# `com.apple.driver.AOPAudio2`

- Name: AOPAudioDriver
- Version: `400.12`
- UUID: `DD19B89E-DB5C-3829-A759-B073A03BC5DE`
- Source version: `400.12.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleEmbeddedAudioLibs`](com.apple.driver.AppleEmbeddedAudioLibs.md) 1.0, [`com.apple.driver.AppleSPU`](com.apple.driver.AppleSPU.md) 1.0.0, [`com.apple.iokit.IOPAudioDriverFamily`](com.apple.iokit.IOPAudioDriverFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0

## Device-tree nodes it binds (4) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/aop/iop-aop-nub/aop-audio`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-audio.md) | `AOPAudioService` | `iop-audio,aop-service` |
| [`/arm-io/aop/iop-aop-nub/aop-audio`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-audio.md) | `AOPAudioService` | `aop-audio` |
| [`/arm-io/aop/iop-aop-nub/aop-voicetrigger`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-voicetrigger.md) | `AOPAudioService` | `iop-audio,aop-service` |
| [`/arm-io/aop/iop-aop-nub/aop-voicetrigger`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-voicetrigger.md) | `AOPAudioService` | `aop-voicetrigger` |

## IOKit personalities (1) [KC]

### AOPAudioService
- `CFBundleIdentifier`: `com.apple.driver.AOPAudio2`
- `IOClass`: `AOPAudioService`
- `IONameMatch`:
  - `aop-audio`
  - `aop-voicetrigger`
  - `iop-audio,aop-service`
- `IOPersonalityPublisher`: `com.apple.driver.AOPAudio2`
- `IOProviderClass`: `AppleSPUAppInterface`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AOPAudioService` | 0xc0 | IOPAudioService → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001682 off=0x0013fa90-0x00141112 addr=0xfffffe0007143a90-0xfffffe0007145112 r--/r--   __TEXT            
	sz=0x00000030 off=0x00140160-0x00140190 addr=0xfffffe0007144160-0xfffffe0007144190               __TEXT.__const            
	sz=0x00000489 off=0x00140190-0x00140619 addr=0xfffffe0007144190-0xfffffe0007144619               __TEXT.__os_log           
	sz=0x00000af9 off=0x00140619-0x00141112 addr=0xfffffe0007144619-0xfffffe0007145112               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00002ea4 off=0x01608780-0x0160b624 addr=0xfffffe000860c780-0xfffffe000860f624 r-x/r-x   __TEXT_EXEC       
	sz=0x00002cb4 off=0x01608780-0x0160b434 addr=0xfffffe000860c780-0xfffffe000860f434          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001f0 off=0x0160b434-0x0160b624 addr=0xfffffe000860f434-0xfffffe000860f624          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000108 off=0x0492dad8-0x0492dbe0 addr=0xfffffe000b931ad8-0xfffffe000b931be0 rw-/rw-   __DATA            
	sz=0x000000d0 off=0x0492dad8-0x0492dba8 addr=0xfffffe000b931ad8-0xfffffe000b931ba8               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b931ba8-0xfffffe000b931be0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000c88 off=0x00f8a650-0x00f8b2d8 addr=0xfffffe0007f8e650-0xfffffe0007f8f2d8 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x00f8a650-0x00f8a658 addr=0xfffffe0007f8e650-0xfffffe0007f8e658         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x00f8a658-0x00f8a660 addr=0xfffffe0007f8e658-0xfffffe0007f8e660         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000007f8 off=0x00f8a660-0x00f8ae58 addr=0xfffffe0007f8e660-0xfffffe0007f8ee58         __DATA_CONST.__const            
	sz=0x000000c0 off=0x00f8ae58-0x00f8af18 addr=0xfffffe0007f8ee58-0xfffffe0007f8ef18         __DATA_CONST.__kalloc_type      
	sz=0x00000280 off=0x00f8af18-0x00f8b198 addr=0xfffffe0007f8ef18-0xfffffe0007f8f198         __DATA_CONST.__kalloc_var       
	sz=0x000000f8 off=0x00f8b198-0x00f8b290 addr=0xfffffe0007f8f198-0xfffffe0007f8f290         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000048 off=0x00f8b290-0x00f8b2d8 addr=0xfffffe0007f8f290-0xfffffe0007f8f2d8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 71 at 0x04ad0958
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     DD19B89E-DB5C-3829-A759-B073A03BC5DE
008: LC_SOURCE_VERSION           400.12.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a96278 size=0x90
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleExecutable`: `AOPAudioDriver`
- `CFBundleIdentifier`: `com.apple.driver.AOPAudio2`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AOPAudioDriver`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `400.12`
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
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AOPAudioDriver.kext`
- `_PrelinkExecutableLoadAddr`: `-2198904489328`
- `_PrelinkExecutableRelativePath`: `AOPAudioDriver`
- `_PrelinkExecutableSize`: `21174`
- `_PrelinkExecutableSourceAddr`: `-2198904489328`
- `_PrelinkKmodInfo`: `-2198829065512`

## Strings (55) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `%s::%s(..) Failed to deliver message ret=%#x`
- `%s: %s, %s file: %s, line: %d\n`

**[__TEXT.__cstring]**

- `121111121222121211122211`
- `!(static_cast<bool>(mServiceInterface))`
- `!((inConnectionInfo.audioService) == nullptr)`
- `AOPAudioService`
- `site.AOPAudioService`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `mServiceInterface->open(mAudioService.get())`
- `AOPCommandInterface`
- `site.RegisterAccess::Packet.uint8_t`
- `/Library/Caches/com.apple.xbs/C9C26AD7-9CB6-4E87-BD55-E0086C9C4601/TemporaryDirectory.bWezrQ/Sources/IOPAudioDriverFamily/src/kext/AOPAudioDriver/service/AOPAudioService/AOPAudioService.cpp`
- `!((inProvider) == nullptr)`
- `ret = mServiceInterface->GetProperty(inPropertyID, ioData, ioDataSize) == 0 `
- `site.AOPCommandInterface`
- `1222111`
- `iop-audio,aop-service`
- `!((key) == nullptr)`
- `!((mServiceInterface) == nullptr)`
- `!((mAudioService) == nullptr)`
- `ret = (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2c7) == 0 `
- `!((spuAppInterface) == nullptr)`
- `/Library/Caches/com.apple.xbs/C9C26AD7-9CB6-4E87-BD55-E0086C9C4601/TemporaryDirectory.bWezrQ/Sources/IOPAudioDriverFamily/src/kext/AOPAudioDriver/service/AOPAudioService/AOPAudioServicePrivate.cpp`
- `\"%s\" @%s:%d`
- `The offset of the pointer inside its valid memory range can't be represented using int32_t`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `\"%s::%s() not ready yet.\" @%s:%d`
- `!(static_cast<bool>(mCommandInterface))`
- `ret = AOPPrivate::processOptionalNameOverrideFromRegistry(inProvider, this) == 0 `
- `ret = mCommandInterface->openConnection(AOPCommandInterface::ConnectionInfo{ .interface = spuAppInterface, .audioService = this, .reportPacketAction = reportPacketAction, }) == 0 `
- `ret = mAggregateMessageDispatcher->sendMessage(message) == 0 `
- `!((value) == nullptr)`
- `!((serviceName) == nullptr)`
- `!((interface) == nullptr)`
- `!((packet) == nullptr)`
- `getCommandInterface`
- `customMapper->setObject(key.get(), value)`
- `!((inTargetService) == nullptr)`
- `dataPtr != nullptr`
- `!(serviceName->getLength() < kMinimumCustomServiceNameLength)`
- `AOPAudioService::Private`
- `message-map-override`
- `!(static_cast<bool>(mAudioService))`
- `!((inConnectionInfo.interface) == nullptr)`
- `AOPAudioService.cpp`
- `_spuReportPacketHandler`
- `OSBoundedPtr.h`
- `name-override`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `/Library/Caches/com.apple.xbs/C9C26AD7-9CB6-4E87-BD55-E0086C9C4601/TemporaryDirectory.bWezrQ/Sources/IOPAudioDriverFamily/src/kext/AOPAudioDriver/service/AOPAudioCommandInterface/AOPAudioCommandInterface.cpp`
- `ret = mServiceInterface->SetProperty(inPropertyID, inData, inDataSize) == 0 `
- `ret = performCommand(packet, outPayload, outPayloadSize) == 0 `
- `!((inPacket) == nullptr)`
- `site.Packet.uint8_t`
