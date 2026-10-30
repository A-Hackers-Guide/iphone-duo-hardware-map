# `/System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/LocalAuthenticationCredentialServices`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 291,152 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 31 (Size: 4824)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe, NlistOutofsyncWithDyldinfo
```

## Linked libraries (14)

- `/System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/LocalAuthenticationCredentialServices (compatibility version 1.0.0, current version 2319.52.2)`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking (compatibility version 1.0.0, current version 72.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0, weak)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0, weak)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2, weak)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (11 classes, 4 protocols)

Classes: `LACSContext`, `LACSError`, `LACSExtractableCredential`, `LACSExtractablePassword`, `LACSSecureCredential`, `LACSSecurePassword`, `LACSUnmanagedContext`, `LACSUnmanagedExtractablePassword`, `LACSUnmanagedSecurePassword`, `_TtC37LocalAuthenticationCredentialServices12LACSPassword`, `_TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword`

Protocols: `LACSContext`, `NSCoding`, `NSObject`, `NSSecureCoding`

## Strings (418)

```
LocalAuthenticationCredentialServices.LACSExtractableCredential
crypto_encryptText_version2
Util_WriteToBuffer
LAContext
com.apple.LocalAuthenticationCredentialServices
ACMCredential - ACMCredentialDataPassphraseEntered
ACMCredential - ACMCredentialDataKextDenyList
ACMContextCreateWithExternalForm
ACMContextRemoveCredentialsByTypeAndScope
LibSer_ACMDeserializeSEPControlCode
crypto_encryptText_version1
AppleCredentialManager
array of ACMCredentialRef
LibCall_ACMTRMSaveState
LocalAuthenticationCredentialServices.LACSPassword
%s: %s (len=%u): acl:
acm_mem_free_info
ACMCredential - ACMCredentialDataBiometryMatchAttempted
ACMGetEnvironmentVariable
ACMContextGetDataEx
v24@?0@\"NSData\"8@\"NSError\"16
%s: %s: mem: type=%s ptr=%p size=%u (total=%u raw=%u data=%u types=%u) %s:%d (%s).\n
crypto_decryptText_version2
ACMCredential
ACMContextCreateWithFlags
ACMContextContainsCredentialType
commandCursor == commandBuffer + sizeof(commandBuffer)
LibCall_ACMContextLoadFromImage
crypto_deriveKeyAndDecryptData
checkCCError
crypto_decryptText_version1
ACMSetEnvironmentVariableWithAccessPolicy
Failed to store data in ACM context, status: %d
Failed to decrypt data, status: %d
DeserializeCredentialList
ACMLib
%s: %s: called.\n
Util_ReadFromBuffer
ACMRequirement - ACMRequirementDataPushButtonWithAttributes
LibCall_ACMGetEnvironmentVariable
%s: %s (len=%u): operation:
Failed to create ACM context, status: %d
crypto_decryptText
ACMParseAclAndCopyConstraintCharacteristics
ACMContextCopyData
LibCall_ACMContextSetData
LocalAuthenticationCredentialServices.LACSSecureCredential
LibSerialization.c
crypto_generateKeyFromSharedInfo_version1
LibCall_ACMSEPControl_Block
v24@?0r^v8Q16
getLengthOfParameters
crypto_encryptText
ccgcm_init
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c
B24@?0^{__ACMHandle=}8^@16
ACMRequirement - ACMRequirementDataPushButton
ACMRequirement - ACMRequirementDataBiometryMatchedWithAttributes
DeallocCredentialList
false
ACMRequirement - ACMRequirementDataKofNWithAttributes
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c
ACMContextVerifyPolicyWithPreflight
ACMRequirementGetProperty
processAclCommandInternal
LocalAuthenticationCredentialServices.LACSUnmanagedExtractablePassword
ACMCredential - ACMCredentialDataUserOutputDisplayed
ACMGlobalContextVerifyPolicy
LibCall_ACMSecSetBuiltinBiometry
Unable to find class %s
LibCall_ACMSEPControl
requirement
crypto_generateKey
ACMCredential - ACMCredentialDataPassphraseExtractable
Util_DeallocRequirement
init
@8@?0
crypto_generateKeyFromSharedInfo_version2
LibCall_ACMSecSetBiometryAvailability
LocalAuthenticationCredentialServices.LACSUnmanagedSecurePassword
platform_rng
ioKitTransport
LibCall_ACMContextUnloadToImage
%s: %s: acl = %p, aclLength = %zu.\n
ACMGetAclAuthMethod
ccrng
LibCall_ACMGlobalContextCredentialGetProperty_Block
ACMRequirement - ACMRequirementDataKeyRef
LibCall_ACMKernelControl
verifyAclConstraintInternal
init()
acm_mem_alloc_info
ccgcm_update
ACMRequirement - ACMRequirementDataBiometryMatchAttempted
ACMGlobalContextAddCredential
LibCall_ACMContextCreateWithExternalForm
LibCall_ACMSecCredentialProviderEnrollmentStateChangedForUser
LibCall_ACMSecContextCopyCredentialsArrayEx
<data>
Util_hexDumpToStrHelper
ACMContextReplacePassphraseCredentialsWithScope
ACMSetEnvironmentVariable
%s: %s: context = %p.\n
DeserializeProcessAcl
LibSer_ACMDeserializeEnvironmentVariableType
ACMRequirement - ACMRequirementDataPasscodeValidatedWithAttributes
ACMContextContainsPassphraseCredentialWithPurpose
ccgcm_finalize
NO
%s: %s: parameters = %p, parameterCount = %u.\n
serializeParameters
ACMRequirement - ACMRequirementDataUserOutputDisplayed
ACMContextRemoveCredentialsByType
LibCall_ACMContextCredentialGetProperty
verifyAclConstraintForOperationCommandInternal
ACMCredential - ACMCredentialDataPasscodeValidated2
array of ACMParameter
0123456789abcdef
ACMCredentialGetProperty
ACMContextSetDataEx
LibCall_ACMContexAddCredentialWithScope
LibCall_ACMPublishTrustedAccessories
ACMRequirement - ACMRequirementDataOr
Util_CreateRequirement
ACMContextDelete
LibCall_ACMPing
Failed to get data from ACM context, status: %d
%s: %s: returning, err = %ld.\n
%s: %s: CoreCrypto - %s() succeeded, ccErr: %d.\n
LibCall_ACMContextVerifyPolicyEx_Block
LibCall_ACMKernDoubleClickNotify
LocalAuthenticationCredentialServices.LACSSecurePassword
ACMCredential - ACMCredentialDataSecureIntent
ACMGlobalContextRemoveCredentialsByType
LibCall_ACMContextCreate
com.apple.LocalAuthentication
crypto_generateKeyFromSharedInfo
ACMRequirement - ACMRequirementDataSecureIntent
%s: %s: returning.\n
dst || !dstCapacity
LibCall_ACMContextDelete
LibCall_ACMContextRemoveCredentialsByValueAndScope
LibCall_ACMContextGetData
Failed to obtain encryption size, status: %d
Failed to allocate decryption buffer
CredentialServices.Default
LibCall_ACMGlobalContextVerifyPolicy_Block
Util_SafeDeallocParameters
ACMCredential - ACMCredentialDataAP
ACMContextVerifyPolicy
v8@?0
ACMCredential - ACMCredentialDataSignature
ACMRequirement - ACMRequirementDataAnd
YES
ACMHandleWithPayload
LibCall_ACMContextGetInfo
%s: %s: maxGlobalCredentialAge = %u.\n
%s: %s: requirePasscode = %p.\n
DeserializeVerifyPolicy
DeserializeVerifyAclConstraint
LibCall_ACMKernelControl_Block
ACMRequirement - ACMRequirementDataAP
ACMContextVerifyPolicyEx
LibCall_ACMSetEnvironmentVariable
LibCall_ACMTRMLoadState
Failed to get encryption seed, status: %d
CredentialServices.Context
ccgcm_set_iv
LibCall_ACMGlobalContextVerifyPolicyEx
aclRequiresPasscodeInternal
Util_AllocCredential
ACMContextGetData
%s: %s: operation = %p, operationLength = %zu.\n
Failed to create ACM context
generateRandom
LibCall_ACMTRMLoadState_Block
ACMRequirementGetProperties
LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx
%s: %s: command = %u.\n
cc_cmp_safe
Util_DeallocCredential
ACMRequirementGetSubrequirements
updateLogLevelFromKext
CredentialServices.Password
Util_AllocRequirement
ACMContextAddCredential
ACMContextCredentialGetPropertyEx
LibCall_ACMContexRemoveCredentialsByTypeAndScope
LibCall_ACMContextVerifyPolicyWithPreflight_Block
LibCall_ACMContextVerifyPolicyEx
crypto_deriveKeyAndEncryptData
LibCall_ACMGetEnvironmentVariable_Block
ACMContextRemovePassphraseCredentialsByPurposeAndScope
ACMKernelControl
LibCall_ACMContextCopyData
ACMRequirement - ACMRequirementDataKofN
%s
NULL
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c
CommonUtil.c
ACMRequirement
ACMRequirement - ACMRequirementDataBiometryMatched
LibCall_ACMContextContainsCredentialTypeEx
LibCall_ACMContextVerifyPolicyAndCopyRequirementEx
ACMCredential - ACMCredentialDataContinuityUnlock
performCommand
LibCall_ACMSecContextVerifyAclConstraintAndCopyRequirement
ACM
ACMGetEnvironmentVariableData
ACMGlobalContextCredentialGetProperty
ACMContextSetData
getRequirementDataSizeForVersion
cchkdf
ACMContextContainsCredentialTypeEx
ACMContextGetDataProperty
LibCall_ACMSecContextGetUnlockSecret
Failed to obtain plain data size, status: %d
LibCall_ACMContextUnloadToImage_Block
src || !srcLen
acm_transport
LibCall_BuildCommand
LibCall_ACMGlobalContextCredentialGetProperty
Failed to encrypt data, status: %d
LibCall_ACMRequirementDelete
LocalAuthenticationCredentialServices.LACSUnmanagedPassword
ACMRequirement - ACMRequirementDataPasscodeValidated
ACMContextGetInfo
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c
%02x 
processAclInternal
%s: %s: CoreCrypto - %s() failed, ccErr: %d.\n
ACMCredential - ACMCredentialDataPasscodeValidated
ACMRequirement - ACMRequirementDataPassphraseEntered
ACMRequirement - ACMRequirementDataRatchet
ACMRequirement - ACMRequirementDataSecureStateWithAttributes
ACMContextRemoveCredentialsByValue
%s: %s: constraintState = %p.\n
LibCall.c
deserializeParameters
crypto_generateRandomSaltLazily
ACMRequirement - ACMRequirementDataAccessGroups
LibCall_ACMGetAclAuthMethod_Block
ACMContextAddCredentialWithScope
ACMContextGetExternalForm
ACMContextRemoveCredentialsByValueAndScope
LocalAuthenticationCredentialServices.LACSExtractablePassword
ACMCredential - ACMCredentialDataBiometryMatched
%s: %s: returning.\n
%s: %s: returning, err = %ld, code=%u.\n
Credential extraction failed (err:%@)
Credential storage failed (err:%@)
Failed to create LACSExtractablePassword: %{public}@
%s: %s: CS[%u] deleted (contextDestroyed=%s).\n
%s: %s: cmd(%u) on CS[%u] -> ok.\n
%{public}@
Failed to extract data %{public}@
Failed to create LACSUnmanagedSecurePassword with contextRef: %{public}@
Failed to create LACSUnmanagedExtractablePassword: %{public}@
%s: %s: CS[%u] acquired.\n
%s: %s: returning, err = %ld, var=%u.\n
%s: %s: log level set to %d.\n
%s: %s: cmd(%u) on CS[%u] -> err 0x%x (%d).\n
Failed to create ACM context from context ref
Failed to create LACSUnmanagedExtractablePassword with contextRef: %{public}@
%s: %s: returning, err = %ld.\n
%s: %s: CS[%u] created (flags=0x%x).\n
%@
Failed to create LACSUnmanagedSecurePassword: %{public}@
Failed to create LACSSecurePassword: %{public}@
%s: %s: called.\n
%s: %s: returning, -> ctx = %p.\n
softlink:r:path:/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
LACSUnmanagedContext
LACSContext
LACSExtractablePassword
NSSecureCoding
LACSUnmanagedSecurePassword
NSObject
LACSSecureCredential
LACSError
_TtC37LocalAuthenticationCredentialServices12LACSPassword
LACSUnmanagedExtractablePassword
_TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword
LACSExtractableCredential
NSCoding
LACSSecurePassword
dictionaryWithObjects:forKeys:count:
init:
context
T@\"LACSExtractablePassword\",N,R,Vpassword
withContextRef:
TQ,R
dataWithBytes:length:
initWithContextRef:error:
encodeObject:forKey:
externalize
hash
initWithContextRef:
isEqual:
password
performSelector:
respondsToSelector:
isProxy
T@\"NSString\",R,C
contextRef
secureCopy
setCredential:type:error:
storeCredentialData:securely:error:
stringWithFormat:
superclass
T@\"NSData\",R,N
T@\"_TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword\",N,R,Vpassword
_externalizedContextRef
data
retain
retainCount
uuid
uuidBytes
dataWithLength:
data:
errorWithDomain:code:userInfo:
externalizedContext
init
initWithACMContextRef:ownsContextRef:
isKindOfClass:
mutableBytes
T@\"LAContext\",R,N,V_context
_ownsContextRef
T@\"<LACSContext>\",N,R,Vcontext
_encryptData:seed:externalizedContext:error:
initWithData:contextRef:error:
self
unsafeContextRef
dealloc
T@\"NSString\",?,R,C
credentialOfType:reply:
supportsSecureCoding
errorWithCode:debugDescription:
_contextRef
_decryptData:seed:externalizedContext:error:
T#,R
_withContext:error:
performSelector:withObject:withObject:
autorelease
conformsToProtocol:
initWithBytes:length:
initWithCoder:
secureCopy:
T@\"LACSSecurePassword\",N,R,Vpassword
.cxx_destruct
fetchCredentialData:
TB,N,R
_context
initWithData:error:
zone
release
T@\"NSUUID\",N,R
errorWithCode:
initWithContext:
initWithPassword:
performSelector:withObject:
T@\"_TtC37LocalAuthenticationCredentialServices12LACSPassword\",N,R,Vpassword
description
length
TB,R
_encryptionSeedForContext:error:
bytes
debugDescription
isMemberOfClass:
_errorWithCode:userInfo:
_newZeroingDataWithBytesNoCopy:length:deallocator:
class
encodeWithCoder:
initWithExternalizedContext:userSession:
initWithUUID:password:error:
@32@0:8@16^@24
B
B16@0:8
B24@0:8#16
B36@0:8@\"NSData\"16B24^@28
@32@0:8^{__ACMHandle=}16^@24
@48@0:8@16@24@32^@40
^{__ACMHandle=}
@24@0:8^@16
B24@0:8@\"Protocol\"16
@32@0:8q16@24
v24@0:8@\"NSCoder\"16
Q16@0:8
^{_NSZone=}16@0:8
@24@0:8q16
v24@0:8@?16
@\"LACSExtractablePassword\"
@24@0:8@\"NSCoder\"16
B24@0:8@16
@\"NSData\"
@16@0:8
v24@0:8@16
@\"<LACSContext>\"
Vv16@0:8
@\"NSString\"16@0:8
@\"LACSSecurePassword\"
@32@0:8:16@24
B36@0:8@16B24^@28
B32@0:8@?16^@24
@24@0:8@16
@24@0:8:16
@40@0:8:16@24@32
@\"NSData\"24@0:8^@16
@\"NSData\"16@0:8
@28@0:8^{__ACMHandle=}16B24
@\"LAContext\"
@\"_TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword\"
v16@0:8
#16@0:8
B24@0:8:16
@\"_TtC37LocalAuthenticationCredentialServices12LACSPassword\"
@40@0:8@16@24^@32
```
