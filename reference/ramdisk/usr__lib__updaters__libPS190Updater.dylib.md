# `/usr/lib/updaters/libPS190Updater.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 336,080 bytes.

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
@24@0:8C16C20
^?
^{__IODPDevice=}
@\"PS190BloodhoundPacketDumper\"
@20@0:8I16
v24@0:8@\"NSString\"16
@\"NSArray\"
{PS190RawAppFirmwareVersion=\"majorField\"C\"minor\"C\"sub\"C}
@24@0:8Q16
r*
i24@0:8@16
v20@0:8I16
C16@0:8
v20@0:8B16
Q
v20@0:8S16
@24@0:8@16
B20@0:8I16
@\"PCONUserClient\"
I28@0:8r*16I24
@36@0:8@16I24@28
@\"<PS190UpdaterInstanceDelegate>\"
r*16@0:8
@84@0:8@16I24I28B32Q36@44@52B60@64B72@76
@44@0:8C16C20C24C28C32@36
B16@0:8
@\"<PS190DeviceDelegate>\"
{PS190RawAppFirmwareVersion=CCC}16@0:8
C
v32@0:8I16r*20I28
^v
I16@0:8
@\"NSObject<OS_os_log>\"
v24@0:8@16
@20@0:8C16
@\"PS190IICDevice\"
v16@0:8
@28@0:8I16@20
B32@0:8@16@24
I
B28@0:8I16@20
{PS190RawBootloaderVersion=CC}16@0:8
i48@0:8r^v16Q24^v32Q40
v32@0:8@16*24
B32@0:8I16^v20I28
@\"NSString\"
@\"PS190PacketDumper\"
@\"NSNumber\"
@28@0:8C16r^{PS190RawAppFirmwareVersion=CCC}20
@28@0:8C16r*20
B32@0:8I16r^v20I28
B36@0:8@16@24B32
B24@0:8@16
v28@0:8@16S24
Q16@0:8
@40@0:8@16^?24^v32
@24@0:8r^{PS190RawBootloaderVersion=CC}16
@20@0:8B16
v44@0:8@16I24^v28Q36
v36@0:8S16I20r*24I32
B32@0:8r*16B24B28
B40@0:8@16@24@32
@24@0:8r^{PS190RawAppFirmwareVersion=CCC}16
v24@0:8I16I20
@\"<PS190RecoveryDeviceDelegate>\"
@16@0:8
@\"NSData\"
B
B20@0:8C16
@\"<PS190DeviceHandle>\"
@24@0:8^{PS190RawBootNonceHash=[32C]}16
@\"PS190Instance\"
B24@0:8*16
v20@0:8C16
[4096C]
{PS190RawBootloaderVersion=\"major\"C\"minor\"C}
I32@0:8{_NSRange=QQ}16
@24@0:8I16I20
Check SDOM Fuse
 RHKP
Checksum: 0x%02x
%s: Unable to locate board ID
SecurityMode
-[PS190RecoveryDevice queryOTPValidFields]
SecurityDomain
Certificate epoch
\tECID: 0x%016llx\n
-[PS190Device otpWriteProductionMode:]
DebugEnableOverride
-[PS190RecoveryDevice resetToMode:]
 Count: %u
Get ECID
Init Update
error
%@: Querying hardware ID.
CertificateEpoch
PCON%u,Ticket
NeRD Stage1
\tHardware Revision: %@\n
ApBoardID
-[PS190Device sendCommandWithDataResponse:]
-[PS190Device checkForBootFailure]
TagNumber
UseHDCPEntitlement
PCON%u,Firmware
-[PS190RecoveryDevice queryChipEpoch]
%@\n
%s %s\n%08x  
Failed to load firmware from RAM.
%@
Recovery mode supported: %s
command tag mismatch
Commit Firmware Update
Return Boot Status
Version: %@\n\n
AppleARMIICDevice
1
 0x%02x
Perform update input = %@
submit command
\n
IOAVController
Tethered
security level not met
Test
BoardId
 0x%08x
Firmware restored successfully.
-[PS190UpdaterInstance programOTPForDevice:withInputParameters:]
%s: Failed to program OTP production mode
%s is not programmed.
Bootloader Version
General
iicDevice
%s: Failed to program security domain
Update failed. Device firmware version does not match file firmware version. Device is running %@. File is %@.
NeedsOTPProgramming
TicketName
Unrecognized
0000  
%u
App Firmware Version
DeferredCommit
GR2
Unable to locate manifest for %@: %@
NVM erase error
-[PCONUserClient getPCONStatus]
-[PS190RecoveryDevice queryOTPProgrammedFields]
-[PS190RecoveryDevice queryChipInfo]
\tDebug Disable (DBGD): %s\n
Get Info
Get Boot Nonce Hash
Calculate CRC32
0x%08x
\tSecurity Mode: %s\n
Failed to query firmware version after update.
recoveryDevice
<%@: Number=%u, crc8=0x%02x>
-[PS190FirmwareFile crc32ForBlocksInRange:]
Get Version
-[PCONUserClient disablePCON]
-[PS190Device readCommandStatus:]
-[PS190Device readData:]
Applying power for %@
signature verify
%02x.%02x.%02x [%s Release]
 CPRO
_getAllRootPaths
IODeviceTree
Boot failure detected, but recovery mode is not supported for OTA updates.
Failed to reset to recovery mode.
Failed to query hardware ID
-[PS190Device otpWriteBoardID:]
@PCON%u,Ticket
-[PS190RecoveryDevice queryBoardID]
Boot failure check failed
Resetting to recovery mode.
%s: Failed to program board ID
%02x %02x %02x %02x %02x %02x %02x %02x    
\tBoot Nonce Hash: %@\n
\tProduction Status: %s\n
-[PS190IODPDevice initWithService:rootPath:]
%.02f%% Complete
ProductionMode
PCON%u,SecurityDomain
PreflightTickets
-[PS190RecoveryDevice queryECID]
%s: Unable to create PS190FirmwareFile from firmware data.
Security Domain
BranchDeviceID
HardwareID
BoardID
Verbose
%@:\n
\tSecurity Domain (SDOM): %u\n
%@\n\n
pHDMIg
-[PS190Device submitCommandForProcessing:]
 (%s)
CRC: 0x%02x\n
integrity error
Attempting to program OTP
-[PS190RecoveryDevice waitForHostAccessEnable]
-[PS190FirmwareFile setIMG4Data:]
Device detected after reset.
%@: Attemping to boot firmware from recovery mode.
-[PS190Device otpWriteSecurityDomain:]
,Firmware
-[PS190RecoveryDevice queryFlags:]
%u.%u
hash mismatch
completed
device
-[PS190RecoveryDevice writeToSRAMAddress:bytes:length:]
\tBoard ID: 0x%08x\n
CertificateProductionStatus
-[PS190Device fillInCommandRegistersForCommand:]
_getDeviceTreePath
%s: Failed to query AP production status
-[PS190RecoveryDevice queryHardwareID]
 
/usr/local/standalone/firmware/ps190/ps190.im4m
Silicon ID
Failed to check for boot failure after loading firmware.
Loaded firmware from RAM successfully
InfoArray
\tCertificate Epoch: %u\n
%02x %02x %02x %02x %02x %02x %02x %02x  
FIFO full
Continue Update
Production Mode
AuthlistFormattedECID
data ready
-[PCONUserClient enablePCON]
 SDOM
 BORD
False
IMG4 Object:\n
ApSecurityMode
%u%% Complete
-[PS190Device waitForCommandStatusNotBusy]
performNextStage
other failure
DebugDisable
Yes
%@ [Response Size: %u]
Failed to commit firmware to flash.
-[PS190Device checkForApplicationMode]
ChipID
RealHDCPKeysPresent
ForceLocalSigning
queryTags
%s is not valid.
-[PS190Device checkForRecoveryMode]
Nonce
PreflightRequired
Using local signing: %s
Chip ID
Abort Update
0x%llx
 (%s) Buffer Size: %u
\tProduction Mode: %s\n
%02x.%02x
firmwareFile
Unable to locate chip after loading firmware.
-[PS190Device writeBytes:length:]
ECID
-[PS190RecoveryDevice querySecurityDomain]
pconUserClient
Setting production mode to %@
-[PS190Device sendCommandWithData:]
ManifestPrefix
Security mode
\tReal HDCP Keys Present (RHKP): %s\n
AppleHDMIPortController
 CEPO
pcon
<%@>
RestoreSystemPartition
PreflightContext
Limited
Unknown
Number: %u\n
\tSecurity Mode (CSEC): %s\n
command CRC mismatch
PCON%u,BoardID
Debug disable
illegal parameter
HDMIPortID
0x%02x
00000000  
%s %s\n%04x  
Board ID
com.apple.accessoryupdater.ps190
BootedOS
Failed to read globally signed manfist: %@
%s: Unable to locate firmware dictionary.
-[PS190UpdaterController performUpdateWithDictionary:]
Check CSEC Fuse
Reset Recovery
True
com.apple.AppleAccessoryManager
DMEM Image: (%u bytes):\n
-[PS190Device sendCommandWithoutData:]
booted
-[PS190IICDevice initIICService]
   
Skipping firmware update, versions match.
-[PS190Device submitDataForProcessing:]
OTA Stage 2
-[PS190RecoveryDevice writeRequest:]
dev
%02x
Unable to locate PS190 handle.
Too many queryInfo calls!
invalid command
Check RHKP Fuse
Check DBGD Fuse
 DBGD
 ECID
,BoardID
 (%s) %@
 Start: %u, End: %u
Reset App Load
busy
%@: Attempting to update flash.
-[PS190RecoveryDevice queryChipID]
success
nonce mismatch
<%@ %@>
Setting board ID to 0x%x
OTP programmed successfully. Resetting...
invalid certificate format
IOService
Failed to download firmware to flash.
Options
Tethered Preflight
-[PS190RecoveryDevice loadFile:]
%02X
Failed to create updater instance for %@
%s: Unable to locate firmware data.
iodpDevice
Nonce queries allowed: %s
Check CPRO Fuse
queryInfo
OTP programmed successfully
Failed to locate device after reset.
UpdaterRef
Real HDCP Keys Valid
FWFeatureConfig
NeRD Preflight
Created %@
Download Firmware
<%@:
\tFlavor Field: %u
APInfo
RestoreInternal
-[PS190RecoveryDevice queryBootNonceHashLSB:]
%02x%02x%02x%02x%02x%02x%02x%02x
Detected boot failure 0x%02x (%s)
Boot failure detected, but nonce queries are not allowed.
Detected boot failure after attempting to load firmware: 0x%02x (%s)
RequiresPersonalization
Skip same version: %s
NVM write error
Unable to add manifest to firmware file.
malformed img4
With Reset
invalid manifest format
 CSEC
%s: Unable to locate security domain
FirmwareData
,SecurityDomain
LocalSigningID
\tNeeds OTP Programming: %s\n
%s
IOPropertyMatch
-[PS190Device commitWithoutReset]
OTA Preflight
No
Without Reset
-[PS190FirmwareFile parseBundle]
name
Failed to enable host access.
generateMeasurements
\tChip ID: 0x%08x\n
%02x 
unrecognized
-[PS190RecoveryDevice enableSRAMAccess]
Loaded globally signed manifest
host access enable
Formal
pcon%u
Get Serial Number
\tSecurity Domain: %u\n
i
OTA Stage 1
-[PS190RecoveryDevice queryBootNonceHashMSB:]
NVM read error
submit data
ApProductionMode
IODPDevice
-[PS190Device updateWithFile:]
-[PS190RecoveryDevice writeFile:]
\xa1
\tPersonalization Required: %s\n
timeout
Init Firmware Update
ap
BranchIEEEOUI
Reset or Boot Status
CertificateSecurityMode
IMEM Image (%u bytes):\n
Setting security domain to %@
SkipSameVersion
firmware update failed
Epoch
certificate validation failed
-[PS190Device queryHardwareRevision:]
 Block Number: %u, CRC8: 0x%02x
\tAuthlist Formatted ECID: %@
Failed to apply power for %@
not initialized
OTP Serial Number
>
ApChipID
<%@: %@>
%@%u
%s: Failed to download %@
DP failed to read address 0x%x length %u (0x%08x)
Detected boot error: 0x%02x (%s)
Production status is programmed, but not valid.
IIC failed to read address 0x%x length %u (0x%08x)
%s: Failed to read command status
%s: Failed to write board ID
%s: IORegistryEntryGetParentEntry failed (0x%08x)
%s: Timed out
%s: Failed to read %u byte(s)
%s: Failed to write IMEM image
%s: Failed to query chip info
%s: Unexpected command status 0x%02x (%s) after submitting data request for %@
Failed to locate PCON service for instance ID %u
%s: Firmware file is too small. DMEM size is %u, but only %lu byte(s) remaining in file
%s: Firmware file is too small (checksum)
%s: Unable to locate %@
%s: Failed to write IMG4
%s: Invalid range specified
%s: Failed to write command packet for %@
%s: Failed to write security domain
%s: Failed to initialize update
%@
%s: Failed to query OTP programmed fields.
%s: Failed to create IODPDevice.
%s: Failed to submit %@
%s: Failed to write production mode
%s: Security domain is programmed, but not valid.
%s: Failed to read CMDIF version
%s: Failed to commit new firmware
%s: Failed to get matching services (0x%08x)
Unexpected boot status: 0x%02x (%s)
Board ID is programmed, but not valid.
%s: Detected '%s' error (0x%02x)
%s: Unexpected CMDIF version (%@)
%s: Failed to write boot block
%s: Failed to reboot to new firmware image
%s: Failed to read failed boot error register
%s: Failed to read boot status
%s: Failed for instance ID %u (0x%08x)
IIC failed to write address 0x%x length %u (0x%08x)
DP failed to write address 0x%x length %u (0x%08x)
%s: Failed
Failed to connect to PCON service for instance ID %u (0x%08x)
%s: Firmware file is too small. IMEM size is %u, but only %lu byte(s) remaining in file
%s: Failed to write %u byte(s)
%s: Failed to write byte %d
%s: Failed to write SRAM address 0x%08x
%s: Unexpected command status 0x%02x (%s) after submitting %@
%s: Failed to read hardware revision
%s: Failed to reset into recovery mode 0x%02x
%s: Unable to open connection to %@ (0x%08x)
%s: Command status indicated an error, but unable to read error value
%s: Failed to read boot status register
%s: Failed to write request 0x%02x
%s: Failed to write data to SRAM address 0x%08x
%s: IMG4 data too large
%s: Firmware file is too small (version check)
%s: Failed to query OTP valid fields.
%s: Failed to write DMEM image
PCONUserClient
PS190BootNonceHash
PS190APHardwareID
PS190PacketDumper
PS190SDOMFuse
PS190CSECFuse
PS190RHKPFuse
PS190DBGDFuse
PS190ECID
PS190CRC32
PS190OTPValidFields
PS190Command
PS190BloodhoundPacketDumper
PS190CommitFirmwareUpdateCommand
PS190GetBootNonceHashCommand
PS190ProgramSecurityDomainOTPCommand
PS190ProgramBoardIDOTPCommand
SoCUpdaterHelper
PS190IODPDevice
PS190UpdaterInstance
PS190DownloadFirmwareCommand
PS190FirmwareBlock
PS190UpdaterController
PS190AppFirmwareVersion
PS190ChipID
Utils
PS190ProgramProductionModeOTPCommand
PS190UpdaterInstanceDelegate
PS190CPROFuse
PS190BootStatus
PS190OTPSerialNumber
PS190Instance
PS190FirmwareFile
PS190IICDevice
PS190RecoveryDevice
PS190BootStatusCommand
PS190BoardID
PS190OTPProgrammedFields
PS190HardwareID
PS190GetInfoCommand
PS190GetECIDCommand
PS190SiliconID
PS190DeviceDelegate
PS190GetVersionCommand
PS190ResetCommand
PS190GetSerialNumberCommand
PS190InitFirmwareUpdateCommand
PS190CalculateCRC32Command
PS190Epoch
PS190BootloaderVersion
PS190DeviceHandle
PS190RecoveryDeviceDelegate
PS190Device
PS190ReadOTPCommand
dumpBlocksString
initWithData:
initWithInstance:tag:delegate:
personalizationParameters
allObjects
requiresPersonalization
setGloballySignedManifestPath:
unsignedIntValue
TB,R,V_allowNonceQueries
TC,R,V_param1
TI,R,V_instanceID
appendByte:
dataWithBytes:length:
initWithBoardID:
initWithRawBootloaderVersion:
otpWriteBoardID:
_handle
TB,R,V_boardID
useLocalSigning
_authlistFormattedECID
byteString
componentsSeparatedByString:
data
date
T@\"NSNumber\",R,V_productionMode
T@\"NSData\",R,V_data
_globallySignedManifestPath
dumpOTPSerialNumber:
enablePCON
initBlocks
initWithData:encoding:
parseBundle
_number
commitWithReset
TI,R,V_securityDomain
_imemImage
dumpCSECFuse:
flavorField
queryInfoAggregate
readRegisterAddress:buffer:length:
_realHDCPKeysPresent
findHandleAfterReset
getPCONStatus
hostAccessEnabled
initIICService
initWithProductionMode:
initWithRootPath:
queryOTPSerialNumber
_string
_ecid
_securityDomainValid
dmemSize
dumpDPCDRegisterRead:bytes:length:
numberWithUnsignedInt:
queryBootNonceHash:
readCommandStatus:
TC,R,V_productionMode
TC,R,V_checksum
_epoch
bootFailureDetected
copy
initWithIICDevice:
performUpdateWithDictionarySingleStep:firmwareFile:
resetToAppLoad
T@\"NSNumber\",R,V_securityDomain
defaultManager
performUpdateWithDictionary:
sendCommandWithDataResponse:
serviceName
timeIntervalSinceDate:
versionString
waitForCommandStatusNotBusy
T@\"NSArray\",R,V_blocks
T@\"NSString\",R,V_hardwareRevision
_status
TB,R,V_isEmpty
otpQueryBoardID
contentsAtPath:
dumpRHKPFuse:
productionStatus
.cxx_destruct
_iicDevice
disablePCON
findDevice
initWithBlockStartNumber:blockEndNumber:
isDone
queryAppFirmwareVersion
queryCPROFuse
TQ,R,V_type
_securityMode
_version
checkForApplicationMode
initWithStatus2:
instanceID
sendCommandWithData:
setObject:forKeyedSubscript:
TC,R,V_bootStatus
TI,R,V_imemSize
_param1
_checksum
dumpDBGDFuse:
snifferPacket
type
writeBytes:length:
_data
_loadToRAMPercentComplete
delegate
dumpEpoch:
resetToAppMode
resetToMode:
TI,R,V_dmemSize
TC,R,V_count
tag
Tr*,R,V_imemImage
dataWithContentsOfFile:options:error:
initWithService:rootPath:
otpQuerySDOMFuse
param1
appendBytes:length:
createCommandPacket
initWithFile:
initializeUpdaterInstances
queryFlags:
realHDCPKeysPresent
securityMode
TQ,R,V_value
Tr*,R
_imemSize
_log
_value
count
dumpCommand:
dumpDPCDRegisterWrite:bytes:length:
T@\"PS190PacketDumper\",&,V_dumper
_hardwareRevision
_tag
dumpPacket:type:metadata:metadataLength:
nonce
queryCSECFuse
readData:
TI,R,V_flavorField
_dmemImage
arrayWithObjects:count:
initWithOptions:logFunction:logContext:
initWithStatus1:
readRegisterAddressNoErrorLog:buffer:length:
startPacketDumperWithFileName:
_count
_type
initWithSubcommand:
isEqualToString:
TC,R,V_type
TC,R,V_value
TI,R
Tr*,R,V_dmemImage
_deviceRef
enableSRAMAccess
otpWriteProductionMode:
_allowNonceQueries
_boardID
loadFile:
log:
responseSize
T@\"<PS190DeviceDelegate>\",W,V_delegate
queryHardwareID
crc8
queryBoardID
stringWithString:
TB,R,V_complete
TI,R,V_certificateEpoch
bundleData
imemImage
initWithBoardID:certficateEpoch:chipID:debugDisable:ecid:nonce:productionMode:realHDCPKeysPresent:securityDomain:securityMode:hardwareRevision:
queryBootNonceHashLSB:
queryInfoSingleStep
writeRequest:
TQ,R,V_ecid
dumpSDOMFuse:
imemSize
T@\"NSData\",R,V_nonce
TB,R,V_productionStatus
_needsOTPProgramming
bytes
performUpdateForFirmwareFile:inputDict:skipSameVersion:
dataWithData:
_blocks
TB,R,V_securityMode
_enabled
_productionStatus
dumpCPROFuse:
initWithHash:
queryBootloaderVersion
initWithHandle:
arrayWithArray:
T@\"NSString\",R,V_rootPath
fillInCommandRegistersForCommand:
generateDigest
querySDOMFuse
sendCommandWithoutData:
isEmpty
appendLittleInt32:
TI,R,V_value
_skipSameVersion
dumpECID:
img4Object
initWithInstanceID:
query
queryHardwareParameters
recoveryModeSupported
dealloc
initWithStatus:
T@\"NSData\",R
_updaterInstances
dictionaryWithDictionary:
T@\"NSString\",R
firmwareBlocksSent:blocksTotal:
_commandPacket
dumpAppFirmwareVersion:
enable
resetToMemoryImage
TC,R,V_epoch
_bundleData
_connection
hardwareRevision
value
T@\"NSData\",R,V_commandPacket
T{PS190RawBootloaderVersion=CC},R,V_version
blocks
commandPacket
param0
performUpdateWithDictionaryAggregate:firmwareFile:
queryChipInfo
querySecurityDomain
_securityDomain
TB,R,V_certificateEpoch
TB,R,V_recoveryModeSupported
_service
queryCRC32ForBlockStartNumber:endNumber:
rawDescription
TB,R,V_securityDomain
T{PS190RawAppFirmwareVersion=CCC},R,V_version
_ps190Instance
_recoveryModeActive
appendString:
performUpdateForInstance:inputDict:firmwareFile:
queryOTPProgrammedFields
TB,R
TI,R,V_number
set
_bootStatus
_debugDisable
certificateEpoch
epoch
initWithEpoch:
numberWithUnsignedChar:
queryHardwareIDIncludingNonce:
TB,R,V_bootFailureDetected
enabled
addObject:
allDeviceNames
appendFormat:
initWithBlock:
initWithType:param0:param1:param2:count:data:
objectAtIndexedSubscript:
_buffer
_bootFailureDetected
_bytesTransferred
_startedFromRecoveryMode
checksum
queryECID
setDelegate:
setEmptyIMG4Data
_param0
_productionMode
_dumper
dumpBootloaderVersion:
logInternal:arguments:
resetToRecoveryMode
stringByExpandingTildeInPath
verboseLog:
T@\"NSDictionary\",R
T@\"NSNumber\",R,V_boardID
TC,R,V_status
_img4Object
_updaterIndex
checkForBootFailure
ecid
initWithValue:
TB,V_useLocalSigning
_dmemSize
dumpBoardID:
dumper
number
otpQueryCPROFuse
queryRHKPFuse
readAddress:readAddressSize:buffer:bufferLength:
TI,R,V_tag
_param2
_delegate
dumpSiliconID:
hasPrefix:
setDumper:
submitCommandForProcessing:
T@\"NSString\",C,V_globallySignedManifestPath
lowercaseString
TC,R,V_crc8
TI,R,V_boardID
_infoQueryComplete
array
checkForRecoveryMode
param2
_verbose
dmemImage
dumpChipID:
initWithSubcommand:version:
queryInfo
queryOTPValidFields
rootPath
sendCommand:
allowNonceQueries
firmwareBytesSent:bytesTotal:
initWithSecurityDomain:
isEqual:
queryHardwareRevision:
_bytesToTransfer
_certificateEpoch
globallySignedManifestPath
initWithNumber:bytes:
numberWithInt:
queryEpoch
setBootErrorStatus:
stringWithValidatedFormat:validFormatSpecifiers:error:
description
initWithRawAppFirmwareVersion:
queryChipEpoch
queryChipID
stringWithCapacity:
TB,R,V_enabled
_recoveryModeSupported
T@\"NSData\",R,V_bundleData
boardID
numberWithBool:
TC,R,V_param0
countByEnumeratingWithState:objects:count:
objectForKeyedSubscript:
submitDataForProcessing:
writeFile:
dumpBootStatus:
initWithFormat:arguments:
programOTPForDevice:withInputParameters:
queryBootNonceHashMSB:
querySiliconID
stringWithUTF8String:
writeRegisterAddress:bytes:length:
writeRegisterAddress:data:
checkFieldNamed:programmed:valid:
commitWithoutReset
debugDisable
dumpString
findHandle
queryDBGDFuse
stringWithFormat:
writeBuffer:
version
_complete
allDevices
boolValue
clearIMG4Data
numberWithUnsignedLongLong:
queryInfoForUpdaterInstance:
writeToSRAMAddress:bytes:length:
TB,R,V_realHDCPKeysPresent
_deviceHandle
_nonce
appendData:
first
init
initWithFileName:
setUseLocalSigning:
TB,R,V_debugDisable
_logContext
dictionaryWithObjects:forKeys:count:
setIMG4Data:
stripHWModelSuffix:
unsignedCharValue
TC,R,V_param2
UTF8String
TB,R,V_hostAccessEnabled
dumpBootNonceHash:
length
otpWriteSecurityDomain:
productionMode
string
queryInstanceID
dumpCMDIFPacket:cmdifType:
needsOTPProgramming
status
subarrayWithRange:
causesReset
chipID
crc32ForBlocksInRange:
queryBootStatus
_instanceID
_isEmpty
bootStatus
queryBootNonceHash
appendLittleInt16:
complete
dictionary
T@\"NSString\",R,V_serviceName
initWithChipID:
T@\"NSString\",R,V_string
_logFunction
_serviceName
_chipID
T@\"<PS190RecoveryDeviceDelegate>\",W,V_delegate
_pconUserClient
TI,R,V_chipID
Tr*,R,V_img4Object
dumpDPCDPacketType:address:bytes:length:
securityDomain
waitForHostAccessEnable
updateWithFile:
TB,R,V_ecid
_flavorField
_rootPath
_useLocalSigning
dumpCRC32:
firstObject
initAllowNonceQueries:
TC,R,V_securityDomain
_crc8
_hostAccessEnabled
_personalizedBundleData
```
