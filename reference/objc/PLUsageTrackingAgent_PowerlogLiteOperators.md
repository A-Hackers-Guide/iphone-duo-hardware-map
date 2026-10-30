# `PLUsageTrackingAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 1 instance variables, 1 properties, 8 instance methods, 9 class methods

## Instance variables

```
@"USUsageReporter" _usageReporter;
```

## Properties

```
@property (T@"USUsageReporter",&,V_usageReporter) usageReporter;
```

## Class methods

```
+[PLUsageTrackingAgent entryEventIntervalDefinitions];
+[PLUsageTrackingAgent entryEventPointDefinitions];
+[PLUsageTrackingAgent entryEventForwardDefinitions];
+[PLUsageTrackingAgent entryEventBackwardDefinitions];
+[PLUsageTrackingAgent entryEventNoneDefinitions];
+[PLUsageTrackingAgent load];
+[PLUsageTrackingAgent defaults];
+[PLUsageTrackingAgent entryAggregateDefinitions];
+[PLUsageTrackingAgent entryEventIntervalDefinitionUsageTime];
```

## Instance methods

```
-[PLUsageTrackingAgent init];
-[PLUsageTrackingAgent initOperatorDependancies];
-[PLUsageTrackingAgent initTaskOperatorDependancies];
-[PLUsageTrackingAgent log];
-[PLUsageTrackingAgent logEntriesFromUsageReports:];
-[PLUsageTrackingAgent logEventIntervalUsageTime];
-[PLUsageTrackingAgent setUsageReporter:];
-[PLUsageTrackingAgent usageReporter];
```
