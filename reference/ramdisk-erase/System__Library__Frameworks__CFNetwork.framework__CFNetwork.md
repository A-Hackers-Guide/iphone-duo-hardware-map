# `/System/Library/Frameworks/CFNetwork.framework/CFNetwork`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 6,652,352 bytes.

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
jul
Err-1202.w
rdar46818402
VaryHeader
Not Implemented
multipathServiceType
v16@?0@\"NSThread\"8
CoreSchedulingSet.h
_kTCPKeepAliveParametersIdleTime
  
failed array validation
<CFURLCredential %p>{Account = %@, persistence = %d}
NSURLDownload.mm
can't obtain peer certs (%d)
No Cellular
plist
_schedulingSet
Library/dafsaData.bin
proposed
qdec_header_process
fake://host/
see other
v24@?0r^{CompactCookieHeader=}8^B16
_owner != nil
_directoryForDownloadedFiles
Found
ConnectionProtocolGetInputFrames
HTTP2ConnectionCache.cpp
failed to initialize compression, error %ld
timeoutIntervalForResource
_alwaysPerformDefaultTrustEvaluation
DROP table IF EXISTS cfurl_vary_state;
nw_loader_third_party_apps
CertificateVerify
ftps
privacyStance
_kCFNTimingDataConnectEnd
index
state
oscar
Jul
AuthBrokerAgent Callback
_kCFHTTPCookiePolicyPropertyAllowOnlyPartitionedCookies
sqlite-wal
, 
NSURLAuthenticationMethodOAuth
mar
viable
DELETE
newTube->getType() == kSTubeTypeHTTP
SELECT * from alt_services WHERE host = ? AND partition = ? AND port = ? AND expires_time > strftime('%s','now')
NSUnbufferedIO
Connections: %ld
Attempted to set the shared cookie storage after it has already been faulted in!
EDT
scheduleAndOpenWithHandler
Connection Waiting
error != NULL
Gateway Time-out
(count % 2) == 0
v32@?0^{__CFHTTPMessage=}8@\"NSObject<OS_dispatch_data>\"16r^{?=qi}24
static const char *_PNAME<URLConnection>::GET() [OBJTYPE = URLConnection]
MSDOS-like directory output is on
kCFProxyTypeAutoConfigurationJavaScript
%@-%ld
!
Aug
<NetConnection@%p> { State = %s, Count = %d, requests = {
%.6d%.2d%.2lu
The certificate for this server is invalid.
^{__CFString=}8@?0
get, post, options
qenc_remove_from_risked_list
NSURLSessionResumeBytesReceived
kConditionalConnectionRequirementTimeWindowStartTime
age
EPSV\r\n
%@://%@%@%@
ERROR: NSURLStorageURLCacheDB _setDBSchema: DB=%@ table index on blob_data - %s. ErrCode: %d.\n
DELETE from cfurl_cache_blob_data WHERE entry_ID in (SELECT entry_ID FROM cfurl_cache_response WHERE time_stamp >= \"%s\")
bytes=
processRequest
v16@?0^{_CFURLCredential=}8
DashboardClient
receive
max-age=31536000
MetaConnectionCache<%p>
MIMEType
description
temporarily redirected
com.apple.runtime-issues
atsTrustPolicy
%s://%@/
Forced
<NetworkProxyAuthorizationElements %p>{cred=%@, protSpace=%@, challenge=%@ client=%@ <%@>}
_disablesNWLoader
100
no host header
AVAssetDownloadTaskMinimumRequiredPresentationSizeKey
<CFURLDownload %p [%p]> {connection = %@, path = %@, client = %p}
<CFNetworkReadStream@%p>
bad signature
(0x
Mac OS X Server
originalRequest
NSErrorPeerCertificateChainKey
Policy
_requiresPowerPluggedIn
DELETE FROM alt_services WHERE expires_time < strftime('%s','now')
\tname:%@\n
cookies_deleted_handler_queue_default
respondedToWillBeginDelayedRequestCallback
feb
kConditionalConnectionClientOptInDiscretionary
APSRelayTransaction
<CFHTTPMessageRef %p(%p)> { %s response, url = %@, status = %ld }
!ss->isEmpty()
_kCFNTimingDataRequestHeaderSize
_immediate_buffer_was_set
OriginURL
ServerHello
file
No
Read Stream PAC Timeout
\tversion:%ld\n
har-capture-pid-date
CFNETWORK_IO_LOG_STDOUT
_kCFNTimingDataNetworkProtocolName
h2 ping
gzip, deflate
_kCFStreamPropertyConditionalRequirementsChangedBlock called
NetworkStorageDB:openReadWriteConnection: failed to open read connection to DB @ %s.  Error=%d. Cause=%s
Requested range not satisfiable
chown
connection
allowsExpensiveNetworkAccessKey
SETTINGS
v16@?0@\"NSFileHandle\"8
clean
%s
NDProtocolKey
com.apple.CFNetwork.CacheDB-write
BEGIN IMMEDIATE;
v16@?0r^{XURLCache=^^?}8
ssl
success
Disk Cookies: { %@, %s %s %s }
dispatch_data_get_size(_dataBuffer) == _dataBufferSize
Apple Inc.
fill: %.2f
__nsurlrequest_proto_prop_obj_13
0x%04x
server
recommendedPolicy
<B 
Apple Global Domain
Certificate revoked
v16@?0^{_CFURLProtectionSpace=}8
SourceContext{ %@ callback %p(%p) }
Cookies
kCFFTPResourceMode
fatal
com.apple.CFNetwork-cc-%d-%lld
AVURLAssetDownloadTokenKey
Invalid Exception Format
ServerHelloDone
_inExpectedBytes != HEADERS_NOT_YET_CHECKED
_companionAppBundleIdentifier
EHA_LIT_WITH_NAME_STAT
ERROR: shrinkDB - shrink of non file system cache did not fully complete.  Result: %d
violationType
kConditionalConnectionRequirementDiscretionaryElevated
taskDescription
__nsurlrequest_proto_prop_obj_14
Mon
v32@?0@8Q16^B24
_kCFNTimingDataNStatWiredTXPackets
[%llu] %s
kCFStreamPropertyFTPFileTransferOffset
{ conn (%llu), local %s => peer %s %s }
NoORWECX
<CFURLDownload %p [%p]> {connection = %@, path = %@, client = %@}
v16@?0q8
FALSE
\r\n\r\n
February
com.apple.webapp
Include Subdomains
link
com.apple.CFNetwork.HSTS.DisableHSTS
RMD %@\r\n
C16@?0@\"BGSystemTask\"8
createTime
CFNetwork _loaderInterface_rejectChallenge - Load %@ Challenge %@
File
Email
\"%@\"
read stream status %s
v16@?0r^{CompactCookieArray=^^?^^?^{__CFData}}8
v16@?0@\"NSURLRequest\"8
got Header Ack instruction, stream=%llu
NetworkStorageDB:_openDBWriteConnections: failed to open write connection to DB @ %s.  Error=%d. Cause=%s
writeDBwithCachedResponse - Invalid protocol-property list - CFURLRequestRef. protoProps=%@
localEndpoint
!claimedByTube
alt-svc
effectiveConfig
%@:%@:%@:%s:%s
cachedResponse
Connection
kConditionalConnectionIsUpload
bytes in: %u; bytes out: %u, ratio: %.3f
from existing connection
NSExceptionDomains
Log file '%s' created
%@/%s
<!--
<AuthenticationInfo@%p>{%s - Valid(%c) Authenticated(%c) ConnAuth(%c)}
_readEOF
Summary
runloop went to finished
Better Route Detected
text
bytes
UIApplicationDidEnterBackgroundNotification
_delegate_willSendRequest
_dataBufferSize <= _maxReadCount
_allowsHSTSWithUntrustedRootCertificate
name hash: 0x%X; nameval hash: 0x%X
EEA_INS_NAMEREF_DYNAMIC
Original Request
-[__CFN_SocksHandshake parse:len:completion:]
_preventsSystemHTTPProxyAuthentication
systemgroup.com.apple.nsurlstoragedresources
_nscfBridgeURLCacheSetMemoryCapacity:
No certificate
Internal error\tfatal
PORT %u,%u,%u,%u,%u,%u\r\n
received == len
OPTIONS
v60@?0B8{shared_ptr<__SecTrust>=^{__SecTrust}^{__shared_weak_count}}12{shared_ptr<const __CFArray>=^{__CFArray}^{__shared_weak_count}}28{?=qi}44
connectionProxyDictionary
needs proxy
too many HTTP redirects
\tisSecure:%@\n
SocketStream IO Logging
_ignoreDidReceiveResponseDisposition
APSRelaySucceeded
MobileSafari
urlstring
basePriority
AwaitingTube.h
_http._tcp
waitsForConnectivity
responseBodySize
_nscfBridgeURLCacheSetDiskCapacity:
Upload tasks from NSData are not supported in background sessions.
v24@?0^{__CFString=}8^{__CFArray=}16
h2 frame
pathToDownloadTaskFile
lighttpd
 p:
NSURLSessionSourceApplicationBundleIdentifierIsExternal
request timed out
uploading
{%s:%@}%@
CountOfBytesClientExpectsToSend
Bearer %@
com.apple.cfnetwork.ats.metrics
'
-[__NSCFURLLocalStreamTask _onqueue_processWriteWork:]
Connection Ready
%.5fs
com.apple.CFNetwork.LogSink[%s]
\nCFNETWORK_ABORT: 
_onqueue_newTubeReady_block_invoke_3
updatedStreamingZipModificationDate
_kCFNTimingDataNStatRXDuplicateBytes
AVAggregateAssetDownloadTaskIdentifierKey
DROP table IF EXISTS cfurl_cache_receiver_data;
ls.apple.com
%@ }\n
CFNetworkConnection-%u
__nsurlrequest_proto_prop_obj_28
-[__NSCFTCPIOStreamTask _onqueue_ioTick]
h2 trls
empty
allocated xhdr size (%zd) is smaller than requested (%zd)
expectation failed
TransportConnection.cpp
_kCFNTimingDataConnectionInterfaceIdentifier
clear
B16@?0@\"NSObject<OS_nw_interface>\"8
HasSZExtractor
usedTFO
_offqueue_read
RunloopBlockContext
[%llu] (last_stream_id=%d, error_code=%s(%d), opaque_data_len=%zu)
v32@?0@\"NSString\"8@\"NSString\"16@\"NSString\"24
_kCFNTimingDataSubflowCountsAtStart
_preventsAppSSO
EEA_INS_LIT
v12@?0C8
_offqueue_write
SameSite
SELECT receiver_data, entry_ID from cfurl_cache_receiver_data WHERE isDataOnFS > 0 AND entry_ID in \t\t\t\t\t\t\t\t (SELECT entry_ID from cfurl_cache_response WHERE entry_ID > 0 ORDER BY time_stamp ASC LIMIT %d)
v20@?0^{_CFURLCredential=}8B16
_readBodyStart
Err-1004
can't load from network
Port
HTTPDigest
Bad record MAC
HTTPHeaderDict
(unsigned) (p - dst) == len_size + enc_size_bytes
set-cookie
requestBody
Tuesday
v16@?0@\"_DASActivity\"8
Already had something invalidating %@
, cnonce=\"%@\", nc=%08lx, qop=\"%@\"
UPDATE cfurl_cache_response SET version=%q, hash_value=%q, storage_policy=%q, partition=%q\t\t\t\t\t\t\t\t\t WHERE entry_ID=%q;
hsts_identifier
Cellular
Err-1019
SPI %s on longer supported
_kCFNetworkHSTSExpiry
fSocketWriteStream == NULL
stream
%02X
B32@?0@8@16^B24
websocketCloseWithCodeAndReason
this queue = %s, this thread = %p, this mach thread = %u
Switching Protocols
!_apsDelivery
<ActualCredentialStorage@%p<%p> { session %p, persistent %p }
Task: %p
CFNETWORK_IO_LOG_FILE
requested range not satisfiable
%lx
safeparent
could not find header block to continue reading
IsRequest
0
NSURLDownloadBytesReceived
HTTP3Stream.mm
_delegate_didReceiveDataArrayWithDataArray
_plusOneForFirstTube
fSchedulingSet
kCFFTPResourceName
ETA_NEW_NAME
NDBackgroundSessionManagerKeySessionUUID
_onqueue_setupStream_block_invoke
HTTPConnectionCacheEntry
CREATE INDEX receiver_data_index ON cfurl_cache_receiver_data(entry_ID);
com.apple.CFNetwork.report_networkscore_metrics
%@ { state %s, chunk state %s  }>
_readFinalized && _writeFinalized
Value
:status
CoreSchedulingSet<%p> { %s }
decoded_val
%@ token=%@
WONR.alloced_len >= WONR.str_len
com.apple.CFNetwork.defaultStorageSession
\r\n%X\r\n
cookie
%25
Oct
EST
<request@%p>
apache
_waitingBodySize == 0
v16@?0@\"BGNonRepeatingSystemTask\"8
INSERT into cfurl_cache_response (version, hash_value, storage_policy, \t\t\t\t\t\t\t\t\t request_key, partition) VALUES (%q, %q, %q, %q, %q);
CantCreateWriteStream
AVAssetDownloadChildDownloadSessionIdentifier
identifier
_duetPreauthorized
):
CFHTTPCookieStorageRemoveObserver
firstOnConnection
gz
The server \"%@\" requires a client certificate.
temporaryDestinationURL
END_HEADERS
SITE TRUTH ON\r\n
Err-999
Location
Upload
captureStreams
NSKeyedArchiveRootObjectKey
com.apple.CFNetwork.HTTP3ServerProtocolViolation
%p for sockaddr %@
__kCFStreamPropertyInternalHostlessKey
HSTS Host
0123456789abcdefghijklmnopqrstuvwxyz
kCFStreamPropertyFTPFetchResourceInfo
dataTransferReport
Err-1000
Err-1018
destinationURL
new_cookie_storage
%u
CoreStreamOpenBlocking
v20@?0B8@\"NSObject<OS_xpc_object>\"12
uniqueIdentifierUUID
AVAssetDownloadConfiguration
NSURLSessionTaskOriginalStartTimeKey
_pendingResponseBytes == nil
qdec: warn: 
%@ (%@)
Failed to query AuthBrokerAgent
har-body-size-limit
CFNetwork Performance Diagnostic
h2 flgs
space
kCFURLProtectionSpaceKeyPort
uniqueIdentifier
com.apple.CFNetwork.HARLogging
rl = %@, performCount = %lld
HTTP2MetaNetStreamInfoForwarder
proxy authentication required
<write side %p to stream %p>
com.apple.CFNetwork.ConnectionIdleAtSleepEvent
fClientCertChallengeCompletion == nullptr
kCFStreamPropertyFTPProxy
__STORAGE_PARTITION_IDENTIFIER
early-data
com.apple.CFNetwork.HTTPHeaderName
User cancelled\tfatal
-[NSURLDownload setDestination:allowOverwrite:]
METRIC_DATE
userinfo
not found
%.2x
expectedContentLength
%@-%d
NSURLAuthenticationMethodPrivateAccessToken
discretionary
 { Status Code: %ld, Headers %@ }
%ld
The certificate for this server was signed by an unknown certifying authority.
_enablesL4SInternal
HTTP2ConnectionCacheEntry
\tvalue:%@\n
mimeType
cfurl_cache_blob_data
Cookie_%d_%p
SessionIdentifier
cannot decode content data
PRAGMA wal_checkpoint;
%@:%@:%@
_onqueue_newTubeReady
uploadData
\xff\xdf\xdf\xdf\xdf\xff
<URLConnectionClient@%p>
URLConnectionClient.cpp
There was a problem establishing a secure tunnel through the web proxy server.
-[__CFN_SocksHandshake finish:]
trackerContext
v36@?0@\"NSObject<OS_dispatch_data>\"8@\"NSObject<OS_nw_content_context>\"16B24@\"NSObject<OS_nw_error>\"28
accept-language
Last Sync
_setupConnection
_allowTCPIOConnectionStreamTask
_explicitlySetATSContext
HTTPEnable
ipAddressWithPolicyId_block_invoke
http://%@/
needClientCert
com.apple.cfnetwork.cfnetworkagentclient
-[NSURLCache _initVaryHeaderEnabledWithPath:]
allowedProtocolTypes
init_with_task
None
cancel called for rl %p, mode %@
%s %s continuation
v28@?0B8@\"NSDictionary\"12@\"NSURLRequest\"20
+[NSURLResponse getObjectKeyWithIndex:]
initial
/%@
DispatchHost<%p>
no-cache
http://%@:%d
SETTINGS_INITIAL_WINDOW_SIZE
isHTTP
_engine
-[NWStreamPair _onqueue_writeData:outError:]
REL
T
!_inData
kSTubeTypeHTTP
Internal consistency check error for http request %p
qos
strongConn
/%@/%@
_prohibitEncryptedDNS
LIST\r\n
SIZE %@\r\n
NotOpen
appleid
<HSTSPolicy@%p <%p>> { HSTSCache=%p }
v16@?0^{BaseAwaitingTube=^^?^{__CFAllocator}iB}8
com.apple.network.AppTransportSecurity
start
[%llu] %s %s frame<length=%ld, flags=0x%x, stream_id=%d> error_code=%d
_metaClientCallback == NULL
Failure
cleaned up
_nscfBridgeURLCacheStoreCachedResponse:forRequest:
!_connection
consumedSize == dataSize
ClassicDelegateHolder
Redirection
<%d cookies in %d domains>
static const char *_PNAME<CFNNSURLRequest>::GET() [OBJTYPE = CFNNSURLRequest]
Close notify
_writeBuffer == NULL
varnish
HTTPServerConnection.cpp
WebSocket tasks are not supported in background sessions
Connections: NULL
com.apple.CFNetwork.CookiesChanged.%@
\tfUnAuthConns(%ld) = {\n
access-control-allow-origin
__nsurlrequest_proto_prop_obj_30
payloadTransmissionTimeout
Expires
v16@?0@\"NSURLSessionConfiguration\"8
<BODY 
Connection Properties
completed
Cannot create file
Request-URI Too Large
_request
new
425
SETTINGS_MAX_CONCURRENT_STREAMS
AVAggregateAssetDownloadTask does not support currentRequest property
%@/Cache.db
+
!_outCB
unacceptable
lastResponse
v16@?0@\"NSObject<OS_nw_array>\"8
com.apple.WebKit.Networking
kConditionalConnectionRequirementDownloadBytes
dispatch_data_get_size(data) > 0
source was canceled
h2 trailers
Authentication Challenge
Attempted to set the shared CFHTTPCookieStorage after it has already been faulted in!
send
upload resumption
CFNetDiagnosticCreateWithURL
TRACE
No Content
max-age=0
CFURLConnectionClient[%@]
application/javascript
DROP TRIGGER IF EXISTS cfurl_vary_state_delete;
NSURLSessionDownloadTaskResumeData
not scheduled
-[__NSURLSessionLocal _request:isCacheEquivalentTo:]
CREATE INDEX proto_props_index ON cfurl_cache_blob_data(entry_ID);
%@ { service name='%@', type='%@', port=%@> }
ProxyAutoConfigJavaScript
 s:%c
kCFURLDownloadResumeBytesReceived
_atsContext
B24@?0Q8@\"NSObject<OS_nw_object>\"16
ERROR: _purgeAllFileSystemCacheData - failed to get the path to the FS cached data at %@
%x\r\n
ConnectionProtocolGetOutputFrames
GOAWAY
h3
NSURLConnection-%d
new_entry->ete_id > enc->qpe_cur_header.hinfo->qhi_max_id
<AppSSOProtocol instance %p>
MDT
outbound control
countOfBytesSent
com.apple.cfnetwork.cfnetworkagent
_kCFNetworkATSClientID
_kCFNetworkHSTSPreloaded
cacheLookupBeginTime
_reusedAfterTime
CREATE TABLE IF NOT EXISTS alt_services (\t\tpartition text NOT NULL,\t\thost text NOT NULL,\t\talternateHost text NOT NULL,\t\tport int NOT NULL,\t\talternatePort int NOT NULL,\t\ttype int NOT NULL,\t\tcreation_time int,\t\texpires_time in
UNEXPECTED: close of sql read connection result=%d
i <= [_pendingWork count]
<File protocol instance %p>
_kCFNTimingDataNStatWifiRXPackets
AVAssetDownloadSessionLinkAssetURLToDestinationURLKey
DELETE from cfurl_cache_blob_data WHERE entry_ID=%s;
kCFProxyTypeAutoConfigurationURL
Continue
access-control-request-headers
newWriteStream
idleDuration
Creating an AVAssetDownloadURLSession requires the com.apple.developer.media-asset-download entitlement
%@: cannot publish an NSNetService created for resolution.
kCFFTPResourceSize
_kCFNTimingDataDomainLookupEnd
schedulingTier
_nscfBridgeURLCacheCurrentMemoryUsage
CFURLAuthChallenge
localizedDescription
NAMESERVER_DOWN
processHeader
niap_removes_builtin_ats_exceptions
called removeCachedResponseForRequest: subclass should implement
max-age=31536000; includesubdomains; preload
__nsurlrequest_proto_prop_obj_9
PWD\r\n
%@ is not a valid file:// url
ERROR: unable to get the receiver data from the DB!
remoteEndpoint
unlink
_kCFNTimingDataNStatVarRTT
__nsurlrequest_proto_prop_obj_21
HTTP2Connection<%p>
A data connection is not currently allowed.
updateTCPAdaptiveParamters
protocol
_kCFNTimingDataTotalBytesReceived
DafsaData
Feb
scoped interface
!fTrailersBegan
\r\n
*** -%s cannot be sent to an abstract object of class %s: Create a concrete instance!
%@:%@:%08lx:%@:%@:%@
<CFNetworkWriteStream@%p>
privacyProxyFailClosed
table size actual: %u; exponential moving average: %.3f
__nsurlrequest_proto_prop_obj_16
__hhaa__
h2
oauthtoken
enc->qpe_cur_max_capacity
task success
protocolProperties
SSLSetPSKIdentity returned %d
<NSHTTPCookieStorage cookies count:%ld>
lsqpack_enc_int
PING
__Secure-
NSURLDownloadBinHexCRC
HSTSCache
UUID
HTTPProtocol
v16@?0@\"NSData\"8
CachePolicy
corrupt?
accept-encoding
//
SSLSetPSKSharedSecret returned %d
NSRequiresNIAPTLSPackageVersion
   
b
CFN_USE_HTTP2_CONNECTION_COALESCING
blocked
get_dst
%s: no longer implemented and should not be called
unknown error
ident
%@: %@\r\n
precondition failed
attributes
storage
kCFHTTPAuthenticationAccountDomain
_onqueue_informationalResponseArrived
DELETE FROM alt_services WHERE (host = ? AND partition = ? AND port = ? AND type = ?)
kCFStreamPropertyStreamLength
https://%@:%d/
use cached response %@
-[__NSCFURLLocalStreamTask _onqueue_ioTick]
CFError { %@, %ld }
_version
$archiver
__kCFStreamPropertyCoalescingDomainSSLSettings
forCache
_onqueue_scheduleIO
v16@?0^{__CFReadStream=}8
application/json
newVaryState is nil
last-modified
Result
needs offset
v16@?0@\"NSDictionary\"8
June
<HTML 
backgroundTrailers
_kCFNTimingDataResponseBodyBytesReceived
NSURLSessionResumeInfoVersion
v28@?0c8@\"NSObject<OS_nw_endpoint>\"12d20
_kProxySupportSyncPACExecutionRunLoopMode
Diagnostics
no-store
_kCFNTimingDataResponseHeaderSize
qenc_add_to_risked_list
created
ioLogger
DELETE from cfurl_cache_response WHERE time_stamp >= \"%s\"
(Request) %@\n(Response) %@\n(Fetch Start) %@\n(Domain Lookup Start) %@\n(Domain Lookup End) %@\n(Connect Start) %@\n(Secure Connection Start) %@\n(Secure Connection End) %@\n(Connect End) %@\n(Request Start) %@\n(Request End) %@\n(Response
redirected to nowhere
v20@?0B8@\"NSDictionary\"12
com.apple.CFNetwork.CustomProtocols
KEYCHAIN_LABEL_FORMAT%@%@
v40@?0{shared_ptr<HTTPResponseMessage>=^{HTTPResponseMessage}^{__shared_weak_count}}8{?=qi}24
kCFStreamPropertyFTPResourceSize
program: %s; %s; %s; flags: 0x%X
!_schedulingSet
NSURLSessionResumeInfoTempFileName
_TLSMinimumSupportedProtocolVersion
custom
resourceForkData
referer
TimeoutActionTurnOff
Connection Established
Create Time
_precisionPreservingTimings
_nscfBridgeURLCacheRemoveCachedResponseForRequest:
copyProperty
NSServerConfigurationOutboundConnectionProxyDictionary
_receivedHeadersDone
_kCFNTimingDataConnectionPeerAddress
responseEndTime
v24@?0{shared_ptr<HTTPResponseMessage>=^{HTTPResponseMessage}^{__shared_weak_count}}8
%.*s %s %s
isEphemeralSession
quic_vle_decode
Ephemeral sessions must use ephemeral HSTS storage.
header_out_begin_dynamic_nameref
sharedCaches
fDQ
EEA_INS_NAMEREF_STATIC
about
<TITLE 
Err-1002
Localizable
kConditionalConnectionInTransitionalDiscretionaryPeriod
Embrace.framework
\t},\n
+backgroundSessionConfiguration: is deprecated. Please use +backgroundSessionConfigurationWithIdentifier: instead
_kCFURLProtectionSpaceAuthenticationSchemeOAuth
ERROR: NSURLStorageURLCacheDB deleteResponsesSinceDate: dbConnection=%p DB=%@ Delete failed:%s ErrCode: %d.
all
OK
origin
NSURLSessionDownloadURL
PDT
service
v20@?0^{__SecTrust=}8I16
DV
v16@?0^{__CFRunLoop=}8
assetOptionsPlist
RLF
length <= bufLen
unknown_host
ERROR: NSURLStorageURLCacheDB deleteAllResponses: dbConnection=%p DB=%@ Truncate Database failed:%s ErrCode: %d.
_TLSMaximumSupportedProtocolVersion
Blocked
manager
idleAtTime
continue
_tlsProcessSaveHandshakeProperties
http/1.0
fProtocolHandler == NULL
decodeAlert
false
CFNetwork.f
CFURLDownload
Coalescing
kCFErrorDomainWinSock
com.apple.cfnetwork.altservicesstorage
error.error != 0
_kCFStreamErrorDomainKey
_kCFNTimingDataTimingDataInit
PATCH
icmp
Negotiate %@
forbiddenProtocols
_neverDecrementedPlusOneForFirstTube
header_out_write_value
x-content-type-options
SELECT * from cfurl_vary_state where request_key=\"
Could not communicate with background transfer service
Err-1020
Err-1203
v24@?0^{__CFString=}8^{__CFString=}16
kConditionalConnectionRequirementUploadBytes
Forbidden
-[_NSCFTranslatedFileURLProtocol initWithRequest:cachedResponse:client:]
CoreStreamBase<%s>(%p %s)
<KerberosAccountStore@%p>
NetworkStorageURLCacheDB-openCacheDB: size of DB specified too small (%ld).  No persistent DB opened at %@.
<CFNAccountKerberos@%p>
h2     
{ Can't stat: %s, errno: %d parentInfo: %@ }
no cellular
Path
NSTemporaryThirdPartyExceptionAllowsInsecureHTTPLoads
fSocketReadStream == NULL
kCFHTTPServerAllowAnonymousServer
NewStateState
NSProxyConnection.m
bad count
Wednesday
The request timed out.
HTTPServer
_allowsVirtualInterfaces
application/dns-message
_kCFNTimingDataConnectionStopTimeCounts
v20@?0i8@\"NSObject<OS_nw_error>\"12
%@,%@
cfurl_cache_receiver_data
v24@?0@\"NSURLConnection\"8@16
.
v24@?0^{__CFArray=}8^{__CFError=}16
allowsExpensiveNetworkAccess
ATSAllowsLocalNetworking
consumeResponseHeaders
httprequest
HSTS.plist
D
httpMessage
_sessionSendsLaunchOnDemandEvents
begin reading header block for stream %llu
v24@?0@\"NSObject<OS_tcp_connection>\"8@\"NSObject<OS_dispatch_queue>\"16
%@://%@:%d%c%@
%PDF-
v24@?0r^v8^v16
_performsEVCertCheck
set
_delegate_needNewBodyStream
v16@?0^{LoaderClientInterface=^^?}8
NSURLSessionTaskStateCanceling
APSRelayTopic
CFNetwork
BAD
SITE DIRSTYLE\r\n
<%@ %p> %@ (%@ %@)
audit
SocksHandshake.m
DROP table IF EXISTS cfurl_cache_schema_version;
Ephemeral %@
_NSURLResponseType
_connectionWorkQueueSuspensionCount >= 0
CFNetworkHTTP3Override
%p -- keeping alive
CREATE INDEX time_stamp_index ON cfurl_cache_response(time_stamp);
DELETE from %s WHERE entry_ID in (%s)
content-type
EHA_INDEXED_DYN
<CFCachedURLResponse %p [%p]>
v24@?0{shared_ptr<AuthenticationState>=^{AuthenticationState}^{__shared_weak_count}}8
UIApplicationSuspendedNotification
failed to make array
firstWaiter != NULL
read_ctx->hbrc_out.xhdr->val_len >= off
NSURLDownloadBinHexEncodedData
True
_kCFHTTPCookiePolicyPropertyIsSafeRequest
error
v20@?0C8^{__CFString=}12
Cannot read file at %@
true
cannot parse response
Request
sendEOF
waiterTube
Export restriction
CFNETWORK_IO_LOG_STDERR
post
max-age=31536000; includesubdomains
_nsurlsessiondErrorDomain
v16@?0^{__CFDictionary=}8
v20@?0@\"NSObject<OS_dispatch_data>\"8i16
_state == State::EnqueuedOnConnection
_kCFNTimingDataNStatRXOutOfOrderBytes
null
requestBodySize
_kCFHTTPCookiePolicyPropertyIsTopLevelNavigation
ATSAllowsArbitraryLoads
+[NSNetService dataFromTXTRecordDictionary:]
%@ %@://%@/<redacted>
%@%@%@
EHA_LIT_WITH_NAME_NEW
server error
kCFProxyTypeKey
writeDBwithCachedResponse-ERROR with UPDATE for item: %@.  Error-code:%d
error != NULL && atEOF != NULL
%s %s %ld
double lit would result in ratio > 0.95, reset
Response Complete
s
response
connectionCacheTypeForTubeType
.tmp
{CGSize=dd}
_invokeCB
CFNetwork Self Signed Certificate
Viable
Err-1007
Err-1200
WriteStream
Friday
-[__NSCFLocalDownloadFile captureFile:outStat:]
transactionMetrics
_offqueue_canRead
v16@?0^{_CFCachedURLResponse={__CFRuntimeBase=QAQ}^{__CFCachedURLResponse}}8
kCFFTPStatusCodeKey
nginx
strict-transport-security
<FTPStream %p>{%@, url = %@, flags = %p }
Err306
%@: cannot convert nil to a dictionary.
v40@?0@\"__NSCFLocalDownloadTask\"8@\"NSURL\"16@\"NSURLResponse\"24@\"NSError\"32
scheme
\t[%ld]: Tube(%p) - Waiter(%p) Client(%p) Request(%p, %@) Auth(%@)
CFNetwork Diagnostics [%d:%d] %s {\n
timeoutIntervalForRequest
aug
cfurl_cache_response
_processResponse
yes
_config
(avail_bits & 7) == 0
\"\"
kCTDataConnectionServiceType
Apr
v32@?0r*8S16S20S24S28
<NetworkProxy %p>{host = %@, port=%d, user=%@, pass=%@, type=%@, CONNECTProperties=%@, transparent=%s}
Invalid stream ID %llu in Cancel Stream
NSURLDownloadEntityTag
v60@?0{FrameMetadata=QQQ}8@\"NSObject<OS_dispatch_data>\"32B40{?=qi}44
fd
_delegate_didReceiveResponse
ConditionalConnectionSIMSupport.cpp
responseBeginTime
_kCFHTTPCookiePolicyPropertySiteForCookies
file-read-data
vary
_kCFNetServiceMonitorBlockingMode
%p for netservice %s %s %s
DELETE from cfurl_cache_receiver_data WHERE entry_ID in (SELECT entry_ID FROM cfurl_cache_response WHERE time_stamp >= \"%s\")
B24@?0r*8@\"NSObject<OS_xpc_object>\"16
com.apple.DispatchHost
dns
Did Timeout
%@: 
strict
%@ %@\n
_onqueue_enqueueRequestForProtocol
Pending Tubes: %ld
key
kCFNetworkAgentXPCMessageTypePACQuery
v16@?0^{ConnectionClientInterface=^^?}8
path not determined
HTTP2StreamBridge
_ATSHasAppleBundleException
com.apple.cfnetwork.cookiestorage
jumping back once we have streams
CFRunLoopGetCurrent = %@
content
%@ - PENDING %s
prog.ep_hea_action == EHA_LIT_WITH_NAME_STAT
NSURLDownloadBinHexFirstCRCByte
AssertLevel
completeTime
PUT
_NSURLErrorRelatedURLSessionTaskErrorKey
called storeCachedResponse:forRequest: with nil request
Custom subclasses of NSURLRequest are not supported in background sessions. Attempted to use a request of class %@
responseUnblocked
multiple choices
 path:\"%@\"
ERROR: NSURLStorageURLCacheDB _setDBSchema: DB=%@ pragma wal enable - %s. ErrCode: %d.
HTTPTransaction.cpp
(Task Interval) %@\n(Redirect Count) %lu\n(Transaction Metrics) %@
__nsurlrequest_proto_prop_obj_8
com.apple.CFNetwork.ForceIOPath
v24@?0^{__CFError=}8d16
301PermMove
Name: %@, Persistence: %s
Err-1205.w
;
kTubeTypeHTTP
Peer certificate
com.apple.cfnetwork.httpserver-connection-queue
AddCookies Continue
AcceptPolicy
NTLM %@
.local.
<HEAD 
ix%ld
v40@?0^{__CFString=}8^{__CFArray=}16^{__CFData=}24^{__CFString=}32
Cookie
_kCFNTimingDataRequestEnd
Sunday
The load of %@ is blocked by ATS policy.
\t\t%d: %@ ,\n
client
_longLivedConnectionCachePurgeTimeout
com.apple.CFNetwork.HTTPFallbackHost
!_inCBData
False
Unknown CA
kNetworkProxyAuthorizationElementsKeyClientDescription
cancel
queue %p %s
.localhost
_batchedStreamData.size() == 0
PRAGMA auto_vacuum = 2;
Err-1203.w
Cancel
conn
writeDBwithCachedResponse-stored into DB FAILED-for item: %@. Error-code=%d
websocket
_kCFNTimingDataTCPInfoAtStart
_prefersInfraWiFi
no error
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-_[]:
_isVaryHeaderSupportEnabled
CREATE TABLE IF NOT EXISTS cfurl_vary_state(request_key TEXT PRIMARY KEY UNIQUE, vary_state TEXT, time_stamp NOT NULL DEFAULT CURRENT_TIMESTAMP);
background_session_bgst
Name
_kCFNTimingDataNStatMinRTT
APSRelayTransaction.cpp
kCFHTTPServerRequestHeaderOrder
_kCFNTimingDataLocalAddressAndPort
cancel header block for stream %llu, seqno %u
NEW CONNECTION
com.apple.__NSCFLocalDownloadFile
%s errno %d cferror %@ ep %s line %d path %s
kCFHTTPAuthenticationUsername
CFNETWORK_HAR_BODYSIZELIMIT
Connection Failed
!_inCBHeaders
spaces
withExistingProtocolAsync
_onqueue_getTransactionItr
STOR %@\r\n
!0
ERROR: failed to write cached response to %@. Falling back to old persistent store mechanism.
~HTTPServerConnection
h2 stgs
request
TimeoutAction
creationTime
Decrypt error
_onqueue_requestIsChunkEncoded
_kCFNTimingDataInternalTransactionMetrics
EEA_NONE
fSocketStream == NULL
Jun
TCP Connection Failed
GIF89a
_connectionWasLost
RAW-READ
got TSU=%llu
circLock
writeDBwithCachedResponse-ERROR: NO key for item: %@
AssertName
smtp
kCFNetDiagnosticPingOptionDataLength
Binary{ %@ }
(_state == State::WaitingToEnqueue) || (_state == State::Canceled) || (_state == State::Error)
accept
textEncodingName
Sun
_canHandleRequest
Default
_delegate_willSendRequestForEstablishedConnection
403
NSThirdPartyExceptionRequiresForwardSecrecy
%@ { state %s - COMPLETED, expected body length %ld  }>
_kCFNTimingDataDomainLookupStart
EarliestBeginDate
invalidateAsync_block_invoke
kCFHTTPServerFailingResponse
!6\xf0%
Use Proxy
INSERT OR REPLACE INTO cfurl_vary_state(request_key, vary_state) VALUES ('
Err-3004
read stream error { %ld, %d }
}\n
unsupported media type
CFAllocatedReferenceCountedObject
text/plain
_ioConn
-[__NSCFLocalSessionTask _private_onqueue_becomeStreamTaskWithCompletionHandler:]
_kCFStreamStatsDNS_ResolutionTimeMs
readResponse
Accessing
status
Err-1205
base
READ
Non-descript-key
_kCFNTimingDataResponseBodyBytesDecoded
%@, ALPN supported %@, Tube type: %@
_readHeadersDoRead
AppSSO chose not to manage url
com.apple.nsurlsessiond-events
Payment Required
kCFStreamPropertyFTPUsePassiveMode
_nscfBridgeURLCacheMemoryCapacity
kCFURLRequestAllowAllPOSTCaching
method
_sourceApplicationBundleIdentifier
HTTP Transactions
%s @ %p, version %2.2x, length %d
_readBufferConsume
Closed
enqueue
_kCFNTimingDataNStatConnectAttempts
EEA_DUP
text/html
requestStream
\t[%ld]: NULL
ATSExceptionDomains
ORWEDM
dispatchData == nullptr
<CFURLCredential %p>{ accepted server trust }
%#?:;/@=&[]
%@ Failure: %s
LocalDownloadTask.mm
_
sourceApplicationBundleIdentifierForMobileAsset
Error
-[NWStreamPair _onqueue_readToBuffer:length:outError:outEOF:]
_preventsDirectWiFiAccess
content-disposition
bad_weak_ptr was thrown in -fno-exceptions mode
(unknown version)
kNSNetServiceBrowserIncludesAWDLKey
-[__NSCFURLLocalStreamTaskFromDataTask connection:didReceiveInformationalResponse:]
objects
<HTTP request stream %p>{url = %@, flags=%p, connection stream = %p}
HTTPS
firstResumeTime
CREATE table cfurl_cache_receiver_data(entry_ID INTEGER PRIMARY KEY, isDataOnFS INTEGER, receiver_data BLOB);
HTTPCookieStorage::setCookiesWithPolicies
!_connectionParams
fSchedulingSet->currentlyInContext()
ftp
NWIOConnection %p
<A 
NDBackgroundSessionManagerRestoredStateKeyTLSSessionCachePrefix
Wed
HTTPStorages
kConditionalConnectionRequirementPowerPluggedIn
v16@?0^{SNetConnectionAuthEntryThing=^^?^{__CFAllocator}i^{HTTPNetConnection}^{_CFHTTPAuthentication}^{_CFHTTPAuthentication}}8
!delegate
_allowsResponseMonitoringDuringBodyTranmission
__nsurlrequest_proto_prop_obj_25
v32@?0@\"NSNumber\"8@\"__NSCFURLSessionTaskInfo\"16^B24
allowsPersistentDNS
range
com.apple.CFURLConnectionSynchronous
NSErrorClientCertificateChainKey
h2 hdrs
INSERT into cfurl_cache_blob_data (entry_ID, response_object, request_object,\t\t\t\t\t\t\t\t\t proto_props, user_info) \t\t\t\t\t\t\t\t\t VALUES (%q, %q, %q, %q, %q);
\xe1\"
originload
EHA_LIT_WITH_NAME_DYN
task failure
com.apple.nsurlsessiond.started
NetworkStorageURLCacheDB-openAndPrepareWriteCacheDB_NoLock: size of DB specified too small (%ld).  No persistent DB opened at %@.
BEGIN IMMEDIATE
NSHTTPCookieAcceptPolicy
v32@?0@8@16^B24
November
The resource could not be loaded because the App Transport Security policy requires the use of a secure connection.
kCFStreamSSLAllowsExpiredRoots
_kCFStreamPropertyHTTPFilterEstablishedConnectionBlock called
UPDATE cfurl_cache_receiver_data SET receiver_data=%q, isDataOnFS=%q WHERE entry_ID=%q;
CantOpen
<HSTSCache@%p> { %p }
ERROR: NSURLStorageURLCacheDB deleteResponsesSinceDate: dbConnection=%p DB=%@ Select for FS data failed:%s ErrCode: %d.
ESF
COMMIT TRANSACTION
Only supported on background sessions
encode `%.*s': `%.*s'
[%llu] (error_code=%s(%d))
Err-1011
CFN_USE_HTTP2
[NSURLSession sharedSession] may not be invalidated
PRIORITY
__nsurlrequest_proto_prop_obj_0
%@ data [ %d ] bytes {\n
13
%@, %@
v16@?0i8B12
<CFHTTPAuthentication %p>{state = %s; scheme = %@, forProxy = %s}
countOfBytesExpectedToSend
initializedFromToken
_taskUUID
com.apple.private.cfnetwork.har-capture-amp
SOCKS
::1
v28@?0@\"<NDBackgroundSessionProtocol>\"8@\"NSDictionary\"16B24
AVAssetDownloadTaskMediaSelectionsForMultichannelKey
-[__NSCFURLLocalStreamTaskFromDataTask connection:request:needsNewBodyStreamFromOffset:callback:]
Unknown attribute name %@
sessionDescription
charset=
INSERT: ERROR: unable to obtain the persistent store directory.
EHA_LIT
kCFURLProtectionSpaceKeyServerType
<CFURLCredential %p>{userPrincipal = %@, hostPrincipal = %@, uuid = %@, kerberosFlags = %@, persistence = %d}
_NSDataType
har-capture-global
Temporary Redirect
-[_NSCFWikipediaProtocol initWithRequest:cachedResponse:client:]
satisfied
CFObserverHolder
com.apple.cfnetwork.AuthBrokerAgent
\tports:{ %@ }\n
not yet parsed
gateway timed out
updateCoalescingConnectionKeyWithHostWithDNSRecord
binarycookies
metricstream_queue
shouldHandleHTTPCookies
oct
Cannot open file
useKeychain
_timerStart
Err-3007
NSURLSessionProxyErrorDomain
v16@?0@\"_NSHTTPConnectionInfo\"8
Opening
warning
%02d:%02d:%02d.%03d
ICI=0 is an error
%@%@
nw_activityUUID
v24@?0@\"NSArray\"8@\"NSError\"16
sandboxExtShm
data
enc_free_hinfo
NSURLSessionDelegateImplementsWillPerformRedirectionKey
Background
bytes out: %u; bytes in: %u, ratio: %.3f
<%p>
fake.com
SecItem-shim.cpp
Error: stepSQLStatement:toCompletionWithRetry - stepping returned unhandled result=%d, DB=%@
+[NSNetService dictionaryFromTXTRecordData:
Internal Server Error
Network Load
,%@
Use Credential
SSL-READ
could not allocate hinfo for stream %llu
Subject Sum
HTTP2ConnectionCacheEntry.cpp
DELETE FROM alt_services WHERE (host = ? AND port = ?)
CFURLCredential
<CFURLAuthChallenge %p>{space = %@, proposedCredential = %@, previousFailureCount = %ld, failureResponse = %@, error = %@/%ld}
_connectionPoolName
__nsurlrequest_proto_prop_obj_2
SessionConnection.mm
Err-1204
existing
HTMLForm
not done
Handshake failure
Persistent
Message
\tdomain:%@\n
CreateToNow
bodyStartProvidingData
v40@?0@\"IDSBaseMessage\"8@\"NSError\"16q24@\"NSDictionary\"32
readFrame
kNSURLSessionImmediateInvalidationErrorKey
write count
status == kSHTTPConnectionCacheEntryNewTubeCreated
_onqueue_changeState
-[__CFN_CoreSchedulingSetRunnable startedRunLoop:]
_neTrackerTCCResult
not writing
%@(%s)
.local
DiskCookieStorage Updated
DiskCookieStorage Checking
w
Windows_NT
Received Accounts
loadingPriority
HTTP Version not supported
v24@?0r^{CoreSchedulingSet=^^?^{__CFAllocator}i^^?^{_opaque_pthread_t}i^{__CFSet}@{os_unfair_lock_s=I}^{__CFRunLoop}^{__CFString}i}8^v16
_nscfBridgeURLCacheDiskCapacity
AppendDNSNameString: Illegal empty label in name \"%s\"
NSURLRequestFileProtocolExpectedDevice
_kCFNTimingDataConnectionReused
 isSecure:%@
!_httpRequest
Negotiate
total bytes
ClientHello
accepted
requestBodyTransferSize
_kCFStreamStatsTLS_HandshakeTimeMs
TRUE
Error: execSQLStatement:onConnection:toCompletionWithRetry:writeLockHelp - SQL=%s, error-code=%d, error-message=%s
Request URL
kCFURLProtectionSpaceKeyHost
%s %s %.*s
init_with_task_with_socket_streams
getPreparedRequest
PRAGMA user_version=203
_allowsIndefiniteConnections
NLST %@\r\n
{ conn: %p, local %s => peer %s %s}
SENT
Caches
AVAggregateAssetDownloadTask does not support response property
CONNECT
_timerState == TimerState::NotSet
PublishingURL
<
INSERT OR REPLACE INTO alt_services(partition, host, alternateHost, port, alternatePort, type, creation_time, expires_time, rowid) \t\tvalues (?, ?, ?, ?, ?, ?, ?, ?, (SELECT max(rowid) FROM alt_services)+1)
getifaddrs
HTTP Proxy
writeEvent
upgrade-insecure-requests
__nsurlrequest_proto_prop_obj_7
AssertionManager.m
NSATSBuiltinOverride
decodeChangeCiperSpec
DynamicStackTracing
DROP table IF EXISTS cfurl_cache_response;
DELETE FROM alt_services WHERE ROWID in (SELECT ROWID FROM alt_services ORDER BY ROWID DESC LIMIT -1 OFFSET %ld)
NSAllowsArbitraryLoadsForMedia
NSParsedCIDRPrefixKey
CFNETWORK_HAR_LOGGING
if-modified-since
%
March
vals
_kCFNTimingDataNStatTXRetransmit
_CFServer
v24@?0^{gss_OID_desc_struct=I^v}8^{gss_cred_id_t_desc_struct=}16
com.apple.CFNetwork-cc-%d-%lld-%@
_onqueue_resetAndReconnect
HTTPS Proxy
v24@?0Q8@\"NSError\"16
UIApplicationWillEnterForegroundNotification
requestNewTube
DiskCookieStorage Sync Request
WONR.alloced_len
_protocolInstance == nil
reset content
policy
_kCFStreamErrorCodeKey
none
kCFNetDiagnosticPingOptionTrafficClass
%@-wal
RB
_supportsAVAssetDownloads
duplicate ICI: %u
_kCFNTimingDataSubflowCountsAtStop
processTransaction
%@/
dtype
certs
@\"NSObject<OS_nw_object>\"28@?0I8^{nw_protocol_identifier=[32c]ii}12^i20
v20@?0^{__CFString=}8B16
B16@?0^{TCPIO_BlockCallbacks_Listener=^^?{CBs=@?@?@?@?@?@?}@i}8
key->isCoalesced() == false
bad gateway
peer
path && [path length]
lax
com.apple.runningboard.can-suspend-locked
RL
redirection
v48@?0B8@\"NSObject<OS_dispatch_data>\"12B20{?=qi}24@\"NSObject<OS_nw_content_context>\"40
personaUniqueString
Cannot create download task with corrupt resume data
 { URL: %@ }
_delegate_connectionWaiting
found != _transactions.end()
checkTube == newTube
_duetPreClearedMode
type
apple-mapkit.com
kCFProxyPortNumberKey
-[NSURLRequest _URLHasScheme:]
authorization
Err-1102
PRAGMA incremental_vacuum(500);
prefetch
NSURLSessionTask %p
v28@?0@\"NSObject<OS_dispatch_data>\"8^{__CFDictionary=}16C24
CREATE TABLE IF NOT EXISTS cookies (        name text NOT NULL,        value text NOT NULL,        domain text NOT NULL,        path text NOT NULL,        partition text NOT NULL,        is_secure int NOT NULL,        is_hostOnly int NOT NU
EEA_NONE == prog.ep_enc_action
<BR 
_handleHeaders
multipath
~PerSide_CFWriteStream
CFURLCache
kConditionalConnectionActivityName
additionalProperties
kNetworkProxyCredentialKeyViability
v24@?0@\"NSMutableSet\"8@\"NSMutableDictionary\"16
kCFStreamPropertyFTPProxyUser
Could not connect to the server.
--
com.apple.nsurlsessiond.NSURLSessionProxyService
persistence
Response
fileURL
bodySize
EHA_INDEXED_STAT
!_willEnqueueRequests()
error %d resolving %s address for socket %d
queue
v16@?0@\"NSCachedURLResponse\"8
_shouldSkipPreferredClientCertificateLookup
internal server error
_loaderEvent_AckBytes
kCFURLStorageSessionProcessSharing
%8.8x: 
clientKey
SETTINGS_MAX_FRAME_SIZE
writeFrame
bundle
flags
effectiveTrafficClass
_kExcessiveKeepalivesParametersEnabled
_kCFNTimingDataResponseEnd
no content
X-Apple-Cache-Session
CFURLDownloadDataDecoder
file is directory
v24@?0^{__CFReadStream=}8q16
NSURLCache.mm
\t\t%d: %p ,\n
SHTTPConnectionCacheEntry.cpp
%@ %@%@
kCFProxyAutoConfigurationURLKey
newTubeReady
kCFURLConnectionSocketStreamProperties
+[NSURLConnection(Deprecated) _setMIMETypesWithNoSizeLimit:]
Content-Type
HTTPServerConnection
content-encoding
=
TCPIOConnectionTest.hpp
}
(_state == State::New) || (_state == State::Canceled)
got Cancel Stream instruction; stream=%llu
Cannot remove file
HTTPNetStreamInfo.cpp
v16@?0@\"NSObject<OS_tcp_connection>\"8
_rs == NULL && _ws == NULL
LocalSession.mm
[%llu] %s %s frame<length=%ld, flags=0x%x, stream_id=%d>
kCFHTTPAuthenticationOAuth1PID
sandboxExt
_tubeManager
CFURLProtectionSpace
v16@?0@?<v@?>8
h2 prio
static const char *_PNAME<URLProtocol>::GET() [OBJTYPE = URLProtocol]
waiter
HTTP_NETWORKSCORE_DATA
<_NSHTTPAlternativeServiceEntry> {\n \t\t\tHost = %@ \n \t\t\tPort = %ld \n \t\t\tPartition = %@ \n \t\t\tAlternate-Host = %@ \n \t\t\tAlternate-Port = %ld \n \t\t\tExpiration = %@ \n} 
kCFURLConnectionSuspensionThreshold
_onqueue_loaderEvent_CancelLoad
One or more certificates have expired or are not valid yet.
v56@?0^{__CFString=}8^{__CFData=}16{shared_ptr<const __CFArray>=^{__CFArray}^{__shared_weak_count}}24{shared_ptr<__CFError>=^{__CFError}^{__shared_weak_count}}40
header block for stream %llu has had an error
bad_optional_access was thrown in -fno-exceptions mode
negotiatedTLSCipherSuite
NSErrorPeerAddressKey
_kCFNTimingDataNStatCellTXPackets
a
timeout
mayBeDemotedToDiscretionary
Unsupported extension
har-host-denial-list
fKind == eDispatchQueueBased
Proxy Authentication Required
CFNETWORK_LOG_AUTH_TIMEOUT
Err-3003
ERROR: NSURLStorageURLCacheDB deleteResponsesSinceDate: dbConnection=%p DB=%@ Commit transaction failed:%s ErrCode: %d.
connectionWasLost
credKind
Original Length
CFHTTPCookieStorageAddObserver
_100ContinueTimer
__NSCFURLSessionConfiguration_Immutable
entry->dte_flags & DTEF_NAME_HASH
__nsurlcredential_proto_plist
%@: Host:%@, Server:%@, Auth-Scheme:%@, Realm:%@, Port:%ld, Proxy:%@, Proxy-Type:%@
StatusCodes
privacyProxyFailClosedForUnreachableNonMainHosts
-[__NSCFLocalDownloadTask _private_completionAfterMetrics]
ATSAllowsArbitraryLoadsInWebContent
_kCFNetworkHSTSIncludeSubDomains
Structured
_kCFNTimingDataConnectionUUID
got ICI instruction, count=%llu
v40@?0@\"__NSCFLocalSessionTask\"8@\"NSData\"16@\"NSURLResponse\"24@\"NSError\"32
Cannot create upload task without request or resume data
NSURLAuthenticationMethodXMobileMeAuthToken
outbound decoder
taskMetrics2
@\"NSDictionary\"8@?0
Unexpected message
kind
 
streamID > 0
got error from inflate, %ld
Err-1005
HTTPOnly
target
establishmentReport
Unsupported Media Type
can't alloc length
Background session configuration must have a non-nil identifier
_loggingPrivacyLevel
<HTTPConnectionCacheEntry@%p>{\n
kCFURLCredentialKerberosNoUIFlag
_customReadBufferSize
_delegate_didStopBuffering
kCFProxyTypeHTTP
cache-control
kCFProxyTypeFTP
;*__%%%SKIP_DECODING%%%__*;
cfnetwork@apple.com
Err-1009
header block error on line %d, offset %llu, stream id %llu
request: 
encoding
ssNeedClientCert
_NSCFTranslatedFileURLProtocol_PIMPL_%d
Dirty
Time from last  dirty
access-control-allow-methods
mainDocumentURL
\r\n0\r\n\r\n
httpresponse
Tube
static const char *_PNAME<HTTPServerRequest>::GET() [OBJTYPE = HTTPServerRequest]
<CFURLCredential %p>{appleID = %@, password = %@ realm = %@, persistence = %d}
client error
v20@?0Q8i16
DoesSZExtractorConsumeExtractedData
nullptr request
-[__NSCFURLLocalStreamTaskFromDataTask connection:sentBodyBytes:totalBytes:expectedBytes:]
kCFURLCredentialKerberosTicketAllowDelegation
persistent
SYST\r\n
kCFCredentialStorageRemoveSynchronizableCredentials
_pendingData == nullptr
NSAllowsArbitraryLoadsInWebContent
_FTPStreamOpenCompleted
wss
%d [%d]
END_STREAM
CFNetDiagnosticCreateBasic
NSURLAuthenticationMethodHTTPBasic
NSURLDownloadBinHexDecodedDataOffset
August
getDispatchQueue
Request Time-out
resumeURL
explicitContentType
_networkReachabilityChanged
com.apple.hstscache.workqueue
kCFProxyUsernameKey
_chunkedWriteHeaderAndBody
^v16@?0^{__CFString=}8
bytes=%lld-
_startConnection_Completion
Connection Viability Changed
kCFURLRequestPreAuthXMMeAuthToken
NSURLSessionDelegateImplementsWillSendRequestForEstablishedConnectionKey
_connection
Cannot get default cookie store - using a memory store for this process
HTTP2CoalescingSupport.mm
schemeWasUpgradedDueToDynamicHSTS
Insufficient security
_downloadFileProtectionType
reset bytes in/out counters, ratio: %.3f
AVAssetDownloadURLSession does not support NSURLSessionUploadTask
hw.memsize
secureConnection
^v8@?0
CachedState
_allowsTLSFallback
AppSSOProtocol
Unviable
304
text/plain;charset=utf-8
FTPPort
kCFStreamPropertyFTPPassword_prevalidated
allowsCellularAccess=%d allowsExpensiveNetworkAccess=%d allowsConstrainedNetworkAccess=%d requiresPowerPluggedIn=%d
nwstream
%@{ default: %d private: %d process-sharing: %d ident: %@, cache = %p, cookies = %p, auth = %p, hsts = %p }
_kCFNTimingDataTCPFastOpenStats
switching protocols
Decode error
!waiter->hasBeenClaimed()
distnames
com.apple.httpserver.bystreams
com.apple.NetworkDiagnostics.notification
[path isAbsolutePath]
__NSCFURLSessionConfiguration
_callbacks->start != NULL
Cookie URL
+[NSURLRequest getObjectKeyWithIndex:]
jun
Vary Validation
CFNetwork _delegate_willSendRequestForAuthenticationChallenge called delegate - Load: %@ Challenge: %@
cookies_added_handler_queue_default
lsqpack_enc_enc_str
ERROR: NSURLStorageURLCacheDB deleteResponsesSinceDate: dbConnection=%p DB=%@ Pragma checkpoint failed:%s ErrCode: %d.
URLConnection.h
_CFCachedURLResponseUserInfo
properties
Err-1003
BundleID
CertificateRequest
v16@?0^{HTTPServerConnection=^^?^^?{_CFHTTPServerClient_V0=q^v^?^?^?}^^?^{__CFAllocator}i^{__CFDictionary}@^{CoreSchedulingSet}^{__CFError}{_CFHTTPServerConnectionCallbacks_V1=q^?^?^?^?^?}^{HTTPServer}C^{__CFReadStream}^{__CFWriteStream}ddq
CFHost
_kCFNTimingDataRemoteAddressAndPort
GIF87a
Failed
v28@?0B8{?=qi}12
v12@?0i8
%@ { state %s, expected total body length %ld  }>
com.apple.nsurlsessiond.readonly
currentRequest
open
%@ { rs = %@, ws = %@ }
A server with the specified hostname could not be found.
user
BuiltinException
uniqueTaskIdentifier
500
HTTP3ConnectionCacheEntryWrapper<@%p> for HTTP3ConnectionCacheEntry<@%p>
base64
Sep
The certificate for this server is not yet valid.
com.apple.CFNetwork.Async.SCNetworkReachability
bad_function_call was thrown in -fno-exceptions mode
kCFURLDownloadFileCreateDate
kCFProxyHostNameKey
Failure occurred while closing file
TubeManager.cpp
sessionSendsLaunchEvents
PreventUserIdleSystemSleep
Tue
DELETE from cfurl_cache_receiver_data WHERE entry_ID=%s;
com.apple.Safari
:scheme
HTTP3ConnectionCacheEntry.mm
kCFProxyTypeHTTPS
v16@?0@?<v@?{shared_ptr<const __CFArray>=^{__CFArray}^{__shared_weak_count}}{shared_ptr<const __CFArray>=^{__CFArray}^{__shared_weak_count}}{?=qi}>8
shared_tcpConnWorkQueue
kTubeTypeHTTP2
user-agent
parse_header_data
body
 \t\r\n
Unauthorized
!snt
<NSHTTPCookie\n
shared_tcpConnWorkQueue_Background
writeDBwithCachedResponse-ERROR: bind of 0 partition value for item: %@
%@ { %@ }
CantRename
NWURLSession
-[__NSCFURLLocalStreamTaskFromDataTask connection:request:needsNewBodyStreamCallback:]
Did Send Body
q8@?0
kCFProxyTypeNone
FATAL: Failed to change priority.
You do not have permission to access the requested resource.
B32@?0@\"NSObject<OS_nw_protocol_definition>\"8Q16Q24
issuing error to ECONNABORTED
kCFStreamPropertyFTPAttemptPersistentConnection
<H1 
Journal
__nsurlrequest_proto_prop_obj_29
ATSAllowsArbitraryLoadsForMedia
_readHeadersStart
%@: %@
AVAssetDownloadToken
Service Unavailable
MKD %@\r\n
kCFSOCKSNegotiationMethodKey
preventHSTSStorage
max-age=604800
upload-
v16@?0@?<v@?B{shared_ptr<__SecTrust>=^{__SecTrust}^{__shared_weak_count}}{shared_ptr<const __CFArray>=^{__CFArray}^{__shared_weak_count}}{?=qi}>8
firstWaiterIdx != -1
%@:%d
_loaderClientEvent_DidReceiveChallenge
_kCFHTTPCookiePolicyPropertyAllowHTTPOnlyOverwrite
%s (%d, 0x%x), length %d (0x%x)
kCFSOCKSVersionKey
 %@
_tlsTrust
com.apple.
NSURLSession
ERROR: failed to get the path to the FS cached data at %@
The read-connection to the DB=%@ is NOT valid.  Unable to determine schema version.
establishTime
NAMELOOKUP_FAILED
STube
<TransportConnection@%p>
unknown_scheme
boundInterfaceIdentifier
ConnectionProtocolConnected
CopyAllCredentials
International roaming is currently off.
Protocol Enqueue
HTTP2Stream.cpp
fsly
See Other
com.apple.cfnetwork.ats.loglevel
WINR.alloced_val_len >= WINR.val_len
0123456789abcdef
CONTINUATION
length required
_onqueue_rdar53306264_addWaiter
kConditionalConnectionLaunchOnDemand
v16@?0@\"NSURLSessionTask\"8
NSURLSessionDelegateImplementsSessionAuthChallengeKey
<%@%p state %s, pending %d { %@ }>
_startRequest
purpose
There was a bad response from the server.
_onqueue_beginTrailers
COMMIT
CFN_FORCE_ATS
Download
<BrotliDecoder@%p>
v24@?0@\"NSObject<OS_dispatch_data>\"8@\"NSObject<OS_nw_content_context>\"16
ERROR: NSURLStorageURLCacheDB _setDBSchema: DB=%@ receiver_data recreate - %s. ErrCode: %d.
END SSL RECORD DECODE: %s
8
IMRemoteURLConnectionAgent
NSURLSessionResumeEntityTag
kCFURLRequestDoNotDecodeData
_writeBufferAlreadyWrittenForNextWrite == 0
:authority
https
h2 updt
Err-3002
<CFHost %p>
errCode
Skipping AppSSOProtocol
_protocolInterface_startLoad_block_invoke
 | 
localhost
<%s %p> { url = %@ }
static const char *_PNAME<CFNACOAuthSigner>::GET() [OBJTYPE = CFNACOAuthSigner]
NSExceptionAllowsInsecureHTTPLoads
_delegate_didFail
preventsIdleSystemSleep
bad URL
writeDBwithCachedResponse-ERROR: bind of storage policy for item: %@
DiskCookieStorage Journaling On
decodeApplication
Not Found
__nsurlrequest_proto_prop_obj_11
_kCFHostBlockingMode
Did Finish
kCFURLRequestContentDecoderSkipURLCheck
kCFHTTPServerFailingRequest
v16@?0^v8
sandboxExtWal
conflict
kTubeTypeHTTP3
Stream Error
<CFURLProtectionSpace %p>{host = %@, port = %d, realm = %@, serverType = %d, authenticationScheme = %d}
-[__NSCFURLLocalStreamTask _onqueue_addBlockOpAtHead:description:]
v16@?0@\"__NSCFURLLocalStreamTask\"8
drop entry %u (`%.*s': `%.*s'), nelem: %u; capacity: %u
SELECT * from alt_services;
__nsurlrequest_proto_prop_obj_1
kCFStreamPropertyFTPProxyPassword
scheduledOriginLoad
,%@;q=0.%u
]
May
posixErrorCode != 0
http/1.1
en
Cannot create an AVAggregateAssetDownloadTask in a non-background session
v16@?0@\"NSObject<OS_sec_protocol_options>\"8
%@://%@/<redacted>
AppleLanguagePreferencesChangedNotification
expiration
[error %d converting %s address for socket %d]
\tisHTTPOnly: %@\n
SELECT r.version, r.storage_policy, b.response_object, b.proto_props, d.isDataOnFS, d.receiver_data, b.request_object, b.user_info, r.time_stamp FROM cfurl_cache_response r, cfurl_cache_blob_data b, cfurl_cache_receiver_data d WHERE r.reque
shouldCancelOnDisconnect
com.apple.NSURLSession.streamTask_work
Finished Merging Classes
<HTTP stream context %p>{url = %@, state = %s, conn=%p, isZombie=%s}
TimeoutIntervalForResource
list
!_callbackBuffer
_forceEnablePQTLS
lsqpack.c
opportunistic
GSE
Err-1010
SocketStream TCP Connection Complete
_streamInitialized
SERVER_UP
-[__NSCFURLLocalStreamTaskFromDataTask connection:didReceiveResponse:completion:]
Monday
Err-3005
MainDocument URL
%c%c
endTime
VaryState
request body stream exhausted
Challenge
bytes=0-
RNFR %@\r\n
url
_onqueue_processRawHeaders
HostLookup
init to origin load
interfaceName
valu
SETTINGS_MAX_HEADER_LIST_SIZE
Completion handler blocks are not supported in background sessions. Use a delegate instead.
create FILE
connect
image/gif
AVAssetDownloadURLSession does not support NSURLSessionDataTask
bad length
connCache
%@/%s_remove
Array
DROP table IF EXISTS cfurl_cache_blob_data;
ERROR: NSURLStorageURLCacheDB _setDBSchema: DB=%@ blob_data create - %s. ErrCode: %d.
NSParsedCIDRAddressKey
NSAppTransportSecurity
com.apple.avfoundation.assetdownload.foregroundonly.
\xff\xdf\xdf\xdf\xff
Err-1201.w
<data URL instance at %p>
\tpartition:%@\n
<CompactCookieArray@%p> { %d cookies }
history size change from %u to %u
newTube
fClientCertChallenge == nullptr
username
kNetworkProxyAuthorizationElementsKeyCredential
Wrapping TransportConnection(%p)
_TCPAdaptiveWriteTimeout
push entry:(`%.*s': `%.*s'), capacity %u
%@/VaryState.db
_allowsHTTP3Internal
close
timeWindowDelay
Total Written
SELECT * from cookies WHERE domain like ? AND expires_time > strftime('%s','now')
ignoreHSTS
LocalStreamTask.mm
mms.um.idmobile.co.uk
kCFNetDiagnosticPingOptionPacketCount
queryString
v56@?0{FrameMetadata=QQQ}8@\"NSObject<OS_dispatch_data>\"32{?=qi}40
INIT-FAIL: _sqlInsertStmtResponse=%p, DB=%@, error-code:%d.
kConditionalConnectionRequirementWorkload
HelloRequest
pair { %p, %s }
prog.ep_tab_action == ETA_NOOP
Err-3000
<CFHTTPMessageRef %p(%p)> { simple response, url = %@, body = %ld bytes }
,
_callbacks->version == 2
Single Sign-On
X-MobileMe-AuthToken %@
ERROR: NSURLStorageURLCacheDB _setDBSchema: DB=%@ response create - %s. ErrCode: %d.
nghttpx
id > enc->qpe_cur_header.base_idx
}  }
()<>@,;:\\\"[]?={} \t
Library/Cookies/
size
v24@?0@\"NSURLRequest\"8@\"NSFileHandle\"16
kCFURLDownloadResumeServerModificationDateString
Common Name
-[NSNetService _internal_publishWithOptions:
enableSPIDelegateCallbacks
_kCFNTimingDataNStatConnectSuccesses
kCFURLDownloadFileModDate
invalid name
bytesPerSecondLimit
%d pending, %d outstanding, %d closed
Accepted
wait
_systemClientOfPrivateAccessTokens
enc->qpe_cur_streams_at_risk > 0
Distinguished Names
requiresPowerPluggedIn
com.apple.httpserver.byname-nw
ConnectionProtocolRemoveInputHandler
_disableAPWakeOnIdleConnections
NDRemoteHostKey
bodyParts
<%@ %p> %@ %@ %@ %d
ClientKeyExchange
Web form password
_kCFURLProtectionSpaceAuthenticationSchemePrivateAccessToken
stat failed: errno %d
%@/%@%@
outbound encoder
\tsessionOnly:%@\n
allowsUCA
com.apple.CFNetwork.Connection
Discard
enc->qpe_cur_streams_at_risk == 0
_sniffData == NULL
response from %@
PST
Task and request are both nullptr; Error: %p [%ld:%d]
ERROR: CFNetwork Protocol SPI not supported.  %p %p %p %p %p %p
_connectionEndpoint
com.apple.ATSCleartextHTTP
_readOutstanding
resume
v16@?0@\"NSArray\"8
SetCredential
NSURLDownloadBinHexResourceForkBytesRemaining
requestPriority
Certificate expired
main queue = %p, main thread = %p, main mach thread = %u
_respectsAllowsCellularAccessForDiscretionaryTasks
content-length
com.apple.network
Time from first dirty
Max-Age
kConditionalConnectionRequirementDuetPreClearedMode
%@ %s %@
_kCFStreamPropertyFTPRemoveResource
__Host-
qdec: debug: 
_resourceTimeout == NULL
key_not_serialized
kCFStreamPropertyFTPUserName_prevalidated
v24@?0@\"NSObject<OS_sec_protocol_metadata>\"8@?<v@?@\"NSObject<OS_sec_identity>\">16
CFNetDiagnosticCreateWithStreams
HTTP2StreamEqualCallBack
resource exceeds maximum size
0\r\n%s\r\n
The certificate for this server is not yet valid. You might be connecting to a server that is pretending to be \"%@\" which could put your confidential information at risk.
status == 0
Task created in a session that has been invalidated
com.apple.cfnetwork
CFNetDiagnostics
value1 && value2
cleanAbort
_kCFNetworkProxySessionNeedsNewBodyStreamSignal
<!DOCTYPE HTML 
ATSConnectionExceptionEvent
Read from disk
v44@?0@\"NSObject<OS_nw_content_context>\"8@\"NSObject<OS_dispatch_data>\"16B24{?=qi}28
Cannot create task from nil request
kCFStreamPropertyFTPUserName
pass
?0
_nscfBridgeURLCacheCopyResponseForRequest:
taskKind
%@%c%@
shared credential storage %p, session %p, persistent %p
_kCFNetworkCFStreamSSLErrorOriginalValue
_asyncWriteFileCompletely
kCFHTTPAuthenticationPassword
v24@?0I8I12@?<v@?@\"NSObject<OS_dispatch_data>\"B{?=qi}>16
_state < State::Negotiating
timing-allow-origin
HTTP2Server.hpp
NSURLConnection-WebKitSync
STubeManager.cpp
Dec
Partial Content
policies
__nsurlrequest_proto_prop_obj_22
r^{CompactCookieArray=^^?^^?^{__CFData}}332@?0{DomainAndPartition=^^?{CFAbsoluteTimeAsSpecified=Cd}[256C]*Q***}8C328
_offqueue_open
__nsurlauthenticationchallenge_proto_plist
writeDBwithCachedResponse-ERROR: bind of hash for item: %@
-[__NSCFLocalSessionTask dealloc]
Task
WARNING: %s should no longer be called
v16@?0@\"NSObject<OS_nw_protocol_options>\"8
<AuthenticationState@%p>{
kConditionalConnectionOnBehalfOfPairedDevice
CFNETWORK_IO_LOG
[error %d converting]
NDMethodKey
T *ClientContextHolder<CFURLDownloadClient>::forget() [T = CFURLDownloadClient]
Err-1017
ERROR: NSURLStorageURLCacheDB deleteResponsesSinceDate: dbConnection=%p DB=%@ Vacuum failed:%s ErrCode: %d.
_delegate_didSendBodyData
kCFHTTPServerRequireClientCertificate
har-capture-pid-specific
v8@?0
kConditionalConnectionIsDiscretionary
earliestBeginDate
<Server %p>{tcp_listener=%p, info=%@}
transferredRequest
Err-1100
!_callbackHandler
DELE %@\r\n
written == [(NSData*)data length]
binary
_currentResponse
com.apple.CFNetwork.har-capture-update
entry == STAILQ_FIRST(&enc->qpe_buckets[buckno].by_name)
WINDOW_UPDATE
USER %@\r\n
shared_tcpConnWorkQueue_UserInitiated
must replay
_tcp
Nov
blockTrackers
## Message %d (0x%x) length %d (0x%x) invalid - encrypted?
unsupported version
explicitFlags
HTTPBasic
LoaderWhatToDo
_minLen == 0 && _maxLen == 0 && _timeout == 0.0 && _cb == nullptr
H
CWD %@\r\n
Space
_requiresSecureHTTPSProxyConnection
<HTTP protocol instance %p>
v16@?0@\"NSObject<OS_nw_error>\"8
%@/%s/%@
-[__NSCFURLLocalSessionConnection _tick_finishing]
v20@?0^{__CFArray=}8B16
\n
_offqueue_openCompleted
_forcedNetworkServiceType
access-control-expose-headers
HEADERS
Err-1206
http://
NetworkStorageDB:_openDBReadConnections: failed to open read connection to DB @ %s.  Error=%d. Cause=%s
__SKIP_USER_AGENT_IN_REQUEST_EQUIVALENCY_CHECK__
\xff\xdf\xdf\xff
AVAssetDownloadTask does not support response property
Persistent Cookies
1.2.12
ApacheTrafficServer
Jan
Prepare Transmission
streams at risk: %u
com.apple.ResourceFork
_transactionUUID
_socketStreamPropertyQOSClass
ReadStream
_onqueue_scheduleAndOpenWithHandler
null url string
websocketPing
found
stopSecureConnection
LiteSpeed
Err-1021
CantOpenWriteStream
Mutations
December
enc->qpe_hist_els
_NSURLErrorPrivacyProxyFailureKey
cannot decode raw data
:%d
_connectionCacheCellPurgeTimeout
cacheLookupEndTime
Response Error
`
kCFStreamSSLAllowsExpiredCertificates
startSecureConnection
CREATE INDEX request_key_index ON cfurl_cache_response(request_key);
empty cookie array
com.apple.private.cfnetwork.har-capture-delegation
,\n
assertionCount > 0
Library
Err-1014
SocketStream watchdog timer fired after %f seconds of inactivity. Timing out the connection.
v16@?0^{AOSTransactionC=}8
errno %d
Alert %s is %s
_state == State::ReceivingResponse
responseBodyTransferSize
_CFURLConnectionSetFrameworkStubs
v24@?0^{__CFString=}8^v16
HTTPCookieStorage::setCookie
com.apple.NSURLSession-delegate
file:
valid=%s, ss=%@
TubeManager.h
v16@?0^{SAwaitingTube=^^?^{__CFAllocator}iB^^?^{HTTPConnectionCacheKey}^{HTTPRequestMessage}^{MetaConnectionCacheClient}{MetaConnectionOptions=ifQCCCC}^{STube}dd}8
ended header; hinfo absent
access-control-allow-headers
RETR %@\r\n
Timeout Interval
kCFFTPResourceModDate
Stream tasks are not supported in background sessions
Non-Authoritative Information
_chunkedReadHeader_block_invoke
%s (%d) | %c
schedulingSet
http
NSURLAuthenticationMethodHTTPDigest
CREATE TRIGGER IF NOT EXISTS cfurl_vary_state_delete AFTER INSERT ON cfurl_vary_state WHEN (select count(*) from cfurl_vary_state)>16384\nBEGIN\nDELETE FROM cfurl_vary_state where request_key NOT IN (SELECT request_key from cfurl_vary_state
<CFURLConnection %p> { request = %@ }
Err-3001
password
_delegate_shouldUseCredentialStorage
Authorization
%@@%@
value
cpgz
Task delegate is not supported on background session task
Total Expected
HTTPServerNWStream.mm
end
ConnectionProtocolAddInputHandler
Request Priority Levels: %d
writeDBwithCachedResponse-ERROR: bind of partition value for item: %@
Loader
readevent
AVAggregateAssetDownload
updateTCPAdaptiveParameters
CFNETWORK_DIAGNOSTICS
_kCFNTimingDataResponseStart
kCFURLConnectionURLConnectionProperties
Evaluation
Root certificate is not trusted.
Hostname mismatch.
endpoint
requiresShortConnectionTimeout
incomplete
allowCellular
Err-1001
LocalSessionTask.mm
New Request
!fSSLDistNamesCompletion
pushed entry %u (`%.*s': `%.*s'), nelem: %u; capacity: %u
SO_RECV_ANYIF
kCFStreamSSLAllowsAnyRoot
Received tcp connection for upgrade
xhdr->flags & LSXPACK_NAME_HASH
_sendHEADERS
CountOfBytesClientExpectsToReceive
headersSize
_kind
_enableOAuthBearerTokenChallenges
etag
Err-1101
negotiatedTLSProtocolVersion
kSTubeTypeNPN
NSURLSessionResumeCurrentRequest
kConditionalConnectionRequirementTimeWindowDuration
_onBehalfOfPairedDevice
1
kCFProxyPasswordKey
%@.%@
AVAssetDownloadSessionMediaSelectionPrefersMultichannelKey
Reset Content
service unavailable
!fSSLTrustCompletion
kCFHTTPAuthenticationOAuthToken
kCFGetAddrInfoFailureKey
max-age=2592000
legacy
ServerKeyExchange
%X\r\n
NSURLSessionDelegateImplementsDidReceiveResponseKey
trailerData
getNegotiateRequest
] recv (stream_id=
headers
v24@?0@\"NSObject<OS_nw_authentication_challenge>\"8@?<v@?@\"NSObject<OS_nw_authentication_credential>\"B>16
NSURLRequest.mm
-[NSURLDownload initWithRequest:delegate:]
TYPE I\r\n
CFNETWORK_HOST_QUEUE_KIND
insertion count too high: %llu
Err-3006
static const char *_PNAME<HTTPServerResponse>::GET() [OBJTYPE = HTTPServerResponse]
parse_header_prefix
<HostLookup@%p> { %p }
com.apple.NSHTTPCookieManagerNotification
Referer
<< ORDER >>
content-security-policy
upload
NSTemporaryExceptionAllowsInsecureHTTPLoads
## Only %ld bytes after header, need at least 4
v32@?0^{NetworkProxyCredential=^^?^{__CFAllocator}i^^?^{_CFURLCredential}iQ}8^v16@?<v@?^{NetworkProxyCredential=^^?^{__CFAllocator}i^^?^{_CFURLCredential}iQ}>24
gs.apple.com
cellular
kCFURLStorageSessionIdentifier
Err-1103
<read side %p to stream %p>
received
download
nulldomain
com.apple.security.get-task-allow
<CFURLCredential %p>{OAuthToken = %@, persistence = %d}
called removeCachedResponsesSince: subclass should implement
com.apple.CFNetwork.NSURLSession.{%@}{%@}{%c}{%d}{%p}
only-if-cached
metricstream
edge-type
PASS %@\r\n
pending retry
Download decoding failed
SELECT receiver_data from cfurl_cache_receiver_data WHERE isDataOnFS > 0 AND entry_ID in (SELECT entry_ID FROM cfurl_cache_response WHERE time_stamp >= \"%s\")
!fSSLTrust
URL
<CompactCookieHeader@%p> { domain: %s, partition: %s, name: %s, path: %s, value: %s, session: %c, secure: %c, httponly? %c, expires: %@, created: %@, accessed: %@ }
bodyType
<CFURLCache %p [%p]>
v64@?0{shared_ptr<HTTPResponseMessage>=^{HTTPResponseMessage}^{__shared_weak_count}}8@24{?=qi}32q48q56
-[__NSCFURLLocalStreamTaskFromDataTask connection:wasRedirected:newRequest:responseCallback:]
NSURLSessionResumeOriginalRequest
CFObject.cpp
%@.%lu.childAssetDownloadTasks
com.apple.NSNetServices.tcplistener-queue
NSURLCredentialStorageRemoveSynchronizableCredentials
com.apple.URLDownload
null response stream
NSIncludesSubdomains
other
kCFFTPProtocolPropertyReturnDirectoryListing
Unsupported NSURLSessionConfiguration
v32@?0@\"NSURLProtectionSpace\"8@\"NSDictionary\"16^B24
com.apple.nsurlsession.wait-unlock
I
domain
kCFNetDiagnosticPingOptionTypeOfService
qenc: info: 
h2 gowy
sendDidFail called with NULL err, request: %@
Err-998
ERROR: encoding user-info failed. Error:%@
Not Acceptable
workQueue
ERROR: shrinkDB - shrink of file system cache did not fully complete.  Result: %d
Client Cert Requested
frame
<GZipDecoder@%p>
NSURLSessionAppWasResumedForBackgroundSessionNotification
kCFURLStorageSessionAppIdentifier
_IDSMessageTimeout
userOverride
ERROR - Unkown Type
Log file '%s' not created, %s failed, errno %d
_kCFNTimingDataConnectionStartTimeCounts
expect-ct
v56@?0{shared_ptr<const __CFArray>=^{__CFArray}^{__shared_weak_count}}8{shared_ptr<const __CFArray>=^{__CFArray}^{__shared_weak_count}}24{?=qi}40
Saturday
privacyProxyStrictFailClosed
Options
NSURLAuthenticationMethodDefault
destroyReadStream
com.apple.system.config.proxy_change
__CFURLRequestNullTokenString__
CFN_USE_NW_LOADER
Tube.cpp
The network connection was lost.
HTTPProtocol.cpp
kCFHTTPCookieStorageGroupContainerURL
v24@?0^{__CFDictionary=}8^{__CFDictionary=}16
fail %ld
UNKNOWN
NSURLSessionResumeServerDownloadDate
%gs
static const char *_PNAME<TransportConnection::RefCountedWrapper>::GET() [OBJTYPE = TransportConnection::RefCountedWrapper]
_nscfBridgeURLCacheCurrentDiskUsage
WebSocket
NWIOConnection
September
Err-997
Bytes Written
WhatToDo
no error available
copyInData
header count actual: %u; exponential moving average: %.3f
__nsurlrequest_proto_prop_obj_3
_establishmentDelegate
_delegate_didCancel
_connectionClientInterface_resumeConnection
_owner == nil
st == LQRHS_ERROR
] sent (stream_id=
v16@?0^{__CFRunLoopTimer=}8
The requested URL was not found on this server.
total time
<CFHTTPMessageRef %p(%p)> { incomplete response, url = %@ }
h2 rsts
com.apple.NSURLConnectionLoader
ERROR: NSURLStorageURLCacheDB _setDBSchema: _dbWriteConnection=%p DB=%@ pragma auto vacuum - %s. ErrCode: %d.
^v16@?0^{__CFWriteStream=}8
_attributedBundleIdentifier
if-none-match
NSURLResponse.mm
%@%d.%d
Connection Start
isMutable
ATS
x-fb-debug
bodyStopProvidingData
stderr
ForceNWLoader
fState == kTubeStatePostConnectConfiguration
TLSv1.1
Cannot set task delegate after resumption
unauthorized
%s [%d] @ %p, version %2.2x, length %d (0x%x)
TLSMaximumSupportedProtocol
Illegal parameter
-[__NSURLSessionLocal _cfurlRequest:isCacheEquivalentTo:]
gzip
Expectation Failed
_kCFNTimingDataConnectStart
206
data connection service type
v16@?0@\"<__NSCFURLSessionConnectionDelegate>\"8
Proxy Error
NSNetServicesErrorCode
_kExcessiveKeepalivesParametersCount
NSURLAuthenticationMethodNegotiate
no longer exists
%s@%s
<CFNetService %p>{domain=%@, type=%@, name=%@, specific=%@, addresses=%@}
%.*s%d%s
taskIdentifier
keys
YIIFdQYGKwYBBQUCoIIFaTCCBWWgFTATBgkqhkiG9xIBAgIGBiqFcCsOA6KCBUoEggVGYIIFQgYJKoZIhvcSAQICAQBuggUxMIIFLaADAgEFoQMCAQ6iBwMFAAAAAACjggQiYYIEHjCCBBqgAwIBBaEbGxlDT1JFU0VSVklDRVNET00uQVBQTEUuQ09NoiowKKADAgEDoSEwHxsESFRUUBsXY29yZXByb3h5MjAwNi5hcHBs
_allowsTLSSessionResumption
_createEndpoint
!_cb
HTTPCookiePolicyPropertyCookieAcceptPolicy
CantParseData
Length Required
ingestTube
q24@?0@8@16
HTTP2Connection
The Internet connection appears to be offline.
204
ETA_NOOP
__nsurlrequest_proto_prop_obj_17
<%sDownloadDataDecoder@%p>
v48@?0^{__CFHTTPMessage=}8I16^{__CFString=}20i28{SmartBlockWithArgs<const _CFURLCredential *, bool>=^v^{__shared_weak_count}}32
SAwaitingTube.h
consumeData
cachePolicy
~HTTPNetConnection
Created
STubeManager
HEAD
%lld
~PerSide_CFReadStream
__nsurlrequest_proto_prop_obj_24
kCFStreamPropertyFTPPassword
HttpOnly
NSURLAuthenticationMethodOAuthBearerToken
Thu
Reading
v16@?0@\"NSInputStream\"8
Writing
prohibitPrivacyProxy
v32@?0{SessionResponseOptions=BBBBBQQ}8
NSTemporaryExceptionRequiresForwardSecrecy
Gone
v44@?0{shared_ptr<NetworkProxy>=^{NetworkProxy}^{__shared_weak_count}}8B24{?=qi}28
503
Proxy List
fLoaderSchedulingSet && !fLoaderSchedulingSet->isEmpty()
v24@?0^{__CFDictionary=}8^{__CFError=}16
_textBase64
reusedAfterTime
NSURLDownloadOriginatingURLString
apple.com
NSURLConnection ordering violation: didReceiveData to be scheduled before didReceiveResponse
v16@?0@\"NSObject<OS_sec_certificate>\"8
%s, %02d %s %04d %02d:%02d:%02d GMT
DNS lookup error
<SocketStream %p>{flags = %p, read = %p, write = %p, socket = %@, properties = %p }
DiskCookieStorage changing policy from %d to %d, cookie file: %@
Multiple Choices
Bad Request
TransportConnection
_infersDiscretionaryFromOriginatingClient
_NSDictionaryType
] [
Sat
!DNSRecordIPAddresses.empty()
^v16@?0^{__CFReadStream=}8
v32@?0@\"NSObject\"8@\"NSObject\"16^B24
<CFURLCredential %p>{ identity = %@, certificate array = %@, persistence = %d}
closeWrite
entry
redirected
v24@?0q8@\"NSURLCredential\"16
HTTP/2.0 
x-cdn
BEGIN TRANSACTION
moved permanently
%p for name %s, port %d
Moved Permanently
_xpcActivityBudgeted
There was a problem communicating with the web proxy server (HTTP).
NSNetServicesErrorDomain
_preferredMaxParallelTasks
-[__NSCFLocalSessionTask _onqueue_suspendWorkQueue]
COMMIT;
privacyProxyFailClosedForUnreachableHosts
cache
*buffer
NSURLDownloadDecoders
%@
didReceiveData
SAwaitingTube
CFN_USE_HTTP3
AppSSO
ClientIdentifier
_received
; 
%p -- setting stream error to ENOTCONN
v32@?0Q8{?=qi}16
copyProperty_offqueue
*** -%s is not supported by %s
%@ { state %s, chunk state %s - INVALID, expected body length %ld  }>
header block for stream %llu is blocked
bytes=-%lld
NSErrorClientCertificateStateKey
*/*
useEnhancedPrivacyMode
v24@?0^{__CFRunLoop=}8^{__CFString=}16
%!PS-Adobe-
__CFNetworkCopyProxiesForAutoConfigurationScript_privatemode__
HTTPConnectionEvent
_kCFNTimingDataNStatAvgRTT
:method
NDBundleKey
CFNetwork SSLHandshake failed (%d)
isDirty
Stream
v16@?0@\"NSObject<OS_dispatch_data>\"8
isSharedSession
_requiresSustainedDataDelivery
Default Session Classes
status == ConnectionSearchStatus::NoConnection
Conflict
header_out_begin_static_nameref
-[__NSCFLocalSessionTask _onqueue_resumeWorkQueue]
<TABLE 
setStreamID
_decodedHeader
_authenticatorStatusCodes
Read Count
DELETE FROM cookies WHERE name = ? AND domain = ? AND path = ? AND partition = ?
HAR
payment required
ERROR: shrinkDB - unable to start a DB transaction.  Error-code=%d
DiskCookieStorage Construction
Task <%@>.<%lu>
HTTPMaximumConnectionsPerHost
_receivedHeadersBlocked
Classic Stream Client <%p>
vary state mismatch
called cachedResponseForRequest: with nil request
%d
__nsurlrequest_proto_props
KEYCHAIN_WEB_FORM_PASSWORD
gws
=%@
unimplemented
offset
kCFHTTPServerKeychain
Err-1006
streamInfo
Protocol PAC Timeout
v16@?0@\"NSObject<OS_xpc_object>\"8
i != -1
```
