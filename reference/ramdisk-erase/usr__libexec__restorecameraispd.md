# `/usr/libexec/restorecameraispd`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 6,269,824 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 32 (Size: 3408)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, PIE
```

## Linked libraries (15)

- `/usr/lib/libIOAccessoryManager.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer (compatibility version 1.0.0, current version 326.31.9)`
- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libFDR.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libcompression.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/IOSurface.framework/IOSurface (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.camera.iokit-user-access</key>
	<true/>
	<key>com.apple.coreaudio.register-internal-aus</key>
	<true/>
	<key>com.apple.driver.VADResource.user-access</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.pearl.iokit-user-access</key>
	<true/>
	<key>com.apple.photondetector.iokit-user-access</key>
	<true/>
	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AGXCommandQueue</string>
		<string>AGXDevice</string>
		<string>AGXDeviceUserClient</string>
		<string>AGXSharedUserClient</string>
		<string>AppleCameraUserClient</string>
		<string>H11ANEInDirectPathClient</string>
		<string>H1xANELoadBalancerDirectPathClient</string>
		<string>IOAccelContext</string>
		<string>IOAccelContext2</string>
		<string>IOAccelDevice</string>
		<string>IOAccelDevice2</string>
		<string>IOAccelSharedUserClient</string>
		<string>IOAccelSharedUserClient2</string>
		<string>IOAccelSubmitter2</string>
		<string>IOSurfaceRootUserClient</string>
		<string>VADResourceArbiterUserClient</string>
		<string>AppleCameraPhotonDetectorUserClient</string>
	</array>
	<key>com.apple.symptom_diagnostics.report</key>
	<true/>
	<key>com.apple.systemstatus.publisher.domains</key>
	<array>
		<string>media</string>
	</array>
</dict>
</plist>
```

## Strings (654)

```
References for %s: Decompressing references\n
rosaline-calibration-current
/usr/local/share/firmware/isp/CmPM-DPCd
com.apple.iokit.matching
/usr/local/share/firmware/isp/8127_01XX.dat
Failed to remove %s token: %@
\tDidn't find calibration\n
%s: Failed to create file \"%s\" because of permissions. Deleting it (in case it exists) and trying again
com.apple.ispdevicecontroller.notifications.queue
ISPServicesRemoteRGBIRMetadataIRKey
DAT file for provisioned Savage - %@
Loading DAT file for unprovisioned Yonkers
map
AppleProxHIDEventDriver
Will use ISP references
ISPServicesRemoteCFTypeDataKey
DAT file for unprovisioned Yonkers - %@
LoadFrontIRHPRFile
chInfo1[ch]->gridCountX == chInfo1[0]->gridCountX
com.apple.isp.backcamerasensorconfig
/usr/local/share/firmware/isp/2027_01XX.dat
sparse reference plist
sparseLP reference plist
Found %s at %s.
v32@?0@\"NSNumber\"8Q16^B24
ISPServicesRemoteRGBIRBufferColorKey
BackCameraSNUM
chInfo[ch]->gridCountX == chInfo[0]->gridCountX
bps
Error converting calibrated power value\n
Could not determine size of file: %s\n
com.apple.isp.backcamerapower
com.apple.isp.frontirsensorpower
/usr/local/share/firmware/isp/ispane.afpp
%s%s/%s
GetSoCGeneration
/usr/local/share/firmware/isp/3527_02XX.dat
/var/mobile/Library/ISP/Pearl
rb
Load YonkersIR DAT File: Size = %ld; SendStatus = %08x, 0x%08X
Couldn't create SavageUID string ref
DspB
LSC_GET_BASE_U32_PT(chInfo1[ch]) % (chInfo1[ch]->gridCountX * chInfo1[ch]->gridCountY) == 0
GICComputeFromNVMApple
/usr/local/share/firmware/isp/2727_01XX.dat
a
\taFDR may not be used
\tCan't create %s! (%d)\n
PRF1: %s-%s: Unexpected references size (Expected %ld, Got %d)\n
Load: 0x%08x\n
no
pLSCConfig->channelGR.gridCountX == pLSCConfig->channelGB.gridCountX
\taFDR may be used
%s/%s-%s.plist
Saving %s\n
Expected file %s to be of size %ld. Actual size: %d\n
Reading rosaline serial number from sysconfig\n
IR sensor not detected
SavageChipID
SavageUID
FCDC
RadialGainEnable
setProperty
ISPServicesRemoteIORegPropertyNameKey
collectDiagState
EnforceClientEntitlement
/usr/local/share/firmware/isp/1925_03XX.dat
Testing if aFDR may be used
multi-camera-cal-swide
FCCl
BackTeleCameraSNUM
DPCd
/usr/local/share/firmware/isp/7324_01XX.dat
wb
Could not find SEP reference location. Will use ISP references
Load Savage DAT File: Size = %ld; SendStatus = %08x, FileStatus = 0x%08X
/usr/local/share/firmware/isp/dcs_isp_fw.bin
FrontCameraCalSwide
pLSCConfig->channelGR.gridCountY == pLSCConfig->channelGB.gridCountY
Can't activate %s projector: no projector token found
Failed to load PDE files\n
-sparseLP
doubleValue
sendMessageSync
chInfo1[ch]->gridCountY == chInfo1[0]->gridCountY
ISP_LoadIspAneAFPPFile
chInfo[ch]->gridCountY == chInfo[0]->gridCountY
/usr/local/share/firmware/isp/2123_01XX.dat
/var/mobile/Documents/Tokens.log
PRF1: Failed to save plist %@\n
rosaline-serial-num
ISPServicesRemoteRGBIRFinalInputPCEConfigKey
daemon
/usr/local/share/firmware/isp/
/usr/local/share/firmware/isp/CmPM-dcnu
%s token doesn't match platform. Token will be removed.
Pearl calibration\n
Creating local cache\n
%s/%@
/
ISP_SetFrontCameraOffsetFromDisplayCenter
/var/mobile/Library/ISP/CalData/DCNUMetadata_0
brcl
/usr/local/share/firmware/isp/7127_02XX.dat
Error converting calibrated power value:  could not fit 32-bit value into 16-bit destination \n
Prod
DAT
/usr/local/share/firmware/isp/CmPM-brgd
/usr/local/share/firmware/isp/CmPM-DPCm
LsAdjustInvertCam%d
fdrLogMessages
%02X
, calibration: 0x
reference
sparseLP
/usr/local/share/firmware/isp/7327_02XX.dat
Pearl FDR is %s, ToF FDR is %s
/private/var/tmp/usr/standalone/firmware/YonkersIR/YonkersIR%dPatch.DAT
LoadHPR
/usr/local/share/firmware/isp/2022_01XX.dat
v8@?0
Found Savage override DAT file, which takes precedence over all others - %@
IFCC
ISP_PowerOnCamera
com.apple.isp.frontrenocamerapower
LoadFDRCalDataFile
LoadFDRDataFileCMPM
Failed to send PCE calibration to FW\n
Could not read calibrated power from sysconfig\n
Could not open input file: %s\n
ISPServicesRemoteRGBIRPCEConfigKey
ISPServicesRemoteWorkIntervalPorts
isp-command-send
/var/mobile/Documents/Pearl
com.apple.isp
\tCouldn't validate directories\n
Cached UUID: 0x
basic_string
CacheChannelConfigs
InitDeviceConfigsCache
IODeviceTree:/arm-io
%@ %s\n
Loading DAT file for unprovisioned Savage
Override DAT file for YonkersIR%d - %@
ISPDevice.cpp
 :
UnitInfoNVMChannelMask
/usr/local/share/firmware/isp/FCCl.DAT
getProperty
/usr/local/share/firmware/isp/3527_03XX.dat
%s token timeout was reached (current time %ld). Token will be removed.
Failed to update %s token file. Will return false so someone looks at that...
Load Yonkers DAT File: Size = %ld; SendStatus = %08x, 0x%08X
%@-%@
/usr/local/share/firmware/isp/CmCl-Override.DAT
CopyAllowUnsealed
LSCComputeFromNVM.cpp
Failed to create log message string with code: %d (0x%X)
services
No DAT file for Yonkers found
deviceFirmwareLoad
LSCAverageGreenApple
general
FormatDR
SavageSNUM
Error converting vader compliance value\n
v16@?0^v8
Found Yonkers override DAT file, which takes precedence over all others - %@
com.apple.restorecameraispd.assistant_active
LSC_GET_BASE_U32_PT(chInfo[ch]) % (chInfo[ch]->gridCountX * chInfo[ch]->gridCountY) == 0
\tUnexpected local cache size (expected: %ld, found: %ld)
%s/%s.bin
%lf
/var/mobile/Library/ISP/Pearl/spotDB.bin
SavageDeviceRev
com.apple.isp.backsuperwidecamerapower
FWOBJECTSPECIALFUNC
/usr/local/share/firmware/isp/7126_01XX.dat
/usr/local/share/firmware/isp/0227_01XX.dat
%s token has exceeded max allowed timeout. Token will be removed.
ISPServicesRemoteCFTypeNameKey
Yonkers/YonkersPatch%s%s.DAT
chInfo2[ch]->gridCountY == chInfo2[0]->gridCountY
com.apple.cameraispd
EnableHawking
/usr/local/share/firmware/isp/4127_01XX.dat
ISPServicesRemoteDeviceID
Couldn't read SavageUID
LoadOCClCalDataFile
PRF1: %s-%s: Unknown format %d
Could not find %s as %s (errno: %d)
ISPServicesRemoteRGBIRBufferDepthKey
device
ISPServicesThread
YonkersFabRevision
coverglass-serial-number-2
/usr/local/share/firmware/isp/0426_01XX.dat
ISPServicesRemoteMapBuffers
brgd
DPCm
CacheDeviceConfigs
LsEnableGreenAvg
/usr/local/share/firmware/isp/2326_01XX.dat
Failed to read boot time. errno %d
Failed to send Romeo data file: 0x%08X\n
Ngsk
FrontCameraOffsetFromDisplayCenter
LoadFDRDspBDataFile
<UNKNOWN>
20.112
Unable to find prox service
iCCl
pCmdAppleChLSCConfigure->tableSize == pCmdAppleChDSCConfigure->numEntries
/System/Library/Isp/afpp/
Savage/SavagePatch%s.DAT
false
/usr/local/share/firmware/isp/0225_01XX.dat
/usr/local/share/firmware/isp/4227_01XX.dat
PRF1: Couldn't create reference file %s to write\n
No HPR file for frontIR found
DAT file for YonkersIR%d - %@
LSC_GET_BASE_U32_PT(chInfo2[ch]) % (chInfo2[ch]->gridCountX * chInfo2[ch]->gridCountY) == 0
System performed boot since %s token creation (boot time: %ld). Token will be removed.
\tLooking for local override files\n
\tUnexpected written size (expected: %ld, written %ld)
Error: Couldn't send NVM\n
front-camera-cal-swide
kCICMaxPerModuleX >= numXCIC
com.apple.isp.cameratorchcoolcurrent
=
No DAT file for Savage found
/private/var/tmp/usr/standalone/firmware/Yonkers/YonkersPatch.DAT
/usr/local/share/firmware/isp/SecureSensorPatchOverride.DAT
AP
cmca
OCCl
LoadFDRiCClDataFile
IgnoreUnitInfoPlist
/usr/local/share/firmware/isp/2626_02XX.dat
Failed to send references to FW\n
Reading rosaline power from IOReg\n
Trying to load reference file %s (type: %d, index: %d, temperature: %lf)\n
/Savage/SavagePatch.DAT
ifsc
com.apple.isp.frontrenocamerasensorconfig
isp_lacc.bin
Failed to read unique chip ID
LoadPDEFiles: isOverridden %d
Sending rosaline configuration: SN: %s; Power: %d\n
SavageMNS
/Yonkers/YonkersPatch.DAT
GetUnitInfoPropertyDict
CmPM
cmcd
Couldn't read unified Pearl FDR: %@
/var/mobile/Library/ISP/Pearl/
Found FrontIR override (has highest precedence) HPR file - camChannel = %d
HWModelStr
LSCComputeSNFVerticalGains
/usr/local/share/firmware/isp/2224_01XX.dat
yyyy-MM-dd HH:mm:ss
Error: Couldn't send rosaline configuration\n
floodCalibrationCurrent
SetupDeviceController
CALm
<null>
com.apple.restorecameraispd.destroy
\tIgnoring unexpected cached version (%d != %d)\n
sparse
Found no IR sensor\n
/usr/local/share/firmware/isp/cam%dclocks.txt
/System/Library/PrivateFrameworks/AppleCVHWA.framework/Firmware/
/usr/local/share/firmware/isp/8824_01XX.dat
\tCouldn't write %s: %s
Sending reference file %s, type: %d\n
NVM
sensor-type
com.apple.isp.frontcamerasensorconfig
LsAdjustEnableCam%d
com.apple.restorecameraispd.photometerManagerSyncQueue
\t%@
IOService
No C string description.
FrontCameraRenoModuleSerialNumString
\tCalibration UUID mismatch, removing contents of directory\n
\tFound\n
Couldn't read vader compliance\n
isp
ChannelArray
/usr/local/share/firmware/isp/4427_01XX.dat
/var/mobile/Documents/Pearl/ProjectorValid.bin
Failed to send rosaline data file: 0x%08X\n
ISPServicesRemoteFDRCalDataKey
com.apple.coremedia
Failed to read unique chip identifier
pDevice is NULL
/usr/local/share/firmware/isp/Savage/FrontIRHPR.DER
multi-camera-cal-wide
/usr/local/share/firmware/isp/cam%dsetfile.dat
pCmdAppleChVALSCConfigure->numTables <= CISP_VA_LSC_MAX_TABLES
com.apple.isp.backtelecamerapower
com.apple.isp.cameratorchwarmcurrent
%s token activation count updated to %d
\tCouldn't read %s: %s
com.apple.restorecameraispd
Secure RGB sensor not detected
Sending special debug function to firmware object returned error : 0x%08x\n
DEV
SendDataFileToFirmware
/usr/local/share/firmware/isp/OCCl-cmca.DAT
/usr/local/share/firmware/isp/2327_01XX.dat
Couldn't read from FDR: %@
unified
product
Failed to read PCE Calibration (FDR data)\n
Could not seek to end of file: %s\n
ISPServicesRemoteDataKey
ISPServicesRemoteTypeKey
UniqueChipID
DAT file for provisioned Yonkers - %@
MultiCameraCalSwide
pCmdAppleChVACICConfigure->numTables <= CISP_VA_CIC_MAX_TABLES
kCICMaxPerModuleY >= numYCIC
WDDC
LsInterpMode
DisableDropDetection
Number of allowed activations has reached zero. %s token will be removed.
/usr/local/share/firmware/isp/2327_02XX.dat
/usr/local/share/firmware/isp/6222_01XX.dat
/usr/local/share/firmware/isp/CmPM-CALm
Failed to open token log file.
%s-%s__T_%lf.bin
Personalized firmware root path accessor not found
Couldn't combine frontIR chipIDStr and uidStr
dcnu
^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8
Failed to read %s projector token file. Token will be removed.
\tReading from FDR\n
IOServiceFirstPublish
ISPServicesRemoteRGBIRReportKey
Dev
YonkersMNS
CmCl
kGICMaxPerModuleY >= numYGIC
/usr/local/share/firmware/isp/2426_02XX.dat
\tLooking for local cache\n
\tFailed to read UUID. Marking as invalid
Reading rosaline power from sysconfig\n
ISPServicesRemoteRGBIRFinalOutputPCEConfigKey
ISPServicesRemoteRGBIRMetadataColorKey
/usr/local/share/firmware/isp/IFSC.DAT
/usr/local/share/firmware/isp/IFCC.DAT
Could not read calibrated power from IOReg\n
Ymgt
ISPDevice
clockdiv
/ispane.afpp
/usr/local/share/firmware/isp/CmPM-brcl
%s-Ch%d.DAT
ISPServicesRemoteIORegPropertyDataKey
/usr/local/share/firmware/isp/3526_02XX.dat
/usr/local/share/firmware/isp/2626_01XX.dat
/usr/local/share/firmware/isp/2426_01XX.dat
/usr/local/share/firmware/isp/2226_01XX.dat
Pearl
MultiCameraCalWide
chInfo2[ch]->gridCountX == chInfo2[0]->gridCountX
:
dense
YonkersIR/YonkersIR%dPatch.DAT
ISP_ColdBootPowerCycle
com.apple.restorecameraispd.firmware_loading
LsBypassVerify
soc-generation
registerDeviceIDForClient
com.apple.private.cameraispd.client
token was removed
fopen_protected
%s: Failed to create file %s: %s
unavailable
floodComplianceRevision
Couldn't read SavageChipID
Couldn't create SavageChipID string ref
/usr/local/share/firmware/isp/ISPUnitInfo.plist
Using last allowed activation. %s token will be removed.
PRF1: %s-%s: Unexpected references size after compression (Expected %ld, Got %ld)\n
AppleCamera
com.apple.isp.backsuperwidesensorconfig
 \n
BackSuperWideCameraSNUM
/usr/local/share/firmware/isp/9723_01XX.dat
%lld
w
denseLP
Couldn't read serial number\n
0
/private/var/tmp/usr/standalone/firmware/Savage/SavagePatch.DAT
Special function: name: %s, parameters %llu %llu %llu %llu\n
/var/mobile/Library/ISP/Pearl/PCECalib.bin
Reading rosaline power from FDR\n
ValidateProjectorToken
CopyFileToBuffer
BackCameraModuleSerialNumString
FrontCameraModuleSerialNumString
BackTeleCameraModuleSerialNumString
ISP_SendCommand
%s token does not match device. Token will be removed.
r
not unified
true
DAT file for unprovisioned Savage - %@
/usr/local/share/firmware/isp/FCCl-Override.DAT
IOGeneralInterest
xpcClientEventHandler
/usr/local/share/firmware/isp/4426_01XX.dat
\tValidating Calibration UUID
LoadPDEFiles: No Savage found. Never mind
kGICMaxPerModuleX >= numXGIC
com.apple.isp.frontcamerapower
com.apple.isp.cameratorch
property
/System/Library/PrivateFrameworks/AppleCVHWA.framework/Firmware/lacc_VIO_ISP_IR.bin
\tLooking for FDR data\n
Will use SEP references
n't
ISP_SavageAuth
SendSysConfigCalibrationDataByKey
/usr/local/share/firmware/isp/dcs_v6x_isp_fw.bin
com.apple.restorecameraispd.writer
com.apple.restorecameraispd.launch
/usr/local/share/firmware/isp/3526_01XX.dat
/var/mobile/Library/ISP
Error reading file\n
%s%s.%s
SWDC
/usr/local/share/firmware/isp/OCCl-cmcd.DAT
/usr/local/share/firmware/isp/9726_01XX.dat
/usr/local/share/firmware/isp/7226_01XX.dat
/usr/local/share/firmware/isp/8227_01XX.dat
com.apple.isp.backtelecamerasensorconfig
/var/mobile/Library/ISP/CalData/DCNUPixbuf_0
/usr/local/share/firmware/isp/isp_fw.bin
LsIdealPctCam%d
ISPServicesRemoteFusingDataKey
ISPServicesRemoteReturnKey
yes
/usr/local/share/firmware/isp/6221_01XX.dat
/usr/local/share/firmware/isp/7327_01XX.dat
Received unexpected event: %s\n
%s - failed to load firmware ret=0x%08x\n
%s - snfRadialGains not enabled for ch %d\n
%s : Load override %s cal data: Size = %ld (== %ld ?); Status = %08x\n
%s - Error reading kernel config cache - chan: %d, res: 0x%08X\n
%s - maxChannels=%d, timeStampFrequency=%d\n
Destroying ISP services assistant\n
%s - kernel config count %d != firmware %d - chan: %d\n
%s - ISP_GetCameraStatus error (0x%08x)\n
This is%s an internal build, and FDR was%s validated\n
Set clock divider reg to 0x%08X\n
Sent ISP-ANE networks file to kernel: Size = %ld (== %ld ?); Status = %08x\n
%s: Savage Pre Auth failed, status = 0x%x\n
%s - %s loaded: Channel = %d, Status = %#08x\n
Client disconnecting (pid %{private}d)\n
%s - received invalid reply\n
%s - type=0x%X, isOverride=%d, size=%u, isEarlyBoot=%d, status=%08x\n
backTeleCameraModuleSerialNumString exists - load OCCl calibration data\n\n
%s : Status = %08x; OCCl (%s) data - %s \n
Couldn't read %s. Sensor is hosed/disconnected.\n
%s - Error getting config - res: 0x%08X\n
Unexpected client Set data length=%zu expected=%zu (pid %{private}d)\n
%s - status: 0x%08X\n
%s - Did not find platform-info for platform:%d. Defaulting to 0\n
Failed to copy model string from MobileGestalt\n
Active client pid %{private}d deviceID %{private}s\n
Error setting FW property: 0x%08x\n
No valid channel %d key provisioning file to send\n
%s - Couldn't read back camera module serial number. Sensor is hosed/disconnected. Skip loading FDR CmCl calibration data\n
backCameraModuleSerialNumString exists - load FDR CmCl calibration data\n\n
%s - client already has a registered device ID\n
Unexpected client message=%d (pid %{private}d)\n
Received XPC_ERROR_CONNECTION_INVALID error on connection\n\n
%s - Assistant Version %s\n
%s: Data file load failed, status = 0x%x\n
%s - Status = %#08x; CmCl data - %s\n
%s - Couldn't read front camera module serial number. Sensor is hosed/disconnected. Skip loading FCCl cal data\n
%s - No module or No DspB data (perhaps cuz the device does not support DspB). Skip loading FDR DspB calibration data\n
%s - %s\n
New connection: pid %{private}d\n
Received unexpected error from client (pid %{private}d)\n
UpdateChannelConfigCache channel %d error: 0x%08X\n
Error sending ISP-ANE networks file to kernel: Size = %ld (== %ld ?); Status = %08x\n\n
%s: Savage Auth failed, status = 0x%x\n
Removing client: pid %{private}d\n
LSC Orientation cam%d, flip = %d, invert = %d, useSetfile = %d, flipSetfile = %d, flipPerModule = %d rotateAls2Profile = %d enableGreenAvg = %d interpMode = %d  idealPct = %d DCS=%d XHatch=%d\n\n
%s - Rear camera not supported on this device\n
Rejecting XPC peer missing %{public}s (pid %{private}d)\n
%s - Status = %08x; HPR - %s\n
Using override ISP-ANE AFPP file\n
%s - channel configs not valid - exiting\n
Total number of connections: %lu\n
%s - %d\n
Error: SetSensorCustomSettings returned an error: 0x%08X\n
%s - ISP command not permitted\n
ISP still in use by another session; keeping shared interface open\n
Received XPC_ERROR_CONNECTION_INTERRUPTED error from client (pid %{private}d)\n
Unable to begin server for isp\n
%s - FTC gain buffer allocation failed\n
Failed to load Bin-format firmware binary: 0x%08x\n
%s - cache is already invalid - exiting\n
error sending camera channel %d over-ride NVM bytes to kernel: 0x%08X\n
ISPServicesRemote: GetProperty (%d) (reply=0x%08X)\n
%s - lsc adjustment not enabled for %x. lsc enabled = %d\n
%s - No module or Unauthorized swap (DspBStatus = 0x%x) or No DspB data (perhaps cuz the device does not support DspB) [error]: %s\n
%s - FCCl standalone loaded: Channel = %d, Status = %#08x\n
Load data file: channel: %d, type: %d, isEarlyBootDataFile: %s, status: %08x\n\n
%s - ISP_GetNumChannels failed with 0x%08x\n
No ALS2 profile found in Setfile\n
Successfully sent camera %d sensor register over-ride values for %d registers\n
sending camera channel %d over-ride NVM bytes to kernel (%d bytesn\n
Loading file for ISP-ANE networks - %s\n
%s - %s - length = %ld; status = %08x\n
Failed to crate SIGTERM dispatch source\n
%s - received reply\n
Failed to fetch handle for %s with return code = 0x%08x\n
Setting FW property 0x%08x to 0x%08X\n
%s - kMGQFrontCameraOffsetFromDisplayCenter Description=%s\n
Error opening ISP-ANE networks file\n
%s - No module or Unauthorized swap (cmclStatus = 0x%x) or No CmCL data (perhaps cuz the device does not support CmCL) [error]: %s\n
(Bin) Loading ISPCPU firmware file: %s\n
%s - %d configurations detected for channel %d\n
%s - [error]: %s\n
%s - poweredOn=%d, poweredOff=%d, res=0x%08X\n
Using override SecureSensorPatchOverride.DAT file\n
New connection: kernel\n
%s: Could not power off the ISP, res = 0x%x\n
Received XPC_ERROR_TERMINATION_IMMINENT error from client (pid %{private}d)\n
Audit: XPC peer missing %{public}s (pid %{private}d) — would reject\n
bypassing sending over-ride NVM bypass from unit-info plist for channel %d (mask bit not set)\n
%s - No module or Unauthorized swap (cmpmStatus = 0x%x) or No CmPM data (perhaps cuz the device does not support CmPM) [error]: %s\n
Camera powered on...waiting\n
%s - received error reply: %s\n
%s: Invalid data file arguments\n
%s - caching device configurations\n
Error: too many camera sensor register over-rides in file\n
%s - Camera powered on...waiting\n
Received SIGTERM - exiting\n
could not read ISPCPU Firmware file\n
%s - noHPR boot-arg set\n
%s - snfRadialGains command not in setfile for ch %d\n
%s: Invalid connection\n
Loaded calibration file from override path: %s\n
Couldn't read back camera module serial number. Sensor is hosed/disconnected. Skip loading OCCl calibration data\n
%s: Could not release channel, res = 0x%x\n
Received XPC_ERROR_TERMINATION_IMMINENT, cleaning up assistant\n\n
%s - powering on camera\n
LoadSetFile returned 0x%08x - ignoring error\n
%s - No module or No iCCl data (perhaps cuz the device does not support iCCl). Skip loading FDR iCCl calibration data\n
%s - no channels detected - exiting\n
Could not set CIL Brightness to %u\n\n
%s - IONotificationPortGetRunLoopSource returned NULL\n
Trying to use override SecureSensorPatchOverride.DAT file\n
could not read channel %d sensor key provisioning file entirely\n
Unable to look up remote connection (pid %{private}d)\n
Creating ISP services assistant\n
Unable to initialize services\n
using sensor setfile from file for camera %d: %s\n
%s - Could not forget firmware, res = %x\n
FrontCameraModuleSerialNumString exists - load OCCl calibration data\n\n
Removing client: kernel\n
Unable to create reply dictionary (pid %{private}d)\n
%s - Collecting ISP Sysdiagnose State\n
Error opening ISPDevice: %08X\n
%s - type=0x%X, isOverride=%d, file=%s, size=%u, isEarlyBoot=%d, status=%08x\n
%s OCCl is not a dict (FDR2.0?), Unauthorized swap or No OCCl data (perhaps cuz the device does not support OCCl) [error]: %s \n
%s - %d complete (res=0x%08X)\n\n
%s: %d: Sending reply to client: rc %08X (pid %{private}d)\n
%s - Timed out waiting for the driver to register service, deviceArrived = %d\n
%s - Error %x loading FW\n
%s - Failed to copy kMGQFrontCameraOffsetFromDisplayCenter answer from MobileGestalt! err=%d\n
%s:%s exists, length of the string = %ld.\n\n
%s - Initializing device configuration cache\n
Bin ISPCPU firmwareFile does not exist %s\n\n
%s - status: %08x\n
%s: Could not power on the ISP, res = 0x%x\n
Received unknown event from client (pid %{private}d)\n
%s - NVM not valid for camera %d sensorId = %x  %d\n
%s - LoadSetFile returned 0x%08x\n
%s - Success: cached configs - numChannels: %d\n
%s: Could not reserve channel, res = 0x%x\n
Unable to create mach service\n
Error parsing camera clock override file\n
%s - ret=%#x\n
%s - IONotificationPortCreate returned NULL\n
createXpcFromType got a dictionary with null value (for key %s)
Found camera clock override information file for camera channel %d\n
%s - Load override cal data: File = %s, Size = %ld (== %ld ?); Status = %08x (cmclStatus = 0x%08x)\n
%s - Parsing ISPUnitInfo.plist\n
Failure loading override ISPUnitInfo property list : CFPropertyListCreateWithStream failed\n
Could not send FW Ideal Percent for LSC channel[%u], returned:0x%08x - ignoring error\n
%s - failed to get SoC generation from the device tree\n
%s - SoC generation from the device tree is invalid!\n
Unexpected client Get data length=%zu expected=%zu (pid %{private}d)\n
%s - LSCComputeSNFVerticalGains: null ptr! pRadialGainAsymScaleSet.\n
ISPServicesRemote: GetProperty (%d) (sent)\n
%s - Using %s from unit info plist\n
No module or No CmPM data (perhaps cuz the device does not support CmPM). Skip loading FDR CmPM calibration data\n
%s - No iCCl data found, will attempt FCCl fallback processing\n
%s - Error getting channel info - chan: %d, res: 0x%08X\n
%s: Savage Auth failed, res = 0x%x\n
Received XPC_ERROR_CONNECTION_INTERRUPTED error on connection\n\n
Error creating ISPDeviceController object: %08X\n
%s - Error: resetting device config cache - res: 0x%08X\n
could not read sensor SetFile\n
Set sensor reg 0x%08x to val 0x%08X\n
%s - Trying to use %s: Size = %lld (== %lld ?);\n
camChannel: %d, cmpmInstance: %s\n
%s - No module or Unauthorized swap (icclStatus = 0x%x) or No iCCl data (perhaps cuz the device does not support iCCl) [error]: %s\n
defaultManager
setObject:forKey:
sortDescriptorWithKey:ascending:
stringByAppendingString:
writeToFile:atomically:
stringByAppendingFormat:
doubleValue
getBytes:length:
length
objectForKey:
copyPathForPersonalizedData:error:
dictionaryWithObjects:forKeys:count:
fileExistsAtPath:
setAttributes:ofItemAtPath:error:
setDateFormat:
stringWithUTF8String:
copyPathForPersistentData:error:
containsObject:
enumerateObjectsUsingBlock:
numberWithUnsignedInt:
sortedArrayUsingDescriptors:
allKeys
initWithContentsOfFile:
sharedDataAccessor
removeItemAtPath:error:
arrayWithObjects:count:
UTF8String
contentsOfDirectoryAtPath:error:
stringFromDate:
stringByAppendingPathComponent:
countByEnumeratingWithState:objects:count:
dataWithContentsOfFile:
date
description
dictionaryWithContentsOfFile:
intValue
stringWithFormat:
```
