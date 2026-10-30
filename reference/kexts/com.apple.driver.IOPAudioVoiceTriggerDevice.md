# `com.apple.driver.IOPAudioVoiceTriggerDevice`

- Name: IOPAudioVoiceTriggerDevice
- Version: `600.6`
- UUID: `1B7A3EA5-1AC6-3B1C-8D42-D1753F895B34`
- Source version: `600.6.0.0.0`
- Depends on: [`com.apple.driver.AppleEmbeddedAudioLibs`](com.apple.driver.AppleEmbeddedAudioLibs.md) 1.0, [`com.apple.driver.ExclavesAudioKext`](com.apple.driver.ExclavesAudioKext.md) 1.0, [`com.apple.iokit.IOPAudioDriverFamily`](com.apple.iokit.IOPAudioDriverFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 9.0.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/iop-voicetrigger-controller/audio-vt-device`](../devicetree/root__arm-io__iop-voicetrigger-controller__audio-vt-device.md) | `IOPAudioIsolatedVoiceTriggerDevice` | `iop-audio,isolated-vt-device` |

## IOKit personalities (2) [KC]

### IOPAudioIsolatedVoiceTriggerDevice
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioVoiceTriggerDevice`
- `IOClass`: `IOPAudioIsolatedVoiceTriggerDevice`
- `IOExclaveProxy`: `True`
- `IONameMatch`:
  - `iop-audio,isolated-vt-device`
- `IOPersonalityPublisher`: `com.apple.driver.IOPAudioVoiceTriggerDevice`
- `IOProviderClass`: `IOPAudioNode`
- `IOUserClientClass`: `IOPAudioVoiceTriggerDeviceUserClient`

### IOPAudioVoiceTriggerDevice
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioVoiceTriggerDevice`
- `IOClass`: `IOPAudioVoiceTriggerDevice`
- `IONameMatch`:
  - `iop-audio,vt-device`
- `IOPersonalityPublisher`: `com.apple.driver.IOPAudioVoiceTriggerDevice`
- `IOProviderClass`: `IOPAudioNode`
- `IOUserClientClass`: `IOPAudioVoiceTriggerDeviceUserClient`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOPAudioIsolatedVoiceTriggerDevice` | 0x1c0 | IOPAudioVoiceTriggerDevice → IOPAudioDevice → IOService → IORegistryEntry |
| `IOPAudioVoiceTriggerDevice` | 0x170 | IOPAudioDevice → IOService → IORegistryEntry |
| `IOPAudioVoiceTriggerDeviceUserClient` | 0xe8 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00004c80 off=0x00a3a950-0x00a3f5d0 addr=0xfffffe0007a3e950-0xfffffe0007a435d0 r--/r--   __TEXT            
	sz=0x00000090 off=0x00a3b018-0x00a3b0a8 addr=0xfffffe0007a3f018-0xfffffe0007a3f0a8               __TEXT.__const            
	sz=0x00002e02 off=0x00a3b0a8-0x00a3deaa addr=0xfffffe0007a3f0a8-0xfffffe0007a41eaa               __TEXT.__cstring          (CstringLiterals)
	sz=0x00001726 off=0x00a3deaa-0x00a3f5d0 addr=0xfffffe0007a41eaa-0xfffffe0007a435d0               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0000d424 off=0x033063b0-0x033137d4 addr=0xfffffe000a30a3b0-0xfffffe000a3177d4 r-x/r-x   __TEXT_EXEC       
	sz=0x0000ce34 off=0x033063b0-0x033131e4 addr=0xfffffe000a30a3b0-0xfffffe000a3171e4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000005f0 off=0x033131e4-0x033137d4 addr=0xfffffe000a3171e4-0xfffffe000a3177d4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000181 off=0x04a14898-0x04a14a19 addr=0xfffffe000ba18898-0xfffffe000ba18a19 rw-/rw-   __DATA            
	sz=0x000000f8 off=0x04a14898-0x04a14990 addr=0xfffffe000ba18898-0xfffffe000ba18990               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000ba18990-0xfffffe000ba18a18               __DATA.__common           (Zerofill)
	sz=0x00000001 off=0x00000000-0x00000001 addr=0xfffffe000ba18a18-0xfffffe000ba18a19               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001b68 off=0x013ced40-0x013d08a8 addr=0xfffffe00083d2d40-0xfffffe00083d48a8 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x013ced40-0x013ced58 addr=0xfffffe00083d2d40-0xfffffe00083d2d58         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x013ced58-0x013ced70 addr=0xfffffe00083d2d58-0xfffffe00083d2d70         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001720 off=0x013ced70-0x013d0490 addr=0xfffffe00083d2d70-0xfffffe00083d4490         __DATA_CONST.__const            
	sz=0x000000c0 off=0x013d0490-0x013d0550 addr=0xfffffe00083d4490-0xfffffe00083d4550         __DATA_CONST.__kalloc_type      
	sz=0x000002f8 off=0x013d0550-0x013d0848 addr=0xfffffe00083d4550-0xfffffe00083d4848         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000060 off=0x013d0848-0x013d08a8 addr=0xfffffe00083d4848-0xfffffe00083d48a8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 202 at 0x04af5e24
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     1B7A3EA5-1AC6-3B1C-8D42-D1753F895B34
008: LC_SOURCE_VERSION           600.6.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac3e50 size=0x198
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOPAudioVoiceTriggerDevice`
- `CFBundleGetInfoString`: `Copyright © 2023 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioVoiceTriggerDevice`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOPAudioVoiceTriggerDevice`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOPAudioVoiceTriggerDevice.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895072944`
- `_PrelinkExecutableRelativePath`: `IOPAudioVoiceTriggerDevice`
- `_PrelinkExecutableSize`: `81293`
- `_PrelinkExecutableSourceAddr`: `-2198895072944`
- `_PrelinkKmodInfo`: `-2198828119912`

## Strings (237) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `_validateUserClient`
- `mDebugClient.debugGetSecureData(eventData)`
- `failed, status: 0x%x, %s(), line %d: `
- `%s::%s() kControlVoiceTriggerEnable = %llu\n`
- `\"TB_FATAL: \" \"invalid result returned from debugSiriLanguageModel\" @%s:%d`
- `\"TB_FATAL: \" \"invalid result returned from getNonSecureData\" @%s:%d`
- `configDictionary`
- `theUserClient->mDevice->open(theUserClient)`
- `initWithEndpoint`
- `%s::%s() continuoustime: %llu, absolutetime: %llu, now: %llu`
- `super::_handleDeviceReady(inProvider)`
- `IOUserClientEntitlements`
- `error`
- `dataSize == propertySize`
- `I32@?0{voicetriggernonsecure_voicetriggernonsecure_getnonsecuredata__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q}{voicetriggernonsecure_voicetriggernonsecuredatatb_s=QQ})}8`
- `AOPVoiceTrigger`
- `ioReturnFromTBError( voicetriggerdebug_voicetriggerdebug__init(&client, mTightbeamEndpoint))`
- `debugSiriLanguageModelRet`
- `VoiceTriggerProxy_C.c`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS) && \\\"failed to wrap packed buffer\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `AppleAudioSystemHelper::isDevelopmentKernel()`
- `v32@?0{voicetriggernonsecure_voicetriggernonsecure_getnonsecuredata__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q}{voicetriggernonsecure_voicetriggernonsecuredatatb_s=QQ})}8`
- `debugGetSecureDataRet`
- `23:35:52`
- `\"TB_ASSERT: \" \"(vErr == TB_ERROR_SUCCESS) && \\\"tb_message_subrange failed\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_FATAL: \" \"unrecognized selector: %llu\" @%s:%d`
- `mDevice`
- `mDebugClient.initWithEndpoint(mProxyEndoint.get())`
- `mNonSecureClient.getNonSecureData(eventData)`
- `ioReturnFromTBError( voicetriggernonsecure_voicetriggernonsecure_getnonsecuredata( &tbClient, ^(voicetriggernonsecure_voicetriggernonsecure_getnonsecuredata__result_s result) { auto success = voicetriggernonsecure_voicetriggernonsecure_getnonsecuredata__result_get_success( &result); if (success != n`
- `1211111212221212111121222222222222222222222122`
- `inArguments`
- `warning`
- `IOPAudioVoiceTriggerDevice`
- `stop`
- `- %s::%s\n`
- `_enableListening(static_cast<bool>(inControlValue))`
- `_enableListening`
- `^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16`
- `getPropertyFromIORegistry(registryEntry.get(), inKey, outData)`
- `no`
- `!(configData->getLength() == 0)`
- `<unknown>`
- `IOUserClientDefaultLocking`
- `inArguments->scalarInput`
- `theUserClient->mDevice->setControlValue(inArguments->scalarInput[0], inArguments->scalarInput[1])`
- `trigger-time`
- `super::_handleStart(inProvider)`
- `%s::%s -> ret: 0x%x\n`
- `\"TB_FATAL: \" \"overflow detected when adding\" @%s:%d`
- `debugGetSecureData`
- `\"TB_FATAL: \" \"invalid result returned from configureTriggerNotification\" @%s:%d`
- `inArguments->scalarOutput`
- `12111112122212121111212222222222222222222221222111111111`
- `_setupProxy`
- `setProperty(VTIORegProperties::kEventInfo, dataDictionary.get())`
- `voiceTriggerChannels`
- `_setEventDictionaryAndMessageClients`
- `pointer \"%s\" is null, cannot continue, %s(), line %d, status: 0x%x\n`
- `getNonSecureData`
- `configureTriggerNotification`
- `(entitlement = copyClientEntitlement(inOwningTask, kIOPAudioVoiceTriggerUserClientEntitlement))`
- `setProperties`
- `getNodeInterface()->setNodeProperty(channelMaskDescriptor)`
- `VTConfiguration`
- `\"TB_ASSERT: \" \"(aopvoicetriggersecure_voicetriggerlanguagemodeltb__decode(msg, &inLanguageModel) == TB_ERROR_SUCCESS) && \\\"failed to decode type: AOPVoiceTriggerSecure.VoiceTriggerLanguageModelTB\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `propertyDictionary`
- `UserClient::init() - New UserClient for process %s (pid %d)\n`
- `inProxyEndpoint`
- `mProxyEndpoint->createTightbeamEndpoint(mTightbeamEndpoint)`
- `ioReturnFromTBError( voicetriggernonsecure_voicetriggernonsecure__init(&client, mTightbeamEndpoint))`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `dispatchSetControlValue`
- `_handleTriggerNotification`
- `getAudioProperty`
- `getNonSecureDataRet`
- `v24@?0{voicetriggerdebug_voicetriggerdebug_debugsirilanguagemodel__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `ioReturnFromTBError( voicetriggerdebug_voicetriggerdebug_debuggetsecuredata( &tbClient, ^(voicetriggerdebug_voicetriggerdebug_debuggetsecuredata__result_s result) { auto payload = voicetriggerdebug_voicetriggerdebug_debuggetsecuredata__result_get_success(&result); if (!payload) { auto failure = voic`
- `CorealisRTModelVersion`
- `_queryListening`
- `_queryModelCRC`
- `\"TB_FATAL: \" \"invalid value: unexpected case value, %llx\" @%s:%d`
- `_validateUserClient(inTarget, &theUserClient)`
- `mProxyEndoint`
- `mDebugEnabled`
- `IODeviceTree:/product/audio`
- `_configure`
- `_setControlValue`
- `VTEventInfo`
- `I16@?0^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}8`
- `_closeDevice`
- `mProxyEndpoint`
- `setupTriggerNotification`
- `inDevice->getWorkLoop()->addEventSource(inAsyncNotification)`
- `+ %s::%s\n`
- `getNodeInterface()->setNodeProperty(IOPAudio::MakeSetPropertyDescriptor(kEnablePropertyID, request))`
- `_configureModel`
- `node-enable-state`
- `IOPAudioVoiceTriggerDeviceUserClient`
- `info`
- `[%s](%s) %s`
- `'Siri' first pass trigger occurred, now <%llu ns, %lld>, trigger time <%llu ns, %lld>, delta %lld ns,aop trigger time <%lld>, sample time %lld, trigger len frames %llu, woke AP %s, trigger state size %d\n`
- `getNodeInterface()->getNodeProperty(getCRCDescriptor)`
- `super::start(inProvider)`
- `_convertTime`
- `%s::%s() hostTime: %llu, sampleTime: %llu -> ret: 0x%x\n`
- `notice`
- `inModelData`
- `\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `entitlement == kOSBooleanTrue`
- `configProperty`
- `%s::%s() -> ret: 0x%x\n`
- `registryEntry`
- `+ %s::%s built %s %s\n`
- `CorealisRTModel`
- `I24@?0{voicetriggernonsecure_voicetriggernonsecure_configuretriggernotification__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `mNonSecureClient.initWithEndpoint(mProxyEndoint.get())`
- `mTriggerData`
- `trigger-length`
- `trigger-woke-ap`
- `messageClients(static_cast<uint32_t>(VTEventTypes::kPhraseDetect))`
- `getNodeInterface()->getNodeProperty(getPowerStatePropertyDescriptor)`
- `VTActiveChannelMask`
- `VTTriggerCount`
- `I24@?0{voicetriggerdebug_voicetriggerdebug_debugsirilanguagemodel__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `I176@?0{voicetriggerdebug_voicetriggerdebug_debuggetsecuredata__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q}{voicetriggercommon_voicetriggersecuredatatb_s=QQQI[128C]})}8`
- `!(theUserClient->isInactive())`
- `getPropertyFromIORegistry`
- `%s::%s() ActiveChannelMask = %llu, Not writable\n`
- `%s::%s() {enabled: %d} -> ret: 0x%x\n`
- `\"TB_FATAL: \" \"invalid tag in '[UInt8]' metadata: 0x%x\" @%s:%d`
- `initWithTask`
- `theUserClient->mDevice->getControlValue(inArguments->scalarInput[0], inArguments->scalarOutput[0])`
- `mDebugClient.debugSiriLanguageModel(configData)`
- `%c%c%c%c`
- `%s::%s() EDT Read channel mask = 0x%08X\n`
- `handleIOPMessage`
- `_queryListening(fEnabled)`
- `\"TB_ASSERT: \" \"(server->debuggetsecuredata != ((void*)0)) && \\\"implementation for debugGetSecureData is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `I8@?0`
- `site.IOPAudioIsolatedVoiceTriggerDevice`
- `trigger-sample-frame-time`
- `inDevice`
- `_handleStart`
- `VTEnabled`
- `\"TB_ASSERT: \" \"(server->debugsirilanguagemodel != ((void*)0)) && \\\"implementation for debugSiriLanguageModel is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `trigger-config-blob`
- `ioReturnFromTBError( voicetriggerdebug_voicetriggerdebug_debugsirilanguagemodel( &tbClient, &languageModel, ^(voicetriggerdebug_voicetriggerdebug_debugsirilanguagemodel__result_s result) { if (!voicetriggerdebug_voicetriggerdebug_debugsirilanguagemodel__result_get_success( &result)) { auto failure =`
- `expression \"%s\" failed, %s(), line %d, status: 0x%x\n`
- `inMessage.getMessageType() == IOPMessageType::kReport`
- `12111112122212121111111111111`
- `IOUserClientDefaultLockingSetProperties`
- `expression \"%s\" FAILED, %s(), line %d, status: 0x%x\n`
- `configData`
- `%s::%s() Set new voice trigger configuration: %s (%u bytes)\n`
- `\"TB_ASSERT: \" \"(server->configuretriggernotification != ((void*)0)) && \\\"implementation for configureTriggerNotification is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `_setupProxy(inProvider)`
- `_setEventDictionaryAndMessageClients()`
- `dispatchOpen`
- `(*outUserClient)->mDevice`
- `setEventData`
- `inAsyncNotification`
- `ioReturnFromTBError( voicetriggernonsecure_voicetriggernonsecure_configuretriggernotification( &tbClient, asyncNotificationID, ^(voicetriggernonsecure_voicetriggernonsecure_configuretriggernotification__result_s result) { if (!voicetriggernonsecure_voicetriggernonsecure_configuretriggernotification_`
- `getNodeInterface()->setNodeProperty( IOPAudio::MakeSetPropertyDescriptor( VoiceTriggerFirmwareProperties::kPropertyVtcmModelConfigBlob, *static_cast<const uint8_t*>(configData->getBytesNoCopy()), configData->getLength()))`
- `VTConfigured`
- `*outUserClient`
- `IOPAudioIsolatedVoiceTriggerDevice`
- `%s::%s() debugEnabled: %hhu\n`
- `inEntry`
- `super::initWithEndpoint(inProxyEndpoint)`
- `_queryModelCRC(modelCRC)`
- `%s::%s() ModelCRC = %llu, Not writable\n`
- `inConfiguration`
- `setProperty(VTIORegProperties::kConfigured, true)`
- `%s::%s() {CRC value: %d} -> ret: 0x%x\n`
- `\"TB_ASSERT: \" \"(server->getnonsecuredata != ((void*)0)) && \\\"implementation for getNonSecureData is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_FATAL: \" \"invalid error returned from %s\" @%s:%d`
- `debugSiriLanguageModel`
- `site.IOPAudioVoiceTriggerDevice`
- `Oct 13 2026`
- `setConfiguration_block_invoke`
- `start`
- `theUserClient->mDevice->isOpen(theUserClient)`
- `com.apple.private.aop-voicetrigger.user-access`
- `asyncNotification`
- `%s-%d`
- `getNodeInterface()->convertTime(conversionDescriptor)`
- `trigger-type`
- `debug`
- `v24@?0{voicetriggernonsecure_voicetriggernonsecure_configuretriggernotification__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `_handleDeviceReady`
- `condition \"%s\" failed, %s() line %d, status: 0x%x\n`
- `setProperty(VTIORegProperties::kConfigurationInfo, configDictionary.get())`
- `\"TB_FATAL: \" \"invalid result returned from debugGetSecureData\" @%s:%d`
- `v20@?0^{IOInterruptEventSource=^^?i^{IOEventSource}^{OSObject}^?B^{IOWorkLoop}^v^{ExpansionData}^{IOService}iIIBB^{ExpansionData}}8i16`
- `mNonSecureClient.setupTriggerNotification(this, asyncNotification.get())`
- `configureTriggerNotificationRet`
- `v176@?0{voicetriggerdebug_voicetriggerdebug_debuggetsecuredata__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q}{voicetriggercommon_voicetriggersecuredatatb_s=QQQI[128C]})}8`
- `yes`
- `i8@?0`
- `_configureModel(configData, configDescription)`
- `%s::%s(%d) -> ret: 0x%x\n`
- `node-disable-state`
- `site.IOPAudioVoiceTriggerDeviceUserClient`
- `IOUserClient::initWithTask(inOwningTask, inSecurityToken, inType, inProperties)`
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `!(currentTimeNS < triggerTimeNS)`
- `setProperty(VTIORegProperties::kTriggerCount, triggerCount, 32)`
- `_getControlValue`
- `\"TB_FATAL: \" \"invalid value: unexpected bits, 0x%llx\" @%s:%d`
- `dispatchClose`
- `dispatchGetControlValue`

**[__TEXT.__os_log]**

- `%s::%s -> ret: 0x%x\n`
- `UserClient::init() - New UserClient for process %s (pid %d)\n`
- `%s::%s() debugEnabled: %hhu\n`
- `%s::%s() continuoustime: %llu, absolutetime: %llu, now: %llu`
- `%s`
- `+ %s::%s built %s %s\n`
- `expression \"%s\" failed, %s(), line %d, status: 0x%x\n`
- `%s::%s() EDT Read channel mask = 0x%08X\n`
- `%s::%s() {CRC value: %d} -> ret: 0x%x\n`
- `%s::%s() hostTime: %llu, sampleTime: %llu -> ret: 0x%x\n`
- `(%s) %s`
- `expression \"%s\" FAILED, %s(), line %d, status: 0x%x\n`
- `condition \"%s\" failed, %s() line %d, status: 0x%x\n`
- `%s::%s(%d) -> ret: 0x%x\n`
- `%s::%s() {enabled: %d} -> ret: 0x%x\n`
- `%s::%s() -> ret: 0x%x\n`
- `+ %s::%s\n`
- `failed, status: 0x%x, %s(), line %d: `
- `%s::%s() kControlVoiceTriggerEnable = %llu\n`
- `%s::%s() ActiveChannelMask = %llu, Not writable\n`
- `%s::%s() ModelCRC = %llu, Not writable\n`
- `pointer \"%s\" is null, cannot continue, %s(), line %d, status: 0x%x\n`
- `- %s::%s\n`
- `'Siri' first pass trigger occurred, now <%llu ns, %lld>, trigger time <%llu ns, %lld>, delta %lld ns,aop trigger time <%lld>, sample time %lld, trigger len frames %llu, woke AP %s, trigger state size %d\n`
- `%s::%s() Set new voice trigger configuration: %s (%u bytes)\n`
