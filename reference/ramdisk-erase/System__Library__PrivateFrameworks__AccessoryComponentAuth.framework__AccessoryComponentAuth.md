# `/System/Library/PrivateFrameworks/AccessoryComponentAuth.framework/AccessoryComponentAuth`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 415,600 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 29 (Size: 4096)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (12)

- `/System/Library/PrivateFrameworks/AccessoryComponentAuth.framework/AccessoryComponentAuth (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libFDR.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (3 classes, 1 protocols)

Classes: `ACCHWComponentAuthService`, `ACCHWComponentAuthServiceParams`, `ACCUserDefaults`

Protocols: `ACCHWComponentAuthServiceProtocol`

## Strings (609)

```
AllowACCAuthProtocolOnAllTransport
v12@?0i8
Beta
PretendAccessoryType
AppleAuthCP
InternalBuild
Uptime
FDRStatusFail
TimeSync
NFCColorOverride
UARPActivityTimerS
HW Component Auth
General
-[ACCHWComponentAuthService _validateWithFDRCertificate:forModuleType:withAuthParams:]
CreateCertificateSerialNumberError
wapi
UseCertDataPropertyForAuth
Failed
ForceAuthFail
DisableACCAuthProtocolOnInductive
WaitForiAPTrafficDelayMS
com.apple.accessories.frameworks.core-accessories
AccessoryCertificate
IdentityCertUseTime
EnableWrongOrientationMessage
SkipGaugeSignatureCheck
no
SerialNumberCompareError
AccessoryCertificateSerialNumber
AuthTTRForAllTransports
DisableAuthFailureTTRForXR
IgnoreAccInfoUpdateRelaySupport
LeafCertData
CopyAllowUnsealed
SigningFuse
VerifyNonceSignatureError
IgnoreIsOnAC
MPPAuthGetLeafCertFirst
com.apple.accessories.authCPEvent
CreateSerialNumberStringFromDataError
RegionCode
cpGetChallengeSignatureLengths
IdentityCertRefreshState
BLEPairingConfigRequestDelayMs
MFi4ECDSADisallow
EnableManager2ForTransport
com.apple.ACCHWComponentAuthService.battery
IOTimeoutDeviceBusyError
DisableCertSupport
com.apple.iapd
com.apple.accessoryd
BLEPairingIgnoreZeroEarlyInfo
MFi4RelayReadRetryDelayMs
ComponentName
authState
FDRStatus
com.apple.ACCHWComponentAuthService.rcam
OverrideCanReceiveInductivePowerOID
authError
App Links
Connection
isTrustedForUI
cpGetComponentIndex: Failed to find ComponentIndex property
NFCAnalyticsDate
com.apple.accessories.hwComponent.isTrusted.failure
Transport Client
IORegistryEntryID
DisableAMSHookUp
AuthenticationOverride
i
NoAuthICPresentError
ShowHiddenAccessories
AllowNFCColorOverride
IgnoreAuthReset
AuthSuccess
Transport
PretendWirelessCTAMatch
ACCAuthProtocolMaxMessageSize
USBHiAPEnable
flags
FullCertData
NullCertificateDataError
InternalComponent
cpSetExpectedPairedCertSN: !CFStringGetCString
iboot-auth
pretend_auth
AuthMinorVersion
CertificateAuthVersionNumberError
Disable1WayNFCForInductive
TransportSignpost
wcrt
CertSerialNumberError
cpGetComponentIndex: Got component index : %x\n
cpCreateFormattedChallengeFromServerRequest
cpGetComponentIndex: Component index not CFNumber
EnableChinaInductiveTx
DisableT56Support
DisableNFCAuthTimer
ChargingPowerOverride
com.apple.ACCHWComponentAuthService.touchcontroller
vcrt
AuthBatteryMismatchOnDevDevice
MPPAuthChallengeFirst
isPeriodic
XpcConnectionError
AuthBatteryMismatchOnProdDevice
PearlIDCapability
Transport Plugins
DisableCertVerification
MFi4AuthTimeoutValueS
Passed
MFi4SigmaIRequired
ChargingPowerBehavior
com.apple.CoreAccessories.PreferencesDidChangeNotification
InternalModuleCapabilityMismatchError
DisableInductiveAuthTTR
ACCAuthProtocolAllowMutualAuth
%02x
CanChargeInductiveError
IgnoreAACPAuthStatus
ComponentBusyError
v8@?0
Battery
bcrt
IDSN
DisableSNOnly
isBatteryModule
prpc
FDRStatusUnknown
Bluetooth Service
com.apple.accessories.signposts
ACCAuthProtocolPretendAuth
SysdiagnoseOnInductiveCTAFailure
GenericMFiIgnoreCertCaps
Endpoint
Use +[%@ %@] instead of -%@.
isInductive
com.apple.ACCHWComponentAuthService.las
tcrt
-
ProductType
DisablePowerUpdateForCurrentDraw
VerifyCertificateSerialNumberError
BLEPairingDontEarlyInfoAsDeviceUID
PretendNFCAuthTimeout
6)
DeviceNonce
PowerSourceUpdateBehavior
AuthDeviceInfoError
CarPlay Service
TouchController
NoDeviceIDSNError
BadArgumentError
AudioAccessory
cpCreateSignatureWithIndexAndToken
InductiveAuthPretendMatchRxID
MPPAuthEnablePretendAuth
UninitializedAuthError
TestCreateBLEPairingOnInductive
MaxOutboundiAP2PacketSize
ComponentIndex
BypassTrustDialog
DeviceIdentityPreArmDateOverride
IdentityCertUseIndex
com.apple.ACCHWComponentAuthService.veridian
ReleaseType
PlatformIDOverride
PretendNFCAuthFailed
AuthTimerExpiredError
ForceAuthTimeout
KeepAACPAuthData
AllowMFi4DevCertsOnProdDevice
ProductVersion
BLEPairingDisableOOBPPlusFlow
MFi4ECDSAOnly
LAS
NoAuthCPServicePresentError
BLEPairingAuthTimeoutValueS
ForceMFi4AuthOverNFC
MissingPairedAuthInstanceError
isTrusted
cpCreateFormattedResponseForServerResponse
Challenge
<Undefined>
AuthPassed
EnableTrustDialog
yes
CreateRandomNonceError
EnableDEVNCertSupport
FDRStatusPass
ConnectionInfo
MismatchedPairingError
DeviceClass
KnownAccessories
TreatAuthCPDEVNAsV3
EnableACCAuthProtocolOnNFC
com.apple.iapd.PreferencesDidChangeNotification
+[ACCHWComponentAuthService _verifyModuleFDR:forModuleType:]
DisableIAPHVCFixForAuth
authErrorDescription
RCAM
VerifyPublicCertificateError
DisableMFi4CertSupport
PretendBatteryLevel
DeviceID
IOAccessory
cpSetActualPairedCertSN: !CFStringGetCString
DontSkipInductiveAuthOnCTA
v36@?0B8@\"NSData\"12@\"NSData\"20B28i32
wiredAuthDuration
CreateCapsFromAuthCertError
PretendAuthFailure
EnableIndonesiaInductiveTx
DisableWirelessCTA
OverrideMPPAuthSupported
SerialNumberPairingError
cpGetTransportEntryId: IOConnectCallScalarMethod failed: 0x%x\n
internalModuleType
DisableAuthTimeoutTTRForXR
IdentityCertIsClassD
SkipNFCAuth
PacketLoggingPlainTextOnly
ForceT56RelaySupport
FirmwareVersion
ACCAuthProtocolRoleSupport
ForceAccInfoUpdateRelaySupport
IdentityCertRefreshInterval
PretendNoNFCResponse
AuthMajorVersion
DisableAACPAuth
IgnorePowerSourceUpdateForAvailableCurrent
VerifyModuleFDRError
External Accessory
SysdiagnoseInsteadOfAuthTTR
NFCSecondaryColorOverride
AuthCPStartDelayMs
RejectionOfMultipleLocation
v28@?0@\"NSData\"8@\"NSData\"16i24
Signature
cpSetAuthError %d\n
cpGetComponentIndex: Component index not SInt32
com.apple.CoreAccessories
com.apple.logging
PretendNoDeviceIdentityCerts
DeviceVersion
EnableAuthTimeoutTTR
MPPAuthPreferredSlot
LiveVoicemailFakeRinging
CreateSignatureError
Veridian
Flags indicate Veridian...do not call cpCopyCertificate()
error evaluating certificate
received response. signature=%@, deviceNonce=%@, authError=%d
verifying battery match using cert %@
(moduleType=%d) Replying with overallAuthPassed = %d, overallFdrValid = %d, authError = %d
(moduleType=%d) Found %lu matching service(s)
(moduleType=%d) Error: Could not parse certificate
AMFDRSealingMapCopyMultiInstanceForClass returned error: %@
_verifyBatteryMatch %d: %ld.%03llu
tryCount = %d (max tries %d)
moduleAuthService = %d
authError %d after _verifyBatteryMatch
CoreAnalytics event: %@\neventDict: %@
auth length = %ld, sizeof(t_bpFDRData_v1) = %lu, does not match
ACASignTouchControllerChallengeWithIndex
(moduleType=%d) authError %d after _signChallenge
Could not cpGetDeviceIDSN: %s\n
error getting MFAACertificateManager
signatureValid ? %@
(moduleType=%d) Error: Could not evaluate certificate
Created log object %s: %s
Failed to create os_log_t object %s: %s!
Flags indicate rcam...do not call cpCopyCertificate()
(moduleType=%d) authError = eNoDeviceIDSNError after _readDeviceIDSN
(moduleType=%d) skip component auth
(moduleType=%d) Error: The component AppleAuthCP was not found, [servicesArray count] is 0
(moduleType=%d) Error: challenge==NULL
(moduleType=%d) Failed to fetch component index: %s\n
(moduleType=%d) authCP service %d tmpAuthFlags == 0x%x
authError %d after _signChallenge
(moduleType=%d) authError = %d after verifyModuleCertificate
Could not cpGetDeviceInfo: %s\n
certificate = %@
(moduleType=%d) Cannot find FDR cert
Sleeping for %d seconds before retrying auth
no error after _verifyBatteryMatch!
Have a match for (t_bpFDRData_v1)
Returning Roswell data of length %ld
cpClearCertificate failed: 0x%x
device nonce = %@
(moduleType=%d) equal:%d
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
acc_internalSettings: internal-only setting %{public}@ active (%ld)
(moduleType=%d) Error: The component AppleAuthCP was not found
error generating signature: auth cp error code %#x\n
(moduleType=%d) %s: cpGetDeviceIDSN failed: ret=%x len=%zu
_signChallengeForModuleType Replying with signature=%@, deviceNonce=%@, authError = %d
dataLength matches Roswell data length, return copy of fdr data
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
(moduleType=%d) sleeping for %d seconds before retrying auth
ACAInitForHIDWithIndex
error verifying serial number
could not open service: %s\n
(moduleType=%d) %s: %d: returned error
no error after _signChallenge!
Have a custom Roswell data structure
(moduleType=%d) Error: The component AppleAuthCP was not found, servicesArray is NULL
(moduleType=%d) tryCount = %d (max tries %d)
(moduleType=%d) Replying with authPassed = %d, fdrValid = %d, authError = %d
AMFDRSealingMapCopyLocalDataForClass returned error = %@
(moduleType=%d) cpSetAuthStatus failed: 0x%x
(moduleType=%d) authError %d after _verifySignature
signature = %@
(moduleType=%d) %s: AMFDRSealingMapCopyLocalDataForClass: returned NULL
verifyBatteryMatch Replying with authError = %d
(moduleType=%d) updateRegistry: cpSetAuthStatus, cpSetTrustStatus
Created %d log object(s)!
received response. response=%@, authError=%d
_verifySignature %d: %ld.%03llu
IDSN length %zu exceeds buffer
(moduleType=%d) cpSetTrustStatus failed: 0x%x
Flags indicate battery...do not call cpCopyCertificate()
_readSignature %d: %ld.%03llu
acc_internalSettings: internal-only setting %{public}@ active
(moduleType=%d) Error: signature==NULL
(moduleType=%d) moduleAuthService = %d
(moduleType=%d) authError = eAuthDeviceInfoError after _verifyDeviceInfo
(moduleType=%d) authError %d after _verifyCertificate
(moduleType=%d) authError %d after _readSignature
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
(moduleType=%d) Could not find authcp services: %s\n
Failed to retrieve device IDSN
(moduleType=%d) cpSetTrustStatusForUI failed: 0x%x
pRoswellDataStructure->roswell_cert_len = %d
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
challenging Veridian using data %@
(moduleType=%d) updateRegistry
(moduleType=%d) %s: AMFDRSealingMapCopyLocalDataForClass returned error=%@
(moduleType=%d) No authIC cert to compare against FDR
Notifying clients of %s
(moduleType=%d) cpSetAuthError failed: 0x%x
(moduleType=%d) done
(moduleType=%d) authError %d after _readCertificate
error parsing certificate
error generating signature: %s\n
ERROR No auth io_service_t is found!
received response. authError=%d
(moduleType=%d) %d: %ld.%03llu
(moduleType=%d) index:%@
(moduleType=%d) Error: The component AppleAuthCP was not found, unexpected NULL service
(moduleType=%d) cpSetBatteryCode failed: 0x%x
error getting certificate
ACCUserDefaults
ACCHWComponentAuthServiceParams
ACCHWComponentAuthService
ACCHWComponentAuthServiceProtocol
_openSessionHandler
authenticateVeridianWithChallenge:completionHandler:componentIndex:
completionHandler
displayAuthUserNVMWrite:key:value:completionHandler:
dealloc
_skipComms
createVeridianNonce:withChallenge:
sharedManager
signVeridianChallenge:completionHandler:
timeIntervalSince1970
unsignedIntValue
_closeSessionHandler
_signature
copy
createVillanovaNonce:IDSN:challenge:
T@?,C,V_signingHandler
TI,N,V_authFlags
_authFlags
_moduleAuthService
arrayForKey:
authenticateBatteryWithChallenge:completionHandler:
boolForKey:
countByEnumeratingWithState:objects:count:
T@\"NSData\",&,N,V_certificate
_batteryCode
certificateRaw
dictionaryWithDictionary:
numberWithDouble:
setCompletionHandler:
setSignature:
T@\"NSData\",&,N,V_deviceNonce
_identityKey
_protocolVersion
displayAuthRefreshAccessState:completionHandler:
isEqualToNumber:
authenticateLASWithChallenge:completionHandler:updateRegistry:componentIndex:
T@\"NSData\",&,N,V_identityCertificates
authenticateRCAMWithChallenge:completionHandler:updateRegistry:
TB,N,V_overrideIdentity
_certificateInfo
setAuthSession:
setIdentityKey:
T@\"NSNumber\",&,N,V_componentIndex
_validateDeviceAndFDRCert:forModuleType:withAuthParams:
boolValue
refreshAccessStateHandler
T@\"NSDictionary\",&,N,V_certificateInfo
T^{mfi4AuthProtocolSession_s=},V_authSession
_sessionUUIDs
addObject:
authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:componentIndex:
dictionaryForKey:
isEqualToData:
isEqualToString:
copyEvaluatedCertificateChainInfo:
setOpenSessionHandler:
setOverrideIdentity:
verifyBatteryMatch:completionHandler:
verifyNonceSignature:nonce:signature:
T@?,C,V_nvmReadSessionHandler
_completionHandler
_verifyBatteryMatch:outputBatteryCode:
authenticateVeridianWithChallenge:completionHandler:
copyPathForPersonalizedData:error:
displayAuthUserNVMRead:key:completionHandler:
identityKey
setModuleAuthService:
signingHandler
_componentIndex
setBatteryCode:
setDeviceNonce:
TI,N,V_batteryCode
authFlags
authenticateLASWithChallenge:completionHandler:updateRegistry:
authenticatedSession
date
_logToAnalytics:authError:fdrValidationStatus:authDurationInMS:
T@?,C,V_completionHandler
challenge
displayAuthCloseSession:completionHandler:
isMFi2_3CertInfo:
nvmReadSessionHandler
setAuthenticatedSession:
setCertificateInfo:
T@\"NSData\",&,N,V_certificateRaw
.cxx_destruct
TI,N,V_moduleAuthService
setNvmReadSessionHandler:
stringForKey:
stringWithUTF8String:
setSigningHandler:
setSkipComms:
signRCAMChallenge:completionHandler:componentIndex:
_nvmReadSessionHandler
authenticateBatteryWithChallenge:completionHandler:componentIndex:
authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:
dataWithContentsOfFile:
setRefreshAccessStateHandler:
_refreshAccessStateHandler
certificate
setNvmWriteSessionHandler:
sharedDefaultsIapd
signVeridianChallenge:completionHandler:componentIndex:
componentIndex
count
displayAuthOpenSession:intermediateCertificate:keyData:completionHandler:
unsignedIntegerValue
T@?,C,V_closeSessionHandler
copyParsedCertificateChainInfo:
_certificateRaw
_authenticatedSession
_findFDRCertData:forModuleType:withAuthParams:hasDeviceCert:withError:
_verifyDeviceInfo:
_verifySignature:
deviceNonce
charValue
initWithSuiteName:
numberWithUnsignedInt:
overrideIdentity
sessionUUIDs
setCertificateRaw:
sharedDefaults
verifyModuleCertificate:forModule:forAuthFlags:forIndex:
closeSessionHandler
T@?,C,V_openSessionHandler
_verifyModuleFDR:forModuleType:
TI,N,V_protocolVersion
_signChallengeForModuleType:challenge:componentIndex:completionHandler:
doubleForKey:
processInfo
skipComms
T@\"NSData\",&,N,V_signature
_signingHandler
_certificate
_verifyBatteryMatch:
integerForKey:
setAuthFlags:
setDouble:forKey:
setSessionUUIDs:
T@?,C,V_nvmWriteSessionHandler
_challenge
_overrideIdentity
_readDeviceIDSN:
getTouchControllerQueue
init
objectForKey:
signature
bytes
_authSession
_readCertificate:
sharedDefaultsLogging
systemUptime
T@\"NSMutableDictionary\",&,V_sessionUUIDs
certificateInfo
authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:
setProtocolVersion:
sharedDataAccessor
setCertificate:
T@?,C,V_refreshAccessStateHandler
identityCertificates
length
objectAtIndexedSubscript:
openSessionHandler
setComponentIndex:
signRCAMChallenge:completionHandler:
_readSignature:
T@\"NSData\",&,N,V_challenge
T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},N,V_identityKey
_notifyComponentAuthFailure
authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:
authenticateTouchControllerWithChallenge:completionHandler:
dataWithBytes:length:
getBytes:length:
_deviceNonce
moduleAuthService
setCloseSessionHandler:
setInteger:forKey:
_signChallenge:
protocolVersion
_findModuleAuthService:withAuthFlags:componentIndex:
_nvmWriteSessionHandler
array
raise:format:
signTouchControllerChallenge:completionHandler:componentIndex:
authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:
isComponentCertInfo:
nvmWriteSessionHandler
setChallenge:
setIdentityCertificates:
numberWithBool:
TB,N,V_authenticatedSession
_validateWithFDRCertificate:forModuleType:withAuthParams:
_verifyCertificate:
authSession
batteryCode
dictionaryWithObjects:forKeys:count:
setObject:forKey:
TB,N,V_skipComms
_authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:
_findAllModuleAuthServices:
_identityCertificates
v32@0:8@16@?24
I16@0:8
v24@0:8^{mfi4AuthProtocolSession_s=}16
@?16@0:8
@?
v36@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24B32
v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSData\"i>24
B20@0:8I16
@\"NSData\"
^{mfi4AuthProtocolSession_s=}
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}
v40@0:8@16@?24@32
v52@0:8@16@?24B32B36B40@44
v44@0:8@16S24@28@?36
i32@0:8@16^S24
v44@0:8i16@20@28@?36
v20@0:8I16
v44@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24B32B36B40
I36@0:8i16^I20@28
i24@0:8@16
v36@0:8i16i20i24Q28
B
I
i52@0:8^@16i24@28^B36^^{__CFError}44
v44@0:8@16@?24B32@36
v56@0:8@16@?24i32B36B40B44@48
@\"NSMutableDictionary\"
v24@0:8@?16
@16@0:8
v24@0:8@16
v20@0:8B16
v24@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16
i36@0:8@16i24@28
@20@0:8i16
B16@0:8
^{mfi4AuthProtocolSession_s=}16@0:8
B28@0:8@16i24
v36@0:8@16@?24B32
v32@0:8@\"NSData\"16@?<v@?i>24
@\"NSNumber\"
v44@0:8@16@?24B32B36B40
v40@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24@\"NSNumber\"32
v44@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24B32@\"NSNumber\"36
v36@0:8@16S24@?28
v16@0:8
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@0:8
@\"NSDictionary\"
v32@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24
v52@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24B32B36B40@\"NSNumber\"44
v40@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSData\"i>24@\"NSNumber\"32
v48@0:8@16@24@32@?40
```
