# `/usr/lib/updaters/libT200Updater.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 265,872 bytes.

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
Cannot allocate memory for tagsInBI
_createMeasurementDict fails.
isVeridianUpdateRequired
[%d] %s:%d Battery UniqueID is Zero. Use Battery Unique ID from getInfo.\n
ret == 0
hwVersionstr != NULL
,
Missing kT200BuildIdentityPathKey
*error == NULL
%u
[%d] %s:%d failed with result =%d \n
EnableValidationCommands
RestoreInternal
%s:%d This is Tatsu signing ,we are done  \n
[%d] %s:%d Failed with Error:%d  \n
pubKeyPkcs1->data[0] == 0x04
Error: Failed to get HW Version.
/Library/Caches/com.apple.xbs/34FB187E-6E8B-4359-9FD4-26A4FD9EA98C/TemporaryDirectory.84cANW/Sources/VeridianDylibs/T200Updater/T200UpdaterPrivateHelper.c
chemistry
[ 
T200: Check Update Needed Failed for Configuration Image %d \n
[%d] %s:%d Manifest BC__sendImage failed commStatus=0x%X \n
BMU,Request
AMSupportMakeDirectory
%s:%d Restore options is empty\n
ChemistryID
batteryInfo
_T200UpdaterCreate
firmwareMapLen && firmwareMapBuffer
chip_id_data
%@%d
AMSupportPlatformFileURLExists
BatFWUpdater: [%d] BC__sendImage \n
T200: Check Update Needed Failed for Configuration Image
[%d] %s:%d set_id_0=%d set_id_1=%d set_id_2=%d \n
%s:%d Successfully stripped firmware PLIST. \n
%s:%d CC_SHA256_Update %d\n
T200TagEFFV
%s:%d Add Entitlements T200TagFWOverWrite\n
BatFWUpdater: Failed to BC__connect
\t\t<TwoStageSupported>%u</TwoStageSupported> \n
\t\t<BoardID>0x%X</BoardID> \n
%@.%@.%@.%@.%@.%@
%s:%d keyPath is NULL \n
Error: Failed to get chem ID.
queryInfo
[%d] %s:%d End
psim-present
Limited
T200TagRevision
T200OptionTicket
kAMSupportErrorNone == status
T200Updater.c
%s:%d Number of Active Battery for FW Updater: %d \n
fOptions
t200UpdaterData->batteryInfo[batIdx].batteryUniqueID == uint32Val
Info
dataDictRef!=NULL
%s:%d start  \n
%s:%d ChipId from IODT 0x%X \n
bmu_id
BMU2,
%s:%d Skipping update - BoardID or ChipID parameter not present in EDM, battery is dev fused and internal restore \n
T200: Get T200 Info Failed
t200UpdaterData
input
[%d] %s:%d End Send Certificate smc API \n
fileExists
%s
[%d] %s:%d cell_ID %d not supported. Error: %d \n
dnvd
T200TagBoardId
BMU
%@.%@
CommunicationError
Error: kT200OptionOptions is NULL.
1 == boolVal
%s:%d Replacing LF with CRLF before digest computation \n
%s cmd=0x%x amount=%d\n
AMSupportCopyFile
buildIdentity
computeFirmwareDigest
%s:%d derDigestData is missing in Firmwaremap.plist\n
BatFWUpdater: [%d] Error starting update: 0x%X. Retrying... \n
\t\t<Firmware supported SetIds> DNVD1:0x%x  DNVD2:0x%x Config:0x%x </Firmware supported SetIds> \n
_getInfoSMCIF
T200: Program Image(s) Failed
%s:%d Start  \n
[%d] %s:%d End with error %d \n
storeFirmwarePlist
%s:%d Successfully stored firmware PLIST. \n
a0p2_node != NULL
T200OptionTicketRef
_send_diget_map
BMUID
version
BatFWUpdater: [%d] BC__startUpdate \n
%s:%d Start \n
firmwareMapDataMutableDict != NULL
[%d] %s:%d End Send DigestMap+Crypto smc API \n
T200: Check Update Needed Failed for Firmware Image %d
%@; %u
BMU,Revision
PreflightRequired
/usr/standalone/firmware/Veridian
%s:%d Error: CFStringCreateWithFormat failed.\n
_send_manifest
[%d] %s:%d Send dummy Digest Dictionary for Access Mode Enable \n
\t</ResetCount> \n
_T200GetBMUID
DebugArgs
BatFWUpdater: Error - cannot open AppleSMC
\t<BatteryIndex>%d</BatteryIndex> \n
_T200UpdaterExecCommand_block_invoke
%s:%d Number of Active Battery: %d \n
BatteryIndex
T200TagBoardID
\t<ServiceType>Read Data</ServiceType> \n
[%d] %s:%d Skipping Second stage in update \n
userInfo
result == kT200Success
\t\t<Configuration>%u</Configuration> \n
%s:%d OTA = %d, BootedOS = %d \n
com.apple.AppleAccessoryManager
%s:%d Update type kT200UpdateTypeFirmware \n
FirmwareData
%s:%d Start\n
%s:%d Add Entitlements T200TagEFFV\n
%s:%d status=%d
%s:%d start \n
CFGetTypeID(tmpDict) == CFDictionaryGetTypeID()
numUnused == 0
Unable to get kT200TagMeasurementPatch
%s:%d Loading FW map url \n
_createMeasurementDict
T200UpdaterIsTwoStageSupported
success==true
skipPlistStore == FALSE
RestoreOptions
%@%d%@
certData != ((void*)0)
%s:%d PLIST  Img Version= %d  SetID= %d. \n
writeSMCKey
[%d] %s:%d End Send Manifest smc API \n
Options
%s:%d outputDict =\n
AppleGasGaugeUpdate
\t\t<DNVDSector2>%u</DNVDSector2> \n
</AMSResponse> \n
\t<ADCReadings> \n
%s:%d Is Battery DevFused? %d \n
derSignature != ((void*)0)
Missing kT200OptionBuildIdentity
BatFWUpdater: [%d] Error committing image. 0x%X \n
%s:%d Entering execCommand: command = queryInfo \n
_extract_cell_ID_Supported
%@.%@.%@.%@.%@
firmwareMapDataRef!=NULL
%s:%d CC_SHA256_Init %d\n
result == kT200Success || t200UpdaterData->batteryRestoreOptions.internalRestore == FALSE
copyRetrievedFirmwarePlist
_CFDictionarySetInteger32
hw_version
fwPlist
%s:%d Performing Sequential battery updates for %d batteries\n
BundleDataDict
%s:%d End\n
%s:%d Options Dict\n
%s:%d BMUID %d \n
AMSupportCreateDataFromFileURL
%s:%d Cell_iD is Skip \n
Allocation_size <= SU__SIZE__MAX_IMAGE
/usr/standalone/firmware/Veridian/FirmwareMap.plist
tmpNumb && (CFGetTypeID(tmpNumb) == CFNumberGetTypeID())
(kAMSupportErrorNone == status) && (NULL != dstFilePathURL)
PackIndex
%s:%d isBootedOS: %d \n
%s:%d Copy the file %s to  %s\n
manifestDataRef != NULL
\t\t<NTCTemperature>%f</NTCTemperature> \n
[%d] %s:%d ERROR:Failed Updating the Configuration 
_isBatteryDevFused
infoDict
_t200InitUpdater
%s:%d Single battery restore failed\n
%s:%d Updater options is empty\n
%s:%d This hardware configuration doesn't exist in FirmwareMap. \n
Error: firmwareURL doesn't exist.
T200MeasurementDictFirmware
options
%s:%d Override is set \n
%s:%d Is Two Stage Supported: %d. \n
Cannot allocate memory for updater
T200: Invalid Updater Data
_commitImageSMCIF
copyStrippedFirmwarePlist
T200TagMeasurementFirmware
_releaseBMUTags
\t<CommunicationStatus>%d</CommunicationStatus> \n
deviceIDRef != NULL
data != ((void*)0)
BMU,BoardID
Path
keyPath != NULL
valid == 1
Expected :
Fail to run AMSupportPlatformCopyURLWithAppendedComponent
CreateFileData: AMSupportPlatformFileURLExists returned FALSE
firmwareData is NULL
Cannot get DeviceInfo
ret == kT200Success
%s:%d item %@ not a dictionary \n
 [Battery %d]
DestBundlePath
filePathURL
%s:%d Loading FW from %s\n
BC__receive
\t\t<UpdaterStatus>%d</UpdaterStatus> \n
batModelIDs
%s:%d Disable Parallel Update: %d \n
[%d] %s:%d Battery UniqueID: %u \n
BMU,EnableValidationCommands
ResponseTags
%s:%d Looking for FirmwareData in BundleDataDict\n
[%d] %s:%d hwVersionstr = %s  \n
restoreOptions
t200UpdaterData->fInput != NULL
_send_certificate
%s:%d Busy loop end with status %d \n
ProductionMode
CFGetTypeID(smc_error_code) == CFNumberGetTypeID()
%s:%d Failed getting info try %d \n
[%d] %s:%d Success. Valid Configuration Version (%u) found on HW. Skip Retry. \n
[%d] %s:%d start Send Binary Image to Update DNVD SMC API, update %d \n
[%d] %s:%d Failed to commitImage with status %d \n
_T200GetChipIdFromDT
_T200GetNumSupportedBMUFromDT
FirmwareIsOverride
T200TagResponseFirmwareTicket
%s:%d Error : %s\n
BatFWUpdater: [%d] Error starting update: 0x%X \n
restoreSystemPartition
T200: Invalid Updater Data 
dt_board_id == uint32Val
plistMutableStr != NULL
CertificationURL
%s:%d data captured =%d\n
performNextStage
_waitTillTargetUpdaterNotBusy_SMCAPI
\t\t<HWReset>%u</HWReset> \n
\t\t<COMMReset>%u</COMMReset> \n
_T200GetNumActiveBattery
cfErrMsg
ChipID
deviceInfo && (CFGetTypeID(deviceInfo)==CFDictionaryGetTypeID())
requestDict
\t\t<Crypto>%u</Crypto> \n
\t\t<DeviceType>%d</DeviceType> \n
_T200UpdaterExecCommand
_T200GetPSimFromDT
\t\t<SetIds> DNVD1:0x%x  DNVD2:0x%x Config:0x%x </SetIds> \n
product_node
%s:%d Rollback FW Version: %d \n
Error: Write PLIST is failed.
[%d] %s:%d Success. Valid DNVD2 Version (%u) found on HW. Skip Retry. \n
CFGetTypeID(chip_id_data) == CFDataGetTypeID()
%@%@
*batModelIDs
chipIDRef != NULL
<VeridianInternalInfo> \n
<VersionInformation \n
%s:%d Performing single battery restore for Battery Index: %d\n
BatFWUpdater: GasGauge Registry Value %d \n
v16@?0Q8
_check_update_needed
%02X
[%d] %s:%d start Send Binary Image to Update Firmware SMC API, update %d \n
\t<UpdaterStatus>%u</UpdaterStatus> \n
UniqueID
Unable to get kT200TagResponseFirmwareTicket
batteryErrors && batteryResults
[%d] %s:%d Start \n
firmwareMapDataRef != NULL
[%d] %s:%d ERROR:Failed Updating the Configuration \n
\t\t<ResetReason>%u</ResetReason> \n
ActiveBMUs
_updateBMUTags
fwDataRef
%@
] %d\n
%s:%d Error: CFErrorRef is NULL. \n
%s:%d End \n
[%d] %s:%d cert len:%u \n
Fail get the file path 
%s:%d End. Return: %d \n
T200OptionRequest
matchingDict
fw_map_digest
numBatteryCount
[%d] %s:%d DigestMap BC__sendImage failed commStatus=0x%X \n
certDataLength != 0
firmwareMapPropertyLength == T200_UPDATER__FIRMWARE_HASH_SIZE
[%d] %s:%d _send_bin failed, commStatus=0x%X, Retry...%d \n
%s:%d Defaults Node present \n
apiNameRef
DeviceInfo
subDeviceInfo && (CFGetTypeID(subDeviceInfo)==CFDictionaryGetTypeID())
deviceInfo
%s:%d Error: Failed to performVersionCheck for DNVD for Battery Idx: %d. \n
[%d] %s:%d In BootedOS, performNextStage is Skipped if isTwoStageSupported is False \n
digestMapPropertyLength == T200_UPDATER__FIRMWARE_HASH_SIZE
[%d] %s:%d start Send Binary Image to Update Configuration SMC API, update %d \n
%@%@; %u
T200Firmware
BMU,
[DICT] %s\n
BatFWUpdater: [%d] BC__getInfo \n
[%d] %s:%d Start performNextStage for Battery Index: %d \n
T200: Get Firmware Image(s) Failed [ChemID: %u]
fDataIn
keyCellIDSkip!=NULL
CreateFileData: Fail to run AMSupportCreateDataFromFileURL
\t\t<DeviceId>%d</DeviceId> \n
board_id_data
firmwareVersionRef && (CFGetTypeID(firmwareVersionRef) == CFNumberGetTypeID() || CFGetTypeID(firmwareVersionRef) ==CFStringGetTypeID())
[%d] %s:%d ERROR:Failed Updating the DNVD \n
%s:%d NumSupportedBMU from IODT 0x%X \n
RollbackFWVer
BMU,DigestMap
NULL != firmwareBytes
T200GetBoardIdFromDT
[%d] %s:%d BC__commitImage failed commStatus=0x%X
Cannot allocate memory for outputDict
Unable to get BMUID
_T200GetNumEnabledBMUFromDT
%s:%d BMUID 0x%X \n
Missing kT200OptionFirmwareData and kT200OptionBundleDataDict
\t\t<Firmware>%u</Firmware> \n
T200: Commit Image Failed
%s:%d Battery BoardID: 0x%X. \n
t200UpdaterData->fOutput != NULL
_extract_digest_map
t200UpdaterData->batteryInfo[batIdx].chipID == uint32Val
[%d] %s:%d digestmap len:%u \n
bmu2-chip-id
%s:%d fwData is NULL\n
T200TagMeasurementFirmwarePlist
firmwarePlist
%s:%d Device Img Version= %d  SetID= %d. \n
%s:%d psim-present property available \n
cell_id_skip
CFArrayCreateMutable
%s:%d DeviceInfo Dict\n
bmu2-board-id
_create_key_payload_Verison
batteryIndexMsg
tagsInTssResponse
converted
readSMCKey
BatFWUpdater: [%d] Error writing image. 0x%X \n
%s:%d Error: Failed to performVersionCheck for FW for Battery Idx: %d. \n
[%d] %s:%d Does Image updated (0-No 1-Yes)= %d, Veridian Image Loaded: %d set-id:%d    Veridian Image Requested:%d new_set-id:%d \n
RestoreSystemPartition
BMU,UniqueID
BMU,ForceFirmwareUpgrade
BuildIdentityTags
BatFWUpdater: [%d] BC__commitImage \n
<AMSResponse> \n
ret==kT200Success
T200: Check Update Needed Failed for Configuration Image %d
BMU,EnableFutureFWVersion
READ_DATA__getVersionInformation
%s:%d BoardId from IODT 0x%X \n
T200UpdaterPrivateHelper.h
%s:%d dict is NULL \n
Error: Failed to parse Image Version.
Missing kT200BuildIdentityInfoKey
bundleDataDict
nonceData != NULL
T200: Parse Tatsu response Failed
t200UpdaterData->fInput
amerror == kAMSupportErrorNone
IsTwoStageSupported
_createRequestDictForTATSU fails.
BatFWUpdater: [%d] BC__sendImage CRC32: 0x%08X (data_length: %llu bytes)\n
targetUpdaterStatus == SU__STATUS__SUCCESS
CreateFileData: Fail to run AMSupportPlatformCopyURLWithAppendedComponent with dstBundleURL
digestMapDataRef
.
result == 0
fwData!=NULL
Error: mountURL is NULL.
innerKeyPath != NULL
kT200TagMeasurement
%s:%d %c%c%c%c rc= %x
Read failed for key '%s' (0x%X, 0x%X)\n\n
numOfActiveBatteryRef != NULL
%s:%d Restore Options:  \n
%s:%d Successfully retrieved firmware PLIST data. \n
_retrieveSignature
T200TagFWOverWrite
CreateFileData: Fail to run AMSupportMakeDirectory with dstFilePathURL
AppleSMC
t200UpdaterData != NULL
_getFirmware
T200: Check Update Needed Failed for Firmware Image
data
%@%@; %@: %u
measurementDict
%s:%d Add Entitlements T200TagFAEnableOption\n
0x%04x 
IODeviceTree:/product
success == true
t200UpdaterData->fOptions
dataRef && CFGetTypeID(dataRef) == CFDataGetTypeID()
chem_node != NULL
Cannot allocate BMUTags
%s:%d Battery update failed for Battery Index: %d with error: %d\n
config_digest && config_payload && dnvd_digest && dnvd_payload
_getBatteryBoardID
%s:%d NumEnabledBMU from IODT 0x%X \n
HWVersion
configuration
T200TagCertificateEpoch
BatteryIndexInfo is NULL
%s:%d Error: Failed to retrieve Firmware PLIST. \n
\t\t<CellIDs> DNVD1:%u  DNVD2:%u Config:%u </CellIDs> \n
_AMAuthInstallFinalize
%s:%d Error: CFStringCreateWithFormat failed. \n
FirmwareData is NULL in input options
[%d] %s:%d Skipping update \n
%s:%d failed to create key substring \n
%s:%d Failed %d \n
T200: Check Update Needed Failed for DNVD Image %d \n
BatteryModelID
totalErrMsg
T200TagDerFirmwarePlist
%s:%d Force Firmware Upgrade: %d \n
%s:%d Single Battery Restore: %d (Target Battery Index: %d) \n
Error: fOptions is NULL.
[%d] %s:%d Entitlment update successful  \n
BatFWUpdater: Select GG %d for side channel communication\n
T200UpdaterIsDone
%s:%d Internal Restore: %d \n
firmwareDictRef && CFGetTypeID(firmwareDictRef) == CFDictionaryGetTypeID()
%@.%@.%@
[%d] %s:%d End Send Binary Image %d  \n
[%d] %s:%d commitImage status  %d \n
bmu-num-enabled
firmwareDataRef
[%d] %s:%d Update status:dnvd:%d conf:%d firmware:%d \n
%s:%d Update type kT200UpdateTypeConfiguration \n
outputDict
BatFWUpdater: [%d] Failed to BC__GasGauge_connect \n
%s:%d FW Override: %d \n
ForceFirmwareUpgrade
manifestLen && manifestBuffer
[%d] %s:%d manifest len:%u \n
\t<TimeStamp>0x%x</TimeStamp> \n
\t\t<Current>%f</Current> \n
%s:%d Update is required for Battery Idx %d. \n
%s:%d Failed getting info %d  \n
%s:%d CFErrorRef is null
AMSupportWriteDictionarytoFileURL
IODeviceTree:/defaults
BMU,CertificateEpoch
T200TagVNVEnable
imageDict
restore_options
battery-state
T200GetBatteryModelIDs
%s:%d end \n
%s:%d %s \n
%s:%d Start file_name=%s \n
%s:%d Failed with %d\n
\n
%s:%d isOTA: %d \n
%s:%d failed to create current substring \n
signature != ((void*)0)
_send_bin_retry
[%d] %s:%d BC__sendImage failed commStatus=0x%X \n
T200TagProductionMode
0x%02x 
BC__transmit
BatFWUpdater: [%d] Error getting info: 0x%X. Retrying... \n
MACH_PORT_VALID(service)
\t\t<Firmware> maj=%d med=%d min=%d rev=%d</Firmware> \n
%s:%d Parallel battery update failed\n
fwPlistDictRef && CFGetTypeID(fwPlistDictRef) == CFDictionaryGetTypeID()
derstat == 0 
success
\t</ADCReadings> \n
bmu-num-supported
BMU,ChipID
BMU,EnableDeveloperCommands
BuildIdentity is NULL in input options
%s:%d fOptions is NULL \n
%s:%d FA/VNV Entitlement Exist. \n
%s:%d Error: Failed to performVersionCheck for Config for Battery Idx: %d. \n
Error: Plist strip failed.
err == 0
AssertMacros: %s, %s file: %s, line: %d, value: %lld\n
Write failed for key '%s' (0x%X, 0x%X)\n\n
num != NULL
*board_id
%s:%d Error: CFPropertyListCreateWithData failed. \n
[%d] %s:%d ERROR:Failed Updating the DNVD 
BMU,FirmwareMap
_T200UpdaterGetTagsWithLogging
tmpData && (CFGetTypeID(tmpData) == CFDataGetTypeID())
%s:%d update required for Battery Idx %d? DNVD: %d, Config: %d, Firmware: %d. \n
%s:%d Error: T200CreateDictionaryRemovingKeyPath failed. \n
performVersionCheck
T200TagFAEnable
%s:%d Skipping update - BoardID mismatch: DT=0x%X, Battery=0x%X, battery is dev fused and internal restore \n
%s:%d Cell_iD is not skip: \n
\t\t<InternalTemperature>%f</InternalTemperature> \n
BMU,ProductionMode
payload
_createRequestDictForTATSU
[%d] %s:%d End performNextStage for Battery Index: %d \n
valueDict != NULL
_parseFWMapDigest
_extract_data_map
T200CreateDictionaryRemovingKeyPath
t200UpdaterData->batteryInfo[batIdx].productionMode == boolVal
%s:%d Removing %s and %s key-value pairs before digest computation \n
imgVerRef && (CFGetTypeID(imgVerRef) == CFNumberGetTypeID() || CFGetTypeID(imgVerRef) ==CFStringGetTypeID())
tmpDict && (CFGetTypeID(tmpDict) == CFDictionaryGetTypeID())
BMU,Nonce
currentKey != NULL
createStrippedConfigDNVD
digest_der
%s:%d Entering execCommand: command = performNextStage \n
[%d] %s:%d Do we need to update(0-No 1-Yes)= %d, current veridian fw: %d set-id:%d    new_firmware:%d new_set-id:%d \n
plistStr != NULL
[%d] %s:%d image len:%u \n
%s:%d requestDict =\n
%s:%d Restore Options\n
T200Updater
 Digest: %s %s \n
UpdaterOptions
PreflightContext
/Library/Caches/com.apple.xbs/34FB187E-6E8B-4359-9FD4-26A4FD9EA98C/TemporaryDirectory.84cANW/Sources/VeridianDylibs/T200RestoreInfo/T200RestoreInfo.c
_T200UpdaterCopyFirmwareWithLogging
CreateFileData: Fail to run AMSupportCopyFile with dstFilePathURL
tmpBool && (CFGetTypeID(tmpBool) == CFBooleanGetTypeID())
TRUE == boolVal
[%d] %s:%d Certificate BC__sendImage failed commStatus=0x%X \n
Revision
DeferredCommit
No info found for key '%s' (0x%X, 0x%X)\n\n
BatFWUpdater: cannot open gas gauge device 
_parseTatsuResponse
keyFwPayload!=NULL && keyFwVersion!=NULL
[%d] %s:%d Start Send Manifest smc API \n
\t\t<Voltage>%f</Voltage> \n
%s:%d firmwareBytes is NULL\n
[DICT] %s \n
[%d] %s:%d End Failed with %d  \n
DisableParallelUpdate
BatFWUpdater: [%d] FW:%u CFG:%u DNVD1:%u DNVD2:%u BL:%u UniqueId:%u Chemistry:%u hwId:0x%08X isTwoStageSupported:%u \n
\t\t<ChemID>%lu</ChemID> \n
[%d] %s:%d End \n
fwStrippedPlist
chip_id
updaterOptions
Error: Failed to get Firmware data.
T200ErrorDomain
%s:%d Sequential battery update failed\n
NULL != *firmwareData
T200: Check Update Needed Failed for Firmware Image %d \n
\t\t<SWReset>%u</SWReset> \n
\t\t<OneSecondPassedCharge>%f</OneSecondPassedCharge> \n
CFGetTypeID(num_supported_data) == CFDataGetTypeID()
rawSignature != ((void*)0)
BatFWRestore: %s
_performBatteryUpdateThread
T200: Check Update Needed Failed for DNVD Image
%s:%d Update type kT200UpdateTypeDNVD \n
</VeridianInternalInfo> \n
BuildIdentity
BundlePath
firmware
\r\n
Error: Failed to get Veridian Info.
[%d] %s:%d start Send Certificate smc API  \n
CFNumberGetValue((CFNumberRef)bmuIDNumberRef, kCFNumberSInt32Type, &bmuid)
%s:%d Single battery restore failed for Battery Index: %d with error: %d\n
[%d] %s:%d Skip Start Update command \n
_programImageSMCIF
[%d] %s:%d start \n
[%d] %s:%d end \n
fwPlistMutableRef
[%d] %s:%d End  Failed  Error:%d  \n
relativePathStr
%s:%d Number of AppleGasGaugeUpdate supported: %d \n
_entitlementExist
CFGetTypeID(num_enabled_data) == CFDataGetTypeID()
PersonalizationOption
BMU,Firmware
%s:%d End queryInfo for Battery Index: %d \n
\t<UpdaterState>%u</UpdaterState> \n
[%d] %s:%d ERROR:Failed Updating the Firmware 
%s:%d Could not find the signature =%d\n
PreflightTickets
Unable to get kT200TagMeasurementFirmwarePlist
__T200UpdaterCreateRequestWithLogging
%s:%d PSimPresent from IODT 0x%X \n
Nonce
EnableDeveloperCommands
%s:%d Battery[%d] ModelID: 0x%X \n
rc == 0
rc==KERN_SUCCESS
%@; %@: %u
SkipSameVersion
T200TagUniqueID
firmwareData
%s:%d Add Entitlements T200TagVNVEnableOption\n
[%d] %s:%d End Crypto \n
[%d] %s:%d Success. Valid Firmware Version (%u) found on HW. Skip Retry. \n
[%d] %s:%d End  Failed  Error:%d 
Cannot allocate memory for tagsInTssResponse
/Library/Caches/com.apple.xbs/34FB187E-6E8B-4359-9FD4-26A4FD9EA98C/TemporaryDirectory.84cANW/Sources/VeridianDylibs/T200Updater/T200Updater.c
[%d] %s:%d Signal Start Update \n
[%d] %s:%d  show fOptions \n
SingleBatteryRestore
a0p2
copyFirmwareData
buildIdentityDict
Fail to do AMSupportPlatformCopyURLWithAppendedComponent
/Library/Caches/com.apple.xbs/34FB187E-6E8B-4359-9FD4-26A4FD9EA98C/TemporaryDirectory.84cANW/Sources/VeridianDylibs/insystem_communication.c
\t<VersionInformation> \n
bmu-board-id
Options is NULL
type != NULL
%s:%d lenDigestData=%d \n
certificate
Actual   :
\t<ResetCount> \n
T200: Check Update Needed Failed for DNVD Image %d
DeviceInfo is NULL
\t</VersionInformation> \n
[%d] %s:%d Veridian Fw  detected maj=%d med=%d min=%d rev=%d \n
found
derDigestData!=NULL
dict != NULL
[%d] %s:%d Failed to send bin with status %d \n
SkipFirmwareMapStore
BMU,Ticket
BootedOS
Error: restoreSystemPartition is NULL.
commStatus == 0
%s:%d Failed getting the kT200OptionOptions \n
T200TagRequestFirmwareTicket
[%d] %s:%d Skip updating as this is not supported cell-id \n
%s:%d Error: fwPlist is NULL. \n
[%d] %s:%d Updater Status (%d) before retry. \n
[%d] %s:%d End Send Binary Image %d  Faild targetUpdaterError=%d \n
<VeridianInternalInfo \n
bmu-chip-id
set_id
%s:%d End,Failed with ret=%d\n
error != NULL
chemID != NULL
[%d] %s:%d ERROR:Failed Updating the Firmware \n
[%d] %s:%d sendbin status  %d \n
\t\t<WDTReset>%u</WDTReset> \n
[%d] %s:%d Start
</VersionInformation> \n
[%d] %s:%d Start  \n
%@.%@.%@.%@
firmwaredataRef && CFGetTypeID(firmwaredataRef) == CFDataGetTypeID()
data_len > 0
rb
BatFWUpdater: [%d] Error getting info: 0x%X \n
status == KERN_SUCCESS
CFGetTypeID(board_id_data) == CFDataGetTypeID()
public_key != ((void*)0)
digest != ((void*)0)
t200UpdaterData->batteryInfo[batIdx].targetUpdaterError == kT200Success
[%d] %s:%d Start Send DigestMap+Crypto smc API \n
CreateDataFromFile
UpdateType
Digest
board_id
T200TagChipID
%s:%d T200 Options Empty \n
_send_bin
T200TagNonce
\t\t<SerialNumber>%u</SerialNumber> \n
\t\t<ModelID>0x%X</ModelID> \n
%s:%d Start queryInfo for Battery Index: %d \n
T200: Failed to allocate parallel error tracking
Error: input is NULL.
mountURL
err == kAMSupportErrorNone
Failed to BC__connect
%s:%d Skipping update - Internal device with battery-state=-1.\n
derstat == DR_Success
\t\t<PackVoltage>%f</PackVoltage> \n
%s:%d Number of Active Battery (%d) exceeds Max Number of Supported Battery (%d). \n
%s:%d CC_SHA256_Final %d\n
options is NULL
AMSupportPlatformCopyURLWithAppendedComponent
BatFWUpdater: [%d] Connect to AppleGasGaugeUpdate PackIndex:%d \n
%s:%d Performing Parallel battery updates for %d batteries\n
\t\t<UPDReset>%u</UPDReset> \n
@BMU,Ticket
LocalSigningID
CFDictionaryCreateMutable
tagsInBIRef
BatFWUpdater: %s
\t\t<DNVDSector1>%u</DNVDSector1> \n
outDict != NULL
could not open %s
Failed on BC__sendDigestMap.
targetUpdaterStatus = %d
Failed on BC__commitImage.
t200UpdaterData->batteryInfo[batIdx].targetUpdaterError = %d
Firmware Update Failed with CommStatus = %d
failed to allocate memory
Failed on BC__sendCert.
Data src is NULL
Failed on BC__sendImage.
Send out the results in fOutput of the commad processed\n
DNVD Update Failed with CommStatus = %d
Config Update Failed with CommStatus = %d
Failed on BC__sendManifest.
```
