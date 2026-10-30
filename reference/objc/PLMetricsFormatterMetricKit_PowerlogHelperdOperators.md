# `PLMetricsFormatterMetricKit`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 38 instance methods, 3 class methods

## Instance variables

```
B _processHangs;
```

## Properties

```
@property (TB,V_processHangs) processHangs;
```

## Class methods

```
+[PLMetricsFormatterMetricKit _decodeExitWithDomain:withCode:];
+[PLMetricsFormatterMetricKit _parseCompositeSBCKey:intoBundleID:sbcIndex:];
+[PLMetricsFormatterMetricKit categorizeAppExits:];
```

## Instance methods

```
-[PLMetricsFormatterMetricKit init];
-[PLMetricsFormatterMetricKit _addExitMetrics:toStateMetrics:];
-[PLMetricsFormatterMetricKit _filterAppTimeEntries:byStates:];
-[PLMetricsFormatterMetricKit _addCellularConditionMetrics:withEventLevelData:];
-[PLMetricsFormatterMetricKit _addCumulativeMetricsToUnattributed:fromAppData:];
-[PLMetricsFormatterMetricKit _addSignpostMetricsFromContextualizedData:toStateMetrics:];
-[PLMetricsFormatterMetricKit _addSignpostOnlyAppsToPayload:withStateIntervals:withSignpostData:forDate:];
-[PLMetricsFormatterMetricKit _constructSignpostMetricsFromStateData:];
-[PLMetricsFormatterMetricKit _createActiveStatesForChunk:fromStatesData:bundleID:];
-[PLMetricsFormatterMetricKit _createEmptyIntervalMetricDataWithDuration:activeStates:];
-[PLMetricsFormatterMetricKit _createIntervalMetricDataWithStartTimestamp:endTimestamp:durationSeconds:intervalMetrics:activeStates:];
-[PLMetricsFormatterMetricKit _createStateMetricDataWithDomain:label:durationSeconds:stableStateContext:stateMetrics:appData:isUnattributed:];
-[PLMetricsFormatterMetricKit _enrichPayload:withStateIntervals:withSignpostData:rawAppTimeEntries:rawLocationIntervals:rawCellularConditionEntries:];
-[PLMetricsFormatterMetricKit _filterCellularConditionEntries:byStates:];
-[PLMetricsFormatterMetricKit _filterLocationIntervals:byStates:];
-[PLMetricsFormatterMetricKit _groupEntriesByBundleID:];
-[PLMetricsFormatterMetricKit _locationAccuracyKeyForValue:];
-[PLMetricsFormatterMetricKit _overrideAppTimeMetrics:withEventLevelData:];
-[PLMetricsFormatterMetricKit _overrideLocationMetrics:withEventLevelData:];
-[PLMetricsFormatterMetricKit addBucketWithDuration:WithEnd:andCount:toList:];
-[PLMetricsFormatterMetricKit addBucketWithSignalBar:withTime:toList:];
-[PLMetricsFormatterMetricKit addPerfMetrics:toAppData:];
-[PLMetricsFormatterMetricKit addPowerMetrics:toAppData:];
-[PLMetricsFormatterMetricKit addSignpostData:forApp:toAppData:];
-[PLMetricsFormatterMetricKit addTelemetryForMetricInconsistencies:];
-[PLMetricsFormatterMetricKit analyticsLogSignpostsWithBundleId:withName:withCategory:withMetrics:];
-[PLMetricsFormatterMetricKit computeBucketEndWithDuration:andValue:];
-[PLMetricsFormatterMetricKit constructCellularData:];
-[PLMetricsFormatterMetricKit constructCellularHistogram:];
-[PLMetricsFormatterMetricKit constructHistogramBucketsWithDuration:andData:];
-[PLMetricsFormatterMetricKit constructPayloadWithMetrics:andSignpostData:forDate:];
-[PLMetricsFormatterMetricKit constructSignpostIntervalDataWithDurations:withMetrics:];
-[PLMetricsFormatterMetricKit enrichPayloadWithChunkIntervals:withSignpostData:];
-[PLMetricsFormatterMetricKit hangtracerEnabled:];
-[PLMetricsFormatterMetricKit normalizeCellularData:];
-[PLMetricsFormatterMetricKit processHangs];
-[PLMetricsFormatterMetricKit publishMetrics:andSignpostData:stateIntervals:rawAppTimeEntries:rawLocationIntervals:rawCellularConditionEntries:forDate:];
-[PLMetricsFormatterMetricKit setProcessHangs:];
```
