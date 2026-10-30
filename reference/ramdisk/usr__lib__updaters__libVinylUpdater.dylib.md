# `/usr/lib/updaters/libVinylUpdater.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 843,840 bytes.

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
%s::%s: failed to initialize object\n
%s::%s: mainIm4p not present in the input\n
%s::%s: failed to extract bbfw item status %d\n
%s::%s: setFwInfo failed delete vinylFirmware object\n
%s::%s: failed to get ldrVer\n
%s::%s: VinylRestore object doesn't exist\n
%s::%s: goldIm4p not present in the input\n
%s::%s: Invalid certIdentifier in \n
%s::%s: Corrupt eUICC FW Data!\n
%s::%s: failed to init logging\n
%s::%s: VinylUpdater Version: %s\n
%s::%s: entering: VinylUpdater: %s\n
%s::%s: Vinyl update through generic updater is supported\n
%s::%s: fwFileName %s\n
%s::%s: failed to read zip file\n
%s::%s: failed to add certId-VAD sequence\n
%s::%s: Missing firmwareMac in info.plist -- firmware too old\n
%s::%s: Vinyl Update is complete!\n
%s::%s: Failed to alloc memory for vinyl dictionary\n
%s::%s: Invalid input Firmware.\n
%s::%s: Invalid plistDict\n
%s::%s: VinylRestore: constructor\n
%s::%s: failed to open bbfw archive for reading eUICCFwReaderOpen\n
%s::%s: failed to add certId\n
%s::%s: entering: generateMeasurementDict\n
%s::%s: No updater object passed, this is fatal\n
%s::%s: Could not create VinylTransport\n
%s::%s: SM::Recovery -- normal? %d macMatchRequired %d\n
%s::%s: ldrVersStrArray count is zero\n
%s::%s: Failed to get Vinyl Firmware Data\n
%s::%s: Fw data dictionary not present in the input\n
%s::%s: fwSrcPath memory alloc failed\n
%s: (%s:%d) Range assignment too large(%p), got(%ld) max(%ld)
%s::%s: failed to get the Vinyl restore instance\n
%s::%s: Get FW Data from Zip failed\n
%s::%s: Failed to extract certIdentifier\n
%s::%s: ACFURestore init failed\n
%s::%s: failed to compute digest\n
%s::%s: VinylRestore object doesn't exist, this is fatal\n
%s::%s: entering: %s\n
%s::%s: failed to encode img4/vad sequence\n
%s::%s: failed to find and/or copy data\n
%s::%s: failed to create mainDict\n
%s::%s: mainProfileData not present in the input\n
%s::%s: Recovery Fw is not available\n
%s::%s: failed to add VAD\n
%s::%s: failed to encode DER buffer\n
%s::%s: digestRef memory alloc failed\n
%s::%s: goldFwData not present in the input\n
%s::%s: failed to create vController object\n
%s::%s: invalid params passed\n
%s::%s: Failed to alloc memory for filename\n
%s::%s: plistFileName %s\n
%s::%s: failed to add top-level sequence\n
%s: (%s:%d) Array assignment too large(%p), got(%zu) max(%zu)
%s::%s: basebandFirmwareUpdateInfoDict is NULL\n
%s::%s: Get FW source path failed\n
%s::%s: failed to collect core dump\n
%s::%s: isPreflight: %d isNeRDOS() %d\n
%s::%s: Vinyl update through generic updater is not supported, skip Vinyl update\n
%s::%s: failed to create fullURL\n
%s::%s: Unable to allocate memory for fullPath:\n
%s::%s: leaving: VinylUpdater: %s\n
%s::%s: diagnostics is not valid\n
%s::%s: failed to initialize update operations\n
%s::%s: Failed to alloc create plistFilePath CFString\n
%s::%s: ldrVers count is zero\n
%s::%s: Updater object created successfully\n
%s::%s: Could not create RTKitFirmware\n
%s::%s: Invalid input Firmware\n
%s::%s: VinylTransport::getBoardParameters not expected to be called\n
%s::%s: missing mandatory euicc parameters for personalization\n
%s::%s: failed to initialize LAI lib create function\n
%s::%s: failed to get byte ptr of fwldrver\n
%s::%s: fwMacData is wrong type\n
%s::%s: failed to create Vinyl CFRuntimeClass\n
%s::%s: VinylFirmware destructor called\n
%s::%s: failed to create Vinyl CFType object\n
%s::%s: Failed to execute command %d\n
%s::%s: mainFwData not present in the input\n
%s::%s: failed to alloc memory for deviceInfoDict\n
%s::%s: Get Profile Data from Zip failed\n
%s::%s: failed to create goldDict\n
%s::%s: entering: VinylUpdater: %s command: %s\n
%s::%s: %s\n%@
%s::%s: Failed to build vinyl info.plist dictionary\n
%s::%s: No sources found \n
%s::%s: failed to create dirPath\n
%s::%s: fwldrver is null\n
%s::%s: srcPath memory alloc failed\n
%s::%s: certPlusLdrVer memory alloc failed\n
%s::%s: failed to find bbfw item status %d\n
%s::%s: Unable to unzip the fwdata:\n
%s::%s: failed to create restore object\n
%s::%s: VinylTransport destructor called\n
%s::%s: Failed to alloc create fwFilePath CFString\n
%s::%s: Memory alloc failed certIds/VadDigest\n
%s::%s: fullPath is null\n
%s::%s: failed to create dirURL\n
%s::%s: Cleaning up restore object\n
%s::%s: ticket not present in the input\n
%s::%s: goldInfoPlistData not present in the input\n
%s::%s: leaving: %s due to failure\n
%s::%s: Failed to initialize restore object (%d)\n
%s::%s: leaving: %s\n
%s::%s: Failed to get a restore mount point to create FW object with\n
%s::%s: basebandFirmwareUpdateInfoDict is valid %d, csn is valid: %d\n
%s::%s: failed to create Controller object\n
%s::%s: failed to peform get param update operation ret value = %d\n
%s::%s: create Main Fw failed\n
%s::%s: kMGQSigningFuse returned NULL\n
%s::%s: Unable to copy the firmware:\n
%s::%s: failed to init debugArgs/logOptions\n
%s::%s: Failed to alloc memory for main/gold entries\n
%s::%s: failed to create im4p\n
%s::%s: failed to create measurementDict\n
%s::%s: mainInfoPlistData not present in the input\n
%s::%s: csn is datatype: %d, Length of CSN  %ld\n
%s::%s: performCmd failed\n
%s::%s: VinylRestore: deconstructor\n
%s::%s: Initializing VinylRestore for preflight\n
%s::%s: failed to open bbfw archive for reading\n
%s::%s: vinylgetFwData srcPath %s:\n
%s::%s: create Gold Fw failed\n
%s::%s: empty implementation not expected to be called\n
%s::%s: skipAll: %d updateBaseband %d vinylPresent %d\n
%s::%s: failed to extract bbfw item fileData is NULL\n
%s::%s: ldrVerComponents count is not expected\n
%s::%s: ACFURestorePartition key not present in updateroptions, defaulting it to empty string\n
%s::%s: Get InfoPlist Data from Zip failed\n
%s::%s: Failed getting FW MAC\n
%s::%s: Count of certID != hashVad \n
%s::%s: AMSupportDigestSha256 failed:\n
%s::%s: leaving: VinylRestore: %s\n
%s::%s: failed to open libauthinstall dylib\n
%s::%s: context passed is null\n
%s::%s: success value %d\n
%s::%s: unexpected debug log path type\n
%s::%s: Create FwData copy failed\n
%s::%s: failed to update FW, ret value = %d\n
%s::%s: error getting properlylist\n
%s::%s: failed stiching img4 and vad\n
%s::%s: setAuthPayload failed delete vinylFirmware object\n
ret %d records %zu\n
X-Apple-Alder-IP
%s::%s: fullPath is null\n
Failed to store data status %d SW1_SW2 0x%x\n
Invalid payload length %u (actual_size: %zu, max_dim: %zu)\n
VinylRestoreObjDestroy
Install main but no ticket -- back to restored please\n
failed to create euiccCSN\n
VinylRestore
MGCopyAnswer
/AppleInternal/Library/BuildRoots/4~CatVugAdRTUoFSQCa_wMfK3SZQyGVDT9VEArIh8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h
...waiting patiently for reset\n
deviceInfoDict passed is NULL:\n
kBBUReturnUMTSBand4CalibrationCheckFailure
Finalize_Perso_Req sent: Msg=0x%x fTlv_Payload = %s\n
Could not get master port %d\n
generateMeasurement
VinylETLEUICC
End of input while parsing format specifier precision
ret = %d\n
euiccData.Valid()
kBBUReturnFusingSECELFFailed
Install_Fw_Req sent: Msg=0x%x fTlv_Payload = %s\n
IODeviceTree:/options
SendReceiptServerRequest.plist
Getdata_Cnf not successful, result 0x%x 
Not support for concatenated indications currently, segment 0x%x/0x%x\n
Auth_Perso_Req not successful, result 0x%x
VinylSkipProvisioning
postProcess           
misc
kVinylFwUpdateCsn
Replacement argument isn't a standard signed or unsigned integer type
UpdateGold
kBBUReturnAPTicketReadContentFailed
BBUpdaterExecCommand rejected  with error\n
0B
Failed to handle Refurb operation, ret %d\n
checkVinylPresence
Timeout waiting for confirmation on Cmd Req Delete Profile.\n
Sep_Cmd_Ind doesn't have fTlv_Cmd_Id\n
Assertion failure ( lib != __null && \"Could not find /usr/lib/libnfrestore.dylib\" )
Failed to get PRP\n
getConfigIdBootstrapV2 not supported\n
EoS_Getdata_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Is_Not_Personalized = %s fTlv_Sw = %s fTlv_Chip_Id = %s fTlv_Eid = %s\n
kVinylFwPath: 
%s::%s: skipAll: %d updateBaseband %d vinylPresent %d\n
!performOptions.alderHostname.empty()
%s::%s: failed to create fullURL\n
/usr/standalone/firmware/Vinyl/
com.apple.telephony.control-msg.xpc.allow
Gold version strings mismatched: Card %s Bundle %s\n
kBBUReturnFailedCreateController
kBBUReturnFileError
Resetting modem: %s\n
fRouterServer
status
%s::%s: create Main Fw failed\n
Ticket provided is larger than spec. [ %ld (lenth) > %d (spec max) ] \n
InstallPairingMSM Sep_Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Msm = %s\n
ManagePairingGetNonce returning success\n
skipAll               
SendReceiptServer %d\n
%s%03d%s
RestoreOptions
UniqueChipID
vector
outPayload : 
0b
SIM Status Req attempt %d failed.\n
mipc::MIPC_SIM_STATUS_CARD_RESTRICTED
quitbootrom
eUICC,RootKeyIdentifier
bbupdater: %s
Integral value outside the range of the char type
Failed to register for proxy\n
optionsDictOverride: 
v28@?0i8^v12^v20
BBUCapabilities
~~~~ MAX APDU PER SET: %zu  ~~~~\n
eUICC Skip All\n
%u.%03u: %s: %s
The config Id request was not made, but the response is not for it, instead it is %d\n
%s::%s: failed to alloc memory for deviceInfoDict\n
AuthenticatePersoDeviceRequest.bin
isR2MUpdate=%d, optimizeRefurbFirmwareUpdatePath=%d\n
VinylCommunication::create
In ManagePairingAuthenticate...\n
ManagePairingGetNonce Sep_Cmd_Cnf failed, result 0x%x\n
BBULog
/mnt4
BBUpdaterSetOptions rejected  with error\n
InitPersoDeviceResponse.bin
%s::%s: setFwInfo failed delete vinylFirmware object\n
Using automatic argument numbering in manual argument numbering mode
j <= req.apdu_payload.apdu_data_size
failed to create goldDict\n
kBBUReturnFusingSourceError
Invalid GetData response from the BB\n
Error: failed to SwitchCardMode\n
%s::%s: fwldrver is null\n
%s::%s: Fw data dictionary not present in the input\n
kBBUReturnRetryError
kBBUReturnDBLImageError
ManagePairingGetNonce Sep_Cmd_Cnf has no fTlv_Result\n
VinylUse4FF
eUICCVinylData cache is valid. Using cached data!\n
getPathComponent
decodeEuuidFromResponse: Invalid input parameters\n
DR_Success == der_ret && TAG_EUUID == dec.tag && LENGTH_TAG_EUUID == dec.content.length
getConfigId: StoreData failed with result %d, sw=0x%04x\n
eUICCeUICCStateMachine
AMAuthInstallApImg4CreatePayload
an integer
StoreData Command failed\n
pushFirmware
Auth_Perso_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s fTlv_Payload = %s\n
%s::%s: failed to add certId\n
GetNonce
kVinylEID
Timeout waiting for indications on Cmd Req store data.\n
Timeout waiting for confirmation on install fw req.\n
mipc::MIPC_SIM_STATUS_SIM_PUK2
%s::%s: Failed to extract certIdentifier\n
%s::%s: failed to create measurementDict\n
%s::%s: entering: %s\n
queryCmd
ManagePairingAuthenticate input nonce size = %zu, should be %d\n
Assertion failure ( success && \"Unrecognized radio type.\" )
Failed to perform LPASigning Request status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
kBBUReturnNAKManifest
%s::%s: performCmd failed\n
InitPersoDevice %d\n
GetNonceServerResponse.plist
Failed to Pairing authenticate result %d SW1_SW2 0x%04x\n
this->reverseProxySettings
client rsp data: %s\n
eUICC
kBBUReturnPingFailed
sepIndSuccess_
Failed to complete FinalizePerso command\n
getConfigId: Failed to decode ConfigId from response\n
VinylForceGenericUpdate
false
infnanINFNAN
%s::%s: mainFwData not present in the input\n
Timeout waiting for confirmation on EoS Get Data Req.\n
VinylForceGold
%s::%s: No sources found \n
successfully switched back to Normal\n
Invalid input parameter\n
Error: invalid simSKUID = %u\n
Bootstrap Preferences
%s::%s: unexpected debug log path type\n
FirmwareLoaderVersion
mipc::MIPC_SIM_STATUS_PH_SIM_PIN
InitPersoServerRequest.plist
%s::%s: Failed to alloc memory for filename\n
measurementSeq : 
Assertion failure ( nullptr == fTransportCreated && \"Telephony transport error.\" )
GetData IBIVinylResult 0x%x\n
!GET_RSP_FIELD(rsp, result_t4)
eUICCVinylValve
rsp->Valid()
a bool
mainFirmware
%s::%s: mainInfoPlistData not present in the input\n
kBBUReturnEOF
kBBUReturnTelephonyUtilReadError
SE closed SUCCESSFULLY\n
Router server was not instantiated by VinylRestore to start it.\n
fCommunication
kPSIM1_HALLEY
No :-(
getFWSrcPath
Client rsp data is not valid\n
kBBUReturnARTMismatchedError
Init_Perso_Cnf returned error[%s].\n
Failed to InitPerso status %d SW1_SW2 0x%x rsp_len %u\n
failed to create mainDict\n
VinylTransport::getTicket  signedManifest: 
Command
00000000000000000000000000000000
mipc::MIPC_SIM_STATUS_EMPT_EUICC
Install_Fw_Cnf result 0x%x sw1_sw2 0x%hx\n
step
BootMode
kMGQBasebandFirmwareUpdateInfo: 
DebugLogPath
recoveryFwData : 
Dump: %s\n
/update/main/profile.bin
SwitchModeReq result 0x%x sw1_sw2 0x%hx\n
kVinylSIMSKUID
eUICC,ProfileDataGold
Getdata_Req sent: Msg=0x%x fTlv_Is_Num_Of_Profile_Needed = %s\n
Sep_Cmd_Ind Cmd_Id %u not supported\n
Getdata_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Is_Not_Personalized = %s fTlv_Sw = %s fTlv_Chip_Id = %s fTlv_Eid = %s\n
Router server eror: %s\n
getBoardParameters
VinylEURCommunication
Yes
kPSIM1_PSIM2
mipc::MIPC_SIM_STATUS_SIM_PUK
hl:C:v:x:t:r:p:e:c:w:i:s:fUFD:nHSqPV
%s::%s: failed to create Vinyl CFRuntimeClass\n
(%s:%d) Range assignment too large(%p), got(%ld) max(%ld)
failed to create firmwareLoaderVersion\n
eUICC,MainRecoveryFw
Install_Vad_Req returned error[%s].\n
profile
inRestoreOS: %d\n
Missing or empty server sssion?! %s\n
Failed to ManagePairingGetNonce result %d SW1_SW2 0x%x\n
createTransport
eUICC,ProfileDataMain
kBBUReturnProvisioningUnknownSupportTypeError
cmdId == mipc::MIPC_DALE_VINYL_SEP_CMD_GET_NONCE || cmdId == mipc::MIPC_DALE_VINYL_SEP_CMD_AUTHENTICATE || cmdId == mipc::MIPC_DALE_VINYL_SEP_CMD_INSTALL
======================================\n
Vinyl
ff_bootup
%s::%s: failed to encode img4/vad sequence\n
returning VinylController::updateFw\n
SIM status req failed even after several retries.\n
certIdentifier: 
Failed to encode ECID\n
BUSY
ret
ManagePairingAuthenticate succeed\n
kVinylForceGenericUpdate NV set to TRUE\n
EID: %s\n
/mnt3
LogDirectory
StartSession
isLETOCapable: hwIdSimConfig[3]=%d, capable=%s\n
%s::%s: create Gold Fw failed\n
kBBUReturnNeedsMoreInput
Finalize_Perso_Req not successful, result 0x%x
init
%s::%s: Could not create RTKitFirmware\n
Router server stopping.\n
VinylTwoPhasePresenceCheck
forceGold             
%s::%s: entering: VinylUpdater: %s\n
%s::%s: leaving: %s\n
0123456789abcdef
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Communication/ICE/VinylICECommunication.cpp
0.1
%s::%s: empty implementation not expected to be called\n
kBBUReturnError
RestoreOSBuild
com.apple.EmbeddedSoftwareRestore.eUICC.firmwareMac
getFwMac
InstallTicket failed to get desired response\n
OPER_NOT_SUPPORTED
InstallPairingMSM returning success\n
failed to create certIdentifier\n
kBBUReturnBadArgument
ECID: 0x%llx\n
kBBUReturnNotReady
EoS_Getdata_Cnf returned error[%s].\n
ff_create_transport
%s::%s: failed to open bbfw archive for reading eUICCFwReaderOpen\n
EUICCChipID
%s::%s: plistFileName %s\n
setAuthPayload
AMAuthInstallApImg4CreateStitchTicket
Failed to LpaSigningRequest status %d SW1_SW2 0x%x rsp_len %u\n
Return 16 byte zero EID as pairing identifier\n
failed to init logging
PersoImpl
No router server available.. bail out\n
eUICC,InfoPlistDataMain
kBBUReturnGetIMEIFailure
kBBUReturnGetICCIDFailure
kBBUReturnManifestStatusNonZeroError
sw1_sw2 0x%hx\n
-c
InRecoveryOS: %d\n
%s::%s: Failed to build vinyl info.plist dictionary\n
GetData status is not valid, hardware does not have eSIM, set absentOk to True\n
apduSetCount
kBBUReturnTimedOut
ManagePairingAuthenticate Sep_Cmd_Cnf failed, result 0x%x\n
%s::%s: VinylUpdater Version: %s\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Support/BBUCommon.cpp
Couldn't get response payload %s\n
Failed to correct result %d\n
transport
 option
Init_Perso_Req not successful, result 0x%x
=========== Vinyl eUICC Options ============\n
%s::%s: basebandFirmwareUpdateInfoDict is NULL\n
VinylSecureElement
plist_filename : 
Error: failed to perform ResetSimCard\n
StringRef
Deserialized plist data is not a dictionary firmwarePlist: 
kBBUReturnInitializerPrepError
kBBUReturnAPTicketMallocFailed
precision
SwitchCardMode: Baseband already in mode %hhu\n
Assertion failure ( ( ( stateMap.end() != def ) && def->second ) && \"eUICCStateMachine is corrupted.\" )
Timeout waiting for indication on ManagePairingGetNonce Sep_Cmd_Req\n
ManagePairingGetNonce Sep_Cmd_Cnf returned error[%s]\n
%s::%s: failed to create dirPath\n
 Initializing KTL options struct, opening ARI channel\n
%s::%s: failed to add VAD\n
.
%s::%s: fwMacData is wrong type\n
EID
GetSIMSKUID error %d status 0x%hhx\n
successfully pushed Install Ticket\n
Bailing on eUICC error due to status %u\n
kTOONIE
mipc::MIPC_SIM_STATUS_COMPLETE_READY
SigningFuse
VinylUpdaterIsDone
error %d status 0x%hhx\n
Failed to complete ValidatePerso command\n
Missing X-Apple-Alder-IP header in response, sticky session not active\n
Invalid external client link instance. \n
Failed to InitPerso status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
kLETO_3V
Status_Req sent: Msg=0x%x fTlv_Mode = %s\n
ff_first_stage
eUICC,EID
GetSimMuxCfg: failed, result=%s(%d)\n
sign
decodeConfigIdFromResponse: Unexpected outer CHOICE tag 0x%02llx\n
getConfigId: Sending ConfigurationRequest for configId\n
%s::%s: failed to update FW, ret value = %d\n
kBBUReturnUnPersonalizedImageError
Failed to assign output data\n
The format string contains an invalid escape sequence
alternate form
entering VinylController::create\n
Validate_Perso_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s fTlv_Payload = %s\n
rsp.Valid()
Failed to FinalizePersoDevice status %hhu SW1 0x%x SW2 0x%x\n
kBBUReturnBootedForCoreDump
Getdata_Cnf returned error[%s].\n
%s::%s: Unable to copy the firmware:\n
true
transport %p, status: %d\n
:
bundMac.size() == kFWMacSize
kBBUReturnBasebandUnresponsive
Unknown sim status
ari
Proxy Available!\n
kBBUReturnInternalError
Pairing Operation Not supported continue with Vinyl Operation
%s::%s: failed to peform get param update operation ret value = %d\n
twoPhaseUrl           
%s::%s: missing mandatory euicc parameters for personalization\n
%s::%s: Failed to alloc create plistFilePath CFString\n
Router server stopped.\n
Payload too large -- payload_size: %zu exceeds uint16_t maximum\n
%s::%s: goldFwData not present in the input\n
kBBUReturnBadManifestStatus
Sticky session: X-Apple-Alder-IP = %s\n
startRouterServer()
Invalid delete action: %d (expected 0 or 1)\n
The argument index should end with a ':' or a '}'
!url.empty() && urlRef
kBBUReturnFlashError
kBBUReturnFSMNoTransitionDefined
%s::%s: ldrVers count is zero\n
InstallTicket result 0x%x sw1_sw2 0x%hx\n
UNKNOWN
VinylKTLEUICC::perform: KTLUTACopyReceiveData failed\n
Status_Cnf received: Msg=0x%x fTlv_Eid = %s fTlv_Iccid = %s fTlv_Atr = %s\n
mipc::MIPC_SIM_STATUS_SEP_AUTH_UNPAIRED
The argument index starts with an invalid character
createTransport attempt %d/%d\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/CommandDrivers/eUICCVinylDALValve.cpp
Finalize perso failed with sw = %02X.\n
Validate_Perso_Req not successful, result 0x%x\n
CreateValidationBlob DR %d\n
 TelephonyBasebandPCITransportCreate returns: %s\n
Need to free transport before creating again
kVinylPersoState
BasebandUpdater
response
%02x
coreDumpPath
Empty euuid data received\n
VinylInstallSealingManifest
%s::%s: failed to add certId-VAD sequence\n
assign
eUICC not enabled, aborted!\n
mipc::MIPC_SIM_STATUS_PH_SP_PIN
%s::%s: Get Profile Data from Zip failed\n
com.apple.EmbeddedSoftwareRestore.eUICC.bootloaderVersionsSupported
Error: failed to get slot info from BB\n
entering VinylController::updateFw\n
com.apple.VinylStatuscallback
configIdProvURL             
Failed to ManagePairingGetNonce status %d\n
StringRef.h
kBBUReturnModemPowercycleError
Clear All eSIM Preferences
VinylDaleCommunication
sizeof(result) == HDLCFrameGetPayloadLength(&rsp)
VinylUpdaterExecCommand
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Controller/VinylController.cpp
sim_state 0x%x, sim_error_cause 0x%x\n
VinylGoldFirmwareCreate
failed to create Vinyl CFType object
/usr/lib/libnfrestore.dylib
response.hwSetRsp == MgrSetSIMHWSetResultType::kSuccess
Failed to allocate shared info dict\n
DR_Success == der_ret && TAG_EUICCDATAREQ == dec.tag
mipc::MIPC_SIM_STATUS_PH_CORP_PUK
%c%04zx  %s
eUICC,GoldRecoveryFw
VinylCommunication
Failed to create propertylist from data, error: 
AuthenticatePersoDeviceResponse.bin
getFileDataFromZip fwSrcPath: 
com.apple.router.abb
eUICCVinylMAVValve
Success!\n
%s::%s: Initializing VinylRestore for preflight\n
UpdateBaseband
%s::%s: failed to read zip file\n
Proxy Aborted? %d\n
gap 
SessionId
%s::%s: Failed getting FW MAC\n
INVALID_PARAM
a floating-point
error %d status %u sw1_sw2 0x%x\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Update/StateMachine/eUICCStateMachine.cpp
KERN_SUCCESS == kr
InitPersoServer %d\n
 formatting argument
main_fw_pcf_mac 0x%s gold_fw_pcf_mac 0x%s pcf_version 0x%x\n
kBBUReturnFileMismatch
kBBUReturnSuccess == ret
%s::%s: failed to open libauthinstall dylib\n
Sending geteUUID request\n
Delete Profile Cmd_Cnf received: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Result = %s\n
VinylMainFirmwareCreate
The value of the argument index exceeds its maximum value
kBBUReturnGetChipIDFailure
successCnf
/update/gold/profile.bin
The format string terminates at a '{'
failed to create Vinyl CFRuntimeClass
kBBUReturnGetPersonalizationInfoFailed
InstallPairingMSM succeed\n
-
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Communication/Eureka/VinylEURCommunication.cpp
decodeConfigIdFromResponse: Invalid input parameters\n
com.apple.VinylCommunicationMisc
Timeout waiting for mipc client start.\n
performCmd
kVinylFwUpdateKeyId
updateAllowed
decodeConfigIdFromResponse: Found auditResponseOk\n
Fail to run eUICC state machine: %d\n
VinylProvisioningURL
No Action
Options
%s::%s: ACFURestore init failed\n
bbupdater
CFGetTypeID(outPlist.get()) == CFDictionaryGetTypeID()
%s::%s: Unable to unzip the fwdata:\n
%s::%s: entering: generateMeasurementDict\n
The width option should not have a leading zero
Options:\n%s\n
Empty payload data received\n
Fatal Error: Error creating vinyl valve! Current State: %s\n
Main version strings mismatched: Card %s Bundle %s
%s::%s: VinylTransport destructor called\n
kBBUReturnNotSupported
alderHost             
%s::%s: leaving: VinylRestore: %s\n
eUICC,Gold
outData
loader_version 0x%s key_id 0x%s perso %d\n
BasebandFirmwareUpdateInfo
VinylKTLEUICC::perform: received NACK\n
0123456789abcdefghijklmnopqrstuvwxyz
%s::%s: failed to extract bbfw item fileData is NULL\n
VinylRestore Options:\n%s\n
Unhandled radio(%d) type or no radio\n
kBBUReturnFFSimError
%s::%s: failed to find and/or copy data\n
measurementDict: 
Running at state %s\n
kBBUReturnInvalidProgrammerItemType
Finalize_Perso_Cnf returned error[%s].\n
/mnt3/bbfs/
%s::%s: Invalid input Firmware.\n
kBBUReturnFailedSendingImage
kBBUReturnEBLImageError
Router server starting.\n
Failed StreamAPDU set %d/%zu, status %d sw1_sw2 0x%x \n
getPersoParameters
kBBUReturnMIImageError
%s::%s: fwFileName %s\n
vinylgetFwData certPlusLdrVer just certIdentifier: 
Router server was not instantiated by VinylRestore to stop it.\n
Switch_Mode_Req returned error[%s].\n
StreamFirmware failed\n
%s::%s: failed to init debugArgs/logOptions\n
Failed to AuthenticatePersoDevice status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
failed to create goldFwMac\n
kBBUReturnBadChecksum
Init_Perso_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s fTlv_Payload = %s\n
/dev/null
%u.%03u: %s: %u%s\n
SwitchSimMuxCfgPolled: perform failed\n
sizeof(resultTo1stCommand) == HDLCFrameGetPayloadLength(&rsp)
kBBUReturnELF32HeaderError
a character
Install gold but no ticket -- back to restored please\n
Timeout waiting for confirmation on Auth Perso Req.\n
EoS_Getdata_Cnf not successful, result 0x%x 
/update/gold/firmware.der
SwitchSimMuxCfgPolled: GetSimMuxCfg failed on poll %d/%d\n
default case\n
kBBUReturnFusingVerificationFailed
%s::%s: Updater object created successfully\n
VinylUpdaterSupported
decodeConfigIdFromResponse: Successfully extracted configID\n
(snipped)
Digest
%s::%s: failed to initialize LAI lib create function\n
kBBUReturnGetKeyStatusFailure
Timeout waiting for indication on ManagePairingAuthenticate Sep_Cmd_Req\n
pfnNfRestoreOpenWithSE failure, outResult: %d\n
tag4cc : 
vinylgetFwData certPlusLdrVer: 
%s::%s: context passed is null\n
goldFwMac
Sep_Cmd_Ind Cmd_id %u should have fTlv_Nonce\n
Failed to complete InitPerso command\n
plistFilePath : 
%s::%s: Failed to alloc memory for vinyl dictionary\n
getFirmwareAPDUs
invalid input params
DebugArgs
eUICCFwReaderOpen
array : 
decodeConfigIdFromResponse: Received error response with code %d\n
!bundVersionString.empty() && !cardVersionString.empty()
force
eUICCFwReaderClose
kBBUReturnIOError
skipOperationOnSEPfail
Client
kNonce
mipc::MIPC_SIM_STATUS_SEP_AUTH_STALLED
OptimizeRefurbFirmwareUpdatePath
%s::%s: Failed to alloc memory for main/gold entries\n
BBUCommon
%s::%s: Failed to alloc create fwFilePath CFString\n
chip_id 0x%x stream_apdu_max_apdus 0x%x isAbsentOk: %s\n
goldNonce && goldDict
internalBuild         
KERN_SUCCESS == kr && nvramInfo
Failed to InstallPairingMSM status %d\n
eUICC not stuffed but that's ok!\n
kBBUReturnProgrammerError
kBBUReturnFailCreateTransportBooted
mipc::MIPC_SIM_STATUS_SEP_AUTH_FAILED
%s::%s: certPlusLdrVer memory alloc failed\n
@
kBBUReturnGetMEIDFailure
verbosity
DR_Success == derRet
VinylFirmware
transport %p, status: %#x\n
VinylRestore object doesn't exist
fCommunication object not created, cannot free Transport\n
kBBUReturnResetToPBL
Serialization error
v24@?0{shared_ptr<ctu::Http::HttpResponse>=^{HttpResponse}^{__shared_weak_count}}8
/firmware.der
IBIVinylSimCardResetRspCb result 0x%x\n
GetSimMuxCfg: perform failed\n
Invalid Refurb Option %s
skip_fusing_validation
Only attach the the existing coredump dir to output dictionary without executing coredump again.\n
Failed to complete AuthPerso command\n
sim_state 0x%x sim_error_cause: 0x%x sim_ext_capabilities 0x%x isAbsentOk: %s\n
PostProcess
NULL requestURL?\n
kBBUReturnTooManyRetry
kBBUReturnGetSerialNumberFailure
kBBUReturnBBTicketMallocFailed
VinylSkipAll
v8@?0
kBBUReturnDSPImageError
kBBUReturnGetEIDFailure
Switch_Mode_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s\n
ManagePairingAuthenticate Sep_Cmd_Cnf has no fTlv_Result\n
ManagePairingAuthenticate has cached succeed result, no following indication\n
eUICCSEPVerifyPairing     
kBBUReturnGetCarrierIDFailure
kBBUReturnSWIDMismatchForHW
postresetdelay
GetWrapKeyServerResponse.plist
rb
accepted
Router server started.\n
(kBBUReturnSuccess == ret) && (sw == 0x9000)
Store data Cmd_Ind not successful, result 0x%x\n
Nonce
%s::%s: failed to extract bbfw item status %d\n
%s::%s: failed to create mainDict\n
!(GET_RSP_FIELD(rsp, sim_error_cause_t28) & sim_error_cause_mask)
kBBUReturnBBTicketDERParseErrorForCal
Timeout waiting for confirmation on install vad req.\n
HardwareType
kBBUReturnFailedSetNVItems
kBBUReturnMDMDDRImageError
getVersionString
failure
UpdateMain
Invalid GetData, but allow Vinyl Update for coredump collection\n
fCommunication object not created, cannot create Transport\n
v12@?0i8
setNonce
kBBUReturnFirmwareDataError
kBBUReturnSBLImageError
The format specifier for 
kBBUReturnFailedStartProvisioning
kBBUReturnFusingInstructionMissing
nonce
certIdToFind : 
%s::%s: failed to create im4p\n
VinylPollResult
01234567
%s::%s: Vinyl Update is complete!\n
deviceInfoDict
filename 
eUICCFwReader
%@
SendReceipt
FAILURE
kBBUReturnFailCreateTransportInitial
%s::%s: Unable to allocate memory for fullPath:\n
<VinylRestoreObj %p [%p]>{}
/mnt5
check failed: %s, %d, assertion: %s\n
NfRestoreDumpUART
kBBUReturnAllocationFailed
ind.fTlv_Nonce.get()->size() == SEP_NONCE_SZ
%s::%s: ldrVersStrArray count is zero\n
SM::Recovery Missing gold with hash %s\n
Main FW versions already matching (no forceMain)\n
chipID
Install_Fw_Req returned error[%s].\n
InstallPairingMSM Sep_Cmd_Cnf failed, result 0x%x\n
EXIT:\n
performCmd fOptions: 
NfRestoreSEOpenWithError
vinylValve
eidSharedRef
eUICC not detected, skipping\n
kBBUReturnFailedFinishProvisioning
In ManagePairingGetNonce...\n
mipc::MIPC_SIM_STATUS_SIM_PIN
create
Error: only kTelephonyRadioVendorINT has IBIVinylSimCardResetReq, current RadioVendor = %d\n
No
Failed to AuthPerso status %d SW1_SW2 0x%x rsp_len %u\n
mipc::MIPC_SIM_STATUS_PH_FSIM_PIN
mipc::MIPC_SIM_STATUS_PH_NET_PUK
VinylOnlyPerso
!!! 
VinylFirmwareCreate
%s::%s: failed to get byte ptr of fwldrver\n
Start
getDebugInfo
InstallPairingMSM Sep_Cmd_Cnf returned error[%s]\n
send
Failed SteamAPDU index '%d' is greater than max array size '%zu'
eUICC,InfoPlistDataGold
mipc::MIPC_SIM_STATUS_PH_FSIM_PUK
mipc::MIPC_SIM_STATUS_PH_NETSUB_PUK
mipc::MIPC_SIM_STATUS_CARD_REBOOT
router.server
installTicket
Delete Profile Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Payload = %s\n
InstallPairingMSM Sep_Cmd_Cnf fail\n
/recovery/gold-
options: 
/mnt4/wireless/Library/Logs/CrashReporter/Vinyl/Baseband/baseband_updater_logs/
%s::%s: failed to initialize object\n
xmissiontimeout
pingattempts
%s::%s: Recovery Fw is not available\n
0123456789ABCDEF
Payload too large -- payload_size: %d  max allowed: %lu)\n
kBBUReturnLoaderVersionError
Assertion failure ( pfnNfRestoreOpenWithSE != __null && \"Could not find NfRestoreSEOpenWithError symbol\\n\" )
mac : 
rsp.Valid() && rsp.contents.rsp_len
successfully streamed Firmware\n
ind.fTlv_Sw && *ind.fTlv_Sw == 0x9000
logmask
euig
VinylKTLEUICC::perform: response unpack failed\n
Finalize_Perso_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s\n
/usr/lib/libMobileGestalt.dylib
%s::%s: Get FW Data from Zip failed\n
tafwLdrVerToFindg4cc : 
getFileDataFromZip filePath: 
fail to free transport: %p\n
!GET_RSP_FIELD(rsp, result_t3)
0x{:02x}
0x{:04x}
NVRAM '%s' exists? %s\n
Creating transport:%p \n
GET_RSP_FIELD(rsp, sw1_sw2_t6) == 0x9000
eUICCVinylFactory
Assertion failure ( nullptr != fTransportCreated && \"Telephony util transport error.\" )
logLevel=%d
ManagePairingAuthenticate returning success\n
kBBUReturnBadEnvironment
TelephonyRadiosGetRadioVendor %d not supported!
result  0x%x \n
filename : 
SwitchSimMuxCfgPolled: timed out after %d polls\n
mainNonce && mainDict
FirmwareData
ManagePairingGetNonce Sep_Cmd_Ind fail\n
Install_Fw_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s\n
%s::%s: csn is datatype: %d, Length of CSN  %ld\n
Failed to create data\n
eUICC HW present is too old so we will skip updating it\n
kBBUReturnNAKHello
kBBUReturnFailedSetSVN
kBBUReturnAPTicketFileInitFailed
Sep_Cmd_Ind sepIndSem_ is NULL because of an unexpected baseband indication but that's fine\n
: 
kVinylFwUpdateLoaderVersion
isAbsentOkay result %d hardwareHasESIM: %d\n
this->serverSessionID && CFStringGetLength( this->serverSessionID.get() ) != 0
GetNonceServer %d\n
VinylRestore::queryCmd ret.value(): 
%s::%s: VinylRestore: constructor\n
successfully streamed recovery Firmware\n
%s::%s: mainProfileData not present in the input\n
/update/gold/info.plist
Failed to stop router server due to timeout\n
DR_Success == der_ret && TAG_CONFIGID_RESPONSE == dec.tag
InstallTicket failed error %d status %hhu sw1 0x%x sw2 0x%x\n
Failed
~VinylTransport
kBBUReturnManifestNoHashes
router.client.vinylrestore
SendReceiptServerResponse.plist
MAV radio %d eSIM lookup not supported!\n
kBBUReturnManifestImageError
Init_Perso_Req sent: Msg=0x%x fTlv_Payload = %s\n
mipc::MIPC_SIM_STATUS_PH_SP_PUK
ENTER: %s\n
SIM still initializing, trying again... sim_state 0x%x (retryCount: %d, retryLimit: %d)\n
kVinylRadioType
eUICC,Im4pMain
VinylTransport
Sep_Cmd_Ind received: Msg=%04x fTlv_Cmd_Id = %s fTlv_Result = %s fTlv_Sw = %s fTlv_Nonce = %s\n
Validate_Perso_Cnf returned error[%s].\n
VinylTwoPhaseRefurbRef
%s::%s: Get FW source path failed\n
checkVinylFwLdrVerLegacy
VinylKTLEUICC::perform: KTLRawSendData failed\n
goldFirmware
simSKUID < ARR_SIZE(MAVHWSIMSKUStr)
handle_signals
~VinylRestore
%s::%s: kMGQSigningFuse returned NULL\n
Condition <<%s>> failed %s %s/%d\n
%s::%s: SM::Recovery -- normal? %d macMatchRequired %d\n
SwitchSimMuxCfgPolled: MUX settled to wrong config, current=%d expected=%d\n
The replacement field misses a terminating '}'
DR_Success == der_ret
StoreData Command failed with sw %x\n
::
%s::%s: Corrupt eUICC FW Data!\n
eUICCVinylICEValve::InstallTicket\n
geteUUID: Sending GetEuiccDataRequest\n
%s::%s: failed to create vController object\n
kBBUReturnNVMImageError
kBBUReturnFailLoadImage
mipc_client_started
com.apple.VinylCommunication
kBBUReturnTUTransportError
Functionality not implemented.\n
Status_Cnf returned error[%s].\n
kHalley
Install_Vad_Req sent: Msg=0x%x fTlv_Payload = %s\n
NVRAM: %s\n
DR_Success == ret
Failed to serialize dictionary %s error %s\n
%s::%s: Memory alloc failed certIds/VadDigest\n
%s::%s: Invalid plistDict\n
SIM still initializing, trying again... IBIVinylResult 0x%x (retryCount: %d, retryLimit: %d)\n
Failed to correct SW during config Id fetch 0x%04x\n
operator=
kVinylFwUpdateMainFwNonce
/
zero-padding
kPSIM1
Delete Profile Cmd_Cnf not successful, result 0x%x\n
Store data Cmd_Ind received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s fTlv_Payload = %s\n
BBUpdaterExtremeCreateWithError rejected with error\n
getRecoveryFwData
%s::%s: AMSupportDigestSha256 failed:\n
%s::%s: entering: VinylUpdater: %s command: %s\n
1.2.12
Failed StreamAPDU set %d/%zu, error %d status %hhu sw1 0x%x sw2 0x%x\n
Timeout waiting for confirmation on Finalize Perso Req.\n
VinylTwoPhaseEidMask
%s::%s: failed to find bbfw item status %d\n
kDeviceIdentifier
outPlist
/usr/lib/libauthinstall.dylib
The type does not fit in the mask
%s::%s: Failed to execute command %d\n
eUICCVinylMAVValve::ResetCard not supported\n
eUICC,Im4pGold
performBootup
%s::%s: Failed to get a restore mount point to create FW object with\n
updateFw
nonce.size() == SEP_NONCE_SZ
respDict
fwReaderInfoPlistCallback
failed to create eUICCSepPairingBypassValue\n
kBBUReturnNoBBTicket
mipc::MIPC_SIM_STATUS_SIM_PIN2
InstallPairingMSM Sep_Cmd_Cnf has no fTlv_Result\n
debugArgs             
SwitchSimMuxCfgPolled: request rejected, result=%s(%d)\n
successfully reset the card\n
ManagePairingAuthenticate Sep_Cmd_Ind Sep_Cmd_Cnf\n
euim
stitchImg4Vad
Gold FW Macs already matching (no forceGold)\n
kBBUReturnAborted
kBBUReturnLibFDRDynLibNotLinked
geteUUIDBootstrapV2 not supported\n
Switch_Mode_Cnf not successful, result 0x%x sw1_sw2 0x%hx\n
persoStatic           
fwMacData: 
0x{:08x}
Deserialized plist data is not a dictionary: %s\n
resultTo1stCommand.status == VinylError::kStatusSuccess
The fill option contains an invalid value
BBUICE16Communication
kBBUReturnRawBinaryImageError
ValidatePersoDeviceRequest.bin
Get data Valid(): %d isAbsentOk %d\n
%s::%s: VinylTransport::getBoardParameters not expected to be called\n
kBBUReturnInitializeRingBufferError
ManagePairingGetNonce Sep_Cmd_Cnf fail\n
Ret %d from state %s next %s\n
certIdentifier
kBBUReturnInvalidTransportType
ff_ping
kVinylFwUpdateGoldFwMac
Empty implementation for PostProcess. Non updater takes care of refurb options!\n
kLETO
%s::%s: setAuthPayload failed delete vinylFirmware object\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Communication/Dale/VinylDaleCommunication.cpp
SimConfigRsp: device supports eSIM\n
%s::%s: failed to create Vinyl CFType object\n
eUICC -- back to host to personalize in state %s\n
kBBUReturnFusingError
kBBUReturnTransferTerminated
End of input while parsing an argument index
%s::%s: failed to init logging\n
decodeEuuidFromResponse: Successfully extracted eUUID\n
fs == std::future_status::ready
VinylVerifyPairing
%s::%s: Could not create VinylTransport\n
Assertion failure ( nullptr != fTransportCreated && \"Telephony Util transport error!\\n\" )
kBBUReturnFailCreateTransportSecond
Delete Profile Cmd_Req returned error[%s].\n
Install_Vad_Cnf received: Msg=0x%x fTlv_Result = %s fTlv_Sw = %s\n
module_verbosity
fwMac : 
%s::%s: Vinyl update through generic updater is supported\n
Resetting state machine: %s --> %s\n
Personalized
GetSimMuxCfg: transient BUSY, result=%s(%d)\n
eUICCVinylDALValve
ind.fTlv_Nonce.get()
Sep_Cmd_Ind nonce size = %zu, should be %d\n
logging
Could not load NVRAM? %d\n
0x
-f
VinylPairingAuthTest
%s::%s: No updater object passed, this is fatal\n
goldFirmware && mainFirmware && restoreOptions
kBBUReturnProtocolError
kBBUReturnGetBootupTimeError
Failed to GetEuuidRequest status %d\n
ManagePairingAuthenticate input nonce is empty\n
uimSlot               
Failed to deserialize dictionary %s error %s\n
Ticket provided is larger than spec. [ %lu (lenth) > %lu (spec max) ] \n
Cleaning up VinylController object \n
infoSharedRef
kBBUReturnProgrammerItemLoadingFailed
payload.size() <= MAX_MSM_SZ
InitPersoServerResponse.plist
Failed to FinalizePerso status %d SW1_SW2 0x%x\n
decodeConfigIdFromResponse: ConfigID not present in response (found tag=0x%02llx instead of configIDValue), exiting\n
kBBUReturnFailedNVSync
kBBUReturnBinaryImageError
Timeout waiting for confirmation on Get Data Req.\n
kBBUReturnSuccess == ret && !dataBuffer.empty()
eUICCFwReaderFindAndCopyFileData
%s::%s: failed to create goldDict\n
%s::%s: failed to collect core dump\n
kBBUReturnDownloadImageError
eUICCVinylDALValve::InstallTicket\n
Clear Bootstrap eSIM Preferences
VinylFirmwareReaderInfoPlistCallback
link accepted failed. t\n
StreamFirmware set %d/%zu adpusThisSet %zu\n
LETO-capable device detected! Attempt to enable eUICC.\n
%s::%s: leaving: VinylUpdater: %s\n
%s::%s: VinylRestore object doesn't exist, this is fatal\n
kBBUReturnSuccess
kBBUReturnNotStarted
returning VinylController::create\n
kBBUReturnNoMemory
kBBUReturnRPMImageError
BypassPairing
BB reset successful\n
Failed to start router server due to timeout\n
eUICCVinylICEValve
VinylKTLEUICC
All
eUICCSEPPairingInstallMSM 
%s::%s: basebandFirmwareUpdateInfoDict is valid %d, csn is valid: %d\n
fwReaderCallback
eUICCVinylICEValve::InstallTicket InstallVad \n
kBBUReturnSysctlError
VinylForceMain
Assertion failure ( pfnNfRestoreSEClose != __null && \"Could not find NfRestoreSEClose symbol\\n\" )
PRP timed out %d\n
kBBUReturnTryAgain
\n
onlyPerso             
iargs
%s::%s: success value %d\n
GetWrapKeyServer %d\n
generateMeasurementDict
SwitchSimMuxCfgPolled: MUX switch confirmed after %d poll(s)\n
response->contents.cmd_rsp_token == resultTo1stCommand.cmd_rsp_token && response->contents.status == VinylError::kStatusSuccess
Auth_Perso_Req sent: Msg=0x%x fTlv_Payload = %s\n
GetSimMuxCfg: sim_cfg_req field not present in response\n
locale-specific form
%s::%s: failed to create restore object\n
%s::%s: Failed to initialize restore object (%d)\n
Skipping free of external transport\n
Timeout waiting for confirmation on Switch Mode Req.\n
ind.fTlv_Result && *ind.fTlv_Result == mipc::MIPC_DALE_VINYL_CMD_RESULT_SUCCESS
SystemRoot
cardData.Valid()
refurbAction: %d\n
eUICC,ApProductionMode
Could not find NVRAM via IOKit\n
%s::%s: failed to create dirURL\n
ManagePairingGetNonce Sep_Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s\n
recv
2
vinylgetFwData fwSrcpath: 
%s\n
ACFUDebugArgs
Auth_Perso_Cnf returned error[%s].\n
0
eUICCVinylICEValve::InstallTicket InstallVad status %d\n
VinylController
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/SecureElement/VinylSecureElement.cpp
inDict
kLOONIE
reg
kBBUReturnTooManyReperso
Sep_Cmd_Ind failed, status word from UICC sw 0x%hx\n
forcePerso            
/update/main/firmware.der
eUICC enabled, mux switch success!\n
a pointer
ManagePairingGetNonce succeed\n
%s::%s: VinylRestore: deconstructor\n
%s::%s: failed to initialize update operations\n
setFwInfo
!GET_RSP_FIELD(rsp, result_t3) && GET_RSP_FIELD(rsp, sim_rsp_len_t5)
Failed to GetNcCfgRequest status %d\n
Store data Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Payload = %s\n
AMAuthInstallSupportCopyDataFromHexString
link.accepter.local
%s::%s: failed to compute digest\n
%s::%s: failed to get the Vinyl restore instance\n
kBBUReturnBBTicketReadContentFailed
Delete All Profiles
~VinylFirmware
opening channel on provided external transport\n
kBBUReturnInvalidBBUStageError
Failed to InstallPairingMSM result %d SW1_SW2 0x%04x\n
ret == kBBUReturnSuccess
ManagePairingGetNonce Failed status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
mipc::MIPC_SIM_STATUS_NOT_INSERT
%s
pargs
%s::%s: Invalid input Firmware\n
f.header.length <= 5 && f.data.length <= 255
The argument index is invalid
NULL
v24@?0i8^v12I20
%s::%s: vinylgetFwData srcPath %s:\n
VinylRestoreObj
%s::%s: failed to create Controller object\n
VinylTransport::updateGoldFw  signedManifest: 
kBBUReturnMultipleDevices
kBBUReturnGetManifestStatusFailed
RemoteFSRoot
%s::%s: srcPath memory alloc failed\n
%s::%s: digestRef memory alloc failed\n
GET_RSP_FIELD(rsp, cfg_req_t4) == IBI_NC_CFG_REQ_CONFIG_ID
Refurb optimization enabled, therefore blocking Refurb to Main FW update.
Timeout waiting for confirmation on Init Perso Req.\n
VinylTwoPhaseUrl
vinylPresent
%s::%s: ticket not present in the input\n
outData.Valid()
VinylRestore-178~10448
%s::%s: isPreflight: %d isNeRDOS() %d\n
NfRestoreSEClose
Creating with timeout set to %u ms\n
kBBUReturnGetPkHashFailure
Firmware APDU not within expected bounds : received (header - 5 : %zu data- 255 : %zu\n
eUICC,MainFwMac
nvramRef
call with %p different from fTransportCreated(%p)\n
The type option contains an invalid value for a string formatting argument
MobileGestalt returned NULL for SigningFuse
forceMain             
(snipped)\n
data : 
ManagePairingAuthenticate Failed status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
kINVALID
kPSIM1_TOONIE
kBBUReturnPowercycleAfterFusing
kBBUReturnProvisioningDataError
twoPhasePresenceCheck 
eUICC,FirmwareLoaderVersion
%s::%s: failed to get ldrVer\n
Result %d next state %s allowRetry %d\n
ManagePairingAuthenticate Sep_Cmd_Req sent: Msg=0x%x fTlv_Cmd_Id = %s fTlv_Signed_Auth = %s fTlv_Nonce = %s\n
ValidatePersoDevice %d\n
eUICC,ChipID
%s::%s: Missing firmwareMac in info.plist -- firmware too old\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/CommandDrivers/eUICCCommon.cpp
kPSIM1_LOONIE
kBBUReturnFDRDataValidationFailed
??????
createGoldFw
respDataPayload
%s::%s: error getting properlylist\n
sw == 0x9000
kBBUReturnGetCertIDFailure
Store data Cmd_Req returned error[%s].\n
Recovery
/update/main/info.plist
 does not allow the 
SwitchCardMode: Failed err %d status %hhu mode %d sw1 0x%x sw2 0x%x\n
Timeout waiting for confirmation on Status Req.\n
Using manual argument numbering in automatic argument numbering mode
Sep_Cmd_Ind failed, result 0x%x\n
fwFilePath : 
getFileDataFromZip
request to free transport: %p\n
GET_RSP_FIELD(rsp, result_t3) == IBI_NC_RESULT_SUCCESS
createMainFw
RestoreSystemPartition
InitPersoDeviceBlob.bin
success
mainFwMac
reset
GetNonceServerRequest.plist
FinalizePersoDeviceRequest.bin
%s::%s: leaving: %s due to failure\n
The argument index value is too large for the number of arguments supplied
The type option contains an invalid value for 
%s::%s: Cleaning up restore object\n
ManagePairingAuthenticate input signed auth size = %zu, should < %d\n
ManagePairingAuthenticate Sep_Cmd_Cnf received: Msg=0x%x fTlv_Result = %s\n
twoPhaseRefurbRef     
eUICC,Main
DATA
/info.plist
%s::%s: ldrVerComponents count is not expected\n
Error: GetData() output not valid and isAbsentOK = false. kBBUReturnGetEIDFailure will be reported as kVinylResultDataMissing!\n
%s::%s: Vinyl update through generic updater is not supported, skip Vinyl update\n
failed to create mainFwMac\n
kBBUReturnAlreadyStarted
eUICC,GoldFwMac
%s::%s: goldIm4p not present in the input\n
kBBUReturnServerError
kBBUReturnInvalidRadioType
In InstallPairingMSM...\n
%s::%s: VinylFirmware destructor called\n
Update Main:Card %s Bundle %s\n
Timeout waiting for indication on InstallPairingMSM Sep_Cmd_Req\n
VinylPersoHost
kBBUReturnBBInitStatusTimeout
kBBUReturnKeysNotAligned
fwLdrVerEqual
Failed to StoreData status %hhu SW1 0x%x SW2 0x%x\n
Failed to InstallPairingMSM status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
eUICCSepPairingBypassValue
ManagePairingAuthenticate Sep_Cmd_Cnf fail\n
The precision option does not contain a value or an argument index
VinylRestoreObjDescribe
Str && \"StringRef cannot be built from a NULL argument\"
%s::%s: mainIm4p not present in the input\n
pingCheck
kBBUReturnNotPermitted
kBBUReturnFileNotFound
%s::%s: ACFURestorePartition key not present in updateroptions, defaulting it to empty string\n
BBUpdater
Retry
Timeout waiting for confirmation on Validate Perso Req.\n
GetWrapKeyServerRequest.plist
SwitchSimMuxCfgPolled: GetSimMuxCfg BUSY on poll %d/%d, MUX still switching\n
eUICCFwReaderStart
VinylKTLEUICC::perform: expected gmid %u, got response gmid %u\n
eUICCVinylDALValve::ResetCard not supported\n
mipc::MIPC_SIM_STATUS_PH_NET_PIN
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/Options/eUICCOptions.cpp
@eUICC,Ticket
fwData : 
geteUUID: StoreData failed with result %d, sw=0x%04x\n
kVinylFwUpdateGoldFwNonce
(%s:%d) Array assignment too large(%p), got(%zu) max(%zu)
firmwareLoaderVersion
EoS_Getdata_Req sent: Msg=0x%x fTlv_Is_Num_Of_Profile_Needed = %s\n
AuthenticatePersoDevice %d\n
%s::%s: Failed to get Vinyl Firmware Data\n
fLink
Failed to get data from UIM\n
ManagePairingGetNonce result %d SW1_SW2 0x%04X length %d\n
sending ConfigId Request
Unpersonalized
SIM status: %s(%d).\n
getFileDataFromZip fullPath: 
Failed to DeleteProfile status %d SW1_SW2 0x%x\n
01
Perso
%s::%s: Invalid certIdentifier in \n
kBBUReturnHashesMismatch
ind.fTlv_Cmd_Id
performCoreDump
fwZipData: 
Fail to create transport: %d\n
InstallPairingMSM Sep_Cmd_Cnf received: Msg=0x%x fTlv_Result = %s\n
VinylRefurbOption
cardData.contents.perso
Error: Invalid GetData response from BB\n
Switch_Mode_Req sent: Msg=0x%x fTlv_Is_Reset_Req = %s\n
Yes :-)
createIm4p
Failed to correct response %d\n
The format specifier contains malformed Unicode characters
mipc::MIPC_SIM_STATUS_PH_CORP_PIN
ManagePairingGetNonce Sep_Cmd_Cnf received: Msg=0x%x fTlv_Result = %s\n
%s::%s: failed to open bbfw archive for reading\n
0X
failed to get the Vinyl restore instance
status 0x%hhx cards_type: %hhu \n
kVinylFirmware
Failed to create dictionary\n
%s::%s: fwSrcPath memory alloc failed\n
The format specifier should consume the input or end with a '}'
%s::%s: VinylRestore object doesn't exist\n
kBBUReturnFailCreateTransportFirst
 -- middle of buffer snipped -- \n
hwType.Valid()
VinylFirmwareReaderCallback
An argument index may not have a negative value
kBBUReturnGetSessionKeyFailure
InstallPairingMSM Sep_Cmd_Ind Fail\n
kVinylFwUpdateEuiccChipId
Received payload length (%d) is smaller than required size (%d)\n
VinylUpdaterCreate
VinylUpdater
twoPhaseEidMask       
xporttimeout
fRouterServerGood
Failed to ManagePairingAuthenticate status %d\n
Bootstrap
result %d code %d raw_error %ld error %s\n
kVinylFwUpdateMainFwMac
GetSimMuxCfg: current sim_cfg=%d\n
Success
kVinylSIMSKU
kBBUReturnProgrammerConnectionError
mipc::MIPC_SIM_STATUS_PH_NETSUB_PIN
eUICCSepPairingBypassValue 
gatherPreflightParameters
BootedUpdate
%s::%s: Create FwData copy failed\n
current_fw_version %s main_fw_nonce 0x%s gold_fw_nonce 0x%s\n
future.get()
kBBUReturnFatalError
kBBUReturnPingtimeout
VinylDebugArgs
returning deviceInfoDict: 
%s::%s: failed to encode DER buffer\n
digestRef: 
localAccepter
No transport available.. bail out\n
geteUUID: Failed to decode eUUID from response\n
euiccCSN
%s::%s: diagnostics is not valid\n
vinylFirmwareInfoDict: 
Validate_Perso_Req sent: Msg=0x%x fTlv_Payload = %s\n
Sep_Cmd_Ind returned error[%s].\n
All Preferences
%s::%s: failed stiching img4 and vad\n
rsp->Valid() && rsp->contents.rsp_len
Update card version as it is overridden\n
kBBUReturnGetFirmwareVersionFailed
payload.size() <= MAX_SEP_SIGNED_AUTH_SZ
ManagePairingAuthenticate Sep_Cmd_Cnf returned error[%s]\n
VinylSkipOperationOnSEPFail
%s::%s: Count of certID != hashVad \n
Error: failed to get SimConfig info from BB\n
/Library/Caches/com.apple.xbs/61B42420-66DE-47CB-99AF-3D4F54CE3CA1/TemporaryDirectory.AQiBIp/Sources/VinylRestore/CommandDrivers/eUICCVinylMAVValve.cpp
ignoremanifest
fakefuse
Assertion failure ( pfnNfRestoreDumpUART != __null && \"Could not find pfnNfRestoreDumpUART symbol\\n\" )
FinalizePersoDevice %d\n
%s::%s: invalid params passed\n
{:02x}
w
Core dump successful \n
%s::%s: failed to add top-level sequence\n
1.0
BBUPurpleReverseProxy
mipc::MIPC_SIM_STATUS_BUSY
Delete All Non-Bootstrap Profiles
Still persod after force?\n
%s::%s: Get InfoPlist Data from Zip failed\n
status 0x%x sw1_sw2 0x%x eid 0x%s op_mode 0x%hhx\n
rsp
eUICC,BypassSEPPairing
%s::%s: goldInfoPlistData not present in the input\n
kBBUReturnELFImageError
kBBUReturnMRCImageError
DataRoot
inData
kBBUReturnBBTicketDecodeError
kBBUReturnBBTicketDERParseErrorForFATPCal
!nonce.empty()
stall
setRecoveryFwInfo
The numeric value of the format specifier is too large
!ind.isError()
eUICC,Ticket
basic_string
GetWrapKey
```
