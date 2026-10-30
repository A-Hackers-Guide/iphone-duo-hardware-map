# `/usr/lib/libamsupport.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 349,488 bytes.

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
-[AMSupportOSURLConnectionDelegate initWithData:Options:]
Received response from URL: %@
no
AMSupportWriteDataToFileURL failed.
encoded size will overrun DERSize
AMSupportCFDictionaryGetBoolean
AMSupportCreateSetFromCFIndexArray input contains invalid number.
outEncodedValue == NULL
AMSupportMakeDirectory failed.
 
Failed to create session
CFMutableRequestRef could not be retrieved to set proxy settings
AMSupportCopyHexStringFromUInt64
Too few delimiters in argument
!!!!!!!!!!!!!!!!!!!!!!!!!! Retries exhausted on attempt %d !!!!!!!!!!!!!!!!!!!!!!!!!!
failed to create link: %s
AMSupportPlatform.c
PKI: verify cert was issued by trusted root %d (success)
init-ing delegate with data=%@ options=%@
Multiple challenge failures.  Aborting.
%s: srcURL is NULL
v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24
-[AMSupportOSURLSession _defaultSessionConfigurationWithIdentifier:]
Checking server certificate %d of %d
outDataBufferLength is NULL
Found executable at %@
%s: failed to copy digest
_
com.apple.libamsupport.amsupporturlsession
outString is NULL
%s: callback is NULL
!
failed to create debugData: %@
debug object written: %@
AMSupportPlatformCopyLocalIPAddressString
-[AMSupportOSURLSession URLSession:didBecomeInvalidWithError:]
Number of server certificates: %d
Too many delimiters in argument
AMSupportWriteDataToFileURL
AMSupportCreateRandomNumber
&
%3C
%40
}
%7D
AMSupportRsaCreatePemFromData
encodedLength == 0: '%@'
%s: failed to finalize digest
%s: failed to open file %@
%27
Timeout
ClientIdentityPassphrase
%s: 
No default type, nor one specified in argument
AMSupportHttpCreatePostBody failed
mac
-[AMSupportOSURLSession sendRequest:completion:]_block_invoke
v8@?0
Multiple challenge failures. Request failed.
certRef must be non-null
Incoming CFNumberRef is of unexpected type %d
Proxy available
)
Session is NULL
Could not mkdir (%s)
hw.product
Number of trusted roots: %d
malloc() returned NULL
%s: failed to allocate params
_create_peer_executable_for_ancestors
can't prepare data for output to file
outPemLength == NULL
inString is NULL
url=%@, path=%s
Finished loading URL.  Total bytes: %d
dataLength == 0
tmpResult (Number) is NULL
AMSupportCommonCopyHexStringFromUInt64 failed (%d)
 after 5 seconds
PKI: decoding cert failed with error 0x%08X
-[AMSupportOSURLConnectionDelegate connection:didReceiveResponse:]
AMSupport.m
item %@ not a dictionary
%s: theString is NULL
invalid requestDictValuesBuffer array
%23
\\
failed to convert url to file system representation
footerLength == 0
invalid requestDictKeysBuffer array
#
%2F
%7B
HTTP request failed (status=%d)
TMPDIR
_tempDirURL != NULL
%s: failed to allocate digest
%s: callback failed
%s: failed to read from file %d
Content-Type
AMSupportErrorDomain
value is NULL
Searched for %@ relative to %@ and its ancestors, found %@
Missing symbols.
%3B
%3F
mac/%s/%s
PKI: cert signature validation with issuer pubkey failed amstatus=%d
Successfully imported PKCS12 identity
base64Buffer == NULL
AMSupportCreateSetFromCFIndexArray CFSetCreateMutable failed.
AMSupportCreateDigest
TrustedServerCAs
ClientIdentity
trustedRootArray must be non-null
sint32
AMSupportCopyBytesFromAsciiEncodedHex
bufferLength is 0
AMSupportGetValueForKeyPathInDict
requestDictValuesBuffer allocation failed
command failed with error: %@
v12@?0i8
%
num != NULL
length is 0
escapedValue is NULL
%2C
URL connection error occurred: %@
AMSupportDebugWriteObject
trustedRootArray must be non NULL and have at least one element
Trusted root #%d has length %d
P12 Identity data length=%d
libamsupport-???
AMSupportHttpSetBase64EncodedValue
{
failed to format log message
Received client certificate challenge.
SSL validation disabled.  Attempting to continue without authentication.
%@/%@
outUnescapedValue == NULL
failed to register for reverse proxy availability
kAMSupportHttpOptionValidResponses is not a CFSet
AMSupportPlatformMakeDirectoryForURL
0123456789ABCDEF
AMSupportCreateDataFromFileURL failed.
%2E
AMSupportHttpURLSessionSendSync
HTTP request failed with error %@
PKI: Root cert is identical to trusted root. (success)
AMSupportBase64Encode
%s: flags is NULL
NULL parameter passed to _create_peer_executable_for_ancestors()
outEscapedValue == NULL
%20
addr2ascii() failed: %s
Trust evaluation succeeded, proceeding..
Receiving %d bytes of data from URL
key is NULL
CFDataGetTypeID() != CFGetTypeID(data)
AMSupportGetUInt32
encodedBuffer == NULL: '%@'
CFDictionaryCreateMutable failed.
[%s: %u bytes]
AMSupportCopySetValueAtTypedKeypath
AMSupportCommonCopyHexStringFromUInt32 failed (%d)
%s: failed to convert 64-bit value
~%d
%s: failed to create digest
unescapedValue == NULL
TestReachability
SocksProxySettings
-[AMSupportOSURLConnectionDelegate connection:didReceiveData:]
encodedLocation != encodedLength
postString=%@
MaxAttempts
HTTP request failed, httpResponseData is NULL
_AMSupportHttpMessageSendSyncNoRetry
%@
%s
AMSupportCopyHexStringFromData
buffer is NULL
value length == 0: '%@'
AMSupportBase64Decode
source path: %s; dest path: %s
PKI: decoding top-level server cert failed with error 0x%08X
PKI: Chain validation complete. (success)
AMSupportX509DecodeParseDERLengthFromBuffer
dataPtr is NULL
AMSupportCommonCopyHexStringFromData failed %d
outDecodedValue == NULL
AMSupportCopySetValueForKeyPathInDict
SSL trust evaluation failed
request is nil
-[AMSupportOSURLSession URLSession:didReceiveChallenge:completionHandler:]
trust evaluation failed (OSStatus=%d)
AMSupportCopyDataFromAsciiEncodedHex
failed to create current substring
%25
bufferToCovert is NULL
Unable to import client identity, aborting challenge.
pemString == NULL
Could not construct NSURLRequest from message %@
_SecCertificateCopyAMSupportCert
requestDictKeysBuffer allocation failed
AMSupportHttpCopyProxySettings_block_invoke
*
RequestHTTPAllowed
%@%s
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
AMSupportHttpCreatePostBody
pemBuffer == NULL
AMSupportCFDictionarySetInteger32
false
(No copy of executable located at %@)
AMSupportReadChunks
AMSupportHttpCopyProxySettings
,
PKI: verify cert was issued and signed by issuer (success)
trusted certificate could not be loaded %@
Failed to parse URL.
AMSupportCreateCStringFromCFString
AMSupportCreateSetFromCFIndexArray
calloc failed
postData allocation failed
No proxy available%s
AMSupportCreatePropertyListFromFileURL
wb
DERParseBitString(sig) failed
-[AMSupportOSURLConnectionDelegate connection:didFailWithError:]
_base64decode of value '%@' failed with error code %d.
invalid overridesKey
AMSupportHttpCreateDataFromURL
/
PKI: cert was not issued by issuer (subject != issuer)
Base64Encode failed
%3E
ClientCredential
-------------------- Attempt %d of %d failed, sleeping for %d seconds --------------------
failed to remove directory: %s
AMSupportError
url
\"
UsePurpleReverseProxy
%s/%s
result must be non-null
failed to decode DER
%2D
%60
Priority
gethostbyname() failed: %s
hexString is NULL
%s: CFURLRef passed, retaining copy
]
_AMSupportPlatformTempDirURLInitialize
Returned credentials for challenge.
encodedLength == 0
Unrecognized data type.
value == NULL
keyPath is NULL
failed to create data: %@
Content-Length
GET
numUnused != 0
1
invalid overridesValue
failed to create property list: %@
+
%2B
;
<
0
decodedData is NULL
AMSupportCopyPreserveFileURL failed.
%22
%2A
|
~
%7E
AMSupportCopyHexStringFromUInt32
%s: failed to convert 32-bit value
failed to convert value to c-string
%s: failed to read file in chunks
%24
%5D
^
DisableSSLValidation
pemBufferLength == 0
pemLocation != pemLength
'
@
TrustServerCAsNonexclusively
HTTP request failed, httpResponseHeader is NULL
HTTP request failed, httpResponse is NULL
Could not stat (%s)
AMSupportApplyDictionaryOverrides
%5C
httpRequest is NULL
-----------------------------------------------
AMSupportPlatformCreateSoftLink
failed to file: %s
gethostname() failed: %s
PKI: decoding trusted root %d failed with error 0x%08X
Connection error %@ for URL
Conversion failed; created 0 bytes of data.
failed to create key substring
_NSGetExecutablePath failed to get path of current executable
AMSupportHttpCopyProxySettings: RPNotificationProxyAvailable
proxyInfo = %@
_AMSupportHttpMessageSendSyncRetry
%02x 
encodedBuffer == NULL
true
stringLength is 0
%5E
ATS: OS is internal.
SecCertificateCopyData returned NULL CFDataRef
AMSupportCommonCopyHexStringFromData
bufferToConvertLength is 0
HTTP server returned unexpected HTTP response code %ld
ATS: disabled per request on allowed build type.
Root cert not signed by any trusted roots.
-[AMSupportOSURLConnectionDelegate connectionDidFinishLoading:]
bool
conversion of postString to c-string failed
AMSupportHttpSetUriEscapedValue
httpStatus is %ld
%5B
.plist
AMSupportPlatformOpenFileStreamWithURL
stringBuffer is NULL
AMSupportCopyFile
%s: digestInfo is NULL
=
HTTP request provided no response data
AMSupportX509ChainEvaluateTrust
outHexString is NULL
outHexStringLength is NULL
-[AMSupportOSURLConnectionDelegate connection:willSendRequestForAuthenticationChallenge:]
(
%5F
NSAllowsArbitraryLoads
outData == NULL
outDataLength == NULL
rb
PKI: verify cert was issued by trusted root %d failed with error 0x%08X
chain_blob must be non NULL and chain_blob_length must be non 0
dict is NULL
:
data is NULL
failed to allocate buffer
AMSupportHttpUriUnescapeString
_AMSupportHttpURLSessionSendSyncNoRetry
%lu
httpResponseData is NULL
%26
%3A
failed to create %s: %s
data
string
outStringLength is NULL
%s: invalid string
%s: failed to init digest
AMSupportWriteDictionarytoFileURLWithFormat
$
hw.machine
AMSupportX509DecodeVerifyCertIssuer
Attempting trust evaluate
Unrecognized Boolean value. (yes/no, true/false, 1/0)
outDataBuffer is NULL
AMSupportHttpCopyProxySettings: RPNotificationAborted
?
ValidResponses
???
headerLength == 0
outPemData == NULL
Failed to convert argument to uint32
yes
POST
AMSupportHttpCopyProxySettings: RPNotificationProxyUnavailable
serverTrust must be non-null
AMSupportCFDictionarySetInteger64
dict is not CFDictionary
asciiBuffer is NULL
AMSupportCreatePathForPeerExecutable
_AMSupportCreateDataFromFileURLInternal
>
kAMSupportHttpOptionValidResponses is not an NSSet
%s%c%s
trust evaluation did not result in okay to proceed (result=%d)
AMSupportRsaCreateDataFromPem
encodedValue == NULL: '%@'
dladdr failed to get info about running framework
tmpStringBuffer allocation failure
Backoff
Failed to create semaphore
AMSupportPlatformCopyURLToNewTempDirectory
footer == NULL
Failed to parse hex encoded data.
://
encodedValue is NULL
%29
-
%s\n
com.apple.libamsupport.http-traffic
-[AMSupportOSURLConnectionDelegate dealloc]
dealloc-ing delegate
data == NULL
%s: failed to allocate chunk buffer
escapedValue == NULL
`
kern.osversion
com.apple.libamsupport.http-session
dict value is not CFBoolean
.
[
%7C
AMSupportPlatformRemoveFile
Session %@ became invalid: %@
Array index of root server cert out of range. (%d)
First server cert length %d
header == NULL
AMSupportCreateURLFromString
%21
HTTP/1.1
text/xml; charset=\"utf-8\"
Authentication challenge received.  Method: %@
keys is NULL
AMSupportHttpUriEscapeString failed
AMSupportHttpCreatePostRequest
%28
%3D
AMSupportPlatformRemoveDirectory
AMSupportHttpUriEscapeString
asciiBufferLength is 0
decodeAlgId failed
encodedSize is 0
AMSupportOSURLConnectionDelegate
NSURLConnectionDelegate
NSObject
NSURLConnectionDataDelegate
AMSupportOSURLSession
NSURLSessionDelegate
T#,R
T@\"NSDictionary\",&,N,V_options
dictionaryWithObjects:forKeys:count:
setSession:
setTimeoutIntervalForRequest:
sslEvalFailed
TB,R,V_sslEvalFailed
arrayWithObject:
connection:needNewBodyStream:
count
dataWithPropertyList:format:options:error:
initWithRequest:delegate:startImmediately:
setTimeoutInterval:
set_atsTrustPolicy:
_data
_options
authenticationMethod
errorWithDomain:code:userInfo:
setAllowsCellularAccess:
protectionSpace
connection:didReceiveResponse:
connection:willCacheResponse:
debugDescription
superclass
_session
priority
setConnectionProxyDictionary:
useCredential:forAuthenticationChallenge:
countByEnumeratingWithState:objects:count:
initWithOptions:
localizedStringForStatusCode:
setQueue:
_queue
_timeout
connection:didReceiveData:
connection:willSendRequest:redirectResponse:
objectForKeyedSubscript:
setPriority:
T@\"NSString\",?,R,C
connectionShouldUseCredentialStorage:
queue
waitForResponseOrError:
error
initWithData:Options:
T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue
Td,N,V_timeout
dataTaskWithRequest:completionHandler:
hash
doubleValue
isEqual:
self
URLSession:didReceiveChallenge:completionHandler:
currentRunLoop
retainCount
sessionWithConfiguration:delegate:delegateQueue:
numberWithLong:
set_atsContext:
_sslEvalFailed
cancelAuthenticationChallenge:
connection:didReceiveAuthenticationChallenge:
connection:didSendBodyData:totalBytesWritten:totalBytesExpectedToWrite:
URLSession:didBecomeInvalidWithError:
release
appendData:
length
dealloc
boolValue
connection:didFailWithError:
connection:willSendRequestForAuthenticationChallenge:
options
isProxy
_CFURLRequest
dataWithCapacity:
performSelector:withObject:
respondsToSelector:
resume
serverTrust
conformsToProtocol:
credentialForTrust:
setLength:
set_shouldSkipPreferredClientCertificateLookup:
zone
connectionDidFinishLoading:
setHTTPBody:
Tf,N,V_priority
requestComplete
_urlRequestForHTTPMessage:
connection:didCancelAuthenticationChallenge:
distantFuture
invalidateAndCancel
setAllHTTPHeaderFields:
addObject:
performSelector:
previousFailureCount
_error
retain
statusCode
T@\"NSData\",R,N,V_data
member:
_newSession
numberWithBool:
T@\"NSError\",R,N,V_error
TQ,R
autorelease
connection:canAuthenticateAgainstProtectionSpace:
performSelector:withObject:withObject:
URLSessionDidFinishEventsForBackgroundURLSession:
_priority
description
init
objectForKey:
setURL:
credentialWithIdentity:certificates:persistence:
floatValue
runMode:beforeDate:
setHTTPMethod:
T@\"NSURLSession\",&,N,V_session
data
isKindOfClass:
performDefaultHandlingForAuthenticationChallenge:
sender
T@\"NSString\",R,C
_defaultSessionConfigurationWithIdentifier:
requestWithURL:cachePolicy:timeoutInterval:
timeout
allHeaderFields
arrayWithCapacity:
session
class
ephemeralSessionConfiguration
isMemberOfClass:
response
setOptions:
sendRequest:completion:
setTimeout:
@24@0:8^@16
@\"NSError\"
v40@0:8@16@24@?32
f16@0:8
Vv16@0:8
B
@\"NSMutableData\"
f
@\"NSURLSession\"
B24@0:8@16
B24@0:8:16
^{_NSZone=}16@0:8
v32@0:8@16@24
B32@0:8@16@24
@\"NSCachedURLResponse\"32@0:8@\"NSURLConnection\"16@\"NSCachedURLResponse\"24
@\"NSURLResponse\"
v20@0:8f16
@32@0:8:16@24
B24@0:8#16
B32@0:8@\"NSURLConnection\"16@\"NSURLProtectionSpace\"24
v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32
@24@0:8:16
@40@0:8:16@24@32
v32@0:8@\"NSURLConnection\"16@\"NSURLAuthenticationChallenge\"24
@40@0:8@16@24@32
@32@0:8@16@24
v32@0:8^{__CFHTTPMessage=}16@?24
v24@0:8d16
#16@0:8
@\"NSString\"16@0:8
v48@0:8@16q24q32q40
v32@0:8@\"NSURLSession\"16@\"NSError\"24
@\"NSObject<OS_dispatch_queue>\"
@16@0:8
B24@0:8@\"Protocol\"16
B24@0:8@\"NSURLConnection\"16
v48@0:8@\"NSURLConnection\"16q24q32q40
v24@0:8@\"NSURLConnection\"16
v16@0:8
@\"NSDictionary\"
v24@0:8@\"NSURLSession\"16
B16@0:8
Q16@0:8
v32@0:8@\"NSURLConnection\"16@\"NSError\"24
@\"NSInputStream\"32@0:8@\"NSURLConnection\"16@\"NSURLRequest\"24
@24@0:8@16
@24@0:8^{__CFHTTPMessage=}16
d16@0:8
d
v24@0:8@16
@\"NSURLRequest\"40@0:8@\"NSURLConnection\"16@\"NSURLRequest\"24@\"NSURLResponse\"32
v32@0:8@\"NSURLConnection\"16@\"NSURLResponse\"24
v32@0:8@\"NSURLConnection\"16@\"NSData\"24
```
