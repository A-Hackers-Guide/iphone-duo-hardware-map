# `com.apple.driver.ApplePearlExclaveSEPDriver`

- Name: ApplePearlExclaveSEPDriver
- Version: `1`
- UUID: `8DAFA6AD-91C4-3DB7-892D-D4972FD23838`
- Source version: `980.40.13.0.1`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleH10PearlCameraInterface`](com.apple.driver.AppleH10PearlCameraInterface.md) 1.0.0, [`com.apple.driver.ApplePearlSEPDriver`](com.apple.driver.ApplePearlSEPDriver.md) 1.0.0, [`com.apple.driver.AppleSEPManager`](com.apple.driver.AppleSEPManager.md) 1.0.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.iokit.AppleSEPGenericTransfer`](com.apple.iokit.AppleSEPGenericTransfer.md) 1.0.0, [`com.apple.iokit.IOBiometricFamily`](com.apple.iokit.IOBiometricFamily.md) 1.0.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.4, [`com.apple.iokit.IOSurface`](com.apple.iokit.IOSurface.md) 52.6.0, [`com.apple.kec.corecrypto`](com.apple.kec.corecrypto.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### ApplePearlExclaveSEPDriver
- `CFBundleIdentifier`: `com.apple.driver.ApplePearlExclaveSEPDriver`
- `IOClass`: `ApplePearlExclaveSEPDriver`
- `IOMatchCategory`: `com_apple_driver_ApplePearlSEPDriver`
- `IONameMatch`: `sep-endpoint,eprl`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePearlExclaveSEPDriver`
- `IOProbeScore`: `1001`
- `IOProviderClass`: `AppleSEPDeviceService`
- `IOUserClientClass`: `ApplePearlExclaveUserClient`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `ApplePearlExclaveSEPDriver` | 0xbb8 | ApplePearlSEPDriver → IOSEPBiometricService → IOBiometricService → IOService → IORegistryEntry |
| `ApplePearlExclaveUserClient` | 0x108 | ApplePearlUserClient → IOBiometricUserClient → IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000025a0 off=0x006a0990-0x006a2f30 addr=0xfffffe00076a4990-0xfffffe00076a6f30 r--/r--   __TEXT            
	sz=0x000013e9 off=0x006a1058-0x006a2441 addr=0xfffffe00076a5058-0xfffffe00076a6441               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000ae1 off=0x006a2441-0x006a2f22 addr=0xfffffe00076a6441-0xfffffe00076a6f22               __TEXT.__os_log           
	sz=0x00000008 off=0x006a2f28-0x006a2f30 addr=0xfffffe00076a6f28-0xfffffe00076a6f30               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x000061d4 off=0x02377910-0x0237dae4 addr=0xfffffe000937b910-0xfffffe0009381ae4 r-x/r-x   __TEXT_EXEC       
	sz=0x00005dd4 off=0x02377910-0x0237d6e4 addr=0xfffffe000937b910-0xfffffe00093816e4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000400 off=0x0237d6e4-0x0237dae4 addr=0xfffffe00093816e4-0xfffffe0009381ae4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000149 off=0x049844d8-0x04984621 addr=0xfffffe000b9884d8-0xfffffe000b988621 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x049844d8-0x0498459c addr=0xfffffe000b9884d8-0xfffffe000b98859c               __DATA.__data             
	sz=0x00000080 off=0x00000000-0x00000080 addr=0xfffffe000b9885a0-0xfffffe000b988620               __DATA.__common           (Zerofill)
	sz=0x00000001 off=0x00000000-0x00000001 addr=0xfffffe000b988620-0xfffffe000b988621               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001150 off=0x01199ce8-0x0119ae38 addr=0xfffffe000819dce8-0xfffffe000819ee38 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x01199ce8-0x01199cf8 addr=0xfffffe000819dce8-0xfffffe000819dcf8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x01199cf8-0x01199d08 addr=0xfffffe000819dcf8-0xfffffe000819dd08         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000e60 off=0x01199d08-0x0119ab68 addr=0xfffffe000819dd08-0xfffffe000819eb68         __DATA_CONST.__const            
	sz=0x00000080 off=0x0119ab68-0x0119abe8 addr=0xfffffe000819eb68-0xfffffe000819ebe8         __DATA_CONST.__kalloc_type      
	sz=0x00000200 off=0x0119abe8-0x0119ade8 addr=0xfffffe000819ebe8-0xfffffe000819ede8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000050 off=0x0119ade8-0x0119ae38 addr=0xfffffe000819ede8-0xfffffe000819ee38         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 138 at 0x04ae1d88
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     8DAFA6AD-91C4-3DB7-892D-D4972FD23838
008: LC_SOURCE_VERSION           980.40.13.0.1
009: LC_FUNCTION_STARTS          offset=0x004aacb58 size=0x80
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `ApplePearlExclaveSEPDriver`
- `CFBundleIdentifier`: `com.apple.driver.ApplePearlExclaveSEPDriver`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `ApplePearlExclaveSEPDriver`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2016-2017 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/ApplePearlExclaveSEPDriver.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898849392`
- `_PrelinkExecutableRelativePath`: `ApplePearlExclaveSEPDriver`
- `_PrelinkExecutableSize`: `39437`
- `_PrelinkExecutableSourceAddr`: `-2198898849392`
- `_PrelinkKmodInfo`: `-2198828710696`

## Strings (181) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `%s: Ignoring frame in enrollOnHold state\n`
- `%s: sensorBootNonce first/last bytes: %02x %02x ... %02x %02x\n`
- `%s: Summerville certificate loading pending\n`
- `%s: Waiting for prox state to clear...\n`
- `%s <- cameraID:%u, streamingSessionDataOut:%p\n`
- `%s -> err:0x%x, sensorType:%d\n`
- `%s: _captureBracketState:%s (%u)\n`
- `%s: frameId:[%d:%d], contextIdx:%u\n`
- `%s: requesting capture bracket (bio caputure): sessionID:%u, numOfDoubles:%u, doubleOrder:%u, probePatternType:%u, probePatternIndex:%u\n`
- `%s <- sessionID:%u\n`
- `%s: cameraID:%u, sessionType:%u\n`
- `%s: cameraID:%u\n`
- `%s: Clearing _brunorKeyUnwrappingState (%d)\n`
- `Couldn't create OS Log for 'com.apple.BiometricKit.SEPDriver-Pearl-UserClient'!\n`
- `ApplePearlExclaveUserClient::%s -> err:0x%x\n`
- `%s: Rounding up the number of requested frames: %u -> %zu\n`
- `%s: requesting capture bracket (probing pattern): sessionID:%u, numOfDoubles:%u, doubleOrder:%u, probePatternType:%u, probePatternIndex:%u\n`
- `%s: Reference frames info record loading pending\n`
- `%s: bioCapture frame received with _bioCaptureFramesToProcess == 0\n`
- `%s: Ignoring unexpected frame (_secureFaceDetectMode:%u, _secureFaceDetectSessionID:%u, _captureBracketState:%s)\n`
- `%s: frameId:[%d:%d] --> SPRL (processingInSEP:%d) (rawFrameProxyId:0x%llx, metaFrameProxyId:0x%llx) fid-griffin-prlkxt\n`
- `%s: Camera error: %s (%d)\n`
- `ApplePearlExclaveUserClient::%s -> success:%d\n`
- `%s: release bracket frame: frameId:[%d:%d]\n`
- `%s <- sessionID:%u, state:%u, lastFeedback:%u, lastOcclusionState:%u, lastWUPE:%u\n`
- `%s: Got frame when running secure streaming check, waking up the other thread\n`
- `%s: Skipping trigger BioCapture for enrollment. _bioCaptureFramesToProcess: %zu\n`
- `%s: cameraID:%x, _commandMode:%s (%u)\n`
- `ApplePearlExclaveUserClient::%s <- \n`
- `ApplePearlExclaveUserClient::%s -> \n`
- `%s <- \n`
- `%s: requesting pause: sessionID:%u\n`
- `%s -> skipped:%d, err:0x%x\n`
- `%s <- sensorTypeOut:%p\n`
- `%s: sensorType:%d\n`
- `ApplePearlExclaveUserClient::%s: Client %s: '%s' (pid %d) type:%u\n\n`
- `%s -> err:0x%x\n`
- `%s <- sessionID:%u, frameId:[%d:%d], isBracket:%u, isRGB:%u, rawFrameProxyId:0x%llx, metaFrameProxyId:0x%llx fid-griffin-prlkxt\n`

**[__TEXT.__cstring]**

- `result`
- `disconnected`
- `bcOptSize == sizeof(biocapture_options_t)`
- `ERROR: %s: Unknown sensor type (deviceID: 0x%04x) - assuming %d to be able to proceed\n\n`
- `selectSecureFaceDetectFlowForAutoRetryMatch`
- `_logging->releaseDebugForFrameId(pages.frameId)`
- `streamingSessionData::nonce`
- `unwrapOutputKeyHmac`
- `clientClose`
- `ApplePearlExclaveSEPDriver`
- `isPearlDisabledSpecific`
- `requestProbingPattern`
- `unwrapHostSig`
- `pearlSupportSetSensorUnwrapData`
- `_commandGate`
- `pattern`
- `request->sessionType == kSessionTypeDefault`
- `streamingSessionDataLength == sizeof(*streamingSessionData)`
- `ariesEphPublicKeySig`
- `cameraStateHandlerSwitch`
- `resetSecureFaceDetectState`
- `_camIn`
- `err == 0 `
- `(request->sessionType == kSessionTypeDefault) || (request->sessionType == kSessionTypeBrunorUnwrap)`
- `pearlSupportEstablishSharedSecret`
- `processFrameMetadata`
- `_captureBracketContext.receivedRGBFrames < _captureBracketContext.requestedRGBFrames`
- `getStreamingSessionData`
- `cmd`
- `cmd->version == 1`
- `unwrapSessionRequest`
- `unwrapInputHostIV`
- `unwrapHostTag`
- `ApplePearlExclaveUserClient`
- `_clientName`
- `logConnectionChange`
- `requestBioCapture`
- `_brunorKeyUnwrappingState == kBrunorKeyUnwrappingStateNone`
- `SEPDriver-Pearl-UserClient`
- `ERROR: ApplePearlExclaveUserClient::%s: Unsupported connection type:%u\n\n`
- `<unknown>`
- `(request->cameraID == kPearlCameraID_IR) || (request->cameraID == kPearlCameraID_RGB)`
- `selectSecureFaceDetectFlowForMatch`
- `TriggerBioCheck`
- `payload`
- `bcOpt`
- `ProbingPattern`
- `unwrapInputKey`
- `/Library/Caches/com.apple.xbs/DC80B99A-71A7-45F7-A533-4926D6628DC9/TemporaryDirectory.RiHkKs/Sources/Pearl_Kernel/ApplePearlExclaveSEPDriver/ApplePearlExclaveUserClient.cpp`
- `_matchSeqType == kMatchSeqSlowPath`
- `makeProcessingThreadsRealTime() == 0 `
- `sensorBootNonce`
- `unwrapOutputKey`
- `blockErr == 0 `
- `sprlInfo`
- `checkSecureStreaming`
- `streamingSessionData`
- `pearlSupportGenerateHostUnwrapData`
- `sizeof(unwrapSessionOptions.wrappedKey) == _brunorWrappedKey->getLength()`
- `unwrapSessionRequestSize == sizeof(*unwrapSessionRequest)`
- `site.ApplePearlExclaveSEPDriver`
- `handleCameraMessage_ReportError`
- `streamingSessionData::ivE`
- `ariesEphPublicKey`
- `_brunorWrappedKey`
- `ERROR: ApplePearlExclaveUserClient::%s: AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n\n`
- `handleSecureFaceDetectState`
- `_matchSeqType == kMatchSeqPasscodeChallenge`
- `_matchSeqType != kMatchSeqPasscodeChallenge`
- `_clientPID`
- `requestSecureFaceDetectRaw`
- `!(flags & kSecureFDRequestFlagMotionDetect)`
- `_eisplibAlgoType != kEisplibAlgoUninitialized`
- `unwrapInputKeyHmac`
- `_hasMirage != kBoolNotSet`
- `handleFrameProcessedMessage`
- `streamingSessionData::lfsrE`
- `handlePearlSupportCommand`
- `_brunorKeyUnwrappingState == kBrunorKeyUnwrappingStateUnwrapSequence`
- `handlePearlSupportTermination`
- `com.apple.BiometricKit`
- `provider`
- `message`
- `getRGBSessionSensorType`
- `false`
- `startPasscodeChallengeSequence`
- `enqueuedInSEP`
- `enqueuedInSEPSize == sizeof(*enqueuedInSEP)`
- `requestPowerAssertion(true) == 0 `
- `Off`
- `streamingSessionData::hostMasterKeyIdx`
- `ERROR: %s: Summerville certificate loading failed\n\n`
- `ProbingPatternDone`
- `Unknown`
- `streamingSessionData for cameraID`
- `sessionOptions.sensorType == kSavageSensorTypeAries || sessionOptions.sensorType == kSavageSensorTypeHamal`
- `initWithTask`
- `YonkersSNUM`
- `rgbSessionSensorType != kRGBSensorTypeUnknown`
- `handlePearlSupportTermination_block_invoke`
- `ERROR: %s: AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n\n`
- `selectSecureFaceDetectFlowForHoldMatch`
- `_runningPasscodeChallenge`
- `patternSize == sizeof(uint8_t)`
- `BioCheckDone`
- `pearlSupportGenerateHostEphemeralKey`
- `changeString`
- `outSize && (*outSize >= sizeof(response))`
- `unwrapOutputSensorSig`
- `121111121222121211212111111111111111111111211211222222221222112222222211112111112122221212111222222222222121122211122222221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222212212222222221212222222222122212222222222222222121211222222`
- `/Library/Caches/com.apple.xbs/DC80B99A-71A7-45F7-A533-4926D6628DC9/TemporaryDirectory.RiHkKs/Sources/Pearl_Kernel/ApplePearlExclaveSEPDriver/ApplePearlExclaveSEPDriver.cpp`
- `makeProcessingThreadsNonRealTime() == 0 `
- `selectSecureFaceDetectFlowForEnroll`
- `BioCheck`
- `outData`
- `ariesSessionDataSize == sizeof(*ariesSessionData)`
- `initializeEngine`
- `requestANEPowerAssertion(kANEPowerModeOff) == 0 `
- `_captureBracketContext.receivedIRFrames < _captureBracketContext.requestedIRFrames`
- `unwrapOutputSensorIV`
- `i8@?0`
- `site.ApplePearlExclaveUserClient`
- `connected`
- `streamingSessionDataOut`
- `sessionOptions.sensorType == kRGBSensorTypeSummerville`
- `sprlInfoSize == sizeof(*sprlInfo)`
- `ERROR: %s: Reference frames info record loading failed\n\n`
- `state.sessionID == _secureFaceDetectSessionID`
- `roundUpFrames < 65535`
- `bcOpt->probePattern == kProbePatternA || bcOpt->probePattern == kProbePatternB`
- `0`
- `sensorTypeOut`
- `ERROR: %s: YonkersSNUM not available, cannot proceed\n\n`
- `frame`
- `payloadSize >= sizeof(*request)`
- `pearlSupportClearSession`
- `121111121222121211111111111211212`
- `state.state < kSecureFDStateCount`
- `owningTask != ((task_t ) nullptr)`
- `stop`
- `selectSecureFaceDetectFlowForEnrollSuspendStateChange`
- `(feedbackSize == 0) || (feedback && feedbackSize == sizeof(enroll_meta_feedback_t))`
- `ariesSessionData`
