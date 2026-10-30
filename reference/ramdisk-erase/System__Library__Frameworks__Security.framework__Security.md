# `/System/Library/Frameworks/Security.framework/Security`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 3,869,744 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 44 (Size: 6576)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (25)

- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore (compatibility version 0.0.0, current version 0.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8, upward)`
- `/usr/lib/libCoreEntitlements.dylib (compatibility version 1.0.0, current version 1.0.0, upward)`
- `/usr/lib/libTLE.dylib (compatibility version 1.0.0, current version 1.0.0, upward)`
- `/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity (compatibility version 0.0.0, current version 0.0.0, upward)`
- `/System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer (compatibility version 1.0.0, current version 326.31.9, upward)`
- `/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter (compatibility version 1.0.0, current version 0.0.0, weak)`
- `/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport (compatibility version 1.0.0, current version 1.0.0, upward)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0, upward)`
- `/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag (compatibility version 1.0.0, current version 1.0.0, upward)`
- `/System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices (compatibility version 1.0.0, current version 1226.0.0, upward)`
- `/System/Library/Frameworks/CoreServices.framework/CoreServices (compatibility version 1.0.0, current version 1226.0.0, upward)`
- `/System/Library/PrivateFrameworks/CoreTime.framework/CoreTime (compatibility version 1.0.0, current version 340.0.14, weak)`
- `/usr/lib/libsqlite3.dylib (compatibility version 9.0.0, current version 408.0.0)`
- `/usr/lib/libcoretls.dylib (compatibility version 1.0.0, current version 189.40.2)`
- `/usr/lib/libcoretls_cfhelpers.dylib (compatibility version 1.0.0, current version 189.40.2)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libbsm.0.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking (compatibility version 1.0.0, current version 72.0.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (109 classes, 32 protocols)

Classes: `AcmeCertRequest`, `CKKSControl`, `CKKSCurrentItemQuery`, `CKKSCurrentItemQueryResult`, `CKKSExternalKey`, `CKKSExternalTLKShare`, `CKKSPCSIdentityQuery`, `CKKSPCSIdentityQueryResult`, `DefaultCollectionActions`, `DetachedCertificateEntry`, `DetachedCertificatesFile`, `DetachedCertificatesLookup`, `ExternalPreSharedKey`, `FakeSecuritydXPCClient`, `KCSharingDaemonConnection`, `KCSharingGroup`, `KCSharingGroupCreateRequest`, `KCSharingGroupDeleteRequest`, `KCSharingGroupFetchRequest`, `KCSharingGroupInvite`, `KCSharingGroupLeaveRequest`, `KCSharingGroupManager`, `KCSharingGroupUpdateInfo`, `KCSharingGroupUpdateRequest`, `KCSharingMessagingdConnection`, `KCSharingParticipant`, `LKAUpgradeOutcomeReport`, `LocalKeychainAnalytics`, `NSData`, `NSDate`, `NSObject`, `OTBottleIDs`, `OTClique`, `OTConfigurationContext`, `OTControl`, `OTControlArguments`, `OTJoiningConfiguration`, `OTMetricsSessionData`, `OTOperationConfiguration`, `OTSerializedPlistEscrowRecord`, `OfferedEPSK`, `SECSFAAction`, `SECSFAActionAutomaticBugCapture`, `SECSFAActionDropEvent`, `SECSFAActionTapToRadar`, `SECSFAEventFilter`, `SECSFAEventRule`, `SECSFAMatchProperty`, `SECSFAPropertyValue`, `SECSFARule`, `SECSFARules`, `SECSFAVersion`, `SECSFAVersionMatch`, `SFAnalytics`, `SFAnalyticsActivityTracker`, `SFAnalyticsCollection`, `SFAnalyticsEvent`, `SFAnalyticsMatchingRule`, `SFAnalyticsMultiSampler`, `SFAnalyticsSQLiteStore`, `SFAnalyticsSampler`, `SFObjCType`, `SFSQLite`, `SFSQLiteStatement`, `SOSAnalytics`, `SOSCachedNotification`, `SecABC`, `SecAsyncPiper`, `SecCBORArray`, `SecCBORData`, `SecCBORMap`, `SecCBORNegative`, `SecCBORString`, `SecCBORUnsigned`, `SecCBORValue`, `SecCTKKey`, `SecConcrete_sec_array`, `SecConcrete_sec_certificate`, `SecConcrete_sec_identity`, `SecConcrete_sec_protocol_configuration`, `SecConcrete_sec_protocol_configuration_builder`, `SecConcrete_sec_trust`, `SecCoreAnalytics`, `SecEscrowRequest`, `SecExpConcrete_sec_experiment`, `SecExperiment`, `SecExperimentConfig`, `SecExternalPreSharedKey`, `SecItemCurrentItemData`, `SecItemRateLimit`, `SecJWSDecoder`, `SecJWSEncoder`, `SecKeyProxy`, `SecKeyProxyTarget`, `SecLaunchEvent`, `SecLaunchSequence`, `SecOfferedEPSK`, `SecOfferedPAKEIdentity`, `SecSFAParsedCollection`, `SecSOSStatus`, `SecSessionInfo`, `SecTapToRadar`, `SecXPCHelper`, `SecXPCUtils`, `SecuritydXPCCallback`, `SecuritydXPCClient`, `SharedCredentialController`, `TPMIDStableTrustedDeviceID`, `TPStableTrustedDeviceID`

Protocols: `ASAuthorizationControllerDelegate`, `ASAuthorizationControllerPresentationContextProviding`, `CKKSControlProtocol`, `EscrowRequestXPCProtocol`, `KCSharingGroupManagerSubscriberProtocol`, `KCSharingInvitationNotificationProtocol`, `KCSharingMessagingdXPCServerProtocol`, `KCSharingXPCClientProtocol`, `KCSharingXPCServerProtocol`, `NSCoding`, `NSCopying`, `NSObject`, `NSSecureCoding`, `NSXPCListenerDelegate`, `OS_sec_array`, `OS_sec_certificate`, `OS_sec_experiment`, `OS_sec_identity`, `OS_sec_protocol_configuration`, `OS_sec_protocol_configuration_builder`, `OS_sec_trust`, `OTControlProtocol`, `SFAnalyticsCollectionAction`, `SFAnalyticsProtocol`, `SFSQLiteRow`, `SOSControlProtocol`, `SecEscrowRequestable`, `SecKeyProxyProtocol`, `SecuritydXPCCallbackProtocol`, `SecuritydXPCClientInterface`, `SecuritydXPCProtocol`, `TrustdFileHelper_protocol`

## Strings (8,655)

First 2,500 of 8,655.
```
Could not configure SOSControlHelper: %@
cccurve448_make_pub() failed, error %d
returning attached embedded content of type %@
SFACollection ratelimit ttr: %@
Setting configuration overrides based on AppTransportSecurity exceptions
skipping recovery key entry
MessageSecurity and Security frameworks have different results, returning Security result. sec: %@, ms: %@
SIRL disabled via feature flag
Failed to increment the exceptions epoch.
%p: unrecognized header magic (%x)
xpc: connection pool full but tracker does not agree (%d vs %ld)
 OctagonSignpostNameFetchEgoPeer=%{public,signpost.telemetry:number1,name=OctagonSignpostNameFetchEgoPeer}d 
Changing itemsChangedBlock
returning keychain database path error: %@
_myKey is NULL, avoiding crash
%p will start remote signature from %p with block %p
SecAccessGroupsSetCurrent releasing gClient access groups
sos requestToJoinCircle complete: %d %@
octagon-checkcustodianrecoverykey, failed to check custodian recovery key
END [%lld] %fs: GenerateInheritanceKey  OctagonSignpostNameGenerateInheritanceKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameGenerateInheritanceKey}d 
Unknown ML-DSA type detected
ticket size was too large: %lld
%zd library dependency bytes in %d blob(s) from %s(%s)
Local reset finished successfully
No rules, not setting up collection
octagon-createinheritancekeyclaimtokenwrappingkey, failed to create octagon inheritance recovery key (w/claim+wrappingkey)
successfully opened analytics db
Non-compliant signature: r is %lld bytes, expected %lld
Adding securityd connection to pool, total now %d
ksd/client/declineInviteForGroupID
Add for id: %@, bk: %@, wrapped: %@
skipping file due to xattr: %s
ksd/client/setChangeTrackingEnabled
no rules %@
fetching user-controllable-sync-async status errored: %@
findOptimalBottleIDsWithContextData succeeded: %@, %@
SOSCCSetUserCredentialsAndDSID for %@\n
Failed to create key from data, algorithm:%d, class:%d: %{public}@
attestation not explicitly required, ignoring error
BEGIN [%lld]: PeerDeviceNamesByPeerID  enableTelemetry=YES 
 OctagonSignpostNameJoinAfterRestore=%{public,signpost.telemetry:number1,name=OctagonSignpostNameJoinAfterRestore}d 
csr: unsupported signature algorithm
Exceptions are valid for the current exceptions epoch. (%llu)
Certificate chain is NULL
SFAnalyticsSampler created without valid client class (%@)
Establish
BEGIN [%lld]: RemoveFriendsInClique  enableTelemetry=YES 
 OctagonSignpostNameCopyViewUnawarePeerInfo=%{public,signpost.telemetry:number1,name=OctagonSignpostNameCopyViewUnawarePeerInfo}d 
createInheritanceKey w/claimToken+wrappingKey invoked for context: %@
xpc: %@
peerDeviceNamesByPeerID succeeded: %@
Failed to parse view name
csr: cert issuance failed: %@
SecKeyCreateWithData
SecKeyCreateDecapsulatedKey
join using custodian recovery key
failed to join using inheritance key: %@
Retrieved non-cached circle value %d
csr: failed to encode atv
xpc: failure to obtain XPC proxy object for app clip promotion, %@
signing context setup with existing cert chain: %@
OctagonAuthenticatedRKJoin overridden to %s
secitemratelimit: unable to get task from self, disabling SIRL
SecItemUpdate_ios
keychain item data exceeds reasonable size (%lu bytes)
Failed to parse signature: %d
SHA224 fingerprint digest
__delegate_identifier__:Performance Diagnostics__:::____message__:This method should not be called on the main thread as it may lead to UI unresponsiveness.
KCSharingSetupMessagingdServerProtocol failed, continuing, but you might crash later: %@
enter SOSCCFetchCompatibilityModeCachedValue
%p caused an error during CoreEntitlements parsing
Could not get basename of %s: %d [%s]
xpc: could not get foreground uid %d
SHA384 fingerprint digest
OctagonRKTLKOwnershipProof override removed
Setting up new rules
successfully joined using custodian recovery key
SecTrustStoreCopyTransparentConnectionPins
Unable to check if path is on rootfs: %d, %s
removeInheritanceKey invoked for context: %@
Unable to create signer info: %@, %@, %@
Resync finished successfully
Unable to get public from octagon peer signing key
xpc: failure to obtain XPC proxy object for SecCopyKeychainDatabasePath %@
Extracting ticket from bundle: %s
 OctagonSignpostNameRemoveFriendsInClique=%{public,signpost.telemetry:number1,name=OctagonSignpostNameRemoveFriendsInClique}d 
successfully removed inerhitance key
Piggybacking include identities(%d) and tlks(%d)
SecTrustStoreSetTrustSettings
unable to read entire ticket from bundle
Remote signing requires hash dictionary.
PreflightRecoverOctagonUsingInheritanceKey
%@ %@ (index %d)
ACME request flow failed at step %lld: %@
type %d (errno %d): %s
Push finished with error: %@
clique-enable-walrus: unable to create otcontrol: %@
csr: failed to decode CSR
cert added to keychain
entering excluded path: %s
excluded
Could not configure SecuritydXPCProtocol: %@
successfully joined using inheritance key
failed to fix files; caught exception: %@
Forcing CTK systemKey due to %{public}@=%{public}@ on shared iPad
Invalid date specification in certificate (see RFC5280 4.1.2.5)
SecItemBackupRestore
could not disable pinning: AppleServerAuthenticationNoPinning not true
Configuration '%{public}s' for experiment '%{public}s' not sampled to run
not using system keychain
Countersigned accepted requests
Invalid InhibitAnyPolicy Extension
(Trust %p) Kick off pending evals
%p loaded InfoDict %p, %schecked
SecAccessGroupsSetCurrent releasing thread local access groups
 OctagonSignpostNameRecreateInheritanceKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameRecreateInheritanceKey}d 
END [%lld] %fs: PerformedCDPStateMachineRun  OctagonSignpostNamePerformedCDPStateMachineRun=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePerformedCDPStateMachineRun}d 
octagon-cdp-status: failed to fetch OTControl object: %@
Failed to get usage constraints for %{mask.hash}@, %d
recreateInheritanceKey invoked for context: %@
RecreateInheritanceKey
Invalid QCStatements Extension
csr: failed to encode extension attributes
Receiving file for %@ with fd %d of size %llu
Set %@ as name on all policies
codesign allocation failed: %s
gSecurityd non-nil, disabling SIRL for testing
_SecKeychainCopyOTABackup
ksd/client/wipe
%{public}@ failed to fix our files: %@
SOS Compatibility Mode feature flag enabled, checking platform availability and sos compat mode
Failed to create key for tokenID=%{public}@: %{public}@
[refTime] process bestEffortTime source=%s (platform_binary=%d)
Failed to parse the current exceptions epoch as a uint64.
Attempt to fetch attestation certificate failed (error %lld)
Checking symlink target: %s
skipping hash agility attribute that failed to decode: %@
finding optimal bottles for context:%@, altdsid:%@
Invalid QCS Type
HybridSig key pair generation failed: %d
(Trust %p) Prior trust results valid
Unable to allocate space for storing basename: %d [%s]
SFAnalytics: could not open db at init, will try again later. Error: %@
%@ v2 peer has no views
SecKeyCreateEncapsulatedKey
no %@ in array!
checking notarization on %d, %@
SFACollection action trigger drop: %@
Configuring pairing channel with configured altDSID: %@
SOS disabled for this platform, returning NO
SecKeyCopyPersistentRef: SecItemCopyMatching returned success, but we got type %lu instead of CFData for key %@.
SecTrustOTAPKIGetUpdatedAsset
Removed TrustSettings for %{mask.hash}@
Configuration '%s' for experiment '%s' succeeded
sfsqlite: sqlite3_bind_null error
octagon: TPStableTrustedDeviceID missing fields: %@
SFAnalyticsMatchingRule match dictionary wrong: %@
Trust settings %{public}s exist for %{mask.hash}@
posted success: %@
Additional cloud identity found in circle after successful creation: %@
SecItemBackupSetConfirmedManifest
codesign: could not preserve setuid/setgid bits on %s
Unable to acquire the xattr list from %s
Push finished successfully
peerDeviceNamesByPeerID errored: %@
SWC received didCompleteWithError
Failed to get exception for epoch check.
kSecUseSystemKeychain present, using system keychain
Requesting a local resync for view %@
fetching entropy for bottling for context:%@, altdsid:%@
octagon-storeinheritancekey, failed to store octagon inheritance recovery key
MessageSecurity and Security frameworks have different attached contents results, returning Security result. sec: %@, ms: %@
cccurve25519_make_pub_with_rng() failed, error %d
csr: failed to create Hybrid Composite Public Key (draft-07+)
failed to copy enabled views
STRICT VALIDATION ERROR: the size of the padding after the universal cannot be calculated to a fixed size
task_cpu_us=%{public,signpost.telemetry:number1,name=task_cpu_us}lld thread_cpu_us=%{public,signpost.telemetry:number2,name=thread_cpu_us}lld enableTelemetry=YES 
Failed to fetch Octagon exclusion status: %@
BEGIN [%lld]: RequestToJoinCircle  enableTelemetry=YES 
csr: pool allocation failure
Invalid or missing key size in: %@
upgradeIfNeeded result: %i
Failed to get the current exceptions epoch.
Platform does not support signing internal requirements
skipping signing time that failed to decode: %@
SFAnalyticsMatchingRule match not dictionary
Invalid SubjectAltName Extension
64-bit linkedit is%s valid
Secure Timestamp Cutoff Date cutoff: %@
CE context should not be accelerated
Failed to create notification, error %@
SecSecurityClientGet new thread!
unexpected CF type (%lu) for key %s
peersHaveViewsEnabled for context:%@, altdsid:%@
 OctagonSignpostNameRequestToJoinCircle=%{public,signpost.telemetry:number1,name=OctagonSignpostNameRequestToJoinCircle}d 
exception reading embedded Info.plist
SecuritydXPCClient: could not get foreground uid %d
App Transport Security value for key %s must be a string
leaveClique success.
Failed to generate software key %{public}@:%{public}@, error: %d
Remote signing requires signing block.
 OctagonSignpostNameLeaveClique=%{public,signpost.telemetry:number1,name=OctagonSignpostNameLeaveClique}d 
Skipping %@, not data.
SOSCircleEnsureRingConsistency requires ring membership and generation count consistency check
Failed to parse CONS SEQ of TLKs
SOSCCSetUserCredentials for %@\n
SecItemCopyMatching_ios
SecTrustReportTLSAnalytics
rss_delta_kb=%{public,signpost.telemetry:number1,name=rss_delta_kb}lld peak_kb=%{public,signpost.telemetry:number2,name=peak_kb}lld enableTelemetry=YES 
CreateInheritanceKeyWithClaimTokenAndWrappingKey
enter SOSCCSetCompatibilityMode
sos-compatibility-mode: fetching compatibility mode error: %@
BUG IN SECURITY CLIENT: policies array contains non-policy value
Failed to remove all trust settings, %d
Cannot determine because deviceMode is NULL
sfsqlite: Error finalizing prepared statement: \"%@\"
 OctagonSignpostNameEstablish=%{public,signpost.telemetry:number1,name=OctagonSignpostNameEstablish}d 
SHA512 fingerprint digest
ksmd/client/cancelPendingInvitesForGroup
failed to preflight join using custodian recovery key: %@
unexpected view number: %d
Passing out external digest: %d, %@
codesign deallocation failed: %s
Serializing DER entitlements failed
Loading matching rules: %@
%p is a fat file with %d architectures
failed to read sysctl %s
fetching clique status failed: %@
Unable to get public from octagon peer encryption key
SecKeyCreateEncryptedDataWithParameters
SecTrustIncrementExceptionResetCount
Remote signing requires valid code directory.
%p done serializing %s
Unable to check if path exists: %d, %s
sampler went away before we could run its once-per-report block
Cannot instantiate SFActivityTracker without name and client class
%{public}s failed, export not implemented for key %{public}@
Configuration '%s' for experiment '%s' failed
ksd/client/acceptInviteForGroupID
failed to preflight join using inheritance key: %@
CheckInheritanceKey
API returned: %d
HybridSig: Unknown private key context type for initialization
SecCopySharedWebCredentialSync found no credential
SecKeyCreateMLDSASignature
Fetch finished successfully
END [%lld] %fs: FetchCliqueStatus  OctagonSignpostNameFetchCliqueStatus=%{public,signpost.telemetry:number1,name=OctagonSignpostNameFetchCliqueStatus}d 
majorVersion: %d
csr: failed to encode extensions
session[%p] failed to decrypt, mktu: %@, mpi: %@, tpi: %@, m: %@
BUG IN SECURITY CLIENT: responseData contains unsupported value type
Invalid signing operation, bailing.
secitemratelimit: unable to get signing identifier, disabling SIRL
xpc: failure to obtain XPC proxy object for Item Persistence, %@
Could not read entire trailer
Failed to fetch current user identifier: %{public}@
successfully removed custodian recovery key
Enter SOSCCCopyMyPeerWithNewDeviceRecoverySecret()
%p is a thin file (%s)
resource validation on xattr file skipped: %s
END [%lld] %fs: CopyViewUnawarePeerInfo  OctagonSignpostNameCopyViewUnawarePeerInfo=%{public,signpost.telemetry:number1,name=OctagonSignpostNameCopyViewUnawarePeerInfo}d 
successfully generated octagon inheritance recovery key
No iCloud identity PeerInfo found in circle
SecKeyControlLifetime
csr: extensions or parameters wrong input type
(Trust %p) Calling completion block
Failed to read trust settings for %{mask.hash}@
SecTrustStoreCopyCARevocationAdditions
ksd/client/provisionWithReply
RemoveFriendsInClique
createInheritanceKey invoked for context: %@
%p validation threw non-common exception
CloudKit reset finished successfully
Invalid certificate version (%d), must be 0..2
leaving %s
Failing to validate empty code directories.
user sessions enabled, targeting %d
establish started
%@: %@
CKP Transport: tearing down xpc connection
Checking view / circle status for %@:  SOSCCStatus: (%@) SOSViewResultCode(%@) Error: (%@)
ML-KEM privkey size=%dbytes import of priv part failed: %d
SecTrustStoreCopyCTExceptions
Probable bug: error destroying Mutex: %d
Requesting a fetch for view %@
attempt to instatiate abstract class SFAnalytics
octagon-recreateinheritancekey, failed to recreate octagon inheritance recovery key
SecCopySharedWebCredentialSync received result %d
unable to stat stapling file: %d
exception getting host requirement (ignored)
Unable to perform remote signing with no certificates: %@
Requesting a local reset for view %@
ksd/client/deleteGroupWithRequest
too many hash agility V2 attributes (%d), skipping
Failed to obtain public key for attestation key, skipping attestation
missing DR info for library index %d
DeferSOSFromSignIn overridden to %s
ksd/client/groupsUpdated
BEGIN [%lld]: AccountUserKeyAvailable  enableTelemetry=YES 
Failed to make FullPeer for iCloud Identity: %@ (%@)
_SecKeychainSyncUpdateMessage
successful preflight join using inheritance key
cced448_make_pub() failed, error %d
octagon-createcustodianrecoverykey, failed to create octagon custodian recovery key
clique-disable-walrus: failed to disable walrus: %@
key not available
close(%d) error %d
Requesting a resync for view %@
END [%lld] %fs: WaitForInitialSync  OctagonSignpostNameWaitForInitialSync=%{public,signpost.telemetry:number1,name=OctagonSignpostNameWaitForInitialSync}d 
Couldn't save tlks to keychain %d
STRICT VALIDATION ERROR: failed to read expected gap bytes
sfsqlite: Can't bind object of type %@
could not create path: %s (%s)
setUserCredentialsAndDSID results: %d %@
This process is requesting a expensive full keychain database checkpoint
SecItemBackupHandoffFD returned %d: %@
SecKeyCopyExternalRepresentation
Out of retries retrieving attestation certificate
couldn't create a managed context from csops call %d
Configuration '%s' for experiment '%s' not configured to run with sampling %s
END [%lld] %fs: RemoveFriendsInClique  OctagonSignpostNameRemoveFriendsInClique=%{public,signpost.telemetry:number1,name=OctagonSignpostNameRemoveFriendsInClique}d 
%p (%s) loaded
cannot open stapled file for reading: %d
FetchEgoPeer
%s: signing identifier is NULL, cannot generate a LWCR
SecItemBackupViewAndCopyBackupPeerID
attestation explicitly required, cannot continue with ACME
stapling is not a regular file
failed to load %s
Starting experiment '%s' synchronously with sampling %s
Logging keychain UI event failed: couldn't turn dialog type c_str into NSString
preflight join using inheritance key
ML-DSA privkey size=%dbytes import of pub part failed: %d
unlink DetachedCertificates.der failed: %s (errno %d)
OctagonSupportsMultiuser override removed
END [%lld] %fs: FindOptimalBottleIDsWithContextData  OctagonSignpostNameFindOptimalBottleIDsWithContextData=%{public,signpost.telemetry:number1,name=OctagonSignpostNameFindOptimalBottleIDsWithContextData}d 
SFAnalytics: failed to deserialize record: %{public}@
Peers In Circle: None
SOSSetNewPublicBackupKey (%@)
signing/encryption CAs do not match
App Transport Security exceptions must be a dictionary
successfully set CDP bit
Invalid PolicyConstraints Extension
using explicit cdFlags=0x%x
failed to read the decrypted content after decoding
SFACollection ratelimit abc: %@
no private key found
Local resync finished with error: %@
KCSharingSetupInvitationNotificationProtocol failed, continuing, but you might crash later: %@
TriggerABC signature generation failed
octagon: Failed to fetch octagon peer ID: %@
END [%lld] %fs: TryUserCredentialsAndDSID  OctagonSignpostNameTryUserCredentialsAndDSID=%{public,signpost.telemetry:number1,name=OctagonSignpostNameTryUserCredentialsAndDSID}d 
couldn't convert CE to CF %d
file helper successfully completed fixes
der: invalid date: %@; %s
Couldn't fetch initial sync status for view %@: %@
BEGIN [%lld]: RemoveCustodianRecoveryKey  enableTelemetry=YES 
valid/debugged platform binary %@ on internal release, enabling SIRL
%{public}@=%{public}@ detected, but not on shared iPad, ignoring this flag
unknown failure key in details dictionary: %@
SFAnalyticsSampler: interval %f is not supported
connection invalidated %@
BEGIN [%lld]: FetchEscrowContents  enableTelemetry=YES 
END [%lld] %fs: RemoveInheritanceKey  OctagonSignpostNameRemoveInheritanceKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameRemoveInheritanceKey}d 
checkInheritanceKey invoked for context: %@
Failed to disable view(%@): %@
keychain database path xpc status error: %@
%s check-fixed (altered).
SFACollection action trigger abc: %@ %@
 OctagonSignpostNameSetNewRecoveryKeyWithData=%{public,signpost.telemetry:number1,name=OctagonSignpostNameSetNewRecoveryKeyWithData}d 
Failed to set signature: %@
Rejected Applicants To Circle: None
callback error: %@
removed stale DetachedCertificates.der at %s
SFAnalytics: attempt to log an event with no name
couldn't add view %@
csr: unsupported public key algorithm in CSR
%@ Reinitializing DH Keys, first: %@
SecTrustExceptionGetResetCount
%s: failed to query hw.osenvironment sysctl (error: %s)
Failed at id: %@, bk: %@ error: %@
Applicants To Circle: None
csr: wrong value type for custom extensions
overriding request extensions with parameters extensions
session[%p]Cannot process message:%@, session is not done negotiating, session state: %@
sfsqlite: Error clearing prepared statement bindings: \"%@\"
cliqueStatus(%{public}scached)(context:%@, altDSID:%@) returning %@ (error: %@)
Couldn't save backupV0 to keychain %d
Skipping general names after the first %d
csr: non-empty signature algorithm parameters
Error preparing statement: %@
failed to fetch OTControl object: %@
app clip deletion result: %i
CFError
tryUserCredentialsAndDSID for context:%@, altdsid:%@
SecItemPersistKeychainWritesAtHighPerformanceCost
ML-KEM pubkey size=%dbytes is invalid
policy 0x%lX has no _oid
SecTaskLoadEntitlements failed error=%d cs_flags=%x, pid=%d task=%@
try %s
Unable to stat %s: %d [%s]
OctagonSupportsMultiuser overridden to %s
successfully disabled walrus
SecItem: failed to create identity
session[%p] failed to decrypt, mktu: %@, mpi: %@, tpi: %@, m: %@, tP: %@, tb: %hhx
kSecUseSystemKeychainAlways… present, using system keychain
ksd/client/groupInvitationWasCancelled
Received %lu Octagon peers
TryUserCredentialsAndDSID
Couldn't serialize json record: %@
failed to talk to %{public}@: %@
csr: failed to get public key
csr: failed to encode notBefore
cleaning up unpooled xpc conn to trustd %p
Received request waiting on passcode: %@ %@
dlsym libnetwork _nw_protocol_metadata_access_handle
SHA256 fingerprint digest
Error processing fat file: Two architectures have the same size
Experiment '%s' not found
Applicants To Circle:
Checking if circle %@ is legacy
clique status is %@; beginning an establish
BEGIN [%lld]: CheckInheritanceKey  enableTelemetry=YES 
Failed to copy peer: %@ (%@)
 OctagonSignpostNamePreflightRecoverOctagonUsingInheritanceKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePreflightRecoverOctagonUsingInheritanceKey}d 
cced25519_make_pub_with_rng() failed, error %d
Failed to generate Kyber key: err %d
keygen failed
(Trust %p) trustd returned %d
%p rule %s added (weight %d, flags 0x%x)
SFAnalytics: cannot add sampler without block
BEGIN [%lld]: RemoveInheritanceKey  enableTelemetry=YES 
enter SOSCCJoinWithCircleJoiningBlob applicant
csr: unsupported SubjectAltName type, skipping
enter SOSCCMessageFromPeerIsPending
SecItemBackupHandoffFD
open(%s,0x%x,0x%x) = %d
looking at identity to create cert chain: %@
SecTrust evaluation of signing certificate failed - not fatal
%s isn't a regular file
cleaning up unpooled xpc conn %p
setting user-controllable-sync status to %@
setUserCredentialsAndDSID for context:%@, altdsid:%@
V0 views disabled by Managed Preferences Profile
Invalid serial number length (%ld), must be 1..20
HybridSig: Unknown public key context type for destruction
(Trust %p) Calling completion block after async xpc
RecoverOctagonUsingInheritanceKey
Kyber pubkey size=%dbytes is invalid
SecServerBackupKeybagAdd
ksd/client/resyncWithCompletion
Invalid KeyUsage Extension
Platform does not support signing secure timestamps
SecAccessGroupsSetCurrent end!
Pairing channel context already configured with altDSID: %@
END [%lld] %fs: PreflightRecoverOctagonUsingInheritanceKey  OctagonSignpostNamePreflightRecoverOctagonUsingInheritanceKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePreflightRecoverOctagonUsingInheritanceKey}d 
csr: failed to encode challenge
HybridSig: Unknown private key context type for public key extraction
%{public}s failed: %{public}@
SecTrustResetSettings
CMS message does not contain a SignedData
findOptimalBottleIDsWithContextData errored: %@
Peer info v2 create copy failed: %@
Not valid/debugged platform binary, disabling SIRL
Signature algorithm mismatch in certificate (see RFC5280 4.1.1.2)
%{public}s called with NULL SecKeyRef
ksd/client/checkAvailabilityForHandles
Cannot log system metrics without name
resetAndEstablish returned an error: %@
octagon-removecustodianrecoverykey, failed to remove custodian recovery key
 OctagonSignpostNameCheckCustodianRecoveryKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameCheckCustodianRecoveryKey}d 
join using inheritance key
public key failed to be created
Checking view / circle status for %@:  ENABLED
fetchCurrentItemOutOfBand
Not internal release, disabling SIRL
Skipping domain-form rfc822Name SAN (no '@'): %@
SecItemFetchCurrentItemDataAcrossAllDevices
Failed to get the exceptions epoch.
Successfully retrieved attestation certificate
symtab is%s valid
SecCodeSignerRemote: Certificate chain uses an unsupported signature algorithm.
dlopen libnetwork
Adding %@ %@
%p validating slot %d
%p: couldn't make up XML
using text cdFlags=0x%x from Info.plist
Received prerecord for %@: %@
cliqueMemberIdentifier complete: %@
ResetAndEstablish
fetchPCSIdentityOutOfBand
cdhash mismatch: %@, %@, %@
Starting experiment '%s' asynchronously with sampling %s
RequestToJoinCircle
policy 0x%lX has no _options
Malformed signature index entry: %d, %zu, %d
RollIdentityOnMIDRotation overridden to %s
Failed to generate ML-KEM key: err %d
SecTrustTriggerValidUpdate
Found no trust settings for %{mask.hash}@
Failed to copy public key data for co-residency, skipping attestation
%p the XML cannot be converted to valid DER
KCSharingSetupServerProtocol failed, continuing, but you might crash later: %@
app clip promotion result: %i
Key with NULL class detected!
creating an Apple pinning policy with a non-Apple OID: %@
Failed to talk to %s after %d attempts.
END [%lld] %fs: Establish  OctagonSignpostNameEstablish=%{public,signpost.telemetry:number1,name=OctagonSignpostNameEstablish}d 
fetched user-controllable-sync-async status as : %@
_SecBackupKeybagDelete
failed to convert apple anchor cert
Account Creation Date Cutoff: %@
SecCodeSignerRemote: remote signer contains no certificate chains.
operation is UpdateTokenItemsForSystemKeychain, always using system keychain
END [%lld] %fs: SetUserCredentialsAndDSID  OctagonSignpostNameSetUserCredentialsAndDSID=%{public,signpost.telemetry:number1,name=OctagonSignpostNameSetUserCredentialsAndDSID}d 
Couldn't serialize rockwell record: %@
unable to create public key from private, using input public key
BUG IN SECURITY CLIENT: policies contains unsupported value type
OctagonSupportsMultiuser is %s
App Transport Security exception %{public}@ is not a valid CIDR notation.
findOptimalBottleIDsWithContextData complete
SecTrustGetAssetVersionNumber
 OctagonSignpostNameCreateCustodianRecoveryKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameCreateCustodianRecoveryKey}d 
keychain database path: %@
Unexpected error checking account creation date: %ld
failed to parse entitlements: %s
Cannot enable visible keychain views due to profile restrictions
policy \"%@\" requires a string value for the %@ key
Invalid ML-DSA type %@ requested for ML-DSA key generation
%p version 0x%x newer than current 0x%x
configuring remote signing with cert chain: %@
 OctagonSignpostNameSetUserCredentialsAndDSID=%{public,signpost.telemetry:number1,name=OctagonSignpostNameSetUserCredentialsAndDSID}d 
Security requires credentials...
PI:    %@
_SecKeychainDeleteMultiUser
unknown otr auth state
Requesting a push for view %@
csr: unable to get challenge bytes
SecSetLoggingInfoForXPCScope
skipping hash agility entry with invalid OID: %@
 OctagonSignpostNameFetchCliqueStatus=%{public,signpost.telemetry:number1,name=OctagonSignpostNameFetchCliqueStatus}d 
 OctagonSignpostNameTryUserCredentialsAndDSID=%{public,signpost.telemetry:number1,name=OctagonSignpostNameTryUserCredentialsAndDSID}d 
 OctagonSignpostNameStoreInheritanceKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameStoreInheritanceKey}d 
asking the file helper to fix our files
enter SOSCCFetchCompatibilityMode
%@ exempt from SIRL
%@ Start packet: %@
Static Persistent Refs are %@ (overridden)
failed to get userKeyID
Parsing :%@:
%s
realpath failed checking symlink: %d
Cannot init db with empty path
sec_protocol_configuration_create failed
CopyPeerPeerInfo
BEGIN [%lld]: GenerateInheritanceKey  enableTelemetry=YES 
_SecKeychainCopyEMCSBackup
Local reset finished with error: %@
BEGIN [%lld]: JoinAfterRestore  enableTelemetry=YES 
HybridSig: Unknown public key context type for initialization
policy \"%@\" requires kSecPolicyPolicyName, kSecPolicyName, and kSecPolicyLeafMarkerOid  input
SecTrustStoreCopyAnchors
ksd/client/accountChanged
octagon: Failed to create OTControl: %@
performing resource validation for %s (%d, %d, %d, %d)
Signature/signer verification failed: %@
END [%lld] %fs: CheckCustodianRecoveryKey  OctagonSignpostNameCheckCustodianRecoveryKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameCheckCustodianRecoveryKey}d 
END [%lld] %fs: CreateInheritanceKey  OctagonSignpostNameCreateInheritanceKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameCreateInheritanceKey}d 
END [%lld] %fs: StoreInheritanceKey  OctagonSignpostNameStoreInheritanceKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameStoreInheritanceKey}d 
SOSCircleGenerationSign: Upgraded peer's Application Signature
SecKeySetParameter
close(%d) err: %d
SOS Feature is %@ (overridden)
successfully stored octagon inheritance recovery key
Invalid PolicyMappings Extension
createCustodianRecoveryKey invoked for context: %@
SOSCCTryUserCredentialsAndDSID!! %@\n
csr: failed to create CSR signature
ML-KEM privkey size=%dbytes import of pub part failed: %d
OTSetupControlProtocol failed, continuing, but you might crash later: %@
Building default configuration for first-party bundle
BEGIN [%lld]: StoreInheritanceKey  enableTelemetry=YES 
preflight join using custodian recovery key
enter SOSCCCleanupKVSKeys
MessageSecurity and Security frameworks have different status results, returning Security result. sec: %d, ms: %d
SecKeyCopyPublicBytes
%s isn't a full path, but a relative path
fetchprerecord: Failed to get XPC connection: %@
octagon-setcdpenabled: failed to fetch OTControl object: %@
Setting CKKS4All status to '%@'
csr: failed to make signature
BUG IN SECURITY CLIENT: newPolicies contains unsupported value type
Trailer not expected length: %u, %u
%p: couldn't size XML entitlements
Failed to generate sealed resource: %d, %d, %s
sfsqlite: Error executing SQL: \"%@\" (%d)
Triggered escrow update for '%@': %@
checkCustodianRecoveryKey invoked for context: %@
Found usage constraints for %{mask.hash}@
Failing executable validation due to memory failure.
sfsqlite: Object class \"%@\" does not have prefix \"%@\"
Could not box FD: %d
_SecKeychainWriteBackupToFile
ID Comparison failed: d: %@ id: %@
32-bit linkedit is%s valid
removeFriendsInClique complete: %d
Add for bk: %@, wrapped: %@
Attempt to remove sampler without specifying samplerName
PeerDeviceNamesByPeerID
unknown ML-KEM type detected
no query dict to determine whether for system keychain: %@
SFAnalytics: cannot add sampler with interval %f
SOSCloudKeychainClearAll called
SecKeyCopyPublicKey
END [%lld] %fs: WaitForOctagonUpgrade  OctagonSignpostNameWaitForOctagonUpgrade=%{public,signpost.telemetry:number1,name=OctagonSignpostNameWaitForOctagonUpgrade}d 
SecDeleteItemsOnSignOut
Failed to create signature: %@
HybridSig: No operations available for context type
Failed to generate ML-DSA key: err %d
CodeSignature too short for new format.
cced25519_make_key_pair() failed, error %d
Invalid exceptions epoch.
Failed to encode signature: %@
choosing %s (%d,0x%x)
FetchCliqueStatus
fetchEscrowRecords complete
FetchEscrowContents
 OctagonSignpostNameGenerateInheritanceKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameGenerateInheritanceKey}d 
Failed to query view(%@): %@
HybridSig private key size validation failed: length=%ld, max=%zu
returning keychain database path as: %@
Removed all trust settings
fetchRequestWaitingOnPasscode: Failed to get XPC connection: %@
BEGIN [%lld]: CheckCustodianRecoveryKey  enableTelemetry=YES 
SOSCircleVerifySignatureExists no pubKey
Retrying operation for registered smart card key after error: %@
SecTrustEvaluateIfNecessary
Fetched current user identifier: %{public}@
END [%lld] %fs: FetchEgoPeer  OctagonSignpostNameFetchEgoPeer=%{public,signpost.telemetry:number1,name=OctagonSignpostNameFetchEgoPeer}d 
removeCustodianRecoveryKey invoked for context: %@
SOSCCResetToOffering called
API Info Called
SecKeyCreateRandomKey
STRICT VALIDATION ERROR: non-zero gap byte found
too many expiration time attributes (%d), skipping
establish returned an error: %@
WaitForOctagonUpgrade
csr: failed to generate self-signed certificate %@
unknown ML-DSA type detected
SecCodeSignerRemote: At least one valid certificate chain must be added for signing.
start building resource directory
SFAnalyticsSampler created without proper data
setNewRecoveryKeyWithData invoked for context: %@
Invalid CRL Distribution Points extension
SecSetLoggingInfoForCircleScope
sfsqlite: Statement is not reset: \"%@\"
ksmd/client/didDeclineInviteForGroupID
BEGIN [%lld]: TryUserCredentialsAndDSID  enableTelemetry=YES 
CreateCustodianRecoveryKey
failed to fetch CDP status: %@
clique-enable-walrus: failed to enable walrus: %@
Attempting to read data...
SecAccessGroupsSetCurrent begin! Setting access groups: %@
BEGIN [%lld]: WaitForInitialSync  enableTelemetry=YES 
fetchEscrowContents succeeded
isNotarized = %d
Secure Timestamp: %@
Maker %p replaces type=%d
%p caused an error during CoreEntitlements dictionary generation
Received response from Diagnostic Reporter - %{public}@/%{public}@/%{public}@: %{public}@
CMS signature verification failed: %@
BEGIN [%lld]: FetchEgoPeer  enableTelemetry=YES 
enter SOSCCCopyCircleJoiningBlob approver
%@ Sending Signature message: %@
Malformed signature file, too short: %zu, %u
octagon-setrecoverykey, SecRKCreateRecoveryKeyWithError() failed: %@
enter SOSCCCopyApplication applicant
csr: failed to decode input subject
SecTrustStoreRemoveCertificate
using numeric cdFlags=0x%x from Info.plist
fetching user-controllable-sync status errored: %@
Calling default itemsChangedBlock - fatal: %@
OTR Process Packet
failed to read signing bytes from %s(%s)
SecItemUpdateTokenItemsForAccessGroups
OctagonAuthenticatedRKJoin is %s
Generation signed updated signatures on peerinfo
skipping dup cert
ML-DSA privkey size=%dbytes import of priv part failed: %d
Encoded CMS signature: %@
can't create public key hash
ML-KEM pubkey size=%dbytes import failed: %d
MD5 fingerprint digest
SCEP failed to find algorithm to match CA fingerprint length: %ld
%s does not exist, forcing resource validation on %s
MessageSecurity and Security frameworks have different trustref results, returning Security result. sec: %@, ms: %@
coretrust decompress failed: %04x
The current exceptions epoch is %llu. (%{public}s)
SecCodeSignerRemote: Invalid certificate chain given to remote signer.
Securityd failed getting endpoint with error: %@
SFAnalytics: sampler \"%@\" already exists
END [%lld] %fs: RecoverOctagonUsingCustodianRecoveryKey  OctagonSignpostNameRecoverOctagonUsingCustodianRecoveryKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameRecoverOctagonUsingCustodianRecoveryKey}d 
enter SOSCCIsSOSTrustAndSyncingEnabled
successfully created octagon inheritance recovery key
Platform does not support the detached signature database
BEGIN [%lld]: Establish  enableTelemetry=YES 
Skipping id %@, no backup key.
Checking view / circle status for %@:  SOSCCStatus: (%@)  Error: (%@)
Readonly API rate exceeded
csr: failed to encode subject
csr: failed to encode certificate
xpc: failure to obtain XPC proxy object for upgradeIfNeeded, %@
Remote signing requires hash list.
SFSQLite: attempt to retrieve property without a key
RollIdentityOnMIDRotation override removed
octagon clique status errored: %@
copyPeerPeerInfo for context:%@, altdsid:%@
No OS String to parse
Receiving file for %@ failed, %d
message error: %s
unexpected message reply type %p
ksmd/client/fetchReceivedInvitesWithCompletion
BEGIN [%lld]: FindOptimalBottleIDsWithContextData  enableTelemetry=YES 
Invalid AuthorityKeyIdentifier Extension
cced448_make_key_pair() failed, error %d
unable to allocate data for ticket
codesign allocate error: one architecture signaled removal while another signaled signing
%p will remove signature from %p
%p unable to fixup entitlement dictionary
Resync finished with error: %@
fetching escrow records for context:%@, altdsid:%@
Setting peerInfo backupKey to %@
%s XPC request to CKD: %s
Read %u bytes
ksmd/client/didAcceptInviteForGroupID
LeaveClique
fetched user-controllable-sync status as : %@
BEGIN [%lld]: SetUserCredentialsAndDSID  enableTelemetry=YES 
adding: %@:%@
SecTrustOTASecExperimentGetUpdatedAsset
%p will sign %p (flags 0x%x)
unknown error domain: %@ for error: %@
_SecKeychainCopyBackup
SecKeyCopyKeyExchangeResult
SCEP failed to find certificate matching CA fingerprint: %@
exiting excluded path: %s
SFACollection action trigger ttr: %@: %@
HybridSig: Unknown descriptor pair for key generation
could not disable pinning: not an internal release
SecTrustStoreCopyUsageConstraints
System Keychain Always Supported set via feature flag to %s
Failed to create trust ref to verify signer: %@
 OctagonSignpostNameCopyPeerPeerInfo=%{public,signpost.telemetry:number1,name=OctagonSignpostNameCopyPeerPeerInfo}d 
generateInheritanceKey invoked for context: %@
CIRCLE:    %@
csr: failed to decode CSR subject name
Invalid key data: The provided key does not contain a valid KEM context.
SecTrustStoreSetCTExceptions
Attempt to remove multisampler without specifying samplerName
octagon-generateinheritancekey, failed to generate octagon inheritance recovery key
The exceptions epoch is %lld.
Maker %p assembles %zu blob(s) into %p (size=%u)
endpoint was null
too many hash agility attributes (%d), skipping
CopyViewUnawarePeerInfo
BEGIN [%lld]: RecoverOctagonUsingInheritanceKey  enableTelemetry=YES 
Failed to enable view(%@): %@
Invalid CertificatePolicies Extension
No error domain for error: %@
ERROR: policy \"%@\" is unsupported or requires additional inputs
challenge failed to decode with UTF8, attempting PrintableString
error converting json to dictionary: %@
checking the legacy list for %d, %@, %@
%p loaded DER blob with length %zu, %schecked
RollIdentityOnMIDRotation is %s
requestToJoinCircle for context:%@, altdsid:%@
END [%lld] %fs: CheckInheritanceKey  OctagonSignpostNameCheckInheritanceKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameCheckInheritanceKey}d 
Odd reply from CloudKeychainProxy: %@: %@
xpc: Failed to persist keychain writes: %d %@
SecKeyIsAlgorithmSupported
BUG IN SECURITY CLIENT: certificates contains unsupported value type
SecTrustCopyTrustStoreAssetVersion
Fetch finished with error: %@
ksd/client/getGroupByGroupID
SFAnalytics: cannot add sampler without name
Failed to fetch attestation certificate, not retrying
STRICT VALIDATION ERROR: invalid structure
meetsDeveloperIDLegacyAllowedPolicy = %d
codesign: could not preserve ownership of %s (was %d:%d, now %d:%d)
%zd signing bytes in %d blob(s) from %s(%s)
PreflightRecoverOctagonUsingCustodianRecoveryKey
Failed to retreive token for %@: error %d
SOSCCResetToEmpty called
unknown Kyber type detected
Storing non-system-session key into system keychain, will always lead to unusable key when retrieved from keychain!
CloudKit reset finished with error: %@
Cached prerecord for %@: %@
 OctagonSignpostNameResetAndEstablish=%{public,signpost.telemetry:number1,name=OctagonSignpostNameResetAndEstablish}d 
BEGIN [%lld]: CopyPeerPeerInfo  enableTelemetry=YES 
%s view %@
Couldn't create kpid: %@
ACME server returned certificate with public key that does not match CSR
Account creation date %@ is after cut-off %@
ksd/client/saveLocalChangesWithReply
CheckCustodianRecoveryKey
SOS Feature is %@ (via feature flags)
Targeting foreground session for uid %d
ksmd/client/fetchReceivedInviteWithGroupID
Pairing channel context configured with altDSID (%@) which does not match Clique altDSID (%@), possible issues ahead
%sorcing SIRL to be enabled (effective: %i)
SecItemUnsetCurrentItemsAcrossAllDevices
certs-only message has signers
END [%lld] %fs: ResetAndEstablish  OctagonSignpostNameResetAndEstablish=%{public,signpost.telemetry:number1,name=OctagonSignpostNameResetAndEstablish}d 
cannot read directory %s
Falling back to built-in anchors
launchBottledPeer
sending UI event for LegacyAPICounts: %@ %@
SecCmsDigestContextUpdate: data size too big (%zu), skipping
Invalid BasicConstraints Extension
SecItemCountAllWithAccessGroups
%d end of data
External block did not provide a signature, failing.
Unable to get volume capabilities from %s: %d [%s]
 enableTelemetry=YES 
resetAndEstablish started
setting user-controllable-sync status succeeded, now : %@
FindOptimalBottleIDsWithContextData
SecCodeSignerRemote: Certificate chain already added for signature slot %ld.
SecKeyCopyPersistentRef: Need a persistentRef pointer for this to work
SecTrustStoreCopyAll
SecTrustStoreContains
%p will edit signature of %p
CMS message has attached content but caller passed in detached contents, using detached contents
END [%lld] %fs: JoinAfterRestore  OctagonSignpostNameJoinAfterRestore=%{public,signpost.telemetry:number1,name=OctagonSignpostNameJoinAfterRestore}d 
%s: no cdhashes for code, cannot generate a LWCR
csr: failed to create EC public key
_SecKeychainRestoreBackup
failed to create chain from %@ to ca cert %@
unexpected connection event %p
performing resource validation on item: %s
WaitForInitialSync
Circle failed to validate after peer signature: %@
Circle accepted successfully
ML-DSA pubkey size=%dbytes is invalid
close(%d)
Requested resource was on root filesystem: %s
getattrlist return length incorrect, expected %lu, got %u
END [%lld] %fs: CopyPeerPeerInfo  OctagonSignpostNameCopyPeerPeerInfo=%{public,signpost.telemetry:number1,name=OctagonSignpostNameCopyPeerPeerInfo}d 
Invalidate EKU Extension
Dropping lock assertion
sfsqlite: Database is closed
%s is %s (via feature flags)
matching rules %@
StoreInheritanceKey
 OctagonSignpostNameCheckInheritanceKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameCheckInheritanceKey}d 
failed to decode requested CSR extensions
SecOTRSessionProcessPacketRemote
Simulating crash, reason: %@, code=%08x
flagAlways:%{bool}d inEduMode:%{bool}d flagOld:%{bool}d
resetAllRequests: %@
%s: failed to parse LightweightCodeRequirement
The size of an SecOTRDHKey is larger than 65 bytes.                      This is not supported in SecOTR and will result in malformed ciphertexts.
STRICT VALIDATION ERROR: Extra data after the last slice in a universal file (expected %zu found %zu)
%p loaded ResourceDict %p
No OS CString to parse
Error creating date from timestamp: %f
DeferSOSFromSignIn is %s
successful preflight join using custodian recovery key
unsupported value tag (%lld) found in Component Attribute dictionary, skipping
SecPasswordGenerate failed to generate a password for SecCreateSharedWebCredentialPassword.
match
SOSCCAccountSetToNew called
SecItemCopyParentCertificates_ios
SecItemSetCurrentItemAcrossAllDevices
explode_identity: Creating old persistent ref for %llu
Trust evaluate failure:%{public}@
Account Creation date: %@
OctagonStableTrustedDeviceIDInclusion is %s
OctagonRKTLKOwnershipProof overridden to %s
ksd/client/fetchRemoteChangesWithReply
BEGIN [%lld]: CreateCustodianRecoveryKey  enableTelemetry=YES 
_SecItemFetchDigests
Unable to map digest algorithm: %@
error from control: %@
An error occurred on the xpc connection to setup the background session: %@
cccurve25519_make_key_pair() failed, error %d
END [%lld] %fs: PeersHaveViewsEnabled  OctagonSignpostNamePeersHaveViewsEnabled=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePeersHaveViewsEnabled}d 
SetNewRecoveryKeyWithData
failed to post %@ result: %@ 
csr: failed to create RSA public key
Triggering TTR: %@
Couldn't validate json record: %@
NO DATA, falling back to waiting 5 minutes for initial sync to finish
SecTrustStoreRemoveAll
attestation request succeeded; got %llu certificates
resetAllRequests: Failed to get XPC connection: %@
clique status is %@; performing no Octagon actions
tryUserCredentialsAndDSID results: %d %@
END [%lld] %fs: CreateCustodianRecoveryKey  OctagonSignpostNameCreateCustodianRecoveryKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameCreateCustodianRecoveryKey}d 
 OctagonSignpostNameRemoveInheritanceKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameRemoveInheritanceKey}d 
The current exception's epoch (%llu) is not the current epoch. (%llu)
%p fixed osinstallersetupd entitlements
OctagonStableTrustedDeviceIDInclusion overridden to %s
requestStatuses: Failed to get XPC connection: %@
BEGIN [%lld]: SetNewRecoveryKeyWithData  enableTelemetry=YES 
END [%lld] %fs: PreflightRecoverOctagonUsingCustodianRecoveryKey  OctagonSignpostNamePreflightRecoverOctagonUsingCustodianRecoveryKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePreflightRecoverOctagonUsingCustodianRecoveryK
SOSCCRegisterUserCredentials - calling SOSCCSetUserCredentials for %@\n
Registering stapled ticket with system
%p xml size: %zu
using explicit identifier=%s
HybridSig pubkey validation failed
Failed to get the exception's epoch.
Unable to create digest algorithm: %@, %@
GenerateInheritanceKey
Non-compliant signature: s is %lld bytes, expected %lld
%@ Restart packet: %@
SCEP failed to create trust for %@
leaveClique invoked using context:%@, altdsid:%@
 OctagonSignpostNameAccountUserKeyAvailable=%{public,signpost.telemetry:number1,name=OctagonSignpostNameAccountUserKeyAvailable}d 
SFAnalytics: failed to open analytics db: %@
END: Circle is %s
SCEP did not find different RA certificates for signing/encryption; looking for one cert
SecTrustGetTrustStoreVersionNumber
meta directory validation on xattr file skipped: %s
Using default configuration settings
enter SOSCCProcessEnsurePeerRegistration
Modifying API rate exceeded
no extensions set
%@ Process DH failed %d
(Trust %p) Waiting for pending eval
ksd/client/updateGroupWithRequest
CMS message does not contain a EnvelopedData
 OctagonSignpostNameCreateInheritanceKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameCreateInheritanceKey}d 
(Trust %p) waiting for queue
%p desirialized size: %zu
%p will ad-hoc sign %p (flags 0x%x)
unable to create cfdata for notarization
isMessageSecurityAllowedForCurrentBundleID %s
bskb-backup: caller passed a nil backup slice keybag
csr: failed to decoder subject name from CA identity
p12Decode: Error %d adding identity to keychain
SCEP failed to find candidate RA certificates
Updated resource path: %s
%s does not contain xattrs, forcing resource validation on %s
_SecItemAddAndNotifyOnSync
Found no usage constraints for %{mask.hash}@
Unexpected digest algorithm: %@
Visiting unhandled file: %d, %s
%s: team identifier is NULL, cannot generate a LWCR
SOSFullPeerInfoCopyDeviceKey failed: %@
SecItemBackupCopyNames
SecTrustReportNetworkingAnalytics failed with error: %d
sfsqlite: Error resetting prepared statement: \"%@\"
ksd/client/createGroupWithRequest
ksmd/client/sendNewInvitesForGroup
RecoverOctagonUsingCustodianRecoveryKey
PerformedCDPStateMachineRun
Unable to save octagon signing key to the keychain
Kyber privkey size=%dbytes import of priv part failed: %d
policy \"%@\" requires kSecPolicyPolicyName input
sfsqlite: Error binding int64 at %ld: \"%@\"
END [%lld] %fs: PeerDeviceNamesByPeerID  OctagonSignpostNamePeerDeviceNamesByPeerID=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePeerDeviceNamesByPeerID}d 
waitForInitialSync for context:%@, altdsid:%@
Failed to parse CONS SEQ of ident
%@ Creating with M: %@, T: %@
using default identifier=%s
%s added complex (rule %p)
unable to create otcontrol: %@
BEGIN [%lld]: RecoverOctagonUsingCustodianRecoveryKey  enableTelemetry=YES 
Error checking concurrence: %@
API Trigger Timed Called
Invalid Authority Information Access extension
SHA1 fingerprint digest
Failed to copy apple anchors: %@
SecDeleteInternalItemsOnSignOut
SecTrustReportNetworkingAnalytics
Unable to check QA certificate status: %d
OctagonRKTLKOwnershipProof is %s
current status is Not In; no need to leave
END [%lld] %fs: RemoveCustodianRecoveryKey  OctagonSignpostNameRemoveCustodianRecoveryKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameRemoveCustodianRecoveryKey}d 
enter SOSCCCopyInitialSyncData approver
identityWithError: %@
STRICT VALIDATION ERROR: gap size does not match expected (%zu != %zu)
%p executable validation threw non-common exception
Unexpected item hit traversing resource: %@
JoinAfterRestore
sos-compatibility-mode-cached: fetching compatibility mode error: %@
SecTrustCopyTrustStoreContentDigest
Unable to get team ID (OrganizationalUnitName) from Apple signed certificate
BEGIN [%lld]: ResetAndEstablish  enableTelemetry=YES 
BEGIN [%lld]: CopyViewUnawarePeerInfo  enableTelemetry=YES 
dlsym libnetwork nw_protocol_options_access_handle
END [%lld] %fs: FetchEscrowContents  OctagonSignpostNameFetchEscrowContents=%{public,signpost.telemetry:number1,name=OctagonSignpostNameFetchEscrowContents}d 
%s: failed to retrieve hw.osenvironment (error: %s)
coretrust compress failed: %04x
xpc: failure to obtain XPC proxy object for app clip deletion, %@
Expected valid trailer, but CodeSignature file too short.
Requesting a CloudKit reset for view %@
ksd/client/getGroupsWithRequest
Piggybacking version 0, setting initial sync timeout to 5 minutes
Invalid Name Constraints extension
SecItemDelete_ios
SFAnalytics: multisampler \"%@\" already exists
fetching current status errored: %@
accountUserKeyAvailable for context:%@, altdsid:%@
ignoring entry in success counts table without an event name
Unable to read signature index %d: %d
unexpected blob type 0x%x in slot %d of binary dependencies
skipping expration time that failed to decode: %@
requestToJoinCircle platform does not support SOS
successfully upgraded to octagon
Failed to parse CONS SEQ
Unable to save octagon encryption key to the keychain
SOSCircleEnsureRingConsistency requires ring signing op
entering %s
Checking resolved resource path for containment: %s
failed to decode CMS message: %@
leaveClique errored: %@
storeInheritanceKey invoked for context: %@
sos trust and syncing is %@
Requesting lock assertion for %lld seconds
using inherited cdFlags=0x%x
 OctagonSignpostNamePeersHaveViewsEnabled=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePeersHaveViewsEnabled}d 
csr: failed to verify signature in CSR
csr: failed to decode encoded certificate
HybridSig: Unknown private key context type for destruction
Secure timestamp %@ is after cut-off %@
sfsqlite: Error opening db at %@: %@
API Trigger Timed returned: %d
opcode 0x%x cannot be handled; aborting
Securityd failed getting whoamid with error: %@
SFA: underlyingErrors failed to encode %{public}@ with failure: %{public}@
Building default configuration for third-party bundle
BEGIN [%lld]: CreateInheritanceKey  enableTelemetry=YES 
Invalid ML-KEM type %@ requested for ML-KEM key generation
BUG IN SECURITY CLIENT: responseData array contains non-data value
Failed to fetch attestation certificate, %u retries left
missing %@ for attestation
cachePrerecord: Failed to get XPC connection: %@
 OctagonSignpostNameRemoveCustodianRecoveryKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameRemoveCustodianRecoveryKey}d 
csr: failed to encode cert request
connection error: %s
instantiating CFBundle for %s
%p cannot find CODESIGNING data in Mach-O
Not running experiments for disallowed process
DeferSOSFromSignIn override removed
dlsym libnetwork nw_protocol_options_copy
SecCMSVerify called without policy -- skipping verification!
Failed to regenerate circle with new gen count: %@  current gencount: %@  error: %@
bad hash %@ in backup
SecGetCurrentServerLoggingInfo
symlink %s
xpc: have been trying %d times to get a securityd connection
successfully checked inerhitance key
Unsupported algorithm oid
 OctagonSignpostNamePreflightRecoverOctagonUsingCustodianRecoveryKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePreflightRecoverOctagonUsingCustodianRecoveryKey}d 
BUG IN SECURITY CLIENT: certificates array contains non-certificate value
unexpected regexec result %d for path '%s'
cliqueStatus noOTControl
octagon: friends removed: %@
 OctagonSignpostNameFindOptimalBottleIDsWithContextData=%{public,signpost.telemetry:number1,name=OctagonSignpostNameFindOptimalBottleIDsWithContextData}d 
 OctagonSignpostNameFetchEscrowContents=%{public,signpost.telemetry:number1,name=OctagonSignpostNameFetchEscrowContents}d 
RemoveCustodianRecoveryKey
BEGIN [%lld]: PreflightRecoverOctagonUsingInheritanceKey  enableTelemetry=YES 
%@ Failed to process reveal sig message (%d): %@
BUG IN SECURITY CLIENT: newPolicies array contains non-policy value
triggerEscrowUpdate: Failed to get XPC connection: %@
Full contents: %@
%s Peer %@ is %s
ccec448_make_key_pair() failed, error %d
Unexpected scan input: %d, %s
Requested resource was not within the code object: %s, %s
END [%lld] %fs: AccountUserKeyAvailable  OctagonSignpostNameAccountUserKeyAvailable=%{public,signpost.telemetry:number1,name=OctagonSignpostNameAccountUserKeyAvailable}d 
csr: unsupported subject CFType
sfsqlite: Statement not reset after last use: \"%@\"
sfsqlite: Error binding int at %ld: \"%@\"
missing value reply
got event: %s
Caller passed a detached content by the content is not a data type.
failed to set CDP bit: %@
CKP Transport: desktopUp happened, reestablishing xpc connections
%p creating new CEQueryContext DER blob with length %lu
App Transport Security exception must be a dictionary
session[%p] failed to decrypt, session: %@, mk: %@, mpk: %@, tpk: %@, tk: %@, chose tktu: %@
copyPeerPeerInfo results: %@ (%@)
More than one cloud identity found, first had error, trying new one.
SecKeyCreate init(%{public}s) failed: %d
Got external signature blob: %@
peersHaveViewsEnabled results: %{BOOL}d (%@)
(Trust %p) No pending evals, starting
API Info returned
ksd/client/performMaintenanceWithCompletion
removeFriendsInClique failed: unable to remove friends: %@
establish succeeded
MessageSecurity and Security frameworks have different signed attributes results, returning Security result. sec: %@, ms: %@
SecItemShareWithGroup
policy \"%@\" requires kSecPolicyName input
%s check-fixed (added).
Unable to convert %s to its filesystem mount [statfs failed]: %d [%s]
sfsqlite: Error binding blob at %ld: \"%@\"
CMS message has %d signers, expected 1
CKP Transport: xpc connection invalid. Will tear down connection.
Value %{public}@ for key %{public}@ is not bool
unload bag failed: %d
Unable to create signed data: %@
SFA: underlyingErrors encoded to not json %{public}@
fetchEscrowContents errored: %@
BEGIN [%lld]: CreateInheritanceKeyWithClaimTokenAndWrappingKey  enableTelemetry=YES 
HybridSig pubkey size=%dbytes import of pub part failed: %d
SecTrustStoreSetTransparentConnectionPins
octagon-removeinheritancekey, failed to remove inheritance key
 OctagonSignpostNameWaitForOctagonUpgrade=%{public,signpost.telemetry:number1,name=OctagonSignpostNameWaitForOctagonUpgrade}d 
%p (%s) unloaded
%d sealed resource(s) not found in code
path is NULL
Received accountChanged notification, invalidating cached current user identifier: %{public}@
removeFriendsInClique invoked using context:%@, altdsid:%@
Can't validate PeerInfo: %@
csr: cert request encoding failed: %@
Loaded existing DetachedCertificates.der for merging
END [%lld] %fs: LeaveClique  OctagonSignpostNameLeaveClique=%{public,signpost.telemetry:number1,name=OctagonSignpostNameLeaveClique}d 
BEGIN [%lld]: PreflightRecoverOctagonUsingCustodianRecoveryKey  enableTelemetry=YES 
successfully created octagon inheritance recovery key (w/claim+wrappingkey)
successfully fetched CDP status as %@
sfsqlite: Error closing database
using system keychain XPC
peerDeviceNamesByPeerID invoked using context:%@, altdsid:%@
joinAfterRestore complete: %d %@
Not a known view
SecTrustEvaluateIfNecessaryFastAsync
looks like a script for %s
Could not create pipe: %d
ksd/client/receivedGroupInvitation
error:[%d] %@
Fixed TCC entitlements for osinstallerstupd %d
failed to remove stale DetachedCertificates.der: %s (errno %d)
too many signing time attributes (%d), skipping
 OctagonSignpostNameWaitForInitialSync=%{public,signpost.telemetry:number1,name=OctagonSignpostNameWaitForInitialSync}d 
enter SOSCCPushResetCircle
Skipping URI SAN missing valid scheme: %@
Failed to export public key: error code %d.
 OctagonSignpostNamePeerDeviceNamesByPeerID=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePeerDeviceNamesByPeerID}d 
waitForInitialSync waited: %d %@
%@
Skipping subtrees after the first %d
SWC received didCompleteWithAuthorization
Unable to create signer due to old CMS interfaces
Unable to create iPhoneProfileApplicationSigning SecPolicy
sfsqlite: Failed to step (%d): \"%@\"
END [%lld] %fs: CreateInheritanceKeyWithClaimTokenAndWrappingKey  OctagonSignpostNameCreateInheritanceKeyWithClaimTokenAndWrappingKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameCreateInheritanceKeyWithClaimTokenAndWrappingK
enter SOSCCIsSOSTrustAndSyncingEnabledCachedValue
csr: failed to encode public key
Successfully persisted keychain data to disk
Failed to remove trust settings for %{mask.hash}@, %d
App Transport Security value for key %s must be a boolean
Accepted peer: %@
Failed to find my private key for spid %@
sfsqlite: Error binding double at %ld: \"%@\"
sfsqlite: Unexpected column type: %d
ksd/client/fetchCurrentUserIdentifierWithReply
TriggerABC for %{public}@/%{public}@/%{public}@
END [%lld] %fs: SetNewRecoveryKeyWithData  OctagonSignpostNameSetNewRecoveryKeyWithData=%{public,signpost.telemetry:number1,name=OctagonSignpostNameSetNewRecoveryKeyWithData}d 
successfully created octagon custodian recovery key
Failed at bk: %@ error: %@
no metapath for %s
Received statuses: %@ %@
skipping hash agility V2 attribute that failed to decode: %@
fetchEscrowRecords succeeded: %@
Unable to get file metadata for %@, fd %d
SecTaskLoadEntitlements: failed to get cs_flags, error=%d, pid=%d
Unable to create signing algorithm: %@
%s added simple (rule %p)
areCertChainsSimilar: Certificate chains are similar
leaveClique complete: %d
setting user-controllable-sync status errored: %@
talkWithKVS error: %@
Invalid SubjectKeyIdentifier Extension
SecItemCertificateExists
Possibly targeting foreground session
RemoveInheritanceKey
enter SOSCCPeersHaveViewsEnabled
%@ Error %d processing packet type %d, session state %d, keyid %d, myKey %p, myNextKey %p, theirKeyId %d, theirKey %p, theirPreviousKey %p, bytes %@
(Trust %p) Started eval block
endpoint was not an endpoint
SecEscrowRequestSetupControlProtocol failed, continuing, but you might crash later: %@
Stored %d records: %@
AccountUserKeyAvailable
BEGIN [%lld]: PerformedCDPStateMachineRun  enableTelemetry=YES 
csr: failed to encode TBS
Kyber privkey size=%dbytes import of pub part failed: %d
could not disable pinning: %@ not true
BEGIN [%lld]: FetchCliqueStatus  enableTelemetry=YES 
Too many views defined, can't make bitmask (%d)
csr: failed to create Hybrid Composite Public Key (draft-13)
SecKeyCreateDecryptedDataWithParameters
SecTrustCopyAppleTrustAnchors
Could not read trailer due to read error: %d
%s: match target %s against %s
%p will sign %p (flags 0x%x) with certs: %@
metrics_memory
API Called
SecKeyCreateAttestation
Kyber pubkey size=%dbytes import failed: %d
Trying to release a CE managed context
CKP Transport: setting up xpc connection
SecItemAdd_ios
SecKeyCopyAttributes
Unable to create signature digest: %@, %@
connection interrupted %@
SOS disabled for this platform, returning NULL
establish complete: %{BOOL}d
BEGIN [%lld]: WaitForOctagonUpgrade  enableTelemetry=YES 
successfully enabled walrus
Peers In Circle:
Encountered error closing file %@: %d
Unable to copy certChain array
metrics_cpu
OctagonAuthenticatedRKJoin override removed
Unknown NIAP TLS package version: %{public}s, treating as recommended
copyViewUnawarePeerInfo for context:%@, altdsid:%@
SetUserCredentialsAndDSID
octagon-setrecoverykey, failed to create octagon recovery key
 OctagonSignpostNameRecoverOctagonUsingInheritanceKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameRecoverOctagonUsingInheritanceKey}d 
Rejected Applicants To Circle:
CKKSSetupControlProtocol failed, continuing, but you might crash later: %@
failed to read the recipient after decoding
SecKeyCopyPersistentRef: Need a key reference for this to work
SecIdentityCreate: failed to extract public key from private key
SecKeyCreateDuplicate
Registered smart card token not found -> retrying to get the session
SecKeyCopyPersistentRef: received status %i for key %@
%@ %@: %@
ML-DSA priv size=%dbytes is invalid
sfsqlite: Error binding text at %ld: \"%@\"
policy is not a SecPolicy or CFArr0ay
 OctagonSignpostNamePerformedCDPStateMachineRun=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePerformedCDPStateMachineRun}d 
HybridSig priv key size=%dbytes import of priv part failed: %d
Creating SecIdentity with mismatching public keys: %{mask.hash}@, %{mask.hash}@
resource validation on root volume skipped: %s
%p reconstituting XML entitlements with context %p
ksd/client/verifyGroupsInSyncWithCompletion
fetchEscrowRecords errored: %@
Setting peerInfo backupKey to NULL
Initial sync completed for view %@: %{BOOL}d
ksd/client/verifyGroupsInSyncAndResyncMissingGroupsWithCompletion
Skipping sending event %@ due to process configuration
octagon: removing octagon friends: %@
BEGIN [%lld]: LeaveClique  enableTelemetry=YES 
BEGIN [%lld]: RecreateInheritanceKey  enableTelemetry=YES 
successfully recreated octagon inheritance recovery key
error in SOSCircleAcceptRequest\n
successfully set octagon recovery key
 OctagonSignpostNameCreateInheritanceKeyWithClaimTokenAndWrappingKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameCreateInheritanceKeyWithClaimTokenAndWrappingKey}d 
Couldn't json validate rockwell record: %@
privKey failed to be created
SecKeyVerifySignature
Set TrustSettings for %{mask.hash}@
SecTrustStoreSetCARevocationAdditions
%d zero read (ignored)
xpc: Unable to re-enqueue securityd connection because already at limit
Did not get a database! (Client %@)
octagon, failed to fetch OTControl object: %@
%p Bundle from path %s(%s)
SFSQLite: attempt to set property without a key
Not showing ttr due to ratelimiting: %@
Local resync finished successfully
SFAnalytics: Need a valid result and name to log result
csr: failed to encode request info
SecKeyCreateSignature
BUG IN SECURITY CLIENT: anchorCertificates array contains non-certificate value
(Trust %p) Completed async eval kickoff
posted error: %@:  %@
_SecKeychainCopyKeybagUUID
unexpected content type %@
failed to join using custodian recovery key: %@
CreateInheritanceKey
couldn't delete view %@
SOSCopyDeviceBackupPublicKey (%@)
ML-DSA pubkey size=%dbytes import failed: %d
der: unable to encode date: %@
Cannot init db without schema
OctagonStableTrustedDeviceIDInclusion override removed
failed to fetch escrow statuses: %@
PeersHaveViewsEnabled
replaced by performEscrowRecoveryWithContextData:escrowArguments:error: remove call
clique-disable-walrus: unable to create otcontrol: %@
failed to serialize resource directory (possibly too many resource rules sharing one value): %@
END [%lld] %fs: RequestToJoinCircle  OctagonSignpostNameRequestToJoinCircle=%{public,signpost.telemetry:number1,name=OctagonSignpostNameRequestToJoinCircle}d 
END [%lld] %fs: RecoverOctagonUsingInheritanceKey  OctagonSignpostNameRecoverOctagonUsingInheritanceKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameRecoverOctagonUsingInheritanceKey}d 
octagon-checkinheritancekey, failed to check inheritance key
csr: failed to decode challenge
stackshot report, reason: %@, code=%08x
%d fcntl(%d,%p) = %d
 OctagonSignpostNameRecoverOctagonUsingCustodianRecoveryKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameRecoverOctagonUsingCustodianRecoveryKey}d 
csr: extension encoding failed: %@
Invalid kyber type %@ requested for Kyber key generation
Checking resolved path for containment: %s
Unable to get digest of certificate at index %lld
attestation request failed with error %@
SFACollection unknown action: %@
BEGIN [%lld]: PeersHaveViewsEnabled  enableTelemetry=YES 
END [%lld] %fs: RecreateInheritanceKey  OctagonSignpostNameRecreateInheritanceKey=%{public,signpost.telemetry:number1,name=OctagonSignpostNameRecreateInheritanceKey}d 
SecOTRSessionCreateRemote
CFStringCreateWithCString failed
Requested resource was not sealed: %d
test %s
ksd/client/leaveGroupWithRequest
joinAfterRestore for context:%@, altdsid:%@
failed to find adaptor: operation=%d, algorithm=%{public}@ (adaptors:%d)
file %s
%p: couldn't deserialize XML entitlements
octagon-createinheritancekey, failed to create octagon inheritance recovery key
failed to create chain %@
Failed set trust settings for %{mask.hash}@, %d
%s doesn't match Xattr file path spec
successfully checked custodian recovery key
csr: failed to encode outer subject sequence
Requested resource was not found: %s
LocalKeychainAnalytics
SecEscrowRequest
SOSAnalytics
OTConfigurationContext
SecKeyProxyProtocol
SecXPCUtils
ExternalPreSharedKey
SOSCachedNotification
SecSessionInfo
KCSharingXPCServerProtocol
TPStableTrustedDeviceID
OTBottleIDs
SOSControlProtocol
ASAuthorizationControllerDelegate
SecKeyProxy
SecCBORNegative
SFAnalyticsActivityTracker
KCSharingXPCClientProtocol
SecuritydXPCCallback
OS_sec_certificate
SecTapToRadar
KCSharingDaemonConnection
FakeSecuritydXPCClient
SecConcrete_sec_protocol_configuration_builder
CKUtilsAdditions
SECSFARule
SecCBORData
SFAnalyticsMultiSampler
OTJoiningConfiguration
SECSFARules
CKKSControl
TrustdFileHelper_protocol
SecCBORArray
SFSQLite
NSSecureCoding
OfferedEPSK
KCSharingGroupManager
SFAnalyticsCollection
OTClique
SFAnalyticsEvent
SecJWSDecoder
SecCBORValue
SFSQLiteStatement
SecOfferedEPSK
SecCBORUnsigned
DetachedCertificateEntry
SFSQLiteAdditions
KCSharingGroupCreateRequest
NSCoding
SECSFAEventRule
SecJWSEncoder
SecABC
SFAnalyticsCollectionAction
SecItemCurrentItemData
SecOfferedPAKEIdentity
SecConcrete_sec_array
KCSharingGroupLeaveRequest
SecLaunchSequence
SECSFAAction
SECSFAEventFilter
OS_sec_protocol_configuration_builder
NSXPCListenerDelegate
KCSharingGroup
SecAsyncPiper
SecExternalPreSharedKey
SecuritydXPCClientInterface
SECSFAMatchProperty
CKKSCurrentItemQuery
KCSharingGroupDeleteRequest
SECSFAVersionMatch
OS_sec_protocol_configuration
CKKSCurrentItemQueryResult
DetachedCertificatesFile
KCSharingGroupFetchRequest
TPMIDStableTrustedDeviceID
SFObjCType
KCSharingMessagingdConnection
SecuritydXPCProtocol
KCSharingGroupUpdateRequest
SecExperiment
SFACollection
KCSharingGroupUpdateInfo
SecXPCHelper
SFAnalyticsSQLiteStore
SecConcrete_sec_identity
SecKeyProxyTarget
SFAnalyticsProtocol
SharedCredentialController
SecCBORString
SECSFAActionAutomaticBugCapture
OS_sec_array
SecCoreAnalytics
SecConcrete_sec_trust
SFAnalytics
OS_sec_trust
ASAuthorizationControllerPresentationContextProviding
SecCBORMap
OTControlArguments
SECSFAPropertyValue
EscrowRequestXPCProtocol
SecSFAParsedCollection
LKAUpgradeOutcomeReport
SECSFAActionDropEvent
SecuritydXPCCallbackProtocol
SECSFAVersion
OTOperationConfiguration
SecCTKKey
NSObject
CKKSExternalTLKShare
SecuritydXPCClient
KCSharingGroupInvite
SecEscrowRequestable
SecSOSStatus
CKKSPCSIdentityQuery
SecExpConcrete_sec_experiment
OS_sec_experiment
CKKSExternalKey
KCSharingInvitationNotificationProtocol
KCSharingParticipant
SFAnalyticsMatchingRule
OS_sec_identity
CKKSPCSIdentityQueryResult
SecExperimentConfig
OTControlProtocol
KCSharingMessagingdXPCServerProtocol
SecItemRateLimit
CKKSControlProtocol
DefaultCollectionActions
SecConcrete_sec_protocol_configuration
OTSerializedPlistEscrowRecord
DetachedCertificatesLookup
KCSharingGroupManagerSubscriberProtocol
SecConcrete_sec_certificate
AcmeCertRequest
NSCopying
SecLaunchEvent
SFAnalyticsSampler
SFSQLiteRow
OTMetricsSessionData
OTControl
SECSFAActionTapToRadar
T@\"NSData\",R,V_senderPeerID
_launchOperation
insertString:atIndex:
intAtIndex:
predicateMatchingGroupsWithName:
streamEventsWithLimit:fromTable:eventHandler:
T@\"NSString\",R,C,N,V_inviteeHandle
TB,N,GisReset,V_reset
attestationChainPEMRepresentation
signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:
signingKey:
setStableTrustedDeviceIDStatus:
_attestationOids
_compatibilityVersion
_configurationData
_keyID
addCertificateChainWithLeaf:intermediate:root:error:
controlObject:
hasMigrated
joinAfterRestore:
setServiceNumber:
successCountForEventType:
_SQLite
initFromKey:
userPublicKey:
_displayName
reset
sharedConnection
keyStatusFor:complete:
numberWithLongLong:
storeWithPath:schema:
bigData
eventsRelativeTime
getAttributesWithReply:
_acmeNewAccountURL
makeCKKSControl:
parseRules:format:error:
rockwells
setLeafCertificates:
_reason
T@\"NSData\",R,V_signature
setCkksControl:
_validateJWSSignature:ofHeader:andPayload:withPublicKey:
identity
isSamplingDisabled
removeParticipant:
cliqueMemberIdentifier
intValue
isRateLimited:
setKey:value:
setupPairingChannelAsAcceptor:
triggerEscrowUpdate:error:
LAContext
_requireAttestation
certificateURL
dictionaryWithDictionary:
extractSKIDFromCertificate:certificateName:error:
initWithToken:LAContext:parameters:error:
eventRulesCount
T@\"NSString\",R,N,V_schemaVersion
TQ,N,V_timeoutWaitForCKAccount
currentItemPointerModificationTime
icscRepairReset:reply:
launch
T@\"<SFAnalyticsCollectionAction>\",&,V_actions
idMSTrustTimestamp
initWithSQLite:SQL:handle:
fetchAccountWideSettingsWithForceFetch:arguments:reply:
fuzzyNumber:
rateLimitingPerformanceCounters:
setContainerName:
SOSMonitorModeSOSIsActive
isOctagonExcluded:
setDomain:
type
loadCertificatesFileMatching:skid:
consumeTokenFromBucket:
encodeObject:forKey:
hasMatch
session
fleetSampleRate
_attestationChain
columnNamesForTable:
metricsReport
provisionWithReply:
initWithArray:
lookupCertificatesForExecutable:skid:error:
matchAttributes:eventClass:processName:logger:
decryptedRecord
createRequest
setHasAction:
setSignature:
T@\"NSString\",R,C,N,V_senderHandle
TB,V_permitLocalIssuer
_roCapacity
cachePrerecord:serializedPrerecord:error:
deleteFrom:where:bindings:
escrowCheck:isBackgroundCheck:reply:
init
initWithDataContent:isDetached:signer:signerChainMode:error:
T@\"NSNumber\",&,V_measurement
T@\"NSString\",&,N,V_componentVersion
_attestationCRKey
hostHash
initWithAltDSID:flowID:deviceSessionID:canSendMetrics:
setOverrideForJoinAfterRestore:
logAcmeCSR
resetStaticRateLimit
setClient_identity:
triggerAutoBugCaptureWithType:subType:subtypeContext:domain:events:payload:detectedProcess:
userVersion
T@\"KCSharingGroup\",R,N,V_group
_controller
canPersistMetrics
declineInviteForGroupID:completion:
setHasInteger:
setRemoteObjectInterface:
stringByReplacingOccurrencesOfString:withString:
TB,N,V_matchOnFirstFailure
datePropertyForKey:
setAllowedBuilds:
hasType
URL
T@\"NSString\",C,N,V_context
class
setExcludeEvent:
_date
_error
hasAction
initWithSKID:certificate:akid:
fetchStableTrustedDeviceID:reply:
isEqual:
containsObject:
callback
hasDropRate
hasString
setAttestation:
_uniqueDeviceID
addEventDict:toTable:timestampBucket:
extractAKIDFromCertificate:certificateName:error:
setProperty:forKey:
_record
_statementsBySQL
establish:
isRegisteredSmartcard
sign_block
T^{sqlite3_stmt=},R,N,V_handle
_propertyName
matchesInString:options:range:
protocolType
removeAllSamplesForName:
setOrderURL:
setUserVersion:
T@\"NSDate\",R,N,V_rwBucket
_tableNameForClass:
substringFromIndex:
T@\"SECSFAActionTapToRadar\",&,N,V_ttr
entitlementsFact:
initWithKey:
removeLegacyDefaultAnalyticsDatabasePath:usingDispatchToken:
traced
all
tlkUUID
Ti,N,V_userVersion
fileExistsAtPath:
initialSyncCredentials:altDSID:flowID:deviceSessionID:canSendMetrics:complete:
numberWithUnsignedLongLong:
sendMetricWithResult:error:
base64EncodedStringWithOptions:
StringAsProperty:
_eventFilters
dateWithTimeIntervalSince1970:
notifyIDMSTrustLevelChangeForAltDSID:reply:
T@\"NSString\",R,N,V_name
productNameAsString:
self
sync
hasExcludeCount
statementForSQL:
setCachedCurrentUserIdentifier:
circleHash:
hasAlert
select:from:where:bindings:
setOldDateFormatter:
T@\"NSString\",R,V_tlkUUID
dictWithError:
fetchTrustedDeviceList:reply:
performedCDPStateMachineRun:success:error:reply:
setQueryItems:
isEqualToArray:
T@\"TKClientTokenObject\",&,N,V_tokenObject
_verificationError
errorWithCode:description:
isVersionSameOrNewer:than:
leafCertificates
TB,V_excludedVersion
_passwordEquivalentToken
ckksControl
initFromRow:
reset:
tlkRecoverabilityForEscrowRecordData:recordData:source:reply:
updateGroupWithRequest:completion:
T@\"NSDictionary\",&,V_config
_machineID
setDateProperty:forKey:
T@\"NSString\",R,N,V_keyID
_disableLogging
T@?,C,V_tearDownMetricsHook
discretionaryNetwork
fetchStatuses:
initWithName:value:
otControl
encoder
setRadarnumber:
setSynchronous:
T@\"NSString\",R,N,V_encoding
addAttribute:value:
connectionWasInvalidated
getCDPStatus:reply:
initWithExternalizedContext:
groupInvitationWasCancelled
setCDPEnabled:reply:
setTimestamp:
sortCertificateArrays
ttr
Td,R,N,V_limitMultiplier
initWithInnerExperiment:
pathExtension
removeSubscriber:
Td,R,N,V_roRate
numberWithLong:
_location
_semaphore
doAction:attributes:logger:
objectClassPrefix
JSONObjectWithData:options:error:
_setError
escrowCompletedWithinLastSeconds:
evaluateAccessControl:aksOperation:options:error:
getDescriptionWithReply:
hash
TQ,V_ticket_creation_time
_isRegisteredSmartcard
armKey
getPublicKey:
m_data
performAction:
protocolWithSync:errorHandler:
T@\"NSArray\",&,V_preferredBottleIDs
clientDisconnectionHandler
resume
verifySignatures:
rpcKnownBadStateForViews:reply:
flowID
insertOrReplaceInto:values:
isNumber
receivedGroupInvitation:
setDaemonConnection:
client_identity
allKeys
metricsAccountID
setDropRate:
_rule
bindInt:atIndex:
initWithConnection:interface:queue:
samplingDisabled
setExcludedVersion:
setFleetSampleRate:
stringValue
_publicKeyProxy
fuzzyInteger:
_readHandle
initWithPredicate:
overrideEscrowCache
setExportedInterface:
setRootCertificates:
writeToPath:error:
T@\"NSData\",R,V_receiverPeerID
TB,N,V_overrideForSetupAccountScript
_xpc_queue
dailyMetrics
predicateWithValue:
hasValue
setConnection:
startLogSystemMetricsForActivityNamed:
T@\"NSString\",&,V_nonce
UUIDString
_authorizationURL
attestationChain
clientCanEditPreferenceOwnership
dataWithCapacity:
hasError
initWithSecKey:
hasRadarDescription
orderURL
T@\"NSString\",&,N,V_subtype
setSelfVersion:
eventType
setIsRegisteredSmartcard:
T@\"NSString\",&,V_altDSID
T@\"NSString\",R,V_view
T@\"NSMutableData\",&,V_bigData
createTrustObjectWithPolicies:error:
secItemFetchPCSIdentityByKeyOutOfBand:forceFetch:complete:
setOpenCount:
typeForEncoding:
T@\"NSString\",R,C,N
_deviceSessionID
initWithName:
setTicket_age_add:
commitKeyWithError:
saveLocalChangesWithReply:
setLocale:
setPasswordEquivalentToken:
setupMetricsHook:
timeIntervalSinceReferenceDate
_psk
containerName
initWithCertificate:signatureAlgorithm:useIssuerAndSerialNumber:error:
newTimer
numberOfRanges
removeAllObjects
rpcResetCloudKit:reason:reply:
userInfo
isGuitarfish
postCDPFollowupResult:success:type:error:reply:
secItemPersistKeychainWritesAtHighPerformanceCost:
versionsAtIndex:
_csr
dataWithData:
errorWithCode:description:underlying:
setInterruptionHandler:
pcsMirrorKeysForServices:reply:
dataWithContentsOfFile:options:error:
enumerateKeysAndObjectsUsingBlock:
initWithSPAKE2PLUSV1Context:clientIdentity:serverIdentity:clientPasswordVerifier:serverPasswordVerifier:registrationRecord:
intermediateCertificates
orderedSetWithCapacity:
rpcResetLocal:reply:
T@\"NSMutableArray\",&,N,V_eventFilters
TB,N,V_isInitiator
Tq,V_stableTrustedDeviceIDStatus
accountChanged
peersHaveViewsEnabled:error:
passwordEquivalentToken
rangeAtIndex:
TB,R,N
extractSKIDFromCMSData:error:
retainedTemporaryBoundObject:
T@\"NSString\",C,N,V_flowID
T@\"NSURL\",R,C,N,V_shareURL
secItemFetchCurrentItemAcrossAllDevices:identifier:viewHint:fetchCloudValue:complete:
setMatchingDictionary:
ghostBustPeriodic:complete:
isReset
setTokenObject:
_traced
isEqualToStableTrustedDeviceID:
_drop
_parameters
T@\"NSString\",&,V_containerName
UUID
_setQueue:
allowedEvents
hasAllowedBuilds
logHardFailureForEventNamed:withAttributes:
stringWithCString:encoding:
tryUserCredentialsAndDSID:password:error:
T@\"NSString\",&,V_radarDescription
invertedSet
listOfRecords:
T@\"KCSharingGroup\",R,N,V_updatedGroup
T@\"NSDateFormatter\",&,N,V_oldDateFormatter
trustedFullPeers:reply:
tryUserCredentialsWithLabel:password:dsid:error:
analyze
T@\"NSString\",&,N,V_eventType
setPsk:
_state
executeRequest
setPosition:
supportsSecureCoding
T@\"NSDate\",&
_invitedBy
regularExpressionWithPattern:options:error:
storePrerecordsInEscrow:
vacuum
T@\"NSArray\",&,V_attestationChain
rwBucket
_synchronousMode
archivedDataWithRootObject:requiringSecureCoding:error:
waitForPriorityViewKeychainDataRecovery:reply:
_corrupt
attributeType
externalizedContext
isModifyingAPICallWithinLimits
setIntermediateCertificates:
numRuns
CKDataWithHexString:
_events
setMatch:
signatureWithProtectedHeader:payload:
compactJSONStringRepresentationWithDictionary:
oldDateFormatter
replaceOccurrencesOfString:withString:options:range:
setAlert:
_acmeNewOrderURL
_senderHandle
blob
fieldType
validatedStashedAccountCredential:flowID:deviceSessionID:canSendMetrics:complete:
StringAsAction:
TB,R,N,GisFloatingPointNumber
_inviteStatus
addRockwellDict:userinfo:toTable:timestampBucket:
attributesOfItemAtPath:error:
indexOfObjectPassingTest:
TB,R,N,GisIntegerNumber
initWithOutcome:attributes:
setOctagonCapableRecordsExist:
shouldRunWithSamplingRate:
T@\"NSDictionary\",R,N,V_keychainAttributes
resetAccountCDPContents:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:reply:
_oncePerReport
_openCount
debugDescription
logSoftFailureForEventNamed:withAttributes:timestampBucket:
rpcVoucherWithArguments:configuration:peerID:permanentInfo:permanentInfoSig:stableInfo:stableInfoSig:maxCapability:reply:
setNonce:
_receiverPeerID
T@\"NSString\",C,N,V_cliqueMemberIdentifier
establish:error:
indexForColumnName:
logMetric:withName:oncePerReport:
safeErrorCollectionClasses
setInvalidationHandler:
T@\"NSData\",R,N,V_signature
noteEventNamed:timestampBucket:
certificate
remove
sendRequestToXPCService:response:
setCollection:
setMajor:
signingTime
_matchOnFirstFailure
dataUsingEncoding:
recoverWithRecoveryKey:recoveryKey:reply:
stableTrustedDeviceIDStatus
T@\"NSString\",&,V_acmeNewAccountURL
noteEventNamed:
_abc
_componentVersion
copyApplicationIdentifier
TC,R,N
_cachedCurrentUserIdentifier
_keyData
initWithAltDSID:flowID:deviceSessionID:
setIndexesByColumnName:
leafSKIDMap
secItemDigest:accessGroup:complete:
select:from:
_configVersion
endpoint
forTestingOnlySetFailXpcFdWrapping:
initWithServiceNumber:accessGroup:publicKey:zoneID:
encodedJWSWithPayload:kid:nonce:url:error:
serialNumber
numberWithBool:
_shareURL
authenticationAppleID
preferredBottleIDs
rpcFetchAndProcessChangesIfNoRecentFetch:reply:
setEvent:
TQ,R,N,V_size
akid
external_identity
icscRepairInvalidateCacheVersion:reply:
initWithSigningTime:
queue
removeLocalSecureElementIdentityPeerID:secureElementIdentityPeerID:reply:
substringToIndex:
_match
bindValues:
predicateMatchingGroupsWithInviteStatus:
secItemUnsetCurrentItemsAcrossAllDevices:identifiers:viewHint:complete:
sortedArrayUsingComparator:
setEpsk:
initWithContainerName:contextID:altDSID:flowID:deviceSessionID:
_identifier
copyWithZone:
experimentIsAllowedForProcess
setVersion:
softFailureCountForEventType:
status:xpcFd:reply:
writeToFile:atomically:
excludedVersion
TB,N,V_canSendMetrics
formattedText
initWithDictionary:andInternalFlag:
scrubBottledPeer:bottleID:reply:
unsignedIntegerValue
T@\"NSString\",&,V_location
authorizations
cachedCliqueStatus:error:
defaultProtectedAnalyticsDatabasePath:
initWithSFARule:logger:
setDateFormatter:
identityWithError:
initWithIdentifier:accessGroup:zoneID:
safeErrorClasses
T@\"NSString\",&,V_accessGroup
T@\"NSData\",&,V_persistentRef
_pake_scheme
_permitLocalIssuer
decompressedDataUsingAlgorithm:error:
interfaceWithProtocol:
setLocalSecureElementIdentity:secureElementIdentity:reply:
trust
Tq,R,N,V_code
initWithType:
logHardFailureForEventNamed:withAttributes:timestampBucket:
processName
stringWithString:
versionsType
setCertificate:
registration_record
T@\"NSData\",R,N,V_skid
hasPrefix:
match
resetAllRequests:
setCurrentItemPointerModificationTime:
_db
_componentName
hasAbc
Tq,V_type
preflightRecoverOctagonUsingCustodianRecoveryKey:custodianRecoveryKey:reply:
ticket_creation_time
triggerAutoBugCaptureWithType:subType:
writeTo:
_componentID
drop
fetchRemoteChangesWithReply:
keyWindow
propertyListWithData:options:format:error:
removeFriendsInClique:error:
zone
T@\"NSString\",?,R,C
logEventNamed:class:attributes:
initWithKey:certificate:
mergeFrom:
rpcFetchAndProcessChanges:reply:
T@\"NSArray\",&,V_attestationCRChain
initWithConfiguration:
rollback
schemaVersion
writeToFile:options:error:
_forceEnabled
accountStatus:
deleteObject:error:
importInitialSyncCredentials:complete:
tokenObject
_name
_value
addEvent:
fetchPrerecord:error:
getLabel
key
T@\"NSDate\",&,V_lastMatch
hasPropertyName
_blob
addConnectionListener:
peerDeviceNamesByPeerID:
setCachedConfig:
overrideForJoinAfterRestore
sbd
_rootCertificates
count
fetchCliqueStatus:
setTearDownMetricsHook:
CKLowercaseHexStringWithoutSpaces
hardFailures
rpcGetCKDeviceIDWithReply:
setLaunchOperation:
T@\"NSData\",&,V_csr
_discretionaryNetwork
_epoch
_idMSTDLNotificationFlowID
compare:
formatSFACollection:error:
numberWithUnsignedLong:
setPreferredBottleIDs:
_attestation
TB,V_launched
_repeatAfterSeconds
skid
_probablyInClassD
oncePerReport
T@\"NSString\",&,V_certificateURL
Td,N,V_samplingInterval
_clientClass
_intermediateSKIDMap
_view
pollForStatus:until:
SQLite
refetchCKKSPolicy:reply:
rootCertificates
SOSTransportMessageGetCircleName
T@\"SECSFAVersionMatch\",&,N,V_allowedBuilds
_uuid
_fetchCliqueStatus:error:
_limitMultiplier
controlObject:error:
copy
setAction:
setIntermediateSKIDMap:
derEncodedSize
parseVersion:platform:
setEventRules:
_connection
configVersion
getAccountMetadata:reply:
jsonDictionary
number
secItemSetCurrentItemAcrossAllDevices:newCurrentItemHash:accessGroup:identifier:viewHint:oldCurrentItemReference:oldCurrentItemHash:complete:
secLookupIndirectUnlockKey:completion:
setAttestationChain:
isRecoveryKeySet:reply:
lookupDetachedCertificatesFileForExecutable:cmsData:error:
property
T@\"NSString\",R,N,V_groupID
TB,N,V_discretionaryNetwork
appleAccountSignedOut:reply:
encodeInteger:forKey:
infoDictionary
keyData
T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},V_attestationCRKey
setCDPEnabled:error:
setUserCredentialsWithLabel:password:dsid:error:
xpcFd
array
connectionListeners
ensureTokenObject:
excludeCount
setTtr:
TB,R,N,V_isCurrentUser
_deviceSampleRate
_sessionParameters
componentID
leaveClique:
T@\"NSData\",C,N,V_metadata
TQ,N,V_epoch
arrayWithCapacity:
attributes
fetchUserControllableViewsSyncingEnabled:
setNumberProperty:forKey:
limitMultiplier
TI,V_counter
attestKeyObject:nonce:error:
cleanDictionaryForXPC:
deleteSEView:reply:
digestAlgorithmWithSignatureAlgorithm:error:
fetchCliqueStatus:error:
setOverrideEscrowCache:
CKDataWithHexString:stringIsUppercase:
_roRate
waitAndReleaseFd_ForTestingOnly
server_identity
int64AtIndex:
dataWithLength:
setOptionNotInteractive:
accessGroup
attestationCRChain
hasDomain
removePropertyForKey:
setFinalizeOrderURL:
setPermitLocalIssuer:
_excludedVersion
bindValue:atIndex:
fetchReceivedInviteWithGroupID:completion:
mutableBytes
pake_scheme
setAuthenticationAppleID:
firstMatchArmed
allObjects
modifyTLKSharesForSEView:adding:deleting:reply:
psk_id
T@\"NSString\",&,V_publicKey
ownerParticipant
setEvents:
waitForOctagonUpgrade:
sanitizeSubject
T@\"NSString\",R,N,V_schema
_nextMessageURL
checkInheritanceKey:inheritanceKeyUUID:reply:
initWithSession:eventName:
restore:dsid:secret:escrowRecordID:reply:
select:from:where:bindings:orderBy:limit:forEachRow:
sentTime
T@\"NSString\",R,C,N,V_groupID
dataWithBytes:length:
setInterface:forSelector:argumentIndex:ofReply:
setWithCapacity:
T@\"NSData\",&,V_psk
set
initWithHashAgilityValues:
protectedAttributes
raise:format:
_daemonConnection
bindDouble:atIndex:
keyParams
lastMatch
parseFromJSONDict:error:
accountUserKeyAvailable
initTargetingSession:
integerFact:
readHandle
setMatchingRules:
_escrowFetchSource
TQ,N,V_version
_productName
allowedVersionsWithSelf:
enumerateEventsWithLimit:usingBlock:
isEqualToString:
logSuccessForEventNamed:
setUserControllableViewsSyncStatus:enabled:reply:
Tq,N,V_integer
_samplingDisabled
encodedDataFromError:
initWithDaemonConnection:
initWithName:interval:block:clientClass:
initWithPublicKey:privateKey:
logRockwellFailureForEventNamed:withAttributes:
setBlob:
incrementIntegerPropertyForKey:
_counter
_metadata
clearOneofValuesForAction
fetchEgoPeerID:reply:
leaveClique:reply:
setLocation:
setOctagonUserControllableViewsSyncEnabled:error:
attestationOids
appNameFromPath:
dataWithBytesNoCopy:length:freeWhenDone:
uniqueDeviceID
_domain
trigger
predicateMatchingAllGroups
setTicket_lifetime:
signatureAlgorithm
rpcPushOutgoingChanges:reply:
T@\"NSMutableArray\",&,N,V_rootCertificates
abc
shouldRatelimit:rule:
testsEnabled
_client_identity
findOptimalBottleIDsWithContextData:error:
generateInheritanceKey:uuid:reply:
initWithUpdatedGroup:
launchBottledPeer:bottleID:reply:
user
addEventRules:
cachedCurrentUserIdentifier
challengeURL
client_password_verifier
connection
creationDate
errorFromEncodedData:
hasMajor
T@\"NSString\",&,N,V_alert
initWithClientIdentity:::
metricsHooks
removeObjectForKey:
T@\"NSError\",R,N,V_verificationError
T@\"NSString\",&,V_deviceSessionID
T@\"NSString\",C,N,V_authenticationAppleID
signers
characterIsMember:
getWatchdogParameters:
hasRadarnumber
pendingEscrowUpload:
acmeNewOrderURL
autoVacuumSetting
fetchAccountSettings:reply:
receiverPeerID
T@\"OTConfigurationContext\",R,N,V_ctx
_ctx
setIsGuitarfish:
T@\"NSData\",&,V_external_identity
launchOperation
T@\"NSString\",R,V_idMSTDLNotificationFlowID
SFSQLiteClassName
T@\"NSNumber\",&,V_serviceNumber
T@\"SECSFAEventRule\",&,V_rule
columnTypeAtIndex:
myPeerInfo:flowID:deviceSessionID:canSendMetrics:complete:
addSubscriber:
hasProcess
hwModelID
sendNewInvitesForGroup:completion:
setValue:
status:context:reply:
updateCollectionConfigurationWithData:
T@\"NSString\",R,N,V_SQL
createCertificate
invalidateEscrowCache:reply:
performOperation:mode:algorithm:parameters:reply:
unsignedIntValue
encodeBool:forKey:
objectEnumerator
predicate
setDeviceSampleRate:
eventDictForEventName:withAttributes:eventClass:timestampBucket:
numberWithInteger:
setupOnceTimer
disableWalrus:preRecords:reply:
_wasAuthenticationContextProvidedBySecCaller
callCallback:error:
logSystemMetricsForActivityNamed:withAction:
_certificate
setReset:
wipe:reply:
actions
setupPairingChannelAsInitiator:
T^{sqlite3=},N,V_db
_nonce
fetchCurrentUserIdentifierWithReply:
logMetric:withName:
sampleNow
T@\"NSString\",&,V_finalizeOrderURL
eventsByTime
setDsid:
setLeafSKIDMap:
_idMSTrustTimestamp
_isCurrentUser
dailyCoreAnalyticsMetrics:
dateByAddingTimeInterval:
safeCKErrorPrimitiveClasses
setAdditionalInformation:item2:output:
setObjectClassPrefix:
T@\"NSString\",R,C,N,V_handle
acmeNewAccountURL
decodeIntegerForKey:
rwCapacity
sharedInvitationNotifier
T@\"NSString\",&,V_processName
_backupStartTime
getResourceValue:forKey:error:
T@\"NSString\",&
T@\"NSData\",&,V_context
_cachedConfig
fetchSEViewKeyHierarchy:reply:
setUniqueClientID:
cleanseErrorForXPC:
OIDWithString:error:
_pdpState
fetchRequestStatuses:
setObject:forKey:
uppercaseString
parseFromData:error:
radarnumber
T@\"NSString\",&,N,V_processName
_radarDescription
hasTtr
secKeychainForceUpgradeIfNeeded:
T@\"NSString\",&,N,V_uniqueClientID
T@\"NSString\",R,C
enumerateObjectsUsingBlock:
initWithUUIDString:
objectForKeyedSubscript:
publicKey
resetAndEstablish:resetReason:idmsTargetContext:idmsCuttlefishPassword:notifyIdMS:accountSettings:isDBRv2:accountIsW:reply:
setAuthorizationURL:
payload
T@\"NSString\",C,N,V_deviceSessionID
_selfVersion
encodeStartItems:output:
iCloudIdentityStatus_internal:
isSubclassOfClass:
requestToJoinCircle:
_ticket_age_add
iCloudIdentityStatus:
reportKeychainBackupStartWithType:
_xpcConnection
daemonConnection
decodeBoolForKey:
initWithUUIDBytes:
setAttestationOids:
outcome
_samplingInterval
encodeCertificateEntry:der:der_end:
processPendingMessages
setEpoch:
shouldCountAPICalls
_schema
_octagonCapableRecordsExist
defaultProtectedAnalyticsDatabasePath:uuid:
removeRecoveryKey:reply:
rpcCKMetric:attributes:reply:
sortDescriptorWithKey:ascending:
subtype
isProxy
groupName:
initForReadingFromData:error:
octagonSigningPublicKey:
setEventClass:
size
StringAsConfigVersion:
gestalt
TB,R,N,GisNumber
schema
timeoutWaitForCKAccount
T@\"NSString\",&,N,V_pairingUUID
T@\"NSString\",&,V_contextID
T@\"NSString\",R,V_uuid
addCertificateChainsWithLeaves:parents:error:
setClientDisconnectionHandler:
stringByDeletingLastPathComponent
T@\"NSString\",R,V_flowID
_event
_serviceNumber
createObjectWithAttributes:error:
removeInheritanceKey:uuid:reply:
hasProcessName
hasSuffix:
removeObjectAtIndex:
setReadHandle:
T^{__SecIdentity=},V_identity
encodeMessageSecurityObject:
setFirstMatchArmed:
synchronousRemoteObjectProxyWithErrorHandler:
_lastMatch
bundleWithURL:
initWithAltDSID:
rule
valueForKey:
lastInsertRowID
bindName:withLength:
_pendingReports
_partialRecoveryBottleIDs
certificates
certs
nextObject
setEncoder:
T@\"NSString\",&,N,V_event
dictionaryWithCapacity:
numberWithFloat:
platformSupportsSOS
rpcPerformanceCounters:
secAssociateIndirectUnlockKey:handle:completion:
targetForKey:error:
SecItemAddAndNotifyOnSync:syncCallback:complete:
_allowedBuilds
databaseBasename
secKeyAlgorithm
appendFormat:
setUserCredentialsAndDSID:password:error:
T@\"NSString\",R,N,V_className
dataPropertyForKey:
initWithConnection:queue:type:
initWithExternalIdentity:::
initWithNewGroup:
lookupDetachedCertificatesFileForExecutable:skid:error:
setXpc_queue:
waitForInitialSync:
checkAvailabilityForHandles:completion:
setupPairingChannelAsAcceptor:error:
T@\"NSString\",C,N,V_passwordEquivalentToken
identifier
setHasExcludeEvent:
setSynchronousMode:
displayName
write:
evaluateRequirements:withFacts:
_timestamp
columnCount
config
removeMetricSamplerForName:
setUploadDate:
logSuccessForEventNamed:timestampBucket:
setAttributes:
propertyForKey:
stringFromDate:
_accessGroup
anonymousListener
hasEventType
qualityOfService
setCliqueMemberIdentifier:
setInteger:
_useCachedAccountStatus
major
matchingRules
setSessionParameters:
T@\"NSArray\",C,N,V_participants
setFirstLaunch:
_isGuitarfish
weakObjectsHashTable
T@\"NSMutableDictionary\",&,V_attributes
addVersions:
dependantLaunches
finalizeOrderURL
floatValue
ghostBust:complete:
T@\"NSHashTable\",&,N,V_connectionListeners
_altDSID
_samplers
deleteGroupWithRequest:completion:
setAuthorizations:
T@\"NSArray\",&,V_partialRecoveryBottleIDs
_tearDownMetricsHook
base64EncodedDataWithOptions:
clearEventFilters
data
T@\"NSString\",&,V_cachedCurrentUserIdentifier
T@\"NSString\",&,V_identifier
OIDString
acmeNewNonceURL
partialRecoveryBottleIDs
versions
Tq,V_timeout
_external_identity
_leafSKIDMap
createGroupWithRequest:completion:
hashAgilityValues
removeMetricsHook:
server_password_verifier
setProcess:
TI,V_deviceSampleRate
TQ,R
decodeObjectOfClasses:forKey:
reason
setKeyParams:
setUserControllableViewsSyncStatus:error:
setProcessName:
totalTrustedPeers:reply:
T@\"NSDictionary\",R,C,N
T@\"NSString\",R,V_parentKeyUUID
_orderURL
allTableNames
areRecoveryKeysDistrusted:reply:
location
```
