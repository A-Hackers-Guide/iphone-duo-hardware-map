# `com.apple.driver.AppleLockdownMode`

- Name: AppleLockdownMode
- Version: `1`
- UUID: `99320B4E-0BE7-3E2D-B485-3294FE70391C`
- Source version: `128.40.5.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleLockdownMode
- `CFBundleIdentifier`: `com.apple.driver.AppleLockdownMode`
- `IOClass`: `AppleLockdownMode`
- `IOMatchCategory`: `AppleLockdownMode`
- `IOPersonalityPublisher`: `com.apple.driver.AppleLockdownMode`
- `IOProviderClass`: `IOResources`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleLockdownMode` | 0x88 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00005140 off=0x0054ef50-0x00554090 addr=0xfffffe0007552f50-0xfffffe0007558090 r--/r--   __TEXT            
	sz=0x00000110 off=0x0054f668-0x0054f778 addr=0xfffffe0007553668-0xfffffe0007553778               __TEXT.__const            
	sz=0x00004918 off=0x0054f778-0x00554090 addr=0xfffffe0007553778-0xfffffe0007558090               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00015608 off=0x020951c0-0x020aa7c8 addr=0xfffffe00090991c0-0xfffffe00090ae7c8 r-x/r-x   __TEXT_EXEC       
	sz=0x000153e8 off=0x020951c0-0x020aa5a8 addr=0xfffffe00090991c0-0xfffffe00090ae5a8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000220 off=0x020aa5a8-0x020aa7c8 addr=0xfffffe00090ae5a8-0xfffffe00090ae7c8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000119 off=0x04951b28-0x04951c41 addr=0xfffffe000b955b28-0xfffffe000b955c41 rw-/rw-   __DATA            
	sz=0x000000c6 off=0x04951b28-0x04951bee addr=0xfffffe000b955b28-0xfffffe000b955bee               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b955bf0-0xfffffe000b955c28               __DATA.__common           (Zerofill)
	sz=0x00000019 off=0x00000000-0x00000019 addr=0xfffffe000b955c28-0xfffffe000b955c41               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001ee0 off=0x0112e4d0-0x011303b0 addr=0xfffffe00081324d0-0xfffffe00081343b0 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x0112e4d0-0x0112e4d8 addr=0xfffffe00081324d0-0xfffffe00081324d8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x0112e4d8-0x0112e4e0 addr=0xfffffe00081324d8-0xfffffe00081324e0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000005f0 off=0x0112e4e0-0x0112ead0 addr=0xfffffe00081324e0-0xfffffe0008132ad0         __DATA_CONST.__const            
	sz=0x00000300 off=0x0112ead0-0x0112edd0 addr=0xfffffe0008132ad0-0xfffffe0008132dd0         __DATA_CONST.__kalloc_type      
	sz=0x000014a0 off=0x0112edd0-0x01130270 addr=0xfffffe0008132dd0-0xfffffe0008134270         __DATA_CONST.__kalloc_var       
	sz=0x00000110 off=0x01130270-0x01130380 addr=0xfffffe0008134270-0xfffffe0008134380         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000028 off=0x01130380-0x011303a8 addr=0xfffffe0008134380-0xfffffe00081343a8         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x011303a8-0x011303b0 addr=0xfffffe00081343a8-0xfffffe00081343b0         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 73 at 0x04ade308
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     99320B4E-0BE7-3E2D-B485-3294FE70391C
008: LC_SOURCE_VERSION           128.40.5.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa6958 size=0x168
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleLockdownMode`
- `CFBundleIdentifier`: `com.apple.driver.AppleLockdownMode`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleLockdownMode`
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
- `NSHumanReadableCopyright`: `Copyright © 2022 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleLockdownMode.kext`
- `_PrelinkExecutableLoadAddr`: `-2198900232368`
- `_PrelinkExecutableRelativePath`: `AppleLockdownMode`
- `_PrelinkExecutableSize`: `116545`
- `_PrelinkExecutableSourceAddr`: `-2198900232368`
- `_PrelinkKmodInfo`: `-2198828917976`

## Strings (498) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `LibCall_ACMPing`
- `dataLength == sizeof(ACMCredentialDataBiometryMatchAttempted)`
- `handle && dataType && data && dataSize`
- `responseData && responseDataSize`
- `LibCall_ACMSecSetBiometryAvailability`
- `ACMRequirement - ACMRequirementDataBiometryMatched`
- `[AppleLockdownMode - %s] setting state to off in nvram because state in ACM is also off (not rebooting)\n`
- `policySatisfied`
- `(size - offset) >= sizeof(uint32_t)`
- `aclConstraint`
- `buffer && type`
- `ACMKernControl`
- `dataLength == USER_OUTPUT_SEID_SIZE`
- `count`
- `%s: %s (len=%u): acl:`
- `ACMRequirement - ACMRequirementDataKofNWithAttributes`
- `oblit-inprogress`
- `credential->type == kACMCredentialTypePassphraseEntered`
- `dataOutBuffer && dataInOutLength`
- `%s: %s: returning, err = %ld, var=%u.\n`
- `[AppleLockdownMode - %s] ProtectedData check failed\n`
- `LibCall_ACMContextUnloadToImage`
- `inSize <= kACMContextDataMaxSize`
- `*resultLength >= respDataSize`
- `buffer && unlockSecret && unlockSecretSize && unlockSecretType`
- `site.ACMCredential.ACMCredentialDataUserOutputDisplayed`
- `responseBufferSize >= 2 * sizeof(uint32_t)`
- `op`
- `param->parameterDataLength == sizeof(uint64_t)`
- `constraintSatisfied`
- `(data && dataLength && dataLength <= kACMControlMaxDataLength) || (!data && !dataLength)`
- `params`
- `%s: %s: constraintState = %p.\n`
- `err != kACMErrorBadParameter`
- `(size - offset) >= constraintLength`
- `os_add_overflow(pos, inDataSize, &end) == 0 `
- `[AppleLockdownMode - %s] restoreOS check failed\n`
- `dataLength == sizeof(ACMKextDenyListRevision)`
- `LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx`
- `ACMKernContextDelete`
- `cmd = (acm_command_t *)acm_malloc_data(cmdSize)`
- `dataLength == DATABASE_HASH_SIZE`
- `[AppleLockdownMode - %s] could not get environment variable from ACM: %d\n`
- `dataLength <= sizeof(credData->signature)`
- `outSize`
- `dataLength == sizeof(ACMCredentialDataPassphraseEntered)`
- `size >= sizeof(ACMHandle) + sizeof(ACMContextDataType)`
- `command && commandSize >= sizeof(ACMSEPControlCode)`
- `ACMRequirement - ACMRequirementDataPasscodeValidatedWithAttributes`
- `requirement->dataLength >= sizeof(ACMRequirementDataRatchet)`
- `credential2`
- `credCount <= MAX_CREDENTIAL_LIST_LEN`
- `212`
- `ACMRequirement - ACMRequirementDataPassphraseEntered`
- `site.ACMRequirement.ACMRequirementDataBiometryMatchAttempted`
- `%s: %s: called.\n`
- `responseSize == sizeof(response.body)`
- `operation`
- `site.ACMRequirement.ACMRequirementDataSecureStateWithAttributes`
- `[AppleLockdownMode - %s] ProtectedData check passed\n`
- `/Library/Caches/com.apple.xbs/4776FB82-4876-4747-BD9A-F14E510003B9/TemporaryDirectory.gzqdtN/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c`
- `equal`
- `LibCall_ACMKernDoubleClickNotify`
- `parametersCount <= MAX_PARAMETERS_COUNT`
- `bufferSize`
- `param`
- `param->parameterDataLength && (param->parameterDataLength <= MAX_ACCESS_GROUPS_LEN)`
- `[AppleLockdownMode - %s] setting state to on in nvram because state in ACM is also on (not rebooting)\n`
- `dataLength == 0`
- `31111111111`
- `ACMKernContextVerifyPolicyAndCopyRequirementEx`
- `dataLength == sizeof(uuid_t)`
- `credential->type == kACMCredentialTypeKextDenyListApplePay || credential->type == kACMCredentialTypeKextDenyListFairPlay`
- `responseBuffer`
- `%02x `
- `LibCall_BuildCommand`
- `fallback`
- `nonAutoDisposable requires tracking support`
- `data`
- `LibCall_ACMContextGetInfo`
- `aclLength`
- `size >= sizeof(ACMCredential)`
- `AppleCredentialManager`
- `dataLength == USER_OUTPUT_HASH_SIZE`
- `responseBufferSize >= 3 * sizeof(uint32_t)`
- `ACMCredential - ACMCredentialDataPassphraseExtractable`
- `inSize >= sizeof(acm_command_t)`
- `/Library/Caches/com.apple.xbs/4776FB82-4876-4747-BD9A-F14E510003B9/TemporaryDirectory.gzqdtN/Sources/AppleCredentialManager_KernelLibs/common/LibSerialization.c`
- `outBuffer`
- `LibCall_ACMContextGetData`
- `tmpAcl`
- `%s: %s: returning, err = %ld, code=%u.\n`
- `/arm-io/sep/iop-sep-nub/xART`
- `(size - offset) >= sizeof(ACMHandle)`
- `Util_WriteToBuffer`
- `requirement->dataLength >= sizeof(ACMRequirementDataBiometryMatched)`
- `LibCall_ACMSecCredentialProviderEnrollmentStateChangedForUser`
- `size >= requiredSize`
- `size >= sizeof(ACMUnlockSecretType)`
- `site.ACMRequirement.ACMRequirementDataOr`
- `requirement->type == kACMRequirementTypeAP`
- `site.ACMRequirement.ACMRequirementDataPushButton`
- `%s: %s: operation = %p, operationLength = %zu.\n`
- `param->parameterDataLength == sizeof(int32_t)`
- `credentialList`
- `requirement->type == kACMRequirementTypeSecureIntent`
- `response->resVersion > 0`
- `LibCall_ACMSEPControl`
- `DeserializeVerifyAclConstraint`
- `dataLength == sizeof(ACMCredentialDataPasscodeValidated2)`
- `0123456789abcdef`
- `externalForm`
- `requirementSize <= reqSize`
- `dataLength == sizeof(ACMCredentialDataPassphraseExtractable)`
- `credentialList || (count == 0)`
- `ACMCredential - ACMCredentialDataKextDenyList`
- `ACMRequirement - ACMRequirementDataUserOutputDisplayed`
- `initAppleCredentialService`
- `credential->type == kACMCredentialTypeAP`
- `aclRequiresPasscodeInternal`
- `responseBufferSize >= 3 * sizeof(uint32_t) + authMethodInstLength`
- `size >= sizeof(ACMHandle) + sizeof(ACMCredentialType) + sizeof(ACMCredentialProperty)`
- `ACMCredential - ACMCredentialDataPassphraseEntered`
- `site.ACMCredential.ACMCredentialDataSecureIntent`
- `site.ACMRequirement.ACMRequirementDataPasscodeValidatedWithAttributes`
- `aclConstraintLength`
- `list`
- `constraint`
- `size >= sizeof(ACMHandle) + sizeof(ACMCredentialType) + sizeof(ACMScope)`
- `(size - newOffset) >= params[i].parameterDataLength`
- `_acmService`
- `performCommandV3`
- `(data && dataLength && dataLength <= kACMEnvironmentVariableMaxDataLength) || (!data && !dataLength)`
- `buffer`
- `ACMCredential - ACMCredentialDataAP`
- `ACMKernGlobalContextAddCredential`
- `credential->type == kACMCredentialTypeBiometryMatched`
- `(state && stateSize && stateSize <= kACMTRMMultiState_MaxSize) || (!state && !stateSize)`
- `targetContextExternalForm && targetContextExternalFormLength == sizeof(ACMHandle)`
- `unlockSecret && unlockSecretLength && unlockSecretType`
- `context && outSize && outBuffer`
- `ACMCredential - ACMCredentialDataSignature`
- `site.ACMRequirement.ACMRequirementDataKofN`
- `sourceContextExternalForm && sourceContextExternalFormLength == sizeof(ACMHandle)`
- `param->parameterDataLength <= kACMParameterTypeACLMaxDataLength`
- `AssertMacros: %s (value: 0x%lx), %s, file: %s:%d\n`
- `UTIL_OPTIONAL_BUFFER(outBuffer,outSize)`
- `LibCall_ACMGetEnvironmentVariable`
- `LibCall_ACMSecContextGetUnlockSecret`
- `(parameters && parametersCount) || (!parameters && !parametersCount)`
- `inSize >= sizeof(ACMEnvironmentVariable)`
- `ACMCredential - ACMCredentialDataSecureIntent`
- `start`
- `err == 0 `
- `req->dataLength == sizeof(ACMRequirementDataKofN)`
- `deserializeParameters`
- `site.ACMCredential.ACMCredentialDataSignature`
- `/Library/Caches/com.apple.xbs/4776FB82-4876-4747-BD9A-F14E510003B9/TemporaryDirectory.gzqdtN/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp`
- `requirement->type == kACMRequirementTypeUserOutputDisplayed`
- `accUUIDsSize <= kACMTrustedAccessoriesUUIDsDataMaxSize`
- `%s: %s: acl = %p, aclLength = %zu.\n`
- `param->parameterDataLength == sizeof(uid_t)`
- `site.ACMCredential.ACMCredentialDataBiometryMatched`
- `site.ACMRequirement.ACMRequirementDataAccessGroups`
- `responseBufferSize >= sizeof(Response)`
- `NULL`
- `Util_CreateRequirement`
- `[AppleLockdownMode - %s] MobileObliteration check passed\n`
- `%s: %s: returning.\n`
- `currentStateSize <= 1`
- `buffer && offset && parameters && parametersCount`
- `ACMRequirement - ACMRequirementDataPasscodeValidated`
- `commandSize == sizeof(commandBuffer)`
- `acmService`
- `dataLength == sizeof(ACMHandle)`
- `LibCall_ACMContextCopyData`
- `authMethodInst`
- `LibSer_ACMDeserializeEnvironmentVariableType`
- `site.ACMRequirement.ACMRequirementDataPasscodeValidated`
- `[AppleLockdownMode - %s] restoreOS check passed\n`
- `[AppleLockdownMode - %s] SEP check passed\n`
- `accUUIDsSize % sizeof(uuid_t) == 0`
- `serializeParameters`
- `ACMRequirement - ACMRequirementDataAccessGroups`
- `LibCall_ACMPublishTrustedAccessories`
- `!accUUIDsSize || accUUIDs`
- `(size - offset) >= sizeof(uint8_t)`
- `\n`
- `validateCommand`
- `0`
- `aclConstraint && aclConstraintLength`
- `(enrollmentState && enrollmentStateLength && enrollmentStateLength <= ENROLLMENT_STATE_MAX_SIZE) || (!enrollmentState && !enrollmentStateLength)`
- `cred->numCredSets <= kACMContextPoolTotalCount`
- `Util_SafeDeallocParameters`
- `site.ACMCredential.ACMCredentialDataPassphraseExtractable`
- `handleWithPayload`
- `LibCall_ACMContextContainsCredentialTypeEx`
- `dataLength == sizeof(int32_t)`
- `LibCall_ACMGlobalContextCredentialGetProperty`
- `(inData && inSize) || (!inData && !inSize)`
- `parametersLength + param->parameterDataLength >= parametersLength`
- `ACMCredential - ACMCredentialDataPasscodeValidated`
- `dataLength == sizeof(credData->originator)`
- `response->version >= kCmdCurrentVersion_ContextGetInfo`
- `credentialType`
- `site.ACMCredential`
- `ACMKernGlobalContextVerifyPolicyAndCopyRequirementEx`
- `LDMCheckParity`
- `command`
- `keybagUuid && keybagUuidLength == sizeof(uuid_t)`
- `LibCall_ACMContextCreateWithExternalForm`
- `commandBuffer`
- `catacombUuid && catacombUuidLength == sizeof(uuid_t)`
- `acl && aclLength`
- `operationLength`
- `ACMKernelLib`
- `site.ACMRequirement.ACMRequirementDataRatchet`
- `ACMKernContextGetData`
- `dataLength == sizeof(ACMPassphrasePurpose)`
- `credentialList[i]`
- `ACMKernContextCredentialGetProperty`
- `policyLength <= MAX_POLICY_LENGTH`
- `(size - offset) >= (policyLength + 1)`
- `(size - offset) >= tmpAclLength`
- `dataLength == sizeof(ACMCredentialDataUserOutputDisplayed)`
- `dataLength == sizeof(ACMCredentialDataSecureIntent)`
- `size - offset >= sizeof(ACMScope)`
- `site.ACMCredential.ACMCredentialDataBiometryMatchAttempted`
- `ACMRequirement - ACMRequirementDataPushButtonWithAttributes`
- `IODTNVRAM`
- `AppleLockdownMode`
- `transport`
- `LibCall_ACMSecContextVerifyAclConstraintAndCopyRequirement`
- `ACMCredential - ACMCredentialDataBiometryMatched`
- `maxGlobalCredentialAge`
- `inData && inSize`
- `(size - newOffset) >= sizeof(uint32_t)`
- `LibCall_ACMContexRemoveCredentialsByTypeAndScope`
- `%s: %s: mem: type=%s ptr=%p size=%u (total=%u raw=%u data=%u types=%u) %s:%d (%s).\n`
- `*outSize >= requiredSize`
- `DeallocCredentialList`
- `ACMRequirement - ACMRequirementDataOr`
- `protected-data-access`
- `%s: %s: parameters = %p, parameterCount = %u.\n`
- `requirePasscode`
- `site.ACMRequirement.ACMRequirementDataUserOutputDisplayed`
- `site.ACMRequirement.ACMRequirementDataKeyRef`
- `site.ACMRequirement.ACMRequirementDataBiometryMatchedWithAttributes`
- `context || scope == kACMScopeGlobal`
- `handle && parameters && parametersCount && command && commandSize`
- `sep-endpoint,scrd`
- `ACM`
- `dataLength == sizeof(credData->accPubKey)`
- `%s: %s: command = %u.\n`
- `size >= reqSize`
- `[AppleLockdownMode - %s] enforcing parity check\n`
- `data && dataLength`
- `!context`
- `credential1`
- `DeserializeCredentialList`
- `size >= sizeof(ACMHandle) + sizeof(ACMContextDataType) + sizeof(uint32_t)`
- `offset + *dataSize <= size`
- `ACMKernContextCreateWithExternalForm`
- `site.AppleLockdownMode`
- `-restore`
- `LibCall_ACMContexAddCredentialWithScope`
- `inputBuffer`
- `dataLength == sizeof(uint32_t)`
- `operation && operationLength`
- `AppleSEPManager`
- `performCommand`
- `requirement`
- `_allocatedMem.total >= size`
- `ACMRequirement - ACMRequirementDataPushButton`
- `ACMKernContextGetDataProperty`
- `[AppleLockdownMode - %s] state in ACM: %d, in nvram: %d\n`
- `commandSize`
- `credential->type == kACMCredentialTypePasscodeValidated2`
- `LibSer_ACMDeserializeSEPControlCode`
- `[AppleLockdownMode - %s] MobileObliteration check failed\n`
- `responseSize == sizeof(response)`
- `(size - offset) >= opLength`
- `dataLength == sizeof(ACMCredentialDataAP)`
- `scope`
- `Util_AllocCredential`
- `ACMRequirement`
- `LibCall_ACMSecContextCopyCredentialsArrayEx`
- `handle`
- `ACMCredential - ACMCredentialDataUserOutputDisplayed`
- `os_add_overflow(sizeof(acm_command_t), dataSize, &cmdSize) == 0 `
- `parametersCount`
- `handle || scope == kACMScopeGlobal`
- `length`
- `%s: %s (len=%u): operation:`
- `_allocatedMem.data >= size`
- `ACMCredential - ACMCredentialDataContinuityUnlock`
- `ACMKernContextCreate`
- `LibCall_ACMTRMSaveState`
- `ACMRequirement - ACMRequirementDataKeyRef`
- `ACMKernRequirementDelete`
- `ACMCredential`
- `ACMRequirement - ACMRequirementDataSecureIntent`
- `site.ACMHandleWithPayload`
- `opcode == kCmdPing || opcode == kCmdPingOnDoubleClick`
- `site.ACMCredential.ACMCredentialDataPasscodeValidated`
- `ACMCredential - ACMCredentialDataPasscodeValidated2`
- `transportContext`
- `policyId`
- `context && outSize`
- `dataLength == sizeof(credData->accUUID)`
- `requirement->type == kACMRequirementTypeKeyRef`
- `stateOutBuffer && stateInOutSize`
- `verifyAclConstraintInternal`
- `DeserializeProcessAcl`
- `dataLength == sizeof(ACMCredentialDataKextDenyList)`
- `%s: %s: maxGlobalCredentialAge = %u.\n`
- `[AppleLockdownMode - %s] skipping parity check\n`
- `dataLength == sizeof(ACMKextDenyListFormat)`
- `credential->type == kACMCredentialTypeSecureIntent`
- `heap underflow / memory tracking issue?`
- `size >= sizeof(uint32_t)`
- `subreqCount > 0 && subreqCount <= kACMRequirementSubRequirementMaxCount`
- `dataLength == sizeof(credData->identityUuid)`
- `dataLength == sizeof(uid_t)`
- `dataLength == sizeof(ACMCredentialDataBiometryMatched)`
- `param->parameterDataLength == sizeof(uint32_t)`
- `ACMKernContextAddCredentialWithScope`
- `processAclCommandInternal`
- `[AppleLockdownMode - %s] SEP check failed\n`
- `dataLength`
- `array of ACMParameter`
- `ACMRequirement - ACMRequirementDataKofN`
- `dataLength == sizeof(ACMCredentialDataSignature)`
- `21111111111`
- `requirement->type == kACMRequirementTypePassphraseEntered`
- `remaining >= sizeof(uint32_t)`
- `credential`
- `reqBuffer`
- `transport && context`
- `os_add_overflow(pos, outDataSize, &end) == 0 `
- `<data>`
- `constraintState`
- `site.ACMCredentialRef`
- `unlockSecret && unlockSecretSize > 0`
- `site.ACMParameter`
- `LDMShouldEnforceParity`
- `ACMKernelTransport`
- `!dataSize || data`
- `performCommandFunc`
- `credential->type == kACMCredentialTypeSignature`
- `size >= sizeof(ACMRequirement)`
- `size >= sizeof(ACMHandle) + sizeof(ACMCredential) + sizeof(ACMScope)`
- `inBuffer && readPos`
- `ACMKernGlobalContextRemoveCredentialsByType`
- `ACMKernCredentialDelete`
- `LibCall_ACMContextVerifyPolicyAndCopyRequirementEx`
- `credential->type == kACMCredentialTypeUserOutputDisplayed`
- `requirement->type == kACMRequirementTypeBiometryMatched`
- `os_add_overflow((uintptr_t)outBufferOpt, pos, (uintptr_t *)&writePtr) == 0 `
- `acl`
- `policy`
- `handle && dataType && getSizeOnly`
- `end <= inBufferSize`
- `LibCall_ACMTRMLoadState`
- `credLen <= *outSize`
- `outBuffer && offset`
- `Util_DeallocCredential`
- `222221111111111`
- `reqLen <= *bufferSize`
- `property`
- `Util_AllocRequirement`
- `getLengthOfParameters`
- `/Library/Caches/com.apple.xbs/4776FB82-4876-4747-BD9A-F14E510003B9/TemporaryDirectory.gzqdtN/Sources/AppleCredentialManager_KernelLibs/common/CommonUtil.c`
- `Util_ReadFromBuffer`
- `ACMRequirement - ACMRequirementDataSecureStateWithAttributes`
- `UTIL_OPTIONAL_ARRAY(parameters, parametersCount)`
- `/Library/Caches/com.apple.xbs/4776FB82-4876-4747-BD9A-F14E510003B9/TemporaryDirectory.gzqdtN/Sources/AppleCredentialManager_KernelLibs/common/CommonMem.c`
- `acm_mem_alloc_info`
- `site.ACMCredential.ACMCredentialDataContinuityUnlock`
- `site.ACMCredential.ACMCredentialDataAP`
- `ACMRequirement - ACMRequirementDataBiometryMatchAttempted`
- `%s: %s: returning, err = %ld.\n`
- `requirement->type == kACMRequirementTypeRatchet`
- `LibCall_ACMSecSetBuiltinBiometry`
- `%s: %s: context = %p.\n`
- `writePos`
- `LibCall_ACMContextCredentialGetProperty`
- `LibCall_ACMContextSetData`
- `!outBufferOpt || end <= outBufferSize`
- `site.ACMRequirement.ACMRequirementDataPushButtonWithAttributes`
- `ACMKernCredentialCreate`
- `transport && context && value`
- `!param->parameterDataLength`
- `12111112122212121`
- `ACMHandleWithPayload`
- `context`
- `---`
- `ctxImageOutBuffer && ctxImageInOutSize`
- `req`
- `ACMCredential - ACMCredentialDataBiometryMatchAttempted`
- `LibCall_ACMRequirementDelete`
- `(policyLength <= MAX_POLICY_LENGTH)`
- `paramsCount <= MAX_PARAMETERS_COUNT`
- `dataLength == SCRED_UUID_SIZE`
- `%s: %s: requirePasscode = %p.\n`
- `(size - offset) >= sizeof(ACMContextProperty)`
- `site.ACMRequirement.ACMRequirementDataPassphraseEntered`
- `dataLength == sizeof(credData->confirmationHash)`
- `param.parameterData && param.parameterDataLength == sizeof(uint8_t)`
- `1`
- `os_add_overflow((uintptr_t)inBuffer, pos, (uintptr_t *)&readPtr) == 0 `
- `site.ACMRequirement.ACMRequirementDataSecureIntent`
- `(size - offset) >= opLen`
- `ACMRequirement - ACMRequirementDataBiometryMatchedWithAttributes`
- `dataLength == UUID_LEN`
- `LibCall_ACMGlobalContextVerifyPolicyEx`
- `acm_mem_free_info`
- `consumedBytes`
- `%s: %s: returning, -> ctx = %p.\n`
- `[AppleLockdownMode - %s] failed to start IOService\n`
- `service`
- `(data && dataLength) || (!data && !dataLength)`
- `requirement->type == kACMRequirementTypePushButtonPressed`
- `LibCall_ACMSetEnvironmentVariable`
- `LibCall_ACMContextLoadFromImage`
- `cred`
- `size >= sizeof(ACMHandle) + sizeof(ACMContextDataType) + sizeof(uint8_t)`
- `dataLength <= sizeof(credData->unlockSecret)`
- `dataLength == sizeof(ACMCredentialDataContinuityUnlock)`
- `size >= sizeof(ACMHandle) + sizeof(uint32_t) + sizeof(uint32_t)`
- `site.ACMRequirement.ACMRequirementDataBiometryMatched`
- `param->parameterDataLength == 0`
- `ACMKernPingOnDoubleClick`
- `LibCall_ACMContextCreate`
- `response.body.found`
- `LibCall_ACMContextDelete`
- `(ctxImage && ctxImageSize && ctxImageSize <= kACMContextImageMaxSize)`
- `site.ACMCredential.ACMCredentialDataPasscodeValidated2`
- `site.ACMRequirement.ACMRequirementDataKofNWithAttributes`
- `ACMKernContextRemoveCredentialsByTypeAndScope`
- `dataLength <= kACMPassphraseMaxLength`
- `ACMRequirement - ACMRequirementDataRatchet`
- `(parametersCount == 0 && !parameters) || (parametersCount > 0 && parameters)`
- `DeserializeVerifyPolicy`
- `sigSize > 0 && sigSize <= kACMCredentialDataSignatureMaxSize`
- `requirement->type == kACMRequirementTypeKofN`
- `remaining >= respSize`
- `ACMRequirement - ACMRequirementDataAP`
- `credentialProperty`
- `serviceMatchingDict`
- `*unlockSecretLength >= dataSize`
- `req->dataLength == sizeof(ACMRequirementDataAnd)`
- `LibCall_ACMContextRemoveCredentialsByValueAndScope`
- `handle && parameters && parametersCount`
- `ACMRequirement - ACMRequirementDataAnd`
- `credential->type == kACMCredentialTypePassphraseExtractable`
- `ptr`
- `size >= sizeof(ACMHandle)`
- `param->parameterDataLength == UUID_LEN`
- `ACMKernDoubleClickNotify`
- `reqBufferSize >= sizeof(uint32_t)`
- `LibCall_ACMContextVerifyPolicyEx`
- `(keybagUuid && keybagUuidLength == UUID_LEN) || (!keybagUuid && !keybagUuidLength)`
- `dataLength == sizeof(ACMCredentialDataPasscodeValidated)`
- `params[i].parameterData`
- `Util_DeallocRequirement`
- `/Library/Caches/com.apple.xbs/4776FB82-4876-4747-BD9A-F14E510003B9/TemporaryDirectory.gzqdtN/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp`
- `ACMKernSetEnvironmentVariable`
- `/chosen`
- `22`
- `outDataLength`
- `param->parameterDataLength == sizeof(uint8_t)`
- `(size - newOffset) >= sizeof(ACMParameterType) + sizeof(uint32_t)`
- `site.ACMRequirement.ACMRequirementDataAP`
- `trackingSupported || !nonAutoDisposableRequested`
- `array of ACMCredentialRef`
- `remaining >= cmdSize`
- `ACMKernGetEnvironmentVariable`
- `err == kACMErrorSuccess`
- `site.ACMCredential.ACMCredentialDataPassphraseEntered`
- `[AppleLockdownMode - %s] unable to start LDMCheckParity thread: %d\n`
- `context not found`
- `responseSize == sizeof(uint32_t)`
- `preflight`
- `parameters`
- `size >= credSize`
- `copy`
- `!preflightFound || allowPreflightParameter`
- `outBuffer && outSize`
- `site.ACMCredential.ACMCredentialDataKextDenyList`
- `site.ACMRequirement`
- `LibCall_ACMKernelControl`
- `processAclInternal`
- `cred->domain == kACMDomainUnknown || cred->domain == kACMDomainUserMode || cred->domain == kACMDomainKernelMode || cred->domain == kACMDomainSecureEnclave`
- `site.ACMRequirement.ACMRequirementDataAnd`
- `ACMKernContextSetData`
- `dataType != kACMContextDataTypeUnknown`
- `[AppleLockdownMode - %s] started\n`
