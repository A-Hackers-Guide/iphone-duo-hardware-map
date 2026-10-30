# `com.apple.driver.AppleEmbeddedAudioLibs`

- Name: AppleEmbeddedAudioLibs
- Version: `600.6`
- UUID: `F3443710-FBC3-32BA-AEB7-A16FE585294E`
- Source version: `600.6.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleAudioClockLibs`](com.apple.driver.AppleAudioClockLibs.md) 1.0, [`com.apple.driver.AppleFirmwareUpdateKext`](com.apple.driver.AppleFirmwareUpdateKext.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (5) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleAudioFirmwareDownloader` | 0xc0 | IOService → IORegistryEntry |
| `AppleExternalPowerManager` | 0x20 |  |
| `AppleExternalPowerProvider` | 0x38 |  |
| `AudioDeviceCommandFunction` | 0x30 | AppleARMFunction |
| `AudioKernelClientInterface` | 0xa8 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00005a8a off=0x00440370-0x00445dfa addr=0xfffffe0007444370-0xfffffe0007449dfa r--/r--   __TEXT            
	sz=0x00000010 off=0x004409e8-0x004409f8 addr=0xfffffe00074449e8-0xfffffe00074449f8               __TEXT.__const            
	sz=0x00003073 off=0x004409f8-0x00443a6b addr=0xfffffe00074449f8-0xfffffe0007447a6b               __TEXT.__os_log           
	sz=0x0000238f off=0x00443a6b-0x00445dfa addr=0xfffffe0007447a6b-0xfffffe0007449dfa               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x0000dc48 off=0x01c1aa10-0x01c28658 addr=0xfffffe0008c1ea10-0xfffffe0008c2c658 r-x/r-x   __TEXT_EXEC       
	sz=0x0000d828 off=0x01c1aa10-0x01c28238 addr=0xfffffe0008c1ea10-0xfffffe0008c2c238          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000420 off=0x01c28238-0x01c28658 addr=0xfffffe0008c2c238-0xfffffe0008c2c658          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000278 off=0x0493e890-0x0493eb08 addr=0xfffffe000b942890-0xfffffe000b942b08 rw-/rw-   __DATA            
	sz=0x000001a0 off=0x0493e890-0x0493ea30 addr=0xfffffe000b942890-0xfffffe000b942a30               __DATA.__data             
	sz=0x000000d8 off=0x00000000-0x000000d8 addr=0xfffffe000b942a30-0xfffffe000b942b08               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000014d0 off=0x0107b318-0x0107c7e8 addr=0xfffffe000807f318-0xfffffe00080807e8 rw-/rw-   __DATA_CONST      
	sz=0x00000020 off=0x0107b318-0x0107b338 addr=0xfffffe000807f318-0xfffffe000807f338         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000020 off=0x0107b338-0x0107b358 addr=0xfffffe000807f338-0xfffffe000807f358         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000fc0 off=0x0107b358-0x0107c318 addr=0xfffffe000807f358-0xfffffe0008080318         __DATA_CONST.__const            
	sz=0x00000200 off=0x0107c318-0x0107c518 addr=0xfffffe0008080318-0xfffffe0008080518         __DATA_CONST.__kalloc_type      
	sz=0x00000210 off=0x0107c518-0x0107c728 addr=0xfffffe0008080518-0xfffffe0008080728         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000c0 off=0x0107c728-0x0107c7e8 addr=0xfffffe0008080728-0xfffffe00080807e8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 156 at 0x04ad82b8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     F3443710-FBC3-32BA-AEB7-A16FE585294E
008: LC_SOURCE_VERSION           600.6.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9ec20 size=0x220
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleEmbeddedAudioLibs`
- `CFBundleGetInfoString`: `Copyright © 2024 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudioLibs`
- `CFBundleInfoDictionaryVersion`: `1.0`
- `CFBundleName`: `AppleEmbeddedAudioLibs`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `600.6`
- `CFBundleSignature`: `aapl`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `600.6`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleEmbeddedAudioLibs.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901341328`
- `_PrelinkExecutableRelativePath`: `AppleEmbeddedAudioLibs`
- `_PrelinkExecutableSize`: `85530`
- `_PrelinkExecutableSourceAddr`: `-2198901341328`
- `_PrelinkKmodInfo`: `-2198828996464`

## Strings (323) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `%s::%s() super::start() failed`
- `%s::%s(inProvider=%p) END [providerName: %s]`
- `%s::%s(inRequestFUDNewFirmwareIfNotPending=%d) dynamic reloading isn't supported.`
- `%s inStartAddress cannot nullptr [errorCode: 0x%x]`
- `%s::%s(%p) registerPowerDriver failed result=0x%x`
- `%s::%s(inClient=%p, inRequests=%p) client provider refused to start the session [errorCode: 0x%x]`
- `%s [%u] invalid parameter, inName=%p`
- `AppleExternalPowerProvider::%s(inService=%s[%p], _externalPowerProvider=%p) [Owner=%s, externalPowerProvider=%s, _externalPowerProviderPowerFlags=0x%lx`
- `%s::%s Skipping firmware image validation`
- `%s::%s Unknown validation status %u. Image loading not permitted`
- `AppleExternalPowerProvider::init(inOwner=%s, inExternalPowerProvider=%s) registered external power provider getState=0x%x pwrFlags=0x%lx`
- `%s::%s unable to create IOTimerEventSource`
- `%s inSampleRate cannot nullptr [errorCode: 0x%x]`
- `AudioKernelClientInterfaceUtility::%s unable to create OSDictionary`
- `%s::%s Unable to validate firmware image`
- `AudioKernelClientInterface::%s unable to create handler ref`
- `AudioKernelClientInterface::%s client cannot be nullptr`
- `%s::%s [powerProvider=%s, _externalPowerStatePendingAck=%u, _externalPowerProviderPowerOn=%u] [ errorCode : 0x%x ]`
- `%s::%s(inValidationStatus=%d) START [providerName: %s]`
- `%s inData cannot nullptr [errorCode: 0x%x]`
- `AudioKernelClientInterface::%s unable to create matching dictionary`
- `%s CreateRequestDictionary returned nullptr [errorCode: 0x%x]`
- `%s inPCMResourceID cannot nullptr [errorCode: 0x%x]`
- `%s failed to initialize an AppleExternalPowerManager object`
- `%s [%u] unable to wait for matching service=%s`
- `AudioKernelClientInterface::%s(%s) init failed [errorCode : 0x%x]`
- `AppleAudioFirmwareDownloader::%s(%s) init failed [errorCode : 0x%x]`
- `%s ioClientRequest cannot nullptr [errorCode: 0x%x]`
- `%s::%s(...) unable to allocate AppleExternalPowerProvider object`
- `%s::%s() - ExternalPowerProvider : %s powered %s [%d/%d]\n`
- `%s::%s [powerProvider=%s, _externalPowerStatePendingAck=%u, _externalPowerProviderPowerOn=%u]`
- `AppleAudioFirmwareDownloader::%s(%s) start failed [errorCode : 0x%x]`
- `AudioKernelClientInterface::%s failed to register client`
- `%s::%s inClient is nullptr [errorCode: 0x%x]`
- `%s::%s(inClient=%p, inRequests=%p) failed [errorCode: 0x%x]`
- `%s::%s(...) invalid parameter.`
- `AudioKernelClientInterfaceUtility::%s(inRequest=%p, inResult=0x%x) failed due to bad arguments.`
- `AudioKernelClientInterfaceUtility::%s(inRequestIndex=%u) requestCount=%u`
- `%s [%u] unable to create function dictionary`
- `AudioKernelClientInterfaceUtility::%s(inData=%p) failed due to bad arguments.`
- `%s inRegisterData cannot nullptr [errorCode: 0x%x]`
- `AudioKernelClientInterface::%s serviceMatchingDictionary cannot be nullptr`
- `AudioKernelClientInterface::%s(%s) unable to allocate AudioKernelClientInterface`
- `%s::%s Unable allocate AppleFirmwareUpdateKext`
- `%s: %s, %s file: %s, line: %d\n`
- `AudioKernelClientInterfaceUtility::%s(inRequest=%p) failed due to bad arguments.`
- `%s(propeinPropertyID=0x%llx) failed [kernResult=0x%x]`
- `%s [%u] invalid parameter inProvider=%p`
- `AudioKernelClientInterfaceHelper::%s inClientInterfaceName cannot be nullptr`
- `%s::%s(%p) Unexpected error encountered`
- `%s::%s(inClient=%p) clientIterator is nullptr [errorCode: 0x%x]`
- `AudioKernelClientInterfaceUtility::%s(inRequestType=%p, inIsInternalProperty=%d) unable to allocate OSDictionary`
- `AudioKernelClientInterface::%s matchingInterface is not an AudioKernelClientInterface`
- `AudioKernelClientInterfaceUtility::%s unable to create matching dictionary`
- `%s::%s() unable to set the result`
- `%s::%u dataEntry for key=%s doesn't exist`
- `%s::%s(inValidationStatus=%d) END [providerName: %s]`
- `AudioKernelClientInterface::%s(%s) start failed [errorCode : 0x%x]`
- `AppleExternalPowerProvider::%s(inOwner=%p, inExternalPowerProvider%p) [%u] failed to allocate AppleExternalPowerProvider`
- `AppleAudioFirmwareDownloader::%s(%s) attach failed [errorCode : 0x%x]`
- `%s::%s(inRequestFUDNewFirmwareIfNotPending=%d) firmware data has already been consumed.`
- `%s::%s(inValidationStatus=%d) Failed to load firmware data [providerName: %s, errorCode: 0x%x]`
- `%s inBitDepth cannot nullptr [errorCode: 0x%x]`
- `%s inPropertyID cannot nullptr [errorCode: 0x%x]`
- `* %s::%s [powerProvider=%s] %s\n`
- `%s unable to create OSData [errorCode:0x%x]`
- `%s::%s(inClient=%p, inRequests=%p) unable to create request dict`
- `%s::%s Unable to init AppleFirmwareUpdateKext`
- `%s unable to create OSNumber [errorCode:0x%x]`
- `AudioKernelClientInterface::%s inNotificationHandler cannot be nullptr`
- `%s::%s failed to acknowledgePowerOffRequest for %s`
- `%s::%s(...) failed to add powerProvider to the list`
- `%s::%s [%u]`
- `AudioKernelClientInterface::%s unable to retrieve matching interface`
- `%s invalid paramter (inOwner==nullptr)`
- `AudioKernelClientInterface::%s handlerRef cannot be nullptr`
- `%s [%u] invalid parameter, inServicePHandles=%p`
- `%s::%s(%p) super::init(..) failed`
- `%s::%s(inClient=%p, inRequests=%p) unable to create OSIterator [errorCode: 0x%x]`
- `%s inAudioSamples cannot nullptr [errorCode: 0x%x]`
- `AudioKernelClientInterfaceUtility::%s(inRequestType=%p, inIsInternalProperty=%d) Invalid property ID (0x%llx)`
- `%s [%u] invalid parameter, inProvider=%p`
- `AudioKernelClientInterface::%s clientInterface cannot be nullptr`
- `%s inRegisterCount cannot nullptr [errorCode: 0x%x]`
- `%s Unable to create OSNumber[errorCode: 0x%x]`
- `%s::%s(inDevice=%s) %x\n`
- `%s::%s [powerProvider=%s, _externalPowerStatePendingAck=%u, _externalPowerProviderPowerOn=%u -> %u]`
- `AudioKernelClientInterfaceUtility::%s(inRequest=%p) failed due to missing result key.`
- `%s unable to create qualifier OSData [errorCode:0x%x]`
- `AudioKernelClientInterfaceUtility::%s(inClientRequest=%p) client request cannot be nullptr`
- `AppleExternalPowerProvider::%s(inOwner=%p, inExternalPowerProvider%p) [%u] failed to init`
- `AppleAudioFirmwareDownloader::%s(%s) unable to allocate AudioKernelClientInterface`
- `%s::%s (inDevice=%p). invalid parameter.`
- `%s::%s (inDevice=%s, isOwnerDevicePoweredOn=%d) deferral=%d ms`
- `%s::%s(inClient=%p, inRequests=%p) device is offline`
- `%s::%s() non-AppleExternalPowerProvider object was stored in the powerProviderList`
- `%s::%s() [ deviceCount=%u, poweredOffDevices=%u]`
- `%s::%s Unable to attach AppleFirmwareUpdateKext`
- `%s::%s(inValidationStatus=%d) Releasing existing firmwareData [providerName: %s]`
- `%s::%s(%p) unable to allocate OSArray`
- `%s::%s(inClient=%p) client is registered already [errorCode: 0x%x]`
- `AppleExternalPowerProvider::init(inOwner=%s, inExternalPowerProvider=%s) externalPowerProvider isn't registered with power management.  Will re-register once it is ready.`
- `AudioKernelClientInterface::%s inClient cannot be nullptr`
- `%s failed to allocate an AppleExternalPowerManager object`
- `%s::%s Unexpected error encountered. Firmware data is nullptr. (validationStatue = %u)`
- `AudioKernelClientInterfaceUtility::%s(inRequestIndex=%u) unable to find request`
- `%s [%u] unable to allocate OSArray`
- `%s::%s(%p) unable to allocate IOLock`
- `%s::%s(inClient=%p, inRequests=%p) request is nullptr [errorCode: 0x%x]`
- `%s::%s [powerProvider=%s, _externalPowerStatePendingAck=%u-> 1, _externalPowerProviderPowerOn=%u]`
- `AudioKernelClientInterfaceUtility::%s(inRequestType=%p, inIsInternalProperty=%d) inRequestType cannot be nullptr`
- `AudioKernelClientInterface::%s(%s) attach failed [errorCode : 0x%x]`
- `%s::%s(inProvider=%p) START [providerName: %s]`
- `AudioKernelClientInterfaceUtility::%s unable to create OSSymbol`
- `* %s::%s [powerProvider=%p] failed [errorCode : 0x%x]\n`
- `AppleExternalPowerProvider::%s (inOwner=%p, inExternalPowerProvider=%p) [%u] ERROR: invalid parameters`

**[__TEXT.__cstring]**

- `-restore`
- `dataEntryData->getLength() > 0`
- `dataBlockMapEntryArrayRef.size() > 0`
- `key != nullptr`
- `propertyNameLength < remainingSize`
- `dataCountNumber != nullptr`
- `handleDevicePowerOnNotification`
- `acknowledgePowerOffRequest`
- `inData != nullptr`
- `AppleExternalPowerManager.cpp`
- `/Library/Caches/com.apple.xbs/4A7BEDE5-9B26-458A-A57C-41E800524322/TemporaryDirectory.0HNr2v/Sources/AppleAudioKextLibs/src/kext/AppleEmbedAudioLibs/AppleAudioDeviceCommandFunction/AudioDeviceCommandFunctionUtility.cpp`
- `!((inData) == nullptr)`
- `_firmwareDownloadCallbackHandler`
- `%s::%s Unexpected error encountered. Firmware data is nullptr. (validationStatue = %u)\n`
- `static IOArrayIndex AudioKernelClientInterfaceUtility::AppendSetPropertyRequest(OSSharedPtr<OSArray> &, OSNumber *, OSObject *, OSObject *)`
- `StartAddress`
- `ret = setObject(inDictionary, inKey, stringObject.get()) == 0 `
- `RegisterAudioKernelInterfaceMatchingNotification`
- `1211221`
- `%s::%s(inRequestFUDNewFirmwareIfNotPending=%d) firmware data has already been consumed.\n`
- `GetAccessType`
- `static IOArrayIndex AudioKernelClientInterfaceUtility::AppendRegisterWriteRequest(OSSharedPtr<OSArray> &, OSNumber *, OSData *)`
- `!((inDictionary) == nullptr)`
- `site.AudioKernelClientInterface`
- `CreateMatchingDictionary`
- `static OSSharedPtr<AppleExternalPowerManager> AppleExternalPowerManager::withCapacity(IOService *, UInt32)`
- `site.AppleExternalPowerProvider`
- `AppleAudioFirmwareDownloader`
- `%s::%s(%p) Unexpected error encountered\n`
- `SetResult`
- `121111`
- `registerClient`
- `recoveryos`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `121111121222121212112111`
- `GetResourceType`
- `!((inObject) == nullptr)`
- `dataMapEntryArray != nullptr`
- `GetLoopCount`
- `static IOArrayIndex AudioKernelClientInterfaceUtility::AppendFWResourceWriteRequest(OSSharedPtr<OSArray> &, OSNumber *, OSData *)`
- `static IOArrayIndex AudioKernelClientInterfaceUtility::AppendGetPropertyRequest(OSSharedPtr<OSArray> &, UInt64, IOByteCount, void *)`
- `LoopCount`
- `/Library/Caches/com.apple.xbs/4A7BEDE5-9B26-458A-A57C-41E800524322/TemporaryDirectory.0HNr2v/Sources/AppleAudioKextLibs/AudioConfigDataHelper.cpp`
- `OSBoundedPtr.h`
- `static IOArrayIndex AudioKernelClientInterfaceUtility::AppendSetPropertyRequest(OSSharedPtr<OSArray> &, UInt64, IOByteCount, const void *, IOByteCount, void *)`
- `The offset of the pointer inside its valid memory range can't be represented using int32_t`
- `Off`
- `withExternalPowerProvider`
- `!((inFunction) == nullptr)`
- `AppleAudioFirmwareDownloader::%s(%s) unable to allocate AudioKernelClientInterface\n`
- `SetData`
- `ret = theFunction->validate() == 0 `
- `121111121222121211111`
- `inDataSize > 0`
- `inRegistryEntry->setProperty(inPropertyKey, inObject)`
- `GetData`
- `static IOArrayIndex AudioKernelClientInterfaceUtility::AppendRegisterReadRequest(OSSharedPtr<OSArray> &, OSNumber *, OSNumber *)`
- `static IOArrayIndex AudioKernelClientInterfaceUtility::AppendSetPropertyRequest(OSSharedPtr<OSArray> &, UInt64, OSObject *, OSObject *)`
- `AssetType`
- `!((inBlock) == nullptr)`
- `!((mHostConfig.commandAction) == nullptr)`
- `ID`
- `AppleAudioFirmwareDownloader::%s(%s) attach failed [errorCode : 0x%x]\n`
- `CreateInterfaceWithOwner`
- `static OSSharedPtr<AudioKernelClientInterface> AudioKernelClientInterface::CreateInterfaceWithOwner(IOService *, const OSString *, IOWorkLoop::Action)`
- `inDataBlockMapList != nullptr`
- `!((propertyData) == nullptr)`
- `CreateAudioFirmwareDownloader`
- `RequestType`
- `IsWriteRequest`
- `site.AudioDeviceCommandFunction`
- `%s-%u`
- `AudioDeviceCommandFunction::Utility`
- `GetPreSilenceFrameCount`
- `static IOArrayIndex AudioKernelClientInterfaceUtility::AppendPCMResourceWriteRequest(OSSharedPtr<OSArray> &, OSNumber *, OSNumber *, OSNumber *, OSData *, OSNumber *, OSNumber *, OSNumber *)`
- `destinationEntry != nullptr`
- `AppleExternalPowerManager`
- `/Library/Caches/com.apple.xbs/4A7BEDE5-9B26-458A-A57C-41E800524322/TemporaryDirectory.0HNr2v/Sources/AppleAudioKextLibs/src/kext/AppleEmbedAudioLibs/IORegistryEntryHelper/AudioKextIORegistryHelper.cpp`
- `!((outData) == nullptr)`
- `inIORegistryPath != nullptr`
- `GetQualifierData`
- `GetRequestResult`
- `init`
- `Length`
- `site.AppleExternalPowerManager`
- `On`
- `GetFailedRequestIndices`
- `!((inKey) == nullptr)`
- `matchingNotificationHandlerGated`
- `!(inDataSize > descriptor.returnData->getLength())`
- `GetResourceID`
- `!((inHostConfig.commandAction) == nullptr)`
- `1`
- `rd`
- `GetStartAddress`
- `osenvironment`
- `1211`
- `getNumberOfPoweredOffExternalDevices`
- `%s::%s Unable to validate firmware image\n`
- `GetResult`
- `CreateRequestDictionary`
- `/chosen`
- `inRegistryEntry->setProperty(inPropertyKey, inValue)`
- `dataBlockMap != nullptr`
- `handleDevicePowerOffNotification`
- `%s::%s Unable allocate AppleFirmwareUpdateKext\n`
- `md0`
- `destinationEntry->setProperty(buffer, dataList->getObject(dataIndex))`
- `already exists`
- `NumberOfRegisters`
- `QualifierData`
- `B24@?0r^{OSSymbol=}8^{OSObject=^^?i}16`
- `!((inString) == nullptr)`
- `AudioDeviceCommandFunction`
- `%s: %s, %s file: %s, line: %d\n\n`
- `dataEntryData->getLength() % sizeof(DataBlockMapEntry) == 0`
- `data != nullptr && data->getBytesNoCopy() != nullptr`
- `propertyPrefixMap->setObject(key, propertyName)`
- `inDataBlockMap != nullptr`
- `AudioKextLibs::AudioConfigDataHelper`
- `Audio::KextLib::IORegistryEntry::Helper`
- `dataEntryData != nullptr`
- `propertyName->getLength() == propertyNameLength`
- `dataListCount > 0`
- `AppleAudioFirmwareDownloader::%s(%s) init failed [errorCode : 0x%x]\n`
- `%s::%s(inValidationStatus=%d) Failed to load firmware data [providerName: %s, errorCode: 0x%x]\n`
- `static IOArrayIndex AudioKernelClientInterfaceUtility::AppendPCMResourceWriteRequest(OSSharedPtr<OSArray> &, UInt32, AudioKernelClientInterfacePCMResourceSampleRate, AudioKernelClientInterfacePCMResourceBitDepth, IOByteCount, const void *, IOByteCount, IOByteCount, IOByteCount)`
- `Offset`
- `ioDataCollectionMap != nullptr`
- `static IOReturn AudioConfigDataHelper::extractDataBlocks(const OSData *, const OSArray *, OSDictionary *, OSArray *)`
- `destinationEntry->setProperty(buffer, dataCountNumber.get())`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `acknowledgeAllPendingPowerOffRequests`
- `_requestFirmwareUpdateCallbackGated`
- `GetRequestType`
- `/Library/Caches/com.apple.xbs/4A7BEDE5-9B26-458A-A57C-41E800524322/TemporaryDirectory.0HNr2v/Sources/AppleAudioKextLibs/src/kext/AppleEmbedAudioLibs/OSDictionaryHelper/AudioKextOSDictionaryHelper.cpp`
- `GetMatchingAudioKernelInterface`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `\"AppleEmbeddedAudio: Invalid size of external-power-provider property [length = %u, pHandleLength = %u, numberOfHandles = %u]\\n\" @%s:%d`
- `AppleAudioFirmwareDownloader::%s(%s) start failed [errorCode : 0x%x]\n`
- `PreSilenceFrames`
- `recovery`
- `kDataEntryKey != nullptr`
- `propertyPrefixMap != nullptr`
- `outMissingDataBlocks->getCount() == 0`
- `propertyPrefix != nullptr`
- `deferPowerOffRequest`
- `!((descriptor.returnData) == nullptr)`
- `%s::%s Unable to attach AppleFirmwareUpdateKext\n`
- `%s%s`
- `propertyNameLength > 0 && kBufferSize > propertyNameLength`
- `static OSSharedPtr<IOService> AppleExternalPowerManager::getARMFunctionProvider(IORegistryEntry *, const char *)`
- `addPowerProvider`
- `ret = inFunction->processCommand(descriptor) == 0 `
- `site.AppleAudioFirmwareDownloader`
- `%s::%s() super::start() failed\n`
- `GetPostSilenceFrameCount`
- `AppleExternalPowerProvider`
- `!(inDataSize < descriptor.returnData->getLength())`
- `%s::%s unable to create IOTimerEventSource\n`
- `static IOArrayIndex AudioKernelClientInterfaceUtility::AppendGetPropertyRequest(OSSharedPtr<OSArray> &, OSNumber *, OSObject *)`
- `Data`
- `inDictionary->setObject(inKey, inObject)`
- `Audio::KextLib::Dictionary::Helper`
- `Product`
- `IOHibernateState`
- `!((inPropertyKey) == nullptr)`
- `offset != nullptr`
- `static OSSharedPtr<OSArray> AppleExternalPowerManager::parsePhandles(OSData *)`
- `updatePowerState`
- `/Library/Caches/com.apple.xbs/4A7BEDE5-9B26-458A-A57C-41E800524322/TemporaryDirectory.0HNr2v/Sources/AppleAudioKextLibs/src/kext/AppleEmbedAudioLibs/AppleAudioDeviceCommandFunction/AudioDeviceCommandFunction.cpp`
- `AudioKernelClientInterface`
- `static OSSharedPtr<AppleAudioFirmwareDownloader> AppleAudioFirmwareDownloader::CreateAudioFirmwareDownloader(IOService *, uint32_t, IOWorkLoop::Action)`
- `%s::%s Unable to init AppleFirmwareUpdateKext\n`
- `%s::%s(inRequestFUDNewFirmwareIfNotPending=%d) dynamic reloading isn't supported.\n`
- `%s::%s Unknown validation status %u. Image loading not permitted\n`
- `GetSampleRate`
- `GetBitDepth`
- `\"%s\" @%s:%d`
- `%c%c%c%c`
- `start`
- `dataMapEntry != nullptr`
- `propertyName != nullptr`
- `kDataMapKey != nullptr`
- `inDataCollectionMap != nullptr`
- `virtual bool AppleExternalPowerManager::init(IOService *, UInt32)`
- `!((symbol) == nullptr)`
- `site.MatchingNotificationHandlerRef`
- `sendRequestGated`
- `length != nullptr`
- `-key-cnt`
- `inPropertyPrefixMap != nullptr`
- ` was added succesfully`
- `%s invalid paramter (inOwner==nullptr)\n`
- `getClientIndexLocked`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `bounded_ptr<T>::discard_bounds: Discarding the bounds on this pointer would lose the fact that it is outside of the bounds set originally`
- `GetRegisterCount`
- `RequestResult`
- `BitDepth`
- `PostSilenceFrames`
- `IOMatchingNotificationCallback`
- `!((inRegistryEntry) == nullptr)`
- `iterator != nullptr`
- `dataList != nullptr`
- `AssetID`
- `SampleRate`
