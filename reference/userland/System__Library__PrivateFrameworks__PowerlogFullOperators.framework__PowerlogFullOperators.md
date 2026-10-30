# `/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators`

iOS 27.2 dyld shared cache image. Version `3486.52.2.0.0`. **[DSC]**

## Linked libraries (12)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`
- `/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport`
- `/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`
- `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`
- `/System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection`
- `/System/Library/PrivateFrameworks/WirelessDiagnostics.framework/WirelessDiagnostics`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/usr/lib/libAWDSupportFramework.dylib`

## Objective-C: 17 classes, 0 protocols, 475 methods, 109 properties

### Class pages

Every class and protocol, with its methods: [`PLAWDAudio`](../objc/PLAWDAudio_PowerlogFullOperators.md), [`PLAWDAuxMetrics`](../objc/PLAWDAuxMetrics_PowerlogFullOperators.md), [`PLAWDBB`](../objc/PLAWDBB_PowerlogFullOperators.md), [`PLAWDBattery`](../objc/PLAWDBattery_PowerlogFullOperators.md), [`PLAWDCamera`](../objc/PLAWDCamera_PowerlogFullOperators.md), [`PLAWDCpuAP`](../objc/PLAWDCpuAP_PowerlogFullOperators.md), [`PLAWDDisplay`](../objc/PLAWDDisplay_PowerlogFullOperators.md), [`PLAWDMetricsService`](../objc/PLAWDMetricsService_PowerlogFullOperators.md), [`PLAWDNetworkUsage`](../objc/PLAWDNetworkUsage_PowerlogFullOperators.md), [`PLAWDWifiBT`](../objc/PLAWDWifiBT_PowerlogFullOperators.md), [`PLBBPowerToolService`](../objc/PLBBPowerToolService_PowerlogFullOperators.md), [`PLPMUAgent`](../objc/PLPMUAgent_PowerlogFullOperators.md), [`PLPersistentConnectionAgent`](../objc/PLPersistentConnectionAgent_PowerlogFullOperators.md), [`PLScheduledWakeAgent`](../objc/PLScheduledWakeAgent_PowerlogFullOperators.md), [`PLSmartPLService`](../objc/PLSmartPLService_PowerlogFullOperators.md), [`SmartPLMemoryTracking`](../objc/SmartPLMemoryTracking_PowerlogFullOperators.md), [`THIRDPartyApps`](../objc/THIRDPartyApps_PowerlogFullOperators.md)

### Classes

`PLAWDAudio`, `PLAWDAuxMetrics`, `PLAWDBB`, `PLAWDBattery`, `PLAWDCamera`, `PLAWDCpuAP`, `PLAWDDisplay`, `PLAWDMetricsService`, `PLAWDNetworkUsage`, `PLAWDWifiBT`, `PLBBPowerToolService`, `PLPMUAgent`, `PLPersistentConnectionAgent`, `PLScheduledWakeAgent`, `PLSmartPLService`, `SmartPLMemoryTracking`, `THIRDPartyApps`

### Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_audioRailCallback) audioRailCallback;
@property (T@"NSDate",&,V_startTime) startTime;
@property (T@"PLOperator",W,V_operator) operator;
@property (T@"NSMutableSet",&,N,V_runningMetrics) runningMetrics;
@property (T@"PLEntryNotificationOperatorComposition",&,V_bbProtocolRailCallback) bbProtocolRailCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_bbEventCallback) bbEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_accountingGroupEventCallback) accountingGroupEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_iceStatsEventCallback) iceStatsEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_connectedPowerRailCallback) connectedPowerRailCallback;
@property (T@"NSDate",&,V_startTimeAppBB) startTimeAppBB;
@property (T@"NSDate",&,V_startTimeBBLqm) startTimeBBLqm;
@property (TI,V_upBytes) upBytes;
@property (TI,V_downBytes) downBytes;
@property (T@"PLEntryNotificationOperatorComposition",&,V_bbLqmCellularActiveCallback) bbLqmCellularActiveCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_bbLqmCumulativeNetworkCallback) bbLqmCumulativeNetworkCallback;
@property (Ti,V_currQuality) currQuality;
@property (Ti,V_newQuality) newQuality;
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryEventCallback) batteryEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_displayEventCallback) displayEventCallback;
@property (Td,V_prevCapacity) prevCapacity;
@property (Td,V_prevVoltage) prevVoltage;
@property (TB,V_prevDeviceCharging) prevDeviceCharging;
@property (TB,V_prevDisplayON) prevDisplayON;
@property (Tq,V_dispOnOffCnt) dispOnOffCnt;
@property (Td,V_prevDispTimeStamp) prevDispTimeStamp;
@property (Tq,V_batterySubmitCnt) batterySubmitCnt;
@property (T@"PLEntryNotificationOperatorComposition",&,V_cameraEventCallback) cameraEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_cameraEventCallbackTorch) cameraEventCallbackTorch;
@property (TB,V_prevFrontCameraState) prevFrontCameraState;
@property (TB,V_prevBackCameraState) prevBackCameraState;
@property (TB,V_prevTorchCameraState) prevTorchCameraState;
@property (Td,V_frontCameraTimestamp) frontCameraTimestamp;
@property (Td,V_backCameraTimestamp) backCameraTimestamp;
@property (Td,V_torchCameraTimestamp) torchCameraTimestamp;
@property (Tq,V_cameraSubmitCnt) cameraSubmitCnt;
@property (T@"PLEntryNotificationOperatorComposition",&,V_monitorEventCallback) monitorEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_wakeEventCallback) wakeEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_ioreportEnergyEventCallback) ioreportEnergyEventCallback;
@property (T@"NSDate",&,V_sleepStartTime) sleepStartTime;
@property (TB,V_isIoreportEnergy) isIoreportEnergy;
@property (Tq,V_apSubmitCnt) apSubmitCnt;
@property (Tq,V_cpuLoadSubmitCnt) cpuLoadSubmitCnt;
@property (T@"PLEntryNotificationOperatorComposition",&,V_displayEventCallback) displayEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_backlightEventCallback) backlightEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_alsUserPreferencesEventCallback) alsUserPreferencesEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryEventCallback) batteryEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_backlightRailCallback) backlightRailCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_touchEventCallback) touchEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_alsEnabledEventCallback) alsEnabledEventCallback;
@property (TB,V_prevDisplayOn) prevDisplayOn;
@property (Td,V_displayOnTimeStamp) displayOnTimeStamp;
@property (TB,V_prevDeviceCharging) prevDeviceCharging;
@property (TB,V_prevMieOn) prevMieOn;
@property (Td,V_mieOnTimeStamp) mieOnTimeStamp;
@property (Td,V_bklTimeStamp) bklTimeStamp;
@property (Tq,V_prevBklBucketIdx) prevBklBucketIdx;
@property (Td,V_prevBklChgTimeStamp) prevBklChgTimeStamp;
@property (Tq,V_startTouchEntryId) startTouchEntryId;
@property (Td,V_bklPowerRailTimeStamp) bklPowerRailTimeStamp;
@property (Tq,V_dispSubmitCnt) dispSubmitCnt;
@property (Tq,V_touchSubmitCnt) touchSubmitCnt;
@property (TB,V_prevAlsOn) prevAlsOn;
@property (Td,V_prevBklPower) prevBklPower;
@property (T@"AWDServerConnection",&,V_awdServerConn) awdServerConn;
@property (T@"NSMutableSet",&,V_currRunningMetrics) currRunningMetrics;
@property (T@"NSMutableSet",&,V_updateRunningMetrics) updateRunningMetrics;
@property (T@"NSMutableDictionary",&,V_classDictionary) classDictionary;
@property (T@"PLEntryNotificationOperatorComposition",&,V_netEventCallback) netEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_nameConnectionCallback) nameConnectionCallback;
@property (TI,V_netState) netState;
@property (T@"NSTimer",&,V_snapshotTimer) snapshotTimer;
@property (T@"PLEntryNotificationOperatorComposition",&,V_wifiEventCallback) wifiEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_btEventCallback) btEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_btPowerCallback) btPowerCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_wifiRailCallback) wifiRailCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_btRailCallback) btRailCallback;
@property (TB,V_isWiFiStart) isWiFiStart;
@property (TB,V_isWiFiRailStart) isWiFiRailStart;
@property (TB,V_isBTStart) isBTStart;
@property (TB,V_isBTRailStart) isBTRailStart;
@property (Tq,V_wifiSubmitCnt) wifiSubmitCnt;
@property (Tq,V_btSubmitCnt) btSubmitCnt;
@property (TC,V_exclusionMask) exclusionMask;
@property (T@"PLEntryNotificationOperatorComposition",&,V_audioEventCallback) audioEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_displayEventCallback) displayEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_hotspotEventCallback) hotspotEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_msgLiteCallback) msgLiteCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_wcdmaRRCCallback) wcdmaRRCCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_lteRRCCallback) lteRRCCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_telActivityCallback) telActivityCallback;
@property (T@"PLNSNotificationOperatorComposition",&,V_dailyTaskNotification) dailyTaskNotification;
@property (T@"NSMutableArray",&,V_startExclusionPeriods) startExclusionPeriods;
@property (T@"NSMutableArray",&,V_endExclusionPeriods) endExclusionPeriods;
@property (T@"PLTelephonyConnection",W,V_connection) connection;
@property (T@"NSDate",&,V_notToRemoveDate) notToRemoveDate;
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryLevelChanged) batteryLevelChanged;
@property (T@"PLCFNotificationOperatorComposition",R,V_intervalChangedNotification) intervalChangedNotification;
@property (T@"PLCFNotificationOperatorComposition",R,V_preferencesChangedNotification) preferencesChangedNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_canSleepNotification) canSleepNotification;
@property (T@"PLSemaphore",&,V_canSleepSemaphore) canSleepSemaphore;
@property (T@"NSMutableDictionary",&,V_previousScheduleWakeEvents) previousScheduleWakeEvents;
@property (T@"NSMutableDictionary",&,V_smartPLHelpers) smartPLHelpers;
@property (T@"PLSmartPLService",W,V_operator) operator;
@property (T@"PLEntryNotificationOperatorComposition",&,V_memoryTrackingNotification) memoryTrackingNotification;
@property (T@"NSString",&,N,VprocessName) processName;
@property (Ti,N,VwifiIn) wifiIn;
@property (Ti,N,VwifiOut) wifiOut;
@property (Ti,N,VcellIn) cellIn;
@property (Ti,N,VcellOut) cellOut;
```

## Strings (505)

```
PCIEActiveDuration
EventTime
PowerTx
-[PLAWDWifiBT handleBTPowerCallback:]
OOSDuration
AutoScan
StackShotDelay
RRCDisconnected
Resason
AssociatedScanDuration
MemoryTrackingOverhead
SampleDuration
WifiState
kPLWAPNOScanSSIDDuration = %f
-[PLAWDAudio submitDataToAWDServer:withAwdConn:]
Routing changed
causeDuration
E0b
C-
kPLWAAssociatedScanDuration = %f
/Library/Caches/com.apple.xbs/2A2EBAD9-79BD-4405-B0BC-3DF1B2E3AA16/TemporaryDirectory.IpG8Qt/Sources/PerfPowerServices_Operators/Operators/Services/PLAWDMetricsService.m
%@ Battery Event: EnergyConsumed: DurationDispOn =%f
Submit BT stats: submit cnt = %ld
signalStrength
ApValue
Scheduled Restart
%@ : Start Camera collection 
-[PLAWDAuxMetrics submitDataToAWDServer:withAwdConn:]
0`
E0a
/Library/Caches/com.apple.xbs/2A2EBAD9-79BD-4405-B0BC-3DF1B2E3AA16/TemporaryDirectory.IpG8Qt/Sources/PerfPowerServices_Operators/Utilities/AwdLibrary/PLAWDNetworkUsage.m
uAmps
DrainDisplayOn
DurationDispOn
RXDuration
GroupID_%@
BBLteType
-[PLAWDAuxMetrics stopMetricCollection:]
sleep
Brightness
ERROR: PMU: Could not find any current sensors
StackShotCount
PowerRx
-[PLAWDWifiBT submitBtDataToAWDServer:withAwdConn:]
Scheduled Wake or Power On
%@ : Re- Initialize Display/Backlight/Als: Display-On=%d Backlight-Idx=%ld Mie-On=%d Plugged=%d
-[PLAWDBattery startMetricCollection:]
MemoryTrackingEnabled
PLAWD AUX class %@ not implementing stopMetricCollection
UnpluggedDispOnDur
WifiScanDuration
-[PLAWDWifiBT stopMetricCollection:]
PNOScanSSIDDuration
Submit WiFi stats: submit cnt = %ld
%@: initAWDInterface Failed!
dirtyMemoryGuess greater than threshold %f
%@ : Re-Init Battery metrics: prevVoltage=%f prevIsCharging=%d prevCapacity=%f prevDisplayOn=%d
TXPower
-[PLAWDBB handleBBRailCallbackTxGsm:]
invalid pid (%d) for %@ no sample for you!
AwdBT
CacheAge
RailValue
Output changed
BTValue
-[PLAWDMetricsService connectToAWDServer]
\xb1
BatteryMetrics
%@ : Submit Touch stats: submit cnt=%ld metric=%@
DisplayAlsMetrics
%@ : Cpu/Soc/Gpu energy entry= %@
HeadsetHasInput
bbPowerPointCause
`
AutoReady
State
WifiTotalDuration
-[PLAWDCamera handleBackCameraCallback:]
Unsupported metric for battery class %@
%@ : Stop BT collection 
-[PLAWDCamera initCameraStats]
-[PLAWDBB handleBBRailCallbackTxUtran:]
MarginalCoverage
v8@?0
UILock
%@ : BackCameraCallback: currState=%d prevState=%d  
-[PLAWDBB handleBBRailCallbackBBTx:]
DisplayOnCount
Connected
campedRat
Background
kPLWATXDuration = %f
persistentConnection
LTE
%@ : %@
-[PLAWDBattery stopMetricCollection:]
aggregated
%@ : init Camera stats: 
S
%@ : Submit ApData stats: Empty container!!
%@ Battery Event: EnergyConsumed=%f Display On=%d dispOnOffCnt=%lu 
-[PLAWDDisplay initTouchStats]
CurrentCapacity
PowerOther
%@ : Start Wifi collection 
Interface
StationaryFingers
PMDuration
MagicDeltaThreshold
%@ : Finalize Battery table :DurationDispOn =%f
%@ : Stop Wifi collection 
badQuality
-[PLAWDDisplay handleAlsEnabledCallback:]
generating sample for %@(%d)
BTTotalPower
kPLWAPMDuration = %f
kPLWAMPCDuration = %f
MemoryTrackingTriggerThreshold
AppName
poweron
/Library/Caches/com.apple.xbs/2A2EBAD9-79BD-4405-B0BC-3DF1B2E3AA16/TemporaryDirectory.IpG8Qt/Sources/PerfPowerServices_Operators/Utilities/AwdLibrary/PLAWDBattery.m
-[PLAWDCpuAP handleIOReportEnergyCallback:]
WifiTotalPower
-[PLAWDCamera startMetricCollection:]
ArmUtilCount
wcdmaRRCState
%@ : Submit ApData stats: submit cnt=%ld
FRTSDuration
-[PLAWDWifiBT handleBTCallback:]
%@ DisplayEvent: Unplugged Display On duration=%f
%@ : Submit Disp idle duration: dispDur=%f dispIdleDur=%f
E2
/Library/Caches/com.apple.xbs/2A2EBAD9-79BD-4405-B0BC-3DF1B2E3AA16/TemporaryDirectory.IpG8Qt/Sources/PerfPowerServices_Operators/Utilities/AwdLibrary/PLAWDWifiBT.m
CurrentChannel
MPCDuration
%@ : Submit WiFi stats: Empty container!!
awdBBLqmCounter
E1
band_5p04_ghz
SleepPower
%@ : Stop Camera collection 
EnergyCharged
%@ : Initialize Battery metrics: prevVoltage=%f prevIsCharging=%d prevCapacity=%f prevDisplayOn=%d
kPLWAUserScanDuration = %f
NetworkUsageStartSnapshot
-[PLAWDBB handleBBRailCallbackTxCdma:]
__PLEntryErrorString__
MetricsKey
-[PLAWDMetricsService initAWDInterface]_block_invoke
-[PLAWDBB handleBBRailCallbackTxEvdo:]
-[PLAWDCpuAP startMetricCollection:]
-[PLAWDBattery finalizeBatteryTable]
%@ : Wifi first DiffProperty entry
APExclusion
SampleTime
RoamScanDuration
-[PLAWDWifiBT submitWiFiDataToAWDServer:withAwdConn:]
%@ : Submit Camera stats: submit cnt=%ld 
%@ : Submit cpuLoad stats: submit cnt=%ld
WifiTxDuration
Unknown
-[PLAWDBB handleBBLqmCellularActiveCallback:]
%@ :DisplayMetrics: currCharging=%d, prevCharging=%d currDisp=%d dur=%f
PLAWD AUX class %@ not implementing startMetricCollection
No update required, currActive = %@\nAudio writes: %@\n%@\n-------------
Band
results=%@\naggregatedResults=%@
Skip logging event %@
-[PLAWDDisplay handleBatteryCallback:]
-[PLAWDDisplay initDisplayBacklightAlsStats]
-[PLAWDDisplay updateMieMetrics:]
%@ : Start CpuLoad collection
%@ : Ioreport CPU/SoC/GPU energy first entry
HSICActiveDuration
SoC Energy
system
BackCameraDur
%@ : Submit Display stats: submit cnt=%ld 
%@ DisplayEvent: currDisp=%d, prevDisp=%d currCharging=%d
-[PLAWDAudio handleAudioRailCallback:]
/Library/Caches/com.apple.xbs/2A2EBAD9-79BD-4405-B0BC-3DF1B2E3AA16/TemporaryDirectory.IpG8Qt/Sources/PerfPowerServices_Operators/Operators/Services/PLBBPowerToolService.m
/Library/Caches/com.apple.xbs/2A2EBAD9-79BD-4405-B0BC-3DF1B2E3AA16/TemporaryDirectory.IpG8Qt/Sources/PerfPowerServices_Operators/Utilities/AwdLibrary/PLAWDDisplay.m
%@ : Start ApData collection
PrimaryUsagePage
Helper
-[PLAWDCpuAP stopMetricCollection:]
%@ signaling done
%@ :Backlight Event: MicroAmps=%lu Lux=%lu prevBucketIdx=%ld duration=%f newBucketIdx=%ld
ERROR: PMU: Could not find any voltage sensors
-[PLAWDNetworkUsage handleNameConnectionCallback:]
-[PLAWDCamera stopMetricCollection:]
-[PLAWDBB handleIceStatsCallback:]
CurrState
DisplayPower
%@=\"%@\"
ProcessName
PLAWD AUX class %@ not implementing getSharedObj
struckInDCH
%@ : Stop Display/Backlight/Als collection.
entry
%@ : ALS Curve changed by user
ApMetrics
%s - %@
DailyTasks notification!
%@ : BacklightPowerRail: Charger event - update timestamp 
PerfPowerServicesExtended
band_5p08_ghz
com.apple.powerlog
PLAWD AUX class %@ not implementing submitDataToAWDServer
%@ : Start Touch collection
Powerlog: %@ %d of %ld
ScheduledEvent
%@ : ALS state changed by user. alsOn=%d
CPU Energy
%@ : Connection to awd server failed!
DailyTasks
-[PLAWDDisplay startMetricCollection:]
%@ : Finalize Battery table :DurationPartialDispOff =%f
-[PLAWDBB handleBBRailCallbackBBProtocol:]
AudioMetrics
Sensors
CameraMetricsValue
%@ : MieEvent: currMie=%d, prevMie=%d dur =%f
C-vbus
NetworkUsage
-[PLAWDCamera handleFrontCameraCallback:]
simulatedMode
/Library/Caches/com.apple.xbs/2A2EBAD9-79BD-4405-B0BC-3DF1B2E3AA16/TemporaryDirectory.IpG8Qt/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLPMUAgent.m
s
-[PLAWDMetricsService initOperatorDependancies]
BBLqmTx
-[PLAWDAuxMetrics startMetricCollection:]
wake
%@ : Init Touch stats: startTouchEntryId=%lld
%@ : Touch Callback: startTouchEntryId=%lld
On
%@ : Stop ApData collection
-[PLAWDCamera handleTorchCameraCallback:]
Scheduled Shutdown
%@ : Stop Touch collection.
%@ : Finalize Display table
Sample
%@ : AWD config change callback: %@
BBLqmTime
prachCount
time
Block
V-vbat
NetworkUsageEndSnapshot
-[PLAWDBB handleBBRailCallbackLTESleep:]
/Library/Caches/com.apple.xbs/2A2EBAD9-79BD-4405-B0BC-3DF1B2E3AA16/TemporaryDirectory.IpG8Qt/Sources/PerfPowerServices_Operators/Utilities/AwdLibrary/PLAWDAuxMetrics.m
AggregatedARMUtil
MieOnCount
%@ : BacklightPowerRail: Charger event - mWhr=%f 
GPU
%@ : Ioreport CPU/SoC/GPU energy first entry - dropped
-[PLAWDBattery handleBatteryCallback:]
LinkQuality
AudioPower
PluggedDispOnDur
L2
UserScanDuration
CameraMetricsKey
DownBytes
HeadphonesConnected
Type
Ready
Awake
-[PLAWDBattery handleDisplayCallback:]
SampleInterval
%@ : Wifi DiffProperty first entry - dropped - %@
CpuMetrics
-[PLAWDMetricsService init]
Enabled
PerepherialMax
MallocSize
Reason
WifiPcieSuspendDuration
ProcessTime
kPLWARoamScanDuration = %f
%s = %@
Volume
PLBasebandPostProcessing
-[PLAWDDisplay stopMetricCollection:]
BatteryMetricsKey
WifiSleepTime
OtherScanDuration
-[PLAWDDisplay submitDataToAWDServer:withAwdConn:]
ApSource
BTState
WifiOut
TorchCameraDur
BBLteThreshold
poorQuality
UpBytes
PMU: could not create HIDEventSystem
AwdWifi
Disconnected
GPU Energy
/Library/Caches/com.apple.xbs/2A2EBAD9-79BD-4405-B0BC-3DF1B2E3AA16/TemporaryDirectory.IpG8Qt/Sources/PerfPowerServices_Operators/Utilities/AwdLibrary/PLAWDCpuAP.m
Product
restart
L0b
%@ : BT Properties first entry
%@ : AWD Submit data callback: metricType=%d
BBLqmSwitchCounter
CacheInterval
CellDCH
C-ich_avg
WifiHsicDuration
%@ : init
pdp_ip0
Audio
Power On from Off state
!
cause
ArmUtil
lteRRCState
-[PLAWDDisplay handleAlsUserPreferencesCallback:]
Active
C-ich
%@ : Submit BT stats: Empty container!!
MetricsValue
unit
DurationPartialDispOn
no sampler inited for %@(%d)
%@ : TorchCameraCallback: currState=%d prevState=%d  
kPLWATimeDuration = %f
%@ : FrontCameraCallback: currState=%d prevState=%d  
PMU 
SmartTrigger
%@ : Re-init Camera stats: 
AudioVolume
Lux
dbEntry = %@ metric = %@ metricContainer = %@
PowerSleep
%@ : Start BT collection 
*******PLAWDMetricsService*******
DurationPartialDispOff
Error, no sampler inited
com.apple
BBLinkQuality
BBPowerName
ALSEnabled
Backlight
-[PLAWDWifiBT handleWifiCallback:]
BBLqmSwitchBucket
%@ : Stop CpuLoad collection
%@
PCIESuspendDuration
%@ : Initialize Display/Backlight/Als: Display-On=%d Backlight-Idx=%ld Mie-On=%d Als-Enabled=%d Plugged=%d bklPower=%f
Stackshot requested
invalid PID
Logged!
CurrentBandwidth
PNOBSSIDDuration
MemoryTrackingDirtyPercent
SOC
BT Properties Callback - %@
causeTimeStamp
UMTS
Off
DrainPartialDisplayOn
-[PLSmartPLService logEventPointSampleForProcessName:]
-[PLAWDWifiBT startMetricCollection:]
RACHFail
shutdown
NetProcessName
group
PLRail_EventNone_Rail
IsContinuous
RXPower
awdBBLqm
CacheId
scheduledby
V-vbus
%@ : Stop Battery collection 
Voltage
OOS
-[PLScheduledWakeAgent logEventForwardScheduledEvent]
IdlePercentDur
AdapterInfo
IsCharging
%@ :DurationPartialDispOn =%f
PID
/Library/Caches/com.apple.xbs/2A2EBAD9-79BD-4405-B0BC-3DF1B2E3AA16/TemporaryDirectory.IpG8Qt/Sources/PerfPowerServices_Operators/Utilities/AwdLibrary/PLAWDBB.m
bbPowerPointCauseHelper
strength
%@ : Finalize Display table backlightpower=%f dur=%f
band_2p4_ghz
CellOut
-[PLAWDBB handleBBRailCallbackTxLte:]
Scheduled Sleep
VSFOMCal
-[PLAWDDisplay reInitDisplayBacklightAlsStats]
BacklightPower
%@ :DurationPartialDispOff =%f
WifiPcieActiveDuration
-[PLAWDBB handleBBRailCallbackTxCdma2K:]
TXDuration
type - %d; curr - %d
V-
Value
-[PLAWDDisplay finalizeDisplayAlsTable]
V-adc_in7
value
ScanDuration
BundleName
/Library/Caches/com.apple.xbs/2A2EBAD9-79BD-4405-B0BC-3DF1B2E3AA16/TemporaryDirectory.IpG8Qt/Sources/PerfPowerServices_Operators/Utilities/AwdLibrary/PLAWDCamera.m
AudioTime
%@ : BT Properties first entry - dropped
-[PLAWDDisplay handleTouchCallback:]
TimeDuration
-[PLBBPowerToolService initOperatorDependancies]_block_invoke_8
AlsCount
%@ : Start Battery collection 
-[PLAWDBattery submitDataToAWDServer:withAwdConn:]
-[PLAWDBB handleAcountGroupCallback:]
MIE
%ld
From WakeCallback - %@
FaceDetected
BatteryMetricsValue
DrainDisplayOff
BBLqmRx
TcXONotShutting
AlsEnableCnt
WifiRxDuration
%@ Battery Event: EnergyConsumed: DurationPartialDispOff =%f
v12@?0I8
eventtype
%@ Battery Event: EnergyConsumed: DurationPartialDispOn =%f
BBLteValue
MieOnDur
%@ : Submit Battery stats: submit cnt=%ld
No scheduled events
v32@?0@\"NSDictionary\"8@\"NSString\"16@24
%@ : Submit Touch stats: start.entryId=%llu end.entryId=%llu On=%f Off=%f Ready=%f Anticipate=%f Active=%f Others=%f
V-vcc_main
band_5p02_ghz
BT ConnectedStateCallback - %@
%@ AWD-Battery:DisplayEvent: currDisplayOn=%d self.prevDisplayON=%d dispOnOffCnt=%lu
%@ : Finalize Battery table
kPLWARXDuration = %f
CameraMetrics
)
ArmUtilityThreshold
Scheduled Wake
-[PLAWDBattery reInitBatteryStats]
WifiIn
-[PLAWDDisplay handleBacklightCallback:]
DRAM
WifiFrtsDuration
DeviceConnected
Config
-[PLAWDDisplay updateDisplayMetrics:withState:]
-[PLAWDCpuAP submitCpuDataToAWDServer:withAwdConn:]
PrimaryUsage
kPLWAPNOScanBSSIDDuration = %f
kPLWAOtherScanDuration = %f
v24@?0@\"NSArray\"8@\"NSArray\"16
aggregatedResults=%@
-[PLAWDCamera submitDataToAWDServer:withAwdConn:]
+[PLAWDAuxMetrics getSharedObjWithOperator:]
ArmUtilBucket
CPU
OtherPower
Cache
goodQuality
wakepoweron
-[PLAWDCpuAP submitApDataToAWDServer:withAwdConn:]
kPLWAScanDuration = %f
BBConnectedPower
RailIndex
-[PLAWDBattery processEnergyConsumedAndAddEntry:withVoltage:]
-[PLAWDCamera reInitCameraStats]
AudioRouting
lux
L1
-[PLPMUAgent init]
i
Anticipate
-[PLAWDCpuAP handleWakeCallback:]
Block=\"Backlight\"
no name
%@ : Battery Event: energyCharged=%f
CycleCount
FrontCameraDur
-[PLAWDBB handleBBRailCallbackOos:]
/Library/Caches/com.apple.xbs/2A2EBAD9-79BD-4405-B0BC-3DF1B2E3AA16/TemporaryDirectory.IpG8Qt/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLScheduledWakeAgent.m
-[PLAWDBB handleBBRailCallbackBBICE:]
EventCode
%@ : Start Display/Backlight/Als collection
%@ DisplayEvent: Plugged Display On duration=%f
/Library/Caches/com.apple.xbs/2A2EBAD9-79BD-4405-B0BC-3DF1B2E3AA16/TemporaryDirectory.IpG8Qt/Sources/PerfPowerServices_Operators/Operators/Services/PLSmartPLService.m
CellIn
PollingInterval
/Library/Caches/com.apple.xbs/2A2EBAD9-79BD-4405-B0BC-3DF1B2E3AA16/TemporaryDirectory.IpG8Qt/Sources/PerfPowerServices_Operators/Utilities/AwdLibrary/PLAWDAudio.m
L0a
-[PLAWDBattery initBatteryStats]
%@ : Finalize Battery table :DurationPartialDispOn =%f
%@
Interval changed
Preferences changed
Cache = %@
```
