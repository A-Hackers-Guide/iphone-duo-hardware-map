# `/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`

iOS 27.2 dyld shared cache image. Version `2774.0.0.0.0`. **[DSC]**

## Linked libraries (33)

- `/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter`
- `/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy`
- `/System/Library/PrivateFrameworks/Trial.framework/Trial`
- `/System/Library/Frameworks/DeviceCheck.framework/DeviceCheck`
- `/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`
- `/usr/lib/libTelephonyCapabilities.dylib`
- `/System/Library/Frameworks/WirelessInsights.framework/WirelessInsights`
- `/usr/lib/libprotobuf-lite.dylib`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics`
- `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`
- `/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension`
- `/usr/lib/libICEClient.dylib`
- `/usr/lib/libARI.dylib`
- `/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi`
- `/System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection`
- `/System/Library/Frameworks/CoreLocation.framework/CoreLocation`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/usr/lib/libMobileGestalt.dylib`
- `/usr/lib/libTelephonyUtilDynamic.dylib`
- `/System/Library/PrivateFrameworks/CallAudioServiceClient.framework/CallAudioServiceClient`
- `/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport`
- `/usr/lib/libQMIParserDynamic.dylib`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration`
- `/usr/lib/libxml2.2.dylib`
- `/System/Library/Frameworks/Security.framework/Security`
- `/System/Library/Frameworks/CFNetwork.framework/CFNetwork`
- `/usr/lib/libATCommandStudioDynamic.dylib`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libc++.1.dylib`
- `/System/Library/Frameworks/Network.framework/Network`

## Objective-C: 7 classes, 6 protocols, 128 methods, 29 properties

### Class pages

Every class and protocol, with its methods: [`AVCAudioSessionDelegate`](../objc/AVCAudioSessionDelegate_libIPTelephony.dylib.md), [`AVCRTTSessionDelegate`](../objc/AVCRTTSessionDelegate_libIPTelephony.dylib.md), [`CLEmergencyLocationSelectorDelegate`](../objc/CLEmergencyLocationSelectorDelegate_libIPTelephony.dylib.protocol.md), [`CLLocationManagerDelegate`](../objc/CLLocationManagerDelegate_libIPTelephony.dylib.protocol.md), [`CoreLocationDelegate`](../objc/CoreLocationDelegate_libIPTelephony.dylib.md), [`E911LocationSelector`](../objc/E911LocationSelector_libIPTelephony.dylib.md), [`ImsNetworkPath`](../objc/ImsNetworkPath_libIPTelephony.dylib.md), [`IptTrialExperimentsManager`](../objc/IptTrialExperimentsManager_libIPTelephony.dylib.md), [`NSObject`](../objc/NSObject_libIPTelephony.dylib.protocol.md), [`NSPTokenFetcherImpl`](../objc/NSPTokenFetcherImpl_libIPTelephony.dylib.md), [`NSPTokenFetcherProtocol`](../objc/NSPTokenFetcherProtocol_libIPTelephony.dylib.protocol.md), [`TAAudioStreamDelegate`](../objc/TAAudioStreamDelegate_libIPTelephony.dylib.protocol.md), [`TATextStreamDelegate`](../objc/TATextStreamDelegate_libIPTelephony.dylib.protocol.md)

### Classes

`AVCAudioSessionDelegate`, `AVCRTTSessionDelegate`, `CoreLocationDelegate`, `E911LocationSelector`, `ImsNetworkPath`, `IptTrialExperimentsManager`, `NSPTokenFetcherImpl`

### Protocols

`CLEmergencyLocationSelectorDelegate`, `CLLocationManagerDelegate`, `NSObject`, `NSPTokenFetcherProtocol`, `TAAudioStreamDelegate`, `TATextStreamDelegate`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB) systemClient;
@property (T@"NSString",&) auxiliaryAuthenticationCacheKey;
@property (T{weak_ptr<AVCAudioSession>=^{AVCAudioSession}^{__shared_weak_count}},N,Vowner) owner;
@property (T{shared_ptr<AVCRTPStackController>=^{AVCRTPStackController}^{__shared_weak_count}},N,VstackController) stackController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T{weak_ptr<AVCRTTSession>=^{AVCRTTSession}^{__shared_weak_count}},N,Vowner) owner;
@property (T{shared_ptr<AVCRTPStackController>=^{AVCRTPStackController}^{__shared_weak_count}},N,VstackController) stackController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T^{dispatch_queue_s=},V_cellularProdExpQueue) cellularProdExpQueue;
@property (TB) systemClient;
@property (T@"NSString",&) auxiliaryAuthenticationCacheKey;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Strings (8,706)

First 3,000 of 8,706.
```
#D %{private, mask.hash}s[SIM %u]: Got SSAC voice barring indication, Factor = %u, time = %u
#E Precondition has no tokens
 srvccHandoverCompleted stackId=%s
handleMediaSessionDeactivated sessionId=%llu error=%u
%{private, mask.hash}sGot %u refer event for %s
Dispatching handleRegistrationActive callback for %s: expiration=%u, regTrxId=%s
%{private, mask.hash}sreceived ACK, time to send pending BYE
Setting reason protocol for %s to %s
%{private, mask.hash}sNo held call to resume
#E Failed to send CallStateNotification: %u (%{public}s)
startRingbackTone [sessionId=%llu
%{private, mask.hash}ssendMsrp
#E Failed to resume sessionId=%llu error: %s
%{private, mask.hash}sdeferring deregistration request until current registration completes
%{private, mask.hash}sClearing throttling due to network interface change.
#E %{private, mask.hash}sUnknown session. Can't send Response from PrackHandler
#E %{private, mask.hash}sprocessDTMFDigitQueue session is null
No AVC stack controller!
%{private, mask.hash}sNetwork is %saware of our deregistration
#D %{private, mask.hash}sIMSCallInfo::handleTryingEvent for an unknown call
#D %{private, mask.hash}sDoing RING to call Id = %{public}s
%{private, mask.hash}sStarting INVITE with Replace for pull call id : %{private, mask.hash}s
%{private, mask.hash}sdeferring new deregistration request until current deinit/deregistration completes
%{private, mask.hash}sRandom delay %ums before sending register
%{private, mask.hash}sAccess network changed. Is LTE?: %{BOOL}d
#D %{private, mask.hash}sreceived UacBarringInd for instance %u: services %{public}s barred
%{private, mask.hash}sUsing Retry-After from proxy rather than preferred time of %{time_t}ld (%lds)
#W %{private, mask.hash}sInvalid OIR request
%{private, mask.hash}s=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
IMSSMSManager::handleLazuliSpamReportResponse - statusCode: %u
#E %{private, mask.hash}shandleInviteOrUpdateRequest couldn't find the attached call
%{private, mask.hash}sshutdown for %s with resetOnDelete: %{bool}d
initialize [stackId=%s]
%{private, mask.hash}sQueuing message request %s on stack %s
#E Can't find 'Signaling' section in default prefs
Created media session successfully, session id : %u
%{private, mask.hash}sRemote answers the same SDP as its last one
#W Cannot fetch transport name/ip - getnameinfo() failed
Non-session %s:
%{private, mask.hash}sFound spam risk %{public}s (identified as '%{public}s')
#D %s (%s) has rank %u
#D %{private, mask.hash}s[SIM %u]: skipBarringSms=%{bool}d
#E Invalid AudioCallEventResponse
#I %{private, mask.hash}sreceived INVITE w/ no SDP while in state: [offer=%{public}s(%{public}s) answer=%{public}s(%{public}s) txn=%{private, mask.hash}s]
#D %{private, mask.hash}s%s transferred to another device
#D Ignoring UPDATE request on instance %u for media %{public}s.  RAT type %{public}s has not changed!
#E %{private, mask.hash}sCouldn't listen on socket: %s
%s{
#D %{private, mask.hash}ssendPreconditionUpdate: waiting %ums for UPDATE from MO
handle timer timerId=%s
%{private, mask.hash}strying to match proxy %s
%{private, mask.hash}sWiFi network: Reset keepalive interval: %u --> %u, delta: %u --> %u
%{private, mask.hash}screating media session for %s stream on %p
#I %{private, mask.hash}smy contact in NOTIFY doesn't have an expires attribute. Not updating expiration timers.
Dispatching handleRegistrationStateChanged callback for %s
nw_parameters_require_interface interface=%s
creating path evaluator for %s
  Preconditions:
%{private, mask.hash}ssetting direction of outgoing SDP to %s
WB codec not present in SDP Media format
#I %{private, mask.hash}sfound matching sip.instance in NOTIFY body
#E %{private, mask.hash}sbase64 decode error pat key: %s size=%zu
#W No SDP session found sessionId=%llu
%{private, mask.hash}ssessionConfigureReq [sessionId=%llu]
#E %{private, mask.hash}sExplicit call transfer is disabled by carrier
dispatch handleParticipantRemoved for %s
#E %{private, mask.hash}sNo Lazuli delegate setup for stack %{public}s
#E %{private, mask.hash}sWe don't have a location to send in UPDATE
#E %{private, mask.hash}sreject called on confirmed or MT dialog
#E %{private, mask.hash}ssessionInitializeReq session is null
%{private, mask.hash}sno need to reregister. refreshing call access network information now
#D %{private, mask.hash}sDoing MERGE ALL
#E %{private, mask.hash}sUnable to store Chat %s
#E %{private, mask.hash}sNo controller associated with this command driver!
#E %s%s: %s
#D %{private, mask.hash}sAuth params provided
#W %{private, mask.hash}susing tag %s from our only from one of our forks for error response
flush [actionQueueSize=%zu]
processDataFromNw autostart
%{private, mask.hash}sreporting active port: %u
#E %{private, mask.hash}sunauthenticated digest request is null
%s]
#E Failed to start media session : %u
#D %{private, mask.hash}supdateNetworkServices: we are updating our registered services (RAT %{public}s)
#E Precondition has invalid number of tokens: %zu for status: %s
#E %{private, mask.hash}sno call to handle SDP offer
#E SDPMediaCandidate parse error, no ipAddress
#D %{private, mask.hash}sloading prefs for SIM-less emergency
  Remote URI:      %s
#E %{private, mask.hash}scan't add ACK retransmit handler for non-invite transaction %{public}s%{private, mask.hash}s
setScreeningMode [sessionId=%llu isScreeningCall=%u
%{private, mask.hash}sprocessing call event %s
%s[
#I %{private, mask.hash}sregistration subscription is disabled
%{private, mask.hash}sNot enough data in decodeStartLine
%{private, mask.hash}sno trailing data
#W %{private, mask.hash}sIgnoring null response.
%{private, mask.hash}ssessionMediaError [qmiSessionId=%u]
Stopping session [sessionId=%llu]
%{private, mask.hash}swaiting for call to finish holding
#I %{private, mask.hash}snew registration wasn't for voice
#E %{private, mask.hash}svalid() Invalid connection
%{private, mask.hash}sSipStackManager::createMessageSession
#W %{private, mask.hash}sAudio stream tokens callback for non-audio stream type %s
Checking if all sessions have completed handover [stackId=%s]
#D %{private, mask.hash}sNot waiting for UAC check %{public}s
%{private, mask.hash}shandleAck: received ack for session inside client transaction, ignoring
GBA_ME: P3 = %s
#E Error while connecting to %s:%u
#E %{private, mask.hash}sno session to handle SDP answer
%{private, mask.hash}slogRegistrationRequest
%{private, mask.hash}ssetting delegate interface to %s
#I %{private, mask.hash}swill attempt transport initialization in %u ms
#W RTP map attribute included for unexpected media format.
#E %{private, mask.hash}saddPreconditionsToOutgoingResponse called with invalid remote tag %{public}s
%{private, mask.hash}sreceived general errors from %u of %zu proxies
#D %{private, mask.hash}sLazuli attestation private key set: %{BOOL}d
#E %{private, mask.hash}sreceived an auth timeout with no pending request
#E %{private, mask.hash}sIncoming security mechanism (%s) has the wrong type
%{private, mask.hash}sTransition participant to Error state.
%{private, mask.hash}sSetting early media support level to: %{public}s was: %{public}s
%{private, mask.hash}sdelegate or SipStackManager is null: no decision to try to shortcuit the retry
%{private, mask.hash}swriteDataToStream : expected: %zu
%{private, mask.hash}sresetting registration mode due to event: %s
#D Dialog is no longer being used for anything. Terminating...
SIP Timeout reported to iRat Manager:
#D %{private, mask.hash}sNetwork error resulting in redial with %s
%{private, mask.hash}slocal QoS is already established. Don't need to start QoS timer.
%{private, mask.hash}snext session refresh due at %{time_t}ld (%lds)
%{private, mask.hash}stimer already started with reason %s
Flowstate is None. Clearing the state in CommandDrivers and calling handleMediaSessionTerminated() for upper layer sessions
Entering pseudo-emergency mode for SMS
#D %{private, mask.hash}susing compressed pdu %zu bytes
#D %{private, mask.hash}sinvalidating USSD session
#E %{private, mask.hash}sno lazuli session to handle SDP offer
handleMediaSessionDeactivated [sessionId=%llu error=%u isTransactionPending=%u actionQueueSize=%zu]
%{private, mask.hash}s%s matched private emergency prefix %s
#E unable to load IPSec library.  IPSec won't be working.
configureRemoteRTCP [sessionId=%llu enabled=%u interval=%u]
%{private, mask.hash}sexitEmergencyState: waiting for ECBM expiration at %{time_t}ld (%lds)
#W No RTPManager available for incoming RTCP
#E Non Digest/AKA authentication response is currently unsupported. Terminating session
#E sdpSession is null
#E Xcap client is not valid. Failing request
%{private, mask.hash}sdirection: %s
#E %{private, mask.hash}sIMSCallManager::answerCall: call %{public}s is already in a conference.
#E Via hop missing protocol version: %s
Unblock queued actions for non-active session [sessionId=%llu]
Handover completed sessionId=%llu error=%u
%{private, mask.hash}sremote side didn't ask for confirmation when our preconditions are satisfied
#E Failed to generated session config
#I %{private, mask.hash}ssubscription terminated by network.  Expected expiration was %{time_t}ld (%lds)
%{private, mask.hash}sWe offered preconditions, setting up status for new fork
#E %{private, mask.hash}sUnable to handle request for unknown stack ID %s
Failed to create CF reference for key: %s
%{private, mask.hash}sfalling over to TCP
#E %{private, mask.hash}sunable to set up temporary SA for client port: %s
%{private, mask.hash}sclearing nextRetryTime due to %s
#D %{private, mask.hash}sSending Call Status Changed notification: disconnection for callid: %{public}s, reason = %{public}s
%{private, mask.hash}sSipTcpConnection::connectionClosedByPeer
#D Ignoring duplicate END call status request (%u remaining) on instance %u for media %{public}s and RAT %{public}s
#W %{private, mask.hash}sAudio bearer revoked.  Ending call!
  Media Session:  %lld
%{private, mask.hash}sregistration event subscription terminated
#E Failed to extract StartDTMFCodeResponse : %d
add sessionId=%llu
#D %{private, mask.hash}sStarting emergency call to uri = %s
#E %{private, mask.hash}ssetConferenceCallActive: no existing conference call
#E %{private, mask.hash}stransaction error %s cseq %u
#E %{private, mask.hash}scancel called on a terminated session
%{private, mask.hash}sStream %llu direction set to %s (was %s)
%{private, mask.hash}sreceived response to our BYE. Time to terminate.
#E %{private, mask.hash}sinvalid SIP stack
%{private, mask.hash}sterminating session
#E %{private, mask.hash}sunable to send ping: %{public}s
%{private, mask.hash}sdesired proxy %s matched proxy #%lu
#W ImsTcpNw is null
Session inactive [sessionId=%llu]
#E Didn't send outgoing INVITE with Mls Blob because session already established. Try again later.
%{private, mask.hash}sfound verstat parameter '%{public}s' in %{public}s header
#E %{private, mask.hash}sunable to send BYE. Terminating immediately.
%{private, mask.hash}signoring deregister, deregister already pending or registration state will be dropped silently
#W %{private, mask.hash}sNo ruleset to fetch call barring info
%{private, mask.hash}sSkipping ULA %{public,network:sockaddr}.*P
%{private, mask.hash}sit's not time for QoS
GBA_ME: Key = %s
#E Missing RTP transport
%{private, mask.hash}sthis is a re-registration. Trying to use the same proxy.
%{private, mask.hash}sregistering for %s due to access barring change
%{private, mask.hash}shandleServiceUnavailable. Retrying OPTIONS again after %u seconds.
IMSSMSManager::reportLazuliSpam for %s
%{private, mask.hash}sKeepalive ping is past due at %{time_t}ld (%lds), triggering it now
#E Treat it as catastrophic error and end session.
%{private, mask.hash}sno registration info in notification
%{private, mask.hash}sSipTransportLayer::handleSystemWake()
Cancel all timers for sessionId=%llu
Session initialize request [sessionId=%llu rtpUuid=%s rtcpUuid=%s
  Default transport:
#D %{private, mask.hash}sContinuing deferred initialization for stack %{public}s
#D %{private, mask.hash}sSending Call Status Changed notification: emergency session required for callid: %{public}s
%{private, mask.hash}searly media is enforced. Activating session and starting local ringback tone.
%{private, mask.hash}svoiceSystemIdUpdated [instance=%u, voiceSystemId=%u]
%{private, mask.hash}sInitialize SipTcpTransport for stack %s useNw=%{bool}d forceTls=%{bool}d forceTls1.3=%{bool}d isLazuliEnabled=%{bool}d UseLibnetcoreForRcs=%{bool}d
%{private, mask.hash}sQMI AUDIO client successfully created
%{private, mask.hash}snetwork based call waiting is enabled. Incoming INVITEs must have a CW indication
#W %{private, mask.hash}sNo dial information cached for %{public}s
%{private, mask.hash}slogSessionRequestedEvent [appCallId=%u]
%{private, mask.hash}sscheduleRetry: retryIntervalOfBarring = %lu
%{private, mask.hash}sThumper is disabled.  Skipping dialog-event subscription.
%{private, mask.hash}sLazuli isThirdPartyApp changed: %{bool}d -> %{bool}d
#E %{private, mask.hash}sinitializeQMISession session is null
sendPortUpdate [sessionId=%llu port=%u]
#W %{private, mask.hash}sgot refer notification without a call object
Rule-Id: %s, Conditions:[%s, Media: %s], Active: %{bool}d, Allowed: %{BOOL}d
%{private, mask.hash}swill no longer drop msg arriving on DefaultSipPort of %s
%{private, mask.hash}sretry not allowed: roaming
#E %{private, mask.hash}sImsUdpSocket: Unable to bind socket (%d) to interface: %s
ACB Skip for voice is enabled, removing voice service flag from barring indication.
%{private, mask.hash}sNW listener failed
#E %{private, mask.hash}sanswerCall: unknown callId %{public}s
#I %{private, mask.hash}sno existing dialog with callId %{private, mask.hash}s
#D %{private, mask.hash}sProcessing 401 sequence=%u
%{private, mask.hash}sneed to add preconditions, but preconditions are disabled
%{private, mask.hash}sdelaying deferred action during reg hysteresis: %s
Replacing manager delegate for %s
Private Relay is active. Local client addresses in message body are fake.
#D %{private, mask.hash}shandleMedia%{public}sctivationEvent
%{private, mask.hash}sping!
#E %{private, mask.hash}sMore than one fork exists, rejecting QoS for ambiguous bearer
%{private, mask.hash}sdeferring deregister request during SRVCC cleanup
%{private, mask.hash}sSetting mediaManager to AP
#E %{private, mask.hash}sSIP stack init failed: %s
#D %{private, mask.hash}sIMSCallInfo: received %{public}s event for an unknown call
%{private, mask.hash}sTransfer complete
#E No more ports available
#E %{private, mask.hash}sinitializeCall: no valid SIP stack for %s
RTCP nw_path_evaluator initialized with uuid = %s clientID=%llu
#D %{private, mask.hash}sCreating PAT auth client. replacing=%{BOOL}d actualPR=%{BOOL}d intendedPR=%{BOOL}d
#E no transport layer
%{private, mask.hash}sadded PRACK handler for cseq %u
%{private, mask.hash}sLaunching emergency location selector
incoming %u response matched termination reason %s with event %s
pop [actionQueueSize=%zu
#W %{private, mask.hash}sCountry of origination is empty
%{private, mask.hash}sSkip ECBM for suspicious emergency call
%{private, mask.hash}s%s is already up
#E SipMultiPartBody: part decode failed
#I %{private, mask.hash}sSipRegistrationClient::initialize()
Stop request negates an earlier start request. Flushing the queue for sessionId=%llu
For the RTP socket, set delegate back to RTPManager
#D %{private, mask.hash}sConference call deactivated
#E %{private, mask.hash}sunable to send session refresh request
%{private, mask.hash}s  TransactionType : SIP INVITE (%u)
%{private, mask.hash}sTerminating Normal session %s
   temporary
%{private, mask.hash}sNormal IMPU ranking:
#E Didn't find valid RTCP transport for session %llu
#W %{private, mask.hash}sstack %s: will still accept %lu bytes from %{public,network:sockaddr}.*P, which is not from myProxies at [%s]
%{private, mask.hash}ssetTextMediaSessionMode: declining pending RTT upgrade for call %{private, mask.hash}s
#E %{private, mask.hash}sNo session to handle AckReceiveTimeout
%{private, mask.hash}scancel complete connection
%{private, mask.hash}sParticipant %s has not yet joined, so ignoring disconnected notification
#E %{private, mask.hash}sreceived unexpected auth challenge timeout.  Ignoring it, but checking queue.
%{private, mask.hash}sWaiting for network paths to become available
#D %{private, mask.hash}s[SIM %u]: (*response.mo_data_barring_t4).barring_status = %u
%{private, mask.hash}sSecondary device should not receive SMS.  Faking timeout.
#E %{private, mask.hash}smedia interface %{public}s not found
%{private, mask.hash}sSipStackManager::deinitializeStack: IncomingRegTrxId= %s, CurrentRegTrxId= %s
#D %{private, mask.hash}sTerminated conference call
      Fatal:      %u
CB Document: Rules: %zu
%{private, mask.hash}scausedByUAC. Will report.
#E Failed to open write stream
#E %{private, mask.hash}sSSLSetConnection failed. Error: %d
findPort address=%{public,network:sockaddr}.*P  port_start=%u
#W %{private, mask.hash}sImsTlsSocket: remote end closed connection
#D %{private, mask.hash}s[SIM %u]: requesting current SSAC info
#E SDP_ENCRYPTION_KEY_TAG NOT IMPLEMENTED: '%c=%s'
%{private, mask.hash}sfound proxy to use (addresses equal): %s
%{private, mask.hash}sconfigureRTPLinkMonitorReq [sessionId=%llu]
Dispatching handleNewRefreshRegistration callback for %s
%{private, mask.hash}sstopped LazuliRegRetryAttempt of retryInterval=%ld at %{time_t}ld (%lds)
#D %{private, mask.hash}sDeferring initialization for stack %{public}s
#E %{private, mask.hash}shangUp called while in NULL state
%{private, mask.hash}snotifying delegate of transport initialization with result %s
Received %lu response
%{private, mask.hash}slast action prerequisites not yet met
%{private, mask.hash}sinitializeDriverForInstance [instance=%u]
#I %{private, mask.hash}snasImsReg Start
#E %{private, mask.hash}ssendMessage: no active transport
    Expiration:          %{time_t}ld (%lds)
QMIRTPSession [sessionId=%llu]
#W SRVCC handover started while RTP handover is in progress. Aborting RTP handover for [stackId=%s]
Enabling RTP timeout for session %llu
%{private, mask.hash}slogSipRequest: using instance %u
%s%s (%s):
Rule-Id: %s, Target: %s
generating SecurityAgreementOptions
%{private, mask.hash}sFor emergency message, saving call-id %{public}s
#W %{private, mask.hash}sreceived an auth response without a pending challenge.  Discarding.
%{private, mask.hash}sUpdating CRLF-KeepAlive interval %u --> %u
#D %{private, mask.hash}s[SIM %u]: *response.skip_barring_mmtel_voice_t7 = %u
%{private, mask.hash}supdated with outgoing SDP [offer=%{public}s(%{public}s) answer=%{public}s(%{public}s) txn=%{private, mask.hash}s]
remove sessionId=%llu stack=%s
#E %{private, mask.hash}sRequest timer fired for configure request
%{private, mask.hash}swill try next proxy in list: %s
#E %{private, mask.hash}sUnknown timer fired
DTMF codec for NB not present in SDP Media format
#D %{private, mask.hash}ssending %s request over preferred transport %s
#W %{private, mask.hash}shandleStartMediaResponse called for non-existent session. ignore it.
#I %{private, mask.hash}sLocal QoS bearer revoked. Ending call!
Router Server: %p
%{private, mask.hash}shandleGeneralErrorFromOneProxy: getting from policy SipRegClientRegType::%s
Call Status reported to iRat Manager:
%{private, mask.hash}supdated stored auth response:
#E %{private, mask.hash}sSIP MESSAGE response %u : Triggering lazuli registration termination
#D %{private, mask.hash}sI hung up with %s
#D %{private, mask.hash}sIMSCallInfo::handleTextMediaDetectedEvent for an unknown call
#E %{private, mask.hash}s%{private, mask.hash}s: no sipstack
#D %{private, mask.hash}scontinue %sauthenticated registration registrationClientSequence=%u
#E %{private, mask.hash}scheckForActivate: no media session for call %{private, mask.hash}s
%s%s: {
audioStreamDidRecoverFromRTCPTimeOut owner is null
%{private, mask.hash}sInitializing old interface
%{private, mask.hash}sattaching SipSession %s
%{private, mask.hash}ssendOverSocket %zu bytes
#E Cannot create challenge from BSF client. Challenge Header: %s
registering timer %s
#S token %s semicolon %zu
#E %{private, mask.hash}sIMSCallInfo::startCall called for invalid stack
%{private, mask.hash}sstopAudio
%{private, mask.hash}sreporting default port: %u
#E %{private, mask.hash}sUnknown timer in ImsTransferWaitingForHoldState::handleTimer
#E %{private, mask.hash}sanswerRttUpgradeRequest: no call object
%{private, mask.hash}sremoved PRACK handler for cseq %u
********************************************************************************
#D %{private, mask.hash}ssending precondition update in fork %{private, mask.hash}s
%{private, mask.hash}s%s%d
%{private, mask.hash}sSet UUID %s
#D %{private, mask.hash}sunsubscribe already in progress
%{private, mask.hash}sskipping already resolved hostname %{public}s
%{private, mask.hash}sgroup isn't initialized
#D Sending status request START on instance %u for media %{public}s and RAT %{public}s
#D %{private, mask.hash}s[SIM %u]: ACB barring applies to voice
#E CreateStringByReplacingPercentEscapes failed for '%s'
%{private, mask.hash}sAUID: %s
#E Remote Accept-Types is empty
#E %{private, mask.hash}shandleInviteOrUpdateResponse: no fork with remote tag %{private, mask.hash}s
#D %{private, mask.hash}sno outstanding SDP. Sending %s immediately.
#E Unknown EVS rx bandwidth setting: %s
#D %{private, mask.hash}s%s Rejected
%{private, mask.hash}sno unheld calls
#E %{private, mask.hash}ssessionSetStreamDirectionReq session is null
%{private, mask.hash}sUninitialized all sessions for [apnType=%u]
#E %{private, mask.hash}sRegistration not allowed due to max consecutive terminations reached
created temporary SA with id = %u, spi = %u (%x)
%{private, mask.hash}sReceived MLS Opaque token from server for conversation %s
%{private, mask.hash}snot a fatal transport error: %s
%{private, mask.hash}suninitializeAllSessionsReq [stackId=%s  apnType=%d
%{private, mask.hash}sAVCRTPStackController created
processDataFromNw [sessionId=%llu len=%zu]
#E updateOutputFrequencyLevel no RTPManager found!
#W received unexpected data with %zu
%{private, mask.hash}scancelled connectionId=%llu
%{private, mask.hash}sReceived %zu bytes from %{public,network:sockaddr}.*P
#E %{private, mask.hash}sNo media session for call
%{private, mask.hash}shandleSendDTMFResp [sessionId=%llu]
#E %{private, mask.hash}sconnection error %{public,network:sockaddr}.*P: %s
We don't have remote AMR format params. Setting default
#E %{private, mask.hash}stransaction not found for key %s pendingTransactions %zu
#D %{private, mask.hash}sreportCallStatus Update with services %{public}s for instance %u on %{public}s, handoverFromWiFi %u, event id: %u...
%{private, mask.hash}sDropping message in Limited Access mode
%{private, mask.hash}sNumber of actions left to perform : %zu
#E %{private, mask.hash}sNo valid call
#E %{private, mask.hash}sNo decoder available, dropping %zu bytes
%{private, mask.hash}sstate transition [%{public}s --> %{public}s]
#E %{private, mask.hash}sINVITE transaction doesn't have an InviteType tag. Can't schedule a retry.
#D %{private, mask.hash}sSuccess SIP %{public}s headerCount=%{public}zu bodyLength=%{public}zu
%{private, mask.hash}s%s left conference %{private, mask.hash}s
#E Tried to set MaxPacketizationTime to %u  setting it to %u
%{private, mask.hash}sInitialize outgoing SipTcpConnection for stack %s useNw=%{bool}d interface=%s forceTls=%{bool}d forceTls1.3=%{bool}d isLazuliConnection=%{bool}d UseLibnetcoreForRcs=%{bool}d pcscfConnectionId=%{uuid}.16P
%{private, mask.hash}s%s : terminating media session %llu
CancelTimerForDelayedStackSwitch
%{private, mask.hash}sUpdating URI for dialog from remote
%{private, mask.hash}shandleEmptyInvite: Ignoring disabled media type %s
Airplane mode is %s
Unable to parse P-Last-Access-Network-Info header timestamp: %s
%{private, mask.hash}sservices revoked, deregistering
#D detaching Session
    Local cseq:     %u
#E %{private, mask.hash}sno security delegate
%{private, mask.hash}sInitial location available %lf, %lf
%{private, mask.hash}scall is already prepared
#S %{private, mask.hash}sSipTransactionLayer::determineIncomingMessageCategory
#E No valid SIP stack
#E %{private, mask.hash}sunable to set CNI to %s
%{private, mask.hash}sinitializing network policy session
#E %{private, mask.hash}sunknown transport type %s
#S %{private, mask.hash}sImsUdpSocket: handle incoming packet from %{public,network:sockaddr}.*P , len = %zu
%{private, mask.hash}signoring deferred registration action and telling delegate about our current registration
#E %{private, mask.hash}sinitializeTransport: no proxy available
#E Hey, don't call handleIncomingMessage with a NULL body!
%{private, mask.hash}s*********************************************
system will sleep
%{private, mask.hash}shandleUninitializeRequestReceipt [sessionId=%llu]
#E Failed to create RTCP nw_path_evaluator
%{private, mask.hash}sNetwork interface hasn't changed. Not clearing throttling.
#W Missing body in conference event
%{private, mask.hash}sinterface %{public}s is not up
Sending handover complete notification for stack type [stackId=%s stackType=%s]
%{private, mask.hash}sPreconditions NOT supported by network
%{private, mask.hash}sMSRP Message session terminated
#E %{private, mask.hash}ssetMediaSessionCreated, No SIP session
Dispatching handleRingbackToneEvent callback for %s
#W %{private, mask.hash}sNot in limited access mode to try LimitedAccess Registration
#W %s: '%c=%s'
%{private, mask.hash}sSSLHandshake succeeded
#E %{private, mask.hash}sAttestationPrivateKey is EMPTY!!
#E Failed to add encryption to the text session
#E %{private, mask.hash}sUnable to deserialize xcap data
#E Didn't find valid RTP transport for session %llu
media is already active
#D [SIM %u]: Response converted to SSAC info, Factor = %u, time = %u
start [sessionId=%llu]
#D %{private, mask.hash}sreceived termination notice for unknown subscription event '%s'
#D %{private, mask.hash}signoring duplicate response rseq=%u, cseq=%u
#D %{private, mask.hash}scouldn't get Min-Expires value from 423 response
IMSSMSManager::handleMessageSent(stackId: %s, messageId:%u)
%{private, mask.hash}slogIncomingPrack request failed: %{public}s
Dispatching handleMessageSendFailure callback for %s
#E NULL HTTP request!
#W isConfigEqualToActiveConfig [sessionId=%llu]  activeAvcSessionConfig is null
%{private, mask.hash}shandleConfigureRequestReceipt [sessionId=%llu]
callAudioServiceDidCrash
#E Cannot create session for conv %s trx %s
%{private, mask.hash}sstate transition [%s --> %s]
Canceling deferred action %s
#E %s (destination) : %{private, mask.hash}s
updated location available
#E %{private, mask.hash}sFailed to extract IBIImsMERtcpSDESReportInd: %d
#D %{private, mask.hash}skeeping winning fork %{private, mask.hash}s
#D %{private, mask.hash}s%{private, mask.hash}s: received %s request
#E %{private, mask.hash}sringCall: unknown callId %{public}s
#E %{private, mask.hash}scannot find dialog for pull call id : %{private, mask.hash}s
Sending StartMedia request
#W %{private, mask.hash}sdid not receive session refresh update in time. Terminating session.
#W %{private, mask.hash}svoice services requested on non-VoLTE RAT type: %{public}s
Stop requested on sessionId=%llu when state is %u
%{private, mask.hash}sprocess receive
#E %{private, mask.hash}sUnable to merge calls across SIP stacks.  Merge from %{public}s to %s requested.
%{private, mask.hash}sParticipant %s has already joined conference
%{private, mask.hash}sincoming connection %{public,network:sockaddr}.*P
#W %{private, mask.hash}sStandard Digest Challenge not supported yet
Session %s:
#D Defer NasClient init as BB is not available.
RTP port %u  already in use
%{private, mask.hash}supper layer requested transport %s
%{private, mask.hash}sactivateMediaSession (%s): RTP auto detection running
%{private, mask.hash}sSkipped updating sdp for media session (%llu)
%{private, mask.hash}sExisting dialog size: %zu
adding custom termination reason %s
#E Failed to set stream property on write stream: kCFStreamPropertyDataConnectionServiceType)
#E %{private, mask.hash}sunable to dial call: stack %{public}s uninitialized.
%{private, mask.hash}shandover total %u wifiToCellHandovers %u
configure [sessionId=%llu _reconfigureNeeded=%u _active=%u startInFlight=%u]
    Route set:      %s
%{private, mask.hash}sduplicate acknowledgement with %s
%{private, mask.hash}sUsing voice system Id %u from %s
#D Successfully reused TCP connection for China Telecom GBA
%{private, mask.hash}ssetting nextRetryTime to %{time_t}ld (%lds) due to %s
%{private, mask.hash}sthe other guy is responsible for session refresh
#W %{private, mask.hash}snot registered for SMS.  Rejecting incoming message.
#E %{private, mask.hash}scouldn't send precondition UPDATE in fork %s: %s
#W No remote connection found for session
#D %{private, mask.hash}sAnalyticsLogger::logSessionRequestedEvent MO=%{BOOL}d hashed call Id is %s
      Forbidden:  %u
#E No remote connection found for session
#E NEPolicyAdd failed
IPSecDBCallBack
#E %{private, mask.hash}sUnable to erase removed participant for %s
%{private, mask.hash}sretryRegistration: we are throttled until %{time_t}ld (%lds)
#D %{private, mask.hash}ssession already established %{public}s
#E %{private, mask.hash}sreason rtp error code %u
%{private, mask.hash}sactivating %s media session (%s)
%{private, mask.hash}slast held call held by user, not auto-resuming call.
#I Audit: %s : %p
%{private, mask.hash}sCouldn't initialize %{public}s
#E %{private, mask.hash}sunable to update pending SA: %s - will retry in %lds
%{private, mask.hash}shandleNotifyIpVersionResp Success
#E %{private, mask.hash}sCannot send Trying response - no encoding available
#E %{private, mask.hash}sUnable to create session for %{public}s
%{private, mask.hash}sdeleting with %zu users still attached
%{private, mask.hash}sneed to update preconditions, but we already have an outstanding offer
%{private, mask.hash}sShrink CRLF ping interval: %u --> %u
Multiple Calls: %{bool}d, Conference: %{bool}d
Host: %s:%u
%{private, mask.hash}schange group info trx %{public}s recipient %s conv %s len %zu
%{private, mask.hash}sActivating chat session to %{sensitive}s conv %s stack %s
#D %{private, mask.hash}ssetMediaManagerForStack to AP: %{BOOL}d appId: %d handoverBetweenCellularAndWifi: %{BOOL}d
#D %{private, mask.hash}sinitial SDP version is %llu
#W RTPManager::processDataFromSocket received unexpected data with %zu bytes from: %{public,network:sockaddr}.*P
%{private, mask.hash}ssystemClockDidChange: next retry time is still within our current retry interval: %{time_t}ld (%lds)
%{private, mask.hash}sstill waiting for emergency transport initialization
#D %{private, mask.hash}sDoing ANSWER to call Id = %{public}s
#D %{private, mask.hash}sretry is no longer enabled. Not resending INVITE or resetting Timer A
#E SDPMediaCandidate parse error, no foundation
#D  XCAP NAF GBA - Domain: %s, Extracted MCC: %s, MNC: %s, TCP connection reuse fix enabled: %{BOOL}d
#I %{private, mask.hash}srefresh cushion = %s
#E Invalid lazuli 1:1 SDP template
%{private, mask.hash}sremoving current activity %s
**********************
#E %{private, mask.hash}sno local SDP to send in PRACK response
#E Empty handover completed for stack %s which is not currently being handed over %s
#E SDPOrigin is missing something: '%c=%s'
#E %{private, mask.hash}sdelete policy failed for spi %u
Deleting socket for port %u
%{private, mask.hash}supdated secondsUntilNextRetry to %ld
%{private, mask.hash}sMessage send success conversationId %s ctTransactionId %s isEmpty %{BOOL}d allChunksAcked %{BOOL}d on stack %s
#W %{private, mask.hash}sfillContactForServicesAndMethod: no stack or transport layer available
%{private, mask.hash}sTrying to coalesce registration refresh for stack %s
%{private, mask.hash}sSipIPSecTransportGroup::initialize()
#E %{private, mask.hash}sno message encoding
#D %{private, mask.hash}signoring %u response on terminated fork %{private, mask.hash}s
%{private, mask.hash}swaiting for emergency SIP stack deinitialization to complete
%{private, mask.hash}sUsing MLS Opaque token provided by CT as server value is not available
#D %{private, mask.hash}s%s failed: we cannot support emergency calls in this location
%{private, mask.hash}s%s isn't held yet
%{private, mask.hash}sCreating Group Chat txn %{public}s subject '%{sensitive}s' xml %{sensitive}s isE2ee=%{BOOL}d
#E %{private, mask.hash}sImsTransferTransferCompleteState::enterState() - transfer handler is null
%{private, mask.hash}scheckForActivate: session %{private, mask.hash}s is terminating, so call can't be made %s
%{private, mask.hash}sattempting deregistration
%{private, mask.hash}ssendConfigureRequest [sessionId=%llu]
%{private, mask.hash}sisVoiceRegistrationBarred: zero barring factor for voice, service barred
#E %{private, mask.hash}ssendPreconditionUpdate: unable to create SDP to send
   deprecated
#W %{private, mask.hash}sreceived unexpected REGISTER response while in state %s
#D %{private, mask.hash}sClientStatusChange for stack %{public}s with status %{public}s
#E %{private, mask.hash}sIMS Xcap client is not initialized. Cannot send Xcap request
%{private, mask.hash}sfinished current activity
%{private, mask.hash}sReceived message [conversationId = %s on stack %s]
%{private, mask.hash}sAction %s finished with result %s
#E %{private, mask.hash}sServer detected group fork: %{private}s trx %{private}s encrypted=%{BOOL}d
#E %{private, mask.hash}ssendRequest: no remote tag specified, and we have multiple forks
#E %{private, mask.hash}sinitializeCall: not registered for voice calls
#D %{private, mask.hash}shandleMedia%sctivationEvent
    Pending SA:          
%s : text matched (%s)
%{private, mask.hash}ssetConnection, connectionId=%llu uuid=%{uuid}.16P
#E createInitialSettings Audio is null
CDIV Document: NoReplyTimer: %u, Rules: %zu
#W %{private, mask.hash}sdefault transport has been removed, resetting transports and reinitializing
Dispatching handlePreIncomingEvent callback for %s
HTTP request to be redirected: %s
#W %{private, mask.hash}sno existing forks. Making up new tag %{private, mask.hash}s for error response
%{private, mask.hash}sFailed to create CF reference for key: %s
%{private, mask.hash}scan't send pending INVITE now. I'll try later.
#I %{private, mask.hash}signoring subscriptionFailed for unknown subscription
#D %{private, mask.hash}sSet call active %{BOOL}d
#I %{private, mask.hash}s%{private, mask.hash}s: SipClientTransaction::handleError
Clear [actionQueueSize=%zu
#D %{private, mask.hash}shandleBurstDtmfSendComplete
#I %{private, mask.hash}sAnalyticsLogger::logLazuliServerTermination
#D Bootstraping NAS client...
%{private, mask.hash}sTransfer Failed
%{private, mask.hash}sRefer sent
%{private, mask.hash}sSkipping registration hysteresis timers for managed RCS connection
#D CallStateNotification request succeeded
%{private, mask.hash}sTracking Chat %s
%{private, mask.hash}sstarting ringing timer
%s[UNKNOWN] %s: %s
#E Via hop missing transport: %s
#D %{private, mask.hash}ssetting remote contact to %s
#D %{private, mask.hash}sNo a valid anonymous preferred identity
%{private, mask.hash}sDropping report; unknown MSRP Message-ID %s
#S %{private, mask.hash}ssendOverSocket %zu bytes
%{private, mask.hash}searly media is enforced. Activating session for network ringback tone.
#E SipMultiPartBody: no boundary specified in Content-Type header
%{private, mask.hash}scontinueSendRequest(): cancel AttestationServiceHelperSigningTimer, if it is still running
Dispatching handleMessageReceived callback for %s
%{private, mask.hash}s%zu participants remaining
#I %{private, mask.hash}sAnalyticsLogger::logRegistrationTerminated
#E %{private, mask.hash}sTODO: Handle re-invite
sendChallengeToDelegate isLazuliEnabled=%{bool}d keyRefLength=%zu
#D %{private, mask.hash}sreceived NOTIFY with state terminated for unknown subscription. Being nice and returning a 200 OK.
#D %{private, mask.hash}s%s not allowed as other secondary device is in use
%{private, mask.hash}sMessageSession MO-MSRP %{public,network:sockaddr}.*P --> %{public,network:sockaddr}.*P
%{private, mask.hash}sretry allowed: proxy list exhausted, but retries are allowed
#S %{private, mask.hash}s%s
#E %{private, mask.hash}sMode not handled in XCAP
#E %{private, mask.hash}senterState: NULL conference call
%{private, mask.hash}sUpdate location available %lf, %lf
  Service route: %s
#E SDPMediaCrypto parse error, unsupported key-param
Sending DTMF digit : %u
updated call delegate %s for stack %s to %p
%{private, mask.hash}sARI client already registered, skipping another register request.
#D %{private, mask.hash}sLazuli vendor: %d
#E %{private, mask.hash}sImsTransferWaitingForHoldState::checkForHeldParticipants() - transfer handler is null
#I %{private, mask.hash}sprocessing deferred %s
#I %{private, mask.hash}sskipping reg event subscription for emergency registration
#S Removing %p from list of sessions.
%{private, mask.hash}sFailed to set join. Conference participant is null
%{private, mask.hash}snew registration is SMS-only. Canceling pending hysteresis timer and any deferred registration.
%{private, mask.hash}sno existing registration policy
#W %{private, mask.hash}sincoming Message not destined for UE. Intended Recipient:%s
#D %{private, mask.hash}sfound existing fork %{private, mask.hash}s
#D %{private, mask.hash}srenewing subscription
Setting up NW Paths for %s  session [sessionId=%llu]
  audio direction:  %s
#E Failed to start DTMF digit send : %u
Deferring new deregistration
#E %{private, mask.hash}sunable to initialize IPSec SAs.  Failing registration.
%{private, mask.hash}sisRegistrationRetryAllowed(emergency) %{bool}d: RequestTimeout on all proxies. Default behavior
%{private, mask.hash}snew proxies: %s
#D %{private, mask.hash}sAdding text service feature tag to dialog
#S interface %s is satisifed?: %{bool}d
#D %{private, mask.hash}sCleaning up queues for conv %s
Auth status %d
#E %{private, mask.hash}sacceptInvitation: no call object
%{private, mask.hash}sfound existing proxy at same offset: %s
#E %{private, mask.hash}sLazuli invite failure: %{pubic}s
%{private, mask.hash}supdating SA pair for local client port <-> remote server port
#D %{private, mask.hash}sTracking MT-only lazuli session %{public}s
#E %{private, mask.hash}sReturning failure status.
%{private, mask.hash}snot terminating registration due to %s since automatic emergency redial is enabled
%{private, mask.hash}schanging registration mode from %s to %s, lastResponseCode=%u
#S Deleting HttpClient: %p
Session start is already queued. Drop this one sessionId=%llu
Skipping socket creation for media type %s
%{private, mask.hash}scheckForActivate: session %{private, mask.hash}s is terminated, so call can't be made %s
%{private, mask.hash}slogWiFiHandover handover total: %u, wifiToCellHandovers: %u, notify BB call ID: %{public}s, _currentAppCallId: %u
#E Auth response is not Digest
%{private, mask.hash}sSkipping transport init for managed RCS connection
#E Time information parsed out of order. Must appear after origin: '%c=%s'
operator: {
#E Unsupported encoding name given
Send event to Audio device
#D QMI client stopped for instance %u
Terminate session actionQueueSize=%zu
Persisting pseudo-emergency mode for SMS
#E %{private, mask.hash}sunable to initialize voice call due to access barring
#E %{private, mask.hash}sno fork with remote tag %{private, mask.hash}s
%{private, mask.hash}ssetting local SIP port to be ephemeral
%{private, mask.hash}sdeferredEndWithReason
#D timer %s fired (%s-%s)
#I %{private, mask.hash}sskipping to next proxy
#W %{private, mask.hash}sUnable to resolve sip stack for callid: %d
%{private, mask.hash}sending session due to %u response to %{public}s request
%{private, mask.hash}snot roaming: no decision to try to shortcuit the retry
%{private, mask.hash}scontinueSendRequest(): seqCnt=%u delayed=%{BOOL}d sendRequest...
%{private, mask.hash}signoring duplicate SDP offer with the same session version
#E %{private, mask.hash}sUnable to initiate transfer with trasferee %{private, mask.hash}s. Call is already a participant or is an emergency call
#D StartImsRegistrationUacCheck response: barringTime will be %u
%{private, mask.hash}sapp call id: %u
#E %{private, mask.hash}s%zu dialogs remaining after deinitialize.  Clearing.
%{private, mask.hash}snew OPTIONS transaction %s
#E %{private, mask.hash}sno SipStackManager delegate to handle exitEmergencyState
#D %{private, mask.hash}sLocal address: %s will be ignored. This will be a proxied connection
%{private, mask.hash}sIn the up-to-date (new) proxy list, current proxy is now #%zu (%s)
%{private, mask.hash}slogOutgoingRingingInfo request failed: %{public}s
#W Delegate is gone sessionId=%llu
%{private, mask.hash}sskipped initializing registration client becasue we have skipped deinitializing registration client before
%{private, mask.hash}sWPS Call requiring CSFB ended in cleanup state - defer sending event until timer expires
#D %{private, mask.hash}sReceived UAC barring info for stack %{public}s: UAC resp=%{public}s, affected services=%{public}s
Sending StopMedia request
#W %{private, mask.hash}sDrop ServiceBindResponse [instance=%u voiceSystemId=0]
IMSSMSManager::sendSMS(stackId: %s, messageId:%u)
#E %{private, mask.hash}saddParticipants: NULL conference call
%{private, mask.hash}sclearing auth info for initial registration
#D %{private, mask.hash}sAdd services to contact for Subscribe Method
#E %{private, mask.hash}sAudio settings DTMF RX payload type failed sanitization: %u
#E Failed to send StartImsRegistrationUacCheck request: %u (%{public}s)
%{private, mask.hash}sResetting decoder state
%{private, mask.hash}sscheduleRetry: set retryInterval = %lu
==================== [SID:%llu%{public}s] HTTP Request %{public}s -----> %{public}s [%{public}s:%u] ====================
Created client on stack %{public}s for conversationId %s
********************************** IMS Config **********************************
%{private, mask.hash}sUnable to add %s to conference.
%{private, mask.hash}sreceived CANCEL for unknown transaction %{private, mask.hash}s
#W %{private, mask.hash}sReceived request to update input frequency level for non-audio stream type %s
#E %{private, mask.hash}shandleParticipantStateChange: NULL conference call
#D %{private, mask.hash}snothing to do for kIMSCallStatusHoldFailed
%{private, mask.hash}sreportAPSession [localPort=%u remotePort=%u callActive=%u remoteAddress=%{public,network:sockaddr}.*P localAddress=%{public,network:sockaddr}.*P]
#I %{private, mask.hash}sStart Limited Access registration
#D SipDialog::transactionTerminated
#E %{private, mask.hash}s%s lazuli settings!
%{private, mask.hash}sthis is the emergency stack. Allowing P-Access-Network-Info in insecure %s
%{private, mask.hash}sSwallow disconnected event in kStateLeaving
#E %{private, mask.hash}sUnable to send call status request for invalid stack %{public}s
%{private, mask.hash}susing MSS %d
#E %{private, mask.hash}sSip stack not found %{public}s
#D %{private, mask.hash}sSipDialog::handleResponse
%{private, mask.hash}sDisable on network error: %{bool}d
#W %{private, mask.hash}sFork %{private, mask.hash}s does not contain remote SDP
#D %{private, mask.hash}sresending %s request with auth info
#W %{private, mask.hash}sInvalid CB request
AssertionCounter increased count - %s: %u
%{private, mask.hash}sno local qos timer
#W ImsTcpSocket: Remote end closed connection
#E _activeAvcSessionConfig is null
#E Failed to pause sessionId=%llu error: %s
%{private, mask.hash}sChanging early media direction from %s to %s
%s\"%s\"
%{private, mask.hash}sImsTlsSocket: No delegate to handle incoming packet from %{public,network:sockaddr}.*P. Discarding packet
#W XcapNafServerInfo::handleHttpResponseRedirect - Not implemented
sending to %{private, mask.hash}s trx %s conversation %s on %s type %s length %zu cpimHeaderLength %zu
Rule-Id: %s, , Allowed: %{BOOL}d
%{private, mask.hash}sContinue SSL/TLS handshake
#D %{private, mask.hash}sresending request
********************************** STATE DUMP **********************************
#E %{private, mask.hash}sPast due timer detected for %s
%{private, mask.hash}slogSessionRequestedEvent request failed: %{public}s
#E ImsTcpSocket: Error reading from socket: %d
#E %{private, mask.hash}sno auth challenge
#E %{private, mask.hash}sAudio session expired
%{private, mask.hash}sNo participant with Call-ID %s
#D %{private, mask.hash}swaiting indefinitely for UPDATE from MO
%{private, mask.hash}sactual wait timer fired. Time to bring down the PDN.
#E %{private, mask.hash}sSSLSetPeerDomainName failed. Error: %d
Init RTCP listener %{public,network:sockaddr}.*P
%zu: %{public}s
%{private, mask.hash}sneedToSendUpdate flag set to %{bool}d in fork %{private, mask.hash}s
#E GBA_ME failure. Invalid Ck/Ik
#E %{private, mask.hash}sDiscarding buffer.  Integer overflow detected adding %zu and %zu
%{private, mask.hash}sOur sim class is %u
#E Lazuli manager is null
#D %{private, mask.hash}susing Auth from stored config
#I %{private, mask.hash}sunable to initialize PRACK from response (missing RSeq or CSeq)
%{private, mask.hash}sAdding Lazuli tags in OPTIONS response: %s
%{private, mask.hash}sInitial state %s
#I %{private, mask.hash}sAnalyticsLogger::logSipResponse
#D Session associated with chat object is already terminated. %p
%{private, mask.hash}shandleAccessCongested (congestionDurationInSeconds=%ld) while in state %s ...
%{private, mask.hash}sexitEmergencyState: still registered. Waiting for registration expiration at %{time_t}ld (%lds)
%{private, mask.hash}sLocal override to always Subscribe.
#E %{private, mask.hash}ssessionDirectionChangeFailed session is null
#E %{private, mask.hash}smedia timeout after handover
#E %{private, mask.hash}sunable to set Virtual Interface MTU to %u: %s
Corrected ptime value is 20, non spec-compliant value was %u
Clear reconfigureNeeded
#E Invalid TLV type 0x%hx
Autostart complete for session [sessionId=%llu]
#D %{private, mask.hash}sAnalyticsLogger::logWiFiHandover - isValidHandover: %{BOOL}d
Switch stacks
%{private, mask.hash}sImsTlsSocket: no delegate to handle error, closing myself
%{private, mask.hash}sNot updating connectivity for emergency stack
No subscriptions
%{private, mask.hash}sstill waiting for these calls to go on hold or terminate:
#I %{private, mask.hash}sBearer revoked for media type %s
#D %{private, mask.hash}sEnd LazuliSession (isMTOnly: %{BOOL}d). Reason: %{public}s
%{private, mask.hash}shandleSessionInitializeIndication [sessionId=%llu qmiSessionId=%u
#E %{private, mask.hash}sIncoming range issue %u-%u/%u
#D %{private, mask.hash}strying to send 200 response
valid() Invalid mediaInfo
%{private, mask.hash}sthis activity is finished
%{private, mask.hash}slogRingingEvent request failed: %{public}s
%{private, mask.hash}send registration requested, terminate immediately
absolute timestamp is : %lf
#E %{private, mask.hash}sSequence %u doesn't match expected %u.  Dropping tokens
%{private, mask.hash}sexpiration set to 0.  Clearing registration timers.
%{private, mask.hash}stransport hasn't changed. Reinitializing emergency stack, but skip deinitializing active emergency registration and transport
#E Email parsed out of order. Must appear after origin: '%c=%s'
#E addPercentEscapes: couldn't create CFString
#D ~SipDialog() [Dialog:%s] %s
#D %{private, mask.hash}sremoving connection user from %s
%{private, mask.hash}sskipped deinitializing registration client
#E %{private, mask.hash}scontributionId not provided, using uuid %s
#S Creating NafServerInfo: %p
Dispatching handleProceedingEvent callback for %s
%{private, mask.hash}sGroup Chat Incoming %{public}s Subject '%{sensitive}s' Encrypted: %{BOOL}d
#D %s rows of precondition table are %s satisfied
#D %{private, mask.hash}sreplaced callId (%s) and localTag (%{private, mask.hash}s)
#E amrBandwidthASVAlue() relevantBWValues array only has %zu values, highest mode is: %u
#E %{private, mask.hash}sImsTransferWaitingForHoldState::checkForHeldParticipants() - state machine is null
No conference call to handle notification
AttestationServiceHelper starts with seqCnt=%u stressTest=%{bool}d qos=%d
%{private, mask.hash}supdating SA pair for local server port <-> remote client port
%s = %s
#E Failed to initialize BSF Transport
%{private, mask.hash}sclearing deferred drop registration
%{private, mask.hash}signoring duplicate SDP answer in txn %{private, mask.hash}s with the same session version
#D %{private, mask.hash}sMatched %s fork %{private, mask.hash}s with media type %s
#E AVC session doesn't have a capabilities dict
%{private, mask.hash}s %s = %s
#I %{private, mask.hash}sAnalyticsLogger::logRegistrationError
%{private, mask.hash}s%s is booted. Swallow refer error, go back to Joined state.
%{private, mask.hash}sreceived duplicate state change to %s (%s)
#D %{private, mask.hash}sreportCallStatus: No Op
%{private, mask.hash}sproxy list hasn't changed
%{private, mask.hash}sAll participants left, ending the conference call
#E Missing MessageEncodingMap. Cannot auto respond
#D %{private, mask.hash}sDoing ReadyToProceed to call Id = %{public}s
#I %{private, mask.hash}sAnalyticsLogger::logDeRegistration
#E %{private, mask.hash}sPRACK request missing RAck header
#I %{private, mask.hash}sre-subscribe on re-registration enabled
Dispatching handleThumperCallDeregister callback for %s
%{private, mask.hash}ssystemClockDidChange: next retry time is in the past: %{time_t}ld (%lds)
#D %{private, mask.hash}sSchedule unsolicited CB request [in %u seconds] to fetch all Rule Ids
Using higher RTP port for an emergency call to work around MAV20 baseband bug.
%{private, mask.hash}sno registration refresh performed while we're being throttled by RegistrationPolicy
%{private, mask.hash}shandleNonSipError(causedByUAC): scheduleRetry(preferredRetryInterval=%lu, useNextProxy=false)
%{private, mask.hash}ssendDTMFDigit DispatchInFlight DTMF digit queue size: %zu
ignoring override reason %s
%{private, mask.hash}sFailed to subscribe to conference event
#I %{private, mask.hash}snext hop preferred transport is TCP
#E %{private, mask.hash}shandleConfigureRequestReceipt session is null
Create new session
%{private, mask.hash}slogSessionTerminationEvent [appCallId=%u]
#S *************************
#D %{private, mask.hash}sSending reinvite for call Id = %{public}s
#E %{private, mask.hash}sTransient init requested on non-transient stack!
handleMediaSessionDeactivated sessionId=%llu result: %s
timestamp is : %lf
%{private, mask.hash}sUpdating MLS opaque token value from server response
#W Config not ready, deferring start [sessionId=%llu]
#D %{private, mask.hash}sForbiddenHttpErrorCode [*] matched
%{private, mask.hash}sclearing current auth info
#E %{private, mask.hash}ssendData() called on uninitialized SA
%{private, mask.hash}sFaking local QoS notification for MT Call
#I %{private, mask.hash}sinternalRetryRegistration: setting to policy SipRegClientRegType::RetryReg
%{private, mask.hash}signoring duplicate registration mode change to %s
%{private, mask.hash}sSaving termination reason : %s
#W %{private, mask.hash}sUnable to resolve sip stack for UUID %{public}s
%{private, mask.hash}sProxy already resolved for managed RCS connection
#E %{private, mask.hash}sNo signed opaque.  Triggering termination via disconnect in %s
%{private, mask.hash}spolicy session already initialized
%{private, mask.hash}sSkipping check timers transient %{bool}d state %s
#D %{private, mask.hash}srestarting expiration timer
%{private, mask.hash}sInvalidate stack %s
%{private, mask.hash}shandleStartMediaResponse [sessionId=%u result=%u]
#E %{private, mask.hash}sRegister request gone.  Moving on.  (dropping TokenRequest)
#W %{private, mask.hash}sNo stack for %{public}s
#E %{private, mask.hash}sUnable to set DSCP on NULL socket descriptor object
#E %{private, mask.hash}sBranded Calling header received : Invalid request
Number of sessions = %u
#W %{private, mask.hash}sI need IPSec, but Reg 200 OK arrived over default transport: ignored! Will retry Registration.
%{private, mask.hash}sNo Baseband for architecture or Baseband is currently not available: go straight to internalRetryRegistration
Register IMS-iRat Client
#E SipBodyPart::decode: create body failed
#E Unknown EVS bandwidth setting: %s
%{private, mask.hash}sKeepaliveRescheduled due to %s
#E %{private, mask.hash}sCan't set state for unknown participant
#E GetAcbInfo request failed: %u (%{public}s)
dispatch handleMessageSend for %s
%{private, mask.hash}sExiting emergency state now.
Node selector: %s
ACB voice skip enabled: %{BOOL}d
#W %{private, mask.hash}snot acting on appId %u while stack is still initializing
#E SDPSession doesn't contain audio settings
%{private, mask.hash}signoring retryRegistration request in state %s
%{private, mask.hash}sEnd transfer requested due to %s
%{private, mask.hash}scall confirmed, send session acknowledged
Session initialize request [sessionId=%llu]
#E Decoded nonce data is only %zu bytes for nonce: %s
#S Removing %p from list of session. Current Size: %zu
%{private, mask.hash}ssessionDidUninitialize [sessionId=%llu]
streamDidStop
#S %{private, mask.hash}sreadAppData exit
%{private, mask.hash}sendWithReason
#W %{private, mask.hash}sSupported header is not present, but we will ignore this carrier non-compliance issue.
%{private, mask.hash}sUsers in the NOTIFY = %zu
%{private, mask.hash}sSipTcpConnection::processDataFromSocket hasPartial=%{public,bool}d crlfInFlight=%{public,bool}d len=%{public}zu
#E %{private, mask.hash}shandling socket error: %s
#E %{private, mask.hash}s%s audio settings!
error(stackId: %s messageSequence: %u ctTransactionId: %s error: %s)
#D %{private, mask.hash}snothing to do for kIMSCallStatusResumeFailed
#W %{private, mask.hash}shandleTerminateMediaSessionResponse called for non-existent session. ignore it.
#D %{private, mask.hash}sPAT auth clear
Pausing inactive session
updated manager delegate %s for stack %s to %p
%{private, mask.hash}sSending registration signaling status STOP for instance %u
#D %{private, mask.hash}sRoaming: %{BOOL}d
#E Invalid StartMediaResponse
%{private, mask.hash}ssendMessage: NULLing out connection
%{private, mask.hash}semergency SIP stack initialization succeeded
%{private, mask.hash}sSending Thumper call %s for ID %s
#E %{private, mask.hash}sreset by peer %{public,network:sockaddr}.*P
#E %{private, mask.hash}sunable to initialize MO dialog
#D %{private, mask.hash}sreplaces header matches dialog:
#S ImsTcpSocket : readFromSocket : exit
%{private, mask.hash}shandleBarringAccessAlleviated: existing nextRetryTime=%{time_t}ld (%lds)
%{private, mask.hash}semergency sip stack media initialized
setRTPStackType [stackId=%s stackType=%d isDeinit=%u]
#E Unable to parse xml:
didPause
%{private, mask.hash}sreceived 180 ringing. Forcing remote preconditions satisfied in fork %{private, mask.hash}s
%{private, mask.hash}sRTT remote hold detected!!
#E skipping unrecognized IMPU type: %s
#E Failed to send digit
%{private, mask.hash}screating new connection for outgoing message: %s
%{private, mask.hash}screating policy with dictionary: %s
#E %{private, mask.hash}sstack is null. Unable to find resolvable proxy
#E %{private, mask.hash}sImsUdpSocket::initialize: unable to create CFSocket
#D %{private, mask.hash}sDeferring emergency initialization for stack %{public}s
%{private, mask.hash}scall %{private, mask.hash}s is already %s
%{private, mask.hash}sPR Fail-Open: %{bool}d
#E %{private, mask.hash}s_sock is empty...
#E Signing digest failed with error = %zu
#I %{private, mask.hash}sAnalyticsLogger::logCallStatusChange
%{private, mask.hash}snext keepalive event %{time_t}ld (%ds)
#E Auth client gone for athm spam tokenrequest
#E %{private, mask.hash}sPropagate failure for removeParticipant %s
#E %{private, mask.hash}sSIP INVITE response %u : Triggering lazuli registration termination
IBISession [sessionId=%llu]
#E %{private, mask.hash}sIMSCallManager: emergency call on emergency stack while no normal stack in use: failed due to no PCSCF provided
Open offer/answer and params match.
#E %{private, mask.hash}srecevied refer notification that isn't a response
#W %{private, mask.hash}sImsTcpSocket: kDebugDropIncoming set.  Dropping incoming packet.
#E Invalid host in Via hop: %s
#E %{private, mask.hash}ssessionDidUninitialize session is null
%{private, mask.hash}srequest mls info trx %s conf %s on %s, isEnhanced: %{bool}d, blob size: %zu
Dispatching handleSRVCCSilentHangupEvent callback for %s
%{private, mask.hash}sresetting proxy list for emergency call
#E Invalid TerminateMediaSessionResponse
#E value for termination reason %s has unknown type
#D %{private, mask.hash}soverriding %s=%s
stackError %d
%{private, mask.hash}sSipUssdSession::cancelSession: StateUninitialized: no op
%{private, mask.hash}sBaseband is currently not available: skip start
#D %{private, mask.hash}sCan not dial calls during existing alerting call
#E %{private, mask.hash}sRegistration moved on.  current sequence %u tokenReqeust sequence %u
#E %{private, mask.hash}saddPreconditionsToOutgoingResponse called with empty remote tag
%{private, mask.hash}sUsing instance %u for stack %s
    Remote contact: %s
#D %{private, mask.hash}sincrementing sdp version to %llu
Session initialize request [sessionId=%llu rtpUuid=%s rtcpUuid=%s]
#E %{private, mask.hash}sUnknown timer in ImsTransferTransferRequestedState::handleTimer
#E %{private, mask.hash}sConference participant is null. Can't handle ParticipantLeftConference
will update manager delegate %s for stack %s to %p
#E %{private, mask.hash}ssendDTMFDigit session is null
#D received UacAccessCheckResp for instance %u: services %{public}s allowed
Sending call status request before sending SMS message on %s
Replacing LazuliSession for conv %s
#E %{private, mask.hash}sUnable to create SDP session
Dispatching handleMediaStackSwitchComplete callback for %s
%{private, mask.hash}s%d: %{public,network:sockaddr}.*P
%{private, mask.hash}susing normal SIP stack for emergency call
#I %{private, mask.hash}sunable to initialize voice call while on an emergency call
%{private, mask.hash}sremoveSession [sessionId=%u]
#I %{private, mask.hash}s~SipTcpConnection
#I %{private, mask.hash}ssubscribeToRegEvents: already have an active subscription
#D %{private, mask.hash}supdateBarredServices: instance=%u, mask=%{public}s
Using PrivateToken scheme
%{private, mask.hash}sthere is currently no registration throttling. Ok to retry registration.
SIM Instance: %u
%{private, mask.hash}sregistration state changed from %s (%s) to %s (%s)
#E %{private, mask.hash}scancelPendingRegistration: no sipstack
#D %{private, mask.hash}sdelaying termination until NOTIFY handler completes
%{private, mask.hash}sForbidden Http Error Codes: %s
#E %{private, mask.hash}sinitializeUssdSession: SIP stack is not initialized
getValueFromMap no session for %llu
%{private, mask.hash}sprocessing pending emergency call
%{private, mask.hash}sinitialized virtual interface %s with address %{public,network:sockaddr}.*P
%{private, mask.hash}sremote is listening on path %s
%{private, mask.hash}swriteDataToStream : success: %zu
#E %{private, mask.hash}shandleSessionConfigureResp session is null
#E %{private, mask.hash}sNo transport layer. Unable to set ANI
%{private, mask.hash}sProcessing blob as one chunk with content size %u
%{private, mask.hash}ssetMediaInitialized called when we are in state: %{public}s
#W configure [sessionId=%llu]
%{private, mask.hash}sReceived conference notification with state Full
#D StartImsRegistrationUacCheck response: Timer 3346 remaining time = %u milliseconds
%{private, mask.hash}ssetQMISessionDirection [sessionId=%llu direction=%s]
#E AMR mode-change-period out of range: %s
%{private, mask.hash}sSuppressing error based on recommendation from policy.
#E %{private, mask.hash}sNo SipStack
#D %{private, mask.hash}sP-CSCF   : %{public}s
#E %{private, mask.hash}sno auth response
#E Request to NAF with auth credentials failed on existing connection (connection may have been closed by server)
%{private, mask.hash}sSaving pub-gruu: %s
%{private, mask.hash}sfound proxy to use (reachable): %s
#E %{private, mask.hash}sperformLocalHold: we're confirmed but don't have a media session. Killing call object.
#E Unable to resolve host force=%{bool}d type=%s
Replacing xcap delegate for %s
%{private, mask.hash}sreceived NOTIFY with event '%s'. Disabling IMS registration.
#E %{private, mask.hash}sinitializeCall: no call manager delegate specified
#D %{private, mask.hash}sisActive: conference call is confirmed or unheld
#W %{private, mask.hash}shandleCreateAudioMediaSessionResponse called for non-existent session. ignore it.
codec[codecsIndex] max_redundancy_duration : %u
configure [sessionId=%llu]
#D %{private, mask.hash}sRemoving subscription %s' from dialog
%{private, mask.hash}slocal QoS is already active
#E %{private, mask.hash}shandleSdpOffer: couldn't create answer for offer
Interface: %s, mtu: %u
#E %{private, mask.hash}sunexpected transaction for local answer: %{private, mask.hash}s
%{private, mask.hash}sNOTIFY has confirmed that %s has left conference
Using Digest scheme
#E %s: %s
#I %{private, mask.hash}s%{private, mask.hash}s: checking for P-CSCF Restoration info in 504 response
Create new session isAutoStart=%u oldSessionActive=%u isDelayedStart=%u
DTMF queue is empty, nothing to send
%{private, mask.hash}sWiFi to Cellular handover: will send SESSION_STARTED event to BB
%{private, mask.hash}sregistration refresh is due at %{time_t}ld (%lds), triggering it now
srvccHandoverStarted activeSessionId=%s
#D %{private, mask.hash}sConference call invalidated
#E SDP_MEDIA_ENCRYPTION_KEY_TAG NOT IMPLEMENTED
no CK provided but encryption algorithm is %s. Using dummy encryption key.
%{private, mask.hash}shysteresis timer fired with deferred action: %s
%{private, mask.hash}sRegistration drop has been deferred, dropping registration now.
%{private, mask.hash}sSipStackManager::deinitializeStack: CurrentRegTrxId= %s
%{private, mask.hash}s-------------------------------------------------------------------------
#D %{private, mask.hash}sConference event: %u
#E Can't find 'SipTimers' section in default prefs
Dispatching handleThumperCallRegister callback for %s
direction set to %s
#E %{private, mask.hash}sUnable to shutdown unknown SIP stack %s
#W %{private, mask.hash}stimed out waiting for prerequisites. Canceling.
#E %{private, mask.hash}ssendMessage: failing send for testing
%{private, mask.hash}squeueing %zu bytes
%{private, mask.hash}sskipping incoming connection id=%{uuid}.16P
Dispatching handleForceLTEFallback callback for %s
%{private, mask.hash}s%zu trailing bytes
#E %{private, mask.hash}sNo stack for %s
#D %{private, mask.hash}sanonymous preferred identity is %s
#D %{private, mask.hash}sIMPU IMSI: %s
#E %{private, mask.hash}sfailed to add authenticated PrivateToken header
%{private, mask.hash}sFound %{public,network:sockaddr}.*P for interface %{public,network:sockaddr}.*P
%{private, mask.hash}supdated dialog info: %s
#D %{private, mask.hash}sPicking IMPU from list of IMPUs received in the 200 (OK) response during last successful registration
#E %{private, mask.hash}scan't send an INVITE while there is a current INVITE transaction
#S Setting up XcapSession: %p
%{private, mask.hash}sregistration policy changed from %s to '%s'
#E Failed to extract TerminateMediaSessionResponse : %d
#E %{private, mask.hash}sreceived a fatal error from ImsClient
#E %{private, mask.hash}sno ImsClientDelegate to handle auth challenge
%{private, mask.hash}sperforming termination of registration due to %s
handleMediaSessionInitialized sessionId=%llu result: %s
%{private, mask.hash}ssendAudioCallEvent [event=%d]
#I %{private, mask.hash}s%{private, mask.hash}s: P-Asserted-Identity from Server Timeout response not found in service route or path
%{private, mask.hash}sold transport using port %u
#E %{private, mask.hash}sInvalid ATHM Spam TokenResponse in push. Unable to skip unauthorized REGISTER
%{private, mask.hash}sPort is available %u
#E %{private, mask.hash}sTTY settings redundant RX payload type failed sanitization: %u
#W spam reporting uri (%s) is invalid. Reporting chatbot spam to chatbot URI
#I %{private, mask.hash}srejecting incoming message from %{public,network:sockaddr}.*P.  Should be from %{public,network:sockaddr}.*P or TCP connection from %{public,network:sockaddr}.*P
%{private, mask.hash}sResponse does not contain valid SOS service Urn
Dispatching handleMergeSuccess callback for %s
%{private, mask.hash}sstill waiting for emergency stack initialization
%{private, mask.hash}squeueing prerequisite [%zu] %s
  Current INVITE:  %s%s
#E %{private, mask.hash}sUninitialized NetworkInterface: can't set next interface
adding SKIP policy at %d
#W %{private, mask.hash}sInvite response is 503 with Retry-After: %u for conv %s
#E %{private, mask.hash}sNo message encoding specified.
#E Failed to validate recipient for MT SMS- Invalid URI
#D %{private, mask.hash}sCall to %s requires CS fallback
#E %{private, mask.hash}stransport is gone
#W %{private, mask.hash}sregistration %s does not have an entry for my contact (%s)
%{private, mask.hash}sTearing down stack %s
#D %{private, mask.hash}signoring non-error response
#E %{private, mask.hash}scurrent state: [offer=%{public}s(%{public}s) answer=%{public}s(%{public}s) txn=%{private, mask.hash}s]
#D %{private, mask.hash}sno Record-Route headers.  Clearing route set.
New start request; session will be started when audio ready notification is received sessionId=%llu
  Confirmed:      %{time_t}ld (%lds)
#S %{private, mask.hash}srtcp SR packets Count %llu
#D Fatal exception occured while trying to submit metric %s with id %u
%{private, mask.hash}slogSessionTerminationEvent request failed: %{public}s
Dispatching handleMergeEnabled callback for %s
%{private, mask.hash}sregistration throttling ends at %{time_t}ld (%lds), retrying now
%{private, mask.hash}sreceived an incoming INVITE while we're waiting for a response to our INVITE
#E Setting Router Server called for a non-Dale device!
%{sensitive}s
#I %{private, mask.hash}swill attempt registration at %{time_t}ld (%lds)
#S Adding %p to list of sessions. Current Size: %zu
%{private, mask.hash}squeued message for send
%{private, mask.hash}sreceived a message over new SAs.  Removing old SAs %s
%{private, mask.hash}sEPS Fallback detected
%{private, mask.hash}s  Action          : Sent (2)
dispatch handleGroupChatUpdate for %s
%{private, mask.hash}sUsing pager for Revoke message
#D %{private, mask.hash}s%{private, mask.hash}s: adding To: tag to %s
%{private, mask.hash}sInitialized TCP connection %{public,network:sockaddr}.*P -> %{public,network:sockaddr}.*P
%{private, mask.hash}sdropping registration error notification while CSFB mode is enabled
#I %{private, mask.hash}sterminating old reg subscription and starting a new one
Initializing active stack type for %s to %s
#E %{private, mask.hash}sIMSCallManager: unable to determine destination URI
#E %{private, mask.hash}scannot cancel from NULL state
%{private, mask.hash}sSkipping an update for IPSec transport expiration for managed RCS connection
%{private, mask.hash}sold proxies: %s
%{private, mask.hash}sNo fork for MO call to set QoS!
%{private, mask.hash}sCurrent call count is %zu SIP callID= %{private, mask.hash}s handover %u
#E %{private, mask.hash}sSipMessageDecoder: no tokens in start line
Dispatching handleDisconnectEvent callback for %s
#W %{private, mask.hash}sIMS services changed during limited connectivity mode, exiting...
%{private, mask.hash}shandleMediaSessionError ignoring RTCP timeout for unconfirmed call
%{private, mask.hash}shandleCreateAudioMediaSessionResponse [sessionId=%u result=%u]
incoming %s request didn't match a termination reason. Defaulting to %s.
#E Delegate is not a MediaSessionStateMachine
#E %{private, mask.hash}sunable to add auth info to %s request: %s
#E %{private, mask.hash}ssessionDidStart session is null
%{private, mask.hash}sImsConferenceCall: still waiting for %u participants to hold before starting conference
%{private, mask.hash}sKeeping headless participant session
  Confirmed:       %{BOOL}d
#E SipMultiPartBody: missing boundary
#E %{private, mask.hash}sError writing to socket: Only sent %zu of %zu bytes to %{public,network:sockaddr}.*P
%{private, mask.hash}smakeOutGoingSipUri: in = %{public}s , out = %{public}s
    RCS group:  %{BOOL}d
#E %{private, mask.hash}sTimer for message sequence %u already exists.
%{private, mask.hash}sUsing dialog-id %{public}s
%{private, mask.hash}shandleBarringAccessAlleviated: retryIntervalExtendedByBarring=%lu
#E %{private, mask.hash}sFailed to create nw_connection due to invalid parameters
#E %{private, mask.hash}sno REGISTER request to send
#W Received an unknown precondition type, not sure what to do
%{private, mask.hash}sthis call was on wifi: no op
#E %{private, mask.hash}sCan't send a spam report for empty remoteUri
handleMediaSessionConfigured sessionId=%llu error=%u
%{private, mask.hash}sreceived message over old SAs %s
   not ready
%{private, mask.hash}sinitializing emergency SIP stack
%{private, mask.hash}smoving to next proxy due to P-CSCF restoration
%{private, mask.hash}sinterface %s is up
#D %{private, mask.hash}sSIP stack is still using access network %{public}s
#E %{private, mask.hash}slocal address cannot reach any proxies
#D started timer %s (%s-%s) with duration %llums
#E %{private, mask.hash}sunable to resolve preferences for given identifier: %{public}s
%{private, mask.hash}sSipStack::reportLazuliSpam
%{private, mask.hash}sSending MLS-Group-Info-Pull request for convId (%s), trxId (%{public}s), isGroupChat: %{bool}d
#E %{private, mask.hash}shandleInviteOrUpdateRequest: couldn't find appropriate fork for remote tag %{private, mask.hash}s
#I %{private, mask.hash}s%{private, mask.hash}s: _retryEnabled: %{BOOL}d (no transport)
#E unable to create IPSec DB
%{private, mask.hash}sNeed to find suitable proxy for new interface address type %s
#D Received Spam ATHM Token. Moving on to retrieving PAT & Reputation Tokens qos=%u
%{private, mask.hash}sthat's error %u of %u
#S readDataFromStream: Expected length: %lu
#D barringTime will be %u
%{private, mask.hash}slogSmsSendAttemptedEvent
#D %{private, mask.hash}sReceived PRACK for response %s
Session configured [sessionId=%llu]
%{private, mask.hash}swill drop %s%s requests
%s%s (%s): %s
%{private, mask.hash}shandleGeneralErrorFromOneProxy(emergency)...
Configured media session successfully, inform delegate
#D %{private, mask.hash}s%{public}s handover detected
#W %{private, mask.hash}sTiming out registration due to error responses from all proxies.
%{private, mask.hash}scleared preferred transport
%{private, mask.hash}srequesting abc snapshot for CT not recognizing chatbot with subdomain
#E Connection information parsed out of order. Must appear after origin: '%c=%s'
#E %{private, mask.hash}shandleIntervalTooSmallResponse: UPDATE transaction has no update type
#E %{private, mask.hash}s%{private, mask.hash}s: MessageEncoding not available
#D %{private, mask.hash}sCall to %s requires emergency session
%{private, mask.hash}screating temporary SA with dict: %s
#W %{private, mask.hash}sregistration timed out on WiFi handover. NOT terminating registration just yet.
%{private, mask.hash}sKey found in prefs file: %s with value: %{BOOL}d
Session terminated [sessionId=%llu]
#E %{private, mask.hash}snot registered for voice calls
#E %{private, mask.hash}sunable to remove group participant(s) on invalid stack %s
%{private, mask.hash}srefer/add [%s] to group %s trx %{public}s
#E %{private, mask.hash}sunable to add new fork
#W %{private, mask.hash}sNOTIFY request has no Subscription-State header
dispatch handleParticipantAdded for %s
#W overwriting timer for %s
#W %{private, mask.hash}sno delegate registered for transaction %s
#E %{private, mask.hash}spolicy session isn't initialized
#E %{private, mask.hash}ssend %zu bytes failed to %{public,network:sockaddr}.*P
Setting prefs (%p) for carrier %s
#E %{private, mask.hash}sError encountered when merging dictionary values for key '%s'
%{private, mask.hash}squeueing base action [%zu] %s
%{private, mask.hash}ssetting remote answer from %{public}s
#E Ignoring body without HTTP response
#D %{private, mask.hash}s%{private, mask.hash}s: already completed.  Ignoring error %s
%{private, mask.hash}sgetSessionById [sessionId=%llu]
Audio ready but config not valid, deferring start [sessionId=%llu]
%{private, mask.hash}sanonymous emergency calls are disabled. Waiting for registration retry.
#E %{private, mask.hash}stoo many transport errors
#E %{private, mask.hash}sderegister called on uninitialized SIP stack
%{private, mask.hash}sProxy provided Retry-After time at %{time_t}ld (%lds)
IMSSMSManager::addParticipants
nw_path local RTP endpoint port=%u RTCP port=%u
#E %{private, mask.hash}sskipping incomplete ipsec-3gpp config %s%s
#I %{private, mask.hash}sno RAck header found in PRACK request
#W %{private, mask.hash}scouldn't find my contact in registration response
#D %{private, mask.hash}s[SIM %u]: Getting current ACB info.
SipStack is no longer existing: no op
%{private, mask.hash}sCRLF-KeepAlive interval already at %u
#I %{private, mask.hash}snasImsReg %s
%{private, mask.hash}ssetScreeningMode [stackId=%s  sessionId=%llu  isScreeningMode=%u]
#E Timezone adjustment offset list %s: '%c=%s'
%s : unable to match reason text (%s != %s)
%{private, mask.hash}sContent Type: %s
#D %{private, mask.hash}svolteRtcpRemote.packetLost %u volteRtcpLocal.senderCount %llu
#E %{private, mask.hash}sUnable to answer call: no local SDP for media session %p
#I %{private, mask.hash}sAnalyticsLogger::logLazuliMessageSessionSendReceive
%{private, mask.hash}sactivateMediaSession (%s): fork %s preconditions have not been met yet, can't activate the session
#E %{private, mask.hash}sPrefs is NULL
#I Stream not ready for data to be written. Buffering request..
#S %{private, mask.hash}sbufToDecodeSize=%zu headerCount=%zu
%{private, mask.hash}shandleDeactivateMediaSessionStatus: %llu result: %{bool}d
#E %{private, mask.hash}s%{private, mask.hash}s: outgoing responses not allowed in state %s
%{private, mask.hash}sstripping Supported header from %u response
#E %{private, mask.hash}sno TLVs
#E %{private, mask.hash}sSpam ATHM TokenResponse empty
Terminate session and ignore the timeout.
#D %{private, mask.hash}sIMSCallInfo::handleSessionHoldFailedEvent for an unknown call
%{private, mask.hash}signoring %{public}s in terminated fork
#E %{private, mask.hash}sno saved transport
#D %{private, mask.hash}sDisableOnNetworkError matched
%{private, mask.hash}sno messages available to send for %s
readData: Length - Expected = %lu, Actual = %lu
#E _handleSSLReadCallback failed. NULL context:
#E Unbalanced quotes at offset %zu: %s
HTTP response doesn't have full body. Waiting for more data. Expected: %lu, Actual: %lu
#E dtmfEventForASCIIChar got invalid input: %u
#E %{private, mask.hash}sNo Security Mechanism
%{private, mask.hash}ssetMediaSessionCreated() is being ignored
%{private, mask.hash}s%s : setting MSS for incoming TCP socket to %d
%{private, mask.hash}sECBM is active.  Renewing emergency registration.
#E %{private, mask.hash}sstart line empty
#D [SIM %u]: Got SSAC voice barring response, Factor = %u, time = %u
#E Invalid CallPsRtpResponse
Location lookup is enabled (roaming=%{BOOL}d)
#D %{private, mask.hash}sIgnore for conference participant.
Adding observer for path on interface %s
%{private, mask.hash}sWill NOT notify SD of connection termination
Failed to serialize HTTP request
#E %{private, mask.hash}scollapseForks: couldn't find fork with tag %s
    Expiration: %{time_t}ld (%lds)
%{private, mask.hash}s----------------------------------------------------
handleMediaSessionConfigured sessionId=%llu result: %s
incoming(stackId: %s sender: %s remote identity: <%s> Contribution-ID: [%s] body length:%zu)
%{private, mask.hash}shandleSdpOffer: initializing MT lazuli session
#W Timer [%s] fired but XcapSession object already deleted: no-op.
#E %{private, mask.hash}sAudio session not found by session ID
%{private, mask.hash}snot on WiFi. Clearing last access network info.
#D %{private, mask.hash}shandling refer response
%{private, mask.hash}semergency registration timed out for current proxy
%{private, mask.hash}sset preferred transport to %{public}s
#E %{private, mask.hash}sno dialog to handle SDP offer
#D %{private, mask.hash}sdeinitializing ims dialogs
%{private, mask.hash}ssilentHangUp called for an unconfirmed call in state: %{public}s
%{private, mask.hash}sSkipped deactivating media session (%llu)
#W %{private, mask.hash}sResolved uri for %{public}s is gone.
#E updateInputFrequencyLevel owner is null
%{private, mask.hash}stimed out waiting for local QoS
%{private, mask.hash}sCall-Info SPAM header received
%{private, mask.hash}sClearing Procedure flags for instance %u
#D %{private, mask.hash}sINVITE timed out to %s
%{private, mask.hash}shandling %u response to %{public}s request in state %{public}s
#I %{private, mask.hash}sproxy changed - terminating old reg subscription and starting a new one
Dispatching handleHoldIndication callback for %s
didResume
%{private, mask.hash}scall is already %s
#E %{private, mask.hash}sreceived %u response to PRACK. Terminating session
#E %{private, mask.hash}sInvalid proxy URI: can't set next interface
%{private, mask.hash}sSkipping expiration and refresh timers for managed RCS connection
#E %{private, mask.hash}sFailed to extract IBIImsMERtcpReceiverReportInd: %d
#D %{private, mask.hash}supdateNetworkServices: Access network has NOT changed
SetConfiguration
#W %{private, mask.hash}sclosed by peer %{public,network:sockaddr}.*P
%{private, mask.hash}srequesting abc snapshot for group fork with context %s
#E %{private, mask.hash}sconfigureRTCPLinkMonitorReq session is null
terminate [sessionId=%llu]
setWifiHotspot [stackId=%s; enabled=%{bool}d]
#E %{private, mask.hash}sContinuing without PAT & Reputation tokens
%{private, mask.hash}sactivateMediaSession: session is not expecting remote RTP packets, won't activate the session with direction %s
#W %{private, mask.hash}sI need IPSec, but Reg 200 OK arrived over default transport: accepted.
#I %{private, mask.hash}susing secure server port for contact
%{private, mask.hash}sremoving ACK retransmit handler for transaction %s
Ignoring startRingbackTone. A session with autostart feature has started on its own for session %llu
%{private, mask.hash}sIgnoring INFO request without valid location discovery Info-Package header
#E %{private, mask.hash}sHow did a %s end up in a %s?
%{private, mask.hash}sMSRP TLS connected to %{public,network:sockaddr}.*P
#D %{private, mask.hash}sNo new calls to merge
#W %{private, mask.hash}sImsTcpNw: remote end closed connection
%{private, mask.hash}sRemote side requests mandatory preconditions
%{private, mask.hash}sImsUdpSocket: detached from source
#I %{private, mask.hash}sAllowing notification in %s
%{private, mask.hash}sattempting registration for (%s) with reason %s
#D Client not initialized, can't get barring info
%{private, mask.hash}s%s local: %{public,network:sockaddr}.*P, remote: %{public,network:sockaddr}.*P inboundSpi: %u, outboundSpi: %u
#D %{private, mask.hash}sMerging %zu calls into existing conference
#D %{private, mask.hash}shandleSystemWake: requesting Barring Info
#E BSF server has challenged us twice. Probably didn't like our response to the 1st challenge. Failing request
#D %{private, mask.hash}s%{private, mask.hash}s: resending %u response
Runtime Vars:
#D No Baseband for architecture or Baseband is currently not available: skip reportCallStatus
#D %{private, mask.hash}sStill waiting on athm=%{bool}d pat=%{bool}d rep=%{bool}d
%{private, mask.hash}sunheld call %{private, mask.hash}s is terminating. Don't need to hold it.
#E NetworkInterfaceMonitor: unable to set dispatch queue for dynamic store
%{private, mask.hash}sstill haven't received an ACK. Terminating our call but keeping the SIP session around.
#D %{private, mask.hash}sSipDialog::handleTryingResponse
%{private, mask.hash}sINFO request to %s trx %{public}s
%{private, mask.hash}sInfinite idle timeout. Never close idle sockets.
%{private, mask.hash}sRemoving %s reference from call and transfer handler
%{private, mask.hash}ssendHoldResumeIndication called for %{private, mask.hash}s with isHeld=%{BOOL}d
#D %{private, mask.hash}sIPTelephonyManager::initiateLimitedAccessRegister: IncomingRegTrxId=%{public}s, CurrentRegTrxId=%{public}s...
#I %{private, mask.hash}sencoding message for existing TCP connection
#E %{private, mask.hash}sunable to send message on invalid stack %s
deactivateSessionWithId [sessionId=%llu direction=%s
#I %{private, mask.hash}sChecking UAC access barring before dialing call %{public}s
#D %{private, mask.hash}sSession acknowledged with %s
Old session is null, cannot replace
#E %{private, mask.hash}sIgnoring null dictionary
%{private, mask.hash}sturning off retransmission of INVITE
#E %{private, mask.hash}sPreferred IMPU is empty!
#D %{private, mask.hash}shandleParticipantLeftConferenceEvent
#D Sending status request CONNECT on instance %u for media %{public}s and RAT %{public}s
%{private, mask.hash}sactivateMediaSession (%s): no valid remote IP address
#W %{private, mask.hash}sreceived redirects from all proxies. Dropping registration.
#E reportCallStatus: instance %u out of bounds (cache size %zu), dropping %{public}s
%{private, mask.hash}sRemove session from _sessions
#E %{private, mask.hash}sInavalid stack %s
No network interface name
GBA_ME: P2 = %s
HTTP Response code %lu not handled
    Id:         %s
%{private, mask.hash}sIMEI: %s
#E %{private, mask.hash}sNo media stream for sessionId %llu
#D %{private, mask.hash}sStack not initialized.  Forcing disconnect to joined parties.
#E %{private, mask.hash}ssendReInvite: offer/answer is not satisfied
#E %{private, mask.hash}sunable to create session refresh request
#E NULL hostInfo or resolver
SipRegistrationEventPackage::handleSubscriptionFailed
%{private, mask.hash}sINFO request %s to group %s trx %{public}s. isEnhancedGroupInfoPull: %{bool}d
%{private, mask.hash}sno device id found. P-Emergency-Info header not added
%{private, mask.hash}sClosing transports for lazuli upon terminating registration
#W %{private, mask.hash}sRemote side requests mandatory preconditions, but we only support %{public}s
BB Server Connection: (0x0)
#E %{private, mask.hash}sno address with mask %{public}s found on media interface %{public}s
#W %{private, mask.hash}sBarring ignored, no change in barring information
#D %{private, mask.hash}sImsSocket: guarded socket fd %d
#E Failed to start sessionId=%llu error: %s
updated stack delegate %s for stack %s to %p
#I %{private, mask.hash}sVoice service is barred 
%{private, mask.hash}sreverting exchange [offer=%{public}s(%{public}s) answer=%{public}s(%{public}s) txn=%{private, mask.hash}s]
carrier: {
#E unable to create dispatch source timer
%{private, mask.hash}sremoving ACK receive handler for cseq %u
Long tone - Starting to send digit: %u To Session: %llu
#E %{private, mask.hash}sUnable to issue emergency redial request - unknown stack id
%{private, mask.hash}sanswering call
%{private, mask.hash}sNot updating connectivity when status hasn't changed
%{private, mask.hash}sstarting timer for %s with action %s and timeout %u
%{private, mask.hash}sskipping %{public}s address %{public,network:sockaddr}.*P
%{private, mask.hash}scannot invalidate non-emergency call
%{private, mask.hash}shandleStopMediaResponse [sessionId=%u result=%u]
 creating new RTP session on destination stack
#E %{private, mask.hash}shandleInitializationFailure
%{private, mask.hash}shandleSessionConfigureResp [sessionId=%llu]
#E %{private, mask.hash}sreceived SUBSCRIBE response, but can't find Event header in request
#D %{private, mask.hash}sUpdating IMPU info received in the 200 (OK) response during last successful registration for stack: %s
%{private, mask.hash}s  TransactionType : SIP BYE (%u)
#E SDPSession expired
#E Set-intersection for accept-wrapped-types is empty
#D %{private, mask.hash}sIs this an EPS silent redial: %{BOOL}d
#D %{private, mask.hash}sFound pending Group Chat leave for new session
#E %{private, mask.hash}sunable to create session update request
canceling %s
#D %{private, mask.hash}scanceling all subscriptions
%{private, mask.hash}spending SA expired prior to successful registration
#D %{private, mask.hash}sinitializing IBINasClient
#W state dump skipped. Too soon!
%{private, mask.hash}sAdding %s to conference %{private, mask.hash}s
#D %{private, mask.hash}sANI at call start: %{public}s
#I %{private, mask.hash}slogSessionProgressEvent
%{private, mask.hash}sSending MLS-Enhanced-Group-Info-Pull request for convId (%s), trxId (%{public}s), isGroupChat: %{bool}d
handleMediaSessionTerminated sessionId=%llu error=%u
Registration:
#D %{private, mask.hash}supdated remote cseq to %u
#D %{private, mask.hash}shandleAuthChallengeResponse: Context: %s, Mode: %s, Result: %s
#D %{private, mask.hash}screated %s for outgoing session with %s
%{private, mask.hash}sstill waiting for local preconditions
Validated recipient for MT SMS - publicUri match
#E no params in security agreement option %s
#W %{private, mask.hash}sNo active remote SDP for fork %{private, mask.hash}s
SleepWakeMonitor instance is NULL! Shouldn't have happened!
#D Sending Start IMS Registration UAC Check Request to BB...
setConfiguration failed for session %llu
#D Initializing NAS client...
%{private, mask.hash}sGenerating response from call termination reason: %{public}s
%{private, mask.hash}swill drop %s%u responses to %s
#E %{private, mask.hash}scurrent AuthInfo doesn't have a Digest auth scheme
#D %{private, mask.hash}sremoving losing fork %{private, mask.hash}s
stack controller NOT initialized properly!
#E %{private, mask.hash}sskipping config for unknown Security Agreement mechanism %s
#S SDPModel Protocol Version set to %llu
      camped: %s%s
#E %{private, mask.hash}sLazuli manager is null
#I %{private, mask.hash}sAnalyticsLogger::logLazuliMessageSipOptions
Media timeout for session(%u) : RTP: %{bool}d, RTCP: %{bool}d
flavorMask |= AddressFlavorTemporary
transactionComplete [isSuccess=%u isTransactionPending=%u actionQueueSize=%zu]
#E %{private, mask.hash}sFailed to fetch TLS Cipher Suite - Failed to get negotiated cipher. Error code: %d
#D %{private, mask.hash}susing Auth from prefs
%{private, mask.hash}sregistering for SMS only due to access barring change
#E %{private, mask.hash}sIMSCallInfo::startCall called on an existing call
%{private, mask.hash}snot emergency registered, using anonymous public URI
#I %{private, mask.hash}shandleAccessCheck (barringDurationInSeconds=%ld) ...
#D %{private, mask.hash}s[SIM %u]: skipBarringMmtelVoice=%{bool}d
#E Auth response is not AKA/Digest
Dispatching handleRegistrationNeeded callback for %s
#E Session config error: %s
#E Bad EVS tx channel setting: %s
added NEPolicy %u for local: %{public,network:sockaddr}.*P remote: %{public,network:sockaddr}.*P
%{private, mask.hash}sIgnoring INFO request without location discovery enabled
%{private, mask.hash}ssending CRLF ping
#D Sending status request END on instance %u for media %{public}s and RAT %{public}s
#E %{private, mask.hash}scan't send a ringing notification when we haven't alerted the user
adding DROP ALL policy at %d
Domain Selector: %s/users/%s/simservs.xml
%{private, mask.hash}sperforming %s
%{private, mask.hash}sRetryRegAccessCheck...
%{private, mask.hash}slogSipResponse: using instance %u
#E %{private, mask.hash}sTerminating call due to auth challenge timeout
GBA_ME: P1 = %s
%{private, mask.hash}sSIP response for lazuli group modification has Warnings? %{BOOL}d
%{private, mask.hash}sInvalid session, don't send subscribe
%{private, mask.hash}shandleMediaSessionError for Media session Id: %llu
%{private, mask.hash}ssipStack is null: no op
%{private, mask.hash}sReceived data length=%zu
#E %{private, mask.hash}sNot a SipRequest or SipResponse
%{private, mask.hash}sclearing %zu items from auth queue
Emergency SIP Stack:
#D %{private, mask.hash}screated %s for incoming %s
%{private, mask.hash}sregisterAudioCodecChangeCb [instance=%u]
#E Invalid default SDP template
stackControllerInitialized stackId=%s appId=%u result=%d
#E streamDidServerDie callback triggered. ---> AVCONFERENCED HAS CRASHED!!! <---.
#E %{private, mask.hash}sunable to send SDP in fork %{private, mask.hash}s : %{public}s
#E %{private, mask.hash}snot registered for SMS
%{private, mask.hash}sneed to reregister. defer refreshing call access network information
#S %{private, mask.hash}sdecode bytes = %zu
  %s (%p)
#E missing end bracket: %s
%{private, mask.hash}swill attempt re-registration %{time_t}ld (%lds), give or take %s
#W Audio RX payload type %u
%{private, mask.hash}sterminating session due to %u response
#E %{private, mask.hash}sFailed to validate recipient for MT request - MDN mismatch
#D Removing call status record on instance %u for media %{public}s and RAT %{public}s
%{private, mask.hash}sImsUdpSocket: No delegate to handle incoming packet from %{public,network:sockaddr}.*P. Discarding packet
#D %{private, mask.hash}s[SIM %u]: Indication converted to ACB info, Factor = %u, time = %u
Terminating session sessionId=%llu
AVCAudioSession [sessionId=%llu]
%{private, mask.hash}sadding initial invitee %s as a participant
Removing expired delegate %s
      IPSecTransport [%{network:in6_addr}.16P <--> ? %hu --> %hu %hu <-- %hu]
%{private, mask.hash}sInitializing for %s with AppId : %u
%{private, mask.hash}sOperator bundle provided ?: %{bool}d _hasOperatorBundle set to: %{bool}d
%{private, mask.hash}sregistration terminated. Continuing to deinitialize.
%{private, mask.hash}sresuming call
%{private, mask.hash}sTearing down TransportLayer
#E %{private, mask.hash}sDiscarding response with status code %u outside valid range [100-699]
#W %{private, mask.hash}sreceived Forbidden/Unknown responses from all proxies.  Falling back to limited-access mode.
stopDTMFDigit
%{private, mask.hash}shandleSessionSetStreamDirectionResp [sessionId=%llu direction=%s]
#I %{private, mask.hash}sretry forced by policy
%{private, mask.hash}s  TransactionType : SIP REFER (%u)
A handover is already in progress on %s.  Deferring until current handover completes.
%{private, mask.hash}semergency SIP stack initialization failed: %s
%{private, mask.hash}sIBISipLogger is not initialized: skip send
%{private, mask.hash}sderegister: not registered
#E Cannot start AVC session due to no SDP session
%{private, mask.hash}sSetting mediaManager to Baseband
#D %{private, mask.hash}sClear active call before conference
%s: (%s:%d) Array assignment too large(%p), got(%zu) max(%zu)
%{private, mask.hash}sstill waiting on %s handshake
#D %{private, mask.hash}sreceived duplicate request
#E %{private, mask.hash}sstackError [error=%d
%{private, mask.hash}sresumed call %{private, mask.hash}s
#E %{private, mask.hash}sUnable to bind socket to interface: %s
Replacing lazuli delegate for %s
#D Transport layer not available for messageEncoding()
#E %{private, mask.hash}ssession initialization failed
%{private, mask.hash}sservice route: %s
#D %{private, mask.hash}sIPTelephonyManager::initializeFromSIM: IncomingRegTrxId=%{public}s, CurrentRegTrxId=%{public}s simInstance=%u stackId=%{public}s
%{private, mask.hash}sCDIV: Supports Target Erasure - %{bool}d
#E %{private, mask.hash}sunable to initialize emergency transport: %s
#E %{private, mask.hash}sUnable to send info for trx %{public}s
#E %{private, mask.hash}scan't find a suitable local address for proxies in list
%{private, mask.hash}sclearing registration failure flags
handleStartMediaResponse RECV: Length: %u, Name: %s
#S %{private, mask.hash}sIs a SipResponse
#E %{private, mask.hash}sunable to add proxy auth info to %s request: %s
#E %{private, mask.hash}sdecode failure on TCP connection
#E %{private, mask.hash}sDid not receive SIP INFO response for trx %{public}s
#E %{private, mask.hash}sunable to create outgoing sip URI for pull : %{public}s , callId : %{private, mask.hash}s
%{private, mask.hash}sAdding initial invitee (%s, %{private, mask.hash}s)
#E %{private, mask.hash}sunable to send optiona request on invalid stack %s
#E %{private, mask.hash}sUnable to attach to NULL dispatch queue
#E streamDidRTCPTimeOut owner is null
%{private, mask.hash}sinvalidate()
%{private, mask.hash}sthis is an initial registration. Sending request through default transport, and do not drop incoming message on default SIP port
#E %{private, mask.hash}sInvalid RTCPRRReportIndication
Dispatching handleConferenceSubscribeEvent callback for %s
#E failed to extract UAC response params
%{private, mask.hash}shandleRTCPSRReportInd RECV: Length: %u, Name: %s
#E %{private, mask.hash}sendCall: unknown callId %{public}s
#E %{private, mask.hash}sNo valid SIP stack to initiate transfer
%{private, mask.hash}sTimed out while waiting for initial participants to go on hold
#E SDPMediaCrypto parse error, no key-params
%{private, mask.hash}sCan not handle incoming call while in limited connectivity
#W altitude is %s; altitude uncertainty is %s
#E %{private, mask.hash}s%{private, mask.hash}s: no transaction user to handle request
#D %{private, mask.hash}sConference session confirmed
%{private, mask.hash}sadded preconditions to outgoing %{public}s
#D Using Spam ATHM key from known issuer
%{private, mask.hash}sclearing 1 item from auth queue
#E Unable to process status request %{public}s.  No call status started for MO call on instance %u with services %{public}s
#D %{private, mask.hash}scan't find matching dialog for callId: %{private, mask.hash}s, fromTag: %{private, mask.hash}s, toTag: %{private, mask.hash}s
#E %{private, mask.hash}sbase64 decode error athm spam tokenresponse: %s size %zu
#E Failed to create media session : %u
Transient: %{BOOL}d
#D %{private, mask.hash}sno session to handle incoming %s request
#E %{private, mask.hash}sUnable to open listener socket: %s
#E Failed to send StopImsRegistrationUacCheck request: %u (%{public}s)
dispatch handleSessionReady for %s
%{private, mask.hash}sLazuli termination:  Waiting for BYE response before terminating
#D Re-initialized NAF transport after connection failure, retrying request
%s
%{private, mask.hash}sResetting state due to registration update while SRVCC cleanup is pending
#E %{private, mask.hash}ssend %s: uri %{sensitive}s trx %s content type %s
#W Invalid RTT config
#D %{private, mask.hash}sIMPU Domain: %{public}s
%{private, mask.hash}sretry not allowed: received error response on reregister
%{private, mask.hash}sshould renew non-emergency registration
#E Ignoring HTTP response since one is already pending
%{private, mask.hash}shandleUninitializeAllSessionsRequestReceipt [isError=%u]
#W %{private, mask.hash}sAppId : %u is already initialized for %s
#I %{private, mask.hash}sauto-renewing registration event subscription
%{private, mask.hash}sisRegistrationRetryAllowed(emergency, statusCode=%u) %{bool}d: Default behavior
#D received GetSsacInfo response for instance %u
%{private, mask.hash}s  Action          : Received (1)
#W SDPSession and Delegate are gone sessionId=%llu
cleanupNonActiveStackControllers [stackId=%s
%{private, mask.hash}sskipToNextProxy...
----- SIP Stack %{public}s (%{public}s) -----
handleMediaSessionTerminated called with kInvalidState for sessionId=%llu
#E %{private, mask.hash}sInvalid IM-SPAM-REPORTING-URI. Can't report spam.
   unique local address
#I %{private, mask.hash}sCarrier spam header reporting is %s for this registration
#W %{private, mask.hash}s%s
#E AVC config is null. Was supposed to be allocated in Audio or RTT session.
%{private, mask.hash}shandleMessageSessionConnected for id: %s
#E SDPConnection: NetworkType set to kNetworkTypeUnknown: '%s'
#E Could not create RTP Listener at %{public,network:sockaddr}.*P
#E %{private, mask.hash}sGroup Chat remove participant(s) failed
%{private, mask.hash}s%s message doesn't have a route set.  Adding default route.
#W Session failed to start [sessionId=%llu]
#E %{private, mask.hash}sUnable to create SSL tunnel
#E %{private, mask.hash}sno lazuli manager
#W %{private, mask.hash}sexpected SDP answer in ACK.  Terminating session.
%{private, mask.hash}sSipSession::sendResponseInTransaction
%{private, mask.hash}sUsing VoiceSystemId %u  for stack %s
Rule-Id: %s, Conditions:[%s, Media: %s], Active: %{bool}d, Target: %s
#W %{private, mask.hash}sAn existing bearer has been updated without ports.  Revoking bearer.
%{private, mask.hash}sUnresponsive peer detection interval = %u seconds
#I %{private, mask.hash}sSuccessfully initialized XCAP client. Ready to process requests
#D already initialized
#E %{private, mask.hash}sUpdateSA failed
%{private, mask.hash}shandleConnected to %{public,network:sockaddr}.*P for %s session
%{private, mask.hash}sUsing next interface address %{public,network:sockaddr}.*P
%{private, mask.hash}ssetTextMediaSessionMode for pending emergency call %s
#I %{private, mask.hash}sNSP error injection: returning error for generateTokenRequestWithQueue
#W %{private, mask.hash}sincoming %u response is missing a To: tag
%s stack controller initialized!
#E %s (spam reporting uri) : %s
#D %{private, mask.hash}sforcing termination of completed transaction %{public}s
#D %{private, mask.hash}sCall %{public}s resume failed!
#W %{private, mask.hash}sAnalyticsLogger::fillCallEndMetricFromEvent - no call
%{private, mask.hash}sserviceInitializeReq [voiceSystemId=%u, instance=%u
%{private, mask.hash}sremoving all ACK handlers
#E %{private, mask.hash}sinitializeCall: can't initialize a call while SipStack is deinitializing
Time taken to init default prefs: %lld ns
%{private, mask.hash}sreceived 401 response. No new registrations allowed until %{time_t}ld (%lds)
#D %{private, mask.hash}srejecting %s request with wrong From: tag %{private, mask.hash}s
%{private, mask.hash}ssend queue is empty
#E %{private, mask.hash}soriginal content size not provided for encoded user text, using encoded size
#E %{private, mask.hash}sFailed MLS group creation trx %{public}s conv %s
#D Got SSAC indication: %u, %u for instance %u
%{private, mask.hash}sInitial location not available
#W %{private, mask.hash}saccess check response triggered from unexpected state %s
%{private, mask.hash}shandling INFO response for key %s trx %{public}s
%{private, mask.hash}sSipSession::handleOutgoingResponse
#E %{private, mask.hash}sNo text stream available
%s}
%{private, mask.hash}signoring duplicate response rseq=%u, cseq=%u
#W %{private, mask.hash}sno delegate to notify of transport initialization
%{private, mask.hash}sEmergency IMPU ranking:
RTCP timeout recovered for session %llu
#E %{private, mask.hash}sNo sip stack %{public}s
#E %{private, mask.hash}sacceptInvitation: no lazuli session object
#E %{private, mask.hash}striggering error in client transaction %{private, mask.hash}s method %{public}s: %{public}s
#D %{private, mask.hash}ssetActiveFork %{private, mask.hash}s to null
#E %{private, mask.hash}sUknown stackID given: %s
%{private, mask.hash}snot adding P-Access-Network-Info to insecure %s
Not setting CNI header with invalid ani timestamp for CellInfoAge
couldn't get data for address %ld
#W Audio TX payload type %u
%{private, mask.hash}s****************** XCAP Config ***************
SRVCC handover is already in progress. Deferring until SRVCC handover completes.
%{private, mask.hash}scall type: %{public}s
#W %{private, mask.hash}sFound unknown key/section with name '%s'
#E %{private, mask.hash}sanswerRttUpgradeRequest: RTT upgrade response attempted in state %s
handleStopDTMFCodeResponse RECV: Length: %u, Name: %s
%{private, mask.hash}ssendTerminateRequest [sessionId=%llu]
#E %{private, mask.hash}sHeader not found: %s
using matching reason %s
%{private, mask.hash}sIMEI Header name: %s
#W %{private, mask.hash}sNot waiting to dial call %{public}s
#D %{private, mask.hash}scall waiting active call is %zu
%{private, mask.hash}sReleasing WoW assertion
Device Type: %{public}s
%{private, mask.hash}sSipStackManager::sendLazuli %{sensitive}s
#E AMR mode-change-neighbor out of range: %s
Not forwarding activated notification to delegate for sessionId=%llu
#E Unable to copy URL from Http Request
#W %{private, mask.hash}shandleInviteOrUpdateRequest: no call
#E %{private, mask.hash}sUnable to initiate transfer on emergency stack
#D %{private, mask.hash}sSipSubscription::subscribeWithExpiration
#E %{private, mask.hash}sconnection receive error: %d
#E %{private, mask.hash}sIncoming REPORT is missing a Message-ID
%{private, mask.hash}sPreconditions enabled in fork (%{private, mask.hash}s) ?: %{BOOL}d
       Allowed Services: %s
#E %{private, mask.hash}sreceived duplicate local offer from %{public}s
%{private, mask.hash}sReceived conference notification with state partial
Queuing terminate and calling stop sessionId=%llu
%{private, mask.hash}slogSipRequestFromNonProxyDropped() no stack
#E %{private, mask.hash}sno Min-SE header in Interval Too Small response
#E %{private, mask.hash}sSDPSession expired in QMIRTPCommandDriver::sessionInitializeReq
#I %{private, mask.hash}sthis is where I will cancel throttling
dispatch handleSessionTerminated for %s
#E %{private, mask.hash}sunable to add group participant(s) on invalid stack %s
#E RTP Transport is null
No more ports available
%{private, mask.hash}sreceived %u to reINVITE; fall back to original call setup
  Local Hold State: %s
%{private, mask.hash}sUnresponsive peer detection probe count = %u
#E No host in Via hop: %s
#W Ignoring RTP timeout notification received for sessionId=%llu
%{private, mask.hash}sthis sipStack still has %zu other active calls: no op
#I Invalid Authorization header: unsupported algorithm %s
%{private, mask.hash}sDesired proxies cannot be reached by the existing transport.  Transport will be initialized.
#E %{private, mask.hash}sCould not send %zu bytes to %s
Terminate requested on sessionId=%llu when state is %u
%{private, mask.hash}susing emergency SIP stack for emergency call
#E Unable to find CPIM Content-Type: - match size: %zu
#E Invalid StartDTMFCodeResponse
#D %{private, mask.hash}sApplication Id: %d
dispatch handleCapabilitiesReceived for %s
%s%d
%{private, mask.hash}sreceived %lu bytes from %{public,network:sockaddr}.*P on outgoing SA socket.  Ignoring.
%{private, mask.hash}swaiting for call to resume
#E Failed to stop media session : %u
%{private, mask.hash}sWill NOT notify SD of connection termination due to Disabled|Reprovision|RegenerateUrl registration mode
%{private, mask.hash}sNo policy present, can't disable registration for wrong country.
%{private, mask.hash}sresetting settings
dispatch handleSessionEvent for %s
Node selector: %s?%s
#E %{private, mask.hash}sunable to create SipSession for call to %s
#D requesting current SSAC info for instance %u
#W Received an initialized event while already initialized [sessonId=%llu]
#E %{private, mask.hash}sdrop %zu bytes on null socket
#E %{private, mask.hash}sWork pending at clear athm=%{bool}d pat=%{bool}d rep=%{bool}d
#E %{private, mask.hash}sunable to create SDP in fork %{private, mask.hash}s
#E SDPMediaCandidate parse error, no componentId
#E unrecognized flag '%s' in %s
%s : unable to match reason cause (%u != %u)
#D %{private, mask.hash}shandleCallInvalidated actually removing the call
#I %{private, mask.hash}s%s
#E Remote connection information not found
%{private, mask.hash}sservice %s not barred
#D %{private, mask.hash}signoring response
Merged Prefs:
%{private, mask.hash}sconversation for refer not found, queueing: %s
%{private, mask.hash}s%s requests aren't supported in dialogs. Seeing if we have an appropriate delegate.
#E %{private, mask.hash}sImsTlsSocket: Failed to read App data from transport. Error: %d
Dispatching handleTryingEvent callback for %s
    Initial reg:         %{BOOL}d
%{private, mask.hash}supdating access network info to %{public}s
%{private, mask.hash}sClearing lastPreferredPublicUri 
%{private, mask.hash}sdisabled mode is, uh, disabled. I'll keep retrying.
#E %{private, mask.hash}svalid() Invalid media
%{private, mask.hash}shandleServiceUnavailable. Retrying MESSAGE again after %u seconds.
#E Handover timer fired for sessionId=%llu
Starting handover stack switcher sessionId=%llu
%{private, mask.hash}sCancelReason: %{public}s : %u : %{public}s
Adding record for emergency
%{private, mask.hash}ssent initial REGISTER. No new registrations allowed until %{time_t}ld (%lds)
%{private, mask.hash}ssendStartDTMFDigitRequest [sessionId=%llu]
%{private, mask.hash}scancel connection
#E %{private, mask.hash}sCannot handle disconnect due to null socket
%{private, mask.hash}supdated SA with id = %u, spi=%u(%x)
Switch stack immediately
Adding extra params for Reason %s :
#E %{private, mask.hash}sconfigureQMISession session is null
%{private, mask.hash}shandleNewFork: setting need to send update to %{bool}d in fork %{private, mask.hash}s
%{private, mask.hash}skeeping old SAs around for a bit: %s
#E %{private, mask.hash}sSipMessageDecoder: invalid Request-URI in start line: %s
%{private, mask.hash}sready connectionId=%{uuid}.16P
%{private, mask.hash}sreason for updateRegisteredServices: %{public}s
createNwPath
#E %{private, mask.hash}sNo call %{public}s found for transfer target
%{private, mask.hash}sinterface %s is not up
%{private, mask.hash}sstarting MT call on access network %s
%{private, mask.hash}shandleGeneralErrorFromAllProxies(non-emergency)...
#D %{private, mask.hash}sIPTelephonyManager::cancelUssdSession: session not found for stack %{public}s
#D barring disabled for instance %u
#E %{private, mask.hash}scouldn't find a call for Media Session. Terminating session id: %llu
Carrier Prefs for %s
#E %{private, mask.hash}sDialogManager is NULL. Can't subscribe to Conference events
%{private, mask.hash}sFailed to send refer. %s
#E %{private, mask.hash}scan't send a BYE in a terminated session
%{private, mask.hash}ssessionInitializeReq [sessionId=%llu appId=%u]
#W %{private, mask.hash}sregisterWithConfig: registration is disabled
#E %{private, mask.hash}sreceived fatal error: %s
%{private, mask.hash}sCurrently unregistered, but response has capabilities
#E %{private, mask.hash}sNo Transport Layer to setup transports
#W Ignoring didStop notification received for sessionId=%llu
handover sessionId=%llu
#D SipDialog::dialogTerminated()
#E %{private, mask.hash}scan't subscribe if we don't have a dialog
%{private, mask.hash}sreceived a BYE while waiting for a response to our BYE. Terminating session.
isConfigEqualToActiveConfig [sessionId=%llu isEqual=%u]
%{private, mask.hash}sremoving queued activity %s
#E Failure to read data from stream. Errorcode: %d
%{private, mask.hash}signoring timer %{public}s in state %{public}s
#E %{private, mask.hash}sno client INVITE transaction to cancel
  In-Reply-To Contribution ID:         %s
released power assertion %{public}s
#E %{private, mask.hash}ssendUpdate: dialog contains no forks
   private address
RTCP reports are not allowed.
#D %{private, mask.hash}s[SIM %u]: *response.skip_barring_sms_t9 = %u
%{private, mask.hash}stoo many re-registration errors. Next attempt will be an initial registration.
#E %{private, mask.hash}stransferee (%{public}s) and transfer target (%{public}s) must be anchored to the same SIP stack
#E CallAudioServiceClient framework not available - cannot create audio session
#E createAudioSettings Remote media is null
Found [action=%s sessionId=%llu]
#W Handover completed for non-handover session
%{private, mask.hash}sset Virtual Interface MTU to %u
#D %{private, mask.hash}sTracking lazuli session %{public}s
#W %{private, mask.hash}sPreconditions satisfied for unknown fork %{private, mask.hash}s
#E %{private, mask.hash}sQMI client is supposed to start only after VSID is retrieved. Do not proceed with Service Bind request.
#S Deleting NafServerInfo: %p
#D Received network congestion indication from baseband
#E %{private, mask.hash}sCan't send a spam report without any message IDs
#E %{private, mask.hash}sIncoming SEND required header is missing.
#E %{private, mask.hash}sno call manager delegate specified
~AVCRTTSession [sessionId=%llu]
%{private, mask.hash}shasDeferredRegistration: set retryAfter = 1 instead of %ld
%{private, mask.hash}shangUp: already terminating
    Registered Services: %s
%{private, mask.hash}shandleGeneralErrorFromOneProxy(non-emergency)...
%{private, mask.hash}sprocessing send queue
#D %{private, mask.hash}sConference call activation accepted
#E GetSsacInfo request failed: %u (%{public}s)
#E Port out of range in media line: '%c=%s'
#E Dropping SIP %{public}s
%{private, mask.hash}sscheduleRetry: got retryInterval = %lu
%{private, mask.hash}sStack marked as invalidated-- skipping uninit delegate call
#D %{private, mask.hash}sConference call activated
%{private, mask.hash}sProcessing %zu queued messages after Large Message Mode transfer
remove sessionId=%llu
%{private, mask.hash}sImsCall has pending invalidation. Invoking invalidate.
#D Resolving for type %s
#E %{private, mask.hash}sIceClient creation failed.
#W %{private, mask.hash}sunable to subscribe to dialog events
%{private, mask.hash}sSkip AP wake ping for lazuli
#D %{private, mask.hash}ssubscription terminates at %{time_t}ld (%ds) _silentTermination? %s
#D %{private, mask.hash}scheckTimers: no expiration time
%{private, mask.hash}sSSLSetPeerDomainName attempt with domain %s
#E Unknown radio vendor %d
%{private, mask.hash}sisRegistrationRetryAllowed(emergency) No: null SipStack
%{private, mask.hash}sattempt %u :resolved %{public}s to %zu addresses
%{private, mask.hash}ssendSessionEnded. isEmgr: %{BOOL}d, isEmgrNormal: %{BOOL}d
#D %{private, mask.hash}sPreempting unconfirmed calls for outgoing emergency call
#D %{private, mask.hash}snotifyDelegates for newly alleviated services=%{public}s
%{private, mask.hash}ssending queued large message on conversation %s
#E %{private, mask.hash}sunable to begin non-emergency call: invalid stack id %{public}s
%{private, mask.hash}sWPS Call failure detected - attempting to cleanup WPS state
%{private, mask.hash}sRemoving participant from original call
#E %{private, mask.hash}sError indication for request: %s error: %d  reason: %s
#E Failed to re-initialize NAF transport
%{private, mask.hash}srequesting abc snapshot for registration failure with context %s
%{public}s
%{private, mask.hash}sSipStack is null: no decision to try to shortcuit the retry
%{private, mask.hash}sRemote answers a different SDP
Context: %llu
#W The text direction was set to undefined, setting to %s
%{private, mask.hash}sexiting emergency state!
%{private, mask.hash}sinitializing IBISipLogger
#E %{private, mask.hash}sIMSCallInfo::continueCall falling back to CS
%{private, mask.hash}sremote preconditions have been satisfied in fork %{private, mask.hash}s
#E scheduleSystemWake requires a container name
%{private, mask.hash}sno need to renew emergency registration
#S %{private, mask.hash}sIs a SipRequest
#E %{private, mask.hash}sReceived 403 for Group Chat MESSAGE. Propagating failure and maintaining registration
%{private, mask.hash}sno client INVITE transaction to cancel, going right to terminated state
[LazuliSession] uri=%s
==================== [SID:%llu%{public}s] HTTP Response %{public}s <----- %{public}s [%{public}s:%u] ====================
#D %{private, mask.hash}sSipSubscription::handleSubscribeResponse
#E %{private, mask.hash}signoring auth response for invalid stack %s
#E %{private, mask.hash}sTried to setMediaSessionIdForCall to %llu while we have an active mediaSessionId %llu
#E Invalid HTTP Request URL
#D %{private, mask.hash}sIMSCallInfo::handleInProgressEvent for an unknown call
#D %{private, mask.hash}sResetting addendum
%{private, mask.hash}sWill initialize session: %{bool}d
%{private, mask.hash}sconnection ready
scheduleSkywalkInit [sessionId=%llu]
Unable to parse network info for mcc/mnc/cell id
%{private, mask.hash}sDeinitialized SSL tunnel
#E Could not bind to RTCP port at %{public,network:sockaddr}.*P error: %d
#E Invalid ConfigureAudioMediaSessionResponse
#E No RTCP socket associated with port %u for session %llu
#D %{private, mask.hash}sadded [Dialog callId=%s conversationID=%s] to map
#D No baseband for architecture
Created RTPMultiMediaSession with sessionId=%llu
%{private, mask.hash}sCB: Supports Media Tag - %{bool}d
#E %{private, mask.hash}sUnable to find configuration for %s
%{private, mask.hash}sEmergencyCallhandler: resetting conditions
  IMS Call ID:   %{private}s
%{private, mask.hash}sneither side requires preconditions, so let's skip them
#E %{private, mask.hash}striggerClientTransactionError: client transaction %s no longer exists
Setting SIP status code for %s to %u
%{private, mask.hash}sTreating notification as Partial.
%{private, mask.hash}sValidated recipient for MT request - MDN match
%{private, mask.hash}signoring PRACK error in confirmed session
%{private, mask.hash}snew expiration is %{time_t}ld (%lds)
#W %{private, mask.hash}sanonymous emergency calls are not allowed, and we aren't able to register. Canceling emergency call.
%{private, mask.hash}snw_connection_send success
#E No NetworkInterfaceMonitor found
%{private, mask.hash}ssendStopDTMFDigitRequest [sessionId=%llu]
%{private, mask.hash}supdated stored proxy auth response:
#W %{private, mask.hash}sUnknown timer fired [timerId=%s]
#E Failed to create RTP nw_path_evaluator
%{private, mask.hash}sstill waiting for headers
#D %{private, mask.hash}sIBINasClient not initialized. Don't request barring info.
#E %{private, mask.hash}sMessage encoding not available from user agent
%{private, mask.hash}sremoveParticipant
%{private, mask.hash}sCall is confirmed, but media is not active. Waiting for Media to get activated.
#E Bandwidth information parsed out of order. Must appear after origin: '%c=%s'
#E %{private, mask.hash}sendCall: CallInfo %{public}s is in a conference call, but manager doesn't have one.
#D %{private, mask.hash}sUse normal stack for emergency
Invalidating stack %s
#D %{private, mask.hash}sSkipping unauthorized REGISTER
%{private, mask.hash}sresolution already in-progress for hostname %{public}s
#E GBA_ME failure. Failed to compute KsNaf
#D %{private, mask.hash}sclient PRACK transaction completed successfully. Seeing if we need to send an update.
#E No RTP socket associated with port %u for session %llu
#D %{private, mask.hash}sAnonymous redial is set for this call, attempting new emergency call.
#E %{private, mask.hash}sendConferenceCall: no existing conference call
#E %{private, mask.hash}sEvent notification: ID of thumper call is empty
#E Failed to create rtp nw_parameters
#W %{private, mask.hash}sbailing timer check as expiration is not yet set
%{private, mask.hash}sThis session is done, removing references...
#W %{private, mask.hash}sdropping %lu bytes on inactive transport %s
%{private, mask.hash}sCall confirmed
Wake on wifi has %zu holders
#E Unable to send SMS message: %s
%{private, mask.hash}sNot clearing throttling on interface change, per policy.
%{private, mask.hash}ssending registration terminated due to sip registration error %s
#D %{private, mask.hash}sTokens received
%{private, mask.hash}stlv.fRtcpReportingInterval=%u
#E %{private, mask.hash}sUnable to attach to NULL socket descriptor object
#E Bandwidth set to kBWTypeUnknown: '%c=%s'
#E %{private, mask.hash}sStatus header not found.  Dropping report for MSRP Message-ID %s
Init RTP listener %{public,network:sockaddr}.*P
%{private, mask.hash}sinterface %s no longer contains address %{public,network:sockaddr}.*P
#E Precondition has invalid status: %u
#E %{private, mask.hash}sReceived unexpected payload while waiting for pong; size %zu
#I %{private, mask.hash}sRequested to create outgoing video call - behavior is undefined
#E no NAS client object
%{private, mask.hash}sSipStack::addLazuliParticipants
%{private, mask.hash}sAll calls have ended, update registration for deferred barring indication
#D %{private, mask.hash}sIBINasClient stopped
#E %{private, mask.hash}sreceived AKA response with wrong Response type
#E Failed to start session which owner is null
#E %{private, mask.hash}sMSRP path is unavailable.
%{private, mask.hash}sSkipping failed address %{public,network:sockaddr}.*P
valid() Invalid connection
#I %{private, mask.hash}sbarring %s call (barringFactor = %u, rand3 = %u, rand4 = %lf, Ty = %u)
Short tone - Sending digits to session %llu
#E %{private, mask.hash}sno user agent
%{private, mask.hash}sactivateMediaSession (%s): waiting for media session to be configured
#E Tried to set MaxPacketizationTime to %u setting it to %u
Initializing Emergency prefs from dict
#E Couldn't unpack ARI result
    reported: %s%s
#W %{private, mask.hash}sdesired stack (%{public}s) not equal to actual stack (%{public}s)
%{private, mask.hash}sFork %{private, mask.hash}s has remote SDP, setting QoS established
matched %s
%{private, mask.hash}sIgnoring INFO request without location discovery body
#E %{private, mask.hash}shandleAck: dialog has no fork
#D %{private, mask.hash}sreportCallStatus Start with services %{public}s for instance %u on %{public}s, handoverFromWiFi %u...
%{private, mask.hash}sadding first route hop %s
#E %{private, mask.hash}sIncoming SEND with group management info has not been negotiated.
%{private, mask.hash}sReceived a 181, not stopping local ringback tone
%{private, mask.hash}scontinueSendRequest(): set opaque=%s
%{private, mask.hash}scancel listener
#E %{private, mask.hash}sunable to initialize TCP transport: %s
%{private, mask.hash}snotifyCallsOfAccessNetworkChange: no current access network
%{private, mask.hash}ssendSessionStarted. isEmgr: %{BOOL}d, isEmgrNormal: %{BOOL}d
#D %{private, mask.hash}s%s Declined, locally busy.
%{private, mask.hash}sstarting Lazuli session
%{private, mask.hash}s%{public}s [offer=%{public}s(%{public}s) answer=%{public}s(%{public}s) txn=%{private, mask.hash}s]
%{private, mask.hash}sContinue to resetProxyOffset()...
%{private, mask.hash}sDropping composing imdn %s on %s
#D %{private, mask.hash}sResending response
Deferring new registration subscription
Sending handover complete notification for stack type [stackId=%s  stackType=%s]
Not setting P-CNI header with invalid timestamp
#W %{private, mask.hash}sFound a renamed/matching key. '%s' has been renamed to: '%s'.
#E %{private, mask.hash}s%{private, mask.hash}s: no TU to handle response
%{private, mask.hash}sHandling RTT upgrade request
Dispatching handlePreIncomingEndEvent callback for %s
#E Unable to parse auth directive: %s=%s
#E %{private, mask.hash}sunable to create secure networking session
start timer for sessionId=%llu
#D %{private, mask.hash}sold barred services=%{public}s
%{private, mask.hash}sinvalidating call %{private, mask.hash}s
%{private, mask.hash}snon-emergency stack %s doesn't have a valid public URI
#E %{private, mask.hash}sNEVirtualInterfaceAddAddress failed
%{private, mask.hash}sWill not report.
%{private, mask.hash}sexpiration timer fired.  Telling my owner.
#D %{private, mask.hash}sStarting conference call with %zu other participants
#E %{private, mask.hash}sunable to initialize transport: %s
%{private, mask.hash}sGot auth challenge request, restarting emergency registration timeout
%{private, mask.hash}sconnect (async) outgoing connection id=%{uuid}.16P remote address=%s
%{private, mask.hash}susing existing transport for IPSec initialization
#E %{private, mask.hash}s%{private, mask.hash}s: dropping registration due to %{public}s error %{public}s
#E %{private, mask.hash}sIncoming SEND FromPath header does not match the one in SDP
%{private, mask.hash}sUpdate needs Geolocation for NormalSetupEmergencyCall
#E %{private, mask.hash}sno transaction specified
Session direction is %s
#E SipReferEventPackage: unable to decode message from sipfrag: %s
#W %{private, mask.hash}sInvalid CDIV request
~AVCAudioSession [sessionId=%llu]
%{private, mask.hash}sRouting incoming OPTIONS tags to Lazuli
%{private, mask.hash}sset _expirationTime to %ld from response's expires: %u before notifying CT
%{private, mask.hash}sUnsolicited Requests: ON, Delay: %u seconds
#I %{private, mask.hash}sreplacing host %s in top Route hop with P-CSCF %s
Initialize
%{private, mask.hash}sSipStackManager::createNewLazuliSession
#E startRingbackTone already playing for session id: %llu Received: %llu
#E %{private, mask.hash}sSipTcpConnection::handleConnected manager is null
#E %{private, mask.hash}scan't send a session refresh in a terminated session
#E %{private, mask.hash}sneed to add preconditions, but there's no SDP
#I %{private, mask.hash}sfake registration expires %{time_t}ld (%lds)
#E %{private, mask.hash}sFailed to create nw_connection
%{private, mask.hash}sSuccessfully subscribed to conference event
Set direction requested on [sessionId=%llu] when state is %u
#D %{private, mask.hash}screated %s for %s subscription
%{private, mask.hash}sgot expires = 0 for a registration. Treating it as a terminated notification.
%{private, mask.hash}sWill notify SD of connection termination for non-SIP error on managed connection
%{private, mask.hash}sNAF: %s:%u:%s
#W %{private, mask.hash}sa media error has been detected, but the emergency call will be continued
%{private, mask.hash}semergency transport initialization succeeded
#D %{private, mask.hash}sSending kIMSCallStatusActive
#I %{private, mask.hash}sAnalyticsLogger::logLazuliRefer
#E %{private, mask.hash}sAudio sessions not found by stack ID
SipSessionInterface::~SipSessionInterface()
bypass_rcs_cellular_override is set — skipping interface binding for %{private}s
#E %{private, mask.hash}sMalformed Status header (too short).  Dropping report for MSRP Message-ID %s
#W %{private, mask.hash}sstack %s: dropping %lu bytes from %{public,network:sockaddr}.*P, which is not from myProxies at [%s]
#E %{private, mask.hash}sImsTlsSocket: handle error %s
    no connections
#E %{private, mask.hash}sTimeout generating Spam ATHM TokenRequest (sequence=%u. registrationClientSequence=%u)
%{private, mask.hash}sWPS call ended normally, not performing CSFB
%{private, mask.hash}ssystemClockDidChange, device not registered: keep checking registration refresh timer
%{private, mask.hash}shandle result.code %d
End of Write stream
#D Adding listener for %{public}s on instance %u with barring for %{public}s
%{private, mask.hash}sreport connection error to %s
#D %{private, mask.hash}sAdding PAT=%{bool}d TLVs=%hu
%{private, mask.hash}sWe neither have a local SDP answer pending nor do we need to update preconditions.
%{private, mask.hash}sSkipping registration coalescing for managed RCS connection
#I %{private, mask.hash}susing subscription expiration %u from config
%{private, mask.hash}sisVoiceRegistrationBarred: not listening for access barring
#E Stream not open for reading:
%{private, mask.hash}ssending data with existing connection using server outbound SPI %u (%x)
#E %{private, mask.hash}sDropping response, because FromPath header does not match the one in SDP
%{private, mask.hash}ssticking with %s registration policy
%{private, mask.hash}sSkipping fake deregistration for managed RCS connection
%{private, mask.hash}snot incrementing retry counter for error %s
%{private, mask.hash}ssubscription attempt %u of %u failed
%{private, mask.hash}ssendCreateMediaRequest [sessionId=%llu]
#E %{private, mask.hash}sclient/server addresses not initialized
#D %{private, mask.hash}sendCall: reason= %s (%s); confirmed= %{BOOL}d
#E %{private, mask.hash}slocal port info unavailable!
#W %{private, mask.hash}sremote end tried to cancel a %{public}s request. Ignoring
#E %{private, mask.hash}sauditTokenData is null
%{private, mask.hash}sRequire interface %s
%{private, mask.hash}sreceived update voice barring factor: %u, time: %u, SpecialAccessClass: %u, services: %s
%{private, mask.hash}ssessionDirectionChangeFailed [sessionId=%llu]
%{private, mask.hash}scancelPendingEmergencyCall: no pending emergency call
Empty handover completed for %s
%{private, mask.hash}snot terminating registration due to %s since our prefs say not to
%{private, mask.hash}sstartTimer: nextRetryTime has passed. Retrying immediately.
%s%{bool}d
#S ***** INCOMING DATA *****
    Remote cseq:    %u
#E %{private, mask.hash}ssessionDidInitialize session is null
%{private, mask.hash}sKeepalive wakeup received
%{private, mask.hash}shandleEvent: not handling
%s: {
#E Invalid GetMediaCapabilityResponse
#E Invalid StopMediaSessionResponse
handleConfigureAudioMediaResponse RECV: Length: %u, Name: %s
%{private, mask.hash}snew: removing unused connection, not resetting connection, and not resetOnDelete
%{private, mask.hash}ssending request through pending SA
    %s (%p)
#I %{private, mask.hash}sinitializing SIP stack %{public}s
%{private, mask.hash}sSipStack::transferComplete
%{private, mask.hash}sWe don't shutdown incoming connection. Mark it for reset on delete
#E %{private, mask.hash}sConnection is not ready to receive data
%{private, mask.hash}sInitializing TransportLayer
%{private, mask.hash}sretrying registration with proxy (%s)
  XCAPEventDelegates:
#W %{private, mask.hash}sreceived Forbidden/Unknown responses from all proxies.  Disabling IMS registration.
handleMediaSessionTerminated sessionId=%llu result:%s
#E CallAudioServiceClient framework not available - cannot create RTT session
#E Failed to get message encoding - decoder will be null
#E %{private, mask.hash}saddDefaultAuthorization request is null
Calls:
#E Unable to create session for media type %s
#E %{private, mask.hash}sreceived rejection answer:
%{private, mask.hash}sfound active emergency dialogs.  Renewing emergency registration.
#E %{private, mask.hash}sSipTlsTransportGroup: sendMessage: no active connection
%{private, mask.hash}snew auth challenge: %s
%{private, mask.hash}ssip_call_id_len_t8: %u
#S %{private, mask.hash}srtcp RR Count %u packets %llu
Transport:
#E %{private, mask.hash}sIncoming 200 response does not contain a recognized contact URI
#I Handling write stream callback with event '%s'
#E %{private, mask.hash}sError retrieving PAT+Reputation tokens: %s
%{private, mask.hash}swill attempt outgoing Re-INVITE for TTY in %u ms
updated message delegate %s for stack %s to %p
#E %{private, mask.hash}sNo SipSession for group modification for trx %{public}s
#D %{private, mask.hash}scanceling subscription
%{private, mask.hash}s%s%s%s%d
%{private, mask.hash}sSSLHandshake not yet completed. Errorcode: %d
%{private, mask.hash}sUsing fork %{private, mask.hash}s for bearer %u
#D %{private, mask.hash}squeuing %u response: %zu outstanding reliable responses
%{private, mask.hash}sSocket not  yet connected. Queue up shutdown
%{private, mask.hash}sscheduling retry with interval 1
%{private, mask.hash}stime to switch proxies
got back seqCnt=%u, signedSignature=%s
%{private, mask.hash}s_sock is already null
%{private, mask.hash}swe need to send an SDP answer
%{private, mask.hash}sI'm responsible for session refresh
#D Client bound for instance %u
%{private, mask.hash}sRemove KeepAlive power assertions for stackId= %s
#E Failed to set stream property on write stream: kCFStreamPropertyAccountIdentifier
#E App data read from transport failed. Error: %d
matched %s with score %d
readData: No bytes available to be read
%{private, mask.hash}sinitialized %s (isMTOnly: %{BOOL}d)
#W The audio direction was set to undefined, setting to sendrecv
#E %{private, mask.hash}snw_connection failed with error=%du
%{private, mask.hash}sisVoiceRegistrationBarred: non-zero barring factor
#E no observer found with id %s
#I %{private, mask.hash}sterminating call with media session id: %llu due to %s
#W %{private, mask.hash}sdropping %lu bytes on DefaultSipPort of %s
Configured Media for Local hold, now de-activate media
#W %{private, mask.hash}sExit emergency state call on normal registration client, ignoring
%{private, mask.hash}sNo emergency call to terminate.
call was dialed as WPS
#W %{private, mask.hash}sincoming message has invalid Via header.  Dropping.
%{private, mask.hash}scurrent proxy is now #%lu (%s)
  Client txns:    %zu
%{private, mask.hash}sTracking chat with conversationID %s
inteface %s path satisified
#E %{private, mask.hash}sperformLocalResume: we're confirmed but don't have a media session. Killing call object.
Ignoring configure request for session %llu
%{private, mask.hash}sUAC barring is in effect for service %s
cancelNwConnectionsAndListeners [sessionId=%llu]
%{private, mask.hash}sexitEmergencyState: still have an emergency call
#E %{private, mask.hash}sconfigureRTCPReportsReq session is null
%{private, mask.hash}ssendDTMFDigit [sessionId=%llu digit=%u]
#I %{private, mask.hash}sUsers in the NOTIFY = %zu
#E %{private, mask.hash}sunable to set up temporary SA for server port: %s
#I %{private, mask.hash}sAnalyticsLogger::logSessionTerminationEvent
#I %{private, mask.hash}sset active transport to default transport
%{private, mask.hash}scall ended while processing %s event
#I %{private, mask.hash}susing default subscription expiration
%{private, mask.hash}sNot enough data in decodeBody
#I %{private, mask.hash}sCF Erasure not supported. Perform deactivation instead
#E Unmatched MMTel response!
#E TTY media information missing.
#E %{private, mask.hash}sConnection queue is null
%{private, mask.hash}sdropping registration terminated notification while CSFB mode is enabled
%{private, mask.hash}sreceived auth challenge error from all proxies
loading IPSec functions
#E %{private, mask.hash}sIncoming Byte-Range size is %u but body size is %zu
#I %{private, mask.hash}sReceived Thumper registration error: %s
%{private, mask.hash}snot resetting registration mode until we see one of these events: %s
%{private, mask.hash}sProcessing blob in %u chunks with content size %u
%{private, mask.hash}spreconditions are active. Sending Session Progress.
#D %{private, mask.hash}signoring duplicate %s request
#E SDPSession expired in AVCRTPAudioSession::setConfiguration
%{private, mask.hash}sWill update XCAP manager about changes in IMPU information
%{private, mask.hash}shandleBarringAccessAlleviated: adjusted and scheduled registration retry for %{time_t}ld (%lds)
%{private, mask.hash}sAdd KeepAlive power assertions for stackId= %s
%{private, mask.hash}sSession already terminated or terminating, not sending SessionAcknowledged event
#E %{private, mask.hash}s%{private, mask.hash}s: can't send response from NULL state
#D %{private, mask.hash}smapped %s to %s
%{private, mask.hash}screating virtual interface with mtu=%u
%{private, mask.hash}sregistration policy will retry on emergency stack, not reporting registration error: %s
%{private, mask.hash}sregistration event subscription failed
%{private, mask.hash}supdating config
%{private, mask.hash}sstarting new activity for %s
#E %{private, mask.hash}sCan't send INVITE with offer: remote answer pending
%{private, mask.hash}ssetScreeningMode. Enabled?: %{BOOL}d
%s : skipping %s address %{public,network:sockaddr}.*P
%{private, mask.hash}sclearing throttling timers for WiFi <---> Cell RAT switch
%{private, mask.hash}sinitialized proxy list
#E NetworkInterfaceMonitor: SetNotificationKeys failed
#D %{private, mask.hash}sall outstanding response SDP has been PRACKed
%{private, mask.hash}shandleLazuliOfferAnswer: we have %s
Updating URI of conversation %s from %{sensitive}s to %{sensitive}s
#E Challenge response doesn't have WWW/Proxy authentication header
%{private, mask.hash}sDisable TLS 1.3
%{private, mask.hash}sParticipant %s , status = %s
#W ignoring timer with no container
#E Unexpected protocol %s (%d)
#E Could not find TX payload type
#E %{private, mask.hash}sunknown sip message type: %s
%{private, mask.hash}sno %s service access barring in effect
#W %{private, mask.hash}ssocket already attached to dispatch queue
%{private, mask.hash}sWiFi: Keep current keepalive interval at %u, min: %u
Dispatching handleAcknowledgedEvent callback for %s
%{private, mask.hash}sProxy list changed.  Clearing throttling and resetting proxy offset...
%{private, mask.hash}sscheduleRetry: barringEndAt %lu
#E Session information parsed out of order. Must appear after origin: '%c=%s'
#I %{private, mask.hash}sno remote client address specified.  Rejecting incoming message from %{public,network:sockaddr}.*P
%{private, mask.hash}sWill NOT notify SD of connection termination following 403
#W Text media session is not configured, possibly due to incomplete upgrade.  Waiting for upper layers to generate new offer.
%{private, mask.hash}s%s matched non-private emergency prefix %s
#W %{private, mask.hash}sRequest to update port for stream of type %s, but actual stream is of type %s
Changing active stack type for %s, old: %s new: %s
Audio ready without pending start action [sessionId=%llu]
#E %{private, mask.hash}sImsUdpSocket: failed to create socket : %s
%{private, mask.hash}scancel listener complete
%{private, mask.hash}sUsing first found active Thumper call: %{private, mask.hash}s [%{private, mask.hash}s]
#E Failed to create header '%s'
#D ignoring duplicate START call status request (%u total) on instance %u for media %{public}s and RAT %{public}s
#I %{private, mask.hash}sdeferring delivery of incoming %s until system wake
%{private, mask.hash}sgroup modification action %{public}s result %{public}s for %s
#N Connection interrupted
#E %{private, mask.hash}sreceived close event for connection to unknown host %s
#D %{private, mask.hash}sending subscription
#I %{private, mask.hash}sIgnoring network unreachable error
#D %{private, mask.hash}sStrange: how could stack be null? startCall() failed.
#D %{private, mask.hash}sLeaving Group Chat %{public}s with trx %s. isE2EE=%{bool}d
Unable to parse P-Last-Access-Network-Info header reg timestamp: %s
%{private, mask.hash}sclosing TLS transport
%{private, mask.hash}sAlready subscribed to Conference Events
%{private, mask.hash}sReuse Auth Credentials ? %{BOOL}d
%{private, mask.hash}s%s is booted. Swallow refer termination, go back to Joined state.
%s (%s)
#D %{private, mask.hash}sIMSCallInfo::handleRingingEvent for an unknown call
#D %{private, mask.hash}ssaved deviceRefId: %{public}s
#I %{private, mask.hash}sAnalyticsLogger::logSipRequestFromNonProxyDropped. Incrementing counter
%{private, mask.hash}sCouldn't set delegate for stateMachine
startTimerForRequest requestId=%u sessionId=%llu
Session deactivated notification received for [sessionId=%llu]
#W TTY with unexpected format parameters parsed: '%s'
%{private, mask.hash}sprocessDTMFDigitQueue [sessionId=%llu]
#I %{private, mask.hash}sNOTIFY doesn't have a registration entry for associated URI %s
#D %{private, mask.hash}sPicking IMPU from list of IMPUs sent to us by SD (read from SIM Config)
Reporting the %s of the VoLTE session [sessionId=%llu]
#E RTCP socket still attached to dispatch source [sessionId=%llu]
%{private, mask.hash}srejectWithResponse: no server INVITE transaction
%{private, mask.hash}snot terminating registration due to %s since no legacy RAT types are available
#E %{private, mask.hash}sSkipping to next proxy for lazuli stack due to termination before we reached Active state.
#E Failed to extract IBICallPsRtpRspCb: %d
#E %{private, mask.hash}shandleNotifyIpVersionResp Error  %s
Received reg notification of type %s
#E %{private, mask.hash}sUnable to HANG UP call Id = %u.  No call found.
#E %{private, mask.hash}sfailed to extract ACB indication params
#E %{private, mask.hash}sfailed to initialize ImsClient
#D %{private, mask.hash}sno %s subscription to handle SUBSCRIBE response.  We might have received a terminating NOTIFY first.
#I %{private, mask.hash}sAnalyticsLogger::logLazuliMessageSessionSetup
#E %{private, mask.hash}ssessionDidConfigure session is null
IBISipLogger ICE client started
#D %{private, mask.hash}sall ims dialogs deinitialized
%{private, mask.hash}sapplyMediaSettingsUsingForkIfRequired: updating sdp for session
#E Indication Register request failed: %u (%{public}s)
#W %{private, mask.hash}shandleStopMediaResponse called for non-existent session. ignore it.
%{private, mask.hash}sText session detected, but call is still hidden. Delaying notification
%{private, mask.hash}sImsTcpSocket: No delegate to handle incoming packet from %{public,network:sockaddr}.*P. Discarding packet
Updating state with new registration (%s, %s) with reason %s
#E failed to extract ACB info response params
Config now valid, executing deferred start [sessionId=%llu]
%{private, mask.hash}smedia config has changed, re-initializing RTPManager
%{private, mask.hash}scall ended due to local hangup. Auto-resuming last held call.
Cancel timer sessionId=%llu
#E %{private, mask.hash}scan't accept an invitation when we haven't alerted the user
#E %{private, mask.hash}signoring auth response with unknown source id '%s'
#D %{private, mask.hash}sCall end times: duration %lus time since last recv %lus time since last send %lus inRemoteRtcp=%{BOOL}d local hold %{BOOL}d remote hold %{BOOL}d
Audio is active over RAT: %s
%{private, mask.hash}sisRegistrationRetryAllowed(non-emergency) %{bool}d: Default behavior
#E Failed to extract StartMediaSessionResponse : %d
#E %{private, mask.hash}sPong timeout. Terminating registration
%{private, mask.hash}sHighest procedure is %{public}s for instance %u
%{private, mask.hash}sisVoiceRegistrationBarred: not on LTE
%{private, mask.hash}sattempt %u : starting DNS lookup for %{public}s
terminateSessionWithId [sessionId=%llu]
initialize [sessionId=%llu isMO=%u]
%{private, mask.hash}sCheck if we need to coalesce registration refresh on other stacks
%{private, mask.hash}sSIP call id: %{public}s
#E Chat instance gone for %s
#D Canceling system wake for timer %@ at %{time_t}ld (%lds)
%{private, mask.hash}sdeinitializing sip stack
#E %{private, mask.hash}sUnable to compute hash for algorithm %d
%{private, mask.hash}sclosing UDP transport
%{private, mask.hash}supdated dialog id container, size: %zu
#E %{private, mask.hash}sno local SDP available
#E NULL parser node
%{private, mask.hash}sallowing %s call (barringFactor = %u, rand3 = %u)
#D %{private, mask.hash}sdone with NOTIFY, moving from %s to %s
%{private, mask.hash}semergency stack initialized, but we no longer have a pending emergency call
%{private, mask.hash}sfillContactForServicesAndMethod: AnonymousEmergencyCall: matched mcc=%u, use imsi as contactUser=%s
#D %{private, mask.hash}signoring tlv type %hu size %zu
#E %s%d%s%s
#E %{private, mask.hash}s%{private, mask.hash}s: no response to resend
#E %{private, mask.hash}ssocket already set: %{public,network:sockaddr}.*P ignoring: %{public,network:sockaddr}.*P
%{private, mask.hash}susing public identity %s
%{private, mask.hash}sTransaction timed out when using this connection.
Setting up sockets for %s session [sessionId=%llu]
#E %{private, mask.hash}sHandling invite failure statusCode %u statusText %s remoteUri %s
%{private, mask.hash}sstill waiting for %zu hostnames to resolve
%{private, mask.hash}sReceived message request %s on stack %s
#E %{private, mask.hash}scan't send an INVITE without a call
#E Unable to fetch HTTP Request headers
%{private, mask.hash}soriginal: removing unused connection, resetting connection, and resetOnDelete
There are %zu sessions remaining for stack ID %s
%{private, mask.hash}sinitialized!
#E Unable to create AVC media stream delegate
#E %{private, mask.hash}sIgnoring call end info from CT.  No call being tracked in logger
#D %{private, mask.hash}sSending kIMSCallStatusHoldFailed
#D %{private, mask.hash}sfound %zu subscriber(s) for %{public}s
override: {
#E %{private, mask.hash}scan't send an INVITE in a terminated session
==================== [SID:%llu%{public}s] HTTPS Request %{public}s -----> %{public}s [%{public}s:%u] ====================
%{private, mask.hash}sholding call %{private, mask.hash}s
#E %{private, mask.hash}sSDPSession expired.
#I %{private, mask.hash}srefreshRegistration: setting to policy SipRegClientRegType::RefreshReg
%{private, mask.hash}sNW listener cancelled
    CallId:     %s
#E SDP session not found
%{private, mask.hash}screating temporary inbound SA for local server port
#E %{private, mask.hash}stransactionTerminated. No dialog for this request
%{private, mask.hash}sConnection closed by both sides. 
#I %{private, mask.hash}sStack %s is a Lazuli stack
%{private, mask.hash}salready removed from transport
#D Ignoring duplicate CONNECT call status request on instance %u for media %{public}s and RAT %{public}s
#W %{private, mask.hash}sCall does not own a fork using bearer %u
%{private, mask.hash}sNR TDD <-> FDD: do not removeConnections()
#E %s%s
%{private, mask.hash}sdata received connectionId=%llu
#D %{private, mask.hash}sIgnoring preferred IMPU %s in favor of previously registered public identity %s
Sending %s
%{private, mask.hash}skeeping old retry time
#E Can't end a line with a backslash
%s : unable to match reason protocol (%s != %s)
#D %{private, mask.hash}s%s hung up
%{private, mask.hash}sShutting down, ignore connect error
%{private, mask.hash}sLeave Group trx %s, conv %s, isSuccess: %{bool}d
#W %{private, mask.hash}sreceived fatal registration response. %u more and you're done.
#E %{private, mask.hash}sno security mechanism specified in SecurityServer header
%{private, mask.hash}sswitching user %s to transport %s
#W DTMF with unexpected format parameters parsed: '%s'
%{private, mask.hash}scall count = %zu . We already told baseband we're in a call.
#W Handover timer for sessionId=%llu already exists
#E %{private, mask.hash}sunable to create media session for incoming call: %s
%{private, mask.hash}sdisallowing redial because response code not in silentRedialAllowedResponses
%{private, mask.hash}sshutting down socket
%{private, mask.hash}screated temporary SA pair %s
Session-level direction was: %s setting it to: %s
#D %{private, mask.hash}sThis is an EPS silent redial requiring reregistration.
#D %{private, mask.hash}sstart ANI: %{public}s, current ANI: %{public}s: EPS Fallback happend during the call
#E User agent not available for messageEncoding()
#W %{private, mask.hash}sDid not set bundle UUID
Set RTCP interval for sessionId=%llu to %u
#E %{private, mask.hash}sTransport layer is null 
Did not get a valid Signaling TLV. Trying the Data TLV.
Terminate sessionId=%llu
#E Tried to set PacketizationTime to %u setting it to %u
Config now valid, deferring to SM-queued start [sessionId=%llu]
#W start [sessionId=%llu _direction=%s]
Session initialized [sessionId=%llu]
#E inteface %s path failed!
#E %{private, mask.hash}scan't send an UPDATE in a terminated session
%{private, mask.hash}signoring reported feature tags (%s) and reporting (%s) instead
#I %{private, mask.hash}sMarking NAS initialization complete for stack %{public}s
%{private, mask.hash}sreceived out-of-order response (rseq=%u, expecting %u)
#E SDPMediaCandidate parse error, no priority
#E %{private, mask.hash}sreceived auth response in unexpected state %s
#D %{private, mask.hash}sforcing termination of transaction %s
#I %{private, mask.hash}sencoded message is small enough for UDP (%lu bytes)
#E Unable to set timeout for power assertion %{public}s
#W Unable to set assertion resources for power assertion %{public}s
#E %{private, mask.hash}sRequest timer is being ignored for session termination timing out
configureRemoteRTCP [sessionId=%llu enabled=%u  interval=%u
%{private, mask.hash}sRegistration mode changed to %s
#D %{private, mask.hash}sDisconnected from %s due to %s
#D %{private, mask.hash}sactive fork is now %{private, mask.hash}s
handleStartDTMFCodeResponse RECV: Length: %u, Name: %s
%{private, mask.hash}sHandle incoming connection connectionId=%{uuid}.16P
#W %{private, mask.hash}sInvalid OIP request
Handover completed for %s
#W %{private, mask.hash}stimed out waiting for prerequisites. Continuing.
#E %{private, mask.hash}sCallAudioServiceClient framework not available - skipping audio session properties setup
#W %{private, mask.hash}sImsTcpNw delegate is null
#I %{private, mask.hash}saccess barring is still in effect until %{time_t}ld (%lds)
%{private, mask.hash}shandleBarringAccessAlleviated: no-op: registration is currently not being throttled
%{private, mask.hash}ssendNotifyIpVersionReq
reportHandover [sessionId=%llu]
#E %{private, mask.hash}sNo delegate for refer %s
#W Timer fired as XCAP transaction didn't complete in %u seconds
Media session started successfully, session id : %u
#E %{private, mask.hash}sInvalid digest nonce in push. Unable to skip unauthorized REGISTER
%{private, mask.hash}sreceived INVITE w/ no SDP. Starting new offer/answer exchange so we can send an offer
%{private, mask.hash}snot registered. Continuing with deinitialization. skipDeinitReg=%{BOOL}d
#D %{private, mask.hash}supdated local URI to %s
#S Cleaning up read stream: %p
#I %{private, mask.hash}sIMSCallInfo::handleSessionRequestedEvent during an existing alerting call. Declining.
#D %{private, mask.hash}sDoing ACTIVATE to call Id = %{public}s
%{private, mask.hash}swill drop msg arriving on DefaultSipPort of %s
%{private, mask.hash}s%s : setting MSS for outgoing TCP socket to %d
Dispatching handleTextStreamTokenEvent callback for %s
Forcing start of session %llu
#E Remote media is null
#I %{private, mask.hash}s~SipInsecureTransportGroup: SipTransportLayer is going away
#D %{private, mask.hash}sTransport init success. isPrivateRelayActive=%{BOOL}d
%{private, mask.hash}ssystem clock changed
#E SipStack is null
%{private, mask.hash}sremoving action for invalided call %s
Dispatching prepareToProceed callback for %s
Dispatching handleRegistrationEvent callback for %s: expiration=%u, willRetry=%{bool}d, errorReason=%s, responseCode=%u, regTrxId=%s, retryAfter=%u
    AutoRenew:  %{BOOL}d
#D Received UAC barring alleviation indication from baseband
DTMF digit received: %c
%{private, mask.hash}sTelemetry Identifier created
#I Set xcap queue for write stream
%{private, mask.hash}sskip ping while unregistered
%{private, mask.hash}sDROPPING %s %u response
#E %{private, mask.hash}sincomplete message received:
#D %{private, mask.hash}s[SIM %u]: (*response.mo_data_barring_t4).remaining_timer = %u
#E Via hop missing protocol name: %s
Action: %s
#E %{private, mask.hash}sCan't change media manager while ongoing calls
%{private, mask.hash}shandleStartDTMFCodeResponse [sessionId=%u result=%u]
%{private, mask.hash}sreceived session moved response for initial invite.  Redialing to new URI %s
%{private, mask.hash}swe have a pending Auth Sync response, not resetting Call-ID
#E Instance lost.
#D %{private, mask.hash}ssendPreconditionUpdate: still have outstanding PRACKs in fork %{private, mask.hash}s
%{private, mask.hash}sSending telemetry data to PowerLog
%{private, mask.hash}sInvite needs Geolocation for NormalSetupEmergencyCall
policy interfaces: 
#W %{private, mask.hash}sreceived redirects from all proxies. Resetting PDN.
#I %{private, mask.hash}sSetting up emergency access network: %{public}s
#E didReceiveDTMFEventWithDigit owner is null
Location lookup is NOT enabled (roaming=%{BOOL}d)
#D %{private, mask.hash}shandleQualityOfServiceRevoked: no call found 
#W %{private, mask.hash}sdropping deferred %s
%{private, mask.hash}snot enough data in decodeHeader
  CallManagerEventDelegates:
%{private, mask.hash}sUsing existing CancelReason: %{public}s: %u: %{public}s
#D %{private, mask.hash}supdateNetworkServices: Moving to LTE RAT.  Requesting current barring information.
#E %{private, mask.hash}stransferee and transfer target must both be valid call objects
#D %{private, mask.hash}sEnding conference call
#I %{private, mask.hash}sContinuing call with uuid %{public}s
#E Timer for request %s already exists
#D requesting current ACB info for instance %u
#E updateSdpForSession() got an invalid session id: %llu
IMSSMSManager::getCapabilities
%{private, mask.hash}scancel connectionId=%llu
transactionPending=%u initialized=%u delayedStart=%u
%{private, mask.hash}stimed out waiting for hold to complete
%{private, mask.hash}sIncoming INVITE doesn't support 100rel
#I %{private, mask.hash}sWill%s notify baseband during handleRegistrationStateChanged
#I %{private, mask.hash}shandleBarringAccessAlleviated...
#E %{private, mask.hash}sunable to create outgoing sip URI: %{public}s
%{private, mask.hash}sEncoding SIP message. Is IPAddress anonymized: %{BOOL}d
%{private, mask.hash}sIPT will no longer retry Lazuli registration. CT will retry after %u for regTrxId %s
%{private, mask.hash}sdestroying ImsTcpSocket %p
#E No matching close bracket in URI header: %s
#D Sending Call Status Request to BB
RTP nw_path_evaluator initialized with uuid = %s clientID=%llu
#E %{private, mask.hash}sdialogTerminated called on unknown dialog %s
#E %{private, mask.hash}sunknown remote tag %{public}s
#I %{private, mask.hash}sno ACK received by timeout.  Terminating session.
%{private, mask.hash}sCheck if registration needs to be disabled due to : %s
%{private, mask.hash}ssetRelayMode [stackId=%s sessionId=%llu isRelayMode=%u]
Stack Type: %{public}s
Connectivity: %{bool}d
#D %{private, mask.hash}sUpdating dict from CT
Creating record for [%s], for %s, on slot %s
#I %{private, mask.hash}sassuming our registration was terminated as well
#D %{private, mask.hash}s%{private, mask.hash}s: transitioning to state [%{public}s]
%{private, mask.hash}s  Value           : %u
Deleting ImsXcapClient: %p
#W Sleep not reverted system state returned for power assertion %{public}s
#W Unable to change direction for session [sessionId=%llu]
#D %{private, mask.hash}sIgnore for non-conference call.
%{private, mask.hash}skeeping auth sync failure info in initial registration
Calling setDirection [sessionId=%llu
#E %{private, mask.hash}sUnable to initiate pull call for invalid stack %{public}s
#E %{private, mask.hash}s%{private, mask.hash}s: received Service Unavailable (IMS Outage) response from P-CSCF.  Terminating registration.
%{private, mask.hash}sno provisional response found with CSeq %u
#S %{private, mask.hash}sHas Lazuli headers? %{BOOL}d
#E %u is not a valid SIP status code
#E RTCP Transport is null
selected valid location %lf, %lf
%{private, mask.hash}sSending chunk %u of %u chunkSize %u bytes
#E %{private, mask.hash}ssendRingingNotification called on a confirmed dialog
%{private, mask.hash}sLending SipSession. This call object will return false for isValid()
%{private, mask.hash}swe previously offered mandatory local preconditions
#W %{private, mask.hash}sDid not set required interface
#E No timer found for request %s
Config: preferredCodecRateMode: %d
#E %{private, mask.hash}sReceived null SipBody
#D %{private, mask.hash}sCreated outgoing emergency call handle for %{public}s on stack %{public}s
%{private, mask.hash}supdateServiceMask: new mask is 0. Resending current state to delegate.
#E %{private, mask.hash}sfailed to decode body of type %s:
#E %{private, mask.hash}sdecode failure on start line
  MessageEventDelegates:
#E %{private, mask.hash}sno branch param in Via header
%{private, mask.hash}sno refers available for %s
#E didResume owner is null
#E URI parsed out of order. Must appear after origin: '%c=%s'
%{private, mask.hash}slogSessionConfirmedEvent [appCallId=%u]. QSL not initialized
#E %{private, mask.hash}sAudio settings RX payload type failed sanitization: %u
Start requested on sessionId=%llu when state is %u
#E Couldn't find session for id: %llu
#E No lazuli delegate set for stackId %s
%{private, mask.hash}sWe don't shutdown incoming connection. And we don't reset on delete
#D %{private, mask.hash}sscheme info %s
%{private, mask.hash}ssuppressing call event %s for hidden call %{private, mask.hash}s
#I %{private, mask.hash}sCoalescing Lazuli registration with IMS
%{private, mask.hash}sdeferring error: %s
#E SDP Media format info has unsupported codec type: %s
%{private, mask.hash}snot updating registration state due to barring factor change while in active call
#D %{private, mask.hash}sCall setup delay is %llums reason is %s
#E %{private, mask.hash}sPropagate failure for addParticipant %s
%{private, mask.hash}sCellular to WiFi handover: will send SESSION_FINISHED event to BB
#I %{private, mask.hash}s%{private, mask.hash}s: found P-Asserted-Identity in service route
  State:         %s
%{private, mask.hash}sChecking for pause (local= %s, remote= %s)
%{private, mask.hash}sGot invalidated callback for participant call %{private, mask.hash}s
#I %{private, mask.hash}sseeing if we need to start reg hysteresis timer
#E %{private, mask.hash}salready have offer and answer for transaction %{private, mask.hash}s
Setting Reason header text for %s to %s
%{private, mask.hash}sunheld call %{private, mask.hash}s has no session. Don't need to hold it.
NB codec not present in SDP Media format
%{private, mask.hash}shandleBarringAccessAlleviated: current state is %s: Indication ignored.
#E %{private, mask.hash}sno call manager delegate to handle incoming call
#E %{private, mask.hash}sNo stack for %s. Ignoring device events - %s
#E unable to load IPSec library
%{private, mask.hash}sLeave Group Chat %s on stack %s
%{private, mask.hash}sPreconditions now enabled for fork %{private, mask.hash}s
#W We don't support send only, defaulting to inactive
#I %{private, mask.hash}swe're in the middle of a registration. Not auto-renewing subscription.
Dispatching handleNewInitialRegistration callback for %s
%{private, mask.hash}sreusing existing connection %s for outgoing message
#D %{private, mask.hash}sNo pending refer requests for conversation %s
%{private, mask.hash}shandleAck: received ack for differnt CSeq, ignoring
flavorMask |= AddressFlavorDetached
resolving %s on %s
Local hold: %{bool}d, Remote Hold: %{bool}d
Subscriptions:
#E Could not create RTCP Listener at %{public,network:sockaddr}.*P
%{private, mask.hash}sdelaying registration error notification until all calls have ended
#E %{private, mask.hash}sTTY settings RX payload type failed sanitization: %u
%{private, mask.hash}sSipStackManager::addLazuliParticipants
#E %{private, mask.hash}scancel called on a confirmed session
#D %{private, mask.hash}sreporting active port %hu
#E Failed to configure media session : %u
%{private, mask.hash}sSuccesfully registered audio codec change callback
%{private, mask.hash}sconfig hasn't changed. Not reinitializing.
#E %{private, mask.hash}sunable to resolve proxy %{public}s : %s
Creating new Chat for %s
#E Repeat Times missing information: '%c=%s'
#D Submitted %s
%{private, mask.hash}sRefers complete.  Terminating
#W %{private, mask.hash}sincoming ACK contains SDP, but we aren't expecting any.  Ignoring it.
#I %{private, mask.hash}skilling fork, but not terminating call
#W %{private, mask.hash}stransactionTerminated: unknown transaction %{private, mask.hash}s
#E %{private, mask.hash}s%{private, mask.hash}s: TransactionLayer is gone
%{private, mask.hash}sNot scheduling Reinvite for TTY, since timeout value is configured to 0
DTMF codec for WB not present in SDP Media format
paused() [sessionId=%llu  paused=%u]
%{private, mask.hash}scall termination wasn't local hangup. Not checking for held call to resume.
#E %{private, mask.hash}shandleTimer: NULL conference call
#E %{private, mask.hash}sreceived invalid SDP answer:
#E %{private, mask.hash}sno fork for 183 response
abc reply success!
#E %{private, mask.hash}sEmpty auth queue. Cannot process auth challenge response.
#E Set-intersection for accept-types is empty
#E %{private, mask.hash}ssendReInvite: already have an active INVITE transaction
%{private, mask.hash}sconfigureRTCPLinkMonitorReq [sessionId=%llu]
NAF_ID: %s
#D %{private, mask.hash}sSipDialog::sendQueuedResponseInTransaction
#D %{private, mask.hash}sresending response
#E %{private, mask.hash}sretransmitAck failed: %s
%{private, mask.hash}sreverting offer/answer state after failed session renegotiation
%{private, mask.hash}sUpdating conference server URI to %{public}s
#S %{private, mask.hash}sImsTlsSocket : process data, len = %zu
%{private, mask.hash}sUnsolicited Requests: OFF
#E %{private, mask.hash}shandleInputFrequencyLevelUpdate: No stream found for %llu frequency: %s
%{private, mask.hash}slogSessionRequestedEvent. isEmgr: %{BOOL}d, isEmgrNormal: %{BOOL}d
#E %{private, mask.hash}shandling connect error: %s
#D %{private, mask.hash}sIPTelephonyManager::handleDeviceEvents: KeepAlive wakeup received
%{private, mask.hash}sRetrying OPTIONS request again as recommended by Server
#E %{private, mask.hash}sNo group params for refer %s
#D canceling timer %s (%s-%s)
#E streamDidRTPTimeOut owner is null
Sending Configuration request
%{private, mask.hash}sReg state changed. Is registered?: %{BOOL}d
#E Instance lost. Stack teardown?
#I %{private, mask.hash}sSipSession::forceDeinitialize
%{private, mask.hash}sdeferring BYE until we receive an ACK
#E unable to start timer %s (%s-%s)
%{private, mask.hash}sgot a non-success response (code = %u, category = %d)
%{private, mask.hash}shandling general registration error #%u
#E %{private, mask.hash}sAll participants failed to join, ending the conference call
#E URI has no closing '>': %s
#E %{private, mask.hash}sno session specified
#D %{private, mask.hash}signoring %u response with To: tag that doesn't match any existing fork: %{private, mask.hash}s
%{private, mask.hash}shandleConfigureRTCPReportsResp [sessionId=%llu]
%{private, mask.hash}sAVC AUDIO client successfully created
#W Session or config null during validation
%{private, mask.hash}sno held call to resume
#E %{private, mask.hash}sNo transport layer. Can't add routableLocalAddress
%{private, mask.hash}sSipStack::removeLazuliParticipants
%{private, mask.hash}smessage id: %{public}s
%{private, mask.hash}ssending %u response to %{public}s request in state %{public}s
%{private, mask.hash}sactivateMediaSession (%s): waiting for session to be confirmed
GBA_ME: Ks_Naf = %s
#E %{private, mask.hash}sImsTcpSocket: error %s
#E %{private, mask.hash}sError writing to socket: %u
#D %{private, mask.hash}sperforming block %{public}s
%{private, mask.hash}sincomingRemoteOriginStr = %{public}s
#S %{private, mask.hash}sAllocated new MSRP message - RESPONSE
#D %{private, mask.hash}sretrying subscription using Min-Expires = %u
Audio RX payload type %u
%{private, mask.hash}sUpdated initial location available %lf, %lf
#D %{private, mask.hash}sendCall: CallInfo %{public}s is in a conference call.  Removing participant from call.
  StackEventDelegates:
----- END -----
isWifi: %{bool}d, simInstance: %llu
#E %{private, mask.hash}sservice unavailable
stopRingbackTone Session id mismatch, expecting: %llu Received: %llu
#E %{private, mask.hash}sNo delegate: dropping %zu bytes from %{public,network:sockaddr}.*P
%{private, mask.hash}spassed on to old delegate
#E No client record for stack %s
#I %{private, mask.hash}scouldn't match my contact in notification.  Using the only contact for my AOR: %s
#E Invalid auth header: missing equals at %s
#E %{private, mask.hash}sno dialog to handle SDP answer
#E %{private, mask.hash}scan't send an INVITE without a lazuli session
#W %{private, mask.hash}shandleAccessNetworkChange: no SIP session
%{private, mask.hash}shandleServiceBindResp [instance=%u]
#E %{private, mask.hash}scan't handle multiple 401 responses for the same SAs
Current transactions:
%{private, mask.hash}sset PID to %llu
%{private, mask.hash}ssending data with existing connection using client outbound SPI %u (%x)
#E %{private, mask.hash}sNo sipstack.  Not adding P-ANI to insecure %s
bw=%u, tx=%u, rx=%u
#W %{private, mask.hash}signoring session refresh timeout
#I %{private, mask.hash}sPerforming audit due to %{public}s for carrier %{public}s
%{private, mask.hash}sRemoving cached audio session %llu
#E %{private, mask.hash}srequest is not valid: %s
#W Not enough information to configure with
#D StartImsRegistrationUacCheck response: Status=%d
%{private, mask.hash}sinitialized on %{public,network:sockaddr}.*P
#S %{private, mask.hash}s%{private, mask.hash}s: action isn't initial registration
#I %{private, mask.hash}sreceived CANCEL in a confirmed session. Terminating.
%{private, mask.hash}sNegotiated Cipher : %u
#D %{private, mask.hash}sReceived %s. Expecting continueSendRequest()
#D %{private, mask.hash}sFailing closed
#D %{private, mask.hash}ssendPreconditionUpdate: we still have outstanding response SDP awaiting a PRACK
#W %{private, mask.hash}sI wasn't waiting for hostname resolution for %{public}s
%{private, mask.hash}sstill waiting for emergency registration to complete
%{private, mask.hash}sregistration terminated, but I wasn't waiting for deregistration
#E %{private, mask.hash}sFailed to initialize IMS Xcap Client
#E EVS max-red value out of range: %s
#S Creating BsfServerInfo: %p
#E %{private, mask.hash}sreceived unexpected service unavailable. Ignoring it.
#E transitionToState: no such state %s
#E Failed to extract CreateAudioMediaSessionResponse : %d
#D %{private, mask.hash}sI'm supposed to renew at %{time_t}ld (%lds)
%{private, mask.hash}snot terminating registration due to %s since we have another ongoing call
%{private, mask.hash}sdeferring new registration while registered SMS-only
%{private, mask.hash}susing signaling address for media
#W %{private, mask.hash}signoring %u response with no To: tag
#W %{private, mask.hash}sInvalid type: '%s' should be type of integer, not string
#E %{private, mask.hash}sImsTransferTransferRequestedState::enterState() - transfer handler is null
handleMediaSessionInitialized sessionID=%llu error=%u handoverState=%s _sessionConfigured=%u
  %{public,network:sockaddr}.*P (flavor mask: %u)
#S %{private, mask.hash}sImsTlsSocket : _handleDataAvailable: read %zu bytes
#E %{private, mask.hash}stoo many subsequent redirection requests.
%{private, mask.hash}sImsTlsSocket: Shutdown not supported on a tls socket
#E %{private, mask.hash}ssetLocalAddressFromSocket failed
#E MSRP hops are not allowed in MSRP TLS
%{private, mask.hash}sNo Baseband for architecture or Baseband is currently not available: skip send
#E %{private, mask.hash}sno stack for trx %{public}s
%{private, mask.hash}sstrict call flows are on. Waiting for INVITE response before terminating
%{private, mask.hash}sGrow CRLF ping interval: %u --> %u
%{private, mask.hash}ssetting baseband available as %{BOOL}d
#E unknown SIP timer %s
#E %{private, mask.hash}sController has been deinitialized while waiting for Service Bind response
  Sender identity: %s
dispatch handleLeaveGroupChat for %s
%{private, mask.hash}schoosing actual wait time in range [%u, %u] = %lu s
%{private, mask.hash}slogSmsSendCompletedEvent
#D %{private, mask.hash}sCall to %s requires redial over LTE
#E createAudioSettings Local media is null
%{private, mask.hash}saddSession [sessionId=%u]
%{private, mask.hash}sreceived provisional response to INVITE. Sending pending CANCEL request.
terminate sessionId=%llu
%{private, mask.hash}sMedia settings mismatch: maybe we should update media settings
%{private, mask.hash}sstarted [instance=%u]
conditions: %s
handleConfigureAudioMediaSessionResponse [_mediaSessionId=%u sessionId=%u result=%u]
%{private, mask.hash}sfound active emergency transactions. Renewing emergency registration.
#E %{private, mask.hash}sno tokens in start line
%{private, mask.hash}sCB: Unsolicited Request Support - %{bool}d
#D %{private, mask.hash}sXCAP Request Dictionary: %@
%{private, mask.hash}sReported ANI: %s
%{private, mask.hash}sSipUssdSession::cancelSession: StateTerminated: no op
%{private, mask.hash}sstartAudio
%{private, mask.hash}shandleActiveForkChanged
#S ImsTcpSocket: No more data to read on socket %d
stopping local ringback tone
streamDidRTCPTimeOut
#E %{private, mask.hash}s%s requests aren't supported outside dialogs
#E %{private, mask.hash}s%{private, mask.hash}s: triggering reregistration due to internal timeout
#E %{private, mask.hash}sTransport failure
#W Failed to create SDP media entry for codec type '%s'
%{private, mask.hash}ssending Session Progress to establish QoS before ringing
%{private, mask.hash}swaiting for emergency SIP stack initialization to complete
#E RcsPcscfNw is null
#I Invalid Authorization header: missing realm
#E %{private, mask.hash}sperformPendingTermination: no pending termination reason
#E %{private, mask.hash}sNo other addresses on %s
%{private, mask.hash}sretryRegistration: no delegate
#E Invalid StopDTMFCodeResponse
#E Unable to process status request %{public}s.  No call status started for MT call on instance %u with services %{public}s
%{private, mask.hash}sIPT will no longer retry Lazuli registration. CT will retry.
#D %{private, mask.hash}sNot sending termination event for hidden call
#E %{private, mask.hash}sLazuli manager is null 
#E MessageSession lost for handling incoming message: %s
#E Invalid SDP template string in config
Attempting to evaluate interfaces %s
#E %{private, mask.hash}sregistration failed with SIP response %u
%{private, mask.hash}signoring auth response in state %s
Replacing stack delegate for %s
%{private, mask.hash}scleanup [stackId=%s, deinitialize=%{bool}d]
#E Codec not recognized: %s
 Config: codecType: %s
%{private, mask.hash}sUpdating To Uri to %{public}s
%{private, mask.hash}sInitializing TCP-KeepAlive on %s
Dispatching handleXcapRequestCompletion callback for %s
#S %{private, mask.hash}sdetermining based on transaction
SipRegistrationClient is no longer existing: no op
Send CallEnd event to Audio device
#E %{private, mask.hash}sdecode failure on headers
#E %{private, mask.hash}sNo profile for stack %s
%{private, mask.hash}sAll participants on hold. Start the session.
#D %{private, mask.hash}sTerminating %zu chats on %s
%{private, mask.hash}signoring session refresh transaction error
#W %{private, mask.hash}sexisting registration entries are:
All Dialogs:
%{private, mask.hash}snot doing phone number prefix mapping while roaming
#E %{private, mask.hash}sno last held call to resume
#E %{private, mask.hash}sNEVirtualInterfaceCreate failed
%{private, mask.hash}s~ImsCall()
%{private, mask.hash}screateLazuliSessionTemplate
#E %{private, mask.hash}sUninitialize all sessions request timed out
#E %{private, mask.hash}sNEPolicyCreateSession failed
#D %{private, mask.hash}sMT-only session already established %{public}s old %p vs %p
#E %{private, mask.hash}shandleIncomingSession failed: %s
#E %{private, mask.hash}sInvalid dialogManager
#E handleUnknownResponse
    State:      %s
%{private, mask.hash}semergency SIP stack is already initialized
%{private, mask.hash}snot sending pending INVITE while glare timer is active
Dispatching handleTextMediaDetectedEvent callback for %s
%{private, mask.hash}shandling fatal registration error #%u
Pausing session %llu
dispatch handleGroupChatCreated for %s
#E %{private, mask.hash}sunable to initialize MT dialog: %s
}
%{private, mask.hash}sremote preconditions have already been satisfied
%{private, mask.hash}ssame as original: removing unused connection, resetting connection, and resetOnDelete
#E startRingbackTone will not be playing ringtone, called for session: %llu while the active session is: %llu
%{private, mask.hash}semergency registration is disabled in config
#E %{private, mask.hash}sCan't send a spam report without valid Spam reporting URI
%{private, mask.hash}sSipSession::handleTransactionError
%{private, mask.hash}shandleGeneralErrorFromAllProxies(emergency)...
#E %{private, mask.hash}sunable to initialize outgoing connection
#W %{private, mask.hash}sReceived AccessBarring information is invalid, but letting it through
#D %{private, mask.hash}s%{private, mask.hash}s: resending %s request
#E %{private, mask.hash}sCan't start authenticated registration without a challenge source
#D %{private, mask.hash}s%{public}s
%{private, mask.hash}sNetwork interface changed. Clearing throttling, failure flags and resetting proxy offset.
#D %{private, mask.hash}sunsubscribe completed
%{private, mask.hash}sPort binding timed out after %u ms
#I %{private, mask.hash}s~SipTlsTransportGroup: SipTransportLayer is going away
%{private, mask.hash}sisVoiceRegistrationBarred: access barring is not enabled
%{private, mask.hash}sderegister requested during voice service fallback, dropping registration silently
Sending DTMF digits: %zu
#D %{private, mask.hash}shandleMediaStackSwitchComplete for stack %{public}s
#E Unable to parse %s format parameter for EVS codec
Skipping socket creation for session with 0 port
%{private, mask.hash}ssetting remote offer from %{public}s in transaction %{private, mask.hash}s
#D %{private, mask.hash}sSipSubscription::handleNotification
%{private, mask.hash}sCDIV: Supports Media Tag - %{bool}d
NEPolicyCallback called with itemID %u, notificationType %u
 trx=%s
%{private, mask.hash}s~AVCRTPStackController
content type = %s, content = \n%s
#D %{private, mask.hash}sHandling QoS notification for %{public}s ports: %s
#E Cannot activate session for conv %s trx %s
#W %{private, mask.hash}sfillContactHost: no active transport
#S %{private, mask.hash}sImsTlsSocket : readDataFromStream errSecSuccess
#E %{private, mask.hash}schallenge is null
#W Ignoring didResume notification received for sessionId=%llu
%{private, mask.hash}sUpdating bearer information for fork %{private, mask.hash}s
#W %{private, mask.hash}sImsTlsSocket: kDebugDropIncoming set.  Dropping incoming packet.
#D %{private, mask.hash}sRegistration active using fallback setting PR=%{BOOL}d SD=%{BOOL}d
%{private, mask.hash}screateMessageSession for id: %s
#W %{private, mask.hash}sdialog %s disappeared during deinitialization
%{private, mask.hash}sThe full remote MSRP path doesn't match the negotiated.  Letting it slide because our SDP also doesn't match ;)
Using RTP port %u
#E %{private, mask.hash}sReceived 403 for Group Chat INVITE. Propagating failure and maintaining registration
will update message delegate %s for stack %s to %p
#E Failed to fetch client to handle auth response.
#I %{private, mask.hash}swe are currently in a call.  Allowing additional outgoing call while unregistered.
#D %{private, mask.hash}sBringing up security policies for %{public}s
      %s
#E Unable to generate AKAv2 password
#E %{private, mask.hash}slogMessageMetrics() no stack
%{private, mask.hash}sdelaying registration terminated notification until all calls have ended
#E %{private, mask.hash}s%lu is not a valid proxy offset
Reachability for %{public,network:sockaddr}.*P is (%s)
#E updateOutputFrequencyLevel owner is null
%{private, mask.hash}sinitializing %s registration policy
%{private, mask.hash}shandleBarringAccessAlleviated: actual nextRetryTime=%{time_t}ld (%lds)
#E SipBodyPart::decode: can't find CRLF in headers
**** XCAP REQUEST ****
#E %{private, mask.hash}signoring auth response for invalid user agent %s
itemID=%u notificationType=%u
%{private, mask.hash}s%s%s
Unsubscribing [%s] from %s
----- Store-And-Forward Lazuli Sessions (%zu) -----
#E %{private, mask.hash}sunknown remote tag %{private, mask.hash}s
#D %{private, mask.hash}sLazuli pinned certificate digests: 
#D %{private, mask.hash}sSending kIMSCallStatusResumeFailed
#E %{private, mask.hash}sInvalid auth params: nonce=%s realm=%s algo=%s challenge=%s resp=%s
Skipping NW path creation for media type %s
%{private, mask.hash}shanging up with reason %{public}s
#E %{private, mask.hash}sUnknown session. Can't handle Prack
%{private, mask.hash}shandleConfigureLinkMonitorResp [sessionId=%llu
%{private, mask.hash}sisRegistrationRetryAllowed(emergency) Yes: RequestTimeout, still more proxy to try
%{private, mask.hash}sSending %zu queued bytes to %s
setScreeningMode [sessionId=%llu isScreeningMode=%u]
%{private, mask.hash}s'%s' is a known section
#D %{private, mask.hash}sSending error response %s immediately.
#E Failed to stop DTMF digit : %u
%{private, mask.hash}ssendDTMFReq [sessionId=%llu]
#D %{private, mask.hash}susing P-CSCF list from prefs
  %s%s
#E RTPManager::deactivateSessionWithId could not find session id: %llu
#D %{private, mask.hash}sReceived PAT and Reputation Token callback.  Starting Spam ATHM TokenRequest.
%{private, mask.hash}slogPrackResponse [appCallId=%u]
Cancelling all timers and clearing dtmf queue.
#I %{private, mask.hash}swe're in the middle of a %sregistration. Not auto-renewing subscription.
%{private, mask.hash}sremoveTextSession
#E Session not found [sessionId=%llu]
#E %{private, mask.hash}sError indication for request: %s [error=%d]
%{private, mask.hash}snot registered SMS-only on LTE
Delegates:
%{private, mask.hash}sResume the conference call
#E Message encoding not available from user agent
#E %{private, mask.hash}sDidn't get a client transaction
%{private, mask.hash}sEntering limited connectivity, pending transactions may be terminated
%{private, mask.hash}sNOT using connectivity hysteresis timer.  Hysteresis from Registration will be used?: %{BOOL}d
#D %{private, mask.hash}sSipSubscription::determineIncomingMessageCategory - %s
#E Failed to pause session which owner is null
#E no semicolon in security agreement option %s
#W %{private, mask.hash}sinvalid SDP answer in ACK.  Terminating session.
#D %{private, mask.hash}sCall setup delay was %lums reason is %s
%{private, mask.hash}scheckForHeldParticipants: participant %s is in state %s
#I %{private, mask.hash}sset active transport to %s
%{private, mask.hash}sheld call %{private, mask.hash}s to %s
%{private, mask.hash}sdeferring deregistration while in limited connectivity
Dispatching handlePdnReset callback for %s
%{private, mask.hash}sconversation not found, queueing: %s
#D resetting timer %s to default
RTCP reports: %s
Dispatching handleUssdError callback for %s
%{private, mask.hash}s}
#D %{private, mask.hash}sHandling QoS notification without any ports
#D %{private, mask.hash}schallenge isLazuliEnabled=%d keyRefLength=%zu
#E %{private, mask.hash}sMessage size %llu exceeds MessageMaxSize %u
#E Failed to parse AMR codec with format parameters '%s'
%{private, mask.hash}shandleMediaError [sessionId=%u rtpTimeout=%u rtcpTimeout=%u
%{private, mask.hash}sCall-Info Branded Calling header received [imageUrl=%{public}s companyName=%{public}s]
#E %{private, mask.hash}ssendPrack: no fork with remote tag %{private, mask.hash}s
#E startSipTimer (%s-%s): no SIP timer values specified
#W Invalid remote address in config
#D %{private, mask.hash}sUsing compressed mls blob %zu bytes
#D %{private, mask.hash}sPAT auth init
%{private, mask.hash}sPreconditions satisfied for session for %{private, mask.hash}s
 convid=%s
#E Access Barring Indication Register request failed: %u (%{public}s)
#E %{private, mask.hash}smedia timeout after handover 
#E Chat instance gone for %s / %s / %s
#W %{private, mask.hash}sdropping invalid response
%{private, mask.hash}sdeferring initialization until we've finished previous deinitialize
#W %{private, mask.hash}s%{private, mask.hash}s: Server Timeout response does not contain P-Asserted-Identity
#E %{private, mask.hash}sno delegate to handle incoming answer
fillCommonFields %{public}s : SIP callId len=%zu , IBI ibiCallId.size=%zu
#D %{private, mask.hash}scallend reason is %s
#E %{private, mask.hash}sImsTransferTransferRequestedState::handleTimer() - transfer handler is null
%{private, mask.hash}stransport is already initialized
%{private, mask.hash}sSkip creating text session for %s because RTT is disabled
%s: [No default]
action [sessionId=%llu]
valid() Invalid attribute
%{private, mask.hash}sauth mechanism wasn't AKA; trying to update with NULL keys
%{private, mask.hash}ssendSessionFailed. isEmgr: %{BOOL}d, isEmgrNormal: %{BOOL}d
#D %{private, mask.hash}sIMSCallInfo::handleJoinedConferenceEvent for an unknown call
#E %{private, mask.hash}sCan not start un-initialized participant
%{private, mask.hash}sNo active call to hold
#S Sessions list is empty.
#E Cannot fetch Bootstrapping Key Lifetime from response. Failing request
processDataFromSocket received unexpected data with %zu bytes
   detached
#I %{private, mask.hash}sStack %{public}s is using %{public}s and wants %{public}s
%{private, mask.hash}sstopping timer for %s
Autostart [sessionId=%llu isBasebandInitialized=%u force=%u]
#E %{private, mask.hash}sEmergency call has no emergency options
#E %{private, mask.hash}sno conference server specified
#E _handleSSLWriteCallback failed. NULL context:
Dispatching handleMediaInitializedEvent callback for %s
#E %{private, mask.hash}sno method or status in the message
#W %{private, mask.hash}sno handler for incoming ACK with CSeq %u (maybe a dup?)
%{private, mask.hash}sskipping RTCP conn. connectionId=%llu
%{private, mask.hash}sResponse %u should be reported as RegistrationTerminated
#E %{private, mask.hash}sRegistration moved on.  Dropping tokens
%{private, mask.hash}suninitializeAllSessionsReq [instance=%u]
%{private, mask.hash}sno last access network. Clearing timestamp.
#W %{private, mask.hash}sBarring ignored, non-LTE RAT
setConfiguration [sessionId=%llu]
%s hasn't been resolved
%{private, mask.hash}sretryRegistration: registration already in progress
#E %{private, mask.hash}sbase64 decode error pat challenge: %s size %zu
%{private, mask.hash}sringback timer fired.  Canceling call.
#E %{private, mask.hash}scannot cancel an MT call
#D Scheduling system wake for timer %@ at %{time_t}ld (%lds)
%{private, mask.hash}sWill not start timer to reReg and will not notify CT about retry due to: stack Uninitialized: %{bool}d, RegistrationModeDisabled: %{bool}d, RegistrationModeReprovision: %{bool}d
#W %{private, mask.hash}signoreDuplicateSdp == %{BOOL}d
%{private, mask.hash}sBSF: %s:%u:%s
#E streamDidStop owner is null
%{private, mask.hash}sSSL/TLS handshake done
%{private, mask.hash}stransferring call between %{private, mask.hash}s and %{private, mask.hash}s
#E %{private, mask.hash}svalid() Invalid timing
#D %{private, mask.hash}ssaved deviceId: %{public}s
#D %{private, mask.hash}s rtcp remote SR in
%{private, mask.hash}supdating configd
#D %{private, mask.hash}sPush triggered registration with auth params, but we connected without private relay. Continuing traditional registration
%{private, mask.hash}scancelled connection
%{private, mask.hash}sexitEmergencyState: not in emergency state
%{private, mask.hash}supdating SA with dictionary: %s
#D %{private, mask.hash}ssending queued %u response
#E %{private, mask.hash}shandleConfigureLinkMonitorResp session is null
%{private, mask.hash}sfound crlf response
#S %{private, mask.hash}sMSRP expected endline: %s
#E Handover completed for stack %s  which is not currently being handed over %s
#E Phone number parsed out of order. Must appear after origin: '%c=%s'
#I Invalid Authorization header: missing or invalid nonce
   service continuity address
#E Failed to deserialize Http response
%{private, mask.hash}sincoming dialog info: %s
%s%s%s%u%s
#E %{private, mask.hash}sIMSCallInfo::continueCall not falling back to CS
#E %{private, mask.hash}sNo call %{public}s found for transferee
#E %{private, mask.hash}sUnable to find call %{public}s -- assuming mobile originated.
handleMediaSessionMediaError sessionId=%llu error=%u
%{private, mask.hash}shandling %{public}s request in state %{public}s
#E %{private, mask.hash}sprocessEarlyMediaHeader: Fork not found. Fork tag: %{private, mask.hash}s
%{private, mask.hash}sno existing calls with QoS established
#I %{private, mask.hash}sregistration is blocked until the PDN is reset
%{private, mask.hash}shandleDataReceived decoding %zu bytes (isMTOnly: %{BOOL}d)
%{private, mask.hash}sremote side has mandatory preconditions
#I %{private, mask.hash}sproxy changed, clearing auth info
%{private, mask.hash}sRemote answers no SDP
#E %{private, mask.hash}shandleSessionSetStreamDirectionResp session is null
#E %{private, mask.hash}sInvalid auth params provided. Unable to skip unauthorized REGISTER
#E %{private, mask.hash}sunable to initialize outgoing connection. Connection manager is null
#E %{private, mask.hash}sapplyMediaSettingsUsingForkIfRequired: no local SDP
#E %{private, mask.hash}sImsTcpSocket: Couldn't connect socket to %{public,network:sockaddr}.*P : %s
#D rescheduling timer %s (%s-%s)
#I %{private, mask.hash}ssubscribeToRegEvents: shouldDeferRegistration first
%{private, mask.hash}shandleConferenceNotification
%{private, mask.hash}slocal deregistration requested
#E Unable to process empty conversationId
%{private, mask.hash}semergency registration is still active. Not re-registering.
#D %{private, mask.hash}sSending kIMSCallStatusInactive
%{private, mask.hash}sA transaction timed out when using this connection.  closing connection.
#S %{private, mask.hash}sCurrent buf (%zu bytes): '%s'
Initialized lazuli Group template SDP (%s)
#I %{private, mask.hash}sSip Stack %s deinitialized
Update appId (if appropriate) to : %u
IMSSMSManager::handleIncomingMessage(stackId: %s, sender:%s, body length:%zu)
#E %{private, mask.hash}sEnding conference due to error response
%{private, mask.hash}sproxy is already reachable.  Not monitoring reachability, just throttling next attempt
#D %{private, mask.hash}sConnection is being attempted
#E GetVoiceSystemId request failed: %u (%{public}s)
#D %{private, mask.hash}strigger spam athm tokenrequest generation (sequence=%u. registrationClientSequence=%u)
%{private, mask.hash}sunable to resolve proxy %s
#E %{private, mask.hash}sreceived AKA response from ISIM but don't have any queued challenges
#E %{private, mask.hash}ssessionMediaError session is null
#E Local SDP is null
#E %{private, mask.hash}sno INVITE transaction to cancel
startTimerForDelayedStackSwitch sessionId=%llu timeout=%u
%{private, mask.hash}sserviceBindReq [instance=%u]
#S Matching Realm: %s
#E %{private, mask.hash}sAttestationServiceHelperSigningTimer expired. continueSendRequest with no opaque. seqCnt=%u
#W %{private, mask.hash}sreceived Forbidden with custom warning header %u
#S fromString %s
#E No matching close bracket in route set header: %s
completeDelayedStackSwitch sessionId=%llu direction=%s start?=%u
%{private, mask.hash}sSipRegistrationClient::sendInitialRequest: kept CurrentRegTrxId=%s
%{private, mask.hash}sforcing TLS transport
%s : %s
#E %{private, mask.hash}stimed out sending session refresh.  Terminating session.
#E Unable to decode header: %s: %s
%{private, mask.hash}sretry not allowed: already exhausted proxy attempts for reregistration
%{private, mask.hash}sattempt %u :unable to resolve %{public}s to an address of type %{public}s
#E no sipstack
#E %{private, mask.hash}sRegister request gone.  Moving on.  (dropping tokens)
%{private, mask.hash}swaiting for PRACK to complete before sending precondition update
%{private, mask.hash}sproxy list has changed.
#E %{private, mask.hash}sCallAudioServiceClient framework not available - cannot get daemon PID
#E %{private, mask.hash}sconnection receive error: %dl
Starting session sessionId=%llu
%{private, mask.hash}ssend trx: %{public}s, call-id: %s, recipient: %s, spam-reporting-uri: %s, conv: %s, content len: %zu, spam type: %s, free text len: %zu
%{private, mask.hash}sSupported options: size= %zu {
#I %{private, mask.hash}sAnalyticsLogger::logSipRequest
will update call delegate %s for stack %s to %p
%{private, mask.hash}sNo Location available to add to %{public}s
%{private, mask.hash}sCan not send ping on uninitialized transport
%{private, mask.hash}sEnabled wake on wifi
%{private, mask.hash}shandlePingTimer: INVITE transaction doesn't have an associated transport
%{private, mask.hash}shandleSdpOffer: initializing MT media session
#E %{private, mask.hash}sunable to set P-CNI to %s
%{private, mask.hash}sIBI Stack Controller initialized!
#D %{private, mask.hash}sProcessing push params sequence=%u
#E %{private, mask.hash}sTransferee and transfer target must be valid objects.
%{private, mask.hash}sNot scheduling Reinvite for TTY for MO call
%{private, mask.hash}sno existing network interface
%{private, mask.hash}sresetting registration errors due to event: %s
#W %{private, mask.hash}sunsupported SMS content type %s
#D %{private, mask.hash}shandleDigestAuthChallenge: handling challenge for %{public}s
#W %{private, mask.hash}sUnable to set text mode for call.  No call for UUID %{public}s
#D %{private, mask.hash}sCall %{private, mask.hash}s IMS code %u event reason %s
#E %{private, mask.hash}sNo sipstack
#E %{private, mask.hash}sMessage so far:
#W %{private, mask.hash}sText stream token callback for non-text stream type %s
#E %{private, mask.hash}sremote address for sendData does not match (got %{public,network:sockaddr}.*P, expected %{public,network:sockaddr}.*P or TCP connection to %{public,network:sockaddr}.*P)
Dispatching handleTransferEvent callback for %s
%{private, mask.hash}sLazor key found: %s with value: %{BOOL}d
#W %{private, mask.hash}sno USSD body
#E %{private, mask.hash}sImsTransferWaitingForHoldState::handleParticipantStateChange() - transfer handler is null
#W %{private, mask.hash}sskipped dropping %lu bytes on inactive transport %s
%{private, mask.hash}shandleSessionUninitializeResp [sessionId=%llu qmiSessionId=%u]
%{private, mask.hash}sSipRegistrationClient::sendInitialRequest: updated CurrentRegTrxId=%s, cleared IncomingRegTrxId
%{private, mask.hash}swill try again with the same proxy.
#W %{private, mask.hash}sreceived Forbidden responses from all proxies. Trigger RCS reprovisioning.
%{private, mask.hash}salready in internalDeinitialize
#E %{private, mask.hash}stransaction not provided, using uuid %s
#E %{private, mask.hash}sImsTlsSocket: Could not sent %zu bytes to %{public,network:sockaddr}.*P
%{private, mask.hash}sDROPPING outgoing message to %{public,network:sockaddr}.*P
%{private, mask.hash}sMedia error in RTT session does not lead to a call drop
#W Nothing to parse as time.
#D %{private, mask.hash}sSkipping update to same dictionary
%{private, mask.hash}s%{public}s request failed for incoming call
Generated session config
%{private, mask.hash}sstate change for %{public}s from %{public}s to %{public}s
QMI srvccHandoverFailed sessionId=%s stackId=%s
  Server txns:    %zu
#E Invalid lazuli Group SDP template
#W Cannot fetch transport name/ip - CFReadStreamCopyProperty() failed
%{private, mask.hash}sfillContactForServicesAndMethod: cellular network mcc=%u, mnc=%u
Client record count was %llu and is now %zu
#E %{private, mask.hash}ssessionConfigureReq session is null
Router Server: (0x0)
#E %{private, mask.hash}sReturning deregistered state due to uninitialized registration client
#E %{private, mask.hash}sUnable to start pending call %{public}s
#I %{private, mask.hash}snew services = %s
  MO/MT:           MO=%{BOOL}d
    Event:      %s
#W ignoring timer with no timer information
#E Failed to set stream property on read stream: kCFStreamPropertyAccountIdentifier
%{private, mask.hash}sSipUssdSession::cancelSession: StateUnconfirmed: sendBye...
#E Auth client gone for signed digest
```
