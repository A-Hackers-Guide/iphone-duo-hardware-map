# `PLASMetric`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
s _metricType;
@"NSString" _metricKey;
@"NSArray" _metricProperties;
@? _query;
@? _summarizer;
```

## Properties

```
@property (T@"NSString",&,V_metricKey) metricKey;
@property (Ts,V_metricType) metricType;
@property (T@"NSArray",&,V_metricProperties) metricProperties;
@property (T@?,C,V_query) query;
@property (T@?,C,V_summarizer) summarizer;
```

## Instance methods

```
-[PLASMetric setMetricType:];
-[PLASMetric metricType];
-[PLASMetric setQuery:];
-[PLASMetric query];
-[PLASMetric initMetric:withType:withProperties:withQuery:andSummarizerBlock:];
-[PLASMetric metricKey];
-[PLASMetric metricProperties];
-[PLASMetric setMetricKey:];
-[PLASMetric setMetricProperties:];
-[PLASMetric setSummarizer:];
-[PLASMetric summarizer];
```
