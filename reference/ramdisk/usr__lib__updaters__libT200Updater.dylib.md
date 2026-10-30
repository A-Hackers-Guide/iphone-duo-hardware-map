# `/usr/lib/updaters/libT200Updater.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 265,872 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2280)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/usr/lib/updaters/libT200Updater.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (729)

```
SkipFirmwareMapStore
Path
measurementDict
BatFWUpdater: [%d] BC__sendImage \n
ChemistryID
T200TagChipID
copyFirmwareData
skipPlistStore == FALSE
%s:%d Error: CFPropertyListCreateWithData failed. \n
%s:%d Error: CFStringCreateWithFormat failed.\n
%s:%d keyPath is NULL \n
[%d] %s:%d Certificate BC__sendImage failed commStatus=0x%X \n
Unable to get BMUID
Missing kT200BuildIdentityPathKey
filePathURL
batteryInfo
BatFWUpdater: [%d] Connect to AppleGasGaugeUpdate PackIndex:%d \n
restoreSystemPartition
%s:%d NumSupportedBMU from IODT 0x%X \n
board_id
/Library/Caches/com.apple.xbs/34FB187E-6E8B-4359-9FD4-26A4FD9EA98C/TemporaryDirectory.84cANW/Sources/VeridianDylibs/T200RestoreInfo/T200RestoreInfo.c
T200TagResponseFirmwareTicket
\t\t<Firmware> maj=%d med=%d min=%d rev=%d</Firmware> \n
numUnused == 0
[%d] %s:%d start Send Binary Image to Update Firmware SMC API, update %d \n
[%d] %s:%d ERROR:Failed Updating the Configuration 
_T200GetBMUID
result == kT200Success
\t\t<DNVDSector2>%u</DNVDSector2> \n
%s:%d Battery update failed for Battery Index: %d with error: %d\n
[%d] %s:%d Failed with Error:%d  \n
_getFirmware
derstat == 0 
_isBatteryDevFused
T200TagProductionMode
%s:%d BMUID %d \n
\t\t<BoardID>0x%X</BoardID> \n
\n
type != NULL
_performBatteryUpdateThread
[%d] %s:%d Do we need to update(0-No 1-Yes)= %d, current veridian fw: %d set-id:%d    new_firmware:%d new_set-id:%d \n
[%d] %s:%d Send dummy Digest Dictionary for Access Mode Enable \n
T200OptionTicket
Cannot get DeviceInfo
T200TagCertificateEpoch
\t\t<UpdaterStatus>%d</UpdaterStatus> \n
hwVersionstr != NULL
_parseTatsuResponse
[%d] %s:%d Does Image updated (0-No 1-Yes)= %d, Veridian Image Loaded: %d set-id:%d    Veridian Image Requested:%d new_set-id:%d \n
[%d] %s:%d Start Send DigestMap+Crypto smc API \n
\t\t<HWReset>%u</HWReset> \n
[%d] %s:%d End  Failed  Error:%d 
%s:%d requestDict =\n
%s:%d Failed %d \n
_getBatteryBoardID
kAMSupportErrorNone == status
%s:%d isBootedOS: %d \n
%u
_extract_cell_ID_Supported
result == 0
batteryIndexMsg
UpdaterOptions
BuildIdentityTags
%s:%d Add Entitlements T200TagEFFV\n
T200GetBatteryModelIDs
fwPlistMutableRef
[%d] %s:%d End Crypto \n
performVersionCheck
CreateFileData: AMSupportPlatformFileURLExists returned FALSE
buildIdentity
%s:%d status=%d
%s:%d Copy the file %s to  %s\n
requestDict
\t<BatteryIndex>%d</BatteryIndex> \n
[%d] %s:%d End with error %d \n
[%d] %s:%d BC__commitImage failed commStatus=0x%X
BMU,Firmware
T200TagFWOverWrite
BatFWUpdater: Failed to BC__connect
\t<VersionInformation> \n
T200: Invalid Updater Data
[%d] %s:%d Battery UniqueID is Zero. Use Battery Unique ID from getInfo.\n
[ 
T200: Invalid Updater Data 
updaterOptions
AMSupportWriteDictionarytoFileURL
[%d] %s:%d sendbin status  %d \n
%s:%d Is Battery DevFused? %d \n
Cannot allocate memory for updater
chemID != NULL
%s:%d Update type kT200UpdateTypeConfiguration \n
amerror == kAMSupportErrorNone
t200UpdaterData->batteryInfo[batIdx].chipID == uint32Val
%@.%@.%@.%@.%@
digestMapPropertyLength == T200_UPDATER__FIRMWARE_HASH_SIZE
T200: Check Update Needed Failed for Configuration Image %d
%s:%d Add Entitlements T200TagFWOverWrite\n
BatFWUpdater: [%d] BC__getInfo \n
board_id_data
[%d] %s:%d Battery UniqueID: %u \n
[%d] %s:%d Skip updating as this is not supported cell-id \n
%s:%d PLIST  Img Version= %d  SetID= %d. \n
T200ErrorDomain
PersonalizationOption
Unable to get kT200TagMeasurementFirmwarePlist
%s:%d firmwareBytes is NULL\n
%s
%s:%d This is Tatsu signing ,we are done  \n
Error: restoreSystemPartition is NULL.
%s:%d Error: CFStringCreateWithFormat failed. \n
firmwareMapDataRef != NULL
BatFWUpdater: [%d] Error starting update: 0x%X \n
%s:%d failed to create key substring \n
\t<ResetCount> \n
\t\t<Voltage>%f</Voltage> \n
Error: Failed to parse Image Version.
BundleDataDict
tmpData && (CFGetTypeID(tmpData) == CFDataGetTypeID())
Error: input is NULL.
config_digest && config_payload && dnvd_digest && dnvd_payload
Expected :
BMU,ForceFirmwareUpgrade
T200TagNonce
T200TagUniqueID
%s:%d Error: Failed to retrieve Firmware PLIST. \n
%@%@
DeferredCommit
%s:%d Start file_name=%s \n
%s:%d Loading FW from %s\n
tmpNumb && (CFGetTypeID(tmpNumb) == CFNumberGetTypeID())
AppleGasGaugeUpdate
%s:%d fOptions is NULL \n
data != ((void*)0)
IsTwoStageSupported
dnvd
BMU,
T200Updater
%s:%d T200 Options Empty \n
[%d] %s:%d ERROR:Failed Updating the Firmware \n
[%d] %s:%d ERROR:Failed Updating the DNVD 
_T200GetNumSupportedBMUFromDT
\t<CommunicationStatus>%d</CommunicationStatus> \n
\t\t<Crypto>%u</Crypto> \n
\t\t<TwoStageSupported>%u</TwoStageSupported> \n
 Digest: %s %s \n
[%d] %s:%d End Send Certificate smc API \n
[%d] %s:%d End Send Binary Image %d  \n
found
PreflightRequired
Cannot allocate memory for tagsInBI
%s:%d Restore options is empty\n
READ_DATA__getVersionInformation
success == true
t200UpdaterData->fOptions
%s:%d Failed getting the kT200OptionOptions \n
%s:%d %s \n
_createMeasurementDict
%s:%d Start \n
_T200UpdaterExecCommand
v16@?0Q8
t200UpdaterData
fwPlistDictRef && CFGetTypeID(fwPlistDictRef) == CFDictionaryGetTypeID()
T200CreateDictionaryRemovingKeyPath
manifestDataRef != NULL
BatteryIndexInfo is NULL
%s:%d Internal Restore: %d \n
ret == 0
T200TagDerFirmwarePlist
ret == kT200Success
NULL != firmwareBytes
BatFWUpdater: cannot open gas gauge device 
%s:%d isOTA: %d \n
fDataIn
rc==KERN_SUCCESS
firmwareMapLen && firmwareMapBuffer
deviceInfo
derstat == DR_Success
%s:%d Removing %s and %s key-value pairs before digest computation \n
\t<UpdaterStatus>%u</UpdaterStatus> \n
T200: Check Update Needed Failed for DNVD Image %d
%s:%d PSimPresent from IODT 0x%X \n
cfErrMsg
CreateFileData: Fail to run AMSupportPlatformCopyURLWithAppendedComponent with dstBundleURL
dataDictRef!=NULL
%s:%d Failed getting info %d  \n
%s:%d Entering execCommand: command = performNextStage \n
t200UpdaterData->fInput != NULL
Error: Failed to get chem ID.
%s:%d CC_SHA256_Final %d\n
rawSignature != ((void*)0)
%s:%d Skipping update - BoardID or ChipID parameter not present in EDM, battery is dev fused and internal restore \n
%s:%d Error: Failed to performVersionCheck for DNVD for Battery Idx: %d. \n
</AMSResponse> \n
copyStrippedFirmwarePlist
CFGetTypeID(tmpDict) == CFDictionaryGetTypeID()
%s:%d End,Failed with ret=%d\n
BatFWRestore: %s
outputDict
CreateFileData: Fail to run AMSupportCopyFile with dstFilePathURL
__T200UpdaterCreateRequestWithLogging
T200: Check Update Needed Failed for DNVD Image
%s:%d Cell_iD is not skip: \n
BMU,EnableValidationCommands
a0p2
%s:%d Skipping update - Internal device with battery-state=-1.\n
chipIDRef != NULL
[%d] %s:%d Manifest BC__sendImage failed commStatus=0x%X \n
%s:%d Device Img Version= %d  SetID= %d. \n
Fail get the file path 
BatFWUpdater: [%d] Failed to BC__GasGauge_connect \n
numBatteryCount
firmwaredataRef && CFGetTypeID(firmwaredataRef) == CFDataGetTypeID()
T200: Check Update Needed Failed for Configuration Image %d \n
\t</ADCReadings> \n
_T200GetPSimFromDT
UniqueID
Failed to BC__connect
BC__receive
%s:%d CFErrorRef is null
T200UpdaterPrivateHelper.h
RestoreOptions
BatFWUpdater: [%d] BC__commitImage \n
batModelIDs
[%d] %s:%d In BootedOS, performNextStage is Skipped if isTwoStageSupported is False \n
_commitImageSMCIF
targetUpdaterStatus == SU__STATUS__SUCCESS
%s:%d Busy loop end with status %d \n
%@; %u
BMUID
T200Firmware
%@
pubKeyPkcs1->data[0] == 0x04
[%d] %s:%d End Send DigestMap+Crypto smc API \n
CFGetTypeID(num_supported_data) == CFDataGetTypeID()
T200TagBoardID
bundleDataDict
AppleSMC
\t\t<Firmware>%u</Firmware> \n
%s:%d Number of Active Battery (%d) exceeds Max Number of Supported Battery (%d). \n
BMU,EnableDeveloperCommands
BundlePath
configuration
ActiveBMUs
BMU
%s:%d Override is set \n
%s:%d Performing Parallel battery updates for %d batteries\n
_send_bin_retry
BMU,ChipID
%s:%d DeviceInfo Dict\n
/Library/Caches/com.apple.xbs/34FB187E-6E8B-4359-9FD4-26A4FD9EA98C/TemporaryDirectory.84cANW/Sources/VeridianDylibs/T200Updater/T200Updater.c
fwStrippedPlist
firmwareMapDataRef!=NULL
[%d] %s:%d start Send Binary Image to Update DNVD SMC API, update %d \n
CreateFileData: Fail to run AMSupportMakeDirectory with dstFilePathURL
[%d] %s:%d Start \n
[%d] %s:%d End \n
err == 0
%s:%d CC_SHA256_Update %d\n
writeSMCKey
%s:%d Error: Failed to performVersionCheck for Config for Battery Idx: %d. \n
%s:%d update required for Battery Idx %d? DNVD: %d, Config: %d, Firmware: %d. \n
[%d] %s:%d  show fOptions \n
.
firmwareMapDataMutableDict != NULL
[%d] %s:%d Start
computeFirmwareDigest
EnableDeveloperCommands
DeviceInfo
Cannot allocate memory for outputDict
Read failed for key '%s' (0x%X, 0x%X)\n\n
%s:%d Is Two Stage Supported: %d. \n
\t\t<Firmware supported SetIds> DNVD1:0x%x  DNVD2:0x%x Config:0x%x </Firmware supported SetIds> \n
%s:%d Rollback FW Version: %d \n
%s:%d Performing single battery restore for Battery Index: %d\n
Limited
payload
\t</VersionInformation> \n
bmu-board-id
numOfActiveBatteryRef != NULL
%s:%d FA/VNV Entitlement Exist. \n
[%d] %s:%d set_id_0=%d set_id_1=%d set_id_2=%d \n
[%d] %s:%d failed with result =%d \n
Revision
SkipSameVersion
T200OptionRequest
outDict != NULL
userInfo
subDeviceInfo && (CFGetTypeID(subDeviceInfo)==CFDictionaryGetTypeID())
Unable to get kT200TagResponseFirmwareTicket
CreateFileData: Fail to run AMSupportCreateDataFromFileURL
CommunicationError
*batModelIDs
plistMutableStr != NULL
_T200GetChipIdFromDT
%@; %@: %u
ResponseTags
%@.%@
BatFWUpdater: [%d] FW:%u CFG:%u DNVD1:%u DNVD2:%u BL:%u UniqueId:%u Chemistry:%u hwId:0x%08X isTwoStageSupported:%u \n
[%d] %s:%d Updater Status (%d) before retry. \n
\t\t<ResetReason>%u</ResetReason> \n
DestBundlePath
<AMSResponse> \n
T200: Commit Image Failed
mountURL
signature != ((void*)0)
\t\t<Current>%f</Current> \n
copyRetrievedFirmwarePlist
T200: Check Update Needed Failed for Configuration Image
[%d] %s:%d End Failed with %d  \n
%s:%d Could not find the signature =%d\n
LocalSigningID
_updateBMUTags
CFGetTypeID(chip_id_data) == CFDataGetTypeID()
%s:%d Add Entitlements T200TagVNVEnableOption\n
BatFWUpdater: [%d] Error getting info: 0x%X \n
%s:%d start  \n
%s:%d Successfully stripped firmware PLIST. \n
%s:%d Start\n
T200TagEFFV
%s:%d Failed getting info try %d \n
chip_id_data
BatteryModelID
CreateDataFromFile
T200: Check Update Needed Failed for Firmware Image %d \n
_waitTillTargetUpdaterNotBusy_SMCAPI
\t<TimeStamp>0x%x</TimeStamp> \n
BMU,Nonce
BuildIdentity
options is NULL
BatFWUpdater: [%d] Error starting update: 0x%X. Retrying... \n
\t<UpdaterState>%u</UpdaterState> \n
%s:%d NumEnabledBMU from IODT 0x%X \n
BMU,Request
%s:%d data captured =%d\n
\r\n
[%d] %s:%d Veridian Fw  detected maj=%d med=%d min=%d rev=%d \n
data_len > 0
_send_diget_map
[%d] %s:%d BC__sendImage failed commStatus=0x%X \n
</VeridianInternalInfo> \n
Info
fw_map_digest
\t\t<DNVDSector1>%u</DNVDSector1> \n
_create_key_payload_Verison
success==true
_parseFWMapDigest
%s:%d Successfully retrieved firmware PLIST data. \n
%s:%d ChipId from IODT 0x%X \n
cell_id_skip
firmwareData
0x%02x 
[%d] %s:%d End Send Manifest smc API \n
[%d] %s:%d start Send Binary Image to Update Configuration SMC API, update %d \n
\t\t<UPDReset>%u</UPDReset> \n
[%d] %s:%d Failed to commitImage with status %d \n
RestoreInternal
%s:%d Parallel battery update failed\n
%s:%d Error: T200CreateDictionaryRemovingKeyPath failed. \n
Unable to get kT200TagMeasurementPatch
FirmwareData is NULL in input options
[%d] %s:%d End Send Binary Image %d  Faild targetUpdaterError=%d \n
Nonce
BMU,UniqueID
AMSupportPlatformFileURLExists
\t\t<SerialNumber>%u</SerialNumber> \n
%s:%d Disable Parallel Update: %d \n
[%d] %s:%d End performNextStage for Battery Index: %d \n
fOptions
1 == boolVal
PreflightTickets
CFDictionaryCreateMutable
Write failed for key '%s' (0x%X, 0x%X)\n\n
BatFWUpdater: [%d] Error getting info: 0x%X. Retrying... \n
T200: Check Update Needed Failed for Firmware Image
[%d] %s:%d Entitlment update successful  \n
imgVerRef && (CFGetTypeID(imgVerRef) == CFNumberGetTypeID() || CFGetTypeID(imgVerRef) ==CFStringGetTypeID())
_retrieveSignature
DisableParallelUpdate
,
%s:%d Restore Options\n
batteryErrors && batteryResults
%s:%d Replacing LF with CRLF before digest computation \n
[%d] %s:%d Success. Valid DNVD2 Version (%u) found on HW. Skip Retry. \n
firmware
AssertMacros: %s, %s file: %s, line: %d, value: %lld\n
Missing kT200BuildIdentityInfoKey
PackIndex
%s:%d End. Return: %d \n
%s:%d FW Override: %d \n
T200: Program Image(s) Failed
dataRef && CFGetTypeID(dataRef) == CFDataGetTypeID()
firmwareDataRef
BatFWUpdater: [%d] BC__startUpdate \n
%s:%d Single battery restore failed for Battery Index: %d with error: %d\n
[%d] %s:%d Skipping Second stage in update \n
%@.%@.%@.%@
%02X
[%d] %s:%d image len:%u \n
\t<ADCReadings> \n
_createRequestDictForTATSU fails.
bmu2-board-id
_getInfoSMCIF
\t\t<InternalTemperature>%f</InternalTemperature> \n
firmwarePlist
totalErrMsg
FirmwareIsOverride
tmpBool && (CFGetTypeID(tmpBool) == CFBooleanGetTypeID())
deviceIDRef != NULL
/usr/standalone/firmware/Veridian/FirmwareMap.plist
RollbackFWVer
BatFWUpdater: GasGauge Registry Value %d \n
[%d] %s:%d Update status:dnvd:%d conf:%d firmware:%d \n
_programImageSMCIF
keyCellIDSkip!=NULL
[%d] %s:%d start \n
chemistry
Cannot allocate memory for tagsInTssResponse
t200UpdaterData->fInput
Error: Write PLIST is failed.
%s:%d dict is NULL \n
%@%@; %@: %u
Fail to do AMSupportPlatformCopyURLWithAppendedComponent
%s:%d Force Firmware Upgrade: %d \n
restoreOptions
_extract_digest_map
manifestLen && manifestBuffer
[%d] %s:%d Success. Valid Configuration Version (%u) found on HW. Skip Retry. \n
Error: Failed to get HW Version.
BMU2,
AMSupportPlatformCopyURLWithAppendedComponent
[%d] %s:%d Start performNextStage for Battery Index: %d \n
storeFirmwarePlist
dict != NULL
CertificationURL
BatFWUpdater: Select GG %d for side channel communication\n
\t\t<DeviceType>%d</DeviceType> \n
IODeviceTree:/product
%s:%d start \n
T200TagRequestFirmwareTicket
T200TagRevision
error != NULL
\t\t<ModelID>0x%X</ModelID> \n
%s:%d Entering execCommand: command = queryInfo \n
bmu-chip-id
\t\t<SetIds> DNVD1:0x%x  DNVD2:0x%x Config:0x%x </SetIds> \n
%s:%d end \n
firmwareMapPropertyLength == T200_UPDATER__FIRMWARE_HASH_SIZE
T200: Check Update Needed Failed for Firmware Image %d
*error == NULL
_check_update_needed
[%d] %s:%d Skipping update \n
firmwareVersionRef && (CFGetTypeID(firmwareVersionRef) == CFNumberGetTypeID() || CFGetTypeID(firmwareVersionRef) ==CFStringGetTypeID())
[%d] %s:%d start Send Certificate smc API  \n
</VersionInformation> \n
t200UpdaterData != NULL
keyPath != NULL
createStrippedConfigDNVD
certDataLength != 0
_send_manifest
%s:%d fwData is NULL\n
<VersionInformation \n
[%d] %s:%d Skip Start Update command \n
TRUE == boolVal
[%d] %s:%d ERROR:Failed Updating the Configuration \n
[%d] %s:%d manifest len:%u \n
PreflightContext
tagsInBIRef
BC__transmit
%s:%d Cell_iD is Skip \n
Error: firmwareURL doesn't exist.
%s:%d Battery BoardID: 0x%X. \n
SingleBatteryRestore
%@%d
T200Updater.c
T200: Parse Tatsu response Failed
IODeviceTree:/defaults
%@%d%@
Missing kT200OptionBuildIdentity
infoDict
BatFWUpdater: [%d] BC__sendImage CRC32: 0x%08X (data_length: %llu bytes)\n
/Library/Caches/com.apple.xbs/34FB187E-6E8B-4359-9FD4-26A4FD9EA98C/TemporaryDirectory.84cANW/Sources/VeridianDylibs/insystem_communication.c
%s:%d Single battery restore failed\n
%s:%d Update type kT200UpdateTypeFirmware \n
%s:%d Error: fwPlist is NULL. \n
T200TagFAEnable
battery-state
%s:%d BoardId from IODT 0x%X \n
t200UpdaterData->fOutput != NULL
firmwareDictRef && CFGetTypeID(firmwareDictRef) == CFDictionaryGetTypeID()
%@.%@.%@
 [Battery %d]
%s:%d Skipping update - BoardID mismatch: DT=0x%X, Battery=0x%X, battery is dev fused and internal restore \n
_CFDictionarySetInteger32
certificate
err == kAMSupportErrorNone
chip_id
\t\t<CellIDs> DNVD1:%u  DNVD2:%u Config:%u </CellIDs> \n
product_node
_T200UpdaterCreate
_T200UpdaterExecCommand_block_invoke
[%d] %s:%d commitImage status  %d \n
buildIdentityDict
\t\t<DeviceId>%d</DeviceId> \n
%s:%d Battery[%d] ModelID: 0x%X \n
[DICT] %s \n
valid == 1
[%d] %s:%d ERROR:Failed Updating the Firmware 
BMU,Ticket
%s:%d End \n
[%d] %s:%d Start Send Manifest smc API \n
bmu-num-enabled
%s:%d Defaults Node present \n
%s:%d psim-present property available \n
%s:%d outputDict =\n
%s cmd=0x%x amount=%d\n
T200: Get Firmware Image(s) Failed [ChemID: %u]
_T200GetNumActiveBattery
BootedOS
%s:%d Failed with %d\n
restore_options
%s:%d Options Dict\n
T200UpdaterIsDone
_t200InitUpdater
input
[%d] %s:%d Failed to send bin with status %d \n
imageDict
\t\t<Configuration>%u</Configuration> \n
Error: kT200OptionOptions is NULL.
apiNameRef
BMU,ProductionMode
%s:%d lenDigestData=%d \n
bmu2-chip-id
/Library/Caches/com.apple.xbs/34FB187E-6E8B-4359-9FD4-26A4FD9EA98C/TemporaryDirectory.84cANW/Sources/VeridianDylibs/T200Updater/T200UpdaterPrivateHelper.c
tmpDict && (CFGetTypeID(tmpDict) == CFDictionaryGetTypeID())
\t\t<ChemID>%lu</ChemID> \n
certData != ((void*)0)
[%d] %s:%d digestmap len:%u \n
_send_bin
RestoreSystemPartition
_T200UpdaterGetTagsWithLogging
relativePathStr
t200UpdaterData->batteryInfo[batIdx].targetUpdaterError == kT200Success
BatFWUpdater: %s
%s:%d Number of AppleGasGaugeUpdate supported: %d \n
DeviceInfo is NULL
fileExists
%s:%d Error: Failed to performVersionCheck for FW for Battery Idx: %d. \n
public_key != ((void*)0)
_T200GetNumEnabledBMUFromDT
HWVersion
Options
[DICT] %s\n
Missing kT200OptionFirmwareData and kT200OptionBundleDataDict
ForceFirmwareUpgrade
/usr/standalone/firmware/Veridian
Actual   :
[%d] %s:%d End  Failed  Error:%d  \n
ProductionMode
set_id
_releaseBMUTags
_createRequestDictForTATSU
%s:%d Successfully stored firmware PLIST. \n
[%d] %s:%d _send_bin failed, commStatus=0x%X, Retry...%d \n
%s:%d CC_SHA256_Init %d\n
_createMeasurementDict fails.
readSMCKey
CFGetTypeID(smc_error_code) == CFNumberGetTypeID()
result == kT200Success || t200UpdaterData->batteryRestoreOptions.internalRestore == FALSE
keyFwPayload!=NULL && keyFwVersion!=NULL
valueDict != NULL
Fail to run AMSupportPlatformCopyURLWithAppendedComponent
T200: Failed to allocate parallel error tracking
rc == 0
%s:%d This hardware configuration doesn't exist in FirmwareMap. \n
plistStr != NULL
BMU,EnableFutureFWVersion
%s:%d Add Entitlements T200TagFAEnableOption\n
num != NULL
T200: Check Update Needed Failed for DNVD Image %d \n
data
Error: Failed to get Firmware data.
BMU,BoardID
converted
fwData!=NULL
%s:%d Start queryInfo for Battery Index: %d \n
[%d] %s:%d DigestMap BC__sendImage failed commStatus=0x%X \n
[%d] %s:%d End
options
_T200UpdaterCopyFirmwareWithLogging
%s:%d OTA = %d, BootedOS = %d \n
<VeridianInternalInfo> \n
psim-present
tagsInTssResponse
%s:%d Sequential battery update failed\n
_entitlementExist
%@.%@.%@.%@.%@.%@
%s:%d Update type kT200UpdateTypeDNVD \n
currentKey != NULL
Digest
%s:%d Number of Active Battery for FW Updater: %d \n
[%d] %s:%d cert len:%u \n
DebugArgs
Cannot allocate BMUTags
No info found for key '%s' (0x%X, 0x%X)\n\n
MACH_PORT_VALID(service)
nonceData != NULL
digestMapDataRef
FirmwareData
version
derDigestData!=NULL
[%d] %s:%d Start  \n
t200UpdaterData->batteryInfo[batIdx].batteryUniqueID == uint32Val
@BMU,Ticket
T200TagMeasurementFirmware
CFArrayCreateMutable
BuildIdentity is NULL in input options
fwPlist
_AMAuthInstallFinalize
T200: Get T200 Info Failed
innerKeyPath != NULL
fwDataRef
\t\t<WDTReset>%u</WDTReset> \n
\t\t<NTCTemperature>%f</NTCTemperature> \n
\t\t<PackVoltage>%f</PackVoltage> \n
<VeridianInternalInfo \n
%@%@; %u
BMU,FirmwareMap
AMSupportCopyFile
status == KERN_SUCCESS
Error: fOptions is NULL.
%s:%d End\n
Options is NULL
%s:%d Error : %s\n
Allocation_size <= SU__SIZE__MAX_IMAGE
Error: mountURL is NULL.
a0p2_node != NULL
rb
UpdateType
digest_der
%s:%d Start  \n
hw_version
CFNumberGetValue((CFNumberRef)bmuIDNumberRef, kCFNumberSInt32Type, &bmuid)
success
%s:%d BMUID 0x%X \n
(kAMSupportErrorNone == status) && (NULL != dstFilePathURL)
t200UpdaterData->batteryInfo[batIdx].productionMode == boolVal
] %d\n
BatFWUpdater: [%d] Error writing image. 0x%X \n
%s:%d Performing Sequential battery updates for %d batteries\n
BatteryIndex
BMU,CertificateEpoch
T200TagBoardId
%s:%d Loading FW map url \n
AMSupportCreateDataFromFileURL
%s:%d Error: CFErrorRef is NULL. \n
T200UpdaterIsTwoStageSupported
%s:%d Restore Options:  \n
T200MeasurementDictFirmware
T200TagMeasurementFirmwarePlist
kT200TagMeasurement
%s:%d End queryInfo for Battery Index: %d \n
_extract_data_map
Error: Plist strip failed.
T200OptionTicketRef
isVeridianUpdateRequired
Error: Failed to get Veridian Info.
[%d] %s:%d cell_ID %d not supported. Error: %d \n
%s:%d item %@ not a dictionary \n
\t\t<OneSecondPassedCharge>%f</OneSecondPassedCharge> \n
BMU,Revision
%s:%d %c%c%c%c rc= %x
T200GetBoardIdFromDT
ret==kT200Success
[%d] %s:%d Success. Valid Firmware Version (%u) found on HW. Skip Retry. \n
\t\t<COMMReset>%u</COMMReset> \n
EnableValidationCommands
%s:%d Updater options is empty\n
queryInfo
[%d] %s:%d Signal Start Update \n
[%d] %s:%d ERROR:Failed Updating the DNVD \n
%s:%d Number of Active Battery: %d \n
deviceInfo && (CFGetTypeID(deviceInfo)==CFDictionaryGetTypeID())
%s:%d derDigestData is missing in Firmwaremap.plist\n
matchingDict
[%d] %s:%d hwVersionstr = %s  \n
%s:%d failed to create current substring \n
dt_board_id == uint32Val
\t\t<SWReset>%u</SWReset> \n
CFGetTypeID(num_enabled_data) == CFDataGetTypeID()
%s:%d Looking for FirmwareData in BundleDataDict\n
BatFWUpdater: Error - cannot open AppleSMC
\t<ServiceType>Read Data</ServiceType> \n
performNextStage
_send_certificate
bmu_id
bmu-num-supported
could not open %s
ChipID
%s:%d Update is required for Battery Idx %d. \n
*board_id
%s:%d Single Battery Restore: %d (Target Battery Index: %d) \n
commStatus == 0
[%d] %s:%d end \n
chem_node != NULL
BMU,DigestMap
T200TagVNVEnable
0x%04x 
BatFWUpdater: [%d] Error committing image. 0x%X \n
com.apple.AppleAccessoryManager
NULL != *firmwareData
\t</ResetCount> \n
derSignature != ((void*)0)
CFGetTypeID(board_id_data) == CFDataGetTypeID()
AMSupportMakeDirectory
firmwareData is NULL
digest != ((void*)0)
Data src is NULL
Failed on BC__commitImage.
t200UpdaterData->batteryInfo[batIdx].targetUpdaterError = %d
DNVD Update Failed with CommStatus = %d
Firmware Update Failed with CommStatus = %d
Failed on BC__sendCert.
Failed on BC__sendImage.
Send out the results in fOutput of the commad processed\n
Config Update Failed with CommStatus = %d
failed to allocate memory
Failed on BC__sendManifest.
Failed on BC__sendDigestMap.
targetUpdaterStatus = %d
```
