# `WADeviceAnalytics_UsageStats`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
s _latestCompleteWeekUsageCumulativePercentage;
s _latestCompleteWeekUsagePercentage;
q _latestCompleteWeekUsageCumulativeSeconds;
q _latestCompleteWeekUsageSeconds;
```

## Properties

```
@property (Ts,N,V_latestCompleteWeekUsageCumulativePercentage) latestCompleteWeekUsageCumulativePercentage;
@property (Tq,N,V_latestCompleteWeekUsageCumulativeSeconds) latestCompleteWeekUsageCumulativeSeconds;
@property (Ts,N,V_latestCompleteWeekUsagePercentage) latestCompleteWeekUsagePercentage;
@property (Tq,N,V_latestCompleteWeekUsageSeconds) latestCompleteWeekUsageSeconds;
```

## Instance methods

```
-[WADeviceAnalytics_UsageStats description];
-[WADeviceAnalytics_UsageStats initWithUniqueMO:];
-[WADeviceAnalytics_UsageStats latestCompleteWeekUsageCumulativePercentage];
-[WADeviceAnalytics_UsageStats latestCompleteWeekUsageCumulativeSeconds];
-[WADeviceAnalytics_UsageStats latestCompleteWeekUsagePercentage];
-[WADeviceAnalytics_UsageStats latestCompleteWeekUsageSeconds];
-[WADeviceAnalytics_UsageStats setLatestCompleteWeekUsageCumulativePercentage:];
-[WADeviceAnalytics_UsageStats setLatestCompleteWeekUsageCumulativeSeconds:];
-[WADeviceAnalytics_UsageStats setLatestCompleteWeekUsagePercentage:];
-[WADeviceAnalytics_UsageStats setLatestCompleteWeekUsageSeconds:];
```
