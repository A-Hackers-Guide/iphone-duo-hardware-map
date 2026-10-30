# `/usr/lib/libVinylNonUpdater.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 983,808 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 37 (Size: 3704)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (20)

- `/usr/lib/libVinylNonUpdater.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/AppleBasebandLink.framework/AppleBasebandLink (compatibility version 1.0.0, current version 0.0.0, weak)`
- `/System/Library/PrivateFrameworks/AppleMipcRouter.framework/AppleMipcRouter (compatibility version 1.0.0, current version 0.0.0, weak)`
- `/usr/lib/libMIPCSdk.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libFDR.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libHDLCDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libReverseProxyDevice.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libBBUpdaterDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libARI.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libKTLDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyCapabilities.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libETLDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libPCITransport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyBasebandDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (1,411)

```
%s: (%s:%d) Range assignment too large(%p), got(%ld) max(%ld)
%s: (%s:%d) Array assignment too large(%p), got(%zu) max(%zu)
HandleInstallationResult
Successfully created mapMetaDataPayLoad (%zu bytes)\n
bpp.get()
Performing ManagePairingGetNonce\n
VinylCommunication
VinylEURCommunication
Failed to assign response data\n
ECID
misc
Power up SE successful.\n
Failed to Refurb: %d\n
sending ConfigId Request
InitPersoDevice %d\n
Status_Req sent: Msg=0x%x fTlv_Mode = %s\n
VinylRefurbOption
DELETE_NOTIFICATION_STATUS_OK == del_status
decode_pfk_bulk_entry
Client rsp data buffer is not valid\n
Failed to FinalizePerso status %d SW1_SW2 0x%x\n
Failed to stop router server due to timeout\n
InstallPairingMSM Sep_Cmd_Cnf received: Msg=0x%x fTlv_Result = %s\n
internalBuild         
: 
EscrowTokenPeriod
{:02x}
-c
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Options/eUICCOptions.cpp
AppleKeyStore
2
ManagePairingGetNonce Sep_Cmd_Cnf failed, result 0x%x\n
ret
Timeout waiting for confirmation on Cmd Req Delete Profile.\n
/Managed Preferences/mobile
InitPersoServerResponse.plist
respDataPayload
result %d code %d raw_error %ld error %s\n
\n
Store data Cmd_Ind not successful, result 0x%x\n
VinylSkipAll
DR_Success == DERDecodeSeqContentInit(&decoded.content, &seq)
deviceSerialNumber && deviceSerialNumber.get()
Failed to handle Refurb operation, ret %d\n
kToBeSignedPayload
DR_Success == der_ret
Received payload length (%d) is smaller than required size (%d)\n
Assertion failure ( nullptr == fTransportCreated && \"Telephony transport error.\" )
postresetdelay
/Library/MedicalID
SwitchCardMode: Baseband already in mode %hhu\n
rsp.Valid()
response->contents.cmd_rsp_token == resultTo1stCommand.cmd_rsp_token && response->contents.status == VinylError::kStatusSuccess
getDataRsp.Valid()
deviceUDIDData != nullptr
kBBUReturnProtocolError
/Library/terminus
geteUUID: Failed to decode eUUID from response\n
Failed to get data from UIM\n
INVALID_PARAM
GetNonceServer %d\n
Failed to create responseNonceFromServers CF Object\n
kBBUReturnDSPImageError
(snipped)
kVinylRadioType
SIM still initializing, trying again... IBIVinylResult 0x%x (retryCount: %d, retryLimit: %d)\n
CreateValidationBlob DR %d\n
Invalid Refurb Option %s
eUUID provisioning failed: BCOM profile(s) found on device.\nTo resolve: Remove all BCOM profiles and retry provisioning.\nSee BCOM Profilelist payload below for details.\n
failed to convert dictionary to Plist for Nonce response from Server\n
/Library/BackBoard
file: %s %i\n
euiccSignature
euicceumCertificate
Router server stopped.\n
kBBUReturnBBInitStatusTimeout
/iomfb_bics_daemon
/Library/DeviceRegistry.dontBackUp
outData.contents.isAbsentOk
hash %s\n
basic_string
HardwareType
No router server available.. bail out\n
Auth_Perso_Req not successful, result 0x%x
ConfigId Provisioning Operation is Success\n
cmd
Failed to LpaSigningRequest status %d SW1_SW2 0x%x rsp_len %u\n
(kBBUReturnSuccess == ret) && (sw == 0x9000)
euiccSignedLPAData:: \n
DR_Success == derRet
VinylClearMetadata::GetListOfIccids: Extracting Profile List\n
CFGetTypeID( ps ) == CFStringGetTypeID()
kBBUReturnGetMEIDFailure
/dev/null
Force collecting BB coredump by return error = %d, previous ret = %d\n
ind.fTlv_Result && *ind.fTlv_Result == mipc::MIPC_DALE_VINYL_CMD_RESULT_SUCCESS
GetBpp
failed to create euiccSig CF Object\n
ff_first_stage
recv
/.overprovisioning_file
/Library/NanoPreferencesSync
Failed to allocate shared info dict\n
Failed to complete InitPerso command\n
NfRestoreSEClose
Skip Vinyl provisioning\n
kBBUReturnNVMImageError
/run
/Library/SMS
CLASS A
Functionality not implemented.\n
VinylPollResult
values
v12@?0i8
debugArgs             
failed to create euiccCertificate CF Object\n
kBBUReturnFailCreateTransportInitial
kBBUReturnFusingInstructionMissing
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/CommandDrivers/eUICCCommon.cpp
0B
TransactionID
kBBUReturnServerError
/Library/NanoTimeKit
akstest_new_ek
Perso Only can only be performed with kVinylOperationNonUpdate\n
DR_Success == der_ret && TAG_EUUID == dec.tag && LENGTH_TAG_EUUID == dec.content.length
Auth_Perso_Req sent: Msg=0x%x fTlv_Payload = %s\n
End of input while parsing format specifier precision
kBBUReturnPingFailed
::
(snipped)\n
xporttimeout
Failed to perform LPASigning Request status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
Sticky session: X-Apple-Alder-IP = %s\n
Sep_Cmd_Ind Cmd_id %u should have fTlv_Nonce\n
DR_Success == DERDecodeSeqContentInit(&dec.content, &seq)
reg
Store data Cmd_Req returned error[%s].\n
EuiccCommandID
DR_Success == der_ret && TAG_PIR == dec.tag
(DR_Success == ret)
kBBUReturnInternalError
Failed to handle configId Provisioning : %d\n
Payload too large -- payload_size: %d  max allowed: %lu)\n
VinylCommunication::create
ind.fTlv_Cmd_Id
The type does not fit in the mask
Assertion failure ( nullptr != fTransportCreated && \"Telephony Util transport error!\\n\" )
forceGold             
success
outPlist
kVinylResultSuccess == handle_result_ret
/Library/AggregateDictionary
/Documents/Pearl
/Library/ManagedAssets
status
kVinylResultSuccess == vinyl_ret && isBootStrapAlreadyInstalled
Send LPA Command to eUICC Failed \n
kBBUReturnRawBinaryImageError
kBBUReturnAPTicketMallocFailed
aks-client-queue
(ret == DR_Success)
ValidatePersoDevice %d\n
Router server was not instantiated by VinylRestore to start it.\n
Status_Cnf returned error[%s].\n
Failed to get valid LPA Signed response from the eUICC\n
/Library/SoftwareUpdate
GetaData() output not valid and isAbsentOK = true. However, device doesn't support SEPPairing, no further non-update operation.\n
Fail to ResetCard\n
Missing or empty server sssion?! %s\n
sizeof(resultTo1stCommand) == HDLCFrameGetPayloadLength(&rsp)
 TelephonyBasebandPCITransportCreate returns: %s\n
kBBUReturnLoaderVersionError
/Library/Cookies
operation == kVinylOperationNonUpdate
Client rsp data is not valid\n
Failed to GetEID but it is fine because BB Provisioning not enabled or it is enabled but Vinyl Provisioning Skipped\n
profile returned with presence check on, returning success\n
/mnt5
kBBUReturnFileMismatch
kBBUReturnFailCreateTransportSecond
kBBUReturnBBTicketDERParseErrorForFATPCal
isLETOCapable: hwIdSimConfig[3]=%d, capable=%s\n
ManagePairingGetNonce Sep_Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s\n
transport %p, status: %d\n
BPPMetaData
/mnt3
kBBUReturnBBTicketMallocFailed
/logs/BurnIn
%s:%spid:%d,%s:%s%s%s%s%s%u:%s bad 1%s\n
check failed: %s, %d, assertion: %s\n
No valid GetData found and trying to reset Vinyl.\n
.
infnanINFNAN
BasebandUpdater
dict
kBBUReturnGetICCIDFailure
/root/Library
Fail to create transport: %d\n
In VINYL_OPERATION_BOOTSTRAP_PROVISIONING\n
Personalized
assign
cardData.Valid()
GetWrapKeyServerRequest.plist
Finalize_Perso_Cnf returned error[%s].\n
kBBUReturnInvalidTransportType
Try to copy the BB coredump from %s\n
kBBUReturnSuccess == ret && !dataBuffer.empty()
SIM status req failed even after several retries.\n
postProcess           
No profile returned with presence check on, device already has a two-phase bootstrap profile installed\n
failed to create deviceSerialNumber CF Object\n
Invalid ECID received\n
Payload too large -- payload_size: %zu exceeds uint16_t maximum\n
Failed to ManagePairingGetNonce result %d SW1_SW2 0x%x\n
ind.fTlv_Nonce.get()
ManagePairingGetNonce Sep_Cmd_Cnf has no fTlv_Result\n
client rsp data: %s\n
kBBUReturnBadArgument
kBBUReturnNAKManifest
/Media/iTunes_Control
Condition <<%s>> failed %s %s/%d\n
0x{:02x}
Assertion failure ( lib != __null && \"Could not find /usr/lib/libnfrestore.dylib\" )
wheel
/Library/ISP
Failed to get nonce\n
main_fw_pcf_mac 0x%s gold_fw_pcf_mac 0x%s pcf_version 0x%x\n
alternate form
DR_Success == DERDecodeSeqContentInit(&content, &seq)
TwoPhaseProv::IsNotificationSentRspSuccess(euicc_rsp)
/logs/AppleSupport
Skipping free of external transport\n
Creating sequence using Key, Value pair failed\n
Successfully created LPASigningRequest (%zu bytes)\n
0123456789ABCDEF
/.fseventsd
akstest_last_user
kBBUReturnKeysNotAligned
/vm
Yes
Empty payload data received\n
mipc::MIPC_SIM_STATUS_CARD_REBOOT
Getdata_Cnf returned error[%s].\n
Vinyl Operation: %d, lastOperation: %d\n
DR_Success == DERDecodeSeqContentInit(&pbi_der, &seq)
(kVinylResultSuccess == result) && (configId.size() == LENGTH_OF_CONFIGID)
kBBUReturnBadChecksum
GET_RSP_FIELD(rsp, cfg_req_t4) == IBI_NC_CFG_REQ_CONFIG_ID
eUICCPublicKey
/mnt4/wireless/Library/Logs/CrashReporter/Vinyl/Baseband/baseband_updater_logs/
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/NonUpdate/VinylRouterClient.cpp
IOService:/IOResources/AppleKeyStoreTest
MSMData
nullptr == sessionData.getError().get()
0x{:04x}
configId
/Library/Fonts
kBBUReturnDBLImageError
/.ssh
akstest_rewrap_ek
%s:%spid:%d,%s:%s%s%s%s%s%u:%s fail%s\n
In VINYL_OPERATION_REFURB\n
ret %d records %zu\n
kBBUReturnEOF
kBBUReturnGetBootupTimeError
Unable to get EID\n
(%s:%d) Array assignment too large(%p), got(%zu) max(%zu)
com.apple.telephony.control-msg.xpc.allow
EXIT:\n
hl:C:v:x:t:r:p:e:c:w:i:s:fUFD:nHSqPV
kVinylEID
01
NEW
bbupdater: %s
kBBUReturnBBTicketReadContentFailed
aks_fv_unwrap_vek_with_acm
Performing SEP-eUICC pairing authentication %d/%d\n
configIdProvURL             
der_ret == DR_EndOfSequence
kBBUReturnGetKeyStatusFailure
/logs
In VINYL_OPERATION_CONFIGID_PROVISIONING\n
GetSimMuxCfg: current sim_cfg=%d\n
sign
eUICCSEPVerifyPairing     
failed to create EID CF Object\n
DR_Success == der_ret && TAG_IMSI == dec.tag && SIZE_OF_BCOM_IMSI == dec.content.length
Creating mapMetaData SEQUENCE with %ld key-value pairs\n
Failed to convert key to UTF8 at index %ld\n
VinylSkipOperationOnSEPFail
kBBUReturnFatalError
Error: only kTelephonyRadioVendorINT has IBIVinylSimCardResetReq, current RadioVendor = %d\n
TAG_GPS == dec.tag
rsp.Valid() && rsp.contents.rsp_len
In VINYL_OPERATION_GET_PAIRING_PARAMS\n
FinalizePersoDevice %d\n
Creating with timeout set to %u ms\n
GetNonceServerResponse.plist
/Library/Assistant
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 3)%s\n
VinylTwoPhaseProvSessionData
 -- middle of buffer snipped -- \n
kAKSReturnSuccess == auth_ret
SwitchSimMuxCfgPolled: request rejected, result=%s(%d)\n
DR_Success == der_ret && TwoPhaseProv::TAG_RNLR_NL == dec.tag
count > 0
coreDumpPath
operationRequested(operation, eUICCoptions)
Card already perso'ed\n
refurbAction: %d\n
Authentication with card failed\n
(der_ret == DR_Success)
Failed to complete FinalizePerso command\n
The format specifier contains malformed Unicode characters
All Preferences
SwitchSimMuxCfgPolled: MUX settled to wrong config, current=%d expected=%d\n
01234567
IsNotificationSentRspSuccess( euicc_rsp )
failed to create signing dict\n
VinylClearMetadata
inRestoreOS: %d\n
/log/com.apple.xpc.launchd
daemon
But the BB coredump dir is empty.\n
Performing SetCardMode(kOpModeNormal)\n
fs == std::future_status::ready
link.accepter.local
Sep_Cmd_Ind failed, status word from UICC sw 0x%hx\n
forceMain             
responseNonceFromServer != nullptr
/Library/Calendar
Failed to install MSM: %d\n
mipc::MIPC_SIM_STATUS_SEP_AUTH_STALLED
InstallPairingMSM Sep_Cmd_Cnf has no fTlv_Result\n
failed to create eUUID CF Object\n
/Library/CountryBundles
infoSharedRef
VinylRestore Options:\n%s\n
euicceumCertificate:: \n
Couldn't get response payload %s\n
Validate_Perso_Req not successful, result 0x%x\n
Failed to convert string value to UTF8 at index %ld\n
Could not find NVRAM via IOKit\n
kBBUReturnNAKHello
Cleaning up VinylController object \n
kVinylSIMSKU
Failed to InitPerso status %d SW1_SW2 0x%x rsp_len %u\n
mipc::MIPC_SIM_STATUS_EMPT_EUICC
skipOperationOnSEPfail
Failed to encode final mapMetaData SEQUENCE\n
kBBUReturnFSMNoTransitionDefined
/backup
Signing payload dictionary not present in the input dictionary\n
!(GET_RSP_FIELD(rsp, sim_error_cause_t28) & sim_error_cause_mask)
DR_Success == der_ret && TAG_DP_RESULT == dec.tag
kBBUReturnBootedForCoreDump
pargs
/.exclave
/Library/Caches
%s:%spid:%d,%s:%s%s%s%s%s%u:%s count %llu exceeds max %u%s\n
In GetParametersDummy\n
The numeric value of the format specifier is too large
uimSlot               
Assertion failure ( pfnNfRestoreSEClose != __null && \"Could not find NfRestoreSEClose symbol\\n\" )
failed to create eumCertificate CF Object\n
CLASS C
!GET_RSP_FIELD(rsp, result_t4)
transport %p, status: %#x\n
gps_req.get()
BCOM Delete notification found\n
/Library/ConfigurationProfiles
com.apple.router.abb
Sep_Cmd_Ind received: Msg=%04x fTlv_Cmd_Id = %s fTlv_Result = %s fTlv_Sw = %s fTlv_Nonce = %s\n
/usr/lib/libnfrestore.dylib
ENTER: %s\n
/Library/CoreBrightness
could not open file: %s (%s)\n
eUICCVinylFactory
1
Unhandled radio(%d) type or no radio\n
VinylForceMain
DR_Success == der_ret && TAG_LN == dec.tag
failed to parse LPA signed data\n
v8@?0
eUICCVinylData cache is valid. Using cached data!\n
fSe
SwitchModeReq result 0x%x sw1_sw2 0x%hx\n
eumCertificate:: \n
Failed to assign output data\n
Timeout waiting for confirmation on Init Perso Req.\n
mipc::MIPC_SIM_STATUS_PH_NETSUB_PIN
decodeConfigIdFromResponse: ConfigID not present in response (found tag=0x%02llx instead of configIDValue), exiting\n
Unknown sim status
0x{:08x}
ldr ver %04X not eligible, skipping\n
 formatting argument
a pointer
kBBUReturnAborted
kBBUReturnInvalidBBUStageError
kPSIM1_PSIM2
kBBUReturnInitializerPrepError
kBBUReturnEBLImageError
mobile
CLASS B
CLASS D
successCnf
0b
DR_Success == DERDecodeSeqNext(&seq, &dec)
CFGetTypeID( cmd ) == CFStringGetTypeID()
Failed to ManagePairingGetNonce status %d\n
decodeConfigIdFromResponse: Invalid input parameters\n
ManagePairingAuthenticate Sep_Cmd_Cnf received: Msg=0x%x fTlv_Result = %s\n
BPP
kBBUReturnGetCarrierIDFailure
kBBUReturnInvalidProgrammerItemType
kBBUReturnMDMDDRImageError
MSMVectorBlob %s\n
eUUIDdata != nullptr
VinylDaleCommunication
mipc::MIPC_SIM_STATUS_COMPLETE_READY
eUICC not stuffed but that's ok!\n
StringRef.h
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/NonUpdate/VinylConfigIdProv.cpp
/Library/ApplePushService
kNonce
matched refurb profileReference\n
(ret == DR_Success) && (er_decoded.bppCommandId.length > 0) && (er_decoded.errorReason.length == 1)
fRouterServer
EID not eligible, skipping\n
Could not load NVRAM? %d\n
verbosity
%u.%03u: %s: %s
Failed to correct SW during config Id fetch 0x%04x\n
ProfileStatus
BB reset successful\n
LogDirectory
%s%s\n
IOService:/IOResources/AppleKeyStore
SIM still initializing, trying again... sim_state 0x%x (retryCount: %d, retryLimit: %d)\n
Fail to SetCardMode(kOpModeRestore)\n
Router server eror: %s\n
tag_props[seg].optional || tag_props[seg].topLevelTag == decoded.tag
VinylConfigIdProv::Perform\n
Server response received after sending SerialNumber and Device UUID\n
eUICCVinylICEValve
eumCertificate
v24@?0i8^v12I20
VinylProvisioningURL
eUICC feed containing signed LPA data sent to server successfully\n
GetSIMSKUID error %d status 0x%hhx\n
0
%@
kBBUReturnSuccess
/Library/DeviceRegistry
In VINYL_OPERATION_GET_INFO\n
UTF8 string encoding for key failed\n
outData
Init_Perso_Cnf returned error[%s].\n
Return 16 byte zero EID as pairing identifier\n
options && !options->twoPhaseRefurbRef.empty()
kBBUReturnFusingSourceError
!nonce.empty()
To be signed dictionary is NULL\n
Deserialized plist data is not a dictionary: %s\n
kBBUReturnGetEIDFailure
kBBUReturnAPTicketReadContentFailed
The value of the argument index exceeds its maximum value
NVRAM: %s\n
Switch_Mode_Req sent: Msg=0x%x fTlv_Is_Reset_Req = %s\n
ManagePairingAuthenticate Sep_Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Signed_Auth = %s fTlv_Nonce = %s\n
 does not allow the 
DR_EndOfSequence == der_ret
GetData status is not valid, hardware does not have eSIM, set absentOk to True\n
Failed to serialize dictionary %s error %s\n
ErrorCode
Failed to encode KeyValuePair sequence at index %ld\n
/root/Library/MobileContainerManager
And found the BB coredump already collected, don't need to trigger collection again. Now return error = %d, previous ret = %d\n
eidValue
performCoreDump
kBBUReturnGetSerialNumberFailure
error %d status %u sw1_sw2 0x%x\n
SIM status: %s(%d).\n
The type option contains an invalid value for 
kBBUReturnSysctlError
returning VinylController::create\n
ManagePairingGetNonce succeed\n
Timeout waiting for indication on ManagePairingAuthenticate Sep_Cmd_Req\n
call with %p different from fTransportCreated(%p)\n
metaDictRef is empty\n
Invalid key or value at index %ld\n
/Managed Preferences
vector
Null rsp dictionary reference passed\n
Failed to get PRP\n
Timeout waiting for indication on ManagePairingGetNonce Sep_Cmd_Req\n
a bool
IsProvTxIdAvailable( euicc_rsp )
quitbootrom
<var>
ManagePairingGetNonce Sep_Cmd_Cnf received: Msg=0x%x fTlv_Result = %s\n
LPA Signed Data to be sent to server in hex format\n
kBBUReturnFileNotFound
aks_kext_set_options
failed to open userclient via %s: %d\n
TelephonyRadiosGetRadioVendor %d not supported!
(%s:%d) Range assignment too large(%p), got(%ld) max(%ld)
future.get()
Validate_Perso_Req sent: Msg=0x%x fTlv_Payload = %s\n
In ManagePairingGetNonce...\n
 (skip)
hwType.Valid()
mipc::MIPC_SIM_STATUS_SIM_PUK2
No Action
LdrVerSupportsTwoPhaseInstall(ldr_ver)
kBBUReturnFailedCreateController
/Media/Downloads
To be signed dictionary is empty\n
twoPhaseRefurbRef     
ProfileInstallationResult
VinylClearMetadata::GetListOfIccids: Successfully populated ICCID list!\n
/Library/MediaStream
/Library/Trial
Failed to correct response %d\n
euiccCertificate
VinylVerifyPairing
pfnNfRestoreOpenWithSE failure, outResult: %d\n
failed to convert deviceSerialNumber to CFData\n
kBBUReturnNeedsMoreInput
/networkd
mipc::MIPC_SIM_STATUS_PH_SP_PIN
Send Command of eUICC Feed to Marina Server Failed\n
Send Notification command to eUICC failed\n
kBBUReturnFailedFinishProvisioning
loader_version 0x%s key_id 0x%s perso %d\n
eidValue:: \n
w
geteUUID: Sending GetEuiccDataRequest\n
ManagePairingAuthenticate input nonce size = %zu, should be %d\n
The fill option contains an invalid value
0123456789abcdefghijklmnopqrstuvwxyz
(ret == DR_Success) && (sm_decoded.eid.length > 0) && (sm_decoded.transactionId.length > 0)
kBBUReturnGetManifestStatusFailed
kBBUReturnFusingVerificationFailed
ignoremanifest
/Library/MobileInstallation
chip_id 0x%x stream_apdu_max_apdus 0x%x isAbsentOk: %s\n
Failed to encode ECID\n
Assertion failure ( nullptr != fTransportCreated && \"Telephony util transport error.\" )
APIVersion
DR_Success == der_ret && top_level_tag == dec.tag
result == kVinylResultSuccess
kBBUReturnTelephonyUtilReadError
skip_fusing_validation
Fail to SetCardMode(kOpModeNormal)\n
AuthenticatePersoDeviceRequest.bin
ind.fTlv_Sw && *ind.fTlv_Sw == 0x9000
kBBUReturnTooManyRetry
module_verbosity
send
/Library/CallHistoryDB
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEK failed with 0x%x%s\n
GET_RSP_FIELD(rsp, sw1_sw2_t6) == 0x9000
Still persod after force?\n
DR_Success == der_ret && TAG_PI == dec.tag
sessionData.isEidEligible( performOptions )
kBBUReturnError
_networkd
/Library/Mail
AuthenticatePersoDevice %d\n
VinylPairingAuthTest
DR_Success == DERParseInteger(&dec_nested.content, &err_val)
/Library/UserConfigurationProfiles
/Library/BulletinBoard
IODeviceTree:/filesystems
user allow list:
decode_pfk_bulk_data
Minimal sealing manifest fetch failed %s\n
Octect string encoding for value failed\n
metaDictRef is null\n
VinylClearMetadata::GetListOfIccids: Requesting Profile List\n
kBBUReturnInvalidRadioType
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestLastUser failed with 0x%x%s\n
Failed to DeleteProfile status %d SW1_SW2 0x%x\n
sepIndSuccess_
ECID: 0x%llx\n
eUICCPublicKey:: \n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/SecureElement/VinylSecureElement.cpp
((operation >= kVinylOperationGetEid) && (operation < kVinylOperationNone))
failed to create deviceSerialNumber\n
kBBUReturnELF32HeaderError
router.server
mipc::MIPC_SIM_STATUS_PH_SIM_PIN
Finalize_Perso_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s\n
BBUpdater
BBUCommon
/Library/DeviceRegistry.state
a floating-point
EuiccSessionID
/root/Library/Logs
aks_internal_state
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/CommandDrivers/eUICCVinylMAVValve.cpp
resetting refurb fw with perso supported in an attempt to clear perso\n
ntf
DataRoot
ManagePairingAuthenticate succeed\n
Vinyl Secure Element object not created, cannot power up SE\n
link accepted failed. t\n
eUICC not enabled, aborted!\n
kBBUReturnARTMismatchedError
Performing SetCardMode(kOpModeRestore)\n
PersoImpl
Creating transport:%p \n
%s\n
kBBUReturnModemPowercycleError
/root/Library/Caches
SubmitEUICCDataFeed
step
Failed to StoreData status %hhu SW1 0x%x SW2 0x%x\n
decodeConfigIdFromResponse: Unexpected outer CHOICE tag 0x%02llx\n
parameterCount > 0
Failed to create dictionary\n
true
ResponseDataFlag
cmdId == mipc::MIPC_DALE_VINYL_SEP_CMD_GET_NONCE || cmdId == mipc::MIPC_DALE_VINYL_SEP_CMD_AUTHENTICATE || cmdId == mipc::MIPC_DALE_VINYL_SEP_CMD_INSTALL
kVinylResultSuccess == result
performBootup
fakefuse
AuthenticatePersoDeviceResponse.bin
ManagePairingAuthenticate input nonce is empty\n
Encoded KeyValuePair %ld: key='%s', value type=%ld\n
kBBUReturnProgrammerConnectionError
root
AppleKeyStoreTest
fCommunication object not created, cannot free Transport\n
BUSY
mipc::MIPC_SIM_STATUS_PH_SP_PUK
 option
BPPRequestData
DR_Success == der_ret && TAG_NS == dec.tag
!getDataRsp.contents.isAbsentOk
%u.%03u: %s: %u%s\n
VinylController
Serialization error
Server URL Not present\n
/Keychains
%lld,%d\n
Failed to InitPerso status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
Failed to complete AuthPerso command\n
SendReceiptServerRequest.plist
Auth_Perso_Cnf returned error[%s].\n
00000000000000000000000000000000
kBBUReturnIOError
kBBUReturnFusingError
/Library/FrontBoard
decodeConfigIdFromResponse: Found auditResponseOk\n
key != nullptr && value != nullptr
kBBUReturnFusingSECELFFailed
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unpack data failed%s\n
mipc_client_started
locale-specific form
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Support/BBUCommon.cpp
logmask
handle_signals
entering VinylController::create\n
No
Integral value outside the range of the char type
onlyPerso             
SystemRoot
Yes :-)
/Library/IdentityServices
kPSIM1
eUICCVinylValve
VinylSkipProvisioning
accepted
/root
aks_delete_xart_leak
ManagePairingGetNonce returning success\n
Router server was not instantiated by VinylRestore to stop it.\n
Getdata_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Is_Not_Personalized = %s fTlv_Sw = %s fTlv_Chip_Id = %s fTlv_Eid = %s\n
DR_Success == der_ret && TAG_PIL_ICCID == iccid_dec.tag
TAG_SEQN == dec.tag
kBBUReturnManifestStatusNonZeroError
/Library/NanoBackup
aks_kext_get_options
eUICCVinylMAVValve::ResetCard not supported\n
/Library/mad
response.hwSetRsp == MgrSetSIMHWSetResultType::kSuccess
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Communication/Eureka/VinylEURCommunication.cpp
deviceSerialNumberData != nullptr
/Library/NFStorage
ManagePairingAuthenticate input signed auth size = %zu, should < %d\n
Sep_Cmd_Ind Cmd_Id %u not supported\n
mipc::MIPC_SIM_STATUS_PH_NETSUB_PUK
Store data Cmd_Ind received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s fTlv_Payload = %s\n
precision
could not create file: %s (%s)\n
getConfigId: StoreData failed with result %d, sw=0x%04x\n
IBIVinylSimCardResetRspCb result 0x%x\n
@
GetData IBIVinylResult 0x%x\n
ManagePairingAuthenticate Sep_Cmd_Cnf fail\n
Switch_Mode_Req returned error[%s].\n
/db
rsp_data
InitPersoDeviceResponse.bin
v24@?0{shared_ptr<ctu::Http::HttpResponse>=^{HttpResponse}^{__shared_weak_count}}8
Bootstrap
twoPhaseUrl           
%s:\n\tNum files:\t%u,\n\tNum hardlinks:\t%u,\n\tNum compressed:\t%u,\n\tTotal Size:\t%lld,\n\tMin File Size:\t%lld,\n\tMax File Size:\t%lld,\n
outData.Valid()
Failed to verify pairing with status %d, fail the restore \n
InitPersoDeviceBlob.bin
VinylTwoPhaseUrl
failed to create configIdData CF Object\n
kBBUReturnBadManifestStatus
kBBUReturnTooManyReperso
Error: Invalid GetData response from BB\n
zero-padding
Retrieving Notification failed\n
kBBUReturnProvisioningUnknownSupportTypeError
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapKey failed with 0x%x%s\n
Failed to register for proxy\n
0x
kBBUReturnAllocationFailed
Dump: %s\n
stall
/Library/AddressBook
ManagePairingGetNonce result %d SW1_SW2 0x%04X length %d\n
keys
Failed to complete ValidatePerso command\n
BypassPairing
kBBUReturnMultipleDevices
kBBUReturnHashesMismatch
/Library/ControlCenter
fCommunication object not created, cannot create Transport\n
FinalizePersoDeviceRequest.bin
BBUICE16Communication
kVinylSIMSKUID
OPER_NOT_SUPPORTED
com.apple.VinylStatuscallback
Sep_Cmd_Ind returned error[%s].\n
DR_Success == der_ret && TAG_NML == dec.tag
result %d code %d raw_error %ld\n
Failed to encode value at index %ld\n
CFEqual(cmd, Alder::ValueCommandGetBppResp)
No operation requested in options\n
Invalid GetData response from the BB\n
GetNonceServerRequest.plist
eUICCVinylDALValve::ResetCard not supported\n
InstallPairingMSM Sep_Cmd_Cnf fail\n
Failed to encode key at index %ld\n
kBBUReturnPowercycleAfterFusing
kBBUReturnFailLoadImage
Failed to verify pairing with status %d, but continue restore as option as PR option skipOperationOnSEPfail is true\n
SimConfigRsp: device supports eSIM\n
VinylKTLEUICC::perform: KTLUTACopyReceiveData failed\n
VinylPairing
kVinylForceGenericUpdate NV set to TRUE\n
mipc::MIPC_SIM_STATUS_SIM_PIN2
VinylTwoPhasePresenceCheck
kBBUReturnSBLImageError
GetData not valid but isAbsentOK = true, eUICC not detected, skipping.\n
Failed to InstallPairingMSM result %d SW1_SW2 0x%04x\n
response
Switch_Mode_Cnf not successful, result 0x%x sw1_sw2 0x%hx\n
stringData != nullptr
DR_Success == der_ret && lpaSigningReq.size() > 0
xmissiontimeout
%s%s
Failed to GetNcCfgRequest status %d\n
mipc::MIPC_SIM_STATUS_SEP_AUTH_FAILED
VinylUse4FF
no profile available nor installed , skipping\n
/Library/TCC
Router server starting.\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/CommandDrivers/eUICCVinylDALValve.cpp
Init_Perso_Req sent: Msg=0x%x fTlv_Payload = %s\n
mipc::MIPC_SIM_STATUS_PH_NET_PIN
sw1_sw2 0x%hx\n
valueSessionid != nullptr
kBBUReturnGetCertIDFailure
Failed to power SE, during Vinyl Operation %d \n
sim_state 0x%x, sim_error_cause 0x%x\n
failed to create deviceUDID\n
Error: failed to get slot info from BB\n
VinylKTLEUICC
current_fw_version %s main_fw_nonce 0x%s gold_fw_nonce 0x%s\n
NULL requestURL?\n
Switch_Mode_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s\n
LETO-capable device detected! Attempt to enable eUICC.\n
shared allow list:
startRouterServer()
Timeout waiting for confirmation on Auth Perso Req.\n
Using manual argument numbering in automatic argument numbering mode
!performOptions.alderHostname.empty()
inData
Timeout waiting for confirmation on Validate Perso Req.\n
EoS_Getdata_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Is_Not_Personalized = %s fTlv_Sw = %s fTlv_Chip_Id = %s fTlv_Eid = %s\n
(kVinylResultSuccess == result) && (eUUID.size() == LENGTH_OF_EUUID)
failed to get ConfigId from eUICC\n
euiccSig != nullptr
aks_fv_set_protection
Invalid GetData output\n
operator=
PRP timed out %d\n
An argument index may not have a negative value
Clear All eSIM Preferences
disable_req.get()
bbupdater
akstest_new_key
kBBUReturnSuccess == ret
DR_Success == ret
EID: %s\n
failed to create signedPayload CF Object\n
failed to create euiccPublicKey CF Object\n
CLASS NONE
After check， card mode was not successfully set to normal\n
router.client.vinylrestore
Error: GetData() output not valid and isAbsentOK = false. kBBUReturnGetEIDFailure will be reported as kVinylResultDataMissing!\n
The format string terminates at a '{'
NfRestoreSEOpenWithError
/wireless
SwitchSimMuxCfgPolled: perform failed\n
/AppleInternal/Library/BuildRoots/4~CatVugAdRTUoFSQCa_wMfK3SZQyGVDT9VEArIh8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h
SendReceiptServerResponse.plist
fail to free transport: %p\n
kBBUReturnFirmwareDataError
Failed to complete bootstrap provisioning: %d\n
kPSIM1_TOONIE
!GET_RSP_FIELD(rsp, result_t3) && GET_RSP_FIELD(rsp, sim_rsp_len_t5)
The argument index starts with an invalid character
VinylTwoPhaseEidMask
Failed to check BCOM delete notification\n
Core dump successful \n
kBBUReturnGetFirmwareVersionFailed
SwitchSimMuxCfgPolled: timed out after %d polls\n
dec.tag == TAG_PIR
/db/com.apple.xpc.launchd
/root/Library/Preferences
/Library/MobileContainerManager
%s: mode=%o, u/g=%i:%i class=%i%s\n
status 0x%hhx cards_type: %hhu \n
Failed to correct result %d\n
InitPersoServer %d\n
TwoPhaseProvImpl::Perform\n
EUICCChipID
aks
In VINYL_OPERATION_GET_PAIRING_IDENTIFIER\n
GET_RSP_FIELD(rsp, result_t3) == IBI_NC_RESULT_SUCCESS
SwitchSimMuxCfgPolled: GetSimMuxCfg BUSY on poll %d/%d, MUX still switching\n
The precision option does not contain a value or an argument index
kBBUReturnBinaryImageError
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapEK failed with 0x%x%s\n
rsp->Valid() && rsp->contents.rsp_len
Auth_Perso_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s fTlv_Payload = %s\n
Bootstrap Preferences
kBBUReturnFileError
Error: failed to SwitchCardMode\n
mipc::MIPC_SIM_STATUS_PH_FSIM_PIN
<user>
StoreData Command failed with sw %x\n
Failed to InstallPairingMSM status %d\n
ManagePairingAuthenticate Sep_Cmd_Cnf returned error[%s]\n
VinylInstallSealingManifest
DR_Success == DERDecodeSeqNext(&seq, &dec_nested)
failed to create dict CF Object\n
BBUpdaterExtremeCreateWithError rejected with error\n
\tSize Distribution:
VinylForceGenericUpdate
geteUUIDBootstrapV2 not supported\n
 Initializing KTL options struct, opening ARI channel\n
Bootstrap profile ICCID found on eUICC\n
kBBUReturnFailCreateTransportBooted
GetEUICCDataNonce
sim_state 0x%x sim_error_cause: 0x%x sim_ext_capabilities 0x%x isAbsentOk: %s\n
CFGetTypeID(outPlist.get()) == CFDictionaryGetTypeID()
EoS_Getdata_Cnf not successful, result 0x%x 
DR_Success == der_ret && TAG_PILR_OK == dec.tag
two-phase flow unsupported with perso incomplete\n
force
TAG_GPS_PS == dec.tag
/Media
kHalley
configIdData != nullptr
gap 
kBBUReturnTransferTerminated
kBBUReturnProvisioningDataError
Fail to get valve\n
In VINYL_OPERATION_PERFORM_SECURE_PERSO\n
Failed to ManagePairingAuthenticate status %d\n
SwitchSimMuxCfgPolled: GetSimMuxCfg failed on poll %d/%d\n
signingPayloadDict
The argument index should end with a ':' or a '}'
UNKNOWN
inDict
Failed to start router server due to timeout\n
Timeout waiting for confirmation on Status Req.\n
mipc::MIPC_SIM_STATUS_NOT_INSERT
sizeof(result) == HDLCFrameGetPayloadLength(&rsp)
Delete All Non-Bootstrap Profiles
eUICCSepPairingBypassValue 
opening channel on provided external transport\n
sig_out %s\n
Failed to deserialize dictionary %s error %s\n
Timeout waiting for mipc client start.\n
alderHost             
======================================\n
deviceUDID && deviceUDID.get()
Nonce
GetWrapKeyServerResponse.plist
tag_props[seg].optional || (tag_props[seg].innerTag == decoded.tag)
euicc_signed_lpa_resp_decoded.profileList.length == 0
ecidNumber != nullptr
failed to create ecidNumber CF Object\n
RemoteFSRoot
MGCopyAnswer
kBBUReturnNoMemory
Creating validatePerso sequence failed\n
offset + length <= offset_seq_end
kBBUReturnGetPersonalizationInfoFailed
akstest_check_class
Failed to InstallPairingMSM status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
Failed to verify pairing: %d\n
isAbsentOkay result %d hardwareHasESIM: %d\n
SwitchSimMuxCfgPolled: MUX switch confirmed after %d poll(s)\n
mipc::MIPC_SIM_STATUS_PH_NET_PUK
Init_Perso_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s fTlv_Payload = %s\n
The type option contains an invalid value for a string formatting argument
eumCertificate != nullptr
SessionId
In ManagePairingAuthenticate...\n
/Library
aks_fs_supports_enhanced_apfs
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestRewrapEK failed with 0x%x%s\n
ManagePairingAuthenticate Sep_Cmd_Ind Sep_Cmd_Cnf\n
End of input while parsing an argument index
The argument index is invalid
0123456789abcdef
request to free transport: %p\n
SE closed SUCCESSFULLY\n
BootMode
kBBUReturnFailedSetNVItems
UpdateBaseband
eUICCSEPPairingInstallMSM 
this->serverSessionID && CFStringGetLength( this->serverSessionID.get() ) != 0
Invalid external client link instance. \n
The format specifier should consume the input or end with a '}'
kPSIM1_LOONIE
ManagePairingGetNonce Sep_Cmd_Cnf fail\n
INSTALLED
kBBUReturnResetToPBL
Pairing Operation Not supported continue with Vinyl Operation
nsr_req.get()
kBBUReturnTryAgain
/Applications
v16@?0^{_ftsent=^{_ftsent}^{_ftsent}^{_ftsent}q^v**iiSSQiSsSSS^{stat}[1c]}8
VinylTwoPhaseRefurbRef
kBBUReturnNoBBTicket
DebugArgs
/protected/trustd
Reset card failed\n
kLOONIE
ValidatePersoDeviceRequest.bin
ManagePairingGetNonce Sep_Cmd_Ind fail\n
eUUID
eid
Failed to store data status %d SW1_SW2 0x%x\n
euiccCertificate:: \n
OptimizeRefurbFirmwareUpdatePath
VinylOnlyPerso
89[0-9]{14}((5[0-9])|(8[0-46-9]))[0-9]{14}
aks_fv_new_vek
GetBppResp
!performOptions.twoPhaseUrl.empty()
kBBUReturnELFImageError
default case\n
Failed to Pairing authenticate result %d SW1_SW2 0x%04x\n
Sending geteUUID request\n
Timeout waiting for confirmation on Switch Mode Req.\n
Finalize_Perso_Req sent: Msg=0x%x fTlv_Payload = %s\n
(nullptr != pir) && (nullptr != err)
!performOptions.configIdProvURL.empty()
/preferences
EoS_Getdata_Req sent: Msg=0x%x fTlv_Is_Num_Of_Profile_Needed = %s\n
-f
Str && \"StringRef cannot be built from a NULL argument\"
/Library/WebClips
InstallPairingMSM Sep_Cmd_Cnf returned error[%s]\n
VinylETLEUICC
/Library/VoiceServices
Timeout waiting for confirmation on Finalize Perso Req.\n
mipc::MIPC_SIM_STATUS_BUSY
Failed to complete secure perso: %d\n
Router server stopping.\n
Not support for concatenated indications currently, segment 0x%x/0x%x\n
The format string contains an invalid escape sequence
kVinylResultSuccess == vinyl_ret && sessionData.getPbiReq().get() && sessionData.getBpp().get()
kBBUReturnSWIDMismatchForHW
kBBUReturnManifestImageError
geteUUID: StoreData failed with result %d, sw=0x%04x\n
EOS - dev product type detected, returning not supported\n
SIM Status Req attempt %d failed.\n
resultTo1stCommand.status == VinylError::kStatusSuccess
failed to get deviceUDID from MobileGestalt\n
transactionId
logging
/root/Library/Lockdown
MAV radio %d eSIM lookup not supported!\n
eUICCVinylDALValve
Status_Cnf received: Msg=0x%x fTlv_Eid = %s fTlv_Iccid = %s fTlv_Atr = %s\n
kBBUReturnInitializeRingBufferError
kBBUReturnGetChipIDFailure
kBBUReturnGetPkHashFailure
/keybags
/Library/MobileBluetooth
vinylValve
GetWrapKeyServer %d\n
eUICC enabled, mux switch success!\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewKey failed with 0x%x%s\n
Failed to GetEuuidRequest status %d\n
Calloc dict values failed\n
DR_Success == DERDecodeSeqNext(&seq, &decoded)
kBBUReturnTUTransportError
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 1)%s\n
rsp
Invalid user operation\n
createTransport attempt %d/%d\n
Command
something is wrong.. : %d\n
NVRAM '%s' exists? %s\n
Finalize_Perso_Req not successful, result 0x%x
GetSimMuxCfg: perform failed\n
failed to create deviceUDID CF Object\n
List Delete notification failed\n
Extract Notification Sequence number failed\n
MapMetaData Creation failed for the LPA Request\n
nvramRef
pingattempts
/log
error %d status 0x%hhx\n
Sep_Cmd_Ind failed, result 0x%x\n
/mnt4
IODeviceTree:/options
/Library/Logs/CrashReporter
Assertion failure ( pfnNfRestoreOpenWithSE != __null && \"Could not find NfRestoreSEOpenWithError symbol\\n\" )
iccid
kBBUReturnMIImageError
 dir: %s %i\n
akstest_new_ekwk
Delete Profile Cmd_Req returned error[%s].\n
Delete All Profiles
skipAll               
BasebandEnableProvisioning
Options
kBBUReturnAlreadyStarted
stat failed: %s\n
!GET_RSP_FIELD(rsp, result_t3)
payload.size() <= MAX_SEP_SIGNED_AUTH_SZ
VinylForceGold
Failed to handle bootstrap provisioning operation, ret %d\n
Router server started.\n
InstallPairingMSM Sep_Cmd_Cnf failed, result 0x%x\n
/Library/CoreFollowUp
DR_Success == der_ret && TAG_EUICCDATAREQ == dec.tag
CreateValidatePersoPayload DR %d\n
Using automatic argument numbering in manual argument numbering mode
failure
NfRestoreDumpUART
kVinylResultSuccess == vinyl_ret
%s
_securityd
Getdata_Req sent: Msg=0x%x fTlv_Is_Num_Of_Profile_Needed = %s\n
Sep_Cmd_Ind doesn't have fTlv_Cmd_Id\n
Sep_Cmd_Ind nonce size = %zu, should be %d\n
The width option should not have a leading zero
twoPhasePresenceCheck 
dict.get() != nullptr
VinylClearMetadata::ClearMetadataForIccids: Attempted metadata clear for ICCID\n
kBBUReturnFFSimError
outData.contents.op_mode == eUICC::VinylOpMode::kOpModeNormal
The config Id request was not made, but the response is not for it, instead it is %d\n
profile
B16@?0^{_ftsent=^{_ftsent}^{_ftsent}^{_ftsent}q^v**iiSSQiSsSSS^{stat}[1c]}8
InstallPairingMSM returning success\n
Performing ResetCard\n
Proxy Available!\n
eidSharedRef
e-apfs
%s:%spid:%d,%s:%s%s%s%s%s%u:%s options value 0x%llx exceeds uint32_t%s\n
v28@?0i8^v12^v20
Config ID provisioning server error, attempt %d of %d\n
Invalid dictionary returned from getEID\n
status 0x%x sw1_sw2 0x%x eid 0x%s op_mode 0x%hhx\n
Failed to create data\n
localAccepter
EscrowPasscodePeriod
GetWrapKey
kBBUReturnManifestNoHashes
iargs
/mobile
ind.fTlv_Nonce.get()->size() == SEP_NONCE_SZ
Delete Profile Cmd_Cnf received: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Result = %s\n
false
BBUpdaterExecCommand rejected  with error\n
/installd
/Library/Backup
ManagePairingAuthenticate Failed status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
kPSIM1_HALLEY
Assertion failure ( pfnNfRestoreDumpUART != __null && \"Could not find pfnNfRestoreDumpUART symbol\\n\" )
nm_decoded.seqNumber.length > 0
aks_fv_new_kek
GetSimMuxCfg: failed, result=%s(%d)\n
InstallPairingMSM succeed\n
mipc::MIPC_SIM_STATUS_SIM_PIN
Delete BCOM notification on eUICC\n
failed to open connection to %s: %d\n
kLETO_3V
decodeConfigIdFromResponse: Received error response with code %d\n
ManagePairingAuthenticate Sep_Cmd_Cnf failed, result 0x%x\n
DR_Success == der_ret && TAG_RNLR == dec.tag
ret == kBBUReturnSuccess
getConfigIdBootstrapV2 not supported\n
mipc::MIPC_SIM_STATUS_PH_CORP_PUK
0 == getDataRsp.contents.perso
SerialNumber
InRecoveryOS: %d\n
No :-(
/Library/SpringBoard
Need to free transport before creating again
failed to get eUUID from eUICC\n
valueSessionid is null\n
metaDictRef != nullptr
(ret == DR_Success) && (ssp_decoded.eUICCSessionId.length > 0)
/Library/SyncedPreferences
%s:%spid:%d,%s:%s%s%s%s%s%u:%s version mismatch: %llu%s\n
kVinylPersoState
StoreData Command failed\n
All
Could not get master port %d\n
kBBUReturnFailedNVSync
/Library/CrashReporter
kBBUReturnRetryError
/tmp
GetSimMuxCfg: sim_cfg_req field not present in response\n
!ind.isError()
Assertion failure ( success && \"Unrecognized radio type.\" )
Invalid user operation: %d\n
Delaying for 6FA5 handling\n
BBUpdaterSetOptions rejected  with error\n
ff_create_transport
EID
com.apple.VinylCommunication
VinylSecureElement
LPA Signed Data to be sent to server in dictionary format %s\n
nonce
Failed to push minimal sealing manifest to the card\n
kBBUReturnProgrammerError
kBBUReturnBBTicketDecodeError
%i,%u,%u,%u,%lld,%lld,%lld,
-apfs_shared_datavolume
In InstallPairingMSM...\n
Resetting modem: %s\n
ManagePairingGetNonce Failed status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
GetNonce
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Communication/ICE/VinylICECommunication.cpp
Clear Bootstrap eSIM Preferences
kBBUReturnBadEnvironment
kBBUReturnGetIMEIFailure
/MobileDevice/ProvisioningProfiles
/Library/Keyboard
Timeout waiting for confirmation on EoS Get Data Req.\n
ManagePairingAuthenticate Sep_Cmd_Cnf has no fTlv_Result\n
In VINYL_OPERATION_GET_EID\n
FAILURE
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/NonUpdate/VinylPairing.cpp
Getdata_Cnf not successful, result 0x%x 
ps
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEKWK failed with 0x%x%s\n
In VINYL_OPERATION_VERFIY_PAIRING_PARAMS\n
Failed to get info: %d\n
VinylKTLEUICC::perform: expected gmid %u, got response gmid %u\n
TAG_NM == dec.tag
TAG_PBI == dec.tag
kBBUReturnBasebandUnresponsive
/MobileAsset
/Library/Preferences
Invalid payload length %u (actual_size: %zu, max_dim: %zu)\n
VinylDebugArgs
rnl_req.get()
keyData != nullptr
/containers
/Library/adi
/Library/DoNotDisturb
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestCheckClass failed with 0x%x%s\n
Verify Pairing is skipped for EOS product\n
aks_system_key_sign failed signing nonce %d\n
decodeEuuidFromResponse: Invalid input parameters\n
decodeEuuidFromResponse: Successfully extracted eUUID\n
this->reverseProxySettings
VinylClearMetadata::Perform: onlyBootstrap=%d\n
_wireless
/Containers
capabilities::euicc::supportsVinylSEPPairing()
ManagePairingAuthenticate has cached succeed result, no following indication\n
der_item.data <= (profile_ref_input.data() + profile_ref_input.size())
%s:%spid:%d,%s:%s%s%s%s%s%u:%s ioreg: %d, boot_arg: %d%s\n
In VINYL_OPERATION_GET_PAIRING_PARAMETERS_DUMMY\n
VinylNonUpdate
euiccCertificate != nullptr
kBBUReturnFailedStartProvisioning
In GetParameters\n
Timeout waiting for confirmation on Get Data Req.\n
VinylConfigIdProv
KERN_SUCCESS == kr && nvramInfo
/Library/UserNotifications
aks_get_convenience_bio_state
Failed to AuthenticatePersoDevice status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
payload.size() <= MAX_MSM_SZ
mipc::MIPC_SIM_STATUS_CARD_RESTRICTED
The replacement field misses a terminating '}'
failed to get deviceSerialNumber from MobileGestalt\n
_aks_operation
/Library/Logs/AppleSupport
Failed to FinalizePersoDevice status %hhu SW1 0x%x SW2 0x%x\n
DATA
Unsupported value type %ld at index %ld, skipping\n
eid && (CFStringGetTypeID() == CFGetTypeID(eid))
an integer
/mnt3/bbfs/
kBBUReturnFailedSetSVN
BBUPurpleReverseProxy
Replacement argument isn't a standard signed or unsigned integer type
persoStatic           
Server returned error response code\n
kBBUReturnLibFDRDynLibNotLinked
fLink
ManagePairingGetNonce Sep_Cmd_Cnf returned error[%s]\n
DR_Success == enc_ret
Notification Response decoding failed\n
Only attach the the existing coredump dir to output dictionary without executing coredump again.\n
kDeviceIdentifier
NEW_BPP_ELSE_INSTALLED_BPP_METADATA
Send Command to Nonce to Marina Server Failed\n
data
/Library/Logs
kTOONIE
com.apple.VinylCommunicationMisc
Proxy Aborted? %d\n
!url.empty() && urlRef
failed to convert deviceUDID to CFData\n
kBBUReturnTimedOut
kBBUReturnFailCreateTransportFirst
kBBUReturnAPTicketFileInitFailed
respDict
Timeout waiting for indication on InstallPairingMSM Sep_Cmd_Req\n
=========== Vinyl eUICC Options ============\n
forcePerso            
(fr_decoded.successResult.length > 0) || (fr_decoded.errorResult.length > 0)
result  0x%x \n
twoPhaseEidMask       
UniqueChipID
Fail to get data after resetting refurb\n
Two-phase provisioning server error, attempt %d of %d\n
kBBUReturnNotSupported
kBBUReturnFailedSendingImage
eidData != nullptr
aks_get_internal_info_for_key
SendReceiptServer %d\n
euiccPublicKey != nullptr
VinylKTLEUICC::perform: received NACK\n
euiccSignedLPAData
nonce.size() == SEP_NONCE_SZ
mipc::MIPC_SIM_STATUS_SEP_AUTH_UNPAIRED
Delete Profile Cmd_Cnf not successful, result 0x%x\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/NonUpdate/VinyleUICC.cpp
aks_run_internal_test
InstallPairingMSM Sep_Cmd_Ind Fail\n
mipc::MIPC_SIM_STATUS_PH_CORP_PIN
(kVinylResultSuccess == sessionData.extractDataFromPir(*pir))
kBBUReturnGetSessionKeyFailure
kBBUReturnBBTicketDERParseErrorForCal
ff_ping
akstest_unwrap_ek
Error: invalid simSKUID = %u\n
GetSimMuxCfg: transient BUSY, result=%s(%d)\n
mipc::MIPC_SIM_STATUS_PH_FSIM_PUK
!!! 
kBBUReturnNotPermitted
Payload %s\n
kLETO
Finalize perso failed with sw = %02X.\n
rsp->Valid()
Error: failed to get SimConfig info from BB\n
DR_Success == der_ret && TAG_PILR == dec.tag
BcomProfileDeleted
kBBUReturnNotStarted
Empty euuid data received\n
Missing X-Apple-Alder-IP header in response, sticky session not active\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Communication/Dale/VinylDaleCommunication.cpp
Client
89[0-9]{14}9[34567][0-9]{14}
kBBUReturnNotReady
kBBUReturnUnPersonalizedImageError
_merge_dict_cb
Failed to retrieve EID: %d\n
VinylKTLEUICC::perform: KTLRawSendData failed\n
Calloc dict keys failed\n
kVinylResultSuccess == ret
EoS_Getdata_Cnf returned error[%s].\n
:
DR_Success == der_ret && TAG_SEQN == dec.tag
VinylControllerTwoPhaseProvisioning
fCommunication
signingPayloadDict && (CFGetTypeID(signingPayloadDict) == CFDictionaryGetTypeID())
BBUCapabilities
updateBaseband false\n
/usr/lib/libMobileGestalt.dylib
kBBUReturnFlashError
BBULog
aks_fv_rewrap_kek
cardData.contents.perso
DR_Success == der_ret && TwoPhaseProv::TAG_RNLR == dec.tag
kBBUReturnProgrammerItemLoadingFailed
kBBUReturnDownloadImageError
kBBUReturnMRCImageError
Failed to handle config id provisioning operation, ret %d\n
Error: failed to perform ResetSimCard\n
DR_Success == der_ret && TAG_CONFIGID_RESPONSE == dec.tag
The argument index value is too large for the number of arguments supplied
VinylPersoHost
unsupported device\n
/Library/Accounts
akstest_unwrap_key
sw == 0x9000
ManagePairingAuthenticate returning success\n
kVinylFirmware
simSKUID < ARR_SIZE(MAVHWSIMSKUStr)
Timeout waiting for indications on Cmd Req store data.\n
Validate_Perso_Cnf returned error[%s].\n
0X
Failed to assign request data\n
Unpersonalized
GetData() output not valid and isAbsentOK = false. than restore should mandatory fail for all operation except getEID operation\n
InstallPairingMSM Sep_Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Msm = %s\n
DR_Success == der_ret && TAG_RNLR_NL == dec.tag
kBBUReturnUMTSBand4CalibrationCheckFailure
kBBUReturnRPMImageError
%c%04zx  %s
%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks connection failed%s\n
delete_req.get()
VinylTwoPhaseProvUtil
pbiReq.get()
euiccSessionId
/MobileSoftwareUpdate
/Library/Voicemail
/Library/mad/activation_records
Failed to get data protection class for given path %s with errno %s (%d)\n
VinylKTLEUICC::perform: response unpack failed\n
StartSession
StringRef
/Library/DataAccess
transport
No transport available.. bail out\n
X-Apple-Alder-IP
Delete Profile Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Payload = %s\n
Sep_Cmd_Ind sepIndSem_ is NULL because of an unexpected baseband indication but that's fine\n
a character
ff_bootup
/Library/CoreDuet
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Controller/VinylController.cpp
decodeConfigIdFromResponse: Successfully extracted configID\n
fRouterServerGood
NULL
mipc::MIPC_SIM_STATUS_SIM_PUK
Init_Perso_Req not successful, result 0x%x
DR_Success == DERDecodeSeqContentInit(&gps_der, &seq)
signedPayload != nullptr
eUICCVinylMAVValve
SendReceipt
The format specifier for 
UniqueDeviceID
RestoreOSBuild
KERN_SUCCESS == kr
/Library/Passes
/Library/Carrier Bundles
InitPersoServerRequest.plist
kBBUReturnPingtimeout
%s/mobile
kINVALID
Failed to AuthPerso status %d SW1_SW2 0x%x rsp_len %u\n
ari
ecid != 0
kBBUReturnFDRDataValidationFailed
/Library/Logs/CoreDuet
failed to write restore bag to disk %s\n
SwitchCardMode: Failed err %d status %hhu mode %d sw1 0x%x sw2 0x%x\n
euiccSignature:: \n
Store data Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Payload = %s\n
Validate_Perso_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s fTlv_Payload = %s\n
Vinyl
kern.bootargs
getConfigId: Failed to decode ConfigId from response\n
getConfigId: Sending ConfigurationRequest for configId\n
kVinylResultSuccess == ret && sw == 0x9000
DeviceUDID
Free Blocks:%lld blocks of size:%d\n
%i
Invalid delete action: %d (expected 0 or 1)\n
FirmwareLoaderVersion
```
