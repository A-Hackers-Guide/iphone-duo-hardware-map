# `HIDAnalyticsReporter`

- Image: [`/System/Library/PrivateFrameworks/HIDAnalytics.framework/HIDAnalytics`](../userland/System__Library__PrivateFrameworks__HIDAnalytics.framework__HIDAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _events;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_source>" _timer;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Instance methods

```
-[HIDAnalyticsReporter init];
-[HIDAnalyticsReporter stop];
-[HIDAnalyticsReporter dealloc];
-[HIDAnalyticsReporter start];
-[HIDAnalyticsReporter logAnalyticsEvent:];
-[HIDAnalyticsReporter registerEvent:];
-[HIDAnalyticsReporter createBucketData:fieldvalue:fieldDescription:];
-[HIDAnalyticsReporter dispatchAnalyticsForEvent:];
-[HIDAnalyticsReporter logAnalyticsEvent:eventDescription:eventValue:];
-[HIDAnalyticsReporter unregisterEvent:];
```
