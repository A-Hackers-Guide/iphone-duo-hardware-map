# `/usr/lib/updaters/libAppleTCONUpdater.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 122,592 bytes.

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
AppleTCONUpdaterCreate - failed to register kLibAppleTCONUpdaterClass
Failed to get Prod value\n
getLifeCycle failed
Baobab,Ticket
AppleTCONUpdaterExecCommand - execCommand error
FirmwareData
AppleTCONDP835Device::updateFWComponent: component=0x%02x, componentDataLength=0x%08x\n
Baobab,Nonce
Fuse SDOM (%d:%d)\n
AppleTCONDP835Device::writeFWPointer: fWPointer:0x%08x\n
Baobab,ECID
device-id
Could not read error code\n
chipid
AppleTCONUpdateController::execCommand: Entering execCommand: command = %s\n
PROD status %s\n
Dev:CmdQueryInfo failure %s\n
bundle major ver < current major ver
AppleTCONUpdaterErrorDomain
setSdom: update failed:0x%x phase:%d\n
setProd: update (getDeviceStatus) error:0x%x\n
out of range
product path type mismatch
nvm ver string create failed
setProd: update failed:0x%x phase:%u\n
Payload
Skipping
FW Update Options I:%d S:%d\n
overflow
queryInfo
Failed to get memoryRef handle\n
nonce alloc failed
failed to write personalization manifest to EEPROM
Baobab,Life
AppleTCONUpdaterExecCommand - no AppleTCON controller instance
1.%s.%s.%s.%s
sdom-status
prod-fuse-value
tcon device not found
Failed to get eepromRef handle\n
getHWCID failed
Reset option %d\n
%02x
fw dict create failed
%u.%s.%s
AppleTCONDP835Device::eventCmdPerformNextStage: update not required\n
Dev:deviceid %s\n
updates failed
failed
Baobab2,TCON
Fuse Prod (%d:%d)\n
Failed to get Prod status\n
libAppleTCONUpdater
erase eeprom error (0x%08x): %s\n
ticket missing
CDIC_Setting
product path not found
performNextStage
Options.%@
AppleTCONDP835Device::eventCmdPerformNextStage: failure %s\n
conversion error
Failed to get bundle version\n
eraseDeviceEEPROM failed
end update failed
AppleTCONDP835Device::eventCmdPerformNextStage: failure: attempt to revert FW pointer %s\n
Baobab,SecurityDomain
AppleTCONUpdaterCreate
AppleTCONUpdateController::execCmdQueryInfo: device failure %d\n
invalid length
nvm_image
comp: key create failed
VCOM_Config
product not found
AppleTCONUpdateController::execCmdQueryInfo: create output dict: failed\n
Baobab2,ManifestEpoch
Options.LifeCycle
bundle minor ver < current minor ver
IODeviceTree:/
Invalid string
tcon-registers
FCBIST_Config
AppleTCONDP855Device::eventCmdPerformNextStage: Finished Personalization\n
getECID failed
Baobab,Cabal
Failed to get SDOM status\n
AppleTCONDP835Device::writeAndVerifyFWPointer: fWPointer:0x%08x\n
AppleTCONDP835Device::eventCmdPerformNextStage: update done\n
Baobab2,ProductionMode
bundle version type invalid
IOReg (%s) error: %s\n
comp: data missing
Baobab,ManifestEpoch
Failed to create AppleTCONControl matching dictionary\n
AppleTCONDP835Device::eventCmdPerformNextStage: didUpdate=%u personalize=%u updateDone=%u\n
AppleTCONUpdaterIsDone
AppleTCONUpdateController::execCmdQueryInfo: Begin Personalization\n
lcd-eeprom
SDOM status %s\n
setSdom: update failed:0x%x phase:%u\n
getChipID failed
enforce-pcds-valid
FuseSDOM
FW component update :%s\n
Timeout Error status 0x%02x\n
AppleTCONDP835Device::isFWComponentsUpdateRequired: %s update to 0x%02x:0x%02x:0x%02x\n
Performing
update fw component error:%s\n
FW_Config
setProd: update failed:0x%x phase:%d\n
submit dev:id failed
AppleTconDev(v2):(%d:%d:%d:%d:0x%02x:0x%02x(0x%04x))\n
get dev:id failed
bundle extent ver <= current extent ver
failed to update fw component
AppleTCONUpdaterCreate - failed to create AppleTCONUpdater
write eeprom error (0x%08x): %s\n
AppleTconDev:(%d:%d:%d:0x%02x:0x%02x:0x%02x)\n
Baobab2,UpdateNonce
firmware-ver
Update to 0x%02x:0x%02x\n
%s
invalid data pointer
start update failed
Dev:CmdQueryInfo SDOM not fused. No Fusing option. Bailing.\n
bundle extent ver < current extent ver
failed to read PCDS 0 top-level header
v8@?0
PLS_Config
PCDS must be generated and programmed before FW update can occur
bundle version after update differs from update bundle version
enforce-pcds-valid=0
Baobab2,ChipID
Baobab2,Provisioning
<libAppleTCONUpdater %p [%p]>{}
device_id
re alloc failed
succeeded
Baobab2,Trinity
AppleTCONUpdaterCreate - AppleTCONUpdateController start error\n
AppleTconDev:ECID: 0x%s\n
Failed to get Firmware version\n
failed to read PCDS 1 top-level header
Component Download Failed:Block:%d:length:%d!\n
RestoreOptions not a dict?
failed to erase
Baobab,TCON
Looking for entry under %s\n
getBoardID failed
Baobab2,BoardID
nonce
Unexpected boot status: 0x%02x\n
failed to update pcds component
writeDeviceEEPROM failed
@Baobab2,Ticket
displayECID: Avoid buffer overflow %d\n
expected bundle version: 0x%02x:0x%02x:0x%02x, actual bundle version: 0x%02x:0x%02x:0x%02x\n
AppleTCONUpdateController::execCmdQueryInfo: Output param missing\n
AppleTCONUpdaterIsDone - no controller instance
EDID
download fw failed
Options
AppleTCONUpdateController::execCommand: device failure %d\n
firmware missing
failed to erase personalization manifest from EEPROM
failed to set FW pointer to update bank
bundle-ver
%s [error]: %s\n
Timeout Error: out status : %x\n
Baobab,Provisioning
Baobab,ChipID
Baobab,BoardID
chipID alloc failed
firmware dict: create failed
Baobab2,BacklightController
%@: %s
Failed to get boot status\n
boardID alloc failed
Baobab2,ECID
Download comp:0x%04x NumBlocks:%d\n
1.firmware.Payload
Baobab,ProductionMode
AppleTCONUpdateController::execCommand: Unsupported command: %s\n
AppleTCONDP835Device::isFWComponentsUpdateRequired: %s\n
Wait Code: 0x%02x 0x%02x\n
download comp: failed
Baobab2,Cabal
AppleTCONUpdaterExecCommand - invalid input
AppleTCONUpdateControllerGetDevice failed: %s\n
AppleTCONUpdateController::start: Dev = (%p) - updateSupported = %d\n
RestoreInternal
TCON_Config
PGAMMA_Config
EQ_Setting_Config
memory alloc failed
Unable to allocate memory
bundle payload type invalid
Baobab2,Nonce
FusePROD
bundle ver: num: invalid
OTP_STATUS_PROGRAMMED
SDOM not fused; see rdar://84123825 for instructions
@Baobab,Ticket
Error code 0x%02x!\n
otp update failed
Baobab,UpdateNonce
prod-status
ecid alloc failed
alloc: failed
Failed to find AppleTCONControl service\n
Baobab2,SecurityDomain
Version
AppleTCONControl
Baobab2,Ticket
PMIC_Config
IODeviceTree:/product
AppleTCONDP835Device::isFWComponentsUpdateRequired: internal:%u skipSameVersion:%u\n
LUTS_Config
AppleTCONUpdateController::execCommand: Exiting execCommand: command = %s, result = 0x%X\n
firmware data type invalid 
getNonce failed
invalid type
Baobab,BacklightController
setSdom: update (getDeviceStatus) error:0x%x\n
Baobab,Trinity
SkipSameVersion
ecid
AppleTCONUpdateController::execCmdQueryInfo: Input\n
AppleTCONDP835Device::readFWPointer: activeFWPointer:0x%08x inactiveFWPointer:0x%08x\n
Dev:next stage failure %s\n
%u.%s.Payload
AppleTCONRestoreLib Version %d.%d\n
Failed to getIORegRootNode. Will Attempt fallback.\n
comp: string create failed
tcon-path
AppleTCONUpdaterExecCommand
getLifeCycle %s\n
update fw error:%s\n
kern.bootargs
OTP_STATUS_UNPROGRAMMED
failed to write
AppleTCONDP835Device::eventCmdQueryInfo: boardID=0x%08x HWCID=0x%08x personalize=%u\n
failed to read bundle version after update
NVM_IMAGE
```
