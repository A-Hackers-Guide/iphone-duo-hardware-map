# `/usr/lib/libPN548_API.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 538,128 bytes.

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
%s:%i Enabling Generic-A headless mode
_NFDriverSetSecureElementRouting
%s:%i RF config to set: %s
%s:%i Returned error: 0x%04x for (0x%x/0x%x)
GetOSUpdateLog_UICC
Enabled
%s:%i Failed to set ECP VAS polling: 0x%08llx
NFDriverGetStackBreadcrumb
NFDriverRemoteDevReceive
%s:%i [L2] %0.6f state=0x%02x 15693state=0x%02x tech=0x%02X status=0x%02x data=%s
%s:%i phLibNfc_RemoteDev_Transceive failed 0x%04llx
%s:%i Customer factory page is locked. Cannot clear E0 tag.
%s:%i 0x%02X TLV length doesn't match expected (%d)
NFDriverAntennaSelfTest
NFDriverRFSettingsSetup
_NFDriverTranslateRF
%s:%i Restricted Mode detected
Dis
%s:%i eSE power-on failed! (%d/%d)
%s:%i > phLibNfc_Mgt_GetNfccParams
%s:%i Failed to set eSE to wired mode
%02X.%02X
RX_CTRL
SetPower_Eos
NFDriverUpdateFirmware
NFDriverDumpLPMDebugLog_block_invoke
%s:%i Failed to configure HW settings
%s:%i Failed to read Module cal data from FDR.
_NFDriverRFSettingsReadCalDataFromFDR
_NFDriverNukeSEGateInfo
NFCC LOW
ESE LOW
NFDriver.c
%s:%i phLibNfc_RemoteDev_FormatNdef failed: 0x%04llx
%s:%i Got FDR data but an error is set : %ld - %s
NFDriverDumpUART_block_invoke
_Callback_NFDriverNotifyDiscovery
%s:%i halted
%s:%i wantsFieldDetect=%d wantsPolling=%d wantsExpress=%d eSE=%d host=%d ceType=%d, hasDiscoveryChanges=%d hasRoutingChanges=%d fullHCE=%d
driver->isHammerfest == false
%s:%i Disabling standby for debugging
%s:%i Powering SE back ON
%s:%i Device does not require RF settings changes
%s:%i profile: %d
FW DL pending
%s:%i NFCC flash write query
NFDriverSetHCETypeBConfig
_NFDriverCustomerFactoryPageFindTLV
_Async_NFDriverSetCEConfigParams_block_invoke
%s:%i F0 TLV too short (%d), treating as unprogrammed.
%s:%i This feature is restricted to internal builds.
%s:%i Failed to stop routing
NFDriverGetPowerCounter
NFDriverRFSettingsPushSetting
YES
%s:%i DL session already open.
[Hex dump: length=%lu bytes] (%s:%i %s)
NDEF message size is over the limit
%s:%i phLibNfc_Mgt_GetNfccParams failed 0x%04llx
NFDriverSetTemporaryPollingPeriod
numRoutes <= MAX_NFCC_ROUTING_ENTRIES
_copyTagInfoFromDevice
_Callback_NFDriverNotifySE
_NFDriverRFSettingsGetEDTAntennaName
%s:%i Unexpected length: %zu
%s:%i Not supported for UICC!
GetAttackCounterLog_P73
%s:%i SMB debug : NULL
_NFDriverLoadMW
%s:%i Error 0x%x using API %d - requires a new firmware !
_NFDriverLoadStackSteps
%s:%i interfaceType:%d path:%s flags:0x%llx
NFDriverSecureElementGetOSInfo
%s:%i Pushing vendor RF settings for %s
%s:%i Failed to setup LPCD_CFG
%s:%i Failed to get platform identifier
%s:%i Not supported on MWF
disable
_NFDriverRebootRemovedSE
%s:%i Frame RF INTF activated
NFDriverConfigureVASPolling
%s:%i Failed to set Prox config : 0x%08llx
%s:%i Discovery already stopped, don't need to stop again
NFDriverDumpLPMDebugLog
%s:%i Type-B only
%s:%i Types-AF only
NFDriverSecureElementCreate
%s:%i Error at step %d, re-initializing
NFDriverRemoteDevReadNdef
%s:%i [L2] %0.6f command=0x%02x debug=0x%02x rssi=0x%04x
%s:%i Failed to read registers from NFCC : 0x%4llx
NFCC is not working
%s:%i Temperature restrictor configured
%s:%i timeout must be < %d
NFDriverRemoteDevConnect
%s:%i phLibNfc_RemoteDev_Disconnect failed: 0x%04llx
NFDriverRemoteDevSend
%s:%i Failed to create data (%lu bytes) with result
%s:%i Got unknown certificate type??
%s:%i Removed Tag (%d) rfTech = %d id= 0x%02x 0x%02x 0x%02x 0x%02x
%s:%i SWP-proc: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
_NFDriverConfigureDiscovery
RF data from controller
NFDriverSecureElement_IsOSReady
%s:%i Unknow Key Usage 0x%x
%s:%i Failed to set eSE to virtual mode
%s:%i failed to get clock TLV
%s:%i EEPROM validation failed (%d/%d)
%s:%i Failed to configure Temperature monitoring : 0x%04llX
%s:%i Failed to merge RF settings
%s:%i SELECT OS Update AID
%s:%i Invalid value for 0x%X, len=%ld
%s:%i Resolve key type from config
%s:%i status=0x%04X
%s:%i CRC error 0x%x
%s:%i Setting polling period to %u
%s:%i Failed to restore SE mode : 0x%x
%s:%i **** getNfccParamsCb: STATUS = 0x%02X ****
Expected tag value : 
ChipID
%s:%i \"%s\" errno=%d Unknown migration state: 0x%04x
_Async_NFDriverIoCtl_block_invoke
Reboot required
%s:%i enable %02X
Customer factory page (all TLVs)
%s:%i Failed to get serial number
%s:%i enabling LPCD assist
_NFDriverSetReaderModeRFConfigRegsSigned
%s:%i Failed to push builtin RF settings.
GetOSInfo_Eos
_Async_NFDriverClose_block_invoke
%s:%i failed to register for notifications: 0x%04llX
%s:%i %d%% ASK modulation requested.
_NFDriverDisableStandby
[FLC_TRIMMING failed]
%s:%i Types-BF only
%s:%i Failed to push Cal to NFCC : 0x%04llx
_NFDriverReadMiniNVForHeadless
[Reader C-APDU>]
%s:%i EDT antenna name: %s
%s:%i Failed to get FDR data : Invalid type.
NFDriverSecureElement_GetManifestQuery
UnlockRequestInfo
NFCallbackMutexWait
%s:%i Device does not support this feature
%s:%i SE is now recovered and set to prior mode
%s:%i LPCD force always OFF
NFDriverRFSettingsGetVendorParameters
CLOCK_SEL_CFG
_Async_NFDriverValidateEEPROM_block_invoke
NFDriverNFCCPowerOff_block_invoke
_NFDriverEnumerateSecureElements
%s:%i Invalid buffer
No response from tag
%s:%i %s Continuous Wave
%s:%i Invalid data returned: %d
%s:%i AMFDRDataCopyTrustObject failed
%s:%i Invalid version tag length %d
ADC HIGH
%s:%i MultiTag false detect counter overflown
NFDriverSecureElement_GetPresenceOfAttackLog
%s:%i Cond init failed : %d
NFDriverCrashNFCC
driver
%s:%i SE recovery complete. Leaving SE in wired
CLOCK_SEL_CFG_SN100v
%s:%i Invalid length : no room for tag
%s:%i TIMEOUT!
%s:%i MultiTag Enabled: %d, Running: %d
DataDirectory
/System/Library/Caches/com.apple.factorydata
%s:%i setting 424
Measurement Error
_Async_NFDriverTriggerDelayedWake_block_invoke
%s:%i %s(%04X) skipped
%s:%i Failed to parse TLVs, is the format correct ?
NFDriverLoadStack_block_invoke
_NFDriverRFSettingsSetup
NFDriverSecureElementGetMigrationInfoJCOP
NFDriverRemoteDevDisconnect
A0130419191919A00D03610982A06A1000000000000078000000000000000000A09808D9DB098019171717A0AF0911FFF419117DA01902A09E0C07001D960090012BD0070000A0940A072003a200314f001902A0682A064060031914204000930418FF7FFF7F94038404D902840307FA000000350008007D
INST
%s:%i This API is available in DL mode only
%s:%i Query AC log presence failed with 0x%02X
%s:%i GetPresenseOfAttackLog will only work in JCOP mode
%s:%i Error : function at index %d will never run
_NFDriverSetControllerInfo_block_invoke
NFCallbackMutexWait timeout
%s:%i ---- ASSERT ----
%s:%i Incompatible firmware !
%s:%i Failed to trigger core dump
%s:%i Failed 0x%04llx
Reading registers
_NFDriverValidateEEPROM
%s:%i timeout must be < %dms
driver && info
NFDriverGetMultiTagState
_Callback_GetNfccParamsCb
_NFDriverConfigureBBClockSource
Thresholds are :
stack dump
NFDriverRemoteDeviceFelicaTransceive
_Callback_NFDriverSendMFGCommand
%s:%i Invalid update info length: %zu
driver != NULL
%s:%i ---- SPMI ----
%s:%i Warning : Standby disabled - skipping enablement.
%s:%i phLibNfc_RemoteDev_Receive failed 0x%04llx
%s:%i Non-default polling period: %u
TrustObject
%s:%i Forcing FDR path.
%s:%i Stack load failed with 0x%x
NFDriverSecureElementGetOSMode
%s:%i eSE not in wired mode
%s:%i ---- WATCHDOG ----
VGPIO_CONFIG_TAG
%s:%i Failed to register notification callback.
%s:%i phLibNfc_RemoteDev_Connect failed: 0x%04llx
%s:%i failed to allocate buffer
Failed to write page :
A0130428282828A12E03838322A09808A4580D80286A6A6AA09E0C07401F9600FA002B52030000A0AF091178B0281159B02802A06A100000000000003C000000000000000000A0682A0640600319142040009304187A1D863D9C00A30077007D0007FA000000350008007D00003500000E0003
_NFDriverChangeISO15693Modulation
%s:%i Response time : %f us (%d), PICC Response: 0x%04X, PCD response = 0x%04X
%s:%i Enabling full HCE routing
%s:%i failed to get stack info
%s:%i Dropping temperature notification
%s:%i MW requested VEN reset.
%s:%i EMVCO field collision detected
[R-APDU UICC<]
%s:%i Unable to alloc memory 
%s:%i Failed to write RF cal data A to NFCC
%s:%i HCE Register error = 0x%04x
%s:%i phLibNfc_RemoteDev_CheckNdef failed: 0x%04llx
[HCE C-APDU>]
NFDriverRemoteDevGetMiFareInfo
_NFDriverLogAssert
%s:%i Reset notification. Len = %d
NFDriverFactoryPageHasExpectedConfigForTag
%s:%i Failed to find tag 0x%04x
LPCD_CONFIG_TAG
%s:%i Failed to resume SE mode
%s:%i Marking ESE reader as disabled!
%s:%i NFDriverConfigureReaderModeRFForMercurySigned: Unable to apply Default RF settings
_Callback_phLibNfc_Mgt_GetNfccParams
%s:%i F0 has production content (version=0x%04x, type=0x%04x), preserving.
NFDriverDisableBoost
FDR: 
%s:%i Failed to %s SE in DL mode.
NFDriverGetHeadlessModeFlags
SPMI RAM
%s:%i enable=%d
NFDriverRemoteDevWriteLockNdef
%s:%i new SuicaEntrySysCode: code 1 enabled: %d, code 1: %04X; code 2 enabled: %d, code 2: %04X
IsOSReady_Eos
[R-APDU System<]
_NFDriverLogHostProhibitTimerSignpost
stockholm-spmi
%s:%i type=0x%x
%s:%i Unknown parameter !
%s:%i Re-using entry threhold
NFDriverIsSecureElementEnumerated
%s:%i configuring Felica transaction end pattern for applet ver 2.0
%s:%i Failed to write IRQ
%s:%i platform: %d.%d.%d.%d
%s:%i eSE Restricted Event %d %d
_NFDriverGetSiliconName
%s:%i Failed to %s continuous wave
%s:%i Setting MultiTag Config. A=%d S=%d S2=%d S3=%d V=%d VASUPA=%d Retries=%d TlvId=%d, debugMode=%d pollDuration=%d pollRetries=%d
%s:%i Enabling ECP mode since no other is selected.
%s:%i Mini NV headless is 0x%x (length = %d)
FELICA_HIGHZ_RX_TAG
NFDriverLoadStack
%s:%i No memory available
TrustObjectDigest
_NFDriverConfigureSEInDownload_block_invoke
%s:%i failed to set baud rate: 0x%04llX
_Async_NFDriverConfigureRFLogging_block_invoke
%s:%i Failed to restore discoverty configuration
%s:%i Platform does not have boot measurements
%s:%i [L2] phase1Abrt=0x%02x phase2Abrt=0x%02x maxRfPulseAbrt=0x%02x successDetect=0x%02x
%s:%i Using default antenna name %s
NFCC debug data
CEF_FILTERING_CONFIG_TAG
%s:%i failed to set NTAG5 local rate: 0x%04llX
APC_CONTROL_TAG
%s:%i Warning : B state cal data was written with A state values. Skipping ..
%s:%i Unknown notification: 0x%x
%s:%i Update successful, previous session state was %d
%s:%i status=0x%04llX, previous state %d
NFDriverSecureElementGetAttackCounterLog
%s:%i \t FLASH buffer overflow status: %d
settings
GetOSUpdateLog_Host
NFDriverRemoteDevWriteNdef
%s:%i Not interested Tag (%d) rfTech = %d
%s:%i Faled to configure Type B emulation : 0x%04llx
disp0
%s:%i Failed to get boot measurements
NFDriverSecureElementGetPresenceOfAttackLog
%s:%i setting 848
%s:%i Failed to decode plist
%s:%i Got null callback context
%s:%i No SE handle
_Async_NFDriverSetSEAlwaysOn_block_invoke
%s:%i E0 tag cleared successfully.
NFDriverRFSettingsSetupSigned
%s:%i Unable to extract trust object digest from AP Ticket
%s:%i HW is not supported
%s:%i No remote tag handle provided
mutex != NULL
_NFDriverRFSettingsGetRFProp
%s:%i Failed to read RF cal data from FDR.
%s:%i Failed to init se of type %d
_Async_NFDriverUnloadStack_block_invoke
%s:%i Failed to configure Type A emulation : 0x%04llx
%s:%i Failed to load hw
%s:%i ProhibitTimer.Host.Start
%s:%i Failed to set RF config set1.
%s:%i Secondary = %s
%s:%i Chipscope buffer empty
%s:%i SE=%d, power=%d, mailbox=%d
_Callback_NFDriverSETransceive
%s:%i NFDriverConfigureReaderModeRFForMercurySigned: Unable to apply Dynamic RF settings. Trying to reset back to defaults
%s:%i Data length is %ld
%s:%i RSSI stats with no sample
_NFDriverGetSecureFWInfo
NFDriverSecureElement_GetAttackCounterLog
%s:%i Write counter is 0x%x (length = %d)
%s:%i Customer Factory page is NULL.
%s:%i Unexpected status: 0x%X
_Callback_NFDriverNotifyGeneral_block_invoke_2
%s:%i Failed to get data
%s:%i Failed to get MG types
%s:%i Failed to verify sealing : %ld
actualRfConfig
_NFDriverRFSettingsNameForTag
_NF_AMFDRSealingMapCopyLocalDataForClass
_Dispatched_NFDriverGetStackBreadcrumb
_NFDriverApplyRFConfig
%s:%i \t ### HLM debug Log ###
MFG command reply: 
LGD
A10A0151
_NFDriverRFSettingsTLVParser
%s:%i SE in recovery
%s:%i Sending 2F 0x%x to FW
UART Error
%s:%i Wrong interfaceType %d - cannot continue!
%s:%i Polling cfg: A:%d B:%d F:%d 15693:%d S:%d S2:%d S3:%d CustomECP:%d VAS_ECP:%d frameRF:%d
%s:%i Crashing in %d ms
bics-param-set
Error data :
%s:%i Primary = %s
%s:%i MFW Notification received
%s:%i Failed to set ECP Frame
%s:%i %s reader mode static BBA control
%s:%i Invalid logging value
%s:%i Full HCE can't be used with polling
%s:%i Invalid format
%s:%i amfdr is NULL
NFDriverSecureElementGetOSUpdateLog
%s:%i Success!
_Callback_NFDriverNotifyHCE
%s:%i phLibNfc_SE_ActModePwrOff is only available on ese - switching to ActModeOff
%s:%i Resource error
RF_REGISTER_SETTINGS/FDT
%s:%i Sealing status is %d
GetJCOPOSSerialNumber
%s:%i Failed to get integrity check
%s:%i Enabling chipscope
%s:%i Found Kovio tag
%s:%i %02d: %04d %04d %04d %04d %04d %04d %04d %04d
%s:%i %s
%s:%i Failed to get RF settings; status=0x%04llX.
%s:%i Could not get Sealed Data Instance
%s:%i Not updating the rest of OS Info : JCOP is not available
%s:%i Note : OS mode is JCOP
%s:%i Manifest Query is not supported on this OS version (sequence counter: %d)
HW Reset
%s:%i Completion pointer was null
%s:%i Detected Tag (%d) rfTech = %d id= 0x%02x 0x%02x 0x%02x 0x%02x
%s:%i Nuked SE gate info : %llu
_NFDriverEnableMultiRFSettings
%s:%i Generic Debug Notification received without data
NFDriverConfigureExpressFelicaEntry
NFDriverHCISoftReset
%s:%i ==== NFCC/SE TEMPERATURE CONDITION EXITED ====
%s:%i failed to allocate Tx data struct
%s:%i Failed to write miniNV
%s:%i Type-F only
Virtual
A0130428282828A0AF09116FB0281159B02802A098086FF10B8028171717A09E0C07401F9600FA002B52030000A12E03838322A0682A06406003191420400093041880578057E000C000C000A00007FA000000350008007D00003500000E0003A06A1000000000000064000000000000000000A0A8400033
%s:%i Failure for tag 0x%x
%s:%i Unknown SE: %d
NFDriverGetUniqueFDRKey
%04X.%04X-%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X
%s:%i Clearing Multitag info state
_Async_NFDriverConfigRoutingTable_block_invoke
_NFDriverSetISO15693LocalDataRate
GetPresenceOfAttackLog_Eos
%s:%i Failed to get ManifestQuery
%s:%i Error : timeout occured !!!
%s:%i polling=%d emulation=%d field=%d express=%d resume=%d reader config=%d
_NFDriverGetReaderModeRFConfigRegs
(options & (NFDriverCustomerFactoryPageLock | NFDriverCustomerFactoryPageDebug)) == 0
NFDriverDisableLPCDAssist
%s:%i Invalid clock register response
_NFDriverRegisterNCINotifications_block_invoke
_NFDriverConfigureRFLogging
%s:%i SE reader mode event : {se=0x%x, startEnd=%d, poll=0x%x, protocol=0x%x}
%s:%i Unexpected size of AID prefix : %d.
%s:%i Changing RF settings to default
%s:%i SE power up failed. Trying to power off
_Async_NFDriverSetSEMode_block_invoke
A0130419191919A00D03610982A06A1000000000000078000000000000000000A09808EFB50B8019171717A0AF0911FFF419117DA01902A09E0C07001D960090012BD0070000A0940A072003a200314f001902A0682A064060031914204000930418FF7FFF7F8D096E06D8076B0507FA000000350008007D
watchDisplayCheck
%s:%i Running build from (B&I) Stockholm_Base-371.8
_NFDriverAcquireSE
%s:%i %sabling headless mode
%s:%i Disabling chipscope
%s:%i WTX: error, too many WTX
%s:%i Failed to write RF cal data to NFCC
_NFDriverConfigureTemperatureNotifications
hammerfest-spmi
%s:%i Unknown poll mode profile 0x%0x, using default
_Async_NFDriverDumpMemory_block_invoke
%s:%i Failed to clear E0 tag : %d
%s:%i Unable to find config tag info for tag 0x%02x
%s:%i %s : 0x%x
%s:%i Unexpected length for TO_BEFORE_STDBY_CFG : %d
NFDriverSetExpressConfig
NFDriverReadPageEraseCounter
NFDriverClearFactoryPageE0Tag
fwVersion
_NFDriverDebugFailedHW
NFDriverSetRFState
%s:%i Failed to get page : 0x%04llx
%s:%i Invalid length for 0xCB
%s:%i MFW factory page config notification received : NULL
NFDriverGetRFState
_NFDriverEnableWriteCounters
core dump
NFDriverSetEmbeddedSecureElementPower
%s:%i Set output read buffer empty. Not applying new values
GetOSInfo_Host
%s:%i Requested read size is over the limit
Unexpected write counter reply
%s:%i Failed to verify %s(%04X)
GetOSMode_UICC
com.apple.spmi.nfc
%s:%i Driver is null
NFDriverGPIOSetPMUStandbyPowerEnabled
RF deactivated
Feature not supported
%s:%i Invalid opcode 0x%x
NFDriverCopyAndClearAssertion
_Callback_NFDriverNotifyGeneral
NFDriverSetPollingProfile
%s:%i Resuming SE mode to 0x%x (stored routing mode is %d)
_seTypeToID
%s:%i Invalid context 0x%02x
Virtual mode routing failure
%s:%i Status = 0x%x, param=%d
%s:%i Clearing E0 tag from customer factory page.
NFDriverRFSettingsCopySigned
ShSC
%s:%i TLV overrun at tag 0x%02x
MFW factory page config notification received
NFDriverSecureElementSelectWithOS
%s:%i failed to allocate Tx context
_NFDriverConfigureDiscovery: CRC error or response timeout
%s:%i Unexpected length for ISO modulation : %d, expected %d
%s:%i Session State=%d,                     HW Version=0x%x,                     ROM=0x%x,                     Model=0x%x,                     FW=%x.%x,                     MW=%x.%x r%llx,                     Chip=%x                     Lif
No system cal
_NFDriverConfigureReaderModeRFForMercurySigned
%s:%i No vendor RF settings found for %s!
%s:%i 212kbps not supported?
%02X.%02X-%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X
%s:%i [R-RAW<] Soft Reset
%s:%i Failed to read miniNV
%s:%i Unable to get presence of AC log
%s:%i Stack logging failed with 0x%x
%s:%i Failed to enable write counters status:0x%08llx
%s:%i phLibNfc_RemoteDev_CheckPresence failed: 0x%04llx
%s:%i phLibNfc_Ndef_Read failed: 0x%04llx
%s:%i Failed to get RF settings.
%s:%i Failed to allocate se of type %d
GetUptime_P73
%s:%i AC log exists, but supplied output parameter is NULL.
%s:%i Mutex init failed : %d
En
Reader mode prohibit timer
%s:%i Error ! Received boot stop interrupt.
_NFDriverUpdateFactoryPage
ShSB
%s:%i \"%s\" errno=%d Payload length overflow error. 
enable
%s:%i phLibNfc_Mgt_RawCtrlMsgTransceive failed 0x%04llx
%s:%i [L1] %0.6f APCInfo=0x%x tech=0x%x retCode=0x%x vpp=%f ALMPhase=%.3f RMRobustness=0x%04x
%s:%i %s reader mode dynamic BBA control
%s:%i Using EDT RF settings
%s:%i wantsFieldDetect=%d wantsPolling=%d wantsExpress=%d eSE=%d host=%d wantsEcpUpdate=%d
false
NFDriverRemoteDevReceiveAsync
%s:%i ---- Core Dump ----
_Callback_NFDriverESERecovery_SetSEModePowerWired
%s:%i No RF settings.
%s:%i rapdu length too short %d
%s:%i isLoaded=%d flags = 0x%x
%s:%i CRC error
SPMI comms error
%s:%i No NDEF write data provided
Transceive Failure
Tag is non NDEF compliant
_Async_NFDriverGetBootMeasurements_block_invoke
NFDriverSetFelicaSystemCode
%s:%i Felica command is too large: %ld bytes
%s:%i Num Tags Detected=%d, Num Tags Not Interested=%d
_Async_NFDriverSetStandbyMode_block_invoke
%s:%i Using local RF settings
%s:%i Extending timeout 10 seconds. User has requested us to avoid crashing.
en
%s:%i Unable to do any RF operations. Returning false.
_NFDriverRFSettingsApplyFDR2CalData
deactivate
%s:%i semaphore released without signal!
NFDriverSecureElementSendCommandToOS
NFDriverDumpSPMIEventLog
%s:%i WARNING : Disabling SE reader mode Power save. Temperature will rise much faster !
%s:%i Unexpected type
%s:%i WARNING ! Do not send data to JCOP in unknown state !!!!!
NFDriverSecureElementGetDataWithOS
%s:%i Failed to query chip info. Bailing
%s:%i Unknown OS mode %d
_Callback_NFDriverESERecovery_SetSEModePowerOff
%s:%i Error: Failed to power cycle the SE.
%s:%i F0 has testing bit (0x%04x), will overwrite.
%s:%i Invalid offset %d for tag 0x%04x
HW
PHASE_OFFSET_TAG
GetManifestQuery_Eos
%s:%i SMB Tx Blocked!
NFDriverSetSecureElementAlwaysOn: CRC error or response timeout
PMU_CFG_TAG
NFDriverEnableAntiRelay
S16@?0^{_NFCallbackMutex=QiS^v^v}8
%s:%i [C-APDU>] REDACTED %ld bytes
%s:%i cfg=0x%04x addr1=0x%08x len1=0x%04x addr2=0x%08x len2=0x%04x
_Async_NFDriverConfigureDiscovery
NFDriverRFSettingsStoreValueForTagAtOffset
%s:%i %s(%04X) is OK
%s:%i Failed to get FDR key : %d
%s:%i Missing CE interface type
_Callback_NFDriverIoCtl
_NFDriverRFTechToTagType
GetPresenceOfAttackLog
%s:%i Generic error : 0x%04X
%s:%i eSE did not re-enumerate
embedded
%s:%i Failed to setup delayed wake, status = 0x%04X
%s:%i Customer Factory page is unlocked.
%s:%i ERROR: no value !
%s:%i Enabling write counters
GetOSUpdateLog_Eos
_NFDriverConfigureBaudRate_block_invoke
NFDriverPrintPageEraseCounter
A0130428282828A12E03838322A09808ACF00D8028B1B1B1A09E0C07401F9600FA002B52030000A0AF091178B0281159B02802A06A10000000000000C8000000000000000000A0682A0640600319142040009304180044804CC800B200B100AB0007FA000000350008007D00003500000E0003
%s:%i Failed to read clock register
%s:%i AID_MANIFESTQUERY returned error: 0x%04x
%s:%i Setting prevent reset to %d
ctx
NFDriverSecureElement_GetOSUpdateLog
%s:%i SE %d does not support wired mode
%s:%i LPCD false detect counter overflown
Wired
_createSE
CRC Error
%s:%i Can't send to OS %d. Not available.
No module cal
%s:%i > phLibNfc_Mgt_GetNfccParams FAILED
%s:%i ProhibitTimer.Host.End
_NFDriverRFSettingsGetRFPropOnce
%s:%i SE Restricted Mode Enable! OS_ID = %d
%s:%i [L2] %0.6f event=0x%02x debug=0x%02x
_Callback_NFDriverDelayedWake
%s:%i serial number too long: %ld
NFDriverRunIntegrityDebug
%s:%i Failed to get driver info
NFDriverResetFWFlags
SMB log: 
_Async_NFDriverSetNfccParams_block_invoke
%s:%i Device in degraded mode. Wired not available.
%s:%i NFCEE powered off
PC
%s:%i Non-default multitag polling period: %u
%s:%i RTID Debug mode enabled
%s:%i Platform id too long: %ld
%s:%i isLoaded=%d
%s:%i Failed to recover SE
[R-APDU<]
com.apple.nfstack
SE communication error
Degraded mode
%s:%i BPMR=0x%04x FMR=0x%04x CR=0x%04x
%s:%i \t Invalid 'eNfccParam' returned
_getACLogPresence
%s:%i LastAPI=0x%02X, LastAPIStatus=0x%04X DebugInfo=0x%016llX
NFDriverCopySMBLog
%s:%i HFLR=0x%04x PSP=0x%04x MSP=0x%04x
%s:%i Failed to allocate manifest query data
_NFDriverRegisterNCINotifications
%s:%i Embedded SE removed: reason=0x%02x, other=0x%02x
%s:%i UICC already found
%s:%i Polling config is not using ECP
%s:%i BFAR=0x%04x CFSR=0x%04x MMFAR=0x%04x
JDI
seid
%s:%i Not enough storage for cert %d (tag 0x%x). Len = %lu, type = %d !
%s:%i Invalid length for 0xC8
%s:%i status=0x%04X for event %d
_Callback_NFDriverNotifySE_block_invoke
%s:%i Marking ESE reader as enabled!
%s:%i select returned error: 0x%04x
NFDriverSecureElementGetCertificates
Failed to parse TLV 
%s:%i LPCD assist disabled!
_Dispatched_NFDriverGetStackDebugInfo
NFDriverFactoryPageHasProductionContent
_NFDriverRegisterFWDLNotifications_block_invoke
SMB debug: 
%s:%i SE Restricted Mode Exit! OS_ID = %d
com.apple.uart.stockholm
NFDriverEnableAutomaticRFOverride
%s:%i Not supported - skipping on this hardware
%s:%i WARNING : power cycling SE
%s:%i Failed to get JCOP Version
_getCertificateType
%s:%i Queuing exit due to timeout
[TXLDO]
%s:%i Routing changed
%s:%i Unknown value: %d
%s:%i Failed to set GPIO : %u
%s:%i Received Spmi Error Register Info notification: 0x%02x, 0x%02x, 0x%02x , 0x%02x, 0x%02x ,0x%02x
%s:%i Failed to stop polling
Insufficient resource
%s:%i Failed to power cycle SE... it's not coming back folks
%s:%i Transceive failure
%s:%i Got temperature notification SWIO1 / AIO3: %d, 0x%x -> %lf
%s:%i phLibNfc_AntennaSelfTest FAILED : 0x%llx
_NFDriverConfigureBaudRate
%s:%i ==== PLL UNLOCKED ====
Generic Debug Notification received
NFDriverClose
%s:%i Type-A only
%s:%i Types-ABF only
Command rejected
NFDriverUnloadStack
NFDriverRestartDiscovery
_Async_NFDriverGetSecureFWInfo_block_invoke
%s:%i [C-RAW>] Soft Reset
%s:%i Warning : B state cal data was written with A state values. Updating tags ...
%s:%i Get Debug Info failed: %04X
txContext != NULL
%s:%i Failed to write RF cal data B to NFCC
SetPower_UICC
%s:%i Failed to get TO_BEFORE_STDBY_CFG.
%s:%i Allocation failure
%s:%i Found eSE state=%d
Success
%s:%i ==== COMM ERROR ====
%s:%i TXLDO error!
_NFDriverRFSettingsValidate
NFDriverSecureElement_GetOSInfo
%s:%i Failed to VEN reset !!!!! : 0x%04X
%s:%i ESE reader config %d -> %d
%s:%i NFHardwareGetHWConfigTLVs() returned success but out string is null!
%s:%i GET OS MODE
%s:%i Certificate too long: %zu
%s:%i setting 106
%s:%i Failed to configure RF logging : 0x%04llX
%s:%i Received SRAM REPAIR %s notification
%s:%i Failed to configure A08F: 0x%04x
%s:%i Error 0x%x powering off !
_NFDriverConfigureReaderModeDynamicBBA
%s:%i Failed to select
_NFDriverReadHeadless
Received tag value : 
NFDriverRemoteDevFormatNdef
%s:%i Failed to set serial log state : %u
SE OS reset
%s:%i Re-configuring XTAL clock source
%s:%i No data received.
%s:%i Failed to set RF settings : status=0x%04X
%s:%i Failed to stop discovery
com.apple.stockholm.driverQueue.primary
Stack error
NFDriverContinuousWave
%s:%i Headless mini NV already set
_Async_NFDriverHCISoftReset_block_invoke
SPMI_CONFIG_TAG
%s:%i host: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
%s:%i Enabling ECP headless mode
%s:%i Headless is 0x%x (length = %d)
%s:%i Got error 0x%2X
_NFDriverSetGenericATxHappenedTimeout
%s:%i [R-APDU<] REDACTED %ld bytes
%s:%i [L2] %0.6f response=0x%02x status=0x%04x debug=0x%02x vpp=%f ALMPhase=%.3f
%s:%i Unable to get RF Conf register values
%s:%i Failed to get FDR data from local store, trying memory
CRC error
Pad voltage extra info
%s:%i Interval must be < 900 ms
%s:%i No command APDU provided
%s:%i Cannot power cycle, request denied
%s:%i %s SPMI event logging
ESE HIGH
%s:%i Failed to set data rate for NTAG5 %d
%s:%i Customer Factory page has no data.
%s:%i EUICC = %s
FAILURE
Unknown Error
%s:%i hw-config-tlvs: %s
GetOSMode_Host
_NFDriverEnableLpcdAssist
NFDriverTriggerDelayedWake
%s:%i No custom RF settings found!
%s:%i Unsupported hardware.
Not Found
%s:%i [L2] %0.6f state=0x%02x mod=0x%02x rssi=0x%04x, extraInfo=0x%0x fs=0x%04x RMRobustness=0x%04x
%s:%i No sealing manifest
-
%s:%i Intf activation ntf error
%s:%i Disabling headless mode
%s:%i Not enough space allocated to store all page counters
%s:%i Failed to get FDR data : no data.
UniqueChipID
NFDriverSecureElement_GetOSMode
NFCC is in DL mode
%s:%i failed to get config TLV LGD
Memory
NFCallbackMutexCreate
%s:%i LPCD-FC=%d
%s:%i Failed to set XTAL clock source
VerifyData
NFDriverSecureElement_SetPower
%s:%i JCOP branch: %d.%d
%s:%i ---- TICKS ----
UNKNOWN
%s:%i Multitag state query
%s:%i RF=0x%04x, SWP=0x%04x, Kernel=0x%04x, Host=0x%04x, SMB=0x%04x, LowPwr=0x%04x, sys=0x%04x
%s:%i Boot status=%d\n                        ROM=0x%x, HW Version=0x%x, Chip version=0x%04X, Variant=%x, ModelID=%x\n                        Protected status=%x, Lifecycle:{scratch=0x%04X,protected=0x%04X}, vendorFW={scratch=0x%04X,protect
%s:%i failed to get config TLV
%s:%i SEID in manifest is %@
Assert
%s:%i sealingManifestData DataCopy failed
%s:%i Selecting OSU
%s:%i failed to validate EEPROM: 0x%04llX
%s:%i deselected
%s:%i Got SE Removed with status %d
%s:%i OS %d removed for reason 0x%x
%s:%i Found UICC state=%d
%s:%i ***WARNING*** Express mode is requested; express won't work under this config!!!
[HCE R-APDU<]
%s:%i Error, trying to power cycle the SE.
%s:%i (%s) mode=%s
%s:%i Express cfg: Transit:%d Access:%d Generic-A:%d SinglePoll:%d Block:%d Debug:%d
%s:%i Command is too large: %ld bytes
[C-APDU>]
%s:%i Failed : 0x%x
%s:%i Failed to get antenna name from EDT : %s
%s:%i Failed to get RF settings; status=0x%04llX
%s:%i JCOP OS Update Mode detected
%s:%i Invalid manifest length
%s:%i Failed to create page content
%s:%i major = %d, minor %d, build = %d
_NFDriverSetStandbyMode
%s:%i Hardware not supported
%s:%i %s SMB log
_NFBootStopInterruptCallback
%s:%i failed to get config TLV JDI
%s:%i Invalid parameter
com.apple.stockholm.callbackQueue.secondary
%s:%i Missing input tagInfo
Disabling
NFDriverEnableFelicaTxEndPatternV2
%s:%i Failed to set HOST to virtual mode
NFDriverGetFactoryPage
%s:%i Restoring RF
Hardware is unresponsive
%s:%i LR=0x%04x PC=0x%04x XPSR=0x%04x
[lpcd]
%s:%i Failed to fully power off eSE
%s:%i Empty factory page
%s:%i E0 tag not found or already cleared. Nothing to do.
%s:%i Stack load failed with 0x%x, continuing in DL mode.
%s:%i Host already found
Unexpected result
_NFDriverLogLPCDDebug
NFDriverSetPollingConfig
%s:%i Failed to get RF conf settings.
_NFDriverSetRFSettings
%s:%i Unknown chip model ID !
%s:%i ESE reader discovery change requested %d -> %d!
%s:%i Configuring Fury Multitag ECP Frame
%s:%i Warning : B state cal data was written with A state values. Applying ..
%s:%i Failed to parse TLV
_NFDriverConfigureVASFieldDetectShortcuts_block_invoke
NFDriverTriggerCoreDump
%s:%i eSE, enabled=%d
_Callback_NFDriverRemoteDevGetMiFareInfo
NFDriverHWSettingsSetup
_NFDriverRFSettingsGetAntennaName
GetCombined
Aborted
%s:%i NFCC does not support Continuous Wave
%s:%i Unable to create TLV config from hex string
%s:%i MultiTag-FC=%d
_NFDriverRFSettingsIsFDRSealed
%s:%i Cal data for B is correct, flashing.
_NFDriverRFSettingsWriteSignedCalData
%s:%i RSSI stats count %d, min=%d, max=%d, average=%d
NFDriverSetConfiguration
%s:%i Unclassified MIFARE (%d) found
%s:%i tag removed
NFDriverSetSecureElementAlwaysOn
[C-APDU UICC>]
%s:%i Reading Die ID ...
NFDriverEnableSERMPowerSave
%s:%i Flags requested DL mode only.
%s:%i %s SE in DL mode
%s:%i \"%s\" errno=%d Unable to allocate memory for capdu. 
%s:%i Idle=%d
%s:%i Failed to write page : 0x%04llx
GetOSMode_P73
%s:%i ==== UART ERROR ====
ADC LOW
_NFDriverSetStandbyMode: CRC error or response timeout
com.apple.spmi.nfc.hammerfest
%s:%i Unexpected length : %d
_Async_NFDriverGetClrAssertRegs_block_invoke
%s:%i phLibNfc_RemoteDev_Receive failed 0x%04hx
%s:%i Failed to query controller info.
%s:%i Num Tags Added=%d, Detected=%d, Removed=%d, Not Interested=%d
_NFDriverRecoverESE_block_invoke
_NFDriverGetSecureElement
NFDriverSecureElementGetOSInfoJCOP
_NFDriverSetRFSettings_block_invoke
%s:%i target lost
%s:%i Fail to get controller info
NFDriverWriteFactoryPage
NFDriverRFSettingsReadSetting
%s:%i dataClass is NULL
deactivated
%s:%i Enabling reader mode dynamic BBA control
%s:%i Invalid length for 0xC9
NFDriverSetReaderModeRFGain
_NFDriverLogLevel2Updated
%s:%i [L2] %0.6f state=0x%02x mod=0x%02x rssi=0x%04x, ALMPhase=%.3f fs=0x%04x RMRobustness=0x%04x
%s:%i mode=0x%x
%s:%i LPEM flash writes disabled! Headless mode will not be updated on the device.
%s:%i mailbox: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
%s:%i WTX: error %d
%s:%i Failed to get factory page : %d
%s:%i Failed to allocate TLV data
%s:%i Error : unable to write to transition registers
_NFDriverEosUpdateJCOPVersion
%s:%i Unhandled tag type 0x%04x
NFDriverPreventReset
%s:%i \"%s\" errno=%d Invalid L1 standby wake event 0x%x
%s:%i Wrong 'eNfccParam' received!
%s:%i \t Number of L2 debug msgs: %d
%s:%i Host did not re-enumerate
_NFDriverConfigMiniNVForHeadless
default
REDACTED
v8@?0
%s:%i num_dev=%d, status=%d
[C-APDU Guest>]
%s:%i MSPL=0x%04x PSPL=0x%04x PMR=0x%04x
%s:%i Failed to get CF types
%s:%i eSE already found
%s:%i Changing RF settings to alternate
%s:%i Truncated tag found. Tag 0x%02x, tlvLen: %d, idx: %d, len: %d
%s:%i Invalid I/O selected
NFDriverUpdateJCOPVersion
GetOSInfo_UICC
%s:%i Unexpected count of SEs : %d
Invalid parameter
FDT_CONFIG
Local
%s:%i Error : invalid reader event
com.apple.stockholm.callbackQueue.primary
NFDriverGetInternal(driver)->hwInfo != NULL
%s:%i Using cached dieID
%s:%i [L2] %0.6f code=0x%04x
%s:%i 0x%02X TLV doesn't match
%s:%i Not interested Tag (%d) rfTech = %d, rfError = %d, numTagsDet = %d
%s:%i Incorrect T1 %ud, using 320usec!
%s:%i Memory error trying to update property: 0x%02x
Target connection lost
GC_RSSI_THRESHOLD_TAG
_NFDriverConfigureECPPolling
NFDriverRemoteDevCheckPresence
Die ID :
NFDriverSetChipscope
%s:%i RF-proc: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
%s:%i [L1] StandbyEventType=0x%x RegValue=0x%x
_NFDriverSetSEMode: CRC error or response timeout
%s:%i Failed to get instance name
%s:%i Enabling VAS CODES
%s:%i 
_NFDriverSetRFProperty
NFDriverGetPowerCounter: CRC error or response timeout
%s:%i HFSR=0x%04x SFAR=0x%04x SFSR=0x%04x
%s:%i Failed to read headless
_NFDriverSetISO15693LocalDataRate_block_invoke
_NFDriverConfigureHardware
%s:%i Failed to get FDR data : %ld - %s
%s:%i ==== HARDWARE RESET ====
%s:%i Already up-to-date
NFDriverSendMFGCommand
physical GPIO
se
updateInfoData
_getKeySize
%s:%i Failed to get controller info
%s:%i Power state tracking query
%s:%i SE uptime failed to be queried, power=%d, mailbox=%d
%s:%i MW Version is NULL?
%s:%i Note : OS mode is System only
Tag is halted
NFDriverSetHCETypeAConfig
%s:%i Disabling field detection for Single Poll express
%s:%i Failed to allocate buffer.
%s:%i Invalid length %d for tag 0x%x: only %zu remaingin
%s:%i interfaceType:%d path:%s flags:0x%llx  aux path:%s
%s:%i Failed to query FW info !
%s:%i JCOP uptime counter overflown
_NFDriverLogLevel1Updated
%s:%i Returned error: 0x%04x
%s:%i status=0x%04llX
%s:%i ESE Reader config %d -> %d
%s:%i Failed to set A11E tag: 0x%04llx
%s:%i Did not find version tag!
GetManifestQuery_P73
%s:%i unknown express mode type (%d)
%s:%i Failed to disable standby mode.
FollowerID is unresponsive
%s:%i LPCD force always ON
%s:%i No compensation applied due to underflow, poll phase duration (ms): %d
NFDriverGetFlashWriteCounter
%s:%i R0=0x%04x R1=0x%04x R2=0x%04x R3=0x%04x R12=0x%04x
%s:%i Unable to read AP Ticket
%s:%i phLibNfc_RemoteDev_Send failed 0x%04llx
%s:%i Simulating HW Reset
%s:%i [L2] ms=0x%02x µs=0x%02x LMA=0x%02x BBA=0x%02x
%s:%i Disabling boost
%s:%i Failed to set RF settings.
NFCLD_THRESHOLD_TAG
%s:%i RF settings is too short: length=%zu
%s:%i Skipping step %d
%s:%i Got temperature notification SWIO2 / AIO2: %d, 0x%x -> %lf
Successfully updated page with content : 
%s:%i AID_P73_MANIFESTQUERY returned error: 0x%04x
GetAttackCounterLog_UICC
%s:%i Writing headless mini NV 
%s:%i ESE reader as config set (%d / %d)!
Writing customer factory page :
%s:%i Re-init failed. Bailing.
%s:%i Setting polling modulation limit to 100%%
NFDriverDisableHeadlessModeMiniNV
NFDriverISO15693SetDataRate
SPMI RAM info
Off
_NFDriverQuerySPMIErrors_block_invoke
%s:%i Customer Factory page is locked.
%s:%i Failed to create RF settings from clock TLV string %s
%s:%i Compensation applied, poll phase duration (ms): %d
%s:%i Unexpected event: %x
No syscfg cal
%s:%i setting rate: %d
%s:%i Error : invalid response.
GetPresenseOfAttackLog_P73
%s:%i phLibNfc_Ndef_Write failed: 0x%04llx
%s:%i ---- HARD FAULT ----
%s:%i host-LP: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
Unexpected headless reply
%s:%i RF settings = %s
%02X
SealingManifest
%s:%i Failed to setup routing 0x%04llx
%s:%i setting 212
%02X.%04X-%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X
%s:%i configs are identical - skipping.
SPMI Flash info
vGPIO
%s:%i SELECT returned error: 0x%04x
Deactivating
%s:%i Use default ECP value
%s:%i Not supported
%s:%i ProhibitTimer.SE.Start
v16@?0^{phNfc_sData=*I}8
%s:%i Found FDR data, %ld bytes
%s:%i SE %s in download mode
_NFDriverEnableCRC
%s:%i Warning : Standby disabled.
%s:%i Allocation failed
%s:%i Failed to update discovery
NFCC HIGH
%s:%i TxLDO OverCurrent Error
%s:%i old SuicaSystemCode: code 1 enabled: %d, code 1: %04X; code 2 enabled: %d, code 2: %04X
%s:%i Got %x (%d), returning %lf
LMA_RSSI
%s:%i Incorrect manifest query length: %zu
NFDriverSecureElementTransceive
Config
%s:%i Unable to create aid needed for selecting ISD
%s:%i Failed to set A1DF: 0x%08llx
%s:%i LPCD assist completed successfully
%s:%i Missing TX LDO data
Bermuda
%s:%i Not supported on SN100V dev boards - skipping..
%s:%i Max retries reached.
%s:%i failed to enable VAS CODES: 0x%04llX
_Async_NFDriverSetHeadlessMode_block_invoke
%s:%i Types-AB only
_NFDriverRemoteDevTransceive
NFDriverSecureElement_UnlockRequestInfo
Delayed crashing
%s:%i F0 version is 0, treating as unprogrammed.
GetOSMode_Eos
_NFDriverSetControllerInfo
%s:%i Re-using exit threhold
%s:%i XTAL start error received
%s:%i Unknown SE removed: reason=0x%02x, other=0x%02x
%s:%i Failed to set routing
NFDriverEnableSPMIEventLogging
%s:%i failed to %sable headless mode: 0x%04llX
%s:%i %s configured successfully
%s:%i WTX: no info
%s:%i Received empty %s debug info from NFCC
%s:%i Forcing full hce routing
%s:%i \t Number of HLM debug msgs: %d
%s:%i Temperature monitoring configured
Unexpected mini NV reply
%s:%i No SEID in manifest
seal
_NFDriverRFSettingsApplyFDR3CalData
%s:%i ISD sequence counter %d does not match migration update counter %d
NFDriverRemoteDeviceIso14443Transceive
_Async_NFDriverSETransceive_block_invoke
hammerfest
%s:%i ==== GPADC TEMPERATURE CONDITION NORMAL ====
%s:%i deactivated
%s:%i Idle counter overflown
NFDriverSecureElementInit
_NFDriverUpdateKeyWithConfigID
%s:%i L2 logging got null info!
stockholm
%s:%i %s CRC
%s:%i Multitag structure is missing
%s:%i kernel: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
alternate
%s:%i Note : OS mode is Boot Loader
GetAttackCounterLog_Eos
%s:%i Error 0x%x using API %d - requires a reboot !
_NFDriverRegisterFWDLNotifications
%s:%i Multi tag status notification received
%s:%i Unknown type: %d
%s:%i Configuring chipscope
NFDriverClearAutomaticMultiTagPollingState
%s:%i Error : Allocation failure
%s:%i Enabling TypeF headless mode
_Async_NFDriverOpen_block_invoke
_Async_NFDriverSetSEAlwaysOn
%s:%i remote dev list is invalid
%s:%i Invalid param
%s:%i No SE for transceive
NFDriverRedactLogging
%04X.%02X-%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X
NFDriverReadATETrimVersion
%s:%i Failed to power off Host
%s:%i Failed to allocate outParams buffer.
%s:%i Flash counter exceeded notification. This is NOT expected unless you live in the 22nd century or later. File a radar and get a new device.
com.apple.stockholm.driverQueue.secondary
%s:%i No SE of type %d.
Enabling
%s:%i Disabling multi-tag polling, RTID=%d
%s:%i Failed to power off eSE
%s:%i Unexpected length, using custom settings...
%s:%i UICC did not re-enumerate
Firmware error
host
%s:%i Failed to set RF conf settings.
%s:%i Error ! Unexpected cert length 
%s:%i Step %d error : 0x%x
MW requested VEN reset
NFDriverOpen
%s:%i Could not find status container
%s:%i Added Tag (%d) rfTech = %d id= 0x%02x 0x%02x 0x%02x 0x%02x
_NFDriverConfigureRoutingTable
REGISTER UPDATE
%s:%i Setting already present - not updating
dis
%s:%i CW detected!
%s:%i Received %s debug data from NFCC (%u bytes)
SE Recovery Failed
_Callback_NFDriverRemoteDevReceiveAsync
NFDriverCustomerFactoryPageIsUnlocked
NFDriverGetControllerInfo
%s:%i Failed to get DieID
NFDriverEnableSMBLogging
_Dispatched_NFDriverConfigureDiscovery
%s:%i \t pInfo (pointer to L2Debug Info) is NULL!
%s:%i Failed to create RF settings from TLV string %s
%s:%i Failed to get update info
_NFDriverConfigureAIOTemperatureRestriction
NFDriverSetSecureElementPower
NFDriverGetUnlockRequestInfo
%s:%i [L1] %0.6f state=0x%x tech=0x%x rssi=0x%x FelicaL1State=0x%x L1DataRxFailure=0x%x AGCRegValue=0x%x vpp=%f ALMPhase=%.3f fs=0x%x RMRobustness=0x%04x
_Async_NFDriverGetFirmwareVersion_block_invoke
_NFDriverSetSEMode
_NFDriverRFSettingsValidateTag
SUCCESS
[C-APDU System>]
_Callback_NFDriverSERawTransceiveWTX
antenna
%s:%i SELECT: ISD
%s:%i Failed to %s NFCC CRC
%s:%i Enabling single poll headless mode
_Callback_NFDriverESERecovery_SetSEModeResume
Power Off
NO
%s:%i JCOP1 = %s
%s:%i RF=%d
%s:%i Failed to get RF settings registers.
NFDriverGetOSUpdateLog
RTM
NfcB
NFDriverSetHeadlessMode
NFDriverSendMFGCommand_block_invoke
%s:%i [L1] %0.6f state=0x%x tech=0x%x rssi=0x%x FelicaL1State=0x%x L1DataRxFailure=0x%x AGCRegValue=0x%x vpp=%f fs=0x%x RMRobustness=0x%04x
%s:%i Enabling express: transit=%d vas=%d generic-a=%d single_poll=%d debug=%d block=%d 
NFDriverConfigureSPMIIRQ
%s:%i uptimne is %llu
%s:%i SELECT returned error: 0x%04x. Cannot query presence of attack log without selecting ISD
NFCSTATUS_OK == ioctlStatus
%s:%i WARNING !!!\nWARNING !!!\nWriting to Mini NV to disable headless. This is not expected outside factory.\nWARNING !!!
NFDriverGetSWIOTemperature
<empty>
[Reader R-APDU<]
%s:%i Unknown se ID: %d
_Callback_NFDriverSETransceiveWTX
SPMI Event log: 
%s:%i Invalid length for tag 0x%x
%s:%i Found Host state=%d
NFDriverReadDieID
%s:%i Failed to read write counter
%s:%i PC: %d
Core Dump
NFDriverSetTypeATagDataRate
%s:%i Type-B disabled
NFDriverCustomerFactoryPage.c
%s:%i toBeforeStdbyCfg=%d ms, requesting %d
%s:%i Unknown rate %d
_Async_NFDriverSetStandbyMode
ShSA
_Async_NFDriverLoadMW_block_invoke
%s:%i > eNfccParam: %d
%s:%i Unexpected element found in status container: 0x%04x
NFDriverGetBootMeasurements
%s:%i Get stack breadcrumb failed
%s:%i RF counter overflown
NFDriverConfigureAutomaticMultiTagPolling
ECP Frame
%s:%i SE uptime counter overflown
%s:%i SE=%d, JCOP=%d eUICC=%d power=%d, mailbox=%d
NFDriverCopySEIDFromFDR
ShMC
%s:%i Polling config is using Custom ECP
%s:%i Failed to setup SERM power save
%s:%i Received Spmi Error Register Info notification
%s:%i Attempt %d of %d
NFDriverEnableHeadlessTestMode
A0130419191919A00D03610982A09808C0f9088019171717A09E0C07001D960090012BD0070000A0AF0911FFF0191196A01902A06A1000000000000064000000000000000000A0682A064060031914204000930418603F204D450330030B031A0307FA000000350008007D00003500000E0003A0940A0720
_EosParseManifestQuery
%s:%i Invalid length for 0xCA
%s:%i CRC error or response timeout - 0x%04llx
%s:%i Getting SMB log..
%s:%i Mutex already signalled timeout! CB status: %04x
%s:%i CE and Reader not allowed at the same time
%s:%i Failed to allocate buffer
NFDriverGetSecureElementInfo
Assert info
_resumeSEMode
%s:%i Enabling multi-tag polling, RTID=%d
_NFSpmiErrorCallback
%s:%i \t Log is empty!
%s:%i Embedded SE EVT_RESTRICTED!
%s:%i [L2] %0.6f state=0x%02x mod=0x%02x sc=0x%04x, extraInfo=0x%0x RMRobustness=0x%04x
%s:%i Unknown SE type %d
_NFDriverConfigureSEInDownload
%s:%i Follower ID unresponsive!
NFDriverStackInit.c
%s:%i Failed to configure Temperature restrictor : 0x%04llX
%s:%i Failed to set rf property:0x%02x status:0x%08llx
%s:%i ---- Core Dump Addr ----
%s:%i ProhibitTimer.SE.End
%s:%i Values different. Will apply new values
_Callback_NFDriverAntennaSelfTest
%s:%i CFStringGetCStringPtr failed?!
PMU_CONFIG_TAG
%s:%i missing creator for SE type %d
NFDriverAntennaSelfTest_block_invoke
%s:%i Unmatched tag 0x%04x
/mnt1
%s:%i Error ! Unexpected serial number length 
%s:%i Bad response APDU length %d
%s:%i %s TEMPERATURE WARNING RECEIVED
NFDriverDebugDumpMemory
%s:%i FAILED: %s
NFDriverSetReaderModeDynamicBBA
%s:%i Power cycling SE success.
_NFDriverCreateInstanceNameForClassData
%s:%i Not supported for Host SE!
SetPower_Host
NFDriverRemoteDeviceIso15693Transceive
NFDriverRemoteDevCheckNdef
[R-APDU Guest<]
%s:%i failed to set vGPIO tag (0xA008)
GetAttackCounterLog_Host
_NFDriverConfigureVASFieldDetectShortcuts
%s:%i enable: %d
%s:%i \t RAM buffer overflow status  : %d
%s:%i Polling config is using VAS ECP
%{public}s:%i No compensation applied due to underflow, poll phase duration (ms): %d
%{public}s:%i SE=%d, power=%d, mailbox=%d
%{public}s:%i [L2] %0.6f state=0x%02x mod=0x%02x rssi=0x%04x, extraInfo=0x%0x fs=0x%04x RMRobustness=0x%04x
%{public}s:%i Types-ABF only
%{public}s:%i Unknown SE type %d
%{public}s:%i Unexpected length, using custom settings...
%{public}s:%i timeout must be < %dms
%{public}s:%i Failed to set A1DF: 0x%08llx
%{public}s:%i Hardware not supported
%{public}s:%i Failed to create page content
%{public}s:%i CFStringGetCStringPtr failed?!
%{public}s:%i Failed to get controller info
%{public}s:%i Multitag state query
%{public}s:%i phLibNfc_Mgt_GetNfccParams failed 0x%04llx
%{public}s:%i MSPL=0x%04x PSPL=0x%04x PMR=0x%04x
%{public}s:%i Failed to get RF settings registers.
%{public}s:%i Running build from (B&I) Stockholm_Base-371.8
%{public}s:%i Stack load failed with 0x%x
%{public}s:%i Headless is 0x%x (length = %d)
%{public}s:%i Failed to get ManifestQuery
%{public}s:%i NFDriverConfigureReaderModeRFForMercurySigned: Unable to apply Dynamic RF settings. Trying to reset back to defaults
%{public}s:%i Interval must be < 900 ms
%{public}s:%i Missing CE interface type
%{public}s:%i [L1] %0.6f APCInfo=0x%x tech=0x%x retCode=0x%x vpp=%f ALMPhase=%.3f RMRobustness=0x%04x
%{public}s:%i [L2] phase1Abrt=0x%02x phase2Abrt=0x%02x maxRfPulseAbrt=0x%02x successDetect=0x%02x
%{public}s:%i Failed to write page : 0x%04llx
%{public}s:%i Device in degraded mode. Wired not available.
%{public}s:%i Max retries reached.
%{public}s:%i Failed to trigger core dump
%{public}s:%i > phLibNfc_Mgt_GetNfccParams
%{public}s:%i Disabling standby for debugging
%{public}s:%i host-LP: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
%{public}s:%i **** getNfccParamsCb: STATUS = 0x%02X ****
%{public}s:%i dataClass is NULL
%{public}s:%i wantsFieldDetect=%d wantsPolling=%d wantsExpress=%d eSE=%d host=%d wantsEcpUpdate=%d
%{public}s:%i Customer Factory page is NULL.
%{public}s:%i GET OS MODE
%{public}s:%i Not interested Tag (%d) rfTech = %d, rfError = %d, numTagsDet = %d
%{public}s:%i LastAPI=0x%02X, LastAPIStatus=0x%04X DebugInfo=0x%016llX
%{public}s:%i Unknown OS mode %d
%{public}s:%i LR=0x%04x PC=0x%04x XPSR=0x%04x
%{public}s:%i RF-proc: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
%{public}s:%i ---- Core Dump ----
%{public}s:%i E0 tag cleared successfully.
%{public}s:%i Warning : Standby disabled.
%{public}s:%i status=0x%04X
%{public}s:%i MW requested VEN reset.
%{public}s:%i eSE power-on failed! (%d/%d)
%{public}s:%i LPCD-FC=%d
%{public}s:%i Changing RF settings to default
%{public}s:%i Resuming SE mode to 0x%x (stored routing mode is %d)
%{public}s:%i Full HCE can't be used with polling
%{public}s:%i uptimne is %llu
%{public}s:%i Detected Tag (%d) rfTech = %d id= 0x%02x 0x%02x 0x%02x 0x%02x
%{public}s:%i enable=%d
%{public}s:%i ---- HARD FAULT ----
%{public}s:%i Restricted Mode detected
%{public}s:%i WARNING ! Do not send data to JCOP in unknown state !!!!!
%{public}s:%i AC log exists, but supplied output parameter is NULL.
%{public}s:%i Enabling TypeF headless mode
%{public}s:%i Failed to power off Host
%{public}s:%i \t pInfo (pointer to L2Debug Info) is NULL!
%{public}s:%i Unexpected status: 0x%X
%{public}s:%i LPCD false detect counter overflown
%{public}s:%i Failed to get platform identifier
%{public}s:%i Failed to set Prox config : 0x%08llx
%{public}s:%i Driver is null
%{public}s:%i phLibNfc_RemoteDev_Disconnect failed: 0x%04llx
%{public}s:%i eSE not in wired mode
%{public}s:%i Failed to set rf property:0x%02x status:0x%08llx
%{public}s:%i Failed to set serial log state : %u
%{public}s:%i Invalid length for tag 0x%x
%{public}s:%i SELECT: ISD
%{public}s:%i Failed to stop discovery
%{public}s:%i RSSI stats with no sample
%{public}s:%i new SuicaEntrySysCode: code 1 enabled: %d, code 1: %04X; code 2 enabled: %d, code 2: %04X
%{public}s:%i Boot status=%d\n                        ROM=0x%x, HW Version=0x%x, Chip version=0x%04X, Variant=%x, ModelID=%x\n                        Protected status=%x, Lifecycle:{scratch=0x%04X,protected=0x%04X}, vendorFW={scratch=0x%04X
%{public}s:%i Not enough storage for cert %d (tag 0x%x). Len = %lu, type = %d !
%{public}s:%i ERROR: no value !
%{public}s:%i %s : 0x%x
%{public}s:%i SE Restricted Mode Exit! OS_ID = %d
LPCDPolling
%{public}s:%i host: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
%{public}s:%i phLibNfc_RemoteDev_Receive failed 0x%04hx
%{public}s:%i Got FDR data but an error is set : %ld - %s
%{public}s:%i Got temperature notification SWIO2 / AIO2: %d, 0x%x -> %lf
FIELD_OFF
%{public}s:%i [R-APDU<] REDACTED %ld bytes
%{public}s:%i SE uptime counter overflown
%{public}s:%i Success!
%{public}s:%i phLibNfc_RemoteDev_CheckNdef failed: 0x%04llx
%{public}s:%i Failed to set eSE to virtual mode
%{public}s:%i TLV overrun at tag 0x%02x
%{public}s:%i Invalid length for 0xCB
%{public}s:%i Queuing exit due to timeout
%{public}s:%i deactivated
%{public}s:%i Failed to get page : 0x%04llx
%{public}s:%i Invalid offset %d for tag 0x%04x
%{public}s:%i Step %d error : 0x%x
%{public}s:%i Response time : %f us (%d), PICC Response: 0x%04X, PCD response = 0x%04X
%{public}s:%i Got null callback context
%{public}s:%i No RF settings.
%{public}s:%i failed to get config TLV JDI
%{public}s:%i Failed to verify %s(%04X)
%{public}s:%i AMFDRDataCopyTrustObject failed
%{public}s:%i NFCC does not support Continuous Wave
%{public}s:%i ProhibitTimer.SE.End
%{public}s:%i Failed to set eSE to wired mode
%{public}s:%i EEPROM validation failed (%d/%d)
%{public}s:%i Failed to configure Temperature monitoring : 0x%04llX
%{public}s:%i Not supported for Host SE!
%{public}s:%i Mutex init failed : %d
%{public}s:%i Failed to set routing
%{public}s:%i Memory error trying to update property: 0x%02x
%{public}s:%i Disabling chipscope
%{public}s:%i Type-B only
%{public}s:%i Mutex already signalled timeout! CB status: %04x
%{public}s:%i Error 0x%x powering off !
%{public}s:%i Enabling Generic-A headless mode
%{public}s:%i [C-RAW>] Soft Reset
%{public}s:%i Clearing E0 tag from customer factory page.
%{public}s:%i Failed to read registers from NFCC : 0x%4llx
%{public}s:%i Resolve key type from config
%{public}s:%i LPCD assist completed successfully
%{public}s:%i Got SE Removed with status %d
%{public}s:%i Use default ECP value
%{public}s:%i HFLR=0x%04x PSP=0x%04x MSP=0x%04x
%{public}s:%i HFSR=0x%04x SFAR=0x%04x SFSR=0x%04x
%{public}s:%i Error: Failed to power cycle the SE.
%{public}s:%i \t Number of HLM debug msgs: %d
%{public}s:%i Warning : B state cal data was written with A state values. Skipping ..
%{public}s:%i Session State=%d,                     HW Version=0x%x,                     ROM=0x%x,                     Model=0x%x,                     FW=%x.%x,                     MW=%x.%x r%llx,                     Chip=%x                
%{public}s:%i deselected
%{public}s:%i interfaceType:%d path:%s flags:0x%llx
%{public}s:%i Disabling multi-tag polling, RTID=%d
%{public}s:%i phLibNfc_RemoteDev_Transceive failed 0x%04llx
%{public}s:%i Failed to allocate buffer.
%{public}s:%i AID_MANIFESTQUERY returned error: 0x%04x
%{public}s:%i Re-using exit threhold
%{public}s:%i Configuring Fury Multitag ECP Frame
%{public}s:%i [L2] %0.6f command=0x%02x debug=0x%02x rssi=0x%04x
%{public}s:%i Marking ESE reader as disabled!
%{public}s:%i Disabling field detection for Single Poll express
%{public}s:%i Unknown se ID: %d
%{public}s:%i Failed to get RF conf settings.
%{public}s:%i Customer Factory page has no data.
%{public}s:%i semaphore released without signal!
%{public}s:%i Failed to get FDR data : no data.
%{public}s:%i Invalid length : no room for tag
%{public}s:%i Certificate too long: %zu
%{public}s:%i Dropping temperature notification
%{public}s:%i Unexpected size of AID prefix : %d.
%{public}s:%i HW is not supported
%{public}s:%i Setting prevent reset to %d
%{public}s:%i Power state tracking query
%{public}s:%i %s SPMI event logging
%{public}s:%i WTX: error, too many WTX
%{public}s:%i eSE already found
%{public}s:%i Wrong interfaceType %d - cannot continue!
%{public}s:%i Invalid length %d for tag 0x%x: only %zu remaingin
%{public}s:%i Device does not support this feature
%{public}s:%i ---- Core Dump Addr ----
%{public}s:%i Forcing FDR path.
%{public}s:%i failed to validate EEPROM: 0x%04llX
%{public}s:%i wantsFieldDetect=%d wantsPolling=%d wantsExpress=%d eSE=%d host=%d ceType=%d, hasDiscoveryChanges=%d hasRoutingChanges=%d fullHCE=%d
%{public}s:%i Failed to restore discoverty configuration
%{public}s:%i phLibNfc_RemoteDev_Connect failed: 0x%04llx
%{public}s:%i Requested read size is over the limit
%{public}s:%i mailbox: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
%{public}s:%i Found FDR data, %ld bytes
%{public}s:%i setting 106
%{public}s:%i setting 424
%{public}s:%i Types-BF only
%{public}s:%i WTX: no info
%{public}s:%i Failed to set RF conf settings.
%{public}s:%i \t Number of L2 debug msgs: %d
%{public}s:%i Failed to decode plist
%{public}s:%i Failed to set RF settings.
%{public}s:%i BPMR=0x%04x FMR=0x%04x CR=0x%04x
%{public}s:%i \"%s\" errno=%d Invalid L1 standby wake event 0x%x
%{public}s:%i Device does not require RF settings changes
%{public}s:%i F0 version is 0, treating as unprogrammed.
%{public}s:%i F0 has testing bit (0x%04x), will overwrite.
%{public}s:%i This feature is restricted to internal builds.
%{public}s:%i Failure for tag 0x%x
%{public}s:%i \"%s\" errno=%d Unknown migration state: 0x%04x
%{public}s:%i TxLDO OverCurrent Error
%{public}s:%i CRC error or response timeout - 0x%04llx
%{public}s:%i RF=%d
%{public}s:%i Failed to get FDR data : Invalid type.
%{public}s:%i Warning : B state cal data was written with A state values. Updating tags ...
%{public}s:%i WARNING : power cycling SE
%{public}s:%i platform: %d.%d.%d.%d
%{public}s:%i HCE Register error = 0x%04x
%{public}s:%i No memory available
%{public}s:%i Failed to configure Type A emulation : 0x%04llx
%{public}s:%i BFAR=0x%04x CFSR=0x%04x MMFAR=0x%04x
%{public}s:%i Failed to set HOST to virtual mode
%{public}s:%i type=0x%x
%{public}s:%i toBeforeStdbyCfg=%d ms, requesting %d
%{public}s:%i Allocation failure
%{public}s:%i XTAL start error received
%{public}s:%i CE and Reader not allowed at the same time
%{public}s:%i Error 0x%x using API %d - requires a new firmware !
%{public}s:%i Setting already present - not updating
%{public}s:%i %s TEMPERATURE WARNING RECEIVED
%{public}s:%i Received Spmi Error Register Info notification
%{public}s:%i Intf activation ntf error
%{public}s:%i OS %d removed for reason 0x%x
%{public}s:%i Failed to setup routing 0x%04llx
%{public}s:%i JCOP uptime counter overflown
%{public}s:%i Write counter is 0x%x (length = %d)
%{public}s:%i Restoring RF
%{public}s:%i ProhibitTimer.SE.Start
%{public}s:%i Transceive failure
%{public}s:%i Error 0x%x using API %d - requires a reboot !
%{public}s:%i Host already found
%{public}s:%i Faled to configure Type B emulation : 0x%04llx
%{public}s:%i Failed to find tag 0x%04x
%{public}s:%i target lost
%{public}s:%i Failed to disable standby mode.
%{public}s:%i Failed to read miniNV
%{public}s:%i Status = 0x%x, param=%d
%{public}s:%i hw-config-tlvs: %s
%{public}s:%i %s Continuous Wave
%{public}s:%i Platform id too long: %ld
%{public}s:%i Unexpected element found in status container: 0x%04x
%{public}s:%i \"%s\" errno=%d Payload length overflow error. 
%{public}s:%i Failed to get DieID
%{public}s:%i configuring Felica transaction end pattern for applet ver 2.0
%{public}s:%i Failed to clear E0 tag : %d
%{public}s:%i RF config to set: %s
%{public}s:%i Cal data for B is correct, flashing.
%{public}s:%i SE %s in download mode
%{public}s:%i Can't send to OS %d. Not available.
%{public}s:%i failed to allocate buffer
%{public}s:%i %s SMB log
%{public}s:%i [L2] %0.6f state=0x%02x mod=0x%02x sc=0x%04x, extraInfo=0x%0x RMRobustness=0x%04x
%{public}s:%i Platform does not have boot measurements
%{public}s:%i Non-default multitag polling period: %u
%{public}s:%i Values different. Will apply new values
%{public}s:%i amfdr is NULL
%{public}s:%i NFCEE powered off
%{public}s:%i (%s) mode=%s
%{public}s:%i %s(%04X) is OK
%{public}s:%i No sealing manifest
%{public}s:%i Error ! Unexpected cert length 
%{public}s:%i Setting polling modulation limit to 100%%
%{public}s:%i SMB debug : NULL
%{public}s:%i UICC already found
%{public}s:%i Failed to set GPIO : %u
%{public}s:%i Wrong 'eNfccParam' received!
%{public}s:%i EDT antenna name: %s
%{public}s:%i enabling LPCD assist
%{public}s:%i Unexpected length for ISO modulation : %d, expected %d
%{public}s:%i Unknown notification: 0x%x
%{public}s:%i halted
%{public}s:%i Failed to get driver info
%{public}s:%i Empty factory page
%{public}s:%i Got temperature notification SWIO1 / AIO3: %d, 0x%x -> %lf
%{public}s:%i phLibNfc_Mgt_RawCtrlMsgTransceive failed 0x%04llx
%{public}s:%i Headless mini NV already set
%{public}s:%i RF settings is too short: length=%zu
%{public}s:%i Nuked SE gate info : %llu
%{public}s:%i Re-init failed. Bailing.
%{public}s:%i Warning : Standby disabled - skipping enablement.
%{public}s:%i Unknown type: %d
%{public}s:%i ---- ASSERT ----
%{public}s:%i phLibNfc_SE_ActModePwrOff is only available on ese - switching to ActModeOff
%{public}s:%i Failed to set XTAL clock source
%{public}s:%i Note : OS mode is JCOP
%{public}s:%i Multi tag status notification received
%{public}s:%i Failed to recover SE
%{public}s:%i Update successful, previous session state was %d
%{public}s:%i Get Debug Info failed: %04X
%{public}s:%i Enabling single poll headless mode
%{public}s:%i Failed to query chip info. Bailing
%{public}s:%i remote dev list is invalid
%{public}s:%i eSE did not re-enumerate
%{public}s:%i Simulating HW Reset
%{public}s:%i \t RAM buffer overflow status  : %d
%{public}s:%i Error at step %d, re-initializing
%{public}s:%i Added Tag (%d) rfTech = %d id= 0x%02x 0x%02x 0x%02x 0x%02x
%{public}s:%i Failed to set ECP Frame
%{public}s:%i Disabling headless mode
%{public}s:%i L2 logging got null info!
%{public}s:%i Got error 0x%2X
%{public}s:%i Error : function at index %d will never run
%{public}s:%i TIMEOUT!
%{public}s:%i SE Restricted Mode Enable! OS_ID = %d
%{public}s:%i No custom RF settings found!
%{public}s:%i Flags requested DL mode only.
%{public}s:%i ESE reader discovery change requested %d -> %d!
%{public}s:%i Not supported on MWF
%{public}s:%i Got %x (%d), returning %lf
%{public}s:%i RTID Debug mode enabled
%{public}s:%i \t Log is empty!
%{public}s:%i Failed to write RF cal data to NFCC
%{public}s:%i Unexpected length: %zu
%{public}s:%i Enabling write counters
%{public}s:%i Failed to set RF config set1.
%{public}s:%i Failed to allocate outParams buffer.
%{public}s:%i SELECT returned error: 0x%04x. Cannot query presence of attack log without selecting ISD
%{public}s:%i Unknow Key Usage 0x%x
[Hex dump: length=%lu bytes] (%{public}s:%i %{public}s)
%{public}s:%i Unknown SE removed: reason=0x%02x, other=0x%02x
%{public}s:%i SE power up failed. Trying to power off
%{public}s:%i Invalid parameter
%{public}s:%i Unhandled tag type 0x%04x
%{public}s:%i isLoaded=%d
%{public}s:%i Enabling VAS CODES
%{public}s:%i CRC error
%{public}s:%i Generic error : 0x%04X
%{public}s:%i Received %s debug data from NFCC (%u bytes)
%{public}s:%i Missing input tagInfo
%{public}s:%i Invalid logging value
%{public}s:%i MW Version is NULL?
%{public}s:%i Error ! Received boot stop interrupt.
%{public}s:%i > eNfccParam: %d
%{public}s:%i Generic Debug Notification received without data
%{public}s:%i SMB Tx Blocked!
%{public}s:%i failed to set vGPIO tag (0xA008)
%{public}s:%i Failed to load hw
%{public}s:%i No NDEF write data provided
%{public}s:%i Failed to write miniNV
%{public}s:%i F0 has production content (version=0x%04x, type=0x%04x), preserving.
%{public}s:%i failed to get clock TLV
%{public}s:%i Failed to get FDR key : %d
%{public}s:%i Warning : B state cal data was written with A state values. Applying ..
%{public}s:%i Unknown rate %d
%{public}s:%i Unknown parameter !
%{public}s:%i Failed to read clock register
%{public}s:%i Not updating the rest of OS Info : JCOP is not available
%{public}s:%i phLibNfc_RemoteDev_Send failed 0x%04llx
%{public}s:%i setting 848
%{public}s:%i %s
%{public}s:%i Invalid clock register response
%{public}s:%i AID_P73_MANIFESTQUERY returned error: 0x%04x
%{public}s:%i CRC error 0x%x
%{public}s:%i Failed to set A11E tag: 0x%04llx
%{public}s:%i Using local RF settings
%{public}s:%i Error ! Unexpected serial number length 
%{public}s:%i Unexpected length for TO_BEFORE_STDBY_CFG : %d
%{public}s:%i Routing changed
%{public}s:%i ***WARNING*** Express mode is requested; express won't work under this config!!!
%{public}s:%i No SE of type %d.
%{public}s:%i Enabling ECP headless mode
%{public}s:%i Types-AF only
%{public}s:%i NFDriverConfigureReaderModeRFForMercurySigned: Unable to apply Default RF settings
%{public}s:%i Unable to create TLV config from hex string
%{public}s:%i SEID in manifest is %@
%{public}s:%i Polling config is using VAS ECP
%{public}s:%i Command is too large: %ld bytes
%{public}s:%i Invalid data returned: %d
%{public}s:%i NFHardwareGetHWConfigTLVs() returned success but out string is null!
%{public}s:%i Error : unable to write to transition registers
%{public}s:%i Failed to get FDR data : %ld - %s
%{public}s:%i Could not get Sealed Data Instance
%{public}s:%i Failed to write RF cal data B to NFCC
%f
%{public}s:%i Idle counter overflown
%{public}s:%i Setting MultiTag Config. A=%d S=%d S2=%d S3=%d V=%d VASUPA=%d Retries=%d TlvId=%d, debugMode=%d pollDuration=%d pollRetries=%d
%{public}s:%i Failed to resume SE mode
%{public}s:%i Enabling express: transit=%d vas=%d generic-a=%d single_poll=%d debug=%d block=%d 
%{public}s:%i Customer Factory page is unlocked.
%{public}s:%i Manifest Query is not supported on this OS version (sequence counter: %d)
%{public}s:%i Got unknown certificate type??
%{public}s:%i WARNING !!!\nWARNING !!!\nWriting to Mini NV to disable headless. This is not expected outside factory.\nWARNING !!!
%{public}s:%i Unexpected count of SEs : %d
%{public}s:%i Already up-to-date
%{public}s:%i Failed to query FW info !
%{public}s:%i phLibNfc_AntennaSelfTest FAILED : 0x%llx
%{public}s:%i cfg=0x%04x addr1=0x%08x len1=0x%04x addr2=0x%08x len2=0x%04x
%{public}s:%i Failed to parse TLVs, is the format correct ?
%{public}s:%i Failed to get serial number
%{public}s:%i Cond init failed : %d
%{public}s:%i num_dev=%d, status=%d
%{public}s:%i Failed to create data (%lu bytes) with result
%{public}s:%i Truncated tag found. Tag 0x%02x, tlvLen: %d, idx: %d, len: %d
%{public}s:%i Note : OS mode is Boot Loader
%{public}s:%i ISD sequence counter %d does not match migration update counter %d
%{public}s:%i Failed to %s SE in DL mode.
%{public}s:%i Failed to configure RF logging : 0x%04llX
%{public}s:%i Failed to select
%{public}s:%i SE %d does not support wired mode
%{public}s:%i 
%{public}s:%i [L1] %0.6f state=0x%x tech=0x%x rssi=0x%x FelicaL1State=0x%x L1DataRxFailure=0x%x AGCRegValue=0x%x vpp=%f ALMPhase=%.3f fs=0x%x RMRobustness=0x%04x
%{public}s:%i Failed to push Cal to NFCC : 0x%04llx
%{public}s:%i Unable to get presence of AC log
%{public}s:%i select returned error: 0x%04x
%{public}s:%i Invalid length for 0xC9
%{public}s:%i Failed to stop routing
%{public}s:%i Failed to get MG types
%{public}s:%i Sealing status is %d
%{public}s:%i Failed to get JCOP Version
%{public}s:%i failed to register for notifications: 0x%04llX
%{public}s:%i Polling config is not using ECP
NFDriverRemoteDevReadNdef
%{public}s:%i No vendor RF settings found for %s!
%{public}s:%i Using default antenna name %s
%{public}s:%i Failed to get data
%{public}s:%i Unexpected event: %x
%{public}s:%i [L1] StandbyEventType=0x%x RegValue=0x%x
%{public}s:%i [L2] %0.6f state=0x%02x 15693state=0x%02x tech=0x%02X status=0x%02x data=%s
%{public}s:%i \t Invalid 'eNfccParam' returned
%{public}s:%i Failed to setup SERM power save
%{public}s:%i Failed to write RF cal data A to NFCC
%{public}s:%i Failed to allocate se of type %d
%{public}s:%i Unknown chip model ID !
%{public}s:%i Type-B disabled
%{public}s:%i Failed to fully power off eSE
%{public}s:%i WTX: error %d
%{public}s:%i JCOP branch: %d.%d
%{public}s:%i Invalid context 0x%02x
%{public}s:%i CW detected!
%{public}s:%i phLibNfc_Ndef_Write failed: 0x%04llx
%{public}s:%i failed to allocate Tx context
%{public}s:%i Failed to get RF settings.
%{public}s:%i Non-default polling period: %u
%{public}s:%i Type-F only
%{public}s:%i Not supported for UICC!
%{public}s:%i phLibNfc_RemoteDev_CheckPresence failed: 0x%04llx
%{public}s:%i Failed to %s continuous wave
%{public}s:%i Customer Factory page is locked.
%{public}s:%i Disabling boost
%{public}s:%i Unexpected type
%{public}s:%i 212kbps not supported?
%{public}s:%i failed to get config TLV LGD
%{public}s:%i Unable to extract trust object digest from AP Ticket
%{public}s:%i Incompatible firmware !
%{public}s:%i Not supported
%{public}s:%i Configuring chipscope
%{public}s:%i Setting polling period to %u
%{public}s:%i Unable to create aid needed for selecting ISD
%{public}s:%i Bad response APDU length %d
%{public}s:%i Error : timeout occured !!!
%{public}s:%i status=0x%04X for event %d
%{public}s:%i Unknown poll mode profile 0x%0x, using default
%{public}s:%i [R-RAW<] Soft Reset
%{public}s:%i polling=%d emulation=%d field=%d express=%d resume=%d reader config=%d
%{public}s:%i Failed to allocate TLV data
%{public}s:%i %s(%04X) skipped
%{public}s:%i MFW factory page config notification received : NULL
NFDriverRemoteDevWriteNdef
%{public}s:%i SE uptime failed to be queried, power=%d, mailbox=%d
%{public}s:%i LPCD force always OFF
%{public}s:%i Types-AB only
%{public}s:%i No SE handle
%{public}s:%i Unable to get RF Conf register values
%{public}s:%i Using EDT RF settings
%{public}s:%i This API is available in DL mode only
%{public}s:%i %sabling headless mode
%{public}s:%i Unknown value: %d
%{public}s:%i Frame RF INTF activated
%{public}s:%i Data length is %ld
%{public}s:%i Failed to set RF settings : status=0x%04X
%{public}s:%i ==== UART ERROR ====
%{public}s:%i Polling config is using Custom ECP
%{public}s:%i Get stack breadcrumb failed
%{public}s:%i Not interested Tag (%d) rfTech = %d
%{public}s:%i Found Kovio tag
%{public}s:%i Powering SE back ON
%{public}s:%i Missing TX LDO data
%{public}s:%i Host did not re-enumerate
%{public}s:%i phLibNfc_RemoteDev_Receive failed 0x%04llx
%{public}s:%i Failed to read headless
%{public}s:%i Unable to alloc memory 
%{public}s:%i Failed to configure HW settings
%{public}s:%i failed to get config TLV
%{public}s:%i Failed to query controller info.
%{public}s:%i Query AC log presence failed with 0x%02X
%{public}s:%i Multitag structure is missing
ANTI_RELAY
%{public}s:%i UICC did not re-enumerate
%{public}s:%i phLibNfc_RemoteDev_FormatNdef failed: 0x%04llx
%{public}s:%i Incorrect T1 %ud, using 320usec!
%{public}s:%i Enabling multi-tag polling, RTID=%d
%{public}s:%i F0 TLV too short (%d), treating as unprogrammed.
%{public}s:%i Secondary = %s
%{public}s:%i Failed to update discovery
%{public}s:%i SE in recovery
%{public}s:%i Num Tags Detected=%d, Num Tags Not Interested=%d
%{public}s:%i kernel: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
%{public}s:%i 0x%02X TLV doesn't match
%{public}s:%i Skipping step %d
%{public}s:%i eSE Restricted Event %d %d
%{public}s:%i enable: %d
%{public}s:%i Failed 0x%04llx
%{public}s:%i Failed to power cycle SE... it's not coming back folks
%{public}s:%i Set output read buffer empty. Not applying new values
%{public}s:%i Invalid I/O selected
%{public}s:%i failed to set baud rate: 0x%04llX
%{public}s:%i Failed to enable write counters status:0x%08llx
%{public}s:%i Failed to set ECP VAS polling: 0x%08llx
%{public}s:%i Reading Die ID ...
%{public}s:%i > phLibNfc_Mgt_GetNfccParams FAILED
%{public}s:%i PC: %d
%{public}s:%i Completion pointer was null
%{public}s:%i 0x%02X TLV length doesn't match expected (%d)
%{public}s:%i sealingManifestData DataCopy failed
%{public}s:%i Invalid length for 0xCA
%{public}s:%i ==== GPADC TEMPERATURE CONDITION NORMAL ====
%{public}s:%i Removed Tag (%d) rfTech = %d id= 0x%02x 0x%02x 0x%02x 0x%02x
%{public}s:%i Discovery already stopped, don't need to stop again
%{public}s:%i configs are identical - skipping.
%{public}s:%i SWP-proc: pc=0x%04x sp=0x%04x obj=0x%04x state=0x%04x
%{public}s:%i Mini NV headless is 0x%x (length = %d)
%{public}s:%i Failed to get instance name
%{public}s:%i SELECT OS Update AID
%{public}s:%i failed to %sable headless mode: 0x%04llX
%{public}s:%i MultiTag Enabled: %d, Running: %d
%{public}s:%i [L2] %0.6f code=0x%04x
%{public}s:%i ProhibitTimer.Host.End
%{public}s:%i failed to enable VAS CODES: 0x%04llX
%{public}s:%i EMVCO field collision detected
%{public}s:%i Failed to read RF cal data from FDR.
%{public}s:%i GetPresenseOfAttackLog will only work in JCOP mode
%{public}s:%i Temperature restrictor configured
%{public}s:%i Num Tags Added=%d, Detected=%d, Removed=%d, Not Interested=%d
%{public}s:%i TXLDO error!
%{public}s:%i No command APDU provided
%{public}s:%i [L2] %0.6f event=0x%02x debug=0x%02x
%{public}s:%i SE recovery complete. Leaving SE in wired
%{public}s:%i SE is now recovered and set to prior mode
%{public}s:%i Unmatched tag 0x%04x
%{public}s:%i Invalid length for 0xC8
%{public}s:%i Embedded SE removed: reason=0x%02x, other=0x%02x
%{public}s:%i Invalid param
%{public}s:%i RF=0x%04x, SWP=0x%04x, Kernel=0x%04x, Host=0x%04x, SMB=0x%04x, LowPwr=0x%04x, sys=0x%04x
%{public}s:%i Failed to power off eSE
%{public}s:%i SELECT returned error: 0x%04x
%{public}s:%i %s SE in DL mode
%{public}s:%i LPCD assist disabled!
%{public}s:%i ==== COMM ERROR ====
%{public}s:%i Stack logging failed with 0x%x
%{public}s:%i Failed to %s NFCC CRC
%{public}s:%i [L1] %0.6f state=0x%x tech=0x%x rssi=0x%x FelicaL1State=0x%x L1DataRxFailure=0x%x AGCRegValue=0x%x vpp=%f fs=0x%x RMRobustness=0x%04x
%{public}s:%i Error : invalid response.
%{public}s:%i Failed to setup LPCD_CFG
%{public}s:%i %d%% ASK modulation requested.
%{public}s:%i Received SRAM REPAIR %s notification
%{public}s:%i tag removed
%{public}s:%i Reset notification. Len = %d
%{public}s:%i Failed to verify sealing : %ld
%{public}s:%i Returned error: 0x%04x for (0x%x/0x%x)
%{public}s:%i Unexpected length : %d
%{public}s:%i Getting SMB log..
%{public}s:%i Pushing vendor RF settings for %s
%{public}s:%i Did not find version tag!
%{public}s:%i Extending timeout 10 seconds. User has requested us to avoid crashing.
%{public}s:%i Idle=%d
%{public}s:%i ---- WATCHDOG ----
%{public}s:%i Enabling ECP mode since no other is selected.
%{public}s:%i Invalid format
%{public}s:%i Failed to get antenna name from EDT : %s
%{public}s:%i Unsupported hardware.
%{public}s:%i timeout must be < %d
%{public}s:%i MFW Notification received
%{public}s:%i Enabling full HCE routing
%{public}s:%i %s reader mode dynamic BBA control
%{public}s:%i R0=0x%04x R1=0x%04x R2=0x%04x R3=0x%04x R12=0x%04x
%{public}s:%i WARNING : Disabling SE reader mode Power save. Temperature will rise much faster !
%{public}s:%i isLoaded=%d flags = 0x%x
%{public}s:%i Allocation failed
%{public}s:%i No remote tag handle provided
%{public}s:%i Resource error
%{public}s:%i JCOP OS Update Mode detected
%{public}s:%i Crashing in %d ms
%{public}s:%i Unable to do any RF operations. Returning false.
%{public}s:%i Failed to push builtin RF settings.
%{public}s:%i eSE, enabled=%d
%{public}s:%i Failed : 0x%x
%{public}s:%i missing creator for SE type %d
%{public}s:%i Chipscope buffer empty
%{public}s:%i status=0x%04llX, previous state %d
%{public}s:%i Failed to allocate buffer
%{public}s:%i Clearing Multitag info state
%{public}s:%i Failed to get CF types
Stockholm SPMI unresponsive
%{public}s:%i Enabling reader mode dynamic BBA control
NFDriverRemoteDevCheckNdef
%{public}s:%i Failed to read write counter
%{public}s:%i Error : Allocation failure
%{public}s:%i Changing RF settings to alternate
%{public}s:%i Failed to setup delayed wake, status = 0x%04X
%{public}s:%i E0 tag not found or already cleared. Nothing to do.
%{public}s:%i failed to get stack info
%{public}s:%i \"%s\" errno=%d Unable to allocate memory for capdu. 
 mutexStatus=%{public, signpost.description:attribute}llu 
%{public}s:%i RF counter overflown
%{public}s:%i Sending 2F 0x%x to FW
%{public}s:%i ProhibitTimer.Host.Start
%{public}s:%i %s configured successfully
%{public}s:%i Unable to read AP Ticket
%{public}s:%i Cannot power cycle, request denied
%{public}s:%i MultiTag-FC=%d
%{public}s:%i Failed to register notification callback.
Error : timeout occured !!!
%{public}s:%i Failed to get integrity check
%{public}s:%i ==== HARDWARE RESET ====
%{public}s:%i Failed to VEN reset !!!!! : 0x%04X
%{public}s:%i Compensation applied, poll phase duration (ms): %d
%{public}s:%i Received Spmi Error Register Info notification: 0x%02x, 0x%02x, 0x%02x , 0x%02x, 0x%02x ,0x%02x
%{public}s:%i Failed to get FDR data from local store, trying memory
%{public}s:%i Could not find status container
%{public}s:%i Attempt %d of %d
%{public}s:%i FAILED: %s
%{public}s:%i Error, trying to power cycle the SE.
%{public}s:%i Forcing full hce routing
%{public}s:%i Temperature monitoring configured
%{public}s:%i ESE Reader config %d -> %d
%{public}s:%i No SE for transceive
%{public}s:%i Not supported - skipping on this hardware
%{public}s:%i setting rate: %d
%{public}s:%i Customer factory page is locked. Cannot clear E0 tag.
%{public}s:%i Received empty %s debug info from NFCC
FIELD_ON
%{public}s:%i Found Host state=%d
%{public}s:%i Failed to set data rate for NTAG5 %d
%{public}s:%i [L2] ms=0x%02x µs=0x%02x LMA=0x%02x BBA=0x%02x
%{public}s:%i Power cycling SE success.
%{public}s:%i Invalid value for 0x%X, len=%ld
%{public}s:%i JCOP1 = %s
%{public}s:%i Error : invalid reader event
%{public}s:%i enable %02X
%{public}s:%i old SuicaSystemCode: code 1 enabled: %d, code 1: %04X; code 2 enabled: %d, code 2: %04X
%{public}s:%i [L2] %0.6f response=0x%02x status=0x%04x debug=0x%02x vpp=%f ALMPhase=%.3f
%{public}s:%i Re-configuring XTAL clock source
%{public}s:%i No data received.
%{public}s:%i Stack load failed with 0x%x, continuing in DL mode.
%{public}s:%i NFCC flash write query
%{public}s:%i %02d: %04d %04d %04d %04d %04d %04d %04d %04d
%{public}s:%i [L2] %0.6f state=0x%02x mod=0x%02x rssi=0x%04x, ALMPhase=%.3f fs=0x%04x RMRobustness=0x%04x
%{public}s:%i Failed to get RF settings; status=0x%04llX
%{public}s:%i No SEID in manifest
%{public}s:%i Failed to parse TLV
%{public}s:%i unknown express mode type (%d)
%{public}s:%i LPEM flash writes disabled! Headless mode will not be updated on the device.
%{public}s:%i RSSI stats count %d, min=%d, max=%d, average=%d
%{public}s:%i Unable to find config tag info for tag 0x%02x
%{public}s:%i Failed to stop polling
%{public}s:%i failed to allocate Tx data struct
%{public}s:%i ---- TICKS ----
%{public}s:%i ESE reader as config set (%d / %d)!
%{public}s:%i Returned error: 0x%04x
%{public}s:%i rapdu length too short %d
%{public}s:%i %s CRC
%{public}s:%i Failed to configure Temperature restrictor : 0x%04llX
%{public}s:%i Failed to restore SE mode : 0x%x
%{public}s:%i LPCD force always ON
%{public}s:%i mode=0x%x
%{public}s:%i Not enough space allocated to store all page counters
%{public}s:%i Failed to get factory page : %d
%{public}s:%i Failed to create RF settings from TLV string %s
%{public}s:%i Unknown SE: %d
%{public}s:%i Express cfg: Transit:%d Access:%d Generic-A:%d SinglePoll:%d Block:%d Debug:%d
%{public}s:%i Incorrect manifest query length: %zu
%{public}s:%i Invalid manifest length
%{public}s:%i Embedded SE EVT_RESTRICTED!
%{public}s:%i Found UICC state=%d
%{public}s:%i Invalid buffer
%{public}s:%i RF settings = %s
%{public}s:%i \t ### HLM debug Log ###
%{public}s:%i Failed to init se of type %d
%{public}s:%i Note : OS mode is System only
%{public}s:%i Failed to get update info
%{public}s:%i interfaceType:%d path:%s flags:0x%llx  aux path:%s
%{public}s:%i setting 212
%{public}s:%i Unclassified MIFARE (%d) found
%{public}s:%i Not supported on SN100V dev boards - skipping..
%{public}s:%i Failed to create RF settings from clock TLV string %s
%{public}s:%i ==== NFCC/SE TEMPERATURE CONDITION EXITED ====
%{public}s:%i ESE reader config %d -> %d
%{public}s:%i phLibNfc_Ndef_Read failed: 0x%04llx
%{public}s:%i Using cached dieID
%{public}s:%i Enabling chipscope
%{public}s:%i Invalid opcode 0x%x
%{public}s:%i Polling cfg: A:%d B:%d F:%d 15693:%d S:%d S2:%d S3:%d CustomECP:%d VAS_ECP:%d frameRF:%d
%{public}s:%i Type-A only
%{public}s:%i \t FLASH buffer overflow status: %d
%{public}s:%i Follower ID unresponsive!
%{public}s:%i Failed to get boot measurements
%{public}s:%i [C-APDU>] REDACTED %ld bytes
%{public}s:%i Fail to get controller info
%{public}s:%i Failed to configure A08F: 0x%04x
%{public}s:%i Writing headless mini NV 
%{public}s:%i Failed to write IRQ
%{public}s:%i EUICC = %s
%{public}s:%i status=0x%04llX
%{public}s:%i SE=%d, JCOP=%d eUICC=%d power=%d, mailbox=%d
%{public}s:%i Failed to merge RF settings
%{public}s:%i Failed to get RF settings; status=0x%04llX.
%{public}s:%i Failed to get TO_BEFORE_STDBY_CFG.
%{public}s:%i SE reader mode event : {se=0x%x, startEnd=%d, poll=0x%x, protocol=0x%x}
%{public}s:%i profile: %d
%{public}s:%i ---- SPMI ----
%{public}s:%i Marking ESE reader as enabled!
%{public}s:%i Failed to read Module cal data from FDR.
%{public}s:%i serial number too long: %ld
%{public}s:%i Flash counter exceeded notification. This is NOT expected unless you live in the 22nd century or later. File a radar and get a new device.
%{public}s:%i major = %d, minor %d, build = %d
%{public}s:%i Invalid update info length: %zu
%{public}s:%i Re-using entry threhold
%{public}s:%i ==== PLL UNLOCKED ====
%{public}s:%i %s reader mode static BBA control
%{public}s:%i failed to set NTAG5 local rate: 0x%04llX
%{public}s:%i Invalid version tag length %d
%{public}s:%i Found eSE state=%d
%{public}s:%i MultiTag false detect counter overflown
%{public}s:%i Primary = %s
%{public}s:%i Felica command is too large: %ld bytes
%{public}s:%i Failed to allocate manifest query data
%{public}s:%i Selecting OSU
%{public}s:%i DL session already open.
```
