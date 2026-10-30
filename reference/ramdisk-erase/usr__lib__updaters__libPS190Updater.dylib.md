# `/usr/lib/updaters/libPS190Updater.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 336,080 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 25 (Size: 3576)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (8)

- `/usr/lib/updaters/libPS190Updater.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (51 classes, 4 protocols)

Classes: `NSData`, `NSMutableData`, `PCONUserClient`, `PS190APHardwareID`, `PS190AppFirmwareVersion`, `PS190BloodhoundPacketDumper`, `PS190BoardID`, `PS190BootNonceHash`, `PS190BootStatus`, `PS190BootStatusCommand`, `PS190BootloaderVersion`, `PS190CPROFuse`, `PS190CRC32`, `PS190CSECFuse`, `PS190CalculateCRC32Command`, `PS190ChipID`, `PS190Command`, `PS190CommitFirmwareUpdateCommand`, `PS190DBGDFuse`, `PS190Device`, `PS190DownloadFirmwareCommand`, `PS190ECID`, `PS190Epoch`, `PS190FirmwareBlock`, `PS190FirmwareFile`, `PS190GetBootNonceHashCommand`, `PS190GetECIDCommand`, `PS190GetInfoCommand`, `PS190GetSerialNumberCommand`, `PS190GetVersionCommand`, `PS190HardwareID`, `PS190IICDevice`, `PS190IODPDevice`, `PS190InitFirmwareUpdateCommand`, `PS190Instance`, `PS190OTPProgrammedFields`, `PS190OTPSerialNumber`, `PS190OTPValidFields`, `PS190PacketDumper`, `PS190ProgramBoardIDOTPCommand`, `PS190ProgramProductionModeOTPCommand`, `PS190ProgramSecurityDomainOTPCommand`, `PS190RHKPFuse`, `PS190ReadOTPCommand`, `PS190RecoveryDevice`, `PS190ResetCommand`, `PS190SDOMFuse`, `PS190SiliconID`, `PS190UpdaterController`, `PS190UpdaterInstance`, `SoCUpdaterHelper`

Protocols: `PS190DeviceDelegate`, `PS190DeviceHandle`, `PS190RecoveryDeviceDelegate`, `PS190UpdaterInstanceDelegate`

## Strings (976)

```
_loadToRAMPercentComplete
dmemImage
dumpCPROFuse:
enableSRAMAccess
otpQueryCPROFuse
_handle
commitWithReset
boardID
TI,R,V_instanceID
_verbose
allDeviceNames
length
TB,R,V_enabled
_version
dictionaryWithDictionary:
init
setDumper:
stripHWModelSuffix:
_nonce
_startedFromRecoveryMode
dumper
param2
queryHardwareRevision:
T@\"NSNumber\",R,V_productionMode
dumpBootStatus:
isEmpty
numberWithInt:
serviceName
T@\"NSArray\",R,V_blocks
clearIMG4Data
createCommandPacket
queryOTPValidFields
writeRegisterAddress:data:
TC,R,V_param0
_boardID
_isEmpty
_updaterIndex
causesReset
certificateEpoch
TC,R,V_param1
dumpString
hardwareRevision
otpWriteSecurityDomain:
TB,R,V_ecid
_authlistFormattedECID
dataWithData:
dumpCSECFuse:
dumpECID:
dumpRHKPFuse:
initWithEpoch:
otpWriteProductionMode:
Tr*,R,V_img4Object
_deviceRef
fillInCommandRegistersForCommand:
findDevice
initWithFormat:arguments:
initWithNumber:bytes:
initWithProductionMode:
initWithRawAppFirmwareVersion:
T@\"NSData\",R,V_nonce
initWithHandle:
_bytesTransferred
_securityMode
_skipSameVersion
dumpDPCDPacketType:address:bytes:length:
queryEpoch
requiresPersonalization
T@\"NSNumber\",R,V_boardID
submitDataForProcessing:
arrayWithArray:
T@\"NSString\",R,V_string
_type
arrayWithObjects:count:
flavorField
rawDescription
_chipID
TC,R,V_bootStatus
_imemSize
allObjects
hostAccessEnabled
initWithValue:
performUpdateWithDictionary:
_buffer
_blocks
T@\"NSDictionary\",R
T@\"<PS190RecoveryDeviceDelegate>\",W,V_delegate
_param1
firmwareBlocksSent:blocksTotal:
_needsOTPProgramming
commitWithoutReset
TC,R,V_productionMode
_bytesToTransfer
_imemImage
_realHDCPKeysPresent
description
initWithData:encoding:
productionMode
readData:
initWithStatus:
TB,R,V_productionStatus
TI,R,V_number
_bundleData
appendLittleInt32:
bootStatus
firmwareBytesSent:bytesTotal:
setEmptyIMG4Data
enabled
TC,R,V_checksum
param1
readRegisterAddress:buffer:length:
stringWithUTF8String:
submitCommandForProcessing:
waitForCommandStatusNotBusy
dmemSize
T@\"NSData\",R,V_bundleData
T{PS190RawAppFirmwareVersion=CCC},R,V_version
boolValue
disablePCON
param0
stringWithCapacity:
type
_globallySignedManifestPath
bundleData
dumpBootNonceHash:
dumpBootloaderVersion:
dumpOTPSerialNumber:
queryCPROFuse
TB,R,V_securityMode
byteString
dumpCRC32:
initWithHash:
TB,R,V_isEmpty
_pconUserClient
TC,R,V_param2
TI,R,V_boardID
_commandPacket
_logFunction
_rootPath
checkFieldNamed:programmed:valid:
_img4Object
date
debugDisable
initWithIICDevice:
queryInfoForUpdaterInstance:
resetToMemoryImage
setGloballySignedManifestPath:
stringByExpandingTildeInPath
_string
queryBootStatus
commandPacket
initAllowNonceQueries:
initWithBlockStartNumber:blockEndNumber:
isDone
otpQuerySDOMFuse
performUpdateForInstance:inputDict:firmwareFile:
TI,R,V_dmemSize
_param2
T@\"PS190PacketDumper\",&,V_dumper
getPCONStatus
queryInfoAggregate
T@\"NSData\",R
queryInstanceID
_delegate
dumpDBGDFuse:
needsOTPProgramming
queryChipEpoch
queryECID
TB,R,V_debugDisable
_iicDevice
checkForApplicationMode
dumpPacket:type:metadata:metadataLength:
initWithBlock:
initWithStatus2:
queryBootNonceHash:
readAddress:readAddressSize:buffer:bufferLength:
TB,V_useLocalSigning
_hardwareRevision
checkForRecoveryMode
dumpCMDIFPacket:cmdifType:
initWithFile:
initWithRootPath:
realHDCPKeysPresent
value
version
_log
securityMode
writeToSRAMAddress:bytes:length:
_number
T@\"<PS190DeviceDelegate>\",W,V_delegate
TC,R,V_epoch
_flavorField
blocks
initWithFileName:
queryCSECFuse
queryOTPSerialNumber
dealloc
_status
queryHardwareID
tag
TI,R,V_certificateEpoch
initWithRawBootloaderVersion:
queryRHKPFuse
readRegisterAddressNoErrorLog:buffer:length:
updateWithFile:
Tr*,R,V_dmemImage
allowNonceQueries
appendBytes:length:
dataWithContentsOfFile:options:error:
dictionaryWithObjects:forKeys:count:
dumpSDOMFuse:
dumpSiliconID:
lowercaseString
TB,R
_recoveryModeSupported
delegate
firstObject
generateDigest
hasPrefix:
personalizationParameters
_dumper
TI,R
_infoQueryComplete
bootFailureDetected
complete
queryBootloaderVersion
queryDBGDFuse
stringWithValidatedFormat:validFormatSpecifiers:error:
TB,R,V_allowNonceQueries
initWithChipID:
Tr*,R,V_imemImage
_useLocalSigning
appendLittleInt16:
bytes
dumpAppFirmwareVersion:
first
_checksum
appendData:
appendString:
checksum
data
dataWithBytes:length:
performUpdateWithDictionaryAggregate:firmwareFile:
queryBoardID
T@\"NSString\",R
contentsAtPath:
TC,R,V_crc8
_allowNonceQueries
dumpBoardID:
isEqual:
numberWithUnsignedChar:
setIMG4Data:
T@\"NSData\",R,V_data
checkForBootFailure
numberWithUnsignedInt:
queryOTPProgrammedFields
readCommandStatus:
resetToAppMode
setBootErrorStatus:
writeBytes:length:
TB,R,V_complete
.cxx_destruct
_data
_personalizedBundleData
initWithSubcommand:version:
otpWriteBoardID:
parseBundle
performUpdateWithDictionarySingleStep:firmwareFile:
TB,R,V_hostAccessEnabled
TI,R,V_tag
TQ,R,V_value
_connection
allDevices
defaultManager
imemImage
queryChipInfo
_securityDomainValid
addObject:
crc32ForBlocksInRange:
dumpDPCDRegisterRead:bytes:length:
initWithSubcommand:
productionStatus
programOTPForDevice:withInputParameters:
queryChipID
otpQueryBoardID
TI,R,V_securityDomain
TQ,R,V_ecid
enable
initIICService
querySecurityDomain
resetToRecoveryMode
setObject:forKeyedSubscript:
initWithOptions:logFunction:logContext:
queryFlags:
queryInfoSingleStep
verboseLog:
writeRegisterAddress:bytes:length:
TB,R,V_realHDCPKeysPresent
appendByte:
appendFormat:
initWithStatus1:
nonce
sendCommand:
string
subarrayWithRange:
TB,R,V_securityDomain
TC,R,V_count
_productionStatus
crc8
imemSize
logInternal:arguments:
queryCRC32ForBlockStartNumber:endNumber:
sendCommandWithData:
TI,R,V_chipID
_instanceID
_value
queryAppFirmwareVersion
queryHardwareIDIncludingNonce:
querySDOMFuse
setDelegate:
waitForHostAccessEnable
T@\"NSString\",C,V_globallySignedManifestPath
T@\"NSString\",R,V_serviceName
TB,R,V_recoveryModeSupported
_certificateEpoch
_crc8
_deviceHandle
initWithBoardID:certficateEpoch:chipID:debugDisable:ecid:nonce:productionMode:realHDCPKeysPresent:securityDomain:securityMode:hardwareRevision:
initWithData:
queryBootNonceHash
queryHardwareParameters
startPacketDumperWithFileName:
stringWithString:
_productionMode
set
_count
_ecid
initWithBoardID:
number
performUpdateForFirmwareFile:inputDict:skipSameVersion:
T@\"NSString\",R,V_rootPath
TB,R,V_certificateEpoch
TC,R,V_status
_bootFailureDetected
_debugDisable
_epoch
_ps190Instance
dictionary
T@\"NSData\",R,V_commandPacket
numberWithBool:
initWithInstanceID:
sendCommandWithDataResponse:
sendCommandWithoutData:
versionString
writeBuffer:
writeFile:
_dmemSize
dumpDPCDRegisterWrite:bytes:length:
img4Object
initializeUpdaterInstances
objectForKeyedSubscript:
queryBootNonceHashMSB:
recoveryModeSupported
status
Tr*,R
_bootStatus
array
dumpCommand:
dumpEpoch:
ecid
epoch
queryInfo
TC,R,V_type
_recoveryModeActive
globallySignedManifestPath
query
responseSize
setUseLocalSigning:
stringWithFormat:
unsignedIntValue
useLocalSigning
componentsSeparatedByString:
UTF8String
countByEnumeratingWithState:objects:count:
dumpBlocksString
dumpChipID:
initWithSecurityDomain:
querySiliconID
securityDomain
snifferPacket
_logContext
_serviceName
copy
initBlocks
queryBootNonceHashLSB:
unsignedCharValue
writeRequest:
TQ,R,V_type
_hostAccessEnabled
count
initWithType:param0:param1:param2:count:data:
T@\"NSString\",R,V_hardwareRevision
TB,R,V_boardID
_enabled
_tag
initWithInstance:tag:delegate:
instanceID
isEqualToString:
resetToAppLoad
TB,R,V_bootFailureDetected
T{PS190RawBootloaderVersion=CC},R,V_version
numberWithUnsignedLongLong:
timeIntervalSinceDate:
_dmemImage
findHandle
log:
rootPath
_param0
_securityDomain
_updaterInstances
enablePCON
findHandleAfterReset
loadFile:
resetToMode:
T@\"NSNumber\",R,V_securityDomain
TI,R,V_imemSize
TC,R,V_securityDomain
_complete
_service
chipID
initWithService:rootPath:
objectAtIndexedSubscript:
TC,R,V_value
TI,R,V_flavorField
TI,R,V_value
@\"PCONUserClient\"
i48@0:8r^v16Q24^v32Q40
^?
^v
^{__IODPDevice=}
C16@0:8
v20@0:8B16
v28@0:8@16S24
B32@0:8r*16B24B28
[4096C]
B16@0:8
v24@0:8I16I20
@36@0:8@16I24@28
B28@0:8I16@20
v36@0:8S16I20r*24I32
@24@0:8^{PS190RawBootNonceHash=[32C]}16
v20@0:8S16
@16@0:8
v24@0:8@16
v32@0:8I16r*20I28
I
@\"PS190BloodhoundPacketDumper\"
B24@0:8*16
B36@0:8@16@24B32
@\"<PS190DeviceHandle>\"
@20@0:8C16
@24@0:8r^{PS190RawAppFirmwareVersion=CCC}16
{PS190RawBootloaderVersion=\"major\"C\"minor\"C}
@\"<PS190DeviceDelegate>\"
@28@0:8C16r^{PS190RawAppFirmwareVersion=CCC}20
@24@0:8C16C20
@40@0:8@16^?24^v32
B40@0:8@16@24@32
@44@0:8C16C20C24C28C32@36
@24@0:8@16
B20@0:8I16
@\"<PS190RecoveryDeviceDelegate>\"
v16@0:8
@\"PS190PacketDumper\"
v20@0:8I16
@\"NSString\"
B
v44@0:8@16I24^v28Q36
@\"NSArray\"
@\"PS190Instance\"
B24@0:8@16
B20@0:8C16
Q
r*16@0:8
Q16@0:8
@24@0:8r^{PS190RawBootloaderVersion=CC}16
v32@0:8@16*24
@\"PS190IICDevice\"
I32@0:8{_NSRange=QQ}16
r*
i24@0:8@16
B32@0:8I16^v20I28
B32@0:8@16@24
@\"<PS190UpdaterInstanceDelegate>\"
@84@0:8@16I24I28B32Q36@44@52B60@64B72@76
@24@0:8Q16
@24@0:8I16I20
@20@0:8B16
v20@0:8C16
@\"NSNumber\"
@20@0:8I16
@\"NSObject<OS_os_log>\"
I16@0:8
C
@\"NSData\"
@28@0:8I16@20
I28@0:8r*16I24
v24@0:8@\"NSString\"16
{PS190RawAppFirmwareVersion=\"majorField\"C\"minor\"C\"sub\"C}
B32@0:8I16r^v20I28
@28@0:8C16r*20
{PS190RawAppFirmwareVersion=CCC}16@0:8
{PS190RawBootloaderVersion=CC}16@0:8
invalid manifest format
%s: Failed to program board ID
Update failed. Device firmware version does not match file firmware version. Device is running %@. File is %@.
SecurityDomain
PreflightRequired
Unrecognized
 Block Number: %u, CRC8: 0x%02x
Return Boot Status
Failed to load firmware from RAM.
-[PS190Device submitDataForProcessing:]
-[PS190RecoveryDevice queryChipInfo]
Number: %u\n
0000  
\tSecurity Domain: %u\n
Device detected after reset.
%s: Unable to locate board ID
Unknown
-[PS190RecoveryDevice writeRequest:]
Check RHKP Fuse
%@\n\n
ApSecurityMode
Unable to locate PS190 handle.
CertificateProductionStatus
-[PS190Device checkForRecoveryMode]
SecurityMode
FirmwareData
Debug disable
 Start: %u, End: %u
Loaded globally signed manifest
IOAVController
%s: Unable to locate security domain
%@: Attempting to update flash.
InfoArray
%s is not programmed.
Check CPRO Fuse
 CPRO
Failed to enable host access.
-[PS190RecoveryDevice queryChipID]
-[PS190RecoveryDevice enableSRAMAccess]
host access enable
Silicon ID
-[PCONUserClient enablePCON]
%u%% Complete
PCON%u,Firmware
PreflightContext
-[PS190RecoveryDevice loadFile:]
Yes
Using local signing: %s
%.02f%% Complete
%02X
timeout
App Firmware Version
Formal
Loaded firmware from RAM successfully
%@\n
%@
\tBoot Nonce Hash: %@\n
%s: Unable to locate firmware dictionary.
Checksum: 0x%02x
LocalSigningID
NeRD Preflight
NVM write error
Get Info
submit command
pconUserClient
 DBGD
Limited
\tPersonalization Required: %s\n
Unable to locate manifest for %@: %@
%02x.%02x
Failed to commit firmware to flash.
\tHardware Revision: %@\n
Reset or Boot Status
completed
IOService
Failed to download firmware to flash.
performNextStage
PreflightTickets
-[PS190RecoveryDevice queryOTPProgrammedFields]
-[PS190RecoveryDevice queryBoardID]
Test
TicketName
com.apple.AppleAccessoryManager
 Count: %u
/usr/local/standalone/firmware/ps190/ps190.im4m
Get ECID
<%@:
-[PS190UpdaterInstance programOTPForDevice:withInputParameters:]
%s: Failed to program security domain
%s %s\n%04x  
Continue Update
submit data
Detected boot failure after attempting to load firmware: 0x%02x (%s)
NeedsOTPProgramming
,Firmware
 (%s) Buffer Size: %u
\tSecurity Mode (CSEC): %s\n
data ready
-[PS190FirmwareFile setIMG4Data:]
-[PS190Device readCommandStatus:]
-[PS190UpdaterController performUpdateWithDictionary:]
Unable to locate chip after loading firmware.
 (%s) %@
 0x%08x
\tSecurity Domain (SDOM): %u\n
%s
Skipping firmware update, versions match.
Firmware restored successfully.
FWFeatureConfig
CRC: 0x%02x\n
invalid command
unrecognized
OTP Serial Number
True
Failed to reset to recovery mode.
Unable to add manifest to firmware file.
Download Firmware
>
-[PS190FirmwareFile crc32ForBlocksInRange:]
Certificate epoch
Get Serial Number
IOPropertyMatch
-[PS190IODPDevice initWithService:rootPath:]
-[PS190RecoveryDevice queryChipEpoch]
-[PS190RecoveryDevice queryHardwareID]
security level not met
illegal parameter
booted
 CSEC
recoveryDevice
%s is not valid.
%s: Unable to create PS190FirmwareFile from firmware data.
certificate validation failed
Setting security domain to %@
-[PS190RecoveryDevice querySecurityDomain]
00000000  
hash mismatch
-[PS190Device commitWithoutReset]
PCON%u,Ticket
OTA Stage 1
\tCertificate Epoch: %u\n
i
pHDMIg
Boot failure check failed
ChipID
signature verify
Epoch
AppleARMIICDevice
%@: Querying hardware ID.
-[PS190Device updateWithFile:]
DMEM Image: (%u bytes):\n
-[PS190Device readData:]
@PCON%u,Ticket
PCON%u,BoardID
Options
%s: Unable to locate firmware data.
ApBoardID
%02x
device
0x%02x
 BORD
Applying power for %@
-[PS190Device sendCommandWithData:]
Nonce
generateMeasurements
-[PS190RecoveryDevice queryOTPValidFields]
%02x%02x%02x%02x%02x%02x%02x%02x
%@:\n
Nonce queries allowed: %s
Failed to locate device after reset.
integrity error
AppleHDMIPortController
\tProduction Status: %s\n
\tSecurity Mode: %s\n
\n
HardwareID
ProductionMode
Verbose
-[PS190RecoveryDevice queryBootNonceHashMSB:]
NVM erase error
error
name
-[PS190Device sendCommandWithoutData:]
-[PS190Device checkForApplicationMode]
\tBoard ID: 0x%08x\n
%s %s\n%08x  
command tag mismatch
Check DBGD Fuse
Version: %@\n\n
TagNumber
\xa1
IODeviceTree
-[PS190Device checkForBootFailure]
GR2
Created %@
Failed to query hardware ID
-[PS190Device queryHardwareRevision:]
RequiresPersonalization
Failed to create updater instance for %@
Failed to apply power for %@
Abort Update
Without Reset
BranchDeviceID
UseHDCPEntitlement
,SecurityDomain
queryInfo
OTA Stage 2
\tProduction Mode: %s\n
-[PS190IICDevice initIICService]
Resetting to recovery mode.
Failed to check for boot failure after loading firmware.
OTP programmed successfully
-[PS190Device waitForCommandStatusNotBusy]
DebugEnableOverride
RestoreInternal
-[PS190RecoveryDevice queryBootNonceHashLSB:]
<%@: Number=%u, crc8=0x%02x>
-[PS190Device sendCommandWithDataResponse:]
AuthlistFormattedECID
UpdaterRef
ManifestPrefix
\tDebug Disable (DBGD): %s\n
ap
False
IODPDevice
Boot failure detected, but nonce queries are not allowed.
CertificateEpoch
Security mode
-[PS190Device otpWriteSecurityDomain:]
APInfo
Recovery mode supported: %s
success
Commit Firmware Update
Calculate CRC32
invalid certificate format
firmwareFile
Setting production mode to %@
ECID
\tAuthlist Formatted ECID: %@
   
Too many queryInfo calls!
malformed img4
iicDevice
-[PS190Device fillInCommandRegistersForCommand:]
RealHDCPKeysPresent
,BoardID
Board ID
busy
com.apple.accessoryupdater.ps190
-[PS190Device otpWriteProductionMode:]
Tethered Preflight
-[PS190RecoveryDevice queryFlags:]
Get Version
%@%u
-[PS190RecoveryDevice waitForHostAccessEnable]
-[PS190RecoveryDevice writeFile:]
Get Boot Nonce Hash
Reset Recovery
%s: Failed to program OTP production mode
-[PCONUserClient disablePCON]
BranchIEEEOUI
SkipSameVersion
\tNeeds OTP Programming: %s\n
Failed to read globally signed manfist: %@
dev
Skip same version: %s
%u
0x%llx
-[PS190Device writeBytes:length:]
Tethered
\tECID: 0x%016llx\n
\tReal HDCP Keys Present (RHKP): %s\n
 
Chip ID
%02x.%02x.%02x [%s Release]
 CEPO
<%@>
Setting board ID to 0x%x
-[PS190RecoveryDevice queryECID]
other failure
0x%08x
CertificateSecurityMode
\tFlavor Field: %u
IMEM Image (%u bytes):\n
%02x %02x %02x %02x %02x %02x %02x %02x    
command CRC mismatch
BoardId
DebugDisable
FIFO full
Init Update
Production Mode
-[PS190Device otpWriteBoardID:]
%u.%u
-[PS190Device submitCommandForProcessing:]
 SDOM
iodpDevice
No
%02x %02x %02x %02x %02x %02x %02x %02x  
NVM read error
firmware update failed
pcon
_getDeviceTreePath
Failed to query firmware version after update.
-[PS190RecoveryDevice writeToSRAMAddress:bytes:length:]
Init Firmware Update
Security Domain
General
HDMIPortID
 ECID
%@ [Response Size: %u]
<%@: %@>
%s: Failed to query AP production status
 0x%02x
_getAllRootPaths
Attempting to program OTP
1
Real HDCP Keys Valid
%02x 
 RHKP
-[PS190FirmwareFile parseBundle]
%@: Attemping to boot firmware from recovery mode.
BootedOS
nonce mismatch
Reset App Load
ApProductionMode
Detected boot failure 0x%02x (%s)
Boot failure detected, but recovery mode is not supported for OTA updates.
BoardID
RestoreSystemPartition
ForceLocalSigning
not initialized
PCON%u,SecurityDomain
OTA Preflight
NeRD Stage1
 (%s)
Perform update input = %@
-[PCONUserClient getPCONStatus]
IMG4 Object:\n
pcon%u
\tChip ID: 0x%08x\n
ApChipID
queryTags
DeferredCommit
Check CSEC Fuse
<%@ %@>
OTP programmed successfully. Resetting...
-[PS190RecoveryDevice resetToMode:]
Bootloader Version
Check SDOM Fuse
With Reset
%s: Firmware file is too small. DMEM size is %u, but only %lu byte(s) remaining in file
%s: Security domain is programmed, but not valid.
%s: Failed to write byte %d
%s: Failed to write SRAM address 0x%08x
%s: Command status indicated an error, but unable to read error value
%s: Failed to write board ID
%s: Unexpected CMDIF version (%@)
%s: Failed to write IMG4
IIC failed to write address 0x%x length %u (0x%08x)
%s: Failed to write command packet for %@
%s: Failed to submit %@
%s: Failed to read hardware revision
%s: Failed to write security domain
%s: Failed to read failed boot error register
%s: Failed to reset into recovery mode 0x%02x
%s: Timed out
%s: Failed to write %u byte(s)
%s: Failed to query OTP valid fields.
DP failed to write address 0x%x length %u (0x%08x)
%s: Failed to download %@
Failed to locate PCON service for instance ID %u
%s: Failed to read command status
%s: Failed to commit new firmware
%s: Invalid range specified
Failed to connect to PCON service for instance ID %u (0x%08x)
%s: Firmware file is too small (checksum)
%s: Unable to locate %@
%s: Failed to read %u byte(s)
Detected boot error: 0x%02x (%s)
%s: Failed to query OTP programmed fields.
%s: Failed to reboot to new firmware image
%s: Failed for instance ID %u (0x%08x)
DP failed to read address 0x%x length %u (0x%08x)
%s: Detected '%s' error (0x%02x)
%s: Failed to write DMEM image
%s: Firmware file is too small (version check)
%s: IORegistryEntryGetParentEntry failed (0x%08x)
%s: Failed to read boot status
%s: Failed to write production mode
%s: Failed to query chip info
%s: Failed to read boot status register
%s: Failed to write data to SRAM address 0x%08x
%s: Failed to write IMEM image
%s: Firmware file is too small. IMEM size is %u, but only %lu byte(s) remaining in file
%s: Unable to open connection to %@ (0x%08x)
IIC failed to read address 0x%x length %u (0x%08x)
%s: Failed to get matching services (0x%08x)
%s: Failed to initialize update
%s: Failed
%s: Failed to write boot block
%s: Failed to create IODPDevice.
%s: Failed to read CMDIF version
Unexpected boot status: 0x%02x (%s)
%@
Production status is programmed, but not valid.
Board ID is programmed, but not valid.
%s: Unexpected command status 0x%02x (%s) after submitting %@
%s: Unexpected command status 0x%02x (%s) after submitting data request for %@
%s: Failed to write request 0x%02x
%s: IMG4 data too large
PS190DBGDFuse
PS190OTPProgrammedFields
PS190IODPDevice
PS190Device
PS190PacketDumper
PS190GetBootNonceHashCommand
PS190BoardID
PS190SDOMFuse
PS190BootNonceHash
PS190Instance
PS190FirmwareBlock
PS190UpdaterInstanceDelegate
PCONUserClient
PS190ChipID
PS190BootStatus
PS190CRC32
PS190OTPValidFields
PS190IICDevice
PS190GetInfoCommand
PS190BloodhoundPacketDumper
PS190ReadOTPCommand
PS190SiliconID
PS190Command
PS190ResetCommand
PS190GetSerialNumberCommand
PS190AppFirmwareVersion
PS190RHKPFuse
Utils
PS190DeviceHandle
PS190DeviceDelegate
PS190HardwareID
PS190OTPSerialNumber
SoCUpdaterHelper
PS190BootStatusCommand
PS190ProgramBoardIDOTPCommand
PS190UpdaterController
PS190CPROFuse
PS190ECID
PS190APHardwareID
PS190FirmwareFile
PS190ProgramSecurityDomainOTPCommand
PS190ProgramProductionModeOTPCommand
PS190UpdaterInstance
PS190RecoveryDevice
PS190InitFirmwareUpdateCommand
PS190DownloadFirmwareCommand
PS190GetECIDCommand
PS190Epoch
PS190RecoveryDeviceDelegate
PS190GetVersionCommand
PS190CommitFirmwareUpdateCommand
PS190CalculateCRC32Command
PS190BootloaderVersion
PS190CSECFuse
```
