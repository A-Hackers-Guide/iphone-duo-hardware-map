# `com.apple.iokit.IOPAudioDriverFamily`

- Name: IOPAudioDriverFamily
- Version: `400.12`
- UUID: `56A3897C-5EAF-3CDF-A133-891E34F0722C`
- Source version: `400.12.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleEmbeddedAudioLibs`](com.apple.driver.AppleEmbeddedAudioLibs.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (2) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/iop-audio-controller`](../devicetree/root__arm-io__iop-audio-controller.md) | `IOPAudioController` | `iop-audio,controller` |
| [`/arm-io/iop-voicetrigger-controller`](../devicetree/root__arm-io__iop-voicetrigger-controller.md) | `IOPAudioController` | `iop-audio,controller` |

## IOKit personalities (1) [KC]

### IOPAudioController
- `CFBundleIdentifier`: `com.apple.iokit.IOPAudioDriverFamily`
- `IOClass`: `IOPAudioController`
- `IONameMatch`:
  - `iop-audio,controller`
- `IOPersonalityPublisher`: `com.apple.iokit.IOPAudioDriverFamily`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (8) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOPAudioAggregateMessageDispatcher` | 0x30 |  |
| `IOPAudioController` | 0xf0 | IOService → IORegistryEntry |
| `IOPAudioDevice` | 0xa8 | IOService → IORegistryEntry |
| `IOPAudioDeviceExternalServiceManager` | 0x60 |  |
| `IOPAudioMessageDispatcher` | 0x38 |  |
| `IOPAudioNode` | 0xa0 | IOService → IORegistryEntry |
| `IOPAudioNodeManager` | 0x58 |  |
| `IOPAudioService` | 0xb0 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000696b off=0x00a2c560-0x00a32ecb addr=0xfffffe0007a30560-0xfffffe0007a36ecb r--/r--   __TEXT            
	sz=0x00000060 off=0x00a2cc30-0x00a2cc90 addr=0xfffffe0007a30c30-0xfffffe0007a30c90               __TEXT.__const            
	sz=0x00003be7 off=0x00a2cc90-0x00a30877 addr=0xfffffe0007a30c90-0xfffffe0007a34877               __TEXT.__cstring          (CstringLiterals)
	sz=0x00002654 off=0x00a30877-0x00a32ecb addr=0xfffffe0007a34877-0xfffffe0007a36ecb               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0001454c off=0x032e4300-0x032f884c addr=0xfffffe000a2e8300-0xfffffe000a2fc84c r-x/r-x   __TEXT_EXEC       
	sz=0x0001401c off=0x032e4300-0x032f831c addr=0xfffffe000a2e8300-0xfffffe000a2fc31c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000530 off=0x032f831c-0x032f884c addr=0xfffffe000a2fc31c-0xfffffe000a2fc84c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000458 off=0x04a13d88-0x04a141e0 addr=0xfffffe000ba17d88-0xfffffe000ba181e0 rw-/rw-   __DATA            
	sz=0x00000308 off=0x04a13d88-0x04a14090 addr=0xfffffe000ba17d88-0xfffffe000ba18090               __DATA.__data             
	sz=0x00000150 off=0x00000000-0x00000150 addr=0xfffffe000ba18090-0xfffffe000ba181e0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00002cf8 off=0x013c7450-0x013ca148 addr=0xfffffe00083cb450-0xfffffe00083ce148 rw-/rw-   __DATA_CONST      
	sz=0x00000040 off=0x013c7450-0x013c7490 addr=0xfffffe00083cb450-0xfffffe00083cb490         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000040 off=0x013c7490-0x013c74d0 addr=0xfffffe00083cb490-0xfffffe00083cb4d0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000022e0 off=0x013c74d0-0x013c97b0 addr=0xfffffe00083cb4d0-0xfffffe00083cd7b0         __DATA_CONST.__const            
	sz=0x00000340 off=0x013c97b0-0x013c9af0 addr=0xfffffe00083cd7b0-0xfffffe00083cdaf0         __DATA_CONST.__kalloc_type      
	sz=0x00000320 off=0x013c9af0-0x013c9e10 addr=0xfffffe00083cdaf0-0xfffffe00083cde10         __DATA_CONST.__kalloc_var       
	sz=0x00000298 off=0x013c9e10-0x013ca0a8 addr=0xfffffe00083cde10-0xfffffe00083ce0a8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000a0 off=0x013ca0a8-0x013ca148 addr=0xfffffe00083ce0a8-0xfffffe00083ce148         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 186 at 0x04af56d4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     56A3897C-5EAF-3CDF-A133-891E34F0722C
008: LC_SOURCE_VERSION           400.12.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac3888 size=0x308
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleExecutable`: `IOPAudioDriverFamily`
- `CFBundleIdentifier`: `com.apple.iokit.IOPAudioDriverFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOPAudioDriverFamily`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOPAudioDriverFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895131296`
- `_PrelinkExecutableRelativePath`: `IOPAudioDriverFamily`
- `_PrelinkExecutableSize`: `122887`
- `_PrelinkExecutableSourceAddr`: `-2198895131296`
- `_PrelinkKmodInfo`: `-2198828122744`

## Strings (323) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `!((inMatchingType) == nullptr)`
- `!((mExternalPowerManager) == nullptr)`
- `!((data) == nullptr)`
- `site.RegisterAccess::Packet.uint8_t`
- `!((inNotifierList) == nullptr)`
- `/Library/Caches/com.apple.xbs/C9C26AD7-9CB6-4E87-BD55-E0086C9C4601/TemporaryDirectory.bWezrQ/Sources/IOPAudioDriverFamily/src/kext/IOPAudioDriverFamily/nub/IOPAudioNode/IOPAudioNode.cpp`
- `ret = mMessageDispatcher->enable() == 0 `
- `site.IOPAudioNodeManager`
- `IOPAudio::NodeManager`
- `!((inTarget) == nullptr)`
- `!((inFrom) == nullptr)`
- `IOPAudio::Node::Helper`
- `virtual IOReturn IOPAudioController::powerStateDidChangeTo(IOPMPowerFlags, unsigned long, IOService *)_block_invoke`
- `!((mConfigProvider) == nullptr)`
- `ret = inCommandInterface.init(domainID, iopDestinationID) == 0 `
- `!((inEntry) == nullptr)`
- `IOPAudioController`
- `!(getProvider() == iopudioService)`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `ret = SetIdentifierProperty(this, getNodeInterface()->getIdentifier()) == 0 `
- `unknown`
- `site.IOPAudioAggregateMessageDispatcher`
- `bounded_ptr<T>::discard_bounds: Discarding the bounds on this pointer would lose the fact that it is outside of the bounds set originally`
- `ret = _retrieveDeviceConfig(inProvider, deviceConfig) == 0 `
- `identifier`
- `ret = setNodeProperty({ .propertyID = kDescriptor.propertyID, .dataSize = kDescriptor.data->getLength(), .data = kDescriptor.data->getBytesNoCopy(), }) == 0 `
- `default-publication-mode`
- `/Library/Caches/com.apple.xbs/C9C26AD7-9CB6-4E87-BD55-E0086C9C4601/TemporaryDirectory.bWezrQ/Sources/IOPAudioDriverFamily/src/kext/IOPAudioDriverFamily/core/IOPAudioCommandInterface/IOPAudioCommandInterface.cpp`
- `!((mIOPAudioService) == nullptr)`
- `ret = mIOPAudioService->performCommand(inCommand) == 0 `
- `!((dataPtr) == nullptr)`
- `IOPAudioCommandInterface`
- `site.IOPAudioMessageDispatcher`
- `ret = retrieveExternalPowerDepedencyInfo(mConfigProvider, mExternalPowerProviderMatchingInfoList) == 0 `
- `ret = inCommand.process(getCommandInterface()) == 0 `
- `inWhatDevice == this`
- `IOPAudioNodeManager`
- `_processProbeCandidates_block_invoke`
- `site.MemoryAccessCommandDescriptor`
- `OSBoundedPtr.h`
- `121111121222121211112`
- `inEntry->setProperty(inPropertyName, kTimeElapsedMs, sizeof(kTimeElapsedMs) * 8)`
- `!((inController) == nullptr)`
- `!((combinedMatchingDictionaryList) == nullptr)`
- `!((notificationHandler) == nullptr)`
- `i8@?0`
- `powerStateWillChangeTo_block_invoke`
- `12121111112`
- `site.struct GetNodePropertyOutputPacket.uint8_t`
- `!((stringObject) == nullptr)`
- `!((dataBuffer.data()) == nullptr)`
- `\"%s\" @%s:%d`
- `ret = registerPowerDriver(this, sIOPMStates, kNumberOfPowerStates) == 0 `
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `externalServiceManager->expectedExternalServiceCount() > 0`
- `ret = extPMRef->addPowerProvider(inService) == 0 `
- `IOPAudioService`
- `ret = _configure(inProvider) == 0 `
- `MatchedAudioServiceName`
- `mIOPAudioService->open(this, clientConfig)`
- `!((inNode) == nullptr)`
- `site.GetNodePropertyCommandDescriptor`
- `static_cast<bool>(constantData) == static_cast<bool>(kDataSize > 0)`
- `/Library/Caches/com.apple.xbs/C9C26AD7-9CB6-4E87-BD55-E0086C9C4601/TemporaryDirectory.bWezrQ/Sources/IOPAudioDriverFamily/src/kext/IOPAudioDriverFamily/core/IOPAudioMessage/IOPAudioMessageHelper.cpp`
- `supports-external-function`
- `ret = sendEvent(IOPAudioNodeManager::Event::kPopulatingNodesBelow) == 0 `
- `!(inDomainID == IOPAudio::DomainID::kInvalid)`
- `MemoryAccessDescriptor`
- `ret = IOPAudio::Helper::addMatchingNotificationForMatchingList( gIOFirstMatchNotification, mExternalPowerProviderMatchingInfoList, mExternalPowerProviderMatchingNotifiers, this, &mExternalPowerProviderMatchingNotifiers, matchingNotificationAction) == 0 `
- `ret = _configureDevice(inProvider) == 0 `
- `!((inPowerProvider) == nullptr)`
- `_waitTillAwake`
- `retrieveDomainInfoFromDeviceTree`
- `!((inPropertyKey) == nullptr)`
- `inEntry->setProperty(IOPAudio::Device::IORegistry::kIdentifier, identifierString.get())`
- `!((mAggregateMessageDispatcher) == nullptr)`
- `setPowerState_block_invoke`
- `!((mCommandGate) == nullptr)`
- `!((inCallback) == nullptr)`
- `site.AttachCommandDescriptor`
- `!((action) == nullptr)`
- `!(boundedArrayRef.size() == 0)`
- `IOPAudio::Node::Helper::isValidPublicationMode(outPublicationMode, true)`
- `site.IOPAudioService`
- `B16@?0^{OSObject=^^?i}8`
- `ret = dispatcher->enable() == 0 `
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `!((destinationNode) == nullptr)`
- `ret = registerWrite(inDescriptor.getNodeID(), kPayload.addressSize, kPayload.address, kPayload.dataElementSize, dataSize, kPayload.constantData, kPayload.qualifier, kPayload.optionBits) == 0 `
- `!((inRegistryEntry) == nullptr)`
- `IOPAudioDevice`
- `ret = mAggregateMessageDispatcher->registerClient( clientConfig->domainID, inClient, clientConfig->messageAction) == 0 `
- `TimeUntilAudioServicedMatched_ms`
- `createNamedMatchingDictionaries`
- `remote-node-interface`
- `!((inConfigProvider) == nullptr)`
- `/Library/Caches/com.apple.xbs/C9C26AD7-9CB6-4E87-BD55-E0086C9C4601/TemporaryDirectory.bWezrQ/Sources/IOPAudioDriverFamily/src/kext/IOPAudioDriverFamily/service/IOPAudioService/IOPAudioService.cpp`
- `populateNodesBelow`
- `ret = _enqueueProbeCandidate(node.get(), true) == 0 `
- `112121211222`
- `static_cast<bool>(modifiableData) == static_cast<bool>(kDataSize > 0)`
- `nameOverride[nameOverrideData->getLength() - 1] == 0`
- `!((inParam4) == nullptr)`
- `!((kDescriptor.data) == nullptr)`
- `!((extPMRef) == nullptr)`
- `success`
- `uses-dedicated-workloop`
- `ret = sendEvent(Event::kProcessedProbeCandidates) == 0 `
- `!((matchingDictionary) == nullptr)`
- `IOPAudioMessageDispatcher`
- `12111112122212121121`
- `super::start(inProvider)`
- `!((mLock) == nullptr)`
- `IOPAudio::MessageHelper`
- `!((iopudioService) == nullptr)`
- `ExpectedExternalPowerProviderCount`
- `ret = mWorkLoop->addEventSource(mWorkerES.get()) == 0 `
- `!(kCurrentCount > kExpectedCount)`
- `/Library/Caches/com.apple.xbs/C9C26AD7-9CB6-4E87-BD55-E0086C9C4601/TemporaryDirectory.bWezrQ/Sources/IOPAudioDriverFamily/src/kext/IOPAudioDriverFamily/core/IOPAudioAggregateMessageDispatcher/IOPAudioAggregateMessageDispatcher.cpp`
- `!((inPropertyList) == nullptr)`
- `!((notifierListRef) == nullptr)`
- `!((notifier) == nullptr)`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `setProperty(IOPAudio::Device::IORegistry::kUsesDedicatedWorkLoop, kOSBooleanTrue)`
- `!((inIOPAudioNode) == nullptr)`
- `!((mExternalServices.externalPowerManager) == nullptr)`
- `!((matchingNotificationAction) == nullptr)`
- `virtual IOReturn IOPAudioDevice::setPowerState(unsigned long, IOService *)_block_invoke`
- `publication-mode`
- `static_cast<bool>(isAttachable)`
- `/Library/Caches/com.apple.xbs/C9C26AD7-9CB6-4E87-BD55-E0086C9C4601/TemporaryDirectory.bWezrQ/Sources/IOPAudioDriverFamily/src/kext/IOPAudioDriverFamily/controller/IOPAudioController/IOPAudioController.cpp`
- `!((inConfig.controller) == nullptr)`
- `site.TimeConversionCommandDescriptor`
- `ret = _configure() == 0 `
- `_audioServiceMatchHandler`
- `!((mUnpublishedNodes) == nullptr)`
- `!((inMatchingInfoList) == nullptr)`
- `!((inAction) == nullptr)`
- `ret = getARMFunctionSignature(inParam1, signature) == 0 `
- `!((mController) == nullptr)`
- `ret = _initForPM(inProvider) == 0 `
- `external-power-provider`
- `!((dispatcher) == nullptr)`
- `static_cast<bool>(dataElementCount) == static_cast<bool>(dataElementSize)`
- `!((theFunction) == nullptr)`
- `\"%s some external devices are still powered off (count=%u).\" @%s:%d`
- `1121212`
- `!((stringList) == nullptr)`
- `static_cast<bool>(address) == static_cast<bool>(addressSize > 0)`
- `!((mRemoteNodeInterfaceMap) == nullptr)`
- `IOPAudioNode`
- `site.IOPAudioNode`
- `NULL`
- `121112`
- `createPropertyMatchingDictionaries`
- `ret = getNodeProperty({ .propertyID = kDescriptor.propertyID, .dataSize = dataBuffer.size(), .ioData = dataBuffer.data(), }) == 0 `
- `IOPAudioController.cpp`
- `!((mWorkLoop) == nullptr)`
- `!((inClient) == nullptr)`
- `ret = getWorkLoop()->runActionBlock(^IOReturn { return _handleDeviceReady(inProvider); }) == 0 `
- `!((mExternalServiceManager) == nullptr)`
- `1211111212221212111222`
- `MatchedExternalPowerProviderCount`
- `IOPAudioDeviceExternalServiceManager`
- `!((mRemoteNodeInterfaceMatchingNotifiers) == nullptr)`
- `!((functionDataRaw) == nullptr)`
- `inOther.isValid()`
- `!((mMessageDispatcher) == nullptr)`
- `!((mWorkerES) == nullptr)`
- `inNameList->getCount() > 0`
- `remainingPayloadSize >= sizeof(PropertyChangeEventPacket)`
- `!((mNotificationHandler) == nullptr)`
- `!((key) == nullptr)`
- `powerStateDidChangeTo_block_invoke`
- `ret = dispatcher->registerClient(inClient, inCallback) == 0 `
- `site.IOPAudioDeviceExternalServiceManager`
- `ret = _addRemoteNodeInterface(remoteNode) == 0 `
- `!((mNodeManager) == nullptr)`
- `ret = IOPAudio::Helper::addMatchingNotificationForMatchingList( gIOFirstMatchNotification, phandleMatchingDictionaryList, mExternalServices.externalPowerProviderMatchingNotifiers, this, &mExternalServices.externalPowerProviderMatchingNotifiers, matchingNotificationAction) == 0 `
- `kValidPublicationMode`
- `ret = sendEvent(Event::kInit) == 0 `
- `ret = inController->transferCommand(IOPAudio::AttachCommandDescriptor(kNodeID, inAttach)) == 0 `
- `!((mMessageDispatchers) == nullptr)`
- `remainingPayloadSize >= sizeof(EventPacket)`
- `combinedMatchingDictionaryList->merge(phandleBasedMatchingDictionaries.get())`
- `!((inService) == nullptr)`
- `!((inNameList) == nullptr)`
- `!((matchingInfoList) == nullptr)`
- `inPropertyList->getCount() > 0`
- `isValid()`
- `inMessage.getMessageType() == IOPAudio::IOPMessage::Type::kReport`
- `ret = IOPAudio::Helper::addMatchingNotificationForMatchingList( gIOFirstMatchNotification, mRemoteNodeInterfaceMatchingInfoList, mRemoteNodeInterfaceMatchingNotifiers, this, &mRemoteNodeInterfaceMatchingNotifiers, matchingNotificationAction) == 0 `
- `matchingInfoCount > 0`
- `!((inPropertyName) == nullptr)`
- `ret = _handleStart(inProvider) == 0 `
- `!((clientConfig) == nullptr)`
- `!(dataBuffer.size() == 0)`
- `!((inProvider) == nullptr)`
- `1121222`
- `ret = registerRead(inDescriptor.getNodeID(), kPayload.addressSize, kPayload.address, kPayload.dataElementSize, &dataSize, kPayload.modifiableData, kPayload.qualifier, kPayload.optionBits) == 0 `
- `121111111111`
- `!((mExternalPowerProviderMatchingNotifiers) == nullptr)`
- `iop-domain-id`
- `ret = inIOPAudioNode->getNodeProperty(propertyDescriptor) == 0 `
- `!(static_cast<bool>(mMessageDispatchers->getObject(domainID.get())))`
- `site.struct SetNodePropertyInputPacket.uint8_t`
- `ret = mController->transferCommand(descriptor) == 0 `
- `ret = processIdentifier(identifierProperty, mIdentifier) == 0 `
- `ret = SetExternalPowerProviderCountProperty(this, extPMRef) == 0 `
- `ret = mNodeManager->populateNodesBelow(inProvider) == 0 `
- `!((inData) == nullptr)`
- `!((client) == nullptr)`
- `ret = _setupExternalDependencies(inProvider) == 0 `
- `ret = makeUsable() == 0 `
- `!((inPowerManagerPtr) == nullptr)`
- `domain-id`
- `stringObject->getLength() == length`
- `!((inParam3) == nullptr)`
- `site.IOPAudioController`
- `ret = _audioServiceMatchHandler(inService) == 0 `
- `1211112`
- `isEnabled()`
- `setProperty(IOPAudio::Device::IORegistry::kUsesDedicatedWorkLoop, kOSBooleanFalse)`
- `ret = mExternalServiceManager->installMatchingNotifications() == 0 `
- `ret = getARMFunctionSignature(inParam3, signature) == 0 `
- `ret = getWorkLoop()->addEventSource(mCommandGate.get()) == 0 `
- `site.SetNodePropertyCommandDescriptor`
- `!(inStartMachAbsoluteTime > currentTime)`
- `/Library/Caches/com.apple.xbs/C9C26AD7-9CB6-4E87-BD55-E0086C9C4601/TemporaryDirectory.bWezrQ/Sources/IOPAudioDriverFamily/src/kext/IOPAudioDriverFamily/core/IOPAudioDriverFamilyTypes/IOPAudioDriverFamilyTypes.cpp`
- `IOPAudioDevice.cpp`
- `!((functionData) == nullptr)`
- `ret = initializeCommandInterface(getCommandInterface(), inProvider) == 0 `
- `121111121222121211111112112222`
- `ret = IOPAudio::Helper::addMatchingNotificationForMatchingList( gIOFirstMatchNotification, namedMatchingDictionaryList, mExternalServices.externalPowerProviderMatchingNotifiers, this, &mExternalServices.externalPowerProviderMatchingNotifiers, matchingNotificationAction) == 0 `
- `!((inDTRoot) == nullptr)`
- `ret = (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2c7) == 0 `
- `!((mClientInfoLock) == nullptr)`
- `!((externalPowerManager) == nullptr)`
- `getNodeInterface()->open(this, clientConfig)`
- `super::handleOpen(inClient, inOptions, inContext)`
- `!((mClient) == nullptr)`
- `!((remoteNode) == nullptr)`
- `ret = mNodeManager->sendEvent(IOPAudioNodeManager::Event::kAllDependenciesReady) == 0 `
- `ret = registerPowerDriver(this, sPowerStates, PowerState::kNumPowerStates) == 0 `
- `!((domainID) == nullptr)`
- `site.Packet.uint8_t`
- `!((getExternalPowerManager()) == nullptr)`
- `!((clientConfig->messageAction) == nullptr)`
- `_addExternalPowerProvider`
- `external-service-name-delimiter`
- `ret = sendEvent(Event::kProbeCandidateUpdated) == 0 `
- `length < remainingSize`
- `!((mNodeInterface) == nullptr)`
- `!(kDescriptor.data->getLength() == 0)`
- `!((boundedArrayRef) == nullptr)`
- `!((mProbeCandidates) == nullptr)`
- `!((probeCandidates) == nullptr)`
- `super::init(inFrom, gIODTPlane)`
- `external-named-power-provider`
- `/Library/Caches/com.apple.xbs/C9C26AD7-9CB6-4E87-BD55-E0086C9C4601/TemporaryDirectory.bWezrQ/Sources/IOPAudioDriverFamily/src/kext/IOPAudioDriverFamily/controller/IOPAudioNodeManager/IOPAudioNodeManager.cpp`
- `/Library/Caches/com.apple.xbs/C9C26AD7-9CB6-4E87-BD55-E0086C9C4601/TemporaryDirectory.bWezrQ/Sources/IOPAudioDriverFamily/src/kext/IOPAudioDriverFamily/device/IOPAudioDevice/IOPAudioDevice.cpp`
- `inEntry->setProperty(kMatchedExternalPowerProviderCountKey, extPowerProviderCount, sizeof(extPowerProviderCount) * 8)`
- `!((node) == nullptr)`
- `11212`
- `name-override`
- `virtual IOReturn IOPAudioController::setPowerState(unsigned long, IOService *)_block_invoke`
- `!(isInactive())`
- `inEntry->setProperty(kExpectedExternalPowerProviderCountKey, extPowerProviderCount, sizeof(extPowerProviderCount) * 8)`
- `%c%c%c%c`
- `ret = _addExternalPowerProvider(inService) == 0 `
- `\"%s::%s(), should not be called without owning the workloop\" @%s:%d`
- `kPayload.isValid()`
- `/Library/Caches/com.apple.xbs/C9C26AD7-9CB6-4E87-BD55-E0086C9C4601/TemporaryDirectory.bWezrQ/Sources/IOPAudioDriverFamily/src/kext/IOPAudioDriverFamily/core/IOPAudioDriverFamilyHelpers/IOPAudioDriverFamilyHelpers.cpp`
- `/Library/Caches/com.apple.xbs/C9C26AD7-9CB6-4E87-BD55-E0086C9C4601/TemporaryDirectory.bWezrQ/Sources/IOPAudioDriverFamily/src/kext/IOPAudioDriverFamily/core/IOPAudioMessageDispatcher/IOPAudioMessageDispatcher.cpp`
- `ret = getExternalPowerManager()->addPowerProvider(inService) == 0 `
- `site.IOPAudioDevice`
- `!((inWhatDevice) == nullptr)`
- `iop-audio-service-name`
- `!((mNodeMap) == nullptr)`
- `IOPAudioAggregateMessageDispatcher`
- `!((inNotifier) == nullptr)`
- `!((mMatchingServiceName) == nullptr)`
- `super::init()`
- `!((inMatchingNotificationHandler) == nullptr)`
- `IOPAudio::Device::ExternalServiceManager`
- `combinedMatchingDictionaryList->merge(nameBasedMatchingDictionaries.get())`
- `!((inParam1) == nullptr)`
- `!((probeConcluded) == nullptr)`
- `!((boundedPtr) == nullptr)`
- `IOPAudio::Helper`
- `remainingPayloadSize == targetPacket->payloadSize`
- `/Library/Caches/com.apple.xbs/C9C26AD7-9CB6-4E87-BD55-E0086C9C4601/TemporaryDirectory.bWezrQ/Sources/IOPAudioDriverFamily/src/kext/IOPAudioDriverFamily/device/IOPAudioDevice/ExternalServiceManager/IOPAudioDevice-ExternalServiceManager.cpp`
- `/Library/Caches/com.apple.xbs/C9C26AD7-9CB6-4E87-BD55-E0086C9C4601/TemporaryDirectory.bWezrQ/Sources/IOPAudioDriverFamily/src/kext/IOPAudioDriverFamily/nub/IOPAudioNode/IOPAudioNodeHelper.cpp`
- `ret = _waitTillAwake() == 0 `
- `_processProbeCandidates`
- `matchingInfoList->setObject(matchingDictionary)`
- `ret = mMessageDispatcher->registerClient(inClient, clientConfig->messageAction) == 0 `
- `!((identifier) == nullptr)`
- `mMessageDispatchers->setObject(domainID.get(), dispatcher.get())`
- `%8x`

**[__TEXT.__os_log]**

- `%s(%p)::%s() \t* Processing nub (id:'%c%c%c%c' name:%s) : [mode:'%c%c%c%c' | publish=%u]`
- `IOPAudioAggregateMessageDispatcher: Registered message dispatcher for domain 0x%x (default domain: 0x%x)`
- `%s name: %s inPowerStateOrdinal=%#lx [start]\n`
- `%s::%s(inService=%p [%s]) failed [ret=%#x]`
- `%s::%s() Found iop-domain-id property: '%c%c%c%c'`
- `%s [%u] unable to get service name at index=%d [NumServiceNames=%d]`
- `%s: %s, %s file: %s, line: %d\n`
- `%s::%s inWhatDevice:%s(%p) | ret = %#x [End]\n`
- `%s::%s() Final domain configuration applied: domainID='%c%c%c%c', iopDomainID='%c%c%c%c'`
- `%s(%p)::%s \t* Publishing nub (id:'%c%c%c%c' name:%s)`
- `IOPAudioAggregateMessageDispatcher: Deregistered message dispatcher for domain %s`
- `IOPAudioAggregateMessageDispatcher: Default domain ID set to 0x%x`
- `%s [%u] unable to get object at index=%d [NumElements=%d]`
- `%s::%s() unknown power state ordinal %#lx`
- `%s::%s inWhatDevice:%s(%p), inPowerStateOrdinal=%#lx [Start]`
- `%s::%s failed to instantiate an IOPAudioNode (entry=%s)`
- `%s::%s failed to retrieve system state for nodeID:'%c%c%c%c'`
- `%s::%s(inPowerStateOrdinal=%lu) ret=%#x (!=IOPMAckImplied)`
- `%s::%s() aborted [commandSleep=%#x]`
- `%s::%s() Found domain-id property: '%c%c%c%c'`
- `%s::%s failed to stringnify identifier(%#x/%c%c%c%c)`
- `%s(%p)::%s() processing publication mode:'%c%c%c%c' [nodeCount:%u]`
- `%s(%p)::%s() \t* Processing nub (id:'%c%c%c%c' name:%s) : [mode:'%c%c%c%c' | systemState:'%c%c%c%c' | publish=%u]`
