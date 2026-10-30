# `/usr/sbin/dietappleh16camerad`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 3,973,472 bytes.

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
%s - Load override cal data: File = %s, Size = %ld (== %ld ?); Status = %#08x (fcclStatus = %#08x)\n
Unexpected client Get data length=%zu expected=%zu (pid %{private}d)\n
Rejecting XPC peer missing %{public}s (pid %{private}d)\n
%s - Assistant Version %s\n
%s - [error]: %s\n
Error opening ISP-ANE networks file\n
(Bin) Using ISPCPU firmware override file\n
%s - Error getting channel info - chan: %d, res: 0x%08X\n
%s - powering on camera\n
could not read sensor SetFile\n
%s - Did not find platform-info for platform:%d. Defaulting to 0\n
%s - FTC gain buffer allocation failed\n
%s - No module or Unauthorized swap (fcclStatus = %#x) or No FCCL data (perhaps cuz the device does not support FCCL) [error]: %s\n
Received unexpected error from client (pid %{private}d)\n
No ALS2 profile found in Setfile\n
%s - snfRadialGains not enabled for ch %d\n
%s - LoadSetFile returned 0x%08x\n
%s - Status = %#08x; CmCl data - %s\n
Load data file: channel: %d, type: %d, isEarlyBootDataFile: %s, status: %08x\n\n
Removing client: kernel\n
Failure loading override ISPUnitInfo property list : CFPropertyListCreateWithStream failed\n
Setting FW property 0x%08x to 0x%08X\n
Error: SetSensorCustomSettings returned an error: 0x%08X\n
sending camera channel %d over-ride NVM bytes to kernel (%d bytesn\n
Error sending ISP-ANE networks file to kernel: Size = %ld (== %ld ?); Status = %08x\n\n
Trying to use SavagePatchOverride.DAT file\n
backTeleCameraModuleSerialNumString exists - load OCCl calibration data\n\n
No module or No CmPM data (perhaps cuz the device does not support CmPM). Skip loading FDR CmPM calibration data\n
could not read ISPCPU Firmware file\n
Could not set CIL Brightness to %u\n\n
Unable to create reply dictionary (pid %{private}d)\n
Client disconnecting (pid %{private}d)\n
Received XPC_ERROR_CONNECTION_INVALID error on connection\n\n
Load firmware from %s\n\n
Unable to look up remote connection (pid %{private}d)\n
could not read Savage firmware file entirely\n
%s: Savage Auth failed, status = 0x%x\n
%s OCCl is not a dict (FDR2.0?), Unauthorized swap or No OCCl data (perhaps cuz the device does not support OCCl) [error]: %s \n
New connection: kernel\n
%s - %d\n
%s - %d complete (res=0x%08X)\n\n
%s - IONotificationPortCreate returned NULL\n
%s: Could not power off the ISP, res = 0x%x\n
Unexpected client message=%d (pid %{private}d)\n
%s - received error reply: %s\n
%s - Load override cal data: File = %s, Size = %ld (== %ld ?); Status = %08x (cmclStatus = 0x%08x)\n
%s - cache is already invalid - exiting\n
No valid Savage firmware file to send\n
FrontCameraModuleSerialNumString exists - load FDR FCCl calibration data\n\n
LSC Orientation cam%d, flip = %d, invert = %d, useSetfile = %d, flipSetfile = %d, flipPerModule = %d rotateAls2Profile = %d enableGreenAvg = %d interpMode = %d  idealPct = %d\n\n
Successfully sent camera %d sensor register over-ride values for %d registers\n
Failed to load Bin-format firmware binary: 0x%08x\n
Trying to use override YonkersPatchOverride.DAT file\n
%s - Camera powered on...waiting\n
could not read Yonkers key provisioning file entirely\n
%s: Invalid connection\n
FrontCameraModuleSerialNumString exists - load OCCl calibration data\n\n
%s - snfRadialGains command not in setfile for ch %d\n
LoadSetFile returned 0x%08x - ignoring error\n
Found camera clock override information file for camera channel %d\n
Error: too many camera sensor register over-rides in file\n
%s - Front camera not supported on this device\n
Total number of connections: %lu\n
%s: Savage Pre Auth failed, status = 0x%x\n
%s - Trying to use %s: Size = %lld (== %lld ?);\n
Loaded calibration file from override path: %s\n
%s - type=0x%X, isOverride=%d, file=%s, size=%u, isEarlyBoot=%d, status=%08x\n
%s - failed to get SoC generation from the device tree\n
Received XPC_ERROR_CONNECTION_INTERRUPTED error on connection\n\n
Error creating H16ISPDeviceController object: %08X\n
UpdateChannelConfigCache channel %d error: 0x%08X\n
%s - ret=%#x\n
Failed to copy model string from MobileGestalt\n
%s: Savage Auth failed, res = 0x%x\n
%s - failed to load firmware ret=0x%08x\n
%s - LSCComputeSNFVerticalGains: null ptr! pRadialGainAsymScaleSet.\n
%s - Could not forget firmware, res = %x\n
%s - maxChannels=%d, timeStampFrequency=%d\n
%s - Status = %#08x; FCCl data - %s\n
Unable to begin server for isp\n
This is%s an internal build, and FDR was%s validated\n
Error parsing camera clock override file\n
Using override YonkersPatchOverride.DAT file\n
Using override ISP-ANE AFPP file\n
%s - No module or Unauthorized swap (cmclStatus = 0x%x) or No CmCL data (perhaps cuz the device does not support CmCL) [error]: %s\n
Couldn't read %s. Sensor is hosed/disconnected.\n
%s - poweredOn=%d, poweredOff=%d, res=0x%08X\n
using sensor setfile from file for camera %d: %s\n
Could not send FW Ideal Percent for LSC channel[%u], returned:0x%08x - ignoring error\n
%s - Using %s from unit info plist\n
%s - Success: cached configs - numChannels: %d\n
%s - Error: resetting device config cache - res: 0x%08X\n
New connection: pid %{private}d\n
Received XPC_ERROR_CONNECTION_INTERRUPTED error from client (pid %{private}d)\n
%s - lsc adjustment not enabled for %x. lsc enabled = %d\n
%s - Failed to copy kMGQFrontCameraOffsetFromDisplayCenter answer from MobileGestalt! err=%d\n
%s - Couldn't read back camera module serial number. Sensor is hosed/disconnected. Skip loading FDR CmCl calibration data\n
%s - ISP_GetNumChannels failed with 0x%08x\n
Set clock divider reg to 0x%08X\n
%s: Data file load failed, status = 0x%x\n
%s - type=0x%X, isOverride=%d, size=%u, isEarlyBoot=%d, status=%08x\n
%s - Rear camera not supported on this device\n
Received unknown event from client (pid %{private}d)\n
Received XPC_ERROR_TERMINATION_IMMINENT, cleaning up assistant\n\n
Camera powered on...waiting\n
%s - received invalid reply\n
Unable to initialize services\n
%s - ISP_GetCameraStatus error (0x%08x)\n
%s : Load override %s cal data: Size = %ld (== %ld ?); Status = %08x\n
%s - Initializing device configuration cache\n
Failed to crate SIGTERM dispatch source\n
Destroying H16ISP services assistant\n
No valid Yonkers key provisioning file to send\n
Couldn't read back camera module serial number. Sensor is hosed/disconnected. Skip loading OCCl calibration data\n
Error opening H16ISPDevice: %08X\n
%s - IONotificationPortGetRunLoopSource returned NULL\n
H16ISPServicesRemote: GetProperty (%d) (sent)\n
%s - Parsing ISPUnitInfo.plist\n
error sending camera channel %d over-ride NVM bytes to kernel: 0x%08X\n
Loading file for ISP-ANE networks - %s\n
%s - Error getting LSC polynomial - chan: %d, res: 0x%08X\n
%s - status: %08x\n
%s: Could not reserve channel, res = 0x%x\n
%s - Error getting config - res: 0x%08X\n
Removing client: pid %{private}d\n
%s - Collecting ISP Sysdiagnose State\n
Received SIGTERM - exiting\n
Unable to create mach service\n
Creating H16ISP services assistant\n
Error setting FW property: 0x%08x\n
%s - status: 0x%08X\n
%s - Timed out waiting for the driver to register service, deviceArrived = %d\n
%s - received reply\n
H16ISPServicesRemote: GetProperty (%d) (reply=0x%08X)\n
%s - noHPR boot-arg set\n
Failed to fetch handle for %s with return code = 0x%08x\n
%s: Invalid data file arguments\n
%s - Error %x loading FW\n
%s - ISP command not permitted\n
%s: %d: Sending reply to client: rc %08X (pid %{private}d)\n
Received XPC_ERROR_TERMINATION_IMMINENT error from client (pid %{private}d)\n
Audit: XPC peer missing %{public}s (pid %{private}d) — would reject\n
%s:%s exists, length of the string = %ld.\n\n
camChannel: %d, cmpmInstance: %s\n
%s - No module or Unauthorized swap (cmpmStatus = 0x%x) or No CmPM data (perhaps cuz the device does not support CmPM) [error]: %s\n
%s - caching device configurations\n
%s - no channels detected - exiting\n
%s - %d configurations detected for channel %d\n
%s - Error getting camera config - chan: %d, res: 0x%08X\n
%s - SoC generation from the device tree is invalid!\n
%s - %s\n
%s: Could not release channel, res = 0x%x\n
Received unexpected event: %s\n
bypassing sending over-ride NVM bypass from unit-info plist for channel %d (mask bit not set)\n
%s - Status = %08x; HPR - %s\n
%s - kMGQFrontCameraOffsetFromDisplayCenter Description=%s\n
Sent ISP-ANE networks file to kernel: Size = %ld (== %ld ?); Status = %08x\n
%s - %s - length = %ld; status = %08x\n
%s - Couldn't read front camera module serial number. Sensor is hosed/disconnected. Skip loading FCCl cal data\n
%s - client already has a registered device ID\n
Unexpected client Set data length=%zu expected=%zu (pid %{private}d)\n
%s - NVM not valid for camera %d sensorId = %x  %d\n
Set sensor reg 0x%08x to val 0x%08X\n
%s : Status = %08x; OCCl (%s) data - %s \n
Active client pid %{private}d deviceID %{private}s\n
%s: Could not power on the ISP, res = 0x%x\n
Using override SavagePatchOverride.DAT file\n
backCameraModuleSerialNumString exists - load FDR CmCl calibration data\n\n
date
description
dictionaryWithContentsOfFile:
doubleValue
objectForKey:
stringByAppendingFormat:
UTF8String
removeItemAtPath:error:
stringByAppendingString:
writeToFile:atomically:
contentsOfDirectoryAtPath:error:
copyPathForPersistentData:error:
dataWithContentsOfFile:
length
setDateFormat:
stringWithUTF8String:
countByEnumeratingWithState:objects:count:
intValue
numberWithUnsignedInt:
setAttributes:ofItemAtPath:error:
setObject:forKey:
sortedArrayUsingDescriptors:
allKeys
dictionaryWithObjects:forKeys:count:
enumerateObjectsUsingBlock:
stringByAppendingPathComponent:
containsObject:
copyPathForPersonalizedData:error:
defaultManager
fileExistsAtPath:
getBytes:length:
stringWithFormat:
arrayWithObjects:count:
stringFromDate:
initWithContentsOfFile:
isEqualToString:
sharedDataAccessor
sortDescriptorWithKey:ascending:
bytes
UnitInfoNVMChannelMask
w
SetupDeviceController
/var/mobile/Library/ISP/CalData/DCNUPixbuf_0
LoadFDRDataFileCMPM
LsEnableGreenAvg
fdrLogMessages
com.apple.dietappleh16camerad.photometerManagerSyncQueue
GICComputeFromNVMApple
Failed to read %s projector token file. Token will be removed.
\tLooking for local override files\n
%02X
Unexpected references size (Expected %ld, Got %d)\n
Failed to load PDE files\n
SendSysConfigCalibrationDataByKey
/usr/local/share/firmware/isp/4425_01XX.dat
/usr/local/share/firmware/isp/8825_01XX.dat
SavageUID
IODeviceTree:/arm-io
/usr/local/share/firmware/isp/3524_01XX.dat
a
AppleH16CamIn
Failed to send PCE calibration to FW\n
H16ISPServicesRemoteRGBIRMetadataIRKey
Special function: name: %s, parameters %llu %llu %llu %llu\n
sensor-type
HWModelStr
%lf
/private/var/tmp/usr/standalone/firmware/Yonkers/YonkersPatch.DAT
property
H16ISPServicesRemoteIORegPropertyDataKey
EnforceClientEntitlement
/usr/local/share/firmware/isp/2924_01XX.dat
Failed to read unique chip ID
%s token does not match device. Token will be removed.
H16ISPServicesRemoteRGBIRFinalOutputPCEConfigKey
0
/usr/local/share/firmware/isp/7424_01XX.dat
/usr/local/share/firmware/isp/3623_01XX.dat
Image4CryptoHashMethod
References for %s: Decompressing references\n
multi-camera-cal-wide
clockdiv
/usr/local/share/firmware/isp/CmPM-DPCd
\tCouldn't validate directories\n
Couldn't read serial number\n
H16ISPServicesRemoteCFTypeDataKey
com.apple.dietappleh16camerad.assistant_active
/usr/local/share/firmware/isp/3624_02XX.dat
Error converting vader compliance value\n
com.apple.appleh16camerad
LSC_GET_BASE_U32_PT(chInfo[ch]) % (chInfo[ch]->gridCountX * chInfo[ch]->gridCountY) == 0
sparse
/usr/local/share/firmware/isp/7524_01XX.dat
%s token activation count updated to %d
\tFailed to digest AP ticket
\tFailed to read UUID. Marking as invalid
Loading DAT file for unprovisioned Yonkers
com.apple.isp.backsuperwidecamerapower
FWOBJECTSPECIALFUNC
\tValidating Calibration UUID
Pearl
Reading rosaline power from FDR\n
ValidateProjectorToken
/System/Library/PrivateFrameworks/AppleCVHWA.framework/Firmware/lacc_VIO_ISP_IR.bin
/ispane.afpp
/usr/local/share/firmware/isp/OCCl-cmca.DAT
/var/mobile/Library/ISP/CalData/DCNUMetadata_0
\tCrypto hash method is %@. Only %s is supported
Pearl calibration\n
/var/mobile/Library/ISP/Pearl/
Sending rosaline configuration: SN: %s; Power: %d\n
Personalized firmware root path accessor not found
Couldn't combine frontIR chipIDStr and uidStr
/usr/local/share/firmware/isp/CmPM-CALm
chInfo[ch]->gridCountY == chInfo[0]->gridCountY
/usr/local/share/firmware/isp/0225_01XX.dat
Number of allowed activations has reached zero. %s token will be removed.
Cached UUID: 0x
Error converting calibrated power value\n
Load: 0x%08x\n
daemon
n't
deviceFirmwareLoad
Error: Couldn't send NVM\n
H16ISPServicesRemoteRGBIRPCEConfigKey
CmPM
InitDeviceConfigsCache
com.apple.iokit.matching
LSCComputeSNFVerticalGains
chInfo[ch]->gridCountX == chInfo[0]->gridCountX
\tCouldn't get crypto hash method
Trying to load reference file %s (type: %d, index: %d, temperature: %lf)\n
H16ISPServicesRemoteDeviceID
FrontCameraCalSwide
com.apple.isp.frontirsensorpower
ISP_SavageAuth
/var/mobile/Documents/Pearl/ProjectorValid.bin
Failed to open token log file.
\tAP ticket digest doesn't match boot manifest hash
v8@?0
Loading DAT file for unprovisioned Savage
FCDC
BackTeleCameraSNUM
/usr/local/share/firmware/isp/CmPM-brcl
\tCouldn't find AP ticket file at path %@
floodCalibrationCurrent
Could not read calibrated power from sysconfig\n
com.apple.isp.backcamerasensorconfig
 :
com.apple.dietappleh16camerad.firmware_loading
WDDC
/usr/local/share/firmware/isp/isp_fw.bin
unavailable
H16ISPServicesRemoteRGBIRMetadataColorKey
CopyAllowUnsealed
LSC_GET_BASE_U32_PT(chInfo1[ch]) % (chInfo1[ch]->gridCountX * chInfo1[ch]->gridCountY) == 0
OCCl
IOGeneralInterest
pLSCConfig->channelGR.gridCountX == pLSCConfig->channelGB.gridCountX
/usr/local/share/firmware/isp/2921_02XX.dat
%@ %s\n
r
general
FrontCameraModuleSerialNumString
brcl
RadialGainEnable
/usr/local/share/firmware/isp/2325_01XX.dat
Reading rosaline power from sysconfig\n
IOServiceFirstPublish
=
DPCd
Could not find reference plist at %s (errno: %d). Will use ISP references
/Yonkers/YonkersPatch.DAT
/usr/local/share/firmware/isp/Savage/FrontIRHPR.DER
/System/Library/Isp/afpp/
/usr/local/share/firmware/isp/OCCl-cmcd.DAT
/usr/local/share/firmware/isp/1925_03XX.dat
Unexpected references size after compression (Expected %ld, Got %ld)\n
Found no IR sensor\n
IgnoreUnitInfoPlist
%s%s/%s
Prod
\taFDR may be used
Couldn't create reference file %s to write\n
not unified
Unable to find prox service
Error converting calibrated power value:  could not fit 32-bit value into 16-bit destination \n
/usr/local/share/firmware/isp/CmCl-Override.DAT
LsBypassVerify
/usr/local/share/firmware/isp/2123_01XX.dat
%lld
LoadPDEFiles: isOverridden %d
H16ISPServicesThread
DAT file for provisioned Savage - %@
%s-Ch%d.DAT
collectDiagState
EnableHawking
Failed to update %s token file. Will return false so someone looks at that...
yyyy-MM-dd HH:mm:ss
Failed to read boot time. errno %d
/var/mobile/Library/ISP/Pearl/NVM.bin
Reading rosaline power from IOReg\n
LSCAverageGreenApple
LSCComputeFromNVM.cpp
IOService
-sparseLP
Failed to send Romeo data file: 0x%08X\n
com.apple.h16ispdevicecontroller.notifications.queue
H16ISPServicesRemoteTypeKey
yes
LSC_GET_BASE_U32_PT(chInfo2[ch]) % (chInfo2[ch]->gridCountX * chInfo2[ch]->gridCountY) == 0
com.apple.isp.backtelecamerapower
token was removed
/usr/local/share/firmware/isp/1020_03XX.dat
/usr/local/share/firmware/isp/1922_02XX.dat
H16ISPServicesRemoteRGBIRReportKey
pCmdAppleChLSCConfigure->tableSize == pCmdAppleChDSCConfigure->numEntries
SendDataFileToFirmware
%s/%s.bin
unified
Could not read calibrated power from IOReg\n
H16ISPServicesRemoteRGBIRFinalInputPCEConfigKey
com.apple.dietappleh16camerad
Yonkers/YonkersPatch%s%s.DAT
DAT file for provisioned Yonkers - %@
<null>
/usr/local/share/firmware/isp/9723_01XX.dat
, calibration: 0x
Failed to save plist
floodComplianceRevision
Couldn't read vader compliance\n
getProperty
H16ISPServicesRemoteIORegPropertyNameKey
pLSCConfig->channelGR.gridCountY == pLSCConfig->channelGB.gridCountY
\tLooking for local cache\n
\tCalibration UUID mismatch, removing contents of directory\n
reference-%s__T_%lf.bin
Pearl FDR is %s, ToF FDR is %s
kCICMaxPerModuleX >= numXCIC
AP
ISP_SendCommand
/usr/local/share/firmware/isp/2224_01XX.dat
\tReading from FDR\n
No DAT file for Yonkers found
com.apple.isp.backsuperwidesensorconfig
/usr/local/share/firmware/isp/
LsIdealPctCam%d
/usr/local/share/firmware/isp/3525_02XX.dat
Can't activate %s projector: no projector token found
Saving %s\n
Could not find SEP reference location. Will use ISP references
H16ISPServicesRemoteDataKey
H16ISPServicesRemoteRGBIRBufferColorKey
H16ISPServicesRemoteRGBIRBufferIRKey
ISP_LoadIspAneAFPPFile
/usr/local/share/firmware/isp/4523_02XX.dat
com.apple.isp
/private/var/tmp/usr/standalone/firmware/Savage/SavagePatch.DAT
kGICMaxPerModuleY >= numYGIC
/usr/local/share/firmware/isp/7425_01XX.dat
%s token doesn't match platform. Token will be removed.
Creating local cache\n
wb
No DAT file for Savage found
YonkersFabRevision
%@-%@
com.apple.isp.frontcamerasensorconfig
Failed to send rosaline data file: 0x%08X\n
v16@?0^v8
/usr/local/share/firmware/isp/ISPUnitInfo.plist
isp_lacc.bin
LoadFDRCalDataFile
CALm
com.apple.coremedia
6.104
reference
H16ISPServicesRemoteRGBIRBufferDepthKey
YonkersMNS
System performed boot since %s token creation (boot time: %ld). Token will be removed.
/var/mobile/Documents/Pearl
\tFailed to initialize Manifest from ticket
H16ISPServicesRemoteReturnKey
Found Savage override DAT file, which takes precedence over all others - %@
chInfo1[ch]->gridCountX == chInfo1[0]->gridCountX
kCICMaxPerModuleY >= numYCIC
com.apple.isp.cameratorchcoolcurrent
/usr/local/share/firmware/isp/4523_01XX.dat
/var/mobile/Library/ISP/Pearl/PCECalib.bin
\t%@
SavageSNUM
/var/mobile/Library/ISP/Pearl/spotDB.bin
DEV
/usr/local/share/firmware/isp/CmPM-DPCm
LoadFDRFCClDataFile
/usr/local/share/firmware/isp/7623_01XX.dat
/usr/local/share/firmware/isp/9724_01XX.dat
/usr/local/share/firmware/isp/8824_01XX.dat
/usr/local/share/firmware/isp/2022_01XX.dat
AppleProxHIDEventDriver
/usr/local/share/firmware/isp/cam%dclocks.txt
cmcd
CacheDeviceConfigs
LoadPDEFiles: No Savage found. Never mind
Found reference plist at %s. Will use SEP references
SavageChipID
BackCameraSNUM
<UNKNOWN>
LsInterpMode
com.apple.dietappleh16camerad.destroy
/usr/local/share/firmware/isp/7525_01XX.dat
 not
\tDidn't find calibration\n
FormatDR
CmCl
H16ISPDevice.cpp
error loading ISPCPU firmware 
LsAdjustInvertCam%d
/usr/local/share/firmware/isp/2820_01XX.dat
/usr/local/share/firmware/isp/6221_01XX.dat
MultiCameraCalSwide
DPCm
GetSoCGeneration
com.apple.private.appleh16camerad.client
/usr/local/share/firmware/isp/2226_01XX.dat
Couldn't read from FDR: %@
doubleValue
FrontCameraOffsetFromDisplayCenter
ISP_SetFrontCameraOffsetFromDisplayCenter
soc-generation
/usr/local/share/firmware/isp/7324_01XX.dat
rb
sparseLP
Couldn't read SavageUID
/usr/local/share/firmware/isp/dcs_isp_fw.bin
registerDeviceIDForClient
/usr/local/share/firmware/isp/4524_01XX.dat
Testing if aFDR may be used
v32@?0@\"NSNumber\"8Q16^B24
LoadFrontIRHPRFile
com.apple.isp.cameratorchwarmcurrent
/usr/local/share/firmware/isp/0019_02XX.dat
dense
product
Error reading file\n
/usr/local/share/firmware/isp/cam%dsetfile.dat
:
/usr/local/share/firmware/isp/Savage/SavagePatchOverride.DAT
/System/Library/PrivateFrameworks/AppleCVHWA.framework/Firmware/
%s token has exceeded max allowed timeout. Token will be removed.
Using last allowed activation. %s token will be removed.
/var/mobile/Documents/Tokens.log
Expected file %s to be of size %ld. Actual size: %d\n
isp
sendMessageSync
/Savage/SavagePatch.DAT
ChannelArray
Failed to create log message string with code: %d (0x%X)
Found FrontIR override (has highest precedence) HPR file - camChannel = %d
No HPR file for frontIR found
GetUnitInfoPropertyDict
%s%s.%s
No C string description.
H16ISPServicesRemoteFusingDataKey
com.apple.dietappleh16camerad.writer
sha2-384
/
Reading rosaline serial number from sysconfig\n
ISP_ColdBootPowerCycle
SWDC
LoadOCClCalDataFile
NVM
chInfo2[ch]->gridCountY == chInfo2[0]->gridCountY
cmca
brgd
SavageMNS
chInfo2[ch]->gridCountX == chInfo2[0]->gridCountX
Sending special debug function to firmware object returned error : 0x%08x\n
xpcClientEventHandler
Load Yonkers DAT File: Size = %ld; SendStatus = %08x, 0x%08X
com.apple.isp.frontcamerapower
/usr/local/share/firmware/isp/dcs_v5x_isp_fw.bin
DisableDropDetection
setProperty
\tLooking for FDR data\n
isp-command-send
/usr/local/share/firmware/isp/3525_01XX.dat
Failed to read PCE Calibration (FDR data)\n
H16ISPDevice
ISP_PowerOnCamera
kGICMaxPerModuleX >= numXGIC
/usr/local/share/firmware/isp/CmPM-dcnu
Failed to read unique chip identifier
\tFound\n
Error: Couldn't send rosaline configuration\n
SavageDeviceRev
Found Yonkers override DAT file, which takes precedence over all others - %@
com.apple.isp.cameratorch
false
/var/mobile/Library/ISP
rosaline-serial-num
Couldn't read SavageChipID
multi-camera-cal-swide
^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8
Failed to send references to FW\n
true
Ymgt
chInfo1[ch]->gridCountY == chInfo1[0]->gridCountY
LsAdjustEnableCam%d
com.apple.dietappleh16camerad.launch
pDevice is NULL
%s token timeout was reached (current time %ld). Token will be removed.
BootManifestHash
H16ISPServicesRemoteCFTypeNameKey
DAT file for unprovisioned Yonkers - %@
Couldn't create SavageChipID string ref
BackCameraModuleSerialNumString
/usr/local/share/firmware/isp/FCCl-Override.DAT
/usr/local/share/firmware/isp/2226_02XX.dat
/usr/local/share/firmware/isp/1921_01XX.dat
\tCouldn't get boot manifest hash
rosaline-calibration-current
DAT file for unprovisioned Savage - %@
Load Savage DAT File: Size = %ld; SendStatus = %08x, FileStatus = 0x%08X
Couldn't create SavageUID string ref
com.apple.isp.backtelecamerasensorconfig
Failed to remove %s token: %@
UniqueChipID
denseLP
device
Ngsk
MultiCameraCalWide
/usr/local/share/firmware/isp/ispane.afpp
BackTeleCameraModuleSerialNumString
/usr/local/share/firmware/isp/4723_01XX.dat
services
/var/mobile/Library/ISP/Pearl
\tCan't create %s! (%d)\n
Couldn't read unified Pearl FDR: %@
Sending reference file %s, type: %d\n
LoadHPR
front-camera-cal-swide
/usr/local/share/firmware/isp/6222_01XX.dat
basic_string
Could not open input file: %s\n
no
Savage/SavagePatch%s.DAT
com.apple.isp.backcamerapower
 \n
CopyFileToBuffer
/usr/local/share/firmware/isp/3624_01XX.dat
\taFDR may%s be used (%d, %d)
%s/%@
%s/reference-%s.plist
Secure RGB sensor not detected
FCCl
iCCl
/usr/local/share/firmware/isp/Yonkers/YonkersPatchOverride.DAT
\tIgnoring unexpected cached version (%d != %d)\n
IR sensor not detected
Dev
DAT
BackSuperWideCameraSNUM
/usr/local/share/firmware/isp/CmPM-brgd
dcnu
```
