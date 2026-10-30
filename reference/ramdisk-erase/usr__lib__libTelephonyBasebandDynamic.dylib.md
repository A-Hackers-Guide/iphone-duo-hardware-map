# `/usr/lib/libTelephonyBasebandDynamic.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 185,488 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2336)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/usr/lib/libTelephonyBasebandDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (514)

```
HEB
received OCP read ready message\n
v24@?0I8I12^v16
TelephonyBasebandControllerRegisterForEvents
%s: context cannot be NULL\n
skipping intervention since power debug options indicate it should only be applied once
crash-modem-with-spmi
power off
Mux to %u\n
get pmuext on
failed to get coredump ready status\n
Set Baseband State
setting did-intervene-once flag
(power-debug) %s detected\n(power-debug) [continue] c; [skip] s\n(power-debug) 
This command will be blocked until the baseband driver sends an out-of-band notification (e.g. bbutil debug power unblock) or until after %.0f s.
Failed to configure property, ret = 0x%08x\n
TelephonyBasebandControllerAddFreqListExt
done
bad argument\n
no-op
Force Reset\n
TelephonyBasebandControllerSetPPMReportConfig
warm-reset
modem not in reset, proceeding\n
SPMI get-events
com.apple.telephony.powerdebugoptions
kTelephonyBasebandPMUTrace_SOC_TO_VCXO_POST_IDLE
Modem Crash via SPMI\n
mux on
Budget Policy = %llu\n
SPMI Reg0Write: [%s:0x%x]\n
TelephonyBasebandControllerIsBootStageDownABP
Power Debug Unblock\n
_TelephonyBasebandControllerFindMatchingService_sync
AppleBaseband
Skipping Modem Crash via SPMI with reason\n
registered for baseband events\n
_TelephonyBasebandHandlePowerDebugIntervention
power debug command mask value (%u) falls outside acceptable range
failed to safe reset\n
no terminal available so power debug intervention not applied
failed to get reset\n
ShouldOnlyInterveneOnce
power debug intervention value (%u) falls outside acceptable range
Enabling Enumeration to %u\n
Data size (%u) is greater than the max size (%lu)\n
modem not in reset\n
kTelephonyBasebandPMUTrace_SOC_TO_S2R_POST
power on
Skipping Modem Crash via SPMI\n
Remove Frequency list\n
TelephonyBasebandControllerGetBasebandProperty
Reset SPMI
TelephonyBasebandControllerSPMIReg0Write
%s: Failed to add IOService notification, err: 0x%x\n
kTelephonyBasebandPMUTrace_AWAKE_TO_VCXO_POST
kTelephonyBasebandPMUTrace_VCXO_TO_AWAKE_PRE
Modem Coredump GPIO = %u\n
Stopped
power-on
failed to create unblocking thread so skipping block power debug intervention
boot stage down, no need to safe reset\n
failed to open ABP control driver\n
Get Modem PMU Trace\n
unblocked because unblock message received
failed to get boot stage\n
timeout for coredump ready\n
failed to allocate TelephonyBasebandWakeStruct\n
_TelephonyBasebandResetCallback
received coredump ready message\n
kTelephonyBasebandPMUTrace_SOC_TO_VCXO_PRE
TelephonyBasebandControllerInitContext
Set budget policy
Failed to read SPMI HEB\n
received PCI bad request message\n
received billboard is ready message\n
null power debug options arg
TelephonyBasebandControllerSetBasebandProperty
Get PPM Report
_TelephonyBasebandControllerClose
safe reset %u, polling\n
received powering down message\n
not setting power debug options because they are invalid
active
coredump
TelephonyBasebandCreateController
Device not supported\n
TelephonyBasebandControllerEnableModemVBUS
events (%p) or outputStructCnt (%p) is NULL!\n
Invalid config parameter provided\n
safe reset %u\n
%s: Could not create notification port\n
TelephonyBasebandControllerPowerDebugUnblock
TelephonyBasebandControllerSetManagerState
Baseband state = %llu\n
Reset SPMI with data (0x%llx)\n
[%u] timestamp: %s\n
Debug Action\n
TelephonyBasebandControllerGetCoredumpReadyStatus
%Y-%m-%d %H:%M:%S
Failed to self-identify with AppleBaseband\n
power debug unblock timeout
_TelephonyBasebandEventCallback
Unable to communicate with AppleBaseband driver\n
A required input parameter is NULL: context: %p, thermalData: %p, result: %p\n
Get baseband device ID
TelephonyBasebandControllerSPMIRawWrite
failed to allocate TelephonyBasebandCoredumpReadyStruct\n
TelephonyBasebandControllerInitContext_block_invoke
TelephonyBasebandControllerSetModemCoredumpGPIO
TelephonyBasebandControllerGetPMUTrace
failed to retrieve ABP boot stage property\n
failed to retrieve ACIPC boot stage property\n
kTelephonyBasebandPMUTrace_S2R_TO_SOC_POST
%s: Timeout for waiting for the driver!\n
false
set baseband property
failed to detect PCIe control driver variant\n
reset modem
CommandMask
com.apple.libTelephonyUtil
Unknown
%s: TelephonyBaseband
received GNSS Wake ACK message\n
Coredump Ready Status = %llu\n
power-off
TelephonyBasebandControllerPowerOnModem
_TelephonyBasebandControllerServiceNotifyCallback
_TelephonyBasebandPowerDebugUnblockCallback
received unknown baseband event %u\n
checking %s %s %s after %u.%06u seconds\n
SPMI raw-write
SPMI Get Events!\n
failed to set did-intervene-once flag
ret %u, boot stage down %d\n
failed to safe reset via polling\n
TelephonyBasebandControllerPowercycleModem
Failed to find %s service\n
TelephonyBasebandControllerReportThermalData
Report Thermal Data\n
TelephonyBasebandControllerGetPPMReport
_TelephonyBasebandControllerRegisterForService
timed out
TelephonyBasebandControllerIsBootStageDownACIPC
DidInterveneOnce
_TelephonyBasebandControllerCallMethod
_TelephonyBasebandControllerInitContext_sync
This command will be blocked until the baseband driver sends an out-of-band notification (e.g. bbutil debug power unblock)
safe reset %u --done\n
invalid GPIO\n
0x%x 
IDC
failed to create runloop timer
received baseband down message\n
================== POWER DEBUG BLOCKING ==================
TelephonyUtilBasebandController
get peak power budget and thermal budget
_TelephonyBasebandControllerOpen_sync
modem in reset\n
TelephonyBasebandControllerDebugCommand
Skipping Radio on to %u\n
crash modem via spmi
%s: could not open service, ret = 0x%08x\n
TelephonyBasebandControllerIsBootStageDown
Found wake asserted when polling, wake %u, ret %u\n
received powered on message\n
_TelephonyBasebandControllerAllocate
TelephonyBasebandReportThermalData
Modem Crash via SPMI with reason\n
TelephonyBasebandControllerSPMIRawRead
failed to register for resets
Failed to receive interrupt lists\n
_TelephonyBasebandPowerDebugOptionsAreValid
Finished scanning for %s service\n
EnableBBUSB
inactive
SPMI Ready Signal Interrupt
power debug options are set but not for this command, proceeding normally...
_TelephonyBasebandControllerSafeResetModemPolling
IOServiceMatched
kTelephonyBasebandPMUTrace_VCXO_TO_SOC_POST
Unable to communicate with AppleBaseband driver
Radio on to %u\n
coredump off
No data is given!\n
_TelephonyBasebandControllerSafeResetModem
boot Stage Down %d\n
%s: Invalid notification port\n
kTelephonyBasebandPMUTrace_VCXO_TO_AWAKE_POST
Failed to allocate baseband controller.\n
TelephonyBasebandControllerResetModem
TelephonyBasebandControllerCrashModemWithSPMIWithReason
VBUS on to %u\n
invalid baseband controller context\n
TelephonyBasebandControllerPollGPIO
mux off
TelephonyBasebandControllerGNSSTrapTrigger
GNSS trigger trap
Baseband device ID = %llu\n
SPMI Raw Read: [%s:0x%x]\n
SPMI raw-read
GNSS Wake Trigger!\n
Telephony Baseband Command \"%s\" Detected
AppleS5L8930XUSBArbitrator
Clear Frequency list\n
???
received power debug unblock message
_TelephonyBasebandControllerSafeResetModemLegacy
v8@?0
kTelephonyBasebandPMUTrace_AWAKE_TO_VCXO_PRE
Received a request to read %u bytes of a report of type %u\n
%s: could not close service, ret = 0x%08x\n
AppleConvergedIPCICEBBControl
AppleConvergedIPCLedaBBControl
unblock command
get reset
GNSS trigger wake
TelephonyBasebandControllerGetBasebandDeviceID
somehow neither unblock message was received nor did timeout occur
timeout for wake\n
received wake-asserted message\n
Failed to create %s instance\n
TelephonyBasebandControllerForceResetModem
TelephonyBasebandControllerGNSSWakeTrigger
failed to get BootStageDown state\n
cannot do safe reset from this runloop context\n
A required input parameter is NULL: ref: %p, data: %p, result: %p\n
Reset\n
GNSS Trap Trigger!\n
[%u] bus: %s\n
failed to get power debug options
get baseband property
Invalid report parameter provided\n
_TelephonyBasebandPowerDebugBlockingThread
_TelephonyBasebandControllerCallMethodGeneric
IOGeneralInterest
received OCP write message\n
kTelephonyBasebandPMUTrace_VCXO_TO_SOC_PRE
true
TelephonyBasebandControllerCrashModemWithSPMI
TelephonyBasebandControllerEnableModemMux
AppleBasebandPCIControl
received wake deasserted message\n
TelephonyBasebandController
OCP Tx Ready Interrupt
CoreDump Ready Interrupt
cold-reset
_TelephonyBasebandControllerInsertInEventQueue
received GNSS Trap ACK message\n
_wireless
TelephonyBasebandControllerInitContext_block_invoke_2
%s: AppleBaseband IOService is not found. Finding it via matching service\n
TelephonyBasebandControllerSPMIGetEvents
received baseband up message\n
received PCI Cpl message\n
TelephonyBasebandSetPowerDebugOptionsInternal
Intervention
kTelephonyBasebandPMUTrace_SOC_TO_S2R_PRE
TelephonyBasebandControllerNoOp
received PCIAER message\n
================== POWER DEBUG UNBLOCKED =================
kTelephonyBasebandPMUTrace_S2R_TO_SOC_PRE
No Op (should skip = %s)\n
Failed to query GPIO %s\n
get manager state
get reset request
Baseband property = %llu\n
\n
SPMI reg0write
Billboard Tx Ready Interrupt
[%u] interrupt source: %s\n
Received %u configs\n
\tReport type: %u, Report Config: %u\n
sQueue
usb on
usb off
TelephonyBasebandControllerRemoveFreqListExt
Data: 
_TelephonyBasebandPowerDebugTimeoutCallback
Could not create run loop source\n
TimeoutMilliseconds
Skipping Reset\n
powercycle modem
RESET_REQUEST
output: 0x%x\n
Skipping Force Reset\n
TelephonyBasebandControllerResetSPMI
Skipping Powercycle\n
TelephonyBasebandControllerGetPPMBudget
%s: no service is found\n
_TelephonyBasebandHandlePowerDebugInterventionAsk
failed to create baseband controller
kTelephonyBasebandPMUTrace_Invalid
TelephonyBasebandSetPowerDebugOptions
UNDEFINED_PIN
OCP Rx Ready Interrupt
%s: Invalid queue\n
failed to open ACIPC control driver\n
failed to allocate TelephonyBasebandEventStruct\n
received baseband alive message\n
TelephonyBasebandGetPowerDebugOptionsInternal
TelephonyBasebandControllerSetCPMSBudgetPolicy
Get budget policy
%s: Failed to find %s service, registering for matching notification\n
Notification port was not successfully created\n
Could not add interest notification on service: %#x\n
TelephonyBasebandControllerEnableModemUSBEnumerationWithAP
TelephonyBasebandControllerSetBasebandState
failed to get PMUExtOn\n
kTelephonyBasebandPMUTrace_SOC_TO_VCXO_POST_CONN
Failed reading data!\n
Skipping Modem Coredump GPIO = %u\n
Remove frequency list
Started
coredump on
clear frequency list
get baseband state
TelephonyBasebandControllerGetBasebandState
received reset detected message\n
get coredump ready status
Set PPM Report Config
%s: operation '%s' failed: 0x%08x\n
received PCI link down message\n
Powercycling\n
Manager state = %llu\n
SPMI Raw Write: [%s:0x%x]\n
No data memory is given!\n
unblocked due to timeout
bootstage
getBasebandPMUTraceINT
Add Frequency list\n
_TelephonyBasebandHandlePowerDebugInterventionBlock
found coredump ready when polling\n
TelephonyBasebandControllerClearFreqListExt
Baseband property = %d, %llu\n
%s: Could not create run loop source\n
timeout for safe reset\n
timesync
%s: Skipping Force Reset\n
%s: not setting power debug options because they are invalid
%s: could not open service, ret = 0x%08x
%s: modem not in reset, proceeding\n
%s: safe reset %u --done\n
%s: received OCP read ready message\n
%s: Device not supported\n
%s: Reset SPMI with data (0x%llx)\n
%s: \n
%s: no terminal available so power debug intervention not applied
%s: Found wake asserted when polling, wake %u, ret %u\n
%s: Could not add interest notification on service: %#x\n
%s: Skipping Modem Coredump GPIO = %u\n
%s: [%u] interrupt source: %s\n
%s: received GNSS Wake ACK message\n
%s: power debug intervention value (%u) falls outside acceptable range
%s: %s: Invalid queue\n
%s: ret %u, boot stage down %d\n
%s: %s: AppleBaseband IOService is not found. Finding it via matching service\n
%s: Skipping Modem Crash via SPMI\n
%s: Modem Crash via SPMI\n
%s: no service is found
%s: ================== POWER DEBUG UNBLOCKED =================
%s: boot stage down, no need to safe reset\n
%s: failed to get boot stage\n
%s: output: 0x%x\n
%s: invalid GPIO\n
%s: Failed to receive interrupt lists\n
%s: %s: Failed to find %s service, registering for matching notification\n
%s: Failed to read SPMI HEB\n
%s: received wake deasserted message\n
%s: Baseband state = %llu\n
%s: received power debug unblock message
%s: failed to open ABP control driver\n
%s: failed to allocate TelephonyBasebandCoredumpReadyStruct\n
%s: received baseband alive message\n
%s: received powered on message\n
%s: Mux to %u\n
%s: Failed to configure property, ret = 0x%08x\n
%s: Manager state = %llu\n
%s: 0x%x 
%s: failed to get PMUExtOn\n
%s: failed to retrieve ABP boot stage property\n
%s: Timeout for waiting for the driver!
%s: No Op (should skip = %s)\n
%s: Invalid queue
%s: %s: could not close service, ret = 0x%08x\n
%s: received coredump ready message\n
Failed to self-identify with AppleBaseband
%s: Failed to allocate baseband controller.\n
%s: Baseband property = %d, %llu\n
%s: SPMI Raw Read: [%s:0x%x]\n
%s: Invalid config parameter provided\n
%s: Failed to find %s service, registering for matching notification
%s: unblocked due to timeout
%s: boot Stage Down %d\n
%s: Powercycling\n
%s: Baseband property = %llu\n
%s: No data memory is given!\n
%s: failed to allocate TelephonyBasebandWakeStruct\n
%s: received PCI link down message\n
%s: Could not create notification port
%s: received reset detected message\n
%s: received baseband up message\n
%s: received GNSS Trap ACK message\n
%s: Add Frequency list\n
%s: null power debug options arg
Device not supported
%s: Skipping Modem Crash via SPMI with reason\n
%s: VBUS on to %u\n
%s: Reset\n
%s: failed to get coredump ready status\n
%s: Baseband device ID = %llu\n
%s: [%u] timestamp: %s\n
%s: failed to register for resets
%s: found coredump ready when polling\n
%s: AppleBaseband IOService is not found. Finding it via matching service
%s: failed to open ACIPC control driver\n
%s: failed to allocate TelephonyBasebandEventStruct\n
Unable to communicate with AppleBaseband driver
%s: A required input parameter is NULL: ref: %p, data: %p, result: %p\n
%s: invalid baseband controller context\n
%s: No data is given!\n
%s: context cannot be NULL
%s: failed to create baseband controller
%s: failed to get reset\n
%s: cannot do safe reset from this runloop context\n
%s: Finished scanning for %s service\n
%s: Data: 
%s: %s: could not open service, ret = 0x%08x\n
%s: skipping intervention since power debug options indicate it should only be applied once
%s: Skipping Reset\n
%s: failed to safe reset\n
%s: Failed to find %s service\n
%s: %s: no service is found\n
%s: failed to set did-intervene-once flag
%s: ================== POWER DEBUG BLOCKING ==================
%s: somehow neither unblock message was received nor did timeout occur
%s: timeout for coredump ready\n
%s: Skipping Powercycle\n
%s: Modem Crash via SPMI with reason\n
%s: GNSS Wake Trigger!\n
%s: SPMI Reg0Write: [%s:0x%x]\n
%s: power debug options are set but not for this command, proceeding normally...
%s: failed to detect PCIe control driver variant\n
%s: bad argument\n
%s: Clear Frequency list\n
%s: Force Reset\n
%s: %s: Could not create notification port\n
%s: %s: Timeout for waiting for the driver!\n
%s: failed to safe reset via polling\n
%s: Get Modem PMU Trace\n
%s: A required input parameter is NULL: context: %p, thermalData: %p, result: %p\n
%s: Skipping Radio on to %u\n
%s: failed to create runloop timer
%s: unblocked because unblock message received
%s: modem not in reset\n
%s: received baseband down message\n
%s: Budget Policy = %llu\n
%s: Invalid report parameter provided\n
%s: Received a request to read %u bytes of a report of type %u\n
%s: power debug unblock timeout
Failed to create %s instance
%s: Radio on to %u\n
%s: failed to get power debug options
%s: setting did-intervene-once flag
%s: failed to retrieve ACIPC boot stage property\n
%s: timeout for wake\n
%s: received wake-asserted message\n
%s: Enabling Enumeration to %u\n
%s: SPMI Get Events!\n
%s: events (%p) or outputStructCnt (%p) is NULL!\n
%s: %s: Failed to add IOService notification, err: 0x%x\n
%s: %s: context cannot be NULL\n
%s: Failed to self-identify with AppleBaseband\n
%s: safe reset %u, polling\n
%s: failed to get BootStageDown state\n
%s: Invalid notification port
%s: Modem Coredump GPIO = %u\n
%s: Failed to query GPIO %s\n
%s: Received %u configs\n
%s: \tReport type: %u, Report Config: %u\n
%s: Could not create run loop source
%s: failed to create unblocking thread so skipping block power debug intervention
%s: %s: operation '%s' failed: 0x%08x\n
%s: Failed to create %s instance\n
%s: Unable to communicate with AppleBaseband driver\n
%s: Power Debug Unblock\n
%s: Remove Frequency list\n
%s: GNSS Trap Trigger!\n
%s: safe reset %u\n
%s: modem in reset\n
%s: Could not create run loop source\n
%s: checking %s %s %s after %u.%06u seconds\n
%s: Data size (%u) is greater than the max size (%lu)\n
%s: received powering down message\n
%s: received PCIAER message\n
%s: received OCP write message\n
%s: received unknown baseband event %u\n
%s: registered for baseband events\n
%s: received PCI bad request message\n
%s: Failed to add IOService notification, err: 0x%x
%s: Coredump Ready Status = %llu\n
%s: power debug command mask value (%u) falls outside acceptable range
Failed to allocate baseband controller.
%s: SPMI Raw Write: [%s:0x%x]\n
%s: Notification port was not successfully created\n
%s: received billboard is ready message\n
%s: Failed reading data!\n
%s: [%u] bus: %s\n
%s: %s: Invalid notification port\n
%s: timeout for safe reset\n
%s: Debug Action\n
%s: Report Thermal Data\n
%s: %s: Could not create run loop source\n
%s: received PCI Cpl message\n
```
