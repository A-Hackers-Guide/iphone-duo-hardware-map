# `PLSMCAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 21 instance variables, 21 properties, 78 instance methods, 19 class methods

## Instance variables

```
@"PLEntryNotificationOperatorComposition" _sbc;
@"PLEntryNotificationOperatorComposition" _screenStateNotification;
@"PLStateTrackingComposition" _stateTracker;
@"NSDictionary" _lastAccumlatedKeysSample;
@"NSDictionary" _lastAccumlatedKeysSampleCA;
@"NSDictionary" _lastDisplayAccumlatedSample;
@"NSDate" _lastDisplayAccumulatedSampleEndDate;
@"PLEntryNotificationOperatorComposition" _focalAppSwitch;
@"NSDate" _lastFocalSampleDate;
@"PLTimer" _focalSwitchFilterTimer;
@"PLTimer" _thermalAggregationTimer;
@"PLTimer" _thermalMonitorTimer;
@"PLTimer" _thermalLoggingTimer;
@"PLEntry" _lastThermalInstantEntry;
@"NSDictionary" _lastPowerAccumlatedSample;
@"NSDictionary" _lastPowerAccumlatedSampleCA;
@"NSMutableDictionary" _lastAccumValueDict;
@"NSMutableDictionary" _lastAccumCycleCountDict;
^{?=IB^{SMCAccumPlatformInfo}[4{?=I{?=ii(?={?=iBSC}[5c])I}(?=Qqd)(?=Qqd)(?=Qqd)}][4{?=I{?=ii(?={?=iBSC}[5c])I}(?=Qqd)(?=Qqd)(?=Qqd)}]CCBBB{?=[4I][4I]CC}BB} _smcConnection;
@"PLEntryNotificationOperatorComposition" _luxEntryNotification;
@"NSNumber" _currentLux;
```

## Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_sbc) sbc;
@property (T@"PLEntryNotificationOperatorComposition",&,V_screenStateNotification) screenStateNotification;
@property (T@"PLStateTrackingComposition",&,V_stateTracker) stateTracker;
@property (T@"NSDictionary",&,V_lastAccumlatedKeysSample) lastAccumlatedKeysSample;
@property (T@"NSDictionary",&,V_lastAccumlatedKeysSampleCA) lastAccumlatedKeysSampleCA;
@property (T@"NSDictionary",&,V_lastDisplayAccumlatedSample) lastDisplayAccumlatedSample;
@property (T@"NSDate",&,V_lastDisplayAccumulatedSampleEndDate) lastDisplayAccumulatedSampleEndDate;
@property (T@"PLEntryNotificationOperatorComposition",&,V_focalAppSwitch) focalAppSwitch;
@property (T@"NSDate",&,V_lastFocalSampleDate) lastFocalSampleDate;
@property (T@"PLTimer",&,V_focalSwitchFilterTimer) focalSwitchFilterTimer;
@property (T@"PLTimer",&,V_thermalAggregationTimer) thermalAggregationTimer;
@property (T@"PLTimer",&,V_thermalMonitorTimer) thermalMonitorTimer;
@property (T@"PLTimer",&,V_thermalLoggingTimer) thermalLoggingTimer;
@property (T@"PLEntry",&,V_lastThermalInstantEntry) lastThermalInstantEntry;
@property (T@"NSDictionary",&,V_lastPowerAccumlatedSample) lastPowerAccumlatedSample;
@property (T@"NSDictionary",&,V_lastPowerAccumlatedSampleCA) lastPowerAccumlatedSampleCA;
@property (T@"NSMutableDictionary",&,V_lastAccumValueDict) lastAccumValueDict;
@property (T@"NSMutableDictionary",&,V_lastAccumCycleCountDict) lastAccumCycleCountDict;
@property (T^{?=IB^{SMCAccumPlatformInfo}[4{?=I{?=ii(?={?=iBSC}[5c])I}(?=Qqd)(?=Qqd)(?=Qqd)}][4{?=I{?=ii(?={?=iBSC}[5c])I}(?=Qqd)(?=Qqd)(?=Qqd)}]CCBBB{?=[4I][4I]CC}BB},V_smcConnection) smcConnection;
@property (T@"PLEntryNotificationOperatorComposition",&,V_luxEntryNotification) luxEntryNotification;
@property (T@"NSNumber",&,V_currentLux) currentLux;
```

## Class methods

```
+[PLSMCAgent entryEventIntervalDefinitions];
+[PLSMCAgent entryEventPointDefinitions];
+[PLSMCAgent entryEventForwardDefinitions];
+[PLSMCAgent entryEventBackwardDefinitions];
+[PLSMCAgent entryEventNoneDefinitions];
+[PLSMCAgent load];
+[PLSMCAgent entryAggregateDefinitions];
+[PLSMCAgent parsePMUEvents:];
+[PLSMCAgent channelValueDiffKey:];
+[PLSMCAgent channelValueKey:];
+[PLSMCAgent cycleCountKey:];
+[PLSMCAgent entryEventNoneDefinitionColdBoot];
+[PLSMCAgent entryEventNoneDefinitionDRAMVendorKey];
+[PLSMCAgent entryEventNoneDefinitionPowerDeliveryKeys];
+[PLSMCAgent entryEventPointDefinitionMetricMonitorInstantKeys];
+[PLSMCAgent reportPMUEventsToCA:];
+[PLSMCAgent supportsBasicSMC];
+[PLSMCAgent supportsThermalSMC];
+[PLSMCAgent variantKey:];
```

## Instance methods

```
-[PLSMCAgent logPowerDeliveryKeys];
-[PLSMCAgent setSmcConnection:];
-[PLSMCAgent accumSupported];
-[PLSMCAgent init];
-[PLSMCAgent stateTracker];
-[PLSMCAgent dealloc];
-[PLSMCAgent setCurrentLux:];
-[PLSMCAgent initOperatorDependancies];
-[PLSMCAgent setLastFocalSampleDate:];
-[PLSMCAgent sampleAccumulatedKeys:];
-[PLSMCAgent setLastDisplayAccumulatedSampleEndDate:];
-[PLSMCAgent anyVirtualTemperatureAboveThreshold];
-[PLSMCAgent setLuxEntryNotification:];
-[PLSMCAgent luxEntryNotification];
-[PLSMCAgent lastDisplayAccumlatedSample];
-[PLSMCAgent setStateTracker:];
-[PLSMCAgent setScreenStateNotification:];
-[PLSMCAgent focalAppSwitch];
-[PLSMCAgent setLastDisplayAccumlatedSample:];
-[PLSMCAgent screenStateNotification];
-[PLSMCAgent lastFocalSampleDate];
-[PLSMCAgent smcConnection];
-[PLSMCAgent setSbc:];
-[PLSMCAgent currentLux];
-[PLSMCAgent setFocalAppSwitch:];
-[PLSMCAgent log];
-[PLSMCAgent sbc];
-[PLSMCAgent lastDisplayAccumulatedSampleEndDate];
-[PLSMCAgent DRAMVendorKey];
-[PLSMCAgent SMCKeyExists:];
-[PLSMCAgent getChannelInfo:];
-[PLSMCAgent setLastPowerAccumlatedSampleCA:];
-[PLSMCAgent focalSwitchFilterTimer];
-[PLSMCAgent getAccumEntryFromSample:lastSample:withEntryKey:withDate:];
-[PLSMCAgent getPowerEntryFromSample:lastSample:withEntryKey:];
-[PLSMCAgent handleStateChangeForSMCStats];
-[PLSMCAgent lastAccumCycleCountDict];
-[PLSMCAgent lastAccumValueDict];
-[PLSMCAgent lastAccumlatedKeysSample];
-[PLSMCAgent lastAccumlatedKeysSampleCA];
-[PLSMCAgent lastPowerAccumlatedSample];
-[PLSMCAgent lastPowerAccumlatedSampleCA];
-[PLSMCAgent lastThermalInstantEntry];
-[PLSMCAgent logAccumKeysToCA:withLastSample:andDate:];
-[PLSMCAgent logAccumulatedKeysToPowerlog:ToCoreAnalytics:withDate:isWake:];
-[PLSMCAgent logColdBoot];
-[PLSMCAgent logDRAMVendorKey];
-[PLSMCAgent logEventPointMetricMonitorInstantKeys];
-[PLSMCAgent logThermalAggregationKeysToCA];
-[PLSMCAgent logThermalInstantAndAccumlatedKeys];
-[PLSMCAgent metricMonitorInstantKeys];
-[PLSMCAgent parseThermalThresholds:thermalPressure:virtualTemp:thermalLevel:];
-[PLSMCAgent powerAccumulatedKeys];
-[PLSMCAgent powerDeliveryKeys];
-[PLSMCAgent powerDeliveryResetKeys];
-[PLSMCAgent readKey:];
-[PLSMCAgent readKeyViaOSAccum:toOutput:];
-[PLSMCAgent registerThermalTimer];
-[PLSMCAgent resetAccumulatedKeys:];
-[PLSMCAgent sampleKey:forKey:];
-[PLSMCAgent setFocalSwitchFilterTimer:];
-[PLSMCAgent setLastAccumCycleCountDict:];
-[PLSMCAgent setLastAccumValueDict:];
-[PLSMCAgent setLastAccumlatedKeysSample:];
-[PLSMCAgent setLastAccumlatedKeysSampleCA:];
-[PLSMCAgent setLastPowerAccumlatedSample:];
-[PLSMCAgent setLastThermalInstantEntry:];
-[PLSMCAgent setThermalAggregationTimer:];
-[PLSMCAgent setThermalLoggingTimer:];
-[PLSMCAgent setThermalMonitorTimer:];
-[PLSMCAgent stopThermalTimerAndlogFirstLowSample:];
-[PLSMCAgent thermalAggregationKeys];
-[PLSMCAgent thermalAggregationTimer];
-[PLSMCAgent thermalLoggingTimer];
-[PLSMCAgent thermalMonitorTimer];
-[PLSMCAgent virtualTemperatureKeys];
-[PLSMCAgent virtualTemperatureMonitorCallback];
-[PLSMCAgent writeKeyNumeric:withValue:];
```
