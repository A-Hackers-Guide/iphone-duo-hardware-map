# `/usr/lib/updaters/libAppleTCONUpdater.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 122,592 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 2304)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/usr/lib/updaters/libAppleTCONUpdater.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libPCDSUpdater.dylib (compatibility version 1.0.0, current version 70.0.0, weak)`
- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (243)

```
start update failed
AppleTCONDP835Device::eventCmdPerformNextStage: failure %s\n
Baobab2,ManifestEpoch
RestoreInternal
v8@?0
PLS_Config
displayECID: Avoid buffer overflow %d\n
Error code 0x%02x!\n
failed to write
Baobab,Life
CDIC_Setting
bundle ver: num: invalid
tcon-path
chipid
Baobab2,BoardID
setSdom: update failed:0x%x phase:%u\n
Baobab,BoardID
Baobab2,SecurityDomain
nonce
PMIC_Config
AppleTCONUpdateController::execCommand: device failure %d\n
AppleTCONUpdateController::execCommand: Entering execCommand: command = %s\n
failed to update pcds component
getLifeCycle failed
AppleTCONUpdateController::execCmdQueryInfo: create output dict: failed\n
bundle extent ver < current extent ver
writeDeviceEEPROM failed
AppleTCONDP835Device::readFWPointer: activeFWPointer:0x%08x inactiveFWPointer:0x%08x\n
Baobab,BacklightController
getLifeCycle %s\n
alloc: failed
Fuse Prod (%d:%d)\n
device-id
AppleTCONUpdaterExecCommand - execCommand error
comp: string create failed
performNextStage
chipID alloc failed
firmware missing
failed to read bundle version after update
bundle version after update differs from update bundle version
VCOM_Config
SDOM status %s\n
Dev:CmdQueryInfo failure %s\n
AppleTCONDP835Device::isFWComponentsUpdateRequired: %s update to 0x%02x:0x%02x:0x%02x\n
conversion error
AppleTCONUpdateController::start: Dev = (%p) - updateSupported = %d\n
AppleTCONUpdateController::execCmdQueryInfo: Begin Personalization\n
Failed to get eepromRef handle\n
FirmwareData
bundle payload type invalid
AppleTCONDP835Device::eventCmdPerformNextStage: update done\n
out of range
lcd-eeprom
comp: data missing
AppleTCONDP835Device::writeFWPointer: fWPointer:0x%08x\n
re alloc failed
submit dev:id failed
AppleTCONUpdateController::execCmdQueryInfo: device failure %d\n
nvm_image
TCON_Config
FW component update :%s\n
Timeout Error status 0x%02x\n
Failed to find AppleTCONControl service\n
PCDS must be generated and programmed before FW update can occur
SkipSameVersion
bundle-ver
%@: %s
Baobab,ProductionMode
Baobab2,Cabal
Baobab2,Trinity
AppleTCONUpdaterCreate
Unable to allocate memory
update fw error:%s\n
erase eeprom error (0x%08x): %s\n
bundle extent ver <= current extent ver
eraseDeviceEEPROM failed
firmware-ver
sdom-status
PROD status %s\n
failed to erase personalization manifest from EEPROM
AppleTCONDP835Device::eventCmdPerformNextStage: didUpdate=%u personalize=%u updateDone=%u\n
download comp: failed
tcon device not found
getHWCID failed
@Baobab2,Ticket
Baobab2,ECID
FCBIST_Config
FW Update Options I:%d S:%d\n
nvm ver string create failed
AppleTCONDP835Device::isFWComponentsUpdateRequired: internal:%u skipSameVersion:%u\n
end update failed
@Baobab,Ticket
AppleTCONRestoreLib Version %d.%d\n
Could not read error code\n
IODeviceTree:/
Failed to get SDOM status\n
firmware dict: create failed
%s [error]: %s\n
Failed to getIORegRootNode. Will Attempt fallback.\n
AppleTCONUpdaterErrorDomain
Version
AppleTCONUpdateController::execCommand: Unsupported command: %s\n
Baobab2,Provisioning
1.firmware.Payload
Options
OTP_STATUS_PROGRAMMED
Baobab,Cabal
%02x
Baobab2,ProductionMode
AppleTCONUpdaterCreate - AppleTCONUpdateController start error\n
AppleTCONUpdateController::execCmdQueryInfo: Output param missing\n
Dev:deviceid %s\n
AppleTCONDP835Device::writeAndVerifyFWPointer: fWPointer:0x%08x\n
Baobab,TCON
AppleTCONUpdaterExecCommand - no AppleTCON controller instance
Failed to get Prod value\n
AppleTconDev(v2):(%d:%d:%d:%d:0x%02x:0x%02x(0x%04x))\n
SDOM not fused; see rdar://84123825 for instructions
product not found
Unexpected boot status: 0x%02x\n
Baobab,Ticket
<libAppleTCONUpdater %p [%p]>{}
setSdom: update failed:0x%x phase:%d\n
fw dict create failed
enforce-pcds-valid
RestoreOptions not a dict?
invalid length
Baobab2,Ticket
Baobab2,Nonce
product path not found
Fuse SDOM (%d:%d)\n
EDID
Baobab,SecurityDomain
getNonce failed
device_id
download fw failed
Baobab,UpdateNonce
Component Download Failed:Block:%d:length:%d!\n
Reset option %d\n
nonce alloc failed
Update to 0x%02x:0x%02x\n
AppleTCONDP855Device::eventCmdPerformNextStage: Finished Personalization\n
setProd: update failed:0x%x phase:%d\n
NVM_IMAGE
OTP_STATUS_UNPROGRAMMED
failed
Dev:CmdQueryInfo SDOM not fused. No Fusing option. Bailing.\n
Dev:next stage failure %s\n
Failed to get bundle version\n
enforce-pcds-valid=0
Baobab,Provisioning
Baobab2,UpdateNonce
Invalid string
Payload
AppleTCONDP835Device::eventCmdPerformNextStage: failure: attempt to revert FW pointer %s\n
Options.%@
Baobab2,TCON
ecid
bundle version type invalid
AppleTCONUpdateController::execCommand: Exiting execCommand: command = %s, result = 0x%X\n
ecid alloc failed
%u.%s.%s
succeeded
failed to update fw component
FuseSDOM
invalid data pointer
ticket missing
expected bundle version: 0x%02x:0x%02x:0x%02x, actual bundle version: 0x%02x:0x%02x:0x%02x\n
FW_Config
IOReg (%s) error: %s\n
bundle minor ver < current minor ver
prod-status
failed to erase
otp update failed
%s
Failed to get Prod status\n
failed to read PCDS 0 top-level header
%u.%s.Payload
AppleTCONUpdaterIsDone
tcon-registers
AppleTCONUpdaterCreate - failed to create AppleTCONUpdater
AppleTconDev:ECID: 0x%s\n
product path type mismatch
AppleTCONUpdateControllerGetDevice failed: %s\n
comp: key create failed
AppleTCONUpdaterExecCommand
memory alloc failed
queryInfo
Failed to get memoryRef handle\n
boardID alloc failed
Baobab2,BacklightController
prod-fuse-value
AppleTCONUpdaterCreate - failed to register kLibAppleTCONUpdaterClass
Failed to get Firmware version\n
Looking for entry under %s\n
Performing
failed to read PCDS 1 top-level header
updates failed
Baobab,ChipID
Baobab,ECID
LUTS_Config
PGAMMA_Config
get dev:id failed
getECID failed
failed to write personalization manifest to EEPROM
update fw component error:%s\n
setProd: update (getDeviceStatus) error:0x%x\n
IODeviceTree:/product
Failed to get boot status\n
AppleTCONDP835Device::eventCmdQueryInfo: boardID=0x%08x HWCID=0x%08x personalize=%u\n
Baobab,Nonce
Download comp:0x%04x NumBlocks:%d\n
write eeprom error (0x%08x): %s\n
kern.bootargs
libAppleTCONUpdater
EQ_Setting_Config
bundle major ver < current major ver
setSdom: update (getDeviceStatus) error:0x%x\n
AppleTCONDP835Device::updateFWComponent: component=0x%02x, componentDataLength=0x%08x\n
AppleTCONUpdaterIsDone - no controller instance
Timeout Error: out status : %x\n
overflow
AppleTCONControl
failed to set FW pointer to update bank
Baobab,ManifestEpoch
Wait Code: 0x%02x 0x%02x\n
setProd: update failed:0x%x phase:%u\n
Baobab,Trinity
FusePROD
1.%s.%s.%s.%s
Skipping
AppleTCONUpdaterExecCommand - invalid input
AppleTCONDP835Device::isFWComponentsUpdateRequired: %s\n
AppleTconDev:(%d:%d:%d:0x%02x:0x%02x:0x%02x)\n
getChipID failed
AppleTCONDP835Device::eventCmdPerformNextStage: update not required\n
Baobab2,ChipID
AppleTCONUpdateController::execCmdQueryInfo: Input\n
Failed to create AppleTCONControl matching dictionary\n
firmware data type invalid 
invalid type
getBoardID failed
Options.LifeCycle
```
