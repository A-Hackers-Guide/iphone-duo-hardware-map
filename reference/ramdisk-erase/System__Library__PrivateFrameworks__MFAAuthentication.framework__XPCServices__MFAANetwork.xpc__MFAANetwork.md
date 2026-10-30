# `/System/Library/PrivateFrameworks/MFAAuthentication.framework/XPCServices/MFAANetwork.xpc/MFAANetwork`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 2,217,616 bytes.

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
T@\"NSObject<OS_dispatch_queue>\",&,N,V_completionQueue
close
listener:shouldAcceptNewConnection:
stringWithFormat:
timeIntervalSinceNow
userInfo
MFAA_errorWithDomain:code:
isEqualToData:
TB,N,V_forceNetworkFailure
_fairPlaySignatureForDataSync:timedOut:error:
_selectedFairPlaySAPServer
_spoofTokenActivation
certStatusCacheVersion
countByEnumeratingWithState:objects:count:
dictionaryWithDictionary:
serviceListener
_delegateQueue
_requestMetadataForCertSerial:issuerSeq:ppid:requestedLocale:requestInfo:withReply:
exportedObject
setHTTPMethod:
T@\"NSObject<OS_dispatch_queue>\",&,N,V_internalQueue
sessionContext
boolValue
allHeaderFields
base64EncodedStringWithOptions:
_completionQueue
_forceTokenConfirmationFailure
description
forceTokenActivationFailure
objectForKey:
_urlSession
errorWithDomain:code:userInfo:
writeToFile:atomically:
_verifyPairingWithToken:withReply:
MFAA_errorWithDomain:code:description:
dataWithContentsOfFile:
T@\"NSNumber\",&,N
_openFairPlaySAPSession
delegate
setForceTokenConfirmationFailure:
TB,N,V_isInternalBuild
_bypassFairPlaySAPSignatureVerification
_generateTokenAuthURLRequestForEndpoint:sessionID:signature:requestUUID:
setExportedObject:
languageCodeAndCountryCode
setPairingTable:
_addPairingWithToken:withReply:
dictionaryWithObjects:forKeys:count:
setBypassFairPlaySAPSignatureVerification:
signatureForData:completionHandler:
userDefaultsQueue
T@\"FairPlaySAPSession\",&,N,V_fairPlaySAPSession
_delegate
hwInfo
mutableCopy
stringByTrimmingCharactersInSet:
respondsToSelector:
retainCount
T@\"NSURLSession\",&,N,V_urlSession
conformsToProtocol:
invalidateAndCancel
sessionWithConfiguration:
superclass
T{FairPlayHWInfo_=I[20C]},N,V_hwInfo
URLWithString:
isEqual:
numberWithUnsignedInt:
objectForKeyedSubscript:
interfaceWithProtocol:
isEqualToString:
performSelector:
setCertStatusCache:
urlSession
T@\"NSString\",R,C
.cxx_destruct
_exportedObject
T@\"NSDictionary\",&,N
_UUID
_checkExpiration
_fairPlaySAPSession
distantFuture
debugDescription
T@\"NSUUID\",R,N,V_UUID
dataWithJSONObject:options:error:
dateWithTimeIntervalSinceNow:
delegateQueue
forceFairPlaySAPFailure
forceTokenConfirmationFailure
setUserDefaultsQueue:
mutableBytes
TB,N,V_spoofPPIDMetadata
T#,R
T@\"NSString\",?,R,C
_expiration
dataWithBytes:length:
appendFormat:
completionQueue
TB,N,V_forceTokenConfirmationFailure
dictionary
isValidJSONObject:
setDelegateQueue:
T@\"NSUserDefaults\",&,N,V_userDefaults
_disableFairPlaySAP
_isInternalBuild
_removePairingWithToken:withReply:
setHwInfo:
setObject:forKey:
TB,N,V_bypassFairPlaySAPSignatureVerification
pairingTable
setState_int:
data
setSessionContext:
zone
_hwInfo
bypassFairPlaySAPSignatureVerification
doubleValue
FPSAPS_errorWithCode:
TQ,N,V_state_int
_selectedAPIServer
pairingTokenExpirationS
setPairingTokenExpirationS:
TB,N,V_disableFairPlaySAP
_requestActivationForToken:withUUID:withReply:
_setCachedStatusForCertSerial:issuerSeq:ppid:certStatus:
dictionaryForKey:
ephemeralSessionConfiguration
fairPlaySAPSession
uploadTaskWithRequest:fromData:completionHandler:
TQ,N,V_pairingTokenExpirationS
_forceFairPlaySAPFailure
_requestMetadataForToken:withUUID:requestedLocale:requestInfo:withReply:
arrayWithObjects:count:
getCachedStatusForCertSerial:issuerSeq:ppid:withReply:
initWithSuiteName:
sharedInstance
_verifyFairPlaySignatureSync:forData:timedOut:error:
appendData:
numberWithUnsignedLongLong:
unsignedLongLongValue
containsObject:
MFAA_errorWithDomain:code:failureReason:
TB,N,V_forceTokenActivationFailure
_forceNetworkFailure
_spoofPPIDMetadata
autorelease
hexadecimalCharacterSet
requestMetadataForToken:withUUID:requestedLocale:requestInfo:withReply:
self
setUrlSession:
TQ,R,N
dataUsingEncoding:
languageCode
removePairingWithToken:withReply:
verifyPairingWithToken:withReply:
release
TB,N,V_forceFairPlaySAPFailure
addObject:
class
null
code
integerForKey:
openWithCompletionHandler:
setObject:forKeyedSubscript:
isProxy
setCompletionQueue:
setSpoofTokenActivation:
_userDefaultsQueue
_validateCertSerial:issuerSeq:ppid:withReply:
addPairingWithToken:withReply:
T@\"<MFAANetworkProtocol>\",R,N,V_exportedObject
hasEntitlement:
dealloc
_confirmActivationForToken:withUUID:withReply:
requestMetadataForCertSerial:issuerSeq:ppid:requestedLocale:requestInfo:withReply:
setFairPlaySAPSession:
setForceFairPlaySAPFailure:
setInternalQueue:
setUserDefaults:
T@\"NSDate\",&,N,V_expiration
_close
dataTaskWithRequest:completionHandler:
initWithBase64EncodedString:options:
setExportedInterface:
componentsSeparatedByCharactersInSet:
length
T^{FPSAPContextOpaque_=},N,V_sessionContext
UTF8String
componentsJoinedByString:
count
date
requestWithURL:cachePolicy:timeoutInterval:
session:requestCertificateWithCompletionHandler:
_forceTokenActivationFailure
allHTTPHeaderFields
initWithDelegate:
isKindOfClass:
setDelegate:
setExpiration:
setForceTokenActivationFailure:
init
removeObjectForKey:
setSpoofPPIDMetadata:
stringWithString:
validateCertSerial:issuerSeq:ppid:withReply:
valueForEntitlement:
JSONObjectWithData:options:error:
TTL
hasBooleanEntitlement:
FPSAPS_errorDescriptionForCode:
T@\"NSObject<OS_dispatch_queue>\",&,N,V_userDefaultsQueue
setTTL:
_userDefaults
internalQueue
isMemberOfClass:
raise:format:
statusCode
set
expiration
T@\"<FairPlaySAPSessionDelegate>\",W,N,V_delegate
disableFairPlaySAP
hash
setWithSet:
stringForKey:
_state_int
setValue:forHTTPHeaderField:
TQ,R
intValue
sharedSession
state_int
invertedSet
objectAtIndexedSubscript:
setPairingTableVersion:
array
boolForKey:
certStatusCache
T@\"NSObject<OS_dispatch_queue>\",&,N,V_delegateQueue
UUID
instancesRespondToSelector:
timeIntervalSince1970
verifySignature:forData:completionHandler:
_init
setForceNetworkFailure:
FPSAPS_errorWithCode:andDescription:
_getCachedStatusForCertSerial:issuerSeq:ppid:withReply:
characterSetWithCharactersInString:
performSelector:withObject:withObject:
sessionWithDelegate:
_internalQueue
confirmActivationForToken:withUUID:withReply:
state
TB,N,V_spoofTokenActivation
initWithData:encoding:
localeWithLocaleIdentifier:
performSelector:withObject:
spoofTokenActivation
_sessionContext
UUIDString
currentConnection
forceNetworkFailure
session:requestHandshakeWithServer:completionHandler:
pairingTableVersion
userDefaults
_pairingTokenExpirationS
setIsInternalBuild:
hasCategory:forEntitlement:
setCertStatusCacheVersion:
Td,N
bytes
countryCode
localeIdentifier
requestActivationForToken:withUUID:withReply:
retain
setDisableFairPlaySAP:
spoofPPIDMetadata
resume
isInternalBuild
B24@0:8@\"Protocol\"16
v24@0:8d16
@32@0:8@16q24
@40@0:8@16q24@32
v24@0:8@16
v24@0:8^{FPSAPContextOpaque_=}16
v56@0:8@\"NSData\"16@\"NSString\"24@\"NSLocale\"32@\"NSDictionary\"40@?<v@?@\"NSString\"@\"NSLocale\"@\"NSDictionary\"@\"NSError\">48
^{_NSZone=}16@0:8
v20@0:8B16
@\"<FairPlaySAPSessionDelegate>\"
^{FPSAPContextOpaque_=}
v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@\"NSError\">32
v48@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@?<v@?i@\"NSError\">40
@32@0:8:16@24
B24@0:8#16
@40@0:8@16^B24^@32
v24@0:8Q16
@\"NSUUID\"
v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@\"NSData\"@\"NSError\">32
B32@0:8@16@24
{FairPlayHWInfo_=I[20C]}16@0:8
@32@0:8q16@24
v40@0:8@16@24@?32
@\"NSUserDefaults\"
Q
@24@0:8q16
#16@0:8
@16@0:8
@40@0:8:16@24@32
B48@0:8@16@24^B32^@40
v44@0:8@16@24@32i40
@\"NSDate\"
v32@0:8@16@?24
v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24
Q16@0:8
@\"FairPlaySAPSession\"
@\"NSURLSession\"
v48@0:8@16@24@32@?40
B24@0:8@16
@24@0:8:16
B24@0:8:16
v40@0:8@\"FairPlaySAPSession\"16@\"NSData\"24@?<v@?@\"NSData\"@\"NSError\">32
B
d16@0:8
v32@0:8@\"NSData\"16@?<v@?B@\"NSError\">24
v56@0:8@16@24@32@40@?48
v64@0:8@16@24@32@40@48@?56
B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24
@\"<MFAANetworkProtocol>\"
@\"NSObject<OS_dispatch_queue>\"
B16@0:8
Vv16@0:8
v40@0:8{FairPlayHWInfo_=I[20C]}16
@48@0:8@16@24@32@40
^{FPSAPContextOpaque_=}16@0:8
{FairPlayHWInfo_=\"IDLength\"I\"ID\"[20C]}
v64@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@\"NSLocale\"40@\"NSDictionary\"48@?<v@?@\"NSString\"@\"NSLocale\"@\"NSDictionary\"@\"NSError\">56
v16@0:8
@24@0:8@16
v24@0:8@?16
@\"NSString\"16@0:8
v32@0:8@\"FairPlaySAPSession\"16@?<v@?@\"NSData\"@\"NSError\">24
ut
ReleaseType
https://iphonesysmaint.corp.apple.com
https://aquila.apple.com
ppid_metadata
model
category
SpoofCertificateStatus
An internal error has occurred.
uuid
000000-0000
Could not Base64 encode pairing token.
%@ <state: %@, TTL: %fs>
CertStatusCache
valid
General
certificates
DisableFairPlaySAP
Timestamp
(null)
Certificate Auth
MFAAuthenticationErrorDomain
1234
TA-01
No
ForceNetworkFailure
CertStatusCacheVersion
An internal server error has occurred.
Apple Inc.
token or uuid = nil.
certSerial, certIssuerSeq, ppid or requestedLocale = nil.
pairing
Token Auth
v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24
request_info
Not Certified
Connection
Session must be open to generate signature.
[Generating Handshake Request]
[Waiting For Handshake Response]
com.apple.accessories.frameworks
PearlIDCapability
https://albert.apple.com
https://aquila-maint.corp.apple.com
deviceservices/sapSession
session-identifier
Transport
SpoofTokenActivation
prod
protocol-version
i
Endpoint
%@-%lu.completionQueue
v8@?0
com.apple.MFAAuthentication
default
https://iphonesysit.corp.apple.com
deviceservices/ackAccessory
Accept
ForceTokenActivationFailure
Status
revoked
ppid
session-info
accessory_name
certificate-auth
tokens
POST
token-auth
[Initialized]
FairPlaySAPServer
AuthFeatures
Beta
ppid_code
Could not initialize session.
Session must be open to verify signature.
[Initializing]
PairingTableVersion
There was a problem connecting to the network.
wapi
AudioAccessory
X-Request-ID
maint
com.apple.MFAAuthentication.PreferencesDidChangeNotification
Framework client is missing entitlement.
v24@?0@\"NSData\"8@\"NSError\"16
The server has determined that the data provided was invalid.
FairPlaySAPSessionErrorDomain
%@-%lu.internalQueue
signature
issuer_dn
The provided token data could not be parsed.
Must use +[%@ %@] instead of +[%@ %@]!
BypassCertificateExpirationCheck
1.0
deviceservices/activateAccessory
true
BypassFairPlaySAPSignatureVerification
<print error>
deviceservices/queryProductPlan
session-validity
Test Accessory
MFAATokenManagerErrorDomain
An unknown error has occurred.
deviceservices/validateCertificate
session-request
userDefaultsQueue
Certified
Invalid cert code returned from server: %d
com.apple.accessories.signposts
DeviceClass
https://aquila-ut.corp.apple.com
certification_status
[Waiting For Certificate]
it
https://static.ips.apple.com
Server
%02X 
cert_serial
%@/%@
PairingTokenExpirationS
RegionCode
Content-Type
Cannot perform this action in the current state.
locale
custom
Use +[%@ %@] instead of +[%@ %@].
v16@?0@\"NSError\"8
Session is already open or initializing.
MFAAPairingManagerErrorDomain
ProductType
https://iphonesysut.corp.apple.com
https://aquila-it.corp.apple.com
X-Mescal-Skipped
CustomServer
SpoofPPIDMetadata
ProductVersion
cert_code
Q
%@_%@
FairPlay is not available on this platform.
[Open]
<Undefined>
ForceTokenConfirmationFailure
%02X
Pairing
InternalBuild
application/json
token, uuid, or requestedLocale = nil.
PairingTable
An invalid parameter was provided by the caller.
%@-%lu.delegateQueue
[Processing Handshake Response]
MFAACertificateManagerErrorDomain
deviceservices/setup.crt
brand
certSerial, certIssuerSeq, or ppid = nil.
Invalid pairingToken provided.
invalid
v20@?0B8@\"NSError\"12
blacklisted_status
[Closed]
ForceFairPlaySAPFailure
Invalidating NSURLSession...
tokenArray.count: %lu
isValidJSONObject (requestDict) = NO!
requestData.length: %lu
Adding pairing with token: %{private}@ (pairingToken.length: %lu)
pairingTableMutable: %{private}@
request.allHTTPHeaderFields: %@
certArray: %{private}@
self._selectedAPIServer: %@
Invalid response dictionary received from server! (responseDict.count: %lu, responseDict: %{private}@)
Pairing token found in pairing table! (timestamp: %@, pairingToken: %{private}@, pairingToken.length: %lu, pairingTokenBase64: %{private}@)
Couldn't open FairPlay SAP session:\n%@
Invalid token array received from server - newTokenArray: %{private}@, newTokenArray.count: %lu!
Confirming activation for token: %{private}@ (token.length: %lu, uuid: %@, requestUUID: %@)
pairingTableVersion: %@
Pairing token is valid - updating timestamp...
[#FairPlaySAPSession] Invalid parameter! (signature.class: %@, data.class: %@, signature: %@, data: %@)
requestDict: %{private}@
requestData (string): %{private}@
Invalid JSON response received from server! %{private}@
[#FairPlaySAPSession] Received handshake response!
Getting cached status for cert serial: %{private}@ (certSerial.length: %lu, issuerSeq.length: %lu, ppid: %{private}@)
certSerialDict: %@
[#FairPlaySAPSession] Could not generate signature! (status: %d)
responseData is empty!
tokens.length: %lu
[#FairPlaySAPSession] Setting TTL... (TTL: %f, self.expiration: %@)
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Updated pairing table!
Forcing network failure...
Forcing token activation failure...
Pairing token is expired - removing it from pairing table...
Server responded with invalid HTTP status code: %ld!
[#FairPlaySAPSession] Opening session...
Requesting PPID metadata for token: %{private}@ (token.length: %lu, uuid: %@, requestedLocale: %@ [%@], requestUUID: %@)
Invalid locale identifier received from server: '%@'
Adding pairing token to table... (pairingTokenBase64: %{private}@)
pItemBegin: %p
itemLength: %zu
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
[#FairPlaySAPSession] Invalid parameter! (data.class: %@, data: %@)
Failed to create os_log_t object %s: %s!
responseData.length: %lu
Requesting activation for token: %{private}@ (token.length: %lu, uuid: %@, requestUUID: %@)
Removing pairing with token: %{private}@ (pairingToken.length: %lu)
pairingTokenExpirationS: %lu
fairPlayError: %@
responseDict: %{private}@
Spoofing PPID metadata...
Local cache doesn't exist!
Requesting certificate for FairPlay SAP session...
[#FairPlaySAPSession] Error requesting certificate: %@
[#FairPlaySAPSession] Invalid certificate received!
FairPlay SAP session opened!
pairingTokenBase64: %{private}@
pairingTable: %{private}@
[#FairPlaySAPSession] Signature verification failed! (status: %d)
Removing pairing token from table... (pairingToken: %{private}@, pairingToken.length: %lu, pairingTokenBase64: %{private}@)
pairingEntryTimestamp: %llu, currentTimestamp: %llu, delta: %lld
Initializing %@...
response: %@
Bypassing verification of FairPlay SAP signature from server...
decodedNewTokenArray: %{private}@
certStatusCacheVersion: %@
[#FairPlaySAPSession] self.state_int: %@
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
Spoofing token activation...
Different cert serial than requested returned from server: %{private}@ (requested: %{private}@)
certStatus: %{coreacc:MFAACertificateManager_CertStatus_t}d, certCode: %@, ppidCode: %@
handshakeData = nil!
Spoofing token confirmation...
[#FairPlaySAPSession] Could not initialize session! (status: %d)
[#FairPlaySAPSession] Could not generate handshake request data! (status: %d, returnCode: %d)
Timed out waiting to generate FairPlay SAP signature!
Cannot verify FairPlay SAP signature with nil parameters!
newTokenArray: %{private}@
[#FairPlaySAPSession] Received certificate!
pDataEnd: %p
ret: %d
pItemEnd: %p
tokenArray: %{private}@
Skipping generation of FairPlay SAP signature...
responseJSONError: %@
Invalid cachedCertStatus! Setting to Unknown...
Updated local cert cache!
Verifying pairing status with token: %{private}@ (pairingToken.length: %lu)
[#FairPlaySAPSession] Could not process handshake response! (status: %d, returnCode: %d)
responseData (string): %{private}@
Validating certificate serial: %{private}@ (certSerial.length: %lu, issuerSeq.length: %lu, ppid: %{private}@, requestUUID: %@)
Pairing token not found in pairing table! (pairingToken: %{private}@, pairingToken.length: %lu, pairingTokenBase64: %{private}@)
Opening FairPlay SAP session...
PPID returned from server does not match provided PPID! (providedPPID: %{private}@, returnedPPID: %{private}@)
Local cert cache doesn't exist, creating it...
Adding cert status to cache... (certSerial: %{private}@)
pairingTokenDict: %@
tokenArray: %@
Timed out waiting to verify FairPlay SAP signature!
newToken.length: %lu, newToken: %{private}@
Cert serial found in local cache! (cachedCertStatus: %{coreacc:MFAACertificateManager_CertStatus_t}d, timestamp: %@, certSerial: %{private}@)
certIssuerSeqDict: %@
Requesting handshake for FairPlay SAP session...
[#FairPlaySAPSession] Invalid handshake response received!
Invalid JSON response received from server!\n%{private}@
Cert serial not found in local cache... (certSerial: %{private}@)
[#FairPlaySAPSession] Verifying signature...
[#FairPlaySAPSession] Checking expiration for session (expiration: %@)...
Pairing table doesn't exist!
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Unknown server selected: '%@'. Falling back to production server...
Sleeping %dms...
self._selectedFairPlaySAPServer: %@
[#FairPlaySAPSession] Generating signature...
certStatusCache: %@
Removing cert status from cache... (certSerial: %{private}@)
tokens: %@
[#FairPlaySAPSession] Could not tear down FairPlay SAP session! (status: %d)
Requesting PPID metadata for certificate serial: %{private}@ (certSerial.length: %lu, issuerSeq.length: %lu, ppid: %{private}@, requestedLocale: %@ [%@], requestUUID: %@)
taskError: %@
certSerialResponse: %{private}@
Pairing table doesn't exist, creating it...
pairingEntryMutable: %{private}@
[#FairPlaySAPSession] Session is past expiration, closing session...
Forcing token confirmation failure...
Initialized FairPlay SAP Session: %@
error: %@
encodedTokenArray: %{private}@
request: %@
[#FairPlaySAPSession] Closing session...
Created %d log object(s)!
requestJSONError: %@
Server responded with invalid HTTP status code: %ld!\nresponseData (string): %@
[#FairPlaySAPSession] Error requesting handshake: %@
Created log object %s: %s
ServiceDelegate
NSXPCListenerDelegate
NSObject
Entitlements
FairPlaySAPSessionDelegate
MFAANetworkExported
Additions
MFAANetworkProtocol
MFAAError
MFAANetwork
FairPlaySAPSession
FairPlaySAPSessionError
```
