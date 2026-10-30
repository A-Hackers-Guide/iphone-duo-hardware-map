# `/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCHWComponentAuthService.xpc/ACCHWComponentAuthService`

From the upgrade restore ramdisk (141-29011-104.dmg). 839,792 bytes.

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
EnableAuthTimeoutTTR
PretendNoDeviceIdentityCerts
MPPAuthEnablePretendAuth
MaxOutboundiAP2PacketSize
prpc
mfi4Auth_protocol_parse
mfi4Auth_protocol_messageHandler_receiveIncomingData
InternalBuild
authErrorDescription
2006-05-31
MFi4SigmaIRequired
no
mfi4Auth_protocol_initMessage_RequestUserNVMErase
Beta
DisableCertSupport
_getCachedUserPublicKey
ComponentName
ConnectionInfo
IdentityCertUseIndex
iAP2MsgGetNextParamWithError
AllowNFCColorOverride
OverrideMPPAuthSupported
Challenge
com.apple.mfi4Auth.process
com.apple.mfi4Auth.send
HW Component Auth
ForceAuthFail
ACCAuthProtocolRoleSupport
6)
VerifyNonceSignatureError
CCSIGMA_MFI_SI_KEY
Transport Client
DisableAACPAuth
KeepAACPAuthData
IgnorePowerSourceUpdateForAvailableCurrent
PlatformIDOverride
InductiveAuthPretendMatchRxID
DontSkipInductiveAuthOnCTA
ForceT56RelaySupport
CarPlay Service
IdentityCertRefreshState
DisableIAPHVCFixForAuth
BLEPairingAuthTimeoutValueS
MFi4ECDSAOnly
com.apple.iapd.PreferencesDidChangeNotification
LeafCertData
wiredAuthDuration
<Undefined>
BypassTrustDialog
IdentityCertIsClassD
ChargingPowerBehavior
CreateRandomNonceError
mfi4Auth_protocol_handle_NVMEraseResponse
CCSIGMA_MFI_CR_KEY
AccessoryCertificateSerialNumber
TouchController
SerialNumberPairingError
FDRStatusUnknown
mfi4Auth_protocol_initMessage_RequestNVMErasePublicKey
com.apple.mfi4Auth.decrypt
ComponentIndex
ucrt
ForceAuthTimeout
EnableDEVNCertSupport
DisablePowerUpdateForCurrentDraw
MFi4AuthTimeoutValueS
DisableNFCAuthTimer
Veridian
VerifyPublicCertificateError
mfi4Auth_protocol_initMessage_RequestNVMAuthFinish
com.apple.accessories.frameworks.core-accessories
AudioAccessory
PretendNFCAuthTimeout
NoDeviceIDSNError
ComponentBusyError
MFi40Attestation-Certificate
nil
_mfi4Auth_relay_handle_AccessoryInformationUpdate
ForceAccInfoUpdateRelaySupport
RCAM
SerialNumberCompareError
MissingPairedAuthInstanceError
mfi4Auth_protocol_initMessage_RequestNVMAuthStart
isTrusted
CCSIGMA_MFI_CI_KEY
DeviceVersion
AuthMinorVersion
isTrustedForUI
cpSetExpectedPairedCertSN: !CFStringGetCString
SysdiagnoseInsteadOfAuthTTR
NFCAnalyticsDate
UseCertDataPropertyForAuth
EnableACCAuthProtocolOnNFC
_convertUserNVMWrite
MPPAuthPreferredSlot
com.apple.CoreAccessories.PreferencesDidChangeNotification
isPeriodic
Failed
CCSIGMA_MFI_TI_KEY
ProductType
IORegistryEntryID
DeviceCompatibility
LiveVoicemailFakeRinging
CertSerialNumberError
CCSIGMA_MFI_SR_IV
_handleNvmReadUserPublicKey
TestCreateBLEPairingOnInductive
ACCAuthProtocolAllowMutualAuth
mfi4Auth_protocol_convertUserAccessoryInfoToAction
mfi4Auth_protocol_messageHandler_handleOutgoingSecureTunnelDataForClient
ShowHiddenAccessories
USBHiAPEnable
WaitForiAPTrafficDelayMS
bcrt
_convertUserVendorNVMRead
MFi4Auth
IdentityCertRefreshInterval
CreateCertificateSerialNumberError
com.apple.mfi4Auth.receive
cpCreateSignatureWithIndexAndToken
AuthSuccess
mfi4Auth_protocol_parse_NVMWriteResponse_v2
CCSIGMA_MFI_EI_IV
DeviceID
Use +[%@ %@] instead of -%@.
AuthDeviceInfoError
mfi4Auth_protocol_messageHandler_sendOutgoingData
Endpoint
AuthTTRForAllTransports
DisableInductiveAuthTTR
ProductID
HardwareVersion
FirmwareVersionPending
SkipNFCAuth
AppleAuthCP
IgnoreAuthReset
PretendNoNFCResponse
wcrt
FDRStatusPass
mfi4Auth_protocol_initSigmaContextNvm
DeviceNonce
cpGetComponentIndex: Failed to find ComponentIndex property
TreatAuthCPDEVNAsV3
AuthBatteryMismatchOnProdDevice
mfi4Auth_protocol_handle_NVMWriteResponse
mfi4Auth_protocol_initMessage_RequestNVMPublicKeyChallenge
com.apple.ACCHWComponentAuthService.rcam
AuthTimerExpiredError
mfi4Auth_protocol_initMessage_RequestManufacturerNVMRead
AccessoryDeviceUID
Transport Plugins
EnableIndonesiaInductiveTx
DisableACCAuthProtocolOnInductive
+[ACCHWComponentAuthService _verifyModuleFDR:forModuleType:]
Bluetooth Service
com.apple.accessories.signposts
PretendWirelessCTAMatch
pretend_auth
com.apple.accessories.hwComponent.isTrusted.failure
Yonkers - Factory
%y%m%d%H%M%SZ
AuthCPStartDelayMs
ACCAuthProtocolMaxMessageSize
CreateSignatureError
IOTimeoutDeviceBusyError
_convertNVMReadResponse
RegionCode
PretendAccessoryType
com.apple.ACCHWComponentAuthService.veridian
vcrt
mfi4Auth_protocol_parse_NVMWriteResponse_v3
App Links
NFCColorOverride
SkipGaugeSignatureCheck
AuthBatteryMismatchOnDevDevice
isInductive
com.apple.ACCHWComponentAuthService.battery
mfi4Auth_relay_StartRelayForType
General
BLEPairingDontEarlyInfoAsDeviceUID
CreateSerialNumberStringFromDataError
mfi4Auth_protocol_handle_NVMAuthFinish
%Y%m%d%H%M%SZ
v8@?0
ProductVersion
SerialNumber
FirmwareVersionActive
OverrideCanReceiveInductivePowerOID
EnableChinaInductiveTx
IgnoreIsOnAC
LAS
Model
PretendBatteryLevel
com.apple.ACCHWComponentAuthService.touchcontroller
_convertNVMEraseResponse
cpGetComponentIndex: Component index not CFNumber
DisableAuthTimeoutTTRForXR
EnableWrongOrientationMessage
mfi4Auth_protocol_cleanupSessionCommon
BLEPairingDisableOOBPPlusFlow
com.apple.ACCHWComponentAuthService.las
_consumeByteInternal
0x%02x, 
com.apple.logging
DisableCertVerification
IgnoreAccInfoUpdateRelaySupport
tcrt
%d
mfi4Auth_protocol_handle_RequestAuthCert
cpGetComponentIndex: Got component index : %x\n
DisableWirelessCTA
Disable1WayNFCForInductive
internalModuleType
CCSIGMA_MFI_CI_IV
cpGetComponentIndex: Component index not SInt32
com.apple.iapd
com.apple.accessoryd
%02x
FullCertData
_convertUserNVMErase
cpGetTransportEntryId: IOConnectCallScalarMethod failed: 0x%x\n
DisableAMSHookUp
UARPActivityTimerS
yes
CCSIGMA_MFI_ER_IV
mfi4Auth_protocol_handleAuthSessionClose
mfi4Auth_protocol_handle_AuthCert
cpSetAuthError %d\n
Repair UCRT
ForceMFi4AuthOverNFC
SigningFuse
PPIDVersionUID
ReleaseType
DisableSNOnly
EnableManager2ForTransport
Battery
authState
-
mfi4Auth_protocol_handle_NVMPublicKeyChallenge
AllowACCAuthProtocolOnAllTransport
MFi4ECDSADisallow
RejectionOfMultipleLocation
FDRStatus
flags
-[ACCHWComponentAuthService _validateWithFDRCertificate:forModuleType:withAuthParams:]
CCSIGMA_MFI_EI_KEY
_replyGetNVMKey
VerifyCertificateSerialNumberError
iAP2MsgForEachParamDo
mfi4Auth_protocol_handle_NVMAuthStart
mfi4Auth_protocol_validateCertChain
AccessoryCertificate
IgnoreAACPAuthStatus
DisableT56Support
MPPAuthChallengeFirst
AuthenticationOverride
Uptime
i
NullCertificateDataError
CertificateAuthVersionNumberError
VendorID
External Accessory
AllowMFi4DevCertsOnProdDevice
NoAuthICPresentError
mfi4Auth_protocol_initMessage_RequestNVMWritePublicKey
mfi4Auth_protocol_requestNvmErasePublicKey
com.apple.mfi4Auth.protocol
MFi40Accessory-Intermediate
Connection
Transport
ChargingPowerOverride
TransportSignpost
IOAccessory
AuthPassed
cpGetChallengeSignatureLengths
%F
InternalModuleCapabilityMismatchError
BadArgumentError
NFCSecondaryColorOverride
PowerSourceUpdateBehavior
isBatteryModule
FDRStatusFail
mfi4Auth_protocol_parse_NVMReadResponse
mfi4Auth_protocol_handle_NVMReadResponse
Name
EnableTrustDialog
DisableAuthFailureTTRForXR
PretendNFCAuthFailed
com.apple.accessories.authCPEvent
PretendAuthFailure
Savage - Factory
Manufacturer
PearlIDCapability
BLEPairingConfigRequestDelayMs
MPPAuthGetLeafCertFirst
GenericMFiIgnoreCertCaps
CopyAllowUnsealed
NoAuthCPServicePresentError
CCSIGMA_MFI_SR_KEY
RefreshInterval
mfi4Auth_protocol_initMessage_RequestNVMOperation
com.apple.mfi4Auth.encrypt
FirmwareVersion
IDSN
cpCreateFormattedChallengeFromServerRequest
ACCAuthProtocolPretendAuth
com.apple.accessories.connection.passedMFi4Auth
MFi40Accessory-Certificate
KnownAccessories
wapi
DeviceClass
BLEPairingIgnoreZeroEarlyInfo
CanChargeInductiveError
__createCertificateRefWithData
InternalComponent
IdentityCertUseTime
DisableMFi4CertSupport
CreateCapsFromAuthCertError
CCSIGMA_MFI_TR_KEY
com.apple.CoreAccessories
DeviceIdentityPreArmDateOverride
v36@?0B8@\"NSData\"12@\"NSData\"20B28i32
mfi4Auth_protocol_initMessage_RequestUserNVMWrite
CCSIGMA_MFI_ER_KEY
MFi40Attestation-Intermediate
Passed
mfi4Auth_protocol_initMessage_RequestVendorNVMRead
mfi4Auth_relay_initMessage_DeviceiAP2RelayRemote_RequestAccessoryInfoUpdate
PPID
AccessoryPlatformID
TimeSync
iboot-auth
XpcConnectionError
CCSIGMA_MFI_SI_IV
MFi30Accessory-Certificate
Count
Signature
MismatchedPairingError
mfi4Auth_protocol_handle_NVMOperationResponse
AuthMajorVersion
cpCreateFormattedResponseForServerResponse
cpSetActualPairedCertSN: !CFStringGetCString
PacketLoggingPlainTextOnly
MFi4RelayReadRetryDelayMs
authError
VerifyModuleFDRError
UninitializedAuthError
CCSIGMA_MFI_CR_IV
SysdiagnoseOnInductiveCTAFailure
com.apple.accessoryd.mfi4.userPublicKey.%@
Invalid parameter: supportedAuthTypesCount!!!
handle_NVMPublicKeyChallenge: !isProgrammed
_replyGetNVMKey: dictionary
receiveIncomingData: outMessage:(%d)
mfi4Auth_protocol_initSigmaContext: try prod identity
processIncomingMessageRelay: override supportedSecureTunnelCapabilitiesMask 0x%llx &= 0x%x
Could not cpGetDeviceInfo: %s\n
parseNVMReadResponse: iAP2MsgGetNextParamWithError: error
handle_NVMPublicKeyChallenge: EraseUserKey: initMessage_RequestNVMErasePublicKey error
handle_NVMAuthStart: !serialNumberString
ccsigma_derive_session_keys: error
_replyGetNVMKey: !contains
(moduleType=%d) Error: signature==NULL
signature = %@
no error after _verifyBatteryMatch!
(moduleType=%d) cpSetAuthError failed: 0x%x
parseNVMWriteResponse: keyNotWritten: 0x%x
handle_NVMAuthStart: U_c0: %@
handle_NVMAuthFinish: Action_WriteUserName
Received AuthenticationSucceeded
(moduleType=%d) authError %d after _readSignature
missing auth session
handle_NVMAuthStart: paramID %d exceeds maximum expected value
handle_NVMAuthFinish: A_c1 len(%d < %d) too small
%s: !keys
dhPublicKeyResponder %@
processIncomingMessageRelay: non-relay message id 0x%04x — no relay action
iAP2RelaySucceeded: !authSession
error getting MFAACertificateManager
handle_AuthSetup: auth type %d
processOutgoingSecureTunnelDataForClient: sessionID %x, type %d, dataOut %@
serialNumberString %@
mfi4Auth_util_unpackFromTunnelDataiAP2Msg: message 0x%04X, type %d, Already have unpackedMessage %ld bytes !!!, release and create new one
(moduleType=%d) Found %lu matching service(s)
handleAuthSessionClose: !authSession
AuthenticationSucceeded: !inMessage
validateCertChain: unexpected count 0
mfi4Auth_protocol_validateSignature: !certData
iAP2RelaySucceeded: !inMessage
%s: unable to allocate outMsg buffer!
Notifying clients of %s
missing data handler
manufacturerString %@
handle_NVMAuthFinish: paramID %d exceeds maximum expected value
handle_NVMAuthFinish: ccsigma_import_peer_verification_key error
handle_NVMAuthFinish: encryptPayload failed: %d
handle_AuthSetup: dhPublicKey fail
mfi4Auth_protocol_handle_AuthCert: decompressed cert is too large! (%zu)
mfi4Auth_protocol_handle_iAP2RelayRemote: paramID %d, dataLen %d
mfi4Auth_util_unpackFromTunnelDataiAP2Msg: message 0x%04X, length %d
NVMPublicKeyChallenge: WriteUserKey: !serialNumberString
decryptIncomingData: !msgId
handle_AuthSetup: authType:%x
mfi4Auth_protocol_handle_AuthCert: count=%d
handle_NVMEraseResponse: iAP2MsgGetNextParamWithError: error
handle_AuthSetup: unexpected param mask:%x
AuthStart: authSession shutting down
mfi4Auth_protocol_handle_AuthCert: authorityIsRoot: dev:%d, prod:%d
Starting xpc service
(moduleType=%d) Replying with overallAuthPassed = %d, overallFdrValid = %d, authError = %d
could not open service: %s\n
ERROR No auth io_service_t is found!
parseNVMReadResponse: key: 0x%x
%s: ForceAuthFail/PretendNFCAuthFailed!!!, set status(%d)
failed to handle auth cert
(moduleType=%d) tryCount = %d (max tries %d)
handle_NVMEraseResponse: AuthNonce length: %d
acc_internalSettings: internal-only setting %{public}@ active (%ld)
handle_AuthSetup: initMessage_RequestAuthChallengeResponse error
handle_NVMAuthFinish: initMessage_RequestNVMOperation
handle_NVMAuthFinish: ccsigma_import_peer_verification_key
_extractPublicKey: keyDataLength:%ld
%s:%d negotiatedAuthType %d, cert_init_len %zu, cert_init_type %d, intermediate1_cert_init_len %zu
hardwareVersionString %@
publicManufacturerNVMRead: initMessage_RequestManufacturerNVMRead failed: %d
handle_NVMEraseResponse: !serialNumberString
PairedToAnotherUser (!keyRef)
Flags indicate battery...do not call cpCopyCertificate()
_verifyBatteryMatch %d: %ld.%03llu
_replyGetNVMKey: !userPublicNVMKeyValues
%s: authSession(%d), keepOpen %d, error %d
mfi4Auth_protocol_handle_AuthCert: decompress error
mfi4Auth_protocol_handle_NVMReadResponse: !serialNumberString
initSigmaContextNvm: ccsigma_set_signing_function
processIncomingMessageExtra: unexpected startOfMessage:0x0000 for NVMReadResponse
setSecureTunnelDataReceiveHandler: !dataHandler
(moduleType=%d) Error: challenge==NULL
device nonce = %@
mfi4Auth_protocol_messageHandler_receiveIncomingData: Found message
wrong type (%d)
mfi4Auth_protocol_initSigmaContext: try dev identity
failed to handle relay success
NVMPublicKeyChallenge: WriteUserKey: initMessage_RequestNVMWritePublicKey error
receiveIncomingData: sendOutgoingData failed
handle_AuthSetup: !authSession
handle_AuthSetup: initSigmaContext error
AuthSetupFailed: authSession shutting down
mfi4Auth_protocol_handle_AuthCert: known skid
processIncomingMessage: !authSession
mfi4Auth_protocol_validateSignature: !leafCert
Created %d log object(s)!
(moduleType=%d) cpSetAuthStatus failed: 0x%x
handle_NVMAuthFinish: ccsigma_verify
processIncomingMessageRelay: supportedSecureTunnelCapabilitiesMask 0x%llx, currentType/Mask %d/0x%llx
iAP2RelayFailed: !inMessage
%s: !authSession
_replyGetNVMKey: !keyRef
_replyGetNVMKey: error
AuthCert:: Invalid cert_resp, null or 0 len(%zu), certType %d
handle_NVMPublicKeyChallenge: kMfi4Auth_Action_WriteUserKey
handle_NVMOperationResponse: Found no message starting with: %x
userNVMRead: initMessage_RequestUserNVMRead failed: %d
initIdentityCerts: authSession shutting down
mfi4Auth_util_packIntoTunnelDataiAP2Msg: invalid data passed in
%s: parse error
handle_NVMAuthFinish: ccsigma_open failed: %d
%s:%d paramMask 0x%x, CertHash paramMask 0x%x, CertKeyID paramMask 0x%x 
AMFDRSealingMapCopyMultiInstanceForClass returned error: %@
(moduleType=%d) equal:%d
Received plain text message
AuthStart: !authSession
processIncomingMessageExtra: authSession shuttingDown
mfi4Auth_relay_handle_iAP2RelayRemote: unable to create parser!!!
vendor nameString %@
Failed to create os_log_t object %s: %s!
handle_NVMEraseResponse: paramID: %d
%s: !keyRead
userNVMWrite: !outMessage
mfi4Auth_protocol_handle_AuthCert: SecCertificateGetAuthorityKeyID error
AuthCert:: certType %d, cert_resp_len %zu, compressedLength %zu
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
(moduleType=%d) Error: Could not parse certificate
mfi4Auth_protocol_initSigmaContext: no identity left
copyDeviceIdentityCertificates completed: %d\n
iAP2RelayFailed: authSession shutting down
handle_NVMPublicKeyChallenge: EraseUserKey: _generateUserSignature failed
handle_NVMAuthStart: U_sig: %@
mfi4Auth_protocol_messageHandler_receiveIncomingData
AuthStart: !inMessage
Could not cpGetDeviceIDSN: %s\n
%s: !keyNotRead
handle_NVMOperationResponse: processIncomingData: error
AuthChallengeResponse: authSession shutting down
kMfi4Auth_Action_ReadUserName
NVMReadResponse: RequestNVMAuthStart
decryptIncomingData: rsp:0x%x
Received unhandled message with ID: 0x%04x
mfi4Auth_protocol_initSigmaContext
(moduleType=%d) cpSetBatteryCode failed: 0x%x
signatureValid ? %@
_handleNvmReadManufacturerPublicKey
RequestAuthStart: !outMessage
AuthStart: !outMessage
mfi4Auth_protocol_validateSignature: MFAAVerifyNonceSignature error
AuthenticationReset: !outMessage
handle_NVMPublicKeyChallenge: EraseUserKey: !serialNumberString
decryptIncomingData: failed: %d
encryptOutgoingData: authSession shutting down
mfi4Auth_protocol_handle_AuthCert: Accessory DID provide PrivacyPrefix!
(moduleType=%d) authError = eAuthDeviceInfoError after _verifyDeviceInfo
ERROR: %s:%d Couldn't get next param from iAP2MsgGetNextParamWithError\n
_extractPublicKey: SecKeyCopyExternalRepresentation
seckey_sign: signature buffer is too small\n
publicManufacturerNVMRead: authSession shutting down
AuthSetupFailed: !inMessage
acc_internalSettings: internal-only setting %{public}@ active
Failed to retrieve device IDSN
handle_NVMEraseResponse: KeyErased
_replyGetNVMKey: !valueData
seckey_sign: signature: %@\n
AuthFinish: !inMessage
pRoswellDataStructure->roswell_cert_len = %d
_handleNvmReadUserPublicKey: !nvmUserPublicKey
%s: string parameter not NUL terminated! (paramID %d)
(moduleType=%d) Failed to fetch component index: %s\n
%s: !authResponse
RequestNVMAuthFinish
_replyGetNVMKey: !dictionary
%s: Received secure tunnel data with invalid type
processIncomingData: cmd:0x%x  rsp:0x%x
received OperationFailed
failed to handle request auth cert
(moduleType=%d) No authIC cert to compare against FDR
encryptOutgoingData: no encrypting required: %x
handle_AuthSetup: !inMessage
RequestAuthCert: paramId %d (0x%x)
verifyModuleCertificate succeeded
verifyBatteryMatch Replying with authError = %d
%s: !authNonce
encryptOutgoingData: !inMessage
mfi4Auth_protocol_validateSignature: ccsigma_verify error
(moduleType=%d) Could not find authcp services: %s\n
no error after _signChallenge!
_signChallengeForModuleType Replying with signature=%@, deviceNonce=%@, authError = %d
ERROR: %s:%d ERROR: message parse error, length (%u) passed allocated buffer length (%u)
handle_NVMPublicKeyChallenge: failed: %d
tag: %@
RequestAuthStart: authSession shutting down
processIncomingData: failed to handle auth setup
decryptPayload: negotiatedVersion: %d
processIncomingMessageRelay: action %d
handle_NVMAuthFinish: completed
mfi4Auth_protocol_handle_AuthCert: Accessory did NOT provide PrivacyPrefix!
encryptPayload: plaintext: %@
_replyGetNVMKey: !keyStringRef
requestRefreshAccessState: authSession shutting down
AuthSetupFailed: !outMessage
mfi4Auth_protocol_processIncomingMessage: success
firmwareVersionString %@
handle_NVMPublicKeyChallenge: isProgrammed: %d
handle_AuthSetup: auth type fail
AuthChallengeResponse: !authSession
mfi4Auth_protocol_initIdentity error: %d
negoTrans %@
AuthenticationReset: !inMessage
processIncomingMessageRelay: !msgId
(moduleType=%d) index:%@
parseNVMReadResponse: AuthNonce: errorNo
handleNVMWriteResponse: received Nonce
handle_NVMAuthStart: ccsigma_seal error
copyUserPublicKeyForSerialNumber: featureTag: %@
seckey_sign: MFAADeviceIdentityCreateSignature error\n
handle_AuthSetup: unsupported auth version %d
unexpected message
mfi4Auth_protocol_processIncomingMessage: error: %d
(moduleType=%d) %s: AMFDRSealingMapCopyLocalDataForClass returned error=%@
_copyOrCreateUserPublicKeyForSerialNumber: featureTag: %@
decryptIncomingData: !authSession
mfi4Auth_protocol_handle_iAP2RelayRemote: Has no payload !!!, retry after %d ms
handle_NVMEraseResponse: KeyErased: errorNo
decryptIncomingData: decryptPayload rc=%d
CTCompressComputeBufferSize: error: %d, certType %d, cert_resp: (%zu bytes)\n%{coreacc:bytes}.*P>
ccsigma_init: error
%s:%d negotiatedAuthType %d, leafCertLen %zu, leafCertType %d, intermediate1_cert_init_len %zu
(moduleType=%d) moduleAuthService = %d
handleNVMWriteResponse: error
_replyGetNVMKey: !actionKeyCount
handleAuthSessionClose: authSession shutting down
AuthenticationReset: Ignored
processIncomingMessageExtra: non-Extra message id 0x%04x — falling through to relay
mfi4Auth_relay_handle_iAP2RelayRemote: Unknown UserMessage 0x%x
handle_NVMAuthStart: !userKey
_handleNvmReadUserPublicKey: !publicKey
mfi4Auth_protocol_handle_AuthCert: compressedLength:%d
failed to handle auth finish
handle_NVMPublicKeyChallenge: kMfi4Auth_Action_BeginVendorKeyErase
handle_NVMOperationResponse: decryptPayload: error
handle_NVMOperationResponse: encryptPayload: error
_handleNvmReadUserPublicKey: !serialNumberString
RefreshAccessStateResponse: authSession shutting down
mfi4Auth_protocol_validateCertChain: certList %@
copyDeviceIdentityCertificates interval: %f\n
processOutgoingSecureTunnelDataForClient: authSession shuttingDown
%s
AuthChallengeResponse: !inMessage
mfi4Auth_relay_handle_iAP2RelayRemote: msgID 0x%04x, len %zu
mfi4Auth_relay_handle_iAP2RelayRemote: type %d, data %@
iAP2RelaySucceeded: authSession shutting down
parseNVMReadResponse: AuthNonce length: %d
ccsigma_set_signing_function: error
AuthenticationFailed: !inMessage
AuthState: authSession shuttingDown
initSigmaContext: ccsigma_import_signing_key
(moduleType=%d) Error: Could not evaluate certificate
handle_NVMAuthStart: paramID: %d
handle_NVMAuthFinish: A_sig: %@
handle_NVMOperationResponse: paramID: %d
initSigmaContextNvm: !userKey
mfi4Auth_protocol_handle_AuthCert: SecCertificateCreateWithBytes error
AuthenticationSucceeded: !authSession
decryptPayload: key_index: %zu
Have a custom Roswell data structure
(moduleType=%d) authError %d after _signChallenge
handle_NVMPublicKeyChallenge: EraseUserKey: !userPublicKey
processIncomingData: !msgId
failed to handle auth challenge response
initSigmaContext: authSession shutting down
validateCertChain: missing certificate
mfi4Auth_protocol_validateSignature: verification passed
(moduleType=%d) %s: AMFDRSealingMapCopyLocalDataForClass: returned NULL
%s: !inMessage
parseNVMReadResponse: AuthNonce: count
handle_AuthSetup: dhPublicKey %d
(moduleType=%d) done
handle_NVMEraseResponse: paramMask:0x%x
mfi4Auth_protocol_handle_NVMReadResponse: KeyRead
RefreshAccessStateResponse: !authSession
validateSignature: keyRepresentation: %@\n
authError %d after _verifyBatteryMatch
handleNVMWriteResponse: parse failed
handle_NVMAuthFinish: initMessage_RequestNVMPublicKeyChallenge failed: %d
handle_AuthSetup: nego_trans malloc error
Received AuthenticationFailed
validateCertChain: evaluate failed
_mfi4Auth_relay_handle_AccessoryInformationUpdate: finish
%s:%d reached end of parameter (%d bytes), grplen %d\n
handle_NVMPublicKeyChallenge: BeginUserKeyErase: !actionReply
handle_NVMAuthFinish: encryptPayload
initMessage_RequestNVMAuthStart
mfi4 %s = 
initSigmaContextNvm: ccsigma_export_key_share: error
AuthenticationSucceeded: authSession shutting down
Received RefreshAccessStateResponse
validateCertChain: authSession shutting down
mfi4Auth_relay_handle_iAP2RelayRemote: invalid packageDataType!!!
error parsing certificate
processIncomingData: !inMessage
%s: !dhPublicKey
initSigmaContext: ccsigma_set_signing_function
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
handle_NVMEraseResponse: AuthNonce: errorNo
%s: !authKeyValue
userNVMWrite: !authSession
validateCertChain: !certList
error generating signature: auth cp error code %#x\n
mfi4Auth_protocol_handle_AuthCert: SecCertificateGetSubjectKeyID(prodRoot) error
RefreshAccessStateResponse: userNVMReadProtected:%d
mfi4Auth_relay_handle_iAP2RelayRemote: no secureTunnelHandler for type %d !!!
missing outboundSecuredData
%s: unable to allocate outMsg!
handle_NVMAuthFinish: initMessage_RequestNVMOperation failed: %d
handle_NVMEraseResponse: KeyNotErased: errorNo
handle_NVMPublicKeyChallenge: EraseUserKey: _copyOrCreateUserPublicKeyForSerialNumber failed
handle_NVMAuthFinish: A_c1[%d]: %@
handle_AuthSetup: sessionNonce fail
AuthFinish: authSession shutting down
AuthState: !authSession
processIncomingMessageExtra: !authSession
_readSignature %d: %ld.%03llu
handle_NVMAuthStart: initSigmaContextNvm error
convert: accessoryUserName: %s
receiveIncomingData: keepOpen:%d
Received AuthenticationReset
decryptPayload: !inMessage
failed to handle relay remote
setSecureTunnelDataReceiveHandler: !authSession
(moduleType=%d) Error: The component AppleAuthCP was not found, [servicesArray count] is 0
error getting certificate
payload: %@
handle_AuthSetup: initMessage_AuthStart error
%s: paramID: %d
(moduleType=%d) Error: The component AppleAuthCP was not found
(moduleType=%d) %d: %ld.%03llu
parseNVMReadResponse: KeyNotRead:0x%x
mfi4 %@
publicManufacturerNVMRead: !outMessage
RequestRefreshAccessState: !outMessage
decryptPayload: ccsigma_open failed: %d
missing secure tunnel handler
mfi4Auth_protocol_handle_NVMReadResponse: Nonce
publicManufacturerNVMRead: !authSession
mfi4Auth_protocol_handle_RequestAuthCert: CertId failed
AuthCert: !outMessage
error evaluating certificate
authSetupStart: !outMessage
AuthCert: !authSession
RequestAuthChallengeResponse: authSession shutting down
copyUserPublicKeyForSerialNumber: failed
handle_AuthSetup: authSession shutting down
processIncomingMessage: authSession shuttingDown
mfi4Auth_protocol_handle_iAP2RelayRemote: %@
mfi4Auth_util_packIntoTunnelDataiAP2Msg: unable to allocate outMsg!
(moduleType=%d) authError = %d after verifyModuleCertificate
handle_NVMAuthStart: ccsigma_sign: error
initIdentityCerts: !authSession
handle_NVMPublicKeyChallenge: isProgrammed
_extractPublicKey: CFDataGetLength
receiveIncomingData: processIncomingData returned:%d
initIdentity: authSession shutting down
(moduleType=%d) %s: cpGetDeviceIDSN failed: ret=%x len=%zu
IDSN length %zu exceeds buffer
mfi4Auth_protocol_handle_NVMReadResponse: UserPublicKey_NotProgrammed
handle_NVMPublicKeyChallenge: kMfi4Auth_Action_BeginUserKeyErase
PairedToCurrentUser
seckey_sign: error: %d\n
AuthenticationReset: !authSession
RequestAuthSetup: authSession shutting down
_verifySignature %d: %ld.%03llu
authError %d after _signChallenge
handleNVMWriteResponse: unexpected response content
processIncomingMessageExtra: cmd:0x%x  rsp:0x%x
processIncomingMessageRelay: supportedSecureTunnelCapabilitiesMask 0x%llx, processed 0x%llx
iAP2RelayRemote: authSession shutting down
requestRefreshAccessState: !authSession
handle_AuthSetup: Capabilities fail: Too Many!
RequestAuthCert: !inMessage
(moduleType=%d) updateRegistry
(moduleType=%d) %s: %d: returned error
moduleAuthService = %d
parseNVMReadResponse: paramID: %d
handle_NVMAuthStart: !userPublicKey
(moduleType=%d) sleeping for %d seconds before retrying auth
error verifying serial number
handle_NVMEraseResponse: key erased: %x
missing data to send out
mfi4Auth_protocol_handle_AuthCert: compressedLength %d, decompressedLength %zu
AuthenticationFailed: !outMessage
validateSignature: authSession shutting down
Have a match for (t_bpFDRData_v1)
handle_NVMPublicKeyChallenge: paramID: %d
handle_NVMPublicKeyChallenge: !kMFi4_Area51_NVM_User_PublicKey
authSetupStart: !authSession
requestRefreshAccessState: !outMessage
RequestAuthCert: authSession shutting down
mfi4Auth_protocol_handle_AuthCert: validateSignature failed: %d
(moduleType=%d) Error: The component AppleAuthCP was not found, unexpected NULL service
parseNVMWriteResponse: paramID: %d
seckey_sign\n
RequestAuthChallengeResponse: !outMessage
mfi4Auth_protocol_handle_AuthCert: decompress error: failed to allocated %zu bytes
RequestAuthSetup: !authSession
AMFDRSealingMapCopyLocalDataForClass returned error = %@
handle_NVMAuthFinish: ccsigma_open A_c1
mfi4Auth_protocol_handle_AuthCert: iAP2MsgGetDataAsArrayU8 error
RequestRefreshAccessState: authSession shutting down
handle_NVMPublicKeyChallenge: paramID %d exceeds maximum expected value
Failed to decrypt message
%s: !sendOutgoingHandler
userNVMRead: !outMessage
handle_NVMPublicKeyChallenge: BeginUserKeyErase: !isProgrammed
handle_NVMAuthStart: initMessage_RequestNVMAuthFinish error
nvmDhPublicKeyY %@
AuthenticationFailed: !authSession
kMfi4Auth_Action_WriteUserName: count:%d, [0]:0x%x
mfi4Auth_protocol_initIdentity: error:%d
processIncomingMessageRelay: !authSession
mfi4Auth_protocol_handle_iAP2RelayRemote: unable to unpack nested message!!!
CoreAnalytics event: %@\neventDict: %@
handle_NVMPublicKeyChallenge: BeginVendorKeyErase: !actionReply
%s: !values
handle_AuthFinish: initMessage_RequestAuthCert failed
verifyModuleCertificate: evaluate failed
mfi4Auth_protocol_handle_iAP2RelayRemote: invalid unpacket message size(%zu) !!!
UserPublicKey %@
RefreshAccessStateResponse: !inMessage
initMessage_RequestAuthCert: malloc failed
mfi4Auth_protocol_validateCertChain: certListDict %@
%s (certData.length: %lu)
(moduleType=%d) Error: The component AppleAuthCP was not found, servicesArray is NULL
(moduleType=%d) Replying with authPassed = %d, fdrValid = %d, authError = %d
handle_NVMPublicKeyChallenge: !authNonceRef
!sigmaContext
mfi4Auth_protocol_handle_iAP2RelayRemote: msgID 0x%04x, len %d
(moduleType=%d) cpSetTrustStatus failed: 0x%x
handle_NVMEraseResponse: AuthNonce: count
errorNo:%d
mfi4Auth_protocol_validateSignature: !nonceData
handle_NVMEraseResponse: KeyNotErased
RequestAuthChallengeResponse: malloc failed
decryptPayload: plainText: %@
mfi4Auth_protocol_validateSignature: __createCertificateRefWithBytes error
!sigmaContextNvm
authSetupStart: initMessage_RequestAuthSetup failed: %d
mfi4Auth_protocol_handle_AuthCert: certType:%d
validateCertChain: parse failed
handle_NVMPublicKeyChallenge: reply
AuthSetupFailed: !authSession
AuthFinish: !authSession
tryCount = %d (max tries %d)
mfi4Auth_protocol_handle_NVMReadResponse: KeyNotRead
userNVMWrite: initMessage_RequestUserNVMWrite failed: %d
handle_AuthSetup: missing params
RequestAuthChallengeResponse: mismatched auth type
mfi4Auth_util_unpackFromTunnelDataiAP2Msg: Unrecognized message 0x%04X !!!
(moduleType=%d) authError %d after _verifySignature
Sleeping for %d seconds before retrying auth
handle_NVMOperationResponse: paramID %d exceeds maximum expected value
mfi4Auth_protocol_initSigmaContextNvm
authSetupStart: authSession shutting down
mfi4Auth_protocol_handle_AuthCert: SecCertificateGetSubjectKeyID(devRoot) error
mfi4Auth_protocol_initMessage_AuthStart: error %d
initIdentity: !authSession
(moduleType=%d) authError %d after _readCertificate
handle_NVMAuthFinish: ccsigma_verify error: %d
handle_AuthSetup: initMessage_RequestAuthChallengeResponse
processIncomingMessage: !inMessage
initSigmaContext: cert_hash_resp: %@
decryptPayload: !authSession
processIncomingMessageRelay: !inMessage
mfi4Auth_relay_handle_iAP2RelayRemote: failed to parse AccessoryInformationUpdate message!!!
auth length = %ld, sizeof(t_bpFDRData_v1) = %lu, does not match
%s: %d
!rng
_copyOrCreateUserPublicKeyForSerialNumber: failed
processIncomingMessageRelay: override supportedSecureTunnelCapabilitiesMask 0x%llx |= 0x%x
decryptIncomingData: !inMessage
RequestAuthSetup: !outMessage
mfi4Auth_protocol_initSigmaContext: key_share_size != 33
mfi4Auth_protocol_validateSignature: ccsigma_import_peer_verification_key error
modelIdentifierString %@
handle_NVMOperationResponse: initMessage_RequestNVMOperation: error
userNVMRead: !authSession
handle_AuthSetup: cert chain type %d
RequestAuthCert: !authSession
mfi4Auth_protocol_initIdentityCerts: error:%d
processIncomingMessageRelay: cmd:0x%x  rsp:0x%x
processIncomingMessageRelay: error: %d
handle_NVMEraseResponse: key not erased: %x
handleNVMWriteResponse: keys not written
initSigmaContextNvm: key_share_size != 33
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
%s: authSession shuttingDown
%s:%d negotiatedVersion %d, force %d, commandID 0x%04x -> 0x%04x
AuthCert: !inMessage
(moduleType=%d) authCP service %d tmpAuthFlags == 0x%x
decryptIncomingData
decryptPayload: authSession shutting down
_handleNvmReadUserPublicKey: !keyRef
processOutgoingSecureTunnelDataForClient: sendOutgoingData failed
Flags indicate Veridian...do not call cpCopyCertificate()
Created log object %s: %s
(moduleType=%d) authError = eNoDeviceIDSNError after _readDeviceIDSN
handle_AuthSetup: cert chain type fail
encryptPayload: ccsigma_seal: error
processIncomingMessageRelay: initMessage RequestAccessoryInfoUpdate
failed to handle refresh access state response
ccsigma_import_signing_key: error
mfi4Auth_protocol_validateSignature: SecCertificateCopyKey error
processOutgoingSecureTunnelDataForClient: !dataOut
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
handle_NVMEraseResponse: paramID %d exceeds maximum expected value
ccsigma_import_peer_key_share: error
mfi4Auth_protocol_processIncomingMessageExtra: error: %d
%s: secureTunnelType %d
%s: !valuesLength
handle_AuthSetup: unexpected error during param parsing
%s: ForceAuthTimeout/PretendNFCAuthTimeout!!!, ignore status(%d)
AuthStart: ccsigma_seal: error
AuthFinish: !outMessage
decryptPayload: cyphertext: %@
_handleNvmReadUserPublicKey: userPublicKeyMask:%x
handle_NVMPublicKeyChallenge: kMfi4Auth_Action_EraseUserKey
AuthenticationSucceeded: !outMessage
mfi4Auth_protocol_validateSignature: SecKeyCopyExternalRepresentation error: %@
(moduleType=%d) skip component auth
parseNVMReadResponse: paramID: %d, subparam: %d
\n
cfError: 0x%ld
mfi4Auth_protocol_messageHandler_receiveIncomingData: Found no message starting with: %x
AuthStart: ccsigma_sign: error
Returning Roswell data of length %ld
handle_AuthSetup: version fail
mfi4Auth_protocol_handle_AuthCert: memcmp error
mfi4Auth_protocol_handle_AuthCert: validateCertChain failed: %d
invalide secureTunnelType (%d)
iAP2RelayRemote: !inMessage
iAP2RelayFailed: !authSession
error generating signature: %s\n
copyUserPrivateKey: error:%d
encryptOutgoingData: cmd:0x%x
userNVMWrite: authSession shutting down
userNVMRead: authSession shutting down
mfi4Auth_protocol_validateSignature: !signatureData
(moduleType=%d) updateRegistry: cpSetAuthStatus, cpSetTrustStatus
%s:%d reached end of message buffer (%d bytes)\n
%s: !keepOpen
nvmDhPublicKeyX %@
requestRefreshAccessState: initMessage_RequestRefreshAccessState failed: %d
AuthenticationReset: authSession shutting down
RefreshAccessStateResponse: accessState:%d
RequestAuthChallengeResponse: !authSession
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
(moduleType=%d) Cannot find FDR cert
parseNVMWriteResponse: keyWritten: 0x%x
NVMPublicKeyChallenge: WriteUserKey: !userPublicKey
%s: !message
outMessage: !authSession
AuthenticationFailed: authSession shutting down
failed to handle auth success
NVMReadResponse: paramID %d exceeds maximum expected value
parseNVMReadResponse: paramMask:0x%x
NVMReadResponse: !userNameString
handle_NVMAuthFinish: ccsigma_open
PairedToAnotherUser
encryptOutgoingData: !msgId
mfi4Auth_protocol_validateCertChain: errorNo: %d
iAP2RelayRemote: !authSession
handle_AuthSetup: Capabilities fail
RequestAuthCert: !outMessage
failed to handle auth reset
dhPublicKeyInitiator %@
encryptPayload: authSession shutting down
Flags indicate rcam...do not call cpCopyCertificate()
certificate = %@
seckey_sign: challenge: %@\n
mfi4Auth_protocol_handle_AuthCert: decompress size error: %d
CTCompress: error: %d, certType %d, cert_resp: (%zu bytes)\n%{coreacc:bytes}.*P>
initSigmaContext: no signing key
%s: wrong messageID
handle_NVMPublicKeyChallenge: BeginUserKeyErase: !kMFi4_Area51_NVM_User_PublicKey
encryptOutgoingData: encryptPayload rc=%d
RefreshAccessStateResponse: error:%d
processIncomingMessageExtra: !inMessage
encryptPayload: !authSession
%s: !dataIn
RequestAuthStart: !authSession
mfi4Auth_util_packIntoTunnelDataiAP2Msg: unable to allocate outMsg buffer!
(moduleType=%d) cpSetTrustStatusForUI failed: 0x%x
decryptIncomingData: authSession shutting down
encryptOutgoingData: !authSession
handle_AuthSetup: initMessage_RequestAuthStart error
mfi4Auth_protocol_initIdentity(dev) error
mfi4Auth_protocol_initSigmaContext: ccsigma_export_key_share: error
(moduleType=%d) authError %d after _verifyCertificate
handle_NVMEraseResponse: featureTag: %@
NVMReadResponse: %@
handle_NVMAuthFinish: paramID: %d
AuthCert: authSession shutting down
setSecureTunnelDataReceiveHandler: authSession shuttingDown
processOutgoingSecureTunnelDataForClient: !authSession
dataLength matches Roswell data length, return copy of fdr data
handleNVMWriteResponse: !serialNumberString
NotPaired
mfi4Auth_protocol_validateSignature: SecKeyCopyExternalRepresentation error
cpClearCertificate failed: 0x%x
failed to handle auth starat
mfi4Auth_protocol_initSigmaContext: authSession->authStatus:%x devIdentityAllowed:%d
mfi4Auth_util_unpackFromTunnelDataiAP2Msg: message 0x%04X, type %d, unpackedMessage %ld bytes
handle_NVMAuthFinish: Action_EraseUserKey
handle_NVMPublicKeyChallenge: BeginUserKeyErase: !authNonceRef
%s: !outMessage
encryptPayload: cyphertext: %@
ServiceDelegate
NSXPCListenerDelegate
NSObject
ACCUserDefaults
ACCHWComponentAuthServiceParams
ACCHWComponentAuthService
ACCHWComponentAuthServiceProtocol
TB,N,V_authenticatedSession
_batteryCode
errorWithDomain:code:userInfo:
authenticateLASWithChallenge:completionHandler:updateRegistry:componentIndex:
performSelector:withObject:
completionHandler
setSignature:
signTouchControllerChallenge:completionHandler:componentIndex:
authenticatedSession
autorelease
copyPathForPersonalizedData:error:
identityCertificates
resume
debugDescription
displayAuthRefreshAccessState:completionHandler:
_certificateInfo
_closeSessionHandler
certificate
isKindOfClass:
authenticateLASWithChallenge:completionHandler:updateRegistry:
dictionaryWithCapacity:
identityKey
_signChallenge:
_verifyDeviceInfo:
boolValue
displayAuthCloseSession:completionHandler:
setDouble:forKey:
setExportedObject:
T@?,C,V_refreshAccessStateHandler
_challenge
copy
createVeridianNonce:withChallenge:
overrideIdentity
signVeridianChallenge:completionHandler:componentIndex:
_signingHandler
authenticateVeridianWithChallenge:completionHandler:componentIndex:
count
T@\"NSData\",&,N,V_identityCertificates
authenticateVeridianWithChallenge:completionHandler:
countByEnumeratingWithState:objects:count:
dictionaryWithObjects:forKeys:count:
_componentIndex
T@\"NSData\",&,N,V_challenge
allKeys
_certificate
_findAllModuleAuthServices:
authSession
initWithSuiteName:
arrayWithArray:
batteryCode
objectAtIndexedSubscript:
setChallenge:
systemUptime
TQ,R
authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:
createVillanovaNonce:IDSN:challenge:
setInteger:forKey:
_logToAnalytics:authError:fdrValidationStatus:authDurationInMS:
T@\"NSData\",&,N,V_signature
T@?,C,V_openSessionHandler
serviceListener
T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},N,V_identityKey
T#,R
_completionHandler
T@\"NSString\",R,C
_findFDRCertData:forModuleType:withAuthParams:hasDeviceCert:withError:
nvmWriteSessionHandler
setSessionUUIDs:
_openSessionHandler
addEntriesFromDictionary:
arrayForKey:
certificateRaw
hash
sharedDataAccessor
TI,N,V_batteryCode
array
numberWithDouble:
authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:
closeSessionHandler
deviceNonce
displayAuthUserNVMRead:key:completionHandler:
raise:format:
verifyNonceSignature:nonce:signature:
setAuthSession:
_verifyCertificate:
stringWithUTF8String:
T@\"NSData\",&,N,V_deviceNonce
TI,N,V_protocolVersion
authenticateBatteryWithChallenge:completionHandler:
isMFi2_3CertInfo:
_verifySignature:
dataWithBytes:length:
setComponentIndex:
copyParsedCertificateChainInfo:
setDeviceNonce:
_findModuleAuthService:withAuthFlags:componentIndex:
_identityKey
authenticateBatteryWithChallenge:completionHandler:componentIndex:
self
verifyModuleCertificate:forModule:forAuthFlags:forIndex:
numberWithUnsignedLongLong:
setNvmWriteSessionHandler:
sharedDefaultsIapd
T@?,C,V_signingHandler
_verifyBatteryMatch:
_verifyBatteryMatch:outputBatteryCode:
authFlags
isEqual:
nvmReadSessionHandler
setRefreshAccessStateHandler:
verifyBatteryMatch:completionHandler:
_certificateRaw
sharedDefaultsLogging
signRCAMChallenge:completionHandler:
signingHandler
stringForKey:
T@\"NSMutableDictionary\",&,V_sessionUUIDs
challenge
setIdentityKey:
setCompletionHandler:
superclass
_refreshAccessStateHandler
_validateDeviceAndFDRCert:forModuleType:withAuthParams:
authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:
dictionaryForKey:
setCertificateInfo:
signRCAMChallenge:completionHandler:componentIndex:
TB,N,V_skipComms
T^{mfi4AuthProtocolSession_s=},V_authSession
setIdentityCertificates:
setProtocolVersion:
release
_protocolVersion
description
interfaceWithProtocol:
listener:shouldAcceptNewConnection:
performSelector:
retain
setCertificateRaw:
_nvmWriteSessionHandler
init
setOpenSessionHandler:
numberWithBool:
setCertificate:
isEqualToData:
isEqualToNumber:
skipComms
setDelegate:
charValue
class
date
numberWithUnsignedInt:
stringWithFormat:
_authenticatedSession
retainCount
setObject:forKeyedSubscript:
setModuleAuthService:
T@?,C,V_completionHandler
isProxy
_verifyModuleFDR:forModuleType:
dataWithContentsOfFile:
setAuthenticatedSession:
authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:
bytes
isMemberOfClass:
refreshAccessStateHandler
T@?,C,V_nvmReadSessionHandler
_authSession
conformsToProtocol:
moduleAuthService
_overrideIdentity
isEqualToString:
T@\"NSDictionary\",&,N,V_certificateInfo
dealloc
_authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:
getBytes:length:
T@?,C,V_closeSessionHandler
_signature
respondsToSelector:
boolForKey:
copyEvaluatedCertificateChainInfo:
_readSignature:
.cxx_destruct
displayAuthUserNVMWrite:key:value:completionHandler:
setObject:forKey:
T@\"NSNumber\",&,N,V_componentIndex
protocolVersion
_validateWithFDRCertificate:forModuleType:withAuthParams:
setAuthFlags:
TI,N,V_moduleAuthService
_signChallengeForModuleType:challenge:componentIndex:completionHandler:
length
integerForKey:
signVeridianChallenge:completionHandler:
_authFlags
openSessionHandler
zone
authenticateTouchControllerWithChallenge:completionHandler:
numberWithUnsignedShort:
sessionUUIDs
_moduleAuthService
addObject:
doubleForKey:
isComponentCertInfo:
processInfo
timeIntervalSince1970
TB,N,V_overrideIdentity
TI,N,V_authFlags
_sessionUUIDs
performSelector:withObject:withObject:
unsignedShortValue
T@\"NSString\",?,R,C
_nvmReadSessionHandler
_readDeviceIDSN:
sharedDefaults
verifyModuleCertificate:forModule:forAuthFlags:
_readCertificate:
arrayWithCapacity:
copyParsedCertificateChainInfoFromCerts:assumeType:
setCloseSessionHandler:
_deviceNonce
authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:componentIndex:
objectForKey:
setExportedInterface:
setNvmReadSessionHandler:
setBatteryCode:
dictionaryWithDictionary:
getTouchControllerQueue
sharedManager
signature
unsignedIntegerValue
T@\"NSData\",&,N,V_certificateRaw
setSigningHandler:
T@?,C,V_nvmWriteSessionHandler
_notifyComponentAuthFailure
_skipComms
componentIndex
displayAuthOpenSession:intermediateCertificate:keyData:completionHandler:
setSkipComms:
unsignedIntValue
certificateInfo
setOverrideIdentity:
authenticateRCAMWithChallenge:completionHandler:updateRegistry:
T@\"NSData\",&,N,V_certificate
_identityCertificates
v40@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSData\"i>24@\"NSNumber\"32
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@0:8
@?16@0:8
I36@0:8i16^I20@28
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}
i52@0:8^@16i24@28^B36^^{__CFError}44
v44@0:8i16@20@28@?36
v32@0:8@\"NSData\"16@?<v@?i>24
^{mfi4AuthProtocolSession_s=}
v36@0:8@16S24@?28
v56@0:8@16@?24i32B36B40B44@48
Q16@0:8
B32@0:8@16@24
v20@0:8B16
v24@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16
I
@\"NSMutableDictionary\"
v32@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24
v44@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24B32@\"NSNumber\"36
v24@0:8@16
^{mfi4AuthProtocolSession_s=}16@0:8
B
v36@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24B32
I16@0:8
@40@0:8:16@24@32
@20@0:8i16
@32@0:8:16@24
B24@0:8@\"Protocol\"16
v16@0:8
@\"NSData\"
B28@0:8@16i24
B16@0:8
i24@0:8@16
v48@0:8@16@24@32@?40
B24@0:8@16
@16@0:8
B24@0:8:16
^{_NSZone=}16@0:8
v24@0:8^{mfi4AuthProtocolSession_s=}16
v24@0:8@?16
@?
v44@0:8@16@?24B32B36B40
v52@0:8@16@?24B32B36B40@44
@24@0:8:16
@\"NSNumber\"
i36@0:8@16i24@28
v44@0:8@16S24@28@?36
v40@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24@\"NSNumber\"32
v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSData\"i>24
B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24
v52@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24B32B36B40@\"NSNumber\"44
Vv16@0:8
@\"NSString\"16@0:8
v20@0:8I16
v44@0:8@16@?24B32@36
#16@0:8
B24@0:8#16
@\"NSDictionary\"
v32@0:8@16@?24
v40@0:8@16@?24@32
v36@0:8@16@?24B32
v44@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24B32B36B40
B20@0:8I16
i32@0:8@16^S24
v36@0:8i16i20i24Q28
```
