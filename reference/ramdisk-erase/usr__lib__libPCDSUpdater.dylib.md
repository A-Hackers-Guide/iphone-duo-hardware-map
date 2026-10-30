# `/usr/lib/libPCDSUpdater.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 200,608 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 26 (Size: 3088)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (10)

- `/usr/lib/libPCDSUpdater.dylib (compatibility version 1.0.0, current version 70.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (313)

```
%s: setOrientationStatus (err %#x)
%s: _copyActivePCDS Failed %d\n
%s: Container ID:%02x%02x%02x%02x-%02x%02x-%02x%02x-%02x%02x-%02x%02x%02x%02x%02x%02x\n
%s: AppleSMC service not found\n
TCONSYSIRQ:%s: TCON_BOOT_DONE
%s: Powering down TCON
%s: Old PCDS to New PCDS Write Failed %d index:0x%x\n
%s: IORegistryEntrySetCFProperty failed: %d
DisplayPerf:%s: END enter TCON idle state (%#x)
%s: Orientation angle is not multiple of 90 degrees
%s: Failed to create powerdown timer.
%s: _copyEDIDTemplate Failed %d\n
%s: _updatePreset Failed %d\n
%s: Failed to read height - primary
%s: Cancel _powerdownTimeout
%s: Failed to power on the TCON module
%s: updatePCDS -End
%s: Preset read index %d Failed %d\n
%s: Failed to erase bundle version in TCON NVM
TCONSYSIRQ:%s: CABAL_MCU_WDT
DisplayPerf:%s: START enter TCON idle state
%s: Failed to open AppleSMC service (%#x)\n
TCONSYSIRQ:%s: FATAL_ERR, PHY_CTRL_REG_SCRATCH_E4 reg value: 0x%02X
%s: IRQ_STATUS0:%#x, SCRATCH_C2:%#x
%s: _sendMsgToBLC failed, return code: %d
%s: BLC register read response time out after 200 ms
%s: fcalPtr Update index %d Failed %d\n
%s: IORegistryEntryFromPath failed to find path: %{public}s
TCONSYSIRQ:%s: TRINITY_MCU_WDT
%s: Read of register %u not supported
TCONSYSIRQ:%s: BLC register 0x%04X value: 0x%02X
%s: FW_LOAD SW Reset
%s: Old PCDS to New PCDS Read Failed %d index:0x%x\n
%s: isValid = %d pcdsTLHeader = %x\n
DisplayPerf:%s: START panelPowerDown
%s: Invalid BLC Fault poll response, bytes[0-4]: 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X, faultMessageCount: %u, faultCondition: %u
TCONSYSIRQ:%s: BLC Sanity registers - Address: 0x%04X, Value: 0x%02X
%s: Failed to get acquire TCON NVM
%s: OrientationServiceAnglePacket angle = %u\n
DisplayPerf:%s: START HostState=%02X(%s) prevHostState=%02X(%s) _tconState=%X
TCONSYSIRQ:%s: End MP_L0_CR_DONE
%s: serialNumber:%0x\n
%s: releaseTCONNVM failed (err %#x)
%s: IORegistry container ID %s
%s: Failed to connect to AppleSMC service (%#x)\n
%s: ambTemp = %f (%#x)
DisplayPerf:%s: END SingleDP
TCONSYSIRQ:%s: DPCD437 = %02X, DPCD43C = %02X, DPCD43B = %02X,DPCD427=%02X, prevDPCD427=%02X DPCD439=%02X
TCONSYSIRQ:%s: BL_THERMAL_THROTTING_ACTIVE
%s: Unexpected CMDIF API error.
%s: updatePCDS -Start
%s: PCDS Write Failed %d\n
%s: Failed to create one shot timer.
DisplayPerf:%s: END HostState=%02X(%s) prevHostState=%02X(%s)
TCONSYSIRQ:%s: BLC_FAULT_ERROR
%s: CREATED %@
DisplayPerf:%s: START Secondary HPD Assert
%s: BLC_OK message not received
%s: current PCDS Version: 0x%x New PCDS Version: %x
TCONSYSIRQ:%s: START_WAKE
%s: Setting Brightness(TCON CMDIF) to %f nits minBrightnessFromPreset = %f maxBrightnessFromPreset = %f ret: %x
%s: Invalid byte 1 in read response, received value: 0x%02X, expected value: 0x%02X
%s: unknown display target
%s: Invalid error mask: %u
%s: Failed to power down the TCON module
%s: writeToURL failed with error: %@
%s: Failed to create virtual temperature timer.
%s: DELETED %@
%s: Failed to read width - primary
%s: Failed to read DP Slave CTRL
DisplayPerf:%s: START SingleDP
%s: Previous command is still executing, cannot send a new command
TCONSYSIRQ:%s: Start DPCD427_WR  DPCD427=%02X prevDPCD427=%02X
TCONSYSIRQ:%s: Start MP_L0_CR_DONE
%s: Releasing TCON NVM (%d)
DisplayPerf:%s: END Primary HPD Assert
%s: Failed to reset the TCON
%s: Failed to write zeroes to bundle version in TCON NVM
%s: TCON isInitialized: %s, tconControlClient isInitialized: %s, displayPlatformCtrlClient isInitialized: %s, _tconRegs isNull: %s\n
%s: Cancel _vtTimer
%s: %#x (%#x)
%s: AppleTCONControl service not found\n
DisplayPerf:%s: START Primary HPD Assert
%s: CMDIF request(%s) Failed cmdStatus = %2X
%s: Failed to create CFData for IORegistry entry
%s: Failed to send CoreAnalytics event of tcon data
TCONSYSIRQ:%s: BLC_SANITY_CHECK_FAIL
DisplayPerf:%s: END exit TCON idle state (%#x)
%s: bitsPerPixel: %u, hWidth: %u, vHeight: %u
TCONSYSIRQ:%s: START_SLEEP
%s: TCON is idle, reading fw pointer directly from TCON NVM
%s: Power cycling TCON
%s: PCDS Structures Write Failed %d\n
%s: Failed to create notification port\n
%s: Failed to read width - secondary
%s: userCalibrationInProgress not asserting Secondary HPD
DisplayPerf:%s: END Secondary HPD Assert
%s: TCON NVM still acquired by other components, early return
%s: BLC register read request time out after 200 ms
%s: _copyDataStructures Failed %d\n
%s: _activeFWPointer:0x%x _inactiveFWPointer:0x%x
%s: Sent CoreAnalytics event of video quality data
%s: userCalibrationInProgress not asserting Primary HPD
%s: userCalibrationInProgress not setting SingleDP
TCONSYSIRQ:%s: End DPCD427_WR
%s: TCON already idle, early return
%s: _readMsgFromBLC failed, return code: %d
%s: Invalid byte 3 in read response, received value: 0x%02X, expected value: 0x%02X
%s: _activePCDSPointer:0x%x _inactivePCDSPointer:0x%x
DisplayPerf:%s: PanelPower=%s
%s: Failed to read height - secondary
%s: Boot Status: %#x\n
%s: TCON NVM acquired previously but TCON is not idle (ret = %#x)
%s: TCON is not idle, reading fw pointer from command interface
%s: Failed to retrieve Virtual Temperature (%#x).
%s: Failed to create file at path: %@
TCONSYSIRQ:%s: DSC_FEC_ERR
%s: Acquiring TCON NVM (%d)
%s: Invalid arguments
%s: EDID Update Failed %d\n
%s: Preset CRC Update index %d Failed %d\n
%s: Cleared bundle version in TCON NVM
%s: AppleDisplayPlatformControl service not found\n
%s: Invalid mask page offset: %u
DisplayPerf:%s: END panelPowerDown
TCONSYSIRQ:%s: TCON_NVMEM_READ_ERROR
%s: Invalid byte 0 in read response, received value: 0x%02X, expected value: 0x%02X
%s: getOrientationAngle (err %#x)
%s: Failed to set Virtual Temperature (%#x, %d errors).
%s: Bundle Data length is invalid %x\n
%s: Failed to open AppleTCONControl service (%#x)\n
%s: Unexpected boot Status, TCON FW recovery required 0x%x
%s: Read of BLC register 0x%04X failed
%s: Write to set LCDPWREnable (0x%X, 0x%X)\n
%s: Invalid value
%s: Checksum doesn't match, Received value: 0x%02X, Calculated value: 0x%02X
%s: userCalibrationInProgress will power down TCON after UC clean up
%s: Failed to read bit depth
%s: CMDIF request(%s) time out after 200 ms
%s: Cleared Active Preset Pointer
%s: %s (%#x)
TCONSYSIRQ:%s: BL_MCU_WDT
%s: Invalid byte 2 in read response, received value: 0x%02X, expected value: 0x%02X
%s: SYS IRQ status1: 0x%02X, status3: 0x%02X
%s: CMDIF request(%s) Failed Previous CMDIF request in progress cmdStatus = %2X
%s: IORegistry Serial Number not available
%s: Failed to create directory
DisplayPerf:%s: START exit TCON idle state
startPeriodic_block_invoke
_setGPIO
v8@?0
assertHPD
HostState
getTCONRegVal
com.apple.Display.VideoQualityData
panelPowerStateControl
_copyDataStructures
tcon
CMDIF_CHECK_HDCP_STATUS
has incorrect length
writeBLCRegsToFile
kern.bootargs
IOGeneralInterest
_getGPIO
AppleTCONControl
Group
_sendMsgToBLC
_logBLCSanityRegs
_logSetBLCRegVal
tconHardResetCount
IOService
012345679CDFGHJKLMNPQRTVWXY
lcd-eeprom
smcHasThunderboltConnection
coverglass-serial-number
kHostStateDisconnected
lcd-cpld1
/var/logs/BLC/
smcGetAmbientTemperature
gP0c
releaseTCONNVM
TCONIOKitInterface
v36@?0^{AppleTCONControlClient=II^{IONotificationPort}I^vB}8^v16i24^v28
startPeriodic
setOrientationStatus
AppleDisplayPlatformControl
D1St
exitTCONIdleState
updateVirtualTemperature
CMDIF_EDID_RELOAD
CMDIF_READ_APB
getOrientationAngle
TCONControlState
@\"NSDictionary\"8@?0
kHostStateSleep
_copyEDIDTemplate
/var/logs/BLC/blc_fault_error_log_%@.plist
IODeviceTree:/options
auto-boot-once
activePresetPointer
_reportVideoQualityData
_sendCMDIF
TimeStamp
vector
com.apple.tconcontrold
prevent
TVL1
CMDIF_READ_SPI_NVMRAM
CMDIF_WRITE_APB
On
handleTCONEvent
acquireTCONNVM
readBLCRegister
false
AppleSMCClient
AppleTCONControlClient
startTelemetryTimer
CMDIF_BL_WL_UPDATE
_startPowerdown_block_invoke
_copyActivePCDS
TVA0
endAccess
handleHostEvent
kHostStateInvalid
CMDIF_GET_MCU_FW_VERSION
lcd-cpld2
_isPCDSValid
clearTCONBundleVersion
smcGetVirtualTemperature
isTCONNoLoad
isAnyIrrecoverableErrorSet
CMDIF_RESET_MCU
CMDIF_CLEAR_SYS_IRQ
_readContainerID
AppleSMC
DisplayCoverGlassConfig
setTCONError
BitsPerPixel
not available
tcon-registers
PreviousHostState
_updateRotationStatus
_readLogBLCFaultCode
_startPowerdown
%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X
setDualDP
unique-serial-number
getSyscfgSerialNumber
setPropertyForRecoveryMode
Reading CMD_IF_QUERY_PANEL_PWR_STATE
Registers
setSingleDP
_readMsgFromBLC
RebindingADPAssertion
DisplayProductionDate
Error
kHostStateActive
0x%02X
/private/var/root/Library/Preferences/com.apple.tconcontrold.plist
_readFWPointer
CMDIF_PANEL_PWR_STATE_CTRL
_performTCONAndModuleReset
userCalibrationInProgress
AppleDisplayPlatformCtrlClient
blc-fault-file-logging-enable=1
setBacklightLevelInNits
<Unknown>
updatePCDS
_readSerialNumber
v40@?0^{AppleDisplayPlatformCtrlClient=II^{IONotificationPort}I^vB}8^v16{HostStateMessage=ii}24^v32
TCONFirmwarePointer
enterTCONIdleState
getFWImageAddresses
CMD_IF_SET_PANEL_PWR_DOWN failed while powered.
CMDIF_BOOT_LOG_DUMP
PCDSUpdater
unique-container-id
dd-MM-yyyy'T'HH-mm-ss
tconSoftResetCount
enable
Off
Resolution
CMDIF_THERMAL_THROTTLING_FACTOR
_updatePreset
getSyscfgContainerID
yes
~RebindingADPAssertion
module-serial-number
%u x %u
active-prevent
Sending CMD_IF_QUERY_PANEL_PWR_STATE
no
vt-enable=0
_setPCIOGPIO
_getResolution
_getBitsPerPixel
setDateFormat:
createDirectoryAtPath:withIntermediateDirectories:attributes:error:
createFileAtPath:contents:attributes:
length
localizedDescription
writeToURL:error:
initWithFormat:
bytes
defaultManager
numberWithUnsignedInt:
stringFromDate:
dictionaryWithObjects:forKeys:count:
fileExistsAtPath:
fileURLWithPath:
date
setValue:forKey:
stringWithFormat:
```
