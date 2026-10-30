# `com.apple.driver.IOPAudioLPMicDevice`

- Name: IOPAudioLPMicDevice
- Version: `400.36`
- UUID: `8B664857-EBAD-35EE-92AF-26BAE0B5EBEC`
- Source version: `400.36.0.0.0`
- Depends on: [`com.apple.driver.IOPAudioClientManagerDevice`](com.apple.driver.IOPAudioClientManagerDevice.md) 1.0, [`com.apple.iokit.IOPAudioDriverFamily`](com.apple.iokit.IOPAudioDriverFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/iop-audio-controller/lp-mic-device`](../devicetree/root__arm-io__iop-audio-controller__lp-mic-device.md) | `IOPAudioLPMicDevice` | `iop-audio,lp-mic-device` |

## IOKit personalities (1) [KC]

### IOPAudioLPMicDevice
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioLPMicDevice`
- `IOClass`: `IOPAudioLPMicDevice`
- `IONameMatch`:
  - `iop-audio,lp-mic-device`
- `IOPersonalityPublisher`: `com.apple.driver.IOPAudioLPMicDevice`
- `IOProviderClass`: `IOPAudioNode`
- `IOUserClientClass`: `IOPAudioLPMicDeviceUserClient`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOPAudioLPMicDevice` | 0x2f0 | IOPAudioClientManagerDevice → IOPAudioDevice → IOService → IORegistryEntry |
| `IOPAudioLPMicDeviceUserClient` | 0xe8 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00002b61 off=0x00a369a0-0x00a39501 addr=0xfffffe0007a3a9a0-0xfffffe0007a3d501 r--/r--   __TEXT            
	sz=0x00000008 off=0x00a37068-0x00a37070 addr=0xfffffe0007a3b068-0xfffffe0007a3b070               __TEXT.__const            
	sz=0x000018a0 off=0x00a37070-0x00a38910 addr=0xfffffe0007a3b070-0xfffffe0007a3c910               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000bf1 off=0x00a38910-0x00a39501 addr=0xfffffe0007a3c910-0xfffffe0007a3d501               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00004a08 off=0x032ff4e0-0x03303ee8 addr=0xfffffe000a3034e0-0xfffffe000a307ee8 r-x/r-x   __TEXT_EXEC       
	sz=0x000048c8 off=0x032ff4e0-0x03303da8 addr=0xfffffe000a3034e0-0xfffffe000a307da8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000140 off=0x03303da8-0x03303ee8 addr=0xfffffe000a307da8-0xfffffe000a307ee8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000130 off=0x04a14640-0x04a14770 addr=0xfffffe000ba18640-0xfffffe000ba18770 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a14640-0x04a14708 addr=0xfffffe000ba18640-0xfffffe000ba18708               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000ba18708-0xfffffe000ba18768               __DATA.__common           (Zerofill)
	sz=0x00000008 off=0x00000000-0x00000008 addr=0xfffffe000ba18768-0xfffffe000ba18770               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001010 off=0x013cce30-0x013cde40 addr=0xfffffe00083d0e30-0xfffffe00083d1e40 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x013cce30-0x013cce40 addr=0xfffffe00083d0e30-0xfffffe00083d0e40         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x013cce40-0x013cce50 addr=0xfffffe00083d0e40-0xfffffe00083d0e50         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000e70 off=0x013cce50-0x013cdcc0 addr=0xfffffe00083d0e50-0xfffffe00083d1cc0         __DATA_CONST.__const            
	sz=0x00000080 off=0x013cdcc0-0x013cdd40 addr=0xfffffe00083d1cc0-0xfffffe00083d1d40         __DATA_CONST.__kalloc_type      
	sz=0x000000a0 off=0x013cdd40-0x013cdde0 addr=0xfffffe00083d1d40-0xfffffe00083d1de0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000060 off=0x013cdde0-0x013cde40 addr=0xfffffe00083d1de0-0xfffffe00083d1e40         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 52 at 0x04af5c58
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     8B664857-EBAD-35EE-92AF-26BAE0B5EBEC
008: LC_SOURCE_VERSION           400.36.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac3cf8 size=0xe0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleExecutable`: `IOPAudioLPMicDevice`
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioLPMicDevice`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOPAudioLPMicDevice`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOPAudioLPMicDevice.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895089248`
- `_PrelinkExecutableRelativePath`: `IOPAudioLPMicDevice`
- `_PrelinkExecutableSize`: `34473`
- `_PrelinkExecutableSourceAddr`: `-2198895089248`
- `_PrelinkKmodInfo`: `-2198828120512`

## Strings (112) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `ret = userClient->mDevice->startIO() == 0 `
- `com.apple.private.aop-audio.user-access`
- `ret = setIORegistryProperty(this, streamDescriptor) == 0 `
- `ret = inNodeInterface->getNodeProperty(propertyDescriptor) == 0 `
- `ret = setIntegerValue(streamDescription, IORegistryKey::Stream::kFormatFlags, inStreamDescriptor.formatFlags) == 0 `
- `mDevice->open(this, 0, &clientID)`
- `ret = userClient->mDevice->stopIO() == 0 `
- `ret = super::_configure(inProvider) == 0 `
- `ret = retrieveDeviceInfoFromIOP(nodeInterface, deviceInfo) == 0 `
- `IOPAudioLPMicDevice`
- `handleIOPMessage`
- `ret = (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2cf) == 0 `
- `!((registryEntry) == nullptr)`
- `inStreamDescription.isAlignedLow()`
- `inMessage.getMessageType() == IOPAudio::IOPMessage::Type::kReport`
- `ret = inNodeInterface->getNodeProperty(latencyProperty) == 0 `
- `remainingPayloadSize == targetPacket->payloadSize`
- `sample rate`
- `bytes per frame`
- `IOUserClientDefaultLockingSetProperties`
- `!((outOptions) == nullptr)`
- `/Library/Caches/com.apple.xbs/20732553-D3E1-4B38-B5F5-87A23D935C9E/TemporaryDirectory.oCjbCa/Sources/IOPAudioDrivers/src/kext/LPMicDevice/LPMicDevice.cpp`
- `!(isSuspended())`
- `ret = getPropertyDataFromIORegistryPath( gIODTPlane, kPath, IORegistry::kEnabledChannelsKey, outChannelControl.enabledChannels) == 0 `
- `ret = setIntegerValue( inRegistryEntry, IORegistryKey::kIOFrameBufferWrapSize, inDeviceInfo.frameBufferWrapSize) == 0 `
- `ret = setIntegerValue(inRegistryEntry, IORegistryKey::kClockDomain, inDeviceInfo.clockDomain) == 0 `
- `ret = setIntegerValue(streamDescription, IORegistryKey::Stream::kBitsPerChannel, inStreamDescriptor.bitsPerChannel) == 0 `
- `!((kRemoteIOStatus) == nullptr)`
- `bits per channel`
- `!((inRegistryEntry) == nullptr)`
- `!((inPath) == nullptr)`
- `inStreamDescription.isLittleEndian()`
- `ret = setIntegerValue(streamDescription, IORegistryKey::Stream::kSafetyOffset, inStreamDescriptor.safetyOffset) == 0 `
- `!((localIOStatus) == nullptr)`
- `io buffer frame size`
- `driver safety offset in frames`
- `!((dataPtr) == nullptr)`
- `ret = PrivateAPI::handleIOAudio2StatusPacket(inMessage, propertyChangePacket->payloadSize, propertyChangePacket->payload, mAudioEngineInputStatus) == 0 `
- `!((mAudioEngineInputStatus) == nullptr)`
- `ret = inNodeInterface->getNodeProperty(streamInfoProperty) == 0 `
- `clock domain`
- `!((inDictionary) == nullptr)`
- `IOUserClient::initWithTask(inOwningTask, inSecurityToken, inType, inProperties)`
- `IOUserClientDefaultLocking`
- `IOUserClientEntitlements`
- `ret = retrieveInputStreamDescriptorFromIOP(nodeInterface, streamDescriptor) == 0 `
- `/Library/Caches/com.apple.xbs/20732553-D3E1-4B38-B5F5-87A23D935C9E/TemporaryDirectory.oCjbCa/Sources/IOPAudioDrivers/src/kext/LPMicDevice/LPMicDeviceHelpers.cpp`
- `ret = getPropertyDataFromIORegistryPath( gIODTPlane, kPath, IORegistry::kSupportedChannelsKey, outChannelControl.supportedChannels) == 0 `
- `ret = inNodeInterface->setNodeProperty(propertyDescriptor) == 0 `
- `input stream description`
- `site.IOPAudioLPMicDeviceUserClient`
- `ret = mDevice->getClientMemoryForType(inType, *outOptions, memoryDescriptor) == 0 `
- `!((userClient) == nullptr)`
- `ret = PrivateAPI::sendChannelControlInfoToIOP(nodeInterface, mChannelControl) == 0 `
- `isIORunning()`
- `ret = getPropertyDataFromIORegistryPath( gIODTPlane, kPath, IORegistry::kHistoryChannelsKey, outChannelControl.historyChannels) == 0 `
- `ret = setIntegerValue(streamDescription, IORegistryKey::Stream::kBytesPerFrame, inStreamDescriptor.bytesPerFrame) == 0 `
- `channels per frame`
- `/Library/Caches/com.apple.xbs/20732553-D3E1-4B38-B5F5-87A23D935C9E/TemporaryDirectory.oCjbCa/Sources/IOPAudioDrivers/src/kext/LPMicDevice/LPMicDeviceHelpers.hpp`
- `!((outMemory) == nullptr)`
- `!((userClient->mDevice) == nullptr)`
- `ret = setIntegerValue( inRegistryEntry, IORegistryKey::kIOFrameBufferSize, inDeviceInfo.frameBufferSize) == 0 `
- `ret = setIntegerValue(streamDescription, IORegistryKey::Stream::kLatency, inStreamDescriptor.latency) == 0 `
- `!((inArguments->scalarOutput) == nullptr)`
- `ret = userClient->mDevice->setControl(inArguments->scalarInput[0], inArguments->scalarInput[1]) == 0 `
- `IOPAudio::LPMicDevice::UserClient`
- `site.IOPAudioLPMicDevice`
- `1211111212221212111122221111111111111111111111111111111111111111111111111111111111111111212221`
- `ret = enableClientManager(true, kIODirectionIn, kDefaultClientID) == 0 `
- `ret = setBooleanValue( inRegistryEntry, IORegistryKey::kHistoricDataSupported, inDeviceInfo.supportsHistorical) == 0 `
- `supportedChannels`
- `historyChannels`
- `historic data supported`
- `entitlement == kOSBooleanTrue`
- `ret = PrivateAPI::retrieveChannelControlInfoFromDT(mChannelControl) == 0 `
- `i8@?0`
- `sizeof(IOPStatusType) == inDataSize`
- `/product/audio`
- `!((inArguments->scalarInput) == nullptr)`
- `inRegistryEntry->setProperty(inKey, valueObject)`
- `ret = processStreamDescription(currentConfig, outStreamDescriptor.formatFlags) == 0 `
- `remainingPayloadSize >= sizeof(EventPacket)`
- `/Library/Caches/com.apple.xbs/20732553-D3E1-4B38-B5F5-87A23D935C9E/TemporaryDirectory.oCjbCa/Sources/IOPAudioDrivers/src/kext/LPMicDevice/UserClient/LPMicDeviceUserClient.cpp`
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `ret = (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2c7) == 0 `
- `!(inStreamDescription.isSignedInt())`
- `inDictionary->setObject(inKey, valueObject.get())`
- `super::start(inProvider)`
- `!((inArguments) == nullptr)`
- `ret = userClient->mDevice->getControl(inArguments->scalarInput[0], inArguments->scalarOutput[0]) == 0 `
- `!((valueObject) == nullptr)`
- `ret = setIntegerValue(streamDescription, IORegistryKey::Stream::kSampleRate, inStreamDescriptor.sampleRate) == 0 `
- `ret = setIntegerValue(streamDescription, IORegistryKey::Stream::kChannelsPerFrame, inStreamDescriptor.channelsPerFrame) == 0 `
- `inRegistryEntry->setProperty(IORegistryKey::kInputStreamDescription, streamDescription.get())`
- `enabledChannels`
- `zero timestamp wrap frames`
- `format flags`
- `latency in frames`
- `ret = super::_retrieveConfig(inProvider, ioConfig) == 0 `
- `!((inKey) == nullptr)`
- `ret = inNodeInterface->getNodeProperty(safetyOffsetProperty) == 0 `
- `remainingPayloadSize >= sizeof(PropertyChangeEventPacket)`
- `inRegistryEntry->setProperty(inKey, valueObject.get())`
- `IOPAudioLPMicDeviceUserClient`
- `12111112122212121111111111111`
- `!((mDevice) == nullptr)`
- `ret = setIORegistryProperty(this, deviceInfo) == 0 `
- `!((propertyChangePacket) == nullptr)`
- `inStreamDescription.isSignedInt()`
- `ret = inMessage.iopTimeToAbsolute(kRemoteIOStatus->mInputHostTime, convertedHostTime) == 0 `

**[__TEXT.__os_log]**

- `%s: %s, %s file: %s, line: %d\n`
- `%s::%s(..) unexpected property ID (%#x) received `
