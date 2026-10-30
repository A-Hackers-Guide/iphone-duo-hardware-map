# `/System/Library/PrivateFrameworks/MFAAuthentication.framework/XPCServices/MFAANetwork.xpc/MFAANetwork`

From the upgrade restore ramdisk (141-29011-104.dmg). 2,217,616 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 3912)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (6)

- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>FairPlay-Classic-Client</key>
	<true/>
	<key>fairplay-client</key>
	<string>441247889</string>
</dict>
</plist>
```

## Objective-C (7 classes, 4 protocols)

Classes: `FairPlaySAPSession`, `MFAANetwork`, `MFAANetworkExported`, `NSError`, `NSLocale`, `NSXPCConnection`, `ServiceDelegate`

Protocols: `FairPlaySAPSessionDelegate`, `MFAANetworkProtocol`, `NSObject`, `NSXPCListenerDelegate`

## Strings (647)

```
ServiceDelegate
NSObject
MFAAError
Additions
FairPlaySAPSession
FairPlaySAPSessionError
MFAANetworkProtocol
NSXPCListenerDelegate
Entitlements
MFAANetwork
FairPlaySAPSessionDelegate
MFAANetworkExported
T@\"NSObject<OS_dispatch_queue>\",&,N,V_internalQueue
TB,N,V_forceTokenConfirmationFailure
pairingTableVersion
verifyPairingWithToken:withReply:
T@\"NSURLSession\",&,N,V_urlSession
TB,N,V_forceNetworkFailure
raise:format:
self
setInternalQueue:
stringWithString:
TB,N,V_forceFairPlaySAPFailure
_init
description
mutableCopy
pairingTable
signatureForData:completionHandler:
stringForKey:
validateCertSerial:issuerSeq:ppid:withReply:
JSONObjectWithData:options:error:
isInternalBuild
initWithDelegate:
containsObject:
UUIDString
_fairPlaySignatureForDataSync:timedOut:error:
count
dictionaryWithDictionary:
performSelector:
verifySignature:forData:completionHandler:
allHTTPHeaderFields
instancesRespondToSelector:
objectForKey:
T@\"<FairPlaySAPSessionDelegate>\",W,N,V_delegate
_delegateQueue
date
isProxy
_forceTokenConfirmationFailure
delegate
setForceTokenConfirmationFailure:
T@\"NSObject<OS_dispatch_queue>\",&,N,V_delegateQueue
T^{FPSAPContextOpaque_=},N,V_sessionContext
forceNetworkFailure
TB,N,V_spoofPPIDMetadata
T@\"NSUUID\",R,N,V_UUID
componentsJoinedByString:
data
spoofPPIDMetadata
_expiration
TQ,N,V_state_int
fairPlaySAPSession
retain
MFAA_errorWithDomain:code:failureReason:
set
_forceTokenActivationFailure
confirmActivationForToken:withUUID:withReply:
doubleValue
null
performSelector:withObject:withObject:
setPairingTokenExpirationS:
array
autorelease
sharedInstance
completionQueue
dealloc
bypassFairPlaySAPSignatureVerification
code
internalQueue
setExportedInterface:
stringWithFormat:
performSelector:withObject:
setBypassFairPlaySAPSignatureVerification:
setUserDefaultsQueue:
T@\"NSObject<OS_dispatch_queue>\",&,N,V_completionQueue
_validateCertSerial:issuerSeq:ppid:withReply:
writeToFile:atomically:
T@\"NSString\",R,C
FPSAPS_errorWithCode:andDescription:
URLWithString:
_UUID
init
listener:shouldAcceptNewConnection:
stringByTrimmingCharactersInSet:
uploadTaskWithRequest:fromData:completionHandler:
_checkExpiration
_setCachedStatusForCertSerial:issuerSeq:ppid:certStatus:
hwInfo
setHTTPMethod:
_verifyPairingWithToken:withReply:
conformsToProtocol:
dataWithBytes:length:
openWithCompletionHandler:
TB,N,V_isInternalBuild
expiration
setExpiration:
statusCode
_removePairingWithToken:withReply:
class
countByEnumeratingWithState:objects:count:
dataTaskWithRequest:completionHandler:
dateWithTimeIntervalSinceNow:
disableFairPlaySAP
isEqual:
languageCodeAndCountryCode
UUID
invertedSet
retainCount
session:requestHandshakeWithServer:completionHandler:
setUrlSession:
userDefaults
MFAA_errorWithDomain:code:description:
_sessionContext
TB,N,V_forceTokenActivationFailure
_delegate
addPairingWithToken:withReply:
componentsSeparatedByCharactersInSet:
forceTokenConfirmationFailure
pairingTokenExpirationS
Td,N
_fairPlaySAPSession
dictionaryForKey:
forceFairPlaySAPFailure
forceTokenActivationFailure
isEqualToString:
spoofTokenActivation
superclass
allHeaderFields
removeObjectForKey:
unsignedLongLongValue
serviceListener
T{FairPlayHWInfo_=I[20C]},N,V_hwInfo
currentConnection
invalidateAndCancel
setObject:forKeyedSubscript:
T@\"NSObject<OS_dispatch_queue>\",&,N,V_userDefaultsQueue
sessionContext
certStatusCache
TQ,R
getCachedStatusForCertSerial:issuerSeq:ppid:withReply:
setDelegate:
setSpoofPPIDMetadata:
setWithSet:
userDefaultsQueue
ephemeralSessionConfiguration
isKindOfClass:
setSessionContext:
TB,N,V_bypassFairPlaySAPSignatureVerification
_state_int
_urlSession
certStatusCacheVersion
setPairingTable:
_confirmActivationForToken:withUUID:withReply:
hasBooleanEntitlement:
languageCode
requestActivationForToken:withUUID:withReply:
requestMetadataForToken:withUUID:requestedLocale:requestInfo:withReply:
urlSession
T@\"FairPlaySAPSession\",&,N,V_fairPlaySAPSession
TB,N,V_disableFairPlaySAP
TB,N,V_spoofTokenActivation
close
T@\"NSNumber\",&,N
T@\"NSUserDefaults\",&,N,V_userDefaults
_requestActivationForToken:withUUID:withReply:
resume
_exportedObject
length
setDelegateQueue:
state
_close
countryCode
integerForKey:
objectAtIndexedSubscript:
setCertStatusCache:
timeIntervalSinceNow
_forceFairPlaySAPFailure
_requestMetadataForToken:withUUID:requestedLocale:requestInfo:withReply:
dataWithContentsOfFile:
interfaceWithProtocol:
_getCachedStatusForCertSerial:issuerSeq:ppid:withReply:
appendData:
boolValue
localeIdentifier
respondsToSelector:
session:requestCertificateWithCompletionHandler:
setSpoofTokenActivation:
sharedSession
TTL
_forceNetworkFailure
arrayWithObjects:count:
dictionaryWithObjects:forKeys:count:
exportedObject
isMemberOfClass:
userInfo
valueForEntitlement:
release
_selectedFairPlaySAPServer
dictionary
setForceFairPlaySAPFailure:
hasCategory:forEntitlement:
setPairingTableVersion:
FPSAPS_errorWithCode:
_generateTokenAuthURLRequestForEndpoint:sessionID:signature:requestUUID:
bytes
base64EncodedStringWithOptions:
characterSetWithCharactersInString:
removePairingWithToken:withReply:
debugDescription
setForceNetworkFailure:
setUserDefaults:
_addPairingWithToken:withReply:
_internalQueue
_selectedAPIServer
numberWithUnsignedLongLong:
zone
_requestMetadataForCertSerial:issuerSeq:ppid:requestedLocale:requestInfo:withReply:
appendFormat:
initWithData:encoding:
FPSAPS_errorDescriptionForCode:
hasEntitlement:
dataUsingEncoding:
setTTL:
hash
intValue
numberWithUnsignedInt:
_isInternalBuild
_spoofPPIDMetadata
_userDefaultsQueue
errorWithDomain:code:userInfo:
hexadecimalCharacterSet
isEqualToData:
state_int
boolForKey:
distantFuture
setObject:forKey:
timeIntervalSince1970
T@\"<MFAANetworkProtocol>\",R,N,V_exportedObject
objectForKeyedSubscript:
setCompletionQueue:
setDisableFairPlaySAP:
T@\"NSString\",?,R,C
_spoofTokenActivation
isValidJSONObject:
setCertStatusCacheVersion:
_openFairPlaySAPSession
setValue:forHTTPHeaderField:
localeWithLocaleIdentifier:
requestMetadataForCertSerial:issuerSeq:ppid:requestedLocale:requestInfo:withReply:
requestWithURL:cachePolicy:timeoutInterval:
sessionWithConfiguration:
sessionWithDelegate:
T@\"NSDate\",&,N,V_expiration
setIsInternalBuild:
setState_int:
_hwInfo
UTF8String
mutableBytes
.cxx_destruct
T@\"NSDictionary\",&,N
TQ,N,V_pairingTokenExpirationS
_completionQueue
_userDefaults
dataWithJSONObject:options:error:
delegateQueue
initWithSuiteName:
_bypassFairPlaySAPSignatureVerification
_pairingTokenExpirationS
addObject:
setExportedObject:
setFairPlaySAPSession:
setForceTokenActivationFailure:
MFAA_errorWithDomain:code:
TQ,R,N
_verifyFairPlaySignatureSync:forData:timedOut:error:
_disableFairPlaySAP
initWithBase64EncodedString:options:
setHwInfo:
T#,R
@\"NSUUID\"
v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@\"NSError\">32
v48@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@?<v@?i@\"NSError\">40
#16@0:8
@24@0:8:16
v40@0:8@\"FairPlaySAPSession\"16@\"NSData\"24@?<v@?@\"NSData\"@\"NSError\">32
@40@0:8@16^B24^@32
B
{FairPlayHWInfo_=\"IDLength\"I\"ID\"[20C]}
B24@0:8@16
@32@0:8:16@24
@40@0:8:16@24@32
@48@0:8@16@24@32@40
@\"NSObject<OS_dispatch_queue>\"
v24@0:8@?16
v56@0:8@\"NSData\"16@\"NSString\"24@\"NSLocale\"32@\"NSDictionary\"40@?<v@?@\"NSString\"@\"NSLocale\"@\"NSDictionary\"@\"NSError\">48
@24@0:8q16
@32@0:8q16@24
B24@0:8@\"Protocol\"16
@40@0:8@16q24@32
v24@0:8^{FPSAPContextOpaque_=}16
v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@\"NSData\"@\"NSError\">32
B24@0:8:16
^{_NSZone=}16@0:8
d16@0:8
{FairPlayHWInfo_=I[20C]}16@0:8
v64@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@\"NSLocale\"40@\"NSDictionary\"48@?<v@?@\"NSString\"@\"NSLocale\"@\"NSDictionary\"@\"NSError\">56
@32@0:8@16q24
v32@0:8@\"FairPlaySAPSession\"16@?<v@?@\"NSData\"@\"NSError\">24
v40@0:8@16@24@?32
v20@0:8B16
Q
v32@0:8@\"NSData\"16@?<v@?B@\"NSError\">24
Q16@0:8
@\"NSURLSession\"
@\"<FairPlaySAPSessionDelegate>\"
^{FPSAPContextOpaque_=}
v48@0:8@16@24@32@?40
@\"NSString\"16@0:8
B48@0:8@16@24^B32^@40
v44@0:8@16@24@32i40
v24@0:8d16
v24@0:8Q16
@\"NSDate\"
B32@0:8@16@24
v40@0:8{FairPlayHWInfo_=I[20C]}16
v56@0:8@16@24@32@40@?48
@16@0:8
B16@0:8
v24@0:8@16
@\"NSUserDefaults\"
@24@0:8@16
^{FPSAPContextOpaque_=}16@0:8
v32@0:8@16@?24
@\"FairPlaySAPSession\"
v64@0:8@16@24@32@40@48@?56
v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24
B24@0:8#16
Vv16@0:8
B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24
v16@0:8
@\"<MFAANetworkProtocol>\"
deviceservices/activateAccessory
session-identifier
SpoofTokenActivation
prod
ReleaseType
deviceservices/sapSession
application/json
true
1234
brand
FairPlaySAPServer
https://aquila-maint.corp.apple.com
Use +[%@ %@] instead of +[%@ %@].
blacklisted_status
v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24
[Generating Handshake Request]
BypassFairPlaySAPSignatureVerification
valid
MFAAPairingManagerErrorDomain
certification_status
Invalid pairingToken provided.
<Undefined>
An invalid parameter was provided by the caller.
An internal error has occurred.
InternalBuild
locale
v20@?0B8@\"NSError\"12
Apple Inc.
Session must be open to verify signature.
General
Token Auth
Pairing
MFAATokenManagerErrorDomain
Framework client is missing entitlement.
com.apple.accessories.signposts
Could not initialize session.
[Initializing]
com.apple.MFAAuthentication
Timestamp
000000-0000
ut
custom
An unknown error has occurred.
session-validity
v16@?0@\"NSError\"8
model
Not Certified
FairPlaySAPSessionErrorDomain
v24@?0@\"NSData\"8@\"NSError\"16
MFAAuthenticationErrorDomain
Beta
%02X 
wapi
tokens
ForceTokenConfirmationFailure
CertStatusCacheVersion
com.apple.MFAAuthentication.PreferencesDidChangeNotification
An internal server error has occurred.
https://aquila.apple.com
certificate-auth
Test Accessory
TA-01
ProductType
https://albert.apple.com
X-Mescal-Skipped
Invalid cert code returned from server: %d
https://aquila-it.corp.apple.com
Could not Base64 encode pairing token.
%@-%lu.delegateQueue
RegionCode
X-Request-ID
https://iphonesysut.corp.apple.com
ppid_code
userDefaultsQueue
category
%@_%@
Session must be open to generate signature.
v8@?0
PairingTokenExpirationS
%02X
https://static.ips.apple.com
certSerial, certIssuerSeq, ppid or requestedLocale = nil.
Q
Endpoint
maint
deviceservices/setup.crt
session-request
Certified
%@-%lu.completionQueue
Cannot perform this action in the current state.
[Waiting For Handshake Response]
PearlIDCapability
Session is already open or initializing.
AudioAccessory
ProductVersion
DeviceClass
deviceservices/validateCertificate
Content-Type
Transport
FairPlay is not available on this platform.
[Processing Handshake Response]
ForceFairPlaySAPFailure
request_info
PairingTableVersion
signature
ppid
ppid_metadata
The server has determined that the data provided was invalid.
Connection
Certificate Auth
1.0
https://aquila-ut.corp.apple.com
uuid
token, uuid, or requestedLocale = nil.
No
Server
<print error>
com.apple.accessories.frameworks
deviceservices/ackAccessory
token-auth
pairing
[Closed]
[Open]
cert_serial
%@/%@
CustomServer
ForceNetworkFailure
protocol-version
Must use +[%@ %@] instead of +[%@ %@]!
[Waiting For Certificate]
CertStatusCache
(null)
AuthFeatures
issuer_dn
The provided token data could not be parsed.
%@ <state: %@, TTL: %fs>
[Initialized]
ForceTokenActivationFailure
BypassCertificateExpirationCheck
accessory_name
SpoofCertificateStatus
it
https://iphonesysmaint.corp.apple.com
session-info
certificates
cert_code
certSerial, certIssuerSeq, or ppid = nil.
%@-%lu.internalQueue
DisableFairPlaySAP
default
MFAACertificateManagerErrorDomain
Accept
token or uuid = nil.
https://iphonesysit.corp.apple.com
i
There was a problem connecting to the network.
POST
SpoofPPIDMetadata
Status
PairingTable
invalid
revoked
deviceservices/queryProductPlan
Timed out waiting to verify FairPlay SAP signature!
Spoofing PPID metadata...
isValidJSONObject (requestDict) = NO!
Cert serial found in local cache! (cachedCertStatus: %{coreacc:MFAACertificateManager_CertStatus_t}d, timestamp: %@, certSerial: %{private}@)
Pairing table doesn't exist, creating it...
tokens.length: %lu
tokenArray: %{private}@
Adding cert status to cache... (certSerial: %{private}@)
tokens: %@
[#FairPlaySAPSession] Invalid certificate received!
Spoofing token activation...
[#FairPlaySAPSession] Invalid parameter! (data.class: %@, data: %@)
[#FairPlaySAPSession] Could not tear down FairPlay SAP session! (status: %d)
Initialized FairPlay SAP Session: %@
Invalidating NSURLSession...
Created %d log object(s)!
certIssuerSeqDict: %@
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
[#FairPlaySAPSession] Could not process handshake response! (status: %d, returnCode: %d)
Pairing token is valid - updating timestamp...
Opening FairPlay SAP session...
Cannot verify FairPlay SAP signature with nil parameters!
Server responded with invalid HTTP status code: %ld!\nresponseData (string): %@
newToken.length: %lu, newToken: %{private}@
Forcing token confirmation failure...
[#FairPlaySAPSession] Checking expiration for session (expiration: %@)...
requestData (string): %{private}@
responseData.length: %lu
Bypassing verification of FairPlay SAP signature from server...
Cert serial not found in local cache... (certSerial: %{private}@)
pItemEnd: %p
requestDict: %{private}@
Requesting activation for token: %{private}@ (token.length: %lu, uuid: %@, requestUUID: %@)
Forcing token activation failure...
Requesting PPID metadata for token: %{private}@ (token.length: %lu, uuid: %@, requestedLocale: %@ [%@], requestUUID: %@)
responseData (string): %{private}@
[#FairPlaySAPSession] Invalid parameter! (signature.class: %@, data.class: %@, signature: %@, data: %@)
Failed to create os_log_t object %s: %s!
fairPlayError: %@
self._selectedAPIServer: %@
request.allHTTPHeaderFields: %@
Different cert serial than requested returned from server: %{private}@ (requested: %{private}@)
pDataEnd: %p
Sleeping %dms...
responseJSONError: %@
newTokenArray: %{private}@
Local cert cache doesn't exist, creating it...
pairingTable: %{private}@
certStatus: %{coreacc:MFAACertificateManager_CertStatus_t}d, certCode: %@, ppidCode: %@
pairingTokenBase64: %{private}@
pairingTableVersion: %@
Requesting handshake for FairPlay SAP session...
pItemBegin: %p
taskError: %@
Invalid cachedCertStatus! Setting to Unknown...
Removing cert status from cache... (certSerial: %{private}@)
Verifying pairing status with token: %{private}@ (pairingToken.length: %lu)
itemLength: %zu
[#FairPlaySAPSession] Could not generate handshake request data! (status: %d, returnCode: %d)
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
[#FairPlaySAPSession] Opening session...
certStatusCacheVersion: %@
Initializing %@...
Couldn't open FairPlay SAP session:\n%@
error: %@
request: %@
Invalid locale identifier received from server: '%@'
certStatusCache: %@
certSerialDict: %@
Created log object %s: %s
requestData.length: %lu
Validating certificate serial: %{private}@ (certSerial.length: %lu, issuerSeq.length: %lu, ppid: %{private}@, requestUUID: %@)
Getting cached status for cert serial: %{private}@ (certSerial.length: %lu, issuerSeq.length: %lu, ppid: %{private}@)
Local cache doesn't exist!
pairingEntryTimestamp: %llu, currentTimestamp: %llu, delta: %lld
pairingEntryMutable: %{private}@
[#FairPlaySAPSession] Session is past expiration, closing session...
Unknown server selected: '%@'. Falling back to production server...
encodedTokenArray: %{private}@
response: %@
PPID returned from server does not match provided PPID! (providedPPID: %{private}@, returnedPPID: %{private}@)
[#FairPlaySAPSession] Error requesting certificate: %@
[#FairPlaySAPSession] Received certificate!
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
responseData is empty!
certArray: %{private}@
Updated local cert cache!
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
Confirming activation for token: %{private}@ (token.length: %lu, uuid: %@, requestUUID: %@)
Adding pairing with token: %{private}@ (pairingToken.length: %lu)
Removing pairing token from table... (pairingToken: %{private}@, pairingToken.length: %lu, pairingTokenBase64: %{private}@)
self._selectedFairPlaySAPServer: %@
Pairing token is expired - removing it from pairing table...
requestJSONError: %@
Invalid JSON response received from server! %{private}@
certSerialResponse: %{private}@
[#FairPlaySAPSession] Received handshake response!
[#FairPlaySAPSession] Verifying signature...
Timed out waiting to generate FairPlay SAP signature!
Invalid JSON response received from server!\n%{private}@
Adding pairing token to table... (pairingTokenBase64: %{private}@)
Requesting certificate for FairPlay SAP session...
[#FairPlaySAPSession] Error requesting handshake: %@
[#FairPlaySAPSession] Closing session...
Requesting PPID metadata for certificate serial: %{private}@ (certSerial.length: %lu, issuerSeq.length: %lu, ppid: %{private}@, requestedLocale: %@ [%@], requestUUID: %@)
Removing pairing with token: %{private}@ (pairingToken.length: %lu)
Pairing token not found in pairing table! (pairingToken: %{private}@, pairingToken.length: %lu, pairingTokenBase64: %{private}@)
Forcing network failure...
responseDict: %{private}@
Server responded with invalid HTTP status code: %ld!
ret: %d
[#FairPlaySAPSession] Invalid handshake response received!
pairingTokenExpirationS: %lu
Spoofing token confirmation...
Updated pairing table!
Pairing token found in pairing table! (timestamp: %@, pairingToken: %{private}@, pairingToken.length: %lu, pairingTokenBase64: %{private}@)
[#FairPlaySAPSession] Could not initialize session! (status: %d)
[#FairPlaySAPSession] self.state_int: %@
FairPlay SAP session opened!
tokenArray.count: %lu
[#FairPlaySAPSession] Could not generate signature! (status: %d)
[#FairPlaySAPSession] Signature verification failed! (status: %d)
Skipping generation of FairPlay SAP signature...
pairingTokenDict: %@
[#FairPlaySAPSession] Setting TTL... (TTL: %f, self.expiration: %@)
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Invalid token array received from server - newTokenArray: %{private}@, newTokenArray.count: %lu!
decodedNewTokenArray: %{private}@
pairingTableMutable: %{private}@
handshakeData = nil!
Invalid response dictionary received from server! (responseDict.count: %lu, responseDict: %{private}@)
Pairing table doesn't exist!
tokenArray: %@
[#FairPlaySAPSession] Generating signature...
```
