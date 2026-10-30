# `PLSMCMetricsAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 25 instance variables, 25 properties, 84 instance methods, 6 class methods

## Instance variables

```
I _loggingCounter;
I _loggingThreshold;
I _powerDeliveryCounter;
@"NSNumber" _currentLux;
@"PLTimer" _monitorTimer;
d _cycleCountInterval;
@"NSDate" _lastFocalSampleDate;
^{?=IB^{SMCAccumPlatformInfo}[4{?=I{?=ii(?={?=iBSC}[5c])I}(?=Qqd)(?=Qqd)(?=Qqd)}][4{?=I{?=ii(?={?=iBSC}[5c])I}(?=Qqd)(?=Qqd)(?=Qqd)}]CCBBB{?=[4I][4I]CC}BB} _smcConnection;
d _monitorCadence;
@"NSSet" _availableKeys;
@"NSDictionary" _lastAccumlatedSample;
@"NSDictionary" _lastAccumlatedSampleCA;
@"PLStateTrackingComposition" _stateTracker;
@"NSArray" _loggedInstantKeysArray;
@"PLEntryNotificationOperatorComposition" _sbc;
@"NSDate" _lastDisplayAccumulatedSampleEndDate;
@"NSDictionary" _lastDisplayAccumlatedSample;
@"NSMutableArray" _accumGaugeArray;
@"NSMutableArray" _instantGaugeArray;
@"NSArray" _loggedAccumulatedKeysArray;
@"NSArray" _loggedPowerDeliveryKeysArray;
@"PLEntryNotificationOperatorComposition" _focalAppSwitch;
@"PLNSNotificationOperatorComposition" _dailyTaskNotification;
@"PLEntryNotificationOperatorComposition" _luxEntryNotification;
@"PLEntryNotificationOperatorComposition" _screenStateNotification;
```

## Properties

```
@property (T@"NSNumber",&,V_currentLux) currentLux;
@property (T@"PLTimer",&,V_monitorTimer) monitorTimer;
@property (TI,V_loggingCounter) loggingCounter;
@property (Td,V_cycleCountInterval) cycleCountInterval;
@property (TI,V_loggingThreshold) loggingThreshold;
@property (T@"NSDate",&,V_lastFocalSampleDate) lastFocalSampleDate;
@property (T^{?=IB^{SMCAccumPlatformInfo}[4{?=I{?=ii(?={?=iBSC}[5c])I}(?=Qqd)(?=Qqd)(?=Qqd)}][4{?=I{?=ii(?={?=iBSC}[5c])I}(?=Qqd)(?=Qqd)(?=Qqd)}]CCBBB{?=[4I][4I]CC}BB},V_smcConnection) smcConnection;
@property (TI,V_powerDeliveryCounter) powerDeliveryCounter;
@property (Td,V_monitorCadence) monitorCadence;
@property (T@"NSSet",&,V_availableKeys) availableKeys;
@property (T@"NSDictionary",&,V_lastAccumlatedSample) lastAccumlatedSample;
@property (T@"NSDictionary",&,V_lastAccumlatedSampleCA) lastAccumlatedSampleCA;
@property (T@"PLStateTrackingComposition",&,V_stateTracker) stateTracker;
@property (T@"NSArray",&,V_loggedInstantKeysArray) loggedInstantKeysArray;
@property (T@"PLEntryNotificationOperatorComposition",&,V_sbc) sbc;
@property (T@"NSDate",&,V_lastDisplayAccumulatedSampleEndDate) lastDisplayAccumulatedSampleEndDate;
@property (T@"NSDictionary",&,V_lastDisplayAccumlatedSample) lastDisplayAccumlatedSample;
@property (T@"NSMutableArray",&,V_accumGaugeArray) accumGaugeArray;
@property (T@"NSMutableArray",&,V_instantGaugeArray) instantGaugeArray;
@property (T@"NSArray",&,V_loggedAccumulatedKeysArray) loggedAccumulatedKeysArray;
@property (T@"NSArray",&,V_loggedPowerDeliveryKeysArray) loggedPowerDeliveryKeysArray;
@property (T@"PLEntryNotificationOperatorComposition",&,V_focalAppSwitch) focalAppSwitch;
@property (T@"PLNSNotificationOperatorComposition",&,V_dailyTaskNotification) dailyTaskNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_luxEntryNotification) luxEntryNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_screenStateNotification) screenStateNotification;
```

## Class methods

```
+[PLSMCMetricsAgent load];
+[PLSMCMetricsAgent isEnabled];
+[PLSMCMetricsAgent parsePMUEvents:];
+[PLSMCMetricsAgent reportPMUEventsToCA:];
+[PLSMCMetricsAgent shouldModelDisplayPowerFromSMC];
+[PLSMCMetricsAgent supportsSMC];
```

## Instance methods

```
-[PLSMCMetricsAgent logPowerDeliveryKeys];
-[PLSMCMetricsAgent setLoggedPowerDeliveryKeysArray:];
-[PLSMCMetricsAgent handleSleepWakeStateChange];
-[PLSMCMetricsAgent setLoggedAccumulatedKeysArray:];
-[PLSMCMetricsAgent logEventPointInstantKeys];
-[PLSMCMetricsAgent loggedAccumulatedKeysArray];
-[PLSMCMetricsAgent setSmcConnection:];
-[PLSMCMetricsAgent thermalMonitorCallback];
-[PLSMCMetricsAgent setMonitorCadence:];
-[PLSMCMetricsAgent getAllowedInstantKeys];
-[PLSMCMetricsAgent accumSupported];
-[PLSMCMetricsAgent isKeyOSAccumSupported:];
-[PLSMCMetricsAgent setLoggingCounter:];
-[PLSMCMetricsAgent init];
-[PLSMCMetricsAgent initOSMetrics];
-[PLSMCMetricsAgent stateTracker];
-[PLSMCMetricsAgent availableKeys];
-[PLSMCMetricsAgent setAvailableKeys:];
-[PLSMCMetricsAgent setMonitorTimer:];
-[PLSMCMetricsAgent dealloc];
-[PLSMCMetricsAgent setCurrentLux:];
-[PLSMCMetricsAgent initOperatorDependancies];
-[PLSMCMetricsAgent isThermalPressureFanNoiseAboveThreshold];
-[PLSMCMetricsAgent readSMCKey:];
-[PLSMCMetricsAgent setAccumGaugeArray:];
-[PLSMCMetricsAgent setLastFocalSampleDate:];
-[PLSMCMetricsAgent sampleAccumulatedKeys:];
-[PLSMCMetricsAgent setLastDisplayAccumulatedSampleEndDate:];
-[PLSMCMetricsAgent anyVirtualTemperatureAboveThreshold];
-[PLSMCMetricsAgent setLuxEntryNotification:];
-[PLSMCMetricsAgent luxEntryNotification];
-[PLSMCMetricsAgent logSMCLookUpTable];
-[PLSMCMetricsAgent loggingCounter];
-[PLSMCMetricsAgent setLoggedInstantKeysArray:];
-[PLSMCMetricsAgent handleNonNumericKeys:keyInfo:];
-[PLSMCMetricsAgent setLoggingThreshold:];
-[PLSMCMetricsAgent setCycleCountInterval:];
-[PLSMCMetricsAgent getAllowedKeys:];
-[PLSMCMetricsAgent getTVKeys];
-[PLSMCMetricsAgent logAccumulatedKeysToPL:ToCA:];
-[PLSMCMetricsAgent getAllKeys];
-[PLSMCMetricsAgent logAccumlatedLookUpTable];
-[PLSMCMetricsAgent accumGaugeArray];
-[PLSMCMetricsAgent logDisplayPower];
-[PLSMCMetricsAgent getAllowedAccumulatedKeys];
-[PLSMCMetricsAgent loggingThreshold];
-[PLSMCMetricsAgent lastDisplayAccumlatedSample];
-[PLSMCMetricsAgent setStateTracker:];
-[PLSMCMetricsAgent setScreenStateNotification:];
-[PLSMCMetricsAgent readAccumSMCKey:toOutput:];
-[PLSMCMetricsAgent setLastAccumlatedSample:];
-[PLSMCMetricsAgent focalAppSwitch];
-[PLSMCMetricsAgent loggedInstantKeysArray];
-[PLSMCMetricsAgent powerDeliveryCallback];
-[PLSMCMetricsAgent setDailyTaskNotification:];
-[PLSMCMetricsAgent setInstantGaugeArray:];
-[PLSMCMetricsAgent setLastDisplayAccumlatedSample:];
-[PLSMCMetricsAgent screenStateNotification];
-[PLSMCMetricsAgent lastFocalSampleDate];
-[PLSMCMetricsAgent isThermalMitigationAboveThreshold];
-[PLSMCMetricsAgent monitorCadence];
-[PLSMCMetricsAgent setLastAccumlatedSampleCA:];
-[PLSMCMetricsAgent loggedPowerDeliveryKeysArray];
-[PLSMCMetricsAgent writeSMCKey:withValue:];
-[PLSMCMetricsAgent smcConnection];
-[PLSMCMetricsAgent setSbc:];
-[PLSMCMetricsAgent getOSAccumListFrom:];
-[PLSMCMetricsAgent currentLux];
-[PLSMCMetricsAgent lastAccumlatedSample];
-[PLSMCMetricsAgent setFocalAppSwitch:];
-[PLSMCMetricsAgent log];
-[PLSMCMetricsAgent cycleCountInterval];
-[PLSMCMetricsAgent sbc];
-[PLSMCMetricsAgent setPowerDeliveryCounter:];
-[PLSMCMetricsAgent logThermalKeysToCoreAnalytics];
-[PLSMCMetricsAgent lastDisplayAccumulatedSampleEndDate];
-[PLSMCMetricsAgent getValueFromAccumSample:lastSample:];
-[PLSMCMetricsAgent lastAccumlatedSampleCA];
-[PLSMCMetricsAgent dailyTaskNotification];
-[PLSMCMetricsAgent powerDeliveryCounter];
-[PLSMCMetricsAgent monitorTimer];
-[PLSMCMetricsAgent instantGaugeArray];
-[PLSMCMetricsAgent handleNumericKeys:keyInfo:keyName:ret:];
-[PLSMCMetricsAgent getAllowedPowerDeliveryKeys];
```
