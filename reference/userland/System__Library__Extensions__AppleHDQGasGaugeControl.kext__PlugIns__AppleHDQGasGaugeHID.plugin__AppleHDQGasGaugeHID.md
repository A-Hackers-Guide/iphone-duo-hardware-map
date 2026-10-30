# `/System/Library/Extensions/AppleHDQGasGaugeControl.kext/PlugIns/AppleHDQGasGaugeHID.plugin/AppleHDQGasGaugeHID`

iOS 27.2 dyld shared cache image. Version `240.0.0.0.0`. **[DSC]**

## Linked libraries (4)

- `/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/usr/lib/libSystem.B.dylib`

## Strings (277)

```
gasgauge success after previous failure
determineVACVoltage:: waiting for vbat(%d) < vac(%d)
gasgauge: could not register for power source events
changed updateSampleConfig=%#x
mask real UPOState=%x FCC=%d RemCap=%d new FCC=%d new RemCap=%d
CCA: re-enable DLOG updatesDone=%u, now=%lu
gasgauge success after previous %gs failure
gas gauge: cannot determine the state of SWI line
gas gauge firmware 1.09: disabling critical battery shutdown
%s:%d UpSeconds=%llu (cfd = %u) forcing critical to 0
%s:%d  updatesDone=%d, fullUpdate=%d, bootFullUpdate=%d, forceFullUpdate=%d] 
gathering data log updatesDone=%d num_clients=%d
determinePoSMThreshold, cmp:%d>%u %d>%u %d>%u %d>%u
could not find %s service
%s: %s
gasgauge: updateThread start
gas gauge: debug_polling=%d
%s:%d  updatesDone=%d READING FLAGS
%s:%d  updatesDone=%d criticalValue=%d external_connected=%d UpSeconds=%llu batteryInfo.voltage=%d
determineVACVoltage, vacLevelCount=%d, vac95LevelCount=%d
Added atvAbsMaxVoltageMV=%u to battery dict
gasgauge: could not register for system power notifications
gasgauge: %llu updateThread critical(%d, 0x%x), uscfg=0x%x, dyn=%d cfd=%d cfd-voltage=%d, upos=%x
*** %s:%d updatesDone=%d message.messageType=%#x system_sleep=%d *** 
%s:%d  updatesDone=%d dictionary failed
CCA: re-enable DLOG updatesDone=%d, now=%lu
CCA: cannot disable DLOG (%#x)
gas gauge charge table inconsistent: %d data entries, %d bytes
determinePoSMThreshold, enabled:%d %d %d %d 
%s:%d break failed (%d)
determineVACVoltage:: vacBasedVoltageMV=%d
determinePoSMThreshold, changed:%d %d %d %d 
cnt:%zu ccnt:%zu errs:%@ errCnts:%@
%s:%d cannot find service %s\n
gasgauge: SWI line low reset disabled, ignoring
%s:%d  updatesDone=%d criticalValue=%d external_connected=%d UpSeconds=%llu cfd=%d cfd-voltage=%d batteryInfo.voltage=%d
%s:%d deadline expired at UpSeconds=%llu (cfd = %u)
%s:%d updatesDone=%d UpSeconds=%llu voltage=%d (low)
cannot read battery data count=%d (err=%d)
gas gauge charge table invalid type: %#x
determinePoSMThreshold,minThreshold=%u threshold:%u %u %u %u
gasgauge: could not register for battery events err=%x
cannot enable gauge interrupts (%d)
*** %s:%d updatesDone=%d message.messageType=%#x  (ign) *** 
IORegistryEntrySetCFProperties(0x%x)
Cannot create the lifetime dictionary
%s: cannot read temperature: rc:%u cnt:%zu ccnt:%zu
could not open service: %#x
Critical battery shutdown disabled
cannot disable DLOG (%#x)
%s:%d cannot read upo data
*** %s:%d updatesDone=%d last_update_ignored=%d now=%f deadline=%f update_interval=%f *** 
gasgauge: SWI line low issuing reset
gasgauge: updateThread terminated
%s:%d cannot dump stats and logs (%x)
gas gauge: cannot issue a reset
%s:%d invalid timestamp
gas gauge: SWI line low, issuing reset
gasgauge: could not map data log: %s
CCA: disabled DLOG updatesDone=%d ccaDeadline=%lu
gas gauge charge table bad checksum: checksum %#x checksum byte %#x expecting %#x
%s:%d cannot read data
%s:%d  updatesDone=%d POLLING THE BATTERY
CCA: cannot read DLOG status (%#x)
num_client<0, client error?
determineVACVoltage:: vac95BasedVoltageMV=%d absMaxVoltageMV=%d
pthread_create
gas gauge: critical flag delay %d
*** %s:%d updatesDone=%d same_adaptor=%d adaptor_type=%d external_connected=%d *** 
CCA: GasGauge still calibrating now=%lu
%s:%d cannot create dictionary
dynATV: cannot write to charger startus (%d)
%s:%d cannot disable interrupts (%x)
gas gauge: log counter %d
gasgauge: listening for battery interrupts
could not find hw.model: %s
%s:%d cannot disable gauge interrupts (%d)
disabling DLOG (num_clients=%i)
gas gauge: reset
Battery Diagnostic Data:: %s
gas gauge: userModeEnabled=%d
failure last_update_failed_counter=%d last_success at %g, supressing %d subsequent errors
*** %s:%d updatesDone=%d last_update_ignored=%d now=%f deadline=%f *** 
disabled passedCharge PCFF=%d err=%d
%s:%d  Error Reading Shutdown reason
CCA: wait for deadline now=%lu
%s:%d break failed break_failures=%d (%d)
flags update only
gas gauge reset detected (flags %#x capacity %d/%dmAh voltage %dmV current %dmA)
cannot drain the data log (%d)
%s:%d cannot update thermal state
%s:%d cannot enable interrupts (%x)
%d: retry OpenProtector (%d)
gasgauge: SWI line, cannot determine the state of line
%s:%d  updatesDone=%d PUBLISHING BATTERY data
CCA: usermode cannot disable DLOG (%#x)
ShutDownNominalChargeCapacity
GasGaugeFirmwareVersion
DOD0
AppleRawBatteryFlags
MaxCapacity
GasGauge-updateThread
DebugPolling
FullChargeCapacity
LifetimeData
debug
ChargerTimeout
LocationID
ShutDownVoltage
Raw
NominalChargeCapacity
BatteryShutdownReason
PrimaryUsage
ErrorInjectionCode
battery
ShutDownMaxDischargeCurrent
SOCBasedShutdown
kern.boottime
Temperature
ResScale
MaximumDischargeCurrent
ShutDownPrevAverageCurrent
debugLog
LowAvgCurrentLastRun
CycleCountLastQmax
ErrorCounts
RestricLogCounter
MaximumFCC
ShutDownTimeAbove95
ChargerData
WeightedRa
GaugeFlagRaw
MinimumDeltaVoltage
FlashWriteCount
AppleHDQGasGaugeHID
ShutDownRaTableRaw
ITSimulationCounter
IOPMPowerSource
Voltage
Amperage
log
ChargerAlert
MaximumOverDischargedCapacity
Product
LastCalledTs
readShutdownReasonData
ShutDownTemperature
ShutDownPrevRemainingCapacity
logBatteryDiagnosticData
141
ChargeTable
PrimaryUsagePage
LastErrTs
CurrentCapacity
CriticalFlagDelay
StateOfCharge
IMaxAndSocSmoothTable
TimeRemaining
/Library/Caches/com.apple.xbs/87492427-93EB-4EF0-8E44-97743D15621B/TemporaryDirectory.gbV94b/Sources/AppleHDQGasGauge/AppleHDQGasGauge.c
ChargerWatchdogTimeout
%#x
ShutDownCycleCountLastQmax
ShutDownPassedCharge
AdapterInfo
FullAvailableCapacity
MfgData
ChemID
MinimumRa0-8
/dev/cu.gas-gauge
com.apple.AppleHDQGasGauge
MaximumRa0-8
TotalOperatingTime
CriticalBattery
RaUpdateCounter
BatteryHealthMetric
MaximumPackVoltage
IOPMUBootUPOState
UpdateSampleConfig
NotChargingReason
ShutDownFullChargeCapacity
UserMode
ResetEnabled
AverageCurrent
RaTable
ThermalCoolDown
updateThermalCoolDownState
statsAndLogs
IOPropertyMatch
AppleRawExternalConnected
PresentDOD
ChargingCurrent
MaximumTemperature
ShutDownTimestamp
ITMiscStatus
ServicePluginDebug
built-in
ShutDownPrevVoltage
%s,%5.2f,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d;%d;%d;%d;%d;%d;%d;%d;%d;%d;%d;%d;%d;%d;%d,%d;%d;%d;%d;%d;%d;%d;%d;%d;%d;%d;%d;%d;%d;%d;%d;%d;%d;%d;%d
ChargerStatus
MinimumFCC
MaximumDeltaVoltage
MinimumQmax
 %02x
ShutDownResScale
PassedCharge
PoSMUpperThreshold
OCVTakenFlag
FCFlag
GaugeResetCounter
gas gauge battery
ShutDownPresentDOD
ShutDownAverageCurrent
IOService
IOPMUBootErrorClear
RemainingCapacity
atvAbsMaxVoltageMV
DesignCapacity
TemperatureEventCnt
ShutDownDOD0
com.apple.gasgauge
ForceFullGGUpdateOnBoot
AtCriticalLevel
HighAvgCurrentLastRun
TimeAbove95Perc
TemperatureEventFailCnt
GGHID_GetTemperature
checkreset
ShutDownMaxRa08
updateThread
AppleDynamicATV
MinimumTemperature
RDISCnt
GGHID_log_error
ShutDownUISoc
AbsoluteCapacity
BatteryData
Flags
MaximumQmax
AverageTemperature
TemperatureSamples
PluginName
IOPMUBootBatteryHealthMetric
iMaxAndSocSmoothTable
ShutDownPrevFullChargeCapacity
ShutDownCycleCount
stats
RaTableRaw
ChemicalWeightedRa
TemperatureEventConsFailCnt
LastSuccessTs
ShutDownRemainingCapacity
ShutDownDLog
MinimumPackVoltage
ErrorHistory
ShutDownQstart
timeSinceAwake
CycleCount
PoSMEnabled
UpdateTime
atvBatteryCapacityMA
ManufactureDate
RSS
hw.model
Qstart
PoSMLowerThreshold
MaximumOverChargedCapacity
ShutDownRSS
IOPMUBootUPOCounter
ChargingVoltage
MaximumChargeCurrent
AppleHDQGasGaugeControl
ggctl_open_device
ShutDownPrevNominalChargeCapacity
IOGeneralInterest
Qmax
Serial
ErrorInjection
```
