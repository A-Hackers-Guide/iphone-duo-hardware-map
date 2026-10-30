# `WiFiScanStatisticsAggregator`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _aggregator;
@"NSDate" _lastSubmissionTime;
@"NSObject<OS_dispatch_queue>" _internalQueue;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_aggregator) aggregator;
@property (T@"NSDate",&,N,V_lastSubmissionTime) lastSubmissionTime;
@property (T@"NSObject<OS_dispatch_queue>",&,V_internalQueue) internalQueue;
```

## Instance methods

```
-[WiFiScanStatisticsAggregator init];
-[WiFiScanStatisticsAggregator setLastSubmissionTime:];
-[WiFiScanStatisticsAggregator setInternalQueue:];
-[WiFiScanStatisticsAggregator lastSubmissionTime];
-[WiFiScanStatisticsAggregator canSubmitToCA:];
-[WiFiScanStatisticsAggregator internalQueue];
-[WiFiScanStatisticsAggregator aggregator];
-[WiFiScanStatisticsAggregator aggregateClientMetrics:];
-[WiFiScanStatisticsAggregator setAggregator:];
```
