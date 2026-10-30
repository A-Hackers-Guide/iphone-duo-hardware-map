# `/usr/lib/libNFC_HAL.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 260,176 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2160)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/usr/lib/libNFC_HAL.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libnfshared.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (676)

```
IONameMatched
%s:%i Failed to get iterator for service
TRUNCATED
%s:%i HW Debugging - FLOW CHECK - EXPECTED OFF
NFHardwareInterfaceHasExternalSPMIIRQ
+
phOsalNfc_Timer_Init
phOsalNfc_Timer_Stop
NFHardwareGPIOConfigureHammerfestSPMI
NFHardwareSerialGetDefaultInterfaceType
%s:%i Write aborted while in progress.
%s:%i \"%s\" errno=%d getsockopt: SYSPROTO_CONTROL
%s:%i Flow is %s (line=%x)
_phTmlNfc_QuerySPMIErrors
NFHardwareGPIOIsHostWakeCapable
HIGH
_NFHardwareWalkTree
_NFHardwareSerialOpenSocket
%s:%i failed to reset serial
required-gpios
support_virtual_gpio
AppleStockholmControl
NFHardwareSerialIsSupported
_NFHardwareSerialCreateSources_block_invoke
Flush
NFCalibrationGetRFConfigTLVs
download_mode_no_ven
rf-clock-tlv
%s:%i Null serial
%s:%i HW error : unit is not powering cycling.
phOsalNfc_LogFunc
%s:%i Failed to allocate timer context - no space available.
normal_mode
%s:%i \"%s\" errno=%d Failed to query SPMI error registers
%s:%i Invalid callback parameter
support_wake_stockholm
%s:%i Null gpio internals
%s:%i %s has property %s : %s
%s:%i devName: %s  auxDevName: %s
%s:%i Failed to issue follower reset. NACK = %d
_NFHardwareGPIOBootStopInterrupt
NFHardwareSerialReadBlock
[TX>]
((NFHardwareSerialInternal*)(serial->internal))->suspendWriteCount == 1
%s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL:TIOCFLUSH - attempt %d - 
%s:%i \"%s\" errno=%d baudRate=%lu
NFCalibrationCopyAntennaName
CRIT:
%s:%i failed to start timer thread
%s:%i Failed to get timer context for type %d
power_off
phTmlNfc_ParseSpmiDrvErrorStatus
%s:%i Setting Hammerfest SPMI config...
IOClass
%s:%i Failed to init timer: %d
%s:%i Failed to create mutex: %d
%s:%i Debug : Pending read cb = %p, context = %p
phTmlNfc_GetHsuMaxBaudRate
%s:%i Null serial internals
NFHardwareSerialDebugger
%ld.%.3d %s %s
%s:%i HW Debugging - current FLOW CHECK
%s:%i Error detecting interface %s
phTmlNfc_Shutdown
%s:%i Unmapped SPMI register 0x%02X = 0x%02X
%s:%i SPMI register 0x%02X = 0x%02X
_phTmlNfc_SEBootMeasurements
AppleHammerfestSPMI
NFHardwareSerialDebugLog
_NFHardwareSerialDebugSaveLastMessage
%s:%i Failed to release OSAL context - not found
phOsalNfc_LogX32
%s:%i Invalid mode parameter
%s:%i enable=%d
%s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL
NFHardwareSerialGetCTS
Boot-Stop-State
%s:%i HW Debugging - FLOW CHECK - EXPECTED ON
phOsalNfc_Timer_Start
tml->isRunning
%s:%i Not initialized
%s:%i Failed to set device wake. NACK = %d
rf-antenna-name
NFHardwareGetModelID
NFHardwareGPIOValidateSPMIConfig
%s:%i Failed to write, buffer already pending TX. Bytes left = %zu, bytes written = %d, suspend state = %d
%s:%i :%s:%s
pConfig->pContext
phTmlNfc_Write
phTmlNfc_ConfigHsuBaudRate
%s:%i antenna name is missing - no RF?
%s:%i %s is of Type %lx, expecting %lx
%s:%i Unexpected result
NFHardwareSerialSetBaudRate
PKT:
pBuffer!=((void*)0)
%s:%i Failed to read
%s:%i Failed to read : not initialized. Pending read = %d
_phTmlNfc_SetDeviceWake
%s:%i mandatory RF settings %s not present in EDT for this config
%s:%i Unexpected CFType, exp = %lu, actual = %lu
LOW
%s:%i %s=0x%llX
phOsalNfc_Timer_Create
pHwRef!=((void*)0)
%s:%i Failed to create TML context !
_phTmlNfc_SetPower
_phTmlNfc_vGPIO
devicePath != ((void*)0)
%s:%i Ignoring for SPMI
stockholm-spmi
v20@?0Q8B16
nfc,primary,gpio
NFHardwareSerialReadBlock_block_invoke
[RX<]
%s:%i Unexpected state.
%s:%i Failed to release timer context - not found
%s:%i Could not find service: %s
NFHardwareHasFollowerReset
%s:%i Failed to create iterator
%s:%i %s has matching {%s / %s}
%s:%i \"%s\" errno=%d socket
_NFHardwareSerialSPMIIOServiceCallback
Follower-RST
pConfig->pDevNameHsu || pConfig->pDevNameSpmi
%s:%i Invalid phTmlNfc_e_Driver_CRC_Config
%s:%i SPMI registers -- 0x%02X = 0x%02X, 0x%02X = 0x%02X, 0x%02X = 0x%02X, 0x%02X = 0x%02X, 0x%02X = 0x%02X
NFHardwareGPIOSetPowerToggle
NFHardwareGPIOClose
%s:%i %s has child %s
%s:%i HW error : unit is not powering on.
se-spmi-irq
phOsalNfc_LogBool
%s:%i NFC FWBM = 0
%s:%i Invalid code: %d
rf-config-tlvs-10
%s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL:IO_STOCKHOLM_ON_DEMAND_CLIENT
IOUserClientClass
v8@?0
%s:%i Debug : Current read cb = %p, context = %p
phTmlNfc_FlushTxRxBuffers
%s:%i Fail to release connection
%s:%i Could not find service with: %s, retrying slow path
%s:%i Flow is %s
%s:%i \"%s\" errno=%d Failed to set flags
com.apple.stockholm
%s:%i Failed to get timer %llX from context
%s:%i 
%s:%i phTmlNfc_e_EnableDownloadMode
phTmlNfc_SpmiDrvErrorStatus
NFHardwareGPIOSetPower
((NFHardwareSerialInternal*)(serial->internal))->currentWriteBuffer == ((void*)0)
%s:%i baudRate=%lu
SE-Measurements
%s:%i %s=%d
%s:%i Can't start timer %llX
%s:%i FAILED: %s
download_mode
%s:%i \"%s\" errno=%d IO_STOCKHOLM_CRC
vGPIO
%s:%i HW Debugging starting - OFF
WARN:
_phTmlNfc_ReleaseContext
tml->ifc
_phTmlNfc_SerialLogEnable
%s:%i \"%s\" errno=%d getsockopt: SYSPROTO_CONTROL:IO_STOCKHOLM_SPMIERRORS
IOMatchCategory
_NFHardwareSerialSetNonBlock
%s:%i Unknown interface %s
phTmlNfc_IoCtl
%s:%i Failed to release TML context - not found
_phTmlNfc_FreeTMLContext
IOGeneralInterest
length!=0
/dev/
spmi
NFHardwareSerialQuerySPMIError
%s:%i Hammerfest SPMI config is incorrect
uart.log
not reconfigure
_NFHardwareDumpIOKit
%s:%i failed to msg
%s:%i No interface defined for writing
phOsalNfc_IsHeapMemory
phOsalNfc_Init
phOsalNfc_Timer_Deinit
NFHardwareCopyRFConfigTLVs
NFHardwareCopyAntennaName
reconfigure
%s:%i enable toggle=%llu
%s:%i failed to open device %s
%s:%i Failed to load hw
%s:%i Interface %s is not supported?!
%s:%i Not Implemented!!!
nfccModel
NFHardwareGPIOSetDownloadRequest
NFHardwareSerialClose
NFHardwareSerialSetOnDemandClientMode
%s:%i Failed to create matching dictionary
releaseTML
NFHardwareGPIOSetSEBootMeasurements
NFHardwareGPIOGetBootStopState
NFHardwareGPIORegisterBootStopInterruptCallback
%s:%i wrong GPIO driver type: %d
NFHardwareGPIOOpen
%s:%i Socket is blocking !!
%s:%i \"%s\" errno=%d open
%s:%i Failed find IOKit service %s
%s:%i selector=%d enable=%llu : Failed with %#x
%s:%i Only %lu bytes available, requested %zu !
_NFHardwareLookInTree
Sleep
%s:%i Error
%s:%i HW Debugging - POWERING OFF
%s:%i HW debugging result : 0x%04X
%s:%i phTmlNfc_e_Nfc_Tuning %d
support_host_wake_spmi
%s:%i Buffers not allocated
%s:%i Failed to allocate interface %s
%s:%i timer %llX already started
hammerfest-spmi
%s:%i Debug : Pending read %d, read cb = %p, context = %p
%s:%i \"%s\" errno=%d Failed to set non-blocking.
%s:%i Unmatched interface %s
_phTmlNfc_SetPMUStandbyEnabled
_phTmlNfc_DebugMWUnload
_NFHardwareCopyConfigTLV
NFHardwareSerialSetCRCEnabled
%s:%i HW Debugging - WAKE
%s:%i Failed to get timer context
_phOsalNfc_Timer_StartTimer
_phTmlNfc_FollowerReset
NFHardwareGetUARTLogEnabled
%s:%i Failed find IOKit service
support_wake_stockholm_soc
nfc,primary,spmi
NFHardwareSerialWriteBlockAbort
_phOsalNfc_CreateContext
-
%s:%i phTmlNfc_e_EnableDownloadMode_NO_VEN
_phTmlNfc_SetCRCEnable
NFHardwareGPIOSetPMUStandbyPowerEnabled
stockholm-spmi-data-socket
%s:%i Not implemented.
%s:%i %s found
%s:%i phOsalNfc_IsHeapMemory: malloc_default_zone returned NULL
phOsalNfc_RaiseExceptionWithDescription
_phOsalNfc_FreeContext
%s:%i Busy !
phTmlNfc_SetGetSpmiDrvConfigRegs
NFHardwareGPIOSetNFCCBootMeasurements
%s:%i Serial device not opened!
%s:%i failed to open socket %s
%s:%i phTmlNfc_e_EnableNormalMode
%s:%i NFC+SE FWBM = 1
%s:%i \"%s\" errno=%d IO_STOCKHOLM_ON_DEMAND_CLIENT
%s:%i Failed to create property matching dictionary
%s:%i Failed to create CF property string
IOPropertyMatch
IONameMatch
%s:%i %s NOT found
wLength>0
phTmlNfc_ConfigureSpmi
phTmlNfc_RegisterSpmiErrorCallback
NFHardwareSerialWriteBlock_block_invoke
*length>0
%s:%i s_compactTime size = %lu
%s
Rx-Abort
FUNC:
phTmlNfc_Read
Tx-Abort
phOsalNfc_LogStr
TRUE
_phTmlNfc_PowerToggle
%s:%i Failed to send vGPIO. NACK = %d
%s:%i Error ! Unexpected invocation of read handler
NFHardwareSerialFlush_block_invoke
%s:%i Found property %s : %s
%s:%i \"%s\" errno=%d baudRate=%d
%s:%i NFC+SE FWBM = 0
%s:%i Failed to set Hammerfest SPMI config
%s:%i Failed to get valid service
%s:%i Matched name %s, returned 0x%04x
%s:%i %s has no child
Tx
Wake
%s:%i Not connected
%s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL:IO_STOCKHOLM_SPMI_CLEAR_ERRORS
Rx
NFHardwareInterfaceOpen
%s:%i SE FWBM = 1
%s:%i \"%s\" errno=%d 
%s:%i Got a null buffer
%s:%i NFHardwareSerialDebugMsg size = %lu
%s:%i %s=%s
_phTmlNfc_CreateTMLContext
_NFHardwarePrintNode
%s:%i \"%s\" errno=%d Failed to get flags
_NFHardwareSerialCreateSources_block_invoke_2
UARTDumpMaxEntries
Close
NFHardwareInterfaceIsSupported
%s:%i Unable to create notify port
%s:%i Failed with %#x
[TX>] Failed : Busy
NFHardwareInterfaceWriteBlock
/dev/tty.stockholm
%s:%i driverName=%s
MW Initiated
%s:%i phTmlNfc_e_Nfc_CoreDump_Trig %d
AppleHammerfestControl
IOService
%s:%i \"%s\" errno=%d TIOCMSET
%s:%i NFHardwareSerialDebug size = %lu
%s:%i %s=0x%X
_phOsalNfc_Timer_StartTimer_block_invoke
tml->ifc!=NULL
%s:%i stockholm doesn't exist
%s:%i Failed to lookup service : 0x%x
phOsalNfc_LogX64
%s:%i Service %s not available
%s:%i Null gpio
NFHardwareInterfaceResetSerial
%s:%i Invalid parameter
phTmlNfc_Read_block_invoke
%s:%i Validating Hammerfest SPMI config...
%s:%i \"%s\" errno=%d tcgetattr
%s:%i Callback already registered
phOsalNfc_Timer_Delete
pConfig!=((void*)0)
spmi_follower_reset
_phTmlNfc_NFCCBootMeasurements
required-functions
nfc,secondary,gpio
INFO:
%s:%i SE FWBM = 0
rf-config-tlvs
%s:%i Will %s spmi for %s
%s:%i Could not open service (%#x)
%02x
phTmlNfc_Init
%s:%i Hammerfest SPMI config is set
NFHardwareCopyHWConfigTLVs
skip-spmi-reconfig
NFHardwareSkipSpmiReconfig
_NFHardwareGPIOSetValue
%s:%i Printing last %ld messages
(tml->ifc && tml->auxIfc)
%s:%i Fail to release service
NFHardwareGPIOSetVBAT
_NFHardwareSerialRead
%s:%i \"%s\" errno=%d connect
%s:%i \"%s\" errno=%d fcntl: F_SETFL
%s:%i Error ! Unexpected invocation of write handler
%s:%i HW Debugging - ON
tml!=NULL
%s:%i NFC FWBM = 1
_phTmlNfc_ConfigureSPMI
NFHardwareSerialFlush
NFHardwareSerialRegisterSPMIErrorCallback
%s:%i Invalid iterator
%s:%i \"%s\" errno=%d ioctl: TIOCEXCL
NFHardwareLoad
%s:%i Could not get valid dictionary from from IO service object, err: 0x%x.
NFCC-Measurements
%s:%i EXCEPTION=%d REASON=%d
_phTmlNfc_AllocateContext
_phTmlNfc_SetDownload
%s:%i %s doesn't exist
NFHardwareSerialOpen
com.apple.
NFHardwareInterfaceReadBlock
phOsalNfc_LogU32
%s:%i Notification subscription failed: %d
%s:%i Could not find service, trying slow path: %s
AppleStockholmSPMI
%s:%i \"%s\" errno=%d ioctl: CTLIOCGINFO
%s:%i debugger->msgListLength size = %d
%s:%i Failed to read : busy. Pending read = %d
phTmlNfc_ReadAbort
%s:%i phTmlNfc_e_Nfc_Rst_Client
%s:%i Hammerfest SPMI config is good
%s:%i VBAT enable=%d
%s:%i failed to allocate last msg buffer
Open
%s:%i HW Debugging - SLEEP + wait 1.5s
FALSE
%s:%i Timer already initialized for config %d
%s:%i Timer fired late: %f
normal_mode_no_ven
%s:%i Invalid input baud rate
%s:%i Failed to allocate TML context - no space available.
SPMI Wake NACKed
NFHardwareUnload
phTmlNfc_WriteAbort
%s:%i Invalid phTmlNfc_e_Nfc_Tuning
%s:%i Skipping SPMI reconfig.
%s:%i Failed to register Boot stop interrupt callback
rf-config-tlvs-12
spmiFollowerReset
NFHardwareHasVirtualGPIO
hammerfest
%s:%i phTmlNfc_e_PowerOff
%s:%i Invalid phTmlNfc_e_Nfc_CoreDump_Trig
%s:%i Failed to register SPMI error callback
!status
%s:%i selector=%d : Not connected
%s:%i Only got %zu bytes, requested %zu, available %lu.
NFHardwareSerialWriteBlock
buffer!=((void*)0)
retainTML
%s:%i Invalid serial parameter
??
_NFHardwareIsEntryMatching
NFHardwareSerialDebugDump_wCB
RestoreOSBuild
%s:%i Failed to create context for interface %s
NFHardwareDebug
%s:%i Failed to allocate OSAL context - no space available
%s:%i selector=%d enable=%llu : Not connected
((NFHardwareSerialInternal*)(serial->internal))->currentWriteBufferSize == 0
%s:%i ----------------------- IOService plane --------------------------
AppleStockholmControlUserClient
_NFHardwareSerialOpenDeviceNode
_NFHardwareSerialDeleteSources_block_invoke
%s:%i No interface defined for reading
stockholm
%s:%i %s
phTmlNfc_RegisterBootStopInterruptCallback
%s:%i Failed to fetch property: %s
%s:%i Unsupported type: %lu
hw-config-tlvs
%s:%i Error : read in progress since %llu
NFHardwareSerialReset
_NFHardwareGPIOGetValue
_NFHardwareFindMatchingService
%{public}s:%i phTmlNfc_e_EnableDownloadMode
%{public}s:%i Not Implemented!!!
%{public}s:%i Failed to register Boot stop interrupt callback
%{public}s:%i HW Debugging - ON
PHNCINFC
%{public}s:%i Could not get valid dictionary from from IO service object, err: 0x%x.
%{public}s:%i %s
%{public}s%{public}s
%{public}s:%i Not initialized
%{public}s:%i \"%s\" errno=%d Failed to query SPMI error registers
%{public}s:%i %s is of Type %lx, expecting %lx
%{public}s:%i Unable to create notify port
%{public}s:%i HW debugging result : 0x%04X
PHLIBNFC
%{public}s:%i Failed to create TML context !
%{public}s:%i Unsupported type: %lu
%{public}s:%i Failed to create CF property string
%{public}s:%i HW Debugging - SLEEP + wait 1.5s
%{public}s:%i selector=%d enable=%llu : Not connected
%{public}s:%i \"%s\" errno=%d Failed to set non-blocking.
%{public}s:%i Unexpected state.
%{public}s%{public}s=0x%08X
%{public}s:%i Failed to init timer: %d
%{public}s:%i Failed to release timer context - not found
%{public}s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL:IO_STOCKHOLM_ON_DEMAND_CLIENT
%{public}s:%i %s has child %s
%{public}s:%i %s=0x%X
%{public}s:%i failed to start timer thread
%{public}s:%i Invalid parameter
%{public}s:%i \"%s\" errno=%d tcgetattr
%{public}s:%i HW Debugging - POWERING OFF
%{public}s:%i driverName=%s
%{public}s:%i %s=0x%llX
%{public}s:%i SPMI register 0x%02X = 0x%02X
%{public}s:%i Fail to release connection
%{public}s:%i Busy !
Error : read received after shutdown : %p / %p
%{public}s:%i NFC+SE FWBM = 0
%{public}s:%i Invalid input baud rate
%{public}s:%i Unmapped SPMI register 0x%02X = 0x%02X
%{public}s:%i stockholm doesn't exist
%{public}s:%i \"%s\" errno=%d TIOCMSET
%{public}s
%{public}s:%{public}s :%{public}s
%{public}s:%i Failed to send vGPIO. NACK = %d
%{public}s:%i Validating Hammerfest SPMI config...
%{public}s:%i Failed to set Hammerfest SPMI config
%{public}s:%i Invalid callback parameter
%{public}s:%i Could not open service (%#x)
%{public}s:%i Write aborted while in progress.
%{public}s:%i %s doesn't exist
%{public}s:%i \"%s\" errno=%d IO_STOCKHOLM_ON_DEMAND_CLIENT
%{public}s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL
%{public}s:%i Matched name %s, returned 0x%04x
%{public}s:%i \"%s\" errno=%d open
%{public}s:%i Failed to create context for interface %s
%{public}s:%i debugger->msgListLength size = %d
%{public}s:%i phOsalNfc_IsHeapMemory: malloc_default_zone returned NULL
PHLIBNFC_TIMER_ID2
%{public}s:%i Failed to read : busy. Pending read = %d
%{public}s:%i VBAT enable=%d
%{public}s:%i %s has property %s : %s
%{public}s:%i \"%s\" errno=%d Failed to set flags
%{public}s:%i \"%s\" errno=%d fcntl: F_SETFL
%{public}s:%i NFHardwareSerialDebugMsg size = %lu
PHLIBNFC_TIMER_ID5
Allocated Timer
%{public}s:%i Can't start timer %llX
%{public}s:%i FAILED: %s
%{public}s:%i Setting Hammerfest SPMI config...
%{public}s:%i \"%s\" errno=%d getsockopt: SYSPROTO_CONTROL:IO_STOCKHOLM_SPMIERRORS
%{public}s:%i NFC+SE FWBM = 1
%{public}s:%i wrong GPIO driver type: %d
%{public}s:%i phTmlNfc_e_EnableDownloadMode_NO_VEN
%{public}s:%i Failed to issue follower reset. NACK = %d
Deleted Timer
-: WARNING: %{public}s: Expected %{public}s eMWApi{wrong}=%{public}d
timerId %llX, ctlr %d
%{public}s:%i Invalid phTmlNfc_e_Nfc_CoreDump_Trig
%{public}s:%i Service %s not available
%{public}s:%i NFHardwareSerialDebug size = %lu
PHLIBNFC_API
%{public}s:%i Failed to read : not initialized. Pending read = %d
%{public}s:%i Failed with %#x
%{public}s:%i Could not find service, trying slow path: %s
%{public}s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL:IO_STOCKHOLM_SPMI_CLEAR_ERRORS
%{public}s:%i Failed to get iterator for service
%{public}s:%i Failed to allocate interface %s
%{public}s:%i Hammerfest SPMI config is incorrect
%{public}s:%i failed to open socket %s
%{public}s:%i Buffers not allocated
%{public}s:%i HW Debugging - FLOW CHECK - EXPECTED ON
%{public}s:%i Unmatched interface %s
%{public}s:%i Failed to create mutex: %d
%{public}s:%i Failed to allocate timer context - no space available.
%{public}s:%i Could not find service: %s
PHLIBNFC_TIMER_ID1
%{public}s:%i SE FWBM = 1
%{public}s:%i Failed find IOKit service %s
%{public}s:%i EXCEPTION=%d REASON=%d
%{public}s:%i Timer fired late: %f
%{public}s:%i failed to reset serial
%{public}s:%i Will %s spmi for %s
%{public}s:%i \"%s\" errno=%d ioctl: CTLIOCGINFO
%{public}s:%i Debug : Pending read cb = %p, context = %p
%{public}s:%i enable=%d
%{public}s:%i %s NOT found
%{public}s:%i Invalid iterator
%{public}s:%i HW error : unit is not powering cycling.
%{public}s:%{public}s <- %{public}s
%{public}s:%i Failed to register SPMI error callback
%{public}s:%i Not connected
%{public}s:%i selector=%d : Not connected
Error : read already in progress.
%{public}s:%i Only %lu bytes available, requested %zu !
%{public}s:%i Failed to get valid service
%{public}s:%i %s found
PHLIBNFC_NDEF
PHLIBNFC_INFRA
Created Timer
%{public}s:%i Failed to read
%{public}s:%i Invalid mode parameter
%{public}s:%i Failed to write, buffer already pending TX. Bytes left = %zu, bytes written = %d, suspend state = %d
%{public}s:%i \"%s\" errno=%d baudRate=%lu
%{public}s:%i Failed to create matching dictionary
%{public}s:%i phTmlNfc_e_PowerOff
%{public}s:%i mandatory RF settings %s not present in EDT for this config
%{public}s:%i %s=%d
%{public}s:%i :%s:%s
%{public}s:%i Failed to fetch property: %s
%{public}s:%i ----------------------- IOService plane --------------------------
%{public}s:%i \"%s\" errno=%d Failed to get flags
%{public}s:%i Socket is blocking !!
%{public}s:%i failed to allocate last msg buffer
PHLIBNFC_TIMER_ID10
%{public}s:%i Failed find IOKit service
PHOSALNFC
%{public}s:%i Failed to set device wake. NACK = %d
%{public}s:%i HW Debugging starting - OFF
PHLIBNFC_TIMER_ID4
%{public}s:%i Debug : Current read cb = %p, context = %p
%{public}s:%i phTmlNfc_e_EnableNormalMode
%{public}s:%i SE FWBM = 0
%{public}s:%i Null gpio
%{public}s:%i baudRate=%lu
%{public}s:%i failed to msg
%{public}s:%i Found property %s : %s
%{public}s:%i NFC FWBM = 1
%{public}s:%i Flow is %s
%{public}s:%i Failed to release OSAL context - not found
%{public}s:%i %s has matching {%s / %s}
%{public}s:%i No interface defined for writing
%{public}s:%i Debug : Pending read %d, read cb = %p, context = %p
%{public}s:%i failed to open device %s
%{public}s:%i Null serial internals
%{public}s:%i Failed to load hw
%{public}s:%i \"%s\" errno=%d 
PHTMLNFC
%{public}s:%i Failed to get timer context
slot %d, ctlr %d
%{public}s:%i Invalid serial parameter
%{public}s:%i Null gpio internals
%{public}s:%i Error ! Unexpected invocation of read handler
%{public}s:%i No interface defined for reading
%{public}s:%i Failed to allocate TML context - no space available.
%{public}s:%i selector=%d enable=%llu : Failed with %#x
%{public}s:%i Error
PHLIBNFC_DNLD
%{public}s:%i Error detecting interface %s
%{public}s:%i Unexpected CFType, exp = %lu, actual = %lu
%{public}s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL:TIOCFLUSH - attempt %d - 
%{public}s:%i \"%s\" errno=%d connect
%{public}s:%i Got a null buffer
%{public}s:%i HW error : unit is not powering on.
%{public}s:%i Unexpected result
%{public}s:%i \"%s\" errno=%d IO_STOCKHOLM_CRC
%{public}s:%i Error ! Unexpected invocation of write handler
%{public}s:%i Failed to release TML context - not found
%{public}s:%i antenna name is missing - no RF?
%{public}s:%i %s=%s
%{public}s:%{public}s
%{public}s:%i Interface %s is not supported?!
%{public}s:%i \"%s\" errno=%d ioctl: TIOCEXCL
%{public}s:%i timer %llX already started
Error : read received after shutdown : %p / %p. Driver context 0x%016llX
%{public}s:%i Hammerfest SPMI config is good
%{public}s:%i Could not find service with: %s, retrying slow path
%{public}s:%i Timer already initialized for config %d
%{public}s:%i Invalid phTmlNfc_e_Nfc_Tuning
%{public}s:%i Invalid code: %d
%{public}s:%i \"%s\" errno=%d baudRate=%d
%{public}s:%i SPMI registers -- 0x%02X = 0x%02X, 0x%02X = 0x%02X, 0x%02X = 0x%02X, 0x%02X = 0x%02X, 0x%02X = 0x%02X
%{public}s:%i Null serial
%{public}s:%i Unknown interface %s
%{public}s:%i HW Debugging - current FLOW CHECK
PHLIBNFC_HCI
%{public}s:%i Fail to release service
%{public}s:%i Serial device not opened!
%{public}s:%i \"%s\" errno=%d getsockopt: SYSPROTO_CONTROL
PHLIBNFC_TIMER_ID9
Released Timer
%{public}s:%i Only got %zu bytes, requested %zu, available %lu.
%{public}s:%i %s has no child
%{public}s:%i Failed to create iterator
%{public}s:%i Failed to get timer %llX from context
%{public}s:%i Invalid phTmlNfc_e_Driver_CRC_Config
PHLIBNFC_TIMER_ID7
%{public}s:%i phTmlNfc_e_Nfc_Rst_Client
%{public}s:%i Notification subscription failed: %d
PHLIBNFC_API_NEW
%{public}s:%i Printing last %ld messages
Error: Failed to get timer 0x%llX from context
%{public}s:%i Hammerfest SPMI config is set
%{public}s:%i Error : read in progress since %llu
%{public}s:%i Not implemented.
%{public}s:%i \"%s\" errno=%d socket
%{public}s:%i Callback already registered
%{public}s:%i Flow is %s (line=%x)
-: WARNING: %{public}s: Expected %{public}s OR %{public}s eMWApi{wrong}=%{public}d
LIBNFC
PHLIBNFC_TIMER_ID6
PHLIBNFC_TIMER_ID8
%{public}s:%i Failed to create property matching dictionary
%{public}s:%i Failed to lookup service : 0x%x
%{public}s:%i s_compactTime size = %lu
%{public}s:%i HW Debugging - WAKE
%{public}s:%i NFC FWBM = 0
%{public}s:%i Failed to get timer context for type %d
%{public}s:%i devName: %s  auxDevName: %s
PHLIBNFC_TIMER_ID3
%{public}s:%i 
%{public}s:%i phTmlNfc_e_Nfc_Tuning %d
%{public}s:%i enable toggle=%llu
%{public}s:%i Ignoring for SPMI
%{public}s:%i Failed to allocate OSAL context - no space available
%{public}s:%i phTmlNfc_e_Nfc_CoreDump_Trig %d
%{public}s:%i Skipping SPMI reconfig.
-: WARNING: %{public}s: Expected %{public}s eMWApi_Id{wrong}=%{public}d
%{public}s:%i HW Debugging - FLOW CHECK - EXPECTED OFF
```
