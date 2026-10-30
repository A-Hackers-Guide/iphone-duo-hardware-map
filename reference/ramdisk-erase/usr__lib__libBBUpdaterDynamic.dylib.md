# `/usr/lib/libBBUpdaterDynamic.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 3,028,416 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 49 (Size: 4952)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (32)

- `/usr/lib/libBBUpdaterDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libHSFilerDynamic.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/AppleMipcRouter.framework/AppleMipcRouter (compatibility version 1.0.0, current version 0.0.0, weak)`
- `/usr/lib/libMIPCSdk.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libIOACIPC.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libIOACIPCBB.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libBasebandSharedServices.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libarchive.2.dylib (compatibility version 9.0.0, current version 9.2.0)`
- `/usr/lib/libTelephonyCapabilities.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyDebugDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libETLDLOADDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libETLDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libETLEFSDumpDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libETLSAHDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libHDLCDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libReverseProxyDevice.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libTelephonyBasebandDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CFNetwork.framework/CFNetwork (compatibility version 1.0.0, current version 3896.200.61)`
- `/usr/lib/libKTLDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libPCITransport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libARI.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/AppleConvergedFirmwareUpdater.framework/AppleConvergedFirmwareUpdater (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (5,781)

First 2,500 of 5,781.
```
createImage_SystemBundle
BBUEUR25Initializer
 in the first stage.
InitPersoDeviceBlob.bin
%s::%s: Length of data contained within the chunk: %u bytes\n
%s::%s: ======== ENTERING FIRST BOOT STAGE (ROM) ========\n
Loaded UEFI\n
Assertion failure ( buf->size )
BBUFSServer failed to start filer read session (%llu)\n
%s::%s: [Boot Logger PCIE] Stopping PL/LK log\n
result  0x%x \n
BBUFSServer
processNVRAMItems
%s::%s: Could not create the FDR file path string\n
Bad ELF format
%s::%s: invalid magic number 0x%x\n
%s::%s: Baseband ECID data conversion failed\n
%s::%s: -------- QUERY (Step %d - %s) --------\n
logManifestStatus
%s::%s: Warning: unable to retrieve baseband chip revision (error code = %d), so skipping chip-revision/firmware-recipe check\n
preflightGetBoardParameters
PSI-Running mode 0x%x (%s)
Assertion failure ( tmp && \"Failed to create dictionary for updating provisioning parameters.\" )
%s::%s: invalid provisioning manifest status after pushing provisioning manifest (0x%x)\n
%s::%s: failed to write DALE_PL_CMD_RECV_BB_CAPABILITES\n
Unable to locate file from directory listing '%s'.
updateSource
BBUEUR25UpdateSource::saveImages\n
copyProvKeyHashSinope
Failed to create fusing dictionary from plist
handleProvisioning
MEID is valid. Populating provisioning params!
%s::%s: Merged NVRAM {key, value} pairs:\n
prepareDestination
AMFDRSealingMapRecoverCurrentDevice
*
AMFDRSetOption
bootcmd
Received hash response, %d entries
iboot
%s::%s: Mismatch - expected boot stage: %u, current boot stage: %u\n
   Detected as unfused BB
Fail to bootup in manifest check: 
%s::%s: getting baseband capabilities...\n
kBBUReturnAPTicketMallocFailed
%s::%s: RootManifest: \n
%s::%s: failed to cold-reset (ACFU error code = %d)\n
v24@?0^{?=III}8r^{KTLCoreDumpListEntry_t=I[32c]}16
Fatal error 3 in FDR data validation/decode
QDSP6SW image missing\n
sendImage_BBCfgHashTable
BundleOverrides
APTicket FileDataSource class init failed...
CopyIdentifier
installTicket
%s::%s: failed to push firwmare (loader stage)\n
AMFDRDataMultiPut
Loaded AOP\n
StageContext::None
Will request provisioning
%s::%s: Let's get a prov manifest\n
: failed to statfs
ETHER_MAC2
sendImage_Nvram
%s::%s: Unexpected baseband ImageTransferSegmentSize option CF type\n
%s::%s: failed to init image object for %s\n
print
bbcfg_hdr.bin
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Communication/ICE/BBUICE16Communication.cpp
Loaded AOPDevCfg\n
%s::%s: copy prov info returned null data\n
%s::%s: NULL data param\n
%s::%s: >>send  power table\n
%s::%s: Transport casting failure\n
ErrorCode from isErrorImageNotFound: 0x%lx\n
Kernel IPC Log
%s::%s: IMEI1: %s\n
%s::%s: Failed to create ACFUDataContainer with zero size CFData\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Provisioning/BBUICEProvisioner.cpp
Boot Logger Transport Unknown
ManifestInfo
generating empty file for %s with size %u
controlFlag
All images transferred\n
Firmware data does not contain programmer\n
%s::%s: arrayCount is 0\n
!GET_RSP_FIELD(rsp, result_t4)
%s::%s: Error: BBUFSServer stop failed\n
verbosity
%s::%s: Missing restore options\n
BbNonce
%s::%s: failed to verify fdr image path\n
%s::%s: image source for %s is not a file (%s)\n
subsystem
airship.io
Assertion failure ( fRootManifestSource == __null )
DR_Success == der_ret
BasebandHttpCommon
profile
%s::%s: failed to send cal image size\n
%s::%s: >>send provisioning manifest image size (%zu)\n
ICEStateMachineSetConfig
saveNewDataToFile
kBBUReturnMultipleDevices
Checking Manifest Request: Length %u Type %u
Not in restore mode - skipping gathering Personalization parameters...
Sec image missing\n
kBBUReturnSWIDMismatchForHW
not connected to programmer\n
invalid path pointer to create directory\n
eUICC ChipID: 0x%llx\n
%i records requested\n
%s::%s: failed to send bbcfg hash-table image\n
boot-command
demote-prod-non-persistent
CAL: Set kAMFDROptionApTicket: %s\n
Command: %s
%s::%s: failed to read status\n
Calibration enabled flag: %d
ECID
trying to find MRC file\n
%s::%s: invalid firmware object\n
Send PSI-RAM (%d bytes)
BB ping return status: %s\n
%s::%s: invalid image size\n
%s::%s: invalid coredump path\n
returning state: %d\n
Cellular2,ProductionMode
RemoteFSRoot
xmissiontimeout
ACDB_HASH
%s::%s: Invalid updater options\n
Failed to read coredump translation table entry instance 
parseAndSaveCrashReason
failed saving data
fakefuse
Registering for NVM updates: opt=%p, ari=%u\n
kBBUReturnInternalError
Assertion failure ( ice16item && \"Error: loading programmer items!\" )
BasebandUpdater:
%s::%s: Ping timeout\n
Fail to getProvisioningStatus
Assertion failure ( fBbcfgImage && \"Failed loading BBCFG image for creating hash.\" )
RegionInfo
BBUFSServerFlushInProgress
kBBUReturnTooManyReperso
Starting Maverick Protocol (%s)
restoreBasebandMigrationDataCmd
Cellular2,HardwareConfigLockOverride
%s::%s: failed to write FLB_MSG_LOAD_BIN_HEADER\n
%s::%s: failed to read ACK for PL_CMD_RECV_EXCEPTION_REASON\n
call with %p different from fTransportCreated(%p)\n
%s::%s: Baseband updater object created successfully\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Support/BBULogging.cpp
Failed to deserialize dictionary %s error %s\n
efs3.bin
%s::%s: BasebandUpdater Version: %s\n
HW Failure
Failed querying chip information
%s: supports flashless %d
Loaded provisioning dictionary\n
%s::%s: failed to verify dynamic image path\n
%s::%s: Failed to prepare bbfs path: %s\n
Retrying ping\n
com.apple.ARITransport
BbGoldCertId
Load PT from iOS\n
%s::%s: Warning: unable to copy recipe from baseband firmware, so skipping chip-revision/firmware-recipe check\n
%s::%s: Could not find begin token 'c40' in bver tag, so skipping FTAB chipID check\n
Failed sending Done ACK packet.\n
%3C
Assertion failure ( success && \"Unable to copy manifest data to finish provisioning.\" )
Resetting baseband .*?
ACIPCInterfaceProviderDevice
Invalid coredump translation table file
%s::%s: CString conversion failure\n
%s::%s: Null lai baseband info\n
Invalid start packet recieved from EBL.\n
feedback
Options.plist
GetNonce
%s::%s: File %s does not exist: returning zero size NVM file %s\n
ping success, PS ready true
Failed performing fusing.
%s::%s: invalid ACK (0x%x) for PL_CMD_SEND_DEVCFG\n
Assertion failure ( false )
Failed NVMSnapshot ARI cmd\n
rsp->Valid()
%s::%s: failed to read baseband capabilities response\n
booted
%s::%s: -------- PERFORM (Step %d - %s) --------\n
%s::%s: ABP kernel interface started\n
BypassMobileAssetRPDownload
Sending PSI enhanced command 'Start MRC Training'
VerifyData
Unknown telephony radio vendor %d
%s::%s: Code:\n\t- m_io_code1: 0x%x\n\t- m_io_code2: 0x%x\n\t- m_status_load: 0x%x\n\t- m_status_verify: 0x%x\n
%s::%s: failed to write to file (%s)\n
dumping %zu records\n
BBTicket malloc for DER decode failed \n
valid
perform eUICC update\n
kBBUBootModeNormal
%s::%s: failed to get image data (offset: %zu, size: %zu)\n
forceMain     
%s::%s: ping check not supported on this device\n
/usr/lib/libMobileGestalt.dylib
Parsing crash reason...
Still persod after force?\n
Assertion failure ( loadBINFiles() && \"Error: Failed to load the BIN image!\" )
%s::%s: bver tag not found in FTAB\n
%s::%s: Current baseband provisioning status: %s\n
%s::%s: IMEI2:%s\n
%s::%s: failed to write PL_CMD_SEND_CAL_IMG\n
%s::%s: >>send bbcfg hash-table data size: %zu\n
Failed to assign output data\n
Cellular1,FDRAllowUnsealed
%s::%s: >>send PL_CMD_RECV_BOOT_MODE\n
BBUFSServerStart
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Protocol/Common/BBUFusing.cpp
Main FW supports %s?\n
%s::%s: failed to read value for boot mode\n
record %u: preference 0x%0x, base 0x%0x, length 0x%0x, description: '%s', filename '%s'\n
kBBUReturnEOF
%s::%s: Failed to create data from NVM file %s\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Images/Eureka/MultiImage/BBUEURMIImage.cpp
%s::%s: m_status_load status error: 0x%x\n
%s::%s: failed to initialize controller object\n
autoboot
collectCoredump_block_invoke
ELF STOR OPEN
Booted for coredump, not programming firmware
BBUpdaterCommon
%s::%s: Failed to create ACIPC interface matching dictionary\n
Assertion failure ( stateRef && \"Failed to create state reference for fusing manifest info.\" )
Loaded SequencerRam\n
received unexpected command: %s\n
RootManifest decode error during FDR data parsing\n
%s::%s: User requested not to cold reset, skipping...\n
%s::%s: encodedBuffer is NULL\n
%s::%s: copy prov info returned error\n
%s::%s: m_io_code1 status error: 0x%x\n
%s::%s: Could not extract no timeout setting\n
CertificationPublicKey
file not found after creating %s\n
%s::%s: Image transfer timeout on iBoot firmware boot stage, aborting via force warm reset\n
ChipID
%s::%s: Failed to set IMEI SVN to %d\n
%s::%s: flush logs completion returned error (error [0x%x])\n
Cellular1,LLB
kBBUReturnTUTransportError
%s::%s: User OR Sticky NVRAM {key, value} pairs:\n
+
%s::%s: Could not create RTKitFirmware with passed in FTAB path\n
%s::%s: ignoring found value as it is a locally-administered MAC address\n
invalid
%lx+%lx
FDR TrustError: %llu\n
PT
this->reverseProxySettings
%s::%s: Baseband NVRAM parsing failed for default nvram list (%d)\n
sys-bundle.img
%s::%s: unexpected response (%s) to oem memory dump\n
validateBootStage
%s::%s: value: 0x%x, boot-mode-value: %u (%s), crash-reason: (%hhu) %s\n
this->serverSessionID && CFStringGetLength( this->serverSessionID.get() ) != 0
%s::%s: failed to add entitlements to the output dictionary\n
%s::%s: failed to get coredump save directory in str format\n
%s::%s: invalid (missing) image source for %s\n
Failed to receive EBL packet.\n
%s
created dummy MDMDDR\n
RGN
%s::%s: >>send PL_CMD_RECV_DDR\n
sBBUFSServerSetConfig function not initialized\n
%s::%s: Certification can only happen in restoreOS\n
DaleController_ExceptionDump
ProvisioningManifestExists
%s::%s: <<rcv boot-mode value\n
%s::%s: >>send PL_CMD_SEND_CAL_IMG\n
%s::%s: failed to create BasebandCoredump object\n
Assertion failure ( status->fNumber && \"Failed to create key status.\" )
%s:  searching in FDR\n
createImage_DDR
Failed to send CoredumpSupported property to AppleBaseband Driver\n
%s::%s: Dictionary allocation failed\n
%s::%s: failed to send power table data size\n
Failed parsing EBL Done packet.\n
Assertion failure ( fDataSource )
CAL: Set kAMFDROptionCopyAllowUnsealed: %s\n
copyBasebandMigrationData
no
j <= req.apdu_payload.apdu_data_size
Failed gathering personalization parameters @ second stage: 
STATUS
%s::%s: Received Response Data: %s\n
failed handling command mode\n
%s::%s: empty queue\n
%s::%s: Baseband NVM Check is %s\n
%s::%s: failed to cold-reset baseband\n
%s::%s: setting TICKET_VERSION failed\n
sbl1.mbn
Assertion failure ( fPSIRamSource == __null )
kBBUReturnInitializerPrepError
none
%s::%s: Failed to crash baseband via SPMI\n
%s::%s: baseband rejected stored ddr data, receiving new ddr data from baseband...\n
off
Loaded download file '%s'\n
MobileAssetRPPath
EUICCMainNonce
Shrm image missing\n
unknown state\n
Requested to sync FATP-calibration\n
%s::%s: Failed to create ACFUDataContainer for crash context data: %s\n
Assuming mature provisioning supported.
%s::%s: SCRT data size: %u\n
qdsp6sw_dtbs.elf
/var/wireless/baseband_data/
%s::%s: Sticky NVRAM items: %s\n
Fail to create transport\n
%s::%s: setting RGN failed\n
%s::%s: sending device config...\n
com.apple.telephony.basebandservices.airship
%s::%s: invalid requestDictKeysBuffer array\n
AMFDRDataExport
successfully pushed Install Ticket\n
%s::%s: failed to write DALE_CMD_SEND_PROVISIONING_MANIFEST\n
kBBUReturnELFImageError
bbcfg_prod.bin
Failed to create dictionary for CAL FDR options\n
%s::%s: msg_id mismatch; expected: 0x%x, actual: 0x%x\n
xbl_sc.elf
kBBUBootModeCoreDump
noTimeout
The format specifier contains malformed Unicode characters
%5B
Assertion failure ( fAcdbImage && \"Failed loading ACDB image for creating hash.\" )
%s::%s: Provisioning RGN has wrong type\n
   SNUM: %s / CHIPID: 0x%08x
%s::%s: failed to write PL_CMD_SEND_ROOT_MANIFEST\n
AMFDRSealingMapCopyLocalData returned NULL data \n
Assertion failure ( (amountCopied == amount) && \"Copied data size mismatch: Failed to copy MRC image payload data to buffer\" )
performManifestCheck
Failed to AuthPerso status %d SW1_SW2 0x%x rsp_len %u\n
kBBUReturnARTMismatchedError
Assertion failure ( capabilities::updater::provisioningCommandTimeout().count() <= std::numeric_limits<UInt32>::max() && \"capabilities::updater::provisioningCommandTimeout().count() exceeds maximum allowable value\" )
CAL: Set kAMFDROptionDataDirectory: %s\n
 
success
%s::%s: failed to write PL_CMD_RECV_BOOT_MODE\n
Assertion failure ( status->fNumber && \"Failed to create key status!\" )
copyVinylEidSinope
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Support/BBUError.cpp
Sending Images
%s::%s: ======== COMPLETED IBOOT PREFIRMWARE BOOT STAGE  ========\n
%s::%s: Using %u ms timeout for ping\n
%s::%s: parsing der encoded file to get the version\n
GetWrapKeyServerRequest.plist
Failed to store data status %d SW1_SW2 0x%x\n
baseband reset detected\n
BBUFSServer failed to set config: NULL configName param\n
, length=
resetting modem
NvramItems
%s::%s: <<rcv FLB_MSG_GET_HW_INFO ACK\n
Prov ping status: 
reset message type: %x\n
%s::%s: Enabling provisioning flow to fix incorrect region setup\n
%s::%s: getting board parameters (loader)...\n
Failed to retrieve mature provisioning parameters.
Sending EBL with xor\n
createImage_BBCfgSegment
handleMaverickGetNonce_nl
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Images/ICE/BBUICENVMImage.cpp
Baseband firmware version size is: %u
Install main but no ticket -- back to restored please\n
%s::%s: failed to read ACK for PL_CMD_SEND_DEVCFG\n
%s::%s: invalid protocol\n
Current SVN: %d
AMFDRSealingMapVerifySealing
The argument index should end with a ':' or a '}'
%s::%s: invalid image configuration; source not provided but image is not optional\n
Failed formatting PSI enhanced command to retrieve personalization info\n
failed sending root manifest data\n
pushFirmware_block_invoke
%s::%s: Returned null provisioned info\n
%s::%s: invalid calibration image\n
finished secure mode
Debug Log Buffer
/private/var/wireless/baseband_data
%s::%s: successfully finished getting crash reason\n
boot-device
rcfgbkpt
%s::%s: Failed to create output dictionary\n
Assertion failure ( amountRead == sizeof( ProgramHeaderTable64 ) && \"Copied data size mismatch: Failed to copy data from program header table.\" )
not found
%s::%s: ======== ENTERING IBOOT PREFIRMWARE BOOT STAGE ========\n
Requested to sync static + dynamic\n
0B
Assertion failure ( fImage && \"Failed to to create BBU Image for the programmer item!\" )
Fail to get update source for fuse
Failed connecting to programmer while querying information in the second stage.
Overriding with preflight information:
IMEI
%s::%s: failed to read ACK for PL_CMD_RECV_HW_INFO\n
kIOReturnSuccess == ret
%20
DaleCoredump
Sending Erase Response: Length %u Type %u  Erase EFS %u
skip_delegate_registration
Loaded OEMMisc\n
Failed to create BasebandUpdater instance
Failed sending data at offset 0x%08x, chunk %u\n
Failed to delete file backup (%s)\n
bbcl
Assertion failure ( false && \"Unrecognized provisioning support type.\" )
%s::%s: Found the fact ack key hash in restore options\n
FWUpdateQuery
?
Found secure manifest in response: 
%s::%s: failed to create exception dump object\n
kBBUReturnAlreadyStarted
kBBUReturnFailCreateTransportBooted
Sending manifest, size %d
Assertion failure ( chipID->fNumber && \"Failed to create certID.\" )
clearBackupFile
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Protocol/ICE/BBUICE18Programmer.cpp
%s::%s: requestDictKeysBuffer allocation failed\n
CertHash
%s::%s: >>send bundle image\n
failed parsing maverick end\n
ctu::cf::convert_copy( description, errorMsg )
%s::%s: setting COMMAND_CODE failed\n
%s::%s: invalid ACK (0x%x) for PL_CMD_RECV_EXCEPTION_REASON\n
Failed creating coredump directory
%s::%s: For %s, combined FDR data is saved as: %s\n
Sending EBL length packet (%d bytes)
ping-attempts
create
%s::%s: Restoring NV items to OQC defaults\n
system-bundle
Version String: 
title
%s::%s: Not Implemented\n
Baseband ARI engage timeout
Manifest
failed sending mode end packet
Using the APTicket in the FS to create the FDR option
failed to save %s ( %d )
for client\\(
Address
%s::%s: >>send bbcfg segment\n
Assertion failure ( fFusingSource == __null )
Failed to change file (%s) owner: %s\n
%s::%s: Sending manifest, size %d\n
%s::%s: invalid provisioningInfoKeysBuffer array\n
Loaded RestorePSI\n
Failed reading MRC training response
aop.mbn
%s::%s: invalid bbcfg segment image\n
%s::%s: failed to read ACK for DALE_PL_CMD_SEND_BBCFG_SEGMENT\n
zero-padding
force-ctrr-lock
%s::%s: Failed to create baseband controller object\n
error %d status 0x%hhx\n
Failed to create CFDataRef from the buffer
BBUZipFile
' already active
00:00:00:00:00:00
Cellular1,L1CL1S
%s::%s: >>send ddr image size: %zu\n
%s::%s: failed to read status after sending bbcfg segment\n
unexpected command %u
%s::%s: Failed GetNvItemsSetting ARI command\n
done
enabling kernel IPC log for coredump\n
Decode 2nd tag failure with der return: %d, decoded tag: %llu\n
CHIPID=0x%x, SNUM=0x%s, PKHASH=0x%s, CERTID=0x%x\n
%s::%s: Initializing BasebandRestore for preflight\n
coredumpInternal
bbcfg-segment
backupFile
%s::%s: copy prov key hash failed\n
%s::%s: NULL output param\n
/sticky_nvram_items.plist
hwType.Valid()
%s::%s: Image transfer timeout on ROM stage, aborting via force warm reset\n
Main & !Gold?\n
InRecoveryOS: %d\n
%s::%s: BTI stage: failed to obtain FTAB sub-mapping containing up to the end of iBoot\n
Failed to FinalizePersoDevice status %hhu SW1 0x%x SW2 0x%x\n
shrm.elf
%s::%s: verify ddr data status: 0x%x\n
Assertion failure ( d.get() && \"Error: Unable retrieve public key to finish provisioning.\" )
failed reading backup directory\n
SIM still initializing, trying again... sim_state 0x%x (retryCount: %d, retryLimit: %d)\n
MRC file %s is too large (%lu), ignoring\n
kBBUReturnGetSerialNumberFailure
modem %s reset
cmdCopyRequirePartitionMount
%s::%s: Missing prov manifest.\n
%s::%s: Failed populating the request dictionary for ProvisioningPing cmd\n
BoardId
backup/
%s::%s: CFDataCopy failure\n
kBBUReturnInvalidBBUStageError
Disconnecting
Cellular2,iBSS
KERN_SUCCESS == kr
%s::%s: Opening ACIPC interface\n
rom
%s::%s: escapedValue == NULL\n
DaleBooter
safe-timer
createDirectoryWithTimestamp
Loaded restoreSBL1\n
Wrote %u bytes to %s\n
com.apple.DaleBootLogger.queue
FTAB ChipID {:x} does not match actual ChipID {:x}. Please restore with an FTAB that matches your baseband chipset.
recv
Failed to restore NV items to state: %d
%s::%s: failed to send loader\n
%s::%s: Failed SysGetInfoV2 ARI command\n
setPreflightMode
%s::%s: Failed to open ARI interface (is baseband booted and ready?)\n
Cellular1,CdpAscDl
resetting modem... may take several seconds for safe reset
v20@?0Q8i16
MEID
OEMMisc image missing\n
Cpucp image missing\n
%s::%s: failed to write DALE_PL_CMD_SEND_POWER_TABLE\n
%s::%s: failed to write PL_CMD_RECV_READ_PUBK_HASH\n
%s::%s: Manifest status: \n\t\t\t  status             : %u\n \t\t\t  provision_status   : %u\n \t\t\t  fatp_cal_status    : %u\n \t\t\t  calibration_status : %u\n \t\t\t  nvm_status         : %u\n \t\t\t  skey_hash length   : %u\n
saveNVRAMFile
Fail to start kernelControl\n
%s::%s: Transport object instance missing\n
<BasebandUpdater %p [%p]>{}
%s::%s: failed to load image from data for %s\n
\n
Failed to get Instructions as CFArrayRef type
filesystem flush operation failed -- check ARI and BB state --
Assertion failure ( fRestorePSIRam2Source == __null )
BBUFSServer failed to backup file (%s)\n
ARI_CLI_ERR - All transaction IDs exhausted for msg\\(.*\\), for client\\(0[xX][0-9a-fA-F]+\\)
marp
failed receiving debug table\n
stopLogging_block_invoke
Assertion failure ( fProgrammer && \"Null programmer?\" )
99:99:99:99:99:99
failed creating ETL header and ring buffer structures\n
%s::%s: Retrieved IMEI SV of %d from the restore options\n
An argument index may not have a negative value
Cellular2,BbFactoryDebugEnable
Assertion failure ( (ret == kBBUReturnSuccess) && \"Failed to copy image payload data to buffer!\" )
%s::%s: Baseband boot failed\n
%s Hash mismatch\n
liveBootGetBoardParameters
LSB
stateProvisionStart
kBBUReturnNoMemory
%s::%s: -------- PING --------\n
The argument index value is too large for the number of arguments supplied
Failed to receive Start packet from EBL.\n
Detect as fused BB\n
second sysctl() failed with err = %d
%s::%s: Collected Sik Data Blob: \n
Waiting %llu milliseconds before first ping
Key alignment is required
multi_image_qti.mbn
%s::%s: null input firmware\n
inData
SyncFile
Assertion failure ( fProvisioningPublicKeySource == __null )
pt
copyResponse
%s%s\n
%s::%s: NULL BasebandUpdater object\n
CarrierID
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Personalization/Common/BBUPersonalizationParameters.cpp
supports legacy eUICC update? %d\n
Main version strings mismatched: Card %s Bundle %s
ping
%s::%s: %s: %u\n
{
Skip because the region type(%s:0x%08X) is in the deny list\n
%s::%s: Failed to get the ACIPC interface object\n
Assertion failure ( fConnected && \"Cannot finish disconnection, since BBU programmer is already (falsely) recognized as disconnected!\" )
Coredump GPIO signalled
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Provisioning/BBUProvisioner.cpp
Dump: %s\n
%s::%s: Failed CsiSecCollectScrtBlob ARI command\n
%s::%s: check status info for FLB_MSG_BIN_BODY_STATUS failed\n
processDDR
%s::%s: >>send DALE_PL_CMD_SEND_BBCFG_HASH_TABLE\n
Assertion failure ( nullptr == fTransportCreated && \"Telephony transport error.\" )
createImage_PowerTableMobileAsset
inRestoreOS: %d\n
Failed fusing check.
DE:AD:BE:FF:00:00
DaleFirmware_Coredump
DataDirectory
Path %s -> Mac %s\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Protocol/Common/BBULoader.cpp
EFS file verify status: %d
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Updater/Common/BBUStages.cpp
a pointer
Assertion failure ( ( sizeof( ProgramHeaderTable32 ) <= fHeader32.e_phentsize ) && \"Program header table size exceeds program header table entry size.\" )
future.get()
%zu -> %s\n
Cold reset
qdsp6sw.mbn
B64_SESS_KEY
failed createing maverick root manifest response\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Updater/Eureka/BBUEURUpdateSource.cpp
BB Init status: not ready\n
SendReceiptServer %d\n
kBBUReturnGetManifestStatusFailed
kBBUReturnFusingSourceError
   Nonce: %s
%s::%s: Skipping gathering of debug info as requested by the client\n
%5E
%s::%s: -------- VERIFY FUSING --------\n
%s::%s: failed to transfer coredump content\n
%s::%s: [Boot Logger] UART created\n
%s::%s: ======== COREDUMP: ENTERING IBOOT PREFIRMWARE BOOT STAGE ========\n
AMFDRDataMultiExport
failed receiving baseband config
Final coredump at %s
%s::%s: failed to allocate buffer\n
Fail to get update source for provision
queryInfo
successfully switched back to Normal\n
%u.%03u: %s: %s
FDR data pull and validation is successful for %s
Start
   NONCE: %s
cal.der
%s::%s: Failed to boot Baseband for manifest check\n
%s::%s: Baseband ChipId is missing.\n
Backing-up file from (%s) to (%s)\n
Failed to match both plist and the fusing data\n
baseband alive detected\n
%s::%s: Successfully set NV items to %s\n
%s::%s: escapedValue is NULL\n
Failed to complete InitPerso command\n
%s::%s: Failed GetCurrentBootState ARI command\n
APPS image missing\n
root manifest hash data mismatches baseband hash query\n
%s::%s: invalid hw info size\n
(ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\(([a-zA-Z]+\\.){0,}|\\) [0-9a-zA-Z]+\\([0-9]+-[0-9a-fA-F]+\\) SZ\\([0-9]+\\) TRX\\(0x[0-9a-f]+\\) AP\\.SEQ\\(0x[0-9a-f]+\\).*)
Stripping and verifying Cal FDR Data on AP\n
%s::%s: BTI stage: 4K-aligned total sub-mapping size: %zu\n
kBBUReturnEBLImageError
%s::%s: failed to verify fastboot status\n
initACFULog
%s::%s: failed to write DALE_PL_CMD_SEND_BBCFG_HASH_TABLE\n
@
AMFDRSealedDataCreate
Fail to ping baseband: 
safe-timer.
failed creating directory\n
goldFirmware
VinylClearMetadata::GetListOfIccids: Requesting Profile List\n
%s::%s: failed to create power table image\n
%s::%s: encodedValue is NULL\n
SBL1_HASH
failed reading file: return code = %d\n
shouldBypassNVMSync
failed creating backup directory\n
request image ID %u, data offset 0x%x, data length %u\n
%s::%s: UART is only applicable for restore environment\n
boot-uart.log
Checking against process %s\n
kBBUNVRestoreSettingFATP
SNUM
Image Size: %u, Code Size: %u\n
   ChipSerialNo: %s
%s::%s: >>send PL_CMD_RECV_HW_INFO\n
\\.([0-9]{8})
failure
Loaded DEVCFG\n
%s::%s: Unexpected bbutil cmd setting type\n
exp_reg
LOG BEGIN: ******* %s *******\n
%s::%s: Failed to initialize update operations\n
Invalid directory path\n
BBULoaderVersion
Buffer too small (%zu) for file (%u)
%s::%s: BTI stage: iBoot offset: %d\n
%40
Cellular1,RTKitOS
Pass Fusing Secure State: (0x%08X)\n
%s::%s: Setting kProvB64_BB_CHIPID failed\n
sGetRecords
Receiving baseband config...
%s::%s: Failed to get reverse proxy settings\n
provisionBaseband
Stripping and verifying Pac FDR Data on AP\n
BasebandProvisioning
%s::%s: <<rcv device config status\n
EFS
%s::%s: Failed to create debug log path override object\n
locale-specific form
NULL BasebandUpdater object
(none)
%s::%s: Failed to get PRP\n
checkStatusInfo
%s::%s: AMSupportHexAsciiToNumeric failed to parse address.\n
m9kefs1
DR_Success == der_ret && TAG_PILR_OK == dec.tag
%s::%s: Manifest Check Status: %s\n
%s::%s: No user defined NVRAM items. So, use default NVRAM items for restore.\n
%s::%s: Path %s does not exist, therefore nothing to erase. Continuing\n
transfer
B64_IMEI
status is %s\n
%s::%s: tmpStringBuffer allocation failure\n
%s::%s: null input value\n
Region Type (%s): Address (0x%08X), LSB (0x%08X), MSB (0x%08X): PASSED!\n
%s::%s: The IMEI SVN is invalid\n
%s::%s: >>send GFH header\n
bbpv
%s::%s: failed to send bbcfg segment data\n
%s::%s: Could not create BasebandUpdaterTransport\n
decodeBase64
BBUFSServer failed to perform snapshot: sTransferFile failed\n
Failed parsing image end command
%s::%s: Bypassing NVM files download: returning zero size NVM file %s\n
VinylSkipAll
%s: Resetting modem
%s::%s: invalid requestDictValuesBuffer array\n
AMFDRDataLocalCreateFullKey
\\$&
Main FW versions already matching (no forceMain)\n
Cellular2,CdpAscDl
%s::%s: failed to read ACK for START_FLB_LOAD_BL_CODE\n
/usr/standalone/firmware/Baseband/
Not stripping FDR Pac Data on AP\n
Return code for the root manifest CAL/FATP_CAL entitlements check is: %d
ACFUFirmware
%s::%s: Failed to get the baseband FW version\n
%s::%s: loading PT from MobileAsset\n
Not stripping Cal FDR Data on AP\n
Manifest check
AMFDRCopyDisposableKeys
v16@?0I8I12
kBBUReturnFileNotFound
Creating firmware object with path: 
BasebandUpdaterSetOptions
Perform Next Stage
%s%s...%c
%s::%s: failed to write PL_CMD_SEND_DEVCFG\n
No root manifest present\n
getNVRestoreSettingOption
cellular
Boot Logger Transport UART
Fail to powercycle modem after fusing
%s::%s: loader size greater than %d\n
BasebandUpdaterObj
boot-args
%s::%s: Failed to create CFString for interface protocol\n
%s::%s: failed to convert imei to data\n
   PUBLIC_KEY_HASH: %s
BBUFSServer timeout waiting for filer read session (%llu) to end\n
%s::%s: Provisioning ping failed.\n
%s::%s: failed to set key %s in plist\n
Assertion failure ( d.get() && \"Unable to extract public key to start mature provisioning.\" )
Unrecognized radio type!
warmResetForce
Detecting unfused BB and skip restore
%s::%s: Getting current IMEI SVN\n
Timeout on waiting for BB Init status\n
%s::%s: Invalid Baseband FW version size (%d)\n
Cellular1,SecurityMode
%s::%s: pkhash is all zeros\n
Loaded Manifest\n
:
%s::%s: %s image currently not supported. Returning zero size file\n
boot.logger
info.plist
verifyDefaultPath_Fdr
Failed sending MRC training start in Fastboot
Assertion failure ( logBuffer && msg )
%s::%s: send power table status error (0x%x)\n
FinalizePersoDevice %d\n
kBBUReturnNotPermitted
queryCmd
malloc failed for proc list
Exception in BBUpdaterInit: %s
Will provision
Failed to handle post processing request\n
Cellular2,ProvisioningFirmware
Yes :-)
FirmwareVersion
NVRestore setting: %d\n
finish processing event: %s\n
%s::%s: failed to send nvram image size\n
invalid path specified %s\n
no response from baseband when trying to receive next action\n
an integer
(msg\\(|\\), for client)
%s::%s: Failed to get bootNonce (ret: 0x%08x)\n
Failed starting loader.
eUICC is not done yet, waiting\n
 ]
%s::%s: failed to send bbcfg hash-table data size\n
%s::%s: nonce: \n
Sending restore mode cookie in Reserved%lu\n
%s::%s: Unsupported data class.\n
%s::%s: Ping returned failure but did not timeout. Waiting for 500 ms and trying again\n
COMMAND_CODE
%s::%s: IMEI:%s\n
%s::%s: crash rason size: %u\n
==== eUICC Source ====\n
AMFDRSealingMapSetMGCopyAnswer
Loaded XBL Support\n
sUpdateAck
The argument index starts with an invalid character
AuthenticatePersoDeviceRequest.bin
kBBUReturnGetPkHashFailure
Unsupported stage: %d\n
Cellular1,HardwareConfigLockOverride
======================================\n
%s::%s: failed to cold-reset baseband (ACFU error code = %d)\n
HASH CMP
%s::%s: invalid ACK (0x%x) for PL_CMD_RECV_FASTBOOT_STATUS\n
PROV: Set kAMFDROptionDataDirectory: %s\n
%s: The LSB of the Plist (0x%08X) is not matched with the LSB of the fusing data from the BB (0x%08X) at the address (0x%08X)\n
cpucp.elf
BasebandProvisioningLineType
failed removing old file, %s, %s\n
%s::%s: NVM file %s not present\n
%s::%s: %s
   ChipID: %u (0x%08x)
%s::%s: Failed to get the baseband transport ImageTransferSegmentSize\n
Finish provision failed, rsp status: 0x%x
Wrong firmware, doesn’t match hardware ID 
PT file (MobileAsset) copied amount is wrong
failed connecting to sahara\n
%s::%s: Default NVRAM items for bbutil: %s\n
MSU based APTicket Raw Path: \"%s\"
allowRetry
%s::%s: BT_MAC2:%s\n
Assertion failure ( !fQuickStepInProgress )
%s::%s: >>send PL_CMD_RECV_EXCEPTION_REASON\n
%s::%s: Failed to initialize BBUCapabilities\n
%s::%s: Failed to create a baseband firmware save path\n
BBUFSServerCreate
failed changing owner of bbfs backup directory:  %s\n
AMFDRCreateLocalPending
%s::%s: failed to write PL_CMD_RECV_EXCEPTION_REASON\n
Loaded NVM file %s\n
oem mrdump
SBL1
!GET_RSP_FIELD(rsp, result_t3)
%s::%s: Baseband already in reset state, no need to crash it\n
#
|
TransferFile
persoStatic   
Assertion failure ( ( amountRead == sizeof( Header32 ) ) && \"Copied data size mismatch: Failed to copy ELF32 header from data source.\" )
UpdateAck
BBUtilCmd
Failed StreamAPDU set %d/%zu, error %d status %hhu sw1 0x%x sw2 0x%x\n
debug-uarts
warmResetSafe
restoreXBLsc
%sBEGIN: %s\n
failed preparing baseband filesystem directory\n
kBBUNVRestoreSettingOQCMagic
no response from baseband after segment transfer\n
Assertion failure ( capabilities::updater::EUICCAttemptCount() <= std::numeric_limits<unsigned>::max() && \"capabilities::updater::EUICCAttemptCount() returns too large a value\" )
Populated request dictionary: 
Collecting core dump...
Record %u: Preference 0x%x, Base 0x%x, Length 0x%x
Assertion failure ( false && \"Invalid BBU provisionin support type.\" )
   CertHash: %s
%s::%s: invalid crash reason buffer\n
failed opening file %s with fd %i errno %d\n
%s::%s: invalid ACK (0x%x) for PL_CMD_RECV_DDR\n
bbufs
Now DERDecode the root manifest to get the calibration enabled flag\n
is not
MigrationData
InitPersoServerResponse.plist
%s::%s: getting board parameters (rom)...\n
authdbg
com.apple.telephony.basebandservices
%s::%s: verify fast-boot status error (0x%x)\n
BBUFSServerSetConfig
Failed to get data from UIM\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Protocol/Common/BBUProgrammer.cpp
hw.model
Failed to pass the secure state: (0x%08X)\n
B64_BB_CHIPID
Unexpected hello disconnect mode\n
%s::%s: Transport obj has not been created. Unable to ping\n
We only have acceptable errors, so we can ignore these errors \n
%s::%s: failed to abort with force-warm-reset, aborting via cold-reset\n
failed to create dump path
BBUpdaterController
dale.transport
Fusing check
Assertion failure ( ( offset < getWritePayloadLength() ) && \"Error: Chunk size is not sufficient to write payload data of the EBL image.\" )
Fail to create transport: 
Image ID: %u, Header version: %u\n
failed
initBBUCapabilities
%s::%s: failed to send power table image\n
MultiImage
DeleteProfile failed, error %d status %hhu sw1 0x%x sw2 0x%x\n
Invalid NVRestore setting provided: %d, changing to NoUpdate settings\n
%s::%s: failed to create crash reason file\n
ret == kBBUReturnSuccess && fOutput
Finish preparing at %s\n
mawi.bin
kBBUReturnFusingError
AMFDRSealingMapCopyLocalData error: %s\n
%s::%s: read logs completion failed (error [0x%x])\n
%s::%s: flush logs completion of size %zu bytes\n
%s::%s: BTI stage: failed to get the iBoot size from the FW\n
Failed creating CFURLRef for %s while restoring baseband migration data
crashContextData
%s::%s: Sticky NVRAM items do not exist\n
%s::%s: Failed to obtain the default personalized FW base path\n
copyDataFromHexString
VinylUse4FF
ELF BAD FILE TYPE
Malloc failed for APTicket content.
Loaded ACDB\n
%s::%s: decodedData is NULL\n
efs1.bin
verifyDefaultPath_Firmware
Failed sending data at offset 0x%x, chunk %u\n
updateIMEISvn
CRASH DUMP File: %s
prepare
percentage
verifyDefaultPath_Dynamic
lpc_reg
calibration
%s::%s: collecting crash reason...\n
Assertion failure ( fProgrammer && \"No valid BBU Programmer!\" )
&
Cellular2,BbProvisioningEnable
01
dbgsoc
error %d status %u sw1_sw2 0x%x\n
%s::%s: Failed to get personalization parameter (ret: %d)\n
%s::%s: copy baseband prov info returned null data\n
%s::%s: invalid bbcfg hash-table image\n
failed parsing hello packet\n
bootscrp
Failed gathering personalization parameters
%s::%s: Result %d code %d raw_error %ld error %s\n\n
Fusing source is not found.\n
%s::%s: >>send PL_CMD_RECV_FASTBOOT_STATUS\n
outData
Failed to create file %s\n
received '%s' error. arg0 = %#llx arg1 = %#llx\n
PerformNVMCheck
kBBUReturnNAKManifest
%s::%s: Invalid APTicket data type.\n
%s::%s: Waiting %u seconds for ACIPC %s interface to start\n
failed reading chipid from booted baseband over KTL
Assertion failure ( fSBLImage && \"Failed loading SBL image for creating hash.\" )
%s::%s: failed to create dynamic nvram image\n
/dev/tty.baseband-boot-logger
    coredump_supported:   %s
ELF HASH SEGMENT
%s::%s: encodedLength is 0\n
dev
%s::%s: failed to save new ddr data to file\n
kBBUReturnDSPImageError
%s::%s: Failed to init logging\n
!!! 
stateDebugMode
on
kBBUReturnDBLImageError
Emergency
bad arguments header = %p, ringBuffer = %p\n
%s::%s: User defined NVRAM items: %s\n
%s::%s: skip sending calibration image\n
%s::%s: NVRAM data creation failed, null nv data\n
Assertion failure ( amountRead == sizeof( ProgramHeaderTable32 ) && \"Copied data size mismatch: Failed to copy data from program header table.\" )
libFDR errors (if any) coming from the API can be ignored
fusing is requested\n
UEFI
,CPU=
failed copying root manifest to buffer\n
performCmd
init_block_invoke
%s::%s: Submitting our request\n
%s::%s: successfully sent nvram image (index: %u)\n
provision
f.header.length <= 5 && f.data.length <= 255
now in %s
DaleFirmware_Boot
%s::%s: Failed to create BasebandUpdater CFRuntime object\n
UniqueChipID
%s::%s: failed to send ddr image size\n
BbProvisioningEnable
%s::%s: Successfully set IMEI SVN to %d\n
Fail to send bootloader !\n
%s::%s: Provisioning PING result: %s\n
%s::%s: %s\n%s\nDebug args: %s\n
Could not load NVRAM? %d\n
%s::%s: send device config status error (0x%x)\n
Failed to register for reset detect
Baseband crashed during ping\n
kBBUReturnRPMImageError
host_taskname
sMergeNVRAMKeyValPairLists
ELF CALLOC HASH TABLE
dmfl:tnp:iuseb:o:
Could not set SVN\n
%s::%s: BTI stage: iBoot size: %d\n
Qupv3Fw image missing\n
Reading file '
%s::%s: pipe context is null in read callback\n
performBootup
Assertion failure ( fOEMMiscImage && \"Failed loading OEMMisc image for creating hash.\" )
invalid SequencerRam image\n
Firmware APDU not within expected bounds : received (header - 5 : %zu data- 255 : %zu\n
%s::%s: Boot logger is gone\n
%s::%s: Successfully collected the Sik pub key from baseband\n
%s::%s: failed to force-warm-reset baseband\n
Failed to get coredump list\n
SequencerRam
1
%s%s...\n
%s::%s: read nonce status error (0x%x)\n
kBBUReturnFailedStartProvisioning
unexpected mode: %s\n
%s::%s: Preparing BBUFSServer with path: %s\n
psiResp.param = %d
FinalizePersoDeviceRequest.bin
TIMEOUT for message MIPC.*?Client=.*?Msg=.*?Trx=.*? 
DataInstance: %s\n
Cert Chain Address: %u, Cert Chain Size: %up\n
Cellular2,BoardID
Restoring NV items to OQC defaults
WARNING: ChipID mismatch (DIAG vs. libTU); using libTU ChipID
Sending PSI enhanced command 'Load and execute EBL'
PL
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Images/Eureka/ELF/BBUEURELFImage.cpp
sTransferFile
%s::%s: fatal error: exception info not present during coredump collection\n
%s::%s: Image transfer timeout on iBoot preFirmware boot stage, aborting via force warm reset\n
failed allocating space for debug table\n
Loaded provisioning manifest\n
failed sending maverick root manifest response\n
The format specifier should consume the input or end with a '}'
output
%s::%s: Failed to create timer\n
BBUEURInitializer
FATPCalibration enabled flag: %s
AMFDRDataDelete
Hello received boot mode:  %s\n
 formatting argument
%s::%s: fatal error: exception type present in cold boot\n
%s::%s: Proxy Available\n
   Detected as unfused BB\n
%s::%s: Send server req returned error for prov ping\n
packetSize = %u; kBufferSize = %u; rootManifestSize = %u
%s::%s: <<rcv FLB_MSG_ACK_BIN_BODY\n
XBLCfg image missing\n
Failed to get sec.elf in CFDataRef type
dumpPCIEState_block_invoke
%s::%s: Successfully gathered personalization parameters\n
%s::%s: Failed to safe warm reset baseband\n
%s::%s: Received unexpected SCRT pubK size: %u bytes\n
%s::%s: send nvram image status error (0x%x)\n
host_line
%s::%s: Baseband coredump report:\n\tCoredump type: %s\n\tFull report:\n%s\n
Failed sending PSI command for Loading EBL\n
Assertion failure ( false && \"Unrecognized BBU programmer item.\" )
MEID: %s
Bypass manifest status check has been specified. Returning success
Cellular1,Recipe
VinylClearMetadata::GetListOfIccids: Extracting Profile List\n
%s::%s: Failed to collect coredump (ACFU error code = %d)\n
_
Fail to perform cmdPerformNextStage
Assertion failure ( success && \"Failed to create certID.\" )
WARNING: Serial number mismatch (DIAG vs. libTU + DIAG); using libTU + DIAG SNUM
stateManifestCheck
Failed to get debug table\n
Stripping and verifying PROV FDR Data on AP\n
fwMacData is wrong type %s\n
fusingState: %d
invalid programmer data size\n
Succeed to enable\n
%s::%s: failed to get baseband capabilities\n
BasebandUpdater unsupported command: 
Proxy Available!\n
force
%s::%s: failed to read status after sending calibration image\n
InitPersoServer %d\n
add log: data %p size %zu\n
Setting reset delay to %u from %u
%s::%s: Failed to handle certification\n
%s::%s: Failed to create plist dictionary for sticky nvram plist file\n
%s::%s: buffer count exceeded kernel limits (param: %u, assigned buffer: %u)\n
;
%s::%s: failed to cast to dale controller object\n
AMFDRSealedDataPopulate
IMEI2
com.apple.telephony.bb
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Feedback/BBUConsoleFeedback.cpp
Root Manifest Source is not NULL
(Baseband got stuck in data context | state: resetting baseband)
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Personalization/Eureka/BBUEURPersonalizationParameters.cpp
??????
Reversed IMEI: 
%7B
AMFDRDataPutForSysCfgKey
mainFW
%s::%s: failed to read pkhash\n
sendServerReq
kBBUReturnAPTicketReadContentFailed
%s::%s: failed to read ACK for DALE_PL_CMD_RECV_BB_CAPABILITES\n
%s::%s: failed to read ACK for PL_CMD_SEND_DDR\n
%s::%s: Baseband ChipId is not in expected data format.\n
%s::%s: Merge default NVRAM items for restore with the above user defined NVRAM items.\n
BasebandUpdater
Cellular1,Nonce
marp.ftab
Assertion failure ( fPSIRam2Source == __null )
%s::%s: UART can only be open in restored environment. If you wish to open UART in OS mode, please open through nanokdp\n
calib.nvm
failed creating hello response\n
%s::%s: Failed to create timer object\n
provisionCmd
%s::%s: Received unexpected bootNonceHash size %u bytes. Expected > 0 and <= %u bytes\n
Running eUICC\n
Failed to load %s (size %s), creating empty file (size %u)
com.apple.AppleBasebandManager.data
%s::%s: >>send power table data size: %zu\n
Set config '%s' to 'infinite'\n
%s::%s: Merge default NVRAM items for bbutil with the above user defined NVRAM items.\n
ccBoot
handleFDRForNonBridgeSetup
Loaded %s (%p)\n
com.apple.EmbeddedSoftwareRestore.eUICC.bootloaderMinorVersion
BBUProgrammer
PCI-EVENT: pci error: 
BasebandUpdaterIsDone
failed handling hash response
Preflight detected
%s::%s: failed to read ACK for BROM_CMD_FLB_GET_EFUSE_PUBLIC\n
Failed to create dictionary\n
createImage_BBTicket
fwMac.size() == kFWMacSize
Loaded QDSP6SW\n
prov.nvm
SWTrap
failed getting nonce\n
/private/var/wireless/Library/Logs/AppleBasebandManager/Boot.scratch
%s::%s: Device is provisioned. Let's send a PING and confirm it is provisioned properly.\n
, failing program\n
Fusing is requested but no fusing program was given yet. 
failed changing owner of bbfs directory:  %s\n
BasebandUpdaterTransport::crashBaseband()
%s::%s: Unsupported sikblobtype: %u\n
%25
EURStateMachineSetConfig
    sbl_sec_version:      0x%04x
%s::%s: invalid image data for %s\n
Copy baseband data to migrate during an erase install
%s::%s: Failed to create coredump file\n
Ignoring ART mismatch
%s::%s: getting boot mode...\n
%s::%s: unexpected core dump reason type\n
Assertion failure ( manifestInfo && \"Failed to create fusing manifest info dictionary.\" )
createTransportNoEvents ret status is %d\n
RegionCode
failed creating done command\n
%s::%s: received status: 0x%016llx\n
Loaded EBL file\n
kBBUReturnLibFDRDynLibNotLinked
%s::%s: Bad bootNonce size %u\n
status 0x%hhx cards_type: %hhu \n
Retry
BasebandHardwareConfigLockOverride
%08X-%@
EUICCFirmwareLoaderVersion
ClassIdentifier bbpc string check: %d
%s::%s: failed to send prov manifest\n
LocalSigningID
Invalid Refurb Option %s
Start provisioning by sending pubkey, size %d
Failed training, failing program
=
Failed to create path %s
BasebandEnableProvisioning
BBUEUR25UpdateSource
Assertion failure ( fwMac.data && \"Corrupt FW in input!\" )
failed reading snum from booted baseband over KTL
StageContext::PersonalizeStageSecond
Failed changing owner of coredump directory:  %s
kBBUReturnFailedSetNVItems
%s::%s: Firmware object instance missing\n
%s::%s: Failed to perform preBoot actions (ACFU error code = %d)\n
fwMacData
restoreBasebandMigrationData
%s::%s: found address (%s): %s\n
RestoreInternal
Failed to get dictionary from the fusing profile array\n
%s::%s: invalid ddr image\n
%s::%s: <<rcv status\n
%s::%s: Mistyped prov key hash\n
%s::%s: [Boot Logger] Unknown stage\n
DaleImage
Failed sending MRC training start in mrcFastboot, bytesSent = %u
invalid arguments transport:  %p, updateSource:  %p
AOPDevCfg image missing\n
%s::%s: failed to decode manifest object (status: %d)\n
BBUFSServer failed to create file (%s) and/or set owner\n
failed handling sahara send hashes command\n
%s::%s: Default NVRAM items for commcenter/basebandd: %s\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/eUICC/Public/eUICCOptions.cpp
ELF READFILE TO STOR
v24@?0^v8r^^{__CFDictionary}16
Assertion failure ( fXBLscImage && \"Failed loading XBLsc image for creating hash.\" )
%s::%s: macAddrKey is NULL\n
Deserialized plist data is not a dictionary: %s\n
failed to set config as one of the args is NULL\n
Baseband
%s::%s: sending bbcfg hash-table image...\n
%s::%s: failed to read status after sending bbcfg hash-table\n
sPrintHelloParameters
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/FirmwareVersion/Common/BBUFirmwareVersion.cpp
Failed training
%s::%s: failed to write calibration image\n
Loading second stage bootloader
kBBUReturnGetCertIDFailure
eUICC HW present is too old so we will skip updating it\n
kBBUReturnFileMismatch
downloadFusingProgram
%s::%s: %s\n
dbguarts
enable-transport-logs
v24@?0i8^v12I20
getFWVersion
Assertion failure ( ( !fFirmwareFolder.empty() || fZipFile ) && \"Firmware data source error!\" )
%s::%s: Provisioner initialized\n
Assertion failure ( fPhases.size() )
Error: image filter list is empty, cannot save any images!\n
%s::%s: NVRAM sticky_nvram_items.plist read failed with status: (%d)\n
Assertion failure ( false && \"Unrecognized provisoning support type.\" )
com.apple.AppleBasebandManager
Failed to get uid and gid information for _wireless:_wireless
Qdsp6SwDtbs
Assertion failure ( fProvisioningManifestSource == __null )
Assertion failure ( (amountCopied == amount) && \"Copied data size mismatch: Failed to copy image payload data to buffer!\" )
SendImage returned %s, amountWritten = %u, status = %u\n
%s::%s: failed to read ACK for PL_CMD_SEND_CAL_IMG\n
Bad arguments:  packet = %p\n
Assertion failure ( dict && \"Failed to create output dictionary for fusing manifest info.\" )
Load PT from MobileAsset\n
%s::%s: failed to write DALE_PL_CMD_SEND_BBCFG_SEGMENT\n
Querying vinyl library for EID
file '%s' not found in item list\n
%s::%s: assigning new buffer of size %zu KB to fetch logs\n
^
xbl_cfg.elf
command packet Length:  %u\n
Sending Hash Response: value %u  success %u
%s::%s: Writing sticky nvram file to %s failed with error %d\n\n
Failed sending EBL binary\n
ctu::cf::create( userInfo, 2 )
APTriggeredCrash
%s::%s: Coredump command success\n
Failed to init logging
com.apple.EmbeddedSoftwareRestore.eUICC.bootloaderVersionsSupported
%s::%s: Waiting for %u ms\n
Assertion failure ( transport && \"TelephonyUtilTransport Error.\" )
Loaded HYP\n
???
sBBUFSServerFlushInProgress function not initialized\n
%s::%s: Null root manifest\n
%s: Start resetting modem
Fuse
100
%s::%s: Failed to get crash reason summary (coredump type is not a sw trap)\n
%s::%s: failed to create coredump timer\n
%s::%s: responseParts is NULL\n
%s::%s: power table image 1 not valid\n
%s::%s: >>send DALE_PL_CMD_SEND_POWER_TABLE\n
map::at:  key not found
reset
%s::%s: unable to determine image size; image not loaded\n
could not locate %s\n
%s::%s: >>send PL_CMD_RECV_READ_PUBK_HASH\n
%s::%s: failed to read ACK for PL_CMD_RECV_READ_PUBK_HASH\n
kBBUReturnAborted
handleRTIClientNVRAMFile
Assertion failure ( fPSIRam2Source && \"Failed to load PSI2.\" )
The numeric value of the format specifier is too large
The root cause of the AMFDR failure is NOT missing bbxx file \n
Couldn't allocate FD for transaction record during coredump! fd %d path %s\n
AMFDRSealingMapCopyLocalDataForClass
%s::%s: send bbcfg segment status error (0x%x)\n
sTransferFile_block_invoke
createNVData
%s::%s: Saving the final NVRAM list file as: %s\n
failed copying root manifest to buffer
ignore-fusing-sec-boot-status
AOPDevCfg
%s::%s: copyResponse failed\n
kBBUReturnSBLImageError
%s::%s: Failed to create file path for sticky nvram plist file\n
Calloc for datadir path failed
%s::%s: Failed to crash baseband via SPMI (with reason)\n
Saving Firmware image [%s] in path [%s]\n
%s::%s: sending bbticket image...\n
response
BasebandFirmware
Assertion failure ( false && \"Invalid radio type: Specified radio does not have a Qdsp6SwDtbs file.\" )
ThreadRadioMacAddressForProvisioning
Failed on reading the file (%s).\n
%s::%s: failed to create modem bundle image\n
delta
AuthInstallProvisioningServerURL
Error: Failed to load or create new MRC data!\n
kBBUReturnFailedSetSVN
kBBUReturnGetEIDFailure
%s::%s: Successfully gathered preflight personalization parameters\n
Unrecognized string %s\n
Cellular1,BoardID
sBBUFSServerFlush function not initialized\n
failed restoring backup file %s\n
%s::%s: Could not create RTKitFirmware with default FTAB path\n
AMFDRDataCopyDigest
Assertion failure ( false && \"Unrecognized BBU stage.\" )
Result %d next state %s allowRetry %d\n
Assertion failure ( success && \"Failed to get the gold loader version from Gold FW.\" )
Failed due to copied size (%d) and original length (%d) is different.
%s::%s: push firmware: loader stage\n
dynamic-nvram
shouldPerformFusingVerification: it didn't go through fusing process before.\n
%s::%s: failed to read device config status\n
Error: Chunk size is not sufficient to write payload data of the image!
Failed reading PSI command response
CoreDump path passed in to BBU is empty, skipping setting the coredump path for caller.
Failed to complete AuthPerso command\n
Assertion failure ( ( offset < getWritePayloadLength() ) && \"Error: Chunk size is not sufficient to write payload data of the ELF image.\" )
%s::%s: boot mode: %s, exctype: 0x%x\n
PSI is not running enhanced mode, unsupported firmware\n
Provision manifest status:%u => state %s(%u), mismatched %u
%s::%s: requestDictValuesBuffer allocation failed\n
Failed to FinalizePerso status %d SW1_SW2 0x%x\n
failed sending snapshot command\n
kBBUReturnBBTicketDERParseErrorForCal
%s::%s: Got NV items settings from the baseband: NVM (%s), EEPROM (%u)\n
postProcess   
%s::%s: moving to next pipe due to null pipe\n
Cellular1,ProductionMode
%s::%s: Setting B64_SESS_KEY failed\n
%s::%s: Setting kProvB64_IMEI2 failed\n
%s::%s: Received the response from server - parse it\n
%qu
%s::%s: ignoring found value as it matches a value known to be used in testing\n
%s::%s: Boot command success\n
gold
IMEI2: %s
::
version compatible:  %u\n
DaleImage_DDR
Failed image download!
%s::%s: Send server req returned error for prov request\n
%s::%s: invalid ACK (0x%x) for PL_CMD_SEND_ROOT_MANIFEST\n
eUICCVinylData cache is valid. Using cached data!\n
INTStateMachineSetConfigDefaults
%s::%s: Found the APTicket key in updater options\n
Cellular2,Nonce
did not find any backup\n
B24@?0^v8Q16
BBUFSServer failed to perform snapshot: unrecognized INT state. This should never happen\n
HSFilerDynamic library is not available for INT case. It should always be\n
%s::%s: Baseband boot failed (ACFU error code = %d)\n
%s::%s: Coredump success\n
bbticket
Assertion failure ( ::memcmp( e_ident, kIdentMagic, sizeof( kIdentMagic ) ) == 0 )
Fail to collect coredump after hitting fatal error: %s
Failed to get manifest status
%s::%s: <<rcv FLB_MSG_ACK_ROOT_PUBK_HASH ACK\n
%s%s%s
Assertion failure ( false && \"Invalid radio type: Specified radio does not have a SignedFirmwareSOCView file.\" )
%s::%s: NULL updater and/or options arguments\n
%s::%s: null input key\n
%s::%s: invalid diagnostics path\n
v28@?0i8^v12^v20
internal buffer is %lu bytes\n
fusingprogram.plist
setPath_Firmware
Restoring NV items to Shipping defaults
%s::%s: Reading oem mrdump command response\n
createIMEIFromString
version number:  %u\n
fail to free transport: %p\n
failed creating image from fdr data\n
efs
ModelNumber
Assertion failure ( ( amountRead == sizeof( SectionHeaderTable32 ) ) && \"Copied data size mismatch: Failed to copy data from section header table.\" )
EBL
%s::%s: successfully written raw crash reason to %s\n
AMFDRGetInfo
Failed to update provisioning parameters
APTicket
)
%s::%s: failed to create bbticket image\n
Failed to create backup directory\n
kBBUReturnKeysNotAligned
%s::%s: NVM sync successful\n
%s::%s: Baseband provisioning status check failed\n
Data Not accepted
%2E
kBBUReturnBBTicketMallocFailed
askToReset
%s::%s: Baseband Update is complete!\n
%s::%s: pipe context is null when trying to schedule read\n
Failed saving %s
failed handling maverick end\n
Assertion failure ( fLongStepInProgress )
%s::%s: defaultsNvramStr has incorrect type, fail.\n
Data accepted
%s::%s: Failed to send SW Trap\n
AMFDRAppendPermissionsString
B64_IMEI2
invalid state machine type %u\n
%s::%s: keyword 'BBFW:' not exist in bver tag\n
destFD >= 0
%s::%s: pci kernel trace started already\n
%s::%s: buffContext is null\n
~~~~ MAX APDU PER SET: %zu  ~~~~\n
Sent bootloader successfully!\n
%s::%s: failed re-assigning new buffer of size %zu KB to fetch logs (error [0x%x])\n
Fail to ping in manifest check: 
ChipSerialNo
kBBUReturnFSMNoTransitionDefined
downloadFusingProgramCmd
>
VersionCheck
failed to set config, unrecognized config name '%s'\n
kBBUReturnMIImageError
AMFDRSealingMapVerifyAndCommitSealedData
mdmddr.mbn
SBL image missing\n
    send_info_ver:        0x%04x
bootdlay
Fail to connect to loader
%s: Finding index (%d) is beyond the capacity in LSB in the fusing data\n
%s::%s: imei tempData is null\n
Cellular1,iBSS
%s::%s: Zero sized input data\n
not performing disconnect as the previous mode was CommandMode\n
Assertion failure ( false && \"Invalid radio type: Specified radio does not have a XBL Support file.\" )
%s::%s: Incorrect type for nvramOutputPath, fail.\n
Cellular1,UID_MODE
INTStateMachineStart
Failed parsing personalization parameters\n
%21
AMFDRDataPut
Fail to get update source for bootup\n
Only applied when debug args is set to pcie
Assertion failure ( false && \"Invalid radio type: Specified radio does not have a AOPDevCfg file.\" )
setPath_Dynamic
Failed to get directory ownership information for _wireless\n
FirmwareLoaderVersion
---------------------%s---------------------\n
Failed writing %u bytes to %s - wrote only %u\n
ELF HASH INIT
kBBUReturnBadManifestStatus
0123456789abcdefghijklmnopqrstuvwxyz
Assertion failure ( fProvisionState.requested && \"Failed to request provision state.\" )
PreflightInfo
kBBUBootModeNone
bbticket.der
failed receiving done response\n
LAI prov info to be returned to PR: 
multi_image.mbn
Apps
%s::%s: VinyleUICCPerformOperation returned %d\n
No
failed sending mode switch command
Calibration enabled flag: %s
AMFDRDataMultiCopy
%s: supports REFS %d
PROV
kBBUReturnIOError
%s::%s: Successfully gathered NerdOS second personalization parameters\n
profile.bin
Fail to prepare at %s with reset %u\n
Is performManFlow?: Bool = %d
%s::%s: failed to read status after reading pkhash\n
%s::%s: failed to init firmware object\n
kBBUReturnGetEIDFailureAdcMismatch
failed reading hash query results\n
runCertification
writeRawCrashReasonToDisk
Fail to create transport %s\n
%s::%s: Only applicable when debug args is set to pcie\n
EUICC but MG has no ChipID?
CFGetTypeID(outPlist.get()) == CFDictionaryGetTypeID()
%s::%s: invalid data size\n
%s::%s: [Boot Logger CIE] Unknown stage\n
%s::%s: Failed to get transport debug info\n
%s::%s: Failed to add NVM file %s to baseband migration data output dict\n
%s::%s: Error: BBUFSServer create failed\n
%s::%s: warm-resetting baseband...\n
BBUpdaterExtremeCreateCommon(): Unable to determine radio vendor\n
Failed to encode ECID\n
chipID:0x%X certID:0x%X\n
IODeviceTree:/options
InitialTuningOK
eUICC::Done( fOptions )
%s::%s: Unable create LAI prov dictionary\n
statePersonalize
%s::%s: m_io_code2 status error: 0x%x\n
Cellular2,CdpHost
GetNonceServerRequest.plist
kBBUReturnSysctlError
%Y-%m-%d-%H-%M-%S
%s::%s: Image external to FTAB provided: %s\n
Assertion failure ( (offset < (getWritePayloadLength() + kBinHeaderSize)) && \"Chunk size is not sufficient to write payload data of the NVM image!\" )
%s::%s: failed to read status after sending power table\n
BBUFSServerStop
acdb
psiResp.result == KTLRPSIEnhancedRspMrcResultInitialTuningOK
RootManifest decode error during CalibEnable FDR data parsing\n
%s::%s: failed to start kernel trace\n
Assertion failure ( ( amountCopied == amount ) && \"Copied data size mismatch: Failed to copy from ELF image!\" )
RestoreOSBuild
Failed to get fusing profile from the plist\n
Invalid path pointer to create coredump directory
ret == kBBUReturnSuccess
Perso
([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})
XBL_CFG
%s::%s: failed to collect sik public key (%d)\n
warmReset
EBL (%s) not found in item list!
ret = %d\n
%s::%s: decode sequence failure with der return: %d, decode tag: %x\n\n
%s::%s: failed to read status after sending bbticket\n
Baseband firmware version
%s::%s: verifying fdr image path... (%s)\n
Failed changing file ownership (%u, %u)\n
%3D
v8@?0
...waiting patiently for reset\n
%s::%s: GFH checksum mismatch; expected: 0x%x, actual: 0x%x\n
/usr/local/lib/libVinylNonUpdater.dylib
Failed NVMSnapshot ARI cmd: result %d\n
ELF HEADER
File    
Response dictionary: 
%s::%s: Prov manifest received from the server\n
sendImage_Calibration
%s::%s: invalid ACK (0x%x) for DALE_CMD_SEND_PROVISIONING_MANIFEST\n
%s::%s: sending bundle image...\n
BypassNVMSync
SN
failed changing file owner:  %s
%s::%s: failed to load image from file for %s\n
[%04u]: %s
NULL requestURL?\n
cardData.Valid()
kBBUReturnGetFirmwareVersionFailed
MRC data size %lu invalid, ignoring existing data
%s::%s: ACIPC start interface timeout\n
%s::%s: Failed to write MMIO:BootFlags register with Preflight\n
Assertion failure ( success && \"Failed to get session key.\" )
%s::%s: failed to read new ddr data size\n
%s::%s: %s hash:\n
GetNonceServer %d\n
%s::%s: failed to create libtu controller\n
AMFDRCopyUnderlyingDictionary
BBUFSServer performed snapshot successfully\n
BasebandUpdaterCreate
Failed to create the directory\n
Powering on modem. It is NOOP if BB is already on\n
%s::%s: Failed to perform NVM sync\n
%s::%s: Wrong type for Enable Prov PR3 option\n
Failed executing secure mode
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Support/BBUCommon.cpp
Assertion failure ( false && \"Unrecognized radio vendor.\" )
\"
IMEI-SVN Check and Update: %d
kBBUReturnPingFailed
sign
AP forced coredump via SPMI - Please analyze reason from AP perspective
uart-boot-logging-boot-stage
%s::%s: invalid crash reason buffer data\n
\n%s\n
%s - Num entries %lu\n
%s::%s: Current IMEI SVN: %d\n
Cellular1,BbFactoryActivationManifestKeyHash
%s::%s: Setting preflight mode\n
%s::%s: Provisioner init() failed\n
setupTimer_sync
NULL updater argument
KERN_SUCCESS == kr && nvramInfo
Not performManifestCheckif ( set kAMFDROptionCopyAllowUnsealed = True\n
%s::%s: ======== ENTERING SECOND BOOT STAGE (iBoot) ========\n
Assertion failure ( !fLongStepInProgress )
Assertion failure ( fRestorePSIRamSource && \"Failed to load RestorePSI.\" )
Integral value outside the range of the char type
SecondaryEthernetMacAddress
failed to set config '%s', invalid config value '%d'\n
%s::%s: NULL updater argument\n
%s::%s: Saving NVRAM binary file as: %s\n
allow-no-imeisv
Ping failed, %u tries left
%s::%s: [PL normal boot] timeout on pl log\n
ProvisioningManifestSupported
Running at state %s\n
-boot-log
%s::%s: Unexpected CC cmd setting type\n
The root cause of the AMFDR failure IS missing bbxx file \n
Preparing at %s with reset requested %u\n
eUICCFirmwareParser
%23
performCoreDump
%s::%s: failed to read nonce size\n
sBBUFSServerStop function not initialized\n
entering %s
/dev/null
Fake Fusing is detected. Bypass the fusing check\n
%s::%s: Null commandCode parameter\n
%s::%s: Missing output bb prov info parameter\n
Determining support
forceGold     
/bbfs/
%s::%s: Received Response Error (if any): %s\n
background
%s::%s: coredump transfer handshake successful; starting transfer...\n
r+b
InstallTicket failed error %d status %hhu sw1 0x%x sw2 0x%x\n
%s::%s: failed to write PL_CMD_RECV_HW_INFO\n
%s::%s: Baseband NVRAM generator failed.\n
-
%s::%s: Invalid boardID\n
%s::%s: Ping success on attempt %zu\n
Load PT image from iOS\n
%s::%s: NVRAM data creation failed with status: (%d)\n
%s::%s: Proxy Aborted? %d\n
%s::%s: failed to send bbcfg hash-table data\n
std::end(bundleVersions) != std::find(bundleVersions.begin(), bundleVersions.end(), cardVersion)
%s::%s: failed to write BROM_CMD_FLB_LOAD_BL\n
Failed to create hello response\n
failed to respond to hello packet\n
efsc.bin
registerWithKernel_sync
AMFDRGetSealingMap
DaleTransport_BootLoader
%s::%s: Could not extract skip coredump setting\n
sPrintKeyValPairs
%s::%s: Sending oem mrdump command\n
%s::%s: BTI stage: NULL FW param. Should never happen\n
AMFDRDataMultiDelete
StageContext::PersonalizeBooted
%s::%s: Successfully changed IMEI SVN from %d to %d\n
Assertion failure ( ( amountRead == sizeof( Header64 ) ) && \"Copied data size mismatch: Failed to copy ELF64 header from data source.\" )
reserved
%s::%s: error: empty fdr image path\n
%s::%s: processing ddr image...\n
%s::%s: decode 1st tag failure with der return: %d, decoded tag: %llu\n\n
Failed to complete ValidatePerso command\n
Fail to get firmware data source\n
Assertion failure ( success && \"Failed to get EID.\" )
%s::%s: failed to send bbticket\n
createFile
%s::%s: Failed to load image on iBoot firmware boot stage\n
kBBUReturnSuccess == ret
Loaded PSI2\n
Assertion failure ( (amountCopied == amount) && \"Copied data size mismatch: Failed to copy binary image payload data to buffer!\" )
PT file (iOS) copied amount is wrong
MLB
loader_version 0x%s key_id 0x%s perso %d\n
%s::%s: Could not extract bbutil cmd setting\n
%s::%s: check status info for FLB_MSG_ACK_HW_INFO failed\n
Failed preparing baseband filesystem directory for copying baseband migration data\n
Restoring NV items to FATP defaults
B64_BB_SNUM
failed parsing sahara hello\n
provisioning-manifest
Error: loading programmer items!
setHttpBase64EncodedValue
Options:\n%s\n
TZ image missing\n
ACDB
%s::%s: Failed to send KTLFinishProvision cmd, rsp status: 0x%x\n
%s::%s: invalid bbticket status after pushing bbticket (0x%x)\n
failed creating reference to fdr\n
%s::%s: failed to create controller object\n
%s::%s: value length is 0\n
SystemRoot
%s::%s: invalid ACK (0x%x) for PL_CMD_RECV_READ_PUBK_HASH\n
The argument index is invalid
Error: Generating Hashmap of items!
BBUpdaterDetermineVendorandPlatform
Verify Fusing
skip_fusing_validation
Loaded APPS\n
%s::%s: Failed to send prov manifest to baseband\n
trying to release invalid file server\n
kBBUReturnInitializeRingBufferError
Failed to create dictionary for PROV FDR options\n
PostProcess
devcfg.mbn
BBUFSServer timeout waiting for file (%s) transfer to complete\n
%s::%s: Did not find corresponding MobileAsset file name for 4cc tag %s\n
Delete All Profiles
collectPreCoredump
Failed to InitPerso status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
DaleCommon
gold-
failed getting record\n
SignedFirmwareSOCView_HASH
%s::%s: <<rcv hash response size: %u\n
%s:  %0.1f%c\n
%s::%s: Failed to create TelephonyBasebandController\n
%s::%s: Null lai prov info\n
coredump
skipAll       
%s::%s: failed to boot baseband (timeout)\n
%3F
sendProvisionPing
generating 0xFF-filled file for %s
w
%s::%s: Failed to get filename for tag: %s\n
Assertion failure ( fOutput )
ret != kBBUReturnSuccess
USB_ETHER_MAC
InitPersoServerRequest.plist
failed closing saved record:  %s\n
%s::%s: Unexpected no timeout setting type\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Images/ICE/BBUICEDownloadImage.cpp
Tag (
full
VinylClearMetadata::ClearMetadataForIccids: Attempted metadata clear for ICCID\n
SHA384 detected\n
 [coredump collected]
error
%s::%s: Baseband boot state: %d\n
Assertion failure ( fPersonalizationParameters )
%s::%s: IMEI data processing failed\n
%s::%s: failed to get IMEIs from baseband\n
%s::%s: Provisioning baseband\n
CAL
EURStateMachinePerformFlush
SyncStaticDynamicCalibration
force warm reset
2
WIFI_MAC
%s::%s: >>send bbcfg hash-table\n
Assertion failure ( ddrDataRef )
%s::%s: ROM object instance/s missing\n
%s::%s: -------- PERFORM FUSING --------\n
DataClass: %s, DataInstance: %s\n
Assertion failure ( (ret == kBBUReturnSuccess) && \"Failed to copy binary image payload data to buffer!\" )
Ret %d from state %s next %s\n
%s::%s: check status info for FLB_MSG_ACK_ROOT_PUBK_HASH failed\n
%s::%s: status info:\n\t- magic:\t0x%x\n\t- ver:\t\t%d\n\t- msg_id:\t0x%x:0x%x\n\t- status:\t0x%x\n
handleCertification
Getting Version
failed to receive reset response\n
Max root packet size from PSI: %u
pingattempts
bbcfg.mbn
kBBUReturnTooManyRetry
%s::%s: FDR file name for %s is: %s\n
The format string contains an invalid escape sequence
Failed to create dictionary for PAC FDR options\n
AuthenticatePersoDeviceResponse.bin
v24@?0^{?=^vQQQ}8r^{ETLSAHDebugDataFieldRecord_t=cII[20c][20c]}16
hit an error while copying data from FDR\n
IMEI-SVN Check and Update...
setNonce
Failed to push images: 
%s::%s: failed to read hw info size\n
GetWrapKeyServerResponse.plist
Running secure mode
ClassIdentifier in error: %s\n
psi_ram.bin
BBUFSServer failed to read file (%s)\n
AMFDRSetRecoveryVerifier
DisallowFusing
%s::%s: failed to open file (%s)\n
%s::%s: failed to get board params\n
Assertion failure ( certID->fNumber && \"Failed to create certID from public key hash.\" )
Manifest status: \n\t\t\t  status             : %u\n \t\t\t  provision_status   : %u\n \t\t\t  fatp_cal_status    : %u\n \t\t\t  calibration_status : %u\n \t\t\t  skey_hash length   : %u
] 
HYP image missing\n
BasebandUpdaterExecCommand
\\
%s::%s: received status: %d\n
%s::%s: using file source for image %s\n
Loaded BBCFG\n
Assertion failure ( fFeedback )
/wireless/Library/Logs/CrashReporter/Baseband/baseband_updater_logs/
%s::%s: >>send bbticket size: %zu\n
ForceSync
sRegister
%s::%s: Failed to handle provisioning\n
%s::%s: RootManifest post_signed_section size: %ld\n
%s::%s: coredump collection: loader stage\n
pingdelay
failed to copy programmer data from data source\n
bbpc string check: %d
%s::%s: collecting coredump...\n
Miss image for collecting coredump
%s::%s: failed to write FLB_MSG_GET_HW_INFO\n
kBBUReturnELFHeaderError
eUICC Source has no FW, ENG?\n
BBUHashData
sendImage_BBTicket
outPlist
preloader.bin
Boot Logger ROM
Failed starting mature provisioning.
%s::%s: firmware directory does not exist (%s)\n
crash_in_crash
airship
%s::%s: Did not find corresponding NVM file name for 4cc tag %s\n
Failed personalizing in second stage 
BypassManifestStatusCheck
failed sending reset command\n
failed to handle kETLSAHGetDDRCalData\n
%s::%s: failed to reverse imei\n
copy_mac_address_existence
%s::%s: >>send ddr image data\n
%s::%s: boot logger transport not exist\n
Requires reprovisioning
Cellular1,BbProvisioningEnable
unknown error %d
%s::%s: poststring creation failed\n
hasManifestSource() = %d, personalize = %d\n
Provision_
kBBUReturnGetChipIDFailure
report.json
%s::%s: Could not extract debug log path timestamp setting\n
BasebandRestore
%s::%s: Failed BBUFSServer prepare after erasing baseband file system\n
EBL (%s) exists, but  is of invalid type!
BBUFSServer releasing registry\n
Boot up
Waiting for PSI command response
failed reading snum and/or chipID from booted baseband over ETL
createProvisionedInfo
%s::%s: CreatePostBodyFromDictionary failed\n
sBBUFSServerStart function not initialized\n
kBBUReturnBBInitStatusTimeout
Assertion failure ( fImage && \"BBU Programmer item creation failed.\" )
DR_Success == der_ret && TAG_PILR == dec.tag
%s::%s: NerdOS second query - simply gather baseband info from ROM without a nonce\n
.
Assertion failure ( fSBLImage == __null )
%s::%s: Using MobileAsset path: %s\n
MRC data too large
%s::%s: WIFI_MAC2:%s\n
Assertion failure ( success && \"Failed to create chipID.\" )
%s::%s: Failed to create imei string ref\n
Hello reserved fields:  %s\n
%s::%s: failed to send nvram image index\n
%s::%s: updaterOptions parameter is NULL\n
%s::%s: failed to read status after sending provisioning manifest\n
Cellular2,ECID
%s::%s: Encountered an error (%d) during NVRAM processing\n
Clear All eSIM Preferences
%s::%s: failed to cast firmware object\n
invalid xbl image\n
r
%s::%s: Setting no-timeout to %d from options\n
%s::%s: Baseband Firmware override has wrong type %lu\n
%s::%s: Total transferred bytes %llu\n
%s::%s: read logs completion of size %zu bytes\n
CMStatusCode
/private/var/wireless/Library/Preferences/com.apple.AppleBasebandManager.Statistics.plist
Setting AMFDR Log Handler\n
%s::%s: boot timeout, aborting via force-warm-reset\n
%s::%s: Failed to create file url for sticky nvram plist file\n
Failed to open file to chown\n
%s::%s: Invalid productionMode\n
Fail to get update source in 
\tCrash reason: File:%s, Line:%d, String:%s
LOG END: ******* %s *******\n
device has no further updates\n
stop
sBBUFSServerSetConfigDefaults function not initialized\n
Assertion failure ( dirPath.empty() != true && \"Failed finding the bbfw path.\" )
%s::%s: failed to create a directory at dynamic image path (%s)\n
uimSlot       
Image Flash Address: %u, Image RAM Address: %u\n
%s::%s: failed to create bootrom object\n
%s::%s: unsupported operation\n
required path length = %zu, copied = %zu, max length = %zu\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Updater/ICE/BBUICE16UpdateSource.cpp
%s::%s: invalid ACK (0x%x) for BROM_CMD_FLB_GET_EFUSE_PUBLIC\n
%s::%s: pre-assigned buffer # %u of size %u KB to fetch logs\n
failed reading PKHash from booted baseband over ETL
restoredInternal
createProvSessionKeySinope
%s::%s: Successfully gathered personalization parameters over ARI\n
%s::%s: Copy identifier command success\n
Assertion failure ( nullptr != fTransportCreated && \"Telephony util transport error.\" )
%s::%s: Failed to sync baseband file system\n
%s::%s: Image external to FTAB provided: %s.\n
handleRTIClientFDRFile
%3E
LINETYPE
exception
Backup directory (%s) does not exist, creating it\n
Loaded XBLs\n
PINTO_MAC
InstallTicket failed to get desired response\n
%s::%s: REFS supported: %d\n
Assertion failure ( fZipFile && \"Firmware data source error.\" )
Assertion failure ( ( ret == kBBUReturnSuccess ) && \"Failed to copy ELF header identity from data source.\" )
BBUpdater error  [0-9]+
createImage_PowerTable
Assertion failure ( success && \"Failed to create CertID!\" )
Cellular2,CdpAscUl
getBasebandCapabilites
EBL length ack unsuccessful: %u\n
CurrentQueue
(%s:%d) Range assignment too large(%p), got(%ld) max(%ld)
StageContext::PersonalizeEUICC
%s::%s: setting firmware path to %s\n
Querying first stage\n
Detected non-zero prov manifest status: 
Cellular1,ProvisioningFirmware
failed creating mode switch command
failed removing %s:  %s\n
Loaded file %s, Comment %s\n
kBBUReturnFDRDataValidationFailed
Baseband indicating EFS erase:  %s
bootdev
%s::%s: ======== COREDUMP: ENTERING IBOOT FIRMWARE BOOT STAGE ========\n
com.apple.BBUCommunication
%s::%s: dynamic image path is not a directory (%s)\n
%s::%s: Failed to setOptions on BasebandUpdater obj\n
bootargs
stateInit
Assertion failure ( loadEBLImage() && \"Error: Failed to load the EBL image!\" )
kBBUReturnFailedCreateController
%s::%s: ======== COMPLETED THIRD BOOT STAGE (CPS) ========\n
%s::%s: failed to get prov session key\n
Assertion failure ( false && \"Unsupported BBU stage.\" )
{unordered_map<std::string, std::string, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::string>>>={__hash_table<std::__hash_value_type<std::string, std::string>, std::__unordered_map_has
%s::%s: Failed BBUFSServer prepare\n
Detect as unfused BB\n
bbpc
Took %f seconds
%s::%s: Could not extract ask to reset setting\n
%s::%s: Ping command failed\n
createAPProvisioningInfo
Assertion failure ( nullptr != fTransportCreated && \"Telephony Util transport error!\" )
handle_signals
%s not found, generating default (ffs) file.
BBUFSServer already running\n
successfully switched Sahara mode to ETLSAHModePending\n
Assertion failure ( false && \"Invalid radio type: Specified radio does not have a XBLsc file.\" )
%s::%s: SysGetInfoV2 response err_stat is: %d\n
Error: failed to get slot info from BB\n
Failed handling hash query
Bad argument
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/API/BBUpdaterController.cpp
ExceptionDump
%s::%s: Failed to open ACIPC interface: 0x%08x\n
%s::%s: sysctlybyname for hw.target failed: %s\n
bbst
root manifest larger than protocol specification, size = %u bytes
StageContext is Coredump, skipping prepare\n
preiboot
Assertion failure ( ( chipID->fNumber && \"Failed to create ChipID!\" ) )
delegate_debug_flags
%s::%s: invalid ACK (0x%x) for PL_CMD_SEND_BUNDLE_IMG\n
received unexpected command ID ( expected: %s, received: %s\n
attempting to put back a buffer the instance does not own
%s::%s: Enabling provisioning flow.\n
Bootstrap Preferences
Unexpected PSI running mode %d (%s)\n
Entry %u: Length 0x%x, filename '%s'
%s::%s: invalid bbcfg hash-table data size\n
kBBUReturnProtocolError
firmware.der
%s::%s: Ping returned success and baseband boot state is ready. Getting the FW version\n
 ,PMStatus=
%s::%s: EID Hex to Data conversion failed\n
%s::%s: could not split parameter: %s\n
%s::%s: failed to read pkhash size\n
assign
Loaded binary file '%s'\n
GoldCertId
%s::%s: Collecting coredump...\n
%s::%s: Baseband ECID is not in expected data format.\n
Assertion failure ( false && \"Invalid radio type: Specified radio does not have a Cpucp file.\" )
gatherPreflightParameters
ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\([a-zA-Z\\.]+\\) [0-9a-zA-Z]+\\([0-9]+-[0-9a-fA-F]+\\) SZ\\(|\\) TRX\\(0x[0-9a-f]+\\) AP\\.SEQ\\(0x[0-9a-f]+\\).*
log_sync
Assertion failure ( false && \"Unrecognized BBUICE Remote Data fileName.\" )
WifiAddress
Failed to open file %s\n
%s::%s: missing power table image - this is allowed for now\n
BBUFSServer filer read session (%llu) file (%s) transfer status: %s\n
%s::%s: snapshot received (flush completion with null-log)\n
/var/wireless/baseband_data/bbfs/
Provisioning Public Key Source is not NULL
%s::%s: Bad bootNonceHash size %u\n
Assertion failure ( fBasebandController )
%s::%s: unexpected debug log path type\n
Assertion failure ( success && \"Failed to get MEID.\" )
failed creating backup directory: %d, %d (%s)\n
BasebandBooter
%s::%s: Unexpected skip coredump setting type\n
chownToWireless
Failed to get IMEI.
iargs
\tDescription: '%s', Filename '%s'
Detected it is fused or fusing source is not found. Use the dummy sec.elf\n
createByteSwappedData
kBBUReturnManifestImageError
%s::%s: Failed to create diagnostics object\n
%s::%s: failed to send nvram dynamic image\n
File %s ret %d\n
Failed to re-seek, err = %s (%u)\n
firmwareSaveFolder
Cellular1,BbActivationBypassEnable
%s::%s: failed to create provisioning manifest image\n
Fatal error 1 in FDR data validation/decode
collectCoredump
enable-auth-debug
DaleFirmware
Failed sending MRC training start in mrcTrainInit
%s::%s: Failed to create personalization parameters dictionary\n
VinylPersoHost
Assertion failure ( ( DR_Success == ret ) && \"Invalid input Firmware.\" )
%s::%s: Failed CsiSecReadSikPKey ARI command\n
Failed to gather provisioning parameters
Baseband FW isn't complete. You are missing some images!\n
GetWrapKeyServer %d\n
fs == std::future_status::ready
 from 
Provisioning Manifest Source is not NULL
Assertion failure ( ( offset < (getWritePayloadLength() + kBinHeaderSize ) ) && \"Error: Chunk size is not sufficient to write payload data of the binary image.\" )
AMFDRSealingMapCreateRecoveryPermissions
bbcfg-hash-table
Failed to AuthenticatePersoDevice status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
%s::%s: >>send bbticket\n
Image NOT found in FDR, so ignore all errors coming from the AMFDR and depend on BB to fail if necassary
%s::%s: ======== COREDUMP: COMPLETED IBOOT PREFIRMWARE BOOT STAGE  ========\n
Fail to check manifest in manifest check: 
%s::%s: send bbcfg hash-table status error (0x%x)\n
%s::%s: missing nonce\n
v28@?0Q8i16r^v20
ELF PARAM
PT version info - MobileAsset[%s] iOS[%s]
%s::%s: USB_ETHER_MAC:%s\n
inDict
kBBUReturnFileError
Debug Log Path: 
%s::%s: successfully retrieved board parameters in loader\n
Failed to DeleteProfile status %d SW1_SW2 0x%x\n
Assertion failure ( transport && \"BBU telephony util transport error.\" )
%s::%s: ======== COREDUMP COMPLETE ========\n
%s::%s: Baseband FW version: %s\n
BluetoothAddress
provisioning/
BBUFSServer failed to create backup directory\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Protocol/ICE/BBUICE16Programmer.cpp
IsBBFused? Bool = %d
failed backing up file %s to %s:  %s\n
%s::%s: Looks like NVRAM dynamic copy is lost somehow. This should not have happened\n
ETH_MAC
%s::%s: Failed to update IMEI SVN to %d\n
m9kefs2
unlinking MRC data %s
v12@?0I8
kBBUReturnProgrammerConnectionError
getNVItems
Assertion failure ( (ret == kBBUReturnSuccess) && \"Failed to copy NVM image payload data to buffer!\" )
%s::%s: Base64Encode failed\n
SHA256 detected\n
%s::%s: Copy existing provisining info from the device\n
%s::%s: Failed to obtain the personalized FW base path from MSU\n
%s::%s: failed to init booter object\n
Boot stage Unknown
Powercycle after fusing
Detected non-zero cal/prov/fac manifests status  [CMStatus=
Gathered AP prov info: 
exception_LoaderStage
Assertion failure ( success && \"Failed to create key status.\" )
CircularFileLogWriter
%s::%s: <<rcv FLB_MSG_GET_ROOT_PUBK_HASH\n
%s::%s: Failed GetNvItemsSetting ARI command: result %d\n
%s::%s: bver data returned has a length of 0, so skipping FTAB chipID check\n
Assertion failure ( false && \"Invalid radio type: Specified radio does not have a XBL Config file.\" )
Failed reading EBL download ack\n
failed sending mode end packet\n
Failed to restore backup file (%s)\n
        %s - %c/%c?: 
backing up file from %s to %s\n
%s::%s: missing goldcertid\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Provisioning/BBUMatureProvisioningData.cpp
invalid field length:  dataClass = %li, serial = %li\n
Sent read data at offset 0x%08x, chunk %u\n
%s::%s: Skipping safe warm reset for ConfigSim\n
Provisioning state %s(%u), mismatched %u
B64_SKEY_HASH
SecondaryBluetoothMacAddress
' (offset=
Fail to send %s !\n
%s::%s: failed to read rsp for FLB_MSG_ACK_BIN_BODY\n
%s::%s: >>send provisioning manifest payload\n
pushFirmware_BootROMStage
Failed to register BasebandUpdater CFRuntimeClass
No :-(
%s::%s: Failed to find boot stage\n
Assertion failure ( success && \"Unrecognized radio type.\" )
Personalize_
Cellular1,CdpHost
%s::%s: >>send PL_CMD_RECV_NONCE\n
%s::%s: failed to create BasebandBooter object\n
kBBUReturnBadArgument
%s::%s: In restoreOS: returning zero size MobileAsset file %s\n
v24@?0^{?=^vQQQ}8r^{ETLSAHDebugDataFieldRecord64Bit_t=QQQ[20c][20c]}16
Assertion failure ( ret == static_cast<SInt32>( amount ) )
%s::%s: Transport instance missing\n
%s::%s: failed to create group\n
Failed to seek to %u, err = %s (%u)\n
crash_details
%s::%s: rootManifestSigCert CFDataCreate error.\n
%s::%s: Failed to store crash reason\n
Failed generating data source for %s while copying baseband migration data\n
%s::%s: >>send PL_CMD_SEND_DYNAMIC_IMG\n
%s::%s: invalid ACK (0x%x) for PL_CMD_SEND_DYNAMIC_IMG\n
(%s:%d) Array assignment too large(%p), got(%zu) max(%zu)
BBUBootLogger: readCompletionBlock: status: 0x%x, size: %u, buffer: %s
com.apple.BBULogIOABP
modem boot up failure \\[.+\\]
oslog
Sending finish provisioning command
%s::%s: imei reversedData is null\n
failed saving record\n
Failed to enable\n
%s::%s: using data source for image %s\n
%28
Cellular2,PMUFW
sSnapshot
%s::%s: FDR file path for %s is: %s\n
\t%-30s  0x%-10llx
%s::%s: Failed to get board params (%d)\n
ELF MAX SIZE
(snipped)
DebugArgs
%s::%s: IMEI2 data processing failed\n
%s::%s: NULL value param\n
Assertion failure ( ( e_ident[EI_CLASS] == kELFClass32 || e_ident[EI_CLASS] == kELFClass64 ) && \"ELF header identity (architecture) mismatch.\" )
%s::%s: Failed to find matching service for BB Control\n
Fail to bootup baseband: 
%s::%s: BT_MAC:%s\n
%s::%s: failed to write bundle image\n
%s::%s: >>send nvram data\n
com.apple.telephony.baseband.
%s::%s: Failed to load image on SECOND (iBoot) boot stage\n
shouldPerformFusingVerification: Fusing verification will not perform on legacy device\n
AMFDRSealingMapCreateAndPopulateSealedData
Assertion failure ( fuser && \"Error in creating fusing process.\" )
Failed generating empty EFS file %u\n
%s::%s: >>send calibration image size (%zu)\n
%s::%s: ChipID: 0x%x, ECID: 0x%016llx\n
%s::%s: cold-resetting baseband...\n
reconfig-breakpoints
%s::%s: failed to read rsp for FLB_MSG_BIN_HEADER_STATUS\n
Failed to get Instructions in fusingprogram.plist
BBUScratchFile
Supported Bootloader Versions success %d ret { %s }\n
%s::%s: Not implemented\n
NULL input parameter(s), returning empty string\n
kBBUReturnGetIMEIFailure
kBBUReturnGetICCIDFailure
%s::%s: invalid boot mode\n
AMFDRPerformManifestCheck
AMFDRDataCopySslRoots
AMFDRSealingMapCopyLocalMinimalManifestForInstance
Failed StreamAPDU set %d/%zu, status %d sw1_sw2 0x%x \n
copyParametersDictionary
createImage_ProvisioningManifest
Failed
%s::%s: failed to read fast-boot status\n
%s::%s: failed to create file object\n
%s::%s: goldCertId: 0x%s\n
could not close file %s\n
}
AMFDRDataCopyTrustObject
   PUBLIC_KEY_HASH: 0x%s
Failed to locate %s while copying baseband migration data\n
%s::%s: >>send DALE_PL_CMD_SEND_BBCFG_SEGMENT\n
creating backup directory at %s\n
%s::%s: Require partition mounts command success\n
%s::%s: reset reason encoding is not supported, so crashing baseband with SPMI without specifying reason\n
too many retries: %u\n
APDP
kBBUNVRestoreSettingMax
supports.fs
pushFirmware_LoaderStage
NVSerialNumber
%s::%s: copy prov key hash returned null data\n
verifyFusing
loader
apps.mbn
%s::%s: MG read for preflight info gathering failed\n
root manifest hash data mismatches baseband hash response
%s::%s: failed to create coredump path ref\n
dataref
%s/Perso-%02d-%s
Assertion failure ( provisioner )
%s::%s: Missing transport parameter\n
BBULogIOABP
failed getting getting DDR training data with %s\n
%s::%s: KernelPCIRestoreTrace obj is gone\n
=========== eUICC Options ============\n
psiResp.result = 0x%X (%s)
%s::%s: Crashing baseband (SPMI)\n
%s::%s: [Boot Logger UART] Stopping rom log\n
mawi
Assertion failure ( loadNVMFiles() && \"Error: Failed to load the NVM image!\" )
Cellular1,BbFATPCalibrationEnable
ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\([a-zA-Z\\.]+\\) [0-9a-zA-Z]+\\([0-9]+-[0-9a-fA-F]+\\) SZ\\([0-9]+\\) TRX\\(0x[0-9a-f]+\\) AP\\.SEQ\\(|\\).*
%s backup present, restoring\n
Assertion failure ( false && \"Unrecognized BBUEUR Remote Data fileName.\" )
createImage_Calibration
populateRequestDictionary
VinylForceMain
%s::%s: failed to process ddr\n
%s::%s: failed to warm-reset baseband\n
DaleController
SVN set: %d\n
VinylClearMetadata
cannot truncate file %s\n
mainFW != nullptr
%s::%s: Received Response Code: %d\n
BBUFSServer stopped successfully\n
%s::%s: -------- INIT --------\n
bypass-nvm-sync
Opening %s\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Provisioning/BBUEURProvisioner.cpp
%s::%s: failed to create loader image\n
Failed to get baseband firmware version.
Failed to allocate space for manifest_status\n
%s::%s: Baseband chip revision %s is not supported by the baseband firmware\n
attemptedToFuse
sCompleteTransfer
%s::%s: Unknown transport type\n
setNVItems
Assertion failure ( ( amountRead == sizeof( SectionHeaderTable64 ) ) && \"Copied data size mismatch: Failed to copy data from section header table.\" )
allocateBuffQueue_sync
Assertion failure ( data && \"Failed to create serial number.\" )
VinyleUICCPerformOperation
%s::%s: >>send baseband capabilities request (shippingSettings=0x%x, controlFlag=0x%llx)\n
invalid parameters specified: parameters = %p, destination = %s\n
kBBUReturnError
%s::%s: Failed to create ACFUDataContainer for NVRAM file\n
%s::%s: Successfully deleted baseband file system directory contents\n
Query whether any partitions need to be mounted
SM::Recovery -- normal? %d\n
failed opening %s:  %s\n
Creating firmware object for post sealing step with path: 
Failed to create Start ACK packet.\n
EncryptedSessionKey
AOP image missing\n
%s::%s: >>send PL_CMD_SEND_DEVCFG\n
Cellular1,Ticket
%s::%s: Baseband chip revision %s is supported by the baseband firmware\n
PAC: Set kAMFDROptionApTicket: %s\n
Miss images for bootupInternal\n
BBCFG
%s::%s: Invalid coredump path\n
UART
Failed performing eUICC: 
kBBUReturnServerError
BBUFSServer timeout waiting for filer read session (%llu) start\n
forcePerso    
02:88:88:88:88:88
outData.Valid()
Register call returns %d\n
auto-boot='1', bootdelay='0', host-env='1', 
loading failed\n
Sending EBL without xor\n
Saving new training data
attempting %u out of %u\n
Loaded SHRM\n
Cellular2,LLB
%s::%s: Unexpected baseband FWSaveFolder option CF type\n
TIMEOUT for message MIPC .*?
%s::%s: Both user and default nvram item lists are empty - this should not happens\n
update
Decode sequence failure with der return: %d, decode tag: %x\n
%s::%s: failed to get crash reason\n
%s::%s: Failed to create Baseband updater object\n
Assertion failure ( ( amountRead == sizeof( e_ident ) ) && \"Copied data size mismatch: Failed to copy ELF header identity from data source.\" )
HelloWaitTimeoutSec
Enabled 
IMEI2 is valid. Populating provisioning params!
SEC
unexpected start mode %u, %s\n
%s::%s:   skey_hash    [0x%02x]: %s\n
bootdelay
rsp
%s::%s: No BbRequestEntries in dictionary passed in by PR.\n
Signature Address: %u, Signature Size: %u\n
dumpPCIEState_sync
Resetting state machine: %s --> %s\n
   SNUM: 0x%s / CHIPID: 0x%08x
logmask
stateFusing
acdb.mbn
%s::%s: provInfo key buffer alloc failed\n
yes
kBBUReturnGetBootupTimeError
%s::%s: Failed to create final nvram CFString for sticky nvram plist file\n
%s::%s: invalid bbticket image\n
Region Type
ff_create_transport
Loader version: %s
Assertion failure ( success && \"Failed to get the main loader version from Main FW.\" )
%s::%s: server request failed -> no response\n
%s::%s: Detected non-zero cal/prov/fac/nvm manifests status\n
Assertion failure ( success && \"Failed to create chipID!\" )
Fatal Error: Error creating vinyl valve! Current State: %s\n
%s::%s: GFH header checksum mismatch; expected: 0x%x, actual: 0x%x\n
%s::%s: Failed to create imei2 string ref\n
%s::%s: <<rcv baseband capabilities\n
restorepsi2.bin
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Support/BBULogCircularBuffer.cpp
%s::%s: >>send body payload\n
CPUCP
%s::%s: Received reverse proxy settings not in correct type\n
/bbupdate_profile.plist
kBBUReturnResetToPBL
(
Failed to gather personalization information.
Assertion failure ( fRestoreSBLImage == __null )
ELF
BBUEURFusing
alternate form
%s::%s: Failed creating nvram.bin.\n
createImage_DynamicNVRAM
QTIMisc
%s::%s: <<rcv new ddr data size\n
Creating transport:%p stage:%d interface:%d\n
coredumpCmd
failed restoring %s to %s:  %s\n
com.apple.EmbeddedSoftwareRestore.eUICC.bootloaderMajorVersion
Fail to get update source for collectCoredump\n
Unknown
%s::%s: booting baseband...\n
%s::%s: Provisioning MPN has wrong type\n
%s: ... %0.1f%c\n
SWID Mismatch
EUICCCertIdentifier
FATPCalibration enabled flag: %d
cps
end of image %u\n
restorexbl_sc.elf
DR_Success == ret
/
Ping success
MRC data doesn't exist or is invalid size - training fresh data
Trying to set SVN\n
Assertion failure ( fSignedFirmwareSOCViewImage && \"Failed loading SignedFirmwareSOCView image for creating hash.\" )
Boot Logger Transport PCIE
%s::%s: Retrieved personalization parameters for live boot successfully\n
%s::%s: Image transfer timeout on ROM stage for coredump, aborting via force warm reset\n
<< SNUM >>
%s::%s: missing chipid\n
ACFUDebugArgs
misc
%s::%s: failed to read crash reason size\n
fusingSource
StartSession
restorepsi.bin
Failed to create BasebandUpdater CFRuntime object
Failed to get PRP\n
ClassIdentifier with show(): %s\n
failed to get uid and gid information for _wireless\n
Baseband reported failure during image download (%s).\n
%Y.%m.%d_%H-%M-%S%z
ProvisionQuery
Calloc for apticket path failed
FusingProfile
hw.target
ValidatePersoDeviceRequest.bin
kBBUReturnFailCreateTransportFirst
BBUFSServer failed to queue filer read session (%llu)\n
bootlogger.timer
%s::%s: Failed to get the baseband BootMode\n
Failed changing owner of coredump directory:  %s: %s\n
%s::%s: stopping kernel trace interface\n
invalid SignedFirmwareSOCView image\n
{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8@?0
%s::%s: Provisioning failed.\n
<
Fail to get update source data for finalize\n
%s::%s: Creating diagnostics object...\n
%s::%s: fUpdaterOptions dictionary is NULL\n
Instructions
Sending Erase BB EEPROM in Reserved%lu\n
%s::%s: Failed to create CFString from personalized FW base path\n
%s::%s: RootManifest Size: %ld\n
%s::%s: Skipping baseband ping\n
failed parsing done response\n
Assertion failure ( ( ret == kBBUReturnSuccess ) && \"Failed to copy data from program header table.\" )
Invalid MRC Data Length received from BB
too many repersonalizations
Invalid GetData response from the BB\n
Assertion failure ( loadELFFiles() && \"Error: Failed to load the ELF image!\" )
ctxt
AMFDRDataCopy
%s::%s: Setting B64_BB_SNUM failed\n
%s::%s: failed to write nvram image\n
SyncStatic
%s::%s: NV items setting provided in the options: %s\n
%s::%s: failed to create libtu controller object\n
%s::%s: required file %s (%s) has 0 bytes of size\n
Failed on closing a file (%s).\n
Failed reading PSI-RAM Running status
ValidatePersoDevice %d\n
%s::%s: verifying dynamic image path... (%s)\n
%s::%s: Did not find baseband migration data in the output dict. Nothing to restore\n
%s::%s: value == NULL\n
Failed to get MEID.
/AppleInternal/Library/BuildRoots/4~CatVugAVHlPmCykG3u5RYNuSUaO3iPS0fZcrWSs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h
%s::%s: Request dictionary cannot be created\n
AMFDRDataPrefetch
%s::%s: failed to read ACK for PL_CMD_SEND_DYNAMIC_IMG\n
%s::%s: Could not create RTKitFirmware with custom FTAB path\n
eUICC not stuffed but that's ok!\n
DaleController_BootROM
initial
Failed to prep\n
Fail to get update source for checkManifest\n
sCreateFilerSession
Waiting for Hello\n
Proxy Aborted? %d\n
%s::%s: Image transfer timeout for coredump, aborting via force warm reset\n
%s::%s: invalid image save path (empty)\n
%s::%s: [Boot Logger UART] Stopping PL/LK log\n
%s::%s: Default NVRAM items for restore: %s\n
%s::%s: NV items setting not provided in the options: defaulting to %s\n
Cellular2,SecurityMode
failed reading pkhash from booted baseband over KTL
Failed opening stream for restoring baseband migration data
failed initializing ring buffer\n
nonce
%s::%s: <<rcv crash reason size\n
%s::%s: failed to read ACK for DALE_CMD_SEND_PROVISIONING_MANIFEST\n
StreamFirmware failed\n
    power_sequence_index: 0x%04x
%s::%s: invalid image type\n
ff_bootup
AP triggered baseband reset over ARI
XblSupport
Backup directory path (%s) exists but is not a directory\n
%s::%s: failed to init exception dump object\n
ClassIdentifier bbcl string check: %d
v24@?0{shared_ptr<ctu::Http::HttpResponse>=^{HttpResponse}^{__shared_weak_count}}8
Unlinking MRC had an error %s
kBBUReturnBootedForCoreDump
%s::%s: >>send PL_CMD_SEND_ROOT_MANIFEST\n
%s::%s: Failed to get NV items settings from the baseband\n
kBBUReturnSuccess == r && infoPlist
Unrecognized command 
re-personalize\n
failed preparing file path\n
%s::%s: %s: true\n
MobileAssetWIPath
%s::%s: BootNonce size: %u\n
getShouldFuseProv %d\n
stateBooting
exiting %s
%s::%s: getting board parameters (preflight)...\n
Failed parsing hash response
%s: Good\n
Failed disconnecting programmer 
Cellular1,PMUFW
getCrashReason
startLogging_block_invoke
The width option should not have a leading zero
Failed creating file server\n
BbSNUM
%s::%s: successfully sent '%s' image\n
%s::%s: invalid nonce size; expected: %u, received: %u\n
FirmwarePreflightInfo
```
