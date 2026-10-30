# `AVTelemetryMonitor`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
^{?=iiiiiiiiiiii} _allAggregratedCount;
@"NSString" _applicationIdentifier;
@"NSObject<OS_dispatch_queue>" _queueCAEvents;
@"NSObject<OS_dispatch_source>" _timerCAEvents;
B _timerActivated;
```

## Class methods

```
+[AVTelemetryMonitor shared];
```

## Instance methods

```
-[AVTelemetryMonitor init];
-[AVTelemetryMonitor dealloc];
-[AVTelemetryMonitor reportAllAggregatedCounts];
-[AVTelemetryMonitor incrementBucketCount:executionTime:];
```
