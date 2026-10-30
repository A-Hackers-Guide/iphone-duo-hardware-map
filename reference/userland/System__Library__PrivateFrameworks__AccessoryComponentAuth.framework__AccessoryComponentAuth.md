# `/System/Library/PrivateFrameworks/AccessoryComponentAuth.framework/AccessoryComponentAuth`

iOS 27.2 dyld shared cache image. Version `1219.52.1.0.0`. **[DSC]**

## Linked libraries (11)

- `/usr/lib/libFDR.dylib`
- `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication`
- `/System/Library/Frameworks/Security.framework/Security`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics`
- `/usr/lib/libMobileGestalt.dylib`

## Objective-C: 3 classes, 1 protocols, 117 methods, 25 properties

### Class pages

Every class and protocol, with its methods: [`ACCHWComponentAuthService`](../objc/ACCHWComponentAuthService_AccessoryComponentAuth.md), [`ACCHWComponentAuthServiceParams`](../objc/ACCHWComponentAuthServiceParams_AccessoryComponentAuth.md), [`ACCHWComponentAuthServiceProtocol`](../objc/ACCHWComponentAuthServiceProtocol_AccessoryComponentAuth.protocol.md), [`ACCUserDefaults`](../objc/ACCUserDefaults_AccessoryComponentAuth.md)

### Classes

`ACCHWComponentAuthService`, `ACCHWComponentAuthServiceParams`, `ACCUserDefaults`

### Protocols

`ACCHWComponentAuthServiceProtocol`

### Properties

```
@property (T@"NSMutableDictionary",&,V_sessionUUIDs) sessionUUIDs;
@property (TI,N,V_moduleAuthService) moduleAuthService;
@property (TI,N,V_authFlags) authFlags;
@property (T@"NSData",&,N,V_certificateRaw) certificateRaw;
@property (T@"NSData",&,N,V_certificate) certificate;
@property (T@"NSData",&,N,V_signature) signature;
@property (T@"NSData",&,N,V_deviceNonce) deviceNonce;
@property (T@"NSData",&,N,V_challenge) challenge;
@property (T@"NSDictionary",&,N,V_certificateInfo) certificateInfo;
@property (TB,N,V_skipComms) skipComms;
@property (TI,N,V_batteryCode) batteryCode;
@property (TI,N,V_protocolVersion) protocolVersion;
@property (T^{mfi4AuthProtocolSession_s=},V_authSession) authSession;
@property (TB,N,V_overrideIdentity) overrideIdentity;
@property (T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},N,V_identityKey) identityKey;
@property (T@"NSData",&,N,V_identityCertificates) identityCertificates;
@property (TB,N,V_authenticatedSession) authenticatedSession;
@property (T@?,C,V_openSessionHandler) openSessionHandler;
@property (T@?,C,V_closeSessionHandler) closeSessionHandler;
@property (T@?,C,V_nvmWriteSessionHandler) nvmWriteSessionHandler;
@property (T@?,C,V_nvmReadSessionHandler) nvmReadSessionHandler;
@property (T@?,C,V_refreshAccessStateHandler) refreshAccessStateHandler;
@property (T@"NSNumber",&,N,V_componentIndex) componentIndex;
@property (T@?,C,V_completionHandler) completionHandler;
@property (T@?,C,V_signingHandler) signingHandler;
```

## Strings (353)

```
AuthTTRForAllTransports
v28@?0@\"NSData\"8@\"NSData\"16i24
AuthDeviceInfoError
PowerSourceUpdateBehavior
MFi4AuthTimeoutValueS
FDRStatusPass
ReleaseType
EnableIndonesiaInductiveTx
iboot-auth
com.apple.iapd
AllowACCAuthProtocolOnAllTransport
MaxOutboundiAP2PacketSize
pretend_auth
SysdiagnoseInsteadOfAuthTTR
NFCColorOverride
MissingPairedAuthInstanceError
Endpoint
DisableWirelessCTA
BLEPairingIgnoreZeroEarlyInfo
IOTimeoutDeviceBusyError
PearlIDCapability
EnableChinaInductiveTx
GenericMFiIgnoreCertCaps
%02x
AuthTimerExpiredError
NoDeviceIDSNError
cpGetComponentIndex: Got component index : %x\n
DisableSNOnly
BLEPairingDontEarlyInfoAsDeviceUID
PretendBatteryLevel
i
CarPlay Service
AllowNFCColorOverride
UARPActivityTimerS
FDRStatus
FirmwareVersion
NFCSecondaryColorOverride
MFi4RelayReadRetryDelayMs
MPPAuthEnablePretendAuth
EnableManager2ForTransport
<Undefined>
UseCertDataPropertyForAuth
SysdiagnoseOnInductiveCTAFailure
flags
OverrideCanReceiveInductivePowerOID
AuthCPStartDelayMs
LiveVoicemailFakeRinging
TransportSignpost
NoAuthCPServicePresentError
cpCreateFormattedResponseForServerResponse
IdentityCertRefreshInterval
InductiveAuthPretendMatchRxID
MPPAuthChallengeFirst
USBHiAPEnable
com.apple.CoreAccessories.PreferencesDidChangeNotification
VerifyNonceSignatureError
Beta
cpSetActualPairedCertSN: !CFStringGetCString
bcrt
wcrt
AuthSuccess
CreateCertificateSerialNumberError
VerifyModuleFDRError
PretendAuthFailure
PretendWirelessCTAMatch
com.apple.CoreAccessories
DisableAACPAuth
WaitForiAPTrafficDelayMS
com.apple.accessories.authCPEvent
Uptime
CreateRandomNonceError
com.apple.accessories.signposts
ShowHiddenAccessories
DisableMFi4CertSupport
DeviceID
cpSetAuthError %d\n
com.apple.accessoryd
SkipNFCAuth
v36@?0B8@\"NSData\"12@\"NSData\"20B28i32
tcrt
Connection
AccessoryCertificate
DisableAMSHookUp
DisableInductiveAuthTTR
EnableACCAuthProtocolOnNFC
ForceMFi4AuthOverNFC
Use +[%@ %@] instead of -%@.
CertificateAuthVersionNumberError
RejectionOfMultipleLocation
PacketLoggingPlainTextOnly
MFi4ECDSAOnly
OverrideMPPAuthSupported
ChargingPowerOverride
Battery
Bluetooth Service
RCAM
DeviceNonce
PretendNFCAuthFailed
wiredAuthDuration
Transport Plugins
ComponentIndex
BypassTrustDialog
DisableCertSupport
IdentityCertIsClassD
IgnoreIsOnAC
DisableACCAuthProtocolOnInductive
Signature
App Links
AuthMinorVersion
DisableAuthTimeoutTTRForXR
BLEPairingAuthTimeoutValueS
authState
Passed
HW Component Auth
cpCreateSignatureWithIndexAndToken
IdentityCertRefreshState
General
IOAccessory
AuthPassed
IgnorePowerSourceUpdateForAvailableCurrent
cpSetExpectedPairedCertSN: !CFStringGetCString
DisableCertVerification
DontSkipInductiveAuthOnCTA
DisableNFCAuthTimer
InternalModuleCapabilityMismatchError
AuthBatteryMismatchOnProdDevice
IgnoreAACPAuthStatus
com.apple.logging
TreatAuthCPDEVNAsV3
MFi4ECDSADisallow
com.apple.ACCHWComponentAuthService.veridian
SkipGaugeSignatureCheck
IgnoreAuthReset
-[ACCHWComponentAuthService _validateWithFDRCertificate:forModuleType:withAuthParams:]
Failed
IdentityCertUseIndex
ACCAuthProtocolRoleSupport
AuthMajorVersion
authError
vcrt
InternalComponent
ComponentName
cpGetComponentIndex: Component index not SInt32
DisableT56Support
com.apple.ACCHWComponentAuthService.rcam
-
IORegistryEntryID
isTrusted
DisablePowerUpdateForCurrentDraw
CopyAllowUnsealed
BadArgumentError
IDSN
PretendNFCAuthTimeout
Veridian
LAS
com.apple.accessories.hwComponent.isTrusted.failure
TimeSync
cpGetChallengeSignatureLengths
DisableIAPHVCFixForAuth
AudioAccessory
EnableWrongOrientationMessage
IgnoreAccInfoUpdateRelaySupport
+[ACCHWComponentAuthService _verifyModuleFDR:forModuleType:]
EnableDEVNCertSupport
VerifyCertificateSerialNumberError
FDRStatusUnknown
KnownAccessories
EnableTrustDialog
PretendNoNFCResponse
com.apple.iapd.PreferencesDidChangeNotification
TouchController
com.apple.ACCHWComponentAuthService.touchcontroller
ConnectionInfo
v12@?0i8
CreateSignatureError
wapi
isTrustedForUI
v8@?0
com.apple.ACCHWComponentAuthService.battery
NoAuthICPresentError
RegionCode
ACCAuthProtocolAllowMutualAuth
com.apple.accessories.frameworks.core-accessories
ChargingPowerBehavior
isPeriodic
TestCreateBLEPairingOnInductive
DisableAuthFailureTTRForXR
ForceAuthTimeout
MPPAuthPreferredSlot
isInductive
AppleAuthCP
no
FullCertData
ForceAuthFail
BLEPairingDisableOOBPPlusFlow
BLEPairingConfigRequestDelayMs
FDRStatusFail
AllowMFi4DevCertsOnProdDevice
yes
SigningFuse
IdentityCertUseTime
ForceT56RelaySupport
MFi4SigmaIRequired
MismatchedPairingError
UninitializedAuthError
ForceAccInfoUpdateRelaySupport
authErrorDescription
internalModuleType
ProductType
prpc
CertSerialNumberError
CanChargeInductiveError
DeviceClass
PretendAccessoryType
isBatteryModule
Transport Client
AccessoryCertificateSerialNumber
cpGetTransportEntryId: IOConnectCallScalarMethod failed: 0x%x\n
NFCAnalyticsDate
DeviceIdentityPreArmDateOverride
Disable1WayNFCForInductive
CreateSerialNumberStringFromDataError
cpGetComponentIndex: Failed to find ComponentIndex property
ACCAuthProtocolPretendAuth
XpcConnectionError
Transport
com.apple.ACCHWComponentAuthService.las
Challenge
NullCertificateDataError
InternalBuild
KeepAACPAuthData
ACCAuthProtocolMaxMessageSize
MPPAuthGetLeafCertFirst
LeafCertData
SerialNumberPairingError
EnableAuthTimeoutTTR
PretendNoDeviceIdentityCerts
AuthenticationOverride
AuthBatteryMismatchOnDevDevice
ComponentBusyError
PlatformIDOverride
6)
SerialNumberCompareError
CreateCapsFromAuthCertError
ProductVersion
VerifyPublicCertificateError
External Accessory
DeviceVersion
cpCreateFormattedChallengeFromServerRequest
cpGetComponentIndex: Component index not CFNumber
(moduleType=%d) No authIC cert to compare against FDR
authError %d after _signChallenge
verifyBatteryMatch Replying with authError = %d
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
challenging Veridian using data %@
(moduleType=%d) %d: %ld.%03llu
(moduleType=%d) Error: The component AppleAuthCP was not found, [servicesArray count] is 0
(moduleType=%d) Error: signature==NULL
error generating signature: %s\n
IDSN length %zu exceeds buffer
(moduleType=%d) updateRegistry: cpSetAuthStatus, cpSetTrustStatus
Returning Roswell data of length %ld
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
Could not cpGetDeviceIDSN: %s\n
_verifyBatteryMatch %d: %ld.%03llu
no error after _signChallenge!
acc_internalSettings: internal-only setting %{public}@ active
error getting MFAACertificateManager
AMFDRSealingMapCopyLocalDataForClass returned error = %@
Notifying clients of %s
ERROR No auth io_service_t is found!
auth length = %ld, sizeof(t_bpFDRData_v1) = %lu, does not match
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
(moduleType=%d) skip component auth
(moduleType=%d) tryCount = %d (max tries %d)
Flags indicate battery...do not call cpCopyCertificate()
Flags indicate rcam...do not call cpCopyCertificate()
error parsing certificate
Have a custom Roswell data structure
pRoswellDataStructure->roswell_cert_len = %d
Failed to create os_log_t object %s: %s!
received response. signature=%@, deviceNonce=%@, authError=%d
received response. response=%@, authError=%d
(moduleType=%d) index:%@
(moduleType=%d) Error: challenge==NULL
(moduleType=%d) authError %d after _readCertificate
AMFDRSealingMapCopyMultiInstanceForClass returned error: %@
Created log object %s: %s
Created %d log object(s)!
(moduleType=%d) Failed to fetch component index: %s\n
error getting certificate
signature = %@
(moduleType=%d) cpSetAuthStatus failed: 0x%x
acc_internalSettings: internal-only setting %{public}@ active (%ld)
ACASignTouchControllerChallengeWithIndex
CoreAnalytics event: %@\neventDict: %@
(moduleType=%d) cpSetTrustStatus failed: 0x%x
Could not cpGetDeviceInfo: %s\n
(moduleType=%d) Cannot find FDR cert
_signChallengeForModuleType Replying with signature=%@, deviceNonce=%@, authError = %d
(moduleType=%d) authError = %d after verifyModuleCertificate
(moduleType=%d) authError = eAuthDeviceInfoError after _verifyDeviceInfo
error generating signature: auth cp error code %#x\n
signatureValid ? %@
(moduleType=%d) %s: cpGetDeviceIDSN failed: ret=%x len=%zu
Failed to retrieve device IDSN
(moduleType=%d) cpSetTrustStatusForUI failed: 0x%x
(moduleType=%d) cpSetAuthError failed: 0x%x
received response. authError=%d
(moduleType=%d) authError = eNoDeviceIDSNError after _readDeviceIDSN
moduleAuthService = %d
Sleeping for %d seconds before retrying auth
no error after _verifyBatteryMatch!
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
_readSignature %d: %ld.%03llu
could not open service: %s\n
ACAInitForHIDWithIndex
(moduleType=%d) Error: The component AppleAuthCP was not found, servicesArray is NULL
(moduleType=%d) moduleAuthService = %d
(moduleType=%d) sleeping for %d seconds before retrying auth
(moduleType=%d) cpSetBatteryCode failed: 0x%x
(moduleType=%d) Could not find authcp services: %s\n
(moduleType=%d) done
(moduleType=%d) authError %d after _readSignature
(moduleType=%d) updateRegistry
(moduleType=%d) Replying with authPassed = %d, fdrValid = %d, authError = %d
(moduleType=%d) Found %lu matching service(s)
error verifying serial number
cpClearCertificate failed: 0x%x
certificate = %@
(moduleType=%d) Replying with overallAuthPassed = %d, overallFdrValid = %d, authError = %d
(moduleType=%d) Error: The component AppleAuthCP was not found
(moduleType=%d) Error: Could not evaluate certificate
(moduleType=%d) %s: %d: returned error
(moduleType=%d) equal:%d
tryCount = %d (max tries %d)
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
verifying battery match using cert %@
(moduleType=%d) authError %d after _signChallenge
(moduleType=%d) authError %d after _verifyCertificate
(moduleType=%d) authError %d after _verifySignature
(moduleType=%d) %s: AMFDRSealingMapCopyLocalDataForClass: returned NULL
(moduleType=%d) Error: Could not parse certificate
Have a match for (t_bpFDRData_v1)
dataLength matches Roswell data length, return copy of fdr data
Flags indicate Veridian...do not call cpCopyCertificate()
error evaluating certificate
_verifySignature %d: %ld.%03llu
device nonce = %@
(moduleType=%d) %s: AMFDRSealingMapCopyLocalDataForClass returned error=%@
authError %d after _verifyBatteryMatch
(moduleType=%d) Error: The component AppleAuthCP was not found, unexpected NULL service
(moduleType=%d) authCP service %d tmpAuthFlags == 0x%x
```
