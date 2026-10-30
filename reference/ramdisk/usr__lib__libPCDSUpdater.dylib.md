# `/usr/lib/libPCDSUpdater.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 200,608 bytes.

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
createFileAtPath:contents:attributes:
length
localizedDescription
setDateFormat:
setValue:forKey:
numberWithUnsignedInt:
writeToURL:error:
initWithFormat:
dictionaryWithObjects:forKeys:count:
stringWithFormat:
bytes
date
defaultManager
fileExistsAtPath:
fileURLWithPath:
createDirectoryAtPath:withIntermediateDirectories:attributes:error:
stringFromDate:
%s: ambTemp = %f (%#x)
DisplayPerf:%s: END panelPowerDown
DisplayPerf:%s: END exit TCON idle state (%#x)
%s: Failed to erase bundle version in TCON NVM
%s: Failed to read height - secondary
%s: Sent CoreAnalytics event of video quality data
TCONSYSIRQ:%s: DPCD437 = %02X, DPCD43C = %02X, DPCD43B = %02X,DPCD427=%02X, prevDPCD427=%02X DPCD439=%02X
%s: FW_LOAD SW Reset
%s: _activeFWPointer:0x%x _inactiveFWPointer:0x%x
%s: serialNumber:%0x\n
%s: Failed to create CFData for IORegistry entry
%s: AppleSMC service not found\n
%s: Failed to read DP Slave CTRL
DisplayPerf:%s: START HostState=%02X(%s) prevHostState=%02X(%s) _tconState=%X
DisplayPerf:%s: START exit TCON idle state
%s: Invalid arguments
%s: %#x (%#x)
%s: _copyDataStructures Failed %d\n
TCONSYSIRQ:%s: End MP_L0_CR_DONE
%s: updatePCDS -End
TCONSYSIRQ:%s: End DPCD427_WR
%s: TCON is idle, reading fw pointer directly from TCON NVM
%s: Invalid byte 2 in read response, received value: 0x%02X, expected value: 0x%02X
%s: Cancel _powerdownTimeout
%s: Failed to power down the TCON module
DisplayPerf:%s: START Secondary HPD Assert
DisplayPerf:%s: END Secondary HPD Assert
%s: isValid = %d pcdsTLHeader = %x\n
%s: IORegistry Serial Number not available
%s: Write to set LCDPWREnable (0x%X, 0x%X)\n
%s: Invalid error mask: %u
TCONSYSIRQ:%s: Start MP_L0_CR_DONE
%s: CMDIF request(%s) Failed cmdStatus = %2X
%s: BLC_OK message not received
%s: BLC register read request time out after 200 ms
%s: Cleared Active Preset Pointer
%s: %s (%#x)
%s: Read of BLC register 0x%04X failed
%s: Invalid BLC Fault poll response, bytes[0-4]: 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X, faultMessageCount: %u, faultCondition: %u
DisplayPerf:%s: PanelPower=%s
TCONSYSIRQ:%s: BLC_FAULT_ERROR
%s: TCON NVM still acquired by other components, early return
%s: Invalid byte 1 in read response, received value: 0x%02X, expected value: 0x%02X
%s: Cleared bundle version in TCON NVM
%s: Checksum doesn't match, Received value: 0x%02X, Calculated value: 0x%02X
%s: setOrientationStatus (err %#x)
TCONSYSIRQ:%s: TCON_BOOT_DONE
TCONSYSIRQ:%s: TRINITY_MCU_WDT
TCONSYSIRQ:%s: BL_THERMAL_THROTTING_ACTIVE
%s: _copyEDIDTemplate Failed %d\n
%s: Old PCDS to New PCDS Write Failed %d index:0x%x\n
%s: Failed to open AppleSMC service (%#x)\n
%s: Unexpected CMDIF API error.
DisplayPerf:%s: END enter TCON idle state (%#x)
%s: Acquiring TCON NVM (%d)
%s: Releasing TCON NVM (%d)
%s: _readMsgFromBLC failed, return code: %d
%s: Failed to open AppleTCONControl service (%#x)\n
%s: releaseTCONNVM failed (err %#x)
DisplayPerf:%s: END SingleDP
%s: _sendMsgToBLC failed, return code: %d
%s: PCDS Structures Write Failed %d\n
%s: Cancel _vtTimer
%s: AppleDisplayPlatformControl service not found\n
%s: Failed to send CoreAnalytics event of tcon data
%s: Failed to read width - secondary
TCONSYSIRQ:%s: DSC_FEC_ERR
%s: Bundle Data length is invalid %x\n
%s: PCDS Write Failed %d\n
%s: Failed to create virtual temperature timer.
%s: CREATED %@
%s: Invalid byte 3 in read response, received value: 0x%02X, expected value: 0x%02X
%s: CMDIF request(%s) time out after 200 ms
%s: Powering down TCON
%s: IORegistry container ID %s
%s: Boot Status: %#x\n
%s: Failed to set Virtual Temperature (%#x, %d errors).
%s: Container ID:%02x%02x%02x%02x-%02x%02x-%02x%02x-%02x%02x-%02x%02x%02x%02x%02x%02x\n
%s: Preset CRC Update index %d Failed %d\n
%s: AppleTCONControl service not found\n
%s: bitsPerPixel: %u, hWidth: %u, vHeight: %u
%s: TCON is not idle, reading fw pointer from command interface
%s: Invalid byte 0 in read response, received value: 0x%02X, expected value: 0x%02X
%s: Failed to create powerdown timer.
%s: unknown display target
%s: Invalid value
TCONSYSIRQ:%s: BL_MCU_WDT
%s: fcalPtr Update index %d Failed %d\n
%s: writeToURL failed with error: %@
%s: IORegistryEntryFromPath failed to find path: %{public}s
%s: CMDIF request(%s) Failed Previous CMDIF request in progress cmdStatus = %2X
%s: Failed to create directory
%s: Invalid mask page offset: %u
%s: Failed to read bit depth
%s: userCalibrationInProgress not setting SingleDP
%s: Failed to read width - primary
TCONSYSIRQ:%s: START_SLEEP
TCONSYSIRQ:%s: FATAL_ERR, PHY_CTRL_REG_SCRATCH_E4 reg value: 0x%02X
%s: TCON already idle, early return
%s: getOrientationAngle (err %#x)
%s: current PCDS Version: 0x%x New PCDS Version: %x
%s: Failed to write zeroes to bundle version in TCON NVM
%s: Failed to create one shot timer.
%s: Setting Brightness(TCON CMDIF) to %f nits minBrightnessFromPreset = %f maxBrightnessFromPreset = %f ret: %x
%s: Failed to create notification port\n
%s: Failed to connect to AppleSMC service (%#x)\n
TCONSYSIRQ:%s: Start DPCD427_WR  DPCD427=%02X prevDPCD427=%02X
%s: EDID Update Failed %d\n
%s: userCalibrationInProgress not asserting Primary HPD
TCONSYSIRQ:%s: CABAL_MCU_WDT
%s: Power cycling TCON
%s: DELETED %@
%s: Orientation angle is not multiple of 90 degrees
%s: SYS IRQ status1: 0x%02X, status3: 0x%02X
%s: userCalibrationInProgress will power down TCON after UC clean up
%s: updatePCDS -Start
%s: OrientationServiceAnglePacket angle = %u\n
%s: Unexpected boot Status, TCON FW recovery required 0x%x
TCONSYSIRQ:%s: BLC_SANITY_CHECK_FAIL
%s: IRQ_STATUS0:%#x, SCRATCH_C2:%#x
%s: _copyActivePCDS Failed %d\n
%s: _updatePreset Failed %d\n
%s: Failed to create file at path: %@
DisplayPerf:%s: START Primary HPD Assert
%s: userCalibrationInProgress not asserting Secondary HPD
TCONSYSIRQ:%s: START_WAKE
%s: TCON NVM acquired previously but TCON is not idle (ret = %#x)
%s: Read of register %u not supported
%s: Failed to get acquire TCON NVM
TCONSYSIRQ:%s: BLC Sanity registers - Address: 0x%04X, Value: 0x%02X
%s: Failed to read height - primary
DisplayPerf:%s: END Primary HPD Assert
DisplayPerf:%s: START enter TCON idle state
%s: Failed to retrieve Virtual Temperature (%#x).
%s: BLC register read response time out after 200 ms
%s: _activePCDSPointer:0x%x _inactivePCDSPointer:0x%x
TCONSYSIRQ:%s: BLC register 0x%04X value: 0x%02X
%s: Previous command is still executing, cannot send a new command
%s: TCON isInitialized: %s, tconControlClient isInitialized: %s, displayPlatformCtrlClient isInitialized: %s, _tconRegs isNull: %s\n
DisplayPerf:%s: START SingleDP
DisplayPerf:%s: START panelPowerDown
DisplayPerf:%s: END HostState=%02X(%s) prevHostState=%02X(%s)
%s: Failed to reset the TCON
%s: Old PCDS to New PCDS Read Failed %d index:0x%x\n
%s: IORegistryEntrySetCFProperty failed: %d
TCONSYSIRQ:%s: TCON_NVMEM_READ_ERROR
%s: Failed to power on the TCON module
%s: Preset read index %d Failed %d\n
getOrientationAngle
module-serial-number
Resolution
CMDIF_READ_SPI_NVMRAM
_isPCDSValid
startTelemetryTimer
_getResolution
enterTCONIdleState
kHostStateDisconnected
_startPowerdown_block_invoke
_updatePreset
startPeriodic
RebindingADPAssertion
readBLCRegister
kHostStateActive
CMD_IF_SET_PANEL_PWR_DOWN failed while powered.
yes
BitsPerPixel
Reading CMD_IF_QUERY_PANEL_PWR_STATE
updateVirtualTemperature
_readFWPointer
/var/logs/BLC/blc_fault_error_log_%@.plist
enable
TVA0
writeBLCRegsToFile
kern.bootargs
IODeviceTree:/options
_getGPIO
setBacklightLevelInNits
_startPowerdown
_getBitsPerPixel
CMDIF_PANEL_PWR_STATE_CTRL
assertHPD
CMDIF_BL_WL_UPDATE
v36@?0^{AppleTCONControlClient=II^{IONotificationPort}I^vB}8^v16i24^v28
IOGeneralInterest
%u x %u
handleHostEvent
setPropertyForRecoveryMode
AppleSMCClient
CMDIF_BOOT_LOG_DUMP
CMDIF_RESET_MCU
tcon
TCONIOKitInterface
vt-enable=0
lcd-eeprom
_readContainerID
smcGetAmbientTemperature
TCONFirmwarePointer
DisplayCoverGlassConfig
isAnyIrrecoverableErrorSet
CMDIF_CLEAR_SYS_IRQ
CMDIF_WRITE_APB
PCDSUpdater
gP0c
CMDIF_GET_MCU_FW_VERSION
_copyEDIDTemplate
clearTCONBundleVersion
active-prevent
_sendCMDIF
_copyActivePCDS
012345679CDFGHJKLMNPQRTVWXY
startPeriodic_block_invoke
~RebindingADPAssertion
smcGetVirtualTemperature
setTCONError
acquireTCONNVM
IOService
@\"NSDictionary\"8@?0
has incorrect length
tcon-registers
D1St
setDualDP
kHostStateSleep
lcd-cpld2
dd-MM-yyyy'T'HH-mm-ss
coverglass-serial-number
CMDIF_EDID_RELOAD
PreviousHostState
unique-serial-number
/var/logs/BLC/
AppleDisplayPlatformCtrlClient
Group
setSingleDP
CMDIF_CHECK_HDCP_STATUS
_setPCIOGPIO
no
activePresetPointer
DisplayProductionDate
kHostStateInvalid
Sending CMD_IF_QUERY_PANEL_PWR_STATE
_performTCONAndModuleReset
getSyscfgContainerID
_reportVideoQualityData
isTCONNoLoad
getTCONRegVal
panelPowerStateControl
_logBLCSanityRegs
updatePCDS
com.apple.tconcontrold
TVL1
exitTCONIdleState
<Unknown>
/private/var/root/Library/Preferences/com.apple.tconcontrold.plist
not available
auto-boot-once
AppleDisplayPlatformControl
On
blc-fault-file-logging-enable=1
releaseTCONNVM
lcd-cpld1
false
tconSoftResetCount
AppleTCONControlClient
handleTCONEvent
0x%02X
HostState
CMDIF_READ_APB
unique-container-id
AppleTCONControl
TCONControlState
Error
v8@?0
CMDIF_THERMAL_THROTTLING_FACTOR
AppleSMC
%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X
_copyDataStructures
tconHardResetCount
userCalibrationInProgress
prevent
_setGPIO
Off
endAccess
_readMsgFromBLC
com.apple.Display.VideoQualityData
_updateRotationStatus
_readLogBLCFaultCode
_logSetBLCRegVal
Registers
TimeStamp
vector
getSyscfgSerialNumber
v40@?0^{AppleDisplayPlatformCtrlClient=II^{IONotificationPort}I^vB}8^v16{HostStateMessage=ii}24^v32
_readSerialNumber
smcHasThunderboltConnection
getFWImageAddresses
setOrientationStatus
_sendMsgToBLC
```
