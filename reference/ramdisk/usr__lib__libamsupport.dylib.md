# `/usr/lib/libamsupport.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 349,488 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 27 (Size: 3680)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (10)

- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libReverseProxyDevice.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration (compatibility version 1.0.0, current version 1453.40.1)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/Frameworks/CFNetwork.framework/CFNetwork (compatibility version 1.0.0, current version 3896.200.61)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (2 classes, 4 protocols)

Classes: `AMSupportOSURLConnectionDelegate`, `AMSupportOSURLSession`

Protocols: `NSObject`, `NSURLConnectionDataDelegate`, `NSURLConnectionDelegate`, `NSURLSessionDelegate`

## Strings (630)

```
Session %@ became invalid: %@
PKI: decoding trusted root %d failed with error 0x%08X
AMSupportCFDictionarySetInteger32
failed to convert value to c-string
%s: failed to create digest
AMSupportCreatePropertyListFromFileURL
 after 5 seconds
MaxAttempts
kAMSupportHttpOptionValidResponses is not a CFSet
com.apple.libamsupport.amsupporturlsession
Failed to convert argument to uint32
AMSupportCopyDataFromAsciiEncodedHex
dladdr failed to get info about running framework
GET
[
_AMSupportHttpMessageSendSyncRetry
No default type, nor one specified in argument
outDataBuffer is NULL
Conversion failed; created 0 bytes of data.
%s: failed to convert 32-bit value
_create_peer_executable_for_ancestors
invalid requestDictKeysBuffer array
%2A
%3B
no
Failed to parse URL.
%s: failed to finalize digest
%2B
%5D
HTTP request failed (status=%d)
Number of trusted roots: %d
Root cert not signed by any trusted roots.
%s: failed to init digest
%s: failed to read from file %d
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
Authentication challenge received.  Method: %@
Received response from URL: %@
AMSupportRsaCreatePemFromData
data
%s: failed to open file %@
%25
]
failed to create %s: %s
-[AMSupportOSURLConnectionDelegate connectionDidFinishLoading:]
encodedLength == 0
postData allocation failed
%20
TrustServerCAsNonexclusively
trustedRootArray must be non NULL and have at least one element
headerLength == 0
dict is NULL
AMSupportCopyBytesFromAsciiEncodedHex
AMSupportCreateCStringFromCFString
encodedBuffer == NULL: '%@'
%s: failed to allocate digest
$
%3C
encodedSize is 0
dataPtr is NULL
value length == 0: '%@'
%s: digestInfo is NULL
%s: callback is NULL
httpStatus is %ld
AMSupportHttpCopyProxySettings: RPNotificationProxyUnavailable
%2F
PKI: cert signature validation with issuer pubkey failed amstatus=%d
PKI: verify cert was issued and signed by issuer (success)
keyPath is NULL
Found executable at %@
_AMSupportCreateDataFromFileURLInternal
wb
Failed to create session
failed to format log message
Received client certificate challenge.
asciiBuffer is NULL
AMSupportCopyHexStringFromData
AMSupportCreateRandomNumber
requestDictValuesBuffer allocation failed
%3D
|
HTTP request failed, httpResponseHeader is NULL
footerLength == 0
AMSupportHttpCopyProxySettings: RPNotificationProxyAvailable
-[AMSupportOSURLSession URLSession:didBecomeInvalidWithError:]
Multiple challenge failures. Request failed.
AMSupportX509ChainEvaluateTrust
outHexString is NULL
~%d
keys is NULL
AMSupportCreateDataFromFileURL failed.
%@/%@
%21
/
%7C
AMSupportPlatformOpenFileStreamWithURL
Successfully imported PKCS12 identity
AMSupportRsaCreateDataFromPem
AMSupportErrorDomain
AMSupportMakeDirectory failed.
Content-Type
(
HTTP request provided no response data
AMSupportPlatformCopyLocalIPAddressString
Failed to parse hex encoded data.
encodedValue == NULL: '%@'
%s: failed to allocate params
)
%s%c%s
invalid overridesKey
No proxy available%s
*
@
%5C
Could not stat (%s)
gethostbyname() failed: %s
trust evaluation failed (OSStatus=%d)
encodedLength == 0: '%@'
\\
Session is NULL
AMSupportCommonCopyHexStringFromData
bool
;
^
v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24
Could not mkdir (%s)
Number of server certificates: %d
0123456789ABCDEF
0
outDecodedValue == NULL
%28
Timeout
kAMSupportHttpOptionValidResponses is not an NSSet
HTTP request failed with error %@
%@
source path: %s; dest path: %s
outDataLength == NULL
pemString == NULL
-[AMSupportOSURLConnectionDelegate connection:didFailWithError:]
%s/%s
_SecCertificateCopyAMSupportCert
outHexStringLength is NULL
Too many delimiters in argument
Unrecognized Boolean value. (yes/no, true/false, 1/0)
AMSupportCopyHexStringFromUInt64
%s: invalid string
command failed with error: %@
%7D
Could not construct NSURLRequest from message %@
base64Buffer == NULL
outDataBufferLength is NULL
CFDataGetTypeID() != CFGetTypeID(data)
%s: theString is NULL
AMSupportPlatformRemoveFile
failed to create property list: %@
escapedValue == NULL
%26
httpRequest is NULL
can't prepare data for output to file
mac/%s/%s
AMSupport.m
true
false
hexString is NULL
inString is NULL
failed to create key substring
AMSupportHttpCreateDataFromURL
?
NULL parameter passed to _create_peer_executable_for_ancestors()
 
SSL trust evaluation failed
HTTP request failed, httpResponseData is NULL
HTTP/1.1
_tempDirURL != NULL
AMSupportBase64Encode
decodedData is NULL
_AMSupportHttpMessageSendSyncNoRetry
-[AMSupportOSURLConnectionDelegate connection:didReceiveResponse:]
escapedValue is NULL
%40
certRef must be non-null
-[AMSupportOSURLConnectionDelegate connection:willSendRequestForAuthenticationChallenge:]
outString is NULL
AMSupportReadChunks
Missing symbols.
AMSupportHttpCopyProxySettings_block_invoke
AMSupportHttpCopyProxySettings: RPNotificationAborted
Backoff
%@%s
AMSupportHttpUriUnescapeString
%24
%7E
failed to create link: %s
trustedRootArray must be non-null
result must be non-null
Array index of root server cert out of range. (%d)
PKI: Root cert is identical to trusted root. (success)
AMSupportX509DecodeParseDERLengthFromBuffer
AMSupportCopySetValueForKeyPathInDict
-
%2D
<
chain_blob must be non NULL and chain_blob_length must be non 0
Too few delimiters in argument
calloc failed
%s: callback failed
Searched for %@ relative to %@ and its ancestors, found %@
Proxy available
%22
ClientCredential
%s: 
data == NULL
buffer is NULL
failed to create current substring
POST
%lu
!
\"
%3F
yes
malloc() returned NULL
text/xml; charset=\"utf-8\"
Content-Length
httpResponseData is NULL
}
debug object written: %@
PKI: Chain validation complete. (success)
AMSupportCopyPreserveFileURL failed.
(No copy of executable located at %@)
AMSupportHttpUriEscapeString
AMSupportHttpCreatePostBody
failed to file: %s
kern.osversion
???
NSAllowsArbitraryLoads
Trust evaluation succeeded, proceeding..
AMSupportHttpSetUriEscapedValue
%23
mac
Trusted root #%d has length %d
dataLength == 0
outPemLength == NULL
failed to register for reverse proxy availability
PKI: verify cert was issued by trusted root %d (success)
Attempting trust evaluate
num != NULL
AMSupportGetValueForKeyPathInDict
%s: flags is NULL
v12@?0i8
>
data is NULL
rb
hw.product
PKI: verify cert was issued by trusted root %d failed with error 0x%08X
Connection error %@ for URL
pemBufferLength == 0
AMSupportCFDictionaryGetBoolean
failed to allocate buffer
item %@ not a dictionary
unescapedValue == NULL
{
_AMSupportHttpURLSessionSendSyncNoRetry
failed to decode DER
://
,
`
Failed to create semaphore
-----------------------------------------------
ATS: disabled per request on allowed build type.
com.apple.libamsupport.http-traffic
length is 0
%s: CFURLRef passed, retaining copy
AMSupportBase64Decode
invalid overridesValue
proxyInfo = %@
~
init-ing delegate with data=%@ options=%@
Multiple challenge failures.  Aborting.
-[AMSupportOSURLConnectionDelegate connection:didReceiveData:]
AMSupportWriteDataToFileURL
%s: srcURL is NULL
+
AMSupportPlatform.c
Unable to import client identity, aborting challenge.
numUnused != 0
Receiving %d bytes of data from URL
AMSupportWriteDictionarytoFileURLWithFormat
AMSupportHttpCreatePostRequest
ClientIdentityPassphrase
_AMSupportPlatformTempDirURLInitialize
PKI: decoding top-level server cert failed with error 0x%08X
AMSupportX509DecodeVerifyCertIssuer
value == NULL
AMSupportCopyFile
%s: failed to read file in chunks
tmpStringBuffer allocation failure
TestReachability
%2C
%s\n
encodedLocation != encodedLength
value is NULL
failed to create data: %@
%02x 
addr2ascii() failed: %s
hw.machine
-[AMSupportOSURLSession URLSession:didReceiveChallenge:completionHandler:]
serverTrust must be non-null
footer == NULL
AMSupportApplyDictionaryOverrides
%29
SocksProxySettings
RequestHTTPAllowed
First server cert length %d
bufferToCovert is NULL
AMSupportGetUInt32
HTTP server returned unexpected HTTP response code %ld
CFMutableRequestRef could not be retrieved to set proxy settings
url=%@, path=%s
bufferToConvertLength is 0
trusted certificate could not be loaded %@
Finished loading URL.  Total bytes: %d
outEscapedValue == NULL
Base64Encode failed
-------------------- Attempt %d of %d failed, sleeping for %d seconds --------------------
pemBuffer == NULL
string
Incoming CFNumberRef is of unexpected type %d
outEncodedValue == NULL
AMSupportHttpURLSessionSendSync
stringBuffer is NULL
AMSupportCreatePathForPeerExecutable
TrustedServerCAs
ValidResponses
AMSupportDebugWriteObject
AMSupportPlatformRemoveDirectory
TMPDIR
AMSupportError
AMSupportCopySetValueAtTypedKeypath
%s: failed to convert 64-bit value
AMSupportCreateDigest
requestDictKeysBuffer allocation failed
&
_
HTTP request failed, httpResponse is NULL
AMSupportCFDictionarySetInteger64
_NSGetExecutablePath failed to get path of current executable
outUnescapedValue == NULL
AMSupportHttpCreatePostBody failed
AMSupportHttpCopyProxySettings
#
request is nil
failed to remove directory: %s
outData == NULL
:
url
stringLength is 0
AMSupportCreateSetFromCFIndexArray input contains invalid number.
_base64decode of value '%@' failed with error code %d.
%2E
%3E
-[AMSupportOSURLConnectionDelegate dealloc]
outPemData == NULL
AMSupportCreateSetFromCFIndexArray
%s: failed to copy digest
invalid requestDictValuesBuffer array
%5F
UsePurpleReverseProxy
AMSupportPlatformCreateSoftLink
decodeAlgId failed
sint32
tmpResult (Number) is NULL
=
%27
AMSupportPlatformCopyURLToNewTempDirectory
failed to convert url to file system representation
-[AMSupportOSURLSession _defaultSessionConfigurationWithIdentifier:]
DERParseBitString(sig) failed
pemLocation != pemLength
Unrecognized data type.
AMSupportCommonCopyHexStringFromData failed %d
Priority
.plist
Checking server certificate %d of %d
PKI: decoding cert failed with error 0x%08X
header == NULL
AMSupportCommonCopyHexStringFromUInt32 failed (%d)
AMSupportCommonCopyHexStringFromUInt64 failed (%d)
AMSupportWriteDataToFileURL failed.
%s: failed to allocate chunk buffer
conversion of postString to c-string failed
AMSupportHttpSetBase64EncodedValue
%5E
dict value is not CFBoolean
1
CFDictionaryCreateMutable failed.
'
%5B
ClientIdentity
-[AMSupportOSURLSession sendRequest:completion:]_block_invoke
v8@?0
SSL validation disabled.  Attempting to continue without authentication.
encoded size will overrun DERSize
-[AMSupportOSURLConnectionDelegate initWithData:Options:]
key is NULL
bufferLength is 0
%
failed to create debugData: %@
SecCertificateCopyData returned NULL CFDataRef
P12 Identity data length=%d
libamsupport-???
AMSupportHttpUriEscapeString failed
encodedValue is NULL
DisableSSLValidation
[%s: %u bytes]
%s
com.apple.libamsupport.http-session
trust evaluation did not result in okay to proceed (result=%d)
AMSupportCopyHexStringFromUInt32
.
postString=%@
%3A
%60
%7B
URL connection error occurred: %@
PKI: cert was not issued by issuer (subject != issuer)
encodedBuffer == NULL
dict is not CFDictionary
outStringLength is NULL
AMSupportCreateSetFromCFIndexArray CFSetCreateMutable failed.
!!!!!!!!!!!!!!!!!!!!!!!!!! Retries exhausted on attempt %d !!!!!!!!!!!!!!!!!!!!!!!!!!
AMSupportPlatformMakeDirectoryForURL
ATS: OS is internal.
dealloc-ing delegate
Returned credentials for challenge.
asciiBufferLength is 0
AMSupportCreateURLFromString
gethostname() failed: %s
AMSupportOSURLSession
NSURLSessionDelegate
AMSupportOSURLConnectionDelegate
NSURLConnectionDelegate
NSObject
NSURLConnectionDataDelegate
numberWithLong:
URLSession:didBecomeInvalidWithError:
errorWithDomain:code:userInfo:
Tf,N,V_priority
_options
connection:canAuthenticateAgainstProtectionSpace:
respondsToSelector:
timeout
connection:willSendRequestForAuthenticationChallenge:
init
priority
serverTrust
T@\"NSError\",R,N,V_error
isProxy
connection:didFailWithError:
connection:needNewBodyStream:
description
setAllHTTPHeaderFields:
member:
dataWithPropertyList:format:options:error:
invalidateAndCancel
allHeaderFields
connection:willSendRequest:redirectResponse:
setQueue:
protectionSpace
TB,R,V_sslEvalFailed
arrayWithObject:
connection:willCacheResponse:
debugDescription
requestComplete
arrayWithCapacity:
connection:didReceiveAuthenticationChallenge:
currentRunLoop
floatValue
URLSession:didReceiveChallenge:completionHandler:
_newSession
dealloc
T@\"NSURLSession\",&,N,V_session
appendData:
isEqual:
sessionWithConfiguration:delegate:delegateQueue:
T#,R
connection:didReceiveResponse:
self
statusCode
sender
setSession:
_queue
previousFailureCount
resume
useCredential:forAuthenticationChallenge:
autorelease
T@\"NSString\",?,R,C
dataTaskWithRequest:completionHandler:
dictionaryWithObjects:forKeys:count:
ephemeralSessionConfiguration
error
requestWithURL:cachePolicy:timeoutInterval:
retainCount
setHTTPMethod:
T@\"NSData\",R,N,V_data
connection:didSendBodyData:totalBytesWritten:totalBytesExpectedToWrite:
isKindOfClass:
performDefaultHandlingForAuthenticationChallenge:
setAllowsCellularAccess:
setConnectionProxyDictionary:
release
credentialWithIdentity:certificates:persistence:
performSelector:withObject:
response
authenticationMethod
doubleValue
set_atsTrustPolicy:
waitForResponseOrError:
connectionShouldUseCredentialStorage:
initWithRequest:delegate:startImmediately:
queue
set_shouldSkipPreferredClientCertificateLookup:
options
_CFURLRequest
class
conformsToProtocol:
data
_sslEvalFailed
hash
initWithData:Options:
setOptions:
objectForKey:
setURL:
T@\"NSDictionary\",&,N,V_options
T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue
numberWithBool:
connectionDidFinishLoading:
isMemberOfClass:
Td,N,V_timeout
set_atsContext:
credentialForTrust:
_defaultSessionConfigurationWithIdentifier:
initWithOptions:
_priority
distantFuture
setPriority:
setTimeoutInterval:
cancelAuthenticationChallenge:
performSelector:withObject:withObject:
runMode:beforeDate:
setTimeout:
count
localizedStringForStatusCode:
sendRequest:completion:
setTimeoutIntervalForRequest:
sslEvalFailed
T@\"NSString\",R,C
setHTTPBody:
zone
_session
_urlRequestForHTTPMessage:
connection:didCancelAuthenticationChallenge:
connection:didReceiveData:
objectForKeyedSubscript:
retain
URLSessionDidFinishEventsForBackgroundURLSession:
_error
_timeout
addObject:
countByEnumeratingWithState:objects:count:
dataWithCapacity:
length
TQ,R
session
boolValue
_data
performSelector:
setLength:
superclass
v32@0:8@\"NSURLConnection\"16@\"NSError\"24
@\"NSInputStream\"32@0:8@\"NSURLConnection\"16@\"NSURLRequest\"24
@\"NSCachedURLResponse\"32@0:8@\"NSURLConnection\"16@\"NSCachedURLResponse\"24
B
@16@0:8
@32@0:8:16@24
B24@0:8:16
^{_NSZone=}16@0:8
B32@0:8@\"NSURLConnection\"16@\"NSURLProtectionSpace\"24
v48@0:8@\"NSURLConnection\"16q24q32q40
v32@0:8@\"NSURLSession\"16@\"NSError\"24
f16@0:8
B16@0:8
Q16@0:8
v24@0:8@16
v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32
@\"NSObject<OS_dispatch_queue>\"
d
#16@0:8
v32@0:8@\"NSURLConnection\"16@\"NSURLAuthenticationChallenge\"24
@40@0:8@16@24@32
@32@0:8@16@24
@24@0:8^{__CFHTTPMessage=}16
v24@0:8d16
B24@0:8#16
@\"NSString\"16@0:8
v32@0:8@\"NSURLConnection\"16@\"NSURLResponse\"24
@\"NSMutableData\"
v24@0:8@\"NSURLSession\"16
B32@0:8@16@24
v32@0:8@\"NSURLConnection\"16@\"NSData\"24
@\"NSError\"
f
@\"NSURLSession\"
Vv16@0:8
v16@0:8
@24@0:8^@16
@\"NSDictionary\"
v40@0:8@16@24@?32
@24@0:8@16
v32@0:8^{__CFHTTPMessage=}16@?24
v20@0:8f16
B24@0:8@16
B24@0:8@\"Protocol\"16
B24@0:8@\"NSURLConnection\"16
v48@0:8@16q24q32q40
@\"NSURLRequest\"40@0:8@\"NSURLConnection\"16@\"NSURLRequest\"24@\"NSURLResponse\"32
v24@0:8@\"NSURLConnection\"16
@\"NSURLResponse\"
d16@0:8
@24@0:8:16
@40@0:8:16@24@32
v32@0:8@16@24
```
