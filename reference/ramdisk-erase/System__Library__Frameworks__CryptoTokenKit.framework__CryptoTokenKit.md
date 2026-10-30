# `/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,098,448 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 39 (Size: 5968)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe, NlistOutofsyncWithDyldinfo
```

## Linked libraries (21)

- `/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit (compatibility version 0.0.0, current version 878.40.5)`
- `/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore (compatibility version 0.0.0, current version 0.0.0)`
- `/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication (compatibility version 1.0.0, current version 2319.42.1)`
- `/System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/CoreServices.framework/CoreServices (compatibility version 1.0.0, current version 1226.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking (compatibility version 1.0.0, current version 72.0.0)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0, weak)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0, weak)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2, weak)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswift_Concurrency.dylib (compatibility version 0.0.0, current version 0.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (100 classes, 38 protocols)

Classes: `NSError`, `TKAKSParameters`, `TKAPDUCommandAnalyzer`, `TKAPDUFormatter`, `TKAPDULogComponents`, `TKAnalytics`, `TKApplicationProxy`, `TKAsyncOperation`, `TKAuthContext`, `TKBERTLVRecord`, `TKCTKDConnection`, `TKClientToken`, `TKClientTokenAdvertisedItem`, `TKClientTokenObject`, `TKClientTokenSession`, `TKCompactTLVRecord`, `TKDataConverter`, `TKDataSource`, `TKExtensionClientToken`, `TKExtensionClientTokenObject`, `TKExtensionClientTokenSession`, `TKLocalSEPKey`, `TKLocalSEPRefKey`, `TKLocalSEPSystemKey`, `TKMLDSAPrehasher`, `TKPowerMonitor`, `TKRegisteredTokenManager`, `TKRemoteSEPKey`, `TKSEPClientToken`, `TKSEPClientTokenObject`, `TKSEPClientTokenSession`, `TKSEPKey`, `TKSharedResource`, `TKSharedResourceSlot`, `TKSimpleTLVRecord`, `TKSlotParameters`, `TKSmartCard`, `TKSmartCardATR`, `TKSmartCardATRInterfaceGroup`, `TKSmartCardPINFormat`, `TKSmartCardSessionEngine`, `TKSmartCardSessionRequest`, `TKSmartCardSlot`, `TKSmartCardSlotEngine`, `TKSmartCardSlotManager`, `TKSmartCardSlotNFCSession`, `TKSmartCardSlotProxy`, `TKSmartCardSlotScreen`, `TKSmartCardStateRequest`, `TKSmartCardToken`, `TKSmartCardTokenDriver`, `TKSmartCardTokenRegistrationManager`, `TKSmartCardTokenRegistrationXPCClient`, `TKSmartCardTokenSession`, `TKSmartCardUserInteraction`, `TKSmartCardUserInteractionForConfirmation`, `TKSmartCardUserInteractionForPINOperation`, `TKSmartCardUserInteractionForSecurePINChange`, `TKSmartCardUserInteractionForSecurePINVerification`, `TKSmartCardUserInteractionForStringEntry`, `TKSmartCardWithError`, `TKTLVRecord`, `TKToken`, `TKTokenAccessDBBackedByUserDefaults`, `TKTokenAccessRegistry`, `TKTokenAccessRequest`, `TKTokenAccessUserPromptInfo`, `TKTokenAccessUserPromptNoop`, `TKTokenAccessUserPromptRemoteAlertSB`, `TKTokenAuthOperation`, `TKTokenBaseContext`, `TKTokenConfiguration`, `TKTokenConfigurationConnection`, `TKTokenConfigurationConnectionProxy`, `TKTokenConfigurationTransaction`, `TKTokenConnection`, `TKTokenDriver`, `TKTokenDriverConfiguration`, `TKTokenDriverContext`, `TKTokenDriverRequest`, `TKTokenID`, `TKTokenKeyAlgorithm`, `TKTokenKeyExchangeParameters`, `TKTokenKeychainCertificate`, `TKTokenKeychainContents`, `TKTokenKeychainItem`, `TKTokenKeychainKey`, `TKTokenPasswordAuthOperation`, `TKTokenService_Subsystem`, `TKTokenSession`, `TKTokenSessionConnection`, `TKTokenSmartCardPINAuthOperation`, `TKTokenWatcher`, `TKTokenWatcherProxy`, `TKTokenWatcherTokenInfo`, `TKXPCConnectionConfigurationDefault`, `TKXPCConnectionDefault`, `TKXPCInterface`, `TLVDebugUtility`, `_TKSmartCardSlotReservation`

Protocols: `LAProtocolEndpointProviderServer`, `NSCoding`, `NSCopying`, `NSExtensionRequestHandling`, `NSObject`, `NSSecureCoding`, `NSXPCListenerDelegate`, `PKModularService`, `SBSRemoteAlertHandleObserver`, `TKClientTokenProtocol`, `TKClientTokenServerProtocol`, `TKProtocolSlot`, `TKProtocolSlotClient`, `TKProtocolSlotClientNotification`, `TKProtocolSlotNotification`, `TKProtocolSlotRegistry`, `TKProtocolSmartCardSession`, `TKProtocolSmartCardSlot`, `TKProtocolSmartCardSlotNotification`, `TKProtocolTokenWatcherHost`, `TKProtocolTokenWatcherServer`, `TKRemoteSEPKeyProtocol`, `TKSmartCardSlotNFCManaging`, `TKSmartCardTokenRegistrationXPC`, `TKSmartCardTokenRegistrationXPCClient`, `TKTokenAccessDB`, `TKTokenAccessUserPrompt`, `TKTokenConfigurationChangeProtocol`, `TKTokenConfigurationProtocol`, `TKTokenDelegate`, `TKTokenDriverDelegate`, `TKTokenDriverHostProtocol`, `TKTokenDriverProtocol`, `TKTokenSessionDelegate`, `TKUIServerProtocol`, `TKXPCConnection`, `TKXPCConnectionConfiguration`, `TKXPCConnectionDelegate`

## Strings (2,983)

First 2,500 of 2,983.
```
bad endSession
VERIFY
LoginWindow
com.apple.ctk.aid
v16@?0@\"NSString\"8
gsmak
@24@?0@\"<TKClientTokenServerProtocol>\"8^@16
Received message for unexpected alert handle
LibCall_BuildCommand
SIGN_DATA
ACMContextCreateWithExternalForm
pubk
Facial
acm_mem_free_info
ACMRequirement - ACMRequirementDataKofN
 %@
T=?
@\"TKXPCConnectionDefault\"8@?0
com.apple.ctk.pmon
com.apple.scslot:%@
Only TKLocalSEPKey instances can be attested
userSecretTriesLeft
[AUTH]
UPDATE BIN
Retired14
%s must be overriden
SBSRemoteAlertHandle
com.apple.sear.SampleToken
Retired20
ACMRequirement - ACMRequirementDataPasscodeValidated
<%@ %@ %p>
\n
initialTimeout
pka_p256
OCC2
com.apple.ctk.first-slot
LibCall_ACMContextCreateWithExternalForm
!
v8@?0
v16@?0@\"NSData\"8
keychain-access-groups
q
ACMRequirement - ACMRequirementDataPasscodeValidatedWithAttributes
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c
com.apple.LocalAuthentication
oik-c
verifyAclConstraintForOperationCommandInternal
maxPINLength
currentPINByteOffset
p384
Retired13
ACMRequirement
v16@?0@\"TKAsyncOperation\"8
systemSessionKey
    securePINChangeSupported: %d\n
kyber768
IDLE
com.apple.ctk.driver-class
com.apple.CryptoTokenKit
    delegateWithEscapeMethod: %d\n}\n
v32@?0@\"NSNumber\"8@\"_TKSmartCardSlotReservation\"16^B24
unable to bump/commit key
com.apple.ctkd.slot-registry
%s: %s: called.\n
ACMRequirement - ACMRequirementDataAccessGroups
unsuitable key for attesting
AKSError
Util_DeallocRequirement
AppleCredentialManager
v24@?0@\"NSData\"8@\"NSError\"16
EndpointProvider
TKSmartCard.m
locale
haven-c
ACMRequirement - ACMRequirementDataRatchet
ACMContextRemovePassphraseCredentialsByPurposeAndScope
extension %@: cannot instantiate TKTokenDriver-based class '%@' (%p)
PINLengthBitOffset
Bad or missing kSecKeyEncryptionParameterRecryptCertificate
Concurrent remote alerts are not yet supported
[%lu bytes]
com.apple.ctk.class-id
+[TKTLVRecord parseFromDataSource:nestingLevel:]
Slot already exists and you are not authorized to receive the TKSmartCardSlotNFCSession
v16@?0q8
    maxOutputLength: %ld\n
    displayMaxLines: %@ \n
mlkem768
<sepk:%@ kid=%016llx>
@32@?0@\"<TKClientTokenProtocol>\"8q16^@24
keySize
[DATA]
v16@?0@\"NSXPCListenerEndpoint\"8
sensitive
v24@?0@\"TKToken\"8@\"NSError\"16
<TKSmartCardSlot: %p '%@'>
0x%02X
prevstate
ACMRequirementGetProperty
avoidInitialKeepAlive
v32@?0@\"<TKProtocolSmartCardSession>\"8@\"NSDictionary\"16@\"NSError\"24
ACTIVE
kTKTokenAccessUserPromptInfo
oecd
installation:%@
v24@?0@\"NSObject<OS_os_log>\"8r*16
BSAuditToken
@\"NSDictionary\"8@?0
%@: %@
@\"NSString\"8@?0
denied
Retired17
Couldn't read \"com.apple.developer.nfc.readersession.iso7816 .select-identifiers\" record in Info.plist
{\n    maxInputLength: %ld\n
PIN
    vendorID: %@\n
false
commit
[PUK+PIN:%lu bytes]
Retired1
 (blocked)
ACMRequirement - ACMRequirementDataSecureIntent
Token plugins are not supported without PlugInKit
VERIFY_TRY_LEFT
publicKey
REGISTERED_SMARTCARD_NFC_PROMPT_MESSAGE
Built-in NFC Slot
-[TKSEPKey accessControl]
@16@?0@8
com.apple.private.ctk.token-access.allow
[%02lX:%lu]
v32@?0@8@16^B24
granted
token driver does not implement any way to create new slot-based token instances
Card is missing
attesteeSystemSession
v32@?0@\"TKSmartCardSessionRequest\"8Q16^B24
@\"LAContext\"16@?0^@8
v24@?0@8@\"NSError\"16
...
SMCertSigner
\xf0a1
*
EMPTY
smartCardSlotNFCSession.%@
ioKitTransport
    productID: %@\n
XPC connection to TKSmartCardTokenRegistrationXPC could not be created
GEN AUTH
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c
/System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
    minPINLength: %@\n
nonce
acmh
kClientDisplayName
sync
PINCompletion
:
%@:%@
TKSmartCardSlotEngine.m
(u)
GET RESP
CHUID
Missing TKSmartCardSlotEngineDelegate delegate
TKLocalSEPKey.m
authenticationContextProvidedBySecCaller
KeyMgmt
resourceslot:%@
read data
com.apple.ctk.slottype
protocol
v24@?0B8B12@\"NSError\"16
UNKNOWN!%d(%d)
 %02lX
SBSRemoteAlertPresentationTarget
com.apple
Iris
sharedrsc
kCorrelationID
ACMRequirement - ACMRequirementDataOr
ACMLib
odel
keyType
[ACCESSKEY]
 (%d more)
com.apple.CryptoTokenKit.analytics
LAContext/ACMHandle temporary default slot
{
pka_p384
@24@?0@\"<TKRemoteSEPKeyProtocol>\"8^@16
User denied access
SmartCard returned error %04hx
(d)
PairingCode
ACMRequirement - ACMRequirementDataPushButtonWithAttributes
AID
Global
EP-provided
com.apple.private.ctk.virtual-token
v24@?0@\"NSXPCListenerEndpoint\"8@\"NSError\"16
v20@?0B8@\"NSError\"12
CardAuth
-[TKSEPKey objectID]
v32@?0@8@\"NSNumber\"16^B24
INS %02X
%02X %02X %02X %02X
CFBundleDisplayName
 
Retired11
 (%d tries)
com.apple.ctk.consoleUserOnly
AIDs must be provided in Info.plist
KeyHistory
 (wrong len)
sign data
-[TKSEPKey systemSessionKey]
LAContext.externalizedContext failed
Retired10
TKTokenSession.m
apduQueue
com.apple.CryptoTokenKit.apduOperationQueue
tokenID
dak-c
ECCompactable
com.apple.ctkd.watcher-started
ACMRequirement - ACMRequirementDataSecureStateWithAttributes
interactionTimeout
curve25519
TKUITokenAccessPromptVC
    pinValidationCondition: %@ \n
v24@?0@\"NSNumber\"8@\"NSError\"16
Access request was cancelled
power
APDU
APDULog
oko
systemKey
OCC1
Fingerprints
LibCall_ACMContextDelete
yyyyMMddHHmmss.SSSS'Z'
ACMRequirement - ACMRequirementDataKeyRef
oect
%@,%@
com.apple.developer.nfc.readersession.iso7816.select-identifiers
Mismatch in active state notifications count
client
Bad kSecKeyEncryptionParameterSymmetricKeySizeInBits - if present, must be set to 128 for both input and output crypto operation
-
com.apple.ctkd.slot-client
T=15
[MGMT]
Discovery
v16@?0@\"NSError\"8
%s must not be called
token_access_registry
    displayMaxCharacters: %@\n
T=1
fik
send(ins:p1:p2:data:le:)
unable to sign digest
CCC
name
%s: %s: returning, err = %ld.\n
bad tag value for TKCompactTLVRecord (%u)
TKRemoteSEPKey.m
[----]
<AKSp:
attestation
Retired6
LAPolicyTokenAuthentication did not fill in LAResultTKAuthOperation
Access request timed out
PIVAuth
 (targetUID=%d)
NULL
PINJustification
T=0
i
Expecting key, but provided certificate objectID
}
Operation not supported in this platform
READ BIN
Retired5
Retired18
<%@ %@ %@ %p o=%@>
/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
sendIns: not in active card session
PINBlockByteLength
com.apple.scpwr:%@
user_prompt
v32@?0@\"NSXPCListenerEndpoint\"8@\"NSString\"16@\"NSError\"24
%02x
Attempt to send APDU with Le=%@
Q
session:%@
Unexpected TKTokenDriverRequest context type
Unsupported smart card protocol 0x%04lx
T=%d:
RESET RETRY
DigSig
[%@:%lu]
v16@?0@\"NSDictionary\"8
v28@?0@\"NSData\"8S16@\"NSError\"20
Requested system key not supported by the platform
v16@?0@\"TKCTKDConnection\"8
remove-objects
value for TKSimpleTLVRecord record too big (%lu)
    securePINVerificationSupported: %d\n
smartcard
sepkey
uik-c
Retired12
    firmwareVersion: %@\n
u_TokenSession
ACMRequirement - ACMRequirementDataAnd
com.apple.SecurityAgent
oa
%@ 0x%llx=%@
xpc
p256
unable to delete key
sik
SmartCard driver created token not inherited from TKSmartCardToken class (token %@)
kProviderDisplayName
YES
idleTimeout
com.apple.ctkd.slot-server-started
INVALID_PIN
result
okd
<TKSmartCardATR: %p %02x
com.apple.CoreAuthentication.daemon.EndpointProvider
mlkem1024
v24@?0@\"NSDictionary\"8@\"NSError\"16
Unexpected result: %@
[CRYPT]
ACM
ACMHandleWithPayload
missing virtual token entitlement
PINConfirmation
failed to serialize objectID '%@'
tokencfg
failed to get DER-encoded aks_params_t (err=%d)
oik-p
root
###
cag
unable to attest key
i8@?0
Retired19
 (not found)
Attempt to import incompatible %@ into %@
BioInfo
@\"NSXPCConnection\"8@?0
PINLengthBitSize
CHANGE REF
ACMRequirement - ACMRequirementDataBiometryMatchAttempted
corrupted objectID detected
dak-p
;
CFBundleVisibleComponentName
ACMRequirement - ACMRequirementDataKofNWithAttributes
Invalid argument ptr
unknown
PINByteOffset
INT AUTH
ECDH1
Retired4
init
od
%@<%d>
v24@?0@\"TKTokenSession\"8@?<v@?>16
<tkid:%@>
%@
override should be called
%s: %s: mem: type=%s ptr=%p size=%u (total=%u raw=%u data=%u types=%u) %s:%d (%s).\n
v16@?0@\"NSArray\"8
@\"TKCTKDConnection\"16@?0^@8
Security
invalid objectOperation %d on token %@
ACMRequirement - ACMRequirementDataBiometryMatched
ACMRequirement - ACMRequirementDataUserOutputDisplayed
token
v16@?0r^{__ACMRequirement=}8
unable to generate key
tkid
<%@: %@>
share
serializeParameters
verifyAclConstraintInternal
1
application-identifier
unable to get public key
%s: %s: returning.\n
com.apple.AppSSOAgent
DisabledTokens
    interactionTimeout: %f\n
unable to compute shared secret
v32@?0@\"NSData\"8@\"NSDictionary\"16@\"NSError\"24
isFinished
An attempt to reference nonexistent session %@ on token %@
performCommand
ctkd did not set configurationEndpoint
[
(s)
sdak-c
<%@: %p> algorithms: %@
v24@?0@\"TKTokenAuthOperation\"8@\"NSError\"16
Double-commit of transaction
Destroying uncommited transaction
com.apple.private.playgrounds-local-signing-allowed
SBSRemoteAlertDefinition
atr
ACMRequirement - ACMRequirementDataBiometryMatchedWithAttributes
 %02x
PrintedInfo
isExecuting
ed25519
kyber1024
updateLogLevelFromKext
-[TKSEPKey keyType]
unable to attest refkey->refkey
dcik
ENVELOPE
 (OK)
 (wrong P1/P2)
READ_DATA
<data>
Detected duplicate objectID for key %@ and certificate %@. This is allowed only for token extensions built for macOS 10.16 or newer. Either change build options to target newer OS version or avoid sharing same objectID for key and certifica
unable to decapsulate shared key
CryptoTokenKit
 (conditions not satisfied)
v12@?0i8
Unable to select card application AID %@
<empty>
PIV
Retired3
acl
BER-TLV tag number must not be 0
v32@?0@\"<NSObject>\"8@\"<NSObject>\"16^B24
%s%x(%@)
Scan your registered smartcard for %@
SBSRemoteAlertPresentationTargetPredicate
Attempt to send APDU with Lc=%lu
    maxPINLength: %@\n
com.apple.keystore.sik.access
sepkey: %@ requires '%@' value when present
gid
com.apple.ctkui
GEN KEY
state
endpolicy
acm_mem_alloc_info
osgn
beginSessionQueue
v24@?0r^v8Q16
sdak-p
Retired8
newPINByteOffset
[OLD+NEW-PIN:%lu bytes]
watcher
HasSEP
<sepk:%s%s kid=%016llx>
ADMIN
v16@?0@\"LAContext\"8
unable to recrypt
B16@?0^@8
Retired15
 Le=%@
ock
com.apple.security.smartcard
-[TKSEPKey keySize]
accessControl
TKRemoteSEPKey-serverConnection
MAILBOX
installation:
>
com.apple.keystore.access-keychain-keys
rsepkey
PreloadedTokens
NSExtensionAttributes
TKTokenAccessUserPromptRemoteAlertSB.m
com.apple.ctk.token-type
token driver does not implement any way to create new token instances
Attempt to read beyond data bounds
@24@?0@\"<TKClientTokenProtocol>\"8^@16
SBSRemoteAlertConfigurationContext
com.apple.ctkbind-notification
SW=%04X
com.apple.ctk.proprietaryCardUsage
B32@?0@\"TKTLVRecord\"8Q16^B24
@16@?0^@8
Received user response for an unexpected request
PUT DATA
ACMRequirement - ACMRequirementDataPushButton
minPINLength
true
objectID contains invalid refkey data
DECRYPT_DATA
ACMRequirement - ACMRequirementDataAP
PINBitOffset
<%@: %@ '%@'>
Retired16
<malformed response>
SELECT
Retired2
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c
<malformed APDU>
com.apple.authorizationhost
ord
+[TKTLVRecord parseFromDataSource:]
com.apple.ctkd.access-db
Reinsertion simulation is currently running or was run recently. Please wait at least %f seconds between the calls.
Unexpected aks_key_type %d
callerPID
BSProcessHandle
external
TKToken.m
v24@?0i8B12r^{__ACMRequirement=}16
objectID contains invalid key type
TKTokenConnection.m
]
haven-p
 (security)
Util_AllocRequirement
objectID of unexpected type
Detected duplicate objectID for objects %@ and %@
com.apple.CryptoTokenKit.APDU
ECDH2
Retired9
keyUsage
TKClientToken.m
[%@-PIN:%lu bytes]
Retired7
ACMRequirement - ACMRequirementDataPassphraseEntered
,
attempt to perform attestation with mixed local/remote keys
GET DATA
appproxy
v16@?0@8
attempt to transmitRequest out of card session
NO
System
com.apple.ctkd.smartcardregistration-client
server-start-notify-q
async
PINFormat
operation
forceSystemSession
SBSRemoteAlertActivationContext
Invalid tokenID format: %@
value for TKCompactTLVRecord too big (%lu)
charset
com.apple.ctkd.token-client
Pairing
ACMContextDelete
ACMRequirementGetSubrequirements
encoding
-[TKSEPKey systemKey]
com.apple.security.attestation.access
uik-p
CFBundleName
params
getLengthOfParameters
v32@?0@\"NSNumber\"8@\"NSNumber\"16q24
\"
TKTokenConfiguration.m
[PAIRING-CODE:%lu bytes]
decrypt data
PINMessageIndices
[PAIRING:%lu bytes]
 (incorrect data)
    delegateWithControlMethod: %d\n
bump
extension %{public}@ instantiating driver class %{public}@
CryptoTokenKit.transmitRequest.async
%{public}@: >>> %{public}@ %{private}@
Call 'setupWithName' was postponed, because root's home directory does not exist
%{public}@: new client connection established
%{public}@ parsed for %{public}@ from objectID: ACL=%{public}@
%{public}@: token disappeared while transmitting request
%{public}@: unpowerCard(eject=%d)
gsmak not supported, attempt to read its public key failed, error %08x
%{public}@: does not implement sign
creating connection to %{public}@, targetUID=%d
Destroying driver %{public}@
ExtClientObject: delete
Failed to create AC from data: %{public}@ (AC data: %{public}@)
registering notification '%@' failed with status %u
ctk: connecting to slot registration server (%{public}@) failed, error:%{public}@
%{public}@: >>> %{public}@
%{public}@: card reset done -> %{public}@
SEPClientObject: getKey
%{public}@: processing accumulated state changes, %d remain
The 'PINLengthBitOffset' is negative or can't fit
Synchronous call failed: %{public}@
LAContext.externalizedContext(sn=%d) failed
OIK not supported, attempt to collect proposed generation failed, error %08x
aks_sik_attest(%{public}@, %@) -> %08x
Failed to recreate TKTokenKeychainItem from attributes: invalid kSecAttrTokenID: %{public}@
Detected duplicate objectID for key %{public}@ and certificate %{public}@. This is allowed only for token extensions built for macOS 10.16 or newer. Either change build options to target newer OS version or avoid sharing same objectID for k
%@ configured with unsupported configuration object %@
Request to allow '%@' access to token provided by '%@' was '%@'
%{public}@: Error when simulating card reinsertion: %{public}@
%{public}@: endSession: counter=%ld, someoneWantsSession=%d
Failed to get configurationEndpoint, returning empty configurations
%{public}@: card reset
Request from %{public}@ for key with objectID containing invalid key type (%d)
Failed to get attributes from certificate %{public}@
%{public}@: slot answered session %{public}@ (protocol=0x%04lx, counter=%ld)
%{public}@: slot refused to allocate exclusive session for the card
Failed to verify PIN. sw=0x%04hx, retries: %d
Detected duplicate objectID for objects %{public}@ and %{public}@
%{public}@: session granted to pid %d (%lu still waiting)
%{public}@ requested systemkey aks_system_key_type_t(%d) not supported by the platform
creating connection to %{public}s endpoint%{public}s
connection to slot registration server was interrupted
release token
Slot %{public}@': failed to register, error:%{public}@
failed to get DER-encoded aks_params_t (err=%d)
Unable to deserialize AC %{public}@, error: %{public}@
create token for token in %{public}@ (AID:%{public}@)
Store skipped
all tokens removed
Slot %{public}@': failed to end NFC slot session, error:%{public}@
%{public}@: failed to call slot to allocate exclusive session for the card: %{public}@
Detected com.apple.keystore.access-keychain-keys entitlement, using in-process SEP SecKey implementation
Only refkeys can be attested by refkey
isKnownProcess:'%@' %@
%{public}@: Skipping simulated card reinsertion due to missing card
%{public}@: <<< %{public}@
%{public}@ system-session-key detected, returning %{public}@=%{public}@ in key's attributes
%{public}@: connectCardSession RESET failed
%{public}@: (%{public}@) %{public}@: error %08x(%d) ACL=%{public}@ params=%{public}@
ExtClientObject: getObject
%{public}@: does not implement key exchange
Idle time detected in extension (%{public}@), shutting down the context %{public}@
ctk: connecting to slot registration server (%{public}@) failed, error %{public}@
ExtClientObject: createObject
finishWithError: failed but did not fill an error
%s: %s: returning.\n
answering endpoint for %@
%{public}@: releasing card session %{public}@
%{public}@: transmitRequest invoked on card invalid (removed) card
operation:%d algo:%{public}@
aks_ref_key_attest(%{public}@, %@, attested: %{public}@) -> %08x
Entitlement rule matched
Present user prompt
%{public}@: does not support auth, failing constraint '%{public}@'
%{public}@: leaving session, policyReset
%{public}@: recrypted data
failed to create token in slot %{public}@ (AID:%{public}@, error:%{public}@)
failed to instantiate token with instanceID %@, error: %@
%{public}@: connectCardSession already in nego state
Failed to send request to token %{public}@, error: %{public}@
Deleting set PIN credential due to tokenID change
User prompt not available
Created new driver %{public}@
Removing stored token access for: %@
%{public}@: sendIns invoked on invalid (removed) card
Failed to create key from advertised item of token %{public}@, error: %{public}@
%s: %s: called.\n
SmartCard slot connection failed (%{public}@)
finished configuring class %{public}@
%{public}@: client pid %d gone, dropping %lu queued session request(s)
%{public}@: bump/commit finished
Token class rule-2 matched
%{public}@: transmitRequest REQ >>> %{public}@ [%{public}@] %{public}@
%{public}@: transmitRequest RSP <<< %{public}@ [%{public}@] err=%{public}@
The 'PINBitOffset' is negative or can't fit
Tried to end NFC session but it was already deallocated
%{public}@: transmitRequest RSP <<< %{public}@ [%{public}@] %{public}@
SmartCard returned error sw: 0x%04hx
logging slot %{public}s
Reset FAILED
SEPClientObject: createKey
-[LAContext evaluateAccessControl:] failed but did not provide an error, synthesizing: %{public}@
User prompt not supported
%{public}@: does not implement decapsulate
%{public}@: connection invalidated
Remote object proxy failed: %{public}@
aks_system_key_attest(%d, generation=%d, attesting=%{public}@, %@) -> %08x
Method 'setupWithName' continues
%{public}@: failed to register, error:%{public}@
unpower FAILED
%{public}@: terminate
deleting temporary context(sn=%d)
%{public}@: is read-only token
failed to instantiate token with slot, error: %@
TKTokenService_Subsystem initializing
%{public}@: sleep notification
%{public}@: going to idle-unpower card
attestKey of unknown key type
%s: %s: returning, -> ctx = %p.\n
%{public}@: signed digest
invalidating rsepkey xpc connection
TKTokenAccessUserPrompt creation failure. Missing framework: 'BaseBoard.framework'
Idle callback detected, but slot is already gone, ignoring it
%s: %s: cmd(%u) on CS[%u] -> err 0x%x (%d).\n
configure token class
%{public}@: slot connected with parameters: %{public}@
%{public}@: slot was set up
%{public}@: session busy (held by pid %d), pid %d queued behind it (%lu waiting); notifying holder
%s: %s: returning, err = %ld.\n
runningInSystemContext manager:'%s'
Cannot find requested key %{public}@ on token %{public}@
Unregistered smartcard, tokenID: %{public}@
%{public}@: connectCardSession did only PPS
%{public}@: dealloc
objectID from %{public}@ contains invalid refkey (err: %d) data:%{public}@
PIN was set for registered smart card
replacing old token with newly acquired: %@
Failed to get host proxy: %{public}@
XPC connection %@ was activated
operation:%d failed, error: %{public}@
%{public}@: does not implement key bumping
%{public}@: failed to waitForStateFlushedWithReply: %{public}@
unable to deserialize accessControl, error %{public}@
creating temporary context(sn=%d)
%{public}@: stateChangedTo:%ld atr:%{public}@
port for pm notifications registered
setupWithName:'%{public}@'
%{public}@: got publicKey %@
got notification for new slot: name=%{public}@, ep=%{public}@
Slot %{public}@': failed to check NFC support, error:%{public}@
%{public}@: delegate returned unsupported protocol 0x%04x, only T=0 or T=1 are supported
unpower
card out
%{public}@: deleted
Called empty implementation of notifyOperation
%{public}@: computed shared secret
Driver shut down all endpoints
Registered smartcard, tokenID: %{public}@, bundleID: %@
%{public}@: set protocol %04x
%{public}@: connectCardSession:proto=%04x, sensitive=%@
got invalid serverAttributes for key
%{public}@: got idle, but item is revived, ignoring
%{public}@: invalidating because of state changed to %ld
TKTokenAccessUserPrompt creation failure. Missing framework: 'SpringBoardServices.framework'
Aborting request on inactive context
%{public}@: got request for used session (%d uses), setting flag to release it ASAP
PPS FAILED
%{public}@: invalidating slot and connection %{public}@
%{public}@: <<< %{public}@ %{private}@
GID-attestKey of unknown key type
%{public}@: card removed
Failed to set protection %{public}@ for ACL (error: %{public}@)
Failed to unregister smartcard, tokenID: %{public}@, error: %@
reconnecting connection to %{public}@, try %d
Unable to connect to tokenServer even after retries. (ep=%{public}@, uid=%@)
%{public}@: connection interrupted, invalidating
%{public}@: attempted to transmit APDU when no session is opened
%{public}@: sendIns: found protocol 0x%04lx, but only T=0 or T=1 protocols are supported
Cannot find requested certificate %{public}@ on token %{public}@
%{public}@: (%{public}@) authentication needed for operation '%{public}@' ACL=%{public}@ params=%{public}@
syskey %d not supported, attempt to collect it failed, error %08x
%s: %s: CS[%u] deleted (contextDestroyed=%s).\n
initWithName:'%{public}@' successfully registered
ExtClientObject: evaluateAccessControl
reconnecting ctkd after invalidate, try %d
Extension request cancelled
CryptoTokenKit.sendIns.async
CryptoTokenKit.sendIns.sync
failed to create shared resource: %{public}@
Fetch skipped
reconnecting ctkd after interrupt, try %d
ATR:%{public}s
Checking whether kAKSReturnPolicyError is because of unsatisfied access groups
%{public}@ generated for %{public}@: ACL=%{public}@
Platform rule matched
runningInLoginWindowContext manager:'%s'
%{public}@: transmitRequest REQ >>> %{public}@ [%{public}@] %{public}@ %{private}@
%{public}@: client pid %d gone while holding the session, reclaiming it
%{public}@: connect:_state=%d,_power=%d,_proto=%d
SEPClientObject: deleteKey
%{public}@: does not implement key committing
Failed to end NFC session, error: %@
attempt to select AID failed: %{public}@
TKTokenKeychainItem got invalid accessControl, error:%{public}@ data:%{public}@
Failing attempt to evaluate ACC without LAContext set
runningInSystemContext = %d
Setting custom idle timeout to %{public}gs
%{public}@: broadcasting state change %{public}@
aks_gid_attest(%{public}@, %@) -> %08x
%@ activating from idle, but idle timer is unset
failed to get app record for %{public}@ with error: %{public}@
%{public}@: unpower done (%d)
provideEndpoint failed with:'%@'
%{public}@: transmitRequest RSP <<< %{public}@ [%{public}@] %{public}@ %{private}@
Failed to create certificate from advertised item of token %{public}@, data: %{public}@
CryptoTokenKit.transmitRequest.sync
%{public}@: leaving session, policyLeave
slot gone
TKClientToken operation failed but did not fill any error, substituting TKErrorCodeCommunicationError
extension %{public}@: cannot instantiate TKTokenDriver-based class '%{public}@' (%p)
Configuration got items: %{public}@
%{public}@: clientConnectionTerminated for pid %d
%{public}@: failed to reset the card
%{public}@: refusing to send APDU while another is in progress.
authentication failed repeatedly: tkid=%{public}@, ac=%{public}@, op=%{public}@
Deleting set PIN credential due to auth error: %@
runningInLoginWindowContext = %d
acquire token by slot
APDU FAILED
BundleID rule matched
Token class rule-1 matched
invoke on token-client connection failed with connection error %{public}@
%s: %s: cmd(%u) on CS[%u] -> ok.\n
Process has com.apple.keystore.access-keychain-keys entitlement but is missing com.apple.keystore.sik.access entitlement, any attestation attempt will fail
APDU <-%{public}s
%@: failed to transmit APDU
Unable to connect to %{public}@ even after retries.
%{public}@: transmitRequest REQ >>> %{public}@ [%{public}@] length=%lu %{private}@
%{public}@: wakeup notification
%{public}@: Reinsertion simulation cancelled due to call rate limitation
%{public}@: does not implement attestation
detected error %08x while deleting refkey, ignoring this error
SIK-attestKey of unknown key type
%{public}@: begin exclusive SmartCard session
%{public}@: used protocol %04x
SEPClientObject: operation
using system_keychain_handle, forced by client
BundleID prefix rule matched
failed to connect to named ctkd port, aborting (probably system shutdown in progress)
An attempt to release nonexistent token with instanceID=%{public}@
%{public}@: Started simulated card reinsertion
Failed to register smartcard, tokenID: %{public}@, error: %@
Mismatch in active state notifications count
%{public}@: state reply for client with no pending request, ignoring
Requested SEP key operation not allowed (%{public}@ is missing '%{public}@' entitlement)
ExtClientObject: slotName
Failed to recreate TKTokenKeychainItem from attributes: invalid kSecAttrTokenOID: %{public}@, error:%{public}@
TKErrorCodeAuthenticationNeeded does not have operation set: %{public}@
ExtClientObject: operation
Token %{public}@ failed to create new session, error %{public}@
ExtClientObject: advertisedItems
%{public}@: transmitRequest RSP <<< %{public}@ [%{public}@] length=%lu %{private}@
%{public}@: card inserted
card in
aks_system_key_collection(%d, %d, %@) -> %08x
Failed to get public key data
Failed to get driver configuration for %@
%s: %s: CS[%u] acquired.\n
APDU ->%{public}s
Authentication failure due to access groups detected, forcing hard failure
Synchronous remote object proxy failed: %{public}@
%{public}@: session requested by pid %d (%lu now queued)
%{public}@ %{public}@: an attempt to %{public}s incompatible key
%s: %s: log level set to %d.\n
%{public}@: connectCardSession did RESET & PPS
Failed notify operation %ld status %ld error %{public}@
Failed to get public key from certificate
%{public}@: does not implement decrypt
Failed to send configuration request: %{public}@
Slot %{public}@': successfully created
%{public}@: an attempt to begin session with invalidated (removed) card
T=%d
%{public}@: attested key %{public}@
with session %{public}@ on token %{public}@
acquire token by instanceID
Slot %{public}@': failed to update NFC slot UI message, error:%{public}@
%{public}@: leaving session, policyPowerDown/Eject
setting PIN sent in creation attributes into LAContext
%{public}@: new beginRequest for token driver
%{public}@: connected to slot %{public}@
invalid objectID used for SEPKey: %@
token session persists: %{public}d
attempt to begin session failed: %{public}@
%{public}@: got request for unused session, releasing it
%{public}@: querying slot for the session, proto=%04lx, counter=%ld
softlink:o:path:/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
softlink:o:path:/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
TKProtocolSmartCardSlot
NSSecureCoding
TKSlotParameters
TKTokenID
TKTokenAccessUserPromptRemoteAlertSB
TKTokenKeyExchangeParameters
TKTokenAuthOperation
TKSmartCardSlotManager
TKTokenBaseContext
TKTokenDelegate
TKTokenDriver
PKModularService
TKTokenDriverRequest
TKXPCConnectionDefault
TKClientTokenObject
TKPowerMonitor
TKExtensionClientToken
TKTokenKeychainKey
LAProtocolEndpointProviderServer
TKSmartCardSessionRequest
TKProtocolSlotRegistry
TKMLDSAPrehasher
NSCopying
TKSmartCardUserInteraction
TKTokenConfiguration
TKSmartCardSlotEngine
TKAuthContext
TKExtensionClientTokenSession
TKTokenAccessRequest
TKAPDUFormatter
TKTokenDriverHostProtocol
TKProtocolSmartCardSession
TKTokenSessionConnection
TKTokenKeyAlgorithm
TKTokenPasswordAuthOperation
TKProtocolTokenWatcherHost
TKTokenDriverDelegate
TKTokenSmartCardPINAuthOperation
TKUIServerProtocol
_TKSmartCardSlotReservation
TKSEPClientTokenObject
TKProtocolSlotClient
TKTokenConfigurationChangeProtocol
TKClientTokenSession
TKRemoteSEPKey
TKCTKDConnection
TKSmartCardTokenRegistrationXPC
TKAnalytics
TKDataSource
TKTokenDriverProtocol
TKTokenAccessDB
TKClientTokenProtocol
TKError
TKTokenAccessUserPromptInfo
NSCoding
TKSmartCardSlotScreen
TKSmartCardUserInteractionForPINOperation
TKSmartCardUserInteractionForSecurePINVerification
TKXPCConnection
TKXPCInterface
TKClientToken
TKClientTokenServerProtocol
TKSmartCardUserInteractionForSecurePINChange
TKAPDULogComponents
TKApplicationProxy
TKTokenSessionDelegate
TKBERTLVRecord
TKTokenConfigurationProtocol
TKTokenKeychainContents
TKSmartCardTokenRegistrationXPCClient
TKSmartCardTokenSession
TKSmartCardSlotProxy
TKSmartCardSlot
TKSEPKey
SBSRemoteAlertHandleObserver
TKSmartCardATRInterfaceGroup
TKAsyncOperation
TKTokenAccessUserPrompt
TKSmartCardSlotNFCManaging
TKTokenDriverContext
TKTokenService_Subsystem
TKCompactTLVRecord
TKSmartCardUserInteractionForConfirmation
TKAPDUCommandAnalyzer
TKSmartCardTokenRegistrationManager
TKExtensionClientTokenObject
TKDataConverter
TKLocalSEPRefKey
TKTokenKeychainCertificate
TKPropertyList
TKSmartCardStateRequest
TKSmartCardSessionEngine
TKAKSParameters
TKTokenConnection
TKXPCConnectionConfiguration
TKRegisteredTokenManager
TKSmartCardWithError
TKTokenAccessUserPromptNoop
TKProtocolTokenWatcherServer
TKTokenAccessDBBackedByUserDefaults
TKProtocolSlotClientNotification
TKTokenConfigurationConnection
TKProtocolSmartCardSlotNotification
TKSmartCardPINFormat
TKXPCConnectionDelegate
TKSEPClientToken
TKSmartCardATR
TKSmartCardSlotNFCSession
TKRemoteSEPKeyProtocol
TKTokenWatcher
TKSmartCard
TKTokenKeychainItem
TKTokenSession
TKProtocolSlot
TLVDebugUtility
TKTokenConfigurationConnectionProxy
TKToken
TKTLVRecord
TKClientTokenAdvertisedItem
TKSmartCardTokenDriver
TKTokenAccessRegistry
TKSharedResource
NSObject
TKProtocolSlotNotification
TKTokenConfigurationTransaction
TKXPCConnectionConfigurationDefault
NSXPCListenerDelegate
TKLocalSEPSystemKey
NSExtensionRequestHandling
TKSEPClientTokenSession
TKLocalSEPKey
TKSmartCardToken
TKTokenWatcherTokenInfo
TKTokenWatcherProxy
TKTokenDriverConfiguration
TKSimpleTLVRecord
TKSmartCardUserInteractionForStringEntry
TKSharedResourceSlot
releaseTokenWithInstanceID:
setConnection:
T@\"NSString\",C,V_keyType
engineResetCard:
setAccessDB:
startWatchingWithReply:
T@?,C,V_replyNextState
Tq,V_stateWhenRequested
_contexts
processServerAtributes:error:
serverEndpoint
tokenSession:decapsulateSharedKey:usingKey:algorithm:error:
T@,R,C,V_objectID
T@\"NSDictionary\",C,V_constraints
sac
T@\"<TKXPCConnectionDelegate>\",W,N,Vdelegate
_replyNextState
activeStateNotifications
publicPart
setPinValidationCondition:
T@\"LAContext\",R,N,V_LAContext
attestKey:usingKey:nonce:reply:
TB,N,V_proprietaryCardUsage
TQ,R
fetchByte
publicKey
securePINVerificationSupported
setVirtualColumnCount:
clientHasAccessTokenEntitlement
certificateRef
decodeResponse:sw:appendTo:error:
keychainClass
lastPathComponent
sessionID
setPassword:
useCommandChaining
T@\"TKTokenID\",R,N,V_tokenID
TB
TQ,V_activeStateNotifications
setResultData:
charset
_PINMessageIndices
decapsulateWithKey:encapsulatedKey:authContext:forceSystemSession:reply:
isAvailable
sessionWithParameters:reply:
T@\"NSNumber\",&,V_protocols
appendBytes:length:
notifyWithParameters:reply:
setContextErrorHandler:
sharedInfo
encodedObjectID
_PINLengthBitOffset
_certificateEncoding
_initWithObjectID:authContext:forceSystemSession:error:
_publicKey
endpointForToken:
evaluateRequirementIgnoringAccessGroups:
privatePart
setCanRequireCardInsertion:
setupWithPublicKey:label:
synchronousRemoteObjectProxyWithErrorHandler:
_publicKeyData
cancelRequestWithError:
finishWithError:
initWithEventName:
stringByAppendingString:
T@\"NSUUID\",R,N,V_correlationID
T@\"TKTokenConnection\",R,N,V_tokenConnection
engine:powerDownWithEject:
idleQueue
_listener
infoDictionary
setSlot:PINFormat:APDU:currentPINByteOffset:newPINByteOffset:
alloc
connectCardSessionWithParameters:
T@\"NSXPCListener\",R,N,V_listener
_currentPINByteOffset
parametersWithACMHandle:
set_testing_AuthenticateInternally:
displayMaxLines
_storeInstallationID:forBundleID:
control:data:expectedLength:reply:
engine:setAttrib:data:attribNotSupported:
setAccessControl:
sharedInstance
startNFCSlotWithName:uiSheetMessage:supportedAppIdentifiers:reply:
stringWithString:
_lastId
getValidAIDsFromCallingBundle
registerSmartCardWithTokenID:promptMessage:error:
setCtkdConnection:
signData:usingKey:algorithm:reply:
value
T@\"NSString\",R,N,V_publicPart
T@,R,N,V_exportedObject
boolValue
endNFCSlotWithError:
initialKeepAlives
setState:
T@\"NSData\",R,N,V_remoteKeyID
_delegate
_delegateWithEscapeMethod
arrayWithCapacity:
code
startRequestWithError:
T@\"NSNumber\",R,N
TQ,V_allowedProtocols
_maxOutputLength
dataForTag:
dataFromHexString:
engine:setProtocol:
powerDownIdleTimeout
T@\"LAContext\",&,N,V_authContext
T@\"NSArray\",R
TB,V_delegateWithEscapeMethod
setServerEndpoint:
T@,&,N,V_sac
_namedConnection
getAttributesOfObject:isCertificate:reply:
keyClassForProtection:
setTokenID:
set
_data
_initWithKeyType:keySize:accessControl:options:authContext:forceSystemSession:error:
_lastCardReinsertionSimulationCallTime
canSign:
displayMaxCharacters
parseFromSource:
releaseSessionWithReply:
createTokenID:persistent:reply:
T@\"NSString\",R,N,V_clientBundleID
virtualRowCount
setParameters:
setSubject:
tokenSession:decryptData:usingKey:algorithm:error:
userInfo
_clientHasAccessTokenEntitlement
initWithSession:key:error:
T@\"NSData\",&,V_subject
TI,V_kernelPort
T@,&,N
_tag
authContext
setInterface:forSelector:argumentIndex:ofReply:
T@\"NSString\",C,V_password
Td,V_interactionTimeout
_AID
_promptUserToEvaluateRequest:error:
initWithProtocol:
initWithTokenID:
logWithBytes:handler:
mapTableWithKeyOptions:valueOptions:
Tq,V_keySizeInBits
_keyType
_protocol
destroyObject
interactionTimeout
protocol
removeAccessForBundleID:matchPartial:
setCertificateEncoding:
T@\"NSObject<OS_dispatch_queue>\",&,V_queue
_certificates
_resultSW
createObjectBlock
setPINLengthBitOffset:
bundleID
_accessRequest
_creatorAuditToken
dataWithData:
getTokenWithAttributes:reply:
handleApduResponse:body:le:isCase4:synchronous:error:reply:
initWithSmartCard:AID:instanceID:tokenDriver:
isSuitableForLogin
tokenConfigurations
_initialTimeout
_keepAliveResourceSlot
_valid
currentHandler
newPINByteOffset
setExportedObject:
T@\"TKSEPKey\",R,N,V_key
_AKSSystemKeyGeneration
_pinValidationCondition
decapsulate:algorithms:parameters:error:
setLAContext:
stringRepresentation
T@\"NSNumber\",&
T@?,C,N,V_createObjectBlock
TB,N
Tq,V_endPolicy
_endpoint
_errorWithCode:userInfo:
session:createObjectWithAttributes:reply:
setDelegateWithEscapeMethod:
Tq,V_powerState
initWithCTKDEndpoint:targetUID:
certificateType
_PINBlockByteLength
_canDecrypt
_testing_stateDelay
inputItems
setExportedInterface:
T@\"NSData\",C,N
_AKSSystemKeyType
_initWithAuthContext:
evaluateRequest:error:
setPhysicalRowCount:
substringWithRange:
T@\"NSXPCConnection\",R,N
_accessControlRef
_sessionEndPolicy
_transmitting
checkAPDUResponse:error:
interfaceForSlotClientNotification
processInfo
setWasPINCredentialProvidedByPINUI:
TB,V_active
exportedInterface
T@\"NSData\",R,C,D
parseIndefiniteLengthValueFromDataSource:nestingLevel:
result
_replyQueue
_tokenManager
_wasPINCredentialInitiallySet
objectForObjectID:error:
slotName
token:terminateSession:
T@\"NSArray\",R,N
_firmwareVersion
encodeObject:forKey:
T@\"NSNumber\",&,V_displayMaxCharacters
_stateLock
certificateForObjectID:error:
date
distantPast
init
initWithTokenID:slotName:driverName:
label
ptr
T@\"TKSmartCardTokenRegistrationManager\",R
TB,V_canSign
_publicPart
initWithClassID:instanceID:
keys
objectForKey:
parseWithY:toProtocol:fromSource:hasNext:
isProxy
T@\"NSString\",C,N,V_eventName
_atr
autorelease
identityRef
setApduSentSinceLastReset:
T@\"NSDictionary\",R
T@\"NSString\",R,N,V_name
currentProtocol
_block
_eventName
_testing_AuthContextUsed
protocols
session:getAdvertisedItemsWithReply:
_activeStateNotifications
attestKeyObject:nonce:error:
beginSessionWithReply:
recryptData:attributes:error:
T@\"<TKSmartCardSlotEngineDelegate>\",W,V_delegate
T@\"TKTokenID\",R,N
TB,V_exclusive
_powerRequestsQueue
certificateForKey:
isEqual:
setAPDUTemplate:
setCanSign:
T@\"NSData\",R,V_AID
T@\"NSMapTable\",R,N,V_sessions
Tq,V_virtualColumnCount
_connectionWithCTKDConnection:
_items
decodedCertificateID:error:
getSmartCardWithError:
driverConfigurationsWithClient:
_clientDisplayName
_hasSeparateKeysAndCertificatesObjectIDSpace
_objectDestroyedBlock
_sessionID
numberWithDouble:
replyNextState
setAPDU:
T@\"TKSmartCardSessionEngine\",W,V_session
_handleConnectionClose
floatValue
setDisplayMaxLines:
setLocale:
setResultSW:
startSessionWithLAContext:parameters:reply:
_keys
engine:escape:
nextObject
removeAllObjects
base64EncodedStringWithOptions:
T@\"NSData\",R,N,V_accessControl
T@\"NSDictionary\",R,N,V_parameters
TS,V_resultSW
UTF8String
_canRequireCardInsertion
_configuration
_token
setSac:
_keySize
_sessions
didWakeUpOnEngine:
isValidWithError:
objectAtIndexedSubscript:
slotRegistryWithErrorHandler:
_serverEndpoint
.cxx_destruct
canDecrypt:
commitKey:reply:
endpoint
ensureSlotWatcherRunningWithReply:
isDaytona
token:createSessionWithError:
T@\"NSNumber\",&,V_pinValidationCondition
T@\"NSString\",R,N,V_providerDisplayName
initWithBytesNoCopy:length:freeWhenDone:
_charset
_exportedInterface
engine:runUserInteraction:error:
initWithKeyType:keySize:accessControl:options:authContext:forceSystemSession:error:
retain
setInterruptionHandler:
setPhysicalColumnCount:
setProtocol:
T@\"NSData\",C,V_publicKeyHash
Tq,V_encoding
_cardReinsertionSimulationCallInterval
_physicalRowCount
isCancelled
setMaxInputLength:
setSession:
setBool:forKey:
wasPINCredentialProvidedByPINUI
decodedKeyID:error:
escape:reply:
handleErrorForRegisteredSmartcards:forToken:
indexSet
initWithTokenID:serverEndpoint:targetUID:
processNotificationParameters:
ACMHandle
_PINJustification
_notifyToken
_session
addOperation:
attestWithKey:keyToAttest:nonce:authContext:forceSystemSessionAttestingKey:forceSystemSessionKeyToAttest:reply:
initWithSession:keychainAttributes:secRef:
sessionRequested
T@\"TKSmartCard\",R,N,V_smartCard
canPerformKeyExchange:
initWithBytes:length:encoding:
prehashDataWithMessageData:publicKey:context:
setKeyType:
setPublicKeyHash:
synchronous
T@\"TKSmartCardSlot\",W,V_slot
_installationKeyForBundleID:
_localizedPasswordLabel
setPreviousState:
setStateWhenRequested:
tokenDriver:configure:
T@,&,N,V_initialKeepAlive
_canSign
subjectKeyID
timeZoneForSecondsFromGMT:
_driverConfigurationsWithConnection:
_formatHexData:to:
_localizedPINLabel
deleteObject:error:
operationMap
proxy
releaseTokenWithInstanceID:reply:
securePINChangeSupported
T@\"NSString\",R,V_name
addTokenConfigurationForTokenInstanceID:
keyUsage
session:evaluateAccessControl:forOperation:reply:
setAllowedProtocols:
setTimeZone:
stringForKey:
tokenConfigurationChanged:
PINJustification
reserveExclusive:reply:
tokenSession:deleteObject:error:
_securePINChangeSupported
checkOperation:usingKey:algorithm:parameters:
setAuthenticationError:
tokenSession:attributesOfObject:error:
T@\"NSObject<OS_dispatch_queue>\",&,V_powerRequestsQueue
T@\"NSData\",R,N,V_ACMHandle
TB,N,V__testing_ForceAuthenticationNeeded
Tq,R,N
Tq,R,V_requestedSize
_key
_remoteAlertSemaphore
delegateWithEscapeMethod
T@\"TKClientTokenSession\",R,N,V_session
_extensionAttributes
_tokenInfos
encodeLength:into:sized:
error:withAKSReturn:ACMHandle:AKSOperation:params:message:
setSessionEndPolicy:
slotParameters
storeInstallationID:forBundleID:
T@\"NSData\",&,V_serialNumber
terminate
timeIntervalSinceDate:
tokenIDs
T@\"NSString\",C,V_label
Tq,V_currentPINByteOffset
initWithData:
unsignedIntegerValue
end
accessControlForConstraints:tokenID:error:
bundleWithIdentifier:
numberWithUnsignedInt:
setActive:
T@\"<TKTokenDriverDelegate>\",W,V_delegate
_LAContext
_kernelPort
cards
getSlotWithName:reply:
isGibraltar
revalidate
setDelegateWithControlMethod:
T@\"TKSmartCardSlotProxy\",R,N,V_proxy
_authenticationContextWasProvidedByCaller
_hasSession
fetchStoredInstallationIDForBundleID:
updateKeychainItemsForTokenID:items:reply:
getTokenIDsForClassID:reply:
initWithConnection:
stringWithUTF8String:
T@\"<TKTokenSessionPrivateDelegate>\",R,N
_ABC
clientName
powerRequestsQueue
setInitialTimeout:
T@\"<TKXPCConnectionDelegate>\",W,N
T@\"TKSmartCard\",R
_clients
_providerDisplayName
archivedDataWithRootObject:requiringSecureCoding:error:
categoryForIns:p1:p2:
connectionDidInvalidate:
setName:
PINMaxExtraDigit
_error
driverName
handleFailureInMethod:object:file:lineNumber:description:
initLocalWithObjectID:authContext:caller:forceSystemSession:error:
processIdentifier
setConstraints:
setProprietaryCardUsage:
updateNFCSlotUIMessageWithMessage:slotName:reply:
T@\"NSString\",R,N,V_tokenID
T@\"NSString\",R,N,V_slotName
T@\"TKTokenDriver\",R,V_tokenDriver
_PINLengthBitSize
boolForKey:
contextForKey:
fetchByte:
identities
TB,N,V_authenticateWhenNeeded
_clearCredentialIfNeededForTokenID:inContext:
_stateWhenRequested
activate
array
keyForObjectID:error:
parseChildTLVRecordFromSource:nestingLevel:
setValue:forKey:
T@\"<TKTokenSessionDelegate>\",W,V_delegate
_clientName
_replyFlushedState
_synchronousRemoteObjectProxyWithErrorHandler:
clientBundleID
hexDigitValue:
interfaceForXPCProtocol:
parseFromDataSource:error:
Tq,V_PINLengthBitOffset
lifetimeControlWithType:error:
setKernelPort:
setPINBlockByteLength:
setPINByteOffset:
setRegisteredTokenManager:
setSmartCard:
setupWithName:delegate:
T@\"NSData\",R,C,V_data
validateIndefiniteLengthBounds:
T@\"NSString\",C,V_PIN
T@\"TKCTKDConnection\",R,N,V_ctkdConnection
_tokenDriver
beginUsing:withBundle:
fetchAccessForRequest:
indexOfObjectPassingTest:
_APDU
arrayByAddingObjectsFromArray:
clientConnection
debugDescription
exclusive
interfaceForChangeProtocol
interfaceGroupAtIndex:
sessionEndPolicy
T@\"NSData\",C,V_APDUTemplate
copyWithZone:
correlationID
updateNFCSlotMessageWithMessage:error:
valid
LAContext
T@\"NSNumber\",&,V_displayMaxLines
T@\"NSString\",?,R,C
_subjectKeyID
_tokenConnection
configureWithConfiguration:
displayNameForBundleID:
engine:getAttrib:error:
T@\"NSData\",&,V_publicKeyHash
_keyID
appendString:
resume
setObject:forKeyedSubscript:
set_testing_stateDelay:
willChangeValueForKey:
parseFromDataSource:nestingLevel:
scheduleIdlePowerDown
Tq,V_PINBitOffset
evaluateAuthOperation:tokenOperation:retry:reply:
initWithPropertyList:
lifetimeControlKey:type:authContext:forceSystemSession:reply:
protectionForKeyClass:
stringByReplacingOccurrencesOfString:withString:
supportsAlgorithm:
unregisterSmartCardWithTokenID:callerBundleID:completion:
T@\"NSData\",&,V_subjectKeyID
_physicalColumnCount
auditToken
beginSessionWithError:
connectionDidActivate:
getAttrib:reply:
self
sign:algorithms:parameters:error:
PINLengthBitOffset
Tr^v,R
formattedAPDUResponseComponentsFromRawResponse:options:
numberWithUnsignedLongLong:
T@\"NSNumber\",&,V_maxPINLength
_active
sendIns:p1:p2:data:le:sw:error:
_extensionBundle
communicationsFailed:
displayMessage:x:y:duration:clearScreen:
minPINLength
start
T@\"TKCTKDConnection\",&,N
_powerDownIdleTimeout
arrayWithObjects:count:
interfaceForSmartCardTokenRegistration
systemLocale
zuluDateFormatter
__testing_ForceAuthenticationNeeded
_configurationConnections
_configurationEndpoint
_keepAlive
initWithInteger:
objectDestroyedBlock
remoteObjectInterface
setFirmwareVersion:
APDU
_endPolicy
_endpoints
_shouldAutomaticallyAllowRequest:
numberWithUnsignedInteger:
remoteObjectProxy
setKeySizeInBits:
setMaxPINLength:
initWithServer:
PINLengthFormatWithError:
T@\"NSArray\",R,N,V_certificates
firstObject
initForPlugInKitWithOptions:
initWithTokenID:configurationConnection:
registerSmartCardWithTokenID:promptMessage:callerBundleID:error:
registeredSmartCardsWithCompletion:
_caller
TQ,V_PINCompletion
Td,R,N
commit
remoteObjectProxyWithErrorHandler:
setInteractionTimeout:
setInvalidationHandler:
setMinPINLength:
_initWithAuthContext:caller:
createNFCSlotWithMessage:completion:
formattedAPDUResponseComponents:sw:options:
initWithTokenID:LAContext:error:
numberWithInteger:
setExclusive:
classID
_initWithToken:LAContext:parameters:error:
prefixForCategory:
setSecurePINChangeSupported:
setPIN:
enumerateObjectsUsingBlock:
isKindOfClass:
lastObject
tokenDriver:createTokenForSmartCard:AID:error:
unregisterSmartCardWithTokenID:callerBundleID:error:
_testing_AuthenticateInternally
registerForConfigurationChange:
T@\"TKTokenKeychainContents\",&,V_keychainContents
Tq,V_newPINByteOffset
_advertisedItems
_keySizeInBits
observeValueForKeyPath:ofObject:change:context:
T@\"NSXPCConnection\",R,W,N,V_connection
_localizedString:
configurationConnection
initialTimeout
operation:data:algorithms:parameters:error:
setNumber:forKey:
systemKey
systemSessionKey
T@\"NSNumber\",&,V_vendorID
TC
_log
createDriver
engineSimulateCardReinsertion:
tokenSession:createObjectWithAttributes:error:
T@\"NSXPCInterface\",R,N
_displayNamesCache
setReplyNextState:
waitForNextState:reply:
allowedProtocols
encodeWithCoder:
initSystemKeyIDs
setResult:
transmitSynchronouslyChunkedIns:p1:p2:data:offset:realLe:chained:isCase4:responseBody:sw:error:
T@?,C,N,V_objectDestroyedBlock
apduSentSinceLastReset
errorWithDomain:code:userInfo:
getEndpoint:
numberWithInt:
setQueue:
_exportedObject
T@\"NSString\",C,V_localizedPINLabel
T^{aks_ref_key_s=},R,N,V_AKSRefKey
_sac
exportedObject
registerSmartCardWithTokenID:promptMessage:callerBundleID:completion:
setShareState:
T{?=[8I]},N,V_creatorAuditToken
T@\"NSData\",R,N,V_value
_delegateWithControlMethod
getAttributesOfKey:authContext:forceSystemSession:reply:
initWithCertificate:objectID:
signWithKey:digest:authContext:forceSystemSession:reply:
T@\"<TKTokenDelegate>\",W,V_delegate
_vendorID
setLastUsedRegisteredTokenID:
T@\"NSData\",C,V_applicationTag
T@\"NSDictionary\",R,C,N
T@\"NSNumber\",&,V_certificateType
Tq,V_previousState
__testing_AuthContextUsed
_synchronousRemoteObjectProxy
cardPresent:
initWithServiceName:viewControllerClassName:
TB,V_canDecrypt
_initWithObjectID:authContext:caller:isIDUnknown:error:
createObjectWithAttributes:reply:
keySizeInBits
sequenceOfRecordsFromData:
session:slotNameWithReply:
setCanDecrypt:
setPINFormat:
T@\"NSNumber\",R,N,V_sessionID
T@\"NSNumber\",R,N,V_protocol
initWithInsertionHandler:
propertyList
setMaxOutputLength:
tokenSession:attestKey:usingKey:nonce:error:
tokenSession:beginAuthForOperation:constraint:error:
_remoteKeyID
smartCard
T#,R
_proprietaryCardUsage
_setQueue:
baseClassForUI
ensureSessionWithClient:connectionIdentifier:error:
initWithBytes:
interfaceForSlotClient
hasEntitlement:
_maxInputLength
_initWithKeyType:keySize:accessControl:options:authContext:caller:forceSystemSession:error:
_productID
_resource
addSlotWithEndpoint:name:type:reply:
bytesSafeToRead:
clearAllAccessRecords
T@\"NSDictionary\",R,N
T@\"NSNumber\",&,V_productID
T@\"NSString\",R,N,V_privatePart
Td,V_initialTimeout
Tq,V_PINBlockByteLength
_storeAccess:forRequest:
beginTransactionWithReply:
commandNameForCla:ins:
transmit:reply:
T@?,C,V_reply
_idleTimeout
accessControlRef
addObject:
initWithCaller:tokenID:extension:
initWithClientBundleID:clientName:clientConnection:clientHasAccessTokenEntitlement:tokenID:providerBundleID:providerName:correlationID:
keyID
dataWithLength:
_result
T@\"NSString\",R,N,V_classID
canSimulateCardReinsertion
initWithLAContext:ACMHandle:sharedResource:
initWithToken:
physicalRowCount
sendControl:data:expectedLength:reply:
T@\"NSString\",R,N,V_providerName
_secRef
Tq,V_charset
buildPayload
setProductID:
substringToIndex:
windowsLocaleCodeFromLocaleIdentifier:
Tq,V_shareState
slotInitialized
_serialNumber
dataWithBytes:length:
initWithObjectID:authContext:forceSystemSession:error:
localeIdentifier
T@,&,N,V_keepAlive
_resultData
eventName
finalizeAuthOperation:evaluatedAuthOperation:reply:
initWithTag:records:
objectAtIndex:
pinValidationCondition
unreserve
T@\"NSDictionary\",R,N,V_keychainAttributes
T@\"TKSmartCardSlotManager\",R
_authenticateWhenNeeded
_idleQueue
delegateWithControlMethod
initWithSuiteName:
setAuthenticateWhenNeeded:
setNFCAllowedAIDs:
dateFromString:
Tq,V_PINLengthBitSize
_sensitive
applicationTag
canRequireCardInsertion
dataFromPtr:
dictionary
powerDownWithEject:
T@\"NSXPCConnection\",R,N,V_connection
_getReservationId
_providerBundleID
releaseResourceImmediatelly:
reply
session:getAttributesOfObjectID:reply:
setCurrentProtocol:
transmitRequest:reply:
withError:accessControl:invoke:
_ATR
initWithToken:LAContext:parameters:error:
initWithTokenID:error:
integerValue
setSerialNumber:
shareState
stringWithFormat:
_removalHandlers
generateKeyType:keySize:accessControl:options:authContext:forceSystemSession:reply:
initWithCard:error:
instanceID
endSessionWithReply:
fileExistsAtPath:isDirectory:
providerBundleID
providerName
_params
T@\"NSNumber\",&,V_certificateEncoding
removeAllTokens
maxOutputLength
_createAIDsValidationError
ctkdConnection
formattedAPDUCommandComponentsFromRawAPDU:options:
insertObject:atIndex:
T@\"NSString\",R,V_tokenID
Tq,V_physicalRowCount
_PINConfirmation
_currentProtocol
_testing_ForceAuthenticationNeeded
isEqualToData:
synchronous:remoteSlotWithErrorHandler:
wasPINCredentialInitiallySet
T@,&,N,V_exportedObject
Tq,V_minPINLength
T@\"NSMutableDictionary\",R,C,D
PINLengthBitSize
setSynchronous:
T@\"TKTokenConfiguration\",R,V_configuration
_encoded
decryptData:usingKey:algorithm:parameters:reply:
_idlePowerDownSource
_ptr
acquireTokenWithInstanceID:reply:
initWithParameters:
processObjectCreationAttributes:authContext:error:
setCurrentPINByteOffset:
setInitialKeepAlive:
setPINLengthBitSize:
PIN
T@\"TKToken\",R,N,V_token
arrayByAddingObject:
configuration
dictionaryRepresentation
inSessionWithError:executeBlock:
mutableCopy
respondsToSelector:
_findReservation:connection:
connectToEndpoint:synchronous:reply:
evaluateAccessControl:forOperation:reply:
fetchDataWithLength:
reserveProtocols:reservationId:exclusive:reply:
setDelegate:
set_testing_noAutomaticReconnect:
startWatching
T@\"NSDictionary\",&,V_parameters
initWithSource:
caller
setSensitive:
setup
suitableForLogin
tokenDriver:tokenForConfiguration:error:
tokenFromAuditToken:
_exclusive
awaken
getConfigurationEndpoint:
performSelector:withObject:withObject:
removeTokenID:reply:
setCanPerformKeyExchange:
stateWhenRequested
_publicKeyHash
addEntriesFromDictionary:
initWithRemoteObjectInterface:exportedInterface:exportedObject:replyQueue:
registerObserver:
tokenDriver:terminateToken:
T@\"NSData\",&,V_resultData
_context
_queuedParameters
conformsToProtocol:
creatorAuditToken
invalidate
remoteAlertHandleDidDeactivate:
T@\"TKClientToken\",R,N,V_token
_useCommandChaining
delegate
externalizedContext
getTokenConfigurationEndpointWithReply:
initWithToken:LAContext:parameters:tokenManager:error:
setAwaken:
setUserInfo:
stringWithCapacity:
userInteractionForStringEntry
validateSendInsPreconditionsWithError:
T@\"NSError\",C,V_authenticationError
bumpKey:reply:
componentsSeparatedByString:
T@\"TKTokenConfiguration\",R
_fetchAccessForRequest:
_maxPINLength
authenticateWhenNeeded
countByEnumeratingWithState:objects:count:
performSelector:
processHandleForAuditToken:
removeObjectForKey:
_PINCompletion
_parentCard
_stateRequests
mutableBytes
objectForKeyedSubscript:
objectID:operation:inputData:algorithms:parameters:reply:
removeObjectsAtIndexes:
setEndPolicy:
TB,V_apduSentSinceLastReset
_auxiliaryConnection
initWithItemInfo:
maxPINLength
parseFromDataSource:
setSuitableForLogin:
setWasPINCredentialInitiallySet:
token
T@\"NSData\",R,N,V_historicalBytes
TB,V_securePINChangeSupported
endNFCSlotWithName:reply:
getClassIDsWithReply:
removeTokenConfigurationForTokenInstanceID:
_sharedResource
currentLocale
mainBundle
T@\"NSXPCInterface\",&,N,V_exportedInterface
Tq,V_state
_allowedProtocols
_isPersistenceEnabled
configurationEndpoint
initWithBundleIdentifier:allowPlaceholder:error:
localizedStringForKey:value:table:
setProtocols:
T@\"NSXPCConnection\",R,N,V_caller
initWithAccessDB:userPrompt:
_issuer
_PINFormat
createObjectWithAttributes:error:
driverConfigurationsWithCTKDConnection:
raise:format:
removeObjectAtIndex:
setData:
setSecurePINVerificationSupported:
tokenConnection
_keychainItems
callerName
useExtendedLength
valueForKey:
_preflightStatus
initWithBlock:
resultSW
setActiveStateNotifications:
PINCompletion
T@,&,N,V__testing_AuthContextUsed
inSlotQueueExecuteBlock:synchronous:
serialNumber
state
tokenSession:performKeyExchangeWithPublicKey:usingKey:algorithm:parameters:error:
errorWithCode:debugDescription:
setCla:
recryptWithKey:data:attributes:authContext:forceSystemSession:reply:
retainCount
setUserPrompt:
transmitRequest:synchronous:logActivity:reply:
setupConnection
insertedToken:
isAlgorithm:
leaveSession:
objectID
allKeys
initWithTokenID:ctkdConnection:
preflightStatus
T@\"TKTokenID\",R,V_tokenID
historicalRecords
initWithTag:value:data:
tokenID
_accessControl
_watcher
dictionaryWithObjects:forKeys:
initWithTokenInfo:
_locale
canDecrypt
dataUsingEncoding:
initWithConfigurationConnection:
physicalColumnCount
setObject:forKey:
T@\"NSString\",R,N,V_providerBundleID
_changeStateTo:forClient:
_objectID
_sharedInfo
dictionaryWithObjects:forKeys:count:
evaluateAuthOperation:tokenOperation:reply:
localizedShortName
_displayMaxCharacters
_label
_providerName
configureWithReply:
fillWithItems:
setClasses:forSelector:argumentIndex:ofReply:
setPINMessageIndices:
T@\"NSArray\",C,N
Tq,V_maxOutputLength
_minPINLength
bundleIdentifier
serverConnection
setObjectDestroyedBlock:
keyType
Td,N,V_idleTimeout
__testing_AuthenticateInternally
_classID
_previousState
willSleepOnEngine:
dealloc
_callerName
_identities
currentPINByteOffset
encodedKeyID:
productID
setIdleQueue:
T@\"NSData\",R,N,V_data
T@\"NSXPCListenerEndpoint\",&,V_serverEndpoint
allValues
encodedCertificateID:
interfaceGroupForProtocol:
transmitRequest:synchronous:reply:
userInteractionForSecurePINChangeWithPINFormat:APDU:currentPINByteOffset:newPINByteOffset:
setConfigurationEndpoint:reply:
cla
TQ,V_PINConfirmation
_localizedShortName
hashTableWithOptions:
initWithSession:objectID:attributes:
setLocalizedPasswordLabel:
T@\"NSString\",R,N,V_clientName
historicalBytes
T@\"TKSlotParameters\",R,C,V_slotParameters
_apduQueue
_connectionWithErrorHandler:
setPINJustification:
terminateWithReply:
PINFormatStringWithError:
context
T@,R,N,V_keyID
_historicalBytes
_tokenID
cardSessionRequested
processName
setLength:
T@\"TKSmartCard\",&,V_smartCard
_nfcAppIdentifiers
initWithSlot:connection:
null
satisfiesKeyUsage:
setCharset:
setPresentationTarget:
synchronous:remoteSlotClientWithErrorHandler:
T@\"TKSmartCardSlot\",R,N,V_slot
_PINBitOffset
_constraints
_sensitiveRequired
_setTargetUserIdentifier:
callerPID
currentConnection
hasPrefix:
T@\"NSString\",R,V_stringRepresentation
T@\"NSXPCConnection\",R,N,V_tokenConnection
computeSharedSecret:error:
locale
pivContainerNames
setApplicationTag:
tokenSession:supportsOperation:usingKey:algorithm:
T@\"TKSharedResource\",R,N,V_sharedResource
_beginSessionQueue
appendFormat:
initWithSlotName:nfcSlotManager:
tokenSession:bumpKey:error:
T@\"NSString\",R,N,V_driverName
_tokenConnections
certificateEncoding
deleteObject:reply:
deleteWithError:
name
setLocalizedPINLabel:
setPowerDownIdleTimeout:
T^{__SecCertificate=},R,N
_setupDriver
_testing_noAutomaticReconnect
initForReadingFromData:error:
numberWithUnsignedLong:
setIssuer:
setVirtualRowCount:
tokenSession:commitKey:error:
session
length
storeAccess:forRequest:
T@\"NSData\",R,N,V_bytes
T@\"NSNumber\",&,V_minPINLength
T@\"NSString\",R,N,V_clientDisplayName
send
sessionWithLAContext:error:
setupSlotWithReply:
withError:invoke:
_serverConnection
sequenceOfRecordsFromData:nestingLevel:
T@\"NSLocale\",&
setWithObjects:
T@\"NSArray\",R,C
authenticationError
initWithTag:value:
setCreatorAuditToken:
unregisterSmartCardWithTokenID:error:
PINBitOffset
_sessionCounter
_apduSentSinceLastReset
addRemovalHandler:forTokenID:
categoryForCla:ins:p1:p2:
getAdvertisedItemsWithReply:
importOperation:
removedToken:
_clientBundleID
Tr*,R
_certificateType
_dumpPlist:into:
setSubjectKeyID:
setValid:
T@\"NSXPCListenerEndpoint\",R,N,V_configurationEndpoint
_lock
defaultService
dictionaryForState:
maskedDataDescriptionForIns:p1:p2:command:
setLabel:
T@\"NSData\",R,N,V_publicKey
T@,&
_PIN
accessControl
localizedStringWithFormat:
performKeyExchangeWithPublicKey:usingKey:algorithm:parameters:reply:
setSlotWithName:endpoint:type:reply:
T@\"NSData\",C,V_publicKeyData
TB,V_awaken
evaluateAccessControl:forOperation:error:
issuer
builtinTokenIDs
initWithName:
kernelPort
setCardReinsertionSimulationCallInterval:
weakObjectsHashTable
_startListening
_proxy
encodeNumber:into:
remoteSessionWithErrorHandler:synchronous:
set_testing_ForceAuthenticationNeeded:
T@\"NSXPCConnection\",R,N,V_clientConnection
T@\"NSXPCInterface\",R,N,V_remoteObjectInterface
TB,V_result
beginRequest
calculateChunkInfoForIns:data:offset:chained:isCase4:
commitKeyWithError:
engine:transmit:
isEqualToString:
keyRef
pivContainerNameForTag:
session:deleteObjectWithObjectID:reply:
setSlot:PINFormat:APDU:PINByteOffset:
userInteractionForSecurePINVerificationWithPINFormat:APDU:PINByteOffset:
_driver
TB,N,V_canRequireCardInsertion
initForPlugInKit
initWithMachServiceName:options:
interfaceForProtocol
parseLongFormValueFromDataSource:lengthByte:
T@\"TKToken\",R,V_token
T@\"TKTokenID\",&,V_tokenID
TB,R,N
_reservationId
localizedName
setPowerRequestsQueue:
T^{__SecIdentity=},R,N
_name
remoteAlertHandleDidActivate:
tokenSession:decryptData:usingKey:algorithm:parameters:error:
T@\"NSObject<OS_dispatch_queue>\",R,N,V_replyQueue
T@\"NSString\",&,V_result
T@\"NSMutableDictionary\",R,N,V_tokenConnections
T@,R,N
_canPerformKeyExchange
_initialKeepAlive
_portRef
bytes
T@\"TKSharedResourceSlot\",&,N,V_keepAliveResourceSlot
_cla
_newPINByteOffset
initWithCoder:
initWithConfiguration:
initWithPreflightStatus:
operationResult:error:
T@\"NSData\",&,V_APDU
setIdleTimeout:
_algorithms
_reply
powerState
setPINBitOffset:
setUseCommandChaining:
initWithTokenDriver:instanceID:
TB,GisSuitableForLogin,V_suitableForLogin
_requestedSize
bumpKeyWithError:
initWithCTKDConnection:
initWithSlot:
installSessionIdentifier
Tq,V_maxPINLength
_finished
_password
allStoredBundleIDs
configurationData
ensureConnectionCanRequireCardInsertion:error:
T@\"NSData\",R,N,V_objectID
_keychainAttributes
acquireTokenWithSlot:AID:proprietaryCardUsage:reply:
forceSystemSession
runUserInteraction:reply:
sendEscape:reply:
setUnderlyingQueue:
userInteractionForConfirmation
_wasPINCredentialProvidedByPINUI
T@\"NSObject<OS_dispatch_queue>\",&,N,V_idleQueue
T@\"TKTokenConfigurationConnection\",R,N
TB,N,V__testing_noAutomaticReconnect
_extensionAuxiliaryVendorProtocol
initWithMaxBlockSize:
session:objectID:operation:data:algorithms:parameters:reply:
setDateFormat:
setPowerState:
_authContext
_protocols
_reservations
replyFlushedState
setUseExtendedLength:
_handle
keybagHandleForceSystemSession:
_remoteObjectProxy
decodeObjectOfClass:forKey:
defaultMonitor
sendIns:p1:p2:data:le:reply:
setPINCompletion:
T@\"NSData\",R,C
T@\"LAContext\",&,N,V_LAContext
_securePINVerificationSupported
Td,V_powerDownIdleTimeout
parseValueFromDataSource:
set_hasSeparateKeysAndCertificatesObjectIDSpace:
sleepForTimeInterval:
tokenConnections
_coreServicesLocalizedNameForBundleID:
containingBundleRecord
hexStringFromData:
localizedPINLabel
numberWithLongLong:
queue
removeObject:
recordFromData:
_object
T@\"NSXPCConnection\",W,V_connection
_parameters
dataWithBytesNoCopy:length:
localizedPasswordLabel
tokenSession:supportsOperation:usingKey:algorithm:parameters:
containsObject:
TB,V_securePINVerificationSupported
_connection
_someoneWantsSession
_state
initWithPublicKey:label:objectID:canSign:canDecrypt:canPerformKeyExchange:
initWithTokenAccessRequest:
remoteKeyID
T@\"NSArray\",R,N,V_identities
numberWithBool:
privateDelegate
setData:forKey:
T@\"LAContext\",R,N,V_authContext
T@\"TKSmartCardATR\",&,V_ATR
configurationForTokenID:
setCertificateType:
PINFormat
_callerPID
finish
setInsertionHandler:
setPreflightStatus:
setReply:
setMaxConcurrentOperationCount:
TQ,R,N,V_tag
_shareState
hasSEP
publicKeyHash
setPublicKeyData:
setSlot:
valueForEntitlement:
_keychainContents
decapsulateSharedKey:usingKey:algorithm:reply:
initWithEndpoint:
maxInputLength
objectEnumerator
setKeychainItems:
_applicationTag
T@\"NSArray\",&,V_PINMessageIndices
PINMessageIndices
TB,V_delegateWithControlMethod
_remoteObjectInterface
_virtualColumnCount
remoteAlertHandle:didInvalidateWithError:
T@\"TKTokenDriverContext\",W,N,V_context
_interactionTimeout
beginTransaction
defaultManager
initWithWatcher:
slotNames
Tq,V_virtualRowCount
constraints
endPolicy
listener
runWithReply:
setPINConfirmation:
_targetUID
initWithObjectID:
setContext:forKey:
TB,R
_suitableForLogin
getKeychainItemsForTokenID:reply:
T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue
_clientConnection
_setupWithDriver:error:
_slot
characterAtIndex:
count
endTransactionWithReply:
keepAliveResourceSlot
addObserver:forKeyPath:options:context:
authContextWithError:
deleteKey:authContext:forceSystemSession:reply:
endRequest
keychainItemWithInfo:
providerDisplayName
setCallerPID:
setCreateObjectBlock:
_AKSRefKey
_privatePart
_queue
extensionAttributes
registerTokenAccessRequestCorrelationID:access:reply:
selectApplication:error:
withSessionID:invoke:
T@\"NSData\",R,N
T@\"NSString\",R
Tq,V_PINJustification
_PINByteOffset
_correlationID
_sessionRequests
_weakConfigurationConnection
computeSharedSecretWithKey:publicKey:authContext:forceSystemSession:reply:
T@\"NSString\",R,C,N,V_slotName
addIndex:
data
domain
encodedAccessGroups
endSession:reply:
engine:control:data:expectedLength:
errorWithResult:operation:forError:
T@\"NSArray\",R,N,V_keys
TB,V_canPerformKeyExchange
notifyOperation:forToken:withStatus:
setNewPINByteOffset:
set_testing_AuthContextUsed:
slot
tokenSessions
unsignedCharValue
firmwareVersion
T@\"NSDictionary\",&,N,V_parameters
Tq,N,V_preflightStatus
_grantedAccess
_virtualRowCount
parseValueFromDataSource:nestingLevel:
reset
setEventName:
TB,R,N,V_clientHasAccessTokenEntitlement
_encoding
_remoteAlertHandle
decapsulateKey:error:
virtualColumnCount
T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},R,N
_ACMHandle
_powerMonitor
_syncObject
decodedObjectID:isCertificate:error:
identifier
keychainItems
_stringRepresentation
appendData:
callerHasEntitlement:error:
cancel
decodeObjectOfClasses:forKey:
getTokenEndpointForTokenID:canRequireCardInsertion:reply:
initWithTargetPredicate:
setCaller:
_extensionAuxiliaryHostProtocol
_slotParameters
T@\"NSXPCListenerEndpoint\",R,N
_debugID
canUseSEPLocally
localizedInfoDictionary
setReplyFlushedState:
simulateCardReinsertionWithError:
PINBlockByteLength
subject
_awaken
_configurationConnection
fillPIN:intoAPDUTemplate:PINByteOffset:error:
isExecuting
readDataForTokenID:reply:
subdataWithRange:
PINByteOffset
attestKey:nonce:error:
hash
keepAlive
querySessionSynchronous:reply:
registeredSmartCardTokens
setRemoteObjectInterface:
clientDisplayName
initWithSlotParameters:
simulateCardReinsertionWithReply:
string
tokenSession:signData:usingKey:algorithm:error:
T@\"NSDictionary\",&,V_extensionAttributes
T@\"<TKSmartCardUserInteractionDelegate>\",W,V_delegate
T@\"NSString\",&,V_firmwareVersion
_queueManager
_value
getDictionaryParameters
superclass
waitForStateFlushedWithReply:
T@\"NSData\",&
TB,V_valid
TQ,V_currentProtocol
_setupWithName:delegate:
_useExtendedLength
auditAuthOperation:auditToken:success:
initWithTokenConnection:
parseShortFormValueFromDataSource:length:
setXpcEndpoint:
_systemKey
active
driver
isAsynchronous
isMemberOfClass:
performSelector:withObject:
predicateForProcess:
PINBlockString
TB,N,V__testing_AuthenticateInternally
_displayMaxLines
_smartCard
indexOfObject:
newHandleWithDefinition:configurationContext:
screen
setVendorID:
_ctkdConnection
T@\"NSHashTable\",R,V_cards
endSession
isCredentialSet:
tokenInfoForTokenID:
hasSuffix:
parameters
sensitive
T@\"NSDictionary\",R,C
initWithPublicPart:privatePart:
__testing_noAutomaticReconnect
_insertionHandler
lengthOfBytesUsingEncoding:
sessions
setEncoding:
signDigest:attributes:error:
APDUTemplate
Tq,V_maxInputLength
_registrationConnection
_writeNumber:into:bitOffset:bitLength:
attributes
idleTimeout
promptUserToEvaluateRequest:error:
resultData
ATR
TQ,R,N
Tr*,R,V_ptr
items
processAccessGroupsOfACLDictionary:intoGroups:callerGroups:
setATR:
TA
_idleTimer
beginRequestWithExtensionContext:
evaluatePolicy:options:reply:
initWithAlgorithmsArray:
longLongValue
strongToWeakObjectsMapTable
T@\"TKTokenDriver\",R,N,V_driver
_connectionToServer
commandNameForIns:
```
