# `PLMonotonicTimer`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 22 instance methods, 3 class methods

## Instance variables

```
@"NSDate" _monotonicFireDate;
d _interval;
@"NSObject<OS_dispatch_queue>" _queue;
@? _block;
@"NSMutableSet" _canceledFireDates;
@"PLEntryNotificationOperatorComposition" _wakeEntryNotification;
```

## Properties

```
@property (Td,V_interval) interval;
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (T@?,C,V_block) block;
@property (T@"NSMutableSet",&,V_canceledFireDates) canceledFireDates;
@property (T@"PLEntryNotificationOperatorComposition",&,V_wakeEntryNotification) wakeEntryNotification;
@property (T@"NSDate",&,N,V_monotonicFireDate) monotonicFireDate;
```

## Class methods

```
+[PLMonotonicTimer debugInstance];
+[PLMonotonicTimer debugScheduledTimerWithMonotonicFireDate:withInterval:withQueue:withBlock:];
+[PLMonotonicTimer scheduledTimerWithMonotonicFireDate:withInterval:withQueue:withBlock:];
```

## Instance methods

```
-[PLMonotonicTimer fire];
-[PLMonotonicTimer block];
-[PLMonotonicTimer setInterval:];
-[PLMonotonicTimer interval];
-[PLMonotonicTimer setBlock:];
-[PLMonotonicTimer dealloc];
-[PLMonotonicTimer wakeEntryNotification];
-[PLMonotonicTimer queue];
-[PLMonotonicTimer _cancel];
-[PLMonotonicTimer setWakeEntryNotification:];
-[PLMonotonicTimer description];
-[PLMonotonicTimer cancel];
-[PLMonotonicTimer setQueue:];
-[PLMonotonicTimer schedule];
-[PLMonotonicTimer reschedule];
-[PLMonotonicTimer timerFiredForMonotonicFireDate:];
-[PLMonotonicTimer _setMonotonicFireDate:];
-[PLMonotonicTimer canceledFireDates];
-[PLMonotonicTimer initWithMonotonicFireDate:withInterval:withQueue:withBlock:];
-[PLMonotonicTimer monotonicFireDate];
-[PLMonotonicTimer setCanceledFireDates:];
-[PLMonotonicTimer setMonotonicFireDate:];
```
