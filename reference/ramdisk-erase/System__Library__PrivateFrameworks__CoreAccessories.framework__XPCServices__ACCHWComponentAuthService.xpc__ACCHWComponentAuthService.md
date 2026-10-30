# `/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCHWComponentAuthService.xpc/ACCHWComponentAuthService`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 839,792 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 28 (Size: 3944)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (11)

- `/usr/lib/libFDR.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.driver.AppleAuthCP.i2c.user-access</key>
	<true/>
	<key>com.apple.driver.AppleAuthCP.user-access</key>
	<true/>
	<key>com.apple.keystore.class.wku</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.mobileactivationd.device-identifiers</key>
	<true/>
	<key>com.apple.mobileactivationd.spi</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>UniqueChipID</string>
		<string>BootManifestHash</string>
		<string>RoswellChipID</string>
		<string>BatterySerialNumber</string>
		<string>SerialNumber</string>
		<string>UniqueDeviceID</string>
		<string>UniqueDeviceIDData</string>
		<string>ScreenSerialNumber</string>
		<string>TopModuleAuthChipID</string>
	</array>
	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
	<true/>
	<key>com.apple.security.attestation.access</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.mobileactivationd</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleAuthCPUserClient</string>
	</array>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.mfiaccessory</string>
	</array>
</dict>
</plist>
```

## Objective-C (4 classes, 3 protocols)

Classes: `ACCHWComponentAuthService`, `ACCHWComponentAuthServiceParams`, `ACCUserDefaults`, `ServiceDelegate`

Protocols: `ACCHWComponentAuthServiceProtocol`, `NSObject`, `NSXPCListenerDelegate`

## Strings (1,289)

```
NSXPCListenerDelegate
NSObject
ACCUserDefaults
ACCHWComponentAuthServiceParams
ACCHWComponentAuthService
ACCHWComponentAuthServiceProtocol
ServiceDelegate
T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},N,V_identityKey
setSkipComms:
boolValue
authenticateRCAMWithChallenge:completionHandler:updateRegistry:
T@?,C,V_closeSessionHandler
setIdentityKey:
_authSession
_challenge
_identityCertificates
authSession
count
arrayWithArray:
boolForKey:
isMemberOfClass:
setObject:forKey:
_deviceNonce
date
dictionaryWithDictionary:
nvmWriteSessionHandler
openSessionHandler
setRefreshAccessStateHandler:
T@?,C,V_nvmReadSessionHandler
signVeridianChallenge:completionHandler:
signVeridianChallenge:completionHandler:componentIndex:
_moduleAuthService
copyEvaluatedCertificateChainInfo:
interfaceWithProtocol:
_findFDRCertData:forModuleType:withAuthParams:hasDeviceCert:withError:
_validateWithFDRCertificate:forModuleType:withAuthParams:
class
signTouchControllerChallenge:completionHandler:componentIndex:
_openSessionHandler
copy
setDeviceNonce:
T@\"NSData\",&,N,V_deviceNonce
displayAuthUserNVMRead:key:completionHandler:
setInteger:forKey:
sharedDefaults
verifyNonceSignature:nonce:signature:
_logToAnalytics:authError:fdrValidationStatus:authDurationInMS:
_certificate
_verifyDeviceInfo:
authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:
completionHandler
identityKey
setCompletionHandler:
_verifyModuleFDR:forModuleType:
_skipComms
_refreshAccessStateHandler
integerForKey:
isKindOfClass:
nvmReadSessionHandler
authenticateVeridianWithChallenge:completionHandler:
numberWithUnsignedInt:
stringWithUTF8String:
authenticateVeridianWithChallenge:completionHandler:componentIndex:
challenge
displayAuthOpenSession:intermediateCertificate:keyData:completionHandler:
doubleForKey:
hash
objectForKey:
array
setObject:forKeyedSubscript:
setSigningHandler:
serviceListener
TI,N,V_batteryCode
_signingHandler
componentIndex
displayAuthCloseSession:completionHandler:
verifyModuleCertificate:forModule:forAuthFlags:
authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:
.cxx_destruct
TB,N,V_overrideIdentity
_authenticatedSession
setIdentityCertificates:
zone
T@?,C,V_nvmWriteSessionHandler
TB,N,V_skipComms
authenticateLASWithChallenge:completionHandler:updateRegistry:
signRCAMChallenge:completionHandler:componentIndex:
closeSessionHandler
dictionaryWithCapacity:
setChallenge:
isProxy
TQ,R
_nvmWriteSessionHandler
isEqualToNumber:
timeIntervalSince1970
T@?,C,V_signingHandler
_sessionUUIDs
sharedManager
unsignedIntegerValue
_verifyBatteryMatch:outputBatteryCode:
authenticateBatteryWithChallenge:completionHandler:componentIndex:
authenticatedSession
batteryCode
displayAuthUserNVMWrite:key:value:completionHandler:
listener:shouldAcceptNewConnection:
setExportedObject:
sharedDefaultsIapd
_identityKey
_notifyComponentAuthFailure
isEqualToString:
retain
T@\"NSNumber\",&,N,V_componentIndex
protocolVersion
addEntriesFromDictionary:
certificateRaw
initWithSuiteName:
isComponentCertInfo:
sharedDefaultsLogging
allKeys
_nvmReadSessionHandler
init
sharedDataAccessor
T@\"NSString\",R,C
setModuleAuthService:
T@\"NSDictionary\",&,N,V_certificateInfo
errorWithDomain:code:userInfo:
setExportedInterface:
_certificateInfo
sessionUUIDs
verifyModuleCertificate:forModule:forAuthFlags:forIndex:
T@?,C,V_completionHandler
createVeridianNonce:withChallenge:
getTouchControllerQueue
setAuthFlags:
identityCertificates
self
signingHandler
T@\"NSData\",&,N,V_certificateRaw
T#,R
authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:
dataWithContentsOfFile:
getBytes:length:
authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:componentIndex:
T@\"NSData\",&,N,V_challenge
TB,N,V_authenticatedSession
_signChallengeForModuleType:challenge:componentIndex:completionHandler:
charValue
setSessionUUIDs:
setAuthSession:
TI,N,V_moduleAuthService
certificate
setOverrideIdentity:
_overrideIdentity
processInfo
unsignedShortValue
authFlags
copyParsedCertificateChainInfoFromCerts:assumeType:
countByEnumeratingWithState:objects:count:
systemUptime
_findAllModuleAuthServices:
autorelease
copyPathForPersonalizedData:error:
description
setAuthenticatedSession:
_readSignature:
arrayForKey:
dataWithBytes:length:
signature
T@\"NSData\",&,N,V_certificate
release
conformsToProtocol:
dictionaryWithObjects:forKeys:count:
setDouble:forKey:
T@\"NSString\",?,R,C
displayAuthRefreshAccessState:completionHandler:
_componentIndex
setBatteryCode:
T@\"NSMutableDictionary\",&,V_sessionUUIDs
certificateInfo
_validateDeviceAndFDRCert:forModuleType:withAuthParams:
_verifyBatteryMatch:
respondsToSelector:
signRCAMChallenge:completionHandler:
authenticateTouchControllerWithChallenge:completionHandler:
bytes
numberWithDouble:
refreshAccessStateHandler
stringForKey:
_readDeviceIDSN:
_verifySignature:
objectAtIndexedSubscript:
superclass
TI,N,V_protocolVersion
_batteryCode
setCloseSessionHandler:
numberWithBool:
TI,N,V_authFlags
_authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:
numberWithUnsignedLongLong:
setDelegate:
T@?,C,V_refreshAccessStateHandler
setCertificate:
_closeSessionHandler
retainCount
setNvmWriteSessionHandler:
setOpenSessionHandler:
T^{mfi4AuthProtocolSession_s=},V_authSession
verifyBatteryMatch:completionHandler:
setComponentIndex:
T@\"NSData\",&,N,V_signature
_findModuleAuthService:withAuthFlags:componentIndex:
_protocolVersion
resume
T@?,C,V_openSessionHandler
arrayWithCapacity:
dictionaryForKey:
isEqual:
performSelector:withObject:withObject:
_signature
debugDescription
skipComms
authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:
setCertificateRaw:
stringWithFormat:
T@\"NSData\",&,N,V_identityCertificates
_certificateRaw
_signChallenge:
performSelector:
_readCertificate:
_verifyCertificate:
authenticateBatteryWithChallenge:completionHandler:
authenticateLASWithChallenge:completionHandler:updateRegistry:componentIndex:
deviceNonce
isEqualToData:
setProtocolVersion:
_completionHandler
numberWithUnsignedShort:
overrideIdentity
performSelector:withObject:
setCertificateInfo:
copyParsedCertificateChainInfo:
isMFi2_3CertInfo:
moduleAuthService
unsignedIntValue
_authFlags
raise:format:
dealloc
addObject:
createVillanovaNonce:IDSN:challenge:
setSignature:
length
setNvmReadSessionHandler:
B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24
v24@0:8@16
v24@0:8@?16
v48@0:8@16@24@32@?40
v52@0:8@16@?24B32B36B40@44
v32@0:8@\"NSData\"16@?<v@?i>24
B32@0:8@16@24
Vv16@0:8
I16@0:8
v24@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16
B28@0:8@16i24
i36@0:8@16i24@28
v56@0:8@16@?24i32B36B40B44@48
v36@0:8i16i20i24Q28
v44@0:8@16S24@28@?36
I36@0:8i16^I20@28
v20@0:8B16
^{mfi4AuthProtocolSession_s=}16@0:8
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@0:8
v36@0:8@16S24@?28
@40@0:8:16@24@32
@?16@0:8
@\"NSDictionary\"
@\"NSNumber\"
v36@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24B32
@32@0:8:16@24
v44@0:8i16@20@28@?36
v40@0:8@16@?24@32
#16@0:8
v20@0:8I16
@\"NSData\"
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}
B20@0:8I16
v40@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24@\"NSNumber\"32
v44@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24B32@\"NSNumber\"36
v40@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSData\"i>24@\"NSNumber\"32
@20@0:8i16
v36@0:8@16@?24B32
v44@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24B32B36B40
B24@0:8#16
@?
Q16@0:8
v44@0:8@16@?24B32@36
^{mfi4AuthProtocolSession_s=}
v32@0:8@16@?24
@16@0:8
B16@0:8
^{_NSZone=}16@0:8
B24@0:8@\"Protocol\"16
v16@0:8
B
@\"NSMutableDictionary\"
v24@0:8^{mfi4AuthProtocolSession_s=}16
I
i52@0:8^@16i24@28^B36^^{__CFError}44
i24@0:8@16
i32@0:8@16^S24
v44@0:8@16@?24B32B36B40
v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSData\"i>24
B24@0:8@16
B24@0:8:16
@\"NSString\"16@0:8
v32@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24
v52@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24B32B36B40@\"NSNumber\"44
@24@0:8:16
UninitializedAuthError
com.apple.accessories.signposts
BLEPairingAuthTimeoutValueS
IgnoreAccInfoUpdateRelaySupport
_convertUserNVMWrite
_mfi4Auth_relay_handle_AccessoryInformationUpdate
%y%m%d%H%M%SZ
AudioAccessory
ForceMFi4AuthOverNFC
LAS
AuthBatteryMismatchOnProdDevice
mfi4Auth_protocol_handle_NVMPublicKeyChallenge
_replyGetNVMKey
cpSetActualPairedCertSN: !CFStringGetCString
FirmwareVersionPending
SkipGaugeSignatureCheck
MFi4SigmaIRequired
yes
CCSIGMA_MFI_SI_KEY
SkipNFCAuth
CopyAllowUnsealed
MissingPairedAuthInstanceError
mfi4Auth_protocol_initMessage_RequestNVMPublicKeyChallenge
CCSIGMA_MFI_CR_IV
_convertNVMReadResponse
EnableAuthTimeoutTTR
AuthTimerExpiredError
mfi4Auth_relay_StartRelayForType
Beta
SysdiagnoseOnInductiveCTAFailure
VerifyPublicCertificateError
InternalModuleCapabilityMismatchError
iAP2MsgGetNextParamWithError
CCSIGMA_MFI_CI_KEY
AccessoryCertificate
cpCreateSignatureWithIndexAndToken
SerialNumber
com.apple.accessories.authCPEvent
BadArgumentError
DisableAMSHookUp
ForceAccInfoUpdateRelaySupport
LiveVoicemailFakeRinging
TransportSignpost
com.apple.CoreAccessories.PreferencesDidChangeNotification
FDRStatus
mfi4Auth_protocol_parse_NVMWriteResponse_v3
mfi4Auth_protocol_initMessage_RequestUserNVMWrite
EnableACCAuthProtocolOnNFC
CreateSerialNumberStringFromDataError
MFi40Attestation-Certificate
Veridian
Signature
CCSIGMA_MFI_SR_KEY
TreatAuthCPDEVNAsV3
DisableAuthTimeoutTTRForXR
PowerSourceUpdateBehavior
GenericMFiIgnoreCertCaps
com.apple.ACCHWComponentAuthService.rcam
prpc
MFi40Attestation-Intermediate
DisableCertVerification
6)
CCSIGMA_MFI_SI_IV
com.apple.mfi4Auth.protocol
wapi
IgnorePowerSourceUpdateForAvailableCurrent
AllowACCAuthProtocolOnAllTransport
AuthSuccess
BLEPairingDontEarlyInfoAsDeviceUID
FullCertData
CCSIGMA_MFI_CR_KEY
ucrt
AccessoryDeviceUID
AccessoryPlatformID
DeviceIdentityPreArmDateOverride
IdentityCertRefreshInterval
AuthCPStartDelayMs
IOTimeoutDeviceBusyError
mfi4Auth_protocol_handleAuthSessionClose
Savage - Factory
PPID
DisableNFCAuthTimer
mfi4Auth_protocol_requestNvmErasePublicKey
OverrideCanReceiveInductivePowerOID
DisableMFi4CertSupport
CreateRandomNonceError
com.apple.accessoryd.mfi4.userPublicKey.%@
ACCAuthProtocolPretendAuth
IgnoreAACPAuthStatus
EnableChinaInductiveTx
com.apple.ACCHWComponentAuthService.touchcontroller
iAP2MsgForEachParamDo
mfi4Auth_protocol_handle_NVMAuthFinish
PlatformIDOverride
TestCreateBLEPairingOnInductive
com.apple.mfi4Auth.encrypt
0x%02x, 
DeviceNonce
KeepAACPAuthData
EnableManager2ForTransport
wiredAuthDuration
cpGetComponentIndex: Failed to find ComponentIndex property
Yonkers - Factory
Transport Client
ShowHiddenAccessories
DisableInductiveAuthTTR
EnableIndonesiaInductiveTx
com.apple.ACCHWComponentAuthService.las
authError
LeafCertData
MFi40Accessory-Intermediate
General
DisableCertSupport
CCSIGMA_MFI_ER_KEY
CCSIGMA_MFI_EI_KEY
com.apple.mfi4Auth.decrypt
DeviceVersion
cpGetComponentIndex: Component index not CFNumber
TimeSync
IdentityCertUseIndex
PretendAccessoryType
PretendAuthFailure
mfi4Auth_protocol_handle_NVMOperationResponse
com.apple.mfi4Auth.send
Repair UCRT
%Y%m%d%H%M%SZ
External Accessory
AuthDeviceInfoError
IORegistryEntryID
cpGetComponentIndex: Component index not SInt32
ProductType
ConnectionInfo
ACCAuthProtocolRoleSupport
FirmwareVersionActive
HW Component Auth
Endpoint
EnableDEVNCertSupport
PretendBatteryLevel
com.apple.ACCHWComponentAuthService.veridian
CanChargeInductiveError
%d
VerifyModuleFDRError
DeviceCompatibility
Connection
DisableT56Support
ChargingPowerOverride
ChargingPowerBehavior
mfi4Auth_protocol_initMessage_RequestNVMOperation
_convertUserVendorNVMRead
EnableWrongOrientationMessage
DisablePowerUpdateForCurrentDraw
authState
authErrorDescription
CCSIGMA_MFI_CI_IV
MFi4Auth
mfi4Auth_protocol_handle_AuthCert
ComponentIndex
SerialNumberCompareError
DisableSNOnly
PretendNFCAuthFailed
RCAM
no
wcrt
CCSIGMA_MFI_TR_KEY
AccessoryCertificateSerialNumber
isInductive
FDRStatusFail
mfi4Auth_protocol_cleanupSessionCommon
isTrusted
cpCreateFormattedChallengeFromServerRequest
DeviceClass
AllowMFi4DevCertsOnProdDevice
PretendNFCAuthTimeout
Disable1WayNFCForInductive
MPPAuthPreferredSlot
isBatteryModule
Passed
NoAuthCPServicePresentError
TouchController
VerifyCertificateSerialNumberError
mfi4Auth_protocol_initMessage_RequestNVMWritePublicKey
CCSIGMA_MFI_TI_KEY
AuthPassed
MFi4ECDSADisallow
IgnoreAuthReset
IDSN
RegionCode
com.apple.accessories.frameworks.core-accessories
com.apple.logging
SysdiagnoseInsteadOfAuthTTR
IdentityCertRefreshState
MPPAuthGetLeafCertFirst
WaitForiAPTrafficDelayMS
CertificateAuthVersionNumberError
ProductID
VerifyNonceSignatureError
NoAuthICPresentError
mfi4Auth_protocol_handle_NVMWriteResponse
mfi4Auth_protocol_initMessage_RequestManufacturerNVMRead
CCSIGMA_MFI_ER_IV
_convertNVMEraseResponse
InternalBuild
KnownAccessories
DisableAuthFailureTTRForXR
nil
Bluetooth Service
AuthTTRForAllTransports
NFCAnalyticsDate
pretend_auth
tcrt
mfi4Auth_protocol_initMessage_RequestNVMAuthStart
_getCachedUserPublicKey
mfi4Auth_protocol_messageHandler_receiveIncomingData
EnableTrustDialog
NFCColorOverride
ACCAuthProtocolMaxMessageSize
Failed
CreateCapsFromAuthCertError
AuthBatteryMismatchOnDevDevice
mfi4Auth_protocol_parse_NVMWriteResponse_v2
mfi4Auth_protocol_convertUserAccessoryInfoToAction
v8@?0
PearlIDCapability
Name
AllowNFCColorOverride
com.apple.iapd.PreferencesDidChangeNotification
mfi4Auth_protocol_handle_NVMReadResponse
FirmwareVersion
ComponentName
BypassTrustDialog
USBHiAPEnable
CreateCertificateSerialNumberError
mfi4Auth_protocol_messageHandler_sendOutgoingData
mfi4Auth_protocol_messageHandler_handleOutgoingSecureTunnelDataForClient
MFi40Accessory-Certificate
RefreshInterval
cpGetTransportEntryId: IOConnectCallScalarMethod failed: 0x%x\n
i
isTrustedForUI
ProductVersion
DisableAACPAuth
com.apple.ACCHWComponentAuthService.battery
_consumeByteInternal
mfi4Auth_protocol_initSigmaContextNvm
DeviceID
InductiveAuthPretendMatchRxID
IOAccessory
ForceAuthTimeout
PacketLoggingPlainTextOnly
IdentityCertUseTime
BLEPairingIgnoreZeroEarlyInfo
mfi4Auth_protocol_initMessage_RequestNVMAuthFinish
InternalComponent
MPPAuthEnablePretendAuth
+[ACCHWComponentAuthService _verifyModuleFDR:forModuleType:]
bcrt
CreateSignatureError
ComponentBusyError
<Undefined>
_convertUserNVMErase
mfi4Auth_protocol_handle_RequestAuthCert
Count
cpCreateFormattedResponseForServerResponse
2006-05-31
Transport Plugins
com.apple.accessoryd
Battery
%02x
-
com.apple.mfi4Auth.receive
cpSetAuthError %d\n
ReleaseType
Manufacturer
isPeriodic
flags
mfi4Auth_protocol_handle_NVMEraseResponse
mfi4Auth_protocol_parse
cpGetChallengeSignatureLengths
OverrideMPPAuthSupported
NullCertificateDataError
MFi4AuthTimeoutValueS
mfi4Auth_protocol_initMessage_RequestUserNVMErase
AuthMinorVersion
UARPActivityTimerS
MFi4RelayReadRetryDelayMs
CCSIGMA_MFI_SR_IV
mfi4Auth_protocol_validateCertChain
cpSetExpectedPairedCertSN: !CFStringGetCString
DisableIAPHVCFixForAuth
PretendWirelessCTAMatch
DontSkipInductiveAuthOnCTA
PretendNoNFCResponse
MaxOutboundiAP2PacketSize
vcrt
SigningFuse
NoDeviceIDSNError
PPIDVersionUID
BLEPairingConfigRequestDelayMs
AuthenticationOverride
MismatchedPairingError
mfi4Auth_protocol_handle_NVMAuthStart
CarPlay Service
Transport
MFi4ECDSAOnly
-[ACCHWComponentAuthService _validateWithFDRCertificate:forModuleType:withAuthParams:]
FDRStatusUnknown
mfi4Auth_protocol_initMessage_RequestNVMErasePublicKey
_handleNvmReadUserPublicKey
com.apple.mfi4Auth.process
com.apple.CoreAccessories
Use +[%@ %@] instead of -%@.
v36@?0B8@\"NSData\"12@\"NSData\"20B28i32
com.apple.accessories.hwComponent.isTrusted.failure
CCSIGMA_MFI_EI_IV
mfi4Auth_relay_initMessage_DeviceiAP2RelayRemote_RequestAccessoryInfoUpdate
cpGetComponentIndex: Got component index : %x\n
SerialNumberPairingError
DisableWirelessCTA
internalModuleType
Uptime
FDRStatusPass
com.apple.accessories.connection.passedMFi4Auth
ACCAuthProtocolAllowMutualAuth
mfi4Auth_protocol_initMessage_RequestVendorNVMRead
%F
HardwareVersion
IdentityCertIsClassD
DisableACCAuthProtocolOnInductive
RejectionOfMultipleLocation
mfi4Auth_protocol_parse_NVMReadResponse
MFi30Accessory-Certificate
AuthMajorVersion
CertSerialNumberError
ForceAuthFail
ForceT56RelaySupport
Challenge
Model
App Links
com.apple.iapd
BLEPairingDisableOOBPPlusFlow
VendorID
NFCSecondaryColorOverride
__createCertificateRefWithData
UseCertDataPropertyForAuth
IgnoreIsOnAC
PretendNoDeviceIdentityCerts
MPPAuthChallengeFirst
iboot-auth
AppleAuthCP
XpcConnectionError
(moduleType=%d) updateRegistry
(moduleType=%d) Could not find authcp services: %s\n
mfi4Auth_protocol_handle_NVMReadResponse: Nonce
handle_NVMPublicKeyChallenge: BeginUserKeyErase: !authNonceRef
_handleNvmReadUserPublicKey: !nvmUserPublicKey
RequestRefreshAccessState: authSession shutting down
AuthState: authSession shuttingDown
iAP2RelayFailed: !inMessage
(moduleType=%d) %s: cpGetDeviceIDSN failed: ret=%x len=%zu
handle_NVMOperationResponse: decryptPayload: error
mfi4Auth_protocol_handle_AuthCert: memcmp error
%s: ForceAuthTimeout/PretendNFCAuthTimeout!!!, ignore status(%d)
AuthStart: !outMessage
processIncomingMessageExtra: authSession shuttingDown
handle_AuthSetup: cert chain type fail
mfi4Auth_protocol_validateSignature: SecKeyCopyExternalRepresentation error: %@
mfi4Auth_relay_handle_iAP2RelayRemote: invalid packageDataType!!!
Created log object %s: %s
signatureValid ? %@
parseNVMReadResponse: paramID: %d, subparam: %d
NVMPublicKeyChallenge: WriteUserKey: initMessage_RequestNVMWritePublicKey error
mfi4Auth_protocol_handle_AuthCert: compressedLength %d, decompressedLength %zu
mfi4Auth_protocol_processIncomingMessageExtra: error: %d
validateCertChain: parse failed
%s: string parameter not NUL terminated! (paramID %d)
handle_NVMEraseResponse: paramID %d exceeds maximum expected value
handleNVMWriteResponse: keys not written
handle_NVMAuthFinish: Action_WriteUserName
(moduleType=%d) cpSetAuthError failed: 0x%x
NVMReadResponse: paramID %d exceeds maximum expected value
handleNVMWriteResponse: error
handle_NVMPublicKeyChallenge: BeginUserKeyErase: !isProgrammed
handle_NVMAuthFinish: ccsigma_open
_extractPublicKey: keyDataLength:%ld
userNVMWrite: !authSession
handle_AuthSetup: sessionNonce fail
acc_internalSettings: internal-only setting %{public}@ active (%ld)
Have a custom Roswell data structure
error evaluating certificate
%s: authSession shuttingDown
%s: !keepOpen
encryptOutgoingData: !inMessage
handle_AuthSetup: initMessage_RequestAuthStart error
RefreshAccessStateResponse: error:%d
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
(moduleType=%d) %d: %ld.%03llu
decryptIncomingData: !inMessage
mfi4Auth_protocol_handle_AuthCert: certType:%d
mfi4Auth_protocol_handle_AuthCert: iAP2MsgGetDataAsArrayU8 error
AuthenticationFailed: !outMessage
mfi4Auth_protocol_processIncomingMessage: success
%s: %d
handle_NVMEraseResponse: AuthNonce length: %d
mfi4Auth_protocol_initSigmaContext: authSession->authStatus:%x devIdentityAllowed:%d
parseNVMReadResponse: AuthNonce: count
initSigmaContextNvm: ccsigma_export_key_share: error
_replyGetNVMKey: !dictionary
PairedToCurrentUser
failed to handle auth success
decryptIncomingData: !authSession
initSigmaContext: cert_hash_resp: %@
handle_AuthSetup: auth type fail
failed to handle auth challenge response
iAP2RelayRemote: authSession shutting down
AMFDRSealingMapCopyLocalDataForClass returned error = %@
\n
mfi4Auth_protocol_validateSignature: !leafCert
_readSignature %d: %ld.%03llu
handleNVMWriteResponse: received Nonce
handle_NVMOperationResponse: Found no message starting with: %x
AuthStart: !authSession
tag: %@
(moduleType=%d) authCP service %d tmpAuthFlags == 0x%x
handle_NVMPublicKeyChallenge: kMfi4Auth_Action_WriteUserKey
handle_NVMAuthFinish: ccsigma_import_peer_verification_key
seckey_sign: challenge: %@\n
handle_AuthSetup: !authSession
AuthenticationReset: !inMessage
processIncomingMessageExtra: !authSession
processIncomingMessageExtra: !inMessage
Returning Roswell data of length %ld
cfError: 0x%ld
Received unhandled message with ID: 0x%04x
initSigmaContext: ccsigma_set_signing_function
mfi4Auth_protocol_validateSignature: __createCertificateRefWithBytes error
mfi4Auth_protocol_validateSignature: ccsigma_verify error
processIncomingMessageRelay: initMessage RequestAccessoryInfoUpdate
(moduleType=%d) authError = eAuthDeviceInfoError after _verifyDeviceInfo
handle_NVMPublicKeyChallenge: kMfi4Auth_Action_EraseUserKey
handle_AuthSetup: cert chain type %d
processIncomingMessage: !authSession
vendor nameString %@
RequestAuthCert: authSession shutting down
AuthFinish: authSession shutting down
AuthenticationReset: !outMessage
processIncomingMessage: !inMessage
received OperationFailed
decryptPayload: key_index: %zu
failed to handle relay success
mfi4Auth_util_unpackFromTunnelDataiAP2Msg: message 0x%04X, type %d, unpackedMessage %ld bytes
mfi4Auth_protocol_handle_AuthCert: SecCertificateGetAuthorityKeyID error
mfi4Auth_util_unpackFromTunnelDataiAP2Msg: message 0x%04X, length %d
handle_NVMPublicKeyChallenge: EraseUserKey: !userPublicKey
nvmDhPublicKeyY %@
AuthCert: authSession shutting down
initIdentityCerts: !authSession
missing data handler
iAP2RelayFailed: !authSession
(moduleType=%d) authError %d after _verifyCertificate
(moduleType=%d) cpSetAuthStatus failed: 0x%x
parseNVMReadResponse: paramID: %d
parseNVMReadResponse: iAP2MsgGetNextParamWithError: error
NVMReadResponse: !userNameString
RefreshAccessStateResponse: !authSession
iAP2RelaySucceeded: !inMessage
tryCount = %d (max tries %d)
Failed to decrypt message
mfi4Auth_protocol_handle_AuthCert: decompress error: failed to allocated %zu bytes
AuthenticationSucceeded: !authSession
RequestAuthStart: !outMessage
copyDeviceIdentityCertificates interval: %f\n
AMFDRSealingMapCopyMultiInstanceForClass returned error: %@
handle_NVMPublicKeyChallenge: EraseUserKey: initMessage_RequestNVMErasePublicKey error
_replyGetNVMKey: dictionary
seckey_sign: error: %d\n
AuthenticationFailed: authSession shutting down
RefreshAccessStateResponse: accessState:%d
mfi4Auth_protocol_handle_iAP2RelayRemote: %@
handle_NVMAuthFinish: ccsigma_open A_c1
publicManufacturerNVMRead: !outMessage
RequestAuthCert: paramId %d (0x%x)
%s: unable to allocate outMsg buffer!
firmwareVersionString %@
%s: !keys
mfi4Auth_relay_handle_iAP2RelayRemote: no secureTunnelHandler for type %d !!!
(moduleType=%d) authError = eNoDeviceIDSNError after _readDeviceIDSN
parseNVMReadResponse: KeyNotRead:0x%x
AuthChallengeResponse: authSession shutting down
mfi4Auth_protocol_validateSignature: ccsigma_import_peer_verification_key error
%s: unable to allocate outMsg!
%s:%d reached end of parameter (%d bytes), grplen %d\n
parseNVMReadResponse: AuthNonce: errorNo
handle_NVMAuthStart: ccsigma_sign: error
publicManufacturerNVMRead: authSession shutting down
AuthenticationSucceeded: authSession shutting down
mfi4Auth_protocol_initIdentityCerts: error:%d
mfi4Auth_protocol_validateCertChain: certListDict %@
handle_NVMAuthFinish: Action_EraseUserKey
Could not cpGetDeviceInfo: %s\n
parseNVMWriteResponse: paramID: %d
initSigmaContextNvm: !userKey
copyUserPrivateKey: error:%d
mfi4Auth_protocol_initSigmaContext: key_share_size != 33
handle_NVMEraseResponse: KeyNotErased: errorNo
failed to handle auth reset
processIncomingMessageExtra: cmd:0x%x  rsp:0x%x
handle_NVMOperationResponse: paramID: %d
(moduleType=%d) done
(moduleType=%d) Failed to fetch component index: %s\n
(moduleType=%d) cpSetTrustStatusForUI failed: 0x%x
handle_NVMAuthFinish: A_c1 len(%d < %d) too small
requestRefreshAccessState: authSession shutting down
AuthCert: !authSession
CTCompress: error: %d, certType %d, cert_resp: (%zu bytes)\n%{coreacc:bytes}.*P>
(moduleType=%d) Error: The component AppleAuthCP was not found, unexpected NULL service
(moduleType=%d) authError %d after _verifySignature
cpClearCertificate failed: 0x%x
handle_NVMAuthFinish: paramID %d exceeds maximum expected value
encryptPayload: authSession shutting down
encryptPayload: cyphertext: %@
handle_NVMEraseResponse: AuthNonce: count
nvmDhPublicKeyX %@
%s: !sendOutgoingHandler
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
userNVMWrite: initMessage_RequestUserNVMWrite failed: %d
decryptPayload: plainText: %@
RequestAuthStart: !authSession
initMessage_RequestAuthCert: malloc failed
mfi4Auth_protocol_initIdentity: error:%d
no error after _verifyBatteryMatch!
parseNVMReadResponse: paramMask:0x%x
handle_NVMAuthFinish: ccsigma_verify error: %d
_extractPublicKey: SecKeyCopyExternalRepresentation
seckey_sign: signature buffer is too small\n
AuthChallengeResponse: !authSession
initIdentity: !authSession
decryptPayload: !authSession
(moduleType=%d) Error: The component AppleAuthCP was not found, [servicesArray count] is 0
AuthState: !authSession
decryptPayload: ccsigma_open failed: %d
processOutgoingSecureTunnelDataForClient: !authSession
(moduleType=%d) skip component auth
error getting certificate
%s: !values
AuthenticationSucceeded: !outMessage
mfi4Auth_protocol_handle_iAP2RelayRemote: paramID %d, dataLen %d
%s
Flags indicate battery...do not call cpCopyCertificate()
handle_NVMEraseResponse: key not erased: %x
%s: !outMessage
userNVMWrite: authSession shutting down
RequestAuthChallengeResponse: authSession shutting down
mfi4Auth_protocol_initSigmaContext: try dev identity
(moduleType=%d) updateRegistry: cpSetAuthStatus, cpSetTrustStatus
handle_NVMPublicKeyChallenge: !isProgrammed
handle_NVMAuthStart: initMessage_RequestNVMAuthFinish error
mfi4Auth_protocol_initMessage_AuthStart: error %d
initIdentity: authSession shutting down
ccsigma_init: error
_copyOrCreateUserPublicKeyForSerialNumber: featureTag: %@
_handleNvmReadUserPublicKey: !serialNumberString
handle_AuthSetup: initMessage_AuthStart error
RequestAuthCert: !authSession
validateSignature: authSession shutting down
validateSignature: keyRepresentation: %@\n
unexpected message
processIncomingMessageExtra: unexpected startOfMessage:0x0000 for NVMReadResponse
iAP2RelaySucceeded: authSession shutting down
_verifySignature %d: %ld.%03llu
handle_NVMEraseResponse: KeyErased: errorNo
NVMReadResponse: %@
handle_NVMPublicKeyChallenge: EraseUserKey: _generateUserSignature failed
handle_NVMAuthStart: U_sig: %@
handle_NVMAuthFinish: ccsigma_verify
%s: !message
handle_AuthSetup: initMessage_RequestAuthChallengeResponse error
Have a match for (t_bpFDRData_v1)
decryptIncomingData: authSession shutting down
handle_AuthSetup: version fail
mfi4Auth_protocol_handle_AuthCert: decompressed cert is too large! (%zu)
RequestAuthCert: !outMessage
initIdentityCerts: authSession shutting down
decryptIncomingData: decryptPayload rc=%d
encryptOutgoingData: !msgId
authSetupStart: !outMessage
AuthStart: authSession shutting down
mfi4Auth_protocol_handle_AuthCert: decompress error
AuthenticationFailed: !authSession
handle_NVMEraseResponse: iAP2MsgGetNextParamWithError: error
mfi4Auth_relay_handle_iAP2RelayRemote: failed to parse AccessoryInformationUpdate message!!!
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
mfi4Auth_protocol_initSigmaContext: ccsigma_export_key_share: error
(moduleType=%d) Error: challenge==NULL
handle_NVMEraseResponse: KeyNotErased
%s: !inMessage
handle_NVMPublicKeyChallenge: isProgrammed
handle_NVMPublicKeyChallenge: kMfi4Auth_Action_BeginUserKeyErase
handle_NVMOperationResponse: initMessage_RequestNVMOperation: error
_replyGetNVMKey: error
RequestAuthSetup: authSession shutting down
processIncomingData: cmd:0x%x  rsp:0x%x
initSigmaContext: authSession shutting down
mfi4Auth_protocol_validateSignature: SecKeyCopyExternalRepresentation error
mfi4Auth_protocol_handle_iAP2RelayRemote: msgID 0x%04x, len %d
processIncomingData: !inMessage
convert: accessoryUserName: %s
failed to handle request auth cert
failed to handle auth finish
(moduleType=%d) Error: The component AppleAuthCP was not found, servicesArray is NULL
handle_NVMPublicKeyChallenge: isProgrammed: %d
_extractPublicKey: CFDataGetLength
mfi4Auth_protocol_handle_NVMReadResponse: KeyRead
handle_NVMPublicKeyChallenge: BeginUserKeyErase: !actionReply
AuthCert:: certType %d, cert_resp_len %zu, compressedLength %zu
_mfi4Auth_relay_handle_AccessoryInformationUpdate: finish
(moduleType=%d) Error: Could not parse certificate
handle_NVMAuthStart: U_c0: %@
failed to handle refresh access state response
processIncomingMessageRelay: action %d
error parsing certificate
Invalid parameter: supportedAuthTypesCount!!!
handle_NVMAuthStart: initSigmaContextNvm error
_replyGetNVMKey: !keyStringRef
userNVMRead: initMessage_RequestUserNVMRead failed: %d
mfi4Auth_protocol_handle_AuthCert: SecCertificateGetSubjectKeyID(prodRoot) error
no error after _signChallenge!
_signChallengeForModuleType Replying with signature=%@, deviceNonce=%@, authError = %d
handle_NVMEraseResponse: featureTag: %@
initMessage_RequestNVMAuthStart
handle_AuthSetup: initSigmaContext error
mfi4Auth_protocol_handle_AuthCert: SecCertificateGetSubjectKeyID(devRoot) error
processIncomingMessageExtra: non-Extra message id 0x%04x — falling through to relay
mfi4Auth_util_unpackFromTunnelDataiAP2Msg: message 0x%04X, type %d, Already have unpackedMessage %ld bytes !!!, release and create new one
(moduleType=%d) Replying with overallAuthPassed = %d, overallFdrValid = %d, authError = %d
error verifying serial number
error generating signature: auth cp error code %#x\n
%s: !authSession
authSetupStart: initMessage_RequestAuthSetup failed: %d
handle_AuthSetup: authType:%x
%s: secureTunnelType %d
(moduleType=%d) Error: signature==NULL
(moduleType=%d) sleeping for %d seconds before retrying auth
ERROR: %s:%d Couldn't get next param from iAP2MsgGetNextParamWithError\n
%s: !keyNotRead
initSigmaContextNvm: key_share_size != 33
_replyGetNVMKey: !keyRef
handle_AuthSetup: nego_trans malloc error
RequestAuthChallengeResponse: mismatched auth type
mfi4Auth_protocol_handle_AuthCert: known skid
AuthenticationReset: Ignored
%s: !authKeyValue
requestRefreshAccessState: !outMessage
RefreshAccessStateResponse: !inMessage
mfi4Auth_protocol_handle_iAP2RelayRemote: invalid unpacket message size(%zu) !!!
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
handle_NVMEraseResponse: paramID: %d
handle_NVMEraseResponse: !serialNumberString
NVMReadResponse: RequestNVMAuthStart
handleNVMWriteResponse: !serialNumberString
handle_NVMPublicKeyChallenge: !kMFi4_Area51_NVM_User_PublicKey
%s: !valuesLength
seckey_sign\n
(moduleType=%d) %s: %d: returned error
CoreAnalytics event: %@\neventDict: %@
%s:%d negotiatedVersion %d, force %d, commandID 0x%04x -> 0x%04x
encryptOutgoingData: authSession shutting down
userNVMRead: !authSession
AuthFinish: !outMessage
RequestAuthChallengeResponse: !authSession
processOutgoingSecureTunnelDataForClient: sendOutgoingData failed
(moduleType=%d) authError %d after _signChallenge
handle_NVMPublicKeyChallenge: !authNonceRef
_handleNvmReadUserPublicKey: !publicKey
encryptOutgoingData: cmd:0x%x
encryptOutgoingData: encryptPayload rc=%d
handle_AuthFinish: initMessage_RequestAuthCert failed
initSigmaContext: ccsigma_import_signing_key
validateCertChain: evaluate failed
error getting MFAACertificateManager
ccsigma_set_signing_function: error
mfi4Auth_protocol_messageHandler_receiveIncomingData: Found message
mfi4Auth_protocol_handle_AuthCert: count=%d
dhPublicKeyInitiator %@
failed to handle auth cert
%s:%d negotiatedAuthType %d, leafCertLen %zu, leafCertType %d, intermediate1_cert_init_len %zu
(moduleType=%d) Error: The component AppleAuthCP was not found
handle_NVMAuthStart: paramID: %d
seckey_sign: MFAADeviceIdentityCreateSignature error\n
mfi4Auth_protocol_initSigmaContext
mfi4Auth_protocol_initSigmaContext: no identity left
processIncomingMessageRelay: override supportedSecureTunnelCapabilitiesMask 0x%llx &= 0x%x
encryptOutgoingData: no encrypting required: %x
(moduleType=%d) cpSetTrustStatus failed: 0x%x
handle_NVMAuthFinish: ccsigma_open failed: %d
!sigmaContextNvm
!rng
receiveIncomingData: outMessage:(%d)
decryptIncomingData: rsp:0x%x
handle_AuthSetup: auth type %d
mfi4Auth_protocol_handle_AuthCert: compressedLength:%d
dataLength matches Roswell data length, return copy of fdr data
mfi4Auth_protocol_handle_NVMReadResponse: !serialNumberString
mfi4Auth_protocol_initSigmaContextNvm
mfi4Auth_protocol_messageHandler_receiveIncomingData
AuthStart: ccsigma_sign: error
negoTrans %@
serialNumberString %@
(moduleType=%d) equal:%d
%s: !authResponse
AuthSetupFailed: !authSession
(moduleType=%d) tryCount = %d (max tries %d)
handle_AuthSetup: !inMessage
mfi4Auth_protocol_validateCertChain: errorNo: %d
(moduleType=%d) Cannot find FDR cert
RequestNVMAuthFinish
mfi4Auth_protocol_messageHandler_receiveIncomingData: Found no message starting with: %x
validateCertChain: missing certificate
errorNo:%d
handle_NVMOperationResponse: processIncomingData: error
ccsigma_derive_session_keys: error
mfi4Auth_protocol_initSigmaContext: try prod identity
authSetupStart: authSession shutting down
mfi4Auth_protocol_validateSignature: !nonceData
encryptOutgoingData: !authSession
authSetupStart: !authSession
handleAuthSessionClose: !authSession
%s: !authNonce
handle_NVMPublicKeyChallenge: BeginUserKeyErase: !kMFi4_Area51_NVM_User_PublicKey
Received AuthenticationFailed
mfi4Auth_protocol_processIncomingMessage: error: %d
certificate = %@
handle_NVMAuthFinish: encryptPayload
handle_NVMAuthFinish: initMessage_RequestNVMOperation
PairedToAnotherUser (!keyRef)
iAP2RelayRemote: !authSession
handle_NVMPublicKeyChallenge: paramID: %d
handle_NVMAuthStart: ccsigma_seal error
handle_NVMAuthFinish: initMessage_RequestNVMPublicKeyChallenge failed: %d
_replyGetNVMKey: !valueData
missing secure tunnel handler
_verifyBatteryMatch %d: %ld.%03llu
mfi4Auth_protocol_handle_NVMReadResponse: UserPublicKey_NotProgrammed
_copyOrCreateUserPublicKeyForSerialNumber: failed
outMessage: !authSession
handle_AuthSetup: Capabilities fail
mfi4Auth_protocol_handle_AuthCert: decompress size error: %d
mfi4Auth_protocol_handle_AuthCert: authorityIsRoot: dev:%d, prod:%d
%s (certData.length: %lu)
Sleeping for %d seconds before retrying auth
decryptIncomingData: !msgId
RequestAuthStart: authSession shutting down
Received AuthenticationReset
iAP2RelaySucceeded: !authSession
manufacturerString %@
mfi4Auth_util_packIntoTunnelDataiAP2Msg: invalid data passed in
ERROR No auth io_service_t is found!
pRoswellDataStructure->roswell_cert_len = %d
authError %d after _signChallenge
handle_NVMPublicKeyChallenge: paramID %d exceeds maximum expected value
handle_NVMAuthStart: !userKey
IDSN length %zu exceeds buffer
copyUserPublicKeyForSerialNumber: failed
handle_AuthSetup: initMessage_RequestAuthChallengeResponse
RequestAuthSetup: !outMessage
mfi4Auth_protocol_handle_AuthCert: Accessory did NOT provide PrivacyPrefix!
RequestAuthChallengeResponse: malloc failed
validateCertChain: !certList
mfi4Auth_relay_handle_iAP2RelayRemote: msgID 0x%04x, len %zu
handle_NVMEraseResponse: KeyErased
handle_NVMAuthStart: !userPublicKey
!sigmaContext
processIncomingMessageRelay: supportedSecureTunnelCapabilitiesMask 0x%llx, currentType/Mask %d/0x%llx
setSecureTunnelDataReceiveHandler: authSession shuttingDown
ccsigma_import_signing_key: error
initSigmaContext: no signing key
(moduleType=%d) moduleAuthService = %d
missing auth session
seckey_sign: signature: %@\n
receiveIncomingData: processIncomingData returned:%d
publicManufacturerNVMRead: !authSession
RequestAuthChallengeResponse: !outMessage
%s:%d negotiatedAuthType %d, cert_init_len %zu, cert_init_type %d, intermediate1_cert_init_len %zu
(moduleType=%d) authError %d after _readSignature
auth length = %ld, sizeof(t_bpFDRData_v1) = %lu, does not match
(moduleType=%d) No authIC cert to compare against FDR
moduleAuthService = %d
verifyBatteryMatch Replying with authError = %d
handleNVMWriteResponse: parse failed
handle_NVMAuthFinish: paramID: %d
receiveIncomingData: keepOpen:%d
requestRefreshAccessState: !authSession
%s: authSession(%d), keepOpen %d, error %d
handle_AuthSetup: Capabilities fail: Too Many!
NVMPublicKeyChallenge: WriteUserKey: !userPublicKey
_replyGetNVMKey: !contains
mfi4Auth_relay_handle_iAP2RelayRemote: Unknown UserMessage 0x%x
handle_NVMPublicKeyChallenge: EraseUserKey: _copyOrCreateUserPublicKeyForSerialNumber failed
(moduleType=%d) Replying with authPassed = %d, fdrValid = %d, authError = %d
handle_NVMPublicKeyChallenge: reply
missing data to send out
copyUserPublicKeyForSerialNumber: featureTag: %@
_replyGetNVMKey: !actionKeyCount
decryptPayload: negotiatedVersion: %d
copyDeviceIdentityCertificates completed: %d\n
mfi4Auth_protocol_handle_NVMReadResponse: KeyNotRead
handle_NVMAuthFinish: completed
RefreshAccessStateResponse: authSession shutting down
processIncomingMessageRelay: cmd:0x%x  rsp:0x%x
mfi4Auth_protocol_handle_iAP2RelayRemote: unable to unpack nested message!!!
mfi4Auth_protocol_handle_AuthCert: validateCertChain failed: %d
AuthFinish: !authSession
AuthenticationReset: !authSession
CTCompressComputeBufferSize: error: %d, certType %d, cert_resp: (%zu bytes)\n%{coreacc:bytes}.*P>
handle_NVMOperationResponse: encryptPayload: error
%s:%d reached end of message buffer (%d bytes)\n
parseNVMReadResponse: AuthNonce length: %d
handle_NVMAuthFinish: A_sig: %@
(moduleType=%d) Error: Could not evaluate certificate
_handleNvmReadManufacturerPublicKey
handleNVMWriteResponse: unexpected response content
%s: !dataIn
%s:%d paramMask 0x%x, CertHash paramMask 0x%x, CertKeyID paramMask 0x%x 
AuthenticationReset: authSession shutting down
decryptPayload: authSession shutting down
processIncomingMessageRelay: non-relay message id 0x%04x — no relay action
AuthCert: !inMessage
mfi4Auth_protocol_handle_AuthCert: SecCertificateCreateWithBytes error
kMfi4Auth_Action_ReadUserName
processOutgoingSecureTunnelDataForClient: !dataOut
hardwareVersionString %@
Starting xpc service
ERROR: %s:%d ERROR: message parse error, length (%u) passed allocated buffer length (%u)
AuthenticationSucceeded: !inMessage
mfi4Auth_protocol_validateSignature: verification passed
processOutgoingSecureTunnelDataForClient: sessionID %x, type %d, dataOut %@
Failed to create os_log_t object %s: %s!
Received plain text message
RequestAuthSetup: !authSession
Received AuthenticationSucceeded
NVMPublicKeyChallenge: WriteUserKey: !serialNumberString
handle_NVMPublicKeyChallenge: kMfi4Auth_Action_BeginVendorKeyErase
wrong type (%d)
encryptPayload: plaintext: %@
mfi4Auth_util_packIntoTunnelDataiAP2Msg: unable to allocate outMsg!
AuthenticationFailed: !inMessage
processIncomingMessageRelay: !inMessage
handle_AuthSetup: authSession shutting down
handle_AuthSetup: unexpected error during param parsing
%s: ForceAuthFail/PretendNFCAuthFailed!!!, set status(%d)
processIncomingMessageRelay: override supportedSecureTunnelCapabilitiesMask 0x%llx |= 0x%x
mfi4Auth_relay_handle_iAP2RelayRemote: unable to create parser!!!
handle_NVMAuthFinish: encryptPayload failed: %d
AuthChallengeResponse: !inMessage
AuthCert:: Invalid cert_resp, null or 0 len(%zu), certType %d
decryptPayload: !inMessage
iAP2RelayFailed: authSession shutting down
(moduleType=%d) Found %lu matching service(s)
Notifying clients of %s
handle_NVMPublicKeyChallenge: BeginVendorKeyErase: !actionReply
UserPublicKey %@
mfi4 %@
handle_AuthSetup: unexpected param mask:%x
RequestAuthCert: !inMessage
AuthFinish: !inMessage
acc_internalSettings: internal-only setting %{public}@ active
error generating signature: %s\n
publicManufacturerNVMRead: initMessage_RequestManufacturerNVMRead failed: %d
RefreshAccessStateResponse: userNVMReadProtected:%d
processIncomingMessageRelay: error: %d
mfi4Auth_util_packIntoTunnelDataiAP2Msg: unable to allocate outMsg buffer!
Created %d log object(s)!
userNVMRead: !outMessage
mfi4Auth_protocol_handle_AuthCert: Accessory DID provide PrivacyPrefix!
mfi4Auth_protocol_validateSignature: !signatureData
modelIdentifierString %@
mfi4Auth_util_unpackFromTunnelDataiAP2Msg: Unrecognized message 0x%04X !!!
signature = %@
%s: !keyRead
setSecureTunnelDataReceiveHandler: !dataHandler
(moduleType=%d) authError = %d after verifyModuleCertificate
handle_NVMEraseResponse: key erased: %x
userNVMRead: authSession shutting down
encryptPayload: ccsigma_seal: error
decryptPayload: cyphertext: %@
mfi4Auth_protocol_validateSignature: MFAAVerifyNonceSignature error
handle_NVMEraseResponse: paramMask:0x%x
PairedToAnotherUser
failed to handle auth starat
processIncomingMessageRelay: !authSession
processIncomingMessageRelay: supportedSecureTunnelCapabilitiesMask 0x%llx, processed 0x%llx
(moduleType=%d) %s: AMFDRSealingMapCopyLocalDataForClass: returned NULL
decryptIncomingData: failed: %d
mfi4Auth_protocol_initIdentity(dev) error
processOutgoingSecureTunnelDataForClient: authSession shuttingDown
(moduleType=%d) authError %d after _readCertificate
could not open service: %s\n
Could not cpGetDeviceIDSN: %s\n
handle_NVMAuthStart: paramID %d exceeds maximum expected value
AuthSetupFailed: !outMessage
device nonce = %@
handle_NVMPublicKeyChallenge: failed: %d
handle_NVMAuthFinish: initMessage_RequestNVMOperation failed: %d
AuthStart: !inMessage
RequestRefreshAccessState: !outMessage
setSecureTunnelDataReceiveHandler: !authSession
%s: wrong messageID
_handleNvmReadUserPublicKey: userPublicKeyMask:%x
AuthSetupFailed: authSession shutting down
AuthStart: ccsigma_seal: error
handle_NVMEraseResponse: AuthNonce: errorNo
parseNVMReadResponse: key: 0x%x
handle_NVMOperationResponse: paramID %d exceeds maximum expected value
mfi4 %s = 
requestRefreshAccessState: initMessage_RequestRefreshAccessState failed: %d
handleAuthSessionClose: authSession shutting down
verifyModuleCertificate succeeded
handle_NVMAuthStart: !serialNumberString
mfi4Auth_protocol_initIdentity error: %d
(moduleType=%d) index:%@
handle_NVMAuthFinish: ccsigma_import_peer_verification_key error
%s: !dhPublicKey
%s: Received secure tunnel data with invalid type
mfi4Auth_protocol_handle_RequestAuthCert: CertId failed
NotPaired
mfi4Auth_protocol_validateSignature: SecCertificateCopyKey error
processIncomingMessageRelay: !msgId
Failed to retrieve device IDSN
handle_AuthSetup: dhPublicKey fail
handle_AuthSetup: dhPublicKey %d
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
_replyGetNVMKey: !userPublicNVMKeyValues
handle_AuthSetup: unsupported auth version %d
dhPublicKeyResponder %@
verifyModuleCertificate: evaluate failed
invalide secureTunnelType (%d)
mfi4Auth_protocol_handle_iAP2RelayRemote: Has no payload !!!, retry after %d ms
receiveIncomingData: sendOutgoingData failed
decryptIncomingData
AuthCert: !outMessage
processIncomingData: failed to handle auth setup
Received RefreshAccessStateResponse
encryptPayload: !authSession
%s: paramID: %d
(moduleType=%d) cpSetBatteryCode failed: 0x%x
(moduleType=%d) %s: AMFDRSealingMapCopyLocalDataForClass returned error=%@
AuthSetupFailed: !inMessage
validateCertChain: authSession shutting down
parseNVMWriteResponse: keyWritten: 0x%x
parseNVMWriteResponse: keyNotWritten: 0x%x
handle_NVMPublicKeyChallenge: EraseUserKey: !serialNumberString
ccsigma_import_peer_key_share: error
Flags indicate rcam...do not call cpCopyCertificate()
authError %d after _verifyBatteryMatch
handle_NVMAuthFinish: A_c1[%d]: %@
handle_AuthSetup: missing params
missing outboundSecuredData
initSigmaContextNvm: ccsigma_set_signing_function
_handleNvmReadUserPublicKey: !keyRef
mfi4Auth_protocol_handle_AuthCert: validateSignature failed: %d
kMfi4Auth_Action_WriteUserName: count:%d, [0]:0x%x
processIncomingMessage: authSession shuttingDown
validateCertChain: unexpected count 0
mfi4Auth_protocol_validateCertChain: certList %@
failed to handle relay remote
payload: %@
mfi4Auth_relay_handle_iAP2RelayRemote: type %d, data %@
Flags indicate Veridian...do not call cpCopyCertificate()
%s: parse error
userNVMWrite: !outMessage
processIncomingData: !msgId
mfi4Auth_protocol_validateSignature: !certData
iAP2RelayRemote: !inMessage
```
