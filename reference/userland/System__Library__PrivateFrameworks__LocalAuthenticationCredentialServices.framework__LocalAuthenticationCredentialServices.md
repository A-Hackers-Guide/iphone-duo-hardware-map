# `/System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/LocalAuthenticationCredentialServices`

iOS 27.2 dyld shared cache image. Version `2319.52.2.0.0`. **[DSC]**

## Linked libraries (13)

- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/usr/lib/swift/libswiftCore.dylib`
- `/usr/lib/swift/libswiftCoreFoundation.dylib`
- `/usr/lib/swift/libswiftDispatch.dylib`
- `/usr/lib/swift/libswiftObjectiveC.dylib`
- `/usr/lib/swift/libswiftXPC.dylib`
- `/usr/lib/swift/libswift_Builtin_float.dylib`
- `/usr/lib/swift/libswiftos.dylib`

## Objective-C: 11 classes, 4 protocols, 117 methods, 25 properties

### Class pages

Every class and protocol, with its methods: [`LACSContext`](../objc/LACSContext_LocalAuthenticationCredentialServices.protocol.md), [`LACSContext`](../objc/LACSContext_LocalAuthenticationCredentialServices.md), [`LACSError`](../objc/LACSError_LocalAuthenticationCredentialServices.md), [`LACSExtractableCredential`](../objc/LACSExtractableCredential_LocalAuthenticationCredentialServices.md), [`LACSExtractablePassword`](../objc/LACSExtractablePassword_LocalAuthenticationCredentialServices.md), [`LACSSecureCredential`](../objc/LACSSecureCredential_LocalAuthenticationCredentialServices.md), [`LACSSecurePassword`](../objc/LACSSecurePassword_LocalAuthenticationCredentialServices.md), [`LACSUnmanagedContext`](../objc/LACSUnmanagedContext_LocalAuthenticationCredentialServices.md), [`LACSUnmanagedExtractablePassword`](../objc/LACSUnmanagedExtractablePassword_LocalAuthenticationCredentialServices.md), [`LACSUnmanagedSecurePassword`](../objc/LACSUnmanagedSecurePassword_LocalAuthenticationCredentialServices.md), [`NSCoding`](../objc/NSCoding_LocalAuthenticationCredentialServices.protocol.md), [`NSObject`](../objc/NSObject_LocalAuthenticationCredentialServices.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_LocalAuthenticationCredentialServices.protocol.md), [`_TtC37LocalAuthenticationCredentialServices12LACSPassword`](../objc/_TtC37LocalAuthenticationCredentialServices12LACSPassword_LocalAuthenticationCredentialServices.md), [`_TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword`](../objc/_TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword_LocalAuthenticationCredentialServices.md)

### Classes

`LACSContext`, `LACSError`, `LACSExtractableCredential`, `LACSExtractablePassword`, `LACSSecureCredential`, `LACSSecurePassword`, `LACSUnmanagedContext`, `LACSUnmanagedExtractablePassword`, `LACSUnmanagedSecurePassword`, `_TtC37LocalAuthenticationCredentialServices12LACSPassword`, `_TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword`

### Protocols

`LACSContext`, `NSCoding`, `NSObject`, `NSSecureCoding`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (class, TB,R) supportsSecureCoding;
@property (T@"LAContext",R,N,V_context) context;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSUUID",N,R) uuid;
@property (T@"LACSExtractablePassword",N,R,Vpassword) password;
@property (T@"_TtC37LocalAuthenticationCredentialServices12LACSPassword",N,R,Vpassword) password;
@property (T@"NSUUID",N,R) uuid;
@property (T@"LACSSecurePassword",N,R,Vpassword) password;
@property (T@"_TtC37LocalAuthenticationCredentialServices12LACSPassword",N,R,Vpassword) password;
@property (T@"NSData",R,N) contextRef;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"_TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword",N,R,Vpassword) password;
@property (T@"_TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword",N,R,Vpassword) password;
@property (T@"<LACSContext>",N,R,Vcontext) context;
@property (T@"<LACSContext>",N,R,Vcontext) context;
```

## Swift types (3)

`LocalAuthenticationCredentialServices.LACSLog`, `LocalAuthenticationCredentialServices.LACSPassword:`, `LocalAuthenticationCredentialServices.LACSUnmanagedPassword:`

## Strings (273)

```
LibCall_ACMContextGetData
init()
LibCall_ACMContextCreateWithExternalForm
LibCall_ACMContextVerifyPolicyAndCopyRequirementEx
LibCall_ACMContextCredentialGetProperty
Util_WriteToBuffer
DeserializeCredentialList
crypto_encryptText
Util_ReadFromBuffer
NO
CredentialServices.Context
com.apple.LocalAuthenticationCredentialServices
ACMContextAddCredentialWithScope
ACMCredentialGetProperty
ACMSetEnvironmentVariableWithAccessPolicy
LibCall_ACMGlobalContextCredentialGetProperty
LocalAuthenticationCredentialServices.LACSUnmanagedSecurePassword
getRequirementDataSizeForVersion
requirement
%s
ACMContextSetData
LibCall_ACMContextGetInfo
Failed to get encryption seed, status: %d
ACMContextGetExternalForm
LibCall_ACMSecSetBuiltinBiometry
%s: %s: operation = %p, operationLength = %zu.\n
false
ACMRequirement - ACMRequirementDataOr
acm_transport
%s: %s: parameters = %p, parameterCount = %u.\n
%s: %s: returning, err = %ld.\n
%s: %s (len=%u): operation:
ccgcm_init
LibCall_ACMTRMLoadState_Block
ACMGlobalContextCredentialGetProperty
LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx
%s: %s: called.\n
Util_AllocCredential
Util_AllocRequirement
ACMContextAddCredential
ACMContextCopyData
LibCall_ACMContexRemoveCredentialsByTypeAndScope
%s: %s: constraintState = %p.\n
ccgcm_update
commandCursor == commandBuffer + sizeof(commandBuffer)
LibCall_ACMSecContextCopyCredentialsArrayEx
LibCall_ACMTRMSaveState
cchkdf
LibCall_ACMContextLoadFromImage
LibCall_ACMSecSetBiometryAvailability
ACMContextCreateWithFlags
LibCall_ACMContextContainsCredentialTypeEx
LibCall_ACMSecContextGetUnlockSecret
%s: %s: acl = %p, aclLength = %zu.\n
LibSer_ACMDeserializeSEPControlCode
%s: %s: CoreCrypto - %s() succeeded, ccErr: %d.\n
crypto_encryptText_version1
ACMRequirement - ACMRequirementDataPasscodeValidatedWithAttributes
ACM
LibCall_ACMPing
ccgcm_finalize
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c
ACMParseAclAndCopyConstraintCharacteristics
ACMKernelControl
LibCall_ACMRequirementDelete
deserializeParameters
ACMContextReplacePassphraseCredentialsWithScope
ACMContextGetData
CredentialServices.Password
ACMRequirement - ACMRequirementDataUserOutputDisplayed
ACMContextVerifyPolicy
LibCall_ACMContextCopyData
ACMRequirement - ACMRequirementDataSecureIntent
ACMGetEnvironmentVariableData
Failed to obtain encryption size, status: %d
crypto_encryptText_version2
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c
ACMRequirement
ACMRequirement - ACMRequirementDataPushButton
ACMSetEnvironmentVariable
LibCall.c
array of ACMCredentialRef
ACMCredential - ACMCredentialDataAP
ACMRequirementGetProperties
init
LibCall_ACMSecContextVerifyAclConstraintAndCopyRequirement
v24@?0r^v8Q16
LibCall_ACMSEPControl_Block
ACMCredential - ACMCredentialDataBiometryMatched
ACMLib
ACMContextCreateWithExternalForm
ccgcm_set_iv
@8@?0
generateRandom
ACMContextDelete
%s: %s (len=%u): acl:
checkCCError
ACMCredential - ACMCredentialDataSignature
ACMCredential
ACMRequirement - ACMRequirementDataKofN
performCommand
ACMCredential - ACMCredentialDataKextDenyList
ACMRequirement - ACMRequirementDataBiometryMatchedWithAttributes
ACMRequirement - ACMRequirementDataPushButtonWithAttributes
LibCall_ACMGlobalContextVerifyPolicyEx
B24@?0^{__ACMHandle=}8^@16
acm_mem_alloc_info
ACMRequirement - ACMRequirementDataAccessGroups
Failed to get data from ACM context, status: %d
crypto_deriveKeyAndEncryptData
crypto_decryptText_version2
ACMRequirement - ACMRequirementDataSecureStateWithAttributes
ACMContextGetInfo
updateLogLevelFromKext
LibCall_ACMKernDoubleClickNotify
ACMCredential - ACMCredentialDataPasscodeValidated2
ACMRequirement - ACMRequirementDataKofNWithAttributes
ACMGlobalContextRemoveCredentialsByType
ACMContextRemoveCredentialsByValueAndScope
ACMContextContainsPassphraseCredentialWithPurpose
ACMGlobalContextVerifyPolicy
LibCall_ACMSEPControl
Failed to allocate decryption buffer
LibCall_ACMContextVerifyPolicyWithPreflight_Block
LibCall_ACMContextVerifyPolicyEx_Block
ACMRequirement - ACMRequirementDataBiometryMatched
LibCall_ACMContexAddCredentialWithScope
ACMCredential - ACMCredentialDataContinuityUnlock
LocalAuthenticationCredentialServices.LACSExtractableCredential
crypto_generateRandomSaltLazily
%s: %s: CoreCrypto - %s() failed, ccErr: %d.\n
dst || !dstCapacity
ACMRequirement - ACMRequirementDataPassphraseEntered
Util_DeallocRequirement
LibCall_ACMContextCreate
com.apple.LocalAuthentication
Util_CreateRequirement
Unable to find class %s
crypto_generateKeyFromSharedInfo
LibCall_ACMGlobalContextCredentialGetProperty_Block
%s: %s: mem: type=%s ptr=%p size=%u (total=%u raw=%u data=%u types=%u) %s:%d (%s).\n
getLengthOfParameters
ACMContextRemoveCredentialsByValue
ACMContextRemoveCredentialsByTypeAndScope
processAclCommandInternal
Failed to create ACM context, status: %d
crypto_decryptText_version1
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c
Failed to decrypt data, status: %d
serializeParameters
0123456789abcdef
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c
ACMCredential - ACMCredentialDataBiometryMatchAttempted
ACMCredential - ACMCredentialDataPasscodeValidated
Failed to encrypt data, status: %d
DeserializeProcessAcl
ACMContextGetDataProperty
LibCall_ACMContextDelete
%s: %s: command = %u.\n
<data>
crypto_decryptText
ACMContextVerifyPolicyWithPreflight
ACMRequirementGetProperty
LibCall_ACMContextRemoveCredentialsByValueAndScope
%s: %s: context = %p.\n
LocalAuthenticationCredentialServices.LACSExtractablePassword
LibCall_ACMGetEnvironmentVariable_Block
LibCall_ACMPublishTrustedAccessories
LocalAuthenticationCredentialServices.LACSPassword
LibSerialization.c
ACMRequirement - ACMRequirementDataBiometryMatchAttempted
ACMRequirement - ACMRequirementDataKeyRef
YES
crypto_generateKeyFromSharedInfo_version1
cc_cmp_safe
LibCall_ACMContextUnloadToImage_Block
DeserializeVerifyAclConstraint
ACMGetEnvironmentVariable
LocalAuthenticationCredentialServices.LACSUnmanagedExtractablePassword
crypto_generateKey
LibCall_BuildCommand
Failed to obtain plain data size, status: %d
src || !srcLen
ACMContextContainsCredentialType
aclRequiresPasscodeInternal
DeserializeVerifyPolicy
ACMGlobalContextAddCredential
%02x 
%s: %s: maxGlobalCredentialAge = %u.\n
v24@?0@\"NSData\"8@\"NSError\"16
array of ACMParameter
LibCall_ACMGlobalContextVerifyPolicy_Block
Util_hexDumpToStrHelper
ACMContextVerifyPolicyEx
LibCall_ACMSetEnvironmentVariable
LibCall_ACMSecCredentialProviderEnrollmentStateChangedForUser
acm_mem_free_info
ioKitTransport
v8@?0
LocalAuthenticationCredentialServices.LACSSecurePassword
NULL
Util_SafeDeallocParameters
ACMContextGetDataEx
LibCall_ACMContextUnloadToImage
LibCall_ACMContextSetData
Failed to create ACM context
CredentialServices.Default
DeallocCredentialList
LibCall_ACMGetEnvironmentVariable
LibCall_ACMKernelControl_Block
Util_DeallocCredential
ACMRequirement - ACMRequirementDataPasscodeValidated
ACMRequirementGetSubrequirements
LibSer_ACMDeserializeEnvironmentVariableType
crypto_generateKeyFromSharedInfo_version2
ACMHandleWithPayload
LocalAuthenticationCredentialServices.LACSUnmanagedPassword
ccrng
verifyAclConstraintForOperationCommandInternal
ACMContextSetDataEx
LibCall_ACMContextVerifyPolicyEx
LibCall_ACMTRMLoadState
Failed to store data in ACM context, status: %d
LocalAuthenticationCredentialServices.LACSSecureCredential
crypto_deriveKeyAndDecryptData
platform_rng
%s: %s: returning.\n
ACMRequirement - ACMRequirementDataAnd
AppleCredentialManager
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c
ACMCredential - ACMCredentialDataPassphraseExtractable
ACMContextContainsCredentialTypeEx
ACMContextCredentialGetPropertyEx
LAContext
ACMContextRemoveCredentialsByType
LibCall_ACMKernelControl
verifyAclConstraintInternal
ACMCredential - ACMCredentialDataPassphraseEntered
ACMContextRemovePassphraseCredentialsByPurposeAndScope
LibCall_ACMGetAclAuthMethod_Block
ACMCredential - ACMCredentialDataUserOutputDisplayed
ACMCredential - ACMCredentialDataSecureIntent
ACMGetAclAuthMethod
CommonUtil.c
ACMRequirement - ACMRequirementDataRatchet
%s: %s: requirePasscode = %p.\n
ACMRequirement - ACMRequirementDataAP
processAclInternal
Failed to extract data %{public}@
Failed to create LACSUnmanagedExtractablePassword: %{public}@
%s: %s: called.\n
%s: %s: CS[%u] created (flags=0x%x).\n
%s: %s: cmd(%u) on CS[%u] -> ok.\n
Failed to create ACM context from context ref
Credential storage failed (err:%@)
Failed to create LACSSecurePassword: %{public}@
%s: %s: CS[%u] acquired.\n
%s: %s: returning, -> ctx = %p.\n
%s: %s: returning, err = %ld, var=%u.\n
%s: %s: log level set to %d.\n
%@
%{public}@
Failed to create LACSExtractablePassword: %{public}@
Failed to create LACSUnmanagedSecurePassword: %{public}@
Failed to create LACSUnmanagedExtractablePassword with contextRef: %{public}@
%s: %s: returning, err = %ld.\n
%s: %s: returning.\n
%s: %s: returning, err = %ld, code=%u.\n
Failed to create LACSUnmanagedSecurePassword with contextRef: %{public}@
%s: %s: CS[%u] deleted (contextDestroyed=%s).\n
%s: %s: cmd(%u) on CS[%u] -> err 0x%x (%d).\n
Credential extraction failed (err:%@)
softlink:r:path:/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
```
