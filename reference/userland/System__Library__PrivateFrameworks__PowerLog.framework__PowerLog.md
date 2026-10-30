# `/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`

iOS 27.2 dyld shared cache image. Version `3486.52.2.0.0`. **[DSC]**

## Linked libraries (12)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libsqlite3.dylib`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics`
- `/System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary`
- `/usr/lib/libMobileGestalt.dylib`
- `/System/Library/PrivateFrameworks/BoardServices.framework/BoardServices`
- `/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard`
- `/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices`
- `/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 20 classes, 5 protocols, 410 methods, 118 properties

### Class pages

Every class and protocol, with its methods: [`MetricDelegate`](../objc/MetricDelegate_PowerLog.md), [`NSObject`](../objc/NSObject_PowerLog.protocol.md), [`PLBatteryUIExternalData`](../objc/PLBatteryUIExternalData_PowerLog.md), [`PLCPUEnergySnapshot`](../objc/PLCPUEnergySnapshot_PowerLog.md), [`PLClientLogAggregator`](../objc/PLClientLogAggregator_PowerLog.md), [`PLClientLogger`](../objc/PLClientLogger_PowerLog.md), [`PLCoreDuetEvent`](../objc/PLCoreDuetEvent_PowerLog.md), [`PLCoreDuetEventInterval`](../objc/PLCoreDuetEventInterval_PowerLog.md), [`PLDiscretionaryEnergyMonitor`](../objc/PLDiscretionaryEnergyMonitor_PowerLog.md), [`PLDiscretionaryInterval`](../objc/PLDiscretionaryInterval_PowerLog.md), [`PLDiscretionaryIntervalManager`](../objc/PLDiscretionaryIntervalManager_PowerLog.md), [`PLDuetActivitySchedulerUsageSnapshot`](../objc/PLDuetActivitySchedulerUsageSnapshot_PowerLog.md), [`PLEnergyBucket`](../objc/PLEnergyBucket_PowerLog.md), [`PLHUDCTLClient`](../objc/PLHUDCTLClient_PowerLog.protocol.md), [`PLHUDCTLServer`](../objc/PLHUDCTLServer_PowerLog.protocol.md), [`PLHUDControl`](../objc/PLHUDControl_PowerLog.md), [`PLModelingUtilities`](../objc/PLModelingUtilities_PowerLog.md), [`PLNetworkEnergyModel`](../objc/PLNetworkEnergyModel_PowerLog.md), [`PLNetworkUsageSnapshot`](../objc/PLNetworkUsageSnapshot_PowerLog.md), [`PLQuickEnergySnapshot`](../objc/PLQuickEnergySnapshot_PowerLog.md), [`PLUsageSnapshot`](../objc/PLUsageSnapshot_PowerLog.md), [`PPSClientDonation`](../objc/PPSClientDonation_PowerLog.md), [`PPSClientRegistrationHelper`](../objc/PPSClientRegistrationHelper_PowerLog.md), [`PPSClientRegistrationProtocol`](../objc/PPSClientRegistrationProtocol_PowerLog.protocol.md), [`PPSMetricMonitorDelegate`](../objc/PPSMetricMonitorDelegate_PowerLog.protocol.md)

### Classes

`MetricDelegate`, `PLBatteryUIExternalData`, `PLCPUEnergySnapshot`, `PLClientLogAggregator`, `PLClientLogger`, `PLCoreDuetEvent`, `PLCoreDuetEventInterval`, `PLDiscretionaryEnergyMonitor`, `PLDiscretionaryInterval`, `PLDiscretionaryIntervalManager`, `PLDuetActivitySchedulerUsageSnapshot`, `PLEnergyBucket`, `PLHUDControl`, `PLModelingUtilities`, `PLNetworkEnergyModel`, `PLNetworkUsageSnapshot`, `PLQuickEnergySnapshot`, `PLUsageSnapshot`, `PPSClientDonation`, `PPSClientRegistrationHelper`

### Protocols

`NSObject`, `PLHUDCTLClient`, `PLHUDCTLServer`, `PPSClientRegistrationProtocol`, `PPSMetricMonitorDelegate`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,V_cpuEnergy) cpuEnergy;
@property (TQ,V_cpuEnergyBilledToMe) cpuEnergyBilledToMe;
@property (TQ,V_cpuEnergyBilledToOthers) cpuEnergyBilledToOthers;
@property (T@"NSMutableDictionary",&,V_mockData) mockData;
@property (T@"NSMutableDictionary",R,V_aggregatesCache) aggregatesCache;
@property (TC,V_numAggregates) numAggregates;
@property (TC,V_numAggregations) numAggregations;
@property (T@"NSObject<OS_os_log>",&,V_logHandle) logHandle;
@property (T@"NSObject<OS_dispatch_queue>",&,V_executionQueue) executionQueue;
@property (T@"NSObject<OS_dispatch_source>",&,V_flushTimer) flushTimer;
@property (TB,V_clientDebug) clientDebug;
@property (T@"NSObject<OS_dispatch_queue>",&,V_workQueue) workQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,V_batchFlushQueue) batchFlushQueue;
@property (T@"NSString",&,V_processName) processName;
@property (T@"NSMutableDictionary",&,V_permissionCache) permissionCache;
@property (T@"NSMutableDictionary",&,V_pendingTaskCache) pendingTaskCache;
@property (T@"NSMutableArray",&,V_batchedTaskCache) batchedTaskCache;
@property (T@"NSMutableDictionary",&,V_dynamicCache) dynamicCache;
@property (T@"NSMutableDictionary",&,V_eventFilterSaved) eventFilterSaved;
@property (T@"NSObject<OS_dispatch_queue>",&,V_xpcConnectionQueue) xpcConnectionQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,V_xpcConnectionHelperQueue) xpcConnectionHelperQueue;
@property (T@"NSObject<OS_xpc_object>",&,N,V_xpcConnection) xpcConnection;
@property (T@"NSObject<OS_xpc_object>",&,N,V_xpcConnectionHelper) xpcConnectionHelper;
@property (TB,V_talkToPowerlogHelper) talkToPowerlogHelper;
@property (TB,V_batchedTimerInFlight) batchedTimerInFlight;
@property (TB,V_forceBatching) forceBatching;
@property (TB,V_batchDropMessages) batchDropMessages;
@property (Ti,V_batchMessagesSentCount) batchMessagesSentCount;
@property (T@"NSSet",R,V_batchingClientAllowlist) batchingClientAllowlist;
@property (T@"NSSet",R,V_curatedBatchingList) curatedBatchingList;
@property (T@"NSSet",R,V_batchingKeysAllowlist) batchingKeysAllowlist;
@property (Ti,V_batchedDropMessageCount) batchedDropMessageCount;
@property (TB,V_hasSeenFirstDrop) hasSeenFirstDrop;
@property (Ti,V_hourlyDropCount) hourlyDropCount;
@property (Td,N,V_hourlyWindowStart) hourlyWindowStart;
@property (T@"NSObject<OS_dispatch_queue>",&,V_adaptivePermissionWorkQueue) adaptivePermissionWorkQueue;
@property (T@"NSString",&,V_bundleID) bundleID;
@property (TC,V_updateType) updateType;
@property (T@"NSString",&,V_processName) processName;
@property (T@"NSDictionary",&,V_childBundleIDToWeight) childBundleIDToWeight;
@property (T@"NSArray",&,V_eventIntervals) eventIntervals;
@property (T@"NSDate",&,V_startDate) startDate;
@property (T@"NSDate",&,V_endDate) endDate;
@property (T@"PLDiscretionaryIntervalManager",&,V_intervalManager) intervalManager;
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (Td,N,V_lastReportedTotalEnergy) lastReportedTotalEnergy;
@property (Td,N,V_lastReportedCPUEnergy) lastReportedCPUEnergy;
@property (Td,N,V_lastReportedNetworkEnergy) lastReportedNetworkEnergy;
@property (T@"NSDictionary",&,N,V_lastPowerlogResponse) lastPowerlogResponse;
@property (T@"NSMutableArray",&,N,V_quickEnergySnapshots) quickEnergySnapshots;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_powerlogQueryTimer) powerlogQueryTimer;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_quickEnergyAccumulatorTimer) quickEnergyAccumulatorTimer;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (Td,V_accumulatedCPUEnergy) accumulatedCPUEnergy;
@property (Td,V_accumulatedNetworkEnergy) accumulatedNetworkEnergy;
@property (Td,V_powerlogEnergyDiff) powerlogEnergyDiff;
@property (T@"NSDate",&,V_powerlogTimestampPrevious) powerlogTimestampPrevious;
@property (T@"NSDate",&,V_powerlogTimestampLast) powerlogTimestampLast;
@property (Td,V_powerlogEnergyPrevious) powerlogEnergyPrevious;
@property (Td,V_powerlogEnergyLast) powerlogEnergyLast;
@property (TB,V_isCharging) isCharging;
@property (TB,V_debugMode) debugMode;
@property (T@"NSMutableDictionary",&,V_mockData) mockData;
@property (T@"NSDate",&,V_originalStartDate) originalStartDate;
@property (T@"NSDate",&,V_currentStartDate) currentStartDate;
@property (T@"NSDate",&,V_endDate) endDate;
@property (T@"PLCPUEnergySnapshot",&,V_cpuEnergySnapshot) cpuEnergySnapshot;
@property (T@"PLNetworkUsageSnapshot",&,V_networkEnergySnapshot) networkEnergySnapshot;
@property (Td,V_startCount) startCount;
@property (Td,V_openCount) openCount;
@property (T@"NSMutableDictionary",&,V_identifierToDiscretionaryIntervals) identifierToDiscretionaryIntervals;
@property (T@"NSMutableDictionary",&,V_activityNameToInvolvedIdentifiers) activityNameToInvolvedIdentifiers;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_openIntervalTimer) openIntervalTimer;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_powerlogReportTimer) powerlogReportTimer;
@property (T@"PLDiscretionaryEnergyMonitor",W,N,V_discretionaryEnergyMonitor) discretionaryEnergyMonitor;
@property (TB,N,V_quickEnergyEnabled) quickEnergyEnabled;
@property (T@"NSMutableDictionary",&,V_mockData) mockData;
@property (T@"NSDate",&,V_startDate) startDate;
@property (T@"NSDate",&,V_stopDate) stopDate;
@property (Td,V_numberOfBytesUploadedWiFi) numberOfBytesUploadedWiFi;
@property (Td,V_numberOfBytesDownloadedWiFi) numberOfBytesDownloadedWiFi;
@property (Td,V_numberOfBytesUploadedCell) numberOfBytesUploadedCell;
@property (Td,V_numberOfBytesDownloadedCell) numberOfBytesDownloadedCell;
@property (T@"NSString",&,V_bundleID) bundleID;
@property (Ts,V_level) level;
@property (T@"BSServiceConnection<BSServiceConnectionClient>",&,N,V_connection) connection;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_connectionQueue) connectionQueue;
@property (TB,N,V_isInvalidated) isInvalidated;
@property (TB,N) internalHUDEnabled;
@property (Td,V_powerlevel1Duration) powerlevel1Duration;
@property (Td,V_powerlevel2Duration) powerlevel2Duration;
@property (Td,V_powerlevel3Duration) powerlevel3Duration;
@property (TC,V_linkType) linkType;
@property (Td,V_overallBytes) overallBytes;
@property (Td,V_overallDuration) overallDuration;
@property (TI,V_updateCount) updateCount;
@property (T@"NSString",&,V_taskUUID) taskUUID;
@property (T@"NSArray",&,V_linkCost) linkCost;
@property (T@"NSArray",&,V_linkDuration) linkDuration;
@property (T@"NSArray",&,V_linkLevel1Parameters) linkLevel1Parameters;
@property (T@"NSDate",&,V_timestamp) timestamp;
@property (T@"NSString",&,V_cellType) cellType;
@property (T@"NSString",&,V_quality) quality;
@property (T@"NSString",&,V_wifi) wifi;
@property (T@"NSDate",&,V_timestamp) timestamp;
@property (Td,V_cpuEnergy) cpuEnergy;
@property (Td,V_networkEnergy) networkEnergy;
@property (T@"NSDate",&,V_timestamp) timestamp;
@property (Td,V_cpuUsage) cpuUsage;
@property (T@"NSXPCConnection",&,N,V_connectionToServer) connectionToServer;
```

## Strings (689)

```
OverallDuration
iPod
__dummyKey
PLClientPermissionToken
/Library/BatteryLife/CurrentPowerlog.PLSQL
.EPSQL
com.apple.energybudgetingdebug.lastPowerlogTimestamp
prediction_b2
DeviceHasEmbeddedSIMOnlyBoard
kPLDefault
GenerativeFunctionMetrics::appleDiffusion
%@.ClientID.%@
+[PPSClientDonation isRegisteredSubsystem:category:]
bundle_id
totalAccumulatedEnergy
i
yyyy-MM-dd_HH-mm
i16@?0^{sqlite3_stmt=}8
log_%@_%@.XCSQL
BackgroundProcessing
7d
dynamic
CPUEnergyPrevious
BLMEnergyResponseTimestamp
v32@?0@\"NSNumber\"8Q16^B24
dropped
ClientDonation
powerlog_%@_%@.PLSQL
/Library/BatteryLife/UpgradeLogs/MinorVersion
DrainRate
cell
___BuildMessageSync___
/AppleInternal/Library/PerfPowerServices/HPDConfig.plist
_dynamic
v16@?0@\"BSServiceConnection\"8
PLUsageSnapshot (%@: %f)
LTE
Button::CaptureButtonConfig
5G
involvedIdentifiers
ableID
BLMBatteryCapacity
com.apple.powerlog.sysdiagnoseTrigger.handleXPCEvent
10d
BackgroundProcessing::SystemConditionsPowerManagement
content
8d
com.apple.energybudgetingdebug.generateEnergyReport
time
reason
BackgroundProcessing::SystemConditionsBattery
[
v32@?0@\"NSString\"8@\"NSMutableArray\"16^B24
NetworkEnergyPrevious
com.apple.energybudgetingdebug.lastPowerlogEnergy
LinkType
ReduceBrightnessSuggestion
OptimizeBatteryPromptEligibility
B32@?0@\"NSString\"8@\"NSSet\"16^B24
com.apple.PerfPowerTelemetryClientRegistrationService
bui_backend_iOS
PausedChargingState
endDate
com.apple.energybudgetingdebug.accumulatedNetworkEnergy
eventType
DeviceSupportsAlwaysListening
insightsAndSuggestionsSummaryKey
kPLCuratedBatchingListCache
BackgroundProcessing::TaskInstanceData
PLCLientLoggingConnectionQueue
UpdateCount
IPHONE
/var/mobile/Library/Logs/CrashReporter/
log_%@_%@.EPSQL
ChargingStateIntervals
v16@?0@\"<BSServiceConnectionConfiguring>\"8
BackgroundProcessing::TaskRuntimeAllocation
cpuEnergyBilledToMe
UIKitApplication:
updateType
prediction_c_b
PerfPowerServices
BackgroundProcessing::TaskCheckpoint
bundleID=%@, processName=%@, eventIntervals=%@, childBundleIDToWeight=%@
com.apple.PerfPowerServices
___sFilterByIntervalBufferSync___
BackgroundProcessing::SystemConditionsOther
SignpostServiceMetrics::CollectionSummary
com.apple.powerlog.plxpclogger.xpc
YES
DidReport
.PLSQL
copyPowerlogTime
AutoLockSuggestion
eventIntervals
attributeID
prediction_b1
ENABLE_AUTOLOCK
GenerativeFunctionMetrics::SmartReplySession
lastEventDate
+[PPSClientDonation createIdentifierForSubsystem:category:]
usage_data
v24@?0@\"NSString\"8^B16
BLMEnergyForDuet
BLMUUIDForDuet
ApplicationMetrics::RemoteControlSession
.XCSQL
DROP TABLE IF EXISTS '%@';
BGSQL
ChargingIntervals
BackgroundProcessing::SystemConditionsInUseOrMotion
bui_bgcpu_insight
BatteryQueryForResponderService
DrainSummary
%@_%@
PermissionUnknown
wifiout
GROUP_BY
@\"NSNumber\"24@?0@\"NSNumber\"8@\"NSNumber\"16
com.apple.powerlog.onGoingRestore
Query
INSERT INTO %@ (timestamp, TaskEndTime, Reason) VALUES ('%@', '%@', '%@')
15d
NetworkEnergyCurrent
v32@?0@8Q16^B24
prediction_r2
Energy
AVG
REDUCEBRIGHTNESS
PLBatteryUIUsageSummaryKey
Sysdiagnose
timestamp=%@, cellType=%@, quality=%@, WiFi=%@
PLDuetActivitySchedulerUsageSnapshot (%@, %@, %f, %f, %f, %f, %@)
BLMReportEnergyDuet
Watch
bui_slow_charging
DeviceClassNumber
-[PLClientLogger permissionForClientID:withKey:withType:completion:]_block_invoke
quality
iPad
GSDeviceName
insightSummary
AUTOLOCK_INFO_TEXT
24hr
enum
discretionaryNetworkTasks
com.apple.energybudgetingdebug.accumulatedCPUEnergy
sequenceNumber
value
events
PLClientLogAggregator
optimizeBatteryPromptEligibility
PLClientLoggingAdaptivePermissionWorkQueue
__firstTimestamp
PLXPCConnectionReturnDict
PLXPCBatchedMessageDropCounts
process_name
/var/db/powerlog
PRAGMA cache_size = 50;
PRAGMA incremental_vacuum;
plistCopyDestination
originalStartDate=%@, currentStartDate=%@, endDate=%@, cpuEnergySnapshot=%@, networkEnergySnapshot=%@, openCount=%f, startCount=%f
CPUEnergyLast
com.apple.energybudgetingdebug.queryPowerlog
BLMStopAllDuetEvents
clientID
REDUCEBRIGHTNESS_INFO_TEXT
%@_%@_%@
DASEnergyReport
NetworkEnergyModel
BatteryIntelligence::BatteryHealthDelta
bgsql_dedicated_cache
Post
v16@?0@\"NSObject<OS_xpc_object>\"8
bufferedEventDate
UISOCLevel
com.apple.energybudgetingdebug.lastReportedNetworkEnergy
PLXPCBatchedMessage
AutoBrightnessSuggestion
1hr
Error fetching group containers for %@ : %llu
LastPowerlogResponseMock
com.apple.powerlog.clientLogAggregator
ClientLogging
PLClientLoggingFlushQueue
@\"NSDictionary\"8@?0
/Library/PerfPowerTelemetry/CleanEnergy/CurrentCleanEnergyDB.CESQL
bui_graph_intervals_iOS
requestingService
CPUEnergyCurrent
taskUUID
Text
INSIGHTS_SUGGESTIONS_SUMMARY_RECENT_USAGE_TEXT_%@
v12@?0s8
UnknownRange
com.apple.powerlog.hudcontrol
cpuEnergyBilledToOthers
Q
v16@?0@\"NSError\"8
___BatchCacheSync___
v32@?0@\"NSDictionary\"8Q16^B24
Probability
com.apple.rawPowerlogRetrieval.failCopy
1
C
wifiin
PLBatteryUIDailyCoalescedBreakdown
%d
com.apple.rawPowerlogRetrieval.failOpenDst
mobile
/Library/PerfPowerTelemetry/XcodeOrganizer/CurrentXcodeOrganizerDB.XCSQL
MyEvent
PRAGMA cache_spill = 256;
flushCacheTime
com.apple.powerlogd
com.apple.common
Unnamed_launchdName
com.apple.energybudgetingdebug.quickEnergySnapshots
prediction_c_c
%@.ClientID.%d
CESQL
copyingTime
bui_last_charge_iOS
cellin
DuetRetrySleep
v12@?0B8
ClientRegistration
iPhone
PLBatteryUIQueryFunctionKey
BackgroundCPUInsight
%@_%zu
startDate
DuetDisabled
DeviceClass
com.apple.PLQueryRegistered.%d.%@.end
start
PowerlogEnergyReportedPrevious
PreLTE
s
GenerativeFunctionMetrics::assetLoad
NO
__pl_internal_timeSensitiveSystemDate
pid
%@-shm
XPCMetrics::ClientDroppedEvents
SELECT MAX(timestamp) - MIN(timestamp) from PLBatteryAgent_EventBackward_Battery;
/Library/PerfPowerTelemetry/ExtendedPersistence/CurrentLog.EPSQL
isDynamicEnd
com.apple.energybudgetingdebug.lastReportedCPUEnergy
BatteryUI
%@.ProcessName.%@
com.apple.rawPowerlogRetrieval.failOpenSrc
XPCCacheFlush
com.apple.energybudgetingdebug.chargingStatus
XPCMetrics::OngoingRestore
shouldLog
/Library/BatteryLife/UpgradeLogs/MajorVersion
UsageTimes
timestamp=%@, cpuEnergy=%f, networkEnergy=%f
wifi
Type
cellout
d
AppleTV
IPAD
com.apple.PLQueryRegistered.%d.%@.start
name
com.apple.systemcontainer
cpuEnergy=%llu, cpuEnergyBilledToMe=%llu, cpuEnergyBilledToOthers=%llu
MIN
com.apple.PLQueryRegistered.%d.%@.queryTime
systemgroup.com.apple.powerlog
/Library/BatteryLife/Quarantine/
BackgroundProcessing_DASPoliciesBlockingCriteria_24_5
collectLogsTime
UPGRADE_TITLE
%d_%@
v32@?0@\"PLQuickEnergySnapshot\"8Q16^B24
v8@?0
PLEnergyBucket (%d)
pragma journal_mode=delete
.BGSQL
TimeOut
BBLogsForSysdiagnose
requiresNetwork
NetworkEnergyLast
PPSBatchingEventsPerFlush
cost
log_%@_%@.CESQL
NoteworthyInformation
cpuEnergy
PT
DeviceSupportsAlwaysOnTime
com.apple.batteryui
com.apple.powerlog.clientPermissionState
BackgroundProcessing::
com.apple.powerlogHelperd.XPCService.xpc
com.apple.PerfPowerServices.Ursa
energy
DuetRetryCount
bui_lpm_ipad_ipod
externaldata
event
PPSBatchedMessages
log_%@_%@.BGSQL
size
PLFrameworkEnergyBudgetingWorkQueue
(null)
BatteryBreakdown
RecentUsageInsight
com.apple.internal.PerfPowerHUD.service
ConfigMetrics::BuddyData
overhead
ThermalMonitor
PLCLientLoggingConnectionHelperQueue
com.apple.powerlog.state_changed
(%f, %f)
BLMNotifyDuetEvent
SUM
BackgroundProcessing::TaskMetadata
Button::CaptureButtonAction
discretionaryenergymonitor
v32@?0@\"NSNumber\"8@\"NSArray\"16^B24
bundleID
v32@?0@\"NSString\"8@\"NSMutableSet\"16^B24
com.apple.energybudgetingdebug.discretionaryIntervals
__number
process-name
bufferedEventDictionary
PowerlogTimestampLast
selectedModel
PLClientLoggingWorkQueue
GenerativeFunctionMetrics::tgiExecuteRequest
Count
path
PLSQL
debug_profile_upgrade
AUTOBRIGHTNESS
AUTOBRIGHTNESS_INFO_TEXT
com.apple.powerlog
Process
status
quarantine_path
Failed to copy files to %@
com.apple.powerlog.sysdiagnose
PowerlogTimestampPrevious
BackgroundProcessing::SystemConditionsNetwork
@\"NSMutableDictionary\"8@?0
BatteryDataCollection_BDC_AMA_30_1
%@_%@_%@_%@
q
IOSUISOCDrain
com.apple.energybudgetingdebug.lastReportedTotalEnergy
powerlevel1Duration=%f, powerlevel2Duration=%f, powerlevel3Duration=%f, linkType=%d, overallBytes=%f, overallDuration=%f TotalEnergy=%f, taskID=%@
hasNoteworthyInformation
GenerativeFunctionMetrics::mmExecuteRequest
-[PLClientLogger queryForClientID:withKey:withPayload:]
BackgroundProcessing_DASActivityLifecycle_24_5
/Library/PerfPowerTelemetry/BackgroundProcessing/CurrentBackgroundProcessingDB.BGSQL
Mode
xpc_hourly_drop_tracking
battery_gauge_event
HasBaseband
Unknown_%lu
com.apple.internal.PerfPowerHUD.service.hudctl
BON
BLMEnergyReferenceDate
unknownQuery;
.CESQL
DeviceSetupInsight
BLMLogType
CarrierInstallCapability
MAX
+[PPSClientDonation sendEventWithIdentifier:payload:]
%s::%s
TimeOfCaptureEvent
v16@?0@\"NSDictionary\"8
UISOCDrain
PowerlogEnergyReportedLast
attributeName
prediction_c_a
OverallBytes
BackgroundProcessing::FeatureCheckpoint
v12@?0i8
PLXPCClientDebug
bucket
__lastTimestamp
___CacheSync___
BackgroundProcessing::TaskWorkload
PermissionDenied
EPSQL
suggestionSummary
en_US_POSIX
LastChargeLevel
com.apple.powerlog.energybudgeting
Title
GenerativeFunctionMetrics::Summarization
/Library/BatteryLife/Archives/
end
BasicAngelIPC
CPUCoalitionsMock
Duet to powerlog call is disabled, returning 0
xpcConnectionWithClientID: event handler fired peerPID=%d %@
(PLLogRegisteredEventFilterByInterval) \t currentEventDate = %@\n
PLCopyPowerlog sqlite replace database failed.
coalitionID found in identifierToCoalitionID for identifier=%@, identifierToCoalitionID=%@
identifierToAccountingName=%@
notify_register_check failed %d
returning finalizedEntries=%@
xpcSendMessageWithReply: no xpcMessage
Configure the page cache
permissionForClientID: returnValue=%hd
valid queryResult=%@
cachePermissionForClientID: %d withKey:%@ withType:%@ - Return=%@
end of hour: %@
after adjusting snapshot self=%@
Adjusting identifier=%@ to accountingName=%@ before reporting to powerlog
(PLLogRegisteredEventFilterByInterval) \t\t Log Buffered(%d, %@ at %@) - %@\n
Adding NetworkEnergy=%f for identifier=%@ over %f seconds from startDate=%@ to endDate=%@
Initializing in debug mode with mockData=%@
# of aggregations before flush: %d
xpcSendMessage: xpc connection is not valid
permissionForClientID:%d withKey:%@ withType:%@\nquery=%@\n\nresult=%@\n\npending=%@
(PLLogRegisteredEventFilterByInterval) \t lastEventDate = %@\n
queryForClientID:%d withKey:%@ withPayload:%@ result=%@, message=%@
Vacuum
After refresh coalitionIDToCoalitionNameMapping count=%lu
DEBUG OUTPUT: Querying powerlog for discretionary energy ...: 
Invalid configuration -- value for %@: %@ (expected AggregateType)
Log %@ withContent %@ cannot continue due to nils!
metric collect \n %s \n
Client Framework -- Marked %@ purgeable with urgency: %llu
Processing identifier=%@ and intervals=%@
intervalsPowerlogFormat=%@
%@
DEBUG OUTPUT: Notification name not recognized
Invalid event data -- GROUP_BY on %@: %@ (expected NSString or NSNumber)
xpcConnectionWithClientID: Event handler fired peerPID=%d %@
xpcSendMessageWithReply: no xpcReturnDict
(PLLogRegisteredEventFilterByInterval) \t Set Timer at %@\n
closed interval=%@ for identifier=%@
Generating energy report for das
xpcConnectionWithClientID: connection created!
PLCopyPowerlog: quarantineSrcPath = %@
Successfully generated plist with configuration %@ and result %@
Querying powerlog for discretionary energy
Not querying for powerlog response in debug mode, using lastPowerlogResponse instead
Setting chargingStatus from isCharging=%@ to isCharging=%@
PowerlogFileUtilities: failed to copy minor upgrade logs with error %@
Adding a new open interval for identifier=%@
Connection error: %@
Received (clientID:%@, eventName:%@, eventDictionary:%@) for aggregation with configuration:%@
Dynamic cache reached the limit, flushing cache now
PLCopyPowerlog: Powerlog is short! Looking in quarantine...
Initializing PLDiscretionaryEnergyMonitor...
cumulativePowerlogEnergy=%f
Configure the cache_spill
Setting state=%@ for notificationName=%@
PLCopyPowerlog open database src failed
identifier received is not equal to accountingIdentifier: identifier=%@, accountingIdentifier=%@
quickEnergyDiff=%f = cpuEnergyDiff=%f + networkEnergydiff=%f
notify_set_state failed %d
Invalid configuration -- event data (%lu) and configuration (%lu) should have the same number of keys
cachedPermissionForClientID: Registering for %@ notification
(PLLogRegisteredEventFilterByInterval) \t Timer Fired at %@\n
PLShouldLogEvent: YES
There are 0 intervals for identifier=%@
-> interval: originalStartDate=%@, currentStartDate=%@, endDate=%@, openCount=%f, startCount=%f
quickEnergyBetweenPowerlogReports=%f = cpuEnergyDiff=%f + networkEnergydiff=%f, from timestamp=%@ to timestamp=%@, powerlogEnergyDiff=%f, powerlogEnergyDiff - QuickEnergyDiff = %f
xpcConnectionWithClientID: _xpcConnection=%@
permissionForClientID: logging %@
PowerlogFileUtilities: successfully copied major upgrade logs, srcPath = %@
Insufficient energy diff, not running completion block with totalAccumulatedEnergy=%f, lastReportedTotalAccumulatedEnergy=%f, ENERGY_DIFF=%f
Could not find type for entry %@
Hit the cache limit, dropping last event:  %@
Client Framework --  Failed to mark %@ purgeable - can't open error: %s
PowerlogFileUtilities: failed to copy minor upgrade logs, srcPath = %@
Cannot update mock data unless in debug mode
State:%@ ***\npermissionCache=%@\n\npendingTaskCache=%@\n\nbatchedTaskCachePPS=%@\n
permissionForClientID: %hd withKey:%@ withType:%@ returnValue=%hd
Quarantine copying failed
After coalescing intervals, intervals=%@
Testing high volume start/stops for activityName=%@, withInfo=%@ for %f iterations
Client Framework -- Failed to mark %@ purgeable - flags 0x%llx returned %d (%s)
Updating to mockData=%@
queryForClientID: no query key! %@
Performed powerlog reset as requested
\"bui_backend_iOS\" feature flag is enabled. Running query via Responder Service...
Failed to generate a new BatteryUI plist
Drop %@
coalitionID not found after refresh, for identifer=%@
(%s) Invalid inputs: %s / %s
Getting cpu energy from coalitions snapshot for  coalitionID=%llu
No open intervals for identifier=%@
Unable to generate energy report -- lastPowerlogResponse=%@
Invalid event data -- value for %@: %@ (according to configuration, %@ expects NSNumber)
xpcSendMessageWithReply: no xpcResponse
DiscretionaryEnergyMonitor : bundleid %@ and launchd name %@
reporting quick energy for interval=%@, identifier=%@, adjustSnapshotToNow=%@
XPC Send Message - Batching enabled xpcSendMessageWithRateLimitingforClient: %d withKey:%@
ClientDroppedEvents: sending payload:  %@
queryForClientID: %s/%d: clientID=%d, payload=%@
Starting powerlog copy to Crash Reporter
\nInterruption ended!
Starting copy of dB: %@ to dst: %@\n
UUIDForDuet: %@
Unknown Permission %d - for client id:%d withKey:%@ withPayload:%@
Setting up debug listeners
sendBatchToPPS: dynamicCache not plist-serializable, falling back to live reference
PLShouldLogRegisteredEvent: %d, ClientID: %d
Finished initializing PLDiscretionaryEnergyMonitor...
accumulating quick energy
is Eligible for Optimize Battery Prompt: %d
xpcConnectionWithClientID: client (%d) is reusing connection to powerlogHelperd!
xpcSendMessageWithReply: xpcMessage=%@, xpcResponse=%@, xpcConnection=%@
xpcSendMessageWithReply: setting clientDebug to %@
Caching %d withKey:%@ withPayload:%@ ...
totalAccumulatedEnergy=%f is composed of cumulativePowerlogEnergy=%f up to timestamp=%@ + quickEnergyDiff=%f since this timestamp.
New Powerlog Accounting Energy: previousPowerlogEnergySum=%f, lastPowerlogEnergySum=%f, powerlogEnergyDiff=%f from previousResponseTimestamp=%@ to lastResponseTimestamp=%@
generating energy report after querying powerlog
%@ result: %@
Reading mock coalitions data for identifier=%@, mockDataForIdentifier=%@
Initializing open interval timer
identifier=%@, intervalCount=%lu
Sending xpc message for client id: %d withKey:%@ withPayload:%@ dispatching...
BGSQL DROP Success: %d Execution Time: %f
PowerlogFileUtilities: successfully copied minor upgrade logs, srcPath = %@
EPSQL DROP Success: %d Execution Time: %f
addToPendingTaskCacheForType: Current cached payloads = %@
xpcConnectionWithClientID error: %@
xpcSendMessage: sending message %@
Failed to open database connection at path: %@
coalitionID not found, refreshing coalition mapping and searching again for identifier=%@
Sending XPC to powerlog to log intervals
Creating quickEnergyAccumulator timer
State:%@ ***\npermissionCache=%@\n\npendingTaskCache=%@\n\nbatchedTaskCache=%@\n
addToBatchedTaskCacheForType: payload not plist-serializable, falling back to shallow copy for clientID=%d key=%@
(PLLogRegisteredEventFilterByInterval) Buffer(%d, %@ at %@) - %@\n
after handleStartEvent, identifierToDiscretionaryIntervals=%@
xpcConnectionWithClientID: XPC Connection back? %@
HUD: No server available for querying state
adjusting networkEnergySnapshot=%@ to now
timeSinceIntervalStart=%f, now=%@, intervalStartDate=%@
xpcConnectionWithClientID: Client (%d) is creating connection to powerlogHelperd, using queue %@!
PowerlogFileUtilities: failed to copy major upgrade logs, srcPath = %@
handling start event for activityName=%@ with info=%@
Starting report intervals to powerlog, identifierToDiscretionaryIntervals=
handlingPowerlogReportTimer
Initializing Powerlog report timer
using key=%@
calculating end of hour from %@
(%s) Permission denied: %s / %s
(PLLogRegisteredEventFilterByInterval)  Log(%d, %@ at %@) - %@\n
HUD: No server available for setting enabled:%d
HUD: service encountered error when setting enabled:%d %@
Attempting to check open interval duration for a closed interval
quick energy accumulation disabled while charging
EnergyResponseTimestamp: %@
Connection was interrupted.
cachedPermissionForClientID: notification %@ registration failed : %d
Date: %@ -> %@ -> %ld
XPC Send Message - not batched xpcSendMessageWithRateLimitingforClient: %d withKey:%@ message %@
Not sending XPC to powerlog to log intervals while in debug mode
Adding CPUEnergy=%f for identifier=%@ over %f seconds from startDate=%@ to endDate=%@
xpcConnectionWithClientID error : %@
xpcSendMessageWithReply: waiting for replay to message %@, xpcConnection=%@
permissionForClientID: query!
(PLLogRegisteredEventFilterByInterval) \t interval = %f, minInterval = %f\n
adjusting snapshot self=%@ to now
(PLLogRegisteredEventFilterByInterval) Drop invalid(%d, %@ at %@) - %@\n
Failed to set cache_size %s
Failed to vacuum db with error %s
coalitionID not found, unable to snapshot identifer=%@
Logging identifierToDiscretionaryIntervals, count=%lu
Logging energy report to powerlog ... logEvent=%@
computing network energy diff between self=%@ and otherSnapshot=%@
Attempted to close interval with openCount=%f
activityName=%@, involvedIdentifiers=%@
energyDiff=%f not sufficient to enqueue new quick energy snapshot
incrementing cpu energy by energy=%f
powerlogStateChanged: Powerlog state changed
Unable to remove directory during powerlog reset, err: %@
Failed to drop %@ data with error %s
Finished initializing DiscretionaryIntervalManager
Logging activityNameToInvolvedIdentifiers, count=%lu
xpcSendMessageWithReply: no response
PLSysdiagnoseTimeSensitivePhase returned
Copying %@ data failed, time taken = %d
Reporting stopEvent activityName=%@, info=%@ from energyMonitor
queryForClientID:%d withKey:%@ withPayload%@ - keyPermission=%d, retry=%d
Error copying for srcDir %@ : %@
PowerlogFileUtilities: failed to copy major upgrade logs with error %@
Reporting startEvent activityName=%@, info=%@ from energyMonitor
Powerlog response: %@
DEBUG OUTPUT: Generating energyReport ...: 
invalid queryResult
-- Updated aggregated event #%@ (key: %@)
computing energy diff between self=%@ and otherSnapshot=%@
Refreshing coalition ID mapping
No valid response from powerlog, response=%@
xpcSendMessageWithReply: response=%@
%@ semaphore timeout %lu
PLCrashMoverCopyPowerlog done copying powerlog : %@
Initializing DiscretionaryIntervalManager, with mockData=%@
There is already an open interval for identifier=%@, incrementing openCount
after handleStopEvent, identifierToDiscretionaryIntervals=%@
powerlogEnergyReportTimestamp=%@
totalAccumulatedEnergy < lastReportedEnergy
shouldLogNowForClientID: (PLLogRegisteredEventFilterByInterval) Check(%d, %@ at %@) - %@\n
xpcSendMessageWithRateLimitingforClient: client id:%d withKey:%@ withPayload:%@ sent!
xpcSendMessageWithRateLimitingforClient: %d withKey:%@ withPayload:%@ sent!
after enqueuing first quickEnergy snapshot, quickEnergySnapshots=%@
Spinning up XPC service
permissionCache: %@
(%s) Invalid inputs: payload=%@
PLCopyPowerlog open database dst failed
PLCrashMoverCopyPowerlog starts cache flush
System hour bucket: %@ -> %@
HUD: Invalidated/Interrupted connection %@
searching cache for coalitionID for identifier=%@
Firing open interval timer when switching charging state
Invalid configuration -- expected at least one numeric AggregateType key
HUD: service encountered error when querying state %@
Coalescing intervals=%@
handlingOpenIntervalTimer
Before removing staleSnapshots, quickEnergySnapshots=%@
incrementing network energy by energy=%f
DEBUG OUTPUT: Discretionary Intervals: 
Notification %s registration failed : %d
(PLLogRegisteredEventFilterByInterval) \t\t No Buffered Log(%d, %@ at %@)\n
\nInterrupted; attempting to resume...
Received stop event for activity with no involvedIdentifiers known for activityName=%@, activityNameToInvolvedIdentifiers=%@
config: %@, queryResult: %@
Could not find title and text for entry %@
Notification %@ registration failed : %d
setCachePermission:%d ForClientID:%d withKey:%@ withType:%@
(%s) Failed to malloc identifier
PLCopyPowerlog file copy status success
Archive copying failed
activityNameToInvolvedIdentifiers=%@, infoWithIdentifiers=%@
currentSnapshot=%@, firstRelevantSnapshot=%@
PLShouldLogEvent: NO
Interval open for %f seconds, potential unclosed interval=%@ for identifier=%@
handling stop event for activityName=%@ with info=%@
reporting energy for openInterval=%@
lastPowerlogResponse=%@
quickEnergySnapshots=%@
Flushing aggregated data to PowerLog (clientID:%d)
Dynamic cache reached the limit, unable to flush, dropping last event %@
xpcConnectionWithClientID: creating connection to powerlog!
Reporting %lu events to powerlog: 
xpcConnectionWithClientID: Reusing connection to powerlog!
xpcSendMessage: no xpcMessage
xpcSendMessageWithReply: xpc connection is not valid
xpcSendMessageWithReply: xpcReturnDict=%@
permissionForClientID: %s/%d: message = %@, result=%@
queryForClientID: Override permission for clientID:%d
Invalid entry in databases at index %zu
After persisting open intervals, identifierToDiscretionaryIntervals=%@
DEBUG OUTPUT: Quick energy snapshots: 
xpcConnectionWithClientID: connection created
xpcSendMessageWithReply: xpcResponse=%@
Running completion block with totalAccumulatedEnergy=%f, lastReportedTotalAccumulatedEnergy=%f, ENERGY_DIFF=%f
Client Permission check completed. Invalidating XPC Connection.
buildMessageForClientID: %d message:%@
\nError: %s\n
PLCopyPowerlog: main log duration = %f
Failed to perform powerlog reset because there is no container URL
BGSQL TimeOfCaptureEvent epoch: %f reason: %d
BGSQL TimeOfCaptureEvent open failed for reason %d
after adjusting networkEnergySnapshot=%@
error: firstRelevantSnapshot=%@, currentSnapshot=%@
Invalid event data -- %@ key (expected NSString)
xpcConnectionWithClientID: Received XPC_ERROR_CONNECTION_INVALID
Failed to copy files to %@
Creating quick energy snapshot, cpuEnergyTotal=%f, networkEnergyTotal=%f, totalEnergy=%f
Failed to set cache_spill %s
Initializing discretionary interval without snapshotting for identifier=%@, snapshottingEnabled=%d
PLCopyPowerlog output: %@
Performed successful query and copy with configuration %@ and result %@
hourNum: %lu
After removing stale snapshots, quickEnergySnapshots=%@
powerlogStateChanged: Unregistering for %@ notification
PLCopyPowerlog file chown success = %d
BGSQL TimeOfCaptureEvent insert failed for reason %d
timedifferential=%f
firstStaleSnapshot=%@, firstRelevantSnapshot=%@
QuickEnergyDiff=%f is greater than powerlogEnergyDiff=%f
-- Log aggregated event #%@ (eventName:%@, eventDictionary:%@)
```
