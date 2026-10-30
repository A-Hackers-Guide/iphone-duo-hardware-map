# `/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,098,448 bytes.

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
Unregistered smartcard, tokenID: %{public}@
initWithName:'%{public}@' successfully registered
%{public}@: failed to reset the card
%{public}@: unpower done (%d)
OIK not supported, attempt to collect proposed generation failed, error %08x
BundleID prefix rule matched
Setting custom idle timeout to %{public}gs
Slot %{public}@': successfully created
port for pm notifications registered
%@: failed to transmit APDU
Fetch skipped
%{public}@: >>> %{public}@
Mismatch in active state notifications count
%{public}@: going to idle-unpower card
%{public}@: session requested by pid %d (%lu now queued)
%{public}@: refusing to send APDU while another is in progress.
failed to create token in slot %{public}@ (AID:%{public}@, error:%{public}@)
%{public}@: set protocol %04x
using system_keychain_handle, forced by client
all tokens removed
Process has com.apple.keystore.access-keychain-keys entitlement but is missing com.apple.keystore.sik.access entitlement, any attestation attempt will fail
SEPClientObject: deleteKey
invalidating rsepkey xpc connection
TKTokenAccessUserPrompt creation failure. Missing framework: 'BaseBoard.framework'
Removing stored token access for: %@
Synchronous remote object proxy failed: %{public}@
Reset FAILED
%{public}@: (%{public}@) authentication needed for operation '%{public}@' ACL=%{public}@ params=%{public}@
Called empty implementation of notifyOperation
%{public}@: does not implement attestation
Failed to send configuration request: %{public}@
setupWithName:'%{public}@'
%{public}@: leaving session, policyReset
%@ activating from idle, but idle timer is unset
%{public}@: state reply for client with no pending request, ignoring
ExtClientObject: delete
Deleting set PIN credential due to auth error: %@
Present user prompt
Configuration got items: %{public}@
Request from %{public}@ for key with objectID containing invalid key type (%d)
unable to deserialize accessControl, error %{public}@
Token class rule-1 matched
ExtClientObject: createObject
Synchronous call failed: %{public}@
%{public}@: card reset done -> %{public}@
Unable to deserialize AC %{public}@, error: %{public}@
%{public}@: begin exclusive SmartCard session
Authentication failure due to access groups detected, forcing hard failure
Failing attempt to evaluate ACC without LAContext set
failed to instantiate token with instanceID %@, error: %@
%{public}@: transmitRequest REQ >>> %{public}@ [%{public}@] %{public}@
%{public}@: <<< %{public}@ %{private}@
ExtClientObject: operation
attempt to select AID failed: %{public}@
Failed to recreate TKTokenKeychainItem from attributes: invalid kSecAttrTokenOID: %{public}@, error:%{public}@
Entitlement rule matched
Store skipped
connection to slot registration server was interrupted
%{public}@: processing accumulated state changes, %d remain
%{public}@: slot connected with parameters: %{public}@
%{public}@: failed to waitForStateFlushedWithReply: %{public}@
%{public}@: client pid %d gone, dropping %lu queued session request(s)
operation:%d algo:%{public}@
BundleID rule matched
failed to get app record for %{public}@ with error: %{public}@
%{public}@: Error when simulating card reinsertion: %{public}@
card out
%{public}@: connectCardSession did RESET & PPS
creating temporary context(sn=%d)
%{public}@: signed digest
attestKey of unknown key type
failed to instantiate token with slot, error: %@
%{public}@: session busy (held by pid %d), pid %d queued behind it (%lu waiting); notifying holder
Requested SEP key operation not allowed (%{public}@ is missing '%{public}@' entitlement)
setting PIN sent in creation attributes into LAContext
%{public}@: does not support auth, failing constraint '%{public}@'
%{public}@: querying slot for the session, proto=%04lx, counter=%ld
%{public}@: failed to register, error:%{public}@
%{public}@: connectCardSession already in nego state
%{public}@: got request for unused session, releasing it
%{public}@: transmitRequest RSP <<< %{public}@ [%{public}@] %{public}@
%{public}@: sendIns: found protocol 0x%04lx, but only T=0 or T=1 protocols are supported
CryptoTokenKit.sendIns.sync
The 'PINBitOffset' is negative or can't fit
Detected com.apple.keystore.access-keychain-keys entitlement, using in-process SEP SecKey implementation
%{public}@: session granted to pid %d (%lu still waiting)
Failed to set protection %{public}@ for ACL (error: %{public}@)
%{public}@: unpowerCard(eject=%d)
%{public}@: connectCardSession RESET failed
Failed to send request to token %{public}@, error: %{public}@
Failed to get driver configuration for %@
creating connection to %{public}s endpoint%{public}s
%s: %s: cmd(%u) on CS[%u] -> err 0x%x (%d).\n
isKnownProcess:'%@' %@
extension %{public}@: cannot instantiate TKTokenDriver-based class '%{public}@' (%p)
%{public}@: new beginRequest for token driver
The 'PINLengthBitOffset' is negative or can't fit
unpower
%{public}@: (%{public}@) %{public}@: error %08x(%d) ACL=%{public}@ params=%{public}@
deleting temporary context(sn=%d)
User prompt not available
acquire token by slot
Slot %{public}@': failed to update NFC slot UI message, error:%{public}@
SmartCard slot connection failed (%{public}@)
%{public}@: Started simulated card reinsertion
%{public}@: transmitRequest invoked on card invalid (removed) card
%{public}@: <<< %{public}@
%{public}@: slot was set up
TKErrorCodeAuthenticationNeeded does not have operation set: %{public}@
TKTokenService_Subsystem initializing
Failed to create key from advertised item of token %{public}@, error: %{public}@
-[LAContext evaluateAccessControl:] failed but did not provide an error, synthesizing: %{public}@
%s: %s: CS[%u] acquired.\n
runningInSystemContext manager:'%s'
TKTokenKeychainItem got invalid accessControl, error:%{public}@ data:%{public}@
Token class rule-2 matched
%{public}@: does not implement sign
%{public}@: does not implement key committing
%s: %s: called.\n
registering notification '%@' failed with status %u
Request to allow '%@' access to token provided by '%@' was '%@'
%{public}@: is read-only token
APDU <-%{public}s
reconnecting ctkd after interrupt, try %d
Slot %{public}@': failed to check NFC support, error:%{public}@
Detected duplicate objectID for key %{public}@ and certificate %{public}@. This is allowed only for token extensions built for macOS 10.16 or newer. Either change build options to target newer OS version or avoid sharing same objectID for k
PPS FAILED
aks_system_key_collection(%d, %d, %@) -> %08x
TKClientToken operation failed but did not fill any error, substituting TKErrorCodeCommunicationError
Destroying driver %{public}@
Detected duplicate objectID for objects %{public}@ and %{public}@
objectID from %{public}@ contains invalid refkey (err: %d) data:%{public}@
aks_ref_key_attest(%{public}@, %@, attested: %{public}@) -> %08x
%{public}@: >>> %{public}@ %{private}@
%{public}@ system-session-key detected, returning %{public}@=%{public}@ in key's attributes
%{public}@: attested key %{public}@
%{public}@: connection invalidated
%{public}@: transmitRequest RSP <<< %{public}@ [%{public}@] err=%{public}@
Failed to verify PIN. sw=0x%04hx, retries: %d
APDU FAILED
Created new driver %{public}@
Only refkeys can be attested by refkey
Unable to connect to tokenServer even after retries. (ep=%{public}@, uid=%@)
%{public}@: stateChangedTo:%ld atr:%{public}@
%{public}@: slot refused to allocate exclusive session for the card
%{public}@: transmitRequest REQ >>> %{public}@ [%{public}@] length=%lu %{private}@
logging slot %{public}s
%{public}@: card inserted
finishWithError: failed but did not fill an error
ctk: connecting to slot registration server (%{public}@) failed, error:%{public}@
CryptoTokenKit.transmitRequest.async
ExtClientObject: evaluateAccessControl
%{public}@: failed to call slot to allocate exclusive session for the card: %{public}@
SEPClientObject: operation
failed to get DER-encoded aks_params_t (err=%d)
detected error %08x while deleting refkey, ignoring this error
replacing old token with newly acquired: %@
%{public}@: Reinsertion simulation cancelled due to call rate limitation
%{public}@: terminate
ExtClientObject: getObject
%s: %s: cmd(%u) on CS[%u] -> ok.\n
Idle time detected in extension (%{public}@), shutting down the context %{public}@
SmartCard returned error sw: 0x%04hx
CryptoTokenKit.sendIns.async
Cannot find requested certificate %{public}@ on token %{public}@
Platform rule matched
reconnecting ctkd after invalidate, try %d
CryptoTokenKit.transmitRequest.sync
%{public}@: transmitRequest RSP <<< %{public}@ [%{public}@] %{public}@ %{private}@
Failed to get configurationEndpoint, returning empty configurations
acquire token by instanceID
XPC connection %@ was activated
%{public}@: clientConnectionTerminated for pid %d
%{public}@ generated for %{public}@: ACL=%{public}@
reconnecting connection to %{public}@, try %d
ExtClientObject: slotName
%{public}@: does not implement decrypt
Aborting request on inactive context
%{public}@: transmitRequest RSP <<< %{public}@ [%{public}@] length=%lu %{private}@
Remote object proxy failed: %{public}@
%{public}@: wakeup notification
%{public}@: deleted
Failed notify operation %ld status %ld error %{public}@
Extension request cancelled
%{public}@: dealloc
%{public}@ parsed for %{public}@ from objectID: ACL=%{public}@
aks_gid_attest(%{public}@, %@) -> %08x
create token for token in %{public}@ (AID:%{public}@)
%{public}@: does not implement key exchange
runningInLoginWindowContext manager:'%s'
%{public}@: token disappeared while transmitting request
Failed to unregister smartcard, tokenID: %{public}@, error: %@
aks_system_key_attest(%d, generation=%d, attesting=%{public}@, %@) -> %08x
Token %{public}@ failed to create new session, error %{public}@
%{public}@: does not implement decapsulate
%s: %s: CS[%u] deleted (contextDestroyed=%s).\n
answering endpoint for %@
aks_sik_attest(%{public}@, %@) -> %08x
GID-attestKey of unknown key type
Failed to get public key from certificate
%s: %s: returning, err = %ld.\n
%{public}@: card removed
Failed to create AC from data: %{public}@ (AC data: %{public}@)
TKTokenAccessUserPrompt creation failure. Missing framework: 'SpringBoardServices.framework'
Driver shut down all endpoints
Slot %{public}@': failed to end NFC slot session, error:%{public}@
%{public}@: attempted to transmit APDU when no session is opened
token session persists: %{public}d
Failed to recreate TKTokenKeychainItem from attributes: invalid kSecAttrTokenID: %{public}@
Method 'setupWithName' continues
failed to connect to named ctkd port, aborting (probably system shutdown in progress)
invalid objectID used for SEPKey: %@
%{public}@: transmitRequest REQ >>> %{public}@ [%{public}@] %{public}@ %{private}@
%{public}@: connectCardSession:proto=%04x, sensitive=%@
APDU ->%{public}s
Failed to get public key data
%s: %s: returning.\n
%{public}@: got publicKey %@
SIK-attestKey of unknown key type
Failed to end NFC session, error: %@
Tried to end NFC session but it was already deallocated
%{public}@: sleep notification
authentication failed repeatedly: tkid=%{public}@, ac=%{public}@, op=%{public}@
%@ configured with unsupported configuration object %@
T=%d
%{public}@: connectCardSession did only PPS
Checking whether kAKSReturnPolicyError is because of unsatisfied access groups
%{public}@: got idle, but item is revived, ignoring
PIN was set for registered smart card
invoke on token-client connection failed with connection error %{public}@
%s: %s: returning, -> ctx = %p.\n
%{public}@: broadcasting state change %{public}@
Deleting set PIN credential due to tokenID change
with session %{public}@ on token %{public}@
extension %{public}@ instantiating driver class %{public}@
ctk: connecting to slot registration server (%{public}@) failed, error %{public}@
%{public}@: invalidating because of state changed to %ld
%{public}@: got request for used session (%d uses), setting flag to release it ASAP
failed to create shared resource: %{public}@
Failed to get host proxy: %{public}@
%{public}@: invalidating slot and connection %{public}@
%{public}@: client pid %d gone while holding the session, reclaiming it
slot gone
%{public}@: bump/commit finished
%{public}@: connection interrupted, invalidating
%{public}@: new client connection established
%{public}@: delegate returned unsupported protocol 0x%04x, only T=0 or T=1 are supported
syskey %d not supported, attempt to collect it failed, error %08x
LAContext.externalizedContext(sn=%d) failed
Idle callback detected, but slot is already gone, ignoring it
configure token class
SEPClientObject: createKey
provideEndpoint failed with:'%@'
%{public}@: Skipping simulated card reinsertion due to missing card
%{public}@: does not implement key bumping
finished configuring class %{public}@
got notification for new slot: name=%{public}@, ep=%{public}@
%{public}@: an attempt to begin session with invalidated (removed) card
Call 'setupWithName' was postponed, because root's home directory does not exist
unpower FAILED
Failed to create certificate from advertised item of token %{public}@, data: %{public}@
Failed to get attributes from certificate %{public}@
got invalid serverAttributes for key
release token
%{public}@: connected to slot %{public}@
%{public}@ requested systemkey aks_system_key_type_t(%d) not supported by the platform
%{public}@: releasing card session %{public}@
%s: %s: log level set to %d.\n
Slot %{public}@': failed to register, error:%{public}@
operation:%d failed, error: %{public}@
%{public}@: recrypted data
attempt to begin session failed: %{public}@
gsmak not supported, attempt to read its public key failed, error %08x
Unable to connect to %{public}@ even after retries.
ExtClientObject: advertisedItems
%{public}@: sendIns invoked on invalid (removed) card
%{public}@: slot answered session %{public}@ (protocol=0x%04lx, counter=%ld)
%{public}@: used protocol %04x
card in
runningInSystemContext = %d
%{public}@: card reset
SEPClientObject: getKey
%{public}@ %{public}@: an attempt to %{public}s incompatible key
runningInLoginWindowContext = %d
ATR:%{public}s
%{public}@: connect:_state=%d,_power=%d,_proto=%d
%{public}@: computed shared secret
An attempt to release nonexistent token with instanceID=%{public}@
%{public}@: endSession: counter=%ld, someoneWantsSession=%d
Failed to register smartcard, tokenID: %{public}@, error: %@
%{public}@: leaving session, policyLeave
%{public}@: leaving session, policyPowerDown/Eject
User prompt not supported
creating connection to %{public}@, targetUID=%d
Cannot find requested key %{public}@ on token %{public}@
Registered smartcard, tokenID: %{public}@, bundleID: %@
softlink:o:path:/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
softlink:o:path:/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
TKSlotParameters
TKSmartCardUserInteractionForPINOperation
TKTokenKeychainContents
TKTokenConnection
TKSmartCardUserInteractionForSecurePINVerification
TKSmartCardUserInteractionForSecurePINChange
TKSmartCardSlotNFCManaging
TKTokenWatcherProxy
TKProtocolSmartCardSlot
TKProtocolSlot
TKSmartCardTokenSession
TKTokenWatcherTokenInfo
TKTokenAccessDB
NSSecureCoding
TKClientTokenObject
TKProtocolSmartCardSlotNotification
TKProtocolSlotNotification
TKTokenConfigurationConnection
TKSEPClientTokenSession
TKSmartCardATR
TKSEPClientTokenObject
TKTokenAccessUserPrompt
TKSmartCardATRInterfaceGroup
TKTokenSessionConnection
NSExtensionRequestHandling
TKSmartCardSlotManager
TKSmartCardSlotScreen
TKTokenConfigurationProtocol
TKTokenDriverConfiguration
TKAPDULogComponents
TKTokenDriverContext
TKDataSource
TKTokenDriverProtocol
TKSimpleTLVRecord
TKLocalSEPRefKey
TKTokenSmartCardPINAuthOperation
TKTokenKeychainKey
TKXPCConnection
TKProtocolSlotRegistry
TKTokenAccessUserPromptInfo
TKTokenAuthOperation
TKClientTokenServerProtocol
TKRemoteSEPKeyProtocol
TKDataConverter
TKExtensionClientTokenSession
TKSmartCardSlotEngine
TLVDebugUtility
TKToken
PKModularService
TKSmartCardUserInteractionForStringEntry
TKTokenConfiguration
SBSRemoteAlertHandleObserver
TKTokenID
TKSmartCardStateRequest
TKTokenKeyAlgorithm
TKTokenDriverRequest
TKTokenDriverHostProtocol
NSCoding
TKClientTokenProtocol
TKSharedResourceSlot
TKSmartCardTokenRegistrationManager
TKCTKDConnection
TKSmartCardSlotProxy
TKSmartCard
TKClientToken
TKSmartCardTokenDriver
NSObject
TKAnalytics
TKProtocolSmartCardSession
TKXPCConnectionDelegate
TKAsyncOperation
TKTLVRecord
TKPropertyList
NSXPCListenerDelegate
TKLocalSEPSystemKey
TKAPDUFormatter
TKTokenKeyExchangeParameters
TKSmartCardTokenRegistrationXPCClient
TKAuthContext
TKSmartCardToken
TKAPDUCommandAnalyzer
TKTokenDriverDelegate
TKRegisteredTokenManager
TKLocalSEPKey
TKClientTokenAdvertisedItem
TKSharedResource
TKTokenSession
TKProtocolSlotClientNotification
TKSmartCardTokenRegistrationXPC
TKSmartCardWithError
TKPowerMonitor
TKMLDSAPrehasher
TKTokenBaseContext
TKTokenService_Subsystem
TKSEPKey
TKTokenConfigurationChangeProtocol
TKClientTokenSession
TKTokenAccessUserPromptRemoteAlertSB
TKSmartCardUserInteractionForConfirmation
TKTokenDelegate
TKXPCConnectionConfigurationDefault
TKApplicationProxy
TKTokenSessionDelegate
TKUIServerProtocol
TKTokenConfigurationConnectionProxy
TKXPCConnectionDefault
_TKSmartCardSlotReservation
TKTokenKeychainCertificate
TKProtocolTokenWatcherHost
TKTokenAccessRegistry
TKCompactTLVRecord
TKProtocolSlotClient
TKSmartCardPINFormat
TKXPCConnectionConfiguration
TKSmartCardSessionEngine
TKTokenAccessRequest
TKBERTLVRecord
TKSmartCardSlot
TKXPCInterface
TKExtensionClientTokenObject
TKTokenAccessUserPromptNoop
TKTokenAccessDBBackedByUserDefaults
LAProtocolEndpointProviderServer
TKExtensionClientToken
TKError
TKRemoteSEPKey
TKProtocolTokenWatcherServer
TKTokenConfigurationTransaction
TKSEPClientToken
TKAKSParameters
TKTokenPasswordAuthOperation
TKSmartCardUserInteraction
TKSmartCardSessionRequest
TKTokenKeychainItem
TKSmartCardSlotNFCSession
TKTokenWatcher
TKTokenDriver
NSCopying
T@,&,N,V_sac
T@?,C,V_replyFlushedState
_PINLengthBitOffset
_classID
_namedConnection
errorWithDomain:code:userInfo:
setLastUsedRegisteredTokenID:
smartCard
setupConnection
certificateType
addRemovalHandler:forTokenID:
cardPresent:
containingBundleRecord
getKeychainItemsForTokenID:reply:
isCancelled
tlvSummaryFromData:
T@\"NSNumber\",&,V_protocols
tokenID
_accessControlRef
dataWithCapacity:
performSelector:
PINJustification
validateIndefiniteLengthBounds:
T@\"NSData\",&,V_serialNumber
displayMaxLines
remoteAlertHandleDidDeactivate:
stringFromDate:
_promptUserToEvaluateRequest:error:
applicationTag
T@\"NSNumber\",R,N
T@\"NSArray\",R,N,V_keys
_ABC
_clientHasAccessTokenEntitlement
_hasSeparateKeysAndCertificatesObjectIDSpace
_tokenID
attestKeyObject:nonce:error:
callerName
allKeys
T@\"NSData\",R,N,V_bytes
TB,V_result
canPerformKeyExchange:
createObjectBlock
handleApduResponse:body:le:isCase4:synchronous:error:reply:
handleFailureInMethod:object:file:lineNumber:description:
initWithMaxBlockSize:
_locale
T@\"NSObject<OS_dispatch_queue>\",R,N,V_replyQueue
T@\"NSXPCListenerEndpoint\",R,N
_ACMHandle
beginTransactionWithReply:
clientConnectionTerminated:
conformsToProtocol:
decodeObjectOfClasses:forKey:
T#,R
_db
_securePINVerificationSupported
_synchronousRemoteObjectProxy
_vendorID
computeSharedSecret:error:
didChangeValueForKey:
isFinished
Tq,R,V_requestedSize
keychainAttributes
serverConnection
setAPDU:
setAPDUTemplate:
setIdleQueue:
setSlot:
Td,R,N
_AKSRefKey
decodedObjectID:isCertificate:error:
displayMaxCharacters
endSession:reply:
initWithToken:
parseLongFormValueFromDataSource:lengthByte:
runUserInteraction:reply:
_nfcSlotManager
T@\"NSDictionary\",R,N,V_parameters
_lock
deleteObject:error:
inputItems
length
processAccessGroupsOfACLDictionary:intoGroups:callerGroups:
protocols
_connectionLock
T@\"NSArray\",R,N,V_certificates
Tq,V_stateWhenRequested
keyRef
setData:
setDelegateWithControlMethod:
stringRepresentation
tokenConfigurations
T@?,C,N,V_objectDestroyedBlock
canDecrypt
didWakeUpOnEngine:
encodedCertificateID:
initWithBytesNoCopy:length:freeWhenDone:
objectForKeyedSubscript:
securePINVerificationSupported
session:getAdvertisedItemsWithReply:
T@\"NSString\",R,V_tokenID
_clientConnection
configurationConnection
configureWithConfiguration:
copyWithZone:
setCertificateType:
setConfigurationData:
setMaxPINLength:
T@\"TKTokenID\",&,V_tokenID
Tq,V_minPINLength
_stateRequests
characterAtIndex:
setDisplayMaxLines:
setProtocols:
setState:
signWithKey:digest:authContext:forceSystemSession:reply:
T@\"NSString\",R,N,V_clientName
engine:transmit:
setLocalizedPINLabel:
setPhysicalColumnCount:
setupSlotWithReply:
setupWithPublicKey:label:
substringWithRange:
tokenSession:decryptData:usingKey:algorithm:parameters:error:
AKSRefKey
T@\"TKSlotParameters\",R,C,V_slotParameters
T@\"TKSmartCardSessionEngine\",W,V_session
_updatePINInitialStateWithContext:forToken:
activate
clientDisplayName
performKeyExchangeWithPublicKey:usingKey:algorithm:parameters:reply:
retain
T@\"NSArray\",R,C
T@\"NSXPCConnection\",R,N
setAttrib:data:reply:
AID
Tr^v,R
dataFromPtr:
issuer
powerDownWithEject:
setEventName:
token:createSessionWithError:
tokenSession:decapsulateSharedKey:usingKey:algorithm:error:
T@\"NSNumber\",R,N,V_sessionID
preflightStatus
_physicalColumnCount
endpoint
parseFromDataSource:
session:getAttributesOfObjectID:reply:
set
T@\"TKToken\",R,V_token
_objectDestroyedBlock
auditAuthOperation:auditToken:success:
driverConfigurationsWithCTKDConnection:
getTokenEndpointForTokenID:canRequireCardInsertion:reply:
initWithTokenID:
privatePart
T@\"NSData\",R,N
decapsulateSharedKey:usingKey:algorithm:reply:
fetchByte:
result
key
Tq,V_PINBitOffset
_AKSSystemKeyType
_subjectKeyID
getClassIDsWithReply:
numberWithInt:
powerDownIdleTimeout
T@\"NSData\",C,V_APDUTemplate
T@\"NSString\",C,V_label
_connectionIdentifier
forceSystemSession
reserveProtocols:reservationId:exclusive:reply:
setObjectDestroyedBlock:
supportsSecureCoding
tokenSessions
T@\"NSXPCInterface\",R,N
TB,R
driver
setSlot:PINFormat:APDU:currentPINByteOffset:newPINByteOffset:
tokenConfigurationChanged:
T@\"NSData\",C,V_applicationTag
dataUsingEncoding:
deleteKey:authContext:forceSystemSession:reply:
initWithPreflightStatus:
userInteractionForConfirmation
weakObjectsHashTable
_extensionAttributes
apduSentSinceLastReset
initWithInteger:
setContext:
setSubjectKeyID:
_lastId
dateFromString:
commit
debugDescription
previousState
setMaxInputLength:
setServerEndpoint:
T@\"TKSmartCard\",R,N,V_smartCard
_PINBitOffset
_previousState
registeredSmartCardTokens
timeZoneForSecondsFromGMT:
T@\"NSNumber\",&,V_certificateType
T@\"TKCTKDConnection\",&,N
T@\"TKToken\",R,N,V_token
authenticationError
externalizedContext
password
providerBundleID
satisfiesKeyUsage:
T@\"NSObject<OS_dispatch_queue>\",&,V_powerRequestsQueue
T@\"TKTokenKeychainContents\",&,V_keychainContents
_accessDB
endNFCSlotWithError:
evaluateAccessControl:forOperation:error:
setNFCAllowedAIDs:
sharedResource
synchronous
_displayMaxLines
addTokenConfigurationForTokenInstanceID:
setObject:forKeyedSubscript:
setValue:forKey:
slotRegistryWithErrorHandler:
tokenInfoForTokenID:
transmitChunkedIns:p1:p2:data:fromOffset:realLe:chained:isCase4:reply:
T@\"NSString\",R,N,V_driverName
_protocols
_remoteObjectProxy
countByEnumeratingWithState:objects:count:
scheduleIdlePowerDown
sendControl:data:expectedLength:reply:
setSlotWithName:endpoint:type:reply:
setSuitableForLogin:
T@,&
Tq,V_PINBlockByteLength
_keyID
delegate
fetchStoredInstallationIDForBundleID:
pivContainerNames
unregisterSmartCardWithTokenID:callerBundleID:error:
updateTokenID:data:reply:
PINCompletion
TQ,V_allowedProtocols
_advertisedItems
_clients
_endPolicy
allValues
connection
doubleValue
handlesTokenID:
T@\"NSString\",C,V_localizedPasswordLabel
T@,R,N,V_exportedObject
_remoteObjectInterface
_stateWhenRequested
lastUsedRegisteredTokenID
physicalRowCount
setCurrentProtocol:
_providerBundleID
initWithSlotParameters:
isSuitableForLogin
providerDisplayName
setActiveStateNotifications:
setRegisteredTokenManager:
TB,V_canSign
_fetchAccessForRequest:
decapsulate:algorithms:parameters:error:
initWithSlotName:nfcSlotManager:
releaseSessionWithReply:
setClasses:forSelector:argumentIndex:ofReply:
setSubject:
set_testing_noAutomaticReconnect:
T@\"NSString\",C,N,V_eventName
UTF8String
_configurationConnection
_extensionAuxiliaryVendorProtocol
beginTransaction
endUsing:
isEqual:
stringWithUTF8String:
T^{__SecAccessControl=},R,N
Td,V_initialTimeout
Tq,N,V_preflightStatus
_error
_removalHandlers
destroyObject
hasPrefix:
initWithCertificate:objectID:
_displayMaxCharacters
_pinValidationCondition
_privatePart
engineSimulateCardReinsertion:
setLength:
setTimeZone:
slotParameters
unsignedIntegerValue
charset
T@\"NSString\",R,N
_authContext
commandNameForIns:
control:data:expectedLength:reply:
data
removeTokenConfigurationForTokenInstanceID:
setExtensionAttributes:
T@\"NSData\",R,N,V_remoteKeyID
T@\"NSXPCConnection\",R,N,V_clientConnection
T@\"TKTokenID\",R,N,V_tokenID
_AKSSystemKeyGeneration
_auxiliaryConnection
connectToEndpoint:synchronous:reply:
copy
initWithAccessDB:userPrompt:
_initWithAuthContext:caller:
bundleWithIdentifier:
initWithMachServiceName:options:
localizedPasswordLabel
setAccessControl:
setActive:
setPublicKeyHash:
setVirtualColumnCount:
_initWithObjectID:authContext:caller:isIDUnknown:error:
importOperation:
setKeySizeInBits:
set_testing_AuthenticateInternally:
signData:usingKey:algorithm:reply:
T@\"NSData\",R,C,D
T@\"NSXPCConnection\",R,N,V_tokenConnection
_PINFormat
initialKeepAlives
publicKeyWithError:
tokenDriver:terminateToken:
tokenSession:supportsOperation:usingKey:algorithm:
setAuthContext:
_delegateWithEscapeMethod
_smartCard
operationMap
setInterface:forSelector:argumentIndex:ofReply:
superclass
session
configurationData
displayNameForBundleID:
initWithObjectID:authContext:forceSystemSession:error:
parseFromDataSource:error:
protectionForKeyClass:
userInteractionForSecurePINVerificationWithPINFormat:APDU:PINByteOffset:
T@\"NSString\",R,N,V_tokenID
_useCommandChaining
correlationID
evaluateAuthOperation:tokenOperation:retry:reply:
integerValue
userInfo
T@\"NSString\",R,N,V_name
T@\"NSHashTable\",R,V_cards
T@\"NSXPCInterface\",R,N,V_exportedInterface
setLocale:
set_testing_AuthContextUsed:
valueForEntitlement:
decodedKeyID:error:
T@\"NSNumber\",&,V_maxPINLength
PINLengthFormatWithError:
T@\"NSDictionary\",C,V_constraints
T@\"NSXPCInterface\",&,N,V_exportedInterface
_cla
appendString:
bytesSafeToRead:
bytes
reportChangesForSlotType:reply:
categoryForCla:ins:p1:p2:
initWithSession:key:error:
parseValueFromDataSource:
setCurrentPINByteOffset:
zone
_slotParameters
appendBytes:length:
beginUsing:withBundle:
evaluateAccessControl:forOperation:reply:
lengthOfBytesUsingEncoding:
slot
delegateWithEscapeMethod
T@\"NSNumber\",&,V_displayMaxLines
T@\"NSArray\",&,V_PINMessageIndices
attestKey:usingKey:nonce:reply:
T@\"NSData\",R,C,V_sharedInfo
appendData:
baseClassForUI
parseIndefiniteLengthValueFromDataSource:nestingLevel:
T@\"NSData\",&,V_APDU
T@\"NSXPCConnection\",R,N,V_connection
T@,&,N,V_keepAlive
_resource
alloc
attributes
initWithTokenAccessRequest:
initialKeepAlive
T@\"<TKTokenSessionDelegate>\",W,V_delegate
setXpcEndpoint:
boolValue
hashTableWithOptions:
historicalRecords
sequenceOfRecordsFromData:nestingLevel:
setKeepAlive:
setWasPINCredentialProvidedByPINUI:
T@\"NSData\",R,C,V_data
T@\"NSXPCListenerEndpoint\",R,N,V_configurationEndpoint
T@\"TKTokenConfigurationConnection\",R,N
canUseSEPLocally
clientConnection
minPINLength
registerSmartCardWithTokenID:promptMessage:error:
setInitialTimeout:
registerForConfigurationChange:
tokenConnection
TB,V_securePINVerificationSupported
Td,N,V_idleTimeout
initWithCaller:tokenID:extension:
setKernelPort:
token
T@\"NSString\",R,V_name
infoDictionary
setInsertionHandler:
updateNFCSlotUIMessageWithMessage:slotName:reply:
T@\"NSData\",&,V_publicKeyHash
_LAContext
_connectionToServer
_keychainContents
startRequestWithError:
stringWithFormat:
_testing_AuthenticateInternally
_configurationConnections
error:withAKSReturn:ACMHandle:AKSOperation:params:message:
initWithPublicKey:label:objectID:canSign:canDecrypt:canPerformKeyExchange:
insertObject:atIndex:
keychainItems
setInitialKeepAlive:
classID
delegateWithControlMethod
fetchAccessForRequest:
isDaytona
setReply:
interfaceForChangeProtocol
requestedSize
retainCount
tokenSession:performKeyExchangeWithPublicKey:usingKey:algorithm:parameters:error:
T@\"TKTokenDriverContext\",W,N,V_context
Tq,V_maxInputLength
_accessControl
_data
_historicalBytes
floatValue
interfaceGroupForProtocol:
remoteAlertHandle:didInvalidateWithError:
TI,V_kernelPort
createTokenConfigurationWithInstanceID:persistent:
providerName
setRemoteObjectInterface:
T@\"LAContext\",&,N,V_authContext
_initWithObjectID:authContext:forceSystemSession:error:
evaluateRequirementIgnoringAccessGroups:
remoteObjectProxyWithErrorHandler:
_someoneWantsSession
_suitableForLogin
deleteObject:reply:
ensureSessionWithClient:connectionIdentifier:error:
finishWithError:
value
T@\"NSData\",R,N,V_objectID
_initWithTokenID:
attestWithKey:keyToAttest:nonce:authContext:forceSystemSessionAttestingKey:forceSystemSessionKeyToAttest:reply:
finish
interfaceForSlotClient
registeredSmartCardsWithCompletion:
PINBlockString
setUseCommandChaining:
__testing_AuthenticateInternally
class
getTokenIDsForClassID:reply:
initWithSession:objectID:attributes:
isCredentialSet:
physicalColumnCount
setExportedInterface:
slotInitialized
TB,N,V_authenticateWhenNeeded
_clearCredentialIfNeededForTokenID:inContext:
allowedProtocols
initLocalWithObjectID:authContext:caller:forceSystemSession:error:
processServerAtributes:error:
numberWithBool:
_initialTimeout
decodeObjectOfClass:forKey:
isNFCSupportedWithReply:
setCertificateEncoding:
tag
_executing
_getReservationId
_virtualColumnCount
attestKey:nonce:error:
createNFCSlotWithMessage:completion:
initWithTokenID:configurationConnection:
keychainItemWithInfo:
TQ,V_activeStateNotifications
_queuedParameters
_reservationId
lastPathComponent
logWithBytes:handler:
protocol
setResultSW:
setSecurePINChangeSupported:
initWithTokenID:ctkdConnection:
_storeInstallationID:forBundleID:
endSession
isNFCSupported
mutableBytes
remoteObjectProxy
setSac:
T@\"NSString\",?,R,C
_idleQueue
currentHandler
isExecuting
setUserInfo:
initWithTokenDriver:instanceID:
_requestedSize
endpointForToken:
setIssuer:
setPINConfirmation:
T@\"NSData\",&,V_subject
T@\"TKSmartCardSlotManager\",R
_initialKeepAlives
fillWithItems:
setSerialNumber:
systemKey
PINLengthBitSize
_callerPID
_certificates
exclusive
initWithRemoteObjectInterface:exportedInterface:exportedObject:replyQueue:
initWithWatcher:
interfaceForXPCProtocol:
releaseTokenWithInstanceID:
solePersonality
Tq,V_charset
_errorWithCode:userInfo:
_publicKeyData
_sessions
_storeAccess:forRequest:
numberWithUnsignedLong:
reserveExclusive:reply:
Tq,V_state
_sessionID
bumpKey:reply:
distantPast
initWithTokenID:serverEndpoint:targetUID:
replyQueue
setCtkdConnection:
T@,R,C,V_objectID
TB,V_apduSentSinceLastReset
Td,V_powerDownIdleTimeout
Tq,V_PINLengthBitOffset
canRequireCardInsertion
maskedDataDescriptionForIns:p1:p2:command:
serialNumber
setPinValidationCondition:
ATR
T@\"NSString\",C,V_PIN
_reply
setMinPINLength:
end
T@\"NSObject<OS_dispatch_queue>\",&,N,V_idleQueue
T@\"TKSmartCardSlotProxy\",R,N,V_proxy
_platformAllowsAllRequests
_session
addOperation:
stateWhenRequested
_awaken
_changeStateTo:forClient:
_sac
enumerateKeysAndObjectsUsingBlock:
startWatchingWithReply:
subjectKeyID
synchronous:remoteSlotWithErrorHandler:
keySize
Tq,V_encoding
_resultData
buildIns:p1:p2:data:range:le:protocol:chained:extended:realLe:
initWithItemInfo:
interfaceForProtocol
setSensitive:
simulateCardReinsertionWithReply:
TA
TS,V_resultSW
__testing_ForceAuthenticationNeeded
_objectID
connectionDidActivate:
hasSuffix:
initWithEndpoint:error:
T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue
T@\"NSString\",R,N,V_privatePart
_localizedString:value:
_tokenInfos
callerHasEntitlement:error:
arrayWithArray:
T@\"LAContext\",&,N,V_LAContext
_prompt
_keychainAttributes
_state
date
initWithConfiguration:
T@\"NSDictionary\",R,N,V_keychainAttributes
T@\"NSString\",&,V_firmwareVersion
_APDUTemplate
processNotificationParameters:
session:objectID:operation:data:algorithms:parameters:reply:
setProprietaryCardUsage:
T@\"TKCTKDConnection\",R,N,V_ctkdConnection
_currentProtocol
_eventName
_sharedInfo
getDictionaryParameters
getSlotWithName:reply:
setCanPerformKeyExchange:
subdataWithRange:
_cardReinsertionSimulationCallInterval
numberWithUnsignedInteger:
shareState
setCla:
_powerDownIdleTimeout
_tokenConnections
arrayWithCapacity:
invalidate
replyFlushedState
dataWithLength:
TB,V_active
_certificateType
_transmitting
description
removeAllObjects
setApduSentSinceLastReset:
setCallerPID:
TQ,R,N,V_tag
_items
_serverConnection
numberWithDouble:
setKeychainItems:
setLabel:
simulateCardReinsertionWithError:
stringWithCapacity:
PINByteOffset
T@\"NSData\",R,N,V_ACMHandle
historicalBytes
raise:format:
PINFormat
initWithServer:
T@\"NSString\",R,N,V_clientBundleID
T@\"TKSmartCardTokenRegistrationManager\",R
activeStateNotifications
idleTimeout
setResult:
array
setVirtualRowCount:
T@,R,N,V_keyID
_parameters
_registrationConnection
sessionID
willSleepOnEngine:
T@\"NSArray\",R,N
builtinTokenIDs
T@\"NSMapTable\",R,N,V_sessions
T@\"TKSharedResourceSlot\",&,N,V_keepAliveResourceSlot
_kernelPort
_password
validateSendInsPreconditionsWithError:
PINFormatStringWithError:
initWithLAContext:ACMHandle:sharedResource:
locale
proxy
T@\"NSDictionary\",&,N,V_parameters
addSlotWithEndpoint:name:type:reply:
null
transmit:reply:
TB,V_delegateWithEscapeMethod
bumpKeyWithError:
defaultManager
extensionAttributes
sessionWithParameters:reply:
_ctkdConnection
T@,&,N,V__testing_AuthContextUsed
_lastCardReinsertionSimulationCallTime
cancelRequestWithError:
computeSharedSecretWithKey:publicKey:authContext:forceSystemSession:reply:
objectForObjectID:error:
publicKeyHash
setProtocol:
_apduQueue
_configuration
parseWithY:toProtocol:fromSource:hasNext:
send
setCanSign:
setReplyFlushedState:
setSecurePINVerificationSupported:
recordFromData:
T@\"<TKXPCConnectionDelegate>\",W,N
T@\"NSNumber\",&,V_productID
_installationKeyForBundleID:
_localizedPasswordLabel
_testing_noAutomaticReconnect
driverName
initWithClassID:instanceID:
_handle
encodedObjectID
T@\"TKSharedResource\",R,N,V_sharedResource
_canRequireCardInsertion
_delegate
_dumpPlist:into:
encodeObject:forKey:
initWithListenerEndpoint:
TB
_forceSystemSession
_setQueue:
initWithParameters:
initWithSlot:
localizedStringWithFormat:
maxInputLength
readDataForTokenID:reply:
TQ,R,N
Tq,V_currentPINByteOffset
interfaceForSmartCardTokenRegistration
keyClassForProtection:
leaveSession:
securePINChangeSupported
set_testing_ForceAuthenticationNeeded:
tokenDriver:createTokenForSmartCard:AID:error:
_caller
cla
_listener
isMemberOfClass:
parseTagFromDataSource:tag:
removeTokenID:reply:
sendEscape:reply:
setPINByteOffset:
Tq,V_shareState
T@\"NSNumber\",&,V_minPINLength
T@\"NSXPCConnection\",R,N,V_caller
anonymousListener
endTransactionWithReply:
initWithSession:keychainAttributes:secRef:
numberWithUnsignedInt:
setPINJustification:
hasEntitlement:
_extensionBundle
_shareState
engine:setAttrib:data:attribNotSupported:
systemLocale
sac
dataWithBytes:length:
setReplyNextState:
setSession:
strongToWeakObjectsMapTable
_powerRequestsQueue
endRequest
initWithSlot:connection:
insertedToken:
T^{__SecCertificate=},R,N
_localizedPINLabel
_publicKeyHash
_sensitiveRequired
bundleIdentifier
dictionaryWithObjects:forKeys:
keepAliveResourceSlot
kernelPort
_PINJustification
_displayNamesCache
ensureConnectionCanRequireCardInsertion:error:
initWithCoder:
objectDestroyedBlock
suitableForLogin
virtualColumnCount
_PINMessageIndices
_createObjectBlock
_creatorAuditToken
_formatHexData:to:
domain
initWithCard:error:
initWithTokenConnection:
newHandleWithDefinition:configurationContext:
driverConfigurationsWithClient:
T@\"NSString\",R,N,V_providerDisplayName
evaluateRequest:error:
removeObjectForKey:
slotName
unregisterSmartCardWithTokenID:error:
_constraints
decryptData:usingKey:algorithm:parameters:reply:
fetchByte
indexSet
sendIns:p1:p2:data:le:sw:error:
currentPINByteOffset
base64EncodedStringWithOptions:
T@\"<TKTokenSessionPrivateDelegate>\",R,N
_handleConnectionClose
code
hasSEP
identifier
initWithCTKDConnection:
initWithTag:records:
T@\"TKSmartCardSlot\",R,N,V_slot
formattedAPDUResponseComponents:sw:options:
isEqualToString:
object
resultData
setCharset:
setSessionEndPolicy:
tokenDriver
_accessRequest
endNFCSlotWithName:reply:
hexStringFromData:
initForPlugInKit
T@\"NSArray\",C,N
T@\"LAContext\",R,N,V_authContext
_configurationEndpoint
initWithAlgorithmsArray:
queue
recryptWithKey:data:attributes:authContext:forceSystemSession:reply:
reply
_issuer
formattedAPDUCommandComponentsFromRawAPDU:options:
runWithReply:
_clientBundleID
dataFromHexString:
notifyWithParameters:reply:
setLAContext:
wasPINCredentialInitiallySet
PINMaxExtraDigit
_encoding
encodedAccessGroups
keyUsage
registerObserver:
resultSW
setCanDecrypt:
setInteractionTimeout:
TB,V_delegateWithControlMethod
_PINByteOffset
_remoteKeyID
numberWithUnsignedLongLong:
removedToken:
setPresentationTarget:
setShareState:
T@\"NSData\",R,N,V_data
T@\"NSDictionary\",R
T@\"NSString\",R,V_stringRepresentation
T@\"NSDictionary\",&,V_parameters
TQ,V_PINCompletion
_queue
fillPIN:intoAPDUTemplate:PINByteOffset:error:
setPassword:
TB,V_canDecrypt
T@\"NSMutableDictionary\",R,N,V_sessions
T@,&,N
beginRequestWithExtensionContext:
contextForKey:
objectAtIndex:
signDigest:attributes:error:
transmitRequest:synchronous:logActivity:reply:
T@\"NSLocale\",&
_debugID
_preflightStatus
_valid
sleepForTimeInterval:
T@?,C,N,V_createObjectBlock
Tq,V_previousState
_PINBlockByteLength
zuluDateFormatter
T@\"<TKTokenDriverDelegate>\",W,V_delegate
TQ,V_PINConfirmation
_initWithAuthContext:
creatorAuditToken
initWithName:
T@\"TKClientTokenSession\",R,N,V_session
TB,N,V__testing_ForceAuthenticationNeeded
_tokenConnection
engine:powerDownWithEject:
name
windowsLocaleCodeFromLocaleIdentifier:
canSign
_maxOutputLength
setSmartCard:
synchronous:remoteSlotClientWithErrorHandler:
systemSessionKey
PIN
T@\"NSData\",R,C
T@\"NSData\",R,N,V_publicKey
T@,&,N,V_initialKeepAlive
_maxPINLength
_value
exportedObject
initForPlugInKitWithOptions:
maxOutputLength
_ptr
engine:runUserInteraction:error:
isEqualToData:
nextObject
remoteAlertHandleDidActivate:
removeObjectAtIndex:
setEndPolicy:
LAContext
T@\"NSString\",R,N,V_publicPart
APDUTemplate
currentLocale
getInstallationIDFromBundleID:
isAvailable
listener
parameters
T@\"NSArray\",R
isProxy
T@\"TKSmartCardATR\",&,V_ATR
TB,N,V__testing_AuthenticateInternally
Tr*,R,V_ptr
createObjectWithAttributes:error:
serverEndpoint
setPINLengthBitSize:
_beginSessionQueue
cancel
hash
instanceID
setPreviousState:
T@\"NSDictionary\",R,C,N
T@\"NSMutableDictionary\",R,C,D
setWithObjects:
_testing_AuthContextUsed
beginAuthForOperation:constraint:reply:
canDecrypt:
decapsulateKey:error:
encodedKeyID:
addObject:
certificateForObjectID:error:
engineResetCard:
initWithBytes:length:encoding:
localeID
promptUserToEvaluateRequest:error:
releaseResourceImmediatelly:
setPINBlockByteLength:
TB,R,N
initWithInsertionHandler:
isEndOfContentMarkerAtSource:
lastObject
maxPINLength
startNFCSlotWithName:uiSheetMessage:supportedAppIdentifiers:reply:
Tq,V_maxOutputLength
_providerDisplayName
auditToken
commitKeyWithError:
dictionaryWithObjects:forKeys:count:
valid
_coreServicesLocalizedNameForBundleID:
driverConfigurations
encodeWithCoder:
initWithBytes:
tokenSession:attestKey:usingKey:nonce:error:
__testing_AuthContextUsed
_wasPINCredentialInitiallySet
T@\"NSXPCListenerEndpoint\",&,V_serverEndpoint
Tq,V_maxPINLength
cards
ctkdConnection
encodeNumber:into:
initLocalWithKeyType:keySize:accessControl:options:authContext:caller:forceSystemSession:error:
setDateFormat:
_exclusive
_key
changeStateTo:powerState:
clientBundleID
configureWithReply:
deleteWithError:
keySizeInBits
tokenSession:decryptData:usingKey:algorithm:error:
_ATR
_atr
_callerName
_delegateWithControlMethod
_token
configuration
endSessionWithReply:
storeInstallationID:forBundleID:
T@\"<TKTokenDelegate>\",W,V_delegate
errorWithResult:operation:forError:
_certificateEncoding
_driverName
addEntriesFromDictionary:
localeIdentifier
newPINByteOffset
powerState
stringByReplacingOccurrencesOfString:withString:
tokenSession:supportsOperation:usingKey:algorithm:parameters:
PINLengthBitOffset
TB,V_securePINChangeSupported
Tq,V_physicalColumnCount
_grantedAccess
_serialNumber
bundleRecordWithBundleIdentifier:allowPlaceholder:error:
callerPID
getSmartCardWithError:
T@\"NSData\",C,N
T@\"NSData\",R,N,V_value
T@\"NSXPCListener\",R,N,V_listener
arrayByAddingObject:
engine:control:data:expectedLength:
eventName
initWithConfigurationConnection:
operation:data:algorithms:parameters:error:
T@\"NSData\",R,V_AID
T@\"NSNumber\",&,V_certificateEncoding
T@\"NSNumber\",&,V_pinValidationCondition
Tq,V_physicalRowCount
communicationsFailed:
evaluatePolicy:options:reply:
initWithProtocol:
keyID
T@\"NSData\",R,N,V_historicalBytes
TB,N,V_proprietaryCardUsage
_keySizeInBits
_keys
_label
_physicalRowCount
_resultSW
_setupWithName:delegate:
_authenticateWhenNeeded
_synchronous
_targetUID
accessControl
autorelease
dataForTag:
objectForKey:
respondsToSelector:
_synchronousRemoteObjectProxyWithErrorHandler:
initWithEventName:
isValidWithError:
performSelector:withObject:withObject:
prefixForCategory:
setCredential:type:
sharedInfo
tokenSession:attributesOfObject:error:
TB,V_exclusive
decrypt:algorithms:parameters:error:
localizedName
reset
setAllowedProtocols:
setAwaken:
setPINBitOffset:
setPreflightStatus:
T@\"NSNumber\",R,N,V_protocol
TB,N,V__testing_noAutomaticReconnect
Tq,R,N
interactionTimeout
keepAlive
session:evaluateAccessControl:forOperation:reply:
setContext:forKey:
tokenConnections
_driver
T@\"TKTokenID\",R,N
T^{__SecIdentity=},R,N
_bytes
active
certificateForKey:
currentConnection
dictionaryRepresentation
_serverEndpoint
canSimulateCardReinsertion
evaluateAuthOperation:tokenOperation:reply:
setEncoding:
start
string
tokenSession:deleteObject:error:
T@\"<TKSmartCardUserInteractionDelegate>\",W,V_delegate
Tq,V_endPolicy
Tq,V_virtualColumnCount
_clientName
provideEndpoint:uid:reply:
signDigest:error:
updateKeychainItemsForTokenID:items:reply:
withSessionID:invoke:
_authenticationError
arrayByAddingObjectsFromArray:
boolForKey:
removeObjectsAtIndexes:
updateNFCSlotMessageWithMessage:error:
T@,R,N
observeValueForKeyPath:ofObject:change:context:
registerSmartCardWithTokenID:promptMessage:callerBundleID:error:
terminate
tokenSession:signData:usingKey:algorithm:error:
setATR:
_AID
waitForStateFlushedWithReply:
setSynchronous:
T@\"NSXPCConnection\",W,V_connection
_idleTimeout
_keepAlive
_testing_stateDelay
_useExtendedLength
localizedStringForKey:value:table:
stringByAppendingString:
T@\"NSNumber\",&
_block
_proxy
getAttributesOfKey:authContext:forceSystemSession:reply:
notifyOperation:forToken:withStatus:
parseShortFormValueFromDataSource:length:
resourceWithError:
self
Tq,V_PINLengthBitSize
_firmwareVersion
_tokenDriver
defaultMonitor
getTokenConfigurationEndpointWithReply:
productID
tokenFromAuditToken:
ACMHandle
T@\"NSError\",C,V_authenticationError
_setTargetUserIdentifier:
ensureSlotWatcherRunningWithReply:
initWithClassID:configurationConnection:
keychainClass
processObjectCreationAttributes:authContext:error:
sendIns:p1:p2:data:le:reply:
parseValueFromDataSource:nestingLevel:
pinValidationCondition
remoteObjectInterface
setApplicationTag:
_powerState
initWithTokenID:error:
setup
release
T@\"NSObject<OS_dispatch_queue>\",R
T@\"NSMutableDictionary\",R,N,V_tokenConnections
_exportedInterface
caller
parseFromDataSource:nestingLevel:
setParameters:
setPublicKeyData:
awaken
dictionaryWithDictionary:
getAdvertisedItemsWithReply:
publicKey
setPowerDownIdleTimeout:
setupWithName:delegate:
setDisplayMaxCharacters:
setUnderlyingQueue:
setUseExtendedLength:
sign:algorithms:parameters:error:
_sensitive
label
T@\"TKTokenConfiguration\",R,V_configuration
_idleTimer
_publicPart
decodedCertificateID:error:
inSessionWithError:executeBlock:
_sessionCounter
accessControlForConstraints:tokenID:error:
commitKey:reply:
_replyNextState
T@\"NSData\",R,N,V_accessControl
virtualRowCount
_name
_queueManager
sharedInstance
canSign:
T@\"NSData\",&,V_issuer
T@\"TKSmartCardPINFormat\",&,V_PINFormat
T@\"TKTokenID\",R,V_tokenID
buildPayload
setWasPINCredentialInitiallySet:
_authenticationContextWasProvidedByCaller
_replyFlushedState
_weakConfigurationConnection
accessControlRef
bundleID
items
transmitRequest:synchronous:reply:
localizedPINLabel
PINConfirmation
T@\"NSDictionary\",R,N
T@\"TKTokenConfiguration\",R
_PINConfirmation
_correlationID
_remoteAlertHandle
addIndex:
userInteractionForSecurePINChangeWithPINFormat:APDU:currentPINByteOffset:newPINByteOffset:
T@\"NSData\",C,V_publicKeyData
_charset
isGibraltar
releaseTokenWithInstanceID:reply:
setInterruptionHandler:
setResultData:
setSlot:PINFormat:APDU:PINByteOffset:
addObserver:forKeyPath:options:context:
createTokenWithSlot:AID:proprietaryCardUsage:error:
encoding
interfaceGroupAtIndex:
_sharedResource
withError:accessControl:invoke:
__testing_noAutomaticReconnect
_virtualRowCount
handleErrorForRegisteredSmartcards:forToken:
listener:shouldAcceptNewConnection:
longLongValue
sessionWithLAContext:error:
Tq,V_powerState
_shouldAutomaticallyAllowRequest:
_tokenManager
mapTableWithKeyOptions:valueOptions:
setAccessDB:
storeAccess:forRequest:
terminateWithReply:
valueForKey:
setMaxConcurrentOperationCount:
_minPINLength
setConfigurationEndpoint:reply:
_allowedProtocols
_writeNumber:into:bitOffset:bitLength:
dataWithBytesNoCopy:length:
keys
_active
T@\"<TKSmartCardSlotEngineDelegate>\",W,V_delegate
Tq,V_PINJustification
_PINCompletion
_slotName
appendFormat:
enumerateObjectsUsingBlock:
setConnection:
T@\"NSArray\",R,N,V_identities
_PIN
_sessionIDCounter
dictionaryForState:
sequenceOfRecordsFromData:
setName:
setValid:
waitForNextState:reply:
T@\"NSString\",&,V_result
PINMessageIndices
T@\"NSDictionary\",R,C
createObjectWithAttributes:reply:
.cxx_destruct
_canPerformKeyExchange
_canSign
getValidAIDsFromCallingBundle
initWithAttributes:authContext:forceSystemSession:error:
setFirmwareVersion:
APDU
PINBitOffset
_stateLock
getAttributesOfObject:isCertificate:reply:
publicPart
querySessionSynchronous:reply:
setNewPINByteOffset:
errorWithCode:debugDescription:
setExclusive:
supportsAlgorithm:
tokenSession:bumpKey:error:
_object
_finished
initWithToken:LAContext:parameters:tokenManager:error:
setMaxOutputLength:
_initWithObjectID:authContext:caller:forceSystemSession:error:
initWithTargetPredicate:
T@\"NSString\",R,C,N,V_slotName
_providerName
exportedInterface
sessions
setDelegate:
tokenSession:commitKey:error:
_applicationTag
T@\"TKSmartCard\",&,V_smartCard
TB,R,N,V_clientHasAccessTokenEntitlement
checkAPDUResponse:error:
dataWithData:
formattedAPDUResponseComponentsFromRawResponse:options:
getEndpoint:
pivContainerNameForTag:
Td,V_interactionTimeout
_watcher
performSelector:withObject:
session:createObjectWithAttributes:reply:
_apduSentSinceLastReset
_contexts
clearAllAccessRecords
identityRef
_encoded
initWithTag:value:
registerSmartCardWithTokenID:promptMessage:callerBundleID:completion:
T@\"NSString\",R,N,V_providerName
setAuthenticationError:
unregisterSmartCardWithTokenID:callerBundleID:completion:
T@\"NSString\",R,N,V_providerBundleID
_localizedString:
finalizeAuthOperation:evaluatedAuthOperation:reply:
initialTimeout
sessionEndPolicy
slotNames
initWithPublicPart:privatePart:
_findReservation:connection:
commandNameForCla:ins:
setPINCompletion:
userInteractionForStringEntry
createTokenID:persistent:reply:
T^{aks_ref_key_s=},R,N,V_AKSRefKey
beginRequest
getConfigurationEndpoint:
setPowerRequestsQueue:
setTokenID:
clientHasAccessTokenEntitlement
_parentCard
_replyQueue
archivedDataWithRootObject:requiringSecureCoding:error:
configurationProtocol
initWithSmartCard:AID:instanceID:tokenDriver:
setVendorID:
T@\"NSString\",R,N,V_slotName
decapsulateWithKey:encapsulatedKey:authContext:forceSystemSession:reply:
evaluateAccessControl:aksOperation:options:error:
setKeyType:
setData:forKey:
T@\"NSNumber\",&,V_vendorID
T@\"TKSmartCard\",R
TB,V_canPerformKeyExchange
_stringRepresentation
constraints
defaultService
isAlgorithm:
keybagHandleForceSystemSession:
T@\"TKTokenDriver\",R,N,V_driver
T@?,C,V_replyNextState
Tq,V_virtualRowCount
_cards
arrayWithObjects:count:
objectID
slotNamed:
T@\"TKClientToken\",R,N,V_token
TQ,V_currentProtocol
_connectionWithErrorHandler:
plugInDictionary
setContextErrorHandler:
T@\"NSString\",C,V_keyType
T@\"LAContext\",R,N,V_LAContext
initWithSource:
T@\"TKSEPKey\",R,N,V_key
_PINLengthBitSize
_sessionRequests
authContextWithError:
inSlotQueueExecuteBlock:synchronous:
setConstraints:
T@\"NSXPCConnection\",R,W,N,V_connection
_driverConfigurationsWithConnection:
_setupDriver
initWithTag:value:data:
interfaceForSlotClientNotification
setShouldDismissOnUILock:
setBool:forKey:
_APDU
_proprietaryCardUsage
componentsSeparatedByString:
initWithPropertyList:
objectID:operation:inputData:algorithms:parameters:reply:
timeIntervalSinceDate:
_interfaces
_isPersistenceEnabled
calculateChunkInfoForIns:data:offset:chained:isCase4:
keyForObjectID:error:
unreserve
T@\"NSData\",&,V_subjectKeyID
configurationForTokenID:
engine:setProtocol:
getAttrib:reply:
revalidate
setDelegateWithEscapeMethod:
setObject:forKey:
setProductID:
firmwareVersion
setIdleTimeout:
T@,&,N,V_exportedObject
_securePINChangeSupported
authenticateWhenNeeded
token:terminateSession:
T@\"TKTokenConnection\",R,N,V_tokenConnection
T@?,C,V_reply
_idlePowerDownSource
_sessionEndPolicy
beginSessionWithError:
fetchDataWithLength:
isKindOfClass:
propertyList
T@\"NSXPCInterface\",R,N,V_remoteObjectInterface
_hasSession
_initWithKeyType:keySize:accessControl:options:authContext:caller:forceSystemSession:error:
clientName
initWithTokenInfo:
parseFromSource:
setCreateObjectBlock:
setLocalizedPasswordLabel:
T@\"NSData\",&,V_resultData
_notifyToken
formattedAPDUCommandComponentsClass:ins:p1:p2:command:le:options:
initWithEndpoint:
acquireTokenWithInstanceID:reply:
activateWithContext:
removeObject:
setStateWhenRequested:
updateWithMessage:error:
_startListening
T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},R,N
Tq,V_newPINByteOffset
initWithServiceName:viewControllerClassName:
installSessionIdentifier
remoteSessionWithErrorHandler:synchronous:
setCreatorAuditToken:
tokenIDs
_nfcAppIdentifiers
interfaceWithProtocol:
publicKeyData
setQueue:
stringWithString:
substringToIndex:
_secRef
_connection
_testing_ForceAuthenticationNeeded
categoryForIns:p1:p2:
generateKeyType:keySize:accessControl:options:authContext:forceSystemSession:reply:
parametersWithACMHandle:
setKeychainContents:
_endpoint
configurationEndpoint
initWithConnection:
withError:invoke:
containsObject:
removeAllTokens
removeObserver:forKeyPath:
session:deleteObjectWithObjectID:reply:
setNumber:forKey:
startWatching
useCommandChaining
_endpoints
_initialKeepAlive
_slot
certificateRef
identities
initWithBlock:
initWithBundleIdentifier:allowPlaceholder:error:
mainBundle
subject
_extensionAuxiliaryHostProtocol
Tq,V_PINByteOffset
_keySize
cardSessionRequested
initForReadingFromData:error:
willChangeValueForKey:
_params
T@\"NSData\",C,V_publicKeyHash
T@\"NSString\",R,C
removeAccessForBundleID:matchPartial:
sensitive
setPINLengthBitOffset:
TB,N,V_canRequireCardInsertion
_localizedShortName
certificates
setCardReinsertionSimulationCallInterval:
T@\"NSString\",C,V_password
setPIN:
TB,N
_publicKey
displayMessage:x:y:duration:clearScreen:
indexOfObject:
setAuthenticateWhenNeeded:
setInvalidationHandler:
ptr
_connectionWithCTKDConnection:
acquireTokenWithSlot:AID:proprietaryCardUsage:reply:
initWithObjectID:
lifetimeControlKey:type:authContext:forceSystemSession:reply:
predicateForProcess:
T{?=[8I]},N,V_creatorAuditToken
T@\"NSDictionary\",&,V_extensionAttributes
T@\"NSString\",C,V_localizedPINLabel
T@\"NSNumber\",&,N,V_callerPID
suspend
T@\"TKTokenDriver\",R,V_tokenDriver
TC
_initWithToken:LAContext:parameters:error:
T@\"NSData\",R
_algorithms
_keepAliveResourceSlot
_keychainItems
_wasPINCredentialProvidedByPINUI
hasSystemKey:ACMHandle:
indexOfObjectPassingTest:
initWithData:
TB,V_awaken
_createAIDsValidationError
lifetimeControlWithType:error:
remoteKeyID
replyNextState
tokenSession:beginAuthForOperation:constraint:error:
initWithCTKDEndpoint:targetUID:
currentProtocol
T@\"NSString\",R,N,V_clientDisplayName
T@\"NSUUID\",R,N,V_correlationID
authContext
exchangeKey:algorithms:parameters:error:
hexDigitValue:
prehashDataWithMessageData:publicKey:context:
_reservations
checkOperation:usingKey:algorithm:parameters:
localizedShortName
set_testing_stateDelay:
synchronousRemoteObjectProxyWithErrorHandler:
tokenDriver:configure:
tokenDriver:tokenForConfiguration:error:
tokenSession:createObjectWithAttributes:error:
T@\"NSNumber\",&,V_displayMaxCharacters
privateDelegate
Tr*,R
_context
_remoteAlertSemaphore
engine:getAttrib:error:
unsignedCharValue
TQ,R
_log
createDriver
engine:escape:
numberWithLongLong:
operationResult:error:
parseChildTLVRecordFromSource:nestingLevel:
powerRequestsQueue
_interactionTimeout
rangeOfString:
session:slotNameWithReply:
setPINMessageIndices:
T@\"NSObject<OS_dispatch_queue>\",&,V_queue
_portRef
connectionDidInvalidate:
fileExistsAtPath:isDirectory:
firstObject
keychainContents
processIdentifier
dealloc
T@\"NSString\",R
_tag
processName
resume
setUserPrompt:
keyType
_productID
connectCardSessionWithParameters:
registerTokenAccessRequestCorrelationID:access:reply:
setExportedObject:
transmitSynchronouslyChunkedIns:p1:p2:data:offset:realLe:chained:isCase4:responseBody:sw:error:
vendorID
_exportedObject
advertisedItems
Tq,V_keySizeInBits
certificateEncoding
recryptData:attributes:error:
_canDecrypt
_insertionHandler
initWithEntriesFromDictionary:
itemsOfClass:
numberWithInteger:
setPowerState:
stringForKey:
wasPINCredentialProvidedByPINUI
T@\"NSMutableDictionary\",R,N,V_initialKeepAlives
T@\"NSString\",R,N,V_classID
T@\"TKSmartCardSlot\",W,V_slot
_clientDisplayName
escape:reply:
idleQueue
useExtendedLength
_result
context
_keyRefForRequest:
encodeLength:into:sized:
objectAtIndexedSubscript:
setPhysicalRowCount:
_syncObject
decodeResponse:sw:appendTo:error:
endPolicy
initWithTokenID:LAContext:error:
setKeepAliveResourceSlot:
set_hasSeparateKeysAndCertificatesObjectIDSpace:
TB,V_valid
_activeStateNotifications
_setupWithDriver:error:
canPerformKeyExchange
init
initWithClientBundleID:clientName:clientConnection:clientHasAccessTokenEntitlement:tokenID:providerBundleID:providerName:correlationID:
initWithKeyType:keySize:accessControl:options:authContext:forceSystemSession:error:
_identities
_initWithKeyType:keySize:accessControl:options:authContext:forceSystemSession:error:
_lastUsedRegisteredTokenID
_newPINByteOffset
_systemKey
beginSessionWithReply:
sessionRequested
transmitRequest:reply:
PINBlockByteLength
getTokenWithAttributes:reply:
localizedInfoDictionary
setPINFormat:
startSessionWithLAContext:parameters:reply:
count
dictionary
T@\"<TKXPCConnectionDelegate>\",W,N,Vdelegate
_currentPINByteOffset
connectionDidInterrupt:
initWithTokenID:slotName:driverName:
isAsynchronous
mutableCopy
proprietaryCardUsage
T@\"NSData\",&
_maxInputLength
TB,GisSuitableForLogin,V_suitableForLogin
initSystemKeyIDs
makeSmartCard
screen
_keyType
_subject
objectEnumerator
processHandleForAuditToken:
selectApplication:error:
state
_powerMonitor
_protocol
allStoredBundleIDs
initWithSuiteName:
initWithToken:LAContext:parameters:error:
processInfo
setCaller:
setCanRequireCardInsertion:
v40@0:8@16@24@32
^{aks_ref_key_s=}16@0:8
@
v24@0:8@\"NSExtensionContext\"16
v64@0:8@16@24Q32B40B44@48@?56
@\"NSObject<OS_os_log>\"
@\"TKCTKDConnection\"
@\"TKClientTokenSession\"
@\"NSError\"
v44@0:8@\"NSData\"16@\"LAContext\"24B32@?<v@?B@\"NSError\">36
v24@0:8q16
C24@0:8^@16
v48@0:8@16@24@32q40
v32@0:8@\"NSString\"16@?<v@?@\"NSArray\">24
{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}
@\"<TKXPCConnectionDelegate>\"
B20@0:8C16
@24@0:8C16C20
v44@0:8@\"NSNumber\"16@\"NSNumber\"24B32@?<v@?@\"NSNumber\"@\"NSNumber\"q>36
@52@0:8@16@24@32B40^@44
@40@0:8@16@24@32
v40@0:8q16@24@?32
v32@0:8@\"NSString\"16@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">24
Q28@0:8C16C20C24
v32@0:8@\"<PKSubsystemServicePersonality>\"16@\"NSBundle\"24
v28@0:8I16@?<v@?@\"NSData\"q>20
B52@0:8@16q24q32d40B48
@76@0:8@16q24^{__SecAccessControl=}32@40@48@56B64^@68
v32@0:8@\"NSNumber\"16@?<v@?@\"NSArray\">24
B40@0:8@16q24^@32
@\"<TKTokenAccessUserPrompt>\"
v32@0:8@16@?24
@\"NSUserDefaults\"
^{IONotificationPort=}
v32@0:8@\"TKSmartCardUserInteraction<NSSecureCoding>\"16@?<v@?@\"NSData\"@\"NSError\">24
@\"NSObject\"
@\"NSObject<OS_dispatch_semaphore>\"
@64@0:8@16@24@32@40@48^@56
@\"NSData\"64@0:8@\"TKTokenSession\"16@\"NSData\"24@32@\"TKTokenKeyAlgorithm\"40@\"TKTokenKeyExchangeParameters\"48^@56
v24@0:8@\"NSString\"16
@\"TKTokenKeychainContents\"
@32@0:8:16@24
v28@0:8@16B24
v44@0:8@16@\"NSData\"24I32@?<v@?@\"NSData\">36
@\"NSNumber\"
@\"TKSEPKey\"
v28@0:8@16I24
q32@0:8@\"TKTokenAccessRequest\"16^@24
@40@0:8:16@24@32
B24@0:8:16
i
@\"TKToken\"
@\"<TKTokenSessionDelegate>\"
v68@0:8@16q24@32@40@48B56@?60
@\"TKSharedResourceSlot\"
v40@0:8@16@24@?32
@20@0:8i16
@40@0:8^@16^{__SecAccessControl=}24@?32
@\"TKTokenWatcher\"
@\"NSString\"
@68@0:8@16q24^{__SecAccessControl=}32@40@48B56^@60
B48@0:8q16@24@32@40
v52@0:8@16q24@32B40@?44
v32@0:8@16@24
v32@0:8q16@?24
B24@0:8@\"NSString\"16
v36@0:8q16I24@?<v@?@\"NSXPCListenerEndpoint\">28
B32@0:8^@16@?24
v20@0:8C16
v28@0:8q16I24
@\"NSString\"24@0:8@\"NSString\"16
B32@0:8@\"NSString\"16^@24
@24@0:8@\"NSCoder\"16
@?16@0:8
@\"TKSharedResource\"
@16@0:8
@\"<PKModularService>\"24@0:8@\"NSDictionary\"16
B
@\"NSLocale\"
S
v24@0:8@\"NSArray\"16
v24@0:8@\"<TKXPCConnection>\"16
v32@0:8@\"NSNumber\"16@?<v@?>24
Vv16@0:8
r*
i20@0:8S16
B16@?0^@8
v32@0:8q16@24
@\"TKSmartCardSlot\"
^{_NSZone=}16@0:8
@40@0:8@16@24^@32
v20@0:8S16
v20@0:8I16
v40@0:8@\"LAContext\"16@\"NSDictionary\"24@?<v@?@\"NSNumber\"@\"NSError\">32
@\"TKClientToken\"
@36@0:8@16S24Q28
@32@0:8@16Q24
v24@0:8d16
@\"TKToken\"40@0:8@\"TKTokenDriver\"16@\"TKTokenConfiguration\"24^@32
v24@0:8@?<v@?@\"NSDictionary\">16
v40@0:8@\"TKTokenID\"16@\"NSArray\"24@?<v@?>32
B40@0:8@16@24^@32
@\"<TKXPCConnection>\"
@48@0:8@16@24@32@40
v32@0:8q16q24
Q
v24@0:8@\"NSCoder\"16
^{aks_params_s=}
@48@0:8@16q24@32^@40
v36@0:8@\"NSString\"16B24@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">28
@?
v40@0:8@\"NSNumber\"16@\"NSData\"24@?<v@?@\"NSDictionary\"@\"NSError\">32
Q16@0:8
r*16@0:8
B24@0:8*16
B24@0:8Q16
B32@0:8@16^@24
@60@0:8C16C20C24@28@36^S44^@52
S16@0:8
@56@0:8C16C20C24C28@32@40Q48
B24@0:8^{__CFString=}16
v32@0:8@\"NSXPCListenerEndpoint\"16@?<v@?>24
v24@0:8@?16
v32@0:8@\"NSData\"16@?<v@?@\"NSData\">24
@48@0:8@16@24q32q40
v24@0:8Q16
@\"TKSmartCard\"
@76@0:8@16@24@32B40@44@52@60@68
@36@0:8C16C20C24@28
@24@0:8:16
@24@0:8r*16
B60@0:8^@16i24@28@36@44@52
@\"TKTokenAccessRequest\"
@\"TKTokenConnection\"
v48@0:8@16@24@32@?40
v24@0:8@?<v@?@\"NSArray\">16
@32@0:8^@16@?24
^{__SecCertificate=}16@0:8
v36@0:8@16B24@?28
{?={_NSRange=QQ}QBB}44@0:8C16@20Q28B36B40
v32@0:8@\"TKTokenID\"16@?<v@?>24
@\"<TKTokenAccessDB>\"
Q32@0:8C16C20C24C28
v64@0:8@16@24@32@40B48B52@?56
@32@0:8@16^@24
v24@0:8@\"<PKSubsystemServicePersonality>\"16
B48@0:8@16^S24@32^@40
@\"NSOperationQueue\"
@24@0:8^{_NSZone=}16
@32@0:8^{__SecCertificate=}16@24
@32@0:8@16@24
@\"<TKTokenDriverDelegate>\"
v48@0:8@\"NSString\"16@\"NSXPCListenerEndpoint\"24@\"NSString\"32@?<v@?>40
v28@0:8I16@?20
@\"TKSmartCardATR\"
@\"NSUUID\"
{?=[8I]}16@0:8
v28@?0@\"NSData\"8S16@\"NSError\"20
v32@0:8@\"NSString\"16@?<v@?>24
v60@0:8@\"NSString\"16{?=[8I]}24B56
v48@0:8@16@24@32^v40
B84@0:8C16C20C24@28^Q36Q44B52B56@60^S68^@76
v48@0:8Q16@24q32q40
@28@0:8@16B24
v40@0:8@\"TKTokenID\"16@\"NSString\"24@?<v@?B@\"NSError\">32
@\"NSXPCConnection\"
v24@0:8@?<v@?@\"NSXPCListenerEndpoint\">16
@\"TKTokenSession\"32@0:8@\"TKToken\"16^@24
@\"TKTokenDriver\"
q
B48@0:8@\"TKTokenID\"16@\"NSString\"24@\"NSString\"32^@40
[3@\"NSNumber\"]
v64@0:8@16q24@32@40@48@?56
B24@0:8@16
^{aks_ref_key_s=}
v32@0:8@\"NSNumber\"16@?<v@?@\"NSString\">24
v60@0:8@\"NSData\"16@\"NSData\"24@\"NSDictionary\"32@\"LAContext\"40B48@?<v@?@\"NSData\"@\"NSError\">52
v64@0:8@\"NSData\"16@\"NSData\"24@\"NSData\"32@\"LAContext\"40B48B52@?<v@?@\"NSData\"@\"NSError\">56
@\"<PKModularService>\"16@0:8
v32@0:8q16@\"TKTokenAccessRequest\"24
v48@0:8{?=[8I]}16
v60@0:8@16@24@32@40B48@?52
v52@0:8@\"NSData\"16@\"NSData\"24@\"LAContext\"32B40@?<v@?@\"NSData\"@\"NSError\">44
@40@0:8Q16@24@32
q24@0:8@\"TKTokenAccessRequest\"16
v32@0:8@\"NSString\"16@\"NSString\"24
v24@0:8@\"<TKXPCConnectionDelegate>\"16
v40@0:8@\"NSUUID\"16q24@?<v@?>32
v32@0:8@\"TKTokenDriver\"16@\"TKToken\"24
@\"NSDictionary\"
v32@0:8@\"NSDictionary\"16@?<v@?@\"<TKProtocolSmartCardSession>\"@\"NSDictionary\"@\"NSError\">24
@\"TKSmartCardSlotEngine\"
v40@0:8@16q24@?32
v40@0:8q16@\"NSString\"24q32
v40@0:8Q16@24q32
@\"NSXPCInterface\"
v16@0:8
v28@0:8@\"NSString\"16B24
B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24
q32@0:8@16^@24
@\"TKTokenConfiguration\"
v44@0:8@\"NSXPCListenerEndpoint\"16@\"NSData\"24B32@?<v@?@\"NSXPCListenerEndpoint\"@\"NSString\"@\"NSError\">36
@\"NSSet\"16@0:8
v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24
@56@0:8@16@24@32@40^@48
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@0:8
B24@0:8#16
Q32@0:8Q16*24
q24@0:8@16
@\"TKSmartCardSlotProxy\"
v20@0:8B16
v40@0:8@16B24B28@?32
v40@0:8@\"NSNumber\"16@\"NSDictionary\"24@?<v@?@\"NSData\"@\"NSDictionary\"@\"NSError\">32
#16@0:8
@\"TKTokenDriverContext\"
v36@0:8I16@20@?28
@\"TKSmartCardPINFormat\"
v32@0:8@\"SBSRemoteAlertHandle\"16@\"NSError\"24
v44@0:8@16q24B32@?36
@88@0:8C16C20C24@28{_NSRange=QQ}36@52Q60B68^B72^Q80
@\"NSObject<OS_dispatch_source>\"
v40@0:8@\"NSNumber\"16@\"NSData\"24@?<v@?B@\"NSError\">32
@48@0:8*16^@24@?32^B40
@\"<TKSmartCardTokenRegistrationXPCClient>\"
v36@0:8q16I24@?28
@24@0:8@16
B32@0:8@16Q24
v52@0:8C16C20C24@28@36@?44
B32@0:8q16^@24
@\"NSArray\"16@0:8
v24@0:8@\"<TKXPCConnectionConfiguration>\"16
r^v16@0:8
@32@0:8q16@24
@\"NSString\"16@0:8
@28@0:8C16@20
^{__SecAccessControl=}16@0:8
v40@0:8@\"TKTokenID\"16@\"NSData\"24@?<v@?>32
@56@0:8q16@24@32@40^@48
^{__SecIdentity=}16@0:8
v32@0:8@?16@24
B24@0:8@\"Protocol\"16
v56@0:8@16@24@32q40q48
@\"<TKSmartCardSlotNFCManaging>\"
@\"TKTokenID\"
v68@0:8C16C20C24@28Q36Q44B52B56@?60
@24@0:8^@16
B28@0:8I16@20
v72@0:8@16@24q32@40@48@56@?64
@20@0:8C16
@\"TKTokenAuthOperation\"48@0:8@\"TKTokenSession\"16q24@32^@40
v56@0:8@16@24@32@40@?48
C
d
@\"<TKSmartCardUserInteractionDelegate>\"
@\"<TKXPCConnectionDelegate>\"16@0:8
{?=\"val\"[8I]}
@\"<TKTokenDelegate>\"
v28@0:8@?16B24
v48@0:8@\"TKTokenID\"16@\"NSString\"24@\"NSString\"32@?<v@?B@\"NSError\">40
B48@0:8@\"TKTokenSession\"16q24@32@\"TKTokenKeyAlgorithm\"40
v44@0:8@16@24B32@?36
C16@0:8
@24@0:8@?16
q16@0:8
v48@0:8@\"NSXPCListenerEndpoint\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSString\">40
B16@0:8
v68@0:8@16q24@\"NSData\"32@\"NSDictionary\"40@\"LAContext\"48B56@?<v@?@\"NSData\"@\"NSDictionary\"@\"NSError\">60
v44@0:8@\"NSData\"16@\"LAContext\"24B32@?<v@?@\"NSDictionary\"@\"NSError\">36
@24@0:8Q16
B32@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@24
v32@0:8@\"NSDictionary\"16@?<v@?>24
v32@0:8@\"TKTokenID\"16@?<v@?@\"NSData\">24
@\"<TKRegisteredTokenManaging>\"
d16@0:8
B24@0:8^@16
@24@0:8q16
@40@0:8@16@24q32
v36@0:8@\"TKTokenID\"16B24@?<v@?>28
I
B24@0:8^{__ACMRequirement=}16
v48@0:8@\"NSNumber\"16@\"NSData\"24@\"NSString\"32@?<v@?B@\"NSError\">40
v40@0:8q16@24q32
v52@0:8@16@24@32B40@?44
@\"NSMutableDictionary\"
v24@0:8@?<v@?B@\"NSError\">16
@\"NSData\"
v32@0:8@\"TKTokenID\"16@?<v@?@\"NSArray\">24
B48@0:8@16@24@32^@40
B40@0:8@\"TKTokenID\"16@\"NSString\"24^@32
@\"NSXPCListenerEndpoint\"
B24@0:8q16
@\"TKSlotParameters\"
@\"NSXPCListener\"
@\"NSMapTable\"
@\"NSData\"56@0:8@\"TKTokenSession\"16@\"NSData\"24@32@\"TKTokenKeyAlgorithm\"40^@48
v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B@\"NSError\">32
B48@0:8@16@24q32^@40
I16@0:8
@\"NSDate\"
v24@0:8@\"SBSRemoteAlertHandle\"16
B48@0:8@16q24@32@40
v36@0:8I16@\"NSData\"20@?<v@?BB>28
v32@0:8q16@?<v@?q>24
v24@0:8@?<v@?>16
@52@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@24@32B40B44B48
v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSError\">24
B32@0:8@16@24
i24@0:8@16
B28@0:8B16^@20
@\"TKTokenConfigurationConnection\"
@28@0:8@?16B24
v28@0:8B16@?20
@\"TKPowerMonitor\"
@\"SBSRemoteAlertHandle\"
v52@0:8@\"NSData\"16q24@\"LAContext\"32B40@?<v@?B@\"NSError\">44
v24@0:8@16
@28@0:8B16@?20
@\"NSHashTable\"
@24@0:8@?<v@?@\"NSError\">16
@\"<TKSmartCardSlotEngineDelegate>\"
@56@0:8@16@24@32^B40^@48
@40@0:8@16^@24^@32
B32@0:8@16^Q24
v48@0:8@\"NSString\"16@\"NSString\"24@\"NSArray\"32@?<v@?BB@\"NSError\">40
v44@0:8@16@24I32@?36
@40@0:8@16^B24^@32
v60@0:8@16{?=[8I]}24B56
@\"NSMutableArray\"
@\"NSObject<OS_dispatch_queue>\"
@\"LAContext\"
i20@0:8B16
v72@0:8@\"NSNumber\"16@\"NSData\"24q32@\"NSData\"40@\"NSArray\"48@\"NSDictionary\"56@?<v@?@@\"NSError\">64
@\"NSArray\"
v32@0:8@\"TKToken\"16@\"TKTokenSession\"24
@44@0:8@16@24B32^@36
@32@0:8Q16@24
@\"TKSmartCardSessionEngine\"
@48@0:8@16@24@32^@40
[%lu bytes]
@16@?0@8
Retired4
    displayMaxLines: %@ \n
v24@?0@\"NSDictionary\"8@\"NSError\"16
GET DATA
1
init
com.apple.scpwr:%@
LAContext/ACMHandle temporary default slot
Access request was cancelled
params
PINLengthBitSize
    maxOutputLength: %ld\n
XPC connection to TKSmartCardTokenRegistrationXPC could not be created
*
%s: %s: returning, err = %ld.\n
v24@?0@\"NSXPCListenerEndpoint\"8@\"NSError\"16
sik
Retired8
ACMRequirement - ACMRequirementDataRatchet
Retired10
ACTIVE
endpolicy
ACMRequirement - ACMRequirementDataKofN
/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
@\"NSXPCConnection\"8@?0
Requested system key not supported by the platform
 (%d more)
ACMRequirement - ACMRequirementDataPushButton
Mismatch in active state notifications count
attesteeSystemSession
ord
CFBundleVisibleComponentName
ACMRequirement - ACMRequirementDataAccessGroups
com.apple.ctkd.smartcardregistration-client
tokenID
<%@ %@ %p>
failed to get DER-encoded aks_params_t (err=%d)
protocol
(u)
SW=%04X
com.apple.developer.nfc.readersession.iso7816.select-identifiers
v16@?0@\"NSData\"8
%02x
ACMRequirementGetSubrequirements
minPINLength
mlkem768
[CRYPT]
LibCall_ACMContextCreateWithExternalForm
TKLocalSEPKey.m
unable to bump/commit key
Retired2
BioInfo
appproxy
CFBundleDisplayName
remove-objects
%@
unable to delete key
keyUsage
LAPolicyTokenAuthentication did not fill in LAResultTKAuthOperation
ACM
Expecting key, but provided certificate objectID
pka_p384
kyber1024
INT AUTH
Retired15
Retired17
<%@: %p> algorithms: %@
PINJustification
TKTokenConfiguration.m
unable to decapsulate shared key
 
Unable to select card application AID %@
###
v16@?0@\"LAContext\"8
Retired5
com.apple.LocalAuthentication
/System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
apduQueue
user_prompt
ADMIN
READ_DATA
v16@?0@\"NSDictionary\"8
APDULog
Reinsertion simulation is currently running or was run recently. Please wait at least %f seconds between the calls.
[OLD+NEW-PIN:%lu bytes]
ock
com.apple.CryptoTokenKit.APDU
v32@?0@\"NSNumber\"8@\"_TKSmartCardSlotReservation\"16^B24
client
```
