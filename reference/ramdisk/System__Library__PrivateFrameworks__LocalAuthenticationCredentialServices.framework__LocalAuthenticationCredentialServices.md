# `/System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/LocalAuthenticationCredentialServices`

From the upgrade restore ramdisk (141-29011-104.dmg). 291,152 bytes.

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
CredentialServices.Password
crypto_decryptText_version2
YES
%s: %s: parameters = %p, parameterCount = %u.\n
Failed to encrypt data, status: %d
LocalAuthenticationCredentialServices.LACSUnmanagedExtractablePassword
ccgcm_finalize
cc_cmp_safe
src || !srcLen
ACMContextContainsCredentialType
LibCall_ACMTRMLoadState
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c
acm_transport
updateLogLevelFromKext
Failed to store data in ACM context, status: %d
getLengthOfParameters
Util_hexDumpToStrHelper
LibCall_ACMGetEnvironmentVariable
LibCall_ACMTRMLoadState_Block
Util_AllocCredential
ACMContextCreateWithFlags
B24@?0^{__ACMHandle=}8^@16
crypto_generateKey
ACMKernelControl
ACMContextCredentialGetPropertyEx
LibCall_ACMPublishTrustedAccessories
ACMCredential - ACMCredentialDataSignature
ACMContextContainsCredentialTypeEx
ACMContextGetInfo
LibCall_ACMSecContextVerifyAclConstraintAndCopyRequirement
LocalAuthenticationCredentialServices.LACSUnmanagedSecurePassword
verifyAclConstraintForOperationCommandInternal
NO
ACMContextGetExternalForm
init()
ACMRequirement - ACMRequirementDataSecureIntent
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c
LibCall_ACMGlobalContextVerifyPolicyEx
LibCall_ACMContextGetData
Failed to get encryption seed, status: %d
LibSer_ACMDeserializeEnvironmentVariableType
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c
ACMCredential - ACMCredentialDataPassphraseExtractable
ACMRequirement - ACMRequirementDataAccessGroups
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c
LocalAuthenticationCredentialServices.LACSPassword
false
crypto_decryptText
ACMContextGetData
init
processAclCommandInternal
%s: %s: requirePasscode = %p.\n
v8@?0
com.apple.LocalAuthenticationCredentialServices
%s: %s: CoreCrypto - %s() failed, ccErr: %d.\n
LibCall_ACMContextDelete
com.apple.LocalAuthentication
crypto_deriveKeyAndDecryptData
ACMRequirement - ACMRequirementDataPassphraseEntered
ACMSetEnvironmentVariableWithAccessPolicy
ACMGetEnvironmentVariableData
LibCall_ACMContexAddCredentialWithScope
commandCursor == commandBuffer + sizeof(commandBuffer)
LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx
%s: %s: returning, err = %ld.\n
getRequirementDataSizeForVersion
acm_mem_alloc_info
DeserializeProcessAcl
crypto_generateKeyFromSharedInfo
ACMCredentialGetProperty
ACMContextSetDataEx
v24@?0r^v8Q16
NULL
ccgcm_init
ACMContextAddCredential
LibCall_ACMKernDoubleClickNotify
crypto_deriveKeyAndEncryptData
ACMContextVerifyPolicyWithPreflight
ACMHandleWithPayload
LibCall_ACMContextVerifyPolicyEx
requirement
CommonUtil.c
ACMRequirement - ACMRequirementDataUserOutputDisplayed
ACMRequirement - ACMRequirementDataSecureStateWithAttributes
LibCall.c
LocalAuthenticationCredentialServices.LACSSecureCredential
LibCall_ACMContextUnloadToImage_Block
ACMGlobalContextVerifyPolicy
LibCall_ACMPing
LibCall_ACMSecSetBiometryAvailability
%s: %s: called.\n
LibCall_ACMGlobalContextVerifyPolicy_Block
0123456789abcdef
ACMRequirement - ACMRequirementDataKeyRef
Unable to find class %s
deserializeParameters
crypto_decryptText_version1
DeallocCredentialList
LocalAuthenticationCredentialServices.LACSUnmanagedPassword
ACM
LibCall_ACMKernelControl
LibCall_ACMContextLoadFromImage
LibCall_ACMContextUnloadToImage
%s: %s: returning.\n
Util_AllocRequirement
ACMContextRemoveCredentialsByType
LibCall_ACMContextCreateWithExternalForm
%s: %s: maxGlobalCredentialAge = %u.\n
ACMRequirement - ACMRequirementDataKofN
LibCall_ACMContextCreate
processAclInternal
%s: %s: mem: type=%s ptr=%p size=%u (total=%u raw=%u data=%u types=%u) %s:%d (%s).\n
LibCall_ACMKernelControl_Block
LibCall_ACMSEPControl
LibCall_ACMSecContextGetUnlockSecret
crypto_generateRandomSaltLazily
ccgcm_set_iv
ACMCredential - ACMCredentialDataKextDenyList
ACMContextGetDataEx
LibCall_ACMGlobalContextCredentialGetProperty
%s: %s (len=%u): acl:
Failed to get data from ACM context, status: %d
CredentialServices.Default
array of ACMCredentialRef
ACMContextCreateWithExternalForm
LibCall_ACMContexRemoveCredentialsByTypeAndScope
LocalAuthenticationCredentialServices.LACSSecurePassword
ACMContextReplacePassphraseCredentialsWithScope
ACMContextGetDataProperty
%s: %s: command = %u.\n
DeserializeVerifyPolicy
ACMCredential - ACMCredentialDataAP
ACMRequirement - ACMRequirementDataKofNWithAttributes
ACMRequirementGetProperties
ioKitTransport
LibCall_ACMContextVerifyPolicyAndCopyRequirementEx
LibCall_ACMSetEnvironmentVariable
%s: %s: acl = %p, aclLength = %zu.\n
Failed to allocate decryption buffer
LibCall_ACMContextGetInfo
%s: %s: operation = %p, operationLength = %zu.\n
Failed to create ACM context
LAContext
platform_rng
crypto_encryptText_version2
ACMCredential - ACMCredentialDataPassphraseEntered
ACMCredential - ACMCredentialDataUserOutputDisplayed
LibCall_BuildCommand
ACMCredential - ACMCredentialDataSecureIntent
ACMContextRemoveCredentialsByValue
verifyAclConstraintInternal
LibCall_ACMSecCredentialProviderEnrollmentStateChangedForUser
LibSer_ACMDeserializeSEPControlCode
LocalAuthenticationCredentialServices.LACSExtractablePassword
LibCall_ACMContextVerifyPolicyWithPreflight_Block
ACMCredential - ACMCredentialDataBiometryMatched
ACMRequirement - ACMRequirementDataBiometryMatchAttempted
Util_CreateRequirement
ACMContextRemoveCredentialsByTypeAndScope
LibCall_ACMSecSetBuiltinBiometry
LibCall_ACMContextSetData
Util_WriteToBuffer
Util_ReadFromBuffer
aclRequiresPasscodeInternal
acm_mem_free_info
ACMContextRemoveCredentialsByValueAndScope
AppleCredentialManager
LibCall_ACMContextCopyData
%s: %s: CoreCrypto - %s() succeeded, ccErr: %d.\n
LibCall_ACMSEPControl_Block
ACMRequirement - ACMRequirementDataPushButtonWithAttributes
performCommand
LibCall_ACMSecContextCopyCredentialsArrayEx
LibCall_ACMContextCredentialGetProperty
%s: %s: constraintState = %p.\n
cchkdf
ACMRequirementGetSubrequirements
crypto_encryptText_version1
ACMGlobalContextAddCredential
Failed to obtain plain data size, status: %d
LibCall_ACMContextVerifyPolicyEx_Block
ACMRequirement - ACMRequirementDataRatchet
<data>
crypto_generateKeyFromSharedInfo_version2
ACMCredential - ACMCredentialDataPasscodeValidated
ACMGetEnvironmentVariable
array of ACMParameter
ACMContextVerifyPolicyEx
ACMContextRemovePassphraseCredentialsByPurposeAndScope
generateRandom
dst || !dstCapacity
ACMCredential - ACMCredentialDataBiometryMatchAttempted
ACMRequirement - ACMRequirementDataAP
Util_DeallocRequirement
LibCall_ACMContextRemoveCredentialsByValueAndScope
%02x 
%s
ACMRequirement - ACMRequirementDataPasscodeValidated
ACMLib
Util_DeallocCredential
ACMCredential
ACMRequirement - ACMRequirementDataBiometryMatched
ACMContextVerifyPolicy
%s: %s (len=%u): operation:
ccrng
ACMRequirement
ACMRequirement - ACMRequirementDataOr
ACMContextContainsPassphraseCredentialWithPurpose
ACMCredential - ACMCredentialDataPasscodeValidated2
Failed to create ACM context, status: %d
LibCall_ACMGetEnvironmentVariable_Block
LibCall_ACMRequirementDelete
%s: %s: context = %p.\n
serializeParameters
Failed to obtain encryption size, status: %d
LibCall_ACMGlobalContextCredentialGetProperty_Block
ACMContextAddCredentialWithScope
ACMRequirementGetProperty
ACMSetEnvironmentVariable
@8@?0
checkCCError
ccgcm_update
LibCall_ACMTRMSaveState
ACMGlobalContextCredentialGetProperty
ACMContextCopyData
ACMContextDelete
DeserializeCredentialList
ACMRequirement - ACMRequirementDataAnd
ACMGlobalContextRemoveCredentialsByType
LocalAuthenticationCredentialServices.LACSExtractableCredential
LibSerialization.c
LibCall_ACMGetAclAuthMethod_Block
ACMContextSetData
LibCall_ACMContextContainsCredentialTypeEx
Failed to decrypt data, status: %d
DeserializeVerifyAclConstraint
crypto_generateKeyFromSharedInfo_version1
Util_SafeDeallocParameters
ACMCredential - ACMCredentialDataContinuityUnlock
ACMRequirement - ACMRequirementDataPushButton
ACMRequirement - ACMRequirementDataPasscodeValidatedWithAttributes
ACMGetAclAuthMethod
CredentialServices.Context
crypto_encryptText
ACMRequirement - ACMRequirementDataBiometryMatchedWithAttributes
ACMParseAclAndCopyConstraintCharacteristics
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c
v24@?0@\"NSData\"8@\"NSError\"16
%s: %s: called.\n
%s: %s: returning, -> ctx = %p.\n
%s: %s: returning, err = %ld, code=%u.\n
%s: %s: cmd(%u) on CS[%u] -> err 0x%x (%d).\n
%@
Failed to create ACM context from context ref
Credential extraction failed (err:%@)
Failed to create LACSUnmanagedSecurePassword: %{public}@
Failed to create LACSUnmanagedExtractablePassword with contextRef: %{public}@
%s: %s: returning.\n
%s: %s: returning, err = %ld, var=%u.\n
Failed to create LACSSecurePassword: %{public}@
%s: %s: CS[%u] created (flags=0x%x).\n
%s: %s: CS[%u] acquired.\n
%s: %s: CS[%u] deleted (contextDestroyed=%s).\n
Credential storage failed (err:%@)
Failed to create LACSExtractablePassword: %{public}@
Failed to extract data %{public}@
%s: %s: returning, err = %ld.\n
%s: %s: log level set to %d.\n
%s: %s: cmd(%u) on CS[%u] -> ok.\n
%{public}@
Failed to create LACSUnmanagedSecurePassword with contextRef: %{public}@
Failed to create LACSUnmanagedExtractablePassword: %{public}@
softlink:r:path:/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
LACSContext
LACSExtractablePassword
NSSecureCoding
LACSUnmanagedSecurePassword
NSObject
LACSExtractableCredential
LACSSecureCredential
NSCoding
LACSUnmanagedContext
LACSError
_TtC37LocalAuthenticationCredentialServices12LACSPassword
LACSUnmanagedExtractablePassword
_TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword
LACSSecurePassword
errorWithDomain:code:userInfo:
hash
init
initWithExternalizedContext:userSession:
T@\"LACSSecurePassword\",N,R,Vpassword
T@\"NSData\",R,N
data:
dataWithLength:
withContextRef:
autorelease
bytes
class
performSelector:
uuidBytes
externalizedContext
initWithContext:
initWithContextRef:error:
mutableBytes
respondsToSelector:
fetchCredentialData:
TQ,R
_encryptData:seed:externalizedContext:error:
externalize
secureCopy:
supportsSecureCoding
context
T@\"NSString\",R,C
T@\"_TtC37LocalAuthenticationCredentialServices12LACSPassword\",N,R,Vpassword
conformsToProtocol:
dataWithBytes:length:
description
dictionaryWithObjects:forKeys:count:
initWithData:contextRef:error:
T@\"NSString\",?,R,C
.cxx_destruct
init:
initWithBytes:length:
isEqual:
isKindOfClass:
length
secureCopy
debugDescription
stringWithFormat:
uuid
_ownsContextRef
release
_errorWithCode:userInfo:
_withContext:error:
credentialOfType:reply:
data
setCredential:type:error:
unsafeContextRef
T@\"_TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword\",N,R,Vpassword
initWithCoder:
superclass
dealloc
T@\"LAContext\",R,N,V_context
_decryptData:seed:externalizedContext:error:
_externalizedContextRef
initWithUUID:password:error:
T@\"LACSExtractablePassword\",N,R,Vpassword
T@\"<LACSContext>\",N,R,Vcontext
errorWithCode:debugDescription:
isProxy
TB,R
contextRef
initWithContextRef:
initWithData:error:
performSelector:withObject:
_contextRef
_encryptionSeedForContext:error:
isMemberOfClass:
performSelector:withObject:withObject:
retain
storeCredentialData:securely:error:
TB,N,R
encodeObject:forKey:
errorWithCode:
initWithPassword:
retainCount
zone
_context
initWithACMContextRef:ownsContextRef:
password
self
T#,R
T@\"NSUUID\",N,R
_newZeroingDataWithBytesNoCopy:length:deallocator:
encodeWithCoder:
@32@0:8^{__ACMHandle=}16^@24
@32@0:8q16@24
B16@0:8
Q16@0:8
Vv16@0:8
@48@0:8@16@24@32^@40
^{__ACMHandle=}
B
@\"LAContext\"
@24@0:8@16
@24@0:8^@16
@16@0:8
@\"LACSExtractablePassword\"
B36@0:8@16B24^@28
@\"NSData\"24@0:8^@16
@40@0:8@16@24^@32
#16@0:8
@\"NSData\"16@0:8
v24@0:8@?16
@\"<LACSContext>\"
@\"NSString\"16@0:8
B36@0:8@\"NSData\"16B24^@28
B32@0:8@?16^@24
v24@0:8@16
@24@0:8:16
v24@0:8@\"NSCoder\"16
@24@0:8@\"NSCoder\"16
^{_NSZone=}16@0:8
@24@0:8q16
@\"_TtC37LocalAuthenticationCredentialServices12LACSPassword\"
B24@0:8#16
v16@0:8
B24@0:8@16
B24@0:8:16
@28@0:8^{__ACMHandle=}16B24
@\"NSData\"
@\"_TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword\"
@\"LACSSecurePassword\"
@32@0:8:16@24
@40@0:8:16@24@32
B24@0:8@\"Protocol\"16
@32@0:8@16^@24
```
