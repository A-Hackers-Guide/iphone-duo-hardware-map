# `/usr/libexec/restorecameraispd`

From the upgrade restore ramdisk (141-29011-104.dmg). 6,269,824 bytes.

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
Couldn't combine frontIR chipIDStr and uidStr
%s token doesn't match platform. Token will be removed.
sparse reference plist
Could not seek to end of file: %s\n
ISPServicesRemoteRGBIRReportKey
ISPServicesRemoteCFTypeNameKey
yes
/Savage/SavagePatch.DAT
Couldn't read SavageChipID
Secure RGB sensor not detected
No C string description.
BackTeleCameraSNUM
DisableDropDetection
LSCAverageGreenApple
Can't activate %s projector: no projector token found
ISPServicesRemoteFDRCalDataKey
LoadFrontIRHPRFile
%@-%@
pCmdAppleChLSCConfigure->tableSize == pCmdAppleChDSCConfigure->numEntries
com.apple.isp.cameratorchwarmcurrent
FrontCameraModuleSerialNumString
CALm
\tCouldn't validate directories\n
wb
sparseLP
FrontCameraOffsetFromDisplayCenter
SendDataFileToFirmware
/usr/local/share/firmware/isp/dcs_v6x_isp_fw.bin
ISP_SendCommand
LsBypassVerify
/usr/local/share/firmware/isp/3527_03XX.dat
a
reference
Reading rosaline power from FDR\n
Could not determine size of file: %s\n
Found Savage override DAT file, which takes precedence over all others - %@
clockdiv
isp_lacc.bin
/usr/local/share/firmware/isp/0225_01XX.dat
\tLooking for FDR data\n
ISP_PowerOnCamera
ISPDevice.cpp
CopyAllowUnsealed
xpcClientEventHandler
collectDiagState
deviceFirmwareLoad
Failed to open token log file.
PRF1: Failed to save plist %@\n
Couldn't read vader compliance\n
Error: Couldn't send rosaline configuration\n
basic_string
sensor-type
/usr/local/share/firmware/isp/CmPM-DPCm
IgnoreUnitInfoPlist
SavageDeviceRev
/usr/local/share/firmware/isp/2626_01XX.dat
isp
v8@?0
LoadHPR
iCCl
soc-generation
ISPServicesRemoteIORegPropertyDataKey
/usr/local/share/firmware/isp/9726_01XX.dat
/usr/local/share/firmware/isp/7127_02XX.dat
\tUnexpected local cache size (expected: %ld, found: %ld)
Could not find %s as %s (errno: %d)
LSC_GET_BASE_U32_PT(chInfo2[ch]) % (chInfo2[ch]->gridCountX * chInfo2[ch]->gridCountY) == 0
FCDC
SWDC
CacheChannelConfigs
/usr/local/share/firmware/isp/7324_01XX.dat
\tDidn't find calibration\n
ISPServicesRemoteMapBuffers
daemon
/System/Library/PrivateFrameworks/AppleCVHWA.framework/Firmware/lacc_VIO_ISP_IR.bin
com.apple.coremedia
LsEnableGreenAvg
/System/Library/PrivateFrameworks/AppleCVHWA.framework/Firmware/
ISPServicesRemoteRGBIRFinalOutputPCEConfigKey
ISPServicesRemoteTypeKey
IR sensor not detected
multi-camera-cal-swide
FCCl
ifsc
LSC_GET_BASE_U32_PT(chInfo1[ch]) % (chInfo1[ch]->gridCountX * chInfo1[ch]->gridCountY) == 0
kGICMaxPerModuleX >= numXGIC
Sending reference file %s, type: %d\n
/usr/local/share/firmware/isp/SecureSensorPatchOverride.DAT
InitDeviceConfigsCache
fdrLogMessages
com.apple.restorecameraispd.photometerManagerSyncQueue
Failed to create log message string with code: %d (0x%X)
%s/%s.bin
SetupDeviceController
MultiCameraCalWide
Special function: name: %s, parameters %llu %llu %llu %llu\n
/usr/local/share/firmware/isp/7327_02XX.dat
services
Testing if aFDR may be used
%02X
AP
BackTeleCameraModuleSerialNumString
brcl
CacheDeviceConfigs
\tCalibration UUID mismatch, removing contents of directory\n
\tCouldn't write %s: %s
References for %s: Decompressing references\n
com.apple.isp.frontcamerasensorconfig
LSCComputeFromNVM.cpp
GICComputeFromNVMApple
Using last allowed activation. %s token will be removed.
/usr/local/share/firmware/isp/1925_03XX.dat
/usr/local/share/firmware/isp/4227_01XX.dat
%lf
Could not open input file: %s\n
/private/var/tmp/usr/standalone/firmware/Yonkers/YonkersPatch.DAT
No DAT file for Yonkers found
n't
%s: Failed to create file %s: %s
unified
/
Load: 0x%08x\n
Couldn't create SavageChipID string ref
/usr/local/share/firmware/isp/cam%dsetfile.dat
pCmdAppleChVALSCConfigure->numTables <= CISP_VA_LSC_MAX_TABLES
/usr/local/share/firmware/isp/OCCl-cmcd.DAT
/usr/local/share/firmware/isp/2226_01XX.dat
Pearl
/var/mobile/Documents/Tokens.log
Could not read calibrated power from IOReg\n
v16@?0^v8
ISPServicesRemoteDeviceID
chInfo2[ch]->gridCountY == chInfo2[0]->gridCountY
com.apple.isp.frontcamerapower
/usr/local/share/firmware/isp/4427_01XX.dat
/usr/local/share/firmware/isp/2426_01XX.dat
YonkersFabRevision
/usr/local/share/firmware/isp/
/usr/local/share/firmware/isp/CmPM-brgd
sparse
/usr/local/share/firmware/isp/2327_01XX.dat
/usr/local/share/firmware/isp/8227_01XX.dat
/var/mobile/Library/ISP/Pearl/PCECalib.bin
\tUnexpected written size (expected: %ld, written %ld)
Found Yonkers override DAT file, which takes precedence over all others - %@
com.apple.isp.frontrenocamerapower
dcnu
/usr/local/share/firmware/isp/3527_02XX.dat
\tLooking for local override files\n
FormatDR
Failed to send rosaline data file: 0x%08X\n
Prod
Dev
Load Yonkers DAT File: Size = %ld; SendStatus = %08x, 0x%08X
/usr/local/share/firmware/isp/CmPM-CALm
/var/mobile/Library/ISP/Pearl
floodCalibrationCurrent
Sending rosaline configuration: SN: %s; Power: %d\n
 :
/ispane.afpp
coverglass-serial-number-2
RadialGainEnable
/usr/local/share/firmware/isp/ISPUnitInfo.plist
isp-command-send
LsInterpMode
com.apple.restorecameraispd.writer
com.apple.restorecameraispd.destroy
/usr/local/share/firmware/isp/7226_01XX.dat
/usr/local/share/firmware/isp/2027_01XX.dat
No DAT file for Savage found
DspB
Sending special debug function to firmware object returned error : 0x%08x\n
UnitInfoNVMChannelMask
%s%s/%s
LSC_GET_BASE_U32_PT(chInfo[ch]) % (chInfo[ch]->gridCountX * chInfo[ch]->gridCountY) == 0
fopen_protected
BackCameraModuleSerialNumString
%s token has exceeded max allowed timeout. Token will be removed.
\tReading from FDR\n
rosaline-serial-num
ISPServicesRemoteDataKey
ISPServicesRemoteWorkIntervalPorts
SavageUID
front-camera-cal-swide
/usr/local/share/firmware/isp/CmPM-dcnu
Couldn't read from FDR: %@
Error: Couldn't send NVM\n
rosaline-calibration-current
DAT file for provisioned Yonkers - %@
GetUnitInfoPropertyDict
com.apple.isp.backsuperwidecamerapower
com.apple.restorecameraispd.launch
LSCComputeSNFVerticalGains
/usr/local/share/firmware/isp/4127_01XX.dat
Found %s at %s.
Yonkers/YonkersPatch%s%s.DAT
IFCC
 \n
brgd
/usr/local/share/firmware/isp/FCCl.DAT
chInfo1[ch]->gridCountX == chInfo1[0]->gridCountX
/System/Library/Isp/afpp/
LoadFDRiCClDataFile
EnforceClientEntitlement
dense
product
Couldn't read serial number\n
SavageMNS
com.apple.restorecameraispd.firmware_loading
%s-Ch%d.DAT
Failed to read unique chip ID
Failed to read unique chip identifier
\t%@
Failed to load PDE files\n
true
/Yonkers/YonkersPatch.DAT
YonkersIR/YonkersIR%dPatch.DAT
IOGeneralInterest
Pearl calibration\n
\tFailed to read UUID. Marking as invalid
%s/%s-%s.plist
no
Savage/SavagePatch%s.DAT
chInfo2[ch]->gridCountX == chInfo2[0]->gridCountX
/usr/local/share/firmware/isp/OCCl-cmca.DAT
System performed boot since %s token creation (boot time: %ld). Token will be removed.
%@ %s\n
/var/mobile/Library/ISP/Pearl/spotDB.bin
YonkersMNS
/var/mobile/Library/ISP
\tIgnoring unexpected cached version (%d != %d)\n
ISPServicesRemoteRGBIRMetadataColorKey
/usr/local/share/firmware/isp/Savage/FrontIRHPR.DER
CmCl
com.apple.isp.backtelecamerapower
ISP_SetFrontCameraOffsetFromDisplayCenter
Creating local cache\n
%s: Failed to create file \"%s\" because of permissions. Deleting it (in case it exists) and trying again
PRF1: %s-%s: Unknown format %d
com.apple.isp.frontirsensorpower
/usr/local/share/firmware/isp/cam%dclocks.txt
/var/mobile/Library/ISP/CalData/DCNUMetadata_0
/usr/local/share/firmware/isp/IFSC.DAT
com.apple.iokit.matching
%s token timeout was reached (current time %ld). Token will be removed.
Cached UUID: 0x
Saving %s\n
Error converting vader compliance value\n
/var/mobile/Library/ISP/Pearl/
ISPServicesRemoteRGBIRFinalInputPCEConfigKey
MultiCameraCalSwide
NVM
%s token does not match device. Token will be removed.
\tLooking for local cache\n
rb
PRF1: %s-%s: Unexpected references size after compression (Expected %ld, Got %ld)\n
PRF1: Couldn't create reference file %s to write\n
sparseLP reference plist
Error converting calibrated power value:  could not fit 32-bit value into 16-bit destination \n
ISPServicesRemoteRGBIRBufferColorKey
bps
com.apple.ispdevicecontroller.notifications.queue
ISPServicesRemoteRGBIRBufferDepthKey
ValidateProjectorToken
kGICMaxPerModuleY >= numYGIC
com.apple.isp.backtelecamerasensorconfig
com.apple.isp.cameratorch
SendSysConfigCalibrationDataByKey
\tCouldn't read %s: %s
Unable to find prox service
Could not read calibrated power from sysconfig\n
doubleValue
Override DAT file for YonkersIR%d - %@
chInfo1[ch]->gridCountY == chInfo1[0]->gridCountY
:
LoadFDRCalDataFile
/var/mobile/Documents/Pearl/ProjectorValid.bin
/usr/local/share/firmware/isp/2426_02XX.dat
\taFDR may be used
unavailable
device
Couldn't create SavageUID string ref
DEV
LoadOCClCalDataFile
/usr/local/share/firmware/isp/0227_01XX.dat
/usr/local/share/firmware/isp/6221_01XX.dat
%lld
SavageSNUM
ISPServicesRemoteCFTypeDataKey
com.apple.isp.backcamerapower
com.apple.isp.cameratorchcoolcurrent
cmcd
yyyy-MM-dd HH:mm:ss
/var/mobile/Documents/Pearl
not unified
ISPServicesThread
Ngsk
Couldn't read SavageUID
kCICMaxPerModuleX >= numXCIC
com.apple.isp.frontrenocamerasensorconfig
/usr/local/share/firmware/isp/7126_01XX.dat
sendMessageSync
DAT file for YonkersIR%d - %@
HWModelStr
/usr/local/share/firmware/isp/dcs_isp_fw.bin
ISP_LoadIspAneAFPPFile
com.apple.restorecameraispd.assistant_active
/usr/local/share/firmware/isp/6222_01XX.dat
DAT file for unprovisioned Yonkers - %@
ChannelArray
com.apple.isp.backsuperwidesensorconfig
LoadFDRDspBDataFile
/usr/local/share/firmware/isp/FCCl-Override.DAT
LsAdjustInvertCam%d
EnableHawking
LoadPDEFiles: isOverridden %d
ISPServicesRemoteRGBIRPCEConfigKey
Ymgt
ISP_ColdBootPowerCycle
CopyFileToBuffer
OCCl
FrontCameraRenoModuleSerialNumString
GetSoCGeneration
/usr/local/share/firmware/isp/2327_02XX.dat
Couldn't read unified Pearl FDR: %@
v32@?0@\"NSNumber\"8Q16^B24
IOServiceFirstPublish
kCICMaxPerModuleY >= numYCIC
BackSuperWideCameraSNUM
/usr/local/share/firmware/isp/CmPM-brcl
denseLP
w
Expected file %s to be of size %ld. Actual size: %d\n
/usr/local/share/firmware/isp/IFCC.DAT
ISPServicesRemoteIORegPropertyNameKey
pLSCConfig->channelGR.gridCountX == pLSCConfig->channelGB.gridCountX
pLSCConfig->channelGR.gridCountY == pLSCConfig->channelGB.gridCountY
chInfo[ch]->gridCountX == chInfo[0]->gridCountX
IOService
multi-camera-cal-wide
registerDeviceIDForClient
Personalized firmware root path accessor not found
map
token was removed
Could not find SEP reference location. Will use ISP references
Error reading file\n
DAT
DPCm
/usr/local/share/firmware/isp/isp_fw.bin
r
DAT file for unprovisioned Savage - %@
=
/usr/local/share/firmware/isp/CmCl-Override.DAT
IODeviceTree:/arm-io
setProperty
getProperty
/usr/local/share/firmware/isp/4426_01XX.dat
Failed to update %s token file. Will return false so someone looks at that...
PRF1: %s-%s: Unexpected references size (Expected %ld, Got %d)\n
%s/%@
Reading rosaline power from IOReg\n
com.apple.restorecameraispd
property
FWOBJECTSPECIALFUNC
/usr/local/share/firmware/isp/3526_02XX.dat
/usr/local/share/firmware/isp/2022_01XX.dat
ISPServicesRemoteFusingDataKey
/usr/local/share/firmware/isp/2326_01XX.dat
/usr/local/share/firmware/isp/2224_01XX.dat
com.apple.isp
Will use ISP references
ISPServicesRemoteRGBIRMetadataIRKey
No HPR file for frontIR found
BackCameraSNUM
com.apple.private.cameraispd.client
Failed to send PCE calibration to FW\n
Load Savage DAT File: Size = %ld; SendStatus = %08x, FileStatus = 0x%08X
/private/var/tmp/usr/standalone/firmware/YonkersIR/YonkersIR%dPatch.DAT
^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8
false
/usr/local/share/firmware/isp/3526_01XX.dat
/usr/local/share/firmware/isp/8824_01XX.dat
Failed to remove %s token: %@
SavageChipID
/var/mobile/Library/ISP/CalData/DCNUPixbuf_0
UniqueChipID
Failed to read PCE Calibration (FDR data)\n
Trying to load reference file %s (type: %d, index: %d, temperature: %lf)\n
pDevice is NULL
com.apple.cameraispd
chInfo[ch]->gridCountY == chInfo[0]->gridCountY
%s token activation count updated to %d
Failed to read %s projector token file. Token will be removed.
\taFDR may not be used
%s-%s__T_%lf.bin
Reading rosaline power from sysconfig\n
com.apple.isp.backcamerasensorconfig
/usr/local/share/firmware/isp/9723_01XX.dat
CmPM
ISPDevice
ISP_SavageAuth
20.112
/usr/local/share/firmware/isp/2626_02XX.dat
Failed to read boot time. errno %d
Pearl FDR is %s, ToF FDR is %s
Will use SEP references
-sparseLP
Error converting calibrated power value\n
0
Loading DAT file for unprovisioned Savage
AppleCamera
Found no IR sensor\n
Load YonkersIR DAT File: Size = %ld; SendStatus = %08x, 0x%08X
FrontCameraCalSwide
/usr/local/share/firmware/isp/ispane.afpp
%s%s.%s
/usr/local/share/firmware/isp/CmPM-DPCd
DPCd
/usr/local/share/firmware/isp/7327_01XX.dat
ISPServicesRemoteReturnKey
WDDC
cmca
LsAdjustEnableCam%d
LsIdealPctCam%d
<null>
/usr/local/share/firmware/isp/0426_01XX.dat
Number of allowed activations has reached zero. %s token will be removed.
, calibration: 0x
AppleProxHIDEventDriver
floodComplianceRevision
Failed to send Romeo data file: 0x%08X\n
/private/var/tmp/usr/standalone/firmware/Savage/SavagePatch.DAT
DAT file for provisioned Savage - %@
/usr/local/share/firmware/isp/2123_01XX.dat
\tFound\n
Reading rosaline serial number from sysconfig\n
Loading DAT file for unprovisioned Yonkers
Found FrontIR override (has highest precedence) HPR file - camChannel = %d
pCmdAppleChVACICConfigure->numTables <= CISP_VA_CIC_MAX_TABLES
LoadFDRDataFileCMPM
<UNKNOWN>
/usr/local/share/firmware/isp/8127_01XX.dat
/usr/local/share/firmware/isp/2727_01XX.dat
general
\tCan't create %s! (%d)\n
\tValidating Calibration UUID
LoadPDEFiles: No Savage found. Never mind
Failed to send references to FW\n
This is%s an internal build, and FDR was%s validated\n
%s - powering on camera\n
%s - kernel config count %d != firmware %d - chan: %d\n
Received XPC_ERROR_TERMINATION_IMMINENT error from client (pid %{private}d)\n
%s - IONotificationPortCreate returned NULL\n
%s - No module or No DspB data (perhaps cuz the device does not support DspB). Skip loading FDR DspB calibration data\n
Sent ISP-ANE networks file to kernel: Size = %ld (== %ld ?); Status = %08x\n
%s - No module or No iCCl data (perhaps cuz the device does not support iCCl). Skip loading FDR iCCl calibration data\n
Received XPC_ERROR_CONNECTION_INTERRUPTED error from client (pid %{private}d)\n
Unable to begin server for isp\n
Setting FW property 0x%08x to 0x%08X\n
%s - kMGQFrontCameraOffsetFromDisplayCenter Description=%s\n
%s - Success: cached configs - numChannels: %d\n
Removing client: pid %{private}d\n
%s: %d: Sending reply to client: rc %08X (pid %{private}d)\n
Received unexpected event: %s\n
%s - snfRadialGains command not in setfile for ch %d\n
%s: Data file load failed, status = 0x%x\n
%s : Load override %s cal data: Size = %ld (== %ld ?); Status = %08x\n
%s - FCCl standalone loaded: Channel = %d, Status = %#08x\n
%s - no channels detected - exiting\n
%s - maxChannels=%d, timeStampFrequency=%d\n
%s - failed to get SoC generation from the device tree\n
%s - %d complete (res=0x%08X)\n\n
Trying to use override SecureSensorPatchOverride.DAT file\n
%s - %s loaded: Channel = %d, Status = %#08x\n
%s - Initializing device configuration cache\n
Audit: XPC peer missing %{public}s (pid %{private}d) — would reject\n
Error creating ISPDeviceController object: %08X\n
%s - channel configs not valid - exiting\n
%s - IONotificationPortGetRunLoopSource returned NULL\n
%s - snfRadialGains not enabled for ch %d\n
Error: too many camera sensor register over-rides in file\n
could not read channel %d sensor key provisioning file entirely\n
Couldn't read back camera module serial number. Sensor is hosed/disconnected. Skip loading OCCl calibration data\n
Could not set CIL Brightness to %u\n\n
%s - Status = %08x; HPR - %s\n
%s: Savage Auth failed, status = 0x%x\n
%s - type=0x%X, isOverride=%d, size=%u, isEarlyBoot=%d, status=%08x\n
Client disconnecting (pid %{private}d)\n
%s - Couldn't read front camera module serial number. Sensor is hosed/disconnected. Skip loading FCCl cal data\n
%s - No module or Unauthorized swap (icclStatus = 0x%x) or No iCCl data (perhaps cuz the device does not support iCCl) [error]: %s\n
could not read ISPCPU Firmware file\n
error sending camera channel %d over-ride NVM bytes to kernel: 0x%08X\n
Failure loading override ISPUnitInfo property list : CFPropertyListCreateWithStream failed\n
No ALS2 profile found in Setfile\n
Could not send FW Ideal Percent for LSC channel[%u], returned:0x%08x - ignoring error\n
%s - status: 0x%08X\n
%s - No module or Unauthorized swap (cmpmStatus = 0x%x) or No CmPM data (perhaps cuz the device does not support CmPM) [error]: %s\n
(Bin) Loading ISPCPU firmware file: %s\n
LSC Orientation cam%d, flip = %d, invert = %d, useSetfile = %d, flipSetfile = %d, flipPerModule = %d rotateAls2Profile = %d enableGreenAvg = %d interpMode = %d  idealPct = %d DCS=%d XHatch=%d\n\n
%s - status: %08x\n
Active client pid %{private}d deviceID %{private}s\n
Total number of connections: %lu\n
%s: Could not power off the ISP, res = 0x%x\n
Received XPC_ERROR_CONNECTION_INVALID error on connection\n\n
ISPServicesRemote: GetProperty (%d) (sent)\n
UpdateChannelConfigCache channel %d error: 0x%08X\n
Failed to load Bin-format firmware binary: 0x%08x\n
%s: Savage Pre Auth failed, status = 0x%x\n
%s - client already has a registered device ID\n
Unable to create mach service\n
%s - LSCComputeSNFVerticalGains: null ptr! pRadialGainAsymScaleSet.\n
Found camera clock override information file for camera channel %d\n
%s - Camera powered on...waiting\n
Failed to copy model string from MobileGestalt\n
%s: Invalid data file arguments\n
backCameraModuleSerialNumString exists - load FDR CmCl calibration data\n\n
Error sending ISP-ANE networks file to kernel: Size = %ld (== %ld ?); Status = %08x\n\n
%s - cache is already invalid - exiting\n
%s - failed to load firmware ret=0x%08x\n
%s - [error]: %s\n
Using override ISP-ANE AFPP file\n
backTeleCameraModuleSerialNumString exists - load OCCl calibration data\n\n
%s: Could not release channel, res = 0x%x\n
Error: SetSensorCustomSettings returned an error: 0x%08X\n
%s - Status = %#08x; CmCl data - %s\n
%s - Error reading kernel config cache - chan: %d, res: 0x%08X\n
%s - ret=%#x\n
%s - Rear camera not supported on this device\n
New connection: pid %{private}d\n
%s - Error %x loading FW\n
%s - LoadSetFile returned 0x%08x\n
%s - %d configurations detected for channel %d\n
Received unexpected error from client (pid %{private}d)\n
Received SIGTERM - exiting\n
Destroying ISP services assistant\n
createXpcFromType got a dictionary with null value (for key %s)
%s - Could not forget firmware, res = %x\n
No valid channel %d key provisioning file to send\n
%s - No module or Unauthorized swap (cmclStatus = 0x%x) or No CmCL data (perhaps cuz the device does not support CmCL) [error]: %s\n
%s OCCl is not a dict (FDR2.0?), Unauthorized swap or No OCCl data (perhaps cuz the device does not support OCCl) [error]: %s \n
Couldn't read %s. Sensor is hosed/disconnected.\n
%s - Error getting channel info - chan: %d, res: 0x%08X\n
%s - SoC generation from the device tree is invalid!\n
%s - ISP_GetCameraStatus error (0x%08x)\n
%s - NVM not valid for camera %d sensorId = %x  %d\n
%s - poweredOn=%d, poweredOff=%d, res=0x%08X\n
Loaded calibration file from override path: %s\n
%s - caching device configurations\n
%s: Could not reserve channel, res = 0x%x\n
Unexpected client message=%d (pid %{private}d)\n
Received XPC_ERROR_CONNECTION_INTERRUPTED error on connection\n\n
%s - FTC gain buffer allocation failed\n
Bin ISPCPU firmwareFile does not exist %s\n\n
New connection: kernel\n
Error opening ISPDevice: %08X\n
using sensor setfile from file for camera %d: %s\n
%s - lsc adjustment not enabled for %x. lsc enabled = %d\n
Removing client: kernel\n
%s - %d\n
Received XPC_ERROR_TERMINATION_IMMINENT, cleaning up assistant\n\n
%s - received reply\n
could not read sensor SetFile\n
Successfully sent camera %d sensor register over-ride values for %d registers\n
Received unknown event from client (pid %{private}d)\n
%s - Collecting ISP Sysdiagnose State\n
%s - Assistant Version %s\n
LoadSetFile returned 0x%08x - ignoring error\n
%s : Status = %08x; OCCl (%s) data - %s \n
%s - No iCCl data found, will attempt FCCl fallback processing\n
Unexpected client Get data length=%zu expected=%zu (pid %{private}d)\n
Error parsing camera clock override file\n
%s - Failed to copy kMGQFrontCameraOffsetFromDisplayCenter answer from MobileGestalt! err=%d\n
%s: Invalid connection\n
%s - Couldn't read back camera module serial number. Sensor is hosed/disconnected. Skip loading FDR CmCl calibration data\n
%s:%s exists, length of the string = %ld.\n\n
No module or No CmPM data (perhaps cuz the device does not support CmPM). Skip loading FDR CmPM calibration data\n
sending camera channel %d over-ride NVM bytes to kernel (%d bytesn\n
%s - received error reply: %s\n
%s - Parsing ISPUnitInfo.plist\n
%s - Error: resetting device config cache - res: 0x%08X\n
Error opening ISP-ANE networks file\n
%s - ISP_GetNumChannels failed with 0x%08x\n
Error setting FW property: 0x%08x\n
Loading file for ISP-ANE networks - %s\n
%s - type=0x%X, isOverride=%d, file=%s, size=%u, isEarlyBoot=%d, status=%08x\n
%s - Load override cal data: File = %s, Size = %ld (== %ld ?); Status = %08x (cmclStatus = 0x%08x)\n
%s - ISP command not permitted\n
ISP still in use by another session; keeping shared interface open\n
%s - noHPR boot-arg set\n
%s - Error getting config - res: 0x%08X\n
Load data file: channel: %d, type: %d, isEarlyBootDataFile: %s, status: %08x\n\n
Unable to look up remote connection (pid %{private}d)\n
Failed to fetch handle for %s with return code = 0x%08x\n
Using override SecureSensorPatchOverride.DAT file\n
%s - Trying to use %s: Size = %lld (== %lld ?);\n
FrontCameraModuleSerialNumString exists - load OCCl calibration data\n\n
%s - No module or Unauthorized swap (DspBStatus = 0x%x) or No DspB data (perhaps cuz the device does not support DspB) [error]: %s\n
%s - %s\n
Rejecting XPC peer missing %{public}s (pid %{private}d)\n
Unable to initialize services\n
%s - Using %s from unit info plist\n
bypassing sending over-ride NVM bypass from unit-info plist for channel %d (mask bit not set)\n
%s - %s - length = %ld; status = %08x\n
camChannel: %d, cmpmInstance: %s\n
Camera powered on...waiting\n
Failed to crate SIGTERM dispatch source\n
Creating ISP services assistant\n
%s - Timed out waiting for the driver to register service, deviceArrived = %d\n
%s - Did not find platform-info for platform:%d. Defaulting to 0\n
%s - received invalid reply\n
ISPServicesRemote: GetProperty (%d) (reply=0x%08X)\n
Set clock divider reg to 0x%08X\n
Set sensor reg 0x%08x to val 0x%08X\n
%s: Could not power on the ISP, res = 0x%x\n
%s: Savage Auth failed, res = 0x%x\n
Unexpected client Set data length=%zu expected=%zu (pid %{private}d)\n
Unable to create reply dictionary (pid %{private}d)\n
stringFromDate:
dictionaryWithContentsOfFile:
numberWithUnsignedInt:
allKeys
UTF8String
defaultManager
description
dictionaryWithObjects:forKeys:count:
initWithContentsOfFile:
sharedDataAccessor
stringByAppendingString:
containsObject:
enumerateObjectsUsingBlock:
setDateFormat:
removeItemAtPath:error:
setAttributes:ofItemAtPath:error:
copyPathForPersonalizedData:error:
date
getBytes:length:
length
objectForKey:
sortDescriptorWithKey:ascending:
stringWithUTF8String:
arrayWithObjects:count:
copyPathForPersistentData:error:
contentsOfDirectoryAtPath:error:
dataWithContentsOfFile:
intValue
stringWithFormat:
writeToFile:atomically:
stringByAppendingPathComponent:
countByEnumeratingWithState:objects:count:
setObject:forKey:
stringByAppendingFormat:
doubleValue
fileExistsAtPath:
sortedArrayUsingDescriptors:
```
