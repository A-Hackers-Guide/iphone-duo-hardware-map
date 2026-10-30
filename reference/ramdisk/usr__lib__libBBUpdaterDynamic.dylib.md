# `/usr/lib/libBBUpdaterDynamic.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 3,028,416 bytes.

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
BB Booted
%s::%s: Unable to update IMEI SVN to %d, but proceeding with restore\n
%s::%s: successfully sent calibration image\n
%s::%s: verifying fdr image path... (%s)\n
%s::%s: Failed to get the baseband transport ImageTransferSegmentSize\n
%s::%s: failed to boot baseband (ACFU error code = %d)\n
send
AMFDRSealingMapRecoverCurrentDevice
Assertion failure ( fFSM )
kBBUReturnCpIdFromBootedFailed
failed sending mode switch command
Assertion failure ( false && \"Unrecognized provisoning support type.\" )
(ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\(([a-zA-Z]+\\.){0,}|\\) [0-9a-zA-Z]+\\([0-9]+-[0-9a-fA-F]+\\) SZ\\([0-9]+\\) TRX\\(0x[0-9a-f]+\\) AP\\.SEQ\\(0x[0-9a-f]+\\).*)
%s::%s: failed to force-warm-reset (ACFU error code = %d), aborting via cold-reset\n
Failed starting loader.
%s::%s: failed to read ACK for PL_CMD_RECV_NONCE\n
BBUFSServer filer read session (%llu) file (%s) transfer status: %s\n
alternate form
Assertion failure ( chipID->fNumber && \"Failed to create certID.\" )
%s::%s: Setting preflight mode\n
%5B
%s::%s: collecting crash reason...\n
XBLsc_HASH
Assertion failure ( false && \"Unsupported BBU stage.\" )
%s::%s: Performing NVM sync to: %s\n
) not found in coredump translation table
%20
Assertion failure ( ( chipID->fNumber && \"Failed to create ChipID!\" ) )
Parsing crash reason...
a character
Ignoring ART mismatch
processDDR
%s::%s: ImageTransferSegmentSize option provided for chunking: %d\n
restoreBasebandMigrationDataCmd
%s::%s: Provisioning failed\n
DaleImage
/dev/null
Failed starting mature provisioning.
%s::%s: invalid bbcfg hash-table image\n
AuthenticatePersoDeviceResponse.bin
Removing Firmware image [%s] in path [%s]\n
Assertion failure ( ( ret == kBBUReturnSuccess ) && \"Failed to copy data from program header table.\" )
AMFDRDataPresent
Preflight detected
%s::%s: failed to read new ddr data size\n
%s::%s: dynamic image path is not a directory (%s)\n
%s::%s: Baseband coredump report:\n\tCoredump type: %s\n\tFull report:\n%s\n
status 0x%hhx cards_type: %hhu \n
AMFDRDataRecover
Main version strings mismatched: Card %s Bundle %s
%s::%s: Failed to load image on iBoot firmware boot stage\n
efsc.bin
%s::%s: Did not find corresponding FDR file name for 4cc tag %s\n
%s::%s: No certification URL found for certification step.\n
checkStatusInfo
%s::%s: Received Response Error (if any): %s\n
Assertion failure ( fRestoreSBLImage == __null )
%s::%s: failed to read ACK for DALE_PL_CMD_SEND_POWER_TABLE\n
cal.der
modem boot up failure \\[|\\]
%s::%s: error: empty fdr image path\n
Unexpected hello disconnect mode\n
%s::%s: Restoring NV items to OQC defaults\n
locale-specific form
restoreBackupFile
BBUICEInitializer
%s::%s: Missing firmware parameter\n
%s::%s: <<rcv new ddr data\n
%s::%s: Failed to create boot logger's transport object\n
Bootstrap
could not close file %s\n
MEID: %s
Assertion failure ( certID->fNumber && \"Failed to create CertID!\" )
%s::%s: failed to read new ddr data\n
failed connecting to sahara in CoreDump\n
-euiccForceCustomer
Fatal error 1 in FDR data validation/decode
%s::%s: postData allocation failed\n
goldFirmware
BbGoldCertId
RegionCode
%s::%s: parsing der encoded file to get the version\n
failed sending maverick hash response\n
%s::%s: failed to read pkhash\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Support/BBULogCircularBuffer.cpp
Waiting for Hello\n
Failed executing secure mode, failing program\n
CRASH DUMP File: %s
escapeHttpUriString
%s::%s: received status: 0x%016llx\n
SendImage returned %s, amountWritten = %u, errorCode = %#x\n
Assertion failure ( d.get() && \"Error: Unable retrieve public key to finish provisioning.\" )
Setting max root packet size from PSI: %u
validateBootStage
%s::%s: invalid msg id 0x%x\n
Gathering Personalization parameters...
%s::%s: Unexpected baseband BootMode option CF type\n
CAL: Set kAMFDROptionCopyAllowUnsealed: %s\n
getBasebandCapabilites
VinyleUICCPerformOperationWithTransport
BBUEUR20Loader
allowRePerso
stopLogging_block_invoke
Failed parsing hash response
Is performManFlow?: Bool = %d
~KernelPCIRestoreTrace
%s::%s: Base64Encode failed\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Provisioning/BBUProvisioningParameters.h
assign
SyncStaticDynamic
Image Size: %u, Code Size: %u\n
ctu::cf::convert_copy( description, errorMsg )
Assertion failure ( ( offset < (getWritePayloadLength() + kBinHeaderSize ) ) && \"Error: Chunk size is not sufficient to write payload data of the binary image.\" )
   Detected as fused BB\n
%s::%s: Encountered an error (%d) during FDR processing\n
Address
%s::%s: failed to write calibration image\n
%s::%s: Provisioning PING result: %s\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Support/BBUFDRUtilities.cpp
We only have acceptable errors, so we can ignore these errors \n
chownToWireless
BBUICE16UpdateSource
%s::%s: failed to create transport\n
OEMMisc_HASH
SendReceipt
failed to receive reset response\n
BBUFSServer failed to set config, unrecognized config name '%s'\n
BBUFSServer failed to clear file backup\n
%s::%s: failed to get image data (offset: %zu, size: %zu)\n
Fail to perform second stage: 
Fusing is requested but no fusing program was given yet. 
kBBUReturnFileNotFound
MobileAssetRPPath
scrt
Cellular2,BbCalibrationEnable
%s::%s: NULL transport parameter\n
ResetReasonEncoder
false
bootdlay
ChipID
AuthInstallProvisioningServerURL
 TelephonyBasebandPCITransportCreate returns: %s\n
attempting to put back a buffer the instance does not own
%s::%s: Could not create RTKitFirmware with params\n
Cellular1,BbActivationBypassEnable
Sending PSI enhanced command 'Start MRC Training' in mrcTrainInit 
PRP timed out %d\n
Cellular1,LLB
BBUEUR13Communication
received too much data ( max expected: %lu, received: %zu )\n
%s::%s: REFS supported: %d\n
Failed to get apticket path; error = %ld
Failed to create dictionary for CAL FDR options\n
%3D
xmissiontimeout
performManifestCheck
%s::%s: -------- QUERY (Step %d - %s) --------\n
%s::%s: Failed to get the ACIPC interface object\n
%s::%s: invalid ACK (0x%x) for PL_CMD_RECV_NONCE\n
Assertion failure ( fZipFile && \"Firmware data source error.\" )
cannot remove existing file %s\n
%2A
Timeout on waiting for BB init status\n
%s::%s: Failed creating nvram.bin.\n
UART
Calloc for datadir path failed
Cellular1,UID_MODE
getReverseProxySettings_block_invoke
IMEI
failed getting record\n
End of Image Transfer due to: 
Loaded EBL file\n
Assertion failure ( nullptr != fTransportCreated && \"Telephony Util transport error!\" )
kBBUReturnManifestNoHashes
kBBUReturnARTMismatchedError
dumpPCIEState_block_invoke
Bunk legacy keys?\n
%s::%s: failed to send bbticket size\n
BBULogIOABP
Requested boot mode:  %s
AMFDRGetTrustError
%s::%s: Null commandCode parameter\n
kBBUReturnTooManyReperso
DR_Success == der_ret && TAG_PILR_OK == dec.tag
Restoring NV items to Factory defaults
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Initialization/ICE/BBUICEInitializer.cpp
 in the first stage.
SM::Recovery -- normal? %d\n
%s::%s: failed to write PL_CMD_SEND_DDR\n
acdb
psi_ram.bin
%s::%s: Could not create RTKitFirmware with custom FTAB path\n
Failed to get coredump list\n
%s::%s: getting crash reason...\n
%s::%s: failed to read status after reading hw info\n
failed sending maverick config response
%s::%s: >>send PL_CMD_SEND_ROOT_MANIFEST\n
Ping success
unordered_map::at: key not found
%s::%s: updaterOptions parameter is NULL\n
ELF READFILE HEADER
Couldn't allocate FD for transaction record during coredump! fd %d path %s\n
output
%s::%s: Failed to send prov manifest to baseband\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Updater/Eureka/BBUEUR20UpdateSource.cpp
Yes
%s::%s: Failed to load image on FIRST (ROM) boot stage\n
%s::%s: Image transfer timeout on ROM stage for coredump, aborting via force warm reset\n
*
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
%s::%s: Path %s does not exist, therefore nothing to erase. Continuing\n
%s::%s: nv parameter is NULL\n
failed copying root manifest to buffer
invalid xbl image\n
ret %d records %zu\n
Assertion failure ( fEnabled )
Unsupported BBU stage: %d\n
%s::%s: MG read for preflight info gathering failed\n
%s::%s: NVRAM sticky_nvram_items.plist read failed with status: (%d)\n
Query whether any partitions need to be mounted
Failed to get FusingProfile\n
full
Assertion failure ( (offset < (getWritePayloadLength())) && \"Chunk size is not sufficient to write payload data of the MRC image!\" )
Failed reading EBL download ack\n
misc
%s::%s: ======== ENTERING SECOND BOOT STAGE (iBoot) ========\n
Get root manifest content from file into memory\n
AMFDRSealedDataCreate
failed to create reset command\n
0x
Boot Logger Transport UART
APTicket FileDataSource class init failed...
%s: Finding index (%d) is beyond the capacity in MSB in the fusing data\n
Set config '%s' to '%d' millisec\n
Failed to enable\n
com.apple.AppleBasebandManager
BasebandHttpCommon
AMFDRGetInfo
eUICC::Done( fOptions )
kBBUReturnKeysNotAligned
Assertion failure ( ( ret == kBBUReturnSuccess ) && \"Failed to copy ELF32 header from data source.\" )
%s::%s: Failed to open ACIPC interface: 0x%08x\n
createProvisionedInfo
%5F
succeeded
Parsing der encoded file to get the version \n
%s::%s: -------- REQUIRE PARTITION MOUNTS --------\n
failed reading hash results\n
StageContext is Coredump, skipping prepare\n
Assertion failure ( fPhases.size() )
%s::%s: missing chipid\n
fwMac.size() == kFWMacSize
%s::%s: ecid str alloc failed\n
%s::%s: Data length %lu is not within range\n
performFusing
%s::%s: failed to send loader\n
logParameters
kBBUReturnNeedsMoreInput
persoStatic   
%s::%s: failed to init image object for ddr\n
com.apple.DaleBootLogger.queue
Failed sending Start ACK packet.\n
fwMacData is wrong type %s\n
setNonce
v16@?0^{dirent=QQSSC[1024c]}8
%s::%s: >>send bbticket\n
performManifestCheckCmd
BypassManifestStatusCheck
v24@?0^v8r^^{__CFDictionary}16
yes
v16@?0I8I12
MGCopyAnswer
%s::%s: Failed to safe warm reset baseband\n
Failed connecting to programmer while querying information in the second stage.
%s::%s: Zero sized input data\n
failed opening %s:  %s\n
Assertion failure ( fProvisioningManifestSource == __null )
%s::%s: Unsupported baseband BootMode option %d\n
%s::%s: Got FTAB chipID: %lu, comparing with actual chipID: %d\n
boot-logging-transport-type
%s::%s: pkhash bytes:\n
%s::%s: Failed to get the baseband BootMode\n
%s::%s: Failed to parse bver data, so skipping FTAB chipID check\n
%s::%s: Pinging baseband with %u ms delay and %zu attempts\n
%s::%s: Failed to create output dictionary\n
decodeBase64
SM::Recovery Missing gold with hash %s\n
%s::%s: Provisioner init() failed\n
%s::%s: failed to write PL_CMD_SEND_DEVCFG\n
finished secure mode
%s::%s: empty queue\n
Failed StreamAPDU set %d/%zu, error %d status %hhu sw1 0x%x sw2 0x%x\n
WARNING: ChipID mismatch (DIAG vs. libTU); using libTU ChipID
%s::%s: Manifest Check Status: %s\n
Cellular1,ECID
boot-command
%s::%s: >>send PL_CMD_SEND_DYNAMIC_IMG\n
%s::%s: fdr directory does not exist, creating (%s)...\n
%s::%s: Transport instance missing\n
MDMDDR
%s::%s: failed to load image from file for %s\n
Resetting state machine: %s --> %s\n
%s::%s: Provisioning MPN has wrong type\n
DataRoot
!GET_RSP_FIELD(rsp, result_t3) && GET_RSP_FIELD(rsp, sim_rsp_len_t5)
Unable to locate file from directory listing '%s'.
kBBUReturnProvisioningDataError
\tCrash reason: File:%s, Line:%d, String:%s
%s::%s: Ping failed, %zu attempts left\n
j <= req.apdu_payload.apdu_data_size
AMFDRDataMultiPut
%s::%s: Firmware instance missing\n
%s::%s: Successfully gathered personalization parameters from ROM; skipping Sik pub key collection from baseband as baseband is in reset\n
MRC data too large
%s::%s: Restoring NV items to Factory defaults\n
%s::%s: failed to collect coredump (timeout)\n
%s::%s: GFH header checksum mismatch; expected: 0x%x, actual: 0x%x\n
%s::%s: sending bbcfg hash-table image...\n
BBUFSServerFlushInProgress
%s::%s: Did not find corresponding NVM file name for 4cc tag %s\n
%s::%s: Invalid ap ticket\n
pingAndGetFWVersion
~~~~ MAX APDU PER SET: %zu  ~~~~\n
,CPU=
Failed to eUICC::updateOutput in BootedStage
CAL
%s::%s: failed to read ACK for PL_CMD_SEND_DYNAMIC_IMG\n
failed closing saved record:  %s\n
kBBUReturnAPTicketFileInitFailed
BBUFSServer started successfully\n
performFusingCmd
BBUBootLogger: readCompletionBlock: status: 0x%x, size: %u, buffer: %s
BoardId
Reset offset for %u, current %u, file %s\n
readStickyNvramItems
feedback
%3F
Current SVN: %d
eUICCVinylMAVValve
Failed creating coredump directory
reset message type: %x\n
kBBUReturnFailedNVSync
%s::%s: Looks like NVRAM dynamic copy is lost somehow. This should not have happened\n
Assertion failure ( eblItem && \"Error: loading EBL item!\" )
SystemRoot
Failed performing eUICC: 
SBL1
rb
kBBUReturnFailCreateTransportInitial
%s::%s: force-warm-resetting baseband...\n
ProvisioningManifestSupported
%s::%s: -------- VERIFY FUSING --------\n
ARI_CLI_ERR - Tracking receipt of unrecognized transaction 0[xX][0-9a-fA-F]+
%s::%s: failed to cold-reset baseband (ACFU error code = %d)\n
boot-args
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Images/ICE/BBUICEEBLImage.cpp
Getting Version
@
createETLStructures
%s::%s: Baseband provisioning status check failed\n
PAC: Set kAMFDROptionDataDirectory: %s\n
%s::%s: getting baseband capabilities...\n
%s::%s: Could not find begin token 'c40' in bver tag, so skipping FTAB chipID check\n
%s: Resetting modem
BbChipID
<libBBUpdater %p [%p]>{}
Fail to get firmware data source\n
MPN
00:00:00:00:00:00
%s::%s: Missing output bb prov info parameter\n
%s backup present, but rule is to delete it\n
%s::%s: Retrieving personalization parameters for preflight\n
kBBUReturnNVMImageError
VinylClearMetadata::GetListOfIccids: Requesting Profile List\n
Assertion failure ( success && \"Failed to create key status.\" )
v12@?0i8
%s::%s: BootNonce size: %u\n
com.apple.BBUCommunication
BBUZipFile
%s::%s: Incorrect type for BasebandOptions dictionary which is passed in by PR.\n
v24@?0^{?=III}8r^{KTLCoreDumpListEntry_t=I[32c]}16
  ckey_hash          : %s
VinyleUICCPerformOperation
%s::%s: >>send baseband capabilities request (shippingSettings=0x%x, controlFlag=0x%llx)\n
Assertion failure ( ( copied == rootManifestSize ) && \"Copied data size does not match root manifest size!\" )
Assertion failure ( ( AMFDRIsSupported() == true ) && \"AMFDR calls are made but dyn libFDR is NOT linked\" )
com.apple.EmbeddedSoftwareRestore.eUICC.bootloaderMinorVersion
QTIMisc image missing\n
Loaded Qupv3Fw\n
SIM still initializing, trying again... sim_state 0x%x (retryCount: %d, retryLimit: %d)\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Communication/ICE/BBUICE16Communication.cpp
%s::%s: failed to get coredump info save directory in str format\n
Gold FW supports %s?\n
%s::%s: Baseband Firmware override has wrong type %lu\n
main
KERN_SUCCESS == kr
prepare
null output
failed to get uid and gid information for _wireless\n
%s::%s: flush logs completion returned error (error [0x%x])\n
%s::%s: BTI stage: iBoot size: %d\n
\t%-30s  <DIR>
Assertion failure ( false && \"Invalid radio type: Specified radio does not have a UEFI file.\" )
load
Invalid directory path\n
<< SNUM >>
kBBUReturnFailCreateTransportSecond
Debug Log Path: 
%40
PMStatusCode
%s::%s: arrayCount is 0\n
Assertion failure ( false && \"Unrecognized BBUEUR Remote Data fileName.\" )
m9kefsc
 \t\n\v\f\r
Sending Erase BB EEPROM in Reserved%lu\n
DaleBootLogger
Integral value outside the range of the char type
shrm.elf
crash_details
Assertion failure ( false && \"Invalid radio type: Specified radio does not have a XBLsc file.\" )
Fail to connect to loader
bbcl string check: %d
coredump.zip
readLogsAsync: ret %#x\n
Failed to load %s (size %s), creating empty file (size %u)
%s::%s: Ping returned failure but did not timeout. Waiting for 500 ms and trying again\n
%s::%s: Dictionary allocation failed\n
Final coredump at %s:
Failed to encode ECID\n
ImageTransferSegmentSizeBytes
BasebandUpdaterIsDone
logLevel=%d
Logic error: invalid BasebandUpdater command: 
Failed to setOptions on BasebandUpdater obj
BBUBootLogger
UEFI
SignedFirmwareSOCView_HASH
%s::%s: Current baseband provisioning status: %s\n
%s::%s: failed to read status after sending provisioning manifest\n
handleRTICrashContextFile
/usr/lib/libMobileGestalt.dylib
MEID
Assertion failure ( fLoader && \"No valid BBULoader!\" )
Wrong firmware, doesn’t match hardware ID 
APDP image missing\n
StageContext::PersonalizeStageFirst
kBBUReturnGetIMEIFailure
failed receiving sahara hello\n
performCmd
failed reading update header\n
%s::%s: baseband coredump collection not supported in firmware\n
The format specifier contains malformed Unicode characters
not found
ClassIdentifier bbpc string check: %d
Assertion failure ( fuser && \"Error in creating fusing process.\" )
Detected non-zero cal/prov/fac manifests status  [CMStatus=
fast-boot
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Updater/ICE/BBUICEUpdateSource.cpp
'
  skey_hash    [0x%02x]: %s
%s::%s: >>send DALE_PL_CMD_SEND_BBCFG_HASH_TABLE\n
NvramItems
handleFDRForNonBridgeSetup
Device has pending updates for file %s\n
Sent Manifest with length %u, %s
%s::%s: defaultsNvramStr has incorrect type, fail.\n
%s::%s: Failed to create BasebandUpdater CFRuntime object\n
CMStatusCode
%s::%s: Provisioning RGN has wrong type\n
StreamFirmware failed\n
%s::%s: invalid image source\n
kBBUReturnFailCreateTransportFirst
statePersonalizeBooted
CPUCP
Reversed IMEI: 
failed creating telephony util transport\n
%s::%s: missing snum\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Support/BBUZipFile.cpp
%s::%s: [Boot Logger] Received %zd pcie log\n
FALSE
Assertion failure ( success && \"Failed to get the main loader version from Main FW.\" )
%s::%s: invalid boot mode\n
%s::%s: Request dictionary cannot be created\n
com.apple.EmbeddedSoftwareRestore.eUICC.firmwareMac
}
unlinking MRC data %s
createDirectoryWithTimestamp
verifyFastBootStatus
StageContext::PersonalizeEUICC
%s::%s: NV items setting not provided in the options: defaulting to %s\n
bootscrp
%s::%s: Invalid uidMode\n
%s::%s: value length is 0\n
failed reading PKHash from booted baseband over ETL
kBBUReturnGetChipIDFailure
HSFilerDynamic library is not available for INT case. It should always be\n
%s::%s: Sending oem mrdump command\n
%s::%s: Failed to load image on SECOND (iBoot) boot stage\n
%s::%s: Received unexpected SCRT pubK size: %u bytes\n
Provisioning Public Key Source is not NULL
error
FSInit: restore_files=%d\n
runCertification
%s::%s: IMEI2: %s\n
%s::%s: Setting kProvB64_IMEI failed\n
handleMaverickGetNonce_nl
Took %f seconds
%@.%@
Signature Address: %u, Signature Size: %u\n
APDP
Failed to complete AuthPerso command\n
failed removing old file, %s, %s\n
%s::%s: %s image currently not supported. Returning zero size file\n
%s::%s: Merged NVRAM {key, value} pairs:\n
collectCoredump_block_invoke
%s::%s: Failed GetCurrentBootState ARI command\n
%s::%s: -------- INIT --------\n
syncBasebandFileSystem
%s::%s: Enabling provisioning flow.\n
not connected to programmer
Perso
%s::%s: Mistyped prov key hash\n
Failed sending data at offset 0x%08x, chunk %u\n
Unknown
%s::%s: Certification failed.\n
AP triggered baseband reset over ARI
AMFDRPerformManifestCheck
successfully streamed Firmware\n
Failed to get debug table\n
failed receiving hello packet\n
Not Enabled
Using the APTicket in the FS to create the FDR option
stateInit
Set ARI context ID to %d\n
Failed writing %u bytes to %s - wrote only %u\n
%s::%s: Failed to create options dictionary\n
Assertion failure ( nullptr != fTransportCreated && \"Telephony util transport error.\" )
Reading of APTicket content failed.
normal
copyVinylEidSinope
%s::%s: wrong imei data\n
GetNonceServerRequest.plist
%s::%s: failed to read rsp for FLB_MSG_ACK_BIN_HEADER\n
configureProvisioner
%s::%s: ROM object instance/s missing\n
EBL
Failed to InitPerso status %d SW1_SW2 0x%x rsp_len %u\n
%s::%s: File %s does not exist: returning zero size NVM file %s\n
Assertion failure ( false && \"Invalid radio type: Specified radio does not have a Shrm file.\" )
forceMain     
_
uefi.elf
%s::%s: IMEI2:%s\n
collectPreCoredump
Connecting to Loader
Key alignment is required
SignData
Assertion failure ( fConnected && \"Cannot finish disconnection, since BBU programmer is already (falsely) recognized as disconnected!\" )
%s::%s: Failed to get domain mode registers\n
UEFI image missing\n
EID: %s
failed creating hello response\n
%s::%s: Failed to send KTLStartProvision cmd\n
An argument index may not have a negative value
Sent PSI successfully!
/bbupdate_profile.plist
PreflightInfo
Cellular2,LLB
Saving image to %s
BBUFSServer filer read session (%llu) status: %s\n
Assertion failure ( fImage && \"BBU Programmer item creation failed.\" )
The fill option contains an invalid value
Baseband fw path that is used: %s\n
MLB
Version String: 
Saved MDMDDR data to: %s\n
BasebandEnableFactoryDebug
\t %s:  %s
%5C
XBLSupport image missing\n
InitPersoDeviceResponse.bin
Proxy Aborted? %d\n
Failed to create dictionary for PROV FDR options\n
Timeout on ping attemps\n
Start
%s::%s: Copy existing provisining info from the device\n
%s::%s: failed to init loader object\n
required path length = %zu, copied = %zu, max length = %zu\n
%s::%s: failed to force-warm-reset baseband\n
%s::%s: Failed to get ecid\n
ICEStateMachinePerformSnapshot
BBUCommon
rom
Region Type (%s): Address (0x%08X), LSB (0x%08X), MSB (0x%08X): PASSED!\n
force
%s::%s: invalid loader image size\n
%s::%s: failed to write PL_CMD_RECV_NONCE\n
BBUFSServer already running\n
Options
FDRSkipSealing
The argument index should end with a ':' or a '}'
Cellular2,BoardID
supports legacy eUICC update? %d\n
sendLoader
%s::%s: IMEI data processing failed\n
%s::%s: failed to read pkhash size\n
failed to copy programmer data from data source\n
%s::%s: Null lai prov info\n
Saving image to %s, success
Copy baseband data to migrate during an erase install
failed opening file %s with fd %i errno %d\n
Assertion failure ( fRestorePSIRamSource == __null )
%s::%s: Baseband boot state: %d\n
BBUFSServerRelease
%s::%s: Failed to create folder %s\n
%s::%s: Failed to initialize BasebandRestore object (%d)\n
VerifyData
Failed to store data status %d SW1_SW2 0x%x\n
Assertion failure ( fwMac.data && \"Corrupt FW in input!\" )
safe-timer.
Preparing at %s with reset requested %u\n
failed converting core dump path to string
Failed to register for reset detect
bootdev
%s::%s: failed to pre-assign buffer # %u of size %u KB to fetch logs (error [0x%x])\n
Loaded TZ\n
Loaded ACDB\n
%s::%s: Provisioning complete\n
Failed to complete FinalizePerso command\n
nothing to back up\n
createReversedIMEI
Assertion failure ( transport && \"Telephony util transport error\" )
%s::%s: Ping timeout\n
/coredump.log
Assertion failure ( false && \"Invalid radio type: Specified radio does not have a XBL Config file.\" )
invalid arguments:  dataClass = %p, serial = %p, options = %p
Assertion failure ( amountRead == sizeof( ProgramHeaderTable32 ) && \"Copied data size mismatch: Failed to copy data from program header table.\" )
backup/
Error: image filter list is empty, cannot save any images!\n
BBUFSServer failed to transfer file (%s)\n
Overriding Product Type : %u and Hardware Config: 0x%x in Reserved %zu\n
%s::%s: Warning: unable to retrieve baseband chip revision (error code = %d), so skipping chip-revision/firmware-recipe check\n
pushFirmware_BootROMStage
Assuming mature provisioning supported.
Path %s -> Mac %s\n
eUICCVinylICEValve
createImage_ProvisioningManifest
Failed to backup file from (%s) to (%s)\n
Assertion failure ( ( amountRead == sizeof( Header64 ) ) && \"Copied data size mismatch: Failed to copy ELF64 header from data source.\" )
Invalid vendor for log delegate registration
eUICC Firmware loaded! Version %s MAC %s\n
%s::%s: failed to init image object for %s\n
createImage_SystemBundle
postString=
Failed to get baseband identifiers from booted baseband
Assertion failure ( success && \"Failed to get IMEI.\" )
sendProvisioningManifest
Assertion failure ( false )
Failed handling hash query
%s::%s: Failed to prepare bbfs path: %s\n
Assertion failure ( stateRef && \"Failed to create state reference for fusing manifest info.\" )
init
Loaded Manifest\n
hit an error while copying data from FDR\n
%s::%s: Invalid boardID\n
%s::%s: Not implemented\n
Requested to sync dynamic\n
kBBUReturnEBLImageError
Sending images for CoreDump...
ping
Cellular1,Ticket
Failed sending MRC training start in mrcTrainInit
%s::%s: failed to reverse imei\n
%s::%s: decode 2nd tag failure with der return: %d, decoded tag: %llu\n\n
internal buffer is %lu bytes\n
%s::%s: Getting current IMEI SVN\n
Assertion failure ( false && \"Unrecognized BBU loader version type!\" )
Cellular1,ProductionMode
modem %s reset
%s::%s: failed to write data header\n
efs
InitPersoDevice %d\n
%s::%s: NULL outData param\n
%s::%s: attempting to set invalid dynamic path\n
%s::%s: send bbcfg segment status error (0x%x)\n
downloadFusingProgram
sign
loading failed\n
/System/Library/Caches/com.apple.factorydata
requirePartitionMount
%s::%s: NULL data param\n
%s::%s: Failed to init logging\n
\t%u - Type: %u, Offset %u, VAddr %u, PAddr %u FileSize %u, MemSize %u, Flags %u\n
pc_trace
v28@?0i8^v12^v20
%s::%s: Failed to create timer\n
%s::%s: Could not extract skip coredump setting\n
Failed changing owner of coredump directory:  %s: %s\n
Restored backup file from (%s) to (%s)\n
SendImage returned %s, amountWritten = %u, status = %u\n
%s::%s: dataptr get nullptr after CFDataGetBytePtr\n
eraseBasebandFileSystem
BBUpdater Version: %s-%s\n
%s::%s: >>send PL_CMD_SEND_CAL_IMG\n
%s::%s: power table image 2 not valid\n
Failed to FinalizePerso status %d SW1_SW2 0x%x\n
failed creating backup directory\n
Miss images for saveImages\n
In UpdateGold, fwMac.data = %p\n
%s::%s: failed to write bundle image\n
%s::%s: index: %u\n
eUICC is not done yet\n
BBUPurpleReverseProxy
Failed creating directory %s\n
%s::%s: ACIPC %s interface opened successfully\n
%s::%s: ======== ENTERING IBOOT PREFIRMWARE BOOT STAGE ========\n
attempting %u out of %u\n
%s::%s: failed to create group\n
BootROM
BBUFDRUtilities
Failed to get directory ownership information for _wireless\n
Assertion failure ( (ret == kBBUReturnSuccess) && \"Failed to copy image payload data to buffer!\" )
%s::%s: Unable create LAI prov dictionary\n
Failed preparing baseband filesystem directory for copying baseband migration data\n
getCrashReason
%s::%s: Unexpected baseband firmware path CF type\n
Assertion failure ( d.get() && \"Unable to extract public key to start mature provisioning.\" )
-boot-log
%s::%s: Error: BBUFSServer stop failed\n
%s::%s: ======== ENTERING THIRD BOOT STAGE (CPS) ========\n
Final stage
Register call returns %d\n
TIMEOUT for message MIPC.*?Client=.*?Msg=.*?Trx=.*? 
PAC: Set kAMFDROptionApTicket: %s\n
%s::%s: Failed to initialize update operations\n
%s::%s: failed to create dynamic nvram image\n
AMFDRSealingMapCopyInstanceWithIdentifiers
Assertion failure ( v )
queryInfo
failed reading file: return code = %d\n
Assertion failure ( fZipFile && \"Error: BBU firmware data error!\" )
kBBUReturnRPMImageError
report.json
%s::%s: SysGetInfoV2 response err_stat is: %d\n
AMFDRSealingMapCopyLocalMinimalManifestForInstance
%s::%s: failed to send the baseband capabilities request\n
sSaveRecord
0X
Failed sending EBL binary\n
IsBBFused? Bool = %d
invalid SequencerRam image\n
%s::%s: invalid ACK for DALE_PL_CMD_SEND_POWER_TABLE\n
PersoImpl
%s::%s: failed to create file container for %s (%s)\n
%s::%s: failed to verify dynamic image path\n
%s::%s: end token '|' does not exist in bver tag\n
^\\[bbutil\\].*
dataref
XblCfg image missing\n
version compatible:  %u\n
Failed to create scratch %s (%d)
%s::%s: >>send PL_CMD_SEND_DEVCFG\n
Missing or empty server sssion?! %s\n
kBBUReturnGetCarrierIDFailure
host_taskname
setNVItems
sMergeNVRAMKeyValPairLists
Failed to finalize: 
%s::%s: <<rcv FLB_MSG_EFUSE_PUBLIC_INFO_STATUS ACK\n
InitPersoServerRequest.plist
waiting for hello with timeout of %u sec\n
%s::%s: [Boot Logger PCIE] Stopping rom log\n
<BasebandUpdater %p [%p]>{}
AMFDRCopyClientId
Gold version strings mismatched: Card %s Bundle %s\n
DF:AD:BE:FF:00:00
invalid arguments transport:  %p, updateSource: %p\n
01
' (offset=
#
ari.create
check failed: %s, %d, assertion: %s\n
%s
BBUFSServer failed to queue filer read session (%llu)\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Provisioning/BBUMatureProvisioningData.cpp
%s::%s: -------- PERFORM FUSING --------\n
Provision manifest status:%u => state %s(%u), mismatched %u
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/FirmwareVersion/Eureka/BBUEURLoaderVersion.cpp
bypass-nvm-sync
valid
%s::%s: send power table status error (0x%x)\n
Fail to get update source for queryInfoSecondStageInternal
%s::%s: responseParts is NULL\n
%s::%s: Baseband provisioning PING is enabled.\n
%2B
Assertion failure ( dict && \"Failed to create dictionary for updating provisioning parameters.\" )
%s::%s: Failed populating the request dictionary for ProvisioningPing cmd\n
getNVRestoreSettingOption
%s::%s: invalid arguments (offset: %zu, length: %zu) for image %s\n
IMEI-SVN Check and Update...
Loaded %s (%p)\n
Failed to serialize dictionary %s error %s\n
received '%s' error. arg0 = %#llx arg1 = %#llx\n
call with %p different from fTransportCreated(%p)\n
Assertion failure ( ::memcmp( e_ident, kIdentMagic, sizeof( kIdentMagic ) ) == 0 )
provisioning
HYP image missing\n
kBBUNVRestoreSettingMax
failed to respond to hello packet\n
VinylClearMetadata::ClearMetadataForIccids: Attempted metadata clear for ICCID\n
profile.bin
([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})
%s::%s: imei reversedData is null\n
Failed to get EID.
a floating-point
%s::%s: copy baseband prov info returned null data\n
verifyFusingCmd
Failed to create BasebandUpdater CFRuntime object
failed sending mode end packet
%s::%s: failed to collect coredump (ACFU error code = %d)\n
Assertion failure ( fPersonalizationParameters->getSerialNumber() && \"Invalid serial number\" )
bootInternal
Failed to gather provisioning parameters
requestedBasebandFSPartitionMountSize
%s::%s: Failed to get filename for tag: %s\n
%s::%s: Failed to create imei string ref\n
sbl1.mbn
Failed to read file %s
Fail to open kernelControl: %#x \n
, 
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Support/BBUError.cpp
%s::%s: Syncing baseband file system\n
precision
Retry
%s::%s: Missing prov manifest.\n
sendImage_BBCfgSegment
%s::%s: verifying firmware path... (%s)\n
BBUFSServer timeout waiting for filer read session (%llu) to end\n
%s::%s: BootNonceHash size: %u\n
~
auto-boot='1', bootdelay='0', host-env='1', 
%s::%s: Successfully deleted baseband file system directory contents\n
Trying to set new SVN\n
Assertion failure ( fProvisioningPublicKeySource == __null )
%s::%s: Failed to determine the value of the boot stage\n
Qupv3Fw image missing\n
BBU_BUILD_INFO
Failed to get fusing source\n
Debug Log Buffer
UDID
%s::%s: Failed to create updater options dictionary\n
getReset
EFS file verify status: %d
AOP
%s::%s: >>send provisioning manifest payload\n
invalid parameters specified: parameters = %p, destination = %s\n
kBBUReturnInitializeRingBufferError
ignore-fusing-sec-boot-status
collectCrashReason
%s::%s: pkhash is all zeros\n
%s::%s: coredump collection: loader stage\n
nvramRef
, FCMStatus=
successfully switched back to Normal\n
Assertion failure ( amountCopied == dataSize && \"Unable to copy manifest data to finish provisioning.\" )
eUICC
%s::%s: failed to write PL_CMD_RECV_BOOT_MODE\n
%s::%s: failed to write DALE_PL_CMD_SEND_BBCFG_HASH_TABLE\n
Sending finish provisioning command
%s::%s: >>send FLB_MSG_LOAD_BIN_HEADER\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/eUICC/Source/eUICCFirmware.cpp
%s::%s: Failed to store crash reason\n
%s::%s: BT_MAC2:%s\n
Gathered baseband prov info: 
%s::%s: Could not create RTKitFirmware with passed in FTAB path\n
Failed to create data\n
createByteSwappedData
Loaded public key source\n
kBBUReturnFailedCreateController
%s::%s: -------- PERFORM (Step %d - %s) --------\n
multi_image_qti.mbn
ARICtxId
Unexpected data size received.  Got %u, expected %u\n
%s::%s: PR3 Force Server Provisioning option: %s\n
bbufs
: failed to statfs
%s::%s: Baseband already in reset state, no need to crash it\n
source
Install gold but no ticket -- back to restored please\n
%s::%s: failed to init bootrom object\n
Sending config response...
%s::%s: data length is equal or less than zero\n
%s::%s: Invalid typecast, fail.\n
NULL BasebandUpdater object
dbgsoc
Retrying ping\n
SyncStaticDynamicCalibration
Failed to get uid gid information for _wireless\n
Failed to restore backup file (%s)\n
%s: Start resetting modem
88:88:88:88:88:88
NVRAM: %s\n
Failed reading MRC training response
kBBUReturnBBTicketDERParseErrorForFATPCal
setupTimer_sync
%7C
failed sending maverick root manifest response\n
%s::%s: boot mode: %s, exctype: 0x%x\n
%s::%s: boot timeout, aborting via force-warm-reset\n
[%04u]: %s
Assertion failure ( ( amountCopied == amount ) && \"Copied data size mismatch: Failed to copy MI Image data.\" )
AMFDRDataPrefetch
Assertion failure ( false && \"Unrecognized provisioning support type.\" )
Failed to write file: 
failed parsing sahara hello\n
TIMEOUT for message MIPC .*?
Error: Data Not accepted, also, BB didn't send new data
ClassIdentifier with show(): %s\n
Baseband FW isn't complete. You are missing some images!\n
log_data
both files not present in backup, removing backup files\n
%s::%s: invalid calibration image\n
%s::%s: Failed to perform preBoot actions (ACFU error code = %d)\n
parseAndSaveCrashReason
%s::%s: Failed to create URL for NVM file %s while restoring baseband migration data\n
auto-boot='1', bootdelay='0', 
prepareDestination
Buffer too small (%zu) for file (%u)
Hit fatal error: %s reason: %s
%s::%s: failed to read ACK for BROM_CMD_FLB_LOAD_BL\n
%s::%s: Boot logger is gone\n
Cellular1,HardwareConfigLockOverride
Failed on closing a file (%s).\n
CommCenter
[\\.\\*\\+\\?\\^\\$\\(\\)\\[\\]\\{\\}\\|\\\\]
re-personalize\n
%s::%s: failed to read ACK for PL_CMD_RECV_DDR\n
/usr/standalone/firmware/Baseband/
Clear Bootstrap eSIM Preferences
malloc failed for proc list
%s::%s: invalid diagnostics path\n
BB ping return status: %s\n
DaleController_Loader
/private/var/wireless/Library/Logs/AppleBasebandManager/CoreDump.scratch
%s::%s: Unsupported data class.\n
enable-auth-debug
AMFDRSealingMapVerifyAndCommitSealedData
%s::%s: failed to create loader object\n
UpdateMain
%s::%s: Failed to get prov manifest\n
%s::%s: new ddr data size: %u\n
Failed parsing image end command
%s::%s: Current IMEI SVN: %d\n
==== eUICC Source ====\n
Fusing check
Tag (
missing parameter
Failed sending MRC training start in mrcFastboot, bytesSent = %u
%2E
pingdelay
%s::%s: >>send PL_CMD_RECV_DDR\n
Fail to collect coredump after hitting fatal error: %s
isPtImageVersionHigher
Fail to start kernelControl\n
%s::%s: Null root manifest\n
DaleController
%s::%s: Failed to get bootNonceHash0 (ret: 0x%08x)\n
crashBaseband
Fail to getProvisioningStatus
dynamic.nvm
%s::%s: invalid provisioning manifest image\n
/bbfs/
step
stateFusing
Checking against process %s\n
Malloc failed for APTicket content.
Loaded RestorePSI2\n
Cellular2,HardwareConfigLockOverride
%s::%s: failed to get board params\n
bbcfg_hdr.bin
fusingprogram.plist
Assertion failure ( ret == static_cast<SInt32>( amount ) )
Baseband indicating EFS erase:  %s
%s::%s: Cold resetting baseband...\n
%s::%s: <<rcv FLB_MSG_GET_HW_INFO ACK\n
%s::%s: ETHER_MAC:%s\n
SyncFile
euiccData.Valid()
Assertion failure ( !fQuickStepInProgress )
%s::%s: Failed to obtain the personalized FW base path from MSU\n
Failed to change file (%s) owner: %s\n
Failed FS flush\n
%s::%s: failed to read ACK for PL_CMD_RECV_HW_INFO\n
Loading second stage bootloader
0123456789abcdef
   CertHash: %s
%s::%s: BTI stage: failed to obtain FTAB sub-mapping containing up to the end of iBoot\n
ari
EncryptedSessionKey
Failed to handle post processing request\n
%s::%s: firmware directory does not exist (%s)\n
kBBUReturnNotPermitted
BBUFSServer timeout waiting for file (%s) transfer to complete\n
%s::%s: failed to create system bundle image\n
%s::%s: Missing output prov info dict parameter\n
Instructions
FTAB ChipID {:x} does not match actual ChipID {:x}. Please restore with an FTAB that matches your baseband chipset.
CopyIdentifier
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Protocol/ICE/BBUICE18Programmer.cpp
%s::%s: failed to create crash reason file\n
NVSerialNumber
Loaded XBLs\n
%s::%s: Failed to set NV items to %s\n
failed acknowledging update\n
failed parsing baseband config
{unordered_map<std::string, std::string, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::string>>>={__hash_table<std::__hash_value_type<std::string, std::string>, std::__unordered_map_has
PCI-EVENT: pci error: 
Baseband firmware version: %s (%u)
baseband provisioning is not requested\n
pushImagesInternal ret status is %d: %s\n
eUICCVinylValve
   PUBLIC_KEY_HASH: %s
%u.%03u: %s: %u%s\n
AMFDRSealingMapVerifySealing
2
BBUFileDataSource
%s::%s: getting boot mode...\n
%s::%s: >>send ddr image size: %zu\n
BbProvisioningEnable
EUICCCSN
DevCfg image missing\n
kBBUReturnIOError
failed creating done command\n
handleRTIClientNVRAMFile
Perform Next Stage
%s::%s: Failed to find matching service for BB Control\n
%s::%s: BTI stage: 4K-aligned total sub-mapping size: %zu\n
Assertion failure ( tmp && \"Failed to create dictionary for updating provisioning parameters.\" )
ff_first_stage
%s::%s: The IMEI SVN (%d) is outside of valid range\n
bbpc string check: %d
Failed to copy the array\n
Loaded DEVCFG\n
kBBUReturnProgrammerConnectionError
%s::%s: Failed to initialize base restore object\n
%s::%s: Failed to create data from NVM file %s\n
GetRecoveryForMac: %s\n
createImage_BBCfgSegment
EUICCTicketVersion
%s::%s: Setting B64_SESS_KEY failed\n
Failed creating CFURLRef for %s while restoring baseband migration data
%s::%s: Skipping cold reset for ConfigSim\n
%s::%s: >>send bundle image\n
kBBUReturnBinaryImageError
loader_version 0x%s key_id 0x%s perso %d\n
%s::%s: Baseband ECID is not in expected data format.\n
a pointer
failed creating reference to fdr\n
%s::%s: BasebandUpdater unsupported command: %s\n
CertID
kBBUReturnMDMDDRImageError
bbticket
Failed to allocate space for manifest_status\n
PINTO_MAC
Assertion failure ( loadEBLImage() && \"Error: Failed to load the EBL image!\" )
failed sending image in CoreDump\n
    coredump_supported:   %s
debug-uarts
AMFDRSealingMapGetEntry
%s::%s: failed to read ACK for PL_CMD_RECV_FASTBOOT_STATUS\n
auto-boot='1', bootdelay='0', host-env='0', 
vector
provisionBaseband
boost::bad_format_string: format-string is ill-formed
Failed parsing maverick hash query results\n
%s::%s: verify ddr data status: 0x%x\n
StageContext::SkipPersonalize
failed to copy programmer data from data source; not all of programmer data was copied\n
Failed to retrieve mature provisioning parameters
%s::%s: Failed to get board params (%d)\n
%s::%s: failed to add entitlements to the output dictionary\n
Assertion failure ( false && \"Invalid radio type: Specified radio does not have a XBL Support file.\" )
There are %zu processes\n
chipID
%s::%s: failed to get buffer constraints from kernel\n
Failed to send PSI!
createIMEIFromString
%s::%s: Unexpected baseband ImageTransferSegmentSize option CF type\n
Fusing Source had read once
BasebandUpdater unsupported command: 
Cellular2,SecurityDomain
Assertion failure ( fBasebandController )
PAC
%s::%s: >>send bbcfg segment size: %zu\n
did not find any backup\n
chip_id 0x%x stream_apdu_max_apdus 0x%x isAbsentOk: %s\n
onlyPerso     
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Updater/Eureka/BBUEUR25UpdateSource.cpp
%s::%s: verifying fastboot status...\n
DaleTransport_BootLoader
%s::%s: Setting no-timeout to %d from options\n
%s::%s: warm-resetting baseband...\n
%s::%s: >>send PL_CMD_RECV_BOOT_MODE\n
%s::%s: skip sending nvram image (index: %u)\n
MRC data doesn't exist or is invalid size - training fresh data
%2C
EraseEFS
%s::%s: failed to write DALE_PL_CMD_RECV_BB_CAPABILITES\n
v16@?0^{?=I[64c][64c][256c]}8
booted
EBL (%s) not found in item list!
waitForReady
delegate_debug_flags
getIMEISinope
%s::%s: failed to write PL_CMD_RECV_READ_PUBK_HASH\n
%s::%s: NerdOS second query - simply gather baseband info from ROM without a nonce\n
>
Failed preparing fs sync parameters\n
%s::%s: tempData is NULL\n
PRODUCT
%s::%s: <<rcv status\n
Resetting modem: %s\n
handleRTIClientNVMFile
%s::%s: Failed to set IMEI SVN to %d\n
%s::%s: Proxy Aborted? %d\n
Assertion failure ( fZipFile && \"Firmware data source error!\" )
Found secure manifest in response: 
%s::%s: Erasing baseband file system at path: %s\n
%s::%s: failed to read rsp for FLB_MSG_ACK_BIN_BODY\n
Cellular2,iBSS
fControlObj->start()
failed reading pkhash from booted baseband over KTL
Failed disconnecting programmer 
no response from baseband after segment transfer\n
Assertion failure ( false && \"Invalid radio type: Specified radio does not have a AOPDevCfg file.\" )
sRegister
Qdsp6SwDtbs image missing\n
%s::%s: setting RGN failed\n
%s::%s: Found the fact ack key hash in restore options\n
%s::%s: Bypassing baseband file system sync based on updater debug args\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Initialization/Eureka/BBUEURInitializer.cpp
cps
%3E
Update
Calibration enabled flag: %d
%lx+%lx
EUICCFirmwareLoaderVersion
Using the new FDR flow
%s::%s: collecting coredump...\n
%s::%s: Could not create the FDR file path URL\n
%s::%s: image source for %s is not a file (%s)\n
MRC data not accepted
failed to create dump path
~DaleBootLogger
%s::%s: Failed to get NV items settings from the baseband\n
vinyl
%s/Perso-%02d-%s
Getting manifest information from BB
logmask
%s::%s: invalid bundle image\n
DR_Success == ret
SWTrap
Bad ELF format
Assertion failure ( ( DR_Success == ret ) && \"Invalid input Firmware.\" )
WIFI_MAC2
02:88:88:88:88:88
%s::%s: Failed to get transport debug info\n
%s::%s: [PL normal boot] timeout on pl log\n
%s::%s: copy prov key hash returned null data\n
kBBUReturnTelephonyUtilReadError
Could not verify that FTAB baseband ChipID matches actual baseband ChipID; 
an integer
%s::%s: Failed to load image on iBoot preFirmware boot stage\n
IMEI2: %s
enabling kernel IPC log\n
%s::%s: invalid magic number 0x%x\n
%s::%s: failed to write bbticket\n
%s::%s: failed to get uid/gid for wireless\n
located
FirmwareLoaderVersion
INTStateMachineSetConfig
BBUError
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/FirmwareVersion/Common/BBUFirmwareVersion.cpp
InRecoveryOS: %d\n
%s::%s: failed to read ACK for DALE_PL_CMD_RECV_BB_CAPABILITES\n
BBUFSServerStart
%s::%s: Invalid NV items setting returned by the baseband: NVM(%u), EEPROM(%u)\n
%s::%s: String conversion failed\n
%s::%s: copy prov key hash failed\n
%s::%s: Unexpected no timeout setting type\n
nvrm
createPostBodyFromDictionary
fControlObj
Succeeded to perform fusing with %d trials\n
Failed to create personalization parameters dictionary
PAC: Set kAMFDROptionCopyAllowUnsealed: %s\n
kBBUReturnAlreadyStarted
saved MRC data
sec.elf SHA-384: %s\n
%s::%s: failed to verify fdr image path\n
BBUFSServer failed to create file (%s) and/or set owner\n
All Preferences
%s::%s: unsupported operation\n
MigrationData
kBBUReturnBBInitStatusTimeout
%s::%s: RootManifest post_signed_section: \n
delta
Program header entries %u\n
Cellular2,ProvisioningFirmware
Sending PSI enhanced command 'Start MRC Training'
EUICC but MG has no ChipID?
.bin
!GET_RSP_FIELD(rsp, result_t4)
psi_ram2.bin
INTStateMachinePerformSnapshot
saveNVRAMFile
getACIPCMatchingDict
ACDB
%s::%s: Reverse proxy setup successful\n
vinylValve
%s::%s: failed to create ddr image\n
No root manifest present
Timeout on waiting for BB Init status\n
verifyFusing
begin token index is larger than end token index.
%s::%s: invalid (missing) image source for %s\n
%7B
Fail to create transport %s\n
initBBUCapabilities
%s::%s: failed to send bbcfg hash-table image\n
CopyAllowUnsealed
%s::%s: ======== COREDUMP: ENTERING IBOOT FIRMWARE BOOT STAGE ========\n
\\
%s::%s: Both user and default nvram item lists are empty - this should not happens\n
%s::%s: Failed to open transport\n
%s::%s: No need to update the IMEI SVN since the current value is already %d\n
Failed training, failing program
%s::%s: Skipping safe warm reset for ConfigSim\n
%s::%s: <<rcv fast-boot status\n
%s::%s: invalid bbticket size\n
Cellular2,BbActivationBypassEnable
|
Assertion failure ( fDataSource )
json.util
entering %s
crash_in_crash
%s backup present, restoring\n
Perform internal manifest check\n
handle_signals
Failed setting config '%s' to '%d'\n
%s: could not set Telephony HW model with %s\n
com.apple.telephony.baseband
%s::%s: NULL output param\n
Switch from file %s to %s\n
%s::%s: Unexpected crash context data type\n
%s::%s: Data for %s does not exist, returning zero size ACFUDataContainer\n
Entering cmdCopyIdentifier\n
%s::%s: failed to read nonce\n
BootMode
coreDumpReason
%s::%s: failed to set device config\n
Running secure mode
%s::%s: invalid nonce size; expected: %u, received: %u\n
InstallTicket failed to get desired response\n
BBUFSServer failed to perform snapshot: sTransferFile failed\n
BBUFSServer successfully created filer read session with ID (%llu)\n
handleCertification
failed establish connection to FDR\n
%25
 in 
%s::%s: failed to process ddr\n
Failed sending PSI command for Loading EBL\n
%s::%s: BTI stage: failed to get the iBoot size from the FW\n
%s::%s: imei tempData is null\n
SBL1_HASH
pingCmd
fakefuse
fusingState: %d
HelloWaitTimeoutSec
Assertion failure ( fEBLImage == __null )
%s::%s: unexpected core dump reason type\n
 ,PMStatus=
%s::%s: BT_MAC:%s\n
status
kBBUReturnFailedSetSVN
Resuming Maverick Protocol
%s::%s: Failed to create timer object\n
%s::%s: Error: BBUFSServer failed to set config %s\n
%s::%s: Baseband chip revision %s is not supported by the baseband firmware\n
%s::%s: failed to read ACK for PL_CMD_SEND_DDR\n
Fatal error in FDR data validation/decode \n
Supported Bootloader Versions success %d ret { %s }\n
Fail to create transport: 
Success!\n
failed reading hash query results\n
copy_mac_address_existence
successfully switched Sahara mode to ETLSAHModePending\n
logLevel
failed createing maverick root manifest response\n
Proxy Available!\n
%s::%s: Failed to collect coredump (ACFU error code = %d)\n
Failed to get MEID.
goldFW
%s::%s: failed to convert imei to data\n
hw.target
%s::%s: failed to read status after sending calibration image\n
file not found after creating %s\n
Not in restore mode - skipping gathering Personalization parameters...
Failed to create backup directory\n
AMFDRDataPutForSysCfgKey
Requested to sync static\n
%s::%s: Could not extract core dump reason\n
The argument index starts with an invalid character
Sending EBL length packet (%d bytes)
Sent Manifest with length %u Hash %s
Cellular1,BoardID
updateSource
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Feedback/BBUConsoleFeedback.cpp
Cellular2,iBootData
kBBUReturnFailedStartProvisioning
Sent Manifest with length %u SHA256 Hash %s
failed handling sahara mode operation
bootargs
%s::%s: failed to create provisioning manifest image\n
sendImage_Nvram
EnablePing
%s::%s: Total transferred bytes %llu\n
%s::%s: ======== COMPLETED FIRST BOOT STAGE (ROM) ========\n
collectCoredump
Assertion failure ( ret == kBBUReturnSuccess && \"Failed overriding preflight personalization parameters.\" )
Baseband chip revision 
%Y-%m-%d-%H-%M-%S
%s::%s: Could not create BasebandUpdaterTransport\n
%s::%s: Failed to encode reset reason, so crashing baseband with SPMI without specifying reason\n
RegionInfo
%s::%s: Found the APTicket key in updater options\n
%s::%s: Baseband boot failed (ACFU error code = %d)\n
a bool
%s::%s: Retrieved personalization parameters for preflight successfully\n
failed getting nonce\n
MEID is valid. Populating provisioning params!
Invalid start packet recieved from EBL.\n
Nothing to backup: file (%s) does not exist\n
Assertion failure ( fOutput )
%s::%s: setting VERSION failed\n
BBUEUR20Fusing
ManifestInfo
%s::%s: failed to write PL_CMD_RECV_DDR\n
saving file %u to %s, offset %u, size %u\n
ELF CALLOC HDR
%s::%s: pre-assigned buffer # %u of size %u KB to fetch logs\n
sUpdateAck
%s::%s: invalid data\n
BasebandFirmware
%s::%s: Reading oem mrdump command response\n
bootCmd
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Images/Eureka/MultiImage/BBUEURMIImage.cpp
failed receiving done response\n
   CertID: %u
DebugArgs
stateBooting
Assertion failure ( success && \"Failed to initialize ring buffer.\" )
requirePartitionMountsCmd
Booted for coredump, not programming firmware
%s::%s: snapshot completion received (flush completion with null-log)\n
Cold reset
Failed to push images: 
Gold FW Macs already matching (no forceGold)\n
%s::%s: successfully sent nvram image (index: %u)\n
sCompleteTransfer
%s::%s: Failed GetRandomNum ARI command\n
Failed to retrieve mature provisioning parameters.
CHIPID=0x%x, SNUM=0x%s, PKHASH=0x%s, CERTID=0x%x\n
%s::%s: Failed to cold reset baseband\n
Main FW versions already matching (no forceMain)\n
OEMMisc image missing\n
Loaded AOPDevCfg\n
Assertion failure ( fSBLImage && \"Failed loading SBL image for creating hash.\" )
%s::%s: Failed to create debug value\n
bootcmd
AMFDRGetCert
lke
%s::%s: failed to read ACK for DALE_PL_CMD_SEND_BBCFG_HASH_TABLE\n
%s::%s: Attempting to set IMEI SVN to %d\n
Assertion failure ( ( amountRead == sizeof( e_ident ) ) && \"Copied data size mismatch: Failed to copy ELF header identity from data source.\" )
Assertion failure ( (ret == kBBUReturnSuccess) && \"Failed to copy NVM image payload data to buffer!\" )
ProvisionedInfo
%s::%s: NVRAM data creation failed, null nv data\n
%s::%s: null input firmware\n
kBBUReturnBadManifestStatus
BBUFSServer
dbguarts
Loaded Qdsp6SwDtbs\n
SerialNumber
Fail to run collectCoreDump
Assertion failure ( fSignedFirmwareSOCViewImage && \"Failed loading SignedFirmwareSOCView image for creating hash.\" )
getBootMode
%s::%s: failed to send bbcfg segment data\n
%s::%s: Result %d code %d raw_error %ld error %s\n\n
%s::%s: Only applicable when debug args is set to pcie\n
createImage_Calibration
%s::%s: read logs completion of size %zu bytes\n
lpc_reg
%s::%s: >>send bbcfg hash-table\n
Loaded NVM file %s\n
Failed sending EBL
plistRef
libBBUpdaterExtreme
DATA
Error: failed to SwitchCardMode\n
Failed to get EID - Adc config mismatch
last readLogBlock callback\n
sCreateFilerSession
mainFW
%s::%s: sending device config...\n
%s::%s: Collecting coredump...\n
success
Ret %d from state %s next %s\n
%s::%s: boot logger transport not exist\n
pushFirmware
%s::%s: failed re-assigning new buffer of size %zu KB to fetch logs (error [0x%x])\n
Assertion failure ( fSBLImage == __null )
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Protocol/Common/BBUFusing.cpp
%s::%s: Image external to FTAB requested: %s.\n
%s::%s: Failed to get PRP\n
Detect as unfused BB\n
%s::%s: rsp.m_u.m_bin_header.m_checksum:0x%x\n
%s::%s: failed to write dev-cfg\n
failed to switch mode\n
Could not load NVRAM? %d\n
%s::%s: failed to convert value to c-string\n
AuthenticatePersoDeviceRequest.bin
/AppleInternal/Library/BuildRoots/4~CatVugAVHlPmCykG3u5RYNuSUaO3iPS0fZcrWSs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h
%s::%s: NULL options param\n
Sending Images
Cellular1,L1CL1S
BBUFSServer transferring file (%s) to path (%s)\n
Product Type : %d and Hardware Config: 0x%x in Reserved%lu\n
startLogging_block_invoke
Cellular2,ECID
Failed to change file ownership
%s::%s: failed to write BROM_CMD_FLB_GET_EFUSE_PUBLIC\n
failed creating ETL header and ring buffer structures\n
sDeRegister
%s::%s: Default NVRAM items for commcenter/basebandd: %s\n
%s::%s: failed to create coredump path ref\n
FusingStatus
Loaded download file '%s'\n
Hello reserved fields:  %s\n
General Error
Failed to create the directory\n
Fail to send %s !\n
%s::%s: check status info for FLB_MSG_BIN_BODY_STATUS failed\n
BT_MAC2
Assertion failure ( fRestorePSIRam2Source == __null )
coredump
    power_sequence_index: 0x%04x
%s::%s: Full ftab chipID string: %s\n
%s::%s: Error: BBUFSServer stopped during flush\n
BasebandNVRAM
Assertion failure ( ( ret == kBBUReturnSuccess ) && \"Failed to copy ELF header identity from data source.\" )
DIAG crash command sent
ret != kBBUReturnSuccess
BasebandHardwareConfigLockOverride
ValidatePersoDeviceRequest.bin
(%s:%d) Array assignment too large(%p), got(%zu) max(%zu)
%s::%s: Unknown transport type\n
Command
Nonce
setDeviceConfig
ctxt
Parsing failed, ret = %s\n
\\$&
ExtendedLOMMacAddress
BBUFSServerCreate
kBBUReturnFailedFinishProvisioning
INTStateMachineSetConfigDefaults
%s::%s: User defined NVRAM items: %s\n
%s::%s: Found defaults write data for daemon NvramItems. Consuming it.\n
Assertion failure ( fLoader && \"Failed to reset and create BBULoader.\" )
stateManifestCheck
Get Records
%s::%s: Bypassing baseband file system sync based on updater options\n
Sent read data at offset 0x%08x, chunk %u\n
%s::%s: [Boot Logger UART] Stopping PL/LK log\n
%s::%s: failed to create boot timer\n
dmfl:tnp:iuseb:o:
EUICCCertIdentifier
sendProvisionPing
sendImage_Calibration
Null output ptr
TransferFile
%s::%s: Invalid coredump path\n
PCI-EVENT: pci error: .*
failed sending root manifest data\n
kBBUReturnUnPersonalizedImageError
sPrintHelloParameters
%s::%s: getting board parameters (loader)...\n
Failed to run ETLFusingGetSecureState()\n
too many retries: %u\n
setPreflightMode
Failed to get fusing profile from the plist\n
%s::%s: rootManifestSigCert CFDataCreate error.\n
File    
FastbootTuningOK
sec.elf
%s::%s: IMEI2 data processing returned null data\n
%s::%s: Postdata created.\n
AuthenticatePersoDevice %d\n
%s::%s: Enabling Baseband certification\n
Resetting baseband 
FDR TrustError: %llu\n
stop
StageContext::Coredump
Receiving DDR Cal Data...\n
FirmwarePreflightInfo
Failed to create BasebandUpdater instance
failed connecting to sahara
rsp
%s::%s: IMEI2 data processing failed\n
SyncStatic
%s::%s: Failed to create Baseband Firmware override key path\n
%s::%s: Failed to send get manifest status command\n
%s::%s: RootManifest: \n
warmReset
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Images/ICE/BBUICEDownloadImage.cpp
second sysctl() failed with err = %d
Load PT from MobileAsset\n
XBLsc
%s::%s: invalid ACK for DALE_PL_CMD_SEND_BBCFG_SEGMENT\n
ForceSync
%s::%s: Failed to allocate BasebandRestore object\n
CFDictionaryGetTypeID() == CFGetTypeID(plistRef.get())
DeleteProfile failed, error %d status %hhu sw1 0x%x sw2 0x%x\n
%s::%s: NULL input param\n
%s::%s: Baseband ECID is missing.\n
%s::%s: Merge default NVRAM items for restore with the above user defined NVRAM items.\n
Assertion failure ( fImage && \"Failed to to create BBU Image for the programmer item!\" )
Assertion failure ( copied == rootManifestSize && \"failed copying root manifest to buffer\" )
getWirelessID
%s::%s: Invalid chipId\n
%s::%s: Received the response from server - parse it\n
Assertion failure ( i != fFileMap.end() )
BBUEnvironment
%s::%s: Setting kProvB64_IMEI2 failed\n
boot-pcie.log
%s::%s: Beginning IMEI SVN check and update (will attempt to set SVN to %d)\n
Assertion failure ( (amountCopied == amount) && \"Copied data size mismatch: Failed to copy binary image payload data to buffer!\" )
%s::%s: Invalid productionMode\n
SHA384 detected\n
StageContext::CheckManifest
Waiting for PSI command response\n
off
%s::%s: Failed to create matching dictionary\n
Assertion failure ( success && \"Failed to get the gold loader version from Gold FW.\" )
Failed to get sec.elf in CFDataRef type
respDataPayload
hasManifestSource() = %d, personalize = %d\n
Assertion failure ( fRestoreXBLscImage == __null )
%s::%s: Received Response Data: %s\n
%s::%s: invalid ACK (0x%x) for PL_CMD_RECV_EXCEPTION_REASON\n
BBUEUR20UpdateSource::saveImages\n
%s::%s: Baseband chipID data conversion failed\n
The root cause of the AMFDR failure is NOT missing bbxx file \n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Personalization/Eureka/BBUEURPersonalizationParameters.cpp
%s::%s: Unexpected acipc boot stage\n
failed sending root manifest data
Invalid path pointer to create coredump directory
too many repersonalizations
kBBUReturnPingtimeout
item not found in item list\n
LAI prov info to be returned to PR: 
DataInstance: %s\n
failed creating directory\n
%s::%s: invalid loader image data\n
kBBUNVRestoreSettingFATP
_wireless
safe-timer
recv
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Images/Common/BBUELF.cpp
Loaded APPS\n
DE:AD:BE:FF:00:00
\tDescription: '%s', Filename '%s'
failed to set config, unrecognized config name '%s'\n
BBUFSServer stopped successfully\n
%08zu
%s::%s: failed to write payload data\n
%s::%s: >>send bbcfg segment\n
unknown state\n
Unrecognized radio type!
%s::%s: failed to abort with force-warm-reset, aborting via cold-reset\n
/report.json
%s%s\n
%s::%s: failed to init firmware object\n
%s::%s: verifying dynamic image path... (%s)\n
Hash missing in BBFW: %s
Done executing kETLSAHGetCommandsID, received: %s
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Protocol/ICE/BBUICE16Programmer.cpp
MSU based APTicket Raw Path: \"%s\"
is
 [
%s::%s: Failed to create ACFUDataContainer for crash context data: %s\n
%s::%s: failed to get boot mode\n
%s::%s: Retrieved personalization parameters for live boot successfully\n
stateCoredump
%s::%s: type: '%s'\n
kBBUReturnAllocationFailed
Sending restore mode cookie in Reserved%lu\n
Fail to ping in manifest check: 
fuseAttemptSucceeded
parseDebugArgs
Failed on getting file status from (%s) \n
Baseband crashed during ping\n
BBCfg image missing\n
populateRequestDictionary
Miss image for collecting coredump
%s::%s: failed to read status\n
No
failed copying root manifest to buffer\n
w
warmResetSafe
verbosity
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Support/BBULogIOABP.cpp
%s::%s: Returned null provisioned info\n
failed receiving debug table\n
End of input while parsing an argument index
BBUpdaterCommon
%s::%s: failed to read coredump chunk\n
XBLsc image missing\n
supports.fs
%s: (%s) length=%u bytes\n
%s::%s: pipe context is null in flush callback\n
%s::%s: >>send calibration image size (%zu)\n
Enabled 
%s::%s: Failed to create ACFUDataContainer for NVM file %s\n
Not stripping Cal FDR Data on AP\n
boot-script
%s::%s: BasebandRestore object is no longer available. Should never happen.\n
AMFDRSetRecoveryVerifier
Baseband
%s::%s: >>send DALE_CMD_SEND_PROVISIONING_MANIFEST\n
Deserialized plist data is not a dictionary: %s\n
sim_state 0x%x, sim_error_cause 0x%x\n
verifyDefaultPath_Firmware
authdbg
%3A
PairedWithSecondaryTarget
%s::%s: Failed to parse baseband firmware recipe info, so skipping chip-revision/firmware-recipe check\n
alderHost     
start
kBBUReturnAPTicketReadContentFailed
%s::%s: [Boot Logger UART] Stopping rom log\n
Cellular1,BbFATPCalibrationEnable
PL
Failed saving images 
Assertion failure ( fAcdbImage && \"Failed loading ACDB image for creating hash.\" )
\n%s\n
%s::%s: >>send nvram index\n
result %d code %d raw_error %ld error %s\n
EURStateMachinePerformFlush
%s::%s: Using MobileAsset path: %s\n
Assertion failure ( ( e_ident[EI_DATA] == kELFData2LSB ) && \"ELF header identity (endianness) mismatch.\" )
EthernetMacAddress
...waiting patiently for reset\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Updater/Common/BBUStages.cpp
Cellular2,FDRAllowUnsealed
%s::%s: bver data returned has a length of 0, so skipping FTAB chipID check\n
true
EURStateMachineSetConfig
%s::%s: Failed to create debug log path override object\n
Failed image download
DaleCommon
%s::%s: Failed to write NVM file %s while restoring baseband migration data\n
]
signature
%s: restoring migration data
%s::%s: Append fact act key hash to request\n
CFDataGetTypeID() == CFGetTypeID(fwMacData)
%s::%s: poststring creation failed\n
%s::%s: invalid hw info size\n
%s::%s: Incorrect root manifest size: %ld\n
BbRequestEntries
Cellular2,CdpHost
%s::%s: invalid ACK (0x%x) for DALE_PL_CMD_RECV_BB_CAPABILITES\n
ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\([a-zA-Z\\.]+\\) [0-9a-zA-Z]+\\([0-9]+-|\\).*
ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\([a-zA-Z\\.]+\\) [0-9a-zA-Z]+\\([0-9]+-[0-9a-fA-F]+\\) SZ\\([0-9]+\\) TRX\\(0x[0-9a-f]+\\) AP\\.SEQ\\(|\\).*
pt.mbn
WifiAddress
%s::%s: Failed to create personalization parameters dictionary\n
Failed formatting PSI enhanced command to retrieve personalization info\n
Fail to get update source in 
copyResponse
%s::%s: Base64 decode failed\n
baseband alive detected\n
backupFile
No MRC image in programmer list
Boot Logger ROM
Assertion failure ( folder.empty() != true && \"Failed finding the bbfw path.\" )
eUICCStateMachine
%s::%s: decodedData is NULL\n
generating empty file for %s with size %u
outPlist
BB Init status: not ready\n
%s: The LSB of the Plist (0x%08X) is not matched with the LSB of the fusing data from the BB (0x%08X) at the address (0x%08X)\n
fusingSource
apTicket
Decode 2nd tag failure with der return: %d, decoded tag: %llu\n
kBBUReturnFailCreateTransportBooted
BasebandUpdaterObj
demote-prod-non-persistent
%s::%s: assigned null-buffer to trigger snapshot\n
BasebandProvisioningLineType
???
ACFUFirmware
setOptions
com.apple.ARITransport
%s::%s: failed to read ACK for PL_CMD_SEND_BUNDLE_IMG\n
handleRTIClientImage
Assertion failure ( fProvisionState.requested && \"Failed to request provision state.\" )
failed saving record\n
kBBUReturnGetEIDFailure
%s::%s: using data source for image %s\n
Updating provisioning parameters from BB
%s::%s: Failed to assign output data\n
r
%sEND%s: %s\n
%s::%s: failed to read ACK for PL_CMD_RECV_READ_PUBK_HASH\n
BBUpdateProgress
ExceptionDump
IMEI-SVN Check and Update: %d
v24@?0^{?=^vQQQ}8r^{ETLSAHDebugDataFieldRecord64Bit_t=QQQ[20c][20c]}16
%s::%s: Preparing BBUFSServer with path: %s\n
%s::%s: Retrieved IMEI SV of %d from the restore options\n
Backup directory path (%s) exists but is not a directory\n
%s::%s: failed to create coredump timer\n
marp
CurrentQueue
failed preparing filesystem after erase\n
Sending EBL without xor\n
Failed to receive Start packet from EBL.\n
registerWithKernel_sync
Failed performing fusing. Retry: 
Failed to deserialize dictionary %s error %s\n
Assertion failure ( buf->size )
Failed executing secure mode
BBUCFDataDataSource
Detect as fused BB\n
%s::%s: m_io_code2 status error: 0x%x\n
ShutdownSync
%s::%s: failed to create a directory at fdr image path (%s)\n
Emergency
Loader
queryCmd
Assertion failure ( loadBINFiles() && \"Error: Failed to load the BIN image!\" )
%s::%s: loader image size: %zu\n
%s::%s: failed to cast ddr image\n
%s::%s: skip sending calibration image\n
aborting pending reads\n
kBBUReturnGetKeyStatusFailure
:
reset
Cellular1,ProvisioningFirmware
bbpc
CreateValidationBlob DR %d\n
ff_create_transport
Cellular1,CdpAscUl
kBBUReturnInvalidTransportType
%s::%s: Baseband NVRAM parsing failed for user provided nvram list (%d)\n
In restoreOS?: Bool = %d
%s::%s: sending loader...\n
createImage_DDR
EBL length ack unsuccessful: %u\n
HW Failure
RootManifest decode error during FDR data parsing\n
%s::%s: Bad bootNonceHash size %u\n
%60
/dev/tty.baseband-boot-logger
%s::%s: failed to create MobileAsset power table image\n
%qx
Failed disconnecting for image\n
%s::%s: Boot command success\n
%s::%s: check status info for FLB_MSG_ACK_ROOT_PUBK_HASH failed\n
DR_Success == der_ret && TAG_PILR == dec.tag
Failed to create fusing dictionary from the plist\n
Bailing on eUICC error due to status %u\n
Failed to create data source from fresh scratch file %s (%d)
kBBUReturnBBTicketDERParseErrorForCal
BasebandCoredump
Loaded file '%s'\n
clearBackupFile
%s::%s: firmware path is not a directory (%s)\n
%s::%s: ======== COMPLETED IBOOT FW STAGE ========\n
PostProcess
failed creating transport with fd %i\n
airship.io
%s::%s: The IMEI SVN is invalid\n
Assertion failure ( fProgrammerDataSource.get() && \"Failed creating data source from data for programmer\" )
%sBEGIN: %s\n
!url.empty() && urlRef
%s::%s: snapshot received (flush completion with null-log)\n
%s::%s: non-zero response status\n
Assertion failure ( !fLongStepInProgress )
%s::%s: Failed BBUFSServer prepare for RTI NVM download\n
%s::%s: Failed to create final nvram CFString for sticky nvram plist file\n
Reading file '
Failed receiving personalization parameters from device\n
%s::%s: Failed to obtain the default personalized FW base path\n
ELF READFILE TO STOR
saveNewDataToFile
BBUICE16Communication
failed reading hash results
Now, set the options for the libFDR API (either legacy or new API function)
RootManifest decode error during FATPCalibEnable FDR data parsing\n
xbl_support.elf
Cellular2,PMUFW2
%s::%s: >>send  power table\n
Unable to remove Firmware image [%s]. Error[%d][%s]\n
ucs_crash_id
Using manual argument numbering in automatic argument numbering mode
%s::%s: failed to create bbcfg hash table image\n
kBBUReturnGetEIDFailureAdcMismatch
bringup
File size is %u\n
SendReceiptServerResponse.plist
%s::%s: failed to allocate output dictionary\n
BasebandEnableActivationBypass
%s::%s: Failed to execute command: %s\n
ClassIdentifier in error: %s\n
Bad argument
failed reading chipid from booted baseband over KTL
profile
%s::%s: Received Response Code: %d\n
Only applied when debug args is set to pcie
%s::%s: Baseband NVRAM data conversion failed (%d)\n
Assertion failure ( fXBLscImage && \"Failed loading XBLsc image for creating hash.\" )
BBUDerHelpers
FDR failure we hit is: %s \n
copyBasebandMigrationData
Loaded HYP\n
STATUS
firmwareSaveFolder
createImage_Loader
(
shouldPerformFusingVerification: it is not Resotre OS!\n
SHRM
%s::%s: B64_SECDATA found in response\n
GetNonceServer %d\n
%s::%s: -------- BOOT --------\n
NULL updater argument
%s::%s: using file source for image %s\n
   PUBLIC_KEY_HASH: 0x%s
root manifest larger than protocol specification, size = %u bytes
%s::%s: Detected non-zero cal/prov/fac/nvm manifests status\n
%s::%s: failed to establish handshake message\n
File %s ret %d\n
%s::%s: User requested not to safe warm reset, skipping...\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/eUICC/Source/eUICCSource.cpp
AMFDRDataDelete
Fail to perform finalization.
B64_BB_CHIPID
%s::%s: Image transfer timeout on CPS stage, aborting via force warm reset\n
statePersonalizeFirst
The type option contains an invalid value for a string formatting argument
%s::%s: Mismatch - expected boot stage: %u, current boot stage: %u\n
SKeyHash
StageContext::PersonalizeStageSecond
SwitchCardMode: Baseband already in mode %hhu\n
%zu -> %s\n
COMMAND_CODE
Running eUICC\n
apduSetCount
Wrote %u bytes to %s\n
%s::%s: %s\n
%s::%s: KernelPCIRestoreTrace obj is gone\n
%s::%s: >>send PL_CMD_RECV_EXCEPTION_REASON\n
HASH
%s::%s: Failed to load image on THIRD (CPS) boot stage\n
%s::%s: failed to read device config status\n
%s::%s: failed to write PL_CMD_RECV_EXCEPTION_REASON\n
BypassNVMSync
-euiccForcePerso
%s::%s: Incorrect type for nvramOutputPath, fail.\n
%s::%s: attempting to set invalid fdr path\n
Assertion failure ( false && \"Unrecognized BBUICE Remote Data fileName.\" )
AMFDRDataCopyDigest
f.header.length <= 5 && f.data.length <= 255
Expecting %d bytes from device\n
%s::%s: fdr image path is not a directory (%s)\n
%s::%s: [pl normal boot] start logging...\n
ACIPCInterfaceProviderDevice
Failed performing fusing with %d trials\n
Update Main:Card %s Bundle %s\n
%s::%s: Failed to get reverse proxy settings\n
UniqueChipID
SendReceiptServer %d\n
kBBUNVRestoreSettingFactory
createFile
%s::%s: failed to read status (ddr data verify)\n
generating 0xFF-filled file for %s
kBBUReturnELFImageError
skipAll       
%s::%s: failed to write DALE_CMD_SEND_PROVISIONING_MANIFEST\n
kBBUNVRestoreSettingNoUpdate
Assertion failure ( fPSIRamSource == __null )
failed creating mode switch command
Sending Image '
Assertion failure ( data )
Boot Logger Transport Unknown
BBUICE16Loader
eUICC is not done yet, waiting\n
%s::%s: failed to create file object\n
main_fw_pcf_mac 0x%s gold_fw_pcf_mac 0x%s pcf_version 0x%x\n
root manifest hash data mismatches baseband hash response\n
failed handling hash response
%s::%s: Unexpected bbutil cmd setting type\n
trying to find MRC file\n
%s::%s: Failed while getting baseband prov info\n
%s::%s: failed to create loader image\n
Sent %s successfully!\n
Failed to match both plist and the fusing data\n
/var/wireless/baseband_data/bbfs/
kBBUReturnManifestStatusNonZeroError
%s::%s: Failed to create ACFUDataContainer for FDR file: %s\n
Failed to complete InitPerso command\n
%s::%s: failed to send system bundle image\n
AMFDRSealedDataPopulate
BBUFSServerParametersInit
HASH CMP
ProvisioningManifestExists
eUICC Source has no FW, ENG?\n
LINETYPE
%s::%s: could not split parameter: %s\n
%s::%s: WIFI_MAC:%s\n
%s::%s: successfully finished getting crash reason\n
%s::%s: Failed to setOptions on BasebandUpdater obj\n
kernel.pci.restore
-
error %d status 0x%hhx\n
%s::%s: failed to write PL_CMD_SEND_CAL_IMG\n
GetWrapKeyServerRequest.plist
copyDataFromHexString
%s::%s: Unsupported sikblobtype: %u\n
filesystem flush operation failed\n
%s::%s: check status info for FLB_MSG_EFUSE_PUBLIC_INFO_STATUS failed\n
%s::%s: failed to create firmware object\n
%s::%s: Warning: unable to get chip information\n
restoreBasebandMigrationData
VersionCheck
%s::%s: decode sequence failure with der return: %d, decode tag: %x\n\n
BBUFSServerPrepare
add log: data %p size %zu\n
Restoring NV items to Shipping defaults
hw.model
EFS1 image missing\n
%s::%s: fLaiProvInfo is null which means sth is wrong. Failing provisioning.\n
DaleController_BootROM
%s::%s: failed to read ACK for PL_CMD_RECV_EXCEPTION_REASON\n
Setting reset delay to %u from %u
loader
ELF READFILE PRG
  ckey_hash    [0x%02x]: %s
?
Failed creating file server\n
invalid restore xbl image\n
Creating firmware object for post sealing step with path: 
No Action
%s::%s: failed to initialize controller object\n
CommCenter-asan
%s::%s: invalid power table image\n
result  0x%x \n
Failed to get manifest status
%s::%s: Missing restore options\n
Assertion failure ( (amountCopied == amount) && \"Copied data size mismatch: Failed to copy image payload data to buffer!\" )
command
%s::%s: >>send BROM_CMD_FLB_LOAD_BL\n
com.apple.telephony.basebandservices.support
%s::%s: copy baseband prov info returned error\n
DR_Success == der_ret
downloadFusingProgramCmd
%s::%s: Did not find corresponding MobileAsset file name for 4cc tag %s\n
Finish provision failed, rsp status: 0x%x
BasebandUpdaterObjDestroy
MLBSerialNumber
failed receiving maverick end\n
boot-uart.log
%s::%s: In restoreOS: returning zero size MobileAsset file %s\n
could not find end token '|' in bver tag.
DataClass: %s, DataInstance: %s\n
%s::%s: null output dataref\n
%s::%s: failed to write FLB_MSG_LOAD_BIN_BODY\n
%s::%s: failed to save new ddr data to file\n
failed receiving baseband config
createZeroSizeContainer
ECID: 0x%llx\n
deregisterWithKernel_sync
%s::%s: Collected Sik Pub Key: \n
%s::%s: loader size greater than %d\n
deleting backup file %s\n
subsystem
%s::%s: Could not create RTKitFirmware with default FTAB path\n
%s::%s: %s: %u\n
Bypass manifest status check has been specified. Returning success
createProvSessionKeySinope
InitPersoServerResponse.plist
%s::%s: Encountered an error (%d) during NVRAM processing\n
mdmddr.mbn
%s::%s: >>send PL_CMD_RECV_HW_INFO\n
kBBUReturnSuccess
kBBUReturnInvalidProgrammerItemType
%s::%s: failed to create modem bundle image\n
InstallTicket failed error %d status %hhu sw1 0x%x sw2 0x%x\n
Assertion failure ( fPersonalizationParameters )
   SNUM: %s / CHIPID: 0x%08x
%s::%s: failed to write ddr image\n
Yes :-)
%s::%s: Failed to create ACIPC interface object\n
aop_devcfg.mbn
%s::%s: failed to get IMEIs from baseband\n
%i records requested\n
%s::%s: failed to create libtu controller\n
%s::%s: failed to decode manifest property object (status: %d)\n
Cellular2,CdpAscDl
inDict
Assertion failure ( false && \"Invalid radio type: Specified radio does not have a SignedFirmwareSOCView file.\" )
ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\([a-zA-Z\\.]+\\) [0-9a-zA-Z]+\\([0-9]+-[0-9a-fA-F]+\\) SZ\\(|\\) TRX\\(0x[0-9a-f]+\\) AP\\.SEQ\\(0x[0-9a-f]+\\).*
Resuming Secure Mode
NULL requestURL?\n
Loaded PSI2\n
returning state: %d\n
%s::%s: Coredump command success\n
rcfgbkpt
%s::%s: >>send body payload\n
SendReceiptServerRequest.plist
fail to free transport: %p\n
Assertion failure ( success )
gatherPreflightParameters
%s::%s: Require partition mounts command success\n
firmwareData
SecondaryWifiMacAddress
sendImage_Bundle
%s::%s: Failed to get coredump report (empty)\n
%s::%s: Interface added\n
%s: Good\n
AMFDRSealingMapGetEntriesForDevice
Assertion failure ( success && \"Failed to get EID.\" )
Options.plist
invalid
failed receiving debug table location\n
psiResp.param >= MRC_SINGLE_FREQ_DATA_LENGTH && psiResp.param <= MRC_MAX_DATA_LENGTH
Failed to create dictionary\n
m9kefs1
kBBUReturnBBTicketReadContentFailed
Device has no (further) updates\n
Cellular2,ChipID
Requested to sync FATP-calibration\n
kBBUReturnBadChecksum
backing up file from %s to %s\n
kBBUReturnFailedSendingImage
Fusing Source cannot be non-zipped source.\n
VinylUse4FF
\t%s: ... %0.1f%c
BasebandUpdater:
psiResp.responseCode = %d
Failed to get datadir path; error = %ld
%s::%s: -------- PROVISION COMMAND --------\n
%s::%s: required file %s (%s) has 0 bytes of size\n
rcfgbhvr
%s::%s: failed to create bbcfg segment image\n
   ChipSerialNo: %s
Fail to get update source for bootup\n
Fail to check manifest in manifest check: 
signed_firmware_soc_view.elf
Bootstrap Preferences
Failed to InitPerso status %hhu SW1 0x%x SW2 0x%x rsp_len %u\n
 on 
%s::%s: invalid ACK (0x%x) for PL_CMD_RECV_HW_INFO\n
SHA256 detected\n
%s::%s: failed to collect sik public key (%d)\n
processNVRAMItems
AMFDRCreateWithOptions
ControllerFSM_TOP
%s::%s: Failed to check baseband reset state\n
setPath_Dynamic
precoredump
GetNonce
v32@?0{pair<pci::transport::kernel::variant, unsigned int>=iI}8^v16^v24
%s::%s: Failed to create options cp\n
%s::%s:   ckey_hash    [0x%02x]: %s\n
force-ctrr-lock
Failed to create dictionary for PAC FDR options\n
%27
%s::%s: sending power table image...\n
%s::%s: User OR Sticky NVRAM {key, value} pairs:\n
finished secure mode\n
eUICCFirmwareParser
%s::%s: loading PT from MobileAsset\n
MRC data exists - fastbooting with existing data
Fail to get update source data for finalize\n
PT
%s::%s: provInfo value buffer alloc failed\n
%s::%s: [Boot Logger PCIE] Stopping PL/LK log\n
VinylClearMetadata::GetListOfIccids: Extracting Profile List\n
Overriding with preflight information:
%s::%s: Failed to insert fw version to output dictionary\n
IMEI1: %s
%s::%s: failed to send power table data size\n
VinylClearMetadata
setPath_Fdr
MRC training RspId invalid
AMFDRDataCopySslRoots
cmdCopyRequirePartitionMount
FinalizePersoDevice %d\n
Baseband config:
%s::%s: User requested not to force warm reset, skipping...\n
EID
hwType.Valid()
    bb_version_string:    %s
%s::%s: ACIPC start interface timeout\n
SKeyStatus
Fail to create transport\n
bad parameters for file server creation\n
restorepsi.bin
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Provisioning/BBUProvisioner.cpp
Assertion failure ( ( offset < getWritePayloadLength() ) && \"Error: Chunk size is not sufficient to write payload data of the EBL image.\" )
call to empty boost::function
%s::%s: invalid provisioning manifest status after pushing provisioning manifest (0x%x)\n
Failed to create hello response\n
sProcessUpdate
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Initialization/Common/BBUInitializer.cpp
%s::%s: failed to send calibration image\n
Need to free transport before creating again
Failed reading PSI command response
%s::%s: >>send PL_CMD_SEND_BUNDLE_IMG\n
Invalid GetData response from the BB\n
Failed formatting EBL Length packet\n
no-timeout
Unknown telephony radio vendor %d\n
%s::%s: Sticky NVRAM items do not exist\n
QTIMisc
%s::%s: Checking if sticky_nvram_items.plist exists in the file system\n
%s::%s: Could not create the FDR file path string\n
Failed sending EBL!
ff_ping
BBUFSServer not running\n
Detected non-zero prov manifest status: 
Failed writing to stream for restoring baseband migration data
Failed NVMSnapshot ARI cmd\n
Assertion failure ( provisioner )
PT file (MobileAsset) copied amount is wrong
ProvisionQuery
Failed to prep\n
SwitchCardMode: Failed err %d status %hhu mode %d sw1 0x%x sw2 0x%x\n
XBL_CFG
BasebandProvInfo
deleting backup file\n
Assertion failure ( fZipFile && \"BBU firmware data error.\" )
%s::%s: read logs completion failed (error [0x%x])\n
%s::%s: send device config status error (0x%x)\n
sys-bundle.img
%s::%s: ABP kernel interface started\n
%s::%s: escapedValue is NULL\n
Assertion failure ( fFeedback )
Unlinking MRC had an error %s
Assertion failure ( fProgrammer && \"No valid BBU Programmer!\" )
%s::%s: Warning: bver not found in baseband firmware, so skipping FTAB chipID check\n
Stripping and verifying PROV FDR Data on AP\n
AMFDRSealingMapCreateAndPopulateSealedData
CircularFileLogWriter
create
%s::%s: invalid ACK (0x%x) for BROM_CMD_FLB_GET_EFUSE_PUBLIC\n
Loaded QTIMisc\n
failed removing old file %s\n
kBBUReturnSuccess == r && installData
Assertion failure ( !fConnected && \"Cannot finish connection, since BBU programmer is already (falsely) recognized as connected!\" )
AMFDRSealedDataCreateSealingRequest
cpucp.elf
Loaded SHRM\n
---------------------%s---------------------\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Personalization/ICE/BBUICEPersonalizationParameters.cpp
Will provision
Assertion failure ( ( !fFirmwareFolder.empty() || fZipFile ) && \"Firmware data source error!\" )
Failed preparing baseband filesystem directory for copying baseband migration data
Cellular1,BbCalibrationEnable
%s::%s: cold-resetting baseband...\n
SWID Mismatch
Assertion failure ( transport && \"BBU telephony util transport error.\" )
%s::%s: UART can only be open in restored environment. If you wish to open UART in OS mode, please open through nanokdp\n
Failed to create transport
queryInfoFirstStageInternal ret status is %d
performCoreDump
%s::%s: USB_ETHER_MAC:%s\n
now in %s
kBBUReturnServerError
%s::%s: Image transfer timeout for coredump, aborting via force warm reset\n
%3C
Collecting core dump...
kBBUReturnRawBinaryImageError
%s::%s: Baseband coredump failed\n
%s::%s: Warning: unable to copy recipe from baseband firmware, so skipping chip-revision/firmware-recipe check\n
first pass - could not find data in FDR for %s
failed reading snum and/or chipID from booted baseband over ETL
%s::%s: failed to get prov session key\n
SecondaryEthernetMacAddress
NVRAMItems
BypassMobileAssetRPDownload
Cellular2,BbFATPCalibrationEnable
modem-bundle.img
BasebandProvisioning
hwt
%s::%s: >>send DALE_PL_CMD_SEND_POWER_TABLE\n
uimSlot       
BasebandUpdaterSetOptions
force-fusing
%s::%s: Invalid Baseband FW version size (%d)\n
 
Cellular1,CdpHost
%s::%s: value: 0x%x, boot-mode-value: %u (%s), crash-reason: (%hhu) %s\n
SyncDynamic
Next image requested\n
PSI is not running supported mode, unsupported firmware\n
processing event: %s, current state %d [%s]\n
postDataSync
::
EBL (%s) exists, but  is of invalid type!
kBBUReturnGetPersonalizationInfoFailed
%s::%s: Failed to sync baseband file system\n
invalid field length:  dataClass = %li, serial = %li\n
%s::%s: Skipping force warm reset for ConfigSimConfigSim\n
Error: copying PSI-RAM buffer.
100
%s::%s: Unable create provisioning dictionary\n
received reset response (dropping)\n
%s::%s: unexpected debug log path type\n
createBackupDir
%26
Loaded restoreSBL1\n
MANIFESTDATA
%s::%s: invalid ddr image\n
kBBUReturnGetManifestStatusFailed
Assertion failure ( (amountCopied == amount) && \"Copied data size mismatch: Failed to copy EBL image payload data to buffer!\" )
%s::%s: successfully retrieved board parameters in loader\n
NULL input parameter(s), returning empty string\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Provisioning/BBUEURProvisioner.cpp
invalid path pointer to create directory\n
Boot Logger PL
DaleController_ExceptionDump
%s::%s: successfully finished sending loader\n
kBBUReturnFatalError
BasebandUpdaterTransport
%s::%s: Failed to get ECID parameter for FDR data instance\n
%s::%s: NULL updater argument\n
Assertion failure ( fFusingSource == __null )
kBBUReturnLibFDRDynLibNotLinked
%s::%s: Unexpected CC cmd setting type\n
KERN_SUCCESS == kr && nvramInfo
Powering on modem. It is NOOP if BB is already on\n
Loaded PT\n
failed to getLogInternalBufferSize... will use %lu bytes.\n
%s::%s: Initializing BasebandRestore for preflight\n
%s::%s: No BbRequestEntries in dictionary passed in by PR.\n
BypassNVMDownload
Cellular1,BbFactoryDebugEnable
dumpPCIEState_sync_block_invoke
%s::%s: null buffer context in read completion callback\n
Loaded XBL Config\n
BBUFSServer releasing registry\n
StageContext::Boot
BasebandRestore
%s::%s: -------- DOWNLOAD FUSING PROGRAM --------\n
BypassMobileAssetWIDownload
%s::%s: NV items setting provided in the options: %s\n
VinylRefurbOption
calib.nvm
%s::%s: >>send ddr image data\n
Assertion failure ( loadPSIImages() && \"Error: Failed to load the PSI images!\" )
kBBUReturnLoaderVersionError
%s::%s: Baseband Update is complete!\n
%s::%s: Writing sticky nvram file to %s failed with error %d\n\n
fs == std::future_status::ready
%s::%s: Bad bootNonce size %u\n
unexpected hello disconnect mode %u, %s\n
status is %s\n
%s::%s: Default NVRAM items for restore: %s\n
Cellular1,FDRAllowUnsealed
%s::%s: Saving the final NVRAM list file as: %s\n
Failed changing file ownership (%u, %u)\n
Failed to get IMEI.
%s::%s: invalid ACK (0x%x) for PL_CMD_RECV_BOOT_MODE\n
Snapshot
Loaded Options\n
%s::%s: failed to start kernel trace\n
NVRestore setting: %d\n
operator()
%s::%s: read nonce status error (0x%x)\n
BBULoaderVersion
failed creating image from fdr data\n
Failed changing owner of coredump directory:  %s
B64_IMEI
unexpected command %u
%s::%s: Enabling provisioning flow to fix incorrect region setup\n
%s::%s: Warning: unable to open ACIPC %s interface\n
boost::too_many_args: format-string referred to fewer arguments than were passed
FWUpdatePerform
Failed due to copied size (%d) and original length (%d) is different.
%s::%s: image size: %zu\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Communication/Eureka/BBUEUR13Communication.cpp
kBBUReturnFFSimError
com.apple.bbu.acipcTransport
$
Fusing state: %d
Failed SteamAPDU index '%d' is greater than max array size '%zu'
mawi.bin
Set shutdownSync config to %s\n
Assertion failure ( err == chunk )
sendProvManSinope
sendImage_BBCfgHashTable
%s::%s: PT version info - [%s] [%s]\n
ret
efs3.bin
kBBUReturnBasebandUnresponsive
received unexpected command: %s\n
%s::%s: Error: BBUFSServer start failed\n
SignedFirmwareSOCView image missing\n
Assertion failure ( false && \"Invalid radio type!\" )
Assertion failure ( ( amountRead == sizeof( Header32 ) ) && \"Copied data size mismatch: Failed to copy ELF32 header from data source.\" )
   ChipID: %u (0x%08x)
BBTicket malloc for DER decode failed \n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Images/ICE/BBUICENVMImage.cpp
Kernel IPC Log
kBBUReturnNoMemory
EBL download unsuccessful: %u\n
Clearing error states since we are retrying.\n
%s::%s: Provisioning ping failed.\n
%s::%s: Failed to get chip information\n
stack
%s::%s: payload checksum: 0x%x\n
%s::%s: Coredump success\n
%s::%s: Length of data contained within the chunk: %u bytes\n
%5E
Install main but no ticket -- back to restored please\n
sBBUFSServerSetConfig function not initialized\n
Mav16
%s::%s: preflight get board parameters not implemented yet, returning success...\n
%s::%s: received status: %d\n
system-bundle
safe warm reset
Failed to create file %s\n
%s::%s: goldCertId: 0x%s\n
%s::%s: -------- PERFORM MANIFEST CHECK --------\n
%s::%s: FDR combined data for %s does not exist. Returning zero size.\n
%s::%s: invalid ACK (0x%x) for DALE_CMD_SEND_PROVISIONING_MANIFEST\n
%s::%s: failed to create BasebandCoredump object\n
%s: hw.model query failed with %d\n
%s::%s: sending bundle image...\n
%s::%s: Successfully changed IMEI SVN from %d to %d\n
Cellular2,Ticket
Trying to set SVN\n
Ticket provided is larger than spec. [ %lu (lenth) > %lu (spec max) ] \n
%s::%s: unexpected hash response size; expected: %zu OR %zu, received: %u\n
%s::%s: invalid protocol\n
Fail to read BB Init Status: I/O error\n
%22
Assertion failure ( fQuickStepInProgress )
%s::%s: invalid bundle image size\n
%s::%s: -------- RESTORE BASEBAND MIGRATION DATA --------\n
exception_LoaderStage
%s::%s: failed to cast firmware object\n
com.apple.telephony.baseband.
fuseRetrial
requireSystemPartitionMount
shouldPerformFusingVerification: it didn't go through fusing process before.\n
%s::%s: nonce: \n
Baseband Mobile Asset MBT image sent
fwMacData
file server stopped\n
DR_Success == der_ret && TAG_PI == dec.tag
Cellular2,BbFactoryActivationManifestKeyHash
Query Identifier Info
Failed gathering personalization parameters
%s::%s: status error (0x%x)\n
DaleFirmware_Boot
unexpected start mode %u, %s\n
%s::%s: Provisioning Ping failed\n
[LEGACY] Bundle Version: %d.%d\n
%s::%s: >>send calibration image payload\n
outData.Valid()
%s::%s: missing goldcertid\n
%s::%s: Successfully collected the Sik pub key from baseband\n
%s::%s: Bypassing NVM files download: returning zero size NVM file %s\n
Assertion failure ( transport && \"TelephonyUtilTransport Error.\" )
unknown
record %u: preference 0x%0x, base 0x%0x, length 0x%0x, description: '%s', filename '%s'\n
failed creating backup directory: %d, %d (%s)\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Protocol/Common/BBUProgrammer.cpp
%s::%s: Failed to force warm reset baseband\n
CoreDump path passed in to BBU is empty, skipping setting the coredump path for caller.
Assertion failure ( ( offset < getWritePayloadLength() ) && \"Error: Chunk size is not sufficient to write payload data of the ELF image.\" )
kBBUReturnNAKHello
ELF MAX SEGMENTS
createImage_BBTicket
Assertion failure ( success && \"Failed to get session key.\" )
%s::%s: failed to read crash reason size\n
Ping attempts set to %u from %u
%s::%s: Unexpected skip reset setting type\n
%s::%s: Failed to create ACFUDataContainer for NVRAM file\n
%s::%s: failed to get coredump save directory in str format\n
%s::%s: failed to init exception dump object\n
Fail to registerEventNotification: %#x \n
File %s does not exist\n
empty
Failed sending Done ACK packet.\n
%s::%s: pipe context is null in read callback\n
Vinyl EID dictionary content: 
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/BBUpdater/Legacy/Framework/Communication/Common/BBUCommunication.cpp
kBBUReturnError
%s::%s: failed to reset chip (ACFU error code = %d)\n
BBUFSServer created successfully\n
kBBUReturnGetICCIDFailure
kBBUReturnBBTicketDecodeError
BBUBootLogger: %.*s
AMFDRCopyDisposableKeys
%s::%s: m_io_code1 status error: 0x%x\n
Firmware version changed since last commcenter launch
Payload too large -- payload_size: %d  max allowed: %lu)\n
kBBUReturnMRCImageError
logManifestStatus
Root manifest size: %d \n
setHttpBase64EncodedValue
%s::%s: failed to read ACK for START_FLB_LOAD_BL_CODE\n
isBasebandProvisioned
Assertion failure ( false && \"Invalid radio type: Specified radio does not have a SequencerRam file.\" )
acdb.mbn
Loaded OEMMisc\n
Firmware APDU not within expected bounds : received (header - 5 : %zu data- 255 : %zu\n
Failed to create ARI transport\n
handleProvisioning
ARI_TIMEOUT - [0-9a-zA-Z]+, client [<>=]{1,2} (AP|BB)\\([a-zA-Z\\.]+\\) [0-9a-zA-Z]+\\([0-9]+-[0-9a-fA-F]+\\) SZ\\([0-9]+\\) TRX\\(|\\) AP\\.SEQ\\(0x[0-9a-f]+\\).*
%s::%s: hw info bytes: \n
kIOReturnSuccess == ret
%s::%s: <<rcv FLB_MSG_BIN_HEADER_STATUS\n
Assertion failure ( fBbcfgImage && \"Failed loading BBCFG image for creating hash.\" )
bbdy
PSI-Running mode 0x%x (%s)
KernelPCIRestoreTrace
%s::%s: Received unexpected bootNonceHash size %u bytes. Expected > 0 and <= %u bytes\n
%s::%s: Failed to get baseband reset state\n
%c%04zx  %s
Main & !Gold?\n
sConcatenatePath
ICEStateMachineSetConfig
kBBUReturnBadArgument
restoredInternal
%s::%s: Failed to create BasebandUpdater instance\n
AMFDRSetSealingMap
HardwareType
No update pending, finished with sync\n
CopyIdentifier returned: 
%s::%s: failed to write data to output URL\n
psiResp.result = 0x%X (%s)
pushFirmware_block_invoke
%s::%s: Failed to get Baseband PMU trace (not fatal)\n
provisioning/
%s::%s: Ping command failed\n
Cellular2,CdpAscUl
BBUFSServerStop
print
perform eUICC update\n
%s::%s: successfully retrieved board parameters in bootrom\n
airship
%s::%s: Error: BBUFSServer create failed\n
 ]
collecting coredump at %s
prov.nvm
invalid path specified %s\n
%s::%s: dynamic directory does not exist, creating (%s)...\n
psiResp.result == KTLRPSIEnhancedRspMrcResultInitialTuningOK
OEMMisc
BBUEURFusing
Could not find NVRAM via IOKit\n
info.plist
Resetting baseband .*?
%s::%s: BTI stage: failed to get the iBoot offset from the FW\n
%s::%s: IMEI:%s\n
%s::%s: baseband capabilities:\n\t- status:           0x%x\n\t- coredump enabled: 0x%x\n\t- bbcfg index:      0x%x\n\t- firmware version: %.*s\n\n
failed copying data from FDR\n
destFD >= 0
%s::%s: invalid ACK (0x%x) for PL_CMD_SEND_DDR\n
BBUFSServerSetConfig
failed handling EBL command.
failed getting entry\n
LogDirectory
modem boot up failure \\[.+\\]
PCIE
future.get()
carrier ID not present\n
%s::%s: failed to read ACK for BROM_CMD_FLB_GET_EFUSE_PUBLIC\n
Fusing source is not found.\n
bbpac.der
kBBUReturnBadEnvironment
BBUFSServer failed to create filer read session\n
```
