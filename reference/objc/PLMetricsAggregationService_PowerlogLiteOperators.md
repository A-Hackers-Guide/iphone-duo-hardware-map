# `PLMetricsAggregationService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 9 instance variables, 9 properties, 25 instance methods, 3 class methods

## Instance variables

```
@"PLCFNotificationOperatorComposition" _aggregateMetricsListener;
@"PLCFNotificationOperatorComposition" _aggregateMetricsForceListener;
@"PLCFNotificationOperatorComposition" _aggregateMetricsTodayListener;
@"PLCFNotificationOperatorComposition" _aggregateMetricsTodayForceListener;
@"PLCFNotificationOperatorComposition" _aggregateMetrics24hrsListener;
@"PLCFNotificationOperatorComposition" _aggregateMetrics24hrsForceListener;
@"PLCFNotificationOperatorComposition" _aggregateMetrics1hrListener;
@"PLCFNotificationOperatorComposition" _aggregateMetrics1hrForceListener;
@"PLXPCResponderOperatorComposition" _metricSummarizationStateResponder;
```

## Properties

```
@property (T@"PLCFNotificationOperatorComposition",&,V_aggregateMetricsListener) aggregateMetricsListener;
@property (T@"PLCFNotificationOperatorComposition",&,V_aggregateMetricsForceListener) aggregateMetricsForceListener;
@property (T@"PLCFNotificationOperatorComposition",&,V_aggregateMetricsTodayListener) aggregateMetricsTodayListener;
@property (T@"PLCFNotificationOperatorComposition",&,V_aggregateMetricsTodayForceListener) aggregateMetricsTodayForceListener;
@property (T@"PLCFNotificationOperatorComposition",&,V_aggregateMetrics24hrsListener) aggregateMetrics24hrsListener;
@property (T@"PLCFNotificationOperatorComposition",&,V_aggregateMetrics24hrsForceListener) aggregateMetrics24hrsForceListener;
@property (T@"PLCFNotificationOperatorComposition",&,V_aggregateMetrics1hrListener) aggregateMetrics1hrListener;
@property (T@"PLCFNotificationOperatorComposition",&,V_aggregateMetrics1hrForceListener) aggregateMetrics1hrForceListener;
@property (T@"PLXPCResponderOperatorComposition",&,V_metricSummarizationStateResponder) metricSummarizationStateResponder;
```

## Class methods

```
+[PLMetricsAggregationService load];
+[PLMetricsAggregationService defaults];
+[PLMetricsAggregationService metrickitClientsAvailable];
```

## Instance methods

```
-[PLMetricsAggregationService init];
-[PLMetricsAggregationService initOperatorDependancies];
-[PLMetricsAggregationService setAggregateMetrics1hrListener:];
-[PLMetricsAggregationService aggregateMetrics1hrForceListener];
-[PLMetricsAggregationService aggregateMetrics1hrListener];
-[PLMetricsAggregationService aggregateMetrics24hrsForceListener];
-[PLMetricsAggregationService aggregateMetrics24hrsListener];
-[PLMetricsAggregationService aggregateMetricsForceListener];
-[PLMetricsAggregationService aggregateMetricsListener];
-[PLMetricsAggregationService aggregateMetricsTodayForceListener];
-[PLMetricsAggregationService aggregateMetricsTodayListener];
-[PLMetricsAggregationService createMetricsFile:];
-[PLMetricsAggregationService logEventNoneSessionsFile];
-[PLMetricsAggregationService metricSummarizationStateResponder];
-[PLMetricsAggregationService setAggregateMetrics1hrForceListener:];
-[PLMetricsAggregationService setAggregateMetrics24hrsForceListener:];
-[PLMetricsAggregationService setAggregateMetrics24hrsListener:];
-[PLMetricsAggregationService setAggregateMetricsForceListener:];
-[PLMetricsAggregationService setAggregateMetricsListener:];
-[PLMetricsAggregationService setAggregateMetricsTodayForceListener:];
-[PLMetricsAggregationService setAggregateMetricsTodayListener:];
-[PLMetricsAggregationService setMetricSummarizationStateResponder:];
-[PLMetricsAggregationService setupMetricsAggregation];
-[PLMetricsAggregationService setupMetricsListeners];
-[PLMetricsAggregationService toggleMetricsAggregation:];
```
