# `/usr/sbin/dietappleh13camerad`

From the upgrade restore ramdisk (141-29011-104.dmg). 2,716,720 bytes.

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
Received XPC_ERROR_TERMINATION_IMMINENT, cleaning up assistant\n
%s: failed to load firmware ret=0x%08x
%s: device already open!
H13ISPDevice::%s - kMGQFrontCameraOffsetFromDisplayCenter Description=%s\n
%s No module or Unauthorized swap (cmclStatus = 0x%x) or No CmCL data (perhaps cuz the device does not support CmCL) [error]: %s \n
Active client pid %{private}d deviceID %{private}s
New connection: pid %{private}d
Unable to look up remote connection (pid %{private}d)
%s: exceeded retry count waiting for camera to power off
%s: attaching to device at index=%ld
MachService error event received: %s
Could not send FW Ideal Percent for LSC channel[%u], returned:0x%08x - ignoring error\n
Failed to copy model string from MobileGestalt
Unable to create reply dictionary (pid %{private}d)
Client disconnecting (pid %{private}d)
%s - poweredOn=%d, poweredOff=%d, res=0x%08X\n
Error sending ISP-ANE networks file to kernel: Size = %ld (== %ld ?); Status = %08x\n
Couldn't read back camera module SNUM. Sensor is hosed/disconnected. Skip loading FDR CmPM calibration data\n
%s No module or Unauthorized swap (fcclStatus = %#x) or No FCCL data (perhaps cuz the device does not support FCCL) [error]: %s \n
Received unknown event from client (pid %{private}d)
%s: failed to create SIGTERM dispatch source
Creating H13ISP services assistant
Destroying H13ISP services assistant
Loaded calibration file from override path: %s
%s : Load override cal data: File = %s, Size = %ld (== %ld ?); Status = %#08x (fcclStatus = %#08x)\n
H13ISP: maxChannels=%d, timeStampFrequency=%d\n
H13ISPServicesAssistant: getProperty %d complete (res=0x%08X)\n
Received SIGTERM - exiting
Sent ISP-ANE networks file to kernel: Size = %ld (== %ld ?); Status = %08x\n
FrontCameraModuleSerialNumString exists - load FDR FCCl calibration data\n
New connection: kernel
Removing client: pid %{private}d
Received XPC_ERROR_CONNECTION_INTERRUPTED error on connection\n
%{private}s client is entitled=%s
%s: Camera powered on...waiting\n
Loading file for ISP-ANE networks - %s \n
%s : %s - length = %ld; status = %08x\n
%s: type=0x%X, isOverride=%d, size=%u, isEarlyBoot=%d, status=%08x\n
Removing client: kernel
H13ISPServicesAssistant: setProperty %d complete (res=0x%08X)\n
%s: daemon services not initialized
Received XPC_ERROR_CONNECTION_INVALID error on connection\n
backCameraModuleSerialNumString exists - load FDR CmCl calibration data\n
H13ISPServicesAssistant: getProperty %d\n
%s: camera powered on... waiting
%s : Using %s from unit info plist
BackCameraSNUM exists - load FDR CmPM calibration data\n
H13ISP: Cannot cache bufferPoolInfo[%u][%u], result = 0x%08x
H13ISPDevice::%s - ret=%#x\n
%s : Status = %#08x; FCCl data - %s \n
could not read ISPCPU Firmware file\n
%s: IONotificationPortGetRunLoopSource returned NULL 
Received XPC_ERROR_CONNECTION_INTERRUPTED error from client (pid %{private}d)
Received unexpected error from client (pid %{private}d)
%s No module or Unauthorized swap (cmpmStatus = 0x%x) or No CmPM data (perhaps cuz the device does not support CmPM) [error]: %s \n
%s : Couldn't read front camera module serial number. Sensor is hosed/disconnected. Skip loading FCCl cal data \n
%s: %s \n
%s: received error reply: %s
H13ISPServicesRemote: GetProperty (%d) (sent)
H13ISPServicesRemote: GetProperty (%d) (reply=0x%08X)
%s: failed to open ISP device
%s: received invalid reply
%s: client already has a registered device ID
H13ISPServicesAssistant: setProperty %d\n
Unexpected client message=%d (pid %{private}d)
H13ISPDEVICE:: This is%s an internal build, and FDR was%s validated\n
%s: Trying to use %s: Size = %lld (== %lld ?); \n
Load firmware from %s\n
(Bin) Using ISPCPU firmware override file\n
Total number of connections: %lu
Sending reply to client: rc %08X (pid %{private}d)
H13ISPDevice::ValidateProjectorToken - ISP_GetCameraStatus error (0x%08x)\n
%s: Error %x loading FW\n
H13ISPDevice::%s - Failed to copy kMGQFrontCameraOffsetFromDisplayCenter answer from MobileGestalt! err=%d\n
Failed to load Bin-format firmware binary: 0x%08x\n
Unable to initialize services
Couldn't read back camera module serial number. Sensor is hosed/disconnected. Skip loading FDR CmCl calibration data\n
%s : Load override cal data: File = %s, Size = %ld (== %ld ?); Status = %08x (cmclStatus = 0x%08x)\n
Received unexpected event: %s
%s: failed to create ISP device controller
%s: Could not forget firmware, res = %x\n
Error opening ISP-ANE networks file. \n
%s : Status = %08x; CmCl data - %s \n
Unable to begin server for isp
H13ISPDEVICE:: LoadSetFile returned 0x%08x - ignoring error\n
Using override ISP-ANE AFPP file \n
%s: type=0x%X, isOverride=%d, file=%s, size=%u, isEarlyBoot=%d, status=%08x\n
%s: IONotificationPortCreate returned NULL 
%s: received reply
Received XPC_ERROR_TERMINATION_IMMINENT error from client (pid %{private}d)
Couldn't read serial number\n
Setting FW property 0x%08x to 0x%08X\n
/usr/local/share/firmware/isp/CmPM-brgd.DAT
/usr/local/share/firmware/isp/CmPM-brcl.DAT
\taFDR may%s be used (%d, %d)
/var/mobile/Library/ISP/Pearl/PCECalib.bin
Couldn't read from FDR: %@
kMaxPerModuleX>=numX
H13ISPDEVICE:: snfRadialGains not enabled for ch %d\n
com.apple.isp.backcamerasensorconfig
com.apple.coremedia
\tFailed to initialize Manifest from ticket
References for %s: Decompressing references\n
/usr/local/share/firmware/isp/3722_01XX.dat
Ngsk
deviceOpen
com.apple.dietappleh13camerad.firmware_loading
yes
\tCouldn't validate directories\n
Error converting calibrated power value:  could not fit 32-bit value into 16-bit destination \n
w
/usr/local/share/firmware/isp/3723_01XX.dat
com.apple.dietappleh13camerad.destroy
-sparseLP
ISP_PowerOnCamera - ISP_GetNumChannels failed with 0x%08x\n
WDDC
brcl
/usr/local/share/firmware/isp/3721_01XX.dat
/usr/local/share/firmware/isp/7721_01XX.dat
com.apple.dietappleh13camerad.photometerManagerSyncQueue
/var/mobile/Documents/Pearl
%02X
Sending reference file %s, type: %d\n
MultiCameraCalWide
:
/usr/local/share/firmware/isp/FCCl-Override.DAT
/usr/local/share/firmware/isp/1922_02XX.dat
EnableHawking
\tDidn't find calibration\n
dense
Failed to load PDE files\n
%s token activation count updated to %d
 :
CopyAllowUnsealed
/usr/local/share/firmware/isp/3820_01XX.dat
com.apple.isp.frontcamerasensorconfig
sending camera channel %d over-ride NVM bytes to kernel (%d bytes)\n
/usr/local/share/firmware/isp/Yonkers/YonkersPatchOverride.DAT
RadialGainEnable
No valid Yonkers key provisioning file to send
/usr/local/share/firmware/isp/2022_01XX.dat
Dev
No DAT file for Yonkers found
Found reference plist at %s. Will use SEP references
yyyy-MM-dd HH:mm:ss
LSCComputeFromNVM.cpp
H13ISPDevice - Did not find platform-info for platform:%d. Defaulting to 0.\n
/ispane.afpp
CopyFileToBuffer
/usr/local/share/firmware/isp/4820_02XX.dat
IOReturn H13ISP::H13ISPDeviceController::SetupDeviceController()
reference-%s__T_%lf.bin
Found Savage override DAT file, which takes precedence over all others - %@
Loading DAT file for unprovisioned Yonkers
Expected file %s to be of size %ld. Actual size: %d\n
Unable to find prox service
Failed to create log message string with code: %d (0x%X)
Failed to send rosaline data file: 0x%08X\n
Failed to read %s projector token file. Token will be removed.
System performed boot since %s token creation (boot time: %ld). Token will be removed.
H13ISPDEVICE:: lsc adjustment not enabled for %x. lsc enabled = %d\n
HWModelStr
/usr/local/share/firmware/isp/2921_01XX.dat
B3
/Yonkers/YonkersPatch.DAT
connectionPrepare
BootManifestHash
\tCan't create %s! (%d)\n
v32@?0@\"NSNumber\"8Q16^B24
%s token timeout was reached (current time %ld). Token will be removed.
/var/mobile/Documents/Pearl/ProjectorValid.bin
using sensor setfile from file for camera %d: %s\n
/System/Library/PrivateFrameworks/AppleCVHWA.framework/Firmware/lacc_VIO_ISP_IR.bin
Found no IR sensor\n
pLSCConfig->channelGR.gridCountX == pLSCConfig->channelGB.gridCountX
pLSCConfig->channelGR.gridCountY == pLSCConfig->channelGB.gridCountY
multi-camera-cal-wide
Special function: name: %s, parameters %llu %llu %llu %llu\n
/usr/local/share/firmware/isp/CmCl-Override.DAT
No C string description.
CmPM
\tFailed to read UUID. Marking as invalid
Couldn't create reference file %s to write\n
Could not open input file: %s\n
Failed to read unique chip identifier
/usr/local/share/firmware/isp/Savage/SavagePatchOverride.DAT
SendSysConfigCalibrationDataByKey
/usr/local/share/firmware/isp/CmPM-dcnu.DAT
LsAdjustInvertCam%d
H13ISPServicesRemoteRGBIRFinalInputPCEConfigKey
H13ISPDEVICE:: lsc not run for %x.  pCmdAppleChLSCConfigure = %p\n
=
FCCl
/usr/local/share/firmware/isp/4820_01XX.dat
/usr/local/share/firmware/isp/3820_11XX.dat
/usr/local/share/firmware/isp/2520_01XX.dat
Error converting vader compliance value\n
ChannelArray
/usr/local/share/firmware/isp/7820_02XX.dat
/usr/local/share/firmware/isp/4722_01XX.dat
Saving %s\n
%s token does not match device. Token will be removed.
H13ISPServicesRemoteTypeKey
Cached UUID: 0x
Set clock divider reg to 0x%08X\n
DAT
/usr/local/share/firmware/isp/isp_fw.bin
com.apple.dietappleh13camerad
Couldn't read unified Pearl FDR: %@
FrontCameraModuleSerialNumString
/usr/local/share/firmware/isp/6221_01XX.dat
SavageDeviceRev
not 
/usr/local/share/firmware/isp/9723_01XX.dat
/usr/local/share/firmware/isp/8720_01XX.dat
BA
YonkersFabRevision
H13ISPServicesRemoteRGBIRReportKey
H13ISPServicesRemoteCFTypeNameKey
Error: Couldn't send NVM\n
Failed to read PCE Calibration (FDR data)\n
Number of allowed activations has reached zero. %s token will be removed.
/var/mobile/Documents/Tokens.log
H13ISPDevice: NVM not valid for camera %d sensorId = %x  %d\n
com.apple.isp.frontirsensorpower
H13ISPServicesRemoteCFTypeDataKey
no
rb
\tFound\n
reference
H13ISPDEVICE:: LSC Orientation cam%d, flip = %d, invert = %d, useSetfile = %d, flipSetfile = %d, flipPerModule = %d rotateAls2Profile = %d enableGreenAvg = %d interpMode = %d  idealPct = %d\n
/var/mobile/Library/ISP/CalData/DCNUMetadata_0
LsBypassVerify
H13ISPServicesRemoteRGBIRBufferDepthKey
token was removed
com.apple.isp.cameratorch
brgd
Using override YonkersPatchOverride.DAT file 
/usr/local/share/firmware/isp/2820_04XX.dat
/usr/local/share/firmware/isp/4920_02XX.dat
/usr/local/share/firmware/isp/7523_01XX.dat
\tLooking for local cache\n
Error reading file\n
Failed to open token log file.
LSCAverageGreenApple
Using override SavagePatchOverride.DAT file 
/usr/local/share/firmware/isp/2820_01XX.dat
/usr/local/share/firmware/isp/3820_12XX.dat
/usr/local/share/firmware/isp/7622_01XX.dat
\t%@
error loading ISPCPU firmware 
Failure loading override ISPUnitInfo property list : CFPropertyListCreateWithStream failed 
/usr/local/share/firmware/isp/1822_02XX.dat
IOServiceMatched
\tLooking for local override files\n
Creating local cache\n
SavageSNUM
floodCalibrationCurrent
com.apple.isp.cameratorchcoolcurrent
/usr/local/share/firmware/isp/ispane.afpp
UnitInfoNVMChannelMask
No ALS2 profile found in Setfile.
H13ISPServicesRemoteRGBIRMetadataIRKey
com.apple.dietappleh13camerad.writer
Pearl calibration\n
Reading rosaline power from FDR\n
fdrLogMessages
Error: too many camera sensor register over-rides in file
/usr/local/share/firmware/isp/6222_01XX.dat
0
H13ISPServicesRemoteReturnKey
/var/mobile/Library/ISP/Pearl/spotDB.bin
rosaline-calibration-current
front-camera-cal-swide
sensor-type
property
Successfully set camera %d clock divider over-ride: 0x%08X\n
/usr/local/share/firmware/isp/1921_01XX.dat
/var/mobile/Library/ISP
Failed to send references to FW\n
/usr/local/share/firmware/isp/ISPUnitInfo.plist
ISP_ColdBootPowerCycle
%s%s.%s
SavageMNS
IR sensor not detected
Savage/SavagePatch%s%s.DAT
\tFailed to digest AP ticket
\tAP ticket digest doesn't match boot manifest hash
denseLP
Unexpected references size (Expected %ld, Got %d)\n
NVM
kMaxPerModuleY>=numY
error sending camera channel %d over-ride NVM bytes to kernel: 0x%08X\n
/var/mobile/Library/ISP/CalData/DCNUPixbuf_0
/var/mobile/Library/ISP/Pearl
Failed to read unique chip ID
Failed to update %s token file. Will return false so someone looks at that...
com.apple.isp.cameratorchwarmcurrent
/usr/local/share/firmware/isp/3820_02XX.dat
/usr/local/share/firmware/isp/5221_02XX.dat
Load Savage DAT File: Size = %ld; SendStatus = %08x, FileStatus = 0x%08X
Yonkers/YonkersPatch%s%s.DAT
v16@?0^v8
 not
Reading rosaline power from IOReg\n
FrontCameraCalSwide
/usr/local/share/firmware/isp/2921_02XX.dat
Loading DAT file for unprovisioned Savage
DAT file for provisioned Yonkers - %@
%s/%@
Couldn't read vader compliance\n
LoadPDEFiles: No Savage found. Never mind
r
/usr/local/share/firmware/isp/
BackCameraSNUM
/usr/local/share/firmware/isp/7920_02XX.dat
Ymgt
\tCouldn't get boot manifest hash
\tIgnoring unexpected cached version (%d != %d)\n
sparseLP
%s/reference-%s.plist
%lld
Error setting FW property: 0x%08x\n
ISP_SetFrontCameraOffsetFromDisplayCenter
\tValidating Calibration UUID
Failed to read boot time. errno %d
multi-camera-cal-swide
/usr/local/share/firmware/isp/4721_01XX.dat
Load Yonkers DAT File: Size = %ld; SendStatus = %08x, 0x%08X
Could not find reference plist at %s (errno: %d). Will use ISP references
%s/%s.bin
WritePropertyValue - UpdateChannelConfigCache channel %d error: 0x%08X\n
/usr/local/share/firmware/isp/h14_isp_fw.bin
/usr/local/share/firmware/isp/9721_01XX.dat
product
H13ISPDevice.cpp
CmCl
Load ISPANEAFPP file: status: %08x\n
/usr/local/share/firmware/isp/7920_01XX.dat
/private/var/tmp/usr/standalone/firmware/Savage/SavagePatch.DAT
\tLooking for FDR data\n
MultiCameraCalSwide
/usr/local/share/firmware/isp/2123_02XX.dat
YonkersMNS
sendMessageSync
H13ISPServicesRemoteDataKey
com.apple.dietappleh13camerad.launch
Unexpected references size after compression (Expected %ld, Got %ld)\n
false
Sending rosaline configuration: SN: %s; Power: %d\n
Using last allowed activation. %s token will be removed.
LsEnableGreenAvg
H13ISPServicesRemoteRGBIRFinalOutputPCEConfigKey
Reading rosaline serial number from sysconfig\n
Reading rosaline power from sysconfig\n
Trying to load reference file %s (type: %d, index: %d, temperature: %lf)\n
%s token has exceeded max allowed timeout. Token will be removed.
Sending special debug function to firmware object returned error : 0x%08x\n
bypassing sending over-ride NVM bypass from unit-info plist for channel %d (mask bit not set)\n
/System/Library/Isp/afpp/
H13ISPServicesRemoteDeviceID
\taFDR may be used
\tCouldn't get crypto hash method
\tCouldn't find AP ticket file at path %@
Pearl FDR is %sunified, ToF FDR is %sunified
SendDataFileToFirmware
DAT file for unprovisioned Yonkers - %@
v8@?0
Failed to save plist
Failed to remove %s token: %@
Error: ISP_OverrideSensorClockFrequency returned an error: 0x%08X\n
/usr/local/share/firmware/isp/7921_01XX.dat
com.apple.dietappleh13camerad.assistant_active
/usr/local/share/firmware/isp/cam%dclocks.txt
BackCameraModuleSerialNumString
IOGeneralInterest
/usr/local/share/firmware/isp/3921_01XX.dat
pDevice is NULL
/private/var/tmp/usr/standalone/firmware/Yonkers/YonkersPatch.DAT
\tCrypto hash method is %@. Only %s is supported
sparse
calibration
com.apple.h13ispdevicecontroller.notifications.queue
No DAT file for Savage found
/var/mobile/Library/ISP/Pearl/NVM.bin
Failed to send PCE calibration to FW\n
UniqueChipID
clockdiv
 \n
LsIdealPctCam%d
Trying to use override YonkersPatchOverride.DAT file 
/usr/local/share/firmware/isp/9251_02XX.dat
com.apple.private.applecamerad.client
\tCalibration UUID mismatch, removing contents of directory\n
a
FCDC
Error parsing camera clock override file
/usr/local/share/firmware/isp/3622_01XX.dat
H13ISPServicesThread
Personalized firmware root path accessor not found
basic_string
Can't activate %s projector: no projector token found
com.apple.isp.backcamerapower
com.apple.isp.backsuperwidesensorconfig
could not read Yonkers key provisioning file entirely 
Prod
Found Yonkers override DAT file, which takes precedence over all others - %@
Secure RGB sensor not detected
H13ISPServicesRemoteRGBIRBufferColorKey
%lf
%@ %s\n
com.apple.isp.backsuperwidecamerapower
/usr/local/share/firmware/isp/8723_01XX.dat
DAT file for unprovisioned Savage - %@
\tReading from FDR\n
Error converting calibrated power value\n
Parsing ISPUnitInfo.plist \n
/usr/local/share/firmware/isp/cam%dsetfile.dat
LsInterpMode
could not read sensor SetFile
/usr/local/share/firmware/isp/7820_01XX.dat
FormatDR
IOService
/
doubleValue
DAT file for provisioned Savage - %@
<null>
H13ISPServicesRemoteFusingDataKey
/var/mobile/Library/ISP/Pearl/
AppleProxHIDEventDriver
Coulnd't read calibrated power from sysconfig\n
SWDC
Trying to use SavagePatchOverride.DAT file - 
/usr/local/share/firmware/isp/2820_03XX.dat
Testing if aFDR may be used
Pearl
LsAdjustEnableCam%d
dcnu
No valid Savage firmware file to send
/Savage/SavagePatch.DAT
AppleH13CamIn
Load: 0x%08x\n
Failed to fetch handle for %s with return code = 0x%08x\n
com.apple.isp.frontcamerapower
/usr/local/share/firmware/isp/h13_isp_fw.bin
could not read Savage firmware file entirely 
/usr/local/share/firmware/isp/9720_01XX.dat
/usr/local/share/firmware/isp/7722_01XX.dat
xpcClientEventHandler
deviceFirmwareLoad
sha2-384
Coulnd't read calibrated power from IOReg\n
n't
H13ISPDEVICE:: LoadSetFile returned 0x%08x\n
com.apple.isp.backtelecamerasensorconfig
Error: SetSensorCustomSettings returned an error: 0x%08X\n
UNKNOWN
Image4CryptoHashMethod
wb
Failed to send Romeo data file: 0x%08X\n
DEV
LoadFDRCalDataFile
/usr/local/share/firmware/isp/2820_02XX.dat
/usr/local/share/firmware/isp/2922_02XX.dat
H13ISPServicesRemoteRGBIRPCEConfigKey
registerDeviceIDForClient
com.apple.iokit.matching
isp
com.apple.isp.backtelecamerapower
Found camera clock override information file for camera channel %d\n
/usr/local/share/firmware/isp/4920_01XX.dat
/usr/local/share/firmware/isp/1820_01XX.dat
H13ISPServicesRemoteRGBIRBufferIRKey
rosaline-serial-num
floodComplianceRevision
Could not find SEP reference location. Will use ISP references
/usr/local/share/firmware/isp/3721_11XX.dat
H13ISPServicesRemoteRGBIRMetadataColorKey
Error: Couldn't send rosaline configuration\n
ISP_PowerOnCamera
H13ISPDEVICE:: snfRadialGains command not in setfile for ch %d\n
Successfully sent camera %d sensor register over-ride values for %d registers\n
FrontCameraOffsetFromDisplayCenter
Load data file: channel: %d, type: 0x%08x, isEarlyBootDataFile: %s, status: %08x\n
%s token doesn't match platform. Token will be removed.
FWOBJECTSPECIALFUNC
Set sensor reg 0x%08x to val 0x%08X\n
LoadFDRDataFileCMPM
, calibration: 0x
LoadPDEFiles: isOverridden %d
AP
LoadFDRFCClDataFile
true
copyPathForPersonalizedData:error:
allKeys
stringByAppendingPathComponent:
length
sharedDataAccessor
defaultManager
fileExistsAtPath:
isEqualToString:
objectForKey:
setDateFormat:
arrayWithObjects:count:
UTF8String
containsObject:
description
intValue
writeToFile:atomically:
countByEnumeratingWithState:objects:count:
date
dictionaryWithContentsOfFile:
initWithContentsOfFile:
numberWithUnsignedInt:
setObject:forKey:
sortDescriptorWithKey:ascending:
bytes
doubleValue
setAttributes:ofItemAtPath:error:
dictionaryWithObjects:forKeys:count:
enumerateObjectsUsingBlock:
getBytes:length:
removeItemAtPath:error:
sortedArrayUsingDescriptors:
stringByAppendingFormat:
stringWithUTF8String:
contentsOfDirectoryAtPath:error:
stringFromDate:
stringWithFormat:
copyPathForPersistentData:error:
dataWithContentsOfFile:
stringByAppendingString:
```
