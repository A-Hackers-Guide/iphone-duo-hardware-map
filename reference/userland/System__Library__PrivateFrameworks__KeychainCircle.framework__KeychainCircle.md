# `/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`

iOS 27.2 dyld shared cache image. Version `62460.40.78.0.0`. **[DSC]**

## Linked libraries (12)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer`
- `/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore`
- `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`
- `/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/usr/lib/libcompression.dylib`
- `/System/Library/Frameworks/Security.framework/Security`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking`

## Objective-C: 26 classes, 8 protocols, 579 methods, 165 properties

### Class pages

Every class and protocol, with its methods: [`AAFAnalyticsEventSecurity`](../objc/AAFAnalyticsEventSecurity_KeychainCircle.md), [`KCAESGCMDuplexSession`](../objc/KCAESGCMDuplexSession_KeychainCircle.md), [`KCInitialMessageData`](../objc/KCInitialMessageData_KeychainCircle.md), [`KCJoiningAcceptAccountCircleDelegate`](../objc/KCJoiningAcceptAccountCircleDelegate_KeychainCircle.md), [`KCJoiningAcceptCircleDelegate`](../objc/KCJoiningAcceptCircleDelegate_KeychainCircle.protocol.md), [`KCJoiningAcceptSession`](../objc/KCJoiningAcceptSession_KeychainCircle.md), [`KCJoiningMessage`](../objc/KCJoiningMessage_KeychainCircle.md), [`KCJoiningRequestAccountCircleDelegate`](../objc/KCJoiningRequestAccountCircleDelegate_KeychainCircle.md), [`KCJoiningRequestCircleDelegate`](../objc/KCJoiningRequestCircleDelegate_KeychainCircle.protocol.md), [`KCJoiningRequestCircleSession`](../objc/KCJoiningRequestCircleSession_KeychainCircle.md), [`KCJoiningRequestSecretSession`](../objc/KCJoiningRequestSecretSession_KeychainCircle.md), [`KCPairingChannel`](../objc/KCPairingChannel_KeychainCircle.md), [`KCPairingChannelContext`](../objc/KCPairingChannelContext_KeychainCircle.md), [`KCSRPClientContext`](../objc/KCSRPClientContext_KeychainCircle.md), [`KCSRPContext`](../objc/KCSRPContext_KeychainCircle.md), [`KCSRPServerContext`](../objc/KCSRPServerContext_KeychainCircle.md), [`MetricSessionInfo`](../objc/MetricSessionInfo_KeychainCircle.md), [`NSCoding`](../objc/NSCoding_KeychainCircle.protocol.md), [`NSCopying`](../objc/NSCopying_KeychainCircle.protocol.md), [`NSObject`](../objc/NSObject_KeychainCircle.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_KeychainCircle.protocol.md), [`OTApplicantToSponsorRound2M1`](../objc/OTApplicantToSponsorRound2M1_KeychainCircle.md), [`OTPairingMessage`](../objc/OTPairingMessage_KeychainCircle.md), [`OTSponsorToApplicantRound1M2`](../objc/OTSponsorToApplicantRound1M2_KeychainCircle.md), [`OTSponsorToApplicantRound2M2`](../objc/OTSponsorToApplicantRound2M2_KeychainCircle.md), [`OTSupportOctagonMessage`](../objc/OTSupportOctagonMessage_KeychainCircle.md), [`OTSupportSOSMessage`](../objc/OTSupportSOSMessage_KeychainCircle.md), [`SOSControlProtocol`](../objc/SOSControlProtocol_KeychainCircle.protocol.md), [`SecurityAnalyticsReporterRTCActualAdapter`](../objc/SecurityAnalyticsReporterRTCActualAdapter_KeychainCircle.md), [`SecurityAnalyticsReporterRTCAdapter`](../objc/SecurityAnalyticsReporterRTCAdapter_KeychainCircle.protocol.md)

### Classes

`AAFAnalyticsEventSecurity`, `KCAESGCMDuplexSession`, `KCInitialMessageData`, `KCJoiningAcceptAccountCircleDelegate`, `KCJoiningAcceptSession`, `KCJoiningMessage`, `KCJoiningRequestAccountCircleDelegate`, `KCJoiningRequestCircleSession`, `KCJoiningRequestSecretSession`, `KCPairingChannel`, `KCPairingChannelContext`, `KCSRPClientContext`, `KCSRPContext`, `KCSRPServerContext`, `MetricSessionInfo`, `NSData`, `NSError`, `NSMutableData`, `NSString`, `OTApplicantToSponsorRound2M1`, `OTPairingMessage`, `OTSponsorToApplicantRound1M2`, `OTSponsorToApplicantRound2M2`, `OTSupportOctagonMessage`, `OTSupportSOSMessage`, `SecurityAnalyticsReporterRTCActualAdapter`

### Protocols

`KCJoiningAcceptCircleDelegate`, `KCJoiningRequestCircleDelegate`, `NSCoding`, `NSCopying`, `NSObject`, `NSSecureCoding`, `SOSControlProtocol`, `SecurityAnalyticsReporterRTCAdapter`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (class, TB,R) supportsSecureCoding;
@property (T@"AAFAnalyticsEvent",&,V_event) event;
@property (TB,V_canSendMetrics) canSendMetrics;
@property (TB,V_isAAAFoundationAvailable) isAAAFoundationAvailable;
@property (TB,V_isAuthKitAvailable) isAuthKitAvailable;
@property (TB,V_metricSent) metricSent;
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (TB,V_asSender) asSender;
@property (TQ,V_context) context;
@property (T@"NSData",&,V_secret) secret;
@property (T^{?=[16C]},V_send) send;
@property (T^{?=[16C]},V_receive) receive;
@property (T@"NSString",&,V_pairingUUID) pairingUUID;
@property (T@"NSString",&,V_altDSID) altDSID;
@property (T@"NSString",&,V_flowID) flowID;
@property (T@"NSString",&,V_deviceSessionID) deviceSessionID;
@property (TQ,V_piggybackingVersion) piggybackingVersion;
@property (TQ,V_epoch) epoch;
@property (TB,R,N) hasPrepareMessage;
@property (T@"NSData",&,N,V_prepareMessage) prepareMessage;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,V_dsid) dsid;
@property (T@"<KCJoiningAcceptSecretDelegate>",W,V_secretDelegate) secretDelegate;
@property (T@"<KCJoiningAcceptCircleDelegate>",W,V_circleDelegate) circleDelegate;
@property (T@"KCSRPServerContext",R,V_context) context;
@property (T@"KCAESGCMDuplexSession",R,V_session) session;
@property (Ti,R,V_state) state;
@property (T@"NSData",&,V_startMessage) startMessage;
@property (T@"NSString",&,V_piggy_uuid) piggy_uuid;
@property (Ti,V_piggy_version) piggy_version;
@property (T@"NSData",&,V_octagon) octagon;
@property (T@"OTJoiningConfiguration",&,N,V_joiningConfiguration) joiningConfiguration;
@property (T@"OTControlArguments",&,N,V_controlArguments) controlArguments;
@property (T@"OTControl",&,N,V_otControl) otControl;
@property (T@"NSMutableDictionary",&,N,V_defaults) defaults;
@property (T@"NSString",&,N,V_altDSID) altDSID;
@property (T@"NSString",&,N,V_flowID) flowID;
@property (T@"NSString",&,N,V_deviceSessionID) deviceSessionID;
@property (TQ,N,V_piggybacking_version_for_tests) piggybacking_version_for_tests;
@property (TB,N,V_failSOSForTests) failSOSForTests;
@property (Ti,R,V_type) type;
@property (T@"NSData",R,V_firstData) firstData;
@property (T@"NSData",R,V_secondData) secondData;
@property (T@"NSData",R,V_der) der;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSObject<KCJoiningRequestCircleDelegate>",R,V_circleDelegate) circleDelegate;
@property (T@"KCAESGCMDuplexSession",R,V_session) session;
@property (Ti,V_state) state;
@property (TQ,N,V_piggy_version) piggy_version;
@property (T@"NSString",&,N,V_altDSID) altDSID;
@property (T@"NSString",&,N,V_flowID) flowID;
@property (T@"NSString",&,N,V_deviceSessionID) deviceSessionID;
@property (T@"OTControl",&,N,V_otControl) otControl;
@property (T@"OTJoiningConfiguration",&,N,V_joiningConfiguration) joiningConfiguration;
@property (T@"OTControlArguments",&,N,V_controlArguments) controlArguments;
@property (TQ,N,V_piggybacking_version_for_tests) piggybacking_version_for_tests;
@property (TB,N,V_failSOSForTests) failSOSForTests;
@property (T@"<KCJoiningRequestSecretDelegate>",W,V_secretDelegate) secretDelegate;
@property (T@"KCSRPClientContext",R,V_context) context;
@property (TQ,R,V_dsid) dsid;
@property (Ti,R,V_state) state;
@property (T@"NSString",&,V_piggy_uuid) piggy_uuid;
@property (TQ,V_piggy_version) piggy_version;
@property (TQ,V_epoch) epoch;
@property (T@"NSData",&,V_challenge) challenge;
@property (T@"NSData",&,V_salt) salt;
@property (T@"NSString",&,V_sessionUUID) sessionUUID;
@property (T@"NSString",&,V_flowID) flowID;
@property (T@"NSString",&,V_deviceSessionID) deviceSessionID;
@property (T@"NSMutableDictionary",&,N,V_defaults) defaults;
@property (T@"KCAESGCMDuplexSession",R,V_session) session;
@property (T@"NSString",&,V_altDSID) altDSID;
@property (T@"KCPairingChannelContext",&,N,V_peerVersionContext) peerVersionContext;
@property (TB,V_initiator) initiator;
@property (TI,V_counter) counter;
@property (TB,V_acceptorWillSendInitialSyncCredentials) acceptorWillSendInitialSyncCredentials;
@property (TI,V_acceptorInitialSyncCredentialsFlags) acceptorInitialSyncCredentialsFlags;
@property (TB,V_acceptorWillSendPCSData) acceptorWillSendPCSData;
@property (TB,V_initiatorExpectPCSData) initiatorExpectPCSData;
@property (T@"NSString",&,N,V_dsidForTest) dsidForTest;
@property (T@"NSNumber",&,N,V_ackNumber) ackNumber;
@property (T@"NSArray",&,N,V_allPCSItemPersistentRefs) allPCSItemPersistentRefs;
@property (TQ,N,V_itemIndex) itemIndex;
@property (TB,N,V_grabbedLockAssertion) grabbedLockAssertion;
@property (T@"NSNumber",&,N,V_countOfReceivedItems) countOfReceivedItems;
@property (T@"NSNumber",&,N,V_countOfSentItems) countOfSentItems;
@property (T@"NSNumber",&,N,V_sizeOfPacket) sizeOfPacket;
@property (T@"NSXPCConnection",&,V_connection) connection;
@property (T@"OTControl",&,V_otControl) otControl;
@property (T@?,C,V_nextOctagonState) nextOctagonState;
@property (T@?,C,V_nextState) nextState;
@property (T@"OTJoiningConfiguration",&,N,V_joiningConfiguration) joiningConfiguration;
@property (T@"OTControlArguments",&,N,V_controlArguments) controlArguments;
@property (TB,N,V_testFailSOS) testFailSOS;
@property (TB,N,V_testFailOctagon) testFailOctagon;
@property (T@"NSString",C,N,V_altDSID) altDSID;
@property (TB,V_sessionSupportsSOS) sessionSupportsSOS;
@property (TB,V_sessionSupportsOctagon) sessionSupportsOctagon;
@property (TB,R,V_needInitialSync) needInitialSync;
@property (T@"NSString",C,N,V_model) model;
@property (T@"NSString",C,N,V_modelVersion) modelVersion;
@property (T@"NSString",C,N,V_modelClass) modelClass;
@property (T@"NSString",C,N,V_osVersion) osVersion;
@property (T@"NSString",C,N,V_uniqueDeviceID) uniqueDeviceID;
@property (T@"NSString",C,N,V_uniqueClientID) uniqueClientID;
@property (T@"NSString",C,N,V_altDSID) altDSID;
@property (T@"NSString",C,N,V_flowID) flowID;
@property (T@"NSString",C,N,V_deviceSessionID) deviceSessionID;
@property (T@"NSString",C,N,V_intent) intent;
@property (T@"NSString",C,N,V_capability) capability;
@property (TB,N,V_accountIsDBR) accountIsDBR;
@property (T^{ccsrp_ctx=^{ccdigest_info}^{ccdh_gp}^{ccrng_state}{?=b1b1b1b16}[1Q]},V_context) context;
@property (T^{ccrng_state=^?},V_rng) rng;
@property (T@"NSString",&,V_user) user;
@property (T@"NSData",&,V_verifier) verifier;
@property (T@"NSData",R,V_salt) salt;
@property (T@"NSString",R,V_altDSID) altDSID;
@property (T@"NSString",R,V_flowID) flowID;
@property (T@"NSString",R,V_deviceSessionID) deviceSessionID;
@property (TB,R,N) hasPeerID;
@property (T@"NSString",&,N,V_peerID) peerID;
@property (TB,R,N) hasPermanentInfo;
@property (T@"NSData",&,N,V_permanentInfo) permanentInfo;
@property (TB,R,N) hasPermanentInfoSig;
@property (T@"NSData",&,N,V_permanentInfoSig) permanentInfoSig;
@property (TB,R,N) hasStableInfo;
@property (T@"NSData",&,N,V_stableInfo) stableInfo;
@property (TB,R,N) hasStableInfoSig;
@property (T@"NSData",&,N,V_stableInfoSig) stableInfoSig;
@property (TB,R,N) hasEpoch;
@property (T@"OTSponsorToApplicantRound1M2",&,N,V_epoch) epoch;
@property (TB,R,N) hasPrepare;
@property (T@"OTApplicantToSponsorRound2M1",&,N,V_prepare) prepare;
@property (TB,R,N) hasVoucher;
@property (T@"OTSponsorToApplicantRound2M2",&,N,V_voucher) voucher;
@property (TB,R,N) hasSupportsOctagon;
@property (T@"OTSupportOctagonMessage",&,N,V_supportsOctagon) supportsOctagon;
@property (TB,R,N) hasSupportsSOS;
@property (T@"OTSupportSOSMessage",&,N,V_supportsSOS) supportsSOS;
@property (TB,N) hasVersion;
@property (TQ,N,V_version) version;
@property (TB,N) hasEpoch;
@property (TQ,N,V_epoch) epoch;
@property (TB,R,N) hasVoucher;
@property (T@"NSData",&,N,V_voucher) voucher;
@property (TB,R,N) hasVoucherSignature;
@property (T@"NSData",&,N,V_voucherSignature) voucherSignature;
@property (TB,N) hasSupported;
@property (Ti,N,V_supported) supported;
@property (TB,N) hasSupported;
@property (Ti,N,V_supported) supported;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Strings (801)

```
pairing: temp packet size is too large for the channel. will not add anymore items
joining: KCJoiningRequestCircleSession initialMessage called
successfully joined octagon
piggy version is 2
initiator complete second packet 2 with octagon
 OctagonSignpostNamePairingChannelInitiatorJoinSOS=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelInitiatorJoinSOS}d 
processResponse: errorData is nil, error: %@
TLKRequest done.
initiatorThirdPacket octagonData missing or wrong class
pairing: failed to check trust status: %@
failed to join circle with blob, continuing to handle octagon protocol
importing %lu items
BEGIN [%lld]: PairingChannelAcceptorMessage2  enableTelemetry=YES 
pairing: failed to fetch voucher %d times, bailing.
PairingChannelAcceptorMessage3
acceptor will send initiator (%lu) items: %@
joining: failed to encrypt initial message: %@
aafanalyticsevent-security: failed to weaklink AAAFoundation
PairingChannelInitiatorJoinSOS
joining: KCJoiningRequestSecretSession handleChallenge called
Failed to create response message: %@
joining: KCJoiningRequestSecretSession processMessage called
SOS not enabled, skipping peer info encryption
joined the SOS circle!
joining: %s
acceptor will send initial credentials
initiatorThirdPacket pairingMessage has no voucher
pairing: no octagon data, ending session
joining: processCircleJoinData failed %@, but continuing for Octagon
decoding piggybacking message failed for version (%llu)
first message is piggybacking v1, no more data
 OctagonSignpostNamePairingChannelAcceptorMessage2=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelAcceptorMessage2}d 
octagon: expected voucher! returning from piggybacking.
END [%lld] %fs: PairingChannelAcceptorCircleJoiningBlob  OctagonSignpostNamePairingChannelAcceptorCircleJoiningBlob=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelAcceptorCircleJoiningBlob}d 
acceptor pairing complete (will send: %{BOOL}d): %@
BEGIN [%lld]: PairingChannelInitiatorMessage2  enableTelemetry=YES 
PairingChannelInitiatorMessage3
initiatorThirdPacket successfully joined Octagon
BEGIN [%lld]: PairingChannelInitiatorMessage4  enableTelemetry=YES 
posting kSOSCCCircleOctagonKeysChangedNotification
will attempt to add more items to the packet
acceptor reply to packet 1
Attempt %d retrying join
error acceptor handling octagon packet %d
joining: unexpected piggybacking version, received: %llu
joining: KCJoiningRequestCircleSession initWithCircleDelegate called, uuid=%@
joining: failed to extract startMessage: %@
END [%lld] %fs: PairingChannelInitiatorJoinSOS  OctagonSignpostNamePairingChannelInitiatorJoinSOS=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelInitiatorJoinSOS}d 
acceptor didn't send a octagon packet, so skipping all octagon flows
initiatorCompleteSecondPacketOctagon returning octagon and sos data
failed to decode v2
BEGIN [%lld]: PairingChannelInitiatorMessage1  enableTelemetry=YES 
 OctagonSignpostNamePairingChannelInitiatorMessage1=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelInitiatorMessage1}d 
PairingChannelInitiatorMakeSOSPeer
pairing: Unable to acquire AKS lock assertion: %@
Attempt %d, calling join
acceptor reply to packet 2
joining: failed to create encrypted peer info, %@, but continuing for Octagon
PairingChannelInitiatorMessage2
initiator will import PCS data
pairing: device is not trusted, stopping the pairing flow
joining: decrypt and verify failed: %@
joining: decode from der failed: %@
processResponse: successfully created response message
piggy version is 0
unload bag failed: %d
%s: Attempt %d failed join: %@
error parsing version 1
BEGIN [%lld]: PairingChannelInitiatorMessage3  enableTelemetry=YES 
pairing: Failed to drop AKS lock assertion: %@
Did not receive expected ack number, re-attempting PCS key transfer
Failed to parse InitialMessageData from decrypted message data
initiator packet 1
END [%lld] %fs: PairingChannelInitiatorMessage4  OctagonSignpostNamePairingChannelInitiatorMessage4=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelInitiatorMessage4}d 
PairingChannelAcceptorFetchStashCredential
Attempt %d fetching epoch
Attempt %d retrying fetching epoch
Failed to decrypt message first data: %@. Trying legacy OTPairingMessage construction.
fetchAuthKitAccountWithAltDSID returned error: %@
END [%lld] %fs: PairingChannelInitiatorMakeSOSPeer  OctagonSignpostNamePairingChannelInitiatorMakeSOSPeer=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelInitiatorMakeSOSPeer}d 
TLK request failed to encrypt: %@
END [%lld] %fs: PairingChannelInitiatorMessage1  OctagonSignpostNamePairingChannelInitiatorMessage1=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelInitiatorMessage1}d 
failed getting application: %@
failed to join circle with blob
acceptor neither of octagon nor SOS
PB threw an error: %@
acceptor will send PCS data
acceptor validatedStashedAccountCredential: %{BOOL}d (%@)
Exchange packet: %u
doing SOS encryptedPeerInfo
eapfs IODT set to %{bool}d
BEGIN [%lld]: PairingChannelAcceptorMessage1  enableTelemetry=YES 
requester explicitly does not support SOS
metrics: failed to send metric event %@ before deallocation
Dropping lock assertion
PairingChannelInitiatorMessage1
adding keychain entry key: %@
acceptorFirstOctagonPacket octagon data missing
END [%lld] %fs: PairingChannelAcceptorMessage3  OctagonSignpostNamePairingChannelAcceptorMessage3=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelAcceptorMessage3}d 
doing SOS processSOSApplication
SeparateUserKeychain set via feature flag to %s
initWithSecretDelegate
joining: error producing octagon voucher: %@
adding keychain entry data: <agrp=%@,vwht=%@,labl=%@,cdat=%@,uuid=%@>
pairing, SecItemUpdate failed %d
 OctagonSignpostNamePairingChannelAcceptorFetchStashCredential=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelAcceptorFetchStashCredential}d 
joining: KCJoiningRequestSecretSession initialMessage called
failed to create version initial message: %@
joining: error preparing identity: %@
sanitizing request for keyclass %d to keyclass %d
eapfs boot-arg set to %{bool}d
 OctagonSignpostNamePairingChannelInitiatorMessage4=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelInitiatorMessage4}d 
%s Attempt %d failed fetching voucher: %@
fetchItemForPersistentRef: failed to fetch persistent ref: %@
pairing: fetched no results, ending session
Exchange packet complete data: %{BOOL}d: %@
joining: Verification failed: %@, error: %@
kicking off SOS Upgrade into Octagon!
Requesting lock assertion for %lld seconds
initiator packet 3
PairingChannelAcceptorMessage1
failed to deserialize
 OctagonSignpostNamePairingChannelInitiatorMakeSOSPeer=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelInitiatorMakeSOSPeer}d 
 OctagonSignpostNamePairingChannelInitiatorMessage3=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelInitiatorMessage3}d 
pairing: failed to fetch epoch %d times, bailing.
 OctagonSignpostNamePairingChannelAcceptorCircleJoiningBlob=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelAcceptorCircleJoiningBlob}d 
InitialMessageData does not contain prepare message
END [%lld] %fs: PairingChannelAcceptorFetchStashCredential  OctagonSignpostNamePairingChannelAcceptorFetchStashCredential=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelAcceptorFetchStashCredential}d 
%s: Attempt %d failed fetching epoch: %@
PairingChannelAcceptorCircleJoiningBlob
acceptorPCSDataPacket: received unexpected return type from SecItemCopyMatching, typeID: %lu
acceptor packet will include pcs data
joining: failed to handle challenge data: %@
processResponse: failed to create error response message: %@
joining: failed to process SOS application: %@, but continuing for Octagon
Attempt %d, retrying fetching prepare
acceptorSecondOctagonPacket octagon data missing
joining: initWithSecretDelegate called
acceptor handled octagon packet %d
received epoch message: %@
joining: KCJoiningRequestSecretSession handleVerification called
device supports SOS, continuing flow with piggyV1
Cannot determine because deviceMode is NULL
BEGIN [%lld]: PairingChannelAcceptorCircleJoiningBlob  enableTelemetry=YES 
initiator packet 4
unable to establish a channel to sos control
acceptor initialSyncCredentials requested
acceptor channel max capability set to %@
Attempt %d retrying fetching voucher
initiator will wait for PCS data
pairing: failed to upgrade initiator into Octagon: %@
 OctagonSignpostNamePairingChannelAcceptorMessage3=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelAcceptorMessage3}d 
pairing packet size %lu
failed to create version 1 message: %@
joining: KCJoiningRequestCircleSession handleCircleBlob called
END [%lld] %fs: PairingChannelInitiatorStashAccountCredential  OctagonSignpostNamePairingChannelInitiatorStashAccountCredential=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelInitiatorStashAccountCredential}d 
successfully updated pcs item: <agrp=%@,vwht=%@,labl=%@,cdat=%@,uuid=%@>
octagon: acceptor did not send its epoch. discontinuing octagon protocol. downgrading to verison 1
pairingchannel: one step too many
 OctagonSignpostNamePairingChannelAcceptorMessage1=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelAcceptorMessage1}d 
joining: expected acceptor epoch! returning nil. error: %@
piggy version is 3
pairing: failed to add PCS item: %d
joining: KCJoiningRequestSecretSession handleChallengeData called
joining: next secret is nil: %@
pairing: failed to serialize temp packet: %@
unsupported version
acceptor rpcEpochWithArguments: %ld (%@)
SOS not enabled for this platform
pairingchannel: failed pairing with: %@
successfully added pcs item: <agrp=%@,vwht=%@,labl=%@,cdat=%@,uuid=%@>
joining: failed to create encrypted peer info: %@
message does not contain SOS data
acceptor explicitly does not support SOS
octagon, failed to create pairing message from JoiningMessage: %@
PairingChannelInitiatorStashAccountCredential
END [%lld] %fs: PairingChannelInitiatorMessage2  OctagonSignpostNamePairingChannelInitiatorMessage2=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelInitiatorMessage2}d 
initiator importInitialSyncCredentials: %{BOOL}d: %@
END [%lld] %fs: PairingChannelAcceptorMessage2  OctagonSignpostNamePairingChannelAcceptorMessage2=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelAcceptorMessage2}d 
failed to send metric event %@ before deallocation
SecAKSDoWithKeybagLockAssertionSoftly: failed to get assertion for %d proceeding bravely: %@
error acceptor handling packet %d
acceptorFirstOctagonPacket 'v' contents wrong
could not stand up otcontrol connection
acceptor reply to packet 3
joining: expected vertification message type: %@
joining: failed to encrypt voucher payload: %@
joining: failed to join octagon: %@
initiator didn't send a octagon packet, so skipping all octagon flows
acceptor received ACK from initiator
joining: failed to create challenge message: %@
failed to decompress
successfully copied response message
processResponse: handle error: %d
octagon, message does not contain prepare message
aafanalyticsevent-security: failed to weaklink AuthKit
 OctagonSignpostNamePairingChannelInitiatorMessage2=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelInitiatorMessage2}d 
initiator circle join complete
octagon haveSelfEgo: status %d: %@ %@ %d: %@
ot-pairing: acceptorSecondOctagonPacket: no octagon message
 enableTelemetry=YES 
joining: KCJoiningRequestSecretSession copyResponseForChallenge called
joining: device does not support SOS, failing flow
joining: failed to copy srpMessage: %@
initiator circle join complete, more data: %{BOOL}d: %@
platform does not support SOS
joining: KCJoiningRequestCircleSession processMessage called
joining: octagon refusing octagon acceptor since we don't have a selfEgo
acceptor packet 2
ot-pairing: failed to create %d message: %@
joining: Failed to copy response message: %@
Failed to get initial sync view: %@
 OctagonSignpostNamePairingChannelInitiatorStashAccountCredential=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelInitiatorStashAccountCredential}d 
%s: Attempt %d, failed fetching prepare %@
BEGIN [%lld]: PairingChannelAcceptorMessage3  enableTelemetry=YES 
acceptor initialSyncCredentials complete: items %u: %@
fetchItemForPersistentRef: unexpected keychain item type fetched for persistent ref: %@, type: %lu
initiatorCompleteSecondPacketOctagon returning octagon data
PairingChannelInitiatorMessage4
END [%lld] %fs: PairingChannelAcceptorMessage1  OctagonSignpostNamePairingChannelAcceptorMessage1=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelAcceptorMessage1}d 
acceptorFirstPacket: expected NSDictionary type
Attempt %d fetching voucher
failed to fetch persistent ref %@, error: %@, continuing
octagon: error joining octagon: %@
joining: failed to process SOS circle: %@
BEGIN [%lld]: PairingChannelInitiatorStashAccountCredential  enableTelemetry=YES 
acceptor handled packet %d
joining: device does not support SOS nor piggybacking version 2
decryptAndVerify failed: %@, but continuing for Octagon
initiator no items to import
PairingChannelAcceptorMessage2
item by itself is too large for the pairing channel: <agrp=%@,vwht=%@,labl=%@,cdat=%@,uuid=%@>
failed stash credentials: %@
pairing: failed to fetch prepare %d times, bailing.
BEGIN [%lld]: PairingChannelAcceptorFetchStashCredential  enableTelemetry=YES 
acceptor packet 3
failed to create version 2 message: %@
error retrieving next message! :%@
platform not supported for pairing
initiator packet 2
acceptor packet 1
joining: failed to create encrypted peerInfo: %@
joining: initial message creation failed: %@
failed to decrypt voucher packet, fall back to legacy path, error: %@
doing SOS processCircleJoinData
piggy version is 1
BEGIN [%lld]: PairingChannelInitiatorMakeSOSPeer  enableTelemetry=YES 
BEGIN [%lld]: PairingChannelInitiatorJoinSOS  enableTelemetry=YES 
Sending ack %@
Received ack number: %@
joining: initWithSecretDelegate called, uuid=%@
joining: failed to decrypt and verify circle blob message failed %@
acceptor doesn't have a stashed credential: %@
initiator complete second packet 2
pairing: failed to join %d times, bailing.
no octagon version set
initiatorCompleteSecondPacketOctagon octagonData missing or wrong class
END [%lld] %fs: PairingChannelInitiatorMessage3  OctagonSignpostNamePairingChannelInitiatorMessage3=%{public,signpost.telemetry:number1,name=OctagonSignpostNamePairingChannelInitiatorMessage3}d 
pairing: failed to compress packet. will not add anymore items, error: %@
joining: failed to prepare identity: %@
processMessages: %@
Attempt %d, calling fetchPrepare
successfully handled challenge data
softlink:o:path:/System/Library/PrivateFrameworks/CloudServices.framework/CloudServices
softlink:o:path:/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
e
pcsdata
com.apple.security.tdlMembershipMultipleRecords
unexpected keychain item type fetched for persistent ref
failed to fetch dsid
RNG fetch failed
Version mising
itemsToModify
recordCount
accountIsG
null
com.apple.security.tdlStableIDDivergenceDisallow
fullRefetchNeeded
avgCKRecords
permanentInfoSig
No session key available
com.apple.security.ckks.CKAccountLogin
peersEvaluatedForMissingTLKShares
SecItemAdd: failed to add PCS item to the keychain
Encountered unexpected packet format while proximity pairing
Expected prepare message!
Got verification but  acceptor doesn't have matching secret: %@
com.apple.security.acceptorCreatesPacket2
com.apple.security.piggybackingCircleInitiatorInitialMessage
com.apple.security.vouchWithReroll
com.apple.security.fetchAccountWideSettingsTPH
com.apple.security.escrowRepairOperation
successfulItemsProcessed
disallowedRecordCount
fetchBecauseNetwork
supported
com.apple.security.validatedStashedAccountCredential
com.apple.security.deletedMIDHashMismatch
totalRetryDuration
com.apple.security.ckks.healTLKShares.uploadMissingTLKShares
Delegate returned error without filling in error: %@
.GlobalPreferences.plist
com.apple.security.ckks.processIncomingQueue
{(
/Library/Managed Preferences/%@/%@
decode failed
Failed to decrypt and verify message
com.apple.security.acceptorPreVersion3Change
com.apple.security.ckks.processIncomingQueue.loadAndProcessIQEs
uniqueClientID
com.apple.security.pairingFailedToFetchItemForPersistentRef
numKeychainItems
requester-deviceid
Library/Keychains
%llu
com.apple.security.fetchRecoverableTLKShares
com.apple.security.ckks.processOutgoingQueue.uploadOQEstoCK
Date Formatting
com.apple.security.pairingFailedFetchPCSItems
String encoding failed
/
api_trace
b
modelVersion
v28@?0B8@\"NSDictionary\"12@\"NSError\"20
DEBUGSCOPE
Circle-Logging
TTROnUnexpectedPairingPacketFormat
zesty
supportsSOS
com.apple.security.acceptorCreatesPacket5
com.apple.security.midVanishedFromTDL
fetchBecauseKeyHierarchy
sepBasedEscrowRepairState
fetchBecauseSE-API
com.apple.mobile.keybagd.lock_status
e-apfs
voucherSignature
Expected challenge!
Extra data at end of message
com.apple.security.fetchStableTrustedDeviceID
octagonSignInResult
machineRecordAllowed
Failed to create circle blob response message
}
deviceSessionID
Error
%@%@:%@
IODeviceTree:/filesystems
ccgcm_finalize failed: %d
failed to encrypt peer info
com.apple.security.initiatorJoinsTrustSystems
errorItemsProcessed
Unexpected message while done
model
com.apple.security.prepareTDIDPresence
numberOfTrustedPeers
totalNumberOfTrustedCustodians
com.apple.ckks.pairing.packet-size.%s.%u
%d
com.apple.aaa.dnu
com.apple.security.tdlDuplicateMIDRecord
com.apple.security.recoverWithInfo
stableTrustedDeviceIDInclusionEnabled
start data
all
full
com.apple.security.resetTPH
com.apple.security.aafanalyticsevent.queue
v24@?0@\"NSData\"8@\"NSError\"16
com.apple.security.createSOSApplication
pendingClassAEntries
midRolled
com.apple.security.acceptorFetchesInitialSyncData
missingPassword
com.apple.security.escrowPasscodeEnableCacheFlow
com.apple.security.performCKServerUnreadableDataRemovalTPH
didSucceed
%@ %@
com.apple.security.prepareIdentityInTPH
com.apple.security.acceptorCreatesPacket4
fetchBecausePeriodic
<KCJoiningAcceptSession: %lld %@ %@ uuid: %@>
Warning
SecretDone
com.apple.security.kVSSyncAndWait
com.apple.security.preApprovedJoin
eventName
confirmation data
0x
com.apple.security.tdlTDIDDuplicates
com.apple.security.recoverSilentWithCDPContext
newTLKShares
Failed to copy srpMessage
com.apple.security.handleRecoveryResults
pairing
PCS-Escrow
Failed to allocate space for der
com.apple.security.fetchTDLInTPH
com.apple.security.oTResetOperation
Library/Preferences
uniqueDeviceID
com.apple.security.prepareVouchAndJoinTPH
com.apple.security.ckks.evaluateTLKShares
com.apple.security.fetchMachineID
Unknown data encoding
uuid
not_supported
private/var/protected/
2
com.apple.security.numberOfTrustedOctagonPeers
com.apple.security.primaryAccountAdded
com.apple.security.joinWithVoucherInTPH
c
initiator
%@
decrypt and verify failed
send->recv
com.apple.security.octagonTrustLost
fetchBecauseFetchFailed
kSecCoreCryptoDomain
fetchBecauseAPI
SecLogging
com.apple.security
SeparateUserKeychain
a
com.apple.securityd.sos
%@-%d
decode from der failed
com.apple.security.pairingFailedToUpdateItemInKeychain
userdriven
numberOfPCSItemsFetched
com.apple.security.ckks.processReceivedKeys
com.apple.security.ckks.deviceLocked
totalNumberOfTrustedRecoveryKeys
%@ incorrect size, Expected %ld, got %ld
,
eapfs
failed to initial peerinfo message
com.apple.security.initiatorCreatesPacket3
com.apple.security.joinWithCircleReset
fetchBecauseInitialFetch
bag allocation failed: %d
SecCopyURLForFileInParameterizedKeychainDirectory: forceUserScope:%d
device cannot support pairing, not trusted in Octagon
com.apple.security.performSilentEscrowRecovery
]
supportsOctagon
com.apple.security.fetchAndPersistChanges
com.apple.security.duplicateMachineID
com.apple.security.tdlProcessingSuccess
stableIDDuplicateDeviceCount
ZuluCalendar
Size didn't match encoding
com.apple.security.establish
itemsToAdd
Bad payload size
ENTER
v16@?0@\"NSError\"8
com.apple.security.initiatorWaitsForUpgrade
com.apple.security.recoverWithCDPContext
fetchBecauseResync
totalNumberOfPeers
!
capability
failed to encrypt initial message
com.apple.security.verifySOSApplication
com.apple.security.resetCKKSZonesLackingTLKsOperation
fetchBecauseTesting
missingDigest
done
)}
avgRemoteKeys
totalNumberOfRecoveryKeys
{
osVersion
Extra space
expected acceptor epoch
Unexpected piggybacking version
com.apple.security.recoverRKTLKShares.recoveredRKTLKShares
pairingSuccessfulImportCount
Failed to process SOS Application
kSecurityRTCErrorDomain
com.apple.security.keychaincircle
permanentInfo
Kern return error
com.apple.security.piggybackingCircleInitiatorHandleCircleBlobMessage
com.apple.security.ckks.localSyncFinish
numLocalRecords
Voucher creation failed
\\
v8@?0
v56@?0@\"NSString\"8@\"NSData\"16@\"NSData\"24@\"NSData\"32@\"NSData\"40@\"NSError\"48
ccgcm_set_iv failed: %d
failed to create version 2 message
requester-id
com.apple.security.tdlSilentDrop
numberOfBluetoothMigrationItemsFetched
modificationsFetched
%c:%@ 
itemsScanned
Server start authentication failed: %d
Invalid size: %zu
failed to create version 1 message
<KCJoiningAcceptSession@%p %lld %@ %@>
com.apple.security.resetProtectedData
com.apple.security.ckks.firstManateeKeyFetch
zonesReverseSyncing
v16@?0r*8
x
Done, no messages expected.
lookupKeyType
totalNumberOfPreapprovals
%02X
Library/Caches
k
com.apple.security.piggybackingAcceptorProcessMessage
com.apple.security.ckks.launchStart
fetchReasons
Failed to decrypt and verify circleBlob
com.apple.security.preflightVouchWithBottle
SRP verification failed
o
(unknown: %i)
Expected verification!
com.apple.security.acceptorCreatesVoucher
newItemsScanned
accepting
acceptor-deviceid
Unable to piggyback with device due to lack of trust system support
SecItemUpdate: failed to update PCS item in the keychain
com.apple.security.cliqueMemberIdentifier
partialFailure
tlkSharesEvaluated
Start packet copy failed: %d
CALLER 
repair
com.apple.security.escrowRepairGenerateRecordPasscodeUnlocked
com.apple.security.anyPotentialRKSponsorsWithFlagSet
totalNumberOfDistrustedRecoveryKeys
octagon
com.apple.aaa
numberOfKeychainItemsCollected
Attempt to encrypt with no session
com.apple.security.ckks.syncingPolicySet
keychain
none
O
137694941
Extra in sequence
com.apple.security.fetchAccountWideSettings
avgSuccessfulItemsProcessed
secaks
fetchBecauseOctagonPairingComplete
v24@?0Q8@\"NSError\"16
v32@?0@\"NSData\"8@\"NSData\"16@\"NSError\"24
v16@?0^{__CFDateFormatter=}8
v28@?0B8@\"NSData\"12@\"NSError\"20
Expected CircleBlob!
com.apple.security.oTTriggerEscrowUpdateOperation
com.apple.security.supportsTLKOwnershipProofSetinStableInfo
prepareMessage
Error generating SRP salt/verifier
Failed to create tlk request response message
%@/%@
version
fetchBecauseKeyset
Failed to extract startMessage
failed to encrypt the voucher
mobile
deletionsFetched
-
v
com.apple.security.establishOperation
com.apple.security.ckks.contentSyncFinish
challenge data
intent
v44@?0q8@\"NSString\"16@\"NSNumber\"24B32@\"NSError\"36
Failed to parse InitialMessageData from decrypted message data
SecureBackupIsDBREnabled
ccgcm_update failed: %d
Decoding failed
Critical
debug
SecItemCopyMatching: failed to fetch pcs data from the keychain
v24@?0@\"NSDictionary\"8@?<v@?B@\"NSDictionary\"@\"NSError\">16
com.apple.ProtectedCloudStorage
com.apple.security.piggybackingAcceptorProcessApplication
numberOfTLKsFetched
com.apple.security.idMSSecurityLevel
isFullUpload
api
fullFetch
yyyy-MM-dd HH:mm
Debug
failed to handle challenge data
com.apple.security.resetSOS
Failed to create error response message
Emergency
Notice
1
com.apple.security.ckks.zoneChangeFetch
device does not support SOS nor piggybacking version 2
com.apple.security.oTLocalCKKSResetOperation
totalCKRecords
logging
n
recv->send
com.apple.security.ckks.tlkOwnershipProofsGenerated
numViews
fetchBecauseCurrentItemCheck
accountIsW
v24@?0r^v8r^v16
secret
v20@?0B8@\"NSError\"12
com.apple.security.ckks.processOutgoingQueue
isLocked
Failed to create response message
, 
limited
com.apple.security.trustedDeviceListFailure
com.apple.security.pairingEmptyAckPayload
failed to encrypt the SOS peer info
v24@?0@\"NSArray\"8@\"NSError\"16
extra data in string
com.apple.security.allowedMIDHashMismatch
com.apple.security.oTBecomeReadyOperation
SanitizeKeyclass
com.apple.security.pairingDidNotReceivePCSData
com.apple.security.vouchWithBottle
com.apple.security.recoverRKTLKShares.fetchRKTLKSharesForRecovery
trustStatus
totalNumberOfCustodians
disabled
Expected response!
%@%@
Unable to find class %s
Decode failure
Failed to process circle join data
com.apple.security.ckks.localReset
Expected prepare message inside InitialMessageData
security scope control
save bag failed: %d
epoch
com.apple.security.performEscrowRecovery
totalRemoteKeys
piggy
com.apple.security.ckks.trustGain
errorData is nil
Alert
missingKey
Failed to encode data
com.apple.security.piggybackingAcceptorInitialMessage
com.apple.security.fetchPolicyDocument
com.apple.security.TLKProofInvalid
%@: [%d] %s
com.apple.security.initiatorChannelSecured
asSender
com.apple.security.rpdDeleteAllRecords
com.apple.security.ckks.scanLocalItems
altDSID
com.apple.security.cloudKitAccountAvailability
edumode
acceptor
KeychainCircle
s
123456
i
com.apple.security.createSOSCircleBlob
isPrioritized
OctagonPiggybacking
com.apple.security.restoreKeychainAsyncWithPassword
com.apple.security.performCKServerUnreadableDataRemoval
numMismatchedItems
com.apple.security.escrowRepairGenerateRecordPasscodeChanged
Unknown string encoding
-apfs_shared_datavolume
y
failed to create initial message
syncingPolicy
avgErrorItemsProcessed
allowedRecordCount
com.apple.security.tdlMembershipCheckFailed
com.apple.security.pairingEmptyOctagonPayload
flowID
Failed to process circleBlob
com.apple.security.vouchWithBottleTPH
kern.bootargs
ACAccountStore
prepare
com.apple.security.ckks.zoneCreation
fetchBecauseKeyHierachyConflict
C%p F%p
com.apple.security.piggybackingSessionInitiatorHandleVerification
com.apple.security.ckks.healTLKShares.createMissingTLKShares
com.apple.security.tdlTDIDReapperance
policyFreshness
%@+%ld
failed to create response message
com.apple.security.pairingFailedToAddItemToKeychain
itemsToDelete
fetchBecauseAPNS
isDemoAccount
lockassertions
enabled
com.apple.security.piggybackingSessionInitiatorHandleChallenge
com.apple.security.ckks.healKeyHierarchy
com.apple.security.ckks.healKeyHierarchy.healBrokenRecords
Expected peerInfo!
message failed to process application
response data
com.apple.security.initiatorCreatesPacket1
com.apple.security.onqueueEstablishTPH
supportedTrustSystem
accountIsDBR
Logging
p
com.apple.security.updateTrust
peersMissingShares
Allocation failure!
unknown
Bad version: %llu
com.apple.security.ckks.scanLocalItems.onboardMissingItems
cannot join piggyback version %d with SOS disabled
v24@?0r*8Q16
com.apple.security.recoveryResultsResetAndEstablish
com.apple.security.clearCliqueFromAccount
com.apple.security.ckks.processOutgoingQueue.saveCKMirrorEntries
com.apple.security.ckks.deviceUnlocked
needsReencryption
SecError
com.apple.security.initiatorImportsInitialSyncData
com.apple.security.acceptorChannelSecured
isCurrentDevice
Failed to create pairing message from JoiningMessage
StableInfoSig
The source device expected an NSDictionary payload but received an unexpected packet format. Please include a sysdiagnose of both this device and the device signing in.
com.apple.security.updateTDL
numViewsWithNewEntries
Challenge processing failed: %d
SecAPITrace 
recordDataMissing
Failed to create challenge message
stableInfo
modelClass
v16@?0r^v8
ot-pairing
failed to create peerinfo response
com.apple.security.oTSetCDPBitOperation
voucher
Failed to copy start message
next secret is nil
Not sequence
com.apple.securityd
com.apple.security.ckks.healTLKShares
Info
com.apple.security.ckks.scanLocalItems.querySyncableItems
[
escrow-identity
com.apple.security.flush
com.apple.security.vouchWithRecoveryKeyOperation
com.apple.security.initiatorPreVersion3Change
com.apple.security.vouchWithRerollTPH
fetchBecauseMoreComing
peerID
SecItemCopyMatching: %d
com.apple.security.initiatorJoinSOS
com.apple.security.piggybackingSessionInitiatorInitialMessage
numberOfKeychainItemsAdded
com.apple.security.ckks.healKeyHierarchy.uploadHealedTLKShares
RETURN
com.apple.security.tdlTDIDStability
com.apple.security.escrowPasscodeCacheAvailable
Security
com.apple.security.cKKSTLKFetch
com.apple.security.restoreFromBottleEvent
com.apple.security.RKSponsorSelection
sepBasedEscrowRepairRateLimitDaysLeft
com.apple.security.pairingImportKeychainResults
retryAttemptCount
pairingFailedImportCount
com.apple.security.ckks.processIncomingQueue.fixMismatchedViewItems
d
%s
Unexpected tag size: %ld
Missing voucher from acceptor
ccgcm_reset failed: %d
totalViableEscrowRecords
extra data
failed to copy response
context
joining
Failed to encrypt encoded data
v24@?0Q8*16
com.apple.security.kcparingchannel
com.apple.security.joinWithVoucherOperation
com.apple.security.fetchAfterEstablish
securityLevel
com.apple.security.ckks.trustLoss
AKS Lock Assertion Queue
Bag CFData Allocation Failed
```
