# `com.apple.driver.IOPAudioPCMAssetManagerDevice`

- Name: IOPAudioPCMAssetManagerDevice
- Version: `400.36`
- UUID: `C487F47D-C957-330B-BA0A-E4E62DC01F80`
- Source version: `400.36.0.0.0`
- Depends on: [`com.apple.driver.IOPAudioAssetManagerDevice`](com.apple.driver.IOPAudioAssetManagerDevice.md) 1.0, [`com.apple.iokit.IOPAudioDriverFamily`](com.apple.iokit.IOPAudioDriverFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/iop-audio-controller/audio-hw-pcm-audiomgr`](../devicetree/root__arm-io__iop-audio-controller__audio-hw-pcm-audiomgr.md) | `IOPAudioPCMAssetManagerDevice` | `iop-audio,pcm-asset-manager-device` |

## IOKit personalities (1) [KC]

### PCMAssetManagerDevice
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioPCMAssetManagerDevice`
- `IOClass`: `IOPAudioPCMAssetManagerDevice`
- `IONameMatch`:
  - `iop-audio,pcm-asset-manager-device`
- `IOPersonalityPublisher`: `com.apple.driver.IOPAudioPCMAssetManagerDevice`
- `IOProviderClass`: `IOPAudioNode`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOPAudioPCMAssetManagerDevice` | 0xb8 | IOPAudioAssetManagerDevice → IOPAudioDevice → IOService → IORegistryEntry |
| `IOPAudioPCMAssetManagerDeviceUserClient` | 0xf8 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000143e off=0x00a39510-0x00a3a94e addr=0xfffffe0007a3d510-0xfffffe0007a3e94e r--/r--   __TEXT            
	sz=0x0000099b off=0x00a39b38-0x00a3a4d3 addr=0xfffffe0007a3db38-0xfffffe0007a3e4d3               __TEXT.__cstring          (CstringLiterals)
	sz=0x0000047b off=0x00a3a4d3-0x00a3a94e addr=0xfffffe0007a3e4d3-0xfffffe0007a3e94e               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x000024b8 off=0x03303ef0-0x033063a8 addr=0xfffffe000a307ef0-0xfffffe000a30a3a8 r-x/r-x   __TEXT_EXEC       
	sz=0x000022f8 off=0x03303ef0-0x033061e8 addr=0xfffffe000a307ef0-0xfffffe000a30a1e8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001c0 off=0x033061e8-0x033063a8 addr=0xfffffe000a30a1e8-0xfffffe000a30a3a8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x04a14770-0x04a14898 addr=0xfffffe000ba18770-0xfffffe000ba18898 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a14770-0x04a14838 addr=0xfffffe000ba18770-0xfffffe000ba18838               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000ba18838-0xfffffe000ba18898               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000f00 off=0x013cde40-0x013ced40 addr=0xfffffe00083d1e40-0xfffffe00083d2d40 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x013cde40-0x013cde50 addr=0xfffffe00083d1e40-0xfffffe00083d1e50         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x013cde50-0x013cde60 addr=0xfffffe00083d1e50-0xfffffe00083d1e60         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000d48 off=0x013cde60-0x013ceba8 addr=0xfffffe00083d1e60-0xfffffe00083d2ba8         __DATA_CONST.__const            
	sz=0x00000080 off=0x013ceba8-0x013cec28 addr=0xfffffe00083d2ba8-0xfffffe00083d2c28         __DATA_CONST.__kalloc_type      
	sz=0x000000e0 off=0x013cec28-0x013ced08 addr=0xfffffe00083d2c28-0xfffffe00083d2d08         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000038 off=0x013ced08-0x013ced40 addr=0xfffffe00083d2d08-0xfffffe00083d2d40         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 63 at 0x04af5d28
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     C487F47D-C957-330B-BA0A-E4E62DC01F80
008: LC_SOURCE_VERSION           400.36.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac3dd8 size=0x78
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleExecutable`: `IOPAudioPCMAssetManagerDevice`
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioPCMAssetManagerDevice`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOPAudioPCMAssetManagerDevice`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOPAudioPCMAssetManagerDevice.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895078128`
- `_PrelinkExecutableRelativePath`: `IOPAudioPCMAssetManagerDevice`
- `_PrelinkExecutableSize`: `18718`
- `_PrelinkExecutableSourceAddr`: `-2198895078128`
- `_PrelinkKmodInfo`: `-2198828120208`

## Strings (49) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `assetBufferSize <= kMaximumSizeOfPCMResourceData`
- `!((resourceID) == nullptr)`
- `!((audioSampleRate) == nullptr)`
- `/Library/Caches/com.apple.xbs/20732553-D3E1-4B38-B5F5-87A23D935C9E/TemporaryDirectory.oCjbCa/Sources/IOPAudioDrivers/src/kext/PCMAssetManagerDevice/UserClient/PCMAssetManagerDeviceUserClient.cpp`
- `!((mDevice) == nullptr)`
- `ret = mAssetResourceData->prepare(kIODirectionInOut) == 0 `
- `IOUserClientDefaultLockingSetProperties`
- `!((inArguments) == nullptr)`
- `ret = super::_configure(inProvider) == 0 `
- `!((inRequest) == nullptr)`
- `audioSampleData->getLength() > 0`
- `ret = inNodeInterface->setNodeProperty({ .propertyID = kAssetPropertyID, .data = inData, .dataSize = inDataSize, }) == 0 `
- `IOPAudioPCMAssetManagerDeviceUserClient`
- `site.IOPAudioPCMAssetManagerDeviceUserClient`
- `IOUserClient::initWithTask(inOwningTask, inSecurityToken, inType, inProperties)`
- `/Library/Caches/com.apple.xbs/20732553-D3E1-4B38-B5F5-87A23D935C9E/TemporaryDirectory.oCjbCa/Sources/IOPAudioDrivers/src/kext/PCMAssetManagerDevice/PCMAssetManagerDevice.cpp`
- `ret = Helper::processPCMAssetUpdateRequest( getNodeInterface(), inRequest, Helper::PCMResourceVariant::version2) == 0 `
- `!((audioSampleData) == nullptr)`
- `!((mMemoryResourceData) == nullptr)`
- `!((resourceData) == nullptr)`
- `IOPAudioPCMAssetManagerDevice`
- `!((audioBitDepth) == nullptr)`
- `!((packetWrapper) == nullptr)`
- `!((inData) == nullptr)`
- `IOPAudio::PCMAssetManagerDevice::Helper`
- `entitlement == kOSBooleanTrue`
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `!((userClient) == nullptr)`
- `!((userClient->mDevice) == nullptr)`
- `!((inArguments->scalarOutput) == nullptr)`
- `!((aopInternalDataPacket) == nullptr)`
- `12111112122212121111212`
- `ret = inNodeInterface->setNodeProperty({ .propertyID = kAssetPropertyID, .data = packetWrapper, .dataSize = totalPacketSize, }) == 0 `
- `com.apple.private.aea.haptics.user-access`
- `1211111212221212111111111111111`
- `super::start(inProvider)`
- `!((ioMemory) == nullptr)`
- `assetBufferSize > 0`
- `ret = userClient->mDevice->getNumberOfSupportedAssets(numAssets) == 0 `
- `site.IOPAudioPCMAssetManagerDevice`
- `/Library/Caches/com.apple.xbs/20732553-D3E1-4B38-B5F5-87A23D935C9E/TemporaryDirectory.oCjbCa/Sources/IOPAudioDrivers/src/kext/PCMAssetManagerDevice/PCMAssetManagerDeviceHelper.cpp`
- `!((mAssetResourceData) == nullptr)`
- `IOPAudio::PCMAssetManagerDevice::UserClient`
- `!((resourceType) == nullptr)`
- `resourceType->unsigned32BitValue() == static_cast<uint32_t>(ResourceType::PCM)`
- `mDevice->open(this)`
- `IOUserClientDefaultLocking`
- `IOUserClientEntitlements`

**[__TEXT.__os_log]**

- `%s: %s, %s file: %s, line: %d\n`
