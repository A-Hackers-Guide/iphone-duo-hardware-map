# `/usr/lib/libTelephonyBasebandDynamic.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 185,488 bytes.

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
No Op (should skip = %s)\n
Enabling Enumeration to %u\n
Stopped
Reset SPMI with data (0x%llx)\n
%s: Invalid queue\n
unblocked because unblock message received
received PCI bad request message\n
kTelephonyBasebandPMUTrace_AWAKE_TO_VCXO_PRE
Failed to find %s service\n
%s: TelephonyBaseband
warm-reset
Reset\n
Manager state = %llu\n
get baseband property
Baseband property = %llu\n
kTelephonyBasebandPMUTrace_S2R_TO_SOC_POST
_TelephonyBasebandControllerServiceNotifyCallback
received powering down message\n
kTelephonyBasebandPMUTrace_VCXO_TO_AWAKE_POST
A required input parameter is NULL: ref: %p, data: %p, result: %p\n
unblock command
timesync
clear frequency list
TelephonyBasebandControllerGetBasebandState
safe reset %u, polling\n
received OCP write message\n
kTelephonyBasebandPMUTrace_SOC_TO_S2R_POST
TelephonyBasebandControllerInitContext_block_invoke
TelephonyBasebandControllerRemoveFreqListExt
active
failed to detect PCIe control driver variant\n
received baseband alive message\n
\n
failed to allocate TelephonyBasebandCoredumpReadyStruct\n
modem not in reset\n
SPMI get-events
null power debug options arg
Failed to create %s instance\n
AppleBaseband
sQueue
TelephonyBasebandControllerDebugCommand
CoreDump Ready Interrupt
received power debug unblock message
get peak power budget and thermal budget
TelephonyBasebandControllerEnableModemVBUS
TelephonyBasebandSetPowerDebugOptionsInternal
OCP Rx Ready Interrupt
Received a request to read %u bytes of a report of type %u\n
failed to create runloop timer
received PCI link down message\n
ShouldOnlyInterveneOnce
crash modem via spmi
failed to get BootStageDown state\n
ret %u, boot stage down %d\n
Skipping Powercycle\n
GNSS Trap Trigger!\n
IDC
TelephonyBasebandControllerSetPPMReportConfig
failed to open ACIPC control driver\n
Modem Coredump GPIO = %u\n
Mux to %u\n
Set Baseband State
set baseband property
TelephonyBasebandControllerSPMIRawRead
This command will be blocked until the baseband driver sends an out-of-band notification (e.g. bbutil debug power unblock) or until after %.0f s.
boot stage down, no need to safe reset\n
Found wake asserted when polling, wake %u, ret %u\n
TelephonyBasebandControllerGetPMUTrace
%s: Failed to find %s service, registering for matching notification\n
no-op
modem not in reset, proceeding\n
received OCP read ready message\n
failed to safe reset\n
A required input parameter is NULL: context: %p, thermalData: %p, result: %p\n
TelephonyBasebandControllerSPMIGetEvents
TelephonyBasebandControllerClearFreqListExt
failed to get coredump ready status\n
0x%x 
failed to create unblocking thread so skipping block power debug intervention
failed to allocate TelephonyBasebandWakeStruct\n
received wake deasserted message\n
CommandMask
kTelephonyBasebandPMUTrace_SOC_TO_VCXO_POST_CONN
Debug Action\n
UNDEFINED_PIN
checking %s %s %s after %u.%06u seconds\n
failed to create baseband controller
timeout for wake\n
received coredump ready message\n
true
false
TelephonyBasebandControllerGNSSWakeTrigger
SPMI Ready Signal Interrupt
Received %u configs\n
found coredump ready when polling\n
received unknown baseband event %u\n
Unable to communicate with AppleBaseband driver\n
Intervention
TelephonyBasebandControllerCrashModemWithSPMIWithReason
TelephonyBasebandControllerGetPPMReport
???
Telephony Baseband Command \"%s\" Detected
invalid baseband controller context\n
get pmuext on
Unknown
no terminal available so power debug intervention not applied
_TelephonyBasebandControllerCallMethodGeneric
kTelephonyBasebandPMUTrace_AWAKE_TO_VCXO_POST
Baseband device ID = %llu\n
getBasebandPMUTraceINT
timed out
SPMI reg0write
_TelephonyBasebandHandlePowerDebugInterventionBlock
_TelephonyBasebandPowerDebugBlockingThread
_TelephonyBasebandPowerDebugUnblockCallback
failed to retrieve ABP boot stage property\n
TelephonyBasebandSetPowerDebugOptions
Powercycling\n
usb off
_TelephonyBasebandHandlePowerDebugIntervention
unblocked due to timeout
%s: Could not create notification port\n
Add Frequency list\n
SPMI raw-write
[%u] timestamp: %s\n
failed to get boot stage\n
mux off
TelephonyBasebandGetPowerDebugOptionsInternal
kTelephonyBasebandPMUTrace_VCXO_TO_AWAKE_PRE
TelephonyBasebandControllerPowerDebugUnblock
SPMI Reg0Write: [%s:0x%x]\n
%s: Timeout for waiting for the driver!\n
Modem Crash via SPMI\n
TelephonyBasebandControllerPollGPIO
GNSS trigger wake
power debug options are set but not for this command, proceeding normally...
_TelephonyBasebandHandlePowerDebugInterventionAsk
EnableBBUSB
v24@?0I8I12^v16
reset modem
TelephonyBasebandCreateController
Get PPM Report
%s: Failed to add IOService notification, err: 0x%x\n
kTelephonyBasebandPMUTrace_SOC_TO_VCXO_PRE
Radio on to %u\n
TelephonyBasebandControllerSetCPMSBudgetPolicy
Get budget policy
power-off
_TelephonyBasebandControllerSafeResetModemLegacy
Unable to communicate with AppleBaseband driver
TelephonyBasebandControllerRegisterForEvents
_TelephonyBasebandResetCallback
VBUS on to %u\n
mux on
AppleS5L8930XUSBArbitrator
get coredump ready status
GNSS Wake Trigger!\n
[%u] bus: %s\n
Set PPM Report Config
_TelephonyBasebandControllerFindMatchingService_sync
(power-debug) %s detected\n(power-debug) [continue] c; [skip] s\n(power-debug) 
_TelephonyBasebandPowerDebugTimeoutCallback
received PCI Cpl message\n
Clear Frequency list\n
Remove Frequency list\n
Billboard Tx Ready Interrupt
somehow neither unblock message was received nor did timeout occur
timeout for safe reset\n
TelephonyBasebandControllerIsBootStageDownABP
failed to safe reset via polling\n
Skipping Modem Crash via SPMI with reason\n
Get Modem PMU Trace\n
get manager state
Failed reading data!\n
output: 0x%x\n
================== POWER DEBUG UNBLOCKED =================
Skipping Reset\n
failed to get PMUExtOn\n
_TelephonyBasebandEventCallback
TelephonyBasebandControllerAddFreqListExt
Report Thermal Data\n
skipping intervention since power debug options indicate it should only be applied once
failed to open ABP control driver\n
failed to retrieve ACIPC boot stage property\n
%s: operation '%s' failed: 0x%08x\n
TelephonyBasebandControllerPowerOnModem
TelephonyBasebandControllerSetManagerState
%s: Invalid notification port\n
modem in reset\n
power debug intervention value (%u) falls outside acceptable range
failed to get reset\n
Device not supported\n
SPMI Raw Read: [%s:0x%x]\n
events (%p) or outputStructCnt (%p) is NULL!\n
setting did-intervene-once flag
failed to register for resets
AppleConvergedIPCLedaBBControl
TelephonyBasebandControllerIsBootStageDown
Failed to read SPMI HEB\n
kTelephonyBasebandPMUTrace_S2R_TO_SOC_PRE
coredump off
Failed to query GPIO %s\n
get reset request
_TelephonyBasebandControllerRegisterForService
received reset detected message\n
received baseband up message\n
v8@?0
TelephonyBasebandReportThermalData
coredump on
TelephonyBasebandControllerGNSSTrapTrigger
_TelephonyBasebandControllerClose
power-on
Invalid report parameter provided\n
_TelephonyBasebandControllerAllocate
%s: could not open service, ret = 0x%08x\n
failed to set did-intervene-once flag
received powered on message\n
Finished scanning for %s service\n
not setting power debug options because they are invalid
TelephonyBasebandController
Skipping Force Reset\n
Modem Crash via SPMI with reason\n
TelephonyBasebandControllerSetBasebandState
IOServiceMatched
TelephonyUtilBasebandController
Power Debug Unblock\n
Started
Baseband state = %llu\n
timeout for coredump ready\n
Could not add interest notification on service: %#x\n
TelephonyBasebandControllerInitContext
power off
inactive
TelephonyBasebandControllerGetCoredumpReadyStatus
bad argument\n
safe reset %u --done\n
cannot do safe reset from this runloop context\n
IOGeneralInterest
TelephonyBasebandControllerCrashModemWithSPMI
Failed to configure property, ret = 0x%08x\n
%s: context cannot be NULL\n
Failed to self-identify with AppleBaseband\n
TelephonyBasebandControllerIsBootStageDownACIPC
TelephonyBasebandControllerReportThermalData
GNSS trigger trap
coredump
TelephonyBasebandControllerInitContext_block_invoke_2
%Y-%m-%d %H:%M:%S
_TelephonyBasebandControllerSafeResetModemPolling
Could not create run loop source\n
received wake-asserted message\n
received GNSS Trap ACK message\n
Baseband property = %d, %llu\n
Notification port was not successfully created\n
_TelephonyBasebandControllerInsertInEventQueue
kTelephonyBasebandPMUTrace_Invalid
TelephonyBasebandControllerEnableModemMux
SPMI Raw Write: [%s:0x%x]\n
OCP Tx Ready Interrupt
\tReport type: %u, Report Config: %u\n
%s: no service is found\n
crash-modem-with-spmi
TelephonyBasebandControllerGetBasebandDeviceID
cold-reset
_TelephonyBasebandControllerCallMethod
power debug command mask value (%u) falls outside acceptable range
kTelephonyBasebandPMUTrace_VCXO_TO_SOC_POST
kTelephonyBasebandPMUTrace_SOC_TO_VCXO_POST_IDLE
Coredump Ready Status = %llu\n
TelephonyBasebandControllerSPMIRawWrite
%s: Could not create run loop source\n
safe reset %u\n
received PCIAER message\n
TelephonyBasebandControllerGetBasebandProperty
TelephonyBasebandControllerSetBasebandProperty
Get baseband device ID
SPMI Get Events!\n
_wireless
kTelephonyBasebandPMUTrace_VCXO_TO_SOC_PRE
Skipping Radio on to %u\n
usb on
invalid GPIO\n
TelephonyBasebandControllerGetPPMBudget
AppleConvergedIPCICEBBControl
_TelephonyBasebandControllerInitContext_sync
AppleBasebandPCIControl
DidInterveneOnce
%s: AppleBaseband IOService is not found. Finding it via matching service\n
Reset SPMI
Data size (%u) is greater than the max size (%lu)\n
Failed to receive interrupt lists\n
%s: could not close service, ret = 0x%08x\n
boot Stage Down %d\n
get reset
TimeoutMilliseconds
Set budget policy
received baseband down message\n
received billboard is ready message\n
Remove frequency list
_TelephonyBasebandControllerSafeResetModem
================== POWER DEBUG BLOCKING ==================
TelephonyBasebandControllerResetModem
_TelephonyBasebandPowerDebugOptionsAreValid
done
HEB
[%u] interrupt source: %s\n
Invalid config parameter provided\n
This command will be blocked until the baseband driver sends an out-of-band notification (e.g. bbutil debug power unblock)
kTelephonyBasebandPMUTrace_SOC_TO_S2R_PRE
TelephonyBasebandControllerForceResetModem
TelephonyBasebandControllerSetModemCoredumpGPIO
Force Reset\n
Budget Policy = %llu\n
SPMI raw-read
TelephonyBasebandControllerSPMIReg0Write
power debug unblock timeout
received GNSS Wake ACK message\n
powercycle modem
Skipping Modem Coredump GPIO = %u\n
TelephonyBasebandControllerEnableModemUSBEnumerationWithAP
RESET_REQUEST
No data is given!\n
_TelephonyBasebandControllerOpen_sync
bootstage
com.apple.libTelephonyUtil
TelephonyBasebandControllerNoOp
power on
get baseband state
TelephonyBasebandControllerResetSPMI
Data: 
No data memory is given!\n
failed to allocate TelephonyBasebandEventStruct\n
com.apple.telephony.powerdebugoptions
TelephonyBasebandControllerPowercycleModem
Skipping Modem Crash via SPMI\n
registered for baseband events\n
failed to get power debug options
Failed to allocate baseband controller.\n
%s: power debug options are set but not for this command, proceeding normally...
%s: failed to set did-intervene-once flag
%s: failed to create unblocking thread so skipping block power debug intervention
%s: somehow neither unblock message was received nor did timeout occur
%s: boot stage down, no need to safe reset\n
%s: failed to get boot stage\n
%s: modem not in reset\n
%s: received baseband alive message\n
%s: received PCI Cpl message\n
%s: power debug command mask value (%u) falls outside acceptable range
%s: Failed to find %s service\n
%s: Add Frequency list\n
%s: [%u] interrupt source: %s\n
%s: \tReport type: %u, Report Config: %u\n
%s: %s: Could not create run loop source\n
%s: ================== POWER DEBUG UNBLOCKED =================
%s: safe reset %u --done\n
%s: Enabling Enumeration to %u\n
%s: failed to open ABP control driver\n
%s: modem in reset\n
%s: %s: Could not create notification port\n
%s: AppleBaseband IOService is not found. Finding it via matching service
%s: failed to safe reset via polling\n
%s: registered for baseband events\n
%s: Budget Policy = %llu\n
%s: Received %u configs\n
%s: failed to get power debug options
%s: received wake deasserted message\n
%s: Skipping Modem Crash via SPMI with reason\n
%s: safe reset %u\n
%s: received coredump ready message\n
%s: received powering down message\n
%s: received OCP read ready message\n
%s: received billboard is ready message\n
%s: Skipping Reset\n
%s: A required input parameter is NULL: context: %p, thermalData: %p, result: %p\n
%s: SPMI Get Events!\n
%s: %s: no service is found\n
%s: Failed to configure property, ret = 0x%08x\n
%s: SPMI Raw Read: [%s:0x%x]\n
%s: Received a request to read %u bytes of a report of type %u\n
%s: failed to register for resets
%s: failed to allocate TelephonyBasebandWakeStruct\n
%s: received wake-asserted message\n
%s: received PCI link down message\n
%s: Modem Crash via SPMI with reason\n
%s: Failed reading data!\n
%s: %s: Failed to add IOService notification, err: 0x%x\n
%s: no terminal available so power debug intervention not applied
%s: modem not in reset, proceeding\n
%s: failed to retrieve ACIPC boot stage property\n
%s: output: 0x%x\n
%s: received reset detected message\n
%s: %s: Timeout for waiting for the driver!\n
%s: failed to safe reset\n
%s: found coredump ready when polling\n
%s: Could not create run loop source\n
%s: Could not add interest notification on service: %#x\n
%s: received powered on message\n
%s: received baseband up message\n
%s: null power debug options arg
%s: %s: AppleBaseband IOService is not found. Finding it via matching service\n
%s: Skipping Radio on to %u\n
%s: \n
%s: Could not create run loop source
%s: no service is found
%s: unblocked due to timeout
%s: %s: operation '%s' failed: 0x%08x\n
%s: Debug Action\n
%s: Powercycling\n
Failed to self-identify with AppleBaseband
%s: failed to get BootStageDown state\n
%s: Notification port was not successfully created\n
%s: received GNSS Trap ACK message\n
Failed to create %s instance
%s: %s: could not open service, ret = 0x%08x\n
%s: Failed to self-identify with AppleBaseband\n
Device not supported
%s: invalid baseband controller context\n
%s: checking %s %s %s after %u.%06u seconds\n
%s: SPMI Raw Write: [%s:0x%x]\n
%s: cannot do safe reset from this runloop context\n
%s: bad argument\n
%s: No Op (should skip = %s)\n
%s: Failed to query GPIO %s\n
%s: Reset SPMI with data (0x%llx)\n
%s: 0x%x 
%s: %s: Invalid notification port\n
%s: Failed to read SPMI HEB\n
%s: Failed to create %s instance\n
%s: Modem Crash via SPMI\n
%s: Data size (%u) is greater than the max size (%lu)\n
%s: could not open service, ret = 0x%08x
%s: received unknown baseband event %u\n
%s: Device not supported\n
%s: Coredump Ready Status = %llu\n
%s: No data is given!\n
%s: context cannot be NULL
%s: A required input parameter is NULL: ref: %p, data: %p, result: %p\n
%s: Baseband property = %d, %llu\n
%s: SPMI Reg0Write: [%s:0x%x]\n
%s: Invalid report parameter provided\n
%s: skipping intervention since power debug options indicate it should only be applied once
%s: failed to allocate TelephonyBasebandEventStruct\n
%s: received OCP write message\n
%s: Power Debug Unblock\n
%s: Skipping Modem Crash via SPMI\n
%s: Baseband property = %llu\n
%s: failed to retrieve ABP boot stage property\n
%s: timeout for coredump ready\n
%s: timeout for wake\n
%s: received PCIAER message\n
%s: Baseband device ID = %llu\n
%s: Skipping Force Reset\n
%s: Finished scanning for %s service\n
%s: failed to create baseband controller
%s: Force Reset\n
%s: Radio on to %u\n
%s: Remove Frequency list\n
%s: GNSS Trap Trigger!\n
%s: failed to get reset\n
%s: timeout for safe reset\n
%s: received GNSS Wake ACK message\n
Unable to communicate with AppleBaseband driver
%s: Baseband state = %llu\n
%s: power debug unblock timeout
%s: failed to open ACIPC control driver\n
%s: Unable to communicate with AppleBaseband driver\n
%s: failed to get PMUExtOn\n
%s: Failed to allocate baseband controller.\n
%s: Failed to receive interrupt lists\n
%s: [%u] timestamp: %s\n
%s: unblocked because unblock message received
%s: safe reset %u, polling\n
%s: received baseband down message\n
%s: not setting power debug options because they are invalid
%s: Invalid config parameter provided\n
%s: %s: Failed to find %s service, registering for matching notification\n
%s: Could not create notification port
%s: Modem Coredump GPIO = %u\n
%s: %s: context cannot be NULL\n
%s: Report Thermal Data\n
%s: GNSS Wake Trigger!\n
%s: Failed to find %s service, registering for matching notification
%s: Invalid notification port
%s: ================== POWER DEBUG BLOCKING ==================
%s: received power debug unblock message
%s: failed to detect PCIe control driver variant\n
Failed to allocate baseband controller.
%s: VBUS on to %u\n
%s: No data memory is given!\n
%s: [%u] bus: %s\n
%s: %s: Invalid queue\n
%s: setting did-intervene-once flag
%s: failed to allocate TelephonyBasebandCoredumpReadyStruct\n
%s: Found wake asserted when polling, wake %u, ret %u\n
%s: Get Modem PMU Trace\n
%s: Mux to %u\n
%s: failed to get coredump ready status\n
%s: Data: 
%s: boot Stage Down %d\n
%s: ret %u, boot stage down %d\n
%s: received PCI bad request message\n
%s: Manager state = %llu\n
%s: power debug intervention value (%u) falls outside acceptable range
%s: Timeout for waiting for the driver!
%s: Skipping Modem Coredump GPIO = %u\n
%s: events (%p) or outputStructCnt (%p) is NULL!\n
%s: Invalid queue
%s: Failed to add IOService notification, err: 0x%x
%s: failed to create runloop timer
%s: Reset\n
%s: Skipping Powercycle\n
%s: Clear Frequency list\n
%s: invalid GPIO\n
%s: %s: could not close service, ret = 0x%08x\n
```
