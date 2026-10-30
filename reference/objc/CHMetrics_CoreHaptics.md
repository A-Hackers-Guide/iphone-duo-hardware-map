# `CHMetrics`

- Image: [`/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`](../userland/System__Library__Frameworks__CoreHaptics.framework__CoreHaptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 0 properties, 42 instance methods, 7 class methods

## Instance variables

```
q _reporterID;
@"NSString" _engineID;
I _audioSessionID;
B _sessionIsShared;
B _isSPI;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
f _CHMetricsIntensityBin1To2Value;
f _CHMetricsIntensityBin2To3Value;
{vector<unsigned long, std::allocator<unsigned long>>="__begin_"^Q"__end_"^Q""{?="__cap_"^Q}} _hapticTransientIDs;
{vector<unsigned long, std::allocator<unsigned long>>="__begin_"^Q"__end_"^Q""{?="__cap_"^Q}} _hapticContinuousSustainedIDs;
{vector<unsigned long, std::allocator<unsigned long>>="__begin_"^Q"__end_"^Q""{?="__cap_"^Q}} _hapticContinuousNonsustainedIDs;
{unordered_map<AVHapticPlayerEventType, NSString *, std::hash<AVHapticPlayerEventType>, std::equal_to<AVHapticPlayerEventType>, std::allocator<std::pair<const AVHapticPlayerEventType, NSString *>>>="__table_"{__hash_table<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, std::__unordered_map_hasher<AVHapticPlayerEventType, std::pair<const AVHapticPlayerEventType, NSString *>, std::hash<AVHapticPlayerEventType>, std::equal_to<AVHapticPlayerEventType>>, std::__unordered_map_equal<AVHapticPlayerEventType, std::pair<const AVHapticPlayerEventType, NSString *>, std::equal_to<AVHapticPlayerEventType>, std::hash<AVHapticPlayerEventType>>, std::allocator<std::pair<const AVHapticPlayerEventType, NSString *>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<AVHapticPlayerEventType, NSString *>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _legacyHapticTransientEventTypeMap;
@"NSMutableDictionary" _playerData;
@"NSMutableDictionary" _patternLibraryData;
B _retainDataForTesting;
@"NSMutableDictionary" _dataForTesting;
```

## Class methods

```
+[CHMetrics handleError:];
+[CHMetrics sharedReporter];
+[CHMetrics currentTime];
+[CHMetrics SelectedErrorsMap];
+[CHMetrics CreateReporterWithServiceType:];
+[CHMetrics sharedReporterQueue];
+[CHMetrics doHandleErrorCode:description:];
```

## Instance methods

```
-[CHMetrics setReporter];
-[CHMetrics initWithEngine:audioSessionID:sessionIsShared:isSPI:];
-[CHMetrics sendDetailedMetricsForPlayerID:endTime:];
-[CHMetrics retainData:forTestingPlayer:];
-[CHMetrics startReporter];
-[CHMetrics handleStartForPlayer:time:isAdvanced:patternID:];
-[CHMetrics preparePlaybackData:events:];
-[CHMetrics getIDForPlayer:];
-[CHMetrics handleEngineStop];
-[CHMetrics stopReporter];
-[CHMetrics handleServerRecovery];
-[CHMetrics handleInitForPlayer:events:isAdvanced:patternID:];
-[CHMetrics dealloc];
-[CHMetrics markAdvancedPlaybackAction:action:time:];
-[CHMetrics handleParamCurveEncountered];
-[CHMetrics removePlaybackData:];
-[CHMetrics isEnabled];
-[CHMetrics continousDictionary:slot:intensity:];
-[CHMetrics handleActionForPlayer:action:time:isAdvanced:];
-[CHMetrics legacyTransientDictionary:eventType:intensity:];
-[CHMetrics handleFinishedForPlayersAtTime:];
-[CHMetrics getLoopsForPlayer:endTime:];
-[CHMetrics setMetricsTestModeEnabled];
-[CHMetrics getLoopsForAdvancedPlayer:endTime:];
-[CHMetrics addPatternLibraryMetric:];
-[CHMetrics getMetricsForPlayer:];
-[CHMetrics markPlaybackAction:action:time:];
-[CHMetrics handleEngineStart];
-[CHMetrics logMetric:value:];
-[CHMetrics sendPatternLibraryMetrics];
-[CHMetrics logPatternLibraryMetric:];
-[CHMetrics resetAdvancedPlaybackData:];
-[CHMetrics logPowerLogMetric:];
-[CHMetrics continuousSharpnessSlotKeyFromSlotValue:];
-[CHMetrics intensityBinKeyFromValue:];
-[CHMetrics prepareAdvancedPlaybackData:events:];
-[CHMetrics transientSharpnessIndexKeyFromIndexValue:];
-[CHMetrics prepareData:events:];
-[CHMetrics transientDictionary:index:intensity:];
-[CHMetrics dispatchOnLocal:];
-[CHMetrics isEventType:inList:];
-[CHMetrics resetPlaybackData:];
```
