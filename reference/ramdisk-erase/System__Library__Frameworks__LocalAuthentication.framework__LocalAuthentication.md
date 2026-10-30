# `/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 817,664 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 37 (Size: 5712)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe, NlistOutofsyncWithDyldinfo
```

## Linked libraries (19)

- `/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication (compatibility version 1.0.0, current version 2319.52.2)`
- `/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore (compatibility version 1.0.0, current version 2319.52.2)`
- `/System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/LocalAuthenticationCredentialServices (compatibility version 1.0.0, current version 2319.52.2)`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking (compatibility version 1.0.0, current version 72.0.0)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils (compatibility version 1.0.0, current version 2319.52.2)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/Combine.framework/Combine (compatibility version 1.0.0, current version 3023.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0, weak)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0)`
- `/usr/lib/swift/libswiftObservation.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2, weak)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3, weak)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (83 classes, 31 protocols)

Classes: `Invalidation`, `LAACL`, `LAACLBuilder`, `LAACLBuilderCustomACLParams`, `LAACLCoder`, `LAAccessKey`, `LAAuthenticationBiometricMethod`, `LAAuthenticationBiometricMethodConfiguration`, `LAAuthenticationBiometricMethodState`, `LAAuthenticationMethod`, `LAAuthenticationMethodConfiguration`, `LAAuthenticationMethodResult`, `LAAuthenticationMethodState`, `LAAuthenticationRequirement`, `LAAuthorizationError`, `LABiometryFallbackRequirement`, `LAClient`, `LAContext`, `LAContextProvider`, `LACustomPasswordRequirement`, `LADomainState`, `LADomainStateBiometry`, `LADomainStateCompanion`, `LAEnvironment`, `LAEnvironmentMechanism`, `LAEnvironmentMechanismBiometry`, `LAEnvironmentMechanismCompanion`, `LAEnvironmentMechanismUserPassword`, `LAEnvironmentServiceXPCClient`, `LAEnvironmentState`, `LAExtendedRequirement`, `LAExtractablePassword`, `LAKeyIdentifier`, `LAKeyStoreBackendBuilder`, `LAKeyStoreBackendQueryBuilder`, `LAKeyStoreBuilder`, `LAKeyStoreItemBuilder`, `LAKeyStoreSecretCoder`, `LAPersistedRight`, `LAPrivateKey`, `LAPublicKey`, `LARatchet`, `LARatchetErrorBuilder`, `LARatchetFeatureEnablementOptions`, `LARatchetManager`, `LARatchetObserverWrapper`, `LARatchetState`, `LARatchetStateValue`, `LARatchetStateValueArmed`, `LARatchetStateValueCollapsed`, `LARatchetStateValueExpired`, `LARatchetStateValueNotStarted`, `LARatchetStateValueReady`, `LARatchetStateValueWaitingForCoolOff`, `LARatchetStateValueWaitingForSecondAuthentication`, `LARight`, `LARightContextHandler`, `LARightStore`, `LASecret`, `LAStorage`, `LAUIDelegateWeakBox`, `_LAAuthenticationBiometricMethodShim`, `_LABKDevice`, `_LABKDeviceDescriptor`, `_LABKDeviceManager`, `_LABKDevicePearl`, `_LABKDeviceTouchID`, `_LABKFaceDetectOperation`, `_LABKFingerDetectOperation`, `_LABKLog`, `_LABKMatchOperation`, `_LABKMatchPearlOperation`, `_LABKMatchResultInfo`, `_LABKOperation`, `_LABKPresenceDetectOperation`, `_LAKeyStore`, `_LAKeyStoreBackendFake`, `_LAKeyStoreBackendKeychain`, `_LAKeyStoreGenericPassword`, `_LAKeyStoreGenericPasswordNull`, `_LAKeyStoreKey`, `_LAKeyStoreKeyNull`, `_LAMKBLog`

Protocols: `BKDeviceDelegate`, `BKMatchOperationDelegate`, `BKOperationDelegate`, `LAACLSerializable`, `LAAuthenticationBiometricMethodObserver`, `LAAuthenticationMethodObserver`, `LACContextCallbackXPC`, `LACContextExternalizing`, `LACContextExternalizingXPC`, `LACContextObserver`, `LACContextProviding`, `LACDTORatchetObserver`, `LACEnvironmentServiceXPC`, `LACRemoteContext`, `LACSecureStorageService`, `LAContextClientEvaluationProt`, `LAContextEventFeedbackProt`, `LAContextPropertiesProt`, `LAContextXPC`, `LADaemonXPC`, `LAKeyStore`, `LAKeyStoreBackend`, `LAKeyStoreGenericPassword`, `LAKeyStoreKey`, `LARightContextHandlerDelegate`, `LAUIDelegate`, `NSCoding`, `NSCopying`, `NSObject`, `NSSecureCoding`, `_LAKeyStoreGenericPasswordCryptor`

## Strings (2,050)

```
v16@?0@\"NSError\"8
LARight.m
MKBKeyBagKeyStashCreateWithOpts
Invalid update value type.
Failed to create LAContext
LARightStore
v32@?0@\"NSDictionary\"8Q16^B24
%@ value expected
MKBGetDeviceLockStateInfo
v24@?0@\"<LAPrearmContextXPC>\"8@\"NSError\"16
LARight[%u]
kLACServiceTypeSecureStorage
%ds
Token
LAPublicKey[%u]
started: %@
v32@?0@\"<LAContextXPC>\"8@\"NSString\"16@\"NSError\"24
rawValue: %@
INF
No authentication required.
TCCService
pad
acmh
cbio
LARight
_LAMKBKeyBagPerformRecovery
The right associated with this key was deallocated
acl
oke
Invalid update value type, expecting dictionary.
Q8@?0
Collapsed
isExtendedPolicyModeEnabled: 
com.apple.LocalAuthentication.environment.StateDidChange
_privateKeys.count == 1
Policy can't be satisfied without UI delegate.
The provided data should have between %d and %d bytes
cup
v24@?0@\"NSXPCListenerEndpoint\"8@\"NSError\"16
com.apple.LocalAuthentication.Storage
MKBEventsUnregister
BKErrorDomain
UUID
new
kv
%@:akey
LAStorage[%u]
0`
ad
_LAMKBGetDeviceLockStateInfo
p
BKDevice
v24@?0@\"LAPersistedRight\"8@\"NSError\"16
v16@?0@?<v@?@@\"NSError\">8
biometry: %@
Error.LocalAuthentication.coreauthd_client
-[_LAKeyStore encryptData:publicKeyHash:completion:]_block_invoke_3
RatchetState
Expected NSData or NSNumber.
Ready
v32@?0@\"NSMutableArray\"8Q16^B24
ow
bkshim
v40@?0@\"<LAContextXPC>\"8@\"NSUUID\"16@\"NSString\"24@\"NSError\"32
_state == LARightStateNotAuthorized
Missing Implementation
MKBPrewarmSPS
LAPrivateKey
isAutoEnablement: 
od
BiometryDatabaseHash
bh
odel
Invalid 'context' argument.
v24@?0@\"<LAKeyStoreGenericPassword>\"8@\"NSError\"16
af
Operation interrupted
com.apple.LocalAuthentication.LARatchetErrorDomain
BKDeviceDescriptor
bc
v8@?0
Failed to build key due to missing 'accc'
LAPublicKey
 uiDelegate:%@
LAPersistedRight.m
forwarding to BK
d
Invalid acmContext.
LAEnvironment work queue
com.apple.CoreAuthentication.daemon.libxpc
Cannot perform operation with nil context
Subcode
TCCServerPrompt
o
v24@?0@\"<LACEnvironmentServiceXPC>\"8@\"NSError\"16
v16@?0q8
*
WaitingForCoolOff
BKPresenceDetectOperation
RetryTime
:
-[LARightStore rightForIdentifier:completion:]_block_invoke_2
LAKeyStore.m
v24@?0@8@\"NSError\"16
_secrets.count <= 1
-> %d
cag
ock
This method has been deprecated
AutoEnablementDenialReason
cpo
orwk
v32@?0@8@16^B24
Failed to get externalized context from LAContext
Cannot perform a key exchange with the given public key.
Invalid remove query %@
Failed to create XPC connection.
with externalized context %x
mkbshim
iter
dacl
@\"LAACLBuilderCustomACLParams\"8@?0
LAStorage[%u] bound with %@
%@,%s
stateHash: %@
Key with identifier '%@' is already present
A
Ratchet not ready
okd
v24@?0@\"NSDictionary\"8@\"NSError\"16
MKBDeviceUnlockedSinceBoot
override
Required data decoder not found
kLAAccessKeyNonce
Failed to build key due to missing 'klbl'
_LAMKBKeyBagKeyStashCommit
_LAMKBKeyBagKeyStashVerify
duration: %@
ag
oa
@\"NSMutableArray\"8@?0
v16@?0@8
_LAMKBGetDeviceLockState
MKBLockDevice
error
AvailableMechanisms
cob
oece
Could not load secret
-> deviceType:%d, BKDevice=%@
async-starting operation %@
BKFaceDetectOperation
kt
Required data coder not found
LAEnvironment notification queue
<biometricState:touchID=%d,faceID=%d,lockoutState=%08x>
biometryType: %@
rkm
pcma
Invalid operation type.
%@:genp
laabio
_LAMKBUnlockDevice
]
oecd
oect
![wrappedData isEqualToData:cpher]
Lost connection to coreauthd.
-nd
tag
q
Could not encode data
com.apple.LocalAuthentication
MKBGetDeviceConfigurations
async
rk
LAEnvironment observer queue
Failed to build 'genp' due to missing 'r_Data'
-[LAUIDelegateWeakBox event:params:reply:]
, 
wrapping %@ with %@
LAContext
v24@?0@\"NSArray\"8@\"NSError\"16
(err:%@)
-[LAPersistedRight secret]
v16@?0@\"<LAAuthenticationMethodObserver>\"8
#
<...>
v20@?0i8^{__CFDictionary=}12
_LAMKBEventsUnregister
Identifier cannot be empty
LASecret
@\"NSMutableDictionary\"8@?0
isStrictModeEnabled: 
bid
Failed to build key due to missing 'labl'
_LAMKBPrewarmSPS
%@,%d
pd
coreauthd_client
v12@?0i8
v24@?0@\"LACEnvironmentState\"8@\"NSError\"16
Missing required 'LAOptionAuthenticationReason' option
MKBDeviceLockAssertion
NO
successfully
Invalid data size
<%@ %p; %@>
_LAMKBEventsRegister
LAPrivateKey[%u]
Helper context invalidated
v32@?0@\"<LAKeyStoreKey>\"8Q16^B24
v32@?0@8@16@?<v@?@\"NSError\">24
(err=%@)
Key creation failed for query %@
-[LAPersistedRight key]
NotStarted
wk
Could not generate nonce
-[LARight deauthorizeWithCompletion:]_block_invoke
v16@?0@?<v@?B@\"NSError\">8
f
ckon
ouw
Invalid update request.
_LAMKBEventsRegister_block_invoke
Unable to find class %s
salt
err != nil || keys != nil
Failed to build 'genp' due to missing 'gena'
MKBKeyBagPerformRecovery
availableCompanions: %@
companion: %@
pub
Invalid format
LARightStore.m
v24@?0@\"<LAKeyStoreKey>\"8@\"NSError\"16
com.apple.CoreAuthentication.daemon
v24@?0@\"<LACSecureStorageService>\"8@?<v@?@@\"NSError\">16
_LAMKBGetDeviceConfigurations
%@,%@
BKFingerDetectOperation
TKTLVRecord
Failed to build key due to missing public key
invalidate called
_LAMKBDeviceUnlockedSinceBoot
MKBEventsRegister
sync-starting operation %@
sync
Non-empty localizedReason must be provided.
The right associated with this secret was deallocated
init()
MKBUnlockDevice
LAContext[%u:%@
Invalid 'ACL' argument.
TKBERTLVRecord
v24@?0@\"NSData\"8@\"NSError\"16
LASecret[%u]
Resource not found
v24@?0@\"NSNumber\"8@\"NSError\"16
_LAMKBDeviceLockAssertion
Invalid uid: %u
oc
com.apple.LocalAuthentication:Authorization:%@
err != nil || genps != nil
Invalid context.
_LAMKBKeyBagKeyStashCreateWithOpts
MKBGetDeviceLockState
MKBKeyBagKeyStashCommit
osgn
-> %@
YES
BKMatchPearlOperation
isGracePeriodEnabled: 
kid
os
oskc
v24@?0@\"LACDTORatchetState\"8@\"NSError\"16
%s
WaitingForSecondAuthentication
APLA
err != nil || key != nil
LAContextUITrampoline
Failed to build key due to missing 'kref'
Invalid fetch query %@
Internal error - unexpected data type
@\"NSObject\"24@?0@\"NSObject\"8^@16
LocalAuthentication_Private.LARatchetFeatureEnablementOptions
@\"LACDTOFeatureEnablementOptions\"8@?0
Authorization
com.apple.LocalAuthentication.ratchet.StateDidChange
i
LARightStore[%u]
Cannot perform operation with invalid context
\"
; 
BKMatchOperation
Nonce
_LAMKBLockDevice
context dealloc
pkofn
NULL
MKBKeyBagKeyStashVerify
MechanismTree
BiometryType
v20@?0B8@\"NSError\"12
%d
uuid: %@
success
oe
la_client
No results for query %@
v32@?0@\"<LAKeyStoreGenericPassword>\"8Q16^B24
Failed to build 'genp' due to missing 'labl'
kLACServiceTypeEnvironment
ed
prp
softlink:r:path:/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
softlink:o:path:/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit
softlink:o:path:/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI
softlink:r:path:/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
softlink:r:path:/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit
objectForKey:%d
objectForKey:%d returned error: %{private}@
LocalAuthentication.Authorization.exportBytes
LocalAuthentication.Authorization.encrypt
%{public}@ exchangeKeys started
notifyEvent:%d cid:%u
Failed to query environment state for user %u: %@
LocalAuthentication.Authorization.rightForIdentifier.fetchKeys
The right associated with this secret was deallocated
%s:callback(type=%d, handle_state=%@
evaluatePolicy on %{public}@ cid:%u returned %{public}@
canEvaluatePolicy:%d on %{public}@ cid:%u returned %{public}@
resetProcessedEvent:%d on %{public}@ cid:%u returned %{public}@
setCredential:%d type:%d on %{public}@ cid:%u returned %{public}@ when attempting to encode credential
%{public}@ _saveRight finished successfully
removeObjectForKey:%d returned error: %{private}@
%s:: -> %@
%{public}@ encrypt started
LAEvaluateAndUpdateACL -> %d, %@
%{public}@ saveRight started
LocalAuthentication.Authorization._saveRight.storeGenericPassword
%{public}@ TCC access request for %@ returned %d
%s:options:%@ -> %@ (%@)
serverPropertyValueForOption:%d on %{public}@ cid:%u returned %{public}@
%{public}@ authorizeWithLocalizedReason finished %{public}@
setObject forKey:%d
LocalAuthentication.Authorization.exchangeKeys
Encoding %{public}@ for transfer to pid:%d cid:%u
Extracting a LACredentialTypeExtractablePassword will require the '%@' entitlement. The operation will be allowed for now. Error: %{public}@
credentialOfType:%d on %{public}@ cid:%u returned %{public}@ when attempting to decode credential
verifyFileVaultUser:%{public}@ volumeUuid:%{public}@ options:%u on %{public}@ cid:%u
externalizedContext on %{public}@ cid:%u
%{public}@ rightForIdentifier started
xpc_connection_set_target_user_session_uid() setting uid:%{public}@
%s:secret:%s option:%@ -> %d
LocalAuthentication.Authorization.canDecrypt
Will notify %d observers of changes in %{public}@
xpc_user_sessions_get_foreground_uid() failed with error %d - %s
%{public}@ target uid: %u
Encountered XPC error on remote proxy: %{private}@
%{public}@ decrypt started
resetWithReply on %{public}@ cid:%u returned %{public}@
Will invoke authentication using policy %d
%s:: -> %d
LocalAuthentication.Authorization.authorizeWithLocalizedReason
%{public}@ authorizeWithOptions finished %{public}@
LocalAuthentication.Authorization.rightForIdentifier
unhandled error for canEvaluate: %@
returned biometryType: %d
Inconsistent result: both error and credential are valid
%s:options:%@ -> %@
Failed to register %{public}s: %u
%{public}@ rightForIdentifier finished successfully
Encoded %{public}@ for transfer with token:%x cid:%u
failProcessedEvent:%d failureError:%{public}@ on %{public}@ cid:%u returned %{public}@
%{public}@ saveRightWithSecret started
Could not derive auth constraints (%{public}@)
objectForKey:%d returned success
LocalAuthentication.Authorization.canVerify
LocalAuthentication.Authorization.canSign
setCredential:forProcessedEvent:%d credentialType:%d on %{public}@ cid:%u
setServerPropertyForOption:%d value:%{public}@ on %{public}@ cid:%u returned %{public}@
externalizedContext on %{public}@ cid:%u returned %x
%{public}@ authorizeWithOptions %{public}@ started
%{public}@ removeAllRights started
%{public}@ fetchData
%{public}@ failed to initialize: %{public}@
setObject forKey:%d returned success
LocalAuthentication.Authorization.sign
setOptions:%x forInternalOperation:%d on %{public}@ cid:%u returned %{public}@
LACopyResultOfPolicyEvaluation -> %@, %@
Operation interrupted
%{public}@ removeRight started
%{public}@ removeRightForIdentifier started
exchangeData forKey:%d returned success
%{public}@ encrypt finished %{public}@
%{public}@ created %{public}@ cid:%u
Encoded %{public}@ for transfer to pid:%d cid:%u
pauseProcessedEvent:%d pause:%d on %{public}@ cid:%u
unknown LAEventParamCoachingFeedback %d received, ignoring
Created LAStorage
%{public}@ verify started
invalidate %{public}@ cid:%u internally returned %{public}@
evaluateAccessControl on %{public}@ cid:%u returned %{public}@
setShowingCoachingHint:%d event:%d on %{public}@ cid:%u returned %{public}@
verifyFileVaultUser:%{public}@ volumeUuid:%{public}@ on %{public}@ cid:%u returned %{public}@
Invalidating domain state cache
Failed to obtain environment endpoint %{public}@
LocalAuthentication.Authorization.authorizeWithOptions
%{public}@ removeRightForIdentifier finished %{public}@
Could not set ACL protection (%{public}@)
unknown LAEventParamPearlSimpleStatus %d received, ignoring
LAEvaluateAndUpdateACL(%@, %@, %@)
LocalAuthentication.Authorization.rightForIdentifier.fetchGenericPasswords
unhandled bioevent: %d
LocalAuthentication.Authorization.verify
failProcessedEvent:%d failureError:%{public}@ on %{public}@ cid:%u
evaluateAccessControl:%{public}@ operation:%{public}@ options:%{public}@ on %{public}@ (%{public}s) cid:%u
serverPropertyValueForOption:%d on %{public}@ cid:%u
LocalAuthentication.Authorization.saveRightWithSecret
%{public}@ removeAllRights finished %{public}@
evaluatePolicy:%d options:%{public}@ on %{public}@ (%{public}s) cid:%u
setCredential:forProcessedEvent:%d credentialType:%d on %{public}@ cid:%u returned %{public}@
prearmTouchIDWithReply on %{public}@ cid:%u
setShowingCoachingHint:%d event:%d on %{public}@ cid:%u
LocalAuthentication.Authorization.saveRight
%{public}@ removeRight finished %{public}@
Retrying on externalizedContextProvider
removeObjectForKey:%d
%s:queue:%@ -> %p
%@ didAuthenticateWithResult:%@
evaluationMechanismsForAccessControl:%@ on %{public}@ cid:%u
LocalAuthentication.Authorization.deauthorizeWithCompletion
LocalAuthentication.Authorization._saveRight.storeKey
Invalid authType
%{public}@ has encountered XPC error on synchronous proxy: %{public}@
%{public}@ will keep returning %{public}@ from now on
setObject forKey:%d returned error: %{private}@
%{public}@ exportBytes finished %{public}@
setCredential:forProcessedEvent:%d credentialType:%d on %{public}@ cid:%u returned %{public}@ when attempting to encode credential
LocalAuthentication.Authorization.rightForIdentifier.fetchKey
LocalAuthentication.Authorization.removeAllRights
Could not initialize trivial ACL (%{public}@)
%{public}@ connection to server interrupted (recovery: %d, willRetry: %d)
unknown LATouchIDSimpleStatus %d received, ignoring
setOptions:%x forInternalOperation:%d on %{public}@ cid:%u
Creating LAContext %{public}@ cid:%u
Failed to get transfer token: %{public}@ cid:%u
DomainState on %{public}@ returned: %{public}@
setCredential:type:%d options:%{public}@ on %{public}@ cid:%u
%{public}@ rightForIdentifier finished %{public}@
%{public}@ saveRightWithSecret finished %{public}@
LocalAuthentication.Authorization._saveRight.rightForIdentifier
%s:ref:%p
LocalAuthentication.Authorization.canEncrypt
%{public}@ verify finished %{public}@
%{public}@ sign finished %{public}@
evaluationMechanismsForPolicy:%d on %{public}@ cid:%u
Connecting to %{public}@, flags:%x, uid:%{public}@
initial evaluatePolicy succeeded
%{public}@ created with uuid: %x token: %x
evaluationMechanismsForPolicy:%d on %{public}@ cid:%u returned %{public}@
evaluationMechanismsForAccessControl:%@ on %{public}@ cid:%u returned %{public}@
canEvaluatePolicy:%d on %{public}@ cid:%u
retryProcessEvent:%d on %{public}@ cid:%u returned %{public}@
Stashing a LACredentialTypeExtractablePassword will require the '%@' entitlement. The operation will be allowed for now. Error: %{public}@
%{public}@ checkCanAuthorizeWithCompletion started
%@ init, method=%@
credentialOfType:%d on %{public}@ cid:%u
credentialOfType:%d on %{public}@ cid:%u returned
prearmTouchIDWithReply on %{public}@ cid:%u returned %{public}@
LACopyResultOfPolicyEvaluation(%@, %d, %@)
Invalid acmContext
%s:options:%@ -> %d
%{public}@ initialized
%{public}@ authorizeWithLocalizedReason '%{public}@' started
%{public}@ checkCanAuthorizeWithCompletion finished %{public}@
exchangeData forKey:%d returned error: %{private}@
LocalAuthentication.Authorization.canExchangeKeys
credentialOfType:%d on %{public}@ cid:%u returned %{public}@
optionsForInternalOperation:%d on %{public}@ cid:%u returned %{public}@
LocalAuthentication.Authorization.authorizeWithOptions.completion
LocalAuthentication.Authorization._saveRight
%{public}@ _saveRight finished %{public}@
%{public}@ invalidated stale XPC connection before creating a new one
evaluatePolicy finished with error: %@
Did reboot successfully
notifyEvent:%d cid:%u returned %{public}@
retryProcessEvent:%d on %{public}@ cid:%u
%@ updated from %@ to %@
%{public}@ deallocated
LocalAuthentication.Authorization.checkCanAuthorizeWithCompletion
Skipping AP constraints
initial evaluatePolicy failed, error: %@
setServerPropertyForOption:%d value:%{public}@ on %{public}@ cid:%u
LocalAuthentication.Authorization.removeRightForIdentifier
%{public}@ _saveRight started
Could not initialize ACL (flags=%d) (%{public}@)
Retrying on an interrupted XPC connection
%{public}@ decrypt finished %{public}@
%@:%@: %@
authMethodWithReply on %{public}@ cid:%u
LocalAuthentication.Authorization.removeRight
%{public}@ invalidated by server: %{public}@
got bio event: %d (%@)
%s:options:%@ stash_mode:%d ACMRef:%@ passcode:%s -> %d
The right associated with this key was deallocated
setCredential:%d type:%d on %{public}@ cid:%u returned %{public}@
Discrepancy between option %d value (%d) and property value (%d)
LocalAuthentication.Authorization.getRequirementKey
evaluatePolicy finished with result: %@
removeObjectForKey:%d returned success
Rebooting for error
LocalAuthentication.Authorization.decrypt
Failed to allow transfer to pid:%d cid:%u: %{public}@
DomainState on %{public}@
isCredentialSet:%d on %{public}@ cid:%u returned %{public}@
%{public}@ saveRight finished %{public}@
exchangeData forKey:%d
%{public}@ exportBytes started
%@ didChangeState:%@
optionsForInternalOperation:%d on %{public}@ cid:%u
LocalAuthentication.Authorization.fetchData
Invalidating %{public}@ cid:%u
resetProcessedEvent:%d on %{public}@ cid:%u
isCredentialSet:%d on %{public}@ cid:%u
resetWithReply on %{public}@ cid:%u
authMethodWithReply on %{public}@ cid:%u returned %{public}@
%{public}@ is recovering connection to server
%@ not forwarding %s, receiver is nil
Using real storage
Failed to reboot with error: %{private}@
%{public}@ sign started
%{public}@ exchangeKeys finished %{public}@
%@ didStartWithState:%@
pauseProcessedEvent:%d on %{public}@ cid:%u returned %{public}@
LocalAuthentication.Authorization.authorizeWithLocalizedReason.completion
%{public}@ fetchData finished %{public}@
_LAKeyStoreKey
LAKeyStoreBuilder
LAAuthenticationMethodResult
LAExtractablePassword
_LAAuthenticationBiometricMethodShim
LARatchetStateValueCollapsed
LAExtendedRequirement
_LAKeyStore
LAKeyStoreGenericPassword
LADomainStateBiometry
LACustomPasswordRequirement
LAPersistedRight
LAAuthorizationError
LAAuthenticationBiometricMethodObserver
LARatchetStateValueNotStarted
LARatchetStateValueArmed
LADomainStateCompanion
LACContextExternalizingXPC
LAContextPropertiesProt
LAContextEventFeedbackProt
LAAuthenticationBiometricMethodState
LABiometryFallbackRequirement
LASecret
LAKeyStoreBackend
LACEnvironmentServiceXPC
LARightContextHandlerDelegate
LAKeyStore
LAContextProvider
LAEnvironment
LAKeyStoreItemBuilder
LARatchetStateValueReady
BKDeviceDelegate
_LABKDevicePearl
LACContextCallbackXPC
LAPrivateKey
_LABKDeviceDescriptor
_LABKMatchPearlOperation
_LABKFaceDetectOperation
LARatchet
_LAKeyStoreBackendKeychain
LAAuthenticationBiometricMethod
_LABKDevice
BKOperationDelegate
LAACLSerializable
LAACLBuilder
LAUIDelegate
NSCoding
LARatchetManager
LAKeyStoreSecretCoder
LAUIDelegateWeakBox
LARatchetState
_LABKMatchResultInfo
LARightContextHandler
LAEnvironmentMechanismCompanion
LAContextXPC
LAAuthenticationMethodConfiguration
NSCopying
LAKeyStoreBackendQueryBuilder
_LAMKBLog
LACSecureStorageService
_LABKFingerDetectOperation
LARatchetStateValueExpired
LARatchetErrorBuilder
_LABKOperation
_LABKPresenceDetectOperation
LAEnvironmentMechanismUserPassword
LAAuthenticationMethod
_LABKLog
LAAccessKey
Authorization
_LAKeyStoreBackendFake
_LABKDeviceManager
_LAKeyStoreGenericPassword
LAClient
LAStorage
LACContextProviding
LAAuthenticationBiometricMethodConfiguration
BKMatchOperationDelegate
LARatchetStateValue
LAAuthenticationRequirement
LACContextObserver
LAEnvironmentMechanismBiometry
LAEnvironmentState
LACDTORatchetObserver
NSObject
LAKeyIdentifier
_LAKeyStoreKeyNull
LAACLBuilderCustomACLParams
LARatchetObserverWrapper
_LAKeyStoreGenericPasswordCryptor
_LAKeyStoreGenericPasswordNull
LAEnvironmentMechanism
LADaemonXPC
LAKeyStoreBackendBuilder
LAAuthenticationMethodState
LAEnvironmentServiceXPCClient
NSSecureCoding
LAACL
LAContextClientEvaluationProt
LARatchetStateValueWaitingForSecondAuthentication
LACRemoteContext
LAACLCoder
LACContextExternalizing
LARightStore
LAKeyStoreKey
LAAuthenticationMethodObserver
LAPublicKey
LARatchetFeatureEnablementOptions
_LABKMatchOperation
LAContext
LARatchetStateValueWaitingForCoolOff
LARight
Invalidation
_LABKDeviceTouchID
LADomainState
authenticationContext
biometryCurrentSetRequirementWithFallback:
stateHash
T@\"BKOperation\",R,N,V__BKOperation
_decodeCredential:type:reply:
_keys
error:hasCode:
optionCallerPID
_backend
_subrequirements
boolForKey:error:
dictionaryForKey:error:
evaluateACL:operation:options:reply:
T@\"NSDictionary\",R,N
initWithExternalizedContext:userSession:
isAutoEnablementAllowed:
optionDisableVisionCompanion
cancelArmRequestWithIdentifier:reason:completion:
client
getDomainStateWithOptions:synchronous:reply:
optionLightweightUIMode
setOptionSkipIntentConfirmation:
_errorWithCode:debugDescription:
_evaluateAccessControl:operation:options:log:cid:synchronous:reply:
addEntriesFromDictionary:
initWithAvailableUsers:
initWithKey:
optionPINTitle
setLocalizedFallbackTitle:
_authType
_externalizedContext
authorizeWithLocalizedReason:completion:
numberForKey:error:
setOptionDisableAutomaticPasscodeFallback:
resetWithReply:
_password
entitlementsChecker
sharedInstance
Tq,N,V_authType
_synchronousRemoteObjectProxy:performCall:
buildWithDictionary:error:
invalidations
setIsAutoEnablement:
deserializeACL:
companionType
notifyEvent:
Tq,R,N
_handleConnectionResult:uuid:proxyId:error:
checkACL:
count
denyAllACL
initWithCoreMechanism:
_maxBiometryFailures
fetchItemsWithQuery:error:
setAuthenticationType:
setDelegate:
setOptionLightweightUI:
dictionaryForKey:
lockoutState
optionBiometryLockoutRecovery
retainCount
setExternalizedContextProvider:
_resolveCombinedStateHash
dataUsingEncoding:
externalizedContextWithReply:
setCredentialsUUID:reply:
numberWithBool:
_publicKeyHash
setOptionCheckApplePayEnabled:
T@\"LAContext\",R,N,V_context
_context
biometricMethodState
initWithRawValue:value:uuid:
setOptionRedactErrors:
initWithSource:
matchOperation:matchedWithResult:
removeItemsWithQuery:error:
_evaluatePolicy:options:synchronous:reply:
addConstraint:
authenticationMethodWillTerminate:
bioLockoutState:forUser:error:
initWithDuration:
_registerDarwinNotification
_secrets
_tag
boolForKey:
remoteObjectProxy
sequenceOfRecordsFromData:
setInvalidationHandler:
T@\"LAClient\",R,N,V_client
_coreState
_wrappedData
avoidUsingFaceIDCamera
deviceTypeNotSupportedWithUserInfo:
mutableCopy
verifyData:signature:secKeyAlgorithm:completion:
T@\"BKDeviceDescriptor\",R,N,V_descriptor
_encodeCredential:type:reply:
_notifyObserversAfterInvalidation
null
requirementByAddingExtendedRequirement:
optionAuthenticationCallbackURL
_BKMatchPearlOperation
array
loadDataWithCompletion:
optionBeginRatchetShowsLocationWarning
optionPINMinLength
redactInternalError:
setOptionPINLength:
saltHash:withBundleID:
setInteractionNotAllowed:
setOptionSoftwareUpdateManifest:
setRight:
setOptionBeginRatchetLocalizedText:
setOptionNotInteractive:
setTouchIDAuthenticationRetryLimit:
boolValue
optionLightweightUI
_checkIdResultForTCC:synchronous:error:retryBlock:finally:
isUserPresent
setObserver:
T@\"_LAAuthenticationBiometricMethodShim\",R,N,V_shim
initWithDomain:authenticationContext:
instanceId
setIsFaceID:
_BKOperation
isEqualToDictionary:
optionNotInteractive
setOptionBeginSecurityDelayImmediately:
TB,N,VisAutoEnablement
_nullCharacterData
authorizeOperation:protectedBy:options:reply:
performSelector:withObject:withObject:
biometryRequirement
newCommandId
optionPINFirst
setOptionCallerPID:
checkCredentialType:
optionsForInternalOperation:reply:
setOptionMatchForUnlock:
T@\"NSObject<LAContextXPC>\",&,N,V_remoteContext
exchangeData:forKey:completionHandler:
setOptionNoGracePeriodUI:
T@\"<BKOperationDelegate>\",W,N,V_delegate
_setServerPropertyForOption:value:
didChangeValueForKey:
setObject:forKey:withOptions:completionHandler:
containsObject:
T@\"NSUUID\",&,N,V_uuid
evaluatedPolicyDomainState
TB,N,VisGracePeriodEnabled
authenticationMethod:didChangeState:
evaluationMechanismsForAccessControl:operation:error:
initWithExternalizedContext:uiDelegate:
lockedOut
lockoutStateFromError:
setCredentialCoder:
setQueue:
T@\"NSDictionary\",&,N,V_apConstraints
addObserver:
customPasswordRequirement:
nextInstanceIDInDomain:
objectForKey:contextUUID:connection:completionHandler:
releaseUIDelegate
T@\"NSNumber\",&,N
domain
interfaceWithInternalProtocol:
removeObject:
T@\"LACExternalizedContextProvider\",&,V_externalizedContextProvider
_synchronousRemoteContext
arrayByAddingObject:
retryProcessedEvent:reply:
_coreMechanism
objectForKeyedSubscript:
optionPINMaxLength
source
userPassword
matchOperation:providedFaceOcclusionInfo:
optionMatchForUnlock
setCredential:type:reply:
setOptionSoftwareUpdateStashMode:
_setQueue:
_updateStateWithSynchronousProxyToEnvironmentService:
canEvaluateCorePolicy:error:
createQueryForKeyWithIdentifier:domain:acl:
externalizedContext
T@\"LAAuthenticationBiometricMethodState\",R,V_biometricMethodState
_acl
debugDescription
setIdentity:
setIsGracePeriodEnabled:
stashPassword:error:
waitForStateUpdate
UUID
TB,N,V_isTouchID
_shouldRecoverConnection
credentialEncodingSeedWithReply:
defaultAccessKeyIdentifierForRightWithIdentifier:
optionDTO
removeRightForIdentifier:completion:
setUiDelegate:
T@\"NSString\",C,N
removeObjectForKey:contextUUID:connection:completionHandler:
addContextObserver:
T@\"<LAUIDelegate>\",W,N
T@\"BKFaceDetectOperation\",R,N
allKeys
_externalizedContextProvider
evaluateCorePolicy:options:error:
optionAllowUnapprovedSensor
setOptionDTO:
tag
T@\"NSError\",&,V_permanentError
T@\"LARatchetState\",R,N
_descriptor
setOptionPushButtonUseMaxPreArmAge:
_evaluationMechanismsFromReturnedError:error:
_workQueue
_fallbackAuthType
T@\"LAAuthenticationBiometricMethodState\",&,N,V_currentState
operation:stateChanged:
rawValue
removeObserver:forKeyPath:
setShowingCoachingHint:event:reply:
stringWithFormat:
TB,R,N
_remoteContext
errorNotArmedWithRatchetState:
isEqual:
T@\"_LAAuthenticationBiometricMethodShim\",R,N
evaluateAccessControl:aksOperation:options:reply:
retain
sensorInaccessible
setExistingContext:
uuid
T@\"NSString\",R,C
authenticatedUser
_keyRef
T@\"BKMatchOperation\",R,N
Tq,N,V_state
deviceWithDescriptor:error:
maxBiometryFailures
recordFromData:
_setServerPropertyForOption:value:log:
setOptionBeginRatchetLocalizedTitle:
currentRatchetWithCompletion:
setOptionCallerAuditTokenUsage:
forEachObserverWithProtocol:selector:invoke:
initWithUUID:token:senderAuditTokenData:context:
setInterruptionHandler:
verifyFileVaultUser:volumeUuid:options:reply:
.cxx_destruct
TB,N,V_isFaceID
coreCredentialOfType:error:
terminate
T@\"NSDictionary\",&,N,V_credentials
T@\"NSString\",R,N,V_uuid
_apConstraints
errorWithDomain:code:userInfo:
evaluatePolicy:options:uiDelegate:reply:
optionCallerAuditToken
optionCountdownLocalizedText
setCredential:type:options:reply:
existingContext
T@\"NSObject<LAContextXPC>\",R,N,V_synchronousRemoteContext
notifyEvent:options:reply:
optionPasswordAuthenticationReason
unlockKeyBagWithError:
_client
set
evaluationMechanismsForPolicy:error:
setOptionSharedValidity:
T@\"LAExtendedRequirement\",R
constraints
credentialOfType:error:
initWithConfiguration:
invalidateWithReply:
_isEnrolled
addCredential:credentialType:
evaluateAccessControl:operation:options:error:
exchangeKeysWithPublicKey:secKeyAlgorithm:secKeyParameters:completion:
isFeatureStrictModeEnabled
T@\"NSData\",R,N
checkEvent:
isAllowed
isExtendedPolicyModeEnabled
release
fetchQueryForGenericPasswordsWithDomain:
fetchKeysWithDomain:completion:
objectForKey:completionHandler:
initWithBlock:
setCredential:forProcessedEvent:credentialType:reply:
T@\"LAEnvironmentState\",R,N
initWithIdentifier:accessKey:privateKeys:secrets:
T@\"LAContext\",R,N,V_authenticationContext
_allowedUsers
_bootstrapServiceType:completion:
_stateHash
decryptData:publicKeyHash:context:completion:
forciblyInvalidate
respondsToSelector:
T@\"<_LAKeyStoreGenericPasswordCryptor>\",W,N,V_cryptor
T@\"BKDevice\",R,N,V__BKDevice
_value
checkStorageOptions:
optionPresentationContext
setOptionFingerMustBeOff:
setSource:
T@\"LAEnvironmentMechanismBiometry\",R,N,V_biometry
allowAllACL
createDefaultQueueWithIdentifier:concurrencyAttribute:
fetchKeyWithIdentifier:domain:completion:
Td,R,N
_resetConnection
enableFeatureStrictModeWithCompletion:
optionPINLength
_invalidateCachedExternalizedContextWithError:
allowedUsers
failProcessedEvent:failureError:reply:
removeAllObjects
isProxy
_coder
_setCredential:type:options:log:cid:error:
classForKey:
environmentStateForUser:completion:
evaluateAccessControl:context:operation:options:presentationContext:reply:
_duration
T@\"LAAuthenticationMethod\",R,N,V_authenticationMethod
checkInternalOperation:options:
_privateKeys
interfaceForXPCProtocol:
permanentError
prearmTouchIDWithReply:
_bootstrapServiceWithAuthenticationPolicy:proxyBlock:completionHandler:
canExchangeKeysUsingSecKeyAlgorithm:
optionMaxBiometryFailures
removeGenericPasswordsWithDomain:completion:
setOptionAuthenticationTitle:
isSensorTrusted
dumpStatusWithCompletion:
evaluateAccessControl:operation:localizedReason:reply:
extractPasswordWithCompletion:
optionBodyText
setOptionMaxCredentialAge:
_optionForRatchetOption:
checkCanEnableFeatureWithCompletion:
evaluateInContext:options:reply:
identitiesWithError:
isEqualToArray:
T@\"LAAuthenticationMethodResult\",R,V_biometricMethodResult
_notifyToken
currentState
evaluatePolicy:options:reply:
isFeatureAvailable
missingImplementation
optionSkipDoublePress
TB,N
_hashWithBundleIdentifier:
_invalidations
_userSession
descriptor
evaluateCorePolicy:options:reply:
setRemoteContext:
_stateLock
credentialOfType:reply:
initWithTag:value:
optionNoGracePeriodUI
setCoreCredential:type:reply:
observers
optionReturnBiometryDatabaseHash
setLocalizedReason:
setObservers:
setOptionPresentingEmbeddedUI:
setTag:
_type
data
setEntitlementsChecker:
setIsStrictModeEnabled:
_synchronousProxyToEnvironmentServiceWithEndpoint:completion:
enableFeatureActivatingGracePeriodWithReply:
setApConstraints:
shim
T@\"NSString\",&,N,V_proxyId
evaluateAccessControl:operation:options:reply:
initWithListenerEndpoint:
optionPasscodeTitle
optionUserCancel
runBiometricOperation
valueWithParameter:error:
T@\"NSHashTable\",&,N,V_observers
T@\"NSData\",&,N,V_externalizedContext
Tq,N,V_approvalState
_pubKeyRef
prearmTouchIdWithReply:
secureDomainStorage
_contextHandler
createPresenceDetectOperationWithError:
isUsable
userCustomCancelErrorWithUserInfo:
acl
optionTKAuthOperationError
resourceNotFoundWithUnderylingError:
setExternalizedContext:
notifyEvent:completionHandler:
setOption:value:
storageErrorWithCode:message:
_autoRetry
_biometricMethodResult
_biometryType
dataForKey:
identifier
setOptionFaceDetectLength:
sharedStore
event:params:reply:
isLockedOut
optionUseModernUI
setProxyId:
credentialCoder
numberForKey:
raise:format:
zone
T@\"NSNumber\",C,N,V_optionRedactErrors
integerValue
optionFallbackToNoAuthentication
optionTimeout
secret
availableDevicesWithFailure:
exchangeData:forKey:error:
saveRight:identifier:secret:completion:
_biometricMethodState
autorelease
evaluatePolicy:options:error:
_proxyId
componentsSeparatedByString:
isEqualToData:
optionCheckApplePayEnabled
serverPropertyForOption:reply:
storeGenericPassword:identifier:domain:protectedBy:completion:
auditToken
connection
genericErrorWithDebugDescription:
resetProcessedEvent:reply:
setFallbackAuthenticationType:
_BKMatchOperation
_right
evaluateRight:localizedReason:reply:
isCredentialSet:
observer
setEvaluatedPolicyDomainState:
synchronousProxyToEnvironmentServiceWithCompletion:
canSignUsingSecKeyAlgorithm:
checkOptions:
description
initWithAccessKey:
optionFaceDetectLength
removeQueryForGenericPasswords
setOptionPINMaxLength:
T@\"NSArray\",R,N,V_allowedUsers
apConstraints
setIsTouchID:
T@\"NSObject<OS_os_log>\",R,N
optionSoftwareUpdateStashMode
whitespaceAndNewlineCharacterSet
T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue
TQ,N,V_lockoutState
createContextWithExternalizedContext:
setOptionCallerIconBundlePath:
setOptionPINLabel:
_performCallBool:finally:
_remoteObjectProxy
_updateState
copy
coreState
distributeBiometricFeedback:
error:hasCode:subcode:
setWithArray:
Tq,R,N,V_domain
authMethodWithReply:
encodeWithACLCoder:
T@\"LAACL\",R,N,V_acl
_performCallId:finally:
setOptionFallbackToNoAuthentication:
synchronousRemoteContext
TB,N,VisStrictModeEnabled
_unregisterDarwinNotification
activate
errorWithCode:message:
setCredential:type:options:error:
_isTouchID
constraintsFromACL:
ratchetErrorForError:
setAuthType:
setOptionMaxBiometryFailures:
userSession
dispatchDelegateSelector:block:
_configuration
class
featureFlagExtractableCredentialProtectionEnabled
evaluateACL:operation:options:uiDelegate:synchronous:reply:
setBool:forKey:error:
setOptionCallerIconPath:
willRetryOnInterruptedConnection
T@\"NSNumber\",R,N,V_userSession
biometricMethodResult
optionMaxCredentialAge
Tq,N,V_biometryType
T@\"LAEnvironmentMechanismUserPassword\",R,N,V_userPassword
optionBeginRatchetLocalizedText
evaluatePolicy:localizedReason:reply:
initWithAutoRetry:avoidUsingFaceIDCamera:allowedUsers:authenticationContext:
appendData:
fetchQueryForKeyWithIdentifier:domain:
serverConnection
state
performSelector:withObject:
storageErrorWithCode:message:suberror:
T#,R
_isAllowed
ratchetState
removeObjectForKey:completionHandler:
storageError:hasCode:
stringByAppendingString:
_observerQueue
accessKey
bootstrapSessionServiceType:serviceClientID:completionHandler:
buildNullGenericPassword
deauthorizeWithCompletion:
matchOperation:providedFaceWUPoseEligibilityInfo:
T@\"LAContext\",R,W,N,V_context
_delegate
stateInContext:completion:
optionPINLabel
removeContextObserver:
setBiometryType:
proxyId
evaluatePolicy:options:uiDelegate:synchronous:reply:
optionAuthenticationTitle
optionPasscodeScreenBlur
optionPresentationStyle
userInfo
_ratchetManager
_isUserPresent
_observer
availableDevices
biometryCurrentSetRequirement
setOptionPhysicalButtonTitle:
authenticationBiometricsMethod:didReceiveFeedback:
biometryType
rightForIdentifier:completion:
serializeACL:
TB,N,V_isUserPresent
TB,V_shouldRecoverConnection
_instanceId
authenticationMethod:didAuthenticateWithResult:
decodeObjectOfClass:forKey:
isCredentialSet:reply:
isSet
enableFeatureWithOptions:reply:
Tq,N,V_fallbackAuthType
_rawValue
hash
setOptionPINFirst:
setCredentials:
T@\"NSXPCConnection\",R,N,V_serverConnection
allowTransferToProcess:receiverAuditTokenData:reply:
numberWithDouble:
optionPhysicalButtonTitle
Td,N
domainState
fetchQueryForGenericPasswordWithIdentifier:domain:
init
isEqualToSet:
initWithState:
logClass:selector:message:
T@\"LAContext\",&,N,V_context
arrayWithArray:
_biometry
beforeFirstUnlockWithUserInfo:
checkCredentialRequiresEncoding:
dictionaryWithDictionary:
fallbackAuthType
numberWithUnsignedInteger:
Tq,R,N,V_type
bootstrapServiceType:completionHandler:
optionUseShortExpirationTimer
supportsSecureCoding
createQueryForGenericPasswordWithIdentifier:domain:data:protectedBy:
setOptionReturnBiometryDatabaseHash:
setOptionUseShortExpirationTimer:
_coreManager
_credentials
_performSynchronous:callId:finally:
isRatchetFeatureEnabled
queue
operation:presenceStateChanged:
T@\"<LAUIDelegate>\",W,N,V_uiDelegate
T@\"LARightStore\",R
canVerifyUsingSecKeyAlgorithm:
fetchQueryForKeysWithDomain:
length
publicKeyHash
context
T@\"NSData\",&,N,V_evaluatedPolicyDomainState
numberForKey:completionHandler:
ratchetResultForResult:
setPermanentError:
_keyStore
initWithTargetUIDRef:
optionNoFailureUI
T@\"LADomainStateBiometry\",R,N,V_biometry
log
T@\"<BKMatchPearlOperationDelegate>\",W,D,N
_optionRedactErrors
allValues
buildNullKey
disableFeatureStrictModeWithContext:completion:
evaluateAccessControl:aksOperation:options:error:
TB,R,N,V_autoRetry
buildBackend
coreCredentialOfType:reply:
dictionaryForKey:completionHandler:
fetchKeyWithPublicKeyHash:completion:
genericErrorWithMessage:
setObject:forKey:completionHandler:
setOptionLightweightUIMode:
addObject:
cachedExternalizedContext
conformsToProtocol:
optionSkipIntentConfirmation
remoteObjectProxyWithErrorHandler:
setOptionPasscodeScreenBlur:
_evaluatePolicy:options:log:cid:error:
_setPermanentError:
initWithData:encoding:
touchIDAuthenticationAllowableReuseDuration
T@\"LACEnvironmentState\",R,N,V_coreState
cryptor
authenticationMethod
setOptionSkipDoublePress:
canEncryptUsingSecKeyAlgorithm:
_evaluatePolicy:options:log:cid:synchronous:reply:
checkPolicy:
date
resourceNotFound
authorizeWithOptions:completion:
automaticallyNotifiesObserversForKey:
notInteractiveErrorWithUserInfo:
setCredential:type:error:
setCurrentState:
setObject:forKey:
TB,R
dealloc
T@\"LAPrivateKey\",R,N
enrolled
enumerateObjectsUsingBlock:
fetchQueryForKeyWithPublicKeyHash:
saveRight:identifier:completion:
T@\"NSString\",R,N,V_identifier
T@\"<LARatchetObserver>\",W,V_observer
T@\"NSData\",R,N,V_stateHash
T@\"LADomainState\",R,N
initWithCoder:
interfaceWithProtocol:
optionFingerMustBeOff
setWillRetryOnInterruptedConnection:
setIsExtendedPolicyModeEnabled:
T@\"NSSet\",R,N
availabilityError
initWithMachServiceName:options:
wrapData:completion:
_optionsForEvent:
optionIgnoreExistingDoublePress
T@\"NSString\",R,N
domainForRightWithIdentifier:
removeItemsWithDomain:completion:
resetRatchetWithReason:completion:
_device
_data
setServerPropertyForOption:value:reply:
T@\"NSData\",&,N,V_existingContext
startWithError:
TI,R
_serverPropertyValueForOption:
checkContextValidWithError:
credentialsUUIDWithReply:
setOptionCallerAuditToken:
performSelector:
initWithExternalizedContext:userSession:flags:
_notifyObserversAboutUpdateFrom:
initWithData:
setOptionIgnoreExistingDoublePress:
_constraint
createDefaultSerialQueueWithIdentifier:
initWithReceiver:
pauseProcessedEvent:pause:reply:
setFallbackAuthType:
setOptionPINMinLength:
setTouchIDAuthenticationAllowableReuseDuration:
value
optionSoftwareUpdateManifest
biometryRefreshableSetRequirementWithFallback:
delegate
localizedFallbackTitle
matchOperation:providedFeedback:
signData:secKeyAlgorithm:completion:
T@\"NSString\",N,R
checkCanAuthorizeWithCompletion:
initWithContextProvider:
isMemberOfClass:
optionCancelVisible
setOptionAuthenticationIdentifier:
_serverPropertyValueForOption:log:
dataForKey:error:
initWithAllowedUsers:authenticationContext:
setOptionPresentationStyle:
setState:
_availableCompanions
_block
contextDidBecomeInvalid:
isAutoEnablement
optionNoCountdownUI
ratchetStateDidChange:
_wrapperKey
compare:
evaluateACL:operation:options:uiDelegate:reply:
optionEventProcessing
T@\"BKMatchPearlOperation\",R,N
_entitlementsChecker
objectForKey:
tokenForTransferToUnknownProcess:
unsignedIntValue
autoEnablementNotAllowedWithUserInfo:
isResourceNotFoundError:
externalizedContextWithError:
addObserver:forKeyPath:options:context:
setOptionAllowEmptyPasscode:
T@\"NSArray\",R,N
UUIDString
_notificationQueue
disableExtendedPolicyProtectionWithContext:completion:
extendedBioLockoutState:forUser:error:
initWithAuthenticatedUser:authenticationMethod:
initWithDelegate:
policyForKey:operation:value:
createConnection:legacyService:
Tq,N,V_tag
_performSynchronous:callBool:finally:
credentials
removeAllRightsWithCompletion:
removeItemsWithCompletion:
_shim
evaluateBoolOption:options:property:
exportBytesWithCompletion:
matchOperation:failedWithReason:
T@\"LACEnvironmentMechanism\",R,N,V_coreMechanism
_lockoutState
_recoverConnectionIfNeeded
_setCredential:type:options:log:cid:reply:
setOptionPasswordAuthenticationReason:
_domain
createMatchOperationWithError:
processInfo
T@\"NSString\",R,N,V_authenticatedUser
setOptionPasscodeScreenStyle:
_accessKey
canEvaluatePolicy:error:
createKeyWithQuery:error:
optionAuthenticationReason
setOptionBeginRatchetShowsLocationWarning:
_flags
enableFeatureWithReply:
genericErrorWithStatus:
allObjects
connectToContextWithUUID:callback:clientId:token:senderAuditTokenData:reply:
initWithACL:
processIdentifier
receiver
setOptionAuthenticationCallbackReason:
setOptionAuthenticationCallbackURL:
initWithResult:
T@\"LASecret\",R,N
T@\"NSMutableArray\",R,N,V_invalidations
setOptionDisableVisionCompanion:
stateWithCompletion:
T@\"LAAuthenticationRequirement\",R
initWithTag:records:
setObject:forKeyedSubscript:
_isCoderAvailable
_wrapperForBKOperation:device:
invalidateWithMessage:
T@\"LADomainStateCompanion\",R,N,V_companion
deviceDescriptorForType:
getDomainStateWithOptions:reply:
mainBundle
_evaluatedPolicyDomainState
authenticationMethod:didStartWithState:
Tq,R,N,V_rawValue
T@\"<LACSecureStorageService>\",R,N,V_remoteObjectProxy
setOptionAllowUnapprovedSensor:
cancelWithReason:completion:
device:matchEventOccurred:
identity
_xpcClient
configuration
optionDisableAutomaticPasscodeFallback
optionSharedValidity
setCoreCredential:type:options:error:
_stateHashForCompanionType
isFaceID
optionCallerName
TB,R,N,V_avoidUsingFaceIDCamera
removeObserver:
Tq,R,N,V_biometryType
_key
armInContext:completion:
defaultRequirement
setData:forKey:completionHandler:
canDecryptUsingSecKeyAlgorithm:
_BKDevice
_constraints
checkCanEvaluateRight:reply:
fetchGenericPasswordWithIdentifier:domain:completion:
optionPresentingEmbeddedUI
T@\"LARatchetStateValue\",R,N,V_value
_running
encryptData:secKeyAlgorithm:completion:
initWithDescriptor:error:
initWithExternalizedContext:userSession:flags:context:
approvalState
armInContext:options:completion:
copyWithZone:
decode:seed:error:
genericErrorWithUnderlyingError:
setOptionUserCancel:
startWithReply:
_performInvalidationBlocks:
numberWithUnsignedInt:
start
_existingContext
availableUsers
setObject:forKey:withOptions:error:
optionAllowEmptyPasscode
optionCallerIconBundlePath
setCoreCredential:type:options:reply:
currentUser
encode
errorWithCode:debugDescription:
T@\"<BKFaceDetectOperationDelegate>\",W,D,N
__BKDevice
disableFeatureWithContext:completion:
errorWithCode:userInfo:
isExtendedPolicyProtectionEnabled
optionDisableMacCompanion
setApprovalState:
authenticationBiometricsMethodDidReceiveNoMatch:
environment:stateDidChangeFromOldState:
initWithGenericPassword:
initWithTimeout:block:
optionsForRatchetArmOptions:
removeQueryForGenericPasswordsWithDomain:
setCredential:type:
weakObjectsHashTable
initWithExternalizedContextRef:
TB,R,N,V_isEnrolled
_createConnectionToDaemon
enumerateKeysAndObjectsUsingBlock:
forwardingTargetForSelector:
isGracePeriodEnabled
observeValueForKeyPath:ofObject:change:context:
stringByAppendingFormat:
TI,R,N,V_instanceId
TQ,R
biometry
setDictionary:forKey:error:
setOptionUseModernUI:
T@\"LABiometryFallbackRequirement\",R
T@\"NSArray\",R,N,V_availableUsers
optionRedactErrors
optionSecurePassphrase
_scheduleRecovery
initNonDisposableWithError:
optionFallbackVisible
setOptionNoFailureUI:
unwrapData:completion:
_credentialCoder
_prearmContext
fetchItemWithQuery:error:
objectAtIndexedSubscript:
remoteContext
optionPushButtonUseMaxPreArmAge
_connectToEndpoint:
decryptData:secKeyAlgorithm:completion:
initWithExternalizedContext:
invoke
removeKeysWithDomain:completion:
setOptionBodyText:
setOptionDisableMacCompanion:
matchOperation:requestedPasscodeShortcutWithReason:
numberWithInteger:
optionBeginRatchetLocalizedTitle
buildKeyStore
checkHasEntitlements:error:
firstObject
optionTransitionStyle
createGenericPasswordWithQuery:error:
device
exchangeKeysWithPublicKey:secKeyAlgorithm:secKeyParameters:context:completion:
optionBiometryLockoutRecoveryRetries
sortedArrayUsingSelector:
_companion
boolForKey:completionHandler:
extractPassword:
operation:finishedWithReason:
performArmRequestWithContext:options:completion:
setOptionFallbackVisible:
T@\"LAEnvironment\",R,N
T@\"LAAuthenticationBiometricMethod\",R,N,V_biometricMethod
T@\"NSArray\",R,N,V_companions
_class:forKey:completionHandler:
connectToExistingContext:callback:clientId:flags:reply:
encode:seed:error:
TB,R,N,V_isAllowed
_identifier
_isDevicePresent
bundleIdentifier
isExtendedPolicyProtectionAvailable
setCoreCredential:type:error:
setOptionBiometryLockoutRecovery:
_isFaceID
encodeWithCoder:
initWithFormat:arguments:
setOptionTintColor:
key
localizedReason
_checkCredentialRequiresExtractionEntitlements:
_serverConnection
dataForKey:completionHandler:
dictionaryWithObjects:forKeys:count:
setOptionCallerName:
_connection
encryptData:publicKeyHash:completion:
setOptionUserFallback:
availableCompanionTypes
enableFeatureWithCompletion:
externalizedContextProvider
optionBeginSecurityDelayImmediately
_availableUsers
_willRetryOnInterruptedConnection
allMechanisms
_serializedInvalidateWithMessage:
createHashForDomainState:
errorWithCode:withUnderlyingErrors:
initWithData:error:
initWithObserver:
invalidate
resume
serverPropertyForOption:error:
_uuid
autoRetry
optionCallerAuditTokenUsage
setOptionBiometryLockoutRecoveryRetries:
devicePasscodeRequirement
newInstanceId
setOptions:forInternalOperation:reply:
biometricMethod
Tq,N,V_lockoutState
T@\"LACContextCredentialCoder\",&,N,V_credentialCoder
isEqualToString:
raiseExceptionOnError:
willChangeValueForKey:
_authenticatedUser
_setTargetUserIdentifier:
defaultSecretIdentifierForRightWithIdentifier:
self
setOptionPasscodeTitle:
_cryptor
initWithIdentifier:
isFeatureSupported
_genps
iconSystemName
unlockKey:inContext:userInfo:completion:
_queue
domainStateWithOptions:
companion
data:
operation:faceDetectStateChanged:
T@\"NSString\",?,R,C
_avoidUsingFaceIDCamera
localizedCancelTitle
matchOperation:presenceDetectedInLockout:
setLocalizedCancelTitle:
setOptionCancelVisible:
T@\"<BKMatchOperationDelegate>\",W,D,N
touchIDAuthenticationRetryLimit
companions
encodeObject:forKey:
setData:forKey:error:
_errorWithCode:userInfo:
addObjectsFromArray:
componentsJoinedByString:
dataWithBytes:length:
enableExtendedPolicyProtectionWithCompletion:
signData:secKeyAlgorithm:context:completion:
archivedDataWithRootObject:requiringSecureCoding:error:
isTouchID
requestAuthorizationForService:completion:
arrayWithObjects:count:
coreMechanism
isStrictModeEnabled
_uidRef
initInternal
optionAuthenticationCallbackReason
setContext:
setServerPropertyForOption:value:error:
__BKOperation
_bootstrapServiceType:completionHandler:
_generateNonce
_observers
setDictionary:forKey:completionHandler:
_approvalState
_genp
_publicErrorFromInternalError:options:
_useModernAuthorizationSheet
armWithOptions:completion:
intValue
setMaxBiometryFailures:
processError:completionHandler:
_userPassword
setBool:forKey:completionHandler:
_xpcConnection
invalidatedWithError:
removeRight:completion:
T@\"BKIdentity\",&,N,V_identity
stashPassword:completion:
initWithRequirement:
initWithTargetUID:
isEnrolled
removeQueryForKeys
setOptionEventProcessing:
T@\"LAAuthenticationMethodConfiguration\",R,N,V_configuration
decryptData:secKeyAlgorithm:context:completion:
invalidateBecauseOfInvalidConnection:
reset
type
customACL:
setOptionPresentationContext:
stringByTrimmingCharactersInSet:
uiDelegate
setUuid:
unsaltedStateHash
T@\"_LABKDevice\",R,N,V_device
setLockoutState:
shouldRecoverConnection
_instanceID
optionAuthenticationIdentifier
setIsUserPresent:
setObject:forKey:options:contextUUID:connection:completionHandler:
setOptionTransitionStyle:
_currentState
biometryRequirementWithFallback:
_resolveUIDelegateFromDelegate:
_callProxyBlock:authenticationPolicy:completionHandler:
biometryNotEnrolledWithUserInfo:
countByEnumeratingWithState:objects:count:
resourceNotFoundWithMessage:
verifyFileVaultUser:volumeUuid:options:error:
T@\"NSNumber\",&,N,V_maxBiometryFailures
_domainStateCache
initWithUIDelegate:
localizedName
setShouldRecoverConnection:
superclass
optionPasscodeScreenStyle
TB,V_willRetryOnInterruptedConnection
initWithCustomPassword:
interactionNotAllowed
setOptionPINCharset:
T@\"LAPublicKey\",R,N
_permanentError
_authenticationMethod
builtInSensorInaccessible
rightContextDidBecomeInvalid
_state
initWithExternalizer:
isFeatureEnabled
setCryptor:
setRemoteObjectInterface:
stateHashForCompanionType:
optionTintColor
T@\"NSXPCConnection\",R,N,V_connection
_authenticationContext
_connectToServerWithRecovery:userSession:legacyService:
_identity
initWithCoreState:
T@\"<LARightContextHandlerDelegate>\",W,N,V_delegate
_biometricMethod
fetchDataWithContext:completion:
setOptionAuthenticationReason:
TB,N,VisExtendedPolicyModeEnabled
authType
synchronousRemoteObjectProxyWithErrorHandler:
initWithRawValue:
publicKey
setOptionNoCountdownUI:
cancelCurrentRatchetWithReason:completion:
setOptionCountdownLocalizedText:
TB,R,N,V_isDevicePresent
applicationRemainsForegroundRequirement
optionUserFallback
T@\"LACEntitlementsChecker\",&,N,V_entitlementsChecker
isDevicePresent
_fetchDomainStateWithOptions:error:
setOptionSecurePassphrase:
_BKFaceDetectOperation
_uiDelegate
code
optionCallerIconPath
passcodeNotSetWithUserInfo:
Tq,N,Vsource
initWithIdentifier:accessKey:
setOptionTimeout:
_updateOptions:
_companions
_handleDarwinNotification
doubleValue
duration
isKindOfClass:
fetchGenericPasswordsWithDomain:completion:
fetchItemsWithDomain:completion:
forEachObserverWithInvoke:
setOptionPINTitle:
storeKeyWithIdentifier:domain:protectedBy:completion:
_initWithBKOperation:device:
createContext
distributeStateChange
right
setOptionTKAuthOperationError:
optionPINCharset
ratchetErrorWithError:
removeQueryForKeysWithDomain:
@\"LARightContextHandler\"
v48@0:8q16^{__SecAccessControl=}24@32@?40
B60@0:8@16q24@32q40I48^@52
v32@0:8@\"BKMatchOperation\"16q24
v24@0:8@16
q16@0:8
v48@0:8@\"NSData\"16@\"NSData\"24@\"LAContext\"32@?<v@?@\"NSData\"@\"NSError\">40
B48@0:8@16q24@32^@40
B36@0:8B16q20^@28
@32@0:8:16@24
v32@0:8@\"NSData\"16@?<v@?@\"<LAKeyStoreKey>\"@\"NSError\">24
@\"<LAUIDelegate>\"
@\"NSObject<LAContextXPC>\"
@\"NSArray\"32@0:8@\"NSDictionary\"16^@24
v44@0:8q16@24B32@?36
@48@0:8^{__SecAccessControl=}16q24@32^@40
q
i
v40@0:8@16^{__CFString=}24@?32
v32@0:8q16@?<v@?@\"NSData\"@\"NSError\">24
B
v32@0:8@\"BKMatchOperation\"16@\"BKMatchResultInfo\"24
v64@0:8@\"NSUUID\"16@\"<LACContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56
@48@0:8@16r^I24q32@40
v32@0:8B16r^I20B28
@20@0:8I16
@\"LAAuthenticationMethodResult\"
@40@0:8:16@24@32
^{__SecAccessControl=}
Q24@0:8@16
@24@0:8@16
@\"LAContext\"
@\"LAEnvironmentServiceXPCClient\"
v32@0:8q16@24
@\"LACEntitlementsChecker\"
@\"LADomainStateCompanion\"
@\"<BKOperationDelegate>\"
@\"LAAccessKey\"
v56@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40@?<v@?@\"<LAKeyStoreGenericPassword>\"@\"NSError\">48
B24@0:8@\"Protocol\"16
v48@0:8@16@24@32@?40
@48@0:8@16@24@32@40
v56@0:8@\"NSData\"16^{__CFString=}24@\"NSDictionary\"32@\"LAContext\"40@?<v@?@\"NSData\"@\"NSError\">48
v32@0:8q16@?<v@?B@\"NSError\">24
v48@0:8@\"NSData\"16q24q32@?<v@?B@\"NSError\">40
v40@0:8@?16q24@?32
@\"BKDevice\"
@\"<LACContext>\"24@0:8@\"NSData\"16
@32@0:8q16^@24
v32@0:8@\"NSError\"16@?<v@?@\"NSError\">24
@\"_LABKDevice\"
v60@0:8@16q24@32q40I48@?52
@\"BKOperation\"
Vv16@0:8
v48@0:8@\"NSData\"16^{__CFString=}24@\"LAContext\"32@?<v@?@\"NSData\"@\"NSError\">40
v32@0:8@16q24
v32@0:8@\"LAAuthenticationBiometricMethod\"16q24
@\"BKDeviceDescriptor\"
v32@0:8@16@?24
@\"NSData\"16@0:8
v24@0:8@?<v@?@\"NSError\">16
v48@0:8@\"NSData\"16@\"NSData\"24^{__CFString=}32@?<v@?@\"NSError\">40
@\"LACEnvironmentMechanism\"
v24@0:8@?<v@?@\"<LAPrearmContextXPC>\"@\"NSError\">16
@40@0:8q16@24@32
B48@0:8@16@24Q32^@40
v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24
@32@0:8q16q24
@\"<LAPrearmContextXPC>\"
@\"LADomainStateBiometry\"
#16@0:8
v24@0:8@?16
@\"<LAKeyStoreBackend>\"
v24@0:8@?<v@?@\"NSUUID\"@\"NSError\">16
v48@0:8@16q24q32@?40
v36@0:8i16@\"NSData\"20@?<v@?B@\"NSError\">28
@\"<LARatchetObserver>\"
@40@0:8q16@24^@32
B24@0:8^{__CFString=}16
@\"NSDictionary\"
v32@0:8r^I16@?24
v40@0:8#16:24@32
d16@0:8
@24@0:8d16
v56@0:8@\"NSData\"16@24@\"NSDictionary\"32@\"<LACContextUIDelegate>\"40@?<v@?@\"NSDictionary\"@\"NSError\">48
@\"LAAuthenticationMethod\"
v40@0:8@\"NSData\"16^{__CFString=}24@?<v@?@\"NSData\"@\"NSError\">32
@\"LAAuthenticationBiometricMethodState\"
B32@0:8@16q24
v24@0:8@\"<LACContext>\"16
v32@0:8@\"LAAuthenticationMethod\"16@\"LAAuthenticationMethodState\"24
v48@0:8^{__SecAccessControl=}16q24@32@?40
@\"NSMutableSet\"
v32@0:8:16@?24
v48@0:8^{__SecAccessControl=}16^v24@32@?40
B40@0:8q16@24^@32
@\"_LAAuthenticationBiometricMethodShim\"
v24@0:8@\"NSCoder\"16
@16@0:8
@\"LAEnvironmentState\"
@\"LAACL\"
v48@0:8@16q24@32@?40
@\"NSMutableDictionary\"
v32@0:8q16@?<v@?@@\"NSError\">24
v24@0:8@\"NSError\"16
@\"NSUUID\"
v24@0:8@\"LAAuthenticationBiometricMethod\"16
d
v32@0:8q16@?24
v40@0:8@16:24@?32
@32@0:8q16@24
@\"LACEnvironmentState\"
@\"LACDTORatchetManager\"
v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24
v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16
v48@0:8q16@\"NSDictionary\"24@\"<LACContextUIDelegate>\"32@?<v@?@\"NSDictionary\"@\"NSError\">40
@\"NSError\"
B32@0:8@\"NSDictionary\"16^@24
@32@0:8@16^I24
@\"LACContextCredentialCoder\"
v32@0:8@16Q24
@\"<LAKeyStore>\"
v56@0:8@16^{__CFString=}24@32@40@?48
v40@0:8q16@24@?<v@?B@\"NSError\">32
v36@0:8B16@?20@?28
@\"NSNumber\"
v48@0:8@16@24^{__CFString=}32@?40
v64@0:8@16q24@32@40@48@?56
@\"LAAuthenticationBiometricMethod\"
v32@0:8@\"LAAuthenticationMethod\"16@\"LAAuthenticationMethodResult\"24
@24@0:8:16
@?
@\"NSArray\"
v48@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32@?<v@?@\"<LAKeyStoreKey>\"@\"NSError\">40
@\"NSData\"
@\"<LAKeyStoreGenericPassword>\"
v36@0:8i16@20@?28
v32@0:8@?16@?24
I16@0:8
@24@0:8^B16
@\"<LACContext>\"16@0:8
v48@0:8@\"NSData\"16q24@\"NSDictionary\"32@?<v@?B@\"NSError\">40
B24@0:8:16
@32@0:8@16@24
@\"LARight\"
v48@0:8@16@24Q32@?40
v36@0:8@16B24@?28
v40@0:8q16@\"NSError\"24@?<v@?B@\"NSError\">32
@\"NSMutableArray\"
@\"NSDictionary\"32@0:8@\"NSDictionary\"16^@24
@40@0:8@16q24^@32
I
v32@0:8@\"BKOperation\"16q24
v28@0:8@\"BKOperation\"16B24
@40@0:8^{__SecAccessControl=}16q24^@32
@\"NSHashTable\"
@40@0:8@16@24@32
v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"<LAKeyStoreGenericPassword>\"@\"NSError\">32
v32@0:8@16@24
@24@0:8q16
v32@0:8@\"BKDevice\"16@\"BKMatchEvent\"24
v24@0:8@\"LAACLCoder\"16
@
v36@0:8q16B24@?28
v24@0:8@\"LAAuthenticationMethod\"16
B24@0:8q16
v40@0:8q16@24q32
Q
v48@0:8@16@24@32@40
@\"LACSExtractablePassword\"
@40@0:8@16r^I24q32
@52@0:8q16@24q32I40^@44
@\"<_LAKeyStoreGenericPasswordCryptor>\"
v56@0:8@\"NSData\"16@\"<LACContextCallbackXPC>\"24Q32q40@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">48
v40@0:8q16@\"NSDictionary\"24@?<v@?B@\"NSError\">32
v48@0:8@\"NSUUID\"16@\"NSUUID\"24Q32@?<v@?B@\"NSError\">40
Q16@0:8
@\"<LARightContextHandlerDelegate>\"
v36@0:8B16q20@?<v@?B@\"NSError\">28
@20@0:8i16
@\"NSObject<OS_dispatch_queue>\"
B16@0:8
v56@0:8@16@24Q32q40@?48
@\"LAEnvironmentMechanismUserPassword\"
@\"LAClient\"
v24@0:8q16
v64@0:8@16@24Q32@40@48@?56
@24@0:8^@16
v40@0:8q16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32
v24@0:8Q16
v32@0:8@\"NSNumber\"16@?<v@?@\"LACEnvironmentState\"@\"NSError\">24
v40@0:8@16@24@?32
@48@0:8^{__SecAccessControl=}16^v24@32^@40
v24@0:8d16
@\"LARatchetStateValue\"
v64@0:8^{__SecAccessControl=}16@24@32q40I48B52@?56
v52@0:8@16B24@28@?36@?44
@\"LAEnvironmentMechanismBiometry\"
v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"<LAKeyStoreKey>\"@\"NSError\">32
v36@0:8q16B24@?<v@?B@\"NSError\">28
q24@0:8q16
@\"<LAKeyStoreKey>\"
@\"LAKeyStoreSecretCoder\"
v40@0:8@16q24@?32
v36@0:8B16q20@?28
@\"NSXPCConnection\"
B36@0:8^q16I24^@28
v32@0:8@\"LAContext\"16@?<v@?@\"NSData\"@\"NSError\">24
v40@0:8q16@24@?32
v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">32
v40@0:8@16q24@?<v@?B@\"NSError\">32
@28@0:8r^I16B24
v24@0:8@?<v@?B@\"NSError\">16
B24@0:8^@16
v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSData\"@\"NSError\">32
v48@0:8@16^{__CFString=}24@32@?40
v64@0:8@\"NSData\"16q24@\"NSDictionary\"32@\"NSUUID\"40@\"NSXPCConnection\"48@?<v@?@@\"NSError\">56
v40@0:8#16q24@?32
v24@0:8@\"LACDTORatchetState\"16
^{_NSZone=}16@0:8
@\"NSString\"
@40@0:8B16B20@24@32
B40@0:8q16@24@32
@\"NSString\"16@0:8
@24@0:8^{_NSZone=}16
B32@0:8@16^@24
v56@0:8q16@24q32I40B44@?48
@\"LAAuthenticationMethodConfiguration\"
v48@0:8@16@24@32^v40
v52@0:8q16@24@32B40@?44
@\"BKIdentity\"
@32@0:8@16^@24
v40@0:8q16@?24@?32
v60@0:8@16@24@32@40B48@?52
@\"LACCacheSync\"
B24@0:8@16
v20@0:8B16
B24@0:8#16
v24@0:8@?<v@?@\"NSData\"@\"NSError\">16
@\"LACExternalizedContextProvider\"
v48@0:8q16@\"NSUUID\"24@\"NSXPCConnection\"32@?<v@?@@\"NSError\">40
B40@0:8@16q24^@32
B32@0:8q16^@24
v28@0:8@16B24
@\"LARatchetManager\"
@24@0:8@?16
v32@0:8@\"NSUUID\"16@?<v@?B@\"NSError\">24
@\"NSData\"24@0:8^@16
@\"<LACSecureStorageService>\"
v16@0:8
{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}
v56@0:8@16@24@32@40@?48
v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24
v48@0:8q16@24@32@?40
@24@0:8@\"NSCoder\"16
```
