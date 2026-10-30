# `/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`

From the upgrade restore ramdisk (141-29011-104.dmg). 817,664 bytes.

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
init()
cup
invalidate called
_LAMKBKeyBagPerformRecovery
-> %@
BKFingerDetectOperation
isAutoEnablement: 
Invalid fetch query %@
LAStorage[%u] bound with %@
kLACServiceTypeEnvironment
duration: %@
LARight[%u]
Cannot perform a key exchange with the given public key.
_LAMKBGetDeviceLockState
iter
-[LAPersistedRight secret]
odel
APLA
com.apple.LocalAuthentication.LARatchetErrorDomain
bkshim
bc
p
Could not encode data
Missing required 'LAOptionAuthenticationReason' option
_LAMKBDeviceUnlockedSinceBoot
rkm
oect
Failed to get externalized context from LAContext
err != nil || key != nil
Lost connection to coreauthd.
No results for query %@
tag
(err=%@)
, 
WaitingForSecondAuthentication
stateHash: %@
v24@?0@\"<LACEnvironmentServiceXPC>\"8@\"NSError\"16
la_client
<...>
@\"NSObject\"24@?0@\"NSObject\"8^@16
LAKeyStore.m
_secrets.count <= 1
MKBGetDeviceLockState
MKBKeyBagPerformRecovery
LAPrivateKey[%u]
wrapping %@ with %@
RetryTime
v40@?0@\"<LAContextXPC>\"8@\"NSUUID\"16@\"NSString\"24@\"NSError\"32
Key with identifier '%@' is already present
Resource not found
com.apple.LocalAuthentication:Authorization:%@
Failed to build key due to missing 'accc'
v16@?0@8
_LAMKBDeviceLockAssertion
error
%@,%d
cag
oa
v16@?0@\"<LAAuthenticationMethodObserver>\"8
-> %d
BKPresenceDetectOperation
pub
Invalid 'ACL' argument.
LAStorage[%u]
com.apple.LocalAuthentication.environment.StateDidChange
_privateKeys.count == 1
NULL
%s
isExtendedPolicyModeEnabled: 
v24@?0@\"LAPersistedRight\"8@\"NSError\"16
v32@?0@\"<LAContextXPC>\"8@\"NSString\"16@\"NSError\"24
MKBKeyBagKeyStashCommit
INF
NO
v24@?0@\"LACEnvironmentState\"8@\"NSError\"16
v24@?0@\"NSData\"8@\"NSError\"16
_LAMKBKeyBagKeyStashCommit
%@,%s
context dealloc
sync
No authentication required.
:
Failed to build key due to missing 'klbl'
mkbshim
v20@?0i8^{__CFDictionary=}12
MKBUnlockDevice
async-starting operation %@
with externalized context %x
LAContextUITrampoline
TKBERTLVRecord
%@:akey
MKBPrewarmSPS
BKDeviceDescriptor
availableCompanions: %@
com.apple.LocalAuthentication
*
kLACServiceTypeSecureStorage
_LAMKBKeyBagKeyStashCreateWithOpts
rawValue: %@
NotStarted
kt
LAEnvironment notification queue
LAPrivateKey
o
v16@?0@\"NSError\"8
i
Expected NSData or NSNumber.
TCCService
pad
pcma
oc
okd
%@ value expected
v24@?0@\"NSXPCListenerEndpoint\"8@\"NSError\"16
_LAMKBKeyBagKeyStashVerify
WaitingForCoolOff
pd
f
rk
cob
LAPersistedRight.m
A
v20@?0B8@\"NSError\"12
BiometryDatabaseHash
@\"LAACLBuilderCustomACLParams\"8@?0
_LAMKBGetDeviceLockStateInfo
The provided data should have between %d and %d bytes
%ds
BKMatchPearlOperation
Invalid uid: %u
biometryType: %@
biometry: %@
v24@?0@\"<LAKeyStoreGenericPassword>\"8@\"NSError\"16
v16@?0@?<v@?@@\"NSError\">8
BKFaceDetectOperation
os
v16@?0q8
-[LAUIDelegateWeakBox event:params:reply:]
Cannot perform operation with invalid context
v24@?0@\"NSNumber\"8@\"NSError\"16
 uiDelegate:%@
Invalid update request.
_state == LARightStateNotAuthorized
-[LARightStore rightForIdentifier:completion:]_block_invoke_2
Failed to build key due to missing public key
-nd
wk
kid
prp
ow
BKMatchOperation
RatchetState
Internal error - unexpected data type
uuid: %@
override
osgn
v12@?0i8
LARightStore.m
err != nil || genps != nil
Could not load secret
acl
Cannot perform operation with nil context
\"
forwarding to BK
LAContext[%u:%@
v24@?0@\"<LACSecureStorageService>\"8@?<v@?@@\"NSError\">16
_LAMKBLockDevice
AvailableMechanisms
v24@?0@\"LACDTORatchetState\"8@\"NSError\"16
sync-starting operation %@
Helper context invalidated
Policy can't be satisfied without UI delegate.
Unable to find class %s
Non-empty localizedReason must be provided.
@\"NSMutableArray\"8@?0
Operation interrupted
com.apple.LocalAuthentication.Storage
-> deviceType:%d, BKDevice=%@
oe
oke
v32@?0@\"NSDictionary\"8Q16^B24
Q8@?0
@\"NSMutableDictionary\"8@?0
#
new
coreauthd_client
isGracePeriodEnabled: 
v32@?0@\"<LAKeyStoreGenericPassword>\"8Q16^B24
-[_LAKeyStore encryptData:publicKeyHash:completion:]_block_invoke_3
Missing Implementation
@\"LACDTOFeatureEnablementOptions\"8@?0
v24@?0@\"<LAKeyStoreKey>\"8@\"NSError\"16
UUID
oecd
Authorization
v32@?0@\"<LAKeyStoreKey>\"8Q16^B24
![wrappedData isEqualToData:cpher]
Invalid data size
LASecret
0`
The right associated with this key was deallocated
TCCServerPrompt
<%@ %p; %@>
_LAMKBGetDeviceConfigurations
MKBKeyBagKeyStashCreateWithOpts
MKBEventsRegister
cpo
LAContext
LASecret[%u]
q
(err:%@)
LARightStore
Failed to build 'genp' due to missing 'labl'
MKBGetDeviceConfigurations
pkofn
LARight.m
v16@?0@?<v@?B@\"NSError\">8
Key creation failed for query %@
_LAMKBPrewarmSPS
bh
-[LAPersistedRight key]
acmh
v32@?0@8@16^B24
Failed to create LAContext
Invalid context.
v32@?0@\"NSMutableArray\"8Q16^B24
_LAMKBEventsRegister_block_invoke
companion: %@
cbio
Required data coder not found
Required data decoder not found
MKBDeviceUnlockedSinceBoot
com.apple.LocalAuthentication.ratchet.StateDidChange
; 
d
Invalid acmContext.
LAEnvironment observer queue
MKBGetDeviceLockStateInfo
Ready
BKDevice
Token
]
async
v24@?0@\"<LAPrearmContextXPC>\"8@\"NSError\"16
This method has been deprecated
isStrictModeEnabled: 
Invalid update value type, expecting dictionary.
Error.LocalAuthentication.coreauthd_client
v24@?0@\"NSArray\"8@\"NSError\"16
BKErrorDomain
Invalid update value type.
-[LARight deauthorizeWithCompletion:]_block_invoke
LAPublicKey
ad
ag
TKTLVRecord
Failed to create XPC connection.
LAPublicKey[%u]
YES
%@,%@
kv
Invalid format
v24@?0@\"NSDictionary\"8@\"NSError\"16
com.apple.CoreAuthentication.daemon.libxpc
_LAMKBEventsUnregister
ckon
err != nil || keys != nil
Collapsed
Nonce
LocalAuthentication_Private.LARatchetFeatureEnablementOptions
ouw
ock
LARight
MKBKeyBagKeyStashVerify
Could not generate nonce
Identifier cannot be empty
Failed to build 'genp' due to missing 'gena'
com.apple.CoreAuthentication.daemon
%d
MKBLockDevice
ed
Ratchet not ready
Invalid operation type.
LAEnvironment work queue
kLAAccessKeyNonce
BiometryType
bid
oece
_LAMKBEventsRegister
v24@?0@8@\"NSError\"16
Failed to build 'genp' due to missing 'r_Data'
The right associated with this secret was deallocated
laabio
_LAMKBUnlockDevice
successfully
%@:genp
Failed to build key due to missing 'labl'
v32@?0@8@16@?<v@?@\"NSError\">24
MKBDeviceLockAssertion
salt
dacl
success
AutoEnablementDenialReason
Failed to build key due to missing 'kref'
Invalid remove query %@
v8@?0
af
<biometricState:touchID=%d,faceID=%d,lockoutState=%08x>
MechanismTree
od
orwk
LARightStore[%u]
MKBEventsUnregister
started: %@
Subcode
oskc
Invalid 'context' argument.
softlink:r:path:/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
softlink:o:path:/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit
softlink:o:path:/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI
softlink:r:path:/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
softlink:r:path:/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit
notifyEvent:%d cid:%u
evaluatePolicy on %{public}@ cid:%u returned %{public}@
evaluationMechanismsForAccessControl:%@ on %{public}@ cid:%u returned %{public}@
setCredential:type:%d options:%{public}@ on %{public}@ cid:%u
setShowingCoachingHint:%d event:%d on %{public}@ cid:%u
Will notify %d observers of changes in %{public}@
%@ updated from %@ to %@
%{public}@ rightForIdentifier finished successfully
exchangeData forKey:%d returned error: %{private}@
Will invoke authentication using policy %d
%s:queue:%@ -> %p
LocalAuthentication.Authorization.verify
LocalAuthentication.Authorization.canExchangeKeys
evaluatePolicy:%d options:%{public}@ on %{public}@ (%{public}s) cid:%u
%{public}@ deallocated
%{public}@ authorizeWithLocalizedReason '%{public}@' started
setObject forKey:%d
%{public}@ sign finished %{public}@
%{public}@ exchangeKeys finished %{public}@
%@ didStartWithState:%@
notifyEvent:%d cid:%u returned %{public}@
%{public}@ created with uuid: %x token: %x
Failed to query environment state for user %u: %@
LocalAuthentication.Authorization.authorizeWithLocalizedReason
LocalAuthentication.Authorization.authorizeWithOptions.completion
evaluationMechanismsForPolicy:%d on %{public}@ cid:%u returned %{public}@
failProcessedEvent:%d failureError:%{public}@ on %{public}@ cid:%u
retryProcessEvent:%d on %{public}@ cid:%u
pauseProcessedEvent:%d on %{public}@ cid:%u returned %{public}@
DomainState on %{public}@ returned: %{public}@
LocalAuthentication.Authorization.removeRightForIdentifier
evaluatePolicy finished with error: %@
%s:options:%@ -> %d
LocalAuthentication.Authorization.encrypt
%{public}@ verify finished %{public}@
%@:%@: %@
%@ didChangeState:%@
resetProcessedEvent:%d on %{public}@ cid:%u returned %{public}@
Failed to obtain environment endpoint %{public}@
%{public}@ rightForIdentifier started
LocalAuthentication.Authorization._saveRight.rightForIdentifier
Invalid authType
unhandled bioevent: %d
objectForKey:%d
setCredential:%d type:%d on %{public}@ cid:%u returned %{public}@ when attempting to encode credential
setServerPropertyForOption:%d value:%{public}@ on %{public}@ cid:%u
%{public}@ rightForIdentifier finished %{public}@
%{public}@ fetchData
setObject forKey:%d returned success
Creating LAContext %{public}@ cid:%u
verifyFileVaultUser:%{public}@ volumeUuid:%{public}@ options:%u on %{public}@ cid:%u
LocalAuthentication.Authorization.getRequirementKey
%{public}@ removeAllRights finished %{public}@
Could not initialize trivial ACL (%{public}@)
Retrying on an interrupted XPC connection
initial evaluatePolicy succeeded
initial evaluatePolicy failed, error: %@
Did reboot successfully
Encountered XPC error on remote proxy: %{private}@
LocalAuthentication.Authorization.authorizeWithOptions
removeObjectForKey:%d returned error: %{private}@
%{public}@ encrypt started
%@ didAuthenticateWithResult:%@
Encoded %{public}@ for transfer with token:%x cid:%u
evaluationMechanismsForPolicy:%d on %{public}@ cid:%u
canEvaluatePolicy:%d on %{public}@ cid:%u
evaluateAccessControl:%{public}@ operation:%{public}@ options:%{public}@ on %{public}@ (%{public}s) cid:%u
LocalAuthentication.Authorization.rightForIdentifier
LocalAuthentication.Authorization.removeAllRights
%{public}@ failed to initialize: %{public}@
Encoding %{public}@ for transfer to pid:%d cid:%u
setOptions:%x forInternalOperation:%d on %{public}@ cid:%u
authMethodWithReply on %{public}@ cid:%u
LACopyResultOfPolicyEvaluation -> %@, %@
LocalAuthentication.Authorization.checkCanAuthorizeWithCompletion
LocalAuthentication.Authorization.fetchData
unknown LAEventParamCoachingFeedback %d received, ignoring
removeObjectForKey:%d
LocalAuthentication.Authorization.canVerify
failProcessedEvent:%d failureError:%{public}@ on %{public}@ cid:%u returned %{public}@
setCredential:forProcessedEvent:%d credentialType:%d on %{public}@ cid:%u returned %{public}@ when attempting to encode credential
Invalidating domain state cache
Could not initialize ACL (flags=%d) (%{public}@)
LocalAuthentication.Authorization.rightForIdentifier.fetchKey
%{public}@ removeRight started
%{public}@ removeAllRights started
%{public}@ _saveRight finished %{public}@
unknown LAEventParamPearlSimpleStatus %d received, ignoring
objectForKey:%d returned success
%s:options:%@ -> %@
evaluatePolicy finished with result: %@
exchangeData forKey:%d
%{public}@ encrypt finished %{public}@
%{public}@ sign started
canEvaluatePolicy:%d on %{public}@ cid:%u returned %{public}@
optionsForInternalOperation:%d on %{public}@ cid:%u returned %{public}@
authMethodWithReply on %{public}@ cid:%u returned %{public}@
verifyFileVaultUser:%{public}@ volumeUuid:%{public}@ on %{public}@ cid:%u returned %{public}@
%{public}@ removeRightForIdentifier started
%{public}@ TCC access request for %@ returned %d
got bio event: %d (%@)
%s:options:%@ stash_mode:%d ACMRef:%@ passcode:%s -> %d
setCredential:forProcessedEvent:%d credentialType:%d on %{public}@ cid:%u returned %{public}@
externalizedContext on %{public}@ cid:%u returned %x
LAEvaluateAndUpdateACL -> %d, %@
xpc_connection_set_target_user_session_uid() setting uid:%{public}@
DomainState on %{public}@
isCredentialSet:%d on %{public}@ cid:%u
setServerPropertyForOption:%d value:%{public}@ on %{public}@ cid:%u returned %{public}@
LACopyResultOfPolicyEvaluation(%@, %d, %@)
LocalAuthentication.Authorization.rightForIdentifier.fetchKeys
%{public}@ saveRight started
%{public}@ _saveRight started
setObject forKey:%d returned error: %{private}@
serverPropertyValueForOption:%d on %{public}@ cid:%u returned %{public}@
Failed to register %{public}s: %u
%{public}@ _saveRight finished successfully
Failed to reboot with error: %{private}@
LocalAuthentication.Authorization.decrypt
LocalAuthentication.Authorization.exchangeKeys
%{public}@ created %{public}@ cid:%u
setCredential:%d type:%d on %{public}@ cid:%u returned %{public}@
credentialOfType:%d on %{public}@ cid:%u
%{public}@ saveRight finished %{public}@
Skipping AP constraints
LocalAuthentication.Authorization.canSign
credentialOfType:%d on %{public}@ cid:%u returned
setShowingCoachingHint:%d event:%d on %{public}@ cid:%u returned %{public}@
LocalAuthentication.Authorization.saveRight
LocalAuthentication.Authorization.removeRight
The right associated with this secret was deallocated
objectForKey:%d returned error: %{private}@
LocalAuthentication.Authorization.sign
%@ init, method=%@
Extracting a LACredentialTypeExtractablePassword will require the '%@' entitlement. The operation will be allowed for now. Error: %{public}@
LocalAuthentication.Authorization.authorizeWithLocalizedReason.completion
%{public}@ invalidated by server: %{public}@
Retrying on externalizedContextProvider
unhandled error for canEvaluate: %@
LocalAuthentication.Authorization.rightForIdentifier.fetchGenericPasswords
unknown LATouchIDSimpleStatus %d received, ignoring
exchangeData forKey:%d returned success
%s:ref:%p
%{public}@ exportBytes finished %{public}@
The right associated with this key was deallocated
Invalid acmContext
LocalAuthentication.Authorization.saveRightWithSecret
removeObjectForKey:%d returned success
%s:secret:%s option:%@ -> %d
credentialOfType:%d on %{public}@ cid:%u returned %{public}@ when attempting to decode credential
LocalAuthentication.Authorization.deauthorizeWithCompletion
%{public}@ authorizeWithOptions finished %{public}@
%{public}@ saveRightWithSecret finished %{public}@
%{public}@ removeRight finished %{public}@
%@ not forwarding %s, receiver is nil
LocalAuthentication.Authorization.canEncrypt
Failed to get transfer token: %{public}@ cid:%u
Stashing a LACredentialTypeExtractablePassword will require the '%@' entitlement. The operation will be allowed for now. Error: %{public}@
LocalAuthentication.Authorization._saveRight.storeGenericPassword
%{public}@ fetchData finished %{public}@
%{public}@ is recovering connection to server
Failed to allow transfer to pid:%d cid:%u: %{public}@
invalidate %{public}@ cid:%u internally returned %{public}@
pauseProcessedEvent:%d pause:%d on %{public}@ cid:%u
serverPropertyValueForOption:%d on %{public}@ cid:%u
%s:callback(type=%d, handle_state=%@
returned biometryType: %d
LAEvaluateAndUpdateACL(%@, %@, %@)
%{public}@ checkCanAuthorizeWithCompletion started
Using real storage
LocalAuthentication.Authorization.canDecrypt
retryProcessEvent:%d on %{public}@ cid:%u returned %{public}@
setCredential:forProcessedEvent:%d credentialType:%d on %{public}@ cid:%u
optionsForInternalOperation:%d on %{public}@ cid:%u
Operation interrupted
%{public}@ removeRightForIdentifier finished %{public}@
LocalAuthentication.Authorization.exportBytes
%{public}@ exportBytes started
Encoded %{public}@ for transfer to pid:%d cid:%u
credentialOfType:%d on %{public}@ cid:%u returned %{public}@
Discrepancy between option %d value (%d) and property value (%d)
%{public}@ target uid: %u
Invalidating %{public}@ cid:%u
resetProcessedEvent:%d on %{public}@ cid:%u
isCredentialSet:%d on %{public}@ cid:%u returned %{public}@
prearmTouchIDWithReply on %{public}@ cid:%u
%{public}@ initialized
%{public}@ checkCanAuthorizeWithCompletion finished %{public}@
%{public}@ verify started
%{public}@ exchangeKeys started
evaluationMechanismsForAccessControl:%@ on %{public}@ cid:%u
resetWithReply on %{public}@ cid:%u
%{public}@ authorizeWithLocalizedReason finished %{public}@
LocalAuthentication.Authorization._saveRight.storeKey
%{public}@ connection to server interrupted (recovery: %d, willRetry: %d)
%{public}@ will keep returning %{public}@ from now on
%s:: -> %d
%s:options:%@ -> %@ (%@)
evaluateAccessControl on %{public}@ cid:%u returned %{public}@
Inconsistent result: both error and credential are valid
%{public}@ saveRightWithSecret started
Could not derive auth constraints (%{public}@)
%{public}@ decrypt started
%{public}@ decrypt finished %{public}@
setOptions:%x forInternalOperation:%d on %{public}@ cid:%u returned %{public}@
prearmTouchIDWithReply on %{public}@ cid:%u returned %{public}@
resetWithReply on %{public}@ cid:%u returned %{public}@
externalizedContext on %{public}@ cid:%u
%{public}@ authorizeWithOptions %{public}@ started
LocalAuthentication.Authorization._saveRight
Could not set ACL protection (%{public}@)
Connecting to %{public}@, flags:%x, uid:%{public}@
%{public}@ invalidated stale XPC connection before creating a new one
%{public}@ has encountered XPC error on synchronous proxy: %{public}@
Created LAStorage
Rebooting for error
xpc_user_sessions_get_foreground_uid() failed with error %d - %s
%s:: -> %@
LAKeyStoreSecretCoder
_LAAuthenticationBiometricMethodShim
LAAuthenticationRequirement
LAExtendedRequirement
LARightContextHandlerDelegate
LAKeyStoreGenericPassword
LAAuthenticationBiometricMethodObserver
_LABKMatchResultInfo
NSObject
LARatchetStateValue
LARatchetStateValueExpired
_LABKFingerDetectOperation
LAStorage
LAExtractablePassword
LACDTORatchetObserver
LARatchetManager
_LAKeyStoreGenericPasswordNull
LASecret
_LAMKBLog
LAEnvironmentServiceXPCClient
_LABKMatchOperation
_LABKFaceDetectOperation
LAACLSerializable
LACustomPasswordRequirement
_LABKDeviceDescriptor
LARatchetStateValueArmed
LACContextProviding
_LAKeyStore
NSCopying
BKDeviceDelegate
NSCoding
LAKeyStoreBackendQueryBuilder
_LABKOperation
LARatchetStateValueNotStarted
LAContext
LAACLCoder
LACContextCallbackXPC
LAAccessKey
_LAKeyStoreKeyNull
LAContextPropertiesProt
LACContextObserver
LAACLBuilderCustomACLParams
LAAuthenticationBiometricMethodState
LAEnvironmentState
LAPublicKey
_LABKDevicePearl
_LABKMatchPearlOperation
LARatchetStateValueWaitingForSecondAuthentication
Authorization
Invalidation
LAContextProvider
LABiometryFallbackRequirement
LARatchet
LARightContextHandler
LARightStore
LAPersistedRight
LAAuthenticationMethodObserver
_LABKDeviceManager
LADomainStateCompanion
LAEnvironmentMechanismCompanion
LAContextEventFeedbackProt
LAEnvironmentMechanismUserPassword
LACEnvironmentServiceXPC
LADomainStateBiometry
_LAKeyStoreKey
LAAuthorizationError
LADomainState
LARight
BKOperationDelegate
LAEnvironment
LAKeyIdentifier
LAKeyStore
LAContextXPC
LACSecureStorageService
LARatchetErrorBuilder
LAAuthenticationMethodResult
_LABKDeviceTouchID
LARatchetStateValueReady
LAClient
LAUIDelegateWeakBox
_LABKDevice
LAACLBuilder
LAAuthenticationBiometricMethodConfiguration
LAPrivateKey
_LABKLog
LAKeyStoreKey
LAContextClientEvaluationProt
LAUIDelegate
LAKeyStoreBackend
LAAuthenticationMethodConfiguration
LARatchetStateValueWaitingForCoolOff
LAKeyStoreItemBuilder
_LAKeyStoreBackendFake
LAAuthenticationMethodState
LARatchetState
_LABKPresenceDetectOperation
LARatchetStateValueCollapsed
LAACL
LADaemonXPC
LAKeyStoreBackendBuilder
LAAuthenticationMethod
LAAuthenticationBiometricMethod
NSSecureCoding
LAKeyStoreBuilder
_LAKeyStoreGenericPassword
LAEnvironmentMechanism
_LAKeyStoreBackendKeychain
BKMatchOperationDelegate
LARatchetFeatureEnablementOptions
_LAKeyStoreGenericPasswordCryptor
LARatchetObserverWrapper
LACContextExternalizingXPC
LACRemoteContext
LAEnvironmentMechanismBiometry
LACContextExternalizing
_serverConnection
biometryCurrentSetRequirementWithFallback:
exportBytesWithCompletion:
checkCredentialRequiresEncoding:
data:
duration
iconSystemName
self
T@\"<BKMatchOperationDelegate>\",W,D,N
beforeFirstUnlockWithUserInfo:
isFeatureEnabled
processInfo
TI,R,N,V_instanceId
_backend
_tag
errorWithCode:message:
evaluatePolicy:options:error:
interactionNotAllowed
localizedCancelTitle
policyForKey:operation:value:
_resolveCombinedStateHash
decodeObjectOfClass:forKey:
fetchQueryForKeyWithIdentifier:domain:
initWithMachServiceName:options:
removeQueryForGenericPasswordsWithDomain:
setServerPropertyForOption:value:reply:
sharedStore
tokenForTransferToUnknownProcess:
_errorWithCode:debugDescription:
apConstraints
setOptionDTO:
T@\"<_LAKeyStoreGenericPasswordCryptor>\",W,N,V_cryptor
T@\"BKOperation\",R,N,V__BKOperation
copy
initWithRequirement:
setSource:
enableFeatureWithOptions:reply:
copyWithZone:
isMemberOfClass:
T@\"LASecret\",R,N
optionPINLength
__BKDevice
_isTouchID
initWithTag:value:
setOptionAllowUnapprovedSensor:
armInContext:completion:
_domain
TQ,N,V_lockoutState
remoteContext
setOptionTimeout:
_notifyObserversAboutUpdateFrom:
_optionsForEvent:
genericErrorWithUnderlyingError:
saveRight:identifier:secret:completion:
setOptionAuthenticationIdentifier:
stateHashForCompanionType:
_updateState
environment:stateDidChangeFromOldState:
setAuthType:
exchangeKeysWithPublicKey:secKeyAlgorithm:secKeyParameters:context:completion:
passcodeNotSetWithUserInfo:
performArmRequestWithContext:options:completion:
credentialEncodingSeedWithReply:
exchangeData:forKey:completionHandler:
optionCallerName
setDictionary:forKey:error:
isResourceNotFoundError:
TB,R,N,V_avoidUsingFaceIDCamera
_keyStore
configuration
secret
setOptionTintColor:
whitespaceAndNewlineCharacterSet
T@\"LARatchetStateValue\",R,N,V_value
_connection
availabilityError
canExchangeKeysUsingSecKeyAlgorithm:
evaluateAccessControl:operation:options:error:
initWithIdentifier:accessKey:privateKeys:secrets:
loadDataWithCompletion:
performSelector:withObject:withObject:
Tq,R,N,V_biometryType
start
userCustomCancelErrorWithUserInfo:
T@\"LAContext\",R,N,V_authenticationContext
_unregisterDarwinNotification
setInvalidationHandler:
setOptionCheckApplePayEnabled:
stateWithCompletion:
T@\"NSSet\",R,N
saveRight:identifier:completion:
contextDidBecomeInvalid:
removeAllObjects
_invalidations
_autoRetry
T@\"<LACSecureStorageService>\",R,N,V_remoteObjectProxy
evaluateAccessControl:aksOperation:options:error:
coreCredentialOfType:reply:
optionEventProcessing
allKeys
conformsToProtocol:
intValue
optionReturnBiometryDatabaseHash
optionSkipIntentConfirmation
setOptionMaxCredentialAge:
T@\"NSNumber\",C,N,V_optionRedactErrors
_acl
boolForKey:completionHandler:
constraintsFromACL:
numberWithInteger:
optionUserCancel
willRetryOnInterruptedConnection
recordFromData:
_optionForRatchetOption:
cancelWithReason:completion:
initWithCoder:
operation:stateChanged:
optionMaxBiometryFailures
setOptionCountdownLocalizedText:
setOptionEventProcessing:
set
T@\"LAAuthenticationRequirement\",R
hash
userInfo
arrayWithArray:
T@\"LAContext\",R,W,N,V_context
_isDevicePresent
enumerateKeysAndObjectsUsingBlock:
optionTimeout
fetchKeysWithDomain:completion:
arrayByAddingObject:
createDefaultSerialQueueWithIdentifier:
_coreMechanism
authenticationMethod
dataForKey:completionHandler:
interfaceWithProtocol:
localizedFallbackTitle
setOptionPasscodeScreenStyle:
setOptions:forInternalOperation:reply:
T@\"LAACL\",R,N,V_acl
.cxx_destruct
containsObject:
objectForKey:completionHandler:
componentsJoinedByString:
setOptionAuthenticationTitle:
T@\"BKIdentity\",&,N,V_identity
Td,N
_synchronousRemoteContext
class
credentialsUUIDWithReply:
mainBundle
setOptionPresentationStyle:
setUiDelegate:
defaultAccessKeyIdentifierForRightWithIdentifier:
encodeWithCoder:
objectForKey:contextUUID:connection:completionHandler:
optionDTO
optionDisableVisionCompanion
serverPropertyForOption:error:
checkACL:
allowAllACL
boolForKey:error:
integerValue
setCryptor:
T@\"NSNumber\",R,N,V_userSession
_observer
initWithCoreState:
optionCallerIconBundlePath
T@\"NSString\",R,N,V_uuid
domain
_device
_biometry
forwardingTargetForSelector:
resetProcessedEvent:reply:
_data
cancelArmRequestWithIdentifier:reason:completion:
device:matchEventOccurred:
stringByAppendingString:
dictionaryWithDictionary:
initWithReceiver:
performSelector:
setIsFaceID:
T@\"NSData\",R,N,V_stateHash
_shouldRecoverConnection
externalizedContextProvider
newInstanceId
queue
setOptionAuthenticationReason:
setOptionCallerIconPath:
state
T@\"NSObject<OS_os_log>\",R,N
UUID
_isAllowed
forEachObserverWithProtocol:selector:invoke:
genericErrorWithMessage:
TB,N,VisExtendedPolicyModeEnabled
_notifyObserversAfterInvalidation
devicePasscodeRequirement
fetchQueryForKeyWithPublicKeyHash:
isExtendedPolicyModeEnabled
authorizeOperation:protectedBy:options:reply:
isFaceID
setOptionNotInteractive:
setTouchIDAuthenticationAllowableReuseDuration:
startWithError:
appendData:
decryptData:publicKeyHash:context:completion:
verifyFileVaultUser:volumeUuid:options:error:
optionIgnoreExistingDoublePress
release
_notificationQueue
canSignUsingSecKeyAlgorithm:
initWithACL:
initWithDomain:authenticationContext:
removeItemsWithCompletion:
sequenceOfRecordsFromData:
evaluationMechanismsForAccessControl:operation:error:
optionBiometryLockoutRecoveryRetries
storageError:hasCode:
Tq,N,V_authType
_currentState
_publicKeyHash
checkContextValidWithError:
extractPassword:
initWithRawValue:value:uuid:
_serverPropertyValueForOption:
setBool:forKey:completionHandler:
setData:forKey:completionHandler:
setDelegate:
setOptionMatchForUnlock:
shouldRecoverConnection
authenticationMethod:didStartWithState:
automaticallyNotifiesObserversForKey:
_rawValue
encode
initWithCoreMechanism:
optionBiometryLockoutRecovery
setOptionFallbackToNoAuthentication:
synchronousRemoteObjectProxyWithErrorHandler:
errorWithCode:debugDescription:
T@\"LAContext\",R,N,V_context
allValues
compare:
objectAtIndexedSubscript:
setCredential:type:options:reply:
_isUserPresent
armWithOptions:completion:
disableFeatureStrictModeWithContext:completion:
evaluatePolicy:options:uiDelegate:reply:
setPermanentError:
optionTintColor
authenticationMethodWillTerminate:
currentUser
fetchItemWithQuery:error:
isEqualToData:
optionNoCountdownUI
raise:format:
_evaluateAccessControl:operation:options:log:cid:synchronous:reply:
_remoteObjectProxy
evaluateAccessControl:operation:localizedReason:reply:
initWithAuthenticatedUser:authenticationMethod:
setOptionDisableAutomaticPasscodeFallback:
touchIDAuthenticationRetryLimit
_willRetryOnInterruptedConnection
biometricMethodState
canEvaluatePolicy:error:
optionUseModernUI
setOptionPINTitle:
_contextHandler
T@\"BKFaceDetectOperation\",R,N
checkHasEntitlements:error:
dataForKey:
fetchGenericPasswordsWithDomain:completion:
_performCallId:finally:
_right
addObserver:
interfaceWithInternalProtocol:
setOptionPresentationContext:
setOptionTKAuthOperationError:
isProxy
_state
setIsUserPresent:
dictionaryWithObjects:forKeys:count:
domainForRightWithIdentifier:
evaluateRight:localizedReason:reply:
evaluationMechanismsForPolicy:error:
resourceNotFound
_bootstrapServiceWithAuthenticationPolicy:proxyBlock:completionHandler:
_stateHash
boolValue
respondsToSelector:
authenticationBiometricsMethodDidReceiveNoMatch:
optionAuthenticationCallbackReason
optionPINTitle
remoteObjectProxy
_credentials
_value
authenticationContext
authenticationMethod:didChangeState:
dumpStatusWithCompletion:
lockedOut
objectForKey:
setOptionTransitionStyle:
setTouchIDAuthenticationRetryLimit:
synchronousRemoteContext
isSensorTrusted
applicationRemainsForegroundRequirement
deviceWithDescriptor:error:
isFeatureAvailable
notifyEvent:options:reply:
setOptionNoCountdownUI:
_coreState
canDecryptUsingSecKeyAlgorithm:
setExternalizedContextProvider:
approvalState
encodeObject:forKey:
setOptionBodyText:
bundleIdentifier
authenticatedUser
coreCredentialOfType:error:
createGenericPasswordWithQuery:error:
optionPasswordAuthenticationReason
removeItemsWithDomain:completion:
T@\"NSArray\",R,N,V_availableUsers
checkCanEvaluateRight:reply:
coreMechanism
_bootstrapServiceType:completion:
_checkIdResultForTCC:synchronous:error:retryBlock:finally:
length
value
_constraints
authorizeWithLocalizedReason:completion:
description
fallbackAuthType
initWithExternalizer:
initWithIdentifier:accessKey:
setCurrentState:
synchronousProxyToEnvironmentServiceWithCompletion:
T@\"NSData\",&,N,V_existingContext
fetchQueryForKeysWithDomain:
initWithTimeout:block:
isAllowed
userPassword
_bootstrapServiceType:completionHandler:
_coreManager
dictionaryForKey:completionHandler:
T@\"NSString\",C,N
_type
fetchQueryForGenericPasswordWithIdentifier:domain:
optionsForInternalOperation:reply:
removeObjectForKey:contextUUID:connection:completionHandler:
setOptionFallbackVisible:
setOptionSoftwareUpdateStashMode:
_scheduleRecovery
optionTransitionStyle
setCoreCredential:type:error:
setIsExtendedPolicyModeEnabled:
encode:seed:error:
T@\"LAAuthenticationMethodConfiguration\",R,N,V_configuration
T@\"NSString\",&,N,V_proxyId
countByEnumeratingWithState:objects:count:
TB,R,N,V_isDevicePresent
_flags
evaluateBoolOption:options:property:
isEqualToString:
notifyEvent:
setOptionReturnBiometryDatabaseHash:
setRemoteContext:
signData:secKeyAlgorithm:completion:
T@\"<BKMatchPearlOperationDelegate>\",W,D,N
optionFallbackVisible
proxyId
initWithData:encoding:
optionSkipDoublePress
canEvaluateCorePolicy:error:
deviceTypeNotSupportedWithUserInfo:
externalizedContext
isUsable
_fallbackAuthType
createDefaultQueueWithIdentifier:concurrencyAttribute:
requestAuthorizationForService:completion:
_publicErrorFromInternalError:options:
runBiometricOperation
verifyFileVaultUser:volumeUuid:options:reply:
T@\"<LARightContextHandlerDelegate>\",W,N,V_delegate
TI,R
T@\"NSHashTable\",&,N,V_observers
TQ,R
_subrequirements
error:hasCode:subcode:
initWithState:
setObject:forKey:withOptions:error:
checkOptions:
wrapData:completion:
setTag:
entitlementsChecker
optionPasscodeScreenStyle
setOptionIgnoreExistingDoublePress:
_maxBiometryFailures
createContext
removeKeysWithDomain:completion:
setState:
_biometryType
_fetchDomainStateWithOptions:error:
_setCredential:type:options:log:cid:error:
authorizeWithOptions:completion:
optionCallerAuditTokenUsage
canEncryptUsingSecKeyAlgorithm:
identitiesWithError:
setOptionPINLabel:
setUuid:
T@\"<BKOperationDelegate>\",W,N,V_delegate
Tq,N,V_tag
initWithFormat:arguments:
setExistingContext:
_permanentError
_descriptor
_instanceID
_client
Tq,R,N,V_type
credentialOfType:error:
errorNotArmedWithRatchetState:
fetchKeyWithPublicKeyHash:completion:
initWithDescriptor:error:
receiver
removeAllRightsWithCompletion:
_BKMatchOperation
buildNullGenericPassword
invoke
isCredentialSet:
optionUseShortExpirationTimer
optionsForRatchetArmOptions:
raiseExceptionOnError:
setLocalizedFallbackTitle:
bootstrapServiceType:completionHandler:
denyAllACL
featureFlagExtractableCredentialProtectionEnabled
setOptionPhysicalButtonTitle:
_BKDevice
_evaluationMechanismsFromReturnedError:error:
bioLockoutState:forUser:error:
bootstrapSessionServiceType:serviceClientID:completionHandler:
coreState
evaluateAccessControl:aksOperation:options:reply:
initWithAvailableUsers:
redactInternalError:
T@\"NSData\",&,N,V_externalizedContext
_availableUsers
T@\"BKMatchOperation\",R,N
T@\"NSDictionary\",&,N,V_apConstraints
_constraint
saltHash:withBundleID:
superclass
_evaluatePolicy:options:log:cid:synchronous:reply:
_generateNonce
boolForKey:
currentRatchetWithCompletion:
objectForKeyedSubscript:
setRight:
T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue
setOptionFaceDetectLength:
_biometricMethod
createQueryForKeyWithIdentifier:domain:acl:
decryptData:secKeyAlgorithm:completion:
isExtendedPolicyProtectionEnabled
optionTKAuthOperationError
storeKeyWithIdentifier:domain:protectedBy:completion:
allowTransferToProcess:receiverAuditTokenData:reply:
setApprovalState:
setMaxBiometryFailures:
_decodeCredential:type:reply:
_isFaceID
_registerDarwinNotification
isFeatureSupported
setFallbackAuthenticationType:
setOptionBiometryLockoutRecoveryRetries:
T@\"LADomainState\",R,N
_initWithBKOperation:device:
connectToExistingContext:callback:clientId:flags:reply:
dictionaryForKey:
right
setObject:forKey:completionHandler:
setOptionDisableVisionCompanion:
checkStorageOptions:
stringByAppendingFormat:
T@\"LAExtendedRequirement\",R
buildBackend
enableFeatureStrictModeWithCompletion:
setOptionUserCancel:
_uuid
failProcessedEvent:failureError:reply:
invalidatedWithError:
T@\"LAAuthenticationMethodResult\",R,V_biometricMethodResult
Td,R,N
enableFeatureWithCompletion:
_authType
credentialOfType:reply:
setOptionAuthenticationCallbackURL:
stringByTrimmingCharactersInSet:
T@\"LADomainStateCompanion\",R,N,V_companion
externalizedContextWithError:
matchOperation:providedFaceWUPoseEligibilityInfo:
optionCheckApplePayEnabled
optionPushButtonUseMaxPreArmAge
initWithCustomPassword:
_nullCharacterData
archivedDataWithRootObject:requiringSecureCoding:error:
accessKey
biometryType
getDomainStateWithOptions:synchronous:reply:
isEqualToDictionary:
optionAuthenticationIdentifier
setApConstraints:
setFallbackAuthType:
setOptionCallerIconBundlePath:
T#,R
log
startWithReply:
T@\"LAPrivateKey\",R,N
T@\"NSMutableArray\",R,N,V_invalidations
initWithAccessKey:
lockoutState
setOptionLightweightUI:
_configuration
publicKeyHash
T@\"LACContextCredentialCoder\",&,N,V_credentialCoder
optionNoFailureUI
optionSoftwareUpdateStashMode
setOptionAllowEmptyPasscode:
setOptionCallerAuditTokenUsage:
authenticationBiometricsMethod:didReceiveFeedback:
isAutoEnablementAllowed:
initNonDisposableWithError:
optionAuthenticationReason
ratchetErrorWithError:
setShouldRecoverConnection:
isKindOfClass:
setWithArray:
willChangeValueForKey:
T@\"LAAuthenticationMethod\",R,N,V_authenticationMethod
TB,R,N,V_isAllowed
_isEnrolled
evaluateAccessControl:operation:options:reply:
optionBodyText
setOptionFingerMustBeOff:
_biometricMethodResult
_password
_userPassword
rawValue
buildKeyStore
code
connection
evaluateACL:operation:options:reply:
isEqual:
optionPasscodeScreenBlur
TB,N,V_isUserPresent
_shim
deauthorizeWithCompletion:
forEachObserverWithInvoke:
invalidateWithReply:
setBool:forKey:error:
tag
_wrappedData
notInteractiveErrorWithUserInfo:
setData:forKey:error:
setOptionUseModernUI:
cryptor
_secrets
error:hasCode:
setOptionNoGracePeriodUI:
_performSynchronous:callId:finally:
evaluatedPolicyDomainState
T@\"NSNumber\",&,N,V_maxBiometryFailures
touchIDAuthenticationAllowableReuseDuration
Tq,N,V_biometryType
_handleConnectionResult:uuid:proxyId:error:
enableFeatureActivatingGracePeriodWithReply:
matchOperation:presenceDetectedInLockout:
setOptionBiometryLockoutRecovery:
identity
setShowingCoachingHint:event:reply:
T@\"LACEnvironmentState\",R,N,V_coreState
T@\"LAAuthenticationBiometricMethodState\",R,V_biometricMethodState
setCredentials:
_hashWithBundleIdentifier:
_remoteContext
addConstraint:
setObservers:
T@\"LAAuthenticationBiometricMethodState\",&,N,V_currentState
autoRetry
observer
optionCallerAuditToken
resume
credentialCoder
TB,R,N
initWithKey:
_identity
biometry
builtInSensorInaccessible
setCoreCredential:type:reply:
setOptionMaxBiometryFailures:
optionAuthenticationCallbackURL
_notifyToken
_setCredential:type:options:log:cid:reply:
unsaltedStateHash
T@\"<LAUIDelegate>\",W,N
_invalidateCachedExternalizedContextWithError:
mutableCopy
setOptionPINCharset:
_performCallBool:finally:
classForKey:
initWithExternalizedContext:
initWithIdentifier:
matchOperation:requestedPasscodeShortcutWithReason:
missingImplementation
ratchetResultForResult:
setOptionCallerName:
optionBeginRatchetLocalizedText
disableExtendedPolicyProtectionWithContext:completion:
distributeStateChange
initWithUIDelegate:
setOptionPresentingEmbeddedUI:
userSession
_authenticatedUser
_context
T@\"LAEnvironmentMechanismBiometry\",R,N,V_biometry
T@\"NSArray\",R,N,V_allowedUsers
TB,R,N,V_autoRetry
arrayWithObjects:count:
cancelCurrentRatchetWithReason:completion:
initWithDuration:
setInterruptionHandler:
setOptionLightweightUIMode:
_xpcConnection
_duration
T@\"_LABKDevice\",R,N,V_device
currentState
initWithAllowedUsers:authenticationContext:
setInteractionNotAllowed:
sortedArrayUsingSelector:
createQueryForGenericPasswordWithIdentifier:domain:data:protectedBy:
encodeWithACLCoder:
initWithTag:records:
isUserPresent
_availableCompanions
T@\"LAEnvironmentState\",R,N
localizedReason
numberForKey:completionHandler:
_updateStateWithSynchronousProxyToEnvironmentService:
autoEnablementNotAllowedWithUserInfo:
optionSecurePassphrase
optionSharedValidity
acl
_performInvalidationBlocks:
isAutoEnablement
setOptionNoFailureUI:
source
stateInContext:completion:
didChangeValueForKey:
_evaluatePolicy:options:log:cid:error:
_keys
T@\"BKMatchPearlOperation\",R,N
T@\"LAClient\",R,N,V_client
T@\"NSString\",?,R,C
supportsSecureCoding
_allowedUsers
interfaceForXPCProtocol:
setCredentialCoder:
setObject:forKey:
allMechanisms
optionPINMaxLength
setOptionSoftwareUpdateManifest:
_synchronousRemoteObjectProxy:performCall:
enableFeatureWithReply:
isExtendedPolicyProtectionAvailable
setEntitlementsChecker:
companion
companionType
customPasswordRequirement:
pauseProcessedEvent:pause:reply:
rightForIdentifier:completion:
_observerQueue
device
releaseUIDelegate
buildNullKey
canVerifyUsingSecKeyAlgorithm:
setCredential:type:error:
T@\"<BKFaceDetectOperationDelegate>\",W,D,N
_genp
addObject:
biometricMethodResult
errorWithCode:userInfo:
identifier
T@\"NSUUID\",&,N,V_uuid
Tq,N,V_fallbackAuthType
availableCompanionTypes
setLockoutState:
descriptor
evaluateInContext:options:reply:
optionFingerMustBeOff
resetRatchetWithReason:completion:
setExternalizedContext:
setOptionCancelVisible:
setOptionPushButtonUseMaxPreArmAge:
setOptionSkipIntentConfirmation:
Tq,R,N
isEqualToSet:
optionPresentationStyle
serializeACL:
T@\"LAPublicKey\",R,N
_externalizedContext
_privateKeys
initInternal
optionMatchForUnlock
permanentError
setOptionCallerPID:
setCoreCredential:type:options:error:
distributeBiometricFeedback:
evaluateACL:operation:options:uiDelegate:synchronous:reply:
initWithExternalizedContext:userSession:flags:
removeObjectForKey:completionHandler:
setCredentialsUUID:reply:
setOptionCallerAuditToken:
T@\"NSData\",&,N,V_evaluatedPolicyDomainState
_accessKey
T@\"NSObject<LAContextXPC>\",&,N,V_remoteContext
T@\"LACEnvironmentMechanism\",R,N,V_coreMechanism
_biometricMethodState
optionFallbackToNoAuthentication
prearmTouchIDWithReply:
reset
ratchetStateDidChange:
storeGenericPassword:identifier:domain:protectedBy:completion:
initWithExternalizedContextRef:
T@\"<LAUIDelegate>\",W,N,V_uiDelegate
_authenticationMethod
terminate
numberWithBool:
T@\"NSString\",R,N
_evaluatePolicy:options:synchronous:reply:
addObjectsFromArray:
prearmTouchIdWithReply:
T@\"NSData\",R,N
setCredential:type:
sharedInstance
Tq,N,V_approvalState
errorWithDomain:code:userInfo:
invalidateBecauseOfInvalidConnection:
isStrictModeEnabled
optionLightweightUIMode
optionUserFallback
setServerPropertyForOption:value:error:
isEqualToArray:
availableUsers
fetchGenericPasswordWithIdentifier:domain:completion:
initWithExternalizedContext:userSession:
instanceId
optionPasscodeTitle
remoteObjectProxyWithErrorHandler:
TB,V_shouldRecoverConnection
_serverPropertyValueForOption:log:
optionSoftwareUpdateManifest
array
client
componentsSeparatedByString:
numberWithDouble:
publicKey
setOptionUserFallback:
stashPassword:completion:
storageErrorWithCode:message:
UUIDString
firstObject
invalidate
matchOperation:matchedWithResult:
setOptionBeginRatchetLocalizedTitle:
setOptionPINMaxLength:
operation:presenceStateChanged:
serverPropertyForOption:reply:
_uidRef
T@\"NSError\",&,V_permanentError
_authenticationContext
deviceDescriptorForType:
genericErrorWithDebugDescription:
initWithBlock:
initWithRawValue:
lockoutStateFromError:
_observers
credentials
disableFeatureWithContext:completion:
evaluateACL:operation:options:uiDelegate:reply:
isLockedOut
optionFaceDetectLength
removeRightForIdentifier:completion:
auditToken
Tq,R,N,V_domain
addCredential:credentialType:
allowedUsers
initWithTargetUIDRef:
setOptionSkipDoublePress:
TB,R
decryptData:secKeyAlgorithm:context:completion:
domainState
initWithUUID:token:senderAuditTokenData:context:
requirementByAddingExtendedRequirement:
resourceNotFoundWithUnderylingError:
retryProcessedEvent:reply:
_companion
availableDevicesWithFailure:
checkCanEnableFeatureWithCompletion:
decode:seed:error:
delegate
existingContext
TB,N
biometryRefreshableSetRequirementWithFallback:
dataWithBytes:length:
initWithConfiguration:
operation:faceDetectStateChanged:
T@\"_LAAuthenticationBiometricMethodShim\",R,N,V_shim
_proxyId
dataUsingEncoding:
null
secureDomainStorage
evaluatePolicy:options:uiDelegate:synchronous:reply:
optionAuthenticationTitle
dataForKey:error:
enableExtendedPolicyProtectionWithCompletion:
initWithDelegate:
T@\"NSDictionary\",R,N
checkCredentialType:
createPresenceDetectOperationWithError:
initWithTargetUID:
removeContextObserver:
setObject:forKey:options:contextUUID:connection:completionHandler:
setOptionPINFirst:
_keyRef
T@\"LABiometryFallbackRequirement\",R
Tq,N,V_lockoutState
_apConstraints
_isCoderAvailable
optionPINCharset
dealloc
T@\"NSNumber\",&,N
_updateOptions:
authMethodWithReply:
date
performSelector:withObject:
_domainStateCache
_setQueue:
TB,N,V_isFaceID
_coder
availableDevices
logClass:selector:message:
biometricMethod
customACL:
optionBeginSecurityDelayImmediately
_checkCredentialRequiresExtractionEntitlements:
T@\"LAAuthenticationBiometricMethod\",R,N,V_biometricMethod
deserializeACL:
T@\"LACExternalizedContextProvider\",&,V_externalizedContextProvider
_setPermanentError:
_stateLock
isSet
removeItemsWithQuery:error:
resourceNotFoundWithMessage:
T@\"BKDeviceDescriptor\",R,N,V_descriptor
_synchronousProxyToEnvironmentServiceWithEndpoint:completion:
removeObserver:forKeyPath:
setCredential:type:options:error:
setOptionAuthenticationCallbackReason:
T@\"_LAAuthenticationBiometricMethodShim\",R,N
fetchQueryForGenericPasswordsWithDomain:
isFeatureStrictModeEnabled
setCredential:type:reply:
autorelease
localizedName
_resetConnection
ratchetErrorForError:
stringWithFormat:
cachedExternalizedContext
initWithSource:
addEntriesFromDictionary:
companions
processIdentifier
setCoreCredential:type:options:reply:
setOptionPasswordAuthenticationReason:
exchangeData:forKey:error:
forciblyInvalidate
ratchetState
retainCount
setRemoteObjectInterface:
_createConnectionToDaemon
numberForKey:error:
setDictionary:forKey:completionHandler:
_companions
evaluateAccessControl:context:operation:options:presentationContext:reply:
optionNoGracePeriodUI
setOptionPasscodeTitle:
Tq,N,Vsource
biometryNotEnrolledWithUserInfo:
createHashForDomainState:
setIsStrictModeEnabled:
waitForStateUpdate
optionCallerPID
genericErrorWithStatus:
initWithAutoRetry:avoidUsingFaceIDCamera:allowedUsers:authenticationContext:
optionBeginRatchetShowsLocationWarning
setQueue:
context
Tq,N,V_state
_recoverConnectionIfNeeded
activate
domainStateWithOptions:
optionPhysicalButtonTitle
removeQueryForKeys
setObject:forKey:withOptions:completionHandler:
_delegate
optionAllowUnapprovedSensor
optionPresentingEmbeddedUI
stashPassword:error:
T@\"LAEnvironmentMechanismUserPassword\",R,N,V_userPassword
_genps
constraints
isCredentialSet:reply:
isRatchetFeatureEnabled
numberWithUnsignedInt:
setCredential:forProcessedEvent:credentialType:reply:
setOptionPINLength:
avoidUsingFaceIDCamera
TB,N,VisGracePeriodEnabled
_entitlementsChecker
_setServerPropertyForOption:value:
connectToContextWithUUID:callback:clientId:token:senderAuditTokenData:reply:
initWithGenericPassword:
optionBeginRatchetLocalizedTitle
TB,N,VisAutoEnablement
_performSynchronous:callBool:finally:
_serializedInvalidateWithMessage:
unsignedIntValue
_BKFaceDetectOperation
_stateHashForCompanionType
allObjects
extendedBioLockoutState:forUser:error:
optionDisableAutomaticPasscodeFallback
resetWithReply:
encryptData:secKeyAlgorithm:completion:
invalidations
setOptionDisableMacCompanion:
createConnection:legacyService:
T@\"NSString\",R,C
T@\"NSString\",R,N,V_identifier
setIsGracePeriodEnabled:
_workQueue
TB,R,N,V_isEnrolled
T@\"NSArray\",R,N,V_companions
_connectToEndpoint:
createMatchOperationWithError:
setIsAutoEnablement:
T@\"NSDictionary\",&,N,V_credentials
T@\"NSString\",N,R
initWithData:error:
setLocalizedCancelTitle:
T@\"LAContext\",&,N,V_context
addContextObserver:
initWithExternalizedContext:uiDelegate:
weakObjectsHashTable
_externalizedContextProvider
_setServerPropertyForOption:value:log:
_userSession
authenticationMethod:didAuthenticateWithResult:
fetchItemsWithQuery:error:
serverConnection
storageErrorWithCode:message:suberror:
T@\"LARatchetState\",R,N
setEvaluatedPolicyDomainState:
setOptionBeginRatchetLocalizedText:
setProxyId:
processError:completionHandler:
_key
checkCanAuthorizeWithCompletion:
T@\"LAEnvironment\",R,N
T@\"BKDevice\",R,N,V__BKDevice
Tq,R,N,V_rawValue
evaluateCorePolicy:options:reply:
externalizedContextWithReply:
notifyEvent:completionHandler:
optionPresentationContext
removeObject:
checkPolicy:
evaluatePolicy:localizedReason:reply:
shim
valueWithParameter:error:
verifyData:signature:secKeyAlgorithm:completion:
operation:finishedWithReason:
removeRight:completion:
setOptionPasscodeScreenBlur:
T@\"NSXPCConnection\",R,N,V_serverConnection
_setTargetUserIdentifier:
optionPINMinLength
_encodeCredential:type:reply:
_pubKeyRef
count
createContextWithExternalizedContext:
environmentStateForUser:completion:
optionCountdownLocalizedText
type
zone
_approvalState
_credentialCoder
buildWithDictionary:error:
evaluatePolicy:options:reply:
event:params:reply:
setOptionPINMinLength:
stateHash
uiDelegate
T@\"NSObject<LAContextXPC>\",R,N,V_synchronousRemoteContext
debugDescription
initWithObserver:
matchOperation:providedFaceOcclusionInfo:
setAuthenticationType:
setIsTouchID:
setLocalizedReason:
exchangeKeysWithPublicKey:secKeyAlgorithm:secKeyParameters:completion:
evaluateCorePolicy:options:error:
isEnrolled
matchOperation:failedWithReason:
optionMaxCredentialAge
setBiometryType:
T@\"NSString\",R,N,V_authenticatedUser
dictionaryForKey:error:
doubleValue
fetchKeyWithIdentifier:domain:completion:
setOptionBeginRatchetShowsLocationWarning:
uuid
fetchItemsWithDomain:completion:
optionDisableMacCompanion
setOptionUseShortExpirationTimer:
_wrapperKey
initWithData:
defaultRequirement
encryptData:publicKeyHash:completion:
retain
setOptionBeginSecurityDelayImmediately:
initWithResult:
isDevicePresent
T@\"NSXPCConnection\",R,N,V_connection
extractPasswordWithCompletion:
removeGenericPasswordsWithDomain:completion:
_BKOperation
_useModernAuthorizationSheet
biometryRequirementWithFallback:
sensorInaccessible
unlockKey:inContext:userInfo:completion:
initWithContextProvider:
optionCancelVisible
setWillRetryOnInterruptedConnection:
_uiDelegate
checkEvent:
initWithListenerEndpoint:
isTouchID
nextInstanceIDInDomain:
setOptionSecurePassphrase:
unlockKeyBagWithError:
_identifier
_xpcClient
errorWithCode:withUnderlyingErrors:
optionLightweightUI
T@\"LACEntitlementsChecker\",&,N,V_entitlementsChecker
_instanceId
unwrapData:completion:
dispatchDelegateSelector:block:
init
optionPINLabel
signData:secKeyAlgorithm:context:completion:
_connectToServerWithRecovery:userSession:legacyService:
_lockoutState
enrolled
getDomainStateWithOptions:reply:
_optionRedactErrors
armInContext:options:completion:
TB,N,V_isTouchID
__BKOperation
T@\"<LARatchetObserver>\",W,V_observer
_resolveUIDelegateFromDelegate:
T@\"LARightStore\",R
_handleDarwinNotification
_wrapperForBKOperation:device:
T@\"LADomainStateBiometry\",R,N,V_biometry
_existingContext
_queue
defaultSecretIdentifierForRightWithIdentifier:
isGracePeriodEnabled
optionPINFirst
numberForKey:
setObserver:
numberWithUnsignedInteger:
_ratchetManager
_class:forKey:completionHandler:
newCommandId
setObject:forKeyedSubscript:
T@\"NSArray\",R,N
matchOperation:providedFeedback:
setContext:
_running
removeQueryForGenericPasswords
removeQueryForKeysWithDomain:
rightContextDidBecomeInvalid
key
TB,N,VisStrictModeEnabled
_BKMatchPearlOperation
_cryptor
_errorWithCode:userInfo:
enumerateObjectsUsingBlock:
invalidateWithMessage:
observeValueForKeyPath:ofObject:change:context:
_evaluatedPolicyDomainState
_prearmContext
_callProxyBlock:authenticationPolicy:completionHandler:
biometryRequirement
initWithExternalizedContext:userSession:flags:context:
optionAllowEmptyPasscode
optionCallerIconPath
optionRedactErrors
TB,V_willRetryOnInterruptedConnection
_avoidUsingFaceIDCamera
authType
observers
setOptionSharedValidity:
removeObserver:
createKeyWithQuery:error:
data
fetchDataWithContext:completion:
maxBiometryFailures
optionNotInteractive
setIdentity:
setOptionRedactErrors:
checkInternalOperation:options:
_block
addObserver:forKeyPath:options:context:
biometryCurrentSetRequirement
setOption:value:
B24@0:8@16
v32@0:8@\"LAAuthenticationMethod\"16@\"LAAuthenticationMethodState\"24
@\"NSMutableSet\"
@\"NSArray\"
@24@0:8^{_NSZone=}16
v36@0:8B16q20@?28
B36@0:8B16q20^@28
I
@\"BKDeviceDescriptor\"
v48@0:8@\"NSData\"16^{__CFString=}24@\"LAContext\"32@?<v@?@\"NSData\"@\"NSError\">40
v48@0:8@16q24q32@?40
B40@0:8q16@24^@32
B
v28@0:8@16B24
@\"LADomainStateCompanion\"
q24@0:8q16
@\"<LAKeyStoreGenericPassword>\"
v64@0:8@16@24Q32@40@48@?56
v24@0:8@\"<LACContext>\"16
@\"<LAKeyStore>\"
v36@0:8q16B24@?28
@48@0:8@16r^I24q32@40
@20@0:8I16
v32@0:8@\"BKMatchOperation\"16@\"BKMatchResultInfo\"24
@\"LACEnvironmentMechanism\"
v24@0:8d16
@\"NSString\"16@0:8
v32@0:8@\"NSData\"16@?<v@?@\"<LAKeyStoreKey>\"@\"NSError\">24
v24@0:8@?<v@?B@\"NSError\">16
v32@0:8@?16@?24
@\"<BKOperationDelegate>\"
v48@0:8^{__SecAccessControl=}16^v24@32@?40
@32@0:8q16q24
@\"LACEntitlementsChecker\"
@\"LAEnvironmentState\"
v40@0:8@\"NSData\"16^{__CFString=}24@?<v@?@\"NSData\"@\"NSError\">32
@\"LAAuthenticationBiometricMethodState\"
d
v56@0:8@16@24@32@40@?48
@\"LARight\"
v64@0:8@\"NSUUID\"16@\"<LACContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56
v24@0:8@?<v@?@\"<LAPrearmContextXPC>\"@\"NSError\">16
v32@0:8@\"BKMatchOperation\"16q24
@40@0:8q16@24^@32
v48@0:8@16@24Q32@?40
@\"LACDTORatchetManager\"
v48@0:8@16^{__CFString=}24@32@?40
@\"<_LAKeyStoreGenericPasswordCryptor>\"
B40@0:8q16@24@32
^{_NSZone=}16@0:8
@32@0:8@16@24
q16@0:8
v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"<LAKeyStoreKey>\"@\"NSError\">32
@24@0:8^@16
v40@0:8@16:24@?32
v32@0:8@\"LAAuthenticationBiometricMethod\"16q24
@40@0:8:16@24@32
v56@0:8@16^{__CFString=}24@32@40@?48
@\"NSError\"
@24@0:8@\"NSCoder\"16
v40@0:8q16@24q32
@24@0:8d16
#16@0:8
v48@0:8@16@24@32@?40
@48@0:8@16@24@32@40
@?
@20@0:8i16
v32@0:8@\"NSError\"16@?<v@?@\"NSError\">24
@24@0:8:16
v48@0:8@\"NSData\"16q24q32@?<v@?B@\"NSError\">40
@\"<LAPrearmContextXPC>\"
@\"NSString\"
@\"<LAKeyStoreBackend>\"
@24@0:8@?16
v32@0:8@\"NSUUID\"16@?<v@?B@\"NSError\">24
@\"NSObject<LAContextXPC>\"
d16@0:8
B32@0:8@16q24
^{__SecAccessControl=}
@\"NSUUID\"
@48@0:8^{__SecAccessControl=}16^v24@32^@40
v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">32
v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16
@32@0:8q16^@24
@\"NSObject<OS_dispatch_queue>\"
v40@0:8q16@24@?<v@?B@\"NSError\">32
@16@0:8
v24@0:8@16
v36@0:8@16B24@?28
B32@0:8@\"NSDictionary\"16^@24
@\"NSArray\"32@0:8@\"NSDictionary\"16^@24
B40@0:8@16q24^@32
@24@0:8q16
v32@0:8q16@?<v@?B@\"NSError\">24
Q24@0:8@16
Vv16@0:8
Q
v48@0:8@\"NSData\"16@\"NSData\"24@\"LAContext\"32@?<v@?@\"NSData\"@\"NSError\">40
v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24
v32@0:8@16q24
v48@0:8q16@\"NSUUID\"24@\"NSXPCConnection\"32@?<v@?@@\"NSError\">40
@28@0:8r^I16B24
v32@0:8@\"LAAuthenticationMethod\"16@\"LAAuthenticationMethodResult\"24
@\"<LACSecureStorageService>\"
v56@0:8q16@24q32I40B44@?48
v32@0:8@16@?24
v56@0:8@\"NSData\"16@24@\"NSDictionary\"32@\"<LACContextUIDelegate>\"40@?<v@?@\"NSDictionary\"@\"NSError\">48
@\"LAAuthenticationBiometricMethod\"
v48@0:8^{__SecAccessControl=}16q24@32@?40
v16@0:8
@\"BKOperation\"
v24@0:8@\"NSCoder\"16
v40@0:8@16^{__CFString=}24@?32
v28@0:8@\"BKOperation\"16B24
B60@0:8@16q24@32q40I48^@52
Q16@0:8
@\"NSDictionary\"
v32@0:8@16Q24
B16@0:8
@\"LARatchetManager\"
@\"LAACL\"
v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24
@40@0:8q16@24@32
v44@0:8q16@24B32@?36
v48@0:8q16^{__SecAccessControl=}24@32@?40
v40@0:8@16q24@?32
@\"LAAuthenticationMethodResult\"
B24@0:8^{__CFString=}16
v36@0:8B16@?20@?28
v32@0:8@\"BKDevice\"16@\"BKMatchEvent\"24
@\"_LABKDevice\"
v32@0:8q16@24
v48@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32@?<v@?@\"<LAKeyStoreKey>\"@\"NSError\">40
v36@0:8q16B24@?<v@?B@\"NSError\">28
@40@0:8@16r^I24q32
v24@0:8@\"LAACLCoder\"16
v36@0:8i16@20@?28
@\"NSXPCConnection\"
v24@0:8@\"LAAuthenticationMethod\"16
@\"BKDevice\"
@\"LACCacheSync\"
B24@0:8@\"Protocol\"16
v32@0:8q16@?<v@?@\"NSData\"@\"NSError\">24
v36@0:8B16q20@?<v@?B@\"NSError\">28
v52@0:8q16@24@32B40@?44
v24@0:8Q16
@24@0:8@16
@32@0:8:16@24
v24@0:8@?<v@?@\"NSError\">16
v40@0:8q16@\"NSDictionary\"24@?<v@?B@\"NSError\">32
v52@0:8@16B24@28@?36@?44
v48@0:8@\"NSUUID\"16@\"NSUUID\"24Q32@?<v@?B@\"NSError\">40
@40@0:8@16q24^@32
v48@0:8@16@24@32^v40
v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"<LAKeyStoreGenericPassword>\"@\"NSError\">32
v32@0:8@\"LAContext\"16@?<v@?@\"NSData\"@\"NSError\">24
v36@0:8i16@\"NSData\"20@?<v@?B@\"NSError\">28
@\"LACExternalizedContextProvider\"
B32@0:8@16^@24
@\"LARatchetStateValue\"
@40@0:8^{__SecAccessControl=}16q24^@32
v60@0:8@16q24@32q40I48@?52
B24@0:8^@16
@\"NSNumber\"
B48@0:8@16q24@32^@40
@\"LARightContextHandler\"
v48@0:8@16@24^{__CFString=}32@?40
@\"NSDictionary\"32@0:8@\"NSDictionary\"16^@24
@\"LAEnvironmentMechanismUserPassword\"
v32@0:8q16@?24
v64@0:8@\"NSData\"16q24@\"NSDictionary\"32@\"NSUUID\"40@\"NSXPCConnection\"48@?<v@?@@\"NSError\">56
B24@0:8q16
@24@0:8^B16
v32@0:8q16@?<v@?@@\"NSError\">24
v48@0:8@\"NSData\"16q24@\"NSDictionary\"32@?<v@?B@\"NSError\">40
@\"<LAUIDelegate>\"
@\"BKIdentity\"
@32@0:8@16^I24
v48@0:8@\"NSData\"16@\"NSData\"24^{__CFString=}32@?<v@?@\"NSError\">40
v60@0:8@16@24@32@40B48@?52
v40@0:8q16@?24@?32
@\"LAKeyStoreSecretCoder\"
@\"_LAAuthenticationBiometricMethodShim\"
B24@0:8#16
v40@0:8q16@24@?32
v24@0:8@?<v@?@\"NSUUID\"@\"NSError\">16
v20@0:8B16
@\"LAClient\"
@\"<LACContext>\"16@0:8
@\"<LARightContextHandlerDelegate>\"
v56@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40@?<v@?@\"<LAKeyStoreGenericPassword>\"@\"NSError\">48
v24@0:8@?<v@?@\"NSData\"@\"NSError\">16
v56@0:8@\"NSData\"16^{__CFString=}24@\"NSDictionary\"32@\"LAContext\"40@?<v@?@\"NSData\"@\"NSError\">48
@
v32@0:8r^I16@?24
@48@0:8^{__SecAccessControl=}16q24@32^@40
v64@0:8@16q24@32@40@48@?56
@\"LAContext\"
v56@0:8@\"NSData\"16@\"<LACContextCallbackXPC>\"24Q32q40@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">48
v48@0:8q16@\"NSDictionary\"24@\"<LACContextUIDelegate>\"32@?<v@?@\"NSDictionary\"@\"NSError\">40
v32@0:8:16@?24
@40@0:8@16@24@32
v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24
v40@0:8@?16q24@?32
q
v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSData\"@\"NSError\">32
@\"NSData\"
@\"LAAuthenticationMethod\"
v32@0:8@16@24
@\"NSHashTable\"
v24@0:8@\"LACDTORatchetState\"16
@\"LADomainStateBiometry\"
@\"LACSExtractablePassword\"
@\"<LACContext>\"24@0:8@\"NSData\"16
@32@0:8@16^@24
v56@0:8@16@24Q32q40@?48
v48@0:8q16@24@32@?40
v24@0:8@\"NSError\"16
B32@0:8q16^@24
@\"LACContextCredentialCoder\"
v48@0:8@16q24@32@?40
v40@0:8q16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32
@\"<LAKeyStoreKey>\"
v32@0:8B16r^I20B28
B24@0:8:16
@\"LAAccessKey\"
@\"NSMutableDictionary\"
v48@0:8@16@24@32@40
I16@0:8
B36@0:8^q16I24^@28
v32@0:8@\"BKOperation\"16q24
@32@0:8q16@24
v40@0:8#16:24@32
v40@0:8@16@24@?32
@\"LAEnvironmentServiceXPCClient\"
@\"NSData\"16@0:8
v40@0:8#16q24@?32
@\"LAEnvironmentMechanismBiometry\"
@\"LACEnvironmentState\"
v24@0:8@?16
v40@0:8@16q24@?<v@?B@\"NSError\">32
@\"NSData\"24@0:8^@16
v32@0:8@\"NSNumber\"16@?<v@?@\"LACEnvironmentState\"@\"NSError\">24
v64@0:8^{__SecAccessControl=}16@24@32q40I48B52@?56
{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}
@\"NSMutableArray\"
v24@0:8@\"LAAuthenticationBiometricMethod\"16
@\"<LARatchetObserver>\"
@52@0:8q16@24q32I40^@44
v24@0:8q16
v40@0:8q16@\"NSError\"24@?<v@?B@\"NSError\">32
B48@0:8@16@24Q32^@40
i
@\"LAAuthenticationMethodConfiguration\"
@40@0:8B16B20@24@32
```
