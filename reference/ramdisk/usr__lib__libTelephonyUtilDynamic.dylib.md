# `/usr/lib/libTelephonyUtilDynamic.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,613,920 bytes.

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
Failed to encode parsed reason because the size of the numeric arguments (%zu bytes) exceeds the maximum size (%d bytes) of the reset reason
 System time advancing by %{public}s
[conn %s (%p)] Sending reply: %s
%s
%s: Failed to get termios options, ret = %s (%u)\n
%s: Failed to close file descriptor %d (error: %d(0x%x)) (%s)
DEBUG: Failed to validate certs.
An error occurred converting decimal string argument %s to unsigned integer
%s: received string parameter with no suffix (non-numeric) characters\n
cBS: %s, cOS: %s, cBSPref: %s, cOSPref: %s, pOSPref: %s
%s: Failed to change mode of file %s to (0x%x) (error: %d(0x%x) (%s))
Successfully encoded reason string: \"%s\"
Oversteer %s
%s: Failed to create pipe FD's, err = %s (%u)\n
%s: Freeing\n
%s: Failed to launch read worker, ret = %s(%u)\n
Missing name for state capture
%s: malloc failed for proc list
%s: Failed to close, err = %s(%u)\n
%s: Failed to get status of source file %s (error: %d(0x%x) (%s))
%s: Failed to unlink file %s (error: %d(0x%x) (%s))
Attempting to parse and encode reason string: \"%s\"
Oversteer disabled due to key not set
Failed to read kern boot time, error: %s
%s: Creating with baud %u, Rx Queue size %u, local queue size %u\n
 * timer fired
%s: Failed to read source file %s (error: %d(0x%x) (%s))
Reason string \"%s\" did not match any existing regex pattern
BBSimulation %s
Failed to get boot session uuid, error: %s
%s: Out of memory!\n
 Time advancing by %{public}s
State capture expired
Created %zu bytes of CFDataRef state for %s
DEBUG: Server pinned certs' trust evaluation failed due to RESULT code: %u
%s: received string with length exceeding maximum int value
%s: write returned %s (%u)\n
Treating device as unknown Telephony product due error determining hardware model info from MobileGestalt query
Unable to find MGCopyAnswer function
Detected unexpected type in the MobileGestalt hardware model string
Failed to parse out submatch with pattern %s
Detected unexpected type in the MobileGestalt device name
Server pinned certs' trust evaluation failed due to STATUS code: %d
%s: received zero-length string parameter\n
%s: Not Supported\n
%s: Failed to get filesystem statistics pertaining to path %s (error: %d(0x%x) (%s))
%s: detected hardware model info string without alphabetical prefix\n
%s: aborting to prevent out-of-bounds access while copying suffix (non-numeric) characters\n
input timeOut: %llu usec, scaled output timeOut: %llu usec
%s: read returned %s (%u)\n
Telephony watchdog fired: %s\n
Unable to determine the hardware model string
%s: Failed get attributes, err = %s (%d)\n
[%s] Scaled timeout value %llu microseconds
%s: Failed to rename %s -> %s (error: %d(0x%x) (%s))
%s: aborting to prevent out-of-bounds access while copying numeric characters\n
uptime: %lld seconds, scenario expiry: %lld seconds
%s: Failed to configure baud of %u, err = %s (%u)\n
%s: Failed to write to file descriptor %d (error: %d(0x%x) (%s))
Uncaught exception of unknown type (it's not C++ or ObjC)! Crashing! ========== Backtrace:\n%{public}s\n==========
Uncaught C++ exception! Diagnostics follow, then crashing!\n========== Diagnostic info:\n%{public}s========== Backtrace:\n%{public}s\n==========
An error occurred converting hex string argument %s to unsigned integer
A problem occurred trying to parse reason string \"%s\", so attempting to send as much of the raw reason string as will fit
Entitlement policy not used by RestXpcListener. Clients always allowed
%s: failed to flush, err = %s (%u)\n
Successfully set the hardware model info
%s: Failed to make directory %s with mode 0x%x (error: %d(0x%x) (%s))
std::terminate() called but there's no exception. Crashing! ========== Backtrace:\n%{public}s\n==========
Uncaught Boost C++ exception! Diagnostics follow, then crashing!\n========== Diagnostic info:\n%{public}s========== Backtrace:\n%{public}s\n==========
Sending NOTIFY to %s (%p): %s
%s: Unable to load CrashReporterSupport framework.\n
\"First Boot After Update\" scenario detected (os version pref mismatch in same boot)
Unable to determine whether device has baseband
Detected a WiFi Watch
%s: Failed to map file %s (error: %d(0x%x) (%s))
%s: Failed set speed, err = %s (%d)\n
Client [%d] is not entitled and thus is rejected
Detected virtual device, so treating it as unknown Telephony product
Detected an unsupported non-baseband device
%s: Failed to close directory %s (error: %d(0x%x) (%s))
%s: Failed to unmap file %s (error: %d(0x%x) (%s))
%s: Failed to change mode of destination file %s (error: %d(0x%x) (%s))
Uncaught ObjC exception! Diagnostics follow, then crashing!\n========== Diagnostic info:\nuserInfo = %{public}@\n%{public}@\n========== Backtrace:\n%{public}s\n
BBSimulation disabled due to key not set
Oversteer disabled due to 'libRemoteTelephonyTransport' not found
%s: Failed to write\n
New REST XPC client has no valid connection
Lost track of default stdlib terminate handler
Could not obtain state data for '%{public}s'
State capture for %s greater than maximum %d bytes in size: %zu
%s: Failed to do stack shot/simulate crash, reason '%s', asCrash %u\n
%s: strtoul failed with error no %d\n
Unexpected return from no-return handler
\"First Boot After Update\" scenario detected (os version mismatch across different boot)
%s: Flushing\n
%s: Failed to launch write worker, ret = %s(%u)\n
Failed to load MobileGestalt library
Unable to determine whether this is a virtual device
%s: aborting because stripLongPrefix failed\n
Invalid expiry time (%lld s) passed for scenario
Collecting state for '%{public}s'
Could not convert state information for %s to serialized CFDataRef: %{public}s
Expected to find a text argument, but none was found
%s: aborting to prevent out-of-bounds access while copying 1-character alphabetical prefix\n
%s: Failed to open file %s, args %s, err = %s (%u)\n
%s: failed to read, err = %s (%u)\n
Unable to copy MobileGestalt hardware model string into local buffer
Invalid scaling factor (%u) passed for scenario
Starting \"First Boot After Update\" expiry timer with %lld seconds
%s: Failed to set termios options, ret = %s (%u)\n
 + created timer
Detected a WiFi iPad
%s: first sysctl() failed with err = %d
%s: Failed to configure VMIN of %u, err = %s (%u)\n
Failed to set hardware model info based on hardware model string '%s'
%s: Failed to open directory %s (error: %d(0x%x) (%s))
%s: Failed to close file %s (error: %d(0x%x) (%s))
Reason string \"%s\" parsed to:\n%s
Unable to determine the device name
%s: Failed to open file %s (error: %d(0x%x) (%s))
Missing callback for state capture
Init
Enough uptime, not starting \"First Boot After Update\" expiry timer
%s: second sysctl() failed with err = %d
%s: Receive queue size %u exceeds max %u\n
%s: Failed to remove file %s (error: %d(0x%x) (%s))
Sending GET to %s (%p): %s
Failed to encode reason string: \"%s\"
%s: Capacity %u is not a power of two\n
%s: process %s exists? %{bool}d
%s: failed to open node (%s), ret = %s(%u)\n
\"First Boot After Update\" scenario detected (boot session doesn't exist)
%s: write to completion returned %s (%u)\n
%s: Telephony watchdog fired: %s\n
Detected a baseband device with hardware model string '%s'
%s: received string parameter without non-numeric prefix\n
Could not obtain %d state data for '%{public}s'
Platform Simulation disabled due to 'libRemoteTelephonyTransport' not found
\"First Boot After Update\" scaling timer expired
%s: Failed to configure RX Queue size of %u, err = %s (%u)\n
%s: Found no matching content in %s
Could not collect state information for '%{public}s
%s: Failed set attributes, err = %s (%d)
URLSessionDelegate
NSURLSessionTaskDelegate
NSURLSessionDelegate
NSObject
NSURLSessionDataDelegate
URL
initWithFormat:arguments:
isEqual:
set_tlsTrustPinningPolicyName:
URLSession:dataTask:didBecomeStreamTask:
setTLSMinimumSupportedProtocol:
URLSession:task:didFinishCollectingMetrics:
URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:
URLSession:task:needNewBodyStream:
backgroundSessionConfigurationWithIdentifier:
URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:
description
performSelector:withObject:withObject:
setAllowsCellularAccess:
getContext:
initWithURL:cachePolicy:timeoutInterval:
sessionWithConfiguration:delegate:delegateQueue:
.cxx_construct
protectionSpace
URLSession:task:didReceiveInformationalResponse:
setHTTPBody:
set_CTDataConnectionServiceType:
setTLSMaximumSupportedProtocol:
T#,R
URLSession:didCreateTask:
URLSession:taskIsWaitingForConnectivity:
URLSessionDidFinishEventsForBackgroundURLSession:
UUIDString
length
setAllHTTPHeaderFields:
dataWithBytes:length:
setProperty:forKey:inRequest:
setBoundInterfaceIdentifier:
release
fTaskHandlers
getBytes:length:
isEqualToString:
initWithBase64EncodedString:options:
retainCount
invalidateAndCancel
removeCallbackFor:
retain
setURL:
_TLSNegotiatedCipherSuite
isKindOfClass:
mutableCopy
setConnectionProxyDictionary:
URLSession:task:needNewBodyStreamFromOffset:completionHandler:
initWithBytesNoCopy:length:encoding:freeWhenDone:
set_sourceApplicationBundleIdentifier:
set_sourceApplicationSecondaryIdentifier:
cStringUsingEncoding:
code
URLSession:dataTask:didBecomeDownloadTask:
URLSession:didBecomeInvalidWithError:
_incompleteCurrentTaskTransactionMetrics
hash
isProxy
dealloc
URLSession:task:didReceiveChallenge:completionHandler:
defaultCStringEncoding
set_connectionCacheCellPurgeTimeout:
setMaxConcurrentOperationCount:
blockOperationWithBlock:
debugDescription
performSelector:withObject:
setTimeoutIntervalForResource:
set_companionProxyPreference:
stringValue
TQ,R
performSelector:
URLSession:dataTask:didReceiveResponse:completionHandler:
drain
stringWithCString:encoding:
taskIdentifier
_privacyStance
defaultSessionConfiguration
ephemeralSessionConfiguration
T@\"NSString\",R,C
authenticationMethod
conformsToProtocol:
resume
self
base64EncodedStringWithOptions:
autorelease
URLSession:task:didCompleteWithError:
addCallbackHandler:for:
appendData:
dataTaskWithRequest:
respondsToSelector:
URLSession:dataTask:willCacheResponse:completionHandler:
URLSession:didReceiveChallenge:completionHandler:
dataWithBytesNoCopy:length:freeWhenDone:
serverTrust
credentialForTrust:
URLSession:task:willBeginDelayedRequest:completionHandler:
domain
isMemberOfClass:
setHTTPMethod:
userInfo
_setAllowsUCA:
credentialWithIdentity:certificates:persistence:
statusCode
zone
allHeaderFields
UTF8String
addOperation:
class
T@\"NSString\",?,R,C
superclass
stringWithFormat:
.cxx_destruct
setWaitsForConnectivity:
URLSession:dataTask:didReceiveData:
localizedStringForStatusCode:
v32@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24
v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLSessionTaskMetrics\"32
v40@0:8{shared_ptr<ctu::Http::HttpRequestCallbackHandler>=^{HttpRequestCallbackHandler}^{__shared_weak_count}}16q32
@24@0:8:16
B24@0:8:16
v40@0:8@16@24@32
v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLAuthenticationChallenge\"32@?<v@?q@\"NSURLCredential\">40
v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32
v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLResponse\"32@?<v@?q>40
v16@0:8
@40@0:8:16@24@32
B24@0:8#16
v48@0:8@16@24@32@?40
v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32@\"NSURLRequest\"40@?<v@?@\"NSURLRequest\">48
v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32q40q48
v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionDownloadTask\"32
B24@0:8@16
#16@0:8
B16@0:8
B24@0:8@\"Protocol\"16
v40@0:8@16@24@?32
v24@0:8q16
v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32
v56@0:8@16@24q32q40q48
v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32
v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSData\"32
v24@0:8@16
v56@0:8@16@24@32@40@?48
{shared_ptr<SessionTaskContext>=^{SessionTaskContext}^{__shared_weak_count}}24@0:8q16
{map<unsigned long, std::shared_ptr<SessionTaskContext>, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, std::shared_ptr<SessionTaskContext>>>>=\"__tree_\"{__tree<std::__value_type<unsigned long, std::shared_ptr<Sess
@16@0:8
@32@0:8:16@24
Vv16@0:8
v32@0:8@16@24
v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32@?<v@?@\"NSInputStream\">40
v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionStreamTask\"32
v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSCachedURLResponse\"32@?<v@?@\"NSCachedURLResponse\">40
Q16@0:8
@\"NSString\"16@0:8
v32@0:8@\"NSURLSession\"16@\"NSError\"24
v24@0:8@\"NSURLSession\"16
v48@0:8@16@24q32@?40
v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLRequest\"32@?<v@?q@\"NSURLRequest\">40
v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@?<v@?@\"NSInputStream\">32
^{_NSZone=}16@0:8
\tParsed Reason:\n
Internal
': method appears not to have been called
kGSM7
(Baseband got stuck in data context | state: resetting baseband)
Connection
TelephonyUtilTransportCreateWithFDPrivate
File Outside Safe Area
iterate_folder
PCI-EVENT: pci error: .*
Baseband request for reset for FS Sync
/usr/local/lib/libRemoteTelephonyTransport.dylib
unknown
fNormalQueue
Message waiting indication group: Discard message
.normal
setAllowUltraConstrained
Unknown
DCS:English
registerDataReceiveCodeblock
setClientCert
filesystem flush operation failed -- check ARI and BB state --
com.apple.libtu.scaledtimeoverride
Telephony watchdog fired: %s\n
ns
registerDataSendCodeblock
ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\([a-zA-Z\\.]+\\) [0-9a-zA-Z]+\\([0-9]+-|\\).*
get_next_capacity, allocator's max size reached
_TelephonyUtilTransportUARTWithTimeoutCreateInternal
t
..
Throw location unknown (consider using BOOST_THROW_EXCEPTION)\n
PUT
Note: 
%s: environment cannot be NULL\n
Carrier
us
DeviceCoverGlassMaterial
TRACE
k8BitData
Class 0
???
-[[:alnum:]]*
): 
Always
DCS:Czech
ARI_CLI_ERR - Tracking receipt of unrecognized transaction 0[xX][0-9a-fA-F]+
ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\([a-zA-Z\\.]+\\) [0-9a-zA-Z]+\\([0-9]+-[0-9a-fA-F]+\\) SZ\\(|\\) TRX\\(0x[0-9a-f]+\\) AP\\.SEQ\\(0x[0-9a-f]+\\).*
aborting because stripLongPrefix failed\n
Desense
!dDtor
Receive queue size %u exceeds max %u\n
CFDictionary(
Server Certificate Not Yet Valid
_TelephonyUtilTransportFileFlushRead
iPad
false
setSharedConfiguration
General data coding indication
kLogMessageTimestamp
DCS:Greek
DCS:Hebrew
%s: parameter cannot be NULL.\n
Failed to launch write worker, ret = %s(%u)\n
AtmPEO/j+Pdr8+WKxv4Aaw
Unable to load CrashReporterSupport framework.\n
DCS:Arabic
ReleaseType
isProcessRunning
first sysctl() failed with err = %d
Telephony operation timeout at '%s', timeout %u\n
Client Certificate Required
GZIP
kLogWriters
Fatal
failed to flush, err = %s (%u)\n
e
Failed set attributes, err = %s (%d)
DCS:Spanish
, but no client found: 
TIMEOUT for message MIPC.*?Client=.*?Msg=.*?Trx=.*? 
Cannot Connect To Host
Dynamic exception type: 
dyn_cast to uint64_t requires nonnegative values
[
setStreamProperty
setCompanionProxyPreference
SIMAP
_TelephonyUtilTransportFileWrite
Failed to close directory %s (error: %d(0x%x) (%s))
Failed to rename %s -> %s (error: %d(0x%x) (%s))
DCS:Swedish
DNS Lookup Failed
Server Certificate Has Unknown Root
ResultIsEmptyError: the result was never set with a success or error value
green-tea
Turkish
iPhone
Cannot Find Host
No diagnostic information available.
getHttpResponseCode
kLoggerDomain
/connections
kGranted
open_file
No Assertions
Message marked for automatic deletion
enabled
n
%F %T %Z
Baseband ARI engage timeout
\t\t\t[
SIMDEV
fHighestQueue
Debug
Set indication active
Got client checkin for client '
%s: argument cannot be NULL\n
pop
received string with length exceeding maximum int value
setProxyServer
DCS:Hungarian
modem boot up failure \\[|\\]
_TelephonyUtilUARTTransportWithTimeoutFreeInternal
SimulateCrash
Callback functor was never set; can't send response!
ARI_CLI_ERR - Tracking receipt of unrecognized transaction 
/dev/uart.debug
Message Waiting Indication group: Store message (UCS2)
com.apple.telephony.util
Resetting baseband .*?
Data Length Exceeds Maximum
Data Not Allowed
Got client error for conn 
EnableOversteer
stripLongPrefix
Restore
] 
Bad URL
CFData(
-%u
chmod
Compressed
\n
TelephonyUtilTransportCreateWithFD
BuildVersion
ProductVersion
ProductType
+
setRequestBody
kern.wakereason
(unknown)
getErrorRef
Failed to open transport to communicate with baseband.*
AP forced coredump via SPMI - Please analyze reason from AP perspective
IsVirtualDevice
POST
ctu:log
setConnectionCacheCellPurgeTimeout
kUCS2
received zero-length string parameter\n
_
Server Certificate Has Bad Date
Cannot Move File
0x
TIMEOUT for message MIPC \\[|\\]
timerScaling.firstbootafterupdate
debug
HTTP Too Many Redirects
ResultIsNotError: cannot return an error unless it was an error
o
::writers
'
null
XPC_ERROR(
setTLSPolicyName
kLoggerName
1
unknown boost::container exception
/usr/lib/libMobileGestalt.dylib
<Allocator %p: %s>
r
Voicemail message waiting
/private/var/wireless/Library/Preferences/com.apple.AppleBasebandManager.plist
Mac
NonUI
User Cancelled Authentication
Cannot Decode Raw Data
s
TIMEOUT for message MIPC .*?
DCS:INVALID LANGUAGE
watchers
CFArray(
Cannot Close File
International Roaming Off
bUJD9zcOcitJwFA0ieIkxA
 (0x
TelephonyUtilRunCommandExt
second sysctl() failed with err = %d
get_filtered_files
DELETE
Reserved, no message class meaning
Failed to get termios options, ret = %s (%u)\n
Client Certificate Rejected
HWModelStr
getResponseCFData
notify
DCS:Portuguese
RestModule::connect cannot be called with a null connector
Not Supported\n
Failed to unlink file %s (error: %d(0x%x) (%s))
Got request for new logger, but check in failed
Request DENIED for new logger '
Failed to change mode of destination file %s (error: %d(0x%x) (%s))
remove_file
aborting to prevent out-of-bounds access while copying numeric characters\n
Returning trivial time since clock service is unavailable\n
%llu:%s
Trace
Server Certificate Untrusted
0
h
x
Watch
{duration<long long, std::ratio<1, 1000000>>=q}8@?0
.
push
DCS:Finnish
Creating with baud %u, Rx Queue size %u, local queue size %u\n
Background Session In Use By Another Process
ResultIsError: cannot return a result because the operation was an error
start
B24@?0Q8^v16
GET
Never
^\\[abmtool\\] 
Failed to launch read worker, ret = %s(%u)\n
Download Decoding Failed Mid Stream
b
_create_directory
setValidateCertsCallback
DCS:Dutch
BBUpdater error  [0-9]+
TelephonyUtilTransportCreateWithFile
MockTimerService
kLogMessageLevel
^\\[bbutil\\].*
_TelephonyUtilUARTTransportWrite
ms
Failed to write to file descriptor %d (error: %d(0x%x) (%s))
setBackgroundConfiguration
AP
%lld:%s
logmaster::
setMaxAllowedRedirects
setSourceIdentifier
baseband
malloc failed for proc list
NO
{time_point<std::chrono::system_clock, std::chrono::duration<long long, std::ratio<1, 1000000>>>={duration<long long, std::ratio<1, 1000000>>=q}}8@?0
TelephonyBasebandWatchdogStartWithStackshot_block_invoke
8bit data encoding
\t\tNumeric Arguments:\n
detected hardware model info string without alphabetical prefix\n
Unknown Error
?
DCS:Russian
%04x  %s
_TelephonyUtilTransportFDWrite
failed to open node (%s), ret = %s(%u)\n
rest.xpc
RegionInfo
Failed to get time from clock service (error = %d); returning trivial time\n
{dict={object=^v}}8@?0
Unsupported URL
registerCallbackQueue
)
PCI-EVENT: pci error: 
kern.boottime
Out of memory!\n
_TelephonyUtilUARTTransportWithTimeoutFree
FALSE
Apple Watch
kCTDataConnectionServiceTypeInternet
Error
0123456789abcdef
_TelephonyUtilTransportFDRead
Request Body Stream Exhausted
DCS:Danish
' in domain '
received string parameter without non-numeric prefix\n
Invalid URL
Failed to close file descriptor %d (error: %d(0x%x)) (%s)
$2
setSourceApplicationBundleIdentifier
SIM
RegionCode
CONTENT-ENCODING
DCS:Icelandic
Class 1
Invalid current byte position
get_partition_info
^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8
setAllowCellularAccess
Electronic mail message waiting
(msg\\(|\\), for client)
Redirect To Non Existent Location
Bad Server Response
RestoreOSBuild
CONNECT
\": 
kLoggers
_TelephonyUtilUARTTransportConfigureFlowControl
createOneShotTimerImpl
setProxySettings
^\\[abmtool\\].*
^([/_\\-[:alnum:]]*)(.*)
DispatchTimerService
Attempted to send message on a disconnected connector.
Uncompressed
ResetReasonEncoder
com.apple.telephony
{vector<std::string, std::allocator<std::string>>=^v^v{?=^v}}8@?0
BootSessionUUID
MGCopyAnswer
WriteStackshotReport
EmptyMockCallArgsException for method '
DCS:Unspecified
revoked
\\s+
aborting to prevent out-of-bounds access while copying 1-character alphabetical prefix\n
read returned %s (%u)\n
TelephonyUtilTransportCreateWithUARTTimeout
 bytes)
DeviceName
DCS:Italian
DeviceIsNED
setServiceType
^\\[bbutil\\] 
DEV
Failed to write\n
Zero Byte Resource
DCS:Norweigian
kKSC5601 encoding
MaxPacketSize
getTLSNegotiatedCipherSuite
Other message waiting
Gsm7 encoding
v8@?0
_TelephonyUtilUARTTransportConfigureVMIN
: 
Callback queue was never set; can't send response!
Data coding/message class
basic_string
v
DCS:French
strtoul failed with error no %d\n
%s
 keys)
Q8@?0
a
Background Session Was Disconnected
FPGA
VendorNonUI
FirstBootAfterUpdate
Cannot Create File
d
Resetting baseband 
1.2.12
-
Reserved, used for KTF, KSC5601 encoding
Cannot Load From Network
<expired>
grant
 elements)
Timed Out
No Permissions To Read File
 bytes]
Hindi
 
/
write_to_completion
Cannot set up a period of 0 time; that would be insane!
ModelNumber
NVRAMDictionary
C8@?0
Assertions remaining: 
aborting to prevent out-of-bounds access while copying suffix (non-numeric) characters\n
MGCopyMultipleAnswers
<nil>
_TelephonyUtilUARTTransportConfigureBaudRate
timer
File Is Directory
Secure Connection Failed
Spanish
Timeout
load
Failed to get status of source file %s (error: %d(0x%x) (%s))
true
getRawErrorCode
set
g
Failed to close file %s (error: %d(0x%x) (%s))
B24@?0r*8^v16
DCS:Polish
Class 3
Server error: 
%s: spawning %s failed! ret: %d\n
Failed to open file %s, args %s, err = %s (%u)\n
YES
Failed to open file %s (error: %d(0x%x) (%s))
Failed to get filesystem statistics pertaining to path %s (error: %d(0x%x) (%s))
kLoggerLevel
Fax message waiting
disabled
/private/var/wireless/Library/Preferences/com.apple.commcenter.plist
state
copy_file
Failed to make directory %s with mode 0x%x (error: %d(0x%x) (%s))
getResponseString
Flushing\n
Failed to close, err = %s(%u)\n
App Transport Security Requires Secure Connection
Call Is Active
Client disconnected (
(ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\(([a-zA-Z]+\\.){0,}|\\) [0-9a-zA-Z]+\\([0-9]+-[0-9a-fA-F]+\\) SZ\\([0-9]+\\) TRX\\(0x[0-9a-f]+\\) AP\\.SEQ\\(0x[0-9a-f]+\\).*)
/usr/lib/libRemoteTelephonyTransport.dylib
ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\([a-zA-Z\\.]+\\) [0-9a-zA-Z]+\\([0-9]+-[0-9a-fA-F]+\\) SZ\\([0-9]+\\) TRX\\(0x[0-9a-f]+\\) AP\\.SEQ\\(0x[0-9a-f]+\\).*
generation
Failed to set termios options, ret = %s (%u)\n
Cannot Remove File
Failed to remove file %s (error: %d(0x%x) (%s))
Throw in function 
Attempted to dispatch on a connector with no queue!
DCS:German
PrevOSVersion
process %s exists? %{bool}d
Cannot Parse Response
Failed to get clock service (error = %d)\n
kLogMessage
modem boot up failure \\[.+\\]
watched
 crashed
Unknown exception.
setBackgroundConfigurationWithUniqueIdentifier
kern.bootsessionuuid
Download Decoding Failed To Complete
kDomainLogLevels
\t\tFree Text:\t
kIdle
context->source
Cannot Write To File
Failed to map file %s (error: %d(0x%x) (%s))
(null)
Info
revoke
Baseband got stuck in data context .* state: resetting baseband
configure
Not Connected To Internet
setRedirection
Portuguese
ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\([a-zA-Z\\.]+\\) [0-9a-zA-Z]+\\([0-9]+-[0-9a-fA-F]+\\) SZ\\([0-9]+\\) TRX\\(|\\) AP\\.SEQ\\(0x[0-9a-f]+\\).*
REST API Misuse: %s
File Does Not Exist
DCS:Turkish
Cannot Open File
Failed to read source file %s (error: %d(0x%x) (%s))
rename_directory_unique
 log messages dropped prior to log start
kLogMessageMetadata
Failed to configure baud of %u, err = %s (%u)\n
.highest
Invalid Request
EOSHalleyConfiguration
Failed to do stack shot/simulate crash, reason '%s', asCrash %u\n
TelephonyUtilRingBufferInitialize
Background Session Requires Shared Container
Failed to unmap file %s (error: %d(0x%x) (%s))
provider
Unset
setOnDemand
Class unspecified
v24@?0{connection={object=^v}}8{dict={object=^v}}16
write returned %s (%u)\n
TRUE
{unique_ptr<ctu::Timer, std::default_delete<ctu::Timer>>={?=^{Timer}}}8@?0
com.apple.commcenter
getPrivateRelayEnabled
Have a message class meaning
waiting
%s: command cannot be NULL\n
com.apple.libtu.timerscaling.firstbootafterupdate
_TelephonyUtilTransportFileUnblockRead
{time_point<std::chrono::steady_clock, std::chrono::duration<long long, std::ratio<1, 1000000000>>>={duration<long long, std::ratio<1, 1000000000>>=q}}8@?0
getResponseHeaders
Failed set speed, err = %s (%d)\n
None
Class 2
for client\\(
ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\([a-zA-Z\\.]+\\) [0-9a-zA-Z]+\\([0-9]+-[0-9a-fA-F]+\\) SZ\\([0-9]+\\) TRX\\(0x[0-9a-f]+\\) AP\\.SEQ\\(|\\).*
v16@?0^v8
Failed to create pipe FD's, err = %s (%u)\n
.work
v16@?0^{dirent=QQSSC[1024c]}8
terminate
Notice
FPGADEV
kPending
createPeriodicTimerImpl
p
setServerPinnedCerts
setWaitForConnectivityTimeout
ARI_CLI_ERR - All transaction IDs exhausted for msg\\(.*\\), for client\\(0[xX][0-9a-fA-F]+\\)
_TelephonyUtilUARTTransportConfigureRxQueueSize
UniqueDeviceID
Message waiting indication group: Store message (GSM-7)
TelephonyUtilParseHardwareModel
Failed to configure RX Queue size of %u, err = %s (%u)\n
close_file
$1-
HEAD
_TelephonyUtilUARTTransportWithTimeoutFlushRead
TelephonyUtilLoadCrashSupport_block_invoke
vector
*
EnableBBSimulation
setTimeout
Failed get attributes, err = %s (%d)\n
Set indication inactive
ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\([a-zA-Z\\.]+\\) [0-9a-zA-Z]+\\(|-[0-9a-fA-F]+\\).*
Failed to change mode of file %s to (0x%x) (error: %d(0x%x) (%s))
{endpoint={object=^v}}8@?0
Cannot Decode Content Data
,
Failed to open directory %s (error: %d(0x%x) (%s))
getResult
_TelephonyUtilTransportFileRead
Found no matching content in %s
std::exception::what: 
HasBaseband
getResponseStatusLine
ping
)\n
0123456789ABCDEF
Vendor
User Authentication Required
registerCompletionCodeblock
CurrentOSVersion
rename
kKSC5601
Failed Lookup
    
unload
received string parameter with no suffix (non-numeric) characters\n
write to completion returned %s (%u)\n
Failed to configure VMIN of %u, err = %s (%u)\n
OPTIONS
get
granted
UCS2 encoding
Freeing\n
Warn
GNSS [0-9]+
\t\tError Code:\t
Capacity %u is not a power of two\n
failed to read, err = %s (%u)\n
TelephonyUtilWriteStackshotWithExcCode
Header does not exist
```
