# `/usr/lib/libPN548_API.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 538,128 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 26 (Size: 2472)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (9)

- `/usr/lib/libPN548_API.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libFDR.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libnfshared.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libNFC_HAL.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libNFC_Comet.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (1,949)

```
%s:%i \t Log is empty!
SPMI_CONFIG_TAG
%s:%i Failed to get FDR data : %ld - %s
%s:%i GET OS MODE
%s:%i SELECT returned error: 0x%04x. Cannot query presence of attack log without selecting ISD
ESE HIGH
NFDriverCopySMBLog
%s:%i Changing RF settings to alternate
%s:%i Unknow Key Usage 0x%x
%s:%i Re-using entry threhold
NFDriverEnableSPMIEventLogging
%s:%i Powering SE back ON
_Async_NFDriverSetSEAlwaysOn_block_invoke
%s:%i Invalid data returned: %d
_NFDriverRFSettingsGetRFProp
%s:%i Unexpected type
%s:%i Note : OS mode is Boot Loader
%s:%i Running build from (B&I) Stockholm_Base-371.8
%s:%i OS %d removed for reason 0x%x
%s:%i wantsFieldDetect=%d wantsPolling=%d wantsExpress=%d eSE=%d host=%d ceType=%d, hasDiscoveryChanges=%d hasRoutingChanges=%d fullHCE=%d
%s:%i Unknown type: %d
%s:%i Failed to set GPIO : %u
NFDriverSendMFGCommand_block_invoke
A0130419191919A00D03610982A09808C0f9088019171717A09E0C07001D960090012BD0070000A0AF0911FFF0191196A01902A06A1000000000000064000000000000000000A0682A064060031914204000930418603F204D450330030B031A0307FA000000350008007D00003500000E0003A0940A0720
%s:%i Got unknown certificate type??
Enabled
NFDriverRunIntegrityDebug
%s:%i Polling config is using VAS ECP
%s:%i phLibNfc_RemoteDev_Disconnect failed: 0x%04llx
%s:%i Simulating HW Reset
NFDriverConfigureExpressFelicaEntry
_NFDriverRecoverESE_block_invoke
LMA_RSSI
GetOSMode_Eos
%s:%i TxLDO OverCurrent Error
%s:%i Unexpected size of AID prefix : %d.
NFDriverSetEmbeddedSecureElementPower
%s:%i phLibNfc_RemoteDev_Send failed 0x%04llx
%s:%i Failed to set eSE to virtual mode
%s:%i Failed to get JCOP Version
GetOSInfo_Host
_NFDriverLoadStackSteps
%s:%i %02d: %04d %04d %04d %04d %04d %04d %04d %04d
%s:%i Non-default polling period: %u
_NFDriverSetReaderModeRFConfigRegsSigned
%s:%i Failed to parse TLVs, is the format correct ?
%s:%i Stack load failed with 0x%x
CRC Error
%s:%i HW is not supported
%s:%i Crashing in %d ms
%s:%i Not supported
%s:%i MultiTag-FC=%d
%s:%i Unknown parameter !
_NFDriverSetRFSettings
%s:%i Added Tag (%d) rfTech = %d id= 0x%02x 0x%02x 0x%02x 0x%02x
%s:%i Failed to read Module cal data from FDR.
_NFDriverRegisterNCINotifications
NFDriverUpdateFirmware
%s:%i Failed to set data rate for NTAG5 %d
%s:%i AID_P73_MANIFESTQUERY returned error: 0x%04x
%s:%i Customer factory page is locked. Cannot clear E0 tag.
%s:%i Could not get Sealed Data Instance
NFDriverUnloadStack
%s:%i Failed to allocate buffer
%s:%i Not supported on MWF
%s:%i %s Continuous Wave
NFDriverSetHCETypeAConfig
vGPIO
%s:%i Failed to trigger core dump
NFDriverSetFelicaSystemCode
%s:%i Error: Failed to power cycle the SE.
_Async_NFDriverSETransceive_block_invoke
%s:%i Types-AF only
%s:%i WTX: error %d
%s:%i Invalid length %d for tag 0x%x: only %zu remaingin
NFDriverGetBootMeasurements
%s:%i **** getNfccParamsCb: STATUS = 0x%02X ****
_Async_NFDriverSetCEConfigParams_block_invoke
%s:%i Customer Factory page is unlocked.
%s:%i Error ! Unexpected cert length 
%s:%i ==== GPADC TEMPERATURE CONDITION NORMAL ====
%s:%i No SE of type %d.
Unknown Error
%s:%i Failed to configure A08F: 0x%04x
%s:%i [L2] %0.6f state=0x%02x mod=0x%02x sc=0x%04x, extraInfo=0x%0x RMRobustness=0x%04x
%s:%i Failed to query controller info.
GetUptime_P73
%s:%i Failed to power off Host
Off
SetPower_Eos
%s:%i SELECT: ISD
_NFDriverConfigureECPPolling
%s:%i target lost
%04X.%02X-%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X
SetPower_Host
_NFDriverSetControllerInfo_block_invoke
%s:%i Failed to set RF settings : status=0x%04X
%s:%i Received Spmi Error Register Info notification
Measurement Error
NFDriverGetMultiTagState
%s:%i Writing headless mini NV 
%s:%i Warning : B state cal data was written with A state values. Applying ..
_NFDriverConfigureRFLogging
%s:%i SE is now recovered and set to prior mode
_NFDriverEnumerateSecureElements
%s:%i Forcing full hce routing
%s:%i Error : timeout occured !!!
%s:%i Discovery already stopped, don't need to stop again
%s:%i \t Invalid 'eNfccParam' returned
%s:%i Failed to read RF cal data from FDR.
%s:%i Secondary = %s
%s:%i HCE Register error = 0x%04x
_NFDriverEnableMultiRFSettings
%s:%i Mutex init failed : %d
%s:%i Removed Tag (%d) rfTech = %d id= 0x%02x 0x%02x 0x%02x 0x%02x
_Async_NFDriverGetClrAssertRegs_block_invoke
NFDriverRFSettingsCopySigned
%s:%i Failed to get FDR data from local store, trying memory
%s:%i Data length is %ld
GetOSInfo_UICC
%s:%i toBeforeStdbyCfg=%d ms, requesting %d
%s:%i Setting prevent reset to %d
Delayed crashing
[Reader C-APDU>]
%s:%i Found FDR data, %ld bytes
NFDriverSecureElement_SetPower
%s:%i Compensation applied, poll phase duration (ms): %d
stack dump
%s:%i profile: %d
%s:%i ProhibitTimer.SE.End
%s:%i RSSI stats count %d, min=%d, max=%d, average=%d
NFDriverAntennaSelfTest_block_invoke
Assert
Unexpected headless reply
%s:%i phLibNfc_RemoteDev_Receive failed 0x%04hx
Failed to write page :
%s:%i Failed to enable write counters status:0x%08llx
%s:%i [L1] %0.6f APCInfo=0x%x tech=0x%x retCode=0x%x vpp=%f ALMPhase=%.3f RMRobustness=0x%04x
(options & (NFDriverCustomerFactoryPageLock | NFDriverCustomerFactoryPageDebug)) == 0
%s:%i Failed to parse TLV
NFDriverGetStackBreadcrumb
No system cal
%s:%i Not updating the rest of OS Info : JCOP is not available
GetJCOPOSSerialNumber
%s:%i Use default ECP value
com.apple.stockholm.driverQueue.primary
%s:%i Power state tracking query
%s:%i RSSI stats with no sample
%s:%i Failed to restore discoverty configuration
%s:%i Failed to write miniNV
_Async_NFDriverHCISoftReset_block_invoke
Received tag value : 
%s:%i platform: %d.%d.%d.%d
GetAttackCounterLog_Host
%s:%i Embedded SE EVT_RESTRICTED!
%s:%i host-LP: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
_NFDriverLogHostProhibitTimerSignpost
%s:%i Types-ABF only
%s:%i Re-init failed. Bailing.
_NFDriverEnableWriteCounters
%s:%i deactivated
_NFDriverGetSiliconName
%s:%i MultiTag Enabled: %d, Running: %d
NFDriverGetFlashWriteCounter
%s:%i kernel: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
%s:%i RF settings = %s
_Async_NFDriverTriggerDelayedWake_block_invoke
_NFDriverRemoteDevTransceive
%s:%i ---- SPMI ----
NFDriverSecureElement_GetPresenceOfAttackLog
%s:%i EEPROM validation failed (%d/%d)
_Async_NFDriverSetHeadlessMode_block_invoke
_Async_NFDriverConfigureDiscovery
GetAttackCounterLog_Eos
%s:%i MW requested VEN reset.
%s:%i Unknown OS mode %d
mutex != NULL
%s:%i Failed to configure HW settings
ShSC
ShSB
%s:%i Temperature monitoring configured
%s:%i LPCD-FC=%d
%s:%i Failed : 0x%x
%s:%i E0 tag not found or already cleared. Nothing to do.
_Callback_NFDriverNotifyGeneral_block_invoke_2
%s:%i Failed to get controller info
_NFDriverConfigMiniNVForHeadless
%s:%i Disabling headless mode
%s:%i Missing TX LDO data
%s:%i Failed to create page content
%s:%i Failed to create RF settings from TLV string %s
GetOSMode_UICC
embedded
%s:%i WARNING : Disabling SE reader mode Power save. Temperature will rise much faster !
%s:%i Failed to allocate manifest query data
%s:%i Failed to stop routing
NFDriverHCISoftReset
NFDriverPrintPageEraseCounter
v16@?0^{phNfc_sData=*I}8
%s:%i SE uptime counter overflown
%s:%i Skipping step %d
%s:%i Received Spmi Error Register Info notification: 0x%02x, 0x%02x, 0x%02x , 0x%02x, 0x%02x ,0x%02x
watchDisplayCheck
INST
%s:%i Cal data for B is correct, flashing.
%s:%i %s : 0x%x
_NFDriverConfigureDiscovery: CRC error or response timeout
_NFDriverApplyRFConfig
%s:%i [C-RAW>] Soft Reset
%s:%i Failed to verify %s(%04X)
NFDriverCopyAndClearAssertion
%s:%i Disabling multi-tag polling, RTID=%d
A0130428282828A12E03838322A09808ACF00D8028B1B1B1A09E0C07401F9600FA002B52030000A0AF091178B0281159B02802A06A10000000000000C8000000000000000000A0682A0640600319142040009304180044804CC800B200B100AB0007FA000000350008007D00003500000E0003
NFDriverSecureElementInit
%s:%i This API is available in DL mode only
%s:%i [C-APDU>] REDACTED %ld bytes
RTM
%s:%i sealingManifestData DataCopy failed
%s:%i Got temperature notification SWIO2 / AIO2: %d, 0x%x -> %lf
[R-APDU<]
_Dispatched_NFDriverConfigureDiscovery
%s:%i Failed to set RF conf settings.
NFDriverCustomerFactoryPage.c
enable
%s:%i Follower ID unresponsive!
%s:%i No memory available
%s:%i FAILED: %s
[C-APDU>]
%s:%i SE=%d, power=%d, mailbox=%d
%s:%i Unable to get presence of AC log
%04X.%04X-%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X
%s:%i Allocation failed
%s:%i SMB Tx Blocked!
%s:%i Unexpected count of SEs : %d
%s:%i No SE for transceive
NFDriverDumpLPMDebugLog
%s:%i Failed to read headless
%s:%i Unable to create TLV config from hex string
%s:%i SE uptime failed to be queried, power=%d, mailbox=%d
%s:%i Failed to get FDR data : no data.
%s:%i Failed to get FDR key : %d
%s:%i Failed to write RF cal data B to NFCC
Generic Debug Notification received
%s:%i Unmatched tag 0x%04x
VerifyData
_NFDriverRFSettingsTLVParser
_NFDriverSetRFSettings_block_invoke
%s:%i Intf activation ntf error
%s:%i Unknown value: %d
%s:%i > eNfccParam: %d
%s:%i Failed to write RF cal data to NFCC
_Async_NFDriverIoCtl_block_invoke
NFCC debug data
%s:%i Already up-to-date
%s:%i isLoaded=%d
%s:%i Failed to setup LPCD_CFG
NFDriverSecureElementGetOSMode
_NFDriverReadMiniNVForHeadless
%s:%i Types-AB only
_Async_NFDriverGetSecureFWInfo_block_invoke
settings
_NFDriverUpdateKeyWithConfigID
%s:%i Max retries reached.
false
NFDriverGetOSUpdateLog
%s:%i failed to allocate Tx data struct
NFDriverRFSettingsStoreValueForTagAtOffset
NFDriverSecureElementGetMigrationInfoJCOP
_Async_NFDriverLoadMW_block_invoke
%s:%i Unexpected length, using custom settings...
%s:%i Unexpected length for ISO modulation : %d, expected %d
_NFDriverRFSettingsGetAntennaName
%s:%i SE Restricted Mode Enable! OS_ID = %d
%s:%i failed to allocate Tx context
Unexpected mini NV reply
%s:%i L2 logging got null info!
%s:%i Got null callback context
Virtual mode routing failure
Tag is non NDEF compliant
%s:%i Failed to stop discovery
core dump
%s:%i Failed to recover SE
NFDriverGetSecureElementInfo
NFDriverGetSWIOTemperature
_Async_NFDriverOpen_block_invoke
%s:%i Failed to create RF settings from clock TLV string %s
%s:%i E0 tag cleared successfully.
Error data :
%s:%i Failed to get FDR data : Invalid type.
%s:%i Warning : B state cal data was written with A state values. Updating tags ...
_getACLogPresence
%s:%i interfaceType:%d path:%s flags:0x%llx  aux path:%s
[HCE R-APDU<]
Customer factory page (all TLVs)
%s:%i Failed to decode plist
%s:%i Failed to allocate buffer.
%s:%i Stack logging failed with 0x%x
%s:%i Failed to get integrity check
%s:%i Pushing vendor RF settings for %s
Memory
%s:%i serial number too long: %ld
%s:%i Nuked SE gate info : %llu
%s:%i %sabling headless mode
%s:%i 
_NFDriverLogLevel2Updated
%s:%i Types-BF only
%s:%i dataClass is NULL
_NFDriverRegisterFWDLNotifications
_NFDriverConfigureVASFieldDetectShortcuts
com.apple.nfstack
_NFDriverQuerySPMIErrors_block_invoke
%s:%i RF config to set: %s
%s:%i WARNING !!!\nWARNING !!!\nWriting to Mini NV to disable headless. This is not expected outside factory.\nWARNING !!!
%s:%i CE and Reader not allowed at the same time
Feature not supported
%s:%i Found Kovio tag
%s:%i semaphore released without signal!
ADC LOW
%s:%i %s TEMPERATURE WARNING RECEIVED
%s:%i Error : invalid reader event
%s:%i %s SPMI event logging
%s:%i Failed to allocate outParams buffer.
NO
_NFDriverDebugFailedHW
_NFDriverAcquireSE
NFDriverOpen
NFDriverCrashNFCC
NFDriverRemoteDevReceiveAsync
%s:%i ProhibitTimer.Host.End
%s:%i Error ! Unexpected serial number length 
%s:%i Invalid version tag length %d
%s:%i status=0x%04X
RF deactivated
%s:%i Stack load failed with 0x%x, continuing in DL mode.
_NFDriverDisableStandby
dis
%s:%i 212kbps not supported?
%s:%i [L1] %0.6f state=0x%x tech=0x%x rssi=0x%x FelicaL1State=0x%x L1DataRxFailure=0x%x AGCRegValue=0x%x vpp=%f fs=0x%x RMRobustness=0x%04x
GetPresenseOfAttackLog_P73
_NFDriverConfigureAIOTemperatureRestriction
%s:%i Not supported on SN100V dev boards - skipping..
%s:%i Failed to merge RF settings
%s:%i Re-configuring XTAL clock source
%s:%i ESE Reader config %d -> %d
%s:%i Not interested Tag (%d) rfTech = %d
%s:%i Configuring chipscope
%s:%i phLibNfc_Mgt_RawCtrlMsgTransceive failed 0x%04llx
%s:%i Success!
%s:%i Power cycling SE success.
physical GPIO
%s:%i Unable to read AP Ticket
%s:%i phLibNfc_RemoteDev_Connect failed: 0x%04llx
%s:%i Type-B only
_NFDriverRFSettingsSetup
%s:%i AMFDRDataCopyTrustObject failed
%s:%i Invalid buffer
NFDriverSetHCETypeBConfig
_Callback_NFDriverIoCtl
%s:%i ==== UART ERROR ====
%s:%i MW Version is NULL?
CLOCK_SEL_CFG
%s:%i Invalid length for 0xCB
%s:%i ESE reader config %d -> %d
%s:%i Failed to get DieID
%s:%i [L2] %0.6f state=0x%02x mod=0x%02x rssi=0x%04x, ALMPhase=%.3f fs=0x%04x RMRobustness=0x%04x
%s:%i LPCD force always OFF
%s:%i status=0x%04llX
%s:%i failed to %sable headless mode: 0x%04llX
%s:%i Found UICC state=%d
com.apple.stockholm.callbackQueue.secondary
%s:%i Unknown poll mode profile 0x%0x, using default
%s:%i [L2] phase1Abrt=0x%02x phase2Abrt=0x%02x maxRfPulseAbrt=0x%02x successDetect=0x%02x
%s:%i Driver is null
NFDriverClearAutomaticMultiTagPollingState
NFDriverSendMFGCommand
_Callback_NFDriverSETransceive
%s:%i NFDriverConfigureReaderModeRFForMercurySigned: Unable to apply Dynamic RF settings. Trying to reset back to defaults
%s:%i LPCD assist disabled!
%s:%i TXLDO error!
%s:%i Hardware not supported
[C-APDU System>]
Reader mode prohibit timer
%s:%i Write counter is 0x%x (length = %d)
NFDriverConfigureAutomaticMultiTagPolling
%s:%i %s SMB log
%s:%i Enabling Generic-A headless mode
_Callback_NFDriverESERecovery_SetSEModePowerWired
JDI
RF_REGISTER_SETTINGS/FDT
ShMC
GetPresenceOfAttackLog
%s:%i failed to set baud rate: 0x%04llX
Success
Successfully updated page with content : 
YES
%s:%i timeout must be < %dms
%s:%i Disabling chipscope
%s:%i Reset notification. Len = %d
MFG command reply: 
%s:%i Clearing E0 tag from customer factory page.
%02X
%s:%i Failed to set XTAL clock source
%s:%i Failed to set serial log state : %u
NFDriverSetChipscope
Reboot required
%s:%i Sending 2F 0x%x to FW
%s:%i \t FLASH buffer overflow status: %d
%s:%i CFStringGetCStringPtr failed?!
-
S16@?0^{_NFCallbackMutex=QiS^v^v}8
%s:%i Enabling TypeF headless mode
SMB log: 
PMU_CFG_TAG
%s:%i \"%s\" errno=%d Unknown migration state: 0x%04x
_NFDriverConfigureSEInDownload
%s:%i Error 0x%x powering off !
%s:%i Got temperature notification SWIO1 / AIO3: %d, 0x%x -> %lf
%s:%i Found Host state=%d
disable
_Async_NFDriverSetSEAlwaysOn
%s:%i Invalid I/O selected
NFDriverIsSecureElementEnumerated
%s:%i Getting SMB log..
en
%s:%i Detected Tag (%d) rfTech = %d id= 0x%02x 0x%02x 0x%02x 0x%02x
%s:%i eSE already found
Hardware is unresponsive
REDACTED
NFDriverSecureElement_UnlockRequestInfo
UnlockRequestInfo
%s:%i rapdu length too short %d
NFDriverEnableHeadlessTestMode
%s:%i failed to allocate buffer
%s:%i Using cached dieID
%s:%i Customer Factory page has no data.
ChipID
%s:%i Not supported for UICC!
[Hex dump: length=%lu bytes] (%s:%i %s)
%s:%i Note : OS mode is System only
%s:%i Failed to disable standby mode.
NFDriverRemoteDevCheckPresence
%s:%i Cannot power cycle, request denied
NFDriverRFSettingsSetup
_NFDriverConfigureSEInDownload_block_invoke
deactivated
%s:%i enable=%d
NFDriverRemoteDeviceIso14443Transceive
SPMI Flash info
%s:%i Failed to find tag 0x%04x
NFCLD_THRESHOLD_TAG
%s:%i Failed to get instance name
TrustObjectDigest
%s:%i Failed to set routing
Aborted
%s:%i Enabling express: transit=%d vas=%d generic-a=%d single_poll=%d debug=%d block=%d 
GetCombined
NFDriverRemoteDevDisconnect
%s:%i Unclassified MIFARE (%d) found
%s:%i WTX: error, too many WTX
%s:%i Failed to clear E0 tag : %d
%s:%i Truncated tag found. Tag 0x%02x, tlvLen: %d, idx: %d, len: %d
stockholm
NFDriverSecureElementGetOSUpdateLog
NFDriverLoadStack_block_invoke
%s:%i Failed to set Prox config : 0x%08llx
%s:%i wantsFieldDetect=%d wantsPolling=%d wantsExpress=%d eSE=%d host=%d wantsEcpUpdate=%d
_Dispatched_NFDriverGetStackBreadcrumb
NFDriverRemoteDevFormatNdef
Disabling
%s:%i SWP-proc: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
_Async_NFDriverClose_block_invoke
_NFDriverRFSettingsGetEDTAntennaName
%s:%i LPCD assist completed successfully
%s:%i setting rate: %d
%s:%i Failed to write page : 0x%04llx
%s:%i Failed to set RF settings.
APC_CONTROL_TAG
CLOCK_SEL_CFG_SN100v
%s:%i No sealing manifest
%s:%i Failed to get TO_BEFORE_STDBY_CFG.
%s:%i LastAPI=0x%02X, LastAPIStatus=0x%04X DebugInfo=0x%016llX
%s:%i Invalid length for 0xC8
%s:%i %d%% ASK modulation requested.
numRoutes <= MAX_NFCC_ROUTING_ENTRIES
%s:%i eSE, enabled=%d
UART Error
_Callback_NFDriverNotifySE_block_invoke
%s:%i Host did not re-enumerate
SPMI comms error
%s:%i Failed to set eSE to wired mode
seid
%s:%i SEID in manifest is %@
LPCD_CONFIG_TAG
_EosParseManifestQuery
stockholm-spmi
IsOSReady_Eos
NFDriverTriggerDelayedWake
%02X.%02X-%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X
%s:%i RTID Debug mode enabled
%s:%i LPCD force always ON
UNKNOWN
%s:%i Resource error
%s:%i %s SE in DL mode
%s:%i Failed to setup delayed wake, status = 0x%04X
%s:%i Error 0x%x using API %d - requires a reboot !
_NFDriverEnableCRC
_NFDriverSetGenericATxHappenedTimeout
%s:%i Num Tags Added=%d, Detected=%d, Removed=%d, Not Interested=%d
%s:%i Received %s debug data from NFCC (%u bytes)
%s:%i ***WARNING*** Express mode is requested; express won't work under this config!!!
NFDriverRestartDiscovery
%s:%i Enabling ECP mode since no other is selected.
<empty>
FDT_CONFIG
%s:%i Certificate too long: %zu
%s:%i This feature is restricted to internal builds.
NFDriverUpdateJCOPVersion
%s:%i failed to get stack info
%s:%i Failed to %s NFCC CRC
Dis
%s:%i Unexpected length : %d
%s:%i host: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
%s:%i type=0x%x
_NFDriverTranslateRF
%s:%i unknown express mode type (%d)
NFDriverSetSecureElementPower
NFDriverGetUniqueFDRKey
_Callback_NFDriverESERecovery_SetSEModeResume
%s:%i Type-B disabled
[TXLDO]
NFDriverSetReaderModeRFGain
REGISTER UPDATE
%s:%i Enabling chipscope
CRC error
%s:%i NFCEE powered off
NFDriverSetTemporaryPollingPeriod
%s:%i Full HCE can't be used with polling
_NFBootStopInterruptCallback
_NFDriverCreateInstanceNameForClassData
GetManifestQuery_Eos
%s:%i ProhibitTimer.SE.Start
_Async_NFDriverSetStandbyMode
%s:%i RF settings is too short: length=%zu
%s:%i %s(%04X) is OK
%s:%i Invalid value for 0x%X, len=%ld
%s:%i setting 424
No syscfg cal
%s:%i new SuicaEntrySysCode: code 1 enabled: %d, code 1: %04X; code 2 enabled: %d, code 2: %04X
%s:%i Failed to read clock register
_Callback_NFDriverNotifyDiscovery
com.apple.uart.stockholm
Invalid parameter
%s:%i NFCC flash write query
NFDriverConfigureSPMIIRQ
GetPresenceOfAttackLog_Eos
%s:%i tag removed
NFDriverSetSecureElementAlwaysOn: CRC error or response timeout
%s:%i \"%s\" errno=%d Payload length overflow error. 
%s:%i Values different. Will apply new values
%s:%i Failed to get platform identifier
%s:%i major = %d, minor %d, build = %d
[FLC_TRIMMING failed]
%s:%i MFW factory page config notification received : NULL
%s:%i Invalid format
NFDriverGetInternal(driver)->hwInfo != NULL
A0130428282828A12E03838322A09808A4580D80286A6A6AA09E0C07401F9600FA002B52030000A0AF091178B0281159B02802A06A100000000000003C000000000000000000A0682A0640600319142040009304187A1D863D9C00A30077007D0007FA000000350008007D00003500000E0003
NFDriverSecureElementGetCertificates
NFDriverRemoteDevWriteLockNdef
NFDriverRemoteDevReadNdef
%02X.%04X-%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X
NFDriverReadATETrimVersion
seal
_NFDriverEosUpdateJCOPVersion
%s:%i Selecting OSU
%s:%i uptimne is %llu
NFDriverRemoteDevCheckNdef
[R-APDU UICC<]
%s:%i Clearing Multitag info state
%s:%i [L2] %0.6f state=0x%02x 15693state=0x%02x tech=0x%02X status=0x%02x data=%s
%s:%i \t pInfo (pointer to L2Debug Info) is NULL!
NFDriverGetFactoryPage
_NFDriverRegisterFWDLNotifications_block_invoke
%s:%i SE Restricted Mode Exit! OS_ID = %d
NFDriverGetControllerInfo
_Async_NFDriverConfigRoutingTable_block_invoke
%s:%i Failed to get antenna name from EDT : %s
actualRfConfig
FDR: 
%s:%i Failed to get CF types
NFDriverSecureElementCreate
%s:%i %s reader mode dynamic BBA control
%s:%i SE in recovery
%s:%i ProhibitTimer.Host.Start
%s:%i Invalid clock register response
se
%s:%i Not enough storage for cert %d (tag 0x%x). Len = %lu, type = %d !
%s:%i Got SE Removed with status %d
%s:%i Failed to set ECP VAS polling: 0x%08llx
%s:%i Disabling standby for debugging
updateInfoData
_getKeySize
%s:%i phLibNfc_RemoteDev_Receive failed 0x%04llx
%s:%i ---- Core Dump Addr ----
_NFDriverRFTechToTagType
_NFDriverConfigureTemperatureNotifications
%s:%i num_dev=%d, status=%d
antenna
%s:%i No vendor RF settings found for %s!
%s:%i No data received.
%s:%i phLibNfc_Mgt_GetNfccParams failed 0x%04llx
NFCallbackMutexCreate
%s:%i CRC error
NFDriverSetHeadlessMode
%s:%i ==== COMM ERROR ====
%s:%i status=0x%04llX, previous state %d
%s:%i NFCC does not support Continuous Wave
%s:%i BFAR=0x%04x CFSR=0x%04x MMFAR=0x%04x
%s:%i Set output read buffer empty. Not applying new values
%s:%i \t RAM buffer overflow status  : %d
SealingManifest
_Async_NFDriverSetStandbyMode_block_invoke
%s:%i F0 version is 0, treating as unprogrammed.
%s:%i failed to get config TLV
%s:%i EUICC = %s
%s:%i ISD sequence counter %d does not match migration update counter %d
%s:%i Flags requested DL mode only.
_NFDriverRegisterNCINotifications_block_invoke
%s:%i > phLibNfc_Mgt_GetNfccParams
%s:%i SELECT OS Update AID
MFW factory page config notification received
%s:%i LPCD false detect counter overflown
%s:%i ---- TICKS ----
_Dispatched_NFDriverGetStackDebugInfo
NFDriverSecureElementTransceive
%s:%i ESE reader as config set (%d / %d)!
_Callback_NFDriverDelayedWake
%s:%i JCOP1 = %s
%s:%i Received empty %s debug info from NFCC
NFDriverSecureElement_IsOSReady
%s:%i Invalid manifest length
GetOSUpdateLog_UICC
%s:%i Device in degraded mode. Wired not available.
NFDriverPreventReset
%s:%i phLibNfc_RemoteDev_FormatNdef failed: 0x%04llx
NFDriverRemoteDevGetMiFareInfo
%s:%i Fail to get controller info
%s:%i Failed to set A1DF: 0x%08llx
%s:%i Platform does not have boot measurements
%s:%i enable: %d
FW DL pending
NFDriverDumpLPMDebugLog_block_invoke
%s:%i Disabling field detection for Single Poll express
%s:%i Setting already present - not updating
_NFDriverConfigureVASFieldDetectShortcuts_block_invoke
%s:%i MFW Notification received
%s:%i Enabling full HCE routing
[C-APDU Guest>]
%s:%i Manifest Query is not supported on this OS version (sequence counter: %d)
%s:%i Error 0x%x using API %d - requires a new firmware !
%s:%i Get Debug Info failed: %04X
NFDriverRemoteDeviceFelicaTransceive
NFDriverSecureElementGetAttackCounterLog
NDEF message size is over the limit
%s:%i Error : function at index %d will never run
%s:%i Unknown SE removed: reason=0x%02x, other=0x%02x
%s:%i Failed to stop polling
%s:%i WTX: no info
%s:%i failed to get clock TLV
%s:%i Unsupported hardware.
Failed to parse TLV 
%s:%i Invalid context 0x%02x
NFDriverNFCCPowerOff_block_invoke
%s:%i Completion pointer was null
%s:%i NFHardwareGetHWConfigTLVs() returned success but out string is null!
%s:%i SELECT returned error: 0x%04x
%s:%i Unknown chip model ID !
driver != NULL
%s:%i Multitag state query
_copyTagInfoFromDevice
FELICA_HIGHZ_RX_TAG
Local
/System/Library/Caches/com.apple.factorydata
%s:%i configuring Felica transaction end pattern for applet ver 2.0
%s:%i Enabling multi-tag polling, RTID=%d
%s:%i phLibNfc_RemoteDev_Transceive failed 0x%04llx
GC_RSSI_THRESHOLD_TAG
SetPower_UICC
%s:%i Allocation failure
%s:%i Wrong interfaceType %d - cannot continue!
default
A0130428282828A0AF09116FB0281159B02802A098086FF10B8028171717A09E0C07401F9600FA002B52030000A12E03838322A0682A06406003191420400093041880578057E000C000C000A00007FA000000350008007D00003500000E0003A06A1000000000000064000000000000000000A0A8400033
GetOSInfo_Eos
NFDriverSecureElementGetOSInfoJCOP
%s:%i Multi tag status notification received
Die ID :
UniqueChipID
NFDriverTriggerCoreDump
%s:%i LPEM flash writes disabled! Headless mode will not be updated on the device.
_NFDriverConfigureRoutingTable
%s:%i polling=%d emulation=%d field=%d express=%d resume=%d reader config=%d
_Callback_NFDriverAntennaSelfTest
%s:%i Using local RF settings
A0130419191919A00D03610982A06A1000000000000078000000000000000000A09808EFB50B8019171717A0AF0911FFF419117DA01902A09E0C07001D960090012BD0070000A0940A072003a200314f001902A0682A064060031914204000930418FF7FFF7F8D096E06D8076B0507FA000000350008007D
%s:%i Unexpected length: %zu
_Callback_NFDriverNotifyGeneral
%s:%i Failed to configure Type A emulation : 0x%04llx
%s:%i HFSR=0x%04x SFAR=0x%04x SFSR=0x%04x
_NFDriverRFSettingsIsFDRSealed
%s:%i DL session already open.
com.apple.spmi.nfc
NFDriverSetReaderModeDynamicBBA
%s:%i HFLR=0x%04x PSP=0x%04x MSP=0x%04x
%s:%i Device does not require RF settings changes
%s:%i Failed to init se of type %d
NFDriverSecureElementGetDataWithOS
_NFDriverConfigureBaudRate_block_invoke
%s:%i Multitag structure is missing
%s:%i Failed to VEN reset !!!!! : 0x%04X
%s:%i Warning : Standby disabled - skipping enablement.
%s:%i Update successful, previous session state was %d
%s:%i failed to set vGPIO tag (0xA008)
%s:%i phLibNfc_RemoteDev_CheckPresence failed: 0x%04llx
[R-APDU Guest<]
NFDriverClearFactoryPageE0Tag
%s:%i Temperature restrictor configured
%s:%i No compensation applied due to underflow, poll phase duration (ms): %d
NFDriverISO15693SetDataRate
%s:%i %s
%s:%i failed to register for notifications: 0x%04llX
%s:%i 0x%02X TLV doesn't match
%s:%i Failed to load hw
NFDriverRFSettingsReadSetting
%s:%i isLoaded=%d flags = 0x%x
%s:%i Interval must be < 900 ms
%s:%i Failed to set rf property:0x%02x status:0x%08llx
FollowerID is unresponsive
_NFDriverLogLevel1Updated
%s:%i Failed to power off eSE
NFDriverGetPowerCounter
%s:%i Failed to query chip info. Bailing
NFDriverGPIOSetPMUStandbyPowerEnabled
%s:%i enable %02X
%s:%i ---- Core Dump ----
disp0
%s:%i Failed to get update info
%s:%i phLibNfc_Ndef_Write failed: 0x%04llx
%s:%i Failed to get driver info
NFDriverCustomerFactoryPageIsUnlocked
%s:%i Failed to get MG types
%s:%i missing creator for SE type %d
_Async_NFDriverUnloadStack_block_invoke
%s:%i Can't send to OS %d. Not available.
Firmware error
%s:%i \t ### HLM debug Log ###
%s:%i Failed to get factory page : %d
%s:%i Using default antenna name %s
NFDriverRFSettingsSetupSigned
%s:%i amfdr is NULL
TrustObject
PC
Command rejected
_Async_NFDriverConfigureRFLogging_block_invoke
%s:%i Failed to setup routing 0x%04llx
%s:%i ---- WATCHDOG ----
%s:%i Failed to get serial number
%s:%i Cond init failed : %d
Unexpected write counter reply
%s:%i Error : invalid response.
Reading registers
SPMI RAM
SE Recovery Failed
NFDriverGetUnlockRequestInfo
SPMI RAM info
Core Dump
%s:%i Failed to restore SE mode : 0x%x
%s:%i Failed to set HOST to virtual mode
_NFDriverConfigureReaderModeRFForMercurySigned
com.apple.stockholm.callbackQueue.primary
%s:%i Requested read size is over the limit
_NFDriverSetISO15693LocalDataRate
%s:%i Status = 0x%x, param=%d
%s:%i GetPresenseOfAttackLog will only work in JCOP mode
%s:%i Unable to create aid needed for selecting ISD
NFDriverDumpUART_block_invoke
%s:%i Received SRAM REPAIR %s notification
%s:%i Mini NV headless is 0x%x (length = %d)
%s:%i Returned error: 0x%04x for (0x%x/0x%x)
%s:%i Re-using exit threhold
%s:%i [R-RAW<] Soft Reset
%s:%i (%s) mode=%s
%s:%i Primary = %s
GetOSMode_Host
%s:%i \"%s\" errno=%d Unable to allocate memory for capdu. 
%s:%i setting 212
%s:%i Failed to push builtin RF settings.
%s:%i Failed to get ManifestQuery
%s:%i SMB debug : NULL
NFDriverConfigureVASPolling
NFDriverEnableAntiRelay
NFDriverSecureElementSelectWithOS
A0130419191919A00D03610982A06A1000000000000078000000000000000000A09808D9DB098019171717A0AF0911FFF419117DA01902A09E0C07001D960090012BD0070000A0940A072003a200314f001902A0682A064060031914204000930418FF7FFF7F94038404D902840307FA000000350008007D
%s:%i Boot status=%d\n                        ROM=0x%x, HW Version=0x%x, Chip version=0x%04X, Variant=%x, ModelID=%x\n                        Protected status=%x, Lifecycle:{scratch=0x%04X,protected=0x%04X}, vendorFW={scratch=0x%04X,protect
NFDriverDisableBoost
%s:%i Could not find status container
NFDriverDebugDumpMemory
%s:%i \t Number of L2 debug msgs: %d
_Async_NFDriverSetNfccParams_block_invoke
%s:%i Failed to get RF settings registers.
NFCSTATUS_OK == ioctlStatus
%s:%i Generic Debug Notification received without data
NFDriverGetRFState
%s:%i Frame RF INTF activated
_NFDriverGetSecureFWInfo
_Async_NFDriverSetSEMode_block_invoke
RF data from controller
%s:%i Failed to configure RF logging : 0x%04llX
_NFDriverSetRFProperty
NFDriverDisableLPCDAssist
_createSE
%s:%i F0 has testing bit (0x%04x), will overwrite.
A10A0151
%s:%i JCOP branch: %d.%d
%s:%i EMVCO field collision detected
NFDriverClose
_Callback_GetNfccParamsCb
NFDriverFactoryPageHasExpectedConfigForTag
Assert info
ShSA
%s:%i Device does not support this feature
NFDriverAntennaSelfTest
%s:%i Headless is 0x%x (length = %d)
%s:%i Failed to verify sealing : %ld
%s:%i [L1] StandbyEventType=0x%x RegValue=0x%x
_Async_NFDriverGetBootMeasurements_block_invoke
%s:%i Got FDR data but an error is set : %ld - %s
GetAttackCounterLog_UICC
%s:%i Failed to set ECP Frame
NFDriverEnableFelicaTxEndPatternV2
%s:%i JCOP OS Update Mode detected
NFCC is not working
%s:%i Got %x (%d), returning %lf
%s:%i Non-default multitag polling period: %u
%s:%i Wrong 'eNfccParam' received!
%s:%i Invalid length for 0xC9
%s:%i Polling config is using Custom ECP
driver && info
%s:%i Configuring Fury Multitag ECP Frame
_NF_AMFDRSealingMapCopyLocalDataForClass
%s:%i Enabling reader mode dynamic BBA control
NFDriverSetTypeATagDataRate
Not Found
host
%s:%i Failed to write IRQ
bics-param-set
RX_CTRL
%s:%i Note : OS mode is JCOP
%s:%i UICC did not re-enumerate
%s:%i SE=%d, JCOP=%d eUICC=%d power=%d, mailbox=%d
%s:%i Error : Allocation failure
%s:%i Failed to read miniNV
%s:%i mode=0x%x
%02X.%02X
%s:%i Failed to setup SERM power save
_NFDriverConfigureBaudRate
%s:%i Embedded SE removed: reason=0x%02x, other=0x%02x
%s:%i interfaceType:%d path:%s flags:0x%llx
alternate
%s:%i Failed to resume SE mode
%s:%i Failed to push Cal to NFCC : 0x%04llx
_NFDriverSetControllerInfo
%s:%i No NDEF write data provided
NFDriverSecureElementGetOSInfo
NFCallbackMutexWait timeout
fwVersion
NfcB
_NFDriverNukeSEGateInfo
%s:%i timeout must be < %d
hammerfest-spmi
%s:%i Unknown rate %d
Config
%s:%i Disabling boost
Expected tag value : 
%s:%i Unable to do any RF operations. Returning false.
_NFDriverConfigureDiscovery
[Reader R-APDU<]
%s:%i Mutex already signalled timeout! CB status: %04x
%s:%i failed to get config TLV JDI
Stack error
%s:%i failed to set NTAG5 local rate: 0x%04llX
_getCertificateType
%s:%i Failed to configure Temperature restrictor : 0x%04llX
NFDriverReadPageEraseCounter
%s:%i Failed to set A11E tag: 0x%04llx
[lpcd]
SUCCESS
%s:%i cfg=0x%04x addr1=0x%08x len1=0x%04x addr2=0x%08x len2=0x%04x
_NFDriverLogLPCDDebug
%s:%i Step %d error : 0x%x
NFDriverSetPollingProfile
NFDriver.c
%s:%i Polling cfg: A:%d B:%d F:%d 15693:%d S:%d S2:%d S3:%d CustomECP:%d VAS_ECP:%d frameRF:%d
%s:%i SE %d does not support wired mode
%s:%i eSE power-on failed! (%d/%d)
%s:%i Platform id too long: %ld
%s:%i CRC error 0x%x
%s:%i No remote tag handle provided
_NFDriverRFSettingsApplyFDR2CalData
%s:%i hw-config-tlvs: %s
_NFDriverSetStandbyMode: CRC error or response timeout
_NFDriverConfigureReaderModeDynamicBBA
Insufficient resource
%s:%i RF=%d
NFDriverGetHeadlessModeFlags
%s:%i Response time : %f us (%d), PICC Response: 0x%04X, PCD response = 0x%04X
%s:%i status=0x%04X for event %d
%s:%i SE reader mode event : {se=0x%x, startEnd=%d, poll=0x%x, protocol=0x%x}
_NFDriverRebootRemovedSE
NFDriverSecureElement_GetAttackCounterLog
%s:%i Missing input tagInfo
%s:%i setting 848
%s:%i R0=0x%04x R1=0x%04x R2=0x%04x R3=0x%04x R12=0x%04x
%s:%i Unable to alloc memory 
NFCallbackMutexWait
En
com.apple.spmi.nfc.hammerfest
%s:%i ---- HARD FAULT ----
_Async_NFDriverDumpMemory_block_invoke
%s:%i Customer Factory page is NULL.
%s:%i No custom RF settings found!
%s:%i Failed to %s SE in DL mode.
com.apple.stockholm.driverQueue.secondary
[C-APDU UICC>]
_NFSpmiErrorCallback
_NFDriverRFSettingsValidate
GetAttackCounterLog_P73
deactivate
%s:%i Attempt %d of %d
NFDriverSetConfiguration
ctx
CEF_FILTERING_CONFIG_TAG
Degraded mode
%s:%i Idle=%d
%s:%i old SuicaSystemCode: code 1 enabled: %d, code 1: %04X; code 2 enabled: %d, code 2: %04X
_Callback_NFDriverESERecovery_SetSEModePowerOff
_NFDriverConfigureBBClockSource
HW Reset
ADC HIGH
%s:%i Routing changed
_resumeSEMode
%s:%i Failed to get RF settings; status=0x%04llX.
/mnt1
%s:%i Generic error : 0x%04X
ECP Frame
%s:%i Got error 0x%2X
%s:%i failed to validate EEPROM: 0x%04llX
%s:%i TIMEOUT!
%s:%i Dropping temperature notification
%s:%i Unknown notification: 0x%x
%s:%i Felica command is too large: %ld bytes
_NFDriverSetSecureElementRouting
%s:%i setting 106
%s:%i CRC error or response timeout - 0x%04llx
%s:%i SE recovery complete. Leaving SE in wired
SPMI Event log: 
%s:%i Failed to write RF cal data A to NFCC
%s:%i Warning : B state cal data was written with A state values. Skipping ..
NFDriverSecureElement_GetOSUpdateLog
%s:%i Returned error: 0x%04x
v8@?0
Bermuda
%s:%i Error : unable to write to transition registers
DataDirectory
NFDriverSecureElement_GetOSInfo
%s:%i Faled to configure Type B emulation : 0x%04llx
_NFDriverGetSecureElement
%s:%i Failed to read registers from NFCC : 0x%4llx
%s:%i Sealing status is %d
driver->isHammerfest == false
%s:%i Failed to %s continuous wave
%s:%i RF=0x%04x, SWP=0x%04x, Kernel=0x%04x, Host=0x%04x, SMB=0x%04x, LowPwr=0x%04x, sys=0x%04x
%s:%i Not enough space allocated to store all page counters
%s:%i WARNING : power cycling SE
%s:%i Resolve key type from config
Deactivating
Virtual
PMU_CONFIG_TAG
%s:%i Unexpected status: 0x%X
%s:%i Setting polling period to %u
%s:%i [L2] %0.6f command=0x%02x debug=0x%02x rssi=0x%04x
%s:%i Failed to fully power off eSE
%s:%i Failed to get RF conf settings.
Thresholds are :
%s:%i Enabling VAS CODES
SMB debug: 
NFDriverSetExpressConfig
NFDriverRemoteDevWriteNdef
%s:%i PC: %d
_Async_NFDriverGetFirmwareVersion_block_invoke
NFDriverDumpSPMIEventLog
%s:%i Invalid logging value
%s:%i Failed to get page : 0x%04llx
%s:%i deselected
NFDriverRedactLogging
NFDriverEnableSMBLogging
%s:%i Type-A only
Wired
_NFDriverSetISO15693LocalDataRate_block_invoke
GetOSMode_P73
%s:%i Transceive failure
NFDriverDisableHeadlessModeMiniNV
NFDriverResetFWFlags
%s:%i Idle counter overflown
%s:%i enabling LPCD assist
%s:%i Found eSE state=%d
%s:%i Get stack breadcrumb failed
No module cal
%s:%i LR=0x%04x PC=0x%04x XPSR=0x%04x
%s:%i Failed to power cycle SE... it's not coming back folks
%s:%i Not supported for Host SE!
%s:%i ERROR: no value !
%s:%i MSPL=0x%04x PSPL=0x%04x PMR=0x%04x
%s:%i Unable to get RF Conf register values
NFDriverRFSettingsPushSetting
%s:%i WARNING ! Do not send data to JCOP in unknown state !!!!!
%s:%i Invalid parameter
NFDriverRemoteDeviceIso15693Transceive
_Callback_phLibNfc_Mgt_GetNfccParams
NFDriverHWSettingsSetup
PHASE_OFFSET_TAG
%s:%i SE %s in download mode
%s:%i 0x%02X TLV length doesn't match expected (%d)
%s:%i Query AC log presence failed with 0x%02X
%s:%i Incompatible firmware !
%s:%i eSE Restricted Event %d %d
%s:%i ESE reader discovery change requested %d -> %d!
[R-APDU System<]
%s:%i Failed to allocate TLV data
NFDriverEnableSERMPowerSave
%s:%i Unknown SE type %d
%s:%i select returned error: 0x%04x
%s:%i Setting MultiTag Config. A=%d S=%d S2=%d S3=%d V=%d VASUPA=%d Retries=%d TlvId=%d, debugMode=%d pollDuration=%d pollRetries=%d
_NFDriverSetSEMode: CRC error or response timeout
%s:%i failed to enable VAS CODES: 0x%04llX
%s:%i ==== NFCC/SE TEMPERATURE CONDITION EXITED ====
Target connection lost
%s:%i No SEID in manifest
%s:%i Unhandled tag type 0x%04x
Unexpected result
%s:%i SE power up failed. Trying to power off
%s:%i Failed to set RF config set1.
Writing customer factory page :
%s:%i Invalid offset %d for tag 0x%04x
%s:%i %s reader mode static BBA control
%s:%i phLibNfc_AntennaSelfTest FAILED : 0x%llx
%s:%i Error at step %d, re-initializing
driver
SE communication error
%s:%i MultiTag false detect counter overflown
NFDriverContinuousWave
%s:%i Marking ESE reader as disabled!
%s:%i Error ! Received boot stop interrupt.
%s:%i Failed to allocate se of type %d
%s:%i Empty factory page
_NFDriverUpdateFactoryPage
%s:%i Did not find version tag!
GetManifestQuery_P73
%s:%i Unexpected element found in status container: 0x%04x
%s:%i Unexpected length for TO_BEFORE_STDBY_CFG : %d
%s:%i JCOP uptime counter overflown
%s:%i [L1] %0.6f state=0x%x tech=0x%x rssi=0x%x FelicaL1State=0x%x L1DataRxFailure=0x%x AGCRegValue=0x%x vpp=%f ALMPhase=%.3f fs=0x%x RMRobustness=0x%04x
_NFDriverRFSettingsValidateTag
%s:%i ==== HARDWARE RESET ====
NFCC is in DL mode
%s:%i Failed to read write counter
%s:%i Enabling ECP headless mode
_NFDriverSetSEMode
%s:%i Host already found
%s:%i Incorrect T1 %ud, using 320usec!
NFDriverGetPowerCounter: CRC error or response timeout
%s:%i Failed 0x%04llx
%s:%i \"%s\" errno=%d Invalid L1 standby wake event 0x%x
%s:%i Failure for tag 0x%x
MW requested VEN reset
FAILURE
%s:%i Failed to get data
%s:%i Extending timeout 10 seconds. User has requested us to avoid crashing.
%s:%i Failed to update discovery
_NFDriverCustomerFactoryPageFindTLV
%s:%i Forcing FDR path.
%s:%i TLV overrun at tag 0x%02x
%s:%i %s CRC
%s:%i XTAL start error received
%s:%i [L2] %0.6f event=0x%02x debug=0x%02x
NFDriverSecureElement_GetManifestQuery
%s:%i Unknown SE: %d
%s:%i Express cfg: Transit:%d Access:%d Generic-A:%d SinglePoll:%d Block:%d Debug:%d
%s:%i Enabling single poll headless mode
%s:%i [L2] ms=0x%02x µs=0x%02x LMA=0x%02x BBA=0x%02x
%s:%i No SE handle
txContext != NULL
_Callback_NFDriverSERawTransceiveWTX
HW
%s:%i NFDriverConfigureReaderModeRFForMercurySigned: Unable to apply Default RF settings
%s:%i Customer Factory page is locked.
%s:%i Warning : Standby disabled.
NFDriverRemoteDevSend
NFDriverSecureElementGetPresenceOfAttackLog
Enabling
_Callback_NFDriverSETransceiveWTX
%s:%i Unable to find config tag info for tag 0x%02x
NFDriverCopySEIDFromFDR
%s:%i Incorrect manifest query length: %zu
%s:%i CW detected!
NFDriverSetPollingConfig
%s:%i Failed to create data (%lu bytes) with result
No response from tag
%s:%i ---- ASSERT ----
_NFDriverReadHeadless
%s:%i AC log exists, but supplied output parameter is NULL.
%s:%i Failed to register notification callback.
NFCC LOW
NFCC HIGH
_NFDriverSetStandbyMode
%s:%i No command APDU provided
%s:%i Not supported - skipping on this hardware
%s:%i Unknown se ID: %d
NFDriverEnableAutomaticRFOverride
%s:%i mailbox: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
%s:%i Session State=%d,                     HW Version=0x%x,                     ROM=0x%x,                     Model=0x%x,                     FW=%x.%x,                     MW=%x.%x r%llx,                     Chip=%x                     Lif
%s:%i BPMR=0x%04x FMR=0x%04x CR=0x%04x
VGPIO_CONFIG_TAG
%s:%i Memory error trying to update property: 0x%02x
%s:%i Invalid opcode 0x%x
%s:%i No RF settings.
%s:%i eSE did not re-enumerate
%s:%i Failed to select
%s:%i Reading Die ID ...
Tag is halted
%s:%i RF counter overflown
_NFDriverRFSettingsNameForTag
_NFDriverLoadMW
%s:%i Queuing exit due to timeout
%s:%i Failed to get boot measurements
%s:%i Num Tags Detected=%d, Num Tags Not Interested=%d
%s:%i Bad response APDU length %d
%s:%i [L2] %0.6f response=0x%02x status=0x%04x debug=0x%02x vpp=%f ALMPhase=%.3f
%s:%i %s configured successfully
NFDriverFactoryPageHasProductionContent
_NFDriverRFSettingsReadCalDataFromFDR
%s:%i Enabling write counters
%s:%i Setting polling modulation limit to 100%%
_Callback_NFDriverNotifySE
%s:%i Missing CE interface type
NFDriverWriteFactoryPage
%s:%i F0 TLV too short (%d), treating as unprogrammed.
%s:%i AID_MANIFESTQUERY returned error: 0x%04x
_NFDriverEnableLpcdAssist
%s:%i Failed to configure Temperature monitoring : 0x%04llX
_Callback_NFDriverNotifyHCE
NFDriverRemoteDevConnect
%s:%i phLibNfc_RemoteDev_CheckNdef failed: 0x%04llx
%s:%i phLibNfc_Ndef_Read failed: 0x%04llx
Power Off
%s:%i Using EDT RF settings
_NFDriverValidateEEPROM
%s:%i configs are identical - skipping.
%s:%i Type-F only
%s:%i Invalid update info length: %zu
Pad voltage extra info
NFDriverRFSettingsGetVendorParameters
%s:%i eSE not in wired mode
NFDriverReadDieID
%s:%i RF-proc: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
_NFDriverRFSettingsGetRFPropOnce
%s:%i Invalid length : no room for tag
%s:%i Invalid length for tag 0x%x
NFDriverSetRFState
_NFDriverLogAssert
%s:%i Headless mini NV already set
_Callback_NFDriverSendMFGCommand
%s:%i F0 has production content (version=0x%04x, type=0x%04x), preserving.
%s:%i Unexpected event: %x
%s:%i Failed to get RF settings.
%s:%i Changing RF settings to default
GetOSUpdateLog_Host
_NFDriverChangeISO15693Modulation
%s:%i [L2] %0.6f code=0x%04x
_NFDriverConfigureHardware
%s:%i \t Number of HLM debug msgs: %d
%s:%i EDT antenna name: %s
%s:%i Restricted Mode detected
_Async_NFDriverValidateEEPROM_block_invoke
SE OS reset
%s:%i > phLibNfc_Mgt_GetNfccParams FAILED
%s:%i UICC already found
%s:%i Error, trying to power cycle the SE.
NFDriverSecureElement_GetOSMode
%s:%i Not interested Tag (%d) rfTech = %d, rfError = %d, numTagsDet = %d
%s:%i halted
%s:%i Chipscope buffer empty
%s:%i Failed to query FW info !
%s:%i Command is too large: %ld bytes
_Callback_NFDriverRemoteDevGetMiFareInfo
%s:%i failed to get config TLV LGD
NFDriverStackInit.c
%s:%i ==== PLL UNLOCKED ====
Transceive Failure
_NFDriverRFSettingsApplyFDR3CalData
GetOSUpdateLog_Eos
%s:%i remote dev list is invalid
[HCE C-APDU>]
%s:%i [R-APDU<] REDACTED %ld bytes
%s:%i [L2] %0.6f state=0x%02x mod=0x%02x rssi=0x%04x, extraInfo=0x%0x fs=0x%04x RMRobustness=0x%04x
%s:%i Marking ESE reader as enabled!
_NFDriverGetReaderModeRFConfigRegs
%s:%i Unable to extract trust object digest from AP Ticket
ESE LOW
%s:%i Polling config is not using ECP
NFDriverSetSecureElementAlwaysOn
NFDriverRemoteDevReceive
%s:%i Resuming SE mode to 0x%x (stored routing mode is %d)
_Callback_NFDriverRemoteDevReceiveAsync
hammerfest
%s:%i Failed to get RF settings; status=0x%04llX
%s:%i phLibNfc_SE_ActModePwrOff is only available on ese - switching to ActModeOff
LGD
%s:%i %s(%04X) skipped
%s:%i Restoring RF
_NFDriverRFSettingsWriteSignedCalData
_seTypeToID
%s:%i Invalid length for 0xCA
NFDriverLoadStack
%s:%i Flash counter exceeded notification. This is NOT expected unless you live in the 22nd century or later. File a radar and get a new device.
%s:%i Invalid param
NFDriverSecureElementSendCommandToOS
%{public}s:%i CRC error
%{public}s:%i Generic Debug Notification received without data
%{public}s:%i Unknown rate %d
%{public}s:%i Using default antenna name %s
%{public}s:%i Failed to setup routing 0x%04llx
%{public}s:%i Forcing FDR path.
%{public}s:%i Note : OS mode is JCOP
%{public}s:%i Failed to %s SE in DL mode.
NFDriverRemoteDevCheckNdef
%{public}s:%i %02d: %04d %04d %04d %04d %04d %04d %04d %04d
%{public}s:%i failed to set NTAG5 local rate: 0x%04llX
%{public}s:%i Failed to push builtin RF settings.
%{public}s:%i HCE Register error = 0x%04x
ANTI_RELAY
%{public}s:%i Unexpected size of AID prefix : %d.
%{public}s:%i Failed to set Prox config : 0x%08llx
%{public}s:%i Failed to read registers from NFCC : 0x%4llx
%{public}s:%i Query AC log presence failed with 0x%02X
%{public}s:%i Invalid version tag length %d
%{public}s:%i [L2] phase1Abrt=0x%02x phase2Abrt=0x%02x maxRfPulseAbrt=0x%02x successDetect=0x%02x
%{public}s:%i Failed to get ManifestQuery
%{public}s:%i AID_MANIFESTQUERY returned error: 0x%04x
%{public}s:%i Failed to query chip info. Bailing
%{public}s:%i Skipping step %d
%{public}s:%i Temperature monitoring configured
%{public}s:%i Update successful, previous session state was %d
%{public}s:%i Failed to set serial log state : %u
%{public}s:%i ---- Core Dump Addr ----
%{public}s:%i major = %d, minor %d, build = %d
%{public}s:%i Setting already present - not updating
%{public}s:%i ==== COMM ERROR ====
%{public}s:%i remote dev list is invalid
%{public}s:%i setting 424
%{public}s:%i new SuicaEntrySysCode: code 1 enabled: %d, code 1: %04X; code 2 enabled: %d, code 2: %04X
%{public}s:%i Failed to power off Host
%{public}s:%i CFStringGetCStringPtr failed?!
%{public}s:%i Failed to allocate outParams buffer.
%{public}s:%i amfdr is NULL
%{public}s:%i Invalid param
%{public}s:%i [C-APDU>] REDACTED %ld bytes
%{public}s:%i Enabling chipscope
%{public}s:%i [L2] %0.6f code=0x%04x
%{public}s:%i Unknown se ID: %d
%{public}s:%i SELECT: ISD
%{public}s:%i Received SRAM REPAIR %s notification
%{public}s:%i Failed to get controller info
%{public}s:%i enable=%d
%{public}s:%i Types-AF only
%{public}s:%i LPCD assist completed successfully
%{public}s:%i Missing input tagInfo
%{public}s:%i RF=0x%04x, SWP=0x%04x, Kernel=0x%04x, Host=0x%04x, SMB=0x%04x, LowPwr=0x%04x, sys=0x%04x
%{public}s:%i Got null callback context
%{public}s:%i phLibNfc_Ndef_Read failed: 0x%04llx
%{public}s:%i failed to allocate buffer
%{public}s:%i Failed to get driver info
%{public}s:%i Failed to power off eSE
%{public}s:%i SE %s in download mode
%{public}s:%i Received Spmi Error Register Info notification
%{public}s:%i Failed to configure A08F: 0x%04x
%{public}s:%i Changing RF settings to alternate
%{public}s:%i HFLR=0x%04x PSP=0x%04x MSP=0x%04x
%{public}s:%i SE power up failed. Trying to power off
%{public}s:%i Invalid data returned: %d
%{public}s:%i Failed to get page : 0x%04llx
%{public}s:%i RSSI stats count %d, min=%d, max=%d, average=%d
%{public}s:%i CRC error 0x%x
%{public}s:%i CW detected!
%{public}s:%i \"%s\" errno=%d Payload length overflow error. 
%{public}s:%i Driver is null
%{public}s:%i Failed 0x%04llx
%{public}s:%i Found Kovio tag
%{public}s:%i Device does not support this feature
%{public}s:%i profile: %d
%{public}s:%i Disabling headless mode
%{public}s:%i polling=%d emulation=%d field=%d express=%d resume=%d reader config=%d
%{public}s:%i Not enough space allocated to store all page counters
%{public}s:%i EDT antenna name: %s
%{public}s:%i Failed to get FDR data : no data.
%{public}s:%i Primary = %s
%{public}s:%i Allocation failed
%{public}s:%i phLibNfc_RemoteDev_CheckNdef failed: 0x%04llx
%{public}s:%i cfg=0x%04x addr1=0x%08x len1=0x%04x addr2=0x%08x len2=0x%04x
%{public}s:%i Completion pointer was null
%{public}s:%i Failed to push Cal to NFCC : 0x%04llx
%{public}s:%i Invalid context 0x%02x
%{public}s:%i failed to %sable headless mode: 0x%04llX
%{public}s:%i MFW factory page config notification received : NULL
%{public}s:%i Unknown chip model ID !
%{public}s:%i No NDEF write data provided
%{public}s:%i Failed to write miniNV
%{public}s:%i Types-ABF only
%{public}s:%i %s
%{public}s:%i Error : invalid response.
%{public}s:%i Crashing in %d ms
%{public}s:%i L2 logging got null info!
%{public}s:%i Not supported on SN100V dev boards - skipping..
%{public}s:%i JCOP branch: %d.%d
%{public}s:%i platform: %d.%d.%d.%d
%{public}s:%i Note : OS mode is System only
%{public}s:%i select returned error: 0x%04x
%{public}s:%i Resolve key type from config
%{public}s:%i Idle=%d
%{public}s:%i Failed to load hw
%{public}s:%i Not supported for Host SE!
%{public}s:%i > eNfccParam: %d
%{public}s:%i Received empty %s debug info from NFCC
%{public}s:%i SE uptime counter overflown
%{public}s:%i %s Continuous Wave
%{public}s:%i %s configured successfully
%{public}s:%i Failed to get RF conf settings.
%{public}s:%i Unable to create TLV config from hex string
%{public}s:%i Re-configuring XTAL clock source
%{public}s:%i 212kbps not supported?
%{public}s:%i Mutex init failed : %d
%{public}s:%i Unknown type: %d
%{public}s:%i SE uptime failed to be queried, power=%d, mailbox=%d
%{public}s:%i phLibNfc_Mgt_RawCtrlMsgTransceive failed 0x%04llx
%{public}s:%i [L2] %0.6f command=0x%02x debug=0x%02x rssi=0x%04x
%{public}s:%i Power cycling SE success.
%{public}s:%i Error: Failed to power cycle the SE.
%{public}s:%i Wrong interfaceType %d - cannot continue!
%{public}s:%i Get stack breadcrumb failed
%{public}s:%i Boot status=%d\n                        ROM=0x%x, HW Version=0x%x, Chip version=0x%04X, Variant=%x, ModelID=%x\n                        Protected status=%x, Lifecycle:{scratch=0x%04X,protected=0x%04X}, vendorFW={scratch=0x%04X
%{public}s:%i Customer factory page is locked. Cannot clear E0 tag.
%{public}s:%i Clearing E0 tag from customer factory page.
%{public}s:%i Invalid offset %d for tag 0x%04x
%{public}s:%i Failed to create RF settings from TLV string %s
%{public}s:%i No SEID in manifest
%{public}s:%i Failed to recover SE
%{public}s:%i > phLibNfc_Mgt_GetNfccParams FAILED
%{public}s:%i \"%s\" errno=%d Unknown migration state: 0x%04x
%{public}s:%i failed to get stack info
%{public}s:%i Failed to enable write counters status:0x%08llx
%{public}s:%i enabling LPCD assist
%{public}s:%i Failed to configure Temperature restrictor : 0x%04llX
%{public}s:%i failed to enable VAS CODES: 0x%04llX
%{public}s:%i Unknown SE: %d
%{public}s:%i Unsupported hardware.
%{public}s:%i Selecting OSU
%{public}s:%i timeout must be < %dms
%{public}s:%i Unexpected length for ISO modulation : %d, expected %d
%{public}s:%i Failed to trigger core dump
%{public}s:%i Got temperature notification SWIO2 / AIO2: %d, 0x%x -> %lf
%{public}s:%i Unexpected count of SEs : %d
%{public}s:%i eSE did not re-enumerate
%{public}s:%i Unable to find config tag info for tag 0x%02x
%{public}s:%i Failed to find tag 0x%04x
%{public}s:%i Enabling VAS CODES
%{public}s:%i Failed to get integrity check
%{public}s:%i Num Tags Added=%d, Detected=%d, Removed=%d, Not Interested=%d
%{public}s:%i Got SE Removed with status %d
%{public}s:%i status=0x%04llX, previous state %d
%{public}s:%i ***WARNING*** Express mode is requested; express won't work under this config!!!
%{public}s:%i RF counter overflown
%{public}s:%i Getting SMB log..
%{public}s:%i Failed to set RF conf settings.
%{public}s:%i deselected
%{public}s:%i SE Restricted Mode Enable! OS_ID = %d
%{public}s:%i interfaceType:%d path:%s flags:0x%llx
%{public}s:%i CE and Reader not allowed at the same time
%{public}s:%i phLibNfc_RemoteDev_CheckPresence failed: 0x%04llx
%{public}s:%i SE %d does not support wired mode
%{public}s:%i Disabling standby for debugging
%{public}s:%i (%s) mode=%s
%{public}s:%i eSE Restricted Event %d %d
%{public}s:%i enable: %d
%{public}s:%i JCOP uptime counter overflown
%{public}s:%i Resource error
%{public}s:%i Failed to clear E0 tag : %d
%{public}s:%i JCOP OS Update Mode detected
%{public}s:%i Unexpected length, using custom settings...
%{public}s:%i Platform does not have boot measurements
%{public}s:%i ProhibitTimer.Host.Start
%{public}s:%i No RF settings.
%{public}s:%i Unable to extract trust object digest from AP Ticket
%{public}s:%i Certificate too long: %zu
%{public}s:%i Stack logging failed with 0x%x
%{public}s:%i %s : 0x%x
%{public}s:%i Failed to restore discoverty configuration
%{public}s:%i Failed to set rf property:0x%02x status:0x%08llx
%{public}s:%i Write counter is 0x%x (length = %d)
%{public}s:%i Failed to set eSE to virtual mode
%{public}s:%i Failed to parse TLV
%{public}s:%i Missing CE interface type
%{public}s:%i Unexpected length : %d
%{public}s:%i ProhibitTimer.SE.Start
%{public}s:%i Failed to set RF config set1.
%{public}s:%i WARNING !!!\nWARNING !!!\nWriting to Mini NV to disable headless. This is not expected outside factory.\nWARNING !!!
%{public}s:%i Got temperature notification SWIO1 / AIO3: %d, 0x%x -> %lf
%{public}s:%i Use default ECP value
%{public}s:%i ESE reader config %d -> %d
%{public}s:%i [L2] %0.6f response=0x%02x status=0x%04x debug=0x%02x vpp=%f ALMPhase=%.3f
%{public}s:%i Failed to power cycle SE... it's not coming back folks
%{public}s:%i Secondary = %s
%{public}s:%i %s CRC
%{public}s:%i WARNING ! Do not send data to JCOP in unknown state !!!!!
%{public}s:%i Bad response APDU length %d
%{public}s:%i This API is available in DL mode only
%{public}s:%i Failed to disable standby mode.
%{public}s:%i Failed to set data rate for NTAG5 %d
%{public}s:%i setting 212
%{public}s:%i Failed to resume SE mode
%{public}s:%i \t Log is empty!
%{public}s:%i [C-RAW>] Soft Reset
%{public}s:%i RF config to set: %s
%{public}s:%i eSE, enabled=%d
%{public}s:%i R0=0x%04x R1=0x%04x R2=0x%04x R3=0x%04x R12=0x%04x
%{public}s:%i BPMR=0x%04x FMR=0x%04x CR=0x%04x
%{public}s:%i ProhibitTimer.SE.End
%{public}s:%i Unknown SE type %d
%{public}s:%i Failed to register notification callback.
%{public}s:%i Setting polling modulation limit to 100%%
%{public}s:%i Cond init failed : %d
%{public}s:%i Warning : B state cal data was written with A state values. Applying ..
%{public}s:%i Unexpected status: 0x%X
%{public}s:%i AC log exists, but supplied output parameter is NULL.
%{public}s:%i ==== PLL UNLOCKED ====
%{public}s:%i Warning : Standby disabled.
%{public}s:%i ==== GPADC TEMPERATURE CONDITION NORMAL ====
%{public}s:%i Discovery already stopped, don't need to stop again
%{public}s:%i SE recovery complete. Leaving SE in wired
%{public}s:%i XTAL start error received
%{public}s:%i Failed to get RF settings registers.
%{public}s:%i Removed Tag (%d) rfTech = %d id= 0x%02x 0x%02x 0x%02x 0x%02x
%{public}s:%i SMB debug : NULL
NFDriverRemoteDevReadNdef
%{public}s:%i Failed to merge RF settings
%{public}s:%i Failed to parse TLVs, is the format correct ?
%{public}s:%i GetPresenseOfAttackLog will only work in JCOP mode
%{public}s:%i Unknown SE removed: reason=0x%02x, other=0x%02x
%{public}s:%i No command APDU provided
%{public}s:%i Customer Factory page has no data.
%{public}s:%i Failed to get CF types
%{public}s:%i Simulating HW Reset
%{public}s:%i Invalid clock register response
%{public}s:%i Restoring RF
%{public}s:%i serial number too long: %ld
%{public}s:%i Failed to get data
%{public}s:%i Enabling write counters
%{public}s:%i semaphore released without signal!
%{public}s:%i SE in recovery
%{public}s:%i ---- TICKS ----
%{public}s:%i F0 has testing bit (0x%04x), will overwrite.
%{public}s:%i Found Host state=%d
%{public}s:%i Multitag state query
%{public}s:%i Setting MultiTag Config. A=%d S=%d S2=%d S3=%d V=%d VASUPA=%d Retries=%d TlvId=%d, debugMode=%d pollDuration=%d pollRetries=%d
%{public}s:%i Unable to alloc memory 
%{public}s:%i failed to get config TLV JDI
%{public}s:%i Found FDR data, %ld bytes
%{public}s:%i Failure for tag 0x%x
%{public}s:%i Re-init failed. Bailing.
%{public}s:%i Embedded SE removed: reason=0x%02x, other=0x%02x
%{public}s:%i Attempt %d of %d
%{public}s:%i Using cached dieID
%{public}s:%i [L2] %0.6f state=0x%02x 15693state=0x%02x tech=0x%02X status=0x%02x data=%s
%{public}s:%i \t pInfo (pointer to L2Debug Info) is NULL!
%{public}s:%i Failed to get FDR data from local store, trying memory
%{public}s:%i timeout must be < %d
%{public}s:%i eSE not in wired mode
%{public}s:%i Enabling ECP mode since no other is selected.
%{public}s:%i SELECT OS Update AID
%{public}s:%i Unable to get presence of AC log
%{public}s:%i MultiTag-FC=%d
%{public}s:%i RF-proc: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
%{public}s:%i Unmatched tag 0x%04x
%{public}s:%i Failed to get FDR key : %d
%{public}s:%i Failed to get MG types
%{public}s:%i Could not find status container
%{public}s:%i Failed to update discovery
%{public}s:%i Dropping temperature notification
%{public}s:%i Failed to read headless
%{public}s:%i Failed to create page content
%{public}s:%i Returned error: 0x%04x
%{public}s:%i Follower ID unresponsive!
%{public}s:%i failed to allocate Tx data struct
%{public}s:%i Changing RF settings to default
%{public}s:%i kernel: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
%{public}s:%i Forcing full hce routing
%{public}s:%i F0 version is 0, treating as unprogrammed.
%{public}s:%i Customer Factory page is unlocked.
%{public}s:%i No memory available
%{public}s:%i Received Spmi Error Register Info notification: 0x%02x, 0x%02x, 0x%02x , 0x%02x, 0x%02x ,0x%02x
%{public}s:%i ProhibitTimer.Host.End
%{public}s:%i RF settings is too short: length=%zu
%{public}s:%i Error : unable to write to transition registers
%{public}s:%i Failed to read RF cal data from FDR.
%{public}s:%i Error 0x%x using API %d - requires a reboot !
%{public}s:%i [L2] %0.6f event=0x%02x debug=0x%02x
%{public}s:%i phLibNfc_RemoteDev_Receive failed 0x%04hx
%{public}s:%i WTX: error, too many WTX
%{public}s:%i Failed to setup SERM power save
Error : timeout occured !!!
NFDriverRemoteDevWriteNdef
%{public}s:%i setting 848
%{public}s:%i %s SPMI event logging
%{public}s:%i failed to set vGPIO tag (0xA008)
%{public}s:%i **** getNfccParamsCb: STATUS = 0x%02X ****
Stockholm SPMI unresponsive
%{public}s:%i Polling config is using Custom ECP
%{public}s:%i SE=%d, power=%d, mailbox=%d
%{public}s:%i 0x%02X TLV length doesn't match expected (%d)
%{public}s:%i Customer Factory page is NULL.
%{public}s:%i Restricted Mode detected
%{public}s:%i Failed to get platform identifier
%{public}s:%i Nuked SE gate info : %llu
%{public}s:%i Error at step %d, re-initializing
%{public}s:%i Command is too large: %ld bytes
%{public}s:%i No SE handle
%{public}s:%i E0 tag cleared successfully.
%{public}s:%i hw-config-tlvs: %s
%{public}s:%i Failed to write RF cal data A to NFCC
%{public}s:%i Chipscope buffer empty
%{public}s:%i Failed to VEN reset !!!!! : 0x%04X
%{public}s:%i Found UICC state=%d
%{public}s:%i Polling config is not using ECP
%{public}s:%i Failed to stop polling
%{public}s:%i Power state tracking query
%{public}s:%i [L2] %0.6f state=0x%02x mod=0x%02x rssi=0x%04x, extraInfo=0x%0x fs=0x%04x RMRobustness=0x%04x
%{public}s:%i ESE reader as config set (%d / %d)!
%{public}s:%i deactivated
%{public}s:%i LPCD force always ON
%{public}s:%i Types-BF only
%{public}s:%i This feature is restricted to internal builds.
%{public}s:%i No sealing manifest
%{public}s:%i Stack load failed with 0x%x
%{public}s:%i Error 0x%x powering off !
%{public}s:%i TIMEOUT!
%{public}s:%i Failed to set RF settings.
%{public}s:%i Failed to get boot measurements
%{public}s:%i ESE Reader config %d -> %d
%{public}s:%i Felica command is too large: %ld bytes
%{public}s:%i failed to allocate Tx context
%{public}s:%i SE=%d, JCOP=%d eUICC=%d power=%d, mailbox=%d
%{public}s:%i configuring Felica transaction end pattern for applet ver 2.0
%{public}s:%i Type-F only
%{public}s:%i AMFDRDataCopyTrustObject failed
%{public}s:%i Unexpected event: %x
%{public}s:%i phLibNfc_RemoteDev_Send failed 0x%04llx
%{public}s:%i BFAR=0x%04x CFSR=0x%04x MMFAR=0x%04x
%{public}s:%i NFDriverConfigureReaderModeRFForMercurySigned: Unable to apply Dynamic RF settings. Trying to reset back to defaults
%{public}s:%i \t RAM buffer overflow status  : %d
%{public}s:%i Sealing status is %d
%{public}s:%i Warning : Standby disabled - skipping enablement.
 mutexStatus=%{public, signpost.description:attribute}llu 
%{public}s:%i Invalid buffer
%{public}s:%i Enabling TypeF headless mode
%{public}s:%i Truncated tag found. Tag 0x%02x, tlvLen: %d, idx: %d, len: %d
%{public}s:%i No custom RF settings found!
%{public}s:%i Unable to read AP Ticket
%{public}s:%i Invalid length for 0xC8
%{public}s:%i Success!
%{public}s:%i Cannot power cycle, request denied
%{public}s:%i failed to register for notifications: 0x%04llX
%{public}s:%i Unexpected length for TO_BEFORE_STDBY_CFG : %d
%{public}s:%i status=0x%04X
LPCDPolling
%{public}s:%i phLibNfc_RemoteDev_FormatNdef failed: 0x%04llx
%{public}s:%i [R-APDU<] REDACTED %ld bytes
%{public}s:%i NFCC flash write query
%{public}s:%i Failed : 0x%x
%{public}s:%i Failed to restore SE mode : 0x%x
%{public}s:%i Failed to set eSE to wired mode
%{public}s:%i Host already found
%{public}s:%i Failed to select
%{public}s:%i Interval must be < 900 ms
%{public}s:%i Frame RF INTF activated
%{public}s:%i setting rate: %d
%{public}s:%i No vendor RF settings found for %s!
%{public}s:%i LPCD assist disabled!
%{public}s:%i Failed to get TO_BEFORE_STDBY_CFG.
%{public}s:%i MW requested VEN reset.
%{public}s:%i old SuicaSystemCode: code 1 enabled: %d, code 1: %04X; code 2 enabled: %d, code 2: %04X
%{public}s:%i Non-default multitag polling period: %u
%{public}s:%i Failed to get serial number
%{public}s:%i Incorrect manifest query length: %zu
%{public}s:%i unknown express mode type (%d)
%{public}s:%i Failed to set routing
%{public}s:%i Clearing Multitag info state
%{public}s:%i mailbox: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
%{public}s:%i Failed to get FDR data : %ld - %s
%{public}s:%i Warning : B state cal data was written with A state values. Skipping ..
%{public}s:%i uptimne is %llu
%{public}s:%i Failed to set HOST to virtual mode
%{public}s:%i Warning : B state cal data was written with A state values. Updating tags ...
%{public}s:%i [L1] %0.6f APCInfo=0x%x tech=0x%x retCode=0x%x vpp=%f ALMPhase=%.3f RMRobustness=0x%04x
%f
%{public}s:%i EMVCO field collision detected
%{public}s:%i halted
%{public}s:%i MW Version is NULL?
%{public}s:%i \t ### HLM debug Log ###
%{public}s:%i Found eSE state=%d
%{public}s:%i Enabling full HCE routing
%{public}s:%i Failed to setup LPCD_CFG
%{public}s:%i Failed to get RF settings; status=0x%04llX
%{public}s:%i %s TEMPERATURE WARNING RECEIVED
%{public}s:%i Num Tags Detected=%d, Num Tags Not Interested=%d
%{public}s:%i Enabling single poll headless mode
%{public}s:%i Failed to %s NFCC CRC
%{public}s:%i Added Tag (%d) rfTech = %d id= 0x%02x 0x%02x 0x%02x 0x%02x
%{public}s:%i Unable to do any RF operations. Returning false.
%{public}s:%i Disabling chipscope
%{public}s:%i %s SMB log
%{public}s:%i Headless is 0x%x (length = %d)
%{public}s:%i Type-B only
%{public}s:%i Failed to configure RF logging : 0x%04llX
%{public}s:%i ==== UART ERROR ====
%{public}s:%i Not supported on MWF
%{public}s:%i Invalid format
%{public}s:%i sealingManifestData DataCopy failed
%{public}s:%i Unable to get RF Conf register values
%{public}s:%i tag removed
%{public}s:%i Memory error trying to update property: 0x%02x
%{public}s:%i Writing headless mini NV 
%{public}s:%i mode=0x%x
%{public}s:%i Device does not require RF settings changes
%{public}s:%i Allocation failure
%{public}s:%i Failed to get DieID
%{public}s:%i Enabling express: transit=%d vas=%d generic-a=%d single_poll=%d debug=%d block=%d 
%{public}s:%i Failed to get factory page : %d
%{public}s:%i Invalid length %d for tag 0x%x: only %zu remaingin
%{public}s:%i Invalid manifest length
%{public}s:%i failed to set baud rate: 0x%04llX
%{public}s:%i MultiTag Enabled: %d, Running: %d
%{public}s:%i [L1] %0.6f state=0x%x tech=0x%x rssi=0x%x FelicaL1State=0x%x L1DataRxFailure=0x%x AGCRegValue=0x%x vpp=%f fs=0x%x RMRobustness=0x%04x
%{public}s:%i Error ! Unexpected cert length 
%{public}s:%i rapdu length too short %d
%{public}s:%i Enabling reader mode dynamic BBA control
%{public}s:%i MFW Notification received
%{public}s:%i NFCC does not support Continuous Wave
%{public}s:%i WTX: no info
%{public}s:%i F0 TLV too short (%d), treating as unprogrammed.
%{public}s:%i Failed to write page : 0x%04llx
%{public}s:%i Could not get Sealed Data Instance
%{public}s:%i Error : function at index %d will never run
%{public}s:%i Wrong 'eNfccParam' received!
FIELD_ON
%{public}s:%i Marking ESE reader as disabled!
%{public}s:%i Failed to allocate TLV data
%{public}s:%i Failed to read Module cal data from FDR.
%{public}s:%i Intf activation ntf error
%{public}s:%i Failed to create data (%lu bytes) with result
%{public}s:%i Invalid opcode 0x%x
%{public}s:%i Failed to get instance name
%{public}s:%i Invalid value for 0x%X, len=%ld
%{public}s:%i configs are identical - skipping.
%{public}s:%i Headless mini NV already set
%{public}s:%i Error ! Received boot stop interrupt.
%{public}s:%i %sabling headless mode
%{public}s:%i Mini NV headless is 0x%x (length = %d)
%{public}s:%i \t Number of HLM debug msgs: %d
%{public}s:%i DL session already open.
%{public}s:%i ==== HARDWARE RESET ====
%{public}s:%i %s reader mode dynamic BBA control
%{public}s:%i Values different. Will apply new values
%{public}s:%i Using local RF settings
%{public}s:%i RSSI stats with no sample
[Hex dump: length=%lu bytes] (%{public}s:%i %{public}s)
%{public}s:%i Idle counter overflown
%{public}s:%i Failed to configure Type A emulation : 0x%04llx
%{public}s:%i ---- SPMI ----
%{public}s:%i Invalid logging value
%{public}s:%i Disabling boost
%{public}s:%i Failed to write RF cal data B to NFCC
%{public}s:%i Failed to set RF settings : status=0x%04X
%{public}s:%i Generic error : 0x%04X
%{public}s:%i [L2] ms=0x%02x µs=0x%02x LMA=0x%02x BBA=0x%02x
%{public}s:%i failed to get config TLV
%{public}s:%i %s reader mode static BBA control
%{public}s:%i Failed to read write counter
%{public}s:%i Enabling ECP headless mode
%{public}s:%i Failed to decode plist
%{public}s:%i Invalid length : no room for tag
%{public}s:%i ==== NFCC/SE TEMPERATURE CONDITION EXITED ====
%{public}s:%i Host did not re-enumerate
%{public}s:%i Failed to %s continuous wave
%{public}s:%i Failed to setup delayed wake, status = 0x%04X
%{public}s:%i WARNING : Disabling SE reader mode Power save. Temperature will rise much faster !
%{public}s:%i Failed to get antenna name from EDT : %s
%{public}s:%i EUICC = %s
%{public}s:%i Unable to create aid needed for selecting ISD
%{public}s:%i OS %d removed for reason 0x%x
%{public}s:%i Express cfg: Transit:%d Access:%d Generic-A:%d SinglePoll:%d Block:%d Debug:%d
%{public}s:%i Set output read buffer empty. Not applying new values
%{public}s:%i %s(%04X) skipped
%{public}s:%i Failed to query controller info.
%{public}s:%i Error ! Unexpected serial number length 
%{public}s:%i Error 0x%x using API %d - requires a new firmware !
%{public}s:%i Step %d error : 0x%x
FIELD_OFF
%{public}s:%i Not supported
%{public}s:%i Configuring Fury Multitag ECP Frame
%{public}s:%i type=0x%x
%{public}s:%i Status = 0x%x, param=%d
%{public}s:%i Invalid length for 0xC9
%{public}s:%i isLoaded=%d
%{public}s:%i Invalid parameter
%{public}s:%i TxLDO OverCurrent Error
%{public}s:%i Enabling multi-tag polling, RTID=%d
%{public}s:%i Failed to init se of type %d
%{public}s:%i Unknow Key Usage 0x%x
%{public}s:%i %s SE in DL mode
%{public}s:%i No compensation applied due to underflow, poll phase duration (ms): %d
%{public}s:%i NFCEE powered off
%{public}s:%i No SE for transceive
%{public}s:%i Reading Die ID ...
%{public}s:%i Types-AB only
%{public}s:%i TLV overrun at tag 0x%02x
%{public}s:%i AID_P73_MANIFESTQUERY returned error: 0x%04x
%{public}s:%i Temperature restrictor configured
%{public}s:%i Multitag structure is missing
%{public}s:%i LPCD force always OFF
%{public}s:%i dataClass is NULL
%{public}s:%i Returned error: 0x%04x for (0x%x/0x%x)
%{public}s:%i Not enough storage for cert %d (tag 0x%x). Len = %lu, type = %d !
%{public}s:%i Queuing exit due to timeout
%{public}s:%i SMB Tx Blocked!
%{public}s:%i \t Number of L2 debug msgs: %d
%{public}s:%i Not interested Tag (%d) rfTech = %d, rfError = %d, numTagsDet = %d
%{public}s:%i Mutex already signalled timeout! CB status: %04x
%{public}s:%i Not updating the rest of OS Info : JCOP is not available
%{public}s:%i ISD sequence counter %d does not match migration update counter %d
%{public}s:%i Max retries reached.
%{public}s:%i Received %s debug data from NFCC (%u bytes)
%{public}s:%i wantsFieldDetect=%d wantsPolling=%d wantsExpress=%d eSE=%d host=%d wantsEcpUpdate=%d
%{public}s:%i phLibNfc_RemoteDev_Disconnect failed: 0x%04llx
%{public}s:%i FAILED: %s
%{public}s:%i Missing TX LDO data
%{public}s:%i Invalid I/O selected
%{public}s:%i Running build from (B&I) Stockholm_Base-371.8
%{public}s:%i Re-using entry threhold
%{public}s:%i status=0x%04llX
%{public}s:%i Unknown value: %d
%{public}s:%i CRC error or response timeout - 0x%04llx
%{public}s:%i Configuring chipscope
%{public}s:%i SWP-proc: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
%{public}s:%i Failed to set ECP VAS polling: 0x%08llx
%{public}s:%i LR=0x%04x PC=0x%04x XPSR=0x%04x
%{public}s:%i 0x%02X TLV doesn't match
%{public}s:%i Flags requested DL mode only.
%{public}s:%i Re-using exit threhold
%{public}s:%i eSE already found
%{public}s:%i RTID Debug mode enabled
%{public}s:%i Failed to get RF settings; status=0x%04llX.
%{public}s:%i Failed to query FW info !
%{public}s:%i \t FLASH buffer overflow status: %d
%{public}s:%i Failed to set XTAL clock source
%{public}s:%i Platform id too long: %ld
%{public}s:%i Error : timeout occured !!!
%{public}s:%i Requested read size is over the limit
%{public}s:%i Faled to configure Type B emulation : 0x%04llx
%{public}s:%i ---- ASSERT ----
%{public}s:%i [L2] %0.6f state=0x%02x mod=0x%02x sc=0x%04x, extraInfo=0x%0x RMRobustness=0x%04x
%{public}s:%i Empty factory page
%{public}s:%i Failed to read clock register
%{public}s:%i Device in degraded mode. Wired not available.
%{public}s:%i Compensation applied, poll phase duration (ms): %d
%{public}s:%i UICC did not re-enumerate
%{public}s:%i phLibNfc_RemoteDev_Connect failed: 0x%04llx
%{public}s:%i phLibNfc_Ndef_Write failed: 0x%04llx
%{public}s:%i Non-default polling period: %u
%{public}s:%i Failed to write IRQ
%{public}s:%i failed to get clock TLV
%{public}s:%i Cal data for B is correct, flashing.
%{public}s:%i Hardware not supported
%{public}s:%i Failed to get RF settings.
%{public}s:%i setting 106
%{public}s:%i [R-RAW<] Soft Reset
%{public}s:%i host: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
%{public}s:%i missing creator for SE type %d
%{public}s:%i Failed to allocate manifest query data
%{public}s:%i Invalid length for 0xCB
%{public}s:%i > phLibNfc_Mgt_GetNfccParams
%{public}s:%i PC: %d
%{public}s:%i host-LP: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
%{public}s:%i Failed to verify sealing : %ld
%{public}s:%i toBeforeStdbyCfg=%d ms, requesting %d
%{public}s:%i Unhandled tag type 0x%04x
%{public}s:%i Fail to get controller info
%{public}s:%i Full HCE can't be used with polling
%{public}s:%i \t Invalid 'eNfccParam' returned
%{public}s:%i Failed to set A1DF: 0x%08llx
%{public}s:%i SE reader mode event : {se=0x%x, startEnd=%d, poll=0x%x, protocol=0x%x}
%{public}s:%i phLibNfc_SE_ActModePwrOff is only available on ese - switching to ActModeOff
%{public}s:%i WTX: error %d
%{public}s:%i SEID in manifest is %@
%{public}s:%i Failed to get JCOP Version
%{public}s:%i Type-A only
%{public}s:%i Disabling field detection for Single Poll express
%{public}s:%i Unexpected element found in status container: 0x%04x
%{public}s:%i Flash counter exceeded notification. This is NOT expected unless you live in the 22nd century or later. File a radar and get a new device.
%{public}s:%i enable %02X
%{public}s:%i Failed to configure HW settings
%{public}s:%i Failed to verify %s(%04X)
%{public}s:%i GET OS MODE
%{public}s:%i Failed to get update info
%{public}s:%i Failed to set ECP Frame
%{public}s:%i No remote tag handle provided
%{public}s:%i phLibNfc_RemoteDev_Receive failed 0x%04llx
%{public}s:%i Sending 2F 0x%x to FW
%{public}s:%i %s(%04X) is OK
%{public}s:%i Data length is %ld
%{public}s:%i Transceive failure
%{public}s:%i Get Debug Info failed: %04X
%{public}s:%i [L1] %0.6f state=0x%x tech=0x%x rssi=0x%x FelicaL1State=0x%x L1DataRxFailure=0x%x AGCRegValue=0x%x vpp=%f ALMPhase=%.3f fs=0x%x RMRobustness=0x%04x
%{public}s:%i Customer Factory page is locked.
%{public}s:%i Got unknown certificate type??
%{public}s:%i LPEM flash writes disabled! Headless mode will not be updated on the device.
%{public}s:%i MSPL=0x%04x PSPL=0x%04x PMR=0x%04x
%{public}s:%i phLibNfc_RemoteDev_Transceive failed 0x%04llx
%{public}s:%i WARNING : power cycling SE
%{public}s:%i Failed to configure Temperature monitoring : 0x%04llX
%{public}s:%i interfaceType:%d path:%s flags:0x%llx  aux path:%s
%{public}s:%i Setting prevent reset to %d
%{public}s:%i Failed to stop routing
%{public}s:%i Failed to stop discovery
%{public}s:%i Unknown notification: 0x%x
%{public}s:%i num_dev=%d, status=%d
%{public}s:%i status=0x%04X for event %d
%{public}s:%i UICC already found
%{public}s:%i Can't send to OS %d. Not available.
%{public}s:%i Failed to get FDR data : Invalid type.
%{public}s:%i Detected Tag (%d) rfTech = %d id= 0x%02x 0x%02x 0x%02x 0x%02x
%{public}s:%i Embedded SE EVT_RESTRICTED!
%{public}s:%i Already up-to-date
%{public}s:%i Not supported - skipping on this hardware
%{public}s:%i LPCD-FC=%d
%{public}s:%i Enabling Generic-A headless mode
%{public}s:%i Failed to create RF settings from clock TLV string %s
%{public}s:%i Unexpected type
%{public}s:%i Unknown OS mode %d
%{public}s:%i phLibNfc_Mgt_GetNfccParams failed 0x%04llx
%{public}s:%i \"%s\" errno=%d Invalid L1 standby wake event 0x%x
%{public}s:%i E0 tag not found or already cleared. Nothing to do.
%{public}s:%i Failed to write RF cal data to NFCC
%{public}s:%i Unexpected length: %zu
%{public}s:%i Invalid length for 0xCA
%{public}s:%i Not supported for UICC!
%{public}s:%i Unknown poll mode profile 0x%0x, using default
%{public}s:%i Failed to allocate buffer
%{public}s:%i Invalid length for tag 0x%x
%{public}s:%i Polling config is using VAS ECP
%{public}s:%i ---- Core Dump ----
%{public}s:%i Pushing vendor RF settings for %s
%{public}s:%i failed to validate EEPROM: 0x%04llX
%{public}s:%i Extending timeout 10 seconds. User has requested us to avoid crashing.
%{public}s:%i Error : invalid reader event
%{public}s:%i 
%{public}s:%i wantsFieldDetect=%d wantsPolling=%d wantsExpress=%d eSE=%d host=%d ceType=%d, hasDiscoveryChanges=%d hasRoutingChanges=%d fullHCE=%d
%{public}s:%i phLibNfc_AntennaSelfTest FAILED : 0x%llx
%{public}s:%i Incompatible firmware !
%{public}s:%i %d%% ASK modulation requested.
%{public}s:%i Session State=%d,                     HW Version=0x%x,                     ROM=0x%x,                     Model=0x%x,                     FW=%x.%x,                     MW=%x.%x r%llx,                     Chip=%x                
%{public}s:%i Response time : %f us (%d), PICC Response: 0x%04X, PCD response = 0x%04X
%{public}s:%i Routing changed
%{public}s:%i Got %x (%d), returning %lf
%{public}s:%i Failed to fully power off eSE
%{public}s:%i Setting polling period to %u
%{public}s:%i Failed to set A11E tag: 0x%04llx
%{public}s:%i HFSR=0x%04x SFAR=0x%04x SFSR=0x%04x
%{public}s:%i failed to get config TLV LGD
%{public}s:%i ERROR: no value !
%{public}s:%i Multi tag status notification received
%{public}s:%i HW is not supported
%{public}s:%i Polling cfg: A:%d B:%d F:%d 15693:%d S:%d S2:%d S3:%d CustomECP:%d VAS_ECP:%d frameRF:%d
%{public}s:%i ---- HARD FAULT ----
%{public}s:%i Using EDT RF settings
%{public}s:%i Manifest Query is not supported on this OS version (sequence counter: %d)
%{public}s:%i LastAPI=0x%02X, LastAPIStatus=0x%04X DebugInfo=0x%016llX
%{public}s:%i RF=%d
%{public}s:%i [L2] %0.6f state=0x%02x mod=0x%02x rssi=0x%04x, ALMPhase=%.3f fs=0x%04x RMRobustness=0x%04x
%{public}s:%i SE is now recovered and set to prior mode
%{public}s:%i Powering SE back ON
%{public}s:%i Type-B disabled
%{public}s:%i No data received.
%{public}s:%i Got FDR data but an error is set : %ld - %s
%{public}s:%i \"%s\" errno=%d Unable to allocate memory for capdu. 
%{public}s:%i Incorrect T1 %ud, using 320usec!
%{public}s:%i MultiTag false detect counter overflown
%{public}s:%i Failed to read miniNV
%{public}s:%i Note : OS mode is Boot Loader
%{public}s:%i Invalid update info length: %zu
%{public}s:%i SELECT returned error: 0x%04x. Cannot query presence of attack log without selecting ISD
%{public}s:%i Stack load failed with 0x%x, continuing in DL mode.
%{public}s:%i No SE of type %d.
%{public}s:%i Error : Allocation failure
%{public}s:%i Marking ESE reader as enabled!
%{public}s:%i Unclassified MIFARE (%d) found
%{public}s:%i Reset notification. Len = %d
%{public}s:%i Not interested Tag (%d) rfTech = %d
%{public}s:%i RF settings = %s
%{public}s:%i Failed to allocate buffer.
%{public}s:%i TXLDO error!
%{public}s:%i ESE reader discovery change requested %d -> %d!
%{public}s:%i Resuming SE mode to 0x%x (stored routing mode is %d)
%{public}s:%i F0 has production content (version=0x%04x, type=0x%04x), preserving.
%{public}s:%i Failed to set GPIO : %u
%{public}s:%i eSE power-on failed! (%d/%d)
%{public}s:%i ---- WATCHDOG ----
%{public}s:%i NFDriverConfigureReaderModeRFForMercurySigned: Unable to apply Default RF settings
%{public}s:%i Did not find version tag!
%{public}s:%i EEPROM validation failed (%d/%d)
%{public}s:%i SE Restricted Mode Exit! OS_ID = %d
%{public}s:%i LPCD false detect counter overflown
%{public}s:%i [L1] StandbyEventType=0x%x RegValue=0x%x
%{public}s:%i Failed to allocate se of type %d
%{public}s:%i SELECT returned error: 0x%04x
%{public}s:%i Error, trying to power cycle the SE.
%{public}s:%i Disabling multi-tag polling, RTID=%d
%{public}s:%i Unknown parameter !
%{public}s:%i isLoaded=%d flags = 0x%x
%{public}s:%i target lost
%{public}s:%i NFHardwareGetHWConfigTLVs() returned success but out string is null!
%{public}s:%i Got error 0x%2X
%{public}s:%i JCOP1 = %s
```
