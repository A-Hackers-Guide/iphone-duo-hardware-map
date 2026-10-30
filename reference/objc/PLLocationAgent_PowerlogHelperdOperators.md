# `PLLocationAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 39 instance variables, 39 properties, 121 instance methods, 27 class methods

## Instance variables

```
B _hadRealGPSSinceSBC;
@"PLCFNotificationOperatorComposition" _techStatusChangedNotification;
@"NSDate" _lastTechStatusNotificationDate;
@"NSNumber" _techStatusLimiterIsActive;
@"PLXPCListenerOperatorComposition" _logLevelNotification;
@"PLXPCListenerOperatorComposition" _statusBarNotification;
@"PLXPCListenerOperatorComposition" _clientStatusNotification;
@"PLXPCListenerOperatorComposition" _gpsSubscriptionListener;
@"PLXPCListenerOperatorComposition" _mapsBusynessStateListener;
@"PLXPCListenerOperatorComposition" _separationAlertListener;
@"PLXPCListenerOperatorComposition" _locationGPSListener;
@"PLEntryNotificationOperatorComposition" _sbcLevelChanged;
@"PLNSNotificationOperatorComposition" _thermalMonitorListener;
@"PLXPCListenerOperatorComposition" _wifiLocationScanRequestersListener;
@"PLXPCListenerOperatorComposition" _odometryListener;
@"PLXPCListenerOperatorComposition" _pdrListener;
@"PLXPCListenerOperatorComposition" _checkInSessionXPCListener;
@"PLXPCListenerOperatorComposition" _predictedContextInferenceListener;
@"PLXPCListenerOperatorComposition" _predictedContextTrainingMetrics;
@"PLXPCListenerOperatorComposition" _miLoScansListener;
@"PLXPCListenerOperatorComposition" _geoFenceTriggerListener;
@"NSMutableDictionary" _localCache;
@"NSMutableDictionary" _clientStatusTypeStrings;
@"NSMutableSet" _processes;
@"NSMutableDictionary" _bundleIDToWeightUsingGPSCache;
@"NSMutableDictionary" _bundleIDToWeightUsingWiFiCache;
@"NSMutableDictionary" _bundleIDToWeightUsingLocationCache;
@"NSMutableDictionary" _activeClients;
@"NSMutableSet" _activeBackgroundLocationClients;
@"NSDate" _lastResyncActiveClientsDate;
d _gps_segment_power;
@"NSDate" _gps_segment_lastWrittenDate;
d _gps_segment_lastWrittenTimestamp;
@"NSDate" _gps_segment_date;
d _gps_segment_timestamp;
@"PLXPCListenerOperatorComposition" _viewObstructedListener;
@"PLXPCListenerOperatorComposition" _suppressionManagerClientListener;
@"PLXPCListenerOperatorComposition" _gnssSessionListener;
@"PLXPCListenerOperatorComposition" _motionPacketListener;
```

## Properties

```
@property (T@"PLCFNotificationOperatorComposition",&,V_techStatusChangedNotification) techStatusChangedNotification;
@property (T@"NSDate",&,V_lastTechStatusNotificationDate) lastTechStatusNotificationDate;
@property (T@"NSNumber",&,V_techStatusLimiterIsActive) techStatusLimiterIsActive;
@property (T@"PLXPCListenerOperatorComposition",&,V_logLevelNotification) logLevelNotification;
@property (T@"PLXPCListenerOperatorComposition",&,V_statusBarNotification) statusBarNotification;
@property (T@"PLXPCListenerOperatorComposition",&,V_clientStatusNotification) clientStatusNotification;
@property (T@"PLXPCListenerOperatorComposition",&,V_gpsSubscriptionListener) gpsSubscriptionListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_mapsBusynessStateListener) mapsBusynessStateListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_separationAlertListener) separationAlertListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_locationGPSListener) locationGPSListener;
@property (T@"PLEntryNotificationOperatorComposition",&,V_sbcLevelChanged) sbcLevelChanged;
@property (TB,V_hadRealGPSSinceSBC) hadRealGPSSinceSBC;
@property (T@"PLNSNotificationOperatorComposition",&,V_thermalMonitorListener) thermalMonitorListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_wifiLocationScanRequestersListener) wifiLocationScanRequestersListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_odometryListener) odometryListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_pdrListener) pdrListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_checkInSessionXPCListener) checkInSessionXPCListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_predictedContextInferenceListener) predictedContextInferenceListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_predictedContextTrainingMetrics) predictedContextTrainingMetrics;
@property (T@"PLXPCListenerOperatorComposition",&,V_miLoScansListener) miLoScansListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_geoFenceTriggerListener) geoFenceTriggerListener;
@property (T@"NSMutableDictionary",&,V_localCache) localCache;
@property (T@"NSMutableDictionary",&,V_clientStatusTypeStrings) clientStatusTypeStrings;
@property (T@"NSMutableSet",&,V_processes) processes;
@property (T@"NSMutableDictionary",&,V_bundleIDToWeightUsingGPSCache) bundleIDToWeightUsingGPSCache;
@property (T@"NSMutableDictionary",&,V_bundleIDToWeightUsingWiFiCache) bundleIDToWeightUsingWiFiCache;
@property (T@"NSMutableDictionary",&,V_bundleIDToWeightUsingLocationCache) bundleIDToWeightUsingLocationCache;
@property (T@"NSMutableDictionary",&,V_activeClients) activeClients;
@property (T@"NSMutableSet",&,V_activeBackgroundLocationClients) activeBackgroundLocationClients;
@property (T@"NSDate",&,V_lastResyncActiveClientsDate) lastResyncActiveClientsDate;
@property (Td,V_gps_segment_power) gps_segment_power;
@property (T@"NSDate",&,V_gps_segment_lastWrittenDate) gps_segment_lastWrittenDate;
@property (Td,V_gps_segment_lastWrittenTimestamp) gps_segment_lastWrittenTimestamp;
@property (T@"NSDate",&,V_gps_segment_date) gps_segment_date;
@property (Td,V_gps_segment_timestamp) gps_segment_timestamp;
@property (T@"PLXPCListenerOperatorComposition",&,V_viewObstructedListener) viewObstructedListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_suppressionManagerClientListener) suppressionManagerClientListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_gnssSessionListener) gnssSessionListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_motionPacketListener) motionPacketListener;
```

## Class methods

```
+[PLLocationAgent entryEventIntervalDefinitions];
+[PLLocationAgent entryEventPointDefinitions];
+[PLLocationAgent entryEventForwardDefinitions];
+[PLLocationAgent entryEventBackwardDefinitions];
+[PLLocationAgent entryEventNoneDefinitions];
+[PLLocationAgent load];
+[PLLocationAgent defaults];
+[PLLocationAgent isEnabled];
+[PLLocationAgent entryAggregateDefinitions];
+[PLLocationAgent entryEventIntervalDefinitionPDR];
+[PLLocationAgent entryEventForwardDefinitionClientStatus];
+[PLLocationAgent entryEventForwardDefinitionGPSSubscription];
+[PLLocationAgent entryEventForwardDefinitionGnssSession];
+[PLLocationAgent entryEventForwardDefinitionLogLevel];
+[PLLocationAgent entryEventForwardDefinitionOdometry];
+[PLLocationAgent entryEventForwardDefinitionStatusBar];
+[PLLocationAgent entryEventForwardDefinitionSuppressionManagerClient];
+[PLLocationAgent entryEventForwardDefinitionTechStatus];
+[PLLocationAgent entryEventForwardDefinitionViewObstructed];
+[PLLocationAgent entryEventIntervalDefinitionMapsBusyness];
+[PLLocationAgent entryEventIntervalDefinitionSeparationAlert];
+[PLLocationAgent entryEventNoneDefinitionClientStatusDebug];
+[PLLocationAgent entryEventPointDefinitionClientStatus];
+[PLLocationAgent entryEventPointDefinitionGeoFenceHandoff];
+[PLLocationAgent entryEventPointDefinitionMiLo];
+[PLLocationAgent entryEventPointDefinitionMotionPacket];
+[PLLocationAgent entryEventPointDefinitionWifiLocationScanRequesters];
```

## Instance methods

```
-[PLLocationAgent processes];
-[PLLocationAgent setLocalCache:];
-[PLLocationAgent init];
-[PLLocationAgent initOperatorDependancies];
-[PLLocationAgent sbcLevelChanged];
-[PLLocationAgent setSbcLevelChanged:];
-[PLLocationAgent setThermalMonitorListener:];
-[PLLocationAgent localCache];
-[PLLocationAgent log];
-[PLLocationAgent setProcesses:];
-[PLLocationAgent thermalMonitorListener];
-[PLLocationAgent activeClients];
-[PLLocationAgent predictedContextTrainingMetrics];
-[PLLocationAgent setGps_segment_lastWrittenDate:];
-[PLLocationAgent setLastResyncActiveClientsDate:];
-[PLLocationAgent activeBackgroundLocationClients];
-[PLLocationAgent handleSBCForGPS];
-[PLLocationAgent humanReadableNameForTechnology:];
-[PLLocationAgent setPdrListener:];
-[PLLocationAgent bundleIDToWeightUsingGPSCache];
-[PLLocationAgent bundleIDToWeightUsingLocationCache];
-[PLLocationAgent bundleIDToWeightUsingWiFiCache];
-[PLLocationAgent checkInSessionXPCListener];
-[PLLocationAgent clientStatusNotification];
-[PLLocationAgent clientStatusTypeStrings];
-[PLLocationAgent closeOpenEntryForClient:withOpenEntry:withTimeStopped:];
-[PLLocationAgent convertCheckInEvent:];
-[PLLocationAgent convertClientEvent:];
-[PLLocationAgent convertOdometryEvent:];
-[PLLocationAgent convertViewObstructedEvent:];
-[PLLocationAgent geoFenceTriggerListener];
-[PLLocationAgent getOpenEntryForClientSettings:withTimeStarted:withClient:withType:withEntryKey:];
-[PLLocationAgent gnssSessionListener];
-[PLLocationAgent gpsSubscriptionListener];
-[PLLocationAgent gps_segment_date];
-[PLLocationAgent gps_segment_lastWrittenDate];
-[PLLocationAgent gps_segment_lastWrittenTimestamp];
-[PLLocationAgent gps_segment_power];
-[PLLocationAgent gps_segment_timestamp];
-[PLLocationAgent hadRealGPSSinceSBC];
-[PLLocationAgent lastEntryWithClient:withType:withBundleID:withEntryKey:];
-[PLLocationAgent lastResyncActiveClientsDate];
-[PLLocationAgent lastTechStatusNotificationDate];
-[PLLocationAgent locationGPSListener];
-[PLLocationAgent logEventForwardCheckInSession:];
-[PLLocationAgent logEventForwardClientStatuswithPayload:];
-[PLLocationAgent logEventForwardGnssSession:];
-[PLLocationAgent logEventForwardOdometry:];
-[PLLocationAgent logEventForwardSuppressionManagerClient:];
-[PLLocationAgent logEventForwardTechStatus];
-[PLLocationAgent logEventForwardTechStatus_withLimiter];
-[PLLocationAgent logEventForwardViewObstructed:];
-[PLLocationAgent logEventFowardGPSSubscription:];
-[PLLocationAgent logEventIntervalMapsBusynessState:];
-[PLLocationAgent logEventIntervalPDR:];
-[PLLocationAgent logEventIntervalSeparationAlert:];
-[PLLocationAgent logEventNoneClientStatus];
-[PLLocationAgent logEventNoneClientStatusDebugWithClients:];
-[PLLocationAgent logEventPointClientStatus];
-[PLLocationAgent logEventPointGeofenceTrigger:];
-[PLLocationAgent logEventPointMiLoScans:];
-[PLLocationAgent logEventPointMotionPacket:];
-[PLLocationAgent logEventPointWifiLocationScanRequesters:];
-[PLLocationAgent logLevelNotification];
-[PLLocationAgent logPredictedContextInferenceEvent:];
-[PLLocationAgent logPredictedContextTrainingEvent:];
-[PLLocationAgent mapsBusynessStateListener];
-[PLLocationAgent miLoScansListener];
-[PLLocationAgent modelGpsSegmentPower:withGpsPower:withTotalDuration:];
-[PLLocationAgent motionPacketListener];
-[PLLocationAgent odometryListener];
-[PLLocationAgent pdrListener];
-[PLLocationAgent predictedContextInferenceListener];
-[PLLocationAgent processesOfInterest:];
-[PLLocationAgent resyncActiveClients];
-[PLLocationAgent separationAlertListener];
-[PLLocationAgent setActiveBackgroundLocationClients:];
-[PLLocationAgent setActiveClients:];
-[PLLocationAgent setBundleIDToWeightUsingGPSCache:];
-[PLLocationAgent setBundleIDToWeightUsingLocationCache:];
-[PLLocationAgent setBundleIDToWeightUsingWiFiCache:];
-[PLLocationAgent setCheckInSessionXPCListener:];
-[PLLocationAgent setClientStatusNotification:];
-[PLLocationAgent setClientStatusTypeStrings:];
-[PLLocationAgent setGeoFenceTriggerListener:];
-[PLLocationAgent setGnssSessionListener:];
-[PLLocationAgent setGpsSubscriptionListener:];
-[PLLocationAgent setGps_segment_date:];
-[PLLocationAgent setGps_segment_lastWrittenTimestamp:];
-[PLLocationAgent setGps_segment_power:];
-[PLLocationAgent setGps_segment_timestamp:];
-[PLLocationAgent setHadRealGPSSinceSBC:];
-[PLLocationAgent setLastTechStatusNotificationDate:];
-[PLLocationAgent setLocationGPSListener:];
-[PLLocationAgent setLogLevelNotification:];
-[PLLocationAgent setMapsBusynessStateListener:];
-[PLLocationAgent setMiLoScansListener:];
-[PLLocationAgent setMotionPacketListener:];
-[PLLocationAgent setOdometryListener:];
-[PLLocationAgent setPredictedContextInferenceListener:];
-[PLLocationAgent setPredictedContextTrainingMetrics:];
-[PLLocationAgent setSeparationAlertListener:];
-[PLLocationAgent setStatusBarNotification:];
-[PLLocationAgent setSuppressionManagerClientListener:];
-[PLLocationAgent setTechStatusChangedNotification:];
-[PLLocationAgent setTechStatusLimiterIsActive:];
-[PLLocationAgent setViewObstructedListener:];
-[PLLocationAgent setWifiLocationScanRequestersListener:];
-[PLLocationAgent shouldRateLimitTechStatus];
-[PLLocationAgent statusBarNotification];
-[PLLocationAgent suppressionManagerClientListener];
-[PLLocationAgent techStatusChangedNotification];
-[PLLocationAgent techStatusLimiterIsActive];
-[PLLocationAgent updateClientsLocationInfo:];
-[PLLocationAgent updateGnssPowerMetric:];
-[PLLocationAgent updateLocalCacheWithClient:withType:withBundleID:withEntry:];
-[PLLocationAgent updateLocationDistributionEvents];
-[PLLocationAgent updateLocationQualificationEvents];
-[PLLocationAgent viewObstructedListener];
-[PLLocationAgent wifiLocationScanRequestersListener];
-[PLLocationAgent writeModeledPower];
```
