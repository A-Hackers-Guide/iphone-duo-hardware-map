# `/usr/sbin/dietappleh16camerad`

From the upgrade restore ramdisk (141-29011-104.dmg). 3,973,472 bytes.

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
		<string>AppleH16CamInUserClient</string>
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
		<string>AppleH16PhotonDetectorUserClient</string>
		<string>IOUserClient</string>
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

## Strings (632)

```
Failed to read unique chip identifier
%s/reference-%s.plist
Error reading file\n
Yonkers/YonkersPatch%s%s.DAT
:
ISP_SendCommand
6.104
\tFailed to initialize Manifest from ticket
H16ISPServicesRemoteRGBIRReportKey
H16ISPServicesRemoteRGBIRBufferIRKey
Load Savage DAT File: Size = %ld; SendStatus = %08x, FileStatus = 0x%08X
ISP_ColdBootPowerCycle
CopyFileToBuffer
CALm
a
product
Error: Couldn't send rosaline configuration\n
SendDataFileToFirmware
/usr/local/share/firmware/isp/7525_01XX.dat
%lld
unified
kGICMaxPerModuleX >= numXGIC
/usr/local/share/firmware/isp/
ISP_LoadIspAneAFPPFile
Failed to update %s token file. Will return false so someone looks at that...
Failed to open token log file.
general
AppleProxHIDEventDriver
device
/usr/local/share/firmware/isp/Savage/FrontIRHPR.DER
Couldn't create SavageChipID string ref
multi-camera-cal-swide
Saving %s\n
Reading rosaline power from IOReg\n
Sending rosaline configuration: SN: %s; Power: %d\n
true
No DAT file for Savage found
ValidateProjectorToken
ISP_PowerOnCamera
chInfo1[ch]->gridCountY == chInfo1[0]->gridCountY
\tCouldn't validate directories\n
wb
v16@?0^v8
n't
cmcd
pLSCConfig->channelGR.gridCountY == pLSCConfig->channelGB.gridCountY
/usr/local/share/firmware/isp/8825_01XX.dat
/usr/local/share/firmware/isp/3624_01XX.dat
%s token does not match device. Token will be removed.
Ymgt
pCmdAppleChLSCConfigure->tableSize == pCmdAppleChDSCConfigure->numEntries
com.apple.isp.frontcamerapower
Sending special debug function to firmware object returned error : 0x%08x\n
LoadFDRCalDataFile
/usr/local/share/firmware/isp/7623_01XX.dat
\tCouldn't get boot manifest hash
\tCrypto hash method is %@. Only %s is supported
IR sensor not detected
Prod
isp-command-send
collectDiagState
/usr/local/share/firmware/isp/2022_01XX.dat
Can't activate %s projector: no projector token found
H16ISPServicesRemoteDeviceID
com.apple.isp.backtelecamerapower
DPCm
com.apple.coremedia
/usr/local/share/firmware/isp/2820_01XX.dat
%s token doesn't match platform. Token will be removed.
sparse
not unified
Error converting vader compliance value\n
InitDeviceConfigsCache
Couldn't read from FDR: %@
Error: Couldn't send NVM\n
Failed to send references to FW\n
H16ISPServicesRemoteRGBIRFinalOutputPCEConfigKey
Couldn't create SavageUID string ref
/usr/local/share/firmware/isp/6221_01XX.dat
/var/mobile/Library/ISP/Pearl
com.apple.isp.backcamerasensorconfig
/usr/local/share/firmware/isp/ispane.afpp
%s token timeout was reached (current time %ld). Token will be removed.
Dev
FrontCameraModuleSerialNumString
dcnu
LoadPDEFiles: isOverridden %d
H16ISPServicesRemoteRGBIRBufferDepthKey
OCCl
LSCAverageGreenApple
services
\tValidating Calibration UUID
H16ISPServicesRemoteRGBIRMetadataIRKey
WDDC
brgd
/usr/local/share/firmware/isp/CmPM-DPCm
/usr/local/share/firmware/isp/dcs_v5x_isp_fw.bin
setProperty
false
/
no
com.apple.iokit.matching
sha2-384
AppleH16CamIn
Error converting calibrated power value\n
/usr/local/share/firmware/isp/cam%dsetfile.dat
kGICMaxPerModuleY >= numYGIC
%s-Ch%d.DAT
H16ISPServicesRemoteIORegPropertyDataKey
GICComputeFromNVMApple
w
\tCouldn't get crypto hash method
\tReading from FDR\n
Couldn't read unified Pearl FDR: %@
/System/Library/PrivateFrameworks/AppleCVHWA.framework/Firmware/lacc_VIO_ISP_IR.bin
/usr/local/share/firmware/isp/3524_01XX.dat
Failed to read unique chip ID
%s token activation count updated to %d
, calibration: 0x
IOService
H16ISPServicesRemoteTypeKey
SavageMNS
ChannelArray
/usr/local/share/firmware/isp/1020_03XX.dat
System performed boot since %s token creation (boot time: %ld). Token will be removed.
DAT file for provisioned Yonkers - %@
Found FrontIR override (has highest precedence) HPR file - camChannel = %d
isp_lacc.bin
/usr/local/share/firmware/isp/OCCl-cmcd.DAT
/usr/local/share/firmware/isp/CmPM-brgd
/usr/local/share/firmware/isp/FCCl-Override.DAT
/usr/local/share/firmware/isp/1922_02XX.dat
Testing if aFDR may be used
Creating local cache\n
clockdiv
LsBypassVerify
IgnoreUnitInfoPlist
com.apple.appleh16camerad
EnforceClientEntitlement
Pearl
rb
denseLP
/usr/local/share/firmware/isp/CmPM-dcnu
com.apple.dietappleh16camerad.writer
pLSCConfig->channelGR.gridCountX == pLSCConfig->channelGB.gridCountX
rosaline-serial-num
H16ISPServicesRemoteCFTypeDataKey
/private/var/tmp/usr/standalone/firmware/Savage/SavagePatch.DAT
YonkersMNS
/usr/local/share/firmware/isp/7524_01XX.dat
Failed to create log message string with code: %d (0x%X)
\tIgnoring unexpected cached version (%d != %d)\n
Found no IR sensor\n
rosaline-calibration-current
LoadHPR
chInfo1[ch]->gridCountX == chInfo1[0]->gridCountX
 :
/usr/local/share/firmware/isp/4425_01XX.dat
/usr/local/share/firmware/isp/2224_01XX.dat
Couldn't read SavageUID
GetUnitInfoPropertyDict
com.apple.isp.backsuperwidesensorconfig
/usr/local/share/firmware/isp/OCCl-cmca.DAT
/usr/local/share/firmware/isp/CmPM-DPCd
<null>
/usr/local/share/firmware/isp/2325_01XX.dat
\tCan't create %s! (%d)\n
Failed to load PDE files\n
Personalized firmware root path accessor not found
LsEnableGreenAvg
UniqueChipID
Image4CryptoHashMethod
com.apple.dietappleh16camerad.launch
Using last allowed activation. %s token will be removed.
/var/mobile/Documents/Pearl/ProjectorValid.bin
Couldn't create reference file %s to write\n
SWDC
/usr/local/share/firmware/isp/4524_01XX.dat
/usr/local/share/firmware/isp/2226_02XX.dat
/usr/local/share/firmware/isp/6222_01XX.dat
%s/%s.bin
unavailable
/var/mobile/Library/ISP/Pearl/
Failed to send Romeo data file: 0x%08X\n
Failed to send rosaline data file: 0x%08X\n
/usr/local/share/firmware/isp/0019_02XX.dat
/usr/local/share/firmware/isp/2123_01XX.dat
/usr/local/share/firmware/isp/0225_01XX.dat
\tLooking for local cache\n
%02X
FormatDR
Could not read calibrated power from sysconfig\n
com.apple.h16ispdevicecontroller.notifications.queue
No HPR file for frontIR found
iCCl
H16ISPDevice.cpp
HWModelStr
/usr/local/share/firmware/isp/Savage/SavagePatchOverride.DAT
DAT
LsAdjustEnableCam%d
LSCComputeFromNVM.cpp
H16ISPServicesRemoteDataKey
LoadFrontIRHPRFile
multi-camera-cal-wide
/ispane.afpp
BackTeleCameraModuleSerialNumString
DPCd
LoadFDRDataFileCMPM
CacheDeviceConfigs
Unexpected references size (Expected %ld, Got %d)\n
Loading DAT file for unprovisioned Yonkers
Special function: name: %s, parameters %llu %llu %llu %llu\n
token was removed
yyyy-MM-dd HH:mm:ss
\tCouldn't find AP ticket file at path %@
Unexpected references size after compression (Expected %ld, Got %ld)\n
H16ISPServicesRemoteRGBIRFinalInputPCEConfigKey
Cached UUID: 0x
Failed to send PCE calibration to FW\n
reference
Couldn't read SavageChipID
MultiCameraCalSwide
CmPM
LSC_GET_BASE_U32_PT(chInfo1[ch]) % (chInfo1[ch]->gridCountX * chInfo1[ch]->gridCountY) == 0
kCICMaxPerModuleY >= numYCIC
/usr/local/share/firmware/isp/7324_01XX.dat
\tFailed to digest AP ticket
\t%@
v8@?0
H16ISPServicesRemoteCFTypeNameKey
Found Savage override DAT file, which takes precedence over all others - %@
Load Yonkers DAT File: Size = %ld; SendStatus = %08x, 0x%08X
FCCl
Found reference plist at %s. Will use SEP references
BackCameraSNUM
/usr/local/share/firmware/isp/isp_fw.bin
LsAdjustInvertCam%d
LsIdealPctCam%d
H16ISPServicesRemoteFusingDataKey
com.apple.dietappleh16camerad.assistant_active
LSCComputeSNFVerticalGains
/usr/local/share/firmware/isp/4723_01XX.dat
/usr/local/share/firmware/isp/9723_01XX.dat
%s/%@
BackCameraModuleSerialNumString
<UNKNOWN>
/System/Library/PrivateFrameworks/AppleCVHWA.framework/Firmware/
soc-generation
%s token has exceeded max allowed timeout. Token will be removed.
/var/mobile/Documents/Pearl
\tFailed to read UUID. Marking as invalid
DAT file for unprovisioned Yonkers - %@
/Yonkers/YonkersPatch.DAT
SavageChipID
NVM
LSC_GET_BASE_U32_PT(chInfo2[ch]) % (chInfo2[ch]->gridCountX * chInfo2[ch]->gridCountY) == 0
/usr/local/share/firmware/isp/4523_01XX.dat
/var/mobile/Library/ISP
com.apple.dietappleh16camerad.firmware_loading
LsInterpMode
getProperty
r
sparseLP
Savage/SavagePatch%s.DAT
MultiCameraCalWide
CopyAllowUnsealed
chInfo2[ch]->gridCountX == chInfo2[0]->gridCountX
com.apple.isp.backcamerapower
/usr/local/share/firmware/isp/cam%dclocks.txt
/usr/local/share/firmware/isp/9724_01XX.dat
Number of allowed activations has reached zero. %s token will be removed.
Could not find reference plist at %s (errno: %d). Will use ISP references
Found Yonkers override DAT file, which takes precedence over all others - %@
H16ISPDevice
=
 \n
property
/usr/local/share/firmware/isp/7424_01XX.dat
H16ISPServicesRemoteRGBIRPCEConfigKey
No DAT file for Yonkers found
com.apple.isp.backsuperwidecamerapower
cmca
BackSuperWideCameraSNUM
/usr/local/share/firmware/isp/CmPM-brcl
UnitInfoNVMChannelMask
/usr/local/share/firmware/isp/2226_01XX.dat
Reading rosaline power from sysconfig\n
DAT file for unprovisioned Savage - %@
/Savage/SavagePatch.DAT
com.apple.isp.frontirsensorpower
/var/mobile/Library/ISP/CalData/DCNUMetadata_0
registerDeviceIDForClient
com.apple.private.appleh16camerad.client
/usr/local/share/firmware/isp/3624_02XX.dat
\taFDR may be used
Reading rosaline serial number from sysconfig\n
isp
Load: 0x%08x\n
sendMessageSync
SavageDeviceRev
sensor-type
\tFound\n
\tLooking for FDR data\n
Loading DAT file for unprovisioned Savage
Couldn't combine frontIR chipIDStr and uidStr
FrontCameraCalSwide
kCICMaxPerModuleX >= numXCIC
com.apple.isp.cameratorchwarmcurrent
FWOBJECTSPECIALFUNC
/usr/local/share/firmware/isp/3525_02XX.dat
/usr/local/share/firmware/isp/1921_01XX.dat
BootManifestHash
Pearl calibration\n
\tLooking for local override files\n
%lf
yes
%@-%@
com.apple.isp
front-camera-cal-swide
com.apple.isp.frontcamerasensorconfig
/usr/local/share/firmware/isp/Yonkers/YonkersPatchOverride.DAT
AP
LoadOCClCalDataFile
/var/mobile/Library/ISP/CalData/DCNUPixbuf_0
brcl
/usr/local/share/firmware/isp/8824_01XX.dat
Failed to read %s projector token file. Token will be removed.
LoadPDEFiles: No Savage found. Never mind
DAT file for provisioned Savage - %@
com.apple.isp.cameratorchcoolcurrent
No C string description.
BackTeleCameraSNUM
%s%s/%s
/usr/local/share/firmware/isp/7425_01XX.dat
%@ %s\n
\tDidn't find calibration\n
SavageSNUM
v32@?0@\"NSNumber\"8Q16^B24
H16ISPServicesThread
pDevice is NULL
/usr/local/share/firmware/isp/CmPM-CALm
/usr/local/share/firmware/isp/4523_02XX.dat
/usr/local/share/firmware/isp/1925_03XX.dat
Expected file %s to be of size %ld. Actual size: %d\n
floodComplianceRevision
FrontCameraOffsetFromDisplayCenter
ISP_SetFrontCameraOffsetFromDisplayCenter
/usr/local/share/firmware/isp/dcs_isp_fw.bin
H16ISPServicesRemoteIORegPropertyNameKey
/var/mobile/Documents/Tokens.log
H16ISPServicesRemoteReturnKey
Secure RGB sensor not detected
SavageUID
DisableDropDetection
GetSoCGeneration
/usr/local/share/firmware/isp/2924_01XX.dat
\tAP ticket digest doesn't match boot manifest hash
Error converting calibrated power value:  could not fit 32-bit value into 16-bit destination \n
DEV
ISP_SavageAuth
FCDC
/usr/local/share/firmware/isp/CmCl-Override.DAT
^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8
reference-%s__T_%lf.bin
/var/mobile/Library/ISP/Pearl/spotDB.bin
floodCalibrationCurrent
SetupDeviceController
YonkersFabRevision
CmCl
LoadFDRFCClDataFile
IODeviceTree:/arm-io
/var/mobile/Library/ISP/Pearl/PCECalib.bin
dense
Unable to find prox service
basic_string
SendSysConfigCalibrationDataByKey
fdrLogMessages
xpcClientEventHandler
EnableHawking
Failed to save plist
Reading rosaline power from FDR\n
doubleValue
error loading ISPCPU firmware 
deviceFirmwareLoad
Could not find SEP reference location. Will use ISP references
Failed to read PCE Calibration (FDR data)\n
%s%s.%s
chInfo[ch]->gridCountX == chInfo[0]->gridCountX
LSC_GET_BASE_U32_PT(chInfo[ch]) % (chInfo[ch]->gridCountX * chInfo[ch]->gridCountY) == 0
\tCalibration UUID mismatch, removing contents of directory\n
Sending reference file %s, type: %d\n
com.apple.dietappleh16camerad.destroy
com.apple.dietappleh16camerad.photometerManagerSyncQueue
/usr/local/share/firmware/isp/3525_01XX.dat
/var/mobile/Library/ISP/Pearl/NVM.bin
References for %s: Decompressing references\n
H16ISPServicesRemoteRGBIRMetadataColorKey
/usr/local/share/firmware/isp/ISPUnitInfo.plist
IOGeneralInterest
/usr/local/share/firmware/isp/2921_02XX.dat
 not
com.apple.isp.backtelecamerasensorconfig
com.apple.isp.cameratorch
Failed to read boot time. errno %d
Pearl FDR is %s, ToF FDR is %s
Could not read calibrated power from IOReg\n
Trying to load reference file %s (type: %d, index: %d, temperature: %lf)\n
Could not open input file: %s\n
/private/var/tmp/usr/standalone/firmware/Yonkers/YonkersPatch.DAT
/System/Library/Isp/afpp/
Couldn't read vader compliance\n
Couldn't read serial number\n
H16ISPServicesRemoteRGBIRBufferColorKey
com.apple.dietappleh16camerad
RadialGainEnable
chInfo[ch]->gridCountY == chInfo[0]->gridCountY
/usr/local/share/firmware/isp/3623_01XX.dat
\taFDR may%s be used (%d, %d)
-sparseLP
IOServiceFirstPublish
0
Ngsk
daemon
chInfo2[ch]->gridCountY == chInfo2[0]->gridCountY
Failed to remove %s token: %@
%s - Could not forget firmware, res = %x\n
No valid Yonkers key provisioning file to send\n
%s - No module or Unauthorized swap (fcclStatus = %#x) or No FCCL data (perhaps cuz the device does not support FCCL) [error]: %s\n
Unable to create reply dictionary (pid %{private}d)\n
bypassing sending over-ride NVM bypass from unit-info plist for channel %d (mask bit not set)\n
Failed to fetch handle for %s with return code = 0x%08x\n
could not read sensor SetFile\n
Error parsing camera clock override file\n
Unexpected client Get data length=%zu expected=%zu (pid %{private}d)\n
Unexpected client message=%d (pid %{private}d)\n
Received unexpected error from client (pid %{private}d)\n
%s - lsc adjustment not enabled for %x. lsc enabled = %d\n
Couldn't read back camera module serial number. Sensor is hosed/disconnected. Skip loading OCCl calibration data\n
%s - cache is already invalid - exiting\n
New connection: kernel\n
%s - [error]: %s\n
UpdateChannelConfigCache channel %d error: 0x%08X\n
%s - FTC gain buffer allocation failed\n
LSC Orientation cam%d, flip = %d, invert = %d, useSetfile = %d, flipSetfile = %d, flipPerModule = %d rotateAls2Profile = %d enableGreenAvg = %d interpMode = %d  idealPct = %d\n\n
Error: too many camera sensor register over-rides in file\n
Error opening ISP-ANE networks file\n
%s - Couldn't read front camera module serial number. Sensor is hosed/disconnected. Skip loading FCCl cal data\n
Found camera clock override information file for camera channel %d\n
Error setting FW property: 0x%08x\n
Set sensor reg 0x%08x to val 0x%08X\n
Using override SavagePatchOverride.DAT file\n
backCameraModuleSerialNumString exists - load FDR CmCl calibration data\n\n
Set clock divider reg to 0x%08X\n
Sent ISP-ANE networks file to kernel: Size = %ld (== %ld ?); Status = %08x\n
%s - Error getting channel info - chan: %d, res: 0x%08X\n
%s - Error getting camera config - chan: %d, res: 0x%08X\n
Successfully sent camera %d sensor register over-ride values for %d registers\n
could not read Yonkers key provisioning file entirely\n
No valid Savage firmware file to send\n
camChannel: %d, cmpmInstance: %s\n
%s - Error: resetting device config cache - res: 0x%08X\n
%s - failed to get SoC generation from the device tree\n
Couldn't read %s. Sensor is hosed/disconnected.\n
%s - Load override cal data: File = %s, Size = %ld (== %ld ?); Status = %#08x (fcclStatus = %#08x)\n
%s - Collecting ISP Sysdiagnose State\n
Failure loading override ISPUnitInfo property list : CFPropertyListCreateWithStream failed\n
%s - ISP_GetNumChannels failed with 0x%08x\n
%s: Savage Pre Auth failed, status = 0x%x\n
%s - Using %s from unit info plist\n
%s: Could not power off the ISP, res = 0x%x\n
%s - kMGQFrontCameraOffsetFromDisplayCenter Description=%s\n
H16ISPServicesRemote: GetProperty (%d) (reply=0x%08X)\n
This is%s an internal build, and FDR was%s validated\n
%s: Savage Auth failed, status = 0x%x\n
%s - Front camera not supported on this device\n
Load firmware from %s\n\n
%s - Error getting config - res: 0x%08X\n
%s - %d complete (res=0x%08X)\n\n
%s - IONotificationPortCreate returned NULL\n
H16ISPServicesRemote: GetProperty (%d) (sent)\n
No ALS2 profile found in Setfile\n
%s - Failed to copy kMGQFrontCameraOffsetFromDisplayCenter answer from MobileGestalt! err=%d\n
%s: Invalid connection\n
%s - type=0x%X, isOverride=%d, file=%s, size=%u, isEarlyBoot=%d, status=%08x\n
FrontCameraModuleSerialNumString exists - load OCCl calibration data\n\n
Rejecting XPC peer missing %{public}s (pid %{private}d)\n
Unable to begin server for isp\n
%s - Did not find platform-info for platform:%d. Defaulting to 0\n
Failed to copy model string from MobileGestalt\n
could not read Savage firmware file entirely\n
Loaded calibration file from override path: %s\n
%s : Status = %08x; OCCl (%s) data - %s \n
No module or No CmPM data (perhaps cuz the device does not support CmPM). Skip loading FDR CmPM calibration data\n
%s - status: %08x\n
%s - NVM not valid for camera %d sensorId = %x  %d\n
%s - No module or Unauthorized swap (cmclStatus = 0x%x) or No CmCL data (perhaps cuz the device does not support CmCL) [error]: %s\n
Active client pid %{private}d deviceID %{private}s\n
%s: Could not release channel, res = 0x%x\n
Received XPC_ERROR_TERMINATION_IMMINENT error from client (pid %{private}d)\n
Received unknown event from client (pid %{private}d)\n
Received SIGTERM - exiting\n
LoadSetFile returned 0x%08x - ignoring error\n
Using override ISP-ANE AFPP file\n
New connection: pid %{private}d\n
Camera powered on...waiting\n
Setting FW property 0x%08x to 0x%08X\n
%s - Camera powered on...waiting\n
Removing client: kernel\n
%s: Savage Auth failed, res = 0x%x\n
%s: %d: Sending reply to client: rc %08X (pid %{private}d)\n
Unable to create mach service\n
Trying to use SavagePatchOverride.DAT file\n
Audit: XPC peer missing %{public}s (pid %{private}d) — would reject\n
%s - ISP_GetCameraStatus error (0x%08x)\n
FrontCameraModuleSerialNumString exists - load FDR FCCl calibration data\n\n
Could not set CIL Brightness to %u\n\n
Error opening H16ISPDevice: %08X\n
sending camera channel %d over-ride NVM bytes to kernel (%d bytesn\n
%s - Timed out waiting for the driver to register service, deviceArrived = %d\n
%s - received reply\n
%s - poweredOn=%d, poweredOff=%d, res=0x%08X\n
%s - Trying to use %s: Size = %lld (== %lld ?);\n
backTeleCameraModuleSerialNumString exists - load OCCl calibration data\n\n
(Bin) Using ISPCPU firmware override file\n
Unable to initialize services\n
Error sending ISP-ANE networks file to kernel: Size = %ld (== %ld ?); Status = %08x\n\n
%s - Rear camera not supported on this device\n
%s - Error getting LSC polynomial - chan: %d, res: 0x%08X\n
%s - Error %x loading FW\n
%s OCCl is not a dict (FDR2.0?), Unauthorized swap or No OCCl data (perhaps cuz the device does not support OCCl) [error]: %s \n
could not read ISPCPU Firmware file\n
%s - %s\n
Unable to look up remote connection (pid %{private}d)\n
%s - IONotificationPortGetRunLoopSource returned NULL\n
%s - powering on camera\n
%s - LoadSetFile returned 0x%08x\n
%s: Data file load failed, status = 0x%x\n
%s - client already has a registered device ID\n
Total number of connections: %lu\n
Removing client: pid %{private}d\n
Received XPC_ERROR_TERMINATION_IMMINENT, cleaning up assistant\n\n
%s - received error reply: %s\n
Error: SetSensorCustomSettings returned an error: 0x%08X\n
%s - status: 0x%08X\n
Trying to use override YonkersPatchOverride.DAT file\n
Using override YonkersPatchOverride.DAT file\n
%s - No module or Unauthorized swap (cmpmStatus = 0x%x) or No CmPM data (perhaps cuz the device does not support CmPM) [error]: %s\n
%s - Parsing ISPUnitInfo.plist\n
%s - %s - length = %ld; status = %08x\n
%s - no channels detected - exiting\n
%s: Could not power on the ISP, res = 0x%x\n
Received unexpected event: %s\n
%s - snfRadialGains not enabled for ch %d\n
Failed to load Bin-format firmware binary: 0x%08x\n
%s - Couldn't read back camera module serial number. Sensor is hosed/disconnected. Skip loading FDR CmCl calibration data\n
%s:%s exists, length of the string = %ld.\n\n
%s - caching device configurations\n
Destroying H16ISP services assistant\n
%s - SoC generation from the device tree is invalid!\n
Received XPC_ERROR_CONNECTION_INVALID error on connection\n\n
%s - failed to load firmware ret=0x%08x\n
Client disconnecting (pid %{private}d)\n
Error creating H16ISPDeviceController object: %08X\n
%s - received invalid reply\n
%s: Invalid data file arguments\n
%s - maxChannels=%d, timeStampFrequency=%d\n
%s - ISP command not permitted\n
%s - Assistant Version %s\n
%s - Status = %08x; HPR - %s\n
%s - snfRadialGains command not in setfile for ch %d\n
%s - type=0x%X, isOverride=%d, size=%u, isEarlyBoot=%d, status=%08x\n
%s - Initializing device configuration cache\n
Received XPC_ERROR_CONNECTION_INTERRUPTED error from client (pid %{private}d)\n
Received XPC_ERROR_CONNECTION_INTERRUPTED error on connection\n\n
Failed to crate SIGTERM dispatch source\n
%s - noHPR boot-arg set\n
using sensor setfile from file for camera %d: %s\n
%s : Load override %s cal data: Size = %ld (== %ld ?); Status = %08x\n
%s - %d configurations detected for channel %d\n
Load data file: channel: %d, type: %d, isEarlyBootDataFile: %s, status: %08x\n\n
%s - %d\n
%s - LSCComputeSNFVerticalGains: null ptr! pRadialGainAsymScaleSet.\n
Loading file for ISP-ANE networks - %s\n
%s - Status = %#08x; FCCl data - %s\n
%s - Success: cached configs - numChannels: %d\n
%s: Could not reserve channel, res = 0x%x\n
Unexpected client Set data length=%zu expected=%zu (pid %{private}d)\n
%s - ret=%#x\n
error sending camera channel %d over-ride NVM bytes to kernel: 0x%08X\n
%s - Status = %#08x; CmCl data - %s\n
Creating H16ISP services assistant\n
Could not send FW Ideal Percent for LSC channel[%u], returned:0x%08x - ignoring error\n
%s - Load override cal data: File = %s, Size = %ld (== %ld ?); Status = %08x (cmclStatus = 0x%08x)\n
length
objectForKey:
sharedDataAccessor
stringByAppendingFormat:
stringByAppendingString:
intValue
removeItemAtPath:error:
sortedArrayUsingDescriptors:
stringWithUTF8String:
stringFromDate:
doubleValue
getBytes:length:
sortDescriptorWithKey:ascending:
allKeys
arrayWithObjects:count:
dataWithContentsOfFile:
writeToFile:atomically:
stringByAppendingPathComponent:
UTF8String
containsObject:
bytes
setDateFormat:
stringWithFormat:
countByEnumeratingWithState:objects:count:
defaultManager
enumerateObjectsUsingBlock:
setAttributes:ofItemAtPath:error:
setObject:forKey:
fileExistsAtPath:
numberWithUnsignedInt:
contentsOfDirectoryAtPath:error:
copyPathForPersonalizedData:error:
date
description
dictionaryWithContentsOfFile:
dictionaryWithObjects:forKeys:count:
initWithContentsOfFile:
isEqualToString:
copyPathForPersistentData:error:
```
