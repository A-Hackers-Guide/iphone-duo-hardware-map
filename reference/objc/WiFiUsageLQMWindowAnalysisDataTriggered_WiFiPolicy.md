# `WiFiUsageLQMWindowAnalysisDataTriggered`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageLQMWindowAnalysis`
- 2 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _triggerCriteriaList;
@"NSString" _dataTriggerReason;
```

## Properties

```
@property (T@"NSString",&,N,V_dataTriggerReason) dataTriggerReason;
@property (T@"NSArray",R,N,V_triggerCriteriaList) triggerCriteriaList;
```

## Instance methods

```
-[WiFiUsageLQMWindowAnalysisDataTriggered addDimensionsTo:];
-[WiFiUsageLQMWindowAnalysisDataTriggered performAnalysis];
-[WiFiUsageLQMWindowAnalysisDataTriggered dataTriggerReason];
-[WiFiUsageLQMWindowAnalysisDataTriggered initWithRollingWindow:andSubReason:andContext:andTimestamp:onQueue:];
-[WiFiUsageLQMWindowAnalysisDataTriggered setDataTriggerReason:];
-[WiFiUsageLQMWindowAnalysisDataTriggered triggerCriteriaList];
```
