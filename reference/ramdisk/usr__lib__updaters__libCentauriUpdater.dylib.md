# `/usr/lib/updaters/libCentauriUpdater.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 402,240 bytes.

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
%s::%s: error converting host ECID\n
%s::%s: successfully created updater\n
%s::%s: interface driver closed\n
%s::%s: setting host platform identifiers to (0x%08x, 0x%08x)\n
%s::%s: failed to write host platform sub-variant identifier\n
%s::%s: handing off memswap regions to control driver\n
%s::%s:     ROM send image: %lld milliseconds\n
%s::%s: =========================\n
createEmpty
getThunderboltDeviceInfo
%s::%s: failed to instantiate CF object\n
%s::%s: updater is %s\n
%s::%s: Destroying updater\n
%s::%s: generated a boot nonce\n
different stage already open
failed to get offset for subsystem 1 memswap section
%s::%s: opening boot object\n
enabled
%s::%s:     subsystem 1: offset %llu, size %u\n
basic_string
manifest unique id too large
CentauriTransport
pushFirmware
%s
response length mismatch
 
failed to get size for subsystem 2 memswap section
%s::%s: replacing %u bytes of existing beta data in firmware\n
%s::%s: failed to create string\n
failed to copy sik public key
proxima
%s::%s: certification failed\n
%s::%s: failed to extract chip revision\n
%s::%s: thunderbolt path property has wrong type %s\n
%s::%s: failed to create secondary ftab\n
pingCheck
Wireless1,BoardID
Wireless1,Nonce
%s::%s: found FDR calibration data: %s\n
failed to get boot nonce hash
%s::%s: failed to get boot nonce\n
secondary ftab header has wrong type
%s::%s: successfully sent image: out code 0x%08x\n
%s::%s: failed to determine whether Centauri is builtin\n
%s::%s: failed to remove calibration tag\n
Wireless1,WifiRegData
Wireless1,CoexRealTimeArbiter
%s::%s: skipping since second boot stage is disabled\n
%s::%s: no response payload\n
%s::%s: successfully opened control driver\n
%s::%s: %s: section too large in %s: offset %zu, section size %u, total size %zu\n
gatherPreflightParameters
Wireless1,FirmwareDigestArray
Wireless1,PhyBlueTooth5G
%s::%s: failed to get thunderbolt port from path\n
failed to create command payload
failed to update calibration tag
copyCalibrationData
writeRegister
%s::%s: failed to allocate image buffer\n
failed to write host platform sub-variant identifier
%s::%s: machine-timeouts not found\n
failed to allocate secondary memory
%s::%s: %s: section too small in %s\n
cal-file-%u-%s.bin
%s::%s: failed to add alpha tag\n
failed to register class with CF
%s::%s: log collection disabled\n
%s::%s: unexpected response size %zu for GetSize, expected %zu\n
parseDeviceBootArgs
Custom Centauri boot-args:
Wireless1,WiFiOTPDatabase
centauri-builtin-protium
%s::%s: closing boot driver\n
oid mismatch
subCC null value
%s::%s: %s: %s invalid\n
failed to remove calibration tag
%s::%s: data class too large\n
%s::%s: failed to initialize restore object\n
%s::%s: failed to create boot-args\n
centauri-builtin
%s::%s:     ROM transport driver open: %lld milliseconds\n
%s::%s: preparing to send an image\n
%s::%s: Overriding platform to FPGA due to %s boot-arg\n
%s::%s: failed to convert subsystem ID at index %zu\n
%s::%s: giving up after %u failed attempts\n
Wireless1,Wifi2GLPhy
copySiKPublicKey
%s::%s: failed to determine platform\n
%s::%s:     Second stage transport driver open: %lld milliseconds\n
%s::%s: WSKU: '%s'\n
%s::%s: failed to load Centauri framework\n
Wireless1,WiFiRx
%s::%s: creating interface object\n
failed to copy WSKU
%s::%s: CentauriUpdater Version: %s\n
%s::%s: failed to create restore object\n
no response payload
%s::%s: failed to create mutable data\n
%s::%s: Boot mode: %s\n
failed to create response payload
%s::%s: replacing %u bytes of existing calibration data in firmware\n
%s::%s: error getting host chipID\n
%s::%s: checking if updater is done\n
failed to remove beta tag
failed to validate calibration dict
CentauriRestore
%s::%s: updater has wrong type\n
%s::%s: failed to create command payload\n
%s::%s: bad firmware size\n
%s::%s: failed to create matching dict\n
centauri-second-stage
%s::%s: failed to get manifest unique id\n
%s::%s: subCC wrong value type\n
boot flags read back mismatch
Control
%s::%s: failed to create key and/or value\n
normal
%s::%s: failed to copy nvram payload\n
supports
%s::%s: failed to get device model ID property\n
CentauriUpdaterExecCommand
failed to get tag for boot mode
%s::%s: interface driver not opened\n
%s::%s: response too small: %u\n
%s::%s: failed to write doorbell\n
image buffer is smaller than requested size
%s::%s: failed to create description\n
CoalescedSubTargetID
%s::%s: failed to initialize transport object\n
%s::%s:     CCHI stage transport driver open: %lld milliseconds\n
failed to open boot object for %s stage: 0x%08x
%s::%s: failed to get size for subsystem 2 memswap section\n
%s::%s: %s: %s crashlog size larger than buffer (%zu > %zu)\n
scrt
%s::%s: save dir: %s\n
Wireless1,BTRegData
%s::%s: error status %u in response\n
%s::%s: no metadata at index %zu\n
%s::%s: Firmware boot-args: '%s'\n
%s::%s: cannot boot in %s mode since %s image is missing from firmware\n
failed to map secondary memory
/usr/standalone/firmware/Centauri/
Wireless1,ACIBTLPEM
Wireless1,BTOTPDatabase
IOService
%s::%s: failed to get manager's parent: 0x%08x\n
%s::%s: failed to get host platform identifier\n
%s::%s: success: '%s'\n
%s::%s: hw.model: \"%s\"\n
%s::%s: stopping CoreCapture\n
Wireless1,PhyBluetooth5GTrim
%s::%s: failed to create updater\n
create
failed to get boot nonce
failed to write host platform identifier
alpha-patch-bay.bin
%s::%s: failed to remove alpha tag\n
UniqueChipID
isCentauriBuiltin_block_invoke
failed to send image on %s stage: 0x%08x: out code 0x%08x
failed to extract chip id
bad parameter
failed to add beta tag
CentauriUpdaterFinalize
Wireless1,ChipRev
%s::%s: same stage already open\n
%s::%s: opening interface object\n
%s::%s: failed to create subsystem id key\n
failed to get manifest unique id
~CentauriRestore
%s::%s: payload too large\n
fdr
failed to validate calibration data
%s::%s: failed to initialize logging\n
Wireless1,ProductionMode
%s::%s: secondary ftab header missing from primary ftab\n
%s::%s: memswap sections in secondary ftab:\n
low power
init
Wireless1,WiFiRxManuf
ccpu image missing
%s::%s: failed to initialize base class\n
%s::%s: failed to map memory: 0x%08x\n
parseCrashlogs
Wireless1,Wifi2GLMAC
failed to get RTKit firmware
payload too large
%s::%s: failed to allocate keys\n
collectLogs
CentauriUpdaterCopySiKPublicKey
%s::%s: closing control driver\n
%s::%s: failed to unmap memory: 0x%08x\n
failed to add calibration tag
%s::%s: %s not found\n
%s::%s: WSKU not found\n
%s::%s: failed to convert save dir\n
%s::%s: (0x%04x, 0x%04x) -> %hhu\n
failed to allocate transport object
%s::%s: failed to get boot nonce hash\n
interface driver not opened
%s::%s: invalid byte at offset %u\n
setCalibration
%s::%s: unexpected type %s\n
performCmd
readRegister
%s::%s: %s: string section too small in %s: %u bytes\n
%s::%s: failed to create error\n
%s::%s: unknown sikBlobType: %u\n
%s::%s: failed to write: 0x%08x\n
%s::%s: Defaulting to disable second boot stage for FPGA platform during restore\n
-
%s::%s: failed to add nvram tag\n
%s::%s: %s firmware is incompatible with %s hardware\n
%s::%s: failed to create dictionary\n
%s::%s: failed to execute command %s\n
failed to remove alpha tag
BootArgs
%s::%s: device model ID out of range: %lld\n
%s::%s: Firmware boot-args: <none>\n
%s::%s: failed to create hello response\n
%s::%s: failed to get hw.model\n
disabled
%s::%s: invalid subsystem ID %u at index %zu\n
%s::%s: failed to compute manifest unique id\n
%@ enable_sik=1
failed to create bootargs string
%s::%s: uninitialized updater\n
%s::%s: failed to create interface object\n
%s::%s: global-scale not found\n
%s::%s: global-scale has wrong length %zu\n
empty data class
openControlDriver
%s::%s: failed to create save path\n
copyWSKU
%s::%s: attempt %u of %u\n
%s::%s: failed to get board params\n
Wireless1,Wifi5GLMAC
%s::%s: amount read too large: %u\n
response too small
%s::%s: failed to read host platform identifier\n
%s::%s:     subsystem 0: offset %llu, size %u\n
%s::%s: empty data class\n
failed to get firmware data
host platform identifier read back mismatch
-restore
%s::%s: failed to set mem swap regions: 0x%08x\n
Crashlog.WFMAIN.bin
%s::%s: failed to convert device vendor ID to an integer\n
%s::%s: get crashlogs returned success but no crashlogs\n
amount read too large
gid mismatch
sendImage
%s::%s: failed to allocate secondary memory: 0x%08x\n
%s::%s: failed to add beta tag\n
%s::%s: subCC wrong key type\n
uninitialized updater
%s::%s: successfully executed command %s\n
openBootDriver
failed to allocate buffer
failed to write
%s::%s: received sequence num %u, expected %u\n
global-scale
%s::%s: failed to extract chip id\n
sendCCHICommand
%s::%s: info at index %zu has wrong type\n
Metadata
%s::%s: removing %u bytes of existing beta data from firmware\n
%s::%s: ignoring FDR calibration data if it exists\n
%s::%s: no raw calibration data provided\n
%s::%s: RFEM not found\n
%s::%s: failed to create domain\n
%s::%s: failed to create firmware object\n
initWithParameters
%s::%s: failed to read host platform sub-variant identifier\n
Wireless1,ScanBTLPEM
Wireless1,PhyBlueTooth5GManuf
v8@?0
%s::%s: successfully inserted calibration data into firmware\n
beta-patch-bay.bin
Wireless1,Wifi5GLPhyManuf
Wireless1,Wifi5GLPhyTrim
Wireless1,MinEpoch
failed to create hello response
failed to allocate diagnostic object
runCertification
%s::%s: successfully opened boot driver for %s stage\n
closeInterfaceDriver
generateBootNonce
%s::%s: image buffer is smaller than requested size (%u < %u)\n
%s::%s: control driver not open\n
%s::%s: failed to validate calibration dict\n
%s::%s: executing command %s\n
failed to get host platform identifier
failed to open interface object
failed to insert WSKU into nvram overrides
failed to update nvram tag
%s::%s: certification requested\n
done
%s::%s: total size %u\n
%s::%s: requesting offset %u, size %u\n
fpga
control driver not open
copyRFEM
Wireless1,PhyBlueTooth
CentauriUpdaterIsDone
<CentauriUpdater>{}
%s::%s: failed to create personalization parameters\n
%s::%s: closing interface driver\n
failed to update beta tag
%s::%s: manifest unique id: '%s'\n
%s::%s: failed to initialize base restore object\n
failed to initialize logging
Wireless1,SecurityMode
failed to read host platform sub-variant identifier
failed to get size for subsystem 1 memswap section
%s::%s: %s: failed to get %s ptr\n
%s::%s: device vendor ID out of range: %lld\n
CentauriUpdaterCreate
%s::%s: failed to open interface object: 0x%08x\n
WSKU
%s::%s: no chip revision in bver\n
certification failed
operator()
TigrisCreek
failed to create restore object
%s::%s: failed to open control driver\n
failed to create controller
%s::%s: failed to copy WSKU\n
secondary ftab header missing from primary ftab
%s::%s: boot driver not opened\n
%s::%s: failed to read boot flags\n
%s::%s: inserting %ld bytes of %s calibration data into firmware\n
%s::%s: creating updater\n
openInterfaceDriver
%s::%s: failed to remove beta tag\n
getManifestUniqueId_block_invoke
%s::%s: failed to allocate values\n
getSupportedChipRevision
Wireless1,PhyBlueToothManuf
%s::%s: failed to get thunderbolt path property\n
::
Wireless1,RestoreRTKitOS
vector
%s::%s: subCC null value\n
%s::%s: failed to register class with CF\n
not done yet
%s::%s: Extend timeouts for SiK generation: %s\n
%s::%s: failed to copy calibration data\n
%s::%s: builtin, host chip ID 0x%04x, host board ID 0x%04x\n
%s::%s: failed to open transport driver for rom\n
%s::%s: failed to copy RFEM\n
%s::%s: creating fresh nvram file with only overrides\n
failed to allocate data
cal-data-with-metadata.bin
ChipID
subCC null key
%s::%s: no diagnostics path\n
%s::%s: opening boot driver for %s stage\n
%s::%s: no subsystem ID at index %zu\n
silicon
%@/scratch
%s::%s: %s: %s crashlog header reports empty: %zu bytes\n
%s::%s: failed to update nvram tag\n
%s::%s: failed to create diagnostic filename\n
%s::%s: failed to read raw calibration data\n
%s::%s: failed to create chip class\n
%s::%s: failed to insert RFEM into nvram overrides\n
%s::%s: looking for calibration data, firmware %s FDR trust evaluation\n
CentauriUpdater
%s::%s: skipping reset for non-silicon platform\n
getPlatform
machine-timeouts
proxima-platform
%s::%s: no board parameters\n
%s::%s: null info at index %zu\n
Wireless1,RTKitOSLPEM
hw.model
simulator
Crashlog.BTMAIN.bin
%s::%s: removing %u bytes of existing calibration data from firmware\n
%s::%s: manifest unique id too large\n
%s::%s: no bver\n
Wireless1,ScanBluetooth
%s::%s: failed to get device vendor ID property\n
%s::%s: failed to set host platform identifier\n
%s::%s: failed to get size for subsystem 0 memswap section\n
%s::%s: failed to create update operations\n
Wireless1,CCPUApplicationFirmware
Wireless1,SecurityDomain
%s::%s: failed to get crashlogs: 0x%08x\n
%s::%s: === CentauriTransport Config ===\n
closeBootDriver
%s::%s: failed to allocate data\n
getPlatformIdentifiers
%s::%s: bootedQuery %s, generateNonce %s\n
%s::%s: Defaulting to disable second boot stage for simulator platform during restore - this is temporary\n
%s::%s: failed to update alpha tag\n
setControllerProperties
setBootFlags
%s::%s: parsing secondary ftab header in primary ftab\n
%s::%s: failed to create metadata key\n
%s::%s: %s: %s crashlog too small: %zu bytes\n
%s::%s: failed to generate boot nonce\n
%s::%s: received oid %u, expected %u\n
failed to read boot flags
failed to get required file size from header
Wireless1,ACIBTManuf
%s::%s: failed to initialize timestamps dictionary\n
%s::%s: creating empty nvram file\n
%s::%s: subCC null key\n
%s::%s: returning cached values\n
failed to write boot flags
%s::%s: successfully handed off memswap regions\n
nvram.bin
%s::%s: opening CCHI interface driver\n
%s::%s: successfully set boot flags to 0x%x\n
failed to create chip class
failed to allocate values
%s::%s: failed to find thunderbolt port's parent: 0x%08x\n
%s::%s: failed to allocate transport object\n
Wireless1,RestoreBootNonce
%s::%s: working dir: %s\n
null updater
error status in response
%s::%s: failed to create controller: 0x%08x\n
createSecondaryFtab
%s::%s: swapping endianness\n
%s::%s: failed to get firmware data\n
bad firmware size
%s::%s: failed to get offset for subsystem 0 memswap section\n
%s::%s:     subsystem 2: offset %llu, size %u\n
getManifestUniqueId
Wireless1,BTSecondary
%s::%s: failed to get tag for boot mode\n
getDebugInfo
%s::%s: %s: failed to create crashlog name\n
%s::%s
Wireless1,ACIWiFiTxManuf
%s::%s: failed to copy sik public key\n
No
%s::%s: merging nvram overrides with existing nvram file\n
%s::%s: found subCC index %zu: %s\n
%s::%s: failed to create regex: %s\n
%s::%s: failed to insert bootargs into nvram overrides\n
copySiKCertificateSigningRequest
%s::%s: Platform: %s\n
%s::%s: sending:\n
%s::%s: %s: %s empty\n
Thunderstrike
%s::%s: successfully set host platform identifiers to (0x%08x, 0x%08x)\n
=
unknown
failed to insert RFEM into nvram overrides
%s::%s: failed to create boot object for %s stage\n
handOffMemswapRegions
Device Vendor ID
%s::%s: Client owns control driver: %s\n
failed to read
%s::%s: timed out: doorbell value 0x%08x\n
failed to set mem swap regions
%s::%s: invalid value for %s debug arg\n
%s::%s: device vendor ID property has wrong type %s\n
failed to get ecid
%s::%s: opening control driver\n
%s::%s: failed to create nvram generator\n
%s::%s: Centauri boot-args option has wrong type\n
Wireless1,Wifi2GLMACManuf
%s::%s: failed to get size for subsystem 1 memswap section\n
%s::%s: success: %s\n
%s::%s: invalid boot mode %d\n
%s::%s: no diagnostics path, skipping CoreCapture initialization\n
%s::%s: failed to read register %u (%u bytes): 0x%08x\n
%s::%s: overriding platform due to global-scale\n
ROM
%s::%s: firmware intended for chip revision %s\n
Wireless1,ACIBT
isCentauriBuiltin
generic
Centauri
%s::%s: different stage already open\n
failed to create boot object
failed to create nvram generator
%s::%s: failed to validate calibration data\n
BoardId
%s::%s: creating boot object\n
kern.bootargs
%s::%s: metadata at index %zu has wrong type\n
%s::%s: failed to insert WSKU into nvram overrides\n
certificationVersion
Wireless1,Wifi5GLMACManuf
Yes
data class too large
Wireless1,Wifi5GLPhy
%s::%s: host chip ID (%lld) or board ID (%lld) out of range\n
%s::%s: wrong response size: expected %zu, received %zu\n
%s::%s: no crashlogs found\n
%s::%s: Timeouts:\n
%s::%s: failed to get offset for subsystem 2 memswap section\n
%s::%s: failed to add calibration tag\n
failed to allocate keys
%s::%s: failed to start CoreCapture\n
Wireless1,Wifi2GLPhyTrim
failed to get offset for subsystem 0 memswap section
%s::%s: %s: %s buffer too small: %zu bytes\n
AppleCentauriManager
%s::%s: failed to allocate diagnostic object\n
%s::%s: booting in %s mode\n
%s::%s: failed to hand off memswap regions\n
sendBootTimestamps
failed to create interface object
%s::%s: failed to write host platform identifier\n
%s::%s: requesting buffer of size %u\n
remote
%s::%s: failed to get chip information\n
%s::%s: initializing memswap\n
%s::%s: failed to reset chip: 0x%08x\n
%s::%s: failed: %s\n
%s::%s: successfully opened CCHI interface driver\n
%s::%s: allocated image buffer of size %u\n
secondary boot
Crashlog.CTRL.bin
boot driver not opened
%s::%s: sending image\n
%s::%s: error converting host chipID\n
%s::%s: no calibration data found\n
Wireless1,Wifi2GLPhyManuf
%s::%s: thunderbolt, %s\n
%s::%s: received:\n
sim
failed to add to nvram generator
%s::%s: removing %u bytes of existing alpha data from firmware\n
BWC3
RFEM:
%s::%s: failed to create working dir\n
%s::%s: device model ID property has wrong type %s\n
%s::%s: secondary ftab header has wrong type\n
%s::%s: CSR unavailable\n
sequence number mismatch
Device Model ID
%s::%s: image size %u -> %u\n
failed to read host platform identifier
%s::%s: failed to get offset for subsystem 1 memswap section\n
failed to create dictionary
Wireless1,ACIWIFI
RestoreFailure
setHostPlatformIdentifiers
closeControlDriver
%s::%s: added key: %s, value: %llu\n
%s::%s: successfully added an nvram file\n
setPatchBay
%s::%s: failed to create transport object\n
Wireless1,ScanWifi
getBoardParameters
SubsystemID
Wireless1,Ticket
%s::%s: failed to find manager service\n
Thunderbolt Path
CentauriPlatform
Wireless1,ECID
%s::%s: boot flags read back (0x%08x) don't match boot flags written (0x%08x)\n
%s::%s: failed to add %s\n
%s::%s: proceeding to boot without any calibration data\n
subCC wrong value type
failed to get board params
Wireless1,WiFiTx
failed to create diagnostic filename
%s::%s: null updater\n
failed to get domain/mode
%s::%s: failed to collect logs: 0x%08x\n
%s::%s: failed to create bootargs string\n
%s::%s: failed to update beta tag\n
%s::%s: property has wrong type %s\n
%s::%s: failed to read doorbell\n
%s::%s: success\n
%s::%s: error getting host ECID\n
chip_revision_([a-zA-Z][0-9])
Wireless1,WiFiTxManuf
failed to get image buffer address
map::at:  key not found
wifi-rfem-info
%s::%s: unexpected size %zu\n
%s::%s: failed to get RTKit firmware\n
%s::%s: failed to allocate buffer\n
%s::%s: setting boot flags to 0x%x\n
%s::%s: host platform sub-variant identifier read back (0x%08x) doesn't match host platform sub-variant identifier written (0x%08x)\n
%s::%s: failed to get required file size from header\n
%s::%s: %s: %s has wrong type\n
setBootTimestamp
createError
failed to copy nvram payload
failed to copy RFEM
%s::%s: failed to get host chip ID (%lld) or board ID (%lld)\n
%s::%s: failed to read: 0x%08x\n
%s::%s: failed to write register %u (%u bytes): 0x%08x\n
%s::%s: successfully created secondary ftab\n
CentauriFirmware
raw
%s::%s: unsupported version %u\n
%s::%s: Enable log collection: %s\n
no board parameters
failed to get size for subsystem 0 memswap section
%s::%s: successfully merged nvram overrides with existing nvram file\n
%s::%s: failed to find service\n
Wireless1,ScanBTManuf
Wireless1,BTSecondaryManuf
%s::%s:     Second stage send image: %lld milliseconds\n
%s::%s: response length mismatch: %hu != %u\n
setNVRAM
%s::%s: no FDR calibration data found\n
enable_sik=1
Wireless1,ScanWifiManuf
%s::%s: \n
%s::%s: bad parameter\n
subCC wrong key type
%s::%s: found raw calibration data: index %zu\n
centauri
startCoreCapture
%s::%s: failed to send image on %s stage: 0x%08x: out code 0x%08x\n
%s::%s: host platform identifier read back (0x%08x) doesn't match host platform identifier written (0x%08x)\n
host platform sub-variant identifier read back mismatch
%s::%s: received gid %u, expected %u\n
%s::%s: failed to get image buffer address\n
%s::%s: using existing nvram file as is\n
%s::%s: failed to get ecid\n
failed to get chip information
%s::%s: Enable second boot stage: %s\n
%s::%s: %s: '%s'\n
Wireless1,PhyBlueToothLPM
reset
%s::%s: subsystem ID at index %zu has wrong type\n
%s::%s: successfully generated identifiers (0x%08x, 0x%08x)\n
%s::%s: already open\n
failed to update alpha tag
does not support
%s::%s: failed to parse debug arguments\n
%s::%s: failed to create response payload\n
%s::%s: %s: section version mismatch in %s: expected 0x%x, found 0x%x\n
Wireless1,RTKitOS
%s::%s: unexpected response size %zu\n
%s::%s: failed to write boot flags\n
%s::%s: failed to add to nvram generator\n
%s::%s: failed to update calibration tag\n
failed to add alpha tag
%s::%s: failed to load CoreCaptureDaemon framework\n
Wireless1,PhyBluetoothTrim
Wireless1,ChipID
%s::%s: boot driver closed\n
%s::%s: wrong firmware type\n
%s::%s: failed to convert device model ID to an integer\n
%s::%s: failed to open interface driver\n
%s::%s: failed: 0x%08x\n
%s::%s: failed to open boot object for %s stage: 0x%08x\n
failed to allocate image buffer
%s::%s: replacing %u bytes of existing alpha data in firmware\n
queryCmd
%s::%s: failed to convert working dir\n
CentauriCommon
WiFi
getThunderboltIdentifier
%s::%s: Overriding second boot stage to %s due to %s boot-arg\n
failed to determine whether Centauri is builtin
failed to read raw calibration data
%s::%s: already preflighted, removing nonce\n
%s::%s: failed to get Thunderbolt device info\n
failed to instantiate CF object
updater has wrong type
v20@?0i8r*12
failed to get offset for subsystem 2 memswap section
skipReset
failed to create personalization parameters
%s::%s: boot-args: \"%s\"\n
BT
secondary lpm boot
failed to add nvram tag
isChipRevisionSupported
%s::%s: ignoring empty WSKU\n
%s::%s: failed to get domain/mode\n
%s::%s: bver: '%s'\n
%s::%s: starting CoreCapture\n
%s::%s: global-scale has wrong type\n
%s::%s: failed to get boot-args\n
%s::%s: %s: %s not found\n
%s::%s: failed to remove alpha tag\n
%s::%s: found FDR calibration data: %s\n
%s::%s: ignoring FDR calibration data if it exists\n
%s::%s: failed to get boot nonce hash\n
%s::%s: failed to determine platform\n
%s::%s: =========================\n
%s::%s: host platform sub-variant identifier read back (0x%08x) doesn't match host platform sub-variant identifier written (0x%08x)\n
%s::%s: added key: %s, value: %llu\n
%s::%s: failed to insert RFEM into nvram overrides\n
%s::%s: failed to get manifest unique id\n
%s::%s: found subCC index %zu: %s\n
%s::%s: failed to instantiate CF object\n
%s::%s: failed to read doorbell\n
%s::%s:     subsystem 2: offset %llu, size %u\n
%s::%s: %s not found\n
%s::%s: found raw calibration data: index %zu\n
%s::%s: no diagnostics path\n
%s::%s: device vendor ID out of range: %lld\n
%s::%s: failed to execute command %s\n
%s::%s: invalid boot mode %d\n
%s::%s: setting boot flags to 0x%x\n
%s::%s: successfully handed off memswap regions\n
%s::%s: successfully added an nvram file\n
%s::%s: certification failed\n
%s::%s: failed to start CoreCapture\n
%s::%s: failed to initialize logging\n
%s::%s: no board parameters\n
%s::%s: %s: %s buffer too small: %zu bytes\n
%s::%s: failed to add alpha tag\n
%s::%s: failed to get image buffer address\n
%s::%s: failed to allocate keys\n
%s::%s: CentauriUpdater Version: %s\n
%s::%s: failed: 0x%08x\n
%s::%s: creating interface object\n
%s::%s: %s: %s has wrong type\n
%s::%s: %s: %s empty\n
%s::%s: replacing %u bytes of existing beta data in firmware\n
%s::%s: secondary ftab header missing from primary ftab\n
%s::%s: no crashlogs found\n
%s::%s: get crashlogs returned success but no crashlogs\n
%s::%s: unknown sikBlobType: %u\n
%s::%s: successfully sent image: out code 0x%08x\n
%s::%s: global-scale has wrong length %zu\n
%s::%s: failed to determine whether Centauri is builtin\n
%s::%s: replacing %u bytes of existing alpha data in firmware\n
%s::%s: sending image\n
%s::%s: requesting buffer of size %u\n
%s::%s: failed to allocate secondary memory: 0x%08x\n
%s::%s: %s: failed to get %s ptr\n
%s::%s: data class too large\n
%s::%s: failed to create dictionary\n
%s::%s: failed to create error\n
%s::%s: failed to get host chip ID (%lld) or board ID (%lld)\n
%s::%s: failed to create boot object for %s stage\n
%s::%s: failed to write host platform sub-variant identifier\n
%s::%s: control driver not open\n
%s::%s: wrong firmware type\n
%s::%s: thunderbolt, %s\n
%s::%s: failed to get device model ID property\n
%s::%s: skipping since second boot stage is disabled\n
%s::%s: already open\n
%s::%s: global-scale has wrong type\n
%s::%s: opening control driver\n
%s::%s: failed to copy nvram payload\n
%s::%s: failed to allocate data\n
%s::%s: failed to create description\n
%s::%s: device model ID out of range: %lld\n
%s::%s: cannot boot in %s mode since %s image is missing from firmware\n
%s::%s:     ROM transport driver open: %lld milliseconds\n
%s::%s: boot driver closed\n
%s::%s: image size %u -> %u\n
%s::%s: failed to create boot-args\n
%s::%s: successfully created updater\n
%s::%s: successfully opened CCHI interface driver\n
%s::%s: machine-timeouts not found\n
%s::%s: bad parameter\n
%s::%s: failed to find manager service\n
%s::%s: failed to get manager's parent: 0x%08x\n
%s::%s: failed to create personalization parameters\n
%s::%s: failed to create secondary ftab\n
%s::%s: payload too large\n
%s::%s: sending:\n
%s::%s: received gid %u, expected %u\n
%s::%s: null info at index %zu\n
%s::%s: %s: section too small in %s\n
%s::%s: (0x%04x, 0x%04x) -> %hhu\n
%s::%s: booting in %s mode\n
%s::%s: failed to allocate buffer\n
%s::%s: memswap sections in secondary ftab:\n
%s::%s: failed to create subsystem id key\n
%s::%s: removing %u bytes of existing beta data from firmware\n
%s::%s: starting CoreCapture\n
%s::%s: failed to create metadata key\n
%s::%s: failed to find thunderbolt port's parent: 0x%08x\n
%s::%s: creating boot object\n
%s::%s: response too small: %u\n
%s::%s: successfully set host platform identifiers to (0x%08x, 0x%08x)\n
%s::%s: bootedQuery %s, generateNonce %s\n
%s::%s: failed to get domain/mode\n
%s::%s: success\n
%s::%s:     Second stage send image: %lld milliseconds\n
%s::%s: opening CCHI interface driver\n
%s::%s: amount read too large: %u\n
%s::%s: inserting %ld bytes of %s calibration data into firmware\n
%s::%s: property has wrong type %s\n
%s::%s: global-scale not found\n
%s::%s: creating updater\n
%s::%s: failed to open interface object: 0x%08x\n
%s::%s: interface driver closed\n
%s::%s: received:\n
%s::%s: error status %u in response\n
%s::%s: failed to read host platform identifier\n
%s::%s: unsupported version %u\n
%s::%s: closing boot driver\n
%s::%s: opening interface object\n
%s::%s: failed to read host platform sub-variant identifier\n
%s::%s: attempt %u of %u\n
%s::%s: host chip ID (%lld) or board ID (%lld) out of range\n
%s::%s: === CentauriTransport Config ===\n
%s::%s: Platform: %s\n
%s::%s: failed to read boot flags\n
%s::%s: failed to extract chip id\n
%s::%s: failed to get required file size from header\n
%s::%s: failed to create regex: %s\n
%s::%s: no diagnostics path, skipping CoreCapture initialization\n
%s::%s: device model ID property has wrong type %s\n
%s::%s: failed to get boot nonce\n
%s::%s: failed to get host platform identifier\n
%s::%s: failed to hand off memswap regions\n
%s::%s: interface driver not opened\n
%s::%s: %s firmware is incompatible with %s hardware\n
%s::%s: swapping endianness\n
%s::%s: failed to initialize restore object\n
%s::%s: failed to convert save dir\n
%s::%s: boot flags read back (0x%08x) don't match boot flags written (0x%08x)\n
%s::%s: failed to create nvram generator\n
%s::%s: error getting host chipID\n
%s::%s: unexpected type %s\n
%s::%s: failed to extract chip revision\n
%s::%s: failed to open interface driver\n
%s::%s: Client owns control driver: %s\n
%s::%s: hw.model: \"%s\"\n
%s::%s: failed to add beta tag\n
%s::%s: device vendor ID property has wrong type %s\n
%s::%s: failed to open transport driver for rom\n
%s::%s: failed to collect logs: 0x%08x\n
%s::%s: failed to create controller: 0x%08x\n
%s::%s: manifest unique id too large\n
%s::%s: failed to find service\n
%s::%s: giving up after %u failed attempts\n
%s::%s: returning cached values\n
%s::%s: unexpected response size %zu\n
%s::%s: failed to create interface object\n
%s::%s: subsystem ID at index %zu has wrong type\n
%s::%s: bver: '%s'\n
%s::%s: failed to create firmware object\n
%s::%s: successfully executed command %s\n
%s::%s: failed to allocate transport object\n
%s::%s:     CCHI stage transport driver open: %lld milliseconds\n
%s::%s: failed to write register %u (%u bytes): 0x%08x\n
%s::%s: successfully opened control driver\n
%s::%s: certification requested\n
%s::%s: failed: %s\n
%s::%s: failed to read register %u (%u bytes): 0x%08x\n
%s::%s: failed to get firmware data\n
%s::%s: Extend timeouts for SiK generation: %s\n
%s::%s: closing control driver\n
%s::%s: metadata at index %zu has wrong type\n
%s::%s: error converting host chipID\n
%s::%s: failed to create command payload\n
%s::%s: no response payload\n
%s::%s: bad firmware size\n
%s::%s: working dir: %s\n
%s::%s: builtin, host chip ID 0x%04x, host board ID 0x%04x\n
%s::%s: failed to initialize timestamps dictionary\n
%s::%s: allocated image buffer of size %u\n
%s::%s: subCC wrong key type\n
%s::%s: Centauri boot-args option has wrong type\n
%s::%s: failed to get board params\n
%s::%s: failed to load CoreCaptureDaemon framework\n
%s::%s: CSR unavailable\n
%s::%s: different stage already open\n
%s::%s: failed to add calibration tag\n
%s::%s: %s: section too large in %s: offset %zu, section size %u, total size %zu\n
%s::%s: failed to create diagnostic filename\n
%s::%s: no FDR calibration data found\n
%s::%s: failed to insert bootargs into nvram overrides\n
%s::%s: failed to create domain\n
%s::%s: null updater\n
%s::%s: opening boot driver for %s stage\n
%s::%s: failed to create response payload\n
%s::%s: failed to update nvram tag\n
%s::%s: no raw calibration data provided\n
%s::%s: failed to convert working dir\n
%s::%s: Destroying updater\n
%s::%s: failed to generate boot nonce\n
%s::%s: proceeding to boot without any calibration data\n
%s::%s: unexpected size %zu\n
%s::%s: failed to get offset for subsystem 0 memswap section\n
%s::%s: failed to get offset for subsystem 2 memswap section\n
%s::%s: failed to read raw calibration data\n
%s::%s: WSKU not found\n
%s::%s: success: '%s'\n
%s::%s: success: %s\n
%s::%s: successfully opened boot driver for %s stage\n
%s::%s: failed to write host platform identifier\n
%s::%s: Boot mode: %s\n
%s::%s: same stage already open\n
%s::%s: Overriding platform to FPGA due to %s boot-arg\n
%s::%s: ignoring empty WSKU\n
%s::%s: stopping CoreCapture\n
%s::%s: image buffer is smaller than requested size (%u < %u)\n
%s::%s: failed to remove beta tag\n
%s::%s: failed to copy sik public key\n
%s::%s: failed to get RTKit firmware\n
%s::%s: opening boot object\n
%s::%s: failed to set mem swap regions: 0x%08x\n
%s::%s: failed to copy RFEM\n
%s::%s: failed to validate calibration dict\n
%s::%s: no calibration data found\n
%s::%s: failed to get Thunderbolt device info\n
%s::%s: updater is %s\n
%s::%s: failed to set host platform identifier\n
%s::%s: Timeouts:\n
%s::%s: received sequence num %u, expected %u\n
%s::%s: preparing to send an image\n
%s::%s: failed to get hw.model\n
%s::%s: failed to create matching dict\n
%s::%s: %s: %s crashlog header reports empty: %zu bytes\n
%s::%s: failed to create key and/or value\n
%s::%s: merging nvram overrides with existing nvram file\n
%s::%s: successfully merged nvram overrides with existing nvram file\n
%s::%s: using existing nvram file as is\n
%s::%s: creating empty nvram file\n
%s::%s: creating fresh nvram file with only overrides\n
%s::%s: failed to add nvram tag\n
%s::%s: replacing %u bytes of existing calibration data in firmware\n
%s::%s: \n
%s::%s: failed to get crashlogs: 0x%08x\n
%s::%s:     subsystem 0: offset %llu, size %u\n
%s::%s: removing %u bytes of existing calibration data from firmware\n
%s::%s: failed to compute manifest unique id\n
%s::%s: failed to initialize base restore object\n
%s::%s: invalid value for %s debug arg\n
%s::%s: host platform identifier read back (0x%08x) doesn't match host platform identifier written (0x%08x)\n
%s::%s: Defaulting to disable second boot stage for FPGA platform during restore\n
%s::%s: failed to create chip class\n
%s::%s:     subsystem 1: offset %llu, size %u\n
%s::%s: failed to copy WSKU\n
%s::%s: removing %u bytes of existing alpha data from firmware\n
%s::%s: no bver\n
%s::%s: failed to create transport object\n
%s::%s: wrong response size: expected %zu, received %zu\n
%s::%s: initializing memswap\n
%s::%s: failed to initialize base class\n
%s::%s: %s: %s invalid\n
%s::%s: %s: '%s'\n
%s::%s: failed to update alpha tag\n
%s::%s: subCC null key\n
%s::%s: failed to convert device vendor ID to an integer\n
%s::%s: failed to send image on %s stage: 0x%08x: out code 0x%08x\n
%s::%s: %s: section version mismatch in %s: expected 0x%x, found 0x%x\n
%s::%s: successfully generated identifiers (0x%08x, 0x%08x)\n
%s::%s: failed to get thunderbolt port from path\n
%s::%s: skipping reset for non-silicon platform\n
%s::%s: timed out: doorbell value 0x%08x\n
%s::%s: failed to get thunderbolt path property\n
%s::%s: failed to get size for subsystem 2 memswap section\n
%s::%s: %s: %s not found\n
%s::%s: failed to update calibration tag\n
%s::%s: empty data class\n
%s::%s: failed to allocate values\n
%s::%s: already preflighted, removing nonce\n
%s::%s: failed to get size for subsystem 1 memswap section\n
%s::%s: failed to create save path\n
%s::%s: uninitialized updater\n
%s::%s: received oid %u, expected %u\n
%s::%s: invalid byte at offset %u\n
%s::%s: failed to parse debug arguments\n
%s::%s: failed to get device vendor ID property\n
%s::%s: failed to convert device model ID to an integer\n
%s::%s: failed to write boot flags\n
%s::%s: successfully set boot flags to 0x%x\n
%s::%s: %s: string section too small in %s: %u bytes\n
%s::%s: Firmware boot-args: <none>\n
%s::%s: manifest unique id: '%s'\n
%s::%s: closing interface driver\n
%s::%s: setting host platform identifiers to (0x%08x, 0x%08x)\n
%s::%s: Overriding second boot stage to %s due to %s boot-arg\n
%s::%s: failed to get offset for subsystem 1 memswap section\n
%s::%s: failed to create bootargs string\n
%s::%s: failed to create string\n
%s::%s: failed to create restore object\n
%s::%s: generated a boot nonce\n
%s::%s:     ROM send image: %lld milliseconds\n
%s::%s: boot-args: \"%s\"\n
%s::%s: %s: failed to create crashlog name\n
%s::%s: successfully inserted calibration data into firmware\n
%s::%s: %s\n%@
%s::%s: no chip revision in bver\n
%s::%s: failed to reset chip: 0x%08x\n
%s::%s: failed to get boot-args\n
%s::%s: failed to add to nvram generator\n
%s::%s: failed to create update operations\n
%s::%s: failed to load Centauri framework\n
%s::%s: thunderbolt path property has wrong type %s\n
%s::%s: failed to create updater\n
%s::%s: parsing secondary ftab header in primary ftab\n
%s::%s: failed to insert WSKU into nvram overrides\n
%s::%s: WSKU: '%s'\n
%s::%s: failed to create working dir\n
%s::%s: checking if updater is done\n
%s::%s: failed to get chip information\n
%s::%s: Enable log collection: %s\n
%s::%s: failed to unmap memory: 0x%08x\n
%s::%s: no metadata at index %zu\n
%s::%s: invalid subsystem ID %u at index %zu\n
%s::%s: error converting host ECID\n
%s::%s: total size %u\n
%s::%s: overriding platform due to global-scale\n
%s::%s: failed to get size for subsystem 0 memswap section\n
%s::%s: failed to copy calibration data\n
%s::%s: failed to open boot object for %s stage: 0x%08x\n
%s::%s: failed to allocate image buffer\n
%s::%s: handing off memswap regions to control driver\n
%s::%s: error getting host ECID\n
%s::%s: save dir: %s\n
%s::%s: failed to register class with CF\n
%s::%s: failed to initialize transport object\n
%s::%s: requesting offset %u, size %u\n
%s::%s: Defaulting to disable second boot stage for simulator platform during restore - this is temporary\n
%s::%s: %s: %s crashlog too small: %zu bytes\n
%s::%s: Firmware boot-args: '%s'\n
%s::%s: failed to remove calibration tag\n
%s::%s: looking for calibration data, firmware %s FDR trust evaluation\n
%s::%s: failed to get tag for boot mode\n
%s::%s: failed to open control driver\n
%s::%s: subCC null value\n
%s::%s: subCC wrong value type\n
%s::%s: firmware intended for chip revision %s\n
%s::%s: failed to allocate diagnostic object\n
%s::%s: unexpected response size %zu for GetSize, expected %zu\n
%s::%s: response length mismatch: %hu != %u\n
%s::%s: boot driver not opened\n
%s::%s: failed to update beta tag\n
%s::%s: updater has wrong type\n
%s::%s:     Second stage transport driver open: %lld milliseconds\n
%s::%s: failed to write: 0x%08x\n
%s::%s: failed to read: 0x%08x\n
%s::%s: successfully created secondary ftab\n
%s::%s: failed to convert subsystem ID at index %zu\n
%s::%s: failed to validate calibration data\n
%s::%s: RFEM not found\n
%s::%s: executing command %s\n
%s::%s: failed to get ecid\n
%s::%s: failed to create hello response\n
%s::%s: log collection disabled\n
%s::%s: failed to create mutable data\n
%s::%s: failed to write doorbell\n
%s::%s: info at index %zu has wrong type\n
%s::%s: %s: %s crashlog size larger than buffer (%zu > %zu)\n
%s::%s: secondary ftab header has wrong type\n
%s::%s: Enable second boot stage: %s\n
%s::%s: failed to map memory: 0x%08x\n
%s::%s: no subsystem ID at index %zu\n
%s::%s: failed to add %s\n
UTF8String
countByEnumeratingWithState:objects:count:
length
numberOfRanges
substringWithRange:
containsString:
description
intValue
stringWithUTF8String:
boolValue
componentsSeparatedByString:
count
isEqualToString:
objectAtIndexedSubscript:
rangeAtIndex:
regularExpressionWithPattern:options:error:
lowercaseString
firstMatchInString:options:range:
mutableCopy
```
