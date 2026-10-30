# `CBAnalyticsExtDisplayManager`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 14 instance methods, 4 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_source>" _reportTimer;
@"NSMutableDictionary" _timestamps;
@"NSMutableDictionary" samples;
B _userActive;
```

## Class methods

```
+[CBAnalyticsExtDisplayManager sharedInstance];
+[CBAnalyticsExtDisplayManager handleColorSample:];
+[CBAnalyticsExtDisplayManager sendEventOnceADayLazy:andDict:];
+[CBAnalyticsExtDisplayManager stopReporting:];
```

## Instance methods

```
-[CBAnalyticsExtDisplayManager init];
-[CBAnalyticsExtDisplayManager dealloc];
-[CBAnalyticsExtDisplayManager setUserActive:];
-[CBAnalyticsExtDisplayManager stringForType:];
-[CBAnalyticsExtDisplayManager handleColorSampleInternal:];
-[CBAnalyticsExtDisplayManager isFirstEventToday:];
-[CBAnalyticsExtDisplayManager isSameDay:asDay:];
-[CBAnalyticsExtDisplayManager logAllColorSamples];
-[CBAnalyticsExtDisplayManager logColorSample:withType:];
-[CBAnalyticsExtDisplayManager sendEventLazy:andDict:];
-[CBAnalyticsExtDisplayManager sendEventOnceADayLazyInternal:andDict:];
-[CBAnalyticsExtDisplayManager startReporting];
-[CBAnalyticsExtDisplayManager stopReportingInternal:];
-[CBAnalyticsExtDisplayManager storeTimestamp:forEventName:];
```
