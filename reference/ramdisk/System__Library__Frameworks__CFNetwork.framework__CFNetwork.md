# `/System/Library/Frameworks/CFNetwork.framework/CFNetwork`

From the upgrade restore ramdisk (141-29011-104.dmg). 6,652,352 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 58 (Size: 5744)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (16)

- `/System/Library/Frameworks/CFNetwork.framework/CFNetwork (compatibility version 1.0.0, current version 3896.200.61)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration (compatibility version 1.0.0, current version 1453.40.1)`
- `/usr/lib/libapple_nghttp2.dylib (compatibility version 1.0.0, current version 1.69.0)`
- `/usr/lib/libcompression.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libicucore.A.dylib (compatibility version 1.0.0, current version 78.1.0)`
- `/usr/lib/libsqlite3.dylib (compatibility version 9.0.0, current version 408.0.0)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/System/Library/Frameworks/CoreServices.framework/CoreServices (compatibility version 1.0.0, current version 1226.0.0, upward)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8, upward)`
- `/System/Library/Frameworks/Network.framework/Network (compatibility version 1.0.0, current version 6681.52.4, upward)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (153 classes, 36 protocols)

Classes: `AVAssetDownloadTask`, `AVAssetDownloadURLSession`, `CFNetworkTimer`, `CONNECTION_SessionTask`, `NSAboutURLProtocol`, `NSCachedURLResponse`, `NSCachedURLResponseInternal`, `NSGZipDecoder`, `NSHTTPCookie`, `NSHTTPCookie2`, `NSHTTPCookie2Key`, `NSHTTPCookie2LookupFilter`, `NSHTTPCookie2Storage`, `NSHTTPCookie2StorageFilter`, `NSHTTPCookieInternal`, `NSHTTPCookieInternal_Data`, `NSHTTPCookieInternal_Ref`, `NSHTTPCookieStorage`, `NSHTTPCookieStorageInternal`, `NSHTTPCookieStorageToCookie2Storage`, `NSHTTPCookieStorageUtils`, `NSHTTPURLRequestParameters`, `NSHTTPURLResponse`, `NSHTTPURLResponseInternal`, `NSHost`, `NSMemoryHTTPCookie2Storage`, `NSMutableHTTPCookie2`, `NSMutableURLRequest`, `NSNetService`, `NSNetServiceBrowser`, `NSNetServicesInternal`, `NSPersistentHTTPCookie2Storage`, `NSProxyConnection`, `NSProxyConnectionStreamTask`, `NSURLAuthenticationChallenge`, `NSURLAuthenticationChallengeInternal`, `NSURLCache`, `NSURLCacheInternal`, `NSURLConnection`, `NSURLConnectionInternal`, `NSURLConnectionInternalConnection`, `NSURLCredential`, `NSURLCredentialStorage`, `NSURLDownload`, `NSURLDownloadInternal`, `NSURLProtectionSpace`, `NSURLProtocol`, `NSURLProtocolInternal`, `NSURLRequest`, `NSURLRequestInternal`, `NSURLResponse`, `NSURLResponseInternal`, `NSURLSession`, `NSURLSessionAVAggregateAssetDownloadTask`, `NSURLSessionAVAssetDownloadTask`, `NSURLSessionConfiguration`, `NSURLSessionDataTask`, `NSURLSessionDownloadTask`, `NSURLSessionEffectiveConfiguration`, `NSURLSessionMutableEffectiveConfiguration`, `NSURLSessionStreamTask`, `NSURLSessionTask`, `NSURLSessionTaskBackgroundHTTPAuthenticator`, `NSURLSessionTaskDependency`, `NSURLSessionTaskDependencyDescription`, `NSURLSessionTaskDependencyTree`, `NSURLSessionTaskHTTPAuthenticator`, `NSURLSessionTaskLocalHTTPAuthenticator`, `NSURLSessionTaskMetrics`, `NSURLSessionTaskTransactionMetrics`, `NSURLSessionUploadTask`, `NSURLSessionWebSocketMessage`, `NSURLSessionWebSocketTask`, `NSURLStorageURLCacheDB`, `NWStreamPair`, `_NSCFServer`, `_NSCFSocksProxy`, `_NSCFTranslatedFileURLProtocol`, `_NSCFTranslatedFileURLProtocol_PIMPL_0`, `_NSCFTranslatedFileURLProtocol_PIMPL_1`, `_NSCFTranslatedFileURLProtocol_PIMPL_2`, `_NSCFTranslatedFileURLProtocol_PIMPL_3`, `_NSCFTranslatedFileURLProtocol_PIMPL_4`, `_NSCFTranslatedFileURLProtocol_PIMPL_5`, `_NSCFTranslatedFileURLProtocol_PIMPL_6`, `_NSCFTranslatedFileURLProtocol_PIMPL_7`, `_NSCFURLProtocol`, `_NSCFWikipediaProtocol`, `_NSHSTSStorage`, `_NSHTTPAlternativeServiceEntry`, `_NSHTTPAlternativeServicesClearEntry`, `_NSHTTPAlternativeServicesFilter`, `_NSHTTPAlternativeServicesStorage`, `_NSHTTPAlternativeServicesStorageSqlite`, `_NSHTTPConnectionInfo`, `_NSNetServiceWeakObject`, `_NSURLAppSSOProtocol`, `_NSURLDataProtocol`, `_NSURLFTPProtocol`, `_NSURLFileProtocol`, `_NSURLHTTPProtocol`, `_NSURLSessionBackgroundTaskOverrides`, `__CFNCoreLoggable`, `__CFN_CoalescingDomainHolder`, `__CFN_ConnectionContextManager`, `__CFN_ConnectionMetrics`, `__CFN_CoreSchedulingSetRunnable`, `__CFN_PathPolicyManager`, `__CFN_SocksHandshake`, `__CFN_SocksHandshakev5`, `__CFN_TaskMetrics`, `__CFN_TransactionMetrics`, `__NSCFBackgroundAVAggregateAssetDownloadTask`, `__NSCFBackgroundAVAggregateAssetDownloadTaskNoChildTask`, `__NSCFBackgroundAVAssetDownloadTask`, `__NSCFBackgroundDataTask`, `__NSCFBackgroundDownloadTask`, `__NSCFBackgroundSessionTask`, `__NSCFBackgroundUploadTask`, `__NSCFDeallocBomb`, `__NSCFLocalDataTask`, `__NSCFLocalDownloadFile`, `__NSCFLocalDownloadTask`, `__NSCFLocalSessionTask`, `__NSCFLocalUploadTask`, `__NSCFMemoryHTTPCookieStorage`, `__NSCFMemoryURLCredentialStorage`, `__NSCFResumableUploadState`, `__NSCFTCPIOStreamTask`, `__NSCFTCPIO_BlockCallbacks_Referent`, `__NSCFTaskForClass`, `__NSCFURLLocalSessionConnection`, `__NSCFURLLocalStreamTask`, `__NSCFURLLocalStreamTaskFromDataTask`, `__NSCFURLLocalStreamTaskFromDataTaskDataBlobby`, `__NSCFURLLocalStreamTaskWork`, `__NSCFURLLocalStreamTaskWorkBlockOp`, `__NSCFURLLocalStreamTaskWorkRead`, `__NSCFURLLocalStreamTaskWorkWrite`, `__NSCFURLLocalTCPIOStreamTaskFromDataTask`, `__NSCFURLProtocolClient_NS`, `__NSCFURLProxySessionConnection`, `__NSCFURLSessionConnection`, `__NSCFURLSessionDelegateWrapper`, `__NSCFURLSessionTaskGroup`, `__NSCFURLSessionTaskInfo`, `__NSCFURLSessionXPC`, `__NSHostExtraIvars`, `__NSURLAVBackgroundSession`, `__NSURLBackgroundSession`, `__NSURLSessionLocal`, `__NSURLSessionStatistics`, `__NSURLSessionWebSocketTask`

Protocols: `AVAssetDownloadDelegate`, `AVAssetDownloadDelegatePrivate`, `AuthBrokerQuery`, `NDBackgroundSessionClient`, `NDBackgroundSessionManagerProtocol`, `NDBackgroundSessionProtocol`, `NSCoding`, `NSCopying`, `NSInternalHTTPCookie2Storage`, `NSMutableCopying`, `NSObject`, `NSProgressReporting`, `NSProxyConnectionDelegate`, `NSSecureCoding`, `NSStreamDelegate`, `NSURLAuthenticationChallengeSender`, `NSURLConnectionRequired`, `NSURLDownloadDecoder`, `NSURLProtocolClient`, `NSURLSessionDataDelegate`, `NSURLSessionDataDelegatePrivate`, `NSURLSessionDataTaskSubclass`, `NSURLSessionDelegate`, `NSURLSessionDelegate_Internal`, `NSURLSessionDownloadTaskSubclass`, `NSURLSessionStreamDelegate`, `NSURLSessionSubclass`, `NSURLSessionTaskDelegate`, `NSURLSessionTaskDelegatePrivate`, `NSURLSessionTaskSubclass`, `NSURLSessionUploadTaskSubclass`, `_CFNWebKitSecureCoding`, `__CFNCoreLoggableReq`, `__NSCFLocalDownloadFileOpener`, `__NSCFURLSessionConnectionDelegate`, `__NSURLSessionTaskGroupForConfiguration`

## Strings (9,282)

First 2,500 of 9,282.
```
_resourceTimeout == NULL
localhost
Err-1206
206
_nscfBridgeURLCacheRemoveAllCachedResponses
v20@?0i8Q12
March
See Other
False
DNS lookup error
Err-3002
v28@?0B8{?=qi}12
-[__NSCFURLLocalStreamTask _onqueue_ioTick]
_delegate_didStopBuffering
DELETE FROM alt_services WHERE host LIKE ('%' || ?) OR partition LIKE ('%' || ?)
oct
Err-1203
v16@?0^{__CFReadStream=}8
v40@?0{shared_ptr<HTTPResponseMessage>=^{HTTPResponseMessage}^{__shared_weak_count}}8{?=qi}24
-[NWStreamPair _onqueue_readToBuffer:length:outError:outEOF:]
file:
\tfAuthConns(%ld) = {\n
AcceptPolicy
%#?:;/@=&[]
com.apple.CFNetwork.Instruments
temporarily redirected
v20@?0^{__CFArray=}8B16
<undecided>
:status
%@ data [ %d ] bytes {\n
lsqpack_enc_enc_str
no host header
kCFStreamPropertyFTPFetchResourceInfo
_waitingBodySize > 0
h3connection
{%d.%d.%d.%d:%d}%@
AddCookies Continue
-[__NSCFURLLocalStreamTask _onqueue_addBlockOpAtHead:description:]
(_state == State::WaitingToEnqueue) || (_state == State::Canceled) || (_state == State::Error)
__delegate_identifier__:Performance Diagnostics__:::____message__:
cannot parse response
*/*
CFHTTPCookieStorage
NSURLSessionTaskStateCanceling
_expiredDNSBehavior
sendDidFail called with NULL err, request: %@
HTTP2Connection<%p>
HTTPS Proxy
_kCFNetworkErrorConditionalRequestKey
LocalWebSocketTask.mm
no-cache
TimeoutActionTurnOff
NSURLSessionSourceApplicationBundleIdentifierIsExternal
kCFStreamPropertyFTPAttemptPersistentConnection
qdec: debug: 
Connection Failed
Viable
Err-1001
writeDBwithCachedResponse-ERROR: bind of partition value for item: %@
%25
v24@?0q8@\"NSURLRequest\"16
r^{CompactCookieArray=^^?^^?^{__CFData}}332@?0{DomainAndPartition=^^?{CFAbsoluteTimeAsSpecified=Cd}[256C]*Q***}8C328
taskDescription
moved permanently
requested range not satisfiable
handleFrame
LiteSpeed
_streamInitialized
NDRemoteHostKey
Created
kCFProxyAutoConfigurationURLKey
<_NSHTTPAlternativeServiceEntry> {\n \t\t\tHost = %@ \n \t\t\tPort = %ld \n \t\t\tPartition = %@ \n \t\t\tAlternate-Host = %@ \n \t\t\tAlternate-Port = %ld \n \t\t\tExpiration = %@ \n} 
requestPriority
Proxy Error
\tcreated:%@\n
%s errno %d cferror %@ ep %s line %d path %s
_CFURLConnectionSetFrameworkStubs
background_session_bgst
fClientCertChallenge == nullptr
_respectsAllowsCellularAccessForDiscretionaryTasks
null
NO
HTTP2Connection
NSURLDownloadOriginatingURLString
Err-1016
_delegate_willCacheResponse
ClientHello
EEA_NONE == prog.ep_enc_action
com.apple.avfoundation.assetdownload.foregroundonly.
taskMetrics2
GZip
kCFURLConnectionSuspensionThreshold
ERROR: unable to get the receiver data from the DB!
ERROR: NSURLStorageURLCacheDB deleteAllResponses: dbConnection=%p DB=%@ Truncate Database failed:%s ErrCode: %d.
LIST\r\n
consumedSize == dataSize
rl = %@, performCount = %lld
NSErrorClientCertificateChainKey
OPTIONS
Non-Authoritative Information
100
HTTP2Server.hpp
NAMESERVER_DOWN
Jan
Ephemeral %@
_onqueue_rdar53306264_addWaiter
HTTP2MetaNetStreamInfoForwarder
newTubeReady
_kCFNTimingDataResponseStart
%s@%@
;
websocket
(unsigned) (p - dst) == len_size + enc_size_bytes
STAT %@\r\n
NSURLDownloadURL
writing
_changeState
charset=
AppleCFNetworkDiagnosticLogging
Client Cert Requested
com.apple.CFNetwork.StreamTaskConnection
INSERT into cfurl_cache_receiver_data (entry_ID, isDataOnFS, receiver_data) \t\t\t\t\t\t\t\t\t VALUES (%q, %q, %q);
kConditionalConnectionRequirementTimeWindowDuration
Prepare Transmission
*buffer
kCFSOCKSVersionKey
_NSDataType
kConditionalConnectionRequirementWorkload
SAwaitingTube.cpp
-
%s:%d
CFHTTPAuthentication
NSURLSession
HTTPServerConnection.cpp
%@: 
ProxyAutoConfigJavaScript
v24@?0@\"NSObject<OS_tcp_connection>\"8@\"NSObject<OS_dispatch_queue>\"16
UNEXPECTED: close of sql read connection result=%d
persistent
nw_activityUUID
H
com.apple.NSURLSession.streamTask_work
!_outCB
qenc_add_to_risked_list
NDBackgroundSessionManagerRestoredStateKeyTasks
November
httprequest
Unviable
SENT
%@ %@\n
_kCFNTimingDataConnectionUUID
ICI=0 is an error
%@://%@:%d%c%@
CREATE TABLE IF NOT EXISTS alt_services (\t\tpartition text NOT NULL,\t\thost text NOT NULL,\t\talternateHost text NOT NULL,\t\tport int NOT NULL,\t\talternatePort int NOT NULL,\t\ttype int NOT NULL,\t\tcreation_time int,\t\texpires_time in
%s\n--\n%s--\n
kCFFTPResourceGroup
unlink
connCache != NULL
could not find header block to continue reading
ETA_NEW
<META 
get-task-allow
_createEndpoint
Event
SELECT * from cfurl_vary_state where request_key=\"
ConditionalConnectionSIMSupport.cpp
Tube.cpp
Session Cookies
_connectionCacheCellPurgeTimeout
Fetching Account for domain
<%p client=%p request=%@>
entry == STAILQ_FIRST(&enc->qpe_buckets[buckno].by_name)
qdec_header_process
v64@?0{shared_ptr<HTTPResponseMessage>=^{HTTPResponseMessage}^{__shared_weak_count}}8@24{?=qi}32q48q56
_disablesUseOfProxySession
Err-1205.w
posixErrorCode != 0
writeDBwithCachedResponse-ERROR: bind of hash for item: %@
v24@?0{shared_ptr<HTTPResponseMessage>=^{HTTPResponseMessage}^{__shared_weak_count}}8
age
writeFrame
DELETE from %s WHERE entry_ID in (%s)
%s [%d] @ %p, version %2.2x, length %d (0x%x)
\xff\xdf\xdf\xdf\xdf\xdf\xdf\xff
v56@?0{FrameMetadata=QQQ}8@\"NSObject<OS_dispatch_data>\"32{?=qi}40
Basic %@
v28@?0{?=qi}8B24
_nscfBridgeURLCacheRemoveCachedResponseForRequest:
_NSURLErrorNWPathKey
bad_weak_ptr was thrown in -fno-exceptions mode
_delegate_connectionWaiting
DiskCookieStorage Checking
.^filecookies^
_neTrackerTCCResult
_batchedStreamData.size() == 0
MIMEType
fd
HTTP2ConnectionCacheEntry(@%p, key=%s)
%@:%@
INSERT OR REPLACE INTO cookies(name, value, domain, path, partition,is_secure,     is_hostOnly, is_httpOnly, same_site, creation_time, expires_time, last_access_time)     values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
com.apple.CFNetwork.LoaderRL
ConnectionReadAggregator.mm
Handshake failure
code
v36@?0@\"NSObject<OS_dispatch_data>\"8{?=qi}16B32
v16@?0@\"NSArray\"8
NSURLSessionResumeInfoVersion
v32@?0@\"NSURLResponse\"8^{__CFData=}16^{__CFError=}24
Better Route Detected
B16@?0@\"NSObject<OS_nw_resolution_report>\"8
You do not have permission to access the requested resource.
Cannot remove file
Persistent Cookies
kCFHTTPServerRequestHeaderValues
WHAT: %p
_delegate_willSendRequestForEstablishedConnection
-[NWStreamPair dealloc]
get_dst
STubeManager
__nsurlauthenticationchallenge_proto_plist
true
workQueue
_pendingResponseBytes == nil
I
ERROR: failed to get the path to the FS cached data at %@
__CFNetworkCopyProxiesForAutoConfigurationScript_privatemode__
kNetworkProxyAuthorizationElementsKeyClientDescription
_state == State::ReceivingResponse
SocketStream %p
_kTCPKeepAliveParametersInterval
prepareTransmission
text/plain
diskcookies
redirected
CFURLRequestSetHTTPCookieStorageAcceptPolicy_block_invoke
password
(null)
Ephemeral sessions must use ephemeral HSTS storage.
1.2.12
{ fd %d }
! _isSharedSession_ivar
v24@?0I8I12@?<v@?@\"NSObject<OS_dispatch_data>\"B{?=qi}>16
SELECT * from cookies
created
Connection Established
__Secure-
set-cookie
error %d resolving %s address for socket %d
constrained
guarantee_out_bytes
Oct
__kCFStreamPropertyNWProxyConfigurationBlock
Payment Required
!_inResponseAssociatedRequest
privateloader
post
There was a problem communicating with the secure web proxy server (HTTPS).
%@ username=\"%@\", realm=\"%@\", nonce=\"%@\", uri=\"%@\", response=\"%@\"
Time from last  dirty
+[NSNetService dictionaryFromTXTRecordData:
_kCFNTimingDataNStatWifiRXPackets
apache
sourceApplicationBundleIdentifier
_kCFNTimingDataConnectionPeerAddress
_kCFStreamErrorDomainKey
kConditionalConnectionInTransitionalDiscretionaryPeriod
yes
Non-descript-key
v32@?0Q8{?=qi}16
SocketStream watchdog timer fired after %f seconds of inactivity. Timing out the connection.
NSURLAuthenticationMethodXMobileMeAuthToken
TCP Connection Failed
Cookie URL
v24@?0^{gss_OID_desc_struct=I^v}8^{gss_cred_id_t_desc_struct=}16
en
''
Version
com.apple.
AVAssetDownloadToken
CFNetDiagnosticCreateBasic
AVAssetDownloadTaskDestinationURLKey
}\n
kNetworkProxyCredentialKeyCredential
%@ (%@)
ERROR: NSURLStorageURLCacheDB _setDBSchema: DB=%@ receiver_data recreate - %s. ErrCode: %d.
v32@?0{shared_ptr<NetworkProxy>=^{NetworkProxy}^{__shared_weak_count}}8^{__CFDictionary=}24
Default
INIT-FAIL: _sqlInsertStmtResponse=%p, DB=%@, error-code:%d.
GET
NOTE: CFURLConnection needDataBuffer no longer supported
CountOfBytesClientExpectsToSend
kCFURLProtectionSpaceKeyAuthenticationScheme
HostLookup
Attempted to set the shared cookie storage after it has already been faulted in!
1; mode=block
NDMethodKey
\tPriority Level [%ld]: RequestQueue(%p) Requests(%ld)
lax
_nscfBridgeURLCacheMemoryCapacity
Err-1202.w
CFHTTPMessage
Did Fail
HTTPHeaderDict
\t\t%d: %p ,\n
TransportConnection
B32@?0@\"NSObject<OS_nw_protocol_definition>\"8Q16Q24
ERROR: NSURLStorageURLCacheDB deleteResponsesSinceDate: dbConnection=%p DB=%@ Delete failed:%s ErrCode: %d.
sessionID
Continue
com.apple.cfnetwork.AuthBrokerAgent
STubeManager.cpp
_kCFNTimingDataNStatWiredRXPackets
%u
_kCFStreamStatsConnectionEstablishmentTimeMs
_minLen == 0 && _maxLen == 0 && _timeout == 0.0 && _cb == nullptr
<read side %p to stream %p>
HTTPMaximumConnectionsPerHost
bad URL
Cannot open file
kCFFTPResourceModDate
_taskUUID
Err-996
AppSSO chose not to manage url
_timerState == TimerState::NotSet
Task delegate is not supported on background session task
writeDBwithCachedResponse-ERROR: bind of 0 partition value for item: %@
%.2x
Tube
NTLM
cloudflare
no original request
readFileToCookies
negotiatedTLSProtocolVersion
_owner == nil
continue
_pendingData == nullptr
%@ connection to %@:%d <%@ proxy to %@:%d>
permanent
0123456789abcdef
\t[%ld]: Tube(%p) - Waiter(%p) Client(%p) Request(%p, %@) Auth(%@)
kCFProxyAutoConfigurationJavaScriptKey
v60@?0B8{shared_ptr<__SecTrust>=^{__SecTrust}^{__shared_weak_count}}12{shared_ptr<const __CFArray>=^{__CFArray}^{__shared_weak_count}}28{?=qi}44
a
<HSTSPolicy@%p <%p>> { HSTSCache=%p }
cannot generate Cancel Stream instruction for stream %llu; buf size=%zu
Invalid stream ID %llu in Cancel Stream
com.apple.nsurlsessiond-events
%@/%s/%@
CopyCredentials
%c
%@/%@
i != -1
_processResponse
-[NSGZipDecoder decodeData:]
HTTP2ConnectionCacheEntry.cpp
header_out_write_value
AVAssetDownloadURLSession does not support NSURLSessionDataTask
<NetConnection@%p> { State = %s, Count = %d, requests = {
 \t\r\n
wait
_decodedHeader
__nsurlrequest_proto_prop_obj_28
com.apple.cfnetwork.httpserver-connection-queue
_tlsProcessValidateServerTrust_Invoke
<A 
corrupt?
SAwaitingTube.h
NSURLAuthenticationMethodHTMLForm
ExceptionsList
SELECT * from alt_services WHERE host = ? AND partition = ? AND port = ? AND expires_time > strftime('%s','now')
kCFProxyTypeNone
waiterTube
B24@?0r*8Q16
^v16@?0^{__CFReadStream=}8
kCFHTTPAuthenticationAccountDomain
cannot decode raw data
_sourceApplicationBundleIdentifier
cancel
completed
%@://%@:%d/
\r\n
coalescingConnectionKeyForHostWithDNSRecord
\tisSecure:%@\n
__nsurlrequest_proto_prop_obj_25
CopyDefaultCredential
_nscfBridgeURLCacheSetDiskCapacity:
getifaddrs
timeout
CountOfBytesClientExpectsToReceive
Cannot create an NSURLSessionAVAssetDownloadTask in a non-background session
CREATE TRIGGER IF NOT EXISTS cfurl_vary_state_delete AFTER INSERT ON cfurl_vary_state WHEN (select count(*) from cfurl_vary_state)>16384\nBEGIN\nDELETE FROM cfurl_vary_state where request_key NOT IN (SELECT request_key from cfurl_vary_state
time
non-authoritative information
com.apple.CFNetwork.HTTP3ServerProtocolViolation
uploading
personaUniqueString
createTime
CantOpen
v16@?0@\"NSObject<OS_nw_data_transfer_report>\"8
qenc_effective_fill
com.apple.nsurlsessiond.started
__kCFStreamPropertyCoalescingDomainSSLSettings
Disk Mod
Unsupported extension
enablesEarlyData
icmp
T *ClientContextHolder<CFURLDownloadClient>::forget() [T = CFURLDownloadClient]
ERROR: unable to allocate receiver data.
SessionIdentifier
bufContainer
v16@?0@\"NSObject<OS_nw_protocol_options>\"8
CFNETWORK_BOGUS_URL
APSRelayTopic
kConditionalConnectionClientOptInDiscretionary
EPSV\r\n
<CFNetService %p>{domain=%@, type=%@, name=%@, specific=%@, addresses=%@}
The certificate for this server has expired.
v16@?0@\"NSURLSessionConfiguration\"8
method
$archiver
%@,%@
Revalidated Cache
com.apple.CFNetwork.CustomProtocols
_received
establishmentReport
ServerHelloDone
uploadFile
v16@?0^{_CFCachedURLResponse={__CFRuntimeBase=QAQ}^{__CFCachedURLResponse}}8
blocked
TYPE I\r\n
The certificate for this server was signed by an unknown certifying authority.
count
Data
T
prefixBufferSize >= 0
shared_tcpConnWorkQueue
ERROR: NSURLStorageURLCacheDB deleteResponsesSinceDate: dbConnection=%p DB=%@ Vacuum failed:%s ErrCode: %d.
kCFURLStorageSessionAppIdentifier
com.apple.private.cfnetwork.har-capture-amp
could not find stream to cancel
NSUnbufferedIO
COMMIT TRANSACTION;
_timeout > 0.0
com.apple.system.config.proxy_change
PRAGMA incremental_vacuum(500);
WhatToDo
Gateway Time-out
%@:%@:%@
_sourceApplicationSecondaryIdentifier
_shouldSkipPreferredClientCertificateLookup
Custom subclasses of NSURLRequest are not supported in background sessions. Attempted to use a request of class %@
## Message %d (0x%x) length %d (0x%x) invalid - encrypted?
CFURLProtocol.mm
<HEAD 
NSExceptionMinimumTLSVersion
com.apple.CFNetwork
DELETE from cfurl_cache_receiver_data WHERE entry_ID=%s;
v24@?0Q8@\"NSError\"16
CFURLDataDecoder
NewStateState
AVAssetVariant
__nsurlrequest_proto_prop_obj_1
NSURLDownloadBinHexResourceForkBytesRemaining
Name: %@, Persistence: %s
com.apple.WebKit
Unexpected message
_timingDataOptions
read_ctx->hbrc_out.xhdr->val_len >= off
Condtional Requirements Changed
got %zu bytes of decoder stream
access-control-allow-origin
script-src 'none'; object-src 'none'; base-uri 'none'
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-_[]:
Write Count
%s %s continuation
_kCFNTimingDataConnectStart
May
allowsUCA
base64
v24@?0^{__CFDictionary=}8^{__CFDictionary=}16
resourceForkData
wss
_CFURLCache
_nscfBridgeURLCacheCurrentMemoryUsage
Bearer %@
username
!_filename
NSURLSessionTask %p
_signalEstablished
_cb
h2 flgs
-[_NSCFWikipediaProtocol initWithRequest:cachedResponse:client:]
kConditionalConnectionRequirementPowerPluggedIn
%@-%ld
_connectionCachePurgeTimeout
download
complete
<CFURLConnection %p> { request = %@ }
Err-1205
opportunistic
URLConnectionClient.cpp
_delegate_needNewBodyStream
serverIPAddress
MetaConnectionCache<%p>
incorporate
PreventUserIdleSystemSleep
Err311
Cannot create file
completeTime
listener-queue
pass
NSTemporaryThirdPartyExceptionRequiresForwardSecrecy
@\"NSObject<OS_nw_object>\"28@?0I8^{nw_protocol_identifier=[32c]ii}12^i20
_TCPAdaptiveReadTimeout
%@/Cache.db
websocketCloseWithCodeAndReason
bytes in: %u; bytes out: %u, ratio: %.3f
value1 && value2
error
v32@?0^{__CFData=}8^{_CFURLResponse=}16^{__CFError=}24
_customReadBufferSize
Err-1010
source was canceled
request
com.apple.NetworkDiagnostics.notification
type
A server with the specified hostname could not be found.
com.apple.CFNetwork.Connection
<SegmentedData@%p> { %ld bytes in %ld segments }
_chunkedWriteTrailer
Wrapping TransportConnection(%p)
ACK
NSURLSessionDelegateImplementsTaskAuthChallengeKey
got more than 8 bytes of trailer, %ld
302
NSIncludesSubdomains
valu
effectiveTrafficClass
\tfQueues[%d] (%ld) = {\n
_kCFHTTPCookiePolicyPropertySiteForCookies
read stream error { %ld, %d }
_initialTubeWidthPlaceholder == 1
_loaderEvent_AckBytes
negotiatedTLSCipherSuite
uniqueTaskIdentifier
_callbacks->start != NULL
server
kNSNetServiceBrowserIncludesAWDLKey
, 
__nsurlrequest_proto_prop_obj_17
Waiting for Accounts
via
Did Timeout
har-path-denial-list
DynamicStackTracing
kCFStreamPropertyFTPProxyPassword
auth challenge
explicitContentType
text
HTTP3ConnectionCacheEntry.mm
unknown
bad_optional_access was thrown in -fno-exceptions mode
HTTP Transactions
--
Local Cache
3
+[NSURLConnection(Deprecated) _setMIMETypesWithNoSizeLimit:]
InProgress
ERROR: encoding user-info failed. Error:%@
_backgroundSessionForPrivilegedDaemon
allowsConstrainedNetworkAccess
CFNETWORK_IO_LOG_STDERR
initial
NSKeyedArchiveRootObjectKey
<%@%p state %s, pending %d { %@ }>
NSURLConnection-%d
httpMessage
keeping alive
Referer
Download
ERROR: NSURLStorageURLCacheDB _setDBSchema: DB=%@ table index on blob_data - %s. ErrCode: %d.\n
NSATSBuiltinOverride
_currentResponse
ix%ld
objects
HTTPAdditionalHeaders
quic_vle_decode
encode `%.*s': `%.*s'
EEA_INS_NAMEREF_DYNAMIC
<data URL instance at %p>
CFError { %@, %ld }
-[NSProxyConnectionStreamTask write:handler:]
-[NSGZipDecoder isFinishedDecoding]
B32@?0@8@16^B24
v16@?0@\"_DASActivity\"8
kConditionalConnectionRequirementTimeWindowDelay
v16@?0@\"NSData\"8
_disablesOutOfProcessDirectWiFiUsage
endReason
requestBody
_onqueue_responseDataArrived
decodeChangeCiperSpec
Proxy Authentication Required
CFNetworkConnection-%u
<CFURLAuthChallenge %p>{space = %@, proposedCredential = %@, previousFailureCount = %ld, failureResponse = %@, error = %@/%ld}
kCFNetworkAgentXPCMessageTypePACResult
_waitingBodySize == 0
issuing error to ECONNABORTED
API
Err-1201
!6\xf0%
<HTML 
fState == kTubeStatePostConnectConfiguration
v24@?0r^v8^v16
_kCFNTimingDataResponseHeaderSize
Connection Properties
har-capture-global
RST_STREAM
%@://%@%@/
REST %lld\r\n
Mutations
NetworkServiceType
WriteCookiesToStream
storagePartitionIdentifier
countOfAvailableBytes
NSTCPConnectionConditionsUnmetReasonErrorDomain
v16@?0Q8
newVaryState is nil
HTTPCookieStorage::setCookie
__Host-
cachedResponse
INSERT into cfurl_cache_blob_data (entry_ID, response_object, request_object,\t\t\t\t\t\t\t\t\t proto_props, user_info) \t\t\t\t\t\t\t\t\t VALUES (%q, %q, %q, %q, %q);
8
!fSSLDistNames
_kCFNTimingDataTimingDataInit
NSURLDownloadBinHexDecodedData
v16@?0@\"NSObject<OS_nw_connection>\"8
v16@?0@\"NSDictionary\"8
kCFStreamPropertyStreamLength
_onqueue_notifyTubeManager
T *ClientContextHolder<CFURLDownloadClient>::remember(const T *) [T = CFURLDownloadClient]
outbound encoder
v24@?0^{__CFString=}8^v16
Background session configuration must have a non-nil identifier
write count
application/x-www-form-urlencoded
fsly
v12@?0C8
Original Length
_kExcessiveKeepalivesParametersCount
_kCFNTimingDataNStatRXOutOfOrderBytes
AllowsVoIP
,%@
Tuesday
Err-1204.w
Name
v16@?0^{__CFDictionary=}8
ForceNWLoader
AppSSO
Nov
Yes
HTTPProtocol.cpp
public, max-age=31536000
cookies
<BR 
VaryHeader
HTTPConnectionEvent
called cachedResponseForRequest: with nil request
CoreStreamBase<%s>(%p %s)
v20@?0^{__SecTrust=}8I16
<CFURLCredential %p>{appleID = %@, password = %@ realm = %@, persistence = %d}
TransportConnection.cpp
October
getDispatchQueue
<NetworkProxy %p>{host = %@, port=%d, user=%@, pass=%@, type=%@, CONNECTProperties=%@, transparent=%s}
NDProtocolKey
HasSZExtractor
Protocol
NSExceptionRequiresForwardSecrecy
plist
v24@?0q8^{__CFError=}16
File
static const char *_PNAME<CFNAccount>::GET() [OBJTYPE = CFNAccount]
v16@?0^{_CFURLCredential=}8
DELETE FROM alt_services WHERE creation_time > ?
HTTPEnable
<CFHTTPAuthentication %p>{state = %s; scheme = %@, forProxy = %s}
ssl
__nsurlrequest_proto_prop_obj_22
requestEndTime
\tsessionOnly:%@\n
cookies_deleted_handler_queue_default
earliestBeginDate
v24@?0r^{CoreSchedulingSet=^^?^{__CFAllocator}i^^?^{_opaque_pthread_t}i^{__CFSet}@{os_unfair_lock_s=I}^{__CFRunLoop}^{__CFString}i}8^v16
readFrame
Tue
fProtocolHandler == NULL
ConnectionProtocolGetInputFrames
origin
+[NSURLResponse getObjectKeyWithIndex:]
HttpOnly
PATCH
fsCachedData
enc->qpe_cur_streams_at_risk == 0
?0
!_httpRequest
_forcedNetworkServiceType
DafsaData
timeWindowDelay
v32@?0^v8{?=qi}16
Connection Waiting
qos
Null URL
%s (%d, 0x%x), length %d (0x%x)
F
_TCPAdaptiveWriteTimeout
realm
AVAssetDownloadSessionDeleteDownloadWhenAssetFinalizesKey
~HTTPServerConnection
NSURLSessionResumeExtractor
expensive
NSExceptionRequiresNIAPTLSPackageVersion
_inExpectedBytes != HEADERS_NOT_YET_CHECKED
<TABLE 
description
application/json
B16@?0r*8
The server \"%@\" did not accept the certificate.
fDQ
\t[%ld]: NULL
metrics
com.apple.CFNetwork.HTTPHeaderName
jan
uniqueIdentifierUUID
!_cb
-[__NSCFLocalDownloadTask _private_completionAfterMetrics]
sourceApplicationBundleIdentifierForMobileAsset
Internal error\tfatal
content-disposition
draftVersion
resource unavailable
HTTP3ConnectionCacheWrapper<@%p> for HTTP3ConnectionCache<@%p>
_isLikelyForProxy
kCFProxyTypeHTTP
static const char *_PNAME<HTTPServerRequest>::GET() [OBJTYPE = HTTPServerRequest]
dup draining
__nsurlrequest_proto_prop_obj_10
DROP table IF EXISTS cfurl_cache_schema_version;
writeDBwithCachedResponse-ERROR: %d bind of response version for item: %@
HTTPDigest
TLSv1.3
{ Can't stat: %s, errno: %d parentInfo: %@ }
%g
_networkReachabilityChanged
%@ { socket rs=%@, socket ws=%@, response rs=%@, %@ }
_workQueue
RNTO %@\r\n
bytesPerSecondLimit
_allowsVirtualInterfaces
NSURLDownloadBinHexEncodedData
ProxyAutoConfigEnable
kTubeTypeHTTP3
Mac OS X Server
NSURLDownloadBinHexRepeatByte
Failed
from existing connection
CFNetwork SSLHandshake failed (%d)
?
_chunkedWriteHeaderAndBody
streamLength
dec
Port
nsurlsessiond
file-read-data
<CFURLDownload %p [%p]> {connection = %@, path = %@, client = %@}
Err-2000
assetOptionsPlist
forbiddenProtocols
v16@?0i8B12
DELETE from cfurl_cache_blob_data WHERE entry_ID=%s;
kCFStreamPropertyFTPFetchNameList
port
v24@?0@\"NSObject<OS_nw_authentication_challenge>\"8@?<v@?@\"NSObject<OS_nw_authentication_credential>\"B>16
init_with_task_with_socket_streams
NSURLConnection-WebKitSync
Response Error
{ conn (%llu), local %s => peer %s %s }
!fTube
writeDBwithCachedResponse-ERROR with UPDATE for item: %@.  Error-code:%d
CFMutableURLRequest
StatusCodes
Stream Error
init to origin load
com.apple.CFNetwork.CookiesChanged.%@
kCFURLConnectionURLConnectionProperties
<%p client=%p, message=%@>
_prohibitEncryptedDNS
v28@?0C8^{__CFDictionary=}12^{_CFURLRequest=}20
_protocolInstance == nil
CFNETWORK_PIPELINE_PACK
etag
com.apple.CFNetwork-cc-%d-%lld
_readOutstanding
-[__NSCFURLLocalStreamTaskFromDataTask connection:_willSendRequestForEstablishedConnection:completion:]
touchConnection
_kCFNTimingDataNStatCellTXPackets
got TSU=%llu
reusedAfterTime
Web form password
B24@?0Q8@\"NSObject<OS_xpc_object>\"16
Err-1005
read_ctx->hbrc_out.xhdr
_state == State::ReadingHeader
token
_kCFURLErrorAuthFailedResponseKey
%d pending, %d outstanding, %d closed
NSURLSessionTaskOriginalStartTimeKey
Internal consistency check error for http request %p
CFURLCredential
_kCFNTimingDataNStatVarRTT
tar
dispatch_data_get_size(_dataBuffer) == _dataBufferSize
%@ { state %s - COMPLETED, expected body length %ld  }>
13
h2 updt
PASS %@\r\n
adobepass.ios.app
X-Apple-Cache-Session
bundle
Load Data
NSURLSessionDelegateImplementsWillSendRequestForEstablishedConnectionKey
Email
fConnection
http://
%f
SELECT r.version, r.storage_policy, b.response_object, b.proto_props, d.isDataOnFS, d.receiver_data, b.request_object, b.user_info, r.time_stamp FROM cfurl_cache_response r, cfurl_cache_blob_data b, cfurl_cache_receiver_data d WHERE r.reque
send
multiple choices
<GZipDecoder@%p>
DELETE FROM alt_services WHERE (host = ? AND partition = ? AND port = ? AND type = ?)
No Cellular
NDBackgroundSessionManagerRestoredStateKeyTLSSessionCachePrefix
CachedState
HTTP
kCFURLCredentialKerberosTicketAllowDelegation
countOfBytesSent
kCFHTTPServerKeychain
chown
mimeType
NSURLAuthenticationChallenge must have init parameters
com.apple.CFNetwork.report_networkscore_metrics
Total Written
~PerSide_CFReadStream
COMMIT;
v24@?0^{_CFURLConnection=}8r^{CFURLConnectionClientCurrent_VMax=q^v^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}16
kCFFTPResourceMode
d
%@ token=%@
_allowsHSTSWithUntrustedRootCertificate
A TLS error caused the secure connection to fail.
NSURLSessionDelegateImplementsDidReceiveResponseKey
kCFNetDiagnosticPingOptionTypeOfService
AppSSOProtocol
v16@?0@\"NSObject<OS_sec_protocol_options>\"8
request body stream exhausted
v32@?0@\"NSString\"8@\"NSString\"16^B24
h3stream
proposed
not required
.localhost
HTTPProxy
CFObserverHolder
NSRequiresNIAPTLSPackageVersion
kCFHTTPServerFailingRequest
_rs == NULL && _ws == NULL
only-if-cached
C16@?0@\"BGSystemTask\"8
apr
_maximumWatchCellularTransferSize
Message
v16@?0^{AOSTransactionC=}8
ClientCertificateRequested
stderr
204
CloudFront
-[NSGZipDecoder decodeDownloadData:dataForkData:resourceForkData:]
v16@?0@\"NSCachedURLResponse\"8
CREATE INDEX receiver_data_index ON cfurl_cache_receiver_data(entry_ID);
kConditionalConnectionIsUpload
Cannot get default cookie store - using a memory store for this process
_
DELETE from cfurl_cache_receiver_data WHERE entry_ID in (SELECT entry_ID FROM cfurl_cache_response WHERE time_stamp >= \"%s\")
countOfBytesExpectedToReceive
=
sep
NSTemporaryThirdPartyExceptionAllowsInsecureHTTPLoads
+backgroundSessionConfiguration: is deprecated. Please use +backgroundSessionConfigurationWithIdentifier: instead
 isHTTPOnly: %@
<CFMultiplexerSource %p>
Err310
ERROR: _purgeAllFileSystemCacheData - failed to get the path to the FS cached data at %@
[%llu] (window_size_increment=%d)
conflict
com.apple.ResourceFork
UPDATE cfurl_cache_response SET version=%q, hash_value=%q, storage_policy=%q, partition=%q\t\t\t\t\t\t\t\t\t WHERE entry_ID=%q;
_kTCPKeepAliveParametersEnabled
allowOnlyPartitionedCookies
-[__NSCFURLLocalSessionConnection _tick_finishing]
unknown_scheme
kNetworkProxyAuthorizationElementsKeyProtectionSpace
upload-
NDPortKey
kCFURLConnectionProhibitAuthChallengeUI
upload resumption
creationTime
systemgroup.com.apple.nsurlstoragedresources
Err-3001
v16@?0^{URLProtocolClient=^^?}8
cfurl_cache_response
TLSConfigured
static const char *_PNAME<URLConnection>::GET() [OBJTYPE = URLConnection]
method not allowed
\xff\xdf\xdf\xdf\xdf\xdf\xff
v24@?0^{__CFString=}8^{__CFString=}16
CFAllocatedReferenceCountedObject
 p:
error.error != 0
session
com.apple.cfnetwork.ats.metrics
kConditionalConnectionLaunchOnDemand
lsqpack.c
: 
_kCFNetServiceBlockingMode
Could not communicate with background transfer service
needServerTrust
kConditionalConnectionRequirementTimeWindowStartTime
%@ %s %@
principle
path && [path length]
v20@?0@\"NSError\"8B16
<P 
%p
SetInJavaScript
v16@?0@\"NSURLRequest\"8
sandbox_ext
YES
%ext%
-[NSURLDownload initWithRequest:delegate:]
v24@?0q8@\"NSURLCredential\"16
com.apple.common
ConnectionProtocolGetOutputFrames
0123456789abcdefghijklmnopqrstuvwxyz
308PermRedirect
discretionary
_state == State::EnqueuedOnConnection
CFURLRequest
COMMIT TRANSACTION
logStruct
kCFURLStorageSessionIsDefault
qdec: info: 
_engine
Content-Type
har-capture-pid-specific
no-store
allowCellular
\tsameSite:%@\n
write
_kCFNTimingDataConnectionInterfaceIdentifier
countOfBytesClientExpectsToSend
%s %s %ld
{ fd: %d, local %s => peer %s %s}
get
clean
EHA_LIT_WITH_NAME_NEW
NSURLSessionAppWasResumedForBackgroundSessionNotification
setProperty_offqueue
http3DiscoveryStatus
HTTP2ConnectionCache<@%p>
Local
[%llu] (error_code=%s(%d))
NSServerConfigurationOutboundConnectionProxyDictionary
nwioconnection
writeRequest
http/1.1
PASS
!_inCBHeaders
anonymous
name
v20@?0@\"NSObject<OS_dispatch_data>\"8i16
_connectionWorkQueueSuspensionCount >= 0
kCFProxyPasswordKey
NSURLAuthenticationMethodPrivateAccessToken
%!PS-Adobe-
https://%@:%d/
_connectionWasLost
Forced
<CFNACOAuthSigner@%p>
kTubeTypeHTTP2
Close notify
backgroundIdentifier
_kCFNTimingDataNStatConnectSuccesses
com.apple.cfnetwork.altservicesstorage
_sniffData == NULL
<BODY 
Err-3003
Should've been invalidated
image/jpeg
qenc_drop_oldest_entry
allowsExpensiveNetworkAccess
v24@?0B8@\"NSObject<OS_dispatch_data>\"12i20
loadingPriority
Received tcp connection for upgrade
_NSURLErrorBlockedTrackerFailureKey
com.apple.httpserver.bysocket
main queue = %p, main thread = %p, main mach thread = %u
dataForkData
entry->dte_flags & DTEF_NAME_HASH
_onqueue_resetAndReconnect
AVAssetDownloadTask requires AVFoundation
_forceEnablePQTLS
allocated xhdr size (%zd) is smaller than requested (%zd)
b
endTime
_doingWorkOnThisQueue == false
readNotCompleted != writeNotCompleted
if-range
ERROR: shrinkDB - unable to start a DB transaction.  Error-code=%d
newState >= _state
prefetch
bytes=%lld-
<CFHost %p>
errDomain
ended header; hinfo absent
text/html; charset=utf-8
v20@?0^{_CFURLCredential=}8B16
v16@?0^v8
<CFNetworkReadStream@%p>
deny
!kwn
<write side %p to stream %p>
_readEOF
NLST %@\r\n
<CFURLCredential %p>{username = %@, password = %@, persistence = %d, attributes = %@, identifier = %@}
kCFSOCKSStatusCodeKey
%@ { %@ %s }>
max-age=604800
HTTPNetConnection.cpp
^v16@?0^{__CFWriteStream=}8
Cannot set task delegate after resumption
NSParsedCIDRPrefixKey
connCache
forCache
_kCFStreamStatsTLS_HandshakeTimeMs
trailerData
sqlite-wal
_systemClientOfPrivateAccessTokens
RETR %@\r\n
 
True
Err-1203.w
_sendHEADERS
_dataBuffer == NULL
privacyProxyStrictFailClosed
statusText
bytes=%lld-%lld
HTTPS
downloadFileURL
<SCRIPT 
newTubeKey
NTLM %@
base
failed to make array
bodyStartProvidingData_block_invoke
v28@?0@\"NSObject<OS_dispatch_data>\"8^{__CFDictionary=}16C24
HTTP2ConnectionCacheEntry
HTTPConnectionCache.cpp
Precondition Failed
challenge space %@, failing response %@
CLOSE-WRITE-ERROR: self=%p _dbWriteConnection=%p, result=%d
nginx
,\n
_callbacks->version == 2
too many HTTP redirects
v56@?0^{__CFString=}8^{__CFData=}16{shared_ptr<const __CFArray>=^{__CFArray}^{__shared_weak_count}}24{shared_ptr<__CFError>=^{__CFError}^{__shared_weak_count}}40
nov
kTubeTypeNegotiate
DiskCookieStorage Journaling On
hsts_persistent
basePriority
prohibitPrivacyProxy
\"%@\"
newTube->getType() == kSTubeTypeHTTP
_onqueue_errorHandler
writeDBwithCachedResponse - Invalid protocol-property list - CFURLRequestRef. protoProps=%@
lighttpd
Received socket streams for upgrade
B
_loggingPrivacyLevel
_preventsIdleSleepOnceConnected
_disableAPWakeOnIdleConnections
com.apple.CFNetwork.ForceIOPath
KEYCHAIN_WEB_FORM_PASSWORD
<!--
status == ConnectionSearchStatus::NoConnection
\tisHTTPOnly: %@\n
retryError
dispatch_data_get_size(data) > 0
read_ctx->hbrc_out.state == XOUT_VALUE
!_processingReadCall
errno %d
%X\r\n
RunloopBlockContext
prog.ep_hea_action == EHA_LIT_WITH_NAME_STAT
6
<HTTP protocol instance %p>
header block for stream %llu is too short (%zd byte%.*s)
http://%@%@
CFNetwork
Request Time-out
vary
CFNETWORK_LOG_AUTH_TIMEOUT
<HTTP request stream %p>{url = %@, flags=%p, connection stream = %p}
%@ { state %s, expected total body length %ld  }>
status
.local
NULL
Include Subdomains
CFNETWORK_IO_LOG_FILE
bytes
Feb
READ
v40@?0@\"IDSBaseMessage\"8@\"NSError\"16q24@\"NSDictionary\"32
com.apple.CFNetwork.CacheDB-write
RLF
har-host-denial-list
max-age=2592000
%@@%@
SetDefaultCredential
v28@?0c8@\"NSObject<OS_nw_endpoint>\"12d20
Negotiate %@
<AuthenticationState@%p>{
INSERT: ERROR: unable to obtain the persistent store directory.
ConnectionProtocolConnected
_allowsPowerNapScheduling
 { Status Code: %ld, Headers %@ }
AVURLAssetDownloadTokenKey
HTTP2StreamBridge
manager
Array
AVAggregateAssetDownloadTask does not support response property
v44@?0@\"NSObject<OS_nw_content_context>\"8@\"NSObject<OS_dispatch_data>\"16B24{?=qi}28
_plusOneForFirstTube
CONNECTION_DOWN
WONR.alloced_len
audit
v16@?0@\"NSURLSessionTask\"8
_readBodyStart
ConnectionProtocolAddInputHandler
com.apple.cfnetwork
shouldOpenNewConnection()
^{__CFError=}8@?0
Memory Cookies: { %p, %s }
NSURLDownloadMacBinaryDataForkLength
Session.mm
startTimeoutTime
_allowsTLSFalseStart
com.apple.runningboard.can-suspend-locked
Cannot create an AVAggregateAssetDownloadTask in a non-background session
127.0.0.1
[%@]:%d
_rl == NULL
explicitFlags
\tcommentURL:%@\n
_kCFURLProtectionSpaceAuthenticationSchemeOAuth
Task <%@>.<%lu>
CST
No
HTTPConnectionCacheEntry.cpp
FALSE
got Header Ack instruction, stream=%llu
LocalSessionTask.mm
:memory:
_neverDecrementedPlusOneForFirstTube
_shouldPreserveBackgroundSessionDisposition
sharingd
GIF87a
CachePolicy
failInsecureLoadWithHTTPSDNSRecord
!_inCBData
NSURLConnection ordering violation: didFinishLoading to be scheduled before didReceiveResponse
requestBeginTime
CoreSchedulingSet.h
kCFProxyAutoConfigurationHTTPResponse
kSTubeTypeHTTP
', '
v24@?0@\"NSObject<OS_sec_protocol_metadata>\"8@?<v@?@\"NSObject<OS_sec_identity>\">16
isWriting
%.*s %s %s
TubeManager.cpp
!_schedulingSet
sharedCaches
com.apple.nsurlsessiond/Downloads
qdec: warn: 
protocol
BEGIN TRANSACTION
encoding
beginTime
v16@?0^{HTTPServerConnection=^^?^^?{_CFHTTPServerClient_V0=q^v^?^?^?}^^?^{__CFAllocator}i^{__CFDictionary}@^{CoreSchedulingSet}^{__CFError}{_CFHTTPServerConnectionCallbacks_V1=q^?^?^?^?^?}^{HTTPServer}C^{__CFReadStream}^{__CFWriteStream}ddq
qdec_maybe_update_entry_hashes
VaryState
NWIOConnection.cpp
Length Required
%@: %@\n
_socketStreamPropertyQOSClass
timeWindowDuration
not yet parsed
httpVersion
METRIC_DATE
expectation failed
STOR %@\r\n
\xff\xdf\xdf\xdf\xff
One or more certificates have expired or are not valid yet.
usesClassicLoadingMode
h2 frame
/%@
_handleEvent_ReadyFinish
CFNetwork _delegate_willSendRequestForAuthenticationChallenge called delegate - Load: %@ Challenge: %@
_metaClientCallback == NULL
%@:%d
stopSecureConnection
REL
create FILE
failed to initialize compression, error %ld
MKD %@\r\n
AssertionManager.m
EffectiveConfigurationVersion
AUTHBROKER_SERVICE_NAME
_establishmentDelegate
CFNETWORK_NOTHROTTLE
hsts_identifier
-[NWStreamPair _onqueue_writeData:outError:]
generated TSU=%u instruction %zd byte%.*s in size
clear
com.apple.CFNetwork.HSTS.DisableHSTS
mayBeDemotedToDiscretionary
oauthtoken
_kCFNTimingDataNStatWifiTXPackets
__nsurlrequest_proto_prop_obj_18
NSServerConfigurationSOCKS5ServerCredentials
kCFProxyTypeAutoConfigurationURL
fSocketStream == NULL
<%sDownloadDataDecoder@%p>
SPI %s on longer supported
_writeBlockedSemaphore == NULL
_kCFNTimingDataTCPInfoAtStart
200
<B 
CFSocketStream
HSTS.plist
com.apple.cfnetwork.cookiestorage
CFNETWORK_HAR_LOGGING
v16@?0@\"NSError\"8
nghttpx
NSURLRequest.mm
_readHeadersDoRead
%@-shm
scheduleAndOpenWithHandler
__hhaa__
{ conn: %p, local %s => peer %s %s}
301PermMove
kConditionalConnectionIsDiscretionary
NSTemporaryExceptionRequiresForwardSecrecy
_kCFHTTPCookiePolicyPropertyAllowOnlyPartitionedCookies
access-control-allow-methods
task failure
Jul
CREATE INDEX time_stamp_index ON cfurl_cache_response(time_stamp);
kCFProxyTypeKey
!_connectionParams
Negotiate
kCFHTTPAuthenticationPassword
firstWaiter != NULL
http://%@/
 { URL: %@ }
 - corrupt
respondedToWillBeginDelayedRequestCallback
CFNETWORK_IO_LOG
Err-1004
_textBase64
v36@?0@\"NSObject<OS_dispatch_data>\"8B16{?=qi}20
NSURLDownload.mm
_kCFNTimingDataRequestStart
qenc: debug: 
%s: no longer implemented and should not be called
address
v24@?0^{__CFReadStream=}8q16
SAwaitingTube
Structured
double lit would result in ratio > 0.95, reset
AVAssetDownloadTaskMinimumRequiredPresentationSizeKey
_provideRequestBodyFromData
kCFStreamPropertyFTPFileTransferOffset
Connection Ready
_receivedHeadersDone
SSL-READ
__nsurlrequest_proto_prop_obj_26
Mon
Err-1017
Skipping AppSSOProtocol
0
DROP table IF EXISTS cfurl_vary_state;
SSL
Summary
!ss->isEmpty()
-[__NSCFLocalSessionTask _onqueue_suspendWorkQueue]
FTPPort
uuid
(ptrdiff_t(&fRetainCount) & 3) == 0
_asyncWriteFileCompletely
TFOSuccess
alt-svc
__nsurlrequest_proto_prop_obj_19
The certificate for this server is not yet valid. You might be connecting to a server that is pretending to be \"%@\" which could put your confidential information at risk.
kCFHTTPCookieStorageGroupContainerURL
HTTPServerNWStream.mm
multipart/x-mixed-replace
atsTrustPolicy
\tdomain:%@\n
hasStarted
Certificate unknown
v40@?0@\"__NSCFLocalDownloadTask\"8@\"NSURL\"16@\"NSURLResponse\"24@\"NSError\"32
!waiter->hasBeenClaimed()
~IOConnWrapper
<FTP protocol instance %p>
kCFHTTPAuthenticationPropertyMethod
Decompression failure
_requiresSustainedDataDelivery
The read-connection to the DB=%@ is NOT valid.  Unable to determine schema version.
_preferredMaxParallelTasks
(This file must be converted with BinHex 4.0)
Err-1022
_delegate_didFail
enqueue
allowsPersistentDNS
_fetchType
-[__NSURLSessionLocal _request:isCacheEquivalentTo:]
setProperty
dtype
%p -- keeping alive
version
\xff\xdf\xdf\xff
TRUE
_supportsAVAssetDownloads
image/gif
requestBodySize
WebSocket tasks are not supported in background sessions
error != NULL
_NSURLErrorVPNInactiveFailureKey
Protocol version
CONTINUATION
empty
AVAggregateAssetDownload
CFNetworkDownload_XXXXXX.tmp
Response
NetworkStorageDB:_openDBWriteConnections: failed to open write connection to DB @ %s.  Error=%d. Cause=%s
v16@?0r^{CompactCookieArray=^^?^^?^{__CFData}}8
=%@
date
mainDocumentURL
<HTTP stream context %p>{url = %@, state = %s, conn=%p, isZombie=%s}
invalidateAsync_block_invoke
duplicate ICI: %u
parse_header_prefix
-[__NSCFLocalSessionTask dealloc]
distnames
%d [%d]
!_callbackBuffer
_kCFStreamPropertyFTPRemoveResource
v16@?0^{NetworkProxyCredential=^^?^{__CFAllocator}i^^?^{_CFURLCredential}iQ}8
NSTemporaryExceptionAllowsInsecureHTTPLoads
v24@?0@\"NSArray\"8@\"NSError\"16
%d
Err-3005
\tname:%@\n
CreateToNow
upgrade-insecure-requests
NDBackgroundSessionManagerKeySessionUUID
Cannot create download task without request or resume data
Dec
%@/%@%@
kCFGetAddrInfoFailureKey
STube.cpp
q24@?0@8@16
can't create filesystem path for %@
## Only %ld bytes after header, need at least 4
No Content
isSharedSession
NSURLDownloadBinHexDataForkBytesRemaining
%@/%s
Cookies
_kCFNTimingDataNStatConnectAttempts
v28@?0@\"NSData\"8B16@\"NSError\"20
_kProxySupportSyncPACExecutionRunLoopMode
program: %s; %s; %s; flags: 0x%X
SITE TRUTH ON\r\n
vary state mismatch
\tcomment:%@\n
\r\n\r\n
akamai
Did Send Body
applyBlock
transactionMetrics
Unsupported Media Type
ETA_NOOP
DiskCookieStorage Updated
bytes=0-
v16@?0^{__CFRunLoop=}8
_allowsTLSSessionTickets
CoreReadStream
_kCFNTimingDataConnectionReused
<H1 
updateTCPAdaptiveParamters
image/png
_nscfBridgeURLCacheDiskCapacity
Sep
Comment
credKind
written == [(NSData*)data length]
CFReadStreamGetStatus(_stream.get()) == kCFStreamStatusNotOpen
timeoutIntervalForResource
__nsurlrequest_proto_prop_obj_15
%s deprecated
Err-1021
Err-1103
updateCoalescingConnectionKeyWithHostWithDNSRecord
Err-997
v16@?0^{BaseAwaitingTube=^^?^{__CFAllocator}iB}8
ciphersuite
D
v20@?0@\"__NSCFLocalSessionTask\"8C16
Finished Merging Classes
responseHeaderSize
new_entry->ete_id > enc->qpe_cur_header.hinfo->qhi_max_id
WINR.alloced_val_len >= WINR.val_len
tgz
%@, %s (Hash %lx)
Illegal parameter
_kCFNTimingDataNStatTXPackets
NSURLSessionResumeResponse
_read
Pending Tubes: %ld
_delegate_shouldUseCredentialStorage
CFNAccountKerberos
other
DELETE FROM alt_services WHERE ROWID in (SELECT ROWID FROM alt_services ORDER BY ROWID DESC LIMIT -1 OFFSET %ld)
Saturday
MDT
isUnlistedTracker
[NSURLSession sharedSession] may not be invalidated
ConnectionProtocolConnect
_kCFNTimingDataInternalTransactionMetrics
Err-1006
kCFDataURLTextEncodingName
<CFNAccount@%p> user-name:%@
_connectionClientInterface_resumeConnection
ClassicDelegateHolder
%@ { service name='%@', type='%@', port=%@> }
CFURLCache
URL
body
preconnect
_kCFURLCachePartitionKey
_kTCPKeepAliveParametersIdleTime
-[NSURLDownloadInternal dealloc]
user-agent
CFN_USE_HTTP3
Err-1002
CFN_USE_HTTP2_CONNECTION_COALESCING
DELETE from cfurl_cache_response WHERE entry_ID=%s;
markAsClaimed
HTTP_NETWORKSCORE_DATA
decoded_val
requestBodyTransferSize
_dataBufferSize <= _maxReadCount
called removeCachedResponsesSince: with nil date.
content
connectionWasLost
expiration
%@, ALPN supported %@, Tube type: %@
PRAGMA journal_mode=WAL;
bad count
bad request
payment required
v16@?0@\"NSInputStream\"8
Exception
suspend
\t\t%d: %@ ,\n
readResponse
AVAssetDownloadTask does not support response property
RAW-SEND
NSURLAuthenticationMethodNegotiate
B24@?0r*8@\"NSObject<OS_xpc_object>\"16
connectionProxyDictionary
access-control-request-method
prefix
x-frame-options
read count
%@ (%s)
content-type
text/html
}
TRACE
<CompactCookieHeader@%p> { domain: %s, partition: %s, name: %s, path: %s, value: %s, session: %c, secure: %c, httponly? %c, expires: %@, created: %@, accessed: %@ }
start
com.apple.cfnetwork.cfnetworkagent
cpio
request has no url
<redacted>
v44@?0{shared_ptr<NetworkProxy>=^{NetworkProxy}^{__shared_weak_count}}8B24{?=qi}28
%@.%lu.childAssetDownloadTasks
persistence
_onqueue_getTransactionItr
T *ClientContextHolderInfo<CFHostClientContext>::forget() [T = CFHostClientContext]
!_inData
_kCFNTimingDataRemoteAddressAndPort
Would you like to connect to the server anyway?
com.apple.WebSheet
kCFURLRequestContentDecoderSkipURLCheck
called removeCachedResponseForRequest: subclass should implement
,
ERROR: shrinkDB - shrink of file system cache did not fully complete.  Result: %d
ERROR: decoding user-info failed.  Error:%@
Total time to write
_kCFNetworkHSTSIncludeSubDomains
%.*s%d%s
%@/%s_remove
link
KEYCHAIN_LABEL_FORMAT%@%@
Failure occurred while closing file
CommentURL
Network Load
Binary{ %@ }
oscar
FTP is deprecated for URLSession and related APIs. Please adopt modern secure networking protocols such as HTTPS.
shouldHandleHTTPCookies
Apple Global Domain
CREATE TABLE IF NOT EXISTS cookies (        name text NOT NULL,        value text NOT NULL,        domain text NOT NULL,        path text NOT NULL,        partition text NOT NULL,        is_secure int NOT NULL,        is_hostOnly int NOT NU
_TLSMinimumSupportedProtocolVersion
-[NSURLCache _initVaryHeaderEnabledWithPath:]
shared_tcpConnWorkQueue_UserInteractive
SYST\r\n
Reset Content
length required
Connection Start
initializedFromToken
Requested range not satisfiable
NSParsedCIDRMaskKey
taskType
%s
HTTP2Connection.cpp
Please check your proxy settings. For help with this problem, contact your system administrator.
v24@?0^{__CFArray=}8^{__CFError=}16
Last Sync
sandboxExtShm
_inExpectedBytes == HEADERS_NOT_YET_CHECKED
_kCFNTimingDataSecureConnectionStart
Cannot create upload task without request or resume data
partition != nil && partitionLen > 0
\n
drop entry %u (`%.*s': `%.*s'), nelem: %u; capacity: %u
no content
Space
Err306
scoped interface
failed array validation
_authenticatorStatusCodes
null url string
storage
metricstream_queue
PASV\r\n
com.apple.kerberosaccountstore.cbqueue
NSHTTPCookieAcceptPolicy
setDestination:allowOverwrite: failed to create url for path.
_allowsTLSFallback
br
_onqueue_scheduleIO
UIApplicationDidEnterBackgroundNotification
NetworkStorageDB:_openDBReadConnections: failed to open read connection to DB @ %s.  Error=%d. Cause=%s
NSURLCredentialStorageRemoveSynchronizableCredentials
__nsurlrequest_proto_prop_obj_27
WARNING: %s should no longer be called
NSAllowsLocalNetworking
LocalDownloadTask.mm
_FTPStreamOpenCompleted
ftp
Max-Age
writeDBwithCachedResponse-ERROR: NO key for item: %@
com.apple.CFNetwork.HTTPFallbackHost
trackerContext
application/javascript
TimeoutSeconds
<HostLookup@%p> { %p }
Certificate revoked
content-encoding
forwarded
EEA_INS_NAMEREF_STATIC
%02x
kCFSOCKSNegotiationMethodKey
-[NSGZipDecoder fileAttributes]
_http._tcp
can't grow data to length
NSURLAuthenticationMethodServerTrust
v16@?0^{MetaConnectionCache=^^?^{__CFAllocator}i@}8
PRAGMA user_version=203
startedUserInitiated
Multiple Choices
enc->qpe_cur_streams_at_risk <= enc->qpe_max_risked_streams
\tpartition:%@\n
allowPrivateAccessTokensForThirdParty
NOT 
unsupported media type
jun
-[__NSCFURLLocalStreamTaskFromDataTask connection:challenged:authCallback:]
_readBufferConsume
_allowsTCPFastOpen
init
Total Expected
WriteStream
403
Session
no cellular
kCFStreamPropertyFTPResourceSize
RemoveCredential
_kNSURLRequestKey
idleDuration
AuthenticationCache.cpp
_data
APSRelayEngine.mm
 | 
CFURLProtectionSpace
PUT
com.apple.__NSCFLocalDownloadFile
!fSSLTrust
<NetworkProxyAuthorizationElements %p>{cred=%@, protSpace=%@, challenge=%@ client=%@ <%@>}
_clientIsNotExplicitlyDiscretionary
`
Completion handler blocks are not supported in background sessions. Use a delegate instead.
Received Accounts
__NSCFURLSessionConfiguration_Immutable
trailers
updatedStreamingZipModificationDate
SSL-SEND
Err-1015
countOfBytesExpectedToSend
get, post, options
-[NSURLRequest _URLHasScheme:]
%s @ %p, version %2.2x, length %d
connect
SetCredential
geo.apple.com
_sourceApplicationAuditTokenData
%lx
Certificate expired
HTTP2ConnectionCache.cpp
-[__NSURLSessionLocal _cfurlRequest:isCacheEquivalentTo:]
Original Request
__CFNetworkUniqueKey
key
fake://host/
__nsurlrequest_proto_prop_obj_14
Err-1009
_prefersInfraWiFi
_schedulingSet
Stream tasks are not supported in background sessions
_allowTCPIOConnectionStreamTask
APSRelay requires FTServices
Err-1014
HTTPConnectionCacheEntry
Domain
!_inHeadroomInfo
_directoryForDownloadedFiles
DoesSZExtractorConsumeExtractedData
isHTTP
NSURLSessionResumeBytesReceived
Cannot create a thread for reading data from the requestBody stream error: %d
NSTemporaryExceptionMinimumTLSVersion
NSURLSessionTaskStateRunning
?1
read
v16@?0@\"__NSCFURLLocalStreamTask\"8
}  }
Read from disk
C
__nsurlrequest_proto_prop_obj_13
com.apple.symptomsd
v32@?0@8@16^B24
copyDebugDesc
v20@?0Q8i16
BuiltinException
ATSConnectionExceptionEvent
v24@?0^{__CFDictionary=}8^{PrivateHTTPCookieStorage=^^?^{__CFAllocator}i^^?^{CoreLockable}C^{__CFString}^{__CFString}C}16
v16@?0^{ConnectionClientInterface=^^?}8
_readFinalized && _writeFinalized
CFNetwork Diagnostics [%d:%d] %s {\n
fSet && CFSetGetTypeID() == CFGetTypeID(fSet)
v20@?0C8^v12
v16@?0@\"BGNonRepeatingSystemTask\"8
 path:\"%@\"
<AuthenticationInfo@%p>{%s - Valid(%c) Authenticated(%c) ConnAuth(%c)}
CREATE INDEX proto_props_index ON cfurl_cache_blob_data(entry_ID);
kCFURLCredentialKerberosNoUIFlag
metricstream
%@%d.%d
Sun
AVAggregateAssetDownloadTask does not support originalRequest property
%@:%@:%@:%s:%s
__NSCFURLSessionConfiguration_Mutable
multipathServiceType
found
close
Connection
com.apple.nsurlsessiond.readonly
v24@?0@\"NSData\"8@\"NSError\"16
_100ContinueTimerStart
\r\n\r\n%@
Redirection
ProxyAutoConfigURLString
SSLSetPSKSharedSecret returned %d
com.apple.cfnetwork.cfnetworkagentclient
kCFURLStorageSessionProcessSharing
_CFCachedURLResponseReceiverDataArray
%@/VaryState.db
-[__CFN_SocksHandshake finish:]
fail %ld
connectionCacheTypeForTubeType
<%p>
new_cookie_storage
Thursday
shared_tcpConnWorkQueue_Unspecified
Hostname mismatch.
_connectionPoolName
unsupported version
%PDF-
com.apple.cfnetwork.ats.hardfailures
%s://%@/
(avail_bits & 7) == 0
__releaseStorageAssertion
Err-1204
C16@?0^v8
neagent
v32@?0@\"NSNumber\"8@\"__NSCFURLSessionTaskInfo\"16^B24
DEBUG: there is no SQL cache DB located at %@.
got error from inflate, %ld
:%d
_allowsIndefiniteConnections
_allowsTLSSessionResumption
copyOutData
connection:didFinishLoadingWithError
SETTINGS_MAX_FRAME_SIZE
CFURLDownloadDataDecoder
Library/Cookies/
%8.8x: 
range
kCFProxyPortNumberKey
_kCFStreamStatsDNS_ResolutionTimeMs
forbidden
_pendingData
gzip
_onqueue_bothSidesFinalized
Path
com.apple.network
requested URL too long
assertionCount > 0
nosniff
HTTPPort
Not Found
-[__NSCFURLLocalStreamTask _onqueue_processWriteWork:]
v24@?0@\"NSURLRequest\"8@\"NSFileHandle\"16
CFNetworkHTTP3Override
stream
Vary Validation
conn
com.apple.cfnetwork.ats.loglevel
EHA_LIT_WITH_NAME_DYN
AppleLanguagePreferencesChangedNotification
Friday
AVAggregateAssetDownloadTaskIdentifierKey
Challenge
_kCFStreamErrorCodeKey
%02X
firstWaiterIdx != -1
[%llu] %s %s frame<length=%ld, flags=0x%x, stream_id=%d>
CoreWriteStream
_chunkedReadHeader_block_invoke
_allowsMultipathTCP
CFNetwork _loaderInterface_performDefaultHandlingForChallenge - Load %@ Challenge %@
suspendCount
text/plain;charset=utf-8
AVAssetDownloadTaskMediaSelectionsForMultichannelKey
<%d cookies in %d domains>
Cache-Control
NSURLSessionDownloadURL
(unknown version)
FinishTaskUninterruptable
_tlsTrust
local
_finished
cancel header block for stream %llu, seqno %u
Cannot write file
//
com.apple.developer.networking.networkextension
\t\t[%ld]: EnqueuedRequest(%p) - Client(%p) Request(%p, %@) Auth(%@)
CantRename
Download decoding failed
Default Session Classes
; 
ORWEDM
Err-998
CFNETWORK_DIAGNOSTICS
accept-language
newWriteStream
www.apple.com
v44@?0@8B16{?=qi}20@\"NSObject<OS_nw_content_context>\"36
^{__CFString=}8@?0
remoteEndpoint
kConditionalConnectionRequirementDownloadBytes
temporaryDestinationURL
-[NSURLSession dealloc]
June
newTube
_allowsResponseMonitoringDuringBodyTranmission
Upload
December
\n\r
index
see other
CFNetworkAVDownload_%@.movpkg
Jun
TLSv1.2
v24@?0q8@\"NSError\"16
responseUnblocked
effectiveConfig
~HTTPProtocol
must replay
v20@?0I8r^v12
_kCFNTimingDataNStatWiredTXPackets
all
BAD
RE
%@{ default: %d private: %d process-sharing: %d ident: %@, cache = %p, cookies = %p, auth = %p, hsts = %p }
_enablesL4SInternal
id > enc->qpe_cur_header.base_idx
qenc_remove_from_risked_list
header_out_begin_literal
ERROR - Unkown Type
cfurl_cache_blob_data
.local.
kConditionalConnectionRequirementUploadBytes
decodeHandshake
Switching Protocols
initWithSchedulingSet
_onqueue_newTubeReady
%@: Host:%@, Server:%@, Auth-Scheme:%@, Realm:%@, Port:%ld, Proxy:%@, Proxy-Type:%@
AVAssetDownloadSessionLinkAssetURLToDestinationURLKey
Err-999
%.5fs
AwaitingTube
pair { %p, %s }
application/dns-message
x-content-type-options
HTTPBasic
HTMLForm
_onqueue_scheduleAndOpenWithHandler
<CFNAccountKerberos@%p>
path
/%@/%@
(Request) %@\n(Response) %@\n(Fetch Start) %@\n(Domain Lookup Start) %@\n(Domain Lookup End) %@\n(Connect Start) %@\n(Secure Connection Start) %@\n(Secure Connection End) %@\n(Connect End) %@\n(Request Start) %@\n(Request End) %@\n(Response
_tlsTrustPinningPolicyName
Err-1000
The request timed out.
HTTPCookiePartitionHelpers.cpp
spaces
com.apple.NSURLSession-work
secureConnection
isEphemeralSession
_100ContinueTimerFired
CREATE TABLE IF NOT EXISTS cfurl_vary_state(request_key TEXT PRIMARY KEY UNIQUE, vary_state TEXT, time_stamp NOT NULL DEFAULT CURRENT_TIMESTAMP);
B24@?0Q8@\"NSObject<OS_nw_object>\"16
Task: %p
<KerberosAccountBroker@%p>
CFNETWORK_HOST_QUEUE_KIND
cache
_onqueue_requestIsChunkEncoded
;*__%%%SKIP_DECODING%%%__*;
cfnetwork@apple.com
AppleLanguages
_nscfBridgeURLCacheCurrentDiskUsage
_kCFHTTPCookiePolicyPropertyAllowHTTPOnlyOverwrite
Localizable
_kCFNTimingDataNStatAvgRTT
_kCFNTimingDataTotalBytesReceived
,%@;q=0.%u
v32@?0@\"NSString\"8@\"NSString\"16@\"NSString\"24
NSAppTransportSecurity
kCFHTTPServerServerTrustChain
startedDateTime
policies
400
huff_decode_fast
lastResponse
CoreStreamOpenBlocking
GIF89a
v32@?0r*8S16S20S24S28
Bytes Written
called storeCachedResponse:forRequest: with nil request
Accepted
EEA_INS_LIT
NSURLAuthenticationMethodHTTPBasic
v20@?0i8@\"NSObject<OS_nw_error>\"12
MST
fKind == eDispatchQueueBased
_onqueue_beginTrailers
<CFURLCredential %p>{ accepted server trust }
blockTrackers
No renegotiation
v48@?0^{__CFHTTPMessage=}8I16^{__CFString=}20i28{SmartBlockWithArgs<const _CFURLCredential *, bool>=^v^{__shared_weak_count}}32
NSURLRequestFileProtocolExpectedDevice
service
DiskCookies
Expectation Failed
_kCFNTimingDataNStatRXDuplicateBytes
QUICUtilities.cpp
_onBehalfOfPairedDevice
%@-%d
_kCFStreamPropertyHTTPFilterEstablishedConnectionBlock called
Error: stepSQLStatement:toCompletionWithRetry - stepping returned unhandled result=%d, DB=%@
CantCreateWriteStream
countOfBytesReceived
com.apple.Foundation.NSHTTPCookieManagerAcceptPolicyChanged
!_callbackHandler
_preventsSystemHTTPProxyAuthentication
NSURLResponse.mm
0x%s
EST
BEGIN IMMEDIATE;
MainDocument URL
-[__CFN_CoreSchedulingSetRunnable startedRunLoop:]
_kCFNTimingDataNStatRXBytes
Unknown attribute name %@
\"\"
(count % 2) == 0
protocolDidFinishLoading
\r\n%X\r\n
userinfo
_kCFNTimingDataNStatMinRTT
com.apple.nsurlsessiond
kCFFTPProtocolPropertyReturnDirectoryListing
appleid
_kCFHostBlockingMode
Loader
called storeCachedResponse:forRequest: subclass should implement
HTTP3ConnectionCacheEntryWrapper<@%p> for HTTP3ConnectionCacheEntry<@%p>
h2 ping
END_HEADERS
_connection
DashboardClient
modTime: %@ st_uid: %d, st_mode: %o st_flags: 0x%x acl: %s
RB
got ICI instruction, count=%llu
__nsurlrequest_proto_prop_obj_4
SELECT * from alt_services where expires_time > strftime('%s','now')
!0
v16@?0@\"NSURLCredential\"8
NoORWECX
There was a problem communicating with the web proxy server (HTTP).
writeDBwithCachedResponse-ERROR: bind of storage policy for item: %@
APSRelayTransaction.cpp
v32@?0^{__CFHTTPMessage=}8@\"NSObject<OS_dispatch_data>\"16r^{?=qi}24
kCFProxyTypeSOCKS
 { request: %@ }
HTTPServer
-[__NSCFURLLocalStreamTaskFromDataTask connection:didReceiveInformationalResponse:]
cancel called for rl %p, mode %@
<%s %p [%p]>
The server requires a client certificate.
withExistingProtocolAsync
UIApplicationSuspendedNotification
_protocolInterface_startLoad_block_invoke
__nsurlrequest_proto_prop_obj_2
Err-3007
~HTTPNetConnection
ioLogger
Decryption failed
Stream
STubeManager.h
SETTINGS_INITIAL_WINDOW_SIZE
BM
shouldCancelOnDisconnect
i <= [_pendingWork count]
HTTPTransaction.cpp
[data length]
IsRequest
Persistent
AtEnd
enableSPIDelegateCallbacks
access-control-expose-headers
ERROR: NSURLStorageURLCacheDB _setDBSchema: DB=%@ table index on receiver_data - %s. ErrCode: %d.
CopyAllDataFromDataArray:  ERROR.  Failed to allocate a CFDataRef of size %ld.
_readHeadersStart
_100ContinueTimer
static const char *_PNAME<TransportConnection::RefCountedWrapper>::GET() [OBJTYPE = TransportConnection::RefCountedWrapper]
header block for stream %llu needs more bytes
service unavailable
__nsurlrequest_proto_prop_obj_3
firstOnConnection
com.apple.URLDownload
New Request
CFHTTPCookieStorageSetSharedHTTPCookieStorage
_state < State::ReceivingResponse
[error %d converting]
YIIFdQYGKwYBBQUCoIIFaTCCBWWgFTATBgkqhkiG9xIBAgIGBiqFcCsOA6KCBUoEggVGYIIFQgYJKoZIhvcSAQICAQBuggUxMIIFLaADAgEFoQMCAQ6iBwMFAAAAAACjggQiYYIEHjCCBBqgAwIBBaEbGxlDT1JFU0VSVklDRVNET00uQVBQTEUuQ09NoiowKKADAgEDoSEwHxsESFRUUBsXY29yZXByb3h5MjAwNi5hcHBs
_reusedAfterTime
NSURLAuthenticationMethodNTLM
__CFURLResponseNullTokenString__
kCFURLDownloadResumeURL
firstResumeTime
urlstring
%@ { queues=%s, %@ }
unsupported URL
Err-1020
v48@?0B8@\"NSObject<OS_dispatch_data>\"12B20{?=qi}24@\"NSObject<OS_nw_content_context>\"40
mediaserverd
Partition
status == kSHTTPConnectionCacheEntryFoundExistingNetConnection
key_not_serialized
com.apple.CFNetwork.LoaderQ
kCFNetDiagnosticPingOptionPacketCount
!DNSRecordIPAddresses.empty()
 isSecure:%@
PRAGMA wal_checkpoint;
satisfied
Method Not Allowed
_allowsHTTP3Internal
lsqpack_enc_int
<__NSCFURLLocalStreamTaskWork %p <%s>>
kCFURLDownloadResumeServerModificationDateString
CFHTTPCookieStorage.c
_kCFNTimingDataResponseBodyBytesReceived
TLSMinimumSupportedProtocol
304
resource exceeds maximum size
_loaderClientEvent_DidReceiveData
ReadStream
errCode
websocketSend
entry == STAILQ_FIRST(&enc->qpe_buckets[buckno].by_nameval)
_CFServer
waiting for offset
stubs->version == 0
unknown error
Cookie_%d_%p
_TLSMaximumSupportedProtocolVersion
HSTSCache
v32@?0@\"NSObject\"8@\"NSObject\"16^B24
h2 stgs
bodyParts
Err-1102
Encountered unexpected state %d for request %p
TLSv1.1
privacyProxyFailClosed
pushed entry %u (`%.*s': `%.*s'), nelem: %u; capacity: %u
MSDOS-like directory output is on
<BrotliDecoder@%p>
NSHTTPCookieManagerCookiesChangedNotification
The server \"%@\" requires a client certificate.
%.*s{%.*s}
_delegate_willSendRequest
basePrioritySetExplicitly
cache-control
Options
AwaitingTube.h
v24@?0r^{CompactCookieHeader=}8^B16
Policy
v24@?0@\"NSMutableArray\"8i16i20
ERROR: NSURLStorageURLCacheDB _setDBSchema: DB=%@ table index on time_stamp - %s. ErrCode: %d.
<CFURLCredential %p>{ identity = %@, certificate array = %@, persistence = %d}
_ignoreDidReceiveResponseDisposition
_longLivedConnectionCacheCellPurgeTimeout
filename
.%s
Cancel
DELETE from cfurl_cache_response WHERE time_stamp >= \"%s\"
<URLConnectionClient@%p>
Caches
v40@?0{shared_ptr<const __CFArray>=^{__CFArray}^{__shared_weak_count}}8{?=qi}24
TCP Connection Start
writeDBwithCachedResponse-ERROR: (_dbWriteConnection=%p) insert SQL stmnt. is nil for storage: %@
policy
_kCFNetworkErrorCachedResponseKey
ClientIdentifier
/
%@@%@:%ld
recommendedPolicy
ERROR: NSURLStorageURLCacheDB _setDBSchema: DB=%@ pragma wal enable - %s. ErrCode: %d.
Credential
establishTime
assetTitle
getPreparedRequest
scheduledOriginLoad
_NSCFTranslatedFileURLProtocol_PIMPL_%d
__nsurlprotectionspace_proto_plist
, cnonce=\"%@\", nc=%08lx, qop=\"%@\"
default
ATSExceptionDomains
com.apple.NSHTTPCookieManagerNotification
%@(%s)
__nsurlrequest_proto_prop_obj_16
bin
task success
called storeCachedResponse:forRequest: with nil cached response
-[__NSURLSessionWebSocketTask _onqueue_validateWebSocketHandshake]
Temporary Redirect
hack
schedulingSet
__nsurlrequest_proto_prop_obj_20
%@
discretionaryOverride
-[NSGZipDecoder filenameWithOriginalFilename:]
_kCFNTimingDataConnectEnd
NDServiceIDKey
httpstorages.sqlite
July
, opaque=\"%@\"
kCFDNSServiceFailureKey
CFNetwork Self Signed Certificate
%@ { state %s, chunk state %s  }>
com.apple.httpserver.bystreams
\tversion:%ld\n
ERROR: NSURLStorageURLCacheDB deleteResponsesSinceDate: dbConnection=%p DB=%@ Pragma checkpoint failed:%s ErrCode: %d.
responseEndTime
AVAssetDownloadURLSession does not support NSURLSessionUploadTask
AVAssetDownloadSessionMediaSelectionArrayKey
gs.apple.com
setup.icloud.com
Error
\r\n0\r\n\r\n
writeDBwithCachedResponse-ERROR: bind of key for item: %@
HTTPCookieStorage::setCookiesWithPolicies
NSAllowsArbitraryLoadsInWebContent
assetArtworkData
_offqueue_finalize
_owner != nil
kCFHTTPServerErrorDomain
RMD %@\r\n
setConnectionDelegate
networkServiceType
LocalTCPIOStreamTask.mm
<KerberosAccountStore@%p>
h2 headers
HTTPConnection.cpp
_offqueue_canRead
Cannot create task from nil request
NDNameKey
');
AssertType
 s:%c
data connection service type
challenge space %@
Request URL
Current Request
bad_function_call was thrown in -fno-exceptions mode
_kCFNetworkATSClientID
Q
kCFProxyHostNameKey
decodeAlert
Insufficient security
  
responseBodyTransferSize
There was a bad response from the server.
Err-1202
ERROR: shrinkDB - shrink of non file system cache did not fully complete.  Result: %d
sandboxExtWal
SHTTPConnectionCacheEntry.cpp
empty scheduling set being deallocated %p\n
EHA_LIT
Journal
com.apple.NSURLSession-delegate
Unsupported NSURLSessionConfiguration
HelloRequest
RL
} [%d:%d]\n
static const char *_PNAME<URLProtocol>::GET() [OBJTYPE = URLProtocol]
yyyy-MM-dd'T'HH:mm:ss.SSSZZZZZ
Library/Cookies
PRAGMA incremental_vacuum(10);
updateTCPAdaptiveParameters
v24@?0*8*16
kCFURLProtectionSpaceKeyServerType
Blocked
x-fb-debug
kConditionalConnectionIdentifier
{%s:%@}%@
kCFFTPResourceType
_timerStart
EHA_INDEXED_DYN
kCTDataConnectionServiceType
Protocol Received
%.3f seconds
HAR
lsqpack_dec_enc_in
ICI: max_acked %u is larger than number of inserts %u
cancelled %u header block%.*s of stream %llu
Already had something invalidating %@
<FTPStream %p>{%@, url = %@, flags = %p }
Cellular
%ld
https://%@:%@
writeDBwithCachedResponse-stored into DB FAILED-for item: %@. Error-code=%d
list
Cookie
PRIORITY
none
<?xml
Invalid Exception Format
Conflict
_version
RAW-READ
_kCFNBackgroundMetricsIsDiscretionary
textEncodingName
%@://%@%@%@
ERROR: NSURLStorageURLCacheDB _setDBSchema: DB=%@ response create - %s. ErrCode: %d.
com.apple.NSNetServices.tcplistener-queue
initializedWithAVAsset
-[__NSCFLocalSessionTask _private_onqueue_becomeStreamTaskWithCompletionHandler:]
Err-3006
_delegate_didCancel
_offqueue_open
Anonymous Self Signed certificate
\nCFNETWORK_ABORT: 
enc->qpe_cur_max_capacity
WebSocket tasks can only be created with ws or wss schemes
NSCFURLProtocolClient@%p:%p { %@ }
hostname
-[__CFN_SocksHandshake parse:len:completion:]
_delegate_conditionalRequirementsChanged
static const char *_PNAME<CFNNSURLRequest>::GET() [OBJTYPE = CFNNSURLRequest]
<CFNetworkWriteStream@%p>
AVAggregateAssetDownloadTask does not support currentRequest property
_kCFURLProtectionSpaceAuthenticationSchemeOAuthBearerToken
captureStreams
stopSecure
_kCFNTimingDataNStatCellRXPackets
_kCFNTimingDataResponseBodyBytesDecoded
EEA_DUP
st == LQRHS_ERROR
GOAWAY
com.apple.system.config.network_change
.0
v24@?0@\"NSObject<OS_dispatch_data>\"8@\"NSObject<OS_nw_content_context>\"16
-[NSNetService _internal_publishWithOptions:
-[__NSCFURLLocalStreamTaskFromDataTask connection:_conditionalRequirementsChanged:]
referer
read_ctx->hbrc_out.xhdr->val_offset >= read_ctx->hbrc_out.xhdr->name_offset
_nscfBridgeURLCacheStoreCachedResponse:forRequest:
CFURLDownload
CFNetwork Performance Diagnostic
%p for sockaddr %@
array [%d] {\n
_duetPreauthorized
_disablesNWLoader
__nsurlrequest_proto_prop_obj_23
com.apple.CFNetwork.ConnectionIdleAtSleepEvent
Connection Viability Changed
Evaluation
idleAtTime
expectedProgressTarget
boundInterfaceIdentifier
Bad certificate
__nsurlrequest_proto_prop_obj_12
kCFStreamPropertyFTPUsePassiveMode
_nscfBridgeURLCacheCopyResponseForRequest:
_isVaryHeaderSupportEnabled
can't obtain peer certs (%d)
_delegate_cacheTrifecta
kCFURLDownloadFileCreateDate
/tmp/PRIVATE_CACHE_HACK
[%llu] %s %s frame<length=%ld, flags=0x%x, stream_id=%d> error_code=%d
Open
socketstream
https://
_onqueue_setupStream_block_invoke
-[__NSCFURLLocalStreamTaskFromDataTask connection:request:needsNewBodyStreamFromOffset:callback:]
waitsForConnectivity
_nscfBridgeURLCacheSetMemoryCapacity:
NSAllowsArbitraryLoads
v24@?0{?=qi}8
_kCFNTimingDataLocalAddressAndPort
cleaned up
:scheme
421
received == len
Aug
requestStream
h2 trailers
fLoaderSchedulingSet && !fLoaderSchedulingSet->isEmpty()
com.apple.runtime-issues
Err-3000
TCPIOConnectionTest.hpp
fill: %.2f
kCFStreamPropertyFTPUserName
resumeURL
()<>@,;:\\\"/[]?={} \t
gz
Cannot move file
this queue = %s, this thread = %p, this mach thread = %u
NSURLSessionUploadTaskResumeData
INSERT OR REPLACE INTO alt_services(partition, host, alternateHost, port, alternatePort, type, creation_time, expires_time, rowid) \t\tvalues (?, ?, ?, ?, ?, ?, ?, ?, (SELECT max(rowid) FROM alt_services)+1)
kCFURLConnectionSocketStreamProperties
zero byte resource
CFNetwork _loaderInterface_rejectChallenge - Load %@ Challenge %@
OK
NSURLCredentialStorageChangedNotification
>
kCFURLDownloadResumeEntityTag
shared_tcpConnWorkQueue_Background
keys
<CFURLCredential %p>{OAuthToken = %@, persistence = %d}
OS_dispatch_data
Connection %llu
Could not connect to the server.
Err-1011
_receivedHeadersBlocked
additionalProperties
%@ { state %s }>
queue %p %s
host
The Internet connection appears to be offline.
\tpath:%@\n
v16@?0^{LoaderInterface=^^?}8
v16@?0r^{XURLCache=^^?}8
kCFURLRequestPreAuthXMMeAuthToken
new
__STORAGE_PARTITION_IDENTIFIER
CFNetDiagnostics
NSPinnedDomains
assumesHTTP3Capable
allowsExpensiveNetworkAccessKey
wrote ICI: count=%u
xhdr->flags & LSXPACK_NAME_HASH
\tports:{ %@ }\n
identifier
+[NSURLRequest getObjectKeyWithIndex:]
v16@?0^{SAwaitingTube=^^?^{__CFAllocator}iB^^?^{HTTPConnectionCacheKey}^{HTTPRequestMessage}^{MetaConnectionCacheClient}{MetaConnectionOptions=ifQCCCC}^{STube}dd}8
_kCFNTimingDataFetchStart
could not allocate hinfo for stream %llu
rinv
Library
HTTPNetStreamInfo.cpp
LocalDownloadFile.mm
CFNetwork _loaderInterface_useCredential - URLConnection timeout timer should restart here - Load %@ Challenge %@ Credential %@
_config
headersSize
s
bytes=
com.apple.CFNetwork.StorageDB
The requested URL was not found on this server.
<NetworkProxyCredential %p>{viability=%@, cred=%p}
{ Target path: %s, modTime: %@, size: %lld, st_uid: %d, st_mode: %o st_flags: 0x%x acl: %s parentInfo: %@ }
kCFURLRequestDoNotDecodeData
HTTPEngine
__nsurlrequest_proto_prop_obj_30
SELECT entry_ID from cfurl_cache_receiver_data WHERE isDataOnFS < 1 AND entry_ID in \t\t\t\t\t\t\t\t (SELECT entry_ID from cfurl_cache_response WHERE entry_ID > 0 ORDER BY time_stamp ASC LIMIT %d)
ERROR: NSURLStorageURLCacheDB deleteResponsesSinceDate: dbConnection=%p DB=%@ Select for FS data failed:%s ErrCode: %d.
SourceContext{ %@ callback %p(%p) }
%@: cannot convert nil to a TXT record.
com.apple.httpserver.byname-nw
closeRead
jumping back once we have streams
NSURLAuthenticationMethodDefault
v28@?0@\"<NDBackgroundSessionProtocol>\"8@\"NSDictionary\"16B24
<cookies not yet read>
resumableUploadData
q24@?0@\"NSHTTPCookie2\"8@\"NSHTTPCookie2\"16
bodySize
_requiresSecureHTTPSProxyConnection
if-modified-since
Use Credential
Moved Permanently
ended header for stream %llu; max ref: %u encoded as %u; risked: %d
redirection
NSURLDownloadDecoders
The server did not accept the certificate.
v32@?0@\"NSString\"8@\"NSArray\"16^B24
kCFURLProtectionSpaceKeyHost
trust
key->isCoalesced() == false
HTTP3Frame.mm
status == 0
Classic Stream Client <%p>
kCFURLProtectionSpaceKeyPort
ATS Resource Blocked
Err-1201.w
_kCFHTTPCookiePolicyPropertyIsTopLevelNavigation
<HTTPConnectionCacheEntry@%p>{\n
Value
X-MobileMe-AuthToken %@
setStreamID
The load of %@ is blocked by ATS policy.
data
SERVER_UP
_setupConnection
Err-1200
Coalescing
v16@?0@\"NSObject<OS_sec_protocol_metadata>\"8
consumeData
Only supported on background sessions
:method
HTTP2StreamEqualCallBack
NSProxyConnection.m
NSURLSessionDelegateImplementsSessionAuthChallengeKey
Certificate
   
com.apple.CFNetwork.har-capture-update
har-capture-amp
_kCFNTimingDataRequestHeaderSize
__nsurlrequest_proto_prop_obj_5
registerForPropertyUpdates
[%@]
Failure
~PerSide_CFWriteStream
STube
_explicitlySetATSContext
location
<CFCachedURLResponse %p [%p]>
Subject Sum
v16@?0@\"NSObject<OS_nw_error>\"8
<HSTSCache@%p> { %p }
^v16@?0^{__CFString=}8
cookie
EHA_INDEXED_STAT
header block for stream %llu is blocked
success
com.apple.CFURLConnectionSynchronous
*** -%s cannot be sent to an abstract object of class %s: Create a concrete instance!
disableRetry
user
!fTrailersBegan
UPDATE cfurl_cache_receiver_data SET receiver_data=%q, isDataOnFS=%q WHERE entry_ID=%q;
NSExceptionAllowsInsecureHTTPLoads
v32@?0^{__CFError=}8{shared_ptr<__CFDictionary>=^{__CFDictionary}^{__shared_weak_count}}16
ERROR: writeDBwithCachedResponse -bind Receiver-receiverData: %d\n
Unsupported certificate
sessionDescription
candidates[1]->ete_id > candidates[0]->ete_id
enc->qpe_hist_els
access-control-request-headers
CWD %@\r\n
nw
CFHTTPCookieStorageGetTypeID() is deprecated
persistent connection
<< DATA %@ >>
Connections: NULL
ERROR: NSURLStorageURLCacheDB _setDBSchema: DB=%@ index on request_key - %s. ErrCode: %d.
called removeCachedResponsesSince: subclass should implement
WINDOW_UPDATE
com.apple.security.get-task-allow
ServerTrustEvaluationRequested
apple.com
Dirty
bodyStartProvidingData
access-control-allow-credentials
Lost connection to background transfer service
request (%p) other than the current request(%p) signalled it was complete on connection %p\n
use cached response %@
consumeResponseHeaders
SELECT * from alt_services;
DELETE FROM alt_services WHERE (host = ? AND port = ?)
Opening
found != _transactions.end()
fSocketReadStream == NULL
kNetworkProxyAuthorizationElementsKeyClientProcessName
name hash: 0x%X; nameval hash: 0x%X
SETTINGS_MAX_HEADER_LIST_SIZE
FATAL: Failed to change priority.
Creating an AVAssetDownloadURLSession requires the com.apple.developer.media-asset-download entitlement
There was a problem establishing a secure tunnel through the web proxy server.
Connections: %ld
_onqueue_responseHeadersArrived
Permanent Redirect
fill: %.2f; effective fill: %.2f
An open requestBody stream is passed to CFReadStreamCreateForStreamedHTTPRequest()
CFObject.cpp
peer
EarliestBeginDate
strict
streamID > 0
kCFURLProtectionSpaceKeyRealm
apple-mapkit.com
NSURLDownloadBytesReceived
Mar
```
