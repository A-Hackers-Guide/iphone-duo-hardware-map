# `/usr/lib/updaters/libVinylUpdater.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 843,840 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 41 (Size: 4112)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (24)

- `/usr/lib/updaters/libVinylUpdater.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/AppleBasebandLink.framework/AppleBasebandLink (compatibility version 1.0.0, current version 0.0.0, weak)`
- `/System/Library/PrivateFrameworks/AppleMipcRouter.framework/AppleMipcRouter (compatibility version 1.0.0, current version 0.0.0, weak)`
- `/usr/lib/libMIPCSdk.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libHDLCDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libReverseProxyDevice.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/AppleConvergedFirmwareUpdater.framework/AppleConvergedFirmwareUpdater (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libKTLDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libARI.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libBBUpdaterDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyCapabilities.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libTelephonyBasebandDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libPCITransport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libETLDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`

## Entitlements

```xml
  - no entitlements
```

## Strings (1,418)

```
Pairing Operation Not supported continue with Vinyl Operation
eUICCVinylValve
successfully streamed recovery Firmware\n
invalid input params
GetNonceServerRequest.plist
SwitchModeReq result 0x%x sw1_sw2 0x%hx\n
eUICC enabled, mux switch success!\n
The argument index starts with an invalid character
kBBUReturnInvalidRadioType
Install_Vad_Req sent: Msg=0x%x fTlv_Payload = %s\n
eUICCFwReaderFindAndCopyFileData
link.accepter.local
The type does not fit in the mask
%s::%s: Vinyl Update is complete!\n
DR_Success == der_ret && TAG_EUUID == dec.tag && LENGTH_TAG_EUUID == dec.content.length
kBBUReturnManifestImageError
Timeout waiting for confirmation on Status Req.\n
twoPhaseEidMask       
v12@?0i8
kBBUReturnBBTicketMallocFailed
InstallPairingMSM Sep_Cmd_Cnf returned error[%s]\n
gatherPreflightParameters
Missing or empty server sssion?! %s\n
%s::%s: failed to create goldDict\n
GetSimMuxCfg: failed, result=%s(%d)\n
mipc::MIPC_SIM_STATUS_SIM_PUK2
eUICC,Ticket
kVinylFwUpdateEuiccChipId
Failed to complete FinalizePerso command\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/CommandDrivers/eUICCCommon.cpp
goldFwMac
Status_Req sent: Msg=0x%x fTlv_Mode = %s\n
Init_Perso_Req not successful, result 0x%x
createIm4p
sim_state 0x%x, sim_error_cause 0x%x\n
%s::%s: failed to init logging\n
Main version strings mismatched: Card %s Bundle %s
future.get()
%s::%s: plistFileName %s\n
Empty payload data received\n
Install gold but no ticket -- back to restored please\n
kBBUReturnBadManifestStatus
kBBUReturnRetryError
Getdata_Cnf returned error[%s].\n
Nonce
filename 
Failed to deserialize dictionary %s error %s\n
fwFilePath : 
The argument index value is too large for the number of arguments supplied
kBBUReturnSWIDMismatchForHW
router.client.vinylrestore
ManagePairingAuthenticate Sep_Cmd_Cnf fail\n
init
GetWrapKeyServerRequest.plist
0X
Failed to InitPerso status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
kBBUReturnInvalidTransportType
mipc::MIPC_SIM_STATUS_COMPLETE_READY
onlyPerso             
Only attach the the existing coredump dir to output dictionary without executing coredump again.\n
getFileDataFromZip fwSrcPath: 
kBBUReturnGetEIDFailure
postresetdelay
kDeviceIdentifier
%02x
fRouterServer
Failed to store data status %d SW1_SW2 0x%x\n
Ticket provided is larger than spec. [ %lu (lenth) > %lu (spec max) ] \n
00000000000000000000000000000000
failed to create Vinyl CFType object
mainFirmware
Cleaning up VinylController object \n
this->reverseProxySettings
%s::%s: failed to read zip file\n
fRouterServerGood
sw == 0x9000
Unknown sim status
(snipped)\n
a pointer
error %d status %u sw1_sw2 0x%x\n
eUICC,EID
inRestoreOS: %d\n
Assertion failure ( pfnNfRestoreSEClose != __null && \"Could not find NfRestoreSEClose symbol\\n\" )
Error: failed to get SimConfig info from BB\n
ManagePairingGetNonce Sep_Cmd_Cnf returned error[%s]\n
forceGold             
SE closed SUCCESSFULLY\n
array : 
SwitchSimMuxCfgPolled: MUX switch confirmed after %d poll(s)\n
0b
Ret %d from state %s next %s\n
UpdateMain
mipc::MIPC_SIM_STATUS_BUSY
xmissiontimeout
Could not load NVRAM? %d\n
getFileDataFromZip
%s::%s: Invalid plistDict\n
Failed to correct result %d\n
VinylRestore object doesn't exist
kBBUReturnBasebandUnresponsive
kBBUReturnFusingVerificationFailed
Ticket provided is larger than spec. [ %ld (lenth) > %d (spec max) ] \n
eUICCFwReader
getPathComponent
%s::%s: certPlusLdrVer memory alloc failed\n
Install_Fw_Req returned error[%s].\n
%s::%s: VinylRestore: constructor\n
IODeviceTree:/options
Functionality not implemented.\n
VinylFirmwareCreate
sim_state 0x%x sim_error_cause: 0x%x sim_ext_capabilities 0x%x isAbsentOk: %s\n
%s::%s: failed to create restore object\n
eUICC,ProfileDataGold
mipc::MIPC_SIM_STATUS_PH_NET_PUK
Install_Fw_Cnf result 0x%x sw1_sw2 0x%hx\n
options: 
Condition <<%s>> failed %s %s/%d\n
The argument index should end with a ':' or a '}'
%s::%s: empty implementation not expected to be called\n
kBBUReturnTryAgain
kBBUReturnInitializerPrepError
performCmd
eUICC,GoldFwMac
NVRAM: %s\n
%s::%s: AMSupportDigestSha256 failed:\n
{:02x}
Success!\n
kBBUReturnKeysNotAligned
SwitchSimMuxCfgPolled: perform failed\n
successfully switched back to Normal\n
tag4cc : 
01234567
rsp
Result %d next state %s allowRetry %d\n
InstallPairingMSM Sep_Cmd_Cnf fail\n
geteUUIDBootstrapV2 not supported\n
Delete Profile Cmd_Req returned error[%s].\n
FirmwareLoaderVersion
logLevel=%d
Failed to handle Refurb operation, ret %d\n
%s::%s: failed to update FW, ret value = %d\n
ManagePairingGetNonce Sep_Cmd_Cnf received: Msg=0x%x fTlv_Result = %s\n
postProcess           
ff_create_transport
Router server started.\n
Router server was not instantiated by VinylRestore to start it.\n
kBBUReturnManifestStatusNonZeroError
mipc::MIPC_SIM_STATUS_NOT_INSERT
Core dump successful \n
%s::%s: fwldrver is null\n
zero-padding
<VinylRestoreObj %p [%p]>{}
kBBUReturnMRCImageError
ManagePairingAuthenticate Sep_Cmd_Cnf returned error[%s]\n
alderHost             
Failed to assign output data\n
setRecoveryFwInfo
VinylForceGenericUpdate
precision
Timeout waiting for confirmation on install vad req.\n
ManagePairingAuthenticate has cached succeed result, no following indication\n
xporttimeout
/mnt5
%s::%s: failed to get byte ptr of fwldrver\n
Start
%s::%s: success value %d\n
Router server stopped.\n
GetData IBIVinylResult 0x%x\n
client rsp data: %s\n
%s::%s: entering: VinylUpdater: %s command: %s\n
decodeConfigIdFromResponse: Received error response with code %d\n
kBBUReturnDownloadImageError
Install_Vad_Req returned error[%s].\n
kBBUReturnPingtimeout
Timeout waiting for indication on ManagePairingAuthenticate Sep_Cmd_Req\n
uimSlot               
forceMain             
BBUpdaterExtremeCreateWithError rejected with error\n
%s::%s: failed to get ldrVer\n
Resetting modem: %s\n
ret == kBBUReturnSuccess
getPersoParameters
Init_Perso_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s fTlv_Payload = %s\n
eUICCSepPairingBypassValue 
InitPersoServerResponse.plist
FinalizePersoDevice %d\n
InstallPairingMSM returning success\n
Perso
deviceInfoDict
fCommunication object not created, cannot create Transport\n
com.apple.VinylStatuscallback
w
a floating-point
Failed to StoreData status %hhu SW1 0x%x SW2 0x%x\n
Timeout waiting for confirmation on Validate Perso Req.\n
Options
0x{:02x}
%s::%s: VinylRestore object doesn't exist, this is fatal\n
Install main but no ticket -- back to restored please\n
kPSIM1_TOONIE
createGoldFw
eUICC,Im4pGold
eUICC,GoldRecoveryFw
%s::%s: Failed to alloc memory for main/gold entries\n
0
%s::%s: Failed to execute command %d\n
ManagePairingGetNonce Failed status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
VinylProvisioningURL
twoPhaseRefurbRef     
ff_first_stage
vinylgetFwData fwSrcpath: 
Failed to correct SW during config Id fetch 0x%04x\n
%s::%s: entering: VinylUpdater: %s\n
Failed to FinalizePersoDevice status %hhu SW1 0x%x SW2 0x%x\n
certIdentifier
kBBUReturnTooManyReperso
Sep_Cmd_Ind failed, status word from UICC sw 0x%hx\n
call with %p different from fTransportCreated(%p)\n
Empty implementation for PostProcess. Non updater takes care of refurb options!\n
VinylRestore Options:\n%s\n
kBBUReturnFailedNVSync
VinylPairingAuthTest
/update/gold/info.plist
VinylVerifyPairing
VinylRefurbOption
%s::%s: No updater object passed, this is fatal\n
reg
mipc::MIPC_SIM_STATUS_SEP_AUTH_UNPAIRED
ManagePairingGetNonce Sep_Cmd_Cnf has no fTlv_Result\n
getBoardParameters
mipc::MIPC_SIM_STATUS_PH_SP_PIN
send
com.apple.EmbeddedSoftwareRestore.eUICC.bootloaderVersionsSupported
Invalid external client link instance. \n
Auth_Perso_Req not successful, result 0x%x
AMAuthInstallSupportCopyDataFromHexString
false
kBBUReturnInvalidProgrammerItemType
nonce.size() == SEP_NONCE_SZ
gap 
%s::%s: Failed to build vinyl info.plist dictionary\n
true
kBBUReturnAPTicketReadContentFailed
kBBUReturnMDMDDRImageError
getConfigIdBootstrapV2 not supported\n
ManagePairingGetNonce Sep_Cmd_Cnf failed, result 0x%x\n
VinylTwoPhaseEidMask
stitchImg4Vad
transport %p, status: %#x\n
StreamFirmware failed\n
getConfigId: Sending ConfigurationRequest for configId\n
VinylTransport
mainFwMac
%s::%s: failed to create Controller object\n
GetNonce
result %d code %d raw_error %ld error %s\n
%s::%s: leaving: %s\n
No :-(
GetWrapKeyServer %d\n
%s::%s: Could not create RTKitFirmware\n
updateAllowed
SwitchCardMode: Baseband already in mode %hhu\n
InstallPairingMSM Sep_Cmd_Ind Fail\n
ind.fTlv_Cmd_Id
twoPhaseUrl           
%s::%s: isPreflight: %d isNeRDOS() %d\n
reset
!nonce.empty()
Validate_Perso_Cnf returned error[%s].\n
ff_bootup
%s::%s: basebandFirmwareUpdateInfoDict is NULL\n
VinylKTLEUICC::perform: response unpack failed\n
0123456789abcdef
step
%s::%s: skipAll: %d updateBaseband %d vinylPresent %d\n
cardData.contents.perso
2
VinylDaleCommunication
Payload too large -- payload_size: %zu exceeds uint16_t maximum\n
ManagePairingAuthenticate returning success\n
??????
Error: invalid simSKUID = %u\n
getFileDataFromZip filePath: 
%s::%s: Missing firmwareMac in info.plist -- firmware too old\n
Failed to Pairing authenticate result %d SW1_SW2 0x%04x\n
VinylKTLEUICC
%s::%s: goldIm4p not present in the input\n
kBBUReturnProgrammerConnectionError
kBBUReturnFFSimError
payload.size() <= MAX_MSM_SZ
%s::%s: unexpected debug log path type\n
%s::%s: error getting properlylist\n
Assertion failure ( success && \"Unrecognized radio type.\" )
Options:\n%s\n
mainNonce && mainDict
Getdata_Req sent: Msg=0x%x fTlv_Is_Num_Of_Profile_Needed = %s\n
persoStatic           
kVinylFwUpdateCsn
kNonce
The value of the argument index exceeds its maximum value
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/CommandDrivers/eUICCVinylDALValve.cpp
 option
kBBUReturnFileError
BBUpdater
DATA
StreamFirmware set %d/%zu adpusThisSet %zu\n
decodeConfigIdFromResponse: Found auditResponseOk\n
com.apple.VinylCommunicationMisc
kBBUReturnIOError
All
misc
/AppleInternal/Library/BuildRoots/4~CatVugAdRTUoFSQCa_wMfK3SZQyGVDT9VEArIh8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h
The type option contains an invalid value for 
kBBUReturnGetBootupTimeError
kVinylFwPath: 
%s%03d%s
digestRef: 
VinylKTLEUICC::perform: received NACK\n
decodeConfigIdFromResponse: ConfigID not present in response (found tag=0x%02llx instead of configIDValue), exiting\n
In ManagePairingAuthenticate...\n
performCmd fOptions: 
%s::%s: failed to add certId\n
Router server was not instantiated by VinylRestore to stop it.\n
eUICC Skip All\n
kVinylSIMSKU
fCommunication
kBBUReturnBBTicketReadContentFailed
Getdata_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Is_Not_Personalized = %s fTlv_Sw = %s fTlv_Chip_Id = %s fTlv_Eid = %s\n
kVinylFwUpdateGoldFwMac
inData
The format string terminates at a '{'
%s::%s: diagnostics is not valid\n
VinylSecureElement
%s::%s: entering: generateMeasurementDict\n
GetSimMuxCfg: current sim_cfg=%d\n
locale-specific form
failed to create euiccCSN\n
BBUPurpleReverseProxy
Timeout waiting for confirmation on Init Perso Req.\n
mipc::MIPC_SIM_STATUS_EMPT_EUICC
BBUpdaterSetOptions rejected  with error\n
GetNonceServer %d\n
link accepted failed. t\n
eUICC,MainRecoveryFw
kBBUReturnNeedsMoreInput
/usr/lib/libauthinstall.dylib
%s::%s: failed to create fullURL\n
VinylCommunication
kBBUReturnServerError
kBBUReturnNoBBTicket
In InstallPairingMSM...\n
DebugArgs
module_verbosity
ManagePairingGetNonce result %d SW1_SW2 0x%04X length %d\n
SwitchCardMode: Failed err %d status %hhu mode %d sw1 0x%x sw2 0x%x\n
kVinylRadioType
VinylController
DataRoot
LogDirectory
response
GetWrapKey
%s::%s: Unable to copy the firmware:\n
Failed to perform LPASigning Request status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
UpdateGold
Retry
DR_Success == ret
mipc::MIPC_SIM_STATUS_PH_SP_PUK
Clear All eSIM Preferences
SessionId
The argument index is invalid
%s::%s: failed to create Vinyl CFType object\n
refurbAction: %d\n
kBBUReturnProtocolError
Str && \"StringRef cannot be built from a NULL argument\"
kBBUReturnNAKHello
kBBUReturnLibFDRDynLibNotLinked
 -- middle of buffer snipped -- \n
data : 
%s::%s: srcPath memory alloc failed\n
(%s:%d) Array assignment too large(%p), got(%zu) max(%zu)
Still persod after force?\n
VinylRestoreObjDescribe
kVinylEID
kBBUReturnInitializeRingBufferError
Sep_Cmd_Ind doesn't have fTlv_Cmd_Id\n
mipc::MIPC_SIM_STATUS_PH_NETSUB_PIN
Store data Cmd_Ind received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s fTlv_Payload = %s\n
Validate_Perso_Req not successful, result 0x%x\n
eUICC,MainFwMac
%s::%s: failed stiching img4 and vad\n
Failed to stop router server due to timeout\n
goldFirmware
InstallPairingMSM Sep_Cmd_Cnf received: Msg=0x%x fTlv_Result = %s\n
EID: %s\n
failed to init logging
%s::%s: Updater object created successfully\n
No transport available.. bail out\n
returning deviceInfoDict: 
GetNonceServerResponse.plist
kBBUReturnInvalidBBUStageError
BBULog
%s::%s: leaving: %s due to failure\n
payload.size() <= MAX_SEP_SIGNED_AUTH_SZ
%s::%s: failed to find bbfw item status %d\n
kBBUReturnSuccess
%s::%s: failed to add certId-VAD sequence\n
GET_RSP_FIELD(rsp, result_t3) == IBI_NC_RESULT_SUCCESS
VinylUpdaterIsDone
entering VinylController::create\n
kBBUReturnModemPowercycleError
mipc::MIPC_SIM_STATUS_SIM_PIN
%s::%s: Failed to alloc memory for filename\n
ManagePairingGetNonce Sep_Cmd_Ind fail\n
-
%s::%s: failed to encode img4/vad sequence\n
Router server eror: %s\n
Resetting state machine: %s --> %s\n
Gold FW Macs already matching (no forceGold)\n
kBBUReturnGetManifestStatusFailed
Switch_Mode_Cnf not successful, result 0x%x sw1_sw2 0x%hx\n
SigningFuse
eUICC,ApProductionMode
CFGetTypeID(outPlist.get()) == CFDictionaryGetTypeID()
%s::%s: SM::Recovery -- normal? %d macMatchRequired %d\n
Personalized
%s::%s: create Gold Fw failed\n
kBBUReturnGetPersonalizationInfoFailed
%s::%s: Failed to alloc memory for vinyl dictionary\n
VinylCommunication::create
FirmwareData
%s::%s: kMGQSigningFuse returned NULL\n
InitPersoServer %d\n
AuthenticatePersoDeviceResponse.bin
%s::%s: Get InfoPlist Data from Zip failed\n
plist_filename : 
%s::%s: failed to create dirURL\n
GET_RSP_FIELD(rsp, sw1_sw2_t6) == 0x9000
VinylTwoPhasePresenceCheck
kVinylFwUpdateKeyId
eUICC,ChipID
euig
%s::%s: Get Profile Data from Zip failed\n
decodeConfigIdFromResponse: Successfully extracted configID\n
kBBUReturnBBTicketDERParseErrorForFATPCal
Finalize_Perso_Cnf returned error[%s].\n
Finalize perso failed with sw = %02X.\n
outData
setFwInfo
0x{:08x}
%s::%s: performCmd failed\n
/update/gold/firmware.der
com.apple.EmbeddedSoftwareRestore.eUICC.firmwareMac
createTransport attempt %d/%d\n
kBBUReturnFlashError
Store data Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Payload = %s\n
%s::%s: Failed to get Vinyl Firmware Data\n
ind.fTlv_Sw && *ind.fTlv_Sw == 0x9000
Payload too large -- payload_size: %d  max allowed: %lu)\n
kVinylFirmware
vinylPresent
kBBUReturnProgrammerError
Timeout waiting for confirmation on Cmd Req Delete Profile.\n
vector
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/SecureElement/VinylSecureElement.cpp
%s::%s: failed to open libauthinstall dylib\n
%s::%s: fwSrcPath memory alloc failed\n
%s::%s: leaving: VinylUpdater: %s\n
Unhandled radio(%d) type or no radio\n
%s::%s: goldInfoPlistData not present in the input\n
eUICC,RootKeyIdentifier
Assertion failure ( lib != __null && \"Could not find /usr/lib/libnfrestore.dylib\" )
%s::%s: Failed to alloc create plistFilePath CFString\n
%s::%s: failed to create dirPath\n
GetSimMuxCfg: transient BUSY, result=%s(%d)\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/CommandDrivers/eUICCVinylMAVValve.cpp
Failed to get PRP\n
kBBUReturnFailCreateTransportSecond
InitPersoDevice %d\n
hwType.Valid()
The width option should not have a leading zero
kPSIM1_HALLEY
-c
!!! 
hl:C:v:x:t:r:p:e:c:w:i:s:fUFD:nHSqPV
/mnt3/bbfs/
GetSIMSKUID error %d status 0x%hhx\n
successfully reset the card\n
PRP timed out %d\n
%s::%s: failed to create vController object\n
kBBUReturnManifestNoHashes
0123456789ABCDEF
1.0
generateMeasurement
%s::%s: Invalid input Firmware\n
StoreData Command failed\n
mipc::MIPC_SIM_STATUS_CARD_REBOOT
pargs
X-Apple-Alder-IP
v24@?0{shared_ptr<ctu::Http::HttpResponse>=^{HttpResponse}^{__shared_weak_count}}8
kBBUReturnUnPersonalizedImageError
stall
GetSimMuxCfg: perform failed\n
main_fw_pcf_mac 0x%s gold_fw_pcf_mac 0x%s pcf_version 0x%x\n
DR_Success == der_ret && TAG_CONFIGID_RESPONSE == dec.tag
eUICC HW present is too old so we will skip updating it\n
kBBUReturnFirmwareDataError
Could not find NVRAM via IOKit\n
%s::%s: Memory alloc failed certIds/VadDigest\n
VinylEURCommunication
mipc::MIPC_SIM_STATUS_SIM_PUK
/mnt3
InitPersoDeviceBlob.bin
SendReceiptServer %d\n
f.header.length <= 5 && f.data.length <= 255
%s::%s: failed to add top-level sequence\n
getFWSrcPath
mipc::MIPC_SIM_STATUS_PH_FSIM_PUK
Clear Bootstrap eSIM Preferences
%s::%s: failed to initialize LAI lib create function\n
%s::%s: Corrupt eUICC FW Data!\n
Failed StreamAPDU set %d/%zu, error %d status %hhu sw1 0x%x sw2 0x%x\n
Fail to run eUICC state machine: %d\n
Timeout waiting for confirmation on Switch Mode Req.\n
No Action
profile
Couldn't get response payload %s\n
setAuthPayload
AMAuthInstallApImg4CreateStitchTicket
%s::%s: failed to init debugArgs/logOptions\n
Deserialized plist data is not a dictionary firmwarePlist: 
apduSetCount
cardData.Valid()
Switch_Mode_Req sent: Msg=0x%x fTlv_Is_Reset_Req = %s\n
VinylPersoHost
Deserialized plist data is not a dictionary: %s\n
fwReaderCallback
INVALID_PARAM
VinylKTLEUICC::perform: KTLUTACopyReceiveData failed\n
an integer
ManagePairingAuthenticate Failed status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
Fatal Error: Error creating vinyl valve! Current State: %s\n
Auth_Perso_Cnf returned error[%s].\n
%s::%s: Count of certID != hashVad \n
kBBUReturnBootedForCoreDump
force
InstallTicket failed to get desired response\n
kBBUReturnFailedFinishProvisioning
kBBUReturnFusingSourceError
kVinylFwUpdateMainFwMac
%s::%s: Could not create VinylTransport\n
InRecoveryOS: %d\n
AuthenticatePersoDeviceRequest.bin
Failed to GetEuuidRequest status %d\n
StringRef.h
Main FW versions already matching (no forceMain)\n
ManagePairingGetNonce Sep_Cmd_Cnf fail\n
The format specifier for 
MAV radio %d eSIM lookup not supported!\n
kBBUReturnRPMImageError
Serialization error
accepted
 does not allow the 
Refurb optimization enabled, therefore blocking Refurb to Main FW update.
InstallPairingMSM succeed\n
VinylRestore::queryCmd ret.value(): 
Yes :-)
inDict
success
DR_Success == der_ret && TAG_EUICCDATAREQ == dec.tag
firmwareLoaderVersion
Finalize_Perso_Req sent: Msg=0x%x fTlv_Payload = %s\n
nonce
%s::%s: failed to get the Vinyl restore instance\n
successfully pushed Install Ticket\n
PostProcess
Bootstrap
Missing X-Apple-Alder-IP header in response, sticky session not active\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Communication/ICE/VinylICECommunication.cpp
ValidatePersoDevice %d\n
getFwMac
outData.Valid()
Failed to LpaSigningRequest status %d SW1_SW2 0x%x rsp_len %u\n
eUICCVinylMAVValve
returning VinylController::create\n
returning VinylController::updateFw\n
Delete Profile Cmd_Cnf not successful, result 0x%x\n
%s::%s: failed to extract bbfw item status %d\n
.
The type option contains an invalid value for a string formatting argument
decodeEuuidFromResponse: Invalid input parameters\n
%s::%s: ticket not present in the input\n
kBBUReturnGetSerialNumberFailure
queryCmd
mac : 
Error: failed to perform ResetSimCard\n
rb
%s::%s: create Main Fw failed\n
kBBUReturnGetFirmwareVersionFailed
kBBUReturnFailLoadImage
v28@?0i8^v12^v20
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Communication/Dale/VinylDaleCommunication.cpp
0x{:04x}
%s::%s: Cleaning up restore object\n
eUICCSepPairingBypassValue
Timeout waiting for mipc client start.\n
SIM status: %s(%d).\n
Client
%s::%s: failed to encode DER buffer\n
resultTo1stCommand.status == VinylError::kStatusSuccess
LETO-capable device detected! Attempt to enable eUICC.\n
%s::%s: mainIm4p not present in the input\n
kBBUReturnGetPkHashFailure
quitbootrom
/usr/standalone/firmware/Vinyl/
%s::%s: ldrVers count is zero\n
eUICC not enabled, aborted!\n
Timeout waiting for indications on Cmd Req store data.\n
kBBUReturnSuccess == ret && !dataBuffer.empty()
/update/main/firmware.der
Failed to complete AuthPerso command\n
%s::%s: VinylFirmware destructor called\n
Error: failed to SwitchCardMode\n
loader_version 0x%s key_id 0x%s perso %d\n
InstallTicket failed error %d status %hhu sw1 0x%x sw2 0x%x\n
Bailing on eUICC error due to status %u\n
eUICC not detected, skipping\n
chipID
NfRestoreDumpUART
getFileDataFromZip fullPath: 
eUICCVinylICEValve::InstallTicket InstallVad \n
alternate form
checkVinylPresence
kBBUReturnFailCreateTransportFirst
Status_Cnf received: Msg=0x%x fTlv_Eid = %s fTlv_Iccid = %s fTlv_Atr = %s\n
Delete All Profiles
getVersionString
operator=
current_fw_version %s main_fw_nonce 0x%s gold_fw_nonce 0x%s\n
ManagePairingGetNonce returning success\n
Timeout waiting for confirmation on Finalize Perso Req.\n
certIdentifier: 
basic_string
%s::%s: setFwInfo failed delete vinylFirmware object\n
fwMac : 
Firmware APDU not within expected bounds : received (header - 5 : %zu data- 255 : %zu\n
~~~~ MAX APDU PER SET: %zu  ~~~~\n
internalBuild         
kBBUReturnSuccess == ret
/info.plist
VinylPollResult
The replacement field misses a terminating '}'
%s::%s: Fw data dictionary not present in the input\n
pingCheck
kBBUReturnGetCarrierIDFailure
Timeout waiting for indication on ManagePairingGetNonce Sep_Cmd_Req\n
%s::%s: ACFURestore init failed\n
BasebandUpdater
bbupdater: %s
/update/gold/profile.bin
!GET_RSP_FIELD(rsp, result_t4)
NULL requestURL?\n
VinylForceGold
eUICC not stuffed but that's ok!\n
kBBUReturnAlreadyStarted
ManagePairingAuthenticate input nonce size = %zu, should be %d\n
plistFilePath : 
eUICCVinylICEValve::InstallTicket\n
ind.fTlv_Result && *ind.fTlv_Result == mipc::MIPC_DALE_VINYL_CMD_RESULT_SUCCESS
VinylUse4FF
verbosity
%s::%s: Failed getting FW MAC\n
End of input while parsing format specifier precision
The precision option does not contain a value or an argument index
kVinylPersoState
%s::%s: failed to alloc memory for deviceInfoDict\n
Failed to serialize dictionary %s error %s\n
NfRestoreSEOpenWithError
kBBUReturnFailedCreateController
Init_Perso_Req sent: Msg=0x%x fTlv_Payload = %s\n
kVinylFwUpdateGoldFwNonce
Yes
Failed to InstallPairingMSM status %d\n
BUSY
0B
%s::%s: Invalid certIdentifier in \n
MGCopyAnswer
kBBUReturnSysctlError
kBBUReturnResetToPBL
Router server stopping.\n
Failed to create propertylist from data, error: 
SIM Status Req attempt %d failed.\n
%@
Skipping free of external transport\n
ret %d records %zu\n
isLETOCapable: hwIdSimConfig[3]=%d, capable=%s\n
Failed to InstallPairingMSM status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
Invalid GetData, but allow Vinyl Update for coredump collection\n
fCommunication object not created, cannot free Transport\n
kBBUReturnMIImageError
fakefuse
(%s:%d) Range assignment too large(%p), got(%ld) max(%ld)
entering VinylController::updateFw\n
Client rsp data is not valid\n
kTOONIE
eUICC,Im4pMain
%s::%s: fullPath is null\n
VinylFirmware
startRouterServer()
Failed to DeleteProfile status %d SW1_SW2 0x%x\n
/firmware.der
kBBUReturnGetMEIDFailure
kBBUReturnFailedStartProvisioning
ind.fTlv_Nonce.get()->size() == SEP_NONCE_SZ
status
goldFirmware && mainFirmware && restoreOptions
VinylRestore-178~10448
DebugLogPath
%s::%s: Get FW Data from Zip failed\n
recoveryFwData : 
SwitchSimMuxCfgPolled: MUX settled to wrong config, current=%d expected=%d\n
!url.empty() && urlRef
kBBUReturnUMTSBand4CalibrationCheckFailure
ManagePairingGetNonce succeed\n
sizeof(resultTo1stCommand) == HDLCFrameGetPayloadLength(&rsp)
StoreData Command failed with sw %x\n
kHalley
Timeout waiting for confirmation on Auth Perso Req.\n
Store data Cmd_Ind not successful, result 0x%x\n
======================================\n
%u.%03u: %s: %u%s\n
performBootup
Failed to encode ECID\n
measurementSeq : 
%s::%s: failed to create im4p\n
localAccepter
getDebugInfo
SendReceiptServerResponse.plist
Failed to create dictionary\n
Digest
%s::%s: ldrVersStrArray count is zero\n
pingattempts
euim
Creating transport:%p \n
kBBUReturnProgrammerItemLoadingFailed
skipOperationOnSEPfail
%s::%s: Recovery Fw is not available\n
Failed to AuthPerso status %d SW1_SW2 0x%x rsp_len %u\n
GET_RSP_FIELD(rsp, cfg_req_t4) == IBI_NC_CFG_REQ_CONFIG_ID
kBBUReturnFailedSetNVItems
optionsDictOverride: 
%s::%s: Failed to alloc create fwFilePath CFString\n
%s::%s: VinylRestore: deconstructor\n
kVinylFwUpdateMainFwNonce
Failed to ManagePairingGetNonce status %d\n
createMainFw
kBBUReturnTelephonyUtilReadError
kBBUReturnAPTicketMallocFailed
Install_Fw_Req sent: Msg=0x%x fTlv_Payload = %s\n
VinylFirmwareReaderCallback
Assertion failure ( nullptr == fTransportCreated && \"Telephony transport error.\" )
euiccData.Valid()
failed to create eUICCSepPairingBypassValue\n
eUICCVinylDALValve::InstallTicket\n
VinylInstallSealingManifest
/mnt4
AuthenticatePersoDevice %d\n
assign
%s::%s: failed to peform get param update operation ret value = %d\n
kBBUReturnInternalError
Bootstrap Preferences
(snipped)
!(GET_RSP_FIELD(rsp, sim_error_cause_t28) & sim_error_cause_mask)
Integral value outside the range of the char type
error %d status 0x%hhx\n
kBBUReturnFatalError
!ind.isError()
%s::%s: setAuthPayload failed delete vinylFirmware object\n
ari
euiccCSN
KERN_SUCCESS == kr
Delete Profile Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Payload = %s\n
vinylgetFwData certPlusLdrVer just certIdentifier: 
kBBUReturnGetIMEIFailure
kBBUReturnELF32HeaderError
Getdata_Cnf not successful, result 0x%x 
!GET_RSP_FIELD(rsp, result_t3) && GET_RSP_FIELD(rsp, sim_rsp_len_t5)
RestoreOptions
v24@?0i8^v12I20
Error: only kTelephonyRadioVendorINT has IBIVinylSimCardResetReq, current RadioVendor = %d\n
transport %p, status: %d\n
...waiting patiently for reset\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Controller/VinylController.cpp
kBBUReturnBadEnvironment
kBBUReturnFailedSetSVN
kBBUReturnGetChipIDFailure
%s::%s: Failed to extract certIdentifier\n
No router server available.. bail out\n
All Preferences
handle_signals
Error: Invalid GetData response from BB\n
bundMac.size() == kFWMacSize
Update Main:Card %s Bundle %s\n
kBBUReturnPingFailed
%u.%03u: %s: %s
kMGQBasebandFirmwareUpdateInfo: 
v8@?0
SendReceipt
%s::%s: Unable to unzip the fwdata:\n
%s::%s: Invalid input Firmware.\n
%s::%s: fwMacData is wrong type\n
%s::%s: failed to create mainDict\n
Failed StreamAPDU set %d/%zu, status %d sw1_sw2 0x%x \n
%s::%s: missing mandatory euicc parameters for personalization\n
VinylFirmwareReaderInfoPlistCallback
%s::%s: failed to initialize object\n
Sep_Cmd_Ind Cmd_id %u should have fTlv_Nonce\n
recv
outPlist
Failed to InstallPairingMSM result %d SW1_SW2 0x%04x\n
kBBUReturnHashesMismatch
Dump: %s\n
%s::%s: failed to extract bbfw item fileData is NULL\n
GetWrapKeyServerResponse.plist
vinylgetFwData certPlusLdrVer: 
generateMeasurementDict
Invalid delete action: %d (expected 0 or 1)\n
VinylUpdaterExecCommand
decodeConfigIdFromResponse: Unexpected outer CHOICE tag 0x%02llx\n
failed to create mainDict\n
CreateValidationBlob DR %d\n
%s::%s: failed to create Vinyl CFRuntimeClass\n
kINVALID
Proxy Available!\n
fs == std::future_status::ready
InstallPairingMSM Sep_Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Msm = %s\n
cmdId == mipc::MIPC_DALE_VINYL_SEP_CMD_GET_NONCE || cmdId == mipc::MIPC_DALE_VINYL_SEP_CMD_AUTHENTICATE || cmdId == mipc::MIPC_DALE_VINYL_SEP_CMD_INSTALL
mipc::MIPC_SIM_STATUS_SEP_AUTH_STALLED
%s::%s: digestRef memory alloc failed\n
response->contents.cmd_rsp_token == resultTo1stCommand.cmd_rsp_token && response->contents.status == VinylError::kStatusSuccess
eUICCVinylMAVValve::ResetCard not supported\n
%s::%s: mainFwData not present in the input\n
kBBUReturnFailedSendingImage
InstallTicket result 0x%x sw1_sw2 0x%hx\n
eUICCeUICCStateMachine
goldNonce && goldDict
kBBUReturnFDRDataValidationFailed
VinylMainFirmwareCreate
%s::%s: No sources found \n
%s::%s: ldrVerComponents count is not expected\n
kBBUReturnFSMNoTransitionDefined
mipc::MIPC_SIM_STATUS_SIM_PIN2
eUICCSEPVerifyPairing     
~VinylRestore
Vinyl
VinylUpdaterCreate
com.apple.VinylCommunication
kBBUReturnARTMismatchedError
eUICC,FirmwareLoaderVersion
ACFUDebugArgs
BB reset successful\n
VinylKTLEUICC::perform: expected gmid %u, got response gmid %u\n
Creating with timeout set to %u ms\n
Assertion failure ( nullptr != fTransportCreated && \"Telephony Util transport error!\\n\" )
kBBUReturnFusingInstructionMissing
eUICC,Gold
NfRestoreSEClose
isR2MUpdate=%d, optimizeRefurbFirmwareUpdatePath=%d\n
kBBUReturnMultipleDevices
skip_fusing_validation
::
eUICCVinylData cache is valid. Using cached data!\n
decodeConfigIdFromResponse: Invalid input parameters\n
rsp.Valid()
simSKUID < ARR_SIZE(MAVHWSIMSKUStr)
Finalize_Perso_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s\n
ENTER: %s\n
Assertion failure ( pfnNfRestoreDumpUART != __null && \"Could not find pfnNfRestoreDumpUART symbol\\n\" )
Error: GetData() output not valid and isAbsentOK = false. kBBUReturnGetEIDFailure will be reported as kVinylResultDataMissing!\n
infnanINFNAN
VinylUpdaterSupported
Failed to register for proxy\n
In ManagePairingGetNonce...\n
%s::%s: entering: %s\n
Sending geteUUID request\n
kBBUReturnProvisioningUnknownSupportTypeError
kBBUReturnEBLImageError
EoS_Getdata_Req sent: Msg=0x%x fTlv_Is_Num_Of_Profile_Needed = %s\n
ManagePairingGetNonce Sep_Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s\n
BBUpdaterExecCommand rejected  with error\n
%s::%s: Initializing VinylRestore for preflight\n
kBBUReturnFusingError
FinalizePersoDeviceRequest.bin
0.1
kBBUReturnBadChecksum
=========== Vinyl eUICC Options ============\n
SystemRoot
!performOptions.alderHostname.empty()
failure
TelephonyRadiosGetRadioVendor %d not supported!
The config Id request was not made, but the response is not for it, instead it is %d\n
successfully streamed Firmware\n
ManagePairingAuthenticate Sep_Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Signed_Auth = %s fTlv_Nonce = %s\n
InitPersoDeviceResponse.bin
HardwareType
KERN_SUCCESS == kr && nvramInfo
An argument index may not have a negative value
failed to create firmwareLoaderVersion\n
StringRef
kBBUReturnNoMemory
kBBUReturnNAKManifest
kBBUReturnFailCreateTransportInitial
kBBUReturnProvisioningDataError
SIM status req failed even after several retries.\n
this->serverSessionID && CFStringGetLength( this->serverSessionID.get() ) != 0
VinylRestoreObj
Assertion failure ( ( ( stateMap.end() != def ) && def->second ) && \"eUICCStateMachine is corrupted.\" )
kBBUReturnTooManyRetry
VinylSkipProvisioning
VinylRestore
UpdateBaseband
response.hwSetRsp == MgrSetSIMHWSetResultType::kSuccess
Received payload length (%d) is smaller than required size (%d)\n
Using automatic argument numbering in manual argument numbering mode
Install_Vad_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s\n
configIdProvURL             
NULL
successCnf
/mnt4/wireless/Library/Logs/CrashReporter/Vinyl/Baseband/baseband_updater_logs/
%s::%s: failed to add VAD\n
status 0x%hhx cards_type: %hhu \n
Failed SteamAPDU index '%d' is greater than max array size '%zu'
ManagePairingAuthenticate Sep_Cmd_Cnf received: Msg=0x%x fTlv_Result = %s\n
ManagePairingAuthenticate Sep_Cmd_Cnf has no fTlv_Result\n
Delete All Non-Bootstrap Profiles
0x
Failed
Get data Valid(): %d isAbsentOk %d\n
twoPhasePresenceCheck 
getConfigId: Failed to decode ConfigId from response\n
%s\n
Update card version as it is overridden\n
failed to create certIdentifier\n
kBBUReturnNotSupported
/dev/null
VinylSkipAll
Invalid payload length %u (actual_size: %zu, max_dim: %zu)\n
The format specifier contains malformed Unicode characters
Sep_Cmd_Ind failed, result 0x%x\n
RestoreSystemPartition
ManagePairingAuthenticate Sep_Cmd_Ind Sep_Cmd_Cnf\n
VinylETLEUICC
sign
Running at state %s\n
%s::%s: failed to collect core dump\n
sepIndSuccess_
EoS_Getdata_Cnf not successful, result 0x%x 
VinylTwoPhaseRefurbRef
%s::%s: csn is datatype: %d, Length of CSN  %ld\n
Failed to correct response %d\n
SwitchSimMuxCfgPolled: request rejected, result=%s(%d)\n
kBBUReturnAborted
-f
%c%04zx  %s
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Support/BBUCommon.cpp
filename : 
eUICCVinylICEValve::InstallTicket InstallVad status %d\n
eUICC -- back to host to personalize in state %s\n
eUICC,InfoPlistDataGold
kBBUReturnDBLImageError
/usr/lib/libnfrestore.dylib
respDict
getFirmwareAPDUs
Failed to GetNcCfgRequest status %d\n
VinylUpdater
rsp->Valid() && rsp->contents.rsp_len
eUICC,BypassSEPPairing
%s::%s: failed to initialize update operations\n
Failed to create data\n
fwZipData: 
fwData : 
checkVinylFwLdrVerLegacy
 TelephonyBasebandPCITransportCreate returns: %s\n
kBBUReturnFailCreateTransportBooted
ind.fTlv_Nonce.get()
Assertion failure ( pfnNfRestoreOpenWithSE != __null && \"Could not find NfRestoreSEOpenWithError symbol\\n\" )
Failed to complete InitPerso command\n
getRecoveryFwData
BypassPairing
DR_Success == derRet
/
createTransport
@eUICC,Ticket
j <= req.apdu_payload.apdu_data_size
Failed to AuthenticatePersoDevice status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
geteUUID: StoreData failed with result %d, sw=0x%04x\n
Timeout waiting for confirmation on install fw req.\n
forcePerso            
BasebandFirmwareUpdateInfo
InitPersoServerRequest.plist
Failed to ManagePairingGetNonce result %d SW1_SW2 0x%x\n
ManagePairingAuthenticate succeed\n
eUICCVinylICEValve
default case\n
eUICC,ProfileDataMain
~VinylTransport
BootMode
Failed to InitPerso status %d SW1_SW2 0x%x rsp_len %u\n
sizeof(result) == HDLCFrameGetPayloadLength(&rsp)
kBBUReturnGetKeyStatusFailure
mipc::MIPC_SIM_STATUS_PH_CORP_PUK
EoS_Getdata_Cnf returned error[%s].\n
skipAll               
01
%s::%s: Vinyl update through generic updater is supported\n
status 0x%x sw1_sw2 0x%x eid 0x%s op_mode 0x%hhx\n
1.2.12
kBBUReturnFileNotFound
outPayload : 
isAbsentOkay result %d hardwareHasESIM: %d\n
a bool
The format specifier should consume the input or end with a '}'
 Initializing KTL options struct, opening ARI channel\n
SM::Recovery Missing gold with hash %s\n
infoSharedRef
kBBUReturnBBTicketDERParseErrorForCal
ret
kLETO
Switch_Mode_Req returned error[%s].\n
SwitchSimMuxCfgPolled: GetSimMuxCfg BUSY on poll %d/%d, MUX still switching\n
rsp.Valid() && rsp.contents.rsp_len
kLOONIE
DR_Success == der_ret
updateFw
%s
create
fwMacData: 
failed to create Vinyl CFRuntimeClass
geteUUID: Sending GetEuiccDataRequest\n
Invalid input parameter\n
kBBUReturnError
Auth_Perso_Req sent: Msg=0x%x fTlv_Payload = %s\n
/usr/lib/libMobileGestalt.dylib
Using manual argument numbering in automatic argument numbering mode
Need to free transport before creating again
%s::%s: mainInfoPlistData not present in the input\n
%s::%s: leaving: VinylRestore: %s\n
%s::%s: ACFURestorePartition key not present in updateroptions, defaulting it to empty string\n
GetSimMuxCfg: sim_cfg_req field not present in response\n
kBBUReturnTimedOut
kBBUReturnNotStarted
kBBUReturnFileMismatch
iargs
SimConfigRsp: device supports eSIM\n
BootedUpdate
%s::%s: basebandFirmwareUpdateInfoDict is valid %d, csn is valid: %d\n
%s::%s: context passed is null\n
SwitchSimMuxCfgPolled: GetSimMuxCfg failed on poll %d/%d\n
FAILURE
kVinylForceGenericUpdate NV set to TRUE\n
kBBUReturnELFImageError
Invalid GetData response from the BB\n
failed to get the Vinyl restore instance
Unpersonalized
failed to create goldFwMac\n
MobileGestalt returned NULL for SigningFuse
VinylTransport::getTicket  signedManifest: 
kBBUReturnGetICCIDFailure
kBBUReturnNVMImageError
SwitchSimMuxCfgPolled: timed out after %d polls\n
eUICCSEPPairingInstallMSM 
Sticky session: X-Apple-Alder-IP = %s\n
opening channel on provided external transport\n
kBBUReturnBadArgument
Timeout waiting for indication on InstallPairingMSM Sep_Cmd_Req\n
Status_Cnf returned error[%s].\n
Install_Fw_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s\n
Invalid Refurb Option %s
%s::%s: Failed to get a restore mount point to create FW object with\n
RemoteFSRoot
kBBUReturnRawBinaryImageError
Finalize_Perso_Req not successful, result 0x%x
%s::%s: failed to open bbfw archive for reading\n
ECID: 0x%llx\n
BBUCommon
Sep_Cmd_Ind Cmd_Id %u not supported\n
Delete Profile Cmd_Cnf received: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Result = %s\n
ignoremanifest
eUICCFwReaderStart
StartSession
%s::%s: Unable to allocate memory for fullPath:\n
!GET_RSP_FIELD(rsp, result_t3)
mipc::MIPC_SIM_STATUS_PH_NET_PIN
Validate_Perso_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s fTlv_Payload = %s\n
/update/main/profile.bin
Failed to allocate shared info dict\n
The format string contains an invalid escape sequence
mipc::MIPC_SIM_STATUS_PH_SIM_PIN
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Options/eUICCOptions.cpp
bbupdater
kBBUReturnFusingSECELFFailed
VinylForceMain
pfnNfRestoreOpenWithSE failure, outResult: %d\n
%s::%s: failed to find and/or copy data\n
Router server starting.\n
getConfigId: StoreData failed with result %d, sw=0x%04x\n
kBBUReturnTUTransportError
%s::%s: failed to open bbfw archive for reading eUICCFwReaderOpen\n
AMAuthInstallApImg4CreatePayload
kBBUReturnEOF
kBBUReturnTransferTerminated
EXIT:\n
UniqueChipID
eUICC,Main
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Communication/Eureka/VinylEURCommunication.cpp
eUICCVinylFactory
(kBBUReturnSuccess == ret) && (sw == 0x9000)
ValidatePersoDeviceRequest.bin
SendReceiptServerRequest.plist
Failed to ManagePairingAuthenticate status %d\n
chip_id 0x%x stream_apdu_max_apdus 0x%x isAbsentOk: %s\n
failed to create goldDict\n
Init_Perso_Cnf returned error[%s].\n
eUICCFwReaderClose
Failed to start router server due to timeout\n
VinylKTLEUICC::perform: KTLRawSendData failed\n
kBBUReturnAPTicketFileInitFailed
mipc::MIPC_SIM_STATUS_CARD_RESTRICTED
logging
:
%s::%s: VinylTransport::getBoardParameters not expected to be called\n
kBBUReturnSBLImageError
mipc::MIPC_SIM_STATUS_PH_CORP_PIN
InstallPairingMSM Sep_Cmd_Cnf has no fTlv_Result\n
VinylTwoPhaseUrl
com.apple.telephony.control-msg.xpc.allow
mipc::MIPC_SIM_STATUS_SEP_AUTH_FAILED
VinylGoldFirmwareCreate
SIM still initializing, trying again... sim_state 0x%x (retryCount: %d, retryLimit: %d)\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Update/StateMachine/eUICCStateMachine.cpp
kVinylSIMSKUID
kBBUReturnBBTicketDecodeError
request to free transport: %p\n
UNKNOWN
Proxy Aborted? %d\n
sw1_sw2 0x%hx\n
coreDumpPath
respDataPayload
 formatting argument
Gold version strings mismatched: Card %s Bundle %s\n
eUICCVinylDALValve
%s::%s: invalid params passed\n
fail to free transport: %p\n
kPSIM1_LOONIE
%s::%s: goldFwData not present in the input\n
mipc_client_started
Timeout waiting for confirmation on Get Data Req.\n
EoS_Getdata_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Is_Not_Personalized = %s fTlv_Sw = %s fTlv_Chip_Id = %s fTlv_Eid = %s\n
debugArgs             
Failed to FinalizePerso status %d SW1_SW2 0x%x\n
BBUICE16Communication
vinylFirmwareInfoDict: 
mipc::MIPC_SIM_STATUS_PH_FSIM_PIN
tafwLdrVerToFindg4cc : 
sending ConfigId Request
OPER_NOT_SUPPORTED
IBIVinylSimCardResetRspCb result 0x%x\n
Return 16 byte zero EID as pairing identifier\n
End of input while parsing an argument index
setNonce
kBBUReturnPowercycleAfterFusing
RestoreOSBuild
/update/main/info.plist
Sep_Cmd_Ind received: Msg=%04x fTlv_Cmd_Id = %s fTlv_Result = %s fTlv_Sw = %s fTlv_Nonce = %s\n
Success
Timeout waiting for confirmation on EoS Get Data Req.\n
Validate_Perso_Req sent: Msg=0x%x fTlv_Payload = %s\n
%s::%s: Failed to initialize restore object (%d)\n
Command
%s::%s: failed to compute digest\n
geteUUID: Failed to decode eUUID from response\n
eUICC
Fail to create transport: %d\n
kBBUReturnDSPImageError
/recovery/gold-
The numeric value of the format specifier is too large
The fill option contains an invalid value
deviceInfoDict passed is NULL:\n
kBBUReturnBinaryImageError
Switch_Mode_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s\n
Failed to complete ValidatePerso command\n
certIdToFind : 
Empty euuid data received\n
rsp->Valid()
eUICCVinylDALValve::ResetCard not supported\n
ManagePairingAuthenticate input nonce is empty\n
Sep_Cmd_Ind sepIndSem_ is NULL because of an unexpected baseband indication but that's fine\n
Not support for concatenated indications currently, segment 0x%x/0x%x\n
performCoreDump
~VinylFirmware
%s::%s: Get FW source path failed\n
fwLdrVerEqual
com.apple.router.abb
BBUCapabilities
Could not get master port %d\n
nvramRef
Replacement argument isn't a standard signed or unsigned integer type
failed to create mainFwMac\n
kPSIM1_PSIM2
InstallPairingMSM Sep_Cmd_Cnf failed, result 0x%x\n
VinylSkipOperationOnSEPFail
logmask
%s::%s: VinylUpdater Version: %s\n
VinylRestoreObjDestroy
kBBUReturnAllocationFailed
: 
Error: failed to get slot info from BB\n
ManagePairingAuthenticate Sep_Cmd_Cnf failed, result 0x%x\n
OptimizeRefurbFirmwareUpdatePath
vinylValve
ret = %d\n
EUICCChipID
PersoImpl
%s::%s: vinylgetFwData srcPath %s:\n
measurementDict: 
VinylTransport::updateGoldFw  signedManifest: 
VinylDebugArgs
SIM still initializing, trying again... IBIVinylResult 0x%x (retryCount: %d, retryLimit: %d)\n
Failed to get data from UIM\n
installTicket
%s::%s: mainProfileData not present in the input\n
kBBUReturnGetSessionKeyFailure
eUICCFwReaderOpen
NVRAM '%s' exists? %s\n
%s::%s: fwFileName %s\n
%s::%s: Vinyl update through generic updater is not supported, skip Vinyl update\n
Store data Cmd_Req returned error[%s].\n
%s::%s: VinylRestore object doesn't exist\n
eUICC,InfoPlistDataMain
ManagePairingAuthenticate input signed auth size = %zu, should < %d\n
router.server
result  0x%x \n
GetData status is not valid, hardware does not have eSIM, set absentOk to True\n
transport
eidSharedRef
decodeEuuidFromResponse: Successfully extracted eUUID\n
pushFirmware
%s::%s: VinylTransport destructor called\n
%s::%s: Create FwData copy failed\n
EID
Assertion failure ( nullptr != fTransportCreated && \"Telephony util transport error.\" )
!bundVersionString.empty() && !cardVersionString.empty()
kBBUReturnBBInitStatusTimeout
kBBUReturnGetCertIDFailure
Sep_Cmd_Ind returned error[%s].\n
ff_ping
a character
kLETO_3V
mipc::MIPC_SIM_STATUS_PH_NETSUB_PUK
\n
fwReaderInfoPlistCallback
fLink
@
Recovery
kBBUReturnNotPermitted
kPSIM1
Auth_Perso_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s fTlv_Payload = %s\n
%s::%s: failed to create measurementDict\n
No
kBBUReturnNotReady
kBBUReturnLoaderVersionError
kVinylFwUpdateLoaderVersion
check failed: %s, %d, assertion: %s\n
0123456789abcdefghijklmnopqrstuvwxyz
Sep_Cmd_Ind nonce size = %zu, should be %d\n
VinylOnlyPerso
%s::%s: AMSupportDigestSha256 failed:\n
%s::%s: ticket not present in the input\n
%s::%s: Invalid certIdentifier in \n
%s::%s: ACFURestore init failed\n
%s: (%s:%d) Range assignment too large(%p), got(%ld) max(%ld)
%s::%s: mainIm4p not present in the input\n
%s::%s: VinylTransport destructor called\n
%s::%s: certPlusLdrVer memory alloc failed\n
%s: (%s:%d) Array assignment too large(%p), got(%zu) max(%zu)
%s::%s: Get Profile Data from Zip failed\n
%s::%s: entering: %s\n
%s::%s: setFwInfo failed delete vinylFirmware object\n
%s::%s: fwFileName %s\n
%s::%s: Recovery Fw is not available\n
%s::%s: failed to compute digest\n
%s::%s: srcPath memory alloc failed\n
%s::%s: failed to create measurementDict\n
%s::%s: invalid params passed\n
%s::%s: Failed to build vinyl info.plist dictionary\n
%s::%s: Failed to alloc memory for vinyl dictionary\n
%s::%s: missing mandatory euicc parameters for personalization\n
%s::%s: Could not create VinylTransport\n
%s::%s: failed to add certId-VAD sequence\n
%s::%s: Vinyl update through generic updater is supported\n
%s::%s: Failed to initialize restore object (%d)\n
%s::%s: failed to open libauthinstall dylib\n
%s::%s: ldrVers count is zero\n
%s::%s: failed to init debugArgs/logOptions\n
%s::%s: No updater object passed, this is fatal\n
%s::%s: create Gold Fw failed\n
%s::%s: basebandFirmwareUpdateInfoDict is valid %d, csn is valid: %d\n
%s::%s: skipAll: %d updateBaseband %d vinylPresent %d\n
%s::%s: Invalid plistDict\n
%s::%s: failed to get the Vinyl restore instance\n
%s::%s: mainFwData not present in the input\n
%s::%s: failed to initialize update operations\n
%s::%s: failed to find bbfw item status %d\n
%s::%s: failed to extract bbfw item status %d\n
%s::%s: failed to initialize LAI lib create function\n
%s::%s: Invalid input Firmware\n
%s::%s: VinylRestore object doesn't exist, this is fatal\n
%s::%s: failed to alloc memory for deviceInfoDict\n
%s::%s: Initializing VinylRestore for preflight\n
%s::%s: Get FW Data from Zip failed\n
%s::%s: vinylgetFwData srcPath %s:\n
%s::%s: fullPath is null\n
%s::%s: failed to find and/or copy data\n
%s::%s: mainInfoPlistData not present in the input\n
%s::%s: failed to extract bbfw item fileData is NULL\n
%s::%s: Get FW source path failed\n
%s::%s: failed to get ldrVer\n
%s::%s: ldrVerComponents count is not expected\n
%s::%s: Corrupt eUICC FW Data!\n
%s::%s: failed to create Vinyl CFType object\n
%s::%s: VinylRestore object doesn't exist\n
%s::%s: VinylRestore: constructor\n
%s::%s: Failed to extract certIdentifier\n
%s::%s: Unable to allocate memory for fullPath:\n
%s::%s: failed to open bbfw archive for reading\n
%s::%s: Updater object created successfully\n
%s::%s: entering: VinylUpdater: %s\n
%s::%s: goldInfoPlistData not present in the input\n
%s::%s: Get InfoPlist Data from Zip failed\n
%s::%s: error getting properlylist\n
%s::%s: failed to add certId\n
%s::%s: failed to update FW, ret value = %d\n
%s::%s: empty implementation not expected to be called\n
%s::%s: Failed to alloc create fwFilePath CFString\n
%s::%s: failed to create im4p\n
%s::%s: failed to create dirURL\n
%s::%s: fwldrver is null\n
%s::%s: goldIm4p not present in the input\n
%s::%s: goldFwData not present in the input\n
%s::%s: ldrVersStrArray count is zero\n
%s::%s: digestRef memory alloc failed\n
%s::%s: leaving: %s due to failure\n
%s::%s: mainProfileData not present in the input\n
%s::%s: success value %d\n
%s::%s: Failed to alloc memory for main/gold entries\n
%s::%s: Count of certID != hashVad \n
%s::%s: Unable to unzip the fwdata:\n
%s::%s: Missing firmwareMac in info.plist -- firmware too old\n
%s::%s: Vinyl update through generic updater is not supported, skip Vinyl update\n
%s::%s: Fw data dictionary not present in the input\n
%s::%s: isPreflight: %d isNeRDOS() %d\n
%s::%s: failed to read zip file\n
%s::%s: No sources found \n
%s::%s: leaving: VinylUpdater: %s\n
%s::%s: Vinyl Update is complete!\n
%s::%s: failed to create vController object\n
%s::%s: Create FwData copy failed\n
%s::%s: Failed to alloc memory for filename\n
%s::%s: failed to init logging\n
%s::%s: Failed to get Vinyl Firmware Data\n
%s::%s: plistFileName %s\n
%s::%s: failed to add VAD\n
%s::%s: Cleaning up restore object\n
%s::%s: VinylRestore: deconstructor\n
%s::%s: entering: generateMeasurementDict\n
%s::%s: failed to initialize object\n
%s::%s: kMGQSigningFuse returned NULL\n
%s::%s: ACFURestorePartition key not present in updateroptions, defaulting it to empty string\n
%s::%s: failed to get byte ptr of fwldrver\n
%s::%s: leaving: VinylRestore: %s\n
%s::%s: basebandFirmwareUpdateInfoDict is NULL\n
%s::%s: diagnostics is not valid\n
%s::%s: %s\n%@
%s::%s: leaving: %s\n
%s::%s: Failed to alloc create plistFilePath CFString\n
%s::%s: fwSrcPath memory alloc failed\n
%s::%s: Invalid input Firmware.\n
%s::%s: failed to create Vinyl CFRuntimeClass\n
%s::%s: entering: VinylUpdater: %s command: %s\n
%s::%s: VinylTransport::getBoardParameters not expected to be called\n
%s::%s: performCmd failed\n
%s::%s: Could not create RTKitFirmware\n
%s::%s: csn is datatype: %d, Length of CSN  %ld\n
%s::%s: failed to open bbfw archive for reading eUICCFwReaderOpen\n
%s::%s: failed to encode DER buffer\n
%s::%s: Unable to copy the firmware:\n
%s::%s: fwMacData is wrong type\n
%s::%s: failed to peform get param update operation ret value = %d\n
%s::%s: failed to create fullURL\n
%s::%s: failed to create mainDict\n
%s::%s: create Main Fw failed\n
%s::%s: VinylUpdater Version: %s\n
%s::%s: setAuthPayload failed delete vinylFirmware object\n
%s::%s: VinylFirmware destructor called\n
%s::%s: failed stiching img4 and vad\n
%s::%s: failed to add top-level sequence\n
%s::%s: failed to create goldDict\n
%s::%s: context passed is null\n
%s::%s: failed to create restore object\n
%s::%s: Failed to get a restore mount point to create FW object with\n
%s::%s: Memory alloc failed certIds/VadDigest\n
%s::%s: failed to encode img4/vad sequence\n
%s::%s: Failed to execute command %d\n
%s::%s: failed to create Controller object\n
%s::%s: failed to collect core dump\n
%s::%s: unexpected debug log path type\n
%s::%s: Failed getting FW MAC\n
%s::%s: SM::Recovery -- normal? %d macMatchRequired %d\n
%s::%s: failed to create dirPath\n
```
