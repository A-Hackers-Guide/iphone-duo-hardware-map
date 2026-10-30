# `/usr/lib/libTelephonyUtilDynamic.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,613,920 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 29 (Size: 4496)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (11)

- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/System/Library/Frameworks/CFNetwork.framework/CFNetwork (compatibility version 1.0.0, current version 3896.200.61)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (1 classes, 4 protocols)

Classes: `URLSessionDelegate`

Protocols: `NSObject`, `NSURLSessionDataDelegate`, `NSURLSessionDelegate`, `NSURLSessionTaskDelegate`

## Strings (876)

```
_privacyStance
backgroundSessionConfigurationWithIdentifier:
isEqualToString:
UUIDString
domain
isKindOfClass:
protectionSpace
defaultSessionConfiguration
setAllHTTPHeaderFields:
stringWithFormat:
.cxx_destruct
UTF8String
initWithURL:cachePolicy:timeoutInterval:
URLSession:task:didReceiveChallenge:completionHandler:
URLSession:task:needNewBodyStream:
credentialForTrust:
isMemberOfClass:
length
userInfo
URLSession:didBecomeInvalidWithError:
_setAllowsUCA:
hash
mutableCopy
addCallbackHandler:for:
setProperty:forKey:inRequest:
release
URLSession:task:didFinishCollectingMetrics:
conformsToProtocol:
stringValue
allHeaderFields
setMaxConcurrentOperationCount:
debugDescription
resume
setAllowsCellularAccess:
URLSession:dataTask:didReceiveResponse:completionHandler:
setTimeoutIntervalForResource:
set_tlsTrustPinningPolicyName:
setTLSMaximumSupportedProtocol:
autorelease
code
stringWithCString:encoding:
URLSession:dataTask:didBecomeStreamTask:
appendData:
isEqual:
credentialWithIdentity:certificates:persistence:
dataTaskWithRequest:
description
performSelector:withObject:
respondsToSelector:
isProxy
TQ,R
dataWithBytes:length:
setTLSMinimumSupportedProtocol:
URLSession:task:needNewBodyStreamFromOffset:completionHandler:
URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:
T@\"NSString\",R,C
initWithBase64EncodedString:options:
performSelector:withObject:withObject:
sessionWithConfiguration:delegate:delegateQueue:
cStringUsingEncoding:
localizedStringForStatusCode:
base64EncodedStringWithOptions:
_incompleteCurrentTaskTransactionMetrics
fTaskHandlers
retainCount
set_companionProxyPreference:
superclass
URLSession:dataTask:didReceiveData:
set_sourceApplicationSecondaryIdentifier:
URLSession:didReceiveChallenge:completionHandler:
URLSession:task:didCompleteWithError:
authenticationMethod
performSelector:
URL
URLSession:dataTask:willCacheResponse:completionHandler:
URLSession:task:willBeginDelayedRequest:completionHandler:
defaultCStringEncoding
drain
getContext:
setBoundInterfaceIdentifier:
serverTrust
_TLSNegotiatedCipherSuite
addOperation:
class
ephemeralSessionConfiguration
set_sourceApplicationBundleIdentifier:
URLSession:task:didReceiveInformationalResponse:
initWithBytesNoCopy:length:encoding:freeWhenDone:
invalidateAndCancel
setConnectionProxyDictionary:
setHTTPBody:
statusCode
T#,R
dealloc
URLSession:didCreateTask:
URLSessionDidFinishEventsForBackgroundURLSession:
blockOperationWithBlock:
initWithFormat:arguments:
removeCallbackFor:
T@\"NSString\",?,R,C
setHTTPMethod:
taskIdentifier
setURL:
retain
URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:
getBytes:length:
self
set_connectionCacheCellPurgeTimeout:
zone
.cxx_construct
URLSession:dataTask:didBecomeDownloadTask:
setWaitsForConnectivity:
URLSession:taskIsWaitingForConnectivity:
dataWithBytesNoCopy:length:freeWhenDone:
set_CTDataConnectionServiceType:
v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSData\"32
{map<unsigned long, std::shared_ptr<SessionTaskContext>, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, std::shared_ptr<SessionTaskContext>>>>=\"__tree_\"{__tree<std::__value_type<unsigned long, std::shared_ptr<Sess
@24@0:8:16
v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32
v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionStreamTask\"32
v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSCachedURLResponse\"32@?<v@?@\"NSCachedURLResponse\">40
@32@0:8:16@24
^{_NSZone=}16@0:8
v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32
v48@0:8@16@24q32@?40
v56@0:8@16@24q32q40q48
v40@0:8@16@24@32
v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLRequest\"32@?<v@?q@\"NSURLRequest\">40
v56@0:8@16@24@32@40@?48
v32@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24
v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLAuthenticationChallenge\"32@?<v@?q@\"NSURLCredential\">40
B24@0:8:16
Vv16@0:8
B24@0:8@\"Protocol\"16
v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32
v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLSessionTaskMetrics\"32
v16@0:8
{shared_ptr<SessionTaskContext>=^{SessionTaskContext}^{__shared_weak_count}}24@0:8q16
B24@0:8@16
@40@0:8:16@24@32
v32@0:8@\"NSURLSession\"16@\"NSError\"24
v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLResponse\"32@?<v@?q>40
v24@0:8q16
#16@0:8
@16@0:8
@\"NSString\"16@0:8
v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32q40q48
v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionDownloadTask\"32
B16@0:8
Q16@0:8
v40@0:8@16@24@?32
v48@0:8@16@24@32@?40
v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32@\"NSURLRequest\"40@?<v@?@\"NSURLRequest\">48
v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@?<v@?@\"NSInputStream\">32
v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32@?<v@?@\"NSInputStream\">40
v40@0:8{shared_ptr<ctu::Http::HttpRequestCallbackHandler>=^{HttpRequestCallbackHandler}^{__shared_weak_count}}16q32
B24@0:8#16
v32@0:8@16@24
v24@0:8@16
v24@0:8@\"NSURLSession\"16
TIMEOUT for message MIPC \\[|\\]
_TelephonyUtilUARTTransportWithTimeoutFreeInternal
ModelNumber
 bytes]
getRawErrorCode
Failed to configure RX Queue size of %u, err = %s (%u)\n
Trace
Message marked for automatic deletion
revoke
<nil>
CFDictionary(
Data Not Allowed
Background Session Was Disconnected
Always
DCS:Greek
)
ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\([a-zA-Z\\.]+\\) [0-9a-zA-Z]+\\(|-[0-9a-fA-F]+\\).*
received string parameter with no suffix (non-numeric) characters\n
Failed to launch write worker, ret = %s(%u)\n
{vector<std::string, std::allocator<std::string>>=^v^v{?=^v}}8@?0
Found no matching content in %s
Failed to do stack shot/simulate crash, reason '%s', asCrash %u\n
TelephonyUtilTransportCreateWithFile
write_to_completion
RegionCode
AtmPEO/j+Pdr8+WKxv4Aaw
kLogWriters
Uncompressed
0123456789abcdef
0123456789ABCDEF
com.apple.libtu.timerscaling.firstbootafterupdate
TelephonyUtilRingBufferInitialize
Failed to open file %s (error: %d(0x%x) (%s))
%lld:%s
TelephonyUtilTransportCreateWithUARTTimeout
.work
write to completion returned %s (%u)\n
{time_point<std::chrono::steady_clock, std::chrono::duration<long long, std::ratio<1, 1000000000>>>={duration<long long, std::ratio<1, 1000000000>>=q}}8@?0
Telephony operation timeout at '%s', timeout %u\n
us
null
setProxyServer
No Assertions
pop
Class 2
Out of memory!\n
Failed to get termios options, ret = %s (%u)\n
{unique_ptr<ctu::Timer, std::default_delete<ctu::Timer>>={?=^{Timer}}}8@?0
No Permissions To Read File
ProductVersion
setTimeout
Class 1
1
TelephonyUtilParseHardwareModel
Internal
Cannot Load From Network
Failed to map file %s (error: %d(0x%x) (%s))
open_file
..
Have a message class meaning
User Authentication Required
ms
Failed to open directory %s (error: %d(0x%x) (%s))
    
Notice
^\\[abmtool\\].*
/usr/lib/libRemoteTelephonyTransport.dylib
Failed to get clock service (error = %d)\n
Failed to change mode of destination file %s (error: %d(0x%x) (%s))
setProxySettings
k8BitData
strtoul failed with error no %d\n
setServiceType
^\\[bbutil\\] 
x
iPad
ctu:log
getResponseStatusLine
for client\\(
read returned %s (%u)\n
NO
Creating with baud %u, Rx Queue size %u, local queue size %u\n
Timeout
v
$1-
Note: 
DCS:Unspecified
ReleaseType
Not Supported\n
HWModelStr
Attempted to dispatch on a connector with no queue!
' in domain '
ResetReasonEncoder
ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\([a-zA-Z\\.]+\\) [0-9a-zA-Z]+\\([0-9]+-|\\).*
Bad URL
g
terminate
 log messages dropped prior to log start
state
_TelephonyUtilUARTTransportConfigureVMIN
_TelephonyUtilTransportFileWrite
App Transport Security Requires Secure Connection
International Roaming Off
EOSHalleyConfiguration
registerDataSendCodeblock
ARI_CLI_ERR - Tracking receipt of unrecognized transaction 
TIMEOUT for message MIPC.*?Client=.*?Msg=.*?Trx=.*? 
SIM
Unsupported URL
Error
setStreamProperty
kLoggers
ARI_CLI_ERR - All transaction IDs exhausted for msg\\(.*\\), for client\\(0[xX][0-9a-fA-F]+\\)
_
malloc failed for proc list
fHighestQueue
Cannot Decode Content Data
Cannot Remove File
GZIP
getPrivateRelayEnabled
revoked
v24@?0{connection={object=^v}}8{dict={object=^v}}16
failed to flush, err = %s (%u)\n
REST API Misuse: %s
copy_file
DCS:Spanish
Failed to get filesystem statistics pertaining to path %s (error: %d(0x%x) (%s))
No diagnostic information available.
Capacity %u is not a power of two\n
Failed to get status of source file %s (error: %d(0x%x) (%s))
get_filtered_files
BuildVersion
kLogMessage
!dDtor
Server Certificate Has Bad Date
n
provider
Client Certificate Rejected
Failed to write to file descriptor %d (error: %d(0x%x) (%s))
ProductType
DCS:Russian
kLogMessageTimestamp
^\\[abmtool\\] 
watched
HEAD
+
DCS:Icelandic
\\s+
kGranted
kPending
Failed to write\n
 bytes)
Baseband request for reset for FS Sync
DCS:English
DCS:Dutch
/usr/local/lib/libRemoteTelephonyTransport.dylib
generation
 crashed
???
 keys)
kGSM7
kKSC5601
DCS:Finnish
detected hardware model info string without alphabetical prefix\n
logmaster::
DCS:Hebrew
\t\tNumeric Arguments:\n
/dev/uart.debug
{dict={object=^v}}8@?0
?
ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\([a-zA-Z\\.]+\\) [0-9a-zA-Z]+\\([0-9]+-[0-9a-fA-F]+\\) SZ\\(|\\) TRX\\(0x[0-9a-f]+\\) AP\\.SEQ\\(0x[0-9a-f]+\\).*
8bit data encoding
Watch
Spanish
BBUpdater error  [0-9]+
^\\[bbutil\\].*
_TelephonyUtilUARTTransportWithTimeoutFlushRead
setRequestBody
setClientCert
setValidateCertsCallback
Failed get attributes, err = %s (%d)\n
kLogMessageLevel
FALSE
CONTENT-ENCODING
Fax message waiting
Got client checkin for client '
basic_string
Q8@?0
^([/_\\-[:alnum:]]*)(.*)
std::exception::what: 
Reserved, no message class meaning
Background Session Requires Shared Container
Background Session In Use By Another Process
Dynamic exception type: 
setBackgroundConfiguration
DCS:Polish
(null)
setServerPinnedCerts
Telephony watchdog fired: %s\n
0
Restore
_TelephonyUtilUARTTransportWrite
.highest
close_file
start
AP forced coredump via SPMI - Please analyze reason from AP perspective
\t\tFree Text:\t
kIdle
_TelephonyUtilTransportFDRead
UniqueDeviceID
e
Client disconnected (
PrevOSVersion
WriteStackshotReport
DCS:Hungarian
Gsm7 encoding
GNSS [0-9]+
\t\tError Code:\t
a
ResultIsEmptyError: the result was never set with a success or error value
get_partition_info
set
Unknown exception.
Callback queue was never set; can't send response!
Set indication active
, but no client found: 
*
FPGA
Server Certificate Not Yet Valid
Cannot Create File
%llu:%s
Got client error for conn 
EnableOversteer
Server Certificate Untrusted
context->source
Cannot Decode Raw Data
Failed to change mode of file %s to (0x%x) (error: %d(0x%x) (%s))
): 
kCTDataConnectionServiceTypeInternet
XPC_ERROR(
setSharedConfiguration
Class 3
Flushing\n
ResultIsNotError: cannot return an error unless it was an error
(unknown)
setSourceApplicationBundleIdentifier
CFData(
Timed Out
File Does Not Exist
Resetting baseband 
stripLongPrefix
RestModule::connect cannot be called with a null connector
debug
HTTP Too Many Redirects
Cannot Close File
ping
'
com.apple.telephony
BootSessionUUID
r
s
-[[:alnum:]]*
Attempted to send message on a disconnected connector.
Voicemail message waiting
%s: argument cannot be NULL\n
MGCopyMultipleAnswers
Unknown Error
Cannot set up a period of 0 time; that would be insane!
GET
Unable to load CrashReporterSupport framework.\n
/connections
_create_directory
^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8
DCS:Arabic
)\n
failed to read, err = %s (%u)\n
Invalid URL
IsVirtualDevice
DeviceIsNED
PUT
Vendor
_TelephonyUtilTransportFileFlushRead
%F %T %Z
<expired>
grant
Cannot Write To File
Failed to configure VMIN of %u, err = %s (%u)\n
Freeing\n
Client Certificate Required
MGCopyAnswer
DeviceName
Throw in function 
getHttpResponseCode
TelephonyUtilTransportCreateWithFD
isProcessRunning
timer
{time_point<std::chrono::system_clock, std::chrono::duration<long long, std::ratio<1, 1000000>>>={duration<long long, std::ratio<1, 1000000>>=q}}8@?0
DispatchTimerService
CONNECT
Fatal
aborting because stripLongPrefix failed\n
%s: spawning %s failed! ret: %d\n
TelephonyBasebandWatchdogStartWithStackshot_block_invoke
DELETE
OPTIONS
Data coding/message class
PCI-EVENT: pci error: .*
PCI-EVENT: pci error: 
 elements)
Cannot Open File
dyn_cast to uint64_t requires nonnegative values
o
C8@?0
setOnDemand
AP
timerScaling.firstbootafterupdate
/
Failed to unlink file %s (error: %d(0x%x) (%s))
DCS:INVALID LANGUAGE
Invalid current byte position
Failed to remove file %s (error: %d(0x%x) (%s))
notify
Electronic mail message waiting
Failed to close file %s (error: %d(0x%x) (%s))
green-tea
getResponseCFData
DCS:French
kKSC5601 encoding
%s: parameter cannot be NULL.\n
TRUE
-%u
/private/var/wireless/Library/Preferences/com.apple.commcenter.plist
unknown
Failed to configure baud of %u, err = %s (%u)\n
unknown boost::container exception
.
TRACE
setBackgroundConfigurationWithUniqueIdentifier
Callback functor was never set; can't send response!
Other message waiting
B24@?0r*8^v16
Header does not exist
disabled
CurrentOSVersion
.normal
h
,
SimulateCrash
Got request for new logger, but check in failed
rest.xpc
Info
Compressed
TelephonyUtilTransportCreateWithFDPrivate
%s
failed to open node (%s), ret = %s(%u)\n
Never
(ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\(([a-zA-Z]+\\.){0,}|\\) [0-9a-zA-Z]+\\([0-9]+-[0-9a-fA-F]+\\) SZ\\([0-9]+\\) TRX\\(0x[0-9a-f]+\\) AP\\.SEQ\\(0x[0-9a-f]+\\).*)
/private/var/wireless/Library/Preferences/com.apple.AppleBasebandManager.plist
MaxPacketSize
Invalid Request
enabled
Cannot Find Host
\": 
push
Server error: 
Portuguese
_TelephonyUtilTransportFileUnblockRead
UCS2 encoding
v16@?0^v8
0x
Debug
\t\t\t[
 (0x
kern.wakereason
FirstBootAfterUpdate
second sysctl() failed with err = %d
Data Length Exceeds Maximum
Returning trivial time since clock service is unavailable\n
modem boot up failure \\[.+\\]
first sysctl() failed with err = %d
Redirect To Non Existent Location
kDomainLogLevels
get_next_capacity, allocator's max size reached
Call Is Active
t
remove_file
DeviceCoverGlassMaterial
TelephonyUtilLoadCrashSupport_block_invoke
{duration<long long, std::ratio<1, 1000000>>=q}8@?0
Bad Server Response
Reserved, used for KTF, KSC5601 encoding
vector
load
registerDataReceiveCodeblock
': method appears not to have been called
%s: environment cannot be NULL\n
Receive queue size %u exceeds max %u\n
DCS:German
ARI_CLI_ERR - Tracking receipt of unrecognized transaction 0[xX][0-9a-fA-F]+
/usr/lib/libMobileGestalt.dylib
Not Connected To Internet
File Is Directory
SIMDEV
getResult
setWaitForConnectivityTimeout
false
Unset
setSourceIdentifier
Failed set speed, err = %s (%d)\n
%s: command cannot be NULL\n
granted
fNormalQueue
Server Certificate Has Unknown Root
Failed to close directory %s (error: %d(0x%x) (%s))
DCS:Portuguese
Message Waiting Indication group: Store message (UCS2)
\tParsed Reason:\n
Download Decoding Failed Mid Stream
v16@?0^{dirent=QQSSC[1024c]}8
registerCallbackQueue
configure
DCS:Norweigian
Class unspecified
(Baseband got stuck in data context | state: resetting baseband)
Resetting baseband .*?
NonUI
getResponseHeaders
setRedirection
kUCS2
_TelephonyUtilUARTTransportConfigureFlowControl
getTLSNegotiatedCipherSuite
setConnectionCacheCellPurgeTimeout
Assertions remaining: 
NVRAMDictionary
(msg\\(|\\), for client)
Cannot Parse Response
Apple Watch
setTLSPolicyName
Request DENIED for new logger '
com.apple.telephony.util
modem boot up failure \\[|\\]
\n
watchers
process %s exists? %{bool}d
createPeriodicTimerImpl
Throw location unknown (consider using BOOST_THROW_EXCEPTION)\n
DCS:Danish
received zero-length string parameter\n
received string with length exceeding maximum int value
received string parameter without non-numeric prefix\n
createOneShotTimerImpl
Cannot Connect To Host
Cannot Move File
RestoreOSBuild
TelephonyUtilWriteStackshotWithExcCode
Mac
Failed to read source file %s (error: %d(0x%x) (%s))
: 
Message waiting indication group: Store message (GSM-7)
kLogMessageMetadata
Failed to open transport to communicate with baseband.*
_TelephonyUtilUARTTransportConfigureRxQueueSize
Failed to unmap file %s (error: %d(0x%x) (%s))
getErrorRef
Turkish
waiting
_TelephonyUtilTransportFileRead
Failed to close file descriptor %d (error: %d(0x%x)) (%s)
setCompanionProxyPreference
DEV
_TelephonyUtilTransportUARTWithTimeoutCreateInternal
b
getResponseString
kLoggerDomain
Failed to get time from clock service (error = %d); returning trivial time\n
p
iterate_folder
rename_directory_unique
true
setMaxAllowedRedirects
None
EnableBBSimulation
_TelephonyUtilUARTTransportWithTimeoutFree
$2
registerCompletionCodeblock
DCS:Turkish
Request Body Stream Exhausted
rename
baseband
Secure Connection Failed
d
B24@?0Q8^v16
{endpoint={object=^v}}8@?0
 
Carrier
kern.bootsessionuuid
Failed to create pipe FD's, err = %s (%u)\n
Zero Byte Resource
Failed to rename %s -> %s (error: %d(0x%x) (%s))
VendorNonUI
write returned %s (%u)\n
CFArray(
kLoggerLevel
kern.boottime
unload
-
Baseband got stuck in data context .* state: resetting baseband
filesystem flush operation failed -- check ARI and BB state --
v8@?0
Failed to set termios options, ret = %s (%u)\n
Failed to launch read worker, ret = %s(%u)\n
Failed Lookup
Connection
Unknown
ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\([a-zA-Z\\.]+\\) [0-9a-zA-Z]+\\([0-9]+-[0-9a-fA-F]+\\) SZ\\([0-9]+\\) TRX\\(|\\) AP\\.SEQ\\(0x[0-9a-f]+\\).*
%04x  %s
aborting to prevent out-of-bounds access while copying 1-character alphabetical prefix\n
Failed to close, err = %s(%u)\n
RegionInfo
bUJD9zcOcitJwFA0ieIkxA
DCS:Swedish
iPhone
Desense
MockTimerService
User Cancelled Authentication
] 
ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\([a-zA-Z\\.]+\\) [0-9a-zA-Z]+\\([0-9]+-[0-9a-fA-F]+\\) SZ\\([0-9]+\\) TRX\\(0x[0-9a-f]+\\) AP\\.SEQ\\(0x[0-9a-f]+\\).*
TIMEOUT for message MIPC .*?
com.apple.commcenter
DCS:Italian
Class 0
Download Decoding Failed To Complete
TelephonyUtilRunCommandExt
Failed to open file %s, args %s, err = %s (%u)\n
YES
File Outside Safe Area
ResultIsError: cannot return a result because the operation was an error
HasBaseband
setAllowUltraConstrained
Failed set attributes, err = %s (%d)
[
::writers
DCS:Czech
1.2.12
<Allocator %p: %s>
DNS Lookup Failed
ns
Set indication inactive
chmod
POST
setAllowCellularAccess
get
General data coding indication
aborting to prevent out-of-bounds access while copying suffix (non-numeric) characters\n
SIMAP
com.apple.libtu.scaledtimeoverride
Failed to make directory %s with mode 0x%x (error: %d(0x%x) (%s))
Warn
EmptyMockCallArgsException for method '
Hindi
ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\([a-zA-Z\\.]+\\) [0-9a-zA-Z]+\\([0-9]+-[0-9a-fA-F]+\\) SZ\\([0-9]+\\) TRX\\(0x[0-9a-f]+\\) AP\\.SEQ\\(|\\).*
aborting to prevent out-of-bounds access while copying numeric characters\n
FPGADEV
_TelephonyUtilTransportFDWrite
_TelephonyUtilUARTTransportConfigureBaudRate
Baseband ARI engage timeout
kLoggerName
Message waiting indication group: Discard message
 * timer fired
Unable to find MGCopyAnswer function
%s: Failed to get status of source file %s (error: %d(0x%x) (%s))
Could not convert state information for %s to serialized CFDataRef: %{public}s
%s: aborting to prevent out-of-bounds access while copying suffix (non-numeric) characters\n
\"First Boot After Update\" scenario detected (os version pref mismatch in same boot)
\"First Boot After Update\" scenario detected (os version mismatch across different boot)
%s: failed to open node (%s), ret = %s(%u)\n
%s: received zero-length string parameter\n
%s: Failed to configure VMIN of %u, err = %s (%u)\n
%s: Failed to set termios options, ret = %s (%u)\n
%s: aborting to prevent out-of-bounds access while copying 1-character alphabetical prefix\n
%s: detected hardware model info string without alphabetical prefix\n
 Time advancing by %{public}s
 System time advancing by %{public}s
%s: Failed to close directory %s (error: %d(0x%x) (%s))
%s: write to completion returned %s (%u)\n
Detected a WiFi iPad
Unable to copy MobileGestalt hardware model string into local buffer
\"First Boot After Update\" scaling timer expired
%s: Not Supported\n
Unable to determine whether this is a virtual device
%s: Failed to open directory %s (error: %d(0x%x) (%s))
%s: Failed to write to file descriptor %d (error: %d(0x%x) (%s))
%s: Failed to rename %s -> %s (error: %d(0x%x) (%s))
Could not collect state information for '%{public}s
%s: process %s exists? %{bool}d
%s: Failed to get termios options, ret = %s (%u)\n
 + created timer
Entitlement policy not used by RestXpcListener. Clients always allowed
Oversteer disabled due to key not set
%s: Telephony watchdog fired: %s\n
%s: Failed to unlink file %s (error: %d(0x%x) (%s))
Uncaught C++ exception! Diagnostics follow, then crashing!\n========== Diagnostic info:\n%{public}s========== Backtrace:\n%{public}s\n==========
Server pinned certs' trust evaluation failed due to STATUS code: %d
BBSimulation disabled due to key not set
Failed to read kern boot time, error: %s
%s: Freeing\n
Failed to load MobileGestalt library
Failed to set hardware model info based on hardware model string '%s'
%s: Failed to get filesystem statistics pertaining to path %s (error: %d(0x%x) (%s))
Uncaught Boost C++ exception! Diagnostics follow, then crashing!\n========== Diagnostic info:\n%{public}s========== Backtrace:\n%{public}s\n==========
Oversteer %s
Init
%s: Out of memory!\n
%s: Failed to create pipe FD's, err = %s (%u)\n
[%s] Scaled timeout value %llu microseconds
%s: Failed to change mode of file %s to (0x%x) (error: %d(0x%x) (%s))
std::terminate() called but there's no exception. Crashing! ========== Backtrace:\n%{public}s\n==========
Could not obtain %d state data for '%{public}s'
%s: malloc failed for proc list
%s: failed to flush, err = %s (%u)\n
%s: Failed to read source file %s (error: %d(0x%x) (%s))
%s: aborting because stripLongPrefix failed\n
%s: first sysctl() failed with err = %d
%s: Failed to launch write worker, ret = %s(%u)\n
Successfully set the hardware model info
Missing name for state capture
DEBUG: Failed to validate certs.
%s: Failed set speed, err = %s (%d)\n
Failed to parse out submatch with pattern %s
%s: received string parameter without non-numeric prefix\n
Telephony watchdog fired: %s\n
An error occurred converting decimal string argument %s to unsigned integer
%s: Failed to map file %s (error: %d(0x%x) (%s))
Created %zu bytes of CFDataRef state for %s
Detected an unsupported non-baseband device
%s: Failed to change mode of destination file %s (error: %d(0x%x) (%s))
%s: Failed to do stack shot/simulate crash, reason '%s', asCrash %u\n
%s: Failed get attributes, err = %s (%d)\n
%s
%s: Receive queue size %u exceeds max %u\n
%s: Failed to remove file %s (error: %d(0x%x) (%s))
%s: Failed set attributes, err = %s (%d)
%s: write returned %s (%u)\n
Client [%d] is not entitled and thus is rejected
Missing callback for state capture
Detected virtual device, so treating it as unknown Telephony product
Detected a WiFi Watch
DEBUG: Server pinned certs' trust evaluation failed due to RESULT code: %u
Failed to get boot session uuid, error: %s
Uncaught exception of unknown type (it's not C++ or ObjC)! Crashing! ========== Backtrace:\n%{public}s\n==========
Uncaught ObjC exception! Diagnostics follow, then crashing!\n========== Diagnostic info:\nuserInfo = %{public}@\n%{public}@\n========== Backtrace:\n%{public}s\n
A problem occurred trying to parse reason string \"%s\", so attempting to send as much of the raw reason string as will fit
Attempting to parse and encode reason string: \"%s\"
Starting \"First Boot After Update\" expiry timer with %lld seconds
%s: read returned %s (%u)\n
Detected a baseband device with hardware model string '%s'
%s: Failed to make directory %s with mode 0x%x (error: %d(0x%x) (%s))
State capture for %s greater than maximum %d bytes in size: %zu
\"First Boot After Update\" scenario detected (boot session doesn't exist)
%s: Failed to open file %s (error: %d(0x%x) (%s))
[conn %s (%p)] Sending reply: %s
%s: Flushing\n
%s: Failed to close file %s (error: %d(0x%x) (%s))
input timeOut: %llu usec, scaled output timeOut: %llu usec
Could not obtain state data for '%{public}s'
Platform Simulation disabled due to 'libRemoteTelephonyTransport' not found
%s: second sysctl() failed with err = %d
%s: Failed to open file %s, args %s, err = %s (%u)\n
%s: Failed to write\n
%s: failed to read, err = %s (%u)\n
Sending NOTIFY to %s (%p): %s
%s: strtoul failed with error no %d\n
BBSimulation %s
Oversteer disabled due to 'libRemoteTelephonyTransport' not found
Invalid expiry time (%lld s) passed for scenario
Unable to determine the device name
Detected unexpected type in the MobileGestalt device name
Lost track of default stdlib terminate handler
An error occurred converting hex string argument %s to unsigned integer
Successfully encoded reason string: \"%s\"
Failed to encode reason string: \"%s\"
Invalid scaling factor (%u) passed for scenario
%s: Found no matching content in %s
Collecting state for '%{public}s'
%s: received string with length exceeding maximum int value
%s: Failed to close file descriptor %d (error: %d(0x%x)) (%s)
Unexpected return from no-return handler
Expected to find a text argument, but none was found
%s: received string parameter with no suffix (non-numeric) characters\n
%s: Failed to launch read worker, ret = %s(%u)\n
Reason string \"%s\" did not match any existing regex pattern
Enough uptime, not starting \"First Boot After Update\" expiry timer
%s: Failed to configure baud of %u, err = %s (%u)\n
%s: Failed to close, err = %s(%u)\n
cBS: %s, cOS: %s, cBSPref: %s, cOSPref: %s, pOSPref: %s
%s: Capacity %u is not a power of two\n
%s: Creating with baud %u, Rx Queue size %u, local queue size %u\n
State capture expired
%s: Unable to load CrashReporterSupport framework.\n
New REST XPC client has no valid connection
Treating device as unknown Telephony product due error determining hardware model info from MobileGestalt query
Detected unexpected type in the MobileGestalt hardware model string
%s: Failed to unmap file %s (error: %d(0x%x) (%s))
Sending GET to %s (%p): %s
%s: aborting to prevent out-of-bounds access while copying numeric characters\n
Failed to encode parsed reason because the size of the numeric arguments (%zu bytes) exceeds the maximum size (%d bytes) of the reset reason
uptime: %lld seconds, scenario expiry: %lld seconds
Unable to determine whether device has baseband
Unable to determine the hardware model string
Reason string \"%s\" parsed to:\n%s
%s: Failed to configure RX Queue size of %u, err = %s (%u)\n
URLSessionDelegate
NSURLSessionTaskDelegate
NSURLSessionDelegate
NSObject
NSURLSessionDataDelegate
```
