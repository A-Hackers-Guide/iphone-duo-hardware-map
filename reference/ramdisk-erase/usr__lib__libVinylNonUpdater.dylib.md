# `/usr/lib/libVinylNonUpdater.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 983,808 bytes.

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
/Library/Logs/CoreDuet
/Library/SMS
eUICCVinylMAVValve
kLETO
DR_Success == der_ret && TAG_CONFIGID_RESPONSE == dec.tag
BBUCommon
getConfigIdBootstrapV2 not supported\n
Not support for concatenated indications currently, segment 0x%x/0x%x\n
BPPRequestData
DataRoot
step
StringRef.h
DR_Success == DERDecodeSeqContentInit(&decoded.content, &seq)
ConfigId Provisioning Operation is Success\n
failed to create euiccPublicKey CF Object\n
kBBUReturnGetKeyStatusFailure
/root/Library
/Documents/Pearl
outData.Valid()
Failed to InstallPairingMSM status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
Failed to install MSM: %d\n
ManagePairingGetNonce Sep_Cmd_Cnf has no fTlv_Result\n
kBBUReturnSuccess == ret && !dataBuffer.empty()
StartSession
sign
kBBUReturnNotSupported
Free Blocks:%lld blocks of size:%d\n
rsp->Valid()
kVinylFirmware
EID: %s\n
Creating mapMetaData SEQUENCE with %ld key-value pairs\n
kBBUReturnInvalidRadioType
kBBUReturnFusingInstructionMissing
Failed to correct response %d\n
Timeout waiting for confirmation on Get Data Req.\n
kBBUReturnLoaderVersionError
logmask
operationRequested(operation, eUICCoptions)
kDeviceIdentifier
ManagePairingGetNonce succeed\n
Auth_Perso_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s fTlv_Payload = %s\n
Auth_Perso_Cnf returned error[%s].\n
nvramRef
kBBUReturnFailCreateTransportSecond
GetSimMuxCfg: transient BUSY, result=%s(%d)\n
DATA
ManagePairingGetNonce Sep_Cmd_Ind fail\n
ManagePairingGetNonce Sep_Cmd_Cnf received: Msg=0x%x fTlv_Result = %s\n
gps_req.get()
kBBUReturnInitializerPrepError
aks_get_internal_info_for_key
fRouterServer
LETO-capable device detected! Attempt to enable eUICC.\n
UniqueChipID
dec.tag == TAG_PIR
89[0-9]{14}((5[0-9])|(8[0-46-9]))[0-9]{14}
/networkd
%i,%u,%u,%u,%lld,%lld,%lld,
AuthenticatePersoDeviceResponse.bin
link accepted failed. t\n
BPP
sessionData.isEidEligible( performOptions )
kBBUReturnGetIMEIFailure
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEK failed with 0x%x%s\n
Validate_Perso_Cnf returned error[%s].\n
ret == kBBUReturnSuccess
aks_system_key_sign failed signing nonce %d\n
fRouterServerGood
eUUIDdata != nullptr
kBBUReturnGetEIDFailure
eidValue:: \n
0
/mnt3
/Library/Assistant
/Library/Mail
Router server eror: %s\n
The argument index should end with a ':' or a '}'
0B
kBBUReturnFailLoadImage
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapEK failed with 0x%x%s\n
geteUUID: Sending GetEuiccDataRequest\n
Failed to allocate shared info dict\n
kLOONIE
BBUCapabilities
Timeout waiting for indication on ManagePairingAuthenticate Sep_Cmd_Req\n
01
GetBpp
failed to create ecidNumber CF Object\n
error %d status 0x%hhx\n
ManagePairingAuthenticate Failed status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
But the BB coredump dir is empty.\n
kLETO_3V
OptimizeRefurbFirmwareUpdatePath
eidData != nullptr
VinylClearMetadata::GetListOfIccids: Extracting Profile List\n
kBBUReturnTooManyRetry
Payload %s\n
Functionality not implemented.\n
mipc::MIPC_SIM_STATUS_SIM_PIN2
mipc::MIPC_SIM_STATUS_PH_FSIM_PUK
kBBUReturnTelephonyUtilReadError
/root
/root/Library/Caches
/Library/VoiceServices
decodeConfigIdFromResponse: Successfully extracted configID\n
ManagePairingAuthenticate input signed auth size = %zu, should < %d\n
successCnf
disable_req.get()
(nullptr != pir) && (nullptr != err)
BB reset successful\n
kBBUReturnManifestImageError
kBBUReturnMRCImageError
Failed to correct result %d\n
xporttimeout
/root/Library/Preferences
/Library/MobileContainerManager
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestRewrapEK failed with 0x%x%s\n
_merge_dict_cb
SwitchSimMuxCfgPolled: perform failed\n
uimSlot               
DELETE_NOTIFICATION_STATUS_OK == del_status
akstest_new_ek
Reset card failed\n
Invalid payload length %u (actual_size: %zu, max_dim: %zu)\n
decodeEuuidFromResponse: Successfully extracted eUUID\n
Sep_Cmd_Ind returned error[%s].\n
/MobileSoftwareUpdate
/Library
SIM status: %s(%d).\n
ManagePairingAuthenticate succeed\n
signingPayloadDict && (CFGetTypeID(signingPayloadDict) == CFDictionaryGetTypeID())
Failed to encode ECID\n
mipc::MIPC_SIM_STATUS_PH_SP_PUK
Failed to check BCOM delete notification\n
1
eUUID
NVRAM: %s\n
CFGetTypeID( cmd ) == CFStringGetTypeID()
kBBUReturnUnPersonalizedImageError
kBBUReturnFailedNVSync
!!! 
/Media/iTunes_Control
decodeConfigIdFromResponse: Unexpected outer CHOICE tag 0x%02llx\n
InitPersoDeviceResponse.bin
The argument index starts with an invalid character
kBBUReturnInvalidBBUStageError
cardData.Valid()
Timeout waiting for confirmation on Cmd Req Delete Profile.\n
mipc::MIPC_SIM_STATUS_BUSY
kBBUReturnBinaryImageError
In VINYL_OPERATION_PERFORM_SECURE_PERSO\n
GetNonce
EoS_Getdata_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Is_Not_Personalized = %s fTlv_Sw = %s fTlv_Chip_Id = %s fTlv_Eid = %s\n
Switch_Mode_Req returned error[%s].\n
kBBUReturnBadArgument
akstest_last_user
aks-client-queue
SIM status req failed even after several retries.\n
stringData != nullptr
kBBUReturnRPMImageError
Received payload length (%d) is smaller than required size (%d)\n
kBBUReturnAPTicketMallocFailed
/Library/UserNotifications
fSe
UniqueDeviceID
GetNonceServerRequest.plist
Finalize perso failed with sw = %02X.\n
stall
And found the BB coredump already collected, don't need to trigger collection again. Now return error = %d, previous ret = %d\n
GetData status is not valid, hardware does not have eSIM, set absentOk to True\n
decodeConfigIdFromResponse: Found auditResponseOk\n
CreateValidatePersoPayload DR %d\n
Switch_Mode_Req sent: Msg=0x%x fTlv_Is_Reset_Req = %s\n
Store data Cmd_Ind received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s fTlv_Payload = %s\n
Server response received after sending SerialNumber and Device UUID\n
Vinyl
eUICCVinylData cache is valid. Using cached data!\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/CommandDrivers/eUICCVinylDALValve.cpp
Getdata_Req sent: Msg=0x%x fTlv_Is_Num_Of_Profile_Needed = %s\n
/tmp
/Library/CoreDuet
Failed to InstallPairingMSM status %d\n
com.apple.VinylStatuscallback
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/NonUpdate/VinylConfigIdProv.cpp
kBBUReturnBBTicketReadContentFailed
/Library/AggregateDictionary
Signing payload dictionary not present in the input dictionary\n
Still persod after force?\n
Command
Missing or empty server sssion?! %s\n
Core dump successful \n
decodeEuuidFromResponse: Invalid input parameters\n
router.server
Timeout waiting for indication on ManagePairingGetNonce Sep_Cmd_Req\n
0x
-c
valueSessionid is null\n
AppleKeyStoreTest
ECID
/Library/mad/activation_records
aks_internal_state
In VINYL_OPERATION_BOOTSTRAP_PROVISIONING\n
Skipping free of external transport\n
keys
Timeout waiting for confirmation on Validate Perso Req.\n
kBBUReturnSBLImageError
resultTo1stCommand.status == VinylError::kStatusSuccess
The width option should not have a leading zero
DR_Success == der_ret && TAG_PI == dec.tag
failed to get eUUID from eUICC\n
BcomProfileDeleted
pbiReq.get()
Fail to get valve\n
EID
Invalid GetData output\n
sim_state 0x%x sim_error_cause: 0x%x sim_ext_capabilities 0x%x isAbsentOk: %s\n
VinylKTLEUICC::perform: expected gmid %u, got response gmid %u\n
InstallPairingMSM succeed\n
mipc::MIPC_SIM_STATUS_SEP_AUTH_STALLED
NfRestoreSEClose
Skip Vinyl provisioning\n
coreDumpPath
aks_delete_xart_leak
!(GET_RSP_FIELD(rsp, sim_error_cause_t28) & sim_error_cause_mask)
Client rsp data buffer is not valid\n
Two-phase provisioning server error, attempt %d of %d\n
NfRestoreSEOpenWithError
Server URL Not present\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s version mismatch: %llu%s\n
check failed: %s, %d, assertion: %s\n
default case\n
Status_Cnf returned error[%s].\n
eUICCSEPPairingInstallMSM 
TransactionID
!getDataRsp.contents.isAbsentOk
Send Command of eUICC Feed to Marina Server Failed\n
Server returned error response code\n
kTOONIE
ManagePairingAuthenticate Sep_Cmd_Cnf has no fTlv_Result\n
The argument index value is too large for the number of arguments supplied
kBBUReturnFailedSetSVN
/dev/null
/Applications
 option
(ret == DR_Success) && (er_decoded.bppCommandId.length > 0) && (er_decoded.errorReason.length == 1)
In InstallPairingMSM...\n
BBUICE16Communication
/Library/CountryBundles
InstallPairingMSM returning success\n
success
0123456789abcdefghijklmnopqrstuvwxyz
twoPhaseUrl           
Could not load NVRAM? %d\n
kBBUReturnPingtimeout
kBBUReturnFusingSECELFFailed
/Library/AddressBook
mipc::MIPC_SIM_STATUS_PH_SIM_PIN
kBBUReturnGetCarrierIDFailure
aks_fv_rewrap_kek
InitPersoServerResponse.plist
a bool
VinylKTLEUICC::perform: received NACK\n
eUICC enabled, mux switch success!\n
VinylPersoHost
DR_Success == DERDecodeSeqContentInit(&dec.content, &seq)
configId
pargs
hl:C:v:x:t:r:p:e:c:w:i:s:fUFD:nHSqPV
Failed to get data protection class for given path %s with errno %s (%d)\n
Failed to AuthenticatePersoDevice status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
fCommunication
ValidatePersoDeviceRequest.bin
failed to create eumCertificate CF Object\n
Invalid key or value at index %ld\n
/backup
/Library/BackBoard
v16@?0^{_ftsent=^{_ftsent}^{_ftsent}^{_ftsent}q^v**iiSSQiSsSSS^{stat}[1c]}8
GetData not valid but isAbsentOK = true, eUICC not detected, skipping.\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Support/BBUCommon.cpp
kBBUReturnFailCreateTransportFirst
kBBUReturnFailedSendingImage
kBBUReturnELF32HeaderError
To be signed dictionary is empty\n
ecidNumber != nullptr
kBBUReturnBBTicketDERParseErrorForCal
kBBUReturnNoBBTicket
/Library/DoNotDisturb
Power up SE successful.\n
Init_Perso_Req sent: Msg=0x%x fTlv_Payload = %s\n
ind.fTlv_Nonce.get()
kBBUReturnPingFailed
Minimal sealing manifest fetch failed %s\n
SimConfigRsp: device supports eSIM\n
GetWrapKeyServer %d\n
ManagePairingAuthenticate has cached succeed result, no following indication\n
twoPhaseEidMask       
/Library/SyncedPreferences
/Library/ConfigurationProfiles
ValidatePersoDevice %d\n
unsupported device\n
configIdData != nullptr
/Library/CoreFollowUp
outData.contents.isAbsentOk
Unable to get EID\n
InitPersoDeviceBlob.bin
ManagePairingAuthenticate Sep_Cmd_Cnf fail\n
ind.fTlv_Nonce.get()->size() == SEP_NONCE_SZ
The value of the argument index exceeds its maximum value
rnl_req.get()
kBBUReturnNAKHello
eUICCVinylMAVValve::ResetCard not supported\n
Failed to FinalizePersoDevice status %hhu SW1 0x%x SW2 0x%x\n
Creating with timeout set to %u ms\n
nm_decoded.seqNumber.length > 0
transactionId
CLASS NONE
VinylSkipOperationOnSEPFail
Failed to create responseNonceFromServers CF Object\n
DR_Success == der_ret && TAG_IMSI == dec.tag && SIZE_OF_BCOM_IMSI == dec.content.length
rsp
Failed to perform LPASigning Request status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
pfnNfRestoreOpenWithSE failure, outResult: %d\n
euicc_signed_lpa_resp_decoded.profileList.length == 0
VinylClearMetadata::GetListOfIccids: Successfully populated ICCID list!\n
Could not find NVRAM via IOKit\n
Yes :-)
bpp.get()
DR_Success == DERDecodeSeqContentInit(&content, &seq)
kBBUReturnTimedOut
VinylProvisioningURL
alderHost             
DR_Success == der_ret && TAG_RNLR == dec.tag
LdrVerSupportsTwoPhaseInstall(ldr_ver)
Failed to get valid LPA Signed response from the eUICC\n
kBBUReturnFileNotFound
verbosity
Client rsp data is not valid\n
Try to copy the BB coredump from %s\n
fCommunication object not created, cannot create Transport\n
createTransport attempt %d/%d\n
com.apple.VinylCommunication
respDataPayload
Router server stopped.\n
iargs
!GET_RSP_FIELD(rsp, result_t4)
ret %d records %zu\n
fLink
ManagePairingGetNonce Sep_Cmd_Cnf fail\n
Sep_Cmd_Ind Cmd_Id %u not supported\n
mipc::MIPC_SIM_STATUS_EMPT_EUICC
deviceUDID && deviceUDID.get()
BBUpdaterSetOptions rejected  with error\n
Verify Pairing is skipped for EOS product\n
(snipped)
(kBBUReturnSuccess == ret) && (sw == 0x9000)
opening channel on provided external transport\n
InstallPairingMSM Sep_Cmd_Cnf has no fTlv_Result\n
BCOM Delete notification found\n
<user>
akstest_unwrap_ek
ManagePairingAuthenticate Sep_Cmd_Cnf received: Msg=0x%x fTlv_Result = %s\n
tag_props[seg].optional || tag_props[seg].topLevelTag == decoded.tag
EUICCChipID
kBBUReturnNotPermitted
ENTER: %s\n
rsp.Valid()
Failed to Refurb: %d\n
0b
Assertion failure ( nullptr != fTransportCreated && \"Telephony Util transport error!\\n\" )
forceGold             
!GET_RSP_FIELD(rsp, result_t3) && GET_RSP_FIELD(rsp, sim_rsp_len_t5)
failed to create signing dict\n
BootMode
/keybags
Config ID provisioning server error, attempt %d of %d\n
GetSimMuxCfg: perform failed\n
two-phase flow unsupported with perso incomplete\n
dict.get() != nullptr
kBBUReturnProgrammerError
kBBUReturnGetCertIDFailure
/Library/Backup
ManagePairingAuthenticate input nonce is empty\n
The numeric value of the format specifier is too large
Need to free transport before creating again
StringRef
/.fseventsd
/AppleInternal/Library/BuildRoots/4~CatVugAdRTUoFSQCa_wMfK3SZQyGVDT9VEArIh8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h
eUICCVinylDALValve
quitbootrom
IOService:/IOResources/AppleKeyStoreTest
Failed to InitPerso status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
Fail to get data after resetting refurb\n
Validate_Perso_Req sent: Msg=0x%x fTlv_Payload = %s\n
Sep_Cmd_Ind failed, status word from UICC sw 0x%hx\n
Error: Invalid GetData response from BB\n
VinylKTLEUICC
0 == getDataRsp.contents.perso
InRecoveryOS: %d\n
: 
%c%04zx  %s
/Keychains
outPlist
======================================\n
IsProvTxIdAvailable( euicc_rsp )
failed to create signedPayload CF Object\n
decode_pfk_bulk_data
transport
Creating validatePerso sequence failed\n
01234567
NEW_BPP_ELSE_INSTALLED_BPP_METADATA
Invalid user operation: %d\n
Failed to store data status %d SW1_SW2 0x%x\n
kNonce
kVinylResultSuccess == vinyl_ret && sessionData.getPbiReq().get() && sessionData.getBpp().get()
%lld,%d\n
rsp->Valid() && rsp->contents.rsp_len
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Options/eUICCOptions.cpp
postProcess           
Str && \"StringRef cannot be built from a NULL argument\"
result == kVinylResultSuccess
/vm
Unpersonalized
VinylPollResult
result %d code %d raw_error %ld\n
kVinylRadioType
Error: failed to get SimConfig info from BB\n
eUICC not enabled, aborted!\n
a floating-point
skipAll               
EuiccSessionID
FAILURE
kVinylForceGenericUpdate NV set to TRUE\n
Getdata_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Is_Not_Personalized = %s fTlv_Sw = %s fTlv_Chip_Id = %s fTlv_Eid = %s\n
No :-(
recv
daemon
Perso Only can only be performed with kVinylOperationNonUpdate\n
signingPayloadDict
kBBUReturnIOError
kBBUReturnBadChecksum
kBBUReturnFusingError
GET_RSP_FIELD(rsp, result_t3) == IBI_NC_RESULT_SUCCESS
SwitchSimMuxCfgPolled: request rejected, result=%s(%d)\n
SwitchSimMuxCfgPolled: MUX switch confirmed after %d poll(s)\n
decodeConfigIdFromResponse: Invalid input parameters\n
In VINYL_OPERATION_CONFIGID_PROVISIONING\n
mipc::MIPC_SIM_STATUS_PH_FSIM_PIN
Delete Profile Cmd_Cnf not successful, result 0x%x\n
VinylClearMetadata::ClearMetadataForIccids: Attempted metadata clear for ICCID\n
aks_kext_set_options
getConfigId: StoreData failed with result %d, sw=0x%04x\n
sim_state 0x%x, sim_error_cause 0x%x\n
VinylNonUpdate
Bootstrap profile ICCID found on eUICC\n
Send Notification command to eUICC failed\n
kBBUReturnProgrammerConnectionError
/protected/trustd
kBBUReturnHashesMismatch
GET_RSP_FIELD(rsp, cfg_req_t4) == IBI_NC_CFG_REQ_CONFIG_ID
(%s:%d) Range assignment too large(%p), got(%ld) max(%ld)
DR_Success == der_ret
response
00000000000000000000000000000000
SubmitEUICCDataFeed
bbupdater
kBBUReturnNeedsMoreInput
Fail to SetCardMode(kOpModeNormal)\n
IBIVinylSimCardResetRspCb result 0x%x\n
DR_Success == der_ret && TwoPhaseProv::TAG_RNLR_NL == dec.tag
Unsupported value type %ld at index %ld, skipping\n
EOS - dev product type detected, returning not supported\n
status 0x%x sw1_sw2 0x%x eid 0x%s op_mode 0x%hhx\n
!nonce.empty()
VinylSkipAll
EID not eligible, skipping\n
kVinylResultSuccess == vinyl_ret && isBootStrapAlreadyInstalled
DR_Success == der_ret && lpaSigningReq.size() > 0
kBBUReturnNotReady
NULL
kBBUReturnFatalError
%s
In VINYL_OPERATION_GET_EID\n
InstallPairingMSM Sep_Cmd_Cnf returned error[%s]\n
skipOperationOnSEPfail
something is wrong.. : %d\n
/Library/NanoTimeKit
returning VinylController::create\n
eid && (CFStringGetTypeID() == CFGetTypeID(eid))
The format string contains an invalid escape sequence
VinylVerifyPairing
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Controller/VinylController.cpp
main_fw_pcf_mac 0x%s gold_fw_pcf_mac 0x%s pcf_version 0x%x\n
decodeConfigIdFromResponse: Received error response with code %d\n
Serialization error
transport %p, status: %d\n
stat failed: %s\n
Status_Cnf received: Msg=0x%x fTlv_Eid = %s fTlv_Iccid = %s fTlv_Atr = %s\n
Store data Cmd_Req returned error[%s].\n
{:02x}
deviceUDIDData != nullptr
kBBUReturnELFImageError
kBBUReturnFusingVerificationFailed
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestLastUser failed with 0x%x%s\n
mipc_client_started
Sep_Cmd_Ind Cmd_id %u should have fTlv_Nonce\n
DR_Success == der_ret && TAG_SEQN == dec.tag
failed to convert deviceUDID to CFData\n
kBBUReturnNotStarted
/iomfb_bics_daemon
/Library/Calendar
FinalizePersoDeviceRequest.bin
false
kVinylEID
error %d status %u sw1_sw2 0x%x\n
Pairing Operation Not supported continue with Vinyl Operation
VinylForceMain
\tSize Distribution:
GetNonceServer %d\n
Timeout waiting for mipc client start.\n
payload.size() <= MAX_MSM_SZ
VinylDebugArgs
VinylConfigIdProv::Perform\n
/usr/lib/libMobileGestalt.dylib
akstest_unwrap_key
outData.contents.op_mode == eUICC::VinylOpMode::kOpModeNormal
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/SecureElement/VinylSecureElement.cpp
DR_Success == DERDecodeSeqNext(&seq, &dec_nested)
/Library/NanoBackup
rsp_data
Getdata_Cnf not successful, result 0x%x 
ManagePairingGetNonce Sep_Cmd_Cnf returned error[%s]\n
VinylSkipProvisioning
kBBUReturnProvisioningUnknownSupportTypeError
ff_create_transport
In GetParameters\n
Proxy Available!\n
ManagePairingAuthenticate input nonce size = %zu, should be %d\n
Resetting modem: %s\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Communication/Eureka/VinylEURCommunication.cpp
twoPhaseRefurbRef     
VinylTwoPhaseProvUtil
Failed to assign response data\n
ind.fTlv_Sw && *ind.fTlv_Sw == 0x9000
Client
%u.%03u: %s: %u%s\n
/logs
could not open file: %s (%s)\n
Failed to correct SW during config Id fetch 0x%04x\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/CommandDrivers/eUICCCommon.cpp
0X
transport %p, status: %#x\n
TAG_GPS_PS == dec.tag
_securityd
Invalid user operation\n
Failed to verify pairing with status %d, but continue restore as option as PR option skipOperationOnSEPfail is true\n
response->contents.cmd_rsp_token == resultTo1stCommand.cmd_rsp_token && response->contents.status == VinylError::kStatusSuccess
DR_Success == DERDecodeSeqContentInit(&gps_der, &seq)
/Library/Voicemail
Failed to handle Refurb operation, ret %d\n
kHalley
Empty payload data received\n
Sep_Cmd_Ind doesn't have fTlv_Cmd_Id\n
kBBUReturnModemPowercycleError
ManagePairingGetNonce Failed status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
Failed to stop router server due to timeout\n
failed to get deviceSerialNumber from MobileGestalt\n
Could not get master port %d\n
kBBUReturnGetICCIDFailure
kBBUReturnBBTicketMallocFailed
kBBUReturnBBTicketDERParseErrorForFATPCal
EXIT:\n
euiccSignature
Failed to complete AuthPerso command\n
tag_props[seg].optional || (tag_props[seg].innerTag == decoded.tag)
inRestoreOS: %d\n
kBBUReturnKeysNotAligned
kBBUReturnProvisioningDataError
DebugArgs
send
GetaData() output not valid and isAbsentOK = true. However, device doesn't support SEPPairing, no further non-update operation.\n
PersoImpl
startRouterServer()
NEW
result %d code %d raw_error %ld error %s\n
Failed to complete bootstrap provisioning: %d\n
sig_out %s\n
Failed to FinalizePerso status %d SW1_SW2 0x%x\n
Sep_Cmd_Ind sepIndSem_ is NULL because of an unexpected baseband indication but that's fine\n
Invalid Refurb Option %s
Retrieving Notification failed\n
kBBUReturnFailCreateTransportBooted
status
VinylCommunication
euiccSignature:: \n
GetNonceServerResponse.plist
Invalid external client link instance. \n
cmdId == mipc::MIPC_DALE_VINYL_SEP_CMD_GET_NONCE || cmdId == mipc::MIPC_DALE_VINYL_SEP_CMD_AUTHENTICATE || cmdId == mipc::MIPC_DALE_VINYL_SEP_CMD_INSTALL
(kVinylResultSuccess == result) && (eUUID.size() == LENGTH_OF_EUUID)
failed to create eUUID CF Object\n
ManagePairingAuthenticate returning success\n
vector
TwoPhaseProvImpl::Perform\n
valueSessionid != nullptr
failed to create euiccSig CF Object\n
kBBUReturnEOF
kBBUReturnAPTicketReadContentFailed
/root/Library/Lockdown
reg
Couldn't get response payload %s\n
mipc::MIPC_SIM_STATUS_CARD_RESTRICTED
VinylTwoPhasePresenceCheck
ps
/Library/mad
aks_run_internal_test
Failed to verify pairing with status %d, fail the restore \n
Performing SetCardMode(kOpModeRestore)\n
Store data Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Payload = %s\n
MapMetaData Creation failed for the LPA Request\n
/Library/Caches
/Library/CoreBrightness
/Library/terminus
<var>
CFGetTypeID(outPlist.get()) == CFDictionaryGetTypeID()
ManagePairingGetNonce Sep_Cmd_Cnf failed, result 0x%x\n
kBBUReturnFailedSetNVItems
/Managed Preferences
aks_fv_new_vek
SwitchSimMuxCfgPolled: timed out after %d polls\n
com.apple.VinylCommunicationMisc
BBUPurpleReverseProxy
Finalize_Perso_Cnf returned error[%s].\n
HandleInstallationResult
DR_Success == der_ret && TwoPhaseProv::TAG_RNLR == dec.tag
metaDictRef is null\n
/MobileAsset
GetSIMSKUID error %d status 0x%hhx\n
Unhandled radio(%d) type or no radio\n
Delete Profile Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Payload = %s\n
mipc::MIPC_SIM_STATUS_NOT_INSERT
mipc::MIPC_SIM_STATUS_SEP_AUTH_UNPAIRED
Init_Perso_Cnf returned error[%s].\n
failed to create deviceUDID CF Object\n
eUUID provisioning failed: BCOM profile(s) found on device.\nTo resolve: Remove all BCOM profiles and retry provisioning.\nSee BCOM Profilelist payload below for details.\n
StoreData Command failed\n
Router server was not instantiated by VinylRestore to stop it.\n
TAG_PBI == dec.tag
LPA Signed Data to be sent to server in dictionary format %s\n
GetEUICCDataNonce
Failed to convert string value to UTF8 at index %ld\n
SystemRoot
/preferences
getConfigId: Sending ConfigurationRequest for configId\n
Creating sequence using Key, Value pair failed\n
Timeout waiting for confirmation on Status Req.\n
sizeof(resultTo1stCommand) == HDLCFrameGetPayloadLength(&rsp)
The format specifier contains malformed Unicode characters
debugArgs             
kBBUReturnBadEnvironment
/Library/ManagedAssets
GetData() output not valid and isAbsentOK = false. than restore should mandatory fail for all operation except getEID operation\n
sending ConfigId Request
euiccCertificate:: \n
GetWrapKeyServerRequest.plist
VinylInstallSealingManifest
/Library/CallHistoryDB
aks_kext_get_options
Deserialized plist data is not a dictionary: %s\n
SIM Status Req attempt %d failed.\n
Switch_Mode_Cnf not successful, result 0x%x sw1_sw2 0x%hx\n
profile
akstest_rewrap_ek
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapKey failed with 0x%x%s\n
AppleKeyStore
Error: failed to get slot info from BB\n
DR_Success == der_ret && TAG_EUUID == dec.tag && LENGTH_TAG_EUUID == dec.content.length
An argument index may not have a negative value
Failed to ManagePairingGetNonce status %d\n
To be signed dictionary is NULL\n
kVinylResultSuccess == ret && sw == 0x9000
accepted
(ret == DR_Success) && (sm_decoded.eid.length > 0) && (sm_decoded.transactionId.length > 0)
kBBUReturnDSPImageError
/log/com.apple.xpc.launchd
configIdProvURL             
The config Id request was not made, but the response is not for it, instead it is %d\n
AuthenticatePersoDeviceRequest.bin
The precision option does not contain a value or an argument index
zero-padding
BPPMetaData
DR_Success == enc_ret
VinylKTLEUICC::perform: response unpack failed\n
call with %p different from fTransportCreated(%p)\n
BBULog
 dir: %s %i\n
file: %s %i\n
Fail to SetCardMode(kOpModeRestore)\n
SwitchSimMuxCfgPolled: GetSimMuxCfg BUSY on poll %d/%d, MUX still switching\n
euicceumCertificate:: \n
TwoPhaseProv::IsNotificationSentRspSuccess(euicc_rsp)
ret
BUSY
eidSharedRef
/log
response.hwSetRsp == MgrSetSIMHWSetResultType::kSuccess
VinylPairingAuthTest
signedPayload != nullptr
euiccSig != nullptr
OPER_NOT_SUPPORTED
inData
/db/com.apple.xpc.launchd
In VINYL_OPERATION_REFURB\n
mipc::MIPC_SIM_STATUS_PH_NET_PIN
BasebandUpdater
profile returned with presence check on, returning success\n
aks
Fail to ResetCard\n
VinylDaleCommunication
Init_Perso_Req not successful, result 0x%x
an integer
/usr/lib/libnfrestore.dylib
Assertion failure ( pfnNfRestoreOpenWithSE != __null && \"Could not find NfRestoreSEOpenWithError symbol\\n\" )
kBBUReturnInternalError
kBBUReturnFileError
euiccSignedLPAData
BypassPairing
VinylControllerTwoPhaseProvisioning
Failed to encode value at index %ld\n
kBBUReturnFSMNoTransitionDefined
kBBUReturnFailedCreateController
/Library/DeviceRegistry.state
geteUUID: Failed to decode eUUID from response\n
Timeout waiting for confirmation on Switch Mode Req.\n
89[0-9]{14}9[34567][0-9]{14}
kBBUReturnARTMismatchedError
Failed to start router server due to timeout\n
DR_Success == DERDecodeSeqNext(&seq, &decoded)
kBBUReturnManifestNoHashes
aks_fs_supports_enhanced_apfs
ManagePairingGetNonce result %d SW1_SW2 0x%04X length %d\n
ind.fTlv_Result && *ind.fTlv_Result == mipc::MIPC_DALE_VINYL_CMD_RESULT_SUCCESS
Error: GetData() output not valid and isAbsentOK = false. kBBUReturnGetEIDFailure will be reported as kVinylResultDataMissing!\n
VinylUse4FF
Assertion failure ( lib != __null && \"Could not find /usr/lib/libnfrestore.dylib\" )
DR_EndOfSequence == der_ret
data
/Library/FrontBoard
In GetParametersDummy\n
future.get()
!performOptions.twoPhaseUrl.empty()
BBUpdater
kBBUReturnTooManyReperso
CLASS D
vinylValve
Failed to handle configId Provisioning : %d\n
(ret == DR_Success)
 does not allow the 
All
internalBuild         
ErrorCode
/mnt4/wireless/Library/Logs/CrashReporter/Vinyl/Baseband/baseband_updater_logs/
mipc::MIPC_SIM_STATUS_PH_CORP_PUK
kBBUReturnTryAgain
kBBUReturnFailedStartProvisioning
/Library/Preferences
Failed to get data from UIM\n
current_fw_version %s main_fw_nonce 0x%s gold_fw_nonce 0x%s\n
2
GetWrapKeyServerResponse.plist
=========== Vinyl eUICC Options ============\n
/logs/BurnIn
/Library/DataAccess
rsp.Valid() && rsp.contents.rsp_len
Getdata_Cnf returned error[%s].\n
ResponseDataFlag
kVinylResultSuccess == result
/Library/Logs
VinylCommunication::create
kBBUReturnServerError
No transport available.. bail out\n
ari
Finalize_Perso_Req not successful, result 0x%x
InstallPairingMSM Sep_Cmd_Cnf failed, result 0x%x\n
der_ret == DR_EndOfSequence
eid
kBBUReturnGetManifestStatusFailed
::
ind.fTlv_Cmd_Id
ManagePairingAuthenticate Sep_Cmd_Cnf returned error[%s]\n
Assertion failure ( nullptr != fTransportCreated && \"Telephony util transport error.\" )
kVinylResultSuccess == handle_result_ret
!performOptions.configIdProvURL.empty()
KERN_SUCCESS == kr
kBBUReturnAlreadyStarted
GetSimMuxCfg: failed, result=%s(%d)\n
Router server was not instantiated by VinylRestore to start it.\n
eUICCSEPVerifyPairing     
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/NonUpdate/VinylRouterClient.cpp
v12@?0i8
The replacement field misses a terminating '}'
((operation >= kVinylOperationGetEid) && (operation < kVinylOperationNone))
DR_Success == der_ret && TAG_LN == dec.tag
DR_Success == DERDecodeSeqNext(&seq, &dec)
(kVinylResultSuccess == result) && (configId.size() == LENGTH_OF_CONFIGID)
kBBUReturnRetryError
logging
SendReceipt
No router server available.. bail out\n
sepIndSuccess_
kBBUReturnLibFDRDynLibNotLinked
/Managed Preferences/mobile
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEKWK failed with 0x%x%s\n
eUICCPublicKey:: \n
Delete Profile Cmd_Req returned error[%s].\n
The format specifier should consume the input or end with a '}'
deviceSerialNumberData != nullptr
kAKSReturnSuccess == auth_ret
GetData IBIVinylResult 0x%x\n
!GET_RSP_FIELD(rsp, result_t3)
Failed to InstallPairingMSM result %d SW1_SW2 0x%04x\n
VinylOnlyPerso
(kVinylResultSuccess == sessionData.extractDataFromPir(*pir))
Failed to encode KeyValuePair sequence at index %ld\n
w
Invalid GetData response from the BB\n
SIM still initializing, trying again... sim_state 0x%x (retryCount: %d, retryLimit: %d)\n
Proxy Aborted? %d\n
SendReceiptServerRequest.plist
Timeout waiting for confirmation on Init Perso Req.\n
mipc::MIPC_SIM_STATUS_PH_NETSUB_PUK
Assertion failure ( success && \"Unrecognized radio type.\" )
Using automatic argument numbering in manual argument numbering mode
status 0x%hhx cards_type: %hhu \n
Failed to complete FinalizePerso command\n
Finalize_Perso_Req sent: Msg=0x%x fTlv_Payload = %s\n
VinylTwoPhaseUrl
DR_Success == der_ret && TAG_PIL_ICCID == iccid_dec.tag
(ret == DR_Success) && (ssp_decoded.eUICCSessionId.length > 0)
0x{:04x}
dict
handle_signals
could not create file: %s (%s)\n
aks_fv_set_protection
Failed to StoreData status %hhu SW1 0x%x SW2 0x%x\n
capabilities::euicc::supportsVinylSEPPairing()
mipc::MIPC_SIM_STATUS_SIM_PUK2
(fr_decoded.successResult.length > 0) || (fr_decoded.errorResult.length > 0)
nonce
_networkd
/Library/SoftwareUpdate
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestCheckClass failed with 0x%x%s\n
FirmwareLoaderVersion
ManagePairingAuthenticate Sep_Cmd_Ind Sep_Cmd_Cnf\n
IsNotificationSentRspSuccess( euicc_rsp )
/Library/Carrier Bundles
Authentication with card failed\n
eUICCVinylDALValve::ResetCard not supported\n
Sep_Cmd_Ind failed, result 0x%x\n
The fill option contains an invalid value
/installd
ManagePairingGetNonce returning success\n
Failed to get info: %d\n
X-Apple-Alder-IP
Sep_Cmd_Ind nonce size = %zu, should be %d\n
ManagePairingAuthenticate Sep_Cmd_Cnf failed, result 0x%x\n
0x{:02x}
Failed to assign request data\n
eUICC feed containing signed LPA data sent to server successfully\n
Failed to LpaSigningRequest status %d SW1_SW2 0x%x rsp_len %u\n
The format specifier for 
SerialNumber
kBBUReturnFileMismatch
 -- middle of buffer snipped -- \n
failed to write restore bag to disk %s\n
shared allow list:
Performing SEP-eUICC pairing authentication %d/%d\n
SwitchSimMuxCfgPolled: GetSimMuxCfg failed on poll %d/%d\n
assign
Failed to GetEID but it is fine because BB Provisioning not enabled or it is enabled but Vinyl Provisioning Skipped\n
responseNonceFromServer != nullptr
kBBUReturnNVMImageError
isAbsentOkay result %d hardwareHasESIM: %d\n
mipc::MIPC_SIM_STATUS_SIM_PUK
failed to get ConfigId from eUICC\n
Encoded KeyValuePair %ld: key='%s', value type=%ld\n
kBBUReturnMultipleDevices
kBBUReturnGetMEIDFailure
kBBUReturnSWIDMismatchForHW
kBBUReturnInvalidTransportType
Failed to get PRP\n
CreateValidationBlob DR %d\n
VinylETLEUICC
VinylEURCommunication
TAG_SEQN == dec.tag
failed to convert deviceSerialNumber to CFData\n
postresetdelay
_wireless
Cleaning up VinylController object \n
mipc::MIPC_SIM_STATUS_PH_CORP_PIN
Validate_Perso_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s fTlv_Payload = %s\n
VinylForceGold
Personalized
The argument index is invalid
persoStatic           
kPSIM1
chip_id 0x%x stream_apdu_max_apdus 0x%x isAbsentOk: %s\n
Bootstrap
Extract Notification Sequence number failed\n
Dump: %s\n
module_verbosity
misc
kPSIM1_TOONIE
operator=
Switch_Mode_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s\n
Options
/Library/MediaStream
/Library/DeviceRegistry
MAV radio %d eSIM lookup not supported!\n
resetting refurb fw with perso supported in an attempt to clear perso\n
SessionId
akstest_new_ekwk
SwitchModeReq result 0x%x sw1_sw2 0x%hx\n
IODeviceTree:/filesystems
infoSharedRef
Calloc dict values failed\n
BasebandEnableProvisioning
kBBUReturnDBLImageError
/run
/Library/CrashReporter
/Library/ApplePushService
outData
Failed to ManagePairingGetNonce result %d SW1_SW2 0x%x\n
Error: only kTelephonyRadioVendorINT has IBIVinylSimCardResetReq, current RadioVendor = %d\n
0123456789abcdef
Bootstrap Preferences
Assertion failure ( pfnNfRestoreDumpUART != __null && \"Could not find pfnNfRestoreDumpUART symbol\\n\" )
kBBUReturnBasebandUnresponsive
wheel
kVinylPersoState
InstallPairingMSM Sep_Cmd_Cnf fail\n
 Initializing KTL options struct, opening ARI channel\n
nullptr == sessionData.getError().get()
ECID: 0x%llx\n
euiccSessionId
/MobileDevice/ProvisioningProfiles
Failed to AuthPerso status %d SW1_SW2 0x%x rsp_len %u\n
FinalizePersoDevice %d\n
forceMain             
Assertion failure ( pfnNfRestoreSEClose != __null && \"Could not find NfRestoreSEClose symbol\\n\" )
kPSIM1_LOONIE
Failed to complete InitPerso command\n
eUICC not stuffed but that's ok!\n
Clear All eSIM Preferences
DeviceUDID
metaDictRef is empty\n
performBootup
skip_fusing_validation
getConfigId: Failed to decode ConfigId from response\n
Error: invalid simSKUID = %u\n
kPSIM1_HALLEY
loader_version 0x%s key_id 0x%s perso %d\n
Auth_Perso_Req sent: Msg=0x%x fTlv_Payload = %s\n
key != nullptr && value != nullptr
0123456789ABCDEF
%s:%spid:%d,%s:%s%s%s%s%s%u:%s options value 0x%llx exceeds uint32_t%s\n
Vinyl Secure Element object not created, cannot power up SE\n
Yes
com.apple.telephony.control-msg.xpc.allow
mipc::MIPC_SIM_STATUS_PH_SP_PIN
Delaying for 6FA5 handling\n
VinylClearMetadata::Perform: onlyBootstrap=%d\n
kBBUReturnAborted
kBBUReturnProgrammerItemLoadingFailed
isLETOCapable: hwIdSimConfig[3]=%d, capable=%s\n
eUICCVinylValve
link.accepter.local
Validate_Perso_Req not successful, result 0x%x\n
sizeof(result) == HDLCFrameGetPayloadLength(&rsp)
failed to get deviceUDID from MobileGestalt\n
fakefuse
/Library/SpringBoard
InstallPairingMSM Sep_Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Msm = %s\n
%@
fail to free transport: %p\n
Assertion failure ( nullptr == fTransportCreated && \"Telephony transport error.\" )
Delete All Profiles
count > 0
root
EscrowTokenPeriod
kVinylSIMSKUID
Null rsp dictionary reference passed\n
AuthenticatePersoDevice %d\n
DR_Success == DERParseInteger(&dec_nested.content, &err_val)
failed to create euiccCertificate CF Object\n
Successfully created mapMetaDataPayLoad (%zu bytes)\n
/Library/Logs/CrashReporter
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unpack data failed%s\n
refurbAction: %d\n
DR_Success == ret
mipc::MIPC_SIM_STATUS_SEP_AUTH_FAILED
locale-specific form
DR_Success == DERDecodeSeqContentInit(&pbi_der, &seq)
VinylClearMetadata
kBBUReturnNoMemory
/.exclave
TelephonyRadiosGetRadioVendor %d not supported!
euiccCertificate
SendReceiptServer %d\n
SE closed SUCCESSFULLY\n
/mnt4
/Library/IdentityServices
/Media/Downloads
B16@?0^{_ftsent=^{_ftsent}^{_ftsent}^{_ftsent}q^v**iiSSQiSsSSS^{stat}[1c]}8
kToBeSignedPayload
Integral value outside the range of the char type
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Communication/ICE/VinylICECommunication.cpp
kBBUReturnResetToPBL
/mobile
Failed to verify pairing: %d\n
result  0x%x \n
cardData.contents.perso
The type option contains an invalid value for 
infnanINFNAN
TAG_NM == dec.tag
%s: mode=%o, u/g=%i:%i class=%i%s\n
GET_RSP_FIELD(rsp, sw1_sw2_t6) == 0x9000
Timeout waiting for indication on InstallPairingMSM Sep_Cmd_Req\n
matched refurb profileReference\n
euiccCertificate != nullptr
kBBUReturnProtocolError
kBBUReturnBBInitStatusTimeout
kBBUReturnGetPersonalizationInfoFailed
MSMVectorBlob %s\n
Performing SetCardMode(kOpModeNormal)\n
Payload too large -- payload_size: %zu exceeds uint16_t maximum\n
Failed to GetNcCfgRequest status %d\n
v24@?0{shared_ptr<ctu::Http::HttpResponse>=^{HttpResponse}^{__shared_weak_count}}8
DR_Success == der_ret && TAG_RNLR_NL == dec.tag
kBBUReturnSysctlError
/wireless
euiccSignedLPAData:: \n
eumCertificate:: \n
EoS_Getdata_Cnf returned error[%s].\n
End of input while parsing an argument index
INSTALLED
LogDirectory
/Media
/Library/adi
DR_Success == derRet
SendReceiptServerResponse.plist
kBBUReturnGetPkHashFailure
/Library/MobileBluetooth
/Library/MedicalID
eumCertificate
VinylConfigIdProv
kBBUReturnMIImageError
/Library/DeviceRegistry.dontBackUp
(%s:%d) Array assignment too large(%p), got(%zu) max(%zu)
inDict
mipc::MIPC_SIM_STATUS_PH_NET_PUK
@
ntf
ldr ver %04X not eligible, skipping\n
Failed to convert key to UTF8 at index %ld\n
Failed to encode key at index %ld\n
Condition <<%s>> failed %s %s/%d\n
No valid GetData found and trying to reset Vinyl.\n
Missing X-Apple-Alder-IP header in response, sticky session not active\n
Failed to encode final mapMetaData SEQUENCE\n
IODeviceTree:/options
kBBUReturnBadManifestStatus
!performOptions.alderHostname.empty()
NfRestoreDumpUART
DR_Success == der_ret && TAG_NML == dec.tag
/Library/ISP
eumCertificate != nullptr
iccid
v24@?0i8^v12I20
Delete All Non-Bootstrap Profiles
VinylSecureElement
nsr_req.get()
failed to create configIdData CF Object\n
No operation requested in options\n
Return 16 byte zero EID as pairing identifier\n
kBBUReturnSuccess == ret
 TelephonyBasebandPCITransportCreate returns: %s\n
geteUUID: StoreData failed with result %d, sw=0x%04x\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/NonUpdate/VinylPairing.cpp
VinylPairing
Timeout waiting for indications on Cmd Req store data.\n
Using manual argument numbering in automatic argument numbering mode
End of input while parsing format specifier precision
%s\n
getDataRsp.Valid()
Invalid delete action: %d (expected 0 or 1)\n
Failed to handle bootstrap provisioning operation, ret %d\n
mipc::MIPC_SIM_STATUS_SIM_PIN
DR_Success == der_ret && TAG_PIR == dec.tag
metaDictRef != nullptr
kBBUReturnFlashError
/.overprovisioning_file
/Library/Keyboard
Failed to Pairing authenticate result %d SW1_SW2 0x%04x\n
VinylKTLEUICC::perform: KTLRawSendData failed\n
parameterCount > 0
No Action
BBUpdaterExecCommand rejected  with error\n
CLASS B
%s:%spid:%d,%s:%s%s%s%s%s%u:%s fail%s\n
In VINYL_OPERATION_GET_PAIRING_PARAMETERS_DUMMY\n
MSMData
eidValue
Failed to serialize dictionary %s error %s\n
nonce.size() == SEP_NONCE_SZ
failed to convert dictionary to Plist for Nonce response from Server\n
List Delete notification failed\n
VinylTwoPhaseProvSessionData
Failed to GetEuuidRequest status %d\n
GetSimMuxCfg: current sim_cfg=%d\n
NULL requestURL?\n
Replacement argument isn't a standard signed or unsigned integer type
bbupdater: %s
EscrowPasscodePeriod
PRP timed out %d\n
a character
VinylRefurbOption
No profile returned with presence check on, device already has a two-phase bootstrap profile installed\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks connection failed%s\n
DR_Success == der_ret && TAG_EUICCDATAREQ == dec.tag
this->reverseProxySettings
onlyPerso             
Vinyl Operation: %d, lastOperation: %d\n
/Library/BulletinBoard
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewKey failed with 0x%x%s\n
Failed to get nonce\n
eUICCVinylICEValve
decodeConfigIdFromResponse: ConfigID not present in response (found tag=0x%02llx instead of configIDValue), exiting\n
In ManagePairingGetNonce...\n
failed to create deviceUDID\n
kBBUReturnSuccess
kBBUReturnBootedForCoreDump
In VINYL_OPERATION_GET_PAIRING_PARAMS\n
ProfileStatus
der_item.data <= (profile_ref_input.data() + profile_ref_input.size())
ignoremanifest
VinylRestore Options:\n%s\n
Force collecting BB coredump by return error = %d, previous ret = %d\n
Failed to DeleteProfile status %d SW1_SW2 0x%x\n
(der_ret == DR_Success)
EoS_Getdata_Cnf not successful, result 0x%x 
VinylTwoPhaseRefurbRef
EuiccCommandID
HardwareType
Timeout waiting for confirmation on Auth Perso Req.\n
Timeout waiting for confirmation on Finalize Perso Req.\n
-apfs_shared_datavolume
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/CommandDrivers/eUICCVinylMAVValve.cpp
SIM still initializing, trying again... IBIVinylResult 0x%x (retryCount: %d, retryLimit: %d)\n
Failed to create data\n
Init_Perso_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s fTlv_Payload = %s\n
TAG_GPS == dec.tag
com.apple.router.abb
InstallPairingMSM Sep_Cmd_Cnf received: Msg=0x%x fTlv_Result = %s\n
forcePerso            
%u.%03u: %s: %s
values
Status_Req sent: Msg=0x%x fTlv_Mode = %s\n
akstest_check_class
kern.bootargs
Sticky session: X-Apple-Alder-IP = %s\n
updateBaseband false\n
offset + length <= offset_seq_end
Only attach the the existing coredump dir to output dictionary without executing coredump again.\n
RestoreOSBuild
v8@?0
StoreData Command failed with sw %x\n
failure
Creating transport:%p \n
kBBUReturnError
kBBUReturnUMTSBand4CalibrationCheckFailure
/Library/UserConfigurationProfiles
%s/mobile
kPSIM1_PSIM2
Sending geteUUID request\n
fCommunication object not created, cannot free Transport\n
this->serverSessionID && CFStringGetLength( this->serverSessionID.get() ) != 0
The format string terminates at a '{'
Card already perso'ed\n
INVALID_PARAM
Store data Cmd_Ind not successful, result 0x%x\n
delete_req.get()
kVinylResultSuccess == vinyl_ret
failed to create deviceSerialNumber CF Object\n
keyData != nullptr
In VINYL_OPERATION_GET_INFO\n
InitPersoDevice %d\n
Sep_Cmd_Ind received: Msg=%04x fTlv_Cmd_Id = %s fTlv_Result = %s fTlv_Sw = %s fTlv_Nonce = %s\n
sw1_sw2 0x%hx\n
operation == kVinylOperationNonUpdate
Invalid dictionary returned from getEID\n
euicceumCertificate
Failed to complete ValidatePerso command\n
ProfileInstallationResult
/mnt3/bbfs/
kBBUReturnRawBinaryImageError
failed to open userclient via %s: %d\n
kVinylSIMSKU
In VINYL_OPERATION_GET_PAIRING_IDENTIFIER\n
0x{:08x}
Successfully created LPASigningRequest (%zu bytes)\n
%i
%s:%spid:%d,%s:%s%s%s%s%s%u:%s count %llu exceeds max %u%s\n
eUICCSepPairingBypassValue 
failed to parse LPA signed data\n
failed to create dict CF Object\n
DR_Success == der_ret && TAG_PILR == dec.tag
kBBUReturnTransferTerminated
/containers
/Library/Cookies
/Library/Fonts
payload.size() <= MAX_SEP_SIGNED_AUTH_SZ
DR_Success == der_ret && TAG_NS == dec.tag
deviceSerialNumber && deviceSerialNumber.get()
failed to create deviceSerialNumber\n
ecid != 0
/mnt5
kBBUReturnTUTransportError
 (skip)
Error: failed to SwitchCardMode\n
Calloc dict keys failed\n
!ind.isError()
The type does not fit in the mask
%s%s
decode_pfk_bulk_entry
UNKNOWN
force
GetWrapKey
mobile
VinylKTLEUICC::perform: KTLUTACopyReceiveData failed\n
Failed to register for proxy\n
kBBUReturnMDMDDRImageError
%s:%spid:%d,%s:%s%s%s%s%s%u:%s bad 1%s\n
basic_string
mipc::MIPC_SIM_STATUS_CARD_REBOOT
GetBppResp
ff_first_stage
/Library/MobileInstallation
eUICCPublicKey
InitPersoServer %d\n
Clear Bootstrap eSIM Preferences
DR_Success == der_ret && top_level_tag == dec.tag
Send Command to Nonce to Marina Server Failed\n
Performing ManagePairingGetNonce\n
hwType.Valid()
localAccepter
APIVersion
DR_Success == der_ret && TAG_DP_RESULT == dec.tag
NVRAM '%s' exists? %s\n
kBBUReturnFailedFinishProvisioning
kBBUReturnFusingSourceError
!url.empty() && urlRef
kBBUReturnFailCreateTransportInitial
/.ssh
/Library/WebClips
Failed to assign output data\n
Notification Response decoding failed\n
/Library/NanoPreferencesSync
/Library/ControlCenter
eUICCVinylFactory
no profile available nor installed , skipping\n
LPA Signed Data to be sent to server in hex format\n
ff_ping
/Library/Trial
/db
Failed to create dictionary\n
VinylTwoPhaseEidMask
kBBUReturnManifestStatusNonZeroError
kBBUReturnGetChipIDFailure
UpdateBaseband
CFGetTypeID( ps ) == CFStringGetTypeID()
kBBUReturnGetSessionKeyFailure
InitPersoServerRequest.plist
kVinylResultSuccess == ret
kBBUReturnPowercycleAfterFusing
kBBUReturnInitializeRingBufferError
kBBUReturnAPTicketFileInitFailed
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 1)%s\n
aks_get_convenience_bio_state
Failed to retrieve EID: %d\n
SwitchSimMuxCfgPolled: MUX settled to wrong config, current=%d expected=%d\n
/Containers
/Library/TCC
In ManagePairingAuthenticate...\n
failed to create EID CF Object\n
VinylClearMetadata::GetListOfIccids: Requesting Profile List\n
(DR_Success == ret)
/Library/Accounts
%s:%spid:%d,%s:%s%s%s%s%s%u:%s ioreg: %d, boot_arg: %d%s\n
v28@?0i8^v12^v20
alternate form
KERN_SUCCESS == kr && nvramInfo
akstest_new_key
e-apfs
Router server started.\n
ManagePairingAuthenticate Sep_Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Signed_Auth = %s fTlv_Nonce = %s\n
/logs/AppleSupport
aks_fv_unwrap_vek_with_acm
UTF8 string encoding for key failed\n
Failed to deserialize dictionary %s error %s\n
Timeout waiting for confirmation on EoS Get Data Req.\n
Auth_Perso_Req not successful, result 0x%x
a pointer
:
MGCopyAnswer
IOService:/IOResources/AppleKeyStore
Failed to complete secure perso: %d\n
Error: failed to perform ResetSimCard\n
VinylForceGenericUpdate
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Communication/Dale/VinylDaleCommunication.cpp
client rsp data: %s\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 3)%s\n
.
Performing ResetCard\n
Empty euuid data received\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/NonUpdate/VinyleUICC.cpp
xmissiontimeout
aks_fv_new_kek
CLASS C
sw == 0x9000
Failed to handle config id provisioning operation, ret %d\n
kINVALID
respDict
-f
kBBUReturnFirmwareDataError
failed to open connection to %s: %d\n
SwitchCardMode: Failed err %d status %hhu mode %d sw1 0x%x sw2 0x%x\n
router.client.vinylrestore
kBBUReturnEBLImageError
(snipped)\n
 formatting argument
performCoreDump
kBBUReturnNAKManifest
kBBUReturnInvalidProgrammerItemType
/Library/Logs/AppleSupport
Finalize_Perso_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s\n
gap 
CFEqual(cmd, Alder::ValueCommandGetBppResp)
%s:\n\tNum files:\t%u,\n\tNum hardlinks:\t%u,\n\tNum compressed:\t%u,\n\tTotal Size:\t%lld,\n\tMin File Size:\t%lld,\n\tMax File Size:\t%lld,\n
%s%s\n
geteUUIDBootstrapV2 not supported\n
Unknown sim status
euiccPublicKey != nullptr
Failed to power SE, during Vinyl Operation %d \n
After check， card mode was not successfully set to normal\n
Router server stopping.\n
true
DR_Success == der_ret && TAG_PILR_OK == dec.tag
kBBUReturnGetBootupTimeError
kBBUReturnFDRDataValidationFailed
Fail to create transport: %d\n
EoS_Getdata_Req sent: Msg=0x%x fTlv_Is_Num_Of_Profile_Needed = %s\n
twoPhasePresenceCheck 
BBUpdaterExtremeCreateWithError rejected with error\n
cmd
user allow list:
SwitchCardMode: Baseband already in mode %hhu\n
Failed to InitPerso status %d SW1_SW2 0x%x rsp_len %u\n
mipc::MIPC_SIM_STATUS_COMPLETE_READY
mipc::MIPC_SIM_STATUS_PH_NETSUB_PIN
\n
kBBUReturnFFSimError
In VINYL_OPERATION_VERFIY_PAIRING_PARAMS\n
hash %s\n
Payload too large -- payload_size: %d  max allowed: %lu)\n
fs == std::future_status::ready
Nonce
kBBUReturnGetFirmwareVersionFailed
CLASS A
GetSimMuxCfg: sim_cfg_req field not present in response\n
ManagePairingGetNonce Sep_Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s\n
Delete Profile Cmd_Cnf received: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Result = %s\n
precision
Send LPA Command to eUICC Failed \n
pingattempts
ff_bootup
_aks_operation
Router server starting.\n
All Preferences
Delete BCOM notification on eUICC\n
kBBUReturnGetSerialNumberFailure
kBBUReturnAllocationFailed
/root/Library/Logs
VinylController
No
Failed to ManagePairingAuthenticate status %d\n
The type option contains an invalid value for a string formatting argument
options && !options->twoPhaseRefurbRef.empty()
RemoteFSRoot
kBBUReturnDownloadImageError
kBBUReturnBBTicketDecodeError
Failed to push minimal sealing manifest to the card\n
Octect string encoding for value failed\n
InstallPairingMSM Sep_Cmd_Ind Fail\n
request to free transport: %p\n
Invalid ECID received\n
/root/Library/MobileContainerManager
/Library/Passes
/Library/NFStorage
entering VinylController::create\n
simSKUID < ARR_SIZE(MAVHWSIMSKUStr)
%s: (%s:%d) Range assignment too large(%p), got(%ld) max(%ld)
%s: (%s:%d) Array assignment too large(%p), got(%zu) max(%zu)
```
