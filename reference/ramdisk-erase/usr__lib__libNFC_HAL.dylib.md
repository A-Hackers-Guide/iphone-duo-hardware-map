# `/usr/lib/libNFC_HAL.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 260,176 bytes.

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
%{public}s%{public}s
Released Timer
%{public}s:%i failed to reset serial
%{public}s:%i phTmlNfc_e_EnableDownloadMode_NO_VEN
%{public}s:%i \"%s\" errno=%d Failed to set non-blocking.
%{public}s:%i phTmlNfc_e_Nfc_Rst_Client
%{public}s:%i Unable to create notify port
%{public}s:%i \"%s\" errno=%d baudRate=%d
%{public}s:%i Failed to read : not initialized. Pending read = %d
%{public}s:%i Invalid phTmlNfc_e_Nfc_Tuning
%{public}s:%i Setting Hammerfest SPMI config...
%{public}s:%i Invalid callback parameter
%{public}s:%i phTmlNfc_e_PowerOff
%{public}s:%i wrong GPIO driver type: %d
%{public}s:%i Ignoring for SPMI
%{public}s:%i Failed to create CF property string
%{public}s:%i Failed to allocate timer context - no space available.
%{public}s:%i Error detecting interface %s
%{public}s:%i NFC+SE FWBM = 0
%{public}s:%i \"%s\" errno=%d ioctl: CTLIOCGINFO
PHLIBNFC_TIMER_ID7
%{public}s:%i Failed find IOKit service
%{public}s:%i ----------------------- IOService plane --------------------------
%{public}s:%{public}s :%{public}s
%{public}s:%i Failed to get timer context for type %d
%{public}s:%i Invalid serial parameter
%{public}s:%i failed to open socket %s
%{public}s:%i \"%s\" errno=%d socket
%{public}s:%i \"%s\" errno=%d Failed to query SPMI error registers
%{public}s:%i enable toggle=%llu
%{public}s:%i Service %s not available
%{public}s:%i Could not open service (%#x)
%{public}s:%i failed to start timer thread
Error : read received after shutdown : %p / %p. Driver context 0x%016llX
%{public}s:%i HW Debugging - SLEEP + wait 1.5s
%{public}s:%i NFC FWBM = 1
%{public}s:%i Error : read in progress since %llu
%{public}s:%i Flow is %s (line=%x)
%{public}s:%i HW Debugging starting - OFF
%{public}s:%i Failed to get timer %llX from context
%{public}s:%i Failed to set Hammerfest SPMI config
%{public}s:%i VBAT enable=%d
%{public}s:%i \"%s\" errno=%d baudRate=%lu
%{public}s:%i Found property %s : %s
PHLIBNFC_TIMER_ID9
%{public}s:%i enable=%d
%{public}s:%i NFHardwareSerialDebugMsg size = %lu
%{public}s:%i s_compactTime size = %lu
%{public}s:%i Unsupported type: %lu
%{public}s:%i Failed to allocate interface %s
%{public}s:%i %s=%s
%{public}s:%i Invalid mode parameter
%{public}s:%i Failed to register SPMI error callback
%{public}s:%i Failed to fetch property: %s
%{public}s:%i %s has no child
%{public}s:%i Error ! Unexpected invocation of write handler
PHTMLNFC
Allocated Timer
%{public}s:%i Debug : Current read cb = %p, context = %p
%{public}s:%i failed to allocate last msg buffer
%{public}s:%i SE FWBM = 0
%{public}s:%i Only got %zu bytes, requested %zu, available %lu.
%{public}s:%i EXCEPTION=%d REASON=%d
%{public}s:%i :%s:%s
%{public}s:%i Can't start timer %llX
%{public}s:%i Debug : Pending read %d, read cb = %p, context = %p
%{public}s:%i Skipping SPMI reconfig.
%{public}s:%i Failed to send vGPIO. NACK = %d
%{public}s:%i Not implemented.
%{public}s:%i Invalid iterator
%{public}s:%i %s=0x%X
%{public}s:%i Interface %s is not supported?!
%{public}s:%i Validating Hammerfest SPMI config...
%{public}s:%i stockholm doesn't exist
%{public}s:%i Failed to load hw
%{public}s:%i Will %s spmi for %s
%{public}s:%i %s has child %s
%{public}s:%i Failed to create context for interface %s
%{public}s:%i Failed to read
%{public}s:%i Not Implemented!!!
%{public}s:%i Failed with %#x
PHNCINFC
LIBNFC
%{public}s:%i \"%s\" errno=%d TIOCMSET
%{public}s:%i FAILED: %s
%{public}s:%i Socket is blocking !!
%{public}s:%i 
%{public}s:%i Debug : Pending read cb = %p, context = %p
%{public}s:%i Failed to allocate TML context - no space available.
%{public}s:%i Fail to release connection
%{public}s:%i Unexpected result
%{public}s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL
%{public}s:%i Failed to create iterator
%{public}s:%i HW Debugging - ON
%{public}s:%i Failed to init timer: %d
%{public}s:%i %s doesn't exist
PHLIBNFC_NDEF
%{public}s:%i Notification subscription failed: %d
%{public}s:%i Flow is %s
%{public}s:%i Failed to create property matching dictionary
%{public}s:%i %s has matching {%s / %s}
%{public}s:%i HW debugging result : 0x%04X
%{public}s:%i Invalid parameter
%{public}s:%i Hammerfest SPMI config is good
%{public}s:%i HW Debugging - WAKE
%{public}s:%i HW error : unit is not powering cycling.
%{public}s:%i Failed to write, buffer already pending TX. Bytes left = %zu, bytes written = %d, suspend state = %d
%{public}s:%i Matched name %s, returned 0x%04x
%{public}s:%i antenna name is missing - no RF?
%{public}s:%i No interface defined for writing
%{public}s:%i \"%s\" errno=%d connect
%{public}s:%i Failed to allocate OSAL context - no space available
%{public}s:%i NFC+SE FWBM = 1
%{public}s:%i \"%s\" errno=%d fcntl: F_SETFL
%{public}s:%i HW error : unit is not powering on.
PHLIBNFC_TIMER_ID3
PHLIBNFC_TIMER_ID8
timerId %llX, ctlr %d
%{public}s:%i phTmlNfc_e_EnableNormalMode
%{public}s:%i SPMI register 0x%02X = 0x%02X
%{public}s:%i selector=%d enable=%llu : Not connected
%{public}s:%i Failed to get valid service
%{public}s:%i HW Debugging - current FLOW CHECK
%{public}s:%{public}s
-: WARNING: %{public}s: Expected %{public}s eMWApi{wrong}=%{public}d
%{public}s:%i phTmlNfc_e_EnableDownloadMode
%{public}s:%i Failed to set device wake. NACK = %d
%{public}s:%i Could not find service, trying slow path: %s
%{public}s:%i Write aborted while in progress.
%{public}s:%i \"%s\" errno=%d tcgetattr
%{public}s:%i driverName=%s
%{public}s:%i Failed to release OSAL context - not found
%{public}s:%i Could not find service: %s
%{public}s:%i Failed to get iterator for service
%{public}s:%i Buffers not allocated
%{public}s:%i Unknown interface %s
%{public}s:%i No interface defined for reading
%{public}s:%i Failed to create mutex: %d
%{public}s:%i Serial device not opened!
%{public}s:%i baudRate=%lu
%{public}s:%i \"%s\" errno=%d open
PHLIBNFC_TIMER_ID2
%{public}s:%i Failed find IOKit service %s
%{public}s:%i phTmlNfc_e_Nfc_Tuning %d
%{public}s:%i debugger->msgListLength size = %d
%{public}s:%i NFC FWBM = 0
PHLIBNFC_HCI
Created Timer
Error: Failed to get timer 0x%llX from context
%{public}s:%i Invalid phTmlNfc_e_Driver_CRC_Config
%{public}s:%i Failed to release TML context - not found
%{public}s:%i Error ! Unexpected invocation of read handler
%{public}s:%i %s found
PHOSALNFC
%{public}s:%i Could not get valid dictionary from from IO service object, err: 0x%x.
%{public}s:%i \"%s\" errno=%d Failed to get flags
PHLIBNFC_DNLD
%{public}s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL:TIOCFLUSH - attempt %d - 
%{public}s:%i Unexpected state.
%{public}s:%i %s has property %s : %s
%{public}s:%i \"%s\" errno=%d Failed to set flags
%{public}s:%i devName: %s  auxDevName: %s
%{public}s:%i Unexpected CFType, exp = %lu, actual = %lu
%{public}s:%i Only %lu bytes available, requested %zu !
%{public}s:%i \"%s\" errno=%d 
%{public}s:%i Null serial
PHLIBNFC_TIMER_ID4
slot %d, ctlr %d
Error : read received after shutdown : %p / %p
%{public}s:%i Hammerfest SPMI config is set
Error : read already in progress.
%{public}s:%i \"%s\" errno=%d getsockopt: SYSPROTO_CONTROL:IO_STOCKHOLM_SPMIERRORS
%{public}s:%i Failed to lookup service : 0x%x
%{public}s:%i NFHardwareSerialDebug size = %lu
%{public}s:%i HW Debugging - FLOW CHECK - EXPECTED OFF
%{public}s:%i %s=%d
PHLIBNFC_INFRA
%{public}s:%i Not initialized
%{public}s:%i Hammerfest SPMI config is incorrect
%{public}s:%i failed to open device %s
%{public}s:%i Printing last %ld messages
PHLIBNFC_API
%{public}s:%i Null gpio
%{public}s:%i \"%s\" errno=%d getsockopt: SYSPROTO_CONTROL
%{public}s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL:IO_STOCKHOLM_ON_DEMAND_CLIENT
%{public}s:%i Failed to create matching dictionary
%{public}s:%i %s
%{public}s:%i %s=0x%llX
%{public}s:%i Timer fired late: %f
%{public}s:%i phTmlNfc_e_Nfc_CoreDump_Trig %d
%{public}s:%i SE FWBM = 1
PHLIBNFC_TIMER_ID10
%{public}s:%i %s is of Type %lx, expecting %lx
%{public}s:%i Callback already registered
%{public}s:%i %s NOT found
PHLIBNFC_API_NEW
-: WARNING: %{public}s: Expected %{public}s OR %{public}s eMWApi{wrong}=%{public}d
%{public}s:%i mandatory RF settings %s not present in EDT for this config
%{public}s:%i Fail to release service
%{public}s:%i Failed to get timer context
Deleted Timer
%{public}s:%i Failed to read : busy. Pending read = %d
%{public}s:%i \"%s\" errno=%d IO_STOCKHOLM_ON_DEMAND_CLIENT
%{public}s:%i Timer already initialized for config %d
%{public}s:%i Invalid code: %d
%{public}s:%i selector=%d : Not connected
%{public}s:%{public}s <- %{public}s
PHLIBNFC_TIMER_ID1
%{public}s:%i Failed to release timer context - not found
%{public}s:%i Got a null buffer
PHLIBNFC_TIMER_ID5
%{public}s:%i Unmapped SPMI register 0x%02X = 0x%02X
%{public}s%{public}s=0x%08X
%{public}s:%i Failed to issue follower reset. NACK = %d
%{public}s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL:IO_STOCKHOLM_SPMI_CLEAR_ERRORS
PHLIBNFC_TIMER_ID6
%{public}s:%i SPMI registers -- 0x%02X = 0x%02X, 0x%02X = 0x%02X, 0x%02X = 0x%02X, 0x%02X = 0x%02X, 0x%02X = 0x%02X
%{public}s:%i Null serial internals
%{public}s:%i Error
%{public}s:%i HW Debugging - FLOW CHECK - EXPECTED ON
%{public}s:%i Null gpio internals
%{public}s:%i \"%s\" errno=%d ioctl: TIOCEXCL
%{public}s:%i Invalid input baud rate
%{public}s:%i Could not find service with: %s, retrying slow path
PHLIBNFC
%{public}s:%i Busy !
%{public}s:%i \"%s\" errno=%d IO_STOCKHOLM_CRC
%{public}s:%i HW Debugging - POWERING OFF
%{public}s
-: WARNING: %{public}s: Expected %{public}s eMWApi_Id{wrong}=%{public}d
%{public}s:%i Failed to create TML context !
%{public}s:%i Not connected
%{public}s:%i failed to msg
%{public}s:%i Unmatched interface %s
%{public}s:%i timer %llX already started
%{public}s:%i Invalid phTmlNfc_e_Nfc_CoreDump_Trig
%{public}s:%i Failed to register Boot stop interrupt callback
%{public}s:%i selector=%d enable=%llu : Failed with %#x
%{public}s:%i phOsalNfc_IsHeapMemory: malloc_default_zone returned NULL
rf-clock-tlv
support_wake_stockholm_soc
%s:%i debugger->msgListLength size = %d
%s:%i failed to msg
%s:%i Failed to get timer context for type %d
%s:%i Not Implemented!!!
%s:%i Failed to register SPMI error callback
/dev/
phOsalNfc_Timer_Create
AppleStockholmSPMI
%s:%i \"%s\" errno=%d 
%s:%i \"%s\" errno=%d connect
%s:%i \"%s\" errno=%d fcntl: F_SETFL
%s:%i s_compactTime size = %lu
Flush
CRIT:
pConfig->pContext
%s:%i NFC+SE FWBM = 1
!status
%s:%i selector=%d enable=%llu : Failed with %#x
PKT:
pConfig->pDevNameHsu || pConfig->pDevNameSpmi
phTmlNfc_Write
%s:%i Invalid phTmlNfc_e_Nfc_Tuning
phTmlNfc_SetGetSpmiDrvConfigRegs
IOMatchCategory
%s:%i Callback already registered
%s:%i stockholm doesn't exist
%s:%i \"%s\" errno=%d tcgetattr
%s:%i Debug : Current read cb = %p, context = %p
phTmlNfc_RegisterSpmiErrorCallback
%s:%i Write aborted while in progress.
%s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL
%s:%i %s has no child
%s:%i phOsalNfc_IsHeapMemory: malloc_default_zone returned NULL
%s:%i Not initialized
%s:%i %s doesn't exist
NFHardwareGPIOSetNFCCBootMeasurements
%s:%i Failed to create matching dictionary
%s:%i \"%s\" errno=%d baudRate=%d
NFHardwareSerialDebugger
%s:%i HW error : unit is not powering on.
%s:%i Failed to load hw
-
%s:%i failed to start timer thread
stockholm-spmi
%s:%i Fail to release connection
%s:%i Could not find service with: %s, retrying slow path
%s:%i \"%s\" errno=%d TIOCMSET
%s:%i \"%s\" errno=%d IO_STOCKHOLM_ON_DEMAND_CLIENT
WARN:
%s:%i NFC FWBM = 1
%s:%i Hammerfest SPMI config is incorrect
%s:%i Invalid callback parameter
IOService
_NFHardwareSerialRead
%s:%i \"%s\" errno=%d Failed to get flags
%s:%i Error ! Unexpected invocation of write handler
%s:%i Failed to set device wake. NACK = %d
%s:%i failed to open socket %s
FUNC:
%s:%i Invalid phTmlNfc_e_Nfc_CoreDump_Trig
spmiFollowerReset
NFHardwareGPIORegisterBootStopInterruptCallback
_NFHardwareGPIOSetValue
%s:%i Could not get valid dictionary from from IO service object, err: 0x%x.
NFHardwareSerialWriteBlockAbort
%s:%i Error : read in progress since %llu
%s:%i Invalid code: %d
(tml->ifc && tml->auxIfc)
hw-config-tlvs
%s:%i selector=%d : Not connected
hammerfest
((NFHardwareSerialInternal*)(serial->internal))->currentWriteBufferSize == 0
com.apple.
%s:%i No interface defined for writing
%s:%i Invalid input baud rate
%s:%i antenna name is missing - no RF?
support_host_wake_spmi
length!=0
NFHardwareSerialQuerySPMIError
_NFHardwareWalkTree
%s:%i %s=%d
%s:%i Invalid parameter
phOsalNfc_Timer_Delete
_phTmlNfc_SerialLogEnable
rf-config-tlvs-10
%s:%i Flow is %s (line=%x)
%s:%i ----------------------- IOService plane --------------------------
%s:%i Null serial
pBuffer!=((void*)0)
_phTmlNfc_DebugMWUnload
_phTmlNfc_SEBootMeasurements
NFHardwareGetUARTLogEnabled
NFHardwareSerialGetCTS
%s:%i Not implemented.
*length>0
%02x
AppleStockholmControlUserClient
Rx
vGPIO
%s:%i HW Debugging - FLOW CHECK - EXPECTED ON
%s:%i Unmatched interface %s
%s:%i Invalid phTmlNfc_e_Driver_CRC_Config
_phTmlNfc_SetDeviceWake
%s:%i Unable to create notify port
NFHardwareGPIOClose
_NFHardwareGPIOBootStopInterrupt
%s:%i Only got %zu bytes, requested %zu, available %lu.
NFHardwareSerialWriteBlock_block_invoke
_NFHardwareSerialOpenDeviceNode
phOsalNfc_LogFunc
_phTmlNfc_ReleaseContext
%s:%i failed to reset serial
phTmlNfc_RegisterBootStopInterruptCallback
_phTmlNfc_CreateTMLContext
%s:%i Not connected
NFHardwareGPIOSetPower
NFHardwareGPIOSetVBAT
_phOsalNfc_FreeContext
TRUE
%s:%i Error detecting interface %s
%s:%i %s is of Type %lx, expecting %lx
NFHardwareSerialWriteBlock
%s:%i failed to open device %s
%s:%i Ignoring for SPMI
IONameMatch
%s:%i Can't start timer %llX
phTmlNfc_ConfigHsuBaudRate
NFHardwareHasVirtualGPIO
AppleStockholmControl
NFHardwareSerialReadBlock_block_invoke
_NFHardwareLookInTree
%s:%i \"%s\" errno=%d ioctl: TIOCEXCL
%s:%i failed to allocate last msg buffer
%s:%i EXCEPTION=%d REASON=%d
wLength>0
%s:%i phTmlNfc_e_Nfc_Tuning %d
%s:%i Failed find IOKit service
%s:%i wrong GPIO driver type: %d
NFHardwareSerialSetCRCEnabled
%s:%i %s has matching {%s / %s}
NFHardwareInterfaceResetSerial
support_virtual_gpio
phOsalNfc_Timer_Init
%s:%i Busy !
phTmlNfc_ParseSpmiDrvErrorStatus
_phTmlNfc_NFCCBootMeasurements
NFHardwareCopyHWConfigTLVs
NFHardwareLoad
IOGeneralInterest
phOsalNfc_Timer_Start
%s:%i Failed to release TML context - not found
rf-antenna-name
NFHardwareGPIOValidateSPMIConfig
%s:%i Only %lu bytes available, requested %zu !
%s:%i Unexpected result
NFHardwareSerialSetBaudRate
%s:%i \"%s\" errno=%d getsockopt: SYSPROTO_CONTROL:IO_STOCKHOLM_SPMIERRORS
NFHardwareGetModelID
NFHardwareGPIOSetDownloadRequest
NFHardwareSerialFlush_block_invoke
%s:%i baudRate=%lu
%s:%i Flow is %s
%s:%i \"%s\" errno=%d IO_STOCKHOLM_CRC
_NFHardwarePrintNode
Close
phTmlNfc_WriteAbort
_phTmlNfc_SetDownload
required-gpios
%s:%i Service %s not available
[TX>]
NFHardwareSerialClose
NFHardwareSerialSetOnDemandClientMode
%s:%i Failed to get iterator for service
%s:%i Failed to issue follower reset. NACK = %d
%s:%i Failed to set Hammerfest SPMI config
%s:%i Null gpio
Follower-RST
%s:%i No interface defined for reading
%s:%i HW Debugging - ON
%s:%i HW Debugging - WAKE
%s:%i driverName=%s
phOsalNfc_LogX64
NFHardwareSerialDebugDump_wCB
%s:%i Failed to create TML context !
hammerfest-spmi
%s:%i VBAT enable=%d
[TX>] Failed : Busy
Open
Sleep
%s:%i HW Debugging - current FLOW CHECK
%s:%i HW Debugging starting - OFF
_phTmlNfc_FreeTMLContext
%s:%i Validating Hammerfest SPMI config...
_NFHardwareCopyConfigTLV
%s:%i %s has property %s : %s
%s:%i \"%s\" errno=%d Failed to set flags
%s:%i NFHardwareSerialDebugMsg size = %lu
TRUNCATED
%ld.%.3d %s %s
%s:%i Failed to allocate timer context - no space available.
%s:%i Interface %s is not supported?!
%s:%i Failed to read : busy. Pending read = %d
%s:%i Failed to get valid service
NFHardwareInterfaceOpen
releaseTML
%s:%i Will %s spmi for %s
NFHardwareInterfaceReadBlock
%s:%i HW Debugging - SLEEP + wait 1.5s
NFCalibrationGetRFConfigTLVs
%s:%i Timer already initialized for config %d
%s:%i Failed to get timer context
%s:%i phTmlNfc_e_EnableNormalMode
%s:%i Setting Hammerfest SPMI config...
rf-config-tlvs-12
NFHardwareSkipSpmiReconfig
%s:%i enable toggle=%llu
%s:%i Failed to allocate OSAL context - no space available
_phTmlNfc_AllocateContext
%s:%i SPMI registers -- 0x%02X = 0x%02X, 0x%02X = 0x%02X, 0x%02X = 0x%02X, 0x%02X = 0x%02X, 0x%02X = 0x%02X
_phTmlNfc_SetPower
%s:%i Unsupported type: %lu
_NFHardwareFindMatchingService
%s:%i %s NOT found
%s:%i Buffers not allocated
%s:%i :%s:%s
phTmlNfc_Init
skip-spmi-reconfig
support_wake_stockholm
NFHardwareSerialGetDefaultInterfaceType
%s:%i Matched name %s, returned 0x%04x
%s:%i Printing last %ld messages
RestoreOSBuild
download_mode
%s:%i phTmlNfc_e_EnableDownloadMode_NO_VEN
%s:%i Failed to release OSAL context - not found
%s:%i %s=0x%llX
%s:%i SPMI register 0x%02X = 0x%02X
NFHardwareGPIOSetPowerToggle
HIGH
??
NFCalibrationCopyAntennaName
phOsalNfc_RaiseExceptionWithDescription
FALSE
power_off
%s:%i SE FWBM = 1
%s:%i mandatory RF settings %s not present in EDT for this config
%s:%i Failed find IOKit service %s
%s:%i enable=%d
phOsalNfc_LogStr
phOsalNfc_LogU32
_phTmlNfc_vGPIO
%s:%i Failed with %#x
required-functions
%s:%i Could not find service, trying slow path: %s
IOPropertyMatch
%s
phTmlNfc_ReadAbort
spmi
IOUserClientClass
%s:%i \"%s\" errno=%d open
UARTDumpMaxEntries
SE-Measurements
NFHardwareDebug
%s:%i Error
%s:%i Failed to create mutex: %d
%s:%i Failed to read : not initialized. Pending read = %d
_phTmlNfc_SetPMUStandbyEnabled
NFHardwareCopyRFConfigTLVs
NFHardwareGPIOIsHostWakeCapable
%s:%i Error ! Unexpected invocation of read handler
%s:%i \"%s\" errno=%d socket
Boot-Stop-State
%s:%i SE FWBM = 0
phTmlNfc_ConfigureSpmi
SPMI Wake NACKed
NFHardwareSerialReset
%s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL:IO_STOCKHOLM_ON_DEMAND_CLIENT
NFHardwareInterfaceWriteBlock
/dev/tty.stockholm
NFHardwareInterfaceIsSupported
tml->ifc
spmi_follower_reset
%s:%i Failed to lookup service : 0x%x
NFCC-Measurements
%s:%i HW Debugging - FLOW CHECK - EXPECTED OFF
%s:%i HW Debugging - POWERING OFF
MW Initiated
rf-config-tlvs
NFHardwareCopyAntennaName
[RX<]
_phTmlNfc_FollowerReset
%s:%i Unexpected CFType, exp = %lu, actual = %lu
%s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL:TIOCFLUSH - attempt %d - 
%s:%i \"%s\" errno=%d ioctl: CTLIOCGINFO
NFHardwareGPIOSetPMUStandbyPowerEnabled
%s:%i %s=%s
phOsalNfc_Timer_Deinit
%s:%i phTmlNfc_e_EnableDownloadMode
%s:%i Failed to register Boot stop interrupt callback
NFHardwareHasFollowerReset
%s:%i Failed to write, buffer already pending TX. Bytes left = %zu, bytes written = %d, suspend state = %d
devicePath != ((void*)0)
phTmlNfc_Read_block_invoke
%s:%i Debug : Pending read %d, read cb = %p, context = %p
normal_mode_no_ven
%s:%i phTmlNfc_e_Nfc_Rst_Client
%s:%i Failed to send vGPIO. NACK = %d
not reconfigure
%s:%i Could not open service (%#x)
_NFHardwareGPIOGetValue
%s:%i Failed to init timer: %d
phOsalNfc_LogX32
phOsalNfc_LogBool
%s:%i Failed to release timer context - not found
%s:%i Failed to read
%s:%i Fail to release service
nfc,secondary,gpio
LOW
phOsalNfc_IsHeapMemory
phTmlNfc_SpmiDrvErrorStatus
_phTmlNfc_ConfigureSPMI
%s:%i Hammerfest SPMI config is good
nfccModel
NFHardwareGPIOGetBootStopState
buffer!=((void*)0)
_NFHardwareDumpIOKit
_phOsalNfc_CreateContext
%s:%i timer %llX already started
_phOsalNfc_Timer_StartTimer_block_invoke
AppleHammerfestControl
%s:%i \"%s\" errno=%d baudRate=%lu
%s:%i Found property %s : %s
Rx-Abort
%s:%i Unknown interface %s
+
%s:%i FAILED: %s
pConfig!=((void*)0)
%s:%i \"%s\" errno=%d Failed to query SPMI error registers
retainTML
%s:%i %s has child %s
com.apple.stockholm
Wake
_phTmlNfc_SetCRCEnable
reconfigure
NFHardwareSerialReadBlock
%s:%i Invalid iterator
_NFHardwareSerialSetNonBlock
_NFHardwareSerialCreateSources_block_invoke
_NFHardwareSerialDeleteSources_block_invoke
_NFHardwareSerialSPMIIOServiceCallback
phTmlNfc_IoCtl
download_mode_no_ven
_phOsalNfc_Timer_StartTimer
v8@?0
%s:%i Debug : Pending read cb = %p, context = %p
((NFHardwareSerialInternal*)(serial->internal))->currentWriteBuffer == ((void*)0)
%s:%i Serial device not opened!
_NFHardwareSerialCreateSources_block_invoke_2
%s:%i Hammerfest SPMI config is set
NFHardwareGPIOConfigureHammerfestSPMI
NFHardwareGPIOOpen
%s:%i Failed to create property matching dictionary
%s:%i Failed to create context for interface %s
pHwRef!=((void*)0)
%s:%i 
_phTmlNfc_QuerySPMIErrors
NFHardwareSerialIsSupported
Tx-Abort
%s:%i HW error : unit is not powering cycling.
%s:%i HW debugging result : 0x%04X
%s:%i phTmlNfc_e_PowerOff
INFO:
phOsalNfc_Timer_Stop
phTmlNfc_Shutdown
phTmlNfc_Read
%s:%i Skipping SPMI reconfig.
%s:%i Null gpio internals
stockholm-spmi-data-socket
%s:%i %s=0x%X
%s:%i devName: %s  auxDevName: %s
%s:%i NFC+SE FWBM = 0
nfc,primary,spmi
%s:%i Failed to create CF property string
IOClass
%s:%i \"%s\" errno=%d Failed to set non-blocking.
_NFHardwareSerialDebugSaveLastMessage
%s:%i Failed to allocate TML context - no space available.
uart.log
%s:%i \"%s\" errno=%d setsockopt: SYSPROTO_CONTROL:IO_STOCKHOLM_SPMI_CLEAR_ERRORS
_NFHardwareIsEntryMatching
_NFHardwareSerialOpenSocket
Tx
%s:%i Unexpected state.
NFHardwareInterfaceHasExternalSPMIIRQ
stockholm
%s:%i Failed to get timer %llX from context
%s:%i Timer fired late: %f
tml->isRunning
v20@?0Q8B16
%s:%i \"%s\" errno=%d getsockopt: SYSPROTO_CONTROL
%s:%i phTmlNfc_e_Nfc_CoreDump_Trig %d
%s:%i NFC FWBM = 0
((NFHardwareSerialInternal*)(serial->internal))->suspendWriteCount == 1
NFHardwareSerialFlush
%s:%i Got a null buffer
%s:%i %s
%s:%i Unmapped SPMI register 0x%02X = 0x%02X
%s:%i Failed to fetch property: %s
%s:%i Notification subscription failed: %d
AppleHammerfestSPMI
%s:%i Failed to allocate interface %s
tml!=NULL
tml->ifc!=NULL
%s:%i Invalid mode parameter
phTmlNfc_GetHsuMaxBaudRate
NFHardwareGPIOSetSEBootMeasurements
%s:%i Invalid serial parameter
nfc,primary,gpio
%s:%i %s found
phOsalNfc_Init
NFHardwareUnload
NFHardwareSerialOpen
NFHardwareSerialRegisterSPMIErrorCallback
IONameMatched
%s:%i Null serial internals
%s:%i NFHardwareSerialDebug size = %lu
se-spmi-irq
normal_mode
%s:%i Could not find service: %s
%s:%i Socket is blocking !!
_phTmlNfc_PowerToggle
%s:%i selector=%d enable=%llu : Not connected
%s:%i Failed to create iterator
NFHardwareSerialDebugLog
phTmlNfc_FlushTxRxBuffers
```
