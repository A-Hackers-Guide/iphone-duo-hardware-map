# `com.apple.driver.AppleM68Buttons`

- Name: AppleM68Buttons
- Version: `1.0.0d1`
- UUID: `EB638DF5-F7CB-3DA8-B82C-B812B3C79B87`
- Source version: `132.40.2.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.5, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (2) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/buttons`](../devicetree/root__buttons.md) | `AppleM68Buttons` | `buttons` |
| [`/buttons`](../devicetree/root__buttons.md) | `AppleM68Buttons` | `buttons` |

## IOKit personalities (1) [KC]

### AppleM68Buttons
- `CFBundleIdentifier`: `com.apple.driver.AppleM68Buttons`
- `IOClass`: `AppleM68Buttons`
- `IONameMatch`: `buttons`
- `IOPersonalityPublisher`: `com.apple.driver.AppleM68Buttons`
- `IOProviderClass`: `IOPlatformDevice`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleButtonsDispatchFunction` | 0x30 | AppleARMFunction |
| `AppleM68Buttons` | 0x460 | AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AppleTimerQueueEventSource` | 0x80 | IOTimerEventSource → IOEventSource |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1800)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00005e8f off=0x0063cc80-0x00642b0f addr=0xfffffe0007640c80-0xfffffe0007646b0f r--/r--   __TEXT            
	sz=0x00004eff off=0x0063d3e8-0x006422e7 addr=0xfffffe00076413e8-0xfffffe00076462e7               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000208 off=0x006422e8-0x006424f0 addr=0xfffffe00076462e8-0xfffffe00076464f0               __TEXT.__const            
	sz=0x0000061f off=0x006424f0-0x00642b0f addr=0xfffffe00076464f0-0xfffffe0007646b0f               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0001d558 off=0x021e7450-0x022049a8 addr=0xfffffe00091eb450-0xfffffe00092089a8 r-x/r-x   __TEXT_EXEC       
	sz=0x0001d088 off=0x021e7450-0x022044d8 addr=0xfffffe00091eb450-0xfffffe00092084d8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000004d0 off=0x022044d8-0x022049a8 addr=0xfffffe00092084d8-0xfffffe00092089a8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001f1 off=0x04978840-0x04978a31 addr=0xfffffe000b97c840-0xfffffe000b97ca31 rw-/rw-   __DATA            
	sz=0x000000ca off=0x04978840-0x0497890a addr=0xfffffe000b97c840-0xfffffe000b97c90a               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000b97c910-0xfffffe000b97c998               __DATA.__common           (Zerofill)
	sz=0x00000099 off=0x00000000-0x00000099 addr=0xfffffe000b97c998-0xfffffe000b97ca31               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000027a0 off=0x011626a0-0x01164e40 addr=0xfffffe00081666a0-0xfffffe0008168e40 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x011626a0-0x011626b0 addr=0xfffffe00081666a0-0xfffffe00081666b0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x011626b0-0x011626c0 addr=0xfffffe00081666b0-0xfffffe00081666c0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000bd8 off=0x011626c0-0x01163298 addr=0xfffffe00081666c0-0xfffffe0008167298         __DATA_CONST.__const            
	sz=0x00000400 off=0x01163298-0x01163698 addr=0xfffffe0008167298-0xfffffe0008167698         __DATA_CONST.__kalloc_type      
	sz=0x000014a0 off=0x01163698-0x01164b38 addr=0xfffffe0008167698-0xfffffe0008168b38         __DATA_CONST.__kalloc_var       
	sz=0x00000268 off=0x01164b38-0x01164da0 addr=0xfffffe0008168b38-0xfffffe0008168da0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000098 off=0x01164da0-0x01164e38 addr=0xfffffe0008168da0-0xfffffe0008168e38         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x01164e38-0x01164e40 addr=0xfffffe0008168e38-0xfffffe0008168e40         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 173 at 0x04adea70
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     EB638DF5-F7CB-3DA8-B82C-B812B3C79B87
008: LC_SOURCE_VERSION           132.40.2.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa99c0 size=0x210
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleM68Buttons`
- `CFBundleGetInfoString`: `Copyright © 2015 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleM68Buttons`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleM68Buttons`
- `CFBundleNumericVersion`: `16785409`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0d1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2015 Apple Inc. All rights reserved.`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleM68Buttons.kext`
- `_PrelinkExecutableLoadAddr`: `-2198899258240`
- `_PrelinkExecutableRelativePath`: `AppleM68Buttons`
- `_PrelinkExecutableSize`: `155000`
- `_PrelinkExecutableSourceAddr`: `-2198899258240`
- `_PrelinkKmodInfo`: `-2198828758976`

## Strings (632) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `!context`
- `array of ACMParameter`
- `DebugState`
- `dataLength == sizeof(uint32_t)`
- `dataLength == sizeof(credData->identityUuid)`
- `dataLength`
- `(size - offset) >= sizeof(uint8_t)`
- `requirementSize <= reqSize`
- `getLengthOfParameters`
- `site.ACMCredential.ACMCredentialDataSecureIntent`
- `LibCall_ACMContextDelete`
- `credential->type == kACMCredentialTypeKextDenyListApplePay || credential->type == kACMCredentialTypeKextDenyListFairPlay`
- `LibCall_ACMGlobalContextVerifyPolicyEx`
- `operationLength`
- `params`
- `site.ACMCredential.ACMCredentialDataBiometryMatchAttempted`
- `site.ACMRequirement.ACMRequirementDataPushButtonWithAttributes`
- `StackshotMask`
- `LibCall_ACMContextCredentialGetProperty`
- `sourceContextExternalForm && sourceContextExternalFormLength == sizeof(ACMHandle)`
- `performCommandV3`
- `0`
- `inSize <= kACMContextDataMaxSize`
- `responseSize == sizeof(uint32_t)`
- `size >= reqSize`
- `credLen <= *outSize`
- `dataLength == sizeof(ACMCredentialDataSignature)`
- `!param->parameterDataLength`
- `LibCall_ACMContextUnloadToImage`
- `commandBuffer`
- `%s: %s (len=%u): acl:`
- `credentialType`
- `remaining >= respSize`
- `ACMCredential - ACMCredentialDataKextDenyList`
- `site.ACMRequirement.ACMRequirementDataKeyRef`
- `StackshotMaskOn`
- `DiagnosticMaskOn`
- `dataLength == USER_OUTPUT_SEID_SIZE`
- `commandSize == sizeof(commandBuffer)`
- `0123456789abcdef`
- `ACMCredential - ACMCredentialDataSecureIntent`
- `preflight`
- `ACMRequirement - ACMRequirementDataPushButton`
- `ACMRequirement - ACMRequirementDataBiometryMatchAttempted`
- `LibCall_ACMRequirementDelete`
- `context || scope == kACMScopeGlobal`
- `requirement->type == kACMRequirementTypePassphraseEntered`
- `bufferSize`
- `site.ACMRequirement.ACMRequirementDataPushButton`
- `ACMRequirement - ACMRequirementDataPasscodeValidatedWithAttributes`
- `tmpAcl`
- `reqLen <= *bufferSize`
- `ACMRequirement - ACMRequirementDataAccessGroups`
- `stackshot-mask`
- `dataLength == sizeof(uuid_t)`
- `requirement->type == kACMRequirementTypeKofN`
- `(ctxImage && ctxImageSize && ctxImageSize <= kACMContextImageMaxSize)`
- `ptr`
- `button-debounce-off_%s`
- `size >= sizeof(ACMHandle) + sizeof(ACMContextDataType) + sizeof(uint32_t)`
- `(enrollmentState && enrollmentStateLength && enrollmentStateLength <= ENROLLMENT_STATE_MAX_SIZE) || (!enrollmentState && !enrollmentStateLength)`
- `currentStateSize <= 1`
- `PressCountUsagePairs`
- `UTIL_OPTIONAL_BUFFER(outBuffer,outSize)`
- `handle`
- `(size - offset) >= opLength`
- `size >= sizeof(ACMHandle) + sizeof(ACMContextDataType) + sizeof(uint8_t)`
- `dataLength == sizeof(ACMCredentialDataContinuityUnlock)`
- `site.ACMRequirement.ACMRequirementDataAccessGroups`
- `AppleARMBacklight`
- `HID: Button NMI`
- `AppleCredentialManager`
- `dataLength == sizeof(ACMHandle)`
- `LibCall_ACMContextContainsCredentialTypeEx`
- `DeserializeVerifyAclConstraint`
- `ACMCredential - ACMCredentialDataPassphraseExtractable`
- `outSize`
- `credential2`
- `param->parameterDataLength && (param->parameterDataLength <= MAX_ACCESS_GROUPS_LEN)`
- `ShutdownDebugDelay`
- `AppleButtonsDispatchFunction`
- `dataLength == UUID_LEN`
- `length`
- `LibCall_ACMTRMLoadState`
- `responseBufferSize >= 3 * sizeof(uint32_t)`
- `op`
- `size >= sizeof(ACMUnlockSecretType)`
- `command`
- `credential`
- `remaining >= cmdSize`
- `os_add_overflow(pos, outDataSize, &end) == 0 `
- `ACMKernContextAddCredentialWithScope`
- `com.apple.ButtonDriver`
- `LibCall_ACMPing`
- `dataLength == sizeof(ACMCredentialDataKextDenyList)`
- `param->parameterDataLength == sizeof(uint64_t)`
- `down`
- `dispatched`
- `/Library/Caches/com.apple.xbs/4776FB82-4876-4747-BD9A-F14E510003B9/TemporaryDirectory.gzqdtN/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp`
- `requirement->type == kACMRequirementTypeAP`
- `requirement`
- `ACMRequirement - ACMRequirementDataBiometryMatched`
- `\"No button at interrupt index %d\" @%s:%d`
- `ringeren`
- `Priority Button`
- `dataLength == DATABASE_HASH_SIZE`
- `(inData && inSize) || (!inData && !inSize)`
- `processAclCommandInternal`
- `aclRequiresPasscodeInternal`
- `dataLength == sizeof(ACMCredentialDataUserOutputDisplayed)`
- `panic-reset-type`
- `(keybagUuid && keybagUuidLength == UUID_LEN) || (!keybagUuid && !keybagUuidLength)`
- `\n`
- `/Library/Caches/com.apple.xbs/4776FB82-4876-4747-BD9A-F14E510003B9/TemporaryDirectory.gzqdtN/Sources/AppleCredentialManager_KernelLibs/common/LibSerialization.c`
- `dataLength == sizeof(ACMCredentialDataSecureIntent)`
- `equal`
- `writePos`
- `os_add_overflow(pos, inDataSize, &end) == 0 `
- `ButtonNames`
- `LibCall_ACMContextSetData`
- `Util_ReadFromBuffer`
- `ACMKernelLib`
- `DOWN`
- `B16@?0^{OSObject=^^?i}8`
- `%s: %s: acl = %p, aclLength = %zu.\n`
- `requirePasscode`
- `(parameters && parametersCount) || (!parameters && !parametersCount)`
- `credCount <= MAX_CREDENTIAL_LIST_LEN`
- `site.ACMRequirement.ACMRequirementDataUserOutputDisplayed`
- `fallback`
- `response->version >= kCmdCurrentVersion_ContextGetInfo`
- `DeserializeProcessAcl`
- `ACMKernGetEnvironmentVariable`
- `helpdouble`
- `SetButtonLogging`
- `response.body.found`
- `site.ACMParameter`
- `DeallocCredentialList`
- `%s: %s: mem: type=%s ptr=%p size=%u (total=%u raw=%u data=%u types=%u) %s:%d (%s).\n`
- `os_add_overflow((uintptr_t)inBuffer, pos, (uintptr_t *)&readPtr) == 0 `
- `ACMRequirement`
- `home-button-type`
- `AppleM68Buttons`
- `\"AppleM68Buttons::handleStart failed to allocate pressCountPairs\" @%s:%d`
- `press-count-triple-timeout`
- `responseSize == sizeof(response.body)`
- `_allocatedMem.data >= size`
- `site.ACMCredential.ACMCredentialDataKextDenyList`
- `service`
- `response->resVersion > 0`
- `param.parameterData && param.parameterDataLength == sizeof(uint8_t)`
- `credentialProperty`
- `remaining >= sizeof(uint32_t)`
- `ACMRequirement - ACMRequirementDataRatchet`
- `diagnostic-mask-all`
- `(size - offset) >= (policyLength + 1)`
- `size >= sizeof(uint32_t)`
- `TestDispatchKeyboardEvent`
- `opcode == kCmdPing || opcode == kCmdPingOnDoubleClick`
- `unlockSecret && unlockSecretLength && unlockSecretType`
- `req`
- `cred`
- `offset + *dataSize <= size`
- `site.ACMCredential`
- `ACMRequirement - ACMRequirementDataKofN`
- `menu`
- `size >= sizeof(ACMHandle) + sizeof(ACMCredentialType) + sizeof(ACMCredentialProperty)`
- `site.ACMCredential.ACMCredentialDataAP`
- `size >= sizeof(ACMHandle) + sizeof(uint32_t) + sizeof(uint32_t)`
- `(data && dataLength && dataLength <= kACMEnvironmentVariableMaxDataLength) || (!data && !dataLength)`
- `AppleTimerQueueEventSource`
- `SydiagnoseMaxHoldDelay`
- `LibCall_ACMTRMSaveState`
- `NULL`
- `stateOutBuffer && stateInOutSize`
- `outBuffer && outSize`
- `handle || scope == kACMScopeGlobal`
- `size >= sizeof(ACMHandle)`
- `debug`
- `LibCall_BuildCommand`
- `context`
- `LibCall_ACMContextVerifyPolicyEx`
- `CoverDetached`
- `commandSize`
- `requirement->type == kACMRequirementTypeRatchet`
- `LibCall_ACMGetEnvironmentVariable`
- `site.ACMRequirement.ACMRequirementDataPassphraseEntered`
- `site.ACMRequirement.ACMRequirementDataSecureStateWithAttributes`
- `acmService`
- `1`
- `ACMCredential - ACMCredentialDataAP`
- `dataLength == sizeof(credData->accPubKey)`
- `LibCall_ACMPublishTrustedAccessories`
- `os_add_overflow((uintptr_t)outBufferOpt, pos, (uintptr_t *)&writePtr) == 0 `
- `ringerab`
- `function-lcd_ldo`
- `kern.darkboot`
- `ACMKernelTransport`
- `handleWithPayload`
- `policyLength <= MAX_POLICY_LENGTH`
- `ACMKernGlobalContextAddCredential`
- `button-priority_%s`
- `ButtonDownFilteredMask`
- `req->dataLength == sizeof(ACMRequirementDataAnd)`
- `scope`
- `site.AppleTimerQueueEvent`
- `PressCountDoublePressTimeout`
- `default`
- `!preflightFound || allowPreflightParameter`
- `param->parameterDataLength == sizeof(int32_t)`
- `outBuffer && offset`
- `site.ACMCredential.ACMCredentialDataContinuityUnlock`
- `ACMRequirement - ACMRequirementDataUserOutputDisplayed`
- `ACMHandleWithPayload`
- `size >= sizeof(ACMRequirement)`
- `/Library/Caches/com.apple.xbs/4776FB82-4876-4747-BD9A-F14E510003B9/TemporaryDirectory.gzqdtN/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp`
- `nonAutoDisposable requires tracking support`
- `requirement->type == kACMRequirementTypeBiometryMatched`
- `data && dataLength`
- `keybagUuid && keybagUuidLength == sizeof(uuid_t)`
- `LibCall_ACMSecSetBuiltinBiometry`
- `%02x `
- `size >= credSize`
- `long-press-timeout`
- `(size - newOffset) >= params[i].parameterDataLength`
- `1121`
- `AlternateLongPressHandling`
- `LibCall_ACMContextVerifyPolicyAndCopyRequirementEx`
- `remap-usages`
- `processAclInternal`
- `LibCall_ACMSecContextGetUnlockSecret`
- `LibSer_ACMDeserializeSEPControlCode`
- `param->parameterDataLength == sizeof(uint32_t)`
- `paramsCount <= MAX_PARAMETERS_COUNT`
- `UTIL_OPTIONAL_ARRAY(parameters, parametersCount)`
- `(data && dataLength && dataLength <= kACMControlMaxDataLength) || (!data && !dataLength)`
- `*resultLength >= respDataSize`
- `dataLength == sizeof(ACMCredentialDataPassphraseExtractable)`
- `site.ACMCredentialRef`
- `array of ACMCredentialRef`
- `DeserializeCredentialList`
- `parametersLength + param->parameterDataLength >= parametersLength`
- `1211121111211111`
- `AppleM68Buttons.cpp`
- `dataLength == sizeof(int32_t)`
- `constraintSatisfied`
- `size >= requiredSize`
- `222221111111111`
- `site.ACMRequirement.ACMRequirementDataPasscodeValidatedWithAttributes`
- `ACMKernContextCredentialGetProperty`
- `capture`
- `responseSize == sizeof(response)`
- `Util_AllocRequirement`
- `ACMKernContextSetData`
- `press-count-usage-pairs`
- `DarkBootPending`
- `data`
- `ctxImageOutBuffer && ctxImageInOutSize`
- `verifyAclConstraintInternal`
- `responseData && responseDataSize`
- `params[i].parameterData`
- `ACMKernContextVerifyPolicyAndCopyRequirementEx`
- `SetButtonDelay`
- `dataLength <= sizeof(credData->signature)`
- `212`
- `LibCall_ACMContexAddCredentialWithScope`
- `LibCall_ACMKernelControl`
- `credential->type == kACMCredentialTypePasscodeValidated2`
- `constraintState`
- `Util_AllocCredential`
- `halleffect`
- `PressCountTrackingEnabled`
- `LongPressTimeout`
- `forced_shutdown_debug_key_mask`
- `LibCall_ACMKernDoubleClickNotify`
- `LibCall_ACMSecCredentialProviderEnrollmentStateChangedForUser`
- `btn_rst`
- `site.AppleButtonsDispatchFunction`
- `site.ACMHandleWithPayload`
- `LibCall_ACMContextRemoveCredentialsByValueAndScope`
- `LibCall_ACMContextGetInfo`
- `aclConstraint && aclConstraintLength`
- `LibCall_ACMSecSetBiometryAvailability`
- `%s: %s: requirePasscode = %p.\n`
- `alternate-long-press`
- `app`
- `IONVRAM-SYNCNOW-PROPERTY`
- `!dataSize || data`
- `dataLength == sizeof(ACMPassphrasePurpose)`
- `dataLength == sizeof(ACMCredentialDataPasscodeValidated2)`
- `dataType != kACMContextDataTypeUnknown`
- `hold`
- `Util_DeallocRequirement`
- `\"AppleM68Buttons::handleStart failed to allocate acm threadcall\" @%s:%d`
- `ShutdownNVRAMSyncDelay`
- `performCommand`
- `LibCall_ACMSetEnvironmentVariable`
- `Util_SafeDeallocParameters`
- `DiagnosticMaskAny`
- `err == kACMErrorSuccess`
- `dataLength == sizeof(ACMCredentialDataBiometryMatchAttempted)`
- `buffer && unlockSecret && unlockSecretSize && unlockSecretType`
- `up`
- `dataLength == sizeof(ACMKextDenyListFormat)`
- `count`
- `DeserializeVerifyPolicy`
- `ACMCredential - ACMCredentialDataBiometryMatched`
- `ACMKernControl`
- `/Library/Caches/com.apple.xbs/4776FB82-4876-4747-BD9A-F14E510003B9/TemporaryDirectory.gzqdtN/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c`
- `LibCall_ACMContextGetData`
- `param->parameterDataLength == UUID_LEN`
- `ACMCredential - ACMCredentialDataBiometryMatchAttempted`
- `site.ACMRequirement.ACMRequirementDataBiometryMatchAttempted`
- `dataLength == sizeof(credData->accUUID)`
- `size - offset >= sizeof(ACMScope)`
- `site.AppleTimerQueueEventSource`
- `EventType`
- `SetButtonProperties`
- `Util_WriteToBuffer`
- `site.ACMRequirement.ACMRequirementDataKofNWithAttributes`
- `ACMKernGlobalContextRemoveCredentialsByType`
- `reqBufferSize >= sizeof(uint32_t)`
- `parameters`
- `aclConstraint`
- `voldown`
- `hesattach`
- `authMethodInst`
- `ACMCredential - ACMCredentialDataPassphraseEntered`
- `ACMKernContextCreate`
- `forced_shutdown_debug_delay`
- `transport`
- `externalForm`
- `dataLength == USER_OUTPUT_HASH_SIZE`
- `param`
- `(size - newOffset) >= sizeof(ACMParameterType) + sizeof(uint32_t)`
- `end <= inBufferSize`
- `ACMRequirement - ACMRequirementDataAP`
- `YES`
- `%s: %s: returning.\n`
- `%s: %s: maxGlobalCredentialAge = %u.\n`
- `context && outSize && outBuffer`
- `site.ACMCredential.ACMCredentialDataSignature`
- `ACMKernContextCreateWithExternalForm`
- `%s: %s: returning, err = %ld, var=%u.\n`
- `targetContextExternalForm && targetContextExternalFormLength == sizeof(ACMHandle)`
- `21111111111`
- `ACMKernPingOnDoubleClick`
- `panic-usage`
- `initAppleCredentialService`
- `context not found`
- `requirement->type == kACMRequirementTypePushButtonPressed`
- `site.ACMRequirement.ACMRequirementDataOr`
- `button-delay_%s`
- `LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx`
- `acm_mem_free_info`
- `function-set_dbl_click_ms`
- `%s: %s: called.\n`
- `responseBuffer`
- `*unlockSecretLength >= dataSize`
- `buffer && type`
- `volup`
- `dataLength == sizeof(uid_t)`
- `ACMRequirement - ACMRequirementDataPushButtonWithAttributes`
- `SydiagnoseMinHoldDelay`
- `os_add_overflow(sizeof(acm_command_t), dataSize, &cmdSize) == 0 `
- `trackingSupported || !nonAutoDisposableRequested`
- `LibCall_ACMContexRemoveCredentialsByTypeAndScope`
- `LibCall_ACMSecContextVerifyAclConstraintAndCopyRequirement`
- `/Library/Caches/com.apple.xbs/4776FB82-4876-4747-BD9A-F14E510003B9/TemporaryDirectory.gzqdtN/Sources/AppleCredentialManager_KernelLibs/common/CommonMem.c`
- `consumedBytes`
- `req->dataLength == sizeof(ACMRequirementDataKofN)`
- `policyId`
- `dataLength == sizeof(ACMCredentialDataPasscodeValidated)`
- `copy`
- `credentialList[i]`
- `site.ACMRequirement.ACMRequirementDataKofN`
- `ACMRequirement - ACMRequirementDataAnd`
- `halleffect1`
- `ButtonUsagePairs`
- `inSize >= sizeof(acm_command_t)`
- `credential->type == kACMCredentialTypeBiometryMatched`
- `Util_DeallocCredential`
- `ACMRequirement - ACMRequirementDataPassphraseEntered`
- `site.ACMRequirement.ACMRequirementDataBiometryMatchedWithAttributes`
- `ButtonUnfilteredMask`
- `cmd = (acm_command_t *)acm_malloc_data(cmdSize)`
- `dataLength == 0`
- `site.ACMCredential.ACMCredentialDataPassphraseEntered`
- `function-wake_button_%s`
- `UsagePage`
- `SetButtonPriority`
- `requirement->dataLength >= sizeof(ACMRequirementDataBiometryMatched)`
- `size >= sizeof(ACMHandle) + sizeof(ACMCredential) + sizeof(ACMScope)`
- `site.ACMRequirement.ACMRequirementDataRatchet`
- `AppleTimerQueueEventSource::free called with non empty eventQueue\n`
- `panic-reset-timeout`
- `reqBuffer`
- `dataLength == sizeof(credData->confirmationHash)`
- `%s: %s: operation = %p, operationLength = %zu.\n`
- `handle && parameters && parametersCount`
- `ACMKernContextGetData`
- `diagnostic-mask-any`
- `%s: %s: returning, err = %ld.\n`
- `handle && dataType && data && dataSize`
- `command && commandSize >= sizeof(ACMSEPControlCode)`
- `!outBufferOpt || end <= outBufferSize`
- `ACMCredential`
- `<data>`
- `31111111111`
- `12111112122212121111111211111111111111111111111111111111111111112111111111122222222222222222222222222222222222222222222111122222222111112112`
- `function-button_%s`
- `ACMKernCredentialDelete`
- `stackshot triggered using diagnostic chord`
- `err == 0 `
- `LibCall_ACMContextCreateWithExternalForm`
- `Util_CreateRequirement`
- `\"AppleM68Buttons::handleStart failed to allocate nvram sync threadcall\" @%s:%d`
- `requirement->type == kACMRequirementTypeUserOutputDisplayed`
- `%s: %s: context = %p.\n`
- `outBuffer`
- `serializeParameters`
- `site.ACMRequirement.ACMRequirementDataBiometryMatched`
- `ACMRequirement - ACMRequirementDataKeyRef`
- `%s: %s (len=%u): operation:`
- `deserializeParameters`
- `press-count-double-timeout`
- `panic-reset-mask`
- `dataLength == sizeof(ACMCredentialDataAP)`
- `sigSize > 0 && sigSize <= kACMCredentialDataSignatureMaxSize`
- `site.ACMCredential.ACMCredentialDataUserOutputDisplayed`
- `Stackshot triggered using keycombo`
- `---`
- `(data && dataLength) || (!data && !dataLength)`
- `constraint`
- `site.ACMRequirement.ACMRequirementDataPasscodeValidated`
- `credential->type == kACMCredentialTypePassphraseExtractable`
- `inData && inSize`
- `22`
- `serviceMatchingDict`
- `credentialList`
- `accUUIDsSize % sizeof(uuid_t) == 0`
- `catacombUuid && catacombUuidLength == sizeof(uuid_t)`
- `responseBufferSize >= 3 * sizeof(uint32_t) + authMethodInstLength`
- `(size - offset) >= sizeof(ACMHandle)`
- `dataLength == sizeof(ACMCredentialDataBiometryMatched)`
- `handle && dataType && getSizeOnly`
- `credential->type == kACMCredentialTypePassphraseEntered`
- `dataLength == sizeof(ACMKextDenyListRevision)`
- `cred->domain == kACMDomainUnknown || cred->domain == kACMDomainUserMode || cred->domain == kACMDomainKernelMode || cred->domain == kACMDomainSecureEnclave`
- `param->parameterDataLength == sizeof(uint8_t)`
- `site.ACMRequirement.ACMRequirementDataAnd`
- `%s: %s: returning, -> ctx = %p.\n`
- `button-names`
- `LibCall_ACMSEPControl`
- `ACMCredential - ACMCredentialDataContinuityUnlock`
- `ACMKernSetEnvironmentVariable`
- `\"AppleM68Buttons::handleStart failed to instantiate %s\" @%s:%d`
- `121111`
- `LibCall_ACMSecContextCopyCredentialsArrayEx`
- `%s: %s: command = %u.\n`
- `dataLength == sizeof(ACMCredentialDataPassphraseEntered)`
- `ACMRequirement - ACMRequirementDataOr`
- `\"AppleM68Buttons::handleStart failed to allocate backlight threadcall\" @%s:%d`
- `site.ACMCredential.ACMCredentialDataPassphraseExtractable`
- `skey`
- `performCommandFunc`
- `credential->type == kACMCredentialTypeSecureIntent`
- `requirement->dataLength >= sizeof(ACMRequirementDataRatchet)`
- `dataOutBuffer && dataInOutLength`
- `(size - offset) >= sizeof(uint32_t)`
- `credential1`
- `ShutdownDebugMode`
- `validateCommand`
- `list`
- `(size - offset) >= sizeof(ACMContextProperty)`
- `/Library/Caches/com.apple.xbs/4776FB82-4876-4747-BD9A-F14E510003B9/TemporaryDirectory.gzqdtN/Sources/AppleCredentialManager_KernelLibs/common/CommonUtil.c`
- `help`
- `filtered`
- `SetDoubleClickTimeout`
- `site.ACMCredential.ACMCredentialDataPasscodeValidated`
- `use-button-type-keychords`
- `credential->type == kACMCredentialTypeUserOutputDisplayed`
- `heap underflow / memory tracking issue?`
- `ACMRequirement - ACMRequirementDataKofNWithAttributes`
- `IOPropertyExistsMatch`
- `ButtonPriorities`
- `dataLength <= sizeof(credData->unlockSecret)`
- `requirement->type == kACMRequirementTypeSecureIntent`
- `property`
- `size >= sizeof(ACMHandle) + sizeof(ACMContextDataType)`
- `defaults`
- `Filter Delay`
- `LibCall_ACMContextCreate`
- `requirement->type == kACMRequirementTypeKeyRef`
- `parametersCount <= MAX_PARAMETERS_COUNT`
- `/options`
- `LibCall_ACMContextCopyData`
- `accUUIDsSize <= kACMTrustedAccessoriesUUIDsDataMaxSize`
- `(parametersCount == 0 && !parameters) || (parametersCount > 0 && parameters)`
- `ACMRequirement - ACMRequirementDataBiometryMatchedWithAttributes`
- `halleffect2`
- `platform-type-consumer`
- `ACM`
- `inputBuffer`
- `operation`
- `param->parameterDataLength <= kACMParameterTypeACLMaxDataLength`
- `param->parameterDataLength == 0`
- `ACMRequirement - ACMRequirementDataPasscodeValidated`
- `PressCountTriplePressTimeout`
- `transport && context`
- `aclConstraintLength`
- `credentialList || (count == 0)`
- `ACMCredential - ACMCredentialDataPasscodeValidated2`
- `ACMKernCredentialCreate`
- `\"AppleM68Buttons::handleStart failed to allocate state serializer\" @%s:%d`
- `ButtonStateMask`
- `dataLength <= kACMPassphraseMaxLength`
- `(state && stateSize && stateSize <= kACMTRMMultiState_MaxSize) || (!state && !stateSize)`
- `_allocatedMem.total >= size`
- `*outSize >= requiredSize`
- `maxGlobalCredentialAge`
- `LibSer_ACMDeserializeEnvironmentVariableType`
- `IOService`
- `ShutdownDebugMask`
- `transport && context && value`
- `ACMKernContextDelete`
- `%s: %s: returning, err = %ld, code=%u.\n`
- `displayport,*`
- `policy`
- `(size - newOffset) >= sizeof(uint32_t)`
- `NO`
- `cred->numCredSets <= kACMContextPoolTotalCount`
- `param->parameterDataLength == sizeof(uid_t)`
- `buffer && offset && parameters && parametersCount`
- `ACMKernContextGetDataProperty`
- `site.AppleM68Buttons`
- `err != kACMErrorBadParameter`
- `buffer`
- `(policyLength <= MAX_POLICY_LENGTH)`
- `(size - offset) >= opLen`
- `subreqCount > 0 && subreqCount <= kACMRequirementSubRequirementMaxCount`
- `site.ACMCredential.ACMCredentialDataPasscodeValidated2`
- `ACMKernRequirementDelete`
- `ButtonInterruptTS(ns)`
- `AssertMacros: %s (value: 0x%lx), %s, file: %s:%d\n`
- `%s: %s: parameters = %p, parameterCount = %u.\n`
- `site.ACMRequirement.ACMRequirementDataSecureIntent`
- `ACMKernDoubleClickNotify`
- `filtered_%s_events`
- `LibCall_ACMGlobalContextCredentialGetProperty`
- `%s: %s: constraintState = %p.\n`
- `(size - offset) >= constraintLength`
- `unlockSecret && unlockSecretSize > 0`
- `ACMCredential - ACMCredentialDataSignature`
- `PanicEnabled`
- `responseBufferSize >= 2 * sizeof(uint32_t)`
- `acm_mem_alloc_info`
- `handle && parameters && parametersCount && command && commandSize`
- `ACMKernContextRemoveCredentialsByTypeAndScope`
- `DiagnosticMaskAll`
- `DiagnosticMaskTS`
- `forced_shutdown_mode`
- `UP`
- `transportContext`
- `policySatisfied`
- `ACMRequirement - ACMRequirementDataSecureStateWithAttributes`
- `outDataLength`
- `press-count-tracking`
- `credential->type == kACMCredentialTypeAP`
- `parametersCount`
- `ACMKernGlobalContextVerifyPolicyAndCopyRequirementEx`
- `button-debounce-on_%s`
- `CurrentTS(ns)`
- `credential->type == kACMCredentialTypeSignature`
- `!accUUIDsSize || accUUIDs`
- `ACMCredential - ACMCredentialDataPasscodeValidated`
- `ACMCredential - ACMCredentialDataUserOutputDisplayed`
- `dataLength == sizeof(credData->originator)`
- `responseBufferSize >= sizeof(Response)`
- `operation && operationLength`
- `(size - offset) >= tmpAclLength`
- `size >= sizeof(ACMCredential)`
- `size >= sizeof(ACMHandle) + sizeof(ACMCredentialType) + sizeof(ACMScope)`
- `ACMRequirement - ACMRequirementDataSecureIntent`
- `PowerState`
- `_acmService`
- `acl && aclLength`
- `acl`
- `aclLength`
- `context && outSize`
- `inSize >= sizeof(ACMEnvironmentVariable)`
- `site.ACMCredential.ACMCredentialDataBiometryMatched`
- `Usage`
- `inBuffer && readPos`
- `site.ACMRequirement`
- `site.ACMRequirement.ACMRequirementDataAP`
- `dataLength == SCRED_UUID_SIZE`
- `LibCall_ACMContextLoadFromImage`

**[__TEXT.__os_log]**

- `handleStart no interrupt for %s`
- `callPlatformFunction`
- `%s has larger debounce interval, deffering`
- `diagnostic triggered with mask %u`
- `Set button logging property is deprecated, %d`
- `set double sysdiagnose min hold duration to %u ms`
- `dispatchEventExt type %d latency %lld`
- `dispatchEventExt after dispatch type %d latency %lld`
- `sysdiagnose_notify_user: 0x%x`
- `Debug stackshot on forced shutdown`
- `%s %s event %s time = %llu delta = %llu`
- `set double sysdiagnose max hold duration to %u ms`
- `Warning: A keychord-based shutdown debug mode was requested (%u), but no keychord was specified. Disabling the shutdown debug feature`
- `_diagnosticMaskFallingEdge current ts %llu down ts %llu triggered %d`
- `Synced NVRAM before 2-finger reset`
- `AppleM68Buttons: dispatching keyboard event up:0x%x u:0x%x state:%d`
- `Power state change: %lu -> %lu`
- `shutdownDebugMode found: %s`
- `ButtonStates: %lu Index: %lu State: %lu Filter: %d Synthetic: %d`
- `Debug panic on forced shutdown, has LCD function: %s`
- `Shutdown is imminent, ButtonStateMask:0x%x ButtonDownFilteredMask:0x%x ButtonUnfilteredMask:0x%x CurrentTS:%llu InterruptTS:%llu %llu %llu %llu %llu`
- `interrupt for button: %s time = %llu`
- `failed to get NVRAM IORegistryEntry\n`
- `dispatchEventExt type: %d time = %llu`
- `matchingDict found: %s`
- `failed to sync NVRAM!`
- `dispatchEventExt keyboard:%d %d %d time = %llu`
- `set double click timeout to %d`
- `defaults found: %s`
- `shutdownDebugMode length %u shutdownDebugMode byte 0x%x`
- `kern_stack_snapshot_with_reason: 0x%x`
- `debounced button: %s, state: %s, time = %llu`
- `Ping ACM`
- `EDT info found for button at index %d, processing the button`
