# `/usr/sbin/dietappleh13camerad`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 2,716,720 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 32 (Size: 3488)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, PIE
```

## Linked libraries (15)

- `/System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer (compatibility version 1.0.0, current version 326.31.9)`
- `/usr/lib/libIOAccessoryManager.dylib (compatibility version 1.0.0, current version 1.0.0)`
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
		<string>AppleH13CamInUserClient</string>
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
		<string>ApplePhotonDetectorUserClient</string>
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

## Strings (532)

```
Received XPC_ERROR_CONNECTION_INTERRUPTED error from client (pid %{private}d)
H13ISPDEVICE:: LoadSetFile returned 0x%08x - ignoring error\n
Failed to load Bin-format firmware binary: 0x%08x\n
%s: Camera powered on...waiting\n
%s: Could not forget firmware, res = %x\n
%s: Error %x loading FW\n
Failed to copy model string from MobileGestalt
%s: type=0x%X, isOverride=%d, size=%u, isEarlyBoot=%d, status=%08x\n
backCameraModuleSerialNumString exists - load FDR CmCl calibration data\n
%s: failed to load firmware ret=0x%08x
%s: device already open!
Creating H13ISP services assistant
Destroying H13ISP services assistant
H13ISPDevice::ValidateProjectorToken - ISP_GetCameraStatus error (0x%08x)\n
H13ISPServicesRemote: GetProperty (%d) (sent)
Active client pid %{private}d deviceID %{private}s
New connection: pid %{private}d
%s: received invalid reply
Unable to look up remote connection (pid %{private}d)
Received XPC_ERROR_CONNECTION_INVALID error on connection\n
Received unexpected event: %s
%s : Status = %#08x; FCCl data - %s \n
(Bin) Using ISPCPU firmware override file\n
could not read ISPCPU Firmware file\n
Total number of connections: %lu
Received XPC_ERROR_CONNECTION_INTERRUPTED error on connection\n
H13ISPDEVICE:: This is%s an internal build, and FDR was%s validated\n
Couldn't read back camera module SNUM. Sensor is hosed/disconnected. Skip loading FDR CmPM calibration data\n
%s: %s \n
%s - poweredOn=%d, poweredOff=%d, res=0x%08X\n
H13ISPDevice::%s - Failed to copy kMGQFrontCameraOffsetFromDisplayCenter answer from MobileGestalt! err=%d\n
Using override ISP-ANE AFPP file \n
Received XPC_ERROR_TERMINATION_IMMINENT error from client (pid %{private}d)
%s: received reply
%s: attaching to device at index=%ld
%s: failed to open ISP device
Loaded calibration file from override path: %s
FrontCameraModuleSerialNumString exists - load FDR FCCl calibration data\n
%s No module or Unauthorized swap (fcclStatus = %#x) or No FCCL data (perhaps cuz the device does not support FCCL) [error]: %s \n
Load firmware from %s\n
Sending reply to client: rc %08X (pid %{private}d)
Received unknown event from client (pid %{private}d)
%s : Load override cal data: File = %s, Size = %ld (== %ld ?); Status = %08x (cmclStatus = 0x%08x)\n
%s: IONotificationPortGetRunLoopSource returned NULL 
Removing client: kernel
Unexpected client message=%d (pid %{private}d)
%s: camera powered on... waiting
BackCameraSNUM exists - load FDR CmPM calibration data\n
Received XPC_ERROR_TERMINATION_IMMINENT, cleaning up assistant\n
MachService error event received: %s
%{private}s client is entitled=%s
Error opening ISP-ANE networks file. \n
%s: type=0x%X, isOverride=%d, file=%s, size=%u, isEarlyBoot=%d, status=%08x\n
Couldn't read back camera module serial number. Sensor is hosed/disconnected. Skip loading FDR CmCl calibration data\n
%s: IONotificationPortCreate returned NULL 
%s: failed to create ISP device controller
%s: failed to create SIGTERM dispatch source
H13ISPDevice::%s - ret=%#x\n
%s: daemon services not initialized
Client disconnecting (pid %{private}d)
%s: received error reply: %s
H13ISPServicesAssistant: getProperty %d complete (res=0x%08X)\n
%s: exceeded retry count waiting for camera to power off
H13ISPServicesAssistant: setProperty %d\n
H13ISPServicesAssistant: setProperty %d complete (res=0x%08X)\n
Received SIGTERM - exiting
Loading file for ISP-ANE networks - %s \n
Error sending ISP-ANE networks file to kernel: Size = %ld (== %ld ?); Status = %08x\n
%s : Status = %08x; CmCl data - %s \n
H13ISP: maxChannels=%d, timeStampFrequency=%d\n
H13ISP: Cannot cache bufferPoolInfo[%u][%u], result = 0x%08x
%s: client already has a registered device ID
H13ISPServicesAssistant: getProperty %d\n
Could not send FW Ideal Percent for LSC channel[%u], returned:0x%08x - ignoring error\n
%s : Couldn't read front camera module serial number. Sensor is hosed/disconnected. Skip loading FCCl cal data \n
%s : Load override cal data: File = %s, Size = %ld (== %ld ?); Status = %#08x (fcclStatus = %#08x)\n
Unable to initialize services
Unable to begin server for isp
Sent ISP-ANE networks file to kernel: Size = %ld (== %ld ?); Status = %08x\n
%s: Trying to use %s: Size = %lld (== %lld ?); \n
Unable to create reply dictionary (pid %{private}d)
Received unexpected error from client (pid %{private}d)
H13ISPServicesRemote: GetProperty (%d) (reply=0x%08X)
New connection: kernel
H13ISPDevice::%s - kMGQFrontCameraOffsetFromDisplayCenter Description=%s\n
%s : Using %s from unit info plist
%s No module or Unauthorized swap (cmclStatus = 0x%x) or No CmCL data (perhaps cuz the device does not support CmCL) [error]: %s \n
Removing client: pid %{private}d
%s : %s - length = %ld; status = %08x\n
%s No module or Unauthorized swap (cmpmStatus = 0x%x) or No CmPM data (perhaps cuz the device does not support CmPM) [error]: %s \n
\tCalibration UUID mismatch, removing contents of directory\n
\tFound\n
floodCalibrationCurrent
/usr/local/share/firmware/isp/4920_01XX.dat
/usr/local/share/firmware/isp/7920_02XX.dat
SavageMNS
LSCAverageGreenApple
/usr/local/share/firmware/isp/cam%dclocks.txt
ISP_ColdBootPowerCycle
error sending camera channel %d over-ride NVM bytes to kernel: 0x%08X\n
/var/mobile/Library/ISP/Pearl
Cached UUID: 0x
ISP_PowerOnCamera
com.apple.isp.cameratorch
Sending special debug function to firmware object returned error : 0x%08x\n
/Savage/SavagePatch.DAT
No DAT file for Savage found
H13ISPServicesRemoteRGBIRMetadataColorKey
Pearl calibration\n
Error converting vader compliance value\n
Coulnd't read calibrated power from sysconfig\n
LSCComputeFromNVM.cpp
bypassing sending over-ride NVM bypass from unit-info plist for channel %d (mask bit not set)\n
WDDC
LoadFDRFCClDataFile
not 
dense
com.apple.isp.backcamerapower
FrontCameraModuleSerialNumString
could not read Savage firmware file entirely 
/usr/local/share/firmware/isp/3721_11XX.dat
Loading DAT file for unprovisioned Savage
/usr/local/share/firmware/isp/CmPM-brcl.DAT
/usr/local/share/firmware/isp/h14_isp_fw.bin
/usr/local/share/firmware/isp/7820_01XX.dat
/usr/local/share/firmware/isp/3622_01XX.dat
H13ISPServicesRemoteRGBIRFinalOutputPCEConfigKey
UNKNOWN
/var/mobile/Library/ISP/Pearl/NVM.bin
%s/%s.bin
Unexpected references size (Expected %ld, Got %d)\n
/usr/local/share/firmware/isp/3921_01XX.dat
\taFDR may%s be used (%d, %d)
com.apple.dietappleh13camerad.launch
com.apple.dietappleh13camerad.firmware_loading
Failed to read PCE Calibration (FDR data)\n
H13ISPDevice - Did not find platform-info for platform:%d. Defaulting to 0.\n
kMaxPerModuleX>=numX
 :
Successfully sent camera %d sensor register over-ride values for %d registers\n
com.apple.dietappleh13camerad.destroy
 not
Could not find SEP reference location. Will use ISP references
IR sensor not detected
YonkersMNS
H13ISPServicesRemoteRGBIRMetadataIRKey
sha2-384
\tCrypto hash method is %@. Only %s is supported
rb
\tValidating Calibration UUID
\tFailed to read UUID. Marking as invalid
Special function: name: %s, parameters %llu %llu %llu %llu\n
H13ISPDEVICE:: lsc not run for %x.  pCmdAppleChLSCConfigure = %p\n
H13ISPServicesRemoteRGBIRBufferIRKey
H13ISPServicesRemoteRGBIRPCEConfigKey
H13ISPServicesRemoteFusingDataKey
%s/%@
Found camera clock override information file for camera channel %d\n
Error: SetSensorCustomSettings returned an error: 0x%08X\n
/System/Library/PrivateFrameworks/AppleCVHWA.framework/Firmware/lacc_VIO_ISP_IR.bin
LsAdjustEnableCam%d
\tFailed to initialize Manifest from ticket
Coulnd't read calibrated power from IOReg\n
token was removed
%lld
/private/var/tmp/usr/standalone/firmware/Yonkers/YonkersPatch.DAT
DAT file for unprovisioned Yonkers - %@
No DAT file for Yonkers found
/var/mobile/Library/ISP/Pearl/spotDB.bin
AppleH13CamIn
/usr/local/share/firmware/isp/2820_04XX.dat
/usr/local/share/firmware/isp/8723_01XX.dat
B3
Load Savage DAT File: Size = %ld; SendStatus = %08x, FileStatus = 0x%08X
\tFailed to digest AP ticket
Saving %s\n
Failed to save plist
IOService
System performed boot since %s token creation (boot time: %ld). Token will be removed.
multi-camera-cal-wide
com.apple.isp.cameratorchcoolcurrent
ISP_SetFrontCameraOffsetFromDisplayCenter
Could not find reference plist at %s (errno: %d). Will use ISP references
Reading rosaline serial number from sysconfig\n
com.apple.isp.backcamerasensorconfig
Load data file: channel: %d, type: 0x%08x, isEarlyBootDataFile: %s, status: %08x\n
LsAdjustInvertCam%d
/usr/local/share/firmware/isp/7921_01XX.dat
/usr/local/share/firmware/isp/2922_02XX.dat
/var/mobile/Library/ISP
H13ISPDEVICE:: snfRadialGains not enabled for ch %d\n
UnitInfoNVMChannelMask
/usr/local/share/firmware/isp/6221_01XX.dat
/usr/local/share/firmware/isp/7523_01XX.dat
Failed to remove %s token: %@
Successfully set camera %d clock divider over-ride: 0x%08X\n
AP
/usr/local/share/firmware/isp/3722_01XX.dat
/usr/local/share/firmware/isp/4722_01XX.dat
/usr/local/share/firmware/isp/7622_01XX.dat
H13ISPServicesRemoteTypeKey
\tCouldn't get crypto hash method
\tAP ticket digest doesn't match boot manifest hash
Error: Couldn't send NVM\n
using sensor setfile from file for camera %d: %s\n
H13ISPDEVICE:: lsc adjustment not enabled for %x. lsc enabled = %d\n
SendDataFileToFirmware
/usr/local/share/firmware/isp/isp_fw.bin
\tLooking for FDR data\n
/var/mobile/Library/ISP/Pearl/
Failed to read unique chip ID
CmCl
IOGeneralInterest
/usr/local/share/firmware/isp/2520_01XX.dat
/usr/local/share/firmware/isp/7722_01XX.dat
/usr/local/share/firmware/isp/1921_01XX.dat
no
EnableHawking
kMaxPerModuleY>=numY
FrontCameraOffsetFromDisplayCenter
BA
AppleProxHIDEventDriver
a
FrontCameraCalSwide
H13ISPDEVICE:: LSC Orientation cam%d, flip = %d, invert = %d, useSetfile = %d, flipSetfile = %d, flipPerModule = %d rotateAls2Profile = %d enableGreenAvg = %d interpMode = %d  idealPct = %d\n
FWOBJECTSPECIALFUNC
\tLooking for local override files\n
%s/reference-%s.plist
Error: Couldn't send rosaline configuration\n
Reading rosaline power from FDR\n
com.apple.dietappleh13camerad
yes
Failed to send references to FW\n
Load: 0x%08x\n
w
Error setting FW property: 0x%08x\n
/var/mobile/Library/ISP/CalData/DCNUPixbuf_0
LsBypassVerify
%s token does not match device. Token will be removed.
Failed to update %s token file. Will return false so someone looks at that...
MultiCameraCalSwide
property
DAT
LsEnableGreenAvg
LsIdealPctCam%d
Using override YonkersPatchOverride.DAT file 
Unexpected references size after compression (Expected %ld, Got %ld)\n
Failed to open token log file.
/usr/local/share/firmware/isp/CmCl-Override.DAT
/usr/local/share/firmware/isp/6222_01XX.dat
/usr/local/share/firmware/isp/2123_02XX.dat
/usr/local/share/firmware/isp/cam%dsetfile.dat
H13ISPDEVICE:: snfRadialGains command not in setfile for ch %d\n
H13ISPServicesRemoteCFTypeNameKey
com.apple.dietappleh13camerad.photometerManagerSyncQueue
\tLooking for local cache\n
sparse
Reading rosaline power from sysconfig\n
multi-camera-cal-swide
Couldn't read vader compliance\n
\tCouldn't find AP ticket file at path %@
\tIgnoring unexpected cached version (%d != %d)\n
, calibration: 0x
sparseLP
%@ %s\n
ChannelArray
com.apple.isp.backtelecamerapower
\tCan't create %s! (%d)\n
reference
Failed to fetch handle for %s with return code = 0x%08x\n
/var/mobile/Library/ISP/CalData/DCNUMetadata_0
fdrLogMessages
could not read Yonkers key provisioning file entirely 
/usr/local/share/firmware/isp/3820_01XX.dat
IOServiceMatched
com.apple.isp.frontcamerapower
\tCouldn't get boot manifest hash
Couldn't create reference file %s to write\n
Failed to send PCE calibration to FW\n
%s token doesn't match platform. Token will be removed.
Failed to create log message string with code: %d (0x%X)
H13ISPDEVICE:: LoadSetFile returned 0x%08x\n
:
Failed to send rosaline data file: 0x%08X\n
/usr/local/share/firmware/isp/CmPM-dcnu.DAT
error loading ISPCPU firmware 
RadialGainEnable
Error parsing camera clock override file
/usr/local/share/firmware/isp/4721_01XX.dat
pDevice is NULL
/private/var/tmp/usr/standalone/firmware/Savage/SavagePatch.DAT
Expected file %s to be of size %ld. Actual size: %d\n
Found no IR sensor\n
Error reading file\n
com.apple.isp.cameratorchwarmcurrent
/usr/local/share/firmware/isp/3721_01XX.dat
/usr/local/share/firmware/isp/1922_02XX.dat
DAT file for provisioned Savage - %@
Creating local cache\n
floodComplianceRevision
Set sensor reg 0x%08x to val 0x%08X\n
/usr/local/share/firmware/isp/Yonkers/YonkersPatchOverride.DAT
DEV
LsInterpMode
/usr/local/share/firmware/isp/3820_11XX.dat
Ngsk
H13ISPServicesRemoteDeviceID
deviceFirmwareLoad
\t%@
SavageSNUM
pLSCConfig->channelGR.gridCountY == pLSCConfig->channelGB.gridCountY
com.apple.isp.backsuperwidesensorconfig
/usr/local/share/firmware/isp/h13_isp_fw.bin
could not read sensor SetFile
%lf
-sparseLP
sensor-type
com.apple.isp.frontirsensorpower
/Yonkers/YonkersPatch.DAT
denseLP
r
BackCameraSNUM
/usr/local/share/firmware/isp/2921_02XX.dat
SavageDeviceRev
YonkersFabRevision
Load Yonkers DAT File: Size = %ld; SendStatus = %08x, 0x%08X
<null>
/var/mobile/Library/ISP/Pearl/PCECalib.bin
Could not open input file: %s\n
Number of allowed activations has reached zero. %s token will be removed.
UniqueChipID
brcl
Found Yonkers override DAT file, which takes precedence over all others - %@
com.apple.private.applecamerad.client
/
Reading rosaline power from IOReg\n
Error converting calibrated power value\n
=
Using override SavagePatchOverride.DAT file 
/usr/local/share/firmware/isp/4820_01XX.dat
product
Using last allowed activation. %s token will be removed.
n't
com.apple.isp.frontcamerasensorconfig
/usr/local/share/firmware/isp/1822_02XX.dat
Secure RGB sensor not detected
/var/mobile/Documents/Pearl
Image4CryptoHashMethod
yyyy-MM-dd HH:mm:ss
/var/mobile/Documents/Tokens.log
SWDC
/usr/local/share/firmware/isp/9723_01XX.dat
Dev
BootManifestHash
Couldn't read unified Pearl FDR: %@
LoadPDEFiles: No Savage found. Never mind
Trying to use SavagePatchOverride.DAT file - 
DAT file for unprovisioned Savage - %@
Trying to load reference file %s (type: %d, index: %d, temperature: %lf)\n
/var/mobile/Documents/Pearl/ProjectorValid.bin
NVM
Trying to use override YonkersPatchOverride.DAT file 
com.apple.dietappleh13camerad.writer
xpcClientEventHandler
Can't activate %s projector: no projector token found
pLSCConfig->channelGR.gridCountX == pLSCConfig->channelGB.gridCountX
MultiCameraCalWide
sendMessageSync
H13ISPServicesRemoteCFTypeDataKey
com.apple.dietappleh13camerad.assistant_active
\tDidn't find calibration\n
BackCameraModuleSerialNumString
true
/usr/local/share/firmware/isp/1820_01XX.dat
basic_string
rosaline-calibration-current
Failed to read unique chip identifier
/usr/local/share/firmware/isp/ispane.afpp
\tCouldn't validate directories\n
FormatDR
Failed to load PDE files\n
CopyFileToBuffer
No ALS2 profile found in Setfile.
/usr/local/share/firmware/isp/4820_02XX.dat
com.apple.h13ispdevicecontroller.notifications.queue
Unable to find prox service
LoadPDEFiles: isOverridden %d
Pearl
/System/Library/Isp/afpp/
FCDC
/usr/local/share/firmware/isp/4920_02XX.dat
/usr/local/share/firmware/isp/9721_01XX.dat
0
H13ISPServicesRemoteReturnKey
H13ISPServicesRemoteRGBIRBufferDepthKey
CmPM
LoadFDRDataFileCMPM
/usr/local/share/firmware/isp/2820_03XX.dat
/usr/local/share/firmware/isp/2022_01XX.dat
H13ISPServicesThread
Personalized firmware root path accessor not found
rosaline-serial-num
Error converting calibrated power value:  could not fit 32-bit value into 16-bit destination \n
/ispane.afpp
CopyAllowUnsealed
Load ISPANEAFPP file: status: %08x\n
Failure loading override ISPUnitInfo property list : CFPropertyListCreateWithStream failed 
DAT file for provisioned Yonkers - %@
v16@?0^v8
Pearl FDR is %sunified, ToF FDR is %sunified
Couldn't read from FDR: %@
com.apple.isp.backsuperwidecamerapower
clockdiv
dcnu
Error: too many camera sensor register over-rides in file
/usr/local/share/firmware/isp/7820_02XX.dat
wb
Sending reference file %s, type: %d\n
Setting FW property 0x%08x to 0x%08X\n
IOReturn H13ISP::H13ISPDeviceController::SetupDeviceController()
Found Savage override DAT file, which takes precedence over all others - %@
Yonkers/YonkersPatch%s%s.DAT
Found reference plist at %s. Will use SEP references
SendSysConfigCalibrationDataByKey
Ymgt
H13ISPServicesRemoteRGBIRReportKey
Testing if aFDR may be used
%s token timeout was reached (current time %ld). Token will be removed.
H13ISPDevice.cpp
/usr/local/share/firmware/isp/
No C string description.
No valid Savage firmware file to send
/usr/local/share/firmware/isp/8720_01XX.dat
v8@?0
\tReading from FDR\n
doubleValue
/usr/local/share/firmware/isp/ISPUnitInfo.plist
 \n
/usr/local/share/firmware/isp/Savage/SavagePatchOverride.DAT
/usr/local/share/firmware/isp/7721_01XX.dat
H13ISPServicesRemoteRGBIRFinalInputPCEConfigKey
References for %s: Decompressing references\n
WritePropertyValue - UpdateChannelConfigCache channel %d error: 0x%08X\n
No valid Yonkers key provisioning file to send
/usr/local/share/firmware/isp/2820_01XX.dat
Savage/SavagePatch%s%s.DAT
H13ISPServicesRemoteDataKey
H13ISPServicesRemoteRGBIRBufferColorKey
com.apple.iokit.matching
calibration
H13ISPDevice: NVM not valid for camera %d sensorId = %x  %d\n
Error: ISP_OverrideSensorClockFrequency returned an error: 0x%08X\n
brgd
/usr/local/share/firmware/isp/3723_01XX.dat
Couldn't read serial number\n
ISP_PowerOnCamera - ISP_GetNumChannels failed with 0x%08x\n
com.apple.isp.backtelecamerasensorconfig
HWModelStr
/usr/local/share/firmware/isp/3820_02XX.dat
Failed to read %s projector token file. Token will be removed.
front-camera-cal-swide
Set clock divider reg to 0x%08X\n
LoadFDRCalDataFile
/usr/local/share/firmware/isp/3820_12XX.dat
connectionPrepare
reference-%s__T_%lf.bin
false
Failed to read boot time. errno %d
%s%s.%s
/usr/local/share/firmware/isp/FCCl-Override.DAT
/usr/local/share/firmware/isp/7920_01XX.dat
/usr/local/share/firmware/isp/2921_01XX.dat
registerDeviceIDForClient
com.apple.coremedia
Sending rosaline configuration: SN: %s; Power: %d\n
%s token has exceeded max allowed timeout. Token will be removed.
Prod
Loading DAT file for unprovisioned Yonkers
Failed to send Romeo data file: 0x%08X\n
Parsing ISPUnitInfo.plist \n
/usr/local/share/firmware/isp/CmPM-brgd.DAT
/usr/local/share/firmware/isp/5221_02XX.dat
deviceOpen
\taFDR may be used
isp
v32@?0@\"NSNumber\"8Q16^B24
%s token activation count updated to %d
FCCl
/usr/local/share/firmware/isp/2820_02XX.dat
/usr/local/share/firmware/isp/9720_01XX.dat
%02X
sending camera channel %d over-ride NVM bytes to kernel (%d bytes)\n
/usr/local/share/firmware/isp/9251_02XX.dat
UTF8String
setDateFormat:
sharedDataAccessor
sortDescriptorWithKey:ascending:
stringByAppendingFormat:
getBytes:length:
isEqualToString:
objectForKey:
stringWithFormat:
contentsOfDirectoryAtPath:error:
bytes
initWithContentsOfFile:
writeToFile:atomically:
allKeys
containsObject:
description
dictionaryWithContentsOfFile:
doubleValue
length
removeItemAtPath:error:
stringByAppendingString:
copyPathForPersistentData:error:
copyPathForPersonalizedData:error:
defaultManager
setAttributes:ofItemAtPath:error:
stringWithUTF8String:
stringByAppendingPathComponent:
stringFromDate:
date
intValue
sortedArrayUsingDescriptors:
countByEnumeratingWithState:objects:count:
enumerateObjectsUsingBlock:
fileExistsAtPath:
numberWithUnsignedInt:
arrayWithObjects:count:
dataWithContentsOfFile:
dictionaryWithObjects:forKeys:count:
setObject:forKey:
```
