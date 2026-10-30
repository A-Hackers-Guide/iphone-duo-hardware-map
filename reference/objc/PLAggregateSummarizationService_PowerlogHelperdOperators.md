# `PLAggregateSummarizationService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 6 instance variables, 6 properties, 56 instance methods, 7 class methods

## Instance variables

```
B _gmsOptInState;
@"NSMutableDictionary" _summarizedData;
@"NSMutableArray" _metrics;
@"NSArray" _appList;
d _maxTimestamp;
@"PLXPCResponderOperatorComposition" _aggregationResponder;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_summarizedData) summarizedData;
@property (T@"NSMutableArray",&,V_metrics) metrics;
@property (T@"NSArray",&,V_appList) appList;
@property (Td,V_maxTimestamp) maxTimestamp;
@property (TB,V_gmsOptInState) gmsOptInState;
@property (T@"PLXPCResponderOperatorComposition",&,V_aggregationResponder) aggregationResponder;
```

## Class methods

```
+[PLAggregateSummarizationService entryEventPointDefinitions];
+[PLAggregateSummarizationService load];
+[PLAggregateSummarizationService osVersion];
+[PLAggregateSummarizationService modelIdentifier];
+[PLAggregateSummarizationService entryAggregateDefinitions];
+[PLAggregateSummarizationService buildType];
+[PLAggregateSummarizationService roundToSignificantDigits:sigDigs:];
```

## Instance methods

```
-[PLAggregateSummarizationService setMetrics:];
-[PLAggregateSummarizationService aggregateMetrics];
-[PLAggregateSummarizationService init];
-[PLAggregateSummarizationService initOperatorDependancies];
-[PLAggregateSummarizationService metrics];
-[PLAggregateSummarizationService setupMetrics];
-[PLAggregateSummarizationService maxTimestamp];
-[PLAggregateSummarizationService getRawAppTimeEntriesForEndTime:];
-[PLAggregateSummarizationService appList];
-[PLAggregateSummarizationService _normalizeChunkMetrics:withSummarizedData:properties:];
-[PLAggregateSummarizationService addMetrics:withType:];
-[PLAggregateSummarizationService aggregateAllMetricsByChunkIntervals:rawAppTimeEntries:rawLocationIntervals:rawCellularConditionEntries:];
-[PLAggregateSummarizationService aggregateAppRunTimeByChunkIntervalsFromRawEntries:startTime:];
-[PLAggregateSummarizationService aggregateCellularConditionByChunkIntervalsFromRawEntries:startTime:];
-[PLAggregateSummarizationService aggregateCoalitionMetricsByChunkIntervalsWithCTE:startTime:endTime:];
-[PLAggregateSummarizationService aggregateDiskIOByChunkIntervalsWithCTE:startTime:endTime:];
-[PLAggregateSummarizationService aggregateDisplayAPLByChunkIntervalsWithCTE:startTime:endTime:];
-[PLAggregateSummarizationService aggregateLocationActivityByChunkIntervalsFromRawEntries:startTime:];
-[PLAggregateSummarizationService aggregateMemoryByChunkIntervalsWithCTE:startTime:endTime:];
-[PLAggregateSummarizationService aggregateNetworkIOByChunkIntervalsWithCTE:startTime:endTime:];
-[PLAggregateSummarizationService aggregationResponder];
-[PLAggregateSummarizationService chunkCTEForEndTime:];
-[PLAggregateSummarizationService getAppList:];
-[PLAggregateSummarizationService getAppMetadata];
-[PLAggregateSummarizationService getAppMultipleVersionsData];
-[PLAggregateSummarizationService getCellularConditionSummarizer];
-[PLAggregateSummarizationService getDeviceMetadataInRange:withSignpostData:];
-[PLAggregateSummarizationService getDrainInfoInRange:];
-[PLAggregateSummarizationService getGenericSummarizer];
-[PLAggregateSummarizationService getInitCountInRange:];
-[PLAggregateSummarizationService getLocationActivitySummarizer];
-[PLAggregateSummarizationService getPluggedInDurationInRange:];
-[PLAggregateSummarizationService getQueryForAppMultipleVersions];
-[PLAggregateSummarizationService getQueryForAverageMemory];
-[PLAggregateSummarizationService getQueryForCellularCondition];
-[PLAggregateSummarizationService getQueryForCoalitionPowerData];
-[PLAggregateSummarizationService getQueryForDiskIO];
-[PLAggregateSummarizationService getQueryForDisplayAPL:];
-[PLAggregateSummarizationService getQueryForLocationActivity];
-[PLAggregateSummarizationService getQueryForNetworkIOData];
-[PLAggregateSummarizationService getQueryForPeakMemory];
-[PLAggregateSummarizationService getQueryForStorageConsumption];
-[PLAggregateSummarizationService getRawCellularConditionEntriesForEndTime:];
-[PLAggregateSummarizationService getRawLocationIntervalsForEndTime:];
-[PLAggregateSummarizationService gmsOptInState];
-[PLAggregateSummarizationService handleAggregationQueryWithPayload:];
-[PLAggregateSummarizationService preformatMetricsForFormatter:];
-[PLAggregateSummarizationService rekeyCompositeKey:withProcessNameToBundleID:];
-[PLAggregateSummarizationService rekeySignpostData:withProcessNameToBundleID:];
-[PLAggregateSummarizationService resolveUnresolvedBundleIDsInStateIntervals:processNameToBundleID:];
-[PLAggregateSummarizationService setAggregationResponder:];
-[PLAggregateSummarizationService setAppList:];
-[PLAggregateSummarizationService setGmsOptInState:];
-[PLAggregateSummarizationService setMaxTimestamp:];
-[PLAggregateSummarizationService setSummarizedData:];
-[PLAggregateSummarizationService summarizedData];
```
