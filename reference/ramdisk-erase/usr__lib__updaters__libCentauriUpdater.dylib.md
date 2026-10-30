# `/usr/lib/updaters/libCentauriUpdater.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 402,240 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 31 (Size: 3544)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (14)

- `/usr/lib/updaters/libCentauriUpdater.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/AirshipCentauriHelper.framework/AirshipCentauriHelper (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/CentauriController.framework/CentauriController (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/Centauri.framework/Centauri (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/AppleConvergedFirmwareUpdater.framework/AppleConvergedFirmwareUpdater (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Strings (1,069)

```
ccpu image missing
%s::%s: failed to get host platform identifier\n
%s::%s: failed to get offset for subsystem 2 memswap section\n
%s::%s: null info at index %zu\n
%s::%s: uninitialized updater\n
uninitialized updater
%s::%s: successfully set host platform identifiers to (0x%08x, 0x%08x)\n
=
remote
Wireless1,RTKitOSLPEM
%s::%s: %s firmware is incompatible with %s hardware\n
%s::%s: received oid %u, expected %u\n
generateBootNonce
%s::%s: manifest unique id too large\n
gid mismatch
Wireless1,BoardID
%s::%s: failed to hand off memswap regions\n
RestoreFailure
%s::%s: failed to copy WSKU\n
failed to remove alpha tag
updater has wrong type
%s::%s: skipping reset for non-silicon platform\n
%s::%s: invalid boot mode %d\n
failed to allocate image buffer
%s::%s: successfully created secondary ftab\n
failed to create bootargs string
getManifestUniqueId_block_invoke
%s::%s: certification failed\n
%s::%s: no crashlogs found\n
%s::%s: successfully sent image: out code 0x%08x\n
secondary lpm boot
%s::%s: builtin, host chip ID 0x%04x, host board ID 0x%04x\n
%s::%s: failed to allocate diagnostic object\n
%s::%s: failed to collect logs: 0x%08x\n
%s::%s: payload too large\n
%s::%s: boot driver not opened\n
%s::%s: %s: section too large in %s: offset %zu, section size %u, total size %zu\n
%s::%s: subCC wrong key type\n
%s::%s: already preflighted, removing nonce\n
Wireless1,ACIBTLPEM
null updater
%s::%s: Enable second boot stage: %s\n
failed to update beta tag
%s::%s: error getting host ECID\n
%s::%s: ignoring empty WSKU\n
%s::%s: failed to load CoreCaptureDaemon framework\n
%s::%s: failed to get Thunderbolt device info\n
%s::%s: failed to get thunderbolt port from path\n
%s::%s: global-scale not found\n
%s::%s: %s: section too small in %s\n
setPatchBay
failed to allocate keys
failed to read raw calibration data
%s::%s: stopping CoreCapture\n
Wireless1,ScanBTManuf
failed to create restore object
failed to create command payload
failed to create controller
%s::%s: failed to get offset for subsystem 0 memswap section\n
CentauriUpdaterIsDone
%s::%s: opening control driver\n
%s::%s: failed to get size for subsystem 2 memswap section\n
-
low power
%s::%s: no bver\n
%s::%s: failed to get manager's parent: 0x%08x\n
getThunderboltDeviceInfo
%s::%s: updater is %s\n
%s::%s: returning cached values\n
%s::%s: failed to write doorbell\n
%s::%s:     subsystem 1: offset %llu, size %u\n
%s::%s: failed to get required file size from header\n
cal-data-with-metadata.bin
failed to update alpha tag
failed to write
%s::%s: no board parameters\n
copyRFEM
copyWSKU
%s::%s: no diagnostics path\n
%s::%s: thunderbolt path property has wrong type %s\n
%s::%s: failed to find thunderbolt port's parent: 0x%08x\n
secondary ftab header has wrong type
%s::%s: closing interface driver\n
%s::%s: image buffer is smaller than requested size (%u < %u)\n
failed to get size for subsystem 2 memswap section
%s::%s:     subsystem 2: offset %llu, size %u\n
failed to create diagnostic filename
empty data class
%s::%s: failed to find service\n
%s::%s: creating updater\n
%s::%s: Timeouts:\n
%s::%s: =========================\n
%s::%s: firmware intended for chip revision %s\n
%s::%s: save dir: %s\n
%@ enable_sik=1
Wireless1,PhyBluetooth5GTrim
%s::%s:     ROM send image: %lld milliseconds\n
%s::%s: failed to allocate image buffer\n
gatherPreflightParameters
Wireless1,Wifi5GLPhyManuf
Wireless1,BTSecondary
%s::%s: device vendor ID property has wrong type %s\n
%s::%s: failed to get boot nonce hash\n
%s::%s: failed to create personalization parameters\n
failed to get firmware data
%s::%s: failed to allocate values\n
%s::%s: failed: %s\n
failed to write host platform identifier
enabled
%s::%s: failed to get offset for subsystem 1 memswap section\n
RFEM:
%s::%s: Centauri boot-args option has wrong type\n
%s::%s: error status %u in response\n
%s::%s: failed to create restore object\n
%s::%s:     CCHI stage transport driver open: %lld milliseconds\n
setHostPlatformIdentifiers
%s::%s: failed to determine whether Centauri is builtin\n
WSKU
%s::%s: WSKU not found\n
CentauriTransport
%s::%s: failed to reset chip: 0x%08x\n
%s::%s: requesting offset %u, size %u\n
boot driver not opened
sim
%s::%s: failed to allocate secondary memory: 0x%08x\n
%s::%s: failed to remove alpha tag\n
subCC wrong key type
%s::%s: preparing to send an image\n
%s::%s: host platform identifier read back (0x%08x) doesn't match host platform identifier written (0x%08x)\n
openControlDriver
%s::%s: failed to create string\n
Wireless1,PhyBlueToothLPM
%s::%s: host chip ID (%lld) or board ID (%lld) out of range\n
%s::%s: failed to get boot nonce\n
%s::%s: secondary ftab header has wrong type\n
%s::%s: Boot mode: %s\n
parseDeviceBootArgs
handOffMemswapRegions
%s::%s: %s: %s invalid\n
%s::%s: no chip revision in bver\n
%s::%s: failed to initialize restore object\n
%s::%s: successfully executed command %s\n
CentauriUpdaterCopySiKPublicKey
Wireless1,RestoreRTKitOS
%s::%s: failed to allocate data\n
%s::%s: failed to validate calibration dict\n
%s::%s: failed to create working dir\n
setBootTimestamp
Wireless1,ChipRev
%s::%s: failed to set host platform identifier\n
%s::%s: image size %u -> %u\n
manifest unique id too large
subCC null value
%s::%s:     subsystem 0: offset %llu, size %u\n
%s::%s: failed to allocate buffer\n
CentauriUpdaterCreate
%s::%s: null updater\n
openInterfaceDriver
%s::%s: failed to get device vendor ID property\n
pingCheck
%s::%s: failed to create hello response\n
%s::%s: failed to open boot object for %s stage: 0x%08x\n
failed to read
failed to create response payload
Crashlog.CTRL.bin
%s::%s: unsupported version %u\n
<CentauriUpdater>{}
%s::%s: unexpected response size %zu\n
%s::%s: received sequence num %u, expected %u\n
%s::%s: setting host platform identifiers to (0x%08x, 0x%08x)\n
%s::%s: failed to get size for subsystem 1 memswap section\n
%s::%s: failed to create subsystem id key\n
%s::%s: failed to compute manifest unique id\n
Wireless1,Wifi2GLPhyManuf
%s::%s: failed to get ecid\n
host platform identifier read back mismatch
hw.model
%s::%s: Overriding second boot stage to %s due to %s boot-arg\n
%s::%s: failed to get size for subsystem 0 memswap section\n
%s::%s: failed to create metadata key\n
%s::%s: failed to create transport object\n
%s::%s: failed to register class with CF\n
sendBootTimestamps
sendImage
%s::%s: failed to update calibration tag\n
failed to get manifest unique id
Wireless1,Wifi5GLMAC
Wireless1,PhyBluetoothTrim
getManifestUniqueId
does not support
%@/scratch
%s::%s: failed to convert device model ID to an integer\n
Wireless1,ECID
%s::%s: failed to get firmware data\n
%s::%s: %s: %s has wrong type\n
%s::%s: subCC null value\n
Wireless1,ACIBTManuf
CentauriFirmware
Wireless1,Wifi2GLPhy
failed to read boot flags
ROM
%s::%s: proceeding to boot without any calibration data\n
certificationVersion
%s::%s: Destroying updater\n
%s::%s: failed to open control driver\n
silicon
%s::%s: failed to copy nvram payload\n
%s::%s: failed to add alpha tag\n
%s::%s: failed to get host chip ID (%lld) or board ID (%lld)\n
failed to copy sik public key
sequence number mismatch
%s::%s: failed to read boot flags\n
%s::%s: parsing secondary ftab header in primary ftab\n
%s::%s: failed to copy calibration data\n
%s::%s: failed to read raw calibration data\n
%s::%s: failed to get board params\n
failed to get board params
%s::%s: failed to open transport driver for rom\n
%s::%s: success: '%s'\n
sendCCHICommand
%s::%s: failed to write: 0x%08x\n
%s::%s: invalid subsystem ID %u at index %zu\n
failed to insert WSKU into nvram overrides
BWC3
%s::%s: hw.model: \"%s\"\n
failed to get required file size from header
%s::%s: failed to update beta tag\n
failed to allocate values
isCentauriBuiltin
%s::%s:     Second stage transport driver open: %lld milliseconds\n
failed to create interface object
failed to write boot flags
%s::%s: failed to update nvram tag\n
wifi-rfem-info
%s::%s: checking if updater is done\n
failed to copy RFEM
failed to add calibration tag
%s::%s: manifest unique id: '%s'\n
Wireless1,CoexRealTimeArbiter
%s::%s: failed to send image on %s stage: 0x%08x: out code 0x%08x\n
failed to get size for subsystem 1 memswap section
vector
centauri
Custom Centauri boot-args:
%s::%s: failed to load Centauri framework\n
%s::%s: response length mismatch: %hu != %u\n
%s::%s: handing off memswap regions to control driver\n
%s::%s: failed to create key and/or value\n
%s::%s: failed to create bootargs string\n
%s::%s: Firmware boot-args: <none>\n
%s::%s: failed to create firmware object\n
%s::%s: failed to create updater\n
openBootDriver
%s::%s: opening boot object\n
image buffer is smaller than requested size
failed to remove beta tag
%s::%s: successfully created updater\n
No
supports
%s::%s: unexpected size %zu\n
%s::%s: bver: '%s'\n
generic
failed to read host platform identifier
Wireless1,ScanBTLPEM
CentauriCommon
Wireless1,ChipID
%s::%s: different stage already open\n
failed to create boot object
%s::%s: working dir: %s\n
Wireless1,WiFiTxManuf
Wireless1,BTOTPDatabase
%s::%s: failed to create controller: 0x%08x\n
%s::%s: failed to set mem swap regions: 0x%08x\n
parseCrashlogs
%s::%s: found raw calibration data: index %zu\n
Wireless1,Wifi2GLMACManuf
Wireless1,Wifi5GLPhyTrim
%s::%s: no diagnostics path, skipping CoreCapture initialization\n
pushFirmware
%s::%s: failed to get tag for boot mode\n
%s::%s: successfully set boot flags to 0x%x\n
global-scale
%s::%s: failed to create update operations\n
%s::%s: device vendor ID out of range: %lld\n
CentauriUpdaterExecCommand
%s::%s: failed to copy sik public key\n
%s::%s: failed to read host platform identifier\n
failed to copy WSKU
%s::%s: successfully generated identifiers (0x%08x, 0x%08x)\n
%s::%s: generated a boot nonce\n
%s::%s: unknown sikBlobType: %u\n
setBootFlags
proxima-platform
%s::%s: error getting host chipID\n
%s::%s: subCC null key\n
Wireless1,WifiRegData
Wireless1,PhyBlueTooth5G
failed to get tag for boot mode
%s::%s: success: %s\n
failed to add alpha tag
copyCalibrationData
%s::%s: failed to insert bootargs into nvram overrides\n
%s::%s: (0x%04x, 0x%04x) -> %hhu\n
%s::%s: failed to get chip information\n
%s::%s:     Second stage send image: %lld milliseconds\n
%s::%s: global-scale has wrong type\n
%s::%s: metadata at index %zu has wrong type\n
%s::%s: no raw calibration data provided\n
%s::%s: failed to initialize logging\n
%s::%s: === CentauriTransport Config ===\n
failed to create chip class
%s::%s: %s: section version mismatch in %s: expected 0x%x, found 0x%x\n
%s::%s: failed to parse debug arguments\n
%s::%s: failed to create command payload\n
%s::%s: creating boot object\n
closeBootDriver
getSupportedChipRevision
%s::%s: failed to convert save dir\n
Wireless1,Wifi5GLMACManuf
%s::%s: failed to create interface object\n
%s::%s: \n
v8@?0
%s::%s: cannot boot in %s mode since %s image is missing from firmware\n
copySiKCertificateSigningRequest
%s::%s: failed to create mutable data\n
kern.bootargs
%s::%s: bad parameter\n
%s::%s: wrong response size: expected %zu, received %zu\n
failed to get host platform identifier
ChipID
%s::%s: no FDR calibration data found\n
Wireless1,WiFiRx
Wireless1,CCPUApplicationFirmware
Wireless1,Wifi2GLPhyTrim
centauri-builtin
failed to create nvram generator
%s::%s: successfully added an nvram file\n
%s::%s: replacing %u bytes of existing alpha data in firmware\n
init
getBoardParameters
%s::%s: failed to read host platform sub-variant identifier\n
simulator
map::at:  key not found
%s::%s: CentauriUpdater Version: %s\n
%s::%s: %s: %s not found\n
certification failed
Wireless1,ScanWifiManuf
Wireless1,PhyBlueTooth
%s::%s: bootedQuery %s, generateNonce %s\n
%s::%s: failed to create response payload\n
failed to read host platform sub-variant identifier
%s::%s: failed to get hw.model\n
no board parameters
%s::%s: %s: failed to get %s ptr\n
%s::%s: already open\n
%s::%s: creating interface object\n
payload too large
Wireless1,RTKitOS
%s::%s: failed to validate calibration data\n
%s::%s: failed to write host platform sub-variant identifier\n
%s::%s: %s: %s buffer too small: %zu bytes\n
%s::%s: Firmware boot-args: '%s'\n
%s::%s: replacing %u bytes of existing calibration data in firmware\n
Wireless1,SecurityMode
failed to get boot nonce hash
%s::%s: failed to get domain/mode\n
%s::%s: received gid %u, expected %u\n
oid mismatch
getPlatform
Wireless1,ProductionMode
writeRegister
%s::%s: overriding platform due to global-scale\n
%s::%s: Defaulting to disable second boot stage for FPGA platform during restore\n
basic_string
%s::%s: failed to insert RFEM into nvram overrides\n
failed to get size for subsystem 0 memswap section
%s::%s: failed to add %s\n
%s::%s: updater has wrong type\n
runCertification
raw
Wireless1,Wifi2GLMAC
Wireless1,WiFiOTPDatabase
Thunderstrike
getDebugInfo
%s::%s: info at index %zu has wrong type\n
%s::%s: failed to insert WSKU into nvram overrides\n
getPlatformIdentifiers
%s::%s: failed to find manager service\n
%s::%s: success\n
%s::%s: failed to initialize base class\n
failed to determine whether Centauri is builtin
%s::%s: failed to add to nvram generator\n
%s::%s: creating fresh nvram file with only overrides\n
Wireless1,PhyBlueToothManuf
v20@?0i8r*12
Metadata
%s::%s: failed to create boot-args\n
unknown
%s::%s: initializing memswap\n
%s::%s: sending image\n
Wireless1,ACIBT
failed to get boot nonce
failed to get chip information
%s::%s: giving up after %u failed attempts\n
initWithParameters
%s::%s: failed to write boot flags\n
/usr/standalone/firmware/Centauri/
Device Vendor ID
getThunderboltIdentifier
failed to allocate diagnostic object
Wireless1,RestoreBootNonce
%s::%s: failed to open interface object: 0x%08x\n
%s::%s: no metadata at index %zu\n
cal-file-%u-%s.bin
isChipRevisionSupported
%s::%s: failed to convert working dir\n
Wireless1,ACIWiFiTxManuf
Wireless1,SecurityDomain
Wireless1,BTRegData
Wireless1,PhyBlueTooth5GManuf
isCentauriBuiltin_block_invoke
copySiKPublicKey
%s::%s: closing boot driver\n
failed to send image on %s stage: 0x%08x: out code 0x%08x
%s::%s: requesting buffer of size %u\n
%s::%s: failed to convert subsystem ID at index %zu\n
%s::%s: %s: failed to create crashlog name\n
Crashlog.WFMAIN.bin
failed to add nvram tag
secondary boot
%s::%s: merging nvram overrides with existing nvram file\n
%s::%s: replacing %u bytes of existing beta data in firmware\n
%s::%s: data class too large\n
%s::%s: unexpected type %s\n
BoardId
%s::%s: interface driver not opened\n
error status in response
%s::%s: failed to read doorbell\n
%s::%s: successfully opened control driver\n
%s::%s: removing %u bytes of existing beta data from firmware\n
failed to get domain/mode
%s::%s: failed: 0x%08x\n
%s::%s: successfully opened CCHI interface driver\n
%s::%s: sending:\n
%s::%s: successfully handed off memswap regions\n
%s::%s: successfully inserted calibration data into firmware\n
%s::%s: error converting host chipID\n
%s::%s: empty data class\n
%s::%s:     ROM transport driver open: %lld milliseconds\n
failed to open interface object
scrt
Wireless1,BTSecondaryManuf
%s::%s: bad firmware size\n
%s::%s: failed to create error\n
Wireless1,ScanWifi
%s::%s: executing command %s\n
failed to get image buffer address
%s::%s: failed to add calibration tag\n
subCC null key
failed to instantiate CF object
failed to register class with CF
bad firmware size
%s::%s: closing control driver\n
%s::%s: failed to extract chip revision\n
IOService
bad parameter
%s::%s: opening CCHI interface driver\n
%s::%s: global-scale has wrong length %zu\n
%s::%s: failed to get boot-args\n
%s::%s: Overriding platform to FPGA due to %s boot-arg\n
%s::%s: failed to create diagnostic filename\n
%s::%s: failed to read: 0x%08x\n
create
failed to get offset for subsystem 2 memswap section
UniqueChipID
AppleCentauriManager
%s::%s: failed to create secondary ftab\n
Yes
%s::%s: failed to get RTKit firmware\n
interface driver not opened
%s::%s: failed to determine platform\n
%s::%s: opening boot driver for %s stage\n
machine-timeouts
createSecondaryFtab
%s::%s: device model ID out of range: %lld\n
failed to write host platform sub-variant identifier
SubsystemID
Wireless1,Ticket
fdr
closeInterfaceDriver
readRegister
%s::%s: failed to execute command %s\n
setControllerProperties
reset
%s::%s: amount read too large: %u\n
%s::%s: failed to extract chip id\n
%s::%s: subCC wrong value type\n
%s::%s: ignoring FDR calibration data if it exists\n
%s::%s: property has wrong type %s\n
startCoreCapture
%s::%s: failed to convert device vendor ID to an integer\n
%s::%s: failed to create save path\n
Wireless1,Wifi5GLPhy
failed to get RTKit firmware
%s::%s: same stage already open\n
%s::%s: failed to get image buffer address\n
 
BT
queryCmd
failed to allocate transport object
amount read too large
boot flags read back mismatch
%s::%s: failed to map memory: 0x%08x\n
%s::%s: failed to create nvram generator\n
%s::%s: failed to update alpha tag\n
%s::%s: failed to generate boot nonce\n
%s::%s: skipping since second boot stage is disabled\n
%s::%s: inserting %ld bytes of %s calibration data into firmware\n
failed to create dictionary
%s::%s: received:\n
failed to insert RFEM into nvram overrides
failed to validate calibration dict
%s::%s: RFEM not found\n
%s::%s: failed to initialize base restore object\n
%s::%s: starting CoreCapture\n
enable_sik=1
Wireless1,ScanBluetooth
%s::%s: boot flags read back (0x%08x) don't match boot flags written (0x%08x)\n
failed to get offset for subsystem 1 memswap section
alpha-patch-bay.bin
CoalescedSubTargetID
Device Model ID
%s::%s: total size %u\n
%s::%s: failed to write register %u (%u bytes): 0x%08x\n
%s::%s: allocated image buffer of size %u\n
normal
%s::%s: looking for calibration data, firmware %s FDR trust evaluation\n
Wireless1,MinEpoch
%s::%s: Client owns control driver: %s\n
%s::%s: %s: %s crashlog header reports empty: %zu bytes\n
%s::%s: added key: %s, value: %llu\n
BootArgs
%s::%s: unexpected response size %zu for GetSize, expected %zu\n
%s::%s: boot driver closed\n
%s::%s: %s: %s crashlog size larger than buffer (%zu > %zu)\n
setCalibration
%s::%s: WSKU: '%s'\n
%s::%s: %s: string section too small in %s: %u bytes\n
Crashlog.BTMAIN.bin
failed to allocate data
%s::%s: wrong firmware type\n
%s::%s: failed to initialize transport object\n
failed to open boot object for %s stage: 0x%08x
host platform sub-variant identifier read back mismatch
%s::%s: Defaulting to disable second boot stage for simulator platform during restore - this is temporary\n
subCC wrong value type
%s::%s: failed to start CoreCapture\n
different stage already open
%s::%s: failed to read register %u (%u bytes): 0x%08x\n
%s::%s: setting boot flags to 0x%x\n
control driver not open
beta-patch-bay.bin
data class too large
%s::%s: failed to create domain\n
secondary ftab header missing from primary ftab
%s::%s: failed to allocate transport object\n
%s::%s: successfully opened boot driver for %s stage\n
centauri-second-stage
%s::%s: control driver not open\n
failed to add to nvram generator
%s
%s::%s: opening interface object\n
%s::%s: boot-args: \"%s\"\n
%s::%s: failed to add beta tag\n
%s::%s: certification requested\n
%s::%s: get crashlogs returned success but no crashlogs\n
failed to extract chip id
failed to copy nvram payload
%s::%s: failed to remove beta tag\n
%s::%s: Extend timeouts for SiK generation: %s\n
failed to allocate buffer
proxima
%s::%s: %s: '%s'\n
createEmpty
%s::%s: found subCC index %zu: %s\n
%s::%s: thunderbolt, %s\n
centauri-builtin-protium
%s::%s: Enable log collection: %s\n
%s::%s: host platform sub-variant identifier read back (0x%08x) doesn't match host platform sub-variant identifier written (0x%08x)\n
-restore
failed to set mem swap regions
failed to remove calibration tag
chip_revision_([a-zA-Z][0-9])
%s::%s: failed to create regex: %s\n
%s::%s: attempt %u of %u\n
%s::%s: failed to copy RFEM\n
%s::%s: device model ID property has wrong type %s\n
TigrisCreek
failed to get ecid
%s::%s: response too small: %u\n
%s::%s: removing %u bytes of existing alpha data from firmware\n
%s::%s: failed to get thunderbolt path property\n
%s::%s: failed to open interface driver\n
%s::%s: no response payload\n
%s::%s: error converting host ECID\n
failed to validate calibration data
Wireless1,FirmwareDigestArray
failed to create personalization parameters
%s::%s: Platform: %s\n
%s::%s: failed to create boot object for %s stage\n
%s::%s: memswap sections in secondary ftab:\n
%s::%s: %s: %s crashlog too small: %zu bytes\n
failed to update calibration tag
%s::%s: no calibration data found\n
%s::%s: swapping endianness\n
done
response too small
%s::%s: successfully merged nvram overrides with existing nvram file\n
%s::%s: invalid byte at offset %u\n
%s::%s: invalid value for %s debug arg\n
operator()
%s::%s
%s::%s: failed to create description\n
%s::%s: CSR unavailable\n
%s::%s: failed to unmap memory: 0x%08x\n
%s::%s: failed to create dictionary\n
performCmd
Wireless1,ACIWIFI
Wireless1,WiFiTx
Wireless1,WiFiRxManuf
response length mismatch
%s::%s: timed out: doorbell value 0x%08x\n
%s::%s: secondary ftab header missing from primary ftab\n
%s::%s: failed to initialize timestamps dictionary\n
failed to allocate secondary memory
skipReset
CentauriUpdaterFinalize
failed to create hello response
%s::%s: log collection disabled\n
closeControlDriver
%s::%s: failed to get manifest unique id\n
collectLogs
::
nvram.bin
%s::%s: failed to instantiate CF object\n
%s::%s: failed to write host platform identifier\n
Control
%s::%s: failed to add nvram tag\n
%s::%s: failed to remove calibration tag\n
Centauri
%s::%s: removing %u bytes of existing calibration data from firmware\n
Thunderbolt Path
CentauriUpdater
%s::%s: booting in %s mode\n
%s::%s: subsystem ID at index %zu has wrong type\n
%s::%s: failed to allocate keys\n
createError
CentauriPlatform
not done yet
%s::%s: failed to get crashlogs: 0x%08x\n
failed to get offset for subsystem 0 memswap section
WiFi
CentauriRestore
%s::%s: machine-timeouts not found\n
failed to map secondary memory
%s::%s: no subsystem ID at index %zu\n
failed to update nvram tag
%s::%s: using existing nvram file as is\n
%s::%s: failed to get device model ID property\n
failed to initialize logging
fpga
disabled
%s::%s: creating empty nvram file\n
failed to add beta tag
%s::%s: %s not found\n
no response payload
%s::%s: interface driver closed\n
%s::%s: failed to create chip class\n
%s::%s: %s: %s empty\n
%s::%s: found FDR calibration data: %s\n
~CentauriRestore
Wireless1,Nonce
%s::%s: failed to create matching dict\n
setNVRAM
%s::%s: secondary ftab header missing from primary ftab\n
%s::%s: already preflighted, removing nonce\n
%s::%s: failed to convert device vendor ID to an integer\n
%s::%s: failed to get boot nonce hash\n
%s::%s:     ROM transport driver open: %lld milliseconds\n
%s::%s: =========================\n
%s::%s: interface driver closed\n
%s::%s: failed to set mem swap regions: 0x%08x\n
%s::%s: failed to allocate data\n
%s::%s: Defaulting to disable second boot stage for simulator platform during restore - this is temporary\n
%s::%s: found subCC index %zu: %s\n
%s::%s: cannot boot in %s mode since %s image is missing from firmware\n
%s::%s: successfully set host platform identifiers to (0x%08x, 0x%08x)\n
%s::%s: global-scale has wrong type\n
%s::%s: Firmware boot-args: '%s'\n
%s::%s: device vendor ID property has wrong type %s\n
%s::%s: failed to open boot object for %s stage: 0x%08x\n
%s::%s: creating fresh nvram file with only overrides\n
%s::%s: failed to get manifest unique id\n
%s::%s: found FDR calibration data: %s\n
%s::%s: failed to create transport object\n
%s::%s: booting in %s mode\n
%s::%s: success: %s\n
%s::%s: Enable second boot stage: %s\n
%s::%s: %s: %s empty\n
%s::%s: %s: %s crashlog header reports empty: %zu bytes\n
%s::%s: failed to add %s\n
%s::%s: unsupported version %u\n
%s::%s: failed to insert bootargs into nvram overrides\n
%s::%s: failed to add calibration tag\n
%s::%s: unexpected type %s\n
%s::%s: WSKU not found\n
%s::%s: stopping CoreCapture\n
%s::%s: failed to create domain\n
%s::%s: (0x%04x, 0x%04x) -> %hhu\n
%s::%s: uninitialized updater\n
%s::%s: failed to initialize transport object\n
%s::%s:     CCHI stage transport driver open: %lld milliseconds\n
%s::%s: successfully handed off memswap regions\n
%s::%s: failed to add alpha tag\n
%s::%s: failed to get thunderbolt path property\n
%s::%s: failed to collect logs: 0x%08x\n
%s::%s: Enable log collection: %s\n
%s::%s: boot driver closed\n
%s::%s: failed to read: 0x%08x\n
%s::%s: parsing secondary ftab header in primary ftab\n
%s::%s: error converting host chipID\n
%s::%s: giving up after %u failed attempts\n
%s::%s: failed to create working dir\n
%s::%s: failed to initialize logging\n
%s::%s: failed to create restore object\n
%s::%s: received gid %u, expected %u\n
%s::%s: invalid subsystem ID %u at index %zu\n
%s::%s: error getting host chipID\n
%s::%s: failed to create personalization parameters\n
%s::%s: failed to create response payload\n
%s::%s: successfully sent image: out code 0x%08x\n
%s::%s: no metadata at index %zu\n
%s::%s: creating empty nvram file\n
%s::%s: error getting host ECID\n
%s::%s: failed to copy sik public key\n
%s::%s: failed to get domain/mode\n
%s::%s: failed to get host platform identifier\n
%s::%s: failed to hand off memswap regions\n
%s::%s: skipping reset for non-silicon platform\n
%s::%s: CSR unavailable\n
%s::%s: failed to get hw.model\n
%s::%s: ignoring FDR calibration data if it exists\n
%s::%s: failed to create mutable data\n
%s::%s: closing boot driver\n
%s::%s: failed to get offset for subsystem 1 memswap section\n
%s::%s: requesting buffer of size %u\n
%s::%s: %s: %s crashlog too small: %zu bytes\n
%s::%s: %s not found\n
%s::%s: certification failed\n
%s::%s: working dir: %s\n
%s::%s: machine-timeouts not found\n
%s::%s: failed to get thunderbolt port from path\n
%s::%s: failed to execute command %s\n
%s::%s: failed to get image buffer address\n
%s::%s: failed to create subsystem id key\n
%s::%s: data class too large\n
%s::%s: failed to initialize restore object\n
%s::%s: failed to convert device model ID to an integer\n
%s::%s: failed to open interface driver\n
%s::%s: failed to get ecid\n
%s::%s: failed to get chip information\n
%s::%s: failed to get crashlogs: 0x%08x\n
%s::%s: failed: 0x%08x\n
%s::%s: interface driver not opened\n
%s::%s: Firmware boot-args: <none>\n
%s::%s: failed to load Centauri framework\n
%s::%s: hw.model: \"%s\"\n
%s::%s: inserting %ld bytes of %s calibration data into firmware\n
%s::%s: failed to find service\n
%s::%s: %s\n%@
%s::%s: wrong firmware type\n
%s::%s: device vendor ID out of range: %lld\n
%s::%s: wrong response size: expected %zu, received %zu\n
%s::%s: failed to unmap memory: 0x%08x\n
%s::%s: %s: %s crashlog size larger than buffer (%zu > %zu)\n
%s::%s: %s: section too small in %s\n
%s::%s: failed to update beta tag\n
%s::%s: manifest unique id too large\n
%s::%s: failed to read raw calibration data\n
%s::%s: bootedQuery %s, generateNonce %s\n
%s::%s: failed to get boot nonce\n
%s::%s: unexpected response size %zu for GetSize, expected %zu\n
%s::%s: Timeouts:\n
%s::%s: received:\n
%s::%s: timed out: doorbell value 0x%08x\n
%s::%s: replacing %u bytes of existing calibration data in firmware\n
%s::%s: failed to convert working dir\n
%s::%s: \n
%s::%s: log collection disabled\n
%s::%s: response too small: %u\n
%s::%s: failed to create save path\n
%s::%s: failed to update alpha tag\n
%s::%s: no diagnostics path, skipping CoreCapture initialization\n
%s::%s: secondary ftab header has wrong type\n
%s::%s: success: '%s'\n
%s::%s: failed to create diagnostic filename\n
%s::%s: error converting host ECID\n
%s::%s: WSKU: '%s'\n
%s::%s: updater is %s\n
%s::%s: requesting offset %u, size %u\n
%s::%s: failed to create key and/or value\n
%s::%s: failed to allocate values\n
%s::%s: subCC wrong value type\n
%s::%s: failed to add to nvram generator\n
%s::%s: invalid value for %s debug arg\n
%s::%s: attempt %u of %u\n
%s::%s: failed to instantiate CF object\n
%s::%s: updater has wrong type\n
%s::%s: allocated image buffer of size %u\n
%s::%s: successfully merged nvram overrides with existing nvram file\n
%s::%s: found raw calibration data: index %zu\n
%s::%s: no raw calibration data provided\n
%s::%s: ignoring empty WSKU\n
%s::%s: firmware intended for chip revision %s\n
%s::%s: checking if updater is done\n
%s::%s: get crashlogs returned success but no crashlogs\n
%s::%s: unexpected response size %zu\n
%s::%s:     ROM send image: %lld milliseconds\n
%s::%s: failed to create interface object\n
%s::%s: failed to create controller: 0x%08x\n
%s::%s: failed to remove calibration tag\n
%s::%s: failed to initialize base restore object\n
%s::%s: no response payload\n
%s::%s: === CentauriTransport Config ===\n
%s::%s: failed to allocate buffer\n
%s::%s: failed to get offset for subsystem 2 memswap section\n
%s::%s: null info at index %zu\n
%s::%s: replacing %u bytes of existing alpha data in firmware\n
%s::%s: subCC null key\n
%s::%s: failed to create update operations\n
%s::%s: failed to create boot object for %s stage\n
%s::%s: boot driver not opened\n
%s::%s: no subsystem ID at index %zu\n
%s::%s: merging nvram overrides with existing nvram file\n
%s::%s: subCC null value\n
%s::%s: failed to start CoreCapture\n
%s::%s: failed to create description\n
%s::%s: host chip ID (%lld) or board ID (%lld) out of range\n
%s::%s: received sequence num %u, expected %u\n
%s::%s: Overriding second boot stage to %s due to %s boot-arg\n
%s::%s:     subsystem 0: offset %llu, size %u\n
%s::%s: successfully inserted calibration data into firmware\n
%s::%s: failed to allocate keys\n
%s::%s: bver: '%s'\n
%s::%s: failed to get board params\n
%s::%s: failed to get device vendor ID property\n
%s::%s: host platform identifier read back (0x%08x) doesn't match host platform identifier written (0x%08x)\n
%s::%s: info at index %zu has wrong type\n
%s::%s: failed to register class with CF\n
%s::%s:     Second stage transport driver open: %lld milliseconds\n
%s::%s: failed to write boot flags\n
%s::%s: removing %u bytes of existing calibration data from firmware\n
%s::%s: failed to validate calibration data\n
%s::%s: no bver\n
%s::%s: executing command %s\n
%s::%s: %s: %s invalid\n
%s::%s: RFEM not found\n
%s::%s: failed to generate boot nonce\n
%s::%s: no crashlogs found\n
%s::%s:     Second stage send image: %lld milliseconds\n
%s::%s: failed to initialize base class\n
%s::%s: payload too large\n
%s::%s: received oid %u, expected %u\n
%s::%s: failed to read boot flags\n
%s::%s:     subsystem 1: offset %llu, size %u\n
%s::%s: failed to initialize timestamps dictionary\n
%s::%s: successfully opened CCHI interface driver\n
%s::%s: failed to allocate image buffer\n
%s::%s: handing off memswap regions to control driver\n
%s::%s: failed to create nvram generator\n
%s::%s: failed to convert save dir\n
%s::%s: failed to create boot-args\n
%s::%s: removing %u bytes of existing beta data from firmware\n
%s::%s: failed: %s\n
%s::%s: failed to open interface object: 0x%08x\n
%s::%s: setting boot flags to 0x%x\n
%s::%s: overriding platform due to global-scale\n
%s::%s: failed to set host platform identifier\n
%s::%s: failed to write host platform sub-variant identifier\n
%s::%s: failed to get boot-args\n
%s::%s: Overriding platform to FPGA due to %s boot-arg\n
%s::%s: subCC wrong key type\n
%s::%s: opening CCHI interface driver\n
%s::%s: failed to read host platform identifier\n
%s::%s: global-scale not found\n
%s::%s: failed to insert RFEM into nvram overrides\n
%s::%s: failed to add beta tag\n
%s::%s: empty data class\n
%s::%s: property has wrong type %s\n
%s::%s: failed to get manager's parent: 0x%08x\n
%s::%s: failed to open control driver\n
%s::%s: unknown sikBlobType: %u\n
%s::%s: %s: '%s'\n
%s::%s: certification requested\n
%s::%s: failed to write doorbell\n
%s::%s: %s: string section too small in %s: %u bytes\n
%s::%s: failed to copy calibration data\n
%s::%s: failed to create dictionary\n
%s::%s: failed to load CoreCaptureDaemon framework\n
%s::%s: failed to allocate diagnostic object\n
%s::%s: failed to get RTKit firmware\n
%s::%s: failed to get tag for boot mode\n
%s::%s: failed to determine platform\n
%s::%s: failed to get firmware data\n
%s::%s: metadata at index %zu has wrong type\n
%s::%s: starting CoreCapture\n
%s::%s: failed to open transport driver for rom\n
%s::%s: invalid boot mode %d\n
%s::%s: opening boot driver for %s stage\n
%s::%s: failed to remove beta tag\n
%s::%s: device model ID property has wrong type %s\n
%s::%s: Client owns control driver: %s\n
%s::%s: global-scale has wrong length %zu\n
%s::%s: failed to extract chip id\n
%s::%s: failed to get size for subsystem 1 memswap section\n
%s::%s: %s: section version mismatch in %s: expected 0x%x, found 0x%x\n
%s::%s: %s: section too large in %s: offset %zu, section size %u, total size %zu\n
%s::%s: failed to insert WSKU into nvram overrides\n
%s::%s: failed to create regex: %s\n
%s::%s: proceeding to boot without any calibration data\n
%s::%s: failed to parse debug arguments\n
%s::%s: successfully generated identifiers (0x%08x, 0x%08x)\n
%s::%s: device model ID out of range: %lld\n
%s::%s: success\n
%s::%s: sending:\n
%s::%s: host platform sub-variant identifier read back (0x%08x) doesn't match host platform sub-variant identifier written (0x%08x)\n
%s::%s: no board parameters\n
%s::%s: unexpected size %zu\n
%s::%s: failed to create firmware object\n
%s::%s: save dir: %s\n
%s::%s: already open\n
%s::%s: removing %u bytes of existing alpha data from firmware\n
%s::%s: no calibration data found\n
%s::%s: Platform: %s\n
%s::%s: bad firmware size\n
%s::%s: image size %u -> %u\n
%s::%s: failed to map memory: 0x%08x\n
%s::%s: subsystem ID at index %zu has wrong type\n
%s::%s: manifest unique id: '%s'\n
%s::%s: CentauriUpdater Version: %s\n
%s::%s: failed to create secondary ftab\n
%s::%s: swapping endianness\n
%s::%s: failed to get host chip ID (%lld) or board ID (%lld)\n
%s::%s: successfully set boot flags to 0x%x\n
%s::%s: successfully created secondary ftab\n
%s::%s: successfully created updater\n
%s::%s: opening boot object\n
%s::%s: failed to read register %u (%u bytes): 0x%08x\n
%s::%s: opening control driver\n
%s::%s: control driver not open\n
%s::%s: successfully added an nvram file\n
%s::%s: failed to update calibration tag\n
%s::%s: no FDR calibration data found\n
%s::%s: successfully executed command %s\n
%s::%s: creating boot object\n
%s::%s: closing control driver\n
%s::%s: memswap sections in secondary ftab:\n
%s::%s: failed to create bootargs string\n
%s::%s: invalid byte at offset %u\n
%s::%s: failed to find manager service\n
%s::%s: skipping since second boot stage is disabled\n
%s::%s: response length mismatch: %hu != %u\n
%s::%s: failed to write host platform identifier\n
%s::%s: failed to get required file size from header\n
%s::%s: failed to copy WSKU\n
%s::%s: failed to remove alpha tag\n
%s::%s: %s firmware is incompatible with %s hardware\n
%s::%s: failed to create metadata key\n
%s::%s: added key: %s, value: %llu\n
%s::%s: failed to add nvram tag\n
%s::%s: creating updater\n
%s::%s: Boot mode: %s\n
%s::%s: different stage already open\n
%s::%s: failed to create chip class\n
%s::%s: %s: %s not found\n
%s::%s: %s: failed to get %s ptr\n
%s::%s: failed to copy nvram payload\n
%s::%s: replacing %u bytes of existing beta data in firmware\n
%s::%s: opening interface object\n
%s::%s: closing interface driver\n
%s::%s: failed to get offset for subsystem 0 memswap section\n
%s::%s: looking for calibration data, firmware %s FDR trust evaluation\n
%s::%s: thunderbolt path property has wrong type %s\n
%s::%s: failed to create command payload\n
%s::%s: failed to write: 0x%08x\n
%s::%s: failed to write register %u (%u bytes): 0x%08x\n
%s::%s: failed to send image on %s stage: 0x%08x: out code 0x%08x\n
%s::%s: %s: %s has wrong type\n
%s::%s: using existing nvram file as is\n
%s::%s: failed to compute manifest unique id\n
%s::%s: failed to get device model ID property\n
%s::%s: failed to create hello response\n
%s::%s: total size %u\n
%s::%s: failed to allocate secondary memory: 0x%08x\n
%s::%s: failed to determine whether Centauri is builtin\n
%s::%s: null updater\n
%s::%s: failed to allocate transport object\n
%s::%s: successfully opened control driver\n
%s::%s: %s: %s buffer too small: %zu bytes\n
%s::%s: failed to get Thunderbolt device info\n
%s::%s: thunderbolt, %s\n
%s::%s: image buffer is smaller than requested size (%u < %u)\n
%s::%s: bad parameter\n
%s::%s: failed to get size for subsystem 2 memswap section\n
%s::%s: no diagnostics path\n
%s::%s: failed to read host platform sub-variant identifier\n
%s::%s: failed to update nvram tag\n
%s::%s: failed to extract chip revision\n
%s::%s: initializing memswap\n
%s::%s: creating interface object\n
%s::%s: setting host platform identifiers to (0x%08x, 0x%08x)\n
%s::%s: failed to create matching dict\n
%s::%s: failed to validate calibration dict\n
%s::%s: Extend timeouts for SiK generation: %s\n
%s::%s: same stage already open\n
%s::%s: sending image\n
%s::%s: Defaulting to disable second boot stage for FPGA platform during restore\n
%s::%s: failed to get size for subsystem 0 memswap section\n
%s::%s: failed to create error\n
%s::%s: boot flags read back (0x%08x) don't match boot flags written (0x%08x)\n
%s::%s: returning cached values\n
%s::%s: generated a boot nonce\n
%s::%s: failed to reset chip: 0x%08x\n
%s::%s: amount read too large: %u\n
%s::%s: error status %u in response\n
%s::%s: failed to create string\n
%s::%s: failed to create updater\n
%s::%s: successfully opened boot driver for %s stage\n
%s::%s:     subsystem 2: offset %llu, size %u\n
%s::%s: no chip revision in bver\n
%s::%s: failed to find thunderbolt port's parent: 0x%08x\n
%s::%s: Destroying updater\n
%s::%s: failed to read doorbell\n
%s::%s: preparing to send an image\n
%s::%s: boot-args: \"%s\"\n
%s::%s: failed to convert subsystem ID at index %zu\n
%s::%s: %s: failed to create crashlog name\n
%s::%s: failed to copy RFEM\n
%s::%s: Centauri boot-args option has wrong type\n
%s::%s: builtin, host chip ID 0x%04x, host board ID 0x%04x\n
lowercaseString
length
mutableCopy
rangeAtIndex:
regularExpressionWithPattern:options:error:
substringWithRange:
boolValue
componentsSeparatedByString:
description
count
countByEnumeratingWithState:objects:count:
firstMatchInString:options:range:
isEqualToString:
numberOfRanges
objectAtIndexedSubscript:
containsString:
UTF8String
intValue
stringWithUTF8String:
```
