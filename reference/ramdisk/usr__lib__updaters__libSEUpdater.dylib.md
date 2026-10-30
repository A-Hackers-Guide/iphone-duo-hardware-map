# `/usr/lib/updaters/libSEUpdater.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,120,192 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 33 (Size: 4568)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (15)

- `/usr/lib/updaters/libSEUpdater.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/NearField.framework/NearField (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libTelephonyCapabilities.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libFDR.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libnfrestore.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libReverseProxyDevice.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (8 classes, 2 protocols)

Classes: `APDUUtil`, `AlohaPairingController`, `AlohaPairingVerifier`, `BAADelegateImpl`, `NSData`, `NSMutableData`, `NSString`, `SETransceiveHelper`

Protocols: `BAASupportDelegate`, `NSObject`

## Strings (1,594)

```
%s
AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n
isEntitledForBAA(): entitled = %u
(
tmpNum
DF30
Error encountered when parsing SCRTBlob %d\n
Failed to decode manifest
ignoreFPTear
splitDERSeq
EVENT LOGGING: Unable to recreate full file name with path\n
@SE2,Ticket
Bad status received when getting Auth Key V2 %d or nil for AuthKey %d\n
Submitting sePK to FDR: %d\n
DecodeSequenceContent returned %d
DERDecodeItem
!rApdu.isBad() && sizeof(SelectOSUResponse) == rApdu.size()
Failed to select CRS with ret %d SW: %x\n
AC Platform Primary %d Platform Secondary %d JCOP1 %d JCOP2 %d\n
Continue update with forceUpdateLoop=%lu \n
len <= MAX_APDU_LEN
info.tag == (ASN1_PRIVATE | ASN1_CONSTRUCTED | 0x3)
SELogObj
-[SETransceiveHelper copyCasdCert:]
no controller instance
Recovery script 0x%llx not found, terminating!
key
Submitting sePk data to FDR\n
payload.length <= 4294967295U
outData->data.resultSize <= (end - pos)
,
Successfully Configured OSU Reserve \n
(sizeof(CApduHeader_t)+len)<=MAX_APDU_LEN
keybagUUID
 for SEChipType 
KeyID %s is not localCA!
Failed to SLAMInstallPTCInstances due to %s, retrying...
setDebugOptions
sharingRequest
 fsn=0x
Davenport Delete
Proxy Available\n
ServerA9CertSN
Cannot parse forceUpdate counter: %s. Ignoring...\n
SCRT is nil\n
CFDataGetLength(nonce) <= sizeof(inData.data.nonce)
, 
Pairing selected: %d\n
sharingResult
Oasis version: %s\n
Cannot proceed in SC state
Successfully deleted SEAppletTool\n
Querying scrt with UniqueDeviceID: %@\n
Fail to parse MQR: wrong top level tag
IMPORT_REQUIRED
iPhone
Iron SLAM
Options
40D0_Enable_WithFilters_SW
Error when verifying session ID %@\n
ApEffectiveProductionMode
Ignoring NFC load stack error\n
crsSetSharingResult
IM4P_validated
entry.data && entry.length
Forced FPF with device BSN != firmware BSN
CertificateProductionStatus
wrong sessionID received %@, expected %@\n
doCommand
Pre-update SE Health check result: %s\n
Cleaning up unused applets\n
Skipping MP <%s> because we are up to date %d or would downgrade %d \n
-[SETransceiveHelper copySeid:]
a
APTicket
SN450 detected based on manifest query response\n
Update was going to proceed but bailing out due to forceDeviceHwVersion debug arg; don't want to brick SEs
ConfigureOSUReserves
shutdown
Skip configuring %s: JCOP version low (current csn: 0x%04X, min csn: 0x%04X)\n
Failed to parse 'sehv' value
Fail to NfRestoreSETransceive
At SLAMDeleteNeon
Bad SW 0x%x received in select %@\n
plist
image_no_reset
Failed to kill all slots with ret: %d and sw: %x\n
Not FW found in option
Skip LoadAndInstallSEAppletTool by SE chip type\n
SE,RapSwBinDsp
SCRT
Fail to parse MQR: cannot decode top level tag
sendIm4M
Legacy Oasis was found, removing it\n
Neon SLAM
Expected tag 0x%llx, got tag 0x%llx\n
-[AlohaPairingVerifier injectSEPKtoSSE_Debug:]
EXPORT_REQUIRED
BeeConnexions package not found (SW=0x%04X)\n
PID on SE %s, version on SE 0x%04llX\n
SE,IsDev
4107_GuardTimeout_30s
Failed to send Image4 trigger
MIFARE DESFire SLAM
SLAMMigrateSodium_1_0_12
deletePTCKeysWithNoStoredPK
While listing keys: %@\n
At SLAMDeleteCopernicusAndSunsprite
info.content.length == 4
Failed to send IM4 APDU
Failed to send manifest query
assertSW
PROD 
Warning: No ApTicket available to pass in fdrOptions
|
PASS
{ 
fSeHandle == nullptr
SN210V detected based on manifest query response\n
skipSeshatCheck
Deleting enablement PTA %s\n
encodeSequence
dataToSign && dataToSignLength
deactivated
doRestrictedMode
EVENT LOGGING: Unable to serialize data - %s\n
Error encountered when decoding top level 0x%llx\n
Setting loglevel to %d\n
makeUpdateController
ParseE3TLVs_block_invoke
0x
updateMeasurementDict
wrong updateTableEnry with wrong hash size
DeleteSEAppletTool
events
APC finished with return code %d\n
pos
GetAvailableMemory
Binaries: 
SN300V2 (Eos v2)
Unexpected returned length for hardware version query %zu != %zu\n
ignoreSecureChannelAM
KUD is set (0x%x), can proceed\n
operator()
retAttestation
confirmSigKey
DERDecodeSequenceContentWithBlock
Cannot parse DeliveryObject.binaries
Copernicus SLAM
Cannot found any matched delivery object
Unknown algorithm 
updateJCOPConfig
[cert length] <= (end - pos)
helsinki
Fail to switch to updaterOS
Invalid listKeys output %@\n
P73 detected based on manifest query response\n
skipAppletCleanup
-[AlohaPairingController verifyAndRetrieveServerSessionId:]
Mismatched signing keys device %s script %s
'
Verified result -- %@\n
Executing script <%s, %s>\n
Failed to dump rc %d sw 0x%x\n
Skipping Install Missing Instance <%s> by key\n
While performing recovery
assign
{
-[AlohaPairingController(FDR) submitPairingRecord:]
DebugLogPath
-- ----------------------- -- \n
 csn=0x
Fail to create dictionary for new manifest
Could not get Stinger config ID: SW=0x%X, size=%zu\n
execCommand
Internal Restore? %s\n
/usr/lib/libAppleSSEExt.dylib
Successfully FDR-injected SE Public Key into SSE for SEID %@\n
  Instance %s Module %s LC %s\n
FPF: forced %d, torn %d, requested %d, required %d, allowed %d\n
getForceUpdateLoop
fail to get Data
Cannot allocate for dict
SE2,Ticket
preflight
SN300V2 detected based on manifest query response\n
Update is done successfully: %s\n
%02X
Error encountered when selecting Star SD %@\n
-[SETransceiveHelper setAuthRandom:mac:error:]
At SLAMInstallPTCInstances
Error encountered when building begin pair dictionary: %@\n
\tsubcounter    = %llu\n
Cannot parse UpdateTable.bsn.
Found BeeConnexions Unified with Load File Version: 0x%04X (expected: 0x%04X)\n
isHardwareiPhone: MGCopyAnswer returned nullptr for DeviceClass, defaulting to iPhone\n
DF21
Bad SW encountered when getting OBKG 0x%x\n
-[AlohaPairingController dealloc]
PreflightContext
While querying SLAM state
Failed to parse updateProperties as per UpdatePropertiesItemSpec.
Successfully set FTA Activation Status to %d\n
SLAMConfigureOSUReserves
production
No personalisable SEs found\n
Error encountered when transceiving copyCasdCert\n
4217_I2CB_FrameLog_Enable_Default
factory_postflight
deleteUnusedApplets
  SEID: %@\n
inData
nonce
Unexpected length for CPLC data %zu
chipID 0x%X isProd %d expectedBSN 0x%X (has_value %d) deliveryBSN 0x%X isPORUpdate %d\n
%s() -> %d
Pushed Manifest successfully\n
Failed to set AR %d 0x%hx\n
with name %s, pkHash %s, platformCategory %d
Fail to allocate tmpData
No factory postflight in the update bundle
Failed to run script %s. %s
Missing SE,ChipID in request dictionary
context
Passing fdrOptions %@
sizeof(CApduHeader_t) >= bytes->size()
CASDCert
SLAM SEFW version 0 is deprecated.
IndexTableCompaction_415E
Encountered error when talking to server %@\n
libDERErrorDomain
Selecting SE with ID: %d \n
Start processing command: %s\n
Unrecognized command %s
getAlohaVerificationOptions
StripImg4
getDataFromDict
-[SETransceiveHelper getSEPK:andSEID:deleteExisting:error:]
Failed to verify the configuration update of 
VERBOSE
Will dump SE to file --> %s\n
Checking for legacy Muirfield to cleanup\n
CFNumberGetValue(tmpNum, kCFNumberSInt32Type, (void*)&tmpValue)
Error encountered when transceiving copy SE Signature \n
PTC Instance %s in LC state 0x%X\n
Adding header %@ = %@\n
Wrong length for updateTableEnry
~P73BaseSEController
At SLAMLoadAndInstallSEAppletTool_0_0_2
SLAMDeletePioneer
SE,RootKeyIdentifier
caught signal %d\n
BAASupport
ExecuteScriptWithResult
  restoreEnvironment: %d\n
updateSize
0
Received incomplete E3 TLV from GetStatusApplications
PTA Package AID on device is %s, skipping delete operation\n
SLAMOasisConfig_10270000050000000000000000000000
While querying migration state
Failed to decode ret %d tag 0x%llx exoected 0x%llx
  requestSig %@\n
Missing element in updateTableEnry
DeactivateAll for %s ret %d SW 0x%hx\n
At SLAMLoadAndInstallLogger
Oasis applet not found: SW=0x%X\n
Bad SW received when copying device type 0x%x\n
SSEGetEntangledAuthorizationRandom
Install SEAppletTool: %s\n
Successfully deleted terminated PTC\n
DeleteEnablementPTA
Successfully deleted enablement PTA\n
service
GetCombined
At SLAMDeleteSEAppletTool
SLAMLoadAndInstallStinger
SLAMLoadAndInstallHelium_v1021_ESE18
SEAC
Skip configuring %s: JCOP platform not supported\n
I2CA_GuardTimeout_40C9
vector
Failed to SELECT Seshat 0x%x?\n
Fail to create dictionary for request
Argon Load and install SLAM
Error encountered when building auth resp dictionary: %@\n
-[AlohaPairingController processAuthReqPayload:outError:]
found SE with ID: %d \n
not 
40D0_Disable
forceUpdate
SLAMLoadAndInstallArgon_2_1_4_0B
DevelopmentUpdatePayloadHash
CFNumberGetValue(tmp, kCFNumberSInt32Type, (void *)&chipID)
/Library/Caches/com.apple.xbs/FF83E7CC-A422-4417-A8D5-3AD7BBA47DD6/TemporaryDirectory.b4kgjH/Sources/AppleSSE/AppleSSElib/AppleSSElib.m
size of factoryPostflightState or cometRootKeyId doesn't match
Bad length for platform primary attack log indicator\n
Neon Package AID on device is %s, skipping delete operation\n
SLAMDESFireMigration_1_0_23
SLAMMigrateCopernicus_2_5_4
Bad SW 0x%x received\n
mac
MQ: %s\n
Starting BeeConnexions update sequence\n
Installing Stinger applet\n
failed to CFDataCreate for manifest data
SE <<<< %@\n
FactoryRFTest
v8@?0
Hardware version %u\n
Successfully loaded and installed Sunsprite Logger\n
Could not get Oasis config ID: SW=0x%X, size=%zu\n
Failed to select the ISD
Select PT: SW1 0x%x SW2 0x%x SW3 0x%x\n
SIMDetectGPIO_4143
ctx
setSigKey
Cannot proceed in OSU state
SLAMStingerConfig_qa_5F7E35F9D391B1367F75823E36496533
Sodium SLAM
getAlohaPairingOptions
Unknown personalizable SE %d\n
Skip DeleteSEAppletTool by SE chip type\n
Configuring Oasis applet\n
SLAMLuauMigration_1_2_0_5
v32@?0@\"NFSecureElement\"8Q16^B24
-[SETransceiveHelper dealloc]
Bad status received when sharing auth key %d or nil for sharing result %d or nil for sharing result signature %d\n
Wrong type for kRoseTagDigest
SLAMLoadAndInstallLogger_1_0_0
performFactoryConfiguration
Bad HTTP Status Code received %ld\n
payload == &((*bytes)[sizeof(CApduHeader_t)])
Aborting due to DO BSN 0x%X <= 0x01AD or device RSN 0x%X < 0x0192\n
SLAMDeleteOasis
-[AlohaPairingVerifier performAuthKeySharingWithAppleSSE:sharingRequest:requestSignature:resultSignature:withError:]
retKeyData
generateSigKey
PlatformBitmap absent for a script with name %s
\n
Luau SLAM
Dumping AM Info\n
%s\n
WriteEvent
FirmwareData
Details: 
Failed to perform pre-update health check Caught exception %s\n
Failed to get SEPK+SEID: %@
Exception! what: %s
Legacy (plist) SLAM SEFW path is no longer supported
 Device info: 
DeactivateAll for %s failed to SELECT CRS %d SW 0x%hx\n
SE,Ticket
Could not parse memory constraints within SEFW
Failed again to SLAMInstallPTCInstances due to %s, terminating.
Apdu
Failed to select ISD %d SW: %x\n
Running trigger %s script 0x%s\n
  --> wouldDowngrade %d\n
@SE,Ticket
Error encountered when transceiving copy SEID \n
EVENT LOGGING: Invalid options parameter\n
Failed to select %@\n
Bad SW from SELECT: 
Failed to set MFDAll SW: %x\n
fDeliveryObj
Failed to configure Oasis\n
Skipping MP <%s> by key\n
Unexpected top level tag 0x%X expected 0x%X\n
AlohaPairingController deallocating\n
  sePk: %@\n
Error encountered when getting cert SN %@\n
ApEffectiveSecurityMode
AlohaV2Pairing-
description
sendApduFile
Setting debugArgs (empty): %s\n
getSigKeyExpDate
-[AlohaPairingVerifier invalidate]
level >= 0 && level < _LOG_LEVEL_MAX && \"level is not good\"
4216_I2CA_FrameLog_Disable
Called SSGetAttV2AuthKey with nonce (hsmChallengeSEP) : %@
Debug argument forceDeviceHwVersion empty
Missing SE,RootKeyIdentifier in request dictionary
Error encountered when performing HTTP request %@, got reply %@, with error %@\n
SN300V3 (Eos v3)
Failed to sign: %d
Proxy Unavailable\n
ERR
Failed to parse as per PropertyItemSpec
skipReperso
At installation trigger %s script %s\n
PTC key in slot %d to be deleted %d\n
Apdu.hpp
sendIm4P
No updater context hint, defaulting to limited environment\n
pubKey
_CFDictionarySetInteger32
version
BeginPair
AC Platform Primary %d Platform Secondary %d\n
SLAMMigrateHaishan_1_2_07
Successfully set AR\n
ApChipId
WARNING
Stinger Config ID: %s\n
StockholmPairingProtocolVersion
SESignature
Failed to transceive %@\n
AppleSSE
For Trigger %s missing instance AID %s\n
Bad SW 0x%x received in copy SE Signature\n
SSEGetAuthorizationRandom %d
CFDataGetLength(sePk) <= 4294967295U
\tauthRand hash = %016llx\n
Fail to Img4EncodeItemBegin: %d
deactivateAll
Failed to register for proxy\n
-[AlohaPairingVerifier getSharingRequestWithSignature:withError:]
Bad SW from GET_STATUS: 
getDataSize
4216_I2CA_FrameLog_Enable_Debug
No update item with index: 
IsBootedOS
\tentropy hash  = %016llx\n
_CFDictionarySetData
~P73BaseUpdateController
Successfully ran trigger %s\n
) 
Was expecting XML format but received %lu\n
%s : 0x%x
end
40C9_GuardTimeout_30s
SE OS not in idle state
SLAMLoadAndInstallReaderSIOPackage
-- JCOP Train too low to GET DATA AVAILABLE MEMORY -- \n
SE in restricted mode
Bad length for secondary attack log indicator\n
Haishan SLAM
SEUpdaterExecCommand
retSharingResultSignature
Verify options:\n
Seshat get data response is 0x%zx bytes, expected 0x%lx or 0x%lx
Dumping OSU\n
outData
Cannot parse ImageBinary.index.
Unknown chipID in BLOB
ChipID
capdu
com.apple.private.applesse.allow
GetChipId
Fail to parse MQR.data
This process may take a long time (~16 min)\n
SE,Nonce
CertificateSecurityMode
Payload dictionary is wrong %@\n
/var/mobile/Library/Logs/AppleSSE.log
nfcd
40BD_DisableInFPM_DisableLogging
 (OSU Key ID: 0x
SN100V detected based on manifest query response\n
No Neon Package loaded on device, skipping delete operation\n
Checking for Bee Connexions and Executable Load File Version Number\n
Failed to parse key data %d %@\n
retSharingResult
/System/Library/Frameworks/Security.framework/Security
 failed for '
%2.2x
_createDataSignature
Unable to get AM Digest with error code %d\n
getOasisVersionAndConfig
SLAMMigrateNeon_YK300R107
SE,OsKeysIdentifier
Perform configuring %s with option %s successfully\n
fail to register kLibSEUpdaterClass
haltOnCrash
Fail to create data for SEDH in request
EVENT LOGGING: Could not recreate log events properties from file - Defaulting to empty file\n
requestDict
rapdu
POST
%s
Returning outError:\n
->pls attach debugger\n
num != nullptr
This update would brick the SE due to rdar://problem/90407147
%s/%d : %s
Error from AMFDRSealingMapCopyLocalData: %@
IM4P_Resent
}: 
KeyID 0x%X, overwriting with dev %d
CleanUpTerminatedPTC
Couldn't get sharedHardwareManager
Bad transceive with return code %d\n
com.apple.private.applesse.baa
-- GET DATA AVAILABLE MEMORY -- \n
Failed to validate delivery object
Skipping cleanup script <%s, %s> because hardware is iPhone\n
SLAMMigrateKrypton_3_3_2_0E
BoardId
Project version%s: %s\n
EVENT LOGGING: debugLogPath not present\n
outdata && outlength
runFactoryPostflight
0x%2.2x 
Are we in booted OS? %d\n
Additional actions: FTA will be %s, MFD will %sbe performed\n
UNK_IM4_STATE
Forcing local signing\n
SLAMStingerConfig_prod_505C2526532CCF2049A2E3BDB6FD2867
SLAMDeleteXenon
keyData
< %s
4216_I2CA_FrameLog_Enable_Default
Failed to read response\n
While selecting ISD
Legacy BeeConnexion was found, removing it\n
mmap()
SetP2
%04x: 
simDetectHIZ
-[AlohaPairingVerifier injectSEPKtoSSE_FDR:]
40BD_EnableInFPM_DisableLogging
NO
EffectiveSecurityModeSEP
Created updater %p\n
] 
At least one slot enrolled & no KUD\n
SLAMDeleteStinger
SLAMDeleteBeeLegacy
A0000001515350414141504C
Bad SW encountered when getting cert SN 0x%x\n
/usr/lib/libMobileGestalt.dylib
While getting ChipId for platform category
412A_Default
Loop %u of 31\n
Skip Oasis install: JCOP version low.\n
Stinger applet not found: SW=0x%X\n
type return to continue
Stinger version 0x%04X is lower than expected 0x%04X\n
handle
open()
attV2AuthKey
Transceive
Unknown RootCAId: 
EXPORT_FINISHED
BeeConnexions update required: %s\n
AlohaPairingController invalidating\n
-[AlohaPairingController performHTTPRequestWithRequestDict:outError:]_block_invoke
retPubKey
Failed to add sers
outError && outMeasurementDict
printManifest
development
WriteCommand
Failed to read CPLC data; defaulting to SN210V
getStingerVersionAndConfig
Failed to retrieve the config ID
simDetectWPD
APDURESP
Dumping platform identifier\n
NfRestoreSETransceive returns %d
SE,RapRTKitOS
manifest is null or zero manifesetLen
DATA
outData->data.attV2AuthKeySize == outDataSize - sizeof(outData->data)
GetInstanceInfo
No matching delivery object found.
SLAMLoadAndInstallLogger_1_0_0_Internal
-[SETransceiveHelper copyDeviceType:]
getSEInfo
SN100V (Venus)
*outDataSignatureLength is 0
DF31
Failed to AMFDRDataPutForRestore : %@
seid
%02x
VerifyData
DEV 
Skipping MP <%s> because module not on SE\n
transmitting C-APDU: %zu \n
SE,BLFWKeysIdentifier
Pairing is requested but no server URL is provided\n
doOneAction
PreLoadEligibleApplets
SLAMMigratePTC
workaroundForPTCExport
ptc_listKeys
Unexpected command received %@\n
Error encountered when selecting CASD %@\n
sharingRequestSignature
Resetting due to 0x%hx
Options not present\n
YES
Found forceUpdateLoop: %lu\n
Called SEUpdaterDestroy updater %p\n
CreateFilesystemPartitions missing or wrong type
outDataSize >= sizeof(outData->data)
Size of UpdateTable.entries is zero
fSeController
Skipping SE update due to low number of available indices\n
While listing keys
SEUpdaterEventsLog.plist
Could not create listKeysCommandData\n
setLogLevelFromOptions
SE in restricted mode\n
Failed to send Select ISD
isSeshatEnrolledAndNotKUD
BootedOS
Get Data AUTH.PK %@\n
Failed to get nonce from manifest
HWState returns UnSupported, bailing out\n
kern.bootargs
Missing kRoseTagDigest in kRoseTagMeasurementSwBinDsp1
Refusing to V2 pair EOS with CSN 0x%X
info.tag == (ASN1_PRIVATE | ASN1_PRIMITIVE | 0x23)
\tsseKey hash   = %016llx\n
\tnoPasscodeCnt = %u\n
UNDEFINED
)
forceSLAM
SLAMLoadAndInstallOasis_1_0_07
Failed to get memory info, skipping indices check. Caught exception: %s\n
context && outdata && outlength
Unsupported manifest query version: 
b.data && b.length
Xenon Delete
Shutdown fSeHandle %p\n
getMinCSNForTrain
Failed to decode with dr %d\n
Pairing protocol version: %s\n
retAttV2AuthKey
\tkeybag hash   = %016llx\n
PerformScriptWithResult
Failed to query hardware version\n
Existing packageAID %s anyPackageOutOfDate %d wouldDowngrade %d anyModuleMissing %d, migrationTrigger %s
SE FW PROD Version
Fail to get SEID from the request
Could not copy device type with error %@\n
\tseid          = 
Passing fdrOptions with ApTicket of length %lu
Exception during dumpDebugInfo: %s\n
Pairing ended without error\n
UniqueDeviceID
%@%@
SE,UpdatePayload
InstallSEAppletTool
Failed to get JCOP Config Trigger, invalid item type
UOS1_ERROR
Failed to parse 'seci' value
Package already present, skipping pre load <%s> \n
doCommand_block_invoke
Get Attestation V2 Auth Key feature is not supported on this device with status %d\n
SEUpdaterErrorDomain
Missing or wrong length tag 0x%llx
QueryAppletStatus.cpp
40BD_DisableInFPM_EnableLogging
Fail to Img4EncodeItemEnd
At MP: %s %s
failed to Img4EncodeCreateManifest
expirationDate
MGGetBoolAnswer
[%3.3ld.%1.1d] [%s] %s: %s
SN210V (Ceres)
doStart
SE in restricted mode; skipping update\n
Encountered error when decoding top level 0x%llx\n
Command output:\n
Error code %d received when setting SE PK in SSE
Successfully dumped SE NVM to %s\n
SLAMLoadAndInstallSEAppletTool_0_0_2
Failed to write at offset 0x%x\n
seDeviceType does not support A9\n
libNfRestoreErrorDomain
Failed to set FTA activation with SW: %x\n
Successfully MFD'ed all applets\n
Skipping cleanup script <%s, %s> by key\n
Skip: JCOP version low.\n
Bad SW 0x%x received in get sharing request\n
SOCProductionMode
While parsing migration state
copySEID
   OSU Mem Reserves PHEAP %u THEAP %u\n
Failed to parse updatePayload as per UpdatePayloadItemSpec
SE310S detected based on manifest query response\n
DebugLogPath not present\n
SSESetSEPubKey returned %d\n
Failed to select CRS %d 0x%hx\n
Failed to get PRP\n
Pairing with reverse proxy: %d\n
AlohaVersion
Failed to select OSU\n
Pioneer Delete
Cleanup complete\n
Could not create deleteKeyCommandData\n
-[SETransceiveHelper transceiveAndRecordCapdu:rapdu:]
Failed to query submit pairing record: %s\n
Error encountered when copying SEID %@\n
size == sizeof(outData)
| 
Install SunspriteLogger: %s\n
%s: \n
Failed to GET_DATA Seshat 0x%x\n
Bad SW 0x%x received in copy SEID\n
Failed to parse CRS get perso state response\n
Unexpected length for perso state response\n
Failed to select CASD\n
HSMChallengeSE
Stinger applet not found\n
Unsupported SE key type
EVENT LOGGING: debugLogPath obtained\n
Fail to add seph
Bee MID was found, removing it\n
Could not get memory info, skipping indices check\n
Calling %s\n
_notifyport
Performed sharing with SEID %@\n
 bsn=0x
Fail to allocate imageProps
SLAMDeletePTCInstances
Configuring Stinger for %s environment\n
-[AlohaPairingController performAlohaPairing]
-[AlohaPairingController getReverseProxySettings:outError:]
Destroying Update Controller\n
Successfully loaded and installed SEAppletTool\n
SLAMSeosMigration_1_2_4
pos <= end
[keyData length] <= (end - pos)
 { 
Bad length for AM status
Dumping manifest query\n
SERS
v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24
Successfully extracted ApTicket from options.\n
Destroy BaseSEController\n
Unknown ChipID
SLAMDeleteNeon
Fail to create dictionary for request image properties
40D0_Enable_WithFilters_SW_ISO_Type
ApSecurityDomain
SEPEffectiveProductionMode
SecureElement
header == reinterpret_cast<CApduHeader_t*>(&((*bytes)[0]))
fOutput
MQ: %s: \n
new state --> %d\n
Failed to transceive code = %d\n
authRandom
retMac
Stinger version: 0x%04X\n
SLAMLoadAndInstallPTC
APDUREQ
UNK_STATE
Failed to parse device info?
Unable to construct obkg data\n
EffectiveProductionStatusAp
Error encountered when geting scrt %@ or scrt absent %d\n
ErrorCode
hasSSE()
Executing script %s ID 0x%llX
While parsing the respons from SLAM state
Successfully debug-injected SE Public Key into SSE for SEID %@\n
Assertion: 
 FPState=0x
Helium Load and install SLAM
SE,OSUPubKeyID
len <= bytes->size()
Cannot parse ImageBinary.apdus
reboot
SE Health Test Policy: %s\n
Oasis is up to date\n
While selecting CASD\n
Skip configuring %s: SE key not supported\n
SEUpdaterDestroy
Unexpected tag for perso state\n
Finish processing command: %s and returning %d \n
UnknownSEConfiguration
Bad length for platform secondary attack log indicator\n
Failed to retrieve CRS perso state\n
Skipping cleanup script <%s, %s> because of no erase install\n
Digest
DEBUG
Dumping AC Log\n
shouldAbortToAvoidBrick
SLAMDeleteBee
-[AlohaPairingController getReverseProxySettings:outError:]_block_invoke
X-Apple-Aloha-IP
CFDataGetLength(seid) <= sizeof(inData.data.seid)
4217_I2CB_FrameLog_Disable
fRequestDict
Found action %d\n
Cleanup script <%s, %s> executed successfully!\n
SLAMSlalomMigration_14_5_0
InstallSunspriteLogger
BSN: 
Sending GET DATA OBKG\n
Invalid input
AMFDRSealingMapCopyLocalData
> %s
getSharingRequestWithSignature
MP <%s, %s> executed successfully!\n
outData->data.authRandomSize <= (end - pos)
AppleSSE Log Starts - System Version %s
Skipping cleanup script <%s, %s> because package is not found\n
Cannot parse properties entries
Failed to send CommandGetAMState
DeleteNeonAppletYK300R106
RestoreInternal
size == sizeof(outData->data) + outData->data.keyDataSize + outData->data.attestationSize + outData->data.pubKeySize
Failed to parse as per DeliveryObjectItemSpec
Skipping SE update due to missing update path coming from CrystalSU\n
hasSufficientIndicesForOSU
SE,ChipID
Skip update since secure channel context AM is in progress\n
All instances found for %s\n
EVENT LOGGING: Successfully wrote to file %s with events %s:\n
RestoreOptions
Unknown ChipId: 0x%x for platform category mapping. Macro HELSINKI_HIDE_NEW_HW: %s
Skipping cleanup script <%s, %s> because module is not in selectable or installed state\n
DERParseSequence
Fail to add chip ID
  useDebugSSEInterface: %d\n
transceive
markForDeleteAll
Failed to decode script %d
setAuthRandom
Failed to add sesa
 overwrite: 0x
command
installSunspriteLogger
Skipping SE Updater due to enrolled Seshat\n
Success
Cannot parse UpdateTable entries
postflight
Pushed Update Payload successfully\n
Skip DeleteSEAppletTool by key\n
While deleting key slot 0x%x\n
EffectiveProductionStatusSEP
parseArgs
_baaSupportClass
Im4_error
Checking for legacy Oasis to cleanup\n
size >= sizeof(outData->data)
Unexpected length for sharing request %u\n
Failed to add seac
While writing command\n
%F %T (%z)
AlohaPairingVerified invalidated\n
Failed to get sharing request\n
SERestoreInfoHelpers.hpp
SLAM unavailable for Pre Load <%s> on current platform\n
Performing cleanup of old PTC keys\n
sendApdus
Bee Delete
SLAMInstallPTCInstances
Failed to parse SEFirmware.version.
Fail to enumerate
Perform Factory Postflight requested? %s\n
copyPayload
ReadResponse
-[SETransceiveHelper invalidate]
No RestoreOptions dictionary? Defaulting to limited environment\n
<libSEUpdater %p [%p]>{}
Wrong DeviceInfo
payload == nullptr
bytes && bytes->size() >= sizeof(CApduHeader_t)
415E_Value0C
Starting SE Dump\n
At SLAMDeletePTCInstances
Missing csn-train mapping for platform: 
-[AlohaPairingController invalidate]
err == 0 
SLAMDeleteSEAppletTool
PID  INFO %s, version  INFO 0x%04llX\n
-[SETransceiveHelper copyA9Parameters:]
I2CB_GuardTimeout_4107
StockholmPairingServerURL
AUTHREQ
userInfo
Error
4143_WeakPullDown
Unsupported chip ID
Dumping Update Table\n
Unexpected tag encountered 0x%llx, expected tag 0x%llx\n
libImage4Encode
Failed to query attack log status %d SW: %x\n
Attempting to split a non DER sequence %d\n
SE %u personalisable %d\n
Failed to load NFC stack
outData.deviceVersion > 0
Wrong UpdateTable entries
performSEHealthCheck
Oasis version mismatch. Current: %s, Expected: %s\n
Failed to configure 
UniqueChipID
Failed to extract ApTicket from options.\n
Fail to parse MQR
setFTAActivationStatus
Error encountered when retrieving casdCertificate %@\n
Pairing error debug log path: %s\n
While executing APDU %d
Fail to add sedh
fSource
Failed to toggle SE power on
Bad length for JCOP1 primary attack log indicator\n
Refusing to V2 pair with ChipID 0x%X
Skip pairing due to RestoreOptions not present\n
Skipping Pre Load <%s> by key\n
Unknown legacy platform category %u
UnknownSEChipType
A00000015153504341534400
40BD_EnableInFPM_EnableLogging
SLAMDeleteSilverBullet
Oasis Config ID not matching or missing, needs reconfiguration\n
Pre Load <%s, %s> executed successfully!\n
fail to create SEUpdaterObj
No command output, returning NULL\n
dataSize <= sizeof(payloadHeader.seid)
4108_DisableInFPM_DisableLogging
No matching FW found
Recovering incomplete termination
forceDeviceHwVersion
Failed to parse DStatusContainerDataItem
CheckAndInstallOasisUnifiedReader
ptc_DeleteKey
Unable to retrieve seDeviceType with error %@\n
 \t
info.tag == (ASN1_PRIVATE | ASN1_CONSTRUCTED | 0x1E)
Failed to add rtod
SN200V detected based on manifest query response\n
No slots are enrolled, can proceed\n
SLAM unavailable for MP <%s> on current platform\n
DeviceClass
data
40D0_Enable_WithFilters_SW_ISO
UOS2_ERROR
Failed to parse device data, manifest query: %s\n
/
Bad SW from GET_DATA AVAILABLE MEMORY: 
LoadAndInstallSunspriteLogger
Fail to add SEID
RestoreOptions not a dict?
outError && outDict
End of LogBuffer\n
I2CB_FrameLog_4217
validate
SLAM
endpair payload %@\n
Command
HSMChallengeSEP
certSize <= (end - pos)
len >= 2
Neon Delete
DebugArgs
Failure
size of MQRD doesn't match
PairStockholm
Unexpected CPLC data top level tag %llu
Failed to send select ISD
EffectiveSecurityModeAp
SN300V (Eos)
no
transceiveInternal
Got personalisable SE with nil manifestQuery?!
seHealthTest
Fail to Img4EncodeItemBegin
setActivateFTA
Stinger Config ID not matching or missing, needs reconfiguration\n
Oasis applet not found\n
Installing Oasis applet\n
PTC SLAM
SESA
Unable to form plist from data %@\n
(end - pos) >= dataSize
SecTaskCreateFromSelf
Cannot parse UpdateTable.
Cannot parse ImageBinary.
Failed to toggle SE power off
Failed to get commnand set-config, invalid option: 
Install signal handlers\n
map::at:  key not found
SLAMDeleteDavenport
data is either not found or in wrong CFType
Hardware still not in a valid state: 
Failed to decode top level 7F21 dr %d\n
Error when copying a9 params %@\n
Pairing options:\n
ECID
Recover interrupted script 0x%llx before running 0x%llx
 
UpdateTable: 
No update table entry match found.
<FAILED TO VASPRINTF>
SLAMSlalomMigration_14_3_0
Failed to transceive code = %d
%s [%s]: 
SE310S (Juno)
forceProd
SLAMDeleteCopernicusAndSunsprite
Invalidating transceiver wrapper\n
Malformed sessionId received %@\n
sizeof(uint32_t) <= (end - pos)
tmpData
Cannot find SE ticket in restore option
SE HW type %d multi-OS %d\n
[
EndPair
InternalBuild
SecTaskCopyValueForEntitlement
Missing kSETagMeasurementUpdatePayload or wrong type
At cleanup script: %s, %s\n
Skipping Install Missing Instance <%s> by platform\n
A000000704C0000000000001
Wrong SEPK + SEID size %zu\n
Skip configuring %s with option %s: already configured.\n
isSCAMInProgress
No personalizable SE found\n
rd=md0
Failed to getSEPK : %@
MAX
Can't retrieve Image4 signer; unknown ChipID: 
No APDU
The csnMap of platform %d is empty. Skip the config item\n
Caller did not provide an output dictionary\n
sharingResultSignature
Failed to decode APDUs %d
Wrong type for kRoseTagMeasurementSwBinDsp1
CreateFilesystemPartitions
  apTicket.length: %lu\n
4108_EnableInFPM_DisableLogging
LoadAndInstallSEAppletTool
PTC key deleted with error %@\n
Malformed reply dictionary received %@\n
Error encountered when parsing IMG4Blob %d\n
SEPEffectiveSecurityMode
SEID
Could not find a matching script within SEFW
getSEHealthCheckResult
At Configure OSU Reserve
Error encountered when decoding tag 0xDF21\n
fstat()
isFPRequired
No PTA loaded on device, skipping delete operation\n
Missing mandatory outparam
Skip pairing due to version %@\n
SOCSecurityMode
retAuthRandom
Warning APDU: %s idx %d replaying %d
Fail to sendApdus
Skip sending the Manifest because of nonce mismatch\n
wouldDowngrade
ExecuteCommand
outDataSignature && outDataSignatureLength
-[SETransceiveHelper crsSetSharingResult:signature:error:]
Wrong type for kRoseTagMeasurementRTKitOS
Failed APDU # %ld during attempt # %d; replaying from scratch\n
Stinger is up to date (version: 0x%04X)\n
index>=0 && index<fObjs.size()
-[SETransceiveHelper selectWithAID:]
SE >>>> %@\n
SessionId
copyIdentifier
CFDataGetLength(seid) <= sizeof(inData->data.seid)
Caught exception %s\n
A000000704C0000000000002
415E_Value00
Cannot switch to UOS
Available indices in index table: %u, Total indices in index table: %u, Max indices in JCOP: %u, Total available indices in JCOP: %u\n
Releasing transceiver wrapper\n
doAlohaPairing
-[AlohaPairingController performHTTPRequestWithRequestDict:outError:]
 }
Context 0x%X status 0x%X\n
singleStep
ExceptionLog_40D0
Failed to get commnand get-config, unsupported se key
Proxy aborted? %d\n
outData->data.macSize <= (end - pos)
userID
Fail to Img4EncodeItemCopyBuffer
rebooting\n
!fIsDone
getDeviceHardwareVersion
expectedBSN
Failed to parse DStatusContainerItem
outData->data.resultSignatureSize <= (end - pos)
Unsupported SLAM SEFW version %u.
-- GET STATUS APPLICATIONS -- \n
i24@?0^{?=Q{?=*Q}}8^B16
yes
ProductionUpdatePayloadHash
Fail to get Nonce from the request
Pairing not enabled\n
Failed to parse signedSection as per SignedSectionItemSpec
SN300V3 detected based on manifest query response\n
At Pre Load: %s %s
SEUpdaterCreate
Got Updater Context %s\n
binaryItem.data && binaryItem.length
fDeviceInfo
Fail to parse SEFW.
*outDataSignature is nullptr
Error encountered when decoding cert SN\n
scrt
AUTHRESP
setEraseInstall
[cert isKindOfClass:[NSData class]]
SN200V (Ceres)
SE Hardware Failure!
EVENT LOGGING: Error writing to file - %s\n
 with option 
cbNfRestoreSEEnumerate
Unexpected SW 0x%hX
Failed to parse attack log output\n
SLAMMigrateArgon_2_1_4_0B
Unable to decode top level 0x%llx\n
Successfully deleted Neon Applet YK300R106 with AID: %s\n
SE FW DEV Version
debugLogPath is unavailable, unable to log APDU and plists\n
activated
IOGeneralInterest
info.tag == (ASN1_PRIVATE | ASN1_PRIMITIVE | 0x2A)
FPF
while encoding extensions : %d\n
\tuserID        = %u\n
Invalid health check policy: 
Bad length for context
Unsupported firmware version: 
queryInfo
EVENT LOGGING: Options not present\n
INFO
bytes
injectSEPKtoSSE
image
skipUpdate
Could not get Oasis version: SW=0x%X, size=%zu\n
Krypton SLAM
-[SETransceiveHelper copySESignature:hsmChallengeSE:ecid:outError:]
len < bytes->size()
4108_EnableInFPM_EnableLogging
fSeHandle
Failed to configure Stinger\n
PerformSLAMMigrations
Failed recovery with scriptID 0x%llx, error was %s
Forcing device hardware version %u\n
sendManifestQuery
libSEUpdater
getSigKeyCertificates
Failed to decode CPLC data top level tag %d
Missing kRoseTagDigest in kRoseTagMeasurementRTKitOS
input.data && input.length
Cannot parse property
Transmitting C-APDU %d: %zu\n
parseStartOptions
FAILED
********************************************************************************\n
 rsn=0x
Cannot init sequence for DeliveryObject.binaries
Skip sending the Update Payload because of IM4 state %s\n
RSN 0x%X BSN 0x%X, skipSLAM %d forceSLAM %d isDowngrade %d\n
deviceFPFBSN 0x%x deviceFPREV %d deliveryBSN 0x%x deliveryFPFRev %d amStateOK %d bsnChanged %d revChanged %d ret %d\n
Seos SLAM
Delete Oasis
Bad length for primary attack log indicator\n
Failed to select seshat with ret: %d and sw: %x\n
doPerform
PTC Load and install SLAM
signInternal
_AddError
fmt
Error encountered when decoding tag 0xFE\n
Encountered error when retrieving seDeviceTypeData from %@\n
IM4M_validated
packageOnSE.size() >= versionLocationInPID.second && targetPackageAID.size() >= versionLocationInPID.second && versionLocationInPID.first < versionLocationInPID.second
-[AlohaPairingController beginPair:]
attestation
Resuming interrupted script 0x%llx
SEFW: %s: \n
InstallMissingInstances
EOSMemoryReserve_412A
ErrorMessage
Failed to select ISD
data.data && data.length
Cannot init sequence for ImageBinary.apdus
CF=(
Fail to add Nonce
Aloha Pairing failed with return code\n
Error encountered when building apdu resp dictionary: %@\n
PRP timed out %d\n
Reinstall PTC
dumpDebugInfo
Failed to get commnand set-config, unsupported se key
logSink
outDataSize <= sizeof(*outData)
Skip LoadAndInstallSEAppletTool by key\n
v12@?0i8
ApBoardId
4108_DisableInFPM_EnableLogging
Receiving R-APDU %d: %zu\n
receiving R-APDU: %zu \n
Fail to DERDecodeSeqInit firmwareArray.
getBlessedUser
print
SE Health check result: %s\n
Failed to query Seshat KUD status, pass forceUpdate if you really know what you are doing and want to skip it\n
Could not get Stinger version: SW=0x%X, size=%zu\n
Failed to get config item 
OBKG
SN300V detected based on manifest query response\n
DERDecodeData
Error encountered when forming request body %@\n
ImageBinary.type is out of range.
Failed to query Seshat KUD
SE is PROD_EVAL -> Skip SE-SEP pairing\n
Oasis Config ID: %s\n
Bailing out.\n
Failed to parse top level %d
disableAMRetry
SE,FactoryMode
performAuthKeySharingWithAppleSSE
SE is PROD_EVAL -> Skip SE-SEP pairing verification\n
Can't retrieve config ID since JCOP is not active
Slalom Dev SLAM
verifyPairing
While terminating
Unable to EnableTestSEContext %d
Unified Reader check/install completed successfully\n
Slalom Prod SLAM
Unexpected SLAM version length %zu
Error.hpp
While reading response for command\n
Unknown command: 
Attempt %d state %d is not yet ready, sleeping a bit\n
Failed to get expected config data, invalid option: 
Setting debugArgs (kv): %s=%s\n
SE,ID
Failed to retrieve SEPK %d 0x%hx\n
I2CA_FrameLog_4216
Unexpected state encountered %lu\n
[%s] %s: %s
Successfully pushed binary: %s\n
Failed to select CRS 0x%X\n
Unexpected Get Status response for BeeConnexions (size=%zu): %s\n
SLAMMigrateCopernicus_2_5_4_LoadAndInstallSunsprite_2_2_6
certificates
Failed to parse forceDeviceHwVersion debug argument
/usr/standalone/firmware/SLAM/SLAM.sefw
Pairing hostname URL: %s\n
Failed to copy SEID
  request    %@\n
FactoryPostflight revision: 
Failed to open file %s\n
-[AlohaPairingController processEndPair:]
performNextStage
} 
DumpSE
Failed to set MFDAll ret: %d\n
NULL deviceInfo
Start of LogBuffer\n
Fail to DERDecodeSeqNext firmwareArray.
verifyAlohaPairing
sizeof(CApduHeader_t) + payloadLen == bytes->size()
Can't get weakly linked NFHM class, nothing to personalize\n
Error getting secure element array
ECID from endPair %@ _ecid %@
4217_I2CB_FrameLog_Enable_Debug
Failed to add rbdd
SunspriteLogger Applet is already installed, skipping load and install\n
Downgrade past 0x2A is not allowed
Argon Migration SLAM
Error encountered when transceiving select %@\n
Unable to split certificates\n
Wrong size for get config response 
-[AlohaPairingVerifier performAlohaVerification]
basic_string
SLAMMigrateIron_2_0_13
Error encountered when getting OBKG %@\n
Error encountered when processing end pair:%@\n
Response from AMFDRDataPutForRestore %d (%@)\n
Failed SW 0x%hX at idx %d
sePk
Copernicus + Sunsprite SLAM
-[SETransceiveHelper crsGetSharingRequestWithError:]
BAADelegateImpl
NSObject
Append
CXX
HexString
DER
SETransceiveHelper
BAASupportDelegate
AlohaPairingVerifier
AlohaPairingController
FDR
APDUUtil
setFSeController:
setValue:forHTTPHeaderField:
asCXXVector
generateSigKey:keyData:attestation:pubKey:
containsObject:
_transceiver
performAlohaVerification
performHTTPRequestWithRequestDict:outError:
setConnectionProxyDictionary:
setObject:forKeyedSubscript:
_options
componentsSeparatedByString:
.cxx_destruct
appendData:
getCXXApduWithCla:ins:p1:p2:payload:
setReverseProxySettings:
dataWithLength:
setRapduRecord:
autorelease
beginPair:
copyA9Parameters:
dataWithBytes:length:
processEndPair:
_debugRecordPath
createFileAtPath:contents:attributes:
TB,N,V_useReverseProxy
isProxy
setDelegate:
count
conformsToProtocol:
resume
DERItem
T@\"NSDictionary\",&,N,V_reverseProxySettings
initWithFormat:arguments:
personalisable
writeRecord:fileExtension:
T@\"NSString\",&,N,V_debugRecordPath
issueNewCertificate
prepareLazily
self
numberWithBool:
stringByAppendingPathExtension:
appendU64LE:
isKindOfClass:
initWithOptions:seController:
performAlohaPairing
debugRecordPath
setDebugRecordPath:
setEcid:
stringWithCString:encoding:
stringWithCXXString:
URLWithString:
UTF8String
array
mutableBytes
numberWithUnsignedInteger:
setAlohaVersion:
useReverseProxy
apChipId
bytes
defaultManager
integerValue
setValue:forKey:
T@\"NSString\",&,N,V_fullServerSessionID
_state
addObject:
info
performSelector:withObject:
T@\"NSString\",&,N,V_serverSessionID
_useReverseProxy
defaultSessionConfiguration
serverSessionID
hash
rapduRecord
retain
T@\"NSData\",&,N,V_seid
dealloc
appendU16BE:
dataWithCXXVector:
debugDescription
length
numberWithLongLong:
sharedHardwareManager
class
crsSetSharingResult:signature:error:
dataWithBytesNoCopy:length:freeWhenDone:
initWithController:options:
processInfo
_reverseProxySettings
description
getAPDUWithCla:ins:p1:p2:payload:
setState:
dataWithContentsOfFile:
release
alohaVersion
processAuthReqPayload:outError:
.cxx_construct
_fSeController
alohaPlistRecord
dataWithCapacity:
isEqual:
appendU16LE:
retainCount
confirmSigKey:status:
copySESignature:hsmChallengeSE:ecid:outError:
injectSEPKtoSSE:
subdataWithRange:
_restoreEnvironment
getSigKeyExpDate:expirationDate:
initWithSEController:
setAlohaHostname:
T#,R
copyCasdCert:
transceiveAndRecordCapdu:rapdu:
setServerSessionID:
_serverSessionID
injectSEPKtoSSE_FDR:
secureElements
setSigKey:expirationDate:keyData:certificates:
setUseReverseProxy:
dictionaryWithObjects:forKeys:count:
queryHardwareSupport:
T@\"SETransceiveHelper\",&,N,V_transceiver
addObjectsFromArray:
appendU8:
isInternal
setTransceiver:
asCXXString
isEqualToNumber:
numberWithInt:
setHTTPBody:
uppercaseString
T@\"NSMutableArray\",&,N,V_capduRecord
getBlessedUser:keybagUUID:
seid
setAlohaPlistRecord:
transceiver
enumerateObjectsUsingBlock:
mutableCopy
setSeid:
_alohaPlistRecord
_apChipId
manifestQuery
T@\"NSMutableArray\",&,N,V_rapduRecord
appendU32LE:
setFullServerSessionID:
_alohaHostname
injectSEPKtoSSE_Debug:
numberWithUnsignedInt:
objectAtIndexedSubscript:
reverseProxySettings
copyDeviceType:
appendBytes:length:
writeToFile:options:error:
zone
T@\"NSNumber\",&,N,V_ecid
T@\"NSString\",?,R,C
init
isEqualToString:
sessionWithConfiguration:
_fullServerSessionID
arrayWithObjects:count:
dataWithDERItem:
dataWithHexString:
numberWithUnsignedLong:
propertyListWithData:options:format:error:
setCapduRecord:
dataWithPropertyList:format:options:error:
errorWithDomain:code:userInfo:
isMemberOfClass:
_ecid
copySeid:
dataUsingEncoding:
getSigKeyCertificates:certificates:
getValue:
statusCode
stringWithCapacity:
setApChipId:
TQ,R
dataWithData:
numberWithInteger:
performAuthKeySharingWithAppleSSE:sharingRequest:requestSignature:resultSignature:withError:
T@\"NSString\",R,C
_seid
crsGetSharingRequestWithError:
superclass
copy
getSharingRequestWithSignature:withError:
setHTTPMethod:
verifyAndRetrieveServerSessionId:
asHexString
boolValue
T{shared_ptr<SEUpdater::P73BaseSEController>=^{P73BaseSEController}^{__shared_weak_count}},N,V_fSeController
capduRecord
stringWithFormat:
_capduRecord
fullServerSessionID
submitPairingRecord:
dataTaskWithRequest:completionHandler:
processApduReqPayload:outError:
T@\"NSString\",&,N,V_alohaHostname
appendU32BE:
getHwSupport
_alohaVersion
getSEPK:andSEID:deleteExisting:error:
performSelector:
processName
requestWithURL:cachePolicy:timeoutInterval:
performSelector:withObject:withObject:
TQ,N,V_state
fSeController
getBytes:length:
unsignedIntValue
T@\"NSNumber\",&,N,V_alohaVersion
T@\"NSNumber\",&,N,V_apChipId
getReverseProxySettings:outError:
objectForKeyedSubscript:
stringValue
appendFormat:
respondsToSelector:
selectWithAID:
stringByAppendingString:
stringByAppendingPathComponent:
_alohaServerIP
appendU64BE:
base64Encoding
invalidate
setAuthRandom:mac:error:
T@\"NSMutableArray\",&,N,V_alohaPlistRecord
_rapduRecord
alohaHostname
countByEnumeratingWithState:objects:count:
ecid
recordApdu:toRecord:
state
i28@0:8I16^@20
B24@0:8@\"Protocol\"16
B44@0:8^@16^@24B32^@36
i32@0:8^I16[16C]24
B24@0:8@16
@24@0:8r^v16
Q
B24@0:8#16
^{_NSZone=}16@0:8
@\"NSMutableArray\"
v20@0:8B16
{CApdu=^^?{shared_ptr<std::vector<unsigned char>>=^v^{__shared_weak_count}}^{?}*QQ}40@0:8C16C20C24C28@32
#16@0:8
@32@0:8:16@24
Vv16@0:8
@16@0:8
B24@0:8^@16
@32@0:8^@16^@24
i44@0:8I16Q20@\"NSData\"28@\"NSArray\"36
@\"NSData\"
B40@0:8@16@24^@32
@32@0:8^v16^v24
B16@0:8
B
B24@0:8:16
@48@0:8@16@24@32^@40
v32@0:8{shared_ptr<SEUpdater::P73BaseSEController>=^{P73BaseSEController}^{__shared_weak_count}}16
@\"NSNumber\"
@24@0:8:16
@\"NSString\"16@0:8
v16@0:8
r^v
@\"SETransceiveHelper\"
{vector<unsigned char, std::allocator<unsigned char>>=**{?=*}}16@0:8
{?=*Q}16@0:8
@32@0:8{shared_ptr<SEUpdater::P73BaseSEController>=^{P73BaseSEController}^{__shared_weak_count}}16
i28@0:8I16^Q20
v20@0:8C16
i24@0:8I16i20
@24@0:8r^{?=*Q}16
i44@0:8I16^@20^@28^@36
v20@0:8I16
{shared_ptr<SEUpdater::P73BaseSEController>=\"__ptr_\"^{P73BaseSEController}\"__cntrl_\"^{__shared_weak_count}}
i16@0:8
@32@0:8@16^@24
Q16@0:8
@24@0:8@16
v32@0:8@16@24
@\"NSString\"
i44@0:8I16Q20@28@36
@56@0:8@16@24@32^@40^@48
v20@0:8S16
{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16@0:8
q24@0:8^@16
{shared_ptr<SEUpdater::P73BaseSEController>=^{P73BaseSEController}^{__shared_weak_count}}16@0:8
v24@0:8@16
@40@0:8:16@24@32
@40@0:8{shared_ptr<SEUpdater::P73BaseSEController>=^{P73BaseSEController}^{__shared_weak_count}}16r^v32
v24@0:8Q16
@24@0:8^@16
v48@0:8{Apdu=^^?{shared_ptr<std::vector<unsigned char>>=^v^{__shared_weak_count}}}16@40
@\"NSDictionary\"
@40@0:8C16C20C24C28@32
@40@0:8r^v16{shared_ptr<SEUpdater::P73BaseSEController>=^{P73BaseSEController}^{__shared_weak_count}}24
```
